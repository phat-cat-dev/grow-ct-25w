---
id: std:doc:qaa-linguistics-2023-benchmarks
title: "Subject Benchmark Statement Linguistics"
profile: standards/subject-benchmark
profileVersion: 0.2.0-draft
issuer: QAA
kind: subject-benchmark
jurisdiction: [UK]
subjectScope: subjects
subjects:
  - { scheme: "hecos", code: "100328", label: "linguistics", basis: "stated" }
  - { scheme: "cah", code: "CAH19-01-07", label: "linguistics", basis: "stated" }
  - { scheme: "hecos", code: "100970", label: "applied linguistics", basis: "stated" }
  - { scheme: "hecos", code: "100972", label: "phonetics", basis: "stated" }
  - { scheme: "hecos", code: "101016", label: "sociolinguistics", basis: "stated" }
  - { scheme: "hecos", code: "101035", label: "psycholinguistics", basis: "stated" }
  - { scheme: "hecos", code: "101410", label: "historical linguistics", basis: "stated" }
  - { scheme: "hecos", code: "100971", label: "phonetics and phonology", basis: "inferred" }
edition: "September 2023"
published: 2023-09
status: current
supersedes: "std:doc:qaa-linguistics-2019-benchmarks (the fourth edition, 2019, named in the back matter; not ingested)"
heldText: { method: sha256-bytes, raw: b82ce2a87934ac152025726dded4e685281df4a1d9a9a3c0009e4b463f542828, normalised: 8bcb923eee79e89790538ca0a130f175b71311279d393149f9d924a4e7dfc696 }
heldTextStan: { method: sha256-stan, raw: b82ce2a87934ac152025726dded4e685281df4a1d9a9a3c0009e4b463f542828, normalised: 22ad473730cff6f8a8ac36ee0aff28caf5de33941d55b9bb8ef129ee4e587df4 }
licence: "QAA copyright; held for study, private to the project, never published"
series: "QAA Subject Benchmark Statements, 2023 revision with the cross-cutting themes (the back matter names a 2019 fourth edition; this one as the fifth is inferred)"
awardsCovered: ["bachelor's with honours"]
levelsCovered: ["fheq:6", "fqheis:10"]
nations: ["England", "Wales", "Scotland", "Northern Ireland"]
parts:
  S: full
  B: "partial: no glossary in the document (it points to QAA's Glossary); terms it defines in passing"
  C: "not-applicable: the document sets expectations, not a procedure"
pins: { structure: 0.13.0-draft, template: 0.8.0-draft, benchmarkTemplate: 0.6.0-draft, runFrame: 0.1.1-draft, runLayer: 0.7.0-draft, standards: none yet, terminology: none yet }
lifecycle: drafted
researchedBy: run frame 0.1.1-draft; standards run layer 0.7.0-draft; std, run 0118 (tools/bm_build.py)
passes:
  P1: "2026-10-03 17:59"
  P2: "skipped: read direct from the held text; inferred codes and rung links are for P3"
  P3: open
version: 0.1.2
---

<!-- from INGEST wpk-0016-ingest-pd-template-standards.md 0.8.0-draft and wpk-0016-ingest-pd-template-standards-benchmark.md 0.6.0-draft; built by tools/bm_build.py from run-src/ -->
# Subject Benchmark Statement: Linguistics (QAA, September 2023)

> Run 0118, P1 by std. The issuer's words are held in the source library, `wkspc2601-library/txt/qaa-2023-linguistics-subject-benchmark-statement-standard.norm.txt`; each S4 record carries its statement in full (`source`) for language analysis, with its span. Paraphrases and versions are ours. Private to the project, never published. In front matter `status` is the issuer's; ours is `lifecycle`. Doubts are in Part E.

## Part 0 Summary

### 0.1 Agent definition
<!-- label: editorial; status: drafted; basis: primary -->
QAA's UK reference point for what a Linguistics graduate should know and be able to do at the end of an honours degree (FHEQ Level 6, FQHEIS Level 10). It gives one rung only, a list of fifteen minimum threshold items, beside a separate list of fifteen generic skills and a few expected outcomes in its narrative sections; anything above the threshold is left to the degree classification descriptions in Annex D of the FHEQ. Reach for it when designing, approving, reviewing or describing a Linguistics course or its outcomes, single or combined honours. It is not a curriculum and not a regulatory requirement, and it names no professional body of its own.

### 0.2 Summary
<!-- label: both; status: drafted; basis: primary -->
Published by QAA in September 2023 for UK higher education, the statement covers General and Applied Linguistics at undergraduate honours level. It sets out the subject's context and purposes with four cross-cutting themes (equality, diversity and inclusion; accessibility; sustainability, tied to the UN Sustainable Development Goals; enterprise and entrepreneurship education), the distinctive features of courses (design, progression, flexibility, partnership, monitoring and review), content by levels of linguistic analysis, domains of language use and applied fields, teaching and assessment, and its benchmark standards. The standards are a threshold rung only (para 4.5, fifteen items) and a list of fifteen generic skills (para 4.6); typical and excellent performance are referred to Annex D. It names no professional, statutory or regulatory body beyond PSRBs in general and the Office for Students.

## Part S Standard

### S1 Identity
<!-- label: source; status: drafted; basis: primary -->
```yaml
issuer: The Quality Assurance Agency for Higher Education
title: "Subject Benchmark Statement Linguistics"
edition: "September 2023"
dates:
  published: 2023-09
  other: []
kind: subject-benchmark
jurisdiction: [UK]
authority: "reference: a sector reference point, not a regulatory requirement (D1, front matter); in England not a sector-recognised standard under the Office for Students' regulatory framework; a key reference point in Wales and Scotland; part of quality requirements in Northern Ireland (D1, front matter: Relationship to legislation)"
licence: "QAA copyright; the document gives no re-use terms in its text (D1, front matter)"
copyrightNotice: { text: "© The Quality Assurance Agency for Higher Education 2023", locator: "D1, index" }
```

### S2 Purpose and scope
<!-- label: source; status: drafted; basis: primary -->
```yaml
governs: "what a graduate in Linguistics (General and Applied) is expected to know, do and understand at the end of an honours degree, and the nature of courses in the subject"
appliesTo:
  awards: ["bachelor's with honours"]
  levels: ["fheq:6", "fqheis:10"]
  providers: ["UK higher education providers"]
whoMustUse: "none-stated; it is a reference point, not a requirement (D1, front matter)"
howUsed: ["design", "approval", "review", "other: external examining; PSRBs; information for prospective students and employers"]
doesNot: "it is not a national curriculum and does not prescribe teaching, learning or assessment; it carries no statutory or regulatory requirement (D1, front matter)"
beneficiary: the student
statedScope: "\"The purpose of this Statement is to make explicit the context, content, scope and benchmark standards of undergraduate degrees in the subject area of Linguistics, which encompasses the interrelated areas of General and Applied Linguistics.\" (D1, 1.1)"
statedSubjects:
  - { name: "Linguistics", locator: "(D1, 1.1)", kind: "subject", codes: [{ scheme: "hecos", code: "100328", label: "linguistics" }, { scheme: "cah", code: "CAH19-01-07", label: "linguistics" }] }
  - { name: "General Linguistics", locator: "(D1, 1.1)", kind: "specialism", codes: [{ scheme: "hecos", code: "100328", label: "linguistics" }] }
  - { name: "Applied Linguistics", locator: "(D1, 1.1; 3.4)", kind: "specialism", codes: [{ scheme: "hecos", code: "100970", label: "applied linguistics" }] }
  - { name: "phonetics; phonology", locator: "(D1, 3.1; 3.2)", kind: "specialism", codes: [{ scheme: "hecos", code: "100972", label: "phonetics" }, { scheme: "hecos", code: "100971", label: "phonetics and phonology" }] }
  - { name: "sociolinguistics", locator: "(D1, 3.3)", kind: "specialism", codes: [{ scheme: "hecos", code: "101016", label: "sociolinguistics" }] }
  - { name: "psycholinguistics", locator: "(D1, 3.3)", kind: "specialism", codes: [{ scheme: "hecos", code: "101035", label: "psycholinguistics" }] }
  - { name: "historical linguistics", locator: "(D1, 3.3)", kind: "specialism", codes: [{ scheme: "hecos", code: "101410", label: "historical linguistics" }] }
  - { name: "single, joint, combined and major-minor honours", locator: "(D1, 2.3; 2.7)", kind: "programme title", codes: [] }
subjects: see front matter (subjectScope subjects)
```

### S3 Structure
<!-- label: both; status: drafted; basis: primary -->
```yaml
components:
  - { number: "1.1", order: 3, componentType: paragraph, parent: "section 1", heading: "Context", gloss: "purpose and coverage: General and Applied Linguistics at undergraduate level" }
  - { number: "1.2", order: 4, componentType: paragraph, parent: "section 1", heading: "Purposes and characteristics of a Linguistics degree", gloss: "what linguistics studies: structural, cognitive, social, cultural and historical sides of language" }
  - { number: "1.3", order: 5, componentType: paragraph, parent: "section 1", heading: "Purposes and characteristics of a Linguistics degree", gloss: "systematic, theory-and-data inquiry across sciences, social sciences and humanities" }
  - { number: "1.4", order: 6, componentType: paragraph, parent: "section 1", heading: "Purposes and characteristics of a Linguistics degree", gloss: "an open, evolving view of the subject rather than fixed boundaries" }
  - { number: "1.5", order: 7, componentType: paragraph, parent: "section 1", heading: "Purposes and characteristics of a Linguistics degree", gloss: "course diversity and common subject combinations" }
  - { number: "1.6", order: 8, componentType: paragraph, parent: "section 1", heading: "Purposes and characteristics of a Linguistics degree", gloss: "breadth of current linguistic research and the varied settings of courses" }
  - { number: "1.7", order: 9, componentType: paragraph, parent: "section 1", heading: "Equality, diversity and inclusion", gloss: "EDI built into curriculum, research, values and assessment" }
  - { number: "1.8", order: 10, componentType: paragraph, parent: "section 1", heading: "Equality, diversity and inclusion", gloss: "reflexivity and EDI within subject knowledge itself" }
  - { number: "1.9", order: 11, componentType: paragraph, parent: "section 1", heading: "Equality, diversity and inclusion", gloss: "language, social hierarchy and symbolic power" }
  - { number: "1.10", order: 12, componentType: paragraph, parent: "section 1", heading: "Equality, diversity and inclusion", gloss: "collaborative learning and diverse students enrich EDI learning" }
  - { number: "1.11", order: 13, componentType: paragraph, parent: "section 1", heading: "Equality, diversity and inclusion", gloss: "real-life assessment linked to EDI issues" }
  - { number: "1.12", order: 14, componentType: paragraph, parent: "section 1", heading: "Accessibility", gloss: "all modes of language; accessible formats and adjustments" }
  - { number: "1.13", order: 15, componentType: paragraph, parent: "section 1", heading: "Accessibility", gloss: "professional communication with respect for diversity; active, independent learners" }
  - { number: "1.14", order: 16, componentType: paragraph, parent: "section 1", heading: "Accessibility", gloss: "multilingual home backgrounds enrich the classroom" }
  - { number: "1.15", order: 17, componentType: paragraph, parent: "section 1", heading: "Accessibility", gloss: "students bring their own linguistic experience to theory" }
  - { number: "1.16", order: 18, componentType: paragraph, parent: "section 1", heading: "Accessibility", gloss: "provider awareness of accessibility needs; accessible digital content" }
  - { number: "1.17", order: 19, componentType: paragraph, parent: "section 1", heading: "Sustainability", gloss: "linguistics and sustainability: analysing factors behind environmental harm" }
  - { number: "1.18", order: 20, componentType: stem, parent: "section 1", heading: "Sustainability", gloss: "two principles for engaging with sustainability" }
  - { number: "1.19", order: 21, componentType: stem, parent: "section 1", heading: "Sustainability", gloss: "links to UNESCO goals SDG4, SDG5, SDG8 and SDG16" }
  - { number: "1.20", order: 22, componentType: paragraph, parent: "section 1", heading: "Sustainability", gloss: "discourse analysis applied to climate and environmental questions" }
  - { number: "1.21", order: 23, componentType: paragraph, parent: "section 1", heading: "Sustainability", gloss: "documentation and endangered-language work in sustainability dialogue" }
  - { number: "1.22", order: 24, componentType: paragraph, parent: "section 1", heading: "Enterprise and entrepreneurship education", gloss: "enterprise education for careers and links with external organisations" }
  - { number: "1.23", order: 25, componentType: paragraph, parent: "section 1", heading: "Enterprise and entrepreneurship education", gloss: "entrepreneurship competencies beyond employment" }
  - { number: "1.24", order: 26, componentType: paragraph, parent: "section 1", heading: "Enterprise and entrepreneurship education", gloss: "critical, creative and analytical skills that create value" }
  - { number: "1.25", order: 27, componentType: paragraph, parent: "section 1", heading: "Enterprise and entrepreneurship education", gloss: "enterprise capabilities, citing the 2018 enterprise guidance" }
  - { number: "1.26", order: 28, componentType: paragraph, parent: "section 1", heading: "Enterprise and entrepreneurship education", gloss: "societal impact of linguistic skills; telling employers about them" }
  - { number: "1.27", order: 29, componentType: paragraph, parent: "section 1", heading: "Enterprise and entrepreneurship education", gloss: "modules and placements build professional attributes" }
  - { number: "1.28", order: 30, componentType: paragraph, parent: "section 1", heading: "Enterprise and entrepreneurship education", gloss: "information technology and data skills" }
  - { number: "1.29", order: 31, componentType: paragraph, parent: "section 1", heading: "Enterprise and entrepreneurship education", gloss: "sectors that employ graduates" }
  - { number: "1.30", order: 32, componentType: paragraph, parent: "section 1", heading: "Enterprise and entrepreneurship education", gloss: "graduates in data-led and AI-related industries" }
  - { number: "1.31", order: 33, componentType: paragraph, parent: "section 1", heading: "Enterprise and entrepreneurship education", gloss: "employability from data analysis and pattern finding" }
  - { number: "2.1", order: 35, componentType: paragraph, parent: "section 2", heading: "Design", gloss: "core and optional modules, research training and critical reflection" }
  - { number: "2.2", order: 36, componentType: paragraph, parent: "section 2", heading: "Design", gloss: "growing independence; a final independent research project" }
  - { number: "2.3", order: 37, componentType: paragraph, parent: "section 2", heading: "Design", gloss: "single honours covers most of section 3; joint routes select from it" }
  - { number: "2.4", order: 38, componentType: paragraph, parent: "section 2", heading: "Progression", gloss: "no single model of sequential study" }
  - { number: "2.5", order: 39, componentType: paragraph, parent: "section 2", heading: "Progression", gloss: "progression across levels towards the threshold at FHEQ 6 and FQHEIS 10" }
  - { number: "2.6", order: 40, componentType: paragraph, parent: "section 2", heading: "Progression", gloss: "signs of progression; readiness for postgraduate study" }
  - { number: "2.7", order: 41, componentType: paragraph, parent: "section 2", heading: "Progression", gloss: "joint and combined routes reach the core skills and add others" }
  - { number: "2.8", order: 42, componentType: paragraph, parent: "section 2", heading: "Progression", gloss: "typical duration, exit awards and Scottish four-year honours" }
  - { number: "2.9", order: 43, componentType: paragraph, parent: "section 2", heading: "Progression", gloss: "micro-credentials as funding changes" }
  - { number: "2.10", order: 44, componentType: paragraph, parent: "section 2", heading: "Flexibility", gloss: "flexible entry and clear entry information" }
  - { number: "2.11", order: 45, componentType: paragraph, parent: "section 2", heading: "Flexibility", gloss: "flexible content, modes and timing; online provision" }
  - { number: "2.12", order: 46, componentType: paragraph, parent: "section 2", heading: "Flexibility", gloss: "resources and training for accessible delivery; uneven access to technology" }
  - { number: "2.13", order: 47, componentType: paragraph, parent: "section 2", heading: "Partnership", gloss: "transferable skills and equal access to partnerships" }
  - { number: "2.14", order: 48, componentType: paragraph, parent: "section 2", heading: "Partnership", gloss: "partnership activities tied to learning outcomes" }
  - { number: "2.15", order: 49, componentType: paragraph, parent: "section 2", heading: "Partnership", gloss: "mobility and exchange across cultures" }
  - { number: "2.16", order: 50, componentType: paragraph, parent: "section 2", heading: "Partnership", gloss: "global outlook even without mobility" }
  - { number: "2.17", order: 51, componentType: paragraph, parent: "section 2", heading: "Partnership", gloss: "partners offering teaching qualifications, as in TESOL" }
  - { number: "2.18", order: 52, componentType: paragraph, parent: "section 2", heading: "Partnership", gloss: "skills employers value; experiential learning" }
  - { number: "2.19", order: 53, componentType: paragraph, parent: "section 2", heading: "Monitoring and review", gloss: "periodic course review against external reference points" }
  - { number: "2.20", order: 54, componentType: paragraph, parent: "section 2", heading: "Monitoring and review", gloss: "external reviewers in periodic review" }
  - { number: "2.21", order: 55, componentType: paragraph, parent: "section 2", heading: "Monitoring and review", gloss: "external examiners and consistency of standards" }
  - { number: "2.22", order: 56, componentType: paragraph, parent: "section 2", heading: "Monitoring and review", gloss: "accreditation of professionally oriented courses" }
  - { number: "3.1", order: 58, componentType: area, parent: "section 3", heading: "Content", gloss: "introductory modules across the levels of analysis" }
  - { number: "3.2", order: 59, componentType: area, parent: "section 3", heading: "Content", gloss: "six levels of analysis described, phonetics to pragmatics" }
  - { number: "3.3", order: 60, componentType: area, parent: "section 3", heading: "Content", gloss: "thirteen domains of language use and development" }
  - { number: "3.4", order: 61, componentType: area, parent: "section 3", heading: "Content", gloss: "applied fields from applied to clinical, computational and forensic linguistics" }
  - { number: "3.5", order: 62, componentType: practice, parent: "section 3", heading: "Teaching and learning", gloss: "teaching, learning and assessment aligned to aims and stage" }
  - { number: "3.6", order: 63, componentType: practice, parent: "section 3", heading: "Teaching and learning", gloss: "course documentation at the outset; varied teaching methods listed" }
  - { number: "3.7", order: 64, componentType: practice, parent: "section 3", heading: "Teaching and learning", gloss: "inclusive teaching and a sense of belonging" }
  - { number: "3.8", order: 65, componentType: practice, parent: "section 3", heading: "Assessment", gloss: "assessment aligned to aims and stage" }
  - { number: "3.9", order: 66, componentType: practice, parent: "section 3", heading: "Assessment", gloss: "what varied assessment methods evaluate" }
  - { number: "3.10", order: 67, componentType: practice, parent: "section 3", heading: "Assessment", gloss: "assessment methods listed" }
  - { number: "3.11", order: 68, componentType: practice, parent: "section 3", heading: "Assessment", gloss: "balance of knowledge and skills in assessment; SDG themes" }
  - { number: "3.12", order: 69, componentType: practice, parent: "section 3", heading: "Assessment", gloss: "clear rationale and criteria for assessment" }
  - { number: "3.13", order: 70, componentType: practice, parent: "section 3", heading: "Assessment", gloss: "formative, diagnostic feedback throughout" }
  - { number: "4.1", order: 72, componentType: paragraph, parent: "section 4", heading: "Benchmark standards", gloss: "the standards are the minimum for honours; joint routes use a subset" }
  - { number: "4.2", order: 73, componentType: paragraph, parent: "section 4", heading: "Benchmark standards", gloss: "most students exceed the threshold; Annex D for classification" }
  - { number: "4.3", order: 74, componentType: paragraph, parent: "section 4", heading: "Benchmark standards", gloss: "expected grasp of core areas and the domains of language use" }
  - { number: "4.4", order: 75, componentType: paragraph, parent: "section 4", heading: "Benchmark standards", gloss: "expected knowledge of empirical phenomena and their terminology" }
  - { number: "4.5", order: 76, componentType: stem, parent: "section 4", heading: "Minimum threshold standards", gloss: "threshold rung: fifteen items" }
  - { number: "4.6", order: 77, componentType: stem, parent: "section 4", heading: "Generic skills", gloss: "fifteen generic skills valued by employers" }
  - { number: "1", componentType: section, parent: none, heading: "Context and purposes of a Linguistics Degree", gloss: "section 1" }
  - { number: "2", componentType: section, parent: none, heading: "Distinctive features of Linguistics degrees", gloss: "section 2" }
  - { number: "3", componentType: section, parent: none, heading: "Content, structure and delivery", gloss: "section 3" }
  - { number: "4", componentType: section, parent: none, heading: "Benchmark standards", gloss: "section 4" }
excluded:
  - { number: "none", heading: "Contents; About this Statement; How can I use this document?; Relationship to legislation; Additional sector reference points", kind: "other: front matter, read for S1, S2, S7, SB5 and SB6" }
  - { number: "none", heading: "section heading lines 1 to 4", kind: "other: headings, recorded in SECTIONS" }
  - { number: "5", heading: "List of references and further resources", kind: "other: back matter, read for S7 and SB6" }
  - { number: "6", heading: "Membership of the Advisory Group (and the 2019, 2015, 2007 and 2002 review groups)", kind: "other: back matter, read for S7 (edition history)" }
  - { number: "none", heading: "Appendix 1: Indicative course titles", kind: "other: back matter, read for S2 (course titles)" }
  - { number: "none", heading: "Appendix 2: Signposting to other Subject Benchmark Statements", kind: "other: back matter, read for S7" }
  - { number: "none", heading: "copyright and address line", kind: "other: read for S1" }
```

