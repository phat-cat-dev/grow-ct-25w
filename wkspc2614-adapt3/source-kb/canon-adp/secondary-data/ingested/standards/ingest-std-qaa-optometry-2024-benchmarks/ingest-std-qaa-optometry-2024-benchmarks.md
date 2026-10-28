---
id: std:doc:qaa-optometry-2024-benchmarks
title: "Subject Benchmark Statement Optometry"
profile: standards/subject-benchmark
profileVersion: 0.2.0-draft
issuer: QAA
kind: subject-benchmark
jurisdiction: [UK]
subjectScope: subjects
subjects:
  - { scheme: "hecos", code: "100036", label: "optometry", basis: "stated" }
  - { scheme: "cah", code: "CAH02-06-03", label: "ophthalmics", basis: "stated" }
  - { scheme: "cah", code: "CAH02-06", label: "allied health", basis: "stated" }
  - { scheme: "cah", code: "CAH02", label: "subjects allied to medicine", basis: "stated" }
edition: "April 2024 (fifth edition)"
published: 2024-04
status: current
supersedes: "Subject Benchmark Statement for Optometry (2019), fourth edition, for the BSc: subsumed in this statement and still available separately (D1, front matter)"
heldText: { method: sha256-bytes, raw: 5ea3d94e6e3a6d13a3a2cca225a389ee954654efe4d0a608326d3b1c43735911, normalised: 2475a7271559e6274991acdc66323eeb504e2d100b3e160b6b34c5e1ff77a0af }
heldTextStan: { method: sha256-stan, raw: 5ea3d94e6e3a6d13a3a2cca225a389ee954654efe4d0a608326d3b1c43735911, normalised: 8b6a82555538c0fd4ca581b38279a8471508ae12eedd1d2c345585f7d66a4a20 }
licence: "QAA copyright; held for study, private to the project, never published"
series: "QAA Subject Benchmark Statements, fifth edition with cross-cutting themes (April 2024)"
awardsCovered: ["integrated master's"]
levelsCovered: ["fheq:7", "fqheis:11"]
nations: ["England", "Wales", "Scotland", "Northern Ireland"]
parts:
  S: full
  B: "partial: no glossary in the document (it points to QAA's Glossary); terms it defines in passing"
  C: "not-applicable: the document sets expectations, not a procedure"
pins: { structure: 0.13.0-draft, template: 0.8.0-draft, benchmarkTemplate: 0.6.0-draft, runFrame: 0.1.1-draft, runLayer: 0.7.0-draft, standards: none yet, terminology: none yet }
lifecycle: drafted
researchedBy: run frame 0.1.1-draft; standards run layer 0.7.0-draft; std, run 0122 (tools/bm_build.py)
passes:
  P1: "2026-10-03 18:02"
  P2: "skipped: read direct from the held text; inferred codes and rung links are for P3"
  P3: open
version: 0.1.2
---

<!-- from INGEST wpk-0016-ingest-pd-template-standards.md 0.8.0-draft and wpk-0016-ingest-pd-template-standards-benchmark.md 0.6.0-draft; built by tools/bm_build.py from run-src/ -->
# Subject Benchmark Statement: Optometry (QAA, April 2024)

> Run 0122, P1 by std. The issuer's words are held in the source library, `wkspc2601-library/txt/qaa-2024-optometry-subject-benchmark-statement-standard.norm.txt`; each S4 record carries its statement in full (`source`) for language analysis, with its span. Paraphrases and versions are ours. Private to the project, never published. In front matter `status` is the issuer's; ours is `lifecycle`. Doubts are in Part E.

## Part 0 Summary

### 0.1 Agent definition
<!-- label: editorial; status: drafted; basis: primary -->
QAA's UK reference point for what a graduate of the registrable integrated master's in Optometry (FHEQ Level 7; FQHEIS Level 11) can know, do and understand at the threshold: a summary of the General Optical Council's seven outcome categories and sixteen generic skills. Reach for it when designing, reviewing or describing an Optometry course that leads to registration. It is not the GOC's own requirements, not a curriculum and not a regulatory requirement in England; it does not cover non-registrable vision science awards.

### 0.2 Summary
<!-- label: both; status: drafted; basis: primary -->
Published by QAA in April 2024 as the fifth edition, the statement covers only the integrated master's that lets graduates register with the General Optical Council, replacing the BSc route whose 2019 statement it subsumes. It describes the profession and the purposes of the degree, the course's distinctive features (placements, progression, flexibility, partnership, review), its content, teaching and assessment, and benchmark standards at one rung only, the threshold: the GOC's seven outcome categories summarised (4.4) and sixteen generic skills (4.5). It carries the four cross-cutting themes (equality, diversity and inclusion; accessibility; education for sustainable development; employability, enterprise and entrepreneurship), points to Annex D of the Frameworks for providers' evidence of achievement, and sets the subject beside its statutory regulator, the GOC, whose registration students must hold by law.

## Part S Standard

### S1 Identity
<!-- label: source; status: drafted; basis: primary -->
```yaml
issuer: The Quality Assurance Agency for Higher Education
title: "Subject Benchmark Statement Optometry"
edition: "April 2024 (fifth edition)"
dates:
  published: 2024-04
  other: []
kind: subject-benchmark
jurisdiction: [UK]
authority: "reference: a sector reference point, not a regulatory requirement; in England not a sector-recognised standard under the OfS framework; a key reference point in Wales and Scotland; part of the quality requirements in Northern Ireland (D1, front matter: Relationship to legislation)"
licence: "QAA copyright; the document gives no re-use terms in its text (D1, front matter)"
copyrightNotice: { text: "© The Quality Assurance Agency for Higher Education 2024", locator: "D1, index" }
```

### S2 Purpose and scope
<!-- label: source; status: drafted; basis: primary -->
```yaml
governs: "what a graduate of a registrable Optometry integrated master's is expected to know, do and understand at the threshold, and the nature of such courses"
appliesTo:
  awards: ["integrated master's"]
  levels: ["fheq:7", "fqheis:11"]
  providers: ["UK higher education providers"]
whoMustUse: "none-stated; it is a reference point, not a requirement (D1, front matter)"
howUsed: ["design", "approval", "review", "other: external examining; PSRBs; information for prospective students and employers"]
doesNot: "it does not prescribe teaching, learning or assessment, interpret legislation or carry statutory or regulatory requirements; it does not apply to non-registrable optometric and vision sciences qualifications (D1, front matter)"
beneficiary: the student
statedScope: "\"This Subject Benchmark Statement is only intended to address integrated master's degree qualifications that enable graduates to register as a practising optometrist.\" (D1, front matter: Relationship to legislation)"
statedSubjects:
  - { name: "Optometry", locator: "(D1, title; front matter; 2.8)", kind: "subject", codes: [{ scheme: "hecos", code: "100036", label: "optometry" }, { scheme: "cah", code: "CAH02-06-03", label: "ophthalmics" }] }
subjects: see front matter (subjectScope subjects)
```

### S3 Structure
<!-- label: both; status: drafted; basis: primary -->
```yaml
components:
  - { number: "1.1", order: 3, componentType: paragraph, parent: "section 1", heading: "Context", gloss: "what the discipline joins and who optometrists are" }
  - { number: "1.2", order: 4, componentType: paragraph, parent: "section 1", heading: "Context", gloss: "where graduates work, from community practice to hospitals and industry" }
  - { number: "1.3", order: 5, componentType: paragraph, parent: "section 1", heading: "Context", gloss: "functions reserved by law and the route to therapeutic prescribing" }
  - { number: "1.4", order: 6, componentType: stem, parent: "section 1", heading: "Purposes of an Optometry degree", gloss: "the aims of the degree in three groups: professionals, patients, the profession" }
  - { number: "1.5", order: 7, componentType: paragraph, parent: "section 1", heading: "Characteristics of an Optometry degree", gloss: "each provider sets its own course within accreditation" }
  - { number: "1.6", order: 8, componentType: paragraph, parent: "section 1", heading: "Characteristics of an Optometry degree", gloss: "clinical skills built on scientific knowledge" }
  - { number: "1.7", order: 9, componentType: paragraph, parent: "section 1", heading: "Characteristics of an Optometry degree", gloss: "a spiral curriculum towards complex patients and autonomy" }
  - { number: "1.8", order: 10, componentType: paragraph, parent: "section 1", heading: "Characteristics of an Optometry degree", gloss: "specialist qualifications that may be built into the degree" }
  - { number: "1.9", order: 11, componentType: paragraph, parent: "section 1", heading: "Equality, diversity and inclusion", gloss: "equality and inclusion across the statement and the shared duty to promote them" }
  - { number: "1.10", order: 12, componentType: paragraph, parent: "section 1", heading: "Equality, diversity and inclusion", gloss: "evidence-based yet personalised, patient-centred care" }
  - { number: "1.11", order: 13, componentType: paragraph, parent: "section 1", heading: "Equality, diversity and inclusion", gloss: "diverse contributors in the curriculum and room to follow personal interests" }
  - { number: "1.12", order: 14, componentType: paragraph, parent: "section 1", heading: "Equality, diversity and inclusion", gloss: "weighing the effects of innovation and reflecting on practice" }
  - { number: "1.13", order: 15, componentType: paragraph, parent: "section 1", heading: "Equality, diversity and inclusion", gloss: "a wide range of patients met in the curriculum" }
  - { number: "1.14", order: 16, componentType: paragraph, parent: "section 1", heading: "Accessibility", gloss: "accessible learning and assessment within patient safety and regulator standards" }
  - { number: "1.15", order: 17, componentType: paragraph, parent: "section 1", heading: "Accessibility", gloss: "varied learning and assessment for access and a diverse student body" }
  - { number: "1.16", order: 18, componentType: paragraph, parent: "section 1", heading: "Accessibility", gloss: "accessible course design without risk to patients" }
  - { number: "1.17", order: 19, componentType: paragraph, parent: "section 1", heading: "Education for sustainable development", gloss: "sustainability, the global goals and visual health" }
  - { number: "1.18", order: 20, componentType: paragraph, parent: "section 1", heading: "Employability, enterprise and entrepreneurship", gloss: "preparing students for working life inside and beyond clinical practice" }
  - { number: "1.19", order: 21, componentType: paragraph, parent: "section 1", heading: "Employability, enterprise and entrepreneurship", gloss: "enterprise education given commercial practice ownership" }
  - { number: "1.20", order: 22, componentType: paragraph, parent: "section 1", heading: "Employability, enterprise and entrepreneurship", gloss: "what enterprise means in the subject" }
  - { number: "1.21", order: 23, componentType: paragraph, parent: "section 1", heading: "Employability, enterprise and entrepreneurship", gloss: "what entrepreneurship means and its value beyond commerce" }
  - { number: "1.22", order: 24, componentType: paragraph, parent: "section 1", heading: "Employability, enterprise and entrepreneurship", gloss: "topics that enterprise education may cover" }
  - { number: "2.1", order: 26, componentType: paragraph, parent: "section 2", heading: "Design", gloss: "entry routes and foundation courses" }
  - { number: "2.2", order: 27, componentType: paragraph, parent: "section 2", heading: "Design", gloss: "extended learning in practice that the regulator requires" }
  - { number: "2.3", order: 28, componentType: paragraph, parent: "section 2", heading: "Design", gloss: "supervised practice building readiness for registration" }
  - { number: "2.4", order: 29, componentType: paragraph, parent: "section 2", heading: "Design", gloss: "from campus clinics to distant placements" }
  - { number: "2.5", order: 30, componentType: paragraph, parent: "section 2", heading: "Design", gloss: "the regulator's seven categories taught through a spiral curriculum" }
  - { number: "2.6", order: 31, componentType: paragraph, parent: "section 2", heading: "Design", gloss: "extra professional qualifications at or near graduation" }
  - { number: "2.7", order: 32, componentType: paragraph, parent: "section 2", heading: "Progression", gloss: "progression through levels towards the threshold skills" }
  - { number: "2.8", order: 33, componentType: paragraph, parent: "section 2", heading: "Progression", gloss: "single-subject study with room for interdisciplinary work" }
  - { number: "2.9", order: 34, componentType: paragraph, parent: "section 2", heading: "Progression", gloss: "course design on Miller's pyramid" }
  - { number: "2.10", order: 35, componentType: stem, parent: "section 2", heading: "Progression", gloss: "progressive learning supported by four kinds of strategy" }
  - { number: "2.11", order: 36, componentType: paragraph, parent: "section 2", heading: "Progression", gloss: "progression rules, resits and exit awards that do not register" }
  - { number: "2.12", order: 37, componentType: paragraph, parent: "section 2", heading: "Flexibility", gloss: "modes and patterns of study" }
  - { number: "2.13", order: 38, componentType: paragraph, parent: "section 2", heading: "Flexibility", gloss: "diverse delivery fitted to learner and material" }
  - { number: "2.14", order: 39, componentType: paragraph, parent: "section 2", heading: "Flexibility", gloss: "practical, reflective sessions in real and simulated settings" }
  - { number: "2.15", order: 40, componentType: paragraph, parent: "section 2", heading: "Flexibility", gloss: "courses able to change and to withstand disruption" }
  - { number: "2.16", order: 41, componentType: paragraph, parent: "section 2", heading: "Flexibility", gloss: "courses able to respond to new technology and AI" }
  - { number: "2.17", order: 42, componentType: paragraph, parent: "section 2", heading: "Partnership", gloss: "partnerships with placement hosts and their oversight" }
  - { number: "2.18", order: 43, componentType: paragraph, parent: "section 2", heading: "Partnership", gloss: "work-based practice and an employability strategy" }
  - { number: "2.19", order: 44, componentType: paragraph, parent: "section 2", heading: "Partnership", gloss: "student societies and learned bodies" }
  - { number: "2.20", order: 45, componentType: paragraph, parent: "section 2", heading: "Partnership", gloss: "students as partners and the student voice" }
  - { number: "2.21", order: 46, componentType: paragraph, parent: "section 2", heading: "Partnership", gloss: "patients as partners in course design and review" }
  - { number: "2.22", order: 47, componentType: paragraph, parent: "section 2", heading: "Monitoring and review", gloss: "course monitoring and periodic review" }
  - { number: "2.23", order: 48, componentType: paragraph, parent: "section 2", heading: "Monitoring and review", gloss: "external reviewers in periodic review" }
  - { number: "2.24", order: 49, componentType: paragraph, parent: "section 2", heading: "Monitoring and review", gloss: "whose feedback review draws on, and embedding ESD and EDI" }
  - { number: "2.25", order: 50, componentType: paragraph, parent: "section 2", heading: "Monitoring and review", gloss: "the external examiner system" }
  - { number: "2.26", order: 51, componentType: paragraph, parent: "section 2", heading: "Monitoring and review", gloss: "ongoing evaluation and who takes part in improving courses" }
  - { number: "2.27", order: 52, componentType: paragraph, parent: "section 2", heading: "Monitoring and review", gloss: "evaluation and accreditation by professional and regulatory bodies" }
  - { number: "3.1", order: 54, componentType: stem, parent: "section 3", heading: "Content", gloss: "three topic areas and the key skills courses build" }
  - { number: "3.2", order: 55, componentType: area, parent: "section 3", heading: "Content", gloss: "the scientific and theoretical content" }
  - { number: "3.3", order: 56, componentType: area, parent: "section 3", heading: "Content", gloss: "the clinical content" }
  - { number: "3.4", order: 57, componentType: area, parent: "section 3", heading: "Content", gloss: "the regulator's outcomes under seven categories" }
  - { number: "3.5", order: 58, componentType: stem, parent: "section 3", heading: "Content", gloss: "the regulator's outcomes for registration as abilities" }
  - { number: "3.6", order: 59, componentType: practice, parent: "section 3", heading: "Teaching and learning", gloss: "teaching for registered practice, not prescribed in method" }
  - { number: "3.7", order: 60, componentType: paragraph, parent: "section 3", heading: "Teaching and learning", gloss: "from structured towards self-directed learning" }
  - { number: "3.8", order: 61, componentType: paragraph, parent: "section 3", heading: "Teaching and learning", gloss: "teaching that keeps pace, and staff development" }
  - { number: "3.9", order: 62, componentType: practice, parent: "section 3", heading: "Teaching and learning", gloss: "student-centred delivery across modes and settings" }
  - { number: "3.10", order: 63, componentType: practice, parent: "section 3", heading: "Teaching and learning", gloss: "the range of learning activities" }
  - { number: "3.11", order: 64, componentType: paragraph, parent: "section 3", heading: "Teaching and learning", gloss: "equal access through inclusive design and adjustments" }
  - { number: "3.12", order: 65, componentType: practice, parent: "section 3", heading: "Assessment", gloss: "aligned, authentic assessment of all regulator outcomes" }
  - { number: "3.13", order: 66, componentType: stem, parent: "section 3", heading: "Assessment", gloss: "six qualities assessment balances" }
  - { number: "3.14", order: 67, componentType: stem, parent: "section 3", heading: "Assessment", gloss: "three properties assessment has" }
  - { number: "3.15", order: 68, componentType: paragraph, parent: "section 3", heading: "Assessment", gloss: "evidence-based assessment, standard setting and moderation" }
  - { number: "3.16", order: 69, componentType: practice, parent: "section 3", heading: "Assessment", gloss: "assessment matched to the layers of Miller's pyramid" }
  - { number: "3.17", order: 70, componentType: practice, parent: "section 3", heading: "Assessment", gloss: "written and practical kinds of assessment evidence" }
  - { number: "3.18", order: 71, componentType: paragraph, parent: "section 3", heading: "Assessment", gloss: "unfamiliar problems and research skills at master's level" }
  - { number: "3.19", order: 72, componentType: practice, parent: "section 3", heading: "Feedback and feedforward", gloss: "qualities of feedback and feedforward" }
  - { number: "3.20", order: 73, componentType: paragraph, parent: "section 3", heading: "Feedback and feedforward", gloss: "what feedback does for learners" }
  - { number: "3.21", order: 74, componentType: paragraph, parent: "section 3", heading: "Feedback and feedforward", gloss: "feedforward, evaluative skill and psychological safety" }
  - { number: "4.1", order: 76, componentType: paragraph, parent: "section 4", heading: "Introduction", gloss: "the standards as the threshold for the master's" }
  - { number: "4.2", order: 77, componentType: paragraph, parent: "section 4", heading: "Introduction", gloss: "providers judge evidence of achievement with Annex D" }
  - { number: "4.3", order: 78, componentType: paragraph, parent: "section 4", heading: "Threshold level: subject knowledge, understanding and skills", gloss: "the threshold standard for entry to a regulated profession" }
  - { number: "4.4", order: 79, componentType: paragraph, parent: "section 4", heading: "Threshold level: subject knowledge, understanding and skills", gloss: "threshold summaries of the regulator's seven outcome categories" }
  - { number: "4.5", order: 80, componentType: stem, parent: "section 4", heading: "Threshold level: generic skills", gloss: "sixteen generic skills on graduating" }
  - { number: "1", componentType: section, parent: none, heading: "Context and purposes of an Optometry degree", gloss: "section 1" }
  - { number: "2", componentType: section, parent: none, heading: "Distinctive features of an Optometry degree", gloss: "section 2" }
  - { number: "3", componentType: section, parent: none, heading: "Content, structure and delivery", gloss: "section 3" }
  - { number: "4", componentType: section, parent: none, heading: "Benchmark standards", gloss: "section 4" }
excluded:
  - { number: "none", heading: "About this Statement; How can I use this document?; Relationship to legislation; Additional sector reference points", kind: "other: front matter, read for S1, S2, S5, S8, SB5 and SB6; its obligations (GOC registration by law) are in SB5 and Part E" }
  - { number: "1, 2, 3, 4 (heading lines)", heading: "section heading lines", kind: "other: headings, recorded in S3 as sections" }
  - { number: "5", heading: "List of references and further resources", kind: "other: reference list, read for SB6 and Part E" }
  - { number: "6", heading: "Membership of the Advisory Group", kind: "other: names, out of scope" }
```

