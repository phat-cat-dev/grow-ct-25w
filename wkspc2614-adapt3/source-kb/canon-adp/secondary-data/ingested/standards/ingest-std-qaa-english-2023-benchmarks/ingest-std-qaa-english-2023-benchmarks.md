---
id: std:doc:qaa-english-2023-benchmarks
title: "Subject Benchmark Statement English"
profile: standards/subject-benchmark
profileVersion: 0.2.0-draft
issuer: QAA
kind: subject-benchmark
jurisdiction: [UK]
subjectScope: subjects
subjects:
  - { scheme: "hecos", code: "100320", label: "English studies", basis: "stated" }
  - { scheme: "cah", code: "CAH19-01", label: "English studies", basis: "stated" }
  - { scheme: "hecos", code: "100318", label: "English language", basis: "stated" }
  - { scheme: "cah", code: "CAH19-01-02", label: "English language", basis: "stated" }
  - { scheme: "hecos", code: "100319", label: "English literature", basis: "stated" }
  - { scheme: "cah", code: "CAH19-01-03", label: "literature in English", basis: "stated" }
  - { scheme: "hecos", code: "100046", label: "creative writing", basis: "stated" }
  - { scheme: "cah", code: "CAH19-01-05", label: "creative writing", basis: "stated" }
  - { scheme: "cah", code: "CAH19-01-01", label: "English studies (non-specific)", basis: "inferred" }
edition: "September 2023"
published: 2023-09
status: current
supersedes: "Subject Benchmark Statement for English, fourth edition (2019), as section 6 names it"
heldText: { method: sha256-bytes, raw: bff45417af9dda9c64109d5fa641127af39048acb90332de6fd077a6ce6edea9, normalised: 529600ffccd08365aeff3f39ce9ec61be8cba6bf006f7b850f843f402d34fa42 }
heldTextStan: { method: sha256-stan, raw: bff45417af9dda9c64109d5fa641127af39048acb90332de6fd077a6ce6edea9, normalised: 8de5404b5a467bf72ab8bcf1fa9aed2bff178718a840dcaa7991b0eb26219e2c }
licence: "QAA copyright; held for study, private to the project, never published"
series: "QAA Subject Benchmark Statements, 2023 revision with the cross-cutting themes (fifth edition of this statement, inferred)"
awardsCovered: ["bachelor's with honours"]
levelsCovered: ["fheq:6", "fqheis:10"]
nations: ["England", "Wales", "Scotland", "Northern Ireland"]
parts:
  S: full
  B: "partial: no glossary in the document (it points to QAA's Glossary); terms it defines in passing"
  C: "not-applicable: the document sets expectations, not a procedure"
pins: { structure: 0.13.0-draft, template: 0.8.0-draft, benchmarkTemplate: 0.6.0-draft, runFrame: 0.1.1-draft, runLayer: 0.7.0-draft, standards: none yet, terminology: none yet }
lifecycle: drafted
researchedBy: run frame 0.1.1-draft; standards run layer 0.7.0-draft; std, run 0105 (tools/bm_build.py)
passes:
  P1: "2026-10-03 17:11"
  P2: "skipped: read direct from the held text; inferred codes and rung links are for P3"
  P3: open
version: 0.1.2
---

<!-- from INGEST wpk-0016-ingest-pd-template-standards.md 0.8.0-draft and wpk-0016-ingest-pd-template-standards-benchmark.md 0.6.0-draft; built by tools/bm_build.py from run-src/ -->
# Subject Benchmark Statement: English (QAA, September 2023)

> Run 0105, P1 by std. The issuer's words are held in the source library, `wkspc2601-library/txt/qaa-2023-english-subject-benchmark-statement-standard.norm.txt`; each S4 record carries its statement in full (`source`) for language analysis, with its span. Paraphrases and versions are ours. Private to the project, never published. In front matter `status` is the issuer's; ours is `lifecycle`. Doubts are in Part E.

## Part 0 Summary

### 0.1 Agent definition
<!-- label: editorial; status: drafted; basis: primary -->
QAA's UK reference point for what an honours graduate in English, across language, literature and creative writing, knows, understands and can do. Its standards form one table with three columns (threshold, typical, excellent) and rows for generic skills; subject knowledge; embedded equality, access, sustainability and enterprise; creative writing. It stands beside two earlier outcome lists. Reach for it when designing, reviewing or describing an English course, its modules or its outcomes. It is not a curriculum and not a regulatory requirement in England.

