#!/usr/bin/env python3
"""Build ingest-std-cardiffmet-generic-2020-assesscriteria.md (run 0051). std."""
import sys, json, re, hashlib, collections
sys.path.insert(0, '/tmp/claude-0/-home-claude-wkspc2600-uni/378bff94-17ab-5a5d-8465-bd8449aca2a6/scratchpad')
from cmet_common import *
import ac_terms as A, ac_build as B
q = B.q
SLUGF = 'cardiffmet-generic-band-descriptors-2020'
HB = S + '/cmet_hold'
raw = open(f'{HB}/{SLUGF}.txt', 'rb').read(); normb = open(f'{HB}/{SLUGF}.norm.txt', 'rb').read(); norm = normb.decode('utf-8')
ns = {}
for f in ['cmet_v3.py', 'cmet_v45.py', 'cmet_v67.py']: exec(open(S + '/' + f).read(), ns)
V = {**ns['V3'], **ns['V45'], **ns['V67']}
DOCX = ('AH1_04_03.docx', 'ca39c478a6509612c24d07ad19b3785ee927638539c80c9695422dc7b90c1711')
ID = lambda i: 'cardiffmet/generic-2020/' + i
LEVELS = [3, 4, 5, 6, 7]
PASS = {3: 40, 4: 40, 5: 40, 6: 40, 7: 50}
FW = {3: ('cqfw:3', 'inferred'), 4: ('fheq:4', 'stated'), 5: ('fheq:5', 'stated'), 6: ('fheq:6', 'stated'), 7: ('fheq:7', 'stated')}
NAME = {'overall': 'Overall summary', 'knowledge': 'Knowledge & Understanding', 'presentation': 'Presentation and communication', 'analysis': 'Analysis & discussion', 'research': 'Research / scholarship', 'argument': 'Structured argument and critical evaluation'}
FIELDS = {'overall': ('Overall summary', []), 'knowledge': ('Knowledge & Understanding', ['criticality']), 'presentation': ('Presentation and communication', ['academic-writing', 'presenting']), 'analysis': ('Analysis & discussion', ['criticality', 'researching-and-research-methods']), 'research': ('Research / scholarship', ['finding-and-using-sources', 'referencing', 'researching-and-research-methods']), 'argument': ('Structured argument and critical evaluation', ['criticality', 'reflective-practice', 'academic-writing'])}
AX = ['fail-low', 'fail-high', '40-49', '50-59', '60-69', '70-79', '80-100']
def axis(b):
    lo = int(b.split('-')[0])
    return 'fail-low' if lo < 20 or b == '1-29' else 'fail-high' if lo < 40 else b
T = A.taxonomy(); FE = B.fheq_echoes()
C = resolved(0.95); pos = 0
for c in C:
    lab = f"L{c['level']} | {c['criterion']} | {c['label']} "
    i = norm.index(lab, pos); s = i + len(lab)
    t = ' '.join(c['text'].split()) if c['text'] else '(empty cell: the band-wide descriptor is in the Knowledge & Understanding row)'
    assert norm[s:s + len(t)] == t, (c['id'], norm[s:s + 80]); c['span'] = (s, s + len(t)); pos = s + len(t)
    c['terms'] = B.terms(c['text'], T) if c['text'] else {k: [] for k in ('verbs', 'objects', 'degree', 'independence', 'scope', 'deficits')}
    c['bandpos'] = axis(c['band']); c['echo'] = B.echo(c['text'], FE) if c['text'] else None
    c['prac'], c['ben'] = V[c['src']] if c['text'] else (None, None)