### S4 Statements
<!-- label: both; status: drafted; basis: primary. Only standards (D-std-0002 (a)): 41 records. `source` is the issuer's statement exactly as its span holds it (D-std-0014). -->
```yaml
- id: qaa/linguistics-2023/1.13
  locator: { number: "1.13", headingPath: ["Context and purposes of a Linguistics Degree", "Accessibility"] }
  span: { start: 15503, end: 15954 }
  source: "1.13 Linguistics students work across a wide range of environments and circumstances and are normally expected to become increasingly able to communicate professionally, with an appreciation of and respect for linguistic, social and cultural diversity. They are also encouraged and supported to be active learners and to develop self-confidence, critical\n\n5\nunderstanding of their academic environment, and independence in their approach to learning.\n"
  stem: none
  statementType: expectation
  rung: none
  force: must   # D-std-0016: "expected to" read as must
  level: fheq:6
  appliesTo: "students of the subject"
  addressee: learner
  verbs: ["communicate"]
  about: "professional communication across settings, respecting diversity"
  themes: [theme:accessibility]
  domain: generic-skill
  award: ["bachelor's with honours"]
  gradeOf: none
  paraphrase: "Linguistics students work in many settings and are normally expected to grow in their ability to communicate professionally while respecting linguistic, social and cultural diversity; they are also helped to become active, confident and independent learners."
  quote: full   # the issuer's statement is in `source` (D-std-0014)
  audience: both
  subjects: inherited
- id: qaa/linguistics-2023/1.19.b4
  locator: { number: "1.19.b4", headingPath: ["Context and purposes of a Linguistics Degree", "Sustainability"] }
  span: { start: 19399, end: 19660 }
  source: "Language use, analysis and understanding are key to empowerment, opportunities, inclusion and equitable access. Particular attention to language and linguistic diversity should be given if we are to develop inclusive education for all (SDG4: Quality Education)."
  stem: "1.19"
  statementType: expectation
  rung: none
  force: should
  level: none
  appliesTo: "those who design and deliver education"
  addressee: provider
  verbs: ["develop"]
  about: "attention to linguistic diversity for inclusive education (SDG4)"
  themes: [theme:esd]
  domain: none
  award: ["none"]
  gradeOf: none
  paraphrase: "Using, analysing and understanding language underpins empowerment, inclusion and fair access, so language and linguistic diversity should receive particular attention in any effort to make education inclusive for everyone (SDG4, Quality Education)."
  quote: full   # the issuer's statement is in `source` (D-std-0014)
  audience: practitioner
  subjects: inherited
- id: qaa/linguistics-2023/1.26
  locator: { number: "1.26", headingPath: ["Context and purposes of a Linguistics Degree", "Enterprise and entrepreneurship education"] }
  span: { start: 22069, end: 22666 }
  source: "1.26 The Linguistics curriculum develops students' skills in a way that can have a significant impact on society - for example, by challenging established language ideologies and attitudes, scrutinising and rationalising institutional policies and practices, identifying assumptions, premises or prejudices underlying discourses, and critically evaluating theoretical positions and the data that drives them. Graduates are able to articulate and demonstrate these skills to potential employers, as well as other skills and personal attributes that are likely to be useful within the workplace.\n\n7\n"
  stem: none
  statementType: outcome
  rung: none
  force: will
  level: fheq:6
  appliesTo: "graduates of the subject"
  addressee: learner
  verbs: ["articulate", "demonstrate"]
  about: "explaining and showing skills to employers"
  themes: [theme:enterprise]
  domain: generic-skill
  award: ["bachelor's with honours"]
  gradeOf: none
  paraphrase: "The curriculum builds skills with real social reach, such as questioning language ideologies, scrutinising institutional policy, exposing hidden assumptions in discourse and weighing theories against data; graduates are able to explain and show these skills, and other useful personal attributes, to employers."
  quote: full   # the issuer's statement is in `source` (D-std-0014)
  audience: both
  subjects: inherited
- id: qaa/linguistics-2023/2.5
  locator: { number: "2.5", headingPath: ["Distinctive features of Linguistics degrees", "Progression"] }
  span: { start: 26728, end: 27181 }
  source: "2.5 Over the course of a degree with honours (FHEQ Level 6; FQHEIS Level 10), Linguistics students will progress from one level of study to the next, in line with the regulations and processes for each institution. However, it is expected that each level would see the progressive attainment of knowledge, skills, expertise and experience that build towards the final achievement of meeting the threshold-level subject skills listed in this Statement.\n\n"
  stem: none
  statementType: expectation
  rung: none
  force: will
  level: fheq:6
  appliesTo: "students on an honours course"
  addressee: learner
  verbs: ["progress"]
  about: "progression through levels to the honours threshold"
  themes: [none]
  domain: none
  award: ["bachelor's with honours"]
  gradeOf: none
  paraphrase: "On an honours degree (FHEQ Level 6; FQHEIS Level 10) students will move from one level of study to the next under each institution's rules, and each level is expected to add knowledge, skills, expertise and experience that lead to meeting the threshold subject skills."
  quote: full   # the issuer's statement is in `source` (D-std-0014)
  audience: both
  subjects: inherited
- id: qaa/linguistics-2023/2.7
  locator: { number: "2.7", headingPath: ["Distinctive features of Linguistics degrees", "Progression"] }
  span: { start: 28313, end: 28645 }
  source: "2.7 Undergraduates studying a combined, joint or major-minor route will achieve core elements of the specific and generic skills for the subject, and will add others according to the requirements of the relevant joint courses. Additionally, they may explore the overlap between their two subject areas via interdisciplinary study.\n\n"
  stem: none
  statementType: outcome
  rung: none
  force: will
  level: fheq:6
  appliesTo: "students on combined, joint or major-minor routes"
  addressee: learner
  verbs: ["achieve", "add"]
  about: "core subject skills on joint and combined routes"
  themes: [none]
  domain: subject-skill
  award: ["bachelor's with honours"]
  gradeOf: none
  paraphrase: "Students on combined, joint or major-minor routes will reach the core parts of the subject's specific and generic skills and will add others that their joint course requires; they may also study where the two subjects overlap."
  quote: full   # the issuer's statement is in `source` (D-std-0014)
  audience: both
  subjects: inherited
- id: qaa/linguistics-2023/2.9
  locator: { number: "2.9", headingPath: ["Distinctive features of Linguistics degrees", "Progression"] }
  span: { start: 29333, end: 29726 }
  source: "2.9 As funding models change and develop, it will increasingly be necessary for providers to consider the development of standalone 'micro-credentials' which may also contribute to more traditionally focused awards. These will need to be appealing to students in terms of professional and personal development, as well as contributing to the study of the subject, more generally.\n\nFlexibility\n"
  stem: none
  statementType: expectation
  rung: none
  force: must   # D-std-0016: "necessary" read as must
  level: none
  appliesTo: "higher education providers"
  addressee: provider
  verbs: ["consider"]
  about: "considering standalone micro-credentials"
  themes: [none]
  domain: none
  award: ["none"]
  gradeOf: none
  paraphrase: "As funding models change, providers will more and more need to consider standalone micro-credentials that can count towards larger awards; these need to attract students for professional and personal growth and to add to the study of the subject."
  quote: full   # the issuer's statement is in `source` (D-std-0014)
  audience: practitioner
  subjects: inherited
- id: qaa/linguistics-2023/2.12
  locator: { number: "2.12", headingPath: ["Distinctive features of Linguistics degrees", "Flexibility"] }
  span: { start: 30367, end: 30712 }
  source: "2.12 The provision of accessible, inclusive and flexible content requires appropriate resources and training to ensure consistent high-quality content and delivery. Where the design includes digital technology, the diversity in students' access to technology needs to be recognised in ways that do not disadvantage them in any way.\n\nPartnership\n"
  stem: none
  statementType: expectation
  rung: none
  force: must
  level: none
  appliesTo: "providers delivering accessible, inclusive and flexible content"
  addressee: provider
  verbs: ["recognised"]
  about: "resourcing accessible delivery and uneven access to technology"
  themes: [none]
  domain: none
  award: ["none"]
  gradeOf: none
  paraphrase: "Accessible, inclusive and flexible content requires suitable resources and staff training to keep quality consistent, and where courses use digital technology, students' unequal access to it needs to be recognised so that no one is disadvantaged."
  quote: full   # the issuer's statement is in `source` (D-std-0014)
  audience: practitioner
  subjects: inherited
- id: qaa/linguistics-2023/2.20
  locator: { number: "2.20", headingPath: ["Distinctive features of Linguistics degrees", "Monitoring and review"] }
  span: { start: 33114, end: 33410 }
  source: "2.20 Externality is an essential component of the quality assurance system in the UK. Providers will use external reviewers as part of periodic review to gain an external perspective on any proposed changes and ensure threshold standards are achieved and content is appropriate for the subject.\n\n"
  stem: none
  statementType: expectation
  rung: none
  force: will
  level: none
  appliesTo: "higher education providers"
  addressee: provider
  verbs: ["use", "ensure"]
  about: "external reviewers in periodic review"
  themes: [none]
  domain: none
  award: ["none"]
  gradeOf: none
  paraphrase: "Externality is essential to UK quality assurance: providers will bring external reviewers into periodic review for an outside view of proposed changes and to make sure threshold standards are met and content suits the subject."
  quote: full   # the issuer's statement is in `source` (D-std-0014)
  audience: practitioner
  subjects: inherited
- id: qaa/linguistics-2023/4.2
  locator: { number: "4.2", headingPath: ["Benchmark standards", "Benchmark standards"] }
  span: { start: 54492, end: 54976 }
  source: "4.2 The vast majority of students will perform significantly better than the minimum threshold standards. Each higher education provider has its own method of determining what appropriate evidence of this achievement will be and should refer to Annex D: Outcome classification descriptions for FHEQ Level 6 and FQHEIS Level 10 degrees. This Annex sets out common descriptions of the four main degree outcome classifications for bachelor's degrees with honours: 1st, 2.1, 2.2 and 3rd.\n"
  stem: none
  statementType: expectation
  rung: none
  force: should
  level: fheq:6
  appliesTo: "higher education providers"
  addressee: provider
  verbs: ["refer"]
  about: "using Annex D to judge achievement above threshold"
  themes: [none]
  domain: none
  award: ["bachelor's with honours"]
  gradeOf: none
  paraphrase: "Most students will do clearly better than the minimum threshold; each provider decides what counts as evidence of that and should refer to Annex D, which describes the four honours classifications (1st, 2.1, 2.2 and 3rd) for FHEQ Level 6 and FQHEIS Level 10."
  quote: full   # the issuer's statement is in `source` (D-std-0014)
  audience: practitioner
  subjects: inherited
- id: qaa/linguistics-2023/4.3
  locator: { number: "4.3", headingPath: ["Benchmark standards", "Benchmark standards"] }
  span: { start: 54976, end: 55537 }
  source: "4.3 Graduates with a bachelor's degree in Linguistics will be expected to have an understanding of the basic concepts and modes of analysis in core areas such as phonetics, phonology, morphology, syntax, semantics, pragmatics, and discourse. These tools lay the foundation for Linguistics graduates to also gain significant knowledge and comprehension of the domains within which these systems arise and exist - for example, language acquisition; language variation and change; the role of language in society; and the nature of language as a cognitive object.\n"
  stem: none
  statementType: expectation
  rung: none
  force: will
  level: fheq:6
  appliesTo: "graduates with a bachelor's degree in the subject"
  addressee: learner
  verbs: ["have"]
  about: "core areas of analysis and the domains of language"
  themes: [none]
  domain: understanding
  award: ["bachelor's with honours"]
  gradeOf: none
  paraphrase: "Graduates will be expected to grasp the basic ideas and analytic methods of the core areas, from phonetics to discourse, a foundation for substantial knowledge of the domains where language systems arise, such as acquisition, variation and change, language in society and language as a cognitive object."
  quote: full   # the issuer's statement is in `source` (D-std-0014)
  audience: both
  subjects: inherited
- id: qaa/linguistics-2023/4.4
  locator: { number: "4.4", headingPath: ["Benchmark standards", "Benchmark standards"] }
  span: { start: 55537, end: 55890 }
  source: "4.4 A Linguistics graduate is expected to have knowledge of a range of empirical linguistic phenomena and of the relevant technical terminology and methodology used in the description and analysis of such phenomena. Knowledge gained may be largely descriptive but is usually informed by an appropriate theoretical framework. Minimum threshold standards\n"
  stem: none
  statementType: expectation
  rung: none
  force: must   # D-std-0016: "is expected to" read as must
  level: fheq:6
  appliesTo: "graduates of the subject"
  addressee: learner
  verbs: ["have"]
  about: "empirical phenomena, terminology and methods"
  themes: [none]
  domain: knowledge
  award: ["bachelor's with honours"]
  gradeOf: none
  paraphrase: "A graduate is expected to know a range of empirical language phenomena and the technical terms and methods used to describe and analyse them; this knowledge may be mainly descriptive but usually rests on a suitable theoretical framework."
  quote: full   # the issuer's statement is in `source` (D-std-0014)
  audience: both
  subjects: inherited
- id: qaa/linguistics-2023/4.5.b1
  locator: { number: "4.5.b1", headingPath: ["Benchmark standards", "Minimum threshold standards"] }
  span: { start: 56146, end: 56265 }
  source: "demonstrate knowledge of the fundamental analytical concepts and methods of inquiry appropriate to a Linguistics degree"
  stem: "4.5"
  statementType: threshold
  rung: threshold
  force: threshold
  level: fheq:6
  appliesTo: "honours graduates at the threshold"
  addressee: learner
  verbs: ["demonstrate"]
  about: "fundamental analytical concepts and methods of inquiry"
  themes: [none]
  domain: knowledge
  award: ["bachelor's with honours"]
  gradeOf: none
  paraphrase: "Show knowledge of the basic analytic concepts and methods of inquiry that a linguistics degree calls for."
  quote: full   # the issuer's statement is in `source` (D-std-0014)
  audience: both
  subjects: inherited
- id: qaa/linguistics-2023/4.5.b2
  locator: { number: "4.5.b2", headingPath: ["Benchmark standards", "Minimum threshold standards"] }
  span: { start: 56268, end: 56364 }
  source: "take a systematic approach to the identification, description and analysis of language phenomena"
  stem: "4.5"
  statementType: threshold
  rung: threshold
  force: threshold
  level: fheq:6
  appliesTo: "honours graduates at the threshold"
  addressee: learner
  verbs: ["take"]
  about: "systematic identification, description and analysis"
  themes: [none]
  domain: subject-skill
  award: ["bachelor's with honours"]
  gradeOf: none
  paraphrase: "Approach language phenomena systematically: identifying, describing and then analysing them."
  quote: full   # the issuer's statement is in `source` (D-std-0014)
  audience: both
  subjects: inherited
- id: qaa/linguistics-2023/4.5.b3
  locator: { number: "4.5.b3", headingPath: ["Benchmark standards", "Minimum threshold standards"] }
  span: { start: 56367, end: 56423 }
  source: "ask motivated questions about language structure and use"
  stem: "4.5"
  statementType: threshold
  rung: threshold
  force: threshold
  level: fheq:6
  appliesTo: "honours graduates at the threshold"
  addressee: learner
  verbs: ["ask"]
  about: "well-motivated questions about language"
  themes: [none]
  domain: subject-skill
  award: ["bachelor's with honours"]
  gradeOf: none
  paraphrase: "Pose well-grounded questions about how language is structured and used."
  quote: full   # the issuer's statement is in `source` (D-std-0014)
  audience: both
  subjects: inherited
- id: qaa/linguistics-2023/4.5.b4
  locator: { number: "4.5.b4", headingPath: ["Benchmark standards", "Minimum threshold standards"] }
  span: { start: 56426, end: 56754 }
  source: "apply the basic techniques for collecting/eliciting and transcribing data specific to the various sub-disciplines of Linguistics, including the use of language corpora, media, politics or advertising, elicitation tasks, introspection, laboratory experiments, questionnaires, interviews and/or other types of linguistic fieldwork"
  stem: "4.5"
  statementType: threshold
  rung: threshold
  force: threshold
  level: fheq:6
  appliesTo: "honours graduates at the threshold"
  addressee: learner
  verbs: ["apply"]
  about: "basic data collection, elicitation and transcription"
  themes: [none]
  domain: subject-skill
  award: ["bachelor's with honours"]
  gradeOf: none
  paraphrase: "Use the basic methods for gathering or eliciting and transcribing data that suit the different branches of linguistics, from corpora and media texts to elicitation, introspection, experiments, questionnaires, interviews and fieldwork."
  quote: full   # the issuer's statement is in `source` (D-std-0014)
  audience: both
  subjects: inherited
- id: qaa/linguistics-2023/4.5.b5
  locator: { number: "4.5.b5", headingPath: ["Benchmark standards", "Minimum threshold standards"] }
  span: { start: 56757, end: 56859 }
  source: "apply analytical concepts specific to different levels of linguistic analysis to appropriate data sets"
  stem: "4.5"
  statementType: threshold
  rung: threshold
  force: threshold
  level: fheq:6
  appliesTo: "honours graduates at the threshold"
  addressee: learner
  verbs: ["apply"]
  about: "level-specific analytical concepts applied to data"
  themes: [none]
  domain: subject-skill
  award: ["bachelor's with honours"]
  gradeOf: none
  paraphrase: "Use the analytic concepts belonging to each level of linguistic analysis on suitable sets of data."
  quote: full   # the issuer's statement is in `source` (D-std-0014)
  audience: both
  subjects: inherited
- id: qaa/linguistics-2023/4.5.b6
  locator: { number: "4.5.b6", headingPath: ["Benchmark standards", "Minimum threshold standards"] }
  span: { start: 56862, end: 56993 }
  source: "formulate linguistic generalisations, and construct and test hypotheses within the scope of linguistics, using appropriate evidence"
  stem: "4.5"
  statementType: threshold
  rung: threshold
  force: threshold
  level: fheq:6
  appliesTo: "honours graduates at the threshold"
  addressee: learner
  verbs: ["formulate", "construct", "test"]
  about: "generalisations and hypothesis testing"
  themes: [none]
  domain: subject-skill
  award: ["bachelor's with honours"]
  gradeOf: none
  paraphrase: "Draw linguistic generalisations and build and test hypotheses within linguistics, using fitting evidence."
  quote: full   # the issuer's statement is in `source` (D-std-0014)
  audience: both
  subjects: inherited
- id: qaa/linguistics-2023/4.5.b7
  locator: { number: "4.5.b7", headingPath: ["Benchmark standards", "Minimum threshold standards"] }
  span: { start: 56996, end: 57182 }
  source: "evaluate alternative analyses of a given set of data, based on an understanding of how linguistic theories help to organise linguistic analysis and to determine what constitutes evidence"
  stem: "4.5"
  statementType: threshold
  rung: threshold
  force: threshold
  level: fheq:6
  appliesTo: "honours graduates at the threshold"
  addressee: learner
  verbs: ["evaluate"]
  about: "weighing alternative analyses of data"
  themes: [none]
  domain: subject-skill
  award: ["bachelor's with honours"]
  gradeOf: none
  paraphrase: "Weigh competing analyses of a data set, understanding how theories shape analysis and decide what counts as evidence."
  quote: full   # the issuer's statement is in `source` (D-std-0014)
  audience: both
  subjects: inherited
- id: qaa/linguistics-2023/4.5.b8
  locator: { number: "4.5.b8", headingPath: ["Benchmark standards", "Minimum threshold standards"] }
  span: { start: 57185, end: 57349 }
  source: "evaluate alternative theories, drawing on an understanding of the nature of linguistic theory and of what constitutes an explanation within the scope of linguistics"
  stem: "4.5"
  statementType: threshold
  rung: threshold
  force: threshold
  level: fheq:6
  appliesTo: "honours graduates at the threshold"
  addressee: learner
  verbs: ["evaluate"]
  about: "weighing alternative theories"
  themes: [none]
  domain: understanding
  award: ["bachelor's with honours"]
  gradeOf: none
  paraphrase: "Weigh competing theories, drawing on what linguistic theory is and on what counts as an explanation in linguistics."
  quote: full   # the issuer's statement is in `source` (D-std-0014)
  audience: both
  subjects: inherited
- id: qaa/linguistics-2023/4.5.b9
  locator: { number: "4.5.b9", headingPath: ["Benchmark standards", "Minimum threshold standards"] }
  span: { start: 57352, end: 57597 }
  source: "present linguistic data and analysis using the appropriate methods and conventions specific to each sub-discipline of Linguistics, including bracketing, tree diagrams,\n\n18\nformal logic, graphs, tables, matrices and specific transcription systems"
  stem: "4.5"
  statementType: threshold
  rung: threshold
  force: threshold
  level: fheq:6
  appliesTo: "honours graduates at the threshold"
  addressee: learner
  verbs: ["present"]
  about: "presenting data with discipline conventions"
  themes: [none]
  domain: subject-skill
  award: ["bachelor's with honours"]
  gradeOf: none
  paraphrase: "Set out linguistic data and analysis with the methods and conventions of each sub-discipline, such as bracketing, tree diagrams, formal logic, graphs, tables, matrices and transcription systems."
  quote: full   # the issuer's statement is in `source` (D-std-0014)
  audience: both
  subjects: inherited
- id: qaa/linguistics-2023/4.5.b10
  locator: { number: "4.5.b10", headingPath: ["Benchmark standards", "Minimum threshold standards"] }
  span: { start: 57600, end: 57684 }
  source: "utilise linguistic terminology, theory and research to address real-world challenges"
  stem: "4.5"
  statementType: threshold
  rung: threshold
  force: threshold
  level: fheq:6
  appliesTo: "honours graduates at the threshold"
  addressee: learner
  verbs: ["utilise", "address"]
  about: "linguistics applied to real-world problems"
  themes: [none]
  domain: subject-skill
  award: ["bachelor's with honours"]
  gradeOf: none
  paraphrase: "Bring linguistic terms, theory and research to bear on problems in the world beyond the discipline."
  quote: full   # the issuer's statement is in `source` (D-std-0014)
  audience: both
  subjects: inherited
- id: qaa/linguistics-2023/4.5.b11
  locator: { number: "4.5.b11", headingPath: ["Benchmark standards", "Minimum threshold standards"] }
  span: { start: 57687, end: 57815 }
  source: "understand and communicate observations about the linguistic representations of ideology, power, social identities and realities"
  stem: "4.5"
  statementType: threshold
  rung: threshold
  force: threshold
  level: fheq:6
  appliesTo: "honours graduates at the threshold"
  addressee: learner
  verbs: ["understand", "communicate"]
  about: "language, ideology, power and identity"
  themes: [none]
  domain: understanding
  award: ["bachelor's with honours"]
  gradeOf: none
  paraphrase: "Grasp, and explain to others, what can be observed about how language represents ideology, power, social identities and realities."
  quote: full   # the issuer's statement is in `source` (D-std-0014)
  audience: both
  subjects: inherited
- id: qaa/linguistics-2023/4.5.b12
  locator: { number: "4.5.b12", headingPath: ["Benchmark standards", "Minimum threshold standards"] }
  span: { start: 57818, end: 57933 }
  source: "analyse linguistic representations of minority groups in different regional, sociocultural and situational settings"
  stem: "4.5"
  statementType: threshold
  rung: threshold
  force: threshold
  level: fheq:6
  appliesTo: "honours graduates at the threshold"
  addressee: learner
  verbs: ["analyse"]
  about: "representations of minority groups"
  themes: [none]
  domain: subject-skill
  award: ["bachelor's with honours"]
  gradeOf: none
  paraphrase: "Analyse how language represents minority groups across regional, sociocultural and situational settings."
  quote: full   # the issuer's statement is in `source` (D-std-0014)
  audience: both
  subjects: inherited
- id: qaa/linguistics-2023/4.5.b13
  locator: { number: "4.5.b13", headingPath: ["Benchmark standards", "Minimum threshold standards"] }
  span: { start: 57936, end: 58126 }
  source: "identify and examine examples of and reasons for language variation across situational, social, cultural, regional and historical contexts as well as multilingual and cross-cultural contexts"
  stem: "4.5"
  statementType: threshold
  rung: threshold
  force: threshold
  level: fheq:6
  appliesTo: "honours graduates at the threshold"
  addressee: learner
  verbs: ["identify", "examine"]
  about: "variation across contexts"
  themes: [none]
  domain: subject-skill
  award: ["bachelor's with honours"]
  gradeOf: none
  paraphrase: "Find and investigate cases of language variation, and their causes, across situational, social, cultural, regional and historical contexts, including multilingual and cross-cultural ones."
  quote: full   # the issuer's statement is in `source` (D-std-0014)
  audience: both
  subjects: inherited
- id: qaa/linguistics-2023/4.5.b14
  locator: { number: "4.5.b14", headingPath: ["Benchmark standards", "Minimum threshold standards"] }
  span: { start: 58129, end: 58259 }
  source: "evaluate the role language plays in shaping sociocultural norms, identities and realities in a range of public and private domains"
  stem: "4.5"
  statementType: threshold
  rung: threshold
  force: threshold
  level: fheq:6
  appliesTo: "honours graduates at the threshold"
  addressee: learner
  verbs: ["evaluate"]
  about: "language's role in shaping norms and identities"
  themes: [none]
  domain: subject-skill
  award: ["bachelor's with honours"]
  gradeOf: none
  paraphrase: "Judge how language helps shape sociocultural norms, identities and realities in public and private domains."
  quote: full   # the issuer's statement is in `source` (D-std-0014)
  audience: both
  subjects: inherited
- id: qaa/linguistics-2023/4.5.b15
  locator: { number: "4.5.b15", headingPath: ["Benchmark standards", "Minimum threshold standards"] }
  span: { start: 58262, end: 58391 }
  source: "show some understanding of language use and ideologies in relation to globalisation, mobility, sustainability and social justice."
  stem: "4.5"
  statementType: threshold
  rung: threshold
  force: threshold
  level: fheq:6
  appliesTo: "honours graduates at the threshold"
  addressee: learner
  verbs: ["show"]
  about: "language and ideology in global and sustainability contexts"
  themes: [none]
  domain: understanding
  award: ["bachelor's with honours"]
  gradeOf: none
  paraphrase: "Show some grasp of how language use and beliefs about language bear on globalisation, mobility, sustainability and social justice."
  quote: full   # the issuer's statement is in `source` (D-std-0014)
  audience: both
  subjects: inherited
- id: qaa/linguistics-2023/4.6.b1
  locator: { number: "4.6.b1", headingPath: ["Benchmark standards", "Generic skills"] }
  span: { start: 58575, end: 58609 }
  source: "hypothesis formulation and testing"
  stem: "4.6"
  statementType: outcome
  rung: none
  force: must   # D-std-0016: "need to" read as must
  level: fheq:6
  appliesTo: "students of the subject"
  addressee: learner
  verbs: []
  about: "forming and testing hypotheses"
  themes: [none]
  domain: generic-skill
  award: ["bachelor's with honours"]
  gradeOf: none
  paraphrase: "Forming hypotheses and testing them."
  quote: full   # the issuer's statement is in `source` (D-std-0014)
  audience: both
  subjects: inherited
- id: qaa/linguistics-2023/4.6.b2
  locator: { number: "4.6.b2", headingPath: ["Benchmark standards", "Generic skills"] }
  span: { start: 58612, end: 58673 }
  source: "assessing the merits of contrasting theories and explanations"
  stem: "4.6"
  statementType: outcome
  rung: none
  force: must   # D-std-0016: "need to" read as must
  level: fheq:6
  appliesTo: "students of the subject"
  addressee: learner
  verbs: ["assessing"]
  about: "weighing contrasting theories"
  themes: [none]
  domain: generic-skill
  award: ["bachelor's with honours"]
  gradeOf: none
  paraphrase: "Judging the strengths of competing theories and explanations."
  quote: full   # the issuer's statement is in `source` (D-std-0014)
  audience: both
  subjects: inherited
- id: qaa/linguistics-2023/4.6.b3
  locator: { number: "4.6.b3", headingPath: ["Benchmark standards", "Generic skills"] }
  span: { start: 58676, end: 58768 }
  source: "verbal, non-verbal and graphical communication, employing format appropriate to the audience"
  stem: "4.6"
  statementType: outcome
  rung: none
  force: must   # D-std-0016: "need to" read as must
  level: fheq:6
  appliesTo: "students of the subject"
  addressee: learner
  verbs: []
  about: "communication suited to the audience"
  themes: [none]
  domain: generic-skill
  award: ["bachelor's with honours"]
  gradeOf: none
  paraphrase: "Communicating in spoken, non-verbal and graphic forms, in a format that suits the audience."
  quote: full   # the issuer's statement is in `source` (D-std-0014)
  audience: both
  subjects: inherited
- id: qaa/linguistics-2023/4.6.b4
  locator: { number: "4.6.b4", headingPath: ["Benchmark standards", "Generic skills"] }
  span: { start: 58771, end: 58865 }
  source: "experimental design; the design and execution of research projects, individually and in groups"
  stem: "4.6"
  statementType: outcome
  rung: none
  force: must   # D-std-0016: "need to" read as must
  level: fheq:6
  appliesTo: "students of the subject"
  addressee: learner
  verbs: []
  about: "research and experimental design, alone and in groups"
  themes: [none]
  domain: generic-skill
  award: ["bachelor's with honours"]
  gradeOf: none
  paraphrase: "Designing experiments and designing and carrying out research projects, alone and in groups."
  quote: full   # the issuer's statement is in `source` (D-std-0014)
  audience: both
  subjects: inherited
- id: qaa/linguistics-2023/4.6.b5
  locator: { number: "4.6.b5", headingPath: ["Benchmark standards", "Generic skills"] }
  span: { start: 58868, end: 58934 }
  source: "understanding the appropriate and ethical use of evidence and data"
  stem: "4.6"
  statementType: outcome
  rung: none
  force: must   # D-std-0016: "need to" read as must
  level: fheq:6
  appliesTo: "students of the subject"
  addressee: learner
  verbs: ["understanding"]
  about: "ethical and appropriate use of evidence"
  themes: [none]
  domain: generic-skill
  award: ["bachelor's with honours"]
  gradeOf: none
  paraphrase: "Knowing how to use evidence and data properly and ethically."
  quote: full   # the issuer's statement is in `source` (D-std-0014)
  audience: both
  subjects: inherited
- id: qaa/linguistics-2023/4.6.b6
  locator: { number: "4.6.b6", headingPath: ["Benchmark standards", "Generic skills"] }
  span: { start: 58937, end: 59009 }
  source: "evaluating the merits of contrasting theories, explanations and evidence"
  stem: "4.6"
  statementType: outcome
  rung: none
  force: must   # D-std-0016: "need to" read as must
  level: fheq:6
  appliesTo: "students of the subject"
  addressee: learner
  verbs: ["evaluating"]
  about: "weighing theories, explanations and evidence"
  themes: [none]
  domain: generic-skill
  award: ["bachelor's with honours"]
  gradeOf: none
  paraphrase: "Judging the merits of contrasting theories and explanations and of the evidence for them."
  quote: full   # the issuer's statement is in `source` (D-std-0014)
  audience: both
  subjects: inherited
- id: qaa/linguistics-2023/4.6.b7
  locator: { number: "4.6.b7", headingPath: ["Benchmark standards", "Generic skills"] }
  span: { start: 59012, end: 59074 }
  source: "distinguishing descriptive systems from the data they describe"
  stem: "4.6"
  statementType: outcome
  rung: none
  force: must   # D-std-0016: "need to" read as must
  level: fheq:6
  appliesTo: "students of the subject"
  addressee: learner
  verbs: ["distinguishing"]
  about: "telling descriptive systems apart from data"
  themes: [none]
  domain: generic-skill
  award: ["bachelor's with honours"]
  gradeOf: none
  paraphrase: "Keeping apart a system of description and the data it is used to describe."
  quote: full   # the issuer's statement is in `source` (D-std-0014)
  audience: both
  subjects: inherited
- id: qaa/linguistics-2023/4.6.b8
  locator: { number: "4.6.b8", headingPath: ["Benchmark standards", "Generic skills"] }
  span: { start: 59077, end: 59179 }
  source: "abstracting and synthesising information; collecting, analysing and manipulating data of diverse kinds"
  stem: "4.6"
  statementType: outcome
  rung: none
  force: must   # D-std-0016: "need to" read as must
  level: fheq:6
  appliesTo: "students of the subject"
  addressee: learner
  verbs: ["abstracting", "synthesising", "collecting", "analysing", "manipulating"]
  about: "handling information and data of many kinds"
  themes: [none]
  domain: generic-skill
  award: ["bachelor's with honours"]
  gradeOf: none
  paraphrase: "Abstracting and combining information, and gathering, analysing and working with varied kinds of data."
  quote: full   # the issuer's statement is in `source` (D-std-0014)
  audience: both
  subjects: inherited
- id: qaa/linguistics-2023/4.6.b9
  locator: { number: "4.6.b9", headingPath: ["Benchmark standards", "Generic skills"] }
  span: { start: 59182, end: 59259 }
  source: "interpreting information presented in the form of diagrams, tables and graphs"
  stem: "4.6"
  statementType: outcome
  rung: none
  force: must   # D-std-0016: "need to" read as must
  level: fheq:6
  appliesTo: "students of the subject"
  addressee: learner
  verbs: ["interpreting"]
  about: "reading diagrams, tables and graphs"
  themes: [none]
  domain: generic-skill
  award: ["bachelor's with honours"]
  gradeOf: none
  paraphrase: "Making sense of information shown in diagrams, tables and graphs."
  quote: full   # the issuer's statement is in `source` (D-std-0014)
  audience: both
  subjects: inherited
- id: qaa/linguistics-2023/4.6.b10
  locator: { number: "4.6.b10", headingPath: ["Benchmark standards", "Generic skills"] }
  span: { start: 59262, end: 59396 }
  source: "searching out and synthesising information occurring in a variety of formats, giving appropriate acknowledgements and lists of sources"
  stem: "4.6"
  statementType: outcome
  rung: none
  force: must   # D-std-0016: "need to" read as must
  level: fheq:6
  appliesTo: "students of the subject"
  addressee: learner
  verbs: ["searching", "synthesising", "giving"]
  about: "finding and combining sources with proper acknowledgement"
  themes: [none]
  domain: generic-skill
  award: ["bachelor's with honours"]
  gradeOf: none
  paraphrase: "Tracking down and combining information from varied formats, with proper acknowledgement and source lists."
  quote: full   # the issuer's statement is in `source` (D-std-0014)
  audience: both
  subjects: inherited
- id: qaa/linguistics-2023/4.6.b11
  locator: { number: "4.6.b11", headingPath: ["Benchmark standards", "Generic skills"] }
  span: { start: 59399, end: 59453 }
  source: "undertaking competent self-directed study and learning"
  stem: "4.6"
  statementType: outcome
  rung: none
  force: must   # D-std-0016: "need to" read as must
  level: fheq:6
  appliesTo: "students of the subject"
  addressee: learner
  verbs: ["undertaking"]
  about: "competent self-directed study"
  themes: [none]
  domain: generic-skill
  award: ["bachelor's with honours"]
  gradeOf: none
  paraphrase: "Carrying out competent study and learning under one's own direction."
  quote: full   # the issuer's statement is in `source` (D-std-0014)
  audience: both
  subjects: inherited
- id: qaa/linguistics-2023/4.6.b12
  locator: { number: "4.6.b12", headingPath: ["Benchmark standards", "Generic skills"] }
  span: { start: 59456, end: 59575 }
  source: "understanding the importance of health and safety, and of equality, diversity and inclusiveness in the work environment"
  stem: "4.6"
  statementType: outcome
  rung: none
  force: must   # D-std-0016: "need to" read as must
  level: fheq:6
  appliesTo: "students of the subject"
  addressee: learner
  verbs: ["understanding"]
  about: "health and safety and EDI at work"
  themes: [none]
  domain: generic-skill
  award: ["bachelor's with honours"]
  gradeOf: none
  paraphrase: "Grasping why health and safety, and equality, diversity and inclusiveness, matter in the workplace."
  quote: full   # the issuer's statement is in `source` (D-std-0014)
  audience: both
  subjects: inherited
- id: qaa/linguistics-2023/4.6.b13
  locator: { number: "4.6.b13", headingPath: ["Benchmark standards", "Generic skills"] }
  span: { start: 59578, end: 59735 }
  source: "appreciating and engaging in contemporary debates relating to sustainability, employability and global perspectives, including decolonisation and anti-racism"
  stem: "4.6"
  statementType: outcome
  rung: none
  force: must   # D-std-0016: "need to" read as must
  level: fheq:6
  appliesTo: "students of the subject"
  addressee: learner
  verbs: ["appreciating", "engaging"]
  about: "current debates: sustainability, employability, decolonisation"
  themes: [none]
  domain: generic-skill
  award: ["bachelor's with honours"]
  gradeOf: none
  paraphrase: "Valuing and taking part in current debates on sustainability, employability and global perspectives, decolonisation and anti-racism among them."
  quote: full   # the issuer's statement is in `source` (D-std-0014)
  audience: both
  subjects: inherited
- id: qaa/linguistics-2023/4.6.b14
  locator: { number: "4.6.b14", headingPath: ["Benchmark standards", "Generic skills"] }
  span: { start: 59738, end: 59832 }
  source: "appreciating the need to act in a sustainable manner and display ethical behaviour and conduct"
  stem: "4.6"
  statementType: outcome
  rung: none
  force: must   # D-std-0016: "need to" read as must
  level: fheq:6
  appliesTo: "students of the subject"
  addressee: learner
  verbs: ["appreciating", "act", "display"]
  about: "sustainable and ethical conduct"
  themes: [none]
  domain: generic-skill
  award: ["bachelor's with honours"]
  gradeOf: none
  paraphrase: "Seeing the need to act sustainably and to behave and conduct oneself ethically."
  quote: full   # the issuer's statement is in `source` (D-std-0014)
  audience: both
  subjects: inherited
- id: qaa/linguistics-2023/4.6.b15
  locator: { number: "4.6.b15", headingPath: ["Benchmark standards", "Generic skills"] }
  span: { start: 59835, end: 60000 }
  source: "communicating subject knowledge (of language) in an authoritative and sensitive way to stakeholders responsible for policies in which language is a critical element."
  stem: "4.6"
  statementType: outcome
  rung: none
  force: must   # D-std-0016: "responsible for" read as must
  level: fheq:6
  appliesTo: "students of the subject"
  addressee: learner
  verbs: ["communicating"]
  about: "communicating language knowledge to policy stakeholders"
  themes: [none]
  domain: generic-skill
  award: ["bachelor's with honours"]
  gradeOf: none
  paraphrase: "Conveying knowledge about language with authority and sensitivity to those responsible for policies where language matters."
  quote: full   # the issuer's statement is in `source` (D-std-0014)
  audience: both
  subjects: inherited
```

