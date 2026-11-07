"""pathway_tiers.py - shared tier-keying rule for benchmark -> pathway keys.

A benchmark statement (universal graduate competency or a subject benchmark
statement) keys into an academic-practice pathway. This module adds the tier
dimension: WHICH of the pathway's three tiers (introductory / intermediate /
advanced) the statement informs, and which of the pathway's 9 capabilities
(3 per tier, catalogue/context/pathway/<pathway>.json) it lands on.

Rule (deterministic, so provenance is traceable both ways):
  1. capability-match - the statement matches one or more of the pathway's
     capabilities (a regex for the universal concepts, or content-word overlap
     for subject prose). It keys into the tiers of those capabilities only.
  2. progression - no capability matches but the edge is `direct`: the pathway
     realises the statement as a climb, so it keys into all three tiers.
  3. floor - no capability matches and the edge is `indirect`: a shared-core
     floor carried at every tier; flagged for review by its basis.

Used by tools/build-universal-benchmark.py and tools/key-benchmark-tiers.py.
"""
import json, os, re

REPO_ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
PATHWAY_DIR = os.path.join(REPO_ROOT, 'catalogue', 'context', 'pathway')
TIERS = ('introductory', 'intermediate', 'advanced')

# Words too common in benchmark/capability prose to count as overlap.
STOP = set('''about above across after against along among their there these those
which while within without would could should other others being because before
between through under using where whether students student graduates graduate
subject subjects ability abilities including include understanding knowledge
level levels study studies range relevant appropriate different particular
develop developed development''' .split())

_cache = {}


def strip_prefix(pathway_key):
    """'adapt-criticality' -> 'criticality'."""
    return pathway_key[len('adapt-'):] if pathway_key.startswith('adapt-') else pathway_key


def capabilities(pathway_key):
    """The pathway's capabilities as (ref, tier, text) triples, cached."""
    pid = strip_prefix(pathway_key)
    if pid not in _cache:
        path = os.path.join(PATHWAY_DIR, pid + '.json')
        caps = []
        if os.path.exists(path):
            for c in json.load(open(path, encoding='utf-8')).get('capabilities') or []:
                comp = c.get('competency') or {}
                voc = c.get('vocabulary') or {}
                text = ' '.join([
                    str(c.get('statement') or ''), str(comp.get('academicStatement') or ''),
                    ' '.join(comp.get('verbs') or []), ' '.join(voc.get('verbs') or []),
                    str(c.get('knowledgeKind') or ''),
                ]).lower()
                ref = c.get('capabilityId') or (pid + '#' + str(c.get('rowId')))
                caps.append((ref, c.get('tier'), text))
        _cache[pid] = caps
    return _cache[pid]


def raw_capabilities(pathway_key):
    """The pathway's capabilities as full dicts, uncached and unfiltered.

    Unlike capabilities(), nothing is flattened to text: vocabulary.terms,
    knowledgeKind, competency, etc. are all still present. Used by
    tools/build-pathway-tier-readings.py, which needs the full shape.
    """
    pid = strip_prefix(pathway_key)
    path = os.path.join(PATHWAY_DIR, pid + '.json')
    if not os.path.exists(path):
        return []
    return json.load(open(path, encoding='utf-8')).get('capabilities') or []


def cap_ref(c, pathway_key):
    """A capability dict's reference id, matching the ref used in capabilities()."""
    pid = strip_prefix(pathway_key)
    return c.get('capabilityId') or (pid + '#' + str(c.get('rowId')))


def _stems(text):
    words = re.findall(r'[a-z]{5,}', text.lower())
    return {w[:6] for w in words if w not in STOP}


def key_tiers(pathway_key, strength, pattern=None, text=None, min_overlap=2):
    """Return (tiers, basis) for one statement -> pathway edge.

    pattern: a regex matched against each capability (universal concepts).
    text: statement prose, matched by content-word overlap (subject benchmarks).
    tiers is [{'tier', 'capabilities': [refs]}] in TIERS order.
    """
    hits = {}
    want = _stems(text) if text else set()
    for ref, tier, ctext in capabilities(pathway_key):
        if pattern and re.search(pattern, ctext):
            hit = True
        elif want:
            hit = len(want & _stems(ctext)) >= min_overlap
        else:
            hit = False
        if hit and tier in TIERS:
            hits.setdefault(tier, []).append(ref)
    if hits:
        return [{'tier': t, 'capabilities': hits[t]} for t in TIERS if t in hits], 'capability-match'
    basis = 'progression' if strength == 'direct' else 'floor'
    return [{'tier': t, 'capabilities': []} for t in TIERS], basis
