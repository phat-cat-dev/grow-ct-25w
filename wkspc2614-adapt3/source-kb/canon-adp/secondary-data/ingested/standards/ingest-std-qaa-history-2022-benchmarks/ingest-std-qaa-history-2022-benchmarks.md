---
id: std:doc:qaa-history-2022-benchmarks
title: "Subject Benchmark Statement History"
profile: standards/subject-benchmark
profileVersion: 0.2.0-draft
issuer: QAA
kind: subject-benchmark
jurisdiction: [UK]
subjectScope: subjects
subjects:
  - { scheme: "hecos", code: "100302", label: "history", basis: "stated" }
  - { scheme: "cah", code: "CAH20-01-01", label: "history", basis: "stated" }
edition: "March 2022 (fifth edition)"
published: 2022-03
status: current
supersedes: "the fourth edition (2019), as the back matter states (D1, back matter: Membership of the Advisory Groups)"
heldText: { method: sha256-bytes, raw: db38993fdf620a2955b0f9bc2a33910eda84d551197c0610941606bfeebd5c6d, normalised: 92456e6ff367582a11ead5c3497f76cdefc49d72f10e383e98737192cf8fab68 }
heldTextStan: { method: sha256-stan, raw: db38993fdf620a2955b0f9bc2a33910eda84d551197c0610941606bfeebd5c6d, normalised: e2b55355c2aa9bd4063c6694dc82bfb76efba2dafbd21b5aca842035e39a15c8 }
licence: "QAA copyright; held for study, private to the project, never published"
series: "QAA Subject Benchmark Statements, fifth edition for History (March 2022), with the cross-cutting themes"
awardsCovered: ["bachelor's with honours"]
levelsCovered: ["fheq:6", "fqheis:10"]
nations: ["England", "Wales", "Scotland", "Northern Ireland"]
parts:
  S: full
  B: "partial: no glossary; the statement sends readers to QAA's Glossary and defines a few terms in passing"
  C: "not-applicable: the document sets expectations, not a procedure"
pins: { structure: 0.13.0-draft, template: 0.8.0-draft, benchmarkTemplate: 0.6.0-draft, runFrame: 0.1.1-draft, runLayer: 0.7.0-draft, standards: none yet, terminology: none yet }
lifecycle: drafted
researchedBy: run frame 0.1.1-draft; standards run layer 0.7.0-draft; std, run 0110 (tools/bm_build.py)
passes:
  P1: "2026-10-03 17:29"
  P2: "skipped: read direct from the held text; inferred codes and rung links are for P3"
  P3: open
version: 0.1.2
---

<!-- from INGEST wpk-0016-ingest-pd-template-standards.md 0.8.0-draft and wpk-0016-ingest-pd-template-standards-benchmark.md 0.6.0-draft; built by tools/bm_build.py from run-src/ -->
# Subject Benchmark Statement: History (QAA, March 2022)

> Run 0110, P1 by std. The issuer's words are held in the source library, `wkspc2601-library/txt/qaa-2022-history-subject-benchmark-statement-standard.norm.txt`; each S4 record carries its statement in full (`source`) for language analysis, with its span. Paraphrases and versions are ours. Private to the project, never published. In front matter `status` is the issuer's; ours is `lifecycle`. Doubts are in Part E.

## Part 0 Summary

### 0.1 Agent definition
<!-- label: editorial; status: drafted; basis: primary -->
QAA's UK reference point for what a History graduate should know, understand and be able to do at the end of a single honours bachelor's degree (FHEQ level 6, FQHEIS level 10), also relevant to History in joint, combined and interdisciplinary courses. Reach for it when designing, reviewing or describing a History course, its outcomes or its assessment. It states one rung only, the minimum threshold, and leaves the classes above it to Annex D of the Frameworks; it is not a curriculum and not a regulatory requirement in England.

### 0.2 Summary
<!-- label: both; status: drafted; basis: primary -->
Published by QAA in March 2022 as the fifth edition, the statement describes the purposes and character of a History degree, six distinctive design features, teaching, learning and assessment, and benchmark standards at the threshold only: 12 subject-specific items (4.5) and 17 generic skills (4.6), both threshold by 2.5, with a fuller form of the subject list among the degree's purposes (1.7). It adds the cross-cutting themes of equality, diversity and inclusion, accessibility, sustainability and enterprise, points to Annex D of the Frameworks for Higher Education Qualifications for the honours classifications, and names no professional, statutory or regulatory body in its body text. The 59 statements also hold provider expectations on course design and assessment (2.1, 2.4, 2.11, 3.7, 3.9 to 3.11, 4.2).

## Part S Standard

### S1 Identity
<!-- label: source; status: drafted; basis: primary -->
```yaml
issuer: The Quality Assurance Agency for Higher Education
title: "Subject Benchmark Statement History"
edition: "March 2022 (fifth edition)"
dates:
  published: 2022-03
  other: []
kind: subject-benchmark
jurisdiction: [UK]
authority: "reference: a sector reference point; in England not a sector-recognised standard under the OfS framework; a key reference point in Wales and Scotland; part of the quality requirements in Northern Ireland (D1, front matter: Relationship to legislation and regulation)"
licence: "QAA copyright; the document gives no re-use terms in its text (D1, front matter)"
copyrightNotice: { text: "© The Quality Assurance Agency for Higher Education 2022", locator: "D1, index" }
```

### S2 Purpose and scope
<!-- label: source; status: drafted; basis: primary -->
```yaml
governs: "what a History graduate can be expected to know, do and understand at the end of a single honours bachelor's degree, and the nature and characteristics of awards in the subject (D1, front matter: About this Statement; 1.1; 4.1)"
appliesTo:
  awards: ["bachelor's degrees with honours, single honours in History", "History in joint, combined and interdisciplinary courses (relevant, D1, 1.1; 2.6)"]
  levels: ["fheq:6", "fqheis:10"]
  providers: ["UK higher education providers"]
whoMustUse: "none-stated; it is a reference point, not a requirement (D1, front matter)"
howUsed: ["design", "approval", "review", "other: external examining; PSRBs; information for prospective students and employers"]
doesNot: "it is not a national curriculum and does not prescribe teaching, learning or assessment; it carries no statutory or regulatory requirement (D1, front matter)"
beneficiary: the student
statedScope: "\"This Subject Benchmark Statement is focused on single honours bachelor’s courses leading to a named award in History.\" (D1, 1.1)"
statedSubjects:
  - { name: "History", locator: "(D1, title; 1.1)", kind: "subject", codes: [{ scheme: "hecos", code: "100302", label: "history" }, { scheme: "cah", code: "CAH20-01-01", label: "history" }] }
  - { name: "History modules offered in joint or combined degrees, or in interdisciplinary courses that include a historical element", locator: "(D1, 1.1; 2.6)", kind: "programme title", codes: [{ scheme: "hecos", code: "100302", label: "history" }] }
  - { name: "Environmental history", locator: "(D1, 1.16; 1.17)", kind: "specialism", codes: [{ scheme: "hecos", code: "100670", label: "environmental history" }] }
  - { name: "Public history", locator: "(D1, 1.16; 1.17)", kind: "specialism", codes: [] }
  - { name: "Economic history", locator: "(D1, 1.16; 2.1)", kind: "specialism", codes: [{ scheme: "hecos", code: "100301", label: "economic history" }] }
  - { name: "Cultural history", locator: "(D1, 1.16; 2.1)", kind: "specialism", codes: [] }
  - { name: "Social history", locator: "(D1, 2.1)", kind: "specialism", codes: [{ scheme: "hecos", code: "100312", label: "social history" }] }
  - { name: "Political history", locator: "(D1, 2.1)", kind: "specialism", codes: [] }
  - { name: "Gender history", locator: "(D1, 2.1)", kind: "specialism", codes: [] }
subjects: see front matter (subjectScope subjects)
```

### S3 Structure
<!-- label: both; status: drafted; basis: primary -->
```yaml
components:
  - { number: "1.1", order: 3, componentType: paragraph, parent: "section 1", heading: "Context", gloss: "scope: single honours History, also relevant to joint, combined and interdisciplinary courses" }
  - { number: "1.2", order: 4, componentType: paragraph, parent: "section 1", heading: "Context", gloss: "the focus is honours; the criteria hold at every stage towards it" }
  - { number: "1.3", order: 5, componentType: paragraph, parent: "section 1", heading: "Context", gloss: "how the subject is organised; the term departments or subject groups" }
  - { number: "1.4", order: 6, componentType: paragraph, parent: "section 1", heading: "Purposes of a History degree", gloss: "what the subject studies: the whole human past, change and continuity" }
  - { number: "1.5", order: 7, componentType: stem, parent: "section 1", heading: "Purposes of a History degree", gloss: "capabilities shared with the humanities and social sciences (18 items, restated in 4.6)" }
  - { number: "1.6", order: 8, componentType: paragraph, parent: "section 1", heading: "Purposes of a History degree", gloss: "the distinctive education the subject gives" }
  - { number: "1.7", order: 9, componentType: stem, parent: "section 1", heading: "Purposes of a History degree", gloss: "outcomes on graduating with honours (12 items, restated more briefly in 4.5)" }
  - { number: "1.8", order: 10, componentType: paragraph, parent: "section 1", heading: "Purposes of a History degree", gloss: "interdisciplinarity and optional experiences such as fieldwork and mobility" }
  - { number: "1.9", order: 11, componentType: paragraph, parent: "section 1", heading: "Characteristics of a History degree", gloss: "independent engagement; no required core of knowledge" }
  - { number: "1.10", order: 12, componentType: paragraph, parent: "section 1", heading: "Characteristics of a History degree", gloss: "variety of teaching; each course sets its own outcomes" }
  - { number: "1.11", order: 13, componentType: paragraph, parent: "section 1", heading: "Characteristics of a History degree", gloss: "clear assessment policies; formative and summative assessment" }
  - { number: "1.12", order: 14, componentType: paragraph, parent: "section 1", heading: "Equality, diversity and inclusion", gloss: "diversity of past experience; a multi-perspectival discipline" }
  - { number: "1.13", order: 15, componentType: paragraph, parent: "section 1", heading: "Equality, diversity and inclusion", gloss: "contingent knowledge; uncomfortable pasts; marginalised cultures" }
  - { number: "1.14", order: 16, componentType: paragraph, parent: "section 1", heading: "Equality, diversity and inclusion", gloss: "an inclusive community: participation, inclusive curricula, decolonising" }
  - { number: "1.15", order: 17, componentType: paragraph, parent: "section 1", heading: "Equality, diversity and inclusion", gloss: "graduates' breadth of skills and contribution to society" }
  - { number: "1.16", order: 18, componentType: paragraph, parent: "section 1", heading: "Sustainability", gloss: "sustainability in content and method; the SDGs; environmental history" }
  - { number: "1.17", order: 19, componentType: paragraph, parent: "section 1", heading: "Sustainability", gloss: "heritage, conservation and public history" }
  - { number: "1.18", order: 20, componentType: paragraph, parent: "section 1", heading: "Sustainability", gloss: "a critical mindset for sustainability challenges" }
  - { number: "1.19", order: 21, componentType: paragraph, parent: "section 1", heading: "Entrepreneurship and enterprise education", gloss: "enterprise education and employability" }
  - { number: "1.20", order: 22, componentType: paragraph, parent: "section 1", heading: "Entrepreneurship and enterprise education", gloss: "employability skills built in; why employers value History graduates" }
  - { number: "1.21", order: 23, componentType: paragraph, parent: "section 1", heading: "Entrepreneurship and enterprise education", gloss: "recognising skills; graduate careers; outcome data" }
  - { number: "2.1", order: 25, componentType: area, parent: "section 2", heading: "Design", gloss: "six central features of a History degree, a) to f)" }
  - { number: "2.2", order: 26, componentType: paragraph, parent: "section 2", heading: "Accessibility", gloss: "accessible design and attention to students facing practical barriers" }
  - { number: "2.3", order: 27, componentType: paragraph, parent: "section 2", heading: "Progression", gloss: "cumulative, non-mechanical progression across an honours degree" }
  - { number: "2.4", order: 28, componentType: paragraph, parent: "section 2", heading: "Progression", gloss: "no fixed order of modules; departments explain progression" }
  - { number: "2.5", order: 29, componentType: paragraph, parent: "section 2", heading: "Progression", gloss: "yearly attainment towards the threshold; readiness for postgraduate study" }
  - { number: "2.6", order: 30, componentType: paragraph, parent: "section 2", heading: "Progression", gloss: "joint honours students reach part of the skills" }
  - { number: "2.7", order: 31, componentType: paragraph, parent: "section 2", heading: "Progression", gloss: "exit awards; four-year Scottish honours" }
  - { number: "2.8", order: 32, componentType: paragraph, parent: "section 2", heading: "Flexibility", gloss: "flexible delivery; part-time and mature students" }
  - { number: "2.9", order: 33, componentType: practice, parent: "section 2", heading: "Partnership", gloss: "placements and work-related projects" }
  - { number: "2.10", order: 34, componentType: paragraph, parent: "section 2", heading: "Monitoring and review", gloss: "monitoring and periodic review" }
  - { number: "2.11", order: 35, componentType: paragraph, parent: "section 2", heading: "Monitoring and review", gloss: "external reviewers in periodic review" }
  - { number: "2.12", order: 36, componentType: paragraph, parent: "section 2", heading: "Monitoring and review", gloss: "external examiners and threshold standards" }
  - { number: "3.1", order: 38, componentType: area, parent: "section 3", heading: "Content", gloss: "breadth and depth of content" }
  - { number: "3.2", order: 39, componentType: practice, parent: "section 3", heading: "Teaching and learning", gloss: "student-centred, blended teaching in many settings" }
  - { number: "3.3", order: 40, componentType: practice, parent: "section 3", heading: "Teaching and learning", gloss: "lectures in their many formats" }
  - { number: "3.4", order: 41, componentType: practice, parent: "section 3", heading: "Teaching and learning", gloss: "seminars and workshops in small groups" }
  - { number: "3.5", order: 42, componentType: practice, parent: "section 3", heading: "Teaching and learning", gloss: "independent study as the main mode" }
  - { number: "3.6", order: 43, componentType: practice, parent: "section 3", heading: "Teaching and learning", gloss: "critical and constructive comment on progress" }
  - { number: "3.7", order: 44, componentType: paragraph, parent: "section 3", heading: "Teaching and learning", gloss: "teaching methods vary and are reviewed; inclusion and sustainability" }
  - { number: "3.8", order: 45, componentType: paragraph, parent: "section 3", heading: "Teaching and learning", gloss: "module documentation for students" }
  - { number: "3.9", order: 46, componentType: practice, parent: "section 3", heading: "Assessment", gloss: "why assessment has to be diverse" }
  - { number: "3.10", order: 47, componentType: stem, parent: "section 3", heading: "Assessment", gloss: "six kinds of assessment a course should include, a) to f)" }
  - { number: "3.11", order: 48, componentType: practice, parent: "section 3", heading: "Assessment", gloss: "each department's assessment mix; every outcome assessed" }
  - { number: "4.1", order: 50, componentType: paragraph, parent: "section 4", heading: "Introduction", gloss: "the lists are the minimum threshold for honours" }
  - { number: "4.2", order: 51, componentType: paragraph, parent: "section 4", heading: "Introduction", gloss: "providers set evidence of achievement with Annex D" }
  - { number: "4.3", order: 52, componentType: paragraph, parent: "section 4", heading: "Introduction", gloss: "templates for different assessment modes" }
  - { number: "4.4", order: 53, componentType: paragraph, parent: "section 4", heading: "Introduction", gloss: "published criteria; positive marking; feedback" }
  - { number: "4.5", order: 54, componentType: stem, parent: "section 4", heading: "Minimum threshold standards", gloss: "threshold subject standards (12 items)" }
  - { number: "4.6", order: 55, componentType: stem, parent: "section 4", heading: "Generic skills", gloss: "threshold generic skills (17 items)" }
  - { number: "1", componentType: section, parent: none, heading: "Context and purposes of a History degree", gloss: "section 1" }
  - { number: "2", componentType: section, parent: none, heading: "Distinctive features of a History degree", gloss: "section 2" }
  - { number: "3", componentType: section, parent: none, heading: "Content, structure and delivery", gloss: "section 3" }
  - { number: "4", componentType: section, parent: none, heading: "Benchmark standards", gloss: "section 4" }
excluded:
  - { number: "none", heading: "Contents; About this Statement; How can I use this document?; Relationship to legislation and regulation; Additional sector reference points", kind: "other: front matter, read for S1, S2, S6 and SB6" }
  - { number: "none", heading: "section heading lines 1 to 4", kind: "other: headings, recorded in SECTIONS" }
  - { number: "5", heading: "List of references and further resources", kind: "other: back matter, read for SB6" }
  - { number: "6", heading: "Membership of the Advisory Groups for the Subject Benchmark Statement for History", kind: "other: back matter, read for the edition history (S8, supersedes)" }
```