LAB = {}
for L in LEVELS: LAB[L] = G[str(L)]['bands']
o = []; w = o.append
w(f'''---
id: std:doc:cardiffmet-generic-2020-assesscriteria
title: "Guidance on Assessment Marking: Generic Band Descriptors, levels 3 to 7"
profile: standards/assessment-criteria
profileVersion: 0.1.6-draft
issuer: Cardiff Metropolitan University
kind: assessment-criteria
jurisdiction: [Wales]
subjectScope: universal
subjects: []
edition: "version 6 (approved 2008-09-04; reviewed Apr 2010, Feb 2011, May 2015, Jul 2019, Nov 2020; next review 2023)"
published: unknown
status: "unknown: the stated next review (2023) has passed; the file supplied was saved 2026-08-10"
supersedes: none-stated
heldText: {{ method: sha256-bytes, raw: {hashlib.sha256(raw).hexdigest()}, normalised: {hashlib.sha256(normb).hexdigest()} }}
originals:
  - {{ file: {DOCX[0]}, method: sha256-bytes, sha256: {DOCX[1]}, held: no }}
scope: institution
levelsCovered: [cqfw:3, fheq:4, fheq:5, fheq:6, fheq:7]
assessmentKinds: any   # every type, coursework and examinations among them (key principles)
criteria: [{", ".join(q(NAME[k]) for k in NAME)}]   # the same six rows at every level
bands:''')
for L in LEVELS: w(f'  l{L}: [{", ".join(q(b) for b in LAB[L])}]')
w(f'''parts:
  S: full
  AC: full
  B: full
  C: described
pins: {{ structure: 0.13.0-draft, template: "wpk-0016-ingest-pd-template-standards-assessment-criteria.md 0.1.0-draft", runFrame: 0.1.1-draft, runLayer: 0.5.0-draft, standards: none yet, terminology: none yet }}
lifecycle: drafted
researchedBy: run frame 0.1.1-draft; standards run layer 0.5.0-draft; std, run 0051
passes:
  P1: "2026-10-03, std (claude.ai, META Project)"
  P2: "skipped: read direct from the issuer's .docx"
  P3: open
version: 0.1.0
---

<!-- from INGEST wpk-0016-ingest-pd-template-standards-assessment-criteria.md 0.1.0-draft (profile 0.1.6-draft, P5a) -->
# Cardiff Metropolitan University: Generic Band Descriptors, levels 3 to 7

> Run 0051, P1 by std: the second `assessment-criteria` set, ingested for comparison with Bristol (run 0050) and to fix the template. The descriptors are tables A to E of the Academic Handbook's Guidance on Assessment Marking (AH1 4.3). The issuer's words are held in UNI only (`held/assessment-criteria/{SLUGF}.norm.txt`); every cell points into them by character span. Everything else is our words. Of the three handbook files supplied, only AH1 4.3 holds criteria: the two programme specification templates (AH2 1.2B and 1.2C) ask only for a mapping of each level to the FHEQ descriptors.

## Part 0 Summary

### 0.1 Agent definition
<!-- label: editorial; status: drafted; basis: primary -->
Cardiff Metropolitan University's Generic Band Descriptors (GBDs): for each of levels 3 to 7, an overall summary and five criteria described in seven percentage bands, each band named by its degree classification (first class to clear fail; at level 7, distinction to fail). Reach for it to see a band scale written in prose paragraphs and tied by name to the UK classes, and to compare with Bristol's short-cell grid. It is a measuring instrument for the FHEQ levels (and a foundation level 3), not a statement of them.

### 0.2 Summary
<!-- label: both; status: drafted; basis: primary -->
The guidance sets four aims (consistent marking, confidence to use the whole 0 to 100 scale, fine distinctions at borderlines, students' understanding of what a mark needs), aligns the descriptors with the FHEQ qualification descriptors (2014 edition), applies them to every undergraduate and taught master's programme and every assessment type, and asks that they be used with discipline and assessment-specific descriptors built on the same principles. Its writing rules are explicit: plain language for staff and students; pass bands in positive terms; each band describes its own work, not what it lacks against the band above; best fit across two bands; formative use. Each level has the same six rows (overall summary; knowledge and understanding; presentation and communication; analysis and discussion; research and scholarship; structured argument and critical evaluation) in 10-mark bands named by classification. {len(C)} cells, of which {sum(1 for c in C if c['text'] and c['src']==c['id'])} carry their own versions; the rest repeat or nearly repeat an earlier level. Cells are paragraphs of several sentences, modal at levels 3 and 4 ("may demonstrate") and plain at 5 to 7 ("demonstrates").

## Part S Standard

### S1 Identity
```yaml
issuer: Cardiff Metropolitan University
title: "Academic Handbook AH1 4.3: Guidance on Assessment Marking (Generic Band Descriptors, tables A to E)"
edition: version 6
dates: {{ published: unknown, other: ["approved 2008-09-04 (Academic Board via AQSC)", "reviews: Apr 2010, Feb 2011, May 2015, Jul 2019, Nov 2020", "next review stated: 2023"] }}
kind: assessment-criteria
jurisdiction: [Wales]
authority: institutional   # policy owner: Chief Student Officer, Registry Services
licence: none stated
copyrightNotice: none-stated
```

### S2 Purpose and scope
```yaml
governs: generic marking of undergraduate (levels 3 to 6) and taught master's (level 7) work, every assessment type
appliesTo: {{ awards: [undergraduate degrees, taught master's degrees], levels: [cqfw:3, fheq:4, fheq:5, fheq:6, fheq:7], providers: Cardiff Metropolitan University }}
whoMustUse: "markers and moderators; students, who are to discuss the descriptors at the start of each year"
howUsed: [summative marking, formative feedback, target setting, writing discipline descriptors]
doesNot: "replace discipline- or assessment-specific descriptors, which supplement them"
beneficiary: the student
statedScope: "all undergraduate or taught Master's degree programmes and all types of assessment"
statedSubjects: none-stated
```

### S3 Structure
```yaml
components:
  - {{ number: guidance, componentType: preamble, heading: "introduction, aims, key principles, role in learning and assessment, structure, the zero rule, simplified versions" }}''')