### S4 Statements
<!-- label: both; status: drafted; basis: primary. Only standards (D-std-0002 (a)): 82 records. `source` is the issuer's statement exactly as its span holds it (D-std-0014). -->
```yaml
- id: qaa/optometry-2024/1.7
  locator: { number: "1.7", headingPath: ["Context and purposes of an Optometry degree", "Characteristics of an Optometry degree"] }
  span: { start: 15837, end: 16256 }
  source: "1.7 During a course, students will develop the capability to manage increasingly complex patients, typically through a spiral approach to curriculum construction. As a consequence, early parts of the course will typically include significant theoretical learning accompanied by clinical experiences delivered through observation and simulation. The level of complexity and learner autonomy is thus developed over time.\n"
  stem: none
  statementType: expectation
  rung: none
  force: will
  level: fheq:7
  appliesTo: "students of the subject"
  addressee: learner
  verbs: ["develop"]
  about: "growing capability with complex patients"
  themes: [none]
  domain: subject-skill
  award: ["integrated master's"]
  gradeOf: none
  paraphrase: "Students will gain the ability to care for patients of rising complexity, usually through a spiral curriculum that starts with theory, observation and simulation and adds complexity and autonomy over time."
  quote: full   # the issuer's statement is in `source` (D-std-0014)
  audience: both
  subjects: inherited
- id: qaa/optometry-2024/1.10
  locator: { number: "1.10", headingPath: ["Context and purposes of an Optometry degree", "Equality, diversity and inclusion"] }
  span: { start: 17273, end: 17725 }
  source: "1.10 Optometry practice relies upon accurate and objective observation. Practitioners also take responsibility for providing care that is appropriate to the needs of all patients. Accordingly, optometrists strike a balance between evidence-based decision-making and\n\n6\nthe needs of the individual receiving care. Graduates are able to navigate the need to personalise their clinical interactions to provide factually grounded but patient-centred care.\n"
  stem: none
  statementType: outcome
  rung: none
  force: will
  level: fheq:7
  appliesTo: "graduates of the subject"
  addressee: learner
  verbs: ["navigate"]
  about: "personalised care grounded in evidence"
  themes: [theme:edi]
  domain: subject-skill
  award: ["integrated master's"]
  gradeOf: none
  paraphrase: "Since practice rests on accurate, objective observation and care must suit every patient, graduates will be able to tailor each clinical encounter so that care stays both evidence-based and centred on the person."
  quote: full   # the issuer's statement is in `source` (D-std-0014)
  audience: both
  subjects: inherited
- id: qaa/optometry-2024/1.11
  locator: { number: "1.11", headingPath: ["Context and purposes of an Optometry degree", "Equality, diversity and inclusion"] }
  span: { start: 17725, end: 18243 }
  source: "1.11 Curricula should recognise the discoveries and contributions of vision scientists, and optical and other healthcare professionals with diverse backgrounds and identities and acknowledge that different cultural backgrounds may provide different insights and lead to new discoveries. Furthermore, learners should have the opportunity to explore Optometry- related topics that inspire them, and that allow them to situate their knowledge in the light of their aspirations, lived experiences or cultural backgrounds.\n"
  stem: none
  statementType: requirement
  rung: none
  force: should
  level: none
  appliesTo: "curricula in the subject"
  addressee: provider
  verbs: ["recognise", "acknowledge", "explore"]
  about: "diverse contributors and personal interests in the curriculum"
  themes: [theme:edi]
  domain: none
  award: ["integrated master's"]
  gradeOf: none
  paraphrase: "Curricula should credit the work of vision scientists and optical and healthcare professionals from varied backgrounds, accept that different cultures bring different insights, and let learners pursue topics that connect with their own aims, lives and cultures."
  quote: full   # the issuer's statement is in `source` (D-std-0014)
  audience: practitioner
  subjects: inherited
- id: qaa/optometry-2024/1.13
  locator: { number: "1.13", headingPath: ["Context and purposes of an Optometry degree", "Equality, diversity and inclusion"] }
  span: { start: 18557, end: 18712 }
  source: "1.13 Curriculum content should expose students to a range of patient experiences and presentations to enable successful care to be delivered across the UK."
  stem: none
  statementType: requirement
  rung: none
  force: should
  level: none
  appliesTo: "curriculum content"
  addressee: provider
  verbs: ["expose"]
  about: "a broad range of patient presentations"
  themes: [theme:edi]
  domain: none
  award: ["integrated master's"]
  gradeOf: none
  paraphrase: "Curriculum content should bring students into contact with a wide spread of patient experiences and presentations, so that good care can be given anywhere in the UK."
  quote: full   # the issuer's statement is in `source` (D-std-0014)
  audience: practitioner
  subjects: inherited
- id: qaa/optometry-2024/1.14
  locator: { number: "1.14", headingPath: ["Context and purposes of an Optometry degree", "Accessibility"] }
  span: { start: 18727, end: 19435 }
  source: "1.14 Equality of opportunity involves enabling access for people who have differing individual requirements, as well as eliminating arbitrary and unnecessary barriers to successful learning. In accordance with this, Optometry courses should ensure that all students are offered learning and assessment opportunities that are equally accessible to them, by means of inclusive design wherever possible and by means of reasonable individual adjustments where necessary and appropriate. It should be noted that assessment design and reasonable adjustments should always ensure that the patient is protected, and the standards of the regulator are met, while also meeting obligations under the Equality Act 2010.\n"
  stem: none
  statementType: requirement
  rung: none
  force: should
  level: none
  appliesTo: "Optometry courses"
  addressee: provider
  verbs: ["ensure"]
  about: "accessible learning and assessment within patient safety"
  themes: [theme:accessibility]
  domain: none
  award: ["integrated master's"]
  gradeOf: none
  paraphrase: "Courses should offer every student equally accessible learning and assessment, through inclusive design where possible and reasonable adjustments where needed, while patients stay protected, the regulator's standards are met and Equality Act 2010 duties are honoured."
  quote: full   # the issuer's statement is in `source` (D-std-0014)
  audience: practitioner
  subjects: inherited
- id: qaa/optometry-2024/1.15
  locator: { number: "1.15", headingPath: ["Context and purposes of an Optometry degree", "Accessibility"] }
  span: { start: 19435, end: 19851 }
  source: "1.15 Learning and assessment experiences should be diverse to both reflect the variety of the subject and to increase accessibility for all. Indeed, to face the challenges of the twenty- first century, the subject needs as diverse a body of students as possible to contribute new ideas and innovations, drawn from the different insights and perspectives from all learners, regardless of disability or circumstances.\n"
  stem: none
  statementType: requirement
  rung: none
  force: should
  level: none
  appliesTo: "learning and assessment"
  addressee: provider
  verbs: ["reflect", "increase"]
  about: "varied learning and assessment for access"
  themes: [theme:accessibility]
  domain: none
  award: ["integrated master's"]
  gradeOf: none
  paraphrase: "Learning and assessment should be varied, to mirror the breadth of the subject and to widen access, because the field needs a student body as diverse as possible to bring in new ideas."
  quote: full   # the issuer's statement is in `source` (D-std-0014)
  audience: practitioner
  subjects: inherited
- id: qaa/optometry-2024/1.16
  locator: { number: "1.16", headingPath: ["Context and purposes of an Optometry degree", "Accessibility"] }
  span: { start: 19851, end: 20275 }
  source: "1.16 Optometry course teams should pay attention to ensuring that curricula, pedagogy, assessments and clinical elements of courses are designed to be accessible, without compromising patient safety. Learners are supported to develop an appropriate range of verbal, spatial and numerical skills alongside other transferable skills required to successfully complete their course and increase their scope of clinical practice."
  stem: none
  statementType: requirement
  rung: none
  force: should
  level: none
  appliesTo: "Optometry course teams"
  addressee: provider
  verbs: ["ensuring", "designed"]
  about: "accessible design of all course elements"
  themes: [theme:accessibility]
  domain: none
  award: ["integrated master's"]
  gradeOf: none
  paraphrase: "Course teams should see that curricula, teaching methods, assessments and clinical elements are designed to be accessible without endangering patients, and learners get support to build verbal, spatial, numerical and other transferable skills."
  quote: full   # the issuer's statement is in `source` (D-std-0014)
  audience: practitioner
  subjects: inherited
- id: qaa/optometry-2024/1.17
  locator: { number: "1.17", headingPath: ["Context and purposes of an Optometry degree", "Education for sustainable development"] }
  span: { start: 20314, end: 21168 }
  source: "1.17 Optometry is central to improving diverse health outcomes, and courses in Optometry should inspire future practitioners to engage with the ongoing process of addressing personal, human and global challenges to create better visual health and life experiences for all. Optometry courses may include topics drawn from the United Nations Sustainable Development Goals, particularly those associated with health and the environment. Education for sustainable development is thus an integral part of the study of Optometry, ensuring that graduates are equipped with the knowledge, skills and competencies that can enable them to generate innovative solutions to complex challenges, and contribute to the improvement of community and global health. More information on education for sustainable development can be found in the QAA and Advance HE guidance."
  stem: none
  statementType: requirement
  rung: none
  force: should
  level: none
  appliesTo: "Optometry courses"
  addressee: both
  verbs: ["inspire", "engage", "equipped"]
  about: "sustainable development and global health in the subject"
  themes: [theme:esd]
  domain: none
  award: ["integrated master's"]
  gradeOf: none
  paraphrase: "Courses should inspire future practitioners to take on personal, human and global challenges for better visual health; they may draw on the UN Sustainable Development Goals, and sustainable development is part of the subject so graduates can find new answers to complex problems in community and global health."
  quote: full   # the issuer's statement is in `source` (D-std-0014)
  audience: both
  subjects: inherited
- id: qaa/optometry-2024/1.18
  locator: { number: "1.18", headingPath: ["Context and purposes of an Optometry degree", "Employability, enterprise and entrepreneurship"] }
  span: { start: 21219, end: 21794 }
  source: "1.18 All Optometry degree courses should equip students with the knowledge, skills, behaviours, characteristics and attributes that prepare them for life after graduation in an increasingly complex and ever-changing social, cultural and economic environment and enable them to make a meaningful and effective contribution to society. Optometry graduates should be equipped not only with the discipline-specific knowledge and professional skills necessary for careers in clinical practice, but also the wider attributes to prepare them for careers in other roles and sectors.\n"
  stem: none
  statementType: requirement
  rung: none
  force: should
  level: fheq:7
  appliesTo: "all Optometry degree courses"
  addressee: both
  verbs: ["equip", "prepare"]
  about: "preparation for working life in and beyond clinical practice"
  themes: [theme:enterprise]
  domain: generic-skill
  award: ["integrated master's"]
  gradeOf: none
  paraphrase: "Every course should give students the knowledge, skills, behaviours and attributes for life after graduating in a complex, changing world, and should prepare them both for clinical careers and for roles in other sectors."
  quote: full   # the issuer's statement is in `source` (D-std-0014)
  audience: both
  subjects: inherited
- id: qaa/optometry-2024/1.19
  locator: { number: "1.19", headingPath: ["Context and purposes of an Optometry degree", "Employability, enterprise and entrepreneurship"] }
  span: { start: 21794, end: 22057 }
  source: "1.19 Enterprise and entrepreneurship education should be integrated into Optometry courses, particularly since many optometrists operate in commercial, manufacturing or charitable environments, and practice ownership/franchising is commonplace among registrants.\n"
  stem: none
  statementType: requirement
  rung: none
  force: should
  level: none
  appliesTo: "Optometry courses"
  addressee: provider
  verbs: ["integrated"]
  about: "enterprise education built into courses"
  themes: [theme:enterprise]
  domain: none
  award: ["integrated master's"]
  gradeOf: none
  paraphrase: "Enterprise and entrepreneurship education should be built into courses, not least because many optometrists work in commercial, manufacturing or charitable settings and owning or franchising a practice is common."
  quote: full   # the issuer's statement is in `source` (D-std-0014)
  audience: practitioner
  subjects: inherited
- id: qaa/optometry-2024/2.2
  locator: { number: "2.2", headingPath: ["Distinctive features of an Optometry degree", "Design"] }
  span: { start: 24081, end: 24567 }
  source: "2.2 Graduates must complete an extensive period of integrated learning in practice to meet the requirements of the regulator. Patient-facing learning opportunities (real and simulated) will increase in volume and complexity as students progress through the course. The length and breadth of clinical experiences will vary, with periods of placement/ assessed professional practice taking place in a range of settings (for example, community, hospital and/or higher education provider).\n"
  stem: none
  statementType: requirement
  rung: none
  force: must
  level: fheq:7
  appliesTo: "graduates of the subject"
  addressee: learner
  verbs: ["complete"]
  about: "an extended period of learning in practice"
  themes: [none]
  domain: none
  award: ["integrated master's"]
  gradeOf: none
  paraphrase: "To satisfy the regulator, graduates must complete a long period of learning integrated with practice; real and simulated patient-facing work will grow in amount and complexity, and placements vary in length and setting."
  quote: full   # the issuer's statement is in `source` (D-std-0014)
  audience: both
  subjects: inherited
- id: qaa/optometry-2024/2.3
  locator: { number: "2.3", headingPath: ["Distinctive features of an Optometry degree", "Design"] }
  span: { start: 24567, end: 24924 }
  source: "2.3 Repeated experiences under controlled conditions will develop students until they are assessed as ready to undertake all the tasks of an optometrist, under delegation from, and under the supervision of, a fully qualified registrant. Readiness for full registration and independent practice as an optometrist will be assessed as part of this experience.\n"
  stem: none
  statementType: expectation
  rung: none
  force: will
  level: fheq:7
  appliesTo: "students of the subject"
  addressee: learner
  verbs: ["develop", "assessed"]
  about: "supervised practice and readiness for registration"
  themes: [none]
  domain: subject-skill
  award: ["integrated master's"]
  gradeOf: none
  paraphrase: "Repeated, controlled and supervised practice will develop students until they are judged ready to do all an optometrist's tasks under delegation, and their readiness for full registration and independent practice will be assessed in this experience."
  quote: full   # the issuer's statement is in `source` (D-std-0014)
  audience: both
  subjects: inherited
- id: qaa/optometry-2024/2.7
  locator: { number: "2.7", headingPath: ["Distinctive features of an Optometry degree", "Progression"] }
  span: { start: 26299, end: 26905 }
  source: "2.7 Over the duration of the degree, an Optometry student will progress from one level of study to the next, in line with the regulations and processes for each higher education institution and the regulator. However, it is expected that each level would see the attainment of knowledge, expertise and experience that builds towards the final achievement of meeting the threshold-level subject-specific and generic skills listed in this Statement. This will usually include successful completion and the award of credit for the full range of learning and assessment, including any practical components.\n\n9\n"
  stem: none
  statementType: expectation
  rung: none
  force: will
  level: fheq:7
  appliesTo: "students of the subject"
  addressee: both
  verbs: ["progress", "include"]
  about: "progression towards the threshold skills"
  themes: [none]
  domain: none
  award: ["integrated master's"]
  gradeOf: none
  paraphrase: "A student will move from level to level under the institution's and the regulator's rules; each level is expected to add knowledge, expertise and experience towards the threshold subject and generic skills, usually including credit for all learning and assessment, practical parts included."
  quote: full   # the issuer's statement is in `source` (D-std-0014)
  audience: both
  subjects: inherited
- id: qaa/optometry-2024/2.9
  locator: { number: "2.9", headingPath: ["Distinctive features of an Optometry degree", "Progression"] }
  span: { start: 27148, end: 27706 }
  source: "2.9 Optometry courses should be designed to promote academic and personal development. The curriculum should be based on Miller’s pyramid (Miller, G E (1990), enabling students to initially apply their knowledge and understanding of simple concepts to solve well-defined problems. As the course advances, they should develop confidence in their subject-specific knowledge and understanding, making connections between more challenging and complex patient scenarios that enable them to analyse and evaluate clinical information and problem-solve effectively.\n"
  stem: none
  statementType: requirement
  rung: none
  force: should
  level: none
  appliesTo: "Optometry courses"
  addressee: provider
  verbs: ["designed", "promote", "based", "develop"]
  about: "design on Miller's pyramid"
  themes: [none]
  domain: none
  award: ["integrated master's"]
  gradeOf: none
  paraphrase: "Courses should be designed for academic and personal growth, with the curriculum built on Miller's pyramid: students first apply understanding of simple ideas to well-defined problems, then gain confidence and link harder patient cases to analyse, evaluate and solve clinical problems."
  quote: full   # the issuer's statement is in `source` (D-std-0014)
  audience: practitioner
  subjects: inherited
- id: qaa/optometry-2024/2.10.b1
  locator: { number: "2.10.b1", headingPath: ["Distinctive features of an Optometry degree", "Progression"] }
  span: { start: 28099, end: 28175 }
  source: "recognise the diversity of prior experience and the challenges of transition"
  stem: "2.10"
  statementType: requirement
  rung: none
  force: should
  level: none
  appliesTo: "learning, teaching and assessment strategies"
  addressee: provider
  verbs: ["recognise"]
  about: "prior experience and transition"
  themes: [none]
  domain: none
  award: ["integrated master's"]
  gradeOf: none
  paraphrase: "Strategies that support progressive learning should take account of the range of students' earlier experience and the difficulty of moving into higher education."
  quote: full   # the issuer's statement is in `source` (D-std-0014)
  audience: practitioner
  subjects: inherited
- id: qaa/optometry-2024/2.10.b2
  locator: { number: "2.10.b2", headingPath: ["Distinctive features of an Optometry degree", "Progression"] }
  span: { start: 28178, end: 28341 }
  source: "provide opportunity for all students to achieve their potential and realise their ambitions, irrespective of their background or motivations for studying Optometry"
  stem: "2.10"
  statementType: requirement
  rung: none
  force: should
  level: none
  appliesTo: "learning, teaching and assessment strategies"
  addressee: provider
  verbs: ["provide", "achieve", "realise"]
  about: "every student able to reach their potential"
  themes: [none]
  domain: none
  award: ["integrated master's"]
  gradeOf: none
  paraphrase: "Progression strategies should give every student the chance to reach their potential and goals, whatever their background or reason for studying."
  quote: full   # the issuer's statement is in `source` (D-std-0014)
  audience: practitioner
  subjects: inherited
- id: qaa/optometry-2024/2.10.b3
  locator: { number: "2.10.b3", headingPath: ["Distinctive features of an Optometry degree", "Progression"] }
  span: { start: 28344, end: 28409 }
  source: "support academic and personal development in addition to learning"
  stem: "2.10"
  statementType: requirement
  rung: none
  force: should
  level: none
  appliesTo: "learning, teaching and assessment strategies"
  addressee: provider
  verbs: ["support"]
  about: "academic and personal development"
  themes: [none]
  domain: none
  award: ["integrated master's"]
  gradeOf: none
  paraphrase: "Progression strategies should foster academic and personal development as well as learning of content."
  quote: full   # the issuer's statement is in `source` (D-std-0014)
  audience: practitioner
  subjects: inherited
- id: qaa/optometry-2024/2.10.b4
  locator: { number: "2.10.b4", headingPath: ["Distinctive features of an Optometry degree", "Progression"] }
  span: { start: 28412, end: 28496 }
  source: "are matched to the course learning outcomes or competencies for each level of study."
  stem: "2.10"
  statementType: requirement
  rung: none
  force: should
  level: none
  appliesTo: "learning, teaching and assessment strategies"
  addressee: provider
  verbs: ["matched"]
  about: "strategies matched to outcomes for each level"
  themes: [none]
  domain: none
  award: ["integrated master's"]
  gradeOf: none
  paraphrase: "Progression strategies should fit the learning outcomes or competencies of the course at each level of study."
  quote: full   # the issuer's statement is in `source` (D-std-0014)
  audience: practitioner
  subjects: inherited
- id: qaa/optometry-2024/2.11
  locator: { number: "2.11", headingPath: ["Distinctive features of an Optometry degree", "Progression"] }
  span: { start: 28497, end: 29441 }
  source: "2.11 Students on an Optometry degree course will progress from one level or academic stage to the next by satisfying the regulations and processes for each institution. Subject to the regulations for the institution, students should usually be offered an opportunity to re-sit any failed assessments, particularly where failure prevents either progression or eligibility for an award. Students who are not eligible to progress, or who choose to leave a course early, may be eligible for a Certificate of Higher Education, a Diploma of Higher Education, or a Pass degree, depending on the amount and type of credit successfully completed. Integrated master’s degrees typically also offer an alternative non-registerable degree as an exit award for those who have attained sufficient credit but do not complete the programme. In such instances where students exit without a master’s degree they will not be eligible to register as an optometrist."
  stem: none
  statementType: requirement
  rung: none
  force: should
  level: fheq:7
  appliesTo: "students of the subject"
  addressee: both
  verbs: ["progress", "offered"]
  about: "progression, resits and exit awards"
  themes: [none]
  domain: none
  award: ["integrated master's"]
  gradeOf: none
  paraphrase: "Students move between levels under each institution's rules; they should usually get a chance to resit failed assessments, especially where failing blocks progression or an award; those who leave early may receive a lower award, but anyone leaving without the master's will not be able to register."
  quote: full   # the issuer's statement is in `source` (D-std-0014)
  audience: both
  subjects: inherited
- id: qaa/optometry-2024/2.13
  locator: { number: "2.13", headingPath: ["Distinctive features of an Optometry degree", "Flexibility"] }
  span: { start: 29816, end: 30043 }
  source: "2.13 Optometry courses utilise diverse modes of delivery. The range of delivery methods (both face-to-face and digital) should be diverse and appropriate for the needs of the learner, the taught material and their assessments.\n"
  stem: none
  statementType: requirement
  rung: none
  force: should
  level: none
  appliesTo: "Optometry courses"
  addressee: provider
  verbs: ["utilise"]
  about: "diverse delivery fitted to learners and material"
  themes: [none]
  domain: none
  award: ["integrated master's"]
  gradeOf: none
  paraphrase: "Courses use many modes of delivery; the face-to-face and digital methods should be varied and suited to learners, content and assessment."
  quote: full   # the issuer's statement is in `source` (D-std-0014)
  audience: practitioner
  subjects: inherited
- id: qaa/optometry-2024/2.14
  locator: { number: "2.14", headingPath: ["Distinctive features of an Optometry degree", "Flexibility"] }
  span: { start: 30043, end: 30320 }
  source: "2.14 Given that Optometry students must acquire clinical, patient-facing and reflective skills, courses must contain practical sessions supported by opportunities to reflect utilising a range of (real and simulated) environments, ensuring an appropriate scope of practice.\n\n10\n"
  stem: none
  statementType: requirement
  rung: none
  force: must
  level: fheq:7
  appliesTo: "Optometry courses and students"
  addressee: both
  verbs: ["acquire", "contain", "reflect"]
  about: "practical, reflective sessions in real and simulated settings"
  themes: [none]
  domain: subject-skill
  award: ["integrated master's"]
  gradeOf: none
  paraphrase: "Because students must gain clinical, patient-facing and reflective skills, courses must include practical sessions with chances to reflect, in real and simulated settings, within a suitable scope of practice."
  quote: full   # the issuer's statement is in `source` (D-std-0014)
  audience: both
  subjects: inherited
- id: qaa/optometry-2024/2.15
  locator: { number: "2.15", headingPath: ["Distinctive features of an Optometry degree", "Flexibility"] }
  span: { start: 30320, end: 30713 }
  source: "2.15 Courses also need to be sufficiently flexible to be able to respond to and anticipate change, both in the advancement of the subject and its interface with other disciplines, and in the needs of its graduates and their employers, as required. Courses should also be sufficiently resilient to be able to adapt to unforeseen circumstances and other challenges that may arise in the future.\n"
  stem: none
  statementType: requirement
  rung: none
  force: should
  level: none
  appliesTo: "Optometry courses"
  addressee: provider
  verbs: ["respond", "anticipate", "adapt"]
  about: "courses able to change and withstand disruption"
  themes: [none]
  domain: none
  award: ["integrated master's"]
  gradeOf: none
  paraphrase: "Courses need enough flexibility to respond to and foresee change in the subject, its links with other fields and the needs of graduates and employers, and should be resilient enough to adapt to unforeseen events."
  quote: full   # the issuer's statement is in `source` (D-std-0014)
  audience: practitioner
  subjects: inherited
- id: qaa/optometry-2024/2.16
  locator: { number: "2.16", headingPath: ["Distinctive features of an Optometry degree", "Flexibility"] }
  span: { start: 30713, end: 30847 }
  source: "2.16 Courses should be sufficiently flexible to be able to respond to changes in technology, including use of artificial intelligence."
  stem: none
  statementType: requirement
  rung: none
  force: should
  level: none
  appliesTo: "Optometry courses"
  addressee: provider
  verbs: ["respond"]
  about: "responding to new technology and artificial intelligence"
  themes: [none]
  domain: none
  award: ["integrated master's"]
  gradeOf: none
  paraphrase: "Courses should be flexible enough to keep up with changing technology, artificial intelligence among it."
  quote: full   # the issuer's statement is in `source` (D-std-0014)
  audience: practitioner
  subjects: inherited
- id: qaa/optometry-2024/2.17
  locator: { number: "2.17", headingPath: ["Distinctive features of an Optometry degree", "Partnership"] }
  span: { start: 30860, end: 31420 }
  source: "2.17 Educational institutions may operate in academic partnerships with placement providers, such as the professional body, employers in hospital or community settings (for example, high street practice), or other relevant partners, to provide training elements of the degree. Providers are expected to develop processes for oversight to ensure that partners involved in degree delivery meet all relevant standards and expectations. This should include effective communication and regular consultation to ensure that courses continue to meet employers’ needs.\n"
  stem: none
  statementType: requirement
  rung: none
  force: should
  level: none
  appliesTo: "institutions with placement partners"
  addressee: provider
  verbs: ["develop", "ensure"]
  about: "oversight of placement partners"
  themes: [none]
  domain: none
  award: ["integrated master's"]
  gradeOf: none
  paraphrase: "Institutions may work with placement partners such as the professional body or employers; they are expected to set up oversight so partners meet all standards, and this should include good communication and regular consultation to keep courses meeting employers' needs."
  quote: full   # the issuer's statement is in `source` (D-std-0014)
  audience: practitioner
  subjects: inherited
- id: qaa/optometry-2024/2.18
  locator: { number: "2.18", headingPath: ["Distinctive features of an Optometry degree", "Partnership"] }
  span: { start: 31420, end: 31919 }
  source: "2.18 Courses should work with relevant stakeholders to incorporate work-based or simulated clinical practice where possible. Enhancing student employability is a fundamental outcome for Optometry courses, which should have a clear strategy for students to develop employment-focused skills and engage with employers. Students may engage with employers through placements of various durations during which they are fully immersed in the workplace and experience the day-to-day routine of employment.\n"
  stem: none
  statementType: requirement
  rung: none
  force: should
  level: none
  appliesTo: "Optometry courses"
  addressee: both
  verbs: ["work", "incorporate", "engage"]
  about: "work-based practice and an employability strategy"
  themes: [none]
  domain: none
  award: ["integrated master's"]
  gradeOf: none
  paraphrase: "Courses should work with stakeholders to include work-based or simulated clinical practice where possible; employability is a core outcome, so courses should have a clear plan for students to build work skills and meet employers, for example through placements."
  quote: full   # the issuer's statement is in `source` (D-std-0014)
  audience: both
  subjects: inherited
- id: qaa/optometry-2024/2.20
  locator: { number: "2.20", headingPath: ["Distinctive features of an Optometry degree", "Partnership"] }
  span: { start: 32467, end: 33232 }
  source: "2.20 Students should expect to be embraced as partners within their own courses and be involved in co-creation of their curriculum. Additionally, the student voice should play a significant role in course development, delivery, review and the overall student experience within Optometry. The student voice can be listened to through departmental representatives, module evaluation and external student surveys such as the National Student Survey (NSS); students provide feedback, which in turn supports their own learning. Furthermore, students can feed into, and collaborate with, their students’ union, and many higher education providers offer public social media platforms to receive feedback from students and discuss current trends in the student experience.\n"
  stem: none
  statementType: requirement
  rung: none
  force: should
  level: none
  appliesTo: "students and courses"
  addressee: both
  verbs: ["expect", "involved"]
  about: "students as partners and co-creators"
  themes: [none]
  domain: none
  award: ["integrated master's"]
  gradeOf: none
  paraphrase: "Students should be able to expect to be treated as partners in their course and to help shape its curriculum, with the student voice playing a large part in development, delivery and review through representatives, evaluations and surveys."
  quote: full   # the issuer's statement is in `source` (D-std-0014)
  audience: both
  subjects: inherited
- id: qaa/optometry-2024/2.24
  locator: { number: "2.24", headingPath: ["Distinctive features of an Optometry degree", "Monitoring and review"] }
  span: { start: 34623, end: 35118 }
  source: "2.24 Monitoring and review should include feedback from current students, external stakeholders, such as employers and placement providers, and alumni, to influence curriculum design, content and delivery. Evaluation of student performance data and various measures of the student experience should be integrated with expert review. Periodic review should enable the embedding of Education for Sustainable Development (ESD) and equality, diversity and inclusion (EDI) throughout the curriculum.\n"
  stem: none
  statementType: requirement
  rung: none
  force: should
  level: none
  appliesTo: "course monitoring and review"
  addressee: provider
  verbs: ["include", "influence", "integrated", "enable"]
  about: "feedback in review and embedding ESD and EDI"
  themes: [none]
  domain: none
  award: ["integrated master's"]
  gradeOf: none
  paraphrase: "Monitoring and review should take in feedback from current students, employers, placement hosts and alumni to shape the curriculum; data on student performance and experience should be combined with expert review; and periodic review should help embed sustainability and equality, diversity and inclusion throughout."
  quote: full   # the issuer's statement is in `source` (D-std-0014)
  audience: practitioner
  subjects: inherited
- id: qaa/optometry-2024/2.26
  locator: { number: "2.26", headingPath: ["Distinctive features of an Optometry degree", "Monitoring and review"] }
  span: { start: 36082, end: 36816 }
  source: "2.26 Course teams conduct regular monitoring and evaluation, with the support of independent evaluators and student feedback, to ensure continuous quality enhancement. Evaluation of student performance data as well as student feedback and the student voice, alongside other measures of the student experience, should be integrated with expert review, including that provided by external examiners, to ensure that curricula remain current, engaging and accessible. Historic data may also enable trend analyses to measure progress and identify emerging issues. Students and graduates, as well as employers, service users and relevant professional bodies, should be actively involved in designing and delivering enhancements to courses.\n"
  stem: none
  statementType: requirement
  rung: none
  force: should
  level: none
  appliesTo: "course teams and stakeholders"
  addressee: both
  verbs: ["conduct", "integrated", "involved"]
  about: "evaluation and involvement in course enhancement"
  themes: [none]
  domain: none
  award: ["integrated master's"]
  gradeOf: none
  paraphrase: "Course teams evaluate regularly for continuing improvement; performance data, student feedback and voice should be joined with expert review, external examiners' included, to keep curricula current, engaging and accessible; students, graduates, employers, service users and professional bodies should be actively involved in improving courses."
  quote: full   # the issuer's statement is in `source` (D-std-0014)
  audience: both
  subjects: inherited
- id: qaa/optometry-2024/2.27
  locator: { number: "2.27", headingPath: ["Distinctive features of an Optometry degree", "Monitoring and review"] }
  span: { start: 36816, end: 37061 }
  source: "2.27 An Optometry course will also require evaluation and accreditation from professional and regulatory bodies, depending on academic level. These processes are usually conducted through a combination of site visits and desk-based reviews.\n\n12\n"
  stem: none
  statementType: requirement
  rung: none
  force: will
  level: none
  appliesTo: "Optometry courses"
  addressee: provider
  verbs: ["require"]
  about: "accreditation by professional and regulatory bodies"
  themes: [none]
  domain: none
  award: ["integrated master's"]
  gradeOf: none
  paraphrase: "An Optometry course will also need evaluation and accreditation by professional and regulatory bodies, depending on its level, usually through visits and desk reviews."
  quote: full   # the issuer's statement is in `source` (D-std-0014)
  audience: practitioner
  subjects: inherited
- id: qaa/optometry-2024/3.1
  locator: { number: "3.1", headingPath: ["Content, structure and delivery", "Content"] }
  span: { start: 37435, end: 37606 }
  source: "For professional registration, graduates must meet the required General Optical Council (GOC) outcomes and standards to join the register as a fully qualified optometrist."
  stem: none
  statementType: requirement
  rung: none
  force: must
  level: fheq:7
  appliesTo: "graduates seeking registration"
  addressee: learner
  verbs: ["meet", "join"]
  about: "meeting the regulator's outcomes to register"
  themes: [none]
  domain: none
  award: ["integrated master's"]
  gradeOf: none
  paraphrase: "To register, graduates must satisfy the General Optical Council's required outcomes and standards to join its register as fully qualified optometrists."
  quote: full   # the issuer's statement is in `source` (D-std-0014)
  audience: both
  subjects: inherited
- id: qaa/optometry-2024/3.1.b1
  locator: { number: "3.1.b1", headingPath: ["Content, structure and delivery", "Content"] }
  span: { start: 37731, end: 37831 }
  source: "working within relevant scope of practice to ensure safe, lawful and effective patient- centred care"
  stem: "3.1"
  statementType: outcome
  rung: none
  force: should
  level: fheq:7
  appliesTo: "graduates of the subject"
  addressee: both
  verbs: ["working", "ensure"]
  about: "safe practice within scope"
  themes: [none]
  domain: subject-skill
  award: ["integrated master's"]
  gradeOf: none
  paraphrase: "Courses should equip graduates to work inside their scope of practice so that patient-centred care is safe, lawful and effective."
  quote: full   # the issuer's statement is in `source` (D-std-0014)
  audience: both
  subjects: inherited
- id: qaa/optometry-2024/3.1.b2
  locator: { number: "3.1.b2", headingPath: ["Content, structure and delivery", "Content"] }
  span: { start: 37834, end: 37895 }
  source: "critical thinking and evidence-based clinical decision-making"
  stem: "3.1"
  statementType: outcome
  rung: none
  force: should
  level: fheq:7
  appliesTo: "graduates of the subject"
  addressee: both
  verbs: []
  about: "critical thinking and evidence-based decisions"
  themes: [none]
  domain: subject-skill
  award: ["integrated master's"]
  gradeOf: none
  paraphrase: "Courses should equip graduates with critical thinking and clinical decisions grounded in evidence."
  quote: full   # the issuer's statement is in `source` (D-std-0014)
  audience: both
  subjects: inherited
- id: qaa/optometry-2024/3.1.b3
  locator: { number: "3.1.b3", headingPath: ["Content, structure and delivery", "Content"] }
  span: { start: 37898, end: 37976 }
  source: "critical appraisal of the research literature and other sources of information"
  stem: "3.1"
  statementType: outcome
  rung: none
  force: should
  level: fheq:7
  appliesTo: "graduates of the subject"
  addressee: both
  verbs: []
  about: "critical appraisal of literature and information"
  themes: [none]
  domain: generic-skill
  award: ["integrated master's"]
  gradeOf: none
  paraphrase: "Courses should equip graduates to appraise research and other information sources critically."
  quote: full   # the issuer's statement is in `source` (D-std-0014)
  audience: both
  subjects: inherited
- id: qaa/optometry-2024/3.1.b4
  locator: { number: "3.1.b4", headingPath: ["Content, structure and delivery", "Content"] }
  span: { start: 37979, end: 38028 }
  source: "effective verbal and written communication skills"
  stem: "3.1"
  statementType: outcome
  rung: none
  force: should
  level: fheq:7
  appliesTo: "graduates of the subject"
  addressee: both
  verbs: []
  about: "verbal and written communication"
  themes: [none]
  domain: generic-skill
  award: ["integrated master's"]
  gradeOf: none
  paraphrase: "Courses should equip graduates with effective spoken and written communication."
  quote: full   # the issuer's statement is in `source` (D-std-0014)
  audience: both
  subjects: inherited
- id: qaa/optometry-2024/3.1.b5
  locator: { number: "3.1.b5", headingPath: ["Content, structure and delivery", "Content"] }
  span: { start: 38031, end: 38098 }
  source: "reflective practice to support continuing professional development."
  stem: "3.1"
  statementType: outcome
  rung: none
  force: should
  level: fheq:7
  appliesTo: "graduates of the subject"
  addressee: both
  verbs: ["support"]
  about: "reflective practice for CPD"
  themes: [none]
  domain: generic-skill
  award: ["integrated master's"]
  gradeOf: none
  paraphrase: "Courses should equip graduates with reflective practice that supports their continuing professional development."
  quote: full   # the issuer's statement is in `source` (D-std-0014)
  audience: both
  subjects: inherited
- id: qaa/optometry-2024/3.5.b1
  locator: { number: "3.5.b1", headingPath: ["Content, structure and delivery", "Content"] }
  span: { start: 41775, end: 41902 }
  source: "employ an adaptive and personalised approach to patient care, taking into account social, clinical, personal and cultural needs"
  stem: "3.5"
  statementType: outcome
  rung: none
  force: must
  level: fheq:7
  appliesTo: "graduates seeking registration"
  addressee: learner
  verbs: ["employ", "taking"]
  about: "adaptive, personalised patient care"
  themes: [none]
  domain: subject-skill
  award: ["integrated master's"]
  gradeOf: none
  paraphrase: "For registration, graduates must be able to adapt and personalise care to each patient's social, clinical, personal and cultural needs."
  quote: full   # the issuer's statement is in `source` (D-std-0014)
  audience: both
  subjects: inherited
- id: qaa/optometry-2024/3.5.b2
  locator: { number: "3.5.b2", headingPath: ["Content, structure and delivery", "Content"] }
  span: { start: 41905, end: 41966 }
  source: "communicate effectively with patients and other professionals"
  stem: "3.5"
  statementType: outcome
  rung: none
  force: must
  level: fheq:7
  appliesTo: "graduates seeking registration"
  addressee: learner
  verbs: ["communicate"]
  about: "communication with patients and professionals"
  themes: [none]
  domain: generic-skill
  award: ["integrated master's"]
  gradeOf: none
  paraphrase: "For registration, graduates must be able to communicate well with patients and other professionals."
  quote: full   # the issuer's statement is in `source` (D-std-0014)
  audience: both
  subjects: inherited
- id: qaa/optometry-2024/3.5.b3
  locator: { number: "3.5.b3", headingPath: ["Content, structure and delivery", "Content"] }
  span: { start: 41969, end: 42116 }
  source: "undertake appropriate ocular examinations and devise evidence-informed management plans within the limits of their scope of practice and competence"
  stem: "3.5"
  statementType: outcome
  rung: none
  force: must
  level: fheq:7
  appliesTo: "graduates seeking registration"
  addressee: learner
  verbs: ["undertake", "devise"]
  about: "examinations and management plans within competence"
  themes: [none]
  domain: subject-skill
  award: ["integrated master's"]
  gradeOf: none
  paraphrase: "For registration, graduates must be able to carry out suitable eye examinations and draw up management plans informed by evidence, within their scope and competence."
  quote: full   # the issuer's statement is in `source` (D-std-0014)
  audience: both
  subjects: inherited
- id: qaa/optometry-2024/3.5.b4
  locator: { number: "3.5.b4", headingPath: ["Content, structure and delivery", "Content"] }
  span: { start: 42123, end: 42214 }
  source: "uphold high equitable professional standards and ethics and work within current legislation"
  stem: "3.5"
  statementType: outcome
  rung: none
  force: must
  level: fheq:7
  appliesTo: "graduates seeking registration"
  addressee: learner
  verbs: ["uphold", "work"]
  about: "professional standards, ethics and law"
  themes: [none]
  domain: subject-skill
  award: ["integrated master's"]
  gradeOf: none
  paraphrase: "For registration, graduates must be able to keep high, fair professional and ethical standards and work within the law."
  quote: full   # the issuer's statement is in `source` (D-std-0014)
  audience: both
  subjects: inherited
- id: qaa/optometry-2024/3.5.b5
  locator: { number: "3.5.b5", headingPath: ["Content, structure and delivery", "Content"] }
  span: { start: 42217, end: 42300 }
  source: "identify risks to patients, colleagues and others and provide sufficient safeguards"
  stem: "3.5"
  statementType: outcome
  rung: none
  force: must
  level: fheq:7
  appliesTo: "graduates seeking registration"
  addressee: learner
  verbs: ["identify", "provide"]
  about: "identifying risk and safeguarding"
  themes: [none]
  domain: subject-skill
  award: ["integrated master's"]
  gradeOf: none
  paraphrase: "For registration, graduates must be able to spot risks to patients, colleagues and others and put enough safeguards in place."
  quote: full   # the issuer's statement is in `source` (D-std-0014)
  audience: both
  subjects: inherited
- id: qaa/optometry-2024/3.5.b6
  locator: { number: "3.5.b6", headingPath: ["Content, structure and delivery", "Content"] }
  span: { start: 42303, end: 42453 }
  source: "provide clinical leadership, promoting and engaging with clinical governance requirements, service improvements and national public health initiatives"
  stem: "3.5"
  statementType: outcome
  rung: none
  force: must
  level: fheq:7
  appliesTo: "graduates seeking registration"
  addressee: learner
  verbs: ["provide", "promoting", "engaging"]
  about: "clinical leadership and governance"
  themes: [none]
  domain: subject-skill
  award: ["integrated master's"]
  gradeOf: none
  paraphrase: "For registration, graduates must be able to lead clinically and support clinical governance, service improvement and national public health initiatives."
  quote: full   # the issuer's statement is in `source` (D-std-0014)
  audience: both
  subjects: inherited
- id: qaa/optometry-2024/3.5.b7
  locator: { number: "3.5.b7", headingPath: ["Content, structure and delivery", "Content"] }
  span: { start: 42456, end: 42566 }
  source: "keep knowledge and skills up to date and evaluate own performance to improve the quality of care for patients."
  stem: "3.5"
  statementType: outcome
  rung: none
  force: must
  level: fheq:7
  appliesTo: "graduates seeking registration"
  addressee: learner
  verbs: ["keep", "evaluate", "improve"]
  about: "keeping up to date and evaluating own performance"
  themes: [none]
  domain: generic-skill
  award: ["integrated master's"]
  gradeOf: none
  paraphrase: "For registration, graduates must be able to keep their knowledge and skills current and assess their own performance to raise the quality of patient care."
  quote: full   # the issuer's statement is in `source` (D-std-0014)
  audience: both
  subjects: inherited
- id: qaa/optometry-2024/3.8
  locator: { number: "3.8", headingPath: ["Content, structure and delivery", "Teaching and learning"] }
  span: { start: 43801, end: 44163 }
  source: "3.8 Teaching and learning strategies used in Optometry courses are not fixed and should be responsive to advances in clinical practice, technology and research around teaching pedagogy. Staff who contribute to student learning keep up to date and have regular access to both subject-specific and educational professional development resources and opportunities.\n"
  stem: none
  statementType: requirement
  rung: none
  force: should
  level: none
  appliesTo: "teaching and learning strategies; staff"
  addressee: provider
  verbs: ["keep"]
  about: "responsive teaching and staff development"
  themes: [none]
  domain: none
  award: ["integrated master's"]
  gradeOf: none
  paraphrase: "Teaching and learning strategies are not fixed and should respond to advances in clinical practice, technology and pedagogic research; staff keep current and have regular access to subject and educational development."
  quote: full   # the issuer's statement is in `source` (D-std-0014)
  audience: practitioner
  subjects: inherited
- id: qaa/optometry-2024/3.12
  locator: { number: "3.12", headingPath: ["Content, structure and delivery", "Assessment"] }
  span: { start: 46346, end: 47076 }
  source: "3.12 The assessment of students' achievement in Optometry constructively aligns with learning outcomes and is appropriate to the knowledge, abilities, academic and professional skills that the course aims to develop. All GOC outcomes must be assessed and mapped. The diversity of assessment deployed across Optometry courses should reflect this. Assessment should be authentic, rigorous and relevant to clinical practice. Wherever possible, it should support the development of skills and concepts required specifically for a career in Optometry but also of more general skills that enhance the wider employability of Optometry graduates. It should also be able to discriminate between achievement at threshold and higher levels.\n"
  stem: none
  statementType: requirement
  rung: none
  force: must
  level: none
  appliesTo: "assessment in Optometry courses"
  addressee: provider
  verbs: ["assessed", "mapped", "reflect", "support", "discriminate"]
  about: "aligned, authentic assessment of every regulator outcome"
  themes: [none]
  domain: none
  award: ["integrated master's"]
  gradeOf: none
  paraphrase: "Assessment is constructively aligned with outcomes; every GOC outcome must be assessed and mapped, and assessment should be varied, authentic, rigorous and clinically relevant, build both professional and wider employability skills, and tell threshold achievement apart from higher achievement."
  quote: full   # the issuer's statement is in `source` (D-std-0014)
  audience: practitioner
  subjects: inherited
- id: qaa/optometry-2024/3.13.b1
  locator: { number: "3.13.b1", headingPath: ["Content, structure and delivery", "Assessment"] }
  span: { start: 47132, end: 47140 }
  source: "validity"
  stem: "3.13"
  statementType: requirement
  rung: none
  force: should
  level: none
  appliesTo: "assessment in Optometry courses"
  addressee: provider
  verbs: []
  about: "assessment balances validity"
  themes: [none]
  domain: none
  award: ["integrated master's"]
  gradeOf: none
  paraphrase: "Assessment should weigh validity against the other qualities listed: it measures what it claims to."
  quote: full   # the issuer's statement is in `source` (D-std-0014)
  audience: practitioner
  subjects: inherited
- id: qaa/optometry-2024/3.13.b2
  locator: { number: "3.13.b2", headingPath: ["Content, structure and delivery", "Assessment"] }
  span: { start: 47143, end: 47154 }
  source: "reliability"
  stem: "3.13"
  statementType: requirement
  rung: none
  force: should
  level: none
  appliesTo: "assessment in Optometry courses"
  addressee: provider
  verbs: []
  about: "assessment balances reliability"
  themes: [none]
  domain: none
  award: ["integrated master's"]
  gradeOf: none
  paraphrase: "Assessment should weigh reliability against the other qualities listed: it gives consistent results."
  quote: full   # the issuer's statement is in `source` (D-std-0014)
  audience: practitioner
  subjects: inherited
- id: qaa/optometry-2024/3.13.b3
  locator: { number: "3.13.b3", headingPath: ["Content, structure and delivery", "Assessment"] }
  span: { start: 47157, end: 47169 }
  source: "equitability"
  stem: "3.13"
  statementType: requirement
  rung: none
  force: should
  level: none
  appliesTo: "assessment in Optometry courses"
  addressee: provider
  verbs: []
  about: "assessment balances equitability"
  themes: [none]
  domain: none
  award: ["integrated master's"]
  gradeOf: none
  paraphrase: "Assessment should weigh equitability against the other qualities listed: it is fair to every student."
  quote: full   # the issuer's statement is in `source` (D-std-0014)
  audience: practitioner
  subjects: inherited
- id: qaa/optometry-2024/3.13.b4
  locator: { number: "3.13.b4", headingPath: ["Content, structure and delivery", "Assessment"] }
  span: { start: 47172, end: 47182 }
  source: "efficiency"
  stem: "3.13"
  statementType: requirement
  rung: none
  force: should
  level: none
  appliesTo: "assessment in Optometry courses"
  addressee: provider
  verbs: []
  about: "assessment balances efficiency"
  themes: [none]
  domain: none
  award: ["integrated master's"]
  gradeOf: none
  paraphrase: "Assessment should weigh efficiency against the other qualities listed: it is proportionate in effort."
  quote: full   # the issuer's statement is in `source` (D-std-0014)
  audience: practitioner
  subjects: inherited
- id: qaa/optometry-2024/3.13.b5
  locator: { number: "3.13.b5", headingPath: ["Content, structure and delivery", "Assessment"] }
  span: { start: 47185, end: 47197 }
  source: "transparency"
  stem: "3.13"
  statementType: requirement
  rung: none
  force: should
  level: none
  appliesTo: "assessment in Optometry courses"
  addressee: provider
  verbs: []
  about: "assessment balances transparency"
  themes: [none]
  domain: none
  award: ["integrated master's"]
  gradeOf: none
  paraphrase: "Assessment should weigh transparency against the other qualities listed: it is clear to students and staff."
  quote: full   # the issuer's statement is in `source` (D-std-0014)
  audience: practitioner
  subjects: inherited
- id: qaa/optometry-2024/3.13.b6
  locator: { number: "3.13.b6", headingPath: ["Content, structure and delivery", "Assessment"] }
  span: { start: 47200, end: 47213 }
  source: "authenticity."
  stem: "3.13"
  statementType: requirement
  rung: none
  force: should
  level: none
  appliesTo: "assessment in Optometry courses"
  addressee: provider
  verbs: []
  about: "assessment balances authenticity"
  themes: [none]
  domain: none
  award: ["integrated master's"]
  gradeOf: none
  paraphrase: "Assessment should weigh authenticity against the other qualities listed: it resembles real practice."
  quote: full   # the issuer's statement is in `source` (D-std-0014)
  audience: practitioner
  subjects: inherited
- id: qaa/optometry-2024/3.14.b1
  locator: { number: "3.14.b1", headingPath: ["Content, structure and delivery", "Assessment"] }
  span: { start: 47235, end: 47282 }
  source: "constructively aligned to the learning outcomes"
  stem: "3.14"
  statementType: requirement
  rung: none
  force: should
  level: none
  appliesTo: "assessment in Optometry courses"
  addressee: provider
  verbs: ["aligned"]
  about: "constructive alignment"
  themes: [none]
  domain: none
  award: ["integrated master's"]
  gradeOf: none
  paraphrase: "Assessment should line up with the learning outcomes it tests."
  quote: full   # the issuer's statement is in `source` (D-std-0014)
  audience: practitioner
  subjects: inherited
- id: qaa/optometry-2024/3.14.b2
  locator: { number: "3.14.b2", headingPath: ["Content, structure and delivery", "Assessment"] }
  span: { start: 47285, end: 47401 }
  source: "designed to provide formative as well as summative opportunities, as well as mechanisms for feedback and feedforward"
  stem: "3.14"
  statementType: requirement
  rung: none
  force: should
  level: none
  appliesTo: "assessment in Optometry courses"
  addressee: provider
  verbs: ["designed", "provide"]
  about: "formative and summative opportunities with feedback"
  themes: [none]
  domain: none
  award: ["integrated master's"]
  gradeOf: none
  paraphrase: "Assessment should offer formative as well as summative chances, with ways of giving feedback and feedforward."
  quote: full   # the issuer's statement is in `source` (D-std-0014)
  audience: practitioner
  subjects: inherited
- id: qaa/optometry-2024/3.14.b3
  locator: { number: "3.14.b3", headingPath: ["Content, structure and delivery", "Assessment"] }
  span: { start: 47404, end: 47429 }
  source: "inclusive and accessible."
  stem: "3.14"
  statementType: requirement
  rung: none
  force: should
  level: none
  appliesTo: "assessment in Optometry courses"
  addressee: provider
  verbs: []
  about: "inclusive, accessible assessment"
  themes: [none]
  domain: none
  award: ["integrated master's"]
  gradeOf: none
  paraphrase: "Assessment should be inclusive and accessible."
  quote: full   # the issuer's statement is in `source` (D-std-0014)
  audience: practitioner
  subjects: inherited
- id: qaa/optometry-2024/3.15
  locator: { number: "3.15", headingPath: ["Content, structure and delivery", "Assessment"] }
  span: { start: 47430, end: 47607 }
  source: "3.15 Higher education providers should ensure their assessment design and methods are evidence-based. Consideration should also be given to standard setting and moderation.\n\n16\n"
  stem: none
  statementType: requirement
  rung: none
  force: should
  level: none
  appliesTo: "higher education providers"
  addressee: provider
  verbs: ["ensure"]
  about: "evidence-based assessment design and moderation"
  themes: [none]
  domain: none
  award: ["integrated master's"]
  gradeOf: none
  paraphrase: "Providers should base assessment design and methods on evidence and should also think about standard setting and moderation."
  quote: full   # the issuer's statement is in `source` (D-std-0014)
  audience: practitioner
  subjects: inherited
- id: qaa/optometry-2024/3.16
  locator: { number: "3.16", headingPath: ["Content, structure and delivery", "Assessment"] }
  span: { start: 47607, end: 47715 }
  source: "3.16 The assessment type should be aligned to the relevant layer of Miller’s pyramid of clinical competence."
  stem: none
  statementType: requirement
  rung: none
  force: should
  level: none
  appliesTo: "assessment in Optometry courses"
  addressee: provider
  verbs: ["aligned"]
  about: "assessment matched to Miller's pyramid"
  themes: [none]
  domain: none
  award: ["integrated master's"]
  gradeOf: none
  paraphrase: "The kind of assessment should fit the layer of Miller's pyramid of clinical competence that it targets."
  quote: full   # the issuer's statement is in `source` (D-std-0014)
  audience: practitioner
  subjects: inherited
- id: qaa/optometry-2024/3.18
  locator: { number: "3.18", headingPath: ["Content, structure and delivery", "Assessment"] }
  span: { start: 49123, end: 49528 }
  source: "3.18 At registerable master's level, there is a strong emphasis on requiring students to apply their knowledge of Optometry to the solution of unfamiliar problems. Assessment of the range of research skills is also considered crucial in determining whether master's level learning outcomes have been achieved. Students should be able to demonstrate they are capable of practising evidence-based Optometry."
  stem: none
  statementType: outcome
  rung: none
  force: should
  level: fheq:7
  appliesTo: "students at registerable master's level"
  addressee: learner
  verbs: ["apply", "demonstrate"]
  about: "unfamiliar problems, research skills and evidence-based practice"
  themes: [none]
  domain: subject-skill
  award: ["integrated master's"]
  gradeOf: none
  paraphrase: "At registerable master's level the stress falls on applying Optometry knowledge to unfamiliar problems, and assessing research skills is key to judging master's outcomes; students should be able to show they can practise evidence-based Optometry."
  quote: full   # the issuer's statement is in `source` (D-std-0014)
  audience: both
  subjects: inherited
- id: qaa/optometry-2024/3.19
  locator: { number: "3.19", headingPath: ["Content, structure and delivery", "Feedback and feedforward"] }
  span: { start: 49554, end: 50012 }
  source: "3.19 Feedback and feedforward should be personal/individual, understandable, empowering, manageable and developmental. It should be timely, relevant to the\n\n17\nassessment brief and accompanied by access to interpretative support/advice. Feedback should allow students the opportunity for supportive reflection on their academic and professional development. The nature, extent and timing of feedback for each assessment task should be made clear in advance.\n"
  stem: none
  statementType: requirement
  rung: none
  force: should
  level: none
  appliesTo: "feedback and feedforward"
  addressee: provider
  verbs: ["made"]
  about: "qualities of feedback and feedforward"
  themes: [none]
  domain: none
  award: ["integrated master's"]
  gradeOf: none
  paraphrase: "Feedback and feedforward should be personal, understandable, empowering, manageable, developmental, timely and tied to the brief, with interpretive support; they should allow supportive reflection, and the nature and timing of feedback should be set out beforehand."
  quote: full   # the issuer's statement is in `source` (D-std-0014)
  audience: practitioner
  subjects: inherited
- id: qaa/optometry-2024/3.21
  locator: { number: "3.21", headingPath: ["Content, structure and delivery", "Feedback and feedforward"] }
  span: { start: 50562, end: 51119 }
  source: "3.21 By providing constructive guidance on how to enhance performance, feedforward enables learners to make improvement. When feedback and feedforward are combined, they create a powerful synergy that ensures a positive developmental impact on learning. However, for this impact to be realised, it is essential that students have the opportunity and support to develop their evaluative skills, enabling them to effectively utilise the feedback they receive. When discussing feedback, the psychological safety of the learner should always be considered.\n\n18\n"
  stem: none
  statementType: requirement
  rung: none
  force: should
  level: none
  appliesTo: "feedback practice"
  addressee: provider
  verbs: ["considered"]
  about: "feedforward, evaluative skill and psychological safety"
  themes: [none]
  domain: none
  award: ["integrated master's"]
  gradeOf: none
  paraphrase: "Feedforward helps learners improve and, joined with feedback, aids development, which needs students to have the chance and help to build evaluative skill; the learner's psychological safety should always be considered in feedback."
  quote: full   # the issuer's statement is in `source` (D-std-0014)
  audience: practitioner
  subjects: inherited
- id: qaa/optometry-2024/4.2
  locator: { number: "4.2", headingPath: ["Benchmark standards", "Introduction"] }
  span: { start: 51477, end: 51712 }
  source: "4.2 Each higher education provider has its own method of determining what appropriate evidence of this achievement will be, and should refer to Annex D in The Frameworks for Higher Education Qualifications of UK Degree-Awarding Bodies."
  stem: none
  statementType: requirement
  rung: none
  force: should
  level: none
  appliesTo: "higher education providers"
  addressee: provider
  verbs: ["refer"]
  about: "evidence of achievement judged with Annex D"
  themes: [none]
  domain: none
  award: ["integrated master's"]
  gradeOf: none
  paraphrase: "Each provider decides what counts as evidence of reaching the standards and should consult Annex D of the Frameworks for Higher Education Qualifications."
  quote: full   # the issuer's statement is in `source` (D-std-0014)
  audience: practitioner
  subjects: inherited
- id: qaa/optometry-2024/4.4.b1
  locator: { number: "4.4.b1", headingPath: ["Benchmark standards", "Threshold level: subject knowledge, understanding and skills"] }
  span: { start: 52284, end: 52684 }
  source: "Person-centred care: Graduates should possess the skill to apply a flexible and individualised approach to patient care, taking into account the patient's social, clinical, personal and cultural requirements, all while actively questioning and addressing any conscious and unconscious biases they may have. When necessary, they should be capable of collaborating efficiently with other professionals."
  stem: "4.4"
  statementType: threshold
  rung: threshold
  force: threshold
  level: fheq:7
  appliesTo: "graduates at the threshold"
  addressee: learner
  verbs: ["apply", "questioning", "addressing", "collaborating"]
  about: "person-centred care"
  themes: [none]
  domain: subject-skill
  award: ["integrated master's"]
  gradeOf: none
  paraphrase: "Person-centred care: will tailor care to each patient's social, clinical, personal and cultural needs while challenging their own conscious and unconscious biases, and work well with other professionals when needed."
  quote: full   # the issuer's statement is in `source` (D-std-0014)
  audience: both
  subjects: inherited
- id: qaa/optometry-2024/4.4.b2
  locator: { number: "4.4.b2", headingPath: ["Benchmark standards", "Threshold level: subject knowledge, understanding and skills"] }
  span: { start: 52685, end: 53097 }
  source: "Communication: Graduates need to demonstrate strong communication skills, both with patients and other professionals. They should be adaptable in their approach, adjusting their style to suit the specific needs of each individual and facilitating the attainment of desired outcomes. This involves proficiency in written and verbal communication, as well as the ability to perceive and understand non-verbal cues."
  stem: "4.4"
  statementType: threshold
  rung: threshold
  force: threshold
  level: fheq:7
  appliesTo: "graduates at the threshold"
  addressee: learner
  verbs: ["demonstrate", "adjusting", "perceive", "understand"]
  about: "communication"
  themes: [none]
  domain: generic-skill
  award: ["integrated master's"]
  gradeOf: none
  paraphrase: "Communication: will show strong communication with patients and professionals, adapting style to each person and to the outcome sought, in writing and speech, and reading non-verbal cues."
  quote: full   # the issuer's statement is in `source` (D-std-0014)
  audience: both
  subjects: inherited
- id: qaa/optometry-2024/4.4.b3
  locator: { number: "4.4.b3", headingPath: ["Benchmark standards", "Threshold level: subject knowledge, understanding and skills"] }
  span: { start: 53098, end: 53434 }
  source: "Clinical practice: Graduates work within their individual scope of practice, assuming professional accountability and personal responsibility for achieving desired patient outcomes. They must operate within their limits of competence and exercise professional judgment while making evidence-informed clinical decisions for all patients."
  stem: "4.4"
  statementType: threshold
  rung: threshold
  force: threshold
  level: fheq:7
  appliesTo: "graduates at the threshold"
  addressee: learner
  verbs: ["work", "operate", "exercise", "making"]
  about: "clinical practice within scope"
  themes: [none]
  domain: subject-skill
  award: ["integrated master's"]
  gradeOf: none
  paraphrase: "Clinical practice: will work within their own scope of practice, accountable for patient outcomes, keeping within their competence and using professional judgement in evidence-informed decisions for every patient."
  quote: full   # the issuer's statement is in `source` (D-std-0014)
  audience: both
  subjects: inherited
- id: qaa/optometry-2024/4.4.b4
  locator: { number: "4.4.b4", headingPath: ["Benchmark standards", "Threshold level: subject knowledge, understanding and skills"] }
  span: { start: 53435, end: 54016 }
  source: "Ethics and standards: Graduates uphold high professional standards and ethics, and are expected to demonstrate honesty, integrity and a commitment to lifelong learning. They bear the responsibility of safeguarding the care and safety of patients and the public. By adhering to their scope of practice and current legislation, such as the Opticians Act 1989 and the GOC Standards of Practice for Optometrists, graduates ensure that their own practice, including supervised and delegated activities, complies with all legal and professional obligations and promotes fairness for all."
  stem: "4.4"
  statementType: threshold
  rung: threshold
  force: threshold
  level: fheq:7
  appliesTo: "graduates at the threshold"
  addressee: learner
  verbs: ["uphold", "demonstrate", "safeguarding", "ensure"]
  about: "ethics and standards"
  themes: [none]
  domain: subject-skill
  award: ["integrated master's"]
  gradeOf: none
  paraphrase: "Ethics and standards: will keep high professional and ethical standards, show honesty, integrity and commitment to learning, safeguard patients and the public, and keep their own and delegated practice within the law, professional duties and fairness."
  quote: full   # the issuer's statement is in `source` (D-std-0014)
  audience: both
  subjects: inherited
- id: qaa/optometry-2024/4.4.b5
  locator: { number: "4.4.b5", headingPath: ["Benchmark standards", "Threshold level: subject knowledge, understanding and skills"] }
  span: { start: 54017, end: 54549 }
  source: "Risk: Graduates bear the responsibility for safeguarding patients, colleagues and others, taking proactive measures to protect them from harm. They must possess a clear understanding of their own capabilities and operate within their competence, acknowledging that their professional practice evolves over time. Graduates should be\n\n19\nadept at recognising situations where individuals may be at risk and should exhibit transparency and candour in admitting mistakes, thereby creating a safe environment for patients and the public."
  stem: "4.4"
  statementType: threshold
  rung: threshold
  force: threshold
  level: fheq:7
  appliesTo: "graduates at the threshold"
  addressee: learner
  verbs: ["safeguarding", "protect", "operate", "recognising", "admitting"]
  about: "risk and safeguarding"
  themes: [none]
  domain: subject-skill
  award: ["integrated master's"]
  gradeOf: none
  paraphrase: "Risk: will safeguard patients, colleagues and others with proactive protection, know and keep within their own capabilities as practice develops, recognise when people may be at risk, and be open and candid about mistakes."
  quote: full   # the issuer's statement is in `source` (D-std-0014)
  audience: both
  subjects: inherited
- id: qaa/optometry-2024/4.4.b6
  locator: { number: "4.4.b6", headingPath: ["Benchmark standards", "Threshold level: subject knowledge, understanding and skills"] }
  span: { start: 54550, end: 54983 }
  source: "Leadership and management: Graduates must exercise clinical leadership within the context of their scope of practice. They should operate within their area of expertise and competence to achieve desired patient outcomes. They will collaborate with healthcare teams and other professionals to actively support and participate in clinical governance requirements, service enhancements, and local and national public health initiatives."
  stem: "4.4"
  statementType: threshold
  rung: threshold
  force: threshold
  level: fheq:7
  appliesTo: "graduates at the threshold"
  addressee: learner
  verbs: ["exercise", "operate", "collaborate", "support", "participate"]
  about: "leadership and management"
  themes: [none]
  domain: subject-skill
  award: ["integrated master's"]
  gradeOf: none
  paraphrase: "Leadership and management: will lead clinically within their scope and expertise to reach good patient outcomes, and will work with healthcare teams to support governance, service improvement and local and national public health work."
  quote: full   # the issuer's statement is in `source` (D-std-0014)
  audience: both
  subjects: inherited
- id: qaa/optometry-2024/4.4.b7
  locator: { number: "4.4.b7", headingPath: ["Benchmark standards", "Threshold level: subject knowledge, understanding and skills"] }
  span: { start: 54984, end: 55336 }
  source: "Lifelong learning: Graduates are personally accountable for their continuing professional development, ensuring the maintenance of up-to-date knowledge and skills within their scope of practice. They must undertake an ongoing process of reflection to evaluate their own performance and that of their peers, identifying areas for growth and improvement."
  stem: "4.4"
  statementType: threshold
  rung: threshold
  force: threshold
  level: fheq:7
  appliesTo: "graduates at the threshold"
  addressee: learner
  verbs: ["ensuring", "undertake", "evaluate"]
  about: "lifelong learning"
  themes: [none]
  domain: generic-skill
  award: ["integrated master's"]
  gradeOf: none
  paraphrase: "Lifelong learning: will own their continuing professional development, keep knowledge and skills current within their scope, and reflect continually on their own and peers' performance to find room to grow."
  quote: full   # the issuer's statement is in `source` (D-std-0014)
  audience: both
  subjects: inherited
- id: qaa/optometry-2024/4.5.b1
  locator: { number: "4.5.b1", headingPath: ["Benchmark standards", "Threshold level: generic skills"] }
  span: { start: 55508, end: 55547 }
  source: "identify issues, questions and problems"
  stem: "4.5"
  statementType: threshold
  rung: threshold
  force: should
  level: fheq:7
  appliesTo: "graduates of the master's"
  addressee: learner
  verbs: ["identify"]
  about: "identifying issues and problems"
  themes: [none]
  domain: generic-skill
  award: ["integrated master's"]
  gradeOf: none
  paraphrase: "On graduating, students should be able to identify the issues, questions and problems in a situation."
  quote: full   # the issuer's statement is in `source` (D-std-0014)
  audience: both
  subjects: inherited
- id: qaa/optometry-2024/4.5.b2
  locator: { number: "4.5.b2", headingPath: ["Benchmark standards", "Threshold level: generic skills"] }
  span: { start: 55550, end: 55644 }
  source: "apply knowledge, understanding and critical thinking to provide evidence-based decision-making"
  stem: "4.5"
  statementType: threshold
  rung: threshold
  force: should
  level: fheq:7
  appliesTo: "graduates of the master's"
  addressee: learner
  verbs: ["apply"]
  about: "evidence-based decision-making"
  themes: [none]
  domain: generic-skill
  award: ["integrated master's"]
  gradeOf: none
  paraphrase: "On graduating, students should be able to use knowledge, understanding and critical thinking to make decisions based on evidence."
  quote: full   # the issuer's statement is in `source` (D-std-0014)
  audience: both
  subjects: inherited
- id: qaa/optometry-2024/4.5.b3
  locator: { number: "4.5.b3", headingPath: ["Benchmark standards", "Threshold level: generic skills"] }
  span: { start: 55647, end: 55709 }
  source: "identify gaps in their own knowledge and acquire new knowledge"
  stem: "4.5"
  statementType: threshold
  rung: threshold
  force: should
  level: fheq:7
  appliesTo: "graduates of the master's"
  addressee: learner
  verbs: ["identify", "acquire"]
  about: "finding and closing gaps in knowledge"
  themes: [none]
  domain: generic-skill
  award: ["integrated master's"]
  gradeOf: none
  paraphrase: "On graduating, students should be able to spot where their own knowledge falls short and learn what is missing."
  quote: full   # the issuer's statement is in `source` (D-std-0014)
  audience: both
  subjects: inherited
- id: qaa/optometry-2024/4.5.b4
  locator: { number: "4.5.b4", headingPath: ["Benchmark standards", "Threshold level: generic skills"] }
  span: { start: 55712, end: 55798 }
  source: "critically appraise and apply the research literature and other sources of information"
  stem: "4.5"
  statementType: threshold
  rung: threshold
  force: should
  level: fheq:7
  appliesTo: "graduates of the master's"
  addressee: learner
  verbs: ["appraise", "apply"]
  about: "appraising and applying research"
  themes: [none]
  domain: generic-skill
  award: ["integrated master's"]
  gradeOf: none
  paraphrase: "On graduating, students should be able to judge research and other sources critically and put them to use."
  quote: full   # the issuer's statement is in `source` (D-std-0014)
  audience: both
  subjects: inherited
- id: qaa/optometry-2024/4.5.b5
  locator: { number: "4.5.b5", headingPath: ["Benchmark standards", "Threshold level: generic skills"] }
  span: { start: 55801, end: 55942 }
  source: "demonstrate an understanding of how established techniques of research and enquiry are used to create and interpret knowledge in a discipline"
  stem: "4.5"
  statementType: threshold
  rung: threshold
  force: should
  level: fheq:7
  appliesTo: "graduates of the master's"
  addressee: learner
  verbs: ["demonstrate"]
  about: "how research creates knowledge"
  themes: [none]
  domain: generic-skill
  award: ["integrated master's"]
  gradeOf: none
  paraphrase: "On graduating, students should be able to show they understand how established research and enquiry methods produce and interpret disciplinary knowledge."
  quote: full   # the issuer's statement is in `source` (D-std-0014)
  audience: both
  subjects: inherited
- id: qaa/optometry-2024/4.5.b6
  locator: { number: "4.5.b6", headingPath: ["Benchmark standards", "Threshold level: generic skills"] }
  span: { start: 55945, end: 56021 }
  source: "engage in reflective practice to support continuing professional development"
  stem: "4.5"
  statementType: threshold
  rung: threshold
  force: should
  level: fheq:7
  appliesTo: "graduates of the master's"
  addressee: learner
  verbs: ["engage", "support"]
  about: "reflective practice for CPD"
  themes: [none]
  domain: generic-skill
  award: ["integrated master's"]
  gradeOf: none
  paraphrase: "On graduating, students should be able to practise reflection to support continuing professional development."
  quote: full   # the issuer's statement is in `source` (D-std-0014)
  audience: both
  subjects: inherited
- id: qaa/optometry-2024/4.5.b7
  locator: { number: "4.5.b7", headingPath: ["Benchmark standards", "Threshold level: generic skills"] }
  span: { start: 56024, end: 56104 }
  source: "demonstrate effective and appropriate verbal and non-verbal communication skills"
  stem: "4.5"
  statementType: threshold
  rung: threshold
  force: should
  level: fheq:7
  appliesTo: "graduates of the master's"
  addressee: learner
  verbs: ["demonstrate"]
  about: "verbal and non-verbal communication"
  themes: [none]
  domain: generic-skill
  award: ["integrated master's"]
  gradeOf: none
  paraphrase: "On graduating, students should be able to communicate effectively and appropriately with and without words."
  quote: full   # the issuer's statement is in `source` (D-std-0014)
  audience: both
  subjects: inherited
- id: qaa/optometry-2024/4.5.b8
  locator: { number: "4.5.b8", headingPath: ["Benchmark standards", "Threshold level: generic skills"] }
  span: { start: 56107, end: 56222 }
  source: "work with a range of data and engage with a range of forms of digital technology to collate and analyse information"
  stem: "4.5"
  statementType: threshold
  rung: threshold
  force: should
  level: fheq:7
  appliesTo: "graduates of the master's"
  addressee: learner
  verbs: ["work", "engage", "collate", "analyse"]
  about: "data and digital technology"
  themes: [none]
  domain: generic-skill
  award: ["integrated master's"]
  gradeOf: none
  paraphrase: "On graduating, students should be able to handle a range of data and digital tools to gather and analyse information."
  quote: full   # the issuer's statement is in `source` (D-std-0014)
  audience: both
  subjects: inherited
- id: qaa/optometry-2024/4.5.b9
  locator: { number: "4.5.b9", headingPath: ["Benchmark standards", "Threshold level: generic skills"] }
  span: { start: 56225, end: 56253 }
  source: "adapt to changing technology"
  stem: "4.5"
  statementType: threshold
  rung: threshold
  force: should
  level: fheq:7
  appliesTo: "graduates of the master's"
  addressee: learner
  verbs: ["adapt"]
  about: "adapting to changing technology"
  themes: [none]
  domain: generic-skill
  award: ["integrated master's"]
  gradeOf: none
  paraphrase: "On graduating, students should be able to adjust to technology as it changes."
  quote: full   # the issuer's statement is in `source` (D-std-0014)
  audience: both
  subjects: inherited
- id: qaa/optometry-2024/4.5.b10
  locator: { number: "4.5.b10", headingPath: ["Benchmark standards", "Threshold level: generic skills"] }
  span: { start: 56256, end: 56356 }
  source: "work collaboratively, including undertaking work in a group or team and participating in discussions"
  stem: "4.5"
  statementType: threshold
  rung: threshold
  force: should
  level: fheq:7
  appliesTo: "graduates of the master's"
  addressee: learner
  verbs: ["work"]
  about: "collaborative working"
  themes: [none]
  domain: generic-skill
  award: ["integrated master's"]
  gradeOf: none
  paraphrase: "On graduating, students should be able to work with others, in groups or teams and in discussion."
  quote: full   # the issuer's statement is in `source` (D-std-0014)
  audience: both
  subjects: inherited
- id: qaa/optometry-2024/4.5.b11
  locator: { number: "4.5.b11", headingPath: ["Benchmark standards", "Threshold level: generic skills"] }
  span: { start: 56359, end: 56476 }
  source: "integrate relevant theory and practice in the areas of equality, diversity and inclusion into the working environment"
  stem: "4.5"
  statementType: threshold
  rung: threshold
  force: should
  level: fheq:7
  appliesTo: "graduates of the master's"
  addressee: learner
  verbs: ["integrate"]
  about: "equality, diversity and inclusion at work"
  themes: [none]
  domain: generic-skill
  award: ["integrated master's"]
  gradeOf: none
  paraphrase: "On graduating, students should be able to bring theory and practice of equality, diversity and inclusion into the workplace."
  quote: full   # the issuer's statement is in `source` (D-std-0014)
  audience: both
  subjects: inherited
- id: qaa/optometry-2024/4.5.b12
  locator: { number: "4.5.b12", headingPath: ["Benchmark standards", "Threshold level: generic skills"] }
  span: { start: 56479, end: 56601 }
  source: "internalise and act on the importance of well-being, mental health and emotions and their relationship with their learning"
  stem: "4.5"
  statementType: threshold
  rung: threshold
  force: should
  level: fheq:7
  appliesTo: "graduates of the master's"
  addressee: learner
  verbs: ["internalise", "act"]
  about: "well-being and its link to learning"
  themes: [none]
  domain: generic-skill
  award: ["integrated master's"]
  gradeOf: none
  paraphrase: "On graduating, students should be able to take to heart how well-being, mental health and emotion bear on learning, and act on it."
  quote: full   # the issuer's statement is in `source` (D-std-0014)
  audience: both
  subjects: inherited
- id: qaa/optometry-2024/4.5.b13
  locator: { number: "4.5.b13", headingPath: ["Benchmark standards", "Threshold level: generic skills"] }
  span: { start: 56604, end: 56745 }
  source: "apply sustainable approaches to working, including waste management, recycling, and environmentally conscious working procedures and policies"
  stem: "4.5"
  statementType: threshold
  rung: threshold
  force: should
  level: fheq:7
  appliesTo: "graduates of the master's"
  addressee: learner
  verbs: ["apply"]
  about: "sustainable working"
  themes: [none]
  domain: generic-skill
  award: ["integrated master's"]
  gradeOf: none
  paraphrase: "On graduating, students should be able to use sustainable ways of working, from waste and recycling to environmentally aware procedures."
  quote: full   # the issuer's statement is in `source` (D-std-0014)
  audience: both
  subjects: inherited
- id: qaa/optometry-2024/4.5.b14
  locator: { number: "4.5.b14", headingPath: ["Benchmark standards", "Threshold level: generic skills"] }
  span: { start: 56748, end: 56880 }
  source: "identify, question and challenge cultural and ethnocentric assumptions and premises, and appreciate other ways of being in the world"
  stem: "4.5"
  statementType: threshold
  rung: threshold
  force: should
  level: fheq:7
  appliesTo: "graduates of the master's"
  addressee: learner
  verbs: ["identify", "question", "challenge", "appreciate"]
  about: "challenging cultural assumptions"
  themes: [none]
  domain: generic-skill
  award: ["integrated master's"]
  gradeOf: none
  paraphrase: "On graduating, students should be able to recognise and challenge cultural and ethnocentric assumptions and value other ways of being."
  quote: full   # the issuer's statement is in `source` (D-std-0014)
  audience: both
  subjects: inherited
- id: qaa/optometry-2024/4.5.b15
  locator: { number: "4.5.b15", headingPath: ["Benchmark standards", "Threshold level: generic skills"] }
  span: { start: 56883, end: 56945 }
  source: "demonstrate an awareness of business and commercial operations"
  stem: "4.5"
  statementType: threshold
  rung: threshold
  force: should
  level: fheq:7
  appliesTo: "graduates of the master's"
  addressee: learner
  verbs: ["demonstrate"]
  about: "business and commercial awareness"
  themes: [none]
  domain: generic-skill
  award: ["integrated master's"]
  gradeOf: none
  paraphrase: "On graduating, students should be able to show awareness of how business and commercial operations work."
  quote: full   # the issuer's statement is in `source` (D-std-0014)
  audience: both
  subjects: inherited
- id: qaa/optometry-2024/4.5.b16
  locator: { number: "4.5.b16", headingPath: ["Benchmark standards", "Threshold level: generic skills"] }
  span: { start: 56948, end: 57071 }
  source: "display creativity and originality both in problem-solving and in the development and communication of ideas and arguments."
  stem: "4.5"
  statementType: threshold
  rung: threshold
  force: should
  level: fheq:7
  appliesTo: "graduates of the master's"
  addressee: learner
  verbs: ["display"]
  about: "creativity and originality"
  themes: [none]
  domain: generic-skill
  award: ["integrated master's"]
  gradeOf: none
  paraphrase: "On graduating, students should be able to show creativity and originality in solving problems and in developing and communicating ideas."
  quote: full   # the issuer's statement is in `source` (D-std-0014)
  audience: both
  subjects: inherited
```

