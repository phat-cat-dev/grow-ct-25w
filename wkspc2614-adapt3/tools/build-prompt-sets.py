#!/usr/bin/env python3
"""build-prompt-sets.py - academic-practice prompt sets from the benchmark keys.

Generates RTCF prompt starters categorised the way the universal benchmark is:

    strand > graduate competency > pathway > tier

Sources (all read, none written except the outputs below):
  - catalogue/context/subject/benchmarks/universal-reference.json
      graduate_competency (strand, label), pathwayMapping (pathway + tier keys,
      tierBasis), tierReadings (the tier pitch)
  - catalogue/context/pathway/<pathway>.json   capabilities (statement per tier)
  - design-kb/design-kb.tier-bands.json        indicative FHEQ levels per tier

Output: src/components/adapt-grow-promptbuilder/libraries/academic-practice-prompts.json,
the full library (one file, authoring source; not shipped in builds, a course
embeds only its own pathway + tier slice). `floor` edges are
left out unless --include-floor: they matched no capability, so they would only
give generic prompts.

--embed writes one pathway + tier slice into a course.json as
_growPromptLibraries["academic-practice"], the shape the prompt builder's
_library lookup already reads ({stage: [{label, items}]}). Draft starters:
review the wording before release. House terms: graduate skill / competency /
attribute / academic practice, never "academic skills"; no em dashes.

Run from the repo root:
    python tools/build-prompt-sets.py
    python tools/build-prompt-sets.py --embed src/course/en/course.json \\
        --pathway ai-technology --tier advanced
"""
import argparse, collections, json, os, re, sys
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import pathway_tiers

REPO_ROOT = pathway_tiers.REPO_ROOT
UNIVERSAL = os.path.join(REPO_ROOT, 'catalogue', 'context', 'subject', 'benchmarks', 'universal-reference.json')
TIER_BANDS = os.path.join(REPO_ROOT, 'design-kb', 'design-kb.tier-bands.json')
OUT = os.path.join(REPO_ROOT, 'src', 'components', 'adapt-grow-promptbuilder', 'libraries', 'academic-practice-prompts.json')
TIERS = pathway_tiers.TIERS
LIB_ID = 'academic-practice'

STRANDS = collections.OrderedDict([
 ('knowledge', ('Knowledge', 'Start with a plain-language summary, then give me three questions to check my understanding.')),
 ('thinking', ('Thinking', 'Set it out as a table: claim, evidence, my judgement, and what would change my mind.')),
 ('application', ('Application', 'Give me a worked example, then a similar task for me to try on my own.')),
 ('communication', ('Communication', 'Show me a short model, then tell me two things to change in my own draft.')),
 ('autonomy', ('Autonomy', 'End with one next step I can take on my own and how I will know it worked.')),
])
# Tier voice: who the AI should be, and how the task is framed.
ROLES = {
 'introductory': ['a patient tutor introducing [subject] to someone new to it',
                  'a study adviser who explains {pathway} from first principles'],
 'intermediate': ['an academic tutor who expects me to analyse and evaluate, not just describe',
                  'a {pathway} tutor who asks me questions before giving answers'],
 'advanced': ['a critical peer reviewer in [subject]',
              'an experienced researcher who challenges my judgements on {pathway}'],
}
TASKS = {
 'introductory': 'Using [topic] as the example, explain step by step how to {cap}, then ask me to try it.',
 'intermediate': 'Using [topic] as the example, coach me to {cap}. Ask me questions rather than doing it for me.',
 'advanced': 'Using [topic] as the example, challenge my attempt to {cap}. Point out where my judgement is weakest.',
}
COMPETENCY_TASK = 'Show me what good work in {competency} looks like in [subject] at my stage, with an example to learn from, not copy.'
TIER_LABEL = {'introductory': 'Introductory', 'intermediate': 'Intermediate', 'advanced': 'Advanced'}


def clean(s):
    s = re.sub(r'\s*—\s*', ', ', s)
    if re.search(r'academic skills', s, re.I):
        raise SystemExit('house-term violation ("academic skills"): ' + s)
    return s


def lower_first(s):
    return s[:1].lower() + s[1:] if len(s) > 1 and s[1].islower() else s


def lower_words(s):
    """Lower-case a title for mid-sentence use, keeping acronyms (AI, GenAI)."""
    return ' '.join(lower_first(w) for w in s.split(' '))


def pathway_info(pathway_key):
    pid = pathway_tiers.strip_prefix(pathway_key)
    doc = json.load(open(os.path.join(pathway_tiers.PATHWAY_DIR, pid + '.json'), encoding='utf-8'))
    title = (doc.get('identity') or {}).get('title') or pid
    title = re.sub(r'\s*\(academic skills pathway\)\s*$', '', title, flags=re.I)
    caps = {}
    for c in doc.get('capabilities') or []:
        ref = c.get('capabilityId') or (pid + '#' + str(c.get('rowId')))
        caps[ref] = (c.get('tier'), c.get('statement') or '')
    return pid, title, caps


