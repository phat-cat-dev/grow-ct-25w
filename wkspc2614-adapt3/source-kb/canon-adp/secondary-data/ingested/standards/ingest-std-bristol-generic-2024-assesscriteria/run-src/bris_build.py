#!/usr/bin/env python3
"""Build ingest-std-bristol-generic-2024-assesscriteria.md (run 0050). std."""
import sys, json, re, hashlib, collections
sys.path.insert(0, '/tmp/claude-0/-home-claude-wkspc2600-uni/378bff94-17ab-5a5d-8465-bd8449aca2a6/scratchpad')
from bris_common import *
import ac_terms as A, ac_build as B
q = B.q
HB = S + '/bris_hold'
raw = open(HB + '/bristol-marking-criteria-2024.txt', 'rb').read(); normb = open(HB + '/bristol-marking-criteria-2024.norm.txt', 'rb').read(); norm = normb.decode('utf-8')
ns = {}
for f in ['bris_v4.py', 'bris_v5.py', 'bris_v67.py']: exec(open(S + '/' + f).read(), ns)
V = {**ns['V'], **ns['V5'], **ns['V67']}
MARKS = {'0-19': '0, 7, 15', '20-39': '22, 29, 35', '40-49': '42, 45, 48', '50-59': '52, 55, 58', '60-69': '62, 65, 68', '70-79': '72, 75, 78', '80-100': '83, 94, 100', '0-39': '0, 7, 15, 22, 29, 35'}
UK = {4: {'0-19': 'fail', '20-39': 'fail', '40-49': 'third (pass)', '50-59': 'lower second', '60-69': 'upper second', '70-79': 'first', '80-100': 'first'},
      7: {'0-39': 'fail', '40-49': 'fail (below the level 7 pass)', '50-59': 'pass', '60-69': 'merit', '70-79': 'distinction', '80-100': 'distinction'}}
UK[5] = UK[6] = UK[4]
PASS = {4: 40, 5: 40, 6: 40, 7: 50}
LH = {4: 'Level 4 (First-year undergraduate level)', 5: 'Level 5 (Second-year undergraduate level)', 6: 'Level 6 (Third-year undergraduate level)', 7: 'Level 7 (Masters level)'}
PDF = {4: ('university-marking-criteria-level4.pdf', '7b72fa184ddf94adc8a5651a980816290cd294a5b5bf4231982077e0a9fbf452', '2024-09-26'), 5: ('university-marking-criteria-level5.pdf', '8eab5f2536c604745d21e1ad7299daea6535fbf97771034fdd773e00477a7057', '2024-09-26'), 6: ('university-marking-criteria-level6.pdf', 'cc0fe234d639849c248b3187f940143d43da591ddb24ce2d7a0858d3f24cd50d', '2024-09-26'), 7: ('university-marking-criteria-level7.pdf', 'fa344aea46c0e30482075309af57913a3a38243666241af68770dca0e7a67140', '2024-10-08')}
ID = lambda i: 'bristol/generic-2024/' + i
FIELDS = {  # criterion slug -> (issuer field, stated?, ACPRAC-DAT pathways inferred)
 'content-knowledge': ('Knowledge and understanding', ['criticality']),
 'critical-approach': ('Critical approach', ['criticality']),
 'use-of-evidence-and-sources': ('Use of evidence and sources', ['finding-and-using-sources', 'criticality']),
 'logical-argument-and-evaluation-of-perspectives': ('Logical argument and evaluation of perspectives', ['criticality', 'academic-writing']),
 'logical-argument-explanation-and-evaluation-of-perspectives': ('Logical argument, explanation and evaluation of perspectives', ['criticality', 'academic-writing']),
 'explanation-application-and-interpretation': ('Explanation, application and interpretation', ['criticality']),
 'explanation-and-interpretation': ('Explanation and interpretation', ['criticality', 'academic-writing']),
 'problem-solving': ('Problem-solving', ['creativity', 'criticality']),
 'specialist-skills-and-techniques': ('Specialist skills and techniques', ['researching-and-research-methods']),
 'specialist-skills-techniques-and-research': ('Specialist skills, techniques and research', ['researching-and-research-methods']),
 'research': ('Research', ['researching-and-research-methods']),
 'academic-skills': ('Academic skills', ['referencing', 'academic-writing']),
 'teamwork': ('Teamwork', ['work-based-and-experiential-learning']),
 'insight': ('Insight', ['reflective-practice']),
 'decision-making': ('Decision-making', ['work-based-and-experiential-learning']),
 'communication': ('Communication', ['presenting']),
 'self-management': ('Self-management', ['starting-progressing-and-succeeding']),
}
T = A.taxonomy(); FE = B.fheq_echoes()
C = cells(); pos = 0
for c in C:
    lab = f"L{c['level']} | {c['category']} | {c['criterion']} | {c['bsp']} | {c['band']} ({MARKS[c['band']]}) "
    i = norm.index(lab, pos); s = i + len(lab); t = ' '.join(c['text'].split())
    assert norm[s:s + len(t)] == t, (c['id'], norm[s:s + 60], t[:60]); c['span'] = (s, s + len(t)); pos = s + len(t)
    c['terms'] = B.terms(c['text'], T); c['bandpos'] = c['band']; c['echo'] = B.echo(c['text'], FE)
    c['prac'], c['ben'] = V[c['first']]