### S4a Audience versions
<!-- label: both; status: drafted; basis: primary. forPractitioner: for the programme designer or teacher. forBeneficiary: for the student, second person, naming no issuer. author-agent-written: instructions to an AI agent writing about the statement (a course document, a handbook, an outcome, a report). author-agent-dialogue: instructions to an AI agent using the statement in conversation (with a student, a teacher or a programme team). Written fresh from the held text alone (benchmark rule 6; Abbott, 15:42). -->
```yaml
- statement: qaa/optometry-2024/1.7
  forPractitioner: { text: "Sequence the course so that students will build the capability to manage ever more complex patients: theory with observed and simulated clinics early on, more complexity and learner autonomy later.", rewrite: light, force: will, status: drafted }
  forBeneficiary: { text: "You will build up your ability to care for patients with more complex needs, starting with theory, observation and simulation and taking on more independence as the course goes on.", rewrite: full, force: will, status: drafted }
  author-agent-written: "Describe this as an expected outcome ('will'): the course builds clinical capability in steps towards complex patients and learner autonomy, set for the registrable integrated master's in Optometry (FHEQ Level 7; FQHEIS Level 11). Cite it as QAA (2024) Optometry Subject Benchmark Statement, para 1.7. Do not claim that a spiral design is mandatory, since the paragraph says it is typical. Set it beside 2.3, 2.7 and 3.7 (the same progression), and qaa/fheq-2024/4.17.b6 with spine:7 for the autonomy it leads to."
  author-agent-dialogue: "Raise this when a student asks why the early stages feel theoretical, or a team plans the order of clinical work. With a student, use plain words and the second person; with staff, frame it as what the course has to let every graduate show. Ask: Which kinds of patient do you feel ready to see now, and which not yet? Avoid reading the issuer's paragraph aloud and avoid implying that a student should already manage complex cases early in the course."
- statement: qaa/optometry-2024/1.10
  forPractitioner: { text: "Graduates will be able to balance evidence-based decisions with the needs of the individual patient, personalising clinical interactions while keeping care grounded in fact.", rewrite: light, force: will, status: drafted }
  forBeneficiary: { text: "You will be able to adapt how you deal with each patient to their needs while keeping your clinical decisions firmly based on evidence.", rewrite: full, force: will, status: drafted }
  author-agent-written: "Describe this as an expected outcome ('will'): graduates can personalise clinical interactions while keeping care evidence-based, framed within the equality theme, set for the registrable integrated master's in Optometry (FHEQ Level 7; FQHEIS Level 11). Cite it as QAA (2024) Optometry Subject Benchmark Statement, para 1.10. Do not claim that the statement itself is a regulatory requirement, or that it covers non-registrable vision science awards. Set it beside 4.4.b1 (person-centred care at threshold), 3.5.b1, and qaa/fheq-2024/4.17.b5 for judgement in complex cases."
  author-agent-dialogue: "Raise this when a student or team discusses balancing protocol and evidence against what a particular patient needs or prefers. With a student, use plain words and the second person; with staff, frame it as what the course has to let every graduate show. Ask: Can you recall a patient where the evidence pointed one way and their circumstances another, and how you handled it? Avoid reading the issuer's paragraph aloud and avoid suggesting that personalising care means departing from the evidence."
- statement: qaa/optometry-2024/1.11
  forPractitioner: { text: "Build into the curriculum the contributions of scientists and practitioners of diverse backgrounds and identities, and give learners scope to explore Optometry topics linked to their aspirations, lived experience or culture.", rewrite: light, force: should, status: drafted }
  forBeneficiary: { text: "not-applicable: a duty on the course in shaping its curriculum; the student meets its effect", rewrite: full, force: should, status: drafted }
  author-agent-written: "Describe this as a recommendation ('should'): curricula credit diverse contributors to the field and leave room for learners to follow their own interests, set for the registrable integrated master's in Optometry (FHEQ Level 7; FQHEIS Level 11). Cite it as QAA (2024) Optometry Subject Benchmark Statement, para 1.11. Do not claim that the statement itself is a regulatory requirement, or that it covers non-registrable vision science awards. Set it beside 1.9 and 1.13 (the equality theme) and 4.5.b14 (challenging cultural assumptions)."
  author-agent-dialogue: "Raise this when a team reviews reading lists, case material or project choice for representation. Frame it for the programme team or teacher as a duty on the course, in their own planning terms. Ask: Whose discoveries does the module currently present, and where could learners choose topics that matter to them? Avoid reading the issuer's paragraph aloud and avoid putting it to a student as something they must achieve, since it is a duty on the course."
- statement: qaa/optometry-2024/1.13
  forPractitioner: { text: "Make sure the curriculum shows students a broad range of patient experiences and presentations, so they can care well for patients across the whole of the UK.", rewrite: light, force: should, status: drafted }
  forBeneficiary: { text: "not-applicable: a duty on the course in choosing its content", rewrite: full, force: should, status: drafted }
  author-agent-written: "Describe this as a recommendation ('should'): the curriculum brings students into contact with a wide range of patients and presentations, set for the registrable integrated master's in Optometry (FHEQ Level 7; FQHEIS Level 11). Cite it as QAA (2024) Optometry Subject Benchmark Statement, para 1.13. Do not claim that the statement itself is a regulatory requirement, or that it covers non-registrable vision science awards. Set it beside 1.10 (personalised care), 3.2.b14 (social determinants and disparities in content) and 4.4.b1."
  author-agent-dialogue: "Raise this when a team plans clinical cases, simulations or placements. Frame it for the programme team or teacher as a duty on the course, in their own planning terms. Ask: Which patient groups and presentations are missing from the cases students meet now? Avoid reading the issuer's paragraph aloud and avoid putting it to a student as something they must achieve, since it is a duty on the course."
- statement: qaa/optometry-2024/1.14
  forPractitioner: { text: "Design learning and assessment to be inclusive by default and add reasonable individual adjustments where needed; keep patient protection and the regulator's standards intact while meeting the Equality Act 2010.", rewrite: light, force: should, status: drafted }
  forBeneficiary: { text: "not-applicable: a duty on the course; the student meets its effect through accessible design and adjustments", rewrite: full, force: should, status: drafted }
  author-agent-written: "Describe this as a recommendation ('should'): courses make learning and assessment equally accessible by inclusive design and reasonable adjustment, without compromising patient safety or the regulator's standards, set for the registrable integrated master's in Optometry (FHEQ Level 7; FQHEIS Level 11). Cite it as QAA (2024) Optometry Subject Benchmark Statement, para 1.14. Do not claim that the statement itself is a regulatory requirement, or that it covers non-registrable vision science awards; it does not lower any competence standard. Set it beside 1.15, 1.16 and 3.11 (the accessibility theme) and 3.14.b3."
  author-agent-dialogue: "Raise this when a team designs an assessment or considers an adjustment request. Frame it for the programme team or teacher as a duty on the course, in their own planning terms. Ask: Is this built in for everyone, or does it rely on individual adjustments, and does either affect patient safety? Avoid reading the issuer's paragraph aloud and avoid putting it to a student as something they must achieve, since it is a duty on the course."
- statement: qaa/optometry-2024/1.15
  forPractitioner: { text: "Use a variety of learning and assessment experiences, both to reflect the breadth of the subject and to open access, so that students of every background and ability can contribute.", rewrite: light, force: should, status: drafted }
  forBeneficiary: { text: "not-applicable: a duty on the course in designing learning and assessment", rewrite: full, force: should, status: drafted }
  author-agent-written: "Describe this as a recommendation ('should'): learning and assessment are kept varied for the sake of access and of a diverse student body, set for the registrable integrated master's in Optometry (FHEQ Level 7; FQHEIS Level 11). Cite it as QAA (2024) Optometry Subject Benchmark Statement, para 1.15. Do not claim that the statement itself is a regulatory requirement, or that it covers non-registrable vision science awards. Set it beside 1.14, 1.16 and 3.13 (the balance assessment seeks)."
  author-agent-dialogue: "Raise this when a team reviews the mix of assessment types in a year or module. Frame it for the programme team or teacher as a duty on the course, in their own planning terms. Ask: How many different ways can a student show this outcome, and who might each format shut out? Avoid reading the issuer's paragraph aloud and avoid putting it to a student as something they must achieve, since it is a duty on the course."
- statement: qaa/optometry-2024/1.16
  forPractitioner: { text: "Check that every part of the course, clinical work included, is accessible by design without compromising patient safety, and support learners in developing the verbal, spatial and numerical skills they need.", rewrite: light, force: should, status: drafted }
  forBeneficiary: { text: "not-applicable: a duty on the course team", rewrite: full, force: should, status: drafted }
  author-agent-written: "Describe this as a recommendation ('should'): course teams design curricula, pedagogy, assessment and clinics to be accessible while protecting patients, set for the registrable integrated master's in Optometry (FHEQ Level 7; FQHEIS Level 11). Cite it as QAA (2024) Optometry Subject Benchmark Statement, para 1.16. Do not claim that the statement itself is a regulatory requirement, or that it covers non-registrable vision science awards. Set it beside 1.14 and 1.15 (the accessibility theme) and 2.14 (practical sessions)."
  author-agent-dialogue: "Raise this when a team plans a clinical session or practical assessment. Frame it for the programme team or teacher as a duty on the course, in their own planning terms. Ask: Where in this clinic or practical could a disabled student meet a barrier, and how would you remove it safely? Avoid reading the issuer's paragraph aloud and avoid putting it to a student as something they must achieve, since it is a duty on the course."
- statement: qaa/optometry-2024/1.17
  forPractitioner: { text: "Inspire students to engage with personal, human and global challenges to visual health; topics from the UN Sustainable Development Goals, especially health and environment, may be used, so graduates can innovate for community and global health.", rewrite: light, force: should, status: drafted }
  forBeneficiary: { text: "Your course should inspire you to tackle wider challenges in visual health, such as those in the global goals for health and the environment, and give you skills to find new answers to complex problems.", rewrite: full, force: should, status: drafted }
  author-agent-written: "Describe this as a recommendation ('should'): courses inspire engagement with sustainability and global health challenges, with the UN goals as a possible source of topics, set for the registrable integrated master's in Optometry (FHEQ Level 7; FQHEIS Level 11). Cite it as QAA (2024) Optometry Subject Benchmark Statement, para 1.17. Do not claim that the statement itself is a regulatory requirement, or that it covers non-registrable vision science awards, or that the UN goals are compulsory content. Set it beside 2.24 (embedding ESD in review), 4.5.b13 (sustainable working) and std:doc:qaa-advancehe-esd-2021-guidance."
  author-agent-dialogue: "Raise this when a student asks how sustainability relates to eye care, or a team looks for places to embed it. With a student, use plain words and the second person; with staff, frame it as what the course has to let every graduate show. Ask: Where do health inequalities or environmental costs show up in the eye care you have seen? Avoid reading the issuer's paragraph aloud and avoid presenting the global goals as a syllabus every course must teach."
- statement: qaa/optometry-2024/1.18
  forPractitioner: { text: "Equip students not only with the discipline knowledge and professional skills for clinical practice but also with wider attributes for careers in other roles and sectors, and for contributing to society.", rewrite: light, force: should, status: drafted }
  forBeneficiary: { text: "Your course should prepare you for life after you graduate, both for a clinical career and for other roles, with the wider skills and qualities that let you contribute to society.", rewrite: full, force: should, status: drafted }
  author-agent-written: "Describe this as a recommendation ('should'): courses prepare students for clinical careers and for roles elsewhere, set for the registrable integrated master's in Optometry (FHEQ Level 7; FQHEIS Level 11). Cite it as QAA (2024) Optometry Subject Benchmark Statement, para 1.18. Do not claim that the statement itself is a regulatory requirement, or that it covers non-registrable vision science awards. Set it beside 1.19 to 1.22 (enterprise), 2.18 (employability strategy), 4.5.b15 and qaa/fheq-2024/4.17.b8.1."
  author-agent-dialogue: "Raise this when a student wonders about careers beyond the consulting room, or a team reviews employability provision. With a student, use plain words and the second person; with staff, frame it as what the course has to let every graduate show. Ask: Which roles outside clinical practice interest you, and which of your skills would carry over? Avoid reading the issuer's paragraph aloud and avoid implying that a clinical career is the only valid outcome."
- statement: qaa/optometry-2024/1.19
  forPractitioner: { text: "Integrate enterprise and entrepreneurship education into the course, reflecting that many registrants work in commercial, manufacturing or charitable settings or own or franchise practices.", rewrite: light, force: should, status: drafted }
  forBeneficiary: { text: "not-applicable: a duty on the course in what it builds in", rewrite: full, force: should, status: drafted }
  author-agent-written: "Describe this as a recommendation ('should'): enterprise and entrepreneurship education is built into courses because of how the profession is organised, set for the registrable integrated master's in Optometry (FHEQ Level 7; FQHEIS Level 11). Cite it as QAA (2024) Optometry Subject Benchmark Statement, para 1.19. Do not claim that the statement itself is a regulatory requirement, or that it covers non-registrable vision science awards. Set it beside 1.20 to 1.22 (what enterprise covers), 4.5.b15 and std:doc:qaa-enterprise-2018-guidance."
  author-agent-dialogue: "Raise this when a team plans business, practice management or innovation content. Frame it for the programme team or teacher as a duty on the course, in their own planning terms. Ask: Where do students currently meet the business side of practice, and is it assessed? Avoid reading the issuer's paragraph aloud and avoid putting it to a student as something they must achieve, since it is a duty on the course."
- statement: qaa/optometry-2024/2.2
  forPractitioner: { text: "Every graduate must finish a long stretch of learning integrated with practice; plan patient-facing work, real and simulated, to grow in volume and complexity, with placements across community, hospital or university settings.", rewrite: light, force: must, status: drafted }
  forBeneficiary: { text: "You must complete a long period of learning in real practice to meet the regulator's requirements, with more and more complex patient work as you progress and placements in different settings.", rewrite: full, force: must, status: drafted }
  author-agent-written: "Describe this as an obligation ('must'): graduates complete extended integrated learning in practice, as the regulator requires, set for the registrable integrated master's in Optometry (FHEQ Level 7; FQHEIS Level 11). Cite it as QAA (2024) Optometry Subject Benchmark Statement, para 2.2. Do not claim that the statement sets the length of the period; that is the GOC's matter. Set it beside 2.3 and 2.4 (placements), 2.14, and 4.4.b3 (clinical practice at threshold)."
  author-agent-dialogue: "Raise this when a student asks about placements or a team plans the clinical timeline. With a student, use plain words and the second person; with staff, frame it as what the course has to let every graduate show. Ask: How much patient-facing time have you had so far, and in which settings? Avoid reading the issuer's paragraph aloud and avoid quoting placement lengths, which the paragraph says vary."
- statement: qaa/optometry-2024/2.3
  forPractitioner: { text: "Give students repeated controlled practice under a fully qualified registrant until they can take on every optometrist task under delegation; assess readiness for registration and independent practice within that experience.", rewrite: light, force: will, status: drafted }
  forBeneficiary: { text: "You will practise repeatedly under supervision until you are ready to carry out all of an optometrist's tasks under delegation, and your readiness to register and practise independently will be assessed during this time.", rewrite: full, force: will, status: drafted }
  author-agent-written: "Describe this as an expected outcome ('will'): supervised practice develops students to readiness, and readiness for full registration is assessed within it, set for the registrable integrated master's in Optometry (FHEQ Level 7; FQHEIS Level 11). Cite it as QAA (2024) Optometry Subject Benchmark Statement, para 2.3. Do not claim that passing this assessment is itself registration. Set it beside 2.2, 2.4, 3.16 (Miller's \"does\" layer) and qaa/fheq-2024/4.17.b6."
  author-agent-dialogue: "Raise this when a student asks what final placements are for, or what being ready for registration means. With a student, use plain words and the second person; with staff, frame it as what the course has to let every graduate show. Ask: Which optometrist tasks can you already do under delegation, and which still need close supervision? Avoid reading the issuer's paragraph aloud and avoid telling a student they are ready to practise independently."
- statement: qaa/optometry-2024/2.7
  forPractitioner: { text: "Map each level's knowledge, expertise and experience onto the threshold subject-specific and generic skills (4.4, 4.5); progression will usually need credit for every element, practical components included.", rewrite: light, force: will, status: drafted }
  forBeneficiary: { text: "You will move up through the levels of your course as you meet its rules and the regulator's, each level building towards the threshold skills, usually by passing every part, practical work included.", rewrite: full, force: will, status: drafted }
  author-agent-written: "Describe this as an expected outcome ('will'): each level of the course builds towards the threshold skills listed in 4.4 and 4.5, set for the registrable integrated master's in Optometry (FHEQ Level 7; FQHEIS Level 11). Cite it as QAA (2024) Optometry Subject Benchmark Statement, para 2.7. Do not claim that it sets progression rules; those are the institution's and the regulator's. Set it beside 4.4.b1 to 4.4.b7, 4.5.b1 to 4.5.b16, 2.11 (progression rules) and spine:7."
  author-agent-dialogue: "Raise this when a student asks what they need to progress, or a team maps level outcomes. With a student, use plain words and the second person; with staff, frame it as what the course has to let every graduate show. Ask: For your current level, which of the threshold skills are you building, and which parts are practical? Avoid reading the issuer's paragraph aloud and avoid stating an institution's progression rules as if they came from this paragraph."
- statement: qaa/optometry-2024/2.9
  forPractitioner: { text: "Base the curriculum on Miller's pyramid, starting with applying knowledge of simple concepts to well-defined problems and moving to complex patient scenarios that call for analysis, evaluation and clinical problem-solving.", rewrite: light, force: should, status: drafted }
  forBeneficiary: { text: "not-applicable: a duty on the course in its design", rewrite: full, force: should, status: drafted }
  author-agent-written: "Describe this as a recommendation ('should'): course design follows Miller's pyramid from simple, well-defined problems to complex clinical scenarios, set for the registrable integrated master's in Optometry (FHEQ Level 7; FQHEIS Level 11). Cite it as QAA (2024) Optometry Subject Benchmark Statement, para 2.9. Do not claim that the statement itself is a regulatory requirement, or that it covers non-registrable vision science awards; name the pyramid as a design model, not a standard. Set it beside 3.16 (assessment by the same pyramid), 1.7 and qaa/fheq-2024/4.17.b5."
  author-agent-dialogue: "Raise this when a team sequences modules or writes level outcomes. Frame it for the programme team or teacher as a duty on the course, in their own planning terms. Ask: Which layer of the pyramid does each year aim at, and does the assessment match it? Avoid reading the issuer's paragraph aloud and avoid putting it to a student as something they must achieve, since it is a duty on the course."
- statement: qaa/optometry-2024/2.10.b1
  forPractitioner: { text: "Make the course's progression strategies allow for students' varied prior experience and for the challenges of transition.", rewrite: light, force: should, status: drafted }
  forBeneficiary: { text: "not-applicable: a duty on the course in its strategies", rewrite: full, force: should, status: drafted }
  author-agent-written: "Describe this as a recommendation ('should'): progression strategies allow for diverse prior experience and transition, set for the registrable integrated master's in Optometry (FHEQ Level 7; FQHEIS Level 11). Cite it as QAA (2024) Optometry Subject Benchmark Statement, para 2.10 (first item). Do not claim that the statement itself is a regulatory requirement, or that it covers non-registrable vision science awards. Set it beside 2.10.b2 to 2.10.b4, 2.1 (entry routes) and 3.7."
  author-agent-dialogue: "Raise this when a team plans induction or the first year. Frame it for the programme team or teacher as a duty on the course, in their own planning terms. Ask: What do students arriving by different routes already know, and where does the first term assume too much? Avoid reading the issuer's paragraph aloud and avoid putting it to a student as something they must achieve, since it is a duty on the course."
- statement: qaa/optometry-2024/2.10.b2
  forPractitioner: { text: "Shape progression strategies so that all students can fulfil their potential and ambitions, regardless of background or motivation.", rewrite: light, force: should, status: drafted }
  forBeneficiary: { text: "not-applicable: a duty on the course in its strategies", rewrite: full, force: should, status: drafted }
  author-agent-written: "Describe this as a recommendation ('should'): progression strategies give every student an equal chance to reach their potential, set for the registrable integrated master's in Optometry (FHEQ Level 7; FQHEIS Level 11). Cite it as QAA (2024) Optometry Subject Benchmark Statement, para 2.10 (second item). Do not claim that the statement itself is a regulatory requirement, or that it covers non-registrable vision science awards. Set it beside 2.10.b1, 1.9 (equality) and 1.14."
  author-agent-dialogue: "Raise this when a team reviews attainment gaps between groups of students. Frame it for the programme team or teacher as a duty on the course, in their own planning terms. Ask: Which groups progress less well here, and what in the course might explain it? Avoid reading the issuer's paragraph aloud and avoid putting it to a student as something they must achieve, since it is a duty on the course."
- statement: qaa/optometry-2024/2.10.b3
  forPractitioner: { text: "Let progression strategies support students' academic and personal development, not only their subject learning.", rewrite: light, force: should, status: drafted }
  forBeneficiary: { text: "not-applicable: a duty on the course in its strategies", rewrite: full, force: should, status: drafted }
  author-agent-written: "Describe this as a recommendation ('should'): progression strategies support academic and personal growth alongside learning, set for the registrable integrated master's in Optometry (FHEQ Level 7; FQHEIS Level 11). Cite it as QAA (2024) Optometry Subject Benchmark Statement, para 2.10 (third item). Do not claim that the statement itself is a regulatory requirement, or that it covers non-registrable vision science awards. Set it beside 2.9, 4.5.b12 (well-being) and 3.7."
  author-agent-dialogue: "Raise this when a team plans personal tutoring or skills support. Frame it for the programme team or teacher as a duty on the course, in their own planning terms. Ask: Where in the course do students get support for their own development, not just for content? Avoid reading the issuer's paragraph aloud and avoid putting it to a student as something they must achieve, since it is a duty on the course."
- statement: qaa/optometry-2024/2.10.b4
  forPractitioner: { text: "Align progression strategies with the course learning outcomes or competencies set for each level.", rewrite: light, force: should, status: drafted }
  forBeneficiary: { text: "not-applicable: a duty on the course in its strategies", rewrite: full, force: should, status: drafted }
  author-agent-written: "Describe this as a recommendation ('should'): progression strategies fit the outcomes or competencies of each level, set for the registrable integrated master's in Optometry (FHEQ Level 7; FQHEIS Level 11). Cite it as QAA (2024) Optometry Subject Benchmark Statement, para 2.10 (fourth item). Do not claim that the statement itself is a regulatory requirement, or that it covers non-registrable vision science awards. Set it beside 2.7, 3.14.b1 (constructive alignment) and spine:7."
  author-agent-dialogue: "Raise this when a team writes or checks level outcomes. Frame it for the programme team or teacher as a duty on the course, in their own planning terms. Ask: For each level, which outcome does each support strategy serve? Avoid reading the issuer's paragraph aloud and avoid putting it to a student as something they must achieve, since it is a duty on the course."
- statement: qaa/optometry-2024/2.11
  forPractitioner: { text: "Usually offer a resit for failed assessments, above all where failure blocks progression or an award; make clear that exit awards (CertHE, DipHE, Pass degree or a non-registerable degree) do not lead to registration.", rewrite: light, force: should, status: drafted }
  forBeneficiary: { text: "If you fail an assessment you should usually get a chance to resit it, and if you leave early you may receive another award, but without the master's you will not be able to register as an optometrist.", rewrite: full, force: should, status: drafted }
  author-agent-written: "Describe this as a recommendation ('should'): students should usually be offered resits, and exit awards below the master's do not lead to registration, set for the registrable integrated master's in Optometry (FHEQ Level 7; FQHEIS Level 11). Cite it as QAA (2024) Optometry Subject Benchmark Statement, para 2.11. Do not claim that a resit is guaranteed; the paragraph says usually and subject to institutional rules. Set it beside 2.7 (progression), 3.1 (the GOC route) and qaa/fheq-2024/4.17.i1."
  author-agent-dialogue: "Raise this when a student fails an assessment or thinks about leaving the course. With a student, use plain words and the second person; with staff, frame it as what the course has to let every graduate show. Ask: Do you know the resit rules for this assessment, and what an exit award would and would not let you do? Avoid reading the issuer's paragraph aloud and avoid promising a resit or an award the institution's rules may not give."
- statement: qaa/optometry-2024/2.13
  forPractitioner: { text: "Choose a varied mix of face-to-face and digital delivery suited to the learners, the material and how it is assessed.", rewrite: light, force: should, status: drafted }
  forBeneficiary: { text: "not-applicable: a duty on the course in its delivery", rewrite: full, force: should, status: drafted }
  author-agent-written: "Describe this as a recommendation ('should'): delivery methods are varied and fitted to learners, content and assessment, set for the registrable integrated master's in Optometry (FHEQ Level 7; FQHEIS Level 11). Cite it as QAA (2024) Optometry Subject Benchmark Statement, para 2.13. Do not claim that the statement itself is a regulatory requirement, or that it covers non-registrable vision science awards. Set it beside 2.12, 3.9 (modes) and 1.15."
  author-agent-dialogue: "Raise this when a team chooses between in-person, online or blended delivery. Frame it for the programme team or teacher as a duty on the course, in their own planning terms. Ask: Why this mode for this material, and does it suit how the material is assessed? Avoid reading the issuer's paragraph aloud and avoid putting it to a student as something they must achieve, since it is a duty on the course."
- statement: qaa/optometry-2024/2.14
  forPractitioner: { text: "Include practical sessions with built-in reflection, in a range of real and simulated environments, so that students acquire clinical, patient-facing and reflective skills within an appropriate scope of practice.", rewrite: light, force: must, status: drafted }
  forBeneficiary: { text: "You must gain clinical, patient-facing and reflective skills, so your course must give you practical sessions in real and simulated settings with time to reflect on them.", rewrite: full, force: must, status: drafted }
  author-agent-written: "Describe this as an obligation ('must'): students acquire clinical, patient-facing and reflective skills and courses contain practical, reflective sessions, set for the registrable integrated master's in Optometry (FHEQ Level 7; FQHEIS Level 11). Cite it as QAA (2024) Optometry Subject Benchmark Statement, para 2.14. Do not claim that the statement itself is a regulatory requirement, or that it covers non-registrable vision science awards. Set it beside 2.2, 3.1.b5 (reflective practice), 4.5.b6 and qaa/fheq-2024/4.17.b8.3."
  author-agent-dialogue: "Raise this when a student asks why reflection is assessed alongside practical work, or a team plans practicals. With a student, use plain words and the second person; with staff, frame it as what the course has to let every graduate show. Ask: After your last practical session, what did you change because of reflecting on it? Avoid reading the issuer's paragraph aloud and avoid treating simulated practice as optional."
- statement: qaa/optometry-2024/2.15
  forPractitioner: { text: "Keep the course flexible enough to anticipate change in the subject, its interfaces and employers' needs, and resilient enough to adapt when unforeseen disruption arrives.", rewrite: light, force: should, status: drafted }
  forBeneficiary: { text: "not-applicable: a duty on the course in how it is run", rewrite: full, force: should, status: drafted }
  author-agent-written: "Describe this as a recommendation ('should'): courses stay flexible to anticipate change and resilient to adapt to disruption, set for the registrable integrated master's in Optometry (FHEQ Level 7; FQHEIS Level 11). Cite it as QAA (2024) Optometry Subject Benchmark Statement, para 2.15. Do not claim that the statement itself is a regulatory requirement, or that it covers non-registrable vision science awards; record \"need to\" as a further obliging phrase, not a must. Set it beside 2.16 (technology), 3.8 and 2.26 (enhancement)."
  author-agent-dialogue: "Raise this when a team reviews a course after disruption or plans for change in practice. Frame it for the programme team or teacher as a duty on the course, in their own planning terms. Ask: What would this course do if placements were suddenly unavailable for a term? Avoid reading the issuer's paragraph aloud and avoid putting it to a student as something they must achieve, since it is a duty on the course."
- statement: qaa/optometry-2024/2.16
  forPractitioner: { text: "Keep the course able to respond to new technology in practice and education, including artificial intelligence.", rewrite: light, force: should, status: drafted }
  forBeneficiary: { text: "not-applicable: a duty on the course in how it is run", rewrite: full, force: should, status: drafted }
  author-agent-written: "Describe this as a recommendation ('should'): courses respond to changes in technology, artificial intelligence included, set for the registrable integrated master's in Optometry (FHEQ Level 7; FQHEIS Level 11). Cite it as QAA (2024) Optometry Subject Benchmark Statement, para 2.16. Do not claim that the statement itself is a regulatory requirement, or that it covers non-registrable vision science awards. Set it beside 3.2.b13 (AI as content), 3.2.b5, 4.5.b9 (adapting to technology) and 2.15."
  author-agent-dialogue: "Raise this when a team discusses AI tools in imaging, teaching or assessment. Frame it for the programme team or teacher as a duty on the course, in their own planning terms. Ask: Where is AI already used in the practice your students will join, and does the course reflect it? Avoid reading the issuer's paragraph aloud and avoid putting it to a student as something they must achieve, since it is a duty on the course."
- statement: qaa/optometry-2024/2.17
  forPractitioner: { text: "Where partners deliver training, set up oversight processes so that they meet all relevant standards, with effective communication and regular consultation to keep the course meeting employers' needs.", rewrite: light, force: should, status: drafted }
  forBeneficiary: { text: "not-applicable: a duty on the institution and its partners", rewrite: full, force: should, status: drafted }
  author-agent-written: "Describe this as a recommendation ('should'): institutions oversee placement partners and consult them regularly, set for the registrable integrated master's in Optometry (FHEQ Level 7; FQHEIS Level 11). Cite it as QAA (2024) Optometry Subject Benchmark Statement, para 2.17. Do not claim that the statement itself is a regulatory requirement, or that it covers non-registrable vision science awards; the oversight duty is worded \"expected to\", recorded under should. Set it beside 2.18, 2.22 and 2.24 (monitoring)."
  author-agent-dialogue: "Raise this when a team sets up or reviews a placement agreement. Frame it for the programme team or teacher as a duty on the course, in their own planning terms. Ask: How do you know each placement meets the standards, and when did you last consult the partner? Avoid reading the issuer's paragraph aloud and avoid putting it to a student as something they must achieve, since it is a duty on the course."
- statement: qaa/optometry-2024/2.18
  forPractitioner: { text: "Work with stakeholders to include work-based or simulated clinical practice, and have a clear employability strategy through which students build employment-focused skills and engage with employers.", rewrite: light, force: should, status: drafted }
  forBeneficiary: { text: "Your course should give you work-based or simulated clinical practice and a clear way to build skills for employment and get to know employers, for example through placements.", rewrite: full, force: should, status: drafted }
  author-agent-written: "Describe this as a recommendation ('should'): courses include work-based or simulated practice and have an employability strategy, set for the registrable integrated master's in Optometry (FHEQ Level 7; FQHEIS Level 11). Cite it as QAA (2024) Optometry Subject Benchmark Statement, para 2.18. Do not claim that the statement itself is a regulatory requirement, or that it covers non-registrable vision science awards. Set it beside 1.18, 2.17 and the enterprise theme (1.19 to 1.22)."
  author-agent-dialogue: "Raise this when a student asks how to meet employers or a team reviews its employability plan. With a student, use plain words and the second person; with staff, frame it as what the course has to let every graduate show. Ask: Which employers have you met through the course so far, and what did you learn about the work? Avoid reading the issuer's paragraph aloud and avoid promising a particular placement or employer."
- statement: qaa/optometry-2024/2.20
  forPractitioner: { text: "Treat students as partners: involve them in co-creating the curriculum and give their voice real weight in course development, delivery and review through representatives, module evaluation and surveys.", rewrite: light, force: should, status: drafted }
  forBeneficiary: { text: "You should expect to be treated as a partner in your course and to help shape what and how you learn, through course representatives, module feedback and surveys.", rewrite: full, force: should, status: drafted }
  author-agent-written: "Describe this as a recommendation ('should'): students are partners in their course and the student voice shapes its development and review, set for the registrable integrated master's in Optometry (FHEQ Level 7; FQHEIS Level 11). Cite it as QAA (2024) Optometry Subject Benchmark Statement, para 2.20. Do not claim that the statement itself is a regulatory requirement, or that it covers non-registrable vision science awards. Set it beside 2.21 (patients as partners), 2.24 and 2.26 (feedback in review)."
  author-agent-dialogue: "Raise this when a student feels unheard, or a team plans curriculum review. With a student, use plain words and the second person; with staff, frame it as what the course has to let every graduate show. Ask: What change would you most like to see in the course, and who could you raise it with? Avoid reading the issuer's paragraph aloud and avoid suggesting that students can decide course content alone."
- statement: qaa/optometry-2024/2.24
  forPractitioner: { text: "Gather feedback from students, employers, placement providers and alumni, combine performance and experience data with expert review, and use periodic review to embed ESD and EDI across the curriculum.", rewrite: light, force: should, status: drafted }
  forBeneficiary: { text: "not-applicable: a duty on the course in its review", rewrite: full, force: should, status: drafted }
  author-agent-written: "Describe this as a recommendation ('should'): monitoring and review draw on varied feedback and data and embed ESD and EDI, set for the registrable integrated master's in Optometry (FHEQ Level 7; FQHEIS Level 11). Cite it as QAA (2024) Optometry Subject Benchmark Statement, para 2.24. Do not claim that the statement itself is a regulatory requirement, or that it covers non-registrable vision science awards. Set it beside 2.22, 2.26, 1.9 (EDI) and 1.17 (ESD)."
  author-agent-dialogue: "Raise this when a team prepares for periodic review. Frame it for the programme team or teacher as a duty on the course, in their own planning terms. Ask: Whose feedback is missing from your evidence, and where does the review show ESD and EDI in the curriculum? Avoid reading the issuer's paragraph aloud and avoid putting it to a student as something they must achieve, since it is a duty on the course."
- statement: qaa/optometry-2024/2.26
  forPractitioner: { text: "Join student data and feedback with expert and external examiner review to keep the curriculum current, engaging and accessible, and actively involve students, graduates, employers, service users and professional bodies in designing improvements.", rewrite: light, force: should, status: drafted }
  forBeneficiary: { text: "You should have an active part, alongside graduates, employers and patients, in designing and making improvements to your course.", rewrite: full, force: should, status: drafted }
  author-agent-written: "Describe this as a recommendation ('should'): evaluation joins data, feedback and expert review, and stakeholders take part in enhancement, set for the registrable integrated master's in Optometry (FHEQ Level 7; FQHEIS Level 11). Cite it as QAA (2024) Optometry Subject Benchmark Statement, para 2.26. Do not claim that the statement itself is a regulatory requirement, or that it covers non-registrable vision science awards. Set it beside 2.20, 2.24 and 2.25 (external examiners)."
  author-agent-dialogue: "Raise this when a student asks how feedback is used, or a team plans enhancement. With a student, use plain words and the second person; with staff, frame it as what the course has to let every graduate show. Ask: What has changed in the course because of feedback, and who took part in deciding it? Avoid reading the issuer's paragraph aloud and avoid implying that a student's single comment must change the course."
- statement: qaa/optometry-2024/2.27
  forPractitioner: { text: "Plan for evaluation and accreditation by the professional and regulatory bodies, normally by a mix of site visits and desk-based review.", rewrite: light, force: will, status: drafted }
  forBeneficiary: { text: "not-applicable: a duty on the course; the student meets its effect", rewrite: full, force: will, status: drafted }
  author-agent-written: "Describe this as an expected outcome ('will'): courses undergo evaluation and accreditation by professional and regulatory bodies, set for the registrable integrated master's in Optometry (FHEQ Level 7; FQHEIS Level 11). Cite it as QAA (2024) Optometry Subject Benchmark Statement, para 2.27. Do not claim that the statement grants or describes accreditation criteria; those are the bodies' own. Set it beside 1.5, 3.4 and SB5 (the General Optical Council)."
  author-agent-dialogue: "Raise this when a team prepares for a regulator visit. Frame it for the programme team or teacher as a duty on the course, in their own planning terms. Ask: Which evidence will the visit look for, and where is it held? Avoid reading the issuer's paragraph aloud and avoid putting it to a student as something they must achieve, since it is a duty on the course."
- statement: qaa/optometry-2024/3.1
  forPractitioner: { text: "Graduates must meet the GOC's required outcomes and standards to join the register as fully qualified optometrists; design content and placements to that end.", rewrite: light, force: must, status: drafted }
  forBeneficiary: { text: "To register as a fully qualified optometrist, you must meet the outcomes and standards the General Optical Council sets.", rewrite: full, force: must, status: drafted }
  author-agent-written: "Describe this as an obligation ('must'): graduates meet the regulator's outcomes and standards to register, set for the registrable integrated master's in Optometry (FHEQ Level 7; FQHEIS Level 11). Cite it as QAA (2024) Optometry Subject Benchmark Statement, para 3.1. Do not claim that the statement itself sets the GOC outcomes. Set it beside 3.4 and 3.5 (the GOC outcomes), 4.4 (their threshold summaries) and SB5."
  author-agent-dialogue: "Raise this when a student asks what registration needs. With a student, use plain words and the second person; with staff, frame it as what the course has to let every graduate show. Ask: Which of the regulator's outcome categories do you feel least sure about meeting? Avoid reading the issuer's paragraph aloud and avoid treating this statement as a substitute for the GOC's own requirements."
- statement: qaa/optometry-2024/3.1.b1
  forPractitioner: { text: "Equip graduates to keep within their scope of practice so that their patient-centred care is safe, lawful and effective.", rewrite: light, force: should, status: drafted }
  forBeneficiary: { text: "Your course should prepare you to work within your scope of practice and give care that is safe, lawful and effective.", rewrite: full, force: should, status: drafted }
  author-agent-written: "Describe this as a recommendation ('should'): courses equip graduates to work within scope for safe, lawful, effective care, set for the registrable integrated master's in Optometry (FHEQ Level 7; FQHEIS Level 11). Cite it as QAA (2024) Optometry Subject Benchmark Statement, para 3.1 (first skill). Do not claim that the statement itself is a regulatory requirement, or that it covers non-registrable vision science awards. Set it beside 4.4.b3 (clinical practice), 4.4.b4 (ethics and standards) and 3.5.b3."
  author-agent-dialogue: "Raise this when a student is unsure where their scope of practice ends. With a student, use plain words and the second person; with staff, frame it as what the course has to let every graduate show. Ask: What would you do if a patient needed something outside what you are allowed or trained to do? Avoid reading the issuer's paragraph aloud and avoid giving a firm view on a specific legal boundary, which the regulator sets."
- statement: qaa/optometry-2024/3.1.b2
  forPractitioner: { text: "Develop graduates' critical thinking and their ability to make clinical decisions based on evidence.", rewrite: light, force: should, status: drafted }
  forBeneficiary: { text: "Your course should help you think critically and base your clinical decisions on evidence.", rewrite: full, force: should, status: drafted }
  author-agent-written: "Describe this as a recommendation ('should'): courses build critical thinking and evidence-based clinical decision-making, set for the registrable integrated master's in Optometry (FHEQ Level 7; FQHEIS Level 11). Cite it as QAA (2024) Optometry Subject Benchmark Statement, para 3.1 (second skill). Do not claim that the statement itself is a regulatory requirement, or that it covers non-registrable vision science awards. Set it beside 4.5.b2, 3.3.b4 and qaa/fheq-2024/4.17.b5."
  author-agent-dialogue: "Raise this when a student explains a clinical decision. With a student, use plain words and the second person; with staff, frame it as what the course has to let every graduate show. Ask: What evidence supported your decision, and what would have changed it? Avoid reading the issuer's paragraph aloud and avoid judging the decision itself rather than how it was reached."
- statement: qaa/optometry-2024/3.1.b3
  forPractitioner: { text: "Develop graduates' critical appraisal of research literature and other information sources.", rewrite: light, force: should, status: drafted }
  forBeneficiary: { text: "Your course should help you judge research papers and other sources of information critically.", rewrite: full, force: should, status: drafted }
  author-agent-written: "Describe this as a recommendation ('should'): courses build critical appraisal of research and other information, set for the registrable integrated master's in Optometry (FHEQ Level 7; FQHEIS Level 11). Cite it as QAA (2024) Optometry Subject Benchmark Statement, para 3.1 (third skill). Do not claim that the statement itself is a regulatory requirement, or that it covers non-registrable vision science awards. Set it beside 4.5.b4, 3.3.b7 and qaa/fheq-2024/4.17.b4.1."
  author-agent-dialogue: "Raise this when a student cites a source for a clinical claim. With a student, use plain words and the second person; with staff, frame it as what the course has to let every graduate show. Ask: How strong is this source, and what would make you trust it less? Avoid reading the issuer's paragraph aloud and avoid appraising the paper for the student instead of with them."
- statement: qaa/optometry-2024/3.1.b4
  forPractitioner: { text: "Develop graduates' effective verbal and written communication skills.", rewrite: light, force: should, status: drafted }
  forBeneficiary: { text: "Your course should help you communicate well, both in speech and in writing.", rewrite: full, force: should, status: drafted }
  author-agent-written: "Describe this as a recommendation ('should'): courses build effective verbal and written communication, set for the registrable integrated master's in Optometry (FHEQ Level 7; FQHEIS Level 11). Cite it as QAA (2024) Optometry Subject Benchmark Statement, para 3.1 (fourth skill). Do not claim that the statement itself is a regulatory requirement, or that it covers non-registrable vision science awards. Set it beside 4.4.b2 (communication at threshold), 4.5.b7 and qaa/fheq-2024/4.17.b5."
  author-agent-dialogue: "Raise this when a student prepares for a patient explanation or a referral letter. With a student, use plain words and the second person; with staff, frame it as what the course has to let every graduate show. Ask: How would you explain this finding to the patient, and how would you write it to another professional? Avoid reading the issuer's paragraph aloud and avoid correcting tone without explaining why."
- statement: qaa/optometry-2024/3.1.b5
  forPractitioner: { text: "Develop graduates' reflective practice as the basis of continuing professional development.", rewrite: light, force: should, status: drafted }
  forBeneficiary: { text: "Your course should help you reflect on your practice in a way that supports your learning throughout your career.", rewrite: full, force: should, status: drafted }
  author-agent-written: "Describe this as a recommendation ('should'): courses build reflective practice for continuing professional development, set for the registrable integrated master's in Optometry (FHEQ Level 7; FQHEIS Level 11). Cite it as QAA (2024) Optometry Subject Benchmark Statement, para 3.1 (fifth skill). Do not claim that the statement itself is a regulatory requirement, or that it covers non-registrable vision science awards. Set it beside 4.4.b7 (lifelong learning), 4.5.b6 and qaa/fheq-2024/4.17.b8.3."
  author-agent-dialogue: "Raise this when a student writes a reflective log entry. With a student, use plain words and the second person; with staff, frame it as what the course has to let every graduate show. Ask: What will you do differently next time, and how will you know it worked? Avoid reading the issuer's paragraph aloud and avoid treating reflection as a summary of events."
- statement: qaa/optometry-2024/3.5.b1
  forPractitioner: { text: "Graduates must be able to use an adaptive, personalised approach to care that weighs social, clinical, personal and cultural needs (the regulator's outcome).", rewrite: light, force: must, status: drafted }
  forBeneficiary: { text: "To register, you must be able to adapt your care to each patient, taking account of their social, clinical, personal and cultural needs.", rewrite: full, force: must, status: drafted }
  author-agent-written: "Describe this as an obligation ('must'): the regulator requires graduates to give adaptive, personalised care, set for the registrable integrated master's in Optometry (FHEQ Level 7; FQHEIS Level 11). Cite it as QAA (2024) Optometry Subject Benchmark Statement, para 3.5 (first outcome). Do not claim that this summary is the General Optical Council's own wording or that it replaces the GOC requirements, nor that it holds at Level 6. Set it beside 4.4.b1 (person-centred care at threshold), 1.10 and 3.4."
  author-agent-dialogue: "Raise this when a student discusses a patient whose needs did not fit the routine. With a student, use plain words and the second person; with staff, frame it as what the course has to let every graduate show. Ask: What did you change for that patient, and why? Avoid reading the issuer's paragraph aloud and avoid implying that one approach suits all patients."
- statement: qaa/optometry-2024/3.5.b2
  forPractitioner: { text: "Graduates must be able to communicate effectively with patients and colleagues in other professions (the regulator's outcome).", rewrite: light, force: must, status: drafted }
  forBeneficiary: { text: "To register, you must be able to communicate well with patients and with other professionals.", rewrite: full, force: must, status: drafted }
  author-agent-written: "Describe this as an obligation ('must'): the regulator requires effective communication with patients and professionals, set for the registrable integrated master's in Optometry (FHEQ Level 7; FQHEIS Level 11). Cite it as QAA (2024) Optometry Subject Benchmark Statement, para 3.5 (second outcome). Do not claim that this summary is the General Optical Council's own wording or that it replaces the GOC requirements, nor that it holds at Level 6. Set it beside 4.4.b2 (communication at threshold), 3.1.b4 and 4.5.b7."
  author-agent-dialogue: "Raise this when a student prepares to explain a result or make a referral. With a student, use plain words and the second person; with staff, frame it as what the course has to let every graduate show. Ask: Who needs to understand this, and what do they already know? Avoid reading the issuer's paragraph aloud and avoid judging communication on fluency alone."
- statement: qaa/optometry-2024/3.5.b3
  forPractitioner: { text: "Graduates must be able to carry out suitable eye examinations and build management plans on evidence, within scope and competence (the regulator's outcome).", rewrite: light, force: must, status: drafted }
  forBeneficiary: { text: "To register, you must be able to carry out the right eye examinations and plan care based on evidence, within the limits of what you are trained and allowed to do.", rewrite: full, force: must, status: drafted }
  author-agent-written: "Describe this as an obligation ('must'): the regulator requires sound examinations and evidence-informed management plans within competence, set for the registrable integrated master's in Optometry (FHEQ Level 7; FQHEIS Level 11). Cite it as QAA (2024) Optometry Subject Benchmark Statement, para 3.5 (third outcome). Do not claim that this summary is the General Optical Council's own wording or that it replaces the GOC requirements, nor that it holds at Level 6. Set it beside 4.4.b3 (clinical practice at threshold), 3.3 and qaa/fheq-2024/4.17.b5."
  author-agent-dialogue: "Raise this when a student plans a patient's management. With a student, use plain words and the second person; with staff, frame it as what the course has to let every graduate show. Ask: What evidence supports this plan, and where would you refer instead? Avoid reading the issuer's paragraph aloud and avoid endorsing a plan beyond the student's scope."
- statement: qaa/optometry-2024/3.5.b4
  forPractitioner: { text: "Graduates must be able to uphold high, equitable professional and ethical standards and keep within current legislation (the regulator's outcome).", rewrite: light, force: must, status: drafted }
  forBeneficiary: { text: "To register, you must be able to keep to high, fair professional and ethical standards and work within the law.", rewrite: full, force: must, status: drafted }
  author-agent-written: "Describe this as an obligation ('must'): the regulator requires high, equitable standards, ethics and legal compliance, set for the registrable integrated master's in Optometry (FHEQ Level 7; FQHEIS Level 11). Cite it as QAA (2024) Optometry Subject Benchmark Statement, para 3.5 (fourth outcome). Do not claim that this summary is the General Optical Council's own wording or that it replaces the GOC requirements, nor that it holds at Level 6. Set it beside 4.4.b4 (ethics and standards at threshold) and 3.2.b11."
  author-agent-dialogue: "Raise this when a student meets an ethical dilemma in clinic. With a student, use plain words and the second person; with staff, frame it as what the course has to let every graduate show. Ask: Which professional standard applies here, and what does the law allow? Avoid reading the issuer's paragraph aloud and avoid giving legal advice on a specific case."
- statement: qaa/optometry-2024/3.5.b5
  forPractitioner: { text: "Graduates must be able to recognise risks to patients, colleagues and others and put adequate safeguards in place (the regulator's outcome).", rewrite: light, force: must, status: drafted }
  forBeneficiary: { text: "To register, you must be able to spot risks to patients, colleagues and others and act to keep them safe.", rewrite: full, force: must, status: drafted }
  author-agent-written: "Describe this as an obligation ('must'): the regulator requires graduates to identify risk and safeguard others, set for the registrable integrated master's in Optometry (FHEQ Level 7; FQHEIS Level 11). Cite it as QAA (2024) Optometry Subject Benchmark Statement, para 3.5 (fifth outcome). Do not claim that this summary is the General Optical Council's own wording or that it replaces the GOC requirements, nor that it holds at Level 6. Set it beside 4.4.b5 (risk at threshold) and qaa/fheq-2024/4.17.b8.2."
  author-agent-dialogue: "Raise this when a student describes a situation where someone might have been at risk. With a student, use plain words and the second person; with staff, frame it as what the course has to let every graduate show. Ask: What made you think there was a risk, and what did you do about it? Avoid reading the issuer's paragraph aloud and avoid handling a live safeguarding concern in conversation instead of directing it to the right person."
- statement: qaa/optometry-2024/3.5.b6
  forPractitioner: { text: "Graduates must be able to provide clinical leadership and engage with clinical governance, service improvement and national public health work (the regulator's outcome).", rewrite: light, force: must, status: drafted }
  forBeneficiary: { text: "To register, you must be able to show clinical leadership and take part in clinical governance, improving services and public health work.", rewrite: full, force: must, status: drafted }
  author-agent-written: "Describe this as an obligation ('must'): the regulator requires clinical leadership and engagement with governance and public health, set for the registrable integrated master's in Optometry (FHEQ Level 7; FQHEIS Level 11). Cite it as QAA (2024) Optometry Subject Benchmark Statement, para 3.5 (sixth outcome). Do not claim that this summary is the General Optical Council's own wording or that it replaces the GOC requirements, nor that it holds at Level 6. Set it beside 4.4.b6 (leadership and management at threshold) and qaa/fheq-2024/4.17.b8.1."
  author-agent-dialogue: "Raise this when a student asks what leadership means for a newly registered optometrist. With a student, use plain words and the second person; with staff, frame it as what the course has to let every graduate show. Ask: Where in your placement could you have suggested an improvement? Avoid reading the issuer's paragraph aloud and avoid equating leadership with a management post."
- statement: qaa/optometry-2024/3.5.b7
  forPractitioner: { text: "Graduates must be able to keep their knowledge and skills current and judge their own performance to improve patient care (the regulator's outcome).", rewrite: light, force: must, status: drafted }
  forBeneficiary: { text: "To register, you must be able to keep your knowledge and skills up to date and judge your own performance to give patients better care.", rewrite: full, force: must, status: drafted }
  author-agent-written: "Describe this as an obligation ('must'): the regulator requires graduates to stay current and evaluate their own performance, set for the registrable integrated master's in Optometry (FHEQ Level 7; FQHEIS Level 11). Cite it as QAA (2024) Optometry Subject Benchmark Statement, para 3.5 (seventh outcome). Do not claim that this summary is the General Optical Council's own wording or that it replaces the GOC requirements, nor that it holds at Level 6. Set it beside 4.4.b7 (lifelong learning at threshold), 4.5.b6 and qaa/fheq-2024/4.17.b8.3."
  author-agent-dialogue: "Raise this when a student plans their learning after a placement. With a student, use plain words and the second person; with staff, frame it as what the course has to let every graduate show. Ask: What evidence do you have about your own performance, and what will you learn next because of it? Avoid reading the issuer's paragraph aloud and avoid setting the plan for them."
- statement: qaa/optometry-2024/3.8
  forPractitioner: { text: "Update teaching and learning strategies as clinical practice, technology and pedagogic research advance, and give staff regular access to subject and educational professional development.", rewrite: light, force: should, status: drafted }
  forBeneficiary: { text: "not-applicable: a duty on the course and its staff", rewrite: full, force: should, status: drafted }
  author-agent-written: "Describe this as a recommendation ('should'): teaching strategies respond to advances in practice, technology and pedagogy, with staff kept up to date, set for the registrable integrated master's in Optometry (FHEQ Level 7; FQHEIS Level 11). Cite it as QAA (2024) Optometry Subject Benchmark Statement, para 3.8. Do not claim that the statement itself is a regulatory requirement, or that it covers non-registrable vision science awards. Set it beside 2.15, 2.16 and 3.6."
  author-agent-dialogue: "Raise this when a team reviews teaching methods or staff development. Frame it for the programme team or teacher as a duty on the course, in their own planning terms. Ask: Which recent change in clinical practice has not yet reached your teaching? Avoid reading the issuer's paragraph aloud and avoid putting it to a student as something they must achieve, since it is a duty on the course."
- statement: qaa/optometry-2024/3.12
  forPractitioner: { text: "Assess and map every GOC outcome; keep assessment authentic, rigorous and clinically relevant, use it to build professional and wider skills, and make sure it separates threshold from higher achievement.", rewrite: light, force: must, status: drafted }
  forBeneficiary: { text: "not-applicable: a duty on the course in designing assessment", rewrite: full, force: must, status: drafted }
  author-agent-written: "Describe this as an obligation ('must'): every regulator outcome is assessed and mapped, and assessment is authentic and discriminates above the threshold, set for the registrable integrated master's in Optometry (FHEQ Level 7; FQHEIS Level 11). Cite it as QAA (2024) Optometry Subject Benchmark Statement, para 3.12. Do not claim that the statement defines grades above the threshold; it states only the threshold. Set it beside 3.13, 3.14, 3.16 and 4.2 (Annex D)."
  author-agent-dialogue: "Raise this when a team maps assessments to the GOC outcomes. Frame it for the programme team or teacher as a duty on the course, in their own planning terms. Ask: Which GOC outcome is assessed nowhere, or only once, and can your marking tell threshold from better work? Avoid reading the issuer's paragraph aloud and avoid putting it to a student as something they must achieve, since it is a duty on the course."
- statement: qaa/optometry-2024/3.13.b1
  forPractitioner: { text: "In designing assessment, balance validity (that it measures what it claims to) against the other five qualities.", rewrite: light, force: should, status: drafted }
  forBeneficiary: { text: "not-applicable: a duty on the course in designing assessment", rewrite: full, force: should, status: drafted }
  author-agent-written: "Describe this as a recommendation ('should'): assessment balances validity with the other listed qualities, set for the registrable integrated master's in Optometry (FHEQ Level 7; FQHEIS Level 11). Cite it as QAA (2024) Optometry Subject Benchmark Statement, para 3.13 (validity). Do not claim that the statement itself is a regulatory requirement, or that it covers non-registrable vision science awards; the six are to be balanced, not each maximised. Set it beside 3.13.b1 to 3.13.b6 together, 3.12 and 3.15."
  author-agent-dialogue: "Raise this when a team reviews an assessment for its validity. Frame it for the programme team or teacher as a duty on the course, in their own planning terms. Ask: What does this assessment give up for validity, and is the trade worth it? Avoid reading the issuer's paragraph aloud and avoid putting it to a student as something they must achieve, since it is a duty on the course."
- statement: qaa/optometry-2024/3.13.b2
  forPractitioner: { text: "In designing assessment, balance reliability (that it gives consistent results) against the other five qualities.", rewrite: light, force: should, status: drafted }
  forBeneficiary: { text: "not-applicable: a duty on the course in designing assessment", rewrite: full, force: should, status: drafted }
  author-agent-written: "Describe this as a recommendation ('should'): assessment balances reliability with the other listed qualities, set for the registrable integrated master's in Optometry (FHEQ Level 7; FQHEIS Level 11). Cite it as QAA (2024) Optometry Subject Benchmark Statement, para 3.13 (reliability). Do not claim that the statement itself is a regulatory requirement, or that it covers non-registrable vision science awards; the six are to be balanced, not each maximised. Set it beside 3.13.b1 to 3.13.b6 together, 3.12 and 3.15."
  author-agent-dialogue: "Raise this when a team reviews an assessment for its reliability. Frame it for the programme team or teacher as a duty on the course, in their own planning terms. Ask: What does this assessment give up for reliability, and is the trade worth it? Avoid reading the issuer's paragraph aloud and avoid putting it to a student as something they must achieve, since it is a duty on the course."
- statement: qaa/optometry-2024/3.13.b3
  forPractitioner: { text: "In designing assessment, balance equitability (that it is fair to every student) against the other five qualities.", rewrite: light, force: should, status: drafted }
  forBeneficiary: { text: "not-applicable: a duty on the course in designing assessment", rewrite: full, force: should, status: drafted }
  author-agent-written: "Describe this as a recommendation ('should'): assessment balances equitability with the other listed qualities, set for the registrable integrated master's in Optometry (FHEQ Level 7; FQHEIS Level 11). Cite it as QAA (2024) Optometry Subject Benchmark Statement, para 3.13 (equitability). Do not claim that the statement itself is a regulatory requirement, or that it covers non-registrable vision science awards; the six are to be balanced, not each maximised. Set it beside 3.13.b1 to 3.13.b6 together, 3.12 and 3.15."
  author-agent-dialogue: "Raise this when a team reviews an assessment for its equitability. Frame it for the programme team or teacher as a duty on the course, in their own planning terms. Ask: What does this assessment give up for equitability, and is the trade worth it? Avoid reading the issuer's paragraph aloud and avoid putting it to a student as something they must achieve, since it is a duty on the course."
- statement: qaa/optometry-2024/3.13.b4
  forPractitioner: { text: "In designing assessment, balance efficiency (that it is proportionate in effort) against the other five qualities.", rewrite: light, force: should, status: drafted }
  forBeneficiary: { text: "not-applicable: a duty on the course in designing assessment", rewrite: full, force: should, status: drafted }
  author-agent-written: "Describe this as a recommendation ('should'): assessment balances efficiency with the other listed qualities, set for the registrable integrated master's in Optometry (FHEQ Level 7; FQHEIS Level 11). Cite it as QAA (2024) Optometry Subject Benchmark Statement, para 3.13 (efficiency). Do not claim that the statement itself is a regulatory requirement, or that it covers non-registrable vision science awards; the six are to be balanced, not each maximised. Set it beside 3.13.b1 to 3.13.b6 together, 3.12 and 3.15."
  author-agent-dialogue: "Raise this when a team reviews an assessment for its efficiency. Frame it for the programme team or teacher as a duty on the course, in their own planning terms. Ask: What does this assessment give up for efficiency, and is the trade worth it? Avoid reading the issuer's paragraph aloud and avoid putting it to a student as something they must achieve, since it is a duty on the course."
- statement: qaa/optometry-2024/3.13.b5
  forPractitioner: { text: "In designing assessment, balance transparency (that it is clear to students and staff) against the other five qualities.", rewrite: light, force: should, status: drafted }
  forBeneficiary: { text: "not-applicable: a duty on the course in designing assessment", rewrite: full, force: should, status: drafted }
  author-agent-written: "Describe this as a recommendation ('should'): assessment balances transparency with the other listed qualities, set for the registrable integrated master's in Optometry (FHEQ Level 7; FQHEIS Level 11). Cite it as QAA (2024) Optometry Subject Benchmark Statement, para 3.13 (transparency). Do not claim that the statement itself is a regulatory requirement, or that it covers non-registrable vision science awards; the six are to be balanced, not each maximised. Set it beside 3.13.b1 to 3.13.b6 together, 3.12 and 3.15."
  author-agent-dialogue: "Raise this when a team reviews an assessment for its transparency. Frame it for the programme team or teacher as a duty on the course, in their own planning terms. Ask: What does this assessment give up for transparency, and is the trade worth it? Avoid reading the issuer's paragraph aloud and avoid putting it to a student as something they must achieve, since it is a duty on the course."
- statement: qaa/optometry-2024/3.13.b6
  forPractitioner: { text: "In designing assessment, balance authenticity (that it resembles real practice) against the other five qualities.", rewrite: light, force: should, status: drafted }
  forBeneficiary: { text: "not-applicable: a duty on the course in designing assessment", rewrite: full, force: should, status: drafted }
  author-agent-written: "Describe this as a recommendation ('should'): assessment balances authenticity with the other listed qualities, set for the registrable integrated master's in Optometry (FHEQ Level 7; FQHEIS Level 11). Cite it as QAA (2024) Optometry Subject Benchmark Statement, para 3.13 (authenticity). Do not claim that the statement itself is a regulatory requirement, or that it covers non-registrable vision science awards; the six are to be balanced, not each maximised. Set it beside 3.13.b1 to 3.13.b6 together, 3.12 and 3.15."
  author-agent-dialogue: "Raise this when a team reviews an assessment for its authenticity. Frame it for the programme team or teacher as a duty on the course, in their own planning terms. Ask: What does this assessment give up for authenticity, and is the trade worth it? Avoid reading the issuer's paragraph aloud and avoid putting it to a student as something they must achieve, since it is a duty on the course."
- statement: qaa/optometry-2024/3.14.b1
  forPractitioner: { text: "Constructively align each assessment with the learning outcomes it is meant to test.", rewrite: light, force: should, status: drafted }
  forBeneficiary: { text: "not-applicable: a duty on the course in designing assessment", rewrite: full, force: should, status: drafted }
  author-agent-written: "Describe this as a recommendation ('should'): assessment is constructively aligned with learning outcomes, set for the registrable integrated master's in Optometry (FHEQ Level 7; FQHEIS Level 11). Cite it as QAA (2024) Optometry Subject Benchmark Statement, para 3.14 (first property). Do not claim that the statement itself is a regulatory requirement, or that it covers non-registrable vision science awards. Set it beside 3.12, 2.10.b4 and 3.16."
  author-agent-dialogue: "Raise this when a team writes an assessment brief. Frame it for the programme team or teacher as a duty on the course, in their own planning terms. Ask: Which outcome does each task test, and could a student pass without meeting it? Avoid reading the issuer's paragraph aloud and avoid putting it to a student as something they must achieve, since it is a duty on the course."
- statement: qaa/optometry-2024/3.14.b2
  forPractitioner: { text: "Design assessment to give formative and summative opportunities and build in feedback and feedforward.", rewrite: light, force: should, status: drafted }
  forBeneficiary: { text: "not-applicable: a duty on the course in designing assessment", rewrite: full, force: should, status: drafted }
  author-agent-written: "Describe this as a recommendation ('should'): assessment gives formative and summative opportunities with feedback and feedforward, set for the registrable integrated master's in Optometry (FHEQ Level 7; FQHEIS Level 11). Cite it as QAA (2024) Optometry Subject Benchmark Statement, para 3.14 (second property). Do not claim that the statement itself is a regulatory requirement, or that it covers non-registrable vision science awards. Set it beside 3.19 to 3.21 (feedback) and 3.12."
  author-agent-dialogue: "Raise this when a team plans an assessment schedule. Frame it for the programme team or teacher as a duty on the course, in their own planning terms. Ask: Where do students get a low-stakes try before each summative task? Avoid reading the issuer's paragraph aloud and avoid putting it to a student as something they must achieve, since it is a duty on the course."
- statement: qaa/optometry-2024/3.14.b3
  forPractitioner: { text: "Make assessment inclusive and accessible to all students.", rewrite: light, force: should, status: drafted }
  forBeneficiary: { text: "not-applicable: a duty on the course in designing assessment", rewrite: full, force: should, status: drafted }
  author-agent-written: "Describe this as a recommendation ('should'): assessment is inclusive and accessible, set for the registrable integrated master's in Optometry (FHEQ Level 7; FQHEIS Level 11). Cite it as QAA (2024) Optometry Subject Benchmark Statement, para 3.14 (third property). Do not claim that the statement itself is a regulatory requirement, or that it covers non-registrable vision science awards. Set it beside 1.14 (accessibility within patient safety), 3.11 and 1.15."
  author-agent-dialogue: "Raise this when a team reviews an assessment format for barriers. Frame it for the programme team or teacher as a duty on the course, in their own planning terms. Ask: Who might this format disadvantage, and what inclusive alternative keeps the standard? Avoid reading the issuer's paragraph aloud and avoid putting it to a student as something they must achieve, since it is a duty on the course."
- statement: qaa/optometry-2024/3.15
  forPractitioner: { text: "Use evidence-based assessment design and methods, and attend to standard setting and moderation.", rewrite: light, force: should, status: drafted }
  forBeneficiary: { text: "not-applicable: a duty on the provider", rewrite: full, force: should, status: drafted }
  author-agent-written: "Describe this as a recommendation ('should'): assessment design is evidence-based, with standard setting and moderation considered, set for the registrable integrated master's in Optometry (FHEQ Level 7; FQHEIS Level 11). Cite it as QAA (2024) Optometry Subject Benchmark Statement, para 3.15. Do not claim that the statement itself is a regulatory requirement, or that it covers non-registrable vision science awards. Set it beside 3.12, 3.13 and 2.25 (external examiners)."
  author-agent-dialogue: "Raise this when a team sets pass marks for a clinical examination. Frame it for the programme team or teacher as a duty on the course, in their own planning terms. Ask: How was the pass mark set, and how is marking moderated? Avoid reading the issuer's paragraph aloud and avoid putting it to a student as something they must achieve, since it is a duty on the course."
- statement: qaa/optometry-2024/3.16
  forPractitioner: { text: "Match each assessment type to the layer of Miller's pyramid it targets: knows, knows how, shows how or does.", rewrite: light, force: should, status: drafted }
  forBeneficiary: { text: "not-applicable: a duty on the course in choosing assessment types", rewrite: full, force: should, status: drafted }
  author-agent-written: "Describe this as a recommendation ('should'): assessment types are matched to the layers of Miller's pyramid, set for the registrable integrated master's in Optometry (FHEQ Level 7; FQHEIS Level 11). Cite it as QAA (2024) Optometry Subject Benchmark Statement, para 3.16. Do not claim that the statement itself is a regulatory requirement, or that it covers non-registrable vision science awards. Set it beside 2.9 (design on the pyramid), 3.17 (types of evidence) and 2.3."
  author-agent-dialogue: "Raise this when a team chooses between written, simulated and workplace assessment. Frame it for the programme team or teacher as a duty on the course, in their own planning terms. Ask: Which layer of the pyramid does this task reach, and is that the layer the outcome needs? Avoid reading the issuer's paragraph aloud and avoid putting it to a student as something they must achieve, since it is a duty on the course."
- statement: qaa/optometry-2024/3.18
  forPractitioner: { text: "Assess students' application of knowledge to unfamiliar problems and their research skills; they should be able to show they can practise evidence-based Optometry.", rewrite: light, force: should, status: drafted }
  forBeneficiary: { text: "You should be able to show that you can apply what you know to problems you have not met before and that your practice is based on evidence, with your research skills assessed along the way.", rewrite: full, force: should, status: drafted }
  author-agent-written: "Describe this as a recommendation ('should'): at master's level students apply knowledge to unfamiliar problems and show evidence-based practice, with research skills assessed, set for the registrable integrated master's in Optometry (FHEQ Level 7; FQHEIS Level 11). Cite it as QAA (2024) Optometry Subject Benchmark Statement, para 3.18. Do not claim that it holds at Level 6; the paragraph ties it to master's level. Set it beside 4.5.b4, 4.5.b5, qaa/fheq-2024/4.17.b3, qaa/fheq-2024/4.17.b4.1 and spine:7."
  author-agent-dialogue: "Raise this when a student meets an unfamiliar case or asks why research is assessed. With a student, use plain words and the second person; with staff, frame it as what the course has to let every graduate show. Ask: Faced with a presentation you have never seen, how would you find and weigh the evidence? Avoid reading the issuer's paragraph aloud and avoid presenting research skills as optional for registration."
- statement: qaa/optometry-2024/3.19
  forPractitioner: { text: "Give personal, clear, timely and developmental feedback and feedforward linked to the brief, offer help to interpret it, allow time for reflection, and publish in advance what feedback each task will get and when.", rewrite: light, force: should, status: drafted }
  forBeneficiary: { text: "not-applicable: a duty on the course in giving feedback", rewrite: full, force: should, status: drafted }
  author-agent-written: "Describe this as a recommendation ('should'): feedback and feedforward are personal, timely, developmental and announced in advance, set for the registrable integrated master's in Optometry (FHEQ Level 7; FQHEIS Level 11). Cite it as QAA (2024) Optometry Subject Benchmark Statement, para 3.19. Do not claim that the statement itself is a regulatory requirement, or that it covers non-registrable vision science awards. Set it beside 3.14.b2, 3.20 and 3.21."
  author-agent-dialogue: "Raise this when a team writes an assessment brief or a feedback policy. Frame it for the programme team or teacher as a duty on the course, in their own planning terms. Ask: Do students know before each task what feedback they will get and by when? Avoid reading the issuer's paragraph aloud and avoid putting it to a student as something they must achieve, since it is a duty on the course."
- statement: qaa/optometry-2024/3.21
  forPractitioner: { text: "Combine feedback with feedforward, help students develop the evaluative skill to use it, and always consider the learner's psychological safety when discussing feedback.", rewrite: light, force: should, status: drafted }
  forBeneficiary: { text: "not-applicable: a duty on the course in giving feedback", rewrite: full, force: should, status: drafted }
  author-agent-written: "Describe this as a recommendation ('should'): feedback is joined with feedforward and given with regard to psychological safety, set for the registrable integrated master's in Optometry (FHEQ Level 7; FQHEIS Level 11). Cite it as QAA (2024) Optometry Subject Benchmark Statement, para 3.21. Do not claim that the statement itself is a regulatory requirement, or that it covers non-registrable vision science awards. Set it beside 3.19, 3.20 and 4.5.b12 (well-being)."
  author-agent-dialogue: "Raise this when a teacher prepares to discuss a poor result with a student. Frame it for the programme team or teacher as a duty on the course, in their own planning terms. Ask: How will the student use this feedback next time, and how will you keep the conversation safe? Avoid reading the issuer's paragraph aloud and avoid putting it to a student as something they must achieve, since it is a duty on the course."
- statement: qaa/optometry-2024/4.2
  forPractitioner: { text: "Set your own method for judging evidence of achievement against these standards, referring to Annex D of the Frameworks for Higher Education Qualifications.", rewrite: light, force: should, status: drafted }
  forBeneficiary: { text: "not-applicable: a duty on the provider in judging achievement", rewrite: full, force: should, status: drafted }
  author-agent-written: "Describe this as a recommendation ('should'): providers judge evidence of achievement in their own way, with reference to Annex D, set for the registrable integrated master's in Optometry (FHEQ Level 7; FQHEIS Level 11). Cite it as QAA (2024) Optometry Subject Benchmark Statement, para 4.2. Do not claim that Annex D sets master's grades; it describes classifications at FHEQ Level 6 and FQHEIS Level 10. Set it beside std:doc:qaa-fheq-2024-framework Annex D (qaa/fheq-2024/annex-d/summary/r1/3rd) and 4.1."
  author-agent-dialogue: "Raise this when a team sets marking criteria for the final year. Frame it for the programme team or teacher as a duty on the course, in their own planning terms. Ask: How do your criteria show the step from threshold to higher achievement, and how do they use Annex D? Avoid reading the issuer's paragraph aloud and avoid putting it to a student as something they must achieve, since it is a duty on the course."
- statement: qaa/optometry-2024/4.4.b1
  forPractitioner: { text: "At threshold, graduates will give flexible, individual care that weighs each patient's social, clinical, personal and cultural needs, question and tackle their own biases, and collaborate with other professionals when necessary.", rewrite: light, force: threshold, status: drafted }
  forBeneficiary: { text: "At the threshold, you will be able to fit your care to each patient's social, clinical, personal and cultural needs, question your own biases and work with other professionals when the patient needs it.", rewrite: full, force: threshold, status: drafted }
  author-agent-written: "Describe this as a threshold the award requires: the threshold summary of the regulator's person-centred care category, set for the registrable integrated master's in Optometry (FHEQ Level 7; FQHEIS Level 11). Cite it as QAA (2024) Optometry Subject Benchmark Statement, para 4.4 (Person-centred care). Do not claim that this summary is the General Optical Council's own wording or that it replaces the GOC requirements, nor that it holds at Level 6. Set it beside 3.5.b1 (the same category as an outcome), 1.10 and qaa/fheq-2024/4.17.b5 with spine:7."
  author-agent-dialogue: "Raise this when a student reflects on a consultation that did not go as planned, or a team writes person-centred care outcomes. With a student, use plain words and the second person; with staff, frame it as what the course has to let every graduate show. Ask: How did you find out what mattered to this patient, and did any assumption of yours get in the way? Avoid reading the issuer's paragraph aloud and avoid presenting this as a level above the minimum; it is the threshold every graduate reaches."
- statement: qaa/optometry-2024/4.4.b2
  forPractitioner: { text: "At threshold, graduates will communicate strongly with patients and professionals, adjust their style to individual needs, write and speak proficiently and pick up non-verbal cues.", rewrite: light, force: threshold, status: drafted }
  forBeneficiary: { text: "At the threshold, you will be able to communicate well with patients and other professionals, change your style to suit each person, write and speak clearly and notice what people show without words.", rewrite: full, force: threshold, status: drafted }
  author-agent-written: "Describe this as a threshold the award requires: the threshold summary of the regulator's communication category, set for the registrable integrated master's in Optometry (FHEQ Level 7; FQHEIS Level 11). Cite it as QAA (2024) Optometry Subject Benchmark Statement, para 4.4 (Communication). Do not claim that this summary is the General Optical Council's own wording or that it replaces the GOC requirements, nor that it holds at Level 6; \"need to\" is recorded under the threshold rung. Set it beside 3.5.b2, 3.1.b4, 4.5.b7 and qaa/fheq-2024/4.17.b5."
  author-agent-dialogue: "Raise this when a student prepares to give a patient difficult news, or a team plans communication assessment. With a student, use plain words and the second person; with staff, frame it as what the course has to let every graduate show. Ask: How will you check that the patient has understood, beyond asking if they have? Avoid reading the issuer's paragraph aloud and avoid judging communication only on what is said aloud."
- statement: qaa/optometry-2024/4.4.b3
  forPractitioner: { text: "At threshold, graduates will practise within their individual scope, take accountability and responsibility for patient outcomes, stay within their competence and exercise professional judgement in evidence-informed decisions.", rewrite: light, force: threshold, status: drafted }
  forBeneficiary: { text: "At the threshold, you will work within your scope of practice, take responsibility for how your patients do, stay within what you are competent to do and use professional judgement based on evidence.", rewrite: full, force: threshold, status: drafted }
  author-agent-written: "Describe this as a threshold the award requires: the threshold summary of the regulator's clinical practice category, set for the registrable integrated master's in Optometry (FHEQ Level 7; FQHEIS Level 11). Cite it as QAA (2024) Optometry Subject Benchmark Statement, para 4.4 (Clinical practice). Do not claim that this summary is the General Optical Council's own wording or that it replaces the GOC requirements, nor that it holds at Level 6. Set it beside 3.5.b3, 3.1.b1, 2.3 and qaa/fheq-2024/4.17.b6 with spine:7."
  author-agent-dialogue: "Raise this when a student is unsure whether to manage or refer a patient. With a student, use plain words and the second person; with staff, frame it as what the course has to let every graduate show. Ask: Is this within your competence today, and what evidence guides the choice? Avoid reading the issuer's paragraph aloud and avoid encouraging the student to work beyond their competence."
- statement: qaa/optometry-2024/4.4.b4
  forPractitioner: { text: "At threshold, graduates will uphold professional standards and ethics, act with honesty and integrity, safeguard patients and the public, and make sure their own, supervised and delegated practice meets legal and professional obligations and is fair.", rewrite: light, force: threshold, status: drafted }
  forBeneficiary: { text: "At the threshold, you will keep to high professional and ethical standards, act honestly, protect patients and the public, and make sure your own work and any work you supervise follows the law and professional rules.", rewrite: full, force: threshold, status: drafted }
  author-agent-written: "Describe this as a threshold the award requires: the threshold summary of the regulator's ethics and standards category, set for the registrable integrated master's in Optometry (FHEQ Level 7; FQHEIS Level 11). Cite it as QAA (2024) Optometry Subject Benchmark Statement, para 4.4 (Ethics and standards). Do not claim that this summary is the General Optical Council's own wording or that it replaces the GOC requirements, nor that it holds at Level 6; \"are expected to\" is recorded under the threshold rung. Set it beside 3.5.b4, 3.2.b11 and the Opticians Act 1989 named in the paragraph."
  author-agent-dialogue: "Raise this when a student faces a conflict between a request and professional standards. With a student, use plain words and the second person; with staff, frame it as what the course has to let every graduate show. Ask: Which standard applies here, and who would you ask if you were unsure? Avoid reading the issuer's paragraph aloud and avoid giving legal advice on a particular case."
- statement: qaa/optometry-2024/4.4.b5
  forPractitioner: { text: "At threshold, graduates will safeguard others proactively, understand and keep within their own capabilities, recognise people at risk, and admit mistakes openly and candidly to keep the environment safe.", rewrite: light, force: threshold, status: drafted }
  forBeneficiary: { text: "At the threshold, you will protect patients, colleagues and others from harm, know the limits of your own ability, notice when someone may be at risk and be open about any mistakes you make.", rewrite: full, force: threshold, status: drafted }
  author-agent-written: "Describe this as a threshold the award requires: the threshold summary of the regulator's risk category, candour included, set for the registrable integrated master's in Optometry (FHEQ Level 7; FQHEIS Level 11). Cite it as QAA (2024) Optometry Subject Benchmark Statement, para 4.4 (Risk). Do not claim that this summary is the General Optical Council's own wording or that it replaces the GOC requirements, nor that it holds at Level 6. Set it beside 3.5.b5 and qaa/fheq-2024/4.17.b8.2."
  author-agent-dialogue: "Raise this when a student has made or witnessed an error, or a team plans safeguarding teaching. With a student, use plain words and the second person; with staff, frame it as what the course has to let every graduate show. Ask: What would being open about this mistake involve, and who needs to know? Avoid reading the issuer's paragraph aloud and avoid handling a live safeguarding concern yourself instead of pointing to the right person."
- statement: qaa/optometry-2024/4.4.b6
  forPractitioner: { text: "At threshold, graduates will exercise clinical leadership within scope and competence, and collaborate with teams to take part in clinical governance, service enhancement and public health initiatives.", rewrite: light, force: threshold, status: drafted }
  forBeneficiary: { text: "At the threshold, you will take the lead clinically within your scope of practice and work with other healthcare staff on improving services, clinical governance and public health.", rewrite: full, force: threshold, status: drafted }
  author-agent-written: "Describe this as a threshold the award requires: the threshold summary of the regulator's leadership and management category, set for the registrable integrated master's in Optometry (FHEQ Level 7; FQHEIS Level 11). Cite it as QAA (2024) Optometry Subject Benchmark Statement, para 4.4 (Leadership and management). Do not claim that this summary is the General Optical Council's own wording or that it replaces the GOC requirements, nor that it holds at Level 6. Set it beside 3.5.b6, 4.5.b10 and qaa/fheq-2024/4.17.b8.1."
  author-agent-dialogue: "Raise this when a student asks what leadership looks like for a new registrant. With a student, use plain words and the second person; with staff, frame it as what the course has to let every graduate show. Ask: What small improvement to a service have you seen or suggested, and who did you need on board? Avoid reading the issuer's paragraph aloud and avoid equating clinical leadership with holding a manager's role."
- statement: qaa/optometry-2024/4.4.b7
  forPractitioner: { text: "At threshold, graduates will take personal responsibility for CPD, keep knowledge and skills current within scope, and reflect continually on their own and their peers' performance.", rewrite: light, force: threshold, status: drafted }
  forBeneficiary: { text: "At the threshold, you will take charge of your own professional development, keep your knowledge and skills current and keep reflecting on how you and your peers perform so you can improve.", rewrite: full, force: threshold, status: drafted }
  author-agent-written: "Describe this as a threshold the award requires: the threshold summary of the regulator's lifelong learning category, set for the registrable integrated master's in Optometry (FHEQ Level 7; FQHEIS Level 11). Cite it as QAA (2024) Optometry Subject Benchmark Statement, para 4.4 (Lifelong learning). Do not claim that this summary is the General Optical Council's own wording or that it replaces the GOC requirements, nor that it holds at Level 6. Set it beside 3.5.b7, 3.1.b5, 4.5.b6 and qaa/fheq-2024/4.17.b8.3."
  author-agent-dialogue: "Raise this when a student plans their learning after registration, or a team designs a CPD-style portfolio. With a student, use plain words and the second person; with staff, frame it as what the course has to let every graduate show. Ask: What did your last reflection change in your practice, and what will you learn next? Avoid reading the issuer's paragraph aloud and avoid treating reflection as a record of events."
- statement: qaa/optometry-2024/4.5.b1
  forPractitioner: { text: "At threshold, graduates of the master's should be able to identify the issues, questions and problems in a situation; design teaching and assessment so every student can show it.", rewrite: light, force: should, status: drafted }
  forBeneficiary: { text: "By the time you graduate, you should be able to pick out the issues, questions and problems a situation raises.", rewrite: full, force: should, status: drafted }
  author-agent-written: "Describe this as a threshold expectation, worded 'should be able to': a generic skill in which graduates identify the issues, questions and problems in a situation, set for the registrable integrated master's in Optometry (FHEQ Level 7; FQHEIS Level 11). Cite it as QAA (2024) Optometry Subject Benchmark Statement, para 4.5 (generic skill 1). Do not claim that it is a regulatory requirement or a typical or excellent standard, or that it holds at Level 6. Set it beside qaa/fheq-2024/4.17.b5, spine:7 and the other generic skills 4.5.b1 to 4.5.b16."
  author-agent-dialogue: "Raise this when a case presents several problems at once. With a student, use plain words and the second person; with staff, frame it as what the course has to let every graduate show. Ask: What is the real question here, before you look for an answer? Avoid reading the issuer's paragraph aloud and avoid presenting it as more than the threshold every graduate is expected to show."
- statement: qaa/optometry-2024/4.5.b2
  forPractitioner: { text: "At threshold, graduates of the master's should be able to use knowledge, understanding and critical thinking to make decisions based on evidence; design teaching and assessment so every student can show it.", rewrite: light, force: should, status: drafted }
  forBeneficiary: { text: "By the time you graduate, you should be able to apply what you know and think critically to reach decisions grounded in evidence.", rewrite: full, force: should, status: drafted }
  author-agent-written: "Describe this as a threshold expectation, worded 'should be able to': a generic skill in which graduates use knowledge, understanding and critical thinking to make decisions based on evidence, set for the registrable integrated master's in Optometry (FHEQ Level 7; FQHEIS Level 11). Cite it as QAA (2024) Optometry Subject Benchmark Statement, para 4.5 (generic skill 2). Do not claim that it is a regulatory requirement or a typical or excellent standard, or that it holds at Level 6. Set it beside qaa/fheq-2024/4.17.b5 and 3.1.b2, spine:7 and the other generic skills 4.5.b1 to 4.5.b16."
  author-agent-dialogue: "Raise this when a student explains a decision. With a student, use plain words and the second person; with staff, frame it as what the course has to let every graduate show. Ask: What evidence did you weigh, and what would have changed your mind? Avoid reading the issuer's paragraph aloud and avoid presenting it as more than the threshold every graduate is expected to show."
- statement: qaa/optometry-2024/4.5.b3
  forPractitioner: { text: "At threshold, graduates of the master's should be able to spot where their own knowledge falls short and learn what is missing; design teaching and assessment so every student can show it.", rewrite: light, force: should, status: drafted }
  forBeneficiary: { text: "By the time you graduate, you should be able to notice where your own knowledge runs out and go and learn what you need.", rewrite: full, force: should, status: drafted }
  author-agent-written: "Describe this as a threshold expectation, worded 'should be able to': a generic skill in which graduates spot where their own knowledge falls short and learn what is missing, set for the registrable integrated master's in Optometry (FHEQ Level 7; FQHEIS Level 11). Cite it as QAA (2024) Optometry Subject Benchmark Statement, para 4.5 (generic skill 3). Do not claim that it is a regulatory requirement or a typical or excellent standard, or that it holds at Level 6. Set it beside qaa/fheq-2024/4.17.b7, spine:7 and the other generic skills 4.5.b1 to 4.5.b16."
  author-agent-dialogue: "Raise this when a student meets something they do not know. With a student, use plain words and the second person; with staff, frame it as what the course has to let every graduate show. Ask: How did you realise you did not know this, and where will you learn it? Avoid reading the issuer's paragraph aloud and avoid presenting it as more than the threshold every graduate is expected to show."
- statement: qaa/optometry-2024/4.5.b4
  forPractitioner: { text: "At threshold, graduates of the master's should be able to judge research and other sources critically and put them to use; design teaching and assessment so every student can show it.", rewrite: light, force: should, status: drafted }
  forBeneficiary: { text: "By the time you graduate, you should be able to judge research and other sources critically and use them well.", rewrite: full, force: should, status: drafted }
  author-agent-written: "Describe this as a threshold expectation, worded 'should be able to': a generic skill in which graduates judge research and other sources critically and put them to use, set for the registrable integrated master's in Optometry (FHEQ Level 7; FQHEIS Level 11). Cite it as QAA (2024) Optometry Subject Benchmark Statement, para 4.5 (generic skill 4). Do not claim that it is a regulatory requirement or a typical or excellent standard, or that it holds at Level 6. Set it beside qaa/fheq-2024/4.17.b4.1 and 3.1.b3, spine:7 and the other generic skills 4.5.b1 to 4.5.b16."
  author-agent-dialogue: "Raise this when a student relies on a single source. With a student, use plain words and the second person; with staff, frame it as what the course has to let every graduate show. Ask: How strong is this evidence, and does it apply to your patient? Avoid reading the issuer's paragraph aloud and avoid presenting it as more than the threshold every graduate is expected to show."
- statement: qaa/optometry-2024/4.5.b5
  forPractitioner: { text: "At threshold, graduates of the master's should be able to show they understand how established research and enquiry methods produce and interpret disciplinary knowledge; design teaching and assessment so every student can show it.", rewrite: light, force: should, status: drafted }
  forBeneficiary: { text: "By the time you graduate, you should be able to show you understand how research methods build and interpret what is known in your field.", rewrite: full, force: should, status: drafted }
  author-agent-written: "Describe this as a threshold expectation, worded 'should be able to': a generic skill in which graduates show they understand how established research and enquiry methods produce and interpret disciplinary knowledge, set for the registrable integrated master's in Optometry (FHEQ Level 7; FQHEIS Level 11). Cite it as QAA (2024) Optometry Subject Benchmark Statement, para 4.5 (generic skill 5). Do not claim that it is a regulatory requirement or a typical or excellent standard, or that it holds at Level 6. Set it beside qaa/fheq-2024/4.17.b3 (closely echoed: Part E), spine:7 and the other generic skills 4.5.b1 to 4.5.b16."
  author-agent-dialogue: "Raise this when a student asks why research methods are taught. With a student, use plain words and the second person; with staff, frame it as what the course has to let every graduate show. Ask: How was the evidence behind this test or treatment produced, and what are its limits? Avoid reading the issuer's paragraph aloud and avoid presenting it as more than the threshold every graduate is expected to show."
- statement: qaa/optometry-2024/4.5.b6
  forPractitioner: { text: "At threshold, graduates of the master's should be able to practise reflection to support continuing professional development; design teaching and assessment so every student can show it.", rewrite: light, force: should, status: drafted }
  forBeneficiary: { text: "By the time you graduate, you should be able to reflect on your practice in ways that support your continuing development.", rewrite: full, force: should, status: drafted }
  author-agent-written: "Describe this as a threshold expectation, worded 'should be able to': a generic skill in which graduates practise reflection to support continuing professional development, set for the registrable integrated master's in Optometry (FHEQ Level 7; FQHEIS Level 11). Cite it as QAA (2024) Optometry Subject Benchmark Statement, para 4.5 (generic skill 6). Do not claim that it is a regulatory requirement or a typical or excellent standard, or that it holds at Level 6. Set it beside qaa/fheq-2024/4.17.b8.3, 4.4.b7 and 3.1.b5, spine:7 and the other generic skills 4.5.b1 to 4.5.b16."
  author-agent-dialogue: "Raise this when a student writes a reflection. With a student, use plain words and the second person; with staff, frame it as what the course has to let every graduate show. Ask: What will you do differently, and how will you check it worked? Avoid reading the issuer's paragraph aloud and avoid presenting it as more than the threshold every graduate is expected to show."
- statement: qaa/optometry-2024/4.5.b7
  forPractitioner: { text: "At threshold, graduates of the master's should be able to communicate effectively and appropriately with and without words; design teaching and assessment so every student can show it.", rewrite: light, force: should, status: drafted }
  forBeneficiary: { text: "By the time you graduate, you should be able to communicate effectively and suitably, both in words and in other ways.", rewrite: full, force: should, status: drafted }
  author-agent-written: "Describe this as a threshold expectation, worded 'should be able to': a generic skill in which graduates communicate effectively and appropriately with and without words, set for the registrable integrated master's in Optometry (FHEQ Level 7; FQHEIS Level 11). Cite it as QAA (2024) Optometry Subject Benchmark Statement, para 4.5 (generic skill 7). Do not claim that it is a regulatory requirement or a typical or excellent standard, or that it holds at Level 6. Set it beside qaa/fheq-2024/4.17.b5 and 4.4.b2, spine:7 and the other generic skills 4.5.b1 to 4.5.b16."
  author-agent-dialogue: "Raise this when a student prepares for a consultation. With a student, use plain words and the second person; with staff, frame it as what the course has to let every graduate show. Ask: How will your manner and body language help or hinder this conversation? Avoid reading the issuer's paragraph aloud and avoid presenting it as more than the threshold every graduate is expected to show."
- statement: qaa/optometry-2024/4.5.b8
  forPractitioner: { text: "At threshold, graduates of the master's should be able to handle a range of data and digital tools to gather and analyse information; design teaching and assessment so every student can show it.", rewrite: light, force: should, status: drafted }
  forBeneficiary: { text: "By the time you graduate, you should be able to work with different kinds of data and digital tools to gather and analyse information.", rewrite: full, force: should, status: drafted }
  author-agent-written: "Describe this as a threshold expectation, worded 'should be able to': a generic skill in which graduates handle a range of data and digital tools to gather and analyse information, set for the registrable integrated master's in Optometry (FHEQ Level 7; FQHEIS Level 11). Cite it as QAA (2024) Optometry Subject Benchmark Statement, para 4.5 (generic skill 8). Do not claim that it is a regulatory requirement or a typical or excellent standard, or that it holds at Level 6. Set it beside qaa/fheq-2024/4.17.b2, spine:7 and the other generic skills 4.5.b1 to 4.5.b16."
  author-agent-dialogue: "Raise this when a student meets imaging or record systems. With a student, use plain words and the second person; with staff, frame it as what the course has to let every graduate show. Ask: Which digital tools do you rely on, and how do you check their output? Avoid reading the issuer's paragraph aloud and avoid presenting it as more than the threshold every graduate is expected to show."
- statement: qaa/optometry-2024/4.5.b9
  forPractitioner: { text: "At threshold, graduates of the master's should be able to adjust to technology as it changes; design teaching and assessment so every student can show it.", rewrite: light, force: should, status: drafted }
  forBeneficiary: { text: "By the time you graduate, you should be able to adjust as the technology you use changes.", rewrite: full, force: should, status: drafted }
  author-agent-written: "Describe this as a threshold expectation, worded 'should be able to': a generic skill in which graduates adjust to technology as it changes, set for the registrable integrated master's in Optometry (FHEQ Level 7; FQHEIS Level 11). Cite it as QAA (2024) Optometry Subject Benchmark Statement, para 4.5 (generic skill 9). Do not claim that it is a regulatory requirement or a typical or excellent standard, or that it holds at Level 6. Set it beside qaa/fheq-2024/4.17.b7 and 2.16, spine:7 and the other generic skills 4.5.b1 to 4.5.b16."
  author-agent-dialogue: "Raise this when a new device or AI tool enters practice. With a student, use plain words and the second person; with staff, frame it as what the course has to let every graduate show. Ask: How would you learn to use and question a new tool safely? Avoid reading the issuer's paragraph aloud and avoid presenting it as more than the threshold every graduate is expected to show."
- statement: qaa/optometry-2024/4.5.b10
  forPractitioner: { text: "At threshold, graduates of the master's should be able to work with others, in groups or teams and in discussion; design teaching and assessment so every student can show it.", rewrite: light, force: should, status: drafted }
  forBeneficiary: { text: "By the time you graduate, you should be able to work well with others in groups and teams and take part in discussion.", rewrite: full, force: should, status: drafted }
  author-agent-written: "Describe this as a threshold expectation, worded 'should be able to': a generic skill in which graduates work with others, in groups or teams and in discussion, set for the registrable integrated master's in Optometry (FHEQ Level 7; FQHEIS Level 11). Cite it as QAA (2024) Optometry Subject Benchmark Statement, para 4.5 (generic skill 10). Do not claim that it is a regulatory requirement or a typical or excellent standard, or that it holds at Level 6. Set it beside qaa/fheq-2024/4.17.b8.1 and 4.4.b6, spine:7 and the other generic skills 4.5.b1 to 4.5.b16."
  author-agent-dialogue: "Raise this when group work goes badly or a team role is unclear. With a student, use plain words and the second person; with staff, frame it as what the course has to let every graduate show. Ask: What did you contribute to the group, and what did others bring that you could not? Avoid reading the issuer's paragraph aloud and avoid presenting it as more than the threshold every graduate is expected to show."
- statement: qaa/optometry-2024/4.5.b11
  forPractitioner: { text: "At threshold, graduates of the master's should be able to bring theory and practice of equality, diversity and inclusion into the workplace; design teaching and assessment so every student can show it.", rewrite: light, force: should, status: drafted }
  forBeneficiary: { text: "By the time you graduate, you should be able to bring what you know about equality, diversity and inclusion into how you work.", rewrite: full, force: should, status: drafted }
  author-agent-written: "Describe this as a threshold expectation, worded 'should be able to': a generic skill in which graduates bring theory and practice of equality, diversity and inclusion into the workplace, set for the registrable integrated master's in Optometry (FHEQ Level 7; FQHEIS Level 11). Cite it as QAA (2024) Optometry Subject Benchmark Statement, para 4.5 (generic skill 11). Do not claim that it is a regulatory requirement or a typical or excellent standard, or that it holds at Level 6. Set it beside spine:7, 1.9 and 1.10, spine:7 and the other generic skills 4.5.b1 to 4.5.b16."
  author-agent-dialogue: "Raise this when a student discusses fairness in access to eye care. With a student, use plain words and the second person; with staff, frame it as what the course has to let every graduate show. Ask: Which patients find it hardest to reach the care you give, and what could you change? Avoid reading the issuer's paragraph aloud and avoid presenting it as more than the threshold every graduate is expected to show."
- statement: qaa/optometry-2024/4.5.b12
  forPractitioner: { text: "At threshold, graduates of the master's should be able to take to heart how well-being, mental health and emotion bear on learning, and act on it; design teaching and assessment so every student can show it.", rewrite: light, force: should, status: drafted }
  forBeneficiary: { text: "By the time you graduate, you should be able to take seriously, and act on, how well-being, mental health and emotions affect your learning.", rewrite: full, force: should, status: drafted }
  author-agent-written: "Describe this as a threshold expectation, worded 'should be able to': a generic skill in which graduates take to heart how well-being, mental health and emotion bear on learning, and act on it, set for the registrable integrated master's in Optometry (FHEQ Level 7; FQHEIS Level 11). Cite it as QAA (2024) Optometry Subject Benchmark Statement, para 4.5 (generic skill 12). Do not claim that it is a regulatory requirement or a typical or excellent standard, or that it holds at Level 6. Set it beside qaa/fheq-2024/4.17.b8.1 and 3.21, spine:7 and the other generic skills 4.5.b1 to 4.5.b16."
  author-agent-dialogue: "Raise this when a student is under pressure before assessments. With a student, use plain words and the second person; with staff, frame it as what the course has to let every graduate show. Ask: What helps you learn well when things are hard, and what gets in the way? Avoid reading the issuer's paragraph aloud and avoid presenting it as more than the threshold every graduate is expected to show."
- statement: qaa/optometry-2024/4.5.b13
  forPractitioner: { text: "At threshold, graduates of the master's should be able to use sustainable ways of working, from waste and recycling to environmentally aware procedures; design teaching and assessment so every student can show it.", rewrite: light, force: should, status: drafted }
  forBeneficiary: { text: "By the time you graduate, you should be able to work in sustainable ways, including handling waste, recycling and following environmentally aware procedures.", rewrite: full, force: should, status: drafted }
  author-agent-written: "Describe this as a threshold expectation, worded 'should be able to': a generic skill in which graduates use sustainable ways of working, from waste and recycling to environmentally aware procedures, set for the registrable integrated master's in Optometry (FHEQ Level 7; FQHEIS Level 11). Cite it as QAA (2024) Optometry Subject Benchmark Statement, para 4.5 (generic skill 13). Do not claim that it is a regulatory requirement or a typical or excellent standard, or that it holds at Level 6. Set it beside spine:7 and 1.17, spine:7 and the other generic skills 4.5.b1 to 4.5.b16."
  author-agent-dialogue: "Raise this when a team or student considers the environmental cost of practice. With a student, use plain words and the second person; with staff, frame it as what the course has to let every graduate show. Ask: What does your clinic throw away, and what could be done differently? Avoid reading the issuer's paragraph aloud and avoid presenting it as more than the threshold every graduate is expected to show."
- statement: qaa/optometry-2024/4.5.b14
  forPractitioner: { text: "At threshold, graduates of the master's should be able to recognise and challenge cultural and ethnocentric assumptions and value other ways of being; design teaching and assessment so every student can show it.", rewrite: light, force: should, status: drafted }
  forBeneficiary: { text: "By the time you graduate, you should be able to recognise and challenge cultural assumptions, including your own, and respect other ways of living.", rewrite: full, force: should, status: drafted }
  author-agent-written: "Describe this as a threshold expectation, worded 'should be able to': a generic skill in which graduates recognise and challenge cultural and ethnocentric assumptions and value other ways of being, set for the registrable integrated master's in Optometry (FHEQ Level 7; FQHEIS Level 11). Cite it as QAA (2024) Optometry Subject Benchmark Statement, para 4.5 (generic skill 14). Do not claim that it is a regulatory requirement or a typical or excellent standard, or that it holds at Level 6. Set it beside qaa/fheq-2024/4.17.b1 and 1.11, spine:7 and the other generic skills 4.5.b1 to 4.5.b16."
  author-agent-dialogue: "Raise this when a student meets a patient whose views differ from theirs. With a student, use plain words and the second person; with staff, frame it as what the course has to let every graduate show. Ask: Which of your own assumptions did this patient make you notice? Avoid reading the issuer's paragraph aloud and avoid presenting it as more than the threshold every graduate is expected to show."
- statement: qaa/optometry-2024/4.5.b15
  forPractitioner: { text: "At threshold, graduates of the master's should be able to show awareness of how business and commercial operations work; design teaching and assessment so every student can show it.", rewrite: light, force: should, status: drafted }
  forBeneficiary: { text: "By the time you graduate, you should be able to show you understand how businesses and commercial practices work.", rewrite: full, force: should, status: drafted }
  author-agent-written: "Describe this as a threshold expectation, worded 'should be able to': a generic skill in which graduates show awareness of how business and commercial operations work, set for the registrable integrated master's in Optometry (FHEQ Level 7; FQHEIS Level 11). Cite it as QAA (2024) Optometry Subject Benchmark Statement, para 4.5 (generic skill 15). Do not claim that it is a regulatory requirement or a typical or excellent standard, or that it holds at Level 6. Set it beside qaa/fheq-2024/4.17.b8.2 and 1.19, spine:7 and the other generic skills 4.5.b1 to 4.5.b16."
  author-agent-dialogue: "Raise this when a student asks about working in or owning a practice. With a student, use plain words and the second person; with staff, frame it as what the course has to let every graduate show. Ask: How does a practice you know pay its way, and what pressures does that create? Avoid reading the issuer's paragraph aloud and avoid presenting it as more than the threshold every graduate is expected to show."
- statement: qaa/optometry-2024/4.5.b16
  forPractitioner: { text: "At threshold, graduates of the master's should be able to show creativity and originality in solving problems and in developing and communicating ideas; design teaching and assessment so every student can show it.", rewrite: light, force: should, status: drafted }
  forBeneficiary: { text: "By the time you graduate, you should be able to be creative and original when solving problems and when developing and putting across ideas.", rewrite: full, force: should, status: drafted }
  author-agent-written: "Describe this as a threshold expectation, worded 'should be able to': a generic skill in which graduates show creativity and originality in solving problems and in developing and communicating ideas, set for the registrable integrated master's in Optometry (FHEQ Level 7; FQHEIS Level 11). Cite it as QAA (2024) Optometry Subject Benchmark Statement, para 4.5 (generic skill 16). Do not claim that it is a regulatory requirement or a typical or excellent standard, or that it holds at Level 6. Set it beside qaa/fheq-2024/4.17.b6, spine:7 and the other generic skills 4.5.b1 to 4.5.b16."
  author-agent-dialogue: "Raise this when a student tackles an open-ended project. With a student, use plain words and the second person; with staff, frame it as what the course has to let every graduate show. Ask: What would a fresh approach to this problem look like? Avoid reading the issuer's paragraph aloud and avoid presenting it as more than the threshold every graduate is expected to show."
```