### S4 Statements
<!-- label: both; status: drafted; basis: primary. Only standards (D-std-0002 (a)): 59 records. `source` is the issuer's statement exactly as its span holds it (D-std-0014). -->
```yaml
- id: qaa/history-2022/1.7.b1
  locator: { number: "1.7.b1", headingPath: ["Context and purposes of a History degree", "Purposes of a History degree"] }
  span: { start: 11748, end: 11802 }
  source: "ask relevant, cogent, and focused historical questions"
  stem: "1.7"
  statementType: outcome
  rung: none
  force: should
  level: fheq:6
  appliesTo: "graduates with honours in History"
  addressee: learner
  verbs: ["ask"]
  about: "framing historical questions"
  themes: [none]
  domain: subject-skill
  award: ["bachelor's with honours"]
  gradeOf: none
  paraphrase: "Should be able to frame pertinent, well-reasoned and tightly focused questions about the past."
  quote: full   # the issuer's statement is in `source` (D-std-0014)
  audience: both
  subjects: inherited
- id: qaa/history-2022/1.7.b2
  locator: { number: "1.7.b2", headingPath: ["Context and purposes of a History degree", "Purposes of a History degree"] }
  span: { start: 11805, end: 11875 }
  source: "know where and how to access relevant and precise historical knowledge"
  stem: "1.7"
  statementType: outcome
  rung: none
  force: should
  level: fheq:6
  appliesTo: "graduates with honours in History"
  addressee: learner
  verbs: ["know", "access"]
  about: "finding reliable historical knowledge"
  themes: [none]
  domain: knowledge
  award: ["bachelor's with honours"]
  gradeOf: none
  paraphrase: "Should be able to find out where trustworthy, exact knowledge about the past is held and how to reach it."
  quote: full   # the issuer's statement is in `source` (D-std-0014)
  audience: both
  subjects: inherited
- id: qaa/history-2022/1.7.b3
  locator: { number: "1.7.b3", headingPath: ["Context and purposes of a History degree", "Purposes of a History degree"] }
  span: { start: 11878, end: 12111 }
  source: "conduct structured enquiries that consist of setting tasks, gathering, sifting, selecting, organising, synthesising and analysing appropriate and often large quantities of evidence, including primary sources and secondary scholarship"
  stem: "1.7"
  statementType: outcome
  rung: none
  force: should
  level: fheq:6
  appliesTo: "graduates with honours in History"
  addressee: learner
  verbs: ["conduct"]
  about: "structured enquiry with large bodies of evidence"
  themes: [none]
  domain: subject-skill
  award: ["bachelor's with honours"]
  gradeOf: none
  paraphrase: "Should be able to plan and carry out a structured enquiry, from setting their own tasks to collecting, filtering, ordering, combining and analysing large bodies of primary and secondary evidence."
  quote: full   # the issuer's statement is in `source` (D-std-0014)
  audience: both
  subjects: inherited
- id: qaa/history-2022/1.7.b4
  locator: { number: "1.7.b4", headingPath: ["Context and purposes of a History degree", "Purposes of a History degree"] }
  span: { start: 12114, end: 12158 }
  source: "use valid and relevant evidence and argument"
  stem: "1.7"
  statementType: outcome
  rung: none
  force: should
  level: fheq:6
  appliesTo: "graduates with honours in History"
  addressee: learner
  verbs: ["use"]
  about: "using sound evidence and argument"
  themes: [none]
  domain: subject-skill
  award: ["bachelor's with honours"]
  gradeOf: none
  paraphrase: "Should be able to draw on sound, pertinent evidence and argument."
  quote: full   # the issuer's statement is in `source` (D-std-0014)
  audience: both
  subjects: inherited
- id: qaa/history-2022/1.7.b5
  locator: { number: "1.7.b5", headingPath: ["Context and purposes of a History degree", "Purposes of a History degree"] }
  span: { start: 12161, end: 12198 }
  source: "employ effective bibliographic skills"
  stem: "1.7"
  statementType: outcome
  rung: none
  force: should
  level: fheq:6
  appliesTo: "graduates with honours in History"
  addressee: learner
  verbs: ["employ"]
  about: "bibliographic skills"
  themes: [none]
  domain: subject-skill
  award: ["bachelor's with honours"]
  gradeOf: none
  paraphrase: "Should be able to handle references, reading lists and bibliographies well."
  quote: full   # the issuer's statement is in `source` (D-std-0014)
  audience: both
  subjects: inherited
- id: qaa/history-2022/1.7.b6
  locator: { number: "1.7.b6", headingPath: ["Context and purposes of a History degree", "Purposes of a History degree"] }
  span: { start: 12201, end: 12514 }
  source: "display analytical skills, including the recognition that not all statements are of equal validity; that there are ways of testing them; that historians operate by rules of evidence which, though themselves subject to critical evaluation, are also a component of intellectual integrity and maturity more generally"
  stem: "1.7"
  statementType: outcome
  rung: none
  force: should
  level: fheq:6
  appliesTo: "graduates with honours in History"
  addressee: learner
  verbs: ["display"]
  about: "analysing claims of differing validity"
  themes: [none]
  domain: subject-skill
  award: ["bachelor's with honours"]
  gradeOf: none
  paraphrase: "Should be able to analyse claims, recognising that some statements are better founded than others, and that historians test claims by rules of evidence which are themselves open to critique and which belong to intellectual integrity more widely."
  quote: full   # the issuer's statement is in `source` (D-std-0014)
  audience: both
  subjects: inherited
- id: qaa/history-2022/1.7.b7
  locator: { number: "1.7.b7", headingPath: ["Context and purposes of a History degree", "Purposes of a History degree"] }
  span: { start: 12517, end: 12775 }
  source: "critically and empathetically analyse primary sources, addressing questions of genre, content, perspective and purpose. Primary sources include any form of evidence from the past that is under examination, including textual, visual, material and oral sources"
  stem: "1.7"
  statementType: outcome
  rung: none
  force: should
  level: fheq:6
  appliesTo: "graduates with honours in History"
  addressee: learner
  verbs: ["analyse", "addressing"]
  about: "critical and empathetic analysis of primary sources"
  themes: [none]
  domain: subject-skill
  award: ["bachelor's with honours"]
  gradeOf: none
  paraphrase: "Should be able to analyse primary sources critically and with empathy, asking about their genre, content, viewpoint and purpose, taking primary sources to mean any textual, visual, material or oral evidence from the past that is being examined."
  quote: full   # the issuer's statement is in `source` (D-std-0014)
  audience: both
  subjects: inherited
- id: qaa/history-2022/1.7.b8
  locator: { number: "1.7.b8", headingPath: ["Context and purposes of a History degree", "Purposes of a History degree"] }
  span: { start: 12778, end: 13238 }
  source: "understand the problems inherent in the historical record itself: awareness of a range of viewpoints and ways to evaluate them; appreciation of the range of problems involved in the interpretation of complex, ambiguous, conflicting and often incomplete material; and comprehension of the limitations of knowledge and dangers of simplistic explanations. These capacities provide an enhanced ability to critically analyse broader historical claims in public life"
  stem: "1.7"
  statementType: outcome
  rung: none
  force: should
  level: fheq:6
  appliesTo: "graduates with honours in History"
  addressee: learner
  verbs: ["understand"]
  about: "the problems of the historical record"
  themes: [none]
  domain: understanding
  award: ["bachelor's with honours"]
  gradeOf: none
  paraphrase: "Should be able to grasp the problems of the historical record: weighing differing viewpoints, interpreting material that is complex, unclear, contradictory or partial, and seeing where knowledge stops and where over-simple explanation misleads, a grasp that also helps them test historical claims made in public life."
  quote: full   # the issuer's statement is in `source` (D-std-0014)
  audience: both
  subjects: inherited
- id: qaa/history-2022/1.7.b9
  locator: { number: "1.7.b9", headingPath: ["Context and purposes of a History degree", "Purposes of a History degree"] }
  span: { start: 13241, end: 13429 }
  source: "appreciate complexity and diversity of situations, events and mentalities in the past and, by extension, present; history is an anti-reductionist subject that fosters intellectual maturity"
  stem: "1.7"
  statementType: outcome
  rung: none
  force: should
  level: fheq:6
  appliesTo: "graduates with honours in History"
  addressee: learner
  verbs: ["appreciate"]
  about: "complexity and diversity of the past"
  themes: [none]
  domain: understanding
  award: ["bachelor's with honours"]
  gradeOf: none
  paraphrase: "Should be able to appreciate how varied and complicated past situations, events and outlooks were, and so how varied the present is, seeing history as a subject that resists reduction and builds intellectual maturity."
  quote: full   # the issuer's statement is in `source` (D-std-0014)
  audience: both
  subjects: inherited
- id: qaa/history-2022/1.7.b10
  locator: { number: "1.7.b10", headingPath: ["Context and purposes of a History degree", "Purposes of a History degree"] }
  span: { start: 13432, end: 13795 }
  source: "understand how people have existed, acted and thought in the always-different context of the past. History involves encountering the past’s otherness and learning to understand unfamiliar structures, cultures and belief systems. These forms of understanding illuminate the influence of the past on the present; they also foster empathy, and respect for difference"
  stem: "1.7"
  statementType: outcome
  rung: none
  force: should
  level: fheq:6
  appliesTo: "graduates with honours in History"
  addressee: learner
  verbs: ["understand"]
  about: "understanding the past on its own terms"
  themes: [none]
  domain: understanding
  award: ["bachelor's with honours"]
  gradeOf: none
  paraphrase: "Should be able to understand how people lived, acted and thought in past settings that always differ from our own, meeting the strangeness of the past, coming to understand unfamiliar structures, cultures and beliefs, and so gaining empathy and respect for difference."
  quote: full   # the issuer's statement is in `source` (D-std-0014)
  audience: both
  subjects: inherited
- id: qaa/history-2022/1.7.b11
  locator: { number: "1.7.b11", headingPath: ["Context and purposes of a History degree", "Purposes of a History degree"] }
  span: { start: 13798, end: 13964 }
  source: "sustain a reasoned line of argument in the face of others, to listen, to engage in sustained debate, to amend views as necessary in the light of evidence and argument"
  stem: "1.7"
  statementType: outcome
  rung: none
  force: should
  level: fheq:6
  appliesTo: "graduates with honours in History"
  addressee: learner
  verbs: ["sustain", "listen", "engage", "amend"]
  about: "sustaining and revising an argument in debate"
  themes: [none]
  domain: subject-skill
  award: ["bachelor's with honours"]
  gradeOf: none
  paraphrase: "Should be able to hold to a reasoned argument when others disagree, listen, debate at length and change their view where evidence and argument call for it."
  quote: full   # the issuer's statement is in `source` (D-std-0014)
  audience: both
  subjects: inherited
- id: qaa/history-2022/1.7.b12
  locator: { number: "1.7.b12", headingPath: ["Context and purposes of a History degree", "Purposes of a History degree"] }
  span: { start: 13967, end: 14081 }
  source: "marshal an argument in pursuit of meaningful questions about the past and, by implication, the present and future."
  stem: "1.7"
  statementType: outcome
  rung: none
  force: should
  level: fheq:6
  appliesTo: "graduates with honours in History"
  addressee: learner
  verbs: ["marshal"]
  about: "arguing about the past with a bearing on present and future"
  themes: [none]
  domain: subject-skill
  award: ["bachelor's with honours"]
  gradeOf: none
  paraphrase: "Should be able to build an argument around questions about the past that matter, and that also bear on the present and future."
  quote: full   # the issuer's statement is in `source` (D-std-0014)
  audience: both
  subjects: inherited
- id: qaa/history-2022/1.20
  locator: { number: "1.20", headingPath: ["Context and purposes of a History degree", "Entrepreneurship and enterprise education"] }
  span: { start: 22810, end: 23177 }
  source: "The practice of working across a wide range of historical sources requires History students to be proficient in the retrieval, selection, interpretation, analysis and synthesis of information from extensive datasets, both analogue and digital, and to be able to summarise complex knowledge and form and communicate clear, reasoned arguments to a variety of audiences."
  stem: none
  statementType: expectation
  rung: none
  force: must
  level: fheq:6
  appliesTo: "students of History"
  addressee: learner
  verbs: ["summarise", "form", "communicate"]
  about: "handling information and arguing for audiences, for employability"
  themes: [theme:enterprise]
  domain: generic-skill
  award: ["bachelor's with honours"]
  gradeOf: none
  paraphrase: "Because the subject works across a wide range of sources, History students must become skilled at finding, choosing, interpreting, analysing and combining information from large analogue and digital datasets, and at condensing complex knowledge into clear, reasoned arguments for varied audiences."
  quote: full   # the issuer's statement is in `source` (D-std-0014)
  audience: both
  subjects: inherited
- id: qaa/history-2022/2.1.b2
  locator: { number: "2.1.b2", headingPath: ["Distinctive features of a History degree", "Design"] }
  span: { start: 24776, end: 24941 }
  source: "Where a single country is the predominant focus of the course, that course incorporates serious and sustained comparison with others and should be multiperspectival."
  stem: "2.1"
  statementType: expectation
  rung: none
  force: should
  level: none
  appliesTo: "History courses focused mainly on one country"
  addressee: provider
  verbs: ["incorporates"]
  about: "comparison in courses centred on one country"
  themes: [none]
  domain: none
  award: ["bachelor's with honours"]
  gradeOf: none
  paraphrase: "A course centred mainly on one country brings in sustained, serious comparison with other places and should take several perspectives."
  quote: full   # the issuer's statement is in `source` (D-std-0014)
  audience: practitioner
  subjects: inherited
- id: qaa/history-2022/2.1.b3
  locator: { number: "2.1.b3", headingPath: ["Distinctive features of a History degree", "Design"] }
  span: { start: 25229, end: 25322 }
  source: "opportunity for close work on source material originating in the period studied is essential."
  stem: "2.1"
  statementType: expectation
  rung: none
  force: must   # D-std-0016: "is essential" read as must
  level: fheq:6
  appliesTo: "History honours courses and their students"
  addressee: both
  verbs: []
  about: "close work on primary sources from the period"
  themes: [none]
  domain: subject-skill
  award: ["bachelor's with honours"]
  gradeOf: none
  paraphrase: "Close study of material produced in the period being studied is indispensable to the degree."
  quote: full   # the issuer's statement is in `source` (D-std-0014)
  audience: both
  subjects: inherited
- id: qaa/history-2022/2.1.b4
  locator: { number: "2.1.b4", headingPath: ["Distinctive features of a History degree", "Design"] }
  span: { start: 26288, end: 26978 }
  source: "History students are expected to demonstrate wider historiographical and methodological awareness and understanding in all modules they undertake, and also in independent extended pieces of coursework. Students also receive appropriate guidance in, and are able to demonstrate their application of, appropriate research ethics; this may include, but is not limited to, compliance with specific and detailed codes and policies covering research ethics developed both by higher education institutions and archival repositories. History students are also acquainted with the subject’s protocols and expectations regarding the quotation and reproduction of the work of others in their own work."
  stem: "2.1"
  statementType: expectation
  rung: none
  force: must   # D-std-0016: "are expected to" read as must
  level: fheq:6
  appliesTo: "students of History"
  addressee: learner
  verbs: ["demonstrate", "receive"]
  about: "historiographical, methodological and ethical awareness across modules"
  themes: [none]
  domain: understanding
  award: ["bachelor's with honours"]
  gradeOf: none
  paraphrase: "Students are expected to show awareness and understanding of historiography and method in every module and in long independent work, to receive guidance in research ethics and show they apply it, and to know the subject's conventions for quoting and reproducing others' work."
  quote: full   # the issuer's statement is in `source` (D-std-0014)
  audience: both
  subjects: inherited
- id: qaa/history-2022/2.4
  locator: { number: "2.4", headingPath: ["Distinctive features of a History degree", "Progression"] }
  span: { start: 30639, end: 30778 }
  source: "However, it is the responsibility of departments to clearly articulate how a given course facilitates progression over the period of study."
  stem: none
  statementType: expectation
  rung: none
  force: must   # D-std-0016: "the responsibility of" read as must
  level: none
  appliesTo: "History departments"
  addressee: provider
  verbs: ["articulate", "facilitates"]
  about: "explaining progression in a non-sequential subject"
  themes: [none]
  domain: none
  award: ["bachelor's with honours"]
  gradeOf: none
  paraphrase: "History has no fixed order of modules, so departments carry the responsibility to explain clearly how each course supports progression across its years."
  quote: full   # the issuer's statement is in `source` (D-std-0014)
  audience: practitioner
  subjects: inherited
- id: qaa/history-2022/2.5
  locator: { number: "2.5", headingPath: ["Distinctive features of a History degree", "Progression"] }
  span: { start: 30779, end: 31295 }
  source: "2.5 Ultimately, it is expected that each year would see the attainment of certain levels of knowledge, expertise and experience which builds towards the final achievement of meeting all of the threshold-level subject-specific and generic skills listed in this Statement. Upon graduation from an undergraduate degree, it would be expected that a student who had\n\n10\nachieved a second-class degree or higher would be capable of, and equipped for, undertaking postgraduate study in History or an associated discipline.\n"
  stem: none
  statementType: expectation
  rung: none
  force: describes
  level: fheq:6
  appliesTo: "students and graduates of History honours courses"
  addressee: learner
  verbs: ["builds", "achieved", "undertaking"]
  about: "yearly attainment towards the threshold; readiness for postgraduate study"
  themes: [none]
  domain: none
  award: ["bachelor's with honours"]
  gradeOf: none
  paraphrase: "Each year is expected to bring knowledge, expertise and experience that build towards meeting every threshold subject and generic skill in the statement; a graduate with a second-class degree or better is expected to be ready for postgraduate study in History or a related field."
  quote: full   # the issuer's statement is in `source` (D-std-0014)
  audience: both
  subjects: inherited
- id: qaa/history-2022/2.6
  locator: { number: "2.6", headingPath: ["Distinctive features of a History degree", "Progression"] }
  span: { start: 31295, end: 31477 }
  source: "2.6 Joint honours undergraduates will achieve elements of the specific and generic skills for the subject but will add others according to the subjects covered in a joint programme.\n"
  stem: none
  statementType: outcome
  rung: none
  force: will
  level: fheq:6
  appliesTo: "joint honours undergraduates"
  addressee: learner
  verbs: ["achieve", "add"]
  about: "joint honours: part of the subject and generic skills"
  themes: [none]
  domain: none
  award: ["bachelor's with honours"]
  gradeOf: none
  paraphrase: "Joint honours students will reach some of the subject's specific and generic skills and will gain others from the other subjects they study."
  quote: full   # the issuer's statement is in `source` (D-std-0014)
  audience: both
  subjects: inherited
- id: qaa/history-2022/2.11
  locator: { number: "2.11", headingPath: ["Distinctive features of a History degree", "Monitoring and review"] }
  span: { start: 34111, end: 34423 }
  source: "2.11 Externality is an essential component of the quality assurance system in the UK. Higher education providers will use external reviewers as part of periodic review to gain an external perspective on any proposed changes and ensure threshold standards are achieved and content is appropriate for the subject.\n"
  stem: none
  statementType: expectation
  rung: none
  force: will
  level: none
  appliesTo: "higher education providers in periodic review"
  addressee: provider
  verbs: ["use", "gain", "ensure"]
  about: "external reviewers in periodic review"
  themes: [none]
  domain: none
  award: ["bachelor's with honours"]
  gradeOf: none
  paraphrase: "Providers will bring external reviewers into periodic review for an outside view of proposed changes and to make sure threshold standards are met and content suits the subject."
  quote: full   # the issuer's statement is in `source` (D-std-0014)
  audience: practitioner
  subjects: inherited
- id: qaa/history-2022/3.7
  locator: { number: "3.7", headingPath: ["Content, structure and delivery", "Teaching and learning"] }
  span: { start: 40166, end: 40336 }
  source: "Teaching and learning methods should also reflect the need to provide an inclusive learning environment and to reflect the goals of Education for Sustainable Development."
  stem: none
  statementType: expectation
  rung: none
  force: should
  level: none
  appliesTo: "History departments and teaching staff"
  addressee: provider
  verbs: ["reflect", "provide"]
  about: "inclusive and sustainable teaching methods"
  themes: [theme:edi, theme:esd]
  domain: none
  award: ["bachelor's with honours"]
  gradeOf: none
  paraphrase: "Teaching and learning methods should also show the need for an inclusive environment and serve the aims of education for sustainable development."
  quote: full   # the issuer's statement is in `source` (D-std-0014)
  audience: practitioner
  subjects: inherited
- id: qaa/history-2022/3.9
  locator: { number: "3.9", headingPath: ["Content, structure and delivery", "Assessment"] }
  span: { start: 41056, end: 41575 }
  source: "3.9 Diversity in assessment is vital for two main reasons. First, the full range of a student's abilities is most unlikely to be revealed through any single mode. Second, the diverse educational backgrounds and formal qualifications of students embarking on degree- level study mean that courses should provide all students with opportunities to show what they know, understand and can do. Students will be rewarded for what they are good at, as well as gaining skills and awareness in what they find more challenging.\n"
  stem: none
  statementType: expectation
  rung: none
  force: should
  level: none
  appliesTo: "History courses"
  addressee: provider
  verbs: ["provide", "show"]
  about: "diverse assessment so every student can show their abilities"
  themes: [none]
  domain: none
  award: ["bachelor's with honours"]
  gradeOf: none
  paraphrase: "Assessment needs variety, because no single mode reveals all of a student's abilities and students arrive with different backgrounds; courses should give everyone chances to demonstrate their knowledge, understanding and skills, rewarding strengths while building weaker areas."
  quote: full   # the issuer's statement is in `source` (D-std-0014)
  audience: practitioner
  subjects: inherited
- id: qaa/history-2022/3.10.b1
  locator: { number: "3.10.b1", headingPath: ["Content, structure and delivery", "Assessment"] }
  span: { start: 41786, end: 42216 }
  source: "assessments that show a student’s ability to communicate information and argument effectively as appropriate to the task set. This includes writing in various forms, at varying lengths, for different audiences, such as reviews, reports, essays or a dissertation. It also includes communication in forms outside written prose, such as oral presentations, the creation of videos, websites and databases, and digital history projects"
  stem: "3.10"
  statementType: expectation
  rung: none
  force: should
  level: none
  appliesTo: "the assessment of History courses"
  addressee: provider
  verbs: ["show", "communicate"]
  about: "communication assessments in varied forms"
  themes: [none]
  domain: none
  award: ["bachelor's with honours"]
  gradeOf: none
  paraphrase: "Assessments should include tasks in which students communicate information and argument to suit the task, in written forms of differing kinds, lengths and audiences, and in forms beyond prose such as talks, videos, websites, databases and digital history projects."
  quote: full   # the issuer's statement is in `source` (D-std-0014)
  audience: practitioner
  subjects: inherited
- id: qaa/history-2022/3.10.b2
  locator: { number: "3.10.b2", headingPath: ["Content, structure and delivery", "Assessment"] }
  span: { start: 42220, end: 42358 }
  source: "assessments that demonstrate an ability to work with a range of historical evidence, such as source or ‘gobbet’ exercises, or commentaries"
  stem: "3.10"
  statementType: expectation
  rung: none
  force: should
  level: none
  appliesTo: "the assessment of History courses"
  addressee: provider
  verbs: ["demonstrate", "work"]
  about: "work with historical evidence"
  themes: [none]
  domain: none
  award: ["bachelor's with honours"]
  gradeOf: none
  paraphrase: "Assessments should include tasks that test handling varied kinds of historical evidence, for example gobbet exercises, source exercises or commentaries."
  quote: full   # the issuer's statement is in `source` (D-std-0014)
  audience: practitioner
  subjects: inherited
- id: qaa/history-2022/3.10.b3
  locator: { number: "3.10.b3", headingPath: ["Content, structure and delivery", "Assessment"] }
  span: { start: 42362, end: 42647 }
  source: "assessments that demonstrate a student’s ability to work under pressure of time and think quickly. This may in some cases take the form of a traditional, timed exam, or it may be seen in a range of other tasks, such as ‘take home’ papers or a task spread over a number of hours or days"
  stem: "3.10"
  statementType: expectation
  rung: none
  force: should
  level: none
  appliesTo: "the assessment of History courses"
  addressee: provider
  verbs: ["demonstrate", "work", "think"]
  about: "time-pressured assessment"
  themes: [none]
  domain: none
  award: ["bachelor's with honours"]
  gradeOf: none
  paraphrase: "Assessments should include tasks that test working against the clock and quick thinking, whether a timed exam, a take-home paper or a task over hours or days."
  quote: full   # the issuer's statement is in `source` (D-std-0014)
  audience: practitioner
  subjects: inherited
- id: qaa/history-2022/3.10.b4
  locator: { number: "3.10.b4", headingPath: ["Content, structure and delivery", "Assessment"] }
  span: { start: 42651, end: 42731 }
  source: "assessments that demonstrate an ability to work independently, under supervision"
  stem: "3.10"
  statementType: expectation
  rung: none
  force: should
  level: none
  appliesTo: "the assessment of History courses"
  addressee: provider
  verbs: ["demonstrate", "work"]
  about: "supervised independent work"
  themes: [none]
  domain: none
  award: ["bachelor's with honours"]
  gradeOf: none
  paraphrase: "Assessments should include tasks that test independent work carried out under supervision."
  quote: full   # the issuer's statement is in `source` (D-std-0014)
  audience: practitioner
  subjects: inherited
- id: qaa/history-2022/3.10.b5
  locator: { number: "3.10.b5", headingPath: ["Content, structure and delivery", "Assessment"] }
  span: { start: 42739, end: 42879 }
  source: "assessments that show an ability to collaborate with others and work effectively as part of a group, such as group presentations or projects"
  stem: "3.10"
  statementType: expectation
  rung: none
  force: should
  level: none
  appliesTo: "the assessment of History courses"
  addressee: provider
  verbs: ["show", "collaborate", "work"]
  about: "collaboration and group work"
  themes: [none]
  domain: none
  award: ["bachelor's with honours"]
  gradeOf: none
  paraphrase: "Assessments should include tasks that test collaboration and effective group work, such as group presentations or projects."
  quote: full   # the issuer's statement is in `source` (D-std-0014)
  audience: practitioner
  subjects: inherited
- id: qaa/history-2022/3.10.b6
  locator: { number: "3.10.b6", headingPath: ["Content, structure and delivery", "Assessment"] }
  span: { start: 42883, end: 43572 }
  source: "at least one major assignment in which students are assessed on their ability to address historical problems in depth through structured historical enquiry . Students are given the opportunity to pursue a historical enquiry , sustaining and developing it through several stages. Such an exercise involves both task-s etti ng and problem- solving. This is often done through an extended piece of wri tten work, sometimes known as a dissertation or final year project, usually of at least twice the length re quired for standard coursework essays; however, it may also be assessed in other forms, including 'authentic' assessment tasks such as writing and presenting for different audiences."
  stem: "3.10"
  statementType: expectation
  rung: none
  force: should
  level: none
  appliesTo: "the assessment of History courses"
  addressee: provider
  verbs: ["assessed", "address", "pursue", "sustaining", "developing"]
  about: "a major staged historical enquiry"
  themes: [none]
  domain: none
  award: ["bachelor's with honours"]
  gradeOf: none
  paraphrase: "Assessments should include at least one major assignment testing the ability to tackle historical problems in depth through structured enquiry pursued over several stages, often a dissertation or final year project at least twice the usual essay length, though other forms, including authentic tasks for different audiences, are possible."
  quote: full   # the issuer's statement is in `source` (D-std-0014)
  audience: practitioner
  subjects: inherited
- id: qaa/history-2022/3.11
  locator: { number: "3.11", headingPath: ["Content, structure and delivery", "Assessment"] }
  span: { start: 44079, end: 44347 }
  source: "In any case, however, the overall combination of assessments must enable students to demonstrate all the learning outcomes of their course, and students given clear, timely information on how they will be assessed as well as constructive feedback on their assessments."
  stem: none
  statementType: requirement
  rung: none
  force: must
  level: none
  appliesTo: "the assessment of History courses"
  addressee: provider
  verbs: ["enable", "demonstrate"]
  about: "assessment covering every outcome, with information and feedback"
  themes: [none]
  domain: none
  award: ["bachelor's with honours"]
  gradeOf: none
  paraphrase: "Whatever the mix, the assessments as a whole must let students show every learning outcome of their course, with clear and timely information on how they will be assessed and constructive feedback."
  quote: full   # the issuer's statement is in `source` (D-std-0014)
  audience: practitioner
  subjects: inherited
- id: qaa/history-2022/4.2
  locator: { number: "4.2", headingPath: ["Benchmark standards", "Introduction"] }
  span: { start: 44718, end: 45263 }
  source: "4.2 Each higher education provider has its own method of determining what appropriate evidence of this achievement will be and should refer to Annex D: Outcome classification descriptions for FHEQ Level 6 and FQHEIS Level 10 degrees. This Annex sets out common descriptions of the four main degree outcome classifications for bachelor's degrees with honours: 1st, 2:1, 2:2 and 3rd. Higher education providers operate, and publish for their students, their own descriptors. This might take the form of a template setting out assessment criteria.\n"
  stem: none
  statementType: expectation
  rung: none
  force: should
  level: fheq:6
  appliesTo: "higher education providers"
  addressee: provider
  verbs: ["refer", "operate", "publish"]
  about: "evidence of achievement and Annex D"
  themes: [none]
  domain: none
  award: ["bachelor's with honours"]
  gradeOf: none
  paraphrase: "Each provider sets its own way of judging what counts as evidence of achievement and should consult Annex D's classification descriptions for honours degrees at FHEQ level 6 and FQHEIS level 10; providers run and publish their own descriptors, perhaps as assessment criteria."
  quote: full   # the issuer's statement is in `source` (D-std-0014)
  audience: practitioner
  subjects: inherited
- id: qaa/history-2022/4.5.b1
  locator: { number: "4.5.b1", headingPath: ["Benchmark standards", "Minimum threshold standards"] }
  span: { start: 46030, end: 46084 }
  source: "ask relevant, cogent, and focused historical questions"
  stem: "4.5"
  statementType: threshold
  rung: threshold
  force: should
  level: fheq:6
  appliesTo: "graduates with honours in History, at the minimum"
  addressee: learner
  verbs: ["ask"]
  about: "framing historical questions"
  themes: [none]
  domain: subject-skill
  award: ["bachelor's with honours"]
  gradeOf: none
  paraphrase: "At threshold, should be able to frame pertinent, well-reasoned and tightly focused questions about the past."
  quote: full   # the issuer's statement is in `source` (D-std-0014)
  audience: both
  subjects: inherited
- id: qaa/history-2022/4.5.b2
  locator: { number: "4.5.b2", headingPath: ["Benchmark standards", "Minimum threshold standards"] }
  span: { start: 46087, end: 46157 }
  source: "know where and how to access relevant and precise historical knowledge"
  stem: "4.5"
  statementType: threshold
  rung: threshold
  force: should
  level: fheq:6
  appliesTo: "graduates with honours in History, at the minimum"
  addressee: learner
  verbs: ["know", "access"]
  about: "finding reliable historical knowledge"
  themes: [none]
  domain: knowledge
  award: ["bachelor's with honours"]
  gradeOf: none
  paraphrase: "At threshold, should be able to find out where trustworthy, exact knowledge about the past is held and how to reach it."
  quote: full   # the issuer's statement is in `source` (D-std-0014)
  audience: both
  subjects: inherited
- id: qaa/history-2022/4.5.b3
  locator: { number: "4.5.b3", headingPath: ["Benchmark standards", "Minimum threshold standards"] }
  span: { start: 46160, end: 46392 }
  source: "conduct structured enquiry that consists of setting tasks, gathering, sifting, selecting, organising, synthesising and analysing appropriate and often large quantities of evidence, including primary sources and secondary scholarship"
  stem: "4.5"
  statementType: threshold
  rung: threshold
  force: should
  level: fheq:6
  appliesTo: "graduates with honours in History, at the minimum"
  addressee: learner
  verbs: ["conduct"]
  about: "structured enquiry with large bodies of evidence"
  themes: [none]
  domain: subject-skill
  award: ["bachelor's with honours"]
  gradeOf: none
  paraphrase: "At threshold, should be able to plan and carry out a structured enquiry, from setting their own tasks to collecting, filtering, ordering, combining and analysing large bodies of primary and secondary evidence."
  quote: full   # the issuer's statement is in `source` (D-std-0014)
  audience: both
  subjects: inherited
- id: qaa/history-2022/4.5.b4
  locator: { number: "4.5.b4", headingPath: ["Benchmark standards", "Minimum threshold standards"] }
  span: { start: 46395, end: 46439 }
  source: "use valid and relevant evidence and argument"
  stem: "4.5"
  statementType: threshold
  rung: threshold
  force: should
  level: fheq:6
  appliesTo: "graduates with honours in History, at the minimum"
  addressee: learner
  verbs: ["use"]
  about: "using sound evidence and argument"
  themes: [none]
  domain: subject-skill
  award: ["bachelor's with honours"]
  gradeOf: none
  paraphrase: "At threshold, should be able to draw on sound, pertinent evidence and argument."
  quote: full   # the issuer's statement is in `source` (D-std-0014)
  audience: both
  subjects: inherited
- id: qaa/history-2022/4.5.b5
  locator: { number: "4.5.b5", headingPath: ["Benchmark standards", "Minimum threshold standards"] }
  span: { start: 46442, end: 46479 }
  source: "employ effective bibliographic skills"
  stem: "4.5"
  statementType: threshold
  rung: threshold
  force: should
  level: fheq:6
  appliesTo: "graduates with honours in History, at the minimum"
  addressee: learner
  verbs: ["employ"]
  about: "bibliographic skills"
  themes: [none]
  domain: subject-skill
  award: ["bachelor's with honours"]
  gradeOf: none
  paraphrase: "At threshold, should be able to handle references, reading lists and bibliographies well."
  quote: full   # the issuer's statement is in `source` (D-std-0014)
  audience: both
  subjects: inherited
- id: qaa/history-2022/4.5.b6
  locator: { number: "4.5.b6", headingPath: ["Benchmark standards", "Minimum threshold standards"] }
  span: { start: 46482, end: 46580 }
  source: "display analytical skills, including the recognition that not all statements are of equal validity"
  stem: "4.5"
  statementType: threshold
  rung: threshold
  force: should
  level: fheq:6
  appliesTo: "graduates with honours in History, at the minimum"
  addressee: learner
  verbs: ["display"]
  about: "analysing claims of differing validity"
  themes: [none]
  domain: subject-skill
  award: ["bachelor's with honours"]
  gradeOf: none
  paraphrase: "At threshold, should be able to analyse claims, recognising that some statements are better founded than others."
  quote: full   # the issuer's statement is in `source` (D-std-0014)
  audience: both
  subjects: inherited
- id: qaa/history-2022/4.5.b7
  locator: { number: "4.5.b7", headingPath: ["Benchmark standards", "Minimum threshold standards"] }
  span: { start: 46583, end: 46701 }
  source: "critically and empathetically analyse primary sources, addressing questions of genre, content, perspective and purpose"
  stem: "4.5"
  statementType: threshold
  rung: threshold
  force: should
  level: fheq:6
  appliesTo: "graduates with honours in History, at the minimum"
  addressee: learner
  verbs: ["analyse", "addressing"]
  about: "critical and empathetic analysis of primary sources"
  themes: [none]
  domain: subject-skill
  award: ["bachelor's with honours"]
  gradeOf: none
  paraphrase: "At threshold, should be able to analyse primary sources critically and with empathy, asking about their genre, content, viewpoint and purpose."
  quote: full   # the issuer's statement is in `source` (D-std-0014)
  audience: both
  subjects: inherited
- id: qaa/history-2022/4.5.b8
  locator: { number: "4.5.b8", headingPath: ["Benchmark standards", "Minimum threshold standards"] }
  span: { start: 46704, end: 47055 }
  source: "understand the problems inherent in the historical record itself: awareness of a range of viewpoints and ways to evaluate them; appreciation of the range of problems involved in the interpretation of complex, ambiguous, conflicting and often incomplete material; and comprehension of the limitations of knowledge and dangers of simplistic explanations"
  stem: "4.5"
  statementType: threshold
  rung: threshold
  force: should
  level: fheq:6
  appliesTo: "graduates with honours in History, at the minimum"
  addressee: learner
  verbs: ["understand"]
  about: "the problems of the historical record"
  themes: [none]
  domain: understanding
  award: ["bachelor's with honours"]
  gradeOf: none
  paraphrase: "At threshold, should be able to grasp the problems of the historical record: weighing differing viewpoints, interpreting material that is complex, unclear, contradictory or partial, and seeing where knowledge stops and where over-simple explanation misleads."
  quote: full   # the issuer's statement is in `source` (D-std-0014)
  audience: both
  subjects: inherited
- id: qaa/history-2022/4.5.b9
  locator: { number: "4.5.b9", headingPath: ["Benchmark standards", "Minimum threshold standards"] }
  span: { start: 47058, end: 47170 }
  source: "appreciate complexity and diversity of situations, events and mentalities in the past and, by extension, present"
  stem: "4.5"
  statementType: threshold
  rung: threshold
  force: should
  level: fheq:6
  appliesTo: "graduates with honours in History, at the minimum"
  addressee: learner
  verbs: ["appreciate"]
  about: "complexity and diversity of the past"
  themes: [none]
  domain: understanding
  award: ["bachelor's with honours"]
  gradeOf: none
  paraphrase: "At threshold, should be able to appreciate how varied and complicated past situations, events and outlooks were, and so how varied the present is."
  quote: full   # the issuer's statement is in `source` (D-std-0014)
  audience: both
  subjects: inherited
- id: qaa/history-2022/4.5.b10
  locator: { number: "4.5.b10", headingPath: ["Benchmark standards", "Minimum threshold standards"] }
  span: { start: 47173, end: 47270 }
  source: "understand how people have existed, acted and thought in the always-different context of the past"
  stem: "4.5"
  statementType: threshold
  rung: threshold
  force: should
  level: fheq:6
  appliesTo: "graduates with honours in History, at the minimum"
  addressee: learner
  verbs: ["understand"]
  about: "understanding the past on its own terms"
  themes: [none]
  domain: understanding
  award: ["bachelor's with honours"]
  gradeOf: none
  paraphrase: "At threshold, should be able to understand how people lived, acted and thought in past settings that always differ from our own."
  quote: full   # the issuer's statement is in `source` (D-std-0014)
  audience: both
  subjects: inherited
- id: qaa/history-2022/4.5.b11
  locator: { number: "4.5.b11", headingPath: ["Benchmark standards", "Minimum threshold standards"] }
  span: { start: 47273, end: 47439 }
  source: "sustain a reasoned line of argument in the face of others, to listen, to engage in sustained debate, to amend views as necessary in the light of evidence and argument"
  stem: "4.5"
  statementType: threshold
  rung: threshold
  force: should
  level: fheq:6
  appliesTo: "graduates with honours in History, at the minimum"
  addressee: learner
  verbs: ["sustain", "listen", "engage", "amend"]
  about: "sustaining and revising an argument in debate"
  themes: [none]
  domain: subject-skill
  award: ["bachelor's with honours"]
  gradeOf: none
  paraphrase: "At threshold, should be able to hold to a reasoned argument when others disagree, listen, debate at length and change their view where evidence and argument call for it."
  quote: full   # the issuer's statement is in `source` (D-std-0014)
  audience: both
  subjects: inherited
- id: qaa/history-2022/4.5.b12
  locator: { number: "4.5.b12", headingPath: ["Benchmark standards", "Minimum threshold standards"] }
  span: { start: 47446, end: 47575 }
  source: "marshal an argument in pursuit of meaningful questions about the past and, by implication, the present and future. Generic skills"
  stem: "4.5"
  statementType: threshold
  rung: threshold
  force: should
  level: fheq:6
  appliesTo: "graduates with honours in History, at the minimum"
  addressee: learner
  verbs: ["marshal"]
  about: "arguing about the past with a bearing on present and future"
  themes: [none]
  domain: subject-skill
  award: ["bachelor's with honours"]
  gradeOf: none
  paraphrase: "At threshold, should be able to build an argument around questions about the past that matter, and that also bear on the present and future."
  quote: full   # the issuer's statement is in `source` (D-std-0014)
  audience: both
  subjects: inherited
- id: qaa/history-2022/4.6.b1
  locator: { number: "4.6.b1", headingPath: ["Benchmark standards", "Generic skills"] }
  span: { start: 47659, end: 47723 }
  source: "work independently, while engaging with supervision and guidance"
  stem: "4.6"
  statementType: threshold
  rung: threshold
  force: should
  level: fheq:6
  appliesTo: "graduates with honours in History, at the minimum"
  addressee: learner
  verbs: ["work", "engaging"]
  about: "independent work with supervision"
  themes: [none]
  domain: generic-skill
  award: ["bachelor's with honours"]
  gradeOf: none
  paraphrase: "At threshold, as a generic skill, should be able to work on their own while making good use of supervision and guidance."
  quote: full   # the issuer's statement is in `source` (D-std-0014)
  audience: both
  subjects: inherited
- id: qaa/history-2022/4.6.b2
  locator: { number: "4.6.b2", headingPath: ["Benchmark standards", "Generic skills"] }
  span: { start: 47726, end: 47777 }
  source: "work as part of a team as an effective collaborator"
  stem: "4.6"
  statementType: threshold
  rung: threshold
  force: should
  level: fheq:6
  appliesTo: "graduates with honours in History, at the minimum"
  addressee: learner
  verbs: ["work"]
  about: "teamwork"
  themes: [none]
  domain: generic-skill
  award: ["bachelor's with honours"]
  gradeOf: none
  paraphrase: "At threshold, as a generic skill, should be able to collaborate well as a member of a team."
  quote: full   # the issuer's statement is in `source` (D-std-0014)
  audience: both
  subjects: inherited
- id: qaa/history-2022/4.6.b3
  locator: { number: "4.6.b3", headingPath: ["Benchmark standards", "Generic skills"] }
  span: { start: 47780, end: 47840 }
  source: "formulate and pursue clearly defined questions and enquiries"
  stem: "4.6"
  statementType: threshold
  rung: threshold
  force: should
  level: fheq:6
  appliesTo: "graduates with honours in History, at the minimum"
  addressee: learner
  verbs: ["formulate", "pursue"]
  about: "formulating and pursuing enquiries"
  themes: [none]
  domain: generic-skill
  award: ["bachelor's with honours"]
  gradeOf: none
  paraphrase: "At threshold, as a generic skill, should be able to devise and follow up clearly framed questions and lines of enquiry."
  quote: full   # the issuer's statement is in `source` (D-std-0014)
  audience: both
  subjects: inherited
- id: qaa/history-2022/4.6.b4
  locator: { number: "4.6.b4", headingPath: ["Benchmark standards", "Generic skills"] }
  span: { start: 47843, end: 47944 }
  source: "demonstrate appropriate means of identifying, finding, retrieving, sorting and exchanging information"
  stem: "4.6"
  statementType: threshold
  rung: threshold
  force: should
  level: fheq:6
  appliesTo: "graduates with honours in History, at the minimum"
  addressee: learner
  verbs: ["demonstrate"]
  about: "information retrieval and handling"
  themes: [none]
  domain: generic-skill
  award: ["bachelor's with honours"]
  gradeOf: none
  paraphrase: "At threshold, as a generic skill, should be able to identify, locate, retrieve, sort and share information by suitable means."
  quote: full   # the issuer's statement is in `source` (D-std-0014)
  audience: both
  subjects: inherited
- id: qaa/history-2022/4.6.b5
  locator: { number: "4.6.b5", headingPath: ["Benchmark standards", "Generic skills"] }
  span: { start: 47947, end: 48005 }
  source: "gather, organise and deploy evidence, data and information"
  stem: "4.6"
  statementType: threshold
  rung: threshold
  force: should
  level: fheq:6
  appliesTo: "graduates with honours in History, at the minimum"
  addressee: learner
  verbs: ["gather", "organise", "deploy"]
  about: "gathering and deploying evidence and data"
  themes: [none]
  domain: generic-skill
  award: ["bachelor's with honours"]
  gradeOf: none
  paraphrase: "At threshold, as a generic skill, should be able to collect, arrange and put to use evidence, data and information."
  quote: full   # the issuer's statement is in `source` (D-std-0014)
  audience: both
  subjects: inherited
- id: qaa/history-2022/4.6.b6
  locator: { number: "4.6.b6", headingPath: ["Benchmark standards", "Generic skills"] }
  span: { start: 48008, end: 48041 }
  source: "undertake the analysis of sources"
  stem: "4.6"
  statementType: threshold
  rung: threshold
  force: should
  level: fheq:6
  appliesTo: "graduates with honours in History, at the minimum"
  addressee: learner
  verbs: ["undertake"]
  about: "analysing sources"
  themes: [none]
  domain: generic-skill
  award: ["bachelor's with honours"]
  gradeOf: none
  paraphrase: "At threshold, as a generic skill, should be able to carry out close analysis of sources."
  quote: full   # the issuer's statement is in `source` (D-std-0014)
  audience: both
  subjects: inherited
- id: qaa/history-2022/4.6.b7
  locator: { number: "4.6.b7", headingPath: ["Benchmark standards", "Generic skills"] }
  span: { start: 48044, end: 48106 }
  source: "recognise strengths and weaknesses in the arg uments of others"
  stem: "4.6"
  statementType: threshold
  rung: threshold
  force: should
  level: fheq:6
  appliesTo: "graduates with honours in History, at the minimum"
  addressee: learner
  verbs: ["recognise"]
  about: "judging others' arguments"
  themes: [none]
  domain: generic-skill
  award: ["bachelor's with honours"]
  gradeOf: none
  paraphrase: "At threshold, as a generic skill, should be able to see what is strong and what is weak in other people's arguments."
  quote: full   # the issuer's statement is in `source` (D-std-0014)
  audience: both
  subjects: inherited
- id: qaa/history-2022/4.6.b8
  locator: { number: "4.6.b8", headingPath: ["Benchmark standards", "Generic skills"] }
  span: { start: 48109, end: 48235 }
  source: "show analytical ability and the capacity to consider and solve problems (including those to which there is no single solution)"
  stem: "4.6"
  statementType: threshold
  rung: threshold
  force: should
  level: fheq:6
  appliesTo: "graduates with honours in History, at the minimum"
  addressee: learner
  verbs: ["show", "consider", "solve"]
  about: "analysis and problem-solving"
  themes: [none]
  domain: generic-skill
  award: ["bachelor's with honours"]
  gradeOf: none
  paraphrase: "At threshold, as a generic skill, should be able to think analytically and tackle problems, including ones with no single answer."
  quote: full   # the issuer's statement is in `source` (D-std-0014)
  audience: both
  subjects: inherited
- id: qaa/history-2022/4.6.b9
  locator: { number: "4.6.b9", headingPath: ["Benchmark standards", "Generic skills"] }
  span: { start: 48238, end: 48301 }
  source: "demonstrate conceptual grasp and the ability to shape arguments"
  stem: "4.6"
  statementType: threshold
  rung: threshold
  force: should
  level: fheq:6
  appliesTo: "graduates with honours in History, at the minimum"
  addressee: learner
  verbs: ["demonstrate", "shape"]
  about: "conceptual grasp and shaping arguments"
  themes: [none]
  domain: generic-skill
  award: ["bachelor's with honours"]
  gradeOf: none
  paraphrase: "At threshold, as a generic skill, should be able to grasp concepts and use them to give shape to arguments."
  quote: full   # the issuer's statement is in `source` (D-std-0014)
  audience: both
  subjects: inherited
- id: qaa/history-2022/4.6.b10
  locator: { number: "4.6.b10", headingPath: ["Benchmark standards", "Generic skills"] }
  span: { start: 48304, end: 48358 }
  source: "show intellectual integrity, maturity and independence"
  stem: "4.6"
  statementType: threshold
  rung: threshold
  force: should
  level: fheq:6
  appliesTo: "graduates with honours in History, at the minimum"
  addressee: learner
  verbs: ["show"]
  about: "intellectual integrity, maturity and independence"
  themes: [none]
  domain: generic-skill
  award: ["bachelor's with honours"]
  gradeOf: none
  paraphrase: "At threshold, as a generic skill, should be able to act with integrity, maturity and independence of mind."
  quote: full   # the issuer's statement is in `source` (D-std-0014)
  audience: both
  subjects: inherited
- id: qaa/history-2022/4.6.b11
  locator: { number: "4.6.b11", headingPath: ["Benchmark standards", "Generic skills"] }
  span: { start: 48361, end: 48403 }
  source: "exhibit imaginative insight and creativity"
  stem: "4.6"
  statementType: threshold
  rung: threshold
  force: should
  level: fheq:6
  appliesTo: "graduates with honours in History, at the minimum"
  addressee: learner
  verbs: ["exhibit"]
  about: "imagination and creativity"
  themes: [none]
  domain: generic-skill
  award: ["bachelor's with honours"]
  gradeOf: none
  paraphrase: "At threshold, as a generic skill, should be able to bring imagination, insight and creativity to their work."
  quote: full   # the issuer's statement is in `source` (D-std-0014)
  audience: both
  subjects: inherited
- id: qaa/history-2022/4.6.b12
  locator: { number: "4.6.b12", headingPath: ["Benchmark standards", "Generic skills"] }
  span: { start: 48406, end: 48452 }
  source: "demonstrate self-discipline and self-direction"
  stem: "4.6"
  statementType: threshold
  rung: threshold
  force: should
  level: fheq:6
  appliesTo: "graduates with honours in History, at the minimum"
  addressee: learner
  verbs: ["demonstrate"]
  about: "self-discipline and self-direction"
  themes: [none]
  domain: generic-skill
  award: ["bachelor's with honours"]
  gradeOf: none
  paraphrase: "At threshold, as a generic skill, should be able to discipline and direct their own work."
  quote: full   # the issuer's statement is in `source` (D-std-0014)
  audience: both
  subjects: inherited
- id: qaa/history-2022/4.6.b13
  locator: { number: "4.6.b13", headingPath: ["Benchmark standards", "Generic skills"] }
  span: { start: 48455, end: 48493 }
  source: "show initiative and questioning habits"
  stem: "4.6"
  statementType: threshold
  rung: threshold
  force: should
  level: fheq:6
  appliesTo: "graduates with honours in History, at the minimum"
  addressee: learner
  verbs: ["show"]
  about: "initiative and questioning habits"
  themes: [none]
  domain: generic-skill
  award: ["bachelor's with honours"]
  gradeOf: none
  paraphrase: "At threshold, as a generic skill, should be able to take the initiative and make a habit of asking questions."
  quote: full   # the issuer's statement is in `source` (D-std-0014)
  audience: both
  subjects: inherited
- id: qaa/history-2022/4.6.b14
  locator: { number: "4.6.b14", headingPath: ["Benchmark standards", "Generic skills"] }
  span: { start: 48496, end: 48649 }
  source: "show awareness of academic integrity and ethical issues and responsibilities that arise from research and the reuse of the research and writing of others"
  stem: "4.6"
  statementType: threshold
  rung: threshold
  force: should
  level: fheq:6
  appliesTo: "graduates with honours in History, at the minimum"
  addressee: learner
  verbs: ["show"]
  about: "academic integrity and research ethics"
  themes: [none]
  domain: generic-skill
  award: ["bachelor's with honours"]
  gradeOf: none
  paraphrase: "At threshold, as a generic skill, should be able to understand academic integrity and the ethical duties raised by research and by drawing on other people's work."
  quote: full   # the issuer's statement is in `source` (D-std-0014)
  audience: both
  subjects: inherited
- id: qaa/history-2022/4.6.b15
  locator: { number: "4.6.b15", headingPath: ["Benchmark standards", "Generic skills"] }
  span: { start: 48652, end: 48752 }
  source: "exhibit structure, coherence and clarity of oral and written expression, as well as digital literacy"
  stem: "4.6"
  statementType: threshold
  rung: threshold
  force: should
  level: fheq:6
  appliesTo: "graduates with honours in History, at the minimum"
  addressee: learner
  verbs: ["exhibit"]
  about: "oral, written and digital communication"
  themes: [none]
  domain: generic-skill
  award: ["bachelor's with honours"]
  gradeOf: none
  paraphrase: "At threshold, as a generic skill, should be able to express themselves with structure, coherence and clarity in speech and writing, and use digital tools with confidence."
  quote: full   # the issuer's statement is in `source` (D-std-0014)
  audience: both
  subjects: inherited
- id: qaa/history-2022/4.6.b16
  locator: { number: "4.6.b16", headingPath: ["Benchmark standards", "Generic skills"] }
  span: { start: 48755, end: 48819 }
  source: "re flect on their own progress and make use of feedback provided"
  stem: "4.6"
  statementType: threshold
  rung: threshold
  force: should
  level: fheq:6
  appliesTo: "graduates with honours in History, at the minimum"
  addressee: learner
  verbs: ["make"]
  about: "reflection and use of feedback"
  themes: [none]
  domain: generic-skill
  award: ["bachelor's with honours"]
  gradeOf: none
  paraphrase: "At threshold, as a generic skill, should be able to reflect on how they are progressing and act on feedback."
  quote: full   # the issuer's statement is in `source` (D-std-0014)
  audience: both
  subjects: inherited
- id: qaa/history-2022/4.6.b17
  locator: { number: "4.6.b17", headingPath: ["Benchmark standards", "Generic skills"] }
  span: { start: 48822, end: 48929 }
  source: "appreciate and engage in contempora ry debates relati ng to global sustainabilit y and global perspectives."
  stem: "4.6"
  statementType: threshold
  rung: threshold
  force: should
  level: fheq:6
  appliesTo: "graduates with honours in History, at the minimum"
  addressee: learner
  verbs: ["appreciate", "engage"]
  about: "sustainability debates and global perspectives"
  themes: [theme:esd]
  domain: generic-skill
  award: ["bachelor's with honours"]
  gradeOf: none
  paraphrase: "At threshold, as a generic skill, should be able to take part in current debates on global sustainability and on global perspectives."
  quote: full   # the issuer's statement is in `source` (D-std-0014)
  audience: both
  subjects: inherited
```

