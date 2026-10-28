---
id: std:doc:advancehe-psf-descriptors-2023-framework
title: "Professional Standards Framework 2023: the Descriptors D1 to D4 and the recognition they lead to"
profile: standards/framework
profileVersion: 0.2.0-draft
issuer: Advance HE (copyright jointly Advance HE, GuildHE and Universities UK)
kind: professional-standards-framework   # proposed kind (Part E; for nts)
jurisdiction: [UK]   # the document states none; Advance HE recognition is UK-based and used internationally (inferred, Part E)
subjectScope: universal
subjects: []
edition: 2023
published: 2023
status: current   # as at the held text; not checked against Advance HE's site (Part E)
supersedes: "not stated in the document; known to replace the UK Professional Standards Framework (UKPSF) of 2011 (std's knowledge, P2 to confirm)"
heldText: { method: sha256-bytes, raw: 121f42258ca8d09c00a9711ae1f58fbb4ff2371d420c9de1d58dc7d4adfa58a1, normalised: a9e6d56f13d921265859cbfefff9c90e6399b4ba8a09ca01f519d69e660740e3 }
original: { method: sha256-bytes, pdf: 3b79bcff1e3ce2533ff2a6f6e74332b3dfcb95a483c718dace6580e976e0a396, held: no }   # supplied files stay out of UNI (nts N-1020)
frameworkKind: professional-standards   # proposed value (Part E)
nations: [UK]
levels: [psf:d1, psf:d2, psf:d3, psf:d4]   # staff categories of practice; not on the qualification spine (S9)
awards: [Associate Fellow, Fellow, Senior Fellow, Principal Fellow]   # Advance HE recognition, as each Descriptor states
credit: none-stated
knowledgePath: { practice: "01 education", stream: "01_03 learning and teaching", reference: "professional recognition (code to issue)", unit: "professional standards framework (ST code to issue)" }   # Abbott, 09:49
licence: "All rights reserved (© Advance HE, GuildHE, Universities UK 2023); reproduction only with the copyright holders' permission. Held and rephrased on Abbott's permission (S1)"
agentUse: source-and-rephrased   # each record carries the issuer's statement (`source`) for language analysis and our rephrasings for agent phrasing; private, never published (Abbott, 10:18, 10:56; D-std-0014)
parts:
  S: "full for the Descriptors and the recognition page (pages 6 to 11); the purpose, the Dimensions and the terms are held once in std:doc:advancehe-psf-dimensions-2023-framework"
  B: full
  C: "not-applicable: the document sets out standards, not a procedure; the recognition route is summarised in S2"
pins: { structure: 0.13.0-draft, template: 0.6.1-draft, framework: 0.1.1-draft, runFrame: 0.1.1-draft, runLayer: 0.6.1-draft, standards: none yet, terminology: none yet }
lifecycle: drafted
researchedBy: run frame 0.1.1-draft; standards run layer 0.6.1-draft; std, run 0068
passes:
  P1: "2026-10-03, std (Claude Code, META Project)"
  P2: "skipped: read direct from the issuer's PDF; the 2011 predecessor and Advance HE's own guidance per Descriptor are wanted (D3)"
  P3: open
version: 0.1.2
usesIds: "psf:V1 to psf:A5, defined in std:doc:advancehe-psf-dimensions-2023-framework"
---

<!-- from INGEST wpk-0016-ingest-pd-template-standards.md 0.6.1-draft under the standards/framework variant (framework template 0.1.1-draft; profile 0.2.0-draft). One of two documents for the PSF 2023, split by Abbott (10:20): this one holds the Descriptors; the purpose, Dimensions and terms are in the companion (D-std-0013, framework rule 4) -->
# Professional Standards Framework 2023: the Descriptors D1 to D4

> Run 0068, P1 by std. Held by permission (S1). Private to the project, never published. Each S4 record carries the issuer's statement in full (`source`) for language analysis, with its character span in the held text (`wkspc2601-library/txt/advance-he-2023-professional-standards-framework-standard.norm.txt`), and our rephrasings (`paraphrase`, S4a), which are what agents phrase from (Abbott, 10:18 and 10:56; D-std-0014). Doubts are in Part E.

## Part 0 Summary

### 0.1 Agent definition
<!-- label: editorial; status: drafted; basis: primary -->
The four Descriptors of Advance HE's Professional Standards Framework 2023, each an introduction and three criteria, with the Fellowship category each leads to: D1 Associate Fellow, D2 Fellow, D3 Senior Fellow, D4 Principal Fellow. Reach for it to say what a recognition claim at a category must evidence, to place a role or a colleague's practice at a category, to plan development towards the next one, or to write mentoring and review prompts. The Dimensions it cites (V1 to A5) are defined in `std:doc:advancehe-psf-dimensions-2023-framework`.

### 0.2 Summary
<!-- label: both; status: drafted; basis: primary -->
Four broad categories of practice for people who teach or support learning in higher education. D1 and D2 are about the person's own practice: D1 asks for some of the Dimensions (at least V1 and V3, K1 to K3, and two Areas of Activity), D2 for all fifteen. D3 and D4 are about influence and leadership: D3 asks for a sustained record of leading or influencing others' practice and practice reaching beyond direct teaching; D4 asks for sustained strategic leadership with wide impact, effective and inclusive strategies or policies, and all the Dimensions built into that leadership. Every category asks for practice that is effective and inclusive. Each Descriptor leads to an Advance HE Fellowship category, directly or through an accredited institutional programme.

## Part S Standard

### S1 Identity
<!-- label: source; status: drafted; basis: primary -->
```yaml
issuer: "Advance HE, developed on behalf of the higher education sector; copyright jointly Advance HE, GuildHE and Universities UK (page 12)"
title: "Professional Standards Framework for teaching and supporting learning in higher education 2023"
shortTitle: PSF 2023
edition: 2023
dates:
  published: 2023
  other: []
kind: professional-standards-framework
jurisdiction: [UK]
authority: sector   # a sector framework for professional recognition; not regulatory
licence: "All rights reserved; redistribution or reproduction, in part or whole, only with the copyright holders' explicit permission (page 12)"
copyrightNotice: "© Advance HE, GuildHE, Universities UK 2023. All Rights Reserved."
permission:
  basis: "Abbott (3 October 2026, 10:18): 'I have permissio I run the Fellowship scheme at CMet and am a former member of the Advance HE consultation team - extarct the original and rephrase as decided - it is the phrases that will be used by agents not the original' (D-std-0013)"
  holder: "Abbott: runs the Cardiff Metropolitan University Fellowship scheme (an accredited route to Advance HE recognition) and is a former member of the Advance HE consultation team"
  use: "the issuer's statements are held in full, in the held text and in each S4 record's `source` field, for private language analysis; nothing is published; agents phrase from our rephrasings (paraphrase, S4a) (D-std-0014)"
scope: "the Descriptors (pages 6 to 10) and the recognition page (page 11) of the PSF 2023; the purpose and the Dimensions are in std:doc:advancehe-psf-dimensions-2023-framework"
```

### S2 Purpose and scope
<!-- label: source; status: drafted; basis: primary -->
```yaml
governs: "four Descriptors of broad categories of practice in teaching and supporting learning in higher education, each with three criteria (pages 6 to 10), and how they lead to recognition (page 11)"
appliesTo:
  awards: [Associate Fellow, Fellow, Senior Fellow, Principal Fellow]
  levels: [psf:d1, psf:d2, psf:d3, psf:d4]
  providers: "institutions with accredited development programmes (recognition.2)"
whoMustUse: none-stated   # voluntary
howUsed: [individual claims for recognition, development planning, institutional development and recognition programmes, career and progression pathways, professional bodies' recognition frameworks]
recognitionRoute: "a person who meets a Descriptor is recognised by Advance HE with the matching Fellowship category, directly or by completing an accredited institutional programme (recognition.1, recognition.2)"
doesNot: "define the Dimensions (companion document) or say how evidence is judged (Advance HE's own guidance, W-std-0021)"
beneficiary: "staff who teach or support learning in higher education"
statedSubjects: none-stated
subjects: see front matter (subjectScope universal)
```