### S5 Levels and alignment
<!-- label: both; status: drafted; basis: primary -->
```yaml
levels:
  - { id: "fheq:7", role: "cites", locator: "D1, front matter: Relationship to legislation" }
  - { id: "fqheis:11", role: "cites", locator: "D1, front matter: Relationship to legislation" }
  - { id: "fheq:6", role: "cites", locator: "D1, front matter: the BSc this award replaces" }
  - { id: "fqheis:10", role: "cites", locator: "D1, front matter: the BSc this award replaces" }
  - { id: "spine:7", role: "refers", locator: "std:ref:uk-framework R2 and R8 (inferred: Part E)" }
crosswalks:
  - { from: "fheq:7", to: "fqheis:11", relation: "equivalent", basis: "stated (D1, front matter: \"integrated master's (FHEQ Level 7; FQHEIS Level 11)\")" }
  - { from: "fheq:6", to: "fqheis:10", relation: "equivalent", basis: "stated (D1, front matter: the BSc in Optometry at FHEQ Level 6, FQHEIS Level 10)" }
  - { from: "fheq:7", to: "cqfw:7", relation: "compares-with", basis: "inferred from std:doc:qaa-fheq-2024-framework 2.24 and std:ref:uk-framework R2 (Part E)" }
```

### S6 Themes
<!-- label: both; status: drafted; basis: primary -->
```yaml
- { id: "theme:edi", role: "carries", carriedIn: ["1.9", "1.10", "1.11", "1.12", "1.13", "2.24", "3.2", "4.5"] }
- { id: "theme:accessibility", role: "carries", carriedIn: ["1.14", "1.15", "1.16", "2.26", "3.9", "3.11", "3.14"] }
- { id: "theme:esd", role: "carries", carriedIn: ["1.17", "2.24", "4.5"] }
- { id: "theme:enterprise", role: "carries", carriedIn: ["1.18", "1.19", "1.20", "1.21", "1.22", "2.18", "3.12", "4.5"] }
```