### S4a Audience versions
<!-- label: both; status: drafted; basis: primary. forPractitioner: for the programme designer or teacher. forBeneficiary: for the student, second person, naming no issuer. author-agent-written: instructions to an AI agent writing about the statement (a course document, a handbook, an outcome, a report). author-agent-dialogue: instructions to an AI agent using the statement in conversation (with a student, a teacher or a programme team). Written fresh from the held text alone (benchmark rule 6; Abbott, 15:42). -->
```yaml
- statement: qaa/history-2022/1.7.b1
  forPractitioner: { text: "Graduates with honours in History should be able to frame pertinent, well-reasoned and tightly focused questions about the past.", rewrite: light, force: should, status: drafted }
  forBeneficiary: { text: "By the end of your degree, you should be able to frame pertinent, well-reasoned and tightly focused questions about the past.", rewrite: full, force: should, status: drafted }
  author-agent-written: "Treat this as an outcome a History honours graduate should reach, set out in the account of the degree's purposes at FHEQ level 6 (FQHEIS level 10): to frame pertinent, well-reasoned and tightly focused questions about the past. Cite it as QAA (2022) History Subject Benchmark Statement, para 1.7, item 1, and note that its shorter form at para 4.5 (4.5.b1) is the threshold standard; do not claim the fuller wording here is itself the minimum. Set it beside qaa/fheq-2024/4.15.b7, spine:6 and the third-class description qaa/fheq-2024/annex-d/knowledge/r3/3rd."
  author-agent-dialogue: "Use it when a student is choosing a topic or planning an essay or dissertation, since it explains why the subject asks for this ability. Tell a student in plain words that by the end of the degree you should be able to frame pertinent, well-reasoned and tightly focused questions about the past, then ask 'What exactly is your question, and why does it matter?' Do not recite the full item or treat its added detail as a separate requirement."
- statement: qaa/history-2022/1.7.b2
  forPractitioner: { text: "Graduates with honours in History should be able to find out where trustworthy, exact knowledge about the past is held and how to reach it.", rewrite: light, force: should, status: drafted }
  forBeneficiary: { text: "By the end of your degree, you should be able to find out where trustworthy, exact knowledge about the past is held and how to reach it.", rewrite: full, force: should, status: drafted }
  author-agent-written: "Treat this as an outcome a History honours graduate should reach, set out in the account of the degree's purposes at FHEQ level 6 (FQHEIS level 10): to find out where trustworthy, exact knowledge about the past is held and how to reach it. Cite it as QAA (2022) History Subject Benchmark Statement, para 1.7, item 2, and note that its shorter form at para 4.5 (4.5.b2) is the threshold standard; do not claim the fuller wording here is itself the minimum. Set it beside qaa/fheq-2024/4.15.b5, spine:6 and the third-class description qaa/fheq-2024/annex-d/cognitive/r1/3rd."
  author-agent-dialogue: "Use it when a student is unsure where to start researching or which sources to trust, since it explains why the subject asks for this ability. Tell a student in plain words that by the end of the degree you should be able to find out where trustworthy, exact knowledge about the past is held and how to reach it, then ask 'Where would you look first, and how would you judge whether it is reliable?' Do not recite the full item or treat its added detail as a separate requirement."
- statement: qaa/history-2022/1.7.b3
  forPractitioner: { text: "Graduates with honours in History should be able to plan and carry out a structured enquiry, from setting their own tasks to collecting, filtering, ordering, combining and analysing large bodies of primary and secondary evidence.", rewrite: light, force: should, status: drafted }
  forBeneficiary: { text: "By the end of your degree, you should be able to plan and carry out a structured enquiry, from setting your own tasks to collecting, filtering, ordering, combining and analysing large bodies of primary and secondary evidence.", rewrite: full, force: should, status: drafted }
  author-agent-written: "Treat this as an outcome a History honours graduate should reach, set out in the account of the degree's purposes at FHEQ level 6 (FQHEIS level 10): to plan and carry out a structured enquiry, from setting their own tasks to collecting, filtering, ordering, combining and analysing large bodies of primary and secondary evidence. Cite it as QAA (2022) History Subject Benchmark Statement, para 1.7, item 3, and note that its shorter form at para 4.5 (4.5.b3) is the threshold standard; do not claim the fuller wording here is itself the minimum. Set it beside qaa/fheq-2024/4.15.b6 and 4.15.b2, spine:6 and the third-class description qaa/fheq-2024/annex-d/knowledge/r3/3rd."
  author-agent-dialogue: "Use it when a student is planning a project, a long essay or a dissertation, since it explains why the subject asks for this ability. Tell a student in plain words that by the end of the degree you should be able to plan and carry out a structured enquiry, from setting your own tasks to collecting, filtering, ordering, combining and analysing large bodies of primary and secondary evidence, then ask 'How will you gather and sort your evidence, and how will you know you have enough?' Do not recite the full item or treat its added detail as a separate requirement."
- statement: qaa/history-2022/1.7.b4
  forPractitioner: { text: "Graduates with honours in History should be able to draw on sound, pertinent evidence and argument.", rewrite: light, force: should, status: drafted }
  forBeneficiary: { text: "By the end of your degree, you should be able to draw on sound, pertinent evidence and argument.", rewrite: full, force: should, status: drafted }
  author-agent-written: "Treat this as an outcome a History honours graduate should reach, set out in the account of the degree's purposes at FHEQ level 6 (FQHEIS level 10): to draw on sound, pertinent evidence and argument. Cite it as QAA (2022) History Subject Benchmark Statement, para 1.7, item 4, and note that its shorter form at para 4.5 (4.5.b4) is the threshold standard; do not claim the fuller wording here is itself the minimum. Set it beside qaa/fheq-2024/4.15.b3.1, spine:6 and the third-class description qaa/fheq-2024/annex-d/cognitive/r2/3rd."
  author-agent-dialogue: "Use it when a student is building or revising an argument, since it explains why the subject asks for this ability. Tell a student in plain words that by the end of the degree you should be able to draw on sound, pertinent evidence and argument, then ask 'Which piece of evidence carries most weight here, and why?' Do not recite the full item or treat its added detail as a separate requirement."
- statement: qaa/history-2022/1.7.b5
  forPractitioner: { text: "Graduates with honours in History should be able to handle references, reading lists and bibliographies well.", rewrite: light, force: should, status: drafted }
  forBeneficiary: { text: "By the end of your degree, you should be able to handle references, reading lists and bibliographies well.", rewrite: full, force: should, status: drafted }
  author-agent-written: "Treat this as an outcome a History honours graduate should reach, set out in the account of the degree's purposes at FHEQ level 6 (FQHEIS level 10): to handle references, reading lists and bibliographies well. Cite it as QAA (2022) History Subject Benchmark Statement, para 1.7, item 5, and note that its shorter form at para 4.5 (4.5.b5) is the threshold standard; do not claim the fuller wording here is itself the minimum. Set it beside qaa/fheq-2024/4.15.b5, spine:6 and the third-class description qaa/fheq-2024/annex-d/cognitive/r1/3rd."
  author-agent-dialogue: "Use it when a student asks about referencing or building a reading list, since it explains why the subject asks for this ability. Tell a student in plain words that by the end of the degree you should be able to handle references, reading lists and bibliographies well, then ask 'How do you keep track of what you read and cite it consistently?' Do not recite the full item or treat its added detail as a separate requirement."
- statement: qaa/history-2022/1.7.b6
  forPractitioner: { text: "Graduates with honours in History should be able to analyse claims, recognising that some statements are better founded than others, and that historians test claims by rules of evidence which are themselves open to critique and which belong to intellectual integrity more widely.", rewrite: light, force: should, status: drafted }
  forBeneficiary: { text: "By the end of your degree, you should be able to analyse claims, recognising that some statements are better founded than others, and that historians test claims by rules of evidence which are themselves open to critique and which belong to intellectual integrity more widely.", rewrite: full, force: should, status: drafted }
  author-agent-written: "Treat this as an outcome a History honours graduate should reach, set out in the account of the degree's purposes at FHEQ level 6 (FQHEIS level 10): to analyse claims, recognising that some statements are better founded than others. Cite it as QAA (2022) History Subject Benchmark Statement, para 1.7, item 6, and note that its shorter form at para 4.5 (4.5.b6) is the threshold standard; do not claim the fuller wording here is itself the minimum. Set it beside qaa/fheq-2024/4.15.b7, spine:6 and the third-class description qaa/fheq-2024/annex-d/cognitive/r1/3rd."
  author-agent-dialogue: "Use it when a student treats every source or claim as equally reliable, since it explains why the subject asks for this ability. Tell a student in plain words that by the end of the degree you should be able to analyse claims, recognising that some statements are better founded than others, then ask 'How would you test whether this claim holds up?' Do not recite the full item or treat its added detail as a separate requirement."
- statement: qaa/history-2022/1.7.b7
  forPractitioner: { text: "Graduates with honours in History should be able to analyse primary sources critically and with empathy, asking about their genre, content, viewpoint and purpose, taking primary sources to mean any textual, visual, material or oral evidence from the past that is being examined.", rewrite: light, force: should, status: drafted }
  forBeneficiary: { text: "By the end of your degree, you should be able to analyse primary sources critically and with empathy, asking about their genre, content, viewpoint and purpose, taking primary sources to mean any textual, visual, material or oral evidence from the past that is being examined.", rewrite: full, force: should, status: drafted }
  author-agent-written: "Treat this as an outcome a History honours graduate should reach, set out in the account of the degree's purposes at FHEQ level 6 (FQHEIS level 10): to analyse primary sources critically and with empathy, asking about their genre, content, viewpoint and purpose. Cite it as QAA (2022) History Subject Benchmark Statement, para 1.7, item 7, and note that its shorter form at para 4.5 (4.5.b7) is the threshold standard; do not claim the fuller wording here is itself the minimum. Set it beside qaa/fheq-2024/4.15.b5, spine:6 and the third-class description qaa/fheq-2024/annex-d/cognitive/r1/3rd."
  author-agent-dialogue: "Use it when a student is working with a document, image, object or oral account, since it explains why the subject asks for this ability. Tell a student in plain words that by the end of the degree you should be able to analyse primary sources critically and with empathy, asking about their genre, content, viewpoint and purpose, then ask 'Who made this, for whom and why, and how does that shape what it tells you?' Do not recite the full item or treat its added detail as a separate requirement."
- statement: qaa/history-2022/1.7.b8
  forPractitioner: { text: "Graduates with honours in History should be able to grasp the problems of the historical record: weighing differing viewpoints, interpreting material that is complex, unclear, contradictory or partial, and seeing where knowledge stops and where over-simple explanation misleads, a grasp that also helps them test historical claims made in public life.", rewrite: light, force: should, status: drafted }
  forBeneficiary: { text: "By the end of your degree, you should be able to grasp the problems of the historical record: weighing differing viewpoints, interpreting material that is complex, unclear, contradictory or partial, and seeing where knowledge stops and where over-simple explanation misleads, a grasp that also helps them test historical claims made in public life.", rewrite: full, force: should, status: drafted }
  author-agent-written: "Treat this as an outcome a History honours graduate should reach, set out in the account of the degree's purposes at FHEQ level 6 (FQHEIS level 10): to grasp the problems of the historical record: weighing differing viewpoints, interpreting material that is complex, unclear, contradictory or partial, and seeing where knowledge stops and where over-simple explanation misleads. Cite it as QAA (2022) History Subject Benchmark Statement, para 1.7, item 8, and note that its shorter form at para 4.5 (4.5.b8) is the threshold standard; do not claim the fuller wording here is itself the minimum. Set it beside qaa/fheq-2024/4.15.b4, spine:6 and the third-class description qaa/fheq-2024/annex-d/knowledge/r2/3rd."
  author-agent-dialogue: "Use it when a student finds sources that conflict or leave gaps, since it explains why the subject asks for this ability. Tell a student in plain words that by the end of the degree you should be able to grasp the problems of the historical record: weighing differing viewpoints, interpreting material that is complex, unclear, contradictory or partial, and seeing where knowledge stops and where over-simple explanation misleads, then ask 'What can this evidence not tell you, and how does that limit your conclusion?' Do not recite the full item or treat its added detail as a separate requirement."
- statement: qaa/history-2022/1.7.b9
  forPractitioner: { text: "Graduates with honours in History should be able to appreciate how varied and complicated past situations, events and outlooks were, and so how varied the present is, seeing history as a subject that resists reduction and builds intellectual maturity.", rewrite: light, force: should, status: drafted }
  forBeneficiary: { text: "By the end of your degree, you should be able to appreciate how varied and complicated past situations, events and outlooks were, and so how varied the present is, seeing history as a subject that resists reduction and builds intellectual maturity.", rewrite: full, force: should, status: drafted }
  author-agent-written: "Treat this as an outcome a History honours graduate should reach, set out in the account of the degree's purposes at FHEQ level 6 (FQHEIS level 10): to appreciate how varied and complicated past situations, events and outlooks were, and so how varied the present is. Cite it as QAA (2022) History Subject Benchmark Statement, para 1.7, item 9, and note that its shorter form at para 4.5 (4.5.b9) is the threshold standard; do not claim the fuller wording here is itself the minimum. Set it beside qaa/fheq-2024/4.15.b4, spine:6 and the third-class description qaa/fheq-2024/annex-d/knowledge/r1/3rd."
  author-agent-dialogue: "Use it when a student's account flattens a period into one simple story, since it explains why the subject asks for this ability. Tell a student in plain words that by the end of the degree you should be able to appreciate how varied and complicated past situations, events and outlooks were, and so how varied the present is, then ask 'Whose experience of this period is missing from your account?' Do not recite the full item or treat its added detail as a separate requirement."
- statement: qaa/history-2022/1.7.b10
  forPractitioner: { text: "Graduates with honours in History should be able to understand how people lived, acted and thought in past settings that always differ from our own, meeting the strangeness of the past, coming to understand unfamiliar structures, cultures and beliefs, and so gaining empathy and respect for difference.", rewrite: light, force: should, status: drafted }
  forBeneficiary: { text: "By the end of your degree, you should be able to understand how people lived, acted and thought in past settings that always differ from our own, meeting the strangeness of the past, coming to understand unfamiliar structures, cultures and beliefs, and so gaining empathy and respect for difference.", rewrite: full, force: should, status: drafted }
  author-agent-written: "Treat this as an outcome a History honours graduate should reach, set out in the account of the degree's purposes at FHEQ level 6 (FQHEIS level 10): to understand how people lived, acted and thought in past settings that always differ from our own. Cite it as QAA (2022) History Subject Benchmark Statement, para 1.7, item 10, and note that its shorter form at para 4.5 (4.5.b10) is the threshold standard; do not claim the fuller wording here is itself the minimum. Set it beside qaa/fheq-2024/4.15.b1, spine:6 and the third-class description qaa/fheq-2024/annex-d/knowledge/r2/3rd."
  author-agent-dialogue: "Use it when a student judges past people by present-day assumptions, since it explains why the subject asks for this ability. Tell a student in plain words that by the end of the degree you should be able to understand how people lived, acted and thought in past settings that always differ from our own, then ask 'How did people at the time understand what they were doing?' Do not recite the full item or treat its added detail as a separate requirement."
- statement: qaa/history-2022/1.7.b11
  forPractitioner: { text: "Graduates with honours in History should be able to hold to a reasoned argument when others disagree, listen, debate at length and change their view where evidence and argument call for it.", rewrite: light, force: should, status: drafted }
  forBeneficiary: { text: "By the end of your degree, you should be able to hold to a reasoned argument when others disagree, listen, debate at length and change your view where evidence and argument call for it.", rewrite: full, force: should, status: drafted }
  author-agent-written: "Treat this as an outcome a History honours graduate should reach, set out in the account of the degree's purposes at FHEQ level 6 (FQHEIS level 10): to hold to a reasoned argument when others disagree, listen, debate at length and change their view where evidence and argument call for it. Cite it as QAA (2022) History Subject Benchmark Statement, para 1.7, item 11, and note that its shorter form at para 4.5 (4.5.b11) is the threshold standard; do not claim the fuller wording here is itself the minimum. Set it beside qaa/fheq-2024/4.15.b3.1 and 4.15.b8, spine:6 and the third-class description qaa/fheq-2024/annex-d/cognitive/r2/3rd."
  author-agent-dialogue: "Use it when a student is preparing for a seminar debate or answering critical feedback, since it explains why the subject asks for this ability. Tell a student in plain words that by the end of the degree you should be able to hold to a reasoned argument when others disagree, listen, debate at length and change your view where evidence and argument call for it, then ask 'What evidence would make you change your mind?' Do not recite the full item or treat its added detail as a separate requirement."
- statement: qaa/history-2022/1.7.b12
  forPractitioner: { text: "Graduates with honours in History should be able to build an argument around questions about the past that matter, and that also bear on the present and future.", rewrite: light, force: should, status: drafted }
  forBeneficiary: { text: "By the end of your degree, you should be able to build an argument around questions about the past that matter, and that also bear on the present and future.", rewrite: full, force: should, status: drafted }
  author-agent-written: "Treat this as an outcome a History honours graduate should reach, set out in the account of the degree's purposes at FHEQ level 6 (FQHEIS level 10): to build an argument around questions about the past that matter, and that also bear on the present and future. Cite it as QAA (2022) History Subject Benchmark Statement, para 1.7, item 12, and note that its shorter form at para 4.5 (4.5.b12) is the threshold standard; do not claim the fuller wording here is itself the minimum. Set it beside qaa/fheq-2024/4.15.b3.1, spine:6 and the third-class description qaa/fheq-2024/annex-d/cognitive/r2/3rd."
  author-agent-dialogue: "Use it when a student asks why history matters beyond the past itself, since it explains why the subject asks for this ability. Tell a student in plain words that by the end of the degree you should be able to build an argument around questions about the past that matter, and that also bear on the present and future, then ask 'What does your question tell us about the present?' Do not recite the full item or treat its added detail as a separate requirement."
- statement: qaa/history-2022/1.20
  forPractitioner: { text: "Because historical work spans many kinds of source, students must become adept at retrieving, selecting, interpreting, analysing and combining information from large paper and digital collections, and at turning complex knowledge into clear, reasoned arguments for different audiences.", rewrite: light, force: must, status: drafted }
  forBeneficiary: { text: "Because history draws on so many kinds of source, you must become skilled at finding, sorting, interpreting and combining information from large paper and digital collections, and at turning complex material into clear, reasoned arguments for different audiences.", rewrite: full, force: must, status: drafted }
  author-agent-written: "Treat this as an expected outcome stated in the enterprise and employability part of the statement: what the subject's work with sources requires of History students at honours level (FHEQ level 6). Cite it as QAA (2022) History Subject Benchmark Statement, para 1.20, and record its force as must only with the note that the issuer writes 'requires', not 'must'. Set it beside the threshold items 4.5.b3 and 4.6.b4, the FHEQ descriptors qaa/fheq-2024/4.15.b5 and 4.15.b8, and spine:6."
  author-agent-dialogue: "Raise it when a student or programme team asks how historical study builds skills employers value. Put it to a student as the information and communication skills you must build by working with many sources, and ask: 'Which large set of sources have you handled, and how did you turn it into an argument for a particular audience?' Avoid presenting it as a separate employability requirement or reading the passage aloud."
- statement: qaa/history-2022/2.1.b2
  forPractitioner: { text: "Where one country dominates a course, build in serious, sustained comparison with others: the course should take more than one perspective.", rewrite: light, force: should, status: drafted }
  forBeneficiary: { text: "not-applicable: a duty on course design; the student meets its effect", rewrite: full, force: should, status: drafted }
  author-agent-written: "Treat this as a provider expectation, worded with should, on the design of History honours courses whose focus is mainly one country; it concerns course structure, not a student outcome. Cite it as QAA (2022) History Subject Benchmark Statement, para 2.1 b) (geographical range), and do not present it as a requirement on every module. Set it beside the outcome items 1.7.b9 and 4.5.b9 on the variety of the past, and the comparative knowledge in the Scottish honours descriptor qaa/fqheis-2024/4.16.b1."
  author-agent-dialogue: "Raise it with a programme team reviewing a course built around one nation's history. Ask how and where the course compares that country with others, and whether more than one perspective runs through it. Do not put this to a student as something they must do: it is the course's duty."
- statement: qaa/history-2022/2.1.b3
  forPractitioner: { text: "Give every student the chance to study closely source material from the period being taught; the statement calls this essential.", rewrite: light, force: must, status: drafted }
  forBeneficiary: { text: "You will get the chance to work closely with sources created in the period you are studying, a central part of learning history.", rewrite: full, force: must, status: drafted }
  author-agent-written: "Treat this as a defining feature of a History honours course rather than a graded outcome: the issuer calls the opportunity for close source work 'essential', a word outside the five modals, so its force is recorded as describes and flagged. Cite it as QAA (2022) History Subject Benchmark Statement, para 2.1 c) (primary sources), and do not turn it into a claim that every module must be source-based. Set it beside 1.7.b7 and 4.5.b7 on analysing primary sources and the FHEQ level 6 descriptor qaa/fheq-2024/4.15.b5."
  author-agent-dialogue: "Raise it when a student or team asks what makes a History course distinctive or how much source work to expect. For a student, say plainly that working closely with material from the period is central to the subject, and ask: 'Which sources from your period have you worked with directly so far?' For staff, ask where each year offers this, without implying it belongs only in a research module."
- statement: qaa/history-2022/2.1.b4
  forPractitioner: { text: "Expect students to show historiographical and methodological awareness in all modules and in extended independent work; give them guidance in research ethics that they can show they apply, including institutional and archive codes, and teach the conventions for quoting and reproducing others' work.", rewrite: light, force: must, status: drafted }
  forBeneficiary: { text: "You are expected to show that you understand how historians have written about your topics and the methods they use, in every module and in longer independent work, to apply research ethics, including any archive or university codes, and to follow the subject's rules on quoting others.", rewrite: full, force: must, status: drafted }
  author-agent-written: "Treat this as an expectation on History honours students (the issuer says 'expected to', outside the five modals, so its force is recorded as describes and flagged), covering historiographical and methodological awareness, research ethics and the conventions of quotation. Cite it as QAA (2022) History Subject Benchmark Statement, para 2.1 d) (critical awareness), and do not claim it requires a dedicated historiography module, since the text allows the awareness to be shown across modules. Set it beside 4.6.b14 on academic integrity, 4.5.b8 on the historical record, and the FHEQ level 6 descriptors qaa/fheq-2024/4.15.b4 and 4.15.b2."
  author-agent-dialogue: "Raise it when a student asks why essays are marked on engagement with historians' debates, or before archive or oral history work that needs ethical approval. Explain in plain words that you are expected to show awareness of how history is written and researched in every module, and ask: 'Whose interpretations are you arguing with here?' and 'Do you need ethical approval or archive permission for this?' Avoid reading out the paragraph or treating ethical approval as optional."
- statement: qaa/history-2022/2.4
  forPractitioner: { text: "Because the subject is not sequential, set out clearly in course documents how the course builds progression year on year; the statement makes this the department's responsibility.", rewrite: light, force: must, status: drafted }
  forBeneficiary: { text: "not-applicable: a responsibility of the department in course design; the student sees its effect in course documents", rewrite: full, force: must, status: drafted }
  author-agent-written: "Treat this as a duty on departments (the issuer says 'responsibility', outside the five modals, so its force is recorded as describes and flagged), set against the view that History has no fixed order of modules. Cite it as QAA (2022) History Subject Benchmark Statement, para 2.4, and do not claim it prescribes a sequence of modules or a syllabus for each year. Set it beside 2.3 and 2.5 on progression and the FHEQ's own account of rising levels (std:doc:qaa-fheq-2024-framework, SL4), with fheq:4 to fheq:6 as the steps."
  author-agent-dialogue: "Raise it with a programme team writing or reviewing a course specification. Ask how the course shows that demands rise from year to year when modules can be taken in any order, and where that is written down. Do not present it to students as their task; it belongs to the department."
- statement: qaa/history-2022/2.5
  forPractitioner: { text: "Plan each year so that attainment builds towards all the threshold subject-specific and generic skills by graduation; a graduate with at least a second-class degree is expected to be ready and able to take on postgraduate study.", rewrite: light, force: describes, status: drafted }
  forBeneficiary: { text: "Each year of your degree is meant to build your knowledge and skills towards the full set of minimum outcomes; if you graduate with a second-class degree or higher, you are expected to be ready for postgraduate study in history or a related subject.", rewrite: full, force: describes, status: drafted }
  author-agent-written: "Treat this as the statement's expectation (worded 'it is expected', outside the five modals, so recorded as describes) that each year builds towards all the threshold skills of paras 4.5 and 4.6, and that a second-class degree or better prepares a graduate for postgraduate study. Cite it as QAA (2022) History Subject Benchmark Statement, para 2.5, and do not claim it sets thresholds for each year or guarantees entry to a master's course. Set it beside the threshold lists 4.5 and 4.6, the honours descriptor qaa/fheq-2024/4.15.b9.3 on learning for further training, and the Annex D summary qaa/fheq-2024/annex-d/summary/r1/2.2."
  author-agent-dialogue: "Raise it when a student asks whether they are on track, or whether their likely classification is enough for a master's course. Say in plain words that each year should move you closer to the full set of minimum outcomes, and ask: 'Which of the outcomes do you feel least sure of now, and how will this year help?' Avoid promising postgraduate admission or treating the expectation as a guarantee."
- statement: qaa/history-2022/2.6
  forPractitioner: { text: "In joint honours, graduates will meet some of History's subject-specific and generic skills and will add others from the partner subjects; design the History part with that in mind.", rewrite: light, force: will, status: drafted }
  forBeneficiary: { text: "If you study History jointly with another subject, you will develop some of the history skills and add others from your other subject.", rewrite: full, force: will, status: drafted }
  author-agent-written: "Treat this as an expected outcome (will) for joint honours students at FHEQ level 6: they meet part of History's subject and generic skills, not necessarily all. Cite it as QAA (2022) History Subject Benchmark Statement, para 2.6, and do not claim that joint honours graduates must meet every item in 4.5 and 4.6, or that the statement says which items. Set it beside 1.1 on joint and combined courses, the threshold lists 4.5 and 4.6, the honours descriptor qaa/fheq-2024/4.15.b1 and spine:6."
  author-agent-dialogue: "Raise it when a joint honours student, or a team designing a joint course, asks which History outcomes apply. Explain that you will build some of the history skills and gain others from your other subject, and ask: 'Which history skills does your course develop, and which come from your other subject?' Avoid telling a joint student they fall short for not covering every History item."
- statement: qaa/history-2022/2.11
  forPractitioner: { text: "Periodic review will draw on external reviewers for an outside perspective on proposed changes, to confirm that threshold standards are achieved and that content fits the subject.", rewrite: light, force: will, status: drafted }
  forBeneficiary: { text: "not-applicable: a duty on the provider's quality assurance", rewrite: full, force: will, status: drafted }
  author-agent-written: "Treat this as a statement, in will, about provider practice in quality assurance: external reviewers take part in the periodic review of History courses. Cite it as QAA (2022) History Subject Benchmark Statement, para 2.11, and do not present it as a student outcome or as a regulatory requirement set by this statement. Set it beside 2.10 and 2.12 on monitoring and external examining, and the threshold lists 4.5 and 4.6 that reviewers check against."
  author-agent-dialogue: "Raise it with a programme team preparing for periodic review. Ask who the external reviewers will be and how their view on threshold standards and subject content will be recorded and acted on. Do not bring it to a student as something they need to do."
- statement: qaa/history-2022/3.7
  forPractitioner: { text: "Choose teaching methods that should create an inclusive environment for learning and serve the aims of education for sustainable development.", rewrite: light, force: should, status: drafted }
  forBeneficiary: { text: "not-applicable: a duty on teaching design; the student meets its effect", rewrite: full, force: should, status: drafted }
  author-agent-written: "Treat this as a provider expectation (should) on teaching and learning methods in History courses, carrying both the equality, diversity and inclusion theme and education for sustainable development. Cite it as QAA (2022) History Subject Benchmark Statement, para 3.7, and do not claim it prescribes particular methods, since the same paragraph leaves methods to each department. Set it beside 1.12 to 1.14 on inclusion, 1.16 to 1.18 on sustainability, and the guidance std:doc:qaa-advancehe-esd-2021-guidance."
  author-agent-dialogue: "Raise it with staff reviewing a module's teaching or a course's learning and teaching strategy. Ask how the current methods include every student and where they connect with sustainability, and what evidence, such as evaluations or peer review, shows it. Do not present it to a student as their duty."
- statement: qaa/history-2022/3.9
  forPractitioner: { text: "Use a variety of assessment modes: no one mode shows the full range of ability, and students arrive with different qualifications, so the course should give all of them chances to demonstrate their knowledge, understanding and abilities.", rewrite: light, force: should, status: drafted }
  forBeneficiary: { text: "not-applicable: a duty on the course's assessment design", rewrite: full, force: should, status: drafted }
  author-agent-written: "Treat this as a provider expectation (should) that History courses assess through varied modes so every student can demonstrate what they have learned. Cite it as QAA (2022) History Subject Benchmark Statement, para 3.9, and do not claim it fixes a list of modes; the kinds are in 3.10. Set it beside 3.10 a) to f) and 3.11, and the Annex D descriptions (std:doc:qaa-fheq-2024-framework, SL6) that classification draws on."
  author-agent-dialogue: "Raise it with a team designing or reviewing a course's assessment pattern. Ask whether any group of students could be disadvantaged by relying on one mode, and where students can play to their strengths. Do not present it to a student as a requirement on them."
- statement: qaa/history-2022/3.10.b1
  forPractitioner: { text: "The course should include tasks in which students communicate information and argument to suit the task, in written forms of differing kinds, lengths and audiences, and in forms beyond prose such as talks, videos, websites, databases and digital history projects.", rewrite: light, force: should, status: drafted }
  forBeneficiary: { text: "not-applicable: a requirement on the course's assessment design; the student meets it as the tasks set", rewrite: full, force: should, status: drafted }
  author-agent-written: "Treat this as a provider expectation (should) on the mix of assessment in a History honours course: the course should include assessments of communicating information and argument in written and non-written forms. Cite it as QAA (2022) History Subject Benchmark Statement, para 3.10 a), and do not claim it requires one particular format. Set it beside 3.10 b) to f), 3.9 and the generic skill 4.6.b15, and the Annex D descriptions it helps to evidence, such as qaa/fheq-2024/annex-d/transferable/r1/3rd."
  author-agent-dialogue: "Raise it with a team mapping assessment across a course, or a module leader choosing a task type. Ask where in the course students meet tasks for different audiences and in non-written forms, and whether the range goes beyond the essay. Do not put it to a student as a demand on them; for a student, simply explain that the course includes such tasks."
- statement: qaa/history-2022/3.10.b2
  forPractitioner: { text: "The course should include tasks that test handling varied kinds of historical evidence, for example gobbet exercises, source exercises or commentaries.", rewrite: light, force: should, status: drafted }
  forBeneficiary: { text: "not-applicable: a requirement on the course's assessment design; the student meets it as the tasks set", rewrite: full, force: should, status: drafted }
  author-agent-written: "Treat this as a provider expectation (should) on the mix of assessment in a History honours course: the course should include assessments of working with historical evidence. Cite it as QAA (2022) History Subject Benchmark Statement, para 3.10 b), and do not claim it requires one particular format. Set it beside 4.5.b7 on primary sources and 3.10 a) to f), and the Annex D descriptions it helps to evidence, such as qaa/fheq-2024/annex-d/cognitive/r1/3rd."
  author-agent-dialogue: "Raise it with a team mapping assessment across a course, or a module leader choosing a task type. Ask where in the course students meet source-based tasks such as gobbets or commentaries, and whether every year includes some. Do not put it to a student as a demand on them; for a student, simply explain that the course includes such tasks."
- statement: qaa/history-2022/3.10.b3
  forPractitioner: { text: "The course should include tasks that test working against the clock and quick thinking, whether a timed exam, a take-home paper or a task over hours or days.", rewrite: light, force: should, status: drafted }
  forBeneficiary: { text: "not-applicable: a requirement on the course's assessment design; the student meets it as the tasks set", rewrite: full, force: should, status: drafted }
  author-agent-written: "Treat this as a provider expectation (should) on the mix of assessment in a History honours course: the course should include assessments of working under time pressure and thinking quickly. Cite it as QAA (2022) History Subject Benchmark Statement, para 3.10 c), and do not claim it requires one particular format, since the text allows exams, take-home papers or tasks over days. Set it beside 3.9 and 3.10 a) to f), and the Annex D descriptions it helps to evidence, such as qaa/fheq-2024/annex-d/cognitive/r3/3rd."
  author-agent-dialogue: "Raise it with a team mapping assessment across a course, or a module leader choosing a task type. Ask where in the course students meet time-limited tasks, and whether they suit students who need adjustments. Do not put it to a student as a demand on them; for a student, simply explain that the course includes such tasks."
- statement: qaa/history-2022/3.10.b4
  forPractitioner: { text: "The course should include tasks that test independent work carried out under supervision.", rewrite: light, force: should, status: drafted }
  forBeneficiary: { text: "not-applicable: a requirement on the course's assessment design; the student meets it as the tasks set", rewrite: full, force: should, status: drafted }
  author-agent-written: "Treat this as a provider expectation (should) on the mix of assessment in a History honours course: the course should include assessments of independent work under supervision. Cite it as QAA (2022) History Subject Benchmark Statement, para 3.10 d), and do not claim it requires one particular format. Set it beside 4.6.b1 and 3.10 f), and the Annex D descriptions it helps to evidence, such as qaa/fheq-2024/annex-d/transferable/r3/3rd."
  author-agent-dialogue: "Raise it with a team mapping assessment across a course, or a module leader choosing a task type. Ask where in the course students meet supervised independent tasks, and whether supervision is set up before the final year. Do not put it to a student as a demand on them; for a student, simply explain that the course includes such tasks."
- statement: qaa/history-2022/3.10.b5
  forPractitioner: { text: "The course should include tasks that test collaboration and effective group work, such as group presentations or projects.", rewrite: light, force: should, status: drafted }
  forBeneficiary: { text: "not-applicable: a requirement on the course's assessment design; the student meets it as the tasks set", rewrite: full, force: should, status: drafted }
  author-agent-written: "Treat this as a provider expectation (should) on the mix of assessment in a History honours course: the course should include assessments of collaboration and group work. Cite it as QAA (2022) History Subject Benchmark Statement, para 3.10 e), and do not claim it requires one particular format. Set it beside 4.6.b2, and the Annex D descriptions it helps to evidence, such as qaa/fheq-2024/annex-d/transferable/r2/3rd."
  author-agent-dialogue: "Raise it with a team mapping assessment across a course, or a module leader choosing a task type. Ask where in the course students meet assessed group work, and whether individual contributions are fairly recognised. Do not put it to a student as a demand on them; for a student, simply explain that the course includes such tasks."
- statement: qaa/history-2022/3.10.b6
  forPractitioner: { text: "The course should include at least one major assignment testing the ability to tackle historical problems in depth through structured enquiry pursued over several stages, often a dissertation or final year project at least twice the usual essay length, though other forms, including authentic tasks for different audiences, are possible.", rewrite: light, force: should, status: drafted }
  forBeneficiary: { text: "not-applicable: a requirement on the course's assessment design; the student meets it as the tasks set", rewrite: full, force: should, status: drafted }
  author-agent-written: "Treat this as a provider expectation (should) on the mix of assessment in a History honours course: the course should include at least one major assignment testing structured historical enquiry in depth over several stages. Cite it as QAA (2022) History Subject Benchmark Statement, para 3.10 f), and do not claim it requires one particular format, since the text allows forms other than a dissertation. Set it beside 2.1 f) on the extended piece of work, 4.5.b3 and 4.6.b3, and the Annex D descriptions it helps to evidence, such as qaa/fheq-2024/annex-d/knowledge/r3/3rd and the honours descriptor qaa/fheq-2024/4.15.b6."
  author-agent-dialogue: "Raise it with a team mapping assessment across a course, or a module leader choosing a task type. Ask where in the course students meet a major staged enquiry, and whether students set their own tasks within it. Do not put it to a student as a demand on them; for a student, simply explain that the course includes such tasks."
- statement: qaa/history-2022/3.11
  forPractitioner: { text: "Taken together, the course's assessments must allow students to demonstrate every intended learning outcome; give students clear, timely information about how they are assessed and constructive feedback on their work.", rewrite: light, force: must, status: drafted }
  forBeneficiary: { text: "not-applicable: a requirement on the course's assessment design", rewrite: full, force: must, status: drafted }
  author-agent-written: "Treat this as the one must in the account of assessment: across a History course, the combined assessments must allow students to demonstrate all its learning outcomes, with clear information and constructive feedback. Cite it as QAA (2022) History Subject Benchmark Statement, para 3.11, and do not claim that each single assessment must cover every outcome. Set it beside 3.9 and 3.10 a) to f), the threshold lists 4.5 and 4.6, and the FHEQ level 6 descriptor qaa/fheq-2024/4.15.b5."
  author-agent-dialogue: "Raise it with a team building an assessment map or a module leader writing assessment briefs. Ask: 'Which assessment shows each learning outcome, and is any outcome never assessed?', and how students learn in good time how they will be assessed. Do not present it to a student as their obligation; to a student, explain only that every outcome is assessed somewhere and that feedback is due."
- statement: qaa/history-2022/4.2
  forPractitioner: { text: "Decide how the course will evidence achievement of the standards; the course team should consult Annex D's descriptions of the four honours classes (1st, 2:1, 2:2, 3rd) and publish its own descriptors for students, for example as assessment criteria.", rewrite: light, force: should, status: drafted }
  forBeneficiary: { text: "not-applicable: a duty on the provider in setting its own descriptors", rewrite: full, force: should, status: drafted }
  author-agent-written: "Treat this as a provider expectation (should) that links the History threshold standards to the generic classification descriptions in Annex D of the Frameworks for Higher Education Qualifications. Cite it as QAA (2022) History Subject Benchmark Statement, para 4.2, and do not claim that the History statement defines the classes itself or that Annex D is subject-specific. Set it beside 4.1 and the threshold lists 4.5 and 4.6, and point to std:doc:qaa-fheq-2024-framework, Annex D (SL6), with third-class cells such as qaa/fheq-2024/annex-d/summary/r1/3rd as the threshold."
  author-agent-dialogue: "Raise it with staff writing marking criteria or grade descriptors for a History course. Ask how the course's descriptors relate to Annex D's four classes and where students can read them. With a student, explain only that the classification bands come from published descriptors, and avoid reading Annex D aloud."
- statement: qaa/history-2022/4.5.b1
  forPractitioner: { text: "At the minimum standard, graduates should be able to frame pertinent, well-reasoned and tightly focused questions about the past.", rewrite: light, force: should, status: drafted }
  forBeneficiary: { text: "To reach the minimum standard for your degree, you should be able to frame pertinent, well-reasoned and tightly focused questions about the past.", rewrite: full, force: should, status: drafted }
  author-agent-written: "Treat this as a threshold standard for the History honours degree at FHEQ level 6 (FQHEIS level 10): every graduate should be able to frame pertinent, well-reasoned and tightly focused questions about the past. Cite it as QAA (2022) History Subject Benchmark Statement, para 4.5, item 1, and do not call it a regulatory rule or a sign of a high classification. Set it beside its fuller form 1.7.b1, the honours descriptor qaa/fheq-2024/4.15.b7 with spine:6, and the third-class floor qaa/fheq-2024/annex-d/knowledge/r3/3rd."
  author-agent-dialogue: "Bring it up when a student is choosing a topic or planning an essay or dissertation. With a student, say in plain words that to graduate you should be able to frame pertinent, well-reasoned and tightly focused questions about the past, and ask 'What exactly is your question, and why does it matter?' With staff, ask where the course teaches and assesses it, and do not present it as more than the minimum for the award."
- statement: qaa/history-2022/4.5.b2
  forPractitioner: { text: "At the minimum standard, graduates should be able to find out where trustworthy, exact knowledge about the past is held and how to reach it.", rewrite: light, force: should, status: drafted }
  forBeneficiary: { text: "To reach the minimum standard for your degree, you should be able to find out where trustworthy, exact knowledge about the past is held and how to reach it.", rewrite: full, force: should, status: drafted }
  author-agent-written: "Treat this as a threshold standard for the History honours degree at FHEQ level 6 (FQHEIS level 10): every graduate should be able to find out where trustworthy, exact knowledge about the past is held and how to reach it. Cite it as QAA (2022) History Subject Benchmark Statement, para 4.5, item 2, and do not call it a regulatory rule or a sign of a high classification. Set it beside its fuller form 1.7.b2, the honours descriptor qaa/fheq-2024/4.15.b5 with spine:6, and the third-class floor qaa/fheq-2024/annex-d/cognitive/r1/3rd."
  author-agent-dialogue: "Bring it up when a student is unsure where to start researching or which sources to trust. With a student, say in plain words that to graduate you should be able to find out where trustworthy, exact knowledge about the past is held and how to reach it, and ask 'Where would you look first, and how would you judge whether it is reliable?' With staff, ask where the course teaches and assesses it, and do not present it as more than the minimum for the award."
- statement: qaa/history-2022/4.5.b3
  forPractitioner: { text: "At the minimum standard, graduates should be able to plan and carry out a structured enquiry, from setting their own tasks to collecting, filtering, ordering, combining and analysing large bodies of primary and secondary evidence.", rewrite: light, force: should, status: drafted }
  forBeneficiary: { text: "To reach the minimum standard for your degree, you should be able to plan and carry out a structured enquiry, from setting your own tasks to collecting, filtering, ordering, combining and analysing large bodies of primary and secondary evidence.", rewrite: full, force: should, status: drafted }
  author-agent-written: "Treat this as a threshold standard for the History honours degree at FHEQ level 6 (FQHEIS level 10): every graduate should be able to plan and carry out a structured enquiry, from setting their own tasks to collecting, filtering, ordering, combining and analysing large bodies of primary and secondary evidence. Cite it as QAA (2022) History Subject Benchmark Statement, para 4.5, item 3, and do not call it a regulatory rule or a sign of a high classification. Set it beside its fuller form 1.7.b3, the honours descriptor qaa/fheq-2024/4.15.b6 and 4.15.b2 with spine:6, and the third-class floor qaa/fheq-2024/annex-d/knowledge/r3/3rd."
  author-agent-dialogue: "Bring it up when a student is planning a project, a long essay or a dissertation. With a student, say in plain words that to graduate you should be able to plan and carry out a structured enquiry, from setting your own tasks to collecting, filtering, ordering, combining and analysing large bodies of primary and secondary evidence, and ask 'How will you gather and sort your evidence, and how will you know you have enough?' With staff, ask where the course teaches and assesses it, and do not present it as more than the minimum for the award."
- statement: qaa/history-2022/4.5.b4
  forPractitioner: { text: "At the minimum standard, graduates should be able to draw on sound, pertinent evidence and argument.", rewrite: light, force: should, status: drafted }
  forBeneficiary: { text: "To reach the minimum standard for your degree, you should be able to draw on sound, pertinent evidence and argument.", rewrite: full, force: should, status: drafted }
  author-agent-written: "Treat this as a threshold standard for the History honours degree at FHEQ level 6 (FQHEIS level 10): every graduate should be able to draw on sound, pertinent evidence and argument. Cite it as QAA (2022) History Subject Benchmark Statement, para 4.5, item 4, and do not call it a regulatory rule or a sign of a high classification. Set it beside its fuller form 1.7.b4, the honours descriptor qaa/fheq-2024/4.15.b3.1 with spine:6, and the third-class floor qaa/fheq-2024/annex-d/cognitive/r2/3rd."
  author-agent-dialogue: "Bring it up when a student is building or revising an argument. With a student, say in plain words that to graduate you should be able to draw on sound, pertinent evidence and argument, and ask 'Which piece of evidence carries most weight here, and why?' With staff, ask where the course teaches and assesses it, and do not present it as more than the minimum for the award."
- statement: qaa/history-2022/4.5.b5
  forPractitioner: { text: "At the minimum standard, graduates should be able to handle references, reading lists and bibliographies well.", rewrite: light, force: should, status: drafted }
  forBeneficiary: { text: "To reach the minimum standard for your degree, you should be able to handle references, reading lists and bibliographies well.", rewrite: full, force: should, status: drafted }
  author-agent-written: "Treat this as a threshold standard for the History honours degree at FHEQ level 6 (FQHEIS level 10): every graduate should be able to handle references, reading lists and bibliographies well. Cite it as QAA (2022) History Subject Benchmark Statement, para 4.5, item 5, and do not call it a regulatory rule or a sign of a high classification. Set it beside its fuller form 1.7.b5, the honours descriptor qaa/fheq-2024/4.15.b5 with spine:6, and the third-class floor qaa/fheq-2024/annex-d/cognitive/r1/3rd."
  author-agent-dialogue: "Bring it up when a student asks about referencing or building a reading list. With a student, say in plain words that to graduate you should be able to handle references, reading lists and bibliographies well, and ask 'How do you keep track of what you read and cite it consistently?' With staff, ask where the course teaches and assesses it, and do not present it as more than the minimum for the award."
- statement: qaa/history-2022/4.5.b6
  forPractitioner: { text: "At the minimum standard, graduates should be able to analyse claims, recognising that some statements are better founded than others.", rewrite: light, force: should, status: drafted }
  forBeneficiary: { text: "To reach the minimum standard for your degree, you should be able to analyse claims, recognising that some statements are better founded than others.", rewrite: full, force: should, status: drafted }
  author-agent-written: "Treat this as a threshold standard for the History honours degree at FHEQ level 6 (FQHEIS level 10): every graduate should be able to analyse claims, recognising that some statements are better founded than others. Cite it as QAA (2022) History Subject Benchmark Statement, para 4.5, item 6, and do not call it a regulatory rule or a sign of a high classification. Set it beside its fuller form 1.7.b6, the honours descriptor qaa/fheq-2024/4.15.b7 with spine:6, and the third-class floor qaa/fheq-2024/annex-d/cognitive/r1/3rd."
  author-agent-dialogue: "Bring it up when a student treats every source or claim as equally reliable. With a student, say in plain words that to graduate you should be able to analyse claims, recognising that some statements are better founded than others, and ask 'How would you test whether this claim holds up?' With staff, ask where the course teaches and assesses it, and do not present it as more than the minimum for the award."
- statement: qaa/history-2022/4.5.b7
  forPractitioner: { text: "At the minimum standard, graduates should be able to analyse primary sources critically and with empathy, asking about their genre, content, viewpoint and purpose.", rewrite: light, force: should, status: drafted }
  forBeneficiary: { text: "To reach the minimum standard for your degree, you should be able to analyse primary sources critically and with empathy, asking about their genre, content, viewpoint and purpose.", rewrite: full, force: should, status: drafted }
  author-agent-written: "Treat this as a threshold standard for the History honours degree at FHEQ level 6 (FQHEIS level 10): every graduate should be able to analyse primary sources critically and with empathy, asking about their genre, content, viewpoint and purpose. Cite it as QAA (2022) History Subject Benchmark Statement, para 4.5, item 7, and do not call it a regulatory rule or a sign of a high classification. Set it beside its fuller form 1.7.b7, the honours descriptor qaa/fheq-2024/4.15.b5 with spine:6, and the third-class floor qaa/fheq-2024/annex-d/cognitive/r1/3rd."
  author-agent-dialogue: "Bring it up when a student is working with a document, image, object or oral account. With a student, say in plain words that to graduate you should be able to analyse primary sources critically and with empathy, asking about their genre, content, viewpoint and purpose, and ask 'Who made this, for whom and why, and how does that shape what it tells you?' With staff, ask where the course teaches and assesses it, and do not present it as more than the minimum for the award."
- statement: qaa/history-2022/4.5.b8
  forPractitioner: { text: "At the minimum standard, graduates should be able to grasp the problems of the historical record: weighing differing viewpoints, interpreting material that is complex, unclear, contradictory or partial, and seeing where knowledge stops and where over-simple explanation misleads.", rewrite: light, force: should, status: drafted }
  forBeneficiary: { text: "To reach the minimum standard for your degree, you should be able to grasp the problems of the historical record: weighing differing viewpoints, interpreting material that is complex, unclear, contradictory or partial, and seeing where knowledge stops and where over-simple explanation misleads.", rewrite: full, force: should, status: drafted }
  author-agent-written: "Treat this as a threshold standard for the History honours degree at FHEQ level 6 (FQHEIS level 10): every graduate should be able to grasp the problems of the historical record: weighing differing viewpoints, interpreting material that is complex, unclear, contradictory or partial, and seeing where knowledge stops and where over-simple explanation misleads. Cite it as QAA (2022) History Subject Benchmark Statement, para 4.5, item 8, and do not call it a regulatory rule or a sign of a high classification. Set it beside its fuller form 1.7.b8, the honours descriptor qaa/fheq-2024/4.15.b4 with spine:6, and the third-class floor qaa/fheq-2024/annex-d/knowledge/r2/3rd."
  author-agent-dialogue: "Bring it up when a student finds sources that conflict or leave gaps. With a student, say in plain words that to graduate you should be able to grasp the problems of the historical record: weighing differing viewpoints, interpreting material that is complex, unclear, contradictory or partial, and seeing where knowledge stops and where over-simple explanation misleads, and ask 'What can this evidence not tell you, and how does that limit your conclusion?' With staff, ask where the course teaches and assesses it, and do not present it as more than the minimum for the award."
- statement: qaa/history-2022/4.5.b9
  forPractitioner: { text: "At the minimum standard, graduates should be able to appreciate how varied and complicated past situations, events and outlooks were, and so how varied the present is.", rewrite: light, force: should, status: drafted }
  forBeneficiary: { text: "To reach the minimum standard for your degree, you should be able to appreciate how varied and complicated past situations, events and outlooks were, and so how varied the present is.", rewrite: full, force: should, status: drafted }
  author-agent-written: "Treat this as a threshold standard for the History honours degree at FHEQ level 6 (FQHEIS level 10): every graduate should be able to appreciate how varied and complicated past situations, events and outlooks were, and so how varied the present is. Cite it as QAA (2022) History Subject Benchmark Statement, para 4.5, item 9, and do not call it a regulatory rule or a sign of a high classification. Set it beside its fuller form 1.7.b9, the honours descriptor qaa/fheq-2024/4.15.b4 with spine:6, and the third-class floor qaa/fheq-2024/annex-d/knowledge/r1/3rd."
  author-agent-dialogue: "Bring it up when a student's account flattens a period into one simple story. With a student, say in plain words that to graduate you should be able to appreciate how varied and complicated past situations, events and outlooks were, and so how varied the present is, and ask 'Whose experience of this period is missing from your account?' With staff, ask where the course teaches and assesses it, and do not present it as more than the minimum for the award."
- statement: qaa/history-2022/4.5.b10
  forPractitioner: { text: "At the minimum standard, graduates should be able to understand how people lived, acted and thought in past settings that always differ from our own.", rewrite: light, force: should, status: drafted }
  forBeneficiary: { text: "To reach the minimum standard for your degree, you should be able to understand how people lived, acted and thought in past settings that always differ from our own.", rewrite: full, force: should, status: drafted }
  author-agent-written: "Treat this as a threshold standard for the History honours degree at FHEQ level 6 (FQHEIS level 10): every graduate should be able to understand how people lived, acted and thought in past settings that always differ from our own. Cite it as QAA (2022) History Subject Benchmark Statement, para 4.5, item 10, and do not call it a regulatory rule or a sign of a high classification. Set it beside its fuller form 1.7.b10, the honours descriptor qaa/fheq-2024/4.15.b1 with spine:6, and the third-class floor qaa/fheq-2024/annex-d/knowledge/r2/3rd."
  author-agent-dialogue: "Bring it up when a student judges past people by present-day assumptions. With a student, say in plain words that to graduate you should be able to understand how people lived, acted and thought in past settings that always differ from our own, and ask 'How did people at the time understand what they were doing?' With staff, ask where the course teaches and assesses it, and do not present it as more than the minimum for the award."
- statement: qaa/history-2022/4.5.b11
  forPractitioner: { text: "At the minimum standard, graduates should be able to hold to a reasoned argument when others disagree, listen, debate at length and change their view where evidence and argument call for it.", rewrite: light, force: should, status: drafted }
  forBeneficiary: { text: "To reach the minimum standard for your degree, you should be able to hold to a reasoned argument when others disagree, listen, debate at length and change your view where evidence and argument call for it.", rewrite: full, force: should, status: drafted }
  author-agent-written: "Treat this as a threshold standard for the History honours degree at FHEQ level 6 (FQHEIS level 10): every graduate should be able to hold to a reasoned argument when others disagree, listen, debate at length and change their view where evidence and argument call for it. Cite it as QAA (2022) History Subject Benchmark Statement, para 4.5, item 11, and do not call it a regulatory rule or a sign of a high classification. Set it beside its fuller form 1.7.b11, the honours descriptor qaa/fheq-2024/4.15.b3.1 and 4.15.b8 with spine:6, and the third-class floor qaa/fheq-2024/annex-d/cognitive/r2/3rd."
  author-agent-dialogue: "Bring it up when a student is preparing for a seminar debate or answering critical feedback. With a student, say in plain words that to graduate you should be able to hold to a reasoned argument when others disagree, listen, debate at length and change your view where evidence and argument call for it, and ask 'What evidence would make you change your mind?' With staff, ask where the course teaches and assesses it, and do not present it as more than the minimum for the award."
- statement: qaa/history-2022/4.5.b12
  forPractitioner: { text: "At the minimum standard, graduates should be able to build an argument around questions about the past that matter, and that also bear on the present and future.", rewrite: light, force: should, status: drafted }
  forBeneficiary: { text: "To reach the minimum standard for your degree, you should be able to build an argument around questions about the past that matter, and that also bear on the present and future.", rewrite: full, force: should, status: drafted }
  author-agent-written: "Treat this as a threshold standard for the History honours degree at FHEQ level 6 (FQHEIS level 10): every graduate should be able to build an argument around questions about the past that matter, and that also bear on the present and future. Cite it as QAA (2022) History Subject Benchmark Statement, para 4.5, item 12, and do not call it a regulatory rule or a sign of a high classification. Set it beside its fuller form 1.7.b12, the honours descriptor qaa/fheq-2024/4.15.b3.1 with spine:6, and the third-class floor qaa/fheq-2024/annex-d/cognitive/r2/3rd."
  author-agent-dialogue: "Bring it up when a student asks why history matters beyond the past itself. With a student, say in plain words that to graduate you should be able to build an argument around questions about the past that matter, and that also bear on the present and future, and ask 'What does your question tell us about the present?' With staff, ask where the course teaches and assesses it, and do not present it as more than the minimum for the award."
- statement: qaa/history-2022/4.6.b1
  forPractitioner: { text: "As a minimum generic skill, graduates should be able to work on their own while making good use of supervision and guidance.", rewrite: light, force: should, status: drafted }
  forBeneficiary: { text: "To reach the minimum standard for your degree, you should be able to work on your own while making good use of supervision and guidance.", rewrite: full, force: should, status: drafted }
  author-agent-written: "Treat this as a threshold generic skill for the History honours degree: it sits with the subject items of para 4.5 as part of the minimum (para 2.5) and refines the FHEQ level 6 descriptor qaa/fheq-2024/4.15.b9.1 (spine:6; FQHEIS level 10). Graduates should be able to work on their own while making good use of supervision and guidance. Cite it as QAA (2022) History Subject Benchmark Statement, para 4.6, item 1; do not claim it holds at another level or is a legal requirement, and set it beside 4.6.b12 and 3.10 d) and the third-class description qaa/fheq-2024/annex-d/transferable/r3/3rd."
  author-agent-dialogue: "Raise it when a student is starting a dissertation or other self-directed work. Put it to a student as a skill you should be able to show by graduation, to work on your own while making good use of supervision and guidance, and ask 'What will you bring to your next supervision, and what will you decide yourself?' For a programme team, ask which modules build and test it, and avoid presenting it as an extra beyond the minimum or reading the list aloud."
- statement: qaa/history-2022/4.6.b2
  forPractitioner: { text: "As a minimum generic skill, graduates should be able to collaborate well as a member of a team.", rewrite: light, force: should, status: drafted }
  forBeneficiary: { text: "To reach the minimum standard for your degree, you should be able to collaborate well as a member of a team.", rewrite: full, force: should, status: drafted }
  author-agent-written: "Treat this as a threshold generic skill for the History honours degree: it sits with the subject items of para 4.5 as part of the minimum (para 2.5) and refines the FHEQ level 6 descriptor qaa/fheq-2024/4.15.b9.1 (spine:6; FQHEIS level 10). Graduates should be able to collaborate well as a member of a team. Cite it as QAA (2022) History Subject Benchmark Statement, para 4.6, item 2; do not claim it holds at another level or is a legal requirement, and set it beside 3.10 e) and the third-class description qaa/fheq-2024/annex-d/transferable/r2/3rd."
  author-agent-dialogue: "Raise it when a student is about to start group work or a group presentation. Put it to a student as a skill you should be able to show by graduation, to collaborate well as a member of a team, and ask 'What role do you usually take in a group, and how could you widen it?' For a programme team, ask which modules build and test it, and avoid presenting it as an extra beyond the minimum or reading the list aloud."
- statement: qaa/history-2022/4.6.b3
  forPractitioner: { text: "As a minimum generic skill, graduates should be able to devise and follow up clearly framed questions and lines of enquiry.", rewrite: light, force: should, status: drafted }
  forBeneficiary: { text: "To reach the minimum standard for your degree, you should be able to devise and follow up clearly framed questions and lines of enquiry.", rewrite: full, force: should, status: drafted }
  author-agent-written: "Treat this as a threshold generic skill for the History honours degree: it sits with the subject items of para 4.5 as part of the minimum (para 2.5) and refines the FHEQ level 6 descriptor qaa/fheq-2024/4.15.b7 (spine:6; FQHEIS level 10). Graduates should be able to devise and follow up clearly framed questions and lines of enquiry. Cite it as QAA (2022) History Subject Benchmark Statement, para 4.6, item 3; do not claim it holds at another level or is a legal requirement, and set it beside 4.5.b1 and 4.5.b3 and the third-class description qaa/fheq-2024/annex-d/knowledge/r3/3rd."
  author-agent-dialogue: "Raise it when a student is turning a broad interest into a researchable question. Put it to a student as a skill you should be able to show by graduation, to devise and follow up clearly framed questions and lines of enquiry, and ask 'Can you state your question in one sentence?' For a programme team, ask which modules build and test it, and avoid presenting it as an extra beyond the minimum or reading the list aloud."
- statement: qaa/history-2022/4.6.b4
  forPractitioner: { text: "As a minimum generic skill, graduates should be able to identify, locate, retrieve, sort and share information by suitable means.", rewrite: light, force: should, status: drafted }
  forBeneficiary: { text: "To reach the minimum standard for your degree, you should be able to identify, locate, retrieve, sort and share information by suitable means.", rewrite: full, force: should, status: drafted }
  author-agent-written: "Treat this as a threshold generic skill for the History honours degree: it sits with the subject items of para 4.5 as part of the minimum (para 2.5) and refines the FHEQ level 6 descriptor qaa/fheq-2024/4.15.b5 (spine:6; FQHEIS level 10). Graduates should be able to identify, locate, retrieve, sort and share information by suitable means. Cite it as QAA (2022) History Subject Benchmark Statement, para 4.6, item 4; do not claim it holds at another level or is a legal requirement, and set it beside 4.5.b2 and 4.5.b5 and the third-class description qaa/fheq-2024/annex-d/practical/r4/3rd."
  author-agent-dialogue: "Raise it when a student struggles to find or manage material for an assignment. Put it to a student as a skill you should be able to show by graduation, to identify, locate, retrieve, sort and share information by suitable means, and ask 'How do you search, and how do you keep what you find in order?' For a programme team, ask which modules build and test it, and avoid presenting it as an extra beyond the minimum or reading the list aloud."
- statement: qaa/history-2022/4.6.b5
  forPractitioner: { text: "As a minimum generic skill, graduates should be able to collect, arrange and put to use evidence, data and information.", rewrite: light, force: should, status: drafted }
  forBeneficiary: { text: "To reach the minimum standard for your degree, you should be able to collect, arrange and put to use evidence, data and information.", rewrite: full, force: should, status: drafted }
  author-agent-written: "Treat this as a threshold generic skill for the History honours degree: it sits with the subject items of para 4.5 as part of the minimum (para 2.5) and refines the FHEQ level 6 descriptor qaa/fheq-2024/4.15.b6 (spine:6; FQHEIS level 10). Graduates should be able to collect, arrange and put to use evidence, data and information. Cite it as QAA (2022) History Subject Benchmark Statement, para 4.6, item 5; do not claim it holds at another level or is a legal requirement, and set it beside 4.5.b3 and 4.5.b4 and the third-class description qaa/fheq-2024/annex-d/practical/r4/3rd."
  author-agent-dialogue: "Raise it when a student has plenty of material but no clear way to use it. Put it to a student as a skill you should be able to show by graduation, to collect, arrange and put to use evidence, data and information, and ask 'Which of your sources does the most work in your argument?' For a programme team, ask which modules build and test it, and avoid presenting it as an extra beyond the minimum or reading the list aloud."
- statement: qaa/history-2022/4.6.b6
  forPractitioner: { text: "As a minimum generic skill, graduates should be able to carry out close analysis of sources.", rewrite: light, force: should, status: drafted }
  forBeneficiary: { text: "To reach the minimum standard for your degree, you should be able to carry out close analysis of sources.", rewrite: full, force: should, status: drafted }
  author-agent-written: "Treat this as a threshold generic skill for the History honours degree: it sits with the subject items of para 4.5 as part of the minimum (para 2.5) and refines the FHEQ level 6 descriptor qaa/fheq-2024/4.15.b7 (spine:6; FQHEIS level 10). Graduates should be able to carry out close analysis of sources. Cite it as QAA (2022) History Subject Benchmark Statement, para 4.6, item 6; do not claim it holds at another level or is a legal requirement, and set it beside 4.5.b7 and the third-class description qaa/fheq-2024/annex-d/cognitive/r1/3rd."
  author-agent-dialogue: "Raise it when a student describes sources instead of analysing them. Put it to a student as a skill you should be able to show by graduation, to carry out close analysis of sources, and ask 'What does this source show that its author may not have intended?' For a programme team, ask which modules build and test it, and avoid presenting it as an extra beyond the minimum or reading the list aloud."
- statement: qaa/history-2022/4.6.b7
  forPractitioner: { text: "As a minimum generic skill, graduates should be able to see what is strong and what is weak in other people's arguments.", rewrite: light, force: should, status: drafted }
  forBeneficiary: { text: "To reach the minimum standard for your degree, you should be able to see what is strong and what is weak in other people's arguments.", rewrite: full, force: should, status: drafted }
  author-agent-written: "Treat this as a threshold generic skill for the History honours degree: it sits with the subject items of para 4.5 as part of the minimum (para 2.5) and refines the FHEQ level 6 descriptor qaa/fheq-2024/4.15.b7 (spine:6; FQHEIS level 10). Graduates should be able to see what is strong and what is weak in other people's arguments. Cite it as QAA (2022) History Subject Benchmark Statement, para 4.6, item 7; do not claim it holds at another level or is a legal requirement, and set it beside 4.5.b6 and 4.5.b11 and the third-class description qaa/fheq-2024/annex-d/cognitive/r2/3rd."
  author-agent-dialogue: "Raise it when a student is reviewing scholarship or responding to peers. Put it to a student as a skill you should be able to show by graduation, to see what is strong and what is weak in other people's arguments, and ask 'Where is this historian's argument least convincing, and why?' For a programme team, ask which modules build and test it, and avoid presenting it as an extra beyond the minimum or reading the list aloud."
- statement: qaa/history-2022/4.6.b8
  forPractitioner: { text: "As a minimum generic skill, graduates should be able to think analytically and tackle problems, including ones with no single answer.", rewrite: light, force: should, status: drafted }
  forBeneficiary: { text: "To reach the minimum standard for your degree, you should be able to think analytically and tackle problems, including ones with no single answer.", rewrite: full, force: should, status: drafted }
  author-agent-written: "Treat this as a threshold generic skill for the History honours degree: it sits with the subject items of para 4.5 as part of the minimum (para 2.5) and refines the FHEQ level 6 descriptor qaa/fheq-2024/4.15.b7 (spine:6; FQHEIS level 10). Graduates should be able to think analytically and tackle problems, including ones with no single answer. Cite it as QAA (2022) History Subject Benchmark Statement, para 4.6, item 8; do not claim it holds at another level or is a legal requirement, and set it beside 4.5.b6 and the third-class description qaa/fheq-2024/annex-d/cognitive/r3/3rd."
  author-agent-dialogue: "Raise it when a student is stuck on a problem with several possible answers. Put it to a student as a skill you should be able to show by graduation, to think analytically and tackle problems, including ones with no single answer, and ask 'What are the possible answers here, and how would you choose between them?' For a programme team, ask which modules build and test it, and avoid presenting it as an extra beyond the minimum or reading the list aloud."
- statement: qaa/history-2022/4.6.b9
  forPractitioner: { text: "As a minimum generic skill, graduates should be able to grasp concepts and use them to give shape to arguments.", rewrite: light, force: should, status: drafted }
  forBeneficiary: { text: "To reach the minimum standard for your degree, you should be able to grasp concepts and use them to give shape to arguments.", rewrite: full, force: should, status: drafted }
  author-agent-written: "Treat this as a threshold generic skill for the History honours degree: it sits with the subject items of para 4.5 as part of the minimum (para 2.5) and refines the FHEQ level 6 descriptor qaa/fheq-2024/4.15.b3.1 (spine:6; FQHEIS level 10). Graduates should be able to grasp concepts and use them to give shape to arguments. Cite it as QAA (2022) History Subject Benchmark Statement, para 4.6, item 9; do not claim it holds at another level or is a legal requirement, and set it beside 4.5.b4 and 4.5.b12 and the third-class description qaa/fheq-2024/annex-d/knowledge/r2/3rd."
  author-agent-dialogue: "Raise it when a student uses concepts such as class, gender or empire loosely. Put it to a student as a skill you should be able to show by graduation, to grasp concepts and use them to give shape to arguments, and ask 'How are you defining this concept, and how does it shape your argument?' For a programme team, ask which modules build and test it, and avoid presenting it as an extra beyond the minimum or reading the list aloud."
- statement: qaa/history-2022/4.6.b10
  forPractitioner: { text: "As a minimum generic skill, graduates should be able to act with integrity, maturity and independence of mind.", rewrite: light, force: should, status: drafted }
  forBeneficiary: { text: "To reach the minimum standard for your degree, you should be able to act with integrity, maturity and independence of mind.", rewrite: full, force: should, status: drafted }
  author-agent-written: "Treat this as a threshold generic skill for the History honours degree: it sits with the subject items of para 4.5 as part of the minimum (para 2.5) and refines the FHEQ level 6 descriptor qaa/fheq-2024/4.15.b9.1 (spine:6; FQHEIS level 10). Graduates should be able to act with integrity, maturity and independence of mind. Cite it as QAA (2022) History Subject Benchmark Statement, para 4.6, item 10; do not claim it holds at another level or is a legal requirement, and set it beside 4.6.b14 and the third-class description qaa/fheq-2024/annex-d/transferable/r4/3rd."
  author-agent-dialogue: "Raise it when a student faces a choice about how to use others' work or how far to lean on a tutor. Put it to a student as a skill you should be able to show by graduation, to act with integrity, maturity and independence of mind, and ask 'Which judgements in this work are genuinely yours?' For a programme team, ask which modules build and test it, and avoid presenting it as an extra beyond the minimum or reading the list aloud."
- statement: qaa/history-2022/4.6.b11
  forPractitioner: { text: "As a minimum generic skill, graduates should be able to bring imagination, insight and creativity to their work.", rewrite: light, force: should, status: drafted }
  forBeneficiary: { text: "To reach the minimum standard for your degree, you should be able to bring imagination, insight and creativity to your work.", rewrite: full, force: should, status: drafted }
  author-agent-written: "Treat this as a threshold generic skill for the History honours degree: it sits with the subject items of para 4.5 as part of the minimum (para 2.5) and refines the FHEQ level 6 descriptor qaa/fheq-2024/4.15.b6 (spine:6; FQHEIS level 10). Graduates should be able to bring imagination, insight and creativity to their work. Cite it as QAA (2022) History Subject Benchmark Statement, para 4.6, item 11; do not claim it holds at another level or is a legal requirement, and set it beside 4.5.b12 and the third-class description qaa/fheq-2024/annex-d/cognitive/r4/3rd."
  author-agent-dialogue: "Raise it when a student wants to try an unusual approach or format. Put it to a student as a skill you should be able to show by graduation, to bring imagination, insight and creativity to your work, and ask 'What fresh angle could you take on this topic?' For a programme team, ask which modules build and test it, and avoid presenting it as an extra beyond the minimum or reading the list aloud."
- statement: qaa/history-2022/4.6.b12
  forPractitioner: { text: "As a minimum generic skill, graduates should be able to discipline and direct their own work.", rewrite: light, force: should, status: drafted }
  forBeneficiary: { text: "To reach the minimum standard for your degree, you should be able to discipline and direct your own work.", rewrite: full, force: should, status: drafted }
  author-agent-written: "Treat this as a threshold generic skill for the History honours degree: it sits with the subject items of para 4.5 as part of the minimum (para 2.5) and refines the FHEQ level 6 descriptor qaa/fheq-2024/4.15.b5 (spine:6; FQHEIS level 10). Graduates should be able to discipline and direct their own work. Cite it as QAA (2022) History Subject Benchmark Statement, para 4.6, item 12; do not claim it holds at another level or is a legal requirement, and set it beside 4.6.b1 and the third-class description qaa/fheq-2024/annex-d/transferable/r3/3rd."
  author-agent-dialogue: "Raise it when a student is managing deadlines or long stretches of independent study. Put it to a student as a skill you should be able to show by graduation, to discipline and direct your own work, and ask 'How do you plan a week of independent study?' For a programme team, ask which modules build and test it, and avoid presenting it as an extra beyond the minimum or reading the list aloud."
- statement: qaa/history-2022/4.6.b13
  forPractitioner: { text: "As a minimum generic skill, graduates should be able to take the initiative and make a habit of asking questions.", rewrite: light, force: should, status: drafted }
  forBeneficiary: { text: "To reach the minimum standard for your degree, you should be able to take the initiative and make a habit of asking questions.", rewrite: full, force: should, status: drafted }
  author-agent-written: "Treat this as a threshold generic skill for the History honours degree: it sits with the subject items of para 4.5 as part of the minimum (para 2.5) and refines the FHEQ level 6 descriptor qaa/fheq-2024/4.15.b9.1 (spine:6; FQHEIS level 10). Graduates should be able to take the initiative and make a habit of asking questions. Cite it as QAA (2022) History Subject Benchmark Statement, para 4.6, item 13; do not claim it holds at another level or is a legal requirement, and set it beside 4.6.b3 and the third-class description qaa/fheq-2024/annex-d/transferable/r4/3rd."
  author-agent-dialogue: "Raise it when a student waits to be told what to read or do. Put it to a student as a skill you should be able to show by graduation, to take the initiative and make a habit of asking questions, and ask 'What question would you like to pursue that nobody has set you?' For a programme team, ask which modules build and test it, and avoid presenting it as an extra beyond the minimum or reading the list aloud."
- statement: qaa/history-2022/4.6.b14
  forPractitioner: { text: "As a minimum generic skill, graduates should be able to understand academic integrity and the ethical duties raised by research and by drawing on other people's work.", rewrite: light, force: should, status: drafted }
  forBeneficiary: { text: "To reach the minimum standard for your degree, you should be able to understand academic integrity and the ethical duties raised by research and by drawing on other people's work.", rewrite: full, force: should, status: drafted }
  author-agent-written: "Treat this as a threshold generic skill for the History honours degree: it sits with the subject items of para 4.5 as part of the minimum (para 2.5) and refines the FHEQ level 6 descriptor qaa/fheq-2024/4.15.b2 (spine:6; FQHEIS level 10). Graduates should be able to understand academic integrity and the ethical duties raised by research and by drawing on other people's work. Cite it as QAA (2022) History Subject Benchmark Statement, para 4.6, item 14; do not claim it holds at another level or is a legal requirement, and set it beside 2.1 d) (2.1.b4) and the third-class description qaa/fheq-2024/annex-d/knowledge/r3/3rd."
  author-agent-dialogue: "Raise it when a student asks about referencing, plagiarism, generative tools or research ethics approval. Put it to a student as a skill you should be able to show by graduation, to understand academic integrity and the ethical duties raised by research and by drawing on other people's work, and ask 'How do you show which ideas are yours and which you have drawn from others?' For a programme team, ask which modules build and test it, and avoid presenting it as an extra beyond the minimum or reading the list aloud."
- statement: qaa/history-2022/4.6.b15
  forPractitioner: { text: "As a minimum generic skill, graduates should be able to express themselves with structure, coherence and clarity in speech and writing, and use digital tools with confidence.", rewrite: light, force: should, status: drafted }
  forBeneficiary: { text: "To reach the minimum standard for your degree, you should be able to express yourself with structure, coherence and clarity in speech and writing, and use digital tools with confidence.", rewrite: full, force: should, status: drafted }
  author-agent-written: "Treat this as a threshold generic skill for the History honours degree: it sits with the subject items of para 4.5 as part of the minimum (para 2.5) and refines the FHEQ level 6 descriptor qaa/fheq-2024/4.15.b8 (spine:6; FQHEIS level 10). Graduates should be able to express themselves with structure, coherence and clarity in speech and writing, and use digital tools with confidence. Cite it as QAA (2022) History Subject Benchmark Statement, para 4.6, item 15; do not claim it holds at another level or is a legal requirement, and set it beside 4.5.b11 and 3.10 a) and the third-class description qaa/fheq-2024/annex-d/transferable/r1/3rd."
  author-agent-dialogue: "Raise it when a student is preparing a presentation, essay or digital output. Put it to a student as a skill you should be able to show by graduation, to express yourself with structure, coherence and clarity in speech and writing, and use digital tools with confidence, and ask 'Could a reader follow your argument from your paragraph openings alone?' For a programme team, ask which modules build and test it, and avoid presenting it as an extra beyond the minimum or reading the list aloud."
- statement: qaa/history-2022/4.6.b16
  forPractitioner: { text: "As a minimum generic skill, graduates should be able to reflect on how they are progressing and act on feedback.", rewrite: light, force: should, status: drafted }
  forBeneficiary: { text: "To reach the minimum standard for your degree, you should be able to reflect on how you are progressing and act on feedback.", rewrite: full, force: should, status: drafted }
  author-agent-written: "Treat this as a threshold generic skill for the History honours degree: it sits with the subject items of para 4.5 as part of the minimum (para 2.5) and refines the FHEQ level 6 descriptor qaa/fheq-2024/4.15.b5 (spine:6; FQHEIS level 10). Graduates should be able to reflect on how they are progressing and act on feedback. Cite it as QAA (2022) History Subject Benchmark Statement, para 4.6, item 16; do not claim it holds at another level or is a legal requirement, and set it beside 4.4 on feedback and the third-class description qaa/fheq-2024/annex-d/transferable/r5/3rd."
  author-agent-dialogue: "Raise it when a student receives marked work or asks how to improve. Put it to a student as a skill you should be able to show by graduation, to reflect on how you are progressing and act on feedback, and ask 'What one change from your last feedback will you make in your next piece?' For a programme team, ask which modules build and test it, and avoid presenting it as an extra beyond the minimum or reading the list aloud."
- statement: qaa/history-2022/4.6.b17
  forPractitioner: { text: "As a minimum generic skill, graduates should be able to take part in current debates on global sustainability and on global perspectives.", rewrite: light, force: should, status: drafted }
  forBeneficiary: { text: "To reach the minimum standard for your degree, you should be able to take part in current debates on global sustainability and on global perspectives.", rewrite: full, force: should, status: drafted }
  author-agent-written: "Treat this as a threshold generic skill for the History honours degree: it sits with the subject items of para 4.5 as part of the minimum (para 2.5) and refines the FHEQ level 6 descriptor qaa/fheq-2024/4.15.b8 (spine:6; FQHEIS level 10). Graduates should be able to take part in current debates on global sustainability and on global perspectives. Cite it as QAA (2022) History Subject Benchmark Statement, para 4.6, item 17; do not claim it holds at another level or is a legal requirement, and set it beside 1.16 to 1.18 and std:doc:qaa-advancehe-esd-2021-guidance and the third-class description qaa/fheq-2024/annex-d/summary/r1/3rd."
  author-agent-dialogue: "Raise it when a student links a topic to climate, environment or global inequality. Put it to a student as a skill you should be able to show by graduation, to take part in current debates on global sustainability and on global perspectives, and ask 'How does the history you are studying bear on a present global challenge?' For a programme team, ask which modules build and test it, and avoid presenting it as an extra beyond the minimum or reading the list aloud."
```

