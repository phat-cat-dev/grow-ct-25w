#!/usr/bin/env python3
"""Build ingest-std-qaa-fheq-2024-framework.md (run 0047: stage 1, the qualification descriptors; stage 2, Annexes B, C, D, Table 1, Definitions, sections 2, 4, 5, 6)."""
import sys as _s; _s.path.insert(0, '/tmp/claude-0/-home-claude-wkspc2600-uni/378bff94-17ab-5a5d-8465-bd8449aca2a6/scratchpad'); import fheq2_parts as P2
import json, sys, hashlib
S = '/tmp/claude-0/-home-claude-wkspc2600-uni/378bff94-17ab-5a5d-8465-bd8449aca2a6/scratchpad'
H = '/home/claude/wkspc2600-uni/mta/claude/mta-relay/designs/ingest/standards/held/frameworks'
sk = json.load(open(f'{S}/fheq-skel.json')); ns = {}; exec(open(f'{S}/fheq_judgement.py', encoding='utf-8').read(), ns)
P, Q, DEF, THREADS, OD = ns['P'], ns['Q'], ns['DEFINING'], ns['THREADS'], ns['ORDER_D']
raw = open(f'{H}/qaa-frameworks-2024.txt', 'rb').read(); normb = open(f'{H}/qaa-frameworks-2024.norm.txt', 'rb').read(); norm = normb.decode('utf-8')
pdfh = '249d3637cc31612e25748b02513f912d5e0c9712851809c3e7bd9552fbd64621'
q = lambda s: json.dumps(s, ensure_ascii=False)
DSET = ['4.10', '4.12', '4.15', '4.17', '4.18']   # D-std-0010: the FHEQ's own descriptors; the FQHEIS's are in std:doc:qaa-fqheis-2024-framework
sk['descriptors'] = [d for d in sk['descriptors'] if d['number'] in DSET]
items = [x for x in sk['items'] if x['descriptor'] in DSET]; byid = {x['id']: x for x in items}
OD = [d for d in OD if d in DSET]; THREADS = [(n, [(d, x) for d, x in st if d in DSET]) for n, st in THREADS]
STEM = {'4.15.b3': 'conceptual understanding that enables the student to (two items)', '4.15.b9': 'qualities and skills for employment that requires (three items)', '4.16.b9': 'applying skills in professional contexts that require (three items)', '4.17.b4': 'conceptual understanding that enables the student to (two items)', '4.17.b8': 'qualities and skills for employment that requires (three items)'}
ORDER = [x['id'] for x in items if not x.get('stem')]
LIST = {'demonstrated': ('threshold', 'threshold-outcomes', 'Outcomes demonstrated for the award (the threshold, 4.2)'),
        'typical': ('will', 'wider-abilities', 'Wider abilities of typical holders (4.3)'),
        'holders': ('will', 'employment-qualities', 'Qualities and transferable skills of holders (4.3)')}
