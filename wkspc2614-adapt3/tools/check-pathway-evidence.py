#!/usr/bin/env python3
"""check-pathway-evidence.py - validate the 9 -> 18 evidence examples.

Each academic-practice pathway's 9 capabilities (3 per tier) get two
descriptive examples of demonstrable evidence a student could offer for that
capability: one CONCEPTUAL (theory / concept / model) and one APPLIED (practice
/ real world). 9 x 2 = 18 per pathway, 6 per tier.

Store: catalogue/context/pathway-evidence/<pathway>.json (authored, kept apart
from catalogue/context/pathway/, which build-pathway-reference.py regenerates).

Checks, per file:
  - every capability of the pathway appears exactly once (ref = capabilityId,
    else <pathway>#<rowId>, as tools/pathway_tiers.py), tier matches
  - exactly two evidence items, one conceptual + one applied
  - conceptual grounding: when the capability has ingested theory ids
    (competency.theory strings), at least one of them; any other entry must be
    "model: <named model>". With no ingested ids, every entry is "model: ...".
    Applied grounding is non-empty.
  - title <= 12 words; example 35-90 words; artefact 8-30 words
  - house rules: no em dash (U+2014), never "academic skills"

Run from the repo root:
    python tools/check-pathway-evidence.py              # all pathways
    python tools/check-pathway-evidence.py criticality  # one or more
"""
import glob, json, os, re, sys
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import pathway_tiers

EVIDENCE_DIR = os.path.join(pathway_tiers.REPO_ROOT, 'catalogue', 'context', 'pathway-evidence')
KINDS = ('conceptual', 'applied')
LIMITS = {'title': (1, 12), 'example': (35, 90), 'artefact': (8, 30)}


def words(s):
    return len(re.findall(r"[A-Za-z0-9'']+", s or ''))


def check(pid):
    errs = []
    cap_path = os.path.join(pathway_tiers.PATHWAY_DIR, pid + '.json')
    ev_path = os.path.join(EVIDENCE_DIR, pid + '.json')
    if not os.path.exists(ev_path):
        return ['missing ' + os.path.relpath(ev_path, pathway_tiers.REPO_ROOT)]
    raw = open(ev_path, encoding='utf-8').read()
    if '—' in raw:
        errs.append('em dash present')
    if re.search(r'academic skills', raw, re.I):
        errs.append('"academic skills" present')
    doc = json.loads(raw)
    caps = {}
    cap_doc = json.load(open(cap_path, encoding='utf-8'))
    attribution = (cap_doc.get('benchmarkKeys') or {}).get('attribution') or {}
    for c in cap_doc['capabilities']:
        ref = c.get('capabilityId') or pid + '#' + str(c.get('rowId'))
        caps[ref] = c
    if doc.get('pathway') != pid:
        errs.append('pathway field is %r' % doc.get('pathway'))
    seen = set()
    for it in doc.get('capabilities') or []:
        ref = it.get('capability')
        if ref not in caps:
            errs.append('unknown capability %r' % ref); continue
        if ref in seen:
            errs.append('duplicate %s' % ref)
        seen.add(ref)
        cap = caps[ref]
        if it.get('tier') != cap.get('tier'):
            errs.append('%s tier %r != %r' % (ref, it.get('tier'), cap.get('tier')))
        ev = it.get('evidence') or []
        if sorted(e.get('kind') for e in ev) != sorted(KINDS):
            errs.append('%s needs one conceptual + one applied, has %s' % (ref, [e.get('kind') for e in ev]))
        # theory entries are ingested ids (strings) or {"unknown": ...} placeholders
        theory = {t for t in (cap.get('competency') or {}).get('theory') or [] if isinstance(t, str)}
        if it.get('attribution') != attribution.get(ref):
            errs.append('%s attribution %r != %r' % (ref, it.get('attribution'), attribution.get(ref)))
        for e in ev:
            for f, (lo, hi) in LIMITS.items():
                n = words(e.get(f))
                if not lo <= n <= hi:
                    errs.append('%s %s.%s is %d words (want %d-%d)' % (ref, e.get('kind'), f, n, lo, hi))
            g = e.get('grounding') or []
            if not g:
                errs.append('%s %s: empty grounding' % (ref, e.get('kind')))
            if e.get('kind') == 'conceptual':
                stray = [x for x in g if x not in theory and not str(x).startswith('model: ')]
                if stray:
                    errs.append('%s conceptual grounding %s is neither a capability theory id %s nor "model: ..."'
                                % (ref, stray, sorted(theory)))
                if theory and not set(g) & theory:
                    errs.append('%s conceptual grounding uses none of the capability theory ids %s'
                                % (ref, sorted(theory)))
    for ref in caps:
        if ref not in seen:
            errs.append('capability not covered: ' + ref)
    return errs


if __name__ == '__main__':
    pids = sys.argv[1:] or sorted(os.path.splitext(os.path.basename(p))[0]
                                  for p in glob.glob(os.path.join(pathway_tiers.PATHWAY_DIR, '*.json')))
    bad = 0
    for pid in pids:
        errs = check(pid)
        print('%-46s %s' % (pid, 'PASS' if not errs else 'FAIL (%d)' % len(errs)))
        for e in errs:
            print('    - ' + e)
        bad += bool(errs)
    sys.exit(1 if bad else 0)
