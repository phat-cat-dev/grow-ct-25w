---
id: std:doc:qaa-economics-2023-benchmarks
title: "Subject Benchmark Statement Economics"
profile: standards/subject-benchmark
profileVersion: 0.2.0-draft
issuer: QAA
kind: subject-benchmark
jurisdiction: [UK]
subjectScope: subjects
subjects:
  - { scheme: "hecos", code: "100450", label: "economics", basis: "stated" }
  - { scheme: "cah", code: "CAH15-02-01", label: "economics", basis: "stated" }
  - { scheme: "cah", code: "CAH15-02", label: "economics", basis: "stated" }
  - { scheme: "cah", code: "CAH15", label: "social sciences", basis: "stated" }
  - { scheme: "hecos", code: "100604", label: "econometrics", basis: "stated" }
  - { scheme: "hecos", code: "101401", label: "microeconomics", basis: "stated" }
  - { scheme: "hecos", code: "101402", label: "macroeconomics", basis: "stated" }
  - { scheme: "hecos", code: "100301", label: "economic history", basis: "stated" }
  - { scheme: "hecos", code: "100452", label: "international economics", basis: "inferred" }
  - { scheme: "hecos", code: "100601", label: "economic policy", basis: "inferred" }
edition: "March 2023 (fifth edition)"
published: 2023-03
status: current
supersedes: "the fourth edition (2019; not yet ingested): std:doc:qaa-economics-2019-benchmarks"
heldText: { method: sha256-bytes, raw: 058755dbafe46dd0062991296954510fefece33e153e98a9184ae8fd98b6f062, normalised: 64244d24a870e7f3e1e6bbdb1c8be7d1a3dd2a628b964d0aff1482161f0e2899 }
heldTextStan: { method: sha256-stan, raw: 058755dbafe46dd0062991296954510fefece33e153e98a9184ae8fd98b6f062, normalised: 8b198ed08a4f779da69b12788ce49980d5d4c47b617f7bb4a5d75a66c7efc4bb }
licence: "QAA copyright; held for study, private to the project, never published"
series: "QAA Subject Benchmark Statements, revised series with cross-cutting themes (2022 onward; recall, to check); fifth edition for Economics (D1, back cover)"
awardsCovered: ["bachelor's with honours"]
levelsCovered: ["fheq:6", "fqheis:10"]
nations: ["England", "Wales", "Scotland", "Northern Ireland"]
parts:
  S: full
  B: "partial: no glossary in the document (it points to QAA's Glossary); terms it defines in passing"
  C: "not-applicable: the document sets expectations, not a procedure"
pins: { structure: 0.13.0-draft, template: 0.8.0-draft, benchmarkTemplate: 0.6.0-draft, runFrame: 0.1.1-draft, runLayer: 0.7.0-draft, standards: none yet, terminology: none yet }
lifecycle: drafted
researchedBy: run frame 0.1.1-draft; standards run layer 0.7.0-draft; std, run 0102 (tools/bm_build.py)
passes:
  P1: "2026-10-03 17:10"
  P2: "skipped: read direct from the held text; inferred codes and rung links are for P3"
  P3: open
version: 0.1.2
---

<!-- from INGEST wpk-0016-ingest-pd-template-standards.md 0.8.0-draft and wpk-0016-ingest-pd-template-standards-benchmark.md 0.6.0-draft; built by tools/bm_build.py from run-src/ -->
# Subject Benchmark Statement: Economics (QAA, March 2023)

> Run 0102, P1 by std. The issuer's words are held in the source library, `wkspc2601-library/txt/qaa-2023-economics-subject-benchmark-statement-standard.norm.txt`; each S4 record carries its statement in full (`source`) for language analysis, with its span. Paraphrases and versions are ours. Private to the project, never published. In front matter `status` is the issuer's; ours is `lifecycle`. Doubts are in Part E.

## Part 0 Summary

### 0.1 Agent definition
<!-- label: editorial; status: drafted; basis: primary -->
QAA's UK reference point for what an Economics graduate should know, understand and be able to do at the end of a bachelor's degree with honours, single or with economics as the major part: three rungs of achievement (threshold, typical, excellent) of eight items each, two lists of core abilities and course outcomes, and a few expectations on courses. Reach for it when designing, reviewing or describing an economics course or its outcomes. It is not a curriculum, not an accreditation standard and not a regulatory requirement in England.

### 0.2 Summary
<!-- label: both; status: drafted; basis: primary -->
Published by QAA in March 2023 as the fifth edition, the statement describes economics as a social science, the purposes and distinctive features of a degree, its content, teaching and assessment; it then sets benchmark standards at threshold, typical and excellent levels for honours degrees (FHEQ level 6, FQHEIS level 10), with the eight items running in parallel across the three rungs. It adds the four cross-cutting themes (equality, diversity and inclusion; accessibility; sustainability; enterprise and entrepreneurship education), aligns its core skills with the Advance HE and QAA ESD guidance and the UN SDGs, and points to Annex D's degree classification descriptions for achievement above threshold. It names no accrediting body; PSRBs appear only in general terms and the Royal Economic Society as a widening-participation partner.

## Part S Standard

### S1 Identity
<!-- label: source; status: drafted; basis: primary -->
```yaml
issuer: The Quality Assurance Agency for Higher Education
title: "Subject Benchmark Statement Economics"
edition: "March 2023 (fifth edition)"
dates:
  published: 2023-03
  other: []
kind: subject-benchmark
jurisdiction: [UK]
authority: "reference: a sector reference point, \"not a regulatory requirement\" (D1, front matter); in England not a sector-recognised standard under the OfS framework; a key reference point in Wales and Scotland; part of the quality arrangements in Northern Ireland (D1, front matter: Relationship to legislation)"
licence: "QAA copyright; the document gives no re-use terms in its text (D1, front matter)"
copyrightNotice: { text: "© The Quality Assurance Agency for Higher Education 2023", locator: "D1, index" }
```

### S2 Purpose and scope
<!-- label: source; status: drafted; basis: primary -->
```yaml
governs: "the knowledge, understanding and skills expected of an Economics graduate on completing an honours degree, the nature of such degrees and the standards at three rungs (D1, front matter: About this Statement; 1.1; 4.1)"
appliesTo:
  awards: ["bachelor's degrees with honours in Economics, single honours or with Economics as a major component (4.1)", "combined, joint or major-minor routes (2.4; rungs not all expected where Economics is a minor component, 4.1)"]
  levels: ["fheq:6", "fqheis:10"]
  providers: ["UK higher education providers"]
whoMustUse: "none-stated; it is a reference point, not a requirement (D1, front matter)"
howUsed: ["design", "approval", "review", "other: external examining; PSRBs; information for prospective students and employers"]
doesNot: "it is not a national curriculum and does not prescribe teaching, learning or assessment; it carries no statutory or regulatory requirement (D1, front matter)"
beneficiary: the student
statedScope: "\"This document sets out benchmark standards for undergraduate degrees in Economics.\" (D1, 1.1)"
statedSubjects:
  - { name: "Economics", locator: "(D1, title; 1.1)", kind: "subject", codes: [{ scheme: "hecos", code: "100450", label: "economics" }, { scheme: "cah", code: "CAH15-02-01", label: "economics" }] }
  - { name: "a single honours degree in Economics and joint degrees where Economics is a major component", locator: "(D1, 4.1; 3.1)", kind: "programme title", codes: [{ scheme: "hecos", code: "100450", label: "economics" }] }
  - { name: "a combined, joint or major-minor route", locator: "(D1, 2.4)", kind: "programme title", codes: [{ scheme: "hecos", code: "100450", label: "economics" }] }
  - { name: "econometrics", locator: "(D1, 3.3; 3.5)", kind: "specialism", codes: [{ scheme: "hecos", code: "100604", label: "econometrics" }] }
  - { name: "the core fields of micro and macroeconomics", locator: "(D1, 1.3; 3.5)", kind: "specialism", codes: [{ scheme: "hecos", code: "101401", label: "microeconomics" }, { scheme: "hecos", code: "101402", label: "macroeconomics" }] }
  - { name: "economic history and history of economic thought", locator: "(D1, 2.2; 3.6)", kind: "specialism", codes: [{ scheme: "hecos", code: "100301", label: "economic history" }] }
  - { name: "international macroeconomics and finance; international trade and migration", locator: "(D1, 3.5)", kind: "specialism", codes: [{ scheme: "hecos", code: "100452", label: "international economics" }] }
  - { name: "political economy", locator: "(D1, 3.5)", kind: "specialism", codes: [{ scheme: "hecos", code: "100601", label: "economic policy" }] }
  - { name: "behavioural, development, environmental, experimental, health, labour, monetary and public economics; growth; industrial organisation", locator: "(D1, 3.5)", kind: "specialism", codes: [] }
subjects: see front matter (subjectScope subjects)
```

### S3 Structure
<!-- label: both; status: drafted; basis: primary -->
```yaml
components:
  - { number: "1.1", order: 3, componentType: paragraph, parent: "section 1", heading: "Context and purposes of an Economics degree", gloss: "what the statement covers: the subject, typical aims, knowledge and skills, learning and assessment and the three rungs" }
  - { number: "1.2", order: 4, componentType: paragraph, parent: "section 1", heading: "Purposes and characteristics of an Economics degree", gloss: "economics defined: decisions and interaction within institutions and power, allocation of resources, well-being and sustainability (S4 none)" }
  - { number: "1.3", order: 5, componentType: paragraph, parent: "section 1", heading: "Purposes and characteristics of an Economics degree", gloss: "micro and macro, static and dynamic analysis; contested interpretations call for plural perspectives and evidence (S4: the requirement of understanding)" }
  - { number: "1.4", order: 6, componentType: paragraph, parent: "section 1", heading: "Purposes and characteristics of an Economics degree", gloss: "a broad social science linked to many disciplines and core to finance, business and accounting" }
  - { number: "1.5", order: 7, componentType: paragraph, parent: "section 1", heading: "Purposes and characteristics of an Economics degree", gloss: "joint and innovative degrees; employment across sectors; knowing the limits of the tools; responsible citizenship" }
  - { number: "1.6", order: 8, componentType: stem, parent: "section 1", heading: "Purposes and characteristics of an Economics degree", gloss: "stem: the core intellectual abilities economists need (six items, S4)" }
  - { number: "1.7", order: 9, componentType: stem, parent: "section 1", heading: "Equality, diversity and inclusion (EDI)", gloss: "the subject studies discrimination and inequality; teachers should foster an inclusive community and embed EDI (S4), with example actions" }
  - { number: "1.8", order: 10, componentType: paragraph, parent: "section 1", heading: "Equality, diversity and inclusion (EDI)", gloss: "evidence-based debate on sensitive EDI questions, held inclusively" }
  - { number: "1.9", order: 11, componentType: paragraph, parent: "section 1", heading: "Equality, diversity and inclusion (EDI)", gloss: "the profession's narrow make-up and the need for compassionate, inclusive teaching" }
  - { number: "1.10", order: 12, componentType: paragraph, parent: "section 1", heading: "Accessibility", gloss: "teaching that answers the needs of the student body through an accessible, inclusive curriculum (S4)" }
  - { number: "1.11", order: 13, componentType: paragraph, parent: "section 1", heading: "Accessibility", gloss: "curricula in which a diverse community can recognise itself" }
  - { number: "1.12", order: 14, componentType: paragraph, parent: "section 1", heading: "Accessibility", gloss: "blended and online delivery since 2020: chances for inclusion and risks to equal access" }
  - { number: "1.13", order: 15, componentType: paragraph, parent: "section 1", heading: "Accessibility", gloss: "digital accessibility of graphs, media, data and software (S4)" }
  - { number: "1.14", order: 16, componentType: paragraph, parent: "section 1", heading: "Accessibility", gloss: "digital capability and published examples of accessibility practice" }
  - { number: "1.15", order: 17, componentType: paragraph, parent: "section 1", heading: "Sustainability", gloss: "sustainability framed by the UN SDGs and Global Compact, defined and woven into concepts and models" }
  - { number: "1.16", order: 18, componentType: paragraph, parent: "section 1", heading: "Sustainability", gloss: "graduates able to face the planetary crisis; critical and creative capacities beyond set tools (S4)" }
  - { number: "1.17", order: 19, componentType: stem, parent: "section 1", heading: "Sustainability", gloss: "stem: core skills aligned with the ESD guidance competencies and four named SDGs" }
  - { number: "1.18", order: 20, componentType: paragraph, parent: "section 1", heading: "Sustainability", gloss: "economics as a basis for sustainable, evidence-informed policy and for communicating it" }
  - { number: "1.19", order: 21, componentType: paragraph, parent: "section 1", heading: "Sustainability", gloss: "areas of economics that address environmental limits, valuation, market failure and equity" }
  - { number: "1.20", order: 22, componentType: paragraph, parent: "section 1", heading: "Enterprise and entrepreneurship education", gloss: "enterprise and entrepreneurship education: what it is and what it offers students" }
  - { number: "1.21", order: 23, componentType: paragraph, parent: "section 1", heading: "Enterprise and entrepreneurship education", gloss: "transferable skills relevant to enterprise" }
  - { number: "1.22", order: 24, componentType: paragraph, parent: "section 1", heading: "Enterprise and entrepreneurship education", gloss: "data software and data handling skills of graduates" }
  - { number: "1.23", order: 25, componentType: paragraph, parent: "section 1", heading: "Enterprise and entrepreneurship education", gloss: "communicating economics to wide audiences in many media" }
  - { number: "1.24", order: 26, componentType: paragraph, parent: "section 1", heading: "Enterprise and entrepreneurship education", gloss: "placements and work experience and the attributes they build" }
  - { number: "1.25", order: 27, componentType: paragraph, parent: "section 1", heading: "Enterprise and entrepreneurship education", gloss: "real-world, interdisciplinary application and how theory has changed with policy challenges" }
  - { number: "1.26", order: 28, componentType: paragraph, parent: "section 1", heading: "Enterprise and entrepreneurship education", gloss: "enterprise education beyond employment: a self-directed life and civic contribution" }
  - { number: "2.1", order: 30, componentType: paragraph, parent: "section 2", heading: "Design", gloss: "broad, rigorous design; a core of methods and tools applied in field modules" }
  - { number: "2.2", order: 31, componentType: stem, parent: "section 2", heading: "Design", gloss: "mathematics on entry and support (S4); research-led teaching; stem of eight typical course outcomes (S4)" }
  - { number: "2.3", order: 32, componentType: paragraph, parent: "section 2", heading: "Progression", gloss: "progression through levels to the threshold skills; readiness for postgraduate study" }
  - { number: "2.4", order: 33, componentType: paragraph, parent: "section 2", heading: "Progression", gloss: "joint and combined routes reach core skills and add others (S4)" }
  - { number: "2.5", order: 34, componentType: paragraph, parent: "section 2", heading: "Progression", gloss: "exit awards and four-year Scottish honours; part-time routes" }
  - { number: "2.6", order: 35, componentType: practice, parent: "section 2", heading: "Flexibility", gloss: "mixed modes of delivery, independent learning and varied materials" }
  - { number: "2.7", order: 36, componentType: paragraph, parent: "section 2", heading: "Partnership", gloss: "degree apprenticeships and placements with outside organisations" }
  - { number: "2.8", order: 37, componentType: paragraph, parent: "section 2", heading: "Partnership", gloss: "widening participation with the Royal Economic Society and others" }
  - { number: "2.9", order: 38, componentType: paragraph, parent: "section 2", heading: "Monitoring and review", gloss: "course monitoring and review, with students taking part (S4)" }
  - { number: "2.10", order: 39, componentType: paragraph, parent: "section 2", heading: "Monitoring and review", gloss: "external reviewers in periodic review (S4)" }
  - { number: "2.11", order: 40, componentType: paragraph, parent: "section 2", heading: "Monitoring and review", gloss: "external examiners and how the statement supports them" }
  - { number: "2.12", order: 41, componentType: paragraph, parent: "section 2", heading: "Monitoring and review", gloss: "accreditation of courses with professional outcomes by professional and regulatory bodies" }
  - { number: "3.1", order: 43, componentType: paragraph, parent: "section 3", heading: "Content", gloss: "content adapts to the degree; the statement does not prescribe forms of analysis" }
  - { number: "3.2", order: 44, componentType: area, parent: "section 3", heading: "Content", gloss: "stem and area: eight key concepts most courses cover (one item obliges, S4)" }
  - { number: "3.3", order: 45, componentType: paragraph, parent: "section 3", heading: "Content", gloss: "data, programming and econometric skills on real data (S4)" }
  - { number: "3.4", order: 46, componentType: paragraph, parent: "section 3", heading: "Content", gloss: "selecting and applying tools to applied topics and policy as an essential outcome (S4)" }
  - { number: "3.5", order: 47, componentType: area, parent: "section 3", heading: "Content", gloss: "stem and area: fourteen common applied fields" }
  - { number: "3.6", order: 48, componentType: area, parent: "section 3", heading: "Content", gloss: "economic history and the history of economic thought as context" }
  - { number: "3.7", order: 49, componentType: practice, parent: "section 3", heading: "Teaching and learning", gloss: "growing critical facility and independence; a range of teaching methods" }
  - { number: "3.8", order: 50, componentType: practice, parent: "section 3", heading: "Teaching and learning", gloss: "interactive, student-centred and blended learning since the pandemic" }
  - { number: "3.9", order: 51, componentType: practice, parent: "section 3", heading: "Teaching and learning", gloss: "resources and organisations that support economics teaching" }
  - { number: "3.10", order: 52, componentType: paragraph, parent: "section 3", heading: "Teaching and learning", gloss: "language, mathematics and study-skills support for diverse cohorts (S4)" }
  - { number: "3.11", order: 53, componentType: practice, parent: "section 3", heading: "Teaching and learning", gloss: "pluralist and decolonial approaches supporting inclusion" }
  - { number: "3.12", order: 54, componentType: practice, parent: "section 3", heading: "Assessment", gloss: "assessment design at module and course level" }
  - { number: "3.13", order: 55, componentType: practice, parent: "section 3", heading: "Assessment", gloss: "assessment that builds problem-solving and higher-order reasoning" }
  - { number: "3.14", order: 56, componentType: practice, parent: "section 3", heading: "Assessment", gloss: "a range of assessment forms, including authentic and data-based tasks" }
  - { number: "3.15", order: 57, componentType: practice, parent: "section 3", heading: "Assessment", gloss: "formative assessment and scaffolded skills development" }
  - { number: "4.1", order: 59, componentType: paragraph, parent: "section 4", heading: "Introduction", gloss: "where the rungs apply (single honours and major joint degrees); typical includes threshold" }
  - { number: "4.2", order: 60, componentType: paragraph, parent: "section 4", heading: "Introduction", gloss: "most students exceed the threshold; providers should use Annex D (S4)" }
  - { number: "4.3", order: 61, componentType: stem, parent: "section 4", heading: "Threshold level", gloss: "rung lead-in: threshold, eight items" }
  - { number: "4.4", order: 62, componentType: stem, parent: "section 4", heading: "Typical level", gloss: "rung lead-in: typical, eight items" }
  - { number: "4.5", order: 63, componentType: stem, parent: "section 4", heading: "Excellent level", gloss: "rung lead-in: excellent, eight items, shown consistently" }
  - { number: "1", componentType: section, parent: none, heading: "Context and purposes of an Economics degree", gloss: "section 1" }
  - { number: "2", componentType: section, parent: none, heading: "Distinctive features of an Economics degree", gloss: "section 2" }
  - { number: "3", componentType: section, parent: none, heading: "Content, structure and delivery", gloss: "section 3" }
  - { number: "4", componentType: section, parent: none, heading: "Benchmark standards", gloss: "section 4" }
excluded:
  - { number: "none", heading: "About this Statement; How can I use this document?; Relationship to legislation; Additional sector reference points", kind: "other: front matter, read for S1 and S2" }
  - { number: "none", heading: "Contents", kind: "contents" }
  - { number: "1 to 4", heading: "section heading lines", kind: "other: headings, kept as section components" }
  - { number: "5", heading: "List of references and further resources", kind: "references" }
  - { number: "6", heading: "Membership of the Advisory Groups for the Subject Benchmark Statement for Economics", kind: "acknowledgements" }
  - { number: "none", heading: "back cover: edition, publication date, membership note, copyright", kind: "other: read for S1 and S8" }
```

