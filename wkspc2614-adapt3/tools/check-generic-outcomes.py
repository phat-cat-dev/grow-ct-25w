#!/usr/bin/env python3
"""check-generic-outcomes.py - validate the generic learning outcomes layer
(the 9 -> 18 -> +4): 4 genericOutcomes entries per capability, in two origins
(distilled, from-benchmark) x two kinds (conceptual, applied).

Mirrors tools/check-pathway-evidence.py's structure and CLI. Store:
catalogue/context/pathway-evidence/<pathway>.json -> capabilities[].genericOutcomes
(beside the existing evidence[], untouched).

Checks, per file:
  - every capability of the pathway covered exactly once, tier matches
  - exactly 4 genericOutcomes entries; the (origin, kind) pairs
    distilled/conceptual, distilled/applied, from-benchmark/conceptual,
    from-benchmark/applied each appear exactly once
  - fields exactly kind, origin, title, example, artefact, grounding, plus
    learningOutcome on from-benchmark entries only (distilled entries must not
    carry it)
  - title <= 12 words; example 35-90 words; artefact 8-30 words;
    learningOutcome (from-benchmark only) 10-40 words
  - grounding non-empty:
      conceptual: every non-benchmark entry is a capability theory id or
        "model: ...". At least one theory id used when the capability has any.
      applied: every non-benchmark entry is "professional: ..." or
        "framework: ...". "practice: ..." is banned here.
      from-benchmark (either kind): exactly one "benchmark: <statementId>"
        entry, resolving to a statementId attributed to this capability in
        catalogue/context/pathway/<pathway>.json -> benchmarkKeys.byTier, or
        "benchmark: none (unattributed; written from capability statement)"
        when the capability's attribution is unattributed.
  - house rules: no em dash (U+2014), never "academic skills"

Run from the repo root:
    python tools/check-generic-outcomes.py              # all pathways
    python tools/check-generic-outcomes.py criticality   # one or more
"""
import glob, json, os, re, sys
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import pathway_tiers

EVIDENCE_DIR = os.path.join(pathway_tiers.REPO_ROOT, 'catalogue', 'context', 'pathway-evidence')
KINDS = ('conceptual', 'applied')
ORIGINS = ('distilled', 'from-benchmark')
PAIRS = {(o, k) for o in ORIGINS for k in KINDS}
FIELDS = {'kind', 'origin', 'title', 'example', 'artefact', 'grounding'}
LIMITS = {'title': (1, 12), 'example': (35, 90), 'artefact': (8, 30)}
LO_LIMITS = (10, 40)
FALLBACK = 'none (unattributed; written from capability statement)'


def words(s):
    return len(re.findall(r"[A-Za-z0-9'']+", s or ''))


def benchmark_ids_for(ref, by_tier):
    ids = set()
    for tier in pathway_tiers.TIERS:
        for e in by_tier.get(tier, []):
            if ref in (e.get('capabilities') or []):
                ids.add(e.get('statementId'))
    return ids


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
    cap_doc = json.load(open(cap_path, encoding='utf-8'))
    caps = {}
    for c in cap_doc['capabilities']:
        ref = c.get('capabilityId') or pid + '#' + str(c.get('rowId'))
        caps[ref] = c
    attribution = (cap_doc.get('benchmarkKeys') or {}).get('attribution') or {}
    by_tier = (cap_doc.get('benchmarkKeys') or {}).get('byTier') or {}

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

        go = it.get('genericOutcomes')
        if go is None:
            errs.append('%s: missing genericOutcomes' % ref)
            continue
        if len(go) != 4:
            errs.append('%s: genericOutcomes has %d entries, want 4' % (ref, len(go)))

        theory = {t for t in (cap.get('competency') or {}).get('theory') or [] if isinstance(t, str)}
        valid_bench_ids = benchmark_ids_for(ref, by_tier)
        attr = attribution.get(ref)

        pairs_seen = []
        for e in go:
            origin_for_fields = e.get('origin')
            want_fields = FIELDS | {'learningOutcome'} if origin_for_fields == 'from-benchmark' else FIELDS
            extra = set(e.keys()) - want_fields
            missing = want_fields - set(e.keys())
            if extra:
                errs.append('%s: unexpected fields %s' % (ref, sorted(extra)))
            if missing:
                errs.append('%s: missing fields %s' % (ref, sorted(missing)))
                continue
            kind, origin = e.get('kind'), e.get('origin')
            if kind not in KINDS:
                errs.append('%s: bad kind %r' % (ref, kind))
            if origin not in ORIGINS:
                errs.append('%s: bad origin %r' % (ref, origin))
            if (origin, kind) in pairs_seen:
                errs.append('%s: duplicate (origin, kind) pair (%s, %s)' % (ref, origin, kind))
            pairs_seen.append((origin, kind))

            for f, (lo, hi) in LIMITS.items():
                n = words(e.get(f))
                if not lo <= n <= hi:
                    errs.append('%s %s/%s.%s is %d words (want %d-%d)' % (ref, origin, kind, f, n, lo, hi))
            if origin == 'from-benchmark' and 'learningOutcome' in e:
                lo, hi = LO_LIMITS
                n = words(e.get('learningOutcome'))
                if not lo <= n <= hi:
                    errs.append('%s %s/%s.learningOutcome is %d words (want %d-%d)' % (ref, origin, kind, n, lo, hi))

            g = e.get('grounding') or []
            if not g:
                errs.append('%s %s/%s: empty grounding' % (ref, origin, kind))
            bench_lines = [x for x in g if isinstance(x, str) and x.startswith('benchmark: ')]
            other = [x for x in g if x not in bench_lines]

            if kind == 'conceptual':
                stray = [x for x in other if x not in theory and not str(x).startswith('model: ')]
                if stray:
                    errs.append('%s %s/conceptual grounding %s is neither a capability theory id %s nor "model: ..."'
                                % (ref, origin, stray, sorted(theory)))
                if theory and not (set(other) & theory):
                    errs.append('%s %s/conceptual grounding uses none of the capability theory ids %s'
                                % (ref, origin, sorted(theory)))
            elif kind == 'applied':
                stray = [x for x in other
                         if not (str(x).startswith('professional: ') or str(x).startswith('framework: '))]
                if stray:
                    errs.append('%s %s/applied grounding %s is neither "professional: ..." nor "framework: ..."'
                                % (ref, origin, stray))

            if origin == 'from-benchmark':
                if len(bench_lines) != 1:
                    errs.append('%s %s/%s: needs exactly one "benchmark: ..." grounding entry, has %d'
                                % (ref, origin, kind, len(bench_lines)))
                else:
                    val = bench_lines[0][len('benchmark: '):]
                    if attr == 'unattributed':
                        if val != FALLBACK:
                            errs.append('%s %s/%s: unattributed capability must use fallback benchmark line, got %r'
                                        % (ref, origin, kind, val))
                    elif val not in valid_bench_ids:
                        errs.append('%s %s/%s: benchmark statementId %r not among this capability\'s benchmarkKeys %s'
                                    % (ref, origin, kind, val, sorted(valid_bench_ids)))
            elif origin == 'distilled' and bench_lines:
                errs.append('%s %s/%s: distilled entries should not carry a "benchmark: ..." line'
                            % (ref, origin, kind))

        if set(pairs_seen) != PAIRS and len(go) == 4:
            errs.append('%s: (origin, kind) pairs %s != required %s' % (ref, sorted(pairs_seen), sorted(PAIRS)))

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