for L in LEVELS: w(f'  - {{ number: l{L}, componentType: level, heading: "Table {"ABCDE"[L-3]}: generic level {L} band descriptors", criteria: 6, bands: 7 }}')
w('''excluded:
  - { number: "key details and version control tables", heading: "policy metadata", kind: "other: recorded in S1" }
  - { number: "AH2 1.2B, AH2 1.2C", heading: "programme specification templates", kind: "other: no criteria; supplied with the set" }
```

## Part AC Assessment criteria

### AC1 Set
```yaml
issuer: Cardiff Metropolitan University
scope: institution
purpose:   # the issuer's four aims, our words
  - make marking more consistent across the university
  - give assessors confidence to use the whole range from 0 to 100
  - help assessors make fine distinctions, above all at borderlines
  - help students see what a mark or classification requires
levelsCovered: [cqfw:3, fheq:4, fheq:5, fheq:6, fheq:7]
alignsWith: [{ framework: "QAA FHEQ qualification descriptors (November 2014 edition); now std:doc:qaa-fheq-2024-framework", basis: stated }]
passRule: "pass descriptors are 40 and above (undergraduate) and 50 and above (postgraduate), written in positive terms"
writingRules:   # the issuer's principles for the descriptors themselves, our words
  - plain, direct language without jargon, for staff and students alike
  - pass bands in positive terms
  - each band describes its own work and does not say what it lacks against the band above
  - work that shows two neighbouring bands is placed by best fit, a professional judgement
  - descriptors serve formative feedback too: a student sees what the next band up asks
useRules: "used with discipline- and assessment-specific descriptors developed on the same principles; students discuss outcomes, tasks, criteria and descriptors at the start of each year; zero for no attempt or for substantiated unfair practice"
crossReference: none
```

### AC2 Levels
```yaml''')
for L in LEVELS:
    w(f'- {{ level: l{L}, label: "Level {L}", framework: {FW[L][0]}, frameworkBasis: {FW[L][1]}, passMark: {PASS[L]}, table: "{"ABCDE"[L-3]}" }}')
w('''```
Level 3 has no FHEQ level; the issuer calls it undergraduate. It is linked to CQFW level 3 by inference (the issuer is in Wales, where the FHEQ is part of the CQFW; std:doc:qaa-fheq-2024-framework, 2.23).

### AC3 Bands
<!-- As given, in the issuer's order (highest first). `uk` is the issuer's own classification label; `axis` is our common column for comparison with other sets. -->
```yaml''')
for L in LEVELS:
    w(f'l{L}:')
    for b in LAB[L]:
        r = rng(b); lo = int(r.split('-')[0]); lab = re.sub(r'^[^(]*\(?', '', b).rstrip(')') if '(' in b else 'none'
        w(f'  - {{ label: {q(b)}, range: "{r}", points: none, pass: {"true" if lo >= PASS[L] else "false"}, threshold: {"true" if lo == PASS[L] else "false"}, uk: {q(lab)}, axis: {axis(r)} }}')