### S4 Statements
<!-- label: both; status: drafted; basis: primary. Only standards (D-std-0002 (a)): 52 records. `source` is the issuer's statement exactly as its span holds it (D-std-0014). -->
```yaml
- id: qaa/economics-2023/1.3
  locator: { number: "1.3", headingPath: ["Context and purposes of an Economics degree", "Purposes and characteristics of an Economics degree"] }
  span: { start: 9292, end: 9658 }
  source: "Studying economics requires an understanding of how resources are used and how economic and social entities, such as households, firms, governments and other institutions, behave and interact. This understanding is required at both the individual (micro) and the aggregate (macro) level as well as with respect to the relationship between the individual and society."
  stem: none
  statementType: requirement
  rung: none
  force: must
  level: fheq:6
  appliesTo: "students of the subject"
  addressee: learner
  verbs: ["requires", "behave", "interact", "required"]
  about: "understanding resource use and economic behaviour at micro and macro levels"
  themes: [none]
  domain: understanding
  award: ["bachelor's with honours"]
  gradeOf: none
  paraphrase: "Studying the subject must rest on understanding how resources are used and how households, firms, governments and other bodies behave and interact, at the level of the single actor, of the whole economy and of the link between person and society."
  quote: full   # the issuer's statement is in `source` (D-std-0014)
  audience: both
  subjects: inherited
- id: qaa/economics-2023/1.6.b1
  locator: { number: "1.6.b1", headingPath: ["Context and purposes of an Economics degree", "Purposes and characteristics of an Economics degree"] }
  span: { start: 12656, end: 12753 }
  source: "gather evidence and assimilate, structure, analyse and evaluate qualitative and quantitative data"
  stem: "1.6"
  statementType: outcome
  rung: none
  force: describes
  level: fheq:6
  appliesTo: "economists, and students in training"
  addressee: learner
  verbs: ["gather", "assimilate", "structure", "analyse", "evaluate"]
  about: "gathering evidence and handling data"
  themes: [none]
  domain: subject-skill
  award: ["bachelor's with honours"]
  gradeOf: none
  paraphrase: "Economists need to gather evidence and to take in, organise, analyse and judge data of both kinds, qualitative and quantitative."
  quote: full   # the issuer's statement is in `source` (D-std-0014)
  audience: both
  subjects: inherited
- id: qaa/economics-2023/1.6.b2
  locator: { number: "1.6.b2", headingPath: ["Context and purposes of an Economics degree", "Purposes and characteristics of an Economics degree"] }
  span: { start: 12756, end: 12833 }
  source: "abstract and simplify in order to identify and model the essence of a problem"
  stem: "1.6"
  statementType: outcome
  rung: none
  force: describes
  level: fheq:6
  appliesTo: "economists, and students in training"
  addressee: learner
  verbs: ["abstract", "simplify", "identify", "model"]
  about: "abstraction and modelling"
  themes: [none]
  domain: subject-skill
  award: ["bachelor's with honours"]
  gradeOf: none
  paraphrase: "Economists need to abstract and simplify so as to find and model what lies at the heart of a problem."
  quote: full   # the issuer's statement is in `source` (D-std-0014)
  audience: both
  subjects: inherited
- id: qaa/economics-2023/1.6.b3
  locator: { number: "1.6.b3", headingPath: ["Context and purposes of an Economics degree", "Purposes and characteristics of an Economics degree"] }
  span: { start: 12836, end: 12983 }
  source: "analyse and reason – deductively, abductively and inductively – using the tools of economics and prior research both within economics and elsewhere"
  stem: "1.6"
  statementType: outcome
  rung: none
  force: describes
  level: fheq:6
  appliesTo: "economists, and students in training"
  addressee: learner
  verbs: ["analyse", "reason", "using"]
  about: "deductive, abductive and inductive reasoning"
  themes: [none]
  domain: subject-skill
  award: ["bachelor's with honours"]
  gradeOf: none
  paraphrase: "Economists need to analyse and reason in deductive, abductive and inductive ways, drawing on economic tools and on earlier research inside and outside the subject."
  quote: full   # the issuer's statement is in `source` (D-std-0014)
  audience: both
  subjects: inherited
- id: qaa/economics-2023/1.6.b4
  locator: { number: "1.6.b4", headingPath: ["Context and purposes of an Economics degree", "Purposes and characteristics of an Economics degree"] }
  span: { start: 12986, end: 13088 }
  source: "communicate results concisely to a variety of audiences, including those with no training in economics"
  stem: "1.6"
  statementType: outcome
  rung: none
  force: describes
  level: fheq:6
  appliesTo: "economists, and students in training"
  addressee: learner
  verbs: ["communicate"]
  about: "communicating results to varied audiences"
  themes: [none]
  domain: generic-skill
  award: ["bachelor's with honours"]
  gradeOf: none
  paraphrase: "Economists need to report their results briefly to many kinds of audience, among them people with no economics background."
  quote: full   # the issuer's statement is in `source` (D-std-0014)
  audience: both
  subjects: inherited
- id: qaa/economics-2023/1.6.b5
  locator: { number: "1.6.b5", headingPath: ["Context and purposes of an Economics degree", "Purposes and characteristics of an Economics degree"] }
  span: { start: 13091, end: 13177 }
  source: "think critically about the limits of their analysis in a broader socioeconomic context"
  stem: "1.6"
  statementType: outcome
  rung: none
  force: describes
  level: fheq:6
  appliesTo: "economists, and students in training"
  addressee: learner
  verbs: ["think"]
  about: "the limits of analysis in its wider context"
  themes: [none]
  domain: understanding
  award: ["bachelor's with honours"]
  gradeOf: none
  paraphrase: "Economists need to think critically about where their analysis stops working within its broader social and economic setting."
  quote: full   # the issuer's statement is in `source` (D-std-0014)
  audience: both
  subjects: inherited
- id: qaa/economics-2023/1.6.b6
  locator: { number: "1.6.b6", headingPath: ["Context and purposes of an Economics degree", "Purposes and characteristics of an Economics degree"] }
  span: { start: 13180, end: 13349 }
  source: "draw economic policy inferences, to recognise the potential constraints in their implementation and to evaluate policy outcomes in the light of stated policy objectives."
  stem: "1.6"
  statementType: outcome
  rung: none
  force: describes
  level: fheq:6
  appliesTo: "economists, and students in training"
  addressee: learner
  verbs: ["draw", "recognise", "evaluate"]
  about: "policy inference, constraints and evaluation"
  themes: [none]
  domain: subject-skill
  award: ["bachelor's with honours"]
  gradeOf: none
  paraphrase: "Economists need to draw conclusions for policy, see what may limit putting them into practice and judge policy results against the aims set for them."
  quote: full   # the issuer's statement is in `source` (D-std-0014)
  audience: both
  subjects: inherited
- id: qaa/economics-2023/1.7
  locator: { number: "1.7", headingPath: ["Context and purposes of an Economics degree", "Equality, diversity and inclusion (EDI)"] }
  span: { start: 13586, end: 13788 }
  source: "Economics educators should aim to foster an inclusive learning community and consider how to embed EDI in learning materials (such as readings, lecture slides, videos, and so on), methods and processes."
  stem: none
  statementType: expectation
  rung: none
  force: should
  level: none
  appliesTo: "teaching staff in economics"
  addressee: provider
  verbs: ["aim", "foster", "consider", "embed"]
  about: "an inclusive learning community and EDI in materials and methods"
  themes: [theme:edi]
  domain: none
  award: ["none"]
  gradeOf: none
  paraphrase: "Teachers of economics should work towards an inclusive learning community and think about how to build equality, diversity and inclusion into their materials, methods and processes."
  quote: full   # the issuer's statement is in `source` (D-std-0014)
  audience: practitioner
  subjects: inherited
- id: qaa/economics-2023/1.10
  locator: { number: "1.10", headingPath: ["Context and purposes of an Economics degree", "Accessibility"] }
  span: { start: 16468, end: 16726 }
  source: "Pedagogic methods for teaching Economics will generally reflect the needs of the student body, with an inclusive curriculum that prioritises the accessibility, equity, appropriateness and resourcing of learning and teaching resources and materials being key."
  stem: none
  statementType: expectation
  rung: none
  force: will
  level: none
  appliesTo: "teaching in economics"
  addressee: provider
  verbs: ["reflect", "prioritises"]
  about: "teaching that answers student needs, with accessible resources"
  themes: [theme:accessibility]
  domain: none
  award: ["none"]
  gradeOf: none
  paraphrase: "Teaching methods will generally respond to what the students in a cohort need, with an inclusive curriculum that puts accessible, fair, suitable and properly resourced materials first."
  quote: full   # the issuer's statement is in `source` (D-std-0014)
  audience: practitioner
  subjects: inherited
- id: qaa/economics-2023/1.13
  locator: { number: "1.13", headingPath: ["Context and purposes of an Economics degree", "Accessibility"] }
  span: { start: 17529, end: 17709 }
  source: "As a discipline that utilises graphical and other visual tools, Economics pay attention to digital accessibility of materials which should include, for example, image descriptions."
  stem: none
  statementType: expectation
  rung: none
  force: should
  level: none
  appliesTo: "economics teaching materials"
  addressee: provider
  verbs: ["pay", "include"]
  about: "digital accessibility of visual materials, media and software"
  themes: [theme:accessibility]
  domain: none
  award: ["none"]
  gradeOf: none
  paraphrase: "Because economics relies on graphs and other visuals, its digital materials should be accessible, for instance through image descriptions; the paragraph goes on to ask for screen-reader-ready content, captions or transcripts, downloadable formats and accessible alternatives for data, software and coding."
  quote: full   # the issuer's statement is in `source` (D-std-0014)
  audience: practitioner
  subjects: inherited
- id: qaa/economics-2023/1.16
  locator: { number: "1.16", headingPath: ["Context and purposes of an Economics degree", "Sustainability"] }
  span: { start: 19994, end: 20572 }
  source: "Reflecting the UN SDGs and their educational implications, a governing purpose of Economics degrees is that graduates have developed capacities that enable them to cope with and attempt to create solutions for the planetary crisis of climate change, biodiversity loss, environmental injustice and potential, consequent instabilities. These problems are fundamentally transdisciplinary and highly dynamic and are characterised by pervasive uncertainty. As such, they require students to foster critical and creative capacities beyond the application of existing tools and models."
  stem: none
  statementType: requirement
  rung: none
  force: must
  level: fheq:6
  appliesTo: "graduates of the subject"
  addressee: learner
  verbs: ["developed", "cope", "create", "require", "foster"]
  about: "capacities to face the planetary crisis"
  themes: [theme:esd]
  domain: generic-skill
  award: ["bachelor's with honours"]
  gradeOf: none
  paraphrase: "A governing aim of the degree is that graduates can cope with, and try to solve, the planetary crisis (a changing climate, lost biodiversity, environmental injustice and the instability these bring); because such problems cross disciplines, change fast and are deeply uncertain, students must develop critical and creative capacities that go past applying familiar tools and models."
  quote: full   # the issuer's statement is in `source` (D-std-0014)
  audience: both
  subjects: inherited
- id: qaa/economics-2023/2.2
  locator: { number: "2.2", headingPath: ["Distinctive features of an Economics degree", "Design"] }
  span: { start: 26477, end: 26714 }
  source: "Where the degree does not require Maths A Levels for entry, the expectation is that suitable teaching and support is provided within the degree to ensure that students are able to engage with the more quantitative elements of the course."
  stem: none
  statementType: expectation
  rung: none
  force: must   # D-std-0016: "require" read as must
  level: none
  appliesTo: "courses admitting students without A level mathematics"
  addressee: provider
  verbs: ["require", "provided", "ensure", "engage"]
  about: "support for quantitative work where mathematics is not an entry condition"
  themes: [none]
  domain: none
  award: ["none"]
  gradeOf: none
  paraphrase: "Where entry does not call for A level mathematics, the issuer expects the degree itself to give suitable teaching and support so that students can take on its quantitative parts."
  quote: full   # the issuer's statement is in `source` (D-std-0014)
  audience: practitioner
  subjects: inherited
- id: qaa/economics-2023/2.2.b1
  locator: { number: "2.2.b1", headingPath: ["Distinctive features of an Economics degree", "Design"] }
  span: { start: 26993, end: 27086 }
  source: "A critical understanding of causality and analytical methods, both theoretical and empirical."
  stem: "2.2"
  statementType: outcome
  rung: none
  force: must   # D-std-0016: "require" read as must
  level: fheq:6
  appliesTo: "students on a typical Economics course"
  addressee: learner
  verbs: []
  about: "causality and analytical methods"
  themes: [none]
  domain: understanding
  award: ["bachelor's with honours"]
  gradeOf: none
  paraphrase: "A course is usually designed so that students critically understand causality and analytical methods, in theory and in empirical work."
  quote: full   # the issuer's statement is in `source` (D-std-0014)
  audience: both
  subjects: inherited
- id: qaa/economics-2023/2.2.b2
  locator: { number: "2.2.b2", headingPath: ["Distinctive features of an Economics degree", "Design"] }
  span: { start: 27089, end: 27262 }
  source: "An appreciation and understanding of the history and development of economic ideas and the differing methods of analysis that have been and are currently used by economists."
  stem: "2.2"
  statementType: outcome
  rung: none
  force: must   # D-std-0016: "require" read as must
  level: fheq:6
  appliesTo: "students on a typical Economics course"
  addressee: learner
  verbs: ["used"]
  about: "the history of economic ideas and methods"
  themes: [none]
  domain: knowledge
  award: ["bachelor's with honours"]
  gradeOf: none
  paraphrase: "A course is usually designed so that students appreciate and understand how economic ideas have developed and the different methods economists have used and use now."
  quote: full   # the issuer's statement is in `source` (D-std-0014)
  audience: both
  subjects: inherited
- id: qaa/economics-2023/2.2.b3
  locator: { number: "2.2.b3", headingPath: ["Distinctive features of an Economics degree", "Design"] }
  span: { start: 27265, end: 27447 }
  source: "An understanding of the historical context of contemporary problems addressed by economists, and, more generally, a knowledge of economic history as relevant to the learning context."
  stem: "2.2"
  statementType: outcome
  rung: none
  force: must   # D-std-0016: "require" read as must
  level: fheq:6
  appliesTo: "students on a typical Economics course"
  addressee: learner
  verbs: ["addressed"]
  about: "historical context and economic history"
  themes: [none]
  domain: knowledge
  award: ["bachelor's with honours"]
  gradeOf: none
  paraphrase: "A course is usually designed so that students understand the history behind present-day problems that economists tackle, and know economic history as fits the course."
  quote: full   # the issuer's statement is in `source` (D-std-0014)
  audience: both
  subjects: inherited
- id: qaa/economics-2023/2.2.b4
  locator: { number: "2.2.b4", headingPath: ["Distinctive features of an Economics degree", "Design"] }
  span: { start: 27450, end: 27517 }
  source: "An ability to apply economic reasoning and tools to applied topics."
  stem: "2.2"
  statementType: outcome
  rung: none
  force: must   # D-std-0016: "require" read as must
  level: fheq:6
  appliesTo: "students on a typical Economics course"
  addressee: learner
  verbs: ["apply"]
  about: "applying economic reasoning and tools"
  themes: [none]
  domain: subject-skill
  award: ["bachelor's with honours"]
  gradeOf: none
  paraphrase: "A course is usually designed so that students can use economic reasoning and tools on applied topics."
  quote: full   # the issuer's statement is in `source` (D-std-0014)
  audience: both
  subjects: inherited
- id: qaa/economics-2023/2.2.b5
  locator: { number: "2.2.b5", headingPath: ["Distinctive features of an Economics degree", "Design"] }
  span: { start: 27520, end: 27641 }
  source: "An ability to critically evaluate differences in policy recommendations in the context of their underlying methodologies."
  stem: "2.2"
  statementType: outcome
  rung: none
  force: must   # D-std-0016: "require" read as must
  level: fheq:6
  appliesTo: "students on a typical Economics course"
  addressee: learner
  verbs: ["evaluate"]
  about: "evaluating policy advice against its methods"
  themes: [none]
  domain: subject-skill
  award: ["bachelor's with honours"]
  gradeOf: none
  paraphrase: "A course is usually designed so that students can judge critically why policy recommendations differ, in the light of the methods behind them."
  quote: full   # the issuer's statement is in `source` (D-std-0014)
  audience: both
  subjects: inherited
- id: qaa/economics-2023/2.2.b6
  locator: { number: "2.2.b6", headingPath: ["Distinctive features of an Economics degree", "Design"] }
  span: { start: 27644, end: 27797 }
  source: "An ability to discuss, analyse and evaluate government policy and to assess the performance of the UK and other economies, as well as the global economy."
  stem: "2.2"
  statementType: outcome
  rung: none
  force: must   # D-std-0016: "require" read as must
  level: fheq:6
  appliesTo: "students on a typical Economics course"
  addressee: learner
  verbs: ["discuss", "analyse", "evaluate", "assess"]
  about: "government policy and economic performance"
  themes: [none]
  domain: subject-skill
  award: ["bachelor's with honours"]
  gradeOf: none
  paraphrase: "A course is usually designed so that students can debate, analyse and judge government policy and assess how the UK, other economies and the world economy perform."
  quote: full   # the issuer's statement is in `source` (D-std-0014)
  audience: both
  subjects: inherited
- id: qaa/economics-2023/2.2.b7
  locator: { number: "2.2.b7", headingPath: ["Distinctive features of an Economics degree", "Design"] }
  span: { start: 27800, end: 28100 }
  source: "An understanding of verbal, graphical, mathematical and econometric representation of economic ideas and analysis, including the relationship between them. Appropriate techniques to enable manipulation, treatment and interpretation of the relevant quantitative and qualitative data are also relevant."
  stem: "2.2"
  statementType: outcome
  rung: none
  force: must   # D-std-0016: "require" read as must
  level: fheq:6
  appliesTo: "students on a typical Economics course"
  addressee: learner
  verbs: ["enable"]
  about: "representing economic ideas and handling data"
  themes: [none]
  domain: understanding
  award: ["bachelor's with honours"]
  gradeOf: none
  paraphrase: "A course is usually designed so that students understand how economic ideas are expressed in words, graphs, mathematics and econometrics and how these relate, together with suitable techniques for working with and interpreting data."
  quote: full   # the issuer's statement is in `source` (D-std-0014)
  audience: both
  subjects: inherited
- id: qaa/economics-2023/2.2.b8
  locator: { number: "2.2.b8", headingPath: ["Distinctive features of an Economics degree", "Design"] }
  span: { start: 28103, end: 28322 }
  source: "An ability to articulate, communicate and present their arguments verbally and/or non-verbally and to both specialist and non-specialist audiences, who may have other kinds of expertise in relation to the issue at hand."
  stem: "2.2"
  statementType: outcome
  rung: none
  force: must   # D-std-0016: "require" read as must
  level: fheq:6
  appliesTo: "students on a typical Economics course"
  addressee: learner
  verbs: ["articulate", "communicate", "present"]
  about: "presenting arguments to specialist and general audiences"
  themes: [none]
  domain: generic-skill
  award: ["bachelor's with honours"]
  gradeOf: none
  paraphrase: "A course is usually designed so that students can put their arguments clearly, in speech or other forms, to specialists and non-specialists, including people with other expertise on the question."
  quote: full   # the issuer's statement is in `source` (D-std-0014)
  audience: both
  subjects: inherited
- id: qaa/economics-2023/2.4
  locator: { number: "2.4", headingPath: ["Distinctive features of an Economics degree", "Progression"] }
  span: { start: 29366, end: 29579 }
  source: "Undergraduates studying a combined, joint or major-minor route will achieve core elements of the specific and generic skills for the subject, and will add others according to the subjects covered in joint courses."
  stem: none
  statementType: expectation
  rung: none
  force: will
  level: fheq:6
  appliesTo: "students on combined, joint or major-minor routes"
  addressee: learner
  verbs: ["achieve", "add"]
  about: "joint and combined routes: the core skills plus others"
  themes: [none]
  domain: subject-skill
  award: ["bachelor's with honours"]
  gradeOf: none
  paraphrase: "Students on a combined, joint or major-minor route will gain the core subject-specific and generic skills of economics and will add others from the other subjects they take."
  quote: full   # the issuer's statement is in `source` (D-std-0014)
  audience: both
  subjects: inherited
- id: qaa/economics-2023/2.9
  locator: { number: "2.9", headingPath: ["Distinctive features of an Economics degree", "Monitoring and review"] }
  span: { start: 32051, end: 32288 }
  source: "Degree-awarding bodies and their collaborative partnerships routinely collect and analyse information and undertake periodic course review according to their own needs, and students should form part of this monitoring and review process."
  stem: none
  statementType: expectation
  rung: none
  force: should
  level: none
  appliesTo: "degree-awarding bodies and their partners"
  addressee: provider
  verbs: ["collect", "analyse", "undertake", "form"]
  about: "students taking part in monitoring and review"
  themes: [none]
  domain: none
  award: ["none"]
  gradeOf: none
  paraphrase: "Degree-awarding bodies and their partners review courses periodically for their own purposes, and students should take part in that monitoring and review."
  quote: full   # the issuer's statement is in `source` (D-std-0014)
  audience: practitioner
  subjects: inherited
- id: qaa/economics-2023/2.10
  locator: { number: "2.10", headingPath: ["Distinctive features of an Economics degree", "Monitoring and review"] }
  span: { start: 32791, end: 33016 }
  source: "Higher education providers will use external reviewers as part of periodic review to gain an external perspective on any proposed changes and ensure threshold standards are achieved and content is appropriate for the subject."
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
  award: ["none"]
  gradeOf: none
  paraphrase: "Providers will bring in external reviewers during periodic review to gain an outside view of proposed changes, make sure threshold standards are met and check that content suits the subject."
  quote: full   # the issuer's statement is in `source` (D-std-0014)
  audience: practitioner
  subjects: inherited
- id: qaa/economics-2023/3.2.b5
  locator: { number: "3.2.b5", headingPath: ["Content, structure and delivery", "Content"] }
  span: { start: 36211, end: 36547 }
  source: "Marginal considerations - economists are trained to recognise that important decisions often relate to small variations in key variables and parameters. Students should also be aware of the limitations of marginal analysis in cases where there are strong threshold effects or discontinuities such as in the analysis of planetary crises."
  stem: "3.2"
  statementType: expectation
  rung: none
  force: should
  level: fheq:6
  appliesTo: "students of the subject"
  addressee: learner
  verbs: ["trained", "recognise"]
  about: "marginal analysis and its limits"
  themes: [none]
  domain: understanding
  award: ["bachelor's with honours"]
  gradeOf: none
  paraphrase: "Economists learn that key decisions often turn on small changes in variables and parameters; students should also know where marginal analysis fails, as with strong threshold effects or discontinuities such as planetary crises."
  quote: full   # the issuer's statement is in `source` (D-std-0014)
  audience: both
  subjects: inherited
- id: qaa/economics-2023/3.3
  locator: { number: "3.3", headingPath: ["Content, structure and delivery", "Content"] }
  span: { start: 37956, end: 38626 }
  source: "Appropriate data, programming, visualisation and other computing skills required in the modern economics profession will be introduced within the degree course, with particular attention to the study of causality. These include appropriate mathematical and statistical methods, including econometrics. Students will have exposure to the use of such techniques on actual economic, financial or social data, using suitable statistical or econometric software. In addition, students will learn about the nature, sources and uses of both quantitative and qualitative data and an ability to select and apply appropriate methods that economists might use to analyse such data."
  stem: none
  statementType: outcome
  rung: none
  force: will
  level: fheq:6
  appliesTo: "students of the subject and their course"
  addressee: both
  verbs: ["introduced", "learn", "select", "apply"]
  about: "data, programming and econometric skills on real data"
  themes: [none]
  domain: subject-skill
  award: ["bachelor's with honours"]
  gradeOf: none
  paraphrase: "The degree will introduce the data, programming, visualisation and computing skills the profession needs, with stress on causality and on mathematical, statistical and econometric methods; students will use them on real data with suitable software and will learn about the kinds, sources and uses of data and how to choose methods for it."
  quote: full   # the issuer's statement is in `source` (D-std-0014)
  audience: both
  subjects: inherited
- id: qaa/economics-2023/3.4
  locator: { number: "3.4", headingPath: ["Content, structure and delivery", "Content"] }
  span: { start: 38627, end: 39136 }
  source: "3.4 An essential learning outcome of the Economics degree is the judgement and skill required to select and apply the relevant economic tools, principles and reasoning to a variety of applied topics or fields, including an awareness of how economics can be applied to design, guide and interpret economic, social and environmental policy. As part of this, students should also learn how to discuss and analyse government policy and to evaluate the performance of the UK and other economies, past and present.\n"
  stem: none
  statementType: outcome
  rung: none
  force: should
  level: fheq:6
  appliesTo: "students of the subject"
  addressee: learner
  verbs: ["select", "apply", "learn", "discuss", "analyse", "evaluate"]
  about: "choosing and applying economic tools to applied topics and policy"
  themes: [none]
  domain: subject-skill
  award: ["bachelor's with honours"]
  gradeOf: none
  paraphrase: "An essential outcome is the judgement and skill to choose and use economic tools, principles and reasoning across applied topics, including how economics can shape and interpret economic, social and environmental policy; students should also learn to talk about and analyse government policy and judge how the UK and other economies have performed."
  quote: full   # the issuer's statement is in `source` (D-std-0014)
  audience: both
  subjects: inherited
- id: qaa/economics-2023/3.10
  locator: { number: "3.10", headingPath: ["Content, structure and delivery", "Teaching and learning"] }
  span: { start: 42027, end: 42352 }
  source: "As the student body in many undergraduate Economics courses can be international and otherwise diverse, course leaders need to think about specific help for students to deal with language issues, mathematics support (as use of mathematics might be quite different from the focus in school), and study and exam skills support."
  stem: none
  statementType: expectation
  rung: none
  force: must   # D-std-0016: "need to" read as must
  level: none
  appliesTo: "course leaders"
  addressee: provider
  verbs: ["think", "deal"]
  about: "support for language, mathematics and study skills"
  themes: [none]
  domain: none
  award: ["none"]
  gradeOf: none
  paraphrase: "Because many cohorts are international and diverse, course leaders need to consider specific help with language, mathematics and study and exam skills, since university economics differs from study at school."
  quote: full   # the issuer's statement is in `source` (D-std-0014)
  audience: practitioner
  subjects: inherited
- id: qaa/economics-2023/4.2
  locator: { number: "4.2", headingPath: ["Benchmark standards", "Introduction"] }
  span: { start: 45463, end: 45794 }
  source: "The vast majority of students will perform significantly better than the minimum threshold standards. Each higher education provider has its own method of determining what appropriate evidence of this achievement will be and should refer to Annex D: Outcome classification descriptions for FHEQ Level 6 and FQHEIS Level 10 degrees."
  stem: none
  statementType: expectation
  rung: none
  force: should
  level: fheq:6
  appliesTo: "higher education providers"
  addressee: provider
  verbs: ["perform", "determining", "refer"]
  about: "achievement above threshold and the use of Annex D"
  themes: [none]
  domain: none
  award: ["bachelor's with honours"]
  gradeOf: none
  paraphrase: "Most students will do much better than the minimum threshold; each provider decides what evidence shows this and should refer to Annex D, which describes the four honours classes."
  quote: full   # the issuer's statement is in `source` (D-std-0014)
  audience: practitioner
  subjects: inherited
- id: qaa/economics-2023/4.3.b1
  locator: { number: "4.3.b1", headingPath: ["Benchmark standards", "Threshold level"] }
  span: { start: 46052, end: 46112 }
  source: "understanding of key economic concepts, principles and tools"
  stem: "4.3"
  statementType: threshold
  rung: threshold
  force: threshold
  level: fheq:6
  appliesTo: "graduates at the threshold level"
  addressee: learner
  verbs: []
  about: "key concepts, principles and tools"
  themes: [none]
  domain: understanding
  award: ["bachelor's with honours"]
  gradeOf: none
  paraphrase: "At threshold, a graduate should have shown that they understand the main ideas, principles and tools that economists work with."
  quote: full   # the issuer's statement is in `source` (D-std-0014)
  audience: both
  subjects: inherited
- id: qaa/economics-2023/4.3.b2
  locator: { number: "4.3.b2", headingPath: ["Benchmark standards", "Threshold level"] }
  span: { start: 46115, end: 46195 }
  source: "understanding of key economic theories, interpretations and modelling approaches"
  stem: "4.3"
  statementType: threshold
  rung: threshold
  force: threshold
  level: fheq:6
  appliesTo: "graduates at the threshold level"
  addressee: learner
  verbs: []
  about: "key theories, interpretations and models"
  themes: [none]
  domain: understanding
  award: ["bachelor's with honours"]
  gradeOf: none
  paraphrase: "At threshold, a graduate should have shown that they understand the main economic theories, the ways they are read and the approaches used to model them."
  quote: full   # the issuer's statement is in `source` (D-std-0014)
  audience: both
  subjects: inherited
- id: qaa/economics-2023/4.3.b3
  locator: { number: "4.3.b3", headingPath: ["Benchmark standards", "Threshold level"] }
  span: { start: 46198, end: 46401 }
  source: "understanding of quantitative and qualitative methods and computing techniques appropriate to their course of study, and an appreciation of the contexts in which these techniques and methods are relevant"
  stem: "4.3"
  statementType: threshold
  rung: threshold
  force: threshold
  level: fheq:6
  appliesTo: "graduates at the threshold level"
  addressee: learner
  verbs: []
  about: "quantitative and qualitative methods and computing"
  themes: [none]
  domain: subject-skill
  award: ["bachelor's with honours"]
  gradeOf: none
  paraphrase: "At threshold, a graduate should have shown that they understand the numerical and non-numerical methods and computing techniques suited to their course, and see where these apply."
  quote: full   # the issuer's statement is in `source` (D-std-0014)
  audience: both
  subjects: inherited
- id: qaa/economics-2023/4.3.b4
  locator: { number: "4.3.b4", headingPath: ["Benchmark standards", "Threshold level"] }
  span: { start: 46404, end: 46566 }
  source: "knowledge of the sources and content of economic data and evidence and an appreciation of what methods might be appropriately applied to the analysis of such data"
  stem: "4.3"
  statementType: threshold
  rung: threshold
  force: threshold
  level: fheq:6
  appliesTo: "graduates at the threshold level"
  addressee: learner
  verbs: ["applied"]
  about: "sources and content of economic data and evidence"
  themes: [none]
  domain: knowledge
  award: ["bachelor's with honours"]
  gradeOf: none
  paraphrase: "At threshold, a graduate should have shown that they know where economic data and evidence come from and what they contain, and see which methods could suit analysing them."
  quote: full   # the issuer's statement is in `source` (D-std-0014)
  audience: both
  subjects: inherited
- id: qaa/economics-2023/4.3.b5
  locator: { number: "4.3.b5", headingPath: ["Benchmark standards", "Threshold level"] }
  span: { start: 46569, end: 46624 }
  source: "an ability to apply economic reasoning to policy issues"
  stem: "4.3"
  statementType: threshold
  rung: threshold
  force: threshold
  level: fheq:6
  appliesTo: "graduates at the threshold level"
  addressee: learner
  verbs: ["apply"]
  about: "economic reasoning applied to policy"
  themes: [none]
  domain: subject-skill
  award: ["bachelor's with honours"]
  gradeOf: none
  paraphrase: "At threshold, a graduate should have shown that they can bring economic reasoning to bear on questions of policy."
  quote: full   # the issuer's statement is in `source` (D-std-0014)
  audience: both
  subjects: inherited
- id: qaa/economics-2023/4.3.b6
  locator: { number: "4.3.b6", headingPath: ["Benchmark standards", "Threshold level"] }
  span: { start: 46627, end: 46797 }
  source: "knowledge and awareness of historical, political, institutional, international, social, cultural and environmental contexts in which specific economic analysis is applied"
  stem: "4.3"
  statementType: threshold
  rung: threshold
  force: threshold
  level: fheq:6
  appliesTo: "graduates at the threshold level"
  addressee: learner
  verbs: ["applied"]
  about: "the contexts in which economic analysis is used"
  themes: [none]
  domain: knowledge
  award: ["bachelor's with honours"]
  gradeOf: none
  paraphrase: "At threshold, a graduate should have shown that they know and are aware of the wider settings (historical, political, institutional, international, social, cultural, environmental) in which particular economic analyses are used."
  quote: full   # the issuer's statement is in `source` (D-std-0014)
  audience: both
  subjects: inherited
- id: qaa/economics-2023/4.3.b7
  locator: { number: "4.3.b7", headingPath: ["Benchmark standards", "Threshold level"] }
  span: { start: 46800, end: 46920 }
  source: "knowledge in an appropriate number of specialised areas in Economics, some of which is informed by research in Economics"
  stem: "4.3"
  statementType: threshold
  rung: threshold
  force: threshold
  level: fheq:6
  appliesTo: "graduates at the threshold level"
  addressee: learner
  verbs: ["informed"]
  about: "knowledge of specialised areas, partly drawn from research"
  themes: [none]
  domain: knowledge
  award: ["bachelor's with honours"]
  gradeOf: none
  paraphrase: "At threshold, a graduate should have shown knowledge of a suitable number of specialist areas of economics, partly grounded in research."
  quote: full   # the issuer's statement is in `source` (D-std-0014)
  audience: both
  subjects: inherited
- id: qaa/economics-2023/4.3.b8
  locator: { number: "4.3.b8", headingPath: ["Benchmark standards", "Threshold level"] }
  span: { start: 46923, end: 47016 }
  source: "awareness of the possibility that many economic problems may admit of more than one approach."
  stem: "4.3"
  statementType: threshold
  rung: threshold
  force: threshold
  level: fheq:6
  appliesTo: "graduates at the threshold level"
  addressee: learner
  verbs: ["admit"]
  about: "awareness that problems allow more than one approach"
  themes: [none]
  domain: understanding
  award: ["bachelor's with honours"]
  gradeOf: none
  paraphrase: "At threshold, a graduate should have shown awareness that many economic problems can be tackled in more than one way."
  quote: full   # the issuer's statement is in `source` (D-std-0014)
  audience: both
  subjects: inherited
- id: qaa/economics-2023/4.4.b1
  locator: { number: "4.4.b1", headingPath: ["Benchmark standards", "Typical level"] }
  span: { start: 47122, end: 47189 }
  source: "systematic understanding of economic concepts, principles and tools"
  stem: "4.4"
  statementType: typical
  rung: typical
  force: should
  level: fheq:6
  appliesTo: "graduates at the typical level"
  addressee: learner
  verbs: []
  about: "systematic grasp of concepts, principles and tools"
  themes: [none]
  domain: understanding
  award: ["bachelor's with honours"]
  gradeOf: { statement: qaa/economics-2023/4.3.b1, basis: inferred }
  paraphrase: "At the typical level, a graduate should have shown a systematic, well-organised understanding of economic concepts, principles and tools."
  quote: full   # the issuer's statement is in `source` (D-std-0014)
  audience: both
  subjects: inherited
- id: qaa/economics-2023/4.4.b2
  locator: { number: "4.4.b2", headingPath: ["Benchmark standards", "Typical level"] }
  span: { start: 47192, end: 47316 }
  source: "systematic understanding of distinctive economic theories, interpretations and modelling approaches, and their competent use"
  stem: "4.4"
  statementType: typical
  rung: typical
  force: should
  level: fheq:6
  appliesTo: "graduates at the typical level"
  addressee: learner
  verbs: []
  about: "systematic grasp of distinctive theories and models, used competently"
  themes: [none]
  domain: understanding
  award: ["bachelor's with honours"]
  gradeOf: { statement: qaa/economics-2023/4.3.b2, basis: inferred }
  paraphrase: "At the typical level, a graduate should have shown a systematic understanding of distinctive economic theories, their readings and modelling approaches, and use them competently."
  quote: full   # the issuer's statement is in `source` (D-std-0014)
  audience: both
  subjects: inherited
- id: qaa/economics-2023/4.4.b3
  locator: { number: "4.4.b3", headingPath: ["Benchmark standards", "Typical level"] }
  span: { start: 47319, end: 47475 }
  source: "proficiency in quantitative methods and computing techniques and knowledge of how to use these techniques and methods effectively across a range of problems"
  stem: "4.4"
  statementType: typical
  rung: typical
  force: should
  level: fheq:6
  appliesTo: "graduates at the typical level"
  addressee: learner
  verbs: ["use"]
  about: "proficiency in methods and computing across problems"
  themes: [none]
  domain: subject-skill
  award: ["bachelor's with honours"]
  gradeOf: { statement: qaa/economics-2023/4.3.b3, basis: inferred }
  paraphrase: "At the typical level, a graduate should have shown proficiency in quantitative methods and computing and know how to use them well across a range of problems."
  quote: full   # the issuer's statement is in `source` (D-std-0014)
  audience: both
  subjects: inherited
- id: qaa/economics-2023/4.4.b4
  locator: { number: "4.4.b4", headingPath: ["Benchmark standards", "Typical level"] }
  span: { start: 47482, end: 47649 }
  source: "systematic understanding of the sources and content of economic data and evidence and of those methods that might be applied appropriately to the analysis of such data"
  stem: "4.4"
  statementType: typical
  rung: typical
  force: should
  level: fheq:6
  appliesTo: "graduates at the typical level"
  addressee: learner
  verbs: ["applied"]
  about: "systematic grasp of data, evidence and methods for them"
  themes: [none]
  domain: knowledge
  award: ["bachelor's with honours"]
  gradeOf: { statement: qaa/economics-2023/4.3.b4, basis: inferred }
  paraphrase: "At the typical level, a graduate should have shown a systematic grasp of where economic data and evidence come from, what they contain and which methods suit their analysis."
  quote: full   # the issuer's statement is in `source` (D-std-0014)
  audience: both
  subjects: inherited
- id: qaa/economics-2023/4.4.b5
  locator: { number: "4.4.b5", headingPath: ["Benchmark standards", "Typical level"] }
  span: { start: 47652, end: 47734 }
  source: "knowledge of how to apply economic reasoning to policy issues in a critical manner"
  stem: "4.4"
  statementType: typical
  rung: typical
  force: should
  level: fheq:6
  appliesTo: "graduates at the typical level"
  addressee: learner
  verbs: ["apply"]
  about: "applying economic reasoning to policy critically"
  themes: [none]
  domain: subject-skill
  award: ["bachelor's with honours"]
  gradeOf: { statement: qaa/economics-2023/4.3.b5, basis: inferred }
  paraphrase: "At the typical level, a graduate should have shown that they know how to bring economic reasoning to policy questions critically."
  quote: full   # the issuer's statement is in `source` (D-std-0014)
  audience: both
  subjects: inherited
- id: qaa/economics-2023/4.4.b6
  locator: { number: "4.4.b6", headingPath: ["Benchmark standards", "Typical level"] }
  span: { start: 47737, end: 47912 }
  source: "systematic understanding of the historical, political, institutional, international, social, cultural and environmental contexts in which specific economic analysis is applied"
  stem: "4.4"
  statementType: typical
  rung: typical
  force: should
  level: fheq:6
  appliesTo: "graduates at the typical level"
  addressee: learner
  verbs: ["applied"]
  about: "systematic grasp of the contexts of economic analysis"
  themes: [none]
  domain: knowledge
  award: ["bachelor's with honours"]
  gradeOf: { statement: qaa/economics-2023/4.3.b6, basis: inferred }
  paraphrase: "At the typical level, a graduate should have shown a systematic grasp of the wider settings (historical, political, institutional, international, social, cultural, environmental) in which particular economic analyses are used."
  quote: full   # the issuer's statement is in `source` (D-std-0014)
  audience: both
  subjects: inherited
- id: qaa/economics-2023/4.4.b7
  locator: { number: "4.4.b7", headingPath: ["Benchmark standards", "Typical level"] }
  span: { start: 47915, end: 48045 }
  source: "knowledge in an appropriate number of specialised areas in Economics and an appreciation of the research literature in these areas"
  stem: "4.4"
  statementType: typical
  rung: typical
  force: should
  level: fheq:6
  appliesTo: "graduates at the typical level"
  addressee: learner
  verbs: []
  about: "specialised areas and their research literature"
  themes: [none]
  domain: knowledge
  award: ["bachelor's with honours"]
  gradeOf: { statement: qaa/economics-2023/4.3.b7, basis: inferred }
  paraphrase: "At the typical level, a graduate should have shown knowledge of a suitable number of specialist areas of economics and an appreciation of their research literature."
  quote: full   # the issuer's statement is in `source` (D-std-0014)
  audience: both
  subjects: inherited
- id: qaa/economics-2023/4.4.b8
  locator: { number: "4.4.b8", headingPath: ["Benchmark standards", "Typical level"] }
  span: { start: 48048, end: 48242 }
  source: "familiarity with some of the different approaches to addressing economic problems and evidence of a critical awareness of the applicability and limits of these approaches in particular contexts."
  stem: "4.4"
  statementType: typical
  rung: typical
  force: should
  level: fheq:6
  appliesTo: "graduates at the typical level"
  addressee: learner
  verbs: ["addressing"]
  about: "different approaches and a critical sense of their limits"
  themes: [none]
  domain: understanding
  award: ["bachelor's with honours"]
  gradeOf: { statement: qaa/economics-2023/4.3.b8, basis: inferred }
  paraphrase: "At the typical level, a graduate should have shown familiarity with some of the different ways of tackling economic problems and a critical awareness of where each works and where it falls short."
  quote: full   # the issuer's statement is in `source` (D-std-0014)
  audience: both
  subjects: inherited
- id: qaa/economics-2023/4.5.b1
  locator: { number: "4.5.b1", headingPath: ["Benchmark standards", "Excellent level"] }
  span: { start: 48365, end: 48431 }
  source: "excellent understanding of economic concepts, principles and tools"
  stem: "4.5"
  statementType: excellent
  rung: excellent
  force: should
  level: fheq:6
  appliesTo: "graduates at the excellent level"
  addressee: learner
  verbs: []
  about: "excellent understanding of concepts, principles and tools"
  themes: [none]
  domain: understanding
  award: ["bachelor's with honours"]
  gradeOf: { statement: qaa/economics-2023/4.4.b1, basis: inferred }
  paraphrase: "At the excellent level, a graduate should consistently have shown an outstanding understanding of economic concepts, principles and tools."
  quote: full   # the issuer's statement is in `source` (D-std-0014)
  audience: both
  subjects: inherited
- id: qaa/economics-2023/4.5.b2
  locator: { number: "4.5.b2", headingPath: ["Benchmark standards", "Excellent level"] }
  span: { start: 48434, end: 48579 }
  source: "excellent understanding of distinctive economic theories, interpretations and modelling approaches, and their competent use in a research context"
  stem: "4.5"
  statementType: excellent
  rung: excellent
  force: should
  level: fheq:6
  appliesTo: "graduates at the excellent level"
  addressee: learner
  verbs: []
  about: "excellent grasp of theories and models, used competently in research"
  themes: [none]
  domain: understanding
  award: ["bachelor's with honours"]
  gradeOf: { statement: qaa/economics-2023/4.4.b2, basis: inferred }
  paraphrase: "At the excellent level, a graduate should consistently have shown an outstanding understanding of distinctive economic theories, their readings and models, used competently in a research setting."
  quote: full   # the issuer's statement is in `source` (D-std-0014)
  audience: both
  subjects: inherited
- id: qaa/economics-2023/4.5.b3
  locator: { number: "4.5.b3", headingPath: ["Benchmark standards", "Excellent level"] }
  span: { start: 48582, end: 48737 }
  source: "excellence in quantitative methods and computing techniques and knowledge of how to use these techniques and methods effectively across a range of problems"
  stem: "4.5"
  statementType: excellent
  rung: excellent
  force: should
  level: fheq:6
  appliesTo: "graduates at the excellent level"
  addressee: learner
  verbs: ["use"]
  about: "excellence in methods and computing across problems"
  themes: [none]
  domain: subject-skill
  award: ["bachelor's with honours"]
  gradeOf: { statement: qaa/economics-2023/4.4.b3, basis: inferred }
  paraphrase: "At the excellent level, a graduate should consistently have shown excellence in quantitative methods and computing and know how to use them well across a range of problems."
  quote: full   # the issuer's statement is in `source` (D-std-0014)
  audience: both
  subjects: inherited
- id: qaa/economics-2023/4.5.b4
  locator: { number: "4.5.b4", headingPath: ["Benchmark standards", "Excellent level"] }
  span: { start: 48740, end: 48898 }
  source: "excellent grasp of the sources and content of economic data and evidence and of those methods that might be applied appropriately to the analysis of such data"
  stem: "4.5"
  statementType: excellent
  rung: excellent
  force: should
  level: fheq:6
  appliesTo: "graduates at the excellent level"
  addressee: learner
  verbs: ["applied"]
  about: "excellent grasp of data, evidence and methods for them"
  themes: [none]
  domain: knowledge
  award: ["bachelor's with honours"]
  gradeOf: { statement: qaa/economics-2023/4.4.b4, basis: inferred }
  paraphrase: "At the excellent level, a graduate should consistently have shown an excellent command of where economic data and evidence come from, what they contain and which methods suit their analysis."
  quote: full   # the issuer's statement is in `source` (D-std-0014)
  audience: both
  subjects: inherited
- id: qaa/economics-2023/4.5.b5
  locator: { number: "4.5.b5", headingPath: ["Benchmark standards", "Excellent level"] }
  span: { start: 48901, end: 48992 }
  source: "advanced knowledge of how to apply economic reasoning to policy issues in a critical manner"
  stem: "4.5"
  statementType: excellent
  rung: excellent
  force: should
  level: fheq:6
  appliesTo: "graduates at the excellent level"
  addressee: learner
  verbs: ["apply"]
  about: "advanced, critical application of economic reasoning to policy"
  themes: [none]
  domain: subject-skill
  award: ["bachelor's with honours"]
  gradeOf: { statement: qaa/economics-2023/4.4.b5, basis: inferred }
  paraphrase: "At the excellent level, a graduate should consistently have shown advanced knowledge of how to bring economic reasoning to policy questions critically."
  quote: full   # the issuer's statement is in `source` (D-std-0014)
  audience: both
  subjects: inherited
- id: qaa/economics-2023/4.5.b6
  locator: { number: "4.5.b6", headingPath: ["Benchmark standards", "Excellent level"] }
  span: { start: 48995, end: 49169 }
  source: "excellent understanding of the historical, political, institutional, international, social, cultural and environmental contexts in which specific economic analysis is applied"
  stem: "4.5"
  statementType: excellent
  rung: excellent
  force: should
  level: fheq:6
  appliesTo: "graduates at the excellent level"
  addressee: learner
  verbs: ["applied"]
  about: "excellent grasp of the contexts of economic analysis"
  themes: [none]
  domain: knowledge
  award: ["bachelor's with honours"]
  gradeOf: { statement: qaa/economics-2023/4.4.b6, basis: inferred }
  paraphrase: "At the excellent level, a graduate should consistently have shown an excellent grasp of the wider settings (historical, political, institutional, international, social, cultural, environmental) in which particular economic analyses are used."
  quote: full   # the issuer's statement is in `source` (D-std-0014)
  audience: both
  subjects: inherited
- id: qaa/economics-2023/4.5.b7
  locator: { number: "4.5.b7", headingPath: ["Benchmark standards", "Excellent level"] }
  span: { start: 49172, end: 49303 }
  source: "advanced knowledge in an appropriate number of specialised areas in Economics, and which is embedded in current research literature"
  stem: "4.5"
  statementType: excellent
  rung: excellent
  force: should
  level: fheq:6
  appliesTo: "graduates at the excellent level"
  addressee: learner
  verbs: ["embedded"]
  about: "advanced knowledge of specialised areas, set in current research"
  themes: [none]
  domain: knowledge
  award: ["bachelor's with honours"]
  gradeOf: { statement: qaa/economics-2023/4.4.b7, basis: inferred }
  paraphrase: "At the excellent level, a graduate should consistently have shown advanced knowledge of a suitable number of specialist areas, grounded in current research literature."
  quote: full   # the issuer's statement is in `source` (D-std-0014)
  audience: both
  subjects: inherited
- id: qaa/economics-2023/4.5.b8
  locator: { number: "4.5.b8", headingPath: ["Benchmark standards", "Excellent level"] }
  span: { start: 49306, end: 49575 }
  source: "excellent knowledge of some of the different approaches to addressing economic problems with excellent awareness of the applicability and limits of these approaches, thus demonstrating creativity and sound judgement in the use of various approaches in diverse contexts."
  stem: "4.5"
  statementType: excellent
  rung: excellent
  force: should
  level: fheq:6
  appliesTo: "graduates at the excellent level"
  addressee: learner
  verbs: ["addressing", "demonstrating"]
  about: "excellent judgement across approaches, showing creativity"
  themes: [none]
  domain: understanding
  award: ["bachelor's with honours"]
  gradeOf: { statement: qaa/economics-2023/4.4.b8, basis: inferred }
  paraphrase: "At the excellent level, a graduate should consistently have shown excellent knowledge of different ways of tackling economic problems and an excellent sense of where each works and where it falls short, using them with creativity and sound judgement in varied settings."
  quote: full   # the issuer's statement is in `source` (D-std-0014)
  audience: both
  subjects: inherited
```