### S7 Relations
<!-- label: both; status: drafted; basis: primary -->
```yaml
- { rel: "partOf", target: "collection: QAA Subject Benchmark Statements", note: "one of 54 held by stan" }
- { rel: "supersedes", target: "std:doc:qaa-optometry-2019-benchmarks (not yet ingested)", note: "the 2019 BSc statement is subsumed here but still available separately (front matter)" }
- { rel: "refersTo", target: "std:doc:qaa-fheq-2024-framework, Annex D", note: "providers refer to it for evidence of achievement (4.2); it describes Level 6 and FQHEIS Level 10 classes" }
- { rel: "refersTo", target: "std:doc:qaa-fheq-2024-framework", note: "FHEQ Levels 6 and 7 (front matter)" }
- { rel: "refersTo", target: "std:doc:qaa-fqheis-2024-framework", note: "FQHEIS Levels 10 and 11 (front matter)" }
- { rel: "refersTo", target: "std:doc:qaa-advancehe-esd-2021-guidance", note: "ESD guidance (1.17)" }
- { rel: "refersTo", target: "std:doc:qaa-enterprise-2018-guidance", note: "enterprise and entrepreneurship guidance (1.22)" }
- { rel: "refersTo", target: "General Optical Council, Requirements for Approved Qualifications in Optometry or Dispensing Optics (not yet ingested)", note: "front matter, 2.5, 3.4: the regulator's outcomes this statement summarises" }
- { rel: "refersTo", target: "QAA Quality Code, Advice and Guidance (not yet ingested)", note: "front matter, 2.22" }
```