### 0.2 Summary
<!-- label: both; status: drafted; basis: primary -->
Published by QAA in September 2023, the statement covers English in its broad sense (language, literature and creative writing, in single, joint and interdisciplinary honours courses) and sets out the subject's purposes, its distinctive features (design, progression, flexibility, partnership, review) and its content, teaching and assessment. Its benchmark standards for the bachelor's degree with honours are a single table read across three columns: 26 threshold items, 27 typical items and 33 excellent records (the excellent rung's defining paragraph and 32 items), with a paragraph on subject knowledge that spans all three. Earlier lists say what English graduates can do (1.6) and will know about (2.2). It carries the four cross-cutting themes (equality, diversity and inclusion; accessibility; education for sustainable development; enterprise and entrepreneurship education) and treats large language models under academic integrity. It cites FHEQ Level 6 with FQHEIS Level 10 and Annex D for the honours classifications; it names UNESCO and points to the Creative Writing and Linguistics statements, but names no professional body for the subject.

## Part S Standard

### S1 Identity
<!-- label: source; status: drafted; basis: primary -->
```yaml
issuer: The Quality Assurance Agency for Higher Education
title: "Subject Benchmark Statement English"
edition: "September 2023"
dates:
  published: 2023-09
  other: []
kind: subject-benchmark
jurisdiction: [UK]
authority: "reference: a sector reference point, not a regulatory requirement (D1, front matter)"
licence: "QAA copyright; the document gives no re-use terms in its text (D1, front matter)"
copyrightNotice: { text: "© The Quality Assurance Agency for Higher Education 2023", locator: "D1, index" }
```

### S2 Purpose and scope
<!-- label: source; status: drafted; basis: primary -->
```yaml
governs: "what can be expected of an English graduate at the end of an honours degree, and what courses in the subject provide"
appliesTo:
  awards: ["bachelor's with honours"]
  levels: ["fheq:6", "fqheis:10"]
  providers: ["UK higher education providers"]
whoMustUse: "none-stated; it is a reference point, not a requirement (D1, front matter)"
howUsed: ["design", "approval", "review", "other: external examining; PSRBs; information for prospective students and employers"]
doesNot: "it is not a national curriculum and does not prescribe teaching, learning or assessment; it carries no statutory or regulatory requirement (D1, front matter)"
beneficiary: the student
statedScope: "\"This document is a QAA Subject Benchmark Statement for English that defines what can be expected of a graduate in the subject, in terms of what they might know, do and understand at the end of their studies.\" (D1, front matter)"
statedSubjects:
  - { name: "English (language, literature and creative writing, in its broadest sense)", locator: "(D1, 1.1, 1.2)", kind: "subject", codes: [{ scheme: "hecos", code: "100320", label: "English studies" }, { scheme: "cah", code: "CAH19-01", label: "English studies" }] }
  - { name: "English Literature; English Language; English Language and Literature; English Literature and Creative Writing", locator: "(D1, 1.1)", kind: "programme title", codes: [{ scheme: "hecos", code: "100319", label: "English literature" }, { scheme: "hecos", code: "100318", label: "English language" }, { scheme: "hecos", code: "100046", label: "creative writing" }] }
  - { name: "joint, combined and major-minor degrees with English", locator: "(D1, 1.1, 2.5)", kind: "programme title", codes: [] }
  - { name: "undergraduate courses leading to a named award with English in its title (postgraduate provision outside scope)", locator: "(D1, 1.3)", kind: "programme title", codes: [] }
subjects: see front matter (subjectScope subjects)
```

### S3 Structure
<!-- label: both; status: drafted; basis: primary -->
```yaml
components:
  - { number: "1.1", order: 3, componentType: paragraph, parent: "section 1", heading: "Context and purposes of an English Degree", gloss: "language, literature and creative writing; single, joint and interdisciplinary honours; course titles" }
  - { number: "1.2", order: 4, componentType: paragraph, parent: "section 1", heading: "Context and purposes of an English Degree", gloss: "English in its broad sense; neighbouring subjects; Linguistics and Creative Writing statements" }
  - { number: "1.3", order: 5, componentType: paragraph, parent: "section 1", heading: "Context and purposes of an English Degree", gloss: "scope limited to undergraduate named awards; postgraduate provision noted" }
  - { number: "1.4", order: 6, componentType: paragraph, parent: "section 1", heading: "Purposes and characteristics of an English Degree", gloss: "studying meaning through communication; what the subject enables" }
  - { number: "1.5", order: 7, componentType: stem, parent: "section 1", heading: "Purposes and characteristics of an English Degree", gloss: "capacities shared with the SHAPE subjects (a list)" }
  - { number: "1.6", order: 8, componentType: stem, parent: "section 1", heading: "Purposes and characteristics of an English Degree", gloss: "what English graduates can do (an outcome list)" }
  - { number: "1.7", order: 9, componentType: paragraph, parent: "section 1", heading: "Purposes and characteristics of an English Degree", gloss: "dialogue, debate and difference in teaching" }
  - { number: "1.8", order: 10, componentType: paragraph, parent: "section 1", heading: "Equality, diversity and inclusion", gloss: "diversity, plural voices and contested narratives" }
  - { number: "1.9", order: 11, componentType: paragraph, parent: "section 1", heading: "Equality, diversity and inclusion", gloss: "the history of the discipline and persistent imbalances" }
  - { number: "1.10", order: 12, componentType: paragraph, parent: "section 1", heading: "Equality, diversity and inclusion", gloss: "diversifying curricula; core and optional" }
  - { number: "1.11", order: 13, componentType: paragraph, parent: "section 1", heading: "Equality, diversity and inclusion", gloss: "graduates who argue well and attend to audiences" }
  - { number: "1.12", order: 14, componentType: paragraph, parent: "section 1", heading: "Accessibility", gloss: "accessible courses and attention to practical challenges" }
  - { number: "1.13", order: 15, componentType: paragraph, parent: "section 1", heading: "Accessibility", gloss: "routes of entry; international and adult students" }
  - { number: "1.14", order: 16, componentType: paragraph, parent: "section 1", heading: "Education for Sustainable Development", gloss: "ESD defined; English working towards it" }
  - { number: "1.15", order: 17, componentType: paragraph, parent: "section 1", heading: "Education for Sustainable Development", gloss: "environment, ecocriticism, world literatures and global citizenship" }
  - { number: "1.16", order: 18, componentType: paragraph, parent: "section 1", heading: "Education for Sustainable Development", gloss: "creativity and sustainable futures" }
  - { number: "1.17", order: 19, componentType: paragraph, parent: "section 1", heading: "Enterprise and entrepreneurship education", gloss: "what enterprise education supports" }
  - { number: "1.18", order: 20, componentType: paragraph, parent: "section 1", heading: "Enterprise and entrepreneurship education", gloss: "four core abilities; careers and value" }
  - { number: "1.19", order: 21, componentType: paragraph, parent: "section 1", heading: "Enterprise and entrepreneurship education", gloss: "communication and context as enterprise" }
  - { number: "1.20", order: 22, componentType: paragraph, parent: "section 1", heading: "Enterprise and entrepreneurship education", gloss: "collaboration, self-management and integrity" }
  - { number: "1.21", order: 23, componentType: paragraph, parent: "section 1", heading: "Enterprise and entrepreneurship education", gloss: "creativity, resilience and new technologies" }
  - { number: "1.22", order: 24, componentType: paragraph, parent: "section 1", heading: "Enterprise and entrepreneurship education", gloss: "critical thinking and problem-solving for enterprise" }
  - { number: "2.1", order: 26, componentType: paragraph, parent: "section 2", heading: "Design", gloss: "varied approaches across the sector" }
  - { number: "2.2", order: 27, componentType: stem, parent: "section 2", heading: "Design", gloss: "what graduates will know about (an outcome list)" }
  - { number: "2.3", order: 28, componentType: paragraph, parent: "section 2", heading: "Design", gloss: "pointer to the content paragraphs (a reference)" }
  - { number: "2.4", order: 29, componentType: paragraph, parent: "section 2", heading: "Progression", gloss: "progression across levels to the threshold; postgraduate study" }
  - { number: "2.5", order: 30, componentType: paragraph, parent: "section 2", heading: "Progression", gloss: "combined, joint and major-minor routes" }
  - { number: "2.6", order: 31, componentType: paragraph, parent: "section 2", heading: "Progression", gloss: "exit awards; course length in the four nations" }
  - { number: "2.7", order: 32, componentType: practice, parent: "section 2", heading: "Accessibility and flexibility", gloss: "flexible and accessible teaching and assessment (examples)" }
  - { number: "2.8", order: 33, componentType: paragraph, parent: "section 2", heading: "Partnership", gloss: "placements and partner organisations" }
  - { number: "2.9", order: 34, componentType: paragraph, parent: "section 2", heading: "Monitoring and review", gloss: "monitoring and periodic review" }
  - { number: "2.10", order: 35, componentType: paragraph, parent: "section 2", heading: "Monitoring and review", gloss: "external reviewers in periodic review" }
  - { number: "2.11", order: 36, componentType: paragraph, parent: "section 2", heading: "Monitoring and review", gloss: "external examiners and threshold standards" }
  - { number: "2.12", order: 37, componentType: paragraph, parent: "section 2", heading: "Monitoring and review", gloss: "accreditation for vocational outcomes" }
  - { number: "3.1", order: 39, componentType: paragraph, parent: "section 3", heading: "Content", gloss: "varied design; combinations with other subjects" }
  - { number: "3.2", order: 40, componentType: area, parent: "section 3", heading: "Content", gloss: "English language: varieties, methods and sub-disciplines" }
  - { number: "3.3", order: 41, componentType: area, parent: "section 3", heading: "Content", gloss: "English literature: periods, forms, contexts and theory" }
  - { number: "3.4", order: 42, componentType: area, parent: "section 3", heading: "Content", gloss: "creative writing within English" }
  - { number: "3.5", order: 43, componentType: practice, parent: "section 3", heading: "Teaching and learning", gloss: "dialogue, collaboration and co-creation in teaching" }
  - { number: "3.6", order: 44, componentType: practice, parent: "section 3", heading: "Teaching and learning", gloss: "structured preparation for classes" }
  - { number: "3.7", order: 45, componentType: practice, parent: "section 3", heading: "Teaching and learning", gloss: "independent study and flipped lectures" }
  - { number: "3.8", order: 46, componentType: practice, parent: "section 3", heading: "Teaching and learning", gloss: "small-group teaching" }
  - { number: "3.9", order: 47, componentType: practice, parent: "section 3", heading: "Teaching and learning", gloss: "libraries, corpora and the capstone project" }
  - { number: "3.10", order: 48, componentType: practice, parent: "section 3", heading: "Assessment", gloss: "diverse assessment; accessibility" }
  - { number: "3.11", order: 49, componentType: practice, parent: "section 3", heading: "Assessment", gloss: "forms of assessment (a list)" }
  - { number: "3.12", order: 50, componentType: practice, parent: "section 3", heading: "Assessment", gloss: "what assessment rewards (a list)" }
  - { number: "4.1", order: 52, componentType: paragraph, parent: "section 4", heading: "Introduction", gloss: "the threshold as the minimum for honours" }
  - { number: "4.2", order: 53, componentType: stem, parent: "section 4", heading: "Introduction", gloss: "Annex D; the three-column standards table" }
  - { number: "1", componentType: section, parent: none, heading: "Context and purposes of an English Degree", gloss: "section 1" }
  - { number: "2", componentType: section, parent: none, heading: "Distinctive features of an English Degree", gloss: "section 2" }
  - { number: "3", componentType: section, parent: none, heading: "Content, structure and delivery", gloss: "section 3" }
  - { number: "4", componentType: section, parent: none, heading: "Benchmark standards", gloss: "section 4" }
excluded:
  - { number: "none", heading: "Contents; About this Statement; How can I use this document?; Relationship to legislation; Additional sector reference points", kind: "other: front matter, read for S1, S2, S7 and SB6" }
  - { number: "1, 2, 3, 4", heading: "section heading lines", kind: "other: headings, recorded in SECTIONS" }
  - { number: "5", heading: "List of references and further resources", kind: "other: four references, read for SB6" }
  - { number: "6", heading: "Membership of the Advisory Groups (2023, 2019, 2015, 2007)", kind: "other: authorship history, read for S7 supersedes" }
```

### S4 Statements
<!-- label: both; status: drafted; basis: primary. Only standards (D-std-0002 (a)): 111 records. `source` is the issuer's statement exactly as its span holds it (D-std-0014). -->
```yaml
- id: qaa/english-2023/1.6.b1
  locator: { number: "1.6.b1", headingPath: ["Context and purposes of an English Degree", "Purposes and characteristics of an English Degree"] }
  span: { start: 10831, end: 10950 }
  source: "read closely, analytically and critically, with an understanding of literary form and historical and linguistic context"
  stem: "1.6"
  statementType: outcome
  rung: none
  force: will
  level: fheq:6
  appliesTo: "graduates in English"
  addressee: learner
  verbs: ["read"]
  about: "close, analytical and critical reading in context"
  themes: [none]
  domain: subject-skill
  award: ["bachelor's with honours"]
  gradeOf: none
  paraphrase: "English graduates can show the capacity to read texts closely and critically, aware of literary form and of the history and language around them."
  quote: full   # the issuer's statement is in `source` (D-std-0014)
  audience: both
  subjects: inherited
- id: qaa/english-2023/1.6.b2
  locator: { number: "1.6.b2", headingPath: ["Context and purposes of an English Degree", "Purposes and characteristics of an English Degree"] }
  span: { start: 10953, end: 11058 }
  source: "understand verbal creativity, including aesthetic and other features of literary and other cultural texts"
  stem: "1.6"
  statementType: outcome
  rung: none
  force: will
  level: fheq:6
  appliesTo: "graduates in English"
  addressee: learner
  verbs: ["understand"]
  about: "verbal creativity and aesthetic features of texts"
  themes: [none]
  domain: understanding
  award: ["bachelor's with honours"]
  gradeOf: none
  paraphrase: "English graduates can show a grasp of creativity in language, including the aesthetic qualities of literary and other cultural works."
  quote: full   # the issuer's statement is in `source` (D-std-0014)
  audience: both
  subjects: inherited
- id: qaa/english-2023/1.6.b3
  locator: { number: "1.6.b3", headingPath: ["Context and purposes of an English Degree", "Purposes and characteristics of an English Degree"] }
  span: { start: 11065, end: 11221 }
  source: "analyse texts and discourses - written and oral, and respond to the affective and rhetorical power of language, using appropriate approaches and terminology"
  stem: "1.6"
  statementType: outcome
  rung: none
  force: will
  level: fheq:6
  appliesTo: "graduates in English"
  addressee: learner
  verbs: ["analyse", "respond", "using"]
  about: "analysing discourse and the force of language"
  themes: [none]
  domain: subject-skill
  award: ["bachelor's with honours"]
  gradeOf: none
  paraphrase: "English graduates can show the capacity to analyse spoken and written texts and discourse and to respond to how language moves and persuades, with fitting methods and terms."
  quote: full   # the issuer's statement is in `source` (D-std-0014)
  audience: both
  subjects: inherited
- id: qaa/english-2023/1.6.b4
  locator: { number: "1.6.b4", headingPath: ["Context and purposes of an English Degree", "Purposes and characteristics of an English Degree"] }
  span: { start: 11224, end: 11293 }
  source: "reflect critically on the acts of reading, writing and interpretation"
  stem: "1.6"
  statementType: outcome
  rung: none
  force: will
  level: fheq:6
  appliesTo: "graduates in English"
  addressee: learner
  verbs: ["reflect"]
  about: "reflecting on reading, writing and interpretation"
  themes: [none]
  domain: subject-skill
  award: ["bachelor's with honours"]
  gradeOf: none
  paraphrase: "English graduates can show critical reflection on what happens when we read, write and interpret."
  quote: full   # the issuer's statement is in `source` (D-std-0014)
  audience: both
  subjects: inherited
- id: qaa/english-2023/1.6.b5
  locator: { number: "1.6.b5", headingPath: ["Context and purposes of an English Degree", "Purposes and characteristics of an English Degree"] }
  span: { start: 11296, end: 11469 }
  source: "develop independent, imaginative and persuasive interpretations of literary, critical, linguistic or creative material, which may include the generation of new creative work"
  stem: "1.6"
  statementType: outcome
  rung: none
  force: will
  level: fheq:6
  appliesTo: "graduates in English"
  addressee: learner
  verbs: ["develop"]
  about: "independent and persuasive interpretations, creative work included"
  themes: [none]
  domain: subject-skill
  award: ["bachelor's with honours"]
  gradeOf: none
  paraphrase: "English graduates can show the capacity to build their own imaginative and convincing readings of literary, critical, linguistic or creative material, possibly by producing new creative work."
  quote: full   # the issuer's statement is in `source` (D-std-0014)
  audience: both
  subjects: inherited
- id: qaa/english-2023/1.6.b6
  locator: { number: "1.6.b6", headingPath: ["Context and purposes of an English Degree", "Purposes and characteristics of an English Degree"] }
  span: { start: 11472, end: 11568 }
  source: "articulate a critical understanding of complex texts and ideas and of their historical relations"
  stem: "1.6"
  statementType: outcome
  rung: none
  force: will
  level: fheq:6
  appliesTo: "graduates in English"
  addressee: learner
  verbs: ["articulate"]
  about: "critical understanding of complex texts and their history"
  themes: [none]
  domain: understanding
  award: ["bachelor's with honours"]
  gradeOf: none
  paraphrase: "English graduates can show the capacity to express a critical grasp of demanding texts and ideas and of how they relate historically."
  quote: full   # the issuer's statement is in `source` (D-std-0014)
  audience: both
  subjects: inherited
- id: qaa/english-2023/1.6.b7
  locator: { number: "1.6.b7", headingPath: ["Context and purposes of an English Degree", "Purposes and characteristics of an English Degree"] }
  span: { start: 11571, end: 11660 }
  source: "communicate - verbally, non-verbally and in writing - clearly, accurately and effectively"
  stem: "1.6"
  statementType: outcome
  rung: none
  force: will
  level: fheq:6
  appliesTo: "graduates in English"
  addressee: learner
  verbs: ["communicate"]
  about: "clear, accurate and effective communication in all modes"
  themes: [none]
  domain: generic-skill
  award: ["bachelor's with honours"]
  gradeOf: none
  paraphrase: "English graduates can show clear, accurate and effective communication, spoken, unspoken and written."
  quote: full   # the issuer's statement is in `source` (D-std-0014)
  audience: both
  subjects: inherited
- id: qaa/english-2023/1.6.b8
  locator: { number: "1.6.b8", headingPath: ["Context and purposes of an English Degree", "Purposes and characteristics of an English Degree"] }
  span: { start: 11663, end: 11740 }
  source: "apply scholarly research and bibliographic skills appropriate to the subject."
  stem: "1.6"
  statementType: outcome
  rung: none
  force: will
  level: fheq:6
  appliesTo: "graduates in English"
  addressee: learner
  verbs: ["apply"]
  about: "scholarly research and bibliographic skills"
  themes: [none]
  domain: generic-skill
  award: ["bachelor's with honours"]
  gradeOf: none
  paraphrase: "English graduates can show the capacity to use research and bibliographic skills that suit the subject."
  quote: full   # the issuer's statement is in `source` (D-std-0014)
  audience: both
  subjects: inherited
- id: qaa/english-2023/2.2.b1
  locator: { number: "2.2.b1", headingPath: ["Distinctive features of an English Degree", "Design"] }
  span: { start: 21291, end: 21327 }
  source: "the expressive resources of language"
  stem: "2.2"
  statementType: outcome
  rung: none
  force: will
  level: fheq:6
  appliesTo: "graduates in English, by the parts of the subject studied"
  addressee: learner
  verbs: []
  about: "the expressive resources of language"
  themes: [none]
  domain: knowledge
  award: ["bachelor's with honours"]
  gradeOf: none
  paraphrase: "Will know about what language offers for expression, depending on which parts of the subject they took."
  quote: full   # the issuer's statement is in `source` (D-std-0014)
  audience: both
  subjects: inherited
- id: qaa/english-2023/2.2.b2
  locator: { number: "2.2.b2", headingPath: ["Distinctive features of an English Degree", "Design"] }
  span: { start: 21330, end: 21453 }
  source: "literature and/or language from different periods and the range of principal literary genres across prose, poetry and drama"
  stem: "2.2"
  statementType: outcome
  rung: none
  force: will
  level: fheq:6
  appliesTo: "graduates in English, by the parts of the subject studied"
  addressee: learner
  verbs: []
  about: "periods and the main literary genres"
  themes: [none]
  domain: knowledge
  award: ["bachelor's with honours"]
  gradeOf: none
  paraphrase: "Will know about literature or language across periods and the chief genres of prose, poetry and drama, depending on which parts of the subject they took."
  quote: full   # the issuer's statement is in `source` (D-std-0014)
  audience: both
  subjects: inherited
- id: qaa/english-2023/2.2.b3
  locator: { number: "2.2.b3", headingPath: ["Distinctive features of an English Degree", "Design"] }
  span: { start: 21456, end: 21493 }
  source: "the breadth of literatures in English"
  stem: "2.2"
  statementType: outcome
  rung: none
  force: will
  level: fheq:6
  appliesTo: "graduates in English, by the parts of the subject studied"
  addressee: learner
  verbs: []
  about: "the range of literatures in English"
  themes: [none]
  domain: knowledge
  award: ["bachelor's with honours"]
  gradeOf: none
  paraphrase: "Will know about how wide the body of literature written in English is, depending on which parts of the subject they took."
  quote: full   # the issuer's statement is in `source` (D-std-0014)
  audience: both
  subjects: inherited
- id: qaa/english-2023/2.2.b4
  locator: { number: "2.2.b4", headingPath: ["Distinctive features of an English Degree", "Design"] }
  span: { start: 21496, end: 21549 }
  source: "regional and global varieties of the English language"
  stem: "2.2"
  statementType: outcome
  rung: none
  force: will
  level: fheq:6
  appliesTo: "graduates in English, by the parts of the subject studied"
  addressee: learner
  verbs: []
  about: "regional and global varieties of English"
  themes: [none]
  domain: knowledge
  award: ["bachelor's with honours"]
  gradeOf: none
  paraphrase: "Will know about the varieties of English spoken and written in regions and around the world, depending on which parts of the subject they took."
  quote: full   # the issuer's statement is in `source` (D-std-0014)
  audience: both
  subjects: inherited
- id: qaa/english-2023/2.2.b5
  locator: { number: "2.2.b5", headingPath: ["Distinctive features of an English Degree", "Design"] }
  span: { start: 21552, end: 21630 }
  source: "the history, structure, levels and discourse functions of the English language"
  stem: "2.2"
  statementType: outcome
  rung: none
  force: will
  level: fheq:6
  appliesTo: "graduates in English, by the parts of the subject studied"
  addressee: learner
  verbs: []
  about: "how English is built and used"
  themes: [none]
  domain: knowledge
  award: ["bachelor's with honours"]
  gradeOf: none
  paraphrase: "Will know about the history, structure, levels and discourse uses of English, depending on which parts of the subject they took."
  quote: full   # the issuer's statement is in `source` (D-std-0014)
  audience: both
  subjects: inherited
- id: qaa/english-2023/2.2.b6
  locator: { number: "2.2.b6", headingPath: ["Distinctive features of an English Degree", "Design"] }
  span: { start: 21633, end: 21742 }
  source: "how culture, language, technology and economics affect how, where and by whom texts are produced and received"
  stem: "2.2"
  statementType: outcome
  rung: none
  force: will
  level: fheq:6
  appliesTo: "graduates in English, by the parts of the subject studied"
  addressee: learner
  verbs: []
  about: "how texts are made and received"
  themes: [none]
  domain: knowledge
  award: ["bachelor's with honours"]
  gradeOf: none
  paraphrase: "Will know about the ways culture, language, technology and economics shape how, where and by whom texts are made and taken up, depending on which parts of the subject they took."
  quote: full   # the issuer's statement is in `source` (D-std-0014)
  audience: both
  subjects: inherited
- id: qaa/english-2023/2.2.b7
  locator: { number: "2.2.b7", headingPath: ["Distinctive features of an English Degree", "Design"] }
  span: { start: 21745, end: 21796 }
  source: "the roles of readers and audiences in shaping texts"
  stem: "2.2"
  statementType: outcome
  rung: none
  force: will
  level: fheq:6
  appliesTo: "graduates in English, by the parts of the subject studied"
  addressee: learner
  verbs: []
  about: "readers and audiences shaping texts"
  themes: [none]
  domain: knowledge
  award: ["bachelor's with honours"]
  gradeOf: none
  paraphrase: "Will know about the part readers and audiences play in shaping texts, depending on which parts of the subject they took."
  quote: full   # the issuer's statement is in `source` (D-std-0014)
  audience: both
  subjects: inherited
- id: qaa/english-2023/2.2.b8
  locator: { number: "2.2.b8", headingPath: ["Distinctive features of an English Degree", "Design"] }
  span: { start: 21799, end: 21861 }
  source: "the relationships between different genres and different media"
  stem: "2.2"
  statementType: outcome
  rung: none
  force: will
  level: fheq:6
  appliesTo: "graduates in English, by the parts of the subject studied"
  addressee: learner
  verbs: []
  about: "relations between genres and media"
  themes: [none]
  domain: knowledge
  award: ["bachelor's with honours"]
  gradeOf: none
  paraphrase: "Will know about how genres and media relate to one another, depending on which parts of the subject they took."
  quote: full   # the issuer's statement is in `source` (D-std-0014)
  audience: both
  subjects: inherited
- id: qaa/english-2023/2.2.b9
  locator: { number: "2.2.b9", headingPath: ["Distinctive features of an English Degree", "Design"] }
  span: { start: 21864, end: 21937 }
  source: "critical, theoretical, linguistic and stylistic concepts and terminology."
  stem: "2.2"
  statementType: outcome
  rung: none
  force: will
  level: fheq:6
  appliesTo: "graduates in English, by the parts of the subject studied"
  addressee: learner
  verbs: []
  about: "critical, theoretical, linguistic and stylistic terms"
  themes: [none]
  domain: knowledge
  award: ["bachelor's with honours"]
  gradeOf: none
  paraphrase: "Will know about the concepts and terms of criticism, theory, linguistics and stylistics, depending on which parts of the subject they took."
  quote: full   # the issuer's statement is in `source` (D-std-0014)
  audience: both
  subjects: inherited
- id: qaa/english-2023/2.4
  locator: { number: "2.4", headingPath: ["Distinctive features of an English Degree", "Progression"] }
  span: { start: 22010, end: 22571 }
  source: "Over the course of a degree with honours (FHEQ Level 6; FQHEIS Level 10), a student of English will progress from one level of study to the next, in line with the regulations and processes for each provider. At each level, the attainment of knowledge, expertise and experience builds towards the final achievement of meeting the threshold-level subject-specific and generic skills listed in this Statement. This will usually include successful completion and the award of credit for the full range of learning and assessment, including any practical components."
  stem: none
  statementType: expectation
  rung: none
  force: will
  level: fheq:6
  appliesTo: "students on an English honours degree"
  addressee: learner
  verbs: ["progress", "builds", "include"]
  about: "progression towards the threshold across the degree"
  themes: [none]
  domain: none
  award: ["bachelor's with honours"]
  gradeOf: none
  paraphrase: "Across an honours degree (FHEQ Level 6; FQHEIS Level 10) an English student will move up through the levels under the provider's rules, each level building towards the threshold skills, usually by completing and gaining credit for all learning and assessment."
  quote: full   # the issuer's statement is in `source` (D-std-0014)
  audience: both
  subjects: inherited
- id: qaa/english-2023/2.5
  locator: { number: "2.5", headingPath: ["Distinctive features of an English Degree", "Progression"] }
  span: { start: 22988, end: 23155 }
  source: "Undergraduates studying a combined, joint or major-minor route will achieve learning outcomes relating to English, and will add more according to their other subjects."
  stem: none
  statementType: expectation
  rung: none
  force: will
  level: fheq:6
  appliesTo: "students on combined, joint or major-minor routes with English"
  addressee: learner
  verbs: ["achieve", "add"]
  about: "outcomes on joint and combined routes"
  themes: [none]
  domain: none
  award: ["bachelor's with honours"]
  gradeOf: none
  paraphrase: "Students on combined, joint or major-minor routes will meet outcomes in English and will gain further ones from their other subjects."
  quote: full   # the issuer's statement is in `source` (D-std-0014)
  audience: both
  subjects: inherited
- id: qaa/english-2023/2.10
  locator: { number: "2.10", headingPath: ["Distinctive features of an English Degree", "Monitoring and review"] }
  span: { start: 26640, end: 26848 }
  source: "Providers will use external reviewers as part of periodic review to gain an external perspective on any proposed changes and ensure threshold standards are achieved and content is appropriate for the subject."
  stem: none
  statementType: expectation
  rung: none
  force: will
  level: none
  appliesTo: "higher education providers"
  addressee: provider
  verbs: ["use", "gain", "ensure"]
  about: "external reviewers in periodic review"
  themes: [none]
  domain: none
  award: ["bachelor's with honours"]
  gradeOf: none
  paraphrase: "Providers will bring in external reviewers during periodic review, for an outside view on proposed changes and to confirm that threshold standards are met and the content suits the subject."
  quote: full   # the issuer's statement is in `source` (D-std-0014)
  audience: practitioner
  subjects: inherited
- id: qaa/english-2023/3.3.s1
  locator: { number: "3.3.s1", headingPath: ["Content, structure and delivery", "Content"] }
  span: { start: 29737, end: 29995 }
  source: "Single honours English Literature students will normally encounter texts from before 1800, and may gain knowledge of literature from one or more early periods (Medieval and Renaissance periods, 17th and 18th centuries), as may some students on joint degrees."
  stem: none
  statementType: expectation
  rung: none
  force: will
  level: fheq:6
  appliesTo: "single honours English Literature students"
  addressee: learner
  verbs: ["encounter", "gain"]
  about: "pre-1800 texts in single honours English Literature"
  themes: [none]
  domain: knowledge
  award: ["bachelor's with honours"]
  gradeOf: none
  paraphrase: "Students on single honours English Literature will normally meet texts written before 1800 and may come to know one or more early periods; some joint students may too."
  quote: full   # the issuer's statement is in `source` (D-std-0014)
  audience: both
  subjects: inherited
- id: qaa/english-2023/4.2
  locator: { number: "4.2", headingPath: ["Benchmark standards", "Introduction"] }
  span: { start: 38099, end: 38328 }
  source: "Each higher education provider has its own method of determining what appropriate evidence of this achievement will be and should refer to Annex D: Outcome classification descriptions for FHEQ Level 6 and FQHEIS Level 10 degrees."
  stem: none
  statementType: expectation
  rung: none
  force: should
  level: fheq:6
  appliesTo: "higher education providers"
  addressee: provider
  verbs: ["determining", "refer"]
  about: "judging achievement above threshold with Annex D"
  themes: [none]
  domain: none
  award: ["bachelor's with honours"]
  gradeOf: none
  paraphrase: "Each provider decides how to evidence achievement above the threshold and should use Annex D, which describes the degree classes for honours at FHEQ Level 6 and FQHEIS Level 10."
  quote: full   # the issuer's statement is in `source` (D-std-0014)
  audience: practitioner
  subjects: inherited
- id: qaa/english-2023/4.2.b1
  locator: { number: "4.2.b1", headingPath: ["Benchmark standards", "Introduction"] }
  span: { start: 39378, end: 39529 }
  source: "communicate clearly verbally, non-verbally and in writing, structuring lucid arguments, using effective expression appropriate to the intended audience"
  stem: "4.2"
  statementType: threshold
  rung: threshold
  force: threshold
  level: fheq:6
  appliesTo: "graduates who studied English as a significant component of their degree, at the threshold level"
  addressee: learner
  verbs: ["communicate", "structuring", "using"]
  about: "clear communication and lucid argument for an audience"
  themes: [none]
  domain: generic-skill
  award: ["bachelor's with honours"]
  gradeOf: none
  paraphrase: "Will have shown, as the minimum for the honours degree, the capacity to get ideas across clearly in speech, other modes and writing, building lucid arguments in a style that suits the audience."
  quote: full   # the issuer's statement is in `source` (D-std-0014)
  audience: both
  subjects: inherited
- id: qaa/english-2023/4.2.ex1
  locator: { number: "4.2.ex1", headingPath: ["Benchmark standards", "Introduction"] }
  span: { start: 38931, end: 39334 }
  source: "Graduates who have attained an excellent standard demonstrate to a higher level the capabilities and skills and show evidence of extensive independent reading, originality of thought and expression, and in-depth understanding. Excellent work displays wide-ranging knowledge of the subject and applies it in subtle and effective ways, showing exceptional critical insight, analytic rigour and creativity."
  stem: none
  statementType: excellent
  rung: excellent
  force: will
  level: fheq:6
  appliesTo: "graduates who have reached the excellent standard"
  addressee: learner
  verbs: ["demonstrate", "show", "displays", "applies"]
  about: "what defines the excellent standard"
  themes: [none]
  domain: understanding
  award: ["bachelor's with honours"]
  gradeOf: none
  paraphrase: "Graduates at the excellent standard show the same capabilities at a higher level, with wide independent reading, original thought and expression and deep understanding; their work brings broad knowledge to bear subtly and effectively, with outstanding critical insight, analytical rigour and creativity."
  quote: full   # the issuer's statement is in `source` (D-std-0014)
  audience: both
  subjects: inherited
- id: qaa/english-2023/4.2.sk1
  locator: { number: "4.2.sk1", headingPath: ["Benchmark standards", "Introduction"] }
  span: { start: 46815, end: 47594 }
  source: "The subject knowledge (including relevant contextual knowledge) will vary depending on the elements of the degree. The breadth, depth and range of knowledge will vary over the threshold, typical and excellent standards. For language elements, this may include the investigation and analysis of spoken, written and multimodal communication and culture; the origins and historical development of English; its regional, national and global circulation; the structure and use of varieties of English; knowledge of key subdisciplinary areas, and of qualitative, quantitative and mixed methods of analysis. Students will understand and deploy critical, theoretical, linguistic and stylistic concepts and terminology, and apply scholarly bibliographic skills appropriate to the subject."
  stem: none
  statementType: expectation
  rung: none
  force: will
  level: fheq:6
  appliesTo: "graduates in English, by the elements of their degree"
  addressee: learner
  verbs: ["vary", "understand", "deploy", "apply"]
  about: "subject knowledge for language elements"
  themes: [none]
  domain: knowledge
  award: ["bachelor's with honours"]
  gradeOf: none
  paraphrase: "Subject knowledge will differ with the parts of the degree and grow in range and depth across the three standards; for language it may cover analysing spoken, written and multimodal communication, the history, spread and varieties of English, its sub-disciplines and methods; students will understand and use the field's concepts and terms and apply scholarly bibliographic skills."
  quote: full   # the issuer's statement is in `source` (D-std-0014)
  audience: both
  subjects: inherited
- id: qaa/english-2023/4.2.b2
  locator: { number: "4.2.b2", headingPath: ["Benchmark standards", "Introduction"] }
  span: { start: 39532, end: 39600 }
  source: "understand writing as a process which includes revision and editing."
  stem: "4.2"
  statementType: threshold
  rung: threshold
  force: threshold
  level: fheq:6
  appliesTo: "graduates who studied English as a significant component of their degree, at the threshold level"
  addressee: learner
  verbs: ["understand"]
  about: "writing as a process of revision and editing"
  themes: [none]
  domain: generic-skill
  award: ["bachelor's with honours"]
  gradeOf: none
  paraphrase: "Will have shown, as the minimum for the honours degree, an understanding that good writing comes through revising and editing."
  quote: full   # the issuer's statement is in `source` (D-std-0014)
  audience: both
  subjects: inherited
- id: qaa/english-2023/4.2.sk2
  locator: { number: "4.2.sk2", headingPath: ["Benchmark standards", "Introduction"] }
  span: { start: 47595, end: 48388 }
  source: "For literature elements, this may include close, analytical reading; knowledge of stylistic, expressive, formal and rhetorical properties of texts; the interconnections between literary texts and other forms of expression; awareness of pre-1800 texts for single honours English; alertness to the social, historical and cultural contexts of the processes of composition and production of texts, the histories of their reception and forms of dissemination. Students will engage with literature and/or language from different periods and from the full range of principal literary genres across prose, poetry and drama; students will understand and deploy critical, theoretical, linguistic and stylistic concepts and terminology and apply scholarly bibliographic skills appropriate to the subject."
  stem: none
  statementType: expectation
  rung: none
  force: will
  level: fheq:6
  appliesTo: "graduates in English, by the elements of their degree"
  addressee: learner
  verbs: ["engage", "understand", "deploy", "apply"]
  about: "subject knowledge for literature elements"
  themes: [none]
  domain: knowledge
  award: ["bachelor's with honours"]
  gradeOf: none
  paraphrase: "For literature it may cover close reading, the stylistic and formal features of texts, links with other forms, pre-1800 texts for single honours and the contexts of production, reception and circulation; students will engage with several periods and the main genres, use the field's concepts and terms and apply scholarly bibliographic skills."
  quote: full   # the issuer's statement is in `source` (D-std-0014)
  audience: both
  subjects: inherited
- id: qaa/english-2023/4.2.b3
  locator: { number: "4.2.b3", headingPath: ["Benchmark standards", "Introduction"] }
  span: { start: 39604, end: 39791 }
  source: "communicate clearly verbally, non-verbally and in writing, structuring lucid, coherent and rigorous arguments using persuasive, effective expression, incorporating the arguments of others"
  stem: "4.2"
  statementType: typical
  rung: typical
  force: will
  level: fheq:6
  appliesTo: "graduates who studied English as a significant component of their degree, at the typical level"
  addressee: learner
  verbs: ["communicate", "structuring", "using", "incorporating"]
  about: "coherent, rigorous argument that draws in other views"
  themes: [none]
  domain: generic-skill
  award: ["bachelor's with honours"]
  gradeOf: { statement: qaa/english-2023/4.2.b1, basis: inferred }
  paraphrase: "Are able to show, at the typical level reached by most honours graduates, clear communication in every mode, with lucid, coherent and rigorous arguments, persuasive expression and other writers' arguments built in."
  quote: full   # the issuer's statement is in `source` (D-std-0014)
  audience: both
  subjects: inherited
- id: qaa/english-2023/4.2.sk3
  locator: { number: "4.2.sk3", headingPath: ["Benchmark standards", "Introduction"] }
  span: { start: 48389, end: 49111 }
  source: "For Creative Writing elements in the context of English, this may include a process of reflection on the development of individual and peer writing practices informed by broad and critical reading of writing produced in a wide range of social, historical and cultural contexts; understanding the complex interactive relationship between writers, publishers, texts and audiences; developing the discipline of writing to specific briefs, and showing awareness of the importance of the drafting process and the benefits of working collaboratively. Students will understand and deploy critical, theoretical, linguistic and stylistic concepts and terminology and apply scholarly bibliographic skills appropriate to the subject."
  stem: none
  statementType: expectation
  rung: none
  force: will
  level: fheq:6
  appliesTo: "graduates in English, by the elements of their degree"
  addressee: learner
  verbs: ["understand", "deploy", "apply"]
  about: "subject knowledge for creative writing elements"
  themes: [none]
  domain: knowledge
  award: ["bachelor's with honours"]
  gradeOf: none
  paraphrase: "For creative writing it may cover reflecting on one's own and peers' writing through wide critical reading, the relations of writer, publisher, text and audience, writing to a brief, drafting and collaboration; students will use the field's concepts and terms and apply scholarly bibliographic skills."
  quote: full   # the issuer's statement is in `source` (D-std-0014)
  audience: both
  subjects: inherited
- id: qaa/english-2023/4.2.b4
  locator: { number: "4.2.b4", headingPath: ["Benchmark standards", "Introduction"] }
  span: { start: 39794, end: 39897 }
  source: "position themselves clearly with respect to those other arguments, appropriate to the intended audience"
  stem: "4.2"
  statementType: typical
  rung: typical
  force: will
  level: fheq:6
  appliesTo: "graduates who studied English as a significant component of their degree, at the typical level"
  addressee: learner
  verbs: ["position"]
  about: "taking a clear stance among others' arguments"
  themes: [none]
  domain: generic-skill
  award: ["bachelor's with honours"]
  gradeOf: none
  paraphrase: "Are able to show, at the typical level reached by most honours graduates, a clear stance of their own in relation to the arguments of others, pitched for the audience."
  quote: full   # the issuer's statement is in `source` (D-std-0014)
  audience: both
  subjects: inherited
- id: qaa/english-2023/4.2.b5
  locator: { number: "4.2.b5", headingPath: ["Benchmark standards", "Introduction"] }
  span: { start: 39900, end: 40016 }
  source: "deploy a reflective approach to the process of writing that deploys revision to improve writing from draft to draft."
  stem: "4.2"
  statementType: typical
  rung: typical
  force: will
  level: fheq:6
  appliesTo: "graduates who studied English as a significant component of their degree, at the typical level"
  addressee: learner
  verbs: ["deploy", "deploys", "improve"]
  about: "reflective revision from draft to draft"
  themes: [none]
  domain: generic-skill
  award: ["bachelor's with honours"]
  gradeOf: { statement: qaa/english-2023/4.2.b2, basis: inferred }
  paraphrase: "Are able to show, at the typical level reached by most honours graduates, a reflective way of writing that uses revision to make each draft better than the last."
  quote: full   # the issuer's statement is in `source` (D-std-0014)
  audience: both
  subjects: inherited
- id: qaa/english-2023/4.2.b6
  locator: { number: "4.2.b6", headingPath: ["Benchmark standards", "Introduction"] }
  span: { start: 40019, end: 40222 }
  source: "communicate clearly, verbally, non-verbally and in writing, including structuring lucid, coherent, rigorous and incisive arguments in support of complex, challenging and cogently expressed central claims"
  stem: "4.2"
  statementType: excellent
  rung: excellent
  force: will
  level: fheq:6
  appliesTo: "graduates who studied English as a significant component of their degree, at the excellent level"
  addressee: learner
  verbs: ["communicate", "structuring"]
  about: "incisive argument for complex, cogent central claims"
  themes: [none]
  domain: generic-skill
  award: ["bachelor's with honours"]
  gradeOf: { statement: qaa/english-2023/4.2.b3, basis: inferred }
  paraphrase: "Are able to show, at the excellent level for the honours degree, clear communication in every mode, including lucid, rigorous and incisive arguments that support complex, demanding and well-expressed central claims."
  quote: full   # the issuer's statement is in `source` (D-std-0014)
  audience: both
  subjects: inherited
- id: qaa/english-2023/4.2.b7
  locator: { number: "4.2.b7", headingPath: ["Benchmark standards", "Introduction"] }
  span: { start: 40225, end: 40332 }
  source: "identify and articulate strengths and weaknesses of the arguments of other writers concisely and accurately"
  stem: "4.2"
  statementType: excellent
  rung: excellent
  force: will
  level: fheq:6
  appliesTo: "graduates who studied English as a significant component of their degree, at the excellent level"
  addressee: learner
  verbs: ["identify", "articulate"]
  about: "concise, accurate assessment of other writers' arguments"
  themes: [none]
  domain: generic-skill
  award: ["bachelor's with honours"]
  gradeOf: { statement: qaa/english-2023/4.2.b4, basis: inferred }
  paraphrase: "Are able to show, at the excellent level for the honours degree, the capacity to name the strengths and weaknesses of other writers' arguments briefly and accurately."
  quote: full   # the issuer's statement is in `source` (D-std-0014)
  audience: both
  subjects: inherited
- id: qaa/english-2023/4.2.b8
  locator: { number: "4.2.b8", headingPath: ["Benchmark standards", "Introduction"] }
  span: { start: 40335, end: 40391 }
  source: "amend and develop positions in light of new evidence and"
  stem: "4.2"
  statementType: excellent
  rung: excellent
  force: will
  level: fheq:6
  appliesTo: "graduates who studied English as a significant component of their degree, at the excellent level"
  addressee: learner
  verbs: ["amend", "develop"]
  about: "revising positions in light of new evidence"
  themes: [none]
  domain: generic-skill
  award: ["bachelor's with honours"]
  gradeOf: none
  paraphrase: "Are able to show, at the excellent level for the honours degree, the capacity to change and extend their positions when new evidence and claims appear (the item continues after a page break)."
  quote: full   # the issuer's statement is in `source` (D-std-0014)
  audience: both
  subjects: inherited
- id: qaa/english-2023/4.2.b9
  locator: { number: "4.2.b9", headingPath: ["Benchmark standards", "Introduction"] }
  span: { start: 40501, end: 40612 }
  source: "deploy a disciplined commitment to their own writing, reading and re-reading their own prose before submission."
  stem: "4.2"
  statementType: excellent
  rung: excellent
  force: will
  level: fheq:6
  appliesTo: "graduates who studied English as a significant component of their degree, at the excellent level"
  addressee: learner
  verbs: ["deploy"]
  about: "disciplined writing habits and re-reading before submission"
  themes: [none]
  domain: generic-skill
  award: ["bachelor's with honours"]
  gradeOf: { statement: qaa/english-2023/4.2.b5, basis: inferred }
  paraphrase: "Are able to show, at the excellent level for the honours degree, a disciplined commitment to their own writing, rereading their prose carefully before handing it in."
  quote: full   # the issuer's statement is in `source` (D-std-0014)
  audience: both
  subjects: inherited
- id: qaa/english-2023/4.2.b10
  locator: { number: "4.2.b10", headingPath: ["Benchmark standards", "Introduction"] }
  span: { start: 40615, end: 40702 }
  source: "recognise that language can have affective power and can manipulate as well as persuade"
  stem: "4.2"
  statementType: threshold
  rung: threshold
  force: threshold
  level: fheq:6
  appliesTo: "graduates who studied English as a significant component of their degree, at the threshold level"
  addressee: learner
  verbs: ["recognise", "manipulate", "persuade"]
  about: "the affective power of language"
  themes: [none]
  domain: subject-skill
  award: ["bachelor's with honours"]
  gradeOf: none
  paraphrase: "Will have shown, as the minimum for the honours degree, a recognition that language carries emotional force and can manipulate as well as persuade."
  quote: full   # the issuer's statement is in `source` (D-std-0014)
  audience: both
  subjects: inherited
- id: qaa/english-2023/4.2.b11
  locator: { number: "4.2.b11", headingPath: ["Benchmark standards", "Introduction"] }
  span: { start: 40705, end: 40811 }
  source: "be aware of implied audiences of texts, and of the need to temper their own writing to specific audiences."
  stem: "4.2"
  statementType: threshold
  rung: threshold
  force: threshold
  level: fheq:6
  appliesTo: "graduates who studied English as a significant component of their degree, at the threshold level"
  addressee: learner
  verbs: ["temper"]
  about: "implied audiences and writing for an audience"
  themes: [none]
  domain: subject-skill
  award: ["bachelor's with honours"]
  gradeOf: none
  paraphrase: "Will have shown, as the minimum for the honours degree, awareness of the audiences texts imply and of the need to adjust their own writing to particular readers."
  quote: full   # the issuer's statement is in `source` (D-std-0014)
  audience: both
  subjects: inherited
- id: qaa/english-2023/4.2.b12
  locator: { number: "4.2.b12", headingPath: ["Benchmark standards", "Introduction"] }
  span: { start: 40814, end: 40983 }
  source: "recognise and respond to the affective power of language, using appropriate approaches and terminology, and to communicate clearly and coherently to different audiences."
  stem: "4.2"
  statementType: typical
  rung: typical
  force: will
  level: fheq:6
  appliesTo: "graduates who studied English as a significant component of their degree, at the typical level"
  addressee: learner
  verbs: ["recognise", "respond", "using", "communicate"]
  about: "responding to affective language and writing for different audiences"
  themes: [none]
  domain: subject-skill
  award: ["bachelor's with honours"]
  gradeOf: { statement: qaa/english-2023/4.2.b10, basis: inferred }
  paraphrase: "Are able to show, at the typical level reached by most honours graduates, recognition of and response to the emotional force of language, with fitting methods and terms, and clear, coherent communication to varied audiences."
  quote: full   # the issuer's statement is in `source` (D-std-0014)
  audience: both
  subjects: inherited
- id: qaa/english-2023/4.2.b13
  locator: { number: "4.2.b13", headingPath: ["Benchmark standards", "Introduction"] }
  span: { start: 40986, end: 41105 }
  source: "analyse the affective power of language, using approaches and terminology appropriate to specific and defined audiences"
  stem: "4.2"
  statementType: excellent
  rung: excellent
  force: will
  level: fheq:6
  appliesTo: "graduates who studied English as a significant component of their degree, at the excellent level"
  addressee: learner
  verbs: ["analyse", "using"]
  about: "analysing affective language for defined audiences"
  themes: [none]
  domain: subject-skill
  award: ["bachelor's with honours"]
  gradeOf: { statement: qaa/english-2023/4.2.b12, basis: inferred }
  paraphrase: "Are able to show, at the excellent level for the honours degree, analysis of the emotional force of language, using methods and terms suited to specific, defined audiences."
  quote: full   # the issuer's statement is in `source` (D-std-0014)
  audience: both
  subjects: inherited
- id: qaa/english-2023/4.2.b14
  locator: { number: "4.2.b14", headingPath: ["Benchmark standards", "Introduction"] }
  span: { start: 41108, end: 41292 }
  source: "exceptional students have a command of rhetoric that enables them to persuade and sometimes move their own readers and are adroit in handling sensitive topics and challenging material."
  stem: "4.2"
  statementType: excellent
  rung: excellent
  force: will
  level: fheq:6
  appliesTo: "graduates who studied English as a significant component of their degree, at the excellent level"
  addressee: learner
  verbs: ["have", "enables", "persuade", "move"]
  about: "command of rhetoric; handling sensitive material"
  themes: [none]
  domain: subject-skill
  award: ["bachelor's with honours"]
  gradeOf: none
  paraphrase: "Are able to show, at the excellent level for the honours degree, a command of rhetoric that lets them persuade and at times move their readers, with deftness in handling sensitive topics and difficult material."
  quote: full   # the issuer's statement is in `source` (D-std-0014)
  audience: both
  subjects: inherited
- id: qaa/english-2023/4.2.b15
  locator: { number: "4.2.b15", headingPath: ["Benchmark standards", "Introduction"] }
  span: { start: 41295, end: 41391 }
  source: "be comfortable with technology and digital communication and use a variety of digital platforms."
  stem: "4.2"
  statementType: threshold
  rung: threshold
  force: threshold
  level: fheq:6
  appliesTo: "graduates who studied English as a significant component of their degree, at the threshold level"
  addressee: learner
  verbs: ["use"]
  about: "comfort with technology and digital platforms"
  themes: [none]
  domain: generic-skill
  award: ["bachelor's with honours"]
  gradeOf: none
  paraphrase: "Will have shown, as the minimum for the honours degree, ease with technology and digital communication and use of a range of digital platforms."
  quote: full   # the issuer's statement is in `source` (D-std-0014)
  audience: both
  subjects: inherited
- id: qaa/english-2023/4.2.b16
  locator: { number: "4.2.b16", headingPath: ["Benchmark standards", "Introduction"] }
  span: { start: 41394, end: 41510 }
  source: "be comfortable with technology and digital communication and able to confidently use a variety of digital platforms."
  stem: "4.2"
  statementType: typical
  rung: typical
  force: will
  level: fheq:6
  appliesTo: "graduates who studied English as a significant component of their degree, at the typical level"
  addressee: learner
  verbs: ["use"]
  about: "confident use of digital platforms"
  themes: [none]
  domain: generic-skill
  award: ["bachelor's with honours"]
  gradeOf: { statement: qaa/english-2023/4.2.b15, basis: inferred }
  paraphrase: "Are able to show, at the typical level reached by most honours graduates, ease with technology and digital communication and confident use of a range of digital platforms."
  quote: full   # the issuer's statement is in `source` (D-std-0014)
  audience: both
  subjects: inherited
- id: qaa/english-2023/4.2.b17
  locator: { number: "4.2.b17", headingPath: ["Benchmark standards", "Introduction"] }
  span: { start: 41513, end: 41627 }
  source: "deploy multiple digital platforms and may inventively exploit new technologies in the communication of their work."
  stem: "4.2"
  statementType: excellent
  rung: excellent
  force: will
  level: fheq:6
  appliesTo: "graduates who studied English as a significant component of their degree, at the excellent level"
  addressee: learner
  verbs: ["deploy", "exploit"]
  about: "inventive use of new technologies to communicate"
  themes: [none]
  domain: generic-skill
  award: ["bachelor's with honours"]
  gradeOf: { statement: qaa/english-2023/4.2.b16, basis: inferred }
  paraphrase: "Are able to show, at the excellent level for the honours degree, use of several digital platforms, possibly with inventive use of new technologies to communicate their work."
  quote: full   # the issuer's statement is in `source` (D-std-0014)
  audience: both
  subjects: inherited
- id: qaa/english-2023/4.2.b18
  locator: { number: "4.2.b18", headingPath: ["Benchmark standards", "Introduction"] }
  span: { start: 41630, end: 41732 }
  source: "both collaborate and work independently showing autonomy, flexibility, resilience and self- management"
  stem: "4.2"
  statementType: threshold
  rung: threshold
  force: threshold
  level: fheq:6
  appliesTo: "graduates who studied English as a significant component of their degree, at the threshold level"
  addressee: learner
  verbs: ["collaborate", "work"]
  about: "collaboration and independent work with self-management"
  themes: [none]
  domain: generic-skill
  award: ["bachelor's with honours"]
  gradeOf: none
  paraphrase: "Will have shown, as the minimum for the honours degree, the capacity to work with others and on their own, showing autonomy, adaptability, resilience and self-management."
  quote: full   # the issuer's statement is in `source` (D-std-0014)
  audience: both
  subjects: inherited
- id: qaa/english-2023/4.2.b19
  locator: { number: "4.2.b19", headingPath: ["Benchmark standards", "Introduction"] }
  span: { start: 41735, end: 41786 }
  source: "develop working relationships with others in teams."
  stem: "4.2"
  statementType: threshold
  rung: threshold
  force: threshold
  level: fheq:6
  appliesTo: "graduates who studied English as a significant component of their degree, at the threshold level"
  addressee: learner
  verbs: ["develop"]
  about: "working relationships in teams"
  themes: [none]
  domain: generic-skill
  award: ["bachelor's with honours"]
  gradeOf: none
  paraphrase: "Will have shown, as the minimum for the honours degree, the capacity to build working relationships with others in a team."
  quote: full   # the issuer's statement is in `source` (D-std-0014)
  audience: both
  subjects: inherited
- id: qaa/english-2023/4.2.b20
  locator: { number: "4.2.b20", headingPath: ["Benchmark standards", "Introduction"] }
  span: { start: 41789, end: 42116 }
  source: "both collaborate and work independently, showing autonomy, flexibility, resilience and self- management; demonstrate skills essential to teamwork - such as constructive dialogue (for example, listening, asking and responding to questions); and adopt discrete tasks and roles within a group - such as rapporteur, scribe, leader."
  stem: "4.2"
  statementType: typical
  rung: typical
  force: will
  level: fheq:6
  appliesTo: "graduates who studied English as a significant component of their degree, at the typical level"
  addressee: learner
  verbs: ["collaborate", "work", "demonstrate", "adopt"]
  about: "teamwork skills and roles within a group"
  themes: [none]
  domain: generic-skill
  award: ["bachelor's with honours"]
  gradeOf: { statement: qaa/english-2023/4.2.b18, basis: inferred }
  paraphrase: "Are able to show, at the typical level reached by most honours graduates, collaboration and independent work with autonomy, adaptability, resilience and self-management, the core skills of teamwork such as listening and answering questions constructively; and the taking of set tasks and roles in a group."
  quote: full   # the issuer's statement is in `source` (D-std-0014)
  audience: both
  subjects: inherited
- id: qaa/english-2023/4.2.b21
  locator: { number: "4.2.b21", headingPath: ["Benchmark standards", "Introduction"] }
  span: { start: 42119, end: 42222 }
  source: "both collaborate and work independently, showing autonomy, flexibility, resilience and self- management"
  stem: "4.2"
  statementType: excellent
  rung: excellent
  force: will
  level: fheq:6
  appliesTo: "graduates who studied English as a significant component of their degree, at the excellent level"
  addressee: learner
  verbs: ["collaborate", "work"]
  about: "collaboration and independence at the excellent level"
  themes: [none]
  domain: generic-skill
  award: ["bachelor's with honours"]
  gradeOf: { statement: qaa/english-2023/4.2.b20, basis: inferred }
  paraphrase: "Are able to show, at the excellent level for the honours degree, work with others and on their own, showing autonomy, adaptability, resilience and self-management (the same wording as the threshold item)."
  quote: full   # the issuer's statement is in `source` (D-std-0014)
  audience: both
  subjects: inherited
- id: qaa/english-2023/4.2.b22
  locator: { number: "4.2.b22", headingPath: ["Benchmark standards", "Introduction"] }
  span: { start: 42225, end: 42370 }
  source: "be a proficient participator in teamwork: listen to others, ask intelligent questions and respond constructively to questions, even critical ones"
  stem: "4.2"
  statementType: excellent
  rung: excellent
  force: will
  level: fheq:6
  appliesTo: "graduates who studied English as a significant component of their degree, at the excellent level"
  addressee: learner
  verbs: ["listen", "ask", "respond"]
  about: "skilled participation in teamwork"
  themes: [none]
  domain: generic-skill
  award: ["bachelor's with honours"]
  gradeOf: { statement: qaa/english-2023/4.2.b20, basis: inferred }
  paraphrase: "Are able to show, at the excellent level for the honours degree, skilled teamwork: listening, asking searching questions and answering even critical questions constructively."
  quote: full   # the issuer's statement is in `source` (D-std-0014)
  audience: both
  subjects: inherited
- id: qaa/english-2023/4.2.b23
  locator: { number: "4.2.b23", headingPath: ["Benchmark standards", "Introduction"] }
  span: { start: 42373, end: 42460 }
  source: "be adept in encompassing a wide range of perspectives, attitudes, ethics and ideologies"
  stem: "4.2"
  statementType: excellent
  rung: excellent
  force: will
  level: fheq:6
  appliesTo: "graduates who studied English as a significant component of their degree, at the excellent level"
  addressee: learner
  verbs: ["encompassing"]
  about: "holding many perspectives and ideologies"
  themes: [none]
  domain: generic-skill
  award: ["bachelor's with honours"]
  gradeOf: none
  paraphrase: "Are able to show, at the excellent level for the honours degree, skill in taking in a broad range of viewpoints, attitudes, ethics and ideologies."
  quote: full   # the issuer's statement is in `source` (D-std-0014)
  audience: both
  subjects: inherited
- id: qaa/english-2023/4.2.b24
  locator: { number: "4.2.b24", headingPath: ["Benchmark standards", "Introduction"] }
  span: { start: 42463, end: 42633 }
  source: "be often essential to their group's success, either in an overt leadership role, or through skills - such as the negotiation of disagreement so as to arrive at consensus."
  stem: "4.2"
  statementType: excellent
  rung: excellent
  force: will
  level: fheq:6
  appliesTo: "graduates who studied English as a significant component of their degree, at the excellent level"
  addressee: learner
  verbs: ["arrive"]
  about: "being central to a group's success, through leadership or negotiation"
  themes: [none]
  domain: generic-skill
  award: ["bachelor's with honours"]
  gradeOf: none
  paraphrase: "Are able to show, at the excellent level for the honours degree, frequent importance to their group's success, either by leading openly or through skills such as negotiating disagreement to reach agreement."
  quote: full   # the issuer's statement is in `source` (D-std-0014)
  audience: both
  subjects: inherited
- id: qaa/english-2023/4.2.b25
  locator: { number: "4.2.b25", headingPath: ["Benchmark standards", "Introduction"] }
  span: { start: 42698, end: 42829 }
  source: "be creative; develop interpretations of literary, critical, linguistic or creative material in interpretative and written practice."
  stem: "4.2"
  statementType: threshold
  rung: threshold
  force: threshold
  level: fheq:6
  appliesTo: "graduates who studied English as a significant component of their degree, at the threshold level"
  addressee: learner
  verbs: ["develop"]
  about: "creativity and interpretation of material"
  themes: [none]
  domain: subject-skill
  award: ["bachelor's with honours"]
  gradeOf: none
  paraphrase: "Will have shown, as the minimum for the honours degree, creativity, developing readings of literary, critical, linguistic or creative material in their interpretation and writing."
  quote: full   # the issuer's statement is in `source` (D-std-0014)
  audience: both
  subjects: inherited
- id: qaa/english-2023/4.2.b26
  locator: { number: "4.2.b26", headingPath: ["Benchmark standards", "Introduction"] }
  span: { start: 42833, end: 43026 }
  source: "be creative; develop independent and imaginative interpretations of literary, critical, linguistic or creative material, showing independence of approach in interpretative and written practice."
  stem: "4.2"
  statementType: typical
  rung: typical
  force: will
  level: fheq:6
  appliesTo: "graduates who studied English as a significant component of their degree, at the typical level"
  addressee: learner
  verbs: ["develop", "showing"]
  about: "independent, imaginative interpretation"
  themes: [none]
  domain: subject-skill
  award: ["bachelor's with honours"]
  gradeOf: { statement: qaa/english-2023/4.2.b25, basis: inferred }
  paraphrase: "Are able to show, at the typical level reached by most honours graduates, creativity, with independent and imaginative readings of literary, critical, linguistic or creative material and an independent approach in their interpretation and writing."
  quote: full   # the issuer's statement is in `source` (D-std-0014)
  audience: both
  subjects: inherited
- id: qaa/english-2023/4.2.b27
  locator: { number: "4.2.b27", headingPath: ["Benchmark standards", "Introduction"] }
  span: { start: 43030, end: 43238 }
  source: "be creative, develop independent and imaginative interpretations of literary, critical, linguistic or creative material showing independence and originality of approach in interpretative and written practice."
  stem: "4.2"
  statementType: excellent
  rung: excellent
  force: will
  level: fheq:6
  appliesTo: "graduates who studied English as a significant component of their degree, at the excellent level"
  addressee: learner
  verbs: ["develop", "showing"]
  about: "original, independent interpretation"
  themes: [none]
  domain: subject-skill
  award: ["bachelor's with honours"]
  gradeOf: { statement: qaa/english-2023/4.2.b26, basis: inferred }
  paraphrase: "Are able to show, at the excellent level for the honours degree, creativity, with independent and imaginative readings of literary, critical, linguistic or creative material that show originality as well as independence in interpretation and writing."
  quote: full   # the issuer's statement is in `source` (D-std-0014)
  audience: both
  subjects: inherited
- id: qaa/english-2023/4.2.b28
  locator: { number: "4.2.b28", headingPath: ["Benchmark standards", "Introduction"] }
  span: { start: 43241, end: 43322 }
  source: "think critically and display powers of understanding, analysis and interpretation"
  stem: "4.2"
  statementType: threshold
  rung: threshold
  force: threshold
  level: fheq:6
  appliesTo: "graduates who studied English as a significant component of their degree, at the threshold level"
  addressee: learner
  verbs: ["think", "display"]
  about: "critical thinking: understanding, analysis and interpretation"
  themes: [none]
  domain: generic-skill
  award: ["bachelor's with honours"]
  gradeOf: none
  paraphrase: "Will have shown, as the minimum for the honours degree, critical thought, with the capacity to understand, analyse and interpret."
  quote: full   # the issuer's statement is in `source` (D-std-0014)
  audience: both
  subjects: inherited
- id: qaa/english-2023/4.2.b29
  locator: { number: "4.2.b29", headingPath: ["Benchmark standards", "Introduction"] }
  span: { start: 43325, end: 43421 }
  source: "articulate a critical understanding of complex texts and ideas and of their historical relations"
  stem: "4.2"
  statementType: threshold
  rung: threshold
  force: threshold
  level: fheq:6
  appliesTo: "graduates who studied English as a significant component of their degree, at the threshold level"
  addressee: learner
  verbs: ["articulate"]
  about: "critical understanding of complex texts and their history"
  themes: [none]
  domain: understanding
  award: ["bachelor's with honours"]
  gradeOf: none
  paraphrase: "Will have shown, as the minimum for the honours degree, the capacity to express a critical grasp of demanding texts and ideas and of how they relate over time."
  quote: full   # the issuer's statement is in `source` (D-std-0014)
  audience: both
  subjects: inherited
- id: qaa/english-2023/4.2.b30
  locator: { number: "4.2.b30", headingPath: ["Benchmark standards", "Introduction"] }
  span: { start: 43424, end: 43548 }
  source: "reflect critically upon the acts of reading and writing; evaluate literary and linguistic forms and other cultural artefacts"
  stem: "4.2"
  statementType: threshold
  rung: threshold
  force: threshold
  level: fheq:6
  appliesTo: "graduates who studied English as a significant component of their degree, at the threshold level"
  addressee: learner
  verbs: ["reflect", "evaluate"]
  about: "reflecting on reading and writing; evaluating forms and artefacts"
  themes: [none]
  domain: subject-skill
  award: ["bachelor's with honours"]
  gradeOf: none
  paraphrase: "Will have shown, as the minimum for the honours degree, critical reflection on reading and writing, and evaluation of literary and linguistic forms and other cultural artefacts."
  quote: full   # the issuer's statement is in `source` (D-std-0014)
  audience: both
  subjects: inherited
- id: qaa/english-2023/4.2.b31
  locator: { number: "4.2.b31", headingPath: ["Benchmark standards", "Introduction"] }
  span: { start: 43551, end: 43630 }
  source: "show rigour and precision in the deployment and evaluation of data and evidence"
  stem: "4.2"
  statementType: threshold
  rung: threshold
  force: threshold
  level: fheq:6
  appliesTo: "graduates who studied English as a significant component of their degree, at the threshold level"
  addressee: learner
  verbs: ["show"]
  about: "rigour and precision with data and evidence"
  themes: [none]
  domain: generic-skill
  award: ["bachelor's with honours"]
  gradeOf: none
  paraphrase: "Will have shown, as the minimum for the honours degree, rigour and precision in using and weighing data and evidence."
  quote: full   # the issuer's statement is in `source` (D-std-0014)
  audience: both
  subjects: inherited
- id: qaa/english-2023/4.2.b32
  locator: { number: "4.2.b32", headingPath: ["Benchmark standards", "Introduction"] }
  span: { start: 43633, end: 43710 }
  source: "follow arguments and debates, negotiate disagreement and recognise ambiguity."
  stem: "4.2"
  statementType: threshold
  rung: threshold
  force: threshold
  level: fheq:6
  appliesTo: "graduates who studied English as a significant component of their degree, at the threshold level"
  addressee: learner
  verbs: ["follow", "negotiate", "recognise"]
  about: "following debate, negotiating disagreement, seeing ambiguity"
  themes: [none]
  domain: generic-skill
  award: ["bachelor's with honours"]
  gradeOf: none
  paraphrase: "Will have shown, as the minimum for the honours degree, the capacity to follow arguments and debates, work through disagreement and spot ambiguity."
  quote: full   # the issuer's statement is in `source` (D-std-0014)
  audience: both
  subjects: inherited
- id: qaa/english-2023/4.2.b33
  locator: { number: "4.2.b33", headingPath: ["Benchmark standards", "Introduction"] }
  span: { start: 43714, end: 43800 }
  source: "think critically and display wide powers of understanding, analysis and interpretation"
  stem: "4.2"
  statementType: typical
  rung: typical
  force: will
  level: fheq:6
  appliesTo: "graduates who studied English as a significant component of their degree, at the typical level"
  addressee: learner
  verbs: ["think", "display"]
  about: "wide powers of critical thought"
  themes: [none]
  domain: generic-skill
  award: ["bachelor's with honours"]
  gradeOf: { statement: qaa/english-2023/4.2.b28, basis: inferred }
  paraphrase: "Are able to show, at the typical level reached by most honours graduates, critical thought, with wide-ranging capacity to understand, analyse and interpret."
  quote: full   # the issuer's statement is in `source` (D-std-0014)
  audience: both
  subjects: inherited
- id: qaa/english-2023/4.2.b34
  locator: { number: "4.2.b34", headingPath: ["Benchmark standards", "Introduction"] }
  span: { start: 43803, end: 43909 }
  source: "articulate an advanced critical understanding of complex texts and ideas and of their historical relations"
  stem: "4.2"
  statementType: typical
  rung: typical
  force: will
  level: fheq:6
  appliesTo: "graduates who studied English as a significant component of their degree, at the typical level"
  addressee: learner
  verbs: ["articulate"]
  about: "advanced critical understanding of complex texts"
  themes: [none]
  domain: understanding
  award: ["bachelor's with honours"]
  gradeOf: { statement: qaa/english-2023/4.2.b29, basis: inferred }
  paraphrase: "Are able to show, at the typical level reached by most honours graduates, the capacity to express an advanced critical grasp of demanding texts and ideas and of how they relate over time."
  quote: full   # the issuer's statement is in `source` (D-std-0014)
  audience: both
  subjects: inherited
- id: qaa/english-2023/4.2.b35
  locator: { number: "4.2.b35", headingPath: ["Benchmark standards", "Introduction"] }
  span: { start: 43912, end: 44051 }
  source: "reflect critically and rigorously upon the acts of reading and writing; evaluate literary and linguistic forms and other cultural artefacts"
  stem: "4.2"
  statementType: typical
  rung: typical
  force: will
  level: fheq:6
  appliesTo: "graduates who studied English as a significant component of their degree, at the typical level"
  addressee: learner
  verbs: ["reflect", "evaluate"]
  about: "rigorous reflection on reading and writing; evaluating forms"
  themes: [none]
  domain: subject-skill
  award: ["bachelor's with honours"]
  gradeOf: { statement: qaa/english-2023/4.2.b30, basis: inferred }
  paraphrase: "Are able to show, at the typical level reached by most honours graduates, rigorous critical reflection on reading and writing, and evaluation of literary and linguistic forms and other cultural artefacts."
  quote: full   # the issuer's statement is in `source` (D-std-0014)
  audience: both
  subjects: inherited
- id: qaa/english-2023/4.2.b36
  locator: { number: "4.2.b36", headingPath: ["Benchmark standards", "Introduction"] }
  span: { start: 44054, end: 44133 }
  source: "show rigour and precision in the deployment and evaluation of data and evidence"
  stem: "4.2"
  statementType: typical
  rung: typical
  force: will
  level: fheq:6
  appliesTo: "graduates who studied English as a significant component of their degree, at the typical level"
  addressee: learner
  verbs: ["show"]
  about: "rigour and precision with data and evidence (typical)"
  themes: [none]
  domain: generic-skill
  award: ["bachelor's with honours"]
  gradeOf: { statement: qaa/english-2023/4.2.b31, basis: inferred }
  paraphrase: "Are able to show, at the typical level reached by most honours graduates, rigour and precision in using and weighing data and evidence (the same wording as the threshold item)."
  quote: full   # the issuer's statement is in `source` (D-std-0014)
  audience: both
  subjects: inherited
- id: qaa/english-2023/4.2.b37
  locator: { number: "4.2.b37", headingPath: ["Benchmark standards", "Introduction"] }
  span: { start: 44136, end: 44245 }
  source: "engage with arguments and debates, negotiate disagreement and recognise and understand the uses of ambiguity."
  stem: "4.2"
  statementType: typical
  rung: typical
  force: will
  level: fheq:6
  appliesTo: "graduates who studied English as a significant component of their degree, at the typical level"
  addressee: learner
  verbs: ["engage", "negotiate", "recognise", "understand"]
  about: "engaging in debate and the uses of ambiguity"
  themes: [none]
  domain: generic-skill
  award: ["bachelor's with honours"]
  gradeOf: { statement: qaa/english-2023/4.2.b32, basis: inferred }
  paraphrase: "Are able to show, at the typical level reached by most honours graduates, engagement with arguments and debates, working through disagreement and understanding how ambiguity is used."
  quote: full   # the issuer's statement is in `source` (D-std-0014)
  audience: both
  subjects: inherited
- id: qaa/english-2023/4.2.b38
  locator: { number: "4.2.b38", headingPath: ["Benchmark standards", "Introduction"] }
  span: { start: 44249, end: 44340 }
  source: "think critically and display extensive powers of understanding, analysis and interpretation"
  stem: "4.2"
  statementType: excellent
  rung: excellent
  force: will
  level: fheq:6
  appliesTo: "graduates who studied English as a significant component of their degree, at the excellent level"
  addressee: learner
  verbs: ["think", "display"]
  about: "extensive powers of critical thought"
  themes: [none]
  domain: generic-skill
  award: ["bachelor's with honours"]
  gradeOf: { statement: qaa/english-2023/4.2.b33, basis: inferred }
  paraphrase: "Are able to show, at the excellent level for the honours degree, critical thought, with an extensive capacity to understand, analyse and interpret."
  quote: full   # the issuer's statement is in `source` (D-std-0014)
  audience: both
  subjects: inherited
- id: qaa/english-2023/4.2.b39
  locator: { number: "4.2.b39", headingPath: ["Benchmark standards", "Introduction"] }
  span: { start: 44343, end: 44454 }
  source: "articulate a sophisticated critical understanding of complex texts and ideas, and of their historical relations"
  stem: "4.2"
  statementType: excellent
  rung: excellent
  force: will
  level: fheq:6
  appliesTo: "graduates who studied English as a significant component of their degree, at the excellent level"
  addressee: learner
  verbs: ["articulate"]
  about: "sophisticated critical understanding of complex texts"
  themes: [none]
  domain: understanding
  award: ["bachelor's with honours"]
  gradeOf: { statement: qaa/english-2023/4.2.b34, basis: inferred }
  paraphrase: "Are able to show, at the excellent level for the honours degree, the capacity to express a sophisticated critical grasp of demanding texts and ideas and of how they relate over time."
  quote: full   # the issuer's statement is in `source` (D-std-0014)
  audience: both
  subjects: inherited
- id: qaa/english-2023/4.2.b40
  locator: { number: "4.2.b40", headingPath: ["Benchmark standards", "Introduction"] }
  span: { start: 44457, end: 44534 }
  source: "reflect critically and in precise detail upon the acts of reading and writing"
  stem: "4.2"
  statementType: excellent
  rung: excellent
  force: will
  level: fheq:6
  appliesTo: "graduates who studied English as a significant component of their degree, at the excellent level"
  addressee: learner
  verbs: ["reflect"]
  about: "precise, detailed reflection on reading and writing"
  themes: [none]
  domain: subject-skill
  award: ["bachelor's with honours"]
  gradeOf: { statement: qaa/english-2023/4.2.b35, basis: inferred }
  paraphrase: "Are able to show, at the excellent level for the honours degree, critical reflection on reading and writing in exact detail."
  quote: full   # the issuer's statement is in `source` (D-std-0014)
  audience: both
  subjects: inherited
- id: qaa/english-2023/4.2.b41
  locator: { number: "4.2.b41", headingPath: ["Benchmark standards", "Introduction"] }
  span: { start: 44537, end: 44650 }
  source: "evaluate literary and linguistic forms and other cultural artefacts in a wide intellectual and historical context"
  stem: "4.2"
  statementType: excellent
  rung: excellent
  force: will
  level: fheq:6
  appliesTo: "graduates who studied English as a significant component of their degree, at the excellent level"
  addressee: learner
  verbs: ["evaluate"]
  about: "evaluating forms and artefacts in wide context"
  themes: [none]
  domain: subject-skill
  award: ["bachelor's with honours"]
  gradeOf: { statement: qaa/english-2023/4.2.b35, basis: inferred }
  paraphrase: "Are able to show, at the excellent level for the honours degree, evaluation of literary and linguistic forms and other cultural artefacts within a broad intellectual and historical setting."
  quote: full   # the issuer's statement is in `source` (D-std-0014)
  audience: both
  subjects: inherited
- id: qaa/english-2023/4.2.b42
  locator: { number: "4.2.b42", headingPath: ["Benchmark standards", "Introduction"] }
  span: { start: 44653, end: 44732 }
  source: "show rigour and precision in the deployment and evaluation of data and evidence"
  stem: "4.2"
  statementType: excellent
  rung: excellent
  force: will
  level: fheq:6
  appliesTo: "graduates who studied English as a significant component of their degree, at the excellent level"
  addressee: learner
  verbs: ["show"]
  about: "rigour and precision with data and evidence (excellent)"
  themes: [none]
  domain: generic-skill
  award: ["bachelor's with honours"]
  gradeOf: { statement: qaa/english-2023/4.2.b36, basis: inferred }
  paraphrase: "Are able to show, at the excellent level for the honours degree, rigour and precision in using and weighing data and evidence (the same wording as the lower columns)."
  quote: full   # the issuer's statement is in `source` (D-std-0014)
  audience: both
  subjects: inherited
- id: qaa/english-2023/4.2.b43
  locator: { number: "4.2.b43", headingPath: ["Benchmark standards", "Introduction"] }
  span: { start: 44735, end: 44894 }
  source: "engage actively with arguments and debates, negotiate disagreement highly effectively; and understand, analyse and appreciate the roles and value of ambiguity."
  stem: "4.2"
  statementType: excellent
  rung: excellent
  force: will
  level: fheq:6
  appliesTo: "graduates who studied English as a significant component of their degree, at the excellent level"
  addressee: learner
  verbs: ["engage", "negotiate", "understand", "analyse", "appreciate"]
  about: "active debate and the value of ambiguity"
  themes: [none]
  domain: generic-skill
  award: ["bachelor's with honours"]
  gradeOf: { statement: qaa/english-2023/4.2.b37, basis: inferred }
  paraphrase: "Are able to show, at the excellent level for the honours degree, active engagement with arguments and debates, highly effective negotiation of disagreement and an understanding, analysis and appreciation of what ambiguity does and is worth."
  quote: full   # the issuer's statement is in `source` (D-std-0014)
  audience: both
  subjects: inherited
- id: qaa/english-2023/4.2.b44
  locator: { number: "4.2.b44", headingPath: ["Benchmark standards", "Introduction"] }
  span: { start: 44897, end: 44992 }
  source: "identify, gather, synthesise, organise, and deploy some evidence in the support of an argument."
  stem: "4.2"
  statementType: threshold
  rung: threshold
  force: threshold
  level: fheq:6
  appliesTo: "graduates who studied English as a significant component of their degree, at the threshold level"
  addressee: learner
  verbs: ["identify", "gather", "synthesise", "organise", "deploy"]
  about: "gathering and using some evidence for an argument"
  themes: [none]
  domain: generic-skill
  award: ["bachelor's with honours"]
  gradeOf: none
  paraphrase: "Will have shown, as the minimum for the honours degree, the capacity to find, collect, combine, arrange and use some evidence to support an argument."
  quote: full   # the issuer's statement is in `source` (D-std-0014)
  audience: both
  subjects: inherited
- id: qaa/english-2023/4.2.b45
  locator: { number: "4.2.b45", headingPath: ["Benchmark standards", "Introduction"] }
  span: { start: 44995, end: 45255 }
  source: "process and interpret the evidence they gather, situating it in wider contexts and formulating research questions to further their investigations. Students at the lower end of this scale may tend to cite evidence in a descriptive rather than analytic register."
  stem: "4.2"
  statementType: typical
  rung: typical
  force: will
  level: fheq:6
  appliesTo: "graduates who studied English as a significant component of their degree, at the typical level"
  addressee: learner
  verbs: ["process", "interpret", "situating", "formulating", "cite"]
  about: "interpreting evidence and framing research questions"
  themes: [none]
  domain: generic-skill
  award: ["bachelor's with honours"]
  gradeOf: { statement: qaa/english-2023/4.2.b44, basis: inferred }
  paraphrase: "Are able to show, at the typical level reached by most honours graduates, the capacity to work through and interpret the evidence they collect, set it in wider contexts and frame research questions that take their enquiry further (weaker students at this level may still cite evidence descriptively)."
  quote: full   # the issuer's statement is in `source` (D-std-0014)
  audience: both
  subjects: inherited
- id: qaa/english-2023/4.2.b46
  locator: { number: "4.2.b46", headingPath: ["Benchmark standards", "Introduction"] }
  span: { start: 45258, end: 45517 }
  source: "interpret and analyses evidence they have gathered, independently and critically; construct well-defined lines of enquiry to produce cogent, well-structured arguments and decisive judgments which articulate a critical understanding of complex texts and ideas."
  stem: "4.2"
  statementType: excellent
  rung: excellent
  force: will
  level: fheq:6
  appliesTo: "graduates who studied English as a significant component of their degree, at the excellent level"
  addressee: learner
  verbs: ["interpret", "analyses", "construct", "produce", "articulate"]
  about: "independent analysis of evidence and well-defined enquiry"
  themes: [none]
  domain: generic-skill
  award: ["bachelor's with honours"]
  gradeOf: { statement: qaa/english-2023/4.2.b45, basis: inferred }
  paraphrase: "Are able to show, at the excellent level for the honours degree, independent, critical interpretation and analysis of the evidence they gather, with sharply defined lines of enquiry that yield cogent, well-built arguments and firm judgements showing critical understanding of complex texts and ideas."
  quote: full   # the issuer's statement is in `source` (D-std-0014)
  audience: both
  subjects: inherited
- id: qaa/english-2023/4.2.b47
  locator: { number: "4.2.b47", headingPath: ["Benchmark standards", "Introduction"] }
  span: { start: 45600, end: 45642 }
  source: "understand the technique of close reading."
  stem: "4.2"
  statementType: threshold
  rung: threshold
  force: threshold
  level: fheq:6
  appliesTo: "graduates who studied English as a significant component of their degree, at the threshold level"
  addressee: learner
  verbs: ["understand"]
  about: "the technique of close reading"
  themes: [none]
  domain: subject-skill
  award: ["bachelor's with honours"]
  gradeOf: none
  paraphrase: "Will have shown, as the minimum for the honours degree, an understanding of how close reading works."
  quote: full   # the issuer's statement is in `source` (D-std-0014)
  audience: both
  subjects: inherited
- id: qaa/english-2023/4.2.b48
  locator: { number: "4.2.b48", headingPath: ["Benchmark standards", "Introduction"] }
  span: { start: 45646, end: 45972 }
  source: "deploy close reading techniques: at the lower second-class standard this may be formulaic or descriptive rather than analytic, and only loosely connected to an overall argument; at the upper- second class standard, students tend to anchor observations generated through close reading more substantially in their own arguments."
  stem: "4.2"
  statementType: typical
  rung: typical
  force: will
  level: fheq:6
  appliesTo: "graduates who studied English as a significant component of their degree, at the typical level"
  addressee: learner
  verbs: ["deploy", "anchor"]
  about: "using close reading in argument"
  themes: [none]
  domain: subject-skill
  award: ["bachelor's with honours"]
  gradeOf: { statement: qaa/english-2023/4.2.b47, basis: inferred }
  paraphrase: "Are able to show, at the typical level reached by most honours graduates, use of close reading, which at the lower second may stay formulaic, descriptive and loosely tied to the argument, and at the upper second is anchored more firmly in their own case."
  quote: full   # the issuer's statement is in `source` (D-std-0014)
  audience: both
  subjects: inherited
- id: qaa/english-2023/4.2.b49
  locator: { number: "4.2.b49", headingPath: ["Benchmark standards", "Introduction"] }
  span: { start: 45975, end: 46264 }
  source: "develop incisive, original observations from sustained close attention to passages from texts, which pay attention where appropriate to form, device and figures of speech, are clearly related to an interpretation of the whole text and seamlessly embedded in the argument of the assignment."
  stem: "4.2"
  statementType: excellent
  rung: excellent
  force: will
  level: fheq:6
  appliesTo: "graduates who studied English as a significant component of their degree, at the excellent level"
  addressee: learner
  verbs: ["develop"]
  about: "incisive close reading embedded in argument"
  themes: [none]
  domain: subject-skill
  award: ["bachelor's with honours"]
  gradeOf: { statement: qaa/english-2023/4.2.b48, basis: inferred }
  paraphrase: "Are able to show, at the excellent level for the honours degree, sharp, original observations drawn from sustained attention to passages, alert to form, device and figures of speech, linked to a reading of the whole text and woven into the argument."
  quote: full   # the issuer's statement is in `source` (D-std-0014)
  audience: both
  subjects: inherited
- id: qaa/english-2023/4.2.b50
  locator: { number: "4.2.b50", headingPath: ["Benchmark standards", "Introduction"] }
  span: { start: 46267, end: 46539 }
  source: "show awareness that interpretation of a text implies a potential plurality of meaning and understand that although interpretation implies potential plurality of meaning and often ambiguity, this does not mean that all interpretation is simply a matter of personal opinion."
  stem: "4.2"
  statementType: threshold
  rung: threshold
  force: threshold
  level: fheq:6
  appliesTo: "graduates who studied English as a significant component of their degree, at the threshold level"
  addressee: learner
  verbs: ["show", "understand", "implies"]
  about: "plurality of meaning without mere opinion"
  themes: [none]
  domain: understanding
  award: ["bachelor's with honours"]
  gradeOf: none
  paraphrase: "Will have shown, as the minimum for the honours degree, awareness that texts can bear several meanings and an understanding that this does not reduce interpretation to personal opinion."
  quote: full   # the issuer's statement is in `source` (D-std-0014)
  audience: both
  subjects: inherited
- id: qaa/english-2023/4.2.b51
  locator: { number: "4.2.b51", headingPath: ["Benchmark standards", "Introduction"] }
  span: { start: 46542, end: 46622 }
  source: "show the ability to evaluate the grounds and value of different interpretations."
  stem: "4.2"
  statementType: typical
  rung: typical
  force: will
  level: fheq:6
  appliesTo: "graduates who studied English as a significant component of their degree, at the typical level"
  addressee: learner
  verbs: ["show", "evaluate"]
  about: "evaluating competing interpretations"
  themes: [none]
  domain: understanding
  award: ["bachelor's with honours"]
  gradeOf: { statement: qaa/english-2023/4.2.b50, basis: inferred }
  paraphrase: "Are able to show, at the typical level reached by most honours graduates, the capacity to weigh the grounds and worth of different readings."
  quote: full   # the issuer's statement is in `source` (D-std-0014)
  audience: both
  subjects: inherited
- id: qaa/english-2023/4.2.b52
  locator: { number: "4.2.b52", headingPath: ["Benchmark standards", "Introduction"] }
  span: { start: 46625, end: 46814 }
  source: "recognise the richness of language and its ability to carry multiple and often ambiguous meanings, of the role of readers in shaping texts, and of texts in shaping the responses of readers."
  stem: "4.2"
  statementType: excellent
  rung: excellent
  force: will
  level: fheq:6
  appliesTo: "graduates who studied English as a significant component of their degree, at the excellent level"
  addressee: learner
  verbs: ["recognise", "carry"]
  about: "richness of language; readers and texts shaping each other"
  themes: [none]
  domain: understanding
  award: ["bachelor's with honours"]
  gradeOf: { statement: qaa/english-2023/4.2.b51, basis: inferred }
  paraphrase: "Are able to show, at the excellent level for the honours degree, a recognition of how rich language is and how it carries many, often ambiguous meanings, of how readers shape texts and of how texts shape readers' responses."
  quote: full   # the issuer's statement is in `source` (D-std-0014)
  audience: both
  subjects: inherited
- id: qaa/english-2023/4.2.b53
  locator: { number: "4.2.b53", headingPath: ["Benchmark standards", "Introduction"] }
  span: { start: 49344, end: 49492 }
  source: "understand and carry out a variety of assessment tasks, including the initiation and completion, under supervision, of lengthy projects of their own"
  stem: "4.2"
  statementType: threshold
  rung: threshold
  force: threshold
  level: fheq:6
  appliesTo: "graduates who studied English as a significant component of their degree, at the threshold level"
  addressee: learner
  verbs: ["understand", "carry"]
  about: "carrying out varied tasks and supervised long projects"
  themes: [none]
  domain: generic-skill
  award: ["bachelor's with honours"]
  gradeOf: none
  paraphrase: "Will have shown, as the minimum for the honours degree, the capacity to understand and complete a range of assessment tasks, including starting and finishing their own long projects under supervision."
  quote: full   # the issuer's statement is in `source` (D-std-0014)
  audience: both
  subjects: inherited
- id: qaa/english-2023/4.2.b54
  locator: { number: "4.2.b54", headingPath: ["Benchmark standards", "Introduction"] }
  span: { start: 49495, end: 49674 }
  source: "understand the necessity of planning time to meet multiple deadlines, and recognise the advisability of delivering material to those deadlines, although they may not always do so."
  stem: "4.2"
  statementType: threshold
  rung: threshold
  force: threshold
  level: fheq:6
  appliesTo: "graduates who studied English as a significant component of their degree, at the threshold level"
  addressee: learner
  verbs: ["understand", "recognise", "delivering"]
  about: "planning time for deadlines"
  themes: [none]
  domain: generic-skill
  award: ["bachelor's with honours"]
  gradeOf: none
  paraphrase: "Will have shown, as the minimum for the honours degree, an understanding that time must be planned to meet several deadlines and that meeting them is wise, though they may not always manage it."
  quote: full   # the issuer's statement is in `source` (D-std-0014)
  audience: both
  subjects: inherited
- id: qaa/english-2023/4.2.b55
  locator: { number: "4.2.b55", headingPath: ["Benchmark standards", "Introduction"] }
  span: { start: 49677, end: 49721 }
  source: "adapt agilely to different demands and tasks"
  stem: "4.2"
  statementType: typical
  rung: typical
  force: will
  level: fheq:6
  appliesTo: "graduates who studied English as a significant component of their degree, at the typical level"
  addressee: learner
  verbs: ["adapt"]
  about: "adapting to different demands and tasks"
  themes: [none]
  domain: generic-skill
  award: ["bachelor's with honours"]
  gradeOf: { statement: qaa/english-2023/4.2.b53, basis: inferred }
  paraphrase: "Are able to show, at the typical level reached by most honours graduates, quick adaptation to differing demands and tasks."
  quote: full   # the issuer's statement is in `source` (D-std-0014)
  audience: both
  subjects: inherited
- id: qaa/english-2023/4.2.b56
  locator: { number: "4.2.b56", headingPath: ["Benchmark standards", "Introduction"] }
  span: { start: 49724, end: 49817 }
  source: "take responsibility for their own work and be proactive in seeking assistance if they need it"
  stem: "4.2"
  statementType: typical
  rung: typical
  force: will
  level: fheq:6
  appliesTo: "graduates who studied English as a significant component of their degree, at the typical level"
  addressee: learner
  verbs: ["take", "seeking"]
  about: "owning work and seeking help early"
  themes: [none]
  domain: generic-skill
  award: ["bachelor's with honours"]
  gradeOf: none
  paraphrase: "Are able to show, at the typical level reached by most honours graduates, responsibility for their own work and readiness to seek help when they need it."
  quote: full   # the issuer's statement is in `source` (D-std-0014)
  audience: both
  subjects: inherited
- id: qaa/english-2023/4.2.b57
  locator: { number: "4.2.b57", headingPath: ["Benchmark standards", "Introduction"] }
  span: { start: 49820, end: 49889 }
  source: "plan their time to deliver material to multiple stipulated deadlines."
  stem: "4.2"
  statementType: typical
  rung: typical
  force: will
  level: fheq:6
  appliesTo: "graduates who studied English as a significant component of their degree, at the typical level"
  addressee: learner
  verbs: ["plan", "deliver"]
  about: "planning time to meet set deadlines"
  themes: [none]
  domain: generic-skill
  award: ["bachelor's with honours"]
  gradeOf: { statement: qaa/english-2023/4.2.b54, basis: inferred }
  paraphrase: "Are able to show, at the typical level reached by most honours graduates, planning of their time so that work arrives by several set deadlines."
  quote: full   # the issuer's statement is in `source` (D-std-0014)
  audience: both
  subjects: inherited
- id: qaa/english-2023/4.2.b58
  locator: { number: "4.2.b58", headingPath: ["Benchmark standards", "Introduction"] }
  span: { start: 49892, end: 49948 }
  source: "respond creatively and independently to assessment tasks"
  stem: "4.2"
  statementType: excellent
  rung: excellent
  force: will
  level: fheq:6
  appliesTo: "graduates who studied English as a significant component of their degree, at the excellent level"
  addressee: learner
  verbs: ["respond"]
  about: "creative, independent response to assessment"
  themes: [none]
  domain: generic-skill
  award: ["bachelor's with honours"]
  gradeOf: { statement: qaa/english-2023/4.2.b55, basis: inferred }
  paraphrase: "Are able to show, at the excellent level for the honours degree, creative and independent responses to assessment tasks."
  quote: full   # the issuer's statement is in `source` (D-std-0014)
  audience: both
  subjects: inherited
- id: qaa/english-2023/4.2.b59
  locator: { number: "4.2.b59", headingPath: ["Benchmark standards", "Introduction"] }
  span: { start: 49951, end: 49995 }
  source: "be proactive in seeking help if they need it"
  stem: "4.2"
  statementType: excellent
  rung: excellent
  force: will
  level: fheq:6
  appliesTo: "graduates who studied English as a significant component of their degree, at the excellent level"
  addressee: learner
  verbs: ["seeking"]
  about: "proactive help-seeking"
  themes: [none]
  domain: generic-skill
  award: ["bachelor's with honours"]
  gradeOf: { statement: qaa/english-2023/4.2.b56, basis: inferred }
  paraphrase: "Are able to show, at the excellent level for the honours degree, a proactive approach to asking for help when needed."
  quote: full   # the issuer's statement is in `source` (D-std-0014)
  audience: both
  subjects: inherited
- id: qaa/english-2023/4.2.b60
  locator: { number: "4.2.b60", headingPath: ["Benchmark standards", "Introduction"] }
  span: { start: 49998, end: 50143 }
  source: "manage their time efficiently, juggling competing demands to meet deadlines, and leaving time to revise and proofread work before its submission."
  stem: "4.2"
  statementType: excellent
  rung: excellent
  force: will
  level: fheq:6
  appliesTo: "graduates who studied English as a significant component of their degree, at the excellent level"
  addressee: learner
  verbs: ["manage", "juggling", "meet", "leaving", "revise"]
  about: "efficient time management with time to revise"
  themes: [none]
  domain: generic-skill
  award: ["bachelor's with honours"]
  gradeOf: { statement: qaa/english-2023/4.2.b57, basis: inferred }
  paraphrase: "Are able to show, at the excellent level for the honours degree, efficient management of time, balancing competing demands to meet deadlines and leaving room to revise and proofread before submission."
  quote: full   # the issuer's statement is in `source` (D-std-0014)
  audience: both
  subjects: inherited
- id: qaa/english-2023/4.2.b61
  locator: { number: "4.2.b61", headingPath: ["Benchmark standards", "Introduction"] }
  span: { start: 50146, end: 50385 }
  source: "be aware of the existence of multiple perspectives, from past and present, and regional to global, and recognise the importance of listening to alternative perspectives, whether they meet them in their learning spaces, or in written texts."
  stem: "4.2"
  statementType: threshold
  rung: threshold
  force: threshold
  level: fheq:6
  appliesTo: "graduates who studied English as a significant component of their degree, at the threshold level"
  addressee: learner
  verbs: ["recognise", "listening", "meet"]
  about: "awareness of multiple perspectives and the value of listening"
  themes: [none]
  domain: generic-skill
  award: ["bachelor's with honours"]
  gradeOf: none
  paraphrase: "Will have shown, as the minimum for the honours degree, awareness that many perspectives exist, past and present, local and global, and recognition that listening to other views matters, whether in class or in texts."
  quote: full   # the issuer's statement is in `source` (D-std-0014)
  audience: both
  subjects: inherited
- id: qaa/english-2023/4.2.b62
  locator: { number: "4.2.b62", headingPath: ["Benchmark standards", "Introduction"] }
  span: { start: 50388, end: 50462 }
  source: "listen to other perspectives, including those with which they may disagree"
  stem: "4.2"
  statementType: typical
  rung: typical
  force: will
  level: fheq:6
  appliesTo: "graduates who studied English as a significant component of their degree, at the typical level"
  addressee: learner
  verbs: ["listen", "disagree"]
  about: "listening to views one disagrees with"
  themes: [none]
  domain: generic-skill
  award: ["bachelor's with honours"]
  gradeOf: { statement: qaa/english-2023/4.2.b61, basis: inferred }
  paraphrase: "Are able to show, at the typical level reached by most honours graduates, a willingness to listen to other perspectives, including ones they may disagree with."
  quote: full   # the issuer's statement is in `source` (D-std-0014)
  audience: both
  subjects: inherited
- id: qaa/english-2023/4.2.b63
  locator: { number: "4.2.b63", headingPath: ["Benchmark standards", "Introduction"] }
  span: { start: 50465, end: 50561 }
  source: "articulate those perspectives fairly and position their own opinions within a spectrum of views."
  stem: "4.2"
  statementType: typical
  rung: typical
  force: will
  level: fheq:6
  appliesTo: "graduates who studied English as a significant component of their degree, at the typical level"
  addressee: learner
  verbs: ["articulate", "position"]
  about: "stating views fairly and placing one's own among them"
  themes: [none]
  domain: generic-skill
  award: ["bachelor's with honours"]
  gradeOf: none
  paraphrase: "Are able to show, at the typical level reached by most honours graduates, the capacity to state those other perspectives fairly and to place their own views within a range of positions."
  quote: full   # the issuer's statement is in `source` (D-std-0014)
  audience: both
  subjects: inherited
- id: qaa/english-2023/4.2.b64
  locator: { number: "4.2.b64", headingPath: ["Benchmark standards", "Introduction"] }
  span: { start: 50564, end: 50657 }
  source: "be sensitive to cultural contexts and shared or unshared backgrounds when working with others"
  stem: "4.2"
  statementType: excellent
  rung: excellent
  force: will
  level: fheq:6
  appliesTo: "graduates who studied English as a significant component of their degree, at the excellent level"
  addressee: learner
  verbs: ["working"]
  about: "cultural sensitivity in working with others"
  themes: [none]
  domain: generic-skill
  award: ["bachelor's with honours"]
  gradeOf: none
  paraphrase: "Are able to show, at the excellent level for the honours degree, sensitivity to cultural contexts and to shared and differing backgrounds when working with others."
  quote: full   # the issuer's statement is in `source` (D-std-0014)
  audience: both
  subjects: inherited
- id: qaa/english-2023/4.2.b65
  locator: { number: "4.2.b65", headingPath: ["Benchmark standards", "Introduction"] }
  span: { start: 50660, end: 50766 }
  source: "articulate those perspectives fairly and position their own opinions precisely within a spectrum of views."
  stem: "4.2"
  statementType: excellent
  rung: excellent
  force: will
  level: fheq:6
  appliesTo: "graduates who studied English as a significant component of their degree, at the excellent level"
  addressee: learner
  verbs: ["articulate", "position"]
  about: "placing one's own views precisely among others"
  themes: [none]
  domain: generic-skill
  award: ["bachelor's with honours"]
  gradeOf: { statement: qaa/english-2023/4.2.b63, basis: inferred }
  paraphrase: "Are able to show, at the excellent level for the honours degree, the capacity to state other perspectives fairly and place their own views exactly within a range of positions."
  quote: full   # the issuer's statement is in `source` (D-std-0014)
  audience: both
  subjects: inherited
- id: qaa/english-2023/4.2.b66
  locator: { number: "4.2.b66", headingPath: ["Benchmark standards", "Introduction"] }
  span: { start: 50769, end: 51088 }
  source: "be aware of the necessity to show academic integrity and ethical responsibility in the use of writing and research of other people, including in the use of large language models (sometimes known as artificial intelligence) as aids for writing, although their bibliographies and citations may be occasionally inaccurate."
  stem: "4.2"
  statementType: threshold
  rung: threshold
  force: threshold
  level: fheq:6
  appliesTo: "graduates who studied English as a significant component of their degree, at the threshold level"
  addressee: learner
  verbs: ["show"]
  about: "awareness of academic integrity, including use of large language models"
  themes: [none]
  domain: generic-skill
  award: ["bachelor's with honours"]
  gradeOf: none
  paraphrase: "Will have shown, as the minimum for the honours degree, awareness that academic integrity and ethical care are needed when using other people's writing and research, including large language models as writing aids, though their references may sometimes be inaccurate."
  quote: full   # the issuer's statement is in `source` (D-std-0014)
  audience: both
  subjects: inherited
- id: qaa/english-2023/4.2.b67
  locator: { number: "4.2.b67", headingPath: ["Benchmark standards", "Introduction"] }
  span: { start: 51091, end: 51297 }
  source: "show academic integrity and ethical responsibility in the use of writing and research of others including in the use of large language models (sometimes known as artificial intelligence) as aids for writing"
  stem: "4.2"
  statementType: typical
  rung: typical
  force: will
  level: fheq:6
  appliesTo: "graduates who studied English as a significant component of their degree, at the typical level"
  addressee: learner
  verbs: ["show"]
  about: "academic integrity, including use of large language models"
  themes: [none]
  domain: generic-skill
  award: ["bachelor's with honours"]
  gradeOf: { statement: qaa/english-2023/4.2.b66, basis: inferred }
  paraphrase: "Are able to show, at the typical level reached by most honours graduates, academic integrity and ethical responsibility in using others' writing and research, large language models used as writing aids included."
  quote: full   # the issuer's statement is in `source` (D-std-0014)
  audience: both
  subjects: inherited
- id: qaa/english-2023/4.2.b68
  locator: { number: "4.2.b68", headingPath: ["Benchmark standards", "Introduction"] }
  span: { start: 51300, end: 51388 }
  source: "offer clear, comprehensive bibliographies, and accurate citations of the work of others."
  stem: "4.2"
  statementType: typical
  rung: typical
  force: will
  level: fheq:6
  appliesTo: "graduates who studied English as a significant component of their degree, at the typical level"
  addressee: learner
  verbs: ["offer"]
  about: "clear bibliographies and accurate citation"
  themes: [none]
  domain: generic-skill
  award: ["bachelor's with honours"]
  gradeOf: none
  paraphrase: "Are able to show, at the typical level reached by most honours graduates, clear and complete bibliographies and accurate citation of others' work."
  quote: full   # the issuer's statement is in `source` (D-std-0014)
  audience: both
  subjects: inherited
- id: qaa/english-2023/4.2.b69
  locator: { number: "4.2.b69", headingPath: ["Benchmark standards", "Introduction"] }
  span: { start: 51391, end: 51597 }
  source: "show academic integrity and ethical responsibility in the use of writing and research of others including in the use of large language models (sometimes known as artificial intelligence) as aids for writing"
  stem: "4.2"
  statementType: excellent
  rung: excellent
  force: will
  level: fheq:6
  appliesTo: "graduates who studied English as a significant component of their degree, at the excellent level"
  addressee: learner
  verbs: ["show"]
  about: "academic integrity at the excellent level, including large language models"
  themes: [none]
  domain: generic-skill
  award: ["bachelor's with honours"]
  gradeOf: { statement: qaa/english-2023/4.2.b67, basis: inferred }
  paraphrase: "Are able to show, at the excellent level for the honours degree, academic integrity and ethical responsibility in using others' writing and research, large language models used as writing aids included (the same wording as the typical item)."
  quote: full   # the issuer's statement is in `source` (D-std-0014)
  audience: both
  subjects: inherited
- id: qaa/english-2023/4.2.b70
  locator: { number: "4.2.b70", headingPath: ["Benchmark standards", "Introduction"] }
  span: { start: 51600, end: 51712 }
  source: "construct clear, comprehensive bibliographies, with consistent and accurate citation and referencing throughout."
  stem: "4.2"
  statementType: excellent
  rung: excellent
  force: will
  level: fheq:6
  appliesTo: "graduates who studied English as a significant component of their degree, at the excellent level"
  addressee: learner
  verbs: ["construct"]
  about: "consistent, accurate referencing throughout"
  themes: [none]
  domain: generic-skill
  award: ["bachelor's with honours"]
  gradeOf: { statement: qaa/english-2023/4.2.b68, basis: inferred }
  paraphrase: "Are able to show, at the excellent level for the honours degree, clear, complete bibliographies with consistent, accurate citation and referencing from start to finish."
  quote: full   # the issuer's statement is in `source` (D-std-0014)
  audience: both
  subjects: inherited
- id: qaa/english-2023/4.2.b71
  locator: { number: "4.2.b71", headingPath: ["Benchmark standards", "Introduction"] }
  span: { start: 51715, end: 51867 }
  source: "be aware of the benefits of paying attention to feedback received from staff and/or peers, although they may need encouragement to address that feedback"
  stem: "4.2"
  statementType: threshold
  rung: threshold
  force: threshold
  level: fheq:6
  appliesTo: "graduates who studied English as a significant component of their degree, at the threshold level"
  addressee: learner
  verbs: ["paying", "address"]
  about: "seeing the value of feedback"
  themes: [none]
  domain: generic-skill
  award: ["bachelor's with honours"]
  gradeOf: none
  paraphrase: "Will have shown, as the minimum for the honours degree, awareness that attending to feedback from staff or peers pays off, though they may need prompting to act on it."
  quote: full   # the issuer's statement is in `source` (D-std-0014)
  audience: both
  subjects: inherited
- id: qaa/english-2023/4.2.b72
  locator: { number: "4.2.b72", headingPath: ["Benchmark standards", "Introduction"] }
  span: { start: 51870, end: 51935 }
  source: "may need structure to enable them to offer peer-to-peer feedback."
  stem: "4.2"
  statementType: threshold
  rung: threshold
  force: threshold
  level: fheq:6
  appliesTo: "graduates who studied English as a significant component of their degree, at the threshold level"
  addressee: learner
  verbs: ["need", "enable", "offer"]
  about: "needing structure to give peer feedback"
  themes: [none]
  domain: generic-skill
  award: ["bachelor's with honours"]
  gradeOf: none
  paraphrase: "Will have shown, as the minimum for the honours degree, a possible need for structure before they can give feedback to peers."
  quote: full   # the issuer's statement is in `source` (D-std-0014)
  audience: both
  subjects: inherited
- id: qaa/english-2023/4.2.b73
  locator: { number: "4.2.b73", headingPath: ["Benchmark standards", "Introduction"] }
  span: { start: 51938, end: 52125 }
  source: "pay attention to feedback received from staff and/or from peers. (Students at the lower level may need encouragement to address feedback; stronger students are more likely to seek it out)"
  stem: "4.2"
  statementType: typical
  rung: typical
  force: will
  level: fheq:6
  appliesTo: "graduates who studied English as a significant component of their degree, at the typical level"
  addressee: learner
  verbs: ["pay", "address", "seek"]
  about: "attending to feedback from staff and peers"
  themes: [none]
  domain: generic-skill
  award: ["bachelor's with honours"]
  gradeOf: { statement: qaa/english-2023/4.2.b71, basis: inferred }
  paraphrase: "Are able to show, at the typical level reached by most honours graduates, attention to feedback from staff and peers (the issuer adds that weaker students may need prompting and stronger ones tend to seek it out)."
  quote: full   # the issuer's statement is in `source` (D-std-0014)
  audience: both
  subjects: inherited
- id: qaa/english-2023/4.2.b74
  locator: { number: "4.2.b74", headingPath: ["Benchmark standards", "Introduction"] }
  span: { start: 52128, end: 52183 }
  source: "offer constructive and supportive suggestions to peers."
  stem: "4.2"
  statementType: typical
  rung: typical
  force: will
  level: fheq:6
  appliesTo: "graduates who studied English as a significant component of their degree, at the typical level"
  addressee: learner
  verbs: ["offer"]
  about: "constructive suggestions to peers"
  themes: [none]
  domain: generic-skill
  award: ["bachelor's with honours"]
  gradeOf: { statement: qaa/english-2023/4.2.b72, basis: inferred }
  paraphrase: "Are able to show, at the typical level reached by most honours graduates, constructive and supportive suggestions for their peers."
  quote: full   # the issuer's statement is in `source` (D-std-0014)
  audience: both
  subjects: inherited
- id: qaa/english-2023/4.2.b75
  locator: { number: "4.2.b75", headingPath: ["Benchmark standards", "Introduction"] }
  span: { start: 52186, end: 52332 }
  source: "engage consistently closely with feedback they receive from staff and from peers, using feedback to reflect on their own practices and assumptions"
  stem: "4.2"
  statementType: excellent
  rung: excellent
  force: will
  level: fheq:6
  appliesTo: "graduates who studied English as a significant component of their degree, at the excellent level"
  addressee: learner
  verbs: ["engage", "receive", "using", "reflect"]
  about: "close, consistent use of feedback to reflect"
  themes: [none]
  domain: generic-skill
  award: ["bachelor's with honours"]
  gradeOf: { statement: qaa/english-2023/4.2.b73, basis: inferred }
  paraphrase: "Are able to show, at the excellent level for the honours degree, close and steady engagement with feedback from staff and peers, using it to reflect on their own practice and assumptions."
  quote: full   # the issuer's statement is in `source` (D-std-0014)
  audience: both
  subjects: inherited
- id: qaa/english-2023/4.2.b76
  locator: { number: "4.2.b76", headingPath: ["Benchmark standards", "Introduction"] }
  span: { start: 52335, end: 52429 }
  source: "will proactively seek out feedback and use it to improve their written and oral communication."
  stem: "4.2"
  statementType: excellent
  rung: excellent
  force: will
  level: fheq:6
  appliesTo: "graduates who studied English as a significant component of their degree, at the excellent level"
  addressee: learner
  verbs: ["seek", "use", "improve"]
  about: "seeking feedback to improve communication"
  themes: [none]
  domain: generic-skill
  award: ["bachelor's with honours"]
  gradeOf: none
  paraphrase: "Are able to show, at the excellent level for the honours degree, active seeking of feedback and its use to improve their written and spoken communication."
  quote: full   # the issuer's statement is in `source` (D-std-0014)
  audience: both
  subjects: inherited
- id: qaa/english-2023/4.2.b77
  locator: { number: "4.2.b77", headingPath: ["Benchmark standards", "Introduction"] }
  span: { start: 52494, end: 52804 }
  source: "understand and effectively transfer the communication, collaboration, creativity and critical thinking skills and the experience of, for example, the development of research questions, self-directed study, and working both independently and with others, to employment and social and commercial entrepreneurship"
  stem: "4.2"
  statementType: threshold
  rung: threshold
  force: threshold
  level: fheq:6
  appliesTo: "graduates who studied English as a significant component of their degree, at the threshold level"
  addressee: learner
  verbs: ["understand", "transfer"]
  about: "transferring core skills to employment and entrepreneurship"
  themes: [none]
  domain: generic-skill
  award: ["bachelor's with honours"]
  gradeOf: none
  paraphrase: "Will have shown, as the minimum for the honours degree, an understanding of how to carry communication, collaboration, creativity and critical thinking, with experience of research questions, self-directed study and work alone and with others, into employment and social and commercial entrepreneurship, with the skill to do so effectively."
  quote: full   # the issuer's statement is in `source` (D-std-0014)
  audience: both
  subjects: inherited
- id: qaa/english-2023/4.2.b78
  locator: { number: "4.2.b78", headingPath: ["Benchmark standards", "Introduction"] }
  span: { start: 52807, end: 52913 }
  source: "have learned to act with integrity and an understanding of both their own values and the values of others."
  stem: "4.2"
  statementType: threshold
  rung: threshold
  force: threshold
  level: fheq:6
  appliesTo: "graduates who studied English as a significant component of their degree, at the threshold level"
  addressee: learner
  verbs: ["learned", "act"]
  about: "acting with integrity and an understanding of values"
  themes: [none]
  domain: generic-skill
  award: ["bachelor's with honours"]
  gradeOf: none
  paraphrase: "Will have shown, as the minimum for the honours degree, the habit of acting with integrity and with an understanding of their own values and those of others."
  quote: full   # the issuer's statement is in `source` (D-std-0014)
  audience: both
  subjects: inherited
- id: qaa/english-2023/4.2.b79
  locator: { number: "4.2.b79", headingPath: ["Benchmark standards", "Introduction"] }
  span: { start: 53018, end: 53081 }
  source: "generate creative work; develop it through editing and revision"
  stem: "4.2"
  statementType: threshold
  rung: threshold
  force: threshold
  level: fheq:6
  appliesTo: "graduates who studied Creative Writing as a significant component of their degree, at the threshold level"
  addressee: learner
  verbs: ["generate", "develop"]
  about: "generating creative work and developing it by revision"
  themes: [none]
  domain: subject-skill
  award: ["bachelor's with honours"]
  gradeOf: none
  paraphrase: "Will have shown, as the minimum for the honours degree, the capacity to produce creative work and improve it through editing and revision."
  quote: full   # the issuer's statement is in `source` (D-std-0014)
  audience: both
  subjects: inherited
- id: qaa/english-2023/4.2.b80
  locator: { number: "4.2.b80", headingPath: ["Benchmark standards", "Introduction"] }
  span: { start: 53084, end: 53219 }
  source: "show awareness of different audiences and modes of dissemination, and read and respond to published creative work and work in progress."
  stem: "4.2"
  statementType: threshold
  rung: threshold
  force: threshold
  level: fheq:6
  appliesTo: "graduates who studied Creative Writing as a significant component of their degree, at the threshold level"
  addressee: learner
  verbs: ["show", "read", "respond"]
  about: "audiences, dissemination and responding to work"
  themes: [none]
  domain: subject-skill
  award: ["bachelor's with honours"]
  gradeOf: none
  paraphrase: "Will have shown, as the minimum for the honours degree, awareness of differing audiences and ways of reaching them, and the capacity to read and respond to published and unfinished creative work."
  quote: full   # the issuer's statement is in `source` (D-std-0014)
  audience: both
  subjects: inherited
- id: qaa/english-2023/4.2.b81
  locator: { number: "4.2.b81", headingPath: ["Benchmark standards", "Introduction"] }
  span: { start: 53223, end: 53367 }
  source: "generate and develop original creative work and conduct research to support their writing, which they understand as a form of research in itself"
  stem: "4.2"
  statementType: typical
  rung: typical
  force: will
  level: fheq:6
  appliesTo: "graduates who studied Creative Writing as a significant component of their degree, at the typical level"
  addressee: learner
  verbs: ["generate", "develop", "conduct", "support", "understand"]
  about: "original work supported by research, writing as research"
  themes: [none]
  domain: subject-skill
  award: ["bachelor's with honours"]
  gradeOf: { statement: qaa/english-2023/4.2.b79, basis: inferred }
  paraphrase: "Are able to show, at the typical level reached by most honours graduates, the capacity to produce and develop original creative work and research in support of it, understanding writing itself as a kind of research."
  quote: full   # the issuer's statement is in `source` (D-std-0014)
  audience: both
  subjects: inherited
- id: qaa/english-2023/4.2.b82
  locator: { number: "4.2.b82", headingPath: ["Benchmark standards", "Introduction"] }
  span: { start: 53370, end: 53596 }
  source: "deploy the rules, conventions and possibilities of written and spoken language in a range of forms, genres and media, aware of the historical and cultural dimensions of language use and literature, including media technologies"
  stem: "4.2"
  statementType: typical
  rung: typical
  force: will
  level: fheq:6
  appliesTo: "graduates who studied Creative Writing as a significant component of their degree, at the typical level"
  addressee: learner
  verbs: ["deploy"]
  about: "using the rules and possibilities of language across forms and media"
  themes: [none]
  domain: subject-skill
  award: ["bachelor's with honours"]
  gradeOf: none
  paraphrase: "Are able to show, at the typical level reached by most honours graduates, use of what written and spoken language allows, its rules and conventions included, across forms, genres and media, aware of the history and culture of language use and literature, media technologies included."
  quote: full   # the issuer's statement is in `source` (D-std-0014)
  audience: both
  subjects: inherited
- id: qaa/english-2023/4.2.b83
  locator: { number: "4.2.b83", headingPath: ["Benchmark standards", "Introduction"] }
  span: { start: 53599, end: 53685 }
  source: "read and respond critically and practically to published work and to work in progress."
  stem: "4.2"
  statementType: typical
  rung: typical
  force: will
  level: fheq:6
  appliesTo: "graduates who studied Creative Writing as a significant component of their degree, at the typical level"
  addressee: learner
  verbs: ["read", "respond"]
  about: "critical and practical response to published and draft work"
  themes: [none]
  domain: subject-skill
  award: ["bachelor's with honours"]
  gradeOf: { statement: qaa/english-2023/4.2.b80, basis: inferred }
  paraphrase: "Are able to show, at the typical level reached by most honours graduates, critical and practical reading of and response to published work and work in progress."
  quote: full   # the issuer's statement is in `source` (D-std-0014)
  audience: both
  subjects: inherited
- id: qaa/english-2023/4.2.b84
  locator: { number: "4.2.b84", headingPath: ["Benchmark standards", "Introduction"] }
  span: { start: 53689, end: 53841 }
  source: "creatively integrate and combine all the qualities in the descriptors with independent enterprise and flair to produce ambitious, markedly original work"
  stem: "4.2"
  statementType: excellent
  rung: excellent
  force: will
  level: fheq:6
  appliesTo: "graduates who studied Creative Writing as a significant component of their degree, at the excellent level"
  addressee: learner
  verbs: ["integrate", "combine", "produce"]
  about: "ambitious, markedly original work with enterprise and flair"
  themes: [none]
  domain: subject-skill
  award: ["bachelor's with honours"]
  gradeOf: { statement: qaa/english-2023/4.2.b81, basis: inferred }
  paraphrase: "Are able to show, at the excellent level for the honours degree, creative integration of all the qualities described with independent enterprise and flair, producing ambitious and strikingly original work."
  quote: full   # the issuer's statement is in `source` (D-std-0014)
  audience: both
  subjects: inherited
- id: qaa/english-2023/4.2.b85
  locator: { number: "4.2.b85", headingPath: ["Benchmark standards", "Introduction"] }
  span: { start: 53844, end: 53947 }
  source: "deploy a creative and discriminating engagement with the expressive and imaginative powers of language."
  stem: "4.2"
  statementType: excellent
  rung: excellent
  force: will
  level: fheq:6
  appliesTo: "graduates who studied Creative Writing as a significant component of their degree, at the excellent level"
  addressee: learner
  verbs: ["deploy"]
  about: "discriminating engagement with the powers of language"
  themes: [none]
  domain: subject-skill
  award: ["bachelor's with honours"]
  gradeOf: { statement: qaa/english-2023/4.2.b82, basis: inferred }
  paraphrase: "Are able to show, at the excellent level for the honours degree, a creative and discerning engagement with what language can express and imagine."
  quote: full   # the issuer's statement is in `source` (D-std-0014)
  audience: both
  subjects: inherited
```

### S4a Audience versions
<!-- label: both; status: drafted; basis: primary. forPractitioner: for the programme designer or teacher. forBeneficiary: for the student, second person, naming no issuer. author-agent-written: instructions to an AI agent writing about the statement (a course document, a handbook, an outcome, a report). author-agent-dialogue: instructions to an AI agent using the statement in conversation (with a student, a teacher or a programme team). Written fresh from the held text alone (benchmark rule 6; Abbott, 15:42). -->
```yaml
- statement: qaa/english-2023/1.6.b1
  forPractitioner: { text: "Expect a graduate of an English course to show the capacity to read texts closely and critically, aware of literary form and of the history and language around them; the statement names it as part of what marks the subject out.", rewrite: light, force: will, status: drafted }
  forBeneficiary: { text: "By the end of your English degree, you can read texts closely and critically, aware of their form and of their historical and linguistic setting.", rewrite: full, force: will, status: drafted }
  author-agent-written: "Describe this as one of the capacities English graduates are said to have, from the outcome list in 1.6 (introduced with 'can'), for the honours degree at FHEQ level 6 (FQHEIS level 10): close, analytical and critical reading in context. Cite it as QAA (2023), English Subject Benchmark Statement, para 1.6, bullet 1. Do not present it as a threshold standard or a regulatory requirement; it describes the subject's emphasis, and the standards themselves are the 4.2 table. Set it beside 4.2.b47 and 4.2.b48, qaa/fheq-2024/4.15.b2 and qaa/fqheis-2024/4.16.b2."
  author-agent-dialogue: "Raise this when a student asks what reading at degree level involves. With a student, put it plainly as something the subject builds in you over the degree; with staff, frame it as a distinctive capacity an English course develops. Ask: 'When you read a passage closely, what do you notice first: its form, its language or its moment in history?' Avoid reading the list aloud or treating it as the pass standard."
- statement: qaa/english-2023/1.6.b2
  forPractitioner: { text: "Expect a graduate of an English course to show a grasp of creativity in language, including the aesthetic qualities of literary and other cultural works; the statement names it as part of what marks the subject out.", rewrite: light, force: will, status: drafted }
  forBeneficiary: { text: "By the end of your English degree, you can understand how language can be creative, and the aesthetic qualities of literary and other cultural works.", rewrite: full, force: will, status: drafted }
  author-agent-written: "Describe this as one of the capacities English graduates are said to have, from the outcome list in 1.6 (introduced with 'can'), for the honours degree at FHEQ level 6 (FQHEIS level 10): verbal creativity and aesthetic features of texts. Cite it as QAA (2023), English Subject Benchmark Statement, para 1.6, bullet 2. Do not present it as a threshold standard or a regulatory requirement; it describes the subject's emphasis, and the standards themselves are the 4.2 table. Set it beside 4.2.b52 and 1.6.b3, qaa/fheq-2024/4.15.b1 and qaa/fqheis-2024/4.16.b1."
  author-agent-dialogue: "Raise this when a student wonders why style and wordplay matter. With a student, put it plainly as something the subject builds in you over the degree; with staff, frame it as a distinctive capacity an English course develops. Ask: 'Where in a text you know well does the language itself do something surprising?' Avoid reading the list aloud or treating it as the pass standard."
- statement: qaa/english-2023/1.6.b3
  forPractitioner: { text: "Expect a graduate of an English course to show the capacity to analyse spoken and written texts and discourse and to respond to how language moves and persuades, with fitting methods and terms; the statement names it as part of what marks the subject out.", rewrite: light, force: will, status: drafted }
  forBeneficiary: { text: "By the end of your English degree, you can analyse spoken and written texts and discourse, and respond to how language moves and persuades, using suitable methods and terms.", rewrite: full, force: will, status: drafted }
  author-agent-written: "Describe this as one of the capacities English graduates are said to have, from the outcome list in 1.6 (introduced with 'can'), for the honours degree at FHEQ level 6 (FQHEIS level 10): analysing discourse and the force of language. Cite it as QAA (2023), English Subject Benchmark Statement, para 1.6, bullet 3. Do not present it as a threshold standard or a regulatory requirement; it describes the subject's emphasis, and the standards themselves are the 4.2 table. Set it beside 4.2.b10, 4.2.b12 and 4.2.b13, qaa/fheq-2024/4.15.b7 and qaa/fqheis-2024/4.16.b7."
  author-agent-dialogue: "Raise this when a student is preparing a discourse or rhetorical analysis. With a student, put it plainly as something the subject builds in you over the degree; with staff, frame it as a distinctive capacity an English course develops. Ask: 'What method would you use to show how this speech tries to persuade its audience?' Avoid reading the list aloud or treating it as the pass standard."
- statement: qaa/english-2023/1.6.b4
  forPractitioner: { text: "Expect a graduate of an English course to show critical reflection on what happens when we read, write and interpret; the statement names it as part of what marks the subject out.", rewrite: light, force: will, status: drafted }
  forBeneficiary: { text: "By the end of your English degree, you can think critically about what happens when you read, write and interpret.", rewrite: full, force: will, status: drafted }
  author-agent-written: "Describe this as one of the capacities English graduates are said to have, from the outcome list in 1.6 (introduced with 'can'), for the honours degree at FHEQ level 6 (FQHEIS level 10): reflecting on reading, writing and interpretation. Cite it as QAA (2023), English Subject Benchmark Statement, para 1.6, bullet 4. Do not present it as a threshold standard or a regulatory requirement; it describes the subject's emphasis, and the standards themselves are the 4.2 table. Set it beside 4.2.b30, 4.2.b35 and 4.2.b40, qaa/fheq-2024/4.15.b7 and qaa/fqheis-2024/4.16.b7."
  author-agent-dialogue: "Raise this when a student is writing a reflective or methodological section. With a student, put it plainly as something the subject builds in you over the degree; with staff, frame it as a distinctive capacity an English course develops. Ask: 'How has the way you read changed since you started the course?' Avoid reading the list aloud or treating it as the pass standard."
- statement: qaa/english-2023/1.6.b5
  forPractitioner: { text: "Expect a graduate of an English course to show the capacity to build their own imaginative and convincing readings of literary, critical, linguistic or creative material, possibly by producing new creative work; the statement names it as part of what marks the subject out.", rewrite: light, force: will, status: drafted }
  forBeneficiary: { text: "By the end of your English degree, you can build your own imaginative and convincing readings of literary, critical, linguistic or creative material, perhaps by writing new creative work of your own.", rewrite: full, force: will, status: drafted }
  author-agent-written: "Describe this as one of the capacities English graduates are said to have, from the outcome list in 1.6 (introduced with 'can'), for the honours degree at FHEQ level 6 (FQHEIS level 10): independent and persuasive interpretations, creative work included. Cite it as QAA (2023), English Subject Benchmark Statement, para 1.6, bullet 5. Do not present it as a threshold standard or a regulatory requirement; it describes the subject's emphasis, and the standards themselves are the 4.2 table. Set it beside 4.2.b25 to 4.2.b27, qaa/fheq-2024/4.15.b3.1 and qaa/fqheis-2024/4.16.b3."
  author-agent-dialogue: "Raise this when a student worries their reading is not original enough. With a student, put it plainly as something the subject builds in you over the degree; with staff, frame it as a distinctive capacity an English course develops. Ask: 'What is your reading of this text that someone else in the seminar might not have reached?' Avoid reading the list aloud or treating it as the pass standard."
- statement: qaa/english-2023/1.6.b6
  forPractitioner: { text: "Expect a graduate of an English course to show the capacity to express a critical grasp of demanding texts and ideas and of how they relate historically; the statement names it as part of what marks the subject out.", rewrite: light, force: will, status: drafted }
  forBeneficiary: { text: "By the end of your English degree, you can explain critically how demanding texts and ideas work and how they relate to each other over time.", rewrite: full, force: will, status: drafted }
  author-agent-written: "Describe this as one of the capacities English graduates are said to have, from the outcome list in 1.6 (introduced with 'can'), for the honours degree at FHEQ level 6 (FQHEIS level 10): critical understanding of complex texts and their history. Cite it as QAA (2023), English Subject Benchmark Statement, para 1.6, bullet 6. Do not present it as a threshold standard or a regulatory requirement; it describes the subject's emphasis, and the standards themselves are the 4.2 table. Set it beside 4.2.b29, 4.2.b34 and 4.2.b39, qaa/fheq-2024/4.15.b1 and qaa/fqheis-2024/4.16.b1."
  author-agent-dialogue: "Raise this when a student is planning a period or survey essay. With a student, put it plainly as something the subject builds in you over the degree; with staff, frame it as a distinctive capacity an English course develops. Ask: 'How does this text answer, or argue with, something written before it?' Avoid reading the list aloud or treating it as the pass standard."
- statement: qaa/english-2023/1.6.b7
  forPractitioner: { text: "Expect a graduate of an English course to show clear, accurate and effective communication, spoken, unspoken and written; the statement names it as part of what marks the subject out.", rewrite: light, force: will, status: drafted }
  forBeneficiary: { text: "By the end of your English degree, you can communicate clearly, accurately and effectively, whether speaking, writing or through other means.", rewrite: full, force: will, status: drafted }
  author-agent-written: "Describe this as one of the capacities English graduates are said to have, from the outcome list in 1.6 (introduced with 'can'), for the honours degree at FHEQ level 6 (FQHEIS level 10): clear, accurate and effective communication in all modes. Cite it as QAA (2023), English Subject Benchmark Statement, para 1.6, bullet 7. Do not present it as a threshold standard or a regulatory requirement; it describes the subject's emphasis, and the standards themselves are the 4.2 table. Set it beside 4.2.b1, 4.2.b3 and 4.2.b6, qaa/fheq-2024/4.15.b8 and qaa/fqheis-2024/4.16.b8."
  author-agent-dialogue: "Raise this when a student asks how presentations and written work are judged. With a student, put it plainly as something the subject builds in you over the degree; with staff, frame it as a distinctive capacity an English course develops. Ask: 'Which do you find hardest to get across clearly: spoken or written argument?' Avoid reading the list aloud or treating it as the pass standard."
- statement: qaa/english-2023/1.6.b8
  forPractitioner: { text: "Expect a graduate of an English course to show the capacity to use research and bibliographic skills that suit the subject; the statement names it as part of what marks the subject out.", rewrite: light, force: will, status: drafted }
  forBeneficiary: { text: "By the end of your English degree, you can use the research and referencing skills that suit English.", rewrite: full, force: will, status: drafted }
  author-agent-written: "Describe this as one of the capacities English graduates are said to have, from the outcome list in 1.6 (introduced with 'can'), for the honours degree at FHEQ level 6 (FQHEIS level 10): scholarly research and bibliographic skills. Cite it as QAA (2023), English Subject Benchmark Statement, para 1.6, bullet 8. Do not present it as a threshold standard or a regulatory requirement; it describes the subject's emphasis, and the standards themselves are the 4.2 table. Set it beside 4.2.b68 and 4.2.b70, qaa/fheq-2024/4.15.b5 and qaa/fqheis-2024/4.16.b5."
  author-agent-dialogue: "Raise this when a student starts a research essay or dissertation. With a student, put it plainly as something the subject builds in you over the degree; with staff, frame it as a distinctive capacity an English course develops. Ask: 'How do you find, record and cite the critical sources for an essay?' Avoid reading the list aloud or treating it as the pass standard."
- statement: qaa/english-2023/2.2.b1
  forPractitioner: { text: "Graduates will know about what language offers for expression, as far as their course covered it; map which modules supply this knowledge.", rewrite: light, force: will, status: drafted }
  forBeneficiary: { text: "Depending on the parts of English you study, you will know about what language gives you to express things.", rewrite: full, force: will, status: drafted }
  author-agent-written: "Describe this as a knowledge outcome stated with 'will' and qualified by what a graduate studied, for the honours degree at FHEQ level 6 (FQHEIS level 10): the expressive resources of language. Cite it as QAA (2023), English Subject Benchmark Statement, para 2.2, bullet 1. Do not claim every graduate knows the whole list, since the lead-in ties it to the aspects studied, or that it is a regulatory requirement. Set it beside 1.6.b2 and 4.2.b82, the content paragraphs 3.2 to 3.4 and qaa/fheq-2024/4.15.b1 (qaa/fqheis-2024/4.16.b1)."
  author-agent-dialogue: "Raise this when a student asks what a language module adds to a literature degree. With a student, say in plain words what knowing this involves and that it depends on the modules you choose; with staff, frame it as coverage to check in programme design. Ask: 'What can a writer do with sound, syntax or word choice that changes what a sentence means?' Avoid reading the list aloud or implying every student meets every item."
- statement: qaa/english-2023/2.2.b2
  forPractitioner: { text: "Graduates will know about literature or language across periods and the chief genres of prose, poetry and drama, as far as their course covered it; map which modules supply this knowledge.", rewrite: light, force: will, status: drafted }
  forBeneficiary: { text: "Depending on the parts of English you study, you will know about literature or language across different periods and the main genres of prose, poetry and drama.", rewrite: full, force: will, status: drafted }
  author-agent-written: "Describe this as a knowledge outcome stated with 'will' and qualified by what a graduate studied, for the honours degree at FHEQ level 6 (FQHEIS level 10): periods and the main literary genres. Cite it as QAA (2023), English Subject Benchmark Statement, para 2.2, bullet 2. Do not claim every graduate knows the whole list, since the lead-in ties it to the aspects studied, or that it is a regulatory requirement. Set it beside 3.3.s1 and 4.2.sk2, the content paragraphs 3.2 to 3.4 and qaa/fheq-2024/4.15.b1 (qaa/fqheis-2024/4.16.b1)."
  author-agent-dialogue: "Raise this when a student is choosing optional modules across periods. With a student, say in plain words what knowing this involves and that it depends on the modules you choose; with staff, frame it as coverage to check in programme design. Ask: 'Which period or genre have you studied least so far?' Avoid reading the list aloud or implying every student meets every item."
- statement: qaa/english-2023/2.2.b3
  forPractitioner: { text: "Graduates will know about how wide the body of literature written in English is, as far as their course covered it; map which modules supply this knowledge.", rewrite: light, force: will, status: drafted }
  forBeneficiary: { text: "Depending on the parts of English you study, you will know about how wide the range of literature written in English is.", rewrite: full, force: will, status: drafted }
  author-agent-written: "Describe this as a knowledge outcome stated with 'will' and qualified by what a graduate studied, for the honours degree at FHEQ level 6 (FQHEIS level 10): the range of literatures in English. Cite it as QAA (2023), English Subject Benchmark Statement, para 2.2, bullet 3. Do not claim every graduate knows the whole list, since the lead-in ties it to the aspects studied, or that it is a regulatory requirement. Set it beside 3.3 and 1.15, the content paragraphs 3.2 to 3.4 and qaa/fheq-2024/4.15.b1 (qaa/fqheis-2024/4.16.b1)."
  author-agent-dialogue: "Raise this when a student asks about world or postcolonial literature options. With a student, say in plain words what knowing this involves and that it depends on the modules you choose; with staff, frame it as coverage to check in programme design. Ask: 'Which literatures in English from outside Britain have you read?' Avoid reading the list aloud or implying every student meets every item."
- statement: qaa/english-2023/2.2.b4
  forPractitioner: { text: "Graduates will know about the varieties of English spoken and written in regions and around the world, as far as their course covered it; map which modules supply this knowledge.", rewrite: light, force: will, status: drafted }
  forBeneficiary: { text: "Depending on the parts of English you study, you will know about the varieties of English used in different regions and around the world.", rewrite: full, force: will, status: drafted }
  author-agent-written: "Describe this as a knowledge outcome stated with 'will' and qualified by what a graduate studied, for the honours degree at FHEQ level 6 (FQHEIS level 10): regional and global varieties of English. Cite it as QAA (2023), English Subject Benchmark Statement, para 2.2, bullet 4. Do not claim every graduate knows the whole list, since the lead-in ties it to the aspects studied, or that it is a regulatory requirement. Set it beside 3.2 and 4.2.sk1, the content paragraphs 3.2 to 3.4 and qaa/fheq-2024/4.15.b1 (qaa/fqheis-2024/4.16.b1)."
  author-agent-dialogue: "Raise this when a student asks what Global Englishes or dialect study covers. With a student, say in plain words what knowing this involves and that it depends on the modules you choose; with staff, frame it as coverage to check in programme design. Ask: 'Which variety of English do you speak, and how does it differ from another you know?' Avoid reading the list aloud or implying every student meets every item."
- statement: qaa/english-2023/2.2.b5
  forPractitioner: { text: "Graduates will know about the history, structure, levels and discourse uses of English, as far as their course covered it; map which modules supply this knowledge.", rewrite: light, force: will, status: drafted }
  forBeneficiary: { text: "Depending on the parts of English you study, you will know about the history and structure of English, its levels of analysis and how it works in discourse.", rewrite: full, force: will, status: drafted }
  author-agent-written: "Describe this as a knowledge outcome stated with 'will' and qualified by what a graduate studied, for the honours degree at FHEQ level 6 (FQHEIS level 10): how English is built and used. Cite it as QAA (2023), English Subject Benchmark Statement, para 2.2, bullet 5. Do not claim every graduate knows the whole list, since the lead-in ties it to the aspects studied, or that it is a regulatory requirement. Set it beside 3.2 and 4.2.sk1, the content paragraphs 3.2 to 3.4 and qaa/fheq-2024/4.15.b1 (qaa/fqheis-2024/4.16.b1)."
  author-agent-dialogue: "Raise this when a student starts a language or linguistics strand. With a student, say in plain words what knowing this involves and that it depends on the modules you choose; with staff, frame it as coverage to check in programme design. Ask: 'Can you name the levels at which a linguist analyses a sentence?' Avoid reading the list aloud or implying every student meets every item."
- statement: qaa/english-2023/2.2.b6
  forPractitioner: { text: "Graduates will know about the ways culture, language, technology and economics shape how, where and by whom texts are made and taken up, as far as their course covered it; map which modules supply this knowledge.", rewrite: light, force: will, status: drafted }
  forBeneficiary: { text: "Depending on the parts of English you study, you will know about how culture, language, technology and money shape how, where and by whom texts are made and read.", rewrite: full, force: will, status: drafted }
  author-agent-written: "Describe this as a knowledge outcome stated with 'will' and qualified by what a graduate studied, for the honours degree at FHEQ level 6 (FQHEIS level 10): how texts are made and received. Cite it as QAA (2023), English Subject Benchmark Statement, para 2.2, bullet 6. Do not claim every graduate knows the whole list, since the lead-in ties it to the aspects studied, or that it is a regulatory requirement. Set it beside 3.3 and 4.2.sk2, the content paragraphs 3.2 to 3.4 and qaa/fheq-2024/4.15.b1 (qaa/fqheis-2024/4.16.b1)."
  author-agent-dialogue: "Raise this when a student studies book history, publishing or media. With a student, say in plain words what knowing this involves and that it depends on the modules you choose; with staff, frame it as coverage to check in programme design. Ask: 'Who could afford to read this text when it first appeared, and how did it reach them?' Avoid reading the list aloud or implying every student meets every item."
- statement: qaa/english-2023/2.2.b7
  forPractitioner: { text: "Graduates will know about the part readers and audiences play in shaping texts, as far as their course covered it; map which modules supply this knowledge.", rewrite: light, force: will, status: drafted }
  forBeneficiary: { text: "Depending on the parts of English you study, you will know about the part readers and audiences play in shaping texts.", rewrite: full, force: will, status: drafted }
  author-agent-written: "Describe this as a knowledge outcome stated with 'will' and qualified by what a graduate studied, for the honours degree at FHEQ level 6 (FQHEIS level 10): readers and audiences shaping texts. Cite it as QAA (2023), English Subject Benchmark Statement, para 2.2, bullet 7. Do not claim every graduate knows the whole list, since the lead-in ties it to the aspects studied, or that it is a regulatory requirement. Set it beside 4.2.b52 and 4.2.b11, the content paragraphs 3.2 to 3.4 and qaa/fheq-2024/4.15.b1 (qaa/fqheis-2024/4.16.b1)."
  author-agent-dialogue: "Raise this when a student asks about reader-response or reception. With a student, say in plain words what knowing this involves and that it depends on the modules you choose; with staff, frame it as coverage to check in programme design. Ask: 'How might a reader today take this text differently from its first audience?' Avoid reading the list aloud or implying every student meets every item."
- statement: qaa/english-2023/2.2.b8
  forPractitioner: { text: "Graduates will know about how genres and media relate to one another, as far as their course covered it; map which modules supply this knowledge.", rewrite: light, force: will, status: drafted }
  forBeneficiary: { text: "Depending on the parts of English you study, you will know about how different genres and media relate to each other.", rewrite: full, force: will, status: drafted }
  author-agent-written: "Describe this as a knowledge outcome stated with 'will' and qualified by what a graduate studied, for the honours degree at FHEQ level 6 (FQHEIS level 10): relations between genres and media. Cite it as QAA (2023), English Subject Benchmark Statement, para 2.2, bullet 8. Do not claim every graduate knows the whole list, since the lead-in ties it to the aspects studied, or that it is a regulatory requirement. Set it beside 3.3 and 4.2.b82, the content paragraphs 3.2 to 3.4 and qaa/fheq-2024/4.15.b1 (qaa/fqheis-2024/4.16.b1)."
  author-agent-dialogue: "Raise this when a student works on adaptation or multimodal texts. With a student, say in plain words what knowing this involves and that it depends on the modules you choose; with staff, frame it as coverage to check in programme design. Ask: 'What changes when this story moves from page to screen?' Avoid reading the list aloud or implying every student meets every item."
- statement: qaa/english-2023/2.2.b9
  forPractitioner: { text: "Graduates will know about the concepts and terms of criticism, theory, linguistics and stylistics, as far as their course covered it; map which modules supply this knowledge.", rewrite: light, force: will, status: drafted }
  forBeneficiary: { text: "Depending on the parts of English you study, you will know about the concepts and vocabulary of criticism, theory, linguistics and stylistics.", rewrite: full, force: will, status: drafted }
  author-agent-written: "Describe this as a knowledge outcome stated with 'will' and qualified by what a graduate studied, for the honours degree at FHEQ level 6 (FQHEIS level 10): critical, theoretical, linguistic and stylistic terms. Cite it as QAA (2023), English Subject Benchmark Statement, para 2.2, bullet 9. Do not claim every graduate knows the whole list, since the lead-in ties it to the aspects studied, or that it is a regulatory requirement. Set it beside 4.2.sk1 to 4.2.sk3, the content paragraphs 3.2 to 3.4 and qaa/fheq-2024/4.15.b1 (qaa/fqheis-2024/4.16.b1)."
  author-agent-dialogue: "Raise this when a student is unsure which terms to use in analysis. With a student, say in plain words what knowing this involves and that it depends on the modules you choose; with staff, frame it as coverage to check in programme design. Ask: 'Which technical term would sharpen the point you are making here?' Avoid reading the list aloud or implying every student meets every item."
- statement: qaa/english-2023/2.4
  forPractitioner: { text: "Plan each level so it builds towards the threshold standards in 4.2, and make sure progression rules require students to complete and gain credit for every part of the course, practical work included.", rewrite: light, force: will, status: drafted }
  forBeneficiary: { text: "As you move through each year of your honours degree, what you learn builds towards the minimum standard for graduating, and you will usually need to pass and gain credit for everything you are assessed on.", rewrite: full, force: will, status: drafted }
  author-agent-written: "Describe this as a 'will' expectation about progression through the honours degree, stated at FHEQ Level 6 and FQHEIS Level 10. Cite it as QAA (2023), English Subject Benchmark Statement, para 2.4. Do not claim it sets credit rules, which belong to each provider, or that a second-class degree guarantees postgraduate entry. Set it beside 4.1, the threshold column of 4.2 and qaa/fheq-2024/4.15.i1 with spine:6."
  author-agent-dialogue: "Raise this when a student or a programme team asks how earlier years relate to the final standard. With a student, explain in plain second-person words that each year builds towards the minimum for graduating; with staff, frame it as level design and progression rules. Ask: 'Which skills from the final-year minimum does this first-year module start to build?' Avoid suggesting the statement sets credit or progression regulations."
- statement: qaa/english-2023/2.5
  forPractitioner: { text: "On joint and combined routes, set outcomes in English and let the partner subject add its own; make clear which ones the English part carries.", rewrite: light, force: will, status: drafted }
  forBeneficiary: { text: "If you take English with another subject, you will meet outcomes in English and gain more from your other subject.", rewrite: full, force: will, status: drafted }
  author-agent-written: "Describe this as a 'will' expectation for joint, combined and major-minor honours routes at FHEQ level 6 (FQHEIS level 10): such students meet English outcomes and add others from their second subject. Cite it as QAA (2023), English Subject Benchmark Statement, para 2.5. Do not claim joint students must meet every single-honours outcome in full; the standards table speaks of English as a significant component. Set it beside 1.1, the 4.2 lead-ins and spine:6."
  author-agent-dialogue: "Raise this when a joint-honours student or a programme team asks which English outcomes apply. With a student, say plainly that you meet English outcomes and others from your second subject; with staff, frame it as dividing outcomes between the two subjects. Ask: 'Which of your outcomes come from English and which from your other subject?' Avoid implying a joint student needs every single-honours item."
- statement: qaa/english-2023/2.10
  forPractitioner: { text: "Include external reviewers in periodic review of English courses, asking them to comment on planned changes, on whether threshold standards are met and on whether content suits the subject.", rewrite: light, force: will, status: drafted }
  forBeneficiary: { text: "not-applicable: a provider duty in course review; nothing for the student to do", rewrite: full, force: will, status: drafted }
  author-agent-written: "Treat this as a 'will' expectation on the provider, not a student outcome: external reviewers take part in periodic review. Cite it as QAA (2023), English Subject Benchmark Statement, para 2.10. Do not claim it is a regulatory requirement or describe it as something students meet. Set it beside 2.9 and 2.11 on review and external examining, and beside the threshold column of 4.2."
  author-agent-dialogue: "Raise this with a programme team preparing for periodic review. Put it in practitioner terms: who the external reviewers are and what they will be asked to judge. Ask: 'What evidence will show a reviewer that threshold standards are met?' Avoid raising it with students as if it were their task."
- statement: qaa/english-2023/3.3.s1
  forPractitioner: { text: "In a single honours English Literature course, normally include texts from before 1800, with the chance to study one or more early periods in depth.", rewrite: light, force: will, status: drafted }
  forBeneficiary: { text: "On a single honours English Literature course you will normally read texts from before 1800, and you may study one or more early periods in depth.", rewrite: full, force: will, status: drafted }
  author-agent-written: "Describe this as a 'will normally' expectation for single honours English Literature at FHEQ level 6 (FQHEIS level 10): students read texts from before 1800, and may study early periods. Cite it as QAA (2023), English Subject Benchmark Statement, para 3.3. Do not extend it to joint or language degrees as a rule, and keep the hedge 'normally'. Set it beside 4.2.sk2 (pre-1800 awareness for single honours), 2.2.b2 and qaa/fheq-2024/4.15.b1."
  author-agent-dialogue: "Raise this when a student or a team plans module choices across periods. With a student, say plainly that a single honours literature course will normally include older texts; with staff, frame it as coverage to check. Ask: 'Which texts from before 1800 have you studied, and which period would you like to know better?' Avoid presenting it as binding on every English course."
- statement: qaa/english-2023/4.2
  forPractitioner: { text: "When setting how marks above the threshold are evidenced and classified, consult Annex D's descriptions of the classes for honours degrees.", rewrite: light, force: should, status: drafted }
  forBeneficiary: { text: "not-applicable: a provider duty on how classifications are judged", rewrite: full, force: should, status: drafted }
  author-agent-written: "Treat this as a 'should' on the provider: it sets its own method for evidencing achievement above the threshold and should refer to Annex D. Cite it as QAA (2023), English Subject Benchmark Statement, para 4.2. Do not claim the statement itself defines the degree classes or that this binds the student. Set it beside std:doc:qaa-fheq-2024-framework, Annex D (qaa/fheq-2024/annex-d/summary/r1/3rd to r1/1st) and 4.1."
  author-agent-dialogue: "Raise this with a programme team or examiners when they align marking criteria with degree classes. Frame it for staff as using Annex D beside the typical and excellent columns. Ask: 'Which Annex D band does this typical-column item most resemble?' Avoid giving it to students as a task of theirs."
- statement: qaa/english-2023/4.2.b1
  forPractitioner: { text: "At threshold, every honours graduate in English will have shown the capacity to get ideas across clearly in speech, other modes and writing, building lucid arguments in a style that suits the audience; check that each passing student can evidence it.", rewrite: light, force: threshold, status: drafted }
  forBeneficiary: { text: "As a minimum for your honours degree, you will get your ideas across clearly in speech, writing and other forms, building lucid arguments in a style that suits your audience.", rewrite: full, force: threshold, status: drafted }
  author-agent-written: "Describe this as a threshold standard, the least an honours graduate in English will have shown at FHEQ level 6 (FQHEIS level 10): clear communication and lucid argument for an audience. Cite it as QAA (2023), English Subject Benchmark Statement, para 4.2, standards table, threshold column, communication (generic skills) row. Do not present it as a regulatory requirement or as where most students end up, since 4.2 expects most to perform well above it. Set it beside 4.2.b3, 4.2.b6 and 1.6.b7, qaa/fheq-2024/4.15.b8, qaa/fqheis-2024/4.16.b8 and spine:6."
  author-agent-dialogue: "Raise this when a student asks what counts as a clear argument at pass level. With a student, say plainly in the second person that this is the floor for the honours degree, not the goal; with staff, frame it as what every passing student has to be able to evidence. Ask: 'Who is the reader of this essay, and what do they need first to follow your case?' Avoid reading the table aloud or treating this minimum as the target."
- statement: qaa/english-2023/4.2.ex1
  forPractitioner: { text: "Read the excellent column through this definition: the top band shows the same capabilities at a higher pitch, wide independent reading; original thought and expression; broad knowledge used with subtlety, insight, rigour and creativity.", rewrite: light, force: will, status: drafted }
  forBeneficiary: { text: "If you reach the excellent level, you show the same skills at a higher level: you read widely on your own, think and write originally, understand deeply and use broad knowledge with subtlety, insight, rigour and creativity.", rewrite: full, force: will, status: drafted }
  author-agent-written: "Describe this as the definition of the excellent standard that heads the excellent column, for the honours degree at FHEQ level 6 (FQHEIS level 10). Cite it as QAA (2023), English Subject Benchmark Statement, para 4.2, standards table, excellent column heading. Do not claim it is a pass requirement or that most graduates reach it. Set it beside 4.2.b38, 4.2.b46, 4.2.b84 and qaa/fheq-2024/4.15.b1, and beside Annex D's first-class descriptions qaa/fheq-2024/annex-d/knowledge/r1/1st and qaa/fheq-2024/annex-d/cognitive/r4/1st."
  author-agent-dialogue: "Raise this when a student or staff member asks what separates excellent work from good work. With a student, put it plainly as what the best work looks like, something to stretch towards; with staff, frame it as the profile behind the top band. Ask: 'Where in your recent work did your own reading take you beyond the reading list?' Avoid presenting it as the minimum or reading it aloud."
- statement: qaa/english-2023/4.2.sk1
  forPractitioner: { text: "For the language parts of an English degree, plan knowledge of English in use and in history, its varieties and sub-disciplines and its methods of analysis, and make sure students use the field's concepts and terms and its referencing skills.", rewrite: light, force: will, status: drafted }
  forBeneficiary: { text: "If your degree includes English language, you will know how spoken, written and multimodal communication works, how English developed and varies and the main methods for studying it; and you will use the subject's concepts, terms and referencing skills.", rewrite: full, force: will, status: drafted }
  author-agent-written: "Describe this as subject knowledge stated with 'will' across all three columns of the standards table, varying in breadth and depth from threshold to excellent and by the elements of the degree, at FHEQ level 6 (FQHEIS level 10): subject knowledge for language elements. Cite it as QAA (2023), English Subject Benchmark Statement, para 4.2, standards table, subject knowledge (the row spanning all three columns). Do not claim every graduate covers each element, since 'may include' lists depend on the degree's make-up, or that it is a regulatory requirement. Set it beside 3.2, 2.2.b4 and 2.2.b5, qaa/fheq-2024/4.15.b1 and qaa/fqheis-2024/4.16.b1."
  author-agent-dialogue: "Raise this when a student on a language strand asks what they are expected to know. With a student, explain in plain second-person words what knowledge your mix of modules gives you and that depth grows from pass to top marks; with staff, frame it as the content map for each element. Ask: 'Which method of language analysis do you feel most at home with, and which least?' Avoid reading the paragraph aloud or treating its 'may include' lists as compulsory content."
- statement: qaa/english-2023/4.2.b2
  forPractitioner: { text: "At threshold, every honours graduate in English will have shown an understanding that good writing comes through revising and editing; check that each passing student can evidence it.", rewrite: light, force: threshold, status: drafted }
  forBeneficiary: { text: "As a minimum for your honours degree, you will understand that good writing comes through revising and editing your drafts.", rewrite: full, force: threshold, status: drafted }
  author-agent-written: "Describe this as a threshold standard, the least an honours graduate in English will have shown at FHEQ level 6 (FQHEIS level 10): writing as a process of revision and editing. Cite it as QAA (2023), English Subject Benchmark Statement, para 4.2, standards table, threshold column, communication (generic skills) row. Do not present it as a regulatory requirement or as where most students end up, since 4.2 expects most to perform well above it. Set it beside 4.2.b5, 4.2.b9 and 3.12.b10, qaa/fheq-2024/4.15.b8, qaa/fqheis-2024/4.16.b8 and spine:6."
  author-agent-dialogue: "Raise this when a student submits first drafts unrevised. With a student, say plainly in the second person that this is the floor for the honours degree, not the goal; with staff, frame it as what every passing student has to be able to evidence. Ask: 'What did you change between your first draft and the version you handed in?' Avoid reading the table aloud or treating this minimum as the target."
- statement: qaa/english-2023/4.2.sk2
  forPractitioner: { text: "For the literature parts of an English degree, cover close reading, form and style, links across forms, pre-1800 texts for single honours and the contexts of making and reception, across periods and all main genres, with the field's terms and referencing skills.", rewrite: light, force: will, status: drafted }
  forBeneficiary: { text: "If your degree includes English literature, you will read closely, know how texts work in form and style and in their contexts, study several periods and all the main genres; and you will use the subject's concepts, terms and referencing skills.", rewrite: full, force: will, status: drafted }
  author-agent-written: "Describe this as subject knowledge stated with 'will' across all three columns of the standards table, varying in breadth and depth from threshold to excellent and by the elements of the degree, at FHEQ level 6 (FQHEIS level 10): subject knowledge for literature elements. Cite it as QAA (2023), English Subject Benchmark Statement, para 4.2, standards table, subject knowledge (the row spanning all three columns). Do not claim every graduate covers each element, since 'may include' lists depend on the degree's make-up, or that it is a regulatory requirement. Set it beside 3.3, 3.3.s1 and 2.2.b2, qaa/fheq-2024/4.15.b1 and qaa/fqheis-2024/4.16.b1."
  author-agent-dialogue: "Raise this when a student on a literature strand asks what range they must cover. With a student, explain in plain second-person words what knowledge your mix of modules gives you and that depth grows from pass to top marks; with staff, frame it as the content map for each element. Ask: 'Which period or genre is thinnest in your reading so far?' Avoid reading the paragraph aloud or treating its 'may include' lists as compulsory content."
- statement: qaa/english-2023/4.2.b3
  forPractitioner: { text: "At the typical level, most honours graduates in English show clear communication in every mode, with lucid, coherent and rigorous arguments, persuasive expression and other writers' arguments built in; design teaching so that the main cluster of students reaches it.", rewrite: light, force: will, status: drafted }
  forBeneficiary: { text: "At the level most students reach by the end of the degree, you are able to communicate clearly in every mode, building coherent and rigorous arguments, writing persuasively and drawing other writers' arguments into your own.", rewrite: full, force: will, status: drafted }
  author-agent-written: "Describe this as a typical standard: what most honours graduates in English, the main cluster of results, are able to do at FHEQ level 6 (FQHEIS level 10), above the threshold: coherent, rigorous argument that draws in other views. Cite it as QAA (2023), English Subject Benchmark Statement, para 4.2, standards table, typical column, communication (generic skills) row. Do not claim it is the pass requirement or a regulatory standard; the threshold column is the minimum. Set it beside 4.2.b1 and 4.2.b6, qaa/fheq-2024/4.15.b8 and Annex D's upper second description qaa/fheq-2024/annex-d/transferable/r1/2.1."
  author-agent-dialogue: "Raise this when a student wants to move from a pass to a good essay. With a student, put it plainly in the second person as what most people show by the end of the degree, not the minimum; with staff, frame it as the profile teaching should help most students reach. Ask: 'Where in this essay do you bring in a critic's argument, and what does it do for your own?' Avoid presenting it as the pass mark or reading the table aloud."
- statement: qaa/english-2023/4.2.sk3
  forPractitioner: { text: "For the creative writing parts of an English degree, build reflection on own and peer practice from wide reading, knowledge of publishing and audiences, writing to briefs, drafting and collaboration, with the field's terms and referencing skills.", rewrite: light, force: will, status: drafted }
  forBeneficiary: { text: "If your degree includes creative writing, you will reflect on your own and others' writing in light of wide reading, understand how writers, publishers, texts and audiences connect, write to briefs, draft and collaborate; and you will use the subject's concepts, terms and referencing skills.", rewrite: full, force: will, status: drafted }
  author-agent-written: "Describe this as subject knowledge stated with 'will' across all three columns of the standards table, varying in breadth and depth from threshold to excellent and by the elements of the degree, at FHEQ level 6 (FQHEIS level 10): subject knowledge for creative writing elements. Cite it as QAA (2023), English Subject Benchmark Statement, para 4.2, standards table, subject knowledge (the row spanning all three columns). Do not claim every graduate covers each element, since 'may include' lists depend on the degree's make-up, or that it is a regulatory requirement. Set it beside 3.4 and 4.2.b79 to 4.2.b85, qaa/fheq-2024/4.15.b1 and qaa/fqheis-2024/4.16.b1."
  author-agent-dialogue: "Raise this when a creative writing student asks what critical knowledge is expected of them. With a student, explain in plain second-person words what knowledge your mix of modules gives you and that depth grows from pass to top marks; with staff, frame it as the content map for each element. Ask: 'How has your reading changed the way you draft?' Avoid reading the paragraph aloud or treating its 'may include' lists as compulsory content."
- statement: qaa/english-2023/4.2.b4
  forPractitioner: { text: "At the typical level, most honours graduates in English show a clear stance of their own in relation to the arguments of others, pitched for the audience; design teaching so that the main cluster of students reaches it.", rewrite: light, force: will, status: drafted }
  forBeneficiary: { text: "At the level most students reach by the end of the degree, you are able to take a clear position in relation to other people's arguments, pitched for your audience.", rewrite: full, force: will, status: drafted }
  author-agent-written: "Describe this as a typical standard: what most honours graduates in English, the main cluster of results, are able to do at FHEQ level 6 (FQHEIS level 10), above the threshold: taking a clear stance among others' arguments. Cite it as QAA (2023), English Subject Benchmark Statement, para 4.2, standards table, typical column, communication (generic skills) row. Do not claim it is the pass requirement or a regulatory standard; the threshold column is the minimum. Set it beside 4.2.b7 and 4.2.b3, qaa/fheq-2024/4.15.b7 and Annex D's upper second description qaa/fheq-2024/annex-d/cognitive/r2/2.1."
  author-agent-dialogue: "Raise this when a student summarises critics without a view of their own. With a student, put it plainly in the second person as what most people show by the end of the degree, not the minimum; with staff, frame it as the profile teaching should help most students reach. Ask: 'Where do you stand in relation to the critics you quote, and how would a reader know?' Avoid presenting it as the pass mark or reading the table aloud."
- statement: qaa/english-2023/4.2.b5
  forPractitioner: { text: "At the typical level, most honours graduates in English show a reflective way of writing that uses revision to make each draft better than the last; design teaching so that the main cluster of students reaches it.", rewrite: light, force: will, status: drafted }
  forBeneficiary: { text: "At the level most students reach by the end of the degree, you are able to reflect on how you write and use revision to make each draft better than the last.", rewrite: full, force: will, status: drafted }
  author-agent-written: "Describe this as a typical standard: what most honours graduates in English, the main cluster of results, are able to do at FHEQ level 6 (FQHEIS level 10), above the threshold: reflective revision from draft to draft. Cite it as QAA (2023), English Subject Benchmark Statement, para 4.2, standards table, typical column, communication (generic skills) row. Do not claim it is the pass requirement or a regulatory standard; the threshold column is the minimum. Set it beside 4.2.b2 and 4.2.b9, qaa/fheq-2024/4.15.b8 and Annex D's upper second description qaa/fheq-2024/annex-d/transferable/r5/2.1."
  author-agent-dialogue: "Raise this when a student asks how to use feedback on a draft. With a student, put it plainly in the second person as what most people show by the end of the degree, not the minimum; with staff, frame it as the profile teaching should help most students reach. Ask: 'What did revision change in your argument, not just your sentences?' Avoid presenting it as the pass mark or reading the table aloud."
- statement: qaa/english-2023/4.2.b6
  forPractitioner: { text: "At the excellent level, the strongest honours graduates in English show clear communication in every mode, including lucid, rigorous and incisive arguments that support complex, demanding and well-expressed central claims; treat it as evidence for the top band, not a requirement.", rewrite: light, force: will, status: drafted }
  forBeneficiary: { text: "If you reach the excellent level, you are able to communicate clearly in every mode, building incisive, rigorous arguments for complex and demanding central claims.", rewrite: full, force: will, status: drafted }
  author-agent-written: "Describe this as an excellent standard: what the strongest honours graduates in English are able to do at FHEQ level 6 (FQHEIS level 10), well above the threshold: incisive argument for complex, cogent central claims. Cite it as QAA (2023), English Subject Benchmark Statement, para 4.2, standards table, excellent column, communication (generic skills) row. Do not claim every graduate shows it or that it sets a pass requirement. Set it beside 4.2.b3 and 4.2.b1, qaa/fheq-2024/4.15.b8 and Annex D's first-class description qaa/fheq-2024/annex-d/transferable/r1/1st."
  author-agent-dialogue: "Raise this when a student aims for a first-class essay. With a student, put it plainly as a mark of the best work, something to stretch towards rather than a requirement; with staff, frame it as evidence for the top band. Ask: 'Can you state your central claim in one sentence, and is it one a reader could dispute?' Avoid presenting it as the minimum or as a checklist every student must complete."
- statement: qaa/english-2023/4.2.b7
  forPractitioner: { text: "At the excellent level, the strongest honours graduates in English show the capacity to name the strengths and weaknesses of other writers' arguments briefly and accurately; treat it as evidence for the top band, not a requirement.", rewrite: light, force: will, status: drafted }
  forBeneficiary: { text: "If you reach the excellent level, you are able to name the strengths and weaknesses of other writers' arguments briefly and accurately.", rewrite: full, force: will, status: drafted }
  author-agent-written: "Describe this as an excellent standard: what the strongest honours graduates in English are able to do at FHEQ level 6 (FQHEIS level 10), well above the threshold: concise, accurate assessment of other writers' arguments. Cite it as QAA (2023), English Subject Benchmark Statement, para 4.2, standards table, excellent column, communication (generic skills) row. Do not claim every graduate shows it or that it sets a pass requirement. Set it beside 4.2.b4 and 4.2.b37, qaa/fheq-2024/4.15.b7 and Annex D's first-class description qaa/fheq-2024/annex-d/cognitive/r2/1st."
  author-agent-dialogue: "Raise this when a student is writing a critical review or literature survey. With a student, put it plainly as a mark of the best work, something to stretch towards rather than a requirement; with staff, frame it as evidence for the top band. Ask: 'What is the strongest point in this critic's argument, and where does it give way?' Avoid presenting it as the minimum or as a checklist every student must complete."
- statement: qaa/english-2023/4.2.b8
  forPractitioner: { text: "At the excellent level, the strongest honours graduates in English show the capacity to change and extend their positions when new evidence and claims appear (the item continues after a page break); treat it as evidence for the top band, not a requirement.", rewrite: light, force: will, status: drafted }
  forBeneficiary: { text: "If you reach the excellent level, you are able to change and extend your position when new evidence or claims come to light.", rewrite: full, force: will, status: drafted }
  author-agent-written: "Describe this as an excellent standard: what the strongest honours graduates in English are able to do at FHEQ level 6 (FQHEIS level 10), well above the threshold: revising positions in light of new evidence. Cite it as QAA (2023), English Subject Benchmark Statement, para 4.2, standards table, excellent column, communication (generic skills) row. Do not claim every graduate shows it or that it sets a pass requirement. Set it beside 4.2.b4 and 4.2.b46, qaa/fheq-2024/4.15.b4 and Annex D's first-class description qaa/fheq-2024/annex-d/cognitive/r2/1st."
  author-agent-dialogue: "Raise this when a student meets evidence that cuts against their thesis. With a student, put it plainly as a mark of the best work, something to stretch towards rather than a requirement; with staff, frame it as evidence for the top band. Ask: 'What would make you change your mind about this argument?' Avoid presenting it as the minimum or as a checklist every student must complete."
- statement: qaa/english-2023/4.2.b9
  forPractitioner: { text: "At the excellent level, the strongest honours graduates in English show a disciplined commitment to their own writing, rereading their prose carefully before handing it in; treat it as evidence for the top band, not a requirement.", rewrite: light, force: will, status: drafted }
  forBeneficiary: { text: "If you reach the excellent level, you are able to commit to your own writing with discipline, rereading your prose carefully before you hand it in.", rewrite: full, force: will, status: drafted }
  author-agent-written: "Describe this as an excellent standard: what the strongest honours graduates in English are able to do at FHEQ level 6 (FQHEIS level 10), well above the threshold: disciplined writing habits and re-reading before submission. Cite it as QAA (2023), English Subject Benchmark Statement, para 4.2, standards table, excellent column, communication (generic skills) row. Do not claim every graduate shows it or that it sets a pass requirement. Set it beside 4.2.b5 and 4.2.b60, qaa/fheq-2024/4.15.b9.1 and Annex D's first-class description qaa/fheq-2024/annex-d/transferable/r3/1st."
  author-agent-dialogue: "Raise this when a student loses marks to avoidable slips. With a student, put it plainly as a mark of the best work, something to stretch towards rather than a requirement; with staff, frame it as evidence for the top band. Ask: 'How many times do you read a piece through before you submit it, and what do you look for?' Avoid presenting it as the minimum or as a checklist every student must complete."
- statement: qaa/english-2023/4.2.b10
  forPractitioner: { text: "At threshold, every honours graduate in English will have shown a recognition that language carries emotional force and can manipulate as well as persuade; check that each passing student can evidence it.", rewrite: light, force: threshold, status: drafted }
  forBeneficiary: { text: "As a minimum for your honours degree, you will recognise that language has emotional force and can manipulate people as well as persuade them.", rewrite: full, force: threshold, status: drafted }
  author-agent-written: "Describe this as a threshold standard, the least an honours graduate in English will have shown at FHEQ level 6 (FQHEIS level 10): the affective power of language. Cite it as QAA (2023), English Subject Benchmark Statement, para 4.2, standards table, threshold column, affective power of language (generic skills) row. Do not present it as a regulatory requirement or as where most students end up, since 4.2 expects most to perform well above it. Set it beside 4.2.b12, 4.2.b13 and 1.6.b3, qaa/fheq-2024/4.15.b7, qaa/fqheis-2024/4.16.b7 and spine:6."
  author-agent-dialogue: "Raise this when a student analyses political speech or advertising. With a student, say plainly in the second person that this is the floor for the honours degree, not the goal; with staff, frame it as what every passing student has to be able to evidence. Ask: 'Where does this text try to make you feel something rather than think something?' Avoid reading the table aloud or treating this minimum as the target."
- statement: qaa/english-2023/4.2.b11
  forPractitioner: { text: "At threshold, every honours graduate in English will have shown awareness of the audiences texts imply and of the need to adjust their own writing to particular readers; check that each passing student can evidence it.", rewrite: light, force: threshold, status: drafted }
  forBeneficiary: { text: "As a minimum for your honours degree, you will notice the audiences that texts imply, and adjust your own writing to the particular readers you have.", rewrite: full, force: threshold, status: drafted }
  author-agent-written: "Describe this as a threshold standard, the least an honours graduate in English will have shown at FHEQ level 6 (FQHEIS level 10): implied audiences and writing for an audience. Cite it as QAA (2023), English Subject Benchmark Statement, para 4.2, standards table, threshold column, affective power of language (generic skills) row. Do not present it as a regulatory requirement or as where most students end up, since 4.2 expects most to perform well above it. Set it beside 4.2.b12 and 4.2.b13, qaa/fheq-2024/4.15.b8, qaa/fqheis-2024/4.16.b8 and spine:6."
  author-agent-dialogue: "Raise this when a student writes in one register for every task. With a student, say plainly in the second person that this is the floor for the honours degree, not the goal; with staff, frame it as what every passing student has to be able to evidence. Ask: 'Who is this text written for, and who are you writing for in your reply?' Avoid reading the table aloud or treating this minimum as the target."
- statement: qaa/english-2023/4.2.b12
  forPractitioner: { text: "At the typical level, most honours graduates in English show recognition of and response to the emotional force of language, with fitting methods and terms, and clear, coherent communication to varied audiences; design teaching so that the main cluster of students reaches it.", rewrite: light, force: will, status: drafted }
  forBeneficiary: { text: "At the level most students reach by the end of the degree, you are able to recognise and respond to the emotional force of language with suitable methods and terms, and communicate clearly to different audiences.", rewrite: full, force: will, status: drafted }
  author-agent-written: "Describe this as a typical standard: what most honours graduates in English, the main cluster of results, are able to do at FHEQ level 6 (FQHEIS level 10), above the threshold: responding to affective language and writing for different audiences. Cite it as QAA (2023), English Subject Benchmark Statement, para 4.2, standards table, typical column, affective power of language (generic skills) row. Do not claim it is the pass requirement or a regulatory standard; the threshold column is the minimum. Set it beside 4.2.b10, 4.2.b11 and 4.2.b13, qaa/fheq-2024/4.15.b7 and Annex D's upper second description qaa/fheq-2024/annex-d/cognitive/r2/2.1."
  author-agent-dialogue: "Raise this when a student moves from noticing effects to analysing them. With a student, put it plainly in the second person as what most people show by the end of the degree, not the minimum; with staff, frame it as the profile teaching should help most students reach. Ask: 'What technique produces the effect you noticed, and how would you name it?' Avoid presenting it as the pass mark or reading the table aloud."
- statement: qaa/english-2023/4.2.b13
  forPractitioner: { text: "At the excellent level, the strongest honours graduates in English show analysis of the emotional force of language, using methods and terms suited to specific, defined audiences; treat it as evidence for the top band, not a requirement.", rewrite: light, force: will, status: drafted }
  forBeneficiary: { text: "If you reach the excellent level, you are able to analyse the emotional force of language, using methods and terms suited to specific, defined audiences.", rewrite: full, force: will, status: drafted }
  author-agent-written: "Describe this as an excellent standard: what the strongest honours graduates in English are able to do at FHEQ level 6 (FQHEIS level 10), well above the threshold: analysing affective language for defined audiences. Cite it as QAA (2023), English Subject Benchmark Statement, para 4.2, standards table, excellent column, affective power of language (generic skills) row. Do not claim every graduate shows it or that it sets a pass requirement. Set it beside 4.2.b12 and 4.2.b14, qaa/fheq-2024/4.15.b7 and Annex D's first-class description qaa/fheq-2024/annex-d/cognitive/r2/1st."
  author-agent-dialogue: "Raise this when a student writes a sophisticated stylistic or rhetorical analysis. With a student, put it plainly as a mark of the best work, something to stretch towards rather than a requirement; with staff, frame it as evidence for the top band. Ask: 'How would your analysis change if you were writing it for a specialist journal rather than a general reader?' Avoid presenting it as the minimum or as a checklist every student must complete."
- statement: qaa/english-2023/4.2.b14
  forPractitioner: { text: "At the excellent level, the strongest honours graduates in English show a command of rhetoric that lets them persuade and at times move their readers, with deftness in handling sensitive topics and difficult material; treat it as evidence for the top band, not a requirement.", rewrite: light, force: will, status: drafted }
  forBeneficiary: { text: "If you reach the excellent level, you are able to use rhetoric well enough to persuade and sometimes move your readers, and handle sensitive topics and difficult material with skill.", rewrite: full, force: will, status: drafted }
  author-agent-written: "Describe this as an excellent standard: what the strongest honours graduates in English are able to do at FHEQ level 6 (FQHEIS level 10), well above the threshold: command of rhetoric; handling sensitive material. Cite it as QAA (2023), English Subject Benchmark Statement, para 4.2, standards table, excellent column, affective power of language (generic skills) row. Do not claim every graduate shows it or that it sets a pass requirement. Set it beside 4.2.b13 and 4.2.b12, qaa/fheq-2024/4.15.b8 and Annex D's first-class description qaa/fheq-2024/annex-d/transferable/r1/1st."
  author-agent-dialogue: "Raise this when a student writes on a painful or contested subject. With a student, put it plainly as a mark of the best work, something to stretch towards rather than a requirement; with staff, frame it as evidence for the top band. Ask: 'How do you write about this difficult material in a way that respects your readers?' Avoid presenting it as the minimum or as a checklist every student must complete."
- statement: qaa/english-2023/4.2.b15
  forPractitioner: { text: "At threshold, every honours graduate in English will have shown ease with technology and digital communication and use of a range of digital platforms; check that each passing student can evidence it.", rewrite: light, force: threshold, status: drafted }
  forBeneficiary: { text: "As a minimum for your honours degree, you will be at ease with technology and digital communication and use a range of digital platforms.", rewrite: full, force: threshold, status: drafted }
  author-agent-written: "Describe this as a threshold standard, the least an honours graduate in English will have shown at FHEQ level 6 (FQHEIS level 10): comfort with technology and digital platforms. Cite it as QAA (2023), English Subject Benchmark Statement, para 4.2, standards table, threshold column, digital (generic skills) row. Do not present it as a regulatory requirement or as where most students end up, since 4.2 expects most to perform well above it. Set it beside 4.2.b16 and 4.2.b17, qaa/fheq-2024/4.15.b8, qaa/fqheis-2024/4.16.b8 and spine:6."
  author-agent-dialogue: "Raise this when a student is asked to produce a blog, podcast or digital edition. With a student, say plainly in the second person that this is the floor for the honours degree, not the goal; with staff, frame it as what every passing student has to be able to evidence. Ask: 'Which digital tools have you used to present your work so far?' Avoid reading the table aloud or treating this minimum as the target."
- statement: qaa/english-2023/4.2.b16
  forPractitioner: { text: "At the typical level, most honours graduates in English show ease with technology and digital communication and confident use of a range of digital platforms; design teaching so that the main cluster of students reaches it.", rewrite: light, force: will, status: drafted }
  forBeneficiary: { text: "At the level most students reach by the end of the degree, you are able to be at ease with technology and use a range of digital platforms with confidence.", rewrite: full, force: will, status: drafted }
  author-agent-written: "Describe this as a typical standard: what most honours graduates in English, the main cluster of results, are able to do at FHEQ level 6 (FQHEIS level 10), above the threshold: confident use of digital platforms. Cite it as QAA (2023), English Subject Benchmark Statement, para 4.2, standards table, typical column, digital (generic skills) row. Do not claim it is the pass requirement or a regulatory standard; the threshold column is the minimum. Set it beside 4.2.b15 and 4.2.b17, qaa/fheq-2024/4.15.b8 and Annex D's upper second description qaa/fheq-2024/annex-d/practical/r1/2.1."
  author-agent-dialogue: "Raise this when a student plans a digital or multimodal assessment. With a student, put it plainly in the second person as what most people show by the end of the degree, not the minimum; with staff, frame it as the profile teaching should help most students reach. Ask: 'Which platform suits this piece best, and why?' Avoid presenting it as the pass mark or reading the table aloud."
- statement: qaa/english-2023/4.2.b17
  forPractitioner: { text: "At the excellent level, the strongest honours graduates in English show use of several digital platforms, possibly with inventive use of new technologies to communicate their work; treat it as evidence for the top band, not a requirement.", rewrite: light, force: will, status: drafted }
  forBeneficiary: { text: "If you reach the excellent level, you are able to use several digital platforms and, where it helps, put new technologies to inventive use in sharing your work.", rewrite: full, force: will, status: drafted }
  author-agent-written: "Describe this as an excellent standard: what the strongest honours graduates in English are able to do at FHEQ level 6 (FQHEIS level 10), well above the threshold: inventive use of new technologies to communicate. Cite it as QAA (2023), English Subject Benchmark Statement, para 4.2, standards table, excellent column, digital (generic skills) row. Do not claim every graduate shows it or that it sets a pass requirement. Set it beside 4.2.b16 and 1.21, qaa/fheq-2024/4.15.b8 and Annex D's first-class description qaa/fheq-2024/annex-d/practical/r1/1st."
  author-agent-dialogue: "Raise this when a student wants to experiment with form or medium. With a student, put it plainly as a mark of the best work, something to stretch towards rather than a requirement; with staff, frame it as evidence for the top band. Ask: 'What could a new tool let you do with this work that print cannot?' Avoid presenting it as the minimum or as a checklist every student must complete."
- statement: qaa/english-2023/4.2.b18
  forPractitioner: { text: "At threshold, every honours graduate in English will have shown the capacity to work with others and on their own, showing autonomy, adaptability, resilience and self-management; check that each passing student can evidence it.", rewrite: light, force: threshold, status: drafted }
  forBeneficiary: { text: "As a minimum for your honours degree, you will work both with others and on your own, showing independence, adaptability, resilience and self-management.", rewrite: full, force: threshold, status: drafted }
  author-agent-written: "Describe this as a threshold standard, the least an honours graduate in English will have shown at FHEQ level 6 (FQHEIS level 10): collaboration and independent work with self-management. Cite it as QAA (2023), English Subject Benchmark Statement, para 4.2, standards table, threshold column, collaboration (generic skills) row. Do not present it as a regulatory requirement or as where most students end up, since 4.2 expects most to perform well above it. Set it beside 4.2.b20, 4.2.b21 and 1.5.b2, qaa/fheq-2024/4.15.b9.1, qaa/fqheis-2024/4.16.b9.1 and spine:6."
  author-agent-dialogue: "Raise this when a student starts a group project. With a student, say plainly in the second person that this is the floor for the honours degree, not the goal; with staff, frame it as what every passing student has to be able to evidence. Ask: 'When did you last have to manage your own work without anyone checking on it?' Avoid reading the table aloud or treating this minimum as the target."
- statement: qaa/english-2023/4.2.b19
  forPractitioner: { text: "At threshold, every honours graduate in English will have shown the capacity to build working relationships with others in a team; check that each passing student can evidence it.", rewrite: light, force: threshold, status: drafted }
  forBeneficiary: { text: "As a minimum for your honours degree, you will build working relationships with other people in a team.", rewrite: full, force: threshold, status: drafted }
  author-agent-written: "Describe this as a threshold standard, the least an honours graduate in English will have shown at FHEQ level 6 (FQHEIS level 10): working relationships in teams. Cite it as QAA (2023), English Subject Benchmark Statement, para 4.2, standards table, threshold column, collaboration (generic skills) row. Do not present it as a regulatory requirement or as where most students end up, since 4.2 expects most to perform well above it. Set it beside 4.2.b20 and 4.2.b22, qaa/fheq-2024/4.15.b9.1, qaa/fqheis-2024/4.16.b9.1 and spine:6."
  author-agent-dialogue: "Raise this when a student finds group work difficult. With a student, say plainly in the second person that this is the floor for the honours degree, not the goal; with staff, frame it as what every passing student has to be able to evidence. Ask: 'What helped, or got in the way of, working well with your last group?' Avoid reading the table aloud or treating this minimum as the target."
- statement: qaa/english-2023/4.2.b20
  forPractitioner: { text: "At the typical level, most honours graduates in English show collaboration and independent work with autonomy, adaptability, resilience and self-management, the core skills of teamwork such as listening and answering questions constructively; and the taking of set tasks and roles in a group; design teaching so that the main cluster of students reaches it.", rewrite: light, force: will, status: drafted }
  forBeneficiary: { text: "At the level most students reach by the end of the degree, you are able to work with others and on your own with independence and resilience, use core teamwork skills such as listening and answering questions constructively; and take on set tasks and roles in a group.", rewrite: full, force: will, status: drafted }
  author-agent-written: "Describe this as a typical standard: what most honours graduates in English, the main cluster of results, are able to do at FHEQ level 6 (FQHEIS level 10), above the threshold: teamwork skills and roles within a group. Cite it as QAA (2023), English Subject Benchmark Statement, para 4.2, standards table, typical column, collaboration (generic skills) row. Do not claim it is the pass requirement or a regulatory standard; the threshold column is the minimum. Set it beside 4.2.b18, 4.2.b19 and 4.2.b22, qaa/fheq-2024/4.15.b9.1 and Annex D's upper second description qaa/fheq-2024/annex-d/transferable/r2/2.1."
  author-agent-dialogue: "Raise this when a group is dividing up roles for a project. With a student, put it plainly in the second person as what most people show by the end of the degree, not the minimum; with staff, frame it as the profile teaching should help most students reach. Ask: 'Which role did you take in your last group, and which would you take next time?' Avoid presenting it as the pass mark or reading the table aloud."
- statement: qaa/english-2023/4.2.b21
  forPractitioner: { text: "At the excellent level, the strongest honours graduates in English show work with others and on their own, showing autonomy, adaptability, resilience and self-management (the same wording as the threshold item); treat it as evidence for the top band, not a requirement.", rewrite: light, force: will, status: drafted }
  forBeneficiary: { text: "If you reach the excellent level, you are able to work both with others and on your own, showing independence, adaptability, resilience and self-management.", rewrite: full, force: will, status: drafted }
  author-agent-written: "Describe this as an excellent standard: what the strongest honours graduates in English are able to do at FHEQ level 6 (FQHEIS level 10), well above the threshold: collaboration and independence at the excellent level. Cite it as QAA (2023), English Subject Benchmark Statement, para 4.2, standards table, excellent column, collaboration (generic skills) row. Do not claim every graduate shows it or that it sets a pass requirement. Set it beside 4.2.b18 and 4.2.b20, qaa/fheq-2024/4.15.b9.1 and Annex D's first-class description qaa/fheq-2024/annex-d/transferable/r3/1st."
  author-agent-dialogue: "Raise this when a strong student asks what more group work can show. With a student, put it plainly as a mark of the best work, something to stretch towards rather than a requirement; with staff, frame it as evidence for the top band. Ask: 'How did you balance leading your own part with supporting the group's whole?' Avoid presenting it as the minimum or as a checklist every student must complete."
- statement: qaa/english-2023/4.2.b22
  forPractitioner: { text: "At the excellent level, the strongest honours graduates in English show skilled teamwork: listening, asking searching questions and answering even critical questions constructively; treat it as evidence for the top band, not a requirement.", rewrite: light, force: will, status: drafted }
  forBeneficiary: { text: "If you reach the excellent level, you are able to take a skilled part in teamwork: listen to others, ask searching questions and answer even critical ones constructively.", rewrite: full, force: will, status: drafted }
  author-agent-written: "Describe this as an excellent standard: what the strongest honours graduates in English are able to do at FHEQ level 6 (FQHEIS level 10), well above the threshold: skilled participation in teamwork. Cite it as QAA (2023), English Subject Benchmark Statement, para 4.2, standards table, excellent column, collaboration (generic skills) row. Do not claim every graduate shows it or that it sets a pass requirement. Set it beside 4.2.b20 and 4.2.b24, qaa/fheq-2024/4.15.b9.1 and Annex D's first-class description qaa/fheq-2024/annex-d/transferable/r2/1st."
  author-agent-dialogue: "Raise this when a student meets sharp questions in a seminar or group. With a student, put it plainly as a mark of the best work, something to stretch towards rather than a requirement; with staff, frame it as evidence for the top band. Ask: 'How do you answer a question that challenges your idea in front of others?' Avoid presenting it as the minimum or as a checklist every student must complete."
- statement: qaa/english-2023/4.2.b23
  forPractitioner: { text: "At the excellent level, the strongest honours graduates in English show skill in taking in a broad range of viewpoints, attitudes, ethics and ideologies; treat it as evidence for the top band, not a requirement.", rewrite: light, force: will, status: drafted }
  forBeneficiary: { text: "If you reach the excellent level, you are able to take in a broad range of viewpoints, attitudes, ethics and ideologies with skill.", rewrite: full, force: will, status: drafted }
  author-agent-written: "Describe this as an excellent standard: what the strongest honours graduates in English are able to do at FHEQ level 6 (FQHEIS level 10), well above the threshold: holding many perspectives and ideologies. Cite it as QAA (2023), English Subject Benchmark Statement, para 4.2, standards table, excellent column, collaboration (generic skills) row. Do not claim every graduate shows it or that it sets a pass requirement. Set it beside 4.2.b62 and 4.2.b64, qaa/fheq-2024/4.15.b4 and Annex D's first-class description qaa/fheq-2024/annex-d/cognitive/r1/1st."
  author-agent-dialogue: "Raise this when a group holds very different views on a text or issue. With a student, put it plainly as a mark of the best work, something to stretch towards rather than a requirement; with staff, frame it as evidence for the top band. Ask: 'Which view in your group was furthest from yours, and what did you learn from it?' Avoid presenting it as the minimum or as a checklist every student must complete."
- statement: qaa/english-2023/4.2.b24
  forPractitioner: { text: "At the excellent level, the strongest honours graduates in English show frequent importance to their group's success, either by leading openly or through skills such as negotiating disagreement to reach agreement; treat it as evidence for the top band, not a requirement.", rewrite: light, force: will, status: drafted }
  forBeneficiary: { text: "If you reach the excellent level, you are able to often be key to your group's success, by leading openly or by skills such as negotiating disagreement until the group agrees.", rewrite: full, force: will, status: drafted }
  author-agent-written: "Describe this as an excellent standard: what the strongest honours graduates in English are able to do at FHEQ level 6 (FQHEIS level 10), well above the threshold: being central to a group's success, through leadership or negotiation. Cite it as QAA (2023), English Subject Benchmark Statement, para 4.2, standards table, excellent column, collaboration (generic skills) row. Do not claim every graduate shows it or that it sets a pass requirement. Set it beside 4.2.b20 and 4.2.b43, qaa/fheq-2024/4.15.b9.2 and Annex D's first-class description qaa/fheq-2024/annex-d/transferable/r2/1st."
  author-agent-dialogue: "Raise this when a group stalls over a disagreement. With a student, put it plainly as a mark of the best work, something to stretch towards rather than a requirement; with staff, frame it as evidence for the top band. Ask: 'How did your group reach agreement the last time it disagreed?' Avoid presenting it as the minimum or as a checklist every student must complete."
- statement: qaa/english-2023/4.2.b25
  forPractitioner: { text: "At threshold, every honours graduate in English will have shown creativity, developing readings of literary, critical, linguistic or creative material in their interpretation and writing; check that each passing student can evidence it.", rewrite: light, force: threshold, status: drafted }
  forBeneficiary: { text: "As a minimum for your honours degree, you will be creative and develop your own readings of literary, critical, linguistic or creative material in how you interpret and write.", rewrite: full, force: threshold, status: drafted }
  author-agent-written: "Describe this as a threshold standard, the least an honours graduate in English will have shown at FHEQ level 6 (FQHEIS level 10): creativity and interpretation of material. Cite it as QAA (2023), English Subject Benchmark Statement, para 4.2, standards table, threshold column, creativity (generic skills) row. Do not present it as a regulatory requirement or as where most students end up, since 4.2 expects most to perform well above it. Set it beside 4.2.b26, 4.2.b27 and 1.6.b5, qaa/fheq-2024/4.15.b3.1, qaa/fqheis-2024/4.16.b3 and spine:6."
  author-agent-dialogue: "Raise this when a student asks how creativity is judged in a critical essay. With a student, say plainly in the second person that this is the floor for the honours degree, not the goal; with staff, frame it as what every passing student has to be able to evidence. Ask: 'What is creative about the reading you are proposing?' Avoid reading the table aloud or treating this minimum as the target."
- statement: qaa/english-2023/4.2.b26
  forPractitioner: { text: "At the typical level, most honours graduates in English show creativity, with independent and imaginative readings of literary, critical, linguistic or creative material and an independent approach in their interpretation and writing; design teaching so that the main cluster of students reaches it.", rewrite: light, force: will, status: drafted }
  forBeneficiary: { text: "At the level most students reach by the end of the degree, you are able to be creative, developing independent and imaginative readings of literary, critical, linguistic or creative material, with your own approach to interpretation and writing.", rewrite: full, force: will, status: drafted }
  author-agent-written: "Describe this as a typical standard: what most honours graduates in English, the main cluster of results, are able to do at FHEQ level 6 (FQHEIS level 10), above the threshold: independent, imaginative interpretation. Cite it as QAA (2023), English Subject Benchmark Statement, para 4.2, standards table, typical column, creativity (generic skills) row. Do not claim it is the pass requirement or a regulatory standard; the threshold column is the minimum. Set it beside 4.2.b25 and 4.2.b27, qaa/fheq-2024/4.15.b3.1 and Annex D's upper second description qaa/fheq-2024/annex-d/cognitive/r4/2.1."
  author-agent-dialogue: "Raise this when a student relies heavily on lecture readings. With a student, put it plainly in the second person as what most people show by the end of the degree, not the minimum; with staff, frame it as the profile teaching should help most students reach. Ask: 'Which part of this reading is yours rather than the lecturer's?' Avoid presenting it as the pass mark or reading the table aloud."
- statement: qaa/english-2023/4.2.b27
  forPractitioner: { text: "At the excellent level, the strongest honours graduates in English show creativity, with independent and imaginative readings of literary, critical, linguistic or creative material that show originality as well as independence in interpretation and writing; treat it as evidence for the top band, not a requirement.", rewrite: light, force: will, status: drafted }
  forBeneficiary: { text: "If you reach the excellent level, you are able to be creative, developing independent and imaginative readings of literary, critical, linguistic or creative material that are original as well as your own.", rewrite: full, force: will, status: drafted }
  author-agent-written: "Describe this as an excellent standard: what the strongest honours graduates in English are able to do at FHEQ level 6 (FQHEIS level 10), well above the threshold: original, independent interpretation. Cite it as QAA (2023), English Subject Benchmark Statement, para 4.2, standards table, excellent column, creativity (generic skills) row. Do not claim every graduate shows it or that it sets a pass requirement. Set it beside 4.2.b26 and 4.2.b84, qaa/fheq-2024/4.15.b3.1 and Annex D's first-class description qaa/fheq-2024/annex-d/cognitive/r4/1st."
  author-agent-dialogue: "Raise this when a student aims for originality in a dissertation. With a student, put it plainly as a mark of the best work, something to stretch towards rather than a requirement; with staff, frame it as evidence for the top band. Ask: 'What would a reader learn from your reading that they could not find elsewhere?' Avoid presenting it as the minimum or as a checklist every student must complete."
- statement: qaa/english-2023/4.2.b28
  forPractitioner: { text: "At threshold, every honours graduate in English will have shown critical thought, with the capacity to understand, analyse and interpret; check that each passing student can evidence it.", rewrite: light, force: threshold, status: drafted }
  forBeneficiary: { text: "As a minimum for your honours degree, you will think critically and show that you can understand, analyse and interpret.", rewrite: full, force: threshold, status: drafted }
  author-agent-written: "Describe this as a threshold standard, the least an honours graduate in English will have shown at FHEQ level 6 (FQHEIS level 10): critical thinking: understanding, analysis and interpretation. Cite it as QAA (2023), English Subject Benchmark Statement, para 4.2, standards table, threshold column, critical thinking (generic skills) row. Do not present it as a regulatory requirement or as where most students end up, since 4.2 expects most to perform well above it. Set it beside 4.2.b33 and 1.5.b4, qaa/fheq-2024/4.15.b7, qaa/fqheis-2024/4.16.b7 and spine:6."
  author-agent-dialogue: "Raise this when a student asks what critical means in feedback. With a student, say plainly in the second person that this is the floor for the honours degree, not the goal; with staff, frame it as what every passing student has to be able to evidence. Ask: 'What question does your essay ask of the text, rather than about it?' Avoid reading the table aloud or treating this minimum as the target."
- statement: qaa/english-2023/4.2.b29
  forPractitioner: { text: "At threshold, every honours graduate in English will have shown the capacity to express a critical grasp of demanding texts and ideas and of how they relate over time; check that each passing student can evidence it.", rewrite: light, force: threshold, status: drafted }
  forBeneficiary: { text: "As a minimum for your honours degree, you will explain critically how demanding texts and ideas work and how they relate to each other over time.", rewrite: full, force: threshold, status: drafted }
  author-agent-written: "Describe this as a threshold standard, the least an honours graduate in English will have shown at FHEQ level 6 (FQHEIS level 10): critical understanding of complex texts and their history. Cite it as QAA (2023), English Subject Benchmark Statement, para 4.2, standards table, threshold column, critical thinking (generic skills) row. Do not present it as a regulatory requirement or as where most students end up, since 4.2 expects most to perform well above it. Set it beside 4.2.b34 and 1.6.b6, qaa/fheq-2024/4.15.b1, qaa/fqheis-2024/4.16.b1 and spine:6."
  author-agent-dialogue: "Raise this when a student writes a contextual or period essay. With a student, say plainly in the second person that this is the floor for the honours degree, not the goal; with staff, frame it as what every passing student has to be able to evidence. Ask: 'How does this text connect with what came before it?' Avoid reading the table aloud or treating this minimum as the target."
- statement: qaa/english-2023/4.2.b30
  forPractitioner: { text: "At threshold, every honours graduate in English will have shown critical reflection on reading and writing, and evaluation of literary and linguistic forms and other cultural artefacts; check that each passing student can evidence it.", rewrite: light, force: threshold, status: drafted }
  forBeneficiary: { text: "As a minimum for your honours degree, you will reflect critically on reading and writing, and judge literary and linguistic forms and other cultural works.", rewrite: full, force: threshold, status: drafted }
  author-agent-written: "Describe this as a threshold standard, the least an honours graduate in English will have shown at FHEQ level 6 (FQHEIS level 10): reflecting on reading and writing; evaluating forms and artefacts. Cite it as QAA (2023), English Subject Benchmark Statement, para 4.2, standards table, threshold column, critical thinking (generic skills) row. Do not present it as a regulatory requirement or as where most students end up, since 4.2 expects most to perform well above it. Set it beside 4.2.b35 and 1.6.b4, qaa/fheq-2024/4.15.b7, qaa/fqheis-2024/4.16.b7 and spine:6."
  author-agent-dialogue: "Raise this when a student writes a reflective commentary. With a student, say plainly in the second person that this is the floor for the honours degree, not the goal; with staff, frame it as what every passing student has to be able to evidence. Ask: 'What did writing this piece teach you about how you read?' Avoid reading the table aloud or treating this minimum as the target."
- statement: qaa/english-2023/4.2.b31
  forPractitioner: { text: "At threshold, every honours graduate in English will have shown rigour and precision in using and weighing data and evidence; check that each passing student can evidence it.", rewrite: light, force: threshold, status: drafted }
  forBeneficiary: { text: "As a minimum for your honours degree, you will use and weigh data and evidence with rigour and precision.", rewrite: full, force: threshold, status: drafted }
  author-agent-written: "Describe this as a threshold standard, the least an honours graduate in English will have shown at FHEQ level 6 (FQHEIS level 10): rigour and precision with data and evidence. Cite it as QAA (2023), English Subject Benchmark Statement, para 4.2, standards table, threshold column, critical thinking (generic skills) row. Do not present it as a regulatory requirement or as where most students end up, since 4.2 expects most to perform well above it. Set it beside 4.2.b36 and 3.12.b8, qaa/fheq-2024/4.15.b7, qaa/fqheis-2024/4.16.b7 and spine:6."
  author-agent-dialogue: "Raise this when a student quotes loosely or uses evidence carelessly. With a student, say plainly in the second person that this is the floor for the honours degree, not the goal; with staff, frame it as what every passing student has to be able to evidence. Ask: 'Does this quotation prove the point you attach to it?' Avoid reading the table aloud or treating this minimum as the target."
- statement: qaa/english-2023/4.2.b32
  forPractitioner: { text: "At threshold, every honours graduate in English will have shown the capacity to follow arguments and debates, work through disagreement and spot ambiguity; check that each passing student can evidence it.", rewrite: light, force: threshold, status: drafted }
  forBeneficiary: { text: "As a minimum for your honours degree, you will follow arguments and debates, work through disagreement and notice where meaning is ambiguous.", rewrite: full, force: threshold, status: drafted }
  author-agent-written: "Describe this as a threshold standard, the least an honours graduate in English will have shown at FHEQ level 6 (FQHEIS level 10): following debate, negotiating disagreement, seeing ambiguity. Cite it as QAA (2023), English Subject Benchmark Statement, para 4.2, standards table, threshold column, critical thinking (generic skills) row. Do not present it as a regulatory requirement or as where most students end up, since 4.2 expects most to perform well above it. Set it beside 4.2.b37 and 3.12.b6, qaa/fheq-2024/4.15.b4, qaa/fqheis-2024/4.16.b4 and spine:6."
  author-agent-dialogue: "Raise this when a seminar debate becomes heated. With a student, say plainly in the second person that this is the floor for the honours degree, not the goal; with staff, frame it as what every passing student has to be able to evidence. Ask: 'Where in this debate could both sides be partly right?' Avoid reading the table aloud or treating this minimum as the target."
- statement: qaa/english-2023/4.2.b33
  forPractitioner: { text: "At the typical level, most honours graduates in English show critical thought, with wide-ranging capacity to understand, analyse and interpret; design teaching so that the main cluster of students reaches it.", rewrite: light, force: will, status: drafted }
  forBeneficiary: { text: "At the level most students reach by the end of the degree, you are able to think critically, with a wide-ranging capacity to understand, analyse and interpret.", rewrite: full, force: will, status: drafted }
  author-agent-written: "Describe this as a typical standard: what most honours graduates in English, the main cluster of results, are able to do at FHEQ level 6 (FQHEIS level 10), above the threshold: wide powers of critical thought. Cite it as QAA (2023), English Subject Benchmark Statement, para 4.2, standards table, typical column, critical thinking (generic skills) row. Do not claim it is the pass requirement or a regulatory standard; the threshold column is the minimum. Set it beside 4.2.b28 and 4.2.b38, qaa/fheq-2024/4.15.b7 and Annex D's upper second description qaa/fheq-2024/annex-d/cognitive/r2/2.1."
  author-agent-dialogue: "Raise this when a student moves from description to analysis. With a student, put it plainly in the second person as what most people show by the end of the degree, not the minimum; with staff, frame it as the profile teaching should help most students reach. Ask: 'What does this analysis show that a summary would not?' Avoid presenting it as the pass mark or reading the table aloud."
- statement: qaa/english-2023/4.2.b34
  forPractitioner: { text: "At the typical level, most honours graduates in English show the capacity to express an advanced critical grasp of demanding texts and ideas and of how they relate over time; design teaching so that the main cluster of students reaches it.", rewrite: light, force: will, status: drafted }
  forBeneficiary: { text: "At the level most students reach by the end of the degree, you are able to explain with advanced critical understanding how demanding texts and ideas work and relate to each other over time.", rewrite: full, force: will, status: drafted }
  author-agent-written: "Describe this as a typical standard: what most honours graduates in English, the main cluster of results, are able to do at FHEQ level 6 (FQHEIS level 10), above the threshold: advanced critical understanding of complex texts. Cite it as QAA (2023), English Subject Benchmark Statement, para 4.2, standards table, typical column, critical thinking (generic skills) row. Do not claim it is the pass requirement or a regulatory standard; the threshold column is the minimum. Set it beside 4.2.b29 and 4.2.b39, qaa/fheq-2024/4.15.b1 and Annex D's upper second description qaa/fheq-2024/annex-d/knowledge/r1/2.1."
  author-agent-dialogue: "Raise this when a student works with dense theory or difficult texts. With a student, put it plainly in the second person as what most people show by the end of the degree, not the minimum; with staff, frame it as the profile teaching should help most students reach. Ask: 'Which idea in this text took you longest to grasp, and how would you now explain it?' Avoid presenting it as the pass mark or reading the table aloud."
- statement: qaa/english-2023/4.2.b35
  forPractitioner: { text: "At the typical level, most honours graduates in English show rigorous critical reflection on reading and writing, and evaluation of literary and linguistic forms and other cultural artefacts; design teaching so that the main cluster of students reaches it.", rewrite: light, force: will, status: drafted }
  forBeneficiary: { text: "At the level most students reach by the end of the degree, you are able to reflect critically and rigorously on reading and writing, and judge literary and linguistic forms and other cultural works.", rewrite: full, force: will, status: drafted }
  author-agent-written: "Describe this as a typical standard: what most honours graduates in English, the main cluster of results, are able to do at FHEQ level 6 (FQHEIS level 10), above the threshold: rigorous reflection on reading and writing; evaluating forms. Cite it as QAA (2023), English Subject Benchmark Statement, para 4.2, standards table, typical column, critical thinking (generic skills) row. Do not claim it is the pass requirement or a regulatory standard; the threshold column is the minimum. Set it beside 4.2.b30 and 4.2.b40, qaa/fheq-2024/4.15.b7 and Annex D's upper second description qaa/fheq-2024/annex-d/transferable/r5/2.1."
  author-agent-dialogue: "Raise this when a student evaluates form in close analysis. With a student, put it plainly in the second person as what most people show by the end of the degree, not the minimum; with staff, frame it as the profile teaching should help most students reach. Ask: 'Why might the writer have chosen this form rather than another?' Avoid presenting it as the pass mark or reading the table aloud."
- statement: qaa/english-2023/4.2.b36
  forPractitioner: { text: "At the typical level, most honours graduates in English show rigour and precision in using and weighing data and evidence (the same wording as the threshold item); design teaching so that the main cluster of students reaches it.", rewrite: light, force: will, status: drafted }
  forBeneficiary: { text: "At the level most students reach by the end of the degree, you are able to use and weigh data and evidence with rigour and precision.", rewrite: full, force: will, status: drafted }
  author-agent-written: "Describe this as a typical standard: what most honours graduates in English, the main cluster of results, are able to do at FHEQ level 6 (FQHEIS level 10), above the threshold: rigour and precision with data and evidence (typical). Cite it as QAA (2023), English Subject Benchmark Statement, para 4.2, standards table, typical column, critical thinking (generic skills) row. Do not claim it is the pass requirement or a regulatory standard; the threshold column is the minimum. Set it beside 4.2.b31 and 4.2.b42, qaa/fheq-2024/4.15.b7 and Annex D's upper second description qaa/fheq-2024/annex-d/practical/r4/2.1."
  author-agent-dialogue: "Raise this when a student builds a corpus or evidence-based argument. With a student, put it plainly in the second person as what most people show by the end of the degree, not the minimum; with staff, frame it as the profile teaching should help most students reach. Ask: 'How did you choose your evidence, and what did you leave out?' Avoid presenting it as the pass mark or reading the table aloud."
- statement: qaa/english-2023/4.2.b37
  forPractitioner: { text: "At the typical level, most honours graduates in English show engagement with arguments and debates, working through disagreement and understanding how ambiguity is used; design teaching so that the main cluster of students reaches it.", rewrite: light, force: will, status: drafted }
  forBeneficiary: { text: "At the level most students reach by the end of the degree, you are able to engage with arguments and debates, work through disagreement and understand how ambiguity can be used.", rewrite: full, force: will, status: drafted }
  author-agent-written: "Describe this as a typical standard: what most honours graduates in English, the main cluster of results, are able to do at FHEQ level 6 (FQHEIS level 10), above the threshold: engaging in debate and the uses of ambiguity. Cite it as QAA (2023), English Subject Benchmark Statement, para 4.2, standards table, typical column, critical thinking (generic skills) row. Do not claim it is the pass requirement or a regulatory standard; the threshold column is the minimum. Set it beside 4.2.b32 and 4.2.b43, qaa/fheq-2024/4.15.b4 and Annex D's upper second description qaa/fheq-2024/annex-d/cognitive/r2/2.1."
  author-agent-dialogue: "Raise this when a student meets a deliberately ambiguous text. With a student, put it plainly in the second person as what most people show by the end of the degree, not the minimum; with staff, frame it as the profile teaching should help most students reach. Ask: 'What does the ambiguity in this passage allow the writer to do?' Avoid presenting it as the pass mark or reading the table aloud."
- statement: qaa/english-2023/4.2.b38
  forPractitioner: { text: "At the excellent level, the strongest honours graduates in English show critical thought, with an extensive capacity to understand, analyse and interpret; treat it as evidence for the top band, not a requirement.", rewrite: light, force: will, status: drafted }
  forBeneficiary: { text: "If you reach the excellent level, you are able to think critically, with an extensive capacity to understand, analyse and interpret.", rewrite: full, force: will, status: drafted }
  author-agent-written: "Describe this as an excellent standard: what the strongest honours graduates in English are able to do at FHEQ level 6 (FQHEIS level 10), well above the threshold: extensive powers of critical thought. Cite it as QAA (2023), English Subject Benchmark Statement, para 4.2, standards table, excellent column, critical thinking (generic skills) row. Do not claim every graduate shows it or that it sets a pass requirement. Set it beside 4.2.b33 and 4.2.b28, qaa/fheq-2024/4.15.b7 and Annex D's first-class description qaa/fheq-2024/annex-d/cognitive/r2/1st."
  author-agent-dialogue: "Raise this when a student aims for the top band. With a student, put it plainly as a mark of the best work, something to stretch towards rather than a requirement; with staff, frame it as evidence for the top band. Ask: 'What does your analysis notice that most readers would miss?' Avoid presenting it as the minimum or as a checklist every student must complete."
- statement: qaa/english-2023/4.2.b39
  forPractitioner: { text: "At the excellent level, the strongest honours graduates in English show the capacity to express a sophisticated critical grasp of demanding texts and ideas and of how they relate over time; treat it as evidence for the top band, not a requirement.", rewrite: light, force: will, status: drafted }
  forBeneficiary: { text: "If you reach the excellent level, you are able to explain with sophisticated critical understanding how demanding texts and ideas work and relate to each other over time.", rewrite: full, force: will, status: drafted }
  author-agent-written: "Describe this as an excellent standard: what the strongest honours graduates in English are able to do at FHEQ level 6 (FQHEIS level 10), well above the threshold: sophisticated critical understanding of complex texts. Cite it as QAA (2023), English Subject Benchmark Statement, para 4.2, standards table, excellent column, critical thinking (generic skills) row. Do not claim every graduate shows it or that it sets a pass requirement. Set it beside 4.2.b34 and 4.2.b29, qaa/fheq-2024/4.15.b1 and Annex D's first-class description qaa/fheq-2024/annex-d/knowledge/r1/1st."
  author-agent-dialogue: "Raise this when a student plans an ambitious comparative essay. With a student, put it plainly as a mark of the best work, something to stretch towards rather than a requirement; with staff, frame it as evidence for the top band. Ask: 'How would you trace this idea across three centuries of writing?' Avoid presenting it as the minimum or as a checklist every student must complete."
- statement: qaa/english-2023/4.2.b40
  forPractitioner: { text: "At the excellent level, the strongest honours graduates in English show critical reflection on reading and writing in exact detail; treat it as evidence for the top band, not a requirement.", rewrite: light, force: will, status: drafted }
  forBeneficiary: { text: "If you reach the excellent level, you are able to reflect critically and in exact detail on reading and writing.", rewrite: full, force: will, status: drafted }
  author-agent-written: "Describe this as an excellent standard: what the strongest honours graduates in English are able to do at FHEQ level 6 (FQHEIS level 10), well above the threshold: precise, detailed reflection on reading and writing. Cite it as QAA (2023), English Subject Benchmark Statement, para 4.2, standards table, excellent column, critical thinking (generic skills) row. Do not claim every graduate shows it or that it sets a pass requirement. Set it beside 4.2.b35 and 4.2.b30, qaa/fheq-2024/4.15.b7 and Annex D's first-class description qaa/fheq-2024/annex-d/transferable/r5/1st."
  author-agent-dialogue: "Raise this when a student writes a reflective or methodological chapter. With a student, put it plainly as a mark of the best work, something to stretch towards rather than a requirement; with staff, frame it as evidence for the top band. Ask: 'Which precise moment in your reading changed your interpretation?' Avoid presenting it as the minimum or as a checklist every student must complete."
- statement: qaa/english-2023/4.2.b41
  forPractitioner: { text: "At the excellent level, the strongest honours graduates in English show evaluation of literary and linguistic forms and other cultural artefacts within a broad intellectual and historical setting; treat it as evidence for the top band, not a requirement.", rewrite: light, force: will, status: drafted }
  forBeneficiary: { text: "If you reach the excellent level, you are able to judge literary and linguistic forms and other cultural works within a broad intellectual and historical setting.", rewrite: full, force: will, status: drafted }
  author-agent-written: "Describe this as an excellent standard: what the strongest honours graduates in English are able to do at FHEQ level 6 (FQHEIS level 10), well above the threshold: evaluating forms and artefacts in wide context. Cite it as QAA (2023), English Subject Benchmark Statement, para 4.2, standards table, excellent column, critical thinking (generic skills) row. Do not claim every graduate shows it or that it sets a pass requirement. Set it beside 4.2.b35 and 4.2.b39, qaa/fheq-2024/4.15.b7 and Annex D's first-class description qaa/fheq-2024/annex-d/knowledge/r1/1st."
  author-agent-dialogue: "Raise this when a student places a text in its intellectual history. With a student, put it plainly as a mark of the best work, something to stretch towards rather than a requirement; with staff, frame it as evidence for the top band. Ask: 'What larger intellectual debate does this form take part in?' Avoid presenting it as the minimum or as a checklist every student must complete."
- statement: qaa/english-2023/4.2.b42
  forPractitioner: { text: "At the excellent level, the strongest honours graduates in English show rigour and precision in using and weighing data and evidence (the same wording as the lower columns); treat it as evidence for the top band, not a requirement.", rewrite: light, force: will, status: drafted }
  forBeneficiary: { text: "If you reach the excellent level, you are able to use and weigh data and evidence with rigour and precision.", rewrite: full, force: will, status: drafted }
  author-agent-written: "Describe this as an excellent standard: what the strongest honours graduates in English are able to do at FHEQ level 6 (FQHEIS level 10), well above the threshold: rigour and precision with data and evidence (excellent). Cite it as QAA (2023), English Subject Benchmark Statement, para 4.2, standards table, excellent column, critical thinking (generic skills) row. Do not claim every graduate shows it or that it sets a pass requirement. Set it beside 4.2.b36 and 4.2.b46, qaa/fheq-2024/4.15.b7 and Annex D's first-class description qaa/fheq-2024/annex-d/practical/r4/1st."
  author-agent-dialogue: "Raise this when a student handles complex or conflicting evidence. With a student, put it plainly as a mark of the best work, something to stretch towards rather than a requirement; with staff, frame it as evidence for the top band. Ask: 'Where does your evidence pull against your claim, and how do you deal with it?' Avoid presenting it as the minimum or as a checklist every student must complete."
- statement: qaa/english-2023/4.2.b43
  forPractitioner: { text: "At the excellent level, the strongest honours graduates in English show active engagement with arguments and debates, highly effective negotiation of disagreement and an understanding, analysis and appreciation of what ambiguity does and is worth; treat it as evidence for the top band, not a requirement.", rewrite: light, force: will, status: drafted }
  forBeneficiary: { text: "If you reach the excellent level, you are able to engage actively in arguments and debates, negotiate disagreement very effectively and understand, analyse and value what ambiguity does.", rewrite: full, force: will, status: drafted }
  author-agent-written: "Describe this as an excellent standard: what the strongest honours graduates in English are able to do at FHEQ level 6 (FQHEIS level 10), well above the threshold: active debate and the value of ambiguity. Cite it as QAA (2023), English Subject Benchmark Statement, para 4.2, standards table, excellent column, critical thinking (generic skills) row. Do not claim every graduate shows it or that it sets a pass requirement. Set it beside 4.2.b37 and 4.2.b24, qaa/fheq-2024/4.15.b4 and Annex D's first-class description qaa/fheq-2024/annex-d/cognitive/r2/1st."
  author-agent-dialogue: "Raise this when a student leads a seminar discussion. With a student, put it plainly as a mark of the best work, something to stretch towards rather than a requirement; with staff, frame it as evidence for the top band. Ask: 'How would you help a group that disagrees reach a better question rather than a winner?' Avoid presenting it as the minimum or as a checklist every student must complete."
- statement: qaa/english-2023/4.2.b44
  forPractitioner: { text: "At threshold, every honours graduate in English will have shown the capacity to find, collect, combine, arrange and use some evidence to support an argument; check that each passing student can evidence it.", rewrite: light, force: threshold, status: drafted }
  forBeneficiary: { text: "As a minimum for your honours degree, you will find, collect, combine, arrange and use some evidence to support an argument.", rewrite: full, force: threshold, status: drafted }
  author-agent-written: "Describe this as a threshold standard, the least an honours graduate in English will have shown at FHEQ level 6 (FQHEIS level 10): gathering and using some evidence for an argument. Cite it as QAA (2023), English Subject Benchmark Statement, para 4.2, standards table, threshold column, evidence (generic skills) row. Do not present it as a regulatory requirement or as where most students end up, since 4.2 expects most to perform well above it. Set it beside 4.2.b45 and 4.2.b31, qaa/fheq-2024/4.15.b5, qaa/fqheis-2024/4.16.b5 and spine:6."
  author-agent-dialogue: "Raise this when a student starts researching an essay. With a student, say plainly in the second person that this is the floor for the honours degree, not the goal; with staff, frame it as what every passing student has to be able to evidence. Ask: 'What evidence have you gathered so far, and which piece does the most work?' Avoid reading the table aloud or treating this minimum as the target."
- statement: qaa/english-2023/4.2.b45
  forPractitioner: { text: "At the typical level, most honours graduates in English show the capacity to work through and interpret the evidence they collect, set it in wider contexts and frame research questions that take their enquiry further (weaker students at this level may still cite evidence descriptively); design teaching so that the main cluster of students reaches it.", rewrite: light, force: will, status: drafted }
  forBeneficiary: { text: "At the level most students reach by the end of the degree, you are able to work through and interpret the evidence you collect, set it in wider contexts and frame research questions that take your enquiry further.", rewrite: full, force: will, status: drafted }
  author-agent-written: "Describe this as a typical standard: what most honours graduates in English, the main cluster of results, are able to do at FHEQ level 6 (FQHEIS level 10), above the threshold: interpreting evidence and framing research questions. Cite it as QAA (2023), English Subject Benchmark Statement, para 4.2, standards table, typical column, evidence (generic skills) row. Do not claim it is the pass requirement or a regulatory standard; the threshold column is the minimum. Set it beside 4.2.b44 and 4.2.b46, qaa/fheq-2024/4.15.b7 and Annex D's upper second description qaa/fheq-2024/annex-d/cognitive/r1/2.1."
  author-agent-dialogue: "Raise this when a student plans a dissertation question. With a student, put it plainly in the second person as what most people show by the end of the degree, not the minimum; with staff, frame it as the profile teaching should help most students reach. Ask: 'What question does your evidence raise that you have not yet asked?' Avoid presenting it as the pass mark or reading the table aloud."
- statement: qaa/english-2023/4.2.b46
  forPractitioner: { text: "At the excellent level, the strongest honours graduates in English show independent, critical interpretation and analysis of the evidence they gather, with sharply defined lines of enquiry that yield cogent, well-built arguments and firm judgements showing critical understanding of complex texts and ideas; treat it as evidence for the top band, not a requirement.", rewrite: light, force: will, status: drafted }
  forBeneficiary: { text: "If you reach the excellent level, you are able to interpret and analyse the evidence you gather independently and critically, and follow sharply defined lines of enquiry to cogent, well-built arguments and firm judgements.", rewrite: full, force: will, status: drafted }
  author-agent-written: "Describe this as an excellent standard: what the strongest honours graduates in English are able to do at FHEQ level 6 (FQHEIS level 10), well above the threshold: independent analysis of evidence and well-defined enquiry. Cite it as QAA (2023), English Subject Benchmark Statement, para 4.2, standards table, excellent column, evidence (generic skills) row. Do not claim every graduate shows it or that it sets a pass requirement. Set it beside 4.2.b45 and 4.2.b8, qaa/fheq-2024/4.15.b6 and Annex D's first-class description qaa/fheq-2024/annex-d/cognitive/r1/1st."
  author-agent-dialogue: "Raise this when a student designs an independent research project. With a student, put it plainly as a mark of the best work, something to stretch towards rather than a requirement; with staff, frame it as evidence for the top band. Ask: 'What is your line of enquiry, and how will you know when it has reached a judgement?' Avoid presenting it as the minimum or as a checklist every student must complete."
- statement: qaa/english-2023/4.2.b47
  forPractitioner: { text: "At threshold, every honours graduate in English will have shown an understanding of how close reading works; check that each passing student can evidence it.", rewrite: light, force: threshold, status: drafted }
  forBeneficiary: { text: "As a minimum for your honours degree, you will understand how close reading works.", rewrite: full, force: threshold, status: drafted }
  author-agent-written: "Describe this as a threshold standard, the least an honours graduate in English will have shown at FHEQ level 6 (FQHEIS level 10): the technique of close reading. Cite it as QAA (2023), English Subject Benchmark Statement, para 4.2, standards table, threshold column, close reading (subject knowledge) row. Do not present it as a regulatory requirement or as where most students end up, since 4.2 expects most to perform well above it. Set it beside 4.2.b48, 4.2.b49 and 1.6.b1, qaa/fheq-2024/4.15.b2, qaa/fqheis-2024/4.16.b2 and spine:6."
  author-agent-dialogue: "Raise this when a student asks what close reading is for. With a student, say plainly in the second person that this is the floor for the honours degree, not the goal; with staff, frame it as what every passing student has to be able to evidence. Ask: 'Pick one line: what does it do, word by word?' Avoid reading the table aloud or treating this minimum as the target."
- statement: qaa/english-2023/4.2.b48
  forPractitioner: { text: "At the typical level, most honours graduates in English show use of close reading, which at the lower second may stay formulaic, descriptive and loosely tied to the argument, and at the upper second is anchored more firmly in their own case; design teaching so that the main cluster of students reaches it.", rewrite: light, force: will, status: drafted }
  forBeneficiary: { text: "At the level most students reach by the end of the degree, you are able to use close reading, and tie what you notice in a passage firmly into your own argument rather than describing it.", rewrite: full, force: will, status: drafted }
  author-agent-written: "Describe this as a typical standard: what most honours graduates in English, the main cluster of results, are able to do at FHEQ level 6 (FQHEIS level 10), above the threshold: using close reading in argument. Cite it as QAA (2023), English Subject Benchmark Statement, para 4.2, standards table, typical column, close reading (subject knowledge) row. Do not claim it is the pass requirement or a regulatory standard; the threshold column is the minimum. Set it beside 4.2.b47 and 4.2.b49, qaa/fheq-2024/4.15.b2 and Annex D's upper second description qaa/fheq-2024/annex-d/practical/r1/2.1."
  author-agent-dialogue: "Raise this when feedback says a student describes rather than analyses. With a student, put it plainly in the second person as what most people show by the end of the degree, not the minimum; with staff, frame it as the profile teaching should help most students reach. Ask: 'How does this observation about the passage move your argument forward?' Avoid presenting it as the pass mark or reading the table aloud."
- statement: qaa/english-2023/4.2.b49
  forPractitioner: { text: "At the excellent level, the strongest honours graduates in English show sharp, original observations drawn from sustained attention to passages, alert to form, device and figures of speech, linked to a reading of the whole text and woven into the argument; treat it as evidence for the top band, not a requirement.", rewrite: light, force: will, status: drafted }
  forBeneficiary: { text: "If you reach the excellent level, you are able to draw sharp, original observations from sustained attention to passages, alert to form and figurative language, and weave them into your reading of the whole text.", rewrite: full, force: will, status: drafted }
  author-agent-written: "Describe this as an excellent standard: what the strongest honours graduates in English are able to do at FHEQ level 6 (FQHEIS level 10), well above the threshold: incisive close reading embedded in argument. Cite it as QAA (2023), English Subject Benchmark Statement, para 4.2, standards table, excellent column, close reading (subject knowledge) row. Do not claim every graduate shows it or that it sets a pass requirement. Set it beside 4.2.b48 and 4.2.b27, qaa/fheq-2024/4.15.b2 and Annex D's first-class description qaa/fheq-2024/annex-d/practical/r1/1st."
  author-agent-dialogue: "Raise this when a student aims to make close reading the engine of an essay. With a student, put it plainly as a mark of the best work, something to stretch towards rather than a requirement; with staff, frame it as evidence for the top band. Ask: 'How does this detail change how we read the whole text?' Avoid presenting it as the minimum or as a checklist every student must complete."
- statement: qaa/english-2023/4.2.b50
  forPractitioner: { text: "At threshold, every honours graduate in English will have shown awareness that texts can bear several meanings and an understanding that this does not reduce interpretation to personal opinion; check that each passing student can evidence it.", rewrite: light, force: threshold, status: drafted }
  forBeneficiary: { text: "As a minimum for your honours degree, you will know that a text can carry several meanings, and understand that this does not make every reading just a matter of opinion.", rewrite: full, force: threshold, status: drafted }
  author-agent-written: "Describe this as a threshold standard, the least an honours graduate in English will have shown at FHEQ level 6 (FQHEIS level 10): plurality of meaning without mere opinion. Cite it as QAA (2023), English Subject Benchmark Statement, para 4.2, standards table, threshold column, interpretation (subject knowledge) row. Do not present it as a regulatory requirement or as where most students end up, since 4.2 expects most to perform well above it. Set it beside 4.2.b51, 4.2.b52 and 4.2.b32, qaa/fheq-2024/4.15.b4, qaa/fqheis-2024/4.16.b4 and spine:6."
  author-agent-dialogue: "Raise this when a student says any reading is valid if it is their opinion. With a student, say plainly in the second person that this is the floor for the honours degree, not the goal; with staff, frame it as what every passing student has to be able to evidence. Ask: 'What in the text supports your reading, and what would count against it?' Avoid reading the table aloud or treating this minimum as the target."
- statement: qaa/english-2023/4.2.b51
  forPractitioner: { text: "At the typical level, most honours graduates in English show the capacity to weigh the grounds and worth of different readings; design teaching so that the main cluster of students reaches it.", rewrite: light, force: will, status: drafted }
  forBeneficiary: { text: "At the level most students reach by the end of the degree, you are able to weigh the grounds and worth of different readings of a text.", rewrite: full, force: will, status: drafted }
  author-agent-written: "Describe this as a typical standard: what most honours graduates in English, the main cluster of results, are able to do at FHEQ level 6 (FQHEIS level 10), above the threshold: evaluating competing interpretations. Cite it as QAA (2023), English Subject Benchmark Statement, para 4.2, standards table, typical column, interpretation (subject knowledge) row. Do not claim it is the pass requirement or a regulatory standard; the threshold column is the minimum. Set it beside 4.2.b50 and 4.2.b52, qaa/fheq-2024/4.15.b7 and Annex D's upper second description qaa/fheq-2024/annex-d/cognitive/r2/2.1."
  author-agent-dialogue: "Raise this when a student meets conflicting critical readings. With a student, put it plainly in the second person as what most people show by the end of the degree, not the minimum; with staff, frame it as the profile teaching should help most students reach. Ask: 'Which of these two readings is better grounded, and why?' Avoid presenting it as the pass mark or reading the table aloud."
- statement: qaa/english-2023/4.2.b52
  forPractitioner: { text: "At the excellent level, the strongest honours graduates in English show a recognition of how rich language is and how it carries many, often ambiguous meanings, of how readers shape texts and of how texts shape readers' responses; treat it as evidence for the top band, not a requirement.", rewrite: light, force: will, status: drafted }
  forBeneficiary: { text: "If you reach the excellent level, you are able to recognise how rich language is and how it carries many meanings, and how readers shape texts and texts shape readers.", rewrite: full, force: will, status: drafted }
  author-agent-written: "Describe this as an excellent standard: what the strongest honours graduates in English are able to do at FHEQ level 6 (FQHEIS level 10), well above the threshold: richness of language; readers and texts shaping each other. Cite it as QAA (2023), English Subject Benchmark Statement, para 4.2, standards table, excellent column, interpretation (subject knowledge) row. Do not claim every graduate shows it or that it sets a pass requirement. Set it beside 4.2.b51 and 1.6.b2, qaa/fheq-2024/4.15.b4 and Annex D's first-class description qaa/fheq-2024/annex-d/knowledge/r1/1st."
  author-agent-dialogue: "Raise this when a student explores reception or reader-response theory. With a student, put it plainly as a mark of the best work, something to stretch towards rather than a requirement; with staff, frame it as evidence for the top band. Ask: 'How has this text shaped the way its readers respond, and how have they shaped it?' Avoid presenting it as the minimum or as a checklist every student must complete."
- statement: qaa/english-2023/4.2.b53
  forPractitioner: { text: "At threshold, every honours graduate in English will have shown the capacity to understand and complete a range of assessment tasks, including starting and finishing their own long projects under supervision; check that each passing student can evidence it.", rewrite: light, force: threshold, status: drafted }
  forBeneficiary: { text: "As a minimum for your honours degree, you will understand and complete a range of assessment tasks, including starting and finishing your own long project with a supervisor.", rewrite: full, force: threshold, status: drafted }
  author-agent-written: "Describe this as a threshold standard, the least an honours graduate in English will have shown at FHEQ level 6 (FQHEIS level 10): carrying out varied tasks and supervised long projects. Cite it as QAA (2023), English Subject Benchmark Statement, para 4.2, standards table, threshold column, assessment tasks and time (embedded understanding) row. Do not present it as a regulatory requirement or as where most students end up, since 4.2 expects most to perform well above it. Set it beside 4.2.b55 and 3.9, qaa/fheq-2024/4.15.b6, qaa/fqheis-2024/4.16.b6 and spine:6."
  author-agent-dialogue: "Raise this when a student begins a dissertation. With a student, say plainly in the second person that this is the floor for the honours degree, not the goal; with staff, frame it as what every passing student has to be able to evidence. Ask: 'What is the first milestone in your project, and when is it due?' Avoid reading the table aloud or treating this minimum as the target."
- statement: qaa/english-2023/4.2.b54
  forPractitioner: { text: "At threshold, every honours graduate in English will have shown an understanding that time must be planned to meet several deadlines and that meeting them is wise, though they may not always manage it; check that each passing student can evidence it.", rewrite: light, force: threshold, status: drafted }
  forBeneficiary: { text: "As a minimum for your honours degree, you will understand that you need to plan your time to meet several deadlines and that meeting them matters, even if you do not always manage it.", rewrite: full, force: threshold, status: drafted }
  author-agent-written: "Describe this as a threshold standard, the least an honours graduate in English will have shown at FHEQ level 6 (FQHEIS level 10): planning time for deadlines. Cite it as QAA (2023), English Subject Benchmark Statement, para 4.2, standards table, threshold column, assessment tasks and time (embedded understanding) row. Do not present it as a regulatory requirement or as where most students end up, since 4.2 expects most to perform well above it. Set it beside 4.2.b57 and 4.2.b60, qaa/fheq-2024/4.15.b9.1, qaa/fqheis-2024/4.16.b9.1 and spine:6."
  author-agent-dialogue: "Raise this when a student has bunched deadlines. With a student, say plainly in the second person that this is the floor for the honours degree, not the goal; with staff, frame it as what every passing student has to be able to evidence. Ask: 'Which deadline is most at risk this month, and what will you do about it?' Avoid reading the table aloud or treating this minimum as the target."
- statement: qaa/english-2023/4.2.b55
  forPractitioner: { text: "At the typical level, most honours graduates in English show quick adaptation to differing demands and tasks; design teaching so that the main cluster of students reaches it.", rewrite: light, force: will, status: drafted }
  forBeneficiary: { text: "At the level most students reach by the end of the degree, you are able to adapt quickly to different demands and tasks.", rewrite: full, force: will, status: drafted }
  author-agent-written: "Describe this as a typical standard: what most honours graduates in English, the main cluster of results, are able to do at FHEQ level 6 (FQHEIS level 10), above the threshold: adapting to different demands and tasks. Cite it as QAA (2023), English Subject Benchmark Statement, para 4.2, standards table, typical column, assessment tasks and time (embedded understanding) row. Do not claim it is the pass requirement or a regulatory standard; the threshold column is the minimum. Set it beside 4.2.b53 and 4.2.b58, qaa/fheq-2024/4.15.b9.2 and Annex D's upper second description qaa/fheq-2024/annex-d/transferable/r4/2.1."
  author-agent-dialogue: "Raise this when a student faces an unfamiliar form of assessment. With a student, put it plainly in the second person as what most people show by the end of the degree, not the minimum; with staff, frame it as the profile teaching should help most students reach. Ask: 'What is new about this task, and what from earlier work can you carry over?' Avoid presenting it as the pass mark or reading the table aloud."
- statement: qaa/english-2023/4.2.b56
  forPractitioner: { text: "At the typical level, most honours graduates in English show responsibility for their own work and readiness to seek help when they need it; design teaching so that the main cluster of students reaches it.", rewrite: light, force: will, status: drafted }
  forBeneficiary: { text: "At the level most students reach by the end of the degree, you are able to take responsibility for your own work and ask for help early when you need it.", rewrite: full, force: will, status: drafted }
  author-agent-written: "Describe this as a typical standard: what most honours graduates in English, the main cluster of results, are able to do at FHEQ level 6 (FQHEIS level 10), above the threshold: owning work and seeking help early. Cite it as QAA (2023), English Subject Benchmark Statement, para 4.2, standards table, typical column, assessment tasks and time (embedded understanding) row. Do not claim it is the pass requirement or a regulatory standard; the threshold column is the minimum. Set it beside 4.2.b59 and 4.2.b54, qaa/fheq-2024/4.15.b9.1 and Annex D's upper second description qaa/fheq-2024/annex-d/transferable/r3/2.1."
  author-agent-dialogue: "Raise this when a student is struggling but has not asked for help. With a student, put it plainly in the second person as what most people show by the end of the degree, not the minimum; with staff, frame it as the profile teaching should help most students reach. Ask: 'Who could you ask about this, and what is stopping you?' Avoid presenting it as the pass mark or reading the table aloud."
- statement: qaa/english-2023/4.2.b57
  forPractitioner: { text: "At the typical level, most honours graduates in English show planning of their time so that work arrives by several set deadlines; design teaching so that the main cluster of students reaches it.", rewrite: light, force: will, status: drafted }
  forBeneficiary: { text: "At the level most students reach by the end of the degree, you are able to plan your time so that your work arrives by each of several set deadlines.", rewrite: full, force: will, status: drafted }
  author-agent-written: "Describe this as a typical standard: what most honours graduates in English, the main cluster of results, are able to do at FHEQ level 6 (FQHEIS level 10), above the threshold: planning time to meet set deadlines. Cite it as QAA (2023), English Subject Benchmark Statement, para 4.2, standards table, typical column, assessment tasks and time (embedded understanding) row. Do not claim it is the pass requirement or a regulatory standard; the threshold column is the minimum. Set it beside 4.2.b54 and 4.2.b60, qaa/fheq-2024/4.15.b9.1 and Annex D's upper second description qaa/fheq-2024/annex-d/transferable/r3/2.1."
  author-agent-dialogue: "Raise this when a student plans a term with several submissions. With a student, put it plainly in the second person as what most people show by the end of the degree, not the minimum; with staff, frame it as the profile teaching should help most students reach. Ask: 'What does your plan for the next four weeks look like?' Avoid presenting it as the pass mark or reading the table aloud."
- statement: qaa/english-2023/4.2.b58
  forPractitioner: { text: "At the excellent level, the strongest honours graduates in English show creative and independent responses to assessment tasks; treat it as evidence for the top band, not a requirement.", rewrite: light, force: will, status: drafted }
  forBeneficiary: { text: "If you reach the excellent level, you are able to respond creatively and independently to assessment tasks.", rewrite: full, force: will, status: drafted }
  author-agent-written: "Describe this as an excellent standard: what the strongest honours graduates in English are able to do at FHEQ level 6 (FQHEIS level 10), well above the threshold: creative, independent response to assessment. Cite it as QAA (2023), English Subject Benchmark Statement, para 4.2, standards table, excellent column, assessment tasks and time (embedded understanding) row. Do not claim every graduate shows it or that it sets a pass requirement. Set it beside 4.2.b55 and 4.2.b27, qaa/fheq-2024/4.15.b9.2 and Annex D's first-class description qaa/fheq-2024/annex-d/transferable/r4/1st."
  author-agent-dialogue: "Raise this when a student wants to take a risk with an assignment. With a student, put it plainly as a mark of the best work, something to stretch towards rather than a requirement; with staff, frame it as evidence for the top band. Ask: 'What would a bolder answer to this task look like?' Avoid presenting it as the minimum or as a checklist every student must complete."
- statement: qaa/english-2023/4.2.b59
  forPractitioner: { text: "At the excellent level, the strongest honours graduates in English show a proactive approach to asking for help when needed; treat it as evidence for the top band, not a requirement.", rewrite: light, force: will, status: drafted }
  forBeneficiary: { text: "If you reach the excellent level, you are able to ask for help proactively when you need it.", rewrite: full, force: will, status: drafted }
  author-agent-written: "Describe this as an excellent standard: what the strongest honours graduates in English are able to do at FHEQ level 6 (FQHEIS level 10), well above the threshold: proactive help-seeking. Cite it as QAA (2023), English Subject Benchmark Statement, para 4.2, standards table, excellent column, assessment tasks and time (embedded understanding) row. Do not claim every graduate shows it or that it sets a pass requirement. Set it beside 4.2.b56 and 4.2.b76, qaa/fheq-2024/4.15.b5 and Annex D's first-class description qaa/fheq-2024/annex-d/transferable/r3/1st."
  author-agent-dialogue: "Raise this when a strong student hesitates to use support. With a student, put it plainly as a mark of the best work, something to stretch towards rather than a requirement; with staff, frame it as evidence for the top band. Ask: 'Which kind of help would most improve your best work?' Avoid presenting it as the minimum or as a checklist every student must complete."
- statement: qaa/english-2023/4.2.b60
  forPractitioner: { text: "At the excellent level, the strongest honours graduates in English show efficient management of time, balancing competing demands to meet deadlines and leaving room to revise and proofread before submission; treat it as evidence for the top band, not a requirement.", rewrite: light, force: will, status: drafted }
  forBeneficiary: { text: "If you reach the excellent level, you are able to manage your time well, balancing competing demands to meet deadlines and leaving room to revise and proofread before you submit.", rewrite: full, force: will, status: drafted }
  author-agent-written: "Describe this as an excellent standard: what the strongest honours graduates in English are able to do at FHEQ level 6 (FQHEIS level 10), well above the threshold: efficient time management with time to revise. Cite it as QAA (2023), English Subject Benchmark Statement, para 4.2, standards table, excellent column, assessment tasks and time (embedded understanding) row. Do not claim every graduate shows it or that it sets a pass requirement. Set it beside 4.2.b57 and 4.2.b9, qaa/fheq-2024/4.15.b9.1 and Annex D's first-class description qaa/fheq-2024/annex-d/transferable/r3/1st."
  author-agent-dialogue: "Raise this when a student finishes work the night before. With a student, put it plainly as a mark of the best work, something to stretch towards rather than a requirement; with staff, frame it as evidence for the top band. Ask: 'When would you need to finish a draft to leave a day for proofreading?' Avoid presenting it as the minimum or as a checklist every student must complete."
- statement: qaa/english-2023/4.2.b61
  forPractitioner: { text: "At threshold, every honours graduate in English will have shown awareness that many perspectives exist, past and present, local and global, and recognition that listening to other views matters, whether in class or in texts; check that each passing student can evidence it.", rewrite: light, force: threshold, status: drafted }
  forBeneficiary: { text: "As a minimum for your honours degree, you will know that many perspectives exist, past and present, local and global, and see why listening to other views matters, in class and in what you read.", rewrite: full, force: threshold, status: drafted }
  author-agent-written: "Describe this as a threshold standard, the least an honours graduate in English will have shown at FHEQ level 6 (FQHEIS level 10): awareness of multiple perspectives and the value of listening. Cite it as QAA (2023), English Subject Benchmark Statement, para 4.2, standards table, threshold column, perspectives (embedded understanding) row. Do not present it as a regulatory requirement or as where most students end up, since 4.2 expects most to perform well above it. Set it beside 4.2.b62 and 1.8, qaa/fheq-2024/4.15.b4, qaa/fqheis-2024/4.16.b4 and spine:6."
  author-agent-dialogue: "Raise this when a discussion touches on cultural difference or contested history. With a student, say plainly in the second person that this is the floor for the honours degree, not the goal; with staff, frame it as what every passing student has to be able to evidence. Ask: 'Whose perspective is missing from this text or this discussion?' Avoid reading the table aloud or treating this minimum as the target."
- statement: qaa/english-2023/4.2.b62
  forPractitioner: { text: "At the typical level, most honours graduates in English show a willingness to listen to other perspectives, including ones they may disagree with; design teaching so that the main cluster of students reaches it.", rewrite: light, force: will, status: drafted }
  forBeneficiary: { text: "At the level most students reach by the end of the degree, you are able to listen to other perspectives, including ones you disagree with.", rewrite: full, force: will, status: drafted }
  author-agent-written: "Describe this as a typical standard: what most honours graduates in English, the main cluster of results, are able to do at FHEQ level 6 (FQHEIS level 10), above the threshold: listening to views one disagrees with. Cite it as QAA (2023), English Subject Benchmark Statement, para 4.2, standards table, typical column, perspectives (embedded understanding) row. Do not claim it is the pass requirement or a regulatory standard; the threshold column is the minimum. Set it beside 4.2.b61 and 4.2.b64, qaa/fheq-2024/4.15.b7 and Annex D's upper second description qaa/fheq-2024/annex-d/cognitive/r1/2.1."
  author-agent-dialogue: "Raise this when a student dismisses a view without hearing it. With a student, put it plainly in the second person as what most people show by the end of the degree, not the minimum; with staff, frame it as the profile teaching should help most students reach. Ask: 'Can you put the opposing view in a way its holder would accept?' Avoid presenting it as the pass mark or reading the table aloud."
- statement: qaa/english-2023/4.2.b63
  forPractitioner: { text: "At the typical level, most honours graduates in English show the capacity to state those other perspectives fairly and to place their own views within a range of positions; design teaching so that the main cluster of students reaches it.", rewrite: light, force: will, status: drafted }
  forBeneficiary: { text: "At the level most students reach by the end of the degree, you are able to state other people's perspectives fairly and place your own views within the range of positions.", rewrite: full, force: will, status: drafted }
  author-agent-written: "Describe this as a typical standard: what most honours graduates in English, the main cluster of results, are able to do at FHEQ level 6 (FQHEIS level 10), above the threshold: stating views fairly and placing one's own among them. Cite it as QAA (2023), English Subject Benchmark Statement, para 4.2, standards table, typical column, perspectives (embedded understanding) row. Do not claim it is the pass requirement or a regulatory standard; the threshold column is the minimum. Set it beside 4.2.b65 and 4.2.b4, qaa/fheq-2024/4.15.b7 and Annex D's upper second description qaa/fheq-2024/annex-d/cognitive/r1/2.1."
  author-agent-dialogue: "Raise this when a student writes an argument on a contested question. With a student, put it plainly in the second person as what most people show by the end of the degree, not the minimum; with staff, frame it as the profile teaching should help most students reach. Ask: 'Where does your view sit among the others you have described?' Avoid presenting it as the pass mark or reading the table aloud."
- statement: qaa/english-2023/4.2.b64
  forPractitioner: { text: "At the excellent level, the strongest honours graduates in English show sensitivity to cultural contexts and to shared and differing backgrounds when working with others; treat it as evidence for the top band, not a requirement.", rewrite: light, force: will, status: drafted }
  forBeneficiary: { text: "If you reach the excellent level, you are able to be sensitive to cultural contexts and to the backgrounds you share or do not share with others when you work together.", rewrite: full, force: will, status: drafted }
  author-agent-written: "Describe this as an excellent standard: what the strongest honours graduates in English are able to do at FHEQ level 6 (FQHEIS level 10), well above the threshold: cultural sensitivity in working with others. Cite it as QAA (2023), English Subject Benchmark Statement, para 4.2, standards table, excellent column, perspectives (embedded understanding) row. Do not claim every graduate shows it or that it sets a pass requirement. Set it beside 4.2.b62 and 4.2.b23, qaa/fheq-2024/4.15.b9.1 and Annex D's first-class description qaa/fheq-2024/annex-d/transferable/r2/1st."
  author-agent-dialogue: "Raise this when a mixed group works together on a project. With a student, put it plainly as a mark of the best work, something to stretch towards rather than a requirement; with staff, frame it as evidence for the top band. Ask: 'What did you need to learn about your groupmates' backgrounds to work well together?' Avoid presenting it as the minimum or as a checklist every student must complete."
- statement: qaa/english-2023/4.2.b65
  forPractitioner: { text: "At the excellent level, the strongest honours graduates in English show the capacity to state other perspectives fairly and place their own views exactly within a range of positions; treat it as evidence for the top band, not a requirement.", rewrite: light, force: will, status: drafted }
  forBeneficiary: { text: "If you reach the excellent level, you are able to state other people's perspectives fairly and place your own views exactly within the range of positions.", rewrite: full, force: will, status: drafted }
  author-agent-written: "Describe this as an excellent standard: what the strongest honours graduates in English are able to do at FHEQ level 6 (FQHEIS level 10), well above the threshold: placing one's own views precisely among others. Cite it as QAA (2023), English Subject Benchmark Statement, para 4.2, standards table, excellent column, perspectives (embedded understanding) row. Do not claim every graduate shows it or that it sets a pass requirement. Set it beside 4.2.b63 and 4.2.b7, qaa/fheq-2024/4.15.b7 and Annex D's first-class description qaa/fheq-2024/annex-d/cognitive/r1/1st."
  author-agent-dialogue: "Raise this when a student refines a nuanced argument. With a student, put it plainly as a mark of the best work, something to stretch towards rather than a requirement; with staff, frame it as evidence for the top band. Ask: 'Exactly how does your position differ from the nearest one to it?' Avoid presenting it as the minimum or as a checklist every student must complete."
- statement: qaa/english-2023/4.2.b66
  forPractitioner: { text: "At threshold, every honours graduate in English will have shown awareness that academic integrity and ethical care are needed when using other people's writing and research, including large language models as writing aids, though their references may sometimes be inaccurate; check that each passing student can evidence it.", rewrite: light, force: threshold, status: drafted }
  forBeneficiary: { text: "As a minimum for your honours degree, you will know that you must act with academic integrity and ethical care when using other people's writing and research, including AI language tools, even if your references are sometimes inaccurate.", rewrite: full, force: threshold, status: drafted }
  author-agent-written: "Describe this as a threshold standard, the least an honours graduate in English will have shown at FHEQ level 6 (FQHEIS level 10): awareness of academic integrity, including use of large language models. Cite it as QAA (2023), English Subject Benchmark Statement, para 4.2, standards table, threshold column, integrity and citation (embedded understanding) row. Do not present it as a regulatory requirement or as where most students end up, since 4.2 expects most to perform well above it. Set it beside 4.2.b67 and 4.2.b68, qaa/fheq-2024/4.15.b5, qaa/fqheis-2024/4.16.b5 and spine:6."
  author-agent-dialogue: "Raise this when a student asks whether they may use an AI writing tool. With a student, say plainly in the second person that this is the floor for the honours degree, not the goal; with staff, frame it as what every passing student has to be able to evidence. Ask: 'How would you show a reader which parts of this work came from you and which from a tool or a source?' Avoid reading the table aloud or treating this minimum as the target."
- statement: qaa/english-2023/4.2.b67
  forPractitioner: { text: "At the typical level, most honours graduates in English show academic integrity and ethical responsibility in using others' writing and research, large language models used as writing aids included; design teaching so that the main cluster of students reaches it.", rewrite: light, force: will, status: drafted }
  forBeneficiary: { text: "At the level most students reach by the end of the degree, you are able to act with academic integrity and ethical responsibility when using other people's writing and research, including AI language tools that help you write.", rewrite: full, force: will, status: drafted }
  author-agent-written: "Describe this as a typical standard: what most honours graduates in English, the main cluster of results, are able to do at FHEQ level 6 (FQHEIS level 10), above the threshold: academic integrity, including use of large language models. Cite it as QAA (2023), English Subject Benchmark Statement, para 4.2, standards table, typical column, integrity and citation (embedded understanding) row. Do not claim it is the pass requirement or a regulatory standard; the threshold column is the minimum. Set it beside 4.2.b66 and 4.2.b69, qaa/fheq-2024/4.15.b5 and Annex D's upper second description qaa/fheq-2024/annex-d/transferable/r4/2.1."
  author-agent-dialogue: "Raise this when a student uses AI tools in drafting. With a student, put it plainly in the second person as what most people show by the end of the degree, not the minimum; with staff, frame it as the profile teaching should help most students reach. Ask: 'What would you write in a note explaining how you used an AI tool on this essay?' Avoid presenting it as the pass mark or reading the table aloud."
- statement: qaa/english-2023/4.2.b68
  forPractitioner: { text: "At the typical level, most honours graduates in English show clear and complete bibliographies and accurate citation of others' work; design teaching so that the main cluster of students reaches it.", rewrite: light, force: will, status: drafted }
  forBeneficiary: { text: "At the level most students reach by the end of the degree, you are able to give clear, complete bibliographies and cite other people's work accurately.", rewrite: full, force: will, status: drafted }
  author-agent-written: "Describe this as a typical standard: what most honours graduates in English, the main cluster of results, are able to do at FHEQ level 6 (FQHEIS level 10), above the threshold: clear bibliographies and accurate citation. Cite it as QAA (2023), English Subject Benchmark Statement, para 4.2, standards table, typical column, integrity and citation (embedded understanding) row. Do not claim it is the pass requirement or a regulatory standard; the threshold column is the minimum. Set it beside 4.2.b70 and 1.6.b8, qaa/fheq-2024/4.15.b5 and Annex D's upper second description qaa/fheq-2024/annex-d/practical/r2/2.1."
  author-agent-dialogue: "Raise this when a student loses marks on referencing. With a student, put it plainly in the second person as what most people show by the end of the degree, not the minimum; with staff, frame it as the profile teaching should help most students reach. Ask: 'Could a reader find every source you cite from your bibliography alone?' Avoid presenting it as the pass mark or reading the table aloud."
- statement: qaa/english-2023/4.2.b69
  forPractitioner: { text: "At the excellent level, the strongest honours graduates in English show academic integrity and ethical responsibility in using others' writing and research, large language models used as writing aids included (the same wording as the typical item); treat it as evidence for the top band, not a requirement.", rewrite: light, force: will, status: drafted }
  forBeneficiary: { text: "If you reach the excellent level, you are able to act with academic integrity and ethical responsibility when using other people's writing and research, including AI language tools that help you write.", rewrite: full, force: will, status: drafted }
  author-agent-written: "Describe this as an excellent standard: what the strongest honours graduates in English are able to do at FHEQ level 6 (FQHEIS level 10), well above the threshold: academic integrity at the excellent level, including large language models. Cite it as QAA (2023), English Subject Benchmark Statement, para 4.2, standards table, excellent column, integrity and citation (embedded understanding) row. Do not claim every graduate shows it or that it sets a pass requirement. Set it beside 4.2.b67 and 4.2.b70, qaa/fheq-2024/4.15.b5 and Annex D's first-class description qaa/fheq-2024/annex-d/transferable/r4/1st."
  author-agent-dialogue: "Raise this when a strong student weighs the ethics of AI in research. With a student, put it plainly as a mark of the best work, something to stretch towards rather than a requirement; with staff, frame it as evidence for the top band. Ask: 'Where would using a language model help your research, and where would it weaken your integrity?' Avoid presenting it as the minimum or as a checklist every student must complete."
- statement: qaa/english-2023/4.2.b70
  forPractitioner: { text: "At the excellent level, the strongest honours graduates in English show clear, complete bibliographies with consistent, accurate citation and referencing from start to finish; treat it as evidence for the top band, not a requirement.", rewrite: light, force: will, status: drafted }
  forBeneficiary: { text: "If you reach the excellent level, you are able to build clear, complete bibliographies and cite and reference consistently and accurately throughout.", rewrite: full, force: will, status: drafted }
  author-agent-written: "Describe this as an excellent standard: what the strongest honours graduates in English are able to do at FHEQ level 6 (FQHEIS level 10), well above the threshold: consistent, accurate referencing throughout. Cite it as QAA (2023), English Subject Benchmark Statement, para 4.2, standards table, excellent column, integrity and citation (embedded understanding) row. Do not claim every graduate shows it or that it sets a pass requirement. Set it beside 4.2.b68 and 4.2.b9, qaa/fheq-2024/4.15.b5 and Annex D's first-class description qaa/fheq-2024/annex-d/practical/r2/1st."
  author-agent-dialogue: "Raise this when a student prepares a dissertation for submission. With a student, put it plainly as a mark of the best work, something to stretch towards rather than a requirement; with staff, frame it as evidence for the top band. Ask: 'Is every reference in the same style and checked against its source?' Avoid presenting it as the minimum or as a checklist every student must complete."
- statement: qaa/english-2023/4.2.b71
  forPractitioner: { text: "At threshold, every honours graduate in English will have shown awareness that attending to feedback from staff or peers pays off, though they may need prompting to act on it; check that each passing student can evidence it.", rewrite: light, force: threshold, status: drafted }
  forBeneficiary: { text: "As a minimum for your honours degree, you will see the value of paying attention to feedback from staff or classmates, even if you sometimes need a nudge to act on it.", rewrite: full, force: threshold, status: drafted }
  author-agent-written: "Describe this as a threshold standard, the least an honours graduate in English will have shown at FHEQ level 6 (FQHEIS level 10): seeing the value of feedback. Cite it as QAA (2023), English Subject Benchmark Statement, para 4.2, standards table, threshold column, feedback (embedded understanding) row. Do not present it as a regulatory requirement or as where most students end up, since 4.2 expects most to perform well above it. Set it beside 4.2.b73 and 4.2.b75, qaa/fheq-2024/4.15.b9.3, qaa/fqheis-2024/4.16.b9.3 and spine:6."
  author-agent-dialogue: "Raise this when a student has not read their feedback. With a student, say plainly in the second person that this is the floor for the honours degree, not the goal; with staff, frame it as what every passing student has to be able to evidence. Ask: 'What was the main point in your last feedback, and what have you done with it?' Avoid reading the table aloud or treating this minimum as the target."
- statement: qaa/english-2023/4.2.b72
  forPractitioner: { text: "At threshold, every honours graduate in English will have shown a possible need for structure before they can give feedback to peers; check that each passing student can evidence it.", rewrite: light, force: threshold, status: drafted }
  forBeneficiary: { text: "As a minimum for your honours degree, you will may need some structure to help you give feedback to your classmates.", rewrite: full, force: threshold, status: drafted }
  author-agent-written: "Describe this as a threshold standard, the least an honours graduate in English will have shown at FHEQ level 6 (FQHEIS level 10): needing structure to give peer feedback. Cite it as QAA (2023), English Subject Benchmark Statement, para 4.2, standards table, threshold column, feedback (embedded understanding) row. Do not present it as a regulatory requirement or as where most students end up, since 4.2 expects most to perform well above it. Set it beside 4.2.b74 and 4.2.b71, qaa/fheq-2024/4.15.b8, qaa/fqheis-2024/4.16.b8 and spine:6."
  author-agent-dialogue: "Raise this when a workshop asks students to comment on each other's drafts. With a student, say plainly in the second person that this is the floor for the honours degree, not the goal; with staff, frame it as what every passing student has to be able to evidence. Ask: 'What one question could you ask about a classmate's draft that would help them most?' Avoid reading the table aloud or treating this minimum as the target."
- statement: qaa/english-2023/4.2.b73
  forPractitioner: { text: "At the typical level, most honours graduates in English show attention to feedback from staff and peers (the issuer adds that weaker students may need prompting and stronger ones tend to seek it out); design teaching so that the main cluster of students reaches it.", rewrite: light, force: will, status: drafted }
  forBeneficiary: { text: "At the level most students reach by the end of the degree, you are able to pay attention to feedback from staff and classmates, and seek it out where you can.", rewrite: full, force: will, status: drafted }
  author-agent-written: "Describe this as a typical standard: what most honours graduates in English, the main cluster of results, are able to do at FHEQ level 6 (FQHEIS level 10), above the threshold: attending to feedback from staff and peers. Cite it as QAA (2023), English Subject Benchmark Statement, para 4.2, standards table, typical column, feedback (embedded understanding) row. Do not claim it is the pass requirement or a regulatory standard; the threshold column is the minimum. Set it beside 4.2.b71 and 4.2.b75, qaa/fheq-2024/4.15.b9.3 and Annex D's upper second description qaa/fheq-2024/annex-d/transferable/r5/2.1."
  author-agent-dialogue: "Raise this when a student wants to improve between assignments. With a student, put it plainly in the second person as what most people show by the end of the degree, not the minimum; with staff, frame it as the profile teaching should help most students reach. Ask: 'Which piece of feedback have you acted on most, and what changed?' Avoid presenting it as the pass mark or reading the table aloud."
- statement: qaa/english-2023/4.2.b74
  forPractitioner: { text: "At the typical level, most honours graduates in English show constructive and supportive suggestions for their peers; design teaching so that the main cluster of students reaches it.", rewrite: light, force: will, status: drafted }
  forBeneficiary: { text: "At the level most students reach by the end of the degree, you are able to give your classmates constructive and supportive suggestions.", rewrite: full, force: will, status: drafted }
  author-agent-written: "Describe this as a typical standard: what most honours graduates in English, the main cluster of results, are able to do at FHEQ level 6 (FQHEIS level 10), above the threshold: constructive suggestions to peers. Cite it as QAA (2023), English Subject Benchmark Statement, para 4.2, standards table, typical column, feedback (embedded understanding) row. Do not claim it is the pass requirement or a regulatory standard; the threshold column is the minimum. Set it beside 4.2.b72 and 4.2.b22, qaa/fheq-2024/4.15.b8 and Annex D's upper second description qaa/fheq-2024/annex-d/transferable/r2/2.1."
  author-agent-dialogue: "Raise this when a student takes part in peer review. With a student, put it plainly in the second person as what most people show by the end of the degree, not the minimum; with staff, frame it as the profile teaching should help most students reach. Ask: 'How could you phrase that criticism so it helps the writer revise?' Avoid presenting it as the pass mark or reading the table aloud."
- statement: qaa/english-2023/4.2.b75
  forPractitioner: { text: "At the excellent level, the strongest honours graduates in English show close and steady engagement with feedback from staff and peers, using it to reflect on their own practice and assumptions; treat it as evidence for the top band, not a requirement.", rewrite: light, force: will, status: drafted }
  forBeneficiary: { text: "If you reach the excellent level, you are able to engage closely and steadily with feedback from staff and classmates, and use it to reflect on your own practice and assumptions.", rewrite: full, force: will, status: drafted }
  author-agent-written: "Describe this as an excellent standard: what the strongest honours graduates in English are able to do at FHEQ level 6 (FQHEIS level 10), well above the threshold: close, consistent use of feedback to reflect. Cite it as QAA (2023), English Subject Benchmark Statement, para 4.2, standards table, excellent column, feedback (embedded understanding) row. Do not claim every graduate shows it or that it sets a pass requirement. Set it beside 4.2.b73 and 4.2.b76, qaa/fheq-2024/4.15.b9.3 and Annex D's first-class description qaa/fheq-2024/annex-d/transferable/r5/1st."
  author-agent-dialogue: "Raise this when a strong student wants to keep improving. With a student, put it plainly as a mark of the best work, something to stretch towards rather than a requirement; with staff, frame it as evidence for the top band. Ask: 'What assumption of yours did your last feedback challenge?' Avoid presenting it as the minimum or as a checklist every student must complete."
- statement: qaa/english-2023/4.2.b76
  forPractitioner: { text: "At the excellent level, the strongest honours graduates in English show active seeking of feedback and its use to improve their written and spoken communication; treat it as evidence for the top band, not a requirement.", rewrite: light, force: will, status: drafted }
  forBeneficiary: { text: "If you reach the excellent level, you are able to actively seek feedback and use it to improve your written and spoken communication.", rewrite: full, force: will, status: drafted }
  author-agent-written: "Describe this as an excellent standard: what the strongest honours graduates in English are able to do at FHEQ level 6 (FQHEIS level 10), well above the threshold: seeking feedback to improve communication. Cite it as QAA (2023), English Subject Benchmark Statement, para 4.2, standards table, excellent column, feedback (embedded understanding) row. Do not claim every graduate shows it or that it sets a pass requirement. Set it beside 4.2.b75 and 4.2.b59, qaa/fheq-2024/4.15.b9.3 and Annex D's first-class description qaa/fheq-2024/annex-d/transferable/r3/1st."
  author-agent-dialogue: "Raise this when a student is preparing an important presentation or submission. With a student, put it plainly as a mark of the best work, something to stretch towards rather than a requirement; with staff, frame it as evidence for the top band. Ask: 'Who could you ask for feedback before you submit, and what would you ask them?' Avoid presenting it as the minimum or as a checklist every student must complete."
- statement: qaa/english-2023/4.2.b77
  forPractitioner: { text: "At threshold, every honours graduate in English will have shown an understanding of how to carry communication, collaboration, creativity and critical thinking, with experience of research questions, self-directed study and work alone and with others, into employment and social and commercial entrepreneurship, with the skill to do so effectively; check that each passing student can evidence it.", rewrite: light, force: threshold, status: drafted }
  forBeneficiary: { text: "As a minimum for your honours degree, you will understand how to carry your communication, collaboration, creativity and critical thinking, together with what you learned from research and from working alone and in groups, into jobs and social or commercial ventures.", rewrite: full, force: threshold, status: drafted }
  author-agent-written: "Describe this as a threshold standard, the least an honours graduate in English will have shown at FHEQ level 6 (FQHEIS level 10): transferring core skills to employment and entrepreneurship. Cite it as QAA (2023), English Subject Benchmark Statement, para 4.2, standards table, threshold column, enterprise and values (embedded understanding) row. Do not present it as a regulatory requirement or as where most students end up, since 4.2 expects most to perform well above it. Set it beside 1.18, 1.22 and 4.2.b20, qaa/fheq-2024/4.15.b9.1, qaa/fqheis-2024/4.16.b9.1 and spine:6."
  author-agent-dialogue: "Raise this when a student asks how an English degree leads to work. With a student, say plainly in the second person that this is the floor for the honours degree, not the goal; with staff, frame it as what every passing student has to be able to evidence. Ask: 'Which skill from your degree would you describe first to an employer, and with what example?' Avoid reading the table aloud or treating this minimum as the target."
- statement: qaa/english-2023/4.2.b78
  forPractitioner: { text: "At threshold, every honours graduate in English will have shown the habit of acting with integrity and with an understanding of their own values and those of others; check that each passing student can evidence it.", rewrite: light, force: threshold, status: drafted }
  forBeneficiary: { text: "As a minimum for your honours degree, you will act with integrity and with an understanding of your own values and other people's.", rewrite: full, force: threshold, status: drafted }
  author-agent-written: "Describe this as a threshold standard, the least an honours graduate in English will have shown at FHEQ level 6 (FQHEIS level 10): acting with integrity and an understanding of values. Cite it as QAA (2023), English Subject Benchmark Statement, para 4.2, standards table, threshold column, enterprise and values (embedded understanding) row. Do not present it as a regulatory requirement or as where most students end up, since 4.2 expects most to perform well above it. Set it beside 1.20 and 4.2.b67, qaa/fheq-2024/4.15.b9.2, qaa/fqheis-2024/4.16.b9.2 and spine:6."
  author-agent-dialogue: "Raise this when a student faces an ethical choice in a group or placement. With a student, say plainly in the second person that this is the floor for the honours degree, not the goal; with staff, frame it as what every passing student has to be able to evidence. Ask: 'Which of your values guided that decision, and whose values did it affect?' Avoid reading the table aloud or treating this minimum as the target."
- statement: qaa/english-2023/4.2.b79
  forPractitioner: { text: "At threshold, every honours graduate in English will have shown the capacity to produce creative work and improve it through editing and revision; check that each passing student can evidence it.", rewrite: light, force: threshold, status: drafted }
  forBeneficiary: { text: "As a minimum for your honours degree, you will produce creative work and improve it through editing and revision.", rewrite: full, force: threshold, status: drafted }
  author-agent-written: "Describe this as a threshold standard, the least an honours graduate in English will have shown at FHEQ level 6 (FQHEIS level 10): generating creative work and developing it by revision. Cite it as QAA (2023), English Subject Benchmark Statement, para 4.2, standards table, threshold column, creative writing row. Do not present it as a regulatory requirement or as where most students end up, since 4.2 expects most to perform well above it. Set it beside 4.2.b81 and 3.4, qaa/fheq-2024/4.15.b6, qaa/fqheis-2024/4.16.b6 and spine:6."
  author-agent-dialogue: "Raise this when a creative writing student asks what the minimum is for a portfolio. With a student, say plainly in the second person that this is the floor for the honours degree, not the goal; with staff, frame it as what every passing student has to be able to evidence. Ask: 'Which piece have you taken through more than one draft, and what changed?' Avoid reading the table aloud or treating this minimum as the target."
- statement: qaa/english-2023/4.2.b80
  forPractitioner: { text: "At threshold, every honours graduate in English will have shown awareness of differing audiences and ways of reaching them, and the capacity to read and respond to published and unfinished creative work; check that each passing student can evidence it.", rewrite: light, force: threshold, status: drafted }
  forBeneficiary: { text: "As a minimum for your honours degree, you will know about different audiences and ways of reaching them, and read and comment on both published creative writing and drafts in progress.", rewrite: full, force: threshold, status: drafted }
  author-agent-written: "Describe this as a threshold standard, the least an honours graduate in English will have shown at FHEQ level 6 (FQHEIS level 10): audiences, dissemination and responding to work. Cite it as QAA (2023), English Subject Benchmark Statement, para 4.2, standards table, threshold column, creative writing row. Do not present it as a regulatory requirement or as where most students end up, since 4.2 expects most to perform well above it. Set it beside 4.2.b83 and 3.4, qaa/fheq-2024/4.15.b7, qaa/fqheis-2024/4.16.b7 and spine:6."
  author-agent-dialogue: "Raise this when a student prepares for a writing workshop. With a student, say plainly in the second person that this is the floor for the honours degree, not the goal; with staff, frame it as what every passing student has to be able to evidence. Ask: 'Who is this piece for, and where might it be read or heard?' Avoid reading the table aloud or treating this minimum as the target."
- statement: qaa/english-2023/4.2.b81
  forPractitioner: { text: "At the typical level, most honours graduates in English show the capacity to produce and develop original creative work and research in support of it, understanding writing itself as a kind of research; design teaching so that the main cluster of students reaches it.", rewrite: light, force: will, status: drafted }
  forBeneficiary: { text: "At the level most students reach by the end of the degree, you are able to produce and develop original creative work with research to support it, understanding your writing as a form of research in its own right.", rewrite: full, force: will, status: drafted }
  author-agent-written: "Describe this as a typical standard: what most honours graduates in English, the main cluster of results, are able to do at FHEQ level 6 (FQHEIS level 10), above the threshold: original work supported by research, writing as research. Cite it as QAA (2023), English Subject Benchmark Statement, para 4.2, standards table, typical column, creative writing row. Do not claim it is the pass requirement or a regulatory standard; the threshold column is the minimum. Set it beside 4.2.b79 and 4.2.b84, qaa/fheq-2024/4.15.b6 and Annex D's upper second description qaa/fheq-2024/annex-d/cognitive/r4/2.1."
  author-agent-dialogue: "Raise this when a student plans the research behind a creative project. With a student, put it plainly in the second person as what most people show by the end of the degree, not the minimum; with staff, frame it as the profile teaching should help most students reach. Ask: 'What did you need to find out in order to write this piece?' Avoid presenting it as the pass mark or reading the table aloud."
- statement: qaa/english-2023/4.2.b82
  forPractitioner: { text: "At the typical level, most honours graduates in English show use of what written and spoken language allows, its rules and conventions included, across forms, genres and media, aware of the history and culture of language use and literature, media technologies included; design teaching so that the main cluster of students reaches it.", rewrite: light, force: will, status: drafted }
  forBeneficiary: { text: "At the level most students reach by the end of the degree, you are able to use what written and spoken language allows, its rules and conventions included, across forms, genres and media, aware of the history and culture behind them.", rewrite: full, force: will, status: drafted }
  author-agent-written: "Describe this as a typical standard: what most honours graduates in English, the main cluster of results, are able to do at FHEQ level 6 (FQHEIS level 10), above the threshold: using the rules and possibilities of language across forms and media. Cite it as QAA (2023), English Subject Benchmark Statement, para 4.2, standards table, typical column, creative writing row. Do not claim it is the pass requirement or a regulatory standard; the threshold column is the minimum. Set it beside 4.2.b85 and 2.2.b8, qaa/fheq-2024/4.15.b2 and Annex D's upper second description qaa/fheq-2024/annex-d/practical/r1/2.1."
  author-agent-dialogue: "Raise this when a student moves between page, performance and screen forms. With a student, put it plainly in the second person as what most people show by the end of the degree, not the minimum; with staff, frame it as the profile teaching should help most students reach. Ask: 'Which convention of this form are you keeping, and which are you breaking on purpose?' Avoid presenting it as the pass mark or reading the table aloud."
- statement: qaa/english-2023/4.2.b83
  forPractitioner: { text: "At the typical level, most honours graduates in English show critical and practical reading of and response to published work and work in progress; design teaching so that the main cluster of students reaches it.", rewrite: light, force: will, status: drafted }
  forBeneficiary: { text: "At the level most students reach by the end of the degree, you are able to read published work and drafts in progress and respond to them both critically and practically.", rewrite: full, force: will, status: drafted }
  author-agent-written: "Describe this as a typical standard: what most honours graduates in English, the main cluster of results, are able to do at FHEQ level 6 (FQHEIS level 10), above the threshold: critical and practical response to published and draft work. Cite it as QAA (2023), English Subject Benchmark Statement, para 4.2, standards table, typical column, creative writing row. Do not claim it is the pass requirement or a regulatory standard; the threshold column is the minimum. Set it beside 4.2.b80 and 4.2.b74, qaa/fheq-2024/4.15.b7 and Annex D's upper second description qaa/fheq-2024/annex-d/cognitive/r2/2.1."
  author-agent-dialogue: "Raise this when a student gives workshop feedback. With a student, put it plainly in the second person as what most people show by the end of the degree, not the minimum; with staff, frame it as the profile teaching should help most students reach. Ask: 'What would you suggest the writer try next, and why?' Avoid presenting it as the pass mark or reading the table aloud."
- statement: qaa/english-2023/4.2.b84
  forPractitioner: { text: "At the excellent level, the strongest honours graduates in English show creative integration of all the qualities described with independent enterprise and flair, producing ambitious and strikingly original work; treat it as evidence for the top band, not a requirement.", rewrite: light, force: will, status: drafted }
  forBeneficiary: { text: "If you reach the excellent level, you are able to bring all these qualities together creatively, with independent enterprise and flair, to produce ambitious and strikingly original work.", rewrite: full, force: will, status: drafted }
  author-agent-written: "Describe this as an excellent standard: what the strongest honours graduates in English are able to do at FHEQ level 6 (FQHEIS level 10), well above the threshold: ambitious, markedly original work with enterprise and flair. Cite it as QAA (2023), English Subject Benchmark Statement, para 4.2, standards table, excellent column, creative writing row. Do not claim every graduate shows it or that it sets a pass requirement. Set it beside 4.2.b81 and 4.2.b27, qaa/fheq-2024/4.15.b6 and Annex D's first-class description qaa/fheq-2024/annex-d/cognitive/r4/1st."
  author-agent-dialogue: "Raise this when a student aims for the top band in a creative dissertation. With a student, put it plainly as a mark of the best work, something to stretch towards rather than a requirement; with staff, frame it as evidence for the top band. Ask: 'What in this piece could only you have written?' Avoid presenting it as the minimum or as a checklist every student must complete."
- statement: qaa/english-2023/4.2.b85
  forPractitioner: { text: "At the excellent level, the strongest honours graduates in English show a creative and discerning engagement with what language can express and imagine; treat it as evidence for the top band, not a requirement.", rewrite: light, force: will, status: drafted }
  forBeneficiary: { text: "If you reach the excellent level, you are able to engage creatively and with discernment with what language can express and imagine.", rewrite: full, force: will, status: drafted }
  author-agent-written: "Describe this as an excellent standard: what the strongest honours graduates in English are able to do at FHEQ level 6 (FQHEIS level 10), well above the threshold: discriminating engagement with the powers of language. Cite it as QAA (2023), English Subject Benchmark Statement, para 4.2, standards table, excellent column, creative writing row. Do not claim every graduate shows it or that it sets a pass requirement. Set it beside 4.2.b82 and 1.6.b2, qaa/fheq-2024/4.15.b2 and Annex D's first-class description qaa/fheq-2024/annex-d/practical/r1/1st."
  author-agent-dialogue: "Raise this when a student revises for precision of language. With a student, put it plainly as a mark of the best work, something to stretch towards rather than a requirement; with staff, frame it as evidence for the top band. Ask: 'Which word in this line would you change, and what would the change gain?' Avoid presenting it as the minimum or as a checklist every student must complete."
```

### S5 Levels and alignment
<!-- label: both; status: drafted; basis: primary -->
```yaml
levels:
  - { id: "fheq:6", role: "cites", locator: "D1, 2.4; 4.2 (Annex D for FHEQ Level 6 degrees)" }
  - { id: "fqheis:10", role: "cites", locator: "D1, 2.4; 4.2 (Annex D for FQHEIS Level 10 degrees)" }
crosswalks:
  - { from: "fheq:6", to: "fqheis:10", relation: "equivalent", basis: "stated (D1, 2.4: \"a degree with honours (FHEQ Level 6; FQHEIS Level 10)\"; 4.2 names both for Annex D); matches std:doc:qaa-fheq-2024-framework Table 1 (honours: FHEQ 6, SCQF 10) and the reference framework spine:6" }
```

### S6 Themes
<!-- label: both; status: drafted; basis: primary -->
```yaml
- { id: "theme:edi", role: "carries", carriedIn: ["1.7", "1.8", "1.9", "1.10", "1.11", "3.5", "4.2"] }
- { id: "theme:accessibility", role: "carries", carriedIn: ["1.12", "1.13", "2.7", "3.10", "4.2"] }
- { id: "theme:esd", role: "carries", carriedIn: ["1.14", "1.15", "1.16", "4.2"] }
- { id: "theme:enterprise", role: "carries", carriedIn: ["1.17", "1.18", "1.19", "1.20", "1.21", "1.22", "2.8", "4.2"] }
- { id: "theme:generative-ai", role: "carries", carriedIn: ["4.2"] }
```

### S7 Relations
<!-- label: both; status: drafted; basis: primary -->
```yaml
- { rel: "partOf", target: "collection: QAA Subject Benchmark Statements", note: "one of 54 held by stan" }
- { rel: "supersedes", target: "std:doc:qaa-english-2019-benchmarks (not ingested)", note: "section 6 names the fourth edition (2019), revised from the 2015 third edition; the 2023 advisory group wrote this edition (D1, section 6)" }
- { rel: "refersTo", target: "std:doc:qaa-fheq-2024-framework, Annex D", note: "the four honours classifications, for achievement above threshold (D1, 4.2)" }
- { rel: "refersTo", target: "std:doc:qaa-fheq-2024-framework", note: "FHEQ Level 6 (D1, 2.4, 4.2)" }
- { rel: "refersTo", target: "std:doc:qaa-fqheis-2024-framework", note: "FQHEIS Level 10 (D1, 2.4, 4.2)" }
- { rel: "refersTo", target: "std:doc:qaa-creative-writing-2024-benchmarks", note: "courses with creative writing reference it; the creative writing rows point to it for the full standards (D1, 1.2, 3.4, 4.2); the edition meant in 2023 was the 2019 one (Part E)" }
- { rel: "refersTo", target: "std:doc:qaa-linguistics-2023-benchmarks (not yet ingested)", note: "courses with Linguistics elements are likely to reference it (D1, 1.2)" }
- { rel: "refersTo", target: "std:doc:qaa-advancehe-esd-2021-guidance", note: "listed in section 5, behind the ESD paragraphs (1.14 to 1.16)" }
- { rel: "refersTo", target: "std:doc:qaa-enterprise-2018-guidance", note: "listed in section 5, behind the enterprise paragraphs (1.17 to 1.22)" }
- { rel: "refersTo", target: "QAA Quality Code for Higher Education and its Advice and Guidance (not ingested)", note: "front matter; section 5" }
```

### S8 Currency and review
<!-- label: source; status: drafted; basis: primary -->
```yaml
published: "2023-09"
lastReviewed: "none-stated"
reviewCycle: "none-stated"
consultation: "none-stated"
replacedBy: "none"
```

### S9 Commentary (optional)
<!-- label: editorial; status: drafted; basis: secondary -->
`unknown`: not researched in P1 (Part E).

### SB1 The subject
<!-- label: both; status: drafted; basis: primary -->
- English studies meaning made through communication in English and related languages, across language, literature and creative writing, and is often studied jointly or with neighbouring subjects such as film, media, cultural or translation studies (D1, 1.1, 1.2, 1.4).
- Its distinctive emphasis is discourse and meaning, aesthetics and rhetoric: close and critical reading in context, analysis of written and spoken texts and reflection on reading, writing and interpretation (D1, 1.6).
- It joins critical and creative response, so producing new creative work sits beside interpretation and analysis (D1, 1.4, 1.6, 3.4).
- It values dialogue, debate and difference, and engages with diverse perspectives and with the discipline's own colonial, patriarchal and elitist history (D1, 1.7 to 1.10).
- It builds four core capacities named throughout: communication, collaboration, creativity and critical thinking (D1, 1.4, 1.5, 1.18, 3.10).
- Teaching leans on small groups, independent and collaborative study, flipped lectures, use of libraries, archives and corpora and a capstone project (D1, 3.5 to 3.9).
- Assessment is deliberately diverse, from essays and examinations to digital objects, performance and portfolios (D1, 3.10, 3.11).

### SB2 Themes in this subject
<!-- label: both; status: drafted; basis: primary -->
```yaml
- theme: theme:edi
  inThisSubject: "plural voices and contested narratives, a reckoning with the discipline's colonial, patriarchal and elitist history and with imbalances among students and staff, diversified curricula beyond a core and periphery and graduates attentive to diverse audiences; in the standards, listening to and fairly placing other perspectives and cultural sensitivity in group work (D1, 1.7 to 1.11, 4.2)"
  statements: ["qaa/english-2023/4.2.b61", "qaa/english-2023/4.2.b62", "qaa/english-2023/4.2.b63", "qaa/english-2023/4.2.b64", "qaa/english-2023/4.2.b65", "qaa/english-2023/4.2.b23"]
- theme: theme:accessibility
  inThisSubject: "accessible courses with inclusive methods and assessment, attention to neurodiversity, health conditions, caring, commuting and religious observance, many routes of entry, responsive design and accessible digital resources (D1, 1.12, 1.13, 2.7, 3.10); the standards table names access in its embedded row heading but no single item carries it"
  statements: []
- theme: theme:esd
  inThisSubject: "the study of English contributes to sustainable development through its four core capacities, ecocriticism, world literatures and global varieties of English, the colonial past and resource extraction and global citizenship in a multilingual world (D1, 1.14 to 1.16); in the standards, awareness of perspectives from local to global"
  statements: ["qaa/english-2023/4.2.b61"]
- theme: theme:enterprise
  inThisSubject: "communication, collaboration, creativity and critical thinking framed as enterprise skills, with careers across many sectors, placements and partnerships; in the standards, transferring these skills to work and entrepreneurship and acting with integrity (D1, 1.17 to 1.22, 2.8, 4.2)"
  statements: ["qaa/english-2023/4.2.b77", "qaa/english-2023/4.2.b78", "qaa/english-2023/4.2.b20"]
- theme: theme:generative-ai
  inThisSubject: "large language models appear only under academic integrity: graduates use them as writing aids with integrity and ethical responsibility, the threshold allowing occasional inaccuracy in references (D1, 4.2)"
  statements: ["qaa/english-2023/4.2.b66", "qaa/english-2023/4.2.b67", "qaa/english-2023/4.2.b69"]
```

### SB3 Content and delivery
<!-- label: both; status: drafted; basis: primary -->
```yaml
areas:
  - { component: "3.2", gloss: "English language: spoken, written and multimodal communication, varieties, history, sub-disciplines and methods" }
  - { component: "3.3", gloss: "English literature: prose, poetry and drama across periods, contexts, theory, reception and dissemination" }
  - { component: "3.4", gloss: "creative writing within English: reflective practice, original work, publishing and audiences" }
practices:
  - { component: "2.7", kind: "teaching", gloss: "responsive design, varied assessment and accessible digital resources" }
  - { component: "3.5", kind: "teaching", gloss: "dialogue, instruction, independent and group work, co-creation; online and face to face" }
  - { component: "3.6", kind: "learning", gloss: "guided preparation for classes" }
  - { component: "3.7", kind: "learning", gloss: "independent study before class; flipped lectures" }
  - { component: "3.8", kind: "teaching", gloss: "seminars, tutorials and workshops for dialogue and peer critique" }
  - { component: "3.9", kind: "learning", gloss: "libraries, archives, corpora and a capstone project" }
  - { component: "3.10", kind: "assessment", gloss: "diverse assessment, also for accessibility" }
  - { component: "3.11", kind: "assessment", gloss: "forms of assessment, from essays to digital objects and portfolios" }
  - { component: "3.12", kind: "assessment", gloss: "what assessment rewards, from argument to imaginative communication" }
```

### SB4 Benchmark standards
<!-- label: both; status: drafted; basis: primary -->
```yaml
rungs:
  - { rung: "threshold", leadIn: "4.2", award: "bachelor's with honours", items: 26 }
  - { rung: "typical", leadIn: "4.2", award: "bachelor's with honours", items: 27 }
  - { rung: "excellent", leadIn: "4.2", award: "bachelor's with honours", items: 33 }
rungBases: "4.1: the statement sets the minimum threshold standards a student will have shown at the award of honours; 4.2: most students perform well above it, judged with Annex D. The standards are one table with three columns, each headed by a rung definition (threshold: the minimum that should be reached; typical: the main cluster; excellent: a defining paragraph, recorded as 4.2.ex1) and the lead-in 'are able to'. Rows: generic skills (communication, affective language, digital, collaboration, creativity, critical thinking, evidence); subject knowledge (close reading, interpretation, then a paragraph spanning all three columns, recorded as 4.2.sk1 to sk3 with rung none); embedded understanding of EDI, access, sustainability and entrepreneurship; creative writing, with its own lead-in. Cells hold several bullets each, so the columns hold different numbers of items."
outcomeLists:
  - { leadIn: "1.6", gloss: "what English graduates can do (introduced with can)", items: 8, award: ["bachelor's with honours"] }
  - { leadIn: "2.2", gloss: "what graduates will know about, by the aspects studied", items: 9, award: ["bachelor's with honours"] }
  - { leadIn: "4.2", gloss: "subject knowledge across all three columns, by the elements of the degree (will)", items: 3, award: ["bachelor's with honours"] }
outcomes:
  - { outcome: "communicating arguments to an audience", threshold: "qaa/english-2023/4.2.b1", typical: "qaa/english-2023/4.2.b3", excellent: "qaa/english-2023/4.2.b6", basis: "inferred", domain: "generic-skill", award: "bachelor's with honours" }
  - { outcome: "writing as a process of revision", threshold: "qaa/english-2023/4.2.b2", typical: "qaa/english-2023/4.2.b5", excellent: "qaa/english-2023/4.2.b9", basis: "inferred", domain: "generic-skill", award: "bachelor's with honours" }
  - { outcome: "engaging other writers' arguments", threshold: "none", typical: "qaa/english-2023/4.2.b4", excellent: "qaa/english-2023/4.2.b7", basis: "inferred", domain: "generic-skill", award: "bachelor's with honours" }
  - { outcome: "the affective power of language", threshold: "qaa/english-2023/4.2.b10", typical: "qaa/english-2023/4.2.b12", excellent: "qaa/english-2023/4.2.b13", basis: "inferred", domain: "subject-skill", award: "bachelor's with honours" }
  - { outcome: "digital communication", threshold: "qaa/english-2023/4.2.b15", typical: "qaa/english-2023/4.2.b16", excellent: "qaa/english-2023/4.2.b17", basis: "inferred", domain: "generic-skill", award: "bachelor's with honours" }
  - { outcome: "collaboration and independent work", threshold: "qaa/english-2023/4.2.b18", typical: "qaa/english-2023/4.2.b20", excellent: "qaa/english-2023/4.2.b21", basis: "inferred", domain: "generic-skill", award: "bachelor's with honours" }
  - { outcome: "creative interpretation", threshold: "qaa/english-2023/4.2.b25", typical: "qaa/english-2023/4.2.b26", excellent: "qaa/english-2023/4.2.b27", basis: "inferred", domain: "subject-skill", award: "bachelor's with honours" }
  - { outcome: "critical thinking", threshold: "qaa/english-2023/4.2.b28", typical: "qaa/english-2023/4.2.b33", excellent: "qaa/english-2023/4.2.b38", basis: "inferred", domain: "generic-skill", award: "bachelor's with honours" }
  - { outcome: "critical understanding of complex texts", threshold: "qaa/english-2023/4.2.b29", typical: "qaa/english-2023/4.2.b34", excellent: "qaa/english-2023/4.2.b39", basis: "inferred", domain: "understanding", award: "bachelor's with honours" }
  - { outcome: "reflecting on reading and writing", threshold: "qaa/english-2023/4.2.b30", typical: "qaa/english-2023/4.2.b35", excellent: "qaa/english-2023/4.2.b40", basis: "inferred", domain: "subject-skill", award: "bachelor's with honours" }
  - { outcome: "rigour with data and evidence", threshold: "qaa/english-2023/4.2.b31", typical: "qaa/english-2023/4.2.b36", excellent: "qaa/english-2023/4.2.b42", basis: "inferred", domain: "generic-skill", award: "bachelor's with honours" }
  - { outcome: "debate, disagreement and ambiguity", threshold: "qaa/english-2023/4.2.b32", typical: "qaa/english-2023/4.2.b37", excellent: "qaa/english-2023/4.2.b43", basis: "inferred", domain: "generic-skill", award: "bachelor's with honours" }
  - { outcome: "gathering and analysing evidence", threshold: "qaa/english-2023/4.2.b44", typical: "qaa/english-2023/4.2.b45", excellent: "qaa/english-2023/4.2.b46", basis: "inferred", domain: "generic-skill", award: "bachelor's with honours" }
  - { outcome: "close reading", threshold: "qaa/english-2023/4.2.b47", typical: "qaa/english-2023/4.2.b48", excellent: "qaa/english-2023/4.2.b49", basis: "inferred", domain: "subject-skill", award: "bachelor's with honours" }
  - { outcome: "plurality and evaluation of interpretations", threshold: "qaa/english-2023/4.2.b50", typical: "qaa/english-2023/4.2.b51", excellent: "qaa/english-2023/4.2.b52", basis: "inferred", domain: "understanding", award: "bachelor's with honours" }
  - { outcome: "assessment tasks", threshold: "qaa/english-2023/4.2.b53", typical: "qaa/english-2023/4.2.b55", excellent: "qaa/english-2023/4.2.b58", basis: "inferred", domain: "generic-skill", award: "bachelor's with honours" }
  - { outcome: "time management", threshold: "qaa/english-2023/4.2.b54", typical: "qaa/english-2023/4.2.b57", excellent: "qaa/english-2023/4.2.b60", basis: "inferred", domain: "generic-skill", award: "bachelor's with honours" }
  - { outcome: "seeking help", threshold: "none", typical: "qaa/english-2023/4.2.b56", excellent: "qaa/english-2023/4.2.b59", basis: "inferred", domain: "generic-skill", award: "bachelor's with honours" }
  - { outcome: "listening to other perspectives", threshold: "qaa/english-2023/4.2.b61", typical: "qaa/english-2023/4.2.b62", excellent: "none", basis: "inferred", domain: "generic-skill", award: "bachelor's with honours" }
  - { outcome: "placing own views among others", threshold: "none", typical: "qaa/english-2023/4.2.b63", excellent: "qaa/english-2023/4.2.b65", basis: "inferred", domain: "generic-skill", award: "bachelor's with honours" }
  - { outcome: "academic integrity", threshold: "qaa/english-2023/4.2.b66", typical: "qaa/english-2023/4.2.b67", excellent: "qaa/english-2023/4.2.b69", basis: "inferred", domain: "generic-skill", award: "bachelor's with honours" }
  - { outcome: "bibliographies and citation", threshold: "none", typical: "qaa/english-2023/4.2.b68", excellent: "qaa/english-2023/4.2.b70", basis: "inferred", domain: "generic-skill", award: "bachelor's with honours" }
  - { outcome: "using feedback", threshold: "qaa/english-2023/4.2.b71", typical: "qaa/english-2023/4.2.b73", excellent: "qaa/english-2023/4.2.b75", basis: "inferred", domain: "generic-skill", award: "bachelor's with honours" }
  - { outcome: "peer feedback", threshold: "qaa/english-2023/4.2.b72", typical: "qaa/english-2023/4.2.b74", excellent: "none", basis: "inferred", domain: "generic-skill", award: "bachelor's with honours" }
  - { outcome: "generating and developing creative work", threshold: "qaa/english-2023/4.2.b79", typical: "qaa/english-2023/4.2.b81", excellent: "qaa/english-2023/4.2.b84", basis: "inferred", domain: "subject-skill", award: "bachelor's with honours" }
  - { outcome: "responding to creative work", threshold: "qaa/english-2023/4.2.b80", typical: "qaa/english-2023/4.2.b83", excellent: "none", basis: "inferred", domain: "subject-skill", award: "bachelor's with honours" }
  - { outcome: "language across forms and media", threshold: "none", typical: "qaa/english-2023/4.2.b82", excellent: "qaa/english-2023/4.2.b85", basis: "inferred", domain: "subject-skill", award: "bachelor's with honours" }
```

### SB4a Student and practitioner versions
<!-- label: both; status: drafted; basis: primary -->
```yaml
written: fresh from the held text; no consumer's statements read (benchmark variant rule 6)
fullRewrites: []
```

### SB5 Bodies
<!-- label: source; status: drafted; basis: primary -->
```yaml
- { body: "professional, statutory and regulatory bodies (PSRBs), unnamed", says: "the statement supports them on academic standards, their requirements are a further reference point and courses with vocational outcomes may need their accreditation (D1, front matter, 2.12)", requirements: "not-applicable-by-design: no body named (Part E)" }
- { body: "Office for Students (regulator, England)", says: "under its regulatory framework the statements are not sector-recognised standards in England (D1, front matter)", requirements: "not yet ingested (Part E)" }
```

### SB6 Cross-cutting references
<!-- label: both; status: drafted; basis: primary -->
```yaml
themes:
  - { id: "theme:edi", named: "Equality, diversity and inclusion", carriedIn: ["1.7", "1.8", "1.9", "1.10", "1.11", "3.5", "4.2"], statements: ["4.2.b61", "4.2.b62", "4.2.b63", "4.2.b64", "4.2.b65", "4.2.b23"] }
  - { id: "theme:accessibility", named: "Accessibility (front matter: accessibility and the needs of disabled students; 4.2: access)", carriedIn: ["1.12", "1.13", "2.7", "3.10", "4.2"], statements: [] }
  - { id: "theme:esd", named: "Education for Sustainable Development (4.2: sustainability)", carriedIn: ["1.14", "1.15", "1.16", "4.2"], statements: ["4.2.b61"] }
  - { id: "theme:enterprise", named: "Enterprise and entrepreneurship education (front matter: employability, entrepreneurship and enterprise education)", carriedIn: ["1.17", "1.18", "1.19", "1.20", "1.21", "1.22", "2.8", "4.2"], statements: ["4.2.b77", "4.2.b78", "4.2.b20"] }
  - { id: "theme:generative-ai", named: "large language models (sometimes known as artificial intelligence)", carriedIn: ["4.2"], statements: ["4.2.b66", "4.2.b67", "4.2.b69"] }
frameworks:
  - { framework: "fheq", levels: ["fheq:6"], citedIn: ["2.4", "4.2"] }
  - { framework: "scqf", levels: ["fqheis:10"], citedIn: ["2.4", "4.2"] }
bodies:
  - { body: "PSRBs (unnamed)", citedIn: ["front matter", "2.12"] }
  - { body: "Office for Students (regulator, England)", citedIn: ["front matter"] }
  - { body: "UNESCO (source of the ESD definition)", citedIn: ["1.14"] }
  - { body: "The British Academy (SHAPE)", citedIn: ["1.5", "5"] }
sharedDocuments:
  - { document: "std:doc:qaa-fheq-2024-framework, Annex D", named: "Annex D: Outcome classification descriptions for FHEQ Level 6 and FQHEIS Level 10 degrees", citedIn: ["4.2"], role: "descriptions of the four honours classifications (1st, 2.1, 2.2, 3rd), for achievement above threshold" }
  - { document: "std:doc:qaa-creative-writing-2024-benchmarks", named: "the Creative Writing Subject Benchmark Statement", citedIn: ["1.2", "3.4", "4.2"], role: "reference for courses with creative writing; full creative writing standards" }
  - { document: "std:doc:qaa-linguistics-2023-benchmarks (not yet ingested: Part E)", named: "the Subject Benchmark Statement for Linguistics", citedIn: ["1.2"], role: "reference for courses with linguistics elements" }
  - { document: "std:doc:qaa-advancehe-esd-2021-guidance", named: "QAA and Advance HE (2021) Education for Sustainable Development Guidance", citedIn: ["5"], role: "listed reference behind the ESD paragraphs" }
  - { document: "std:doc:qaa-enterprise-2018-guidance", named: "QAA (2018) Enterprise and Entrepreneurship Education: Guidance for UK Higher Education Providers", citedIn: ["5"], role: "listed reference behind the enterprise paragraphs" }
  - { document: "UNESCO (2019) and the UN Sustainable Development Goals (external, not ingested)", named: "UNESCO, 2019; the UN's Sustainable Development Goals", citedIn: ["1.14"], role: "definition of ESD" }
  - { document: "The British Academy (2020) SHAPE (external, not ingested)", named: "Social Sciences, Humanities and the Arts for People and the Economy/Environment (SHAPE)", citedIn: ["1.5", "2.8", "5"], role: "the family of subjects whose general capabilities English shares" }
  - { document: "QAA Quality Code, Advice and Guidance (not yet ingested)", named: "Advice and Guidance to support the Quality Code for Higher Education; The UK Quality Code for Higher Education", citedIn: ["front matter", "5"], role: "course design, teaching, external expertise, monitoring" }
  - { document: "QAA Glossary (not ingested)", named: "QAA's Glossary", citedIn: ["front matter"], role: "explains unfamiliar terms" }
  - { document: "Quality Enhancement Review (Wales); Quality Enhancement Framework (Scotland) (not ingested)", named: "the same", citedIn: ["front matter"], role: "where the statement is a key reference point" }
```

## Part B Terminology
<!-- The statement has no glossary of its own unless Part E says so; these are terms it defines in its text. -->

### B1 Concepts
<!-- label: both; status: drafted; basis: primary -->
```yaml
- { slug: "threshold-standard", definition: "the minimum a student will have shown to be awarded the honours degree, and the least that should be reached (D1, 4.1, 4.2)", beneficiaryDefinition: "the least you need to have shown by the end of your honours degree", scopeNote: "the threshold column of the 4.2 table", category: "unknown", practices: ["education"] }
- { slug: "typical-standard", definition: "what the typical student in the main cluster of results attains (D1, 4.2)", beneficiaryDefinition: "what most people show by the end of the degree", scopeNote: "the typical column of the 4.2 table", category: "unknown", practices: ["education"] }
- { slug: "excellent-standard", definition: "the capabilities shown at a higher level, with wide independent reading, originality and deep understanding (D1, 4.2)", beneficiaryDefinition: "what the strongest work shows, beyond the typical", scopeNote: "the excellent column of the 4.2 table", category: "unknown", practices: ["education"] }
- { slug: "shape-subjects", definition: "the social sciences, humanities and arts grouped as subjects for people and the economy or environment, whose general capabilities English shares (D1, 1.5)", category: "unknown", practices: ["education"] }
- { slug: "ecocriticism", definition: "criticism that puts the environment at the centre of interpretation (D1, 1.15)", beneficiaryDefinition: "reading texts with the environment as the main focus", category: "unknown", practices: ["education"] }
- { slug: "flipped-approach", definition: "teaching in which students read and form responses before class, which then discusses them (D1, 3.7)", beneficiaryDefinition: "you prepare and form your views before the class, which then builds on them", category: "unknown", practices: ["education"] }
```

### B2a Terms as the issuer defines them
<!-- label: source; status: drafted; basis: primary -->
```yaml
- { concept: "threshold-standard", form: "Threshold Standard", lang: "en", partOfSpeech: "noun-phrase", termStatus: "preferred", register: "formal" }
- { concept: "typical-standard", form: "Typical Standard", lang: "en", partOfSpeech: "noun-phrase", termStatus: "preferred", register: "formal" }
- { concept: "excellent-standard", form: "Excellent Standard", lang: "en", partOfSpeech: "noun-phrase", termStatus: "preferred", register: "formal" }
- { concept: "shape-subjects", form: "SHAPE subjects", lang: "en", partOfSpeech: "noun-phrase", termStatus: "preferred", register: "formal" }
- { concept: "ecocriticism", form: "Ecocriticism", lang: "en", partOfSpeech: "noun", termStatus: "preferred", register: "discipline-specific" }
- { concept: "flipped-approach", form: "'flipped' approach", lang: "en", partOfSpeech: "noun-phrase", termStatus: "preferred", register: "discipline-specific" }
```

### B2b Associated vocabulary
`not-applicable-by-design`: the statement names no wider vocabulary.

### B3 Framework blocks
`not-applicable-by-design`: no term is defined its own way for one component.

### B4 Relations
`not-applicable-by-design`: no relations between the terms are stated.

## Part C Process
<!-- label: both; status: drafted; basis: primary -->

### C0 Formality
`not-applicable`: the statement sets out what graduates achieve and what courses provide, not a procedure.

## Part D Sources
```yaml
- key: D1
  issuer: The Quality Assurance Agency for Higher Education
  title: "Subject Benchmark Statement English"
  edition: "September 2023"
  year: 2023
  url: unknown (the QAA page; the text came by stan's extraction)
  retrieved: "held from stan: wkspc2615-QAAVector mapped/english-2023/english-2023.raw.txt, commit 366bcb99a01118f2c4c3ebfa2a8337596bddc455; received 2026-10-03"
  licence: QAA copyright
  tier: primary
  readVia: direct
  held: bff45417af9dda9c64109d5fa641127af39048acb90332de6fd077a6ce6edea9
  heldFiles: ["wkspc2601-library/txt/qaa-2023-english-subject-benchmark-statement-standard.txt", "wkspc2601-library/txt/qaa-2023-english-subject-benchmark-statement-standard.norm.txt", "wkspc2601-library/records/qaa-2023-english-subject-benchmark-statement-standard.chunks.json", "wkspc2601-library/records/qaa-2023-english-subject-benchmark-statement-standard.held.json"]
  citedIn: [S1, S2, S3, S4, S4a, S5, S6, S7, SB1, SB2, SB3, SB4, SB5, SB6]
```

### D2 Research log
```yaml
- { ref: D1, tier: primary, consulted: 2026-10-03, pass: P1, outcome: "read whole, direct, from the normalised text; skeleton by tools/std_prep.py, document by tools/bm_build.py" }
- { ref: "ADAPT subj HESA stores, cah.json and hecos.json (designs/ingest/standards/subj/vocab)", tier: primary, consulted: 2026-10-03, pass: P1, outcome: "codes for statedSubjects and subjects" }
```

### D3 Wanted sources
```yaml
[]
```

## Part E Gaps and questions
- SB4, rung shape: one table under 4.2 with three columns (Threshold Standard, Typical Standard, Excellent Standard), its header repeated on each page; the held text linearises it cell by cell, threshold cell then typical cell then excellent cell for each row, with no column marks. Each bullet (skeleton 4.2.b1 to b85) is assigned to its column by reading the row: threshold 26, typical 27, excellent 32 items plus the excellent rung's defining paragraph (4.2.ex1), so 33. The skeleton's rung counts (85 threshold) were wrong. For P3: the column of each bullet is our reading, not marked in the held text.
- SB4, rows with uncertain column breaks, for P3: communication (b1 to b2 threshold, b3 to b5 typical, b6 to b9 excellent); affective language (b10 and b11 threshold, b12 typical, b13 and b14 excellent); collaboration (b18 and b19 threshold, b20 typical, b21 to b24 excellent); assessment tasks (b53 and b54, b55 to b57, b58 to b60); perspectives (b61, b62 and b63, b64 and b65); feedback (b71 and b72, b73 and b74, b75 and b76).
- SB4, enterprise and values row (4.2.b77, b78): only two bullets, with no second or third cell in the held text. Read as the threshold cell; the cell may span all three columns in the original layout. Wanted: the PDF page for this row.
- S4, 4.2.b8 ends at a page break ('in light of new evidence and'); the rest of the item ('claims, appropriate to the intended audience') follows the repeated table header on the next page. The span keeps the skeleton's cut so `source` holds no header text; the paraphrase covers the whole item.
- S4, skeleton corrections by `find`: 4.2.b52, whose skeleton span ran on through the subject knowledge paragraph, is cut at the end of its bullet; the paragraph is recorded as 4.2.sk1 (with its two opening sentences and the language elements), 4.2.sk2 (literature elements) and 4.2.sk3 (creative writing elements), rung none, force will. 4.2.b85 is cut before 'For a full expression of Creative Writing benchmark standards, please consult the Creative Writing Benchmark Statement' (a pointer, not a standard). 2.4, 2.5, 2.10 and 4.2 are cut as their obliging sentences; 3.3.s1 is our id for 3.3's first sentence.
- S4, ids: 4.2.ex1, 4.2.sk1 to sk3 and 3.3.s1 are ours, not the issuer's numbering; the builder sorts them after the numbered records.
- S4, force: threshold cells take `threshold` from the column definition ('the minimum requirement that should be reached', given by `forceFrom`) and from 4.1; typical and excellent cells take `will` from their lead-ins ('are able to'), by `forceFrom`; 4.2.ex1 (plain present 'demonstrate') takes `will` from 4.1 by `forceFrom`. For Abbott at P3: the threshold definition also carries 'requirement' and 'should'.
- S4, 1.6: an outcome list introduced with 'can' ('English graduates can:'), recorded as 8 outcome items with force `will` (the builder reads 'can' with 'able to' as will). For Abbott: keep as will, or describes? The list echoes the standards table and 3.12.
- S4, 2.2: an outcome list in 'will know about', qualified by 'depending on the aspects of the subject they have studied'; recorded as 9 knowledge outcomes at fheq:6 (level from 2.4). 2.3's 'paragraphs 3.2-3.4' is a reference (DPN-1), not cut.
- S4, 2.4: recorded as its first three sentences (will progress; builds towards the threshold; will usually include credit). Its fourth sentence ('it would be expected ... would be capable of') is outside the five words and not taken; its fifth ('may require', of postgraduate entry) is hedged and not taken.
- S4, not taken as statements (D-std-0002 (a)): 1.5 (capacities the subject develops, plain present); 1.11 and 1.21 (graduates and students described in plain present); 2.11 ('will be asked', 'will consider': a description of the external examiner system, hedged by 'typically'); 2.12 ('may also require' accreditation: hedged); 3.5 ('there will usually be' a mix of online modes); 3.7 ('will very often take a flipped approach', 'will then be encouraged': descriptive); 4.1 (the definition of the threshold, used as `forceFrom`); the typical column's definition ('the level of attainment reached by the typical student').
- S4, plain-present provider norms not recorded as statements (template open point 5): 1.12 ('English courses are designed to be highly accessible'; staff 'reflect current legislation'); 2.7 (programmes 'make use of' inclusive methods, with four examples); 2.9 (review processes); 3.6 (preparation 'is clearly structured'); 3.11 and 3.12 (forms of assessment; what assessment 'rewards').
- S4, obliging words outside the five: 'requirement' (the threshold definition, recorded as the threshold force) and 'necessity' (4.2.b54, b66: what students understand or are aware of, not an obligation on them) recorded with their cells' force, not as must.
- S4, domain: our reading. The issuer heads the first rows 'Generic skills', but the affective-language row (b10 to b14), the creativity row (b25 to b27) and the reflection and evaluation items (b30, b35, b40, b41) concern the subject's own texts and methods and are recorded as subject-skill; b29, b34, b39 (critical understanding of texts and their history) and the interpretation row (b50 to b52) as understanding. The embedded understanding rows are generic-skill.
- S4, gradeOf: 48 links, all inferred (the issuer pairs nothing; a row only groups cells): within each traced outcome in SB4, typical to threshold and excellent to typical, plus 4.2.b22 to b20 (teamwork) and 4.2.b41 to b35 (evaluating forms). Less plain, for P3: b21 to b20 (b21 repeats the threshold wording b18 at the excellent rung), b55 to b53 (adapting to tasks against carrying out tasks), b58 to b55, b13 to b12.
- S4, repeated wording across rungs: b18 and b21 (collaboration), b31, b36 and b42 (rigour with evidence), b67 and b69 (integrity) are word for word the same in two or three columns; the rung is given by the column alone.
- S4, verbs: 2.2's items are noun phrases with no action verb, so `verbs` is empty. 4.2.b46 has the issuer's 'analyses' (sic) and b85 'deploy'; verbs are recorded as spelled.
- S3: sub-headings fall at the end of the paragraph before them in the held text (for example 'Equality, diversity and inclusion' closes 1.7, 'Purposes and characteristics of an English Degree' closes 1.3), so the skeleton's components 1.3, 1.7, 1.11, 1.13 and 1.16 carry a following heading. Sub-heading ranges in SUB are ours, from the contents list.
- SB6, themes: the skeleton's candidate hits were one paragraph early (from the trailing headings); confirmed hits are EDI 1.8 to 1.11 (with 1.7 and 3.5 on difference and perspectives), accessibility 1.12, 1.13, 2.7, 3.10, ESD 1.14 to 1.16, enterprise 1.17 to 1.22 and 2.8 (careers), with all four in the 4.2 row heading 'Embedded understanding of EDI, access, sustainability and entrepreneurship'. Large language models appear only in the integrity row (4.2.b66, b67, b69) and are recorded as theme:generative-ai by the batch 1 convention.
- SB6, frameworks: FHEQ Level 6 and FQHEIS Level 10 named together in 2.4 and 4.2. CQFW is not cited. 'Scottish Highers' (1.13) and Scottish four-year honours (2.6) name no framework.
- SB5 and SB6, bodies: no professional body for the subject is named; PSRBs appear only generically (front matter, 2.12). The Office for Students is named as England's regulator. UNESCO (1.14) and The British Academy (1.5 via SHAPE; section 5) are named organisations, not PSRBs; listed in SB6 only.
- SB6, shared documents: the Creative Writing statement is cited without a year (1.2, 3.4, 4.2); in September 2023 the current edition was 2019, but the ingested one is 2024. Linked to std:doc:qaa-creative-writing-2024-benchmarks; for P3. The Linguistics statement (1.2) is not yet ingested. The ESD guidance (2021) and the enterprise guidance (2018) are cited only in section 5 (excluded matter); 1.14 cites UNESCO (2019) directly.
- S2, subjects: HECoS 100320 (English studies, whose non-preferred terms include 'English') and CAH19-01 are stated by the subject name; 100318, 100319 and 100046 (with CAH19-01-02, CAH19-01-03 and CAH19-01-05) are stated by the course titles in 1.1. CAH19-01-01 (English studies, non-specific) is inferred as the CAH3 home of 100320. Linguistics (CAH19-01-07) is a neighbouring statement, not entered.
- S7, supersedes: section 6 names the fourth edition (2019), revised by QAA from the 2015 third edition; this edition (September 2023) is therefore read as the fifth (inferred). The 2023 advisory group is the one that wrote it.
- Patterns differing from Psychology: one three-column table in place of separate rung lists, linearised cell by cell; rung definitions as column headings rather than lead-ins; varying numbers of items per cell; a paragraph spanning all three columns; a separate creative writing lead-in inside the table; an outcome list with 'can' (1.6); large language models under integrity; no professional body.
- S9: not researched in P1.
- S1, licence: the text gives a copyright notice and no re-use terms; QAA's terms for holding and chunking are still to check.
- ST-12: versions here run to the lengths the content needs; no length range is yet set.

---

## Change notes
- 0.1.2, 3 October 2026, 21:02: moved with its held text from UNI to the source library repo (`wkspc2601-library/ingested/standards/`, texts in `txt/`, records in `records/`); paths only (Abbott, 20:56; std N-0119).
- 0.1.1, 3 October 2026, 20:20: obliging words outside the five read as must, "ought to" as should, on statements outside the rungs, each marked on its force line (Abbott, 20:17; D-std-0016).
- 0.1.0, 2026-10-03 17:11: researched by run frame 0.1.1-draft and standards run layer 0.7.0-draft, std, run 0105 (P1); built by tools/bm_build.py.