### S4a Audience versions
<!-- label: both; status: drafted; basis: primary. forPractitioner: for the programme designer or teacher. forBeneficiary: for the student, second person, naming no issuer. author-agent-written: instructions to an AI agent writing about the statement (a course document, a handbook, an outcome, a report). author-agent-dialogue: instructions to an AI agent using the statement in conversation (with a student, a teacher or a programme team). Written fresh from the held text alone (benchmark rule 6; Abbott, 15:42). -->
```yaml
- statement: qaa/economics-2023/1.3
  forPractitioner: { text: "Design the course so that every student builds an understanding of resource use and of how economic actors behave and interact, at both micro and macro level and in how individuals relate to society.", rewrite: light, force: must, status: drafted }
  forBeneficiary: { text: "You must come to understand how resources are used and how households, firms, governments and other bodies behave and interact, both one by one and across the whole economy.", rewrite: full, force: must, status: drafted }
  author-agent-written: "Treat this as a requirement of studying the subject (the issuer's word is 'requires', read as must): an understanding of resource use and economic behaviour at micro and macro levels, for honours at FHEQ level 6. Cite QAA (2023) Economics Subject Benchmark Statement, para 1.3, and do not present it as a rung item or a regulatory rule. Set it beside the threshold items qaa/economics-2023/4.3.b1 and 4.3.b2 and the honours descriptor qaa/fheq-2024/4.15.b1."
  author-agent-dialogue: "Raise this when a student is unsure why both microeconomics and macroeconomics are taught, or when a team reviews the core modules. Explain to a student that you need to grasp both how single actors decide and how the economy behaves as a whole; for staff, frame it as what the core must secure. Ask \"Can you explain one idea at each level and how the two connect?\" Avoid reciting the paragraph or treating it as a graded rung."
- statement: qaa/economics-2023/1.6.b1
  forPractitioner: { text: "Develop students' ability to collect evidence and then absorb, organise, analyse and weigh both numerical and non-numerical data.", rewrite: light, force: describes, status: drafted }
  forBeneficiary: { text: "As an economist in training, you need to gather evidence and then organise, analyse and judge both numerical and non-numerical data.", rewrite: full, force: describes, status: drafted }
  author-agent-written: "Describe this as one of the core abilities the statement says economists need (gathering evidence and handling data); the issuer's word is 'need', recorded as describes, so give it no must or should. Cite QAA (2023) Economics Subject Benchmark Statement, para 1.6, and do not present it as a threshold requirement: for that, use the rung item qaa/economics-2023/4.3.b4. Set it beside the honours descriptor qaa/fheq-2024/4.15.b7 at spine:6, and note that 1.17 aligns these skills with the ESD guidance's competencies."
  author-agent-dialogue: "Use this when a student or programme team asks what makes the economist's way of working distinctive, here gathering evidence and handling data. Put it plainly to a student: economists collect evidence and make sense of numbers and words alike; for staff, ask where the course builds it. Ask \"What evidence did you gather for your last piece of work, and how did you judge its quality?\" Do not call it a pass requirement or read the whole list aloud."
- statement: qaa/economics-2023/1.6.b2
  forPractitioner: { text: "Teach students to strip a problem to its essentials through abstraction and simplification, and to model that core.", rewrite: light, force: describes, status: drafted }
  forBeneficiary: { text: "You need to be able to simplify a messy problem, find what really matters in it and build a model of that.", rewrite: full, force: describes, status: drafted }
  author-agent-written: "Describe this as one of the core abilities the statement says economists need (abstraction and modelling); the issuer's word is 'need', recorded as describes, so give it no must or should. Cite QAA (2023) Economics Subject Benchmark Statement, para 1.6, and do not present it as a threshold requirement: for that, use the rung item qaa/economics-2023/4.3.b2. Set it beside the honours descriptor qaa/fheq-2024/4.15.b3.1 at spine:6, and note that 1.17 aligns these skills with the ESD guidance's competencies."
  author-agent-dialogue: "Use this when a student or programme team asks what makes the economist's way of working distinctive, here abstraction and modelling. Put it plainly to a student: economists simplify a problem to its core and build a model of it; for staff, ask where the course builds it. Ask \"What did you leave out of your model, and why was that safe?\" Do not call it a pass requirement or read the whole list aloud."
- statement: qaa/economics-2023/1.6.b3
  forPractitioner: { text: "Give students practice in deductive, abductive and inductive reasoning with economic tools and with prior research from economics and other fields.", rewrite: light, force: describes, status: drafted }
  forBeneficiary: { text: "You need to be able to reason in several ways, from theory to case, from cases to general patterns and to the best explanation, using economic tools and existing research.", rewrite: full, force: describes, status: drafted }
  author-agent-written: "Describe this as one of the core abilities the statement says economists need (deductive, abductive and inductive reasoning); the issuer's word is 'need', recorded as describes, so give it no must or should. Cite QAA (2023) Economics Subject Benchmark Statement, para 1.6, and do not present it as a threshold requirement: for that, use the rung item qaa/economics-2023/4.3.b2. Set it beside the honours descriptor qaa/fheq-2024/4.15.b3.1 at spine:6, and note that 1.17 aligns these skills with the ESD guidance's competencies."
  author-agent-dialogue: "Use this when a student or programme team asks what makes the economist's way of working distinctive, here deductive, abductive and inductive reasoning. Put it plainly to a student: economists reason from theory, from evidence and towards the best explanation; for staff, ask where the course builds it. Ask \"Was your argument built from a theory, from the data or from the most likely explanation?\" Do not call it a pass requirement or read the whole list aloud."
- statement: qaa/economics-2023/1.6.b4
  forPractitioner: { text: "Build students' ability to present findings concisely to varied audiences, including people untrained in economics.", rewrite: light, force: describes, status: drafted }
  forBeneficiary: { text: "You need to be able to explain your results briefly to different audiences, including people who have never studied economics.", rewrite: full, force: describes, status: drafted }
  author-agent-written: "Describe this as one of the core abilities the statement says economists need (communicating results to varied audiences); the issuer's word is 'need', recorded as describes, so give it no must or should. Cite QAA (2023) Economics Subject Benchmark Statement, para 1.6, and do not present it as a threshold requirement: for that, use the rung item qaa/economics-2023/2.2.b8. Set it beside the honours descriptor qaa/fheq-2024/4.15.b8 at spine:6, and note that 1.17 aligns these skills with the ESD guidance's competencies."
  author-agent-dialogue: "Use this when a student or programme team asks what makes the economist's way of working distinctive, here communicating results to varied audiences. Put it plainly to a student: economists explain results briefly to experts and non-experts alike; for staff, ask where the course builds it. Ask \"How would you explain your main finding to someone with no economics in one minute?\" Do not call it a pass requirement or read the whole list aloud."
- statement: qaa/economics-2023/1.6.b5
  forPractitioner: { text: "Teach students to question the limits of their own analysis within its wider socioeconomic setting.", rewrite: light, force: describes, status: drafted }
  forBeneficiary: { text: "You need to think critically about what your analysis cannot tell you once it is placed in its wider social and economic setting.", rewrite: full, force: describes, status: drafted }
  author-agent-written: "Describe this as one of the core abilities the statement says economists need (the limits of analysis in its wider context); the issuer's word is 'need', recorded as describes, so give it no must or should. Cite QAA (2023) Economics Subject Benchmark Statement, para 1.6, and do not present it as a threshold requirement: for that, use the rung item qaa/economics-2023/4.3.b8. Set it beside the honours descriptor qaa/fheq-2024/4.15.b4 at spine:6, and note that 1.17 aligns these skills with the ESD guidance's competencies."
  author-agent-dialogue: "Use this when a student or programme team asks what makes the economist's way of working distinctive, here the limits of analysis in its wider context. Put it plainly to a student: economists question what their own analysis leaves out; for staff, ask where the course builds it. Ask \"What can your analysis not tell us, and why?\" Do not call it a pass requirement or read the whole list aloud."
- statement: qaa/economics-2023/1.6.b6
  forPractitioner: { text: "Develop students' ability to infer policy implications, identify constraints on implementation and evaluate outcomes against stated objectives.", rewrite: light, force: describes, status: drafted }
  forBeneficiary: { text: "You need to be able to work out what your analysis means for policy, see what might get in the way of a policy and judge whether it met its aims.", rewrite: full, force: describes, status: drafted }
  author-agent-written: "Describe this as one of the core abilities the statement says economists need (policy inference, constraints and evaluation); the issuer's word is 'need', recorded as describes, so give it no must or should. Cite QAA (2023) Economics Subject Benchmark Statement, para 1.6, and do not present it as a threshold requirement: for that, use the rung item qaa/economics-2023/4.3.b5. Set it beside the honours descriptor qaa/fheq-2024/4.15.b7 at spine:6, and note that 1.17 aligns these skills with the ESD guidance's competencies."
  author-agent-dialogue: "Use this when a student or programme team asks what makes the economist's way of working distinctive, here policy inference, constraints and evaluation. Put it plainly to a student: economists turn analysis into policy advice and judge policies against their aims; for staff, ask where the course builds it. Ask \"What would stop this policy working as planned, and how would you know whether it succeeded?\" Do not call it a pass requirement or read the whole list aloud."
- statement: qaa/economics-2023/1.7
  forPractitioner: { text: "Aim to build an inclusive learning community and plan how equality, diversity and inclusion shape your readings, slides, videos, methods and processes; the statement's examples include widening participation, countering under-representation, zero tolerance of harassment, anticipating neurodiverse access and closing awarding gaps.", rewrite: light, force: should, status: drafted }
  forBeneficiary: { text: "not-applicable: a duty on teaching staff and the course; the student meets its effect, not a standard to reach", rewrite: full, force: should, status: drafted }
  author-agent-written: "Present this as an expectation on teaching staff (should), not on students, about inclusive learning communities and embedding EDI in materials and methods. Cite QAA (2023) Economics Subject Benchmark Statement, para 1.7, and do not claim the listed efforts in 1.7's bullets are required: the issuer offers them as examples. Set it beside the accessibility expectations qaa/economics-2023/1.10 and 1.13 and the EDI discussion in 1.8 and 1.9."
  author-agent-dialogue: "Raise this with a programme team reviewing materials, reading lists or assessment for inclusion. Frame it for staff as an aim to work towards and ask \"Whose experiences do your readings and examples show?\" and \"Which of the example actions, such as closing awarding gaps, does your course take?\" Do not give it to a student as something they must do."
- statement: qaa/economics-2023/1.10
  forPractitioner: { text: "Expect your teaching approach to respond to the students you actually have, and make an inclusive curriculum with accessible, equitable, fitting and well-resourced materials a priority.", rewrite: light, force: will, status: drafted }
  forBeneficiary: { text: "not-applicable: an expectation on teaching and the curriculum; the student meets its effect", rewrite: full, force: will, status: drafted }
  author-agent-written: "Present this as an expectation on teaching (will, generally), not a student outcome: methods respond to student needs and an inclusive, accessible curriculum is key. Cite QAA (2023) Economics Subject Benchmark Statement, para 1.10, and do not turn it into a promise of particular adjustments. Set it beside qaa/economics-2023/1.13 on digital accessibility and qaa/economics-2023/1.7 on inclusion."
  author-agent-dialogue: "Raise this when a team plans materials or delivery, or reviews accessibility after student feedback. For staff, ask \"How do your methods change for the students in this cohort?\" and \"Which materials are not yet accessible?\" Do not present it to a student as their responsibility."
- statement: qaa/economics-2023/1.13
  forPractitioner: { text: "Make graphs and other visuals accessible, for example with image descriptions; check that digital content works with screen readers, has captions or transcripts for audio and video, can be downloaded in different formats, and that data, specialist software and coding tasks have accessible alternatives.", rewrite: light, force: should, status: drafted }
  forBeneficiary: { text: "not-applicable: a duty on the course and its staff; the student meets its effect", rewrite: full, force: should, status: drafted }
  author-agent-written: "Present this as an expectation on the course and its staff (should) for the digital accessibility of graphs, media and specialist software. Cite QAA (2023) Economics Subject Benchmark Statement, para 1.13, and do not claim it sets a legal standard or a student outcome. Set it beside qaa/economics-2023/1.10 and the examples of practice in 1.14."
  author-agent-dialogue: "Raise this when staff prepare slides, graphs, recordings or coding tasks. Ask \"Can a screen-reader user follow your diagrams?\" and \"Is there an alternative to the specialist software?\" Do not put this duty to a student; a student who meets a barrier can be pointed to the course team."
- statement: qaa/economics-2023/1.16
  forPractitioner: { text: "Build the course so graduates develop the capacity to cope with and seek solutions to the planetary crisis; these problems must push students past applying familiar tools and models towards critical and creative thinking.", rewrite: light, force: must, status: drafted }
  forBeneficiary: { text: "You must develop critical and creative abilities that go beyond applying the usual tools and models, so that you can cope with the planetary crisis, such as a changing climate and lost biodiversity, and help find solutions.", rewrite: full, force: must, status: drafted }
  author-agent-written: "Present this as a requirement the issuer states ('require', read as must) for honours graduates at FHEQ level 6: critical and creative capacities to address the planetary crisis, beyond applying set tools. Cite QAA (2023) Economics Subject Benchmark Statement, para 1.16, and do not claim it is a regulatory rule or a rung item. Set it beside the excellent rung item qaa/economics-2023/4.5.b8, the ESD guidance (std:doc:qaa-advancehe-esd-2021-guidance) and the honours descriptor qaa/fheq-2024/4.15.b7."
  author-agent-dialogue: "Raise this when a student or team asks how sustainability fits an economics degree. Tell a student plainly that you need to think critically and creatively about climate and nature problems, not only apply standard models; with staff, ask where the course stretches students past textbook tools. Ask \"Where have you had to go beyond a standard model to tackle an environmental problem?\" Avoid reading the paragraph aloud or turning it into a topic list."
- statement: qaa/economics-2023/2.2
  forPractitioner: { text: "If you admit students without A level mathematics, provide suitable teaching and support within the degree so they can take on its quantitative content.", rewrite: light, force: must, status: drafted }
  forBeneficiary: { text: "not-applicable: an expectation on the course; the student meets its effect", rewrite: full, force: must, status: drafted }
  author-agent-written: "Present this as an expectation on the course, worded 'the expectation is that' and recorded as describes because the phrase is outside the five obliging words: where entry asks for no A level mathematics, suitable teaching and support are provided for quantitative work. Cite QAA (2023) Economics Subject Benchmark Statement, para 2.2, and do not claim it creates or forbids a mathematics entry condition. Set it beside the support note qaa/economics-2023/3.10 and the methods rung item qaa/economics-2023/4.3.b3."
  author-agent-dialogue: "Raise this when a team reviews admissions or first-year support, or when a student without A level mathematics worries about the quantitative modules. For staff, ask \"What support do students without A level maths get, and when?\"; for a student, explain plainly that the course is expected to help you build the maths you need. Do not present it to a student as a duty of theirs."
- statement: qaa/economics-2023/2.2.b1
  forPractitioner: { text: "Typical course outcome: students critically understand causality and the analytical methods of the subject, both theoretical and empirical.", rewrite: light, force: must, status: drafted }
  forBeneficiary: { text: "Your course is usually designed to help you understand, critically, how to establish cause and effect and how economic methods work in theory and with data.", rewrite: full, force: must, status: drafted }
  author-agent-written: "Describe this as a learning outcome that the usual Economics course is built to reach (causality and analytical methods); the issuer states no modal, so record it as describing usual course design, not a requirement. Cite QAA (2023) Economics Subject Benchmark Statement, para 2.2, and do not claim every course must adopt it or that it is a rung item. Set it beside qaa/economics-2023/4.3.b3 and the honours descriptor qaa/fheq-2024/4.15.b2."
  author-agent-dialogue: "Raise this when a student asks what the course is meant to give them, or when a team writes programme outcomes, here causality and analytical methods. Tell a student plainly: the course aims to help you see how economists establish cause and effect; for staff, compare it with your own programme outcomes. Ask \"How would you show that one thing caused another, rather than just moving with it?\" Avoid presenting it as a minimum standard or quoting the list at length."
- statement: qaa/economics-2023/2.2.b2
  forPractitioner: { text: "Typical course outcome: students understand the history and development of economic thought and the varied methods economists have used and still use.", rewrite: light, force: must, status: drafted }
  forBeneficiary: { text: "Your course is usually designed to help you understand how economic ideas grew over time and the different methods economists have used.", rewrite: full, force: must, status: drafted }
  author-agent-written: "Describe this as a learning outcome that the usual Economics course is built to reach (the history of economic ideas and methods); the issuer states no modal, so record it as describing usual course design, not a requirement. Cite QAA (2023) Economics Subject Benchmark Statement, para 2.2, and do not claim every course must adopt it or that it is a rung item. Set it beside qaa/economics-2023/4.3.b6 and the honours descriptor qaa/fheq-2024/4.15.b1."
  author-agent-dialogue: "Raise this when a student asks what the course is meant to give them, or when a team writes programme outcomes, here the history of economic ideas and methods. Tell a student plainly: the course aims to show you where economic ideas came from and how methods changed; for staff, compare it with your own programme outcomes. Ask \"Which earlier idea still shapes the theory you are using now?\" Avoid presenting it as a minimum standard or quoting the list at length."
- statement: qaa/economics-2023/2.2.b3
  forPractitioner: { text: "Typical course outcome: students understand the historical background of current economic problems and know economic history as relevant to the course.", rewrite: light, force: must, status: drafted }
  forBeneficiary: { text: "Your course is usually designed to help you understand the history behind today's economic problems and to know the economic history that matters for them.", rewrite: full, force: must, status: drafted }
  author-agent-written: "Describe this as a learning outcome that the usual Economics course is built to reach (historical context and economic history); the issuer states no modal, so record it as describing usual course design, not a requirement. Cite QAA (2023) Economics Subject Benchmark Statement, para 2.2, and do not claim every course must adopt it or that it is a rung item. Set it beside qaa/economics-2023/4.3.b6 and the honours descriptor qaa/fheq-2024/4.15.b1."
  author-agent-dialogue: "Raise this when a student asks what the course is meant to give them, or when a team writes programme outcomes, here historical context and economic history. Tell a student plainly: the course aims to give you the history behind current economic problems; for staff, compare it with your own programme outcomes. Ask \"What earlier episode helps explain the problem you are studying?\" Avoid presenting it as a minimum standard or quoting the list at length."
- statement: qaa/economics-2023/2.2.b4
  forPractitioner: { text: "Typical course outcome: students apply economic reasoning and tools to applied topics.", rewrite: light, force: must, status: drafted }
  forBeneficiary: { text: "Your course is usually designed to help you use economic reasoning and tools on real, applied topics.", rewrite: full, force: must, status: drafted }
  author-agent-written: "Describe this as a learning outcome that the usual Economics course is built to reach (applying economic reasoning and tools); the issuer states no modal, so record it as describing usual course design, not a requirement. Cite QAA (2023) Economics Subject Benchmark Statement, para 2.2, and do not claim every course must adopt it or that it is a rung item. Set it beside qaa/economics-2023/4.3.b5 and qaa/economics-2023/3.4 and the honours descriptor qaa/fheq-2024/4.15.b6."
  author-agent-dialogue: "Raise this when a student asks what the course is meant to give them, or when a team writes programme outcomes, here applying economic reasoning and tools. Tell a student plainly: the course aims to have you use economics on real topics; for staff, compare it with your own programme outcomes. Ask \"Which applied topic have you tackled with an economic tool, and what did it show?\" Avoid presenting it as a minimum standard or quoting the list at length."
- statement: qaa/economics-2023/2.2.b5
  forPractitioner: { text: "Typical course outcome: students critically evaluate differing policy recommendations against their underlying methodologies.", rewrite: light, force: must, status: drafted }
  forBeneficiary: { text: "Your course is usually designed to help you judge why experts recommend different policies, by looking at the methods behind each view.", rewrite: full, force: must, status: drafted }
  author-agent-written: "Describe this as a learning outcome that the usual Economics course is built to reach (evaluating policy advice against its methods); the issuer states no modal, so record it as describing usual course design, not a requirement. Cite QAA (2023) Economics Subject Benchmark Statement, para 2.2, and do not claim every course must adopt it or that it is a rung item. Set it beside qaa/economics-2023/4.4.b5 and the honours descriptor qaa/fheq-2024/4.15.b7."
  author-agent-dialogue: "Raise this when a student asks what the course is meant to give them, or when a team writes programme outcomes, here evaluating policy advice against its methods. Tell a student plainly: the course aims to help you see why economists disagree about policy; for staff, compare it with your own programme outcomes. Ask \"Why do two economists reach different advice on this policy, and whose method do you trust more?\" Avoid presenting it as a minimum standard or quoting the list at length."
- statement: qaa/economics-2023/2.2.b6
  forPractitioner: { text: "Typical course outcome: students discuss, analyse and evaluate government policy and assess the performance of the UK, other national economies and the global economy.", rewrite: light, force: must, status: drafted }
  forBeneficiary: { text: "Your course is usually designed to help you debate and judge government policy and assess how the UK and other economies, and the world economy, are doing.", rewrite: full, force: must, status: drafted }
  author-agent-written: "Describe this as a learning outcome that the usual Economics course is built to reach (government policy and economic performance); the issuer states no modal, so record it as describing usual course design, not a requirement. Cite QAA (2023) Economics Subject Benchmark Statement, para 2.2, and do not claim every course must adopt it or that it is a rung item. Set it beside qaa/economics-2023/3.4 and qaa/economics-2023/4.3.b5 and the honours descriptor qaa/fheq-2024/4.15.b7."
  author-agent-dialogue: "Raise this when a student asks what the course is meant to give them, or when a team writes programme outcomes, here government policy and economic performance. Tell a student plainly: the course aims to have you judge policy and how economies perform; for staff, compare it with your own programme outcomes. Ask \"How would you judge whether the economy is doing well, and by which measures?\" Avoid presenting it as a minimum standard or quoting the list at length."
- statement: qaa/economics-2023/2.2.b7
  forPractitioner: { text: "Typical course outcome: students understand verbal, graphical, mathematical and econometric forms of economic ideas and how they link, and can use suitable techniques to handle and interpret quantitative and qualitative data.", rewrite: light, force: must, status: drafted }
  forBeneficiary: { text: "Your course is usually designed to help you express economic ideas in words, graphs, maths and statistics, see how these connect and work with data.", rewrite: full, force: must, status: drafted }
  author-agent-written: "Describe this as a learning outcome that the usual Economics course is built to reach (representing economic ideas and handling data); the issuer states no modal, so record it as describing usual course design, not a requirement. Cite QAA (2023) Economics Subject Benchmark Statement, para 2.2, and do not claim every course must adopt it or that it is a rung item. Set it beside qaa/economics-2023/4.3.b3 and the honours descriptor qaa/fheq-2024/4.15.b2."
  author-agent-dialogue: "Raise this when a student asks what the course is meant to give them, or when a team writes programme outcomes, here representing economic ideas and handling data. Tell a student plainly: the course aims to help you move between words, graphs, maths and data; for staff, compare it with your own programme outcomes. Ask \"Can you state the same idea in a sentence, a graph and an equation?\" Avoid presenting it as a minimum standard or quoting the list at length."
- statement: qaa/economics-2023/2.2.b8
  forPractitioner: { text: "Typical course outcome: students articulate, communicate and present arguments verbally or non-verbally to specialist and non-specialist audiences, including experts from other fields.", rewrite: light, force: must, status: drafted }
  forBeneficiary: { text: "Your course is usually designed to help you make and present your arguments, spoken or otherwise, to experts and non-experts, including people with other kinds of expertise.", rewrite: full, force: must, status: drafted }
  author-agent-written: "Describe this as a learning outcome that the usual Economics course is built to reach (presenting arguments to specialist and general audiences); the issuer states no modal, so record it as describing usual course design, not a requirement. Cite QAA (2023) Economics Subject Benchmark Statement, para 2.2, and do not claim every course must adopt it or that it is a rung item. Set it beside qaa/economics-2023/1.6.b4 and the honours descriptor qaa/fheq-2024/4.15.b8."
  author-agent-dialogue: "Raise this when a student asks what the course is meant to give them, or when a team writes programme outcomes, here presenting arguments to specialist and general audiences. Tell a student plainly: the course aims to help you argue clearly to any audience; for staff, compare it with your own programme outcomes. Ask \"Who outside economics would need to hear your argument, and how would you adapt it?\" Avoid presenting it as a minimum standard or quoting the list at length."
- statement: qaa/economics-2023/2.4
  forPractitioner: { text: "On joint or combined routes, plan for students to reach the core subject-specific and generic skills of economics, alongside the skills their other subject adds.", rewrite: light, force: will, status: drafted }
  forBeneficiary: { text: "If you study economics with another subject, you will gain the core economics skills, both subject-specific and general, and add others from your second subject.", rewrite: full, force: will, status: drafted }
  author-agent-written: "Present this as an expected outcome (will) for students on combined, joint or major-minor honours routes at FHEQ level 6: core elements of the subject's skills, with others added by the second subject. Cite QAA (2023) Economics Subject Benchmark Statement, para 2.4, and do not claim joint students meet every rung item, since paragraph 4.1 applies the rungs only where economics is a major component. Set it beside the threshold list qaa/economics-2023/4.3.b1 to 4.3.b8."
  author-agent-dialogue: "Raise this when a joint or combined honours student asks whether they are held to the same standards as single honours students. Tell them plainly that you will build the core economics skills and gain others from your second subject; for staff, frame it as what the joint route must still secure. Ask \"Which core economics skills does your timetable cover, and where?\" Do not suggest every rung item applies where economics is the minor part."
- statement: qaa/economics-2023/2.9
  forPractitioner: { text: "Include students in course monitoring and periodic review, alongside the information you collect and the external reference points you use.", rewrite: light, force: should, status: drafted }
  forBeneficiary: { text: "not-applicable: a duty on the degree-awarding body to involve students; not a standard for the student to reach", rewrite: full, force: should, status: drafted }
  author-agent-written: "Present this as an expectation on degree-awarding bodies and their partners (should): students take part in monitoring and periodic review. Cite QAA (2023) Economics Subject Benchmark Statement, para 2.9, and do not claim it sets a review cycle or a student outcome. Set it beside the external review expectation qaa/economics-2023/2.10."
  author-agent-dialogue: "Raise this with a programme team planning annual monitoring or periodic review. Ask \"How do students take part in review, beyond surveys?\" and \"How are their views reported back?\" Do not present it to a student as an obligation; a student asking how to have a say can be told the course should involve them."
- statement: qaa/economics-2023/2.10
  forPractitioner: { text: "Use external reviewers in periodic review to test proposed changes, confirm that threshold standards are achieved and check that content fits the subject.", rewrite: light, force: will, status: drafted }
  forBeneficiary: { text: "not-applicable: a duty on the provider; the student meets its effect", rewrite: full, force: will, status: drafted }
  author-agent-written: "Present this as an expected practice of providers (will): external reviewers in periodic review to secure threshold standards and suitable content. Cite QAA (2023) Economics Subject Benchmark Statement, para 2.10, and do not claim the statement sets how reviewers are chosen. Set it beside qaa/economics-2023/2.9 and the threshold list qaa/economics-2023/4.3.b1 to 4.3.b8."
  author-agent-dialogue: "Raise this with a team preparing for periodic review. Ask \"Which external reviewer will look at the proposed changes?\" and \"Which threshold items will they check?\" Do not raise it with students as a standard they meet."
- statement: qaa/economics-2023/3.2.b5
  forPractitioner: { text: "Teach marginal reasoning, and make sure students also learn where it breaks down, for example where threshold effects or sudden discontinuities, such as those in planetary crises, dominate.", rewrite: light, force: should, status: drafted }
  forBeneficiary: { text: "You should know how decisions often turn on small changes, and also where that way of thinking stops working, such as when sudden tipping points occur.", rewrite: full, force: should, status: drafted }
  author-agent-written: "Present this as an expectation on students (should) inside the list of key concepts most courses cover: awareness of the limits of marginal analysis, at FHEQ level 6. Cite QAA (2023) Economics Subject Benchmark Statement, para 3.2 (the marginal considerations item), and do not claim the rest of 3.2's concept list is required, as it describes what most courses cover. Set it beside qaa/economics-2023/4.3.b8 (more than one approach) and the honours descriptor qaa/fheq-2024/4.15.b4 on the limits of knowledge."
  author-agent-dialogue: "Raise this when a student applies marginal reasoning to a problem with tipping points, such as climate or financial crises. Ask \"Would a small change here have a small effect, or could it tip the system?\" Explain plainly that you should know when the marginal tool stops working; with staff, ask where the course shows its limits. Avoid presenting the full list of key concepts as a checklist."
- statement: qaa/economics-2023/3.3
  forPractitioner: { text: "Introduce data, programming, visualisation and computing skills, with mathematical, statistical and econometric methods and a focus on causality; give students practice on actual economic, financial or social data in suitable software, and teach the nature and sources of quantitative and qualitative data and how to choose methods.", rewrite: light, force: will, status: drafted }
  forBeneficiary: { text: "You will learn data, programming, visualisation and computing skills, including statistics and econometrics, use them on real economic or social data with suitable software, and learn how to choose the right method for the data.", rewrite: full, force: will, status: drafted }
  author-agent-written: "Present this as an expected outcome and course commitment (will) at FHEQ level 6: data, programming and econometric skills, practised on real data, with attention to causality. Cite QAA (2023) Economics Subject Benchmark Statement, para 3.3, and do not name particular software or languages as required, since the statement names none. Set it beside the methods rung items qaa/economics-2023/4.3.b3, 4.4.b3 and 4.5.b3 and the honours descriptor qaa/fheq-2024/4.15.b2."
  author-agent-dialogue: "Raise this when a student asks why coding or econometrics is in the course, or when staff plan where data skills are taught. Tell a student plainly that you will learn to work with real data using statistical software, and ask \"Which real dataset have you analysed, and how did you choose the method?\" For staff, ask where causality is taught. Do not imply a particular package is compulsory."
- statement: qaa/economics-2023/3.4
  forPractitioner: { text: "Make sure students can choose and apply the right economic tools and reasoning to applied fields and to policy design and evaluation, and that they learn to examine government policy and the performance of economies past and present.", rewrite: light, force: should, status: drafted }
  forBeneficiary: { text: "You should learn to choose and use the right economic tools and reasoning for real topics, and to examine government policy and how economies, including the UK's, have performed.", rewrite: full, force: should, status: drafted }
  author-agent-written: "Present this as an essential learning outcome with the force should, at FHEQ level 6: judgement in selecting and applying economic tools to applied topics and policy. Cite QAA (2023) Economics Subject Benchmark Statement, para 3.4, and do not claim it fixes which applied fields a course must offer, since 3.5 lists common ones only. Set it beside the policy rung items qaa/economics-2023/4.3.b5, 4.4.b5 and 4.5.b5, the outcome qaa/economics-2023/2.2.b6 and the honours descriptor qaa/fheq-2024/4.15.b6."
  author-agent-dialogue: "Raise this when a student is choosing which model to use for a real problem or a policy question. Ask \"Why is this the right tool here, and what would another tool tell you?\" Explain plainly that you should pick tools with judgement, not by habit; with staff, ask where students practise this choice. Avoid reading the paragraph aloud."
- statement: qaa/economics-2023/3.10
  forPractitioner: { text: "Plan specific support for language, mathematics (which may differ from school maths) and study and exam skills, given international and diverse cohorts and the jump from school-level economics.", rewrite: light, force: must, status: drafted }
  forBeneficiary: { text: "not-applicable: an expectation on course leaders; the student meets its effect", rewrite: full, force: must, status: drafted }
  author-agent-written: "Present this as an expectation on course leaders, worded 'need to' and recorded as describes because the phrase is outside the five obliging words: specific language, mathematics and study-skills support. Cite QAA (2023) Economics Subject Benchmark Statement, para 3.10, and do not claim it sets a level of provision. Set it beside qaa/economics-2023/2.2 (support where maths is not an entry condition) and qaa/economics-2023/1.10."
  author-agent-dialogue: "Raise this with a team planning induction, first-year support or exam preparation. Ask \"What help do students get with mathematics that differs from school, and with academic English?\" Do not present it to a student as their duty; point a student who is struggling to the support the course should offer."
- statement: qaa/economics-2023/4.2
  forPractitioner: { text: "Expect most students to exceed the threshold; set your own way of evidencing achievement above it, and refer to the Annex D descriptions of degree classes when doing so.", rewrite: light, force: should, status: drafted }
  forBeneficiary: { text: "not-applicable: a duty on the provider in judging and classifying achievement", rewrite: full, force: should, status: drafted }
  author-agent-written: "Present this as two claims: a prediction (will) that most students exceed the threshold, and an expectation on providers (should) to use Annex D when judging achievement above it. Cite QAA (2023) Economics Subject Benchmark Statement, para 4.2, and do not equate the typical or excellent rung with a degree class, as the statement makes no such mapping. Set it beside Annex D in std:doc:qaa-fheq-2024-framework (for example qaa/fheq-2024/annex-d/summary/r1/3rd) and the rung lists 4.3 to 4.5."
  author-agent-dialogue: "Raise this when staff align marking criteria or classification with the rung lists. Ask \"How do your class descriptors use Annex D?\" and \"Where would a typical graduate's work sit?\" Do not tell a student that the typical rung equals a 2.1 or that the threshold is a target."
- statement: qaa/economics-2023/4.3.b1
  forPractitioner: { text: "At threshold, check that every graduate has shown a working grasp of the discipline's main concepts, principles and analytical tools.", rewrite: light, force: threshold, status: drafted }
  forBeneficiary: { text: "To reach the threshold standard, you should have shown that you understand the main ideas, principles and tools of economics.", rewrite: full, force: threshold, status: drafted }
  author-agent-written: "Describe this as a threshold standard on key concepts, principles and tools: the least an Economics honours graduate at FHEQ level 6 (FQHEIS level 10) should have shown, not the level most reach. Cite QAA (2023) Economics Subject Benchmark Statement, para 4.3, and do not present it as a regulatory requirement or as binding where economics is a minor subject (para 4.1). Set it beside the same outcome higher up, qaa/economics-2023/4.4.b1 and qaa/economics-2023/4.5.b1, the honours descriptor qaa/fheq-2024/4.15.b1, the Annex D threshold cell qaa/fheq-2024/annex-d/knowledge/r2/3rd and spine:6."
  author-agent-dialogue: "Bring this up when a student or programme team asks what must be shown by graduation on key concepts, principles and tools. Tell a student in plain words that by the end you should be able to show you understand the main ideas, principles and tools of economics; for staff, frame it as the floor that every graduate's assessed work has to evidence. Ask \"Which core idea or tool could you explain and use without notes?\" and \"Which piece of assessed work shows it?\" Avoid reading the list aloud and avoid treating the typical or excellent rung as the minimum."
- statement: qaa/economics-2023/4.3.b2
  forPractitioner: { text: "At threshold, graduates should have shown they understand the principal theories of the subject, how they are interpreted and how economists model them.", rewrite: light, force: threshold, status: drafted }
  forBeneficiary: { text: "To reach the threshold standard, you should have shown that you understand the main theories in economics, how they are interpreted and how economists build models.", rewrite: full, force: threshold, status: drafted }
  author-agent-written: "Describe this as a threshold standard on key theories, interpretations and models: the least an Economics honours graduate at FHEQ level 6 (FQHEIS level 10) should have shown, not the level most reach. Cite QAA (2023) Economics Subject Benchmark Statement, para 4.3, and do not present it as a regulatory requirement or as binding where economics is a minor subject (para 4.1). Set it beside the same outcome higher up, qaa/economics-2023/4.4.b2 and qaa/economics-2023/4.5.b2, the honours descriptor qaa/fheq-2024/4.15.b3.1, the Annex D threshold cell qaa/fheq-2024/annex-d/knowledge/r2/3rd and spine:6."
  author-agent-dialogue: "Bring this up when a student or programme team asks what must be shown by graduation on key theories, interpretations and models. Tell a student in plain words that by the end you should understand the main theories, how they are read and how economists build models; for staff, frame it as the floor that every graduate's assessed work has to evidence. Ask \"Which theory could you explain, and which model goes with it?\" and \"Which piece of assessed work shows it?\" Avoid reading the list aloud and avoid treating the typical or excellent rung as the minimum."
- statement: qaa/economics-2023/4.3.b3
  forPractitioner: { text: "At threshold, graduates should have shown they understand the quantitative, qualitative and computing techniques their course uses and the settings where each fits.", rewrite: light, force: threshold, status: drafted }
  forBeneficiary: { text: "To reach the threshold standard, you should have shown that you understand the numerical, non-numerical and computing methods your course uses, and when each is the right one.", rewrite: full, force: threshold, status: drafted }
  author-agent-written: "Describe this as a threshold standard on quantitative and qualitative methods and computing: the least an Economics honours graduate at FHEQ level 6 (FQHEIS level 10) should have shown, not the level most reach. Cite QAA (2023) Economics Subject Benchmark Statement, para 4.3, and do not present it as a regulatory requirement or as binding where economics is a minor subject (para 4.1). Set it beside the same outcome higher up, qaa/economics-2023/4.4.b3 and qaa/economics-2023/4.5.b3, the honours descriptor qaa/fheq-2024/4.15.b2, the Annex D threshold cell qaa/fheq-2024/annex-d/practical/r1/3rd and spine:6."
  author-agent-dialogue: "Bring this up when a student or programme team asks what must be shown by graduation on quantitative and qualitative methods and computing. Tell a student in plain words that by the end you should understand the methods and computing techniques your course uses and when each fits; for staff, frame it as the floor that every graduate's assessed work has to evidence. Ask \"Which method would you choose for this question, and why that one?\" and \"Which piece of assessed work shows it?\" Avoid reading the list aloud and avoid treating the typical or excellent rung as the minimum."
- statement: qaa/economics-2023/4.3.b4
  forPractitioner: { text: "At threshold, graduates should have shown they know where economic data and evidence originate and what they hold, and which analytical methods fit them.", rewrite: light, force: threshold, status: drafted }
  forBeneficiary: { text: "To reach the threshold standard, you should have shown that you know where economic data and evidence come from, what they hold and which methods could be used to analyse them.", rewrite: full, force: threshold, status: drafted }
  author-agent-written: "Describe this as a threshold standard on sources and content of economic data and evidence: the least an Economics honours graduate at FHEQ level 6 (FQHEIS level 10) should have shown, not the level most reach. Cite QAA (2023) Economics Subject Benchmark Statement, para 4.3, and do not present it as a regulatory requirement or as binding where economics is a minor subject (para 4.1). Set it beside the same outcome higher up, qaa/economics-2023/4.4.b4 and qaa/economics-2023/4.5.b4, the honours descriptor qaa/fheq-2024/4.15.b7, the Annex D threshold cell qaa/fheq-2024/annex-d/practical/r4/3rd and spine:6."
  author-agent-dialogue: "Bring this up when a student or programme team asks what must be shown by graduation on sources and content of economic data and evidence. Tell a student in plain words that by the end you should know where economic data come from and which methods suit them; for staff, frame it as the floor that every graduate's assessed work has to evidence. Ask \"Where would you find data on this question, and what would you do with it?\" and \"Which piece of assessed work shows it?\" Avoid reading the list aloud and avoid treating the typical or excellent rung as the minimum."
- statement: qaa/economics-2023/4.3.b5
  forPractitioner: { text: "At threshold, graduates should have shown they can use economic reasoning on policy questions.", rewrite: light, force: threshold, status: drafted }
  forBeneficiary: { text: "To reach the threshold standard, you should have shown that you can use economic reasoning on policy questions.", rewrite: full, force: threshold, status: drafted }
  author-agent-written: "Describe this as a threshold standard on economic reasoning applied to policy: the least an Economics honours graduate at FHEQ level 6 (FQHEIS level 10) should have shown, not the level most reach. Cite QAA (2023) Economics Subject Benchmark Statement, para 4.3, and do not present it as a regulatory requirement or as binding where economics is a minor subject (para 4.1). Set it beside the same outcome higher up, qaa/economics-2023/4.4.b5 and qaa/economics-2023/4.5.b5, the honours descriptor qaa/fheq-2024/4.15.b6, the Annex D threshold cell qaa/fheq-2024/annex-d/cognitive/r2/3rd and spine:6."
  author-agent-dialogue: "Bring this up when a student or programme team asks what must be shown by graduation on economic reasoning applied to policy. Tell a student in plain words that by the end you should be able to use economic reasoning on a policy question; for staff, frame it as the floor that every graduate's assessed work has to evidence. Ask \"What does economic reasoning say about this policy?\" and \"Which piece of assessed work shows it?\" Avoid reading the list aloud and avoid treating the typical or excellent rung as the minimum."
- statement: qaa/economics-2023/4.3.b6
  forPractitioner: { text: "At threshold, graduates should have shown they know the wider settings, from history and politics to institutions, culture and the environment, in which economic analysis is used.", rewrite: light, force: threshold, status: drafted }
  forBeneficiary: { text: "To reach the threshold standard, you should have shown that you know the wider settings, such as history, politics, institutions, society, culture and the environment, in which economic analysis is used.", rewrite: full, force: threshold, status: drafted }
  author-agent-written: "Describe this as a threshold standard on the contexts in which economic analysis is used: the least an Economics honours graduate at FHEQ level 6 (FQHEIS level 10) should have shown, not the level most reach. Cite QAA (2023) Economics Subject Benchmark Statement, para 4.3, and do not present it as a regulatory requirement or as binding where economics is a minor subject (para 4.1). Set it beside the same outcome higher up, qaa/economics-2023/4.4.b6 and qaa/economics-2023/4.5.b6, the honours descriptor qaa/fheq-2024/4.15.b1, the Annex D threshold cell qaa/fheq-2024/annex-d/knowledge/r1/3rd and spine:6."
  author-agent-dialogue: "Bring this up when a student or programme team asks what must be shown by graduation on the contexts in which economic analysis is used. Tell a student in plain words that by the end you should know the wider settings in which an economic analysis is used; for staff, frame it as the floor that every graduate's assessed work has to evidence. Ask \"What in the history, politics or environment around this problem changes your analysis?\" and \"Which piece of assessed work shows it?\" Avoid reading the list aloud and avoid treating the typical or excellent rung as the minimum."
- statement: qaa/economics-2023/4.3.b7
  forPractitioner: { text: "At threshold, graduates should have shown knowledge of an appropriate range of specialist fields, some of it drawn from research in the subject.", rewrite: light, force: threshold, status: drafted }
  forBeneficiary: { text: "To reach the threshold standard, you should have shown that you know several specialist areas of economics, partly through research in those areas.", rewrite: full, force: threshold, status: drafted }
  author-agent-written: "Describe this as a threshold standard on knowledge of specialised areas, partly drawn from research: the least an Economics honours graduate at FHEQ level 6 (FQHEIS level 10) should have shown, not the level most reach. Cite QAA (2023) Economics Subject Benchmark Statement, para 4.3, and do not present it as a regulatory requirement or as binding where economics is a minor subject (para 4.1). Set it beside the same outcome higher up, qaa/economics-2023/4.4.b7 and qaa/economics-2023/4.5.b7, the honours descriptor qaa/fheq-2024/4.15.b3.2, the Annex D threshold cell qaa/fheq-2024/annex-d/cognitive/r1/3rd and spine:6."
  author-agent-dialogue: "Bring this up when a student or programme team asks what must be shown by graduation on knowledge of specialised areas, partly drawn from research. Tell a student in plain words that by the end you should know a few specialist areas of economics, some of it through research; for staff, frame it as the floor that every graduate's assessed work has to evidence. Ask \"Which specialist area do you know best, and which research shaped what you know?\" and \"Which piece of assessed work shows it?\" Avoid reading the list aloud and avoid treating the typical or excellent rung as the minimum."
- statement: qaa/economics-2023/4.3.b8
  forPractitioner: { text: "At threshold, graduates should have shown they recognise that many economic problems can be approached in more than one way.", rewrite: light, force: threshold, status: drafted }
  forBeneficiary: { text: "To reach the threshold standard, you should have shown that you know many economic problems can be tackled in more than one way.", rewrite: full, force: threshold, status: drafted }
  author-agent-written: "Describe this as a threshold standard on awareness that problems allow more than one approach: the least an Economics honours graduate at FHEQ level 6 (FQHEIS level 10) should have shown, not the level most reach. Cite QAA (2023) Economics Subject Benchmark Statement, para 4.3, and do not present it as a regulatory requirement or as binding where economics is a minor subject (para 4.1). Set it beside the same outcome higher up, qaa/economics-2023/4.4.b8 and qaa/economics-2023/4.5.b8, the honours descriptor qaa/fheq-2024/4.15.b4, the Annex D threshold cell qaa/fheq-2024/annex-d/cognitive/r2/3rd and spine:6."
  author-agent-dialogue: "Bring this up when a student or programme team asks what must be shown by graduation on awareness that problems allow more than one approach. Tell a student in plain words that by the end you should know that many problems can be tackled in more than one way; for staff, frame it as the floor that every graduate's assessed work has to evidence. Ask \"What other approach could someone take to this problem?\" and \"Which piece of assessed work shows it?\" Avoid reading the list aloud and avoid treating the typical or excellent rung as the minimum."
- statement: qaa/economics-2023/4.4.b1
  forPractitioner: { text: "At the typical level, graduates should have shown they understand economic concepts, principles and tools as a connected system, not as separate items.", rewrite: light, force: should, status: drafted }
  forBeneficiary: { text: "At the typical level, you should have shown that you understand economic ideas, principles and tools as a connected whole.", rewrite: full, force: should, status: drafted }
  author-agent-written: "Describe this as the typical rung on systematic grasp of concepts, principles and tools: what most Economics honours graduates at FHEQ level 6 should have shown, above the minimum in qaa/economics-2023/4.3.b1. Cite QAA (2023) Economics Subject Benchmark Statement, para 4.4, and do not call it a pass requirement or tie it to a degree class, since the statement leaves classes to Annex D (para 4.2). Set it beside qaa/economics-2023/4.3.b1, qaa/economics-2023/4.5.b1 and the honours descriptor qaa/fheq-2024/4.15.b1 at spine:6."
  author-agent-dialogue: "Raise this when a student wants to know what a good, ordinary result looks like on systematic grasp of concepts, principles and tools, or when staff calibrate marking above the minimum. Tell a student that most people at the end understand economic ideas, principles and tools as a connected whole, and make clear that falling short of it is not failing; with staff, use it to describe the usual graduate. Ask \"How do the core ideas you have learned fit together?\" Do not present this rung as the pass standard or quote the issuer's list at length."
- statement: qaa/economics-2023/4.4.b2
  forPractitioner: { text: "At the typical level, graduates should have shown a systematic grasp of the subject's distinctive theories, interpretations and models and be able to use them competently.", rewrite: light, force: should, status: drafted }
  forBeneficiary: { text: "At the typical level, you should have shown a systematic understanding of the distinctive theories and models of economics and that you can use them competently.", rewrite: full, force: should, status: drafted }
  author-agent-written: "Describe this as the typical rung on systematic grasp of distinctive theories and models, used competently: what most Economics honours graduates at FHEQ level 6 should have shown, above the minimum in qaa/economics-2023/4.3.b2. Cite QAA (2023) Economics Subject Benchmark Statement, para 4.4, and do not call it a pass requirement or tie it to a degree class, since the statement leaves classes to Annex D (para 4.2). Set it beside qaa/economics-2023/4.3.b2, qaa/economics-2023/4.5.b2 and the honours descriptor qaa/fheq-2024/4.15.b3.1 at spine:6."
  author-agent-dialogue: "Raise this when a student wants to know what a good, ordinary result looks like on systematic grasp of distinctive theories and models, used competently, or when staff calibrate marking above the minimum. Tell a student that most people at the end understand the distinctive theories and models systematically and use them well, and make clear that falling short of it is not failing; with staff, use it to describe the usual graduate. Ask \"Which model would you choose for this question, and how confident are you using it?\" Do not present this rung as the pass standard or quote the issuer's list at length."
- statement: qaa/economics-2023/4.4.b3
  forPractitioner: { text: "At the typical level, graduates should have shown proficiency in quantitative and computing techniques and know how to apply them effectively to varied problems.", rewrite: light, force: should, status: drafted }
  forBeneficiary: { text: "At the typical level, you should have shown that you are proficient in quantitative and computing methods and can use them well on different kinds of problem.", rewrite: full, force: should, status: drafted }
  author-agent-written: "Describe this as the typical rung on proficiency in methods and computing across problems: what most Economics honours graduates at FHEQ level 6 should have shown, above the minimum in qaa/economics-2023/4.3.b3. Cite QAA (2023) Economics Subject Benchmark Statement, para 4.4, and do not call it a pass requirement or tie it to a degree class, since the statement leaves classes to Annex D (para 4.2). Set it beside qaa/economics-2023/4.3.b3, qaa/economics-2023/4.5.b3 and the honours descriptor qaa/fheq-2024/4.15.b2 at spine:6."
  author-agent-dialogue: "Raise this when a student wants to know what a good, ordinary result looks like on proficiency in methods and computing across problems, or when staff calibrate marking above the minimum. Tell a student that most people at the end are proficient in quantitative and computing methods across different problems, and make clear that falling short of it is not failing; with staff, use it to describe the usual graduate. Ask \"Which technique have you used on more than one kind of problem?\" Do not present this rung as the pass standard or quote the issuer's list at length."
- statement: qaa/economics-2023/4.4.b4
  forPractitioner: { text: "At the typical level, graduates should have shown a systematic grasp of where economic data and evidence come from, what they contain and which methods suit their analysis.", rewrite: light, force: should, status: drafted }
  forBeneficiary: { text: "At the typical level, you should have shown a systematic understanding of economic data and evidence, where they come from and which methods suit them.", rewrite: full, force: should, status: drafted }
  author-agent-written: "Describe this as the typical rung on systematic grasp of data, evidence and methods for them: what most Economics honours graduates at FHEQ level 6 should have shown, above the minimum in qaa/economics-2023/4.3.b4. Cite QAA (2023) Economics Subject Benchmark Statement, para 4.4, and do not call it a pass requirement or tie it to a degree class, since the statement leaves classes to Annex D (para 4.2). Set it beside qaa/economics-2023/4.3.b4, qaa/economics-2023/4.5.b4 and the honours descriptor qaa/fheq-2024/4.15.b7 at spine:6."
  author-agent-dialogue: "Raise this when a student wants to know what a good, ordinary result looks like on systematic grasp of data, evidence and methods for them, or when staff calibrate marking above the minimum. Tell a student that most people at the end understand economic data and evidence systematically, with the methods that suit them, and make clear that falling short of it is not failing; with staff, use it to describe the usual graduate. Ask \"How did you decide which data and which method fitted your question?\" Do not present this rung as the pass standard or quote the issuer's list at length."
- statement: qaa/economics-2023/4.4.b5
  forPractitioner: { text: "At the typical level, graduates should have shown they can bring economic reasoning to bear on policy questions critically.", rewrite: light, force: should, status: drafted }
  forBeneficiary: { text: "At the typical level, you should have shown that you can use economic reasoning on policy questions critically, not only apply it.", rewrite: full, force: should, status: drafted }
  author-agent-written: "Describe this as the typical rung on applying economic reasoning to policy critically: what most Economics honours graduates at FHEQ level 6 should have shown, above the minimum in qaa/economics-2023/4.3.b5. Cite QAA (2023) Economics Subject Benchmark Statement, para 4.4, and do not call it a pass requirement or tie it to a degree class, since the statement leaves classes to Annex D (para 4.2). Set it beside qaa/economics-2023/4.3.b5, qaa/economics-2023/4.5.b5 and the honours descriptor qaa/fheq-2024/4.15.b6 at spine:6."
  author-agent-dialogue: "Raise this when a student wants to know what a good, ordinary result looks like on applying economic reasoning to policy critically, or when staff calibrate marking above the minimum. Tell a student that most people at the end use economic reasoning on policy critically, and make clear that falling short of it is not failing; with staff, use it to describe the usual graduate. Ask \"What are the weaknesses of the economic case for this policy?\" Do not present this rung as the pass standard or quote the issuer's list at length."
- statement: qaa/economics-2023/4.4.b6
  forPractitioner: { text: "At the typical level, graduates should have shown a systematic grasp of the wider settings, historical to environmental, in which economic analysis is used.", rewrite: light, force: should, status: drafted }
  forBeneficiary: { text: "At the typical level, you should have shown a systematic understanding of the wider settings, such as history, politics, institutions, culture and the environment, in which economic analysis is used.", rewrite: full, force: should, status: drafted }
  author-agent-written: "Describe this as the typical rung on systematic grasp of the contexts of economic analysis: what most Economics honours graduates at FHEQ level 6 should have shown, above the minimum in qaa/economics-2023/4.3.b6. Cite QAA (2023) Economics Subject Benchmark Statement, para 4.4, and do not call it a pass requirement or tie it to a degree class, since the statement leaves classes to Annex D (para 4.2). Set it beside qaa/economics-2023/4.3.b6, qaa/economics-2023/4.5.b6 and the honours descriptor qaa/fheq-2024/4.15.b1 at spine:6."
  author-agent-dialogue: "Raise this when a student wants to know what a good, ordinary result looks like on systematic grasp of the contexts of economic analysis, or when staff calibrate marking above the minimum. Tell a student that most people at the end understand systematically the wider settings in which economic analysis is used, and make clear that falling short of it is not failing; with staff, use it to describe the usual graduate. Ask \"How does the setting of this problem shape what the analysis can say?\" Do not present this rung as the pass standard or quote the issuer's list at length."
- statement: qaa/economics-2023/4.4.b7
  forPractitioner: { text: "At the typical level, graduates should have shown knowledge of an appropriate range of specialist fields and an appreciation of the research written in them.", rewrite: light, force: should, status: drafted }
  forBeneficiary: { text: "At the typical level, you should have shown that you know several specialist areas of economics and appreciate the research written in them.", rewrite: full, force: should, status: drafted }
  author-agent-written: "Describe this as the typical rung on specialised areas and their research literature: what most Economics honours graduates at FHEQ level 6 should have shown, above the minimum in qaa/economics-2023/4.3.b7. Cite QAA (2023) Economics Subject Benchmark Statement, para 4.4, and do not call it a pass requirement or tie it to a degree class, since the statement leaves classes to Annex D (para 4.2). Set it beside qaa/economics-2023/4.3.b7, qaa/economics-2023/4.5.b7 and the honours descriptor qaa/fheq-2024/4.15.b3.2 at spine:6."
  author-agent-dialogue: "Raise this when a student wants to know what a good, ordinary result looks like on specialised areas and their research literature, or when staff calibrate marking above the minimum. Tell a student that most people at the end know several specialist areas and appreciate their research literature, and make clear that falling short of it is not failing; with staff, use it to describe the usual graduate. Ask \"Which recent study in your specialist area would you recommend, and why?\" Do not present this rung as the pass standard or quote the issuer's list at length."
- statement: qaa/economics-2023/4.4.b8
  forPractitioner: { text: "At the typical level, graduates should have shown familiarity with several approaches to economic problems and critical awareness of their applicability and limits in particular settings.", rewrite: light, force: should, status: drafted }
  forBeneficiary: { text: "At the typical level, you should have shown that you know several ways to tackle economic problems and can judge critically where each works and where it falls short.", rewrite: full, force: should, status: drafted }
  author-agent-written: "Describe this as the typical rung on different approaches and a critical sense of their limits: what most Economics honours graduates at FHEQ level 6 should have shown, above the minimum in qaa/economics-2023/4.3.b8. Cite QAA (2023) Economics Subject Benchmark Statement, para 4.4, and do not call it a pass requirement or tie it to a degree class, since the statement leaves classes to Annex D (para 4.2). Set it beside qaa/economics-2023/4.3.b8, qaa/economics-2023/4.5.b8 and the honours descriptor qaa/fheq-2024/4.15.b4 at spine:6."
  author-agent-dialogue: "Raise this when a student wants to know what a good, ordinary result looks like on different approaches and a critical sense of their limits, or when staff calibrate marking above the minimum. Tell a student that most people at the end know several approaches and judge critically where each works, and make clear that falling short of it is not failing; with staff, use it to describe the usual graduate. Ask \"Where would this approach stop working, and what would you use instead?\" Do not present this rung as the pass standard or quote the issuer's list at length."
- statement: qaa/economics-2023/4.5.b1
  forPractitioner: { text: "At the excellent level, graduates should consistently have shown an outstanding grasp of the subject's concepts, principles and tools.", rewrite: light, force: should, status: drafted }
  forBeneficiary: { text: "At the excellent level, you should consistently have shown an outstanding grasp of economic ideas, principles and tools.", rewrite: full, force: should, status: drafted }
  author-agent-written: "Describe this as the excellent rung on excellent understanding of concepts, principles and tools: an aspiration for the strongest Economics honours graduates at FHEQ level 6, shown consistently. Cite QAA (2023) Economics Subject Benchmark Statement, para 4.5, and do not present it as required or as the same thing as a first; compare it only loosely with qaa/fheq-2024/annex-d/knowledge/r2/1st. Set it beside qaa/economics-2023/4.4.b1, qaa/economics-2023/4.3.b1 and the honours descriptor qaa/fheq-2024/4.15.b1."
  author-agent-dialogue: "Raise this when a strong student asks how to stand out on excellent understanding of concepts, principles and tools, or when staff describe their best work. Say in plain words that the very best show an outstanding grasp of economic ideas, principles and tools, and do so consistently; with staff, frame it as an aspiration, not a requirement. Ask \"Where could you explain a core idea in a way that goes past the textbook?\" Do not treat it as expected of everyone or read the issuer's wording aloud at length."
- statement: qaa/economics-2023/4.5.b2
  forPractitioner: { text: "At the excellent level, graduates should consistently have shown an outstanding grasp of distinctive theories, interpretations and models and use them competently in research.", rewrite: light, force: should, status: drafted }
  forBeneficiary: { text: "At the excellent level, you should consistently have shown an outstanding understanding of distinctive theories and models in economics and used them well in your own research.", rewrite: full, force: should, status: drafted }
  author-agent-written: "Describe this as the excellent rung on excellent grasp of theories and models, used competently in research: an aspiration for the strongest Economics honours graduates at FHEQ level 6, shown consistently. Cite QAA (2023) Economics Subject Benchmark Statement, para 4.5, and do not present it as required or as the same thing as a first; compare it only loosely with qaa/fheq-2024/annex-d/knowledge/r2/1st. Set it beside qaa/economics-2023/4.4.b2, qaa/economics-2023/4.3.b2 and the honours descriptor qaa/fheq-2024/4.15.b3.1."
  author-agent-dialogue: "Raise this when a strong student asks how to stand out on excellent grasp of theories and models, used competently in research, or when staff describe their best work. Say in plain words that the very best understand distinctive theories and models outstandingly and use them well in research, and do so consistently; with staff, frame it as an aspiration, not a requirement. Ask \"How did you use a theory or model in your own research, and what did it let you see?\" Do not treat it as expected of everyone or read the issuer's wording aloud at length."
- statement: qaa/economics-2023/4.5.b3
  forPractitioner: { text: "At the excellent level, graduates should consistently have shown excellence in quantitative and computing techniques and know how to apply them effectively to varied problems.", rewrite: light, force: should, status: drafted }
  forBeneficiary: { text: "At the excellent level, you should consistently have shown excellent quantitative and computing skills and used them well on many kinds of problem.", rewrite: full, force: should, status: drafted }
  author-agent-written: "Describe this as the excellent rung on excellence in methods and computing across problems: an aspiration for the strongest Economics honours graduates at FHEQ level 6, shown consistently. Cite QAA (2023) Economics Subject Benchmark Statement, para 4.5, and do not present it as required or as the same thing as a first; compare it only loosely with qaa/fheq-2024/annex-d/practical/r1/1st. Set it beside qaa/economics-2023/4.4.b3, qaa/economics-2023/4.3.b3 and the honours descriptor qaa/fheq-2024/4.15.b2."
  author-agent-dialogue: "Raise this when a strong student asks how to stand out on excellence in methods and computing across problems, or when staff describe their best work. Say in plain words that the very best show excellent quantitative and computing skills across many problems, and do so consistently; with staff, frame it as an aspiration, not a requirement. Ask \"Which hard problem did your methods let you crack?\" Do not treat it as expected of everyone or read the issuer's wording aloud at length."
- statement: qaa/economics-2023/4.5.b4
  forPractitioner: { text: "At the excellent level, graduates should consistently have shown an excellent command of economic data and evidence and of the methods that suit their analysis.", rewrite: light, force: should, status: drafted }
  forBeneficiary: { text: "At the excellent level, you should consistently have shown an excellent command of economic data and evidence and of the methods that suit them.", rewrite: full, force: should, status: drafted }
  author-agent-written: "Describe this as the excellent rung on excellent grasp of data, evidence and methods for them: an aspiration for the strongest Economics honours graduates at FHEQ level 6, shown consistently. Cite QAA (2023) Economics Subject Benchmark Statement, para 4.5, and do not present it as required or as the same thing as a first; compare it only loosely with qaa/fheq-2024/annex-d/practical/r4/1st. Set it beside qaa/economics-2023/4.4.b4, qaa/economics-2023/4.3.b4 and the honours descriptor qaa/fheq-2024/4.15.b7."
  author-agent-dialogue: "Raise this when a strong student asks how to stand out on excellent grasp of data, evidence and methods for them, or when staff describe their best work. Say in plain words that the very best command economic data, evidence and their methods excellently, and do so consistently; with staff, frame it as an aspiration, not a requirement. Ask \"What makes your choice of data and method the strongest one available?\" Do not treat it as expected of everyone or read the issuer's wording aloud at length."
- statement: qaa/economics-2023/4.5.b5
  forPractitioner: { text: "At the excellent level, graduates should consistently have shown advanced, critical use of economic reasoning on policy issues.", rewrite: light, force: should, status: drafted }
  forBeneficiary: { text: "At the excellent level, you should consistently have shown advanced, critical use of economic reasoning on policy questions.", rewrite: full, force: should, status: drafted }
  author-agent-written: "Describe this as the excellent rung on advanced, critical application of economic reasoning to policy: an aspiration for the strongest Economics honours graduates at FHEQ level 6, shown consistently. Cite QAA (2023) Economics Subject Benchmark Statement, para 4.5, and do not present it as required or as the same thing as a first; compare it only loosely with qaa/fheq-2024/annex-d/cognitive/r2/1st. Set it beside qaa/economics-2023/4.4.b5, qaa/economics-2023/4.3.b5 and the honours descriptor qaa/fheq-2024/4.15.b6."
  author-agent-dialogue: "Raise this when a strong student asks how to stand out on advanced, critical application of economic reasoning to policy, or when staff describe their best work. Say in plain words that the very best use economic reasoning on policy with advanced, critical judgement, and do so consistently; with staff, frame it as an aspiration, not a requirement. Ask \"What would you advise a minister, and what is the strongest objection to your advice?\" Do not treat it as expected of everyone or read the issuer's wording aloud at length."
- statement: qaa/economics-2023/4.5.b6
  forPractitioner: { text: "At the excellent level, graduates should consistently have shown an excellent grasp of the wider settings, historical to environmental, in which economic analysis is used.", rewrite: light, force: should, status: drafted }
  forBeneficiary: { text: "At the excellent level, you should consistently have shown an excellent understanding of the wider settings in which economic analysis is used, from history and politics to culture and the environment.", rewrite: full, force: should, status: drafted }
  author-agent-written: "Describe this as the excellent rung on excellent grasp of the contexts of economic analysis: an aspiration for the strongest Economics honours graduates at FHEQ level 6, shown consistently. Cite QAA (2023) Economics Subject Benchmark Statement, para 4.5, and do not present it as required or as the same thing as a first; compare it only loosely with qaa/fheq-2024/annex-d/knowledge/r1/1st. Set it beside qaa/economics-2023/4.4.b6, qaa/economics-2023/4.3.b6 and the honours descriptor qaa/fheq-2024/4.15.b1."
  author-agent-dialogue: "Raise this when a strong student asks how to stand out on excellent grasp of the contexts of economic analysis, or when staff describe their best work. Say in plain words that the very best understand outstandingly the wider settings in which economic analysis is used, and do so consistently; with staff, frame it as an aspiration, not a requirement. Ask \"Which part of the wider setting would most change your conclusion?\" Do not treat it as expected of everyone or read the issuer's wording aloud at length."
- statement: qaa/economics-2023/4.5.b7
  forPractitioner: { text: "At the excellent level, graduates should consistently have shown advanced knowledge of an appropriate range of specialist fields, rooted in current research.", rewrite: light, force: should, status: drafted }
  forBeneficiary: { text: "At the excellent level, you should consistently have shown advanced knowledge of several specialist areas of economics, built on current research.", rewrite: full, force: should, status: drafted }
  author-agent-written: "Describe this as the excellent rung on advanced knowledge of specialised areas, set in current research: an aspiration for the strongest Economics honours graduates at FHEQ level 6, shown consistently. Cite QAA (2023) Economics Subject Benchmark Statement, para 4.5, and do not present it as required or as the same thing as a first; compare it only loosely with qaa/fheq-2024/annex-d/cognitive/r1/1st. Set it beside qaa/economics-2023/4.4.b7, qaa/economics-2023/4.3.b7 and the honours descriptor qaa/fheq-2024/4.15.b3.2."
  author-agent-dialogue: "Raise this when a strong student asks how to stand out on advanced knowledge of specialised areas, set in current research, or when staff describe their best work. Say in plain words that the very best know specialist areas in advanced depth, built on current research, and do so consistently; with staff, frame it as an aspiration, not a requirement. Ask \"Which current debate in your specialist area could you take a side in, and why?\" Do not treat it as expected of everyone or read the issuer's wording aloud at length."
- statement: qaa/economics-2023/4.5.b8
  forPractitioner: { text: "At the excellent level, graduates should consistently have shown excellent knowledge of alternative approaches and their applicability and limits, and creative, well-judged use of them across diverse settings.", rewrite: light, force: should, status: drafted }
  forBeneficiary: { text: "At the excellent level, you should consistently have shown excellent knowledge of different ways to tackle economic problems, where each works and where it fails, and used them creatively and with sound judgement.", rewrite: full, force: should, status: drafted }
  author-agent-written: "Describe this as the excellent rung on excellent judgement across approaches, showing creativity: an aspiration for the strongest Economics honours graduates at FHEQ level 6, shown consistently. Cite QAA (2023) Economics Subject Benchmark Statement, para 4.5, and do not present it as required or as the same thing as a first; compare it only loosely with qaa/fheq-2024/annex-d/cognitive/r2/1st. Set it beside qaa/economics-2023/4.4.b8, qaa/economics-2023/4.3.b8 and the honours descriptor qaa/fheq-2024/4.15.b4."
  author-agent-dialogue: "Raise this when a strong student asks how to stand out on excellent judgement across approaches, showing creativity, or when staff describe their best work. Say in plain words that the very best choose among approaches creatively and with sound judgement, and do so consistently; with staff, frame it as an aspiration, not a requirement. Ask \"When did you combine or swap approaches creatively, and what made that the right call?\" Do not treat it as expected of everyone or read the issuer's wording aloud at length."
```

