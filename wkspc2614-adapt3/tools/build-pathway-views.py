#!/usr/bin/env python3
"""build-pathway-views.py - the full benchmark chain per pathway, as a view.

A VIEW, not a new store: everything here is already built and checked
elsewhere. This script only joins, read-only, across four existing stores,
per pathway:

  benchmark statement (full text, pulled back from
    catalogue/context/subject/benchmarks/<source>.json)
    -> the 9 capabilities (catalogue/context/pathway/<pathway>.json)
    -> the 18 generic learning outcomes
       (catalogue/context/pathway-evidence/<pathway>.json)
    -> the 9 tier readings: practice / knowledge / identity per tier
       (catalogue/context/pathway-tier-readings/<pathway>.json)

No new data is invented, filled or inflected. Nothing here is authored.
Deterministic: the same four stores always give byte-identical output, so a
rebuild is a no-op and determinism is itself checkable (git diff
--exit-code). No timestamp is recorded.

Each pathway writes two per-pathway files plus contributes one row to a
single combined Markdown file (catalogue/context/pathway-views/<pathway>.json,
<pathway>.yaml, pathway-views.md):

    python3 tools/build-pathway-views.py --self-test
    python3 tools/build-pathway-views.py academic-writing --dry-run
    python3 tools/build-pathway-views.py            # builds all 13 + the combined md
"""
import argparse, json, os, sys

import yaml

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import pathway_tiers as pt

REPO_ROOT = pt.REPO_ROOT
PATHWAY_DIR = pt.PATHWAY_DIR
EVIDENCE_DIR = os.path.join(REPO_ROOT, 'catalogue', 'context', 'pathway-evidence')
READINGS_DIR = os.path.join(REPO_ROOT, 'catalogue', 'context', 'pathway-tier-readings')
BENCHMARKS_DIR = os.path.join(REPO_ROOT, 'catalogue', 'context', 'subject', 'benchmarks')
OUT_DIR = os.path.join(REPO_ROOT, 'catalogue', 'context', 'pathway-views')
MD_PATH = os.path.join(OUT_DIR, 'pathway-views.md')
TIERS = pt.TIERS
FIELDS = ('practice', 'knowledge', 'identity')

_benchmark_cache = {}


def pathway_ids():
    return sorted(
        os.path.splitext(f)[0] for f in os.listdir(PATHWAY_DIR) if f.endswith('.json')
    )


def load_benchmark_source(source):
    if source not in _benchmark_cache:
        path = os.path.join(BENCHMARKS_DIR, source + '.json')
        _benchmark_cache[source] = json.load(open(path, encoding='utf-8')) if os.path.exists(path) else {}
    return _benchmark_cache[source]


def resolve_statement(key):
    """Full statement text for one benchmarkKeys entry, pulled back from its
    own source file - statement text only, not the formula scaffolding
    (slots/options/agentInstruction), which already lives in the source
    file and would just be duplicated here.

    'universal-reference' keys resolve against graduate_competency.items,
    keyed by id (the statementId's last '/'-segment, matching the id scheme
    tools/render-pathway-benchmarks-md.py already relies on). Every other
    source (today: psychology-2023, the one authored subject map) resolves
    against its own statements[], keyed by the statementId verbatim.

    psychology-2023.json's statements[] is a partial extraction (61 entries,
    mostly sub-bullets of a few numbered points) - most benchmarkKeys refer to
    points that were never pulled into full statement form. Every benchmarkKey
    still carries its own short 'extract' string (checked live: all 378 keys
    across all 13 pathways have one), so a key that misses the full-statement
    lookup falls back to that extract rather than vanishing from the view.
    This is marked extractOnly: true so the view stays honest about which text
    is the full statement and which is the key's own short extract.
    """
    source = key['source']
    doc = load_benchmark_source(source)
    if source == 'universal-reference':
        comps = {i['id']: i for i in (doc.get('graduate_competency') or {}).get('items') or []}
        item = comps.get(key['statementId'].split('/')[-1])
        if item:
            return {
                'source': source, 'statementId': key['statementId'], 'strength': key['strength'],
                'label': item.get('label'), 'strand': item.get('strand'),
                'graduateStatement': item.get('graduateStatement'),
                'studentStatement': item.get('studentStatement'),
            }
    else:
        statements = {s['id']: s for s in doc.get('statements') or []}
        item = statements.get(key['statementId'])
        if item:
            audience = item.get('audienceVersions') or {}
            return {
                'source': source, 'statementId': key['statementId'], 'strength': key['strength'],
                'locator': (item.get('locator') or {}).get('number'),
                'paraphrase': item.get('paraphrase'),
                'forBeneficiary': (audience.get('forBeneficiary') or {}).get('text'),
            }
    extract = key.get('extract')
    if not extract:
        return None
    return {
        'source': source, 'statementId': key['statementId'], 'strength': key['strength'],
        'extract': extract, 'extractOnly': True,
    }