### S4a Audience versions
<!-- label: both; status: drafted; basis: primary. forPractitioner: for the programme designer or teacher. forBeneficiary: for the student, second person, naming no issuer. author-agent-written: instructions to an AI agent writing about the statement (a course document, a handbook, an outcome, a report). author-agent-dialogue: instructions to an AI agent using the statement in conversation (with a student, a teacher or a programme team). Written fresh from the held text alone (benchmark rule 6; Abbott, 15:42). -->
```yaml
- statement: qaa/linguistics-2023/1.13
  forPractitioner: { text: "Plan for a steady growth in professional communication across the course, set in varied environments, with respect for linguistic, social and cultural difference built in; support students to learn actively and independently and to read their academic setting critically.", rewrite: light, force: must, status: drafted }
  forBeneficiary: { text: "Over your course you are normally expected to get better at communicating in a professional way, wherever you are working, while showing respect for differences of language, society and culture. You will also be helped to learn actively and on your own, with growing confidence.", rewrite: full, force: must, status: drafted }
  author-agent-written: "Present this as a described expectation of growth through the course, not a threshold the award requires: the issuer's wording is 'normally expected', which sits outside must, should and will. Place it at honours level (fheq:6) and cite it as QAA (2023) Linguistics Subject Benchmark Statement, para 1.13. Do not state it as a pass condition; set it beside the threshold item on communicating observations (qaa/linguistics-2023/4.5.b11), the generic skill on communication to audiences (qaa/linguistics-2023/4.6.b3) and the honours descriptor on communication (std:doc:qaa-fheq-2024-framework qaa/fheq-2024/4.15.b8)."
  author-agent-dialogue: "Raise it when a student or team talks about placements, group work or speaking to people from other language backgrounds. With a student, say plainly that the course expects them to grow in professional communication and in respect for difference; with staff, frame it as a progression the modules should build. Ask: 'Where in your course have you had to communicate with people whose language or culture differs from yours?' and 'What would you do differently next time?' Avoid reading it as a fixed hurdle at a set mark."
- statement: qaa/linguistics-2023/1.19.b4
  forPractitioner: { text: "Give language and linguistic diversity deliberate attention when making education inclusive: language use and understanding shape who gains access, inclusion and opportunity, in line with SDG4 (Quality Education).", rewrite: light, force: should, status: drafted }
  forBeneficiary: { text: "not-applicable: a principle for those who shape education, not an outcome a student reaches", rewrite: full, force: should, status: drafted }
  author-agent-written: "Treat this as a 'should' addressed to whoever designs or runs education, given within the statement's list of links to the UN Sustainable Development Goals (SDG4). It holds at no single level and binds no student. Cite it as QAA (2023) Linguistics Subject Benchmark Statement, para 1.19 (fourth bullet); do not present it as a regulatory duty. Set it beside the accessibility paragraphs (qaa/linguistics-2023/1.12 to 1.16), the provider expectation on access to technology (qaa/linguistics-2023/2.12) and the ESD guidance (std:doc:qaa-advancehe-esd-2021-guidance)."
  author-agent-dialogue: "Raise it with a programme team discussing inclusive curricula, language support or education for sustainable development. Put it in practitioner terms: inclusive education needs explicit attention to the languages and varieties students bring. Ask: 'Which languages and varieties do your students use, and where does the course recognise them?' Do not hand it to a student as something they must achieve."
- statement: qaa/linguistics-2023/1.26
  forPractitioner: { text: "Make the social uses of linguistic skill visible in modules (challenging language ideologies, scrutinising policy, uncovering assumptions in discourse, testing theory against data) and give students practice in naming and evidencing those skills for employers.", rewrite: light, force: will, status: drafted }
  forBeneficiary: { text: "You will be able to explain to employers, and show them, the skills your study has given you: questioning beliefs about language, examining how institutions use it, spotting hidden assumptions and judging theories against evidence.", rewrite: full, force: will, status: drafted }
  author-agent-written: "Present this as an outcome graduates are able to show (force: will) at honours level (fheq:6), within the enterprise and entrepreneurship section. Cite it as QAA (2023) Linguistics Subject Benchmark Statement, para 1.26. Do not claim it guarantees employment or that it is a threshold item; it sits outside the rung list. Set it beside the generic skills (qaa/linguistics-2023/4.6.b13, 4.6.b15), the honours descriptor's qualities for employment (std:doc:qaa-fheq-2024-framework qaa/fheq-2024/4.15.b9.1) and the 2018 enterprise guidance (std:doc:qaa-enterprise-2018-guidance)."
  author-agent-dialogue: "Raise it when a student prepares a CV, a placement application or an interview, or when staff plan employability work. With a student, use 'you' and ask them to name a skill and the evidence for it. Ask: 'Which piece of your linguistics work shows you questioning an assumption?' and 'How would you explain that to someone outside the subject?' Avoid lecturing on the issuer's list of sectors."
- statement: qaa/linguistics-2023/2.5
  forPractitioner: { text: "Map each level of the course so that it adds knowledge, skills, expertise and experience in steps that lead to the threshold subject skills at the end; progression rules remain the institution's own.", rewrite: light, force: will, status: drafted }
  forBeneficiary: { text: "You will move up through the levels of your course under your institution's rules, and each year should build what you know and can do until you reach the standard needed for your honours degree.", rewrite: full, force: will, status: drafted }
  author-agent-written: "Present this as a 'will' about progression across the levels of an honours course that ends at FHEQ Level 6 (FQHEIS Level 10), as the paragraph itself states. Cite it as QAA (2023) Linguistics Subject Benchmark Statement, para 2.5. Do not claim it sets level-by-level outcomes; the statement gives none below honours. Set it beside the threshold list (qaa/linguistics-2023/4.5.b1 to 4.5.b15), the progression signs in para 2.6 and the reference framework's steps spine:4 to spine:6 (std:ref:uk-framework, R8)."
  author-agent-dialogue: "Raise it when a student asks how first and second year relate to the final standard, or when a team designs level outcomes. Put it simply: each year builds towards the final threshold. Ask: 'What can you do now that you could not do a year ago?' and 'Which threshold skills still feel furthest away?' Avoid implying the statement fixes what each year must contain."
- statement: qaa/linguistics-2023/2.7
  forPractitioner: { text: "On joint, combined or major-minor routes, secure the core of the subject's specific and generic skills, then let the partner subject's requirements add to them; consider space for interdisciplinary study across the two.", rewrite: light, force: will, status: drafted }
  forBeneficiary: { text: "If you study linguistics with another subject, you will gain the core linguistics skills, both subject-specific and general, and add others that your other subject asks for. You may also get to explore where the two subjects meet.", rewrite: full, force: will, status: drafted }
  author-agent-written: "Present this as a 'will' for joint, combined and major-minor honours (fheq:6): such graduates reach the core of the skills, not every item. Cite it as QAA (2023) Linguistics Subject Benchmark Statement, para 2.7, and read it with para 4.1, which says joint degrees draw on a subset of the standards. Do not claim joint-honours students must meet all fifteen threshold items; set it beside qaa/linguistics-2023/4.5.b1 to 4.5.b15 and qaa/linguistics-2023/4.6.b1 to 4.6.b15."
  author-agent-dialogue: "Raise it with joint-honours students or with teams designing combined routes. With a student, explain that they need the core skills of linguistics plus what the other subject adds. Ask: 'Which linguistics skills does your course treat as core for you?' and 'Where do your two subjects meet?' Avoid telling a joint student they are held to the single-honours range."
- statement: qaa/linguistics-2023/2.9
  forPractitioner: { text: "Consider short standalone credentials that can stack into larger awards, designed so they appeal to learners for professional and personal development and still advance the study of linguistics.", rewrite: light, force: must, status: drafted }
  forBeneficiary: { text: "not-applicable: a forecast about provider planning, not something a student achieves", rewrite: full, force: must, status: drafted }
  author-agent-written: "Present this as a forecast about provider planning, worded as a growing necessity ('will increasingly be necessary', 'will need to'), not as a standard on students or a firm obligation. Cite it as QAA (2023) Linguistics Subject Benchmark Statement, para 2.9. Do not claim the statement requires micro-credentials or sets their level; it gives none. Set it beside the flexibility paragraphs (qaa/linguistics-2023/2.10 to 2.12)."
  author-agent-dialogue: "Raise it only with programme or portfolio teams planning short courses or stackable credit. Frame it as a trend the subject community expects, with two tests: appeal to learners and value to the subject. Ask: 'Would this short course stand on its own for a learner, and would it count towards a degree?' Do not present it to students."
- statement: qaa/linguistics-2023/2.12
  forPractitioner: { text: "Resource and train staff for accessible, inclusive and flexible delivery; where you use digital technology, account for students' differing access to devices and connectivity so that none is disadvantaged.", rewrite: light, force: must, status: drafted }
  forBeneficiary: { text: "not-applicable: a duty on the provider; the student meets its effect", rewrite: full, force: must, status: drafted }
  author-agent-written: "Present this as a provider necessity ('requires', 'needs to be recognised', recorded as must; the reading is ours and is listed for review), not a student outcome. It holds for delivery at every level and names none. Cite it as QAA (2023) Linguistics Subject Benchmark Statement, para 2.12. Do not claim it is a legal duty; the paragraph cites no law. Set it beside the accessibility paragraphs (qaa/linguistics-2023/1.12 to 1.16) and para 2.11 on flexible delivery."
  author-agent-dialogue: "Raise it with a programme team moving teaching or assessment online, or when a student reports trouble getting online. With staff, ask what resources and training the change needs and who might lack devices or connection. Ask: 'Which students would struggle to reach this material, and what is the alternative?' Do not put it to a student as their responsibility."
- statement: qaa/linguistics-2023/2.20
  forPractitioner: { text: "Involve external reviewers in periodic review, asking them to test proposed changes, confirm that threshold standards are met and judge whether content fits the subject.", rewrite: light, force: will, status: drafted }
  forBeneficiary: { text: "not-applicable: a duty on the provider in quality assurance", rewrite: full, force: will, status: drafted }
  author-agent-written: "Present this as a provider 'will' in quality assurance: external reviewers take part in periodic review. It applies to the course, not to a level of student achievement. Cite it as QAA (2023) Linguistics Subject Benchmark Statement, para 2.20. Do not claim it is an Office for Students condition; the statement says it is not a regulatory requirement in England. Set it beside para 2.19 on review, para 2.21 on external examiners and the threshold list (qaa/linguistics-2023/4.5.b1 to 4.5.b15)."
  author-agent-dialogue: "Raise it with programme teams preparing for periodic review or revalidation. Frame it as the place where outside reviewers test changes against the threshold standards. Ask: 'Which threshold items would an external reviewer find hard to trace in your modules?' Do not raise it with students as something they do."
- statement: qaa/linguistics-2023/4.2
  forPractitioner: { text: "Set your own evidence for achievement above the threshold, and use Annex D, which describes each honours class at FHEQ Level 6 (FQHEIS Level 10), when you describe the 1st, 2.1, 2.2 and 3rd.", rewrite: light, force: should, status: drafted }
  forBeneficiary: { text: "not-applicable: a duty on the provider; the student-facing account of classes belongs to the provider's own criteria", rewrite: full, force: should, status: drafted }
  author-agent-written: "Present this as a provider 'should': refer to Annex D when deciding how achievement above the threshold is evidenced. It concerns the honours award at FHEQ Level 6 and FQHEIS Level 10. Cite it as QAA (2023) Linguistics Subject Benchmark Statement, para 4.2, and Annex D as std:doc:qaa-fheq-2024-framework, Annex D (qaa/fheq-2024/annex-d/...; the 3rd column, such as qaa/fheq-2024/annex-d/summary/r1/3rd, is the threshold). Do not claim the statement itself defines typical or excellent standards; it does not."
  author-agent-dialogue: "Raise it with staff writing marking criteria or classification descriptors for linguistics. Frame it as a pointer: the subject sets the floor, Annex D describes the classes above it. Ask: 'How do your criteria for a 2.1 differ from the threshold list?' Avoid telling a student that the threshold list describes a good result."
- statement: qaa/linguistics-2023/4.3
  forPractitioner: { text: "Ensure every graduate meets the basic concepts and analytic methods of the core areas (phonetics, phonology, morphology, syntax, semantics, pragmatics and discourse), then builds on them into domains such as acquisition, variation and change, society and cognition.", rewrite: light, force: will, status: drafted }
  forBeneficiary: { text: "You will be expected to understand the basic ideas and methods of analysis in the core areas of linguistics, such as sounds, word structure, sentence structure, meaning, use in context and discourse, and to use them to learn about how language is acquired, varies, changes, works in society and works in the mind.", rewrite: full, force: will, status: drafted }
  author-agent-written: "Present this as a 'will be expected' outcome for honours graduates (fheq:6) that frames the threshold list rather than belonging to it. Cite it as QAA (2023) Linguistics Subject Benchmark Statement, para 4.3. Do not present the named core areas as a compulsory syllabus; para 1.5 says the statement does not set definitive design criteria. Set it beside qaa/linguistics-2023/4.5.b1 and 4.4, and the honours descriptor on systematic understanding (std:doc:qaa-fheq-2024-framework qaa/fheq-2024/4.15.b1)."
  author-agent-dialogue: "Raise it when a student asks what a linguistics graduate is supposed to know, or when a team checks core module coverage. With a student, list the core areas in plain terms and ask which feel secure. Ask: 'Could you analyse a short sample of data at each level, from sound to discourse?' Avoid reciting the paragraph or treating every area as equally weighted on every course."
- statement: qaa/linguistics-2023/4.4
  forPractitioner: { text: "Expose students to a range of real language phenomena and to the terminology and methods for describing and analysing them, framed by theory even where the work is mostly descriptive.", rewrite: light, force: must, status: drafted }
  forBeneficiary: { text: "You are expected to know about a range of real language phenomena and the technical terms and methods used to describe and analyse them, usually within a theory that explains them.", rewrite: full, force: must, status: drafted }
  author-agent-written: "Present this as a described expectation ('is expected to', outside must, should and will) for honours graduates at fheq:6, not as an item on the threshold list. Cite it as QAA (2023) Linguistics Subject Benchmark Statement, para 4.4. Do not claim it requires a particular theoretical school. Set it beside qaa/linguistics-2023/4.3, the threshold item on knowledge of concepts and methods (qaa/linguistics-2023/4.5.b1) and Annex D's knowledge strand at threshold (std:doc:qaa-fheq-2024-framework qaa/fheq-2024/annex-d/knowledge/r1/3rd)."
  author-agent-dialogue: "Raise it when a student is unsure whether describing data is enough, or when staff review how theory frames descriptive work. Say plainly that description is fine if it is grounded in a theory. Ask: 'Which theory helps you explain the pattern you described?' Avoid presenting it as a separate hurdle from the threshold list."
- statement: qaa/linguistics-2023/4.5.b1
  forPractitioner: { text: "Graduates at threshold show they know the field's basic analytic concepts and its methods of inquiry.", rewrite: light, force: threshold, status: drafted }
  forBeneficiary: { text: "You will show that you know the basic concepts linguists use to analyse language and the main ways they investigate it.", rewrite: full, force: threshold, status: drafted }
  author-agent-written: "Present this as threshold item 1 of 15: the minimum a Linguistics honours graduate shows at FHEQ Level 6 (FQHEIS Level 10), here knowledge of the basic analytic concepts and methods of inquiry. Cite it as QAA (2023) Linguistics Subject Benchmark Statement, para 4.5, bullet 1. Do not call it a regulatory requirement or a picture of a good result, and do not apply it to any award below honours. Set it beside qaa/linguistics-2023/4.3, the honours descriptor on systematic understanding (std:doc:qaa-fheq-2024-framework qaa/fheq-2024/4.15.b1) and Annex D's knowledge strand (qaa/fheq-2024/annex-d/knowledge/r1/3rd) and the reference framework's step spine:6 (std:ref:uk-framework, R8)."
  author-agent-dialogue: "Raise it when a student wonders whether they have the basics, or a team audits its introductory modules. With a student, say in plain words and in the second person that this is the least they need to show by the end of the degree; with staff, ask where the course teaches and assesses it. Ask: 'Which analytic concepts do you use without having to look them up?' and 'Which method of inquiry could you explain to a first-year student?' Do not read the list aloud or treat it as the level most students reach. Most students go well beyond it (para 4.2)."
- statement: qaa/linguistics-2023/4.5.b2
  forPractitioner: { text: "Graduates at threshold identify, describe and analyse language phenomena in an orderly, systematic way.", rewrite: light, force: threshold, status: drafted }
  forBeneficiary: { text: "You will be able to work through language data step by step: spotting a feature, describing it and then analysing it.", rewrite: full, force: threshold, status: drafted }
  author-agent-written: "Present this as threshold item 2 of 15: the minimum a Linguistics honours graduate shows at FHEQ Level 6 (FQHEIS Level 10), here working systematically from identifying to describing to analysing language phenomena. Cite it as QAA (2023) Linguistics Subject Benchmark Statement, para 4.5, bullet 2. Do not call it a regulatory requirement or a picture of a good result, and do not apply it to any award below honours. Set it beside qaa/linguistics-2023/4.5.b5 and the honours descriptor on accurate use of established techniques (std:doc:qaa-fheq-2024-framework qaa/fheq-2024/4.15.b2) and the reference framework's step spine:6 (std:ref:uk-framework, R8)."
  author-agent-dialogue: "Raise it when a student jumps straight to interpretation, or staff set data-analysis tasks. With a student, say in plain words and in the second person that this is the least they need to show by the end of the degree; with staff, ask where the course teaches and assesses it. Ask: 'What did you notice first, how did you describe it, and only then what did you conclude?' Do not read the list aloud or treat it as the level most students reach. Most students go well beyond it (para 4.2)."
- statement: qaa/linguistics-2023/4.5.b3
  forPractitioner: { text: "Graduates at threshold pose well-grounded questions about language structure and use.", rewrite: light, force: threshold, status: drafted }
  forBeneficiary: { text: "You will be able to ask good, well-reasoned questions about how language is built and how people use it.", rewrite: full, force: threshold, status: drafted }
  author-agent-written: "Present this as threshold item 3 of 15: the minimum a Linguistics honours graduate shows at FHEQ Level 6 (FQHEIS Level 10), here posing well-grounded questions about language structure and use. Cite it as QAA (2023) Linguistics Subject Benchmark Statement, para 4.5, bullet 3. Do not call it a regulatory requirement or a picture of a good result, and do not apply it to any award below honours. Set it beside qaa/linguistics-2023/4.5.b6 and the honours descriptor on framing questions (std:doc:qaa-fheq-2024-framework qaa/fheq-2024/4.15.b7) and the reference framework's step spine:6 (std:ref:uk-framework, R8)."
  author-agent-dialogue: "Raise it when a student is choosing a project or dissertation topic. With a student, say in plain words and in the second person that this is the least they need to show by the end of the degree; with staff, ask where the course teaches and assesses it. Ask: 'Why is your question worth asking, and what in the data or the literature prompted it?' Do not read the list aloud or treat it as the level most students reach. Most students go well beyond it (para 4.2)."
- statement: qaa/linguistics-2023/4.5.b4
  forPractitioner: { text: "Graduates at threshold apply basic techniques for collecting or eliciting and transcribing data suited to the sub-disciplines, such as corpora, media and political or advertising texts, elicitation tasks, introspection, laboratory work, questionnaires, interviews or fieldwork.", rewrite: light, force: threshold, status: drafted }
  forBeneficiary: { text: "You will be able to use the basic ways of gathering and transcribing language data that fit your area, such as corpora, media texts, experiments, questionnaires, interviews or fieldwork.", rewrite: full, force: threshold, status: drafted }
  author-agent-written: "Present this as threshold item 4 of 15: the minimum a Linguistics honours graduate shows at FHEQ Level 6 (FQHEIS Level 10), here basic techniques for gathering, eliciting and transcribing data. Cite it as QAA (2023) Linguistics Subject Benchmark Statement, para 4.5, bullet 4. Do not call it a regulatory requirement or a picture of a good result, and do not apply it to any award below honours. Set it beside qaa/linguistics-2023/4.6.b8, the honours descriptor on applying methods (std:doc:qaa-fheq-2024-framework qaa/fheq-2024/4.15.b6) and Annex D's practical strand (qaa/fheq-2024/annex-d/practical/r1/3rd) and the reference framework's step spine:6 (std:ref:uk-framework, R8)."
  author-agent-dialogue: "Raise it when a student plans data collection or staff design methods training. With a student, say in plain words and in the second person that this is the least they need to show by the end of the degree; with staff, ask where the course teaches and assesses it. Ask: 'Which data-gathering method suits your question, and how will you transcribe what you collect?' Do not read the list aloud or treat it as the level most students reach. Most students go well beyond it (para 4.2)."
- statement: qaa/linguistics-2023/4.5.b5
  forPractitioner: { text: "Graduates at threshold apply the analytic concepts of each level of linguistic analysis to suitable data sets.", rewrite: light, force: threshold, status: drafted }
  forBeneficiary: { text: "You will be able to take the concepts for each level of analysis, such as sounds, words or sentences, and use them on real data.", rewrite: full, force: threshold, status: drafted }
  author-agent-written: "Present this as threshold item 5 of 15: the minimum a Linguistics honours graduate shows at FHEQ Level 6 (FQHEIS Level 10), here applying the concepts of each level of analysis to suitable data. Cite it as QAA (2023) Linguistics Subject Benchmark Statement, para 4.5, bullet 5. Do not call it a regulatory requirement or a picture of a good result, and do not apply it to any award below honours. Set it beside qaa/linguistics-2023/4.5.b2 and the honours descriptor on arguing and solving problems (std:doc:qaa-fheq-2024-framework qaa/fheq-2024/4.15.b3.1) and the reference framework's step spine:6 (std:ref:uk-framework, R8)."
  author-agent-dialogue: "Raise it when a student meets a new data set or staff write problem sets. With a student, say in plain words and in the second person that this is the least they need to show by the end of the degree; with staff, ask where the course teaches and assesses it. Ask: 'Which level of analysis does this data call for, and which concept would you start with?' Do not read the list aloud or treat it as the level most students reach. Most students go well beyond it (para 4.2)."
- statement: qaa/linguistics-2023/4.5.b6
  forPractitioner: { text: "Graduates at threshold formulate linguistic generalisations and construct and test hypotheses on suitable evidence.", rewrite: light, force: threshold, status: drafted }
  forBeneficiary: { text: "You will be able to draw general patterns from language data and set up and test hypotheses using the right kind of evidence.", rewrite: full, force: threshold, status: drafted }
  author-agent-written: "Present this as threshold item 6 of 15: the minimum a Linguistics honours graduate shows at FHEQ Level 6 (FQHEIS Level 10), here forming generalisations and building and testing hypotheses on evidence. Cite it as QAA (2023) Linguistics Subject Benchmark Statement, para 4.5, bullet 6. Do not call it a regulatory requirement or a picture of a good result, and do not apply it to any award below honours. Set it beside the generic skill on hypotheses (qaa/linguistics-2023/4.6.b1) and the honours descriptor on critical evaluation (std:doc:qaa-fheq-2024-framework qaa/fheq-2024/4.15.b7) and the reference framework's step spine:6 (std:ref:uk-framework, R8)."
  author-agent-dialogue: "Raise it when a student moves from describing examples to claiming a pattern. With a student, say in plain words and in the second person that this is the least they need to show by the end of the degree; with staff, ask where the course teaches and assesses it. Ask: 'What would count as evidence against your generalisation, and have you looked for it?' Do not read the list aloud or treat it as the level most students reach. Most students go well beyond it (para 4.2)."
- statement: qaa/linguistics-2023/4.5.b7
  forPractitioner: { text: "Graduates at threshold evaluate alternative analyses of a data set, understanding how theory organises analysis and settles what counts as evidence.", rewrite: light, force: threshold, status: drafted }
  forBeneficiary: { text: "You will be able to compare different analyses of the same data and judge between them, knowing how theory shapes analysis and what counts as evidence.", rewrite: full, force: threshold, status: drafted }
  author-agent-written: "Present this as threshold item 7 of 15: the minimum a Linguistics honours graduate shows at FHEQ Level 6 (FQHEIS Level 10), here judging between competing analyses of the same data. Cite it as QAA (2023) Linguistics Subject Benchmark Statement, para 4.5, bullet 7. Do not call it a regulatory requirement or a picture of a good result, and do not apply it to any award below honours. Set it beside qaa/linguistics-2023/4.5.b8, qaa/linguistics-2023/4.6.b6 and the honours descriptor on uncertainty (std:doc:qaa-fheq-2024-framework qaa/fheq-2024/4.15.b4) and the reference framework's step spine:6 (std:ref:uk-framework, R8)."
  author-agent-dialogue: "Raise it when two analyses of the same data seem equally plausible to a student. With a student, say in plain words and in the second person that this is the least they need to show by the end of the degree; with staff, ask where the course teaches and assesses it. Ask: 'Which analysis accounts for more of the data, and what does each theory treat as evidence?' Do not read the list aloud or treat it as the level most students reach. Most students go well beyond it (para 4.2)."
- statement: qaa/linguistics-2023/4.5.b8
  forPractitioner: { text: "Graduates at threshold evaluate alternative theories, grounded in an understanding of linguistic theory and of explanation in the field.", rewrite: light, force: threshold, status: drafted }
  forBeneficiary: { text: "You will be able to compare and judge rival theories, knowing what a linguistic theory is and what makes a good explanation.", rewrite: full, force: threshold, status: drafted }
  author-agent-written: "Present this as threshold item 8 of 15: the minimum a Linguistics honours graduate shows at FHEQ Level 6 (FQHEIS Level 10), here judging between rival theories and what counts as an explanation. Cite it as QAA (2023) Linguistics Subject Benchmark Statement, para 4.5, bullet 8. Do not call it a regulatory requirement or a picture of a good result, and do not apply it to any award below honours. Set it beside qaa/linguistics-2023/4.5.b7, qaa/linguistics-2023/4.6.b2 and the honours descriptor on commenting on research (std:doc:qaa-fheq-2024-framework qaa/fheq-2024/4.15.b3.2) and the reference framework's step spine:6 (std:ref:uk-framework, R8)."
  author-agent-dialogue: "Raise it when a student meets two schools of thought on the same question. With a student, say in plain words and in the second person that this is the least they need to show by the end of the degree; with staff, ask where the course teaches and assesses it. Ask: 'What does each theory explain that the other cannot?' Do not read the list aloud or treat it as the level most students reach. Most students go well beyond it (para 4.2)."
- statement: qaa/linguistics-2023/4.5.b9
  forPractitioner: { text: "Graduates at threshold present data and analysis using each sub-discipline's conventions: bracketing, tree diagrams, formal logic, graphs, tables, matrices and transcription systems.", rewrite: light, force: threshold, status: drafted }
  forBeneficiary: { text: "You will be able to set out your data and analysis using the conventions your area expects, such as tree diagrams, brackets, logic notation, graphs, tables or phonetic transcription.", rewrite: full, force: threshold, status: drafted }
  author-agent-written: "Present this as threshold item 9 of 15: the minimum a Linguistics honours graduate shows at FHEQ Level 6 (FQHEIS Level 10), here presenting data and analysis with the conventions of each sub-discipline. Cite it as QAA (2023) Linguistics Subject Benchmark Statement, para 4.5, bullet 9. Do not call it a regulatory requirement or a picture of a good result, and do not apply it to any award below honours. Set it beside qaa/linguistics-2023/4.6.b3, the honours descriptor on communication (std:doc:qaa-fheq-2024-framework qaa/fheq-2024/4.15.b8) and Annex D's practical strand (qaa/fheq-2024/annex-d/practical/r4/3rd) and the reference framework's step spine:6 (std:ref:uk-framework, R8)."
  author-agent-dialogue: "Raise it when a student is unsure how to lay out an analysis or staff write assessment guidance. With a student, say in plain words and in the second person that this is the least they need to show by the end of the degree; with staff, ask where the course teaches and assesses it. Ask: 'Which notation does your sub-field expect here, and would a specialist read it without help?' Do not read the list aloud or treat it as the level most students reach. Most students go well beyond it (para 4.2)."
- statement: qaa/linguistics-2023/4.5.b10
  forPractitioner: { text: "Graduates at threshold use linguistic terminology, theory and research to tackle real-world problems.", rewrite: light, force: threshold, status: drafted }
  forBeneficiary: { text: "You will be able to use linguistic terms, theory and research to help with real problems outside your course.", rewrite: full, force: threshold, status: drafted }
  author-agent-written: "Present this as threshold item 10 of 15: the minimum a Linguistics honours graduate shows at FHEQ Level 6 (FQHEIS Level 10), here using linguistic terms, theory and research on real problems. Cite it as QAA (2023) Linguistics Subject Benchmark Statement, para 4.5, bullet 10. Do not call it a regulatory requirement or a picture of a good result, and do not apply it to any award below honours. Set it beside qaa/linguistics-2023/1.26, the applied fields in para 3.4 and the honours descriptor on applying methods (std:doc:qaa-fheq-2024-framework qaa/fheq-2024/4.15.b6) and the reference framework's step spine:6 (std:ref:uk-framework, R8)."
  author-agent-dialogue: "Raise it when a student asks what linguistics is for, or a team plans applied or placement modules. With a student, say in plain words and in the second person that this is the least they need to show by the end of the degree; with staff, ask where the course teaches and assesses it. Ask: 'What problem outside the university could your linguistics help with, and how?' Do not read the list aloud or treat it as the level most students reach. Most students go well beyond it (para 4.2)."
- statement: qaa/linguistics-2023/4.5.b11
  forPractitioner: { text: "Graduates at threshold understand and communicate observations on how language represents ideology, power, social identity and social reality.", rewrite: light, force: threshold, status: drafted }
  forBeneficiary: { text: "You will understand, and be able to explain, how language can carry ideology and power and shape how identities and social realities are shown.", rewrite: full, force: threshold, status: drafted }
  author-agent-written: "Present this as threshold item 11 of 15: the minimum a Linguistics honours graduate shows at FHEQ Level 6 (FQHEIS Level 10), here understanding and explaining how language represents ideology, power and identity. Cite it as QAA (2023) Linguistics Subject Benchmark Statement, para 4.5, bullet 11. Do not call it a regulatory requirement or a picture of a good result, and do not apply it to any award below honours. Set it beside qaa/linguistics-2023/4.5.b12, para 1.9 and the honours descriptor on communication (std:doc:qaa-fheq-2024-framework qaa/fheq-2024/4.15.b8) and the reference framework's step spine:6 (std:ref:uk-framework, R8)."
  author-agent-dialogue: "Raise it when a student analyses media, political or institutional texts. With a student, say in plain words and in the second person that this is the least they need to show by the end of the degree; with staff, ask where the course teaches and assesses it. Ask: 'Whose view does this text take for granted, and which language features show it?' Do not read the list aloud or treat it as the level most students reach. Most students go well beyond it (para 4.2)."
- statement: qaa/linguistics-2023/4.5.b12
  forPractitioner: { text: "Graduates at threshold analyse how language depicts minority groups across regional, sociocultural and situational settings.", rewrite: light, force: threshold, status: drafted }
  forBeneficiary: { text: "You will be able to analyse how language portrays minority groups in different places, cultures and situations.", rewrite: full, force: threshold, status: drafted }
  author-agent-written: "Present this as threshold item 12 of 15: the minimum a Linguistics honours graduate shows at FHEQ Level 6 (FQHEIS Level 10), here analysing how language represents minority groups. Cite it as QAA (2023) Linguistics Subject Benchmark Statement, para 4.5, bullet 12. Do not call it a regulatory requirement or a picture of a good result, and do not apply it to any award below honours. Set it beside qaa/linguistics-2023/4.5.b11, the EDI paragraphs (qaa/linguistics-2023/1.7 to 1.11) and the honours descriptor on critical evaluation (std:doc:qaa-fheq-2024-framework qaa/fheq-2024/4.15.b7) and the reference framework's step spine:6 (std:ref:uk-framework, R8)."
  author-agent-dialogue: "Raise it when a student works on representation, discourse or sociolinguistic data. With a student, say in plain words and in the second person that this is the least they need to show by the end of the degree; with staff, ask where the course teaches and assesses it. Ask: 'How do the word choices in this text position the group it describes?' Do not read the list aloud or treat it as the level most students reach. Most students go well beyond it (para 4.2)."
- statement: qaa/linguistics-2023/4.5.b13
  forPractitioner: { text: "Graduates at threshold identify and examine examples of, and reasons for, variation across situational, social, cultural, regional, historical, multilingual and cross-cultural contexts.", rewrite: light, force: threshold, status: drafted }
  forBeneficiary: { text: "You will be able to spot and look into how and why language varies between situations, social groups, cultures, regions and periods, as well as between languages.", rewrite: full, force: threshold, status: drafted }
  author-agent-written: "Present this as threshold item 13 of 15: the minimum a Linguistics honours graduate shows at FHEQ Level 6 (FQHEIS Level 10), here identifying and examining variation and its causes across contexts. Cite it as QAA (2023) Linguistics Subject Benchmark Statement, para 4.5, bullet 13. Do not call it a regulatory requirement or a picture of a good result, and do not apply it to any award below honours. Set it beside the domains in para 3.3 (sociolinguistics, historical linguistics) and the honours descriptor on systematic understanding (std:doc:qaa-fheq-2024-framework qaa/fheq-2024/4.15.b1) and the reference framework's step spine:6 (std:ref:uk-framework, R8)."
  author-agent-dialogue: "Raise it when a student meets dialect, register or language-change data. With a student, say in plain words and in the second person that this is the least they need to show by the end of the degree; with staff, ask where the course teaches and assesses it. Ask: 'What explains this variation: the situation, the speaker's group, the region or the period?' Do not read the list aloud or treat it as the level most students reach. Most students go well beyond it (para 4.2)."
- statement: qaa/linguistics-2023/4.5.b14
  forPractitioner: { text: "Graduates at threshold evaluate how far language shapes sociocultural norms, identities and realities, in public and in private domains.", rewrite: light, force: threshold, status: drafted }
  forBeneficiary: { text: "You will be able to judge how language helps to shape social norms, identities and realities, in public life and in private.", rewrite: full, force: threshold, status: drafted }
  author-agent-written: "Present this as threshold item 14 of 15: the minimum a Linguistics honours graduate shows at FHEQ Level 6 (FQHEIS Level 10), here judging language's part in shaping norms, identities and realities. Cite it as QAA (2023) Linguistics Subject Benchmark Statement, para 4.5, bullet 14. Do not call it a regulatory requirement or a picture of a good result, and do not apply it to any award below honours. Set it beside qaa/linguistics-2023/4.5.b11 and the honours descriptor on critical evaluation (std:doc:qaa-fheq-2024-framework qaa/fheq-2024/4.15.b7) and the reference framework's step spine:6 (std:ref:uk-framework, R8)."
  author-agent-dialogue: "Raise it when a student studies discourse, identity or language attitudes. With a student, say in plain words and in the second person that this is the least they need to show by the end of the degree; with staff, ask where the course teaches and assesses it. Ask: 'How does this way of speaking make some behaviour seem normal, and for whom?' Do not read the list aloud or treat it as the level most students reach. Most students go well beyond it (para 4.2)."
- statement: qaa/linguistics-2023/4.5.b15
  forPractitioner: { text: "Graduates at threshold show some grasp of how language use and language ideologies connect with globalisation, mobility, sustainability and social justice.", rewrite: light, force: threshold, status: drafted }
  forBeneficiary: { text: "You will show some understanding of how language use and beliefs about language connect with globalisation, migration and movement, sustainability and social justice.", rewrite: full, force: threshold, status: drafted }
  author-agent-written: "Present this as threshold item 15 of 15: the minimum a Linguistics honours graduate shows at FHEQ Level 6 (FQHEIS Level 10), here some understanding of language and ideology in global and sustainability contexts. Cite it as QAA (2023) Linguistics Subject Benchmark Statement, para 4.5, bullet 15. Do not call it a regulatory requirement or a picture of a good result, and do not apply it to any award below honours. Set it beside the sustainability paragraphs (qaa/linguistics-2023/1.17 to 1.21), qaa/linguistics-2023/4.6.b13 and the honours descriptor on uncertainty and limits of knowledge (std:doc:qaa-fheq-2024-framework qaa/fheq-2024/4.15.b4) and the reference framework's step spine:6 (std:ref:uk-framework, R8)."
  author-agent-dialogue: "Raise it when a student or team links linguistics to sustainability, migration or justice. With a student, say in plain words and in the second person that this is the least they need to show by the end of the degree; with staff, ask where the course teaches and assesses it. Ask: 'Where in your course have you seen language tied to global movement or environmental debate?' Do not read the list aloud or treat it as the level most students reach. Most students go well beyond it (para 4.2)."
- statement: qaa/linguistics-2023/4.6.b1
  forPractitioner: { text: "Give students practice in forming hypotheses and testing them.", rewrite: light, force: must, status: drafted }
  forBeneficiary: { text: "You will have the chance to practise forming hypotheses and testing them, a skill employers value.", rewrite: full, force: must, status: drafted }
  author-agent-written: "Present this as generic skill 1 of 15 that the statement singles out as valuable to employers: a described opportunity with no modal, not a threshold condition of the award. It refines the honours level (fheq:6) in the strand:thinking strand (std:ref:uk-framework, R3). Cite it as QAA (2023) Linguistics Subject Benchmark Statement, para 4.6, bullet 1, and do not claim every graduate must show it at a set standard. Set it beside the threshold item qaa/linguistics-2023/4.5.b6 and the honours descriptor on framing questions (std:doc:qaa-fheq-2024-framework qaa/fheq-2024/4.15.b7)."
  author-agent-dialogue: "Raise it when a student describes their project to an employer. With a student, use plain words and 'you', and treat it as a skill the course gives them the chance to build; with staff, ask where modules give that chance and whether it is assessed. Ask: 'Can you give an example of a hunch you turned into a testable claim?' Avoid presenting it as a pass requirement."
- statement: qaa/linguistics-2023/4.6.b2
  forPractitioner: { text: "Develop students' ability to weigh the merits of contrasting theories and explanations.", rewrite: light, force: must, status: drafted }
  forBeneficiary: { text: "You will build your ability to weigh up competing theories and explanations, which employers value.", rewrite: full, force: must, status: drafted }
  author-agent-written: "Present this as generic skill 2 of 15 that the statement singles out as valuable to employers: a described opportunity with no modal, not a threshold condition of the award. It refines the honours level (fheq:6) in the strand:thinking strand (std:ref:uk-framework, R3). Cite it as QAA (2023) Linguistics Subject Benchmark Statement, para 4.6, bullet 2, and do not claim every graduate must show it at a set standard. Set it beside qaa/linguistics-2023/4.5.b8 and qaa/linguistics-2023/4.6.b6 (close in wording; listed in Part E)."
  author-agent-dialogue: "Raise it when a student must choose between explanations in an essay. With a student, use plain words and 'you', and treat it as a skill the course gives them the chance to build; with staff, ask where modules give that chance and whether it is assessed. Ask: 'What makes one explanation stronger than the other here?' Avoid presenting it as a pass requirement."
- statement: qaa/linguistics-2023/4.6.b3
  forPractitioner: { text: "Give practice in spoken, non-verbal and graphic communication, choosing the format for the audience.", rewrite: light, force: must, status: drafted }
  forBeneficiary: { text: "You will practise communicating in speech, in other non-verbal ways and with visuals, choosing a format that suits your audience.", rewrite: full, force: must, status: drafted }
  author-agent-written: "Present this as generic skill 3 of 15 that the statement singles out as valuable to employers: a described opportunity with no modal, not a threshold condition of the award. It refines the honours level (fheq:6) in the strand:communication strand (std:ref:uk-framework, R3). Cite it as QAA (2023) Linguistics Subject Benchmark Statement, para 4.6, bullet 3, and do not claim every graduate must show it at a set standard. Set it beside qaa/linguistics-2023/4.5.b9, the honours descriptor on communication (std:doc:qaa-fheq-2024-framework qaa/fheq-2024/4.15.b8) and Annex D's transferable strand (qaa/fheq-2024/annex-d/transferable/r1/3rd)."
  author-agent-dialogue: "Raise it when a student prepares a presentation or poster. With a student, use plain words and 'you', and treat it as a skill the course gives them the chance to build; with staff, ask where modules give that chance and whether it is assessed. Ask: 'Who is your audience, and why did you choose this format for them?' Avoid presenting it as a pass requirement."
- statement: qaa/linguistics-2023/4.6.b4
  forPractitioner: { text: "Build experimental design and the design and conduct of research projects, both individual and group, into the course.", rewrite: light, force: must, status: drafted }
  forBeneficiary: { text: "You will learn to design experiments and to plan and carry out research projects, on your own and with others.", rewrite: full, force: must, status: drafted }
  author-agent-written: "Present this as generic skill 4 of 15 that the statement singles out as valuable to employers: a described opportunity with no modal, not a threshold condition of the award. It refines the honours level (fheq:6) in the strand:application strand (std:ref:uk-framework, R3). Cite it as QAA (2023) Linguistics Subject Benchmark Statement, para 4.6, bullet 4, and do not claim every graduate must show it at a set standard. Set it beside qaa/linguistics-2023/4.5.b4, the honours descriptor on applying methods (std:doc:qaa-fheq-2024-framework qaa/fheq-2024/4.15.b6) and Annex D on group work (qaa/fheq-2024/annex-d/transferable/r2/3rd)."
  author-agent-dialogue: "Raise it when a student plans a group or individual project. With a student, use plain words and 'you', and treat it as a skill the course gives them the chance to build; with staff, ask where modules give that chance and whether it is assessed. Ask: 'What part of the design did you shape yourself, and what did the group decide together?' Avoid presenting it as a pass requirement."
- statement: qaa/linguistics-2023/4.6.b5
  forPractitioner: { text: "Teach the proper and ethical use of evidence and data, including in students' own research.", rewrite: light, force: must, status: drafted }
  forBeneficiary: { text: "You will come to understand how to use evidence and data properly and ethically.", rewrite: full, force: must, status: drafted }
  author-agent-written: "Present this as generic skill 5 of 15 that the statement singles out as valuable to employers: a described opportunity with no modal, not a threshold condition of the award. It refines the honours level (fheq:6) in the strand:application strand (std:ref:uk-framework, R3). Cite it as QAA (2023) Linguistics Subject Benchmark Statement, para 4.6, bullet 5, and do not claim every graduate must show it at a set standard. Set it beside qaa/linguistics-2023/4.6.b14 and the honours descriptor on decisions in complex contexts (std:doc:qaa-fheq-2024-framework qaa/fheq-2024/4.15.b9.2)."
  author-agent-dialogue: "Raise it when a student collects data from people or handles sensitive material. With a student, use plain words and 'you', and treat it as a skill the course gives them the chance to build; with staff, ask where modules give that chance and whether it is assessed. Ask: 'What consent and care does this data need, and how will you store and cite it?' Avoid presenting it as a pass requirement."
- statement: qaa/linguistics-2023/4.6.b6
  forPractitioner: { text: "Develop students' judgement of contrasting theories, explanations and the evidence behind them.", rewrite: light, force: must, status: drafted }
  forBeneficiary: { text: "You will build your ability to judge competing theories and explanations, and the evidence behind each.", rewrite: full, force: must, status: drafted }
  author-agent-written: "Present this as generic skill 6 of 15 that the statement singles out as valuable to employers: a described opportunity with no modal, not a threshold condition of the award. It refines the honours level (fheq:6) in the strand:thinking strand (std:ref:uk-framework, R3). Cite it as QAA (2023) Linguistics Subject Benchmark Statement, para 4.6, bullet 6, and do not claim every graduate must show it at a set standard. Set it beside qaa/linguistics-2023/4.6.b2 (close in wording; Part E), qaa/linguistics-2023/4.5.b7 and the honours descriptor on critical evaluation (std:doc:qaa-fheq-2024-framework qaa/fheq-2024/4.15.b7)."
  author-agent-dialogue: "Raise it when a student reviews literature with conflicting findings. With a student, use plain words and 'you', and treat it as a skill the course gives them the chance to build; with staff, ask where modules give that chance and whether it is assessed. Ask: 'Which evidence would change your mind about this theory?' Avoid presenting it as a pass requirement."
- statement: qaa/linguistics-2023/4.6.b7
  forPractitioner: { text: "Help students separate descriptive frameworks from the data they describe.", rewrite: light, force: must, status: drafted }
  forBeneficiary: { text: "You will learn to tell the difference between a system for describing language and the language data itself.", rewrite: full, force: must, status: drafted }
  author-agent-written: "Present this as generic skill 7 of 15 that the statement singles out as valuable to employers: a described opportunity with no modal, not a threshold condition of the award. It refines the honours level (fheq:6) in the strand:thinking strand (std:ref:uk-framework, R3). Cite it as QAA (2023) Linguistics Subject Benchmark Statement, para 4.6, bullet 7, and do not claim every graduate must show it at a set standard. Set it beside qaa/linguistics-2023/4.4 and the honours descriptor on arguing with established ideas (std:doc:qaa-fheq-2024-framework qaa/fheq-2024/4.15.b3.1)."
  author-agent-dialogue: "Raise it when a student confuses a category label with what speakers actually do. With a student, use plain words and 'you', and treat it as a skill the course gives them the chance to build; with staff, ask where modules give that chance and whether it is assessed. Ask: 'Is that a fact about the data or about the way we chose to describe it?' Avoid presenting it as a pass requirement."
- statement: qaa/linguistics-2023/4.6.b8
  forPractitioner: { text: "Give students practice in abstracting and synthesising information and in collecting, analysing and manipulating varied data.", rewrite: light, force: must, status: drafted }
  forBeneficiary: { text: "You will practise drawing out and combining information and gathering, analysing and working with many kinds of data.", rewrite: full, force: must, status: drafted }
  author-agent-written: "Present this as generic skill 8 of 15 that the statement singles out as valuable to employers: a described opportunity with no modal, not a threshold condition of the award. It refines the honours level (fheq:6) in the strand:application strand (std:ref:uk-framework, R3). Cite it as QAA (2023) Linguistics Subject Benchmark Statement, para 4.6, bullet 8, and do not claim every graduate must show it at a set standard. Set it beside qaa/linguistics-2023/4.5.b4, qaa/linguistics-2023/1.28 and Annex D's practical strand (qaa/fheq-2024/annex-d/practical/r4/3rd)."
  author-agent-dialogue: "Raise it when a student describes data work to an employer. With a student, use plain words and 'you', and treat it as a skill the course gives them the chance to build; with staff, ask where modules give that chance and whether it is assessed. Ask: 'What kinds of data have you handled, and what did you do with each?' Avoid presenting it as a pass requirement."
- statement: qaa/linguistics-2023/4.6.b9
  forPractitioner: { text: "Build students' skill in interpreting diagrams, tables and graphs.", rewrite: light, force: must, status: drafted }
  forBeneficiary: { text: "You will build your skill in reading and making sense of diagrams, tables and graphs.", rewrite: full, force: must, status: drafted }
  author-agent-written: "Present this as generic skill 9 of 15 that the statement singles out as valuable to employers: a described opportunity with no modal, not a threshold condition of the award. It refines the honours level (fheq:6) in the strand:thinking strand (std:ref:uk-framework, R3). Cite it as QAA (2023) Linguistics Subject Benchmark Statement, para 4.6, bullet 9, and do not claim every graduate must show it at a set standard. Set it beside qaa/linguistics-2023/4.5.b9 and Annex D's transferable strand on numeracy (qaa/fheq-2024/annex-d/transferable/r1/3rd)."
  author-agent-dialogue: "Raise it when a student meets quantitative results in a paper. With a student, use plain words and 'you', and treat it as a skill the course gives them the chance to build; with staff, ask where modules give that chance and whether it is assessed. Ask: 'What does this graph show, and what does it leave out?' Avoid presenting it as a pass requirement."
- statement: qaa/linguistics-2023/4.6.b10
  forPractitioner: { text: "Teach students to search for and synthesise information in many formats and to acknowledge and list their sources properly.", rewrite: light, force: must, status: drafted }
  forBeneficiary: { text: "You will learn to find and combine information from many kinds of source and to credit and list your sources properly.", rewrite: full, force: must, status: drafted }
  author-agent-written: "Present this as generic skill 10 of 15 that the statement singles out as valuable to employers: a described opportunity with no modal, not a threshold condition of the award. It refines the honours level (fheq:6) in the strand:application strand (std:ref:uk-framework, R3). Cite it as QAA (2023) Linguistics Subject Benchmark Statement, para 4.6, bullet 10, and do not claim every graduate must show it at a set standard. Set it beside the honours descriptor on managing learning from scholarly and primary sources (std:doc:qaa-fheq-2024-framework qaa/fheq-2024/4.15.b5)."
  author-agent-dialogue: "Raise it when a student starts a literature search or asks about referencing. With a student, use plain words and 'you', and treat it as a skill the course gives them the chance to build; with staff, ask where modules give that chance and whether it is assessed. Ask: 'Where did you look, and how will a reader find each source you used?' Avoid presenting it as a pass requirement."
- statement: qaa/linguistics-2023/4.6.b11
  forPractitioner: { text: "Develop students' capacity for competent self-directed study.", rewrite: light, force: must, status: drafted }
  forBeneficiary: { text: "You will build your ability to study and learn well on your own.", rewrite: full, force: must, status: drafted }
  author-agent-written: "Present this as generic skill 11 of 15 that the statement singles out as valuable to employers: a described opportunity with no modal, not a threshold condition of the award. It refines the honours level (fheq:6) in the strand:autonomy strand (std:ref:uk-framework, R3). Cite it as QAA (2023) Linguistics Subject Benchmark Statement, para 4.6, bullet 11, and do not claim every graduate must show it at a set standard. Set it beside the honours descriptors on managing own learning (std:doc:qaa-fheq-2024-framework qaa/fheq-2024/4.15.b5, 4.15.b9.3) and Annex D (qaa/fheq-2024/annex-d/transferable/r3/3rd)."
  author-agent-dialogue: "Raise it when a student struggles to plan independent study. With a student, use plain words and 'you', and treat it as a skill the course gives them the chance to build; with staff, ask where modules give that chance and whether it is assessed. Ask: 'How do you decide what to study next when no one sets it?' Avoid presenting it as a pass requirement."
- statement: qaa/linguistics-2023/4.6.b12
  forPractitioner: { text: "Make sure students learn why health and safety and equality, diversity and inclusiveness matter at work.", rewrite: light, force: must, status: drafted }
  forBeneficiary: { text: "You will come to understand why health and safety, and equality, diversity and inclusion, matter in a workplace.", rewrite: full, force: must, status: drafted }
  author-agent-written: "Present this as generic skill 12 of 15 that the statement singles out as valuable to employers: a described opportunity with no modal, not a threshold condition of the award. It refines the honours level (fheq:6) in the strand:autonomy strand (std:ref:uk-framework, R3). Cite it as QAA (2023) Linguistics Subject Benchmark Statement, para 4.6, bullet 12, and do not claim every graduate must show it at a set standard. Set it beside the EDI paragraphs (qaa/linguistics-2023/1.7 to 1.11) and the honours descriptor on personal responsibility (std:doc:qaa-fheq-2024-framework qaa/fheq-2024/4.15.b9.1)."
  author-agent-dialogue: "Raise it when a student prepares for a placement, lab work or fieldwork. With a student, use plain words and 'you', and treat it as a skill the course gives them the chance to build; with staff, ask where modules give that chance and whether it is assessed. Ask: 'What risks and inclusion questions does this setting raise for you and others?' Avoid presenting it as a pass requirement."
- statement: qaa/linguistics-2023/4.6.b13
  forPractitioner: { text: "Give students room to engage with live debates on sustainability, employability and global outlooks, decolonisation and anti-racism among them.", rewrite: light, force: must, status: drafted }
  forBeneficiary: { text: "You will have the chance to take part in current debates about sustainability, careers and global perspectives, including decolonisation and anti-racism.", rewrite: full, force: must, status: drafted }
  author-agent-written: "Present this as generic skill 13 of 15 that the statement singles out as valuable to employers: a described opportunity with no modal, not a threshold condition of the award. It refines the honours level (fheq:6) in the strand:thinking strand (std:ref:uk-framework, R3). Cite it as QAA (2023) Linguistics Subject Benchmark Statement, para 4.6, bullet 13, and do not claim every graduate must show it at a set standard. Set it beside qaa/linguistics-2023/4.5.b15, the sustainability paragraphs (qaa/linguistics-2023/1.17 to 1.21) and std:doc:qaa-advancehe-esd-2021-guidance."
  author-agent-dialogue: "Raise it when a student or team discusses decolonising the curriculum or sustainability. With a student, use plain words and 'you', and treat it as a skill the course gives them the chance to build; with staff, ask where modules give that chance and whether it is assessed. Ask: 'Which current debate does your own linguistics work speak to?' Avoid presenting it as a pass requirement."
- statement: qaa/linguistics-2023/4.6.b14
  forPractitioner: { text: "Help students see why sustainable action and ethical conduct matter, and give them chances to practise both.", rewrite: light, force: must, status: drafted }
  forBeneficiary: { text: "You will come to see why acting sustainably and behaving ethically matter, and practise both.", rewrite: full, force: must, status: drafted }
  author-agent-written: "Present this as generic skill 14 of 15 that the statement singles out as valuable to employers: a described opportunity with no modal, not a threshold condition of the award. It refines the honours level (fheq:6) in the strand:autonomy strand (std:ref:uk-framework, R3). Cite it as QAA (2023) Linguistics Subject Benchmark Statement, para 4.6, bullet 14, and do not claim every graduate must show it at a set standard. Set it beside qaa/linguistics-2023/4.6.b5 and the honours descriptor on personal responsibility (std:doc:qaa-fheq-2024-framework qaa/fheq-2024/4.15.b9.1)."
  author-agent-dialogue: "Raise it when a student plans fieldwork, data use or a placement. With a student, use plain words and 'you', and treat it as a skill the course gives them the chance to build; with staff, ask where modules give that chance and whether it is assessed. Ask: 'What would acting sustainably and ethically look like in this project?' Avoid presenting it as a pass requirement."
- statement: qaa/linguistics-2023/4.6.b15
  forPractitioner: { text: "Give students practice in communicating subject knowledge with authority and sensitivity to policy stakeholders for whom language is central.", rewrite: light, force: must, status: drafted }
  forBeneficiary: { text: "You will practise explaining what you know about language, clearly and sensitively, to people who make policies where language matters.", rewrite: full, force: must, status: drafted }
  author-agent-written: "Present this as generic skill 15 of 15 that the statement singles out as valuable to employers: a described opportunity with no modal, not a threshold condition of the award. It refines the honours level (fheq:6) in the strand:communication strand (std:ref:uk-framework, R3). Cite it as QAA (2023) Linguistics Subject Benchmark Statement, para 4.6, bullet 15, and do not claim every graduate must show it at a set standard. Set it beside qaa/linguistics-2023/4.5.b10, the language planning and policy field in para 3.4 and the honours descriptor on communication (std:doc:qaa-fheq-2024-framework qaa/fheq-2024/4.15.b8)."
  author-agent-dialogue: "Raise it when a student works on language policy, education or public engagement. With a student, use plain words and 'you', and treat it as a skill the course gives them the chance to build; with staff, ask where modules give that chance and whether it is assessed. Ask: 'How would you explain this finding to someone writing a language policy?' Avoid presenting it as a pass requirement."
```