### S5 Levels and alignment
<!-- label: both; status: drafted; basis: primary -->
```yaml
levels:
  - { id: "fheq:6", role: "cites", locator: "D1, 2.3; 4.2" }
  - { id: "fqheis:10", role: "cites", locator: "D1, 2.3; 4.2" }
crosswalks:
  - { from: "fheq:6", to: "fqheis:10", relation: "equivalent", basis: "stated (D1, 2.3: \"a degree with honours (FHEQ Level 6; FQHEIS Level 10)\"; 4.2)" }
```

### S6 Themes
<!-- label: both; status: drafted; basis: primary -->
```yaml
- { id: "theme:edi", role: "carries", carriedIn: ["1.7", "1.8", "1.9", "1.11", "1.12", "2.7", "2.8", "3.10", "3.11"] }
- { id: "theme:accessibility", role: "carries", carriedIn: ["1.7", "1.10", "1.11", "1.12", "1.13", "1.14", "3.11"] }
- { id: "theme:esd", role: "carries", carriedIn: ["1.2", "1.3", "1.5", "1.15", "1.16", "1.17", "1.18", "1.19", "3.2"] }
- { id: "theme:enterprise", role: "carries", carriedIn: ["1.20", "1.21", "1.22", "1.23", "1.24", "1.25", "1.26", "2.7", "3.7"] }
```