### S5 Levels and alignment
<!-- label: both; status: drafted; basis: primary -->
```yaml
levels:
  - { id: "fheq:6", role: "cites", locator: "D1, 2.3; 4.2" }
  - { id: "fqheis:10", role: "cites", locator: "D1, 2.3; 4.2" }
crosswalks:
  - { from: "fheq:6", to: "fqheis:10", relation: "equivalent", basis: "stated (D1, 2.3: a degree with honours at FHEQ Level 6 and FQHEIS Level 10; 4.2: Annex D for both); matches std:doc:qaa-fheq-2024-framework S5, Table 1" }
```

### S6 Themes
<!-- label: both; status: drafted; basis: primary -->
```yaml
- { id: "theme:edi", role: "carries", carriedIn: ["1.12", "1.13", "1.14", "3.7", "3.11"] }
- { id: "theme:accessibility", role: "carries", carriedIn: ["2.2", "2.8"] }
- { id: "theme:esd", role: "carries", carriedIn: ["1.5", "1.16", "1.17", "1.18", "3.7", "3.11", "4.6"] }
- { id: "theme:enterprise", role: "carries", carriedIn: ["1.19", "1.20", "1.21"] }
```

### S7 Relations
<!-- label: both; status: drafted; basis: primary -->
```yaml
- { rel: "partOf", target: "collection: QAA Subject Benchmark Statements", note: "one of 54 held by stan" }
- { rel: "supersedes", target: "std:doc:qaa-history-2019-benchmarks (not ingested)", note: "the fourth edition, 2019; this is the fifth (D1, back matter)" }
- { rel: "refersTo", target: "std:doc:qaa-fheq-2024-framework, Annex D", note: "cited at 4.2 as Annex D: Outcome classification descriptions for FHEQ Level 6 and FQHEIS Level 10 degrees; now part of the Frameworks 2024" }
- { rel: "refersTo", target: "std:doc:qaa-fheq-2024-framework", note: "fheq:6 (2.3, 4.2)" }
- { rel: "refersTo", target: "std:doc:qaa-fqheis-2024-framework", note: "fqheis:10 (2.3, 4.2)" }
- { rel: "refersTo", target: "std:doc:qaa-advancehe-esd-2021-guidance", note: "cited at 1.16 and in the list of references" }
- { rel: "refersTo", target: "QAA Quality Code, Advice and Guidance (not yet ingested)", note: "front matter" }
- { rel: "refersTo", target: "QAA Glossary (not ingested)", note: "front matter" }
```