NOTE = (
    "Pathway view: the benchmark chain for this pathway, joined read-only from "
    "four already-built stores. No new data is invented, filled or inflected "
    "here; this is a view, not a new store. Built deterministically by "
    "tools/build-pathway-views.py. Chain: benchmark statement (full text, "
    "pulled back from catalogue/context/subject/benchmarks/<source>.json) -> "
    "the 9 capabilities (catalogue/context/pathway/<pathway>.json) -> the 18 "
    "generic learning outcomes (catalogue/context/pathway-evidence/<pathway>.json) "
    "-> the 9 tier readings, practice/knowledge/identity per tier "
    "(catalogue/context/pathway-tier-readings/<pathway>.json)."
)


def build_pathway(pid):
    pw = json.load(open(os.path.join(PATHWAY_DIR, pid + '.json'), encoding='utf-8'))
    ev_path = os.path.join(EVIDENCE_DIR, pid + '.json')
    ev = json.load(open(ev_path, encoding='utf-8')) if os.path.exists(ev_path) else {}
    ev_by_ref = {c['capability']: c for c in ev.get('capabilities') or []}
    tr_path = os.path.join(READINGS_DIR, pid + '.json')
    tr = json.load(open(tr_path, encoding='utf-8')) if os.path.exists(tr_path) else {}
    tr_by_tier = {t['tier']: t for t in tr.get('tierReadings') or []}

    by_tier = (pw.get('benchmarkKeys') or {}).get('byTier') or {}
    all_caps = pw.get('capabilities') or []

    tiers_out = []
    for t in TIERS:
        tier_caps = [c for c in all_caps if c.get('tier') == t]
        matched = [k for k in by_tier.get(t, []) if k.get('tierBasis') == 'capability-match']
        caps_out = []
        for c in tier_caps:
            ref = pt.cap_ref(c, pid)
            landed = [k for k in matched if ref in (k.get('capabilities') or [])]
            benchmarks = []
            for k in landed:
                st = resolve_statement(k)
                if st:
                    benchmarks.append(st)
            item = ev_by_ref.get(ref)
            generic = [
                {'kind': g.get('kind'), 'title': g.get('title'), 'learningOutcome': g.get('learningOutcome')}
                for g in ((item or {}).get('genericOutcomes') or [])
            ]
            caps_out.append({
                'ref': ref,
                'rowId': c.get('rowId'),
                'fheqLevel': c.get('fheqLevel'),
                'statement': c.get('statement'),
                'knowledgeKind': c.get('knowledgeKind'),
                'benchmarks': benchmarks,
                'genericOutcomes': generic,
            })
        reading = tr_by_tier.get(t) or {}
        statements = reading.get('statements') or {}
        tiers_out.append({
            'tier': t,
            'fheqLevel': reading.get('fheqLevel'),
            'verbBand': reading.get('verbBand'),
            'capabilities': caps_out,
            'tierReading': {f: (statements.get(f) or {}).get('statement') for f in FIELDS},
        })

    every, seen = [], set()
    for t in TIERS:
        for k in by_tier.get(t, []):
            if k.get('tierBasis') != 'capability-match' and (k['source'], k['statementId']) not in seen:
                seen.add((k['source'], k['statementId']))
                st = resolve_statement(k)
                if st:
                    every.append(dict(st, tierBasis=k['tierBasis']))

    sources = (pw.get('benchmarkKeys') or {}).get('sources') or []
    inputs = [
        'catalogue/context/pathway/%s.json' % pid,
        'catalogue/context/pathway-evidence/%s.json' % pid,
        'catalogue/context/pathway-tier-readings/%s.json' % pid,
    ] + ['catalogue/context/subject/benchmarks/%s.json' % s for s in sources]

    return {
        'pathway': pid,
        'status': 'generated',
        'note': NOTE,
        'tiers': tiers_out,
        'everyTierBenchmarks': every,
        'source': {
            'script': 'tools/build-pathway-views.py',
            'inputs': inputs,
            'note': 'Deterministic join across already-built stores; no authored content. A rebuild is byte-identical.',
        },
    }


def render_markdown(views):
    L = [
        '# Pathway views: the full benchmark chain, per pathway', '',
        'Generated by `tools/build-pathway-views.py`; do not hand-edit. A view, not a '
        'new store: it joins, read-only, catalogue/context/pathway/, pathway-evidence/, '
        'pathway-tier-readings/ and subject/benchmarks/.', '',
        '## Contents', '',
    ]
    L += ['%d. [%s](#%s)' % (i + 1, v['pathway'], v['pathway']) for i, v in enumerate(views)] + ['']
    for v in views:
        L += ['<a id="%s"></a>' % v['pathway'], '## %s' % v['pathway'], '']
        for t in v['tiers']:
            L += ['### %s (FHEQ %s, verb band %s)' % (t['tier'].title(), t['fheqLevel'], t['verbBand']), '']
            for c in t['capabilities']:
                L.append('**%s:** %s' % (c['rowId'], c['statement']))
                if c['benchmarks']:
                    for b in c['benchmarks']:
                        text = b.get('graduateStatement') or b.get('paraphrase') or b.get('extract') or ''
                        flag = ' [extract only]' if b.get('extractOnly') else ''
                        L.append('- *Benchmark (%s, %s)%s:* %s' % (b['source'], b['strength'], flag, text))
                else:
                    L.append('- *Benchmark:* none matched at this tier')
                for g in c['genericOutcomes']:
                    L.append('- *Generic outcome [%s]:* %s' % (g['kind'], g['learningOutcome']))
                L.append('')
            L += ['**Tier reading:**', '']
            for f in FIELDS:
                L.append('- *%s:* %s' % (f.title(), t['tierReading'].get(f)))
            L.append('')
        if v['everyTierBenchmarks']:
            L += ['**Benchmarks at every tier (progression / floor):**', '']
            for b in v['everyTierBenchmarks']:
                text = b.get('graduateStatement') or b.get('paraphrase') or b.get('extract') or ''
                flag = ' [extract only]' if b.get('extractOnly') else ''
                L.append('- *(%s, %s, %s)%s:* %s' % (b['source'], b['strength'], b['tierBasis'], flag, text))
            L.append('')
    return '\n'.join(L)