### S8 Currency and review
<!-- label: source; status: drafted; basis: primary -->
```yaml
published: "2024-04"
lastReviewed: "none-stated"
reviewCycle: "none-stated"
consultation: "none-stated; an advisory group is named (section 6)"
replacedBy: "none"
```

### S9 Commentary (optional)
<!-- label: editorial; status: drafted; basis: secondary -->
`unknown`: not researched in P1 (Part E).

### SB1 The subject
<!-- label: both; status: drafted; basis: primary -->
- Optometry joins scientific knowledge with patient-facing clinical skill to secure the best vision and eye health; optometrists are registered healthcare professionals who detect, diagnose, manage and rehabilitate conditions of the eye and visual system (D1, 1.1).
- It is a regulated profession: the General Optical Council approves qualifications, and some functions such as sight testing and contact lens fitting are reserved by law (D1, front matter; 1.3).
- Its graduates work mainly in community primary care but also in hospitals, private clinics, universities, charities and industry, often in portfolio careers (D1, 1.2).
- Its course is a single-subject integrated master's that leads to registration, built as a spiral curriculum from theory and simulation to extended placements (D1, front matter; 1.7; 2.2 to 2.4; 2.8).
- Its standards follow the regulator's seven categories: person-centred care, communication, clinical practice, ethics and standards, risk, leadership and management, and lifelong learning (D1, 2.5; 3.4; 4.4).
- Clinical competence is framed by Miller's pyramid, from knowing to doing, in both design and assessment (D1, 2.9; 3.16).
- Patients and students are treated as partners in designing and reviewing courses (D1, 2.20; 2.21).