### S8 Currency and review
<!-- label: source; status: drafted; basis: primary -->
```yaml
published: "2022-03"
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
- The study of the whole human past, from human origins to recent events, tracing change and continuity across society, politics, economics, culture, ideas and environments (D1, 1.4).
- Allied to the humanities, arts and social sciences, yet distinct in its sense of the past, its respect for context and its rigorous handling of evidence (D1, 1.5, 1.6).
- No fixed canon: historians recognise no required body of knowledge or core, so courses legitimately differ in content, teaching and assessment (D1, 1.9 to 1.11).
- Six central features: depth of time; geographical range and comparison; close work on primary sources; critical, historiographical and ethical awareness; varied specialisms; an extended independent piece of work (D1, 2.1).
- A non-sequential subject: progression is cumulative and qualitative rather than a fixed order of modules (D1, 2.3, 2.4).
- Multi-perspectival and, by its own account, uncomfortable, attending to non-dominant and marginalised cultures (D1, 1.12, 1.13).

### SB2 Themes in this subject
<!-- label: both; status: drafted; basis: primary -->
```yaml
- theme: theme:edi
  inThisSubject: "the subject recovers the diversity of past experience and is multi-perspectival; it faces uncomfortable pasts, attends to marginalised cultures and commits its community to widening participation, inclusive curricula and decolonising the curriculum (D1, 1.12 to 1.14); teaching methods should be inclusive (D1, 3.7)"
  statements: ["qaa/history-2022/3.7"]