### S7 Relations
<!-- label: both; status: drafted; basis: primary -->
```yaml
- { rel: "partOf", target: "collection: QAA Subject Benchmark Statements", note: "one of 54 held by stan" }
- { rel: "supersedes", target: "std:doc:qaa-economics-2019-benchmarks (fourth edition, 2019; not yet ingested)", note: "the back matter names the 2019 fourth edition and the front matter lists key changes from the previous statement" }
- { rel: "refersTo", target: "std:doc:qaa-fheq-2024-framework, Annex D", note: "the outcome classification descriptions for FHEQ level 6 and FQHEIS level 10 degrees (4.2)" }
- { rel: "refersTo", target: "std:doc:qaa-fheq-2024-framework", note: "FHEQ level 6 (2.3; 4.2)" }
- { rel: "refersTo", target: "std:doc:qaa-fqheis-2024-framework", note: "FQHEIS level 10 (2.3; 4.2)" }
- { rel: "cites", target: "std:doc:qaa-advancehe-esd-2021-guidance", note: "the Education for Sustainable Development Guidance (Advance HE and QAA, March 2021), with whose learning outcomes the core skills of 1.6 align (1.17)" }
- { rel: "refersTo", target: "QAA Quality Code, Advice and Guidance (not yet ingested)", note: "front matter" }
- { rel: "refersTo", target: "QAA Glossary (not ingested)", note: "front matter" }
```