LEADQ = {'demonstrated': 'awarded to students who have demonstrated', 'typical': 'Typically, holders ... will be able to', 'holders': 'And holders will have'}
NAME = {d: f'{d} {Q[d][2]}' for d in OD}
LV = lambda d: '[' + ', '.join(Q[d][0]) + ']' if len(Q[d][0]) > 1 else Q[d][0][0]
ID = lambda i: f'qaa/fheq-2024/{i}'
o = []; w = o.append
w(f'''---
id: std:doc:qaa-fheq-2024-framework
title: "The Frameworks for Higher Education Qualifications of UK Degree-Awarding Bodies: the FHEQ, and the material common to both frameworks"
profile: standards/framework
profileVersion: 0.1.6-draft
issuer: The Quality Assurance Agency for Higher Education (QAA)
kind: qualification-framework
jurisdiction: [England, Wales, Northern Ireland]   # the common material (Annexes B to D, sections 2 to 6) also applies in Scotland
subjectScope: universal
subjects: []
edition: 2nd edition, updated February 2024
published: 2024-02-21
status: current   # as at the held text; not checked against QAA's site (Part E)
supersedes: "the first edition (2014), as the document's 'About this edition' says"
heldText: {{ method: sha256-bytes, raw: {hashlib.sha256(raw).hexdigest()}, normalised: {hashlib.sha256(normb).hexdigest()} }}
original: {{ method: sha256-bytes, pdf: {pdfh}, held: no }}   # supplied files stay out of UNI (nts N-1020)
frameworkKind: qualification
nations: [England, Wales, Northern Ireland]
levels: [fheq:4, fheq:5, fheq:6, fheq:7, fheq:8]   # equivalents stated by the document: S5; the FQHEIS levels are std:doc:qaa-fqheis-2024-framework
awards: [CertHE, foundation degree, bachelor's with honours, master's, doctorate]
credit: "illustrative: Annex C, typical minimum credit per qualification and nation (S5 credit)"
licence: none read yet (Part E)
parts:
  S: full   # Annex A (the 2014 advisory group) excluded
  B: full
  C: described
pins: {{ structure: 0.13.0-draft, template: 0.6.0-draft, runFrame: 0.1.1-draft, runLayer: 0.5.0-draft, standards: none yet, terminology: none yet }}
lifecycle: drafted
researchedBy: run frame 0.1.1-draft; standards run layer 0.5.0-draft; std, run 0047
passes:
  P1: "2026-10-03, std (claude.ai, META Project): stage 1 at 04:35, stage 2 at 04:53; split from the FQHEIS at 05:24 (D-std-0010)"
  P2: "skipped: read direct from the issuer's PDF"
  P3: open
version: 0.3.0
---

<!-- from INGEST wpk-0016-ingest-pd-template-standards.md 0.6.0-draft under the standards/framework variant (profile 0.1.6-draft; its template is to write), with the level-language section SL as in the CQFW run (std N-0057) -->
# The Frameworks for Higher Education Qualifications (QAA, 2024): the FHEQ

> Run 0047, P1 by std, in two stages: (1) the FHEQ's five qualification descriptors (4.10, 4.12, 4.15, 4.17, 4.18) and their level language; (2) Annex D (the honours classification descriptions), Annex B (the Dublin descriptors), Table 1 and Annex C (read from the page images), the Definitions, and the provider statements of sections 2, 4, 5 and 6. The issuer's words are held in UNI only (`wkspc2601-library/txt/qaa-2024-frameworks-higher-education-qualifications-uk-degree-standard.norm.txt`); every statement points into them by character span. Everything else is our words; in the level-language section, words in quotation marks are the issuer's, a few at a time. Doubts are in Part E.

> **One document per framework** (Abbott, 05:20; D-std-0010). This document holds the FHEQ (England, Wales, Northern Ireland). The FQHEIS (Scotland) is `std:doc:qaa-fqheis-2024-framework`: its four own descriptors (4.11, 4.13, 4.14, 4.16) and its level language. The master's and doctoral descriptors (4.17, 4.18) are common to both frameworks and are held here once; the FQHEIS document's SCQF 11 and 12 records point to them. The material common to both frameworks (sections 2 to 6, Annexes B to D, Table 1, the Definitions) is also held here once.

## Part 0 Summary

### 0.1 Agent definition
<!-- label: editorial; status: drafted; basis: primary -->
The FHEQ: QAA's framework for higher education qualifications in England, Wales and Northern Ireland, Levels 4 to 8, with the material QAA's Frameworks document gives both UK frameworks (award and title rules, the Dublin descriptors, the credit table and the honours classification descriptions). Reach for it to say what a holder of an FHEQ qualification has shown at the threshold, what a typical holder can also do, and how the levels compare with Scotland's and Europe's. It is generic across subjects; subject benchmarks particularise it.

### 0.2 Summary
<!-- label: both; status: drafted; basis: primary -->
Five qualification descriptors, one for the main qualification at each FHEQ level: CertHE (Level 4), foundation degree (Level 5), honours degree (Level 6), master's (Level 7) and doctorate (Level 8); the last two are shared with the FQHEIS as SCQF 11 and 12. Each has two parts (4.2, 4.3): the outcomes a student has demonstrated for the award, which the document calls the national threshold academic standard, and the wider abilities a typical holder will have, including the qualities employment asks for. The descriptors are noun phrases hung on a lead ("awarded to students who have demonstrated:"), not imperatives as in the CQFW; progression is carried by the qualifiers of knowledge (outline, detailed, systematic, at the forefront, new), of problem (routine, clearly defined, complex, incomplete data), and of independence. Around them the document sets the rules for awarding and titling qualifications (sections 2, 4, 5, 6), relates the levels to the European cycles (Table 1, the Dublin descriptors in Annex B), gives typical credit by nation (Annex C), and describes the four honours classes and failure across five strands (Annex D).

## Part S Standard

### S1 Identity
<!-- label: source; status: drafted; basis: primary -->
```yaml
issuer: The Quality Assurance Agency for Higher Education
title: The Frameworks for Higher Education Qualifications of UK Degree-Awarding Bodies
edition: 2nd edition, updated February 2024
dates:
  published: 2024-02-21
  other: ["first edition 2014 (About this edition)"]
kind: qualification-framework
jurisdiction: [England, Wales, Northern Ireland, Scotland]
authority: reference   # degree-awarding bodies use it as a reference point; England's providers also refer to the OfS sector-recognised standards (4.9)
licence: none read yet
copyrightNotice: "© The Quality Assurance Agency for Higher Education 2024"
```

### S2 Purpose and scope
<!-- label: source; status: drafted; basis: primary -->
```yaml
governs: the levels of UK higher education qualifications and the generic outcomes of the main qualification at each (section 4)
appliesTo:
  awards: [CertHE, foundation degree, bachelor's with honours, master's, doctorate]
  levels: [fheq:4, fheq:5, fheq:6, fheq:7, fheq:8]
  providers: UK degree-awarding bodies
whoMustUse: "degree-awarding bodies and their delivery partners; in Scotland, Wales and Northern Ireland the full framework, in England through the OfS sector-recognised standards (How the Frameworks are used; 2.2)"
howUsed: [positioning, designing, approving, assessing, awarding, classifying, titling, reviewing]   # 1.1, 2.4, 4.2, section 6
doesNot: "specific subjects: Subject Benchmark Statements fulfil that purpose (4.1)"
beneficiary: the student
statedScope: "generic: the descriptors cover the full range of disciplines (4.1)"
statedSubjects: none-stated
```

### S3 Structure
<!-- label: both; status: drafted; basis: primary. The issuer's structure: nine descriptors, each a heading (4.10 to 4.18), of which the FHEQ's five are here, a lead and up to three lists; list items numbered by us in order (b1, b2, ...), sub-items b<n>.<m>. Stems (list leads ending in a colon) are components, not statements; their sub-items carry them. -->
```yaml
components:''')
for c in sk['descriptors']:
    w(f'  - {{ number: "{c["number"]}", componentType: descriptor, heading: {q(" ".join(c["title"].split()))}, level: {LV(c["number"])} }}')
