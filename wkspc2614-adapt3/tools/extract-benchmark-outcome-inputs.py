#!/usr/bin/env python3
"""extract-benchmark-outcome-inputs.py - input packets for authoring the new
learningOutcome field on each capability's two from-benchmark genericOutcomes
entries (conceptual + applied).

For every capability already carrying genericOutcomes
(catalogue/context/pathway-evidence/<pathway>.json), emits the two
from-benchmark entries (kind, title, example, artefact, grounding) plus the
benchmark extract(s) actually attributed to that capability
(catalogue/context/pathway/<pathway>.json -> benchmarkKeys.byTier), or the
capability's own statement where unattributed - the same fallback rule as the
genericOutcomes themselves.

Output: /tmp/benchmark-outcome-inputs/<pathway>.json
Shape: {"pathway": ..., "capabilities": [{
  "capability": <ref>, "tier": ..., "statement": ...,
  "benchmarks": [{"statementId", "strength", "extract"}, ...],  # [] if unattributed
  "fromBenchmark": {"conceptual": {...entry...}, "applied": {...entry...}}
}, ...]}

Run from the repo root:
    python tools/extract-benchmark-outcome-inputs.py
"""
import glob, json, os, sys
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import pathway_tiers

REPO_ROOT = pathway_tiers.REPO_ROOT
PATHWAY_DIR = pathway_tiers.PATHWAY_DIR
EVIDENCE_DIR = os.path.join(REPO_ROOT, 'catalogue', 'context', 'pathway-evidence')
OUTPUT_DIR = '/tmp/benchmark-outcome-inputs'


def benchmarks_for(by_tier, ref):
    out = []
    for entries in (by_tier or {}).values():
        for e in entries:
            if ref in (e.get('capabilities') or []):
                out.append({'statementId': e['statementId'], 'strength': e['strength'], 'extract': e['extract']})
    return out


def extract_one(pid):
    pdoc = json.load(open(os.path.join(PATHWAY_DIR, pid + '.json'), encoding='utf-8'))
    by_tier = (pdoc.get('benchmarkKeys') or {}).get('byTier') or {}
    pcaps = {}
    for c in pdoc.get('capabilities') or []:
        ref = c.get('capabilityId') or pid + '#' + str(c.get('rowId'))
        pcaps[ref] = c

    edoc = json.load(open(os.path.join(EVIDENCE_DIR, pid + '.json'), encoding='utf-8'))
    out_caps = []
    for ec in edoc.get('capabilities') or []:
        ref = ec['capability']
        pc = pcaps.get(ref) or {}
        gos = ec.get('genericOutcomes') or []
        from_bm = {g['kind']: g for g in gos if g.get('origin') == 'from-benchmark'}
        if set(from_bm) != {'conceptual', 'applied'}:
            raise ValueError('%s %s: expected conceptual+applied from-benchmark entries, found %r' %
                              (pid, ref, sorted(from_bm)))
        out_caps.append({
            'capability': ref,
            'tier': pc.get('tier'),
            'statement': pc.get('statement'),
            'benchmarks': benchmarks_for(by_tier, ref),
            'fromBenchmark': from_bm,
        })
    return {'pathway': pid, 'capabilities': out_caps}


if __name__ == '__main__':
    os.makedirs(OUTPUT_DIR, exist_ok=True)
    pids = sys.argv[1:] or sorted(os.path.splitext(os.path.basename(p))[0]
                                  for p in glob.glob(os.path.join(EVIDENCE_DIR, '*.json'))
                                  if not os.path.basename(p).startswith('_'))
    for pid in pids:
        packet = extract_one(pid)
        out_path = os.path.join(OUTPUT_DIR, pid + '.json')
        with open(out_path, 'w', encoding='utf-8') as fh:
            json.dump(packet, fh, indent=2, ensure_ascii=False)
        print('wrote %s: %d capabilities' % (pid, len(packet['capabilities'])))