### S5 Levels and alignment
<!-- label: both; status: drafted; basis: primary -->
```yaml
levels:
  - { id: "fheq:6", role: "cites", locator: "D1, 2.5; 4.2" }
  - { id: "fqheis:10", role: "cites", locator: "D1, 2.5; 4.2" }
  - { id: "cqfw:6", role: "inferred", locator: "std:doc:qaa-fheq-2024-framework 2.24 (CQFW levels 4 to 8 compare with the FHEQ); the statement names Wales but not the CQFW" }
  - { id: "spine:6", role: "inferred", locator: "std:ref:uk-framework R2 (step 6: FHEQ 6, SCQF 10 for honours)" }
crosswalks:
  - { from: "fheq:6", to: "fqheis:10", relation: "equivalent", basis: "stated (D1, 2.5: \"(FHEQ Level 6; FQHEIS Level 10)\"; 4.2)" }
  - { from: "fheq:6", to: "cqfw:6", relation: "compares-with", basis: "inferred from std:doc:qaa-fheq-2024-framework 2.24 (Part E)" }
  - { from: "fheq:6", to: "spine:6", relation: "equivalent", basis: "inferred from std:ref:uk-framework R2 (Part E)" }
```

### S6 Themes
<!-- label: both; status: drafted; basis: primary -->
```yaml
- { id: "theme:edi", role: "carries", carriedIn: ["1.7", "1.8", "1.9", "1.10", "1.11", "2.13", "3.7", "3.11", "4.6"] }
- { id: "theme:accessibility", role: "carries", carriedIn: ["1.12", "1.13", "1.14", "1.15", "1.16", "2.11", "2.12"] }
- { id: "theme:esd", role: "carries", carriedIn: ["1.17", "1.18", "1.19", "1.20", "1.21", "3.11", "4.5", "4.6"] }
- { id: "theme:enterprise", role: "carries", carriedIn: ["1.22", "1.23", "1.24", "1.25", "1.26", "1.27", "1.28", "1.29", "1.30", "1.31", "4.6"] }
```

