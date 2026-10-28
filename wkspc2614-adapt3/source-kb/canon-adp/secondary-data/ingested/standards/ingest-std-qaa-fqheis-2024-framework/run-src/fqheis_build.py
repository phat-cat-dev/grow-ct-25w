#!/usr/bin/env python3
"""Build ingest-std-qaa-fqheis-2024-framework.md (run 0047, split out by D-std-0010). std."""
import json, sys, hashlib
S = '/tmp/claude-0/-home-claude-wkspc2600-uni/378bff94-17ab-5a5d-8465-bd8449aca2a6/scratchpad'
H = '/home/claude/wkspc2600-uni/mta/claude/mta-relay/designs/ingest/standards/held/frameworks'
sk = json.load(open(f'{S}/fheq-skel.json')); ns = {}; exec(open(f'{S}/fheq_judgement.py', encoding='utf-8').read(), ns)
P, Q, DEF, THREADS = ns['P'], ns['Q'], ns['DEFINING'], ns['THREADS']
raw = open(f'{H}/qaa-frameworks-2024.txt', 'rb').read(); normb = open(f'{H}/qaa-frameworks-2024.norm.txt', 'rb').read()
q = lambda s: json.dumps(s, ensure_ascii=False)
OWN = ['4.11', '4.13', '4.14', '4.16']; SHARED = ['4.17', '4.18']; OD = OWN + SHARED
LEVEL = {'4.11': 'fqheis:7', '4.13': 'fqheis:8', '4.14': 'fqheis:9', '4.16': 'fqheis:10', '4.17': 'fqheis:11', '4.18': 'fqheis:12'}
NAME = {'4.11': '4.11 CertHE (SCQF 7)', '4.13': '4.13 DipHE (SCQF 8)', '4.14': "4.14 bachelor's non-honours (SCQF 9)", '4.16': '4.16 honours degree (SCQF 10)', '4.17': "4.17 master's (SCQF 11; shared)", '4.18': '4.18 doctorate (SCQF 12; shared)'}
items = [x for x in sk['items'] if x['descriptor'] in OWN]; byid = {x['id']: x for x in items}
ORDER = [x['id'] for x in items if not x.get('stem')]
ALL = [x for x in sk['items'] if x['descriptor'] in OD and not x.get('stem')]
LIST = {'demonstrated': ('threshold', 'threshold-outcomes', 'Outcomes demonstrated for the award (the threshold, 4.2)'), 'typical': ('will', 'wider-abilities', 'Wider abilities of typical holders (4.3)'), 'holders': ('will', 'employment-qualities', 'Qualities and transferable skills of holders (4.3)')}
ID = lambda i: f'qaa/fqheis-2024/{i}'
FH = 'std:doc:qaa-fheq-2024-framework'
THR = [(n, [(d, x) for d, x in st if d in OD]) for n, st in THREADS]
o = []; w = o.append
w(f'''---
id: std:doc:qaa-fqheis-2024-framework
title: "The Frameworks for Higher Education Qualifications of UK Degree-Awarding Bodies: the FQHEIS"
profile: standards/framework
profileVersion: 0.1.6-draft
issuer: The Quality Assurance Agency for Higher Education (QAA)
kind: qualification-framework
jurisdiction: [Scotland]
subjectScope: universal
subjects: []
edition: 2nd edition, updated February 2024
published: 2024-02-21
status: current   # as at the held text (Part E)
supersedes: "the first edition (2014)"
heldText: {{ method: sha256-bytes, raw: {hashlib.sha256(raw).hexdigest()}, normalised: {hashlib.sha256(normb).hexdigest()} }}   # the same held text as {FH}
original: {{ method: sha256-bytes, pdf: 249d3637cc31612e25748b02513f912d5e0c9712851809c3e7bd9552fbd64621, held: no }}
frameworkKind: qualification
nations: [Scotland]
levels: [fqheis:7, fqheis:8, fqheis:9, fqheis:10, fqheis:11, fqheis:12]   # SCQF numbering; 11 and 12 share the FHEQ's descriptors (S5)
awards: [CertHE, DipHE, bachelor's non-honours, bachelor's with honours, master's, doctorate]
credit: "see {FH} (Annex C, Scotland column)"
licence: none read yet
parts:
  S: "full for the FQHEIS's own descriptors; the shared descriptors and the common material are in {FH}"
  B: "see {FH}"
  C: "see {FH}"
pins: {{ structure: 0.13.0-draft, template: 0.6.1-draft, runFrame: 0.1.1-draft, runLayer: 0.5.0-draft, standards: none yet, terminology: none yet }}
lifecycle: drafted
researchedBy: run frame 0.1.1-draft; standards run layer 0.5.0-draft; std, run 0047
passes:
  P1: "2026-10-03, std (claude.ai, META Project): read with the FHEQ at 04:35; split into its own document at 05:24 (D-std-0010)"
  P2: "skipped: read direct from the issuer's PDF"
  P3: open
version: 0.1.0
---

<!-- from INGEST wpk-0016-ingest-pd-template-standards.md 0.6.1-draft under the standards/framework variant (profile 0.1.6-draft), with the level-language section SL -->
# The Frameworks for Higher Education Qualifications (QAA, 2024): the FQHEIS

> Run 0047, P1 by std. **One document per framework** (Abbott, 05:20; D-std-0010). This document holds the Framework for Qualifications of Higher Education Institutions in Scotland: its four own descriptors (4.11, 4.13, 4.14, 4.16) and its level language. QAA publishes it in one document with the FHEQ. The master's and doctoral descriptors (4.17, 4.18) are common to both frameworks and are held once in `{FH}`, as is the material common to both (sections 2 to 6, Annexes B to D, Table 1, Annex C, the Definitions); this document points to them. The issuer's words are held in UNI only (`wkspc2601-library/txt/qaa-2024-frameworks-higher-education-qualifications-uk-degree-standard.norm.txt`); every statement points into them by character span.

## Part 0 Summary

### 0.1 Agent definition
<!-- label: editorial; status: drafted; basis: primary -->
The FQHEIS: QAA's framework for higher education qualifications awarded in Scotland, SCQF Levels 7 to 12, part of the Scottish Credit and Qualifications Framework. Reach for it to say what a holder of a Scottish higher education qualification has shown at the threshold and what a typical holder can also do, level by level, including the two steps the FHEQ does not have: the DipHE and the non-honours bachelor's degree.

### 0.2 Summary
<!-- label: both; status: drafted; basis: primary -->
Six levels, numbered on the SCQF (7 to 12): CertHE (7), DipHE (8), bachelor's non-honours (9), bachelor's with honours (10), master's (11) and doctorate (12). The first four have descriptors of their own, here; master's and doctorate share the FHEQ's text. Each descriptor has the two parts the Frameworks use everywhere: outcomes demonstrated for the award (the threshold) and the abilities a typical holder will have. Below honours the Scottish descriptors are fuller than the FHEQ's: they name materials and techniques, ICT and the handling of data, and they set the context in which skills are applied (clearly defined, generally well defined, then professional). The honours descriptor asks more than the FHEQ's: the subject as a whole and its links, emerging issues at the forefront, how knowledge is developed, and "some originality and creativity".

## Part S Standard

### S1 Identity
```yaml
issuer: The Quality Assurance Agency for Higher Education
title: "The Frameworks for Higher Education Qualifications of UK Degree-Awarding Bodies (the FQHEIS within it)"
edition: 2nd edition, updated February 2024
dates: {{ published: 2024-02-21, other: ["first edition 2014"] }}
kind: qualification-framework
jurisdiction: [Scotland]
authority: reference   # degree-awarding bodies in Scotland award in accordance with it (2.2); it is part of the SCQF (2.23)
licence: none read yet
copyrightNotice: "© The Quality Assurance Agency for Higher Education 2024"
```

### S2 Purpose and scope
```yaml
governs: the levels of higher education qualifications in Scotland and the generic outcomes of the main qualification at each
appliesTo: {{ awards: [CertHE, DipHE, bachelor's non-honours, bachelor's with honours, master's, doctorate], levels: [fqheis:7, fqheis:8, fqheis:9, fqheis:10, fqheis:11, fqheis:12], providers: degree-awarding bodies in Scotland }}
whoMustUse: "degree-awarding bodies in Scotland (2.2; How the Frameworks are used); the provider rules are in {FH}"
howUsed: [positioning, designing, approving, assessing, awarding, titling, reviewing]
doesNot: "specific subjects (4.1)"
beneficiary: the student
statedScope: "generic: the full range of disciplines (4.1)"
statedSubjects: none-stated
```

### S3 Structure
```yaml
components:''')
for c in sk['descriptors']:
    if c['number'] in OWN: w(f'  - {{ number: "{c["number"]}", componentType: descriptor, heading: {q(" ".join(c["title"].split()))}, level: {LEVEL[c["number"]]} }}')