- theme: theme:accessibility
  inThisSubject: "courses aim to be highly accessible through varied teaching and assessment, digital resources and attention to students facing practical barriers: disability, health conditions, caring, commuting, low income and religious observance (D1, 2.2); flexible and part-time delivery follow (D1, 2.8)"
  statements: []
- theme: theme:esd
  inThisSubject: "headed Sustainability: content and method serve the UN goals, with environmental, public, economic and cultural history to the fore, links to heritage and conservation, and a mindset of change, continuity and causation (D1, 1.16 to 1.18); a generic skill and teaching methods carry it (D1, 4.6, 3.7)"
  statements: ["qaa/history-2022/3.7", "qaa/history-2022/4.6.b17"]
- theme: theme:enterprise
  inThisSubject: "headed Entrepreneurship and enterprise education: employability built into modules through real-world tasks such as policy papers, group work and presentations; career resilience; a wide spread of graduate careers (D1, 1.19 to 1.21)"
  statements: ["qaa/history-2022/1.20"]
```

### SB3 Content and delivery
<!-- label: both; status: drafted; basis: primary -->
```yaml
areas:
  - { component: "2.1", gloss: "six central features of course design: time depth, geographical range, primary sources, critical awareness, varied specialisms, extended work" }
  - { component: "3.1", gloss: "breadth and depth vary by department and module choice, resting on sections 1 and 2" }
