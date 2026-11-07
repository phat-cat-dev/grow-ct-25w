#!/usr/bin/env python3
"""merge-generic-outcomes.py - insert the authored genericOutcomes arrays into
catalogue/context/pathway-evidence/<pathway>.json, one capability at a time.

Inputs: /tmp/generic-outcome-outputs/<pathway>.json (authored by the parallel
authoring agents; see tools/extract-generic-outcome-inputs.py for the input
packets they worked from). Shape: {"pathway": ..., "capabilities": [{
"capability": <ref>, "genericOutcomes": [4 entries]}, ...]}.

Insertion is surgical, not a whole-document reserialisation: some
pathway-evidence files already use slightly different pretty-printing for
short arrays (some collapse a 1-2 element "grounding" array onto one line;
others always spread one element per line). A whole-document
parse-and-redump would silently renormalise that pre-existing formatting.
Instead this finds each capability's "evidence": [...] block in the raw text
by depth-aware, string-aware scanning (so literal brackets inside example
text cannot confuse it), and inserts a new "genericOutcomes" key immediately
after it, formatted at the same indentation, with un-touched bytes either
side. A capability already carrying "genericOutcomes" is left untouched.

Safety: before writing, the untouched parts of the new text are diffed
against the original to confirm nothing outside the inserted spans changed.

Run from the repo root:
    python tools/merge-generic-outcomes.py              # all 13 pathways
    python tools/merge-generic-outcomes.py criticality   # one or more
"""
import glob, json, os, sys
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import pathway_tiers

EVIDENCE_DIR = os.path.join(pathway_tiers.REPO_ROOT, 'catalogue', 'context', 'pathway-evidence')
OUTPUT_DIR = '/tmp/generic-outcome-outputs'


def find_capability_spans(text):
    """[(start, end)] character spans of each top-level object inside the
    "capabilities" array, in document order. start/end bracket the object's
    own { ... }, string-aware (so brackets inside string values are ignored).
    """
    key = '"capabilities"'
    k = text.index(key)
    arr_start = text.index('[', k)
    i = arr_start + 1
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
            elif c == ']' and depth == 0:
                break
        i += 1
    return spans


def find_evidence_close(obj_text):
    """Offset (within obj_text) just after the "]" that closes this
    capability's "evidence" array. String-aware, depth-aware.
    """
    key = '"evidence"'
    k = obj_text.index(key)
    arr_start = obj_text.index('[', k)
    i = arr_start + 1
    n = len(obj_text)
    in_string = False
    escape = False
    depth = 1
    while i < n:
        c = obj_text[i]
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
            elif c == '[':
                depth += 1
            elif c == ']':
                depth -= 1
                if depth == 0:
                    return i + 1
        i += 1
    raise ValueError('unbalanced evidence array')


def indent_of_key(obj_text, key):
    k = obj_text.index('"' + key + '"')
    line_start = obj_text.rfind('\n', 0, k) + 1
    return obj_text[line_start:k]


def build_insertion(generic_outcomes, base_indent):
    dumped = json.dumps(generic_outcomes, indent=2, ensure_ascii=False)
    lines = dumped.split('\n')
    reindented = lines[0] + '\n' + '\n'.join(base_indent + l for l in lines[1:])
    return ',\n' + base_indent + '"genericOutcomes": ' + reindented


def merge_one(pid):
    ev_path = os.path.join(EVIDENCE_DIR, pid + '.json')
    out_path = os.path.join(OUTPUT_DIR, pid + '.json')
    text = open(ev_path, encoding='utf-8').read()
    doc = json.loads(text)
    authored = json.load(open(out_path, encoding='utf-8'))
    by_ref = {c['capability']: c['genericOutcomes'] for c in authored['capabilities']}

    cap_refs_in_order = [c['capability'] for c in doc['capabilities']]
    spans = find_capability_spans(text)
    if len(spans) != len(cap_refs_in_order):
        raise ValueError('%s: found %d capability spans, expected %d' % (pid, len(spans), len(cap_refs_in_order)))

    # Walk spans in reverse so earlier offsets stay valid as we insert.
    new_text = text
    inserts = []
    for ref, (start, end) in zip(cap_refs_in_order, spans):
        if ref not in by_ref:
            raise ValueError('%s: no authored genericOutcomes for %s' % (pid, ref))
        obj_text = text[start:end]
        if '"genericOutcomes"' in obj_text:
            continue  # already merged, idempotent
        close_off = find_evidence_close(obj_text)
        insert_pos = start + close_off
        base_indent = indent_of_key(obj_text, 'evidence')
        insertion = build_insertion(by_ref[ref], base_indent)
        inserts.append((insert_pos, insertion))

    for pos, insertion in sorted(inserts, key=lambda t: -t[0]):
        new_text = new_text[:pos] + insertion + new_text[pos:]

    # Safety: confirm every byte outside the inserted spans is untouched, by
    # stripping the insertions back out (smallest offset first, the reverse
    # of the build order) and comparing to the original.
    check_text = new_text
    for pos, insertion in sorted(inserts, key=lambda t: t[0]):
        assert check_text[pos:pos + len(insertion)] == insertion, '%s: insertion not found when stripping back out' % pid
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
        print('merged %s: %d capabilities updated' % (pid, n))