### S7 Relations
<!-- label: both; status: drafted; basis: primary -->
```yaml
- { rel: "partOf", target: "collection: QAA Subject Benchmark Statements", note: "one of 54 held by stan" }
- { rel: "supersedes", target: "std:doc:qaa-linguistics-2019-benchmarks (not yet ingested)", note: "front matter names key changes from the previous statement; the back matter dates the fourth edition 2019" }
- { rel: "refersTo", target: "std:doc:qaa-fheq-2024-framework, Annex D", note: "the degree outcome classification descriptions for FHEQ Level 6 and FQHEIS Level 10 (4.2); above-threshold performance is left to it" }
- { rel: "refersTo", target: "std:doc:qaa-fheq-2024-framework", note: "FHEQ Level 6 (2.5; 4.2)" }
- { rel: "refersTo", target: "std:doc:qaa-fqheis-2024-framework", note: "FQHEIS Level 10 (2.5; 4.2)" }
- { rel: "cites", target: "std:doc:qaa-enterprise-2018-guidance", note: "cited as QAA 2018 (1.25) and in the reference list" }
- { rel: "cites", target: "std:doc:qaa-advancehe-esd-2021-guidance", note: "in the reference list only" }
- { rel: "refersTo", target: "QAA UK Quality Code for Higher Education (2019), Advice and Guidance (not yet ingested)", note: "front matter; reference list" }
- { rel: "refersTo", target: "QAA's Glossary (not ingested)", note: "front matter: explains unfamiliar terms" }
- { rel: "cites", target: "UNESCO Sustainable Development Goals (not a standards document; not ingested)", note: "1.19; 3.11 (the UN SDGs); reference list" }
- { rel: "readWith", target: "the 16 Subject Benchmark Statements in Appendix 2 (anthropology to Welsh), each std:doc:qaa-<subject>-<year>-benchmarks", note: "Appendix 2: related statements" }
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
- The study of the human capacity for language in every mode, spoken, signed and written: its structure, its processing in the mind and brain, and how it is acquired, used, interpreted and changes in social, cultural and historical settings (D1, 1.2).
- Its guiding principle is that linguistic behaviour can be explained by systematic study, with theoretical models tested against empirical data, by both cognitive and social approaches (D1, 1.3).
- Broad and interdisciplinary, spanning the sciences, social sciences and humanities; the statement keeps the subject's boundaries deliberately open and evolving (D1, 1.3, 1.4, 1.6).
- Taught through levels of analysis (phonetics, phonology, morphology, syntax, semantics, pragmatics) applied to domains of language use and to applied fields such as clinical, computational and forensic linguistics, language teaching and lexicography (D1, 3.1 to 3.4).
- Reflexive and socially engaged: students examine their own linguistic identities and attitudes, and the subject studies language, power and social hierarchy and works in partnership with communities (D1, 1.8, 1.9).
- Commonly studied in combination, with English, TESOL, other languages, psychology, philosophy, politics and many more; single honours covers most of the content, joint routes a selection (D1, 1.5, 2.3, 2.7).

### SB2 Themes in this subject
<!-- label: both; status: drafted; basis: primary -->
```yaml
- theme: theme:edi
  inThisSubject: "EDI sits inside the subject knowledge itself: comparative study of unrelated, often non-European languages, attention to vernaculars, minority languages and representation, reflexivity about one's own language attitudes, and research done with communities; assessment linked to real-life EDI issues (D1, 1.7 to 1.11); threshold items on ideology, power and minority groups and a generic skill on EDI at work (D1, 4.5, 4.6)"
  statements: ["qaa/linguistics-2023/4.5.b11", "qaa/linguistics-2023/4.5.b12", "qaa/linguistics-2023/4.6.b12"]
