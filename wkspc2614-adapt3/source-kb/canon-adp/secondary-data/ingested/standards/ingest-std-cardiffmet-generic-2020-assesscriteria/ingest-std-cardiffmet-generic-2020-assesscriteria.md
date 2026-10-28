---
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
heldText: { method: sha256-bytes, raw: fa71198a33ce25fed3163787a16d9a8dfa79f6dc8f25cbe328399a0ffe833613, normalised: 06d8dfae21ede6e77c00b336e5af0b7c79fc72edd6abe52d253208af11ef39cc }
originals:
  - { file: AH1_04_03.docx, method: sha256-bytes, sha256: ca39c478a6509612c24d07ad19b3785ee927638539c80c9695422dc7b90c1711, held: no }
scope: institution
levelsCovered: [cqfw:3, fheq:4, fheq:5, fheq:6, fheq:7]
assessmentKinds: any   # every type, coursework and examinations among them (key principles)
criteria: ["Overall summary", "Knowledge & Understanding", "Presentation and communication", "Analysis & discussion", "Research / scholarship", "Structured argument and critical evaluation"]   # the same six rows at every level
bands:
  l3: ["80%-100% (1st Class +)", "70%-79% (1st)", "60%-69% (2:1)", "50%-59% (2:2)", "40%-49% (3rd)", "30-39% (Narrow Fail)", "1-29% (Clear Fail)"]
  l4: ["80%-100% (1st Class +)", "70%-79% (1st)", "60%-69% (2:1)", "50%-59% (2:2)", "40%-49% (3rd)", "30-39% (Narrow Fail)", "1-29% (Clear Fail)"]
  l5: ["80%-100% (1st Class +)", "70%-79% (1st)", "60%-69% (2:1)", "50%-59% (2:2)", "40%-49% (3rd)", "30-39% (Narrow Fail)", "1-29% (Clear Fail)"]
  l6: ["80%-100% (1st Class +)", "70%-79% (1st)", "60%-69% (2:1)", "50%-59% (2:2)", "40%-49% (3rd)", "30-39% (Narrow Fail)", "1-29% (Clear Fail)"]
  l7: ["80%-100% (Distinction+)", "70%-79% (Distinction)", "60%-69% (Merit)", "50%-59% (Pass)", "40%-49% (Narrow Fail)", "20-39% (Clear Fail)", "1-19%"]
parts:
  S: full
  AC: full
  B: full
  C: described
pins: { structure: 0.13.0-draft, template: "wpk-0016-ingest-pd-template-standards-assessment-criteria.md 0.1.0-draft", runFrame: 0.1.1-draft, runLayer: 0.5.0-draft, standards: none yet, terminology: none yet }
lifecycle: drafted
researchedBy: run frame 0.1.1-draft; standards run layer 0.5.0-draft; std, run 0051
passes:
  P1: "2026-10-03, std (claude.ai, META Project)"
  P2: "skipped: read direct from the issuer's .docx"
  P3: open
version: 0.2.1
---

<!-- from INGEST wpk-0016-ingest-pd-template-standards-assessment-criteria.md 0.1.0-draft (profile 0.1.6-draft, P5a) -->
# Cardiff Metropolitan University: Generic Band Descriptors, levels 3 to 7

> Run 0051, P1 by std: the second `assessment-criteria` set, ingested for comparison with Bristol (run 0050) and to fix the template. The descriptors are tables A to E of the Academic Handbook's Guidance on Assessment Marking (AH1 4.3). The issuer's words are held in the source library repo only (`wkspc2601-library/txt/cardiff-metropolitan-university-2020-generic-band-descriptors-standard.norm.txt`); every cell points into them by character span. Everything else is our words. Of the three handbook files supplied, only AH1 4.3 holds criteria: the two programme specification templates (AH2 1.2B and 1.2C) ask only for a mapping of each level to the FHEQ descriptors.

## Part 0 Summary

### 0.1 Agent definition
<!-- label: editorial; status: drafted; basis: primary -->
Cardiff Metropolitan University's Generic Band Descriptors (GBDs): for each of levels 3 to 7, an overall summary and five criteria described in seven percentage bands, each band named by its degree classification (first class to clear fail; at level 7, distinction to fail). Reach for it to see a band scale written in prose paragraphs and tied by name to the UK classes, and to compare with Bristol's short-cell grid. It is a measuring instrument for the FHEQ levels (and a foundation level 3), not a statement of them.

### 0.2 Summary
<!-- label: both; status: drafted; basis: primary -->
The guidance sets four aims (consistent marking, confidence to use the whole 0 to 100 scale, fine distinctions at borderlines, students' understanding of what a mark needs), aligns the descriptors with the FHEQ qualification descriptors (2014 edition), applies them to every undergraduate and taught master's programme and every assessment type, and asks that they be used with discipline and assessment-specific descriptors built on the same principles. Its writing rules are explicit: plain language for staff and students; pass bands in positive terms; each band describes its own work, not what it lacks against the band above; best fit across two bands; formative use. Each level has the same six rows (overall summary; knowledge and understanding; presentation and communication; analysis and discussion; research and scholarship; structured argument and critical evaluation) in 10-mark bands named by classification. 210 cells, of which 143 carry their own versions; the rest repeat or nearly repeat an earlier level. Cells are paragraphs of several sentences, modal at levels 3 and 4 ("may demonstrate") and plain at 5 to 7 ("demonstrates").

## Part S Standard
<!-- label: both; status: drafted; basis: primary -->

### S1 Identity
```yaml
issuer: Cardiff Metropolitan University
title: "Academic Handbook AH1 4.3: Guidance on Assessment Marking (Generic Band Descriptors, tables A to E)"
edition: version 6
dates: { published: unknown, other: ["approved 2008-09-04 (Academic Board via AQSC)", "reviews: Apr 2010, Feb 2011, May 2015, Jul 2019, Nov 2020", "next review stated: 2023"] }
kind: assessment-criteria
jurisdiction: [Wales]
authority: institutional   # policy owner: Chief Student Officer, Registry Services
licence: none stated
copyrightNotice: none-stated
```

### S2 Purpose and scope
```yaml
governs: generic marking of undergraduate (levels 3 to 6) and taught master's (level 7) work, every assessment type
appliesTo: { awards: [undergraduate degrees, taught master's degrees], levels: [cqfw:3, fheq:4, fheq:5, fheq:6, fheq:7], providers: Cardiff Metropolitan University }
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
  - { number: guidance, componentType: preamble, heading: "introduction, aims, key principles, role in learning and assessment, structure, the zero rule, simplified versions" }
  - { number: l3, componentType: level, heading: "Table A: generic level 3 band descriptors", criteria: 6, bands: 7 }
  - { number: l4, componentType: level, heading: "Table B: generic level 4 band descriptors", criteria: 6, bands: 7 }
  - { number: l5, componentType: level, heading: "Table C: generic level 5 band descriptors", criteria: 6, bands: 7 }
  - { number: l6, componentType: level, heading: "Table D: generic level 6 band descriptors", criteria: 6, bands: 7 }
  - { number: l7, componentType: level, heading: "Table E: generic level 7 band descriptors", criteria: 6, bands: 7 }
excluded:
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
```yaml
- { level: l3, label: "Level 3", framework: cqfw:3, frameworkBasis: inferred, passMark: 40, table: "A" }
- { level: l4, label: "Level 4", framework: fheq:4, frameworkBasis: stated, passMark: 40, table: "B" }
- { level: l5, label: "Level 5", framework: fheq:5, frameworkBasis: stated, passMark: 40, table: "C" }
- { level: l6, label: "Level 6", framework: fheq:6, frameworkBasis: stated, passMark: 40, table: "D" }
- { level: l7, label: "Level 7", framework: fheq:7, frameworkBasis: stated, passMark: 50, table: "E" }
```
Level 3 has no FHEQ level; the issuer calls it undergraduate. It is linked to CQFW level 3 by inference (the issuer is in Wales, where the FHEQ is part of the CQFW; std:doc:qaa-fheq-2024-framework, 2.23).

### AC3 Bands
<!-- As given, in the issuer's order (highest first). `uk` is the issuer's own classification label; `axis` is our common column for comparison with other sets. -->
```yaml
l3:
  - { label: "80%-100% (1st Class +)", range: "80-100", points: none, pass: true, threshold: false, uk: "1st Class +", axis: 80-100 }
  - { label: "70%-79% (1st)", range: "70-79", points: none, pass: true, threshold: false, uk: "1st", axis: 70-79 }
  - { label: "60%-69% (2:1)", range: "60-69", points: none, pass: true, threshold: false, uk: "2:1", axis: 60-69 }
  - { label: "50%-59% (2:2)", range: "50-59", points: none, pass: true, threshold: false, uk: "2:2", axis: 50-59 }
  - { label: "40%-49% (3rd)", range: "40-49", points: none, pass: true, threshold: true, uk: "3rd", axis: 40-49 }
  - { label: "30-39% (Narrow Fail)", range: "30-39", points: none, pass: false, threshold: false, uk: "Narrow Fail", axis: fail-high }
  - { label: "1-29% (Clear Fail)", range: "1-29", points: none, pass: false, threshold: false, uk: "Clear Fail", axis: fail-low }
l4:
  - { label: "80%-100% (1st Class +)", range: "80-100", points: none, pass: true, threshold: false, uk: "1st Class +", axis: 80-100 }
  - { label: "70%-79% (1st)", range: "70-79", points: none, pass: true, threshold: false, uk: "1st", axis: 70-79 }
  - { label: "60%-69% (2:1)", range: "60-69", points: none, pass: true, threshold: false, uk: "2:1", axis: 60-69 }
  - { label: "50%-59% (2:2)", range: "50-59", points: none, pass: true, threshold: false, uk: "2:2", axis: 50-59 }
  - { label: "40%-49% (3rd)", range: "40-49", points: none, pass: true, threshold: true, uk: "3rd", axis: 40-49 }
  - { label: "30-39% (Narrow Fail)", range: "30-39", points: none, pass: false, threshold: false, uk: "Narrow Fail", axis: fail-high }
  - { label: "1-29% (Clear Fail)", range: "1-29", points: none, pass: false, threshold: false, uk: "Clear Fail", axis: fail-low }
l5:
  - { label: "80%-100% (1st Class +)", range: "80-100", points: none, pass: true, threshold: false, uk: "1st Class +", axis: 80-100 }
  - { label: "70%-79% (1st)", range: "70-79", points: none, pass: true, threshold: false, uk: "1st", axis: 70-79 }
  - { label: "60%-69% (2:1)", range: "60-69", points: none, pass: true, threshold: false, uk: "2:1", axis: 60-69 }
  - { label: "50%-59% (2:2)", range: "50-59", points: none, pass: true, threshold: false, uk: "2:2", axis: 50-59 }
  - { label: "40%-49% (3rd)", range: "40-49", points: none, pass: true, threshold: true, uk: "3rd", axis: 40-49 }
  - { label: "30-39% (Narrow Fail)", range: "30-39", points: none, pass: false, threshold: false, uk: "Narrow Fail", axis: fail-high }
  - { label: "1-29% (Clear Fail)", range: "1-29", points: none, pass: false, threshold: false, uk: "Clear Fail", axis: fail-low }
l6:
  - { label: "80%-100% (1st Class +)", range: "80-100", points: none, pass: true, threshold: false, uk: "1st Class +", axis: 80-100 }
  - { label: "70%-79% (1st)", range: "70-79", points: none, pass: true, threshold: false, uk: "1st", axis: 70-79 }
  - { label: "60%-69% (2:1)", range: "60-69", points: none, pass: true, threshold: false, uk: "2:1", axis: 60-69 }
  - { label: "50%-59% (2:2)", range: "50-59", points: none, pass: true, threshold: false, uk: "2:2", axis: 50-59 }
  - { label: "40%-49% (3rd)", range: "40-49", points: none, pass: true, threshold: true, uk: "3rd", axis: 40-49 }
  - { label: "30-39% (Narrow Fail)", range: "30-39", points: none, pass: false, threshold: false, uk: "Narrow Fail", axis: fail-high }
  - { label: "1-29% (Clear Fail)", range: "1-29", points: none, pass: false, threshold: false, uk: "Clear Fail", axis: fail-low }
l7:
  - { label: "80%-100% (Distinction+)", range: "80-100", points: none, pass: true, threshold: false, uk: "Distinction+", axis: 80-100 }
  - { label: "70%-79% (Distinction)", range: "70-79", points: none, pass: true, threshold: false, uk: "Distinction", axis: 70-79 }
  - { label: "60%-69% (Merit)", range: "60-69", points: none, pass: true, threshold: false, uk: "Merit", axis: 60-69 }
  - { label: "50%-59% (Pass)", range: "50-59", points: none, pass: true, threshold: true, uk: "Pass", axis: 50-59 }
  - { label: "40%-49% (Narrow Fail)", range: "40-49", points: none, pass: false, threshold: false, uk: "Narrow Fail", axis: 40-49 }
  - { label: "20-39% (Clear Fail)", range: "20-39", points: none, pass: false, threshold: false, uk: "Clear Fail", axis: fail-high }
  - { label: "1-19%", range: "1-19", points: none, pass: false, threshold: false, uk: "none", axis: fail-low }
```
A mark of zero sits outside the bands: it is given for no attempt or for substantiated unfair practice, and is a fail. The 80-100 band is split in the overall summary: 80-89 excellent, 90-100 outstanding and exceptional.

### AC4 Categories and criteria
The same six rows at every level, in this order, with no grouping and no cross-references: Overall summary; Knowledge & Understanding; Presentation and communication; Analysis & discussion; Research / scholarship; Structured argument and critical evaluation. At level 7 the lowest band (1-19) has one band-wide descriptor, in the Knowledge & Understanding row; the four rows below it are empty.

### AC5 Cells
<!-- One record per level, criterion and band. `sameAs`: same text as an earlier cell (level numbers masked). `like`: nearly the same text as the same criterion and band at an earlier level (word similarity 0.95 or more); versions are that cell's. `spans`: the cell stands for the whole band. `echoes`: a run of seven or more words shared with an FHEQ statement, our finding. -->
```yaml
- id: cardiffmet/generic-2020/l3/overall/80-100
  level: l3
  criterion: "Overall summary"
  band: { label: "80%-100% (1st Class +)", range: "80-100", axis: 80-100 }
  span: { start: 8020, end: 8252 }
  source: "A full and detailed understanding of the set task and an ability to have met the learning outcomes and address the assessment criteria at an excellent level (80-89%) or outstanding and exceptional level (90-100%) and beyond level 3."
  versionsFrom: none
  spans: "none"
  echoes: none
  force: describes
  paraphrase: "Full, detailed grasp of the task; outcomes met and criteria addressed excellently (80-89) or outstandingly (90-100), beyond this level."   # the whole cell, our words; sentences in AC5a
  sentences: 1
- id: cardiffmet/generic-2020/l3/overall/70-79
  level: l3
  criterion: "Overall summary"
  band: { label: "70%-79% (1st)", range: "70-79", axis: 70-79 }
  span: { start: 8291, end: 8447 }
  source: "A full and detailed understanding of the set task and an ability to have met the learning outcomes and address the assessment criteria at a very good level."
  versionsFrom: none
  spans: "none"
  echoes: none
  force: describes
  paraphrase: "Full, detailed grasp of the task; outcomes met and criteria addressed very well."   # the whole cell, our words; sentences in AC5a
  sentences: 1
- id: cardiffmet/generic-2020/l3/overall/60-69
  level: l3
  criterion: "Overall summary"
  band: { label: "60%-69% (2:1)", range: "60-69", axis: 60-69 }
  span: { start: 8486, end: 8624 }
  source: "A full understanding of the set task and an ability to have met the learning outcomes and address the assessment criteria at a good level."
  versionsFrom: none
  spans: "none"
  echoes: none
  force: describes
  paraphrase: "Full grasp of the task; outcomes met and criteria addressed well."   # the whole cell, our words; sentences in AC5a
  sentences: 1
- id: cardiffmet/generic-2020/l3/overall/50-59
  level: l3
  criterion: "Overall summary"
  band: { label: "50%-59% (2:2)", range: "50-59", axis: 50-59 }
  span: { start: 8663, end: 8822 }
  source: "A secure understanding of the set task and an ability to have met the associated learning outcomes and address the assessment criteria at a satisfactory level."
  versionsFrom: none
  spans: "none"
  echoes: none
  force: describes
  paraphrase: "Secure grasp of the task; outcomes met and criteria addressed satisfactorily."   # the whole cell, our words; sentences in AC5a
  sentences: 1
- id: cardiffmet/generic-2020/l3/overall/40-49
  level: l3
  criterion: "Overall summary"
  band: { label: "40%-49% (3rd)", range: "40-49", axis: 40-49 }
  span: { start: 8861, end: 9016 }
  source: "A basic understanding of the set task and an ability to have met the associated learning outcomes and address the assessment criteria at a threshold level."
  versionsFrom: none
  spans: "none"
  echoes: none
  force: describes
  paraphrase: "Basic grasp of the task; outcomes met and criteria addressed at the threshold."   # the whole cell, our words; sentences in AC5a
  sentences: 1
- id: cardiffmet/generic-2020/l3/overall/30-39
  level: l3
  criterion: "Overall summary"
  band: { label: "30-39% (Narrow Fail)", range: "30-39", axis: fail-high }
  span: { start: 9062, end: 9323 }
  source: "Unsatisfactory overall. A partial understanding of the set task and an ability to have met some of the associated learning outcomes at a basic level. However, attainment is uneven with some learning outcomes not met and some assessment criteria are unaddressed."
  versionsFrom: none
  spans: "none"
  echoes: none
  force: describes
  paraphrase: "Unsatisfactory: partial grasp; some outcomes met at a basic level, others not; some criteria unaddressed; uneven."   # the whole cell, our words; sentences in AC5a
  sentences: 3
- id: cardiffmet/generic-2020/l3/overall/1-29
  level: l3
  criterion: "Overall summary"
  band: { label: "1-29% (Clear Fail)", range: "1-29", axis: fail-low }
  span: { start: 9367, end: 9534 }
  source: "Poor overall. Minimal understanding of the set task. Has partially met one or two learning outcomes, or no learning outcomes. Many assessment criteria are unaddressed."
  versionsFrom: none
  spans: "none"
  echoes: none
  force: describes
  paraphrase: "Poor: minimal grasp of the task; one or two outcomes partly met, or none; many criteria unaddressed."   # the whole cell, our words; sentences in AC5a
  sentences: 4
- id: cardiffmet/generic-2020/l3/knowledge/80-100
  level: l3
  criterion: "Knowledge & Understanding"
  band: { label: "80%-100% (1st Class +)", range: "80-100", axis: 80-100 }
  span: { start: 9592, end: 9693 }
  source: "Further to the 70%-79% band, work in the 80%-100% bands would extend beyond that expected at Level 3."
  versionsFrom: none
  spans: "none"
  echoes: none
  force: describes
  paraphrase: "The top band goes further than 70-79, past what this level expects."   # the whole cell, our words; sentences in AC5a
  sentences: 1
- id: cardiffmet/generic-2020/l3/knowledge/70-79
  level: l3
  criterion: "Knowledge & Understanding"
  band: { label: "70%-79% (1st)", range: "70-79", axis: 70-79 }
  span: { start: 9742, end: 10108 }
  source: "May demonstrate a detailed knowledge of the field of study relevant to the task. There is strong evidence of an ability to apply such knowledge. The student also demonstrates an ability to engage in confident discussion of basic concepts and displays an awareness of different perspectives or approaches. Independent thinking is also a feature of work at this level."
  versionsFrom: none
  spans: "none"
  echoes: none
  force: describes
  paraphrase: "Detailed knowledge of the relevant field, applied strongly; confident discussion of basic concepts; aware of other perspectives; independent thinking."   # the whole cell, our words; sentences in AC5a
  sentences: 4
- id: cardiffmet/generic-2020/l3/knowledge/60-69
  level: l3
  criterion: "Knowledge & Understanding"
  band: { label: "60%-69% (2:1)", range: "60-69", axis: 60-69 }
  span: { start: 10157, end: 10410 }
  source: "May demonstrate a detailed knowledge of the field of study relevant to the task. There is clear evidence of an ability to apply such knowledge. The discussion of basic concepts is often tackled successfully and there is evidence of independent thinking."
  versionsFrom: none
  spans: "none"
  echoes: none
  force: describes
  paraphrase: "Detailed knowledge of the relevant field, clearly applied; basic concepts often discussed well; some independent thinking."   # the whole cell, our words; sentences in AC5a
  sentences: 3
- id: cardiffmet/generic-2020/l3/knowledge/50-59
  level: l3
  criterion: "Knowledge & Understanding"
  band: { label: "50%-59% (2:2)", range: "50-59", axis: 50-59 }
  span: { start: 10459, end: 10790 }
  source: "May demonstrate a sound knowledge of the field of study relevant to the task. Although there may be a tendency to rely on information received from elsewhere (e.g. programme materials), there is still some evidence of independent thinking. A few errors and/or misconceptions may be present, but these will not be in important areas"
  versionsFrom: none
  spans: "none"
  echoes: none
  force: describes
  paraphrase: "Sound knowledge of the field; some leaning on received material but some independent thought; a few errors, none in important areas."   # the whole cell, our words; sentences in AC5a
  sentences: 3
- id: cardiffmet/generic-2020/l3/knowledge/40-49
  level: l3
  criterion: "Knowledge & Understanding"
  band: { label: "40%-49% (3rd)", range: "40-49", axis: 40-49 }
  span: { start: 10839, end: 11171 }
  source: "May demonstrate a basic knowledge of the field of study relevant to the task. Reproducing information received from elsewhere (e.g. programme materials) is a frequent feature of work at this level. Errors and misconceptions will be evident, but these are outweighed by the degree of knowledge and understanding demonstrated overall."
  versionsFrom: none
  spans: "none"
  echoes: none
  force: describes
  paraphrase: "Basic knowledge of the field; often reproduces received material; errors and misconceptions present but outweighed by what is understood."   # the whole cell, our words; sentences in AC5a
  sentences: 3
- id: cardiffmet/generic-2020/l3/knowledge/30-39
  level: l3
  criterion: "Knowledge & Understanding"
  band: { label: "30-39% (Narrow Fail)", range: "30-39", axis: fail-high }
  span: { start: 11227, end: 11466 }
  source: "May demonstrate limited knowledge and understanding of the field of study relevant to the task. Factual inaccuracies, errors and misconceptions are evident in important areas and elements of the assessed work may be irrelevant to the task."
  versionsFrom: none
  spans: "none"
  echoes: none
  force: describes
  paraphrase: "Limited knowledge of the field; inaccuracies and misconceptions in important areas; parts of the work off the task."   # the whole cell, our words; sentences in AC5a
  sentences: 2
- id: cardiffmet/generic-2020/l3/knowledge/1-29
  level: l3
  criterion: "Knowledge & Understanding"
  band: { label: "1-29% (Clear Fail)", range: "1-29", axis: fail-low }
  span: { start: 11520, end: 11846 }
  source: "May demonstrate little knowledge and understanding of the field of study relevant to the task. Factual inaccuracies, errors and misconceptions are evident in many important areas and these outweigh the degree of knowledge and understanding demonstrated. Substantial elements of the assessed work may be irrelevant to the task."
  versionsFrom: none
  spans: "none"
  echoes: none
  force: describes
  paraphrase: "Little knowledge of the field; errors in many important areas outweigh what is understood; much of the work off the task."   # the whole cell, our words; sentences in AC5a
  sentences: 3
- id: cardiffmet/generic-2020/l3/presentation/80-100
  level: l3
  criterion: "Presentation and communication"
  band: { label: "80%-100% (1st Class +)", range: "80-100", axis: 80-100 }
  span: { start: 11909, end: 12010 }
  source: "Further to the 70%-79% band, work in the 80%-100% bands would extend beyond that expected at Level 3."
  versionsFrom: { sameAs: cardiffmet/generic-2020/l3/knowledge/80-100 }
  spans: "none"
  echoes: none
  force: describes
  paraphrase: "The top band goes further than 70-79, past what this level expects."   # the whole cell, our words; sentences in AC5a
  sentences: 1
- id: cardiffmet/generic-2020/l3/presentation/70-79
  level: l3
  criterion: "Presentation and communication"
  band: { label: "70%-79% (1st)", range: "70-79", axis: 70-79 }
  span: { start: 12064, end: 12494 }
  source: "May demonstrate an ability to present, evaluate and interpret qualitative and quantitative data, in order to develop lines of argument and make sound judgements in accordance with basic theories and concepts of their subject(s) of study. The standard of presentation is high and the format appropriate. Key points are logically organised and in written work, the style is lucid. Arguments are well-defined and clearly articulated."
  versionsFrom: none
  spans: "none"
  echoes: { statement: qaa/fheq-2024/4.10.b2, words: 35 }
  force: describes
  paraphrase: "Presents, weighs and interprets data to argue and judge soundly from basic theory; high standard of presentation; logical structure, lucid style, clear arguments."   # the whole cell, our words; sentences in AC5a
  sentences: 4
- id: cardiffmet/generic-2020/l3/presentation/60-69
  level: l3
  criterion: "Presentation and communication"
  band: { label: "60%-69% (2:1)", range: "60-69", axis: 60-69 }
  span: { start: 12548, end: 12960 }
  source: "May demonstrate an ability to present, evaluate and interpret qualitative and quantitative data, in order to develop lines of argument and make sound judgements in accordance with basic theories and concepts of their subject(s) of study. Work is well presented and the format appropriate. Key points are appropriately organised and in written work, the writing style is fluent and arguments are well articulated."
  versionsFrom: none
  spans: "none"
  echoes: { statement: qaa/fheq-2024/4.10.b2, words: 35 }
  force: describes
  paraphrase: "Presents, weighs and interprets data to argue and judge soundly; well presented and organised; fluent style, arguments well put."   # the whole cell, our words; sentences in AC5a
  sentences: 3
- id: cardiffmet/generic-2020/l3/presentation/50-59
  level: l3
  criterion: "Presentation and communication"
  band: { label: "50%-59% (2:2)", range: "50-59", axis: 50-59 }
  span: { start: 13014, end: 13441 }
  source: "May demonstrate some ability to present, evaluate and interpret qualitative and quantitative data, in order to develop lines of argument and make sound judgements in accordance with basic theories and concepts of their subject(s) of study. Overall, the structure and format of the work are appropriate. There may be occasional faults in the presentation of work but overall, these do not detract from the clarity of expression."
  versionsFrom: none
  spans: "none"
  echoes: { statement: qaa/fheq-2024/4.10.b2, words: 34 }
  force: describes
  paraphrase: "Some ability to present and interpret data for argument and judgement; structure and format appropriate; occasional faults that do not obscure meaning."   # the whole cell, our words; sentences in AC5a
  sentences: 3
- id: cardiffmet/generic-2020/l3/presentation/40-49
  level: l3
  criterion: "Presentation and communication"
  band: { label: "40%-49% (3rd)", range: "40-49", axis: 40-49 }
  span: { start: 13495, end: 14047 }
  source: "May demonstrate limited ability to present, evaluate and interpret qualitative and quantitative data, in order to develop lines of argument and make sound judgements in accordance with basic theories and concepts of their subject(s) of study. However, more success is achieved in describing and reporting factual information rather than communicating complex ideas. Generally, the work is appropriately structured although key points may not be logically sequenced. Although there will be faults in the presentation of work, the meaning is still clear."
  versionsFrom: none
  spans: "none"
  echoes: { statement: qaa/fheq-2024/4.10.b2, words: 34 }
  force: describes
  paraphrase: "Limited data handling for argument; better at reporting facts than conveying complex ideas; mostly structured, points not always in order; faults, but meaning clear."   # the whole cell, our words; sentences in AC5a
  sentences: 4
- id: cardiffmet/generic-2020/l3/presentation/30-39
  level: l3
  criterion: "Presentation and communication"
  band: { label: "30-39% (Narrow Fail)", range: "30-39", axis: fail-high }
  span: { start: 14108, end: 14409 }
  source: "May demonstrate limited ability to present, evaluate and interpret qualitative and quantitative data. Ideas may not be communicated clearly and present comprehension difficulties for the reader. If attempted, the presentation of arguments and more complex ideas may be confused and clumsily expressed."
  versionsFrom: none
  spans: "none"
  echoes: { statement: qaa/fheq-2024/4.10.b2, words: 10 }
  force: describes
  paraphrase: "Limited data handling; ideas unclear and hard for the reader to follow; arguments and complex ideas, if tried, confused."   # the whole cell, our words; sentences in AC5a
  sentences: 3
- id: cardiffmet/generic-2020/l3/presentation/1-29
  level: l3
  criterion: "Presentation and communication"
  band: { label: "1-29% (Clear Fail)", range: "1-29", axis: fail-low }
  span: { start: 14468, end: 14774 }
  source: "May demonstrate little ability to present, evaluate and interpret qualitative and quantitative data. Frequent faults in the presentation of work and significant difficulties in its structure and organisation detract from the clarity and meaning overall. The writing style is often clumsy and inappropriate."
  versionsFrom: none
  spans: "none"
  echoes: { statement: qaa/fheq-2024/4.10.b2, words: 10 }
  force: describes
  paraphrase: "Little data handling; frequent faults and weak structure obscure meaning; style often clumsy and unsuitable."   # the whole cell, our words; sentences in AC5a
  sentences: 3
- id: cardiffmet/generic-2020/l3/analysis/80-100
  level: l3
  criterion: "Analysis & discussion"
  band: { label: "80%-100% (1st Class +)", range: "80-100", axis: 80-100 }
  span: { start: 14828, end: 14929 }
  source: "Further to the 70%-79% band, work in the 80%-100% bands would extend beyond that expected at Level 3."
  versionsFrom: { sameAs: cardiffmet/generic-2020/l3/knowledge/80-100 }
  spans: "none"
  echoes: none
  force: describes
  paraphrase: "The top band goes further than 70-79, past what this level expects."   # the whole cell, our words; sentences in AC5a
  sentences: 1
- id: cardiffmet/generic-2020/l3/analysis/70-79
  level: l3
  criterion: "Analysis & discussion"
  band: { label: "70%-79% (1st)", range: "70-79", axis: 70-79 }
  span: { start: 14974, end: 15244 }
  source: "May demonstrate an ability to select and use different approaches to solving well-defined, complex and non-routine problems related to their area of study by making use of appropriate techniques. The student is highly successful in presenting and commenting on outcomes."
  versionsFrom: none
  spans: "none"
  echoes: none
  force: describes
  paraphrase: "Chooses and uses approaches, with fitting techniques, to defined but complex, non-routine problems; presents and comments on results very successfully."   # the whole cell, our words; sentences in AC5a
  sentences: 2
- id: cardiffmet/generic-2020/l3/analysis/60-69
  level: l3
  criterion: "Analysis & discussion"
  band: { label: "60%-69% (2:1)", range: "60-69", axis: 60-69 }
  span: { start: 15289, end: 15541 }
  source: "May demonstrate an ability to select and use different approaches to solving well-defined, complex and non-routine problems related to their area of study by making use of appropriate techniques and has success in presenting and commenting on outcomes."
  versionsFrom: none
  spans: "none"
  echoes: none
  force: describes
  paraphrase: "Chooses and uses approaches, with fitting techniques, to defined, complex, non-routine problems; presents and comments on results successfully."   # the whole cell, our words; sentences in AC5a
  sentences: 1
- id: cardiffmet/generic-2020/l3/analysis/50-59
  level: l3
  criterion: "Analysis & discussion"
  band: { label: "50%-59% (2:2)", range: "50-59", axis: 50-59 }
  span: { start: 15586, end: 15808 }
  source: "May demonstrate an ability to select and use different approaches to solving well-defined, complex and non-routine problems related to their area of study and generally has success in presenting and commenting on outcomes."
  versionsFrom: none
  spans: "none"
  echoes: none
  force: describes
  paraphrase: "Chooses and uses approaches to defined, complex, non-routine problems; generally succeeds in presenting and commenting on results."   # the whole cell, our words; sentences in AC5a
  sentences: 1
- id: cardiffmet/generic-2020/l3/analysis/40-49
  level: l3
  criterion: "Analysis & discussion"
  band: { label: "40%-49% (3rd)", range: "40-49", axis: 40-49 }
  span: { start: 15853, end: 16085 }
  source: "May demonstrate a limited ability to select and use different approaches to solving well-defined, complex and non-routine problems related to their area of study and has intermittent success in presenting and commenting on outcomes."
  versionsFrom: none
  spans: "none"
  echoes: none
  force: describes
  paraphrase: "Limited choice and use of approaches to complex, non-routine problems; presents and comments on results with intermittent success."   # the whole cell, our words; sentences in AC5a
  sentences: 1
- id: cardiffmet/generic-2020/l3/analysis/30-39
  level: l3
  criterion: "Analysis & discussion"
  band: { label: "30-39% (Narrow Fail)", range: "30-39", axis: fail-high }
  span: { start: 16137, end: 16357 }
  source: "May demonstrate a limited ability to select and use different approaches to solving well-defined, complex and non-routine problems related to their area of study but outcomes may be naïve, simplistic and/or unconvincing."
  versionsFrom: none
  spans: "none"
  echoes: none
  force: describes
  paraphrase: "Limited choice and use of approaches; results may be naive, simplistic or unconvincing."   # the whole cell, our words; sentences in AC5a
  sentences: 1
- id: cardiffmet/generic-2020/l3/analysis/1-29
  level: l3
  criterion: "Analysis & discussion"
  band: { label: "1-29% (Clear Fail)", range: "1-29", axis: fail-low }
  span: { start: 16407, end: 16647 }
  source: "May demonstrate little ability to select and use of different approaches to solving well-defined, complex and non-routine problems related to their area of study. Where such work has been attempted, outcomes may be inappropriate, or absent."
  versionsFrom: none
  spans: "none"
  echoes: none
  force: describes
  paraphrase: "Little choice or use of approaches; results, where attempted, unsuitable or missing."   # the whole cell, our words; sentences in AC5a
  sentences: 2
- id: cardiffmet/generic-2020/l3/research/80-100
  level: l3
  criterion: "Research / scholarship"
  band: { label: "80%-100% (1st Class +)", range: "80-100", axis: 80-100 }
  span: { start: 16702, end: 16803 }
  source: "Further to the 70%-79% band, work in the 80%-100% bands would extend beyond that expected at Level 3."
  versionsFrom: { sameAs: cardiffmet/generic-2020/l3/knowledge/80-100 }
  spans: "none"
  echoes: none
  force: describes
  paraphrase: "The top band goes further than 70-79, past what this level expects."   # the whole cell, our words; sentences in AC5a
  sentences: 1
- id: cardiffmet/generic-2020/l3/research/70-79
  level: l3
  criterion: "Research / scholarship"
  band: { label: "70%-79% (1st)", range: "70-79", axis: 70-79 }
  span: { start: 16849, end: 17375 }
  source: "May demonstrate an awareness of current research/advanced scholarship in the discipline. Use of scholarly reviews/primary sources and a breadth of individual reading and investigation, extending beyond the sources provided, is apparent. The referencing of literature and other sources is accurate and in line with academic conventions. A knowledge and understanding of research processes, techniques and methods is demonstrated along with an ability to apply research knowledge and skills successfully in appropriate contexts."
  versionsFrom: none
  spans: "none"
  echoes: none
  force: describes
  paraphrase: "Aware of current research; reading and investigation range beyond the sources given; accurate referencing; understands research processes and applies them successfully."   # the whole cell, our words; sentences in AC5a
  sentences: 4
- id: cardiffmet/generic-2020/l3/research/60-69
  level: l3
  criterion: "Research / scholarship"
  band: { label: "60%-69% (2:1)", range: "60-69", axis: 60-69 }
  span: { start: 17421, end: 17845 }
  source: "May demonstrate an awareness of current research/advanced scholarship in the discipline. Examples referred to indicate a breadth of individual reading and investigation that extend beyond the sources provided. The referencing of literature and other sources is almost always accurate. A basic knowledge of research processes is evident along with an ability to apply research skills and knowledge in the appropriate context."
  versionsFrom: none
  spans: "none"
  echoes: none
  force: describes
  paraphrase: "Aware of current research; reading beyond the sources given; referencing almost always accurate; basic grasp of research processes, applied fittingly."   # the whole cell, our words; sentences in AC5a
  sentences: 4
- id: cardiffmet/generic-2020/l3/research/50-59
  level: l3
  criterion: "Research / scholarship"
  band: { label: "50%-59% (2:2)", range: "50-59", axis: 50-59 }
  span: { start: 17891, end: 18355 }
  source: "May demonstrate some awareness of current research/advanced scholarship in the discipline. Examples of research/scholarship referred to in the work demonstrate some individual reading and investigation. Occasional errors may be present in the referencing of literature and other sources. Some knowledge of research processes is evident and the application of research skills and knowledge is generally successful, although there may be a reliance on tutor support."
  versionsFrom: none
  spans: "none"
  echoes: none
  force: describes
  paraphrase: "Some awareness of current research; some independent reading; occasional referencing errors; research skills generally applied well, perhaps relying on tutor support."   # the whole cell, our words; sentences in AC5a
  sentences: 4
- id: cardiffmet/generic-2020/l3/research/40-49
  level: l3
  criterion: "Research / scholarship"
  band: { label: "40%-49% (3rd)", range: "40-49", axis: 40-49 }
  span: { start: 18401, end: 18831 }
  source: "May demonstrate limited awareness of current research/advanced scholarship in the discipline. Examples of research/scholarship referred to in the work may indicate an over-reliance on programme materials rather than individual reading and investigation. There are errors in the referencing of literature and other sources. Some knowledge of research processes is evident, although the application of such knowledge is less secure."
  versionsFrom: none
  spans: "none"
  echoes: none
  force: describes
  paraphrase: "Limited awareness of current research; over-reliance on course materials; referencing errors; some grasp of research processes, applied less securely."   # the whole cell, our words; sentences in AC5a
  sentences: 4
- id: cardiffmet/generic-2020/l3/research/30-39
  level: l3
  criterion: "Research / scholarship"
  band: { label: "30-39% (Narrow Fail)", range: "30-39", axis: fail-high }
  span: { start: 18884, end: 19375 }
  source: "May demonstrate limited or sporadic knowledge awareness of current research/advanced scholarship in the discipline. A restricted range of sources are used but overall, there is an over-reliance on programme materials with little evidence of individual reading and investigation. There are frequent errors in the referencing of literature and other sources. Although limited knowledge of research processes may evident, nevertheless, the application of such knowledge is largely unsuccessful."
  versionsFrom: none
  spans: "none"
  echoes: none
  force: describes
  paraphrase: "Limited or patchy awareness of research; narrow sources, over-reliance on course materials; frequent referencing errors; research knowledge applied largely without success."   # the whole cell, our words; sentences in AC5a
  sentences: 4
- id: cardiffmet/generic-2020/l3/research/1-29
  level: l3
  criterion: "Research / scholarship"
  band: { label: "1-29% (Clear Fail)", range: "1-29", axis: fail-low }
  span: { start: 19426, end: 19763 }
  source: "May demonstrate little knowledge of current research/scholarship in the discipline. Evidence of individual reading and investigation is negligible and the limited referencing of literature and other sources is frequently inaccurate. Very limited knowledge of research processes is apparent and there is a failure to apply this knowledge."
  versionsFrom: none
  spans: "none"
  echoes: none
  force: describes
  paraphrase: "Little knowledge of current research; negligible own reading; referencing scant and often wrong; little grasp or use of research processes."   # the whole cell, our words; sentences in AC5a
  sentences: 3
- id: cardiffmet/generic-2020/l3/argument/80-100
  level: l3
  criterion: "Structured argument and critical evaluation"
  band: { label: "80%-100% (1st Class +)", range: "80-100", axis: 80-100 }
  span: { start: 19839, end: 19940 }
  source: "Further to the 70%-79% band, work in the 80%-100% bands would extend beyond that expected at Level 3."
  versionsFrom: { sameAs: cardiffmet/generic-2020/l3/knowledge/80-100 }
  spans: "none"
  echoes: none
  force: describes
  paraphrase: "The top band goes further than 70-79, past what this level expects."   # the whole cell, our words; sentences in AC5a
  sentences: 1
- id: cardiffmet/generic-2020/l3/argument/70-79
  level: l3
  criterion: "Structured argument and critical evaluation"
  band: { label: "70%-79% (1st)", range: "70-79", axis: 70-79 }
  span: { start: 20007, end: 20524 }
  source: "May demonstrate an ability to communicate the results of their study/work accurately and reliably with structured arguments. Arguments are well developed and substantiated and there is recognition of the complexities of academic debate. Appropriate solutions are offered to problems and the effectiveness of the methods of resolution are reviewed. There is strong evidence that the student is able to reflect effectively on the student’s own practice, with a full awareness of the implications for future development."
  versionsFrom: none
  spans: "none"
  echoes: { statement: qaa/fheq-2024/4.10.b4, words: 10 }
  force: describes
  paraphrase: "Reports results accurately in structured arguments, well developed and supported; sees the complexity of academic debate; offers fitting solutions and reviews them; reflects effectively on own practice and future development."   # the whole cell, our words; sentences in AC5a
  sentences: 4
- id: cardiffmet/generic-2020/l3/argument/60-69
  level: l3
  criterion: "Structured argument and critical evaluation"
  band: { label: "60%-69% (2:1)", range: "60-69", axis: 60-69 }
  span: { start: 20591, end: 21057 }
  source: "May demonstrate an ability to communicate the results of their study/work accurately and reliably. Arguments are clearly considered and substantiated and there is evidence of an ability to make appropriate judgements and to suggest solutions to problems. The effectiveness of the methods of resolution are reviewed. The student also demonstrates an ability to engage in reflective practice and to take account of personal evaluations planning for future development."
  versionsFrom: none
  spans: "none"
  echoes: { statement: qaa/fheq-2024/4.10.b4, words: 10 }
  force: describes
  paraphrase: "Reports results accurately; arguments considered and supported; judges fittingly and suggests solutions, reviewing how they were reached; reflects on own practice and plans development."   # the whole cell, our words; sentences in AC5a
  sentences: 4
- id: cardiffmet/generic-2020/l3/argument/50-59
  level: l3
  criterion: "Structured argument and critical evaluation"
  band: { label: "50%-59% (2:2)", range: "50-59", axis: 50-59 }
  span: { start: 21124, end: 21555 }
  source: "May demonstrate, at times, an ability to communicate the results of their study/work accurately and reliably, although there may be some over-reliance on description and factual presentation. Arguments are usually substantiated. There is some evidence of the student’s ability to evaluate and reflect on the student’s own practice, but reflections may lack insight and the implications for future development may be underestimated."
  versionsFrom: none
  spans: "none"
  echoes: { statement: qaa/fheq-2024/4.10.b4, words: 10 }
  force: describes
  paraphrase: "Reports results accurately at times, leaning on description; arguments usually supported; some evaluation of and reflection on own practice, though lacking insight into future development."   # the whole cell, our words; sentences in AC5a
  sentences: 3
- id: cardiffmet/generic-2020/l3/argument/40-49
  level: l3
  criterion: "Structured argument and critical evaluation"
  band: { label: "40%-49% (3rd)", range: "40-49", axis: 40-49 }
  span: { start: 21622, end: 22112 }
  source: "May demonstrate a limited ability to communicate the results of their study/work accurately and reliably. The balance within the work is likely to be in favour of description and factual presentation. Arguments are generally substantiated but may be under-developed. There is some evidence of the student’s ability to evaluate and reflect on the student’s own practice. although reflections may be limited and superficial with little consideration of their relevance for future development."
  versionsFrom: none
  spans: "none"
  echoes: { statement: qaa/fheq-2024/4.10.b4, words: 10 }
  force: describes
  paraphrase: "Limited accurate reporting; mostly description; arguments generally supported but thin; some reflection on own practice, limited and superficial."   # the whole cell, our words; sentences in AC5a
  sentences: 4
- id: cardiffmet/generic-2020/l3/argument/30-39
  level: l3
  criterion: "Structured argument and critical evaluation"
  band: { label: "30-39% (Narrow Fail)", range: "30-39", axis: fail-high }
  span: { start: 22186, end: 22476 }
  source: "May demonstrate limited evidence of an ability to communicate the results of their study/work accurately and reliably. The work is largely descriptive and arguments, if attempted, are rarely substantiated. Self-evaluation and reflections on the student’s own practice are extremely limited."
  versionsFrom: none
  spans: "none"
  echoes: { statement: qaa/fheq-2024/4.10.b4, words: 10 }
  force: describes
  paraphrase: "Little sign of accurate reporting; largely descriptive; arguments, if tried, rarely supported; self-evaluation very limited."   # the whole cell, our words; sentences in AC5a
  sentences: 3
- id: cardiffmet/generic-2020/l3/argument/1-29
  level: l3
  criterion: "Structured argument and critical evaluation"
  band: { label: "1-29% (Clear Fail)", range: "1-29", axis: fail-low }
  span: { start: 22548, end: 22753 }
  source: "May demonstrate little evidence of an ability to communicate the results of their study/work accurately and reliably. Self-evaluation and reflections on the student’s own practice are negligible or absent."
  versionsFrom: none
  spans: "none"
  echoes: { statement: qaa/fheq-2024/4.10.b4, words: 10 }
  force: describes
  paraphrase: "Little or no accurate reporting; self-evaluation and reflection negligible or absent."   # the whole cell, our words; sentences in AC5a
  sentences: 2
- id: cardiffmet/generic-2020/l4/overall/80-100
  level: l4
  criterion: "Overall summary"
  band: { label: "80%-100% (1st Class +)", range: "80-100", axis: 80-100 }
  span: { start: 22835, end: 23067 }
  source: "A full and detailed understanding of the set task and an ability to have met the learning outcomes and address the assessment criteria at an excellent level (80-89%) or outstanding and exceptional level (90-100%) and beyond level 4."
  versionsFrom: { sameAs: cardiffmet/generic-2020/l3/overall/80-100 }
  spans: "none"
  echoes: none
  force: describes
  paraphrase: "Full, detailed grasp of the task; outcomes met and criteria addressed excellently (80-89) or outstandingly (90-100), beyond this level."   # the whole cell, our words; sentences in AC5a
  sentences: 1
- id: cardiffmet/generic-2020/l4/overall/70-79
  level: l4
  criterion: "Overall summary"
  band: { label: "70%-79% (1st)", range: "70-79", axis: 70-79 }
  span: { start: 23106, end: 23262 }
  source: "A full and detailed understanding of the set task and an ability to have met the learning outcomes and address the assessment criteria at a very good level."
  versionsFrom: { sameAs: cardiffmet/generic-2020/l3/overall/70-79 }
  spans: "none"
  echoes: none
  force: describes
  paraphrase: "Full, detailed grasp of the task; outcomes met and criteria addressed very well."   # the whole cell, our words; sentences in AC5a
  sentences: 1
- id: cardiffmet/generic-2020/l4/overall/60-69
  level: l4
  criterion: "Overall summary"
  band: { label: "60%-69% (2:1)", range: "60-69", axis: 60-69 }
  span: { start: 23301, end: 23439 }
  source: "A full understanding of the set task and an ability to have met the learning outcomes and address the assessment criteria at a good level."
  versionsFrom: { sameAs: cardiffmet/generic-2020/l3/overall/60-69 }
  spans: "none"
  echoes: none
  force: describes
  paraphrase: "Full grasp of the task; outcomes met and criteria addressed well."   # the whole cell, our words; sentences in AC5a
  sentences: 1
- id: cardiffmet/generic-2020/l4/overall/50-59
  level: l4
  criterion: "Overall summary"
  band: { label: "50%-59% (2:2)", range: "50-59", axis: 50-59 }
  span: { start: 23478, end: 23637 }
  source: "A secure understanding of the set task and an ability to have met the associated learning outcomes and address the assessment criteria at a satisfactory level."
  versionsFrom: { sameAs: cardiffmet/generic-2020/l3/overall/50-59 }
  spans: "none"
  echoes: none
  force: describes
  paraphrase: "Secure grasp of the task; outcomes met and criteria addressed satisfactorily."   # the whole cell, our words; sentences in AC5a
  sentences: 1
- id: cardiffmet/generic-2020/l4/overall/40-49
  level: l4
  criterion: "Overall summary"
  band: { label: "40%-49% (3rd)", range: "40-49", axis: 40-49 }
  span: { start: 23676, end: 23831 }
  source: "A basic understanding of the set task and an ability to have met the associated learning outcomes and address the assessment criteria at a threshold level."
  versionsFrom: { sameAs: cardiffmet/generic-2020/l3/overall/40-49 }
  spans: "none"
  echoes: none
  force: describes
  paraphrase: "Basic grasp of the task; outcomes met and criteria addressed at the threshold."   # the whole cell, our words; sentences in AC5a
  sentences: 1
- id: cardiffmet/generic-2020/l4/overall/30-39
  level: l4
  criterion: "Overall summary"
  band: { label: "30-39% (Narrow Fail)", range: "30-39", axis: fail-high }
  span: { start: 23877, end: 24134 }
  source: "Unsatisfactory overall. A partial understanding of the set task and an ability to have met some of the associated learning outcomes at a basic level. However, attainment is uneven with some learning outcomes not met and some assessment criteria unaddressed."
  versionsFrom: { like: cardiffmet/generic-2020/l3/overall/30-39, similarity: 0.99 }
  spans: "none"
  echoes: none
  force: describes
  paraphrase: "Unsatisfactory: partial grasp; some outcomes met at a basic level, others not; some criteria unaddressed; uneven."   # the whole cell, our words; sentences in AC5a
  sentences: 3
- id: cardiffmet/generic-2020/l4/overall/1-29
  level: l4
  criterion: "Overall summary"
  band: { label: "1-29% (Clear Fail)", range: "1-29", axis: fail-low }
  span: { start: 24178, end: 24337 }
  source: "Poor overall. Minimal understanding of the set task and will partially have met one or two learning outcomes or none. Many assessment criteria are unaddressed."
  versionsFrom: none
  spans: "none"
  echoes: none
  force: describes
  paraphrase: "Poor: minimal grasp of the task; one or two outcomes partly met, or none; many criteria unaddressed."   # the whole cell, our words; sentences in AC5a
  sentences: 3
- id: cardiffmet/generic-2020/l4/knowledge/80-100
  level: l4
  criterion: "Knowledge & Understanding"
  band: { label: "80%-100% (1st Class +)", range: "80-100", axis: 80-100 }
  span: { start: 24395, end: 24496 }
  source: "Further to the 70%-79% band, work in the 80%-100% bands would extend beyond that expected at Level 4."
  versionsFrom: { sameAs: cardiffmet/generic-2020/l3/knowledge/80-100 }
  spans: "none"
  echoes: none
  force: describes
  paraphrase: "The top band goes further than 70-79, past what this level expects."   # the whole cell, our words; sentences in AC5a
  sentences: 1
- id: cardiffmet/generic-2020/l4/knowledge/70-79
  level: l4
  criterion: "Knowledge & Understanding"
  band: { label: "70%-79% (1st)", range: "70-79", axis: 70-79 }
  span: { start: 24545, end: 24972 }
  source: "May demonstrate a detailed knowledge of the underlying aspects of the field of study relevant to the task. There is strong evidence of an ability to apply such knowledge. The student also demonstrates an ability to engage in confident discussion of basic concepts and an awareness of the limitations and/or ambiguity of disciplinary knowledge. Independent thinking and original insights are also features of work at this level."
  versionsFrom: none
  spans: "none"
  echoes: none
  force: describes
  paraphrase: "Detailed knowledge of the field's underlying aspects, applied strongly; confident discussion of basic concepts; aware of the limits and ambiguity of knowledge; independent, original insight."   # the whole cell, our words; sentences in AC5a
  sentences: 4
- id: cardiffmet/generic-2020/l4/knowledge/60-69
  level: l4
  criterion: "Knowledge & Understanding"
  band: { label: "60%-69% (2:1)", range: "60-69", axis: 60-69 }
  span: { start: 25021, end: 25350 }
  source: "May demonstrate a detailed knowledge of the underlying aspects of the field of study relevant to the task. There is clear evidence of an ability to apply such knowledge and, in some contexts, to extend and transform it. The discussion of basic concepts is often tackled successfully and there is evidence of independent thinking."
  versionsFrom: none
  spans: "none"
  echoes: none
  force: describes
  paraphrase: "Detailed knowledge of the field's underlying aspects, clearly applied and sometimes extended or transformed; basic concepts often discussed well; independent thinking."   # the whole cell, our words; sentences in AC5a
  sentences: 3
- id: cardiffmet/generic-2020/l4/knowledge/50-59
  level: l4
  criterion: "Knowledge & Understanding"
  band: { label: "50%-59% (2:2)", range: "50-59", axis: 50-59 }
  span: { start: 25399, end: 25756 }
  source: "May demonstrate a sound knowledge of the underlying aspects of the field of study relevant to the task. Although there may be a tendency to rely on information received from elsewhere (e.g. programme materials), there is still some evidence of independent thinking. A few errors and/or misconceptions may be present, but these will not be in important areas"
  versionsFrom: { like: cardiffmet/generic-2020/l3/knowledge/50-59, similarity: 0.97 }
  spans: "none"
  echoes: none
  force: describes
  paraphrase: "Sound knowledge of the field; some leaning on received material but some independent thought; a few errors, none in important areas."   # the whole cell, our words; sentences in AC5a
  sentences: 3
- id: cardiffmet/generic-2020/l4/knowledge/40-49
  level: l4
  criterion: "Knowledge & Understanding"
  band: { label: "40%-49% (3rd)", range: "40-49", axis: 40-49 }
  span: { start: 25805, end: 26163 }
  source: "May demonstrate a basic knowledge of the underlying aspects of the field of study relevant to the task. Reproducing information received from elsewhere (e.g. programme materials) is a frequent feature of work at this level. Errors and misconceptions will be evident, but these are outweighed by the degree of knowledge and understanding demonstrated overall."
  versionsFrom: { like: cardiffmet/generic-2020/l3/knowledge/40-49, similarity: 0.96 }
  spans: "none"
  echoes: none
  force: describes
  paraphrase: "Basic knowledge of the field; often reproduces received material; errors and misconceptions present but outweighed by what is understood."   # the whole cell, our words; sentences in AC5a
  sentences: 3
- id: cardiffmet/generic-2020/l4/knowledge/30-39
  level: l4
  criterion: "Knowledge & Understanding"
  band: { label: "30-39% (Narrow Fail)", range: "30-39", axis: fail-high }
  span: { start: 26219, end: 26484 }
  source: "May demonstrate limited knowledge and understanding of the underlying aspects of the field of study relevant to the task. Factual inaccuracies, errors and misconceptions are evident in important areas and elements of the assessed work may be irrelevant to the task."
  versionsFrom: none
  spans: "none"
  echoes: none
  force: describes
  paraphrase: "Limited knowledge of the field's underlying aspects; inaccuracies in important areas; parts of the work off the task."   # the whole cell, our words; sentences in AC5a
  sentences: 2
- id: cardiffmet/generic-2020/l4/knowledge/1-29
  level: l4
  criterion: "Knowledge & Understanding"
  band: { label: "1-29% (Clear Fail)", range: "1-29", axis: fail-low }
  span: { start: 26538, end: 26890 }
  source: "May demonstrate little knowledge and understanding of the underlying aspects of the field of study relevant to the task. Factual inaccuracies, errors and misconceptions are evident in many important areas and these outweigh the degree of knowledge and understanding demonstrated. Substantial elements of the assessed work may be irrelevant to the task."
  versionsFrom: { like: cardiffmet/generic-2020/l3/knowledge/1-29, similarity: 0.96 }
  spans: "none"
  echoes: none
  force: describes
  paraphrase: "Little knowledge of the field; errors in many important areas outweigh what is understood; much of the work off the task."   # the whole cell, our words; sentences in AC5a
  sentences: 3
- id: cardiffmet/generic-2020/l4/presentation/80-100
  level: l4
  criterion: "Presentation and communication"
  band: { label: "80%-100% (1st Class +)", range: "80-100", axis: 80-100 }
  span: { start: 26953, end: 27054 }
  source: "Further to the 70%-79% band, work in the 80%-100% bands would extend beyond that expected at Level 4."
  versionsFrom: { sameAs: cardiffmet/generic-2020/l3/knowledge/80-100 }
  spans: "none"
  echoes: none
  force: describes
  paraphrase: "The top band goes further than 70-79, past what this level expects."   # the whole cell, our words; sentences in AC5a
  sentences: 1
- id: cardiffmet/generic-2020/l4/presentation/70-79
  level: l4
  criterion: "Presentation and communication"
  band: { label: "70%-79% (1st)", range: "70-79", axis: 70-79 }
  span: { start: 27108, end: 27563 }
  source: "May demonstrate an ability to present, evaluate and interpret qualitative and quantitative data, in order to develop lines of argument and make sound judgements in accordance with basic theories and concepts of their subject(s) of study. The standard of presentation is high and the format appropriate. Key points are logically organised and in written work, the style is lucid. Arguments are well-defined and clearly articulated, structured and coherent."
  versionsFrom: { like: cardiffmet/generic-2020/l3/presentation/70-79, similarity: 0.98 }
  spans: "none"
  echoes: { statement: qaa/fheq-2024/4.10.b2, words: 35 }
  force: describes
  paraphrase: "Presents, weighs and interprets data to argue and judge soundly from basic theory; high standard of presentation; logical structure, lucid style, clear arguments."   # the whole cell, our words; sentences in AC5a
  sentences: 4
- id: cardiffmet/generic-2020/l4/presentation/60-69
  level: l4
  criterion: "Presentation and communication"
  band: { label: "60%-69% (2:1)", range: "60-69", axis: 60-69 }
  span: { start: 27617, end: 28054 }
  source: "May demonstrate an ability to present, evaluate and interpret qualitative and quantitative data, in order to develop lines of argument and make sound judgements in accordance with basic theories and concepts of their subject(s) of study. Work is well presented and the format appropriate. Key points are appropriately organised and in written work, the writing style is fluent and arguments are well articulated, structured and coherent."
  versionsFrom: { like: cardiffmet/generic-2020/l3/presentation/60-69, similarity: 0.98 }
  spans: "none"
  echoes: { statement: qaa/fheq-2024/4.10.b2, words: 35 }
  force: describes
  paraphrase: "Presents, weighs and interprets data to argue and judge soundly; well presented and organised; fluent style, arguments well put."   # the whole cell, our words; sentences in AC5a
  sentences: 3
- id: cardiffmet/generic-2020/l4/presentation/50-59
  level: l4
  criterion: "Presentation and communication"
  band: { label: "50%-59% (2:2)", range: "50-59", axis: 50-59 }
  span: { start: 28108, end: 28535 }
  source: "May demonstrate some ability to present, evaluate and interpret qualitative and quantitative data, in order to develop lines of argument and make sound judgements in accordance with basic theories and concepts of their subject(s) of study. Overall, the structure and format of the work are appropriate. There may be occasional faults in the presentation of work but overall, these do not detract from the clarity of expression."
  versionsFrom: { sameAs: cardiffmet/generic-2020/l3/presentation/50-59 }
  spans: "none"
  echoes: { statement: qaa/fheq-2024/4.10.b2, words: 34 }
  force: describes
  paraphrase: "Some ability to present and interpret data for argument and judgement; structure and format appropriate; occasional faults that do not obscure meaning."   # the whole cell, our words; sentences in AC5a
  sentences: 3
- id: cardiffmet/generic-2020/l4/presentation/40-49
  level: l4
  criterion: "Presentation and communication"
  band: { label: "40%-49% (3rd)", range: "40-49", axis: 40-49 }
  span: { start: 28589, end: 29141 }
  source: "May demonstrate limited ability to present, evaluate and interpret qualitative and quantitative data, in order to develop lines of argument and make sound judgements in accordance with basic theories and concepts of their subject(s) of study. However, more success is achieved in describing and reporting factual information rather than communicating complex ideas. Generally, the work is appropriately structured although key points may not be logically sequenced. Although there will be faults in the presentation of work, the meaning is still clear."
  versionsFrom: { sameAs: cardiffmet/generic-2020/l3/presentation/40-49 }
  spans: "none"
  echoes: { statement: qaa/fheq-2024/4.10.b2, words: 34 }
  force: describes
  paraphrase: "Limited data handling for argument; better at reporting facts than conveying complex ideas; mostly structured, points not always in order; faults, but meaning clear."   # the whole cell, our words; sentences in AC5a
  sentences: 4
- id: cardiffmet/generic-2020/l4/presentation/30-39
  level: l4
  criterion: "Presentation and communication"
  band: { label: "30-39% (Narrow Fail)", range: "30-39", axis: fail-high }
  span: { start: 29202, end: 29503 }
  source: "May demonstrate limited ability to present, evaluate and interpret qualitative and quantitative data. Ideas may not be communicated clearly and present comprehension difficulties for the reader. If attempted, the presentation of arguments and more complex ideas may be confused and clumsily expressed."
  versionsFrom: { sameAs: cardiffmet/generic-2020/l3/presentation/30-39 }
  spans: "none"
  echoes: { statement: qaa/fheq-2024/4.10.b2, words: 10 }
  force: describes
  paraphrase: "Limited data handling; ideas unclear and hard for the reader to follow; arguments and complex ideas, if tried, confused."   # the whole cell, our words; sentences in AC5a
  sentences: 3
- id: cardiffmet/generic-2020/l4/presentation/1-29
  level: l4
  criterion: "Presentation and communication"
  band: { label: "1-29% (Clear Fail)", range: "1-29", axis: fail-low }
  span: { start: 29562, end: 29868 }
  source: "May demonstrate little ability to present, evaluate and interpret qualitative and quantitative data. Frequent faults in the presentation of work and significant difficulties in its structure and organisation detract from the clarity and meaning overall. The writing style is often clumsy and inappropriate."
  versionsFrom: { sameAs: cardiffmet/generic-2020/l3/presentation/1-29 }
  spans: "none"
  echoes: { statement: qaa/fheq-2024/4.10.b2, words: 10 }
  force: describes
  paraphrase: "Little data handling; frequent faults and weak structure obscure meaning; style often clumsy and unsuitable."   # the whole cell, our words; sentences in AC5a
  sentences: 3
- id: cardiffmet/generic-2020/l4/analysis/80-100
  level: l4
  criterion: "Analysis & discussion"
  band: { label: "80%-100% (1st Class +)", range: "80-100", axis: 80-100 }
  span: { start: 29922, end: 30023 }
  source: "Further to the 70%-79% band, work in the 80%-100% bands would extend beyond that expected at Level 4."
  versionsFrom: { sameAs: cardiffmet/generic-2020/l3/knowledge/80-100 }
  spans: "none"
  echoes: none
  force: describes
  paraphrase: "The top band goes further than 70-79, past what this level expects."   # the whole cell, our words; sentences in AC5a
  sentences: 1
- id: cardiffmet/generic-2020/l4/analysis/70-79
  level: l4
  criterion: "Analysis & discussion"
  band: { label: "70%-79% (1st)", range: "70-79", axis: 70-79 }
  span: { start: 30068, end: 30421 }
  source: "May demonstrate an ability to evaluate the appropriateness of different approaches to solving well-defined, complex and non-routine problems related to their area of study. The student is highly successful in presenting and commenting on outcomes and is able to comment perceptively and with some insight on the relationship between theory and practice."
  versionsFrom: none
  spans: "none"
  echoes: { statement: qaa/fheq-2024/4.10.b3, words: 8 }
  force: describes
  paraphrase: "Evaluates how well different approaches suit complex, non-routine problems; presents and comments on results very successfully, with perceptive insight on theory and practice."   # the whole cell, our words; sentences in AC5a
  sentences: 2
- id: cardiffmet/generic-2020/l4/analysis/60-69
  level: l4
  criterion: "Analysis & discussion"
  band: { label: "60%-69% (2:1)", range: "60-69", axis: 60-69 }
  span: { start: 30466, end: 30799 }
  source: "May demonstrate an ability to evaluate the appropriateness of different approaches to solving well-defined, complex and non-routine problems related to their area of study by making use of appropriate techniques and has considerable success in presenting and commenting on outcomes. There is some linkage between theory and practice."
  versionsFrom: none
  spans: "none"
  echoes: { statement: qaa/fheq-2024/4.10.b3, words: 8 }
  force: describes
  paraphrase: "Evaluates how well approaches suit complex, non-routine problems, with fitting techniques; considerable success with results; some link of theory and practice."   # the whole cell, our words; sentences in AC5a
  sentences: 2
- id: cardiffmet/generic-2020/l4/analysis/50-59
  level: l4
  criterion: "Analysis & discussion"
  band: { label: "50%-59% (2:2)", range: "50-59", axis: 50-59 }
  span: { start: 30844, end: 31083 }
  source: "May demonstrate an ability to evaluate the appropriateness of different approaches to solving well-defined, complex and non-routine problems related to their area of study and generally has success in presenting and commenting on outcomes."
  versionsFrom: none
  spans: "none"
  echoes: { statement: qaa/fheq-2024/4.10.b3, words: 8 }
  force: describes
  paraphrase: "Evaluates how well approaches suit complex, non-routine problems; generally succeeds in presenting and commenting on results."   # the whole cell, our words; sentences in AC5a
  sentences: 1
- id: cardiffmet/generic-2020/l4/analysis/40-49
  level: l4
  criterion: "Analysis & discussion"
  band: { label: "40%-49% (3rd)", range: "40-49", axis: 40-49 }
  span: { start: 31128, end: 31377 }
  source: "May demonstrate a limited ability to evaluate the appropriateness of different approaches to solving well-defined, complex and non-routine problems related to their area of study and has intermittent success in presenting and commenting on outcomes."
  versionsFrom: none
  spans: "none"
  echoes: { statement: qaa/fheq-2024/4.10.b3, words: 8 }
  force: describes
  paraphrase: "Limited evaluation of approaches to complex, non-routine problems; intermittent success with results."   # the whole cell, our words; sentences in AC5a
  sentences: 1
- id: cardiffmet/generic-2020/l4/analysis/30-39
  level: l4
  criterion: "Analysis & discussion"
  band: { label: "30-39% (Narrow Fail)", range: "30-39", axis: fail-high }
  span: { start: 31429, end: 31666 }
  source: "May demonstrate a limited ability to evaluate the appropriateness of different approaches to solving well-defined, complex and non-routine problems related to their area of study but outcomes may be naïve, simplistic and/or unconvincing."
  versionsFrom: none
  spans: "none"
  echoes: { statement: qaa/fheq-2024/4.10.b3, words: 8 }
  force: describes
  paraphrase: "Limited evaluation of approaches; results may be naive, simplistic or unconvincing."   # the whole cell, our words; sentences in AC5a
  sentences: 1
- id: cardiffmet/generic-2020/l4/analysis/1-29
  level: l4
  criterion: "Analysis & discussion"
  band: { label: "1-29% (Clear Fail)", range: "1-29", axis: fail-low }
  span: { start: 31716, end: 31970 }
  source: "May demonstrate little ability to evaluate the appropriateness of different approaches to solving well-defined, complex and non-routine problems related to their area of study. Where such work has been attempted, outcomes may be inappropriate, or absent."
  versionsFrom: none
  spans: "none"
  echoes: { statement: qaa/fheq-2024/4.10.b3, words: 8 }
  force: describes
  paraphrase: "Little evaluation of approaches to problems; results, where attempted, unsuitable or missing."   # the whole cell, our words; sentences in AC5a
  sentences: 2
- id: cardiffmet/generic-2020/l4/research/80-100
  level: l4
  criterion: "Research / scholarship"
  band: { label: "80%-100% (1st Class +)", range: "80-100", axis: 80-100 }
  span: { start: 32025, end: 32126 }
  source: "Further to the 70%-79% band, work in the 80%-100% bands would extend beyond that expected at Level 4."
  versionsFrom: { sameAs: cardiffmet/generic-2020/l3/knowledge/80-100 }
  spans: "none"
  echoes: none
  force: describes
  paraphrase: "The top band goes further than 70-79, past what this level expects."   # the whole cell, our words; sentences in AC5a
  sentences: 1
- id: cardiffmet/generic-2020/l4/research/70-79
  level: l4
  criterion: "Research / scholarship"
  band: { label: "70%-79% (1st)", range: "70-79", axis: 70-79 }
  span: { start: 32172, end: 32725 }
  source: "May demonstrate an awareness of current research/advanced scholarship in the discipline. The use of scholarly reviews/primary sources is confident and a breadth and depth of individual reading and investigation, extending beyond the sources provided, is apparent. The referencing of literature and other sources is accurate and in line with academic conventions. A knowledge and understanding of research processes, techniques and methods is demonstrated along with an ability to apply research knowledge and skills successfully in appropriate contexts."
  versionsFrom: { like: cardiffmet/generic-2020/l3/research/70-79, similarity: 0.97 }
  spans: "none"
  echoes: none
  force: describes
  paraphrase: "Aware of current research; reading and investigation range beyond the sources given; accurate referencing; understands research processes and applies them successfully."   # the whole cell, our words; sentences in AC5a
  sentences: 4
- id: cardiffmet/generic-2020/l4/research/60-69
  level: l4
  criterion: "Research / scholarship"
  band: { label: "60%-69% (2:1)", range: "60-69", axis: 60-69 }
  span: { start: 32771, end: 33207 }
  source: "May demonstrate an awareness of current research/advanced scholarship in the discipline. Examples referred to indicate a breadth and depth of individual reading and investigation that extend beyond the sources provided. The referencing of literature and other sources is almost always accurate. A secure knowledge of research processes is evident, along with an ability to apply research skills and knowledge in the appropriate context."
  versionsFrom: { like: cardiffmet/generic-2020/l3/research/60-69, similarity: 0.97 }
  spans: "none"
  echoes: none
  force: describes
  paraphrase: "Aware of current research; reading beyond the sources given; referencing almost always accurate; basic grasp of research processes, applied fittingly."   # the whole cell, our words; sentences in AC5a
  sentences: 4
- id: cardiffmet/generic-2020/l4/research/50-59
  level: l4
  criterion: "Research / scholarship"
  band: { label: "50%-59% (2:2)", range: "50-59", axis: 50-59 }
  span: { start: 33253, end: 33711 }
  source: "May demonstrate some awareness of current research/advanced scholarship in the discipline. Examples of research/scholarship referred to in the work demonstrate individual reading and investigation. Occasional errors may be present in the referencing of literature and other sources. Some knowledge of research processes is evident and the application of research skills and knowledge is generally successful, although there may be a reliance on tutor support"
  versionsFrom: { like: cardiffmet/generic-2020/l3/research/50-59, similarity: 0.99 }
  spans: "none"
  echoes: none
  force: describes
  paraphrase: "Some awareness of current research; some independent reading; occasional referencing errors; research skills generally applied well, perhaps relying on tutor support."   # the whole cell, our words; sentences in AC5a
  sentences: 4
- id: cardiffmet/generic-2020/l4/research/40-49
  level: l4
  criterion: "Research / scholarship"
  band: { label: "40%-49% (3rd)", range: "40-49", axis: 40-49 }
  span: { start: 33757, end: 34186 }
  source: "May demonstrate limited awareness of current research/advanced scholarship in the discipline. Examples of research/scholarship referred to in the work may indicate an over-reliance on programme materials rather than individual reading and investigation. There are errors in the referencing of literature and other sources. Some knowledge of research processes is evident although the application of such knowledge is less secure."
  versionsFrom: { sameAs: cardiffmet/generic-2020/l3/research/40-49 }
  spans: "none"
  echoes: none
  force: describes
  paraphrase: "Limited awareness of current research; over-reliance on course materials; referencing errors; some grasp of research processes, applied less securely."   # the whole cell, our words; sentences in AC5a
  sentences: 4
- id: cardiffmet/generic-2020/l4/research/30-39
  level: l4
  criterion: "Research / scholarship"
  band: { label: "30-39% (Narrow Fail)", range: "30-39", axis: fail-high }
  span: { start: 34239, end: 34733 }
  source: "May demonstrate limited or sporadic knowledge awareness of current research/advanced scholarship in the discipline. A restricted range of sources are used but overall, there is an over-reliance on programme materials with little evidence of individual reading and investigation. There are frequent errors in the referencing of literature and other sources. Although limited knowledge of research processes may be evident, nevertheless, the application of such knowledge is largely unsuccessful."
  versionsFrom: { like: cardiffmet/generic-2020/l3/research/30-39, similarity: 0.99 }
  spans: "none"
  echoes: none
  force: describes
  paraphrase: "Limited or patchy awareness of research; narrow sources, over-reliance on course materials; frequent referencing errors; research knowledge applied largely without success."   # the whole cell, our words; sentences in AC5a
  sentences: 4
- id: cardiffmet/generic-2020/l4/research/1-29
  level: l4
  criterion: "Research / scholarship"
  band: { label: "1-29% (Clear Fail)", range: "1-29", axis: fail-low }
  span: { start: 34784, end: 35120 }
  source: "May demonstrate little knowledge of current research/scholarship in the discipline. Evidence of individual reading and investigation is negligible and the limited referencing of literature and other sources is frequently inaccurate. Very limited knowledge of research processes is apparent and there is a failure to apply this knowledge"
  versionsFrom: { sameAs: cardiffmet/generic-2020/l3/research/1-29 }
  spans: "none"
  echoes: none
  force: describes
  paraphrase: "Little knowledge of current research; negligible own reading; referencing scant and often wrong; little grasp or use of research processes."   # the whole cell, our words; sentences in AC5a
  sentences: 3
- id: cardiffmet/generic-2020/l4/argument/80-100
  level: l4
  criterion: "Structured argument and critical evaluation"
  band: { label: "80%-100% (1st Class +)", range: "80-100", axis: 80-100 }
  span: { start: 35196, end: 35297 }
  source: "Further to the 70%-79% band, work in the 80%-100% bands would extend beyond that expected at Level 4."
  versionsFrom: { sameAs: cardiffmet/generic-2020/l3/knowledge/80-100 }
  spans: "none"
  echoes: none
  force: describes
  paraphrase: "The top band goes further than 70-79, past what this level expects."   # the whole cell, our words; sentences in AC5a
  sentences: 1
- id: cardiffmet/generic-2020/l4/argument/70-79
  level: l4
  criterion: "Structured argument and critical evaluation"
  band: { label: "70%-79% (1st)", range: "70-79", axis: 70-79 }
  span: { start: 35364, end: 36052 }
  source: "May demonstrate an ability to communicate the results of their study/work accurately and reliably with structured and coherent arguments. Arguments are well developed, sustained and substantiated. Where relevant, basic assumptions are challenged and there is recognition of the complexities of academic debate. Appropriate solutions are offered to problems and there is review of their effectiveness and appropriateness. There is strong evidence that the student is able to reflect effectively on her/his own practice. Critical evaluation of the student’s own work and/or professional practice is highly perceptive and there is a full awareness of the implications for future development."
  versionsFrom: none
  spans: "none"
  echoes: { statement: qaa/fheq-2024/4.10.b4, words: 10 }
  force: describes
  paraphrase: "Reports results accurately in structured, coherent arguments, well developed and supported; challenges assumptions where relevant; sees the complexity of debate; reviews solutions; reflects on own practice with high perception."   # the whole cell, our words; sentences in AC5a
  sentences: 6
- id: cardiffmet/generic-2020/l4/argument/60-69
  level: l4
  criterion: "Structured argument and critical evaluation"
  band: { label: "60%-69% (2:1)", range: "60-69", axis: 60-69 }
  span: { start: 36119, end: 36576 }
  source: "May demonstrate an ability to communicate the results of their study/work accurately and reliably. Arguments are clearly considered and substantiated and there is evidence of an ability to make appropriate judgements and to suggest solutions to problems and review their effectiveness and appropriateness. The student also demonstrates an ability to engage in reflective practice and to take account of personal evaluations, planning for future development."
  versionsFrom: none
  spans: "none"
  echoes: { statement: qaa/fheq-2024/4.10.b4, words: 10 }
  force: describes
  paraphrase: "Reports results accurately; arguments considered and supported; judges fittingly, suggests and reviews solutions; reflects on own practice and plans development."   # the whole cell, our words; sentences in AC5a
  sentences: 3
- id: cardiffmet/generic-2020/l4/argument/50-59
  level: l4
  criterion: "Structured argument and critical evaluation"
  band: { label: "50%-59% (2:2)", range: "50-59", axis: 50-59 }
  span: { start: 36643, end: 37087 }
  source: "May demonstrate, at times, an ability to communicate the results of their study/work accurately and reliably, although there may be some over-reliance on description and factual presentation. Arguments are usually substantiated. There is some evidence of the student’s ability to evaluate and reflect on the student’s own practice. own practice but reflections may lack insight and the implications for future development may be underestimated."
  versionsFrom: { like: cardiffmet/generic-2020/l3/argument/50-59, similarity: 0.99 }
  spans: "none"
  echoes: { statement: qaa/fheq-2024/4.10.b4, words: 10 }
  force: describes
  paraphrase: "Reports results accurately at times, leaning on description; arguments usually supported; some evaluation of and reflection on own practice, though lacking insight into future development."   # the whole cell, our words; sentences in AC5a
  sentences: 3
- id: cardiffmet/generic-2020/l4/argument/40-49
  level: l4
  criterion: "Structured argument and critical evaluation"
  band: { label: "40%-49% (3rd)", range: "40-49", axis: 40-49 }
  span: { start: 37154, end: 37645 }
  source: "May demonstrate a limited ability to communicate the results of their study/work accurately and reliably. The balance within the work is likely to be in favour of description and factual presentation. Arguments are generally substantiated but may be under-developed. There is some evidence of the student’s ability to evaluate and reflect on the student’s own practice. although reflections may be limited and superficial, with little consideration of their relevance for future development."
  versionsFrom: { sameAs: cardiffmet/generic-2020/l3/argument/40-49 }
  spans: "none"
  echoes: { statement: qaa/fheq-2024/4.10.b4, words: 10 }
  force: describes
  paraphrase: "Limited accurate reporting; mostly description; arguments generally supported but thin; some reflection on own practice, limited and superficial."   # the whole cell, our words; sentences in AC5a
  sentences: 4
- id: cardiffmet/generic-2020/l4/argument/30-39
  level: l4
  criterion: "Structured argument and critical evaluation"
  band: { label: "30-39% (Narrow Fail)", range: "30-39", axis: fail-high }
  span: { start: 37719, end: 38009 }
  source: "May demonstrate limited evidence of an ability to communicate the results of their study/work accurately and reliably. The work is largely descriptive and arguments, if attempted, are rarely substantiated. Self-evaluation and reflections on the student’s own practice are extremely limited."
  versionsFrom: { sameAs: cardiffmet/generic-2020/l3/argument/30-39 }
  spans: "none"
  echoes: { statement: qaa/fheq-2024/4.10.b4, words: 10 }
  force: describes
  paraphrase: "Little sign of accurate reporting; largely descriptive; arguments, if tried, rarely supported; self-evaluation very limited."   # the whole cell, our words; sentences in AC5a
  sentences: 3
- id: cardiffmet/generic-2020/l4/argument/1-29
  level: l4
  criterion: "Structured argument and critical evaluation"
  band: { label: "1-29% (Clear Fail)", range: "1-29", axis: fail-low }
  span: { start: 38081, end: 38286 }
  source: "May demonstrate little evidence of an ability to communicate the results of their study/work accurately and reliably. Self-evaluation and reflections on the student’s own practice are negligible or absent."
  versionsFrom: { sameAs: cardiffmet/generic-2020/l3/argument/1-29 }
  spans: "none"
  echoes: { statement: qaa/fheq-2024/4.10.b4, words: 10 }
  force: describes
  paraphrase: "Little or no accurate reporting; self-evaluation and reflection negligible or absent."   # the whole cell, our words; sentences in AC5a
  sentences: 2
- id: cardiffmet/generic-2020/l5/overall/80-100
  level: l5
  criterion: "Overall summary"
  band: { label: "80%-100% (1st Class +)", range: "80-100", axis: 80-100 }
  span: { start: 38368, end: 38600 }
  source: "A full and detailed understanding of the set task and an ability to have met the learning outcomes and address the assessment criteria at an excellent level (80-89%) or outstanding and exceptional level (90-100%) and beyond level 5."
  versionsFrom: { sameAs: cardiffmet/generic-2020/l3/overall/80-100 }
  spans: "none"
  echoes: none
  force: describes
  paraphrase: "Full, detailed grasp of the task; outcomes met and criteria addressed excellently (80-89) or outstandingly (90-100), beyond this level."   # the whole cell, our words; sentences in AC5a
  sentences: 1
- id: cardiffmet/generic-2020/l5/overall/70-79
  level: l5
  criterion: "Overall summary"
  band: { label: "70%-79% (1st)", range: "70-79", axis: 70-79 }
  span: { start: 38639, end: 38795 }
  source: "A full and detailed understanding of the set task and an ability to have met the learning outcomes and address the assessment criteria at a very good level."
  versionsFrom: { sameAs: cardiffmet/generic-2020/l3/overall/70-79 }
  spans: "none"
  echoes: none
  force: describes
  paraphrase: "Full, detailed grasp of the task; outcomes met and criteria addressed very well."   # the whole cell, our words; sentences in AC5a
  sentences: 1
- id: cardiffmet/generic-2020/l5/overall/60-69
  level: l5
  criterion: "Overall summary"
  band: { label: "60%-69% (2:1)", range: "60-69", axis: 60-69 }
  span: { start: 38834, end: 38972 }
  source: "A full understanding of the set task and an ability to have met the learning outcomes and address the assessment criteria at a good level."
  versionsFrom: { sameAs: cardiffmet/generic-2020/l3/overall/60-69 }
  spans: "none"
  echoes: none
  force: describes
  paraphrase: "Full grasp of the task; outcomes met and criteria addressed well."   # the whole cell, our words; sentences in AC5a
  sentences: 1
- id: cardiffmet/generic-2020/l5/overall/50-59
  level: l5
  criterion: "Overall summary"
  band: { label: "50%-59% (2:2)", range: "50-59", axis: 50-59 }
  span: { start: 39011, end: 39170 }
  source: "A secure understanding of the set task and an ability to have met the associated learning outcomes and address the assessment criteria at a satisfactory level."
  versionsFrom: { sameAs: cardiffmet/generic-2020/l3/overall/50-59 }
  spans: "none"
  echoes: none
  force: describes
  paraphrase: "Secure grasp of the task; outcomes met and criteria addressed satisfactorily."   # the whole cell, our words; sentences in AC5a
  sentences: 1
- id: cardiffmet/generic-2020/l5/overall/40-49
  level: l5
  criterion: "Overall summary"
  band: { label: "40%-49% (3rd)", range: "40-49", axis: 40-49 }
  span: { start: 39209, end: 39364 }
  source: "A basic understanding of the set task and an ability to have met the associated learning outcomes and address the assessment criteria at a threshold level."
  versionsFrom: { sameAs: cardiffmet/generic-2020/l3/overall/40-49 }
  spans: "none"
  echoes: none
  force: describes
  paraphrase: "Basic grasp of the task; outcomes met and criteria addressed at the threshold."   # the whole cell, our words; sentences in AC5a
  sentences: 1
- id: cardiffmet/generic-2020/l5/overall/30-39
  level: l5
  criterion: "Overall summary"
  band: { label: "30-39% (Narrow Fail)", range: "30-39", axis: fail-high }
  span: { start: 39410, end: 39658 }
  source: "Unsatisfactory overall. A partial understanding of the set task and an ability to have met some of the associated learning outcomes at a basic level. Attainment is uneven with some learning outcomes not met and some assessment criteria unaddressed."
  versionsFrom: { like: cardiffmet/generic-2020/l3/overall/30-39, similarity: 0.97 }
  spans: "none"
  echoes: none
  force: describes
  paraphrase: "Unsatisfactory: partial grasp; some outcomes met at a basic level, others not; some criteria unaddressed; uneven."   # the whole cell, our words; sentences in AC5a
  sentences: 3
- id: cardiffmet/generic-2020/l5/overall/1-29
  level: l5
  criterion: "Overall summary"
  band: { label: "1-29% (Clear Fail)", range: "1-29", axis: fail-low }
  span: { start: 39702, end: 39862 }
  source: "Poor overall. Minimal understanding of the set task and will partially have met one or two learning outcomes, or none. Many assessment criteria are unaddressed."
  versionsFrom: { sameAs: cardiffmet/generic-2020/l4/overall/1-29 }
  spans: "none"
  echoes: none
  force: describes
  paraphrase: "Poor: minimal grasp of the task; one or two outcomes partly met, or none; many criteria unaddressed."   # the whole cell, our words; sentences in AC5a
  sentences: 3
- id: cardiffmet/generic-2020/l5/knowledge/80-100
  level: l5
  criterion: "Knowledge & Understanding"
  band: { label: "80%-100% (1st Class +)", range: "80-100", axis: 80-100 }
  span: { start: 39920, end: 40021 }
  source: "Further to the 70%-79% band, work in the 80%-100% bands would extend beyond that expected at Level 5."
  versionsFrom: { sameAs: cardiffmet/generic-2020/l3/knowledge/80-100 }
  spans: "none"
  echoes: none
  force: describes
  paraphrase: "The top band goes further than 70-79, past what this level expects."   # the whole cell, our words; sentences in AC5a
  sentences: 1
- id: cardiffmet/generic-2020/l5/knowledge/70-79
  level: l5
  criterion: "Knowledge & Understanding"
  band: { label: "70%-79% (1st)", range: "70-79", axis: 70-79 }
  span: { start: 40070, end: 40554 }
  source: "Demonstrates a detailed knowledge and critical understanding of underlying concepts and principles of the field of study relevant to the task. There is strong evidence of an ability to extend, transform and apply such knowledge. The student also demonstrates an ability to engage in confident discussion of complex concepts and to recognise the limitations and/or ambiguity of disciplinary knowledge. Independent thinking and original insights are also features of work at this level."
  versionsFrom: none
  spans: "none"
  echoes: none
  force: describes
  paraphrase: "Detailed knowledge and critical understanding of the field's concepts and principles, strongly extended and applied; confident discussion of complex concepts; recognises limits and ambiguity of knowledge; original insight."   # the whole cell, our words; sentences in AC5a
  sentences: 4
- id: cardiffmet/generic-2020/l5/knowledge/60-69
  level: l5
  criterion: "Knowledge & Understanding"
  band: { label: "60%-69% (2:1)", range: "60-69", axis: 60-69 }
  span: { start: 40603, end: 40941 }
  source: "Demonstrates a detailed knowledge and critical understanding of underlying concepts and principles of the field of study relevant to the task. There is good evidence of an ability to extend, transform and apply such knowledge. The discussion of complex concepts is often tackled successfully and there is evidence of independent thinking."
  versionsFrom: none
  spans: "none"
  echoes: none
  force: describes
  paraphrase: "Detailed knowledge and critical understanding of concepts and principles, well extended and applied; complex concepts often discussed well; independent thinking."   # the whole cell, our words; sentences in AC5a
  sentences: 3
- id: cardiffmet/generic-2020/l5/knowledge/50-59
  level: l5
  criterion: "Knowledge & Understanding"
  band: { label: "50%-59% (2:2)", range: "50-59", axis: 50-59 }
  span: { start: 40990, end: 41465 }
  source: "Demonstrates a sound knowledge and critical understanding of underlying concepts and principles of the field of study relevant to the task. There is evidence of an ability to extend, transform and apply such knowledge. Although there may be a tendency to reproduce information received from elsewhere (e.g. programme materials), there is still some evidence of independent thinking. A few errors and/or misconceptions may be present, but these will not be in important areas."
  versionsFrom: none
  spans: "none"
  echoes: none
  force: describes
  paraphrase: "Sound knowledge and critical understanding of concepts and principles, extended and applied; some reproduction of received material, but some independent thought; minor errors only."   # the whole cell, our words; sentences in AC5a
  sentences: 4
- id: cardiffmet/generic-2020/l5/knowledge/40-49
  level: l5
  criterion: "Knowledge & Understanding"
  band: { label: "40%-49% (3rd)", range: "40-49", axis: 40-49 }
  span: { start: 41514, end: 41992 }
  source: "Demonstrates a basic knowledge and critical understanding of underlying concepts and principles of the field of study relevant to the task. There is some evidence of an ability to extend, transform and apply such knowledge. Reproducing information received from elsewhere (e.g. programme materials) is a frequent feature of work at this level. Errors and misconceptions will be evident, but these are outweighed by the degree of knowledge and understanding demonstrated overall."
  versionsFrom: none
  spans: "none"
  echoes: none
  force: describes
  paraphrase: "Basic knowledge and critical understanding of concepts and principles, with some extension and application; frequent reproduction of received material; errors outweighed by what is understood."   # the whole cell, our words; sentences in AC5a
  sentences: 4
- id: cardiffmet/generic-2020/l5/knowledge/30-39
  level: l5
  criterion: "Knowledge & Understanding"
  band: { label: "30-39% (Narrow Fail)", range: "30-39", axis: fail-high }
  span: { start: 42048, end: 42423 }
  source: "Demonstrates limited knowledge and critical understanding of underlying concepts and principles of the field of study relevant to the task. There is insufficient evidence of an ability to extend, transform and apply such knowledge. Factual inaccuracies, errors and misconceptions are evident in important areas and elements of the assessed work may be irrelevant to the task."
  versionsFrom: none
  spans: "none"
  echoes: none
  force: describes
  paraphrase: "Limited knowledge and critical understanding; not enough extension or application; inaccuracies in important areas; parts off the task."   # the whole cell, our words; sentences in AC5a
  sentences: 3
- id: cardiffmet/generic-2020/l5/knowledge/1-29
  level: l5
  criterion: "Knowledge & Understanding"
  band: { label: "1-29% (Clear Fail)", range: "1-29", axis: fail-low }
  span: { start: 42477, end: 42933 }
  source: "Demonstrates little knowledge and critical understanding of underlying concepts and principles of the field of study relevant to the task. There is little evidence of an ability to extend, transform and apply such knowledge. Factual inaccuracies, errors and misconceptions are evident in many important areas and these outweigh the degree of knowledge and understanding demonstrated. Substantial elements of the assessed work may be irrelevant to the task."
  versionsFrom: none
  spans: "none"
  echoes: none
  force: describes
  paraphrase: "Little knowledge or critical understanding; little extension or application; errors in many important areas outweigh understanding; much off the task."   # the whole cell, our words; sentences in AC5a
  sentences: 4
- id: cardiffmet/generic-2020/l5/presentation/80-100
  level: l5
  criterion: "Presentation and communication"
  band: { label: "80%-100% (1st Class +)", range: "80-100", axis: 80-100 }
  span: { start: 42996, end: 43097 }
  source: "Further to the 70%-79% band, work in the 80%-100% bands would extend beyond that expected at Level 5."
  versionsFrom: { sameAs: cardiffmet/generic-2020/l3/knowledge/80-100 }
  spans: "none"
  echoes: none
  force: describes
  paraphrase: "The top band goes further than 70-79, past what this level expects."   # the whole cell, our words; sentences in AC5a
  sentences: 1
- id: cardiffmet/generic-2020/l5/presentation/70-79
  level: l5
  criterion: "Presentation and communication"
  band: { label: "70%-79% (1st)", range: "70-79", axis: 70-79 }
  span: { start: 43151, end: 43514 }
  source: "Demonstrates an ability to communicate information, arguments and analysis in a coherent and succinct manner in a range of situations. The standard of presentation is high and the format appropriate. Key points are logically organised and in written work, the style is lucid and mature. Arguments are well-defined and clearly articulated, structured and coherent."
  versionsFrom: none
  spans: "none"
  echoes: { statement: qaa/fheq-2024/4.12.b6, words: 7 }
  force: describes
  paraphrase: "Communicates information, argument and analysis coherently and concisely in many situations; high standard of presentation; logical, lucid and mature style; clear, structured arguments."   # the whole cell, our words; sentences in AC5a
  sentences: 4
- id: cardiffmet/generic-2020/l5/presentation/60-69
  level: l5
  criterion: "Presentation and communication"
  band: { label: "60%-69% (2:1)", range: "60-69", axis: 60-69 }
  span: { start: 43568, end: 43902 }
  source: "Demonstrates an ability to communicate information, arguments and analysis in a coherent and succinct manner in a range of situations. Work is well presented and the format appropriate. Key points are appropriately organised and in written work, the writing style is fluent and arguments are well articulated, structured and coherent."
  versionsFrom: none
  spans: "none"
  echoes: { statement: qaa/fheq-2024/4.12.b6, words: 7 }
  force: describes
  paraphrase: "Communicates information, argument and analysis coherently and concisely in many situations; well presented and organised; fluent style."   # the whole cell, our words; sentences in AC5a
  sentences: 3
- id: cardiffmet/generic-2020/l5/presentation/50-59
  level: l5
  criterion: "Presentation and communication"
  band: { label: "50%-59% (2:2)", range: "50-59", axis: 50-59 }
  span: { start: 43956, end: 44278 }
  source: "Demonstrates a satisfactory ability to communicate information, arguments and analysis in a coherent and succinct manner in a range of situations. Overall, the structure and format of the work are appropriate. There may be occasional faults in the presentation of work. These do not detract from the clarity of expression."
  versionsFrom: none
  spans: "none"
  echoes: { statement: qaa/fheq-2024/4.12.b6, words: 7 }
  force: describes
  paraphrase: "Satisfactory coherent, concise communication across situations; structure and format appropriate; occasional faults that do not obscure meaning."   # the whole cell, our words; sentences in AC5a
  sentences: 4
- id: cardiffmet/generic-2020/l5/presentation/40-49
  level: l5
  criterion: "Presentation and communication"
  band: { label: "40%-49% (3rd)", range: "40-49", axis: 40-49 }
  span: { start: 44332, end: 44782 }
  source: "Demonstrates a basic ability to communicate information, arguments and analysis in a coherent and succinct manner in a range of situations. However, more success is achieved in describing and reporting factual information, rather than communicating complex ideas. Generally, the work is appropriately structured although key points may not be logically sequenced. Although there will be faults in the presentation of work, the meaning is still clear."
  versionsFrom: none
  spans: "none"
  echoes: { statement: qaa/fheq-2024/4.12.b6, words: 7 }
  force: describes
  paraphrase: "Basic coherent communication; better at reporting facts than complex ideas; mostly structured, points not always in order; faults, but meaning clear."   # the whole cell, our words; sentences in AC5a
  sentences: 4
- id: cardiffmet/generic-2020/l5/presentation/30-39
  level: l5
  criterion: "Presentation and communication"
  band: { label: "30-39% (Narrow Fail)", range: "30-39", axis: fail-high }
  span: { start: 44843, end: 45065 }
  source: "Demonstrates a limited ability to communicate some basic concepts, arguments and analysis in a range of situations. If attempted, the presentation of arguments and more complex ideas may be confused and clumsily expressed."
  versionsFrom: none
  spans: "none"
  echoes: none
  force: describes
  paraphrase: "Limited communication of basic concepts and arguments; arguments and complex ideas, if tried, confused."   # the whole cell, our words; sentences in AC5a
  sentences: 2
- id: cardiffmet/generic-2020/l5/presentation/1-29
  level: l5
  criterion: "Presentation and communication"
  band: { label: "1-29% (Clear Fail)", range: "1-29", axis: fail-low }
  span: { start: 45124, end: 45442 }
  source: "Demonstrates little ability to communicate some basic concepts, arguments and analysis in a range of situations. Frequent faults in the presentation of work and significant difficulties in its structure and organisation detract from the clarity and meaning overall. The writing style is often clumsy and inappropriate."
  versionsFrom: none
  spans: "none"
  echoes: none
  force: describes
  paraphrase: "Little communication of basic concepts; frequent faults and weak structure obscure meaning; style often clumsy."   # the whole cell, our words; sentences in AC5a
  sentences: 3
- id: cardiffmet/generic-2020/l5/analysis/80-100
  level: l5
  criterion: "Analysis & discussion"
  band: { label: "80%-100% (1st Class +)", range: "80-100", axis: 80-100 }
  span: { start: 45496, end: 45746 }
  source: "Demonstrates the ability to design and undertake their own research or advanced scholarship, applying relevant techniques and methods appropriately. Further to the 70%-79% band, work in the 80%-100% bands would extend beyond that expected at Level 5."
  versionsFrom: none
  spans: "none"
  echoes: none
  force: describes
  paraphrase: "Designs and carries out own research or advanced scholarship with fitting techniques; beyond what this level expects."   # the whole cell, our words; sentences in AC5a
  sentences: 2
- id: cardiffmet/generic-2020/l5/analysis/70-79
  level: l5
  criterion: "Analysis & discussion"
  band: { label: "70%-79% (1st)", range: "70-79", axis: 70-79 }
  span: { start: 45791, end: 46207 }
  source: "Demonstrates an ability to undertake analysis of qualitative and quantitative data by making very good use of a range of established techniques. The student is highly successful in presenting, synthesising and commenting on outcomes and is able to comment perceptively and with insight on the relationship between theory and practice and the impact of the limits of their knowledge on the analysis of their findings."
  versionsFrom: none
  spans: "none"
  echoes: none
  force: describes
  paraphrase: "Analyses qualitative and quantitative data with very good use of established techniques; presents, synthesises and comments on results very successfully; perceptive on theory and practice and on the limits of own knowledge."   # the whole cell, our words; sentences in AC5a
  sentences: 2
- id: cardiffmet/generic-2020/l5/analysis/60-69
  level: l5
  criterion: "Analysis & discussion"
  band: { label: "60%-69% (2:1)", range: "60-69", axis: 60-69 }
  span: { start: 46252, end: 46669 }
  source: "Demonstrates an ability to undertake analysis of qualitative and quantitative data by making good use of a range of established techniques. The student is considerably successful in presenting, synthesising and commenting on outcomes and is able to comment perceptively and with insight on the relationship between theory and practice and the impact of the limits of their knowledge on the analysis of their findings."
  versionsFrom: none
  spans: "none"
  echoes: none
  force: describes
  paraphrase: "Analyses data with good use of established techniques; presents, synthesises and comments on results with considerable success; perceptive on theory, practice and the limits of own knowledge."   # the whole cell, our words; sentences in AC5a
  sentences: 2
- id: cardiffmet/generic-2020/l5/analysis/50-59
  level: l5
  criterion: "Analysis & discussion"
  band: { label: "50%-59% (2:2)", range: "50-59", axis: 50-59 }
  span: { start: 46714, end: 46976 }
  source: "Demonstrates an ability to undertake analysis of qualitative and quantitative data by making use of a range of established techniques and generally has success in presenting and commenting on outcomes. Awareness of the limits of their knowledge and their impact."
  versionsFrom: none
  spans: "none"
  echoes: { statement: qaa/fheq-2024/4.12.b4, words: 7 }
  force: describes
  paraphrase: "Analyses data with a range of established techniques; generally succeeds with results; aware of the limits of own knowledge and their effect."   # the whole cell, our words; sentences in AC5a
  sentences: 2
- id: cardiffmet/generic-2020/l5/analysis/40-49
  level: l5
  criterion: "Analysis & discussion"
  band: { label: "40%-49% (3rd)", range: "40-49", axis: 40-49 }
  span: { start: 47021, end: 47297 }
  source: "Demonstrates an ability to undertake analysis of qualitative and quantitative data by making basic use of a range of established techniques and has intermittent success in presenting and commenting on outcomes. Some awareness of the limits of their knowledge and their impact."
  versionsFrom: none
  spans: "none"
  echoes: { statement: qaa/fheq-2024/4.12.b4, words: 7 }
  force: describes
  paraphrase: "Analyses data with basic use of established techniques; intermittent success with results; some awareness of the limits of own knowledge."   # the whole cell, our words; sentences in AC5a
  sentences: 2
- id: cardiffmet/generic-2020/l5/analysis/30-39
  level: l5
  criterion: "Analysis & discussion"
  band: { label: "30-39% (Narrow Fail)", range: "30-39", axis: fail-high }
  span: { start: 47349, end: 47526 }
  source: "Is likely to have attempted to undertake analysis of qualitative and quantitative data relevant to the task/discipline but outcomes may be naïve, simplistic and/or unconvincing."
  versionsFrom: none
  spans: "none"
  echoes: none
  force: describes
  paraphrase: "Attempts data analysis, but results may be naive, simplistic or unconvincing."   # the whole cell, our words; sentences in AC5a
  sentences: 1
- id: cardiffmet/generic-2020/l5/analysis/1-29
  level: l5
  criterion: "Analysis & discussion"
  band: { label: "1-29% (Clear Fail)", range: "1-29", axis: fail-low }
  span: { start: 47576, end: 47788 }
  source: "Demonstrates little evidence of being able to undertake analysis of qualitative and quantitative data relevant to the task/discipline. Where such work has been attempted, outcomes may be inappropriate, or absent."
  versionsFrom: none
  spans: "none"
  echoes: none
  force: describes
  paraphrase: "Little evidence of data analysis; results, where attempted, unsuitable or missing."   # the whole cell, our words; sentences in AC5a
  sentences: 2
- id: cardiffmet/generic-2020/l5/research/80-100
  level: l5
  criterion: "Research / scholarship"
  band: { label: "80%-100% (1st Class +)", range: "80-100", axis: 80-100 }
  span: { start: 47843, end: 48166 }
  source: "In written coursework, reference citations extend significantly beyond the main body of reading normally expected in the discipline/field of study. In examinations, a substantial range of reference citations are included. Further to the 70%-79% band, work in the 80%-100% bands would extend beyond that expected at Level 5."
  versionsFrom: none
  spans: "none"
  echoes: none
  force: describes
  paraphrase: "Citations range well beyond the reading the field normally expects (coursework), or are substantial (examinations); beyond this level."   # the whole cell, our words; sentences in AC5a
  sentences: 3
- id: cardiffmet/generic-2020/l5/research/70-79
  level: l5
  criterion: "Research / scholarship"
  band: { label: "70%-79% (1st)", range: "70-79", axis: 70-79 }
  span: { start: 48212, end: 48792 }
  source: "Demonstrates a detailed and thorough knowledge of current research/advanced scholarship in the discipline. The use of scholarly reviews/primary sources is confident and a breadth and depth of individual reading and investigation, extending beyond the sources provided, is apparent. The referencing of literature and other sources is accurate and in line with academic conventions. A thorough knowledge and understanding of research processes, techniques and methods is demonstrated along with an ability to apply research knowledge and skills successfully in appropriate contexts."
  versionsFrom: none
  spans: "none"
  echoes: none
  force: describes
  paraphrase: "Detailed, thorough knowledge of current research; confident use of reviews and primary sources; reading beyond the sources given; accurate referencing; thorough grasp of research processes, applied successfully."   # the whole cell, our words; sentences in AC5a
  sentences: 4
- id: cardiffmet/generic-2020/l5/research/60-69
  level: l5
  criterion: "Research / scholarship"
  band: { label: "60%-69% (2:1)", range: "60-69", axis: 60-69 }
  span: { start: 48838, end: 49265 }
  source: "Demonstrates a good knowledge of current research/scholarship in the discipline. Examples referred to indicate a breadth and depth of individual reading and investigation that extend beyond the sources provided. The referencing of literature and other sources is almost always accurate. A secure knowledge of research processes is evident along with an ability to apply research skills and knowledge in the appropriate context."
  versionsFrom: none
  spans: "none"
  echoes: none
  force: describes
  paraphrase: "Good knowledge of current research; reading beyond the sources given; referencing almost always accurate; secure grasp of research processes, applied fittingly."   # the whole cell, our words; sentences in AC5a
  sentences: 4
- id: cardiffmet/generic-2020/l5/research/50-59
  level: l5
  criterion: "Research / scholarship"
  band: { label: "50%-59% (2:2)", range: "50-59", axis: 50-59 }
  span: { start: 49311, end: 49817 }
  source: "Demonstrates a satisfactory knowledge of current research/scholarship in the discipline and shows an ability to discuss its implications. Examples of research/scholarship referred to in the work demonstrate individual reading and investigation. Occasional errors may be present in the referencing of literature and other sources. Some knowledge of research processes is evident and the application of research skills and knowledge is generally successful, although there may be a reliance on tutor support."
  versionsFrom: none
  spans: "none"
  echoes: none
  force: describes
  paraphrase: "Satisfactory knowledge of current research and its implications; own reading; occasional referencing errors; research skills generally applied well, perhaps relying on tutor support."   # the whole cell, our words; sentences in AC5a
  sentences: 4
- id: cardiffmet/generic-2020/l5/research/40-49
  level: l5
  criterion: "Research / scholarship"
  band: { label: "40%-49% (3rd)", range: "40-49", axis: 40-49 }
  span: { start: 49863, end: 50371 }
  source: "Demonstrates basic knowledge of current research/scholarship in the discipline and demonstrates an ability to provide limited comment and/or discussion of its implications. Examples of research/scholarship referred to in the work may indicate an over-reliance on programme materials rather than individual reading and investigation. There are errors in the referencing of literature and other sources. Some knowledge of research processes is evident although the application of such knowledge is less secure."
  versionsFrom: none
  spans: "none"
  echoes: none
  force: describes
  paraphrase: "Basic knowledge of current research, with limited comment on its implications; over-reliance on course materials; referencing errors; research processes applied less securely."   # the whole cell, our words; sentences in AC5a
  sentences: 4
- id: cardiffmet/generic-2020/l5/research/30-39
  level: l5
  criterion: "Research / scholarship"
  band: { label: "30-39% (Narrow Fail)", range: "30-39", axis: fail-high }
  span: { start: 50424, end: 50896 }
  source: "Demonstrates limited or sporadic knowledge of current research/scholarship in the discipline. A restricted range of sources are used but overall, there is an over-reliance on programme materials with little evidence of individual reading and investigation. There are frequent errors in the referencing of literature and other sources. Although limited knowledge of research processes may be evident, nevertheless, the application of such knowledge is largely unsuccessful."
  versionsFrom: { like: cardiffmet/generic-2020/l3/research/30-39, similarity: 0.96 }
  spans: "none"
  echoes: none
  force: describes
  paraphrase: "Limited or patchy awareness of research; narrow sources, over-reliance on course materials; frequent referencing errors; research knowledge applied largely without success."   # the whole cell, our words; sentences in AC5a
  sentences: 4
- id: cardiffmet/generic-2020/l5/research/1-29
  level: l5
  criterion: "Research / scholarship"
  band: { label: "1-29% (Clear Fail)", range: "1-29", axis: fail-low }
  span: { start: 50947, end: 51281 }
  source: "Demonstrates little knowledge of current research/scholarship in the discipline. Evidence of individual reading and investigation is negligible and the limited referencing of literature and other sources is frequently inaccurate. Very limited knowledge of research processes is apparent and there is a failure to apply this knowledge."
  versionsFrom: { like: cardiffmet/generic-2020/l3/research/1-29, similarity: 0.97 }
  spans: "none"
  echoes: none
  force: describes
  paraphrase: "Little knowledge of current research; negligible own reading; referencing scant and often wrong; little grasp or use of research processes."   # the whole cell, our words; sentences in AC5a
  sentences: 3
- id: cardiffmet/generic-2020/l5/argument/80-100
  level: l5
  criterion: "Structured argument and critical evaluation"
  band: { label: "80%-100% (1st Class +)", range: "80-100", axis: 80-100 }
  span: { start: 51357, end: 51585 }
  source: "Important insights are offered that are informed by critical evaluation of current research/scholarship/professional practice. Further to the 70%-79% band, work in the 80%-100% bands would extend beyond that expected at Level 5."
  versionsFrom: none
  spans: "none"
  echoes: none
  force: describes
  paraphrase: "Offers important insights informed by critical evaluation of current research, scholarship or practice; beyond this level."   # the whole cell, our words; sentences in AC5a
  sentences: 2
- id: cardiffmet/generic-2020/l5/argument/70-79
  level: l5
  criterion: "Structured argument and critical evaluation"
  band: { label: "70%-79% (1st)", range: "70-79", axis: 70-79 }
  span: { start: 51652, end: 52367 }
  source: "Demonstrates an ability to solve broadly defined, complex problems and to engage in critical understanding of principles in the field of study. Arguments are well developed, sustained and substantiated. Where relevant, assumptions are challenged and there is clear recognition of the complexities of academic debate. Appropriate and sometimes innovative solutions are offered to problems, evaluating different approaches to solving problems. There is strong evidence that the student is able to reflect effectively on the student’s own practice. Critical evaluation of the student’s own work and/or professional practice is highly perceptive and there is a full awareness of the implications for future development."
  versionsFrom: none
  spans: "none"
  echoes: none
  force: describes
  paraphrase: "Solves broadly defined, complex problems with critical understanding of the field's principles; well-developed, supported arguments; challenges assumptions; sometimes innovative solutions, weighing approaches; highly perceptive self-evaluation."   # the whole cell, our words; sentences in AC5a
  sentences: 6
- id: cardiffmet/generic-2020/l5/argument/60-69
  level: l5
  criterion: "Structured argument and critical evaluation"
  band: { label: "60%-69% (2:1)", range: "60-69", axis: 60-69 }
  span: { start: 52434, end: 52942 }
  source: "Demonstrates an ability to solve broadly defined, complex problems and to engage in critical understanding of principles in the field of study. Arguments are clearly considered and substantiated and there is evidence of an ability to make appropriate judgements and to suggest solutions to problems, evaluating different approaches to solving problems. The student also demonstrates an ability to engage in reflective practice and to take account of personal evaluations when planning for future development."
  versionsFrom: none
  spans: "none"
  echoes: none
  force: describes
  paraphrase: "Solves broadly defined, complex problems with critical understanding; considered, supported arguments; judges fittingly and suggests solutions, weighing approaches; reflects on own practice to plan development."   # the whole cell, our words; sentences in AC5a
  sentences: 3
- id: cardiffmet/generic-2020/l5/argument/50-59
  level: l5
  criterion: "Structured argument and critical evaluation"
  band: { label: "50%-59% (2:2)", range: "50-59", axis: 50-59 }
  span: { start: 53009, end: 53486 }
  source: "Demonstrates a satisfactory ability to solve broadly defined, complex problems and to engage in critical understanding of principles in the field of study, although there may be some over-reliance on description and factual presentation. Arguments are usually substantiated. There is some evidence of the student’s ability to evaluate and reflect on the student’s own practice, but reflections may lack insight and the implications for future development may be underestimated."
  versionsFrom: none
  spans: "none"
  echoes: none
  force: describes
  paraphrase: "Satisfactory problem-solving and critical understanding, with some leaning on description; arguments usually supported; some reflection, lacking insight into future development."   # the whole cell, our words; sentences in AC5a
  sentences: 3
- id: cardiffmet/generic-2020/l5/argument/40-49
  level: l5
  criterion: "Structured argument and critical evaluation"
  band: { label: "40%-49% (3rd)", range: "40-49", axis: 40-49 }
  span: { start: 53553, end: 54132 }
  source: "Demonstrates a basic ability to solve broadly defined, complex problems and to engage in critical understanding of principles in the field of study. Although some critical reflection is evident, the balance within the work is likely to be in favour of description and factual presentation. Arguments are generally substantiated but may be under-developed. There is some evidence of the student’s ability to evaluate and reflect on the student’s own practice. although reflections may be limited and superficial with little consideration of their relevance for future development."
  versionsFrom: none
  spans: "none"
  echoes: none
  force: describes
  paraphrase: "Basic problem-solving and critical understanding; some critical reflection but mostly description; arguments generally supported but thin; reflection limited and superficial."   # the whole cell, our words; sentences in AC5a
  sentences: 4
- id: cardiffmet/generic-2020/l5/argument/30-39
  level: l5
  criterion: "Structured argument and critical evaluation"
  band: { label: "30-39% (Narrow Fail)", range: "30-39", axis: fail-high }
  span: { start: 54206, end: 54537 }
  source: "Demonstrates little evidence of ability to solve broadly defined, complex problems and to engage in critical understanding of principles in the field of study. The work is largely descriptive and arguments, if attempted, are rarely substantiated. Self-evaluation and reflections on the student’s own practice are extremely limited."
  versionsFrom: none
  spans: "none"
  echoes: none
  force: describes
  paraphrase: "Little sign of complex problem-solving or critical understanding; largely descriptive; arguments rarely supported; self-evaluation very limited."   # the whole cell, our words; sentences in AC5a
  sentences: 3
- id: cardiffmet/generic-2020/l5/argument/1-29
  level: l5
  criterion: "Structured argument and critical evaluation"
  band: { label: "1-29% (Clear Fail)", range: "1-29", axis: fail-low }
  span: { start: 54609, end: 54889 }
  source: "Demonstrates little ability to describe and report but very little evidence is available to indicate an ability to solve broadly defined, complex problems and engage in critical understanding. Self-evaluation and reflections on the student’s own practice are negligible or absent."
  versionsFrom: none
  spans: "none"
  echoes: none
  force: describes
  paraphrase: "Some description and reporting, but very little sign of problem-solving or critical understanding; self-evaluation negligible or absent."   # the whole cell, our words; sentences in AC5a
  sentences: 2
- id: cardiffmet/generic-2020/l6/overall/80-100
  level: l6
  criterion: "Overall summary"
  band: { label: "80%-100% (1st Class +)", range: "80-100", axis: 80-100 }
  span: { start: 54971, end: 55309 }
  source: "A full and detailed understanding of the set task and an ability to have met the learning outcomes and address the assessment criteria at an excellent level (80-89%) or outstanding and exceptional level (90-100%) and beyond level 6. Work is of a standard deemed to be worthy of publication/manufacture/public exhibition/public performance"
  versionsFrom: none
  spans: "none"
  echoes: none
  force: describes
  paraphrase: "Full, detailed grasp of the task; outcomes met excellently (80-89) or outstandingly (90-100), beyond this level; work of a standard fit for publication, manufacture, exhibition or performance."   # the whole cell, our words; sentences in AC5a
  sentences: 2
- id: cardiffmet/generic-2020/l6/overall/70-79
  level: l6
  criterion: "Overall summary"
  band: { label: "70%-79% (1st)", range: "70-79", axis: 70-79 }
  span: { start: 55348, end: 55504 }
  source: "A full and detailed understanding of the set task and an ability to have met the learning outcomes and address the assessment criteria at a very good level."
  versionsFrom: { sameAs: cardiffmet/generic-2020/l3/overall/70-79 }
  spans: "none"
  echoes: none
  force: describes
  paraphrase: "Full, detailed grasp of the task; outcomes met and criteria addressed very well."   # the whole cell, our words; sentences in AC5a
  sentences: 1
- id: cardiffmet/generic-2020/l6/overall/60-69
  level: l6
  criterion: "Overall summary"
  band: { label: "60%-69% (2:1)", range: "60-69", axis: 60-69 }
  span: { start: 55543, end: 55681 }
  source: "A full understanding of the set task and an ability to have met the learning outcomes and address the assessment criteria at a good level."
  versionsFrom: { sameAs: cardiffmet/generic-2020/l3/overall/60-69 }
  spans: "none"
  echoes: none
  force: describes
  paraphrase: "Full grasp of the task; outcomes met and criteria addressed well."   # the whole cell, our words; sentences in AC5a
  sentences: 1
- id: cardiffmet/generic-2020/l6/overall/50-59
  level: l6
  criterion: "Overall summary"
  band: { label: "50%-59% (2:2)", range: "50-59", axis: 50-59 }
  span: { start: 55720, end: 55879 }
  source: "A secure understanding of the set task and an ability to have met the associated learning outcomes and address the assessment criteria at a satisfactory level."
  versionsFrom: { sameAs: cardiffmet/generic-2020/l3/overall/50-59 }
  spans: "none"
  echoes: none
  force: describes
  paraphrase: "Secure grasp of the task; outcomes met and criteria addressed satisfactorily."   # the whole cell, our words; sentences in AC5a
  sentences: 1
- id: cardiffmet/generic-2020/l6/overall/40-49
  level: l6
  criterion: "Overall summary"
  band: { label: "40%-49% (3rd)", range: "40-49", axis: 40-49 }
  span: { start: 55918, end: 56073 }
  source: "A basic understanding of the set task and an ability to have met the associated learning outcomes and address the assessment criteria at a threshold level."
  versionsFrom: { sameAs: cardiffmet/generic-2020/l3/overall/40-49 }
  spans: "none"
  echoes: none
  force: describes
  paraphrase: "Basic grasp of the task; outcomes met and criteria addressed at the threshold."   # the whole cell, our words; sentences in AC5a
  sentences: 1
- id: cardiffmet/generic-2020/l6/overall/30-39
  level: l6
  criterion: "Overall summary"
  band: { label: "30-39% (Narrow Fail)", range: "30-39", axis: fail-high }
  span: { start: 56119, end: 56376 }
  source: "Unsatisfactory overall. A partial understanding of the set task and an ability to have met some of the associated learning outcomes at a basic level. However, attainment is uneven with some learning outcomes not met and some assessment criteria unaddressed."
  versionsFrom: { sameAs: cardiffmet/generic-2020/l3/overall/30-39 }
  spans: "none"
  echoes: none
  force: describes
  paraphrase: "Unsatisfactory: partial grasp; some outcomes met at a basic level, others not; some criteria unaddressed; uneven."   # the whole cell, our words; sentences in AC5a
  sentences: 3
- id: cardiffmet/generic-2020/l6/overall/1-29
  level: l6
  criterion: "Overall summary"
  band: { label: "1-29% (Clear Fail)", range: "1-29", axis: fail-low }
  span: { start: 56420, end: 56571 }
  source: "Poor overall. Minimal understanding of the set task and will partially have met one or two learning outcomes. Many assessment criteria are unaddressed."
  versionsFrom: { like: cardiffmet/generic-2020/l4/overall/1-29, similarity: 0.96 }
  spans: "none"
  echoes: none
  force: describes
  paraphrase: "Poor: minimal grasp of the task; one or two outcomes partly met, or none; many criteria unaddressed."   # the whole cell, our words; sentences in AC5a
  sentences: 3
- id: cardiffmet/generic-2020/l6/knowledge/80-100
  level: l6
  criterion: "Knowledge & Understanding"
  band: { label: "80%-100% (1st Class +)", range: "80-100", axis: 80-100 }
  span: { start: 56629, end: 56795 }
  source: "Further to the 70%-79% band, work in the 80%-100% bands would extend beyond that expected at Level 6. Demonstrates exceptional knowledge and systematic understanding."
  versionsFrom: none
  spans: "none"
  echoes: none
  force: describes
  paraphrase: "Beyond what this level expects: exceptional knowledge and systematic understanding."   # the whole cell, our words; sentences in AC5a
  sentences: 2
- id: cardiffmet/generic-2020/l6/knowledge/70-79
  level: l6
  criterion: "Knowledge & Understanding"
  band: { label: "70%-79% (1st)", range: "70-79", axis: 70-79 }
  span: { start: 56844, end: 57326 }
  source: "A detailed knowledge and systematic understanding of key aspects of the field of study relevant to the task. There is strong evidence of an ability to extend, transform and apply such knowledge. The student also demonstrates an ability to engage in confident discussion of complex concepts and to recognise the limitations and/or ambiguity of disciplinary knowledge. Independent thinking and original insights and self-management of learning are also features of work at this level."
  versionsFrom: none
  spans: "none"
  echoes: none
  force: describes
  paraphrase: "Detailed knowledge and systematic understanding of key aspects, strongly extended and applied; confident discussion of complex concepts; recognises limits of knowledge; original insight; manages own learning."   # the whole cell, our words; sentences in AC5a
  sentences: 4
- id: cardiffmet/generic-2020/l6/knowledge/60-69
  level: l6
  criterion: "Knowledge & Understanding"
  band: { label: "60%-69% (2:1)", range: "60-69", axis: 60-69 }
  span: { start: 57375, end: 57738 }
  source: "A detailed knowledge and thorough understanding of key aspects of the field of study relevant to the task. There is clear evidence of an ability to apply such knowledge and, in some contexts, to extend and transform it. The discussion of complex concepts is often tackled successfully and there is evidence of independent thinking and self-management of learning."
  versionsFrom: none
  spans: "none"
  echoes: none
  force: describes
  paraphrase: "Detailed knowledge and thorough understanding of key aspects, clearly applied and sometimes extended; complex concepts often discussed well; independent thinking; manages own learning."   # the whole cell, our words; sentences in AC5a
  sentences: 3
- id: cardiffmet/generic-2020/l6/knowledge/50-59
  level: l6
  criterion: "Knowledge & Understanding"
  band: { label: "50%-59% (2:2)", range: "50-59", axis: 50-59 }
  span: { start: 57787, end: 58249 }
  source: "A sound knowledge and understanding of most key aspects of the field of study relevant to the task and there is some evidence of an ability to apply such knowledge. Although there may be a tendency to reproduce information received from elsewhere (e.g. programme materials), there is still some evidence of independent thinking. A few errors and/or misconceptions may be present, but these will not be in important areas. Evidence of self-management of learning."
  versionsFrom: none
  spans: "none"
  echoes: none
  force: describes
  paraphrase: "Sound knowledge of most key aspects, with some application; some reproduction of received material, some independent thought; minor errors only; some self-management of learning."   # the whole cell, our words; sentences in AC5a
  sentences: 4
- id: cardiffmet/generic-2020/l6/knowledge/40-49
  level: l6
  criterion: "Knowledge & Understanding"
  band: { label: "40%-49% (3rd)", range: "40-49", axis: 40-49 }
  span: { start: 58298, end: 58689 }
  source: "A basic knowledge and understanding of many aspects of the field of study relevant to the task. Reproducing information received from elsewhere (e.g. programme materials) is a frequent feature of work at this level. Errors and misconceptions will be evident, but these are outweighed by the degree of knowledge and understanding demonstrated overall. Evidence of self-management of learning."
  versionsFrom: none
  spans: "none"
  echoes: none
  force: describes
  paraphrase: "Basic knowledge of many aspects of the field; frequent reproduction of received material; errors outweighed by understanding; some self-management of learning."   # the whole cell, our words; sentences in AC5a
  sentences: 4
- id: cardiffmet/generic-2020/l6/knowledge/30-39
  level: l6
  criterion: "Knowledge & Understanding"
  band: { label: "30-39% (Narrow Fail)", range: "30-39", axis: fail-high }
  span: { start: 58745, end: 58968 }
  source: "Limited knowledge and understanding of the field of study relevant to the task. Factual inaccuracies, errors and misconceptions are evident in important areas and elements of the assessed work may be irrelevant to the task."
  versionsFrom: { like: cardiffmet/generic-2020/l3/knowledge/30-39, similarity: 0.97 }
  spans: "none"
  echoes: none
  force: describes
  paraphrase: "Limited knowledge of the field; inaccuracies and misconceptions in important areas; parts of the work off the task."   # the whole cell, our words; sentences in AC5a
  sentences: 2
- id: cardiffmet/generic-2020/l6/knowledge/1-29
  level: l6
  criterion: "Knowledge & Understanding"
  band: { label: "1-29% (Clear Fail)", range: "1-29", axis: fail-low }
  span: { start: 59022, end: 59332 }
  source: "Little knowledge and understanding of the field of study relevant to the task. Factual inaccuracies, errors and misconceptions are evident in many important areas and these outweigh the degree of knowledge and understanding demonstrated. Substantial elements of the assessed work may be irrelevant to the task."
  versionsFrom: { like: cardiffmet/generic-2020/l3/knowledge/1-29, similarity: 0.98 }
  spans: "none"
  echoes: none
  force: describes
  paraphrase: "Little knowledge of the field; errors in many important areas outweigh what is understood; much of the work off the task."   # the whole cell, our words; sentences in AC5a
  sentences: 3
- id: cardiffmet/generic-2020/l6/presentation/80-100
  level: l6
  criterion: "Presentation and communication"
  band: { label: "80%-100% (1st Class +)", range: "80-100", axis: 80-100 }
  span: { start: 59395, end: 59589 }
  source: "Further to the 70%-79% band, work in the 80%-100% bands would extend beyond that expected at Level 6. The standard of presentation attains the professional standards expected for the discipline."
  versionsFrom: none
  spans: "none"
  echoes: none
  force: describes
  paraphrase: "Beyond what this level expects: presentation reaches the discipline's professional standard."   # the whole cell, our words; sentences in AC5a
  sentences: 2
- id: cardiffmet/generic-2020/l6/presentation/70-79
  level: l6
  criterion: "Presentation and communication"
  band: { label: "70%-79% (1st)", range: "70-79", axis: 70-79 }
  span: { start: 59643, end: 59972 }
  source: "An ability to communicate information, complex ideas and concepts in a coherent and succinct manner in a range of situations. The standard of presentation is high and the format appropriate. Key points are logically organised and in written work, the style is lucid and mature. Arguments are well-defined and clearly articulated."
  versionsFrom: none
  spans: "none"
  echoes: none
  force: describes
  paraphrase: "Communicates information and complex ideas coherently and concisely in many situations; high standard of presentation; logical, lucid, mature style; clear arguments."   # the whole cell, our words; sentences in AC5a
  sentences: 4
- id: cardiffmet/generic-2020/l6/presentation/60-69
  level: l6
  criterion: "Presentation and communication"
  band: { label: "60%-69% (2:1)", range: "60-69", axis: 60-69 }
  span: { start: 60026, end: 60307 }
  source: "An ability to communicate information, ideas and concepts clearly and succinctly in a range of situations. Work is well presented and the format appropriate. Key points are appropriately organised and in written work, the writing style is fluent and arguments are well articulated."
  versionsFrom: none
  spans: "none"
  echoes: none
  force: describes
  paraphrase: "Communicates information and ideas clearly and concisely in many situations; well presented and organised; fluent style."   # the whole cell, our words; sentences in AC5a
  sentences: 3
- id: cardiffmet/generic-2020/l6/presentation/50-59
  level: l6
  criterion: "Presentation and communication"
  band: { label: "50%-59% (2:2)", range: "50-59", axis: 50-59 }
  span: { start: 60361, end: 60681 }
  source: "Demonstrates a satisfactory ability to communicate information, ideas, concepts and arguments successfully in a range of situations. Overall, the structure and format of the work are appropriate. There may be occasional faults in the presentation of work but overall, these do not detract from the clarity of expression."
  versionsFrom: none
  spans: "none"
  echoes: none
  force: describes
  paraphrase: "Satisfactory communication of information, ideas and arguments in many situations; structure and format appropriate; occasional faults that do not obscure meaning."   # the whole cell, our words; sentences in AC5a
  sentences: 3
- id: cardiffmet/generic-2020/l6/presentation/40-49
  level: l6
  criterion: "Presentation and communication"
  band: { label: "40%-49% (3rd)", range: "40-49", axis: 40-49 }
  span: { start: 60735, end: 61141 }
  source: "Some ability to communicate information, ideas, concepts and arguments in a range of situations. However, more success is achieved in describing and reporting factual information rather than communicating complex ideas. Generally, the work is appropriately structured although key points may not be logically sequenced. Although there will be faults in the presentation of work, the meaning is still clear."
  versionsFrom: none
  spans: "none"
  echoes: none
  force: describes
  paraphrase: "Some communication of ideas and arguments; better at reporting facts than complex ideas; mostly structured, points not always in order; faults, but meaning clear."   # the whole cell, our words; sentences in AC5a
  sentences: 4
- id: cardiffmet/generic-2020/l6/presentation/30-39
  level: l6
  criterion: "Presentation and communication"
  band: { label: "30-39% (Narrow Fail)", range: "30-39", axis: fail-high }
  span: { start: 61202, end: 61521 }
  source: "Limited ability to communicate simple concepts and/or factual information in a range of situations. However, faults in the presentation of work and in its structure and organisation mar the clarity of expression. If attempted, the presentation of arguments and more complex ideas may be confused and clumsily expressed."
  versionsFrom: none
  spans: "none"
  echoes: none
  force: describes
  paraphrase: "Limited communication of simple concepts or facts; faults in presentation and structure mar clarity; complex ideas, if tried, confused."   # the whole cell, our words; sentences in AC5a
  sentences: 3
- id: cardiffmet/generic-2020/l6/presentation/1-29
  level: l6
  criterion: "Presentation and communication"
  band: { label: "1-29% (Clear Fail)", range: "1-29", axis: fail-low }
  span: { start: 61580, end: 61859 }
  source: "Little ability to communicate simple concepts and/or factual information. Frequent faults in the presentation of work and significant difficulties in its structure and organisation detract from the clarity and meaning overall. The writing style is often clumsy and inappropriate."
  versionsFrom: none
  spans: "none"
  echoes: none
  force: describes
  paraphrase: "Little communication of simple concepts or facts; frequent faults and weak structure obscure meaning; style often clumsy."   # the whole cell, our words; sentences in AC5a
  sentences: 3
- id: cardiffmet/generic-2020/l6/analysis/80-100
  level: l6
  criterion: "Analysis & discussion"
  band: { label: "80%-100% (1st Class +)", range: "80-100", axis: 80-100 }
  span: { start: 61913, end: 62073 }
  source: "The student demonstrates the ability to design and undertake their own research or advanced scholarship, applying relevant techniques and methods appropriately."
  versionsFrom: none
  spans: "none"
  echoes: none
  force: describes
  paraphrase: "Designs and carries out own research or advanced scholarship with fitting techniques."   # the whole cell, our words; sentences in AC5a
  sentences: 1
- id: cardiffmet/generic-2020/l6/analysis/70-79
  level: l6
  criterion: "Analysis & discussion"
  band: { label: "70%-79% (1st)", range: "70-79", axis: 70-79 }
  span: { start: 62118, end: 62597 }
  source: "An ability to undertake detailed analysis and critical enquiry of qualitative and quantitative data relevant to the task/discipline by making very good use of a number of appropriate techniques. The student is highly successful in presenting, synthesising and commenting on outcomes and is able to comment perceptively and with insight on the relationship between theory and practice and the impact of uncertainty, assumptions and the limits of their knowledge on their findings."
  versionsFrom: none
  spans: "none"
  echoes: none
  force: describes
  paraphrase: "Detailed analysis and critical enquiry of data with very good use of fitting techniques; presents, synthesises and comments very successfully; perceptive on theory, practice, uncertainty, assumptions and the limits of own knowledge."   # the whole cell, our words; sentences in AC5a
  sentences: 2
- id: cardiffmet/generic-2020/l6/analysis/60-69
  level: l6
  criterion: "Analysis & discussion"
  band: { label: "60%-69% (2:1)", range: "60-69", axis: 60-69 }
  span: { start: 62642, end: 63002 }
  source: "An ability to undertake detailed analysis and critical enquiry relevant to the task/discipline by making use of appropriate techniques and has considerable success in presenting, synthesising and commenting on outcomes. There is some linkage between theory and practice and awareness of the impact of uncertainty, assumptions and the limits of their knowledge."
  versionsFrom: none
  spans: "none"
  echoes: none
  force: describes
  paraphrase: "Detailed analysis and critical enquiry with fitting techniques; considerable success with results; some link of theory and practice; aware of uncertainty, assumptions and own limits."   # the whole cell, our words; sentences in AC5a
  sentences: 2
- id: cardiffmet/generic-2020/l6/analysis/50-59
  level: l6
  criterion: "Analysis & discussion"
  band: { label: "50%-59% (2:2)", range: "50-59", axis: 50-59 }
  span: { start: 63047, end: 63299 }
  source: "An ability to utilise some techniques to undertake analysis and enquiry relevant to the task/discipline and generally has success in presenting and commenting on outcomes, with an awareness of uncertainty, assumptions and the limits of their knowledge."
  versionsFrom: none
  spans: "none"
  echoes: none
  force: describes
  paraphrase: "Uses some techniques for analysis and enquiry; generally succeeds with results; aware of uncertainty, assumptions and own limits."   # the whole cell, our words; sentences in AC5a
  sentences: 1
- id: cardiffmet/generic-2020/l6/analysis/40-49
  level: l6
  criterion: "Analysis & discussion"
  band: { label: "40%-49% (3rd)", range: "40-49", axis: 40-49 }
  span: { start: 63344, end: 63598 }
  source: "An ability to undertake some limited analysis and enquiry relevant to the task/discipline and has intermittent success in presenting, synthesising and commenting on outcomes with an awareness of uncertainty, assumptions and the limits of their knowledge."
  versionsFrom: none
  spans: "none"
  echoes: none
  force: describes
  paraphrase: "Some limited analysis and enquiry; intermittent success with results; aware of uncertainty, assumptions and own limits."   # the whole cell, our words; sentences in AC5a
  sentences: 1
- id: cardiffmet/generic-2020/l6/analysis/30-39
  level: l6
  criterion: "Analysis & discussion"
  band: { label: "30-39% (Narrow Fail)", range: "30-39", axis: fail-high }
  span: { start: 63650, end: 63829 }
  source: "Likely to have attempted some enquiry and analysis of qualitative and quantitative data relevant to the task/discipline, but outcomes may be naïve, simplistic and/or unconvincing."
  versionsFrom: none
  spans: "none"
  echoes: none
  force: describes
  paraphrase: "Attempts some enquiry and analysis of data, but results may be naive, simplistic or unconvincing."   # the whole cell, our words; sentences in AC5a
  sentences: 1
- id: cardiffmet/generic-2020/l6/analysis/1-29
  level: l6
  criterion: "Analysis & discussion"
  band: { label: "1-29% (Clear Fail)", range: "1-29", axis: fail-low }
  span: { start: 63879, end: 64090 }
  source: "Little evidence of being able to undertake enquiry and analysis of qualitative and quantitative data relevant to the task/discipline. Where such work has been attempted, outcomes may be inappropriate, or absent."
  versionsFrom: { like: cardiffmet/generic-2020/l5/analysis/1-29, similarity: 0.95 }
  spans: "none"
  echoes: none
  force: describes
  paraphrase: "Little evidence of data analysis; results, where attempted, unsuitable or missing."   # the whole cell, our words; sentences in AC5a
  sentences: 2
- id: cardiffmet/generic-2020/l6/research/80-100
  level: l6
  criterion: "Research / scholarship"
  band: { label: "80%-100% (1st Class +)", range: "80-100", axis: 80-100 }
  span: { start: 64145, end: 64366 }
  source: "In written coursework, reference citations extend significantly beyond the main body of reading normally expected in the discipline/field of study. In examinations, a substantial range of reference citations are included."
  versionsFrom: none
  spans: "none"
  echoes: none
  force: describes
  paraphrase: "Citations range well beyond the reading the field normally expects (coursework), or are substantial (examinations)."   # the whole cell, our words; sentences in AC5a
  sentences: 2
- id: cardiffmet/generic-2020/l6/research/70-79
  level: l6
  criterion: "Research / scholarship"
  band: { label: "70%-79% (1st)", range: "70-79", axis: 70-79 }
  span: { start: 64412, end: 65032 }
  source: "A detailed, thorough knowledge and systematic understanding of current research/advanced scholarship in the discipline. The use of scholarly reviews/primary sources is confident and a breadth and depth of individual reading and investigation, extending beyond the sources provided, is apparent. The referencing of literature and other sources is accurate and in line with academic conventions. A thorough knowledge and understanding of research processes, techniques and methods is demonstrated along with an ability to determine, refine, adapt and use research knowledge and skills successfully in appropriate contexts."
  versionsFrom: none
  spans: "none"
  echoes: none
  force: describes
  paraphrase: "Detailed, thorough, systematic knowledge of current research; confident use of reviews and primary sources; reading beyond the sources given; accurate referencing; determines, refines, adapts and uses research methods successfully."   # the whole cell, our words; sentences in AC5a
  sentences: 4
- id: cardiffmet/generic-2020/l6/research/60-69
  level: l6
  criterion: "Research / scholarship"
  band: { label: "60%-69% (2:1)", range: "60-69", axis: 60-69 }
  span: { start: 65078, end: 65541 }
  source: "A thorough knowledge and understanding of current research/scholarship in the discipline. Examples referred to indicate a breadth and depth of individual reading and investigation that extend beyond the sources provided. The referencing of literature and other sources is almost always accurate. A secure knowledge of research processes is evident along with an ability to determine, refine, adapt and use research skills and knowledge in the appropriate context."
  versionsFrom: none
  spans: "none"
  echoes: none
  force: describes
  paraphrase: "Thorough knowledge of current research; reading beyond the sources given; referencing almost always accurate; secure grasp of research processes, determined, refined, adapted and used fittingly."   # the whole cell, our words; sentences in AC5a
  sentences: 4
- id: cardiffmet/generic-2020/l6/research/50-59
  level: l6
  criterion: "Research / scholarship"
  band: { label: "50%-59% (2:2)", range: "50-59", axis: 50-59 }
  span: { start: 65587, end: 66091 }
  source: "A sound knowledge and understanding of current research/scholarship in the discipline and shows an ability to discuss its implications. Examples of research/scholarship referred to in the work demonstrate individual reading and investigation. Occasional errors may be present in the referencing of literature and other sources. Some knowledge of research processes is evident and the application of research skills and knowledge is generally successful, although there may be a reliance on tutor support."
  versionsFrom: { like: cardiffmet/generic-2020/l5/research/50-59, similarity: 0.97 }
  spans: "none"
  echoes: none
  force: describes
  paraphrase: "Satisfactory knowledge of current research and its implications; own reading; occasional referencing errors; research skills generally applied well, perhaps relying on tutor support."   # the whole cell, our words; sentences in AC5a
  sentences: 4
- id: cardiffmet/generic-2020/l6/research/40-49
  level: l6
  criterion: "Research / scholarship"
  band: { label: "40%-49% (3rd)", range: "40-49", axis: 40-49 }
  span: { start: 66137, end: 66649 }
  source: "Some knowledge and understanding of current research/scholarship in the discipline and demonstrates an ability to provide limited comment and/or discussion of its implications. Examples of research/scholarship referred to in the work may indicate an over-reliance on programme materials rather than individual reading and investigation. There are errors in the referencing of literature and other sources. Some knowledge of research processes is evident although the application of such knowledge is less secure."
  versionsFrom: { like: cardiffmet/generic-2020/l5/research/40-49, similarity: 0.97 }
  spans: "none"
  echoes: none
  force: describes
  paraphrase: "Basic knowledge of current research, with limited comment on its implications; over-reliance on course materials; referencing errors; research processes applied less securely."   # the whole cell, our words; sentences in AC5a
  sentences: 4
- id: cardiffmet/generic-2020/l6/research/30-39
  level: l6
  criterion: "Research / scholarship"
  band: { label: "30-39% (Narrow Fail)", range: "30-39", axis: fail-high }
  span: { start: 66702, end: 67179 }
  source: "Limited or sporadic knowledge and understanding of current research/scholarship in the discipline. A restricted range of sources are used but overall, there is an over-reliance on programme materials with little evidence of individual reading and investigation. There are frequent errors in the referencing of literature and other sources. Although limited knowledge of research processes may be evident, nevertheless, the application of such knowledge is largely unsuccessful."
  versionsFrom: none
  spans: "none"
  echoes: none
  force: describes
  paraphrase: "Limited or patchy knowledge of current research; narrow sources, over-reliance on course materials; frequent referencing errors; research knowledge applied largely without success."   # the whole cell, our words; sentences in AC5a
  sentences: 4
- id: cardiffmet/generic-2020/l6/research/1-29
  level: l6
  criterion: "Research / scholarship"
  band: { label: "1-29% (Clear Fail)", range: "1-29", axis: fail-low }
  span: { start: 67230, end: 67562 }
  source: "Little knowledge and understanding of current research/scholarship in the discipline. Evidence of individual reading and investigation is negligible. Limited referencing of literature and other sources is frequently inaccurate. Very limited knowledge of research processes is apparent and there is a failure to apply this knowledge."
  versionsFrom: none
  spans: "none"
  echoes: none
  force: describes
  paraphrase: "Little knowledge of current research; negligible own reading; referencing scant and often wrong; little grasp or use of research processes."   # the whole cell, our words; sentences in AC5a
  sentences: 4
- id: cardiffmet/generic-2020/l6/argument/80-100
  level: l6
  criterion: "Structured argument and critical evaluation"
  band: { label: "80%-100% (1st Class +)", range: "80-100", axis: 80-100 }
  span: { start: 67638, end: 67900 }
  source: "Work may challenge the boundaries of knowledge within the discipline/field of study and is informed by innovative and/or creative thinking. New insights are offered that are informed by critical evaluation of current research/ scholarship/ professional practice."
  versionsFrom: none
  spans: "none"
  echoes: none
  force: describes
  paraphrase: "May push at the boundaries of knowledge with innovative or creative thinking; new insights informed by critical evaluation of current research, scholarship or practice."   # the whole cell, our words; sentences in AC5a
  sentences: 2
- id: cardiffmet/generic-2020/l6/argument/70-79
  level: l6
  criterion: "Structured argument and critical evaluation"
  band: { label: "70%-79% (1st)", range: "70-79", axis: 70-79 }
  span: { start: 67967, end: 68667 }
  source: "An ability to engage in critical evaluation of concepts/arguments/data and to make appropriate and informed judgements. Arguments are well developed, sustained and substantiated. Where relevant, assumptions are challenged and there is clear recognition of the complexities of academic debate. Appropriate and sometimes innovative solutions are offered to problems that have limited definition and multiple interacting factors. There is strong evidence that the student is able to reflect effectively on the student’s own practice. Critical evaluation of the student’s own work and/or professional practice is highly perceptive and there is a full awareness of the implications for future development."
  versionsFrom: none
  spans: "none"
  echoes: none
  force: describes
  paraphrase: "Critically evaluates concepts, arguments and data and judges in an informed way; well-developed, supported arguments; challenges assumptions; sometimes innovative solutions to ill-defined, many-factor problems; highly perceptive self-evaluation."   # the whole cell, our words; sentences in AC5a
  sentences: 6
- id: cardiffmet/generic-2020/l6/argument/60-69
  level: l6
  criterion: "Structured argument and critical evaluation"
  band: { label: "60%-69% (2:1)", range: "60-69", axis: 60-69 }
  span: { start: 68734, end: 69167 }
  source: "An ability to engage in critical evaluation and reflection. Arguments are clearly considered and substantiated and there is evidence of an ability to make appropriate judgements and to suggest solutions to problems that have limited definition and multiple interacting factors. The student also demonstrates an ability to engage in reflective practice and to take account of personal evaluations when planning for future development."
  versionsFrom: none
  spans: "none"
  echoes: none
  force: describes
  paraphrase: "Critically evaluates and reflects; considered, supported arguments; judges fittingly and suggests solutions to ill-defined, many-factor problems; reflects on own practice to plan development."   # the whole cell, our words; sentences in AC5a
  sentences: 3
- id: cardiffmet/generic-2020/l6/argument/50-59
  level: l6
  criterion: "Structured argument and critical evaluation"
  band: { label: "50%-59% (2:2)", range: "50-59", axis: 50-59 }
  span: { start: 69234, end: 69600 }
  source: "An ability to critically evaluate and reflect although there may be some over-reliance on description and factual presentation. Arguments are usually substantiated. There is some evidence of the student’s ability to evaluate and reflect on the student’s own practice but reflections may lack insight and the implications for future development may be underestimated."
  versionsFrom: none
  spans: "none"
  echoes: none
  force: describes
  paraphrase: "Critically evaluates and reflects, with some leaning on description; arguments usually supported; some reflection on own practice, lacking insight into future development."   # the whole cell, our words; sentences in AC5a
  sentences: 3
- id: cardiffmet/generic-2020/l6/argument/40-49
  level: l6
  criterion: "Structured argument and critical evaluation"
  band: { label: "40%-49% (3rd)", range: "40-49", axis: 40-49 }
  span: { start: 69667, end: 70143 }
  source: "A limited ability to critically evaluate and reflect. Although some critical reflection is evident, the balance within the work is likely to be in favour of description and factual presentation. Arguments are generally substantiated but may be under-developed. There is some evidence of the student’s ability to evaluate and reflect on the student’s own practice. Reflections may be limited and superficial, with little consideration of their relevance for future development."
  versionsFrom: none
  spans: "none"
  echoes: none
  force: describes
  paraphrase: "Limited critical evaluation and reflection; mostly description; arguments generally supported but thin; reflection limited and superficial."   # the whole cell, our words; sentences in AC5a
  sentences: 5
- id: cardiffmet/generic-2020/l6/argument/30-39
  level: l6
  criterion: "Structured argument and critical evaluation"
  band: { label: "30-39% (Narrow Fail)", range: "30-39", axis: fail-high }
  span: { start: 70217, end: 70443 }
  source: "Limited evidence of critical evaluation and reflection. The work is largely descriptive and arguments if attempted, are rarely substantiated. Self-evaluation and reflections on the student’s own practice are extremely limited."
  versionsFrom: none
  spans: "none"
  echoes: none
  force: describes
  paraphrase: "Limited sign of critical evaluation; largely descriptive; arguments rarely supported; self-evaluation very limited."   # the whole cell, our words; sentences in AC5a
  sentences: 3
- id: cardiffmet/generic-2020/l6/argument/1-29
  level: l6
  criterion: "Structured argument and critical evaluation"
  band: { label: "1-29% (Clear Fail)", range: "1-29", axis: fail-low }
  span: { start: 70515, end: 70747 }
  source: "Little ability to describe and report. Very little evidence is available to indicate an ability to engage in critical evaluation and reflection. Self-evaluation and reflections on the student’s own practice are negligible or absent."
  versionsFrom: none
  spans: "none"
  echoes: none
  force: describes
  paraphrase: "Little description or reporting and very little sign of critical evaluation; self-evaluation negligible or absent."   # the whole cell, our words; sentences in AC5a
  sentences: 3
- id: cardiffmet/generic-2020/l7/overall/80-100
  level: l7
  criterion: "Overall summary"
  band: { label: "80%-100% (Distinction+)", range: "80-100", axis: 80-100 }
  span: { start: 70830, end: 71164 }
  source: "A full and detailed understanding of the set task and an ability to have met the learning outcomes and address the assessment criteria at an excellent level (80-89%) or outstanding and exceptional level (90-100%) and beyond level 7. Work is of a standard deemed worthy of publication/manufacture/ public exhibition/public performance."
  versionsFrom: { like: cardiffmet/generic-2020/l6/overall/80-100, similarity: 0.98 }
  spans: "none"
  echoes: none
  force: describes
  paraphrase: "Full, detailed grasp of the task; outcomes met excellently (80-89) or outstandingly (90-100), beyond this level; work of a standard fit for publication, manufacture, exhibition or performance."   # the whole cell, our words; sentences in AC5a
  sentences: 2
- id: cardiffmet/generic-2020/l7/overall/70-79
  level: l7
  criterion: "Overall summary"
  band: { label: "70%-79% (Distinction)", range: "70-79", axis: 70-79 }
  span: { start: 71211, end: 71367 }
  source: "A full and detailed understanding of the set task and an ability to have met the learning outcomes and address the assessment criteria at a very good level."
  versionsFrom: { sameAs: cardiffmet/generic-2020/l3/overall/70-79 }
  spans: "none"
  echoes: none
  force: describes
  paraphrase: "Full, detailed grasp of the task; outcomes met and criteria addressed very well."   # the whole cell, our words; sentences in AC5a
  sentences: 1
- id: cardiffmet/generic-2020/l7/overall/60-69
  level: l7
  criterion: "Overall summary"
  band: { label: "60%-69% (Merit)", range: "60-69", axis: 60-69 }
  span: { start: 71408, end: 71546 }
  source: "A full understanding of the set task and an ability to have met the learning outcomes and address the assessment criteria at a good level."
  versionsFrom: { sameAs: cardiffmet/generic-2020/l3/overall/60-69 }
  spans: "none"
  echoes: none
  force: describes
  paraphrase: "Full grasp of the task; outcomes met and criteria addressed well."   # the whole cell, our words; sentences in AC5a
  sentences: 1
- id: cardiffmet/generic-2020/l7/overall/50-59
  level: l7
  criterion: "Overall summary"
  band: { label: "50%-59% (Pass)", range: "50-59", axis: 50-59 }
  span: { start: 71586, end: 71752 }
  source: "A basic but secure understanding of the set task and an ability to have met the associated learning outcomes and address the assessment criteria at a threshold level."
  versionsFrom: none
  spans: "none"
  echoes: none
  force: describes
  paraphrase: "Basic but secure grasp of the task; outcomes met and criteria addressed at the threshold."   # the whole cell, our words; sentences in AC5a
  sentences: 1
- id: cardiffmet/generic-2020/l7/overall/40-49
  level: l7
  criterion: "Overall summary"
  band: { label: "40%-49% (Narrow Fail)", range: "40-49", axis: 40-49 }
  span: { start: 71799, end: 72103 }
  source: "A partial understanding of the set task and an ability to have met the associated learning outcomes and address the assessment criteria at a limited and insufficient level. Unsatisfactory overall. However, attainment is uneven with some learning outcomes not met and some assessment criteria unaddressed."
  versionsFrom: none
  spans: "none"
  echoes: none
  force: describes
  paraphrase: "Unsatisfactory: partial grasp of the task; outcomes and criteria met at a limited, insufficient level; uneven, some outcomes unmet."   # the whole cell, our words; sentences in AC5a
  sentences: 3
- id: cardiffmet/generic-2020/l7/overall/20-39
  level: l7
  criterion: "Overall summary"
  band: { label: "20-39% (Clear Fail)", range: "20-39", axis: fail-high }
  span: { start: 72148, end: 72370 }
  source: "Unsatisfactory overall. A minimal understanding of the set task and an ability to have met some of the associated learning outcomes at a basic level. However, attainment is uneven with many assessment criteria unaddressed."
  versionsFrom: none
  spans: "none"
  echoes: none
  force: describes
  paraphrase: "Unsatisfactory: minimal grasp; some outcomes met at a basic level; uneven, many criteria unaddressed."   # the whole cell, our words; sentences in AC5a
  sentences: 3
- id: cardiffmet/generic-2020/l7/overall/1-19
  level: l7
  criterion: "Overall summary"
  band: { label: "1-19%", range: "1-19", axis: fail-low }
  span: { start: 72401, end: 72660 }
  source: "Very poor, incomplete and/or irrelevant. Demonstrates a serious lack of comprehension and/or engagement with the set task. May have misunderstood the set task. No learning outcomes are met in full, although there may be minimal attainment in one or two areas."
  versionsFrom: none
  spans: "none"
  echoes: none
  force: describes
  paraphrase: "Very poor, incomplete or irrelevant; serious lack of comprehension or engagement, perhaps a misreading of the task; no outcome met in full."   # the whole cell, our words; sentences in AC5a
  sentences: 4
- id: cardiffmet/generic-2020/l7/knowledge/80-100
  level: l7
  criterion: "Knowledge & Understanding"
  band: { label: "80%-100% (Distinction+)", range: "80-100", axis: 80-100 }
  span: { start: 72719, end: 72918 }
  source: "Further to the 70%-79% band, academic work in the 80%-100% bands is beyond the expectation of that expected at level 7. Demonstrates exceptional mastery of a complex and specialist area of knowledge."
  versionsFrom: none
  spans: "none"
  echoes: none
  force: describes
  paraphrase: "Beyond what this level expects: exceptional mastery of a complex, specialist area."   # the whole cell, our words; sentences in AC5a
  sentences: 2
- id: cardiffmet/generic-2020/l7/knowledge/70-79
  level: l7
  criterion: "Knowledge & Understanding"
  band: { label: "70%-79% (Distinction)", range: "70-79", axis: 70-79 }
  span: { start: 72975, end: 73397 }
  source: "Demonstrates mastery of a complex and specialised area of knowledge. There is strong evidence of an ability to extend, transform and apply such knowledge. The student also demonstrates an ability to engage in sophisticated discussion of complex concepts and to recognise the limitations and/or ambiguity of disciplinary knowledge. Independent thinking and action. Original insights are also features of work at this level."
  versionsFrom: none
  spans: "none"
  echoes: none
  force: describes
  paraphrase: "Mastery of a complex, specialised area, strongly extended and applied; sophisticated discussion of complex concepts; recognises limits of knowledge; independent thought and action; original insight."   # the whole cell, our words; sentences in AC5a
  sentences: 5
- id: cardiffmet/generic-2020/l7/knowledge/60-69
  level: l7
  criterion: "Knowledge & Understanding"
  band: { label: "60%-69% (Merit)", range: "60-69", axis: 60-69 }
  span: { start: 73448, end: 73760 }
  source: "Demonstrates mastery of a complex and specialised area of knowledge. There is clear evidence of an ability to apply such knowledge within familiar contexts, to extend and transform it. The discussion of complex concepts is often tackled successfully and there is some evidence of independent thinking and action."
  versionsFrom: none
  spans: "none"
  echoes: none
  force: describes
  paraphrase: "Mastery of a complex, specialised area, applied in familiar contexts and extended; complex concepts often discussed well; some independent thought and action."   # the whole cell, our words; sentences in AC5a
  sentences: 3
- id: cardiffmet/generic-2020/l7/knowledge/50-59
  level: l7
  criterion: "Knowledge & Understanding"
  band: { label: "50%-59% (Pass)", range: "50-59", axis: 50-59 }
  span: { start: 73810, end: 73998 }
  source: "Demonstrates mastery of a complex and specialised area of knowledge, but is frequently descriptive and based on given sources. There is limited evidence of independent thinking and action."
  versionsFrom: none
  spans: "none"
  echoes: none
  force: describes
  paraphrase: "Mastery of a complex, specialised area, but often descriptive and tied to given sources; limited independent thought."   # the whole cell, our words; sentences in AC5a
  sentences: 2
- id: cardiffmet/generic-2020/l7/knowledge/40-49
  level: l7
  criterion: "Knowledge & Understanding"
  band: { label: "40%-49% (Narrow Fail)", range: "40-49", axis: 40-49 }
  span: { start: 74055, end: 74278 }
  source: "Limited knowledge and understanding of the field of study relevant to the task. Factual inaccuracies, errors and misconceptions are evident in important areas and elements of the assessed work may be irrelevant to the task."
  versionsFrom: { sameAs: cardiffmet/generic-2020/l3/knowledge/30-39 }
  spans: "none"
  echoes: none
  force: describes
  paraphrase: "Limited knowledge of the field; inaccuracies and misconceptions in important areas; parts of the work off the task."   # the whole cell, our words; sentences in AC5a
  sentences: 2
- id: cardiffmet/generic-2020/l7/knowledge/20-39
  level: l7
  criterion: "Knowledge & Understanding"
  band: { label: "20-39% (Clear Fail)", range: "20-39", axis: fail-high }
  span: { start: 74333, end: 74643 }
  source: "Little knowledge and understanding of the field of study relevant to the task. Factual inaccuracies, errors and misconceptions are evident in many important areas and these outweigh the degree of knowledge and understanding demonstrated. Substantial elements of the assessed work may be irrelevant to the task."
  versionsFrom: { sameAs: cardiffmet/generic-2020/l3/knowledge/1-29 }
  spans: "none"
  echoes: none
  force: describes
  paraphrase: "Little knowledge of the field; errors in many important areas outweigh what is understood; much of the work off the task."   # the whole cell, our words; sentences in AC5a
  sentences: 3
- id: cardiffmet/generic-2020/l7/knowledge/1-19
  level: l7
  criterion: "Knowledge & Understanding"
  band: { label: "1-19%", range: "1-19", axis: fail-low }
  span: { start: 74684, end: 74986 }
  source: "Work may be: short irrelevant contain serious/numerous errors and misunderstandings no evidence of analysis, synthesis, critical evaluation and reflection no reference/minimal reference to external sources very poor presentation and inappropriate format very poor communication of information and ideas"
  versionsFrom: none
  spans: "band"
  echoes: none
  force: describes
  paraphrase: "Band-wide: work may be short or irrelevant, with serious errors; no analysis, synthesis, evaluation or reflection; little or no use of sources; very poor presentation and communication."   # the whole cell, our words; sentences in AC5a
  sentences: 1
- id: cardiffmet/generic-2020/l7/presentation/80-100
  level: l7
  criterion: "Presentation and communication"
  band: { label: "80%-100% (Distinction+)", range: "80-100", axis: 80-100 }
  span: { start: 75050, end: 75294 }
  source: "Further to the 70% – 79% band, academic work in the 80% - 100% provides consistently convincing and succinct arguments in all areas. The standard of presentation shows an enhanced ability to communicate using an eloquent and professional style."
  versionsFrom: none
  spans: "none"
  echoes: none
  force: describes
  paraphrase: "Beyond 70-79: consistently convincing, concise arguments throughout; eloquent, professional style."   # the whole cell, our words; sentences in AC5a
  sentences: 2
- id: cardiffmet/generic-2020/l7/presentation/70-79
  level: l7
  criterion: "Presentation and communication"
  band: { label: "70%-79% (Distinction)", range: "70-79", axis: 70-79 }
  span: { start: 75356, end: 75707 }
  source: "An ability to communicate information, complex ideas, results of research and concepts in a coherent and succinct manner, in a range of situations. The standard of presentation is high and the format appropriate. Key points are logically organised and in written work, the style is lucid and mature. Arguments are well-defined and clearly articulated."
  versionsFrom: { like: cardiffmet/generic-2020/l6/presentation/70-79, similarity: 0.97 }
  spans: "none"
  echoes: none
  force: describes
  paraphrase: "Communicates information and complex ideas coherently and concisely in many situations; high standard of presentation; logical, lucid, mature style; clear arguments."   # the whole cell, our words; sentences in AC5a
  sentences: 4
- id: cardiffmet/generic-2020/l7/presentation/60-69
  level: l7
  criterion: "Presentation and communication"
  band: { label: "60%-69% (Merit)", range: "60-69", axis: 60-69 }
  span: { start: 75763, end: 76025 }
  source: "An ability to communicate information, results of research, ideas and concepts clearly and succinctly in a range of situations. Work is well presented and the format appropriate. Key points are appropriately organised, fluently conveyed and are well articulated."
  versionsFrom: none
  spans: "none"
  echoes: none
  force: describes
  paraphrase: "Communicates information, research results and ideas clearly and concisely in many situations; well presented; points organised, fluent and well put."   # the whole cell, our words; sentences in AC5a
  sentences: 3
- id: cardiffmet/generic-2020/l7/presentation/50-59
  level: l7
  criterion: "Presentation and communication"
  band: { label: "50%-59% (Pass)", range: "50-59", axis: 50-59 }
  span: { start: 76080, end: 76442 }
  source: "Satisfactory ability to communicate information, results of research, ideas, concepts and arguments satisfactorily in familiar situations. Some aspects of the task lack academic rigour and rely on describing and reporting factual information rather than communicating complex ideas. Generally, the work is appropriately structured but may not always be coherent."
  versionsFrom: none
  spans: "none"
  echoes: none
  force: describes
  paraphrase: "Satisfactory communication of research results and ideas in familiar situations; some lack of rigour, leaning on description; mostly structured, not always coherent."   # the whole cell, our words; sentences in AC5a
  sentences: 3
- id: cardiffmet/generic-2020/l7/presentation/40-49
  level: l7
  criterion: "Presentation and communication"
  band: { label: "40%-49% (Narrow Fail)", range: "40-49", axis: 40-49 }
  span: { start: 76504, end: 76778 }
  source: "An ability to communicate some simple concepts and/or factual information. Ideas may not be communicated clearly and present comprehension difficulties for the reader. If attempted, the presentation of arguments and more complex ideas may be confused and clumsily expressed."
  versionsFrom: none
  spans: "none"
  echoes: none
  force: describes
  paraphrase: "Communicates some simple concepts or facts; ideas unclear and hard to follow; arguments and complex ideas, if tried, confused."   # the whole cell, our words; sentences in AC5a
  sentences: 3
- id: cardiffmet/generic-2020/l7/presentation/20-39
  level: l7
  criterion: "Presentation and communication"
  band: { label: "20-39% (Clear Fail)", range: "20-39", axis: fail-high }
  span: { start: 76838, end: 77118 }
  source: "Limited ability to communicate simple concepts and/or factual information. Frequent faults in the presentation of work and significant difficulties in its structure and organisation detract from the clarity and meaning overall. The writing style is often clumsy and inappropriate."
  versionsFrom: none
  spans: "none"
  echoes: none
  force: describes
  paraphrase: "Limited communication of simple concepts or facts; frequent faults and weak structure obscure meaning; style often clumsy."   # the whole cell, our words; sentences in AC5a
  sentences: 3
- id: cardiffmet/generic-2020/l7/presentation/1-19
  level: l7
  criterion: "Presentation and communication"
  band: { label: "1-19%", range: "1-19", axis: fail-low }
  span: { start: 77164, end: 77242 }
  source: "(empty cell: the band-wide descriptor is in the Knowledge & Understanding row)"
  versionsFrom: none
  spans: "merged into cardiffmet/generic-2020/l7/knowledge/1-19"
  echoes: none
  force: describes
  paraphrase: none   # the whole cell, our words; sentences in AC5a
  sentences: 0
- id: cardiffmet/generic-2020/l7/analysis/80-100
  level: l7
  criterion: "Analysis & discussion"
  band: { label: "80%-100% (Distinction+)", range: "80-100", axis: 80-100 }
  span: { start: 77297, end: 77507 }
  source: "The students demonstrates the ability to design and undertake their own extensive and independent inquiry applying advanced concepts, methods or techniques consistently to solve problems in unfamiliar contexts."
  versionsFrom: none
  spans: "none"
  echoes: none
  force: describes
  paraphrase: "Designs and carries out own extensive, independent inquiry, applying advanced concepts and methods consistently to problems in unfamiliar contexts."   # the whole cell, our words; sentences in AC5a
  sentences: 1
- id: cardiffmet/generic-2020/l7/analysis/70-79
  level: l7
  criterion: "Analysis & discussion"
  band: { label: "70%-79% (Distinction)", range: "70-79", axis: 70-79 }
  span: { start: 77560, end: 78090 }
  source: "An ability to conduct research or advanced technical or professional activity, undertake detailed analysis and critical enquiry relevant to the task/discipline and expertise in highly specialised and advanced technical, professional and/or research skills, by making excellent use of a number of appropriate techniques. The student is highly successful in presenting, synthesising and commenting on research process and outcomes and is able to comment perceptively and with insight on the relationship between theory and practice."
  versionsFrom: none
  spans: "none"
  echoes: none
  force: describes
  paraphrase: "Conducts research or advanced professional activity; detailed analysis and critical enquiry; expertise in highly specialised skills with excellent use of techniques; very successful synthesis and comment; perceptive on theory and practice."   # the whole cell, our words; sentences in AC5a
  sentences: 2
- id: cardiffmet/generic-2020/l7/analysis/60-69
  level: l7
  criterion: "Analysis & discussion"
  band: { label: "60%-69% (Merit)", range: "60-69", axis: 60-69 }
  span: { start: 78137, end: 78580 }
  source: "An ability to conduct research or advanced technical or professional activity, undertake some detailed analysis and critical enquiry relevant to the task/discipline and expertise in highly specialised and advanced technical, professional and/or research skills, by making use of appropriate techniques and has considerable success in presenting and commenting on research process and outcomes. There is some linkage between theory and practice"
  versionsFrom: none
  spans: "none"
  echoes: none
  force: describes
  paraphrase: "Conducts research or advanced professional activity; some detailed analysis and critical enquiry; specialised expertise with fitting techniques; considerable success with process and results; some link of theory and practice."   # the whole cell, our words; sentences in AC5a
  sentences: 2
- id: cardiffmet/generic-2020/l7/analysis/50-59
  level: l7
  criterion: "Analysis & discussion"
  band: { label: "50%-59% (Pass)", range: "50-59", axis: 50-59 }
  span: { start: 78626, end: 78963 }
  source: "An ability to conduct research or advanced technical or professional activity and undertake some limited analysis and enquiry relevant to the task/discipline and expertise in highly specialised and advanced technical, professional and/or research skills and has some success in presenting and commenting on research process and outcomes."
  versionsFrom: none
  spans: "none"
  echoes: none
  force: describes
  paraphrase: "Conducts research or advanced professional activity; some limited analysis and enquiry; specialised expertise; some success with process and results."   # the whole cell, our words; sentences in AC5a
  sentences: 1
- id: cardiffmet/generic-2020/l7/analysis/40-49
  level: l7
  criterion: "Analysis & discussion"
  band: { label: "40%-49% (Narrow Fail)", range: "40-49", axis: 40-49 }
  span: { start: 79016, end: 79178 }
  source: "Likely to have attempted some enquiry and analysis relevant to the task/discipline but research process and outcomes may be naïve, simplistic and/or unconvincing."
  versionsFrom: none
  spans: "none"
  echoes: none
  force: describes
  paraphrase: "Attempts some enquiry and analysis, but process and results may be naive, simplistic or unconvincing."   # the whole cell, our words; sentences in AC5a
  sentences: 1
- id: cardiffmet/generic-2020/l7/analysis/20-39
  level: l7
  criterion: "Analysis & discussion"
  band: { label: "20-39% (Clear Fail)", range: "20-39", axis: fail-high }
  span: { start: 79229, end: 79424 }
  source: "Little evidence of being able to undertake enquiry and analysis relevant to the task/discipline. Where such work has been attempted, research process and outcomes may be inappropriate, or absent."
  versionsFrom: none
  spans: "none"
  echoes: none
  force: describes
  paraphrase: "Little sign of enquiry or analysis; process and results, where attempted, unsuitable or missing."   # the whole cell, our words; sentences in AC5a
  sentences: 2
- id: cardiffmet/generic-2020/l7/analysis/1-19
  level: l7
  criterion: "Analysis & discussion"
  band: { label: "1-19%", range: "1-19", axis: fail-low }
  span: { start: 79461, end: 79539 }
  source: "(empty cell: the band-wide descriptor is in the Knowledge & Understanding row)"
  versionsFrom: { sameAs: cardiffmet/generic-2020/l7/presentation/1-19 }
  spans: "merged into cardiffmet/generic-2020/l7/knowledge/1-19"
  echoes: none
  force: describes
  paraphrase: none   # the whole cell, our words; sentences in AC5a
  sentences: 0
- id: cardiffmet/generic-2020/l7/research/80-100
  level: l7
  criterion: "Research / scholarship"
  band: { label: "80%-100% (Distinction+)", range: "80-100", axis: 80-100 }
  span: { start: 79595, end: 80009 }
  source: "Exceptional breadth and depth of knowledge and understanding evidenced by the student’s own independent insight and critical awareness of relevant literature at the forefront of the discipline. In written coursework, reference citations extend significantly beyond the main body of reading normally expected in the discipline/field of study. In examinations a substantial range of reference citations are included."
  versionsFrom: none
  spans: "none"
  echoes: { statement: qaa/fheq-2024/annex-d/knowledge/r1/2.1, words: 7 }
  force: describes
  paraphrase: "Exceptional breadth and depth shown by independent insight and critical awareness of literature at the forefront; citations well beyond normal reading (coursework) or substantial (examinations)."   # the whole cell, our words; sentences in AC5a
  sentences: 3
- id: cardiffmet/generic-2020/l7/research/70-79
  level: l7
  criterion: "Research / scholarship"
  band: { label: "70%-79% (Distinction)", range: "70-79", axis: 70-79 }
  span: { start: 80063, end: 80709 }
  source: "A detailed and thorough knowledge and understanding of current research/advanced scholarship in the discipline. The use of scholarly reviews/primary sources is sophisticated and a breadth and depth of individual reading and investigation extending beyond the sources provided, is apparent. The referencing of literature and other sources is accurate and in line with academic conventions. A thorough knowledge and understanding of research processes, techniques and methods, is demonstrated along with an ability to design and apply appropriate research methodologies. Can apply research knowledge and skills successfully in appropriate contexts."
  versionsFrom: none
  spans: "none"
  echoes: none
  force: describes
  paraphrase: "Detailed, thorough knowledge of current research; sophisticated use of reviews and primary sources; reading beyond the sources given; accurate referencing; designs and applies fitting methodologies successfully."   # the whole cell, our words; sentences in AC5a
  sentences: 5
- id: cardiffmet/generic-2020/l7/research/60-69
  level: l7
  criterion: "Research / scholarship"
  band: { label: "60%-69% (Merit)", range: "60-69", axis: 60-69 }
  span: { start: 80757, end: 81248 }
  source: "A thorough knowledge and understanding of current research/scholarship in the discipline. Examples referred to indicate a breadth and depth of individual reading and investigation that extends beyond the sources provided. The referencing of literature and other sources is almost always accurate. A secure knowledge of research processes is evident along with an ability to design and apply appropriate research methodologies. Can apply research skills and knowledge in appropriate contexts."
  versionsFrom: none
  spans: "none"
  echoes: none
  force: describes
  paraphrase: "Thorough knowledge of current research; reading beyond the sources given; referencing almost always accurate; secure grasp of research processes; designs and applies fitting methodologies."   # the whole cell, our words; sentences in AC5a
  sentences: 5
- id: cardiffmet/generic-2020/l7/research/50-59
  level: l7
  criterion: "Research / scholarship"
  band: { label: "50%-59% (Pass)", range: "50-59", axis: 50-59 }
  span: { start: 81295, end: 81651 }
  source: "Demonstrates knowledge and understanding of current research/scholarship in the discipline and an ability to provide some comment and/or discussion of its implications. Examples of research/scholarship referred to in the work may indicate an over-reliance on given sources to advance work/direct arguments, rather than individual reading and investigation."
  versionsFrom: none
  spans: "none"
  echoes: none
  force: describes
  paraphrase: "Knows current research and comments on its implications to some degree; may rely on given sources rather than own reading to advance the work."   # the whole cell, our words; sentences in AC5a
  sentences: 2
- id: cardiffmet/generic-2020/l7/research/40-49
  level: l7
  criterion: "Research / scholarship"
  band: { label: "40%-49% (Narrow Fail)", range: "40-49", axis: 40-49 }
  span: { start: 81705, end: 82232 }
  source: "Limited or sporadic knowledge and understanding of current research/scholarship in the discipline. A restricted range of sources are used, but overall there is an over-reliance on programme materials with little evidence of individual reading and investigation. There are frequent errors in the referencing of literature and other sources. Inconsistent application of academic conventions. Although limited knowledge of research processes may be evident, nevertheless, the application of such knowledge is largely unsuccessful."
  versionsFrom: none
  spans: "none"
  echoes: none
  force: describes
  paraphrase: "Limited or patchy knowledge of current research; narrow sources, over-reliance on course materials; frequent referencing errors; conventions applied inconsistently; research knowledge applied largely without success."   # the whole cell, our words; sentences in AC5a
  sentences: 5
- id: cardiffmet/generic-2020/l7/research/20-39
  level: l7
  criterion: "Research / scholarship"
  band: { label: "20-39% (Clear Fail)", range: "20-39", axis: fail-high }
  span: { start: 82284, end: 82623 }
  source: "Little knowledge and understanding of current research/scholarship in the discipline. Evidence of individual reading and investigation is negligible and the limited referencing of literature and other sources is frequently inaccurate. Very limited knowledge of research processes is apparent and there is a failure to apply this knowledge."
  versionsFrom: none
  spans: "none"
  echoes: none
  force: describes
  paraphrase: "Little knowledge of current research; negligible own reading; referencing scant and often wrong; little grasp or use of research processes."   # the whole cell, our words; sentences in AC5a
  sentences: 3
- id: cardiffmet/generic-2020/l7/research/1-19
  level: l7
  criterion: "Research / scholarship"
  band: { label: "1-19%", range: "1-19", axis: fail-low }
  span: { start: 82661, end: 82739 }
  source: "(empty cell: the band-wide descriptor is in the Knowledge & Understanding row)"
  versionsFrom: { sameAs: cardiffmet/generic-2020/l7/presentation/1-19 }
  spans: "merged into cardiffmet/generic-2020/l7/knowledge/1-19"
  echoes: none
  force: describes
  paraphrase: none   # the whole cell, our words; sentences in AC5a
  sentences: 0
- id: cardiffmet/generic-2020/l7/argument/80-100
  level: l7
  criterion: "Structured argument and critical evaluation"
  band: { label: "80%-100% (Distinction+)", range: "80-100", axis: 80-100 }
  span: { start: 82816, end: 83078 }
  source: "Work may challenge the boundaries of knowledge within the discipline/field of study and is informed by innovative and/or creative thinking. New insights are offered that are informed by critical evaluation of current research/ scholarship/ professional practice."
  versionsFrom: { sameAs: cardiffmet/generic-2020/l6/argument/80-100 }
  spans: "none"
  echoes: none
  force: describes
  paraphrase: "May push at the boundaries of knowledge with innovative or creative thinking; new insights informed by critical evaluation of current research, scholarship or practice."   # the whole cell, our words; sentences in AC5a
  sentences: 2
- id: cardiffmet/generic-2020/l7/argument/70-79
  level: l7
  criterion: "Structured argument and critical evaluation"
  band: { label: "70%-79% (Distinction)", range: "70-79", axis: 70-79 }
  span: { start: 83153, end: 83824 }
  source: "An ability to engage in critical evaluation of concepts/arguments/data and to make appropriate and informed judgements where there are many interacting factors. Arguments are well developed, sustained and substantiated. Where relevant, assumptions are challenged and there is clear recognition of the complexities of academic debate. Appropriate and sometimes innovative solutions are offered to problems. There is strong evidence that the student is able to reflect effectively on their own practice. Critical evaluation of the student’s own work and/or professional practice is highly perceptive and there is a full awareness of the implications for future development."
  versionsFrom: none
  spans: "none"
  echoes: none
  force: describes
  paraphrase: "Critically evaluates concepts, arguments and data and judges in an informed way among many interacting factors; well-developed, supported arguments; challenges assumptions; sometimes innovative solutions; highly perceptive self-evaluation."   # the whole cell, our words; sentences in AC5a
  sentences: 6
- id: cardiffmet/generic-2020/l7/argument/60-69
  level: l7
  criterion: "Structured argument and critical evaluation"
  band: { label: "60%-69% (Merit)", range: "60-69", axis: 60-69 }
  span: { start: 83893, end: 84305 }
  source: "An ability to engage in critical evaluation and reflection. Arguments are clearly considered and substantiated and there is evidence of an ability to make appropriate judgements where there are many interacting factors and to suggest solutions to problems. The student also demonstrates an ability to engage in reflective practice and to take account of personal evaluations when planning for future development."
  versionsFrom: none
  spans: "none"
  echoes: none
  force: describes
  paraphrase: "Critically evaluates and reflects; considered, supported arguments; judges fittingly among many interacting factors and suggests solutions; reflects on own practice to plan development."   # the whole cell, our words; sentences in AC5a
  sentences: 3
- id: cardiffmet/generic-2020/l7/argument/50-59
  level: l7
  criterion: "Structured argument and critical evaluation"
  band: { label: "50%-59% (Pass)", range: "50-59", axis: 50-59 }
  span: { start: 84373, end: 84848 }
  source: "A limited ability to critically evaluate and reflect. Although some critical reflection is evident, the balance within the work is likely to be in favour of description and factual presentation. Arguments are generally substantiated but may be under-developed. There is some evidence of the student’s ability to evaluate and reflect on their own practice although reflections may be limited and superficial with little consideration of their relevance for future development."
  versionsFrom: none
  spans: "none"
  echoes: none
  force: describes
  paraphrase: "Limited critical evaluation and reflection; some critical reflection but mostly description; arguments generally supported but thin; reflection limited and superficial."   # the whole cell, our words; sentences in AC5a
  sentences: 4
- id: cardiffmet/generic-2020/l7/argument/40-49
  level: l7
  criterion: "Structured argument and critical evaluation"
  band: { label: "40%-49% (Narrow Fail)", range: "40-49", axis: 40-49 }
  span: { start: 84923, end: 85149 }
  source: "Little evidence of critical evaluation and reflection. The work is largely descriptive and arguments, if attempted, are rarely substantiated. Self-evaluation and reflections on the student’s own practice are extremely limited."
  versionsFrom: none
  spans: "none"
  echoes: none
  force: describes
  paraphrase: "Little sign of critical evaluation; largely descriptive; arguments rarely supported; self-evaluation very limited."   # the whole cell, our words; sentences in AC5a
  sentences: 3
- id: cardiffmet/generic-2020/l7/argument/20-39
  level: l7
  criterion: "Structured argument and critical evaluation"
  band: { label: "20-39% (Clear Fail)", range: "20-39", axis: fail-high }
  span: { start: 85222, end: 85455 }
  source: "Some ability to describe and report but very little evidence is available to indicate an ability to engage in critical evaluation and reflection. Self-evaluation and reflections on the student’s own practice are negligible or absent."
  versionsFrom: none
  spans: "none"
  echoes: none
  force: describes
  paraphrase: "Some description and reporting, but very little sign of critical evaluation; self-evaluation negligible or absent."   # the whole cell, our words; sentences in AC5a
  sentences: 2
- id: cardiffmet/generic-2020/l7/argument/1-19
  level: l7
  criterion: "Structured argument and critical evaluation"
  band: { label: "1-19%", range: "1-19", axis: fail-low }
  span: { start: 85514, end: 85592 }
  source: "(empty cell: the band-wide descriptor is in the Knowledge & Understanding row)"
  versionsFrom: { sameAs: cardiffmet/generic-2020/l7/presentation/1-19 }
  spans: "merged into cardiffmet/generic-2020/l7/knowledge/1-19"
  echoes: none
  force: describes
  paraphrase: none   # the whole cell, our words; sentences in AC5a
  sentences: 0
```

### AC5a Sentences
<!-- The cut (Abbott, 05:18, "1 Yes"; D-std-0008): each cell is cut into its sentences, each a record pointing into the held text, with its own terms and versions. `versionsFrom`: `sameAs` an identical sentence anywhere earlier, or `like` the same criterion and band at an earlier level at word similarity 0.95 or more. -->
```yaml
- id: cardiffmet/generic-2020/l3/overall/80-100.s1
  cell: cardiffmet/generic-2020/l3/overall/80-100
  span: { start: 8020, end: 8252 }
  source: "A full and detailed understanding of the set task and an ability to have met the learning outcomes and address the assessment criteria at an excellent level (80-89%) or outstanding and exceptional level (90-100%) and beyond level 3."
  versionsFrom: none
  echoes: none
  force: describes
  terms:
    verbs: [{ lemma: "address", form: "address", taxonomy: ["none"] }, { lemma: "meet", form: "met", taxonomy: ["none"] }]
    objects: ["understanding", "set task", "learning outcomes", "assessment criteria"]
    degree: ["detailed", "excellent", "outstanding", "exceptional"]
    independence: []
    scope: ["beyond level"]
    deficits: []
- id: cardiffmet/generic-2020/l3/overall/70-79.s1
  cell: cardiffmet/generic-2020/l3/overall/70-79
  span: { start: 8291, end: 8447 }
  source: "A full and detailed understanding of the set task and an ability to have met the learning outcomes and address the assessment criteria at a very good level."
  versionsFrom: none
  echoes: none
  force: describes
  terms:
    verbs: [{ lemma: "address", form: "address", taxonomy: ["none"] }, { lemma: "meet", form: "met", taxonomy: ["none"] }]
    objects: ["understanding", "set task", "learning outcomes", "assessment criteria"]
    degree: ["detailed", "very good"]
    independence: []
    scope: []
    deficits: []
- id: cardiffmet/generic-2020/l3/overall/60-69.s1
  cell: cardiffmet/generic-2020/l3/overall/60-69
  span: { start: 8486, end: 8624 }
  source: "A full understanding of the set task and an ability to have met the learning outcomes and address the assessment criteria at a good level."
  versionsFrom: none
  echoes: none
  force: describes
  terms:
    verbs: [{ lemma: "address", form: "address", taxonomy: ["none"] }, { lemma: "meet", form: "met", taxonomy: ["none"] }]
    objects: ["understanding", "set task", "learning outcomes", "assessment criteria"]
    degree: ["good"]
    independence: []
    scope: []
    deficits: []
- id: cardiffmet/generic-2020/l3/overall/50-59.s1
  cell: cardiffmet/generic-2020/l3/overall/50-59
  span: { start: 8663, end: 8822 }
  source: "A secure understanding of the set task and an ability to have met the associated learning outcomes and address the assessment criteria at a satisfactory level."
  versionsFrom: none
  echoes: none
  force: describes
  terms:
    verbs: [{ lemma: "address", form: "address", taxonomy: ["none"] }, { lemma: "meet", form: "met", taxonomy: ["none"] }]
    objects: ["understanding", "set task", "learning outcomes", "assessment criteria"]
    degree: ["secure", "satisfactory"]
    independence: []
    scope: []
    deficits: []
- id: cardiffmet/generic-2020/l3/overall/40-49.s1
  cell: cardiffmet/generic-2020/l3/overall/40-49
  span: { start: 8861, end: 9016 }
  source: "A basic understanding of the set task and an ability to have met the associated learning outcomes and address the assessment criteria at a threshold level."
  versionsFrom: none
  echoes: none
  force: describes
  terms:
    verbs: [{ lemma: "address", form: "address", taxonomy: ["none"] }, { lemma: "meet", form: "met", taxonomy: ["none"] }]
    objects: ["understanding", "set task", "learning outcomes", "assessment criteria"]
    degree: ["basic"]
    independence: []
    scope: ["basic"]
    deficits: []
- id: cardiffmet/generic-2020/l3/overall/30-39.s1
  cell: cardiffmet/generic-2020/l3/overall/30-39
  span: { start: 9062, end: 9085 }
  source: "Unsatisfactory overall."
  versionsFrom: none
  echoes: none
  force: describes
  terms:
    verbs: []
    objects: []
    degree: []
    independence: []
    scope: []
    deficits: []
- id: cardiffmet/generic-2020/l3/overall/30-39.s2
  cell: cardiffmet/generic-2020/l3/overall/30-39
  span: { start: 9086, end: 9211 }
  source: "A partial understanding of the set task and an ability to have met some of the associated learning outcomes at a basic level."
  versionsFrom: none
  echoes: none
  force: describes
  terms:
    verbs: [{ lemma: "meet", form: "met", taxonomy: ["none"] }]
    objects: ["understanding", "set task", "learning outcomes"]
    degree: ["some", "basic"]
    independence: []
    scope: ["basic"]
    deficits: []
- id: cardiffmet/generic-2020/l3/overall/30-39.s3
  cell: cardiffmet/generic-2020/l3/overall/30-39
  span: { start: 9212, end: 9323 }
  source: "However, attainment is uneven with some learning outcomes not met and some assessment criteria are unaddressed."
  versionsFrom: none
  echoes: none
  force: describes
  terms:
    verbs: [{ lemma: "meet", form: "met", taxonomy: ["none"] }]
    objects: ["learning outcomes", "assessment criteria"]
    degree: ["some", "some"]
    independence: []
    scope: []
    deficits: ["not", "unaddressed"]
- id: cardiffmet/generic-2020/l3/overall/1-29.s1
  cell: cardiffmet/generic-2020/l3/overall/1-29
  span: { start: 9367, end: 9380 }
  source: "Poor overall."
  versionsFrom: none
  echoes: none
  force: describes
  terms:
    verbs: []
    objects: []
    degree: ["poor"]
    independence: []
    scope: []
    deficits: []
- id: cardiffmet/generic-2020/l3/overall/1-29.s2
  cell: cardiffmet/generic-2020/l3/overall/1-29
  span: { start: 9381, end: 9419 }
  source: "Minimal understanding of the set task."
  versionsFrom: none
  echoes: none
  force: describes
  terms:
    verbs: []
    objects: ["understanding", "set task"]
    degree: ["minimal"]
    independence: []
    scope: []
    deficits: []
- id: cardiffmet/generic-2020/l3/overall/1-29.s3
  cell: cardiffmet/generic-2020/l3/overall/1-29
  span: { start: 9420, end: 9492 }
  source: "Has partially met one or two learning outcomes, or no learning outcomes."
  versionsFrom: none
  echoes: none
  force: describes
  terms:
    verbs: [{ lemma: "meet", form: "met", taxonomy: ["none"] }]
    objects: ["learning outcomes", "learning outcomes"]
    degree: []
    independence: []
    scope: []
    deficits: ["no"]
- id: cardiffmet/generic-2020/l3/overall/1-29.s4
  cell: cardiffmet/generic-2020/l3/overall/1-29
  span: { start: 9493, end: 9534 }
  source: "Many assessment criteria are unaddressed."
  versionsFrom: none
  echoes: none
  force: describes
  terms:
    verbs: []
    objects: ["assessment criteria"]
    degree: []
    independence: []
    scope: []
    deficits: ["unaddressed"]
- id: cardiffmet/generic-2020/l3/knowledge/80-100.s1
  cell: cardiffmet/generic-2020/l3/knowledge/80-100
  span: { start: 9592, end: 9693 }
  source: "Further to the 70%-79% band, work in the 80%-100% bands would extend beyond that expected at Level 3."
  versionsFrom: none
  echoes: none
  force: describes
  terms:
    verbs: [{ lemma: "extend", form: "extend", taxonomy: ["bloom-r:understand"] }]
    objects: []
    degree: []
    independence: []
    scope: []
    deficits: []
- id: cardiffmet/generic-2020/l3/knowledge/70-79.s1
  cell: cardiffmet/generic-2020/l3/knowledge/70-79
  span: { start: 9742, end: 9822 }
  source: "May demonstrate a detailed knowledge of the field of study relevant to the task."
  versionsFrom: none
  echoes: none
  force: describes
  terms:
    verbs: [{ lemma: "demonstrate", form: "demonstrate", taxonomy: ["bloom-r:apply/understand"] }]
    objects: ["knowledge", "field of study"]
    degree: ["detailed"]
    independence: []
    scope: []
    deficits: []
- id: cardiffmet/generic-2020/l3/knowledge/70-79.s2
  cell: cardiffmet/generic-2020/l3/knowledge/70-79
  span: { start: 9823, end: 9886 }
  source: "There is strong evidence of an ability to apply such knowledge."
  versionsFrom: none
  echoes: none
  force: describes
  terms:
    verbs: [{ lemma: "apply", form: "apply", taxonomy: ["bloom-r:apply", "solo:relational"] }]
    objects: ["knowledge"]
    degree: ["strong"]
    independence: []
    scope: []
    deficits: []
- id: cardiffmet/generic-2020/l3/knowledge/70-79.s3
  cell: cardiffmet/generic-2020/l3/knowledge/70-79
  span: { start: 9887, end: 10046 }
  source: "The student also demonstrates an ability to engage in confident discussion of basic concepts and displays an awareness of different perspectives or approaches."
  versionsFrom: none
  echoes: none
  force: describes
  terms:
    verbs: [{ lemma: "demonstrate", form: "demonstrates", taxonomy: ["bloom-r:apply/understand"] }]
    objects: ["concepts", "perspectives", "approaches"]
    degree: ["confident"]
    independence: []
    scope: ["basic"]
    deficits: []
- id: cardiffmet/generic-2020/l3/knowledge/70-79.s4
  cell: cardiffmet/generic-2020/l3/knowledge/70-79
  span: { start: 10047, end: 10108 }
  source: "Independent thinking is also a feature of work at this level."
  versionsFrom: none
  echoes: none
  force: describes
  terms:
    verbs: []
    objects: []
    degree: []
    independence: ["independent thinking"]
    scope: ["at this level"]
    deficits: []
- id: cardiffmet/generic-2020/l3/knowledge/60-69.s1
  cell: cardiffmet/generic-2020/l3/knowledge/60-69
  span: { start: 10157, end: 10237 }
  source: "May demonstrate a detailed knowledge of the field of study relevant to the task."
  versionsFrom: { sameAs: cardiffmet/generic-2020/l3/knowledge/70-79.s1 }
  echoes: none
  force: describes
  terms:
    verbs: [{ lemma: "demonstrate", form: "demonstrate", taxonomy: ["bloom-r:apply/understand"] }]
    objects: ["knowledge", "field of study"]
    degree: ["detailed"]
    independence: []
    scope: []
    deficits: []
- id: cardiffmet/generic-2020/l3/knowledge/60-69.s2
  cell: cardiffmet/generic-2020/l3/knowledge/60-69
  span: { start: 10238, end: 10300 }
  source: "There is clear evidence of an ability to apply such knowledge."
  versionsFrom: none
  echoes: none
  force: describes
  terms:
    verbs: [{ lemma: "apply", form: "apply", taxonomy: ["bloom-r:apply", "solo:relational"] }]
    objects: ["knowledge"]
    degree: ["clear"]
    independence: []
    scope: []
    deficits: []
- id: cardiffmet/generic-2020/l3/knowledge/60-69.s3
  cell: cardiffmet/generic-2020/l3/knowledge/60-69
  span: { start: 10301, end: 10410 }
  source: "The discussion of basic concepts is often tackled successfully and there is evidence of independent thinking."
  versionsFrom: none
  echoes: none
  force: describes
  terms:
    verbs: []
    objects: ["concepts"]
    degree: ["successfully"]
    independence: ["independent thinking"]
    scope: ["basic"]
    deficits: []
- id: cardiffmet/generic-2020/l3/knowledge/50-59.s1
  cell: cardiffmet/generic-2020/l3/knowledge/50-59
  span: { start: 10459, end: 10536 }
  source: "May demonstrate a sound knowledge of the field of study relevant to the task."
  versionsFrom: none
  echoes: none
  force: describes
  terms:
    verbs: [{ lemma: "demonstrate", form: "demonstrate", taxonomy: ["bloom-r:apply/understand"] }]
    objects: ["knowledge", "field of study"]
    degree: ["sound"]
    independence: []
    scope: []
    deficits: []
- id: cardiffmet/generic-2020/l3/knowledge/50-59.s2
  cell: cardiffmet/generic-2020/l3/knowledge/50-59
  span: { start: 10537, end: 10698 }
  source: "Although there may be a tendency to rely on information received from elsewhere (e.g. programme materials), there is still some evidence of independent thinking."
  versionsFrom: none
  echoes: none
  force: describes
  terms:
    verbs: []
    objects: ["information"]
    degree: ["some"]
    independence: ["independent thinking"]
    scope: []
    deficits: []
- id: cardiffmet/generic-2020/l3/knowledge/50-59.s3
  cell: cardiffmet/generic-2020/l3/knowledge/50-59
  span: { start: 10699, end: 10790 }
  source: "A few errors and/or misconceptions may be present, but these will not be in important areas"
  versionsFrom: none
  echoes: none
  force: describes
  terms:
    verbs: [{ lemma: "present", form: "present", taxonomy: ["none"] }]
    objects: []
    degree: []
    independence: []
    scope: []
    deficits: ["errors", "misconceptions", "not"]
- id: cardiffmet/generic-2020/l3/knowledge/40-49.s1
  cell: cardiffmet/generic-2020/l3/knowledge/40-49
  span: { start: 10839, end: 10916 }
  source: "May demonstrate a basic knowledge of the field of study relevant to the task."
  versionsFrom: none
  echoes: none
  force: describes
  terms:
    verbs: [{ lemma: "demonstrate", form: "demonstrate", taxonomy: ["bloom-r:apply/understand"] }]
    objects: ["knowledge", "field of study"]
    degree: ["basic"]
    independence: []
    scope: ["basic"]
    deficits: []
- id: cardiffmet/generic-2020/l3/knowledge/40-49.s2
  cell: cardiffmet/generic-2020/l3/knowledge/40-49
  span: { start: 10917, end: 11036 }
  source: "Reproducing information received from elsewhere (e.g. programme materials) is a frequent feature of work at this level."
  versionsFrom: none
  echoes: none
  force: describes
  terms:
    verbs: [{ lemma: "reproduce", form: "reproducing", taxonomy: ["bloom-r:remember", "solo:unistructural"] }]
    objects: ["information"]
    degree: []
    independence: []
    scope: ["at this level"]
    deficits: []
- id: cardiffmet/generic-2020/l3/knowledge/40-49.s3
  cell: cardiffmet/generic-2020/l3/knowledge/40-49
  span: { start: 11037, end: 11171 }
  source: "Errors and misconceptions will be evident, but these are outweighed by the degree of knowledge and understanding demonstrated overall."
  versionsFrom: none
  echoes: none
  force: describes
  terms:
    verbs: [{ lemma: "demonstrate", form: "demonstrated", taxonomy: ["bloom-r:apply/understand"] }]
    objects: ["knowledge and understanding"]
    degree: []
    independence: []
    scope: []
    deficits: ["errors", "misconceptions"]
- id: cardiffmet/generic-2020/l3/knowledge/30-39.s1
  cell: cardiffmet/generic-2020/l3/knowledge/30-39
  span: { start: 11227, end: 11322 }
  source: "May demonstrate limited knowledge and understanding of the field of study relevant to the task."
  versionsFrom: none
  echoes: none
  force: describes
  terms:
    verbs: [{ lemma: "demonstrate", form: "demonstrate", taxonomy: ["bloom-r:apply/understand"] }]
    objects: ["knowledge and understanding", "field of study"]
    degree: ["limited"]
    independence: []
    scope: []
    deficits: []
- id: cardiffmet/generic-2020/l3/knowledge/30-39.s2
  cell: cardiffmet/generic-2020/l3/knowledge/30-39
  span: { start: 11323, end: 11466 }
  source: "Factual inaccuracies, errors and misconceptions are evident in important areas and elements of the assessed work may be irrelevant to the task."
  versionsFrom: none
  echoes: none
  force: describes
  terms:
    verbs: []
    objects: []
    degree: []
    independence: []
    scope: []
    deficits: ["inaccuracies", "errors", "misconceptions", "irrelevant"]
- id: cardiffmet/generic-2020/l3/knowledge/1-29.s1
  cell: cardiffmet/generic-2020/l3/knowledge/1-29
  span: { start: 11520, end: 11614 }
  source: "May demonstrate little knowledge and understanding of the field of study relevant to the task."
  versionsFrom: none
  echoes: none
  force: describes
  terms:
    verbs: [{ lemma: "demonstrate", form: "demonstrate", taxonomy: ["bloom-r:apply/understand"] }]
    objects: ["knowledge and understanding", "field of study"]
    degree: ["little"]
    independence: []
    scope: []
    deficits: []
- id: cardiffmet/generic-2020/l3/knowledge/1-29.s2
  cell: cardiffmet/generic-2020/l3/knowledge/1-29
  span: { start: 11615, end: 11773 }
  source: "Factual inaccuracies, errors and misconceptions are evident in many important areas and these outweigh the degree of knowledge and understanding demonstrated."
  versionsFrom: none
  echoes: none
  force: describes
  terms:
    verbs: [{ lemma: "demonstrate", form: "demonstrated", taxonomy: ["bloom-r:apply/understand"] }]
    objects: ["knowledge and understanding"]
    degree: []
    independence: []
    scope: []
    deficits: ["inaccuracies", "errors", "misconceptions"]
- id: cardiffmet/generic-2020/l3/knowledge/1-29.s3
  cell: cardiffmet/generic-2020/l3/knowledge/1-29
  span: { start: 11774, end: 11846 }
  source: "Substantial elements of the assessed work may be irrelevant to the task."
  versionsFrom: none
  echoes: none
  force: describes
  terms:
    verbs: []
    objects: []
    degree: []
    independence: []
    scope: []
    deficits: ["irrelevant"]
- id: cardiffmet/generic-2020/l3/presentation/80-100.s1
  cell: cardiffmet/generic-2020/l3/presentation/80-100
  span: { start: 11909, end: 12010 }
  source: "Further to the 70%-79% band, work in the 80%-100% bands would extend beyond that expected at Level 3."
  versionsFrom: { sameAs: cardiffmet/generic-2020/l3/knowledge/80-100.s1 }
  echoes: none
  force: describes
  terms:
    verbs: [{ lemma: "extend", form: "extend", taxonomy: ["bloom-r:understand"] }]
    objects: []
    degree: []
    independence: []
    scope: []
    deficits: []
- id: cardiffmet/generic-2020/l3/presentation/70-79.s1
  cell: cardiffmet/generic-2020/l3/presentation/70-79
  span: { start: 12064, end: 12301 }
  source: "May demonstrate an ability to present, evaluate and interpret qualitative and quantitative data, in order to develop lines of argument and make sound judgements in accordance with basic theories and concepts of their subject(s) of study."
  versionsFrom: none
  echoes: { statement: qaa/fheq-2024/4.10.b2, words: 35 }
  force: describes
  terms:
    verbs: [{ lemma: "demonstrate", form: "demonstrate", taxonomy: ["bloom-r:apply/understand"] }, { lemma: "interpret", form: "interpret", taxonomy: ["bloom-r:apply/evaluate/understand", "solo:extended-abstract/relational"] }, { lemma: "evaluate", form: "evaluate", taxonomy: ["bloom-r:analyze/create/evaluate", "solo:extended-abstract"] }, { lemma: "develop", form: "develop", taxonomy: ["bloom-r:apply/create"] }, { lemma: "make", form: "make", taxonomy: ["bloom-r:create"] }, { lemma: "present", form: "present", taxonomy: ["none"] }]
    objects: ["qualitative and quantitative data", "lines of argument", "basic theories and concepts"]
    degree: ["sound"]
    independence: []
    scope: ["basic"]
    deficits: []
- id: cardiffmet/generic-2020/l3/presentation/70-79.s2
  cell: cardiffmet/generic-2020/l3/presentation/70-79
  span: { start: 12302, end: 12366 }
  source: "The standard of presentation is high and the format appropriate."
  versionsFrom: none
  echoes: none
  force: describes
  terms:
    verbs: [{ lemma: "present", form: "presentation", taxonomy: ["none"] }]
    objects: ["presentation"]
    degree: ["high"]
    independence: []
    scope: []
    deficits: []
- id: cardiffmet/generic-2020/l3/presentation/70-79.s3
  cell: cardiffmet/generic-2020/l3/presentation/70-79
  span: { start: 12367, end: 12442 }
  source: "Key points are logically organised and in written work, the style is lucid."
  versionsFrom: none
  echoes: none
  force: describes
  terms:
    verbs: []
    objects: []
    degree: []
    independence: []
    scope: ["key"]
    deficits: []
- id: cardiffmet/generic-2020/l3/presentation/70-79.s4
  cell: cardiffmet/generic-2020/l3/presentation/70-79
  span: { start: 12443, end: 12494 }
  source: "Arguments are well-defined and clearly articulated."
  versionsFrom: none
  echoes: none
  force: describes
  terms:
    verbs: []
    objects: ["arguments"]
    degree: ["clearly"]
    independence: []
    scope: ["well-defined"]
    deficits: []
- id: cardiffmet/generic-2020/l3/presentation/60-69.s1
  cell: cardiffmet/generic-2020/l3/presentation/60-69
  span: { start: 12548, end: 12785 }
  source: "May demonstrate an ability to present, evaluate and interpret qualitative and quantitative data, in order to develop lines of argument and make sound judgements in accordance with basic theories and concepts of their subject(s) of study."
  versionsFrom: { sameAs: cardiffmet/generic-2020/l3/presentation/70-79.s1 }
  echoes: { statement: qaa/fheq-2024/4.10.b2, words: 35 }
  force: describes
  terms:
    verbs: [{ lemma: "demonstrate", form: "demonstrate", taxonomy: ["bloom-r:apply/understand"] }, { lemma: "interpret", form: "interpret", taxonomy: ["bloom-r:apply/evaluate/understand", "solo:extended-abstract/relational"] }, { lemma: "evaluate", form: "evaluate", taxonomy: ["bloom-r:analyze/create/evaluate", "solo:extended-abstract"] }, { lemma: "develop", form: "develop", taxonomy: ["bloom-r:apply/create"] }, { lemma: "make", form: "make", taxonomy: ["bloom-r:create"] }, { lemma: "present", form: "present", taxonomy: ["none"] }]
    objects: ["qualitative and quantitative data", "lines of argument", "basic theories and concepts"]
    degree: ["sound"]
    independence: []
    scope: ["basic"]
    deficits: []
- id: cardiffmet/generic-2020/l3/presentation/60-69.s2
  cell: cardiffmet/generic-2020/l3/presentation/60-69
  span: { start: 12786, end: 12836 }
  source: "Work is well presented and the format appropriate."
  versionsFrom: none
  echoes: none
  force: describes
  terms:
    verbs: []
    objects: []
    degree: ["well"]
    independence: []
    scope: []
    deficits: []
- id: cardiffmet/generic-2020/l3/presentation/60-69.s3
  cell: cardiffmet/generic-2020/l3/presentation/60-69
  span: { start: 12837, end: 12960 }
  source: "Key points are appropriately organised and in written work, the writing style is fluent and arguments are well articulated."
  versionsFrom: none
  echoes: none
  force: describes
  terms:
    verbs: []
    objects: ["arguments"]
    degree: ["well"]
    independence: []
    scope: ["key"]
    deficits: []
- id: cardiffmet/generic-2020/l3/presentation/50-59.s1
  cell: cardiffmet/generic-2020/l3/presentation/50-59
  span: { start: 13014, end: 13253 }
  source: "May demonstrate some ability to present, evaluate and interpret qualitative and quantitative data, in order to develop lines of argument and make sound judgements in accordance with basic theories and concepts of their subject(s) of study."
  versionsFrom: none
  echoes: { statement: qaa/fheq-2024/4.10.b2, words: 34 }
  force: describes
  terms:
    verbs: [{ lemma: "demonstrate", form: "demonstrate", taxonomy: ["bloom-r:apply/understand"] }, { lemma: "interpret", form: "interpret", taxonomy: ["bloom-r:apply/evaluate/understand", "solo:extended-abstract/relational"] }, { lemma: "evaluate", form: "evaluate", taxonomy: ["bloom-r:analyze/create/evaluate", "solo:extended-abstract"] }, { lemma: "develop", form: "develop", taxonomy: ["bloom-r:apply/create"] }, { lemma: "make", form: "make", taxonomy: ["bloom-r:create"] }, { lemma: "present", form: "present", taxonomy: ["none"] }]
    objects: ["qualitative and quantitative data", "lines of argument", "basic theories and concepts"]
    degree: ["some", "sound"]
    independence: []
    scope: ["basic"]
    deficits: []
- id: cardiffmet/generic-2020/l3/presentation/50-59.s2
  cell: cardiffmet/generic-2020/l3/presentation/50-59
  span: { start: 13254, end: 13316 }
  source: "Overall, the structure and format of the work are appropriate."
  versionsFrom: none
  echoes: none
  force: describes
  terms:
    verbs: []
    objects: ["structure"]
    degree: []
    independence: []
    scope: []
    deficits: []
- id: cardiffmet/generic-2020/l3/presentation/50-59.s3
  cell: cardiffmet/generic-2020/l3/presentation/50-59
  span: { start: 13317, end: 13441 }
  source: "There may be occasional faults in the presentation of work but overall, these do not detract from the clarity of expression."
  versionsFrom: none
  echoes: none
  force: describes
  terms:
    verbs: [{ lemma: "present", form: "presentation", taxonomy: ["none"] }]
    objects: ["presentation"]
    degree: []
    independence: []
    scope: []
    deficits: ["not"]
- id: cardiffmet/generic-2020/l3/presentation/40-49.s1
  cell: cardiffmet/generic-2020/l3/presentation/40-49
  span: { start: 13495, end: 13737 }
  source: "May demonstrate limited ability to present, evaluate and interpret qualitative and quantitative data, in order to develop lines of argument and make sound judgements in accordance with basic theories and concepts of their subject(s) of study."
  versionsFrom: none
  echoes: { statement: qaa/fheq-2024/4.10.b2, words: 34 }
  force: describes
  terms:
    verbs: [{ lemma: "demonstrate", form: "demonstrate", taxonomy: ["bloom-r:apply/understand"] }, { lemma: "interpret", form: "interpret", taxonomy: ["bloom-r:apply/evaluate/understand", "solo:extended-abstract/relational"] }, { lemma: "evaluate", form: "evaluate", taxonomy: ["bloom-r:analyze/create/evaluate", "solo:extended-abstract"] }, { lemma: "develop", form: "develop", taxonomy: ["bloom-r:apply/create"] }, { lemma: "make", form: "make", taxonomy: ["bloom-r:create"] }, { lemma: "present", form: "present", taxonomy: ["none"] }]
    objects: ["qualitative and quantitative data", "lines of argument", "basic theories and concepts"]
    degree: ["limited", "sound"]
    independence: []
    scope: ["basic"]
    deficits: []
- id: cardiffmet/generic-2020/l3/presentation/40-49.s2
  cell: cardiffmet/generic-2020/l3/presentation/40-49
  span: { start: 13738, end: 13860 }
  source: "However, more success is achieved in describing and reporting factual information rather than communicating complex ideas."
  versionsFrom: none
  echoes: none
  force: describes
  terms:
    verbs: [{ lemma: "communicate", form: "communicating", taxonomy: ["none"] }, { lemma: "describe", form: "describing", taxonomy: ["bloom-r:evaluate/remember/understand", "solo:multistructural"] }, { lemma: "report", form: "reporting", taxonomy: ["bloom-r:apply/understand", "solo:multistructural"] }]
    objects: ["information", "ideas"]
    degree: []
    independence: []
    scope: ["complex"]
    deficits: []
- id: cardiffmet/generic-2020/l3/presentation/40-49.s3
  cell: cardiffmet/generic-2020/l3/presentation/40-49
  span: { start: 13861, end: 13960 }
  source: "Generally, the work is appropriately structured although key points may not be logically sequenced."
  versionsFrom: none
  echoes: none
  force: describes
  terms:
    verbs: []
    objects: []
    degree: ["generally"]
    independence: []
    scope: ["key"]
    deficits: ["not"]
- id: cardiffmet/generic-2020/l3/presentation/40-49.s4
  cell: cardiffmet/generic-2020/l3/presentation/40-49
  span: { start: 13961, end: 14047 }
  source: "Although there will be faults in the presentation of work, the meaning is still clear."
  versionsFrom: none
  echoes: none
  force: describes
  terms:
    verbs: [{ lemma: "present", form: "presentation", taxonomy: ["none"] }]
    objects: ["presentation"]
    degree: ["clear"]
    independence: []
    scope: []
    deficits: []
- id: cardiffmet/generic-2020/l3/presentation/30-39.s1
  cell: cardiffmet/generic-2020/l3/presentation/30-39
  span: { start: 14108, end: 14209 }
  source: "May demonstrate limited ability to present, evaluate and interpret qualitative and quantitative data."
  versionsFrom: none
  echoes: { statement: qaa/fheq-2024/4.10.b2, words: 10 }
  force: describes
  terms:
    verbs: [{ lemma: "demonstrate", form: "demonstrate", taxonomy: ["bloom-r:apply/understand"] }, { lemma: "interpret", form: "interpret", taxonomy: ["bloom-r:apply/evaluate/understand", "solo:extended-abstract/relational"] }, { lemma: "evaluate", form: "evaluate", taxonomy: ["bloom-r:analyze/create/evaluate", "solo:extended-abstract"] }, { lemma: "present", form: "present", taxonomy: ["none"] }]
    objects: ["qualitative and quantitative data"]
    degree: ["limited"]
    independence: []
    scope: []
    deficits: []
- id: cardiffmet/generic-2020/l3/presentation/30-39.s2
  cell: cardiffmet/generic-2020/l3/presentation/30-39
  span: { start: 14210, end: 14302 }
  source: "Ideas may not be communicated clearly and present comprehension difficulties for the reader."
  versionsFrom: none
  echoes: none
  force: describes
  terms:
    verbs: [{ lemma: "present", form: "present", taxonomy: ["none"] }]
    objects: ["ideas"]
    degree: ["clearly"]
    independence: []
    scope: []
    deficits: ["not"]
- id: cardiffmet/generic-2020/l3/presentation/30-39.s3
  cell: cardiffmet/generic-2020/l3/presentation/30-39
  span: { start: 14303, end: 14409 }
  source: "If attempted, the presentation of arguments and more complex ideas may be confused and clumsily expressed."
  versionsFrom: none
  echoes: none
  force: describes
  terms:
    verbs: [{ lemma: "present", form: "presentation", taxonomy: ["none"] }]
    objects: ["presentation", "arguments", "ideas"]
    degree: []
    independence: []
    scope: ["complex"]
    deficits: ["confused"]
- id: cardiffmet/generic-2020/l3/presentation/1-29.s1
  cell: cardiffmet/generic-2020/l3/presentation/1-29
  span: { start: 14468, end: 14568 }
  source: "May demonstrate little ability to present, evaluate and interpret qualitative and quantitative data."
  versionsFrom: none
  echoes: { statement: qaa/fheq-2024/4.10.b2, words: 10 }
  force: describes
  terms:
    verbs: [{ lemma: "demonstrate", form: "demonstrate", taxonomy: ["bloom-r:apply/understand"] }, { lemma: "interpret", form: "interpret", taxonomy: ["bloom-r:apply/evaluate/understand", "solo:extended-abstract/relational"] }, { lemma: "evaluate", form: "evaluate", taxonomy: ["bloom-r:analyze/create/evaluate", "solo:extended-abstract"] }, { lemma: "present", form: "present", taxonomy: ["none"] }]
    objects: ["qualitative and quantitative data"]
    degree: ["little"]
    independence: []
    scope: []
    deficits: []
- id: cardiffmet/generic-2020/l3/presentation/1-29.s2
  cell: cardiffmet/generic-2020/l3/presentation/1-29
  span: { start: 14569, end: 14721 }
  source: "Frequent faults in the presentation of work and significant difficulties in its structure and organisation detract from the clarity and meaning overall."
  versionsFrom: none
  echoes: none
  force: describes
  terms:
    verbs: [{ lemma: "present", form: "presentation", taxonomy: ["none"] }]
    objects: ["presentation", "structure"]
    degree: []
    independence: []
    scope: []
    deficits: []
- id: cardiffmet/generic-2020/l3/presentation/1-29.s3
  cell: cardiffmet/generic-2020/l3/presentation/1-29
  span: { start: 14722, end: 14774 }
  source: "The writing style is often clumsy and inappropriate."
  versionsFrom: none
  echoes: none
  force: describes
  terms:
    verbs: []
    objects: []
    degree: []
    independence: []
    scope: []
    deficits: ["clumsy"]
- id: cardiffmet/generic-2020/l3/analysis/80-100.s1
  cell: cardiffmet/generic-2020/l3/analysis/80-100
  span: { start: 14828, end: 14929 }
  source: "Further to the 70%-79% band, work in the 80%-100% bands would extend beyond that expected at Level 3."
  versionsFrom: { sameAs: cardiffmet/generic-2020/l3/knowledge/80-100.s1 }
  echoes: none
  force: describes
  terms:
    verbs: [{ lemma: "extend", form: "extend", taxonomy: ["bloom-r:understand"] }]
    objects: []
    degree: []
    independence: []
    scope: []
    deficits: []
- id: cardiffmet/generic-2020/l3/analysis/70-79.s1
  cell: cardiffmet/generic-2020/l3/analysis/70-79
  span: { start: 14974, end: 15169 }
  source: "May demonstrate an ability to select and use different approaches to solving well-defined, complex and non-routine problems related to their area of study by making use of appropriate techniques."
  versionsFrom: none
  echoes: none
  force: describes
  terms:
    verbs: [{ lemma: "demonstrate", form: "demonstrate", taxonomy: ["bloom-r:apply/understand"] }, { lemma: "use", form: "use", taxonomy: ["bloom-r:apply"] }, { lemma: "make", form: "making", taxonomy: ["bloom-r:create"] }, { lemma: "select", form: "select", taxonomy: ["bloom-r:analyze/apply/evaluate/remember/understand", "solo:multistructural"] }, { lemma: "solve", form: "solving", taxonomy: ["bloom-r:analyze/apply/create", "solo:multistructural"] }]
    objects: ["approaches", "problems", "techniques"]
    degree: []
    independence: []
    scope: ["well-defined", "complex", "non-routine"]
    deficits: []
- id: cardiffmet/generic-2020/l3/analysis/70-79.s2
  cell: cardiffmet/generic-2020/l3/analysis/70-79
  span: { start: 15170, end: 15244 }
  source: "The student is highly successful in presenting and commenting on outcomes."
  versionsFrom: none
  echoes: none
  force: describes
  terms:
    verbs: [{ lemma: "comment", form: "commenting", taxonomy: ["none"] }, { lemma: "present", form: "presenting", taxonomy: ["none"] }]
    objects: []
    degree: ["highly", "successful"]
    independence: []
    scope: []
    deficits: []
- id: cardiffmet/generic-2020/l3/analysis/60-69.s1
  cell: cardiffmet/generic-2020/l3/analysis/60-69
  span: { start: 15289, end: 15541 }
  source: "May demonstrate an ability to select and use different approaches to solving well-defined, complex and non-routine problems related to their area of study by making use of appropriate techniques and has success in presenting and commenting on outcomes."
  versionsFrom: none
  echoes: none
  force: describes
  terms:
    verbs: [{ lemma: "demonstrate", form: "demonstrate", taxonomy: ["bloom-r:apply/understand"] }, { lemma: "comment", form: "commenting", taxonomy: ["none"] }, { lemma: "use", form: "use", taxonomy: ["bloom-r:apply"] }, { lemma: "make", form: "making", taxonomy: ["bloom-r:create"] }, { lemma: "select", form: "select", taxonomy: ["bloom-r:analyze/apply/evaluate/remember/understand", "solo:multistructural"] }, { lemma: "present", form: "presenting", taxonomy: ["none"] }, { lemma: "solve", form: "solving", taxonomy: ["bloom-r:analyze/apply/create", "solo:multistructural"] }]
    objects: ["approaches", "problems", "techniques"]
    degree: []
    independence: []
    scope: ["well-defined", "complex", "non-routine"]
    deficits: []
- id: cardiffmet/generic-2020/l3/analysis/50-59.s1
  cell: cardiffmet/generic-2020/l3/analysis/50-59
  span: { start: 15586, end: 15808 }
  source: "May demonstrate an ability to select and use different approaches to solving well-defined, complex and non-routine problems related to their area of study and generally has success in presenting and commenting on outcomes."
  versionsFrom: none
  echoes: none
  force: describes
  terms:
    verbs: [{ lemma: "demonstrate", form: "demonstrate", taxonomy: ["bloom-r:apply/understand"] }, { lemma: "comment", form: "commenting", taxonomy: ["none"] }, { lemma: "use", form: "use", taxonomy: ["bloom-r:apply"] }, { lemma: "select", form: "select", taxonomy: ["bloom-r:analyze/apply/evaluate/remember/understand", "solo:multistructural"] }, { lemma: "present", form: "presenting", taxonomy: ["none"] }, { lemma: "solve", form: "solving", taxonomy: ["bloom-r:analyze/apply/create", "solo:multistructural"] }]
    objects: ["approaches", "problems"]
    degree: ["generally"]
    independence: []
    scope: ["well-defined", "complex", "non-routine"]
    deficits: []
- id: cardiffmet/generic-2020/l3/analysis/40-49.s1
  cell: cardiffmet/generic-2020/l3/analysis/40-49
  span: { start: 15853, end: 16085 }
  source: "May demonstrate a limited ability to select and use different approaches to solving well-defined, complex and non-routine problems related to their area of study and has intermittent success in presenting and commenting on outcomes."
  versionsFrom: none
  echoes: none
  force: describes
  terms:
    verbs: [{ lemma: "demonstrate", form: "demonstrate", taxonomy: ["bloom-r:apply/understand"] }, { lemma: "comment", form: "commenting", taxonomy: ["none"] }, { lemma: "use", form: "use", taxonomy: ["bloom-r:apply"] }, { lemma: "select", form: "select", taxonomy: ["bloom-r:analyze/apply/evaluate/remember/understand", "solo:multistructural"] }, { lemma: "present", form: "presenting", taxonomy: ["none"] }, { lemma: "solve", form: "solving", taxonomy: ["bloom-r:analyze/apply/create", "solo:multistructural"] }]
    objects: ["approaches", "problems"]
    degree: ["limited"]
    independence: []
    scope: ["well-defined", "complex", "non-routine"]
    deficits: []
- id: cardiffmet/generic-2020/l3/analysis/30-39.s1
  cell: cardiffmet/generic-2020/l3/analysis/30-39
  span: { start: 16137, end: 16357 }
  source: "May demonstrate a limited ability to select and use different approaches to solving well-defined, complex and non-routine problems related to their area of study but outcomes may be naïve, simplistic and/or unconvincing."
  versionsFrom: none
  echoes: none
  force: describes
  terms:
    verbs: [{ lemma: "demonstrate", form: "demonstrate", taxonomy: ["bloom-r:apply/understand"] }, { lemma: "use", form: "use", taxonomy: ["bloom-r:apply"] }, { lemma: "select", form: "select", taxonomy: ["bloom-r:analyze/apply/evaluate/remember/understand", "solo:multistructural"] }, { lemma: "solve", form: "solving", taxonomy: ["bloom-r:analyze/apply/create", "solo:multistructural"] }]
    objects: ["approaches", "problems"]
    degree: ["limited"]
    independence: []
    scope: ["well-defined", "complex", "non-routine"]
    deficits: ["naïve", "simplistic", "unconvincing"]
- id: cardiffmet/generic-2020/l3/analysis/1-29.s1
  cell: cardiffmet/generic-2020/l3/analysis/1-29
  span: { start: 16407, end: 16569 }
  source: "May demonstrate little ability to select and use of different approaches to solving well-defined, complex and non-routine problems related to their area of study."
  versionsFrom: none
  echoes: none
  force: describes
  terms:
    verbs: [{ lemma: "demonstrate", form: "demonstrate", taxonomy: ["bloom-r:apply/understand"] }, { lemma: "use", form: "use", taxonomy: ["bloom-r:apply"] }, { lemma: "select", form: "select", taxonomy: ["bloom-r:analyze/apply/evaluate/remember/understand", "solo:multistructural"] }, { lemma: "solve", form: "solving", taxonomy: ["bloom-r:analyze/apply/create", "solo:multistructural"] }]
    objects: ["approaches", "problems"]
    degree: ["little"]
    independence: []
    scope: ["well-defined", "complex", "non-routine"]
    deficits: []
- id: cardiffmet/generic-2020/l3/analysis/1-29.s2
  cell: cardiffmet/generic-2020/l3/analysis/1-29
  span: { start: 16570, end: 16647 }
  source: "Where such work has been attempted, outcomes may be inappropriate, or absent."
  versionsFrom: none
  echoes: none
  force: describes
  terms:
    verbs: []
    objects: []
    degree: []
    independence: []
    scope: []
    deficits: ["absent"]
- id: cardiffmet/generic-2020/l3/research/80-100.s1
  cell: cardiffmet/generic-2020/l3/research/80-100
  span: { start: 16702, end: 16803 }
  source: "Further to the 70%-79% band, work in the 80%-100% bands would extend beyond that expected at Level 3."
  versionsFrom: { sameAs: cardiffmet/generic-2020/l3/knowledge/80-100.s1 }
  echoes: none
  force: describes
  terms:
    verbs: [{ lemma: "extend", form: "extend", taxonomy: ["bloom-r:understand"] }]
    objects: []
    degree: []
    independence: []
    scope: []
    deficits: []
- id: cardiffmet/generic-2020/l3/research/70-79.s1
  cell: cardiffmet/generic-2020/l3/research/70-79
  span: { start: 16849, end: 16937 }
  source: "May demonstrate an awareness of current research/advanced scholarship in the discipline."
  versionsFrom: none
  echoes: none
  force: describes
  terms:
    verbs: [{ lemma: "demonstrate", form: "demonstrate", taxonomy: ["bloom-r:apply/understand"] }]
    objects: ["research", "scholarship", "discipline"]
    degree: []
    independence: []
    scope: ["current", "advanced"]
    deficits: []
- id: cardiffmet/generic-2020/l3/research/70-79.s2
  cell: cardiffmet/generic-2020/l3/research/70-79
  span: { start: 16938, end: 17085 }
  source: "Use of scholarly reviews/primary sources and a breadth of individual reading and investigation, extending beyond the sources provided, is apparent."
  versionsFrom: none
  echoes: none
  force: describes
  terms:
    verbs: [{ lemma: "use", form: "use", taxonomy: ["bloom-r:apply"] }]
    objects: ["primary sources", "reading", "sources"]
    degree: []
    independence: []
    scope: []
    deficits: []
- id: cardiffmet/generic-2020/l3/research/70-79.s3
  cell: cardiffmet/generic-2020/l3/research/70-79
  span: { start: 17086, end: 17184 }
  source: "The referencing of literature and other sources is accurate and in line with academic conventions."
  versionsFrom: none
  echoes: none
  force: describes
  terms:
    verbs: []
    objects: ["referencing", "literature", "sources", "academic conventions"]
    degree: []
    independence: []
    scope: []
    deficits: []
- id: cardiffmet/generic-2020/l3/research/70-79.s4
  cell: cardiffmet/generic-2020/l3/research/70-79
  span: { start: 17185, end: 17375 }
  source: "A knowledge and understanding of research processes, techniques and methods is demonstrated along with an ability to apply research knowledge and skills successfully in appropriate contexts."
  versionsFrom: none
  echoes: none
  force: describes
  terms:
    verbs: [{ lemma: "demonstrate", form: "demonstrated", taxonomy: ["bloom-r:apply/understand"] }, { lemma: "apply", form: "apply", taxonomy: ["bloom-r:apply", "solo:relational"] }]
    objects: ["knowledge and understanding", "research processes", "techniques", "research", "knowledge"]
    degree: ["successfully"]
    independence: []
    scope: []
    deficits: []
- id: cardiffmet/generic-2020/l3/research/60-69.s1
  cell: cardiffmet/generic-2020/l3/research/60-69
  span: { start: 17421, end: 17509 }
  source: "May demonstrate an awareness of current research/advanced scholarship in the discipline."
  versionsFrom: { sameAs: cardiffmet/generic-2020/l3/research/70-79.s1 }
  echoes: none
  force: describes
  terms:
    verbs: [{ lemma: "demonstrate", form: "demonstrate", taxonomy: ["bloom-r:apply/understand"] }]
    objects: ["research", "scholarship", "discipline"]
    degree: []
    independence: []
    scope: ["current", "advanced"]
    deficits: []
- id: cardiffmet/generic-2020/l3/research/60-69.s2
  cell: cardiffmet/generic-2020/l3/research/60-69
  span: { start: 17510, end: 17630 }
  source: "Examples referred to indicate a breadth of individual reading and investigation that extend beyond the sources provided."
  versionsFrom: none
  echoes: none
  force: describes
  terms:
    verbs: [{ lemma: "extend", form: "extend", taxonomy: ["bloom-r:understand"] }]
    objects: ["reading", "sources"]
    degree: []
    independence: []
    scope: []
    deficits: []
- id: cardiffmet/generic-2020/l3/research/60-69.s3
  cell: cardiffmet/generic-2020/l3/research/60-69
  span: { start: 17631, end: 17705 }
  source: "The referencing of literature and other sources is almost always accurate."
  versionsFrom: none
  echoes: none
  force: describes
  terms:
    verbs: []
    objects: ["referencing", "literature", "sources"]
    degree: []
    independence: []
    scope: []
    deficits: []
- id: cardiffmet/generic-2020/l3/research/60-69.s4
  cell: cardiffmet/generic-2020/l3/research/60-69
  span: { start: 17706, end: 17845 }
  source: "A basic knowledge of research processes is evident along with an ability to apply research skills and knowledge in the appropriate context."
  versionsFrom: none
  echoes: none
  force: describes
  terms:
    verbs: [{ lemma: "apply", form: "apply", taxonomy: ["bloom-r:apply", "solo:relational"] }]
    objects: ["knowledge", "research processes", "research", "knowledge"]
    degree: ["basic"]
    independence: []
    scope: ["basic"]
    deficits: []
- id: cardiffmet/generic-2020/l3/research/50-59.s1
  cell: cardiffmet/generic-2020/l3/research/50-59
  span: { start: 17891, end: 17981 }
  source: "May demonstrate some awareness of current research/advanced scholarship in the discipline."
  versionsFrom: none
  echoes: none
  force: describes
  terms:
    verbs: [{ lemma: "demonstrate", form: "demonstrate", taxonomy: ["bloom-r:apply/understand"] }]
    objects: ["research", "scholarship", "discipline"]
    degree: ["some"]
    independence: []
    scope: ["current", "advanced"]
    deficits: []
- id: cardiffmet/generic-2020/l3/research/50-59.s2
  cell: cardiffmet/generic-2020/l3/research/50-59
  span: { start: 17982, end: 18093 }
  source: "Examples of research/scholarship referred to in the work demonstrate some individual reading and investigation."
  versionsFrom: none
  echoes: none
  force: describes
  terms:
    verbs: [{ lemma: "demonstrate", form: "demonstrate", taxonomy: ["bloom-r:apply/understand"] }]
    objects: ["research", "scholarship", "reading"]
    degree: ["some"]
    independence: []
    scope: []
    deficits: []
- id: cardiffmet/generic-2020/l3/research/50-59.s3
  cell: cardiffmet/generic-2020/l3/research/50-59
  span: { start: 18094, end: 18178 }
  source: "Occasional errors may be present in the referencing of literature and other sources."
  versionsFrom: none
  echoes: none
  force: describes
  terms:
    verbs: [{ lemma: "present", form: "present", taxonomy: ["none"] }]
    objects: ["referencing", "literature", "sources"]
    degree: []
    independence: []
    scope: []
    deficits: ["errors"]
- id: cardiffmet/generic-2020/l3/research/50-59.s4
  cell: cardiffmet/generic-2020/l3/research/50-59
  span: { start: 18179, end: 18355 }
  source: "Some knowledge of research processes is evident and the application of research skills and knowledge is generally successful, although there may be a reliance on tutor support."
  versionsFrom: none
  echoes: none
  force: describes
  terms:
    verbs: [{ lemma: "apply", form: "application", taxonomy: ["bloom-r:apply", "solo:relational"] }]
    objects: ["knowledge", "research processes", "research", "knowledge"]
    degree: ["some", "generally", "successful"]
    independence: ["reliance on tutor support"]
    scope: []
    deficits: ["reliance"]
- id: cardiffmet/generic-2020/l3/research/40-49.s1
  cell: cardiffmet/generic-2020/l3/research/40-49
  span: { start: 18401, end: 18494 }
  source: "May demonstrate limited awareness of current research/advanced scholarship in the discipline."
  versionsFrom: none
  echoes: none
  force: describes
  terms:
    verbs: [{ lemma: "demonstrate", form: "demonstrate", taxonomy: ["bloom-r:apply/understand"] }]
    objects: ["research", "scholarship", "discipline"]
    degree: ["limited"]
    independence: []
    scope: ["current", "advanced"]
    deficits: []
- id: cardiffmet/generic-2020/l3/research/40-49.s2
  cell: cardiffmet/generic-2020/l3/research/40-49
  span: { start: 18495, end: 18654 }
  source: "Examples of research/scholarship referred to in the work may indicate an over-reliance on programme materials rather than individual reading and investigation."
  versionsFrom: none
  echoes: none
  force: describes
  terms:
    verbs: []
    objects: ["research", "scholarship", "reading"]
    degree: []
    independence: []
    scope: []
    deficits: ["over-reliance"]
- id: cardiffmet/generic-2020/l3/research/40-49.s3
  cell: cardiffmet/generic-2020/l3/research/40-49
  span: { start: 18655, end: 18723 }
  source: "There are errors in the referencing of literature and other sources."
  versionsFrom: none
  echoes: none
  force: describes
  terms:
    verbs: []
    objects: ["referencing", "literature", "sources"]
    degree: []
    independence: []
    scope: []
    deficits: ["errors"]
- id: cardiffmet/generic-2020/l3/research/40-49.s4
  cell: cardiffmet/generic-2020/l3/research/40-49
  span: { start: 18724, end: 18831 }
  source: "Some knowledge of research processes is evident, although the application of such knowledge is less secure."
  versionsFrom: none
  echoes: none
  force: describes
  terms:
    verbs: [{ lemma: "apply", form: "application", taxonomy: ["bloom-r:apply", "solo:relational"] }]
    objects: ["knowledge", "research processes", "knowledge"]
    degree: ["some", "secure"]
    independence: []
    scope: []
    deficits: []
- id: cardiffmet/generic-2020/l3/research/30-39.s1
  cell: cardiffmet/generic-2020/l3/research/30-39
  span: { start: 18884, end: 18999 }
  source: "May demonstrate limited or sporadic knowledge awareness of current research/advanced scholarship in the discipline."
  versionsFrom: none
  echoes: none
  force: describes
  terms:
    verbs: [{ lemma: "demonstrate", form: "demonstrate", taxonomy: ["bloom-r:apply/understand"] }]
    objects: ["knowledge", "research", "scholarship", "discipline"]
    degree: ["limited"]
    independence: []
    scope: ["current", "advanced"]
    deficits: []
- id: cardiffmet/generic-2020/l3/research/30-39.s2
  cell: cardiffmet/generic-2020/l3/research/30-39
  span: { start: 19000, end: 19162 }
  source: "A restricted range of sources are used but overall, there is an over-reliance on programme materials with little evidence of individual reading and investigation."
  versionsFrom: none
  echoes: none
  force: describes
  terms:
    verbs: [{ lemma: "use", form: "used", taxonomy: ["bloom-r:apply"] }]
    objects: ["sources", "reading"]
    degree: ["little"]
    independence: []
    scope: []
    deficits: ["over-reliance"]
- id: cardiffmet/generic-2020/l3/research/30-39.s3
  cell: cardiffmet/generic-2020/l3/research/30-39
  span: { start: 19163, end: 19240 }
  source: "There are frequent errors in the referencing of literature and other sources."
  versionsFrom: none
  echoes: none
  force: describes
  terms:
    verbs: []
    objects: ["referencing", "literature", "sources"]
    degree: []
    independence: []
    scope: []
    deficits: ["errors"]
- id: cardiffmet/generic-2020/l3/research/30-39.s4
  cell: cardiffmet/generic-2020/l3/research/30-39
  span: { start: 19241, end: 19375 }
  source: "Although limited knowledge of research processes may evident, nevertheless, the application of such knowledge is largely unsuccessful."
  versionsFrom: none
  echoes: none
  force: describes
  terms:
    verbs: [{ lemma: "apply", form: "application", taxonomy: ["bloom-r:apply", "solo:relational"] }]
    objects: ["knowledge", "research processes", "knowledge"]
    degree: ["limited"]
    independence: []
    scope: []
    deficits: []
- id: cardiffmet/generic-2020/l3/research/1-29.s1
  cell: cardiffmet/generic-2020/l3/research/1-29
  span: { start: 19426, end: 19509 }
  source: "May demonstrate little knowledge of current research/scholarship in the discipline."
  versionsFrom: none
  echoes: none
  force: describes
  terms:
    verbs: [{ lemma: "demonstrate", form: "demonstrate", taxonomy: ["bloom-r:apply/understand"] }]
    objects: ["knowledge", "research", "scholarship", "discipline"]
    degree: ["little"]
    independence: []
    scope: ["current"]
    deficits: []
- id: cardiffmet/generic-2020/l3/research/1-29.s2
  cell: cardiffmet/generic-2020/l3/research/1-29
  span: { start: 19510, end: 19658 }
  source: "Evidence of individual reading and investigation is negligible and the limited referencing of literature and other sources is frequently inaccurate."
  versionsFrom: none
  echoes: none
  force: describes
  terms:
    verbs: []
    objects: ["reading", "referencing", "literature", "sources"]
    degree: ["limited"]
    independence: []
    scope: []
    deficits: ["negligible"]
- id: cardiffmet/generic-2020/l3/research/1-29.s3
  cell: cardiffmet/generic-2020/l3/research/1-29
  span: { start: 19659, end: 19763 }
  source: "Very limited knowledge of research processes is apparent and there is a failure to apply this knowledge."
  versionsFrom: none
  echoes: none
  force: describes
  terms:
    verbs: [{ lemma: "apply", form: "apply", taxonomy: ["bloom-r:apply", "solo:relational"] }]
    objects: ["knowledge", "research processes", "knowledge"]
    degree: ["very limited"]
    independence: []
    scope: []
    deficits: ["failure"]
- id: cardiffmet/generic-2020/l3/argument/80-100.s1
  cell: cardiffmet/generic-2020/l3/argument/80-100
  span: { start: 19839, end: 19940 }
  source: "Further to the 70%-79% band, work in the 80%-100% bands would extend beyond that expected at Level 3."
  versionsFrom: { sameAs: cardiffmet/generic-2020/l3/knowledge/80-100.s1 }
  echoes: none
  force: describes
  terms:
    verbs: [{ lemma: "extend", form: "extend", taxonomy: ["bloom-r:understand"] }]
    objects: []
    degree: []
    independence: []
    scope: []
    deficits: []
- id: cardiffmet/generic-2020/l3/argument/70-79.s1
  cell: cardiffmet/generic-2020/l3/argument/70-79
  span: { start: 20007, end: 20131 }
  source: "May demonstrate an ability to communicate the results of their study/work accurately and reliably with structured arguments."
  versionsFrom: none
  echoes: { statement: qaa/fheq-2024/4.10.b4, words: 10 }
  force: describes
  terms:
    verbs: [{ lemma: "demonstrate", form: "demonstrate", taxonomy: ["bloom-r:apply/understand"] }, { lemma: "communicate", form: "communicate", taxonomy: ["none"] }]
    objects: ["arguments"]
    degree: []
    independence: []
    scope: []
    deficits: []
- id: cardiffmet/generic-2020/l3/argument/70-79.s2
  cell: cardiffmet/generic-2020/l3/argument/70-79
  span: { start: 20132, end: 20243 }
  source: "Arguments are well developed and substantiated and there is recognition of the complexities of academic debate."
  versionsFrom: none
  echoes: none
  force: describes
  terms:
    verbs: [{ lemma: "develop", form: "developed", taxonomy: ["bloom-r:apply/create"] }, { lemma: "recognise", form: "recognition", taxonomy: ["solo:unistructural"] }]
    objects: ["arguments"]
    degree: ["well"]
    independence: []
    scope: []
    deficits: []
- id: cardiffmet/generic-2020/l3/argument/70-79.s3
  cell: cardiffmet/generic-2020/l3/argument/70-79
  span: { start: 20244, end: 20354 }
  source: "Appropriate solutions are offered to problems and the effectiveness of the methods of resolution are reviewed."
  versionsFrom: none
  echoes: none
  force: describes
  terms:
    verbs: [{ lemma: "solve", form: "solutions", taxonomy: ["bloom-r:analyze/apply/create", "solo:multistructural"] }]
    objects: ["problems"]
    degree: []
    independence: []
    scope: []
    deficits: []
- id: cardiffmet/generic-2020/l3/argument/70-79.s4
  cell: cardiffmet/generic-2020/l3/argument/70-79
  span: { start: 20355, end: 20524 }
  source: "There is strong evidence that the student is able to reflect effectively on the student’s own practice, with a full awareness of the implications for future development."
  versionsFrom: none
  echoes: none
  force: describes
  terms:
    verbs: [{ lemma: "develop", form: "development", taxonomy: ["bloom-r:apply/create"] }, { lemma: "reflect", form: "reflect", taxonomy: ["solo:extended-abstract"] }]
    objects: ["own practice"]
    degree: ["strong", "effectively"]
    independence: []
    scope: []
    deficits: []
- id: cardiffmet/generic-2020/l3/argument/60-69.s1
  cell: cardiffmet/generic-2020/l3/argument/60-69
  span: { start: 20591, end: 20689 }
  source: "May demonstrate an ability to communicate the results of their study/work accurately and reliably."
  versionsFrom: none
  echoes: { statement: qaa/fheq-2024/4.10.b4, words: 10 }
  force: describes
  terms:
    verbs: [{ lemma: "demonstrate", form: "demonstrate", taxonomy: ["bloom-r:apply/understand"] }, { lemma: "communicate", form: "communicate", taxonomy: ["none"] }]
    objects: []
    degree: []
    independence: []
    scope: []
    deficits: []
- id: cardiffmet/generic-2020/l3/argument/60-69.s2
  cell: cardiffmet/generic-2020/l3/argument/60-69
  span: { start: 20690, end: 20845 }
  source: "Arguments are clearly considered and substantiated and there is evidence of an ability to make appropriate judgements and to suggest solutions to problems."
  versionsFrom: none
  echoes: none
  force: describes
  terms:
    verbs: [{ lemma: "make", form: "make", taxonomy: ["bloom-r:create"] }, { lemma: "solve", form: "solutions", taxonomy: ["bloom-r:analyze/apply/create", "solo:multistructural"] }]
    objects: ["arguments", "problems"]
    degree: ["clearly"]
    independence: []
    scope: []
    deficits: []
- id: cardiffmet/generic-2020/l3/argument/60-69.s3
  cell: cardiffmet/generic-2020/l3/argument/60-69
  span: { start: 20846, end: 20906 }
  source: "The effectiveness of the methods of resolution are reviewed."
  versionsFrom: none
  echoes: none
  force: describes
  terms:
    verbs: []
    objects: []
    degree: []
    independence: []
    scope: []
    deficits: []
- id: cardiffmet/generic-2020/l3/argument/60-69.s4
  cell: cardiffmet/generic-2020/l3/argument/60-69
  span: { start: 20907, end: 21057 }
  source: "The student also demonstrates an ability to engage in reflective practice and to take account of personal evaluations planning for future development."
  versionsFrom: none
  echoes: none
  force: describes
  terms:
    verbs: [{ lemma: "demonstrate", form: "demonstrates", taxonomy: ["bloom-r:apply/understand"] }, { lemma: "evaluate", form: "evaluations", taxonomy: ["bloom-r:analyze/create/evaluate", "solo:extended-abstract"] }, { lemma: "develop", form: "development", taxonomy: ["bloom-r:apply/create"] }, { lemma: "plan", form: "planning", taxonomy: ["bloom-r:create", "solo:relational"] }]
    objects: []
    degree: []
    independence: []
    scope: []
    deficits: []
- id: cardiffmet/generic-2020/l3/argument/50-59.s1
  cell: cardiffmet/generic-2020/l3/argument/50-59
  span: { start: 21124, end: 21315 }
  source: "May demonstrate, at times, an ability to communicate the results of their study/work accurately and reliably, although there may be some over-reliance on description and factual presentation."
  versionsFrom: none
  echoes: { statement: qaa/fheq-2024/4.10.b4, words: 10 }
  force: describes
  terms:
    verbs: [{ lemma: "demonstrate", form: "demonstrate", taxonomy: ["bloom-r:apply/understand"] }, { lemma: "communicate", form: "communicate", taxonomy: ["none"] }, { lemma: "present", form: "presentation", taxonomy: ["none"] }, { lemma: "describe", form: "description", taxonomy: ["bloom-r:evaluate/remember/understand", "solo:multistructural"] }]
    objects: ["presentation"]
    degree: ["some"]
    independence: []
    scope: []
    deficits: ["over-reliance"]
- id: cardiffmet/generic-2020/l3/argument/50-59.s2
  cell: cardiffmet/generic-2020/l3/argument/50-59
  span: { start: 21316, end: 21352 }
  source: "Arguments are usually substantiated."
  versionsFrom: none
  echoes: none
  force: describes
  terms:
    verbs: []
    objects: ["arguments"]
    degree: []
    independence: []
    scope: []
    deficits: []
- id: cardiffmet/generic-2020/l3/argument/50-59.s3
  cell: cardiffmet/generic-2020/l3/argument/50-59
  span: { start: 21353, end: 21555 }
  source: "There is some evidence of the student’s ability to evaluate and reflect on the student’s own practice, but reflections may lack insight and the implications for future development may be underestimated."
  versionsFrom: none
  echoes: none
  force: describes
  terms:
    verbs: [{ lemma: "evaluate", form: "evaluate", taxonomy: ["bloom-r:analyze/create/evaluate", "solo:extended-abstract"] }, { lemma: "develop", form: "development", taxonomy: ["bloom-r:apply/create"] }, { lemma: "reflect", form: "reflect", taxonomy: ["solo:extended-abstract"] }]
    objects: ["own practice"]
    degree: ["some"]
    independence: []
    scope: []
    deficits: ["lack"]
- id: cardiffmet/generic-2020/l3/argument/40-49.s1
  cell: cardiffmet/generic-2020/l3/argument/40-49
  span: { start: 21622, end: 21727 }
  source: "May demonstrate a limited ability to communicate the results of their study/work accurately and reliably."
  versionsFrom: none
  echoes: { statement: qaa/fheq-2024/4.10.b4, words: 10 }
  force: describes
  terms:
    verbs: [{ lemma: "demonstrate", form: "demonstrate", taxonomy: ["bloom-r:apply/understand"] }, { lemma: "communicate", form: "communicate", taxonomy: ["none"] }]
    objects: []
    degree: ["limited"]
    independence: []
    scope: []
    deficits: []
- id: cardiffmet/generic-2020/l3/argument/40-49.s2
  cell: cardiffmet/generic-2020/l3/argument/40-49
  span: { start: 21728, end: 21822 }
  source: "The balance within the work is likely to be in favour of description and factual presentation."
  versionsFrom: none
  echoes: none
  force: describes
  terms:
    verbs: [{ lemma: "present", form: "presentation", taxonomy: ["none"] }, { lemma: "describe", form: "description", taxonomy: ["bloom-r:evaluate/remember/understand", "solo:multistructural"] }]
    objects: ["presentation"]
    degree: []
    independence: []
    scope: []
    deficits: []
- id: cardiffmet/generic-2020/l3/argument/40-49.s3
  cell: cardiffmet/generic-2020/l3/argument/40-49
  span: { start: 21823, end: 21888 }
  source: "Arguments are generally substantiated but may be under-developed."
  versionsFrom: none
  echoes: none
  force: describes
  terms:
    verbs: []
    objects: ["arguments"]
    degree: ["generally"]
    independence: []
    scope: []
    deficits: []
- id: cardiffmet/generic-2020/l3/argument/40-49.s4
  cell: cardiffmet/generic-2020/l3/argument/40-49
  span: { start: 21889, end: 22112 }
  source: "There is some evidence of the student’s ability to evaluate and reflect on the student’s own practice. although reflections may be limited and superficial with little consideration of their relevance for future development."
  versionsFrom: none
  echoes: none
  force: describes
  terms:
    verbs: [{ lemma: "evaluate", form: "evaluate", taxonomy: ["bloom-r:analyze/create/evaluate", "solo:extended-abstract"] }, { lemma: "develop", form: "development", taxonomy: ["bloom-r:apply/create"] }, { lemma: "consider", form: "consideration", taxonomy: ["none"] }, { lemma: "reflect", form: "reflect", taxonomy: ["solo:extended-abstract"] }]
    objects: ["own practice"]
    degree: ["some", "limited", "little"]
    independence: []
    scope: []
    deficits: ["superficial"]
- id: cardiffmet/generic-2020/l3/argument/30-39.s1
  cell: cardiffmet/generic-2020/l3/argument/30-39
  span: { start: 22186, end: 22304 }
  source: "May demonstrate limited evidence of an ability to communicate the results of their study/work accurately and reliably."
  versionsFrom: none
  echoes: { statement: qaa/fheq-2024/4.10.b4, words: 10 }
  force: describes
  terms:
    verbs: [{ lemma: "demonstrate", form: "demonstrate", taxonomy: ["bloom-r:apply/understand"] }, { lemma: "communicate", form: "communicate", taxonomy: ["none"] }]
    objects: []
    degree: ["limited"]
    independence: []
    scope: []
    deficits: []
- id: cardiffmet/generic-2020/l3/argument/30-39.s2
  cell: cardiffmet/generic-2020/l3/argument/30-39
  span: { start: 22305, end: 22391 }
  source: "The work is largely descriptive and arguments, if attempted, are rarely substantiated."
  versionsFrom: none
  echoes: none
  force: describes
  terms:
    verbs: [{ lemma: "describe", form: "descriptive", taxonomy: ["bloom-r:evaluate/remember/understand", "solo:multistructural"] }]
    objects: ["arguments"]
    degree: []
    independence: []
    scope: []
    deficits: []
- id: cardiffmet/generic-2020/l3/argument/30-39.s3
  cell: cardiffmet/generic-2020/l3/argument/30-39
  span: { start: 22392, end: 22476 }
  source: "Self-evaluation and reflections on the student’s own practice are extremely limited."
  versionsFrom: none
  echoes: none
  force: describes
  terms:
    verbs: []
    objects: ["own practice"]
    degree: ["limited"]
    independence: []
    scope: []
    deficits: []
- id: cardiffmet/generic-2020/l3/argument/1-29.s1
  cell: cardiffmet/generic-2020/l3/argument/1-29
  span: { start: 22548, end: 22665 }
  source: "May demonstrate little evidence of an ability to communicate the results of their study/work accurately and reliably."
  versionsFrom: none
  echoes: { statement: qaa/fheq-2024/4.10.b4, words: 10 }
  force: describes
  terms:
    verbs: [{ lemma: "demonstrate", form: "demonstrate", taxonomy: ["bloom-r:apply/understand"] }, { lemma: "communicate", form: "communicate", taxonomy: ["none"] }]
    objects: []
    degree: ["little"]
    independence: []
    scope: []
    deficits: []
- id: cardiffmet/generic-2020/l3/argument/1-29.s2
  cell: cardiffmet/generic-2020/l3/argument/1-29
  span: { start: 22666, end: 22753 }
  source: "Self-evaluation and reflections on the student’s own practice are negligible or absent."
  versionsFrom: none
  echoes: none
  force: describes
  terms:
    verbs: []
    objects: ["own practice"]
    degree: []
    independence: []
    scope: []
    deficits: ["negligible", "absent"]
- id: cardiffmet/generic-2020/l4/overall/80-100.s1
  cell: cardiffmet/generic-2020/l4/overall/80-100
  span: { start: 22835, end: 23067 }
  source: "A full and detailed understanding of the set task and an ability to have met the learning outcomes and address the assessment criteria at an excellent level (80-89%) or outstanding and exceptional level (90-100%) and beyond level 4."
  versionsFrom: { sameAs: cardiffmet/generic-2020/l3/overall/80-100.s1 }
  echoes: none
  force: describes
  terms:
    verbs: [{ lemma: "address", form: "address", taxonomy: ["none"] }, { lemma: "meet", form: "met", taxonomy: ["none"] }]
    objects: ["understanding", "set task", "learning outcomes", "assessment criteria"]
    degree: ["detailed", "excellent", "outstanding", "exceptional"]
    independence: []
    scope: ["beyond level"]
    deficits: []
- id: cardiffmet/generic-2020/l4/overall/70-79.s1
  cell: cardiffmet/generic-2020/l4/overall/70-79
  span: { start: 23106, end: 23262 }
  source: "A full and detailed understanding of the set task and an ability to have met the learning outcomes and address the assessment criteria at a very good level."
  versionsFrom: { sameAs: cardiffmet/generic-2020/l3/overall/70-79.s1 }
  echoes: none
  force: describes
  terms:
    verbs: [{ lemma: "address", form: "address", taxonomy: ["none"] }, { lemma: "meet", form: "met", taxonomy: ["none"] }]
    objects: ["understanding", "set task", "learning outcomes", "assessment criteria"]
    degree: ["detailed", "very good"]
    independence: []
    scope: []
    deficits: []
- id: cardiffmet/generic-2020/l4/overall/60-69.s1
  cell: cardiffmet/generic-2020/l4/overall/60-69
  span: { start: 23301, end: 23439 }
  source: "A full understanding of the set task and an ability to have met the learning outcomes and address the assessment criteria at a good level."
  versionsFrom: { sameAs: cardiffmet/generic-2020/l3/overall/60-69.s1 }
  echoes: none
  force: describes
  terms:
    verbs: [{ lemma: "address", form: "address", taxonomy: ["none"] }, { lemma: "meet", form: "met", taxonomy: ["none"] }]
    objects: ["understanding", "set task", "learning outcomes", "assessment criteria"]
    degree: ["good"]
    independence: []
    scope: []
    deficits: []
- id: cardiffmet/generic-2020/l4/overall/50-59.s1
  cell: cardiffmet/generic-2020/l4/overall/50-59
  span: { start: 23478, end: 23637 }
  source: "A secure understanding of the set task and an ability to have met the associated learning outcomes and address the assessment criteria at a satisfactory level."
  versionsFrom: { sameAs: cardiffmet/generic-2020/l3/overall/50-59.s1 }
  echoes: none
  force: describes
  terms:
    verbs: [{ lemma: "address", form: "address", taxonomy: ["none"] }, { lemma: "meet", form: "met", taxonomy: ["none"] }]
    objects: ["understanding", "set task", "learning outcomes", "assessment criteria"]
    degree: ["secure", "satisfactory"]
    independence: []
    scope: []
    deficits: []
- id: cardiffmet/generic-2020/l4/overall/40-49.s1
  cell: cardiffmet/generic-2020/l4/overall/40-49
  span: { start: 23676, end: 23831 }
  source: "A basic understanding of the set task and an ability to have met the associated learning outcomes and address the assessment criteria at a threshold level."
  versionsFrom: { sameAs: cardiffmet/generic-2020/l3/overall/40-49.s1 }
  echoes: none
  force: describes
  terms:
    verbs: [{ lemma: "address", form: "address", taxonomy: ["none"] }, { lemma: "meet", form: "met", taxonomy: ["none"] }]
    objects: ["understanding", "set task", "learning outcomes", "assessment criteria"]
    degree: ["basic"]
    independence: []
    scope: ["basic"]
    deficits: []
- id: cardiffmet/generic-2020/l4/overall/30-39.s1
  cell: cardiffmet/generic-2020/l4/overall/30-39
  span: { start: 23877, end: 23900 }
  source: "Unsatisfactory overall."
  versionsFrom: { sameAs: cardiffmet/generic-2020/l3/overall/30-39.s1 }
  echoes: none
  force: describes
  terms:
    verbs: []
    objects: []
    degree: []
    independence: []
    scope: []
    deficits: []
- id: cardiffmet/generic-2020/l4/overall/30-39.s2
  cell: cardiffmet/generic-2020/l4/overall/30-39
  span: { start: 23901, end: 24026 }
  source: "A partial understanding of the set task and an ability to have met some of the associated learning outcomes at a basic level."
  versionsFrom: { sameAs: cardiffmet/generic-2020/l3/overall/30-39.s2 }
  echoes: none
  force: describes
  terms:
    verbs: [{ lemma: "meet", form: "met", taxonomy: ["none"] }]
    objects: ["understanding", "set task", "learning outcomes"]
    degree: ["some", "basic"]
    independence: []
    scope: ["basic"]
    deficits: []
- id: cardiffmet/generic-2020/l4/overall/30-39.s3
  cell: cardiffmet/generic-2020/l4/overall/30-39
  span: { start: 24027, end: 24134 }
  source: "However, attainment is uneven with some learning outcomes not met and some assessment criteria unaddressed."
  versionsFrom: { like: cardiffmet/generic-2020/l3/overall/30-39.s3, similarity: 0.97 }
  echoes: none
  force: describes
  terms:
    verbs: [{ lemma: "meet", form: "met", taxonomy: ["none"] }]
    objects: ["learning outcomes", "assessment criteria"]
    degree: ["some", "some"]
    independence: []
    scope: []
    deficits: ["not", "unaddressed"]
- id: cardiffmet/generic-2020/l4/overall/1-29.s1
  cell: cardiffmet/generic-2020/l4/overall/1-29
  span: { start: 24178, end: 24191 }
  source: "Poor overall."
  versionsFrom: { sameAs: cardiffmet/generic-2020/l3/overall/1-29.s1 }
  echoes: none
  force: describes
  terms:
    verbs: []
    objects: []
    degree: ["poor"]
    independence: []
    scope: []
    deficits: []
- id: cardiffmet/generic-2020/l4/overall/1-29.s2
  cell: cardiffmet/generic-2020/l4/overall/1-29
  span: { start: 24192, end: 24295 }
  source: "Minimal understanding of the set task and will partially have met one or two learning outcomes or none."
  versionsFrom: none
  echoes: none
  force: describes
  terms:
    verbs: [{ lemma: "meet", form: "met", taxonomy: ["none"] }]
    objects: ["understanding", "set task", "learning outcomes"]
    degree: ["minimal"]
    independence: []
    scope: []
    deficits: ["none"]
- id: cardiffmet/generic-2020/l4/overall/1-29.s3
  cell: cardiffmet/generic-2020/l4/overall/1-29
  span: { start: 24296, end: 24337 }
  source: "Many assessment criteria are unaddressed."
  versionsFrom: { sameAs: cardiffmet/generic-2020/l3/overall/1-29.s4 }
  echoes: none
  force: describes
  terms:
    verbs: []
    objects: ["assessment criteria"]
    degree: []
    independence: []
    scope: []
    deficits: ["unaddressed"]
- id: cardiffmet/generic-2020/l4/knowledge/80-100.s1
  cell: cardiffmet/generic-2020/l4/knowledge/80-100
  span: { start: 24395, end: 24496 }
  source: "Further to the 70%-79% band, work in the 80%-100% bands would extend beyond that expected at Level 4."
  versionsFrom: { sameAs: cardiffmet/generic-2020/l3/knowledge/80-100.s1 }
  echoes: none
  force: describes
  terms:
    verbs: [{ lemma: "extend", form: "extend", taxonomy: ["bloom-r:understand"] }]
    objects: []
    degree: []
    independence: []
    scope: []
    deficits: []
- id: cardiffmet/generic-2020/l4/knowledge/70-79.s1
  cell: cardiffmet/generic-2020/l4/knowledge/70-79
  span: { start: 24545, end: 24651 }
  source: "May demonstrate a detailed knowledge of the underlying aspects of the field of study relevant to the task."
  versionsFrom: none
  echoes: none
  force: describes
  terms:
    verbs: [{ lemma: "demonstrate", form: "demonstrate", taxonomy: ["bloom-r:apply/understand"] }]
    objects: ["knowledge", "field of study"]
    degree: ["detailed"]
    independence: []
    scope: []
    deficits: []
- id: cardiffmet/generic-2020/l4/knowledge/70-79.s2
  cell: cardiffmet/generic-2020/l4/knowledge/70-79
  span: { start: 24652, end: 24715 }
  source: "There is strong evidence of an ability to apply such knowledge."
  versionsFrom: { sameAs: cardiffmet/generic-2020/l3/knowledge/70-79.s2 }
  echoes: none
  force: describes
  terms:
    verbs: [{ lemma: "apply", form: "apply", taxonomy: ["bloom-r:apply", "solo:relational"] }]
    objects: ["knowledge"]
    degree: ["strong"]
    independence: []
    scope: []
    deficits: []
- id: cardiffmet/generic-2020/l4/knowledge/70-79.s3
  cell: cardiffmet/generic-2020/l4/knowledge/70-79
  span: { start: 24716, end: 24888 }
  source: "The student also demonstrates an ability to engage in confident discussion of basic concepts and an awareness of the limitations and/or ambiguity of disciplinary knowledge."
  versionsFrom: none
  echoes: none
  force: describes
  terms:
    verbs: [{ lemma: "demonstrate", form: "demonstrates", taxonomy: ["bloom-r:apply/understand"] }]
    objects: ["concepts", "limitations", "knowledge"]
    degree: ["confident"]
    independence: []
    scope: ["basic"]
    deficits: []
- id: cardiffmet/generic-2020/l4/knowledge/70-79.s4
  cell: cardiffmet/generic-2020/l4/knowledge/70-79
  span: { start: 24889, end: 24972 }
  source: "Independent thinking and original insights are also features of work at this level."
  versionsFrom: none
  echoes: none
  force: describes
  terms:
    verbs: []
    objects: []
    degree: []
    independence: ["independent thinking"]
    scope: ["original", "at this level"]
    deficits: []
- id: cardiffmet/generic-2020/l4/knowledge/60-69.s1
  cell: cardiffmet/generic-2020/l4/knowledge/60-69
  span: { start: 25021, end: 25127 }
  source: "May demonstrate a detailed knowledge of the underlying aspects of the field of study relevant to the task."
  versionsFrom: { sameAs: cardiffmet/generic-2020/l4/knowledge/70-79.s1 }
  echoes: none
  force: describes
  terms:
    verbs: [{ lemma: "demonstrate", form: "demonstrate", taxonomy: ["bloom-r:apply/understand"] }]
    objects: ["knowledge", "field of study"]
    degree: ["detailed"]
    independence: []
    scope: []
    deficits: []
- id: cardiffmet/generic-2020/l4/knowledge/60-69.s2
  cell: cardiffmet/generic-2020/l4/knowledge/60-69
  span: { start: 25128, end: 25240 }
  source: "There is clear evidence of an ability to apply such knowledge and, in some contexts, to extend and transform it."
  versionsFrom: none
  echoes: none
  force: describes
  terms:
    verbs: [{ lemma: "apply", form: "apply", taxonomy: ["bloom-r:apply", "solo:relational"] }, { lemma: "extend", form: "extend", taxonomy: ["bloom-r:understand"] }, { lemma: "transform", form: "transform", taxonomy: ["none"] }]
    objects: ["knowledge"]
    degree: ["clear", "some"]
    independence: []
    scope: []
    deficits: []
- id: cardiffmet/generic-2020/l4/knowledge/60-69.s3
  cell: cardiffmet/generic-2020/l4/knowledge/60-69
  span: { start: 25241, end: 25350 }
  source: "The discussion of basic concepts is often tackled successfully and there is evidence of independent thinking."
  versionsFrom: { sameAs: cardiffmet/generic-2020/l3/knowledge/60-69.s3 }
  echoes: none
  force: describes
  terms:
    verbs: []
    objects: ["concepts"]
    degree: ["successfully"]
    independence: ["independent thinking"]
    scope: ["basic"]
    deficits: []
- id: cardiffmet/generic-2020/l4/knowledge/50-59.s1
  cell: cardiffmet/generic-2020/l4/knowledge/50-59
  span: { start: 25399, end: 25502 }
  source: "May demonstrate a sound knowledge of the underlying aspects of the field of study relevant to the task."
  versionsFrom: none
  echoes: none
  force: describes
  terms:
    verbs: [{ lemma: "demonstrate", form: "demonstrate", taxonomy: ["bloom-r:apply/understand"] }]
    objects: ["knowledge", "field of study"]
    degree: ["sound"]
    independence: []
    scope: []
    deficits: []
- id: cardiffmet/generic-2020/l4/knowledge/50-59.s2
  cell: cardiffmet/generic-2020/l4/knowledge/50-59
  span: { start: 25503, end: 25664 }
  source: "Although there may be a tendency to rely on information received from elsewhere (e.g. programme materials), there is still some evidence of independent thinking."
  versionsFrom: { sameAs: cardiffmet/generic-2020/l3/knowledge/50-59.s2 }
  echoes: none
  force: describes
  terms:
    verbs: []
    objects: ["information"]
    degree: ["some"]
    independence: ["independent thinking"]
    scope: []
    deficits: []
- id: cardiffmet/generic-2020/l4/knowledge/50-59.s3
  cell: cardiffmet/generic-2020/l4/knowledge/50-59
  span: { start: 25665, end: 25756 }
  source: "A few errors and/or misconceptions may be present, but these will not be in important areas"
  versionsFrom: { sameAs: cardiffmet/generic-2020/l3/knowledge/50-59.s3 }
  echoes: none
  force: describes
  terms:
    verbs: [{ lemma: "present", form: "present", taxonomy: ["none"] }]
    objects: []
    degree: []
    independence: []
    scope: []
    deficits: ["errors", "misconceptions", "not"]
- id: cardiffmet/generic-2020/l4/knowledge/40-49.s1
  cell: cardiffmet/generic-2020/l4/knowledge/40-49
  span: { start: 25805, end: 25908 }
  source: "May demonstrate a basic knowledge of the underlying aspects of the field of study relevant to the task."
  versionsFrom: none
  echoes: none
  force: describes
  terms:
    verbs: [{ lemma: "demonstrate", form: "demonstrate", taxonomy: ["bloom-r:apply/understand"] }]
    objects: ["knowledge", "field of study"]
    degree: ["basic"]
    independence: []
    scope: ["basic"]
    deficits: []
- id: cardiffmet/generic-2020/l4/knowledge/40-49.s2
  cell: cardiffmet/generic-2020/l4/knowledge/40-49
  span: { start: 25909, end: 26028 }
  source: "Reproducing information received from elsewhere (e.g. programme materials) is a frequent feature of work at this level."
  versionsFrom: { sameAs: cardiffmet/generic-2020/l3/knowledge/40-49.s2 }
  echoes: none
  force: describes
  terms:
    verbs: [{ lemma: "reproduce", form: "reproducing", taxonomy: ["bloom-r:remember", "solo:unistructural"] }]
    objects: ["information"]
    degree: []
    independence: []
    scope: ["at this level"]
    deficits: []
- id: cardiffmet/generic-2020/l4/knowledge/40-49.s3
  cell: cardiffmet/generic-2020/l4/knowledge/40-49
  span: { start: 26029, end: 26163 }
  source: "Errors and misconceptions will be evident, but these are outweighed by the degree of knowledge and understanding demonstrated overall."
  versionsFrom: { sameAs: cardiffmet/generic-2020/l3/knowledge/40-49.s3 }
  echoes: none
  force: describes
  terms:
    verbs: [{ lemma: "demonstrate", form: "demonstrated", taxonomy: ["bloom-r:apply/understand"] }]
    objects: ["knowledge and understanding"]
    degree: []
    independence: []
    scope: []
    deficits: ["errors", "misconceptions"]
- id: cardiffmet/generic-2020/l4/knowledge/30-39.s1
  cell: cardiffmet/generic-2020/l4/knowledge/30-39
  span: { start: 26219, end: 26340 }
  source: "May demonstrate limited knowledge and understanding of the underlying aspects of the field of study relevant to the task."
  versionsFrom: none
  echoes: none
  force: describes
  terms:
    verbs: [{ lemma: "demonstrate", form: "demonstrate", taxonomy: ["bloom-r:apply/understand"] }]
    objects: ["knowledge and understanding", "field of study"]
    degree: ["limited"]
    independence: []
    scope: []
    deficits: []
- id: cardiffmet/generic-2020/l4/knowledge/30-39.s2
  cell: cardiffmet/generic-2020/l4/knowledge/30-39
  span: { start: 26341, end: 26484 }
  source: "Factual inaccuracies, errors and misconceptions are evident in important areas and elements of the assessed work may be irrelevant to the task."
  versionsFrom: { sameAs: cardiffmet/generic-2020/l3/knowledge/30-39.s2 }
  echoes: none
  force: describes
  terms:
    verbs: []
    objects: []
    degree: []
    independence: []
    scope: []
    deficits: ["inaccuracies", "errors", "misconceptions", "irrelevant"]
- id: cardiffmet/generic-2020/l4/knowledge/1-29.s1
  cell: cardiffmet/generic-2020/l4/knowledge/1-29
  span: { start: 26538, end: 26658 }
  source: "May demonstrate little knowledge and understanding of the underlying aspects of the field of study relevant to the task."
  versionsFrom: none
  echoes: none
  force: describes
  terms:
    verbs: [{ lemma: "demonstrate", form: "demonstrate", taxonomy: ["bloom-r:apply/understand"] }]
    objects: ["knowledge and understanding", "field of study"]
    degree: ["little"]
    independence: []
    scope: []
    deficits: []
- id: cardiffmet/generic-2020/l4/knowledge/1-29.s2
  cell: cardiffmet/generic-2020/l4/knowledge/1-29
  span: { start: 26659, end: 26817 }
  source: "Factual inaccuracies, errors and misconceptions are evident in many important areas and these outweigh the degree of knowledge and understanding demonstrated."
  versionsFrom: { sameAs: cardiffmet/generic-2020/l3/knowledge/1-29.s2 }
  echoes: none
  force: describes
  terms:
    verbs: [{ lemma: "demonstrate", form: "demonstrated", taxonomy: ["bloom-r:apply/understand"] }]
    objects: ["knowledge and understanding"]
    degree: []
    independence: []
    scope: []
    deficits: ["inaccuracies", "errors", "misconceptions"]
- id: cardiffmet/generic-2020/l4/knowledge/1-29.s3
  cell: cardiffmet/generic-2020/l4/knowledge/1-29
  span: { start: 26818, end: 26890 }
  source: "Substantial elements of the assessed work may be irrelevant to the task."
  versionsFrom: { sameAs: cardiffmet/generic-2020/l3/knowledge/1-29.s3 }
  echoes: none
  force: describes
  terms:
    verbs: []
    objects: []
    degree: []
    independence: []
    scope: []
    deficits: ["irrelevant"]
- id: cardiffmet/generic-2020/l4/presentation/80-100.s1
  cell: cardiffmet/generic-2020/l4/presentation/80-100
  span: { start: 26953, end: 27054 }
  source: "Further to the 70%-79% band, work in the 80%-100% bands would extend beyond that expected at Level 4."
  versionsFrom: { sameAs: cardiffmet/generic-2020/l3/knowledge/80-100.s1 }
  echoes: none
  force: describes
  terms:
    verbs: [{ lemma: "extend", form: "extend", taxonomy: ["bloom-r:understand"] }]
    objects: []
    degree: []
    independence: []
    scope: []
    deficits: []
- id: cardiffmet/generic-2020/l4/presentation/70-79.s1
  cell: cardiffmet/generic-2020/l4/presentation/70-79
  span: { start: 27108, end: 27345 }
  source: "May demonstrate an ability to present, evaluate and interpret qualitative and quantitative data, in order to develop lines of argument and make sound judgements in accordance with basic theories and concepts of their subject(s) of study."
  versionsFrom: { sameAs: cardiffmet/generic-2020/l3/presentation/70-79.s1 }
  echoes: { statement: qaa/fheq-2024/4.10.b2, words: 35 }
  force: describes
  terms:
    verbs: [{ lemma: "demonstrate", form: "demonstrate", taxonomy: ["bloom-r:apply/understand"] }, { lemma: "interpret", form: "interpret", taxonomy: ["bloom-r:apply/evaluate/understand", "solo:extended-abstract/relational"] }, { lemma: "evaluate", form: "evaluate", taxonomy: ["bloom-r:analyze/create/evaluate", "solo:extended-abstract"] }, { lemma: "develop", form: "develop", taxonomy: ["bloom-r:apply/create"] }, { lemma: "make", form: "make", taxonomy: ["bloom-r:create"] }, { lemma: "present", form: "present", taxonomy: ["none"] }]
    objects: ["qualitative and quantitative data", "lines of argument", "basic theories and concepts"]
    degree: ["sound"]
    independence: []
    scope: ["basic"]
    deficits: []
- id: cardiffmet/generic-2020/l4/presentation/70-79.s2
  cell: cardiffmet/generic-2020/l4/presentation/70-79
  span: { start: 27346, end: 27410 }
  source: "The standard of presentation is high and the format appropriate."
  versionsFrom: { sameAs: cardiffmet/generic-2020/l3/presentation/70-79.s2 }
  echoes: none
  force: describes
  terms:
    verbs: [{ lemma: "present", form: "presentation", taxonomy: ["none"] }]
    objects: ["presentation"]
    degree: ["high"]
    independence: []
    scope: []
    deficits: []
- id: cardiffmet/generic-2020/l4/presentation/70-79.s3
  cell: cardiffmet/generic-2020/l4/presentation/70-79
  span: { start: 27411, end: 27486 }
  source: "Key points are logically organised and in written work, the style is lucid."
  versionsFrom: { sameAs: cardiffmet/generic-2020/l3/presentation/70-79.s3 }
  echoes: none
  force: describes
  terms:
    verbs: []
    objects: []
    degree: []
    independence: []
    scope: ["key"]
    deficits: []
- id: cardiffmet/generic-2020/l4/presentation/70-79.s4
  cell: cardiffmet/generic-2020/l4/presentation/70-79
  span: { start: 27487, end: 27563 }
  source: "Arguments are well-defined and clearly articulated, structured and coherent."
  versionsFrom: none
  echoes: none
  force: describes
  terms:
    verbs: []
    objects: ["arguments"]
    degree: ["clearly"]
    independence: []
    scope: ["well-defined"]
    deficits: []
- id: cardiffmet/generic-2020/l4/presentation/60-69.s1
  cell: cardiffmet/generic-2020/l4/presentation/60-69
  span: { start: 27617, end: 27854 }
  source: "May demonstrate an ability to present, evaluate and interpret qualitative and quantitative data, in order to develop lines of argument and make sound judgements in accordance with basic theories and concepts of their subject(s) of study."
  versionsFrom: { sameAs: cardiffmet/generic-2020/l3/presentation/70-79.s1 }
  echoes: { statement: qaa/fheq-2024/4.10.b2, words: 35 }
  force: describes
  terms:
    verbs: [{ lemma: "demonstrate", form: "demonstrate", taxonomy: ["bloom-r:apply/understand"] }, { lemma: "interpret", form: "interpret", taxonomy: ["bloom-r:apply/evaluate/understand", "solo:extended-abstract/relational"] }, { lemma: "evaluate", form: "evaluate", taxonomy: ["bloom-r:analyze/create/evaluate", "solo:extended-abstract"] }, { lemma: "develop", form: "develop", taxonomy: ["bloom-r:apply/create"] }, { lemma: "make", form: "make", taxonomy: ["bloom-r:create"] }, { lemma: "present", form: "present", taxonomy: ["none"] }]
    objects: ["qualitative and quantitative data", "lines of argument", "basic theories and concepts"]
    degree: ["sound"]
    independence: []
    scope: ["basic"]
    deficits: []
- id: cardiffmet/generic-2020/l4/presentation/60-69.s2
  cell: cardiffmet/generic-2020/l4/presentation/60-69
  span: { start: 27855, end: 27905 }
  source: "Work is well presented and the format appropriate."
  versionsFrom: { sameAs: cardiffmet/generic-2020/l3/presentation/60-69.s2 }
  echoes: none
  force: describes
  terms:
    verbs: []
    objects: []
    degree: ["well"]
    independence: []
    scope: []
    deficits: []
- id: cardiffmet/generic-2020/l4/presentation/60-69.s3
  cell: cardiffmet/generic-2020/l4/presentation/60-69
  span: { start: 27906, end: 28054 }
  source: "Key points are appropriately organised and in written work, the writing style is fluent and arguments are well articulated, structured and coherent."
  versionsFrom: none
  echoes: none
  force: describes
  terms:
    verbs: []
    objects: ["arguments"]
    degree: ["well"]
    independence: []
    scope: ["key"]
    deficits: []
- id: cardiffmet/generic-2020/l4/presentation/50-59.s1
  cell: cardiffmet/generic-2020/l4/presentation/50-59
  span: { start: 28108, end: 28347 }
  source: "May demonstrate some ability to present, evaluate and interpret qualitative and quantitative data, in order to develop lines of argument and make sound judgements in accordance with basic theories and concepts of their subject(s) of study."
  versionsFrom: { sameAs: cardiffmet/generic-2020/l3/presentation/50-59.s1 }
  echoes: { statement: qaa/fheq-2024/4.10.b2, words: 34 }
  force: describes
  terms:
    verbs: [{ lemma: "demonstrate", form: "demonstrate", taxonomy: ["bloom-r:apply/understand"] }, { lemma: "interpret", form: "interpret", taxonomy: ["bloom-r:apply/evaluate/understand", "solo:extended-abstract/relational"] }, { lemma: "evaluate", form: "evaluate", taxonomy: ["bloom-r:analyze/create/evaluate", "solo:extended-abstract"] }, { lemma: "develop", form: "develop", taxonomy: ["bloom-r:apply/create"] }, { lemma: "make", form: "make", taxonomy: ["bloom-r:create"] }, { lemma: "present", form: "present", taxonomy: ["none"] }]
    objects: ["qualitative and quantitative data", "lines of argument", "basic theories and concepts"]
    degree: ["some", "sound"]
    independence: []
    scope: ["basic"]
    deficits: []
- id: cardiffmet/generic-2020/l4/presentation/50-59.s2
  cell: cardiffmet/generic-2020/l4/presentation/50-59
  span: { start: 28348, end: 28410 }
  source: "Overall, the structure and format of the work are appropriate."
  versionsFrom: { sameAs: cardiffmet/generic-2020/l3/presentation/50-59.s2 }
  echoes: none
  force: describes
  terms:
    verbs: []
    objects: ["structure"]
    degree: []
    independence: []
    scope: []
    deficits: []
- id: cardiffmet/generic-2020/l4/presentation/50-59.s3
  cell: cardiffmet/generic-2020/l4/presentation/50-59
  span: { start: 28411, end: 28535 }
  source: "There may be occasional faults in the presentation of work but overall, these do not detract from the clarity of expression."
  versionsFrom: { sameAs: cardiffmet/generic-2020/l3/presentation/50-59.s3 }
  echoes: none
  force: describes
  terms:
    verbs: [{ lemma: "present", form: "presentation", taxonomy: ["none"] }]
    objects: ["presentation"]
    degree: []
    independence: []
    scope: []
    deficits: ["not"]
- id: cardiffmet/generic-2020/l4/presentation/40-49.s1
  cell: cardiffmet/generic-2020/l4/presentation/40-49
  span: { start: 28589, end: 28831 }
  source: "May demonstrate limited ability to present, evaluate and interpret qualitative and quantitative data, in order to develop lines of argument and make sound judgements in accordance with basic theories and concepts of their subject(s) of study."
  versionsFrom: { sameAs: cardiffmet/generic-2020/l3/presentation/40-49.s1 }
  echoes: { statement: qaa/fheq-2024/4.10.b2, words: 34 }
  force: describes
  terms:
    verbs: [{ lemma: "demonstrate", form: "demonstrate", taxonomy: ["bloom-r:apply/understand"] }, { lemma: "interpret", form: "interpret", taxonomy: ["bloom-r:apply/evaluate/understand", "solo:extended-abstract/relational"] }, { lemma: "evaluate", form: "evaluate", taxonomy: ["bloom-r:analyze/create/evaluate", "solo:extended-abstract"] }, { lemma: "develop", form: "develop", taxonomy: ["bloom-r:apply/create"] }, { lemma: "make", form: "make", taxonomy: ["bloom-r:create"] }, { lemma: "present", form: "present", taxonomy: ["none"] }]
    objects: ["qualitative and quantitative data", "lines of argument", "basic theories and concepts"]
    degree: ["limited", "sound"]
    independence: []
    scope: ["basic"]
    deficits: []
- id: cardiffmet/generic-2020/l4/presentation/40-49.s2
  cell: cardiffmet/generic-2020/l4/presentation/40-49
  span: { start: 28832, end: 28954 }
  source: "However, more success is achieved in describing and reporting factual information rather than communicating complex ideas."
  versionsFrom: { sameAs: cardiffmet/generic-2020/l3/presentation/40-49.s2 }
  echoes: none
  force: describes
  terms:
    verbs: [{ lemma: "communicate", form: "communicating", taxonomy: ["none"] }, { lemma: "describe", form: "describing", taxonomy: ["bloom-r:evaluate/remember/understand", "solo:multistructural"] }, { lemma: "report", form: "reporting", taxonomy: ["bloom-r:apply/understand", "solo:multistructural"] }]
    objects: ["information", "ideas"]
    degree: []
    independence: []
    scope: ["complex"]
    deficits: []
- id: cardiffmet/generic-2020/l4/presentation/40-49.s3
  cell: cardiffmet/generic-2020/l4/presentation/40-49
  span: { start: 28955, end: 29054 }
  source: "Generally, the work is appropriately structured although key points may not be logically sequenced."
  versionsFrom: { sameAs: cardiffmet/generic-2020/l3/presentation/40-49.s3 }
  echoes: none
  force: describes
  terms:
    verbs: []
    objects: []
    degree: ["generally"]
    independence: []
    scope: ["key"]
    deficits: ["not"]
- id: cardiffmet/generic-2020/l4/presentation/40-49.s4
  cell: cardiffmet/generic-2020/l4/presentation/40-49
  span: { start: 29055, end: 29141 }
  source: "Although there will be faults in the presentation of work, the meaning is still clear."
  versionsFrom: { sameAs: cardiffmet/generic-2020/l3/presentation/40-49.s4 }
  echoes: none
  force: describes
  terms:
    verbs: [{ lemma: "present", form: "presentation", taxonomy: ["none"] }]
    objects: ["presentation"]
    degree: ["clear"]
    independence: []
    scope: []
    deficits: []
- id: cardiffmet/generic-2020/l4/presentation/30-39.s1
  cell: cardiffmet/generic-2020/l4/presentation/30-39
  span: { start: 29202, end: 29303 }
  source: "May demonstrate limited ability to present, evaluate and interpret qualitative and quantitative data."
  versionsFrom: { sameAs: cardiffmet/generic-2020/l3/presentation/30-39.s1 }
  echoes: { statement: qaa/fheq-2024/4.10.b2, words: 10 }
  force: describes
  terms:
    verbs: [{ lemma: "demonstrate", form: "demonstrate", taxonomy: ["bloom-r:apply/understand"] }, { lemma: "interpret", form: "interpret", taxonomy: ["bloom-r:apply/evaluate/understand", "solo:extended-abstract/relational"] }, { lemma: "evaluate", form: "evaluate", taxonomy: ["bloom-r:analyze/create/evaluate", "solo:extended-abstract"] }, { lemma: "present", form: "present", taxonomy: ["none"] }]
    objects: ["qualitative and quantitative data"]
    degree: ["limited"]
    independence: []
    scope: []
    deficits: []
- id: cardiffmet/generic-2020/l4/presentation/30-39.s2
  cell: cardiffmet/generic-2020/l4/presentation/30-39
  span: { start: 29304, end: 29396 }
  source: "Ideas may not be communicated clearly and present comprehension difficulties for the reader."
  versionsFrom: { sameAs: cardiffmet/generic-2020/l3/presentation/30-39.s2 }
  echoes: none
  force: describes
  terms:
    verbs: [{ lemma: "present", form: "present", taxonomy: ["none"] }]
    objects: ["ideas"]
    degree: ["clearly"]
    independence: []
    scope: []
    deficits: ["not"]
- id: cardiffmet/generic-2020/l4/presentation/30-39.s3
  cell: cardiffmet/generic-2020/l4/presentation/30-39
  span: { start: 29397, end: 29503 }
  source: "If attempted, the presentation of arguments and more complex ideas may be confused and clumsily expressed."
  versionsFrom: { sameAs: cardiffmet/generic-2020/l3/presentation/30-39.s3 }
  echoes: none
  force: describes
  terms:
    verbs: [{ lemma: "present", form: "presentation", taxonomy: ["none"] }]
    objects: ["presentation", "arguments", "ideas"]
    degree: []
    independence: []
    scope: ["complex"]
    deficits: ["confused"]
- id: cardiffmet/generic-2020/l4/presentation/1-29.s1
  cell: cardiffmet/generic-2020/l4/presentation/1-29
  span: { start: 29562, end: 29662 }
  source: "May demonstrate little ability to present, evaluate and interpret qualitative and quantitative data."
  versionsFrom: { sameAs: cardiffmet/generic-2020/l3/presentation/1-29.s1 }
  echoes: { statement: qaa/fheq-2024/4.10.b2, words: 10 }
  force: describes
  terms:
    verbs: [{ lemma: "demonstrate", form: "demonstrate", taxonomy: ["bloom-r:apply/understand"] }, { lemma: "interpret", form: "interpret", taxonomy: ["bloom-r:apply/evaluate/understand", "solo:extended-abstract/relational"] }, { lemma: "evaluate", form: "evaluate", taxonomy: ["bloom-r:analyze/create/evaluate", "solo:extended-abstract"] }, { lemma: "present", form: "present", taxonomy: ["none"] }]
    objects: ["qualitative and quantitative data"]
    degree: ["little"]
    independence: []
    scope: []
    deficits: []
- id: cardiffmet/generic-2020/l4/presentation/1-29.s2
  cell: cardiffmet/generic-2020/l4/presentation/1-29
  span: { start: 29663, end: 29815 }
  source: "Frequent faults in the presentation of work and significant difficulties in its structure and organisation detract from the clarity and meaning overall."
  versionsFrom: { sameAs: cardiffmet/generic-2020/l3/presentation/1-29.s2 }
  echoes: none
  force: describes
  terms:
    verbs: [{ lemma: "present", form: "presentation", taxonomy: ["none"] }]
    objects: ["presentation", "structure"]
    degree: []
    independence: []
    scope: []
    deficits: []
- id: cardiffmet/generic-2020/l4/presentation/1-29.s3
  cell: cardiffmet/generic-2020/l4/presentation/1-29
  span: { start: 29816, end: 29868 }
  source: "The writing style is often clumsy and inappropriate."
  versionsFrom: { sameAs: cardiffmet/generic-2020/l3/presentation/1-29.s3 }
  echoes: none
  force: describes
  terms:
    verbs: []
    objects: []
    degree: []
    independence: []
    scope: []
    deficits: ["clumsy"]
- id: cardiffmet/generic-2020/l4/analysis/80-100.s1
  cell: cardiffmet/generic-2020/l4/analysis/80-100
  span: { start: 29922, end: 30023 }
  source: "Further to the 70%-79% band, work in the 80%-100% bands would extend beyond that expected at Level 4."
  versionsFrom: { sameAs: cardiffmet/generic-2020/l3/knowledge/80-100.s1 }
  echoes: none
  force: describes
  terms:
    verbs: [{ lemma: "extend", form: "extend", taxonomy: ["bloom-r:understand"] }]
    objects: []
    degree: []
    independence: []
    scope: []
    deficits: []
- id: cardiffmet/generic-2020/l4/analysis/70-79.s1
  cell: cardiffmet/generic-2020/l4/analysis/70-79
  span: { start: 30068, end: 30240 }
  source: "May demonstrate an ability to evaluate the appropriateness of different approaches to solving well-defined, complex and non-routine problems related to their area of study."
  versionsFrom: none
  echoes: { statement: qaa/fheq-2024/4.10.b3, words: 8 }
  force: describes
  terms:
    verbs: [{ lemma: "demonstrate", form: "demonstrate", taxonomy: ["bloom-r:apply/understand"] }, { lemma: "evaluate", form: "evaluate", taxonomy: ["bloom-r:analyze/create/evaluate", "solo:extended-abstract"] }, { lemma: "solve", form: "solving", taxonomy: ["bloom-r:analyze/apply/create", "solo:multistructural"] }]
    objects: ["approaches", "problems"]
    degree: []
    independence: []
    scope: ["well-defined", "complex", "non-routine"]
    deficits: []
- id: cardiffmet/generic-2020/l4/analysis/70-79.s2
  cell: cardiffmet/generic-2020/l4/analysis/70-79
  span: { start: 30241, end: 30421 }
  source: "The student is highly successful in presenting and commenting on outcomes and is able to comment perceptively and with some insight on the relationship between theory and practice."
  versionsFrom: none
  echoes: none
  force: describes
  terms:
    verbs: [{ lemma: "comment", form: "comment", taxonomy: ["none"] }, { lemma: "present", form: "presenting", taxonomy: ["none"] }]
    objects: ["theory and practice"]
    degree: ["highly", "successful", "perceptively", "some"]
    independence: []
    scope: []
    deficits: []
- id: cardiffmet/generic-2020/l4/analysis/60-69.s1
  cell: cardiffmet/generic-2020/l4/analysis/60-69
  span: { start: 30466, end: 30748 }
  source: "May demonstrate an ability to evaluate the appropriateness of different approaches to solving well-defined, complex and non-routine problems related to their area of study by making use of appropriate techniques and has considerable success in presenting and commenting on outcomes."
  versionsFrom: none
  echoes: { statement: qaa/fheq-2024/4.10.b3, words: 8 }
  force: describes
  terms:
    verbs: [{ lemma: "demonstrate", form: "demonstrate", taxonomy: ["bloom-r:apply/understand"] }, { lemma: "comment", form: "commenting", taxonomy: ["none"] }, { lemma: "evaluate", form: "evaluate", taxonomy: ["bloom-r:analyze/create/evaluate", "solo:extended-abstract"] }, { lemma: "use", form: "use", taxonomy: ["bloom-r:apply"] }, { lemma: "make", form: "making", taxonomy: ["bloom-r:create"] }, { lemma: "present", form: "presenting", taxonomy: ["none"] }, { lemma: "solve", form: "solving", taxonomy: ["bloom-r:analyze/apply/create", "solo:multistructural"] }]
    objects: ["approaches", "problems", "techniques"]
    degree: []
    independence: []
    scope: ["well-defined", "complex", "non-routine"]
    deficits: []
- id: cardiffmet/generic-2020/l4/analysis/60-69.s2
  cell: cardiffmet/generic-2020/l4/analysis/60-69
  span: { start: 30749, end: 30799 }
  source: "There is some linkage between theory and practice."
  versionsFrom: none
  echoes: none
  force: describes
  terms:
    verbs: []
    objects: ["theory and practice"]
    degree: ["some"]
    independence: []
    scope: []
    deficits: []
- id: cardiffmet/generic-2020/l4/analysis/50-59.s1
  cell: cardiffmet/generic-2020/l4/analysis/50-59
  span: { start: 30844, end: 31083 }
  source: "May demonstrate an ability to evaluate the appropriateness of different approaches to solving well-defined, complex and non-routine problems related to their area of study and generally has success in presenting and commenting on outcomes."
  versionsFrom: none
  echoes: { statement: qaa/fheq-2024/4.10.b3, words: 8 }
  force: describes
  terms:
    verbs: [{ lemma: "demonstrate", form: "demonstrate", taxonomy: ["bloom-r:apply/understand"] }, { lemma: "comment", form: "commenting", taxonomy: ["none"] }, { lemma: "evaluate", form: "evaluate", taxonomy: ["bloom-r:analyze/create/evaluate", "solo:extended-abstract"] }, { lemma: "present", form: "presenting", taxonomy: ["none"] }, { lemma: "solve", form: "solving", taxonomy: ["bloom-r:analyze/apply/create", "solo:multistructural"] }]
    objects: ["approaches", "problems"]
    degree: ["generally"]
    independence: []
    scope: ["well-defined", "complex", "non-routine"]
    deficits: []
- id: cardiffmet/generic-2020/l4/analysis/40-49.s1
  cell: cardiffmet/generic-2020/l4/analysis/40-49
  span: { start: 31128, end: 31377 }
  source: "May demonstrate a limited ability to evaluate the appropriateness of different approaches to solving well-defined, complex and non-routine problems related to their area of study and has intermittent success in presenting and commenting on outcomes."
  versionsFrom: none
  echoes: { statement: qaa/fheq-2024/4.10.b3, words: 8 }
  force: describes
  terms:
    verbs: [{ lemma: "demonstrate", form: "demonstrate", taxonomy: ["bloom-r:apply/understand"] }, { lemma: "comment", form: "commenting", taxonomy: ["none"] }, { lemma: "evaluate", form: "evaluate", taxonomy: ["bloom-r:analyze/create/evaluate", "solo:extended-abstract"] }, { lemma: "present", form: "presenting", taxonomy: ["none"] }, { lemma: "solve", form: "solving", taxonomy: ["bloom-r:analyze/apply/create", "solo:multistructural"] }]
    objects: ["approaches", "problems"]
    degree: ["limited"]
    independence: []
    scope: ["well-defined", "complex", "non-routine"]
    deficits: []
- id: cardiffmet/generic-2020/l4/analysis/30-39.s1
  cell: cardiffmet/generic-2020/l4/analysis/30-39
  span: { start: 31429, end: 31666 }
  source: "May demonstrate a limited ability to evaluate the appropriateness of different approaches to solving well-defined, complex and non-routine problems related to their area of study but outcomes may be naïve, simplistic and/or unconvincing."
  versionsFrom: none
  echoes: { statement: qaa/fheq-2024/4.10.b3, words: 8 }
  force: describes
  terms:
    verbs: [{ lemma: "demonstrate", form: "demonstrate", taxonomy: ["bloom-r:apply/understand"] }, { lemma: "evaluate", form: "evaluate", taxonomy: ["bloom-r:analyze/create/evaluate", "solo:extended-abstract"] }, { lemma: "solve", form: "solving", taxonomy: ["bloom-r:analyze/apply/create", "solo:multistructural"] }]
    objects: ["approaches", "problems"]
    degree: ["limited"]
    independence: []
    scope: ["well-defined", "complex", "non-routine"]
    deficits: ["naïve", "simplistic", "unconvincing"]
- id: cardiffmet/generic-2020/l4/analysis/1-29.s1
  cell: cardiffmet/generic-2020/l4/analysis/1-29
  span: { start: 31716, end: 31892 }
  source: "May demonstrate little ability to evaluate the appropriateness of different approaches to solving well-defined, complex and non-routine problems related to their area of study."
  versionsFrom: none
  echoes: { statement: qaa/fheq-2024/4.10.b3, words: 8 }
  force: describes
  terms:
    verbs: [{ lemma: "demonstrate", form: "demonstrate", taxonomy: ["bloom-r:apply/understand"] }, { lemma: "evaluate", form: "evaluate", taxonomy: ["bloom-r:analyze/create/evaluate", "solo:extended-abstract"] }, { lemma: "solve", form: "solving", taxonomy: ["bloom-r:analyze/apply/create", "solo:multistructural"] }]
    objects: ["approaches", "problems"]
    degree: ["little"]
    independence: []
    scope: ["well-defined", "complex", "non-routine"]
    deficits: []
- id: cardiffmet/generic-2020/l4/analysis/1-29.s2
  cell: cardiffmet/generic-2020/l4/analysis/1-29
  span: { start: 31893, end: 31970 }
  source: "Where such work has been attempted, outcomes may be inappropriate, or absent."
  versionsFrom: { sameAs: cardiffmet/generic-2020/l3/analysis/1-29.s2 }
  echoes: none
  force: describes
  terms:
    verbs: []
    objects: []
    degree: []
    independence: []
    scope: []
    deficits: ["absent"]
- id: cardiffmet/generic-2020/l4/research/80-100.s1
  cell: cardiffmet/generic-2020/l4/research/80-100
  span: { start: 32025, end: 32126 }
  source: "Further to the 70%-79% band, work in the 80%-100% bands would extend beyond that expected at Level 4."
  versionsFrom: { sameAs: cardiffmet/generic-2020/l3/knowledge/80-100.s1 }
  echoes: none
  force: describes
  terms:
    verbs: [{ lemma: "extend", form: "extend", taxonomy: ["bloom-r:understand"] }]
    objects: []
    degree: []
    independence: []
    scope: []
    deficits: []
- id: cardiffmet/generic-2020/l4/research/70-79.s1
  cell: cardiffmet/generic-2020/l4/research/70-79
  span: { start: 32172, end: 32260 }
  source: "May demonstrate an awareness of current research/advanced scholarship in the discipline."
  versionsFrom: { sameAs: cardiffmet/generic-2020/l3/research/70-79.s1 }
  echoes: none
  force: describes
  terms:
    verbs: [{ lemma: "demonstrate", form: "demonstrate", taxonomy: ["bloom-r:apply/understand"] }]
    objects: ["research", "scholarship", "discipline"]
    degree: []
    independence: []
    scope: ["current", "advanced"]
    deficits: []
- id: cardiffmet/generic-2020/l4/research/70-79.s2
  cell: cardiffmet/generic-2020/l4/research/70-79
  span: { start: 32261, end: 32435 }
  source: "The use of scholarly reviews/primary sources is confident and a breadth and depth of individual reading and investigation, extending beyond the sources provided, is apparent."
  versionsFrom: none
  echoes: none
  force: describes
  terms:
    verbs: [{ lemma: "use", form: "use", taxonomy: ["bloom-r:apply"] }]
    objects: ["primary sources", "reading", "sources"]
    degree: ["confident"]
    independence: []
    scope: []
    deficits: []
- id: cardiffmet/generic-2020/l4/research/70-79.s3
  cell: cardiffmet/generic-2020/l4/research/70-79
  span: { start: 32436, end: 32534 }
  source: "The referencing of literature and other sources is accurate and in line with academic conventions."
  versionsFrom: { sameAs: cardiffmet/generic-2020/l3/research/70-79.s3 }
  echoes: none
  force: describes
  terms:
    verbs: []
    objects: ["referencing", "literature", "sources", "academic conventions"]
    degree: []
    independence: []
    scope: []
    deficits: []
- id: cardiffmet/generic-2020/l4/research/70-79.s4
  cell: cardiffmet/generic-2020/l4/research/70-79
  span: { start: 32535, end: 32725 }
  source: "A knowledge and understanding of research processes, techniques and methods is demonstrated along with an ability to apply research knowledge and skills successfully in appropriate contexts."
  versionsFrom: { sameAs: cardiffmet/generic-2020/l3/research/70-79.s4 }
  echoes: none
  force: describes
  terms:
    verbs: [{ lemma: "demonstrate", form: "demonstrated", taxonomy: ["bloom-r:apply/understand"] }, { lemma: "apply", form: "apply", taxonomy: ["bloom-r:apply", "solo:relational"] }]
    objects: ["knowledge and understanding", "research processes", "techniques", "research", "knowledge"]
    degree: ["successfully"]
    independence: []
    scope: []
    deficits: []
- id: cardiffmet/generic-2020/l4/research/60-69.s1
  cell: cardiffmet/generic-2020/l4/research/60-69
  span: { start: 32771, end: 32859 }
  source: "May demonstrate an awareness of current research/advanced scholarship in the discipline."
  versionsFrom: { sameAs: cardiffmet/generic-2020/l3/research/70-79.s1 }
  echoes: none
  force: describes
  terms:
    verbs: [{ lemma: "demonstrate", form: "demonstrate", taxonomy: ["bloom-r:apply/understand"] }]
    objects: ["research", "scholarship", "discipline"]
    degree: []
    independence: []
    scope: ["current", "advanced"]
    deficits: []
- id: cardiffmet/generic-2020/l4/research/60-69.s2
  cell: cardiffmet/generic-2020/l4/research/60-69
  span: { start: 32860, end: 32990 }
  source: "Examples referred to indicate a breadth and depth of individual reading and investigation that extend beyond the sources provided."
  versionsFrom: none
  echoes: none
  force: describes
  terms:
    verbs: [{ lemma: "extend", form: "extend", taxonomy: ["bloom-r:understand"] }]
    objects: ["reading", "sources"]
    degree: []
    independence: []
    scope: []
    deficits: []
- id: cardiffmet/generic-2020/l4/research/60-69.s3
  cell: cardiffmet/generic-2020/l4/research/60-69
  span: { start: 32991, end: 33065 }
  source: "The referencing of literature and other sources is almost always accurate."
  versionsFrom: { sameAs: cardiffmet/generic-2020/l3/research/60-69.s3 }
  echoes: none
  force: describes
  terms:
    verbs: []
    objects: ["referencing", "literature", "sources"]
    degree: []
    independence: []
    scope: []
    deficits: []
- id: cardiffmet/generic-2020/l4/research/60-69.s4
  cell: cardiffmet/generic-2020/l4/research/60-69
  span: { start: 33066, end: 33207 }
  source: "A secure knowledge of research processes is evident, along with an ability to apply research skills and knowledge in the appropriate context."
  versionsFrom: { like: cardiffmet/generic-2020/l3/research/60-69.s4, similarity: 0.95 }
  echoes: none
  force: describes
  terms:
    verbs: [{ lemma: "apply", form: "apply", taxonomy: ["bloom-r:apply", "solo:relational"] }]
    objects: ["knowledge", "research processes", "research", "knowledge"]
    degree: ["secure"]
    independence: []
    scope: []
    deficits: []
- id: cardiffmet/generic-2020/l4/research/50-59.s1
  cell: cardiffmet/generic-2020/l4/research/50-59
  span: { start: 33253, end: 33343 }
  source: "May demonstrate some awareness of current research/advanced scholarship in the discipline."
  versionsFrom: { sameAs: cardiffmet/generic-2020/l3/research/50-59.s1 }
  echoes: none
  force: describes
  terms:
    verbs: [{ lemma: "demonstrate", form: "demonstrate", taxonomy: ["bloom-r:apply/understand"] }]
    objects: ["research", "scholarship", "discipline"]
    degree: ["some"]
    independence: []
    scope: ["current", "advanced"]
    deficits: []
- id: cardiffmet/generic-2020/l4/research/50-59.s2
  cell: cardiffmet/generic-2020/l4/research/50-59
  span: { start: 33344, end: 33450 }
  source: "Examples of research/scholarship referred to in the work demonstrate individual reading and investigation."
  versionsFrom: { like: cardiffmet/generic-2020/l3/research/50-59.s2, similarity: 0.97 }
  echoes: none
  force: describes
  terms:
    verbs: [{ lemma: "demonstrate", form: "demonstrate", taxonomy: ["bloom-r:apply/understand"] }]
    objects: ["research", "scholarship", "reading"]
    degree: []
    independence: []
    scope: []
    deficits: []
- id: cardiffmet/generic-2020/l4/research/50-59.s3
  cell: cardiffmet/generic-2020/l4/research/50-59
  span: { start: 33451, end: 33535 }
  source: "Occasional errors may be present in the referencing of literature and other sources."
  versionsFrom: { sameAs: cardiffmet/generic-2020/l3/research/50-59.s3 }
  echoes: none
  force: describes
  terms:
    verbs: [{ lemma: "present", form: "present", taxonomy: ["none"] }]
    objects: ["referencing", "literature", "sources"]
    degree: []
    independence: []
    scope: []
    deficits: ["errors"]
- id: cardiffmet/generic-2020/l4/research/50-59.s4
  cell: cardiffmet/generic-2020/l4/research/50-59
  span: { start: 33536, end: 33711 }
  source: "Some knowledge of research processes is evident and the application of research skills and knowledge is generally successful, although there may be a reliance on tutor support"
  versionsFrom: { sameAs: cardiffmet/generic-2020/l3/research/50-59.s4 }
  echoes: none
  force: describes
  terms:
    verbs: [{ lemma: "apply", form: "application", taxonomy: ["bloom-r:apply", "solo:relational"] }]
    objects: ["knowledge", "research processes", "research", "knowledge"]
    degree: ["some", "generally", "successful"]
    independence: ["reliance on tutor support"]
    scope: []
    deficits: ["reliance"]
- id: cardiffmet/generic-2020/l4/research/40-49.s1
  cell: cardiffmet/generic-2020/l4/research/40-49
  span: { start: 33757, end: 33850 }
  source: "May demonstrate limited awareness of current research/advanced scholarship in the discipline."
  versionsFrom: { sameAs: cardiffmet/generic-2020/l3/research/40-49.s1 }
  echoes: none
  force: describes
  terms:
    verbs: [{ lemma: "demonstrate", form: "demonstrate", taxonomy: ["bloom-r:apply/understand"] }]
    objects: ["research", "scholarship", "discipline"]
    degree: ["limited"]
    independence: []
    scope: ["current", "advanced"]
    deficits: []
- id: cardiffmet/generic-2020/l4/research/40-49.s2
  cell: cardiffmet/generic-2020/l4/research/40-49
  span: { start: 33851, end: 34010 }
  source: "Examples of research/scholarship referred to in the work may indicate an over-reliance on programme materials rather than individual reading and investigation."
  versionsFrom: { sameAs: cardiffmet/generic-2020/l3/research/40-49.s2 }
  echoes: none
  force: describes
  terms:
    verbs: []
    objects: ["research", "scholarship", "reading"]
    degree: []
    independence: []
    scope: []
    deficits: ["over-reliance"]
- id: cardiffmet/generic-2020/l4/research/40-49.s3
  cell: cardiffmet/generic-2020/l4/research/40-49
  span: { start: 34011, end: 34079 }
  source: "There are errors in the referencing of literature and other sources."
  versionsFrom: { sameAs: cardiffmet/generic-2020/l3/research/40-49.s3 }
  echoes: none
  force: describes
  terms:
    verbs: []
    objects: ["referencing", "literature", "sources"]
    degree: []
    independence: []
    scope: []
    deficits: ["errors"]
- id: cardiffmet/generic-2020/l4/research/40-49.s4
  cell: cardiffmet/generic-2020/l4/research/40-49
  span: { start: 34080, end: 34186 }
  source: "Some knowledge of research processes is evident although the application of such knowledge is less secure."
  versionsFrom: { sameAs: cardiffmet/generic-2020/l3/research/40-49.s4 }
  echoes: none
  force: describes
  terms:
    verbs: [{ lemma: "apply", form: "application", taxonomy: ["bloom-r:apply", "solo:relational"] }]
    objects: ["knowledge", "research processes", "knowledge"]
    degree: ["some", "secure"]
    independence: []
    scope: []
    deficits: []
- id: cardiffmet/generic-2020/l4/research/30-39.s1
  cell: cardiffmet/generic-2020/l4/research/30-39
  span: { start: 34239, end: 34354 }
  source: "May demonstrate limited or sporadic knowledge awareness of current research/advanced scholarship in the discipline."
  versionsFrom: { sameAs: cardiffmet/generic-2020/l3/research/30-39.s1 }
  echoes: none
  force: describes
  terms:
    verbs: [{ lemma: "demonstrate", form: "demonstrate", taxonomy: ["bloom-r:apply/understand"] }]
    objects: ["knowledge", "research", "scholarship", "discipline"]
    degree: ["limited"]
    independence: []
    scope: ["current", "advanced"]
    deficits: []
- id: cardiffmet/generic-2020/l4/research/30-39.s2
  cell: cardiffmet/generic-2020/l4/research/30-39
  span: { start: 34355, end: 34517 }
  source: "A restricted range of sources are used but overall, there is an over-reliance on programme materials with little evidence of individual reading and investigation."
  versionsFrom: { sameAs: cardiffmet/generic-2020/l3/research/30-39.s2 }
  echoes: none
  force: describes
  terms:
    verbs: [{ lemma: "use", form: "used", taxonomy: ["bloom-r:apply"] }]
    objects: ["sources", "reading"]
    degree: ["little"]
    independence: []
    scope: []
    deficits: ["over-reliance"]
- id: cardiffmet/generic-2020/l4/research/30-39.s3
  cell: cardiffmet/generic-2020/l4/research/30-39
  span: { start: 34518, end: 34595 }
  source: "There are frequent errors in the referencing of literature and other sources."
  versionsFrom: { sameAs: cardiffmet/generic-2020/l3/research/30-39.s3 }
  echoes: none
  force: describes
  terms:
    verbs: []
    objects: ["referencing", "literature", "sources"]
    degree: []
    independence: []
    scope: []
    deficits: ["errors"]
- id: cardiffmet/generic-2020/l4/research/30-39.s4
  cell: cardiffmet/generic-2020/l4/research/30-39
  span: { start: 34596, end: 34733 }
  source: "Although limited knowledge of research processes may be evident, nevertheless, the application of such knowledge is largely unsuccessful."
  versionsFrom: { like: cardiffmet/generic-2020/l3/research/30-39.s4, similarity: 0.97 }
  echoes: none
  force: describes
  terms:
    verbs: [{ lemma: "apply", form: "application", taxonomy: ["bloom-r:apply", "solo:relational"] }]
    objects: ["knowledge", "research processes", "knowledge"]
    degree: ["limited"]
    independence: []
    scope: []
    deficits: []
- id: cardiffmet/generic-2020/l4/research/1-29.s1
  cell: cardiffmet/generic-2020/l4/research/1-29
  span: { start: 34784, end: 34867 }
  source: "May demonstrate little knowledge of current research/scholarship in the discipline."
  versionsFrom: { sameAs: cardiffmet/generic-2020/l3/research/1-29.s1 }
  echoes: none
  force: describes
  terms:
    verbs: [{ lemma: "demonstrate", form: "demonstrate", taxonomy: ["bloom-r:apply/understand"] }]
    objects: ["knowledge", "research", "scholarship", "discipline"]
    degree: ["little"]
    independence: []
    scope: ["current"]
    deficits: []
- id: cardiffmet/generic-2020/l4/research/1-29.s2
  cell: cardiffmet/generic-2020/l4/research/1-29
  span: { start: 34868, end: 35016 }
  source: "Evidence of individual reading and investigation is negligible and the limited referencing of literature and other sources is frequently inaccurate."
  versionsFrom: { sameAs: cardiffmet/generic-2020/l3/research/1-29.s2 }
  echoes: none
  force: describes
  terms:
    verbs: []
    objects: ["reading", "referencing", "literature", "sources"]
    degree: ["limited"]
    independence: []
    scope: []
    deficits: ["negligible"]
- id: cardiffmet/generic-2020/l4/research/1-29.s3
  cell: cardiffmet/generic-2020/l4/research/1-29
  span: { start: 35017, end: 35120 }
  source: "Very limited knowledge of research processes is apparent and there is a failure to apply this knowledge"
  versionsFrom: { sameAs: cardiffmet/generic-2020/l3/research/1-29.s3 }
  echoes: none
  force: describes
  terms:
    verbs: [{ lemma: "apply", form: "apply", taxonomy: ["bloom-r:apply", "solo:relational"] }]
    objects: ["knowledge", "research processes", "knowledge"]
    degree: ["very limited"]
    independence: []
    scope: []
    deficits: ["failure"]
- id: cardiffmet/generic-2020/l4/argument/80-100.s1
  cell: cardiffmet/generic-2020/l4/argument/80-100
  span: { start: 35196, end: 35297 }
  source: "Further to the 70%-79% band, work in the 80%-100% bands would extend beyond that expected at Level 4."
  versionsFrom: { sameAs: cardiffmet/generic-2020/l3/knowledge/80-100.s1 }
  echoes: none
  force: describes
  terms:
    verbs: [{ lemma: "extend", form: "extend", taxonomy: ["bloom-r:understand"] }]
    objects: []
    degree: []
    independence: []
    scope: []
    deficits: []
- id: cardiffmet/generic-2020/l4/argument/70-79.s1
  cell: cardiffmet/generic-2020/l4/argument/70-79
  span: { start: 35364, end: 35501 }
  source: "May demonstrate an ability to communicate the results of their study/work accurately and reliably with structured and coherent arguments."
  versionsFrom: none
  echoes: { statement: qaa/fheq-2024/4.10.b4, words: 10 }
  force: describes
  terms:
    verbs: [{ lemma: "demonstrate", form: "demonstrate", taxonomy: ["bloom-r:apply/understand"] }, { lemma: "communicate", form: "communicate", taxonomy: ["none"] }]
    objects: ["arguments"]
    degree: []
    independence: []
    scope: []
    deficits: []
- id: cardiffmet/generic-2020/l4/argument/70-79.s2
  cell: cardiffmet/generic-2020/l4/argument/70-79
  span: { start: 35502, end: 35560 }
  source: "Arguments are well developed, sustained and substantiated."
  versionsFrom: none
  echoes: none
  force: describes
  terms:
    verbs: [{ lemma: "develop", form: "developed", taxonomy: ["bloom-r:apply/create"] }, { lemma: "sustain", form: "sustained", taxonomy: ["none"] }]
    objects: ["arguments"]
    degree: ["well"]
    independence: []
    scope: []
    deficits: []
- id: cardiffmet/generic-2020/l4/argument/70-79.s3
  cell: cardiffmet/generic-2020/l4/argument/70-79
  span: { start: 35561, end: 35674 }
  source: "Where relevant, basic assumptions are challenged and there is recognition of the complexities of academic debate."
  versionsFrom: none
  echoes: none
  force: describes
  terms:
    verbs: [{ lemma: "recognise", form: "recognition", taxonomy: ["solo:unistructural"] }, { lemma: "challenge", form: "challenged", taxonomy: ["none"] }]
    objects: []
    degree: ["basic"]
    independence: []
    scope: ["basic"]
    deficits: []
- id: cardiffmet/generic-2020/l4/argument/70-79.s4
  cell: cardiffmet/generic-2020/l4/argument/70-79
  span: { start: 35675, end: 35784 }
  source: "Appropriate solutions are offered to problems and there is review of their effectiveness and appropriateness."
  versionsFrom: none
  echoes: none
  force: describes
  terms:
    verbs: [{ lemma: "solve", form: "solutions", taxonomy: ["bloom-r:analyze/apply/create", "solo:multistructural"] }, { lemma: "review", form: "review", taxonomy: ["bloom-r:evaluate/remember/understand", "solo:relational"] }]
    objects: ["problems"]
    degree: []
    independence: []
    scope: []
    deficits: []
- id: cardiffmet/generic-2020/l4/argument/70-79.s5
  cell: cardiffmet/generic-2020/l4/argument/70-79
  span: { start: 35785, end: 35882 }
  source: "There is strong evidence that the student is able to reflect effectively on her/his own practice."
  versionsFrom: none
  echoes: none
  force: describes
  terms:
    verbs: [{ lemma: "reflect", form: "reflect", taxonomy: ["solo:extended-abstract"] }]
    objects: ["own practice"]
    degree: ["strong", "effectively"]
    independence: []
    scope: []
    deficits: []
- id: cardiffmet/generic-2020/l4/argument/70-79.s6
  cell: cardiffmet/generic-2020/l4/argument/70-79
  span: { start: 35883, end: 36052 }
  source: "Critical evaluation of the student’s own work and/or professional practice is highly perceptive and there is a full awareness of the implications for future development."
  versionsFrom: none
  echoes: none
  force: describes
  terms:
    verbs: [{ lemma: "evaluate", form: "evaluation", taxonomy: ["bloom-r:analyze/create/evaluate", "solo:extended-abstract"] }, { lemma: "develop", form: "development", taxonomy: ["bloom-r:apply/create"] }]
    objects: []
    degree: ["highly", "perceptive"]
    independence: []
    scope: []
    deficits: []
- id: cardiffmet/generic-2020/l4/argument/60-69.s1
  cell: cardiffmet/generic-2020/l4/argument/60-69
  span: { start: 36119, end: 36217 }
  source: "May demonstrate an ability to communicate the results of their study/work accurately and reliably."
  versionsFrom: { sameAs: cardiffmet/generic-2020/l3/argument/60-69.s1 }
  echoes: { statement: qaa/fheq-2024/4.10.b4, words: 10 }
  force: describes
  terms:
    verbs: [{ lemma: "demonstrate", form: "demonstrate", taxonomy: ["bloom-r:apply/understand"] }, { lemma: "communicate", form: "communicate", taxonomy: ["none"] }]
    objects: []
    degree: []
    independence: []
    scope: []
    deficits: []
- id: cardiffmet/generic-2020/l4/argument/60-69.s2
  cell: cardiffmet/generic-2020/l4/argument/60-69
  span: { start: 36218, end: 36424 }
  source: "Arguments are clearly considered and substantiated and there is evidence of an ability to make appropriate judgements and to suggest solutions to problems and review their effectiveness and appropriateness."
  versionsFrom: none
  echoes: none
  force: describes
  terms:
    verbs: [{ lemma: "make", form: "make", taxonomy: ["bloom-r:create"] }, { lemma: "solve", form: "solutions", taxonomy: ["bloom-r:analyze/apply/create", "solo:multistructural"] }, { lemma: "review", form: "review", taxonomy: ["bloom-r:evaluate/remember/understand", "solo:relational"] }]
    objects: ["arguments", "problems"]
    degree: ["clearly"]
    independence: []
    scope: []
    deficits: []
- id: cardiffmet/generic-2020/l4/argument/60-69.s3
  cell: cardiffmet/generic-2020/l4/argument/60-69
  span: { start: 36425, end: 36576 }
  source: "The student also demonstrates an ability to engage in reflective practice and to take account of personal evaluations, planning for future development."
  versionsFrom: { sameAs: cardiffmet/generic-2020/l3/argument/60-69.s4 }
  echoes: none
  force: describes
  terms:
    verbs: [{ lemma: "demonstrate", form: "demonstrates", taxonomy: ["bloom-r:apply/understand"] }, { lemma: "evaluate", form: "evaluations", taxonomy: ["bloom-r:analyze/create/evaluate", "solo:extended-abstract"] }, { lemma: "develop", form: "development", taxonomy: ["bloom-r:apply/create"] }, { lemma: "plan", form: "planning", taxonomy: ["bloom-r:create", "solo:relational"] }]
    objects: []
    degree: []
    independence: []
    scope: []
    deficits: []
- id: cardiffmet/generic-2020/l4/argument/50-59.s1
  cell: cardiffmet/generic-2020/l4/argument/50-59
  span: { start: 36643, end: 36834 }
  source: "May demonstrate, at times, an ability to communicate the results of their study/work accurately and reliably, although there may be some over-reliance on description and factual presentation."
  versionsFrom: { sameAs: cardiffmet/generic-2020/l3/argument/50-59.s1 }
  echoes: { statement: qaa/fheq-2024/4.10.b4, words: 10 }
  force: describes
  terms:
    verbs: [{ lemma: "demonstrate", form: "demonstrate", taxonomy: ["bloom-r:apply/understand"] }, { lemma: "communicate", form: "communicate", taxonomy: ["none"] }, { lemma: "present", form: "presentation", taxonomy: ["none"] }, { lemma: "describe", form: "description", taxonomy: ["bloom-r:evaluate/remember/understand", "solo:multistructural"] }]
    objects: ["presentation"]
    degree: ["some"]
    independence: []
    scope: []
    deficits: ["over-reliance"]
- id: cardiffmet/generic-2020/l4/argument/50-59.s2
  cell: cardiffmet/generic-2020/l4/argument/50-59
  span: { start: 36835, end: 36871 }
  source: "Arguments are usually substantiated."
  versionsFrom: { sameAs: cardiffmet/generic-2020/l3/argument/50-59.s2 }
  echoes: none
  force: describes
  terms:
    verbs: []
    objects: ["arguments"]
    degree: []
    independence: []
    scope: []
    deficits: []
- id: cardiffmet/generic-2020/l4/argument/50-59.s3
  cell: cardiffmet/generic-2020/l4/argument/50-59
  span: { start: 36872, end: 37087 }
  source: "There is some evidence of the student’s ability to evaluate and reflect on the student’s own practice. own practice but reflections may lack insight and the implications for future development may be underestimated."
  versionsFrom: { like: cardiffmet/generic-2020/l3/argument/50-59.s3, similarity: 0.97 }
  echoes: none
  force: describes
  terms:
    verbs: [{ lemma: "evaluate", form: "evaluate", taxonomy: ["bloom-r:analyze/create/evaluate", "solo:extended-abstract"] }, { lemma: "develop", form: "development", taxonomy: ["bloom-r:apply/create"] }, { lemma: "reflect", form: "reflect", taxonomy: ["solo:extended-abstract"] }]
    objects: ["own practice", "own practice"]
    degree: ["some"]
    independence: []
    scope: []
    deficits: ["lack"]
- id: cardiffmet/generic-2020/l4/argument/40-49.s1
  cell: cardiffmet/generic-2020/l4/argument/40-49
  span: { start: 37154, end: 37259 }
  source: "May demonstrate a limited ability to communicate the results of their study/work accurately and reliably."
  versionsFrom: { sameAs: cardiffmet/generic-2020/l3/argument/40-49.s1 }
  echoes: { statement: qaa/fheq-2024/4.10.b4, words: 10 }
  force: describes
  terms:
    verbs: [{ lemma: "demonstrate", form: "demonstrate", taxonomy: ["bloom-r:apply/understand"] }, { lemma: "communicate", form: "communicate", taxonomy: ["none"] }]
    objects: []
    degree: ["limited"]
    independence: []
    scope: []
    deficits: []
- id: cardiffmet/generic-2020/l4/argument/40-49.s2
  cell: cardiffmet/generic-2020/l4/argument/40-49
  span: { start: 37260, end: 37354 }
  source: "The balance within the work is likely to be in favour of description and factual presentation."
  versionsFrom: { sameAs: cardiffmet/generic-2020/l3/argument/40-49.s2 }
  echoes: none
  force: describes
  terms:
    verbs: [{ lemma: "present", form: "presentation", taxonomy: ["none"] }, { lemma: "describe", form: "description", taxonomy: ["bloom-r:evaluate/remember/understand", "solo:multistructural"] }]
    objects: ["presentation"]
    degree: []
    independence: []
    scope: []
    deficits: []
- id: cardiffmet/generic-2020/l4/argument/40-49.s3
  cell: cardiffmet/generic-2020/l4/argument/40-49
  span: { start: 37355, end: 37420 }
  source: "Arguments are generally substantiated but may be under-developed."
  versionsFrom: { sameAs: cardiffmet/generic-2020/l3/argument/40-49.s3 }
  echoes: none
  force: describes
  terms:
    verbs: []
    objects: ["arguments"]
    degree: ["generally"]
    independence: []
    scope: []
    deficits: []
- id: cardiffmet/generic-2020/l4/argument/40-49.s4
  cell: cardiffmet/generic-2020/l4/argument/40-49
  span: { start: 37421, end: 37645 }
  source: "There is some evidence of the student’s ability to evaluate and reflect on the student’s own practice. although reflections may be limited and superficial, with little consideration of their relevance for future development."
  versionsFrom: { sameAs: cardiffmet/generic-2020/l3/argument/40-49.s4 }
  echoes: none
  force: describes
  terms:
    verbs: [{ lemma: "evaluate", form: "evaluate", taxonomy: ["bloom-r:analyze/create/evaluate", "solo:extended-abstract"] }, { lemma: "develop", form: "development", taxonomy: ["bloom-r:apply/create"] }, { lemma: "consider", form: "consideration", taxonomy: ["none"] }, { lemma: "reflect", form: "reflect", taxonomy: ["solo:extended-abstract"] }]
    objects: ["own practice"]
    degree: ["some", "limited", "little"]
    independence: []
    scope: []
    deficits: ["superficial"]
- id: cardiffmet/generic-2020/l4/argument/30-39.s1
  cell: cardiffmet/generic-2020/l4/argument/30-39
  span: { start: 37719, end: 37837 }
  source: "May demonstrate limited evidence of an ability to communicate the results of their study/work accurately and reliably."
  versionsFrom: { sameAs: cardiffmet/generic-2020/l3/argument/30-39.s1 }
  echoes: { statement: qaa/fheq-2024/4.10.b4, words: 10 }
  force: describes
  terms:
    verbs: [{ lemma: "demonstrate", form: "demonstrate", taxonomy: ["bloom-r:apply/understand"] }, { lemma: "communicate", form: "communicate", taxonomy: ["none"] }]
    objects: []
    degree: ["limited"]
    independence: []
    scope: []
    deficits: []
- id: cardiffmet/generic-2020/l4/argument/30-39.s2
  cell: cardiffmet/generic-2020/l4/argument/30-39
  span: { start: 37838, end: 37924 }
  source: "The work is largely descriptive and arguments, if attempted, are rarely substantiated."
  versionsFrom: { sameAs: cardiffmet/generic-2020/l3/argument/30-39.s2 }
  echoes: none
  force: describes
  terms:
    verbs: [{ lemma: "describe", form: "descriptive", taxonomy: ["bloom-r:evaluate/remember/understand", "solo:multistructural"] }]
    objects: ["arguments"]
    degree: []
    independence: []
    scope: []
    deficits: []
- id: cardiffmet/generic-2020/l4/argument/30-39.s3
  cell: cardiffmet/generic-2020/l4/argument/30-39
  span: { start: 37925, end: 38009 }
  source: "Self-evaluation and reflections on the student’s own practice are extremely limited."
  versionsFrom: { sameAs: cardiffmet/generic-2020/l3/argument/30-39.s3 }
  echoes: none
  force: describes
  terms:
    verbs: []
    objects: ["own practice"]
    degree: ["limited"]
    independence: []
    scope: []
    deficits: []
- id: cardiffmet/generic-2020/l4/argument/1-29.s1
  cell: cardiffmet/generic-2020/l4/argument/1-29
  span: { start: 38081, end: 38198 }
  source: "May demonstrate little evidence of an ability to communicate the results of their study/work accurately and reliably."
  versionsFrom: { sameAs: cardiffmet/generic-2020/l3/argument/1-29.s1 }
  echoes: { statement: qaa/fheq-2024/4.10.b4, words: 10 }
  force: describes
  terms:
    verbs: [{ lemma: "demonstrate", form: "demonstrate", taxonomy: ["bloom-r:apply/understand"] }, { lemma: "communicate", form: "communicate", taxonomy: ["none"] }]
    objects: []
    degree: ["little"]
    independence: []
    scope: []
    deficits: []
- id: cardiffmet/generic-2020/l4/argument/1-29.s2
  cell: cardiffmet/generic-2020/l4/argument/1-29
  span: { start: 38199, end: 38286 }
  source: "Self-evaluation and reflections on the student’s own practice are negligible or absent."
  versionsFrom: { sameAs: cardiffmet/generic-2020/l3/argument/1-29.s2 }
  echoes: none
  force: describes
  terms:
    verbs: []
    objects: ["own practice"]
    degree: []
    independence: []
    scope: []
    deficits: ["negligible", "absent"]
- id: cardiffmet/generic-2020/l5/overall/80-100.s1
  cell: cardiffmet/generic-2020/l5/overall/80-100
  span: { start: 38368, end: 38600 }
  source: "A full and detailed understanding of the set task and an ability to have met the learning outcomes and address the assessment criteria at an excellent level (80-89%) or outstanding and exceptional level (90-100%) and beyond level 5."
  versionsFrom: { sameAs: cardiffmet/generic-2020/l3/overall/80-100.s1 }
  echoes: none
  force: describes
  terms:
    verbs: [{ lemma: "address", form: "address", taxonomy: ["none"] }, { lemma: "meet", form: "met", taxonomy: ["none"] }]
    objects: ["understanding", "set task", "learning outcomes", "assessment criteria"]
    degree: ["detailed", "excellent", "outstanding", "exceptional"]
    independence: []
    scope: ["beyond level"]
    deficits: []
- id: cardiffmet/generic-2020/l5/overall/70-79.s1
  cell: cardiffmet/generic-2020/l5/overall/70-79
  span: { start: 38639, end: 38795 }
  source: "A full and detailed understanding of the set task and an ability to have met the learning outcomes and address the assessment criteria at a very good level."
  versionsFrom: { sameAs: cardiffmet/generic-2020/l3/overall/70-79.s1 }
  echoes: none
  force: describes
  terms:
    verbs: [{ lemma: "address", form: "address", taxonomy: ["none"] }, { lemma: "meet", form: "met", taxonomy: ["none"] }]
    objects: ["understanding", "set task", "learning outcomes", "assessment criteria"]
    degree: ["detailed", "very good"]
    independence: []
    scope: []
    deficits: []
- id: cardiffmet/generic-2020/l5/overall/60-69.s1
  cell: cardiffmet/generic-2020/l5/overall/60-69
  span: { start: 38834, end: 38972 }
  source: "A full understanding of the set task and an ability to have met the learning outcomes and address the assessment criteria at a good level."
  versionsFrom: { sameAs: cardiffmet/generic-2020/l3/overall/60-69.s1 }
  echoes: none
  force: describes
  terms:
    verbs: [{ lemma: "address", form: "address", taxonomy: ["none"] }, { lemma: "meet", form: "met", taxonomy: ["none"] }]
    objects: ["understanding", "set task", "learning outcomes", "assessment criteria"]
    degree: ["good"]
    independence: []
    scope: []
    deficits: []
- id: cardiffmet/generic-2020/l5/overall/50-59.s1
  cell: cardiffmet/generic-2020/l5/overall/50-59
  span: { start: 39011, end: 39170 }
  source: "A secure understanding of the set task and an ability to have met the associated learning outcomes and address the assessment criteria at a satisfactory level."
  versionsFrom: { sameAs: cardiffmet/generic-2020/l3/overall/50-59.s1 }
  echoes: none
  force: describes
  terms:
    verbs: [{ lemma: "address", form: "address", taxonomy: ["none"] }, { lemma: "meet", form: "met", taxonomy: ["none"] }]
    objects: ["understanding", "set task", "learning outcomes", "assessment criteria"]
    degree: ["secure", "satisfactory"]
    independence: []
    scope: []
    deficits: []
- id: cardiffmet/generic-2020/l5/overall/40-49.s1
  cell: cardiffmet/generic-2020/l5/overall/40-49
  span: { start: 39209, end: 39364 }
  source: "A basic understanding of the set task and an ability to have met the associated learning outcomes and address the assessment criteria at a threshold level."
  versionsFrom: { sameAs: cardiffmet/generic-2020/l3/overall/40-49.s1 }
  echoes: none
  force: describes
  terms:
    verbs: [{ lemma: "address", form: "address", taxonomy: ["none"] }, { lemma: "meet", form: "met", taxonomy: ["none"] }]
    objects: ["understanding", "set task", "learning outcomes", "assessment criteria"]
    degree: ["basic"]
    independence: []
    scope: ["basic"]
    deficits: []
- id: cardiffmet/generic-2020/l5/overall/30-39.s1
  cell: cardiffmet/generic-2020/l5/overall/30-39
  span: { start: 39410, end: 39433 }
  source: "Unsatisfactory overall."
  versionsFrom: { sameAs: cardiffmet/generic-2020/l3/overall/30-39.s1 }
  echoes: none
  force: describes
  terms:
    verbs: []
    objects: []
    degree: []
    independence: []
    scope: []
    deficits: []
- id: cardiffmet/generic-2020/l5/overall/30-39.s2
  cell: cardiffmet/generic-2020/l5/overall/30-39
  span: { start: 39434, end: 39559 }
  source: "A partial understanding of the set task and an ability to have met some of the associated learning outcomes at a basic level."
  versionsFrom: { sameAs: cardiffmet/generic-2020/l3/overall/30-39.s2 }
  echoes: none
  force: describes
  terms:
    verbs: [{ lemma: "meet", form: "met", taxonomy: ["none"] }]
    objects: ["understanding", "set task", "learning outcomes"]
    degree: ["some", "basic"]
    independence: []
    scope: ["basic"]
    deficits: []
- id: cardiffmet/generic-2020/l5/overall/30-39.s3
  cell: cardiffmet/generic-2020/l5/overall/30-39
  span: { start: 39560, end: 39658 }
  source: "Attainment is uneven with some learning outcomes not met and some assessment criteria unaddressed."
  versionsFrom: none
  echoes: none
  force: describes
  terms:
    verbs: [{ lemma: "meet", form: "met", taxonomy: ["none"] }]
    objects: ["learning outcomes", "assessment criteria"]
    degree: ["some", "some"]
    independence: []
    scope: []
    deficits: ["not", "unaddressed"]
- id: cardiffmet/generic-2020/l5/overall/1-29.s1
  cell: cardiffmet/generic-2020/l5/overall/1-29
  span: { start: 39702, end: 39715 }
  source: "Poor overall."
  versionsFrom: { sameAs: cardiffmet/generic-2020/l3/overall/1-29.s1 }
  echoes: none
  force: describes
  terms:
    verbs: []
    objects: []
    degree: ["poor"]
    independence: []
    scope: []
    deficits: []
- id: cardiffmet/generic-2020/l5/overall/1-29.s2
  cell: cardiffmet/generic-2020/l5/overall/1-29
  span: { start: 39716, end: 39820 }
  source: "Minimal understanding of the set task and will partially have met one or two learning outcomes, or none."
  versionsFrom: { sameAs: cardiffmet/generic-2020/l4/overall/1-29.s2 }
  echoes: none
  force: describes
  terms:
    verbs: [{ lemma: "meet", form: "met", taxonomy: ["none"] }]
    objects: ["understanding", "set task", "learning outcomes"]
    degree: ["minimal"]
    independence: []
    scope: []
    deficits: ["none"]
- id: cardiffmet/generic-2020/l5/overall/1-29.s3
  cell: cardiffmet/generic-2020/l5/overall/1-29
  span: { start: 39821, end: 39862 }
  source: "Many assessment criteria are unaddressed."
  versionsFrom: { sameAs: cardiffmet/generic-2020/l3/overall/1-29.s4 }
  echoes: none
  force: describes
  terms:
    verbs: []
    objects: ["assessment criteria"]
    degree: []
    independence: []
    scope: []
    deficits: ["unaddressed"]
- id: cardiffmet/generic-2020/l5/knowledge/80-100.s1
  cell: cardiffmet/generic-2020/l5/knowledge/80-100
  span: { start: 39920, end: 40021 }
  source: "Further to the 70%-79% band, work in the 80%-100% bands would extend beyond that expected at Level 5."
  versionsFrom: { sameAs: cardiffmet/generic-2020/l3/knowledge/80-100.s1 }
  echoes: none
  force: describes
  terms:
    verbs: [{ lemma: "extend", form: "extend", taxonomy: ["bloom-r:understand"] }]
    objects: []
    degree: []
    independence: []
    scope: []
    deficits: []
- id: cardiffmet/generic-2020/l5/knowledge/70-79.s1
  cell: cardiffmet/generic-2020/l5/knowledge/70-79
  span: { start: 40070, end: 40212 }
  source: "Demonstrates a detailed knowledge and critical understanding of underlying concepts and principles of the field of study relevant to the task."
  versionsFrom: none
  echoes: none
  force: describes
  terms:
    verbs: [{ lemma: "demonstrate", form: "demonstrates", taxonomy: ["bloom-r:apply/understand"] }]
    objects: ["knowledge", "understanding", "concepts", "principles", "field of study"]
    degree: ["detailed"]
    independence: []
    scope: []
    deficits: []
- id: cardiffmet/generic-2020/l5/knowledge/70-79.s2
  cell: cardiffmet/generic-2020/l5/knowledge/70-79
  span: { start: 40213, end: 40298 }
  source: "There is strong evidence of an ability to extend, transform and apply such knowledge."
  versionsFrom: none
  echoes: none
  force: describes
  terms:
    verbs: [{ lemma: "apply", form: "apply", taxonomy: ["bloom-r:apply", "solo:relational"] }, { lemma: "extend", form: "extend", taxonomy: ["bloom-r:understand"] }, { lemma: "transform", form: "transform", taxonomy: ["none"] }]
    objects: ["knowledge"]
    degree: ["strong"]
    independence: []
    scope: []
    deficits: []
- id: cardiffmet/generic-2020/l5/knowledge/70-79.s3
  cell: cardiffmet/generic-2020/l5/knowledge/70-79
  span: { start: 40299, end: 40470 }
  source: "The student also demonstrates an ability to engage in confident discussion of complex concepts and to recognise the limitations and/or ambiguity of disciplinary knowledge."
  versionsFrom: none
  echoes: none
  force: describes
  terms:
    verbs: [{ lemma: "demonstrate", form: "demonstrates", taxonomy: ["bloom-r:apply/understand"] }, { lemma: "recognise", form: "recognise", taxonomy: ["solo:unistructural"] }]
    objects: ["concepts", "limitations", "knowledge"]
    degree: ["confident"]
    independence: []
    scope: ["complex"]
    deficits: []
- id: cardiffmet/generic-2020/l5/knowledge/70-79.s4
  cell: cardiffmet/generic-2020/l5/knowledge/70-79
  span: { start: 40471, end: 40554 }
  source: "Independent thinking and original insights are also features of work at this level."
  versionsFrom: { sameAs: cardiffmet/generic-2020/l4/knowledge/70-79.s4 }
  echoes: none
  force: describes
  terms:
    verbs: []
    objects: []
    degree: []
    independence: ["independent thinking"]
    scope: ["original", "at this level"]
    deficits: []
- id: cardiffmet/generic-2020/l5/knowledge/60-69.s1
  cell: cardiffmet/generic-2020/l5/knowledge/60-69
  span: { start: 40603, end: 40745 }
  source: "Demonstrates a detailed knowledge and critical understanding of underlying concepts and principles of the field of study relevant to the task."
  versionsFrom: { sameAs: cardiffmet/generic-2020/l5/knowledge/70-79.s1 }
  echoes: none
  force: describes
  terms:
    verbs: [{ lemma: "demonstrate", form: "demonstrates", taxonomy: ["bloom-r:apply/understand"] }]
    objects: ["knowledge", "understanding", "concepts", "principles", "field of study"]
    degree: ["detailed"]
    independence: []
    scope: []
    deficits: []
- id: cardiffmet/generic-2020/l5/knowledge/60-69.s2
  cell: cardiffmet/generic-2020/l5/knowledge/60-69
  span: { start: 40746, end: 40829 }
  source: "There is good evidence of an ability to extend, transform and apply such knowledge."
  versionsFrom: none
  echoes: none
  force: describes
  terms:
    verbs: [{ lemma: "apply", form: "apply", taxonomy: ["bloom-r:apply", "solo:relational"] }, { lemma: "extend", form: "extend", taxonomy: ["bloom-r:understand"] }, { lemma: "transform", form: "transform", taxonomy: ["none"] }]
    objects: ["knowledge"]
    degree: ["good"]
    independence: []
    scope: []
    deficits: []
- id: cardiffmet/generic-2020/l5/knowledge/60-69.s3
  cell: cardiffmet/generic-2020/l5/knowledge/60-69
  span: { start: 40830, end: 40941 }
  source: "The discussion of complex concepts is often tackled successfully and there is evidence of independent thinking."
  versionsFrom: none
  echoes: none
  force: describes
  terms:
    verbs: []
    objects: ["concepts"]
    degree: ["successfully"]
    independence: ["independent thinking"]
    scope: ["complex"]
    deficits: []
- id: cardiffmet/generic-2020/l5/knowledge/50-59.s1
  cell: cardiffmet/generic-2020/l5/knowledge/50-59
  span: { start: 40990, end: 41129 }
  source: "Demonstrates a sound knowledge and critical understanding of underlying concepts and principles of the field of study relevant to the task."
  versionsFrom: none
  echoes: none
  force: describes
  terms:
    verbs: [{ lemma: "demonstrate", form: "demonstrates", taxonomy: ["bloom-r:apply/understand"] }]
    objects: ["knowledge", "understanding", "concepts", "principles", "field of study"]
    degree: ["sound"]
    independence: []
    scope: []
    deficits: []
- id: cardiffmet/generic-2020/l5/knowledge/50-59.s2
  cell: cardiffmet/generic-2020/l5/knowledge/50-59
  span: { start: 41130, end: 41208 }
  source: "There is evidence of an ability to extend, transform and apply such knowledge."
  versionsFrom: none
  echoes: none
  force: describes
  terms:
    verbs: [{ lemma: "apply", form: "apply", taxonomy: ["bloom-r:apply", "solo:relational"] }, { lemma: "extend", form: "extend", taxonomy: ["bloom-r:understand"] }, { lemma: "transform", form: "transform", taxonomy: ["none"] }]
    objects: ["knowledge"]
    degree: []
    independence: []
    scope: []
    deficits: []
- id: cardiffmet/generic-2020/l5/knowledge/50-59.s3
  cell: cardiffmet/generic-2020/l5/knowledge/50-59
  span: { start: 41209, end: 41372 }
  source: "Although there may be a tendency to reproduce information received from elsewhere (e.g. programme materials), there is still some evidence of independent thinking."
  versionsFrom: none
  echoes: none
  force: describes
  terms:
    verbs: [{ lemma: "reproduce", form: "reproduce", taxonomy: ["bloom-r:remember", "solo:unistructural"] }]
    objects: ["information"]
    degree: ["some"]
    independence: ["independent thinking"]
    scope: []
    deficits: []
- id: cardiffmet/generic-2020/l5/knowledge/50-59.s4
  cell: cardiffmet/generic-2020/l5/knowledge/50-59
  span: { start: 41373, end: 41465 }
  source: "A few errors and/or misconceptions may be present, but these will not be in important areas."
  versionsFrom: { sameAs: cardiffmet/generic-2020/l3/knowledge/50-59.s3 }
  echoes: none
  force: describes
  terms:
    verbs: [{ lemma: "present", form: "present", taxonomy: ["none"] }]
    objects: []
    degree: []
    independence: []
    scope: []
    deficits: ["errors", "misconceptions", "not"]
- id: cardiffmet/generic-2020/l5/knowledge/40-49.s1
  cell: cardiffmet/generic-2020/l5/knowledge/40-49
  span: { start: 41514, end: 41653 }
  source: "Demonstrates a basic knowledge and critical understanding of underlying concepts and principles of the field of study relevant to the task."
  versionsFrom: none
  echoes: none
  force: describes
  terms:
    verbs: [{ lemma: "demonstrate", form: "demonstrates", taxonomy: ["bloom-r:apply/understand"] }]
    objects: ["knowledge", "understanding", "concepts", "principles", "field of study"]
    degree: ["basic"]
    independence: []
    scope: ["basic"]
    deficits: []
- id: cardiffmet/generic-2020/l5/knowledge/40-49.s2
  cell: cardiffmet/generic-2020/l5/knowledge/40-49
  span: { start: 41654, end: 41737 }
  source: "There is some evidence of an ability to extend, transform and apply such knowledge."
  versionsFrom: none
  echoes: none
  force: describes
  terms:
    verbs: [{ lemma: "apply", form: "apply", taxonomy: ["bloom-r:apply", "solo:relational"] }, { lemma: "extend", form: "extend", taxonomy: ["bloom-r:understand"] }, { lemma: "transform", form: "transform", taxonomy: ["none"] }]
    objects: ["knowledge"]
    degree: ["some"]
    independence: []
    scope: []
    deficits: []
- id: cardiffmet/generic-2020/l5/knowledge/40-49.s3
  cell: cardiffmet/generic-2020/l5/knowledge/40-49
  span: { start: 41738, end: 41857 }
  source: "Reproducing information received from elsewhere (e.g. programme materials) is a frequent feature of work at this level."
  versionsFrom: { sameAs: cardiffmet/generic-2020/l3/knowledge/40-49.s2 }
  echoes: none
  force: describes
  terms:
    verbs: [{ lemma: "reproduce", form: "reproducing", taxonomy: ["bloom-r:remember", "solo:unistructural"] }]
    objects: ["information"]
    degree: []
    independence: []
    scope: ["at this level"]
    deficits: []
- id: cardiffmet/generic-2020/l5/knowledge/40-49.s4
  cell: cardiffmet/generic-2020/l5/knowledge/40-49
  span: { start: 41858, end: 41992 }
  source: "Errors and misconceptions will be evident, but these are outweighed by the degree of knowledge and understanding demonstrated overall."
  versionsFrom: { sameAs: cardiffmet/generic-2020/l3/knowledge/40-49.s3 }
  echoes: none
  force: describes
  terms:
    verbs: [{ lemma: "demonstrate", form: "demonstrated", taxonomy: ["bloom-r:apply/understand"] }]
    objects: ["knowledge and understanding"]
    degree: []
    independence: []
    scope: []
    deficits: ["errors", "misconceptions"]
- id: cardiffmet/generic-2020/l5/knowledge/30-39.s1
  cell: cardiffmet/generic-2020/l5/knowledge/30-39
  span: { start: 42048, end: 42187 }
  source: "Demonstrates limited knowledge and critical understanding of underlying concepts and principles of the field of study relevant to the task."
  versionsFrom: none
  echoes: none
  force: describes
  terms:
    verbs: [{ lemma: "demonstrate", form: "demonstrates", taxonomy: ["bloom-r:apply/understand"] }]
    objects: ["knowledge", "understanding", "concepts", "principles", "field of study"]
    degree: ["limited"]
    independence: []
    scope: []
    deficits: []
- id: cardiffmet/generic-2020/l5/knowledge/30-39.s2
  cell: cardiffmet/generic-2020/l5/knowledge/30-39
  span: { start: 42188, end: 42279 }
  source: "There is insufficient evidence of an ability to extend, transform and apply such knowledge."
  versionsFrom: none
  echoes: none
  force: describes
  terms:
    verbs: [{ lemma: "apply", form: "apply", taxonomy: ["bloom-r:apply", "solo:relational"] }, { lemma: "extend", form: "extend", taxonomy: ["bloom-r:understand"] }, { lemma: "transform", form: "transform", taxonomy: ["none"] }]
    objects: ["knowledge"]
    degree: []
    independence: []
    scope: []
    deficits: ["insufficient"]
- id: cardiffmet/generic-2020/l5/knowledge/30-39.s3
  cell: cardiffmet/generic-2020/l5/knowledge/30-39
  span: { start: 42280, end: 42423 }
  source: "Factual inaccuracies, errors and misconceptions are evident in important areas and elements of the assessed work may be irrelevant to the task."
  versionsFrom: { sameAs: cardiffmet/generic-2020/l3/knowledge/30-39.s2 }
  echoes: none
  force: describes
  terms:
    verbs: []
    objects: []
    degree: []
    independence: []
    scope: []
    deficits: ["inaccuracies", "errors", "misconceptions", "irrelevant"]
- id: cardiffmet/generic-2020/l5/knowledge/1-29.s1
  cell: cardiffmet/generic-2020/l5/knowledge/1-29
  span: { start: 42477, end: 42615 }
  source: "Demonstrates little knowledge and critical understanding of underlying concepts and principles of the field of study relevant to the task."
  versionsFrom: none
  echoes: none
  force: describes
  terms:
    verbs: [{ lemma: "demonstrate", form: "demonstrates", taxonomy: ["bloom-r:apply/understand"] }]
    objects: ["knowledge", "understanding", "concepts", "principles", "field of study"]
    degree: ["little"]
    independence: []
    scope: []
    deficits: []
- id: cardiffmet/generic-2020/l5/knowledge/1-29.s2
  cell: cardiffmet/generic-2020/l5/knowledge/1-29
  span: { start: 42616, end: 42701 }
  source: "There is little evidence of an ability to extend, transform and apply such knowledge."
  versionsFrom: none
  echoes: none
  force: describes
  terms:
    verbs: [{ lemma: "apply", form: "apply", taxonomy: ["bloom-r:apply", "solo:relational"] }, { lemma: "extend", form: "extend", taxonomy: ["bloom-r:understand"] }, { lemma: "transform", form: "transform", taxonomy: ["none"] }]
    objects: ["knowledge"]
    degree: ["little"]
    independence: []
    scope: []
    deficits: []
- id: cardiffmet/generic-2020/l5/knowledge/1-29.s3
  cell: cardiffmet/generic-2020/l5/knowledge/1-29
  span: { start: 42702, end: 42860 }
  source: "Factual inaccuracies, errors and misconceptions are evident in many important areas and these outweigh the degree of knowledge and understanding demonstrated."
  versionsFrom: { sameAs: cardiffmet/generic-2020/l3/knowledge/1-29.s2 }
  echoes: none
  force: describes
  terms:
    verbs: [{ lemma: "demonstrate", form: "demonstrated", taxonomy: ["bloom-r:apply/understand"] }]
    objects: ["knowledge and understanding"]
    degree: []
    independence: []
    scope: []
    deficits: ["inaccuracies", "errors", "misconceptions"]
- id: cardiffmet/generic-2020/l5/knowledge/1-29.s4
  cell: cardiffmet/generic-2020/l5/knowledge/1-29
  span: { start: 42861, end: 42933 }
  source: "Substantial elements of the assessed work may be irrelevant to the task."
  versionsFrom: { sameAs: cardiffmet/generic-2020/l3/knowledge/1-29.s3 }
  echoes: none
  force: describes
  terms:
    verbs: []
    objects: []
    degree: []
    independence: []
    scope: []
    deficits: ["irrelevant"]
- id: cardiffmet/generic-2020/l5/presentation/80-100.s1
  cell: cardiffmet/generic-2020/l5/presentation/80-100
  span: { start: 42996, end: 43097 }
  source: "Further to the 70%-79% band, work in the 80%-100% bands would extend beyond that expected at Level 5."
  versionsFrom: { sameAs: cardiffmet/generic-2020/l3/knowledge/80-100.s1 }
  echoes: none
  force: describes
  terms:
    verbs: [{ lemma: "extend", form: "extend", taxonomy: ["bloom-r:understand"] }]
    objects: []
    degree: []
    independence: []
    scope: []
    deficits: []
- id: cardiffmet/generic-2020/l5/presentation/70-79.s1
  cell: cardiffmet/generic-2020/l5/presentation/70-79
  span: { start: 43151, end: 43285 }
  source: "Demonstrates an ability to communicate information, arguments and analysis in a coherent and succinct manner in a range of situations."
  versionsFrom: none
  echoes: { statement: qaa/fheq-2024/4.12.b6, words: 7 }
  force: describes
  terms:
    verbs: [{ lemma: "demonstrate", form: "demonstrates", taxonomy: ["bloom-r:apply/understand"] }, { lemma: "communicate", form: "communicate", taxonomy: ["none"] }]
    objects: ["information", "arguments"]
    degree: []
    independence: []
    scope: ["a range of"]
    deficits: []
- id: cardiffmet/generic-2020/l5/presentation/70-79.s2
  cell: cardiffmet/generic-2020/l5/presentation/70-79
  span: { start: 43286, end: 43350 }
  source: "The standard of presentation is high and the format appropriate."
  versionsFrom: { sameAs: cardiffmet/generic-2020/l3/presentation/70-79.s2 }
  echoes: none
  force: describes
  terms:
    verbs: [{ lemma: "present", form: "presentation", taxonomy: ["none"] }]
    objects: ["presentation"]
    degree: ["high"]
    independence: []
    scope: []
    deficits: []
- id: cardiffmet/generic-2020/l5/presentation/70-79.s3
  cell: cardiffmet/generic-2020/l5/presentation/70-79
  span: { start: 43351, end: 43437 }
  source: "Key points are logically organised and in written work, the style is lucid and mature."
  versionsFrom: none
  echoes: none
  force: describes
  terms:
    verbs: []
    objects: []
    degree: []
    independence: []
    scope: ["key"]
    deficits: []
- id: cardiffmet/generic-2020/l5/presentation/70-79.s4
  cell: cardiffmet/generic-2020/l5/presentation/70-79
  span: { start: 43438, end: 43514 }
  source: "Arguments are well-defined and clearly articulated, structured and coherent."
  versionsFrom: { sameAs: cardiffmet/generic-2020/l4/presentation/70-79.s4 }
  echoes: none
  force: describes
  terms:
    verbs: []
    objects: ["arguments"]
    degree: ["clearly"]
    independence: []
    scope: ["well-defined"]
    deficits: []
- id: cardiffmet/generic-2020/l5/presentation/60-69.s1
  cell: cardiffmet/generic-2020/l5/presentation/60-69
  span: { start: 43568, end: 43702 }
  source: "Demonstrates an ability to communicate information, arguments and analysis in a coherent and succinct manner in a range of situations."
  versionsFrom: { sameAs: cardiffmet/generic-2020/l5/presentation/70-79.s1 }
  echoes: { statement: qaa/fheq-2024/4.12.b6, words: 7 }
  force: describes
  terms:
    verbs: [{ lemma: "demonstrate", form: "demonstrates", taxonomy: ["bloom-r:apply/understand"] }, { lemma: "communicate", form: "communicate", taxonomy: ["none"] }]
    objects: ["information", "arguments"]
    degree: []
    independence: []
    scope: ["a range of"]
    deficits: []
- id: cardiffmet/generic-2020/l5/presentation/60-69.s2
  cell: cardiffmet/generic-2020/l5/presentation/60-69
  span: { start: 43703, end: 43753 }
  source: "Work is well presented and the format appropriate."
  versionsFrom: { sameAs: cardiffmet/generic-2020/l3/presentation/60-69.s2 }
  echoes: none
  force: describes
  terms:
    verbs: []
    objects: []
    degree: ["well"]
    independence: []
    scope: []
    deficits: []
- id: cardiffmet/generic-2020/l5/presentation/60-69.s3
  cell: cardiffmet/generic-2020/l5/presentation/60-69
  span: { start: 43754, end: 43902 }
  source: "Key points are appropriately organised and in written work, the writing style is fluent and arguments are well articulated, structured and coherent."
  versionsFrom: { sameAs: cardiffmet/generic-2020/l4/presentation/60-69.s3 }
  echoes: none
  force: describes
  terms:
    verbs: []
    objects: ["arguments"]
    degree: ["well"]
    independence: []
    scope: ["key"]
    deficits: []
- id: cardiffmet/generic-2020/l5/presentation/50-59.s1
  cell: cardiffmet/generic-2020/l5/presentation/50-59
  span: { start: 43956, end: 44102 }
  source: "Demonstrates a satisfactory ability to communicate information, arguments and analysis in a coherent and succinct manner in a range of situations."
  versionsFrom: none
  echoes: { statement: qaa/fheq-2024/4.12.b6, words: 7 }
  force: describes
  terms:
    verbs: [{ lemma: "demonstrate", form: "demonstrates", taxonomy: ["bloom-r:apply/understand"] }, { lemma: "communicate", form: "communicate", taxonomy: ["none"] }]
    objects: ["information", "arguments"]
    degree: ["satisfactory"]
    independence: []
    scope: ["a range of"]
    deficits: []
- id: cardiffmet/generic-2020/l5/presentation/50-59.s2
  cell: cardiffmet/generic-2020/l5/presentation/50-59
  span: { start: 44103, end: 44165 }
  source: "Overall, the structure and format of the work are appropriate."
  versionsFrom: { sameAs: cardiffmet/generic-2020/l3/presentation/50-59.s2 }
  echoes: none
  force: describes
  terms:
    verbs: []
    objects: ["structure"]
    degree: []
    independence: []
    scope: []
    deficits: []
- id: cardiffmet/generic-2020/l5/presentation/50-59.s3
  cell: cardiffmet/generic-2020/l5/presentation/50-59
  span: { start: 44166, end: 44225 }
  source: "There may be occasional faults in the presentation of work."
  versionsFrom: none
  echoes: none
  force: describes
  terms:
    verbs: [{ lemma: "present", form: "presentation", taxonomy: ["none"] }]
    objects: ["presentation"]
    degree: []
    independence: []
    scope: []
    deficits: []
- id: cardiffmet/generic-2020/l5/presentation/50-59.s4
  cell: cardiffmet/generic-2020/l5/presentation/50-59
  span: { start: 44226, end: 44278 }
  source: "These do not detract from the clarity of expression."
  versionsFrom: none
  echoes: none
  force: describes
  terms:
    verbs: []
    objects: []
    degree: []
    independence: []
    scope: []
    deficits: ["not"]
- id: cardiffmet/generic-2020/l5/presentation/40-49.s1
  cell: cardiffmet/generic-2020/l5/presentation/40-49
  span: { start: 44332, end: 44471 }
  source: "Demonstrates a basic ability to communicate information, arguments and analysis in a coherent and succinct manner in a range of situations."
  versionsFrom: none
  echoes: { statement: qaa/fheq-2024/4.12.b6, words: 7 }
  force: describes
  terms:
    verbs: [{ lemma: "demonstrate", form: "demonstrates", taxonomy: ["bloom-r:apply/understand"] }, { lemma: "communicate", form: "communicate", taxonomy: ["none"] }]
    objects: ["information", "arguments"]
    degree: ["basic"]
    independence: []
    scope: ["basic", "a range of"]
    deficits: []
- id: cardiffmet/generic-2020/l5/presentation/40-49.s2
  cell: cardiffmet/generic-2020/l5/presentation/40-49
  span: { start: 44472, end: 44595 }
  source: "However, more success is achieved in describing and reporting factual information, rather than communicating complex ideas."
  versionsFrom: { sameAs: cardiffmet/generic-2020/l3/presentation/40-49.s2 }
  echoes: none
  force: describes
  terms:
    verbs: [{ lemma: "communicate", form: "communicating", taxonomy: ["none"] }, { lemma: "describe", form: "describing", taxonomy: ["bloom-r:evaluate/remember/understand", "solo:multistructural"] }, { lemma: "report", form: "reporting", taxonomy: ["bloom-r:apply/understand", "solo:multistructural"] }]
    objects: ["information", "ideas"]
    degree: []
    independence: []
    scope: ["complex"]
    deficits: []
- id: cardiffmet/generic-2020/l5/presentation/40-49.s3
  cell: cardiffmet/generic-2020/l5/presentation/40-49
  span: { start: 44596, end: 44695 }
  source: "Generally, the work is appropriately structured although key points may not be logically sequenced."
  versionsFrom: { sameAs: cardiffmet/generic-2020/l3/presentation/40-49.s3 }
  echoes: none
  force: describes
  terms:
    verbs: []
    objects: []
    degree: ["generally"]
    independence: []
    scope: ["key"]
    deficits: ["not"]
- id: cardiffmet/generic-2020/l5/presentation/40-49.s4
  cell: cardiffmet/generic-2020/l5/presentation/40-49
  span: { start: 44696, end: 44782 }
  source: "Although there will be faults in the presentation of work, the meaning is still clear."
  versionsFrom: { sameAs: cardiffmet/generic-2020/l3/presentation/40-49.s4 }
  echoes: none
  force: describes
  terms:
    verbs: [{ lemma: "present", form: "presentation", taxonomy: ["none"] }]
    objects: ["presentation"]
    degree: ["clear"]
    independence: []
    scope: []
    deficits: []
- id: cardiffmet/generic-2020/l5/presentation/30-39.s1
  cell: cardiffmet/generic-2020/l5/presentation/30-39
  span: { start: 44843, end: 44958 }
  source: "Demonstrates a limited ability to communicate some basic concepts, arguments and analysis in a range of situations."
  versionsFrom: none
  echoes: none
  force: describes
  terms:
    verbs: [{ lemma: "demonstrate", form: "demonstrates", taxonomy: ["bloom-r:apply/understand"] }, { lemma: "communicate", form: "communicate", taxonomy: ["none"] }]
    objects: ["concepts", "arguments"]
    degree: ["limited", "some"]
    independence: []
    scope: ["basic", "a range of"]
    deficits: []
- id: cardiffmet/generic-2020/l5/presentation/30-39.s2
  cell: cardiffmet/generic-2020/l5/presentation/30-39
  span: { start: 44959, end: 45065 }
  source: "If attempted, the presentation of arguments and more complex ideas may be confused and clumsily expressed."
  versionsFrom: { sameAs: cardiffmet/generic-2020/l3/presentation/30-39.s3 }
  echoes: none
  force: describes
  terms:
    verbs: [{ lemma: "present", form: "presentation", taxonomy: ["none"] }]
    objects: ["presentation", "arguments", "ideas"]
    degree: []
    independence: []
    scope: ["complex"]
    deficits: ["confused"]
- id: cardiffmet/generic-2020/l5/presentation/1-29.s1
  cell: cardiffmet/generic-2020/l5/presentation/1-29
  span: { start: 45124, end: 45236 }
  source: "Demonstrates little ability to communicate some basic concepts, arguments and analysis in a range of situations."
  versionsFrom: none
  echoes: none
  force: describes
  terms:
    verbs: [{ lemma: "demonstrate", form: "demonstrates", taxonomy: ["bloom-r:apply/understand"] }, { lemma: "communicate", form: "communicate", taxonomy: ["none"] }]
    objects: ["concepts", "arguments"]
    degree: ["little", "some"]
    independence: []
    scope: ["basic", "a range of"]
    deficits: []
- id: cardiffmet/generic-2020/l5/presentation/1-29.s2
  cell: cardiffmet/generic-2020/l5/presentation/1-29
  span: { start: 45237, end: 45389 }
  source: "Frequent faults in the presentation of work and significant difficulties in its structure and organisation detract from the clarity and meaning overall."
  versionsFrom: { sameAs: cardiffmet/generic-2020/l3/presentation/1-29.s2 }
  echoes: none
  force: describes
  terms:
    verbs: [{ lemma: "present", form: "presentation", taxonomy: ["none"] }]
    objects: ["presentation", "structure"]
    degree: []
    independence: []
    scope: []
    deficits: []
- id: cardiffmet/generic-2020/l5/presentation/1-29.s3
  cell: cardiffmet/generic-2020/l5/presentation/1-29
  span: { start: 45390, end: 45442 }
  source: "The writing style is often clumsy and inappropriate."
  versionsFrom: { sameAs: cardiffmet/generic-2020/l3/presentation/1-29.s3 }
  echoes: none
  force: describes
  terms:
    verbs: []
    objects: []
    degree: []
    independence: []
    scope: []
    deficits: ["clumsy"]
- id: cardiffmet/generic-2020/l5/analysis/80-100.s1
  cell: cardiffmet/generic-2020/l5/analysis/80-100
  span: { start: 45496, end: 45644 }
  source: "Demonstrates the ability to design and undertake their own research or advanced scholarship, applying relevant techniques and methods appropriately."
  versionsFrom: none
  echoes: none
  force: describes
  terms:
    verbs: [{ lemma: "demonstrate", form: "demonstrates", taxonomy: ["bloom-r:apply/understand"] }, { lemma: "apply", form: "applying", taxonomy: ["bloom-r:apply", "solo:relational"] }, { lemma: "undertake", form: "undertake", taxonomy: ["none"] }]
    objects: ["research", "scholarship", "techniques"]
    degree: []
    independence: []
    scope: ["advanced"]
    deficits: []
- id: cardiffmet/generic-2020/l5/analysis/80-100.s2
  cell: cardiffmet/generic-2020/l5/analysis/80-100
  span: { start: 45645, end: 45746 }
  source: "Further to the 70%-79% band, work in the 80%-100% bands would extend beyond that expected at Level 5."
  versionsFrom: { sameAs: cardiffmet/generic-2020/l3/knowledge/80-100.s1 }
  echoes: none
  force: describes
  terms:
    verbs: [{ lemma: "extend", form: "extend", taxonomy: ["bloom-r:understand"] }]
    objects: []
    degree: []
    independence: []
    scope: []
    deficits: []
- id: cardiffmet/generic-2020/l5/analysis/70-79.s1
  cell: cardiffmet/generic-2020/l5/analysis/70-79
  span: { start: 45791, end: 45935 }
  source: "Demonstrates an ability to undertake analysis of qualitative and quantitative data by making very good use of a range of established techniques."
  versionsFrom: none
  echoes: none
  force: describes
  terms:
    verbs: [{ lemma: "demonstrate", form: "demonstrates", taxonomy: ["bloom-r:apply/understand"] }, { lemma: "use", form: "use", taxonomy: ["bloom-r:apply"] }, { lemma: "make", form: "making", taxonomy: ["bloom-r:create"] }, { lemma: "undertake", form: "undertake", taxonomy: ["none"] }]
    objects: ["qualitative and quantitative data", "techniques"]
    degree: ["very good"]
    independence: []
    scope: ["a range of"]
    deficits: []
- id: cardiffmet/generic-2020/l5/analysis/70-79.s2
  cell: cardiffmet/generic-2020/l5/analysis/70-79
  span: { start: 45936, end: 46207 }
  source: "The student is highly successful in presenting, synthesising and commenting on outcomes and is able to comment perceptively and with insight on the relationship between theory and practice and the impact of the limits of their knowledge on the analysis of their findings."
  versionsFrom: none
  echoes: none
  force: describes
  terms:
    verbs: [{ lemma: "comment", form: "comment", taxonomy: ["none"] }, { lemma: "synthesise", form: "synthesising", taxonomy: ["bloom-r:create/evaluate"] }, { lemma: "present", form: "presenting", taxonomy: ["none"] }]
    objects: ["theory and practice", "knowledge"]
    degree: ["highly", "successful", "perceptively"]
    independence: []
    scope: []
    deficits: []
- id: cardiffmet/generic-2020/l5/analysis/60-69.s1
  cell: cardiffmet/generic-2020/l5/analysis/60-69
  span: { start: 46252, end: 46391 }
  source: "Demonstrates an ability to undertake analysis of qualitative and quantitative data by making good use of a range of established techniques."
  versionsFrom: none
  echoes: none
  force: describes
  terms:
    verbs: [{ lemma: "demonstrate", form: "demonstrates", taxonomy: ["bloom-r:apply/understand"] }, { lemma: "use", form: "use", taxonomy: ["bloom-r:apply"] }, { lemma: "make", form: "making", taxonomy: ["bloom-r:create"] }, { lemma: "undertake", form: "undertake", taxonomy: ["none"] }]
    objects: ["qualitative and quantitative data", "techniques"]
    degree: ["good"]
    independence: []
    scope: ["a range of"]
    deficits: []
- id: cardiffmet/generic-2020/l5/analysis/60-69.s2
  cell: cardiffmet/generic-2020/l5/analysis/60-69
  span: { start: 46392, end: 46669 }
  source: "The student is considerably successful in presenting, synthesising and commenting on outcomes and is able to comment perceptively and with insight on the relationship between theory and practice and the impact of the limits of their knowledge on the analysis of their findings."
  versionsFrom: none
  echoes: none
  force: describes
  terms:
    verbs: [{ lemma: "comment", form: "comment", taxonomy: ["none"] }, { lemma: "synthesise", form: "synthesising", taxonomy: ["bloom-r:create/evaluate"] }, { lemma: "present", form: "presenting", taxonomy: ["none"] }]
    objects: ["theory and practice", "knowledge"]
    degree: ["successful", "perceptively"]
    independence: []
    scope: []
    deficits: []
- id: cardiffmet/generic-2020/l5/analysis/50-59.s1
  cell: cardiffmet/generic-2020/l5/analysis/50-59
  span: { start: 46714, end: 46915 }
  source: "Demonstrates an ability to undertake analysis of qualitative and quantitative data by making use of a range of established techniques and generally has success in presenting and commenting on outcomes."
  versionsFrom: none
  echoes: none
  force: describes
  terms:
    verbs: [{ lemma: "demonstrate", form: "demonstrates", taxonomy: ["bloom-r:apply/understand"] }, { lemma: "comment", form: "commenting", taxonomy: ["none"] }, { lemma: "use", form: "use", taxonomy: ["bloom-r:apply"] }, { lemma: "make", form: "making", taxonomy: ["bloom-r:create"] }, { lemma: "undertake", form: "undertake", taxonomy: ["none"] }, { lemma: "present", form: "presenting", taxonomy: ["none"] }]
    objects: ["qualitative and quantitative data", "techniques"]
    degree: ["generally"]
    independence: []
    scope: ["a range of"]
    deficits: []
- id: cardiffmet/generic-2020/l5/analysis/50-59.s2
  cell: cardiffmet/generic-2020/l5/analysis/50-59
  span: { start: 46916, end: 46976 }
  source: "Awareness of the limits of their knowledge and their impact."
  versionsFrom: none
  echoes: { statement: qaa/fheq-2024/4.12.b4, words: 7 }
  force: describes
  terms:
    verbs: []
    objects: ["knowledge"]
    degree: []
    independence: []
    scope: []
    deficits: []
- id: cardiffmet/generic-2020/l5/analysis/40-49.s1
  cell: cardiffmet/generic-2020/l5/analysis/40-49
  span: { start: 47021, end: 47231 }
  source: "Demonstrates an ability to undertake analysis of qualitative and quantitative data by making basic use of a range of established techniques and has intermittent success in presenting and commenting on outcomes."
  versionsFrom: none
  echoes: none
  force: describes
  terms:
    verbs: [{ lemma: "demonstrate", form: "demonstrates", taxonomy: ["bloom-r:apply/understand"] }, { lemma: "comment", form: "commenting", taxonomy: ["none"] }, { lemma: "use", form: "use", taxonomy: ["bloom-r:apply"] }, { lemma: "make", form: "making", taxonomy: ["bloom-r:create"] }, { lemma: "undertake", form: "undertake", taxonomy: ["none"] }, { lemma: "present", form: "presenting", taxonomy: ["none"] }]
    objects: ["qualitative and quantitative data", "techniques"]
    degree: ["basic"]
    independence: []
    scope: ["basic", "a range of"]
    deficits: []
- id: cardiffmet/generic-2020/l5/analysis/40-49.s2
  cell: cardiffmet/generic-2020/l5/analysis/40-49
  span: { start: 47232, end: 47297 }
  source: "Some awareness of the limits of their knowledge and their impact."
  versionsFrom: none
  echoes: { statement: qaa/fheq-2024/4.12.b4, words: 7 }
  force: describes
  terms:
    verbs: []
    objects: ["knowledge"]
    degree: ["some"]
    independence: []
    scope: []
    deficits: []
- id: cardiffmet/generic-2020/l5/analysis/30-39.s1
  cell: cardiffmet/generic-2020/l5/analysis/30-39
  span: { start: 47349, end: 47526 }
  source: "Is likely to have attempted to undertake analysis of qualitative and quantitative data relevant to the task/discipline but outcomes may be naïve, simplistic and/or unconvincing."
  versionsFrom: none
  echoes: none
  force: describes
  terms:
    verbs: [{ lemma: "undertake", form: "undertake", taxonomy: ["none"] }]
    objects: ["qualitative and quantitative data", "discipline"]
    degree: []
    independence: []
    scope: []
    deficits: ["naïve", "simplistic", "unconvincing"]
- id: cardiffmet/generic-2020/l5/analysis/1-29.s1
  cell: cardiffmet/generic-2020/l5/analysis/1-29
  span: { start: 47576, end: 47710 }
  source: "Demonstrates little evidence of being able to undertake analysis of qualitative and quantitative data relevant to the task/discipline."
  versionsFrom: none
  echoes: none
  force: describes
  terms:
    verbs: [{ lemma: "demonstrate", form: "demonstrates", taxonomy: ["bloom-r:apply/understand"] }, { lemma: "undertake", form: "undertake", taxonomy: ["none"] }]
    objects: ["qualitative and quantitative data", "discipline"]
    degree: ["little"]
    independence: []
    scope: []
    deficits: []
- id: cardiffmet/generic-2020/l5/analysis/1-29.s2
  cell: cardiffmet/generic-2020/l5/analysis/1-29
  span: { start: 47711, end: 47788 }
  source: "Where such work has been attempted, outcomes may be inappropriate, or absent."
  versionsFrom: { sameAs: cardiffmet/generic-2020/l3/analysis/1-29.s2 }
  echoes: none
  force: describes
  terms:
    verbs: []
    objects: []
    degree: []
    independence: []
    scope: []
    deficits: ["absent"]
- id: cardiffmet/generic-2020/l5/research/80-100.s1
  cell: cardiffmet/generic-2020/l5/research/80-100
  span: { start: 47843, end: 47990 }
  source: "In written coursework, reference citations extend significantly beyond the main body of reading normally expected in the discipline/field of study."
  versionsFrom: none
  echoes: none
  force: describes
  terms:
    verbs: [{ lemma: "extend", form: "extend", taxonomy: ["bloom-r:understand"] }]
    objects: ["reading", "discipline", "field of study"]
    degree: []
    independence: []
    scope: ["main"]
    deficits: []
- id: cardiffmet/generic-2020/l5/research/80-100.s2
  cell: cardiffmet/generic-2020/l5/research/80-100
  span: { start: 47991, end: 48064 }
  source: "In examinations, a substantial range of reference citations are included."
  versionsFrom: none
  echoes: none
  force: describes
  terms:
    verbs: []
    objects: []
    degree: []
    independence: []
    scope: []
    deficits: []
- id: cardiffmet/generic-2020/l5/research/80-100.s3
  cell: cardiffmet/generic-2020/l5/research/80-100
  span: { start: 48065, end: 48166 }
  source: "Further to the 70%-79% band, work in the 80%-100% bands would extend beyond that expected at Level 5."
  versionsFrom: { sameAs: cardiffmet/generic-2020/l3/knowledge/80-100.s1 }
  echoes: none
  force: describes
  terms:
    verbs: [{ lemma: "extend", form: "extend", taxonomy: ["bloom-r:understand"] }]
    objects: []
    degree: []
    independence: []
    scope: []
    deficits: []
- id: cardiffmet/generic-2020/l5/research/70-79.s1
  cell: cardiffmet/generic-2020/l5/research/70-79
  span: { start: 48212, end: 48318 }
  source: "Demonstrates a detailed and thorough knowledge of current research/advanced scholarship in the discipline."
  versionsFrom: none
  echoes: none
  force: describes
  terms:
    verbs: [{ lemma: "demonstrate", form: "demonstrates", taxonomy: ["bloom-r:apply/understand"] }]
    objects: ["knowledge", "research", "scholarship", "discipline"]
    degree: ["detailed", "thorough"]
    independence: []
    scope: ["current", "advanced"]
    deficits: []
- id: cardiffmet/generic-2020/l5/research/70-79.s2
  cell: cardiffmet/generic-2020/l5/research/70-79
  span: { start: 48319, end: 48493 }
  source: "The use of scholarly reviews/primary sources is confident and a breadth and depth of individual reading and investigation, extending beyond the sources provided, is apparent."
  versionsFrom: { sameAs: cardiffmet/generic-2020/l4/research/70-79.s2 }
  echoes: none
  force: describes
  terms:
    verbs: [{ lemma: "use", form: "use", taxonomy: ["bloom-r:apply"] }]
    objects: ["primary sources", "reading", "sources"]
    degree: ["confident"]
    independence: []
    scope: []
    deficits: []
- id: cardiffmet/generic-2020/l5/research/70-79.s3
  cell: cardiffmet/generic-2020/l5/research/70-79
  span: { start: 48494, end: 48592 }
  source: "The referencing of literature and other sources is accurate and in line with academic conventions."
  versionsFrom: { sameAs: cardiffmet/generic-2020/l3/research/70-79.s3 }
  echoes: none
  force: describes
  terms:
    verbs: []
    objects: ["referencing", "literature", "sources", "academic conventions"]
    degree: []
    independence: []
    scope: []
    deficits: []
- id: cardiffmet/generic-2020/l5/research/70-79.s4
  cell: cardiffmet/generic-2020/l5/research/70-79
  span: { start: 48593, end: 48792 }
  source: "A thorough knowledge and understanding of research processes, techniques and methods is demonstrated along with an ability to apply research knowledge and skills successfully in appropriate contexts."
  versionsFrom: { like: cardiffmet/generic-2020/l3/research/70-79.s4, similarity: 0.98 }
  echoes: none
  force: describes
  terms:
    verbs: [{ lemma: "demonstrate", form: "demonstrated", taxonomy: ["bloom-r:apply/understand"] }, { lemma: "apply", form: "apply", taxonomy: ["bloom-r:apply", "solo:relational"] }]
    objects: ["knowledge and understanding", "research processes", "techniques", "research", "knowledge"]
    degree: ["thorough", "successfully"]
    independence: []
    scope: []
    deficits: []
- id: cardiffmet/generic-2020/l5/research/60-69.s1
  cell: cardiffmet/generic-2020/l5/research/60-69
  span: { start: 48838, end: 48918 }
  source: "Demonstrates a good knowledge of current research/scholarship in the discipline."
  versionsFrom: none
  echoes: none
  force: describes
  terms:
    verbs: [{ lemma: "demonstrate", form: "demonstrates", taxonomy: ["bloom-r:apply/understand"] }]
    objects: ["knowledge", "research", "scholarship", "discipline"]
    degree: ["good"]
    independence: []
    scope: ["current"]
    deficits: []
- id: cardiffmet/generic-2020/l5/research/60-69.s2
  cell: cardiffmet/generic-2020/l5/research/60-69
  span: { start: 48919, end: 49049 }
  source: "Examples referred to indicate a breadth and depth of individual reading and investigation that extend beyond the sources provided."
  versionsFrom: { sameAs: cardiffmet/generic-2020/l4/research/60-69.s2 }
  echoes: none
  force: describes
  terms:
    verbs: [{ lemma: "extend", form: "extend", taxonomy: ["bloom-r:understand"] }]
    objects: ["reading", "sources"]
    degree: []
    independence: []
    scope: []
    deficits: []
- id: cardiffmet/generic-2020/l5/research/60-69.s3
  cell: cardiffmet/generic-2020/l5/research/60-69
  span: { start: 49050, end: 49124 }
  source: "The referencing of literature and other sources is almost always accurate."
  versionsFrom: { sameAs: cardiffmet/generic-2020/l3/research/60-69.s3 }
  echoes: none
  force: describes
  terms:
    verbs: []
    objects: ["referencing", "literature", "sources"]
    degree: []
    independence: []
    scope: []
    deficits: []
- id: cardiffmet/generic-2020/l5/research/60-69.s4
  cell: cardiffmet/generic-2020/l5/research/60-69
  span: { start: 49125, end: 49265 }
  source: "A secure knowledge of research processes is evident along with an ability to apply research skills and knowledge in the appropriate context."
  versionsFrom: { sameAs: cardiffmet/generic-2020/l3/research/60-69.s4 }
  echoes: none
  force: describes
  terms:
    verbs: [{ lemma: "apply", form: "apply", taxonomy: ["bloom-r:apply", "solo:relational"] }]
    objects: ["knowledge", "research processes", "research", "knowledge"]
    degree: ["secure"]
    independence: []
    scope: []
    deficits: []
- id: cardiffmet/generic-2020/l5/research/50-59.s1
  cell: cardiffmet/generic-2020/l5/research/50-59
  span: { start: 49311, end: 49448 }
  source: "Demonstrates a satisfactory knowledge of current research/scholarship in the discipline and shows an ability to discuss its implications."
  versionsFrom: none
  echoes: none
  force: describes
  terms:
    verbs: [{ lemma: "demonstrate", form: "demonstrates", taxonomy: ["bloom-r:apply/understand"] }]
    objects: ["knowledge", "research", "scholarship", "discipline"]
    degree: ["satisfactory"]
    independence: []
    scope: ["current"]
    deficits: []
- id: cardiffmet/generic-2020/l5/research/50-59.s2
  cell: cardiffmet/generic-2020/l5/research/50-59
  span: { start: 49449, end: 49555 }
  source: "Examples of research/scholarship referred to in the work demonstrate individual reading and investigation."
  versionsFrom: { sameAs: cardiffmet/generic-2020/l3/research/50-59.s2 }
  echoes: none
  force: describes
  terms:
    verbs: [{ lemma: "demonstrate", form: "demonstrate", taxonomy: ["bloom-r:apply/understand"] }]
    objects: ["research", "scholarship", "reading"]
    degree: []
    independence: []
    scope: []
    deficits: []
- id: cardiffmet/generic-2020/l5/research/50-59.s3
  cell: cardiffmet/generic-2020/l5/research/50-59
  span: { start: 49556, end: 49640 }
  source: "Occasional errors may be present in the referencing of literature and other sources."
  versionsFrom: { sameAs: cardiffmet/generic-2020/l3/research/50-59.s3 }
  echoes: none
  force: describes
  terms:
    verbs: [{ lemma: "present", form: "present", taxonomy: ["none"] }]
    objects: ["referencing", "literature", "sources"]
    degree: []
    independence: []
    scope: []
    deficits: ["errors"]
- id: cardiffmet/generic-2020/l5/research/50-59.s4
  cell: cardiffmet/generic-2020/l5/research/50-59
  span: { start: 49641, end: 49817 }
  source: "Some knowledge of research processes is evident and the application of research skills and knowledge is generally successful, although there may be a reliance on tutor support."
  versionsFrom: { sameAs: cardiffmet/generic-2020/l3/research/50-59.s4 }
  echoes: none
  force: describes
  terms:
    verbs: [{ lemma: "apply", form: "application", taxonomy: ["bloom-r:apply", "solo:relational"] }]
    objects: ["knowledge", "research processes", "research", "knowledge"]
    degree: ["some", "generally", "successful"]
    independence: ["reliance on tutor support"]
    scope: []
    deficits: ["reliance"]
- id: cardiffmet/generic-2020/l5/research/40-49.s1
  cell: cardiffmet/generic-2020/l5/research/40-49
  span: { start: 49863, end: 50035 }
  source: "Demonstrates basic knowledge of current research/scholarship in the discipline and demonstrates an ability to provide limited comment and/or discussion of its implications."
  versionsFrom: none
  echoes: none
  force: describes
  terms:
    verbs: [{ lemma: "demonstrate", form: "demonstrates", taxonomy: ["bloom-r:apply/understand"] }, { lemma: "comment", form: "comment", taxonomy: ["none"] }, { lemma: "provide", form: "provide", taxonomy: ["none"] }]
    objects: ["knowledge", "research", "scholarship", "discipline"]
    degree: ["basic", "limited"]
    independence: []
    scope: ["basic", "current"]
    deficits: []
- id: cardiffmet/generic-2020/l5/research/40-49.s2
  cell: cardiffmet/generic-2020/l5/research/40-49
  span: { start: 50036, end: 50195 }
  source: "Examples of research/scholarship referred to in the work may indicate an over-reliance on programme materials rather than individual reading and investigation."
  versionsFrom: { sameAs: cardiffmet/generic-2020/l3/research/40-49.s2 }
  echoes: none
  force: describes
  terms:
    verbs: []
    objects: ["research", "scholarship", "reading"]
    degree: []
    independence: []
    scope: []
    deficits: ["over-reliance"]
- id: cardiffmet/generic-2020/l5/research/40-49.s3
  cell: cardiffmet/generic-2020/l5/research/40-49
  span: { start: 50196, end: 50264 }
  source: "There are errors in the referencing of literature and other sources."
  versionsFrom: { sameAs: cardiffmet/generic-2020/l3/research/40-49.s3 }
  echoes: none
  force: describes
  terms:
    verbs: []
    objects: ["referencing", "literature", "sources"]
    degree: []
    independence: []
    scope: []
    deficits: ["errors"]
- id: cardiffmet/generic-2020/l5/research/40-49.s4
  cell: cardiffmet/generic-2020/l5/research/40-49
  span: { start: 50265, end: 50371 }
  source: "Some knowledge of research processes is evident although the application of such knowledge is less secure."
  versionsFrom: { sameAs: cardiffmet/generic-2020/l3/research/40-49.s4 }
  echoes: none
  force: describes
  terms:
    verbs: [{ lemma: "apply", form: "application", taxonomy: ["bloom-r:apply", "solo:relational"] }]
    objects: ["knowledge", "research processes", "knowledge"]
    degree: ["some", "secure"]
    independence: []
    scope: []
    deficits: []
- id: cardiffmet/generic-2020/l5/research/30-39.s1
  cell: cardiffmet/generic-2020/l5/research/30-39
  span: { start: 50424, end: 50517 }
  source: "Demonstrates limited or sporadic knowledge of current research/scholarship in the discipline."
  versionsFrom: none
  echoes: none
  force: describes
  terms:
    verbs: [{ lemma: "demonstrate", form: "demonstrates", taxonomy: ["bloom-r:apply/understand"] }]
    objects: ["knowledge", "research", "scholarship", "discipline"]
    degree: ["limited"]
    independence: []
    scope: ["current"]
    deficits: []
- id: cardiffmet/generic-2020/l5/research/30-39.s2
  cell: cardiffmet/generic-2020/l5/research/30-39
  span: { start: 50518, end: 50680 }
  source: "A restricted range of sources are used but overall, there is an over-reliance on programme materials with little evidence of individual reading and investigation."
  versionsFrom: { sameAs: cardiffmet/generic-2020/l3/research/30-39.s2 }
  echoes: none
  force: describes
  terms:
    verbs: [{ lemma: "use", form: "used", taxonomy: ["bloom-r:apply"] }]
    objects: ["sources", "reading"]
    degree: ["little"]
    independence: []
    scope: []
    deficits: ["over-reliance"]
- id: cardiffmet/generic-2020/l5/research/30-39.s3
  cell: cardiffmet/generic-2020/l5/research/30-39
  span: { start: 50681, end: 50758 }
  source: "There are frequent errors in the referencing of literature and other sources."
  versionsFrom: { sameAs: cardiffmet/generic-2020/l3/research/30-39.s3 }
  echoes: none
  force: describes
  terms:
    verbs: []
    objects: ["referencing", "literature", "sources"]
    degree: []
    independence: []
    scope: []
    deficits: ["errors"]
- id: cardiffmet/generic-2020/l5/research/30-39.s4
  cell: cardiffmet/generic-2020/l5/research/30-39
  span: { start: 50759, end: 50896 }
  source: "Although limited knowledge of research processes may be evident, nevertheless, the application of such knowledge is largely unsuccessful."
  versionsFrom: { sameAs: cardiffmet/generic-2020/l3/research/30-39.s4 }
  echoes: none
  force: describes
  terms:
    verbs: [{ lemma: "apply", form: "application", taxonomy: ["bloom-r:apply", "solo:relational"] }]
    objects: ["knowledge", "research processes", "knowledge"]
    degree: ["limited"]
    independence: []
    scope: []
    deficits: []
- id: cardiffmet/generic-2020/l5/research/1-29.s1
  cell: cardiffmet/generic-2020/l5/research/1-29
  span: { start: 50947, end: 51027 }
  source: "Demonstrates little knowledge of current research/scholarship in the discipline."
  versionsFrom: none
  echoes: none
  force: describes
  terms:
    verbs: [{ lemma: "demonstrate", form: "demonstrates", taxonomy: ["bloom-r:apply/understand"] }]
    objects: ["knowledge", "research", "scholarship", "discipline"]
    degree: ["little"]
    independence: []
    scope: ["current"]
    deficits: []
- id: cardiffmet/generic-2020/l5/research/1-29.s2
  cell: cardiffmet/generic-2020/l5/research/1-29
  span: { start: 51028, end: 51176 }
  source: "Evidence of individual reading and investigation is negligible and the limited referencing of literature and other sources is frequently inaccurate."
  versionsFrom: { sameAs: cardiffmet/generic-2020/l3/research/1-29.s2 }
  echoes: none
  force: describes
  terms:
    verbs: []
    objects: ["reading", "referencing", "literature", "sources"]
    degree: ["limited"]
    independence: []
    scope: []
    deficits: ["negligible"]
- id: cardiffmet/generic-2020/l5/research/1-29.s3
  cell: cardiffmet/generic-2020/l5/research/1-29
  span: { start: 51177, end: 51281 }
  source: "Very limited knowledge of research processes is apparent and there is a failure to apply this knowledge."
  versionsFrom: { sameAs: cardiffmet/generic-2020/l3/research/1-29.s3 }
  echoes: none
  force: describes
  terms:
    verbs: [{ lemma: "apply", form: "apply", taxonomy: ["bloom-r:apply", "solo:relational"] }]
    objects: ["knowledge", "research processes", "knowledge"]
    degree: ["very limited"]
    independence: []
    scope: []
    deficits: ["failure"]
- id: cardiffmet/generic-2020/l5/argument/80-100.s1
  cell: cardiffmet/generic-2020/l5/argument/80-100
  span: { start: 51357, end: 51483 }
  source: "Important insights are offered that are informed by critical evaluation of current research/scholarship/professional practice."
  versionsFrom: none
  echoes: none
  force: describes
  terms:
    verbs: [{ lemma: "evaluate", form: "evaluation", taxonomy: ["bloom-r:analyze/create/evaluate", "solo:extended-abstract"] }]
    objects: ["research", "scholarship"]
    degree: ["informed"]
    independence: []
    scope: ["current"]
    deficits: []
- id: cardiffmet/generic-2020/l5/argument/80-100.s2
  cell: cardiffmet/generic-2020/l5/argument/80-100
  span: { start: 51484, end: 51585 }
  source: "Further to the 70%-79% band, work in the 80%-100% bands would extend beyond that expected at Level 5."
  versionsFrom: { sameAs: cardiffmet/generic-2020/l3/knowledge/80-100.s1 }
  echoes: none
  force: describes
  terms:
    verbs: [{ lemma: "extend", form: "extend", taxonomy: ["bloom-r:understand"] }]
    objects: []
    degree: []
    independence: []
    scope: []
    deficits: []
- id: cardiffmet/generic-2020/l5/argument/70-79.s1
  cell: cardiffmet/generic-2020/l5/argument/70-79
  span: { start: 51652, end: 51795 }
  source: "Demonstrates an ability to solve broadly defined, complex problems and to engage in critical understanding of principles in the field of study."
  versionsFrom: none
  echoes: none
  force: describes
  terms:
    verbs: [{ lemma: "demonstrate", form: "demonstrates", taxonomy: ["bloom-r:apply/understand"] }, { lemma: "solve", form: "solve", taxonomy: ["bloom-r:analyze/apply/create", "solo:multistructural"] }]
    objects: ["complex problems", "understanding", "principles", "field of study"]
    degree: []
    independence: []
    scope: ["complex"]
    deficits: []
- id: cardiffmet/generic-2020/l5/argument/70-79.s2
  cell: cardiffmet/generic-2020/l5/argument/70-79
  span: { start: 51796, end: 51854 }
  source: "Arguments are well developed, sustained and substantiated."
  versionsFrom: { sameAs: cardiffmet/generic-2020/l4/argument/70-79.s2 }
  echoes: none
  force: describes
  terms:
    verbs: [{ lemma: "develop", form: "developed", taxonomy: ["bloom-r:apply/create"] }, { lemma: "sustain", form: "sustained", taxonomy: ["none"] }]
    objects: ["arguments"]
    degree: ["well"]
    independence: []
    scope: []
    deficits: []
- id: cardiffmet/generic-2020/l5/argument/70-79.s3
  cell: cardiffmet/generic-2020/l5/argument/70-79
  span: { start: 51855, end: 51968 }
  source: "Where relevant, assumptions are challenged and there is clear recognition of the complexities of academic debate."
  versionsFrom: none
  echoes: none
  force: describes
  terms:
    verbs: [{ lemma: "recognise", form: "recognition", taxonomy: ["solo:unistructural"] }, { lemma: "challenge", form: "challenged", taxonomy: ["none"] }]
    objects: []
    degree: ["clear"]
    independence: []
    scope: []
    deficits: []
- id: cardiffmet/generic-2020/l5/argument/70-79.s4
  cell: cardiffmet/generic-2020/l5/argument/70-79
  span: { start: 51969, end: 52093 }
  source: "Appropriate and sometimes innovative solutions are offered to problems, evaluating different approaches to solving problems."
  versionsFrom: none
  echoes: none
  force: describes
  terms:
    verbs: [{ lemma: "evaluate", form: "evaluating", taxonomy: ["bloom-r:analyze/create/evaluate", "solo:extended-abstract"] }, { lemma: "solve", form: "solving", taxonomy: ["bloom-r:analyze/apply/create", "solo:multistructural"] }]
    objects: ["problems", "approaches", "problems"]
    degree: ["innovative"]
    independence: []
    scope: []
    deficits: []
- id: cardiffmet/generic-2020/l5/argument/70-79.s5
  cell: cardiffmet/generic-2020/l5/argument/70-79
  span: { start: 52094, end: 52197 }
  source: "There is strong evidence that the student is able to reflect effectively on the student’s own practice."
  versionsFrom: none
  echoes: none
  force: describes
  terms:
    verbs: [{ lemma: "reflect", form: "reflect", taxonomy: ["solo:extended-abstract"] }]
    objects: ["own practice"]
    degree: ["strong", "effectively"]
    independence: []
    scope: []
    deficits: []
- id: cardiffmet/generic-2020/l5/argument/70-79.s6
  cell: cardiffmet/generic-2020/l5/argument/70-79
  span: { start: 52198, end: 52367 }
  source: "Critical evaluation of the student’s own work and/or professional practice is highly perceptive and there is a full awareness of the implications for future development."
  versionsFrom: { sameAs: cardiffmet/generic-2020/l4/argument/70-79.s6 }
  echoes: none
  force: describes
  terms:
    verbs: [{ lemma: "evaluate", form: "evaluation", taxonomy: ["bloom-r:analyze/create/evaluate", "solo:extended-abstract"] }, { lemma: "develop", form: "development", taxonomy: ["bloom-r:apply/create"] }]
    objects: []
    degree: ["highly", "perceptive"]
    independence: []
    scope: []
    deficits: []
- id: cardiffmet/generic-2020/l5/argument/60-69.s1
  cell: cardiffmet/generic-2020/l5/argument/60-69
  span: { start: 52434, end: 52577 }
  source: "Demonstrates an ability to solve broadly defined, complex problems and to engage in critical understanding of principles in the field of study."
  versionsFrom: { sameAs: cardiffmet/generic-2020/l5/argument/70-79.s1 }
  echoes: none
  force: describes
  terms:
    verbs: [{ lemma: "demonstrate", form: "demonstrates", taxonomy: ["bloom-r:apply/understand"] }, { lemma: "solve", form: "solve", taxonomy: ["bloom-r:analyze/apply/create", "solo:multistructural"] }]
    objects: ["complex problems", "understanding", "principles", "field of study"]
    degree: []
    independence: []
    scope: ["complex"]
    deficits: []
- id: cardiffmet/generic-2020/l5/argument/60-69.s2
  cell: cardiffmet/generic-2020/l5/argument/60-69
  span: { start: 52578, end: 52786 }
  source: "Arguments are clearly considered and substantiated and there is evidence of an ability to make appropriate judgements and to suggest solutions to problems, evaluating different approaches to solving problems."
  versionsFrom: none
  echoes: none
  force: describes
  terms:
    verbs: [{ lemma: "evaluate", form: "evaluating", taxonomy: ["bloom-r:analyze/create/evaluate", "solo:extended-abstract"] }, { lemma: "make", form: "make", taxonomy: ["bloom-r:create"] }, { lemma: "solve", form: "solving", taxonomy: ["bloom-r:analyze/apply/create", "solo:multistructural"] }]
    objects: ["arguments", "problems", "approaches", "problems"]
    degree: ["clearly"]
    independence: []
    scope: []
    deficits: []
- id: cardiffmet/generic-2020/l5/argument/60-69.s3
  cell: cardiffmet/generic-2020/l5/argument/60-69
  span: { start: 52787, end: 52942 }
  source: "The student also demonstrates an ability to engage in reflective practice and to take account of personal evaluations when planning for future development."
  versionsFrom: { like: cardiffmet/generic-2020/l3/argument/60-69.s4, similarity: 0.98 }
  echoes: none
  force: describes
  terms:
    verbs: [{ lemma: "demonstrate", form: "demonstrates", taxonomy: ["bloom-r:apply/understand"] }, { lemma: "evaluate", form: "evaluations", taxonomy: ["bloom-r:analyze/create/evaluate", "solo:extended-abstract"] }, { lemma: "develop", form: "development", taxonomy: ["bloom-r:apply/create"] }, { lemma: "plan", form: "planning", taxonomy: ["bloom-r:create", "solo:relational"] }]
    objects: []
    degree: []
    independence: []
    scope: []
    deficits: []
- id: cardiffmet/generic-2020/l5/argument/50-59.s1
  cell: cardiffmet/generic-2020/l5/argument/50-59
  span: { start: 53009, end: 53246 }
  source: "Demonstrates a satisfactory ability to solve broadly defined, complex problems and to engage in critical understanding of principles in the field of study, although there may be some over-reliance on description and factual presentation."
  versionsFrom: none
  echoes: none
  force: describes
  terms:
    verbs: [{ lemma: "demonstrate", form: "demonstrates", taxonomy: ["bloom-r:apply/understand"] }, { lemma: "present", form: "presentation", taxonomy: ["none"] }, { lemma: "solve", form: "solve", taxonomy: ["bloom-r:analyze/apply/create", "solo:multistructural"] }, { lemma: "describe", form: "description", taxonomy: ["bloom-r:evaluate/remember/understand", "solo:multistructural"] }]
    objects: ["complex problems", "understanding", "principles", "field of study", "presentation"]
    degree: ["satisfactory", "some"]
    independence: []
    scope: ["complex"]
    deficits: ["over-reliance"]
- id: cardiffmet/generic-2020/l5/argument/50-59.s2
  cell: cardiffmet/generic-2020/l5/argument/50-59
  span: { start: 53247, end: 53283 }
  source: "Arguments are usually substantiated."
  versionsFrom: { sameAs: cardiffmet/generic-2020/l3/argument/50-59.s2 }
  echoes: none
  force: describes
  terms:
    verbs: []
    objects: ["arguments"]
    degree: []
    independence: []
    scope: []
    deficits: []
- id: cardiffmet/generic-2020/l5/argument/50-59.s3
  cell: cardiffmet/generic-2020/l5/argument/50-59
  span: { start: 53284, end: 53486 }
  source: "There is some evidence of the student’s ability to evaluate and reflect on the student’s own practice, but reflections may lack insight and the implications for future development may be underestimated."
  versionsFrom: { sameAs: cardiffmet/generic-2020/l3/argument/50-59.s3 }
  echoes: none
  force: describes
  terms:
    verbs: [{ lemma: "evaluate", form: "evaluate", taxonomy: ["bloom-r:analyze/create/evaluate", "solo:extended-abstract"] }, { lemma: "develop", form: "development", taxonomy: ["bloom-r:apply/create"] }, { lemma: "reflect", form: "reflect", taxonomy: ["solo:extended-abstract"] }]
    objects: ["own practice"]
    degree: ["some"]
    independence: []
    scope: []
    deficits: ["lack"]
- id: cardiffmet/generic-2020/l5/argument/40-49.s1
  cell: cardiffmet/generic-2020/l5/argument/40-49
  span: { start: 53553, end: 53701 }
  source: "Demonstrates a basic ability to solve broadly defined, complex problems and to engage in critical understanding of principles in the field of study."
  versionsFrom: none
  echoes: none
  force: describes
  terms:
    verbs: [{ lemma: "demonstrate", form: "demonstrates", taxonomy: ["bloom-r:apply/understand"] }, { lemma: "solve", form: "solve", taxonomy: ["bloom-r:analyze/apply/create", "solo:multistructural"] }]
    objects: ["complex problems", "understanding", "principles", "field of study"]
    degree: ["basic"]
    independence: []
    scope: ["basic", "complex"]
    deficits: []
- id: cardiffmet/generic-2020/l5/argument/40-49.s2
  cell: cardiffmet/generic-2020/l5/argument/40-49
  span: { start: 53702, end: 53842 }
  source: "Although some critical reflection is evident, the balance within the work is likely to be in favour of description and factual presentation."
  versionsFrom: none
  echoes: none
  force: describes
  terms:
    verbs: [{ lemma: "reflect", form: "reflection", taxonomy: ["solo:extended-abstract"] }, { lemma: "present", form: "presentation", taxonomy: ["none"] }, { lemma: "describe", form: "description", taxonomy: ["bloom-r:evaluate/remember/understand", "solo:multistructural"] }]
    objects: ["presentation"]
    degree: ["some"]
    independence: []
    scope: []
    deficits: []
- id: cardiffmet/generic-2020/l5/argument/40-49.s3
  cell: cardiffmet/generic-2020/l5/argument/40-49
  span: { start: 53843, end: 53908 }
  source: "Arguments are generally substantiated but may be under-developed."
  versionsFrom: { sameAs: cardiffmet/generic-2020/l3/argument/40-49.s3 }
  echoes: none
  force: describes
  terms:
    verbs: []
    objects: ["arguments"]
    degree: ["generally"]
    independence: []
    scope: []
    deficits: []
- id: cardiffmet/generic-2020/l5/argument/40-49.s4
  cell: cardiffmet/generic-2020/l5/argument/40-49
  span: { start: 53909, end: 54132 }
  source: "There is some evidence of the student’s ability to evaluate and reflect on the student’s own practice. although reflections may be limited and superficial with little consideration of their relevance for future development."
  versionsFrom: { sameAs: cardiffmet/generic-2020/l3/argument/40-49.s4 }
  echoes: none
  force: describes
  terms:
    verbs: [{ lemma: "evaluate", form: "evaluate", taxonomy: ["bloom-r:analyze/create/evaluate", "solo:extended-abstract"] }, { lemma: "develop", form: "development", taxonomy: ["bloom-r:apply/create"] }, { lemma: "consider", form: "consideration", taxonomy: ["none"] }, { lemma: "reflect", form: "reflect", taxonomy: ["solo:extended-abstract"] }]
    objects: ["own practice"]
    degree: ["some", "limited", "little"]
    independence: []
    scope: []
    deficits: ["superficial"]
- id: cardiffmet/generic-2020/l5/argument/30-39.s1
  cell: cardiffmet/generic-2020/l5/argument/30-39
  span: { start: 54206, end: 54365 }
  source: "Demonstrates little evidence of ability to solve broadly defined, complex problems and to engage in critical understanding of principles in the field of study."
  versionsFrom: none
  echoes: none
  force: describes
  terms:
    verbs: [{ lemma: "demonstrate", form: "demonstrates", taxonomy: ["bloom-r:apply/understand"] }, { lemma: "solve", form: "solve", taxonomy: ["bloom-r:analyze/apply/create", "solo:multistructural"] }]
    objects: ["complex problems", "understanding", "principles", "field of study"]
    degree: ["little"]
    independence: []
    scope: ["complex"]
    deficits: []
- id: cardiffmet/generic-2020/l5/argument/30-39.s2
  cell: cardiffmet/generic-2020/l5/argument/30-39
  span: { start: 54366, end: 54452 }
  source: "The work is largely descriptive and arguments, if attempted, are rarely substantiated."
  versionsFrom: { sameAs: cardiffmet/generic-2020/l3/argument/30-39.s2 }
  echoes: none
  force: describes
  terms:
    verbs: [{ lemma: "describe", form: "descriptive", taxonomy: ["bloom-r:evaluate/remember/understand", "solo:multistructural"] }]
    objects: ["arguments"]
    degree: []
    independence: []
    scope: []
    deficits: []
- id: cardiffmet/generic-2020/l5/argument/30-39.s3
  cell: cardiffmet/generic-2020/l5/argument/30-39
  span: { start: 54453, end: 54537 }
  source: "Self-evaluation and reflections on the student’s own practice are extremely limited."
  versionsFrom: { sameAs: cardiffmet/generic-2020/l3/argument/30-39.s3 }
  echoes: none
  force: describes
  terms:
    verbs: []
    objects: ["own practice"]
    degree: ["limited"]
    independence: []
    scope: []
    deficits: []
- id: cardiffmet/generic-2020/l5/argument/1-29.s1
  cell: cardiffmet/generic-2020/l5/argument/1-29
  span: { start: 54609, end: 54801 }
  source: "Demonstrates little ability to describe and report but very little evidence is available to indicate an ability to solve broadly defined, complex problems and engage in critical understanding."
  versionsFrom: none
  echoes: none
  force: describes
  terms:
    verbs: [{ lemma: "demonstrate", form: "demonstrates", taxonomy: ["bloom-r:apply/understand"] }, { lemma: "solve", form: "solve", taxonomy: ["bloom-r:analyze/apply/create", "solo:multistructural"] }, { lemma: "describe", form: "describe", taxonomy: ["bloom-r:evaluate/remember/understand", "solo:multistructural"] }, { lemma: "report", form: "report", taxonomy: ["bloom-r:apply/understand", "solo:multistructural"] }]
    objects: ["complex problems", "understanding"]
    degree: ["little", "very little"]
    independence: []
    scope: ["complex"]
    deficits: []
- id: cardiffmet/generic-2020/l5/argument/1-29.s2
  cell: cardiffmet/generic-2020/l5/argument/1-29
  span: { start: 54802, end: 54889 }
  source: "Self-evaluation and reflections on the student’s own practice are negligible or absent."
  versionsFrom: { sameAs: cardiffmet/generic-2020/l3/argument/1-29.s2 }
  echoes: none
  force: describes
  terms:
    verbs: []
    objects: ["own practice"]
    degree: []
    independence: []
    scope: []
    deficits: ["negligible", "absent"]
- id: cardiffmet/generic-2020/l6/overall/80-100.s1
  cell: cardiffmet/generic-2020/l6/overall/80-100
  span: { start: 54971, end: 55203 }
  source: "A full and detailed understanding of the set task and an ability to have met the learning outcomes and address the assessment criteria at an excellent level (80-89%) or outstanding and exceptional level (90-100%) and beyond level 6."
  versionsFrom: { sameAs: cardiffmet/generic-2020/l3/overall/80-100.s1 }
  echoes: none
  force: describes
  terms:
    verbs: [{ lemma: "address", form: "address", taxonomy: ["none"] }, { lemma: "meet", form: "met", taxonomy: ["none"] }]
    objects: ["understanding", "set task", "learning outcomes", "assessment criteria"]
    degree: ["detailed", "excellent", "outstanding", "exceptional"]
    independence: []
    scope: ["beyond level"]
    deficits: []
- id: cardiffmet/generic-2020/l6/overall/80-100.s2
  cell: cardiffmet/generic-2020/l6/overall/80-100
  span: { start: 55204, end: 55309 }
  source: "Work is of a standard deemed to be worthy of publication/manufacture/public exhibition/public performance"
  versionsFrom: none
  echoes: none
  force: describes
  terms:
    verbs: []
    objects: []
    degree: []
    independence: []
    scope: []
    deficits: []
- id: cardiffmet/generic-2020/l6/overall/70-79.s1
  cell: cardiffmet/generic-2020/l6/overall/70-79
  span: { start: 55348, end: 55504 }
  source: "A full and detailed understanding of the set task and an ability to have met the learning outcomes and address the assessment criteria at a very good level."
  versionsFrom: { sameAs: cardiffmet/generic-2020/l3/overall/70-79.s1 }
  echoes: none
  force: describes
  terms:
    verbs: [{ lemma: "address", form: "address", taxonomy: ["none"] }, { lemma: "meet", form: "met", taxonomy: ["none"] }]
    objects: ["understanding", "set task", "learning outcomes", "assessment criteria"]
    degree: ["detailed", "very good"]
    independence: []
    scope: []
    deficits: []
- id: cardiffmet/generic-2020/l6/overall/60-69.s1
  cell: cardiffmet/generic-2020/l6/overall/60-69
  span: { start: 55543, end: 55681 }
  source: "A full understanding of the set task and an ability to have met the learning outcomes and address the assessment criteria at a good level."
  versionsFrom: { sameAs: cardiffmet/generic-2020/l3/overall/60-69.s1 }
  echoes: none
  force: describes
  terms:
    verbs: [{ lemma: "address", form: "address", taxonomy: ["none"] }, { lemma: "meet", form: "met", taxonomy: ["none"] }]
    objects: ["understanding", "set task", "learning outcomes", "assessment criteria"]
    degree: ["good"]
    independence: []
    scope: []
    deficits: []
- id: cardiffmet/generic-2020/l6/overall/50-59.s1
  cell: cardiffmet/generic-2020/l6/overall/50-59
  span: { start: 55720, end: 55879 }
  source: "A secure understanding of the set task and an ability to have met the associated learning outcomes and address the assessment criteria at a satisfactory level."
  versionsFrom: { sameAs: cardiffmet/generic-2020/l3/overall/50-59.s1 }
  echoes: none
  force: describes
  terms:
    verbs: [{ lemma: "address", form: "address", taxonomy: ["none"] }, { lemma: "meet", form: "met", taxonomy: ["none"] }]
    objects: ["understanding", "set task", "learning outcomes", "assessment criteria"]
    degree: ["secure", "satisfactory"]
    independence: []
    scope: []
    deficits: []
- id: cardiffmet/generic-2020/l6/overall/40-49.s1
  cell: cardiffmet/generic-2020/l6/overall/40-49
  span: { start: 55918, end: 56073 }
  source: "A basic understanding of the set task and an ability to have met the associated learning outcomes and address the assessment criteria at a threshold level."
  versionsFrom: { sameAs: cardiffmet/generic-2020/l3/overall/40-49.s1 }
  echoes: none
  force: describes
  terms:
    verbs: [{ lemma: "address", form: "address", taxonomy: ["none"] }, { lemma: "meet", form: "met", taxonomy: ["none"] }]
    objects: ["understanding", "set task", "learning outcomes", "assessment criteria"]
    degree: ["basic"]
    independence: []
    scope: ["basic"]
    deficits: []
- id: cardiffmet/generic-2020/l6/overall/30-39.s1
  cell: cardiffmet/generic-2020/l6/overall/30-39
  span: { start: 56119, end: 56142 }
  source: "Unsatisfactory overall."
  versionsFrom: { sameAs: cardiffmet/generic-2020/l3/overall/30-39.s1 }
  echoes: none
  force: describes
  terms:
    verbs: []
    objects: []
    degree: []
    independence: []
    scope: []
    deficits: []
- id: cardiffmet/generic-2020/l6/overall/30-39.s2
  cell: cardiffmet/generic-2020/l6/overall/30-39
  span: { start: 56143, end: 56268 }
  source: "A partial understanding of the set task and an ability to have met some of the associated learning outcomes at a basic level."
  versionsFrom: { sameAs: cardiffmet/generic-2020/l3/overall/30-39.s2 }
  echoes: none
  force: describes
  terms:
    verbs: [{ lemma: "meet", form: "met", taxonomy: ["none"] }]
    objects: ["understanding", "set task", "learning outcomes"]
    degree: ["some", "basic"]
    independence: []
    scope: ["basic"]
    deficits: []
- id: cardiffmet/generic-2020/l6/overall/30-39.s3
  cell: cardiffmet/generic-2020/l6/overall/30-39
  span: { start: 56269, end: 56376 }
  source: "However, attainment is uneven with some learning outcomes not met and some assessment criteria unaddressed."
  versionsFrom: { sameAs: cardiffmet/generic-2020/l3/overall/30-39.s3 }
  echoes: none
  force: describes
  terms:
    verbs: [{ lemma: "meet", form: "met", taxonomy: ["none"] }]
    objects: ["learning outcomes", "assessment criteria"]
    degree: ["some", "some"]
    independence: []
    scope: []
    deficits: ["not", "unaddressed"]
- id: cardiffmet/generic-2020/l6/overall/1-29.s1
  cell: cardiffmet/generic-2020/l6/overall/1-29
  span: { start: 56420, end: 56433 }
  source: "Poor overall."
  versionsFrom: { sameAs: cardiffmet/generic-2020/l3/overall/1-29.s1 }
  echoes: none
  force: describes
  terms:
    verbs: []
    objects: []
    degree: ["poor"]
    independence: []
    scope: []
    deficits: []
- id: cardiffmet/generic-2020/l6/overall/1-29.s2
  cell: cardiffmet/generic-2020/l6/overall/1-29
  span: { start: 56434, end: 56529 }
  source: "Minimal understanding of the set task and will partially have met one or two learning outcomes."
  versionsFrom: none
  echoes: none
  force: describes
  terms:
    verbs: [{ lemma: "meet", form: "met", taxonomy: ["none"] }]
    objects: ["understanding", "set task", "learning outcomes"]
    degree: ["minimal"]
    independence: []
    scope: []
    deficits: []
- id: cardiffmet/generic-2020/l6/overall/1-29.s3
  cell: cardiffmet/generic-2020/l6/overall/1-29
  span: { start: 56530, end: 56571 }
  source: "Many assessment criteria are unaddressed."
  versionsFrom: { sameAs: cardiffmet/generic-2020/l3/overall/1-29.s4 }
  echoes: none
  force: describes
  terms:
    verbs: []
    objects: ["assessment criteria"]
    degree: []
    independence: []
    scope: []
    deficits: ["unaddressed"]
- id: cardiffmet/generic-2020/l6/knowledge/80-100.s1
  cell: cardiffmet/generic-2020/l6/knowledge/80-100
  span: { start: 56629, end: 56730 }
  source: "Further to the 70%-79% band, work in the 80%-100% bands would extend beyond that expected at Level 6."
  versionsFrom: { sameAs: cardiffmet/generic-2020/l3/knowledge/80-100.s1 }
  echoes: none
  force: describes
  terms:
    verbs: [{ lemma: "extend", form: "extend", taxonomy: ["bloom-r:understand"] }]
    objects: []
    degree: []
    independence: []
    scope: []
    deficits: []
- id: cardiffmet/generic-2020/l6/knowledge/80-100.s2
  cell: cardiffmet/generic-2020/l6/knowledge/80-100
  span: { start: 56731, end: 56795 }
  source: "Demonstrates exceptional knowledge and systematic understanding."
  versionsFrom: none
  echoes: none
  force: describes
  terms:
    verbs: [{ lemma: "demonstrate", form: "demonstrates", taxonomy: ["bloom-r:apply/understand"] }]
    objects: ["knowledge", "understanding"]
    degree: ["exceptional"]
    independence: []
    scope: ["systematic"]
    deficits: []
- id: cardiffmet/generic-2020/l6/knowledge/70-79.s1
  cell: cardiffmet/generic-2020/l6/knowledge/70-79
  span: { start: 56844, end: 56952 }
  source: "A detailed knowledge and systematic understanding of key aspects of the field of study relevant to the task."
  versionsFrom: none
  echoes: none
  force: describes
  terms:
    verbs: []
    objects: ["knowledge", "understanding", "field of study"]
    degree: ["detailed"]
    independence: []
    scope: ["systematic", "key"]
    deficits: []
- id: cardiffmet/generic-2020/l6/knowledge/70-79.s2
  cell: cardiffmet/generic-2020/l6/knowledge/70-79
  span: { start: 56953, end: 57038 }
  source: "There is strong evidence of an ability to extend, transform and apply such knowledge."
  versionsFrom: { sameAs: cardiffmet/generic-2020/l5/knowledge/70-79.s2 }
  echoes: none
  force: describes
  terms:
    verbs: [{ lemma: "apply", form: "apply", taxonomy: ["bloom-r:apply", "solo:relational"] }, { lemma: "extend", form: "extend", taxonomy: ["bloom-r:understand"] }, { lemma: "transform", form: "transform", taxonomy: ["none"] }]
    objects: ["knowledge"]
    degree: ["strong"]
    independence: []
    scope: []
    deficits: []
- id: cardiffmet/generic-2020/l6/knowledge/70-79.s3
  cell: cardiffmet/generic-2020/l6/knowledge/70-79
  span: { start: 57039, end: 57210 }
  source: "The student also demonstrates an ability to engage in confident discussion of complex concepts and to recognise the limitations and/or ambiguity of disciplinary knowledge."
  versionsFrom: { sameAs: cardiffmet/generic-2020/l5/knowledge/70-79.s3 }
  echoes: none
  force: describes
  terms:
    verbs: [{ lemma: "demonstrate", form: "demonstrates", taxonomy: ["bloom-r:apply/understand"] }, { lemma: "recognise", form: "recognise", taxonomy: ["solo:unistructural"] }]
    objects: ["concepts", "limitations", "knowledge"]
    degree: ["confident"]
    independence: []
    scope: ["complex"]
    deficits: []
- id: cardiffmet/generic-2020/l6/knowledge/70-79.s4
  cell: cardiffmet/generic-2020/l6/knowledge/70-79
  span: { start: 57211, end: 57326 }
  source: "Independent thinking and original insights and self-management of learning are also features of work at this level."
  versionsFrom: none
  echoes: none
  force: describes
  terms:
    verbs: []
    objects: []
    degree: []
    independence: ["independent thinking"]
    scope: ["original", "at this level"]
    deficits: []
- id: cardiffmet/generic-2020/l6/knowledge/60-69.s1
  cell: cardiffmet/generic-2020/l6/knowledge/60-69
  span: { start: 57375, end: 57481 }
  source: "A detailed knowledge and thorough understanding of key aspects of the field of study relevant to the task."
  versionsFrom: none
  echoes: none
  force: describes
  terms:
    verbs: []
    objects: ["knowledge", "understanding", "field of study"]
    degree: ["detailed", "thorough"]
    independence: []
    scope: ["key"]
    deficits: []
- id: cardiffmet/generic-2020/l6/knowledge/60-69.s2
  cell: cardiffmet/generic-2020/l6/knowledge/60-69
  span: { start: 57482, end: 57594 }
  source: "There is clear evidence of an ability to apply such knowledge and, in some contexts, to extend and transform it."
  versionsFrom: { sameAs: cardiffmet/generic-2020/l4/knowledge/60-69.s2 }
  echoes: none
  force: describes
  terms:
    verbs: [{ lemma: "apply", form: "apply", taxonomy: ["bloom-r:apply", "solo:relational"] }, { lemma: "extend", form: "extend", taxonomy: ["bloom-r:understand"] }, { lemma: "transform", form: "transform", taxonomy: ["none"] }]
    objects: ["knowledge"]
    degree: ["clear", "some"]
    independence: []
    scope: []
    deficits: []
- id: cardiffmet/generic-2020/l6/knowledge/60-69.s3
  cell: cardiffmet/generic-2020/l6/knowledge/60-69
  span: { start: 57595, end: 57738 }
  source: "The discussion of complex concepts is often tackled successfully and there is evidence of independent thinking and self-management of learning."
  versionsFrom: none
  echoes: none
  force: describes
  terms:
    verbs: []
    objects: ["concepts"]
    degree: ["successfully"]
    independence: ["independent thinking"]
    scope: ["complex"]
    deficits: []
- id: cardiffmet/generic-2020/l6/knowledge/50-59.s1
  cell: cardiffmet/generic-2020/l6/knowledge/50-59
  span: { start: 57787, end: 57951 }
  source: "A sound knowledge and understanding of most key aspects of the field of study relevant to the task and there is some evidence of an ability to apply such knowledge."
  versionsFrom: none
  echoes: none
  force: describes
  terms:
    verbs: [{ lemma: "apply", form: "apply", taxonomy: ["bloom-r:apply", "solo:relational"] }]
    objects: ["knowledge and understanding", "field of study", "knowledge"]
    degree: ["sound", "some"]
    independence: []
    scope: ["key"]
    deficits: []
- id: cardiffmet/generic-2020/l6/knowledge/50-59.s2
  cell: cardiffmet/generic-2020/l6/knowledge/50-59
  span: { start: 57952, end: 58115 }
  source: "Although there may be a tendency to reproduce information received from elsewhere (e.g. programme materials), there is still some evidence of independent thinking."
  versionsFrom: { sameAs: cardiffmet/generic-2020/l5/knowledge/50-59.s3 }
  echoes: none
  force: describes
  terms:
    verbs: [{ lemma: "reproduce", form: "reproduce", taxonomy: ["bloom-r:remember", "solo:unistructural"] }]
    objects: ["information"]
    degree: ["some"]
    independence: ["independent thinking"]
    scope: []
    deficits: []
- id: cardiffmet/generic-2020/l6/knowledge/50-59.s3
  cell: cardiffmet/generic-2020/l6/knowledge/50-59
  span: { start: 58116, end: 58208 }
  source: "A few errors and/or misconceptions may be present, but these will not be in important areas."
  versionsFrom: { sameAs: cardiffmet/generic-2020/l3/knowledge/50-59.s3 }
  echoes: none
  force: describes
  terms:
    verbs: [{ lemma: "present", form: "present", taxonomy: ["none"] }]
    objects: []
    degree: []
    independence: []
    scope: []
    deficits: ["errors", "misconceptions", "not"]
- id: cardiffmet/generic-2020/l6/knowledge/50-59.s4
  cell: cardiffmet/generic-2020/l6/knowledge/50-59
  span: { start: 58209, end: 58249 }
  source: "Evidence of self-management of learning."
  versionsFrom: none
  echoes: none
  force: describes
  terms:
    verbs: []
    objects: []
    degree: []
    independence: []
    scope: []
    deficits: []
- id: cardiffmet/generic-2020/l6/knowledge/40-49.s1
  cell: cardiffmet/generic-2020/l6/knowledge/40-49
  span: { start: 58298, end: 58393 }
  source: "A basic knowledge and understanding of many aspects of the field of study relevant to the task."
  versionsFrom: none
  echoes: none
  force: describes
  terms:
    verbs: []
    objects: ["knowledge and understanding", "field of study"]
    degree: ["basic"]
    independence: []
    scope: ["basic"]
    deficits: []
- id: cardiffmet/generic-2020/l6/knowledge/40-49.s2
  cell: cardiffmet/generic-2020/l6/knowledge/40-49
  span: { start: 58394, end: 58513 }
  source: "Reproducing information received from elsewhere (e.g. programme materials) is a frequent feature of work at this level."
  versionsFrom: { sameAs: cardiffmet/generic-2020/l3/knowledge/40-49.s2 }
  echoes: none
  force: describes
  terms:
    verbs: [{ lemma: "reproduce", form: "reproducing", taxonomy: ["bloom-r:remember", "solo:unistructural"] }]
    objects: ["information"]
    degree: []
    independence: []
    scope: ["at this level"]
    deficits: []
- id: cardiffmet/generic-2020/l6/knowledge/40-49.s3
  cell: cardiffmet/generic-2020/l6/knowledge/40-49
  span: { start: 58514, end: 58648 }
  source: "Errors and misconceptions will be evident, but these are outweighed by the degree of knowledge and understanding demonstrated overall."
  versionsFrom: { sameAs: cardiffmet/generic-2020/l3/knowledge/40-49.s3 }
  echoes: none
  force: describes
  terms:
    verbs: [{ lemma: "demonstrate", form: "demonstrated", taxonomy: ["bloom-r:apply/understand"] }]
    objects: ["knowledge and understanding"]
    degree: []
    independence: []
    scope: []
    deficits: ["errors", "misconceptions"]
- id: cardiffmet/generic-2020/l6/knowledge/40-49.s4
  cell: cardiffmet/generic-2020/l6/knowledge/40-49
  span: { start: 58649, end: 58689 }
  source: "Evidence of self-management of learning."
  versionsFrom: { sameAs: cardiffmet/generic-2020/l6/knowledge/50-59.s4 }
  echoes: none
  force: describes
  terms:
    verbs: []
    objects: []
    degree: []
    independence: []
    scope: []
    deficits: []
- id: cardiffmet/generic-2020/l6/knowledge/30-39.s1
  cell: cardiffmet/generic-2020/l6/knowledge/30-39
  span: { start: 58745, end: 58824 }
  source: "Limited knowledge and understanding of the field of study relevant to the task."
  versionsFrom: none
  echoes: none
  force: describes
  terms:
    verbs: []
    objects: ["knowledge and understanding", "field of study"]
    degree: ["limited"]
    independence: []
    scope: []
    deficits: []
- id: cardiffmet/generic-2020/l6/knowledge/30-39.s2
  cell: cardiffmet/generic-2020/l6/knowledge/30-39
  span: { start: 58825, end: 58968 }
  source: "Factual inaccuracies, errors and misconceptions are evident in important areas and elements of the assessed work may be irrelevant to the task."
  versionsFrom: { sameAs: cardiffmet/generic-2020/l3/knowledge/30-39.s2 }
  echoes: none
  force: describes
  terms:
    verbs: []
    objects: []
    degree: []
    independence: []
    scope: []
    deficits: ["inaccuracies", "errors", "misconceptions", "irrelevant"]
- id: cardiffmet/generic-2020/l6/knowledge/1-29.s1
  cell: cardiffmet/generic-2020/l6/knowledge/1-29
  span: { start: 59022, end: 59100 }
  source: "Little knowledge and understanding of the field of study relevant to the task."
  versionsFrom: none
  echoes: none
  force: describes
  terms:
    verbs: []
    objects: ["knowledge and understanding", "field of study"]
    degree: ["little"]
    independence: []
    scope: []
    deficits: []
- id: cardiffmet/generic-2020/l6/knowledge/1-29.s2
  cell: cardiffmet/generic-2020/l6/knowledge/1-29
  span: { start: 59101, end: 59259 }
  source: "Factual inaccuracies, errors and misconceptions are evident in many important areas and these outweigh the degree of knowledge and understanding demonstrated."
  versionsFrom: { sameAs: cardiffmet/generic-2020/l3/knowledge/1-29.s2 }
  echoes: none
  force: describes
  terms:
    verbs: [{ lemma: "demonstrate", form: "demonstrated", taxonomy: ["bloom-r:apply/understand"] }]
    objects: ["knowledge and understanding"]
    degree: []
    independence: []
    scope: []
    deficits: ["inaccuracies", "errors", "misconceptions"]
- id: cardiffmet/generic-2020/l6/knowledge/1-29.s3
  cell: cardiffmet/generic-2020/l6/knowledge/1-29
  span: { start: 59260, end: 59332 }
  source: "Substantial elements of the assessed work may be irrelevant to the task."
  versionsFrom: { sameAs: cardiffmet/generic-2020/l3/knowledge/1-29.s3 }
  echoes: none
  force: describes
  terms:
    verbs: []
    objects: []
    degree: []
    independence: []
    scope: []
    deficits: ["irrelevant"]
- id: cardiffmet/generic-2020/l6/presentation/80-100.s1
  cell: cardiffmet/generic-2020/l6/presentation/80-100
  span: { start: 59395, end: 59496 }
  source: "Further to the 70%-79% band, work in the 80%-100% bands would extend beyond that expected at Level 6."
  versionsFrom: { sameAs: cardiffmet/generic-2020/l3/knowledge/80-100.s1 }
  echoes: none
  force: describes
  terms:
    verbs: [{ lemma: "extend", form: "extend", taxonomy: ["bloom-r:understand"] }]
    objects: []
    degree: []
    independence: []
    scope: []
    deficits: []
- id: cardiffmet/generic-2020/l6/presentation/80-100.s2
  cell: cardiffmet/generic-2020/l6/presentation/80-100
  span: { start: 59497, end: 59589 }
  source: "The standard of presentation attains the professional standards expected for the discipline."
  versionsFrom: none
  echoes: none
  force: describes
  terms:
    verbs: [{ lemma: "present", form: "presentation", taxonomy: ["none"] }]
    objects: ["presentation", "discipline"]
    degree: []
    independence: []
    scope: []
    deficits: []
- id: cardiffmet/generic-2020/l6/presentation/70-79.s1
  cell: cardiffmet/generic-2020/l6/presentation/70-79
  span: { start: 59643, end: 59768 }
  source: "An ability to communicate information, complex ideas and concepts in a coherent and succinct manner in a range of situations."
  versionsFrom: none
  echoes: none
  force: describes
  terms:
    verbs: [{ lemma: "communicate", form: "communicate", taxonomy: ["none"] }]
    objects: ["information", "ideas", "concepts"]
    degree: []
    independence: []
    scope: ["complex", "a range of"]
    deficits: []
- id: cardiffmet/generic-2020/l6/presentation/70-79.s2
  cell: cardiffmet/generic-2020/l6/presentation/70-79
  span: { start: 59769, end: 59833 }
  source: "The standard of presentation is high and the format appropriate."
  versionsFrom: { sameAs: cardiffmet/generic-2020/l3/presentation/70-79.s2 }
  echoes: none
  force: describes
  terms:
    verbs: [{ lemma: "present", form: "presentation", taxonomy: ["none"] }]
    objects: ["presentation"]
    degree: ["high"]
    independence: []
    scope: []
    deficits: []
- id: cardiffmet/generic-2020/l6/presentation/70-79.s3
  cell: cardiffmet/generic-2020/l6/presentation/70-79
  span: { start: 59834, end: 59920 }
  source: "Key points are logically organised and in written work, the style is lucid and mature."
  versionsFrom: { sameAs: cardiffmet/generic-2020/l5/presentation/70-79.s3 }
  echoes: none
  force: describes
  terms:
    verbs: []
    objects: []
    degree: []
    independence: []
    scope: ["key"]
    deficits: []
- id: cardiffmet/generic-2020/l6/presentation/70-79.s4
  cell: cardiffmet/generic-2020/l6/presentation/70-79
  span: { start: 59921, end: 59972 }
  source: "Arguments are well-defined and clearly articulated."
  versionsFrom: { sameAs: cardiffmet/generic-2020/l3/presentation/70-79.s4 }
  echoes: none
  force: describes
  terms:
    verbs: []
    objects: ["arguments"]
    degree: ["clearly"]
    independence: []
    scope: ["well-defined"]
    deficits: []
- id: cardiffmet/generic-2020/l6/presentation/60-69.s1
  cell: cardiffmet/generic-2020/l6/presentation/60-69
  span: { start: 60026, end: 60132 }
  source: "An ability to communicate information, ideas and concepts clearly and succinctly in a range of situations."
  versionsFrom: none
  echoes: none
  force: describes
  terms:
    verbs: [{ lemma: "communicate", form: "communicate", taxonomy: ["none"] }]
    objects: ["information", "ideas", "concepts"]
    degree: ["clearly"]
    independence: []
    scope: ["a range of"]
    deficits: []
- id: cardiffmet/generic-2020/l6/presentation/60-69.s2
  cell: cardiffmet/generic-2020/l6/presentation/60-69
  span: { start: 60133, end: 60183 }
  source: "Work is well presented and the format appropriate."
  versionsFrom: { sameAs: cardiffmet/generic-2020/l3/presentation/60-69.s2 }
  echoes: none
  force: describes
  terms:
    verbs: []
    objects: []
    degree: ["well"]
    independence: []
    scope: []
    deficits: []
- id: cardiffmet/generic-2020/l6/presentation/60-69.s3
  cell: cardiffmet/generic-2020/l6/presentation/60-69
  span: { start: 60184, end: 60307 }
  source: "Key points are appropriately organised and in written work, the writing style is fluent and arguments are well articulated."
  versionsFrom: { sameAs: cardiffmet/generic-2020/l3/presentation/60-69.s3 }
  echoes: none
  force: describes
  terms:
    verbs: []
    objects: ["arguments"]
    degree: ["well"]
    independence: []
    scope: ["key"]
    deficits: []
- id: cardiffmet/generic-2020/l6/presentation/50-59.s1
  cell: cardiffmet/generic-2020/l6/presentation/50-59
  span: { start: 60361, end: 60493 }
  source: "Demonstrates a satisfactory ability to communicate information, ideas, concepts and arguments successfully in a range of situations."
  versionsFrom: none
  echoes: none
  force: describes
  terms:
    verbs: [{ lemma: "demonstrate", form: "demonstrates", taxonomy: ["bloom-r:apply/understand"] }, { lemma: "communicate", form: "communicate", taxonomy: ["none"] }]
    objects: ["information", "ideas", "concepts", "arguments"]
    degree: ["satisfactory", "successfully"]
    independence: []
    scope: ["a range of"]
    deficits: []
- id: cardiffmet/generic-2020/l6/presentation/50-59.s2
  cell: cardiffmet/generic-2020/l6/presentation/50-59
  span: { start: 60494, end: 60556 }
  source: "Overall, the structure and format of the work are appropriate."
  versionsFrom: { sameAs: cardiffmet/generic-2020/l3/presentation/50-59.s2 }
  echoes: none
  force: describes
  terms:
    verbs: []
    objects: ["structure"]
    degree: []
    independence: []
    scope: []
    deficits: []
- id: cardiffmet/generic-2020/l6/presentation/50-59.s3
  cell: cardiffmet/generic-2020/l6/presentation/50-59
  span: { start: 60557, end: 60681 }
  source: "There may be occasional faults in the presentation of work but overall, these do not detract from the clarity of expression."
  versionsFrom: { sameAs: cardiffmet/generic-2020/l3/presentation/50-59.s3 }
  echoes: none
  force: describes
  terms:
    verbs: [{ lemma: "present", form: "presentation", taxonomy: ["none"] }]
    objects: ["presentation"]
    degree: []
    independence: []
    scope: []
    deficits: ["not"]
- id: cardiffmet/generic-2020/l6/presentation/40-49.s1
  cell: cardiffmet/generic-2020/l6/presentation/40-49
  span: { start: 60735, end: 60831 }
  source: "Some ability to communicate information, ideas, concepts and arguments in a range of situations."
  versionsFrom: none
  echoes: none
  force: describes
  terms:
    verbs: [{ lemma: "communicate", form: "communicate", taxonomy: ["none"] }]
    objects: ["information", "ideas", "concepts", "arguments"]
    degree: ["some"]
    independence: []
    scope: ["a range of"]
    deficits: []
- id: cardiffmet/generic-2020/l6/presentation/40-49.s2
  cell: cardiffmet/generic-2020/l6/presentation/40-49
  span: { start: 60832, end: 60954 }
  source: "However, more success is achieved in describing and reporting factual information rather than communicating complex ideas."
  versionsFrom: { sameAs: cardiffmet/generic-2020/l3/presentation/40-49.s2 }
  echoes: none
  force: describes
  terms:
    verbs: [{ lemma: "communicate", form: "communicating", taxonomy: ["none"] }, { lemma: "describe", form: "describing", taxonomy: ["bloom-r:evaluate/remember/understand", "solo:multistructural"] }, { lemma: "report", form: "reporting", taxonomy: ["bloom-r:apply/understand", "solo:multistructural"] }]
    objects: ["information", "ideas"]
    degree: []
    independence: []
    scope: ["complex"]
    deficits: []
- id: cardiffmet/generic-2020/l6/presentation/40-49.s3
  cell: cardiffmet/generic-2020/l6/presentation/40-49
  span: { start: 60955, end: 61054 }
  source: "Generally, the work is appropriately structured although key points may not be logically sequenced."
  versionsFrom: { sameAs: cardiffmet/generic-2020/l3/presentation/40-49.s3 }
  echoes: none
  force: describes
  terms:
    verbs: []
    objects: []
    degree: ["generally"]
    independence: []
    scope: ["key"]
    deficits: ["not"]
- id: cardiffmet/generic-2020/l6/presentation/40-49.s4
  cell: cardiffmet/generic-2020/l6/presentation/40-49
  span: { start: 61055, end: 61141 }
  source: "Although there will be faults in the presentation of work, the meaning is still clear."
  versionsFrom: { sameAs: cardiffmet/generic-2020/l3/presentation/40-49.s4 }
  echoes: none
  force: describes
  terms:
    verbs: [{ lemma: "present", form: "presentation", taxonomy: ["none"] }]
    objects: ["presentation"]
    degree: ["clear"]
    independence: []
    scope: []
    deficits: []
- id: cardiffmet/generic-2020/l6/presentation/30-39.s1
  cell: cardiffmet/generic-2020/l6/presentation/30-39
  span: { start: 61202, end: 61301 }
  source: "Limited ability to communicate simple concepts and/or factual information in a range of situations."
  versionsFrom: none
  echoes: none
  force: describes
  terms:
    verbs: [{ lemma: "communicate", form: "communicate", taxonomy: ["none"] }]
    objects: ["concepts", "information"]
    degree: ["limited"]
    independence: []
    scope: ["a range of"]
    deficits: []
- id: cardiffmet/generic-2020/l6/presentation/30-39.s2
  cell: cardiffmet/generic-2020/l6/presentation/30-39
  span: { start: 61302, end: 61414 }
  source: "However, faults in the presentation of work and in its structure and organisation mar the clarity of expression."
  versionsFrom: none
  echoes: none
  force: describes
  terms:
    verbs: [{ lemma: "present", form: "presentation", taxonomy: ["none"] }]
    objects: ["presentation", "structure"]
    degree: []
    independence: []
    scope: []
    deficits: []
- id: cardiffmet/generic-2020/l6/presentation/30-39.s3
  cell: cardiffmet/generic-2020/l6/presentation/30-39
  span: { start: 61415, end: 61521 }
  source: "If attempted, the presentation of arguments and more complex ideas may be confused and clumsily expressed."
  versionsFrom: { sameAs: cardiffmet/generic-2020/l3/presentation/30-39.s3 }
  echoes: none
  force: describes
  terms:
    verbs: [{ lemma: "present", form: "presentation", taxonomy: ["none"] }]
    objects: ["presentation", "arguments", "ideas"]
    degree: []
    independence: []
    scope: ["complex"]
    deficits: ["confused"]
- id: cardiffmet/generic-2020/l6/presentation/1-29.s1
  cell: cardiffmet/generic-2020/l6/presentation/1-29
  span: { start: 61580, end: 61653 }
  source: "Little ability to communicate simple concepts and/or factual information."
  versionsFrom: none
  echoes: none
  force: describes
  terms:
    verbs: [{ lemma: "communicate", form: "communicate", taxonomy: ["none"] }]
    objects: ["concepts", "information"]
    degree: ["little"]
    independence: []
    scope: []
    deficits: []
- id: cardiffmet/generic-2020/l6/presentation/1-29.s2
  cell: cardiffmet/generic-2020/l6/presentation/1-29
  span: { start: 61654, end: 61806 }
  source: "Frequent faults in the presentation of work and significant difficulties in its structure and organisation detract from the clarity and meaning overall."
  versionsFrom: { sameAs: cardiffmet/generic-2020/l3/presentation/1-29.s2 }
  echoes: none
  force: describes
  terms:
    verbs: [{ lemma: "present", form: "presentation", taxonomy: ["none"] }]
    objects: ["presentation", "structure"]
    degree: []
    independence: []
    scope: []
    deficits: []
- id: cardiffmet/generic-2020/l6/presentation/1-29.s3
  cell: cardiffmet/generic-2020/l6/presentation/1-29
  span: { start: 61807, end: 61859 }
  source: "The writing style is often clumsy and inappropriate."
  versionsFrom: { sameAs: cardiffmet/generic-2020/l3/presentation/1-29.s3 }
  echoes: none
  force: describes
  terms:
    verbs: []
    objects: []
    degree: []
    independence: []
    scope: []
    deficits: ["clumsy"]
- id: cardiffmet/generic-2020/l6/analysis/80-100.s1
  cell: cardiffmet/generic-2020/l6/analysis/80-100
  span: { start: 61913, end: 62073 }
  source: "The student demonstrates the ability to design and undertake their own research or advanced scholarship, applying relevant techniques and methods appropriately."
  versionsFrom: { like: cardiffmet/generic-2020/l5/analysis/80-100.s1, similarity: 0.95 }
  echoes: none
  force: describes
  terms:
    verbs: [{ lemma: "demonstrate", form: "demonstrates", taxonomy: ["bloom-r:apply/understand"] }, { lemma: "apply", form: "applying", taxonomy: ["bloom-r:apply", "solo:relational"] }, { lemma: "undertake", form: "undertake", taxonomy: ["none"] }]
    objects: ["research", "scholarship", "techniques"]
    degree: []
    independence: []
    scope: ["advanced"]
    deficits: []
- id: cardiffmet/generic-2020/l6/analysis/70-79.s1
  cell: cardiffmet/generic-2020/l6/analysis/70-79
  span: { start: 62118, end: 62312 }
  source: "An ability to undertake detailed analysis and critical enquiry of qualitative and quantitative data relevant to the task/discipline by making very good use of a number of appropriate techniques."
  versionsFrom: none
  echoes: none
  force: describes
  terms:
    verbs: [{ lemma: "use", form: "use", taxonomy: ["bloom-r:apply"] }, { lemma: "make", form: "making", taxonomy: ["bloom-r:create"] }, { lemma: "undertake", form: "undertake", taxonomy: ["none"] }]
    objects: ["qualitative and quantitative data", "discipline", "techniques"]
    degree: ["detailed", "very good"]
    independence: []
    scope: []
    deficits: []
- id: cardiffmet/generic-2020/l6/analysis/70-79.s2
  cell: cardiffmet/generic-2020/l6/analysis/70-79
  span: { start: 62313, end: 62597 }
  source: "The student is highly successful in presenting, synthesising and commenting on outcomes and is able to comment perceptively and with insight on the relationship between theory and practice and the impact of uncertainty, assumptions and the limits of their knowledge on their findings."
  versionsFrom: none
  echoes: none
  force: describes
  terms:
    verbs: [{ lemma: "comment", form: "comment", taxonomy: ["none"] }, { lemma: "synthesise", form: "synthesising", taxonomy: ["bloom-r:create/evaluate"] }, { lemma: "present", form: "presenting", taxonomy: ["none"] }]
    objects: ["theory and practice", "knowledge"]
    degree: ["highly", "successful", "perceptively"]
    independence: []
    scope: []
    deficits: []
- id: cardiffmet/generic-2020/l6/analysis/60-69.s1
  cell: cardiffmet/generic-2020/l6/analysis/60-69
  span: { start: 62642, end: 62861 }
  source: "An ability to undertake detailed analysis and critical enquiry relevant to the task/discipline by making use of appropriate techniques and has considerable success in presenting, synthesising and commenting on outcomes."
  versionsFrom: none
  echoes: none
  force: describes
  terms:
    verbs: [{ lemma: "comment", form: "commenting", taxonomy: ["none"] }, { lemma: "use", form: "use", taxonomy: ["bloom-r:apply"] }, { lemma: "make", form: "making", taxonomy: ["bloom-r:create"] }, { lemma: "undertake", form: "undertake", taxonomy: ["none"] }, { lemma: "synthesise", form: "synthesising", taxonomy: ["bloom-r:create/evaluate"] }, { lemma: "present", form: "presenting", taxonomy: ["none"] }]
    objects: ["discipline", "techniques"]
    degree: ["detailed"]
    independence: []
    scope: []
    deficits: []
- id: cardiffmet/generic-2020/l6/analysis/60-69.s2
  cell: cardiffmet/generic-2020/l6/analysis/60-69
  span: { start: 62862, end: 63002 }
  source: "There is some linkage between theory and practice and awareness of the impact of uncertainty, assumptions and the limits of their knowledge."
  versionsFrom: none
  echoes: none
  force: describes
  terms:
    verbs: []
    objects: ["theory and practice", "knowledge"]
    degree: ["some"]
    independence: []
    scope: []
    deficits: []
- id: cardiffmet/generic-2020/l6/analysis/50-59.s1
  cell: cardiffmet/generic-2020/l6/analysis/50-59
  span: { start: 63047, end: 63299 }
  source: "An ability to utilise some techniques to undertake analysis and enquiry relevant to the task/discipline and generally has success in presenting and commenting on outcomes, with an awareness of uncertainty, assumptions and the limits of their knowledge."
  versionsFrom: none
  echoes: none
  force: describes
  terms:
    verbs: [{ lemma: "comment", form: "commenting", taxonomy: ["none"] }, { lemma: "undertake", form: "undertake", taxonomy: ["none"] }, { lemma: "present", form: "presenting", taxonomy: ["none"] }]
    objects: ["techniques", "discipline", "knowledge"]
    degree: ["some", "generally"]
    independence: []
    scope: []
    deficits: []
- id: cardiffmet/generic-2020/l6/analysis/40-49.s1
  cell: cardiffmet/generic-2020/l6/analysis/40-49
  span: { start: 63344, end: 63598 }
  source: "An ability to undertake some limited analysis and enquiry relevant to the task/discipline and has intermittent success in presenting, synthesising and commenting on outcomes with an awareness of uncertainty, assumptions and the limits of their knowledge."
  versionsFrom: none
  echoes: none
  force: describes
  terms:
    verbs: [{ lemma: "comment", form: "commenting", taxonomy: ["none"] }, { lemma: "undertake", form: "undertake", taxonomy: ["none"] }, { lemma: "synthesise", form: "synthesising", taxonomy: ["bloom-r:create/evaluate"] }, { lemma: "present", form: "presenting", taxonomy: ["none"] }]
    objects: ["discipline", "knowledge"]
    degree: ["some", "limited"]
    independence: []
    scope: []
    deficits: []
- id: cardiffmet/generic-2020/l6/analysis/30-39.s1
  cell: cardiffmet/generic-2020/l6/analysis/30-39
  span: { start: 63650, end: 63829 }
  source: "Likely to have attempted some enquiry and analysis of qualitative and quantitative data relevant to the task/discipline, but outcomes may be naïve, simplistic and/or unconvincing."
  versionsFrom: none
  echoes: none
  force: describes
  terms:
    verbs: []
    objects: ["qualitative and quantitative data", "discipline"]
    degree: ["some"]
    independence: []
    scope: []
    deficits: ["naïve", "simplistic", "unconvincing"]
- id: cardiffmet/generic-2020/l6/analysis/1-29.s1
  cell: cardiffmet/generic-2020/l6/analysis/1-29
  span: { start: 63879, end: 64012 }
  source: "Little evidence of being able to undertake enquiry and analysis of qualitative and quantitative data relevant to the task/discipline."
  versionsFrom: none
  echoes: none
  force: describes
  terms:
    verbs: [{ lemma: "undertake", form: "undertake", taxonomy: ["none"] }]
    objects: ["qualitative and quantitative data", "discipline"]
    degree: ["little"]
    independence: []
    scope: []
    deficits: []
- id: cardiffmet/generic-2020/l6/analysis/1-29.s2
  cell: cardiffmet/generic-2020/l6/analysis/1-29
  span: { start: 64013, end: 64090 }
  source: "Where such work has been attempted, outcomes may be inappropriate, or absent."
  versionsFrom: { sameAs: cardiffmet/generic-2020/l3/analysis/1-29.s2 }
  echoes: none
  force: describes
  terms:
    verbs: []
    objects: []
    degree: []
    independence: []
    scope: []
    deficits: ["absent"]
- id: cardiffmet/generic-2020/l6/research/80-100.s1
  cell: cardiffmet/generic-2020/l6/research/80-100
  span: { start: 64145, end: 64292 }
  source: "In written coursework, reference citations extend significantly beyond the main body of reading normally expected in the discipline/field of study."
  versionsFrom: { sameAs: cardiffmet/generic-2020/l5/research/80-100.s1 }
  echoes: none
  force: describes
  terms:
    verbs: [{ lemma: "extend", form: "extend", taxonomy: ["bloom-r:understand"] }]
    objects: ["reading", "discipline", "field of study"]
    degree: []
    independence: []
    scope: ["main"]
    deficits: []
- id: cardiffmet/generic-2020/l6/research/80-100.s2
  cell: cardiffmet/generic-2020/l6/research/80-100
  span: { start: 64293, end: 64366 }
  source: "In examinations, a substantial range of reference citations are included."
  versionsFrom: { sameAs: cardiffmet/generic-2020/l5/research/80-100.s2 }
  echoes: none
  force: describes
  terms:
    verbs: []
    objects: []
    degree: []
    independence: []
    scope: []
    deficits: []
- id: cardiffmet/generic-2020/l6/research/70-79.s1
  cell: cardiffmet/generic-2020/l6/research/70-79
  span: { start: 64412, end: 64531 }
  source: "A detailed, thorough knowledge and systematic understanding of current research/advanced scholarship in the discipline."
  versionsFrom: none
  echoes: none
  force: describes
  terms:
    verbs: []
    objects: ["knowledge", "understanding", "research", "scholarship", "discipline"]
    degree: ["detailed", "thorough"]
    independence: []
    scope: ["systematic", "current", "advanced"]
    deficits: []
- id: cardiffmet/generic-2020/l6/research/70-79.s2
  cell: cardiffmet/generic-2020/l6/research/70-79
  span: { start: 64532, end: 64706 }
  source: "The use of scholarly reviews/primary sources is confident and a breadth and depth of individual reading and investigation, extending beyond the sources provided, is apparent."
  versionsFrom: { sameAs: cardiffmet/generic-2020/l4/research/70-79.s2 }
  echoes: none
  force: describes
  terms:
    verbs: [{ lemma: "use", form: "use", taxonomy: ["bloom-r:apply"] }]
    objects: ["primary sources", "reading", "sources"]
    degree: ["confident"]
    independence: []
    scope: []
    deficits: []
- id: cardiffmet/generic-2020/l6/research/70-79.s3
  cell: cardiffmet/generic-2020/l6/research/70-79
  span: { start: 64707, end: 64805 }
  source: "The referencing of literature and other sources is accurate and in line with academic conventions."
  versionsFrom: { sameAs: cardiffmet/generic-2020/l3/research/70-79.s3 }
  echoes: none
  force: describes
  terms:
    verbs: []
    objects: ["referencing", "literature", "sources", "academic conventions"]
    degree: []
    independence: []
    scope: []
    deficits: []
- id: cardiffmet/generic-2020/l6/research/70-79.s4
  cell: cardiffmet/generic-2020/l6/research/70-79
  span: { start: 64806, end: 65032 }
  source: "A thorough knowledge and understanding of research processes, techniques and methods is demonstrated along with an ability to determine, refine, adapt and use research knowledge and skills successfully in appropriate contexts."
  versionsFrom: none
  echoes: none
  force: describes
  terms:
    verbs: [{ lemma: "demonstrate", form: "demonstrated", taxonomy: ["bloom-r:apply/understand"] }, { lemma: "use", form: "use", taxonomy: ["bloom-r:apply"] }, { lemma: "adapt", form: "adapt", taxonomy: ["bloom-r:apply/create", "solo:relational"] }]
    objects: ["knowledge and understanding", "research processes", "techniques", "research", "knowledge"]
    degree: ["thorough", "successfully"]
    independence: []
    scope: []
    deficits: []
- id: cardiffmet/generic-2020/l6/research/60-69.s1
  cell: cardiffmet/generic-2020/l6/research/60-69
  span: { start: 65078, end: 65167 }
  source: "A thorough knowledge and understanding of current research/scholarship in the discipline."
  versionsFrom: none
  echoes: none
  force: describes
  terms:
    verbs: []
    objects: ["knowledge and understanding", "research", "scholarship", "discipline"]
    degree: ["thorough"]
    independence: []
    scope: ["current"]
    deficits: []
- id: cardiffmet/generic-2020/l6/research/60-69.s2
  cell: cardiffmet/generic-2020/l6/research/60-69
  span: { start: 65168, end: 65298 }
  source: "Examples referred to indicate a breadth and depth of individual reading and investigation that extend beyond the sources provided."
  versionsFrom: { sameAs: cardiffmet/generic-2020/l4/research/60-69.s2 }
  echoes: none
  force: describes
  terms:
    verbs: [{ lemma: "extend", form: "extend", taxonomy: ["bloom-r:understand"] }]
    objects: ["reading", "sources"]
    degree: []
    independence: []
    scope: []
    deficits: []
- id: cardiffmet/generic-2020/l6/research/60-69.s3
  cell: cardiffmet/generic-2020/l6/research/60-69
  span: { start: 65299, end: 65373 }
  source: "The referencing of literature and other sources is almost always accurate."
  versionsFrom: { sameAs: cardiffmet/generic-2020/l3/research/60-69.s3 }
  echoes: none
  force: describes
  terms:
    verbs: []
    objects: ["referencing", "literature", "sources"]
    degree: []
    independence: []
    scope: []
    deficits: []
- id: cardiffmet/generic-2020/l6/research/60-69.s4
  cell: cardiffmet/generic-2020/l6/research/60-69
  span: { start: 65374, end: 65541 }
  source: "A secure knowledge of research processes is evident along with an ability to determine, refine, adapt and use research skills and knowledge in the appropriate context."
  versionsFrom: none
  echoes: none
  force: describes
  terms:
    verbs: [{ lemma: "use", form: "use", taxonomy: ["bloom-r:apply"] }, { lemma: "adapt", form: "adapt", taxonomy: ["bloom-r:apply/create", "solo:relational"] }]
    objects: ["knowledge", "research processes", "research", "knowledge"]
    degree: ["secure"]
    independence: []
    scope: []
    deficits: []
- id: cardiffmet/generic-2020/l6/research/50-59.s1
  cell: cardiffmet/generic-2020/l6/research/50-59
  span: { start: 65587, end: 65722 }
  source: "A sound knowledge and understanding of current research/scholarship in the discipline and shows an ability to discuss its implications."
  versionsFrom: none
  echoes: none
  force: describes
  terms:
    verbs: []
    objects: ["knowledge and understanding", "research", "scholarship", "discipline"]
    degree: ["sound"]
    independence: []
    scope: ["current"]
    deficits: []
- id: cardiffmet/generic-2020/l6/research/50-59.s2
  cell: cardiffmet/generic-2020/l6/research/50-59
  span: { start: 65723, end: 65829 }
  source: "Examples of research/scholarship referred to in the work demonstrate individual reading and investigation."
  versionsFrom: { sameAs: cardiffmet/generic-2020/l3/research/50-59.s2 }
  echoes: none
  force: describes
  terms:
    verbs: [{ lemma: "demonstrate", form: "demonstrate", taxonomy: ["bloom-r:apply/understand"] }]
    objects: ["research", "scholarship", "reading"]
    degree: []
    independence: []
    scope: []
    deficits: []
- id: cardiffmet/generic-2020/l6/research/50-59.s3
  cell: cardiffmet/generic-2020/l6/research/50-59
  span: { start: 65830, end: 65914 }
  source: "Occasional errors may be present in the referencing of literature and other sources."
  versionsFrom: { sameAs: cardiffmet/generic-2020/l3/research/50-59.s3 }
  echoes: none
  force: describes
  terms:
    verbs: [{ lemma: "present", form: "present", taxonomy: ["none"] }]
    objects: ["referencing", "literature", "sources"]
    degree: []
    independence: []
    scope: []
    deficits: ["errors"]
- id: cardiffmet/generic-2020/l6/research/50-59.s4
  cell: cardiffmet/generic-2020/l6/research/50-59
  span: { start: 65915, end: 66091 }
  source: "Some knowledge of research processes is evident and the application of research skills and knowledge is generally successful, although there may be a reliance on tutor support."
  versionsFrom: { sameAs: cardiffmet/generic-2020/l3/research/50-59.s4 }
  echoes: none
  force: describes
  terms:
    verbs: [{ lemma: "apply", form: "application", taxonomy: ["bloom-r:apply", "solo:relational"] }]
    objects: ["knowledge", "research processes", "research", "knowledge"]
    degree: ["some", "generally", "successful"]
    independence: ["reliance on tutor support"]
    scope: []
    deficits: ["reliance"]
- id: cardiffmet/generic-2020/l6/research/40-49.s1
  cell: cardiffmet/generic-2020/l6/research/40-49
  span: { start: 66137, end: 66313 }
  source: "Some knowledge and understanding of current research/scholarship in the discipline and demonstrates an ability to provide limited comment and/or discussion of its implications."
  versionsFrom: none
  echoes: none
  force: describes
  terms:
    verbs: [{ lemma: "demonstrate", form: "demonstrates", taxonomy: ["bloom-r:apply/understand"] }, { lemma: "comment", form: "comment", taxonomy: ["none"] }, { lemma: "provide", form: "provide", taxonomy: ["none"] }]
    objects: ["knowledge and understanding", "research", "scholarship", "discipline"]
    degree: ["some", "limited"]
    independence: []
    scope: ["current"]
    deficits: []
- id: cardiffmet/generic-2020/l6/research/40-49.s2
  cell: cardiffmet/generic-2020/l6/research/40-49
  span: { start: 66314, end: 66473 }
  source: "Examples of research/scholarship referred to in the work may indicate an over-reliance on programme materials rather than individual reading and investigation."
  versionsFrom: { sameAs: cardiffmet/generic-2020/l3/research/40-49.s2 }
  echoes: none
  force: describes
  terms:
    verbs: []
    objects: ["research", "scholarship", "reading"]
    degree: []
    independence: []
    scope: []
    deficits: ["over-reliance"]
- id: cardiffmet/generic-2020/l6/research/40-49.s3
  cell: cardiffmet/generic-2020/l6/research/40-49
  span: { start: 66474, end: 66542 }
  source: "There are errors in the referencing of literature and other sources."
  versionsFrom: { sameAs: cardiffmet/generic-2020/l3/research/40-49.s3 }
  echoes: none
  force: describes
  terms:
    verbs: []
    objects: ["referencing", "literature", "sources"]
    degree: []
    independence: []
    scope: []
    deficits: ["errors"]
- id: cardiffmet/generic-2020/l6/research/40-49.s4
  cell: cardiffmet/generic-2020/l6/research/40-49
  span: { start: 66543, end: 66649 }
  source: "Some knowledge of research processes is evident although the application of such knowledge is less secure."
  versionsFrom: { sameAs: cardiffmet/generic-2020/l3/research/40-49.s4 }
  echoes: none
  force: describes
  terms:
    verbs: [{ lemma: "apply", form: "application", taxonomy: ["bloom-r:apply", "solo:relational"] }]
    objects: ["knowledge", "research processes", "knowledge"]
    degree: ["some", "secure"]
    independence: []
    scope: []
    deficits: []
- id: cardiffmet/generic-2020/l6/research/30-39.s1
  cell: cardiffmet/generic-2020/l6/research/30-39
  span: { start: 66702, end: 66800 }
  source: "Limited or sporadic knowledge and understanding of current research/scholarship in the discipline."
  versionsFrom: none
  echoes: none
  force: describes
  terms:
    verbs: []
    objects: ["knowledge and understanding", "research", "scholarship", "discipline"]
    degree: ["limited"]
    independence: []
    scope: ["current"]
    deficits: []
- id: cardiffmet/generic-2020/l6/research/30-39.s2
  cell: cardiffmet/generic-2020/l6/research/30-39
  span: { start: 66801, end: 66963 }
  source: "A restricted range of sources are used but overall, there is an over-reliance on programme materials with little evidence of individual reading and investigation."
  versionsFrom: { sameAs: cardiffmet/generic-2020/l3/research/30-39.s2 }
  echoes: none
  force: describes
  terms:
    verbs: [{ lemma: "use", form: "used", taxonomy: ["bloom-r:apply"] }]
    objects: ["sources", "reading"]
    degree: ["little"]
    independence: []
    scope: []
    deficits: ["over-reliance"]
- id: cardiffmet/generic-2020/l6/research/30-39.s3
  cell: cardiffmet/generic-2020/l6/research/30-39
  span: { start: 66964, end: 67041 }
  source: "There are frequent errors in the referencing of literature and other sources."
  versionsFrom: { sameAs: cardiffmet/generic-2020/l3/research/30-39.s3 }
  echoes: none
  force: describes
  terms:
    verbs: []
    objects: ["referencing", "literature", "sources"]
    degree: []
    independence: []
    scope: []
    deficits: ["errors"]
- id: cardiffmet/generic-2020/l6/research/30-39.s4
  cell: cardiffmet/generic-2020/l6/research/30-39
  span: { start: 67042, end: 67179 }
  source: "Although limited knowledge of research processes may be evident, nevertheless, the application of such knowledge is largely unsuccessful."
  versionsFrom: { sameAs: cardiffmet/generic-2020/l3/research/30-39.s4 }
  echoes: none
  force: describes
  terms:
    verbs: [{ lemma: "apply", form: "application", taxonomy: ["bloom-r:apply", "solo:relational"] }]
    objects: ["knowledge", "research processes", "knowledge"]
    degree: ["limited"]
    independence: []
    scope: []
    deficits: []
- id: cardiffmet/generic-2020/l6/research/1-29.s1
  cell: cardiffmet/generic-2020/l6/research/1-29
  span: { start: 67230, end: 67315 }
  source: "Little knowledge and understanding of current research/scholarship in the discipline."
  versionsFrom: none
  echoes: none
  force: describes
  terms:
    verbs: []
    objects: ["knowledge and understanding", "research", "scholarship", "discipline"]
    degree: ["little"]
    independence: []
    scope: ["current"]
    deficits: []
- id: cardiffmet/generic-2020/l6/research/1-29.s2
  cell: cardiffmet/generic-2020/l6/research/1-29
  span: { start: 67316, end: 67379 }
  source: "Evidence of individual reading and investigation is negligible."
  versionsFrom: none
  echoes: none
  force: describes
  terms:
    verbs: []
    objects: ["reading"]
    degree: []
    independence: []
    scope: []
    deficits: ["negligible"]
- id: cardiffmet/generic-2020/l6/research/1-29.s3
  cell: cardiffmet/generic-2020/l6/research/1-29
  span: { start: 67380, end: 67457 }
  source: "Limited referencing of literature and other sources is frequently inaccurate."
  versionsFrom: none
  echoes: none
  force: describes
  terms:
    verbs: []
    objects: ["referencing", "literature", "sources"]
    degree: ["limited"]
    independence: []
    scope: []
    deficits: []
- id: cardiffmet/generic-2020/l6/research/1-29.s4
  cell: cardiffmet/generic-2020/l6/research/1-29
  span: { start: 67458, end: 67562 }
  source: "Very limited knowledge of research processes is apparent and there is a failure to apply this knowledge."
  versionsFrom: { sameAs: cardiffmet/generic-2020/l3/research/1-29.s3 }
  echoes: none
  force: describes
  terms:
    verbs: [{ lemma: "apply", form: "apply", taxonomy: ["bloom-r:apply", "solo:relational"] }]
    objects: ["knowledge", "research processes", "knowledge"]
    degree: ["very limited"]
    independence: []
    scope: []
    deficits: ["failure"]
- id: cardiffmet/generic-2020/l6/argument/80-100.s1
  cell: cardiffmet/generic-2020/l6/argument/80-100
  span: { start: 67638, end: 67777 }
  source: "Work may challenge the boundaries of knowledge within the discipline/field of study and is informed by innovative and/or creative thinking."
  versionsFrom: none
  echoes: none
  force: describes
  terms:
    verbs: [{ lemma: "challenge", form: "challenge", taxonomy: ["none"] }]
    objects: ["knowledge", "discipline", "field of study"]
    degree: ["informed", "innovative"]
    independence: []
    scope: []
    deficits: []
- id: cardiffmet/generic-2020/l6/argument/80-100.s2
  cell: cardiffmet/generic-2020/l6/argument/80-100
  span: { start: 67778, end: 67900 }
  source: "New insights are offered that are informed by critical evaluation of current research/ scholarship/ professional practice."
  versionsFrom: none
  echoes: none
  force: describes
  terms:
    verbs: [{ lemma: "evaluate", form: "evaluation", taxonomy: ["bloom-r:analyze/create/evaluate", "solo:extended-abstract"] }]
    objects: ["research", "scholarship"]
    degree: ["informed"]
    independence: []
    scope: ["current"]
    deficits: []
- id: cardiffmet/generic-2020/l6/argument/70-79.s1
  cell: cardiffmet/generic-2020/l6/argument/70-79
  span: { start: 67967, end: 68086 }
  source: "An ability to engage in critical evaluation of concepts/arguments/data and to make appropriate and informed judgements."
  versionsFrom: none
  echoes: none
  force: describes
  terms:
    verbs: [{ lemma: "evaluate", form: "evaluation", taxonomy: ["bloom-r:analyze/create/evaluate", "solo:extended-abstract"] }, { lemma: "make", form: "make", taxonomy: ["bloom-r:create"] }]
    objects: ["concepts", "arguments", "data"]
    degree: ["informed"]
    independence: []
    scope: []
    deficits: []
- id: cardiffmet/generic-2020/l6/argument/70-79.s2
  cell: cardiffmet/generic-2020/l6/argument/70-79
  span: { start: 68087, end: 68145 }
  source: "Arguments are well developed, sustained and substantiated."
  versionsFrom: { sameAs: cardiffmet/generic-2020/l4/argument/70-79.s2 }
  echoes: none
  force: describes
  terms:
    verbs: [{ lemma: "develop", form: "developed", taxonomy: ["bloom-r:apply/create"] }, { lemma: "sustain", form: "sustained", taxonomy: ["none"] }]
    objects: ["arguments"]
    degree: ["well"]
    independence: []
    scope: []
    deficits: []
- id: cardiffmet/generic-2020/l6/argument/70-79.s3
  cell: cardiffmet/generic-2020/l6/argument/70-79
  span: { start: 68146, end: 68259 }
  source: "Where relevant, assumptions are challenged and there is clear recognition of the complexities of academic debate."
  versionsFrom: { sameAs: cardiffmet/generic-2020/l5/argument/70-79.s3 }
  echoes: none
  force: describes
  terms:
    verbs: [{ lemma: "recognise", form: "recognition", taxonomy: ["solo:unistructural"] }, { lemma: "challenge", form: "challenged", taxonomy: ["none"] }]
    objects: []
    degree: ["clear"]
    independence: []
    scope: []
    deficits: []
- id: cardiffmet/generic-2020/l6/argument/70-79.s4
  cell: cardiffmet/generic-2020/l6/argument/70-79
  span: { start: 68260, end: 68393 }
  source: "Appropriate and sometimes innovative solutions are offered to problems that have limited definition and multiple interacting factors."
  versionsFrom: none
  echoes: none
  force: describes
  terms:
    verbs: [{ lemma: "solve", form: "solutions", taxonomy: ["bloom-r:analyze/apply/create", "solo:multistructural"] }]
    objects: ["problems"]
    degree: ["innovative", "limited"]
    independence: []
    scope: []
    deficits: []
- id: cardiffmet/generic-2020/l6/argument/70-79.s5
  cell: cardiffmet/generic-2020/l6/argument/70-79
  span: { start: 68394, end: 68497 }
  source: "There is strong evidence that the student is able to reflect effectively on the student’s own practice."
  versionsFrom: { sameAs: cardiffmet/generic-2020/l5/argument/70-79.s5 }
  echoes: none
  force: describes
  terms:
    verbs: [{ lemma: "reflect", form: "reflect", taxonomy: ["solo:extended-abstract"] }]
    objects: ["own practice"]
    degree: ["strong", "effectively"]
    independence: []
    scope: []
    deficits: []
- id: cardiffmet/generic-2020/l6/argument/70-79.s6
  cell: cardiffmet/generic-2020/l6/argument/70-79
  span: { start: 68498, end: 68667 }
  source: "Critical evaluation of the student’s own work and/or professional practice is highly perceptive and there is a full awareness of the implications for future development."
  versionsFrom: { sameAs: cardiffmet/generic-2020/l4/argument/70-79.s6 }
  echoes: none
  force: describes
  terms:
    verbs: [{ lemma: "evaluate", form: "evaluation", taxonomy: ["bloom-r:analyze/create/evaluate", "solo:extended-abstract"] }, { lemma: "develop", form: "development", taxonomy: ["bloom-r:apply/create"] }]
    objects: []
    degree: ["highly", "perceptive"]
    independence: []
    scope: []
    deficits: []
- id: cardiffmet/generic-2020/l6/argument/60-69.s1
  cell: cardiffmet/generic-2020/l6/argument/60-69
  span: { start: 68734, end: 68793 }
  source: "An ability to engage in critical evaluation and reflection."
  versionsFrom: none
  echoes: none
  force: describes
  terms:
    verbs: [{ lemma: "evaluate", form: "evaluation", taxonomy: ["bloom-r:analyze/create/evaluate", "solo:extended-abstract"] }, { lemma: "reflect", form: "reflection", taxonomy: ["solo:extended-abstract"] }]
    objects: []
    degree: []
    independence: []
    scope: []
    deficits: []
- id: cardiffmet/generic-2020/l6/argument/60-69.s2
  cell: cardiffmet/generic-2020/l6/argument/60-69
  span: { start: 68794, end: 69011 }
  source: "Arguments are clearly considered and substantiated and there is evidence of an ability to make appropriate judgements and to suggest solutions to problems that have limited definition and multiple interacting factors."
  versionsFrom: none
  echoes: none
  force: describes
  terms:
    verbs: [{ lemma: "make", form: "make", taxonomy: ["bloom-r:create"] }, { lemma: "solve", form: "solutions", taxonomy: ["bloom-r:analyze/apply/create", "solo:multistructural"] }]
    objects: ["arguments", "problems"]
    degree: ["clearly", "limited"]
    independence: []
    scope: []
    deficits: []
- id: cardiffmet/generic-2020/l6/argument/60-69.s3
  cell: cardiffmet/generic-2020/l6/argument/60-69
  span: { start: 69012, end: 69167 }
  source: "The student also demonstrates an ability to engage in reflective practice and to take account of personal evaluations when planning for future development."
  versionsFrom: { sameAs: cardiffmet/generic-2020/l3/argument/60-69.s4 }
  echoes: none
  force: describes
  terms:
    verbs: [{ lemma: "demonstrate", form: "demonstrates", taxonomy: ["bloom-r:apply/understand"] }, { lemma: "evaluate", form: "evaluations", taxonomy: ["bloom-r:analyze/create/evaluate", "solo:extended-abstract"] }, { lemma: "develop", form: "development", taxonomy: ["bloom-r:apply/create"] }, { lemma: "plan", form: "planning", taxonomy: ["bloom-r:create", "solo:relational"] }]
    objects: []
    degree: []
    independence: []
    scope: []
    deficits: []
- id: cardiffmet/generic-2020/l6/argument/50-59.s1
  cell: cardiffmet/generic-2020/l6/argument/50-59
  span: { start: 69234, end: 69361 }
  source: "An ability to critically evaluate and reflect although there may be some over-reliance on description and factual presentation."
  versionsFrom: none
  echoes: none
  force: describes
  terms:
    verbs: [{ lemma: "evaluate", form: "evaluate", taxonomy: ["bloom-r:analyze/create/evaluate", "solo:extended-abstract"] }, { lemma: "reflect", form: "reflect", taxonomy: ["solo:extended-abstract"] }, { lemma: "present", form: "presentation", taxonomy: ["none"] }, { lemma: "describe", form: "description", taxonomy: ["bloom-r:evaluate/remember/understand", "solo:multistructural"] }]
    objects: ["presentation"]
    degree: ["some"]
    independence: []
    scope: []
    deficits: ["over-reliance"]
- id: cardiffmet/generic-2020/l6/argument/50-59.s2
  cell: cardiffmet/generic-2020/l6/argument/50-59
  span: { start: 69362, end: 69398 }
  source: "Arguments are usually substantiated."
  versionsFrom: { sameAs: cardiffmet/generic-2020/l3/argument/50-59.s2 }
  echoes: none
  force: describes
  terms:
    verbs: []
    objects: ["arguments"]
    degree: []
    independence: []
    scope: []
    deficits: []
- id: cardiffmet/generic-2020/l6/argument/50-59.s3
  cell: cardiffmet/generic-2020/l6/argument/50-59
  span: { start: 69399, end: 69600 }
  source: "There is some evidence of the student’s ability to evaluate and reflect on the student’s own practice but reflections may lack insight and the implications for future development may be underestimated."
  versionsFrom: { sameAs: cardiffmet/generic-2020/l3/argument/50-59.s3 }
  echoes: none
  force: describes
  terms:
    verbs: [{ lemma: "evaluate", form: "evaluate", taxonomy: ["bloom-r:analyze/create/evaluate", "solo:extended-abstract"] }, { lemma: "develop", form: "development", taxonomy: ["bloom-r:apply/create"] }, { lemma: "reflect", form: "reflect", taxonomy: ["solo:extended-abstract"] }]
    objects: ["own practice"]
    degree: ["some"]
    independence: []
    scope: []
    deficits: ["lack"]
- id: cardiffmet/generic-2020/l6/argument/40-49.s1
  cell: cardiffmet/generic-2020/l6/argument/40-49
  span: { start: 69667, end: 69720 }
  source: "A limited ability to critically evaluate and reflect."
  versionsFrom: none
  echoes: none
  force: describes
  terms:
    verbs: [{ lemma: "evaluate", form: "evaluate", taxonomy: ["bloom-r:analyze/create/evaluate", "solo:extended-abstract"] }, { lemma: "reflect", form: "reflect", taxonomy: ["solo:extended-abstract"] }]
    objects: []
    degree: ["limited"]
    independence: []
    scope: []
    deficits: []
- id: cardiffmet/generic-2020/l6/argument/40-49.s2
  cell: cardiffmet/generic-2020/l6/argument/40-49
  span: { start: 69721, end: 69861 }
  source: "Although some critical reflection is evident, the balance within the work is likely to be in favour of description and factual presentation."
  versionsFrom: { sameAs: cardiffmet/generic-2020/l5/argument/40-49.s2 }
  echoes: none
  force: describes
  terms:
    verbs: [{ lemma: "reflect", form: "reflection", taxonomy: ["solo:extended-abstract"] }, { lemma: "present", form: "presentation", taxonomy: ["none"] }, { lemma: "describe", form: "description", taxonomy: ["bloom-r:evaluate/remember/understand", "solo:multistructural"] }]
    objects: ["presentation"]
    degree: ["some"]
    independence: []
    scope: []
    deficits: []
- id: cardiffmet/generic-2020/l6/argument/40-49.s3
  cell: cardiffmet/generic-2020/l6/argument/40-49
  span: { start: 69862, end: 69927 }
  source: "Arguments are generally substantiated but may be under-developed."
  versionsFrom: { sameAs: cardiffmet/generic-2020/l3/argument/40-49.s3 }
  echoes: none
  force: describes
  terms:
    verbs: []
    objects: ["arguments"]
    degree: ["generally"]
    independence: []
    scope: []
    deficits: []
- id: cardiffmet/generic-2020/l6/argument/40-49.s4
  cell: cardiffmet/generic-2020/l6/argument/40-49
  span: { start: 69928, end: 70030 }
  source: "There is some evidence of the student’s ability to evaluate and reflect on the student’s own practice."
  versionsFrom: none
  echoes: none
  force: describes
  terms:
    verbs: [{ lemma: "evaluate", form: "evaluate", taxonomy: ["bloom-r:analyze/create/evaluate", "solo:extended-abstract"] }, { lemma: "reflect", form: "reflect", taxonomy: ["solo:extended-abstract"] }]
    objects: ["own practice"]
    degree: ["some"]
    independence: []
    scope: []
    deficits: []
- id: cardiffmet/generic-2020/l6/argument/40-49.s5
  cell: cardiffmet/generic-2020/l6/argument/40-49
  span: { start: 70031, end: 70143 }
  source: "Reflections may be limited and superficial, with little consideration of their relevance for future development."
  versionsFrom: none
  echoes: none
  force: describes
  terms:
    verbs: [{ lemma: "develop", form: "development", taxonomy: ["bloom-r:apply/create"] }, { lemma: "consider", form: "consideration", taxonomy: ["none"] }]
    objects: []
    degree: ["limited", "little"]
    independence: []
    scope: []
    deficits: ["superficial"]
- id: cardiffmet/generic-2020/l6/argument/30-39.s1
  cell: cardiffmet/generic-2020/l6/argument/30-39
  span: { start: 70217, end: 70272 }
  source: "Limited evidence of critical evaluation and reflection."
  versionsFrom: none
  echoes: none
  force: describes
  terms:
    verbs: [{ lemma: "evaluate", form: "evaluation", taxonomy: ["bloom-r:analyze/create/evaluate", "solo:extended-abstract"] }, { lemma: "reflect", form: "reflection", taxonomy: ["solo:extended-abstract"] }]
    objects: []
    degree: ["limited"]
    independence: []
    scope: []
    deficits: []
- id: cardiffmet/generic-2020/l6/argument/30-39.s2
  cell: cardiffmet/generic-2020/l6/argument/30-39
  span: { start: 70273, end: 70358 }
  source: "The work is largely descriptive and arguments if attempted, are rarely substantiated."
  versionsFrom: { sameAs: cardiffmet/generic-2020/l3/argument/30-39.s2 }
  echoes: none
  force: describes
  terms:
    verbs: [{ lemma: "describe", form: "descriptive", taxonomy: ["bloom-r:evaluate/remember/understand", "solo:multistructural"] }]
    objects: ["arguments"]
    degree: []
    independence: []
    scope: []
    deficits: []
- id: cardiffmet/generic-2020/l6/argument/30-39.s3
  cell: cardiffmet/generic-2020/l6/argument/30-39
  span: { start: 70359, end: 70443 }
  source: "Self-evaluation and reflections on the student’s own practice are extremely limited."
  versionsFrom: { sameAs: cardiffmet/generic-2020/l3/argument/30-39.s3 }
  echoes: none
  force: describes
  terms:
    verbs: []
    objects: ["own practice"]
    degree: ["limited"]
    independence: []
    scope: []
    deficits: []
- id: cardiffmet/generic-2020/l6/argument/1-29.s1
  cell: cardiffmet/generic-2020/l6/argument/1-29
  span: { start: 70515, end: 70553 }
  source: "Little ability to describe and report."
  versionsFrom: none
  echoes: none
  force: describes
  terms:
    verbs: [{ lemma: "describe", form: "describe", taxonomy: ["bloom-r:evaluate/remember/understand", "solo:multistructural"] }, { lemma: "report", form: "report", taxonomy: ["bloom-r:apply/understand", "solo:multistructural"] }]
    objects: []
    degree: ["little"]
    independence: []
    scope: []
    deficits: []
- id: cardiffmet/generic-2020/l6/argument/1-29.s2
  cell: cardiffmet/generic-2020/l6/argument/1-29
  span: { start: 70554, end: 70659 }
  source: "Very little evidence is available to indicate an ability to engage in critical evaluation and reflection."
  versionsFrom: none
  echoes: none
  force: describes
  terms:
    verbs: [{ lemma: "evaluate", form: "evaluation", taxonomy: ["bloom-r:analyze/create/evaluate", "solo:extended-abstract"] }, { lemma: "reflect", form: "reflection", taxonomy: ["solo:extended-abstract"] }]
    objects: []
    degree: ["very little"]
    independence: []
    scope: []
    deficits: []
- id: cardiffmet/generic-2020/l6/argument/1-29.s3
  cell: cardiffmet/generic-2020/l6/argument/1-29
  span: { start: 70660, end: 70747 }
  source: "Self-evaluation and reflections on the student’s own practice are negligible or absent."
  versionsFrom: { sameAs: cardiffmet/generic-2020/l3/argument/1-29.s2 }
  echoes: none
  force: describes
  terms:
    verbs: []
    objects: ["own practice"]
    degree: []
    independence: []
    scope: []
    deficits: ["negligible", "absent"]
- id: cardiffmet/generic-2020/l7/overall/80-100.s1
  cell: cardiffmet/generic-2020/l7/overall/80-100
  span: { start: 70830, end: 71062 }
  source: "A full and detailed understanding of the set task and an ability to have met the learning outcomes and address the assessment criteria at an excellent level (80-89%) or outstanding and exceptional level (90-100%) and beyond level 7."
  versionsFrom: { sameAs: cardiffmet/generic-2020/l3/overall/80-100.s1 }
  echoes: none
  force: describes
  terms:
    verbs: [{ lemma: "address", form: "address", taxonomy: ["none"] }, { lemma: "meet", form: "met", taxonomy: ["none"] }]
    objects: ["understanding", "set task", "learning outcomes", "assessment criteria"]
    degree: ["detailed", "excellent", "outstanding", "exceptional"]
    independence: []
    scope: ["beyond level"]
    deficits: []
- id: cardiffmet/generic-2020/l7/overall/80-100.s2
  cell: cardiffmet/generic-2020/l7/overall/80-100
  span: { start: 71063, end: 71164 }
  source: "Work is of a standard deemed worthy of publication/manufacture/ public exhibition/public performance."
  versionsFrom: none
  echoes: none
  force: describes
  terms:
    verbs: []
    objects: []
    degree: []
    independence: []
    scope: []
    deficits: []
- id: cardiffmet/generic-2020/l7/overall/70-79.s1
  cell: cardiffmet/generic-2020/l7/overall/70-79
  span: { start: 71211, end: 71367 }
  source: "A full and detailed understanding of the set task and an ability to have met the learning outcomes and address the assessment criteria at a very good level."
  versionsFrom: { sameAs: cardiffmet/generic-2020/l3/overall/70-79.s1 }
  echoes: none
  force: describes
  terms:
    verbs: [{ lemma: "address", form: "address", taxonomy: ["none"] }, { lemma: "meet", form: "met", taxonomy: ["none"] }]
    objects: ["understanding", "set task", "learning outcomes", "assessment criteria"]
    degree: ["detailed", "very good"]
    independence: []
    scope: []
    deficits: []
- id: cardiffmet/generic-2020/l7/overall/60-69.s1
  cell: cardiffmet/generic-2020/l7/overall/60-69
  span: { start: 71408, end: 71546 }
  source: "A full understanding of the set task and an ability to have met the learning outcomes and address the assessment criteria at a good level."
  versionsFrom: { sameAs: cardiffmet/generic-2020/l3/overall/60-69.s1 }
  echoes: none
  force: describes
  terms:
    verbs: [{ lemma: "address", form: "address", taxonomy: ["none"] }, { lemma: "meet", form: "met", taxonomy: ["none"] }]
    objects: ["understanding", "set task", "learning outcomes", "assessment criteria"]
    degree: ["good"]
    independence: []
    scope: []
    deficits: []
- id: cardiffmet/generic-2020/l7/overall/50-59.s1
  cell: cardiffmet/generic-2020/l7/overall/50-59
  span: { start: 71586, end: 71752 }
  source: "A basic but secure understanding of the set task and an ability to have met the associated learning outcomes and address the assessment criteria at a threshold level."
  versionsFrom: none
  echoes: none
  force: describes
  terms:
    verbs: [{ lemma: "address", form: "address", taxonomy: ["none"] }, { lemma: "meet", form: "met", taxonomy: ["none"] }]
    objects: ["understanding", "set task", "learning outcomes", "assessment criteria"]
    degree: ["basic", "secure"]
    independence: []
    scope: ["basic"]
    deficits: []
- id: cardiffmet/generic-2020/l7/overall/40-49.s1
  cell: cardiffmet/generic-2020/l7/overall/40-49
  span: { start: 71799, end: 71971 }
  source: "A partial understanding of the set task and an ability to have met the associated learning outcomes and address the assessment criteria at a limited and insufficient level."
  versionsFrom: none
  echoes: none
  force: describes
  terms:
    verbs: [{ lemma: "address", form: "address", taxonomy: ["none"] }, { lemma: "meet", form: "met", taxonomy: ["none"] }]
    objects: ["understanding", "set task", "learning outcomes", "assessment criteria"]
    degree: ["limited"]
    independence: []
    scope: []
    deficits: ["insufficient"]
- id: cardiffmet/generic-2020/l7/overall/40-49.s2
  cell: cardiffmet/generic-2020/l7/overall/40-49
  span: { start: 71972, end: 71995 }
  source: "Unsatisfactory overall."
  versionsFrom: { sameAs: cardiffmet/generic-2020/l3/overall/30-39.s1 }
  echoes: none
  force: describes
  terms:
    verbs: []
    objects: []
    degree: []
    independence: []
    scope: []
    deficits: []
- id: cardiffmet/generic-2020/l7/overall/40-49.s3
  cell: cardiffmet/generic-2020/l7/overall/40-49
  span: { start: 71996, end: 72103 }
  source: "However, attainment is uneven with some learning outcomes not met and some assessment criteria unaddressed."
  versionsFrom: { sameAs: cardiffmet/generic-2020/l3/overall/30-39.s3 }
  echoes: none
  force: describes
  terms:
    verbs: [{ lemma: "meet", form: "met", taxonomy: ["none"] }]
    objects: ["learning outcomes", "assessment criteria"]
    degree: ["some", "some"]
    independence: []
    scope: []
    deficits: ["not", "unaddressed"]
- id: cardiffmet/generic-2020/l7/overall/20-39.s1
  cell: cardiffmet/generic-2020/l7/overall/20-39
  span: { start: 72148, end: 72171 }
  source: "Unsatisfactory overall."
  versionsFrom: { sameAs: cardiffmet/generic-2020/l3/overall/30-39.s1 }
  echoes: none
  force: describes
  terms:
    verbs: []
    objects: []
    degree: []
    independence: []
    scope: []
    deficits: []
- id: cardiffmet/generic-2020/l7/overall/20-39.s2
  cell: cardiffmet/generic-2020/l7/overall/20-39
  span: { start: 72172, end: 72297 }
  source: "A minimal understanding of the set task and an ability to have met some of the associated learning outcomes at a basic level."
  versionsFrom: none
  echoes: none
  force: describes
  terms:
    verbs: [{ lemma: "meet", form: "met", taxonomy: ["none"] }]
    objects: ["understanding", "set task", "learning outcomes"]
    degree: ["minimal", "some", "basic"]
    independence: []
    scope: ["basic"]
    deficits: []
- id: cardiffmet/generic-2020/l7/overall/20-39.s3
  cell: cardiffmet/generic-2020/l7/overall/20-39
  span: { start: 72298, end: 72370 }
  source: "However, attainment is uneven with many assessment criteria unaddressed."
  versionsFrom: none
  echoes: none
  force: describes
  terms:
    verbs: []
    objects: ["assessment criteria"]
    degree: []
    independence: []
    scope: []
    deficits: ["unaddressed"]
- id: cardiffmet/generic-2020/l7/overall/1-19.s1
  cell: cardiffmet/generic-2020/l7/overall/1-19
  span: { start: 72401, end: 72441 }
  source: "Very poor, incomplete and/or irrelevant."
  versionsFrom: none
  echoes: none
  force: describes
  terms:
    verbs: []
    objects: []
    degree: ["poor"]
    independence: []
    scope: []
    deficits: ["irrelevant"]
- id: cardiffmet/generic-2020/l7/overall/1-19.s2
  cell: cardiffmet/generic-2020/l7/overall/1-19
  span: { start: 72442, end: 72523 }
  source: "Demonstrates a serious lack of comprehension and/or engagement with the set task."
  versionsFrom: none
  echoes: none
  force: describes
  terms:
    verbs: [{ lemma: "demonstrate", form: "demonstrates", taxonomy: ["bloom-r:apply/understand"] }]
    objects: ["set task"]
    degree: []
    independence: []
    scope: []
    deficits: ["lack"]
- id: cardiffmet/generic-2020/l7/overall/1-19.s3
  cell: cardiffmet/generic-2020/l7/overall/1-19
  span: { start: 72524, end: 72560 }
  source: "May have misunderstood the set task."
  versionsFrom: none
  echoes: none
  force: describes
  terms:
    verbs: []
    objects: ["set task"]
    degree: []
    independence: []
    scope: []
    deficits: []
- id: cardiffmet/generic-2020/l7/overall/1-19.s4
  cell: cardiffmet/generic-2020/l7/overall/1-19
  span: { start: 72561, end: 72660 }
  source: "No learning outcomes are met in full, although there may be minimal attainment in one or two areas."
  versionsFrom: none
  echoes: none
  force: describes
  terms:
    verbs: [{ lemma: "meet", form: "met", taxonomy: ["none"] }]
    objects: ["learning outcomes"]
    degree: ["minimal"]
    independence: []
    scope: []
    deficits: ["no"]
- id: cardiffmet/generic-2020/l7/knowledge/80-100.s1
  cell: cardiffmet/generic-2020/l7/knowledge/80-100
  span: { start: 72719, end: 72838 }
  source: "Further to the 70%-79% band, academic work in the 80%-100% bands is beyond the expectation of that expected at level 7."
  versionsFrom: none
  echoes: none
  force: describes
  terms:
    verbs: []
    objects: []
    degree: []
    independence: []
    scope: []
    deficits: []
- id: cardiffmet/generic-2020/l7/knowledge/80-100.s2
  cell: cardiffmet/generic-2020/l7/knowledge/80-100
  span: { start: 72839, end: 72918 }
  source: "Demonstrates exceptional mastery of a complex and specialist area of knowledge."
  versionsFrom: none
  echoes: none
  force: describes
  terms:
    verbs: [{ lemma: "demonstrate", form: "demonstrates", taxonomy: ["bloom-r:apply/understand"] }]
    objects: ["knowledge"]
    degree: ["exceptional", "mastery"]
    independence: []
    scope: ["complex", "specialist"]
    deficits: []
- id: cardiffmet/generic-2020/l7/knowledge/70-79.s1
  cell: cardiffmet/generic-2020/l7/knowledge/70-79
  span: { start: 72975, end: 73043 }
  source: "Demonstrates mastery of a complex and specialised area of knowledge."
  versionsFrom: none
  echoes: none
  force: describes
  terms:
    verbs: [{ lemma: "demonstrate", form: "demonstrates", taxonomy: ["bloom-r:apply/understand"] }]
    objects: ["knowledge"]
    degree: ["mastery"]
    independence: []
    scope: ["complex", "specialised"]
    deficits: []
- id: cardiffmet/generic-2020/l7/knowledge/70-79.s2
  cell: cardiffmet/generic-2020/l7/knowledge/70-79
  span: { start: 73044, end: 73129 }
  source: "There is strong evidence of an ability to extend, transform and apply such knowledge."
  versionsFrom: { sameAs: cardiffmet/generic-2020/l5/knowledge/70-79.s2 }
  echoes: none
  force: describes
  terms:
    verbs: [{ lemma: "apply", form: "apply", taxonomy: ["bloom-r:apply", "solo:relational"] }, { lemma: "extend", form: "extend", taxonomy: ["bloom-r:understand"] }, { lemma: "transform", form: "transform", taxonomy: ["none"] }]
    objects: ["knowledge"]
    degree: ["strong"]
    independence: []
    scope: []
    deficits: []
- id: cardiffmet/generic-2020/l7/knowledge/70-79.s3
  cell: cardiffmet/generic-2020/l7/knowledge/70-79
  span: { start: 73130, end: 73305 }
  source: "The student also demonstrates an ability to engage in sophisticated discussion of complex concepts and to recognise the limitations and/or ambiguity of disciplinary knowledge."
  versionsFrom: { like: cardiffmet/generic-2020/l5/knowledge/70-79.s3, similarity: 0.96 }
  echoes: none
  force: describes
  terms:
    verbs: [{ lemma: "demonstrate", form: "demonstrates", taxonomy: ["bloom-r:apply/understand"] }, { lemma: "recognise", form: "recognise", taxonomy: ["solo:unistructural"] }]
    objects: ["concepts", "limitations", "knowledge"]
    degree: ["sophisticated"]
    independence: []
    scope: ["complex"]
    deficits: []
- id: cardiffmet/generic-2020/l7/knowledge/70-79.s4
  cell: cardiffmet/generic-2020/l7/knowledge/70-79
  span: { start: 73306, end: 73338 }
  source: "Independent thinking and action."
  versionsFrom: none
  echoes: none
  force: describes
  terms:
    verbs: []
    objects: []
    degree: []
    independence: ["independent thinking"]
    scope: []
    deficits: []
- id: cardiffmet/generic-2020/l7/knowledge/70-79.s5
  cell: cardiffmet/generic-2020/l7/knowledge/70-79
  span: { start: 73339, end: 73397 }
  source: "Original insights are also features of work at this level."
  versionsFrom: none
  echoes: none
  force: describes
  terms:
    verbs: []
    objects: []
    degree: []
    independence: []
    scope: ["original", "at this level"]
    deficits: []
- id: cardiffmet/generic-2020/l7/knowledge/60-69.s1
  cell: cardiffmet/generic-2020/l7/knowledge/60-69
  span: { start: 73448, end: 73516 }
  source: "Demonstrates mastery of a complex and specialised area of knowledge."
  versionsFrom: { sameAs: cardiffmet/generic-2020/l7/knowledge/70-79.s1 }
  echoes: none
  force: describes
  terms:
    verbs: [{ lemma: "demonstrate", form: "demonstrates", taxonomy: ["bloom-r:apply/understand"] }]
    objects: ["knowledge"]
    degree: ["mastery"]
    independence: []
    scope: ["complex", "specialised"]
    deficits: []
- id: cardiffmet/generic-2020/l7/knowledge/60-69.s2
  cell: cardiffmet/generic-2020/l7/knowledge/60-69
  span: { start: 73517, end: 73632 }
  source: "There is clear evidence of an ability to apply such knowledge within familiar contexts, to extend and transform it."
  versionsFrom: none
  echoes: none
  force: describes
  terms:
    verbs: [{ lemma: "apply", form: "apply", taxonomy: ["bloom-r:apply", "solo:relational"] }, { lemma: "extend", form: "extend", taxonomy: ["bloom-r:understand"] }, { lemma: "transform", form: "transform", taxonomy: ["none"] }]
    objects: ["knowledge"]
    degree: ["clear"]
    independence: []
    scope: []
    deficits: []
- id: cardiffmet/generic-2020/l7/knowledge/60-69.s3
  cell: cardiffmet/generic-2020/l7/knowledge/60-69
  span: { start: 73633, end: 73760 }
  source: "The discussion of complex concepts is often tackled successfully and there is some evidence of independent thinking and action."
  versionsFrom: none
  echoes: none
  force: describes
  terms:
    verbs: []
    objects: ["concepts"]
    degree: ["successfully", "some"]
    independence: ["independent thinking"]
    scope: ["complex"]
    deficits: []
- id: cardiffmet/generic-2020/l7/knowledge/50-59.s1
  cell: cardiffmet/generic-2020/l7/knowledge/50-59
  span: { start: 73810, end: 73936 }
  source: "Demonstrates mastery of a complex and specialised area of knowledge, but is frequently descriptive and based on given sources."
  versionsFrom: none
  echoes: none
  force: describes
  terms:
    verbs: [{ lemma: "demonstrate", form: "demonstrates", taxonomy: ["bloom-r:apply/understand"] }, { lemma: "describe", form: "descriptive", taxonomy: ["bloom-r:evaluate/remember/understand", "solo:multistructural"] }]
    objects: ["knowledge", "sources"]
    degree: ["mastery"]
    independence: []
    scope: ["complex", "specialised"]
    deficits: []
- id: cardiffmet/generic-2020/l7/knowledge/50-59.s2
  cell: cardiffmet/generic-2020/l7/knowledge/50-59
  span: { start: 73937, end: 73998 }
  source: "There is limited evidence of independent thinking and action."
  versionsFrom: none
  echoes: none
  force: describes
  terms:
    verbs: []
    objects: []
    degree: ["limited"]
    independence: ["independent thinking"]
    scope: []
    deficits: []
- id: cardiffmet/generic-2020/l7/knowledge/40-49.s1
  cell: cardiffmet/generic-2020/l7/knowledge/40-49
  span: { start: 74055, end: 74134 }
  source: "Limited knowledge and understanding of the field of study relevant to the task."
  versionsFrom: { sameAs: cardiffmet/generic-2020/l6/knowledge/30-39.s1 }
  echoes: none
  force: describes
  terms:
    verbs: []
    objects: ["knowledge and understanding", "field of study"]
    degree: ["limited"]
    independence: []
    scope: []
    deficits: []
- id: cardiffmet/generic-2020/l7/knowledge/40-49.s2
  cell: cardiffmet/generic-2020/l7/knowledge/40-49
  span: { start: 74135, end: 74278 }
  source: "Factual inaccuracies, errors and misconceptions are evident in important areas and elements of the assessed work may be irrelevant to the task."
  versionsFrom: { sameAs: cardiffmet/generic-2020/l3/knowledge/30-39.s2 }
  echoes: none
  force: describes
  terms:
    verbs: []
    objects: []
    degree: []
    independence: []
    scope: []
    deficits: ["inaccuracies", "errors", "misconceptions", "irrelevant"]
- id: cardiffmet/generic-2020/l7/knowledge/20-39.s1
  cell: cardiffmet/generic-2020/l7/knowledge/20-39
  span: { start: 74333, end: 74411 }
  source: "Little knowledge and understanding of the field of study relevant to the task."
  versionsFrom: { sameAs: cardiffmet/generic-2020/l6/knowledge/1-29.s1 }
  echoes: none
  force: describes
  terms:
    verbs: []
    objects: ["knowledge and understanding", "field of study"]
    degree: ["little"]
    independence: []
    scope: []
    deficits: []
- id: cardiffmet/generic-2020/l7/knowledge/20-39.s2
  cell: cardiffmet/generic-2020/l7/knowledge/20-39
  span: { start: 74412, end: 74570 }
  source: "Factual inaccuracies, errors and misconceptions are evident in many important areas and these outweigh the degree of knowledge and understanding demonstrated."
  versionsFrom: { sameAs: cardiffmet/generic-2020/l3/knowledge/1-29.s2 }
  echoes: none
  force: describes
  terms:
    verbs: [{ lemma: "demonstrate", form: "demonstrated", taxonomy: ["bloom-r:apply/understand"] }]
    objects: ["knowledge and understanding"]
    degree: []
    independence: []
    scope: []
    deficits: ["inaccuracies", "errors", "misconceptions"]
- id: cardiffmet/generic-2020/l7/knowledge/20-39.s3
  cell: cardiffmet/generic-2020/l7/knowledge/20-39
  span: { start: 74571, end: 74643 }
  source: "Substantial elements of the assessed work may be irrelevant to the task."
  versionsFrom: { sameAs: cardiffmet/generic-2020/l3/knowledge/1-29.s3 }
  echoes: none
  force: describes
  terms:
    verbs: []
    objects: []
    degree: []
    independence: []
    scope: []
    deficits: ["irrelevant"]
- id: cardiffmet/generic-2020/l7/knowledge/1-19.s1
  cell: cardiffmet/generic-2020/l7/knowledge/1-19
  span: { start: 74684, end: 74986 }
  source: "Work may be: short irrelevant contain serious/numerous errors and misunderstandings no evidence of analysis, synthesis, critical evaluation and reflection no reference/minimal reference to external sources very poor presentation and inappropriate format very poor communication of information and ideas"
  versionsFrom: none
  echoes: none
  force: describes
  terms:
    verbs: [{ lemma: "evaluate", form: "evaluation", taxonomy: ["bloom-r:analyze/create/evaluate", "solo:extended-abstract"] }, { lemma: "synthesise", form: "synthesis", taxonomy: ["bloom-r:create/evaluate"] }, { lemma: "reflect", form: "reflection", taxonomy: ["solo:extended-abstract"] }, { lemma: "present", form: "presentation", taxonomy: ["none"] }]
    objects: ["sources", "presentation", "information", "ideas"]
    degree: ["minimal", "poor", "poor"]
    independence: []
    scope: []
    deficits: ["irrelevant", "errors", "no", "no"]
- id: cardiffmet/generic-2020/l7/presentation/80-100.s1
  cell: cardiffmet/generic-2020/l7/presentation/80-100
  span: { start: 75050, end: 75182 }
  source: "Further to the 70% – 79% band, academic work in the 80% - 100% provides consistently convincing and succinct arguments in all areas."
  versionsFrom: none
  echoes: none
  force: describes
  terms:
    verbs: [{ lemma: "provide", form: "provides", taxonomy: ["none"] }]
    objects: ["arguments"]
    degree: ["consistently"]
    independence: []
    scope: []
    deficits: []
- id: cardiffmet/generic-2020/l7/presentation/80-100.s2
  cell: cardiffmet/generic-2020/l7/presentation/80-100
  span: { start: 75183, end: 75294 }
  source: "The standard of presentation shows an enhanced ability to communicate using an eloquent and professional style."
  versionsFrom: none
  echoes: none
  force: describes
  terms:
    verbs: [{ lemma: "use", form: "using", taxonomy: ["bloom-r:apply"] }, { lemma: "communicate", form: "communicate", taxonomy: ["none"] }, { lemma: "present", form: "presentation", taxonomy: ["none"] }]
    objects: ["presentation"]
    degree: []
    independence: []
    scope: []
    deficits: []
- id: cardiffmet/generic-2020/l7/presentation/70-79.s1
  cell: cardiffmet/generic-2020/l7/presentation/70-79
  span: { start: 75356, end: 75503 }
  source: "An ability to communicate information, complex ideas, results of research and concepts in a coherent and succinct manner, in a range of situations."
  versionsFrom: none
  echoes: none
  force: describes
  terms:
    verbs: [{ lemma: "communicate", form: "communicate", taxonomy: ["none"] }]
    objects: ["information", "ideas", "research", "concepts"]
    degree: []
    independence: []
    scope: ["complex", "a range of"]
    deficits: []
- id: cardiffmet/generic-2020/l7/presentation/70-79.s2
  cell: cardiffmet/generic-2020/l7/presentation/70-79
  span: { start: 75504, end: 75568 }
  source: "The standard of presentation is high and the format appropriate."
  versionsFrom: { sameAs: cardiffmet/generic-2020/l3/presentation/70-79.s2 }
  echoes: none
  force: describes
  terms:
    verbs: [{ lemma: "present", form: "presentation", taxonomy: ["none"] }]
    objects: ["presentation"]
    degree: ["high"]
    independence: []
    scope: []
    deficits: []
- id: cardiffmet/generic-2020/l7/presentation/70-79.s3
  cell: cardiffmet/generic-2020/l7/presentation/70-79
  span: { start: 75569, end: 75655 }
  source: "Key points are logically organised and in written work, the style is lucid and mature."
  versionsFrom: { sameAs: cardiffmet/generic-2020/l5/presentation/70-79.s3 }
  echoes: none
  force: describes
  terms:
    verbs: []
    objects: []
    degree: []
    independence: []
    scope: ["key"]
    deficits: []
- id: cardiffmet/generic-2020/l7/presentation/70-79.s4
  cell: cardiffmet/generic-2020/l7/presentation/70-79
  span: { start: 75656, end: 75707 }
  source: "Arguments are well-defined and clearly articulated."
  versionsFrom: { sameAs: cardiffmet/generic-2020/l3/presentation/70-79.s4 }
  echoes: none
  force: describes
  terms:
    verbs: []
    objects: ["arguments"]
    degree: ["clearly"]
    independence: []
    scope: ["well-defined"]
    deficits: []
- id: cardiffmet/generic-2020/l7/presentation/60-69.s1
  cell: cardiffmet/generic-2020/l7/presentation/60-69
  span: { start: 75763, end: 75890 }
  source: "An ability to communicate information, results of research, ideas and concepts clearly and succinctly in a range of situations."
  versionsFrom: none
  echoes: none
  force: describes
  terms:
    verbs: [{ lemma: "communicate", form: "communicate", taxonomy: ["none"] }]
    objects: ["information", "research", "ideas", "concepts"]
    degree: ["clearly"]
    independence: []
    scope: ["a range of"]
    deficits: []
- id: cardiffmet/generic-2020/l7/presentation/60-69.s2
  cell: cardiffmet/generic-2020/l7/presentation/60-69
  span: { start: 75891, end: 75941 }
  source: "Work is well presented and the format appropriate."
  versionsFrom: { sameAs: cardiffmet/generic-2020/l3/presentation/60-69.s2 }
  echoes: none
  force: describes
  terms:
    verbs: []
    objects: []
    degree: ["well"]
    independence: []
    scope: []
    deficits: []
- id: cardiffmet/generic-2020/l7/presentation/60-69.s3
  cell: cardiffmet/generic-2020/l7/presentation/60-69
  span: { start: 75942, end: 76025 }
  source: "Key points are appropriately organised, fluently conveyed and are well articulated."
  versionsFrom: none
  echoes: none
  force: describes
  terms:
    verbs: []
    objects: []
    degree: ["well"]
    independence: []
    scope: ["key"]
    deficits: []
- id: cardiffmet/generic-2020/l7/presentation/50-59.s1
  cell: cardiffmet/generic-2020/l7/presentation/50-59
  span: { start: 76080, end: 76218 }
  source: "Satisfactory ability to communicate information, results of research, ideas, concepts and arguments satisfactorily in familiar situations."
  versionsFrom: none
  echoes: none
  force: describes
  terms:
    verbs: [{ lemma: "communicate", form: "communicate", taxonomy: ["none"] }]
    objects: ["information", "research", "ideas", "concepts", "arguments"]
    degree: ["satisfactory"]
    independence: []
    scope: []
    deficits: []
- id: cardiffmet/generic-2020/l7/presentation/50-59.s2
  cell: cardiffmet/generic-2020/l7/presentation/50-59
  span: { start: 76219, end: 76362 }
  source: "Some aspects of the task lack academic rigour and rely on describing and reporting factual information rather than communicating complex ideas."
  versionsFrom: none
  echoes: none
  force: describes
  terms:
    verbs: [{ lemma: "communicate", form: "communicating", taxonomy: ["none"] }, { lemma: "describe", form: "describing", taxonomy: ["bloom-r:evaluate/remember/understand", "solo:multistructural"] }, { lemma: "report", form: "reporting", taxonomy: ["bloom-r:apply/understand", "solo:multistructural"] }]
    objects: ["information", "ideas"]
    degree: ["some"]
    independence: []
    scope: ["complex"]
    deficits: ["lack"]
- id: cardiffmet/generic-2020/l7/presentation/50-59.s3
  cell: cardiffmet/generic-2020/l7/presentation/50-59
  span: { start: 76363, end: 76442 }
  source: "Generally, the work is appropriately structured but may not always be coherent."
  versionsFrom: none
  echoes: none
  force: describes
  terms:
    verbs: []
    objects: []
    degree: ["generally"]
    independence: []
    scope: []
    deficits: ["not"]
- id: cardiffmet/generic-2020/l7/presentation/40-49.s1
  cell: cardiffmet/generic-2020/l7/presentation/40-49
  span: { start: 76504, end: 76578 }
  source: "An ability to communicate some simple concepts and/or factual information."
  versionsFrom: none
  echoes: none
  force: describes
  terms:
    verbs: [{ lemma: "communicate", form: "communicate", taxonomy: ["none"] }]
    objects: ["concepts", "information"]
    degree: ["some"]
    independence: []
    scope: []
    deficits: []
- id: cardiffmet/generic-2020/l7/presentation/40-49.s2
  cell: cardiffmet/generic-2020/l7/presentation/40-49
  span: { start: 76579, end: 76671 }
  source: "Ideas may not be communicated clearly and present comprehension difficulties for the reader."
  versionsFrom: { sameAs: cardiffmet/generic-2020/l3/presentation/30-39.s2 }
  echoes: none
  force: describes
  terms:
    verbs: [{ lemma: "present", form: "present", taxonomy: ["none"] }]
    objects: ["ideas"]
    degree: ["clearly"]
    independence: []
    scope: []
    deficits: ["not"]
- id: cardiffmet/generic-2020/l7/presentation/40-49.s3
  cell: cardiffmet/generic-2020/l7/presentation/40-49
  span: { start: 76672, end: 76778 }
  source: "If attempted, the presentation of arguments and more complex ideas may be confused and clumsily expressed."
  versionsFrom: { sameAs: cardiffmet/generic-2020/l3/presentation/30-39.s3 }
  echoes: none
  force: describes
  terms:
    verbs: [{ lemma: "present", form: "presentation", taxonomy: ["none"] }]
    objects: ["presentation", "arguments", "ideas"]
    degree: []
    independence: []
    scope: ["complex"]
    deficits: ["confused"]
- id: cardiffmet/generic-2020/l7/presentation/20-39.s1
  cell: cardiffmet/generic-2020/l7/presentation/20-39
  span: { start: 76838, end: 76912 }
  source: "Limited ability to communicate simple concepts and/or factual information."
  versionsFrom: none
  echoes: none
  force: describes
  terms:
    verbs: [{ lemma: "communicate", form: "communicate", taxonomy: ["none"] }]
    objects: ["concepts", "information"]
    degree: ["limited"]
    independence: []
    scope: []
    deficits: []
- id: cardiffmet/generic-2020/l7/presentation/20-39.s2
  cell: cardiffmet/generic-2020/l7/presentation/20-39
  span: { start: 76913, end: 77065 }
  source: "Frequent faults in the presentation of work and significant difficulties in its structure and organisation detract from the clarity and meaning overall."
  versionsFrom: { sameAs: cardiffmet/generic-2020/l3/presentation/1-29.s2 }
  echoes: none
  force: describes
  terms:
    verbs: [{ lemma: "present", form: "presentation", taxonomy: ["none"] }]
    objects: ["presentation", "structure"]
    degree: []
    independence: []
    scope: []
    deficits: []
- id: cardiffmet/generic-2020/l7/presentation/20-39.s3
  cell: cardiffmet/generic-2020/l7/presentation/20-39
  span: { start: 77066, end: 77118 }
  source: "The writing style is often clumsy and inappropriate."
  versionsFrom: { sameAs: cardiffmet/generic-2020/l3/presentation/1-29.s3 }
  echoes: none
  force: describes
  terms:
    verbs: []
    objects: []
    degree: []
    independence: []
    scope: []
    deficits: ["clumsy"]
- id: cardiffmet/generic-2020/l7/analysis/80-100.s1
  cell: cardiffmet/generic-2020/l7/analysis/80-100
  span: { start: 77297, end: 77507 }
  source: "The students demonstrates the ability to design and undertake their own extensive and independent inquiry applying advanced concepts, methods or techniques consistently to solve problems in unfamiliar contexts."
  versionsFrom: none
  echoes: none
  force: describes
  terms:
    verbs: [{ lemma: "demonstrate", form: "demonstrates", taxonomy: ["bloom-r:apply/understand"] }, { lemma: "apply", form: "applying", taxonomy: ["bloom-r:apply", "solo:relational"] }, { lemma: "undertake", form: "undertake", taxonomy: ["none"] }, { lemma: "solve", form: "solve", taxonomy: ["bloom-r:analyze/apply/create", "solo:multistructural"] }]
    objects: ["concepts", "techniques", "problems"]
    degree: ["consistently"]
    independence: ["independent"]
    scope: ["advanced", "unfamiliar"]
    deficits: []
- id: cardiffmet/generic-2020/l7/analysis/70-79.s1
  cell: cardiffmet/generic-2020/l7/analysis/70-79
  span: { start: 77560, end: 77879 }
  source: "An ability to conduct research or advanced technical or professional activity, undertake detailed analysis and critical enquiry relevant to the task/discipline and expertise in highly specialised and advanced technical, professional and/or research skills, by making excellent use of a number of appropriate techniques."
  versionsFrom: none
  echoes: none
  force: describes
  terms:
    verbs: [{ lemma: "use", form: "use", taxonomy: ["bloom-r:apply"] }, { lemma: "make", form: "making", taxonomy: ["bloom-r:create"] }, { lemma: "undertake", form: "undertake", taxonomy: ["none"] }, { lemma: "conduct", form: "conduct", taxonomy: ["solo:multistructural"] }]
    objects: ["research", "discipline", "research", "techniques"]
    degree: ["detailed", "highly", "excellent"]
    independence: []
    scope: ["advanced", "specialised", "advanced"]
    deficits: []
- id: cardiffmet/generic-2020/l7/analysis/70-79.s2
  cell: cardiffmet/generic-2020/l7/analysis/70-79
  span: { start: 77880, end: 78090 }
  source: "The student is highly successful in presenting, synthesising and commenting on research process and outcomes and is able to comment perceptively and with insight on the relationship between theory and practice."
  versionsFrom: none
  echoes: none
  force: describes
  terms:
    verbs: [{ lemma: "comment", form: "comment", taxonomy: ["none"] }, { lemma: "synthesise", form: "synthesising", taxonomy: ["bloom-r:create/evaluate"] }, { lemma: "present", form: "presenting", taxonomy: ["none"] }]
    objects: ["research", "theory and practice"]
    degree: ["highly", "successful", "perceptively"]
    independence: []
    scope: []
    deficits: []
- id: cardiffmet/generic-2020/l7/analysis/60-69.s1
  cell: cardiffmet/generic-2020/l7/analysis/60-69
  span: { start: 78137, end: 78530 }
  source: "An ability to conduct research or advanced technical or professional activity, undertake some detailed analysis and critical enquiry relevant to the task/discipline and expertise in highly specialised and advanced technical, professional and/or research skills, by making use of appropriate techniques and has considerable success in presenting and commenting on research process and outcomes."
  versionsFrom: none
  echoes: none
  force: describes
  terms:
    verbs: [{ lemma: "comment", form: "commenting", taxonomy: ["none"] }, { lemma: "use", form: "use", taxonomy: ["bloom-r:apply"] }, { lemma: "make", form: "making", taxonomy: ["bloom-r:create"] }, { lemma: "undertake", form: "undertake", taxonomy: ["none"] }, { lemma: "conduct", form: "conduct", taxonomy: ["solo:multistructural"] }, { lemma: "present", form: "presenting", taxonomy: ["none"] }]
    objects: ["research", "discipline", "research", "techniques", "research"]
    degree: ["some", "detailed", "highly"]
    independence: []
    scope: ["advanced", "specialised", "advanced"]
    deficits: []
- id: cardiffmet/generic-2020/l7/analysis/60-69.s2
  cell: cardiffmet/generic-2020/l7/analysis/60-69
  span: { start: 78531, end: 78580 }
  source: "There is some linkage between theory and practice"
  versionsFrom: { sameAs: cardiffmet/generic-2020/l4/analysis/60-69.s2 }
  echoes: none
  force: describes
  terms:
    verbs: []
    objects: ["theory and practice"]
    degree: ["some"]
    independence: []
    scope: []
    deficits: []
- id: cardiffmet/generic-2020/l7/analysis/50-59.s1
  cell: cardiffmet/generic-2020/l7/analysis/50-59
  span: { start: 78626, end: 78963 }
  source: "An ability to conduct research or advanced technical or professional activity and undertake some limited analysis and enquiry relevant to the task/discipline and expertise in highly specialised and advanced technical, professional and/or research skills and has some success in presenting and commenting on research process and outcomes."
  versionsFrom: none
  echoes: none
  force: describes
  terms:
    verbs: [{ lemma: "comment", form: "commenting", taxonomy: ["none"] }, { lemma: "undertake", form: "undertake", taxonomy: ["none"] }, { lemma: "conduct", form: "conduct", taxonomy: ["solo:multistructural"] }, { lemma: "present", form: "presenting", taxonomy: ["none"] }]
    objects: ["research", "discipline", "research", "research"]
    degree: ["some", "limited", "highly", "some"]
    independence: []
    scope: ["advanced", "specialised", "advanced"]
    deficits: []
- id: cardiffmet/generic-2020/l7/analysis/40-49.s1
  cell: cardiffmet/generic-2020/l7/analysis/40-49
  span: { start: 79016, end: 79178 }
  source: "Likely to have attempted some enquiry and analysis relevant to the task/discipline but research process and outcomes may be naïve, simplistic and/or unconvincing."
  versionsFrom: none
  echoes: none
  force: describes
  terms:
    verbs: []
    objects: ["discipline", "research"]
    degree: ["some"]
    independence: []
    scope: []
    deficits: ["naïve", "simplistic", "unconvincing"]
- id: cardiffmet/generic-2020/l7/analysis/20-39.s1
  cell: cardiffmet/generic-2020/l7/analysis/20-39
  span: { start: 79229, end: 79325 }
  source: "Little evidence of being able to undertake enquiry and analysis relevant to the task/discipline."
  versionsFrom: none
  echoes: none
  force: describes
  terms:
    verbs: [{ lemma: "undertake", form: "undertake", taxonomy: ["none"] }]
    objects: ["discipline"]
    degree: ["little"]
    independence: []
    scope: []
    deficits: []
- id: cardiffmet/generic-2020/l7/analysis/20-39.s2
  cell: cardiffmet/generic-2020/l7/analysis/20-39
  span: { start: 79326, end: 79424 }
  source: "Where such work has been attempted, research process and outcomes may be inappropriate, or absent."
  versionsFrom: none
  echoes: none
  force: describes
  terms:
    verbs: []
    objects: ["research"]
    degree: []
    independence: []
    scope: []
    deficits: ["absent"]
- id: cardiffmet/generic-2020/l7/research/80-100.s1
  cell: cardiffmet/generic-2020/l7/research/80-100
  span: { start: 79595, end: 79788 }
  source: "Exceptional breadth and depth of knowledge and understanding evidenced by the student’s own independent insight and critical awareness of relevant literature at the forefront of the discipline."
  versionsFrom: none
  echoes: { statement: qaa/fheq-2024/annex-d/knowledge/r1/2.1, words: 7 }
  force: describes
  terms:
    verbs: []
    objects: ["knowledge and understanding", "literature", "forefront", "discipline"]
    degree: ["exceptional"]
    independence: ["independent"]
    scope: ["forefront"]
    deficits: []
- id: cardiffmet/generic-2020/l7/research/80-100.s2
  cell: cardiffmet/generic-2020/l7/research/80-100
  span: { start: 79789, end: 79936 }
  source: "In written coursework, reference citations extend significantly beyond the main body of reading normally expected in the discipline/field of study."
  versionsFrom: { sameAs: cardiffmet/generic-2020/l5/research/80-100.s1 }
  echoes: none
  force: describes
  terms:
    verbs: [{ lemma: "extend", form: "extend", taxonomy: ["bloom-r:understand"] }]
    objects: ["reading", "discipline", "field of study"]
    degree: []
    independence: []
    scope: ["main"]
    deficits: []
- id: cardiffmet/generic-2020/l7/research/80-100.s3
  cell: cardiffmet/generic-2020/l7/research/80-100
  span: { start: 79937, end: 80009 }
  source: "In examinations a substantial range of reference citations are included."
  versionsFrom: { sameAs: cardiffmet/generic-2020/l5/research/80-100.s2 }
  echoes: none
  force: describes
  terms:
    verbs: []
    objects: []
    degree: []
    independence: []
    scope: []
    deficits: []
- id: cardiffmet/generic-2020/l7/research/70-79.s1
  cell: cardiffmet/generic-2020/l7/research/70-79
  span: { start: 80063, end: 80174 }
  source: "A detailed and thorough knowledge and understanding of current research/advanced scholarship in the discipline."
  versionsFrom: none
  echoes: none
  force: describes
  terms:
    verbs: []
    objects: ["knowledge and understanding", "research", "scholarship", "discipline"]
    degree: ["detailed", "thorough"]
    independence: []
    scope: ["current", "advanced"]
    deficits: []
- id: cardiffmet/generic-2020/l7/research/70-79.s2
  cell: cardiffmet/generic-2020/l7/research/70-79
  span: { start: 80175, end: 80352 }
  source: "The use of scholarly reviews/primary sources is sophisticated and a breadth and depth of individual reading and investigation extending beyond the sources provided, is apparent."
  versionsFrom: { like: cardiffmet/generic-2020/l4/research/70-79.s2, similarity: 0.96 }
  echoes: none
  force: describes
  terms:
    verbs: [{ lemma: "use", form: "use", taxonomy: ["bloom-r:apply"] }]
    objects: ["primary sources", "reading", "sources"]
    degree: ["sophisticated"]
    independence: []
    scope: []
    deficits: []
- id: cardiffmet/generic-2020/l7/research/70-79.s3
  cell: cardiffmet/generic-2020/l7/research/70-79
  span: { start: 80353, end: 80451 }
  source: "The referencing of literature and other sources is accurate and in line with academic conventions."
  versionsFrom: { sameAs: cardiffmet/generic-2020/l3/research/70-79.s3 }
  echoes: none
  force: describes
  terms:
    verbs: []
    objects: ["referencing", "literature", "sources", "academic conventions"]
    degree: []
    independence: []
    scope: []
    deficits: []
- id: cardiffmet/generic-2020/l7/research/70-79.s4
  cell: cardiffmet/generic-2020/l7/research/70-79
  span: { start: 80452, end: 80631 }
  source: "A thorough knowledge and understanding of research processes, techniques and methods, is demonstrated along with an ability to design and apply appropriate research methodologies."
  versionsFrom: none
  echoes: none
  force: describes
  terms:
    verbs: [{ lemma: "demonstrate", form: "demonstrated", taxonomy: ["bloom-r:apply/understand"] }, { lemma: "apply", form: "apply", taxonomy: ["bloom-r:apply", "solo:relational"] }]
    objects: ["knowledge and understanding", "research processes", "techniques", "research"]
    degree: ["thorough"]
    independence: []
    scope: []
    deficits: []
- id: cardiffmet/generic-2020/l7/research/70-79.s5
  cell: cardiffmet/generic-2020/l7/research/70-79
  span: { start: 80632, end: 80709 }
  source: "Can apply research knowledge and skills successfully in appropriate contexts."
  versionsFrom: none
  echoes: none
  force: describes
  terms:
    verbs: [{ lemma: "apply", form: "apply", taxonomy: ["bloom-r:apply", "solo:relational"] }]
    objects: ["research", "knowledge"]
    degree: ["successfully"]
    independence: []
    scope: []
    deficits: []
- id: cardiffmet/generic-2020/l7/research/60-69.s1
  cell: cardiffmet/generic-2020/l7/research/60-69
  span: { start: 80757, end: 80846 }
  source: "A thorough knowledge and understanding of current research/scholarship in the discipline."
  versionsFrom: { sameAs: cardiffmet/generic-2020/l6/research/60-69.s1 }
  echoes: none
  force: describes
  terms:
    verbs: []
    objects: ["knowledge and understanding", "research", "scholarship", "discipline"]
    degree: ["thorough"]
    independence: []
    scope: ["current"]
    deficits: []
- id: cardiffmet/generic-2020/l7/research/60-69.s2
  cell: cardiffmet/generic-2020/l7/research/60-69
  span: { start: 80847, end: 80978 }
  source: "Examples referred to indicate a breadth and depth of individual reading and investigation that extends beyond the sources provided."
  versionsFrom: none
  echoes: none
  force: describes
  terms:
    verbs: [{ lemma: "extend", form: "extends", taxonomy: ["bloom-r:understand"] }]
    objects: ["reading", "sources"]
    degree: []
    independence: []
    scope: []
    deficits: []
- id: cardiffmet/generic-2020/l7/research/60-69.s3
  cell: cardiffmet/generic-2020/l7/research/60-69
  span: { start: 80979, end: 81053 }
  source: "The referencing of literature and other sources is almost always accurate."
  versionsFrom: { sameAs: cardiffmet/generic-2020/l3/research/60-69.s3 }
  echoes: none
  force: describes
  terms:
    verbs: []
    objects: ["referencing", "literature", "sources"]
    degree: []
    independence: []
    scope: []
    deficits: []
- id: cardiffmet/generic-2020/l7/research/60-69.s4
  cell: cardiffmet/generic-2020/l7/research/60-69
  span: { start: 81054, end: 81183 }
  source: "A secure knowledge of research processes is evident along with an ability to design and apply appropriate research methodologies."
  versionsFrom: none
  echoes: none
  force: describes
  terms:
    verbs: [{ lemma: "apply", form: "apply", taxonomy: ["bloom-r:apply", "solo:relational"] }]
    objects: ["knowledge", "research processes", "research"]
    degree: ["secure"]
    independence: []
    scope: []
    deficits: []
- id: cardiffmet/generic-2020/l7/research/60-69.s5
  cell: cardiffmet/generic-2020/l7/research/60-69
  span: { start: 81184, end: 81248 }
  source: "Can apply research skills and knowledge in appropriate contexts."
  versionsFrom: none
  echoes: none
  force: describes
  terms:
    verbs: [{ lemma: "apply", form: "apply", taxonomy: ["bloom-r:apply", "solo:relational"] }]
    objects: ["research", "knowledge"]
    degree: []
    independence: []
    scope: []
    deficits: []
- id: cardiffmet/generic-2020/l7/research/50-59.s1
  cell: cardiffmet/generic-2020/l7/research/50-59
  span: { start: 81295, end: 81463 }
  source: "Demonstrates knowledge and understanding of current research/scholarship in the discipline and an ability to provide some comment and/or discussion of its implications."
  versionsFrom: none
  echoes: none
  force: describes
  terms:
    verbs: [{ lemma: "demonstrate", form: "demonstrates", taxonomy: ["bloom-r:apply/understand"] }, { lemma: "comment", form: "comment", taxonomy: ["none"] }, { lemma: "provide", form: "provide", taxonomy: ["none"] }]
    objects: ["knowledge and understanding", "research", "scholarship", "discipline"]
    degree: ["some"]
    independence: []
    scope: ["current"]
    deficits: []
- id: cardiffmet/generic-2020/l7/research/50-59.s2
  cell: cardiffmet/generic-2020/l7/research/50-59
  span: { start: 81464, end: 81651 }
  source: "Examples of research/scholarship referred to in the work may indicate an over-reliance on given sources to advance work/direct arguments, rather than individual reading and investigation."
  versionsFrom: none
  echoes: none
  force: describes
  terms:
    verbs: []
    objects: ["research", "scholarship", "sources", "arguments", "reading"]
    degree: []
    independence: []
    scope: []
    deficits: ["over-reliance"]
- id: cardiffmet/generic-2020/l7/research/40-49.s1
  cell: cardiffmet/generic-2020/l7/research/40-49
  span: { start: 81705, end: 81803 }
  source: "Limited or sporadic knowledge and understanding of current research/scholarship in the discipline."
  versionsFrom: { sameAs: cardiffmet/generic-2020/l6/research/30-39.s1 }
  echoes: none
  force: describes
  terms:
    verbs: []
    objects: ["knowledge and understanding", "research", "scholarship", "discipline"]
    degree: ["limited"]
    independence: []
    scope: ["current"]
    deficits: []
- id: cardiffmet/generic-2020/l7/research/40-49.s2
  cell: cardiffmet/generic-2020/l7/research/40-49
  span: { start: 81804, end: 81966 }
  source: "A restricted range of sources are used, but overall there is an over-reliance on programme materials with little evidence of individual reading and investigation."
  versionsFrom: { sameAs: cardiffmet/generic-2020/l3/research/30-39.s2 }
  echoes: none
  force: describes
  terms:
    verbs: [{ lemma: "use", form: "used", taxonomy: ["bloom-r:apply"] }]
    objects: ["sources", "reading"]
    degree: ["little"]
    independence: []
    scope: []
    deficits: ["over-reliance"]
- id: cardiffmet/generic-2020/l7/research/40-49.s3
  cell: cardiffmet/generic-2020/l7/research/40-49
  span: { start: 81967, end: 82044 }
  source: "There are frequent errors in the referencing of literature and other sources."
  versionsFrom: { sameAs: cardiffmet/generic-2020/l3/research/30-39.s3 }
  echoes: none
  force: describes
  terms:
    verbs: []
    objects: ["referencing", "literature", "sources"]
    degree: []
    independence: []
    scope: []
    deficits: ["errors"]
- id: cardiffmet/generic-2020/l7/research/40-49.s4
  cell: cardiffmet/generic-2020/l7/research/40-49
  span: { start: 82045, end: 82094 }
  source: "Inconsistent application of academic conventions."
  versionsFrom: none
  echoes: none
  force: describes
  terms:
    verbs: [{ lemma: "apply", form: "application", taxonomy: ["bloom-r:apply", "solo:relational"] }]
    objects: ["academic conventions"]
    degree: []
    independence: []
    scope: []
    deficits: ["inconsistent"]
- id: cardiffmet/generic-2020/l7/research/40-49.s5
  cell: cardiffmet/generic-2020/l7/research/40-49
  span: { start: 82095, end: 82232 }
  source: "Although limited knowledge of research processes may be evident, nevertheless, the application of such knowledge is largely unsuccessful."
  versionsFrom: { sameAs: cardiffmet/generic-2020/l3/research/30-39.s4 }
  echoes: none
  force: describes
  terms:
    verbs: [{ lemma: "apply", form: "application", taxonomy: ["bloom-r:apply", "solo:relational"] }]
    objects: ["knowledge", "research processes", "knowledge"]
    degree: ["limited"]
    independence: []
    scope: []
    deficits: []
- id: cardiffmet/generic-2020/l7/research/20-39.s1
  cell: cardiffmet/generic-2020/l7/research/20-39
  span: { start: 82284, end: 82369 }
  source: "Little knowledge and understanding of current research/scholarship in the discipline."
  versionsFrom: { sameAs: cardiffmet/generic-2020/l6/research/1-29.s1 }
  echoes: none
  force: describes
  terms:
    verbs: []
    objects: ["knowledge and understanding", "research", "scholarship", "discipline"]
    degree: ["little"]
    independence: []
    scope: ["current"]
    deficits: []
- id: cardiffmet/generic-2020/l7/research/20-39.s2
  cell: cardiffmet/generic-2020/l7/research/20-39
  span: { start: 82370, end: 82518 }
  source: "Evidence of individual reading and investigation is negligible and the limited referencing of literature and other sources is frequently inaccurate."
  versionsFrom: { sameAs: cardiffmet/generic-2020/l3/research/1-29.s2 }
  echoes: none
  force: describes
  terms:
    verbs: []
    objects: ["reading", "referencing", "literature", "sources"]
    degree: ["limited"]
    independence: []
    scope: []
    deficits: ["negligible"]
- id: cardiffmet/generic-2020/l7/research/20-39.s3
  cell: cardiffmet/generic-2020/l7/research/20-39
  span: { start: 82519, end: 82623 }
  source: "Very limited knowledge of research processes is apparent and there is a failure to apply this knowledge."
  versionsFrom: { sameAs: cardiffmet/generic-2020/l3/research/1-29.s3 }
  echoes: none
  force: describes
  terms:
    verbs: [{ lemma: "apply", form: "apply", taxonomy: ["bloom-r:apply", "solo:relational"] }]
    objects: ["knowledge", "research processes", "knowledge"]
    degree: ["very limited"]
    independence: []
    scope: []
    deficits: ["failure"]
- id: cardiffmet/generic-2020/l7/argument/80-100.s1
  cell: cardiffmet/generic-2020/l7/argument/80-100
  span: { start: 82816, end: 82955 }
  source: "Work may challenge the boundaries of knowledge within the discipline/field of study and is informed by innovative and/or creative thinking."
  versionsFrom: { sameAs: cardiffmet/generic-2020/l6/argument/80-100.s1 }
  echoes: none
  force: describes
  terms:
    verbs: [{ lemma: "challenge", form: "challenge", taxonomy: ["none"] }]
    objects: ["knowledge", "discipline", "field of study"]
    degree: ["informed", "innovative"]
    independence: []
    scope: []
    deficits: []
- id: cardiffmet/generic-2020/l7/argument/80-100.s2
  cell: cardiffmet/generic-2020/l7/argument/80-100
  span: { start: 82956, end: 83078 }
  source: "New insights are offered that are informed by critical evaluation of current research/ scholarship/ professional practice."
  versionsFrom: { sameAs: cardiffmet/generic-2020/l6/argument/80-100.s2 }
  echoes: none
  force: describes
  terms:
    verbs: [{ lemma: "evaluate", form: "evaluation", taxonomy: ["bloom-r:analyze/create/evaluate", "solo:extended-abstract"] }]
    objects: ["research", "scholarship"]
    degree: ["informed"]
    independence: []
    scope: ["current"]
    deficits: []
- id: cardiffmet/generic-2020/l7/argument/70-79.s1
  cell: cardiffmet/generic-2020/l7/argument/70-79
  span: { start: 83153, end: 83313 }
  source: "An ability to engage in critical evaluation of concepts/arguments/data and to make appropriate and informed judgements where there are many interacting factors."
  versionsFrom: none
  echoes: none
  force: describes
  terms:
    verbs: [{ lemma: "evaluate", form: "evaluation", taxonomy: ["bloom-r:analyze/create/evaluate", "solo:extended-abstract"] }, { lemma: "make", form: "make", taxonomy: ["bloom-r:create"] }]
    objects: ["concepts", "arguments", "data"]
    degree: ["informed"]
    independence: []
    scope: []
    deficits: []
- id: cardiffmet/generic-2020/l7/argument/70-79.s2
  cell: cardiffmet/generic-2020/l7/argument/70-79
  span: { start: 83314, end: 83372 }
  source: "Arguments are well developed, sustained and substantiated."
  versionsFrom: { sameAs: cardiffmet/generic-2020/l4/argument/70-79.s2 }
  echoes: none
  force: describes
  terms:
    verbs: [{ lemma: "develop", form: "developed", taxonomy: ["bloom-r:apply/create"] }, { lemma: "sustain", form: "sustained", taxonomy: ["none"] }]
    objects: ["arguments"]
    degree: ["well"]
    independence: []
    scope: []
    deficits: []
- id: cardiffmet/generic-2020/l7/argument/70-79.s3
  cell: cardiffmet/generic-2020/l7/argument/70-79
  span: { start: 83373, end: 83486 }
  source: "Where relevant, assumptions are challenged and there is clear recognition of the complexities of academic debate."
  versionsFrom: { sameAs: cardiffmet/generic-2020/l5/argument/70-79.s3 }
  echoes: none
  force: describes
  terms:
    verbs: [{ lemma: "recognise", form: "recognition", taxonomy: ["solo:unistructural"] }, { lemma: "challenge", form: "challenged", taxonomy: ["none"] }]
    objects: []
    degree: ["clear"]
    independence: []
    scope: []
    deficits: []
- id: cardiffmet/generic-2020/l7/argument/70-79.s4
  cell: cardiffmet/generic-2020/l7/argument/70-79
  span: { start: 83487, end: 83558 }
  source: "Appropriate and sometimes innovative solutions are offered to problems."
  versionsFrom: none
  echoes: none
  force: describes
  terms:
    verbs: [{ lemma: "solve", form: "solutions", taxonomy: ["bloom-r:analyze/apply/create", "solo:multistructural"] }]
    objects: ["problems"]
    degree: ["innovative"]
    independence: []
    scope: []
    deficits: []
- id: cardiffmet/generic-2020/l7/argument/70-79.s5
  cell: cardiffmet/generic-2020/l7/argument/70-79
  span: { start: 83559, end: 83654 }
  source: "There is strong evidence that the student is able to reflect effectively on their own practice."
  versionsFrom: none
  echoes: none
  force: describes
  terms:
    verbs: [{ lemma: "reflect", form: "reflect", taxonomy: ["solo:extended-abstract"] }]
    objects: ["own practice"]
    degree: ["strong", "effectively"]
    independence: []
    scope: []
    deficits: []
- id: cardiffmet/generic-2020/l7/argument/70-79.s6
  cell: cardiffmet/generic-2020/l7/argument/70-79
  span: { start: 83655, end: 83824 }
  source: "Critical evaluation of the student’s own work and/or professional practice is highly perceptive and there is a full awareness of the implications for future development."
  versionsFrom: { sameAs: cardiffmet/generic-2020/l4/argument/70-79.s6 }
  echoes: none
  force: describes
  terms:
    verbs: [{ lemma: "evaluate", form: "evaluation", taxonomy: ["bloom-r:analyze/create/evaluate", "solo:extended-abstract"] }, { lemma: "develop", form: "development", taxonomy: ["bloom-r:apply/create"] }]
    objects: []
    degree: ["highly", "perceptive"]
    independence: []
    scope: []
    deficits: []
- id: cardiffmet/generic-2020/l7/argument/60-69.s1
  cell: cardiffmet/generic-2020/l7/argument/60-69
  span: { start: 83893, end: 83952 }
  source: "An ability to engage in critical evaluation and reflection."
  versionsFrom: { sameAs: cardiffmet/generic-2020/l6/argument/60-69.s1 }
  echoes: none
  force: describes
  terms:
    verbs: [{ lemma: "evaluate", form: "evaluation", taxonomy: ["bloom-r:analyze/create/evaluate", "solo:extended-abstract"] }, { lemma: "reflect", form: "reflection", taxonomy: ["solo:extended-abstract"] }]
    objects: []
    degree: []
    independence: []
    scope: []
    deficits: []
- id: cardiffmet/generic-2020/l7/argument/60-69.s2
  cell: cardiffmet/generic-2020/l7/argument/60-69
  span: { start: 83953, end: 84149 }
  source: "Arguments are clearly considered and substantiated and there is evidence of an ability to make appropriate judgements where there are many interacting factors and to suggest solutions to problems."
  versionsFrom: none
  echoes: none
  force: describes
  terms:
    verbs: [{ lemma: "make", form: "make", taxonomy: ["bloom-r:create"] }, { lemma: "solve", form: "solutions", taxonomy: ["bloom-r:analyze/apply/create", "solo:multistructural"] }]
    objects: ["arguments", "problems"]
    degree: ["clearly"]
    independence: []
    scope: []
    deficits: []
- id: cardiffmet/generic-2020/l7/argument/60-69.s3
  cell: cardiffmet/generic-2020/l7/argument/60-69
  span: { start: 84150, end: 84305 }
  source: "The student also demonstrates an ability to engage in reflective practice and to take account of personal evaluations when planning for future development."
  versionsFrom: { sameAs: cardiffmet/generic-2020/l3/argument/60-69.s4 }
  echoes: none
  force: describes
  terms:
    verbs: [{ lemma: "demonstrate", form: "demonstrates", taxonomy: ["bloom-r:apply/understand"] }, { lemma: "evaluate", form: "evaluations", taxonomy: ["bloom-r:analyze/create/evaluate", "solo:extended-abstract"] }, { lemma: "develop", form: "development", taxonomy: ["bloom-r:apply/create"] }, { lemma: "plan", form: "planning", taxonomy: ["bloom-r:create", "solo:relational"] }]
    objects: []
    degree: []
    independence: []
    scope: []
    deficits: []
- id: cardiffmet/generic-2020/l7/argument/50-59.s1
  cell: cardiffmet/generic-2020/l7/argument/50-59
  span: { start: 84373, end: 84426 }
  source: "A limited ability to critically evaluate and reflect."
  versionsFrom: { sameAs: cardiffmet/generic-2020/l6/argument/40-49.s1 }
  echoes: none
  force: describes
  terms:
    verbs: [{ lemma: "evaluate", form: "evaluate", taxonomy: ["bloom-r:analyze/create/evaluate", "solo:extended-abstract"] }, { lemma: "reflect", form: "reflect", taxonomy: ["solo:extended-abstract"] }]
    objects: []
    degree: ["limited"]
    independence: []
    scope: []
    deficits: []
- id: cardiffmet/generic-2020/l7/argument/50-59.s2
  cell: cardiffmet/generic-2020/l7/argument/50-59
  span: { start: 84427, end: 84567 }
  source: "Although some critical reflection is evident, the balance within the work is likely to be in favour of description and factual presentation."
  versionsFrom: { sameAs: cardiffmet/generic-2020/l5/argument/40-49.s2 }
  echoes: none
  force: describes
  terms:
    verbs: [{ lemma: "reflect", form: "reflection", taxonomy: ["solo:extended-abstract"] }, { lemma: "present", form: "presentation", taxonomy: ["none"] }, { lemma: "describe", form: "description", taxonomy: ["bloom-r:evaluate/remember/understand", "solo:multistructural"] }]
    objects: ["presentation"]
    degree: ["some"]
    independence: []
    scope: []
    deficits: []
- id: cardiffmet/generic-2020/l7/argument/50-59.s3
  cell: cardiffmet/generic-2020/l7/argument/50-59
  span: { start: 84568, end: 84633 }
  source: "Arguments are generally substantiated but may be under-developed."
  versionsFrom: { sameAs: cardiffmet/generic-2020/l3/argument/40-49.s3 }
  echoes: none
  force: describes
  terms:
    verbs: []
    objects: ["arguments"]
    degree: ["generally"]
    independence: []
    scope: []
    deficits: []
- id: cardiffmet/generic-2020/l7/argument/50-59.s4
  cell: cardiffmet/generic-2020/l7/argument/50-59
  span: { start: 84634, end: 84848 }
  source: "There is some evidence of the student’s ability to evaluate and reflect on their own practice although reflections may be limited and superficial with little consideration of their relevance for future development."
  versionsFrom: none
  echoes: none
  force: describes
  terms:
    verbs: [{ lemma: "evaluate", form: "evaluate", taxonomy: ["bloom-r:analyze/create/evaluate", "solo:extended-abstract"] }, { lemma: "develop", form: "development", taxonomy: ["bloom-r:apply/create"] }, { lemma: "consider", form: "consideration", taxonomy: ["none"] }, { lemma: "reflect", form: "reflect", taxonomy: ["solo:extended-abstract"] }]
    objects: ["own practice"]
    degree: ["some", "limited", "little"]
    independence: []
    scope: []
    deficits: ["superficial"]
- id: cardiffmet/generic-2020/l7/argument/40-49.s1
  cell: cardiffmet/generic-2020/l7/argument/40-49
  span: { start: 84923, end: 84977 }
  source: "Little evidence of critical evaluation and reflection."
  versionsFrom: none
  echoes: none
  force: describes
  terms:
    verbs: [{ lemma: "evaluate", form: "evaluation", taxonomy: ["bloom-r:analyze/create/evaluate", "solo:extended-abstract"] }, { lemma: "reflect", form: "reflection", taxonomy: ["solo:extended-abstract"] }]
    objects: []
    degree: ["little"]
    independence: []
    scope: []
    deficits: []
- id: cardiffmet/generic-2020/l7/argument/40-49.s2
  cell: cardiffmet/generic-2020/l7/argument/40-49
  span: { start: 84978, end: 85064 }
  source: "The work is largely descriptive and arguments, if attempted, are rarely substantiated."
  versionsFrom: { sameAs: cardiffmet/generic-2020/l3/argument/30-39.s2 }
  echoes: none
  force: describes
  terms:
    verbs: [{ lemma: "describe", form: "descriptive", taxonomy: ["bloom-r:evaluate/remember/understand", "solo:multistructural"] }]
    objects: ["arguments"]
    degree: []
    independence: []
    scope: []
    deficits: []
- id: cardiffmet/generic-2020/l7/argument/40-49.s3
  cell: cardiffmet/generic-2020/l7/argument/40-49
  span: { start: 85065, end: 85149 }
  source: "Self-evaluation and reflections on the student’s own practice are extremely limited."
  versionsFrom: { sameAs: cardiffmet/generic-2020/l3/argument/30-39.s3 }
  echoes: none
  force: describes
  terms:
    verbs: []
    objects: ["own practice"]
    degree: ["limited"]
    independence: []
    scope: []
    deficits: []
- id: cardiffmet/generic-2020/l7/argument/20-39.s1
  cell: cardiffmet/generic-2020/l7/argument/20-39
  span: { start: 85222, end: 85367 }
  source: "Some ability to describe and report but very little evidence is available to indicate an ability to engage in critical evaluation and reflection."
  versionsFrom: none
  echoes: none
  force: describes
  terms:
    verbs: [{ lemma: "evaluate", form: "evaluation", taxonomy: ["bloom-r:analyze/create/evaluate", "solo:extended-abstract"] }, { lemma: "reflect", form: "reflection", taxonomy: ["solo:extended-abstract"] }, { lemma: "describe", form: "describe", taxonomy: ["bloom-r:evaluate/remember/understand", "solo:multistructural"] }, { lemma: "report", form: "report", taxonomy: ["bloom-r:apply/understand", "solo:multistructural"] }]
    objects: []
    degree: ["some", "very little"]
    independence: []
    scope: []
    deficits: []
- id: cardiffmet/generic-2020/l7/argument/20-39.s2
  cell: cardiffmet/generic-2020/l7/argument/20-39
  span: { start: 85368, end: 85455 }
  source: "Self-evaluation and reflections on the student’s own practice are negligible or absent."
  versionsFrom: { sameAs: cardiffmet/generic-2020/l3/argument/1-29.s2 }
  echoes: none
  force: describes
  terms:
    verbs: []
    objects: ["own practice"]
    degree: []
    independence: []
    scope: []
    deficits: ["negligible", "absent"]
```

### S4a Audience versions
<!-- label: both; status: drafted; basis: primary. Per sentence: forPractitioner, what a marker looks for; forBeneficiary, what the student shows, second person, naming no issuer. Sentences with versionsFrom carry that sentence's versions. -->
```yaml
- sentence: cardiffmet/generic-2020/l3/overall/80-100.s1
  forPractitioner: { text: "Full, detailed grasp of the task; outcomes met and criteria addressed excellently (80-89) or outstandingly (90-100), past this level.", rewrite: light, force: describes, status: drafted }
  forBeneficiary: { text: "You understand the task fully and in detail and meet its outcomes excellently, or outstandingly above 90, past this level.", rewrite: full, force: describes, status: drafted }
- sentence: cardiffmet/generic-2020/l3/overall/70-79.s1
  forPractitioner: { text: "Full, detailed grasp of the task; outcomes met and criteria addressed very well.", rewrite: light, force: describes, status: drafted }
  forBeneficiary: { text: "You understand the task fully and in detail and meet its outcomes and criteria very well.", rewrite: full, force: describes, status: drafted }
- sentence: cardiffmet/generic-2020/l3/overall/60-69.s1
  forPractitioner: { text: "Full grasp of the task; outcomes met and criteria addressed well.", rewrite: light, force: describes, status: drafted }
  forBeneficiary: { text: "You understand the task fully and meet its outcomes and criteria well.", rewrite: full, force: describes, status: drafted }
- sentence: cardiffmet/generic-2020/l3/overall/50-59.s1
  forPractitioner: { text: "Secure grasp of the task; outcomes met and criteria addressed satisfactorily.", rewrite: light, force: describes, status: drafted }
  forBeneficiary: { text: "You understand the task securely and meet its outcomes and criteria satisfactorily.", rewrite: full, force: describes, status: drafted }
- sentence: cardiffmet/generic-2020/l3/overall/40-49.s1
  forPractitioner: { text: "Basic grasp of the task; outcomes met and criteria addressed at the threshold.", rewrite: light, force: describes, status: drafted }
  forBeneficiary: { text: "You understand the task at a basic level and meet its outcomes and criteria at the minimum standard.", rewrite: full, force: describes, status: drafted }
- sentence: cardiffmet/generic-2020/l3/overall/30-39.s1
  forPractitioner: { text: "Unsatisfactory overall.", rewrite: light, force: describes, status: drafted }
  forBeneficiary: { text: "Your work is not yet satisfactory overall.", rewrite: full, force: describes, status: drafted }
- sentence: cardiffmet/generic-2020/l3/overall/30-39.s2
  forPractitioner: { text: "Partial grasp of the task; some outcomes met at a basic level.", rewrite: light, force: describes, status: drafted }
  forBeneficiary: { text: "You understand the task in part and meet some outcomes at a basic level.", rewrite: full, force: describes, status: drafted }
- sentence: cardiffmet/generic-2020/l3/overall/30-39.s3
  forPractitioner: { text: "Uneven: some outcomes unmet, some criteria unaddressed.", rewrite: light, force: describes, status: drafted }
  forBeneficiary: { text: "Your work is uneven: some outcomes are not met and some criteria are not addressed.", rewrite: full, force: describes, status: drafted }
- sentence: cardiffmet/generic-2020/l3/overall/1-29.s1
  forPractitioner: { text: "Poor overall.", rewrite: light, force: describes, status: drafted }
  forBeneficiary: { text: "Your work is poor overall.", rewrite: full, force: describes, status: drafted }
- sentence: cardiffmet/generic-2020/l3/overall/1-29.s2
  forPractitioner: { text: "Minimal grasp of the task.", rewrite: light, force: describes, status: drafted }
  forBeneficiary: { text: "You show little understanding of the task.", rewrite: full, force: describes, status: drafted }
- sentence: cardiffmet/generic-2020/l3/overall/1-29.s3
  forPractitioner: { text: "One or two outcomes partly met, or none.", rewrite: light, force: describes, status: drafted }
  forBeneficiary: { text: "You meet one or two outcomes in part, or none.", rewrite: full, force: describes, status: drafted }
- sentence: cardiffmet/generic-2020/l3/overall/1-29.s4
  forPractitioner: { text: "Many criteria unaddressed.", rewrite: light, force: describes, status: drafted }
  forBeneficiary: { text: "You leave many of the criteria unaddressed.", rewrite: full, force: describes, status: drafted }
- sentence: cardiffmet/generic-2020/l3/knowledge/80-100.s1
  forPractitioner: { text: "The top band goes further than 70-79, past what this level expects.", rewrite: light, force: describes, status: drafted }
  forBeneficiary: { text: "At the top, your work goes further than first-class work and past what this level expects.", rewrite: full, force: describes, status: drafted }
- sentence: cardiffmet/generic-2020/l3/knowledge/70-79.s1
  forPractitioner: { text: "Detailed knowledge of the relevant field may be shown.", rewrite: light, force: describes, status: drafted }
  forBeneficiary: { text: "You may show detailed knowledge of the field the task covers.", rewrite: full, force: describes, status: drafted }
- sentence: cardiffmet/generic-2020/l3/knowledge/70-79.s2
  forPractitioner: { text: "Strong evidence of applying that knowledge.", rewrite: light, force: describes, status: drafted }
  forBeneficiary: { text: "You apply that knowledge strongly.", rewrite: full, force: describes, status: drafted }
- sentence: cardiffmet/generic-2020/l3/knowledge/70-79.s3
  forPractitioner: { text: "Confident discussion of basic concepts; aware of other perspectives or approaches.", rewrite: light, force: describes, status: drafted }
  forBeneficiary: { text: "You discuss basic ideas confidently and show you know other views and approaches.", rewrite: full, force: describes, status: drafted }
- sentence: cardiffmet/generic-2020/l3/knowledge/70-79.s4
  forPractitioner: { text: "Independent thinking is a feature.", rewrite: light, force: describes, status: drafted }
  forBeneficiary: { text: "You think for yourself.", rewrite: full, force: describes, status: drafted }
- sentence: cardiffmet/generic-2020/l3/knowledge/60-69.s1
  forPractitioner: { text: "Detailed knowledge of the relevant field may be shown.", rewrite: light, force: describes, status: drafted }
  forBeneficiary: { text: "You may show detailed knowledge of the field the task covers.", rewrite: full, force: describes, status: drafted }
- sentence: cardiffmet/generic-2020/l3/knowledge/60-69.s2
  forPractitioner: { text: "Clear evidence of applying that knowledge.", rewrite: light, force: describes, status: drafted }
  forBeneficiary: { text: "You apply that knowledge clearly.", rewrite: full, force: describes, status: drafted }
- sentence: cardiffmet/generic-2020/l3/knowledge/60-69.s3
  forPractitioner: { text: "Basic concepts often discussed well; some independent thinking.", rewrite: light, force: describes, status: drafted }
  forBeneficiary: { text: "You often discuss basic ideas well and show some thought of your own.", rewrite: full, force: describes, status: drafted }
- sentence: cardiffmet/generic-2020/l3/knowledge/50-59.s1
  forPractitioner: { text: "Sound knowledge of the relevant field may be shown.", rewrite: light, force: describes, status: drafted }
  forBeneficiary: { text: "You may show sound knowledge of the field the task covers.", rewrite: full, force: describes, status: drafted }
- sentence: cardiffmet/generic-2020/l3/knowledge/50-59.s2
  forPractitioner: { text: "Some leaning on received material, but still some independent thought.", rewrite: light, force: describes, status: drafted }
  forBeneficiary: { text: "You lean a little on course materials but still show some thought of your own.", rewrite: full, force: describes, status: drafted }
- sentence: cardiffmet/generic-2020/l3/knowledge/50-59.s3
  forPractitioner: { text: "A few errors or misconceptions, none in important areas.", rewrite: light, force: describes, status: drafted }
  forBeneficiary: { text: "You make a few mistakes, but none in important areas.", rewrite: full, force: describes, status: drafted }
- sentence: cardiffmet/generic-2020/l3/knowledge/40-49.s1
  forPractitioner: { text: "Basic knowledge of the relevant field may be shown.", rewrite: light, force: describes, status: drafted }
  forBeneficiary: { text: "You may show basic knowledge of the field the task covers.", rewrite: full, force: describes, status: drafted }
- sentence: cardiffmet/generic-2020/l3/knowledge/40-49.s2
  forPractitioner: { text: "Often reproduces received material.", rewrite: light, force: describes, status: drafted }
  forBeneficiary: { text: "You often repeat what course materials say.", rewrite: full, force: describes, status: drafted }
- sentence: cardiffmet/generic-2020/l3/knowledge/40-49.s3
  forPractitioner: { text: "Errors and misconceptions present, outweighed by what is understood.", rewrite: light, force: describes, status: drafted }
  forBeneficiary: { text: "You make mistakes, but what you understand outweighs them.", rewrite: full, force: describes, status: drafted }
- sentence: cardiffmet/generic-2020/l3/knowledge/30-39.s1
  forPractitioner: { text: "Limited knowledge of the relevant field may be shown.", rewrite: light, force: describes, status: drafted }
  forBeneficiary: { text: "You may show limited knowledge of the field the task covers.", rewrite: full, force: describes, status: drafted }
- sentence: cardiffmet/generic-2020/l3/knowledge/30-39.s2
  forPractitioner: { text: "Inaccuracies and misconceptions in important areas; parts may be off the task.", rewrite: light, force: describes, status: drafted }
  forBeneficiary: { text: "You make mistakes in important areas, and parts of your work may be off the task.", rewrite: full, force: describes, status: drafted }
- sentence: cardiffmet/generic-2020/l3/knowledge/1-29.s1
  forPractitioner: { text: "Little knowledge of the relevant field may be shown.", rewrite: light, force: describes, status: drafted }
  forBeneficiary: { text: "You may show little knowledge of the field the task covers.", rewrite: full, force: describes, status: drafted }
- sentence: cardiffmet/generic-2020/l3/knowledge/1-29.s2
  forPractitioner: { text: "Errors in many important areas outweigh what is understood.", rewrite: light, force: describes, status: drafted }
  forBeneficiary: { text: "Your mistakes in many important areas outweigh what you understand.", rewrite: full, force: describes, status: drafted }
- sentence: cardiffmet/generic-2020/l3/knowledge/1-29.s3
  forPractitioner: { text: "Much of the work may be off the task.", rewrite: light, force: describes, status: drafted }
  forBeneficiary: { text: "Much of your work may be off the task.", rewrite: full, force: describes, status: drafted }
- sentence: cardiffmet/generic-2020/l3/presentation/80-100.s1
  forPractitioner: { text: "The top band goes further than 70-79, past what this level expects.", rewrite: light, force: describes, status: drafted }
  forBeneficiary: { text: "At the top, your work goes further than first-class work and past what this level expects.", rewrite: full, force: describes, status: drafted }
- sentence: cardiffmet/generic-2020/l3/presentation/70-79.s1
  forPractitioner: { text: "Presents, weighs and interprets data to argue and judge soundly from basic theory.", rewrite: light, force: describes, status: drafted }
  forBeneficiary: { text: "You present and interpret numbers and other data to build arguments and judge soundly from basic theory.", rewrite: full, force: describes, status: drafted }
- sentence: cardiffmet/generic-2020/l3/presentation/70-79.s2
  forPractitioner: { text: "High standard of presentation; format fits.", rewrite: light, force: describes, status: drafted }
  forBeneficiary: { text: "Your work is presented to a high standard in a suitable format.", rewrite: full, force: describes, status: drafted }
- sentence: cardiffmet/generic-2020/l3/presentation/70-79.s3
  forPractitioner: { text: "Points logically organised; lucid style in writing.", rewrite: light, force: describes, status: drafted }
  forBeneficiary: { text: "Your points are logically ordered and your writing is lucid.", rewrite: full, force: describes, status: drafted }
- sentence: cardiffmet/generic-2020/l3/presentation/70-79.s4
  forPractitioner: { text: "Arguments well defined and clearly put.", rewrite: light, force: describes, status: drafted }
  forBeneficiary: { text: "Your arguments are well defined and clearly put.", rewrite: full, force: describes, status: drafted }
- sentence: cardiffmet/generic-2020/l3/presentation/60-69.s1
  forPractitioner: { text: "Presents, weighs and interprets data to argue and judge soundly from basic theory.", rewrite: light, force: describes, status: drafted }
  forBeneficiary: { text: "You present and interpret numbers and other data to build arguments and judge soundly from basic theory.", rewrite: full, force: describes, status: drafted }
- sentence: cardiffmet/generic-2020/l3/presentation/60-69.s2
  forPractitioner: { text: "Well presented; format fits.", rewrite: light, force: describes, status: drafted }
  forBeneficiary: { text: "Your work is well presented in a suitable format.", rewrite: full, force: describes, status: drafted }
- sentence: cardiffmet/generic-2020/l3/presentation/60-69.s3
  forPractitioner: { text: "Points organised; fluent style; arguments well put.", rewrite: light, force: describes, status: drafted }
  forBeneficiary: { text: "Your points are organised, your writing fluent and your arguments well put.", rewrite: full, force: describes, status: drafted }
- sentence: cardiffmet/generic-2020/l3/presentation/50-59.s1
  forPractitioner: { text: "Some ability to present and interpret data to argue and judge from basic theory.", rewrite: light, force: describes, status: drafted }
  forBeneficiary: { text: "You can present and interpret data to build arguments to some extent.", rewrite: full, force: describes, status: drafted }
- sentence: cardiffmet/generic-2020/l3/presentation/50-59.s2
  forPractitioner: { text: "Structure and format appropriate overall.", rewrite: light, force: describes, status: drafted }
  forBeneficiary: { text: "Your work is suitably structured and formatted overall.", rewrite: full, force: describes, status: drafted }
- sentence: cardiffmet/generic-2020/l3/presentation/50-59.s3
  forPractitioner: { text: "Occasional faults that do not cloud meaning.", rewrite: light, force: describes, status: drafted }
  forBeneficiary: { text: "You make occasional slips that do not cloud your meaning.", rewrite: full, force: describes, status: drafted }
- sentence: cardiffmet/generic-2020/l3/presentation/40-49.s1
  forPractitioner: { text: "Limited ability to present and interpret data to argue and judge from basic theory.", rewrite: light, force: describes, status: drafted }
  forBeneficiary: { text: "You present and interpret data to build arguments only to a limited extent.", rewrite: full, force: describes, status: drafted }
- sentence: cardiffmet/generic-2020/l3/presentation/40-49.s2
  forPractitioner: { text: "Better at reporting facts than conveying complex ideas.", rewrite: light, force: describes, status: drafted }
  forBeneficiary: { text: "You report facts better than you explain complex ideas.", rewrite: full, force: describes, status: drafted }
- sentence: cardiffmet/generic-2020/l3/presentation/40-49.s3
  forPractitioner: { text: "Mostly structured, though points may be out of order.", rewrite: light, force: describes, status: drafted }
  forBeneficiary: { text: "Your work is mostly structured, though some points may be out of order.", rewrite: full, force: describes, status: drafted }
- sentence: cardiffmet/generic-2020/l3/presentation/40-49.s4
  forPractitioner: { text: "Faults in presentation, but meaning clear.", rewrite: light, force: describes, status: drafted }
  forBeneficiary: { text: "There are faults in your presentation, but your meaning is clear.", rewrite: full, force: describes, status: drafted }
- sentence: cardiffmet/generic-2020/l3/presentation/30-39.s1
  forPractitioner: { text: "Limited ability to present and interpret data.", rewrite: light, force: describes, status: drafted }
  forBeneficiary: { text: "You present and interpret data only a little.", rewrite: full, force: describes, status: drafted }
- sentence: cardiffmet/generic-2020/l3/presentation/30-39.s2
  forPractitioner: { text: "Ideas may be unclear and hard for the reader to follow.", rewrite: light, force: describes, status: drafted }
  forBeneficiary: { text: "Your ideas may be unclear and hard to follow.", rewrite: full, force: describes, status: drafted }
- sentence: cardiffmet/generic-2020/l3/presentation/30-39.s3
  forPractitioner: { text: "Arguments and complex ideas, if tried, may be confused and clumsy.", rewrite: light, force: describes, status: drafted }
  forBeneficiary: { text: "Any arguments or complex ideas you try may come out confused.", rewrite: full, force: describes, status: drafted }
- sentence: cardiffmet/generic-2020/l3/presentation/1-29.s1
  forPractitioner: { text: "Little ability to present and interpret data.", rewrite: light, force: describes, status: drafted }
  forBeneficiary: { text: "You present and interpret data very little.", rewrite: full, force: describes, status: drafted }
- sentence: cardiffmet/generic-2020/l3/presentation/1-29.s2
  forPractitioner: { text: "Frequent faults and weak structure obscure meaning.", rewrite: light, force: describes, status: drafted }
  forBeneficiary: { text: "Frequent faults and weak structure hide your meaning.", rewrite: full, force: describes, status: drafted }
- sentence: cardiffmet/generic-2020/l3/presentation/1-29.s3
  forPractitioner: { text: "Writing often clumsy and unsuitable.", rewrite: light, force: describes, status: drafted }
  forBeneficiary: { text: "Your writing is often clumsy and unsuitable.", rewrite: full, force: describes, status: drafted }
- sentence: cardiffmet/generic-2020/l3/analysis/80-100.s1
  forPractitioner: { text: "The top band goes further than 70-79, past what this level expects.", rewrite: light, force: describes, status: drafted }
  forBeneficiary: { text: "At the top, your work goes further than first-class work and past what this level expects.", rewrite: full, force: describes, status: drafted }
- sentence: cardiffmet/generic-2020/l3/analysis/70-79.s1
  forPractitioner: { text: "Chooses and uses approaches, with fitting techniques, to defined but complex, non-routine problems.", rewrite: light, force: describes, status: drafted }
  forBeneficiary: { text: "You choose and use suitable methods for complex, unfamiliar problems.", rewrite: full, force: describes, status: drafted }
- sentence: cardiffmet/generic-2020/l3/analysis/70-79.s2
  forPractitioner: { text: "Presents and comments on results very successfully.", rewrite: light, force: describes, status: drafted }
  forBeneficiary: { text: "You present and comment on your results very successfully.", rewrite: full, force: describes, status: drafted }
- sentence: cardiffmet/generic-2020/l3/analysis/60-69.s1
  forPractitioner: { text: "Chooses and uses approaches, with fitting techniques, to complex, non-routine problems; presents and comments on results successfully.", rewrite: light, force: describes, status: drafted }
  forBeneficiary: { text: "You choose and use suitable methods for complex problems and present your results successfully.", rewrite: full, force: describes, status: drafted }
- sentence: cardiffmet/generic-2020/l3/analysis/50-59.s1
  forPractitioner: { text: "Chooses and uses approaches to complex, non-routine problems; generally succeeds with results.", rewrite: light, force: describes, status: drafted }
  forBeneficiary: { text: "You choose and use methods for complex problems and generally present your results well.", rewrite: full, force: describes, status: drafted }
- sentence: cardiffmet/generic-2020/l3/analysis/40-49.s1
  forPractitioner: { text: "Limited choice and use of approaches to complex problems; intermittent success with results.", rewrite: light, force: describes, status: drafted }
  forBeneficiary: { text: "You choose and use methods for complex problems only a little, with mixed success in presenting results.", rewrite: full, force: describes, status: drafted }
- sentence: cardiffmet/generic-2020/l3/analysis/30-39.s1
  forPractitioner: { text: "Limited choice and use of approaches; results may be naive, simplistic or unconvincing.", rewrite: light, force: describes, status: drafted }
  forBeneficiary: { text: "You choose and use methods only a little, and your results may be simplistic or unconvincing.", rewrite: full, force: describes, status: drafted }
- sentence: cardiffmet/generic-2020/l3/analysis/1-29.s1
  forPractitioner: { text: "Little choice or use of approaches to problems.", rewrite: light, force: describes, status: drafted }
  forBeneficiary: { text: "You show little use of methods for problems.", rewrite: full, force: describes, status: drafted }
- sentence: cardiffmet/generic-2020/l3/analysis/1-29.s2
  forPractitioner: { text: "Results, where attempted, unsuitable or missing.", rewrite: light, force: describes, status: drafted }
  forBeneficiary: { text: "Where you try, your results are unsuitable or missing.", rewrite: full, force: describes, status: drafted }
- sentence: cardiffmet/generic-2020/l3/research/80-100.s1
  forPractitioner: { text: "The top band goes further than 70-79, past what this level expects.", rewrite: light, force: describes, status: drafted }
  forBeneficiary: { text: "At the top, your work goes further than first-class work and past what this level expects.", rewrite: full, force: describes, status: drafted }
- sentence: cardiffmet/generic-2020/l3/research/70-79.s1
  forPractitioner: { text: "Awareness of current research or advanced scholarship may be shown.", rewrite: light, force: describes, status: drafted }
  forBeneficiary: { text: "You may show awareness of current research in the subject.", rewrite: full, force: describes, status: drafted }
- sentence: cardiffmet/generic-2020/l3/research/70-79.s2
  forPractitioner: { text: "Reviews and primary sources used; reading ranges beyond the sources given.", rewrite: light, force: describes, status: drafted }
  forBeneficiary: { text: "You use reviews and primary sources and read well past the sources you were given.", rewrite: full, force: describes, status: drafted }
- sentence: cardiffmet/generic-2020/l3/research/70-79.s3
  forPractitioner: { text: "Referencing accurate and conventional.", rewrite: light, force: describes, status: drafted }
  forBeneficiary: { text: "Your referencing is accurate and follows academic conventions.", rewrite: full, force: describes, status: drafted }
- sentence: cardiffmet/generic-2020/l3/research/70-79.s4
  forPractitioner: { text: "Understands research processes and methods and applies them successfully.", rewrite: light, force: describes, status: drafted }
  forBeneficiary: { text: "You understand research methods and use them successfully.", rewrite: full, force: describes, status: drafted }
- sentence: cardiffmet/generic-2020/l3/research/60-69.s1
  forPractitioner: { text: "Awareness of current research or advanced scholarship may be shown.", rewrite: light, force: describes, status: drafted }
  forBeneficiary: { text: "You may show awareness of current research in the subject.", rewrite: full, force: describes, status: drafted }
- sentence: cardiffmet/generic-2020/l3/research/60-69.s2
  forPractitioner: { text: "Reading ranges beyond the sources given.", rewrite: light, force: describes, status: drafted }
  forBeneficiary: { text: "Your examples show reading well past the sources you were given.", rewrite: full, force: describes, status: drafted }
- sentence: cardiffmet/generic-2020/l3/research/60-69.s3
  forPractitioner: { text: "Referencing almost always accurate.", rewrite: light, force: describes, status: drafted }
  forBeneficiary: { text: "Your referencing is almost always accurate.", rewrite: full, force: describes, status: drafted }
- sentence: cardiffmet/generic-2020/l3/research/60-69.s4
  forPractitioner: { text: "Basic grasp of research processes, applied fittingly.", rewrite: light, force: describes, status: drafted }
  forBeneficiary: { text: "You know the basics of research methods and use them well.", rewrite: full, force: describes, status: drafted }
- sentence: cardiffmet/generic-2020/l3/research/50-59.s1
  forPractitioner: { text: "Some awareness of current research may be shown.", rewrite: light, force: describes, status: drafted }
  forBeneficiary: { text: "You may show some awareness of current research.", rewrite: full, force: describes, status: drafted }
- sentence: cardiffmet/generic-2020/l3/research/50-59.s2
  forPractitioner: { text: "Some independent reading and investigation shown.", rewrite: light, force: describes, status: drafted }
  forBeneficiary: { text: "Your examples show some reading and investigation of your own.", rewrite: full, force: describes, status: drafted }
- sentence: cardiffmet/generic-2020/l3/research/50-59.s3
  forPractitioner: { text: "Occasional referencing errors.", rewrite: light, force: describes, status: drafted }
  forBeneficiary: { text: "Your referencing has occasional slips.", rewrite: full, force: describes, status: drafted }
- sentence: cardiffmet/generic-2020/l3/research/50-59.s4
  forPractitioner: { text: "Some grasp of research processes, generally applied well, perhaps relying on tutor support.", rewrite: light, force: describes, status: drafted }
  forBeneficiary: { text: "You know something of research methods and use them well, perhaps with your tutor's help.", rewrite: full, force: describes, status: drafted }
- sentence: cardiffmet/generic-2020/l3/research/40-49.s1
  forPractitioner: { text: "Limited awareness of current research may be shown.", rewrite: light, force: describes, status: drafted }
  forBeneficiary: { text: "You may show limited awareness of current research.", rewrite: full, force: describes, status: drafted }
- sentence: cardiffmet/generic-2020/l3/research/40-49.s2
  forPractitioner: { text: "May over-rely on course materials rather than own reading.", rewrite: light, force: describes, status: drafted }
  forBeneficiary: { text: "You may rely on course materials more than on your own reading.", rewrite: full, force: describes, status: drafted }
- sentence: cardiffmet/generic-2020/l3/research/40-49.s3
  forPractitioner: { text: "Referencing errors.", rewrite: light, force: describes, status: drafted }
  forBeneficiary: { text: "Your referencing has errors.", rewrite: full, force: describes, status: drafted }
- sentence: cardiffmet/generic-2020/l3/research/40-49.s4
  forPractitioner: { text: "Some grasp of research processes, applied less securely.", rewrite: light, force: describes, status: drafted }
  forBeneficiary: { text: "You know something of research methods but use them unsteadily.", rewrite: full, force: describes, status: drafted }
- sentence: cardiffmet/generic-2020/l3/research/30-39.s1
  forPractitioner: { text: "Limited or patchy awareness of current research may be shown.", rewrite: light, force: describes, status: drafted }
  forBeneficiary: { text: "Your awareness of current research may be limited or patchy.", rewrite: full, force: describes, status: drafted }
- sentence: cardiffmet/generic-2020/l3/research/30-39.s2
  forPractitioner: { text: "Narrow sources; over-reliance on course materials; little own reading.", rewrite: light, force: describes, status: drafted }
  forBeneficiary: { text: "You use a narrow set of sources, rely on course materials and read little for yourself.", rewrite: full, force: describes, status: drafted }
- sentence: cardiffmet/generic-2020/l3/research/30-39.s3
  forPractitioner: { text: "Frequent referencing errors.", rewrite: light, force: describes, status: drafted }
  forBeneficiary: { text: "Your referencing has frequent errors.", rewrite: full, force: describes, status: drafted }
- sentence: cardiffmet/generic-2020/l3/research/30-39.s4
  forPractitioner: { text: "Research knowledge, where present, applied largely without success.", rewrite: light, force: describes, status: drafted }
  forBeneficiary: { text: "Where you know research methods, you mostly fail to apply them.", rewrite: full, force: describes, status: drafted }
- sentence: cardiffmet/generic-2020/l3/research/1-29.s1
  forPractitioner: { text: "Little knowledge of current research may be shown.", rewrite: light, force: describes, status: drafted }
  forBeneficiary: { text: "You may show little knowledge of current research.", rewrite: full, force: describes, status: drafted }
- sentence: cardiffmet/generic-2020/l3/research/1-29.s2
  forPractitioner: { text: "Negligible own reading; scant referencing, often wrong.", rewrite: light, force: describes, status: drafted }
  forBeneficiary: { text: "You do almost no reading of your own, and your few references are often wrong.", rewrite: full, force: describes, status: drafted }
- sentence: cardiffmet/generic-2020/l3/research/1-29.s3
  forPractitioner: { text: "Very limited grasp of research processes, not applied.", rewrite: light, force: describes, status: drafted }
  forBeneficiary: { text: "You know very little about research methods and do not apply them.", rewrite: full, force: describes, status: drafted }
- sentence: cardiffmet/generic-2020/l3/argument/80-100.s1
  forPractitioner: { text: "The top band goes further than 70-79, past what this level expects.", rewrite: light, force: describes, status: drafted }
  forBeneficiary: { text: "At the top, your work goes further than first-class work and past what this level expects.", rewrite: full, force: describes, status: drafted }
- sentence: cardiffmet/generic-2020/l3/argument/70-79.s1
  forPractitioner: { text: "Reports results accurately and reliably in structured arguments.", rewrite: light, force: describes, status: drafted }
  forBeneficiary: { text: "You report your results accurately in well-built arguments.", rewrite: full, force: describes, status: drafted }
- sentence: cardiffmet/generic-2020/l3/argument/70-79.s2
  forPractitioner: { text: "Arguments developed and supported; sees the complexity of academic debate.", rewrite: light, force: describes, status: drafted }
  forBeneficiary: { text: "Your arguments are developed and supported, and you see how complex academic debate is.", rewrite: full, force: describes, status: drafted }
- sentence: cardiffmet/generic-2020/l3/argument/70-79.s3
  forPractitioner: { text: "Offers fitting solutions and reviews how well the methods worked.", rewrite: light, force: describes, status: drafted }
  forBeneficiary: { text: "You offer suitable solutions and review how well your methods worked.", rewrite: full, force: describes, status: drafted }
- sentence: cardiffmet/generic-2020/l3/argument/70-79.s4
  forPractitioner: { text: "Reflects effectively on own practice, fully aware of what it means for future development.", rewrite: light, force: describes, status: drafted }
  forBeneficiary: { text: "You reflect well on your own practice and see clearly what it means for how you develop.", rewrite: full, force: describes, status: drafted }
- sentence: cardiffmet/generic-2020/l3/argument/60-69.s1
  forPractitioner: { text: "Reports results accurately and reliably.", rewrite: light, force: describes, status: drafted }
  forBeneficiary: { text: "You report your results accurately.", rewrite: full, force: describes, status: drafted }
- sentence: cardiffmet/generic-2020/l3/argument/60-69.s2
  forPractitioner: { text: "Arguments considered and supported; judges fittingly and suggests solutions.", rewrite: light, force: describes, status: drafted }
  forBeneficiary: { text: "Your arguments are considered and supported, and you judge well and suggest solutions.", rewrite: full, force: describes, status: drafted }
- sentence: cardiffmet/generic-2020/l3/argument/60-69.s3
  forPractitioner: { text: "Reviews how well the methods worked.", rewrite: light, force: describes, status: drafted }
  forBeneficiary: { text: "You review how well your methods worked.", rewrite: full, force: describes, status: drafted }
- sentence: cardiffmet/generic-2020/l3/argument/60-69.s4
  forPractitioner: { text: "Reflects on own practice and uses self-evaluation to plan development.", rewrite: light, force: describes, status: drafted }
  forBeneficiary: { text: "You reflect on your practice and use what you find to plan how to develop.", rewrite: full, force: describes, status: drafted }
- sentence: cardiffmet/generic-2020/l3/argument/50-59.s1
  forPractitioner: { text: "Reports results accurately at times, leaning on description and fact.", rewrite: light, force: describes, status: drafted }
  forBeneficiary: { text: "You sometimes report your results accurately, but lean on description.", rewrite: full, force: describes, status: drafted }
- sentence: cardiffmet/generic-2020/l3/argument/50-59.s2
  forPractitioner: { text: "Arguments usually supported.", rewrite: light, force: describes, status: drafted }
  forBeneficiary: { text: "Your arguments are usually supported.", rewrite: full, force: describes, status: drafted }
- sentence: cardiffmet/generic-2020/l3/argument/50-59.s3
  forPractitioner: { text: "Some reflection on own practice, lacking insight into future development.", rewrite: light, force: describes, status: drafted }
  forBeneficiary: { text: "You reflect on your own practice, but without much insight into how to develop.", rewrite: full, force: describes, status: drafted }
- sentence: cardiffmet/generic-2020/l3/argument/40-49.s1
  forPractitioner: { text: "Limited accurate reporting of results.", rewrite: light, force: describes, status: drafted }
  forBeneficiary: { text: "You report your results accurately only to a limited extent.", rewrite: full, force: describes, status: drafted }
- sentence: cardiffmet/generic-2020/l3/argument/40-49.s2
  forPractitioner: { text: "Mostly description and fact.", rewrite: light, force: describes, status: drafted }
  forBeneficiary: { text: "Your work is mostly description and fact.", rewrite: full, force: describes, status: drafted }
- sentence: cardiffmet/generic-2020/l3/argument/40-49.s3
  forPractitioner: { text: "Arguments generally supported but thin.", rewrite: light, force: describes, status: drafted }
  forBeneficiary: { text: "Your arguments are generally supported but thin.", rewrite: full, force: describes, status: drafted }
- sentence: cardiffmet/generic-2020/l3/argument/40-49.s4
  forPractitioner: { text: "Some reflection on own practice, limited and superficial, with little thought for development.", rewrite: light, force: describes, status: drafted }
  forBeneficiary: { text: "You reflect on your practice, but only briefly and on the surface.", rewrite: full, force: describes, status: drafted }
- sentence: cardiffmet/generic-2020/l3/argument/30-39.s1
  forPractitioner: { text: "Limited sign of accurate reporting.", rewrite: light, force: describes, status: drafted }
  forBeneficiary: { text: "You show little accurate reporting of your results.", rewrite: full, force: describes, status: drafted }
- sentence: cardiffmet/generic-2020/l3/argument/30-39.s2
  forPractitioner: { text: "Largely descriptive; arguments, if tried, rarely supported.", rewrite: light, force: describes, status: drafted }
  forBeneficiary: { text: "Your work is largely descriptive, and any arguments are rarely supported.", rewrite: full, force: describes, status: drafted }
- sentence: cardiffmet/generic-2020/l3/argument/30-39.s3
  forPractitioner: { text: "Self-evaluation very limited.", rewrite: light, force: describes, status: drafted }
  forBeneficiary: { text: "You reflect on your own practice very little.", rewrite: full, force: describes, status: drafted }
- sentence: cardiffmet/generic-2020/l3/argument/1-29.s1
  forPractitioner: { text: "Little sign of accurate reporting.", rewrite: light, force: describes, status: drafted }
  forBeneficiary: { text: "You show almost no accurate reporting of your results.", rewrite: full, force: describes, status: drafted }
- sentence: cardiffmet/generic-2020/l3/argument/1-29.s2
  forPractitioner: { text: "Self-evaluation negligible or absent.", rewrite: light, force: describes, status: drafted }
  forBeneficiary: { text: "You reflect on your own practice little or not at all.", rewrite: full, force: describes, status: drafted }
- sentence: cardiffmet/generic-2020/l4/overall/80-100.s1
  forPractitioner: { text: "Full, detailed grasp of the task; outcomes met and criteria addressed excellently (80-89) or outstandingly (90-100), past this level.", rewrite: light, force: describes, status: drafted }
  forBeneficiary: { text: "You understand the task fully and in detail and meet its outcomes excellently, or outstandingly above 90, past this level.", rewrite: full, force: describes, status: drafted }
- sentence: cardiffmet/generic-2020/l4/overall/70-79.s1
  forPractitioner: { text: "Full, detailed grasp of the task; outcomes met and criteria addressed very well.", rewrite: light, force: describes, status: drafted }
  forBeneficiary: { text: "You understand the task fully and in detail and meet its outcomes and criteria very well.", rewrite: full, force: describes, status: drafted }
- sentence: cardiffmet/generic-2020/l4/overall/60-69.s1
  forPractitioner: { text: "Full grasp of the task; outcomes met and criteria addressed well.", rewrite: light, force: describes, status: drafted }
  forBeneficiary: { text: "You understand the task fully and meet its outcomes and criteria well.", rewrite: full, force: describes, status: drafted }
- sentence: cardiffmet/generic-2020/l4/overall/50-59.s1
  forPractitioner: { text: "Secure grasp of the task; outcomes met and criteria addressed satisfactorily.", rewrite: light, force: describes, status: drafted }
  forBeneficiary: { text: "You understand the task securely and meet its outcomes and criteria satisfactorily.", rewrite: full, force: describes, status: drafted }
- sentence: cardiffmet/generic-2020/l4/overall/40-49.s1
  forPractitioner: { text: "Basic grasp of the task; outcomes met and criteria addressed at the threshold.", rewrite: light, force: describes, status: drafted }
  forBeneficiary: { text: "You understand the task at a basic level and meet its outcomes and criteria at the minimum standard.", rewrite: full, force: describes, status: drafted }
- sentence: cardiffmet/generic-2020/l4/overall/30-39.s1
  forPractitioner: { text: "Unsatisfactory overall.", rewrite: light, force: describes, status: drafted }
  forBeneficiary: { text: "Your work is not yet satisfactory overall.", rewrite: full, force: describes, status: drafted }
- sentence: cardiffmet/generic-2020/l4/overall/30-39.s2
  forPractitioner: { text: "Partial grasp of the task; some outcomes met at a basic level.", rewrite: light, force: describes, status: drafted }
  forBeneficiary: { text: "You understand the task in part and meet some outcomes at a basic level.", rewrite: full, force: describes, status: drafted }
- sentence: cardiffmet/generic-2020/l4/overall/30-39.s3
  forPractitioner: { text: "Uneven: some outcomes unmet, some criteria unaddressed.", rewrite: light, force: describes, status: drafted }
  forBeneficiary: { text: "Your work is uneven: some outcomes are not met and some criteria are not addressed.", rewrite: full, force: describes, status: drafted }
- sentence: cardiffmet/generic-2020/l4/overall/1-29.s1
  forPractitioner: { text: "Poor overall.", rewrite: light, force: describes, status: drafted }
  forBeneficiary: { text: "Your work is poor overall.", rewrite: full, force: describes, status: drafted }
- sentence: cardiffmet/generic-2020/l4/overall/1-29.s2
  forPractitioner: { text: "Minimal grasp of the task; one or two outcomes partly met, or none.", rewrite: light, force: describes, status: drafted }
  forBeneficiary: { text: "You show little understanding of the task and meet one or two outcomes in part, or none.", rewrite: full, force: describes, status: drafted }
- sentence: cardiffmet/generic-2020/l4/overall/1-29.s3
  forPractitioner: { text: "Many criteria unaddressed.", rewrite: light, force: describes, status: drafted }
  forBeneficiary: { text: "You leave many of the criteria unaddressed.", rewrite: full, force: describes, status: drafted }
- sentence: cardiffmet/generic-2020/l4/knowledge/80-100.s1
  forPractitioner: { text: "The top band goes further than 70-79, past what this level expects.", rewrite: light, force: describes, status: drafted }
  forBeneficiary: { text: "At the top, your work goes further than first-class work and past what this level expects.", rewrite: full, force: describes, status: drafted }
- sentence: cardiffmet/generic-2020/l4/knowledge/70-79.s1
  forPractitioner: { text: "Detailed knowledge of the field's underlying aspects may be shown.", rewrite: light, force: describes, status: drafted }
  forBeneficiary: { text: "You may show detailed knowledge of the basics of the field the task covers.", rewrite: full, force: describes, status: drafted }
- sentence: cardiffmet/generic-2020/l4/knowledge/70-79.s2
  forPractitioner: { text: "Strong evidence of applying that knowledge.", rewrite: light, force: describes, status: drafted }
  forBeneficiary: { text: "You apply that knowledge strongly.", rewrite: full, force: describes, status: drafted }
- sentence: cardiffmet/generic-2020/l4/knowledge/70-79.s3
  forPractitioner: { text: "Confident discussion of basic concepts; aware of the limits and ambiguity of knowledge in the discipline.", rewrite: light, force: describes, status: drafted }
  forBeneficiary: { text: "You discuss basic ideas confidently and see where your subject's knowledge is limited or unclear.", rewrite: full, force: describes, status: drafted }
- sentence: cardiffmet/generic-2020/l4/knowledge/70-79.s4
  forPractitioner: { text: "Independent thinking and original insight are features.", rewrite: light, force: describes, status: drafted }
  forBeneficiary: { text: "You think for yourself and offer original insight.", rewrite: full, force: describes, status: drafted }
- sentence: cardiffmet/generic-2020/l4/knowledge/60-69.s1
  forPractitioner: { text: "Detailed knowledge of the field's underlying aspects may be shown.", rewrite: light, force: describes, status: drafted }
  forBeneficiary: { text: "You may show detailed knowledge of the basics of the field the task covers.", rewrite: full, force: describes, status: drafted }
- sentence: cardiffmet/generic-2020/l4/knowledge/60-69.s2
  forPractitioner: { text: "Clear evidence of applying knowledge and, in places, extending and transforming it.", rewrite: light, force: describes, status: drafted }
  forBeneficiary: { text: "You apply what you know clearly and sometimes take it further.", rewrite: full, force: describes, status: drafted }
- sentence: cardiffmet/generic-2020/l4/knowledge/60-69.s3
  forPractitioner: { text: "Basic concepts often discussed well; some independent thinking.", rewrite: light, force: describes, status: drafted }
  forBeneficiary: { text: "You often discuss basic ideas well and show some thought of your own.", rewrite: full, force: describes, status: drafted }
- sentence: cardiffmet/generic-2020/l4/knowledge/50-59.s1
  forPractitioner: { text: "Sound knowledge of the field's underlying aspects may be shown.", rewrite: light, force: describes, status: drafted }
  forBeneficiary: { text: "You may show sound knowledge of the basics of the field.", rewrite: full, force: describes, status: drafted }
- sentence: cardiffmet/generic-2020/l4/knowledge/50-59.s2
  forPractitioner: { text: "Some leaning on received material, but still some independent thought.", rewrite: light, force: describes, status: drafted }
  forBeneficiary: { text: "You lean a little on course materials but still show some thought of your own.", rewrite: full, force: describes, status: drafted }
- sentence: cardiffmet/generic-2020/l4/knowledge/50-59.s3
  forPractitioner: { text: "A few errors or misconceptions, none in important areas.", rewrite: light, force: describes, status: drafted }
  forBeneficiary: { text: "You make a few mistakes, but none in important areas.", rewrite: full, force: describes, status: drafted }
- sentence: cardiffmet/generic-2020/l4/knowledge/40-49.s1
  forPractitioner: { text: "Basic knowledge of the field's underlying aspects may be shown.", rewrite: light, force: describes, status: drafted }
  forBeneficiary: { text: "You may show basic knowledge of the basics of the field.", rewrite: full, force: describes, status: drafted }
- sentence: cardiffmet/generic-2020/l4/knowledge/40-49.s2
  forPractitioner: { text: "Often reproduces received material.", rewrite: light, force: describes, status: drafted }
  forBeneficiary: { text: "You often repeat what course materials say.", rewrite: full, force: describes, status: drafted }
- sentence: cardiffmet/generic-2020/l4/knowledge/40-49.s3
  forPractitioner: { text: "Errors and misconceptions present, outweighed by what is understood.", rewrite: light, force: describes, status: drafted }
  forBeneficiary: { text: "You make mistakes, but what you understand outweighs them.", rewrite: full, force: describes, status: drafted }
- sentence: cardiffmet/generic-2020/l4/knowledge/30-39.s1
  forPractitioner: { text: "Limited knowledge of the field's underlying aspects may be shown.", rewrite: light, force: describes, status: drafted }
  forBeneficiary: { text: "You may show limited knowledge of the basics of the field.", rewrite: full, force: describes, status: drafted }
- sentence: cardiffmet/generic-2020/l4/knowledge/30-39.s2
  forPractitioner: { text: "Inaccuracies and misconceptions in important areas; parts may be off the task.", rewrite: light, force: describes, status: drafted }
  forBeneficiary: { text: "You make mistakes in important areas, and parts of your work may be off the task.", rewrite: full, force: describes, status: drafted }
- sentence: cardiffmet/generic-2020/l4/knowledge/1-29.s1
  forPractitioner: { text: "Little knowledge of the field's underlying aspects may be shown.", rewrite: light, force: describes, status: drafted }
  forBeneficiary: { text: "You may show little knowledge of the basics of the field.", rewrite: full, force: describes, status: drafted }
- sentence: cardiffmet/generic-2020/l4/knowledge/1-29.s2
  forPractitioner: { text: "Errors in many important areas outweigh what is understood.", rewrite: light, force: describes, status: drafted }
  forBeneficiary: { text: "Your mistakes in many important areas outweigh what you understand.", rewrite: full, force: describes, status: drafted }
- sentence: cardiffmet/generic-2020/l4/knowledge/1-29.s3
  forPractitioner: { text: "Much of the work may be off the task.", rewrite: light, force: describes, status: drafted }
  forBeneficiary: { text: "Much of your work may be off the task.", rewrite: full, force: describes, status: drafted }
- sentence: cardiffmet/generic-2020/l4/presentation/80-100.s1
  forPractitioner: { text: "The top band goes further than 70-79, past what this level expects.", rewrite: light, force: describes, status: drafted }
  forBeneficiary: { text: "At the top, your work goes further than first-class work and past what this level expects.", rewrite: full, force: describes, status: drafted }
- sentence: cardiffmet/generic-2020/l4/presentation/70-79.s1
  forPractitioner: { text: "Presents, weighs and interprets data to argue and judge soundly from basic theory.", rewrite: light, force: describes, status: drafted }
  forBeneficiary: { text: "You present and interpret numbers and other data to build arguments and judge soundly from basic theory.", rewrite: full, force: describes, status: drafted }
- sentence: cardiffmet/generic-2020/l4/presentation/70-79.s2
  forPractitioner: { text: "High standard of presentation; format fits.", rewrite: light, force: describes, status: drafted }
  forBeneficiary: { text: "Your work is presented to a high standard in a suitable format.", rewrite: full, force: describes, status: drafted }
- sentence: cardiffmet/generic-2020/l4/presentation/70-79.s3
  forPractitioner: { text: "Points logically organised; lucid style in writing.", rewrite: light, force: describes, status: drafted }
  forBeneficiary: { text: "Your points are logically ordered and your writing is lucid.", rewrite: full, force: describes, status: drafted }
- sentence: cardiffmet/generic-2020/l4/presentation/70-79.s4
  forPractitioner: { text: "Arguments well defined, clearly put, structured and coherent.", rewrite: light, force: describes, status: drafted }
  forBeneficiary: { text: "Your arguments are well defined, clear, structured and coherent.", rewrite: full, force: describes, status: drafted }
- sentence: cardiffmet/generic-2020/l4/presentation/60-69.s1
  forPractitioner: { text: "Presents, weighs and interprets data to argue and judge soundly from basic theory.", rewrite: light, force: describes, status: drafted }
  forBeneficiary: { text: "You present and interpret numbers and other data to build arguments and judge soundly from basic theory.", rewrite: full, force: describes, status: drafted }
- sentence: cardiffmet/generic-2020/l4/presentation/60-69.s2
  forPractitioner: { text: "Well presented; format fits.", rewrite: light, force: describes, status: drafted }
  forBeneficiary: { text: "Your work is well presented in a suitable format.", rewrite: full, force: describes, status: drafted }
- sentence: cardiffmet/generic-2020/l4/presentation/60-69.s3
  forPractitioner: { text: "Points organised; fluent style; arguments well put, structured and coherent.", rewrite: light, force: describes, status: drafted }
  forBeneficiary: { text: "Your points are organised, your writing fluent and your arguments structured and coherent.", rewrite: full, force: describes, status: drafted }
- sentence: cardiffmet/generic-2020/l4/presentation/50-59.s1
  forPractitioner: { text: "Some ability to present and interpret data to argue and judge from basic theory.", rewrite: light, force: describes, status: drafted }
  forBeneficiary: { text: "You can present and interpret data to build arguments to some extent.", rewrite: full, force: describes, status: drafted }
- sentence: cardiffmet/generic-2020/l4/presentation/50-59.s2
  forPractitioner: { text: "Structure and format appropriate overall.", rewrite: light, force: describes, status: drafted }
  forBeneficiary: { text: "Your work is suitably structured and formatted overall.", rewrite: full, force: describes, status: drafted }
- sentence: cardiffmet/generic-2020/l4/presentation/50-59.s3
  forPractitioner: { text: "Occasional faults that do not cloud meaning.", rewrite: light, force: describes, status: drafted }
  forBeneficiary: { text: "You make occasional slips that do not cloud your meaning.", rewrite: full, force: describes, status: drafted }
- sentence: cardiffmet/generic-2020/l4/presentation/40-49.s1
  forPractitioner: { text: "Limited ability to present and interpret data to argue and judge from basic theory.", rewrite: light, force: describes, status: drafted }
  forBeneficiary: { text: "You present and interpret data to build arguments only to a limited extent.", rewrite: full, force: describes, status: drafted }
- sentence: cardiffmet/generic-2020/l4/presentation/40-49.s2
  forPractitioner: { text: "Better at reporting facts than conveying complex ideas.", rewrite: light, force: describes, status: drafted }
  forBeneficiary: { text: "You report facts better than you explain complex ideas.", rewrite: full, force: describes, status: drafted }
- sentence: cardiffmet/generic-2020/l4/presentation/40-49.s3
  forPractitioner: { text: "Mostly structured, though points may be out of order.", rewrite: light, force: describes, status: drafted }
  forBeneficiary: { text: "Your work is mostly structured, though some points may be out of order.", rewrite: full, force: describes, status: drafted }
- sentence: cardiffmet/generic-2020/l4/presentation/40-49.s4
  forPractitioner: { text: "Faults in presentation, but meaning clear.", rewrite: light, force: describes, status: drafted }
  forBeneficiary: { text: "There are faults in your presentation, but your meaning is clear.", rewrite: full, force: describes, status: drafted }
- sentence: cardiffmet/generic-2020/l4/presentation/30-39.s1
  forPractitioner: { text: "Limited ability to present and interpret data.", rewrite: light, force: describes, status: drafted }
  forBeneficiary: { text: "You present and interpret data only a little.", rewrite: full, force: describes, status: drafted }
- sentence: cardiffmet/generic-2020/l4/presentation/30-39.s2
  forPractitioner: { text: "Ideas may be unclear and hard for the reader to follow.", rewrite: light, force: describes, status: drafted }
  forBeneficiary: { text: "Your ideas may be unclear and hard to follow.", rewrite: full, force: describes, status: drafted }
- sentence: cardiffmet/generic-2020/l4/presentation/30-39.s3
  forPractitioner: { text: "Arguments and complex ideas, if tried, may be confused and clumsy.", rewrite: light, force: describes, status: drafted }
  forBeneficiary: { text: "Any arguments or complex ideas you try may come out confused.", rewrite: full, force: describes, status: drafted }
- sentence: cardiffmet/generic-2020/l4/presentation/1-29.s1
  forPractitioner: { text: "Little ability to present and interpret data.", rewrite: light, force: describes, status: drafted }
  forBeneficiary: { text: "You present and interpret data very little.", rewrite: full, force: describes, status: drafted }
- sentence: cardiffmet/generic-2020/l4/presentation/1-29.s2
  forPractitioner: { text: "Frequent faults and weak structure obscure meaning.", rewrite: light, force: describes, status: drafted }
  forBeneficiary: { text: "Frequent faults and weak structure hide your meaning.", rewrite: full, force: describes, status: drafted }
- sentence: cardiffmet/generic-2020/l4/presentation/1-29.s3
  forPractitioner: { text: "Writing often clumsy and unsuitable.", rewrite: light, force: describes, status: drafted }
  forBeneficiary: { text: "Your writing is often clumsy and unsuitable.", rewrite: full, force: describes, status: drafted }
- sentence: cardiffmet/generic-2020/l4/analysis/80-100.s1
  forPractitioner: { text: "The top band goes further than 70-79, past what this level expects.", rewrite: light, force: describes, status: drafted }
  forBeneficiary: { text: "At the top, your work goes further than first-class work and past what this level expects.", rewrite: full, force: describes, status: drafted }
- sentence: cardiffmet/generic-2020/l4/analysis/70-79.s1
  forPractitioner: { text: "Evaluates how well different approaches suit defined but complex, non-routine problems.", rewrite: light, force: describes, status: drafted }
  forBeneficiary: { text: "You judge how well different methods suit complex, unfamiliar problems.", rewrite: full, force: describes, status: drafted }
- sentence: cardiffmet/generic-2020/l4/analysis/70-79.s2
  forPractitioner: { text: "Presents and comments on results very successfully; comments perceptively on theory and practice.", rewrite: light, force: describes, status: drafted }
  forBeneficiary: { text: "You present and comment on your results very successfully and say perceptive things about how theory meets practice.", rewrite: full, force: describes, status: drafted }
- sentence: cardiffmet/generic-2020/l4/analysis/60-69.s1
  forPractitioner: { text: "Evaluates approaches to complex problems with fitting techniques; considerable success with results.", rewrite: light, force: describes, status: drafted }
  forBeneficiary: { text: "You judge which methods suit complex problems, use suitable techniques and present your results with considerable success.", rewrite: full, force: describes, status: drafted }
- sentence: cardiffmet/generic-2020/l4/analysis/60-69.s2
  forPractitioner: { text: "Some link made between theory and practice.", rewrite: light, force: describes, status: drafted }
  forBeneficiary: { text: "You link theory with practice to some degree.", rewrite: full, force: describes, status: drafted }
- sentence: cardiffmet/generic-2020/l4/analysis/50-59.s1
  forPractitioner: { text: "Evaluates approaches to complex problems; generally succeeds with results.", rewrite: light, force: describes, status: drafted }
  forBeneficiary: { text: "You judge which methods suit complex problems and generally present your results well.", rewrite: full, force: describes, status: drafted }
- sentence: cardiffmet/generic-2020/l4/analysis/40-49.s1
  forPractitioner: { text: "Limited evaluation of approaches to complex problems; intermittent success with results.", rewrite: light, force: describes, status: drafted }
  forBeneficiary: { text: "You judge methods for complex problems only a little, with mixed success in presenting results.", rewrite: full, force: describes, status: drafted }
- sentence: cardiffmet/generic-2020/l4/analysis/30-39.s1
  forPractitioner: { text: "Limited evaluation of approaches; results may be naive, simplistic or unconvincing.", rewrite: light, force: describes, status: drafted }
  forBeneficiary: { text: "You judge methods only a little, and your results may be simplistic or unconvincing.", rewrite: full, force: describes, status: drafted }
- sentence: cardiffmet/generic-2020/l4/analysis/1-29.s1
  forPractitioner: { text: "Little evaluation of approaches to problems.", rewrite: light, force: describes, status: drafted }
  forBeneficiary: { text: "You show little judgement of which methods suit a problem.", rewrite: full, force: describes, status: drafted }
- sentence: cardiffmet/generic-2020/l4/analysis/1-29.s2
  forPractitioner: { text: "Results, where attempted, unsuitable or missing.", rewrite: light, force: describes, status: drafted }
  forBeneficiary: { text: "Where you try, your results are unsuitable or missing.", rewrite: full, force: describes, status: drafted }
- sentence: cardiffmet/generic-2020/l4/research/80-100.s1
  forPractitioner: { text: "The top band goes further than 70-79, past what this level expects.", rewrite: light, force: describes, status: drafted }
  forBeneficiary: { text: "At the top, your work goes further than first-class work and past what this level expects.", rewrite: full, force: describes, status: drafted }
- sentence: cardiffmet/generic-2020/l4/research/70-79.s1
  forPractitioner: { text: "Awareness of current research or advanced scholarship may be shown.", rewrite: light, force: describes, status: drafted }
  forBeneficiary: { text: "You may show awareness of current research in the subject.", rewrite: full, force: describes, status: drafted }
- sentence: cardiffmet/generic-2020/l4/research/70-79.s2
  forPractitioner: { text: "Confident use of reviews and primary sources; broad, deep reading beyond the sources given.", rewrite: light, force: describes, status: drafted }
  forBeneficiary: { text: "You use reviews and primary sources confidently and read broadly and deeply past the sources given.", rewrite: full, force: describes, status: drafted }
- sentence: cardiffmet/generic-2020/l4/research/70-79.s3
  forPractitioner: { text: "Referencing accurate and conventional.", rewrite: light, force: describes, status: drafted }
  forBeneficiary: { text: "Your referencing is accurate and follows academic conventions.", rewrite: full, force: describes, status: drafted }
- sentence: cardiffmet/generic-2020/l4/research/70-79.s4
  forPractitioner: { text: "Understands research processes and methods and applies them successfully.", rewrite: light, force: describes, status: drafted }
  forBeneficiary: { text: "You understand research methods and use them successfully.", rewrite: full, force: describes, status: drafted }
- sentence: cardiffmet/generic-2020/l4/research/60-69.s1
  forPractitioner: { text: "Awareness of current research or advanced scholarship may be shown.", rewrite: light, force: describes, status: drafted }
  forBeneficiary: { text: "You may show awareness of current research in the subject.", rewrite: full, force: describes, status: drafted }
- sentence: cardiffmet/generic-2020/l4/research/60-69.s2
  forPractitioner: { text: "Reading broad and deep, beyond the sources given.", rewrite: light, force: describes, status: drafted }
  forBeneficiary: { text: "Your examples show broad, deep reading past the sources given.", rewrite: full, force: describes, status: drafted }
- sentence: cardiffmet/generic-2020/l4/research/60-69.s3
  forPractitioner: { text: "Referencing almost always accurate.", rewrite: light, force: describes, status: drafted }
  forBeneficiary: { text: "Your referencing is almost always accurate.", rewrite: full, force: describes, status: drafted }
- sentence: cardiffmet/generic-2020/l4/research/60-69.s4
  forPractitioner: { text: "Basic grasp of research processes, applied fittingly.", rewrite: light, force: describes, status: drafted }
  forBeneficiary: { text: "You know the basics of research methods and use them well.", rewrite: full, force: describes, status: drafted }
- sentence: cardiffmet/generic-2020/l4/research/50-59.s1
  forPractitioner: { text: "Some awareness of current research may be shown.", rewrite: light, force: describes, status: drafted }
  forBeneficiary: { text: "You may show some awareness of current research.", rewrite: full, force: describes, status: drafted }
- sentence: cardiffmet/generic-2020/l4/research/50-59.s2
  forPractitioner: { text: "Some independent reading and investigation shown.", rewrite: light, force: describes, status: drafted }
  forBeneficiary: { text: "Your examples show some reading and investigation of your own.", rewrite: full, force: describes, status: drafted }
- sentence: cardiffmet/generic-2020/l4/research/50-59.s3
  forPractitioner: { text: "Occasional referencing errors.", rewrite: light, force: describes, status: drafted }
  forBeneficiary: { text: "Your referencing has occasional slips.", rewrite: full, force: describes, status: drafted }
- sentence: cardiffmet/generic-2020/l4/research/50-59.s4
  forPractitioner: { text: "Some grasp of research processes, generally applied well, perhaps relying on tutor support.", rewrite: light, force: describes, status: drafted }
  forBeneficiary: { text: "You know something of research methods and use them well, perhaps with your tutor's help.", rewrite: full, force: describes, status: drafted }
- sentence: cardiffmet/generic-2020/l4/research/40-49.s1
  forPractitioner: { text: "Limited awareness of current research may be shown.", rewrite: light, force: describes, status: drafted }
  forBeneficiary: { text: "You may show limited awareness of current research.", rewrite: full, force: describes, status: drafted }
- sentence: cardiffmet/generic-2020/l4/research/40-49.s2
  forPractitioner: { text: "May over-rely on course materials rather than own reading.", rewrite: light, force: describes, status: drafted }
  forBeneficiary: { text: "You may rely on course materials more than on your own reading.", rewrite: full, force: describes, status: drafted }
- sentence: cardiffmet/generic-2020/l4/research/40-49.s3
  forPractitioner: { text: "Referencing errors.", rewrite: light, force: describes, status: drafted }
  forBeneficiary: { text: "Your referencing has errors.", rewrite: full, force: describes, status: drafted }
- sentence: cardiffmet/generic-2020/l4/research/40-49.s4
  forPractitioner: { text: "Some grasp of research processes, applied less securely.", rewrite: light, force: describes, status: drafted }
  forBeneficiary: { text: "You know something of research methods but use them unsteadily.", rewrite: full, force: describes, status: drafted }
- sentence: cardiffmet/generic-2020/l4/research/30-39.s1
  forPractitioner: { text: "Limited or patchy awareness of current research may be shown.", rewrite: light, force: describes, status: drafted }
  forBeneficiary: { text: "Your awareness of current research may be limited or patchy.", rewrite: full, force: describes, status: drafted }
- sentence: cardiffmet/generic-2020/l4/research/30-39.s2
  forPractitioner: { text: "Narrow sources; over-reliance on course materials; little own reading.", rewrite: light, force: describes, status: drafted }
  forBeneficiary: { text: "You use a narrow set of sources, rely on course materials and read little for yourself.", rewrite: full, force: describes, status: drafted }
- sentence: cardiffmet/generic-2020/l4/research/30-39.s3
  forPractitioner: { text: "Frequent referencing errors.", rewrite: light, force: describes, status: drafted }
  forBeneficiary: { text: "Your referencing has frequent errors.", rewrite: full, force: describes, status: drafted }
- sentence: cardiffmet/generic-2020/l4/research/30-39.s4
  forPractitioner: { text: "Research knowledge, where present, applied largely without success.", rewrite: light, force: describes, status: drafted }
  forBeneficiary: { text: "Where you know research methods, you mostly fail to apply them.", rewrite: full, force: describes, status: drafted }
- sentence: cardiffmet/generic-2020/l4/research/1-29.s1
  forPractitioner: { text: "Little knowledge of current research may be shown.", rewrite: light, force: describes, status: drafted }
  forBeneficiary: { text: "You may show little knowledge of current research.", rewrite: full, force: describes, status: drafted }
- sentence: cardiffmet/generic-2020/l4/research/1-29.s2
  forPractitioner: { text: "Negligible own reading; scant referencing, often wrong.", rewrite: light, force: describes, status: drafted }
  forBeneficiary: { text: "You do almost no reading of your own, and your few references are often wrong.", rewrite: full, force: describes, status: drafted }
- sentence: cardiffmet/generic-2020/l4/research/1-29.s3
  forPractitioner: { text: "Very limited grasp of research processes, not applied.", rewrite: light, force: describes, status: drafted }
  forBeneficiary: { text: "You know very little about research methods and do not apply them.", rewrite: full, force: describes, status: drafted }
- sentence: cardiffmet/generic-2020/l4/argument/80-100.s1
  forPractitioner: { text: "The top band goes further than 70-79, past what this level expects.", rewrite: light, force: describes, status: drafted }
  forBeneficiary: { text: "At the top, your work goes further than first-class work and past what this level expects.", rewrite: full, force: describes, status: drafted }
- sentence: cardiffmet/generic-2020/l4/argument/70-79.s1
  forPractitioner: { text: "Reports results accurately in structured, coherent arguments.", rewrite: light, force: describes, status: drafted }
  forBeneficiary: { text: "You report your results accurately in structured, coherent arguments.", rewrite: full, force: describes, status: drafted }
- sentence: cardiffmet/generic-2020/l4/argument/70-79.s2
  forPractitioner: { text: "Arguments developed, sustained and supported.", rewrite: light, force: describes, status: drafted }
  forBeneficiary: { text: "Your arguments are developed, sustained and supported.", rewrite: full, force: describes, status: drafted }
- sentence: cardiffmet/generic-2020/l4/argument/70-79.s3
  forPractitioner: { text: "Challenges basic assumptions where relevant; sees the complexity of academic debate.", rewrite: light, force: describes, status: drafted }
  forBeneficiary: { text: "You question basic assumptions where it matters and see how complex academic debate is.", rewrite: full, force: describes, status: drafted }
- sentence: cardiffmet/generic-2020/l4/argument/70-79.s4
  forPractitioner: { text: "Offers fitting solutions and reviews how effective and suitable they are.", rewrite: light, force: describes, status: drafted }
  forBeneficiary: { text: "You offer suitable solutions and review how well they work.", rewrite: full, force: describes, status: drafted }
- sentence: cardiffmet/generic-2020/l4/argument/70-79.s5
  forPractitioner: { text: "Strong evidence of reflecting effectively on own practice.", rewrite: light, force: describes, status: drafted }
  forBeneficiary: { text: "You reflect well on your own practice.", rewrite: full, force: describes, status: drafted }
- sentence: cardiffmet/generic-2020/l4/argument/70-79.s6
  forPractitioner: { text: "Highly perceptive evaluation of own work or practice; fully aware of what it means for development.", rewrite: light, force: describes, status: drafted }
  forBeneficiary: { text: "You evaluate your own work with sharp insight and see clearly what it means for how you develop.", rewrite: full, force: describes, status: drafted }
- sentence: cardiffmet/generic-2020/l4/argument/60-69.s1
  forPractitioner: { text: "Reports results accurately and reliably.", rewrite: light, force: describes, status: drafted }
  forBeneficiary: { text: "You report your results accurately.", rewrite: full, force: describes, status: drafted }
- sentence: cardiffmet/generic-2020/l4/argument/60-69.s2
  forPractitioner: { text: "Arguments considered and supported; judges fittingly, suggests solutions and reviews them.", rewrite: light, force: describes, status: drafted }
  forBeneficiary: { text: "Your arguments are considered and supported, and you judge well, suggest solutions and review them.", rewrite: full, force: describes, status: drafted }
- sentence: cardiffmet/generic-2020/l4/argument/60-69.s3
  forPractitioner: { text: "Reflects on own practice and uses self-evaluation to plan development.", rewrite: light, force: describes, status: drafted }
  forBeneficiary: { text: "You reflect on your practice and use what you find to plan how to develop.", rewrite: full, force: describes, status: drafted }
- sentence: cardiffmet/generic-2020/l4/argument/50-59.s1
  forPractitioner: { text: "Reports results accurately at times, leaning on description and fact.", rewrite: light, force: describes, status: drafted }
  forBeneficiary: { text: "You sometimes report your results accurately, but lean on description.", rewrite: full, force: describes, status: drafted }
- sentence: cardiffmet/generic-2020/l4/argument/50-59.s2
  forPractitioner: { text: "Arguments usually supported.", rewrite: light, force: describes, status: drafted }
  forBeneficiary: { text: "Your arguments are usually supported.", rewrite: full, force: describes, status: drafted }
- sentence: cardiffmet/generic-2020/l4/argument/50-59.s3
  forPractitioner: { text: "Some reflection on own practice, lacking insight into future development.", rewrite: light, force: describes, status: drafted }
  forBeneficiary: { text: "You reflect on your own practice, but without much insight into how to develop.", rewrite: full, force: describes, status: drafted }
- sentence: cardiffmet/generic-2020/l4/argument/40-49.s1
  forPractitioner: { text: "Limited accurate reporting of results.", rewrite: light, force: describes, status: drafted }
  forBeneficiary: { text: "You report your results accurately only to a limited extent.", rewrite: full, force: describes, status: drafted }
- sentence: cardiffmet/generic-2020/l4/argument/40-49.s2
  forPractitioner: { text: "Mostly description and fact.", rewrite: light, force: describes, status: drafted }
  forBeneficiary: { text: "Your work is mostly description and fact.", rewrite: full, force: describes, status: drafted }
- sentence: cardiffmet/generic-2020/l4/argument/40-49.s3
  forPractitioner: { text: "Arguments generally supported but thin.", rewrite: light, force: describes, status: drafted }
  forBeneficiary: { text: "Your arguments are generally supported but thin.", rewrite: full, force: describes, status: drafted }
- sentence: cardiffmet/generic-2020/l4/argument/40-49.s4
  forPractitioner: { text: "Some reflection on own practice, limited and superficial, with little thought for development.", rewrite: light, force: describes, status: drafted }
  forBeneficiary: { text: "You reflect on your practice, but only briefly and on the surface.", rewrite: full, force: describes, status: drafted }
- sentence: cardiffmet/generic-2020/l4/argument/30-39.s1
  forPractitioner: { text: "Limited sign of accurate reporting.", rewrite: light, force: describes, status: drafted }
  forBeneficiary: { text: "You show little accurate reporting of your results.", rewrite: full, force: describes, status: drafted }
- sentence: cardiffmet/generic-2020/l4/argument/30-39.s2
  forPractitioner: { text: "Largely descriptive; arguments, if tried, rarely supported.", rewrite: light, force: describes, status: drafted }
  forBeneficiary: { text: "Your work is largely descriptive, and any arguments are rarely supported.", rewrite: full, force: describes, status: drafted }
- sentence: cardiffmet/generic-2020/l4/argument/30-39.s3
  forPractitioner: { text: "Self-evaluation very limited.", rewrite: light, force: describes, status: drafted }
  forBeneficiary: { text: "You reflect on your own practice very little.", rewrite: full, force: describes, status: drafted }
- sentence: cardiffmet/generic-2020/l4/argument/1-29.s1
  forPractitioner: { text: "Little sign of accurate reporting.", rewrite: light, force: describes, status: drafted }
  forBeneficiary: { text: "You show almost no accurate reporting of your results.", rewrite: full, force: describes, status: drafted }
- sentence: cardiffmet/generic-2020/l4/argument/1-29.s2
  forPractitioner: { text: "Self-evaluation negligible or absent.", rewrite: light, force: describes, status: drafted }
  forBeneficiary: { text: "You reflect on your own practice little or not at all.", rewrite: full, force: describes, status: drafted }
- sentence: cardiffmet/generic-2020/l5/overall/80-100.s1
  forPractitioner: { text: "Full, detailed grasp of the task; outcomes met and criteria addressed excellently (80-89) or outstandingly (90-100), past this level.", rewrite: light, force: describes, status: drafted }
  forBeneficiary: { text: "You understand the task fully and in detail and meet its outcomes excellently, or outstandingly above 90, past this level.", rewrite: full, force: describes, status: drafted }
- sentence: cardiffmet/generic-2020/l5/overall/70-79.s1
  forPractitioner: { text: "Full, detailed grasp of the task; outcomes met and criteria addressed very well.", rewrite: light, force: describes, status: drafted }
  forBeneficiary: { text: "You understand the task fully and in detail and meet its outcomes and criteria very well.", rewrite: full, force: describes, status: drafted }
- sentence: cardiffmet/generic-2020/l5/overall/60-69.s1
  forPractitioner: { text: "Full grasp of the task; outcomes met and criteria addressed well.", rewrite: light, force: describes, status: drafted }
  forBeneficiary: { text: "You understand the task fully and meet its outcomes and criteria well.", rewrite: full, force: describes, status: drafted }
- sentence: cardiffmet/generic-2020/l5/overall/50-59.s1
  forPractitioner: { text: "Secure grasp of the task; outcomes met and criteria addressed satisfactorily.", rewrite: light, force: describes, status: drafted }
  forBeneficiary: { text: "You understand the task securely and meet its outcomes and criteria satisfactorily.", rewrite: full, force: describes, status: drafted }
- sentence: cardiffmet/generic-2020/l5/overall/40-49.s1
  forPractitioner: { text: "Basic grasp of the task; outcomes met and criteria addressed at the threshold.", rewrite: light, force: describes, status: drafted }
  forBeneficiary: { text: "You understand the task at a basic level and meet its outcomes and criteria at the minimum standard.", rewrite: full, force: describes, status: drafted }
- sentence: cardiffmet/generic-2020/l5/overall/30-39.s1
  forPractitioner: { text: "Unsatisfactory overall.", rewrite: light, force: describes, status: drafted }
  forBeneficiary: { text: "Your work is not yet satisfactory overall.", rewrite: full, force: describes, status: drafted }
- sentence: cardiffmet/generic-2020/l5/overall/30-39.s2
  forPractitioner: { text: "Partial grasp of the task; some outcomes met at a basic level.", rewrite: light, force: describes, status: drafted }
  forBeneficiary: { text: "You understand the task in part and meet some outcomes at a basic level.", rewrite: full, force: describes, status: drafted }
- sentence: cardiffmet/generic-2020/l5/overall/30-39.s3
  forPractitioner: { text: "Uneven: some outcomes unmet, some criteria unaddressed.", rewrite: light, force: describes, status: drafted }
  forBeneficiary: { text: "Your work is uneven: some outcomes are not met and some criteria are not addressed.", rewrite: full, force: describes, status: drafted }
- sentence: cardiffmet/generic-2020/l5/overall/1-29.s1
  forPractitioner: { text: "Poor overall.", rewrite: light, force: describes, status: drafted }
  forBeneficiary: { text: "Your work is poor overall.", rewrite: full, force: describes, status: drafted }
- sentence: cardiffmet/generic-2020/l5/overall/1-29.s2
  forPractitioner: { text: "Minimal grasp of the task; one or two outcomes partly met, or none.", rewrite: light, force: describes, status: drafted }
  forBeneficiary: { text: "You show little understanding of the task and meet one or two outcomes in part, or none.", rewrite: full, force: describes, status: drafted }
- sentence: cardiffmet/generic-2020/l5/overall/1-29.s3
  forPractitioner: { text: "Many criteria unaddressed.", rewrite: light, force: describes, status: drafted }
  forBeneficiary: { text: "You leave many of the criteria unaddressed.", rewrite: full, force: describes, status: drafted }
- sentence: cardiffmet/generic-2020/l5/knowledge/80-100.s1
  forPractitioner: { text: "The top band goes further than 70-79, past what this level expects.", rewrite: light, force: describes, status: drafted }
  forBeneficiary: { text: "At the top, your work goes further than first-class work and past what this level expects.", rewrite: full, force: describes, status: drafted }
- sentence: cardiffmet/generic-2020/l5/knowledge/70-79.s1
  forPractitioner: { text: "Detailed knowledge and critical understanding of the field's concepts and principles.", rewrite: light, force: describes, status: drafted }
  forBeneficiary: { text: "You know your field's concepts and principles in detail and understand them critically.", rewrite: full, force: describes, status: drafted }
- sentence: cardiffmet/generic-2020/l5/knowledge/70-79.s2
  forPractitioner: { text: "Strong evidence of extending, transforming and applying that knowledge.", rewrite: light, force: describes, status: drafted }
  forBeneficiary: { text: "You take what you know further, reshape it and apply it strongly.", rewrite: full, force: describes, status: drafted }
- sentence: cardiffmet/generic-2020/l5/knowledge/70-79.s3
  forPractitioner: { text: "Confident discussion of complex concepts; recognises the limits and ambiguity of knowledge.", rewrite: light, force: describes, status: drafted }
  forBeneficiary: { text: "You discuss complex ideas confidently and see where knowledge is limited or unclear.", rewrite: full, force: describes, status: drafted }
- sentence: cardiffmet/generic-2020/l5/knowledge/70-79.s4
  forPractitioner: { text: "Independent thinking and original insight are features.", rewrite: light, force: describes, status: drafted }
  forBeneficiary: { text: "You think for yourself and offer original insight.", rewrite: full, force: describes, status: drafted }
- sentence: cardiffmet/generic-2020/l5/knowledge/60-69.s1
  forPractitioner: { text: "Detailed knowledge and critical understanding of the field's concepts and principles.", rewrite: light, force: describes, status: drafted }
  forBeneficiary: { text: "You know your field's concepts and principles in detail and understand them critically.", rewrite: full, force: describes, status: drafted }
- sentence: cardiffmet/generic-2020/l5/knowledge/60-69.s2
  forPractitioner: { text: "Good evidence of extending, transforming and applying that knowledge.", rewrite: light, force: describes, status: drafted }
  forBeneficiary: { text: "You take what you know further, reshape it and apply it well.", rewrite: full, force: describes, status: drafted }
- sentence: cardiffmet/generic-2020/l5/knowledge/60-69.s3
  forPractitioner: { text: "Complex concepts often discussed well; independent thinking.", rewrite: light, force: describes, status: drafted }
  forBeneficiary: { text: "You often discuss complex ideas well and think for yourself.", rewrite: full, force: describes, status: drafted }
- sentence: cardiffmet/generic-2020/l5/knowledge/50-59.s1
  forPractitioner: { text: "Sound knowledge and critical understanding of concepts and principles.", rewrite: light, force: describes, status: drafted }
  forBeneficiary: { text: "You know your field's concepts and principles soundly and understand them critically.", rewrite: full, force: describes, status: drafted }
- sentence: cardiffmet/generic-2020/l5/knowledge/50-59.s2
  forPractitioner: { text: "Evidence of extending, transforming and applying that knowledge.", rewrite: light, force: describes, status: drafted }
  forBeneficiary: { text: "You take what you know further and apply it.", rewrite: full, force: describes, status: drafted }
- sentence: cardiffmet/generic-2020/l5/knowledge/50-59.s3
  forPractitioner: { text: "Some reproduction of received material, but still some independent thought.", rewrite: light, force: describes, status: drafted }
  forBeneficiary: { text: "You repeat course material at times but still show thought of your own.", rewrite: full, force: describes, status: drafted }
- sentence: cardiffmet/generic-2020/l5/knowledge/50-59.s4
  forPractitioner: { text: "A few errors or misconceptions, none in important areas.", rewrite: light, force: describes, status: drafted }
  forBeneficiary: { text: "You make a few mistakes, but none in important areas.", rewrite: full, force: describes, status: drafted }
- sentence: cardiffmet/generic-2020/l5/knowledge/40-49.s1
  forPractitioner: { text: "Basic knowledge and critical understanding of concepts and principles.", rewrite: light, force: describes, status: drafted }
  forBeneficiary: { text: "You know your field's concepts and principles at a basic level.", rewrite: full, force: describes, status: drafted }
- sentence: cardiffmet/generic-2020/l5/knowledge/40-49.s2
  forPractitioner: { text: "Some evidence of extending and applying that knowledge.", rewrite: light, force: describes, status: drafted }
  forBeneficiary: { text: "You take what you know further and apply it a little.", rewrite: full, force: describes, status: drafted }
- sentence: cardiffmet/generic-2020/l5/knowledge/40-49.s3
  forPractitioner: { text: "Often reproduces received material.", rewrite: light, force: describes, status: drafted }
  forBeneficiary: { text: "You often repeat what course materials say.", rewrite: full, force: describes, status: drafted }
- sentence: cardiffmet/generic-2020/l5/knowledge/40-49.s4
  forPractitioner: { text: "Errors and misconceptions present, outweighed by what is understood.", rewrite: light, force: describes, status: drafted }
  forBeneficiary: { text: "You make mistakes, but what you understand outweighs them.", rewrite: full, force: describes, status: drafted }
- sentence: cardiffmet/generic-2020/l5/knowledge/30-39.s1
  forPractitioner: { text: "Limited knowledge and critical understanding of concepts and principles.", rewrite: light, force: describes, status: drafted }
  forBeneficiary: { text: "Your knowledge of your field's concepts and principles is limited.", rewrite: full, force: describes, status: drafted }
- sentence: cardiffmet/generic-2020/l5/knowledge/30-39.s2
  forPractitioner: { text: "Not enough evidence of extending or applying knowledge.", rewrite: light, force: describes, status: drafted }
  forBeneficiary: { text: "You do not yet take your knowledge further or apply it enough.", rewrite: full, force: describes, status: drafted }
- sentence: cardiffmet/generic-2020/l5/knowledge/30-39.s3
  forPractitioner: { text: "Inaccuracies and misconceptions in important areas; parts may be off the task.", rewrite: light, force: describes, status: drafted }
  forBeneficiary: { text: "You make mistakes in important areas, and parts of your work may be off the task.", rewrite: full, force: describes, status: drafted }
- sentence: cardiffmet/generic-2020/l5/knowledge/1-29.s1
  forPractitioner: { text: "Little knowledge or critical understanding of concepts and principles.", rewrite: light, force: describes, status: drafted }
  forBeneficiary: { text: "You show little knowledge of your field's concepts and principles.", rewrite: full, force: describes, status: drafted }
- sentence: cardiffmet/generic-2020/l5/knowledge/1-29.s2
  forPractitioner: { text: "Little evidence of extending or applying knowledge.", rewrite: light, force: describes, status: drafted }
  forBeneficiary: { text: "You hardly take your knowledge further or apply it.", rewrite: full, force: describes, status: drafted }
- sentence: cardiffmet/generic-2020/l5/knowledge/1-29.s3
  forPractitioner: { text: "Errors in many important areas outweigh what is understood.", rewrite: light, force: describes, status: drafted }
  forBeneficiary: { text: "Your mistakes in many important areas outweigh what you understand.", rewrite: full, force: describes, status: drafted }
- sentence: cardiffmet/generic-2020/l5/knowledge/1-29.s4
  forPractitioner: { text: "Much of the work may be off the task.", rewrite: light, force: describes, status: drafted }
  forBeneficiary: { text: "Much of your work may be off the task.", rewrite: full, force: describes, status: drafted }
- sentence: cardiffmet/generic-2020/l5/presentation/80-100.s1
  forPractitioner: { text: "The top band goes further than 70-79, past what this level expects.", rewrite: light, force: describes, status: drafted }
  forBeneficiary: { text: "At the top, your work goes further than first-class work and past what this level expects.", rewrite: full, force: describes, status: drafted }
- sentence: cardiffmet/generic-2020/l5/presentation/70-79.s1
  forPractitioner: { text: "Communicates information, argument and analysis coherently and concisely in many situations.", rewrite: light, force: describes, status: drafted }
  forBeneficiary: { text: "You communicate information, argument and analysis coherently and concisely in many settings.", rewrite: full, force: describes, status: drafted }
- sentence: cardiffmet/generic-2020/l5/presentation/70-79.s2
  forPractitioner: { text: "High standard of presentation; format fits.", rewrite: light, force: describes, status: drafted }
  forBeneficiary: { text: "Your work is presented to a high standard in a suitable format.", rewrite: full, force: describes, status: drafted }
- sentence: cardiffmet/generic-2020/l5/presentation/70-79.s3
  forPractitioner: { text: "Points logically organised; lucid, mature style in writing.", rewrite: light, force: describes, status: drafted }
  forBeneficiary: { text: "Your points are logically ordered and your writing is lucid and mature.", rewrite: full, force: describes, status: drafted }
- sentence: cardiffmet/generic-2020/l5/presentation/70-79.s4
  forPractitioner: { text: "Arguments well defined, clearly put, structured and coherent.", rewrite: light, force: describes, status: drafted }
  forBeneficiary: { text: "Your arguments are well defined, clear, structured and coherent.", rewrite: full, force: describes, status: drafted }
- sentence: cardiffmet/generic-2020/l5/presentation/60-69.s1
  forPractitioner: { text: "Communicates information, argument and analysis coherently and concisely in many situations.", rewrite: light, force: describes, status: drafted }
  forBeneficiary: { text: "You communicate information, argument and analysis coherently and concisely in many settings.", rewrite: full, force: describes, status: drafted }
- sentence: cardiffmet/generic-2020/l5/presentation/60-69.s2
  forPractitioner: { text: "Well presented; format fits.", rewrite: light, force: describes, status: drafted }
  forBeneficiary: { text: "Your work is well presented in a suitable format.", rewrite: full, force: describes, status: drafted }
- sentence: cardiffmet/generic-2020/l5/presentation/60-69.s3
  forPractitioner: { text: "Points organised; fluent style; arguments well put, structured and coherent.", rewrite: light, force: describes, status: drafted }
  forBeneficiary: { text: "Your points are organised, your writing fluent and your arguments structured and coherent.", rewrite: full, force: describes, status: drafted }
- sentence: cardiffmet/generic-2020/l5/presentation/50-59.s1
  forPractitioner: { text: "Satisfactory coherent, concise communication across situations.", rewrite: light, force: describes, status: drafted }
  forBeneficiary: { text: "You communicate coherently and concisely to a satisfactory standard.", rewrite: full, force: describes, status: drafted }
- sentence: cardiffmet/generic-2020/l5/presentation/50-59.s2
  forPractitioner: { text: "Structure and format appropriate overall.", rewrite: light, force: describes, status: drafted }
  forBeneficiary: { text: "Your work is suitably structured and formatted overall.", rewrite: full, force: describes, status: drafted }
- sentence: cardiffmet/generic-2020/l5/presentation/50-59.s3
  forPractitioner: { text: "Occasional faults in presentation.", rewrite: light, force: describes, status: drafted }
  forBeneficiary: { text: "You make occasional slips in presentation.", rewrite: full, force: describes, status: drafted }
- sentence: cardiffmet/generic-2020/l5/presentation/50-59.s4
  forPractitioner: { text: "The faults do not cloud meaning.", rewrite: light, force: describes, status: drafted }
  forBeneficiary: { text: "Your slips do not cloud your meaning.", rewrite: full, force: describes, status: drafted }
- sentence: cardiffmet/generic-2020/l5/presentation/40-49.s1
  forPractitioner: { text: "Basic coherent, concise communication across situations.", rewrite: light, force: describes, status: drafted }
  forBeneficiary: { text: "You communicate coherently and concisely at a basic level.", rewrite: full, force: describes, status: drafted }
- sentence: cardiffmet/generic-2020/l5/presentation/40-49.s2
  forPractitioner: { text: "Better at reporting facts than conveying complex ideas.", rewrite: light, force: describes, status: drafted }
  forBeneficiary: { text: "You report facts better than you explain complex ideas.", rewrite: full, force: describes, status: drafted }
- sentence: cardiffmet/generic-2020/l5/presentation/40-49.s3
  forPractitioner: { text: "Mostly structured, though points may be out of order.", rewrite: light, force: describes, status: drafted }
  forBeneficiary: { text: "Your work is mostly structured, though some points may be out of order.", rewrite: full, force: describes, status: drafted }
- sentence: cardiffmet/generic-2020/l5/presentation/40-49.s4
  forPractitioner: { text: "Faults in presentation, but meaning clear.", rewrite: light, force: describes, status: drafted }
  forBeneficiary: { text: "There are faults in your presentation, but your meaning is clear.", rewrite: full, force: describes, status: drafted }
- sentence: cardiffmet/generic-2020/l5/presentation/30-39.s1
  forPractitioner: { text: "Limited communication of basic concepts, arguments and analysis.", rewrite: light, force: describes, status: drafted }
  forBeneficiary: { text: "You communicate basic ideas and arguments only a little.", rewrite: full, force: describes, status: drafted }
- sentence: cardiffmet/generic-2020/l5/presentation/30-39.s2
  forPractitioner: { text: "Arguments and complex ideas, if tried, may be confused and clumsy.", rewrite: light, force: describes, status: drafted }
  forBeneficiary: { text: "Any arguments or complex ideas you try may come out confused.", rewrite: full, force: describes, status: drafted }
- sentence: cardiffmet/generic-2020/l5/presentation/1-29.s1
  forPractitioner: { text: "Little communication of basic concepts, arguments and analysis.", rewrite: light, force: describes, status: drafted }
  forBeneficiary: { text: "You communicate basic ideas and arguments very little.", rewrite: full, force: describes, status: drafted }
- sentence: cardiffmet/generic-2020/l5/presentation/1-29.s2
  forPractitioner: { text: "Frequent faults and weak structure obscure meaning.", rewrite: light, force: describes, status: drafted }
  forBeneficiary: { text: "Frequent faults and weak structure hide your meaning.", rewrite: full, force: describes, status: drafted }
- sentence: cardiffmet/generic-2020/l5/presentation/1-29.s3
  forPractitioner: { text: "Writing often clumsy and unsuitable.", rewrite: light, force: describes, status: drafted }
  forBeneficiary: { text: "Your writing is often clumsy and unsuitable.", rewrite: full, force: describes, status: drafted }
- sentence: cardiffmet/generic-2020/l5/analysis/80-100.s1
  forPractitioner: { text: "Designs and carries out own research or advanced scholarship with fitting techniques.", rewrite: light, force: describes, status: drafted }
  forBeneficiary: { text: "At the top, you design and carry out your own research with suitable methods.", rewrite: full, force: describes, status: drafted }
- sentence: cardiffmet/generic-2020/l5/analysis/80-100.s2
  forPractitioner: { text: "The top band goes further than 70-79, past what this level expects.", rewrite: light, force: describes, status: drafted }
  forBeneficiary: { text: "At the top, your work goes further than first-class work and past what this level expects.", rewrite: full, force: describes, status: drafted }
- sentence: cardiffmet/generic-2020/l5/analysis/70-79.s1
  forPractitioner: { text: "Analyses qualitative and quantitative data with very good use of established techniques.", rewrite: light, force: describes, status: drafted }
  forBeneficiary: { text: "You analyse numbers and other data very well with standard techniques.", rewrite: full, force: describes, status: drafted }
- sentence: cardiffmet/generic-2020/l5/analysis/70-79.s2
  forPractitioner: { text: "Presents, synthesises and comments very successfully; perceptive on theory, practice and how the limits of own knowledge affect findings.", rewrite: light, force: describes, status: drafted }
  forBeneficiary: { text: "You bring your results together very successfully and comment perceptively on theory, practice and how the limits of what you know affect your findings.", rewrite: full, force: describes, status: drafted }
- sentence: cardiffmet/generic-2020/l5/analysis/60-69.s1
  forPractitioner: { text: "Analyses data with good use of established techniques.", rewrite: light, force: describes, status: drafted }
  forBeneficiary: { text: "You analyse data well with standard techniques.", rewrite: full, force: describes, status: drafted }
- sentence: cardiffmet/generic-2020/l5/analysis/60-69.s2
  forPractitioner: { text: "Presents, synthesises and comments with considerable success; perceptive on theory, practice and own limits.", rewrite: light, force: describes, status: drafted }
  forBeneficiary: { text: "You bring your results together with considerable success and comment perceptively on theory, practice and your limits.", rewrite: full, force: describes, status: drafted }
- sentence: cardiffmet/generic-2020/l5/analysis/50-59.s1
  forPractitioner: { text: "Analyses data with a range of established techniques; generally succeeds with results.", rewrite: light, force: describes, status: drafted }
  forBeneficiary: { text: "You analyse data with standard techniques and generally present your results well.", rewrite: full, force: describes, status: drafted }
- sentence: cardiffmet/generic-2020/l5/analysis/50-59.s2
  forPractitioner: { text: "Aware of the limits of own knowledge and their effect.", rewrite: light, force: describes, status: drafted }
  forBeneficiary: { text: "You see the limits of what you know and how they affect your work.", rewrite: full, force: describes, status: drafted }
- sentence: cardiffmet/generic-2020/l5/analysis/40-49.s1
  forPractitioner: { text: "Analyses data with basic use of established techniques; intermittent success with results.", rewrite: light, force: describes, status: drafted }
  forBeneficiary: { text: "You analyse data with basic use of standard techniques and present results with mixed success.", rewrite: full, force: describes, status: drafted }
- sentence: cardiffmet/generic-2020/l5/analysis/40-49.s2
  forPractitioner: { text: "Some awareness of the limits of own knowledge.", rewrite: light, force: describes, status: drafted }
  forBeneficiary: { text: "You see some of the limits of what you know.", rewrite: full, force: describes, status: drafted }
- sentence: cardiffmet/generic-2020/l5/analysis/30-39.s1
  forPractitioner: { text: "Attempts data analysis, but results may be naive, simplistic or unconvincing.", rewrite: light, force: describes, status: drafted }
  forBeneficiary: { text: "You attempt data analysis, but your results may be simplistic or unconvincing.", rewrite: full, force: describes, status: drafted }
- sentence: cardiffmet/generic-2020/l5/analysis/1-29.s1
  forPractitioner: { text: "Little evidence of data analysis.", rewrite: light, force: describes, status: drafted }
  forBeneficiary: { text: "You show little data analysis.", rewrite: full, force: describes, status: drafted }
- sentence: cardiffmet/generic-2020/l5/analysis/1-29.s2
  forPractitioner: { text: "Results, where attempted, unsuitable or missing.", rewrite: light, force: describes, status: drafted }
  forBeneficiary: { text: "Where you try, your results are unsuitable or missing.", rewrite: full, force: describes, status: drafted }
- sentence: cardiffmet/generic-2020/l5/research/80-100.s1
  forPractitioner: { text: "In coursework, citations range well beyond the reading the field normally expects.", rewrite: light, force: describes, status: drafted }
  forBeneficiary: { text: "At the top, your coursework cites well beyond the usual reading.", rewrite: full, force: describes, status: drafted }
- sentence: cardiffmet/generic-2020/l5/research/80-100.s2
  forPractitioner: { text: "In examinations, a substantial range of citations.", rewrite: light, force: describes, status: drafted }
  forBeneficiary: { text: "In exams, you cite widely.", rewrite: full, force: describes, status: drafted }
- sentence: cardiffmet/generic-2020/l5/research/80-100.s3
  forPractitioner: { text: "The top band goes further than 70-79, past what this level expects.", rewrite: light, force: describes, status: drafted }
  forBeneficiary: { text: "At the top, your work goes further than first-class work and past what this level expects.", rewrite: full, force: describes, status: drafted }
- sentence: cardiffmet/generic-2020/l5/research/70-79.s1
  forPractitioner: { text: "Detailed, thorough knowledge of current research.", rewrite: light, force: describes, status: drafted }
  forBeneficiary: { text: "You know current research thoroughly and in detail.", rewrite: full, force: describes, status: drafted }
- sentence: cardiffmet/generic-2020/l5/research/70-79.s2
  forPractitioner: { text: "Confident use of reviews and primary sources; broad, deep reading beyond the sources given.", rewrite: light, force: describes, status: drafted }
  forBeneficiary: { text: "You use reviews and primary sources confidently and read broadly and deeply past the sources given.", rewrite: full, force: describes, status: drafted }
- sentence: cardiffmet/generic-2020/l5/research/70-79.s3
  forPractitioner: { text: "Referencing accurate and conventional.", rewrite: light, force: describes, status: drafted }
  forBeneficiary: { text: "Your referencing is accurate and follows academic conventions.", rewrite: full, force: describes, status: drafted }
- sentence: cardiffmet/generic-2020/l5/research/70-79.s4
  forPractitioner: { text: "Understands research processes and methods and applies them successfully.", rewrite: light, force: describes, status: drafted }
  forBeneficiary: { text: "You understand research methods and use them successfully.", rewrite: full, force: describes, status: drafted }
- sentence: cardiffmet/generic-2020/l5/research/60-69.s1
  forPractitioner: { text: "Good knowledge of current research.", rewrite: light, force: describes, status: drafted }
  forBeneficiary: { text: "You know current research well.", rewrite: full, force: describes, status: drafted }
- sentence: cardiffmet/generic-2020/l5/research/60-69.s2
  forPractitioner: { text: "Reading broad and deep, beyond the sources given.", rewrite: light, force: describes, status: drafted }
  forBeneficiary: { text: "Your examples show broad, deep reading past the sources given.", rewrite: full, force: describes, status: drafted }
- sentence: cardiffmet/generic-2020/l5/research/60-69.s3
  forPractitioner: { text: "Referencing almost always accurate.", rewrite: light, force: describes, status: drafted }
  forBeneficiary: { text: "Your referencing is almost always accurate.", rewrite: full, force: describes, status: drafted }
- sentence: cardiffmet/generic-2020/l5/research/60-69.s4
  forPractitioner: { text: "Basic grasp of research processes, applied fittingly.", rewrite: light, force: describes, status: drafted }
  forBeneficiary: { text: "You know the basics of research methods and use them well.", rewrite: full, force: describes, status: drafted }
- sentence: cardiffmet/generic-2020/l5/research/50-59.s1
  forPractitioner: { text: "Satisfactory knowledge of current research and discussion of its implications.", rewrite: light, force: describes, status: drafted }
  forBeneficiary: { text: "You know current research satisfactorily and discuss what it means.", rewrite: full, force: describes, status: drafted }
- sentence: cardiffmet/generic-2020/l5/research/50-59.s2
  forPractitioner: { text: "Some independent reading and investigation shown.", rewrite: light, force: describes, status: drafted }
  forBeneficiary: { text: "Your examples show some reading and investigation of your own.", rewrite: full, force: describes, status: drafted }
- sentence: cardiffmet/generic-2020/l5/research/50-59.s3
  forPractitioner: { text: "Occasional referencing errors.", rewrite: light, force: describes, status: drafted }
  forBeneficiary: { text: "Your referencing has occasional slips.", rewrite: full, force: describes, status: drafted }
- sentence: cardiffmet/generic-2020/l5/research/50-59.s4
  forPractitioner: { text: "Some grasp of research processes, generally applied well, perhaps relying on tutor support.", rewrite: light, force: describes, status: drafted }
  forBeneficiary: { text: "You know something of research methods and use them well, perhaps with your tutor's help.", rewrite: full, force: describes, status: drafted }
- sentence: cardiffmet/generic-2020/l5/research/40-49.s1
  forPractitioner: { text: "Basic knowledge of current research, with limited comment on its implications.", rewrite: light, force: describes, status: drafted }
  forBeneficiary: { text: "You know current research at a basic level and comment a little on what it means.", rewrite: full, force: describes, status: drafted }
- sentence: cardiffmet/generic-2020/l5/research/40-49.s2
  forPractitioner: { text: "May over-rely on course materials rather than own reading.", rewrite: light, force: describes, status: drafted }
  forBeneficiary: { text: "You may rely on course materials more than on your own reading.", rewrite: full, force: describes, status: drafted }
- sentence: cardiffmet/generic-2020/l5/research/40-49.s3
  forPractitioner: { text: "Referencing errors.", rewrite: light, force: describes, status: drafted }
  forBeneficiary: { text: "Your referencing has errors.", rewrite: full, force: describes, status: drafted }
- sentence: cardiffmet/generic-2020/l5/research/40-49.s4
  forPractitioner: { text: "Some grasp of research processes, applied less securely.", rewrite: light, force: describes, status: drafted }
  forBeneficiary: { text: "You know something of research methods but use them unsteadily.", rewrite: full, force: describes, status: drafted }
- sentence: cardiffmet/generic-2020/l5/research/30-39.s1
  forPractitioner: { text: "Limited or patchy knowledge of current research.", rewrite: light, force: describes, status: drafted }
  forBeneficiary: { text: "Your knowledge of current research is limited or patchy.", rewrite: full, force: describes, status: drafted }
- sentence: cardiffmet/generic-2020/l5/research/30-39.s2
  forPractitioner: { text: "Narrow sources; over-reliance on course materials; little own reading.", rewrite: light, force: describes, status: drafted }
  forBeneficiary: { text: "You use a narrow set of sources, rely on course materials and read little for yourself.", rewrite: full, force: describes, status: drafted }
- sentence: cardiffmet/generic-2020/l5/research/30-39.s3
  forPractitioner: { text: "Frequent referencing errors.", rewrite: light, force: describes, status: drafted }
  forBeneficiary: { text: "Your referencing has frequent errors.", rewrite: full, force: describes, status: drafted }
- sentence: cardiffmet/generic-2020/l5/research/30-39.s4
  forPractitioner: { text: "Research knowledge, where present, applied largely without success.", rewrite: light, force: describes, status: drafted }
  forBeneficiary: { text: "Where you know research methods, you mostly fail to apply them.", rewrite: full, force: describes, status: drafted }
- sentence: cardiffmet/generic-2020/l5/research/1-29.s1
  forPractitioner: { text: "Little knowledge of current research.", rewrite: light, force: describes, status: drafted }
  forBeneficiary: { text: "You show little knowledge of current research.", rewrite: full, force: describes, status: drafted }
- sentence: cardiffmet/generic-2020/l5/research/1-29.s2
  forPractitioner: { text: "Negligible own reading; scant referencing, often wrong.", rewrite: light, force: describes, status: drafted }
  forBeneficiary: { text: "You do almost no reading of your own, and your few references are often wrong.", rewrite: full, force: describes, status: drafted }
- sentence: cardiffmet/generic-2020/l5/research/1-29.s3
  forPractitioner: { text: "Very limited grasp of research processes, not applied.", rewrite: light, force: describes, status: drafted }
  forBeneficiary: { text: "You know very little about research methods and do not apply them.", rewrite: full, force: describes, status: drafted }
- sentence: cardiffmet/generic-2020/l5/argument/80-100.s1
  forPractitioner: { text: "Offers important insights informed by critical evaluation of current research or practice.", rewrite: light, force: describes, status: drafted }
  forBeneficiary: { text: "At the top, you offer important insights drawn from critical evaluation of current research or practice.", rewrite: full, force: describes, status: drafted }
- sentence: cardiffmet/generic-2020/l5/argument/80-100.s2
  forPractitioner: { text: "The top band goes further than 70-79, past what this level expects.", rewrite: light, force: describes, status: drafted }
  forBeneficiary: { text: "At the top, your work goes further than first-class work and past what this level expects.", rewrite: full, force: describes, status: drafted }
- sentence: cardiffmet/generic-2020/l5/argument/70-79.s1
  forPractitioner: { text: "Solves broadly defined, complex problems with critical understanding of the field's principles.", rewrite: light, force: describes, status: drafted }
  forBeneficiary: { text: "You solve broad, complex problems with critical understanding of your field's principles.", rewrite: full, force: describes, status: drafted }
- sentence: cardiffmet/generic-2020/l5/argument/70-79.s2
  forPractitioner: { text: "Arguments developed, sustained and supported.", rewrite: light, force: describes, status: drafted }
  forBeneficiary: { text: "Your arguments are developed, sustained and supported.", rewrite: full, force: describes, status: drafted }
- sentence: cardiffmet/generic-2020/l5/argument/70-79.s3
  forPractitioner: { text: "Challenges assumptions where relevant; clearly sees the complexity of academic debate.", rewrite: light, force: describes, status: drafted }
  forBeneficiary: { text: "You question assumptions where it matters and see clearly how complex academic debate is.", rewrite: full, force: describes, status: drafted }
- sentence: cardiffmet/generic-2020/l5/argument/70-79.s4
  forPractitioner: { text: "Offers fitting, sometimes innovative solutions, weighing different approaches.", rewrite: light, force: describes, status: drafted }
  forBeneficiary: { text: "You offer suitable and sometimes inventive solutions, weighing different approaches.", rewrite: full, force: describes, status: drafted }
- sentence: cardiffmet/generic-2020/l5/argument/70-79.s5
  forPractitioner: { text: "Strong evidence of reflecting effectively on own practice.", rewrite: light, force: describes, status: drafted }
  forBeneficiary: { text: "You reflect well on your own practice.", rewrite: full, force: describes, status: drafted }
- sentence: cardiffmet/generic-2020/l5/argument/70-79.s6
  forPractitioner: { text: "Highly perceptive evaluation of own work or practice; fully aware of what it means for development.", rewrite: light, force: describes, status: drafted }
  forBeneficiary: { text: "You evaluate your own work with sharp insight and see clearly what it means for how you develop.", rewrite: full, force: describes, status: drafted }
- sentence: cardiffmet/generic-2020/l5/argument/60-69.s1
  forPractitioner: { text: "Solves broadly defined, complex problems with critical understanding of the field's principles.", rewrite: light, force: describes, status: drafted }
  forBeneficiary: { text: "You solve broad, complex problems with critical understanding of your field's principles.", rewrite: full, force: describes, status: drafted }
- sentence: cardiffmet/generic-2020/l5/argument/60-69.s2
  forPractitioner: { text: "Arguments considered and supported; judges fittingly and suggests solutions, weighing approaches.", rewrite: light, force: describes, status: drafted }
  forBeneficiary: { text: "Your arguments are considered and supported, and you judge well and suggest solutions, weighing approaches.", rewrite: full, force: describes, status: drafted }
- sentence: cardiffmet/generic-2020/l5/argument/60-69.s3
  forPractitioner: { text: "Reflects on own practice and uses self-evaluation to plan development.", rewrite: light, force: describes, status: drafted }
  forBeneficiary: { text: "You reflect on your practice and use what you find to plan how to develop.", rewrite: full, force: describes, status: drafted }
- sentence: cardiffmet/generic-2020/l5/argument/50-59.s1
  forPractitioner: { text: "Satisfactory problem-solving and critical understanding, with some leaning on description.", rewrite: light, force: describes, status: drafted }
  forBeneficiary: { text: "You solve complex problems and think critically to a satisfactory standard, though you lean on description.", rewrite: full, force: describes, status: drafted }
- sentence: cardiffmet/generic-2020/l5/argument/50-59.s2
  forPractitioner: { text: "Arguments usually supported.", rewrite: light, force: describes, status: drafted }
  forBeneficiary: { text: "Your arguments are usually supported.", rewrite: full, force: describes, status: drafted }
- sentence: cardiffmet/generic-2020/l5/argument/50-59.s3
  forPractitioner: { text: "Some reflection on own practice, lacking insight into future development.", rewrite: light, force: describes, status: drafted }
  forBeneficiary: { text: "You reflect on your own practice, but without much insight into how to develop.", rewrite: full, force: describes, status: drafted }
- sentence: cardiffmet/generic-2020/l5/argument/40-49.s1
  forPractitioner: { text: "Basic problem-solving and critical understanding.", rewrite: light, force: describes, status: drafted }
  forBeneficiary: { text: "You solve complex problems and think critically at a basic level.", rewrite: full, force: describes, status: drafted }
- sentence: cardiffmet/generic-2020/l5/argument/40-49.s2
  forPractitioner: { text: "Some critical reflection, but mostly description and fact.", rewrite: light, force: describes, status: drafted }
  forBeneficiary: { text: "You reflect critically a little, but your work is mostly description.", rewrite: full, force: describes, status: drafted }
- sentence: cardiffmet/generic-2020/l5/argument/40-49.s3
  forPractitioner: { text: "Arguments generally supported but thin.", rewrite: light, force: describes, status: drafted }
  forBeneficiary: { text: "Your arguments are generally supported but thin.", rewrite: full, force: describes, status: drafted }
- sentence: cardiffmet/generic-2020/l5/argument/40-49.s4
  forPractitioner: { text: "Some reflection on own practice, limited and superficial, with little thought for development.", rewrite: light, force: describes, status: drafted }
  forBeneficiary: { text: "You reflect on your practice, but only briefly and on the surface.", rewrite: full, force: describes, status: drafted }
- sentence: cardiffmet/generic-2020/l5/argument/30-39.s1
  forPractitioner: { text: "Little sign of complex problem-solving or critical understanding.", rewrite: light, force: describes, status: drafted }
  forBeneficiary: { text: "You show little problem-solving or critical thinking.", rewrite: full, force: describes, status: drafted }
- sentence: cardiffmet/generic-2020/l5/argument/30-39.s2
  forPractitioner: { text: "Largely descriptive; arguments, if tried, rarely supported.", rewrite: light, force: describes, status: drafted }
  forBeneficiary: { text: "Your work is largely descriptive, and any arguments are rarely supported.", rewrite: full, force: describes, status: drafted }
- sentence: cardiffmet/generic-2020/l5/argument/30-39.s3
  forPractitioner: { text: "Self-evaluation very limited.", rewrite: light, force: describes, status: drafted }
  forBeneficiary: { text: "You reflect on your own practice very little.", rewrite: full, force: describes, status: drafted }
- sentence: cardiffmet/generic-2020/l5/argument/1-29.s1
  forPractitioner: { text: "Some description and reporting, but very little sign of problem-solving or critical understanding.", rewrite: light, force: describes, status: drafted }
  forBeneficiary: { text: "You describe and report a little but show almost no problem-solving or critical thinking.", rewrite: full, force: describes, status: drafted }
- sentence: cardiffmet/generic-2020/l5/argument/1-29.s2
  forPractitioner: { text: "Self-evaluation negligible or absent.", rewrite: light, force: describes, status: drafted }
  forBeneficiary: { text: "You reflect on your own practice little or not at all.", rewrite: full, force: describes, status: drafted }
- sentence: cardiffmet/generic-2020/l6/overall/80-100.s1
  forPractitioner: { text: "Full, detailed grasp of the task; outcomes met and criteria addressed excellently (80-89) or outstandingly (90-100), past this level.", rewrite: light, force: describes, status: drafted }
  forBeneficiary: { text: "You understand the task fully and in detail and meet its outcomes excellently, or outstandingly above 90, past this level.", rewrite: full, force: describes, status: drafted }
- sentence: cardiffmet/generic-2020/l6/overall/80-100.s2
  forPractitioner: { text: "Work of a standard fit for publication, manufacture, exhibition or performance.", rewrite: light, force: describes, status: drafted }
  forBeneficiary: { text: "Your work is good enough to publish, make, exhibit or perform.", rewrite: full, force: describes, status: drafted }
- sentence: cardiffmet/generic-2020/l6/overall/70-79.s1
  forPractitioner: { text: "Full, detailed grasp of the task; outcomes met and criteria addressed very well.", rewrite: light, force: describes, status: drafted }
  forBeneficiary: { text: "You understand the task fully and in detail and meet its outcomes and criteria very well.", rewrite: full, force: describes, status: drafted }
- sentence: cardiffmet/generic-2020/l6/overall/60-69.s1
  forPractitioner: { text: "Full grasp of the task; outcomes met and criteria addressed well.", rewrite: light, force: describes, status: drafted }
  forBeneficiary: { text: "You understand the task fully and meet its outcomes and criteria well.", rewrite: full, force: describes, status: drafted }
- sentence: cardiffmet/generic-2020/l6/overall/50-59.s1
  forPractitioner: { text: "Secure grasp of the task; outcomes met and criteria addressed satisfactorily.", rewrite: light, force: describes, status: drafted }
  forBeneficiary: { text: "You understand the task securely and meet its outcomes and criteria satisfactorily.", rewrite: full, force: describes, status: drafted }
- sentence: cardiffmet/generic-2020/l6/overall/40-49.s1
  forPractitioner: { text: "Basic grasp of the task; outcomes met and criteria addressed at the threshold.", rewrite: light, force: describes, status: drafted }
  forBeneficiary: { text: "You understand the task at a basic level and meet its outcomes and criteria at the minimum standard.", rewrite: full, force: describes, status: drafted }
- sentence: cardiffmet/generic-2020/l6/overall/30-39.s1
  forPractitioner: { text: "Unsatisfactory overall.", rewrite: light, force: describes, status: drafted }
  forBeneficiary: { text: "Your work is not yet satisfactory overall.", rewrite: full, force: describes, status: drafted }
- sentence: cardiffmet/generic-2020/l6/overall/30-39.s2
  forPractitioner: { text: "Partial grasp of the task; some outcomes met at a basic level.", rewrite: light, force: describes, status: drafted }
  forBeneficiary: { text: "You understand the task in part and meet some outcomes at a basic level.", rewrite: full, force: describes, status: drafted }
- sentence: cardiffmet/generic-2020/l6/overall/30-39.s3
  forPractitioner: { text: "Uneven: some outcomes unmet, some criteria unaddressed.", rewrite: light, force: describes, status: drafted }
  forBeneficiary: { text: "Your work is uneven: some outcomes are not met and some criteria are not addressed.", rewrite: full, force: describes, status: drafted }
- sentence: cardiffmet/generic-2020/l6/overall/1-29.s1
  forPractitioner: { text: "Poor overall.", rewrite: light, force: describes, status: drafted }
  forBeneficiary: { text: "Your work is poor overall.", rewrite: full, force: describes, status: drafted }
- sentence: cardiffmet/generic-2020/l6/overall/1-29.s2
  forPractitioner: { text: "Minimal grasp of the task; one or two outcomes partly met.", rewrite: light, force: describes, status: drafted }
  forBeneficiary: { text: "You show little understanding of the task and meet one or two outcomes only in part.", rewrite: full, force: describes, status: drafted }
- sentence: cardiffmet/generic-2020/l6/overall/1-29.s3
  forPractitioner: { text: "Many criteria unaddressed.", rewrite: light, force: describes, status: drafted }
  forBeneficiary: { text: "You leave many of the criteria unaddressed.", rewrite: full, force: describes, status: drafted }
- sentence: cardiffmet/generic-2020/l6/knowledge/80-100.s1
  forPractitioner: { text: "The top band goes further than 70-79, past what this level expects.", rewrite: light, force: describes, status: drafted }
  forBeneficiary: { text: "At the top, your work goes further than first-class work and past what this level expects.", rewrite: full, force: describes, status: drafted }
- sentence: cardiffmet/generic-2020/l6/knowledge/80-100.s2
  forPractitioner: { text: "Exceptional knowledge and systematic understanding.", rewrite: light, force: describes, status: drafted }
  forBeneficiary: { text: "Your knowledge is exceptional and your understanding systematic.", rewrite: full, force: describes, status: drafted }
- sentence: cardiffmet/generic-2020/l6/knowledge/70-79.s1
  forPractitioner: { text: "Knows the key aspects of the field in detail and understands them systematically.", rewrite: light, force: describes, status: drafted }
  forBeneficiary: { text: "You know the key parts of your field in detail and understand them systematically.", rewrite: full, force: describes, status: drafted }
- sentence: cardiffmet/generic-2020/l6/knowledge/70-79.s2
  forPractitioner: { text: "Strong evidence of extending, transforming and applying that knowledge.", rewrite: light, force: describes, status: drafted }
  forBeneficiary: { text: "You take what you know further, reshape it and apply it strongly.", rewrite: full, force: describes, status: drafted }
- sentence: cardiffmet/generic-2020/l6/knowledge/70-79.s3
  forPractitioner: { text: "Confident discussion of complex concepts; recognises the limits and ambiguity of knowledge.", rewrite: light, force: describes, status: drafted }
  forBeneficiary: { text: "You discuss complex ideas confidently and see where knowledge is limited or unclear.", rewrite: full, force: describes, status: drafted }
- sentence: cardiffmet/generic-2020/l6/knowledge/70-79.s4
  forPractitioner: { text: "Independent thinking, original insight and self-managed learning are features.", rewrite: light, force: describes, status: drafted }
  forBeneficiary: { text: "You think for yourself, offer original insight and manage your own learning.", rewrite: full, force: describes, status: drafted }
- sentence: cardiffmet/generic-2020/l6/knowledge/60-69.s1
  forPractitioner: { text: "Knows the key aspects of the field in detail and understands them thoroughly.", rewrite: light, force: describes, status: drafted }
  forBeneficiary: { text: "You know the key parts of your field in detail and understand them thoroughly.", rewrite: full, force: describes, status: drafted }
- sentence: cardiffmet/generic-2020/l6/knowledge/60-69.s2
  forPractitioner: { text: "Clear evidence of applying knowledge and, in places, extending and transforming it.", rewrite: light, force: describes, status: drafted }
  forBeneficiary: { text: "You apply what you know clearly and sometimes take it further.", rewrite: full, force: describes, status: drafted }
- sentence: cardiffmet/generic-2020/l6/knowledge/60-69.s3
  forPractitioner: { text: "Complex concepts often discussed well; independent thinking; self-managed learning.", rewrite: light, force: describes, status: drafted }
  forBeneficiary: { text: "You often discuss complex ideas well, think for yourself and manage your own learning.", rewrite: full, force: describes, status: drafted }
- sentence: cardiffmet/generic-2020/l6/knowledge/50-59.s1
  forPractitioner: { text: "Sound knowledge of most key aspects, with some application.", rewrite: light, force: describes, status: drafted }
  forBeneficiary: { text: "You know most key parts of your field soundly and apply them a little.", rewrite: full, force: describes, status: drafted }
- sentence: cardiffmet/generic-2020/l6/knowledge/50-59.s2
  forPractitioner: { text: "Some reproduction of received material, but still some independent thought.", rewrite: light, force: describes, status: drafted }
  forBeneficiary: { text: "You repeat course material at times but still show thought of your own.", rewrite: full, force: describes, status: drafted }
- sentence: cardiffmet/generic-2020/l6/knowledge/50-59.s3
  forPractitioner: { text: "A few errors or misconceptions, none in important areas.", rewrite: light, force: describes, status: drafted }
  forBeneficiary: { text: "You make a few mistakes, but none in important areas.", rewrite: full, force: describes, status: drafted }
- sentence: cardiffmet/generic-2020/l6/knowledge/50-59.s4
  forPractitioner: { text: "Some self-management of learning.", rewrite: light, force: describes, status: drafted }
  forBeneficiary: { text: "You show you can manage your own learning.", rewrite: full, force: describes, status: drafted }
- sentence: cardiffmet/generic-2020/l6/knowledge/40-49.s1
  forPractitioner: { text: "Basic knowledge of many aspects of the field.", rewrite: light, force: describes, status: drafted }
  forBeneficiary: { text: "You know many parts of your field at a basic level.", rewrite: full, force: describes, status: drafted }
- sentence: cardiffmet/generic-2020/l6/knowledge/40-49.s2
  forPractitioner: { text: "Often reproduces received material.", rewrite: light, force: describes, status: drafted }
  forBeneficiary: { text: "You often repeat what course materials say.", rewrite: full, force: describes, status: drafted }
- sentence: cardiffmet/generic-2020/l6/knowledge/40-49.s3
  forPractitioner: { text: "Errors and misconceptions present, outweighed by what is understood.", rewrite: light, force: describes, status: drafted }
  forBeneficiary: { text: "You make mistakes, but what you understand outweighs them.", rewrite: full, force: describes, status: drafted }
- sentence: cardiffmet/generic-2020/l6/knowledge/40-49.s4
  forPractitioner: { text: "Some self-management of learning.", rewrite: light, force: describes, status: drafted }
  forBeneficiary: { text: "You show you can manage your own learning.", rewrite: full, force: describes, status: drafted }
- sentence: cardiffmet/generic-2020/l6/knowledge/30-39.s1
  forPractitioner: { text: "Limited knowledge of the relevant field.", rewrite: light, force: describes, status: drafted }
  forBeneficiary: { text: "Your knowledge of the field is limited.", rewrite: full, force: describes, status: drafted }
- sentence: cardiffmet/generic-2020/l6/knowledge/30-39.s2
  forPractitioner: { text: "Inaccuracies and misconceptions in important areas; parts may be off the task.", rewrite: light, force: describes, status: drafted }
  forBeneficiary: { text: "You make mistakes in important areas, and parts of your work may be off the task.", rewrite: full, force: describes, status: drafted }
- sentence: cardiffmet/generic-2020/l6/knowledge/1-29.s1
  forPractitioner: { text: "Little knowledge of the relevant field.", rewrite: light, force: describes, status: drafted }
  forBeneficiary: { text: "You show little knowledge of the field.", rewrite: full, force: describes, status: drafted }
- sentence: cardiffmet/generic-2020/l6/knowledge/1-29.s2
  forPractitioner: { text: "Errors in many important areas outweigh what is understood.", rewrite: light, force: describes, status: drafted }
  forBeneficiary: { text: "Your mistakes in many important areas outweigh what you understand.", rewrite: full, force: describes, status: drafted }
- sentence: cardiffmet/generic-2020/l6/knowledge/1-29.s3
  forPractitioner: { text: "Much of the work may be off the task.", rewrite: light, force: describes, status: drafted }
  forBeneficiary: { text: "Much of your work may be off the task.", rewrite: full, force: describes, status: drafted }
- sentence: cardiffmet/generic-2020/l6/presentation/80-100.s1
  forPractitioner: { text: "The top band goes further than 70-79, past what this level expects.", rewrite: light, force: describes, status: drafted }
  forBeneficiary: { text: "At the top, your work goes further than first-class work and past what this level expects.", rewrite: full, force: describes, status: drafted }
- sentence: cardiffmet/generic-2020/l6/presentation/80-100.s2
  forPractitioner: { text: "Presentation reaches the discipline's professional standard.", rewrite: light, force: describes, status: drafted }
  forBeneficiary: { text: "Your presentation meets the professional standard of your field.", rewrite: full, force: describes, status: drafted }
- sentence: cardiffmet/generic-2020/l6/presentation/70-79.s1
  forPractitioner: { text: "Communicates information and complex ideas coherently and concisely in many situations.", rewrite: light, force: describes, status: drafted }
  forBeneficiary: { text: "You communicate complex ideas coherently and concisely in many settings.", rewrite: full, force: describes, status: drafted }
- sentence: cardiffmet/generic-2020/l6/presentation/70-79.s2
  forPractitioner: { text: "High standard of presentation; format fits.", rewrite: light, force: describes, status: drafted }
  forBeneficiary: { text: "Your work is presented to a high standard in a suitable format.", rewrite: full, force: describes, status: drafted }
- sentence: cardiffmet/generic-2020/l6/presentation/70-79.s3
  forPractitioner: { text: "Points logically organised; lucid, mature style in writing.", rewrite: light, force: describes, status: drafted }
  forBeneficiary: { text: "Your points are logically ordered and your writing is lucid and mature.", rewrite: full, force: describes, status: drafted }
- sentence: cardiffmet/generic-2020/l6/presentation/70-79.s4
  forPractitioner: { text: "Arguments well defined and clearly put.", rewrite: light, force: describes, status: drafted }
  forBeneficiary: { text: "Your arguments are well defined and clearly put.", rewrite: full, force: describes, status: drafted }
- sentence: cardiffmet/generic-2020/l6/presentation/60-69.s1
  forPractitioner: { text: "Communicates information and ideas clearly and concisely in many situations.", rewrite: light, force: describes, status: drafted }
  forBeneficiary: { text: "You communicate ideas clearly and concisely in many settings.", rewrite: full, force: describes, status: drafted }
- sentence: cardiffmet/generic-2020/l6/presentation/60-69.s2
  forPractitioner: { text: "Well presented; format fits.", rewrite: light, force: describes, status: drafted }
  forBeneficiary: { text: "Your work is well presented in a suitable format.", rewrite: full, force: describes, status: drafted }
- sentence: cardiffmet/generic-2020/l6/presentation/60-69.s3
  forPractitioner: { text: "Points organised; fluent style; arguments well put.", rewrite: light, force: describes, status: drafted }
  forBeneficiary: { text: "Your points are organised, your writing fluent and your arguments well put.", rewrite: full, force: describes, status: drafted }
- sentence: cardiffmet/generic-2020/l6/presentation/50-59.s1
  forPractitioner: { text: "Satisfactory communication of information, ideas and arguments in many situations.", rewrite: light, force: describes, status: drafted }
  forBeneficiary: { text: "You communicate ideas and arguments to a satisfactory standard in many settings.", rewrite: full, force: describes, status: drafted }
- sentence: cardiffmet/generic-2020/l6/presentation/50-59.s2
  forPractitioner: { text: "Structure and format appropriate overall.", rewrite: light, force: describes, status: drafted }
  forBeneficiary: { text: "Your work is suitably structured and formatted overall.", rewrite: full, force: describes, status: drafted }
- sentence: cardiffmet/generic-2020/l6/presentation/50-59.s3
  forPractitioner: { text: "Occasional faults that do not cloud meaning.", rewrite: light, force: describes, status: drafted }
  forBeneficiary: { text: "You make occasional slips that do not cloud your meaning.", rewrite: full, force: describes, status: drafted }
- sentence: cardiffmet/generic-2020/l6/presentation/40-49.s1
  forPractitioner: { text: "Some communication of information, ideas and arguments across situations.", rewrite: light, force: describes, status: drafted }
  forBeneficiary: { text: "You communicate ideas and arguments to some extent.", rewrite: full, force: describes, status: drafted }
- sentence: cardiffmet/generic-2020/l6/presentation/40-49.s2
  forPractitioner: { text: "Better at reporting facts than conveying complex ideas.", rewrite: light, force: describes, status: drafted }
  forBeneficiary: { text: "You report facts better than you explain complex ideas.", rewrite: full, force: describes, status: drafted }
- sentence: cardiffmet/generic-2020/l6/presentation/40-49.s3
  forPractitioner: { text: "Mostly structured, though points may be out of order.", rewrite: light, force: describes, status: drafted }
  forBeneficiary: { text: "Your work is mostly structured, though some points may be out of order.", rewrite: full, force: describes, status: drafted }
- sentence: cardiffmet/generic-2020/l6/presentation/40-49.s4
  forPractitioner: { text: "Faults in presentation, but meaning clear.", rewrite: light, force: describes, status: drafted }
  forBeneficiary: { text: "There are faults in your presentation, but your meaning is clear.", rewrite: full, force: describes, status: drafted }
- sentence: cardiffmet/generic-2020/l6/presentation/30-39.s1
  forPractitioner: { text: "Limited communication of simple concepts or facts.", rewrite: light, force: describes, status: drafted }
  forBeneficiary: { text: "You communicate simple ideas or facts only a little.", rewrite: full, force: describes, status: drafted }
- sentence: cardiffmet/generic-2020/l6/presentation/30-39.s2
  forPractitioner: { text: "Faults in presentation and structure mar clarity.", rewrite: light, force: describes, status: drafted }
  forBeneficiary: { text: "Faults in your presentation and structure cloud your meaning.", rewrite: full, force: describes, status: drafted }
- sentence: cardiffmet/generic-2020/l6/presentation/30-39.s3
  forPractitioner: { text: "Arguments and complex ideas, if tried, may be confused and clumsy.", rewrite: light, force: describes, status: drafted }
  forBeneficiary: { text: "Any arguments or complex ideas you try may come out confused.", rewrite: full, force: describes, status: drafted }
- sentence: cardiffmet/generic-2020/l6/presentation/1-29.s1
  forPractitioner: { text: "Little communication of simple concepts or facts.", rewrite: light, force: describes, status: drafted }
  forBeneficiary: { text: "You communicate simple ideas or facts very little.", rewrite: full, force: describes, status: drafted }
- sentence: cardiffmet/generic-2020/l6/presentation/1-29.s2
  forPractitioner: { text: "Frequent faults and weak structure obscure meaning.", rewrite: light, force: describes, status: drafted }
  forBeneficiary: { text: "Frequent faults and weak structure hide your meaning.", rewrite: full, force: describes, status: drafted }
- sentence: cardiffmet/generic-2020/l6/presentation/1-29.s3
  forPractitioner: { text: "Writing often clumsy and unsuitable.", rewrite: light, force: describes, status: drafted }
  forBeneficiary: { text: "Your writing is often clumsy and unsuitable.", rewrite: full, force: describes, status: drafted }
- sentence: cardiffmet/generic-2020/l6/analysis/80-100.s1
  forPractitioner: { text: "Designs and carries out own research or advanced scholarship with fitting techniques.", rewrite: light, force: describes, status: drafted }
  forBeneficiary: { text: "At the top, you design and carry out your own research with suitable methods.", rewrite: full, force: describes, status: drafted }
- sentence: cardiffmet/generic-2020/l6/analysis/70-79.s1
  forPractitioner: { text: "Detailed analysis and critical enquiry of data with very good use of fitting techniques.", rewrite: light, force: describes, status: drafted }
  forBeneficiary: { text: "You analyse data in detail and critically, using well-chosen techniques very well.", rewrite: full, force: describes, status: drafted }
- sentence: cardiffmet/generic-2020/l6/analysis/70-79.s2
  forPractitioner: { text: "Presents, synthesises and comments very successfully; perceptive on theory, practice, uncertainty, assumptions and own limits.", rewrite: light, force: describes, status: drafted }
  forBeneficiary: { text: "You bring your results together very successfully and comment perceptively on uncertainty, assumptions and the limits of what you know.", rewrite: full, force: describes, status: drafted }
- sentence: cardiffmet/generic-2020/l6/analysis/60-69.s1
  forPractitioner: { text: "Detailed analysis and critical enquiry with fitting techniques; considerable success with results.", rewrite: light, force: describes, status: drafted }
  forBeneficiary: { text: "You analyse in detail and critically, with suitable techniques, and present your results with considerable success.", rewrite: full, force: describes, status: drafted }
- sentence: cardiffmet/generic-2020/l6/analysis/60-69.s2
  forPractitioner: { text: "Some link of theory and practice; aware of uncertainty, assumptions and own limits.", rewrite: light, force: describes, status: drafted }
  forBeneficiary: { text: "You link theory and practice and see uncertainty, assumptions and the limits of what you know.", rewrite: full, force: describes, status: drafted }
- sentence: cardiffmet/generic-2020/l6/analysis/50-59.s1
  forPractitioner: { text: "Uses some techniques for analysis and enquiry; generally succeeds with results; aware of uncertainty and own limits.", rewrite: light, force: describes, status: drafted }
  forBeneficiary: { text: "You use some techniques to analyse, generally present your results well and see uncertainty and your own limits.", rewrite: full, force: describes, status: drafted }
- sentence: cardiffmet/generic-2020/l6/analysis/40-49.s1
  forPractitioner: { text: "Some limited analysis and enquiry; intermittent success with results; aware of uncertainty and own limits.", rewrite: light, force: describes, status: drafted }
  forBeneficiary: { text: "You analyse a little, present your results with mixed success and see uncertainty and your own limits.", rewrite: full, force: describes, status: drafted }
- sentence: cardiffmet/generic-2020/l6/analysis/30-39.s1
  forPractitioner: { text: "Attempts some enquiry and data analysis, but results may be naive, simplistic or unconvincing.", rewrite: light, force: describes, status: drafted }
  forBeneficiary: { text: "You attempt some analysis, but your results may be simplistic or unconvincing.", rewrite: full, force: describes, status: drafted }
- sentence: cardiffmet/generic-2020/l6/analysis/1-29.s1
  forPractitioner: { text: "Little evidence of enquiry or data analysis.", rewrite: light, force: describes, status: drafted }
  forBeneficiary: { text: "You show little research or data analysis.", rewrite: full, force: describes, status: drafted }
- sentence: cardiffmet/generic-2020/l6/analysis/1-29.s2
  forPractitioner: { text: "Results, where attempted, unsuitable or missing.", rewrite: light, force: describes, status: drafted }
  forBeneficiary: { text: "Where you try, your results are unsuitable or missing.", rewrite: full, force: describes, status: drafted }
- sentence: cardiffmet/generic-2020/l6/research/80-100.s1
  forPractitioner: { text: "In coursework, citations range well beyond the reading the field normally expects.", rewrite: light, force: describes, status: drafted }
  forBeneficiary: { text: "At the top, your coursework cites well beyond the usual reading.", rewrite: full, force: describes, status: drafted }
- sentence: cardiffmet/generic-2020/l6/research/80-100.s2
  forPractitioner: { text: "In examinations, a substantial range of citations.", rewrite: light, force: describes, status: drafted }
  forBeneficiary: { text: "In exams, you cite widely.", rewrite: full, force: describes, status: drafted }
- sentence: cardiffmet/generic-2020/l6/research/70-79.s1
  forPractitioner: { text: "Detailed, thorough and systematic knowledge of current research.", rewrite: light, force: describes, status: drafted }
  forBeneficiary: { text: "You know current research thoroughly and systematically.", rewrite: full, force: describes, status: drafted }
- sentence: cardiffmet/generic-2020/l6/research/70-79.s2
  forPractitioner: { text: "Confident use of reviews and primary sources; broad, deep reading beyond the sources given.", rewrite: light, force: describes, status: drafted }
  forBeneficiary: { text: "You use reviews and primary sources confidently and read broadly and deeply past the sources given.", rewrite: full, force: describes, status: drafted }
- sentence: cardiffmet/generic-2020/l6/research/70-79.s3
  forPractitioner: { text: "Referencing accurate and conventional.", rewrite: light, force: describes, status: drafted }
  forBeneficiary: { text: "Your referencing is accurate and follows academic conventions.", rewrite: full, force: describes, status: drafted }
- sentence: cardiffmet/generic-2020/l6/research/70-79.s4
  forPractitioner: { text: "Thorough grasp of research processes; determines, refines, adapts and uses research methods successfully.", rewrite: light, force: describes, status: drafted }
  forBeneficiary: { text: "You understand research methods thoroughly and choose, refine and adapt them successfully.", rewrite: full, force: describes, status: drafted }
- sentence: cardiffmet/generic-2020/l6/research/60-69.s1
  forPractitioner: { text: "Thorough knowledge of current research.", rewrite: light, force: describes, status: drafted }
  forBeneficiary: { text: "You know current research thoroughly.", rewrite: full, force: describes, status: drafted }
- sentence: cardiffmet/generic-2020/l6/research/60-69.s2
  forPractitioner: { text: "Reading broad and deep, beyond the sources given.", rewrite: light, force: describes, status: drafted }
  forBeneficiary: { text: "Your examples show broad, deep reading past the sources given.", rewrite: full, force: describes, status: drafted }
- sentence: cardiffmet/generic-2020/l6/research/60-69.s3
  forPractitioner: { text: "Referencing almost always accurate.", rewrite: light, force: describes, status: drafted }
  forBeneficiary: { text: "Your referencing is almost always accurate.", rewrite: full, force: describes, status: drafted }
- sentence: cardiffmet/generic-2020/l6/research/60-69.s4
  forPractitioner: { text: "Secure grasp of research processes; determines, refines, adapts and uses them fittingly.", rewrite: light, force: describes, status: drafted }
  forBeneficiary: { text: "You know research methods securely and choose and adapt them well.", rewrite: full, force: describes, status: drafted }
- sentence: cardiffmet/generic-2020/l6/research/50-59.s1
  forPractitioner: { text: "Sound knowledge of current research and discussion of its implications.", rewrite: light, force: describes, status: drafted }
  forBeneficiary: { text: "You know current research soundly and discuss what it means.", rewrite: full, force: describes, status: drafted }
- sentence: cardiffmet/generic-2020/l6/research/50-59.s2
  forPractitioner: { text: "Some independent reading and investigation shown.", rewrite: light, force: describes, status: drafted }
  forBeneficiary: { text: "Your examples show some reading and investigation of your own.", rewrite: full, force: describes, status: drafted }
- sentence: cardiffmet/generic-2020/l6/research/50-59.s3
  forPractitioner: { text: "Occasional referencing errors.", rewrite: light, force: describes, status: drafted }
  forBeneficiary: { text: "Your referencing has occasional slips.", rewrite: full, force: describes, status: drafted }
- sentence: cardiffmet/generic-2020/l6/research/50-59.s4
  forPractitioner: { text: "Some grasp of research processes, generally applied well, perhaps relying on tutor support.", rewrite: light, force: describes, status: drafted }
  forBeneficiary: { text: "You know something of research methods and use them well, perhaps with your tutor's help.", rewrite: full, force: describes, status: drafted }
- sentence: cardiffmet/generic-2020/l6/research/40-49.s1
  forPractitioner: { text: "Some knowledge of current research, with limited comment on its implications.", rewrite: light, force: describes, status: drafted }
  forBeneficiary: { text: "You know some current research and comment a little on what it means.", rewrite: full, force: describes, status: drafted }
- sentence: cardiffmet/generic-2020/l6/research/40-49.s2
  forPractitioner: { text: "May over-rely on course materials rather than own reading.", rewrite: light, force: describes, status: drafted }
  forBeneficiary: { text: "You may rely on course materials more than on your own reading.", rewrite: full, force: describes, status: drafted }
- sentence: cardiffmet/generic-2020/l6/research/40-49.s3
  forPractitioner: { text: "Referencing errors.", rewrite: light, force: describes, status: drafted }
  forBeneficiary: { text: "Your referencing has errors.", rewrite: full, force: describes, status: drafted }
- sentence: cardiffmet/generic-2020/l6/research/40-49.s4
  forPractitioner: { text: "Some grasp of research processes, applied less securely.", rewrite: light, force: describes, status: drafted }
  forBeneficiary: { text: "You know something of research methods but use them unsteadily.", rewrite: full, force: describes, status: drafted }
- sentence: cardiffmet/generic-2020/l6/research/30-39.s1
  forPractitioner: { text: "Limited or patchy knowledge of current research.", rewrite: light, force: describes, status: drafted }
  forBeneficiary: { text: "Your knowledge of current research is limited or patchy.", rewrite: full, force: describes, status: drafted }
- sentence: cardiffmet/generic-2020/l6/research/30-39.s2
  forPractitioner: { text: "Narrow sources; over-reliance on course materials; little own reading.", rewrite: light, force: describes, status: drafted }
  forBeneficiary: { text: "You use a narrow set of sources, rely on course materials and read little for yourself.", rewrite: full, force: describes, status: drafted }
- sentence: cardiffmet/generic-2020/l6/research/30-39.s3
  forPractitioner: { text: "Frequent referencing errors.", rewrite: light, force: describes, status: drafted }
  forBeneficiary: { text: "Your referencing has frequent errors.", rewrite: full, force: describes, status: drafted }
- sentence: cardiffmet/generic-2020/l6/research/30-39.s4
  forPractitioner: { text: "Research knowledge, where present, applied largely without success.", rewrite: light, force: describes, status: drafted }
  forBeneficiary: { text: "Where you know research methods, you mostly fail to apply them.", rewrite: full, force: describes, status: drafted }
- sentence: cardiffmet/generic-2020/l6/research/1-29.s1
  forPractitioner: { text: "Little knowledge of current research.", rewrite: light, force: describes, status: drafted }
  forBeneficiary: { text: "You show little knowledge of current research.", rewrite: full, force: describes, status: drafted }
- sentence: cardiffmet/generic-2020/l6/research/1-29.s2
  forPractitioner: { text: "Negligible own reading and investigation.", rewrite: light, force: describes, status: drafted }
  forBeneficiary: { text: "You do almost no reading or investigation of your own.", rewrite: full, force: describes, status: drafted }
- sentence: cardiffmet/generic-2020/l6/research/1-29.s3
  forPractitioner: { text: "Scant referencing, often wrong.", rewrite: light, force: describes, status: drafted }
  forBeneficiary: { text: "Your few references are often wrong.", rewrite: full, force: describes, status: drafted }
- sentence: cardiffmet/generic-2020/l6/research/1-29.s4
  forPractitioner: { text: "Very limited grasp of research processes, not applied.", rewrite: light, force: describes, status: drafted }
  forBeneficiary: { text: "You know very little about research methods and do not apply them.", rewrite: full, force: describes, status: drafted }
- sentence: cardiffmet/generic-2020/l6/argument/80-100.s1
  forPractitioner: { text: "May push at the boundaries of knowledge, with innovative or creative thinking.", rewrite: light, force: describes, status: drafted }
  forBeneficiary: { text: "At the top, your work may push at the edges of what is known, with inventive thinking.", rewrite: full, force: describes, status: drafted }
- sentence: cardiffmet/generic-2020/l6/argument/80-100.s2
  forPractitioner: { text: "New insights informed by critical evaluation of current research or practice.", rewrite: light, force: describes, status: drafted }
  forBeneficiary: { text: "You offer new insights drawn from critical evaluation of current research or practice.", rewrite: full, force: describes, status: drafted }
- sentence: cardiffmet/generic-2020/l6/argument/70-79.s1
  forPractitioner: { text: "Critically evaluates concepts, arguments and data and judges in an informed way.", rewrite: light, force: describes, status: drafted }
  forBeneficiary: { text: "You evaluate ideas, arguments and data critically and judge well.", rewrite: full, force: describes, status: drafted }
- sentence: cardiffmet/generic-2020/l6/argument/70-79.s2
  forPractitioner: { text: "Arguments developed, sustained and supported.", rewrite: light, force: describes, status: drafted }
  forBeneficiary: { text: "Your arguments are developed, sustained and supported.", rewrite: full, force: describes, status: drafted }
- sentence: cardiffmet/generic-2020/l6/argument/70-79.s3
  forPractitioner: { text: "Challenges assumptions where relevant; clearly sees the complexity of academic debate.", rewrite: light, force: describes, status: drafted }
  forBeneficiary: { text: "You question assumptions where it matters and see clearly how complex academic debate is.", rewrite: full, force: describes, status: drafted }
- sentence: cardiffmet/generic-2020/l6/argument/70-79.s4
  forPractitioner: { text: "Fitting, sometimes innovative solutions to ill-defined, many-factor problems.", rewrite: light, force: describes, status: drafted }
  forBeneficiary: { text: "You find suitable and sometimes inventive solutions to loosely defined problems with many factors.", rewrite: full, force: describes, status: drafted }
- sentence: cardiffmet/generic-2020/l6/argument/70-79.s5
  forPractitioner: { text: "Strong evidence of reflecting effectively on own practice.", rewrite: light, force: describes, status: drafted }
  forBeneficiary: { text: "You reflect well on your own practice.", rewrite: full, force: describes, status: drafted }
- sentence: cardiffmet/generic-2020/l6/argument/70-79.s6
  forPractitioner: { text: "Highly perceptive evaluation of own work or practice; fully aware of what it means for development.", rewrite: light, force: describes, status: drafted }
  forBeneficiary: { text: "You evaluate your own work with sharp insight and see clearly what it means for how you develop.", rewrite: full, force: describes, status: drafted }
- sentence: cardiffmet/generic-2020/l6/argument/60-69.s1
  forPractitioner: { text: "Critically evaluates and reflects.", rewrite: light, force: describes, status: drafted }
  forBeneficiary: { text: "You evaluate and reflect critically.", rewrite: full, force: describes, status: drafted }
- sentence: cardiffmet/generic-2020/l6/argument/60-69.s2
  forPractitioner: { text: "Arguments considered and supported; judges fittingly and suggests solutions to ill-defined, many-factor problems.", rewrite: light, force: describes, status: drafted }
  forBeneficiary: { text: "Your arguments are considered and supported, and you suggest solutions to loosely defined problems.", rewrite: full, force: describes, status: drafted }
- sentence: cardiffmet/generic-2020/l6/argument/60-69.s3
  forPractitioner: { text: "Reflects on own practice and uses self-evaluation to plan development.", rewrite: light, force: describes, status: drafted }
  forBeneficiary: { text: "You reflect on your practice and use what you find to plan how to develop.", rewrite: full, force: describes, status: drafted }
- sentence: cardiffmet/generic-2020/l6/argument/50-59.s1
  forPractitioner: { text: "Critically evaluates and reflects, with some leaning on description.", rewrite: light, force: describes, status: drafted }
  forBeneficiary: { text: "You evaluate and reflect critically, though you lean on description.", rewrite: full, force: describes, status: drafted }
- sentence: cardiffmet/generic-2020/l6/argument/50-59.s2
  forPractitioner: { text: "Arguments usually supported.", rewrite: light, force: describes, status: drafted }
  forBeneficiary: { text: "Your arguments are usually supported.", rewrite: full, force: describes, status: drafted }
- sentence: cardiffmet/generic-2020/l6/argument/50-59.s3
  forPractitioner: { text: "Some reflection on own practice, lacking insight into future development.", rewrite: light, force: describes, status: drafted }
  forBeneficiary: { text: "You reflect on your own practice, but without much insight into how to develop.", rewrite: full, force: describes, status: drafted }
- sentence: cardiffmet/generic-2020/l6/argument/40-49.s1
  forPractitioner: { text: "Limited critical evaluation and reflection.", rewrite: light, force: describes, status: drafted }
  forBeneficiary: { text: "You evaluate and reflect critically only a little.", rewrite: full, force: describes, status: drafted }
- sentence: cardiffmet/generic-2020/l6/argument/40-49.s2
  forPractitioner: { text: "Some critical reflection, but mostly description and fact.", rewrite: light, force: describes, status: drafted }
  forBeneficiary: { text: "You reflect critically a little, but your work is mostly description.", rewrite: full, force: describes, status: drafted }
- sentence: cardiffmet/generic-2020/l6/argument/40-49.s3
  forPractitioner: { text: "Arguments generally supported but thin.", rewrite: light, force: describes, status: drafted }
  forBeneficiary: { text: "Your arguments are generally supported but thin.", rewrite: full, force: describes, status: drafted }
- sentence: cardiffmet/generic-2020/l6/argument/40-49.s4
  forPractitioner: { text: "Some evaluation of and reflection on own practice.", rewrite: light, force: describes, status: drafted }
  forBeneficiary: { text: "You evaluate and reflect on your own practice to some extent.", rewrite: full, force: describes, status: drafted }
- sentence: cardiffmet/generic-2020/l6/argument/40-49.s5
  forPractitioner: { text: "Reflection may be limited and superficial, with little thought for development.", rewrite: light, force: describes, status: drafted }
  forBeneficiary: { text: "Your reflection may be brief and on the surface, with little thought about how to develop.", rewrite: full, force: describes, status: drafted }
- sentence: cardiffmet/generic-2020/l6/argument/30-39.s1
  forPractitioner: { text: "Limited sign of critical evaluation and reflection.", rewrite: light, force: describes, status: drafted }
  forBeneficiary: { text: "You show little critical evaluation or reflection.", rewrite: full, force: describes, status: drafted }
- sentence: cardiffmet/generic-2020/l6/argument/30-39.s2
  forPractitioner: { text: "Largely descriptive; arguments, if tried, rarely supported.", rewrite: light, force: describes, status: drafted }
  forBeneficiary: { text: "Your work is largely descriptive, and any arguments are rarely supported.", rewrite: full, force: describes, status: drafted }
- sentence: cardiffmet/generic-2020/l6/argument/30-39.s3
  forPractitioner: { text: "Self-evaluation very limited.", rewrite: light, force: describes, status: drafted }
  forBeneficiary: { text: "You reflect on your own practice very little.", rewrite: full, force: describes, status: drafted }
- sentence: cardiffmet/generic-2020/l6/argument/1-29.s1
  forPractitioner: { text: "Little description or reporting.", rewrite: light, force: describes, status: drafted }
  forBeneficiary: { text: "You describe and report very little.", rewrite: full, force: describes, status: drafted }
- sentence: cardiffmet/generic-2020/l6/argument/1-29.s2
  forPractitioner: { text: "Very little sign of critical evaluation or reflection.", rewrite: light, force: describes, status: drafted }
  forBeneficiary: { text: "You show almost no critical evaluation or reflection.", rewrite: full, force: describes, status: drafted }
- sentence: cardiffmet/generic-2020/l6/argument/1-29.s3
  forPractitioner: { text: "Self-evaluation negligible or absent.", rewrite: light, force: describes, status: drafted }
  forBeneficiary: { text: "You reflect on your own practice little or not at all.", rewrite: full, force: describes, status: drafted }
- sentence: cardiffmet/generic-2020/l7/overall/80-100.s1
  forPractitioner: { text: "Full, detailed grasp of the task; outcomes met and criteria addressed excellently (80-89) or outstandingly (90-100), past this level.", rewrite: light, force: describes, status: drafted }
  forBeneficiary: { text: "You understand the task fully and in detail and meet its outcomes excellently, or outstandingly above 90, past this level.", rewrite: full, force: describes, status: drafted }
- sentence: cardiffmet/generic-2020/l7/overall/80-100.s2
  forPractitioner: { text: "Work of a standard fit for publication, manufacture, exhibition or performance.", rewrite: light, force: describes, status: drafted }
  forBeneficiary: { text: "Your work is good enough to publish, make, exhibit or perform.", rewrite: full, force: describes, status: drafted }
- sentence: cardiffmet/generic-2020/l7/overall/70-79.s1
  forPractitioner: { text: "Full, detailed grasp of the task; outcomes met and criteria addressed very well.", rewrite: light, force: describes, status: drafted }
  forBeneficiary: { text: "You understand the task fully and in detail and meet its outcomes and criteria very well.", rewrite: full, force: describes, status: drafted }
- sentence: cardiffmet/generic-2020/l7/overall/60-69.s1
  forPractitioner: { text: "Full grasp of the task; outcomes met and criteria addressed well.", rewrite: light, force: describes, status: drafted }
  forBeneficiary: { text: "You understand the task fully and meet its outcomes and criteria well.", rewrite: full, force: describes, status: drafted }
- sentence: cardiffmet/generic-2020/l7/overall/50-59.s1
  forPractitioner: { text: "Basic but secure grasp of the task; outcomes met and criteria addressed at the threshold.", rewrite: light, force: describes, status: drafted }
  forBeneficiary: { text: "You understand the task at a basic but secure level and meet its outcomes and criteria at the minimum standard.", rewrite: full, force: describes, status: drafted }
- sentence: cardiffmet/generic-2020/l7/overall/40-49.s1
  forPractitioner: { text: "Partial grasp of the task; outcomes and criteria met at a limited, insufficient level.", rewrite: light, force: describes, status: drafted }
  forBeneficiary: { text: "You understand the task in part and do not yet meet its outcomes and criteria well enough.", rewrite: full, force: describes, status: drafted }
- sentence: cardiffmet/generic-2020/l7/overall/40-49.s2
  forPractitioner: { text: "Unsatisfactory overall.", rewrite: light, force: describes, status: drafted }
  forBeneficiary: { text: "Your work is not yet satisfactory overall.", rewrite: full, force: describes, status: drafted }
- sentence: cardiffmet/generic-2020/l7/overall/40-49.s3
  forPractitioner: { text: "Uneven: some outcomes unmet, some criteria unaddressed.", rewrite: light, force: describes, status: drafted }
  forBeneficiary: { text: "Your work is uneven: some outcomes are not met and some criteria are not addressed.", rewrite: full, force: describes, status: drafted }
- sentence: cardiffmet/generic-2020/l7/overall/20-39.s1
  forPractitioner: { text: "Unsatisfactory overall.", rewrite: light, force: describes, status: drafted }
  forBeneficiary: { text: "Your work is not yet satisfactory overall.", rewrite: full, force: describes, status: drafted }
- sentence: cardiffmet/generic-2020/l7/overall/20-39.s2
  forPractitioner: { text: "Minimal grasp of the task; some outcomes met at a basic level.", rewrite: light, force: describes, status: drafted }
  forBeneficiary: { text: "You show little understanding of the task and meet only some outcomes at a basic level.", rewrite: full, force: describes, status: drafted }
- sentence: cardiffmet/generic-2020/l7/overall/20-39.s3
  forPractitioner: { text: "Uneven, with many criteria unaddressed.", rewrite: light, force: describes, status: drafted }
  forBeneficiary: { text: "Your work is uneven, and many criteria are not addressed.", rewrite: full, force: describes, status: drafted }
- sentence: cardiffmet/generic-2020/l7/overall/1-19.s1
  forPractitioner: { text: "Very poor, incomplete or irrelevant.", rewrite: light, force: describes, status: drafted }
  forBeneficiary: { text: "Your work is very poor, incomplete or off the point.", rewrite: full, force: describes, status: drafted }
- sentence: cardiffmet/generic-2020/l7/overall/1-19.s2
  forPractitioner: { text: "Serious lack of comprehension of, or engagement with, the task.", rewrite: light, force: describes, status: drafted }
  forBeneficiary: { text: "You show a serious lack of understanding of, or engagement with, the task.", rewrite: full, force: describes, status: drafted }
- sentence: cardiffmet/generic-2020/l7/overall/1-19.s3
  forPractitioner: { text: "The task may have been misunderstood.", rewrite: light, force: describes, status: drafted }
  forBeneficiary: { text: "You may have misread the task.", rewrite: full, force: describes, status: drafted }
- sentence: cardiffmet/generic-2020/l7/overall/1-19.s4
  forPractitioner: { text: "No outcome met in full; perhaps minimal attainment in one or two areas.", rewrite: light, force: describes, status: drafted }
  forBeneficiary: { text: "You meet no outcome in full, though you may achieve a little in one or two areas.", rewrite: full, force: describes, status: drafted }
- sentence: cardiffmet/generic-2020/l7/knowledge/80-100.s1
  forPractitioner: { text: "The top band goes beyond what this level expects.", rewrite: light, force: describes, status: drafted }
  forBeneficiary: { text: "At the top, your work goes past what this level expects.", rewrite: full, force: describes, status: drafted }
- sentence: cardiffmet/generic-2020/l7/knowledge/80-100.s2
  forPractitioner: { text: "Exceptional mastery of a complex, specialist area.", rewrite: light, force: describes, status: drafted }
  forBeneficiary: { text: "You show exceptional mastery of a complex specialist area.", rewrite: full, force: describes, status: drafted }
- sentence: cardiffmet/generic-2020/l7/knowledge/70-79.s1
  forPractitioner: { text: "Mastery of a complex, specialised area of knowledge.", rewrite: light, force: describes, status: drafted }
  forBeneficiary: { text: "You have mastered a complex specialist area.", rewrite: full, force: describes, status: drafted }
- sentence: cardiffmet/generic-2020/l7/knowledge/70-79.s2
  forPractitioner: { text: "Strong evidence of extending, transforming and applying that knowledge.", rewrite: light, force: describes, status: drafted }
  forBeneficiary: { text: "You take what you know further, reshape it and apply it strongly.", rewrite: full, force: describes, status: drafted }
- sentence: cardiffmet/generic-2020/l7/knowledge/70-79.s3
  forPractitioner: { text: "Confident discussion of complex concepts; recognises the limits and ambiguity of knowledge.", rewrite: light, force: describes, status: drafted }
  forBeneficiary: { text: "You discuss complex ideas confidently and see where knowledge is limited or unclear.", rewrite: full, force: describes, status: drafted }
- sentence: cardiffmet/generic-2020/l7/knowledge/70-79.s4
  forPractitioner: { text: "Independent thought and action.", rewrite: light, force: describes, status: drafted }
  forBeneficiary: { text: "You think and act independently.", rewrite: full, force: describes, status: drafted }
- sentence: cardiffmet/generic-2020/l7/knowledge/70-79.s5
  forPractitioner: { text: "Original insights are a feature.", rewrite: light, force: describes, status: drafted }
  forBeneficiary: { text: "You offer original insight.", rewrite: full, force: describes, status: drafted }
- sentence: cardiffmet/generic-2020/l7/knowledge/60-69.s1
  forPractitioner: { text: "Mastery of a complex, specialised area of knowledge.", rewrite: light, force: describes, status: drafted }
  forBeneficiary: { text: "You have mastered a complex specialist area.", rewrite: full, force: describes, status: drafted }
- sentence: cardiffmet/generic-2020/l7/knowledge/60-69.s2
  forPractitioner: { text: "Applies knowledge clearly in familiar contexts, extending and transforming it.", rewrite: light, force: describes, status: drafted }
  forBeneficiary: { text: "You apply your knowledge clearly in familiar settings and take it further.", rewrite: full, force: describes, status: drafted }
- sentence: cardiffmet/generic-2020/l7/knowledge/60-69.s3
  forPractitioner: { text: "Complex concepts often discussed well; some independent thought and action.", rewrite: light, force: describes, status: drafted }
  forBeneficiary: { text: "You often discuss complex ideas well and show some independent thought and action.", rewrite: full, force: describes, status: drafted }
- sentence: cardiffmet/generic-2020/l7/knowledge/50-59.s1
  forPractitioner: { text: "Mastery of a complex, specialised area, but often descriptive and tied to given sources.", rewrite: light, force: describes, status: drafted }
  forBeneficiary: { text: "You have mastered a complex specialist area, but you often describe and stay with given sources.", rewrite: full, force: describes, status: drafted }
- sentence: cardiffmet/generic-2020/l7/knowledge/50-59.s2
  forPractitioner: { text: "Limited independent thought and action.", rewrite: light, force: describes, status: drafted }
  forBeneficiary: { text: "You show little independent thought or action.", rewrite: full, force: describes, status: drafted }
- sentence: cardiffmet/generic-2020/l7/knowledge/40-49.s1
  forPractitioner: { text: "Limited knowledge of the relevant field.", rewrite: light, force: describes, status: drafted }
  forBeneficiary: { text: "Your knowledge of the field is limited.", rewrite: full, force: describes, status: drafted }
- sentence: cardiffmet/generic-2020/l7/knowledge/40-49.s2
  forPractitioner: { text: "Inaccuracies and misconceptions in important areas; parts may be off the task.", rewrite: light, force: describes, status: drafted }
  forBeneficiary: { text: "You make mistakes in important areas, and parts of your work may be off the task.", rewrite: full, force: describes, status: drafted }
- sentence: cardiffmet/generic-2020/l7/knowledge/20-39.s1
  forPractitioner: { text: "Little knowledge of the relevant field.", rewrite: light, force: describes, status: drafted }
  forBeneficiary: { text: "You show little knowledge of the field.", rewrite: full, force: describes, status: drafted }
- sentence: cardiffmet/generic-2020/l7/knowledge/20-39.s2
  forPractitioner: { text: "Errors in many important areas outweigh what is understood.", rewrite: light, force: describes, status: drafted }
  forBeneficiary: { text: "Your mistakes in many important areas outweigh what you understand.", rewrite: full, force: describes, status: drafted }
- sentence: cardiffmet/generic-2020/l7/knowledge/20-39.s3
  forPractitioner: { text: "Much of the work may be off the task.", rewrite: light, force: describes, status: drafted }
  forBeneficiary: { text: "Much of your work may be off the task.", rewrite: full, force: describes, status: drafted }
- sentence: cardiffmet/generic-2020/l7/knowledge/1-19.s1
  forPractitioner: { text: "Band-wide: work may be short or irrelevant, with serious errors; no analysis, synthesis, evaluation or reflection; little or no use of sources; very poor presentation and communication.", rewrite: light, force: describes, status: drafted }
  forBeneficiary: { text: "In this band your work may be short or off the point, with serious errors, no analysis or reflection, few or no sources, and very poor presentation.", rewrite: full, force: describes, status: drafted }
- sentence: cardiffmet/generic-2020/l7/presentation/80-100.s1
  forPractitioner: { text: "Beyond 70-79: consistently convincing, concise arguments throughout.", rewrite: light, force: describes, status: drafted }
  forBeneficiary: { text: "At the top, your arguments are convincing and concise throughout.", rewrite: full, force: describes, status: drafted }
- sentence: cardiffmet/generic-2020/l7/presentation/80-100.s2
  forPractitioner: { text: "Eloquent, professional style of communication.", rewrite: light, force: describes, status: drafted }
  forBeneficiary: { text: "You communicate in an eloquent, professional style.", rewrite: full, force: describes, status: drafted }
- sentence: cardiffmet/generic-2020/l7/presentation/70-79.s1
  forPractitioner: { text: "Communicates information, complex ideas and research results coherently and concisely in many situations.", rewrite: light, force: describes, status: drafted }
  forBeneficiary: { text: "You communicate complex ideas and research results coherently and concisely in many settings.", rewrite: full, force: describes, status: drafted }
- sentence: cardiffmet/generic-2020/l7/presentation/70-79.s2
  forPractitioner: { text: "High standard of presentation; format fits.", rewrite: light, force: describes, status: drafted }
  forBeneficiary: { text: "Your work is presented to a high standard in a suitable format.", rewrite: full, force: describes, status: drafted }
- sentence: cardiffmet/generic-2020/l7/presentation/70-79.s3
  forPractitioner: { text: "Points logically organised; lucid, mature style in writing.", rewrite: light, force: describes, status: drafted }
  forBeneficiary: { text: "Your points are logically ordered and your writing is lucid and mature.", rewrite: full, force: describes, status: drafted }
- sentence: cardiffmet/generic-2020/l7/presentation/70-79.s4
  forPractitioner: { text: "Arguments well defined and clearly put.", rewrite: light, force: describes, status: drafted }
  forBeneficiary: { text: "Your arguments are well defined and clearly put.", rewrite: full, force: describes, status: drafted }
- sentence: cardiffmet/generic-2020/l7/presentation/60-69.s1
  forPractitioner: { text: "Communicates information, research results and ideas clearly and concisely in many situations.", rewrite: light, force: describes, status: drafted }
  forBeneficiary: { text: "You communicate your research and ideas clearly and concisely in many settings.", rewrite: full, force: describes, status: drafted }
- sentence: cardiffmet/generic-2020/l7/presentation/60-69.s2
  forPractitioner: { text: "Well presented; format fits.", rewrite: light, force: describes, status: drafted }
  forBeneficiary: { text: "Your work is well presented in a suitable format.", rewrite: full, force: describes, status: drafted }
- sentence: cardiffmet/generic-2020/l7/presentation/60-69.s3
  forPractitioner: { text: "Points organised, fluent and well put.", rewrite: light, force: describes, status: drafted }
  forBeneficiary: { text: "Your points are organised, fluent and well put.", rewrite: full, force: describes, status: drafted }
- sentence: cardiffmet/generic-2020/l7/presentation/50-59.s1
  forPractitioner: { text: "Satisfactory communication of research results and ideas in familiar situations.", rewrite: light, force: describes, status: drafted }
  forBeneficiary: { text: "You communicate your research and ideas satisfactorily in familiar settings.", rewrite: full, force: describes, status: drafted }
- sentence: cardiffmet/generic-2020/l7/presentation/50-59.s2
  forPractitioner: { text: "Some lack of rigour; leans on description and fact rather than complex ideas.", rewrite: light, force: describes, status: drafted }
  forBeneficiary: { text: "Parts of your work lack rigour and lean on description rather than complex ideas.", rewrite: full, force: describes, status: drafted }
- sentence: cardiffmet/generic-2020/l7/presentation/50-59.s3
  forPractitioner: { text: "Mostly structured, but not always coherent.", rewrite: light, force: describes, status: drafted }
  forBeneficiary: { text: "Your work is mostly structured, but not always coherent.", rewrite: full, force: describes, status: drafted }
- sentence: cardiffmet/generic-2020/l7/presentation/40-49.s1
  forPractitioner: { text: "Communicates some simple concepts or facts.", rewrite: light, force: describes, status: drafted }
  forBeneficiary: { text: "You communicate some simple ideas or facts.", rewrite: full, force: describes, status: drafted }
- sentence: cardiffmet/generic-2020/l7/presentation/40-49.s2
  forPractitioner: { text: "Ideas may be unclear and hard for the reader to follow.", rewrite: light, force: describes, status: drafted }
  forBeneficiary: { text: "Your ideas may be unclear and hard to follow.", rewrite: full, force: describes, status: drafted }
- sentence: cardiffmet/generic-2020/l7/presentation/40-49.s3
  forPractitioner: { text: "Arguments and complex ideas, if tried, may be confused and clumsy.", rewrite: light, force: describes, status: drafted }
  forBeneficiary: { text: "Any arguments or complex ideas you try may come out confused.", rewrite: full, force: describes, status: drafted }
- sentence: cardiffmet/generic-2020/l7/presentation/20-39.s1
  forPractitioner: { text: "Limited communication of simple concepts or facts.", rewrite: light, force: describes, status: drafted }
  forBeneficiary: { text: "You communicate simple ideas or facts only a little.", rewrite: full, force: describes, status: drafted }
- sentence: cardiffmet/generic-2020/l7/presentation/20-39.s2
  forPractitioner: { text: "Frequent faults and weak structure obscure meaning.", rewrite: light, force: describes, status: drafted }
  forBeneficiary: { text: "Frequent faults and weak structure hide your meaning.", rewrite: full, force: describes, status: drafted }
- sentence: cardiffmet/generic-2020/l7/presentation/20-39.s3
  forPractitioner: { text: "Writing often clumsy and unsuitable.", rewrite: light, force: describes, status: drafted }
  forBeneficiary: { text: "Your writing is often clumsy and unsuitable.", rewrite: full, force: describes, status: drafted }
- sentence: cardiffmet/generic-2020/l7/analysis/80-100.s1
  forPractitioner: { text: "Designs and carries out extensive, independent inquiry, applying advanced methods consistently to unfamiliar problems.", rewrite: light, force: describes, status: drafted }
  forBeneficiary: { text: "At the top, you design and carry out your own extensive inquiry, applying advanced methods to unfamiliar problems.", rewrite: full, force: describes, status: drafted }
- sentence: cardiffmet/generic-2020/l7/analysis/70-79.s1
  forPractitioner: { text: "Conducts research or advanced professional activity; detailed, critical analysis; expert specialist skills with excellent use of techniques.", rewrite: light, force: describes, status: drafted }
  forBeneficiary: { text: "You carry out research or advanced professional work, analyse critically and in detail, and use specialist techniques expertly.", rewrite: full, force: describes, status: drafted }
- sentence: cardiffmet/generic-2020/l7/analysis/70-79.s2
  forPractitioner: { text: "Presents, synthesises and comments on process and results very successfully; perceptive on theory and practice.", rewrite: light, force: describes, status: drafted }
  forBeneficiary: { text: "You bring together and comment on your process and results very successfully, with perceptive points on theory and practice.", rewrite: full, force: describes, status: drafted }
- sentence: cardiffmet/generic-2020/l7/analysis/60-69.s1
  forPractitioner: { text: "Conducts research or advanced professional activity; some detailed, critical analysis; specialist skills; considerable success with process and results.", rewrite: light, force: describes, status: drafted }
  forBeneficiary: { text: "You carry out research or advanced professional work with specialist skill, analyse in some detail and present your process and results with considerable success.", rewrite: full, force: describes, status: drafted }
- sentence: cardiffmet/generic-2020/l7/analysis/60-69.s2
  forPractitioner: { text: "Some link made between theory and practice.", rewrite: light, force: describes, status: drafted }
  forBeneficiary: { text: "You link theory with practice to some degree.", rewrite: full, force: describes, status: drafted }
- sentence: cardiffmet/generic-2020/l7/analysis/50-59.s1
  forPractitioner: { text: "Conducts research or advanced professional activity; some limited analysis; specialist skills; some success with process and results.", rewrite: light, force: describes, status: drafted }
  forBeneficiary: { text: "You carry out research or advanced professional work with specialist skill, analyse to a limited extent and present your results with some success.", rewrite: full, force: describes, status: drafted }
- sentence: cardiffmet/generic-2020/l7/analysis/40-49.s1
  forPractitioner: { text: "Attempts some enquiry and analysis, but process and results may be naive, simplistic or unconvincing.", rewrite: light, force: describes, status: drafted }
  forBeneficiary: { text: "You attempt some research and analysis, but your process and results may be simplistic or unconvincing.", rewrite: full, force: describes, status: drafted }
- sentence: cardiffmet/generic-2020/l7/analysis/20-39.s1
  forPractitioner: { text: "Little evidence of enquiry or analysis.", rewrite: light, force: describes, status: drafted }
  forBeneficiary: { text: "You show little research or analysis.", rewrite: full, force: describes, status: drafted }
- sentence: cardiffmet/generic-2020/l7/analysis/20-39.s2
  forPractitioner: { text: "Process and results, where attempted, unsuitable or missing.", rewrite: light, force: describes, status: drafted }
  forBeneficiary: { text: "Where you try, your process and results are unsuitable or missing.", rewrite: full, force: describes, status: drafted }
- sentence: cardiffmet/generic-2020/l7/research/80-100.s1
  forPractitioner: { text: "Exceptional breadth and depth shown by independent insight and critical awareness of literature at the forefront.", rewrite: light, force: describes, status: drafted }
  forBeneficiary: { text: "At the top, your knowledge is exceptionally broad and deep, with your own insight into leading-edge literature.", rewrite: full, force: describes, status: drafted }
- sentence: cardiffmet/generic-2020/l7/research/80-100.s2
  forPractitioner: { text: "In coursework, citations range well beyond the reading the field normally expects.", rewrite: light, force: describes, status: drafted }
  forBeneficiary: { text: "At the top, your coursework cites well beyond the usual reading.", rewrite: full, force: describes, status: drafted }
- sentence: cardiffmet/generic-2020/l7/research/80-100.s3
  forPractitioner: { text: "In examinations, a substantial range of citations.", rewrite: light, force: describes, status: drafted }
  forBeneficiary: { text: "In exams, you cite widely.", rewrite: full, force: describes, status: drafted }
- sentence: cardiffmet/generic-2020/l7/research/70-79.s1
  forPractitioner: { text: "Detailed, thorough knowledge of current research.", rewrite: light, force: describes, status: drafted }
  forBeneficiary: { text: "You know current research thoroughly and in detail.", rewrite: full, force: describes, status: drafted }
- sentence: cardiffmet/generic-2020/l7/research/70-79.s2
  forPractitioner: { text: "Confident use of reviews and primary sources; broad, deep reading beyond the sources given.", rewrite: light, force: describes, status: drafted }
  forBeneficiary: { text: "You use reviews and primary sources confidently and read broadly and deeply past the sources given.", rewrite: full, force: describes, status: drafted }
- sentence: cardiffmet/generic-2020/l7/research/70-79.s3
  forPractitioner: { text: "Referencing accurate and conventional.", rewrite: light, force: describes, status: drafted }
  forBeneficiary: { text: "Your referencing is accurate and follows academic conventions.", rewrite: full, force: describes, status: drafted }
- sentence: cardiffmet/generic-2020/l7/research/70-79.s4
  forPractitioner: { text: "Thorough grasp of research processes; designs and applies fitting methodologies.", rewrite: light, force: describes, status: drafted }
  forBeneficiary: { text: "You understand research methods thoroughly and design and apply suitable ones.", rewrite: full, force: describes, status: drafted }
- sentence: cardiffmet/generic-2020/l7/research/70-79.s5
  forPractitioner: { text: "Applies research knowledge and skills successfully.", rewrite: light, force: describes, status: drafted }
  forBeneficiary: { text: "You apply research skills successfully.", rewrite: full, force: describes, status: drafted }
- sentence: cardiffmet/generic-2020/l7/research/60-69.s1
  forPractitioner: { text: "Thorough knowledge of current research.", rewrite: light, force: describes, status: drafted }
  forBeneficiary: { text: "You know current research thoroughly.", rewrite: full, force: describes, status: drafted }
- sentence: cardiffmet/generic-2020/l7/research/60-69.s2
  forPractitioner: { text: "Reading broad and deep, beyond the sources given.", rewrite: light, force: describes, status: drafted }
  forBeneficiary: { text: "Your examples show broad, deep reading past the sources given.", rewrite: full, force: describes, status: drafted }
- sentence: cardiffmet/generic-2020/l7/research/60-69.s3
  forPractitioner: { text: "Referencing almost always accurate.", rewrite: light, force: describes, status: drafted }
  forBeneficiary: { text: "Your referencing is almost always accurate.", rewrite: full, force: describes, status: drafted }
- sentence: cardiffmet/generic-2020/l7/research/60-69.s4
  forPractitioner: { text: "Secure grasp of research processes; designs and applies fitting methodologies.", rewrite: light, force: describes, status: drafted }
  forBeneficiary: { text: "You know research methods securely and design and apply suitable ones.", rewrite: full, force: describes, status: drafted }
- sentence: cardiffmet/generic-2020/l7/research/60-69.s5
  forPractitioner: { text: "Applies research skills and knowledge fittingly.", rewrite: light, force: describes, status: drafted }
  forBeneficiary: { text: "You apply research skills well.", rewrite: full, force: describes, status: drafted }
- sentence: cardiffmet/generic-2020/l7/research/50-59.s1
  forPractitioner: { text: "Knows current research and comments on its implications to some degree.", rewrite: light, force: describes, status: drafted }
  forBeneficiary: { text: "You know current research and comment on what it means to some degree.", rewrite: full, force: describes, status: drafted }
- sentence: cardiffmet/generic-2020/l7/research/50-59.s2
  forPractitioner: { text: "May rely on given sources rather than own reading to advance the work.", rewrite: light, force: describes, status: drafted }
  forBeneficiary: { text: "You may rely on given sources rather than your own reading to move your work on.", rewrite: full, force: describes, status: drafted }
- sentence: cardiffmet/generic-2020/l7/research/40-49.s1
  forPractitioner: { text: "Limited or patchy knowledge of current research.", rewrite: light, force: describes, status: drafted }
  forBeneficiary: { text: "Your knowledge of current research is limited or patchy.", rewrite: full, force: describes, status: drafted }
- sentence: cardiffmet/generic-2020/l7/research/40-49.s2
  forPractitioner: { text: "Narrow sources; over-reliance on course materials; little own reading.", rewrite: light, force: describes, status: drafted }
  forBeneficiary: { text: "You use a narrow set of sources, rely on course materials and read little for yourself.", rewrite: full, force: describes, status: drafted }
- sentence: cardiffmet/generic-2020/l7/research/40-49.s3
  forPractitioner: { text: "Frequent referencing errors.", rewrite: light, force: describes, status: drafted }
  forBeneficiary: { text: "Your referencing has frequent errors.", rewrite: full, force: describes, status: drafted }
- sentence: cardiffmet/generic-2020/l7/research/40-49.s4
  forPractitioner: { text: "Academic conventions applied inconsistently.", rewrite: light, force: describes, status: drafted }
  forBeneficiary: { text: "You follow academic conventions inconsistently.", rewrite: full, force: describes, status: drafted }
- sentence: cardiffmet/generic-2020/l7/research/40-49.s5
  forPractitioner: { text: "Research knowledge, where present, applied largely without success.", rewrite: light, force: describes, status: drafted }
  forBeneficiary: { text: "Where you know research methods, you mostly fail to apply them.", rewrite: full, force: describes, status: drafted }
- sentence: cardiffmet/generic-2020/l7/research/20-39.s1
  forPractitioner: { text: "Little knowledge of current research.", rewrite: light, force: describes, status: drafted }
  forBeneficiary: { text: "You show little knowledge of current research.", rewrite: full, force: describes, status: drafted }
- sentence: cardiffmet/generic-2020/l7/research/20-39.s2
  forPractitioner: { text: "Negligible own reading; scant referencing, often wrong.", rewrite: light, force: describes, status: drafted }
  forBeneficiary: { text: "You do almost no reading of your own, and your few references are often wrong.", rewrite: full, force: describes, status: drafted }
- sentence: cardiffmet/generic-2020/l7/research/20-39.s3
  forPractitioner: { text: "Very limited grasp of research processes, not applied.", rewrite: light, force: describes, status: drafted }
  forBeneficiary: { text: "You know very little about research methods and do not apply them.", rewrite: full, force: describes, status: drafted }
- sentence: cardiffmet/generic-2020/l7/argument/80-100.s1
  forPractitioner: { text: "May push at the boundaries of knowledge, with innovative or creative thinking.", rewrite: light, force: describes, status: drafted }
  forBeneficiary: { text: "At the top, your work may push at the edges of what is known, with inventive thinking.", rewrite: full, force: describes, status: drafted }
- sentence: cardiffmet/generic-2020/l7/argument/80-100.s2
  forPractitioner: { text: "New insights informed by critical evaluation of current research or practice.", rewrite: light, force: describes, status: drafted }
  forBeneficiary: { text: "You offer new insights drawn from critical evaluation of current research or practice.", rewrite: full, force: describes, status: drafted }
- sentence: cardiffmet/generic-2020/l7/argument/70-79.s1
  forPractitioner: { text: "Critically evaluates concepts, arguments and data and judges in an informed way among many interacting factors.", rewrite: light, force: describes, status: drafted }
  forBeneficiary: { text: "You evaluate ideas and data critically and judge well where many factors interact.", rewrite: full, force: describes, status: drafted }
- sentence: cardiffmet/generic-2020/l7/argument/70-79.s2
  forPractitioner: { text: "Arguments developed, sustained and supported.", rewrite: light, force: describes, status: drafted }
  forBeneficiary: { text: "Your arguments are developed, sustained and supported.", rewrite: full, force: describes, status: drafted }
- sentence: cardiffmet/generic-2020/l7/argument/70-79.s3
  forPractitioner: { text: "Challenges assumptions where relevant; clearly sees the complexity of academic debate.", rewrite: light, force: describes, status: drafted }
  forBeneficiary: { text: "You question assumptions where it matters and see clearly how complex academic debate is.", rewrite: full, force: describes, status: drafted }
- sentence: cardiffmet/generic-2020/l7/argument/70-79.s4
  forPractitioner: { text: "Fitting, sometimes innovative solutions to problems.", rewrite: light, force: describes, status: drafted }
  forBeneficiary: { text: "You find suitable and sometimes inventive solutions to problems.", rewrite: full, force: describes, status: drafted }
- sentence: cardiffmet/generic-2020/l7/argument/70-79.s5
  forPractitioner: { text: "Strong evidence of reflecting effectively on own practice.", rewrite: light, force: describes, status: drafted }
  forBeneficiary: { text: "You reflect well on your own practice.", rewrite: full, force: describes, status: drafted }
- sentence: cardiffmet/generic-2020/l7/argument/70-79.s6
  forPractitioner: { text: "Highly perceptive evaluation of own work or practice; fully aware of what it means for development.", rewrite: light, force: describes, status: drafted }
  forBeneficiary: { text: "You evaluate your own work with sharp insight and see clearly what it means for how you develop.", rewrite: full, force: describes, status: drafted }
- sentence: cardiffmet/generic-2020/l7/argument/60-69.s1
  forPractitioner: { text: "Critically evaluates and reflects.", rewrite: light, force: describes, status: drafted }
  forBeneficiary: { text: "You evaluate and reflect critically.", rewrite: full, force: describes, status: drafted }
- sentence: cardiffmet/generic-2020/l7/argument/60-69.s2
  forPractitioner: { text: "Arguments considered and supported; judges fittingly among many interacting factors and suggests solutions.", rewrite: light, force: describes, status: drafted }
  forBeneficiary: { text: "Your arguments are considered and supported, and you judge well where many factors interact and suggest solutions.", rewrite: full, force: describes, status: drafted }
- sentence: cardiffmet/generic-2020/l7/argument/60-69.s3
  forPractitioner: { text: "Reflects on own practice and uses self-evaluation to plan development.", rewrite: light, force: describes, status: drafted }
  forBeneficiary: { text: "You reflect on your practice and use what you find to plan how to develop.", rewrite: full, force: describes, status: drafted }
- sentence: cardiffmet/generic-2020/l7/argument/50-59.s1
  forPractitioner: { text: "Limited critical evaluation and reflection.", rewrite: light, force: describes, status: drafted }
  forBeneficiary: { text: "You evaluate and reflect critically only a little.", rewrite: full, force: describes, status: drafted }
- sentence: cardiffmet/generic-2020/l7/argument/50-59.s2
  forPractitioner: { text: "Some critical reflection, but mostly description and fact.", rewrite: light, force: describes, status: drafted }
  forBeneficiary: { text: "You reflect critically a little, but your work is mostly description.", rewrite: full, force: describes, status: drafted }
- sentence: cardiffmet/generic-2020/l7/argument/50-59.s3
  forPractitioner: { text: "Arguments generally supported but thin.", rewrite: light, force: describes, status: drafted }
  forBeneficiary: { text: "Your arguments are generally supported but thin.", rewrite: full, force: describes, status: drafted }
- sentence: cardiffmet/generic-2020/l7/argument/50-59.s4
  forPractitioner: { text: "Some reflection on own practice, limited and superficial, with little thought for development.", rewrite: light, force: describes, status: drafted }
  forBeneficiary: { text: "You reflect on your practice, but only briefly and on the surface.", rewrite: full, force: describes, status: drafted }
- sentence: cardiffmet/generic-2020/l7/argument/40-49.s1
  forPractitioner: { text: "Little sign of critical evaluation and reflection.", rewrite: light, force: describes, status: drafted }
  forBeneficiary: { text: "You show little critical evaluation or reflection.", rewrite: full, force: describes, status: drafted }
- sentence: cardiffmet/generic-2020/l7/argument/40-49.s2
  forPractitioner: { text: "Largely descriptive; arguments, if tried, rarely supported.", rewrite: light, force: describes, status: drafted }
  forBeneficiary: { text: "Your work is largely descriptive, and any arguments are rarely supported.", rewrite: full, force: describes, status: drafted }
- sentence: cardiffmet/generic-2020/l7/argument/40-49.s3
  forPractitioner: { text: "Self-evaluation very limited.", rewrite: light, force: describes, status: drafted }
  forBeneficiary: { text: "You reflect on your own practice very little.", rewrite: full, force: describes, status: drafted }
- sentence: cardiffmet/generic-2020/l7/argument/20-39.s1
  forPractitioner: { text: "Some description and reporting, but very little sign of critical evaluation or reflection.", rewrite: light, force: describes, status: drafted }
  forBeneficiary: { text: "You describe and report a little but show almost no critical evaluation or reflection.", rewrite: full, force: describes, status: drafted }
- sentence: cardiffmet/generic-2020/l7/argument/20-39.s2
  forPractitioner: { text: "Self-evaluation negligible or absent.", rewrite: light, force: describes, status: drafted }
  forBeneficiary: { text: "You reflect on your own practice little or not at all.", rewrite: full, force: describes, status: drafted }
```

### AC6 Terms
<!-- The set's lexicon: count over all cells, levels, and count per common column (fail-low, fail-high, 40-49, 50-59, 60-69, 70-79, 80-100). Taxonomy placements from INGEST's revised Bloom and SOLO documents. -->

#### Performance verbs (lemma)

| Term | Count | Levels | By column (fail-low to 80-100) | Taxonomy |
|---|---|---|---|---|
| demonstrate | 129 | 3,4,5,6,7 | 20 15 20 22 21 26 5 | bloom-r: apply/understand |
| present | 78 | 3,4,5,6,7 | 7 10 16 24 7 12 2 | none |
| evaluate | 53 | 3,4,5,6,7 | 5 5 9 10 11 10 3 | bloom-r: analyze/create/evaluate; solo: extended-abstract |
| apply | 47 | 3,4,5,6,7 | 5 6 7 6 10 10 3 | bloom-r: apply; solo: relational |
| meet | 40 | 3,4,5,6,7 | 5 9 6 5 5 5 5 | none |
| extend | 36 | 3,4,5,6,7 | 1 1 1 1 9 3 20 | bloom-r: understand |
| communicate | 35 | 3,4,5,6,7 | 4 5 9 6 5 5 1 | none |
| develop | 32 | 3,4,5,6,7 | 0 0 6 7 7 12 0 | bloom-r: apply/create |
| solve | 29 | 3,4,5,6,7 | 3 3 3 3 8 8 1 | bloom-r: analyze/apply/create; solo: multistructural |
| use | 28 | 3,4,5,6,7 | 1 5 3 2 6 10 1 | bloom-r: apply |
| reflect | 27 | 3,4,5,6,7 | 2 2 8 8 2 5 0 | solo: extended-abstract |
| make | 26 | 3,4,5,6,7 | 0 0 3 3 12 8 0 | bloom-r: create |
| address | 25 | 3,4,5,6,7 | 0 0 5 5 5 5 5 | none |
| describe | 23 | 3,4,5,6,7 | 2 5 9 7 0 0 0 | bloom-r: evaluate/remember/understand; solo: multistructural |
| comment | 22 | 3,4,5,6,7 | 0 0 6 6 5 5 0 | none |
| undertake | 18 | 5,6,7 | 2 2 2 3 3 3 3 | none |
| interpret | 12 | 3,4 | 2 2 2 2 2 2 0 | bloom-r: apply/evaluate/understand; solo: extended-abstract/relational |
| transform | 11 | 4,5,6,7 | 1 1 1 1 4 3 0 | none |
| report | 8 | 3,4,5,6,7 | 2 1 4 1 0 0 0 | bloom-r: apply/understand; solo: multistructural |
| recognise | 8 | 3,4,5,6,7 | 0 0 0 0 0 8 0 | solo: unistructural |
| synthesise | 7 | 5,6,7 | 1 0 1 0 2 3 0 | bloom-r: create/evaluate |
| reproduce | 6 | 3,4,5,6 | 0 0 4 2 0 0 0 | bloom-r: remember; solo: unistructural |
| select | 6 | 3 | 1 1 1 1 1 1 0 | bloom-r: analyze/apply/evaluate/remember/understand; solo: multistructural |
| challenge | 6 | 4,5,6,7 | 0 0 0 0 0 4 2 | none |
| plan | 5 | 3,4,5,6,7 | 0 0 0 0 5 0 0 | bloom-r: create; solo: relational |
| consider | 5 | 3,4,5,6,7 | 0 0 4 1 0 0 0 | none |
| sustain | 4 | 4,5,6,7 | 0 0 0 0 0 4 0 | none |
| provide | 4 | 5,6,7 | 0 0 2 1 0 0 1 | none |
| conduct | 3 | 7 | 0 0 0 1 1 1 0 | solo: multistructural |
| review | 2 | 4 | 0 0 0 0 1 1 0 | bloom-r: evaluate/remember/understand; solo: relational |
| adapt | 2 | 6 | 0 0 0 0 1 1 0 | bloom-r: apply/create; solo: relational |

#### Objects

| Term | Count | Levels | By column (fail-low to 80-100) |
|---|---|---|---|
| knowledge | 112 | 3,4,5,6,7 | 13 15 17 17 23 23 4 |
| research | 73 | 3,4,5,6,7 | 4 6 10 18 15 15 5 |
| arguments | 53 | 3,4,5,6,7 | 1 9 8 9 10 15 1 |
| understanding | 50 | 3,4,5,6,7 | 6 7 7 7 8 9 6 |
| discipline | 49 | 3,4,5,6,7 | 6 8 7 7 7 7 7 |
| sources | 46 | 3,4,5,6,7 | 5 9 6 6 10 10 0 |
| scholarship | 43 | 3,4,5,6,7 | 4 5 9 10 5 5 5 |
| learning outcomes | 41 | 3,4,5,6,7 | 6 9 6 5 5 5 5 |
| set task | 36 | 3,4,5,6,7 | 6 5 5 5 5 5 5 |
| field of study | 36 | 3,4,5,6,7 | 4 6 6 5 5 5 5 |
| presentation | 36 | 3,4,5,6,7 | 5 6 9 9 0 5 2 |
| assessment criteria | 35 | 3,4,5,6,7 | 4 5 6 5 5 5 5 |
| knowledge and understanding | 35 | 3,4,5,6,7 | 8 7 8 3 2 6 1 |
| concepts | 32 | 3,4,5,6,7 | 3 4 3 3 8 10 1 |
| reading | 32 | 3,4,5,6,7 | 4 5 5 5 5 5 3 |
| information | 29 | 3,4,5,6,7 | 2 2 11 8 3 3 0 |
| literature | 29 | 3,4,5,6,7 | 4 5 5 4 5 5 1 |
| referencing | 28 | 3,4,5,6,7 | 4 5 5 4 5 5 0 |
| research processes | 28 | 3,4,5,6,7 | 4 5 5 4 5 5 0 |
| problems | 25 | 3,4,5,6,7 | 2 2 2 2 8 8 1 |
| own practice | 25 | 3,4,5,6,7 | 4 5 5 6 0 5 0 |
| qualitative and quantitative data | 21 | 3,4,5,6 | 4 4 3 3 3 4 0 |
| ideas | 21 | 3,4,5,6,7 | 1 6 7 3 2 2 0 |
| techniques | 20 | 3,4,5,6,7 | 0 0 1 2 5 9 3 |
| approaches | 15 | 3,4,5 | 2 2 2 2 3 4 0 |
| principles | 11 | 5 | 1 2 2 2 2 2 0 |
| structure | 10 | 3,4,5,6,7 | 4 2 0 4 0 0 0 |
| lines of argument | 8 | 3,4 | 0 0 2 2 2 2 0 |
| basic theories and concepts | 8 | 3,4 | 0 0 2 2 2 2 0 |
| theory and practice | 8 | 4,5,6,7 | 0 0 0 0 4 4 0 |
| academic conventions | 6 | 3,4,5,6,7 | 0 0 1 0 0 5 0 |
| complex problems | 6 | 5 | 1 1 1 1 1 1 0 |
| primary sources | 5 | 3,4,5,6,7 | 0 0 0 0 0 5 0 |
| limitations | 4 | 4,5,6,7 | 0 0 0 0 0 4 0 |
| data | 2 | 6,7 | 0 0 0 0 0 2 0 |

#### Qualifiers of degree

| Term | Count | Levels | By column (fail-low to 80-100) |
|---|---|---|---|
| some | 73 | 3,4,5,6,7 | 1 16 19 29 7 1 0 |
| limited | 58 | 3,4,5,6,7 | 4 27 21 4 1 1 0 |
| little | 36 | 3,4,5,6,7 | 21 8 6 1 0 0 0 |
| detailed | 25 | 3,4,5,6,7 | 0 0 0 0 6 14 5 |
| basic | 20 | 3,4,5,6,7 | 0 5 12 1 1 1 0 |
| generally | 18 | 3,4,5,6,7 | 0 0 8 10 0 0 0 |
| clearly | 15 | 3,4,5,6,7 | 0 2 1 0 7 5 0 |
| well | 15 | 3,4,5,6,7 | 0 0 0 0 10 5 0 |
| secure | 13 | 3,4,5,6,7 | 0 0 4 5 4 0 0 |
| sound | 13 | 3,4,5,6 | 0 0 2 7 2 2 0 |
| highly | 12 | 3,4,5,6,7 | 0 0 0 1 1 10 0 |
| clear | 11 | 3,4,5,6,7 | 0 0 4 0 4 3 0 |
| successfully | 11 | 3,4,5,6,7 | 0 0 0 1 5 5 0 |
| strong | 10 | 3,4,5,6,7 | 0 0 0 0 0 10 0 |
| successful | 10 | 3,4,5,6,7 | 0 0 0 4 1 5 0 |
| satisfactory | 9 | 3,4,5,6,7 | 0 0 0 9 0 0 0 |
| thorough | 9 | 5,6,7 | 0 0 0 0 3 6 0 |
| exceptional | 8 | 3,4,5,6,7 | 0 0 0 0 0 0 8 |
| good | 8 | 3,4,5,6,7 | 0 0 0 0 8 0 0 |
| very good | 7 | 3,4,5,6,7 | 0 0 0 0 0 7 0 |
| poor | 7 | 3,4,5,6,7 | 7 0 0 0 0 0 0 |
| minimal | 7 | 3,4,5,6,7 | 6 1 0 0 0 0 0 |
| confident | 7 | 3,4,5,6 | 0 0 0 0 0 7 0 |
| informed | 7 | 5,6,7 | 0 0 0 0 0 2 5 |
| excellent | 6 | 3,4,5,6,7 | 0 0 0 0 0 1 5 |
| outstanding | 5 | 3,4,5,6,7 | 0 0 0 0 0 0 5 |
| high | 5 | 3,4,5,6,7 | 0 0 0 0 0 5 0 |
| very limited | 5 | 3,4,5,6,7 | 4 1 0 0 0 0 0 |
| effectively | 5 | 3,4,5,6,7 | 0 0 0 0 0 5 0 |
| perceptively | 5 | 4,5,6,7 | 0 0 0 0 1 4 0 |
| innovative | 5 | 5,6,7 | 0 0 0 0 0 3 2 |
| perceptive | 4 | 4,5,6,7 | 0 0 0 0 0 4 0 |
| mastery | 4 | 7 | 0 0 0 1 1 1 1 |
| very little | 3 | 5,6,7 | 2 1 0 0 0 0 0 |
| sophisticated | 2 | 7 | 0 0 0 0 0 2 0 |
| consistently | 2 | 7 | 0 0 0 0 0 0 2 |

#### Independence

| Term | Count | Levels | By column (fail-low to 80-100) |
|---|---|---|---|
| independent thinking | 15 | 3,4,5,6,7 | 0 0 0 5 5 5 0 |
| reliance on tutor support | 4 | 3,4,5,6 | 0 0 0 4 0 0 0 |
| independent | 2 | 7 | 0 0 0 0 0 0 2 |

#### Scope

| Term | Count | Levels | By column (fail-low to 80-100) |
|---|---|---|---|
| complex | 40 | 3,4,5,6,7 | 3 7 8 5 7 9 1 |
| basic | 34 | 3,4,5,6,7 | 1 6 14 3 5 5 0 |
| current | 32 | 3,4,5,6,7 | 4 5 5 5 5 5 3 |
| advanced | 22 | 3,4,5,6,7 | 0 2 2 4 4 7 3 |
| key | 17 | 3,4,5,6,7 | 0 0 4 1 6 6 0 |
| well-defined | 17 | 3,4,5,6,7 | 2 2 2 2 2 7 0 |
| a range of | 17 | 5,6,7 | 1 2 3 3 4 4 0 |
| non-routine | 12 | 3,4 | 2 2 2 2 2 2 0 |
| at this level | 9 | 3,4,5,6,7 | 0 0 4 0 0 5 0 |
| specialised | 6 | 7 | 0 0 0 2 2 2 0 |
| beyond level | 5 | 3,4,5,6,7 | 0 0 0 0 0 0 5 |
| original | 4 | 4,5,6,7 | 0 0 0 0 0 4 0 |
| main | 3 | 5,6,7 | 0 0 0 0 0 0 3 |
| systematic | 3 | 6 | 0 0 0 0 0 2 1 |
| specialist | 1 | 7 | 0 0 0 0 0 0 1 |
| unfamiliar | 1 | 7 | 0 0 0 0 0 0 1 |
| forefront | 1 | 7 | 0 0 0 0 0 0 1 |

#### Negations and deficits

| Term | Count | Levels | By column (fail-low to 80-100) |
|---|---|---|---|
| errors | 32 | 3,4,5,6,7 | 5 9 10 8 0 0 0 |
| not | 21 | 3,4,5,6,7 | 0 6 6 9 0 0 0 |
| misconceptions | 18 | 3,4,5,6,7 | 4 5 5 4 0 0 0 |
| over-reliance | 14 | 3,4,5,6,7 | 0 4 5 5 0 0 0 |
| irrelevant | 12 | 3,4,5,6,7 | 6 5 1 0 0 0 0 |
| unaddressed | 10 | 3,4,5,6,7 | 4 5 1 0 0 0 0 |
| inaccuracies | 10 | 3,4,5,6,7 | 4 5 1 0 0 0 0 |
| absent | 10 | 3,4,5,6,7 | 8 2 0 0 0 0 0 |
| negligible | 10 | 3,4,5,6,7 | 8 2 0 0 0 0 0 |
| lack | 6 | 3,4,5,6,7 | 1 0 0 5 0 0 0 |
| confused | 5 | 3,4,5,6,7 | 0 4 1 0 0 0 0 |
| clumsy | 5 | 3,4,5,6,7 | 4 1 0 0 0 0 0 |
| naïve | 5 | 3,4,5,6,7 | 0 4 1 0 0 0 0 |
| simplistic | 5 | 3,4,5,6,7 | 0 4 1 0 0 0 0 |
| unconvincing | 5 | 3,4,5,6,7 | 0 4 1 0 0 0 0 |
| failure | 5 | 3,4,5,6,7 | 4 1 0 0 0 0 0 |
| superficial | 5 | 3,4,5,6,7 | 0 0 4 1 0 0 0 |
| no | 4 | 3,7 | 4 0 0 0 0 0 0 |
| reliance | 4 | 3,4,5,6 | 0 0 0 4 0 0 0 |
| none | 2 | 4,5 | 2 0 0 0 0 0 0 |
| insufficient | 2 | 5,7 | 0 1 1 0 0 0 0 |
| inconsistent | 1 | 7 | 0 0 1 0 0 0 0 |

#### AC6.1 The set's ladders
<!-- Each degree and independence term used three or more times, placed by the mean column it appears in (0 = fail-low, 6 = 80-100). -->

| Mean column | Term | Kind | Count |
|---|---|---|---|
| 0.0 (fail-low) | poor | degree | 7 |
| 0.1 (fail-low) | minimal | degree | 7 |
| 0.2 (fail-low) | very limited | degree | 5 |
| 0.3 (fail-low) | very little | degree | 3 |
| 0.6 (fail-high) | little | degree | 36 |
| 1.6 (40-49) | limited | degree | 58 |
| 2.0 (40-49) | basic | degree | 20 |
| 2.4 (40-49) | some | degree | 73 |
| 2.6 (50-59) | generally | degree | 18 |
| 3.0 (50-59) | reliance on tutor support | independence | 4 |
| 3.0 (50-59) | satisfactory | degree | 9 |
| 3.0 (50-59) | secure | degree | 13 |
| 3.3 (50-59) | sound | degree | 13 |
| 3.5 (60-69) | clear | degree | 11 |
| 3.8 (60-69) | clearly | degree | 15 |
| 4.0 (60-69) | good | degree | 8 |
| 4.0 (60-69) | independent thinking | independence | 15 |
| 4.1 (60-69) | successful | degree | 10 |
| 4.3 (60-69) | well | degree | 15 |
| 4.4 (60-69) | successfully | degree | 11 |
| 4.5 (60-69) | mastery | degree | 4 |
| 4.7 (70-79) | thorough | degree | 9 |
| 4.8 (70-79) | highly | degree | 12 |
| 4.8 (70-79) | perceptively | degree | 5 |
| 5.0 (70-79) | detailed | degree | 25 |
| 5.0 (70-79) | confident | degree | 7 |
| 5.0 (70-79) | effectively | degree | 5 |
| 5.0 (70-79) | high | degree | 5 |
| 5.0 (70-79) | perceptive | degree | 4 |
| 5.0 (70-79) | strong | degree | 10 |
| 5.0 (70-79) | very good | degree | 7 |
| 5.4 (70-79) | innovative | degree | 5 |
| 5.7 (80-100) | informed | degree | 7 |
| 5.8 (80-100) | excellent | degree | 6 |
| 6.0 (80-100) | exceptional | degree | 8 |
| 6.0 (80-100) | outstanding | degree | 5 |

#### AC6.2 Modality
<!-- How firmly each level states its descriptors: cells opening "May demonstrate" (or containing "may") against plain statements. -->

| Level | Cells | Opening "May demonstrate" | Containing "may" |
|---|---|---|---|
| 3 | 35 | 30 | 30 |
| 4 | 35 | 30 | 30 |
| 5 | 35 | 0 | 13 |
| 6 | 35 | 0 | 14 |
| 7 | 31 | 0 | 11 |

### AC7 Progressions

#### AC7.1 Across bands within a level
<!-- Degree, independence and deficit words per band, summed over the six rows. -->

**Level 3**

| Band | Degree | Independence | Deficits |
|---|---|---|---|
| 80%-100% (1st Class +) | detailed 1, excellent 1, outstanding 1, exceptional 1 | (none) | (none) |
| 70%-79% (1st) | detailed 2, strong 2, very good 1, confident 1, sound 1, high 1 | independent thinking 1 | (none) |
| 60%-69% (2:1) | well 2, good 1, detailed 1, clear 1, successfully 1, sound 1 | independent thinking 1 | (none) |
| 50%-59% (2:2) | some 7, sound 2, generally 2, secure 1, satisfactory 1, successful 1 | independent thinking 1, reliance on tutor support 1 | errors 2, not 2, misconceptions 1, reliance 1, over-reliance 1, lack 1 |
| 40%-49% (3rd) | limited 5, basic 2, generally 2, some 2, sound 1, clear 1 | (none) | errors 2, misconceptions 1, not 1, over-reliance 1, superficial 1 |
| 30-39% (Narrow Fail) | limited 7, some 3, basic 1, clearly 1, little 1 | (none) | not 2, errors 2, unaddressed 1, inaccuracies 1, misconceptions 1, irrelevant 1 |
| 1-29% (Clear Fail) | little 5, poor 1, minimal 1, limited 1, very limited 1 | (none) | absent 2, negligible 2, no 1, unaddressed 1, inaccuracies 1, errors 1 |

**Level 4**

| Band | Degree | Independence | Deficits |
|---|---|---|---|
| 80%-100% (1st Class +) | detailed 1, excellent 1, outstanding 1, exceptional 1 | (none) | (none) |
| 70%-79% (1st) | detailed 2, strong 2, confident 2, highly 2, very good 1, sound 1 | independent thinking 1 | (none) |
| 60%-69% (2:1) | some 2, well 2, good 1, detailed 1, clear 1, successfully 1 | independent thinking 1 | (none) |
| 50%-59% (2:2) | some 6, sound 2, generally 2, secure 1, satisfactory 1, successful 1 | independent thinking 1, reliance on tutor support 1 | errors 2, not 2, misconceptions 1, reliance 1, over-reliance 1, lack 1 |
| 40%-49% (3rd) | limited 5, basic 2, generally 2, some 2, sound 1, clear 1 | (none) | errors 2, misconceptions 1, not 1, over-reliance 1, superficial 1 |
| 30-39% (Narrow Fail) | limited 7, some 3, basic 1, clearly 1, little 1 | (none) | not 2, errors 2, unaddressed 1, inaccuracies 1, misconceptions 1, irrelevant 1 |
| 1-29% (Clear Fail) | little 5, poor 1, minimal 1, limited 1, very limited 1 | (none) | absent 2, negligible 2, none 1, unaddressed 1, inaccuracies 1, errors 1 |

**Level 5**

| Band | Degree | Independence | Deficits |
|---|---|---|---|
| 80%-100% (1st Class +) | detailed 1, excellent 1, outstanding 1, exceptional 1, informed 1 | (none) | (none) |
| 70%-79% (1st) | detailed 3, very good 2, strong 2, confident 2, highly 2, thorough 2 | independent thinking 1 | (none) |
| 60%-69% (2:1) | good 4, well 2, detailed 1, successfully 1, successful 1, perceptively 1 | independent thinking 1 | (none) |
| 50%-59% (2:2) | satisfactory 4, some 4, generally 2, secure 1, sound 1, successful 1 | independent thinking 1, reliance on tutor support 1 | errors 2, not 2, misconceptions 1, reliance 1, over-reliance 1, lack 1 |
| 40%-49% (3rd) | basic 6, some 5, generally 2, limited 2, clear 1, secure 1 | (none) | errors 2, misconceptions 1, not 1, over-reliance 1, superficial 1 |
| 30-39% (Narrow Fail) | limited 5, some 4, little 2, basic 1 | (none) | errors 2, not 1, unaddressed 1, insufficient 1, inaccuracies 1, misconceptions 1 |
| 1-29% (Clear Fail) | little 6, poor 1, minimal 1, some 1, limited 1, very limited 1 | (none) | absent 2, negligible 2, none 1, unaddressed 1, inaccuracies 1, errors 1 |

**Level 6**

| Band | Degree | Independence | Deficits |
|---|---|---|---|
| 80%-100% (1st Class +) | exceptional 2, informed 2, detailed 1, excellent 1, outstanding 1, innovative 1 | (none) | (none) |
| 70%-79% (1st) | detailed 4, very good 2, strong 2, confident 2, highly 2, thorough 2 | independent thinking 1 | (none) |
| 60%-69% (2:1) | detailed 2, thorough 2, some 2, clearly 2, well 2, good 1 | independent thinking 1 | (none) |
| 50%-59% (2:2) | some 6, satisfactory 2, sound 2, generally 2, secure 1, successfully 1 | independent thinking 1, reliance on tutor support 1 | errors 2, not 2, misconceptions 1, reliance 1, over-reliance 1, lack 1 |
| 40%-49% (3rd) | some 6, limited 4, basic 2, generally 2, clear 1, secure 1 | (none) | errors 2, misconceptions 1, not 1, over-reliance 1, superficial 1 |
| 30-39% (Narrow Fail) | limited 6, some 4, basic 1, little 1 | (none) | errors 2, not 1, unaddressed 1, inaccuracies 1, misconceptions 1, irrelevant 1 |
| 1-29% (Clear Fail) | little 5, poor 1, minimal 1, limited 1, very limited 1, very little 1 | (none) | absent 2, negligible 2, unaddressed 1, inaccuracies 1, errors 1, misconceptions 1 |

**Level 7**

| Band | Degree | Independence | Deficits |
|---|---|---|---|
| 80%-100% (Distinction+) | exceptional 3, consistently 2, informed 2, detailed 1, excellent 1, outstanding 1 | independent 2 | (none) |
| 70%-79% (Distinction) | detailed 3, highly 3, strong 2, sophisticated 2, thorough 2, very good 1 | independent thinking 1 | (none) |
| 60%-69% (Merit) | some 3, clearly 2, well 2, good 1, mastery 1, clear 1 | independent thinking 1 | (none) |
| 50%-59% (Pass) | some 6, limited 4, generally 2, basic 1, secure 1, mastery 1 | independent thinking 1 | lack 1, not 1, over-reliance 1, superficial 1 |
| 40%-49% (Narrow Fail) | limited 5, some 4, little 2, clearly 1 | (none) | not 2, errors 2, insufficient 1, unaddressed 1, inaccuracies 1, misconceptions 1 |
| 20-39% (Clear Fail) | little 3, some 2, limited 2, minimal 1, basic 1, very limited 1 | (none) | absent 2, negligible 2, unaddressed 1, inaccuracies 1, errors 1, misconceptions 1 |
| 1-19% | poor 3, minimal 2 | (none) | no 3, irrelevant 2, lack 1, errors 1 |

#### AC7.2 Across levels within a band
<!-- For each criterion, the scope and object words of the pass band (40-49 at levels 3 to 6, 50-59 at level 7) and of the 70-79 band, by level. -->

| Criterion | Band | L3 | L4 | L5 | L6 | L7 |
|---|---|---|---|---|---|---|
| Overall summary | pass | basic, understanding, set task, learning outcomes, assessment criteria | basic, understanding, set task, learning outcomes, assessment criteria | basic, understanding, set task, learning outcomes, assessment criteria | basic, understanding, set task, learning outcomes, assessment criteria | basic, understanding, set task, learning outcomes, assessment criteria |
| Overall summary | 70-79 | understanding, set task, learning outcomes, assessment criteria | understanding, set task, learning outcomes, assessment criteria | understanding, set task, learning outcomes, assessment criteria | understanding, set task, learning outcomes, assessment criteria | understanding, set task, learning outcomes, assessment criteria |
| Knowledge & Understanding | pass | basic, at this level, knowledge, field of study, information, knowledge and understanding | basic, at this level, knowledge, field of study, information, knowledge and understanding | basic, at this level, knowledge, understanding, concepts, principles, field of study, information, knowledge and understanding | basic, at this level, knowledge and understanding, field of study, information | complex, specialised, knowledge, sources, independent thinking |
| Knowledge & Understanding | 70-79 | basic, at this level, knowledge, field of study, concepts, perspectives, approaches, independent thinking | basic, original, at this level, knowledge, field of study, concepts, limitations, independent thinking | complex, original, at this level, knowledge, understanding, concepts, principles, field of study, limitations, independent thinking | systematic, key, complex, original, at this level, knowledge, understanding, field of study, concepts, limitations, independent thinking | complex, specialised, original, at this level, knowledge, concepts, limitations, independent thinking |
| Presentation and communication | pass | basic, complex, key, qualitative and quantitative data, lines of argument, basic theories and concepts, information, ideas, presentation | basic, complex, key, qualitative and quantitative data, lines of argument, basic theories and concepts, information, ideas, presentation | basic, a range of, complex, key, information, arguments, ideas, presentation | a range of, complex, key, information, ideas, concepts, arguments, presentation | complex, information, research, ideas, concepts, arguments |
| Presentation and communication | 70-79 | basic, key, well-defined, qualitative and quantitative data, lines of argument, basic theories and concepts, presentation, arguments | basic, key, well-defined, qualitative and quantitative data, lines of argument, basic theories and concepts, presentation, arguments | a range of, key, well-defined, information, arguments, presentation | complex, a range of, key, well-defined, information, ideas, concepts, presentation, arguments | complex, a range of, key, well-defined, information, ideas, research, concepts, presentation, arguments |
| Analysis & discussion | pass | well-defined, complex, non-routine, approaches, problems | well-defined, complex, non-routine, approaches, problems | basic, a range of, qualitative and quantitative data, techniques, knowledge | discipline, knowledge | advanced, specialised, research, discipline |
| Analysis & discussion | 70-79 | well-defined, complex, non-routine, approaches, problems, techniques | well-defined, complex, non-routine, approaches, problems, theory and practice | a range of, qualitative and quantitative data, techniques, theory and practice, knowledge | qualitative and quantitative data, discipline, techniques, theory and practice, knowledge | advanced, specialised, research, discipline, techniques, theory and practice |
| Research / scholarship | pass | current, advanced, research, scholarship, discipline, reading, referencing, literature, sources, knowledge, research processes | current, advanced, research, scholarship, discipline, reading, referencing, literature, sources, knowledge, research processes | basic, current, knowledge, research, scholarship, discipline, reading, referencing, literature, sources, research processes | current, knowledge and understanding, research, scholarship, discipline, reading, referencing, literature, sources, knowledge, research processes | current, knowledge and understanding, research, scholarship, discipline, sources, arguments, reading |
| Research / scholarship | 70-79 | current, advanced, research, scholarship, discipline, primary sources, reading, sources, referencing, literature, academic conventions, knowledge and understanding, research processes, techniques, knowledge | current, advanced, research, scholarship, discipline, primary sources, reading, sources, referencing, literature, academic conventions, knowledge and understanding, research processes, techniques, knowledge | current, advanced, knowledge, research, scholarship, discipline, primary sources, reading, sources, referencing, literature, academic conventions, knowledge and understanding, research processes, techniques | systematic, current, advanced, knowledge, understanding, research, scholarship, discipline, primary sources, reading, sources, referencing, literature, academic conventions, knowledge and understanding, research processes, techniques | current, advanced, knowledge and understanding, research, scholarship, discipline, primary sources, reading, sources, referencing, literature, academic conventions, research processes, techniques, knowledge |
| Structured argument and critical evaluation | pass | presentation, arguments, own practice | presentation, arguments, own practice | basic, complex, complex problems, understanding, principles, field of study, presentation, arguments, own practice | presentation, arguments, own practice | presentation, arguments, own practice |
| Structured argument and critical evaluation | 70-79 | arguments, problems, own practice | basic, arguments, problems, own practice | complex, complex problems, understanding, principles, field of study, arguments, problems, approaches, own practice | concepts, arguments, data, problems, own practice | concepts, arguments, data, problems, own practice |

#### AC7.3 Our reading
<!-- label: editorial; status: drafted; basis: primary (from AC5 to AC7) -->
- **The bands are named by class.** Each band carries its UK classification (1st Class +, 1st, 2:1, 2:2, 3rd, Narrow Fail, Clear Fail; at level 7 Distinction+, Distinction, Merit, Pass, Narrow Fail, Clear Fail). The marriage to the UK scale is in the labels themselves.
- **The overall summary is a ladder of one adjective.** Every level's summary row reads the same frame, "understanding of the set task" and outcomes met "at a ... level", and only the adjective moves: minimal, partial, basic (threshold), secure (satisfactory), full (good), full and detailed (very good), then excellent or outstanding. It is the plainest degree ladder in either set.
- **The degree ladder, read from counts:** poor, minimal, very limited (clear fail); little (fail); limited, basic, some (third); generally, satisfactory, secure, sound (2:2); clear, good, successful, well (2:1); thorough, detailed, confident, strong, highly, perceptive (first); excellent, exceptional, outstanding (80-100). Bristol's ladder and this one agree in order where they share words (limited, some, sound, good, thorough, excellent, exceptional).
- **Independence is thin.** Only "independent thinking" (2:2 to first) and "reliance on tutor support" (2:2) grade independence; Bristol grades guidance and autonomy band by band. Cardiff Met grades by quality and by the balance of description against argument ("over-reliance on description", "largely descriptive").
- **The pass bands are not deficit-free, against the issuer's own rule.** The guidance says pass descriptors are positive and that no band says what it lacks; yet the 40-49 cells carry errors, misconceptions, superficial reflection and over-reliance on programme materials (0.93 deficit terms per pass-band cell; Bristol 0.10). Above the pass band Cardiff Met still hedges (0.28; Bristol 0).
- **Modality falls away with level.** Levels 3 and 4 open nearly every cell with "May demonstrate"; levels 5 to 7 state "Demonstrates" (AC6.2). A modal descriptor describes what might be seen, a plain one what is.
- **The levels borrow the frameworks' wording.** Level 3 and 4 presentation cells carry the FHEQ Level 4 descriptor almost whole (4.10's present, evaluate and interpret data to argue from basic theory: 35 words); level 5 carries 4.12's communication to specialist and non-specialist audiences and the limits of knowledge; level 6 and 7 argument and research cells take short CQFW phrases ("limited definition", "many interacting factors", "determine, refine, adapt and use"), below the seven-word echo line. Level 3, a foundation level, is written in FHEQ Level 4's words.
- **The top band is mostly a formula.** At levels 3 and 4 every criterion's 80-100 cell says only that the work goes beyond the 70-79 band and the level; from level 5 some criteria add a real descriptor (own research design, citations beyond the usual reading, new insights, professional presentation, publishable work at level 6).
- **One paragraph per cell.** A cell runs to 30 to 120 words in several sentences, each grading a different quality; so each cell is also cut into its sentences (AC5a; D-std-0008), the unit a marker reads.


### AC8 Fields
```yaml
- { criterion: "Overall summary", fields: [{ field: "Overall summary", basis: stated }] }
- { criterion: "Knowledge & Understanding", fields: [{ field: "Knowledge & Understanding", basis: stated }, { field: criticality, basis: inferred }] }
- { criterion: "Presentation and communication", fields: [{ field: "Presentation and communication", basis: stated }, { field: academic-writing, basis: inferred }, { field: presenting, basis: inferred }] }
- { criterion: "Analysis & discussion", fields: [{ field: "Analysis & discussion", basis: stated }, { field: criticality, basis: inferred }, { field: researching-and-research-methods, basis: inferred }] }
- { criterion: "Research / scholarship", fields: [{ field: "Research / scholarship", basis: stated }, { field: finding-and-using-sources, basis: inferred }, { field: referencing, basis: inferred }, { field: researching-and-research-methods, basis: inferred }] }
- { criterion: "Structured argument and critical evaluation", fields: [{ field: "Structured argument and critical evaluation", basis: stated }, { field: criticality, basis: inferred }, { field: reflective-practice, basis: inferred }, { field: academic-writing, basis: inferred }] }
```

## Part B Terminology
<!-- label: both; status: drafted; basis: primary -->
```yaml
- { term: "Generic Band Descriptors (GBDs)", gloss: "the issuer's university-wide descriptions of attainment in each 10% band, by level", basis: paraphrase }
- { term: "band descriptor", gloss: "the issuer's preferred term over grade descriptor, since marks are percentages grouped into bands", basis: paraphrase }
- { term: "discipline-specific band descriptors", gloss: "descriptors written by programmes or schools for the context of a task, used alongside the generic ones", basis: paraphrase }
- { term: "best fit", gloss: "placing work that shows features of two neighbouring bands by professional judgement", basis: paraphrase }
- { term: "narrow fail, clear fail", gloss: "the issuer's names for the 30-39 and 1-29 bands (undergraduate) and 40-49 and 20-39 bands (level 7)", basis: paraphrase }
- { term: "simplified Grade Band Descriptors", gloss: "shorter versions for staff and students, linked from the guidance, not held", basis: paraphrase }
```

## Part C Process
<!-- label: both; status: drafted; basis: primary -->

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
  held: fa71198a33ce25fed3163787a16d9a8dfa79f6dc8f25cbe328399a0ffe833613
  heldFiles: [wkspc2601-library/txt/cardiff-metropolitan-university-2020-generic-band-descriptors-standard.txt, wkspc2601-library/txt/cardiff-metropolitan-university-2020-generic-band-descriptors-standard.norm.txt, wkspc2601-library/records/<name>.held.json]
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
- { w: W-std-0007, citation: "the simplified Grade Band Descriptors for levels 3 to 7 (linked from the guidance)", settles: [AC5, S4a], asked: not yet, state: wanted }
- { w: W-std-0008, citation: "the current published version of AH1 4.3, if reviewed after November 2020", settles: [S1], asked: not yet, state: wanted }
```

## Part E Gaps and questions
- Name: `ingest-std-cardiffmet-generic-2020-assesscriteria`, the year being version 6's last review (November 2020); the file was saved in August 2026 and belongs to the 2026/27 handbook. For Abbott: 2020 or 2026? The issuer code (`cardiffmet`) waits on D-std-0007's open part.
- AC2: level 3 is linked to CQFW level 3 by inference; levels 4 to 7 to the FHEQ as the issuer states (aligned with the FHEQ of November 2014, now replaced by the 2024 edition).
- AC3: bands kept in the issuer's order (highest first); our `axis` puts 1-29 and 1-19 under fail-low and 30-39 and 20-39 under fail-high so the two sets compare.
- AC4 and AC5: at level 7 the 1-19 band has one band-wide cell, in the Knowledge & Understanding row; the four cells below it are empty (merged), recorded with `spans`.
- AC5, `versionsFrom`: `sameAs` when the text matches with level numbers masked; `like` when the same criterion and band at an earlier level matches with word similarity 0.95 or more. 210 cells: 143 with their own cell paraphrase.
- AC5 and AC5a, cut: each cell is a record (AC5) and is cut into its sentences (AC5a), each sentence with its own terms and versions (Abbott, 05:18; D-std-0008). 550 sentences, 285 with their own versions. The split is at a full stop followed by a capital; the issuer's "practice. own practice" slip stays inside one sentence.
- AC6: terms found by `ac_terms.py`; "may" counted in AC6.2, not as a degree word.
- AC1: the guidance says the two top bands are "supplemented by characteristics" likely to be present; the tables hold no separate list, and the simplified descriptors are not held (D3).
- Issuer slips kept as held: a doubled "own practice. own practice but" in the 2:2 argument cell (levels 3, 4); "limited knowledge of research processes may evident" (level 3); "The students demonstrates" (level 7).
- The two programme specification templates (AH2 1.2B, 1.2C) hold no criteria and are not ingested.

---

## Change notes
- 0.2.1, 3 October 2026, 21:02: moved with its held text from UNI to the source library repo (`wkspc2601-library/ingested/standards/`; texts in `txt/`, records in `records/`); paths only (Abbott, 20:56; std N-0119).
- 0.2.0, 3 October 2026, 11:00: every statement record now carries the issuer's statement in full (`source`, taken from its span in the held text) beside our paraphrase and versions, for language analysis; private, never published (Abbott, 10:56 and 10:59; D-std-0014). No paraphrase changed.
- 0.1.1, 3 October 2026, 07:34: provenance lines added to Parts B and C and S; wanted sources in D3 given their W-std ids from the wanted-sources list (the ingest tool's G3 and G7 warnings; std N-0100). No statement changed.
- 0.1.0: 2026-10-03: researched by run frame 0.1.1-draft and standards run layer 0.5.0-draft under the assessment-criteria template 0.1.0-draft, std, run 0051 (P1).