### SB2 Themes in this subject
<!-- label: both; status: drafted; basis: primary -->
```yaml
- theme: theme:edi
  inThisSubject: "evidence-based but personalised care for every patient; diverse contributors and patient presentations in the curriculum; social determinants, disparities, bias and disability as content; EDI in practice as a generic skill (D1, 1.9 to 1.13; 3.2; 4.5)"
  statements: ["qaa/optometry-2024/1.10", "qaa/optometry-2024/1.11", "qaa/optometry-2024/1.13", "qaa/optometry-2024/4.5.b11", "qaa/optometry-2024/4.5.b14"]
- theme: theme:accessibility
  inThisSubject: "access by inclusive design and reasonable adjustment, bounded by patient safety and the regulator's standards; accessible clinical elements (D1, 1.14 to 1.16; 3.11; 3.14)"
  statements: ["qaa/optometry-2024/1.14", "qaa/optometry-2024/1.15", "qaa/optometry-2024/1.16", "qaa/optometry-2024/3.14.b3"]
- theme: theme:esd
  inThisSubject: "visual health as a global and community health challenge, with the UN goals for health and environment as possible topics; sustainable working and waste in practice (D1, 1.17; 2.24; 4.5)"
  statements: ["qaa/optometry-2024/1.17", "qaa/optometry-2024/2.24", "qaa/optometry-2024/4.5.b13"]
- theme: theme:enterprise
  inThisSubject: "many registrants own or franchise practices or work in commercial, manufacturing or charitable settings; employability as a core outcome with placements and employer contact (D1, 1.18 to 1.22; 2.18; 3.12; 4.5)"
  statements: ["qaa/optometry-2024/1.18", "qaa/optometry-2024/1.19", "qaa/optometry-2024/2.18", "qaa/optometry-2024/4.5.b15"]
```