### S3 Structure
<!-- label: both; status: drafted; basis: primary. The issuer numbers the Descriptors D1 to D4 and their criteria D1.1 to D4.3; the explanatory bullets, introductions and lead-ins are unnumbered and named here. -->
```yaml
components:
  - { number: about, componentType: section, parent: none, heading: "Descriptors: What are Descriptors?", items: 6 }
  - { number: D1, componentType: level, parent: none, heading: "Descriptor 1", items: [D1/intro, D1/stem, D1.1, D1.2, D1.3, D1/aligns] }
  - { number: D2, componentType: level, parent: none, heading: "Descriptor 2", items: [D2/intro, D2/stem, D2.1, D2.2, D2.3, D2/aligns] }
  - { number: D3, componentType: level, parent: none, heading: "Descriptor 3", items: [D3/intro, D3/stem, D3.1, D3.2, D3.3, D3/aligns] }
  - { number: D4, componentType: level, parent: none, heading: "Descriptor 4", items: [D4/intro, D4/stem, D4.1, D4.2, D4.3, D4/aligns] }
  - { number: recognition, componentType: section, parent: none, heading: "Relationship to Advance HE individual professional recognition and institutional accreditation", items: 3 }
companions:
  - { id: std:doc:advancehe-psf-dimensions-2023-framework, holds: "the purpose (page 2), the Dimensions (pages 4, 5) and the terms (Part B)" }
statements: 34
```