for x in items:
    if x.get('stem'): w(f'  - {{ number: "{x["id"]}", componentType: stem, parent: "{x["descriptor"]}", heading: "applying skills in professional contexts that require (three items)" }}')
for d in SHARED: w(f'  - {{ number: "{d}", componentType: shared-descriptor, heading: {q(NAME[d])}, level: {LEVEL[d]}, heldIn: "{FH}, statements qaa/fheq-2024/{d}.*" }}')
w(f'''excluded:
  - {{ number: "4.10, 4.12, 4.15", heading: "the FHEQ's own descriptors", kind: "other: {FH}" }}
  - {{ number: "1 to 3, 4.1 to 4.9, 5, 6, Annexes A to D", heading: "the material common to both frameworks", kind: "other: held once in {FH}" }}
```

### S4 Statements
<!-- label: both; status: drafted; basis: primary. {len(ORDER)} records, the FQHEIS's own descriptors. Force: `threshold` for outcomes demonstrated for the award (4.2); `will` for typical holders (4.3). -->
```yaml''')
for i in ORDER:
    r = P[i]; x = byid[i]; d = x['descriptor']; force, dim, lab = LIST[x['list']]
    stem = ID(x['parent']) if x.get('parent') else 'none'
    w(f'''- id: {ID(i)}
  locator: {{ number: "{i}", headingPath: [{q(NAME[d])}, {q(lab)}] }}
  span: {{ start: {x['span']['start']}, end: {x['span']['end']} }}
  stem: {stem}
  statementType: descriptor
  force: {force}
  level: {LEVEL[d]}
  dimension: {dim}
  award: {q(Q[d][1])}
  appliesTo: {q('the award of ' + Q[d][1])}
  addressee: {'student' if x['list'] == 'demonstrated' else 'holder'}
  verbs: [{', '.join(r['verbs'])}]
  about: {q(r['about'])}
  themes: [none]
  paraphrase: {q(r['para'])}
  quote: none
  audience: both
  subjects: inherited''')