def build(include_floor):
    u = json.load(open(UNIVERSAL, encoding='utf-8'))
    comps = {i['id']: i for i in u['graduate_competency']['items']}
    readings = {r['tier']: r for r in u['tierReadings']['rows']}
    levels = {t['tier']: t['indicativeLevels'] for t in json.load(open(TIER_BANDS, encoding='utf-8'))['tiers']}

    tiers = {}
    for t in TIERS:
        practice = readings[t]['practice'].rstrip('.')
        tiers[t] = {
            'label': TIER_LABEL[t],
            'levels': levels.get(t, []),
            'context': [clean('Pitch your help for a learner who ' + lower_first(practice) + '.')]
                       + ['I am studying at Level %s.' % l[1:] for l in levels.get(t, [])],
        }

    pathways, sets = {}, []
    for pk, pw in u['pathwayMapping'].items():
        pid, title, caps = pathway_info(pk)
        pathways[pid] = {
            'title': title,
            'role': {t: [clean(r.format(pathway=lower_words(title))) for r in ROLES[t]] for t in TIERS},
            # the pathway's own capabilities per tier, so every cell has tasks
            # even where no graduate competency matched
            'practice': {t: [clean(TASKS[t].format(cap=lower_first(stmt)))
                             for ct, stmt in caps.values() if ct == t] for t in TIERS},
        }
        for st in pw.get('statements') or []:
            basis = st.get('tierBasis')
            if basis == 'floor' and not include_floor:
                continue
            cid = st['chunkId'].split('/')[-1]
            comp = comps.get(cid)
            if not comp:
                continue
            for tk in st.get('tiers') or []:
                t = tk['tier']
                refs = tk.get('capabilities') or [r for r, (ct, _) in caps.items() if ct == t]
                task = [clean(TASKS[t].format(cap=lower_first(caps[r][1]))) for r in refs if r in caps]
                task.append(clean(COMPETENCY_TASK.format(competency=comp['label'].lower())))
                sets.append({
                    'id': '%s/%s/%s' % (pid, t, cid),
                    'pathway': pid, 'tier': t, 'strand': comp['strand'],
                    'competency': cid, 'competencyLabel': comp['label'],
                    'studentStatement': comp.get('studentStatement', ''),
                    'strength': st.get('strength'), 'tierBasis': basis,
                    'capabilities': refs, 'task': task,
                })

    return {
        '_comment': 'GENERATED by tools/build-prompt-sets.py; do not hand-edit. Academic-practice '
                    'prompt starters (RTCF), categorised strand > graduate competency > pathway > tier '
                    'from the universal benchmark keys. Draft wording: review before release.',
        'source': {
            'universal': os.path.relpath(UNIVERSAL, REPO_ROOT).replace('\\', '/'),
            'pathways': 'catalogue/context/pathway/*.json',
            'tierBands': os.path.relpath(TIER_BANDS, REPO_ROOT).replace('\\', '/'),
            'includeFloor': include_floor,
        },
        'formula': 'rtcf',
        'terms': u['graduate_competency'].get('terms', []),
        'strands': {k: {'label': v[0], 'format': [v[1]]} for k, v in STRANDS.items()},
        'tiers': tiers,
        'pathways': pathways,
        'sets': sets,
    }


def slice_for(lib, pathway, tier):
    """One pathway + tier as {stage: [{label, items}]} for _growPromptLibraries."""
    if pathway not in lib['pathways']:
        raise SystemExit('unknown pathway: ' + pathway)
    chosen = [s for s in lib['sets'] if s['pathway'] == pathway and s['tier'] == tier]
    task, fmt, seen = [], [], set()
    for sk, sv in lib['strands'].items():
        items = []
        for s in chosen:
            if s['strand'] == sk:
                # a capability task shared by several competencies shows once,
                # under the first strand it lands in
                items.extend(i for i in s['task'] if i not in seen and not seen.add(i))
        if items:
            task.append({'label': 'Graduate skill: ' + sv['label'], 'items': items})
            fmt.append(sv['format'][0])
    pw = lib['pathways'][pathway]
    rest = [i for i in pw['practice'][tier] if i not in seen]
    if rest:
        task.append({'label': 'Academic practice: ' + pw['title'], 'items': rest})
    tl = lib['tiers'][tier]
    return {
        'role': [{'label': tl['label'] + ' tier', 'items': lib['pathways'][pathway]['role'][tier]}],
        'task': task,
        'context': [{'label': tl['label'] + ' tier', 'items': tl['context']}],
        'format': [{'label': 'Graduate skill', 'items': fmt}],
    }


def write_json(path, doc):
    with open(path, 'w', encoding='utf-8') as fh:
        json.dump(doc, fh, ensure_ascii=False, indent=2)
        fh.write('\n')


if __name__ == '__main__':
    ap = argparse.ArgumentParser(description='Build academic-practice prompt sets from the benchmark keys.')
    ap.add_argument('--include-floor', action='store_true', help='also emit floor (unmatched indirect) edges')
    ap.add_argument('--embed', metavar='COURSE_JSON', help='write a pathway + tier slice into this course.json')
    ap.add_argument('--pathway', help='pathway id for --embed, e.g. ai-technology')
    ap.add_argument('--tier', choices=TIERS, help='tier for --embed')
    args = ap.parse_args()

    lib = build(args.include_floor)
    os.makedirs(os.path.dirname(OUT), exist_ok=True)
    write_json(OUT, lib)
    count = collections.Counter((s['pathway'], s['tier']) for s in lib['sets'])
    print('wrote', os.path.relpath(OUT, REPO_ROOT), '| sets:', len(lib['sets']),
          '| pathway x tier cells:', len(count), '| min/max per cell:',
          min(count.values()), max(count.values()))

    if args.embed:
        if not (args.pathway and args.tier):
            raise SystemExit('--embed needs --pathway and --tier')
        course = json.load(open(args.embed, encoding='utf-8'))
        libs = course.get('_growPromptLibraries') or {}
        libs[LIB_ID] = slice_for(lib, args.pathway, args.tier)
        course['_growPromptLibraries'] = libs
        write_json(args.embed, course)
        print('embedded %s / %s into %s as _growPromptLibraries["%s"]' % (
            args.pathway, args.tier, args.embed, LIB_ID))