### S8 Currency and review
<!-- label: source; status: drafted; basis: primary -->
```yaml
published: "2023-03"
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
- A social science of how individuals and groups decide and interact within institutions, power structures and their wider setting, aiming to inform policy through theory and evidence (D1, 1.2, 1.4).
- Its central question is how resources are allocated, distributed and used, and what follows for well-being and sustainability, past, present and future (D1, 1.2).
- It works at micro and macro levels and in static and dynamic terms; because interpretations are contested, it studies phenomena through several theoretical lenses and in their historical, political, social and environmental settings (D1, 1.3).
- Its characteristic method is abstraction and modelling tested against quantitative and qualitative evidence, with causality to the fore and attention to the limits of its own tools (D1, 1.5, 1.6, 3.3).
- It links to politics, geography, history, philosophy, law, data science, psychology and the sciences, and underpins finance, business and accounting (D1, 1.4).
- It names its own narrow make-up (a field that remains predominantly white, male and Western) as an EDI challenge (D1, 1.9).
- Its graduates enter a wide range of sectors, as professional economists and in other careers (D1, 1.5, 2.1).

### SB2 Themes in this subject
<!-- label: both; status: drafted; basis: primary -->
```yaml
- theme: theme:edi
  inThisSubject: "the subject itself studies discrimination and inequality and debates sensitive questions from evidence; it names its narrow make-up and its concentration in selective universities, and asks for inclusive materials, widening participation, zero tolerance of harassment and closing awarding gaps (D1, 1.7 to 1.9; 2.7; 2.8; 3.11)"
  statements: ["qaa/economics-2023/1.7"]