for x in items:
    if x.get('stem'):
        w(f'  - {{ number: "{x["id"]}", componentType: stem, parent: "{x["descriptor"]}", heading: {q(STEM[x['id']])} }}')
w(P2.s3())
w('''excluded:
  - { number: "4.11, 4.13, 4.14, 4.16", heading: "the FQHEIS's own descriptors", kind: "other: std:doc:qaa-fqheis-2024-framework (D-std-0010)" }
  - { number: "4.10 to 4.18, the paragraphs after each list", heading: "which qualifications meet the descriptor in full or in part", kind: "other: stage 2" }
  - { number: "Annex A", heading: "Advisory group (for 2014 version)", kind: "other: names, out of scope" }
  - { number: "1, 2, 3, 4.1 to 4.9, 5, 6 (descriptive paragraphs)", heading: "context and explanation", kind: "other: read for S1, S2, S5, S7, Part C; only obliging sentences are S4 records (D-std-0002 (a))" }
```

### S4 Statements
<!-- label: both; status: drafted; basis: primary. The FHEQ's descriptor records, then the common material. Force: `threshold` for the outcomes demonstrated for the award (4.2: "the national threshold academic standard"); `will` for the typical holder's wider abilities and qualities (4.3), which the issuer frames as expectations, not conditions of award. -->
```yaml''')
for i in ORDER:
    r = P[i]; x = byid[i]; d = x['descriptor']; force, dim, _ = LIST[x['list']]
    stem = ID(x['parent']) if x.get('parent') else 'none'
    w(f'''- id: {ID(i)}
  locator: {{ number: "{i}", headingPath: [{q(NAME[d])}, {q(LIST[x['list']][2])}] }}
  span: {{ start: {x['span']['start']}, end: {x['span']['end']} }}
  stem: {stem}
  statementType: descriptor
  force: {force}
  level: {LV(d)}
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
w(P2.s4())
w('```\n\n### S4a Audience versions\n<!-- label: both; status: drafted; basis: primary. The student versions name the qualification, never the framework or the issuer; force kept: "you will have shown" for the threshold, "you will usually be able to" or "you will have" for the typical holder. -->\n```yaml')
for i in ORDER:
    r = P[i]; force = LIST[byid[i]['list']][0]
    w(f'''- statement: {ID(i)}
  forPractitioner: {{ text: {q(r['prac'])}, rewrite: light, force: {force}, status: drafted }}
  forBeneficiary: {{ text: {q(r['ben'])}, rewrite: full, force: {force}, status: drafted }}''')
w(P2.s4a())
_cw, _cr = P2.s5()
w('''```

### S5 Levels and alignment
<!-- label: both; status: drafted; basis: primary. Each level a shared level record; equivalences only as the document states them (framework rule 2). -->
```yaml
levels:
  - { id: fheq:4, role: defines, locator: "3.4; 4.10", typical: CertHE }
  - { id: fheq:5, role: defines, locator: "3.4; 4.12", typical: foundation degree }
  - { id: fheq:6, role: defines, locator: "3.4; 4.15", typical: bachelor's degree with honours }
  - { id: fheq:7, role: defines, locator: "3.4; 4.17", typical: master's degree }
  - { id: fheq:8, role: defines, locator: "3.4; 4.18", typical: doctoral degree }
  - { id: "fqheis:7 to fqheis:12", role: refers, locator: "std:doc:qaa-fqheis-2024-framework (D-std-0010); fqheis:11 and fqheis:12 take this document's 4.17 and 4.18" }
  - { id: qfehea:short, role: refers, locator: "Annex B; Table 1" }
  - { id: qfehea:1, role: refers, locator: "Annex B; Table 1" }
  - { id: qfehea:2, role: refers, locator: "Annex B; Table 1" }
  - { id: qfehea:3, role: refers, locator: "Annex B; Table 1" }
crosswalks:
  - { from: fheq:7, to: fqheis:11, relation: shared-descriptor, source: "4.8 and the heading of 4.17: one descriptor common to both" }
  - { from: fheq:8, to: fqheis:12, relation: shared-descriptor, source: "3.4 (doctoral level 8, in Scotland 12); 4.8 and the heading of 4.18" }
  - { from: "cqfw:4 to cqfw:8", to: "fheq:4 to fheq:8", relation: compares-with, source: "2.24: the CQFW's Levels 4 to 8 'compare with the corresponding levels of the FHEQ'; 2.23: the FHEQ forms part of the CQFW" }
  - { from: "rqf:4 to rqf:8", to: "fheq:4 to fheq:8", relation: compares-with, source: "2.24 (the RQF is separate from the FHEQ)" }
  - { from: fqheis, to: scqf, relation: part-of, source: "2.23: the FQHEIS forms part of the SCQF; its levels are SCQF levels (3.4)" }
''')
w(_cw)
w(_cr)
w('''```

### S6 Themes
`not-applicable-by-design`: the document carries no cross-cutting themes.

### S7 Relations
```yaml
- { rel: partOf, target: "CQFW (the FHEQ is part of it, 2.23)", note: "std:doc:welsh-government-cqfw-2009-framework" }
- { rel: partOf, target: "SCQF (the FQHEIS is part of it, 2.23)" }
- { rel: particularisedBy, target: "QAA Subject Benchmark Statements (4.1)", note: "std:doc:qaa-psychology-2023-benchmarks and the 53 others (S-02)" }
- { rel: alignsWith, target: "OfS sector-recognised standards (4.9, England)" }
- { rel: alignsWith, target: "QF-EHEA and its Dublin descriptors (2.16 to 2.20, Annex B)" }
- { rel: alignsWith, target: "EQF, verified compatible (2.21, 2.22; last verified June 2019)" }
- { rel: refersTo, target: "QAA Characteristics Statements (5.4); Higher Education Credit Framework for England (2.27 to 2.29); the Quality Code (2.12)" }
```

### S8 Currency and review
```yaml
published: 2024-02-21
lastReviewed: 2024-02
reviewCycle: none-stated   # 4.7: QAA reviews the need for further or amended descriptors
consultation: none-stated   # Annex D: informed by providers' criteria and consultation with students, providers and PSRBs
replacedBy: unknown
```

### S9 Commentary (optional)
`unknown`: not researched.

### SL Level language
<!-- As in the CQFW document (Abbott, 04:03; std N-0057). label: both; status: drafted; basis: primary. Our words, with the issuer's verbs and short quoted phrases. The FHEQ's five levels; the FQHEIS's are in its own document. -->

#### SL1 What defines each level
<!-- Each level's defining step, in our words, for the practitioner and the learner. -->

| Descriptor and level | For the practitioner | For the learner |
|---|---|---|''')
for d in OD:
    w(f'| {NAME[d]} | {DEF[d][0]} | {DEF[d][1]} |')
w('''
#### SL2 The level table, by part
<!-- Each cell is our short gloss of the issuer's items at that level and part (the S4 `about` fields). The issuer's strands are its two parts, not knowledge, application and autonomy as in the CQFW. -->

| Descriptor and level | Threshold outcomes | Wider abilities | Qualities for employment |
|---|---|---|---|''')
for d in OD:
    cells = []
    for li in ('demonstrated', 'typical', 'holders'):
        ab = [P[i]['about'] for i in ORDER if byid[i]['descriptor'] == d and byid[i]['list'] == li]
        cells.append('; '.join(ab) if ab else '(none)')
    w(f'| {NAME[d]} | ' + ' | '.join(cells) + ' |')
w('''
#### SL3 Verbs by level
<!-- The issuer's own verbs, as given, by part (from the S4 `verbs` fields, first occurrence kept). Threshold outcomes are mostly noun phrases ("knowledge of", "an ability to"), so that column is thin: its progression is in the nouns and qualifiers (SL4). -->

| Descriptor and level | Threshold outcomes | Wider abilities | Qualities for employment |
|---|---|---|---|''')
for d in OD:
    cells = []
    for li in ('demonstrated', 'typical', 'holders'):
        seen = []
        for i in ORDER:
            if byid[i]['descriptor'] == d and byid[i]['list'] == li:
                for v in P[i]['verbs']:
                    if v.lower() not in seen: seen.append(v.lower())
        cells.append(', '.join(seen))
    w(f'| {NAME[d]} | ' + ' | '.join(cells) + ' |')
w('''
#### SL4 How progression is communicated
<!-- Each thread follows one quality up the levels: where the wording changes, the level is listed with the new wording (the issuer's words in quotation marks, otherwise our short reading). A level not listed adds nothing new to that thread. -->
''')
for name, steps in THREADS:
    w(f'- **{name[0].upper() + name[1:]}:** ' + '; '.join(f'{d}: {t}' for d, t in steps) + '.')
w('''
#### SL5 Observations on the formulation
<!-- label: editorial; status: drafted; basis: primary -->
- **Two parts, two forces.** Each descriptor separates what must have been shown for the award (the threshold, 4.2) from what a typical holder can also do (4.3). The CQFW has one register for all; here the threshold list is the standard and the second part is expectation. A progression model can borrow the split: what you must show, and what you will usually be able to do.
- **Nouns, not imperatives.** The threshold items are noun phrases ("knowledge of", "an understanding of", "an ability to") completing one lead. The level lives in the noun's qualifier: outline, detailed, broad and comparative, systematic, systematic and extensive, substantial; and in what is done: knowing, understanding critically, appreciating limits, creating.
- **The forefront is the spine.** From honours up, each level states how much of the student's knowledge reaches the forefront: "at least some" (honours), "much" (master's), then extending it (doctorate). It is the one quality the descriptors grade in quantity.
- **Uncertainty is graded.** The limits of one's knowledge (foundation degree), uncertainty and ambiguity (honours), current problems and new insights (master's).
- **Data become incomplete.** Routine information in a clearly defined context at the bottom; data "that may be incomplete" at honours; judgement "in the absence of complete data" at master's and doctorate.
- **Originality arrives late and in stages.** Not asked at Levels 4 to 6; originality in applying knowledge (master's), then new knowledge (doctorate).
- **The employment ladder repeats the CQFW's.** Personal responsibility (some, limited, plain), then initiative and decision-making, then complex and unpredictable contexts, then autonomy. The two frameworks share this strand almost word for word.
- **Against the FQHEIS.** The Scottish framework has six levels to the FHEQ's five, with steps the FHEQ lacks (DipHE, non-honours bachelor's) and fuller wording below honours; at master's and doctorate the two share this document's text (std:doc:qaa-fqheis-2024-framework, SL5).
- **Against the CQFW (first look; the full comparison is the second layer, std N-0058).** The CQFW grades by context (how defined the problem is) and by autonomy; the FHEQ grades by knowledge (how deep, how near the forefront, how certain) and by what the student does with research. A pathway that wants both can take its knowledge rungs from the FHEQ and its context and autonomy rungs from the CQFW.''')
w(P2.sl())
w('''
## Part B Terminology
<!-- label: both; status: drafted; basis: primary. The document's Definitions, glossed in our words. -->''')
w(P2.partB())
w('''
## Part C Process
''')
w(P2.partC())
w('''
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
  held: ''' + hashlib.sha256(raw).hexdigest() + '''
  heldFiles: [wkspc2601-library/txt/qaa-2024-frameworks-higher-education-qualifications-uk-degree-standard.txt, wkspc2601-library/txt/qaa-2024-frameworks-higher-education-qualifications-uk-degree-standard.norm.txt, wkspc2601-library/records/<name>.held.json]
  citedIn: [S1, S2, S3, S4, S4a, S5, S7, SL, B, C]
```

### D2 Research log
```yaml
- { ref: D1, tier: primary, consulted: 2026-10-03, pass: P1, outcome: "stage 1: section 4 read whole; 2.23 to 2.26, 3.1 to 3.7, 4.1 to 4.9 read for S1, S2, S5 and S7; text by pdftotext, normalised with stan's tool" }
- { ref: D1, tier: primary, consulted: 2026-10-03, pass: P1, outcome: "stage 2: the whole document read; Annex D cut by table cell from the held text, its row and column order checked against the page images (PDF pages 47, 53); Table 1 and Annex C read from the page images (PDF pages 14, 43 to 45) and checked against pdftotext layout mode; the PDF from Abbott's upload, byte hash matching index.json" }
```

### D3 Wanted sources
```yaml
- { citation: "QAA's web page for this edition: its licence and re-use terms, and whether a later edition exists", settles: [S1, S8], asked: not yet, state: wanted }
```

## Part E Gaps and questions
- Stage 2 read Table 1 and Annex C from the page images; their values are ours to check at P3 against the PDF.
- One document per framework (D-std-0010, Abbott, 05:20): the FQHEIS's four own descriptors moved to std:doc:qaa-fqheis-2024-framework with their statements, now `qaa/fqheis-2024/...`. The shared master's and doctoral descriptors and the common material stay here once, so that nothing is held twice; the FQHEIS document links to them.
- S3, the cut: the descriptors have no knowledge, application and autonomy headings; profile framework rule 3 is applied as one record per list item, the issuer's own unit. Stems (5) are components; their sub-items carry the stem's id.
- S4, force: `threshold` for the outcomes demonstrated (4.2 names them the threshold standard); `will` for the typical holder's abilities and qualities (4.3). The issuer says "Typically, holders ... will be able to", so the force is an expectation of the typical, not a condition.
- 4.8, an issuer slip: it names the shared Level 7/SCQF 11 descriptor as for "bachelor's degrees" and the shared Level 8/SCQF 12 one as for "master's degrees"; the headings of 4.17 and 4.18 show these are the master's and the doctoral descriptors. Recorded by the headings.
- S5, Table 1 and Annex C disagree in three places: foundation degrees are SCQF "NA" in Table 1 but 8 in Annex C; the Professional Graduate PGCE is SCQF 9 in Table 1 but "NA" in Annex C; graduate diplomas and certificates are SCQF 9 in both but SCQF 10 in 6.13. Recorded as each table gives them; for QAA (D3).
- S5, Annex C: the Scottish integrated master's "600c" carries note c (ECTS), probably meant for note d (a year longer); the Welsh HNC row reads "150 (30 at FHEQ Level 5 ...)" where England's reads "120 at FHEQ Level 4". Both recorded as printed.
- S5: equivalence is by qualification, not by level: FHEQ 6 sits beside SCQF 10 (honours) and SCQF 9 (other bachelor's and graduate awards); the short cycle spans FHEQ 5 and SCQF 8. The CQFW and RQF comparison (2.24) is "compare with", and 2.25 warns that the cross-UK guide gives comparisons, "rather than direct equivalences": recorded as `compares-with`, not `equals`.
- S1: the licence is not yet read (the back page gives only the copyright line); status is taken as current from the held text alone (D3).
- ST-12: versions run short and close to the issuer's formulaic wording; 13 nine-word copies were found and reworded in stage 1, 32 checker findings in stage 2 (10 copies, 22 student versions not in the second person or naming a framework), all fixed.
- Annex D, the not-successful column: no student version (24 cells); a "what is missing" version for students may be wanted (P3).
- Annex D: issuer slips kept as held: "The student has some produced creative work" (cognitive, 3rd); "problemsolving", "subjectspecific", "disciplinespecific" (PDF line breaks).
- Annex D, grid cells: the S4 paraphrase is the practitioner version (one wording, not two), the cells being short single judgements.
- Annex B: the short-cycle lead says "(within the first cycle)"; Table 1 says "within or linked to the first cycle".
- Provider statements: present-tense rules ("degree-awarding bodies ensure") carry force `must` or `should` with `forceBasis: inferred`; "must", "required", "only" are `stated`.
- Annex A (the 2014 advisory group) is excluded: names only.

---

## Change notes
- 0.3.0: 2026-10-03, 05:24: the FQHEIS split out (D-std-0010): its descriptors 4.11, 4.13, 4.14 and 4.16 (35 statements) and their level language moved to std:doc:qaa-fqheis-2024-framework; this document is the FHEQ and the material common to both.
- 0.2.0: 2026-10-03: stage 2: 181 records added (56 provider statements, 21 Dublin descriptors, 104 Annex D cells), Table 1 crosswalk and Annex C credit in S5, SL6 to SL8, Part B and Part C; std, run 0047 (P1).
- 0.1.0: 2026-10-03: stage 1 researched by run frame 0.1.1-draft and standards run layer 0.5.0-draft, std, run 0047 (P1).''')
open(sys.argv[1], 'w', encoding='utf-8').write('\n'.join(o) + '\n')
# held companion: the issuer's descriptor wording, by descriptor (UNI only)
hc = ['# The Frameworks 2024, qualification descriptors 4.10 to 4.18: the issuer\'s wording', '', '> HELD. UNI only: never in the Project, a mirror, an artifact or a store. Rendered from the held text by span; the ingestion document carries our words.', '']
for c in sk['descriptors']:
    hc.append(f'## {NAME[c["number"]]}'); hc.append(norm[c['start']:c['notesStart']].strip()); hc.append('')
open(f'{H}/qaa-frameworks-2024.levels.held.md', 'w', encoding='utf-8').write('\n'.join(hc))
print('S4', len(ORDER))