LEVELS = [4, 5, 6, 7]
crit_by_level = {L: [] for L in LEVELS}
for c in C:
    if c['crit'] not in [x[0] for x in crit_by_level[c['level']]]: crit_by_level[c['level']].append((c['crit'], c['name'], c['category'], c['bsp']))
o = []; w = o.append
w(f'''---
id: std:doc:bristol-generic-2024-assesscriteria
title: University marking criteria, levels 4 to 7
profile: standards/assessment-criteria
profileVersion: 0.1.6-draft
issuer: University of Bristol
kind: assessment-criteria
jurisdiction: [England]
subjectScope: universal
subjects: []
edition: "2024 (PDFs created 2024-09-26, levels 4 to 6; 2024-10-08, level 7)"
published: unknown
status: unknown   # current as supplied by Abbott; not checked against the issuer's site (Part E)
supersedes: unknown
heldText: {{ method: sha256-bytes, raw: {hashlib.sha256(raw).hexdigest()}, normalised: {hashlib.sha256(normb).hexdigest()} }}
originals:''')
for L in LEVELS: w(f'  - {{ level: {L}, file: {PDF[L][0]}, method: sha256-bytes, sha256: {PDF[L][1]}, created: {PDF[L][2]}, held: no }}')
w(f'''scope: institution
levelsCovered: [fheq:4, fheq:5, fheq:6, fheq:7]
assessmentKinds: any   # none stated; "an overarching framework for student attainment" (AC1)
criteria:''')
for L in LEVELS: w(f'  l{L}: [{", ".join(q(x[1]) for x in crit_by_level[L])}]')
w('bands:')
for L in LEVELS: w(f'  l{L}: [{", ".join(q(b + " (" + MARKS[b] + ")") for b in BANDS[str(L)])}]')
w(f'''parts:
  S: full
  AC: full
  B: full
  C: "not-applicable: the use rules are in the issuer's regulations (section 15), not held"
pins: {{ structure: 0.13.0-draft, template: "wpk-0016-ingest-pd-template-standards-assessment-criteria.md 0.1.0-draft", runFrame: 0.1.1-draft, runLayer: 0.5.0-draft, standards: none yet, terminology: none yet }}
lifecycle: drafted
researchedBy: run frame 0.1.1-draft; standards run layer 0.5.0-draft; std, run 0050
passes:
  P1: "2026-10-03, std (claude.ai, META Project)"
  P2: "skipped: read direct from the issuer's PDFs (byte hashes match nts's index)"
  P3: open
version: 0.1.0
---

<!-- from INGEST wpk-0016-ingest-pd-template-standards-assessment-criteria.md 0.1.0-draft (profile 0.1.6-draft, P5a) -->
# University of Bristol: University marking criteria, levels 4 to 7 (2024)

> Run 0050, P1 by std: the `assessment-criteria` pilot. Four level documents ingested as one set; the opening they share is held once. The issuer's words are held in UNI only (`wkspc2601-library/txt/university-of-bristol-2024-marking-criteria-levels-4-to-7-standard.norm.txt`, the grids cell by cell); every cell points into them by character span. Everything else is our words. Term lists (AC6) are the issuer's single words and short phrases, counted.

## Part 0 Summary

### 0.1 Agent definition
<!-- label: editorial; status: drafted; basis: primary -->
The University of Bristol's generic marking criteria for levels 4 to 7: for each level, a grid of 11 to 14 criteria in four categories, each described in seven mark bands (six at level 7). Reach for it to see how one institution grades work against the FHEQ levels, band by band, and to borrow its degree ladder and verbs when writing criteria. It is a measuring instrument for the FHEQ levels, not a statement of them.

### 0.2 Summary
<!-- label: both; status: drafted; basis: primary -->
''' + f'''A shared opening states four aims (help students see what to aim for, consistent marking, commensurability with the FHEQ and the OfS sector standards, a base for discipline criteria), ties the pass mark at award level to the programme's intended learning outcomes, and links every criterion to the Bristol Skills Profile (BSP, 27 skills in nine groups, organised as knowing, doing and being). Each level then gives a grid: rows are criteria grouped under Knowledge and understanding; Intellectual skills; Scholarly, research and disciplinary practices; Professional and life skills; columns are mark bands with three fixed mark points each. The criteria list changes by level (11, 12, 14, 12). {len(C)} cells in all, {len(set(c["first"] for c in C))} distinct texts: many cells repeat word for word across levels, chiefly the professional and life skills. Progression across bands runs on a degree ladder (very limited, limited, some, consistent, good, thorough, excellent, exceptional) and a guidance-to-autonomy ladder; across levels it runs on scope words (introductory, well-established, specialist, complex, forefront) and sources (directed reading, then sources beyond the set range, then current research). Several pass-band cells at levels 5 and 6 reuse the FHEQ's own wording (AC5 `echoes`).

## Part S Standard

### S1 Identity
```yaml
issuer: University of Bristol
title: "University marking criteria: level 4 (and levels 5, 6, 7)"
edition: 2024
dates: {{ published: unknown, other: ["PDF creation dates: 2024-09-26 (levels 4 to 6), 2024-10-08 (level 7)"] }}
kind: assessment-criteria
jurisdiction: [England]
authority: institutional   # the issuer's own marking criteria, governed by its taught programmes code, section 15
licence: none stated
copyrightNotice: none-stated
```

### S2 Purpose and scope
```yaml
governs: generic marking of student work at levels 4 to 7
appliesTo: {{ awards: none-stated, levels: [fheq:4, fheq:5, fheq:6, fheq:7], providers: University of Bristol }}
whoMustUse: none-stated   # section 15 of the Regulations and Code of Practice for Taught Programmes governs use (not held)
howUsed: [marking, guiding students, writing discipline criteria]
doesNot: none-stated
beneficiary: the student
statedScope: "an overarching framework for student attainment"
statedSubjects: none-stated
```

### S3 Structure
```yaml
components:
  - {{ number: opening, componentType: preamble, heading: "the shared opening: four aims, the pass-mark rule, the four categories and the BSP", parts: [l4, l5, l6, l7] }}''')