w('''```
A mark of zero sits outside the bands: it is given for no attempt or for substantiated unfair practice, and is a fail. The 80-100 band is split in the overall summary: 80-89 excellent, 90-100 outstanding and exceptional.

### AC4 Categories and criteria
The same six rows at every level, in this order, with no grouping and no cross-references: Overall summary; Knowledge & Understanding; Presentation and communication; Analysis & discussion; Research / scholarship; Structured argument and critical evaluation. At level 7 the lowest band (1-19) has one band-wide descriptor, in the Knowledge & Understanding row; the four rows below it are empty.

### AC5 Cells
<!-- One record per level, criterion and band. `sameAs`: same text as an earlier cell (level numbers masked). `like`: nearly the same text as the same criterion and band at an earlier level (word similarity 0.95 or more); versions are that cell's. `spans`: the cell stands for the whole band. `echoes`: a run of seven or more words shared with an FHEQ statement, our finding. -->
```yaml''')
for c in C:
    tm = c['terms']
    vb = ', '.join('{ lemma: ' + q(v['lemma']) + ', form: ' + q(v['form']) + ', taxonomy: [' + ', '.join(q(x) for x in v['taxonomy']) + '] }' for v in tm['verbs'])
    lst = lambda k: '[' + ', '.join(q(x) for x in tm[k]) + ']'
    ec = f'{{ statement: {c["echo"][0]}, words: {c["echo"][2]} }}' if c['echo'] else 'none'
    rel = 'none' if c['src'] == c['id'] else f'{{ {"sameAs" if c["rel"] == "sameAs" else "like"}: {ID(c["src"])}' + (f', similarity: {c["sim"]}' if c['rel'] == 'like' else '') + ' }'
    empty = not c['text']
    spans = 'band' if c['id'] == 'l7/knowledge/1-19' else ('merged into ' + ID('l7/knowledge/1-19') if empty else 'none')
    w(f'''- id: {ID(c['id'])}
  level: l{c['level']}
  criterion: {q(NAME[c['crit']])}
  band: {{ label: {q(c['label'])}, range: "{c['band']}", axis: {c['bandpos']} }}
  span: {{ start: {c['span'][0]}, end: {c['span'][1]} }}
  versionsFrom: {rel}
  spans: {q(spans)}
  echoes: {ec}
  force: describes
  paraphrase: {q(c['prac']) if c['prac'] else 'none'}
  terms:
    verbs: [{vb}]
    objects: {lst('objects')}
    degree: {lst('degree')}
    independence: {lst('independence')}
    scope: {lst('scope')}
    deficits: {lst('deficits')}''')
w('''```

### S4a Audience versions
<!-- label: both; status: drafted; basis: primary. forPractitioner: what a marker looks for; forBeneficiary: what the student shows in that band, second person, naming no issuer. Cells with versionsFrom carry that cell's versions. -->
```yaml''')
for c in C:
    if not c['text']: continue
    w(f'''- cell: {ID(c['id'])}
  forPractitioner: {{ text: {q(c['prac'])}, rewrite: light, force: describes, status: drafted }}
  forBeneficiary: {{ text: {q(c['ben'])}, rewrite: full, force: describes, status: drafted }}''')
w('```')
LX = B.lexicon([c for c in C if c['text']])
def bandcount(e): return ' '.join(str(e['bands'].get(b, 0)) for b in AX)
w('''
### AC6 Terms
<!-- The set's lexicon: count over all cells, levels, and count per common column (fail-low, fail-high, 40-49, 50-59, 60-69, 70-79, 80-100). Taxonomy placements from INGEST's revised Bloom and SOLO documents. -->
''')
for k, title in (('verbs', 'Performance verbs (lemma)'), ('objects', 'Objects'), ('degree', 'Qualifiers of degree'), ('independence', 'Independence'), ('scope', 'Scope'), ('deficits', 'Negations and deficits')):
    w(f'#### {title}\n\n| Term | Count | Levels | By column (fail-low to 80-100) |' + (' Taxonomy |' if k == 'verbs' else '') + '\n|---|---|---|---|' + ('---|' if k == 'verbs' else ''))
    for term, e in sorted(LX[k].items(), key=lambda x: -x[1]['n']):
        if e['n'] < 2 and k == 'objects': continue
        tx = ''
        if k == 'verbs':
            p = T.get(term) or T.get(term.replace('ise', 'ize')) or []
            tx = ' ' + ('; '.join(f'{s}: {"/".join(c)}' for s, c in p) or 'none') + ' |'
        w(f'| {term} | {e["n"]} | {",".join(str(x) for x in sorted(e["levels"]))} | {bandcount(e)} |{tx}')
    w('')
