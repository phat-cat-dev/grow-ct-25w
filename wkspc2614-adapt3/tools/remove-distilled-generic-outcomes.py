#!/usr/bin/env python3
"""remove-distilled-generic-outcomes.py - strip the two distilled-origin entries
from each capability's genericOutcomes array in
catalogue/context/pathway-evidence/<pathway>.json, leaving only the two
from-benchmark entries (conceptual + applied, each with its learningOutcome).

Removal is surgical, not a whole-document reserialisation, for the same reason
as the other tools in this family: a parse-and-redump would silently
renormalise pre-existing pretty-printing elsewhere in the file. Instead this
finds each capability's genericOutcomes array, confirms the expected entry
order (distilled, distilled, from-benchmark, from-benchmark), and deletes the
exact byte range spanning the two distilled entries - from the opening "{" of
the first distilled entry to the opening "{" of the first from-benchmark entry
- leaving the array's own indentation and the from-benchmark entries
untouched.

Safety: after removal, the result must still be valid JSON, each capability
must have exactly 2 genericOutcomes entries (both from-benchmark), and
everything else in the file (evidence[], the from-benchmark entries
themselves) must be byte-identical to before.

Run from the repo root:
    python tools/remove-distilled-generic-outcomes.py              # all 13 pathways
    python tools/remove-distilled-generic-outcomes.py criticality  # one or more
"""
import glob, json, os, sys
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import pathway_tiers

EVIDENCE_DIR = os.path.join(pathway_tiers.REPO_ROOT, 'catalogue', 'context', 'pathway-evidence')


def _scan_objects(text, start, stop_char):
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
    key = '"genericOutcomes"'
    if key not in obj_text:
        return []
    k = obj_text.index(key)
    arr_start = obj_text.index('[', k)
    spans, _ = _scan_objects(obj_text, arr_start + 1, ']')
    return spans


def origin_of(entry_text):
    if '"origin": "distilled"' in entry_text:
        return 'distilled'
    if '"origin": "from-benchmark"' in entry_text:
        return 'from-benchmark'
    raise ValueError('entry has no recognised origin: %r' % entry_text[:80])


def remove_one(pid):
    ev_path = os.path.join(EVIDENCE_DIR, pid + '.json')
    text = open(ev_path, encoding='utf-8').read()
    doc = json.loads(text)

    cap_refs_in_order = [c['capability'] for c in doc['capabilities']]
    spans = find_capability_spans(text)
    if len(spans) != len(cap_refs_in_order):
        raise ValueError('%s: found %d capability spans, expected %d' % (pid, len(spans), len(cap_refs_in_order)))

    removals = []  # (abs_start, abs_end) ranges to delete, outer coords
    for ref, (cap_start, cap_end) in zip(cap_refs_in_order, spans):
        cap_text = text[cap_start:cap_end]
        entry_spans = find_generic_outcomes_entry_spans(cap_text)
        if len(entry_spans) == 0:
            continue  # already stripped (idempotent) or no genericOutcomes at all
        if len(entry_spans) == 2:
            origins = [origin_of(cap_text[s:e]) for s, e in entry_spans]
            if origins == ['from-benchmark', 'from-benchmark']:
                continue  # already stripped (idempotent)
            raise ValueError('%s %s: 2 entries but unexpected origins %r' % (pid, ref, origins))
        if len(entry_spans) != 4:
            raise ValueError('%s %s: expected 4 genericOutcomes entries, found %d' % (pid, ref, len(entry_spans)))
        origins = [origin_of(cap_text[s:e]) for s, e in entry_spans]
        if origins != ['distilled', 'distilled', 'from-benchmark', 'from-benchmark']:
            raise ValueError('%s %s: unexpected genericOutcomes order %r' % (pid, ref, origins))
        remove_start = cap_start + entry_spans[0][0]   # opening "{" of first distilled entry
        remove_end = cap_start + entry_spans[2][0]     # opening "{" of first from-benchmark entry
        removals.append((remove_start, remove_end))

    new_text = text
    for start, end in sorted(removals, key=lambda t: -t[0]):
        new_text = new_text[:start] + new_text[end:]

    # Safety: re-inserting the removed slices (in ascending order) must reproduce
    # the original byte-for-byte.
    check_text = new_text
    for start, end in sorted(removals, key=lambda t: t[0]):
        removed_slice = text[start:end]
        check_text = check_text[:start] + removed_slice + check_text[start:]
    if check_text != text:
        raise ValueError('%s: re-inserting the removed slices does not reproduce the original byte-for-byte' % pid)

    json.loads(new_text)  # must still be valid JSON
    return new_text, len(removals)


if __name__ == '__main__':
    pids = sys.argv[1:] or sorted(os.path.splitext(os.path.basename(p))[0]
                                  for p in glob.glob(os.path.join(EVIDENCE_DIR, '*.json'))
                                  if not os.path.basename(p).startswith('_'))
    for pid in pids:
        new_text, n = remove_one(pid)
        ev_path = os.path.join(EVIDENCE_DIR, pid + '.json')
        with open(ev_path, 'w', encoding='utf-8') as fh:
            fh.write(new_text)
        print('stripped %s: %d capabilities had their distilled pair removed' % (pid, n))