for L in LEVELS: w(f'  - {{ number: l{L}, componentType: level, heading: {q(LH[L])}, criteria: {len(crit_by_level[L])}, bands: {len(BANDS[str(L)])} }}')
w('''excluded:
  - { number: "BSP table", heading: "the Bristol Skills Profile (27 skills)", kind: "other: cross-reference vocabulary; codes recorded in AC4, the skill names held only" }
```

## Part AC Assessment criteria

### AC1 Set
<!-- label: source; status: drafted; basis: primary -->
```yaml
issuer: University of Bristol
scope: institution
purpose:   # the issuer's four aims, our words
  - help students see what learning to aim for at each level, in subject knowledge and skills
  - support consistent marking within and across programmes
  - keep marks commensurate with external frameworks, the FHEQ and the OfS sector standards derived from it
  - give a base for discipline-relevant marking criteria
levelsCovered: [fheq:4, fheq:5, fheq:6, fheq:7]
alignsWith: [{ framework: std:doc:qaa-fheq-2024-framework, basis: stated }, { framework: "OfS sector-recognised standards", basis: stated }]
passRule: "the criteria for the pass mark at award level (40 at level 6, 50 at level 7) should align with the programme's intended learning outcomes, which every student must attain for an award (opening)"
useRules: "Regulations and Code of Practice for Taught Programmes, section 15 (cited, not held)"
crossReference: { name: Bristol Skills Profile (BSP), codes: "1a to 9c", groups: ["1 to 3: what will I learn (knowing)", "4 to 6: what will I be able to do (doing)", "7 to 9: what will I become (being)"], basis: stated }
categoryFrame: "knowing leads in category 1, doing in categories 2 and 3, being in category 4 (opening, our words)"
```

### AC2 Levels
```yaml''')
for L in LEVELS:
    w(f'- {{ level: l{L}, label: {q(LH[L])}, framework: fheq:{L}, frameworkBasis: stated, passMark: {PASS[L]}, awardPassMark: {"40 (at level 6)" if L < 7 else "50"}, part: {PDF[L][0]} }}')