def self_test():
    errs = []
    pids = pathway_ids()
    if len(pids) != 13:
        errs.append('expected 13 pathway files, found %d' % len(pids))
    sources_seen = set()
    for pid in pids:
        pw = json.load(open(os.path.join(PATHWAY_DIR, pid + '.json'), encoding='utf-8'))
        sources_seen.update((pw.get('benchmarkKeys') or {}).get('sources') or [])
    for s in sources_seen:
        path = os.path.join(BENCHMARKS_DIR, s + '.json')
        if not os.path.exists(path):
            errs.append('missing benchmark source file for %r' % s)
    # Resolve every single benchmark key across every pathway and require a hit -
    # an unresolvable key would silently vanish from the view otherwise.
    unresolved = []
    for pid in pids:
        pw = json.load(open(os.path.join(PATHWAY_DIR, pid + '.json'), encoding='utf-8'))
        by_tier = (pw.get('benchmarkKeys') or {}).get('byTier') or {}
        for t in TIERS:
            for k in by_tier.get(t, []):
                if resolve_statement(k) is None:
                    unresolved.append((pid, t, k['source'], k['statementId']))
    if unresolved:
        for u in unresolved[:10]:
            errs.append('unresolved benchmark key: %s' % (u,))
        errs.append('%d unresolved benchmark keys total' % len(unresolved))
    print('build-pathway-views.py --self-test:', 'FAIL' if errs else 'PASS')
    print()
    print('pathways found:', len(pids))
    print('benchmark sources in use:', sorted(sources_seen))
    print('benchmark keys resolved: all' if not unresolved else '%d unresolved' % len(unresolved))
    for e in errs:
        print('    -', e)
    return errs


def main():
    ap = argparse.ArgumentParser(description=__doc__)
    ap.add_argument('pathway', nargs='?', help='pathway key, e.g. academic-writing')
    ap.add_argument('--dry-run', action='store_true', help='print, do not write')
    ap.add_argument('--report', action='store_true', help='read-through report')
    ap.add_argument('--self-test', action='store_true', help='validate benchmark-key resolution')
    args = ap.parse_args()

    if args.self_test:
        errs = self_test()
        sys.exit(1 if errs else 0)

    if args.pathway:
        payload = build_pathway(args.pathway)
        if args.dry_run or args.report:
            print(json.dumps(payload, indent=2, ensure_ascii=False))
            return
        os.makedirs(OUT_DIR, exist_ok=True)
        json_path = os.path.join(OUT_DIR, args.pathway + '.json')
        with open(json_path, 'w', encoding='utf-8') as fh:
            json.dump(payload, fh, indent=2, ensure_ascii=False, sort_keys=False)
            fh.write('\n')
        yaml_path = os.path.join(OUT_DIR, args.pathway + '.yaml')
        with open(yaml_path, 'w', encoding='utf-8') as fh:
            yaml.dump(payload, fh, sort_keys=False, allow_unicode=True, default_flow_style=False, width=100)
        print('wrote', os.path.relpath(json_path, REPO_ROOT))
        print('wrote', os.path.relpath(yaml_path, REPO_ROOT))
        return

    pids = pathway_ids()
    views = [build_pathway(pid) for pid in pids]
    if args.dry_run or args.report:
        print(render_markdown(views))
        return
    os.makedirs(OUT_DIR, exist_ok=True)
    for pid, payload in zip(pids, views):
        json_path = os.path.join(OUT_DIR, pid + '.json')
        with open(json_path, 'w', encoding='utf-8') as fh:
            json.dump(payload, fh, indent=2, ensure_ascii=False, sort_keys=False)
            fh.write('\n')
        yaml_path = os.path.join(OUT_DIR, pid + '.yaml')
        with open(yaml_path, 'w', encoding='utf-8') as fh:
            yaml.dump(payload, fh, sort_keys=False, allow_unicode=True, default_flow_style=False, width=100)
    with open(MD_PATH, 'w', encoding='utf-8') as fh:
        fh.write(render_markdown(views))
    print('wrote %d pathways x (json, yaml) + %s' % (len(pids), os.path.relpath(MD_PATH, REPO_ROOT)))


if __name__ == '__main__':
    main()