w('```\n\n### S4a Audience versions\n<!-- label: both; status: drafted; basis: primary. The student versions name the qualification, never the framework or the issuer. -->\n```yaml')
for i in ORDER:
    r = P[i]; force = LIST[byid[i]['list']][0]
    w(f'''- statement: {ID(i)}
  forPractitioner: {{ text: {q(r['prac'])}, rewrite: light, force: {force}, status: drafted }}
  forBeneficiary: {{ text: {q(r['ben'])}, rewrite: full, force: {force}, status: drafted }}''')
w(f'''```

### S5 Levels and alignment
```yaml
levels:
  - {{ id: fqheis:7, role: defines, locator: "3.4; 4.11", typical: CertHE }}
  - {{ id: fqheis:8, role: defines, locator: "3.4; 4.13", typical: DipHE }}
  - {{ id: fqheis:9, role: defines, locator: "3.4; 4.14", typical: bachelor's non-honours degree }}
  - {{ id: fqheis:10, role: defines, locator: "3.4; 4.16", typical: bachelor's degree with honours }}
  - {{ id: fqheis:11, role: defines, locator: "3.4; 4.17", typical: master's degree, descriptor: "{FH}: qaa/fheq-2024/4.17.* (shared)" }}
  - {{ id: fqheis:12, role: defines, locator: "3.4; 4.18", typical: doctoral degree, descriptor: "{FH}: qaa/fheq-2024/4.18.* (shared)" }}
crosswalks:
  - {{ from: fqheis:11, to: fheq:7, relation: shared-descriptor, source: "4.8 and the heading of 4.17" }}
  - {{ from: fqheis:12, to: fheq:8, relation: shared-descriptor, source: "3.4; 4.8 and the heading of 4.18" }}
  - {{ from: fqheis, to: scqf, relation: part-of, source: "2.23; the levels are SCQF levels (3.4)" }}
  # Table 1's qualification-by-qualification crosswalk (FHEQ, FQHEIS, QF-EHEA cycles) and Annex C's credit are held once in {FH}, S5
```

### S6 Themes
`not-applicable-by-design`: the descriptors carry no cross-cutting themes.

### S7 Relations
```yaml
- {{ rel: siblingOf, target: "{FH}", note: "published together; holds the shared master's and doctoral descriptors and the common material" }}
- {{ rel: partOf, target: "SCQF (2.23)" }}
- {{ rel: particularisedBy, target: "QAA Subject Benchmark Statements (4.1)" }}
- {{ rel: alignsWith, target: "QF-EHEA and its Dublin descriptors (Annex B, in {FH})" }}
```

### S8 Currency and review
```yaml
published: 2024-02-21
lastReviewed: 2024-02
reviewCycle: none-stated
consultation: none-stated
replacedBy: unknown
```

### S9 Commentary (optional)
`unknown`: not researched.

### SL Level language
<!-- label: both; status: drafted; basis: primary. Our words, with the issuer's verbs and short quoted phrases. SCQF 11 and 12 are read from the shared descriptors, whose statements are in {FH}. -->

#### SL1 What defines each level

| Descriptor and level | For the practitioner | For the learner |
|---|---|---|''')
for d in OD: w(f'| {NAME[d]} | {DEF[d][0]} | {DEF[d][1]} |')
w('''
#### SL2 The level table, by part

| Descriptor and level | Threshold outcomes | Wider abilities | Qualities for employment |
|---|---|---|---|''')
for d in OD:
    cells = []
    for li in ('demonstrated', 'typical', 'holders'):
        ab = [P[x['id']]['about'] for x in ALL if x['descriptor'] == d and x['list'] == li]
        cells.append('; '.join(ab) if ab else '(none)')
    w(f'| {NAME[d]} | ' + ' | '.join(cells) + ' |')