w('''```

### AC3 Bands
<!-- Mark ranges and mark points exactly as given. `uk` is our reading of the band against UK honours classes (undergraduate) and master's outcomes (level 7); the issuer labels bands by marks only. -->
```yaml''')
for L in LEVELS:
    w(f'l{L}:')
    for b in BANDS[str(L)]:
        lo = int(b.split('-')[0]); w(f'  - {{ range: "{b}", points: [{MARKS[b]}], pass: {"true" if lo >= PASS[L] else "false"}, threshold: {"true" if lo == PASS[L] else "false"}, uk: {q(UK[L][b])} }}')
w('''```
Level 7 merges the two lowest bands into one, 0-39, with six mark points; levels 4 to 6 keep 0-19 and 20-39 apart.

### AC4 Categories and criteria
<!-- The issuer's order per level. BSP codes are the issuer's cross-references. -->

| Criterion | Category | L4 | L5 | L6 | L7 |
|---|---|---|---|---|---|''')
allc = []
for L in LEVELS:
    for slug_, name, cat, bsp in crit_by_level[L]:
        if slug_ not in [x[0] for x in allc]: allc.append((slug_, name, cat))
for slug_, name, cat in allc:
    cellsL = []
    for L in LEVELS:
        m = [x for x in crit_by_level[L] if x[0] == slug_]
        cellsL.append(m[0][3] if m else '(absent)')
    w(f'| {name} | {cat} | ' + ' | '.join(cellsL) + ' |')
w('''
### AC5 Cells
<!-- One record per level, criterion and band. `sameAs`: the cell's text repeats an earlier cell's (case, spacing and a few function words aside); its versions are that cell's. `echoes`: the longest run of seven or more words the cell shares with an FHEQ statement (std:doc:qaa-fheq-2024-framework), our finding. Terms: AC6. -->
```yaml''')
for c in C:
    tm = c['terms']
    vb = ', '.join('{ lemma: ' + q(v['lemma']) + ', form: ' + q(v['form']) + ', taxonomy: [' + ', '.join(q(x) for x in v['taxonomy']) + '] }' for v in tm['verbs'])
    lst = lambda k: '[' + ', '.join(q(x) for x in tm[k]) + ']'
    ec = f'{{ statement: {c["echo"][0]}, words: {c["echo"][2]} }}' if c['echo'] else 'none'
    w(f'''- id: {ID(c['id'])}
  level: l{c['level']}
  category: {q(c['category'])}
  criterion: {q(c['name'])}
  band: {{ range: "{c['band']}", points: [{MARKS[c['band']]}] }}
  span: {{ start: {c['span'][0]}, end: {c['span'][1]} }}
  sameAs: {ID(c['first']) if c['first'] != c['id'] else 'none'}
  echoes: {ec}
  force: describes
  paraphrase: {q(c['prac'])}   # for grid cells the paraphrase is the practitioner version
  terms:
    verbs: [{vb}]
    objects: {lst('objects')}
    degree: {lst('degree')}
    independence: {lst('independence')}
    scope: {lst('scope')}
    deficits: {lst('deficits')}''')
w('''```

### S4a Audience versions
<!-- label: both; status: drafted; basis: primary. forPractitioner: what a marker looks for; forBeneficiary: what the student shows in that band, second person, naming no issuer. Cells marked sameAs carry the first cell's versions. -->
```yaml''')
for c in C:
    w(f'''- cell: {ID(c['id'])}
  forPractitioner: {{ text: {q(c['prac'])}, rewrite: light, force: describes, status: drafted }}
  forBeneficiary: {{ text: {q(c['ben'])}, rewrite: full, force: describes, status: drafted }}''')
w('```')
# AC6
LX = B.lexicon(C)
BP = BANDS['4']
def bandcount(e):
    m = {'0-39': '0-19'}
    cnt = collections.Counter()
    for b, n in e['bands'].items(): cnt[m.get(b, b)] += n
    return ' '.join(f'{cnt.get(b, 0)}' for b in BP)