- theme: theme:accessibility
  inThisSubject: "inclusive pedagogy and resources; blended delivery since 2020 and its risks for equal access; digital accessibility of graphs, video, data and specialist software, with sector examples (D1, 1.10 to 1.14; 3.11)"
  statements: ["qaa/economics-2023/1.10", "qaa/economics-2023/1.13"]
- theme: theme:esd
  inThisSubject: "headed Sustainability: framed by the UN SDGs and Global Compact, defined in the text and built into concepts and models; graduates able to face the planetary crisis; core skills aligned with the ESD guidance's competencies and with SDGs 8, 9, 10 and 12 (D1, 1.15 to 1.19; 3.2)"
  statements: ["qaa/economics-2023/1.16"]
- theme: theme:enterprise
  inThisSubject: "headed Enterprise and entrepreneurship education: transferable skills for careers, data and software fluency, communicating to wide audiences, placements and degree apprenticeships, and civic as well as career value (D1, 1.20 to 1.26; 2.7)"
  statements: []
```

### SB3 Content and delivery
<!-- label: both; status: drafted; basis: primary -->
```yaml
areas:
  - { component: "3.2", gloss: "eight key concepts: opportunity cost and scarcity; incentives and biases; strategic thinking; expectations and shocks; marginal considerations; equilibrium and dynamics; mutual gains, conflict and power; markets and market failure" }
  - { component: "3.5", gloss: "fourteen common applied fields beside the core micro, macro and econometrics, from behavioural to public economics" }
  - { component: "3.6", gloss: "economic history and the history of economic thought, embedded or taught separately" }
practices:
  - { component: "2.6", kind: "learning", gloss: "mixed distance, online and in-person delivery; independent and peer learning; varied materials including code and policy briefs" }
  - { component: "3.7", kind: "teaching", gloss: "lectures, seminars, tutorials, workshops, peer and project-based learning, experiments, games, technology-enabled and experiential learning, practitioners" }
  - { component: "3.8", kind: "learning", gloss: "interactive, student-centred and blended learning since the pandemic" }
  - { component: "3.9", kind: "teaching", gloss: "subject teaching networks and general teaching centres as resources" }
  - { component: "3.11", kind: "teaching", gloss: "pluralist and decolonial approaches" }
  - { component: "3.12", kind: "assessment", gloss: "course-level analysis of assessment design" }
  - { component: "3.13", kind: "assessment", gloss: "assessment that builds problem-solving and higher-order reasoning" }
  - { component: "3.14", kind: "assessment", gloss: "closed and open-book exams, projects, essays, multimedia, group and policy-brief tasks; authentic, data-based assessment" }
  - { component: "3.15", kind: "assessment", gloss: "formative assessment, feedback and scaffolded skills development" }
