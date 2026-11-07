#!/usr/bin/env python3
"""add-benchmark-learning-outcomes.py - insert a "learningOutcome" field into
each capability's two from-benchmark genericOutcomes entries (conceptual +
applied) in catalogue/context/pathway-evidence/<pathway>.json.

Inputs: /tmp/learning-outcome-outputs/<pathway>.json (authored by the parallel
authoring agents; see tools/extract-benchmark-outcome-inputs.py for the input
packets they worked from). Shape: {"pathway": ..., "capabilities": [{
"capability": <ref>, "learningOutcomes": {"conceptual": <str>, "applied": <str>}}, ...]}.

Insertion is surgical, not a whole-document reserialisation, for the same
reason as tools/merge-generic-outcomes.py: some pathway-evidence files use
different pre-existing pretty-printing for short arrays, and a whole-document
parse-and-redump would silently renormalise that. Instead this finds each
capability's genericOutcomes array, locates the from-benchmark/<kind> entry by
depth-aware, string-aware scanning, and inserts a new "learningOutcome" key
immediately after "title", formatted at the same indentation, with untouched
bytes either side. An entry already carrying "learningOutcome" is left
untouched (idempotent).

Safety: before writing, the untouched parts of the new text are diffed
against the original to confirm nothing outside the inserted spans changed.

Run from the repo root:
    python tools/add-benchmark-learning-outcomes.py              # all 13 pathways
    python tools/add-benchmark-learning-outcomes.py criticality   # one or more
"""
import glob, json, os, sys
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import pathway_tiers

EVIDENCE_DIR = os.path.join(pathway_tiers.REPO_ROOT, 'catalogue', 'context', 'pathway-evidence')
OUTPUT_DIR = '/tmp/learning-outcome-outputs'


def _scan_objects(text, start, stop_char):
    """[(start, end)] spans of each top-level {...} object between start and
    the first stop_char at depth 0, string-aware."""
    i = start
    n = len(text)
    spans = []
    in_string = False
    escape = False
    depth = 0
    obj_start = None
    while i < n:
        c = text[i]
        if in_string:
            if escape:
                escape = False
            elif c == '\\':
                escape = True
            elif c == '"':
                in_string = False
        else:
            if c == '"':
                in_string = True
            elif c == '{':
                if depth == 0:
                    obj_start = i
                depth += 1
            elif c == '}':
                depth -= 1
                if depth == 0:
                    spans.append((obj_start, i + 1))
            elif c == stop_char and depth == 0:
                break
        i += 1
    return spans, i


def find_capability_spans(text):
    key = '"capabilities"'
    k = text.index(key)
    arr_start = text.index('[', k)
    spans, _ = _scan_objects(text, arr_start + 1, ']')
    return spans


def find_generic_outcomes_entry_spans(obj_text):
    """[(start, end)] spans of each entry object inside this capability's
    "genericOutcomes" array. Returns [] if the capability has no
    genericOutcomes key (should not happen post earlier merge)."""
    key = '"genericOutcomes"'
    if key not in obj_text:
        return []
    k = obj_text.index(key)
    arr_start = obj_text.index('[', k)
    spans, _ = _scan_objects(obj_text, arr_start + 1, ']')
    return spans


def indent_of_key(obj_text, key):
    k = obj_text.index('"' + key + '"')
    line_start = obj_text.rfind('\n', 0, k) + 1
    return obj_text[line_start:k]


def find_title_close(entry_text):
    """Offset just after the closing quote of the "title" string value."""
    key = '"title"'
    k = entry_text.index(key)
    colon = entry_text.index(':', k + len(key))
    i = colon + 1
    n = len(entry_text)
    while entry_text[i] != '"':
        i += 1
    i += 1  # past opening quote
    escape = False
    while i < n:
        c = entry_text[i]
        if escape:
            escape = False
        elif c == '\\':
            escape = True
        elif c == '"':
            return i + 1
        i += 1
    raise ValueError('unterminated title string')


def build_insertion(text, base_indent):
    return ',\n' + base_indent + '"learningOutcome": ' + json.dumps(text, ensure_ascii=False)


def merge_one(pid):
    ev_path = os.path.join(EVIDENCE_DIR, pid + '.json')
    out_path = os.path.join(OUTPUT_DIR, pid + '.json')
    text = open(ev_path, encoding='utf-8').read()
    doc = json.loads(text)
    authored = json.load(open(out_path, encoding='utf-8'))
    by_ref = {c['capability']: c['learningOutcomes'] for c in authored['capabilities']}

    cap_refs_in_order = [c['capability'] for c in doc['capabilities']]
    spans = find_capability_spans(text)
    if len(spans) != len(cap_refs_in_order):
        raise ValueError('%s: found %d capability spans, expected %d' % (pid, len(spans), len(cap_refs_in_order)))

    inserts = []
    for ref, (cap_start, cap_end) in zip(cap_refs_in_order, spans):
        if ref not in by_ref:
            raise ValueError('%s: no authored learningOutcomes for %s' % (pid, ref))
        cap_text = text[cap_start:cap_end]
        entry_spans = find_generic_outcomes_entry_spans(cap_text)
        if len(entry_spans) != 4:
            raise ValueError('%s %s: expected 4 genericOutcomes entries, found %d' % (pid, ref, len(entry_spans)))
        for e_start, e_end in entry_spans:
            entry_text = cap_text[e_start:e_end]
            if '"origin": "from-benchmark"' not in entry_text:
                continue
            if '"learningOutcome"' in entry_text:
                continue  # already merged, idempotent
            kind = 'conceptual' if '"kind": "conceptual"' in entry_text else 'applied'
            close_off = find_title_close(entry_text)
            insert_pos = cap_start + e_start + close_off
            base_indent = indent_of_key(entry_text, 'title')
            insertion = build_insertion(by_ref[ref][kind], base_indent)
            inserts.append((insert_pos, insertion))

    new_text = text
    for pos, insertion in sorted(inserts, key=lambda t: -t[0]):
        new_text = new_text[:pos] + insertion + new_text[pos:]

    check_text = new_text
    for pos, insertion in sorted(inserts, key=lambda t: t[0]):
        assert check_text[pos:pos + len(insertion)] == insertion, \
            '%s: insertion not found when stripping back out' % pid
        check_text = check_text[:pos] + check_text[pos + len(insertion):]
    if check_text != text:
        raise ValueError('%s: stripping the insertions back out does not reproduce the original byte-for-byte' % pid)

    json.loads(new_text)  # must still be valid JSON
    return new_text, len(inserts)


if __name__ == '__main__':
    pids = sys.argv[1:] or sorted(os.path.splitext(os.path.basename(p))[0]
                                  for p in glob.glob(os.path.join(EVIDENCE_DIR, '*.json'))
                                  if not os.path.basename(p).startswith('_'))
    for pid in pids:
        new_text, n = merge_one(pid)
        ev_path = os.path.join(EVIDENCE_DIR, pid + '.json')
        with open(ev_path, 'w', encoding='utf-8') as fh:
            fh.write(new_text)
        print('merged %s: %d learningOutcome entries inserted' % (pid, n))