w('''
### AC6 Terms
<!-- The set's lexicon: each term with its count over all cells, the levels it appears in, and its count per band (columns 0-19, 20-39, 40-49, 50-59, 60-69, 70-79, 80-100; level 7's 0-39 counted under 0-19). Taxonomy placements are from INGEST's revised Bloom and SOLO documents (ing:doc:bloom-anderson-krathwohl-2001, ing:doc:solo-biggs-collis-1982), whose own caution stands: a verb's level depends on its object. -->
''')
for k, title in (('verbs', 'Performance verbs (lemma)'), ('objects', 'Objects'), ('degree', 'Qualifiers of degree'), ('independence', 'Independence'), ('scope', 'Scope'), ('deficits', 'Negations and deficits')):
    w(f'#### {title}\n\n| Term | Count | Levels | By band (0-19 to 80-100) |' + (' Taxonomy |' if k == 'verbs' else '') + '\n|---|---|---|---|' + ('---|' if k == 'verbs' else ''))
    for term, e in sorted(LX[k].items(), key=lambda x: -x[1]['n']):
        if e['n'] < 2 and k in ('objects',): continue
        tx = ''
        if k == 'verbs':
            p = T.get(term) or T.get(term.replace('ise', 'ize')) or []
            tx = ' ' + ('; '.join(f'{s}: {"/".join(c)}' for s, c in p) or 'none') + ' |'
        w(f'| {term} | {e["n"]} | {",".join(str(x) for x in sorted(e["levels"]))} | {bandcount(e)} |{tx}')
    w('')
POS = {b: i for i, b in enumerate(BP)}; POS['0-39'] = 0.5
LAD = B.ladder(C, lambda c: POS[c['band']])
w('''#### AC6.1 The set's ladders
<!-- Each degree and independence term used three or more times, placed by the mean position of the bands it appears in (0 = 0-19, 6 = 80-100), lowest first: the set's own ladder, read from counts. -->

| Mean band position | Term | Kind | Count |
|---|---|---|---|''')
for m, term, k, n in LAD: w(f'| {m:.1f} ({BP[min(6, round(m))]}) | {term} | {k} | {n} |')
w('')
# AC7 progressions
w('''### AC7 Progressions

#### AC7.1 Across bands within a level
<!-- For each level, the degree, independence and deficit words that mark each band, summed over all criteria (counts). Read left to right: what changes from fail to the top band. -->
''')
for L in LEVELS:
    w(f'**Level {L}**\n\n| Band | Degree | Independence | Deficits |\n|---|---|---|---|')
    for b in BANDS[str(L)]:
        cs = [c for c in C if c['level'] == L and c['band'] == b]
        fmt = lambda k: ', '.join(f'{t} {n}' for t, n in collections.Counter(x for c in cs for x in c['terms'][k]).most_common(6)) or '(none)'
        w(f'| {b} | {fmt("degree")} | {fmt("independence")} | {fmt("deficits")} |')
    w('')
w('''#### AC7.2 Across levels within a band
<!-- For each criterion present at three or more levels, the scope and object words of the pass band (40-49 at levels 4 to 6, 50-59 at level 7) and of the top band, by level: what the same band asks as the level rises. -->

| Criterion | Band | L4 | L5 | L6 | L7 |
|---|---|---|---|---|---|''')
def pick(L, crit, top):
    b = BANDS[str(L)][-1] if top else ('50-59' if L == 7 else '40-49')
    m = [c for c in C if c['level'] == L and c['crit'] == crit and c['band'] == b]
    if not m: return '(absent)'
    t = m[0]['terms']; return ', '.join(dict.fromkeys(t['scope'] + t['objects'] + t['independence'])) or '(none)'
for slug_, name, cat in allc:
    if sum(1 for L in LEVELS if any(x[0] == slug_ for x in crit_by_level[L])) < 3: continue
    for top in (False, True):
        w(f'| {name} | {"top" if top else "pass"} | ' + ' | '.join(pick(L, slug_, top) for L in LEVELS) + ' |')