- theme: theme:accessibility
  inThisSubject: "an inclusive view of all modes of language, sign included; accessible formats and reasonable adjustments; multilingual home backgrounds as a resource; provider awareness of disabled students' needs and accessible digital content (D1, 1.12 to 1.16); resourcing accessible delivery and uneven access to technology (D1, 2.11, 2.12)"
  statements: ["qaa/linguistics-2023/1.13", "qaa/linguistics-2023/2.12"]
- theme: theme:esd
  inThisSubject: "headed Sustainability: language as central to articulating sustainable futures; links to UNESCO's goals SDG4, SDG5, SDG8 and SDG16; discourse analysis of climate communication; endangered-language and documentation work opening space for other knowledges (D1, 1.17 to 1.21); SDG themes in assessment (D1, 3.11); a threshold item and two generic skills (D1, 4.5, 4.6)"
  statements: ["qaa/linguistics-2023/1.19.b4", "qaa/linguistics-2023/4.5.b15", "qaa/linguistics-2023/4.6.b13", "qaa/linguistics-2023/4.6.b14"]
- theme: theme:enterprise
  inThisSubject: "enterprise and entrepreneurship education for careers and wider social value, placements and external links; the subject's critical, creative and analytical mix; IT and data skills; graduates sought in publishing, technology, AI, teaching, therapy, data science and more (D1, 1.22 to 1.31); employability among the debates in the generic skills (D1, 4.6)"
  statements: ["qaa/linguistics-2023/1.26", "qaa/linguistics-2023/4.6.b13"]