POS = {b: i for i, b in enumerate(AX)}
LAD = B.ladder([c for c in C if c['text']], lambda c: POS[c['bandpos']])
w('''#### AC6.1 The set's ladders
<!-- Each degree and independence term used three or more times, placed by the mean column it appears in (0 = fail-low, 6 = 80-100). -->

| Mean column | Term | Kind | Count |
|---|---|---|---|''')
for m, term, k, n in LAD: w(f'| {m:.1f} ({AX[min(6, round(m))]}) | {term} | {k} | {n} |')
w('''
#### AC6.2 Modality
<!-- How firmly each level states its descriptors: cells opening "May demonstrate" (or containing "may") against plain statements. -->

| Level | Cells | Opening "May demonstrate" | Containing "may" |
|---|---|---|---|''')
for L in LEVELS:
    cs = [c for c in C if c['level'] == L and c['text'] and c['crit'] != 'overall']
    w(f'| {L} | {len(cs)} | {sum(1 for c in cs if c["text"].startswith("May demonstrate"))} | {sum(1 for c in cs if re.search(r"\bmay\b", c["text"], re.I))} |')
w('''
### AC7 Progressions

#### AC7.1 Across bands within a level
<!-- Degree, independence and deficit words per band, summed over the six rows. -->
''')
for L in LEVELS:
    w(f'**Level {L}**\n\n| Band | Degree | Independence | Deficits |\n|---|---|---|---|')
    for b in LAB[L]:
        r = rng(b); cs = [c for c in C if c['level'] == L and c['band'] == r and c['text']]
        fmt = lambda k: ', '.join(f'{t} {n}' for t, n in collections.Counter(x for c in cs for x in c['terms'][k]).most_common(6)) or '(none)'
        w(f'| {b} | {fmt("degree")} | {fmt("independence")} | {fmt("deficits")} |')
    w('')
w('''#### AC7.2 Across levels within a band
<!-- For each criterion, the scope and object words of the pass band (40-49 at levels 3 to 6, 50-59 at level 7) and of the 70-79 band, by level. -->

| Criterion | Band | L3 | L4 | L5 | L6 | L7 |
|---|---|---|---|---|---|---|''')
def pick(L, crit, top):
    b = '70-79' if top else ('50-59' if L == 7 else '40-49')
    m = [c for c in C if c['level'] == L and c['crit'] == crit and c['band'] == b]
    if not m or not m[0]['text']: return '(none)'
    t = m[0]['terms']; return ', '.join(dict.fromkeys(t['scope'] + t['objects'] + t['independence'])) or '(none)'
for k in NAME:
    for top in (False, True):
        w(f'| {NAME[k]} | {"70-79" if top else "pass"} | ' + ' | '.join(pick(L, k, top) for L in LEVELS) + ' |')
w(open(S + '/cmet_obs.md').read())
w('''
### AC8 Fields
```yaml''')
for k in NAME:
    f, pw = FIELDS[k]
    w(f'- {{ criterion: {q(NAME[k])}, fields: [{{ field: {q(f)}, basis: stated }}' + ''.join(f', {{ field: {p}, basis: inferred }}' for p in pw) + '] }')