```

### SB4 Benchmark standards
<!-- label: both; status: drafted; basis: primary -->
```yaml
rungs:
  - { rung: "threshold", leadIn: "4.3", award: "bachelor's with honours", items: 8 }
  - { rung: "typical", leadIn: "4.4", award: "bachelor's with honours", items: 8 }
  - { rung: "excellent", leadIn: "4.5", award: "bachelor's with honours", items: 8 }
rungBases: "4.1: the rungs apply to single honours and to joint degrees where economics is a major part, not in full where it is a minor part; reaching typical implies threshold. 4.2: most students exceed the threshold; achievement above it is judged by each provider with Annex D. 4.5 adds 'consistently'."
outcomeLists:
  - { leadIn: "1.6", gloss: "core intellectual abilities economists need (lead-in uses need, recorded as describes)", items: 6, award: ["honours"] }
  - { leadIn: "2.2", gloss: "learning outcomes the typical course is designed to achieve (no modal)", items: 8, award: ["honours"] }
outcomes:
  - { outcome: "concepts, principles and tools", threshold: "qaa/economics-2023/4.3.b1", typical: "qaa/economics-2023/4.4.b1", excellent: "qaa/economics-2023/4.5.b1", basis: "inferred", domain: "understanding", award: "bachelor's with honours" }
  - { outcome: "theories, interpretations and modelling", threshold: "qaa/economics-2023/4.3.b2", typical: "qaa/economics-2023/4.4.b2", excellent: "qaa/economics-2023/4.5.b2", basis: "inferred", domain: "understanding", award: "bachelor's with honours" }
  - { outcome: "quantitative and qualitative methods and computing", threshold: "qaa/economics-2023/4.3.b3", typical: "qaa/economics-2023/4.4.b3", excellent: "qaa/economics-2023/4.5.b3", basis: "inferred", domain: "subject-skill", award: "bachelor's with honours" }
  - { outcome: "data and evidence", threshold: "qaa/economics-2023/4.3.b4", typical: "qaa/economics-2023/4.4.b4", excellent: "qaa/economics-2023/4.5.b4", basis: "inferred", domain: "knowledge", award: "bachelor's with honours" }
  - { outcome: "economic reasoning applied to policy", threshold: "qaa/economics-2023/4.3.b5", typical: "qaa/economics-2023/4.4.b5", excellent: "qaa/economics-2023/4.5.b5", basis: "inferred", domain: "subject-skill", award: "bachelor's with honours" }
  - { outcome: "the contexts of economic analysis", threshold: "qaa/economics-2023/4.3.b6", typical: "qaa/economics-2023/4.4.b6", excellent: "qaa/economics-2023/4.5.b6", basis: "inferred", domain: "knowledge", award: "bachelor's with honours" }
  - { outcome: "specialised areas and research", threshold: "qaa/economics-2023/4.3.b7", typical: "qaa/economics-2023/4.4.b7", excellent: "qaa/economics-2023/4.5.b7", basis: "inferred", domain: "knowledge", award: "bachelor's with honours" }
  - { outcome: "alternative approaches and their limits", threshold: "qaa/economics-2023/4.3.b8", typical: "qaa/economics-2023/4.4.b8", excellent: "qaa/economics-2023/4.5.b8", basis: "inferred", domain: "understanding", award: "bachelor's with honours" }
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
- { body: "professional, statutory and regulatory bodies (PSRBs), none named", says: "the statement supports PSRBs with the academic standards expected (front matter); courses with professional or vocational outcomes may need their evaluation and accreditation, by site visit and desk review (D1, 2.12)", requirements: "not-applicable-by-design: no body is named (Part E)" }
- { body: "Royal Economic Society", says: "a partner with providers in widening-participation work, which also lets current students work with it (D1, 2.8)", requirements: "not-applicable-by-design: named as a partner, not as an accrediting body (Part E)" }
```

### SB6 Cross-cutting references
<!-- label: both; status: drafted; basis: primary -->
```yaml
themes:
  - { id: "theme:edi", named: "Equality, diversity and inclusion (EDI)", carriedIn: ["1.7", "1.8", "1.9", "1.11", "1.12", "2.7", "2.8", "3.10", "3.11"], statements: ["qaa/economics-2023/1.7"] }
  - { id: "theme:accessibility", named: "Accessibility (front matter: accessibility and the needs of disabled students)", carriedIn: ["1.7", "1.10", "1.11", "1.12", "1.13", "1.14", "3.11"], statements: ["qaa/economics-2023/1.10", "qaa/economics-2023/1.13"] }
  - { id: "theme:esd", named: "Sustainability (front matter: education for sustainable development)", carriedIn: ["1.2", "1.3", "1.5", "1.15", "1.16", "1.17", "1.18", "1.19", "3.2"], statements: ["qaa/economics-2023/1.16"] }
  - { id: "theme:enterprise", named: "Enterprise and entrepreneurship education (EED) (front matter: employability, entrepreneurship and enterprise education)", carriedIn: ["1.20", "1.21", "1.22", "1.23", "1.24", "1.25", "1.26", "2.7", "3.7"], statements: [] }
frameworks:
  - { framework: "fheq", levels: ["fheq:6"], citedIn: ["2.3", "4.2"] }
  - { framework: "scqf", levels: ["fqheis:10"], citedIn: ["2.3", "4.2"] }
bodies:
  - { body: "professional, statutory and regulatory bodies (unnamed)", citedIn: ["front matter", "2.12"] }
  - { body: "Royal Economic Society", citedIn: ["2.8"] }
sharedDocuments:
  - { document: "std:doc:qaa-fheq-2024-framework, Annex D", named: "Annex D: Outcome classification descriptions for FHEQ Level 6 and FQHEIS Level 10 degrees", citedIn: ["4.2"], role: "descriptions of the four honours classes (1st, 2.1, 2.2, 3rd), to which providers should refer when evidencing achievement above threshold" }
  - { document: "std:doc:qaa-advancehe-esd-2021-guidance", named: "Education for Sustainable Development Guidance produced by Advance HE and QAA (March 2021)", citedIn: ["1.17"], role: "its learning outcomes and competencies align with the core skills of 1.6" }
  - { document: "QAA Quality Code, Advice and Guidance (not yet ingested)", named: "Advice and Guidance to support the Quality Code", citedIn: ["front matter"], role: "course design, teaching, external expertise, monitoring" }
  - { document: "QAA Glossary (not ingested)", named: "QAA's Glossary", citedIn: ["front matter"], role: "explains unfamiliar terms" }
  - { document: "UN Sustainable Development Goals (external)", named: "UN Sustainable Development Goals (SDGs)", citedIn: ["1.15", "1.16", "1.17"], role: "frame of the sustainability theme; SDGs 8, 9, 10 and 12 named" }
  - { document: "UN Global Compact (external)", named: "UN Global Compact", citedIn: ["1.15"], role: "standard-setting in human rights, labour, environment and anti-corruption, reflected in the discipline" }
  - { document: "Equality Act 2010 (law)", named: "the Equality Act 2010", citedIn: ["1.7"], role: "protected characteristics, as a floor that inclusion goes beyond" }
  - { document: "Jisc (2020) Steps to improve your institution's digital accessibility (external)", named: "Steps to improve your institution’s digital accessibility", citedIn: ["1.14"], role: "example of digital accessibility guidance" }
  - { document: "The Open University (2022) Accessibility Statement (external)", named: "accessibility statements such as that produced by The Open University", citedIn: ["1.14"], role: "example of a provider accessibility statement" }
```

## Part B Terminology
<!-- The statement has no glossary of its own unless Part E says so; these are terms it defines in its text. -->

### B1 Concepts
<!-- label: both; status: drafted; basis: primary -->
```yaml
- { slug: "sustainability", definition: "present and future states, backed by strategies and operations aimed at social goals, centred on preserving resources, upholding human rights and fair labour relations, and reaching equitable welfare (D1, 1.15)", beneficiaryDefinition: "meeting needs now and later while protecting resources, rights and fairness", scopeNote: "the statement says it goes beyond climate change", category: "unknown", practices: ["education"] }
- { slug: "enterprise-and-entrepreneurship-education", definition: "education that builds behaviours, attributes and competencies likely to support successful careers and readiness for change, often through placements and external links (D1, 1.20)", beneficiaryDefinition: "learning that prepares you to create opportunities and adapt at work", scopeNote: "abbreviated EED; front matter groups it with employability", category: "unknown", practices: ["education"] }
- { slug: "authentic-assessment", definition: "assessment whose tasks mirror activities in the wider world, workplaces included, used for applied skills (D1, 3.14)", beneficiaryDefinition: "tasks like the ones economists do at work", scopeNote: "research projects and data-based tasks are the examples", category: "unknown", practices: ["education"] }
- { slug: "monitoring-and-evaluation", definition: "periodic assessment of a course, internal or external, drawing on current and past monitoring to understand achievement or plan the course (D1, 2.9)", scopeNote: "students should take part (2.9)", category: "unknown", practices: ["education"] }
- { slug: "threshold-standard", definition: "the minimum standard of achievement for the award, which most students exceed (D1, 4.2, 4.3)", scopeNote: "with typical and excellent above it (4.4, 4.5)", category: "unknown", practices: ["education"] }
```

### B2a Terms as the issuer defines them
<!-- label: source; status: drafted; basis: primary -->
```yaml
- { concept: "sustainability", form: "sustainability", lang: "en", partOfSpeech: "noun", termStatus: "preferred", register: "formal" }
- { concept: "enterprise-and-entrepreneurship-education", form: "enterprise and entrepreneurship education", lang: "en", partOfSpeech: "noun-phrase", termStatus: "preferred", register: "formal" }
- { concept: "enterprise-and-entrepreneurship-education", form: "EED", lang: "en", partOfSpeech: "noun", termStatus: "admitted", register: "formal" }
- { concept: "authentic-assessment", form: "authentic assessment", lang: "en", partOfSpeech: "noun-phrase", termStatus: "preferred", register: "formal" }
- { concept: "monitoring-and-evaluation", form: "monitoring and evaluation", lang: "en", partOfSpeech: "noun-phrase", termStatus: "preferred", register: "formal" }
- { concept: "threshold-standard", form: "threshold level", lang: "en", partOfSpeech: "noun-phrase", termStatus: "preferred", register: "formal" }
- { concept: "threshold-standard", form: "minimum threshold standards", lang: "en", partOfSpeech: "noun-phrase", termStatus: "admitted", register: "formal" }
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
  title: "Subject Benchmark Statement Economics"
  edition: "March 2023 (fifth edition)"
  year: 2023
  url: unknown (the QAA page; the text came by stan's extraction)
  retrieved: "held from stan: wkspc2615-QAAVector mapped/economics-2023/economics-2023.raw.txt, commit 366bcb99a01118f2c4c3ebfa2a8337596bddc455; received 2026-10-03"
  licence: QAA copyright
  tier: primary
  readVia: direct
  held: 058755dbafe46dd0062991296954510fefece33e153e98a9184ae8fd98b6f062
  heldFiles: ["wkspc2601-library/txt/qaa-2023-economics-subject-benchmark-statement-standard.txt", "wkspc2601-library/txt/qaa-2023-economics-subject-benchmark-statement-standard.norm.txt", "wkspc2601-library/records/qaa-2023-economics-subject-benchmark-statement-standard.chunks.json", "wkspc2601-library/records/qaa-2023-economics-subject-benchmark-statement-standard.held.json"]
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
- SB4, rungs: three rung lists of eight items each (4.3 threshold, 4.4 typical, 4.5 excellent) with lead-ins in 'should have demonstrated' (Psychology's are in 'will'); 4.5 adds 'consistently'. Threshold items take force `threshold` because 4.2 calls the threshold the minimum; typical and excellent items take the lead-in's `should` (forceFrom 4.4, 4.5).
- SB4, gradeOf: unlike Psychology, the three lists run plainly in parallel item by item (concepts; theories; methods; data; policy; contexts; specialised areas; approaches), differing in qualifiers (key, systematic, excellent, advanced). All 16 links (4.4.b1 to b8 to 4.3.b1 to b8; 4.5.b1 to b8 to 4.4.b1 to b8) are inferred: the issuer does not pair them. 4.1 says typical implies threshold. For Abbott at P3: whether the parallel wording makes them `stated`.
- SB4, domains: the rung items are noun phrases completing the lead-in's 'demonstrated', so many records carry no verb of their own (verbs: []); none of the 24 is a generic skill. The method items (b3) mix understanding (threshold) with proficiency (typical, excellent); kept as subject-skill across the rungs so the gradeOf links share a domain.
- S3, std-prep: the skeleton marked 2.2's eight items as the typical rung because the lead-in says 'The typical Economics course'; they are an outcome list of the usual course design, not a rung (SB4 outcomeLists). Lesson for the script: 'typical' qualifying a course is not a rung lead-in.
- S3, std-prep: five spans ran on into the next sub-heading (1.6.b6 'Equality, diversity and inclusion (EDI)', 2.2.b8 'Progression', 4.2 'Threshold level', 4.3.b8 'Typical level', 4.4.b8 'Excellent level'); each was cut back with `find`. The theme candidate hits 1.6 (edi), 1.9 (accessibility), 1.14 (esd) and 1.19 (enterprise) came from the same spill-over and were dropped from SB6 where the paragraph does not otherwise carry the theme.
- S4, outcome lists with no listed modal: 1.6 ('Economists need the ability to:'; 'need' outside the five, recorded as describes, forceFrom 1.6) and 2.2 ('The typical Economics course is designed to achieve the following learning outcomes'; plain present, recorded as describes). Taken as statements because they are outcome lists and 1.17 calls 1.6 'the core skills provided by all Economics courses'. For Abbott at P3: keep as statements, and with what force?
- S4, force outside the five, recorded as describes: 'the expectation is that' (2.2, provider support where maths is not required on entry); 'need to' (3.10, course leaders' support for language, mathematics and study skills). For Abbott: should these read as should?
- S4, 'requires' read as must (brief 0.2.2): 1.3 ('Studying economics requires an understanding ...'; 'required at both the individual (micro) and the aggregate (macro) level') and 1.16 ('they require students to foster critical and creative capacities'). Not taken as statements despite the word: 2.1 ('a core of required modules' describes most courses), 2.2 ('may or may not require a mathematics qualification for admission'), 2.3 (postgraduate entry 'may require specified levels'), 2.12 ('may also require evaluation and accreditation': conditional, about PSRBs) and the front matter's 'regulatory requirements'.
- S4, not taken (predictive or descriptive 'will', or plain present): 2.3 ('will typically progress'; 'it is expected that each level would see' attainment building to the threshold skills: 'expected' outside the five); 2.11 (external examiners 'will be asked'); 1.22 and 1.23 (graduates 'are familiar' with software, 'are trained' in communicating); 4.1 (minor-subject students 'are not expected to attain all of these benchmarks').
- S4, plain-present provider norms (template open point 5), not statements: 3.2's key concepts 'most Economics courses cover' (seven of eight items; only 3.2.b5, with 'should', is a statement), 3.5's applied fields (may cover), 3.6, 3.7 ('is designed to encourage'), 3.12 to 3.15 on assessment.
- S4, 1.7: the obliging sentence (educators 'should aim to foster an inclusive learning community') is the statement; its five bullets are examples ('such efforts might include') and are not statements. The paragraph says 'Economics educators': the provider-facing word, kept in our versions as teachers and staff.
- S4, 1.13: the issuer's text reads 'Economics pay attention' (a grammatical slip, kept in source); the statement is cut at the first sentence ('should include ... image descriptions'); the rest of the paragraph ('needs to be suitable', 'needs consideration') is summarised in the paraphrase, 'needs to' being outside the five.
- S4, 4.2 holds two forces: a prediction ('will perform significantly better than the minimum threshold standards') and the provider's 'should refer to Annex D'; recorded as should, addressee provider.
- S1, front matter: the issuer's template placeholder '[SUBJECT]' is left unfilled in 'About this Statement' ('a QAA Subject Benchmark Statement for [SUBJECT]'); kept in the held text.
- S2, awards: honours only (FHEQ 6, FQHEIS 10, stated in 2.3 and 4.2); exit awards (CertHE, DipHE, Pass degree) are mentioned in 2.5 but given no standards. No master's level.
- Front matter subjects, inferred: hecos 100452 international economics (from 3.5's international macroeconomics and finance, and international trade and migration) and hecos 100601 economic policy (from 3.5's political economy, a non-preferred term of 100601, and 1.2's policy aim). For P3. CAH15 social sciences is taken as stated from 1.4 ('Economics is a social science'). Specialisms with no HECoS term of their own (behavioural, development, environmental, experimental, health, labour, monetary, public economics; growth; industrial organisation) are listed without codes.
- SB5: no professional, statutory or regulatory body is named; PSRBs appear only in general (front matter, 2.12). The Royal Economic Society (2.8) is a widening-participation partner, not an accreditor. Other organisations named, not bodies in SB5's sense: the Bank of England and economic consultancies as degree-apprenticeship and placement partners (2.7); the Economics Network, the Centre for Teaching and Learning Economics and Advance HE as teaching resources (3.9; section 5); Jisc and The Open University as accessibility examples (1.14); the United Nations (1.15 to 1.17).
- SB6, frameworks: FHEQ level 6 and FQHEIS level 10 cited in 2.3 and 4.2; CQFW not cited. The front matter also names the OfS regulatory framework (England), the Quality Assessment Framework for Wales and the Quality Enhancement Framework (Scotland): regulatory arrangements, excluded front matter, not qualification frameworks.
- SB6, themes: EDI is also carried by 1.11 (curricula a diverse community can see itself in) and 1.12 (diverse and inclusive teaching), both under the Accessibility heading; accessibility by 1.7's bullet on neurodiverse access; esd by 1.5 (the climate crisis among contemporary problems) and 3.2 (planetary crises, environmental degradation, sustainability as an evaluative criterion); enterprise by 2.7 (an employability angle) and 3.7 (learning organised to support employability). Generative AI is not treated (1.4 names Data Science and Artificial Intelligence only as linked subjects).
- SB6, sharedDocuments: Annex D is cited by name without a year (4.2); resolved to the ingested FHEQ 2024 document, Annex D. The ESD guidance (1.17) resolves to std:doc:qaa-advancehe-esd-2021-guidance.
- Patterns that differ from Psychology: rung lead-ins in 'should have demonstrated' rather than 'will'; eight parallel items per rung; no master's or conversion award; no named PSRB; an outcome list in 'need' (1.6) and one with no modal (2.2); 'Economics educators' named in the text; sub-headings run on to the end of the preceding paragraph in the held text; section 4 has no separate list of subject-specific and generic skills, so generic skills appear only in 1.6.b4, 2.2.b8 and 1.16.
- Levels: all learner statements at fheq:6, honours, read from 2.3 (FHEQ Level 6; FQHEIS Level 10) and checked against std:doc:qaa-fheq-2024-framework S5 and SL1 (4.15) and std:doc:qaa-fqheis-2024-framework (4.16); spine:6 from std:ref:uk-framework R2 and R8. The FHEQ descriptor and Annex D cells each aaw names (4.15.b1 to b9.3; annex-d/<strand>/<row>/3rd and /1st) are our pointing, inferred.
- S7, supersedes: the text names the fourth edition (2019) and says the 2023 statement revises it; its id std:doc:qaa-economics-2019-benchmarks is ours and not yet ingested.
- S1, licence: the text gives a copyright notice and no re-use terms; QAA's terms for holding and chunking are to check (template open point 3).
- S9: not researched in P1.
- ST-12: versions here run to the lengths the content needs; no length range is yet set.

---

## Change notes
- 0.1.2, 3 October 2026, 21:02: moved with its held text from UNI to the source library repo (`wkspc2601-library/ingested/standards/`, texts in `txt/`, records in `records/`); paths only (Abbott, 20:56; std N-0119).
- 0.1.1, 3 October 2026, 20:20: obliging words outside the five read as must, "ought to" as should, on statements outside the rungs, each marked on its force line (Abbott, 20:17; D-std-0016).
- 0.1.0, 2026-10-03 17:10: researched by run frame 0.1.1-draft and standards run layer 0.7.0-draft, std, run 0102 (P1); built by tools/bm_build.py.