```

### SB3 Content and delivery
<!-- label: both; status: drafted; basis: primary -->
```yaml
areas:
  - { component: "3.1", gloss: "introductory study across the core levels of linguistic analysis" }
  - { component: "3.2", gloss: "levels of analysis: phonetics, phonology, morphology, syntax, semantics, pragmatics" }
  - { component: "3.3", gloss: "domains of language use and development: acquisition, historical, evolutionary, typological, socio-, psycho- and neurolinguistics, history and philosophy of language, corpus, discourse, stylistics, educational linguistics" }
  - { component: "3.4", gloss: "applied fields: applied, clinical, computational and forensic linguistics; translation and interpreting; language teaching and TESOL; language planning and policy; lexicography" }
practices:
  - { component: "3.5", kind: "teaching", gloss: "methods aligned to aims and to the stage of progression" }
  - { component: "3.6", kind: "teaching", gloss: "lectures, seminars, practicals and lab work, research-methods workshops, tutorials, group study, projects, data exercises, specialist software, placements, VLEs" }
  - { component: "3.7", kind: "learning", gloss: "inclusive learning environment, belonging and engagement" }
  - { component: "3.8", kind: "assessment", gloss: "assessment aligned to aims and stage; formative and summative" }
  - { component: "3.9", kind: "assessment", gloss: "what assessment should be able to evaluate, from analysis of linguistic systems to applying language-learning principles" }
  - { component: "3.10", kind: "assessment", gloss: "essays, projects, examinations, presentations, problem sets, data work, materials design, lab work, portfolios, reviews, online resources, peer and self-evaluation, skills tasks" }
  - { component: "3.11", kind: "assessment", gloss: "balancing knowledge and skills; inclusivity and the SDGs in assessment themes" }
  - { component: "3.12", kind: "assessment", gloss: "clear rationale and explicit criteria" }
  - { component: "3.13", kind: "assessment", gloss: "formative and diagnostic feedback throughout" }