w('''```

## Part B Terminology
```yaml
- { term: "Generic Band Descriptors (GBDs)", gloss: "the issuer's university-wide descriptions of attainment in each 10% band, by level", basis: paraphrase }
- { term: "band descriptor", gloss: "the issuer's preferred term over grade descriptor, since marks are percentages grouped into bands", basis: paraphrase }
- { term: "discipline-specific band descriptors", gloss: "descriptors written by programmes or schools for the context of a task, used alongside the generic ones", basis: paraphrase }
- { term: "best fit", gloss: "placing work that shows features of two neighbouring bands by professional judgement", basis: paraphrase }
- { term: "narrow fail, clear fail", gloss: "the issuer's names for the 30-39 and 1-29 bands (undergraduate) and 40-49 and 20-39 bands (level 7)", basis: paraphrase }
- { term: "simplified Grade Band Descriptors", gloss: "shorter versions for staff and students, linked from the guidance, not held", basis: paraphrase }
```

## Part C Process

### C0 Formality
`described`: the guidance sets out the descriptors' place in a cycle; the steps are its, the order ours.

### C1 Steps
```yaml
- { step: 1, name: set outcomes, does: "module descriptors state learning outcomes" }
- { step: 2, name: design, does: "curriculum and activities give students the chance to meet the outcomes at a high level" }
- { step: 3, name: set tasks and criteria, does: "programme teams set assessment tasks and devise criteria; discipline descriptors supplement the GBDs" }
- { step: 4, name: share, does: "students discuss outcomes, tasks, criteria and descriptors at the start of each year" }
- { step: 5, name: mark, does: "markers place work in a band by best fit, using the full range; zero only for no attempt or substantiated unfair practice" }
- { step: 6, name: feed back, does: "feedback names the next band's expectations and sets targets" }
```

## Part D Sources
```yaml
- key: D1
  issuer: Cardiff Metropolitan University
  title: "Academic Handbook AH1 4.3: Guidance on Assessment Marking"
  year: 2020
  url: unknown
  retrieved: "AH1_04_03.docx attached by Abbott, 2026-10-03, 04:49"
  licence: none stated
  tier: primary
  readVia: direct
  held: ''' + hashlib.sha256(raw).hexdigest() + '''
  heldFiles: [held/assessment-criteria/''' + SLUGF + '''.txt, held/assessment-criteria/''' + SLUGF + '''.norm.txt, wkspc2601-library/records/<name>.held.json]
  citedIn: [S1, S2, S3, AC1, AC2, AC3, AC4, AC5, S4a, AC6, AC7, AC8, B, C]
- { key: D2, issuer: Cardiff Metropolitan University, title: "Academic Handbook AH2 1.2B and 1.2C: programme specification templates (undergraduate, postgraduate)", retrieved: "attached by Abbott, 2026-10-03, 04:49", tier: primary, readVia: direct, use: "checked for criteria: none; each asks for a mapping of programme levels to the FHEQ descriptors", held: no }
- { key: D3, ref: std:doc:qaa-fheq-2024-framework, use: "AC2 level links; AC5 echoes" }
- { key: D4, ref: "ing:doc:bloom-anderson-krathwohl-2001; ing:doc:solo-biggs-collis-1982", use: "AC6 verb placements" }
```

### D2 Research log
```yaml
- { ref: D1, tier: primary, consulted: 2026-10-03, pass: P1, outcome: "read whole from the .docx (python-docx): key details, guidance paragraphs and tables A to E cell by cell; held and normalised with stan's tool (word sequence equal)" }
- { ref: D2, tier: primary, consulted: 2026-10-03, pass: P1, outcome: "converted with pandoc and searched: no criteria or band descriptors" }
```

### D3 Wanted sources
```yaml
- { citation: "the simplified Grade Band Descriptors for levels 3 to 7 (linked from the guidance)", settles: [AC5, S4a], asked: not yet, state: wanted }
- { citation: "the current published version of AH1 4.3, if reviewed after November 2020", settles: [S1], asked: not yet, state: wanted }
```

## Part E Gaps and questions
''' + open(S + '/cmet_parte.md').read() + '''
---

## Change notes
- 0.1.0: 2026-10-03: researched by run frame 0.1.1-draft and standards run layer 0.5.0-draft under the assessment-criteria template 0.1.0-draft, std, run 0051 (P1).''')
open(sys.argv[1], 'w', encoding='utf-8').write('\n'.join(o) + '\n')
json.dump([{k: c[k] for k in ('id', 'level', 'crit', 'band', 'bandpos', 'span', 'src', 'rel', 'echo', 'terms')} for c in C], open(S + '/cmet-cells-final.json', 'w'), indent=1)
print(len(C), 'cells')