w('''
#### SL3 Verbs by level

| Descriptor and level | Threshold outcomes | Wider abilities | Qualities for employment |
|---|---|---|---|''')
for d in OD:
    cells = []
    for li in ('demonstrated', 'typical', 'holders'):
        seen = []
        for x in ALL:
            if x['descriptor'] == d and x['list'] == li:
                for v in P[x['id']]['verbs']:
                    if v.lower() not in seen: seen.append(v.lower())
        cells.append(', '.join(seen))
    w(f'| {NAME[d]} | ' + ' | '.join(cells) + ' |')
w('''
#### SL4 How progression is communicated
<!-- Each thread follows one quality up the Scottish levels; the issuer's words in quotation marks, a few at a time. -->
''')
for name, steps in THR:
    if steps: w(f'- **{name[0].upper() + name[1:]}:** ' + '; '.join(f'{d}: {t}' for d, t in steps) + '.')
w(f'''
#### SL5 Observations on the formulation
<!-- label: editorial; status: drafted; basis: primary -->
- **Six steps, not five.** The FQHEIS puts two awards between CertHE and honours that the FHEQ does not have as levels: the DipHE (SCQF 8) and the non-honours bachelor's (SCQF 9). Its ladder is finer below honours, matching a four-year Scottish honours degree (3.3).
- **Context is graded explicitly.** Each of the four own descriptors closes with the setting in which skills are applied: limited responsibility and well-defined decisions (7), generally well defined but with some initiative (8), well defined but with decision-making (9), then professional contexts with complex and unpredictable decisions (10). It is the CQFW's way of grading, inside a qualifications framework.
- **The forefront arrives earlier.** An "awareness of major issues at the forefront" already at SCQF 8; "current developments" informing specialised study at 9; "advanced and emerging issues" at 10. The FHEQ first names the forefront at honours.
- **Knowledge is graded by breadth as well as depth.** Outline (7), scope and main areas (8), broad and comparative (9), "systematic, extensive and comparative", the subject "as a whole" (10).
- **Data handling is a strand of its own.** Gathering, basic analysis and presentation of routine data (7), critical analysis of core data (8), "well-developed skills" from current sources (9), identifying information needs and systematic gathering from evaluated sources (10), with ICT named at 7 to 9.
- **Scottish honours asks for originality.** "Some originality and creativity" (10), which the FHEQ does not ask before master's.
- **The top two levels are the FHEQ's.** At SCQF 11 and 12 the two frameworks share one text; the differences are all below master's ({FH}, SL5).

## Part B Terminology
`see {FH}`: the Definitions are common to both frameworks and held there.

## Part C Process
`see {FH}`: the provider responsibilities (section 6) are common to both frameworks and held there.

## Part D Sources
```yaml
- key: D1
  issuer: The Quality Assurance Agency for Higher Education
  title: The Frameworks for Higher Education Qualifications of UK Degree-Awarding Bodies
  edition: 2nd edition, updated February 2024
  year: 2024
  url: unknown
  retrieved: "PDF attached by Abbott, 2026-10-03, 03:47"
  licence: none read yet
  tier: primary
  readVia: direct
  held: {hashlib.sha256(raw).hexdigest()}
  heldFiles: [wkspc2601-library/txt/qaa-2024-frameworks-higher-education-qualifications-uk-degree-standard.txt, wkspc2601-library/txt/qaa-2024-frameworks-higher-education-qualifications-uk-degree-standard.norm.txt, wkspc2601-library/records/<name>.held.json]
  citedIn: [S1, S2, S3, S4, S4a, S5, S7, SL]
- {{ key: D2, ref: "{FH}", use: "the shared descriptors (4.17, 4.18) and the common material" }}
```

### D2 Research log
```yaml
- {{ ref: D1, tier: primary, consulted: 2026-10-03, pass: P1, outcome: "section 4 read whole with the FHEQ (run 0047); the FQHEIS's own descriptors taken into this document at the split (D-std-0010)" }}
```

### D3 Wanted sources
```yaml
- {{ citation: "the SCQF Partnership's level descriptors for SCQF 7 to 12, which the FQHEIS sits within", settles: [S5, SL], asked: not yet, state: wanted }}
```

## Part E Gaps and questions
- The split (D-std-0010): the shared master's and doctoral descriptors and the common material are held once, in {FH}; this document points to them. If Abbott wants the common material in a document of its own, both documents change their pointers.
- Statement ids changed at the split: `qaa/fheq-2024/4.11.*` and the like are now `qaa/fqheis-2024/4.11.*`; spans unchanged.
- 4.8, the issuer's slip on the shared descriptors' names, is recorded in {FH}, Part E.
- The SCQF level descriptors (the SCQF Partnership's own) are not held; the FQHEIS's levels are SCQF levels, so a crosswalk to them would come from that source (D3).
- ST-12: the statements and versions were checked with the FHEQ's in run 0047 (no nine-word copies).

---

## Change notes
- 0.1.0: 2026-10-03, 05:24: split out of the Frameworks 2024 document (D-std-0010, Abbott, 05:20): the FQHEIS's four descriptors (35 statements, one stem), its level records and its level language; std, run 0047 (P1).''')
open(sys.argv[1], 'w', encoding='utf-8').write('\n'.join(o) + '\n')
print('S4', len(ORDER))