### SB3 Content and delivery
<!-- label: both; status: drafted; basis: primary -->
```yaml
areas:
  - { component: "3.1", gloss: "three topic areas: basic and clinical sciences; law, professional standards and ethics; leadership and management" }
  - { component: "3.2", gloss: "optics, ophthalmic devices, perception, ocular biology and disease, imaging, pharmacology, statistics, law and ethics, communication, AI, and social determinants of eye health" }
  - { component: "3.3", gloss: "history-taking, visual function, examination techniques, clinical decision-making, prescribing and dispensing, diagnosis and management, evidence-based practice" }
  - { component: "3.4", gloss: "the regulator's seven outcome categories for registration" }
practices:
  - { component: "3.6", kind: "teaching", gloss: "authentic clinical learning and reflective practice, methods not prescribed" }
  - { component: "3.9", kind: "teaching", gloss: "synchronous, asynchronous and blended delivery; experiential learning across clinical settings; simulation" }
  - { component: "3.10", kind: "learning", gloss: "lectures, labs, workshops, problem- and team-based learning, simulations, placements, portfolios and research projects" }
  - { component: "3.12", kind: "assessment", gloss: "authentic, rigorous assessment mapped to every regulator outcome and able to separate threshold from higher achievement" }
  - { component: "3.16", kind: "assessment", gloss: "assessment matched to the layers of Miller's pyramid" }
  - { component: "3.17", kind: "assessment", gloss: "written evidence (reports, essays, logbooks, examinations) and practical evidence (OSCEs, observed encounters, EPAs)" }
  - { component: "3.19", kind: "assessment", gloss: "personal, timely feedback and feedforward" }
```

### SB4 Benchmark standards
<!-- label: both; status: drafted; basis: primary -->
```yaml
rungs:
  - { rung: "threshold", leadIn: "4.3", award: "integrated master's", items: 23 }
rungBases: "threshold only: 4.1 and 4.3 define it as what a student has shown on being awarded the master's; 4.4 summarises the regulator's seven categories at threshold and 4.5 lists generic skills, which 2.7 calls threshold-level; no typical or excellent rung; 4.2 points to Annex D for evidence of achievement"
outcomeLists:
  - { leadIn: "3.1", gloss: "key skills courses should equip graduates with", items: 5, award: ["integrated master's"] }
  - { leadIn: "3.5", gloss: "the regulator's outcomes for registration, as abilities", items: 7, award: ["integrated master's"] }
outcomes:
  - { outcome: "person-centred care", threshold: "qaa/optometry-2024/4.4.b1", typical: "none", excellent: "none", basis: "stated", domain: "subject-skill", award: "integrated master's" }
  - { outcome: "communication", threshold: "qaa/optometry-2024/4.4.b2", typical: "none", excellent: "none", basis: "stated", domain: "generic-skill", award: "integrated master's" }
  - { outcome: "clinical practice", threshold: "qaa/optometry-2024/4.4.b3", typical: "none", excellent: "none", basis: "stated", domain: "subject-skill", award: "integrated master's" }
  - { outcome: "ethics and standards", threshold: "qaa/optometry-2024/4.4.b4", typical: "none", excellent: "none", basis: "stated", domain: "subject-skill", award: "integrated master's" }
  - { outcome: "risk", threshold: "qaa/optometry-2024/4.4.b5", typical: "none", excellent: "none", basis: "stated", domain: "subject-skill", award: "integrated master's" }
  - { outcome: "leadership and management", threshold: "qaa/optometry-2024/4.4.b6", typical: "none", excellent: "none", basis: "stated", domain: "subject-skill", award: "integrated master's" }
  - { outcome: "lifelong learning", threshold: "qaa/optometry-2024/4.4.b7", typical: "none", excellent: "none", basis: "stated", domain: "generic-skill", award: "integrated master's" }
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
- { body: "General Optical Council (GOC)", says: "the statutory regulator for the optical professions in the UK, under the Opticians Act 1989: it approves qualifications, sets standards, keeps the registers and handles fitness to practise; its 2021 requirements for approved qualifications drive the move to the integrated master's; students must by law stay registered with it throughout, and providers check this; its seven outcome categories frame the standards (D1, front matter; 2.2; 2.5; 3.1; 3.4; 3.5; 3.12; 4.4)", requirements: "not yet ingested (Part E)" }
- { body: "Optometry Schools Council", says: "an education and professional body whose expectations providers may consider (D1, front matter)", requirements: "not-applicable-by-design" }
- { body: "Sector Partnership for Optical Knowledge and Education (SPOKE)", says: "an education and professional body providers may consider; listed under the College of Optometrists in the references (D1, front matter; section 5)", requirements: "not-applicable-by-design" }
- { body: "Office for Students (OfS)", says: "in England, benchmark statements are not sector-recognised standards under its framework; it gives guidance on monitoring placement activity (D1, front matter; 2.22)", requirements: "not-applicable-by-design" }
```

### SB6 Cross-cutting references
<!-- label: both; status: drafted; basis: primary -->
```yaml
themes:
  - { id: "theme:edi", named: "Equality, diversity and inclusion", carriedIn: ["front matter", "1.9", "1.10", "1.11", "1.12", "1.13", "2.24", "3.2", "4.5"], statements: ["qaa/optometry-2024/1.10", "qaa/optometry-2024/1.11", "qaa/optometry-2024/1.13", "qaa/optometry-2024/2.24", "qaa/optometry-2024/4.5.b11", "qaa/optometry-2024/4.5.b14"] }
  - { id: "theme:accessibility", named: "Accessibility (front matter: accessibility and the needs of disabled students)", carriedIn: ["front matter", "1.14", "1.15", "1.16", "2.26", "3.9", "3.11", "3.14"], statements: ["qaa/optometry-2024/1.14", "qaa/optometry-2024/1.15", "qaa/optometry-2024/1.16", "qaa/optometry-2024/2.26", "qaa/optometry-2024/3.14.b3"] }
  - { id: "theme:esd", named: "Education for sustainable development", carriedIn: ["front matter", "1.17", "2.24", "4.5"], statements: ["qaa/optometry-2024/1.17", "qaa/optometry-2024/2.24", "qaa/optometry-2024/4.5.b13"] }
  - { id: "theme:enterprise", named: "Employability, enterprise and entrepreneurship (front matter: employability, entrepreneurship and enterprise education)", carriedIn: ["front matter", "1.18", "1.19", "1.20", "1.21", "1.22", "2.18", "3.12", "4.5"], statements: ["qaa/optometry-2024/1.18", "qaa/optometry-2024/1.19", "qaa/optometry-2024/2.18", "qaa/optometry-2024/3.12", "qaa/optometry-2024/4.5.b15"] }
frameworks:
  - { framework: "fheq", levels: ["fheq:6", "fheq:7"], citedIn: ["front matter", "4.2"] }
  - { framework: "scqf", levels: ["fqheis:10", "fqheis:11"], citedIn: ["front matter"] }
bodies:
  - { body: "General Optical Council", citedIn: ["front matter", "1.4", "2.2", "2.5", "3.1", "3.4", "3.5", "3.12", "4.4"] }
  - { body: "Optometry Schools Council", citedIn: ["front matter"] }
  - { body: "Sector Partnership for Optical Knowledge and Education", citedIn: ["front matter"] }
  - { body: "Office for Students", citedIn: ["front matter", "2.22"] }
  - { body: "Universities UK", citedIn: ["2.22"] }
sharedDocuments:
  - { document: "std:doc:qaa-fheq-2024-framework, Annex D", named: "Annex D in The Frameworks for Higher Education Qualifications of UK Degree-Awarding Bodies", citedIn: ["4.2"], role: "providers refer to it in deciding evidence of achievement" }
  - { document: "std:doc:qaa-advancehe-esd-2021-guidance", named: "the QAA and Advance HE guidance (on education for sustainable development)", citedIn: ["1.17"], role: "further information on the ESD theme" }
  - { document: "std:doc:qaa-enterprise-2018-guidance", named: "Enterprise and Entrepreneurship Education: Guidance for UK Higher Education Providers", citedIn: ["1.22"], role: "further information on the enterprise theme" }
  - { document: "QAA Quality Code, Advice and Guidance (not yet ingested)", named: "Advice and Guidance to support the Quality Code; QAA advice and guidance", citedIn: ["front matter", "2.22"], role: "course design, teaching, external expertise, monitoring" }
  - { document: "QAA Glossary (not ingested)", named: "QAA's Glossary", citedIn: ["front matter"], role: "explains unfamiliar terms" }
  - { document: "Opticians Act 1989 (law)", named: "Opticians Act 1989", citedIn: ["front matter", "1.3", "4.4"], role: "the regulator's powers, reserved functions, student registration" }
  - { document: "Equality Act 2010 (law)", named: "Equality Act 2010", citedIn: ["1.14"], role: "duties behind accessibility" }
  - { document: "UN Sustainable Development Goals (external)", named: "United Nations Sustainable Development Goals", citedIn: ["1.17"], role: "possible source of ESD topics" }
  - { document: "General Optical Council requirements for approved qualifications (not yet ingested: Part E)", named: "Requirements for Approved Qualifications in Optometry or Dispensing Optics; Outcomes for GOC registration; Standards of Practice", citedIn: ["front matter", "2.5", "3.4", "4.4"], role: "the regulator's outcomes and standards the statement summarises" }
```

## Part B Terminology
<!-- The statement has no glossary of its own unless Part E says so; these are terms it defines in its text. -->

### B1 Concepts
<!-- label: both; status: drafted; basis: primary -->
```yaml
- { slug: "registerable-integrated-masters", definition: "an integrated master's at FHEQ Level 7 (FQHEIS Level 11) that brings patient-facing learning into the degree so its graduates can join the regulator's register as fully qualified optometrists (D1, front matter)", beneficiaryDefinition: "the master's course that lets you register as an optometrist when you graduate", scopeNote: "replaces the BSc route; the only award this statement covers", category: "unknown", practices: ["education"] }
- { slug: "millers-pyramid", definition: "a hierarchy of clinical competence used in health education with four layers, knows, knows how, shows how and does, used here for course design and for matching assessment (D1, 2.9; 3.16)", beneficiaryDefinition: "a way of describing how clinical skill grows, from knowing about something to doing it reliably in practice", scopeNote: "named for theory ingest (Part E)", category: "unknown", practices: ["education"] }
- { slug: "enterprise", definition: "a mix of creativity, originality, innovation, adaptability, reflection, problem-solving, expression, communication and practical action (D1, 1.20)", beneficiaryDefinition: "the creative, practical and problem-solving qualities that help you make things happen", scopeNote: "paired with entrepreneurship", category: "unknown", practices: ["education"] }
- { slug: "entrepreneurship", definition: "using enterprise behaviours to create social, cultural or economic value, in private, public and third sectors alike (D1, 1.21)", beneficiaryDefinition: "using enterprising qualities to create value of any kind, not only profit", scopeNote: "not restricted to commercial activity", category: "unknown", practices: ["education"] }
- { slug: "feedforward", definition: "guidance that looks ahead to future assignments on how to improve, as distinct from feedback on current performance (D1, 3.20; 3.21)", beneficiaryDefinition: "advice on how to do better in your next piece of work", scopeNote: "used with feedback", category: "unknown", practices: ["education"] }
- { slug: "threshold-standard", definition: "what a student will have shown on being awarded the master's, the abilities expected of a graduate entering a regulated healthcare profession (D1, 4.1; 4.3)", beneficiaryDefinition: "the level you need to reach to gain the award and enter the profession", scopeNote: "the only rung this statement sets", category: "unknown", practices: ["education"] }
```

### B2a Terms as the issuer defines them
<!-- label: source; status: drafted; basis: primary -->
```yaml
- { concept: "registerable-integrated-masters", form: "registerable integrated master's", lang: "en", partOfSpeech: "noun-phrase", termStatus: "preferred", register: "formal" }
- { concept: "millers-pyramid", form: "Miller's pyramid of clinical competence", lang: "en", partOfSpeech: "noun-phrase", termStatus: "preferred", register: "discipline-specific" }
- { concept: "enterprise", form: "enterprise", lang: "en", partOfSpeech: "noun", termStatus: "preferred", register: "formal" }
- { concept: "entrepreneurship", form: "entrepreneurship", lang: "en", partOfSpeech: "noun", termStatus: "preferred", register: "formal" }
- { concept: "feedforward", form: "feedforward", lang: "en", partOfSpeech: "noun", termStatus: "preferred", register: "formal" }
- { concept: "threshold-standard", form: "threshold standard", lang: "en", partOfSpeech: "noun-phrase", termStatus: "preferred", register: "formal" }
```

### B2b Associated vocabulary
`not-applicable-by-design`: the statement names no wider vocabulary.

### B3 Framework blocks
`not-applicable-by-design`: no term is defined its own way for one component.

### B4 Relations
<!-- label: both; status: drafted; basis: primary -->
```yaml
- { rel: "related", from: "enterprise", to: "entrepreneurship", note: "1.21: entrepreneurship applies enterprise behaviours" }
```

## Part C Process
<!-- label: both; status: drafted; basis: primary -->

### C0 Formality
`not-applicable`: the statement sets out what graduates achieve and what courses provide, not a procedure.

## Part D Sources
```yaml
- key: D1
  issuer: The Quality Assurance Agency for Higher Education
  title: "Subject Benchmark Statement Optometry"
  edition: "April 2024 (fifth edition)"
  year: 2024
  url: unknown (the QAA page; the text came by stan's extraction)
  retrieved: "held from stan: wkspc2615-QAAVector mapped/optometry-2024/optometry-2024.raw.txt, commit 366bcb99a01118f2c4c3ebfa2a8337596bddc455; received 2026-10-03"
  licence: QAA copyright
  tier: primary
  readVia: direct
  held: 5ea3d94e6e3a6d13a3a2cca225a389ee954654efe4d0a608326d3b1c43735911
  heldFiles: ["wkspc2601-library/txt/qaa-2024-optometry-subject-benchmark-statement-standard.txt", "wkspc2601-library/txt/qaa-2024-optometry-subject-benchmark-statement-standard.norm.txt", "wkspc2601-library/records/qaa-2024-optometry-subject-benchmark-statement-standard.chunks.json", "wkspc2601-library/records/qaa-2024-optometry-subject-benchmark-statement-standard.held.json"]
  citedIn: [S1, S2, S3, S4, S4a, S5, S6, S7, SB1, SB2, SB3, SB4, SB5, SB6]
```

### D2 Research log
```yaml
- { ref: D1, tier: primary, consulted: 2026-10-03, pass: P1, outcome: "read whole, direct, from the normalised text; skeleton by tools/std_prep.py, document by tools/bm_build.py" }
- { ref: "ADAPT subj HESA stores, cah.json and hecos.json (designs/ingest/standards/subj/vocab)", tier: primary, consulted: 2026-10-03, pass: P1, outcome: "codes for statedSubjects and subjects" }
```

### D3 Wanted sources
```yaml
- { w: "W-std-0086", title: "General Optical Council, Requirements for Approved Qualifications in Optometry or Dispensing Optics (2021; revised May 2023)", why: "the outcomes 3.4, 3.5 and 4.4 summarise; for SB5 requirements and a standards document of its own" }
- { w: "W-std-0087", title: "QAA, Subject Benchmark Statement: Optometry (2019)", why: "the superseded BSc statement, for S7 supersedes" }
```

## Part E Gaps and questions
- Rungs: threshold only. 4.3 (heading 'Threshold level') defines the rung; 4.4 and 4.5 sit under it. No typical or excellent rung; 4.2 points to Annex D, which describes FHEQ Level 6 and FQHEIS Level 10 classes, not Level 7 (pattern differs from Psychology).
- Award: only the registrable integrated master's (fheq:7, fqheis:11); the BSc (fheq:6, fqheis:10) is named as replaced. Award value written "integrated master's" (pattern differs from Psychology).
- 4.4 is one paragraph holding seven category summaries; cut by us into 4.4.b1 to 4.4.b7 by category heading (find=). The skeleton gave 4.4 as a single paragraph. Force recorded as threshold (forceFrom 4.3), since the text mixes should, must, need to, will, are expected to and plain present within each category; P3 to confirm.
- 4.5 lead-in ('should be able to demonstrate') does not name a rung; recorded as threshold because it sits under the 'Threshold level' heading and 2.7 calls the listed generic skills threshold-level. Force should, from the lead-in. P3 to confirm.
- gradeOf: none; only one rung is stated.
- 4.5.b5 closely echoes the FHEQ master's descriptor (qaa/fheq-2024/4.17.b3) word for word in part; an echo, not a cut.
- Outcome lists: 3.5 ('requires that graduates are able to', force must) and 3.1 (courses 'should equip graduates with key skills', force should). 3.5 repeats the regulator's outcomes that 4.4 summarises at threshold; the two are not linked by gradeOf.
- Obliging words outside the five: 'need to' (2.15; 4.4 Communication), 'are expected to' (2.7; 2.17; 4.4 Ethics and standards), 'responsibility' (1.9; front matter: course providers check GOC registration), 'it is essential' (3.21), 'is expected to' (front matter: courses continuing to 2030). Recorded under the paragraph's own five-word modal where one is present; 1.9 left as a component.
- Front matter obligations not cut as statements (excluded matter): every Optometry student must by law stay registered with the GOC (Opticians Act 1989, s8A; GOC Registration Rules 2005); course providers have a responsibility to check it; all courses must move to the GOC's 2021 requirements. Recorded in SB5; P3 to decide whether they become S4 records.
- Plain-present provider norms, not statements (template open point 5): 1.5, 1.6, 2.5, 2.12, 2.21, 2.22, 2.23 ('will use external reviewers'), 2.25 ('will be asked'), 3.4 ('ensures'), 3.6, 3.9 ('will take place'), 3.11 ('courses ensure'), 3.17.
- 1.4 (aims of the degree, 12 items in three groups) recorded as a component, not statements: aims, not standards; 1.4.b10 contains 'will foster'.
- 3.2, 3.3 ('generally includes'), 3.10 ('may include') and 3.17 ('includes') are content and practice lists, recorded in SB3, not statements. 3.13's six items and 3.14's three are cut one record per item, as the brief's stem rule asks.
- 3.16: only its first sentence (should) is a statement; the four pyramid layers it lists are definitions (B1 millers-pyramid).
- Spans trimmed by find= where the skeleton span ran on into the next sub-heading: 1.13, 1.16, 1.17, 2.11, 2.16, 3.5.b7, 3.18, 4.2.
- Artificial intelligence is named in 1.4, 2.16, 3.2 and 4.5 (via technology) but there is no generative AI section; theme:generative-ai not used.
- Subjects: HECoS 100036 optometry and its CAH line (CAH02-06-03, CAH02-06, CAH02) marked stated, as the statement names the subject; the codes themselves are not printed. Related codes not taken: 101511 ophthalmic dispensing, 100037 orthoptics; the statement excludes non-registrable vision science awards.
- S5: spine:7 and the crosswalk fheq:7 to cqfw:7 are inferred from std:doc:qaa-fheq-2024-framework 2.24 and std:ref:uk-framework R2; the statement names no CQFW level although it applies in Wales.
- Pedagogy named for theory ingest: Miller's pyramid (2.9; 3.16; Miller 1990; Witheridge and others 2019), the spiral curriculum (1.7; 2.5; Harden 1999), constructive alignment (3.12; 3.14), feedforward (3.20; 3.21).
- Bodies named only in the references or advisory group, not in the body text: the College of Optometrists, the Association for Independent Optometrists and Dispensing Opticians; Higher Education Academy (employability framework, references). Not in SB6.
- Universities UK (2.22) is listed under SB6 bodies as a named sector body, not a PSRB; not in SB5.
- The statement names the National Student Survey (2.20) as a source of student voice; not a shared document.
- S9 commentary not researched in P1.
- ST-12: versions here run to the lengths the content needs; no length range is yet set.

---

## Change notes
- 0.1.2, 3 October 2026, 21:02: moved with its held text from UNI to the source library repo (`wkspc2601-library/ingested/standards/`, texts in `txt/`, records in `records/`); paths only (Abbott, 20:56; std N-0119).
- 0.1.1, 3 October 2026, 20:20: obliging words outside the five read as must, "ought to" as should, on statements outside the rungs, each marked on its force line (Abbott, 20:17; D-std-0016).
- 0.1.0, 2026-10-03 18:02: researched by run frame 0.1.1-draft and standards run layer 0.7.0-draft, std, run 0122 (P1); built by tools/bm_build.py.