### S4 Statements
<!-- label: both; status: drafted; basis: primary. 34 records: 6 about the Descriptors, 4 introductions (D4's in two sentences), 4 lead-ins, 12 criteria, 4 recognition alignments, 3 on recognition and accreditation. Force: the criteria and their lead-ins are `threshold`, the conditions a claim must evidence (D-std-0004); the rest `describes`. The criteria are noun phrases completing their lead-in, so most carry no verb of their own; `requires` gives, in our terms, which Dimensions each criterion names. -->
```yaml
- id: advancehe/psf-descriptors-2023/about.1
  locator: { number: "about.1", headingPath: ["Descriptors", "What are Descriptors?"] }
  span: { start: 4181, end: 4270 }
  stem: none
  statementType: definition
  force: describes
  level: none
  dimension: what-are-descriptors
  appliesTo: "the Descriptors"
  addressee: none
  verbs: ["consist"]
  about: "the shape of a Descriptor"
  themes: [none]
  paraphrase: "There are four Descriptors, each made of an introduction and three criteria."
  source: "Four Descriptors, each consist of an introduction and a set of three criteria statements."
  quote: full   # the issuer statement, held for analysis (D-std-0014)
  audience: both
  subjects: inherited
- id: advancehe/psf-descriptors-2023/about.2
  locator: { number: "about.2", headingPath: ["Descriptors", "What are Descriptors?"] }
  span: { start: 4273, end: 4347 }
  stem: none
  statementType: definition
  force: describes
  level: none
  dimension: what-are-descriptors
  appliesTo: "the Descriptors"
  addressee: none
  verbs: ["define"]
  about: "four categories of practice"
  themes: [none]
  paraphrase: "They set out what marks four broad categories of practice."
  source: "These define the key characteristics of four broad categories of practice."
  quote: full   # the issuer statement, held for analysis (D-std-0014)
  audience: both
  subjects: inherited
- id: advancehe/psf-descriptors-2023/about.3
  locator: { number: "about.3", headingPath: ["Descriptors", "What are Descriptors?"] }
  span: { start: 4348, end: 4559 }
  stem: none
  statementType: definition
  force: describes
  level: none
  dimension: what-are-descriptors
  appliesTo: "the Descriptors"
  addressee: none
  verbs: ["Incorporating", "identifies", "meet", "recognises", "teach", "support"]
  about: "extent of practice; variety of roles"
  themes: [none]
  paraphrase: "Each Descriptor draws on the Dimensions, says how much practice meets it, and allows for the range of roles and practice among people who teach or support learning."
  source: "Incorporating the Dimensions, each Descriptor identifies the extent of practice required to meet it and recognises the variety of practice and roles undertaken by professionals who teach and/or support learning."
  quote: full   # the issuer statement, held for analysis (D-std-0014)
  audience: both
  subjects: inherited
- id: advancehe/psf-descriptors-2023/about.4
  locator: { number: "about.4", headingPath: ["Descriptors", "What are Descriptors?"] }
  span: { start: 4562, end: 4684 }
  stem: none
  statementType: definition
  force: describes
  level: none
  dimension: what-are-descriptors
  appliesTo: "the Descriptors"
  addressee: none
  verbs: ["use", "plan", "evidence", "achieve"]
  about: "use by individuals"
  themes: [none]
  paraphrase: "Individuals use them to plan development and to evidence practice for professional recognition."
  source: "Individuals use the Descriptors to plan their development and evidence their practice to achieve professional recognition."
  quote: full   # the issuer statement, held for analysis (D-std-0014)
  audience: both
  subjects: inherited
- id: advancehe/psf-descriptors-2023/about.5
  locator: { number: "about.5", headingPath: ["Descriptors", "What are Descriptors?"] }
  span: { start: 4687, end: 4881 }
  stem: none
  statementType: definition
  force: describes
  level: none
  dimension: what-are-descriptors
  appliesTo: "the Descriptors"
  addressee: none
  verbs: ["use", "inform", "support"]
  about: "use by institutions"
  themes: [none]
  paraphrase: "Institutions build early and continuing development and recognition programmes on them, and use them for career pathways and talent development."
  source: "Institutions use the Descriptors as a basis for initial and continuing professional development and recognition programmes, to inform career/ progression pathways and support talent development."
  quote: full   # the issuer statement, held for analysis (D-std-0014)
  audience: both
  subjects: inherited
- id: advancehe/psf-descriptors-2023/about.6
  locator: { number: "about.6", headingPath: ["Descriptors", "What are Descriptors?"] }
  span: { start: 4884, end: 5058 }
  stem: none
  statementType: definition
  force: describes
  level: none
  dimension: what-are-descriptors
  appliesTo: "the Descriptors"
  addressee: none
  verbs: ["use", "support"]
  about: "use by professional bodies"
  themes: [none]
  paraphrase: "Professional bodies base their activities and recognition frameworks for individual and institutional development on them."
  source: "Professional organisations use the Descriptors as a basis for activities and recognition frameworks that support the professional development of individuals and institutions."
  quote: full   # the issuer statement, held for analysis (D-std-0014)
  audience: both
  subjects: inherited
- id: advancehe/psf-descriptors-2023/D1/intro.1
  locator: { number: "D1/intro.1", headingPath: ["Descriptor 1", "Introduction"] }
  span: { start: 5177, end: 5264 }
  stem: none
  statementType: descriptor
  force: describes
  level: psf:d1
  dimension: introduction
  appliesTo: "recognition at D1"
  addressee: practitioner
  verbs: ["enables", "evidence"]
  about: "who D1 fits"
  themes: [none]
  paraphrase: "Descriptor 1 fits people whose practice lets them evidence some of the Dimensions."
  source: "D1 is suitable for individuals whose practice enables them to evidence some Dimensions."
  quote: full   # the issuer statement, held for analysis (D-std-0014)
  audience: both
  subjects: inherited
- id: advancehe/psf-descriptors-2023/D1/stem
  locator: { number: "D1/stem", headingPath: ["Descriptor 1", "Stem"] }
  span: { start: 5265, end: 5366 }
  stem: none
  statementType: stem
  force: threshold
  level: psf:d1
  dimension: stem
  appliesTo: "recognition at D1"
  addressee: practitioner
  verbs: ["demonstrated"]
  about: "D1 lead-in: effectiveness shown by evidence"
  themes: [none]
  paraphrase: "Effective teaching or learning support is shown by evidence of the following."
  source: "Effectiveness of practice in teaching and/or support of learning is demonstrated through evidence of:"
  quote: full   # the issuer statement, held for analysis (D-std-0014)
  audience: both
  subjects: inherited
- id: advancehe/psf-descriptors-2023/D1/1
  locator: { number: "D1/1", headingPath: ["Descriptor 1", "Criteria"] }
  span: { start: 5373, end: 5441 }
  stem: advancehe/psf-descriptors-2023/D1/stem
  statementType: criterion
  force: threshold
  level: psf:d1
  requires: {"atLeast": ["V1", "V3"], "plus": "the others that fit the role"}
  dimension: criteria
  appliesTo: "recognition at D1"
  addressee: practitioner
  verbs: []
  about: "values that fit, at least V1 and V3"
  themes: [none]
  paraphrase: "Acting on the Professional Values that fit the role, V1 and V3 among them at least."
  source: "use of appropriate Professional Values, including at least V1 and V3"
  quote: full   # the issuer statement, held for analysis (D-std-0014)
  audience: both
  subjects: inherited
- id: advancehe/psf-descriptors-2023/D1/2
  locator: { number: "D1/2", headingPath: ["Descriptor 1", "Criteria"] }
  span: { start: 5448, end: 5523 }
  stem: advancehe/psf-descriptors-2023/D1/stem
  statementType: criterion
  force: threshold
  level: psf:d1
  requires: {"atLeast": ["K1", "K2", "K3"], "plus": "the others that fit the role"}
  dimension: criteria
  appliesTo: "recognition at D1"
  addressee: practitioner
  verbs: []
  about: "knowledge that fits, at least K1 to K3"
  themes: [none]
  paraphrase: "Applying the Core Knowledge that fits the role, at least K1, K2 and K3."
  source: "application of appropriate Core Knowledge, including at least K1, K2 and K3"
  quote: full   # the issuer statement, held for analysis (D-std-0014)
  audience: both
  subjects: inherited
- id: advancehe/psf-descriptors-2023/D1/3
  locator: { number: "D1/3", headingPath: ["Descriptor 1", "Criteria"] }
  span: { start: 5530, end: 5608 }
  stem: advancehe/psf-descriptors-2023/D1/stem
  statementType: criterion
  force: threshold
  level: psf:d1
  requires: {"countOf": "A1-A5", "min": 2, "quality": ["effective", "inclusive"]}
  dimension: criteria
  appliesTo: "recognition at D1"
  addressee: practitioner
  verbs: []
  about: "two or more Areas of Activity"
  themes: [none]
  paraphrase: "Effective, inclusive practice in two or more of the five Areas of Activity."
  source: "effective and inclusive practice in at least two of the five Areas of Activity"
  quote: full   # the issuer statement, held for analysis (D-std-0014)
  audience: both
  subjects: inherited
- id: advancehe/psf-descriptors-2023/D1/aligns
  locator: { number: "D1/aligns", headingPath: ["Descriptor 1", "Recognition"] }
  span: { start: 5610, end: 5678 }
  stem: none
  statementType: crosswalk
  force: describes
  level: psf:d1
  dimension: recognition
  appliesTo: "recognition at D1"
  addressee: practitioner
  verbs: ["aligns"]
  about: "D1 and Associate Fellow"
  themes: [none]
  paraphrase: "D1 corresponds to Associate Fellow recognition."
  source: "Descriptor 1 aligns with Advance HE recognition as Associate Fellow."
  quote: full   # the issuer statement, held for analysis (D-std-0014)
  audience: both
  subjects: inherited
- id: advancehe/psf-descriptors-2023/D2/intro.1
  locator: { number: "D2/intro.1", headingPath: ["Descriptor 2", "Introduction"] }
  span: { start: 5797, end: 5921 }
  stem: none
  statementType: descriptor
  force: describes
  level: psf:d2
  dimension: introduction
  appliesTo: "recognition at D2"
  addressee: practitioner
  verbs: ["has", "enabling", "evidence"]
  about: "who D2 fits"
  themes: [none]
  paraphrase: "Descriptor 2 fits people whose work with learners is broad and deep enough to evidence every Dimension."
  source: "D2 is suitable for individuals whose practice with learners has breadth and depth, enabling them to evidence all Dimensions."
  quote: full   # the issuer statement, held for analysis (D-std-0014)
  audience: both
  subjects: inherited
- id: advancehe/psf-descriptors-2023/D2/stem
  locator: { number: "D2/stem", headingPath: ["Descriptor 2", "Stem"] }
  span: { start: 5922, end: 6035 }
  stem: none
  statementType: stem
  force: threshold
  level: psf:d2
  dimension: stem
  appliesTo: "recognition at D2"
  addressee: practitioner
  verbs: ["demonstrated"]
  about: "D2 lead-in: effectiveness shown by evidence"
  themes: [none]
  paraphrase: "Effective teaching or support of high-quality learning is shown by evidence of the following."
  source: "Effectiveness of practice in teaching and/or support of highquality learning is demonstrated through evidence of:"
  quote: full   # the issuer statement, held for analysis (D-std-0014)
  audience: both
  subjects: inherited
- id: advancehe/psf-descriptors-2023/D2/1
  locator: { number: "D2/1", headingPath: ["Descriptor 2", "Criteria"] }
  span: { start: 6042, end: 6077 }
  stem: advancehe/psf-descriptors-2023/D2/stem
  statementType: criterion
  force: threshold
  level: psf:d2
  requires: {"all": ["V1", "V2", "V3", "V4", "V5"]}
  dimension: criteria
  appliesTo: "recognition at D2"
  addressee: practitioner
  verbs: []
  about: "all five values"
  themes: [none]
  paraphrase: "Acting on every one of the five Professional Values."
  source: "use of all five Professional Values"
  quote: full   # the issuer statement, held for analysis (D-std-0014)
  audience: both
  subjects: inherited
- id: advancehe/psf-descriptors-2023/D2/2
  locator: { number: "D2/2", headingPath: ["Descriptor 2", "Criteria"] }
  span: { start: 6084, end: 6131 }
  stem: advancehe/psf-descriptors-2023/D2/stem
  statementType: criterion
  force: threshold
  level: psf:d2
  requires: {"all": ["K1", "K2", "K3", "K4", "K5"]}
  dimension: criteria
  appliesTo: "recognition at D2"
  addressee: practitioner
  verbs: []
  about: "all five forms of knowledge"
  themes: [none]
  paraphrase: "Applying every one of the five forms of Core Knowledge."
  source: "application of all five forms of Core Knowledge"
  quote: full   # the issuer statement, held for analysis (D-std-0014)
  audience: both
  subjects: inherited
- id: advancehe/psf-descriptors-2023/D2/3
  locator: { number: "D2/3", headingPath: ["Descriptor 2", "Criteria"] }
  span: { start: 6138, end: 6200 }
  stem: advancehe/psf-descriptors-2023/D2/stem
  statementType: criterion
  force: threshold
  level: psf:d2
  requires: {"all": ["A1", "A2", "A3", "A4", "A5"], "quality": ["effective", "inclusive"]}
  dimension: criteria
  appliesTo: "recognition at D2"
  addressee: practitioner
  verbs: []
  about: "all five Areas of Activity"
  themes: [none]
  paraphrase: "Effective, inclusive practice across every Area of Activity."
  source: "effective and inclusive practice in all five Areas of Activity"
  quote: full   # the issuer statement, held for analysis (D-std-0014)
  audience: both
  subjects: inherited
- id: advancehe/psf-descriptors-2023/D2/aligns
  locator: { number: "D2/aligns", headingPath: ["Descriptor 2", "Recognition"] }
  span: { start: 6202, end: 6260 }
  stem: none
  statementType: crosswalk
  force: describes
  level: psf:d2
  dimension: recognition
  appliesTo: "recognition at D2"
  addressee: practitioner
  verbs: ["aligns"]
  about: "D2 and Fellow"
  themes: [none]
  paraphrase: "D2 corresponds to Fellow recognition."
  source: "Descriptor 2 aligns with Advance HE recognition as Fellow."
  quote: full   # the issuer statement, held for analysis (D-std-0014)
  audience: both
  subjects: inherited
- id: advancehe/psf-descriptors-2023/D3/intro.1
  locator: { number: "D3/intro.1", headingPath: ["Descriptor 3", "Introduction"] }
  span: { start: 6379, end: 6571 }
  stem: none
  statementType: descriptor
  force: describes
  level: psf:d3
  dimension: introduction
  appliesTo: "recognition at D3"
  addressee: practitioner
  verbs: ["provides", "lead", "influence", "teach", "support"]
  about: "who D3 fits"
  themes: [none]
  paraphrase: "Descriptor 3 fits people whose thorough understanding and effective practice equip them to lead or influence others who teach or support high-quality learning."
  source: "D3 is suitable for individuals whose comprehensive understanding and effective practice provides a basis from which they lead or influence those who teach and/or support high-quality learning."
  quote: full   # the issuer statement, held for analysis (D-std-0014)
  audience: both
  subjects: inherited
- id: advancehe/psf-descriptors-2023/D3/stem
  locator: { number: "D3/stem", headingPath: ["Descriptor 3", "Stem"] }
  span: { start: 6572, end: 6605 }
  stem: none
  statementType: stem
  force: threshold
  level: psf:d3
  dimension: stem
  appliesTo: "recognition at D3"
  addressee: practitioner
  verbs: ["evidence"]
  about: "D3 lead-in"
  themes: [none]
  paraphrase: "The person can evidence the following."
  source: "Individuals are able to evidence:"
  quote: full   # the issuer statement, held for analysis (D-std-0014)
  audience: both
  subjects: inherited
- id: advancehe/psf-descriptors-2023/D3/1
  locator: { number: "D3/1", headingPath: ["Descriptor 3", "Criteria"] }
  span: { start: 6612, end: 6725 }
  stem: advancehe/psf-descriptors-2023/D3/stem
  statementType: criterion
  force: threshold
  level: psf:d3
  requires: {"sustained": true, "of": "others' practice"}
  dimension: criteria
  appliesTo: "recognition at D3"
  addressee: practitioner
  verbs: ["leading", "influencing", "teach", "support"]
  about: "a record of leading or influencing others"
  themes: [none]
  paraphrase: "A record, over time, of leading or influencing how others teach or support high-quality learning."
  source: "a sustained record of leading or influencing the practice of those who teach and/or support high quality learning"
  quote: full   # the issuer statement, held for analysis (D-std-0014)
  audience: both
  subjects: inherited
- id: advancehe/psf-descriptors-2023/D3/2
  locator: { number: "D3/2", headingPath: ["Descriptor 3", "Criteria"] }
  span: { start: 6732, end: 6799 }
  stem: advancehe/psf-descriptors-2023/D3/stem
  statementType: criterion
  force: threshold
  level: psf:d3
  requires: {"integrates": "all fifteen", "quality": ["effective", "inclusive"]}
  dimension: criteria
  appliesTo: "recognition at D3"
  addressee: practitioner
  verbs: ["integrates"]
  about: "all Dimensions integrated"
  themes: [none]
  paraphrase: "Practice that is effective and inclusive and brings all the Dimensions together."
  source: "practice that is effective, inclusive and integrates all Dimensions"
  quote: full   # the issuer statement, held for analysis (D-std-0014)
  audience: both
  subjects: inherited
- id: advancehe/psf-descriptors-2023/D3/3
  locator: { number: "D3/3", headingPath: ["Descriptor 3", "Criteria"] }
  span: { start: 6806, end: 6899 }
  stem: advancehe/psf-descriptors-2023/D3/stem
  statementType: criterion
  force: threshold
  level: psf:d3
  dimension: criteria
  appliesTo: "recognition at D3"
  addressee: practitioner
  verbs: ["extends"]
  about: "practice beyond direct teaching"
  themes: [none]
  paraphrase: "Practice reaching well beyond one's own direct teaching or direct learning support."
  source: "practice that extends significantly beyond direct teaching and/or direct support for learning"
  quote: full   # the issuer statement, held for analysis (D-std-0014)
  audience: both
  subjects: inherited
- id: advancehe/psf-descriptors-2023/D3/aligns
  locator: { number: "D3/aligns", headingPath: ["Descriptor 3", "Recognition"] }
  span: { start: 6901, end: 6966 }
  stem: none
  statementType: crosswalk
  force: describes
  level: psf:d3
  dimension: recognition
  appliesTo: "recognition at D3"
  addressee: practitioner
  verbs: ["aligns"]
  about: "D3 and Senior Fellow"
  themes: [none]
  paraphrase: "D3 corresponds to Senior Fellow recognition."
  source: "Descriptor 3 aligns with Advance HE recognition as Senior Fellow."
  quote: full   # the issuer statement, held for analysis (D-std-0014)
  audience: both
  subjects: inherited
- id: advancehe/psf-descriptors-2023/D4/intro.1
  locator: { number: "D4/intro.1", headingPath: ["Descriptor 4", "Introduction"] }
  span: { start: 7085, end: 7244 }
  stem: none
  statementType: descriptor
  force: describes
  level: psf:d4
  dimension: introduction
  appliesTo: "recognition at D4"
  addressee: practitioner
  verbs: ["involves"]
  about: "who D4 fits"
  themes: [none]
  paraphrase: "Descriptor 4 fits very experienced people with a long, effective record of leading high-quality learning strategically."
  source: "D4 is suitable for highly experienced individuals whose practice involves a sustained record of effectiveness in strategic leadership of high-quality learning."
  quote: full   # the issuer statement, held for analysis (D-std-0014)
  audience: both
  subjects: inherited
- id: advancehe/psf-descriptors-2023/D4/intro.2
  locator: { number: "D4/intro.2", headingPath: ["Descriptor 4", "Introduction"] }
  span: { start: 7245, end: 7271 }
  stem: none
  statementType: descriptor
  force: describes
  level: psf:d4
  dimension: introduction
  appliesTo: "recognition at D4"
  addressee: practitioner
  verbs: []
  about: "wide impact"
  themes: [none]
  paraphrase: "Their impact is wide."
  source: "Their impact is extensive."
  quote: full   # the issuer statement, held for analysis (D-std-0014)
  audience: both
  subjects: inherited
- id: advancehe/psf-descriptors-2023/D4/stem
  locator: { number: "D4/stem", headingPath: ["Descriptor 4", "Stem"] }
  span: { start: 7272, end: 7305 }
  stem: none
  statementType: stem
  force: threshold
  level: psf:d4
  dimension: stem
  appliesTo: "recognition at D4"
  addressee: practitioner
  verbs: ["evidence"]
  about: "D4 lead-in"
  themes: [none]
  paraphrase: "The person can evidence the following."
  source: "Individuals are able to evidence:"
  quote: full   # the issuer statement, held for analysis (D-std-0014)
  audience: both
  subjects: inherited
- id: advancehe/psf-descriptors-2023/D4/1
  locator: { number: "D4/1", headingPath: ["Descriptor 4", "Criteria"] }
  span: { start: 7312, end: 7504 }
  stem: advancehe/psf-descriptors-2023/D4/stem
  statementType: criterion
  force: threshold
  level: psf:d4
  requires: {"sustained": true, "scope": ["institution", "beyond", "discipline", "profession"]}
  dimension: criteria
  appliesTo: "recognition at D4"
  addressee: practitioner
  verbs: []
  about: "strategic leadership with wide impact"
  themes: [none]
  paraphrase: "Strategic leadership of higher education practice, effective and kept up over time, with wide impact on high-quality learning, inside an institution, beyond it, or across a whole discipline or profession."
  source: "sustained and effective strategic leadership of higher education practice, with extensive impact on high-quality learning: within or beyond an institution, or across a discipline or profession"
  quote: full   # the issuer statement, held for analysis (D-std-0014)
  audience: both
  subjects: inherited
- id: advancehe/psf-descriptors-2023/D4/2
  locator: { number: "D4/2", headingPath: ["Descriptor 4", "Criteria"] }
  span: { start: 7511, end: 7671 }
  stem: advancehe/psf-descriptors-2023/D4/stem
  statementType: criterion
  force: threshold
  level: psf:d4
  requires: {"quality": ["effective", "inclusive"]}
  dimension: criteria
  appliesTo: "recognition at D4"
  addressee: practitioner
  verbs: ["enhance"]
  about: "strategies and policies that improve practice"
  themes: [none]
  paraphrase: "Developing and putting in place effective, inclusive strategies, policies, procedures or initiatives that improve practice and learners' outcomes."
  source: "development and implementation of effective and inclusive: strategies, or policies, or procedures, or initiatives, to enhance practice and outcomes for learners"
  quote: full   # the issuer statement, held for analysis (D-std-0014)
  audience: both
  subjects: inherited
- id: advancehe/psf-descriptors-2023/D4/3
  locator: { number: "D4/3", headingPath: ["Descriptor 4", "Criteria"] }
  span: { start: 7678, end: 7800 }
  stem: advancehe/psf-descriptors-2023/D4/stem
  statementType: criterion
  force: threshold
  level: psf:d4
  requires: {"integrates": "all fifteen", "in": "strategic leadership"}
  dimension: criteria
  appliesTo: "recognition at D4"
  addressee: practitioner
  verbs: []
  about: "all Dimensions in strategic leadership"
  themes: [none]
  paraphrase: "Active commitment to all the Dimensions, built into strategic leadership of academic or professional practice."
  source: "active commitment to, and integration of, all Dimensions in the strategic leadership of academic or professional practices"
  quote: full   # the issuer statement, held for analysis (D-std-0014)
  audience: both
  subjects: inherited
- id: advancehe/psf-descriptors-2023/D4/aligns
  locator: { number: "D4/aligns", headingPath: ["Descriptor 4", "Recognition"] }
  span: { start: 7802, end: 7870 }
  stem: none
  statementType: crosswalk
  force: describes
  level: psf:d4
  dimension: recognition
  appliesTo: "recognition at D4"
  addressee: practitioner
  verbs: ["aligns"]
  about: "D4 and Principal Fellow"
  themes: [none]
  paraphrase: "D4 corresponds to Principal Fellow recognition."
  source: "Descriptor 4 aligns with Advance HE recognition as Principal Fellow."
  quote: full   # the issuer statement, held for analysis (D-std-0014)
  audience: both
  subjects: inherited
- id: advancehe/psf-descriptors-2023/recognition.1
  locator: { number: "recognition.1", headingPath: ["Relationship to Advance HE individual professional recognition and institutional accreditation"] }
  span: { start: 8072, end: 8250 }
  stem: none
  statementType: context
  force: describes
  level: none
  dimension: relationship-to-advance-he-individual-professional-recognition-and-institutional-accreditation
  appliesTo: "recognition and accreditation"
  addressee: none
  verbs: ["recognises", "meet"]
  about: "Fellowship for meeting a Descriptor"
  themes: [none]
  paraphrase: "Advance HE recognises a person who meets one of the Descriptors by awarding the matching category of Fellowship."
  source: "Advance HE recognises individuals who meet the requirements of one of the Descriptors of the Professional Standards Framework (PSF) through the award of a category of Fellowship."
  quote: full   # the issuer statement, held for analysis (D-std-0014)
  audience: both
  subjects: inherited
- id: advancehe/psf-descriptors-2023/recognition.2
  locator: { number: "recognition.2", headingPath: ["Relationship to Advance HE individual professional recognition and institutional accreditation"] }
  span: { start: 8251, end: 8522 }
  stem: none
  statementType: context
  force: describes
  level: none
  dimension: relationship-to-advance-he-individual-professional-recognition-and-institutional-accreditation
  appliesTo: "recognition and accreditation"
  addressee: none
  verbs: ["provides", "confirmed", "enabling", "complete", "recognised"]
  about: "accredited programmes"
  themes: [none]
  paraphrase: "Through institutional accreditation, a development programme can be confirmed as aligned with the PSF, so that those completing it are recognised in one of the four categories."
  source: "Advance HE institutional accreditation provides a mechanism through which professional development programmes can be confirmed as being aligned to the PSF enabling those who complete them to be recognised as an Associate Fellow, Fellow, Senior Fellow or Principal Fellow."
  quote: full   # the issuer statement, held for analysis (D-std-0014)
  audience: both
  subjects: inherited
- id: advancehe/psf-descriptors-2023/recognition.3
  locator: { number: "recognition.3", headingPath: ["Relationship to Advance HE individual professional recognition and institutional accreditation"] }
  span: { start: 8523, end: 8685 }
  stem: none
  statementType: context
  force: describes
  level: none
  dimension: relationship-to-advance-he-individual-professional-recognition-and-institutional-accreditation
  appliesTo: "recognition and accreditation"
  addressee: none
  verbs: ["offered", "wishing", "accredited"]
  about: "help for institutions seeking accreditation"
  themes: [none]
  paraphrase: "Advance HE helps institutions that seek accreditation for how they apply and use the PSF."
  source: "Guidance and support is offered through the work of Advance HE to higher education institutions wishing to be accredited for their application and use of the PSF."
  quote: full   # the issuer statement, held for analysis (D-std-0014)
  audience: practitioner
  subjects: inherited
```

### S4a Audience versions
<!-- label: both; status: drafted; basis: primary. forPractitioner: for those who lead, mentor, review or design recognition and development. forBeneficiary: for the person making a claim, in the second person. These are the phrases agents use (Abbott, 10:18). -->
```yaml
- statement: advancehe/psf-descriptors-2023/about.1
  forPractitioner: { text: "Each of the four Descriptors has an introduction followed by three criteria.", rewrite: full, force: describes, status: drafted }
  forBeneficiary: { text: "You meet a Descriptor by evidencing its three criteria; each also has an introduction saying who it suits.", rewrite: full, force: describes, status: drafted }
- statement: advancehe/psf-descriptors-2023/about.2
  forPractitioner: { text: "The Descriptors set out what marks each of four broad categories of practice.", rewrite: full, force: describes, status: drafted }
  forBeneficiary: { text: "Each Descriptor marks a broad category of practice you can work towards.", rewrite: full, force: describes, status: drafted }
- statement: advancehe/psf-descriptors-2023/about.3
  forPractitioner: { text: "Each Descriptor builds in the Dimensions, sets how much practice is needed to meet it, and allows for the many roles people hold in teaching and supporting learning.", rewrite: full, force: describes, status: drafted }
  forBeneficiary: { text: "Each Descriptor draws on the Dimensions, sets how much practice you need to meet it, and allows for the role you hold in teaching or supporting learning.", rewrite: full, force: describes, status: drafted }
- statement: advancehe/psf-descriptors-2023/about.4
  forPractitioner: { text: "People seeking recognition plan their development with the Descriptors and evidence their practice against them.", rewrite: full, force: describes, status: drafted }
  forBeneficiary: { text: "You use the Descriptors to plan your development and to evidence your practice for professional recognition.", rewrite: full, force: describes, status: drafted }
- statement: advancehe/psf-descriptors-2023/about.5
  forPractitioner: { text: "Institutions base their development and recognition programmes, early-career and continuing, on the Descriptors, and use them to shape career pathways and develop talent.", rewrite: full, force: describes, status: drafted }
  forBeneficiary: { text: "Your institution may build its development and recognition programmes, and its career pathways, on the Descriptors.", rewrite: full, force: describes, status: drafted }
- statement: advancehe/psf-descriptors-2023/about.6
  forPractitioner: { text: "Professional bodies use the Descriptors to base their own development activities and recognition frameworks on.", rewrite: full, force: describes, status: drafted }
  forBeneficiary: { text: "Your professional body may also use the Descriptors in its own development activities and recognition schemes.", rewrite: full, force: describes, status: drafted }
- statement: advancehe/psf-descriptors-2023/D1/intro.1
  forPractitioner: { text: "D1 suits colleagues whose role gives them evidence of some of the Dimensions, not necessarily all.", rewrite: full, force: describes, status: drafted }
  forBeneficiary: { text: "D1 suits you if your role lets you evidence some of the Dimensions, though not necessarily all of them.", rewrite: full, force: describes, status: drafted }
- statement: advancehe/psf-descriptors-2023/D1/stem
  forPractitioner: { text: "For D1, effective practice in teaching or supporting learning is shown through evidence of the three criteria.", rewrite: full, force: threshold, status: drafted }
  forBeneficiary: { text: "For D1, you show your teaching or support for learning is effective by evidencing:", rewrite: full, force: threshold, status: drafted }
- statement: advancehe/psf-descriptors-2023/D1/1
  forPractitioner: { text: "Evidence that the applicant acts on the values relevant to their role, including V1 (respect for learners) and V3 (evidence-informed practice) as a minimum.", rewrite: full, force: threshold, status: drafted }
  forBeneficiary: { text: "You show that you act on the values that fit your role, and always on V1 (respecting learners) and V3 (basing practice on evidence).", rewrite: full, force: threshold, status: drafted }
- statement: advancehe/psf-descriptors-2023/D1/2
  forPractitioner: { text: "Evidence that the applicant applies the knowledge relevant to their role, including at minimum K1 (how learners learn), K2 (approaches to teaching and support) and K3 (critical evaluation).", rewrite: full, force: threshold, status: drafted }
  forBeneficiary: { text: "You show you apply the knowledge your role needs, at least K1 (how people learn), K2 (ways to teach or support learning) and K3 (critical evaluation).", rewrite: full, force: threshold, status: drafted }
- statement: advancehe/psf-descriptors-2023/D1/3
  forPractitioner: { text: "Evidence of effective and inclusive practice in two or more Areas of Activity.", rewrite: full, force: threshold, status: drafted }
  forBeneficiary: { text: "You show effective, inclusive practice in two or more of the five areas of activity.", rewrite: full, force: threshold, status: drafted }
- statement: advancehe/psf-descriptors-2023/D1/aligns
  forPractitioner: { text: "Meeting D1 leads to Advance HE recognition as Associate Fellow.", rewrite: full, force: describes, status: drafted }
  forBeneficiary: { text: "If you meet D1, you are recognised as an Associate Fellow.", rewrite: full, force: describes, status: drafted }
- statement: advancehe/psf-descriptors-2023/D2/intro.1
  forPractitioner: { text: "D2 suits colleagues with a substantive role with learners, broad and deep enough to evidence all fifteen Dimensions.", rewrite: full, force: describes, status: drafted }
  forBeneficiary: { text: "D2 suits you if your work with learners is broad and deep enough to evidence all fifteen Dimensions.", rewrite: full, force: describes, status: drafted }
- statement: advancehe/psf-descriptors-2023/D2/stem
  forPractitioner: { text: "For D2, effective practice in teaching or supporting high-quality learning is shown through evidence of the three criteria.", rewrite: full, force: threshold, status: drafted }
  forBeneficiary: { text: "For D2, you show your teaching or support for high-quality learning is effective by evidencing:", rewrite: full, force: threshold, status: drafted }
- statement: advancehe/psf-descriptors-2023/D2/1
  forPractitioner: { text: "Evidence that the applicant acts on all five values, V1 to V5.", rewrite: full, force: threshold, status: drafted }
  forBeneficiary: { text: "You show you act on all five values, V1 to V5.", rewrite: full, force: threshold, status: drafted }
- statement: advancehe/psf-descriptors-2023/D2/2
  forPractitioner: { text: "Evidence that the applicant applies all five forms of knowledge, K1 to K5.", rewrite: full, force: threshold, status: drafted }
  forBeneficiary: { text: "You show you apply all five forms of knowledge, K1 to K5.", rewrite: full, force: threshold, status: drafted }
- statement: advancehe/psf-descriptors-2023/D2/3
  forPractitioner: { text: "Evidence of effective, inclusive practice across all five Areas of Activity, A1 to A5.", rewrite: full, force: threshold, status: drafted }
  forBeneficiary: { text: "You show effective, inclusive practice in every area of activity, A1 to A5.", rewrite: full, force: threshold, status: drafted }
- statement: advancehe/psf-descriptors-2023/D2/aligns
  forPractitioner: { text: "Meeting D2 leads to Advance HE recognition as Fellow.", rewrite: full, force: describes, status: drafted }
  forBeneficiary: { text: "If you meet D2, you are recognised as a Fellow.", rewrite: full, force: describes, status: drafted }
- statement: advancehe/psf-descriptors-2023/D3/intro.1
  forPractitioner: { text: "D3 suits experienced colleagues whose full understanding and effective practice give them a base for leading or influencing others who teach or support learning.", rewrite: full, force: describes, status: drafted }
  forBeneficiary: { text: "D3 suits you if your understanding and effective practice let you lead or influence the people who teach or support learning.", rewrite: full, force: describes, status: drafted }
- statement: advancehe/psf-descriptors-2023/D3/stem
  forPractitioner: { text: "For D3, the applicant evidences the three criteria.", rewrite: full, force: threshold, status: drafted }
  forBeneficiary: { text: "For D3, you evidence:", rewrite: full, force: threshold, status: drafted }
- statement: advancehe/psf-descriptors-2023/D3/1
  forPractitioner: { text: "Evidence of leading or influencing, over a sustained period, the practice of colleagues who teach or support learning.", rewrite: full, force: threshold, status: drafted }
  forBeneficiary: { text: "You show a record, kept up over time, of leading or influencing how others teach or support learning.", rewrite: full, force: threshold, status: drafted }
- statement: advancehe/psf-descriptors-2023/D3/2
  forPractitioner: { text: "Evidence of effective, inclusive practice that integrates all fifteen Dimensions.", rewrite: full, force: threshold, status: drafted }
  forBeneficiary: { text: "You show effective, inclusive practice that brings all fifteen Dimensions together.", rewrite: full, force: threshold, status: drafted }
- statement: advancehe/psf-descriptors-2023/D3/3
  forPractitioner: { text: "Evidence of practice reaching well beyond the applicant's own direct teaching or direct support for learning.", rewrite: full, force: threshold, status: drafted }
  forBeneficiary: { text: "You show practice that reaches well beyond your own teaching or direct support for learning.", rewrite: full, force: threshold, status: drafted }
- statement: advancehe/psf-descriptors-2023/D3/aligns
  forPractitioner: { text: "Meeting D3 leads to Advance HE recognition as Senior Fellow.", rewrite: full, force: describes, status: drafted }
  forBeneficiary: { text: "If you meet D3, you are recognised as a Senior Fellow.", rewrite: full, force: describes, status: drafted }
- statement: advancehe/psf-descriptors-2023/D4/intro.1
  forPractitioner: { text: "D4 suits very experienced colleagues with a long, effective record of strategic leadership of high-quality learning.", rewrite: full, force: describes, status: drafted }
  forBeneficiary: { text: "D4 suits you if you are very experienced and have a long, effective record of leading learning strategically.", rewrite: full, force: describes, status: drafted }
- statement: advancehe/psf-descriptors-2023/D4/intro.2
  forPractitioner: { text: "Their impact reaches widely.", rewrite: full, force: describes, status: drafted }
  forBeneficiary: { text: "Your impact reaches widely.", rewrite: full, force: describes, status: drafted }
- statement: advancehe/psf-descriptors-2023/D4/stem
  forPractitioner: { text: "For D4, the applicant evidences the three criteria.", rewrite: full, force: threshold, status: drafted }
  forBeneficiary: { text: "For D4, you evidence:", rewrite: full, force: threshold, status: drafted }
- statement: advancehe/psf-descriptors-2023/D4/1
  forPractitioner: { text: "Evidence of effective strategic leadership of higher education practice, kept up over time, whose impact on learning reaches across an institution, beyond it, or across a whole discipline or profession.", rewrite: full, force: threshold, status: drafted }
  forBeneficiary: { text: "You show effective strategic leadership of higher education practice, kept up over time, with wide impact on learning in your institution, beyond it or across your discipline or profession.", rewrite: full, force: threshold, status: drafted }
- statement: advancehe/psf-descriptors-2023/D4/2
  forPractitioner: { text: "Evidence of developing and implementing effective, inclusive strategies, policies, procedures or initiatives that improve practice and what learners achieve.", rewrite: full, force: threshold, status: drafted }
  forBeneficiary: { text: "You show you have developed and put in place effective, inclusive strategies, policies, procedures or initiatives that improve practice and learners' outcomes.", rewrite: full, force: threshold, status: drafted }
- statement: advancehe/psf-descriptors-2023/D4/3
  forPractitioner: { text: "Evidence of active commitment to all the Dimensions, integrated into strategic leadership of academic or professional practice.", rewrite: full, force: threshold, status: drafted }
  forBeneficiary: { text: "You show active commitment to all the Dimensions, built into how you lead academic or professional practice strategically.", rewrite: full, force: threshold, status: drafted }
- statement: advancehe/psf-descriptors-2023/D4/aligns
  forPractitioner: { text: "Meeting D4 leads to Advance HE recognition as Principal Fellow.", rewrite: full, force: describes, status: drafted }
  forBeneficiary: { text: "If you meet D4, you are recognised as a Principal Fellow.", rewrite: full, force: describes, status: drafted }
- statement: advancehe/psf-descriptors-2023/recognition.1
  forPractitioner: { text: "Advance HE awards the category of Fellowship that matches the Descriptor a person meets.", rewrite: full, force: describes, status: drafted }
  forBeneficiary: { text: "If you meet one of the Descriptors, you are recognised with the matching category of Fellowship.", rewrite: full, force: describes, status: drafted }
- statement: advancehe/psf-descriptors-2023/recognition.2
  forPractitioner: { text: "Through institutional accreditation, a development programme is confirmed as aligned with the PSF; completing it brings recognition in one of the four Fellowship categories.", rewrite: full, force: describes, status: drafted }
  forBeneficiary: { text: "If you complete an accredited programme aligned with the framework, you are recognised in the matching category, from Associate Fellow to Principal Fellow.", rewrite: full, force: describes, status: drafted }
- statement: advancehe/psf-descriptors-2023/recognition.3
  forPractitioner: { text: "Advance HE helps institutions that seek accreditation for how they apply and use the PSF.", rewrite: full, force: describes, status: drafted }
  forBeneficiary: none   # practitioner-only record
```

### S5 Levels and alignment
<!-- label: both; status: drafted; basis: primary -->
```yaml
levels:
  - { id: psf:d1, role: defines, locator: "Descriptor 1 (page 7)", typical: Associate Fellow }
  - { id: psf:d2, role: defines, locator: "Descriptor 2 (page 8)", typical: Fellow }
  - { id: psf:d3, role: defines, locator: "Descriptor 3 (page 9)", typical: Senior Fellow }
  - { id: psf:d4, role: defines, locator: "Descriptor 4 (page 10)", typical: Principal Fellow }
dimensionsUsed: { ids: "psf:V1 to psf:A5", definedIn: std:doc:advancehe-psf-dimensions-2023-framework }
crosswalks:
  - { from: psf:d1, to: "Advance HE Associate Fellow", relation: equivalent, source: "D1/aligns: the issuer's 'aligns with'" }
  - { from: psf:d2, to: "Advance HE Fellow", relation: equivalent, source: "D2/aligns" }
  - { from: psf:d3, to: "Advance HE Senior Fellow", relation: equivalent, source: "D3/aligns" }
  - { from: psf:d4, to: "Advance HE Principal Fellow", relation: equivalent, source: "D4/aligns" }
  # no crosswalk to any qualification framework is stated, and none is inferred here (framework rule 2)
```

### S6 Themes
<!-- label: both; status: drafted; basis: primary -->
```yaml
- { theme: "inclusion", where: "D1/3, D2/3, D3/2, D4/2", note: "every category asks for inclusive practice" }
- { theme: "leadership", where: "D3/1, D4/1, D4/2, D4/3", note: "influence at D3, strategic leadership at D4" }
```

### S7 Relations
```yaml
- { rel: companionOf, target: std:doc:advancehe-psf-dimensions-2023-framework, note: "one framework, two documents (Abbott, 10:20; D-std-0013); the criteria cite its Dimension ids" }
- { rel: describedBy, target: ing:doc:professional-standards-framework-advance-he-2023, note: "ing's theory-side document on the same PDF (run 0053)" }
- { rel: supersedes, target: "UKPSF 2011 descriptors D1 to D4", note: "not stated in the document; std's knowledge, P2 to confirm (W-std-0022)" }
```

### S8 Currency and review
```yaml
published: 2023
lastReviewed: none-stated
reviewCycle: none-stated
consultation: "none stated in the document; Abbott reports he was a member of Advance HE's consultation team (S1)"
replacedBy: none known
```

### S9 Commentary (optional)
<!-- label: editorial; status: drafted; basis: inferred. Our reading; nothing here is the issuer's. -->
- **A staff ladder beside the student spine.** D1 to D4 step professional practice, not qualification level. They do not map to `spine:4` to `spine:8`, and no crosswalk is stated. A Fellowship scheme often sits beside a postgraduate certificate at FHEQ 7; that is a programme's choice, not the framework's.
- **Two kinds of step.** D1 to D2 is a step in coverage (some to all Dimensions, in one's own practice). D2 to D3 changes whose practice counts (one's own to others'). D3 to D4 changes the scale (influence to strategic leadership with wide impact).
- **For writers of mentoring and review prompts:** the criteria name what to evidence, not how much; Advance HE's guidance per Descriptor (W-std-0021) and a scheme's own criteria set the judgement.

### SL Level language
<!-- label: both; status: drafted; basis: primary. Our words, built from S4 and S4a; the issuer's words appear only as single terms in quotation marks. -->

#### SL1 What defines each level
| Level | For the practitioner | For the applicant |
|---|---|---|
| `psf:d1` (Associate Fellow) | D1 suits colleagues whose role gives them evidence of some of the Dimensions, not necessarily all. | D1 suits you if your role lets you evidence some of the Dimensions, though not necessarily all of them. |
| `psf:d2` (Fellow) | D2 suits colleagues with a substantive role with learners, broad and deep enough to evidence all fifteen Dimensions. | D2 suits you if your work with learners is broad and deep enough to evidence all fifteen Dimensions. |
| `psf:d3` (Senior Fellow) | D3 suits experienced colleagues whose full understanding and effective practice give them a base for leading or influencing others who teach or support learning. | D3 suits you if your understanding and effective practice let you lead or influence the people who teach or support learning. |
| `psf:d4` (Principal Fellow) | D4 suits very experienced colleagues with a long, effective record of strategic leadership of high-quality learning. | D4 suits you if you are very experienced and have a long, effective record of leading learning strategically. |

#### SL2 The level table, by part
| Level | Professional Values | Core Knowledge | Areas of Activity | Beyond the Dimensions |
|---|---|---|---|---|
| `psf:d1` | those that fit the role; V1 and V3 at least | those that fit the role; K1, K2 and K3 at least | two or more, effective and inclusive | none |
| `psf:d2` | all five | all five | all five, effective and inclusive | none |
| `psf:d3` | all, integrated | all, integrated | all, integrated; effective and inclusive | a sustained record of leading or influencing others; practice well beyond direct teaching or support |
| `psf:d4` | all, built into strategic leadership | all, built into strategic leadership | all, built into strategic leadership | sustained, effective strategic leadership with wide impact; effective, inclusive strategies, policies, procedures or initiatives |

#### SL3 Verbs by level
| Level | Lead-in | Criteria (the issuer's head words, first occurrence kept) |
|---|---|---|
| `psf:d1` | demonstrated through evidence of | use; application; practice |
| `psf:d2` | demonstrated through evidence of | use; application; practice |
| `psf:d3` | able to evidence | leading, influencing; integrates; extends |
| `psf:d4` | able to evidence | leadership; development, implementation; commitment, integration |

#### SL4 How progression is communicated
<!-- Each thread follows one quality up the Descriptors; the issuer's single words in quotation marks, otherwise our short reading. -->
- **Coverage of the Dimensions:** D1: "some", with named minimums; D2: "all"; D3: all, "integrates"; D4: all, "integration" within strategic leadership.
- **Whose practice:** D1 and D2: the person's own, with learners; D3: others who teach or support learning; D4: an institution, beyond it, a discipline or a profession.
- **Reach:** D3: "beyond" direct teaching; D4: "extensive" impact, "strategic".
- **Time:** D1 and D2: none stated; D3 and D4: "sustained" record.
- **Experience:** D2: "breadth and depth"; D3: "comprehensive" understanding; D4: "highly experienced".
- **Quality words:** "effective" and "inclusive" at every level; "high-quality" learning from D2 up.
- **What is evidenced:** D1 and D2: practice, through evidence of the criteria; D3 and D4: the person is "able to evidence" a record.

#### SL5 Observations on the formulation
<!-- label: editorial; status: drafted; basis: primary -->
- **Noun-phrase criteria.** Every criterion is a noun phrase completing its lead-in ("use of", "application of", "a sustained record of"), so verbs carry little; the step sits in quantifiers (some, at least, all), in whose practice, and in reach.
- **Named minimums at D1 only.** D1 is the only Descriptor that names Dimensions (V1, V3, K1 to K3) and a count (two Areas of Activity); higher Descriptors take all fifteen as given.
- **Integration as the step to D3.** "All" (D2) becomes "integrates all" (D3): from covering the Dimensions to joining them up.
- **Agent use.** For a claim, name the category, then evidence each criterion in the person's own setting (the Dimensions' lead-ins), using the forBeneficiary versions as prompts.

#### SL6 Recognition categories
| Level | Category (as each Descriptor states) | Route |
|---|---|---|
| `psf:d1` | Associate Fellow | direct claim or accredited programme (recognition.1, recognition.2) |
| `psf:d2` | Fellow | as above |
| `psf:d3` | Senior Fellow | as above |
| `psf:d4` | Principal Fellow | as above |

## Part B Terminology
<!-- label: both; status: drafted; basis: primary -->
`see std:doc:advancehe-psf-dimensions-2023-framework`, Part B: the terms for both PSF documents are held there once (framework rule 4).

## Part C Process
<!-- label: both; status: drafted; basis: primary -->

### C0 Formality
`described`: S2 gives the recognition route in brief; the procedure itself is Advance HE's and an accredited institution's (W-std-0021).

## Part D Sources
```yaml
- key: D1
  issuer: Advance HE (copyright Advance HE, GuildHE, Universities UK)
  title: "Professional Standards Framework for teaching and supporting learning in higher education 2023"
  edition: 2023 (screen-reader compatible version)
  year: 2023
  url: unknown   # www.advance-he.ac.uk named on page 11
  retrieved: "PDF attached by Abbott, 2026-10-03, 09:49"
  licence: "all rights reserved; held by permission (S1)"
  tier: primary
  readVia: direct
  held: 121f42258ca8d09c00a9711ae1f58fbb4ff2371d420c9de1d58dc7d4adfa58a1
  heldFiles: [wkspc2601-library/txt/advance-he-2023-professional-standards-framework-standard.txt, wkspc2601-library/txt/advance-he-2023-professional-standards-framework-standard.norm.txt, wkspc2601-library/records/<name>.held.json]
  citedIn: [S1, S2, S3, S4, S4a, S5, S6, SL]
```

### D2 Research log
```yaml
- { ref: D1, tier: primary, consulted: 2026-10-03, pass: P1, outcome: "read whole, direct; as the Dimensions document's D2 (one held text for both)" }
- { ref: "run-src (in the Dimensions document's folder): psf_data.py, psf_build.py", tier: method, consulted: 2026-10-03, pass: P1, outcome: "built by script with the Dimensions document; spans and verbs checked; `source` holds the issuer's statements; rephrasings checked for no nine-word run of the held text" }
```

### D3 Wanted sources
```yaml
- { w: W-std-0021, citation: "Advance HE's guidance notes for the PSF 2023, one per Descriptor, and its glossary", settles: [S2, S9, C0], asked: not yet, state: wanted }
- { w: W-std-0022, citation: "the UK Professional Standards Framework (UKPSF) 2011, the predecessor, and Advance HE's account of the 2023 review", settles: [S7, S8], asked: not yet, state: wanted }
```

## Part E Gaps and questions
- S1, licence: as the Dimensions document's Part E: source statements held in full on Abbott's permission and direction (10:18, 10:56; D-std-0014).
- S4: the issuer's page for D2 runs "high-" and "quality" across a line; the extraction joins them as one word, kept in the held text as extracted.
- S4, force: the criteria are `threshold`: a claim at a category must evidence all three. The introductions say who a Descriptor suits and are `describes`.
- S4, `requires`: our reading of which Dimensions a criterion names; "appropriate" at D1 is left to the role (`plus: the others that fit the role`).
- S5: the recognition categories are recorded as stated ("aligns with"); no link to the qualification spine is stated or inferred.
- Names, kind and knowledgePath: as the Dimensions document's Part E.

---

## Change notes
- 0.1.2, 3 October 2026, 21:02: moved with its held text from UNI to the source library repo (`wkspc2601-library/ingested/standards/`; texts in `txt/`, records in `records/`); paths only (Abbott, 20:56; std N-0119).
- 0.1.1, 3 October 2026, 10:56: each S4 record now carries the issuer's statement in full (`source`, `quote: full`) for language analysis, beside our rephrasings (Abbott, 10:56; D-std-0014).
- 0.1.0, 3 October 2026, 10:28: researched by run frame 0.1.1-draft and standards run layer 0.6.1-draft, std, run 0068 (P1), with the Dimensions document; held and rephrased on Abbott's permission (D-std-0013).