open(S + '/bris_obs.md').read() and w(open(S + '/bris_obs.md').read())
w('''
### AC8 Fields
<!-- The issuer's criterion name as its own field (`stated`), and the academic practice pathways (ACPRAC-DAT's thirteen, as named in its charter) each criterion assesses (`inferred`). -->
```yaml''')
for slug_, name, cat in allc:
    f, pw = FIELDS[slug_]
    w(f'- {{ criterion: {q(name)}, fields: [{{ field: {q(f)}, basis: stated }}' + ''.join(f', {{ field: {p}, basis: inferred }}' for p in pw) + '] }')
w('''```

## Part B Terminology
```yaml
- { term: "marking criteria", gloss: "the issuer's name for the set: generic descriptions of attainment by level and mark band", basis: paraphrase }
- { term: "mark band", gloss: "a range of marks with its own descriptor (0-19 to 80-100), each with three fixed mark points", basis: paraphrase }
- { term: "mark points", gloss: "the fixed marks a marker may award within a band (for example 42, 45, 48)", basis: inferred }
- { term: "pass mark at award level", gloss: "40 at level 6, 50 at level 7; the criteria defining it align with the programme's intended learning outcomes", basis: paraphrase }
- { term: "Bristol Skills Profile (BSP)", gloss: "the issuer's 27 skills in nine groups, cross-referenced from each criterion", basis: paraphrase }
- { term: "being, doing, knowing", gloss: "the frame of the issuer's curriculum framework that the four categories follow", basis: paraphrase }
```

## Part C Process
`not-applicable`: how the criteria are used is set in the issuer's taught programmes code, section 15, which is not held.

## Part D Sources
```yaml
- key: D1
  issuer: University of Bristol
  title: "University marking criteria: levels 4, 5, 6 and 7 (four PDFs)"
  year: 2024
  url: unknown
  retrieved: "PDFs attached by Abbott, 2026-10-03, 03:52 (to nts) and 04:49 (to std)"
  licence: none stated
  tier: primary
  readVia: direct
  held: ''' + hashlib.sha256(raw).hexdigest() + '''
  heldFiles: [wkspc2601-library/txt/university-of-bristol-2024-marking-criteria-levels-4-to-7-standard.txt, wkspc2601-library/txt/university-of-bristol-2024-marking-criteria-levels-4-to-7-standard.norm.txt, wkspc2601-library/txt/university-of-bristol-2024-marking-criteria-level-4-standard.txt, wkspc2601-library/txt/university-of-bristol-2024-marking-criteria-level-5-standard.txt, wkspc2601-library/txt/university-of-bristol-2024-marking-criteria-level-6-standard.txt, wkspc2601-library/txt/university-of-bristol-2024-marking-criteria-level-7-standard.txt, wkspc2601-library/records/<name>.held.json]
  citedIn: [S1, S2, S3, AC1, AC2, AC3, AC4, AC5, S4a, AC6, AC7, AC8]
- { key: D2, ref: std:doc:qaa-fheq-2024-framework, use: "AC2 level links; AC5 echoes" }
- { key: D3, ref: "ing:doc:bloom-anderson-krathwohl-2001; ing:doc:solo-biggs-collis-1982", use: "AC6 verb placements" }
```

### D2 Research log
```yaml
- { ref: D1, tier: primary, consulted: 2026-10-03, pass: P1, outcome: "the four PDFs read direct (byte hashes match index.json); grids extracted cell by cell with pdfplumber, cells continued across page breaks rejoined; held as one text with the shared opening once, normalised with stan's tool (word sequence equal)" }
```

### D3 Wanted sources
```yaml
- { citation: "the issuer's Regulations and Code of Practice for Taught Programmes, section 15 (use of marking criteria)", settles: [S2, C], asked: not yet, state: wanted }
- { citation: "the issuer's web page for these criteria: date, status, licence", settles: [S1], asked: not yet, state: wanted }
```

## Part E Gaps and questions
''' + open(S + '/bris_parte.md').read() + '''
---

## Change notes
- 0.1.0: 2026-10-03: researched by run frame 0.1.1-draft and standards run layer 0.5.0-draft under the assessment-criteria template 0.1.0-draft, std, run 0050 (P1).''')
open(sys.argv[1], 'w', encoding='utf-8').write('\n'.join(o) + '\n')
json.dump([{k: c[k] for k in ('id', 'level', 'crit', 'band', 'span', 'first', 'echo', 'terms')} for c in C], open(S + '/bris-cells-final.json', 'w'), indent=1)
print(len(C), 'cells')