practices:
  - { component: "3.2", kind: "teaching", gloss: "student-centred, blended, in classrooms, libraries, online and at museums, galleries and heritage sites" }
  - { component: "3.3", kind: "teaching", gloss: "lectures in many formats, including online and flipped" }
  - { component: "3.4", kind: "learning", gloss: "seminars and workshops in small groups, with preparatory tasks" }
  - { component: "3.5", kind: "learning", gloss: "independent study as the main mode, guided by reading lists" }
  - { component: "3.6", kind: "learning", gloss: "regular critical and constructive comment from staff" }
  - { component: "2.9", kind: "learning", gloss: "work placements and work-related projects, history-related or not" }
  - { component: "3.9", kind: "assessment", gloss: "varied modes so every student can show their abilities" }
  - { component: "3.10", kind: "assessment", gloss: "six kinds of assessment, including one major staged enquiry" }
  - { component: "3.11", kind: "assessment", gloss: "each department's own mix, covering every outcome, with information and feedback" }
```

### SB4 Benchmark standards
<!-- label: both; status: drafted; basis: primary -->
```yaml
rungs:
  - { rung: "threshold", leadIn: "4.5", award: "bachelor's with honours", items: 29 }
rungBases: "4.1 calls section 4 the minimum threshold standards for an honours degree. 4.5, headed Minimum threshold standards, holds the 12 subject-specific items; 4.6, headed Generic skills, holds 17 more under the same lead-in, threshold by 2.5 ('threshold-level subject-specific and generic skills'). No typical or excellent rung: 4.2 sends providers to Annex D for the classes above threshold."
outcomeLists:
  - { leadIn: "1.7", gloss: "outcomes on graduating with honours, in the account of the purposes; restated more briefly as the 4.5 threshold items, item for item", items: 12, award: ["honours"] }