```

### SB4 Benchmark standards
<!-- label: both; status: drafted; basis: primary -->
```yaml
rungs:
  - { rung: "threshold", leadIn: "4.5", award: "bachelor's with honours", items: 15 }
rungBases: "threshold only: 4.5 defines the threshold as the minimally acceptable attainment of an honours graduate; 4.2 says most students do much better and refers providers to Annex D (std:doc:qaa-fheq-2024-framework) for the classes above it. No typical or excellent rung."
outcomeLists:
  - { leadIn: "4.6", gloss: "generic skills of value to employers (an opportunity to develop, no modal)", items: 15, award: ["honours"] }
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
- { body: "professional, statutory and regulatory bodies (PSRBs), none named", says: "the statement supports PSRBs on the academic standards expected of students; providers may weigh PSRB requirements; courses with professional or vocational outcomes may need their evaluation and accreditation (D1, front matter, 2.22)", requirements: "not-applicable: no body named" }
- { body: "Office for Students", says: "in England the statement is not a sector-recognised standard under the OfS regulatory framework (D1, front matter)", requirements: "not yet ingested (Part E)" }
```

### SB6 Cross-cutting references
<!-- label: both; status: drafted; basis: primary -->
```yaml
themes:
  - { id: "theme:edi", named: "Equality, diversity and inclusion", carriedIn: ["1.7", "1.8", "1.9", "1.10", "1.11", "2.13", "3.7", "3.11", "4.6"], statements: ["4.5.b11", "4.5.b12", "4.6.b12"] }
  - { id: "theme:accessibility", named: "Accessibility (front matter: accessibility and the needs of disabled students)", carriedIn: ["1.12", "1.13", "1.14", "1.15", "1.16", "2.11", "2.12"], statements: ["1.13", "2.12"] }
  - { id: "theme:esd", named: "Sustainability (front matter: education for sustainable development)", carriedIn: ["1.17", "1.18", "1.19", "1.20", "1.21", "3.11", "4.5", "4.6"], statements: ["1.19.b4", "4.5.b15", "4.6.b13", "4.6.b14"] }
  - { id: "theme:enterprise", named: "Enterprise and entrepreneurship education (front matter: employability, entrepreneurship and enterprise education)", carriedIn: ["1.22", "1.23", "1.24", "1.25", "1.26", "1.27", "1.28", "1.29", "1.30", "1.31", "4.6"], statements: ["1.26", "4.6.b13"] }
frameworks:
  - { framework: "fheq", levels: ["fheq:6"], citedIn: ["2.5", "4.2"] }
  - { framework: "scqf", levels: ["fqheis:10"], citedIn: ["2.5", "4.2"] }
bodies:
  - { body: "professional, statutory and regulatory bodies (PSRBs), generic", citedIn: ["front matter", "2.22"] }
  - { body: "Office for Students", citedIn: ["front matter"] }
sharedDocuments:
  - { document: "std:doc:qaa-fheq-2024-framework, Annex D", named: "Annex D: Outcome classification descriptions for FHEQ Level 6 and FQHEIS Level 10 degrees", citedIn: ["4.2"], role: "descriptions of the four honours classes (1st, 2.1, 2.2, 3rd); the only account of achievement above the threshold" }
  - { document: "std:doc:qaa-enterprise-2018-guidance", named: "QAA 2018 (Enterprise and Entrepreneurship Education: Guidance for UK Higher Education Providers)", citedIn: ["1.25", "back matter"], role: "source of the enterprise capabilities listed in 1.25" }
  - { document: "std:doc:qaa-advancehe-esd-2021-guidance", named: "QAA and Advance HE (2021) Education for Sustainable Development Guidance", citedIn: ["back matter"], role: "further reading for the sustainability theme" }
  - { document: "QAA UK Quality Code for Higher Education and its Advice and Guidance (not yet ingested: Part E)", named: "The UK Quality Code for Higher Education; Advice and Guidance", citedIn: ["front matter", "back matter"], role: "course design, teaching, external expertise, monitoring" }
  - { document: "QAA Glossary (not ingested: Part E)", named: "QAA's Glossary", citedIn: ["front matter"], role: "explains unfamiliar terms" }
  - { document: "UNESCO Sustainable Development Goals (not a QAA document; not ingested)", named: "UNESCO's education for sustainable development goals; United Nations Sustainable Development Goals", citedIn: ["1.19", "3.11", "back matter"], role: "frames the sustainability theme (SDG4, SDG5, SDG8, SDG16 in 1.19; five goals named in 3.11)" }
```

## Part B Terminology
<!-- The statement has no glossary of its own unless Part E says so; these are terms it defines in its text. -->

### B1 Concepts
<!-- label: both; status: drafted; basis: primary -->
```yaml
- { slug: "threshold-standard", definition: "the least level of attainment acceptable for an honours graduate in the subject (D1, 4.5)", beneficiaryDefinition: "the minimum you need to reach to gain your honours degree", scopeNote: "the only rung this statement gives", category: "unknown", practices: ["education"] }
- { slug: "levels-of-linguistic-analysis", definition: "the tiers at which language is analysed, from speech sounds through word structure and sentence structure to meaning and use in context (D1, 3.1, 3.2)", beneficiaryDefinition: "the layers at which you study language, from sounds up to meaning and use", scopeNote: "phonetics, phonology, morphology, syntax, semantics, pragmatics", category: "unknown", practices: ["education"] }
- { slug: "applied-linguistics", definition: "study of practical, real-world problems that involve language, drawing on linguistics and neighbouring disciplines and working with those affected (D1, 3.4)", beneficiaryDefinition: "using linguistics to help solve real problems involving language", scopeNote: "one of the two areas the statement covers (1.1)", category: "unknown", practices: ["education"] }
- { slug: "psrb", definition: "a professional, statutory or regulatory body (D1, front matter)", beneficiaryDefinition: "an organisation that sets or checks standards for a profession", scopeNote: "none is named in this statement", category: "unknown", practices: ["education"] }
```

### B2a Terms as the issuer defines them
<!-- label: source; status: drafted; basis: primary -->
```yaml
- { concept: "threshold-standard", form: "threshold standard", lang: "en", partOfSpeech: "noun-phrase", termStatus: "preferred", register: "formal" }
- { concept: "threshold-standard", form: "minimum threshold standards", lang: "en", partOfSpeech: "noun-phrase", termStatus: "admitted", register: "formal" }
- { concept: "levels-of-linguistic-analysis", form: "levels of linguistic analysis", lang: "en", partOfSpeech: "noun-phrase", termStatus: "preferred", register: "formal" }
- { concept: "applied-linguistics", form: "Applied linguistics", lang: "en", partOfSpeech: "noun-phrase", termStatus: "preferred", register: "formal" }
- { concept: "psrb", form: "professional, statutory and regulatory bodies (PSRBs)", lang: "en", partOfSpeech: "noun-phrase", termStatus: "preferred", register: "formal" }
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
  title: "Subject Benchmark Statement Linguistics"
  edition: "September 2023"
  year: 2023
  url: unknown (the QAA page; the text came by stan's extraction)
  retrieved: "held from stan: wkspc2615-QAAVector mapped/linguistics-2023/linguistics-2023.raw.txt, commit 366bcb99a01118f2c4c3ebfa2a8337596bddc455; received 2026-10-03"
  licence: QAA copyright
  tier: primary
  readVia: direct
  held: b82ce2a87934ac152025726dded4e685281df4a1d9a9a3c0009e4b463f542828
  heldFiles: ["wkspc2601-library/txt/qaa-2023-linguistics-subject-benchmark-statement-standard.txt", "wkspc2601-library/txt/qaa-2023-linguistics-subject-benchmark-statement-standard.norm.txt", "wkspc2601-library/records/qaa-2023-linguistics-subject-benchmark-statement-standard.chunks.json", "wkspc2601-library/records/qaa-2023-linguistics-subject-benchmark-statement-standard.held.json"]
  citedIn: [S1, S2, S3, S4, S4a, S5, S6, S7, SB1, SB2, SB3, SB4, SB5, SB6]
```

### D2 Research log
```yaml
- { ref: D1, tier: primary, consulted: 2026-10-03, pass: P1, outcome: "read whole, direct, from the normalised text; skeleton by tools/std_prep.py, document by tools/bm_build.py" }
- { ref: "ADAPT subj HESA stores, cah.json and hecos.json (designs/ingest/standards/subj/vocab)", tier: primary, consulted: 2026-10-03, pass: P1, outcome: "codes for statedSubjects and subjects" }
```

### D3 Wanted sources
```yaml
- { w: "W-std-0078", source: "QAA Subject Benchmark Statement Linguistics, 2019 (fourth edition)", why: "to confirm the supersedes link and compare the standards" }
- { w: "W-std-0052", source: "QAA UK Quality Code for Higher Education (2019) and Advice and Guidance", why: "cited in the front matter and reference list; not yet ingested" }
```

## Part E Gaps and questions
- Rungs: threshold only (4.5, 15 items). No typical or excellent rung; 4.2 says most students exceed the threshold and refers providers to Annex D (as Archaeology, run 0085). Pattern differs from Psychology.
- Threshold lead-in wording: "students should be able to acquire a range of subject-specific and generic skills including:" (4.5). Force recorded as threshold because 4.5 defines the rung as the minimally acceptable attainment; the lead-in modal is "should be able to", not Psychology's "will". For P3.
- The threshold lead-in names both subject-specific and generic skills, but its fifteen items are mostly subject-specific; the separate generic skills list (4.6) has no rung and no modal ("offer students the opportunity to develop"). Recorded as an outcome list with force describes, rung none, domain generic-skill, level fheq:6. P3: whether 4.6 should count as part of the threshold through 4.5's "generic skills".
- 4.6.b2 ("assessing the merits of contrasting theories and explanations") and 4.6.b6 ("evaluating the merits of contrasting theories, explanations and evidence") nearly repeat each other; both kept as the issuer gives them.
- Skeleton correction: 4.5.b9 ran only to the page break ("tree diagrams,"); recut with find to include its continuation after the page number, so its source holds the stray page number "18".
- Skeleton correction: the theme hits were one paragraph early, because each sub-heading line falls at the end of the paragraph before it (for example "Equality, diversity and inclusion" sits in 1.6). Themes placed by sub-heading: EDI 1.7 to 1.11, accessibility 1.12 to 1.16, sustainability 1.17 to 1.21, enterprise 1.22 to 1.31; and 4.5 and 4.6 placed under their own sub-headings.
- Skeleton candidates not taken as statements: 1.18.b1 and b2 and 1.19.b1 to b3 (descriptive principles and SDG links); 3.2, 3.3, 3.6, 3.9 and 3.10 list items (content areas, teaching and assessment methods: components, not standards).
- Obliging words outside the five: 1.13 "are normally expected to" (describes); 4.4 "is expected to" (describes); 2.9 "will increasingly be necessary" and "will need to" (a forecast; describes); 2.12 "requires" and "needs to be recognised" (recorded as must). For Abbott.
- 4.3 "will be expected to" recorded as will; it frames the threshold list and is not itself a rung item (rung none).
- Plain-present provider norms, not recorded as statements (template open point 5): 1.16 (providers aware of accessibility needs; accessible formats); 2.3 (honours courses have an introductory module); 2.10 (institutions provide entry information); 2.13 (institutions ensure equal access to partnerships); 3.5, 3.6 (documentation at the outset), 3.7, 3.8, 3.12 and 3.13 (assessment practice). For P3.
- Plain-present student outcomes not recorded: 1.24 ("students develop capabilities that make them ... able to"), 1.28 (IT and data skills gained), 2.6 (a second-class graduate is capable of postgraduate study). For P3.
- 2.21 (external examiners "will be asked", "will consider") read as a description of the external examining system, not a standard; 2.2 and 2.22 use "may" and are not statements.
- Inferred code: hecos 100971 phonetics and phonology (the text names phonetics and phonology separately, 3.2). The CAH parent of CAH19-01-07 is CAH19-01 English studies, not added. Other fields named (translation, lexicography, forensic, clinical, computational linguistics) are applied areas, not given codes.
- Inferred levels and crosswalks: cqfw:6 (from std:doc:qaa-fheq-2024-framework 2.24; the statement names Wales but not the CQFW) and spine:6 (std:ref:uk-framework R2). The FHEQ 6 to FQHEIS 10 equivalence is stated (2.5).
- Generic skills levels: each 4.6 item is set at fheq:6 as the honours level it refines; the statement gives no level per skill. Inferred.
- Series: the 2023 statement as the fifth edition is inferred from the back matter (fourth edition 2019; third 2015; earlier 2007 and 2002). Supersedes 2019 by the same reading.
- Bodies: none named as a PSRB. Bodies named only in the excluded membership lists (Linguistics Association of Great Britain, British Association for Applied Linguistics, British Council, Chartered College of Teaching, University Council for Modern Languages, International Clinical Phonetics and Linguistics Association) and UCAS (Appendix 1) are not recorded in SB5. Speech and Language Therapy is named as a profession (1.29, 3.4) with no regulator named.
- Office for Students: requirements not yet ingested.
- SB6 documents not ingested: the Quality Code and Advice and Guidance, QAA Glossary, UNESCO and UN SDGs.
- TH tags only statements inside a theme's own paragraphs (1.13, 1.19.b4, 1.26); SB6 also lists the threshold and generic items that name a theme (4.5.b11, 4.5.b12, 4.5.b15, 4.6.b12 to 4.6.b14). 4.5.b11 and 4.5.b12 under EDI are our reading (ideology, power, minority groups; the item does not use the theme name).
- Different from Psychology: no master's award; threshold only; a separate unmoded generic skills list; Appendix 1 (course titles) and Appendix 2 (related statements); the enterprise section is long (1.22 to 1.31) and includes graduate sectors.
- Agent instructions (aaw, aad) set each standard beside FHEQ 4.15 descriptor ids, Annex D threshold cells and std:ref:uk-framework spine and strand ids; the strand for each 4.6 skill is our assignment.
- ST-12: versions here run to the lengths the content needs; no length range is yet set.

---

## Change notes
- 0.1.2, 3 October 2026, 21:02: moved with its held text from UNI to the source library repo (`wkspc2601-library/ingested/standards/`, texts in `txt/`, records in `records/`); paths only (Abbott, 20:56; std N-0119).
- 0.1.1, 3 October 2026, 20:20: obliging words outside the five read as must, "ought to" as should, on statements outside the rungs, each marked on its force line (Abbott, 20:17; D-std-0016).
- 0.1.0, 2026-10-03 17:59: researched by run frame 0.1.1-draft and standards run layer 0.7.0-draft, std, run 0118 (P1); built by tools/bm_build.py.