outcomes: []
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
[]
```

### SB6 Cross-cutting references
<!-- label: both; status: drafted; basis: primary -->
```yaml
themes:
  - { id: "theme:edi", named: "Equality, diversity and inclusion", carriedIn: ["1.12", "1.13", "1.14", "3.7", "3.11"], statements: ["3.7"] }
  - { id: "theme:accessibility", named: "Accessibility", carriedIn: ["2.2", "2.8"], statements: [] }
  - { id: "theme:esd", named: "Sustainability (front matter: education for sustainable development; 3.7: Education for Sustainable Development)", carriedIn: ["1.5", "1.16", "1.17", "1.18", "3.7", "3.11", "4.6"], statements: ["3.7", "4.6.b17"] }
  - { id: "theme:enterprise", named: "Entrepreneurship and enterprise education (front matter: employability, entrepreneurship and enterprise education)", carriedIn: ["1.19", "1.20", "1.21"], statements: ["1.20"] }
frameworks:
  - { framework: "fheq", levels: ["fheq:6"], citedIn: ["2.3", "4.2"] }
  - { framework: "scqf", levels: ["fqheis:10"], citedIn: ["2.3", "4.2"] }
bodies: []
sharedDocuments:
  - { document: "std:doc:qaa-fheq-2024-framework, Annex D", named: "Annex D: Outcome classification descriptions for FHEQ Level 6 and FQHEIS Level 10 degrees", citedIn: ["4.2"], role: "descriptions of the four honours classes (1st, 2:1, 2:2, 3rd); the only account of standards above threshold" }
  - { document: "std:doc:qaa-advancehe-esd-2021-guidance", named: "QAA and Advance HE, Education for Sustainable Development Guidance", citedIn: ["1.16", "section 5"], role: "frame for the sustainability theme" }
  - { document: "UN Sustainable Development Goals (external)", named: "UN Sustainable Development Goals", citedIn: ["1.16"], role: "what the subject can contribute to" }
  - { document: "Prospects and HESA graduate outcomes data (external)", named: "Prospects and HESA", citedIn: ["1.21", "section 5"], role: "data on graduate careers" }
  - { document: "QAA Quality Code, Advice and Guidance (not yet ingested)", named: "Advice and Guidance to support the Quality Code", citedIn: ["front matter"], role: "course design, teaching, external expertise, monitoring" }
  - { document: "QAA Glossary (not ingested)", named: "QAA's Glossary", citedIn: ["front matter"], role: "explains unfamiliar terms" }
  - { document: "OfS regulatory framework; Quality Assessment Framework for Wales; Quality Enhancement Framework (Scotland) (not ingested)", named: "Office for Students' regulatory framework; Quality Assessment Framework for Wales; Quality Enhancement Framework", citedIn: ["front matter"], role: "the statement's standing in each nation" }
```

## Part B Terminology
<!-- The statement has no glossary of its own unless Part E says so; these are terms it defines in its text. -->

### B1 Concepts
<!-- label: both; status: drafted; basis: primary -->
```yaml
- { slug: "historiography", definition: "the study of how history has been written (D1, 2.1 d)", beneficiaryDefinition: "how historians have written about the past and why their accounts differ", scopeNote: "expected to show across all modules, not only in a dedicated one", category: "unknown", practices: ["education"] }
- { slug: "primary-source", definition: "any evidence from the past that is under examination, whether textual, visual, material or oral (D1, 1.7; 2.1 c)", beneficiaryDefinition: "material made in the period you are studying", scopeNote: "close work on it is called essential (2.1 c)", category: "unknown", practices: ["education"] }
- { slug: "formative-assessment", definition: "assessment meant as feedback on progress (D1, 1.11)", beneficiaryDefinition: "work that is marked to help you improve, not to count towards your degree", scopeNote: "set against summative assessment", category: "unknown", practices: ["education"] }
- { slug: "summative-assessment", definition: "assessment chiefly for awarding and classifying the degree (D1, 1.11)", beneficiaryDefinition: "work that counts towards your degree result", scopeNote: "set against formative assessment", category: "unknown", practices: ["education"] }
- { slug: "extended-piece-of-work", definition: "an independent extended piece of work under supervision, often called a dissertation or final year project, usually source-based or historiographical (D1, 2.1 f; 3.10 f)", beneficiaryDefinition: "your own long project, such as a dissertation", scopeNote: "one of the six features (2.1 f) and an assessment the course should include (3.10 f)", category: "unknown", practices: ["education"] }
- { slug: "flipped-lecture", definition: "a lecture students meet online first and then build on in class discussion and reflection (D1, 3.3)", beneficiaryDefinition: "a lecture you watch beforehand and then discuss in class", scopeNote: "one of several lecture formats", category: "unknown", practices: ["education"] }
- { slug: "threshold-standard", definition: "the minimum a student will have shown on being awarded honours in History (D1, 4.1, 4.5)", beneficiaryDefinition: "the minimum you need to show to gain your degree", scopeNote: "the only rung stated; classes above it are in Annex D (4.2)", category: "unknown", practices: ["education"] }
- { slug: "departments-or-history-subject-groups", definition: "the statement's term for the unit that teaches History, whether a department or part of a wider cluster (D1, 1.3)", beneficiaryDefinition: "the staff group that runs your History course", scopeNote: "used throughout", category: "unknown", practices: ["education"] }
```

### B2a Terms as the issuer defines them
<!-- label: source; status: drafted; basis: primary -->
```yaml
- { concept: "historiography", form: "historiography", lang: "en", partOfSpeech: "noun", termStatus: "preferred", register: "discipline-specific" }
- { concept: "primary-source", form: "primary sources", lang: "en", partOfSpeech: "noun-phrase", termStatus: "preferred", register: "discipline-specific" }
- { concept: "formative-assessment", form: "formative assessment", lang: "en", partOfSpeech: "noun-phrase", termStatus: "preferred", register: "formal" }
- { concept: "summative-assessment", form: "summative assessment", lang: "en", partOfSpeech: "noun-phrase", termStatus: "preferred", register: "formal" }
- { concept: "extended-piece-of-work", form: "extended piece of work", lang: "en", partOfSpeech: "noun-phrase", termStatus: "preferred", register: "formal" }
- { concept: "extended-piece-of-work", form: "dissertation", lang: "en", partOfSpeech: "noun", termStatus: "admitted", register: "formal" }
- { concept: "extended-piece-of-work", form: "final year project", lang: "en", partOfSpeech: "noun-phrase", termStatus: "admitted", register: "formal" }
- { concept: "flipped-lecture", form: "'flipped' lectures", lang: "en", partOfSpeech: "noun-phrase", termStatus: "preferred", register: "formal" }
- { concept: "threshold-standard", form: "minimum threshold standards", lang: "en", partOfSpeech: "noun-phrase", termStatus: "preferred", register: "formal" }
- { concept: "departments-or-history-subject-groups", form: "departments or History subject groups", lang: "en", partOfSpeech: "noun-phrase", termStatus: "preferred", register: "formal" }
```

### B2b Associated vocabulary
`not-applicable-by-design`: the statement names no wider vocabulary.

### B3 Framework blocks
`not-applicable-by-design`: no term is defined its own way for one component.

### B4 Relations
<!-- label: both; status: drafted; basis: primary -->
```yaml
- { rel: "contrasts-with", from: "formative-assessment", to: "summative-assessment", note: "1.11" }
```

## Part C Process
<!-- label: both; status: drafted; basis: primary -->

### C0 Formality
`not-applicable`: the statement sets out what graduates achieve and what courses provide, not a procedure.

## Part D Sources
```yaml
- key: D1
  issuer: The Quality Assurance Agency for Higher Education
  title: "Subject Benchmark Statement History"
  edition: "March 2022 (fifth edition)"
  year: 2022
  url: unknown (the QAA page; the text came by stan's extraction)
  retrieved: "held from stan: wkspc2615-QAAVector mapped/history-2022/history-2022.raw.txt, commit 366bcb99a01118f2c4c3ebfa2a8337596bddc455; received 2026-10-03"
  licence: QAA copyright
  tier: primary
  readVia: direct
  held: db38993fdf620a2955b0f9bc2a33910eda84d551197c0610941606bfeebd5c6d
  heldFiles: ["wkspc2601-library/txt/qaa-2022-history-subject-benchmark-statement-standard.txt", "wkspc2601-library/txt/qaa-2022-history-subject-benchmark-statement-standard.norm.txt", "wkspc2601-library/records/qaa-2022-history-subject-benchmark-statement-standard.chunks.json", "wkspc2601-library/records/qaa-2022-history-subject-benchmark-statement-standard.held.json"]
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
- SB4, rungs: one rung only, threshold. 4.5 (Minimum threshold standards, 12 subject-specific items) and 4.6 (Generic skills, 17 items) share one lead-in wording; 4.6 is recorded as threshold on 2.5's words "threshold-level subject-specific and generic skills" (the skeleton gave 4.6 no rung). No typical or excellent rung; 4.2 leaves the classes above threshold to Annex D. Pattern as Archaeology, unlike Psychology. For P3: confirm 4.6 as threshold.
- SB4, force: the threshold lead-ins say "should be able to"; force is recorded as should, the issuer's modal, not as threshold, although 4.1 and 4.5's heading call the lists the minimum. For Abbott: should a rung list with "should" take force threshold?
- SB4, gradeOf: none, since one rung is stated. SB4 outcomes is empty.
- S4, 1.7 and 4.5: the outcome list in section 1 (1.7, "should be able to") runs item for item with the 4.5 threshold list, 4.5 being shorter (4.5.b6 to b10 drop 1.7's second clauses). Both are recorded, as the template counts every outcome-list item; 1.7 is rung none. For P3: keep 1.7 or treat it as a duplicate of 4.5.
- S4, 1.5: its 18 items ("Students of history develop ... the ability to") repeat 4.6 almost word for word (1.5.b6 "evidence", 4.6.b6 "sources"; 1.5 splits digital literacy into its own item). The lead-in is plain present with no modal, so 1.5 is an S3 stem, not statements; 4.6 carries the standard.
- S4, 1.20: "requires History students to be proficient" is recorded with force must ("required" is must, batch-1 convention); the sentence describes what the work demands rather than imposing a rule. For Abbott.
- S4, obliging words outside the five, recorded as describes: "is essential" (2.1.b3, 2.1 c)), "are expected to" (2.1.b4, 2.1 d)), "it is the responsibility of departments" (2.4), "it is expected that" (2.5). Also "are essential" in 3.6 and "a shared commitment to and responsibility for" in 1.14, not taken (descriptive). For Abbott.
- S4, 2.1: the six features a) to f) are run-in letters inside one paragraph; ids 2.1.b2 to 2.1.b4 follow the letters (b = 2, c = 3, d = 4). a), e) and f) state plain-present norms ("Courses introduce students", "Students are introduced", "the student is enabled") and are not statements.
- S4, plain-present provider norms not taken as statements (template open point 5): 1.10, 1.11, 2.1 a), e), f), 2.2, 3.5, 3.6, 3.8, 4.4 ("Published criteria and grade descriptors are available"). Predictive or permissive "will" and "may" not taken: 1.3, 2.3 ("a History student will progress"), 2.7, 2.9, 2.12 ("external examiners will be asked"), 4.1, 4.3.
- S4, 4.1 is the rung's definition ("the minimum threshold standards that student will have demonstrated"), recorded in SB4 rungBases, not as a statement.
- S4, 3.10: the skeleton cut only one item (e) and f) run together over the page break); a) to f) are re-cut by find as 3.10.b1 to b6, taking "These should include" as lead-in. 3.10.b6 keeps the extraction's broken words ("task-s etti ng", "wri tten", "re quired") in its source.
- S4, verbs: 4.6.b16's span has "re flect" split by extraction, so only "make" is recorded; 4.6.b17 ("contempora ry", "relati ng", "sustainabilit y") and 4.6.b7 ("arg uments") also carry split words in source. 2.1.b3 has no action verb in its span.
- S4, provider statements carry no student version (2.1.b2, 2.4, 2.11, 3.7, 3.9, 3.10.b1 to b6, 3.11, 4.2).
- S5: fheq:6 and fqheis:10 are stated together at 2.3 and 4.2. 2.7 names exit awards (CertHE, DipHE) and four-year Scottish honours without levels; by the FHEQ document (S5, Table 1) these would be fheq:4 and fheq:5: inferred, not recorded as cited.
- S6 and SB6: theme paragraphs read from what each paragraph says; the skeleton's hits on 1.11, 1.15, 2.1 and 1.18 came from section headings that the extraction ran onto the end of those paragraphs, and were dropped. 1.15 ("environmental responsibility", "social justice") is not tagged esd or edi. 2.9 (placements) is linked from 1.19 but does not name enterprise: not tagged.
- SB5 and SB6 bodies: no professional, statutory or regulatory body is named in the body text; PSRBs appear generically in the front matter, and the Royal Historical Society, the Historical Association, The National Archives and the Disabled Students' Commission only in the advisory group back matter (excluded). Prospects and HESA (1.21) are data sources, listed in sharedDocuments.
- S2, statedSubjects: no HECoS term for public, cultural, political or gender history; the generic history code covers them.
- S7: the fourth edition (2019) is named in the back matter only; std:doc:qaa-history-2019-benchmarks is our id for it, not ingested.
- S1, licence: the text gives a copyright notice and no re-use terms (template open point 3).
- S9: not researched in P1.
- Patterns that differ from Psychology: one rung only (threshold), no typical or excellent; generic skills given as a threshold list of their own (4.6) rather than an outcome list; an outcome list (1.7) duplicating the threshold list; lead-ins in "should be able to"; no PSRB; four themes, all in section 1 under their own headings; Annex D cited at 4.2 as part of the 2024 Frameworks.
- ST-12: versions here run to the lengths the content needs; no length range is yet set.

---

## Change notes
- 0.1.2, 3 October 2026, 21:02: moved with its held text from UNI to the source library repo (`wkspc2601-library/ingested/standards/`, texts in `txt/`, records in `records/`); paths only (Abbott, 20:56; std N-0119).
- 0.1.1, 3 October 2026, 20:20: obliging words outside the five read as must, "ought to" as should, on statements outside the rungs, each marked on its force line (Abbott, 20:17; D-std-0016).
- 0.1.0, 2026-10-03 17:29: researched by run frame 0.1.1-draft and standards run layer 0.7.0-draft, std, run 0110 (P1); built by tools/bm_build.py.
