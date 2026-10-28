---
id: std:doc:qaa-librarianship-information-knowledge-records-and-archives-management-2025-benchmarks
title: "Subject Benchmark Statement: Librarianship, Information, Knowledge, Records and Archives Management"
profile: standards/subject-benchmark
profileVersion: 0.2.0-draft
issuer: QAA
kind: subject-benchmark
jurisdiction: [UK]
subjectScope: subjects
subjects:
  - { scheme: "hecos", code: "100913", label: "librarianship", basis: "stated" }
  - { scheme: "hecos", code: "100915", label: "archives and records management", basis: "stated" }
  - { scheme: "hecos", code: "100370", label: "information management", basis: "inferred" }
  - { scheme: "hecos", code: "100916", label: "information services", basis: "inferred" }
  - { scheme: "cah", code: "CAH24-01-01", label: "information services", basis: "inferred" }
edition: "Fifth edition, April 2025"
published: 2025-04
status: current
supersedes: "the previous Subject Benchmark Statement, named only as such in the front matter; the advisory group list names a 2019 minor update, a 2015 and a 2007 revision and the 2000 original (D1, section 6)"
heldText: { method: sha256-bytes, raw: 9fa2e745227bc8ee1d311cdf78b47df194361d9f4ccd0f2876f383aebe7ac875, normalised: ad4d38dba37429aaf63c575b9ee2b22f4dc93d19f89dce822b6afb9c05e03e8f }
heldTextStan: { method: sha256-stan, raw: 9fa2e745227bc8ee1d311cdf78b47df194361d9f4ccd0f2876f383aebe7ac875, normalised: d727ff303bc4b042608fbc181ae01b2b42325afda81c3d3aa2f13375c964d485 }
licence: "QAA copyright; held for study, private to the project, never published"
series: "QAA Subject Benchmark Statements, 2025 revisions with cross-cutting themes (fifth edition of this statement)"
awardsCovered: ["bachelor's with honours", "master's", "postgraduate diploma", "postgraduate certificate"]
levelsCovered: ["fheq:6", "fqheis:10", "fheq:7", "fqheis:11"]
nations: ["England", "Wales", "Scotland", "Northern Ireland"]
parts:
  S: full
  B: "partial: no glossary in the document (it points to QAA's Glossary); terms it defines in passing"
  C: "not-applicable: the document sets expectations, not a procedure"
pins: { structure: 0.13.0-draft, template: 0.8.0-draft, benchmarkTemplate: 0.6.0-draft, runFrame: 0.1.1-draft, runLayer: 0.7.0-draft, standards: none yet, terminology: none yet }
lifecycle: drafted
researchedBy: run frame 0.1.1-draft; standards run layer 0.7.0-draft; std, run 0117 (tools/bm_build.py)
passes:
  P1: "2026-10-03 17:45"
  P2: "skipped: read direct from the held text; inferred codes and rung links are for P3"
  P3: open
version: 0.1.2
---

<!-- from INGEST wpk-0016-ingest-pd-template-standards.md 0.8.0-draft and wpk-0016-ingest-pd-template-standards-benchmark.md 0.6.0-draft; built by tools/bm_build.py from run-src/ -->
# Subject Benchmark Statement: Librarianship, Information, Knowledge, Records and Archives Management (QAA, April 2025)

> Run 0117, P1 by std. The issuer's words are held in the source library, `wkspc2601-library/txt/qaa-2025-librarianship-information-knowledge-records-archives-management-standard.norm.txt`; each S4 record carries its statement in full (`source`) for language analysis, with its span. Paraphrases and versions are ours. Private to the project, never published. In front matter `status` is the issuer's; ours is `lifecycle`. Doubts are in Part E.

## Part 0 Summary

### 0.1 Agent definition
<!-- label: editorial; status: drafted; basis: primary -->
A reference record of the QAA statement for librarianship, information, knowledge, records and archives management, 2025. It holds the statement's standards as 101 records: honours threshold lists for subject skills and generic skills, master's threshold lists for the same, and the few obliging sentences elsewhere, each with its span, our paraphrase, a practitioner and a student version and two instructions for AI agents. Use it to write or check course outcomes in this field at FHEQ levels 6 and 7, never as a regulatory text.

### 0.2 Summary
<!-- label: both; status: drafted; basis: primary -->
The statement covers honours degrees, postgraduate certificates and diplomas and master's degrees in librarianship, information, knowledge, records and archives management, noting that the field is mostly studied at postgraduate level. It states one rung only, the threshold, twice: for honours (4.5 to 4.8, with 4.6 defining a third as some proficiency in most attributes) and for master's and other postgraduate awards (4.9 to 4.12); it names typical standards in 1.1 but lists none, and leaves classes above the threshold to Annex D (4.2). Its five cross-cutting themes are equality, diversity and inclusion; accessibility; education for sustainable development (with the UN goals); employability, enterprise and entrepreneurship; and generative AI. It names CILIP, the Archives and Records Association, IFLA, the Information and Records Management Society and the Equality and Human Rights Commission, and cites the FHEQ and FQHEIS levels in 2.4 and 2.7.

## Part S Standard

### S1 Identity
<!-- label: source; status: drafted; basis: primary -->
```yaml
issuer: The Quality Assurance Agency for Higher Education
title: "Subject Benchmark Statement: Librarianship, Information, Knowledge, Records and Archives Management"
edition: "Fifth edition, April 2025"
dates:
  published: 2025-04
  other: []
kind: subject-benchmark
jurisdiction: [UK]
authority: "reference: a sector-owned reference point, not a regulatory requirement; not a sector-recognised standard in England, part of quality arrangements in Scotland, Wales and Northern Ireland (D1, front matter)"
licence: "QAA copyright; the document gives no re-use terms in its text (D1, front matter)"
copyrightNotice: { text: "© The Quality Assurance Agency for Higher Education 2025", locator: "D1, index" }
```

### S2 Purpose and scope
<!-- label: source; status: drafted; basis: primary -->
```yaml
governs: "what graduates in librarianship, information, knowledge, records and archives management know, understand and can do at the end of honours and postgraduate study, and the nature of courses in the field"
appliesTo:
  awards: ["bachelor's with honours", "master's", "postgraduate diploma", "postgraduate certificate"]
  levels: ["fheq:6", "fqheis:10", "fheq:7", "fqheis:11"]
  providers: ["UK higher education providers"]
whoMustUse: "none-stated; it is a reference point, not a requirement (D1, front matter)"
howUsed: ["design", "approval", "review", "other: external examining; PSRBs; information for prospective students and employers"]
doesNot: "it is not a national curriculum and does not prescribe teaching, learning or assessment; it carries no statutory or regulatory requirement (D1, front matter)"
beneficiary: the student
statedScope: "\"The Subject Benchmark Statement for Librarianship, Information, Knowledge, Records and Archives Management sets out threshold and typical standards for bachelor's degrees with honours, postgraduate certificates, postgraduate diplomas and master's degrees.\" (D1, 1.1)"
statedSubjects:
  - { name: "Librarianship, Information, Knowledge, Records and Archives Management", locator: "(D1, title; 1.1)", kind: "subject", codes: [{ scheme: "hecos", code: "100913", label: "librarianship" }, { scheme: "hecos", code: "100915", label: "archives and records management" }, { scheme: "hecos", code: "100370", label: "information management" }, { scheme: "hecos", code: "100916", label: "information services" }] }
subjects: see front matter (subjectScope subjects)
```

### S3 Structure
<!-- label: both; status: drafted; basis: primary -->
```yaml
components:
  - { number: "1.1", order: 3, componentType: paragraph, parent: "section 1", heading: "Context", gloss: "what the statement covers; awards; joint courses vary" }
  - { number: "1.2", order: 4, componentType: paragraph, parent: "section 1", heading: "Purposes of a Librarianship, Information, Knowledge, Records and Archives Management degree", gloss: "aim: preparing students for information careers" }
  - { number: "1.3", order: 5, componentType: area, parent: "section 1", heading: "Purposes of a Librarianship, Information, Knowledge, Records and Archives Management degree", gloss: "areas courses are likely to address, under seven headings" }
  - { number: "1.4", order: 6, componentType: area, parent: "section 1", heading: "Characteristics of a Librarianship, Information, Knowledge, Records and Archives Management degree", gloss: "usual features of degrees in the field" }
  - { number: "1.5", order: 7, componentType: practice, parent: "section 1", heading: "Characteristics of a Librarianship, Information, Knowledge, Records and Archives Management degree", gloss: "varied teaching; courses set their own outcomes" }
  - { number: "1.6", order: 8, componentType: practice, parent: "section 1", heading: "Characteristics of a Librarianship, Information, Knowledge, Records and Archives Management degree", gloss: "varied assessment; clear policies; formative and summative" }
  - { number: "1.7", order: 9, componentType: paragraph, parent: "section 1", heading: "Equality, diversity and inclusion", gloss: "the disciplines and equitable access to information" }
  - { number: "1.8", order: 10, componentType: paragraph, parent: "section 1", heading: "Equality, diversity and inclusion", gloss: "information services, needs and information architecture" }
  - { number: "1.9", order: 11, componentType: paragraph, parent: "section 1", heading: "Equality, diversity and inclusion", gloss: "cultural competence and care for historic material" }
  - { number: "1.10", order: 12, componentType: paragraph, parent: "section 1", heading: "Equality, diversity and inclusion", gloss: "fair access at the heart of professional ethics" }
  - { number: "1.11", order: 13, componentType: paragraph, parent: "section 1", heading: "Accessibility and the needs of disabled students", gloss: "accessible courses and attention to varied student needs" }
  - { number: "1.12", order: 14, componentType: paragraph, parent: "section 1", heading: "Education for sustainable development", gloss: "the field and the UN sustainable development goals" }
  - { number: "1.13", order: 15, componentType: paragraph, parent: "section 1", heading: "Education for sustainable development", gloss: "recorded knowledge and heritage as sustainability" }
  - { number: "1.14", order: 16, componentType: paragraph, parent: "section 1", heading: "Education for sustainable development", gloss: "sustainable management of information; sector initiatives" }
  - { number: "1.15", order: 17, componentType: paragraph, parent: "section 1", heading: "Employability, enterprise and entrepreneurship education", gloss: "employability education and career destinations" }
  - { number: "1.16", order: 18, componentType: paragraph, parent: "section 1", heading: "Employability, enterprise and entrepreneurship education", gloss: "entrepreneurship education beyond employment" }
  - { number: "1.17", order: 19, componentType: practice, parent: "section 1", heading: "Employability, enterprise and entrepreneurship education", gloss: "practice-based courses and authentic assessment" }
  - { number: "1.18", order: 20, componentType: paragraph, parent: "section 1", heading: "Employability, enterprise and entrepreneurship education", gloss: "enterprise skills and the professional skills base" }
  - { number: "1.19", order: 21, componentType: paragraph, parent: "section 1", heading: "Employability, enterprise and entrepreneurship education", gloss: "enterprise at the core of the subject" }
  - { number: "1.20", order: 22, componentType: paragraph, parent: "section 1", heading: "Generative artificial intelligence", gloss: "generative AI: ethical questions and literacies" }
  - { number: "1.21", order: 23, componentType: paragraph, parent: "section 1", heading: "Generative artificial intelligence", gloss: "preparing students to use AI ethically in services" }
  - { number: "2.1", order: 25, componentType: paragraph, parent: "section 2", heading: "Design", gloss: "ethical, theoretical and legal foundations; careers" }
  - { number: "2.2", order: 26, componentType: paragraph, parent: "section 2", heading: "Design", gloss: "vocational and academic; many routes in" }
  - { number: "2.3", order: 27, componentType: paragraph, parent: "section 2", heading: "Design", gloss: "information as the object of study; reflection" }
  - { number: "2.4", order: 28, componentType: paragraph, parent: "section 2", heading: "Progression", gloss: "progression through the levels to the threshold" }
  - { number: "2.5", order: 29, componentType: paragraph, parent: "section 2", heading: "Progression", gloss: "readiness for postgraduate study" }
  - { number: "2.6", order: 30, componentType: paragraph, parent: "section 2", heading: "Progression", gloss: "joint and combined honours routes" }
  - { number: "2.7", order: 31, componentType: paragraph, parent: "section 2", heading: "Progression", gloss: "exit awards below honours" }
  - { number: "2.8", order: 32, componentType: paragraph, parent: "section 2", heading: "Progression", gloss: "continuing development and professional recognition" }
  - { number: "2.9", order: 33, componentType: paragraph, parent: "section 2", heading: "Flexibility", gloss: "flexible teaching; part-time and mature students" }
  - { number: "2.10", order: 34, componentType: paragraph, parent: "section 2", heading: "Flexibility", gloss: "modes of study, credit and micro-credentials" }
  - { number: "2.11", order: 35, componentType: paragraph, parent: "section 2", heading: "Flexibility", gloss: "course lengths across the UK nations" }
  - { number: "2.12", order: 36, componentType: paragraph, parent: "section 2", heading: "Flexibility", gloss: "part-time credit in proportion to study" }
  - { number: "2.13", order: 37, componentType: paragraph, parent: "section 2", heading: "Partnership", gloss: "varied careers; learning tied to society" }
  - { number: "2.14", order: 38, componentType: paragraph, parent: "section 2", heading: "Partnership", gloss: "placements and workplace projects" }
  - { number: "2.15", order: 39, componentType: paragraph, parent: "section 2", heading: "Partnership", gloss: "accreditation and engaging with professional bodies" }
  - { number: "2.16", order: 40, componentType: paragraph, parent: "section 2", heading: "Monitoring and review", gloss: "monitoring and periodic review" }
  - { number: "2.17", order: 41, componentType: paragraph, parent: "section 2", heading: "Monitoring and review", gloss: "the student voice in monitoring" }
  - { number: "2.18", order: 42, componentType: paragraph, parent: "section 2", heading: "Monitoring and review", gloss: "external reviewers in periodic review" }
  - { number: "2.19", order: 43, componentType: paragraph, parent: "section 2", heading: "Monitoring and review", gloss: "external examiners and threshold standards" }
  - { number: "2.20", order: 44, componentType: paragraph, parent: "section 2", heading: "Monitoring and review", gloss: "professional accreditation of courses" }
  - { number: "3.1", order: 46, componentType: area, parent: "section 3", heading: "Content", gloss: "a broad, interdisciplinary subject" }
  - { number: "3.2", order: 47, componentType: area, parent: "section 3", heading: "Content", gloss: "content gives a broad, relevant base" }
  - { number: "3.3", order: 48, componentType: practice, parent: "section 3", heading: "Teaching and learning", gloss: "modes of teaching; theory and practice" }
  - { number: "3.4", order: 49, componentType: practice, parent: "section 3", heading: "Teaching and learning", gloss: "forms of teaching to suit learners" }
  - { number: "3.5", order: 50, componentType: practice, parent: "section 3", heading: "Teaching and learning", gloss: "partnership with professional practice" }
  - { number: "3.6", order: 51, componentType: practice, parent: "section 3", heading: "Teaching and learning", gloss: "support for independent learning" }
  - { number: "3.7", order: 52, componentType: practice, parent: "section 3", heading: "Teaching and learning", gloss: "evidence-based practice and research training" }
  - { number: "3.8", order: 53, componentType: practice, parent: "section 3", heading: "Teaching and learning", gloss: "continuing development and lifelong learning" }
  - { number: "3.9", order: 54, componentType: practice, parent: "section 3", heading: "Assessment", gloss: "why varied assessment matters" }
  - { number: "3.10", order: 55, componentType: practice, parent: "section 3", heading: "Assessment", gloss: "authentic assignments; what assessment will include" }
  - { number: "3.11", order: 56, componentType: practice, parent: "section 3", heading: "Assessment", gloss: "feedback and self-directed learning" }
  - { number: "4.1", order: 58, componentType: paragraph, parent: "section 4", heading: "Introduction", gloss: "threshold standards for honours defined" }
  - { number: "4.2", order: 59, componentType: paragraph, parent: "section 4", heading: "Introduction", gloss: "most exceed threshold; Annex D for classes" }
  - { number: "4.3", order: 60, componentType: paragraph, parent: "section 4", heading: "Introduction", gloss: "published criteria and feedback" }
  - { number: "4.4", order: 61, componentType: paragraph, parent: "section 4", heading: "Introduction", gloss: "not competence standards; equality guidance" }
  - { number: "4.5", order: 62, componentType: stem, parent: "section 4", heading: "Threshold level", gloss: "honours threshold: core knowledge and application" }
  - { number: "4.6", order: 63, componentType: paragraph, parent: "section 4", heading: "Threshold level", gloss: "third class: some proficiency in most attributes" }
  - { number: "4.7", order: 64, componentType: stem, parent: "section 4", heading: "Subject knowledge, understanding and skills", gloss: "honours subject knowledge and skills list" }
  - { number: "4.8", order: 65, componentType: stem, parent: "section 4", heading: "Generic skills", gloss: "honours generic skills list" }
  - { number: "4.9", order: 66, componentType: stem, parent: "section 4", heading: "Master's degree in Librarianship, Information, Knowledge, Records and Archive Management", gloss: "the postgraduate standard: advanced concepts" }
  - { number: "4.10", order: 67, componentType: paragraph, parent: "section 4", heading: "Master's degree in Librarianship, Information, Knowledge, Records and Archive Management", gloss: "master's knowledge, application and options" }
  - { number: "4.11", order: 68, componentType: stem, parent: "section 4", heading: "Subject knowledge, understanding and skills (master's)", gloss: "master's threshold and subject skills list" }
  - { number: "4.12", order: 69, componentType: stem, parent: "section 4", heading: "Generic skills (master's)", gloss: "master's generic skills list" }
  - { number: "1", componentType: section, parent: none, heading: "Context and purposes of a Librarianship, Information, Knowledge, Records and Archives Management degree", gloss: "section 1" }
  - { number: "2", componentType: section, parent: none, heading: "Distinctive features of Librarianship, Information, Knowledge, Records and Archive Management", gloss: "section 2" }
  - { number: "3", componentType: section, parent: none, heading: "Content, structure and delivery", gloss: "section 3" }
  - { number: "4", componentType: section, parent: none, heading: "Benchmark standards", gloss: "section 4" }
excluded:
  - { number: "none", heading: "About this Statement; How can I use this document?; Relationship to legislation; Additional sector reference points", kind: "other: front matter, read for S1 and S2" }
  - { number: "none", heading: "section heading lines (sections 1 to 4)", kind: "other: headings, recorded in S3 as sections" }
  - { number: "5", heading: "List of references and further resources", kind: "other: references, read for SB5, SB6 and D3" }
  - { number: "6", heading: "Membership of the Advisory Group", kind: "other: membership lists, read for S8 and supersedes" }
```

### S4 Statements
<!-- label: both; status: drafted; basis: primary. Only standards (D-std-0002 (a)): 101 records. `source` is the issuer's statement exactly as its span holds it (D-std-0014). -->
```yaml
- id: qaa/librarianship-information-knowledge-records-and-archives-management-2025/2.3.s1
  locator: { number: "2.3.s1", headingPath: ["Distinctive features of Librarianship, Information, Knowledge, Records and Archive Management", "Design"] }
  span: { start: 32914, end: 33074 }
  source: "As such, students are required to reflect on their own experiences and ethical priorities as information users, when information is itself the subject of study."
  stem: none
  statementType: requirement
  rung: none
  force: must
  level: none
  appliesTo: "students of the subject at any award"
  addressee: learner
  verbs: ["required", "reflect"]
  about: "reflecting on their own information use and ethics"
  themes: [none]
  domain: subject-skill
  award: ["bachelor's with honours", "master's", "postgraduate diploma", "postgraduate certificate"]
  gradeOf: none
  paraphrase: "Since information is the very thing the subject studies, students must look back on their own experience and ethical priorities as people who use information."
  quote: full   # the issuer's statement is in `source` (D-std-0014)
  audience: both
  subjects: inherited
- id: qaa/librarianship-information-knowledge-records-and-archives-management-2025/2.3.s2
  locator: { number: "2.3.s2", headingPath: ["Distinctive features of Librarianship, Information, Knowledge, Records and Archive Management", "Design"] }
  span: { start: 33075, end: 33254 }
  source: "Students should be able to develop and demonstrate an understanding of the fluidity of information, impact of use and need for appraisal amid societal and technological evolution."
  stem: none
  statementType: outcome
  rung: none
  force: should
  level: none
  appliesTo: "students of the subject at any award"
  addressee: learner
  verbs: ["develop", "demonstrate"]
  about: "how information shifts and why it needs appraising"
  themes: [none]
  domain: understanding
  award: ["bachelor's with honours", "master's", "postgraduate diploma", "postgraduate certificate"]
  gradeOf: none
  paraphrase: "Students should be able to build, and show, an understanding that information keeps changing, that how it is used has effects, and that it has to be judged afresh as society and technology move on."
  quote: full   # the issuer's statement is in `source` (D-std-0014)
  audience: both
  subjects: inherited
- id: qaa/librarianship-information-knowledge-records-and-archives-management-2025/2.6
  locator: { number: "2.6", headingPath: ["Distinctive features of Librarianship, Information, Knowledge, Records and Archive Management", "Progression"] }
  span: { start: 34543, end: 34942 }
  source: "Undergraduates studying Librarianship, Information, Knowledge, Records and Archives Management courses as part of a combined or joint degree with other subjects (including courses that specify major and minor options) will achieve core elements of the specific and generic skills outlined in this Statement, and will add others according to the areas covered in the other subject(s) of their degree."
  stem: none
  statementType: expectation
  rung: none
  force: will
  level: fheq:6
  appliesTo: "joint and combined honours students"
  addressee: learner
  verbs: ["achieve", "add"]
  about: "core skills for joint and combined honours students"
  themes: [none]
  domain: none
  award: ["bachelor's with honours"]
  gradeOf: none
  paraphrase: "Undergraduates taking the subject within a joint or combined degree, including major and minor routes, will attain the central subject-specific and generic skills set out here and gain others from their second subject."
  quote: full   # the issuer's statement is in `source` (D-std-0014)
  audience: both
  subjects: inherited
- id: qaa/librarianship-information-knowledge-records-and-archives-management-2025/2.17
  locator: { number: "2.17", headingPath: ["Distinctive features of Librarianship, Information, Knowledge, Records and Archive Management", "Monitoring and review"] }
  span: { start: 40936, end: 41109 }
  source: "The student voice is paramount in monitoring and review, and degree-awarding bodies will have in place a system for student input into the monitoring and evaluation process."
  stem: none
  statementType: expectation
  rung: none
  force: will
  level: none
  appliesTo: "degree-awarding bodies"
  addressee: provider
  verbs: ["have"]
  about: "a system for student input to course monitoring"
  themes: [none]
  domain: none
  award: ["bachelor's with honours", "master's", "postgraduate diploma", "postgraduate certificate"]
  gradeOf: none
  paraphrase: "Students' views come first in monitoring and review, and the awarding body will run a system through which students feed into monitoring and evaluation."
  quote: full   # the issuer's statement is in `source` (D-std-0014)
  audience: practitioner
  subjects: inherited
- id: qaa/librarianship-information-knowledge-records-and-archives-management-2025/2.18
  locator: { number: "2.18", headingPath: ["Distinctive features of Librarianship, Information, Knowledge, Records and Archive Management", "Monitoring and review"] }
  span: { start: 41470, end: 41681 }
  source: "Providers will use external reviewers as part of periodic review to gain an independent perspective on any proposed changes and ensure threshold standards are achieved and content is appropriate for the subject."
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
  award: ["bachelor's with honours", "master's", "postgraduate diploma", "postgraduate certificate"]
  gradeOf: none
  paraphrase: "In periodic review the institution will bring in external reviewers, for an outside view of planned changes and to confirm that threshold standards are met and content suits the subject."
  quote: full   # the issuer's statement is in `source` (D-std-0014)
  audience: practitioner
  subjects: inherited
- id: qaa/librarianship-information-knowledge-records-and-archives-management-2025/3.10.b1
  locator: { number: "3.10.b1", headingPath: ["Content, structure and delivery", "Assessment"] }
  span: { start: 47058, end: 47199 }
  source: "allow a student to develop and demonstrate professional competencies, for example through portfolios, synoptic assessment and self-reflection"
  stem: "3.10"
  statementType: expectation
  rung: none
  force: will
  level: none
  appliesTo: "assessment in courses of the subject"
  addressee: both
  verbs: ["allow", "develop", "demonstrate"]
  about: "assessment of professional competencies"
  themes: [none]
  domain: none
  award: ["bachelor's with honours", "master's", "postgraduate diploma", "postgraduate certificate"]
  gradeOf: none
  paraphrase: "Assessment will include tasks, such as portfolios, synoptic work and self-reflection, through which students build and show professional competence."
  quote: full   # the issuer's statement is in `source` (D-std-0014)
  audience: both
  subjects: inherited
- id: qaa/librarianship-information-knowledge-records-and-archives-management-2025/3.10.b2
  locator: { number: "3.10.b2", headingPath: ["Content, structure and delivery", "Assessment"] }
  span: { start: 47202, end: 47431 }
  source: "provide the opportunity for reflexive and critical evaluation of professional and sector identity, professional development and a student's learning journey, for example through critical reflections, presentations or case studies"
  stem: "3.10"
  statementType: expectation
  rung: none
  force: will
  level: none
  appliesTo: "assessment in courses of the subject"
  addressee: both
  verbs: ["provide"]
  about: "reflexive evaluation of professional identity"
  themes: [none]
  domain: none
  award: ["bachelor's with honours", "master's", "postgraduate diploma", "postgraduate certificate"]
  gradeOf: none
  paraphrase: "Assessment will include chances to evaluate, reflexively and critically, professional and sector identity, professional growth and the student's own learning, through reflections, presentations or case studies."
  quote: full   # the issuer's statement is in `source` (D-std-0014)
  audience: both
  subjects: inherited
- id: qaa/librarianship-information-knowledge-records-and-archives-management-2025/3.10.b3
  locator: { number: "3.10.b3", headingPath: ["Content, structure and delivery", "Assessment"] }
  span: { start: 47434, end: 47707 }
  source: "enable students to engage in authentic assessment and apply learning which makes a meaningful contribution within sector or workplace settings, or in social environments and contexts, by engaging in practical projects, placements or producing project- related documentation"
  stem: "3.10"
  statementType: expectation
  rung: none
  force: will
  level: none
  appliesTo: "assessment in courses of the subject"
  addressee: both
  verbs: ["enable", "engage", "apply"]
  about: "authentic assessment in real settings"
  themes: [none]
  domain: none
  award: ["bachelor's with honours", "master's", "postgraduate diploma", "postgraduate certificate"]
  gradeOf: none
  paraphrase: "Assessment will include authentic tasks in which students apply their learning to make a real contribution in a workplace, sector or community setting, through projects, placements or project documents."
  quote: full   # the issuer's statement is in `source` (D-std-0014)
  audience: both
  subjects: inherited
- id: qaa/librarianship-information-knowledge-records-and-archives-management-2025/3.10.b4
  locator: { number: "3.10.b4", headingPath: ["Content, structure and delivery", "Assessment"] }
  span: { start: 47710, end: 47857 }
  source: "demonstrate an ability to work collaboratively and effectively as part of a group through, for example, group projects, presentations or portfolios"
  stem: "3.10"
  statementType: expectation
  rung: none
  force: will
  level: none
  appliesTo: "assessment in courses of the subject"
  addressee: both
  verbs: ["demonstrate", "work"]
  about: "assessed group work"
  themes: [none]
  domain: none
  award: ["bachelor's with honours", "master's", "postgraduate diploma", "postgraduate certificate"]
  gradeOf: none
  paraphrase: "Assessment will include tasks, such as group projects, presentations or portfolios, that show students can work well with others in a team."
  quote: full   # the issuer's statement is in `source` (D-std-0014)
  audience: both
  subjects: inherited
- id: qaa/librarianship-information-knowledge-records-and-archives-management-2025/3.10.b5
  locator: { number: "3.10.b5", headingPath: ["Content, structure and delivery", "Assessment"] }
  span: { start: 47860, end: 48078 }
  source: "demonstrate the ability to use digital technologies, including use of generative AI, for the creation of websites, databases, online catalogues, presentations, posters, social media outputs and/or other digital content"
  stem: "3.10"
  statementType: expectation
  rung: none
  force: will
  level: none
  appliesTo: "assessment in courses of the subject"
  addressee: both
  verbs: ["demonstrate", "use"]
  about: "assessed use of digital technologies"
  themes: [none]
  domain: none
  award: ["bachelor's with honours", "master's", "postgraduate diploma", "postgraduate certificate"]
  gradeOf: none
  paraphrase: "Assessment will include tasks showing that students can use digital technologies, generative AI among them, to make websites, databases, catalogues, presentations, posters, social media outputs or other digital content."
  quote: full   # the issuer's statement is in `source` (D-std-0014)
  audience: both
  subjects: inherited
- id: qaa/librarianship-information-knowledge-records-and-archives-management-2025/3.10.b6
  locator: { number: "3.10.b6", headingPath: ["Content, structure and delivery", "Assessment"] }
  span: { start: 48081, end: 48255 }
  source: "enable students to conduct research, involving primary data collection or extensive interrogation and synthesis of secondary data, data analysis and presentation of findings."
  stem: "3.10"
  statementType: expectation
  rung: none
  force: will
  level: none
  appliesTo: "assessment in courses of the subject"
  addressee: both
  verbs: ["enable", "conduct"]
  about: "assessed research"
  themes: [none]
  domain: none
  award: ["bachelor's with honours", "master's", "postgraduate diploma", "postgraduate certificate"]
  gradeOf: none
  paraphrase: "Assessment will include research tasks, gathering primary data or interrogating and synthesising secondary data at length, analysing it and presenting the findings."
  quote: full   # the issuer's statement is in `source` (D-std-0014)
  audience: both
  subjects: inherited
- id: qaa/librarianship-information-knowledge-records-and-archives-management-2025/4.2
  locator: { number: "4.2", headingPath: ["Benchmark standards", "Introduction"] }
  span: { start: 49278, end: 49508 }
  source: "Each higher education provider has its own method of determining what appropriate evidence of this achievement will be and should refer to Annex D of the Frameworks for Higher Education Qualifications of UK Degree-Awarding Bodies."
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
  paraphrase: "Each institution sets its own way of deciding what evidence shows achievement beyond the threshold, and should consult Annex D of the UK qualifications frameworks (the classification descriptions) in doing so."
  quote: full   # the issuer's statement is in `source` (D-std-0014)
  audience: practitioner
  subjects: inherited
- id: qaa/librarianship-information-knowledge-records-and-archives-management-2025/4.4
  locator: { number: "4.4", headingPath: ["Benchmark standards", "Introduction"] }
  span: { start: 50415, end: 50534 }
  source: "In these circumstances, providers should follow the most recent guidance from the Equality and Human Rights Commission."
  stem: none
  statementType: expectation
  rung: none
  force: should
  level: none
  appliesTo: "providers writing competence standards"
  addressee: provider
  verbs: ["follow"]
  about: "competence standards and equality guidance"
  themes: [none]
  domain: none
  award: ["bachelor's with honours", "master's", "postgraduate diploma", "postgraduate certificate"]
  gradeOf: none
  paraphrase: "Where an institution writes competence standards under the Equality Act 2010 into a programme specification, it should follow the latest guidance of the Equality and Human Rights Commission."
  quote: full   # the issuer's statement is in `source` (D-std-0014)
  audience: practitioner
  subjects: inherited
- id: qaa/librarianship-information-knowledge-records-and-archives-management-2025/4.5.b1
  locator: { number: "4.5.b1", headingPath: ["Benchmark standards", "Threshold level"] }
  span: { start: 51093, end: 51142 }
  source: "apply knowledge in structured and guided contexts"
  stem: "4.5"
  statementType: threshold
  rung: threshold
  force: should
  level: fheq:6
  appliesTo: "honours graduates at the threshold"
  addressee: learner
  verbs: ["apply"]
  about: "applying knowledge in structured, guided settings"
  themes: [none]
  domain: subject-skill
  award: ["bachelor's with honours"]
  gradeOf: none
  paraphrase: "Part of those concepts and practices: honours students should be able to use their knowledge where the setting is structured and guidance is given."
  quote: full   # the issuer's statement is in `source` (D-std-0014)
  audience: both
  subjects: inherited
- id: qaa/librarianship-information-knowledge-records-and-archives-management-2025/4.5.s1
  locator: { number: "4.5.s1", headingPath: ["Benchmark standards", "Threshold level"] }
  span: { start: 50555, end: 50788 }
  source: "On graduating with an honours degree in Librarianship, Information, Knowledge, Records and Archive Management, students should be able to demonstrate a systematic understanding of the main body of knowledge for their course of study."
  stem: none
  statementType: threshold
  rung: threshold
  force: should
  level: fheq:6
  appliesTo: "honours graduates at the threshold"
  addressee: learner
  verbs: ["demonstrate"]
  about: "systematic grasp of the course's core knowledge"
  themes: [none]
  domain: knowledge
  award: ["bachelor's with honours"]
  gradeOf: none
  paraphrase: "At the honours threshold, students should be able to show a systematic grasp of the central knowledge their course covers."
  quote: full   # the issuer's statement is in `source` (D-std-0014)
  audience: both
  subjects: inherited
- id: qaa/librarianship-information-knowledge-records-and-archives-management-2025/4.5.b2
  locator: { number: "4.5.b2", headingPath: ["Benchmark standards", "Threshold level"] }
  span: { start: 51145, end: 51207 }
  source: "analyse and evaluate information within established frameworks"
  stem: "4.5"
  statementType: threshold
  rung: threshold
  force: should
  level: fheq:6
  appliesTo: "honours graduates at the threshold"
  addressee: learner
  verbs: ["analyse", "evaluate"]
  about: "analysing information within set frameworks"
  themes: [none]
  domain: subject-skill
  award: ["bachelor's with honours"]
  gradeOf: none
  paraphrase: "Honours students should be able to analyse and judge information inside frameworks already set for the task."
  quote: full   # the issuer's statement is in `source` (D-std-0014)
  audience: both
  subjects: inherited
- id: qaa/librarianship-information-knowledge-records-and-archives-management-2025/4.5.s2
  locator: { number: "4.5.s2", headingPath: ["Benchmark standards", "Threshold level"] }
  span: { start: 50789, end: 51025 }
  source: "They should be able to understand and apply essential concepts, principles and practices of the subject in the context of well-defined scenarios, showing judgement in the selection and application of processes, materials and techniques."
  stem: none
  statementType: threshold
  rung: threshold
  force: should
  level: fheq:6
  appliesTo: "honours graduates at the threshold"
  addressee: learner
  verbs: ["understand", "apply", "showing"]
  about: "using core concepts in clearly bounded cases"
  themes: [none]
  domain: subject-skill
  award: ["bachelor's with honours"]
  gradeOf: none
  paraphrase: "They should be able to grasp and use the subject's key concepts, principles and practices in clearly bounded situations, choosing processes, materials and techniques with judgement."
  quote: full   # the issuer's statement is in `source` (D-std-0014)
  audience: both
  subjects: inherited
- id: qaa/librarianship-information-knowledge-records-and-archives-management-2025/4.5.b3
  locator: { number: "4.5.b3", headingPath: ["Benchmark standards", "Threshold level"] }
  span: { start: 51210, end: 51274 }
  source: "use tools, technologies and methodologies in practical settings."
  stem: "4.5"
  statementType: threshold
  rung: threshold
  force: should
  level: fheq:6
  appliesTo: "honours graduates at the threshold"
  addressee: learner
  verbs: ["use"]
  about: "using tools and methods in practice"
  themes: [none]
  domain: subject-skill
  award: ["bachelor's with honours"]
  gradeOf: none
  paraphrase: "Honours students should be able to use the subject's tools, technologies and methods in practical settings."
  quote: full   # the issuer's statement is in `source` (D-std-0014)
  audience: both
  subjects: inherited
- id: qaa/librarianship-information-knowledge-records-and-archives-management-2025/4.6
  locator: { number: "4.6", headingPath: ["Benchmark standards", "Threshold level"] }
  span: { start: 51279, end: 51472 }
  source: "In this context, honours graduates at a threshold level of attainment (third class) will have demonstrated some degree of proficiency in the majority of the attributes listed in this Statement."
  stem: none
  statementType: threshold
  rung: threshold
  force: will
  level: fheq:6
  appliesTo: "honours graduates at the threshold"
  addressee: learner
  verbs: ["demonstrated"]
  about: "what the third-class threshold means"
  themes: [none]
  domain: none
  award: ["bachelor's with honours"]
  gradeOf: none
  paraphrase: "Honours graduates at the threshold, the third class, will have shown some proficiency in most, not all, of the attributes the statement lists."
  quote: full   # the issuer's statement is in `source` (D-std-0014)
  audience: both
  subjects: inherited
- id: qaa/librarianship-information-knowledge-records-and-archives-management-2025/4.7.b1
  locator: { number: "4.7.b1", headingPath: ["Benchmark standards", "Subject knowledge, understanding and skills"] }
  span: { start: 51666, end: 51845 }
  source: "develop and implement strategies that identify and address biases in information collections, systems and services, ensuring fair representation and dismantling barriers to access"
  stem: "4.7"
  statementType: threshold
  rung: threshold
  force: should
  level: fheq:6
  appliesTo: "honours graduates at the threshold"
  addressee: learner
  verbs: ["develop", "implement", "identify", "address"]
  about: "tackling bias in collections, systems and services"
  themes: [none]
  domain: subject-skill
  award: ["bachelor's with honours"]
  gradeOf: none
  paraphrase: "At the honours threshold, graduates should be able to plan and carry out approaches that expose and reduce bias in collections, systems and services, so that people are fairly represented and obstacles to access come down."
  quote: full   # the issuer's statement is in `source` (D-std-0014)
  audience: both
  subjects: inherited
- id: qaa/librarianship-information-knowledge-records-and-archives-management-2025/4.7.b2
  locator: { number: "4.7.b2", headingPath: ["Benchmark standards", "Subject knowledge, understanding and skills"] }
  span: { start: 51848, end: 52072 }
  source: "demonstrate a commitment to accessibility and equity in all aspects of their work, including research, communication and collaboration with others, and actively seek to remove barriers to information access and participation"
  stem: "4.7"
  statementType: threshold
  rung: threshold
  force: should
  level: fheq:6
  appliesTo: "honours graduates at the threshold"
  addressee: learner
  verbs: ["demonstrate", "seek", "remove"]
  about: "a working commitment to access and equity"
  themes: [none]
  domain: subject-skill
  award: ["bachelor's with honours"]
  gradeOf: none
  paraphrase: "At the honours threshold, graduates should be able to show, across research, communication and teamwork, that they hold accessibility and fairness as commitments, and act to clear away what blocks access and participation."
  quote: full   # the issuer's statement is in `source` (D-std-0014)
  audience: both
  subjects: inherited
- id: qaa/librarianship-information-knowledge-records-and-archives-management-2025/4.7.b3
  locator: { number: "4.7.b3", headingPath: ["Benchmark standards", "Subject knowledge, understanding and skills"] }
  span: { start: 52075, end: 52202 }
  source: "create inclusive physical and digital library spaces and collections that cater to individuals with varying abilities and needs"
  stem: "4.7"
  statementType: threshold
  rung: threshold
  force: should
  level: fheq:6
  appliesTo: "honours graduates at the threshold"
  addressee: learner
  verbs: ["create", "cater"]
  about: "inclusive physical and online spaces and collections"
  themes: [none]
  domain: subject-skill
  award: ["bachelor's with honours"]
  gradeOf: none
  paraphrase: "At the honours threshold, graduates should be able to shape library spaces and collections, in person and online, so that they serve people with a wide spread of abilities and needs."
  quote: full   # the issuer's statement is in `source` (D-std-0014)
  audience: both
  subjects: inherited
- id: qaa/librarianship-information-knowledge-records-and-archives-management-2025/4.7.b4
  locator: { number: "4.7.b4", headingPath: ["Benchmark standards", "Subject knowledge, understanding and skills"] }
  span: { start: 52205, end: 52410 }
  source: "partner with community organisations and educators to promote a range of literacies, including academic, data, digital, media and information, in supporting scholarship and lifelong learning within society"
  stem: "4.7"
  statementType: threshold
  rung: threshold
  force: should
  level: fheq:6
  appliesTo: "honours graduates at the threshold"
  addressee: learner
  verbs: ["partner", "promote"]
  about: "building literacies with community partners"
  themes: [none]
  domain: subject-skill
  award: ["bachelor's with honours"]
  gradeOf: none
  paraphrase: "At the honours threshold, graduates should be able to work with community groups and teachers to advance academic, data, digital, media and information literacies that serve scholarship and learning through life."
  quote: full   # the issuer's statement is in `source` (D-std-0014)
  audience: both
  subjects: inherited
- id: qaa/librarianship-information-knowledge-records-and-archives-management-2025/4.7.b5
  locator: { number: "4.7.b5", headingPath: ["Benchmark standards", "Subject knowledge, understanding and skills"] }
  span: { start: 52413, end: 52729 }
  source: "engage in critical discussions about human rights and equalities in information provision, including confronting structural inequalities within knowledge systems, such as biases based on race, gender or disability, and championing the importance of information equity for groups who have been previously marginalised"
  stem: "4.7"
  statementType: threshold
  rung: threshold
  force: should
  level: fheq:6
  appliesTo: "honours graduates at the threshold"
  addressee: learner
  verbs: ["engage", "confronting", "championing"]
  about: "human rights, equality and fair access to information"
  themes: [none]
  domain: understanding
  award: ["bachelor's with honours"]
  gradeOf: none
  paraphrase: "At the honours threshold, graduates should be able to debate critically how information provision bears on human rights and equality, question structural inequality and bias (by race, gender or disability) in knowledge systems, and argue for fair access for groups once pushed aside."
  quote: full   # the issuer's statement is in `source` (D-std-0014)
  audience: both
  subjects: inherited
- id: qaa/librarianship-information-knowledge-records-and-archives-management-2025/4.7.b6
  locator: { number: "4.7.b6", headingPath: ["Benchmark standards", "Subject knowledge, understanding and skills"] }
  span: { start: 52732, end: 52960 }
  source: "advocate for the importance of freedom of access to information as a fundamental human right, and the associated importance of open access to knowledge resources, and the skills and systems necessary for facilitating such access"
  stem: "4.7"
  statementType: threshold
  rung: threshold
  force: should
  level: fheq:6
  appliesTo: "honours graduates at the threshold"
  addressee: learner
  verbs: ["advocate"]
  about: "freedom of access and open access"
  themes: [none]
  domain: subject-skill
  award: ["bachelor's with honours"]
  gradeOf: none
  paraphrase: "At the honours threshold, graduates should be able to argue that free access to information is a basic human right, and make the case for open access to knowledge and for the skills and systems that make access possible."
  quote: full   # the issuer's statement is in `source` (D-std-0014)
  audience: both
  subjects: inherited
- id: qaa/librarianship-information-knowledge-records-and-archives-management-2025/4.7.b7
  locator: { number: "4.7.b7", headingPath: ["Benchmark standards", "Subject knowledge, understanding and skills"] }
  span: { start: 52963, end: 53144 }
  source: "develop retention schedules and comprehensive preservation plans addressing both physical and digital assets, ensuring long-term accessibility, and addressing format migration needs"
  stem: "4.7"
  statementType: threshold
  rung: threshold
  force: should
  level: fheq:6
  appliesTo: "honours graduates at the threshold"
  addressee: learner
  verbs: ["develop", "addressing", "ensuring"]
  about: "retention schedules and preservation plans"
  themes: [none]
  domain: subject-skill
  award: ["bachelor's with honours"]
  gradeOf: none
  paraphrase: "At the honours threshold, graduates should be able to draw up retention schedules and full preservation plans for physical and digital holdings that keep them usable for the long term and plan for format migration."
  quote: full   # the issuer's statement is in `source` (D-std-0014)
  audience: both
  subjects: inherited
- id: qaa/librarianship-information-knowledge-records-and-archives-management-2025/4.7.b8
  locator: { number: "4.7.b8", headingPath: ["Benchmark standards", "Subject knowledge, understanding and skills"] }
  span: { start: 53147, end: 53280 }
  source: "understand and apply appropriate archival principles, such as provenance and original order, when organising and describing materials"
  stem: "4.7"
  statementType: threshold
  rung: threshold
  force: should
  level: fheq:6
  appliesTo: "honours graduates at the threshold"
  addressee: learner
  verbs: ["understand", "apply"]
  about: "archival principles in arrangement and description"
  themes: [none]
  domain: understanding
  award: ["bachelor's with honours"]
  gradeOf: none
  paraphrase: "At the honours threshold, graduates should be able to understand archival principles such as provenance and original order and use them when arranging and describing collections."
  quote: full   # the issuer's statement is in `source` (D-std-0014)
  audience: both
  subjects: inherited
- id: qaa/librarianship-information-knowledge-records-and-archives-management-2025/4.7.b9
  locator: { number: "4.7.b9", headingPath: ["Benchmark standards", "Subject knowledge, understanding and skills"] }
  span: { start: 53283, end: 53423 }
  source: "adhere to industry standards for the storage of fragile or sensitive materials, ensuring proper environmental controls and security measures"
  stem: "4.7"
  statementType: threshold
  rung: threshold
  force: should
  level: fheq:6
  appliesTo: "honours graduates at the threshold"
  addressee: learner
  verbs: ["adhere", "ensuring"]
  about: "storage standards for fragile or sensitive items"
  themes: [none]
  domain: subject-skill
  award: ["bachelor's with honours"]
  gradeOf: none
  paraphrase: "At the honours threshold, graduates should be able to follow the sector's standards for keeping fragile or sensitive items, with the right environmental conditions and security."
  quote: full   # the issuer's statement is in `source` (D-std-0014)
  audience: both
  subjects: inherited
- id: qaa/librarianship-information-knowledge-records-and-archives-management-2025/4.7.b10
  locator: { number: "4.7.b10", headingPath: ["Benchmark standards", "Subject knowledge, understanding and skills"] }
  span: { start: 53426, end: 53586 }
  source: "master cataloguing and classification, description, and metadata creation and application using controlled vocabularies and standards to enhance discoverability"
  stem: "4.7"
  statementType: threshold
  rung: threshold
  force: should
  level: fheq:6
  appliesTo: "honours graduates at the threshold"
  addressee: learner
  verbs: ["master", "enhance"]
  about: "cataloguing, classification and metadata"
  themes: [none]
  domain: subject-skill
  award: ["bachelor's with honours"]
  gradeOf: none
  paraphrase: "At the honours threshold, graduates should be able to command cataloguing, classification, description and metadata work securely, using controlled vocabularies and standards so resources are easier to find."
  quote: full   # the issuer's statement is in `source` (D-std-0014)
  audience: both
  subjects: inherited
- id: qaa/librarianship-information-knowledge-records-and-archives-management-2025/4.7.b11
  locator: { number: "4.7.b11", headingPath: ["Benchmark standards", "Subject knowledge, understanding and skills"] }
  span: { start: 53589, end: 53714 }
  source: "design and manage content management systems, digital repositories and web platforms adhering to accessibility best practices"
  stem: "4.7"
  statementType: threshold
  rung: threshold
  force: should
  level: fheq:6
  appliesTo: "honours graduates at the threshold"
  addressee: learner
  verbs: ["design", "manage", "adhering"]
  about: "content systems, repositories and web platforms"
  themes: [none]
  domain: subject-skill
  award: ["bachelor's with honours"]
  gradeOf: none
  paraphrase: "At the honours threshold, graduates should be able to design and run content management systems, digital repositories and web platforms in line with good accessibility practice."
  quote: full   # the issuer's statement is in `source` (D-std-0014)
  audience: both
  subjects: inherited
- id: qaa/librarianship-information-knowledge-records-and-archives-management-2025/4.7.b12
  locator: { number: "4.7.b12", headingPath: ["Benchmark standards", "Subject knowledge, understanding and skills"] }
  span: { start: 53717, end: 53865 }
  source: "implement user-centred design principles and accessibility guidelines to create intuitive and inclusive interfaces for online resources and services"
  stem: "4.7"
  statementType: threshold
  rung: threshold
  force: should
  level: fheq:6
  appliesTo: "honours graduates at the threshold"
  addressee: learner
  verbs: ["implement", "create"]
  about: "user-centred, accessible interface design"
  themes: [none]
  domain: subject-skill
  award: ["bachelor's with honours"]
  gradeOf: none
  paraphrase: "At the honours threshold, graduates should be able to apply user-centred design and accessibility guidance so that online resources and services are intuitive and inclusive to use."
  quote: full   # the issuer's statement is in `source` (D-std-0014)
  audience: both
  subjects: inherited
- id: qaa/librarianship-information-knowledge-records-and-archives-management-2025/4.7.b13
  locator: { number: "4.7.b13", headingPath: ["Benchmark standards", "Subject knowledge, understanding and skills"] }
  span: { start: 53868, end: 53986 }
  source: "critically evaluate and apply emerging technologies for information management tasks, considering ethical implications"
  stem: "4.7"
  statementType: threshold
  rung: threshold
  force: should
  level: fheq:6
  appliesTo: "honours graduates at the threshold"
  addressee: learner
  verbs: ["evaluate", "apply", "considering"]
  about: "judging new technologies ethically"
  themes: [none]
  domain: subject-skill
  award: ["bachelor's with honours"]
  gradeOf: none
  paraphrase: "At the honours threshold, graduates should be able to appraise new technologies for managing information critically and put them to use, weighing their ethical consequences."
  quote: full   # the issuer's statement is in `source` (D-std-0014)
  audience: both
  subjects: inherited
- id: qaa/librarianship-information-knowledge-records-and-archives-management-2025/4.7.b14
  locator: { number: "4.7.b14", headingPath: ["Benchmark standards", "Subject knowledge, understanding and skills"] }
  span: { start: 53989, end: 54165 }
  source: "collaborate with educators and community partners to develop comprehensive information literacy and reader development programmes that address a range of skill levels and needs"
  stem: "4.7"
  statementType: threshold
  rung: threshold
  force: should
  level: fheq:6
  appliesTo: "honours graduates at the threshold"
  addressee: learner
  verbs: ["collaborate", "develop"]
  about: "information literacy and reader development programmes"
  themes: [none]
  domain: subject-skill
  award: ["bachelor's with honours"]
  gradeOf: none
  paraphrase: "At the honours threshold, graduates should be able to build, with teaching staff and community partners, full information literacy and reader development programmes for varied levels of skill and need."
  quote: full   # the issuer's statement is in `source` (D-std-0014)
  audience: both
  subjects: inherited
- id: qaa/librarianship-information-knowledge-records-and-archives-management-2025/4.7.b15
  locator: { number: "4.7.b15", headingPath: ["Benchmark standards", "Subject knowledge, understanding and skills"] }
  span: { start: 54168, end: 54304 }
  source: "design instruction and outreach activities that foster critical thinking, media literacy, and safe and responsible digital participation"
  stem: "4.7"
  statementType: threshold
  rung: threshold
  force: should
  level: fheq:6
  appliesTo: "honours graduates at the threshold"
  addressee: learner
  verbs: ["design", "foster"]
  about: "teaching and outreach for critical thinking"
  themes: [none]
  domain: subject-skill
  award: ["bachelor's with honours"]
  gradeOf: none
  paraphrase: "At the honours threshold, graduates should be able to plan teaching and outreach that build critical thinking, media literacy and safe, responsible participation online."
  quote: full   # the issuer's statement is in `source` (D-std-0014)
  audience: both
  subjects: inherited
- id: qaa/librarianship-information-knowledge-records-and-archives-management-2025/4.7.b16
  locator: { number: "4.7.b16", headingPath: ["Benchmark standards", "Subject knowledge, understanding and skills"] }
  span: { start: 54307, end: 54425 }
  source: "adapt critical information literacy instruction to diverse audiences, including children, adults and lifelong learners"
  stem: "4.7"
  statementType: threshold
  rung: threshold
  force: should
  level: fheq:6
  appliesTo: "honours graduates at the threshold"
  addressee: learner
  verbs: ["adapt"]
  about: "critical information literacy for varied audiences"
  themes: [none]
  domain: subject-skill
  award: ["bachelor's with honours"]
  gradeOf: none
  paraphrase: "At the honours threshold, graduates should be able to adjust critical information literacy teaching for different audiences, children, adults and lifelong learners among them."
  quote: full   # the issuer's statement is in `source` (D-std-0014)
  audience: both
  subjects: inherited
- id: qaa/librarianship-information-knowledge-records-and-archives-management-2025/4.7.b17
  locator: { number: "4.7.b17", headingPath: ["Benchmark standards", "Subject knowledge, understanding and skills"] }
  span: { start: 54432, end: 54567 }
  source: "collect and analyse user data, service metrics and industry trends to inform evidence- based decision-making and continuous improvement"
  stem: "4.7"
  statementType: threshold
  rung: threshold
  force: should
  level: fheq:6
  appliesTo: "honours graduates at the threshold"
  addressee: learner
  verbs: ["collect", "analyse", "inform"]
  about: "user data and metrics for evidence-based improvement"
  themes: [none]
  domain: subject-skill
  award: ["bachelor's with honours"]
  gradeOf: none
  paraphrase: "At the honours threshold, graduates should be able to gather and analyse data on users, service performance and sector trends, and use it to ground decisions in evidence and keep improving."
  quote: full   # the issuer's statement is in `source` (D-std-0014)
  audience: both
  subjects: inherited
- id: qaa/librarianship-information-knowledge-records-and-archives-management-2025/4.7.b18
  locator: { number: "4.7.b18", headingPath: ["Benchmark standards", "Subject knowledge, understanding and skills"] }
  span: { start: 54570, end: 54694 }
  source: "explore the use of AI tools for automated tasks like metadata generation and recommender systems, ensuring ethical oversight"
  stem: "4.7"
  statementType: threshold
  rung: threshold
  force: should
  level: fheq:6
  appliesTo: "honours graduates at the threshold"
  addressee: learner
  verbs: ["explore", "ensuring"]
  about: "AI tools for automated tasks, with ethical oversight"
  themes: [none]
  domain: subject-skill
  award: ["bachelor's with honours"]
  gradeOf: none
  paraphrase: "At the honours threshold, graduates should be able to try out AI tools for automated work such as metadata generation and recommender systems, keeping ethical oversight in place."
  quote: full   # the issuer's statement is in `source` (D-std-0014)
  audience: both
  subjects: inherited
- id: qaa/librarianship-information-knowledge-records-and-archives-management-2025/4.7.b19
  locator: { number: "4.7.b19", headingPath: ["Benchmark standards", "Subject knowledge, understanding and skills"] }
  span: { start: 54697, end: 54780 }
  source: "champion intellectual freedom, data privacy and open access to information and data"
  stem: "4.7"
  statementType: threshold
  rung: threshold
  force: should
  level: fheq:6
  appliesTo: "honours graduates at the threshold"
  addressee: learner
  verbs: ["champion"]
  about: "intellectual freedom, privacy and openness"
  themes: [none]
  domain: subject-skill
  award: ["bachelor's with honours"]
  gradeOf: none
  paraphrase: "At the honours threshold, graduates should be able to stand up for freedom of thought and expression, for the privacy of personal data, and for open access to information and data."
  quote: full   # the issuer's statement is in `source` (D-std-0014)
  audience: both
  subjects: inherited
- id: qaa/librarianship-information-knowledge-records-and-archives-management-2025/4.7.b20
  locator: { number: "4.7.b20", headingPath: ["Benchmark standards", "Subject knowledge, understanding and skills"] }
  span: { start: 54783, end: 54928 }
  source: "participate in the development of organisational policies that address ethical information practices, responsible data governance and user rights"
  stem: "4.7"
  statementType: threshold
  rung: threshold
  force: should
  level: fheq:6
  appliesTo: "honours graduates at the threshold"
  addressee: learner
  verbs: ["participate", "address"]
  about: "organisational policy on information ethics"
  themes: [none]
  domain: subject-skill
  award: ["bachelor's with honours"]
  gradeOf: none
  paraphrase: "At the honours threshold, graduates should be able to help shape organisational policy on ethical information practice, responsible data governance and the rights of users."
  quote: full   # the issuer's statement is in `source` (D-std-0014)
  audience: both
  subjects: inherited
- id: qaa/librarianship-information-knowledge-records-and-archives-management-2025/4.7.b21
  locator: { number: "4.7.b21", headingPath: ["Benchmark standards", "Subject knowledge, understanding and skills"] }
  span: { start: 54931, end: 55074 }
  source: "engage in local and national advocacy efforts to support legislation that promotes equitable access to information and safeguards user privacy."
  stem: "4.7"
  statementType: threshold
  rung: threshold
  force: should
  level: fheq:6
  appliesTo: "honours graduates at the threshold"
  addressee: learner
  verbs: ["engage", "support"]
  about: "advocacy for fair access and privacy law"
  themes: [none]
  domain: subject-skill
  award: ["bachelor's with honours"]
  gradeOf: none
  paraphrase: "At the honours threshold, graduates should be able to take part in local and national campaigning for laws that widen fair access to information and protect users' privacy."
  quote: full   # the issuer's statement is in `source` (D-std-0014)
  audience: both
  subjects: inherited
- id: qaa/librarianship-information-knowledge-records-and-archives-management-2025/4.8.b1
  locator: { number: "4.8.b1", headingPath: ["Benchmark standards", "Generic skills"] }
  span: { start: 55235, end: 55274 }
  source: "identify issues, questions and problems"
  stem: "4.8"
  statementType: threshold
  rung: threshold
  force: should
  level: fheq:6
  appliesTo: "honours graduates at the threshold"
  addressee: learner
  verbs: ["identify"]
  about: "identifying issues, questions and problems"
  themes: [none]
  domain: generic-skill
  award: ["bachelor's with honours"]
  gradeOf: none
  paraphrase: "At the honours threshold, graduates should be able to recognise the issues, questions and problems a situation raises."
  quote: full   # the issuer's statement is in `source` (D-std-0014)
  audience: both
  subjects: inherited
- id: qaa/librarianship-information-knowledge-records-and-archives-management-2025/4.8.b2
  locator: { number: "4.8.b2", headingPath: ["Benchmark standards", "Generic skills"] }
  span: { start: 55277, end: 55405 }
  source: "demonstrate proficiency in applying a wide range of referencing standards, adhering to their respective details and requirements"
  stem: "4.8"
  statementType: threshold
  rung: threshold
  force: should
  level: fheq:6
  appliesTo: "honours graduates at the threshold"
  addressee: learner
  verbs: ["demonstrate", "applying", "adhering"]
  about: "accurate use of referencing styles"
  themes: [none]
  domain: generic-skill
  award: ["bachelor's with honours"]
  gradeOf: none
  paraphrase: "At the honours threshold, graduates should be able to use a wide range of referencing styles accurately, following the detail each one asks for."
  quote: full   # the issuer's statement is in `source` (D-std-0014)
  audience: both
  subjects: inherited
- id: qaa/librarianship-information-knowledge-records-and-archives-management-2025/4.8.b3
  locator: { number: "4.8.b3", headingPath: ["Benchmark standards", "Generic skills"] }
  span: { start: 55408, end: 55470 }
  source: "identify gaps in their own knowledge and acquire new knowledge"
  stem: "4.8"
  statementType: threshold
  rung: threshold
  force: should
  level: fheq:6
  appliesTo: "honours graduates at the threshold"
  addressee: learner
  verbs: ["identify", "acquire"]
  about: "finding and filling gaps in their knowledge"
  themes: [none]
  domain: generic-skill
  award: ["bachelor's with honours"]
  gradeOf: none
  paraphrase: "At the honours threshold, graduates should be able to see where their own knowledge falls short and gain what is missing."
  quote: full   # the issuer's statement is in `source` (D-std-0014)
  audience: both
  subjects: inherited
- id: qaa/librarianship-information-knowledge-records-and-archives-management-2025/4.8.b4
  locator: { number: "4.8.b4", headingPath: ["Benchmark standards", "Generic skills"] }
  span: { start: 55473, end: 55521 }
  source: "understand and analyse knowledge and information"
  stem: "4.8"
  statementType: threshold
  rung: threshold
  force: should
  level: fheq:6
  appliesTo: "honours graduates at the threshold"
  addressee: learner
  verbs: ["understand", "analyse"]
  about: "understanding and analysing information"
  themes: [none]
  domain: generic-skill
  award: ["bachelor's with honours"]
  gradeOf: none
  paraphrase: "At the honours threshold, graduates should be able to make sense of knowledge and information and analyse it."
  quote: full   # the issuer's statement is in `source` (D-std-0014)
  audience: both
  subjects: inherited
- id: qaa/librarianship-information-knowledge-records-and-archives-management-2025/4.8.b5
  locator: { number: "4.8.b5", headingPath: ["Benchmark standards", "Generic skills"] }
  span: { start: 55524, end: 55579 }
  source: "synthesise the state of knowledge on a particular topic"
  stem: "4.8"
  statementType: threshold
  rung: threshold
  force: should
  level: fheq:6
  appliesTo: "honours graduates at the threshold"
  addressee: learner
  verbs: ["synthesise"]
  about: "drawing together what is known on a topic"
  themes: [none]
  domain: generic-skill
  award: ["bachelor's with honours"]
  gradeOf: none
  paraphrase: "At the honours threshold, graduates should be able to pull together the current state of knowledge on a given topic."
  quote: full   # the issuer's statement is in `source` (D-std-0014)
  audience: both
  subjects: inherited
- id: qaa/librarianship-information-knowledge-records-and-archives-management-2025/4.8.b6
  locator: { number: "4.8.b6", headingPath: ["Benchmark standards", "Generic skills"] }
  span: { start: 55582, end: 55648 }
  source: "apply knowledge and understanding to provide evidenced conclusions"
  stem: "4.8"
  statementType: threshold
  rung: threshold
  force: should
  level: fheq:6
  appliesTo: "honours graduates at the threshold"
  addressee: learner
  verbs: ["apply", "provide"]
  about: "reaching conclusions backed by evidence"
  themes: [none]
  domain: generic-skill
  award: ["bachelor's with honours"]
  gradeOf: none
  paraphrase: "At the honours threshold, graduates should be able to use knowledge and understanding to reach conclusions supported by evidence."
  quote: full   # the issuer's statement is in `source` (D-std-0014)
  audience: both
  subjects: inherited
- id: qaa/librarianship-information-knowledge-records-and-archives-management-2025/4.8.b7
  locator: { number: "4.8.b7", headingPath: ["Benchmark standards", "Generic skills"] }
  span: { start: 55651, end: 55721 }
  source: "communicate effectively and appropriately verbally and/or non-verbally"
  stem: "4.8"
  statementType: threshold
  rung: threshold
  force: should
  level: fheq:6
  appliesTo: "honours graduates at the threshold"
  addressee: learner
  verbs: ["communicate"]
  about: "communicating effectively"
  themes: [none]
  domain: generic-skill
  award: ["bachelor's with honours"]
  gradeOf: none
  paraphrase: "At the honours threshold, graduates should be able to communicate well and fittingly, in speech and in other forms."
  quote: full   # the issuer's statement is in `source` (D-std-0014)
  audience: both
  subjects: inherited
- id: qaa/librarianship-information-knowledge-records-and-archives-management-2025/4.8.b8
  locator: { number: "4.8.b8", headingPath: ["Benchmark standards", "Generic skills"] }
  span: { start: 55724, end: 55798 }
  source: "present knowledge or an argument in a way that is comprehensible to others"
  stem: "4.8"
  statementType: threshold
  rung: threshold
  force: should
  level: fheq:6
  appliesTo: "honours graduates at the threshold"
  addressee: learner
  verbs: ["present"]
  about: "presenting knowledge or argument clearly"
  themes: [none]
  domain: generic-skill
  award: ["bachelor's with honours"]
  gradeOf: none
  paraphrase: "At the honours threshold, graduates should be able to set out knowledge or an argument so that others can follow it."
  quote: full   # the issuer's statement is in `source` (D-std-0014)
  audience: both
  subjects: inherited
- id: qaa/librarianship-information-knowledge-records-and-archives-management-2025/4.8.b9
  locator: { number: "4.8.b9", headingPath: ["Benchmark standards", "Generic skills"] }
  span: { start: 55801, end: 55881 }
  source: "work with a range of data, including qualitative and quantitative empirical data"
  stem: "4.8"
  statementType: threshold
  rung: threshold
  force: should
  level: fheq:6
  appliesTo: "honours graduates at the threshold"
  addressee: learner
  verbs: ["work"]
  about: "working with qualitative and quantitative data"
  themes: [none]
  domain: generic-skill
  award: ["bachelor's with honours"]
  gradeOf: none
  paraphrase: "At the honours threshold, graduates should be able to handle varied data, empirical qualitative and quantitative data included."
  quote: full   # the issuer's statement is in `source` (D-std-0014)
  audience: both
  subjects: inherited
- id: qaa/librarianship-information-knowledge-records-and-archives-management-2025/4.8.b10
  locator: { number: "4.8.b10", headingPath: ["Benchmark standards", "Generic skills"] }
  span: { start: 55884, end: 55997 }
  source: "critically engage with a range of forms of digital technology to collate, analyse, select and present information"
  stem: "4.8"
  statementType: threshold
  rung: threshold
  force: should
  level: fheq:6
  appliesTo: "honours graduates at the threshold"
  addressee: learner
  verbs: ["engage", "collate", "analyse", "select", "present"]
  about: "critical use of digital technology"
  themes: [none]
  domain: generic-skill
  award: ["bachelor's with honours"]
  gradeOf: none
  paraphrase: "At the honours threshold, graduates should be able to use a range of digital technologies critically to gather, analyse, choose and present information."
  quote: full   # the issuer's statement is in `source` (D-std-0014)
  audience: both
  subjects: inherited
- id: qaa/librarianship-information-knowledge-records-and-archives-management-2025/4.8.b11
  locator: { number: "4.8.b11", headingPath: ["Benchmark standards", "Generic skills"] }
  span: { start: 56000, end: 56187 }
  source: "assert intellectual independence, including undertaking tasks independently (with appropriate guidance and support), conducting self-directed research and demonstrating critical judgement"
  stem: "4.8"
  statementType: threshold
  rung: threshold
  force: should
  level: fheq:6
  appliesTo: "honours graduates at the threshold"
  addressee: learner
  verbs: ["assert", "undertaking", "conducting", "demonstrating"]
  about: "intellectual independence"
  themes: [none]
  domain: generic-skill
  award: ["bachelor's with honours"]
  gradeOf: none
  paraphrase: "At the honours threshold, graduates should be able to show intellectual independence: working on tasks alone with suitable support, running their own research and exercising critical judgement."
  quote: full   # the issuer's statement is in `source` (D-std-0014)
  audience: both
  subjects: inherited
- id: qaa/librarianship-information-knowledge-records-and-archives-management-2025/4.8.b12
  locator: { number: "4.8.b12", headingPath: ["Benchmark standards", "Generic skills"] }
  span: { start: 56190, end: 56293 }
  source: "work collaboratively, including undertaking work in a group or team and/or participating in discussions"
  stem: "4.8"
  statementType: threshold
  rung: threshold
  force: should
  level: fheq:6
  appliesTo: "honours graduates at the threshold"
  addressee: learner
  verbs: ["work", "undertaking", "participating"]
  about: "working with others"
  themes: [none]
  domain: generic-skill
  award: ["bachelor's with honours"]
  gradeOf: none
  paraphrase: "At the honours threshold, graduates should be able to work with others, in a group or team or by taking part in discussion."
  quote: full   # the issuer's statement is in `source` (D-std-0014)
  audience: both
  subjects: inherited
- id: qaa/librarianship-information-knowledge-records-and-archives-management-2025/4.8.b13
  locator: { number: "4.8.b13", headingPath: ["Benchmark standards", "Generic skills"] }
  span: { start: 56296, end: 56363 }
  source: "reflect on their own progress, including personal leadership skills"
  stem: "4.8"
  statementType: threshold
  rung: threshold
  force: should
  level: fheq:6
  appliesTo: "honours graduates at the threshold"
  addressee: learner
  verbs: ["reflect"]
  about: "reflecting on progress and personal leadership"
  themes: [none]
  domain: generic-skill
  award: ["bachelor's with honours"]
  gradeOf: none
  paraphrase: "At the honours threshold, graduates should be able to look back on their own progress, their personal leadership skills among it."
  quote: full   # the issuer's statement is in `source` (D-std-0014)
  audience: both
  subjects: inherited
- id: qaa/librarianship-information-knowledge-records-and-archives-management-2025/4.8.b14
  locator: { number: "4.8.b14", headingPath: ["Benchmark standards", "Generic skills"] }
  span: { start: 56366, end: 56466 }
  source: "identify and examine underlying values and ethics within culture and society and on a personal level"
  stem: "4.8"
  statementType: threshold
  rung: threshold
  force: should
  level: fheq:6
  appliesTo: "honours graduates at the threshold"
  addressee: learner
  verbs: ["identify", "examine"]
  about: "examining values and ethics"
  themes: [none]
  domain: generic-skill
  award: ["bachelor's with honours"]
  gradeOf: none
  paraphrase: "At the honours threshold, graduates should be able to recognise and examine the values and ethics beneath culture, society and their own conduct."
  quote: full   # the issuer's statement is in `source` (D-std-0014)
  audience: both
  subjects: inherited
- id: qaa/librarianship-information-knowledge-records-and-archives-management-2025/4.8.b15
  locator: { number: "4.8.b15", headingPath: ["Benchmark standards", "Generic skills"] }
  span: { start: 56469, end: 56573 }
  source: "understand the importance of well-being, mental health and emotions and their relationship with learning"
  stem: "4.8"
  statementType: threshold
  rung: threshold
  force: should
  level: fheq:6
  appliesTo: "honours graduates at the threshold"
  addressee: learner
  verbs: ["understand"]
  about: "well-being, emotion and learning"
  themes: [none]
  domain: generic-skill
  award: ["bachelor's with honours"]
  gradeOf: none
  paraphrase: "At the honours threshold, graduates should be able to understand why well-being, mental health and emotion matter and how they bear on learning."
  quote: full   # the issuer's statement is in `source` (D-std-0014)
  audience: both
  subjects: inherited
- id: qaa/librarianship-information-knowledge-records-and-archives-management-2025/4.8.b16
  locator: { number: "4.8.b16", headingPath: ["Benchmark standards", "Generic skills"] }
  span: { start: 56576, end: 56659 }
  source: "make appropriate use of feedback provided to further their intellectual development"
  stem: "4.8"
  statementType: threshold
  rung: threshold
  force: should
  level: fheq:6
  appliesTo: "honours graduates at the threshold"
  addressee: learner
  verbs: ["make"]
  about: "using feedback to develop"
  themes: [none]
  domain: generic-skill
  award: ["bachelor's with honours"]
  gradeOf: none
  paraphrase: "At the honours threshold, graduates should be able to use the feedback they receive well, to take their thinking further."
  quote: full   # the issuer's statement is in `source` (D-std-0014)
  audience: both
  subjects: inherited
- id: qaa/librarianship-information-knowledge-records-and-archives-management-2025/4.8.b17
  locator: { number: "4.8.b17", headingPath: ["Benchmark standards", "Generic skills"] }
  span: { start: 56662, end: 56790 }
  source: "appreciate and engage in contemporary debates relating to culture and society, for example around inequality and sustainability."
  stem: "4.8"
  statementType: threshold
  rung: threshold
  force: should
  level: fheq:6
  appliesTo: "honours graduates at the threshold"
  addressee: learner
  verbs: ["appreciate", "engage"]
  about: "current debates on culture and society"
  themes: [none]
  domain: generic-skill
  award: ["bachelor's with honours"]
  gradeOf: none
  paraphrase: "At the honours threshold, graduates should be able to value and join current debates on culture and society, such as those on inequality and sustainability."
  quote: full   # the issuer's statement is in `source` (D-std-0014)
  audience: both
  subjects: inherited
- id: qaa/librarianship-information-knowledge-records-and-archives-management-2025/4.9.b1
  locator: { number: "4.9.b1", headingPath: ["Benchmark standards", "Master's degree in Librarianship, Information, Knowledge, Records and Archive Management"] }
  span: { start: 57197, end: 57311 }
  source: "emphasise a deeper understanding of complex issues and the ability to engage with current research and scholarship"
  stem: "4.9"
  statementType: threshold
  rung: threshold
  force: describes
  level: fheq:7
  appliesTo: "graduates of postgraduate certificates, diplomas and master's degrees"
  addressee: learner
  verbs: ["emphasise", "engage"]
  about: "deeper understanding and engagement with research"
  themes: [none]
  domain: understanding
  award: ["master's", "postgraduate diploma", "postgraduate certificate"]
  gradeOf: none
  paraphrase: "Postgraduate study involves advanced ideas that call for a deeper grasp of complex issues and the ability to work with current research and scholarship."
  quote: full   # the issuer's statement is in `source` (D-std-0014)
  audience: both
  subjects: inherited
- id: qaa/librarianship-information-knowledge-records-and-archives-management-2025/4.9.b2
  locator: { number: "4.9.b2", headingPath: ["Benchmark standards", "Master's degree in Librarianship, Information, Knowledge, Records and Archive Management"] }
  span: { start: 57314, end: 57434 }
  source: "highlight the ability to apply knowledge in real-world scenarios that may be ill-defined or require innovative solutions"
  stem: "4.9"
  statementType: threshold
  rung: threshold
  force: describes
  level: fheq:7
  appliesTo: "graduates of postgraduate certificates, diplomas and master's degrees"
  addressee: learner
  verbs: ["highlight", "apply"]
  about: "applying knowledge where problems are ill-defined"
  themes: [none]
  domain: subject-skill
  award: ["master's", "postgraduate diploma", "postgraduate certificate"]
  gradeOf: none
  paraphrase: "Postgraduate study involves advanced ideas that bring out the ability to use knowledge in real situations that are loosely defined or need new solutions."
  quote: full   # the issuer's statement is in `source` (D-std-0014)
  audience: both
  subjects: inherited
- id: qaa/librarianship-information-knowledge-records-and-archives-management-2025/4.9.b3
  locator: { number: "4.9.b3", headingPath: ["Benchmark standards", "Master's degree in Librarianship, Information, Knowledge, Records and Archive Management"] }
  span: { start: 57437, end: 57536 }
  source: "stress the ability to conduct original research, evaluate methodologies, and propose new hypotheses"
  stem: "4.9"
  statementType: threshold
  rung: threshold
  force: describes
  level: fheq:7
  appliesTo: "graduates of postgraduate certificates, diplomas and master's degrees"
  addressee: learner
  verbs: ["stress", "conduct", "evaluate", "propose"]
  about: "original research and new hypotheses"
  themes: [none]
  domain: generic-skill
  award: ["master's", "postgraduate diploma", "postgraduate certificate"]
  gradeOf: none
  paraphrase: "Postgraduate study involves advanced ideas that put weight on doing original research, judging methods and putting forward new hypotheses."
  quote: full   # the issuer's statement is in `source` (D-std-0014)
  audience: both
  subjects: inherited
- id: qaa/librarianship-information-knowledge-records-and-archives-management-2025/4.9.b4
  locator: { number: "4.9.b4", headingPath: ["Benchmark standards", "Master's degree in Librarianship, Information, Knowledge, Records and Archive Management"] }
  span: { start: 57539, end: 57675 }
  source: "focus on the ability to lead and influence change, advocate for ethical practices and develop strategic solutions to complex challenges."
  stem: "4.9"
  statementType: threshold
  rung: threshold
  force: describes
  level: fheq:7
  appliesTo: "graduates of postgraduate certificates, diplomas and master's degrees"
  addressee: learner
  verbs: ["focus", "lead", "influence", "advocate", "develop"]
  about: "leading change and strategic solutions"
  themes: [none]
  domain: generic-skill
  award: ["master's", "postgraduate diploma", "postgraduate certificate"]
  gradeOf: none
  paraphrase: "Postgraduate study involves advanced ideas centred on leading and shaping change, arguing for ethical practice and devising strategic answers to complex problems."
  quote: full   # the issuer's statement is in `source` (D-std-0014)
  audience: both
  subjects: inherited
- id: qaa/librarianship-information-knowledge-records-and-archives-management-2025/4.10.s1
  locator: { number: "4.10.s1", headingPath: ["Benchmark standards", "Master's degree in Librarianship, Information, Knowledge, Records and Archive Management"] }
  span: { start: 57681, end: 57971 }
  source: "Given the diverse routes into this profession, including postgraduate qualification of those with undergraduate degrees in different disciplines, students should be expected to demonstrate a systematic and comprehensive understanding of the main body of knowledge for their course of study."
  stem: none
  statementType: threshold
  rung: threshold
  force: should
  level: fheq:7
  appliesTo: "graduates of postgraduate certificates, diplomas and master's degrees"
  addressee: learner
  verbs: ["demonstrate"]
  about: "systematic and comprehensive core knowledge"
  themes: [none]
  domain: knowledge
  award: ["master's", "postgraduate diploma", "postgraduate certificate"]
  gradeOf: none
  paraphrase: "Because many enter the profession through postgraduate study after a first degree in another field, master's students should show a systematic and comprehensive grasp of their course's central knowledge."
  quote: full   # the issuer's statement is in `source` (D-std-0014)
  audience: both
  subjects: inherited
- id: qaa/librarianship-information-knowledge-records-and-archives-management-2025/4.10.s2
  locator: { number: "4.10.s2", headingPath: ["Benchmark standards", "Master's degree in Librarianship, Information, Knowledge, Records and Archive Management"] }
  span: { start: 57972, end: 58220 }
  source: "They should be able to critically analyse and apply essential concepts, principles and practices of the subject in complex and diverse scenarios, demonstrating sound judgement in the selection and application of processes, materials and techniques."
  stem: none
  statementType: threshold
  rung: threshold
  force: should
  level: fheq:7
  appliesTo: "graduates of postgraduate certificates, diplomas and master's degrees"
  addressee: learner
  verbs: ["analyse", "apply", "demonstrating"]
  about: "critical application in complex, varied cases"
  themes: [none]
  domain: subject-skill
  award: ["master's", "postgraduate diploma", "postgraduate certificate"]
  gradeOf: none
  paraphrase: "Master's students should be able to analyse critically and use the subject's key concepts, principles and practices in complex and varied situations, choosing methods and materials with sound judgement."
  quote: full   # the issuer's statement is in `source` (D-std-0014)
  audience: both
  subjects: inherited
- id: qaa/librarianship-information-knowledge-records-and-archives-management-2025/4.10.s3
  locator: { number: "4.10.s3", headingPath: ["Benchmark standards", "Master's degree in Librarianship, Information, Knowledge, Records and Archive Management"] }
  span: { start: 58221, end: 58441 }
  source: "At master's level, students may also be asked to demonstrate skills and understanding in relation to strategic thinking and leadership, as well as the ability to undertake original research to a higher academic standard."
  stem: none
  statementType: expectation
  rung: none
  force: may
  level: fheq:7
  appliesTo: "master's students"
  addressee: learner
  verbs: ["asked", "demonstrate", "undertake"]
  about: "strategic thinking, leadership and original research"
  themes: [none]
  domain: generic-skill
  award: ["master's", "postgraduate diploma", "postgraduate certificate"]
  gradeOf: none
  paraphrase: "Master's students may also have to show skill and understanding in strategic thinking and leadership, and the ability to carry out original research to a higher academic standard."
  quote: full   # the issuer's statement is in `source` (D-std-0014)
  audience: both
  subjects: inherited
- id: qaa/librarianship-information-knowledge-records-and-archives-management-2025/4.11.b1
  locator: { number: "4.11.b1", headingPath: ["Benchmark standards", "Subject knowledge, understanding and skills (master's)"] }
  span: { start: 58832, end: 59080 }
  source: "demonstrate a nuanced understanding of the specific information needs and resources relevant to diverse disciplines and professional fields, such as science, technology, engineering and mathematics (STEM), law, business, and the arts and humanities"
  stem: "4.11"
  statementType: threshold
  rung: threshold
  force: will
  level: fheq:7
  appliesTo: "master's graduates at the threshold"
  addressee: learner
  verbs: ["demonstrate"]
  about: "information needs across disciplines and fields"
  themes: [none]
  domain: understanding
  award: ["master's", "postgraduate diploma", "postgraduate certificate"]
  gradeOf: none
  paraphrase: "At the master's threshold, graduates will have shown the ability to understand, with nuance, the particular information needs and sources of different disciplines and professions, such as STEM, law, business and the arts and humanities."
  quote: full   # the issuer's statement is in `source` (D-std-0014)
  audience: both
  subjects: inherited
- id: qaa/librarianship-information-knowledge-records-and-archives-management-2025/4.11.s1
  locator: { number: "4.11.s1", headingPath: ["Benchmark standards", "Subject knowledge, understanding and skills (master's)"] }
  span: { start: 58447, end: 58620 }
  source: "At master's level, graduates at a threshold level of attainment will have demonstrated some degree of proficiency in the majority of the attributes listed in this Statement."
  stem: none
  statementType: threshold
  rung: threshold
  force: will
  level: fheq:7
  appliesTo: "graduates of postgraduate certificates, diplomas and master's degrees"
  addressee: learner
  verbs: ["demonstrated"]
  about: "what the master's threshold means"
  themes: [none]
  domain: none
  award: ["master's", "postgraduate diploma", "postgraduate certificate"]
  gradeOf: none
  paraphrase: "Master's graduates at the threshold will have shown some proficiency in most, not all, of the listed attributes."
  quote: full   # the issuer's statement is in `source` (D-std-0014)
  audience: both
  subjects: inherited
- id: qaa/librarianship-information-knowledge-records-and-archives-management-2025/4.11.b2
  locator: { number: "4.11.b2", headingPath: ["Benchmark standards", "Subject knowledge, understanding and skills (master's)"] }
  span: { start: 59083, end: 59210 }
  source: "design and implement culturally responsive outreach, programming and services tailored to meet the needs of diverse communities"
  stem: "4.11"
  statementType: threshold
  rung: threshold
  force: will
  level: fheq:7
  appliesTo: "master's graduates at the threshold"
  addressee: learner
  verbs: ["design", "implement"]
  about: "culturally responsive outreach and services"
  themes: [none]
  domain: subject-skill
  award: ["master's", "postgraduate diploma", "postgraduate certificate"]
  gradeOf: none
  paraphrase: "At the master's threshold, graduates will have shown the ability to design and deliver outreach, programmes and services that respond to culture and fit the needs of diverse communities."
  quote: full   # the issuer's statement is in `source` (D-std-0014)
  audience: both
  subjects: inherited
- id: qaa/librarianship-information-knowledge-records-and-archives-management-2025/4.11.b3
  locator: { number: "4.11.b3", headingPath: ["Benchmark standards", "Subject knowledge, understanding and skills (master's)"] }
  span: { start: 59213, end: 59340 }
  source: "create inclusive physical and digital library spaces and collections that cater to individuals with varying abilities and needs"
  stem: "4.11"
  statementType: threshold
  rung: threshold
  force: will
  level: fheq:7
  appliesTo: "master's graduates at the threshold"
  addressee: learner
  verbs: ["create", "cater"]
  about: "inclusive physical and online spaces and collections"
  themes: [none]
  domain: subject-skill
  award: ["master's", "postgraduate diploma", "postgraduate certificate"]
  gradeOf: none
  paraphrase: "At the master's threshold, graduates will have shown the ability to shape library spaces and collections, in person and online, so that they serve people with a wide spread of abilities and needs."
  quote: full   # the issuer's statement is in `source` (D-std-0014)
  audience: both
  subjects: inherited
- id: qaa/librarianship-information-knowledge-records-and-archives-management-2025/4.11.b4
  locator: { number: "4.11.b4", headingPath: ["Benchmark standards", "Subject knowledge, understanding and skills (master's)"] }
  span: { start: 59343, end: 59509 }
  source: "partner with community organisations and educators to promote a range of literacies, including academic, data, digital, media and information, for marginalised groups"
  stem: "4.11"
  statementType: threshold
  rung: threshold
  force: will
  level: fheq:7
  appliesTo: "master's graduates at the threshold"
  addressee: learner
  verbs: ["partner", "promote"]
  about: "building literacies for marginalised groups"
  themes: [none]
  domain: subject-skill
  award: ["master's", "postgraduate diploma", "postgraduate certificate"]
  gradeOf: none
  paraphrase: "At the master's threshold, graduates will have shown the ability to work with community groups and teachers to advance academic, data, digital, media and information literacies among marginalised groups."
  quote: full   # the issuer's statement is in `source` (D-std-0014)
  audience: both
  subjects: inherited
- id: qaa/librarianship-information-knowledge-records-and-archives-management-2025/4.11.b5
  locator: { number: "4.11.b5", headingPath: ["Benchmark standards", "Subject knowledge, understanding and skills (master's)"] }
  span: { start: 59512, end: 59648 }
  source: "engage in critical discussions about decolonising information practices and confronting structural inequalities within knowledge systems"
  stem: "4.11"
  statementType: threshold
  rung: threshold
  force: will
  level: fheq:7
  appliesTo: "master's graduates at the threshold"
  addressee: learner
  verbs: ["engage", "confronting"]
  about: "decolonising information practice"
  themes: [none]
  domain: understanding
  award: ["master's", "postgraduate diploma", "postgraduate certificate"]
  gradeOf: none
  paraphrase: "At the master's threshold, graduates will have shown the ability to debate critically the decolonising of information practice and challenge structural inequality in knowledge systems."
  quote: full   # the issuer's statement is in `source` (D-std-0014)
  audience: both
  subjects: inherited
- id: qaa/librarianship-information-knowledge-records-and-archives-management-2025/4.11.b6
  locator: { number: "4.11.b6", headingPath: ["Benchmark standards", "Subject knowledge, understanding and skills (master's)"] }
  span: { start: 59651, end: 59831 }
  source: "develop retention schedules and comprehensive preservation plans addressing both physical and digital assets, ensuring long-term accessibility and addressing format migration needs"
  stem: "4.11"
  statementType: threshold
  rung: threshold
  force: will
  level: fheq:7
  appliesTo: "master's graduates at the threshold"
  addressee: learner
  verbs: ["develop", "addressing", "ensuring"]
  about: "retention schedules and preservation plans"
  themes: [none]
  domain: subject-skill
  award: ["master's", "postgraduate diploma", "postgraduate certificate"]
  gradeOf: none
  paraphrase: "At the master's threshold, graduates will have shown the ability to draw up retention schedules and full preservation plans for physical and digital holdings that keep them usable for the long term and plan for format migration."
  quote: full   # the issuer's statement is in `source` (D-std-0014)
  audience: both
  subjects: inherited
- id: qaa/librarianship-information-knowledge-records-and-archives-management-2025/4.11.b7
  locator: { number: "4.11.b7", headingPath: ["Benchmark standards", "Subject knowledge, understanding and skills (master's)"] }
  span: { start: 59834, end: 59967 }
  source: "understand and apply appropriate archival principles, such as provenance and original order, when organising and describing materials"
  stem: "4.11"
  statementType: threshold
  rung: threshold
  force: will
  level: fheq:7
  appliesTo: "master's graduates at the threshold"
  addressee: learner
  verbs: ["understand", "apply"]
  about: "archival principles in arrangement and description"
  themes: [none]
  domain: understanding
  award: ["master's", "postgraduate diploma", "postgraduate certificate"]
  gradeOf: none
  paraphrase: "At the master's threshold, graduates will have shown the ability to understand archival principles such as provenance and original order and use them when arranging and describing collections."
  quote: full   # the issuer's statement is in `source` (D-std-0014)
  audience: both
  subjects: inherited
- id: qaa/librarianship-information-knowledge-records-and-archives-management-2025/4.11.b8
  locator: { number: "4.11.b8", headingPath: ["Benchmark standards", "Subject knowledge, understanding and skills (master's)"] }
  span: { start: 59974, end: 60080 }
  source: "implement disaster preparedness measures, including risk assessments, backup strategies and recovery plans"
  stem: "4.11"
  statementType: threshold
  rung: threshold
  force: will
  level: fheq:7
  appliesTo: "master's graduates at the threshold"
  addressee: learner
  verbs: ["implement"]
  about: "disaster preparedness and recovery"
  themes: [none]
  domain: subject-skill
  award: ["master's", "postgraduate diploma", "postgraduate certificate"]
  gradeOf: none
  paraphrase: "At the master's threshold, graduates will have shown the ability to put in place disaster preparedness, with risk assessment, backup strategies and recovery plans."
  quote: full   # the issuer's statement is in `source` (D-std-0014)
  audience: both
  subjects: inherited
- id: qaa/librarianship-information-knowledge-records-and-archives-management-2025/4.11.b9
  locator: { number: "4.11.b9", headingPath: ["Benchmark standards", "Subject knowledge, understanding and skills (master's)"] }
  span: { start: 60083, end: 60223 }
  source: "adhere to industry standards for the storage of fragile or sensitive materials, ensuring proper environmental controls and security measures"
  stem: "4.11"
  statementType: threshold
  rung: threshold
  force: will
  level: fheq:7
  appliesTo: "master's graduates at the threshold"
  addressee: learner
  verbs: ["adhere", "ensuring"]
  about: "storage standards for fragile or sensitive items"
  themes: [none]
  domain: subject-skill
  award: ["master's", "postgraduate diploma", "postgraduate certificate"]
  gradeOf: none
  paraphrase: "At the master's threshold, graduates will have shown the ability to follow the sector's standards for keeping fragile or sensitive items, with the right environmental conditions and security."
  quote: full   # the issuer's statement is in `source` (D-std-0014)
  audience: both
  subjects: inherited
- id: qaa/librarianship-information-knowledge-records-and-archives-management-2025/4.11.b10
  locator: { number: "4.11.b10", headingPath: ["Benchmark standards", "Subject knowledge, understanding and skills (master's)"] }
  span: { start: 60226, end: 60386 }
  source: "master cataloguing and classification, description, and metadata creation and application using controlled vocabularies and standards to enhance discoverability"
  stem: "4.11"
  statementType: threshold
  rung: threshold
  force: will
  level: fheq:7
  appliesTo: "master's graduates at the threshold"
  addressee: learner
  verbs: ["master", "enhance"]
  about: "cataloguing, classification and metadata"
  themes: [none]
  domain: subject-skill
  award: ["master's", "postgraduate diploma", "postgraduate certificate"]
  gradeOf: none
  paraphrase: "At the master's threshold, graduates will have shown the ability to command cataloguing, classification, description and metadata work securely, using controlled vocabularies and standards so resources are easier to find."
  quote: full   # the issuer's statement is in `source` (D-std-0014)
  audience: both
  subjects: inherited
- id: qaa/librarianship-information-knowledge-records-and-archives-management-2025/4.11.b11
  locator: { number: "4.11.b11", headingPath: ["Benchmark standards", "Subject knowledge, understanding and skills (master's)"] }
  span: { start: 60389, end: 60514 }
  source: "design and manage content management systems, digital repositories and web platforms adhering to accessibility best practices"
  stem: "4.11"
  statementType: threshold
  rung: threshold
  force: will
  level: fheq:7
  appliesTo: "master's graduates at the threshold"
  addressee: learner
  verbs: ["design", "manage", "adhering"]
  about: "content systems, repositories and web platforms"
  themes: [none]
  domain: subject-skill
  award: ["master's", "postgraduate diploma", "postgraduate certificate"]
  gradeOf: none
  paraphrase: "At the master's threshold, graduates will have shown the ability to design and run content management systems, digital repositories and web platforms in line with good accessibility practice."
  quote: full   # the issuer's statement is in `source` (D-std-0014)
  audience: both
  subjects: inherited
- id: qaa/librarianship-information-knowledge-records-and-archives-management-2025/4.11.b12
  locator: { number: "4.11.b12", headingPath: ["Benchmark standards", "Subject knowledge, understanding and skills (master's)"] }
  span: { start: 60517, end: 60665 }
  source: "implement user-centred design principles and accessibility guidelines to create intuitive and inclusive interfaces for online resources and services"
  stem: "4.11"
  statementType: threshold
  rung: threshold
  force: will
  level: fheq:7
  appliesTo: "master's graduates at the threshold"
  addressee: learner
  verbs: ["implement", "create"]
  about: "user-centred, accessible interface design"
  themes: [none]
  domain: subject-skill
  award: ["master's", "postgraduate diploma", "postgraduate certificate"]
  gradeOf: none
  paraphrase: "At the master's threshold, graduates will have shown the ability to apply user-centred design and accessibility guidance so that online resources and services are intuitive and inclusive to use."
  quote: full   # the issuer's statement is in `source` (D-std-0014)
  audience: both
  subjects: inherited
- id: qaa/librarianship-information-knowledge-records-and-archives-management-2025/4.11.b13
  locator: { number: "4.11.b13", headingPath: ["Benchmark standards", "Subject knowledge, understanding and skills (master's)"] }
  span: { start: 60668, end: 60786 }
  source: "critically evaluate and apply emerging technologies for information management tasks, considering ethical implications"
  stem: "4.11"
  statementType: threshold
  rung: threshold
  force: will
  level: fheq:7
  appliesTo: "master's graduates at the threshold"
  addressee: learner
  verbs: ["evaluate", "apply", "considering"]
  about: "judging new technologies ethically"
  themes: [none]
  domain: subject-skill
  award: ["master's", "postgraduate diploma", "postgraduate certificate"]
  gradeOf: none
  paraphrase: "At the master's threshold, graduates will have shown the ability to appraise new technologies for managing information critically and put them to use, weighing their ethical consequences."
  quote: full   # the issuer's statement is in `source` (D-std-0014)
  audience: both
  subjects: inherited
- id: qaa/librarianship-information-knowledge-records-and-archives-management-2025/4.11.b14
  locator: { number: "4.11.b14", headingPath: ["Benchmark standards", "Subject knowledge, understanding and skills (master's)"] }
  span: { start: 60789, end: 61024 }
  source: "collaborate with educators and community partners to develop comprehensive information literacy and reader development programmes that address a range of skill levels and needs, including those of children, adults and lifelong learners"
  stem: "4.11"
  statementType: threshold
  rung: threshold
  force: will
  level: fheq:7
  appliesTo: "master's graduates at the threshold"
  addressee: learner
  verbs: ["collaborate", "develop", "address"]
  about: "information literacy and reader development programmes"
  themes: [none]
  domain: subject-skill
  award: ["master's", "postgraduate diploma", "postgraduate certificate"]
  gradeOf: none
  paraphrase: "At the master's threshold, graduates will have shown the ability to build, with teaching staff and community partners, full information literacy and reader development programmes for varied levels of skill and need, children, adults and lifelong learners included."
  quote: full   # the issuer's statement is in `source` (D-std-0014)
  audience: both
  subjects: inherited
- id: qaa/librarianship-information-knowledge-records-and-archives-management-2025/4.11.b15
  locator: { number: "4.11.b15", headingPath: ["Benchmark standards", "Subject knowledge, understanding and skills (master's)"] }
  span: { start: 61027, end: 61158 }
  source: "adapt critical information literacy instruction to the needs of diverse audiences, including children, adults and lifelong learners"
  stem: "4.11"
  statementType: threshold
  rung: threshold
  force: will
  level: fheq:7
  appliesTo: "master's graduates at the threshold"
  addressee: learner
  verbs: ["adapt"]
  about: "critical information literacy for varied audiences"
  themes: [none]
  domain: subject-skill
  award: ["master's", "postgraduate diploma", "postgraduate certificate"]
  gradeOf: none
  paraphrase: "At the master's threshold, graduates will have shown the ability to adjust critical information literacy teaching to what different audiences need, children, adults and lifelong learners among them."
  quote: full   # the issuer's statement is in `source` (D-std-0014)
  audience: both
  subjects: inherited
- id: qaa/librarianship-information-knowledge-records-and-archives-management-2025/4.11.b16
  locator: { number: "4.11.b16", headingPath: ["Benchmark standards", "Subject knowledge, understanding and skills (master's)"] }
  span: { start: 61161, end: 61297 }
  source: "design instruction and outreach activities that foster critical thinking, media literacy, and safe and responsible digital participation"
  stem: "4.11"
  statementType: threshold
  rung: threshold
  force: will
  level: fheq:7
  appliesTo: "master's graduates at the threshold"
  addressee: learner
  verbs: ["design", "foster"]
  about: "teaching and outreach for critical thinking"
  themes: [none]
  domain: subject-skill
  award: ["master's", "postgraduate diploma", "postgraduate certificate"]
  gradeOf: none
  paraphrase: "At the master's threshold, graduates will have shown the ability to plan teaching and outreach that build critical thinking, media literacy and safe, responsible participation online."
  quote: full   # the issuer's statement is in `source` (D-std-0014)
  audience: both
  subjects: inherited
- id: qaa/librarianship-information-knowledge-records-and-archives-management-2025/4.11.b17
  locator: { number: "4.11.b17", headingPath: ["Benchmark standards", "Subject knowledge, understanding and skills (master's)"] }
  span: { start: 61300, end: 61435 }
  source: "collect and analyse user data, service metrics and industry trends to inform evidence- based decision-making and continuous improvement"
  stem: "4.11"
  statementType: threshold
  rung: threshold
  force: will
  level: fheq:7
  appliesTo: "master's graduates at the threshold"
  addressee: learner
  verbs: ["collect", "analyse", "inform"]
  about: "user data and metrics for evidence-based improvement"
  themes: [none]
  domain: subject-skill
  award: ["master's", "postgraduate diploma", "postgraduate certificate"]
  gradeOf: none
  paraphrase: "At the master's threshold, graduates will have shown the ability to gather and analyse data on users, service performance and sector trends, and use it to ground decisions in evidence and keep improving."
  quote: full   # the issuer's statement is in `source` (D-std-0014)
  audience: both
  subjects: inherited
- id: qaa/librarianship-information-knowledge-records-and-archives-management-2025/4.11.b18
  locator: { number: "4.11.b18", headingPath: ["Benchmark standards", "Subject knowledge, understanding and skills (master's)"] }
  span: { start: 61438, end: 61553 }
  source: "foster a culture of experimentation, exploring how new technologies and approaches can enhance information services"
  stem: "4.11"
  statementType: threshold
  rung: threshold
  force: will
  level: fheq:7
  appliesTo: "master's graduates at the threshold"
  addressee: learner
  verbs: ["foster", "exploring", "enhance"]
  about: "a culture of experiment in services"
  themes: [none]
  domain: subject-skill
  award: ["master's", "postgraduate diploma", "postgraduate certificate"]
  gradeOf: none
  paraphrase: "At the master's threshold, graduates will have shown the ability to build a habit of experiment, testing how new technologies and approaches could improve information services."
  quote: full   # the issuer's statement is in `source` (D-std-0014)
  audience: both
  subjects: inherited
- id: qaa/librarianship-information-knowledge-records-and-archives-management-2025/4.11.b19
  locator: { number: "4.11.b19", headingPath: ["Benchmark standards", "Subject knowledge, understanding and skills (master's)"] }
  span: { start: 61556, end: 61680 }
  source: "proactively identify opportunities for entrepreneurship, developing new information- based products, services or enterprises"
  stem: "4.11"
  statementType: threshold
  rung: threshold
  force: will
  level: fheq:7
  appliesTo: "master's graduates at the threshold"
  addressee: learner
  verbs: ["identify", "developing"]
  about: "spotting openings for enterprise"
  themes: [none]
  domain: subject-skill
  award: ["master's", "postgraduate diploma", "postgraduate certificate"]
  gradeOf: none
  paraphrase: "At the master's threshold, graduates will have shown the ability to look actively for chances to be entrepreneurial, creating new information products, services or ventures."
  quote: full   # the issuer's statement is in `source` (D-std-0014)
  audience: both
  subjects: inherited
- id: qaa/librarianship-information-knowledge-records-and-archives-management-2025/4.11.b20
  locator: { number: "4.11.b20", headingPath: ["Benchmark standards", "Subject knowledge, understanding and skills (master's)"] }
  span: { start: 61683, end: 61807 }
  source: "explore the use of AI tools for automated tasks like metadata generation and recommender systems, ensuring ethical oversight"
  stem: "4.11"
  statementType: threshold
  rung: threshold
  force: will
  level: fheq:7
  appliesTo: "master's graduates at the threshold"
  addressee: learner
  verbs: ["explore", "ensuring"]
  about: "AI tools for automated tasks, with ethical oversight"
  themes: [none]
  domain: subject-skill
  award: ["master's", "postgraduate diploma", "postgraduate certificate"]
  gradeOf: none
  paraphrase: "At the master's threshold, graduates will have shown the ability to try out AI tools for automated work such as metadata generation and recommender systems, keeping ethical oversight in place."
  quote: full   # the issuer's statement is in `source` (D-std-0014)
  audience: both
  subjects: inherited
- id: qaa/librarianship-information-knowledge-records-and-archives-management-2025/4.11.b21
  locator: { number: "4.11.b21", headingPath: ["Benchmark standards", "Subject knowledge, understanding and skills (master's)"] }
  span: { start: 61810, end: 61893 }
  source: "champion intellectual freedom, data privacy and open access to information and data"
  stem: "4.11"
  statementType: threshold
  rung: threshold
  force: will
  level: fheq:7
  appliesTo: "master's graduates at the threshold"
  addressee: learner
  verbs: ["champion"]
  about: "intellectual freedom, privacy and openness"
  themes: [none]
  domain: subject-skill
  award: ["master's", "postgraduate diploma", "postgraduate certificate"]
  gradeOf: none
  paraphrase: "At the master's threshold, graduates will have shown the ability to stand up for freedom of thought and expression, for the privacy of personal data, and for open access to information and data."
  quote: full   # the issuer's statement is in `source` (D-std-0014)
  audience: both
  subjects: inherited
- id: qaa/librarianship-information-knowledge-records-and-archives-management-2025/4.11.b22
  locator: { number: "4.11.b22", headingPath: ["Benchmark standards", "Subject knowledge, understanding and skills (master's)"] }
  span: { start: 61896, end: 62041 }
  source: "participate in the development of organisational policies that address ethical information practices, responsible data governance and user rights"
  stem: "4.11"
  statementType: threshold
  rung: threshold
  force: will
  level: fheq:7
  appliesTo: "master's graduates at the threshold"
  addressee: learner
  verbs: ["participate", "address"]
  about: "organisational policy on information ethics"
  themes: [none]
  domain: subject-skill
  award: ["master's", "postgraduate diploma", "postgraduate certificate"]
  gradeOf: none
  paraphrase: "At the master's threshold, graduates will have shown the ability to help shape organisational policy on ethical information practice, responsible data governance and the rights of users."
  quote: full   # the issuer's statement is in `source` (D-std-0014)
  audience: both
  subjects: inherited
- id: qaa/librarianship-information-knowledge-records-and-archives-management-2025/4.11.b23
  locator: { number: "4.11.b23", headingPath: ["Benchmark standards", "Subject knowledge, understanding and skills (master's)"] }
  span: { start: 62044, end: 62186 }
  source: "engage in local and national advocacy efforts to support legislation that promotes equitable access to information and safeguards user privacy"
  stem: "4.11"
  statementType: threshold
  rung: threshold
  force: will
  level: fheq:7
  appliesTo: "master's graduates at the threshold"
  addressee: learner
  verbs: ["engage", "support"]
  about: "advocacy for fair access and privacy law"
  themes: [none]
  domain: subject-skill
  award: ["master's", "postgraduate diploma", "postgraduate certificate"]
  gradeOf: none
  paraphrase: "At the master's threshold, graduates will have shown the ability to take part in local and national campaigning for laws that widen fair access to information and protect users' privacy."
  quote: full   # the issuer's statement is in `source` (D-std-0014)
  audience: both
  subjects: inherited
- id: qaa/librarianship-information-knowledge-records-and-archives-management-2025/4.11.b24
  locator: { number: "4.11.b24", headingPath: ["Benchmark standards", "Subject knowledge, understanding and skills (master's)"] }
  span: { start: 62189, end: 62350 }
  source: "employ strategic analysis and leadership to implement, monitor and evaluate the success of initiatives and understand the impact on communities or users involved"
  stem: "4.11"
  statementType: threshold
  rung: threshold
  force: will
  level: fheq:7
  appliesTo: "master's graduates at the threshold"
  addressee: learner
  verbs: ["employ", "implement", "monitor", "evaluate", "understand"]
  about: "strategic leadership of initiatives"
  themes: [none]
  domain: subject-skill
  award: ["master's", "postgraduate diploma", "postgraduate certificate"]
  gradeOf: none
  paraphrase: "At the master's threshold, graduates will have shown the ability to use strategic analysis and leadership to deliver, track and judge initiatives and grasp their effect on the communities or users concerned."
  quote: full   # the issuer's statement is in `source` (D-std-0014)
  audience: both
  subjects: inherited
- id: qaa/librarianship-information-knowledge-records-and-archives-management-2025/4.11.b25
  locator: { number: "4.11.b25", headingPath: ["Benchmark standards", "Subject knowledge, understanding and skills (master's)"] }
  span: { start: 62353, end: 62424 }
  source: "use outcomes to inform the development of future services and outreach."
  stem: "4.11"
  statementType: threshold
  rung: threshold
  force: will
  level: fheq:7
  appliesTo: "master's graduates at the threshold"
  addressee: learner
  verbs: ["use", "inform"]
  about: "using results to plan future services"
  themes: [none]
  domain: subject-skill
  award: ["master's", "postgraduate diploma", "postgraduate certificate"]
  gradeOf: none
  paraphrase: "At the master's threshold, graduates will have shown the ability to draw on results to shape future services and outreach."
  quote: full   # the issuer's statement is in `source` (D-std-0014)
  audience: both
  subjects: inherited
- id: qaa/librarianship-information-knowledge-records-and-archives-management-2025/4.12.b1
  locator: { number: "4.12.b1", headingPath: ["Benchmark standards", "Generic skills (master's)"] }
  span: { start: 62598, end: 62799 }
  source: "a comprehensive understanding of techniques applicable to their own research or advanced scholarship, together with the ability to demonstrate use of appropriate research philosophies and methodologies"
  stem: "4.12"
  statementType: threshold
  rung: threshold
  force: should
  level: fheq:7
  appliesTo: "master's graduates at the threshold"
  addressee: learner
  verbs: ["demonstrate"]
  about: "research techniques and philosophies"
  themes: [none]
  domain: generic-skill
  award: ["master's", "postgraduate diploma", "postgraduate certificate"]
  gradeOf: none
  paraphrase: "Master's graduates should be able to show a full grasp of the research techniques their own research or advanced study needs, and a sound use of fitting research philosophies and methods."
  quote: full   # the issuer's statement is in `source` (D-std-0014)
  audience: both
  subjects: inherited
- id: qaa/librarianship-information-knowledge-records-and-archives-management-2025/4.12.b2
  locator: { number: "4.12.b2", headingPath: ["Benchmark standards", "Generic skills (master's)"] }
  span: { start: 62802, end: 62845 }
  source: "originality in the application of knowledge"
  stem: "4.12"
  statementType: threshold
  rung: threshold
  force: should
  level: fheq:7
  appliesTo: "master's graduates at the threshold"
  addressee: learner
  verbs: []
  about: "originality in applying knowledge"
  themes: [none]
  domain: generic-skill
  award: ["master's", "postgraduate diploma", "postgraduate certificate"]
  gradeOf: none
  paraphrase: "Master's graduates should be able to show originality in the way they put knowledge to use."
  quote: full   # the issuer's statement is in `source` (D-std-0014)
  audience: both
  subjects: inherited
- id: qaa/librarianship-information-knowledge-records-and-archives-management-2025/4.12.b3
  locator: { number: "4.12.b3", headingPath: ["Benchmark standards", "Generic skills (master's)"] }
  span: { start: 62852, end: 63007 }
  source: "a practical understanding of how established techniques of research and enquiry are used to create and evaluate evidence for enhanced professional practice"
  stem: "4.12"
  statementType: threshold
  rung: threshold
  force: should
  level: fheq:7
  appliesTo: "master's graduates at the threshold"
  addressee: learner
  verbs: ["used", "create", "evaluate"]
  about: "research as evidence for professional practice"
  themes: [none]
  domain: generic-skill
  award: ["master's", "postgraduate diploma", "postgraduate certificate"]
  gradeOf: none
  paraphrase: "Master's graduates should be able to show a working grasp of how established research and enquiry produce and test evidence that improves professional practice."
  quote: full   # the issuer's statement is in `source` (D-std-0014)
  audience: both
  subjects: inherited
- id: qaa/librarianship-information-knowledge-records-and-archives-management-2025/4.12.b4
  locator: { number: "4.12.b4", headingPath: ["Benchmark standards", "Generic skills (master's)"] }
  span: { start: 63010, end: 63252 }
  source: "an ability to complete through independent study a substantial, critical, empirical research or work-based project, significant review or case study that may also contribute to research in the subject or the solution of a work-related problem"
  stem: "4.12"
  statementType: threshold
  rung: threshold
  force: should
  level: fheq:7
  appliesTo: "master's graduates at the threshold"
  addressee: learner
  verbs: ["complete"]
  about: "an independent substantial project"
  themes: [none]
  domain: generic-skill
  award: ["master's", "postgraduate diploma", "postgraduate certificate"]
  gradeOf: none
  paraphrase: "Master's graduates should be able to show that they can carry through, by independent study, a substantial critical piece of empirical research, a work-based project, a major review or a case study, which may add to research or solve a workplace problem."
  quote: full   # the issuer's statement is in `source` (D-std-0014)
  audience: both
  subjects: inherited
- id: qaa/librarianship-information-knowledge-records-and-archives-management-2025/4.12.b6
  locator: { number: "4.12.b6", headingPath: ["Benchmark standards", "Generic skills (master's)"] }
  span: { start: 63306, end: 63387 }
  source: "critically evaluate current research and advanced scholarship in the subject area"
  stem: "4.12"
  statementType: threshold
  rung: threshold
  force: should
  level: fheq:7
  appliesTo: "master's graduates at the threshold"
  addressee: learner
  verbs: ["evaluate"]
  about: "evaluating current research critically"
  themes: [none]
  domain: generic-skill
  award: ["master's", "postgraduate diploma", "postgraduate certificate"]
  gradeOf: none
  paraphrase: "Master's graduates should be able to show a conceptual grasp that lets them judge current research and advanced scholarship in the field critically."
  quote: full   # the issuer's statement is in `source` (D-std-0014)
  audience: both
  subjects: inherited
- id: qaa/librarianship-information-knowledge-records-and-archives-management-2025/4.12.b7
  locator: { number: "4.12.b7", headingPath: ["Benchmark standards", "Generic skills (master's)"] }
  span: { start: 63390, end: 63557 }
  source: "evaluate methodologies, develop critiques of them and, where appropriate, propose new hypotheses; this skill may require awareness of methodologies in cognate subjects"
  stem: "4.12"
  statementType: threshold
  rung: threshold
  force: should
  level: fheq:7
  appliesTo: "master's graduates at the threshold"
  addressee: learner
  verbs: ["evaluate", "develop", "propose"]
  about: "critiquing methods and proposing hypotheses"
  themes: [none]
  domain: generic-skill
  award: ["master's", "postgraduate diploma", "postgraduate certificate"]
  gradeOf: none
  paraphrase: "Master's graduates should be able to show a conceptual grasp that lets them assess and critique research methods and, where fitting, put forward new hypotheses, which may mean knowing methods from neighbouring fields."
  quote: full   # the issuer's statement is in `source` (D-std-0014)
  audience: both
  subjects: inherited
- id: qaa/librarianship-information-knowledge-records-and-archives-management-2025/4.12.b8
  locator: { number: "4.12.b8", headingPath: ["Benchmark standards", "Generic skills (master's)"] }
  span: { start: 63560, end: 63771 }
  source: "ability to deal with complex issues both systematically and creatively, make sound judgements in the absence of complete data, and communicate their conclusions clearly to specialist and non-specialist audiences"
  stem: "4.12"
  statementType: threshold
  rung: threshold
  force: should
  level: fheq:7
  appliesTo: "master's graduates at the threshold"
  addressee: learner
  verbs: ["deal", "make", "communicate"]
  about: "complex issues, judgement and clear communication"
  themes: [none]
  domain: generic-skill
  award: ["master's", "postgraduate diploma", "postgraduate certificate"]
  gradeOf: none
  paraphrase: "Master's graduates should be able to show that they can handle complex issues both methodically and inventively, judge soundly when data are incomplete, and explain their conclusions plainly to expert and general audiences."
  quote: full   # the issuer's statement is in `source` (D-std-0014)
  audience: both
  subjects: inherited
- id: qaa/librarianship-information-knowledge-records-and-archives-management-2025/4.12.b9
  locator: { number: "4.12.b9", headingPath: ["Benchmark standards", "Generic skills (master's)"] }
  span: { start: 63774, end: 63816 }
  source: "self-direction, creativity and originality"
  stem: "4.12"
  statementType: threshold
  rung: threshold
  force: should
  level: fheq:7
  appliesTo: "master's graduates at the threshold"
  addressee: learner
  verbs: []
  about: "self-direction and originality"
  themes: [none]
  domain: generic-skill
  award: ["master's", "postgraduate diploma", "postgraduate certificate"]
  gradeOf: none
  paraphrase: "Master's graduates should be able to show that they direct themselves and work with creativity and originality."
  quote: full   # the issuer's statement is in `source` (D-std-0014)
  audience: both
  subjects: inherited
- id: qaa/librarianship-information-knowledge-records-and-archives-management-2025/4.12.b10
  locator: { number: "4.12.b10", headingPath: ["Benchmark standards", "Generic skills (master's)"] }
  span: { start: 63819, end: 63943 }
  source: "skills in leadership and advocacy, with informed awareness of dynamic internal and external factors that may influence these"
  stem: "4.12"
  statementType: threshold
  rung: threshold
  force: should
  level: fheq:7
  appliesTo: "master's graduates at the threshold"
  addressee: learner
  verbs: []
  about: "leadership and advocacy"
  themes: [none]
  domain: generic-skill
  award: ["master's", "postgraduate diploma", "postgraduate certificate"]
  gradeOf: none
  paraphrase: "Master's graduates should be able to show skill in leading and advocating, aware of the shifting internal and external factors that bear on both."
  quote: full   # the issuer's statement is in `source` (D-std-0014)
  audience: both
  subjects: inherited
- id: qaa/librarianship-information-knowledge-records-and-archives-management-2025/4.12.b11
  locator: { number: "4.12.b11", headingPath: ["Benchmark standards", "Generic skills (master's)"] }
  span: { start: 63946, end: 64019 }
  source: "an ability to exploit tools and processes for effective global networking"
  stem: "4.12"
  statementType: threshold
  rung: threshold
  force: should
  level: fheq:7
  appliesTo: "master's graduates at the threshold"
  addressee: learner
  verbs: ["exploit"]
  about: "networking globally"
  themes: [none]
  domain: generic-skill
  award: ["master's", "postgraduate diploma", "postgraduate certificate"]
  gradeOf: none
  paraphrase: "Master's graduates should be able to show that they can use tools and processes to network effectively across the world."
  quote: full   # the issuer's statement is in `source` (D-std-0014)
  audience: both
  subjects: inherited
- id: qaa/librarianship-information-knowledge-records-and-archives-management-2025/4.12.b12
  locator: { number: "4.12.b12", headingPath: ["Benchmark standards", "Generic skills (master's)"] }
  span: { start: 64022, end: 64093 }
  source: "an ability to challenge existing practice and justify proposed changes."
  stem: "4.12"
  statementType: threshold
  rung: threshold
  force: should
  level: fheq:7
  appliesTo: "master's graduates at the threshold"
  addressee: learner
  verbs: ["challenge", "justify"]
  about: "challenging practice and justifying change"
  themes: [none]
  domain: generic-skill
  award: ["master's", "postgraduate diploma", "postgraduate certificate"]
  gradeOf: none
  paraphrase: "Master's graduates should be able to show that they can question current practice and make the case for the changes they propose."
  quote: full   # the issuer's statement is in `source` (D-std-0014)
  audience: both
  subjects: inherited
```

### S4a Audience versions
<!-- label: both; status: drafted; basis: primary. forPractitioner: for the programme designer or teacher. forBeneficiary: for the student, second person, naming no issuer. author-agent-written: instructions to an AI agent writing about the statement (a course document, a handbook, an outcome, a report). author-agent-dialogue: instructions to an AI agent using the statement in conversation (with a student, a teacher or a programme team). Written fresh from the held text alone (benchmark rule 6; Abbott, 15:42). -->
```yaml
- statement: qaa/librarianship-information-knowledge-records-and-archives-management-2025/2.3.s1
  forPractitioner: { text: "Give students structured occasions to examine their own habits and ethical priorities as information users: the subject requires it, because information is what they study.", rewrite: light, force: must, status: drafted }
  forBeneficiary: { text: "You must reflect on how you yourself use information and on the ethical priorities you bring to it, because information is the thing you are studying.", rewrite: full, force: must, status: drafted }
  author-agent-written: "Treat this as a requirement worded with \"must\", at any award the statement covers: reflecting on their own information use and ethics. Cite it as (QAA, 2025, Librarianship, Information, Knowledge, Records and Archives Management Subject Benchmark Statement, para 2.3, first sentence). Do not claim it is a regulatory requirement or a rung of its own; set it beside the threshold lists in section 4 (4.7, 4.8, 4.11, 4.12)."
  author-agent-dialogue: "Raise this when a student or team discusses reflective tasks, ethics teaching or why the course asks students to examine their own information habits. Put it plainly, in the second person for a student and as a course design question for staff. Ask, for example: \"What does your own way of finding and judging information say about the priorities you would bring to a service?\" Do not read the issuer's wording aloud at length."
- statement: qaa/librarianship-information-knowledge-records-and-archives-management-2025/2.3.s2
  forPractitioner: { text: "Students should come to understand, and be able to show, that information is fluid, that its use has consequences and that appraisal must keep pace with social and technical change.", rewrite: light, force: should, status: drafted }
  forBeneficiary: { text: "You should be able to show that you understand how information changes over time, how its use affects people, and why it needs judging again as society and technology change.", rewrite: full, force: should, status: drafted }
  author-agent-written: "Treat this as an expectation worded with \"should\", at any award the statement covers: how information shifts and why it needs appraising. Cite it as (QAA, 2025, Librarianship, Information, Knowledge, Records and Archives Management Subject Benchmark Statement, para 2.3, second sentence). Do not claim it is a regulatory requirement or a rung of its own; set it beside the threshold lists in section 4 (4.7, 4.8, 4.11, 4.12)."
  author-agent-dialogue: "Raise this when a student or team asks what the course expects about how information shifts and why it needs appraising. Put it plainly, in the second person for a student and as a course design question for staff. Ask, for example: \"Can you think of a source whose value or meaning has changed since it was made, and how you would appraise it now?\" Do not read the issuer's wording aloud at length."
- statement: qaa/librarianship-information-knowledge-records-and-archives-management-2025/2.6
  forPractitioner: { text: "In a joint or combined honours course, students will reach the core of the subject-specific and generic skills set out here; the other subject adds further skills, so map which core items each route covers.", rewrite: light, force: will, status: drafted }
  forBeneficiary: { text: "If you study this field as part of a joint or combined degree, you will gain its core subject and general skills, plus further skills from the other subject you take.", rewrite: full, force: will, status: drafted }
  author-agent-written: "Treat this as an expectation worded with \"will\", for bachelor's with honours: core skills for joint and combined honours students. Cite it as (QAA, 2025, Librarianship, Information, Knowledge, Records and Archives Management Subject Benchmark Statement, para 2.6). Do not claim it is a regulatory requirement or a rung of its own; set it beside the framework descriptor qaa/fheq-2024/4.15.b1."
  author-agent-dialogue: "Raise this when a joint or combined honours student, or the team designing such a route, asks how much of the subject it must cover. Put it plainly, in the second person for a student and as a course design question for staff. Ask, for example: \"Which of the core skills does your half of the course cover, and which come from your other subject?\" Do not read the issuer's wording aloud at length."
- statement: qaa/librarianship-information-knowledge-records-and-archives-management-2025/2.17
  forPractitioner: { text: "The awarding body will have a working route, such as a staff and student liaison forum, for students to contribute to course monitoring and evaluation.", rewrite: light, force: will, status: drafted }
  forBeneficiary: { text: "not-applicable: a duty on the provider and the people who run the course, not a standard the student reaches", rewrite: full, force: will, status: drafted }
  author-agent-written: "Treat this as a duty on the institution, worded with \"will\": a system for student input to course monitoring, for every award the statement covers. Cite it as (QAA, 2025, Librarianship, Information, Knowledge, Records and Archives Management Subject Benchmark Statement, para 2.17). Do not present it as something a student must achieve, or as a regulatory requirement in England. Set it beside the threshold definitions at 4.6 and 4.11.s1 and the review duties at 2.17 and 2.18."
  author-agent-dialogue: "Raise this when a programme team or quality office plans monitoring, annual review or student representation. Put it in practitioner terms, as something the course or institution does. Ask, for example: \"How do students on this course currently feed into monitoring, and what changed last year as a result?\" Do not put it to a student as a standard they have to reach."
- statement: qaa/librarianship-information-knowledge-records-and-archives-management-2025/2.18
  forPractitioner: { text: "Plan periodic review with external reviewers who will give an independent view of proposed changes and confirm that threshold standards are met and the content fits the subject.", rewrite: light, force: will, status: drafted }
  forBeneficiary: { text: "not-applicable: a duty on the provider and the people who run the course, not a standard the student reaches", rewrite: full, force: will, status: drafted }
  author-agent-written: "Treat this as a duty on the institution, worded with \"will\": external reviewers in periodic review, for every award the statement covers. Cite it as (QAA, 2025, Librarianship, Information, Knowledge, Records and Archives Management Subject Benchmark Statement, para 2.18). Do not present it as something a student must achieve, or as a regulatory requirement in England. Set it beside the threshold definitions at 4.6 and 4.11.s1 and the review duties at 2.17 and 2.18."
  author-agent-dialogue: "Raise this when a programme team prepares for periodic review or revalidation. Put it in practitioner terms, as something the course or institution does. Ask, for example: \"Who will act as the external reviewer at the next periodic review, and which proposed changes most need their view?\" Do not put it to a student as a standard they have to reach."
- statement: qaa/librarianship-information-knowledge-records-and-archives-management-2025/3.10.b1
  forPractitioner: { text: "Include assessment, for instance a portfolio, a synoptic task or a self-reflective piece, in which students grow and evidence professional competencies.", rewrite: light, force: will, status: drafted }
  forBeneficiary: { text: "You will be assessed through tasks such as portfolios, synoptic work and self-reflection, which let you build and show your professional skills.", rewrite: full, force: will, status: drafted }
  author-agent-written: "Treat this as an expected feature of assessment design, worded with \"will\", for every award the statement covers: assessment of professional competencies. Cite it as (QAA, 2025, Librarianship, Information, Knowledge, Records and Archives Management Subject Benchmark Statement, para 3.10, first item), and do not claim it fixes a method or a weighting. Set it beside the other assessment items in 3.10, the practice paragraphs 3.9 and 3.11, and the outcomes it serves in 4.7, 4.8, 4.11 and 4.12."
  author-agent-dialogue: "Raise this when a team designs assessment, or when a student asks how and why they will be assessed. With a student, say plainly in the second person what kind of task to expect; with staff, frame it as a feature the assessment strategy should show. Ask, for example: \"Which piece of your portfolio best shows a professional skill, and what does it show?\" Avoid reading the list out at length."
- statement: qaa/librarianship-information-knowledge-records-and-archives-management-2025/3.10.b2
  forPractitioner: { text: "Include assessment, such as critical reflections, presentations or case studies, where students evaluate their professional and sector identity, their development and their learning journey.", rewrite: light, force: will, status: drafted }
  forBeneficiary: { text: "You will have assessments, such as reflective writing, presentations or case studies, where you look critically at your professional identity, your development and how your learning has gone.", rewrite: full, force: will, status: drafted }
  author-agent-written: "Treat this as an expected feature of assessment design, worded with \"will\", for every award the statement covers: reflexive evaluation of professional identity. Cite it as (QAA, 2025, Librarianship, Information, Knowledge, Records and Archives Management Subject Benchmark Statement, para 3.10, second item), and do not claim it fixes a method or a weighting. Set it beside the other assessment items in 3.10, the practice paragraphs 3.9 and 3.11, and the outcomes it serves in 4.7, 4.8, 4.11 and 4.12."
  author-agent-dialogue: "Raise this when a team designs assessment, or when a student asks how and why they will be assessed. With a student, say plainly in the second person what kind of task to expect; with staff, frame it as a feature the assessment strategy should show. Ask, for example: \"How has your sense of yourself as an information professional changed since you started?\" Avoid reading the list out at length."
- statement: qaa/librarianship-information-knowledge-records-and-archives-management-2025/3.10.b3
  forPractitioner: { text: "Include authentic assessment, such as practical projects, placements or project documentation, where students apply learning and make a genuine contribution in a sector, workplace or community setting.", rewrite: light, force: will, status: drafted }
  forBeneficiary: { text: "You will have assessments set in real workplaces, the sector or the community, such as projects or placements, where what you do makes a genuine contribution.", rewrite: full, force: will, status: drafted }
  author-agent-written: "Treat this as an expected feature of assessment design, worded with \"will\", for every award the statement covers: authentic assessment in real settings. Cite it as (QAA, 2025, Librarianship, Information, Knowledge, Records and Archives Management Subject Benchmark Statement, para 3.10, third item), and do not claim it fixes a method or a weighting. Set it beside the other assessment items in 3.10, the practice paragraphs 3.9 and 3.11, and the outcomes it serves in 4.7, 4.8, 4.11 and 4.12."
  author-agent-dialogue: "Raise this when a team designs assessment, or when a student asks how and why they will be assessed. With a student, say plainly in the second person what kind of task to expect; with staff, frame it as a feature the assessment strategy should show. Ask, for example: \"What did your placement or project change for the people it served?\" Avoid reading the list out at length."
- statement: qaa/librarianship-information-knowledge-records-and-archives-management-2025/3.10.b4
  forPractitioner: { text: "Include assessed group work, such as joint projects, presentations or portfolios, through which students show they can collaborate effectively.", rewrite: light, force: will, status: drafted }
  forBeneficiary: { text: "You will be assessed on how well you work in a group, for example through team projects, joint presentations or shared portfolios.", rewrite: full, force: will, status: drafted }
  author-agent-written: "Treat this as an expected feature of assessment design, worded with \"will\", for every award the statement covers: assessed group work. Cite it as (QAA, 2025, Librarianship, Information, Knowledge, Records and Archives Management Subject Benchmark Statement, para 3.10, fourth item), and do not claim it fixes a method or a weighting. Set it beside the other assessment items in 3.10, the practice paragraphs 3.9 and 3.11, and the outcomes it serves in 4.7, 4.8, 4.11 and 4.12."
  author-agent-dialogue: "Raise this when a team designs assessment, or when a student asks how and why they will be assessed. With a student, say plainly in the second person what kind of task to expect; with staff, frame it as a feature the assessment strategy should show. Ask, for example: \"What did you contribute to your last group task, and how did the group decide who did what?\" Avoid reading the list out at length."
- statement: qaa/librarianship-information-knowledge-records-and-archives-management-2025/3.10.b5
  forPractitioner: { text: "Include assessment in which students produce digital content (websites, databases, online catalogues, posters, social media outputs and the like) and may use generative AI in doing so.", rewrite: light, force: will, status: drafted }
  forBeneficiary: { text: "You will have assessments where you make digital content, such as a website, a database, an online catalogue or social media posts, and you may use generative AI tools to help.", rewrite: full, force: will, status: drafted }
  author-agent-written: "Treat this as an expected feature of assessment design, worded with \"will\", for every award the statement covers: assessed use of digital technologies. Cite it as (QAA, 2025, Librarianship, Information, Knowledge, Records and Archives Management Subject Benchmark Statement, para 3.10, fifth item), and do not claim it fixes a method or a weighting. Set it beside the other assessment items in 3.10, the practice paragraphs 3.9 and 3.11, and the outcomes it serves in 4.7, 4.8, 4.11 and 4.12."
  author-agent-dialogue: "Raise this when a team designs assessment, or when a student asks how and why they will be assessed. With a student, say plainly in the second person what kind of task to expect; with staff, frame it as a feature the assessment strategy should show. Ask, for example: \"Which digital tool did you use for your last piece of work, and how did you check what it produced?\" Avoid reading the list out at length."
- statement: qaa/librarianship-information-knowledge-records-and-archives-management-2025/3.10.b6
  forPractitioner: { text: "Include an assessed research task in which students collect primary data or work extensively with secondary data, analyse it and present what they find.", rewrite: light, force: will, status: drafted }
  forBeneficiary: { text: "You will carry out assessed research, collecting your own data or working closely with existing data, analysing it and presenting what you found.", rewrite: full, force: will, status: drafted }
  author-agent-written: "Treat this as an expected feature of assessment design, worded with \"will\", for every award the statement covers: assessed research. Cite it as (QAA, 2025, Librarianship, Information, Knowledge, Records and Archives Management Subject Benchmark Statement, para 3.10, sixth item), and do not claim it fixes a method or a weighting. Set it beside the other assessment items in 3.10, the practice paragraphs 3.9 and 3.11, and the outcomes it serves in 4.7, 4.8, 4.11 and 4.12."
  author-agent-dialogue: "Raise this when a team designs assessment, or when a student asks how and why they will be assessed. With a student, say plainly in the second person what kind of task to expect; with staff, frame it as a feature the assessment strategy should show. Ask, for example: \"What question would your research project answer, and where would your data come from?\" Avoid reading the list out at length."
- statement: qaa/librarianship-information-knowledge-records-and-archives-management-2025/4.2
  forPractitioner: { text: "When deciding what evidence marks achievement above the threshold, use your own method but consult Annex D of the Frameworks (the classification descriptions for honours degrees).", rewrite: light, force: should, status: drafted }
  forBeneficiary: { text: "not-applicable: a duty on the provider and the people who run the course, not a standard the student reaches", rewrite: full, force: should, status: drafted }
  author-agent-written: "Treat this as a duty on the institution, worded with \"should\": using Annex D to judge achievement above threshold, for honours courses. Cite it as (QAA, 2025, Librarianship, Information, Knowledge, Records and Archives Management Subject Benchmark Statement, para 4.2). Do not present it as something a student must achieve, or as a regulatory requirement in England. Set it beside qaa/fheq-2024/annex-d (the classification bands, SL6 in std:doc:qaa-fheq-2024-framework)."
  author-agent-dialogue: "Raise this when a programme team writes marking criteria or grade descriptors, or asks how classes above the threshold are judged. Put it in practitioner terms, as something the course or institution does. Ask, for example: \"How do your marking criteria for each class line up with the Annex D descriptions?\" Do not put it to a student as a standard they have to reach."
- statement: qaa/librarianship-information-knowledge-records-and-archives-management-2025/4.4
  forPractitioner: { text: "If you set competence standards (in the Equality Act 2010 sense) for a programme, follow the current Equality and Human Rights Commission guidance; the threshold standards here are not competence standards.", rewrite: light, force: should, status: drafted }
  forBeneficiary: { text: "not-applicable: a duty on the provider and the people who run the course, not a standard the student reaches", rewrite: full, force: should, status: drafted }
  author-agent-written: "Treat this as a duty on the institution, worded with \"should\": competence standards and equality guidance, for every award the statement covers. Cite it as (QAA, 2025, Librarianship, Information, Knowledge, Records and Archives Management Subject Benchmark Statement, para 4.4). Do not present it as something a student must achieve, or as a regulatory requirement in England. Set it beside 4.4's own context: the threshold standards are not competence standards."
  author-agent-dialogue: "Raise this when a programme team considers competence standards, reasonable adjustments or a PSRB requirement. Put it in practitioner terms, as something the course or institution does. Ask, for example: \"Does the programme specification set any competence standards, and has the current equality guidance been checked for them?\" Do not put it to a student as a standard they have to reach."
- statement: qaa/librarianship-information-knowledge-records-and-archives-management-2025/4.5.b1
  forPractitioner: { text: "Honours students should be able to put knowledge to work in structured contexts with guidance; at this level the setting is framed for them.", rewrite: light, force: should, status: drafted }
  forBeneficiary: { text: "You should be able to use what you know in tasks that are clearly structured and where you have guidance.", rewrite: full, force: should, status: drafted }
  author-agent-written: "Treat this as an honours threshold standard worded with \"should\", of which a third-class graduate shows most items to some degree (4.6). It holds at FHEQ level 6 (FQHEIS level 10, qaa/fqheis-2024/4.16) and concerns applying knowledge in structured, guided settings. Cite it as (QAA, 2025, Librarianship, Information, Knowledge, Records and Archives Management Subject Benchmark Statement, para 4.5, first item). Do not present it as a regulatory requirement or as a standard for master's awards, and set it beside the framework descriptor qaa/fheq-2024/4.15.b6 and spine:6 in the reference framework (std:ref:uk-framework, R8)."
  author-agent-dialogue: "Raise this when an honours student asks what the course should leave them able to do about applying knowledge in structured, guided settings, or plans work that draws on it. With a student, put it plainly in the second person; with staff, frame it as an outcome the course must give students the chance to show. Ask, for example: \"Which task so far has asked you to apply what you know, and what guidance did you lean on?\" Avoid reading the issuer's list aloud, and do not treat one item as a pass condition: at threshold most items, not all, are shown."
- statement: qaa/librarianship-information-knowledge-records-and-archives-management-2025/4.5.s1
  forPractitioner: { text: "By the end of an honours course, students should be able to show ordered, systematic understanding of the course's core knowledge; teach and assess the whole of it, not isolated topics.", rewrite: light, force: should, status: drafted }
  forBeneficiary: { text: "By the end of your honours degree, you should be able to show a well-organised understanding of the main knowledge your course covers.", rewrite: full, force: should, status: drafted }
  author-agent-written: "Treat this as an honours threshold standard worded with \"should\", of which a third-class graduate shows most items to some degree (4.6). It holds at FHEQ level 6 (FQHEIS level 10, qaa/fqheis-2024/4.16) and concerns systematic grasp of the course's core knowledge. Cite it as (QAA, 2025, Librarianship, Information, Knowledge, Records and Archives Management Subject Benchmark Statement, para 4.5, first sentence). Do not present it as a regulatory requirement or as a standard for master's awards, and set it beside its counterpart 4.10.s1 at the other award, the framework descriptor qaa/fheq-2024/4.15.b1 and spine:6 in the reference framework (std:ref:uk-framework, R8)."
  author-agent-dialogue: "Raise this when an honours student asks what the course should leave them able to do about systematic grasp of the course's core knowledge, or plans work that draws on it. With a student, put it plainly in the second person; with staff, frame it as an outcome the course must give students the chance to show. Ask, for example: \"If you had to map the main areas of your course on one page, how would they connect?\" Avoid reading the issuer's list aloud, and do not treat one item as a pass condition: at threshold most items, not all, are shown."
- statement: qaa/librarianship-information-knowledge-records-and-archives-management-2025/4.5.b2
  forPractitioner: { text: "Honours students should analyse and evaluate information within established frameworks, rather than devising their own.", rewrite: light, force: should, status: drafted }
  forBeneficiary: { text: "You should be able to analyse and judge information using frameworks that are already set out for you.", rewrite: full, force: should, status: drafted }
  author-agent-written: "Treat this as an honours threshold standard worded with \"should\", of which a third-class graduate shows most items to some degree (4.6). It holds at FHEQ level 6 (FQHEIS level 10, qaa/fqheis-2024/4.16) and concerns analysing information within set frameworks. Cite it as (QAA, 2025, Librarianship, Information, Knowledge, Records and Archives Management Subject Benchmark Statement, para 4.5, second item). Do not present it as a regulatory requirement or as a standard for master's awards, and set it beside the framework descriptor qaa/fheq-2024/4.15.b7 and spine:6 in the reference framework (std:ref:uk-framework, R8)."
  author-agent-dialogue: "Raise this when an honours student asks what the course should leave them able to do about analysing information within set frameworks, or plans work that draws on it. With a student, put it plainly in the second person; with staff, frame it as an outcome the course must give students the chance to show. Ask, for example: \"Which framework did you use to judge a source recently, and what did it help you see?\" Avoid reading the issuer's list aloud, and do not treat one item as a pass condition: at threshold most items, not all, are shown."
- statement: qaa/librarianship-information-knowledge-records-and-archives-management-2025/4.5.s2
  forPractitioner: { text: "Honours students should apply the subject's key concepts, principles and practices to clearly framed cases, exercising judgement over which processes, materials and techniques to use.", rewrite: light, force: should, status: drafted }
  forBeneficiary: { text: "You should be able to understand and use the main ideas, principles and practices of your subject in clearly set-out situations, choosing sensibly which methods and materials to use.", rewrite: full, force: should, status: drafted }
  author-agent-written: "Treat this as an honours threshold standard worded with \"should\", of which a third-class graduate shows most items to some degree (4.6). It holds at FHEQ level 6 (FQHEIS level 10, qaa/fqheis-2024/4.16) and concerns using core concepts in clearly bounded cases. Cite it as (QAA, 2025, Librarianship, Information, Knowledge, Records and Archives Management Subject Benchmark Statement, para 4.5, second sentence). Do not present it as a regulatory requirement or as a standard for master's awards, and set it beside its counterpart 4.10.s2 at the other award, the framework descriptor qaa/fheq-2024/4.15.b6 and spine:6 in the reference framework (std:ref:uk-framework, R8)."
  author-agent-dialogue: "Raise this when an honours student asks what the course should leave them able to do about using core concepts in clearly bounded cases, or plans work that draws on it. With a student, put it plainly in the second person; with staff, frame it as an outcome the course must give students the chance to show. Ask, for example: \"In your last practical task, how did you decide which technique to use?\" Avoid reading the issuer's list aloud, and do not treat one item as a pass condition: at threshold most items, not all, are shown."
- statement: qaa/librarianship-information-knowledge-records-and-archives-management-2025/4.5.b3
  forPractitioner: { text: "Honours students should use tools, technologies and methodologies of the field in practical settings, such as labs, projects or placements.", rewrite: light, force: should, status: drafted }
  forBeneficiary: { text: "You should be able to use the tools, technologies and methods of your field in practical work.", rewrite: full, force: should, status: drafted }
  author-agent-written: "Treat this as an honours threshold standard worded with \"should\", of which a third-class graduate shows most items to some degree (4.6). It holds at FHEQ level 6 (FQHEIS level 10, qaa/fqheis-2024/4.16) and concerns using tools and methods in practice. Cite it as (QAA, 2025, Librarianship, Information, Knowledge, Records and Archives Management Subject Benchmark Statement, para 4.5, third item). Do not present it as a regulatory requirement or as a standard for master's awards, and set it beside the framework descriptor qaa/fheq-2024/4.15.b2 and spine:6 in the reference framework (std:ref:uk-framework, R8)."
  author-agent-dialogue: "Raise this when an honours student asks what the course should leave them able to do about using tools and methods in practice, or plans work that draws on it. With a student, put it plainly in the second person; with staff, frame it as an outcome the course must give students the chance to show. Ask, for example: \"Which tools or systems can you now use confidently, and which still feel new?\" Avoid reading the issuer's list aloud, and do not treat one item as a pass condition: at threshold most items, not all, are shown."
- statement: qaa/librarianship-information-knowledge-records-and-archives-management-2025/4.6
  forPractitioner: { text: "Read the honours lists as a profile: a third-class graduate will have shown some proficiency in most of the listed attributes, not every one of them.", rewrite: light, force: will, status: drafted }
  forBeneficiary: { text: "To reach the minimum level for an honours degree (a third), you will have shown some skill in most, though not all, of the abilities set out for your subject.", rewrite: full, force: will, status: drafted }
  author-agent-written: "Treat this as an honours threshold standard worded with \"should\", of which a third-class graduate shows most items to some degree (4.6). It holds at FHEQ level 6 (FQHEIS level 10, qaa/fqheis-2024/4.16) and concerns what the third-class threshold means. Cite it as (QAA, 2025, Librarianship, Information, Knowledge, Records and Archives Management Subject Benchmark Statement, para 4.6). Do not present it as a regulatory requirement or as a standard for master's awards, and set it beside its counterpart 4.11.s1 at the other award, the framework descriptor qaa/fheq-2024/annex-d/summary/r1/3rd and the 3rd column of Annex D and spine:6 in the reference framework (std:ref:uk-framework, R8)."
  author-agent-dialogue: "Raise this when an honours student asks what the course should leave them able to do about what the third-class threshold means, or plans work that draws on it. With a student, put it plainly in the second person; with staff, frame it as an outcome the course must give students the chance to show. Ask, for example: \"Looking across the full list of abilities, which are your strongest and which have you not yet shown?\" Avoid reading the issuer's list aloud, and do not treat one item as a pass condition: at threshold most items, not all, are shown."
- statement: qaa/librarianship-information-knowledge-records-and-archives-management-2025/4.7.b1
  forPractitioner: { text: "By the end of an honours course, students should be able to plan and carry out approaches that expose and reduce bias in collections, systems and services, so that people are fairly represented and obstacles to access come down; give them a task that lets them show it.", rewrite: light, force: should, status: drafted }
  forBeneficiary: { text: "By the end of your honours degree, you should be able to plan and carry out ways of spotting and correcting bias in collections, catalogues and services, so that everyone is fairly represented and can reach what they need.", rewrite: full, force: should, status: drafted }
  author-agent-written: "Treat this as an honours threshold standard worded with \"should\", of which a third-class graduate shows most items to some degree (4.6). It holds at FHEQ level 6 (FQHEIS level 10, qaa/fqheis-2024/4.16) and concerns tackling bias in collections, systems and services. Cite it as (QAA, 2025, Librarianship, Information, Knowledge, Records and Archives Management Subject Benchmark Statement, para 4.7, first item). Do not present it as a regulatory requirement or as a standard for master's awards, and set it beside the framework descriptor qaa/fheq-2024/4.15.b6 and spine:6 in the reference framework (std:ref:uk-framework, R8)."
  author-agent-dialogue: "Raise this when an honours student asks what the course should leave them able to do about tackling bias in collections, systems and services, or plans work that draws on it. With a student, put it plainly in the second person; with staff, frame it as an outcome the course must give students the chance to show. Ask, for example: \"Which piece of your work so far best shows what you can do on tackling bias in collections, systems and services, and what would make it stronger?\" Avoid reading the issuer's list aloud, and do not treat one item as a pass condition: at threshold most items, not all, are shown."
- statement: qaa/librarianship-information-knowledge-records-and-archives-management-2025/4.7.b2
  forPractitioner: { text: "By the end of an honours course, students should be able to show, across research, communication and teamwork, that they hold accessibility and fairness as commitments, and act to clear away what blocks access and participation; give them a task that lets them show it.", rewrite: light, force: should, status: drafted }
  forBeneficiary: { text: "By the end of your honours degree, you should be able to show in all your work, research and teamwork included, that you care about access and fairness, and take steps to remove what stops people finding information or joining in.", rewrite: full, force: should, status: drafted }
  author-agent-written: "Treat this as an honours threshold standard worded with \"should\", of which a third-class graduate shows most items to some degree (4.6). It holds at FHEQ level 6 (FQHEIS level 10, qaa/fqheis-2024/4.16) and concerns a working commitment to access and equity. Cite it as (QAA, 2025, Librarianship, Information, Knowledge, Records and Archives Management Subject Benchmark Statement, para 4.7, second item). Do not present it as a regulatory requirement or as a standard for master's awards, and set it beside the framework descriptor qaa/fheq-2024/4.15.b6 and spine:6 in the reference framework (std:ref:uk-framework, R8)."
  author-agent-dialogue: "Raise this when an honours student asks what the course should leave them able to do about a working commitment to access and equity, or plans work that draws on it. With a student, put it plainly in the second person; with staff, frame it as an outcome the course must give students the chance to show. Ask, for example: \"Which piece of your work so far best shows what you can do on a working commitment to access and equity, and what would make it stronger?\" Avoid reading the issuer's list aloud, and do not treat one item as a pass condition: at threshold most items, not all, are shown."
- statement: qaa/librarianship-information-knowledge-records-and-archives-management-2025/4.7.b3
  forPractitioner: { text: "By the end of an honours course, students should be able to shape library spaces and collections, in person and online, so that they serve people with a wide spread of abilities and needs; give them a task that lets them show it.", rewrite: light, force: should, status: drafted }
  forBeneficiary: { text: "By the end of your honours degree, you should be able to design library spaces and collections, physical and online, that work well for people with different abilities and needs.", rewrite: full, force: should, status: drafted }
  author-agent-written: "Treat this as an honours threshold standard worded with \"should\", of which a third-class graduate shows most items to some degree (4.6). It holds at FHEQ level 6 (FQHEIS level 10, qaa/fqheis-2024/4.16) and concerns inclusive physical and online spaces and collections. Cite it as (QAA, 2025, Librarianship, Information, Knowledge, Records and Archives Management Subject Benchmark Statement, para 4.7, third item). Do not present it as a regulatory requirement or as a standard for master's awards, and set it beside its counterpart 4.11.b3 at the other award, the framework descriptor qaa/fheq-2024/4.15.b6 and spine:6 in the reference framework (std:ref:uk-framework, R8)."
  author-agent-dialogue: "Raise this when an honours student asks what the course should leave them able to do about inclusive physical and online spaces and collections, or plans work that draws on it. With a student, put it plainly in the second person; with staff, frame it as an outcome the course must give students the chance to show. Ask, for example: \"Which piece of your work so far best shows what you can do on inclusive physical and online spaces and collections, and what would make it stronger?\" Avoid reading the issuer's list aloud, and do not treat one item as a pass condition: at threshold most items, not all, are shown."
- statement: qaa/librarianship-information-knowledge-records-and-archives-management-2025/4.7.b4
  forPractitioner: { text: "By the end of an honours course, students should be able to work with community groups and teachers to advance academic, data, digital, media and information literacies that serve scholarship and learning through life; give them a task that lets them show it.", rewrite: light, force: should, status: drafted }
  forBeneficiary: { text: "By the end of your honours degree, you should be able to team up with community groups and teachers to help people build their academic, data, digital, media and information skills, for study and for learning through life.", rewrite: full, force: should, status: drafted }
  author-agent-written: "Treat this as an honours threshold standard worded with \"should\", of which a third-class graduate shows most items to some degree (4.6). It holds at FHEQ level 6 (FQHEIS level 10, qaa/fqheis-2024/4.16) and concerns building literacies with community partners. Cite it as (QAA, 2025, Librarianship, Information, Knowledge, Records and Archives Management Subject Benchmark Statement, para 4.7, fourth item). Do not present it as a regulatory requirement or as a standard for master's awards, and set it beside its counterpart 4.11.b4 at the other award, the framework descriptor qaa/fheq-2024/4.15.b6 and spine:6 in the reference framework (std:ref:uk-framework, R8)."
  author-agent-dialogue: "Raise this when an honours student asks what the course should leave them able to do about building literacies with community partners, or plans work that draws on it. With a student, put it plainly in the second person; with staff, frame it as an outcome the course must give students the chance to show. Ask, for example: \"Which piece of your work so far best shows what you can do on building literacies with community partners, and what would make it stronger?\" Avoid reading the issuer's list aloud, and do not treat one item as a pass condition: at threshold most items, not all, are shown."
- statement: qaa/librarianship-information-knowledge-records-and-archives-management-2025/4.7.b5
  forPractitioner: { text: "By the end of an honours course, students should be able to debate critically how information provision bears on human rights and equality, question structural inequality and bias (by race, gender or disability) in knowledge systems, and argue for fair access for groups once pushed aside; give them a task that lets them show it.", rewrite: light, force: should, status: drafted }
  forBeneficiary: { text: "By the end of your honours degree, you should be able to discuss critically how information services affect human rights and equality, challenge bias built into knowledge systems, such as bias by race, gender or disability, and speak up for fair access for groups who have been left out.", rewrite: full, force: should, status: drafted }
  author-agent-written: "Treat this as an honours threshold standard worded with \"should\", of which a third-class graduate shows most items to some degree (4.6). It holds at FHEQ level 6 (FQHEIS level 10, qaa/fqheis-2024/4.16) and concerns human rights, equality and fair access to information. Cite it as (QAA, 2025, Librarianship, Information, Knowledge, Records and Archives Management Subject Benchmark Statement, para 4.7, fifth item). Do not present it as a regulatory requirement or as a standard for master's awards, and set it beside its counterpart 4.11.b5 at the other award, the framework descriptor qaa/fheq-2024/4.15.b1 and spine:6 in the reference framework (std:ref:uk-framework, R8)."
  author-agent-dialogue: "Raise this when an honours student asks what the course should leave them able to do about human rights, equality and fair access to information, or plans work that draws on it. With a student, put it plainly in the second person; with staff, frame it as an outcome the course must give students the chance to show. Ask, for example: \"Which piece of your work so far best shows what you can do on human rights, equality and fair access to information, and what would make it stronger?\" Avoid reading the issuer's list aloud, and do not treat one item as a pass condition: at threshold most items, not all, are shown."
- statement: qaa/librarianship-information-knowledge-records-and-archives-management-2025/4.7.b6
  forPractitioner: { text: "By the end of an honours course, students should be able to argue that free access to information is a basic human right, and make the case for open access to knowledge and for the skills and systems that make access possible; give them a task that lets them show it.", rewrite: light, force: should, status: drafted }
  forBeneficiary: { text: "By the end of your honours degree, you should be able to argue that everyone has a right to reach information, and make the case for open access to knowledge and for the skills and systems that make it possible.", rewrite: full, force: should, status: drafted }
  author-agent-written: "Treat this as an honours threshold standard worded with \"should\", of which a third-class graduate shows most items to some degree (4.6). It holds at FHEQ level 6 (FQHEIS level 10, qaa/fqheis-2024/4.16) and concerns freedom of access and open access. Cite it as (QAA, 2025, Librarianship, Information, Knowledge, Records and Archives Management Subject Benchmark Statement, para 4.7, sixth item). Do not present it as a regulatory requirement or as a standard for master's awards, and set it beside the framework descriptor qaa/fheq-2024/4.15.b6 and spine:6 in the reference framework (std:ref:uk-framework, R8)."
  author-agent-dialogue: "Raise this when an honours student asks what the course should leave them able to do about freedom of access and open access, or plans work that draws on it. With a student, put it plainly in the second person; with staff, frame it as an outcome the course must give students the chance to show. Ask, for example: \"Which piece of your work so far best shows what you can do on freedom of access and open access, and what would make it stronger?\" Avoid reading the issuer's list aloud, and do not treat one item as a pass condition: at threshold most items, not all, are shown."
- statement: qaa/librarianship-information-knowledge-records-and-archives-management-2025/4.7.b7
  forPractitioner: { text: "By the end of an honours course, students should be able to draw up retention schedules and full preservation plans for physical and digital holdings that keep them usable for the long term and plan for format migration; give them a task that lets them show it.", rewrite: light, force: should, status: drafted }
  forBeneficiary: { text: "By the end of your honours degree, you should be able to write retention schedules and preservation plans for physical and digital material that keep it usable for years, including moving it to new formats when needed.", rewrite: full, force: should, status: drafted }
  author-agent-written: "Treat this as an honours threshold standard worded with \"should\", of which a third-class graduate shows most items to some degree (4.6). It holds at FHEQ level 6 (FQHEIS level 10, qaa/fqheis-2024/4.16) and concerns retention schedules and preservation plans. Cite it as (QAA, 2025, Librarianship, Information, Knowledge, Records and Archives Management Subject Benchmark Statement, para 4.7, seventh item). Do not present it as a regulatory requirement or as a standard for master's awards, and set it beside its counterpart 4.11.b6 at the other award, the framework descriptor qaa/fheq-2024/4.15.b6 and spine:6 in the reference framework (std:ref:uk-framework, R8)."
  author-agent-dialogue: "Raise this when an honours student asks what the course should leave them able to do about retention schedules and preservation plans, or plans work that draws on it. With a student, put it plainly in the second person; with staff, frame it as an outcome the course must give students the chance to show. Ask, for example: \"Which piece of your work so far best shows what you can do on retention schedules and preservation plans, and what would make it stronger?\" Avoid reading the issuer's list aloud, and do not treat one item as a pass condition: at threshold most items, not all, are shown."
- statement: qaa/librarianship-information-knowledge-records-and-archives-management-2025/4.7.b8
  forPractitioner: { text: "By the end of an honours course, students should be able to understand archival principles such as provenance and original order and use them when arranging and describing collections; give them a task that lets them show it.", rewrite: light, force: should, status: drafted }
  forBeneficiary: { text: "By the end of your honours degree, you should be able to understand archival principles such as provenance and original order and use them when you arrange and describe material.", rewrite: full, force: should, status: drafted }
  author-agent-written: "Treat this as an honours threshold standard worded with \"should\", of which a third-class graduate shows most items to some degree (4.6). It holds at FHEQ level 6 (FQHEIS level 10, qaa/fqheis-2024/4.16) and concerns archival principles in arrangement and description. Cite it as (QAA, 2025, Librarianship, Information, Knowledge, Records and Archives Management Subject Benchmark Statement, para 4.7, eighth item). Do not present it as a regulatory requirement or as a standard for master's awards, and set it beside its counterpart 4.11.b7 at the other award, the framework descriptor qaa/fheq-2024/4.15.b1 and spine:6 in the reference framework (std:ref:uk-framework, R8)."
  author-agent-dialogue: "Raise this when an honours student asks what the course should leave them able to do about archival principles in arrangement and description, or plans work that draws on it. With a student, put it plainly in the second person; with staff, frame it as an outcome the course must give students the chance to show. Ask, for example: \"Which piece of your work so far best shows what you can do on archival principles in arrangement and description, and what would make it stronger?\" Avoid reading the issuer's list aloud, and do not treat one item as a pass condition: at threshold most items, not all, are shown."
- statement: qaa/librarianship-information-knowledge-records-and-archives-management-2025/4.7.b9
  forPractitioner: { text: "By the end of an honours course, students should be able to follow the sector's standards for keeping fragile or sensitive items, with the right environmental conditions and security; give them a task that lets them show it.", rewrite: light, force: should, status: drafted }
  forBeneficiary: { text: "By the end of your honours degree, you should be able to follow the industry's standards for storing fragile or sensitive material, keeping conditions and security right.", rewrite: full, force: should, status: drafted }
  author-agent-written: "Treat this as an honours threshold standard worded with \"should\", of which a third-class graduate shows most items to some degree (4.6). It holds at FHEQ level 6 (FQHEIS level 10, qaa/fqheis-2024/4.16) and concerns storage standards for fragile or sensitive items. Cite it as (QAA, 2025, Librarianship, Information, Knowledge, Records and Archives Management Subject Benchmark Statement, para 4.7, ninth item). Do not present it as a regulatory requirement or as a standard for master's awards, and set it beside its counterpart 4.11.b9 at the other award, the framework descriptor qaa/fheq-2024/4.15.b6 and spine:6 in the reference framework (std:ref:uk-framework, R8)."
  author-agent-dialogue: "Raise this when an honours student asks what the course should leave them able to do about storage standards for fragile or sensitive items, or plans work that draws on it. With a student, put it plainly in the second person; with staff, frame it as an outcome the course must give students the chance to show. Ask, for example: \"Which piece of your work so far best shows what you can do on storage standards for fragile or sensitive items, and what would make it stronger?\" Avoid reading the issuer's list aloud, and do not treat one item as a pass condition: at threshold most items, not all, are shown."
- statement: qaa/librarianship-information-knowledge-records-and-archives-management-2025/4.7.b10
  forPractitioner: { text: "By the end of an honours course, students should be able to command cataloguing, classification, description and metadata work securely, using controlled vocabularies and standards so resources are easier to find; give them a task that lets them show it.", rewrite: light, force: should, status: drafted }
  forBeneficiary: { text: "By the end of your honours degree, you should be able to catalogue, classify and describe resources and create metadata skilfully, using controlled vocabularies and standards so that people can find things.", rewrite: full, force: should, status: drafted }
  author-agent-written: "Treat this as an honours threshold standard worded with \"should\", of which a third-class graduate shows most items to some degree (4.6). It holds at FHEQ level 6 (FQHEIS level 10, qaa/fqheis-2024/4.16) and concerns cataloguing, classification and metadata. Cite it as (QAA, 2025, Librarianship, Information, Knowledge, Records and Archives Management Subject Benchmark Statement, para 4.7, tenth item). Do not present it as a regulatory requirement or as a standard for master's awards, and set it beside its counterpart 4.11.b10 at the other award, the framework descriptor qaa/fheq-2024/4.15.b6 and spine:6 in the reference framework (std:ref:uk-framework, R8)."
  author-agent-dialogue: "Raise this when an honours student asks what the course should leave them able to do about cataloguing, classification and metadata, or plans work that draws on it. With a student, put it plainly in the second person; with staff, frame it as an outcome the course must give students the chance to show. Ask, for example: \"Which piece of your work so far best shows what you can do on cataloguing, classification and metadata, and what would make it stronger?\" Avoid reading the issuer's list aloud, and do not treat one item as a pass condition: at threshold most items, not all, are shown."
- statement: qaa/librarianship-information-knowledge-records-and-archives-management-2025/4.7.b11
  forPractitioner: { text: "By the end of an honours course, students should be able to design and run content management systems, digital repositories and web platforms in line with good accessibility practice; give them a task that lets them show it.", rewrite: light, force: should, status: drafted }
  forBeneficiary: { text: "By the end of your honours degree, you should be able to set up and run content management systems, digital repositories and websites that follow good accessibility practice.", rewrite: full, force: should, status: drafted }
  author-agent-written: "Treat this as an honours threshold standard worded with \"should\", of which a third-class graduate shows most items to some degree (4.6). It holds at FHEQ level 6 (FQHEIS level 10, qaa/fqheis-2024/4.16) and concerns content systems, repositories and web platforms. Cite it as (QAA, 2025, Librarianship, Information, Knowledge, Records and Archives Management Subject Benchmark Statement, para 4.7, eleventh item). Do not present it as a regulatory requirement or as a standard for master's awards, and set it beside its counterpart 4.11.b11 at the other award, the framework descriptor qaa/fheq-2024/4.15.b6 and spine:6 in the reference framework (std:ref:uk-framework, R8)."
  author-agent-dialogue: "Raise this when an honours student asks what the course should leave them able to do about content systems, repositories and web platforms, or plans work that draws on it. With a student, put it plainly in the second person; with staff, frame it as an outcome the course must give students the chance to show. Ask, for example: \"Which piece of your work so far best shows what you can do on content systems, repositories and web platforms, and what would make it stronger?\" Avoid reading the issuer's list aloud, and do not treat one item as a pass condition: at threshold most items, not all, are shown."
- statement: qaa/librarianship-information-knowledge-records-and-archives-management-2025/4.7.b12
  forPractitioner: { text: "By the end of an honours course, students should be able to apply user-centred design and accessibility guidance so that online resources and services are intuitive and inclusive to use; give them a task that lets them show it.", rewrite: light, force: should, status: drafted }
  forBeneficiary: { text: "By the end of your honours degree, you should be able to use user-centred design and accessibility guidelines to make online resources and services easy for everyone to use.", rewrite: full, force: should, status: drafted }
  author-agent-written: "Treat this as an honours threshold standard worded with \"should\", of which a third-class graduate shows most items to some degree (4.6). It holds at FHEQ level 6 (FQHEIS level 10, qaa/fqheis-2024/4.16) and concerns user-centred, accessible interface design. Cite it as (QAA, 2025, Librarianship, Information, Knowledge, Records and Archives Management Subject Benchmark Statement, para 4.7, twelfth item). Do not present it as a regulatory requirement or as a standard for master's awards, and set it beside its counterpart 4.11.b12 at the other award, the framework descriptor qaa/fheq-2024/4.15.b6 and spine:6 in the reference framework (std:ref:uk-framework, R8)."
  author-agent-dialogue: "Raise this when an honours student asks what the course should leave them able to do about user-centred, accessible interface design, or plans work that draws on it. With a student, put it plainly in the second person; with staff, frame it as an outcome the course must give students the chance to show. Ask, for example: \"Which piece of your work so far best shows what you can do on user-centred, accessible interface design, and what would make it stronger?\" Avoid reading the issuer's list aloud, and do not treat one item as a pass condition: at threshold most items, not all, are shown."
- statement: qaa/librarianship-information-knowledge-records-and-archives-management-2025/4.7.b13
  forPractitioner: { text: "By the end of an honours course, students should be able to appraise new technologies for managing information critically and put them to use, weighing their ethical consequences; give them a task that lets them show it.", rewrite: light, force: should, status: drafted }
  forBeneficiary: { text: "By the end of your honours degree, you should be able to weigh up new technologies for managing information, use them well and think through their ethical effects.", rewrite: full, force: should, status: drafted }
  author-agent-written: "Treat this as an honours threshold standard worded with \"should\", of which a third-class graduate shows most items to some degree (4.6). It holds at FHEQ level 6 (FQHEIS level 10, qaa/fqheis-2024/4.16) and concerns judging new technologies ethically. Cite it as (QAA, 2025, Librarianship, Information, Knowledge, Records and Archives Management Subject Benchmark Statement, para 4.7, thirteenth item). Do not present it as a regulatory requirement or as a standard for master's awards, and set it beside its counterpart 4.11.b13 at the other award, the framework descriptor qaa/fheq-2024/4.15.b6 and spine:6 in the reference framework (std:ref:uk-framework, R8)."
  author-agent-dialogue: "Raise this when an honours student asks what the course should leave them able to do about judging new technologies ethically, or plans work that draws on it. With a student, put it plainly in the second person; with staff, frame it as an outcome the course must give students the chance to show. Ask, for example: \"Which piece of your work so far best shows what you can do on judging new technologies ethically, and what would make it stronger?\" Avoid reading the issuer's list aloud, and do not treat one item as a pass condition: at threshold most items, not all, are shown."
- statement: qaa/librarianship-information-knowledge-records-and-archives-management-2025/4.7.b14
  forPractitioner: { text: "By the end of an honours course, students should be able to build, with teaching staff and community partners, full information literacy and reader development programmes for varied levels of skill and need; give them a task that lets them show it.", rewrite: light, force: should, status: drafted }
  forBeneficiary: { text: "By the end of your honours degree, you should be able to work with teachers and community partners to build information literacy and reading programmes that suit people at different levels and with different needs.", rewrite: full, force: should, status: drafted }
  author-agent-written: "Treat this as an honours threshold standard worded with \"should\", of which a third-class graduate shows most items to some degree (4.6). It holds at FHEQ level 6 (FQHEIS level 10, qaa/fqheis-2024/4.16) and concerns information literacy and reader development programmes. Cite it as (QAA, 2025, Librarianship, Information, Knowledge, Records and Archives Management Subject Benchmark Statement, para 4.7, fourteenth item). Do not present it as a regulatory requirement or as a standard for master's awards, and set it beside its counterpart 4.11.b14 at the other award, the framework descriptor qaa/fheq-2024/4.15.b6 and spine:6 in the reference framework (std:ref:uk-framework, R8)."
  author-agent-dialogue: "Raise this when an honours student asks what the course should leave them able to do about information literacy and reader development programmes, or plans work that draws on it. With a student, put it plainly in the second person; with staff, frame it as an outcome the course must give students the chance to show. Ask, for example: \"Which piece of your work so far best shows what you can do on information literacy and reader development programmes, and what would make it stronger?\" Avoid reading the issuer's list aloud, and do not treat one item as a pass condition: at threshold most items, not all, are shown."
- statement: qaa/librarianship-information-knowledge-records-and-archives-management-2025/4.7.b15
  forPractitioner: { text: "By the end of an honours course, students should be able to plan teaching and outreach that build critical thinking, media literacy and safe, responsible participation online; give them a task that lets them show it.", rewrite: light, force: should, status: drafted }
  forBeneficiary: { text: "By the end of your honours degree, you should be able to plan teaching and outreach sessions that help people think critically, read the media well and take part safely and responsibly online.", rewrite: full, force: should, status: drafted }
  author-agent-written: "Treat this as an honours threshold standard worded with \"should\", of which a third-class graduate shows most items to some degree (4.6). It holds at FHEQ level 6 (FQHEIS level 10, qaa/fqheis-2024/4.16) and concerns teaching and outreach for critical thinking. Cite it as (QAA, 2025, Librarianship, Information, Knowledge, Records and Archives Management Subject Benchmark Statement, para 4.7, fifteenth item). Do not present it as a regulatory requirement or as a standard for master's awards, and set it beside its counterpart 4.11.b16 at the other award, the framework descriptor qaa/fheq-2024/4.15.b6 and spine:6 in the reference framework (std:ref:uk-framework, R8)."
  author-agent-dialogue: "Raise this when an honours student asks what the course should leave them able to do about teaching and outreach for critical thinking, or plans work that draws on it. With a student, put it plainly in the second person; with staff, frame it as an outcome the course must give students the chance to show. Ask, for example: \"Which piece of your work so far best shows what you can do on teaching and outreach for critical thinking, and what would make it stronger?\" Avoid reading the issuer's list aloud, and do not treat one item as a pass condition: at threshold most items, not all, are shown."
- statement: qaa/librarianship-information-knowledge-records-and-archives-management-2025/4.7.b16
  forPractitioner: { text: "By the end of an honours course, students should be able to adjust critical information literacy teaching for different audiences, children, adults and lifelong learners among them; give them a task that lets them show it.", rewrite: light, force: should, status: drafted }
  forBeneficiary: { text: "By the end of your honours degree, you should be able to adjust how you teach critical information literacy for different groups, such as children, adults and lifelong learners.", rewrite: full, force: should, status: drafted }
  author-agent-written: "Treat this as an honours threshold standard worded with \"should\", of which a third-class graduate shows most items to some degree (4.6). It holds at FHEQ level 6 (FQHEIS level 10, qaa/fqheis-2024/4.16) and concerns critical information literacy for varied audiences. Cite it as (QAA, 2025, Librarianship, Information, Knowledge, Records and Archives Management Subject Benchmark Statement, para 4.7, sixteenth item). Do not present it as a regulatory requirement or as a standard for master's awards, and set it beside its counterpart 4.11.b15 at the other award, the framework descriptor qaa/fheq-2024/4.15.b6 and spine:6 in the reference framework (std:ref:uk-framework, R8)."
  author-agent-dialogue: "Raise this when an honours student asks what the course should leave them able to do about critical information literacy for varied audiences, or plans work that draws on it. With a student, put it plainly in the second person; with staff, frame it as an outcome the course must give students the chance to show. Ask, for example: \"Which piece of your work so far best shows what you can do on critical information literacy for varied audiences, and what would make it stronger?\" Avoid reading the issuer's list aloud, and do not treat one item as a pass condition: at threshold most items, not all, are shown."
- statement: qaa/librarianship-information-knowledge-records-and-archives-management-2025/4.7.b17
  forPractitioner: { text: "By the end of an honours course, students should be able to gather and analyse data on users, service performance and sector trends, and use it to ground decisions in evidence and keep improving; give them a task that lets them show it.", rewrite: light, force: should, status: drafted }
  forBeneficiary: { text: "By the end of your honours degree, you should be able to gather and analyse data about users, how services perform and trends in the sector, and use it to make decisions and keep improving.", rewrite: full, force: should, status: drafted }
  author-agent-written: "Treat this as an honours threshold standard worded with \"should\", of which a third-class graduate shows most items to some degree (4.6). It holds at FHEQ level 6 (FQHEIS level 10, qaa/fqheis-2024/4.16) and concerns user data and metrics for evidence-based improvement. Cite it as (QAA, 2025, Librarianship, Information, Knowledge, Records and Archives Management Subject Benchmark Statement, para 4.7, seventeenth item). Do not present it as a regulatory requirement or as a standard for master's awards, and set it beside its counterpart 4.11.b17 at the other award, the framework descriptor qaa/fheq-2024/4.15.b6 and spine:6 in the reference framework (std:ref:uk-framework, R8)."
  author-agent-dialogue: "Raise this when an honours student asks what the course should leave them able to do about user data and metrics for evidence-based improvement, or plans work that draws on it. With a student, put it plainly in the second person; with staff, frame it as an outcome the course must give students the chance to show. Ask, for example: \"Which piece of your work so far best shows what you can do on user data and metrics for evidence-based improvement, and what would make it stronger?\" Avoid reading the issuer's list aloud, and do not treat one item as a pass condition: at threshold most items, not all, are shown."
- statement: qaa/librarianship-information-knowledge-records-and-archives-management-2025/4.7.b18
  forPractitioner: { text: "By the end of an honours course, students should be able to try out AI tools for automated work such as metadata generation and recommender systems, keeping ethical oversight in place; give them a task that lets them show it.", rewrite: light, force: should, status: drafted }
  forBeneficiary: { text: "By the end of your honours degree, you should be able to try out AI tools for automatic tasks, such as creating metadata or recommending resources, while keeping an ethical check on how they are used.", rewrite: full, force: should, status: drafted }
  author-agent-written: "Treat this as an honours threshold standard worded with \"should\", of which a third-class graduate shows most items to some degree (4.6). It holds at FHEQ level 6 (FQHEIS level 10, qaa/fqheis-2024/4.16) and concerns AI tools for automated tasks, with ethical oversight. Cite it as (QAA, 2025, Librarianship, Information, Knowledge, Records and Archives Management Subject Benchmark Statement, para 4.7, eighteenth item). Do not present it as a regulatory requirement or as a standard for master's awards, and set it beside its counterpart 4.11.b20 at the other award, the framework descriptor qaa/fheq-2024/4.15.b6 and spine:6 in the reference framework (std:ref:uk-framework, R8)."
  author-agent-dialogue: "Raise this when an honours student asks what the course should leave them able to do about AI tools for automated tasks, with ethical oversight, or plans work that draws on it. With a student, put it plainly in the second person; with staff, frame it as an outcome the course must give students the chance to show. Ask, for example: \"Which piece of your work so far best shows what you can do on AI tools for automated tasks, with ethical oversight, and what would make it stronger?\" Avoid reading the issuer's list aloud, and do not treat one item as a pass condition: at threshold most items, not all, are shown."
- statement: qaa/librarianship-information-knowledge-records-and-archives-management-2025/4.7.b19
  forPractitioner: { text: "By the end of an honours course, students should be able to stand up for freedom of thought and expression, for the privacy of personal data, and for open access to information and data; give them a task that lets them show it.", rewrite: light, force: should, status: drafted }
  forBeneficiary: { text: "By the end of your honours degree, you should be able to stand up for people's freedom of thought and expression, for the privacy of their data, and for open access to information and data.", rewrite: full, force: should, status: drafted }
  author-agent-written: "Treat this as an honours threshold standard worded with \"should\", of which a third-class graduate shows most items to some degree (4.6). It holds at FHEQ level 6 (FQHEIS level 10, qaa/fqheis-2024/4.16) and concerns intellectual freedom, privacy and openness. Cite it as (QAA, 2025, Librarianship, Information, Knowledge, Records and Archives Management Subject Benchmark Statement, para 4.7, nineteenth item). Do not present it as a regulatory requirement or as a standard for master's awards, and set it beside its counterpart 4.11.b21 at the other award, the framework descriptor qaa/fheq-2024/4.15.b6 and spine:6 in the reference framework (std:ref:uk-framework, R8)."
  author-agent-dialogue: "Raise this when an honours student asks what the course should leave them able to do about intellectual freedom, privacy and openness, or plans work that draws on it. With a student, put it plainly in the second person; with staff, frame it as an outcome the course must give students the chance to show. Ask, for example: \"Which piece of your work so far best shows what you can do on intellectual freedom, privacy and openness, and what would make it stronger?\" Avoid reading the issuer's list aloud, and do not treat one item as a pass condition: at threshold most items, not all, are shown."
- statement: qaa/librarianship-information-knowledge-records-and-archives-management-2025/4.7.b20
  forPractitioner: { text: "By the end of an honours course, students should be able to help shape organisational policy on ethical information practice, responsible data governance and the rights of users; give them a task that lets them show it.", rewrite: light, force: should, status: drafted }
  forBeneficiary: { text: "By the end of your honours degree, you should be able to help write your organisation's policies on the ethical use of information, careful handling of data and the rights of its users.", rewrite: full, force: should, status: drafted }
  author-agent-written: "Treat this as an honours threshold standard worded with \"should\", of which a third-class graduate shows most items to some degree (4.6). It holds at FHEQ level 6 (FQHEIS level 10, qaa/fqheis-2024/4.16) and concerns organisational policy on information ethics. Cite it as (QAA, 2025, Librarianship, Information, Knowledge, Records and Archives Management Subject Benchmark Statement, para 4.7, twentieth item). Do not present it as a regulatory requirement or as a standard for master's awards, and set it beside its counterpart 4.11.b22 at the other award, the framework descriptor qaa/fheq-2024/4.15.b6 and spine:6 in the reference framework (std:ref:uk-framework, R8)."
  author-agent-dialogue: "Raise this when an honours student asks what the course should leave them able to do about organisational policy on information ethics, or plans work that draws on it. With a student, put it plainly in the second person; with staff, frame it as an outcome the course must give students the chance to show. Ask, for example: \"Which piece of your work so far best shows what you can do on organisational policy on information ethics, and what would make it stronger?\" Avoid reading the issuer's list aloud, and do not treat one item as a pass condition: at threshold most items, not all, are shown."
- statement: qaa/librarianship-information-knowledge-records-and-archives-management-2025/4.7.b21
  forPractitioner: { text: "By the end of an honours course, students should be able to take part in local and national campaigning for laws that widen fair access to information and protect users' privacy; give them a task that lets them show it.", rewrite: light, force: should, status: drafted }
  forBeneficiary: { text: "By the end of your honours degree, you should be able to take part in local and national campaigns for laws that give people fair access to information and protect their privacy.", rewrite: full, force: should, status: drafted }
  author-agent-written: "Treat this as an honours threshold standard worded with \"should\", of which a third-class graduate shows most items to some degree (4.6). It holds at FHEQ level 6 (FQHEIS level 10, qaa/fqheis-2024/4.16) and concerns advocacy for fair access and privacy law. Cite it as (QAA, 2025, Librarianship, Information, Knowledge, Records and Archives Management Subject Benchmark Statement, para 4.7, twenty-first item). Do not present it as a regulatory requirement or as a standard for master's awards, and set it beside its counterpart 4.11.b23 at the other award, the framework descriptor qaa/fheq-2024/4.15.b6 and spine:6 in the reference framework (std:ref:uk-framework, R8)."
  author-agent-dialogue: "Raise this when an honours student asks what the course should leave them able to do about advocacy for fair access and privacy law, or plans work that draws on it. With a student, put it plainly in the second person; with staff, frame it as an outcome the course must give students the chance to show. Ask, for example: \"Which piece of your work so far best shows what you can do on advocacy for fair access and privacy law, and what would make it stronger?\" Avoid reading the issuer's list aloud, and do not treat one item as a pass condition: at threshold most items, not all, are shown."
- statement: qaa/librarianship-information-knowledge-records-and-archives-management-2025/4.8.b1
  forPractitioner: { text: "Honours graduates should be able to recognise the issues, questions and problems a situation raises; build it into teaching and assessment across the course, not one module.", rewrite: light, force: should, status: drafted }
  forBeneficiary: { text: "By the end of your honours degree, you should be able to spot the issues, questions and problems a situation raises.", rewrite: full, force: should, status: drafted }
  author-agent-written: "Treat this as a generic skill: an honours threshold standard worded with \"should\", of which a third-class graduate shows most items to some degree (4.6). It holds at FHEQ level 6 (FQHEIS level 10, qaa/fqheis-2024/4.16) and concerns identifying issues, questions and problems. Cite it as (QAA, 2025, Librarianship, Information, Knowledge, Records and Archives Management Subject Benchmark Statement, para 4.8, first item). Do not present it as a regulatory requirement or as a standard for master's awards, and set it beside the framework descriptor qaa/fheq-2024/4.15.b7 and spine:6 in the reference framework (std:ref:uk-framework, R8)."
  author-agent-dialogue: "Raise this when an honours student asks what the course should leave them able to do about identifying issues, questions and problems, or plans work that draws on it. With a student, put it plainly in the second person; with staff, frame it as an outcome the course must give students the chance to show. Ask, for example: \"Which piece of your work so far best shows what you can do on identifying issues, questions and problems, and what would make it stronger?\" Avoid reading the issuer's list aloud, and do not treat one item as a pass condition: at threshold most items, not all, are shown."
- statement: qaa/librarianship-information-knowledge-records-and-archives-management-2025/4.8.b2
  forPractitioner: { text: "Honours graduates should be able to use a wide range of referencing styles accurately, following the detail each one asks for; build it into teaching and assessment across the course, not one module.", rewrite: light, force: should, status: drafted }
  forBeneficiary: { text: "By the end of your honours degree, you should be able to use many referencing styles accurately, following the detailed rules of each.", rewrite: full, force: should, status: drafted }
  author-agent-written: "Treat this as a generic skill: an honours threshold standard worded with \"should\", of which a third-class graduate shows most items to some degree (4.6). It holds at FHEQ level 6 (FQHEIS level 10, qaa/fqheis-2024/4.16) and concerns accurate use of referencing styles. Cite it as (QAA, 2025, Librarianship, Information, Knowledge, Records and Archives Management Subject Benchmark Statement, para 4.8, second item). Do not present it as a regulatory requirement or as a standard for master's awards, and set it beside the framework descriptor qaa/fheq-2024/4.15.b5 and spine:6 in the reference framework (std:ref:uk-framework, R8)."
  author-agent-dialogue: "Raise this when an honours student asks what the course should leave them able to do about accurate use of referencing styles, or plans work that draws on it. With a student, put it plainly in the second person; with staff, frame it as an outcome the course must give students the chance to show. Ask, for example: \"Which piece of your work so far best shows what you can do on accurate use of referencing styles, and what would make it stronger?\" Avoid reading the issuer's list aloud, and do not treat one item as a pass condition: at threshold most items, not all, are shown."
- statement: qaa/librarianship-information-knowledge-records-and-archives-management-2025/4.8.b3
  forPractitioner: { text: "Honours graduates should be able to see where their own knowledge falls short and gain what is missing; build it into teaching and assessment across the course, not one module.", rewrite: light, force: should, status: drafted }
  forBeneficiary: { text: "By the end of your honours degree, you should be able to see where your own knowledge falls short and learn what is missing.", rewrite: full, force: should, status: drafted }
  author-agent-written: "Treat this as a generic skill: an honours threshold standard worded with \"should\", of which a third-class graduate shows most items to some degree (4.6). It holds at FHEQ level 6 (FQHEIS level 10, qaa/fqheis-2024/4.16) and concerns finding and filling gaps in their knowledge. Cite it as (QAA, 2025, Librarianship, Information, Knowledge, Records and Archives Management Subject Benchmark Statement, para 4.8, third item). Do not present it as a regulatory requirement or as a standard for master's awards, and set it beside the framework descriptor qaa/fheq-2024/4.15.b9.3 and spine:6 in the reference framework (std:ref:uk-framework, R8)."
  author-agent-dialogue: "Raise this when an honours student asks what the course should leave them able to do about finding and filling gaps in their knowledge, or plans work that draws on it. With a student, put it plainly in the second person; with staff, frame it as an outcome the course must give students the chance to show. Ask, for example: \"Which piece of your work so far best shows what you can do on finding and filling gaps in their knowledge, and what would make it stronger?\" Avoid reading the issuer's list aloud, and do not treat one item as a pass condition: at threshold most items, not all, are shown."
- statement: qaa/librarianship-information-knowledge-records-and-archives-management-2025/4.8.b4
  forPractitioner: { text: "Honours graduates should be able to make sense of knowledge and information and analyse it; build it into teaching and assessment across the course, not one module.", rewrite: light, force: should, status: drafted }
  forBeneficiary: { text: "By the end of your honours degree, you should be able to make sense of knowledge and information and analyse it.", rewrite: full, force: should, status: drafted }
  author-agent-written: "Treat this as a generic skill: an honours threshold standard worded with \"should\", of which a third-class graduate shows most items to some degree (4.6). It holds at FHEQ level 6 (FQHEIS level 10, qaa/fqheis-2024/4.16) and concerns understanding and analysing information. Cite it as (QAA, 2025, Librarianship, Information, Knowledge, Records and Archives Management Subject Benchmark Statement, para 4.8, fourth item). Do not present it as a regulatory requirement or as a standard for master's awards, and set it beside the framework descriptor qaa/fheq-2024/4.15.b7 and spine:6 in the reference framework (std:ref:uk-framework, R8)."
  author-agent-dialogue: "Raise this when an honours student asks what the course should leave them able to do about understanding and analysing information, or plans work that draws on it. With a student, put it plainly in the second person; with staff, frame it as an outcome the course must give students the chance to show. Ask, for example: \"Which piece of your work so far best shows what you can do on understanding and analysing information, and what would make it stronger?\" Avoid reading the issuer's list aloud, and do not treat one item as a pass condition: at threshold most items, not all, are shown."
- statement: qaa/librarianship-information-knowledge-records-and-archives-management-2025/4.8.b5
  forPractitioner: { text: "Honours graduates should be able to pull together the current state of knowledge on a given topic; build it into teaching and assessment across the course, not one module.", rewrite: light, force: should, status: drafted }
  forBeneficiary: { text: "By the end of your honours degree, you should be able to pull together what is currently known about a topic.", rewrite: full, force: should, status: drafted }
  author-agent-written: "Treat this as a generic skill: an honours threshold standard worded with \"should\", of which a third-class graduate shows most items to some degree (4.6). It holds at FHEQ level 6 (FQHEIS level 10, qaa/fqheis-2024/4.16) and concerns drawing together what is known on a topic. Cite it as (QAA, 2025, Librarianship, Information, Knowledge, Records and Archives Management Subject Benchmark Statement, para 4.8, fifth item). Do not present it as a regulatory requirement or as a standard for master's awards, and set it beside the framework descriptor qaa/fheq-2024/4.15.b3.2 and spine:6 in the reference framework (std:ref:uk-framework, R8)."
  author-agent-dialogue: "Raise this when an honours student asks what the course should leave them able to do about drawing together what is known on a topic, or plans work that draws on it. With a student, put it plainly in the second person; with staff, frame it as an outcome the course must give students the chance to show. Ask, for example: \"Which piece of your work so far best shows what you can do on drawing together what is known on a topic, and what would make it stronger?\" Avoid reading the issuer's list aloud, and do not treat one item as a pass condition: at threshold most items, not all, are shown."
- statement: qaa/librarianship-information-knowledge-records-and-archives-management-2025/4.8.b6
  forPractitioner: { text: "Honours graduates should be able to use knowledge and understanding to reach conclusions supported by evidence; build it into teaching and assessment across the course, not one module.", rewrite: light, force: should, status: drafted }
  forBeneficiary: { text: "By the end of your honours degree, you should be able to use what you know and understand to reach conclusions backed by evidence.", rewrite: full, force: should, status: drafted }
  author-agent-written: "Treat this as a generic skill: an honours threshold standard worded with \"should\", of which a third-class graduate shows most items to some degree (4.6). It holds at FHEQ level 6 (FQHEIS level 10, qaa/fqheis-2024/4.16) and concerns reaching conclusions backed by evidence. Cite it as (QAA, 2025, Librarianship, Information, Knowledge, Records and Archives Management Subject Benchmark Statement, para 4.8, sixth item). Do not present it as a regulatory requirement or as a standard for master's awards, and set it beside the framework descriptor qaa/fheq-2024/4.15.b7 and spine:6 in the reference framework (std:ref:uk-framework, R8)."
  author-agent-dialogue: "Raise this when an honours student asks what the course should leave them able to do about reaching conclusions backed by evidence, or plans work that draws on it. With a student, put it plainly in the second person; with staff, frame it as an outcome the course must give students the chance to show. Ask, for example: \"Which piece of your work so far best shows what you can do on reaching conclusions backed by evidence, and what would make it stronger?\" Avoid reading the issuer's list aloud, and do not treat one item as a pass condition: at threshold most items, not all, are shown."
- statement: qaa/librarianship-information-knowledge-records-and-archives-management-2025/4.8.b7
  forPractitioner: { text: "Honours graduates should be able to communicate well and fittingly, in speech and in other forms; build it into teaching and assessment across the course, not one module.", rewrite: light, force: should, status: drafted }
  forBeneficiary: { text: "By the end of your honours degree, you should be able to communicate clearly and suitably, in speech and in other ways.", rewrite: full, force: should, status: drafted }
  author-agent-written: "Treat this as a generic skill: an honours threshold standard worded with \"should\", of which a third-class graduate shows most items to some degree (4.6). It holds at FHEQ level 6 (FQHEIS level 10, qaa/fqheis-2024/4.16) and concerns communicating effectively. Cite it as (QAA, 2025, Librarianship, Information, Knowledge, Records and Archives Management Subject Benchmark Statement, para 4.8, seventh item). Do not present it as a regulatory requirement or as a standard for master's awards, and set it beside the framework descriptor qaa/fheq-2024/4.15.b8 and spine:6 in the reference framework (std:ref:uk-framework, R8)."
  author-agent-dialogue: "Raise this when an honours student asks what the course should leave them able to do about communicating effectively, or plans work that draws on it. With a student, put it plainly in the second person; with staff, frame it as an outcome the course must give students the chance to show. Ask, for example: \"Which piece of your work so far best shows what you can do on communicating effectively, and what would make it stronger?\" Avoid reading the issuer's list aloud, and do not treat one item as a pass condition: at threshold most items, not all, are shown."
- statement: qaa/librarianship-information-knowledge-records-and-archives-management-2025/4.8.b8
  forPractitioner: { text: "Honours graduates should be able to set out knowledge or an argument so that others can follow it; build it into teaching and assessment across the course, not one module.", rewrite: light, force: should, status: drafted }
  forBeneficiary: { text: "By the end of your honours degree, you should be able to set out what you know, or an argument, so that others can follow it.", rewrite: full, force: should, status: drafted }
  author-agent-written: "Treat this as a generic skill: an honours threshold standard worded with \"should\", of which a third-class graduate shows most items to some degree (4.6). It holds at FHEQ level 6 (FQHEIS level 10, qaa/fqheis-2024/4.16) and concerns presenting knowledge or argument clearly. Cite it as (QAA, 2025, Librarianship, Information, Knowledge, Records and Archives Management Subject Benchmark Statement, para 4.8, eighth item). Do not present it as a regulatory requirement or as a standard for master's awards, and set it beside the framework descriptor qaa/fheq-2024/4.15.b8 and spine:6 in the reference framework (std:ref:uk-framework, R8)."
  author-agent-dialogue: "Raise this when an honours student asks what the course should leave them able to do about presenting knowledge or argument clearly, or plans work that draws on it. With a student, put it plainly in the second person; with staff, frame it as an outcome the course must give students the chance to show. Ask, for example: \"Which piece of your work so far best shows what you can do on presenting knowledge or argument clearly, and what would make it stronger?\" Avoid reading the issuer's list aloud, and do not treat one item as a pass condition: at threshold most items, not all, are shown."
- statement: qaa/librarianship-information-knowledge-records-and-archives-management-2025/4.8.b9
  forPractitioner: { text: "Honours graduates should be able to handle varied data, empirical qualitative and quantitative data included; build it into teaching and assessment across the course, not one module.", rewrite: light, force: should, status: drafted }
  forBeneficiary: { text: "By the end of your honours degree, you should be able to work with many kinds of data, including qualitative and quantitative data from research.", rewrite: full, force: should, status: drafted }
  author-agent-written: "Treat this as a generic skill: an honours threshold standard worded with \"should\", of which a third-class graduate shows most items to some degree (4.6). It holds at FHEQ level 6 (FQHEIS level 10, qaa/fqheis-2024/4.16) and concerns working with qualitative and quantitative data. Cite it as (QAA, 2025, Librarianship, Information, Knowledge, Records and Archives Management Subject Benchmark Statement, para 4.8, ninth item). Do not present it as a regulatory requirement or as a standard for master's awards, and set it beside the framework descriptor qaa/fheq-2024/annex-d/practical/r4/3rd and spine:6 in the reference framework (std:ref:uk-framework, R8)."
  author-agent-dialogue: "Raise this when an honours student asks what the course should leave them able to do about working with qualitative and quantitative data, or plans work that draws on it. With a student, put it plainly in the second person; with staff, frame it as an outcome the course must give students the chance to show. Ask, for example: \"Which piece of your work so far best shows what you can do on working with qualitative and quantitative data, and what would make it stronger?\" Avoid reading the issuer's list aloud, and do not treat one item as a pass condition: at threshold most items, not all, are shown."
- statement: qaa/librarianship-information-knowledge-records-and-archives-management-2025/4.8.b10
  forPractitioner: { text: "Honours graduates should be able to use a range of digital technologies critically to gather, analyse, choose and present information; build it into teaching and assessment across the course, not one module.", rewrite: light, force: should, status: drafted }
  forBeneficiary: { text: "By the end of your honours degree, you should be able to use digital tools critically to gather, analyse, choose and present information.", rewrite: full, force: should, status: drafted }
  author-agent-written: "Treat this as a generic skill: an honours threshold standard worded with \"should\", of which a third-class graduate shows most items to some degree (4.6). It holds at FHEQ level 6 (FQHEIS level 10, qaa/fqheis-2024/4.16) and concerns critical use of digital technology. Cite it as (QAA, 2025, Librarianship, Information, Knowledge, Records and Archives Management Subject Benchmark Statement, para 4.8, tenth item). Do not present it as a regulatory requirement or as a standard for master's awards, and set it beside the framework descriptor qaa/fheq-2024/annex-d/transferable/r1/3rd and spine:6 in the reference framework (std:ref:uk-framework, R8)."
  author-agent-dialogue: "Raise this when an honours student asks what the course should leave them able to do about critical use of digital technology, or plans work that draws on it. With a student, put it plainly in the second person; with staff, frame it as an outcome the course must give students the chance to show. Ask, for example: \"Which piece of your work so far best shows what you can do on critical use of digital technology, and what would make it stronger?\" Avoid reading the issuer's list aloud, and do not treat one item as a pass condition: at threshold most items, not all, are shown."
- statement: qaa/librarianship-information-knowledge-records-and-archives-management-2025/4.8.b11
  forPractitioner: { text: "Honours graduates should be able to show intellectual independence: working on tasks alone with suitable support, running their own research and exercising critical judgement; build it into teaching and assessment across the course, not one module.", rewrite: light, force: should, status: drafted }
  forBeneficiary: { text: "By the end of your honours degree, you should be able to think and work for yourself: take on tasks alone with the right support, run your own research and make critical judgements.", rewrite: full, force: should, status: drafted }
  author-agent-written: "Treat this as a generic skill: an honours threshold standard worded with \"should\", of which a third-class graduate shows most items to some degree (4.6). It holds at FHEQ level 6 (FQHEIS level 10, qaa/fqheis-2024/4.16) and concerns intellectual independence. Cite it as (QAA, 2025, Librarianship, Information, Knowledge, Records and Archives Management Subject Benchmark Statement, para 4.8, eleventh item). Do not present it as a regulatory requirement or as a standard for master's awards, and set it beside the framework descriptor qaa/fheq-2024/4.15.b9.1 and spine:6 in the reference framework (std:ref:uk-framework, R8)."
  author-agent-dialogue: "Raise this when an honours student asks what the course should leave them able to do about intellectual independence, or plans work that draws on it. With a student, put it plainly in the second person; with staff, frame it as an outcome the course must give students the chance to show. Ask, for example: \"Which piece of your work so far best shows what you can do on intellectual independence, and what would make it stronger?\" Avoid reading the issuer's list aloud, and do not treat one item as a pass condition: at threshold most items, not all, are shown."
- statement: qaa/librarianship-information-knowledge-records-and-archives-management-2025/4.8.b12
  forPractitioner: { text: "Honours graduates should be able to work with others, in a group or team or by taking part in discussion; build it into teaching and assessment across the course, not one module.", rewrite: light, force: should, status: drafted }
  forBeneficiary: { text: "By the end of your honours degree, you should be able to work with others, in a group or team or by joining in discussion.", rewrite: full, force: should, status: drafted }
  author-agent-written: "Treat this as a generic skill: an honours threshold standard worded with \"should\", of which a third-class graduate shows most items to some degree (4.6). It holds at FHEQ level 6 (FQHEIS level 10, qaa/fqheis-2024/4.16) and concerns working with others. Cite it as (QAA, 2025, Librarianship, Information, Knowledge, Records and Archives Management Subject Benchmark Statement, para 4.8, twelfth item). Do not present it as a regulatory requirement or as a standard for master's awards, and set it beside the framework descriptor qaa/fheq-2024/annex-d/transferable/r2/3rd and spine:6 in the reference framework (std:ref:uk-framework, R8)."
  author-agent-dialogue: "Raise this when an honours student asks what the course should leave them able to do about working with others, or plans work that draws on it. With a student, put it plainly in the second person; with staff, frame it as an outcome the course must give students the chance to show. Ask, for example: \"Which piece of your work so far best shows what you can do on working with others, and what would make it stronger?\" Avoid reading the issuer's list aloud, and do not treat one item as a pass condition: at threshold most items, not all, are shown."
- statement: qaa/librarianship-information-knowledge-records-and-archives-management-2025/4.8.b13
  forPractitioner: { text: "Honours graduates should be able to look back on their own progress, their personal leadership skills among it; build it into teaching and assessment across the course, not one module.", rewrite: light, force: should, status: drafted }
  forBeneficiary: { text: "By the end of your honours degree, you should be able to look back on your own progress, including how you lead.", rewrite: full, force: should, status: drafted }
  author-agent-written: "Treat this as a generic skill: an honours threshold standard worded with \"should\", of which a third-class graduate shows most items to some degree (4.6). It holds at FHEQ level 6 (FQHEIS level 10, qaa/fqheis-2024/4.16) and concerns reflecting on progress and personal leadership. Cite it as (QAA, 2025, Librarianship, Information, Knowledge, Records and Archives Management Subject Benchmark Statement, para 4.8, thirteenth item). Do not present it as a regulatory requirement or as a standard for master's awards, and set it beside the framework descriptor qaa/fheq-2024/annex-d/transferable/r5/3rd and spine:6 in the reference framework (std:ref:uk-framework, R8)."
  author-agent-dialogue: "Raise this when an honours student asks what the course should leave them able to do about reflecting on progress and personal leadership, or plans work that draws on it. With a student, put it plainly in the second person; with staff, frame it as an outcome the course must give students the chance to show. Ask, for example: \"Which piece of your work so far best shows what you can do on reflecting on progress and personal leadership, and what would make it stronger?\" Avoid reading the issuer's list aloud, and do not treat one item as a pass condition: at threshold most items, not all, are shown."
- statement: qaa/librarianship-information-knowledge-records-and-archives-management-2025/4.8.b14
  forPractitioner: { text: "Honours graduates should be able to recognise and examine the values and ethics beneath culture, society and their own conduct; build it into teaching and assessment across the course, not one module.", rewrite: light, force: should, status: drafted }
  forBeneficiary: { text: "By the end of your honours degree, you should be able to recognise and examine the values and ethics behind culture, society and your own choices.", rewrite: full, force: should, status: drafted }
  author-agent-written: "Treat this as a generic skill: an honours threshold standard worded with \"should\", of which a third-class graduate shows most items to some degree (4.6). It holds at FHEQ level 6 (FQHEIS level 10, qaa/fqheis-2024/4.16) and concerns examining values and ethics. Cite it as (QAA, 2025, Librarianship, Information, Knowledge, Records and Archives Management Subject Benchmark Statement, para 4.8, fourteenth item). Do not present it as a regulatory requirement or as a standard for master's awards, and set it beside the framework descriptor qaa/fheq-2024/4.15.b7 and spine:6 in the reference framework (std:ref:uk-framework, R8)."
  author-agent-dialogue: "Raise this when an honours student asks what the course should leave them able to do about examining values and ethics, or plans work that draws on it. With a student, put it plainly in the second person; with staff, frame it as an outcome the course must give students the chance to show. Ask, for example: \"Which piece of your work so far best shows what you can do on examining values and ethics, and what would make it stronger?\" Avoid reading the issuer's list aloud, and do not treat one item as a pass condition: at threshold most items, not all, are shown."
- statement: qaa/librarianship-information-knowledge-records-and-archives-management-2025/4.8.b15
  forPractitioner: { text: "Honours graduates should be able to understand why well-being, mental health and emotion matter and how they bear on learning; build it into teaching and assessment across the course, not one module.", rewrite: light, force: should, status: drafted }
  forBeneficiary: { text: "By the end of your honours degree, you should be able to understand why well-being, mental health and emotions matter and how they affect your learning.", rewrite: full, force: should, status: drafted }
  author-agent-written: "Treat this as a generic skill: an honours threshold standard worded with \"should\", of which a third-class graduate shows most items to some degree (4.6). It holds at FHEQ level 6 (FQHEIS level 10, qaa/fqheis-2024/4.16) and concerns well-being, emotion and learning. Cite it as (QAA, 2025, Librarianship, Information, Knowledge, Records and Archives Management Subject Benchmark Statement, para 4.8, fifteenth item). Do not present it as a regulatory requirement or as a standard for master's awards, and set it beside the framework descriptor qaa/fheq-2024/4.15.b5 and spine:6 in the reference framework (std:ref:uk-framework, R8)."
  author-agent-dialogue: "Raise this when an honours student asks what the course should leave them able to do about well-being, emotion and learning, or plans work that draws on it. With a student, put it plainly in the second person; with staff, frame it as an outcome the course must give students the chance to show. Ask, for example: \"Which piece of your work so far best shows what you can do on well-being, emotion and learning, and what would make it stronger?\" Avoid reading the issuer's list aloud, and do not treat one item as a pass condition: at threshold most items, not all, are shown."
- statement: qaa/librarianship-information-knowledge-records-and-archives-management-2025/4.8.b16
  forPractitioner: { text: "Honours graduates should be able to use the feedback they receive well, to take their thinking further; build it into teaching and assessment across the course, not one module.", rewrite: light, force: should, status: drafted }
  forBeneficiary: { text: "By the end of your honours degree, you should be able to use the feedback you get to take your thinking further.", rewrite: full, force: should, status: drafted }
  author-agent-written: "Treat this as a generic skill: an honours threshold standard worded with \"should\", of which a third-class graduate shows most items to some degree (4.6). It holds at FHEQ level 6 (FQHEIS level 10, qaa/fqheis-2024/4.16) and concerns using feedback to develop. Cite it as (QAA, 2025, Librarianship, Information, Knowledge, Records and Archives Management Subject Benchmark Statement, para 4.8, sixteenth item). Do not present it as a regulatory requirement or as a standard for master's awards, and set it beside the framework descriptor qaa/fheq-2024/4.15.b5 and spine:6 in the reference framework (std:ref:uk-framework, R8)."
  author-agent-dialogue: "Raise this when an honours student asks what the course should leave them able to do about using feedback to develop, or plans work that draws on it. With a student, put it plainly in the second person; with staff, frame it as an outcome the course must give students the chance to show. Ask, for example: \"Which piece of your work so far best shows what you can do on using feedback to develop, and what would make it stronger?\" Avoid reading the issuer's list aloud, and do not treat one item as a pass condition: at threshold most items, not all, are shown."
- statement: qaa/librarianship-information-knowledge-records-and-archives-management-2025/4.8.b17
  forPractitioner: { text: "Honours graduates should be able to value and join current debates on culture and society, such as those on inequality and sustainability; build it into teaching and assessment across the course, not one module.", rewrite: light, force: should, status: drafted }
  forBeneficiary: { text: "By the end of your honours degree, you should be able to follow and join current debates about culture and society, such as inequality and sustainability.", rewrite: full, force: should, status: drafted }
  author-agent-written: "Treat this as a generic skill: an honours threshold standard worded with \"should\", of which a third-class graduate shows most items to some degree (4.6). It holds at FHEQ level 6 (FQHEIS level 10, qaa/fqheis-2024/4.16) and concerns current debates on culture and society. Cite it as (QAA, 2025, Librarianship, Information, Knowledge, Records and Archives Management Subject Benchmark Statement, para 4.8, seventeenth item). Do not present it as a regulatory requirement or as a standard for master's awards, and set it beside the framework descriptor qaa/fheq-2024/4.15.b7 and spine:6 in the reference framework (std:ref:uk-framework, R8)."
  author-agent-dialogue: "Raise this when an honours student asks what the course should leave them able to do about current debates on culture and society, or plans work that draws on it. With a student, put it plainly in the second person; with staff, frame it as an outcome the course must give students the chance to show. Ask, for example: \"Which piece of your work so far best shows what you can do on current debates on culture and society, and what would make it stronger?\" Avoid reading the issuer's list aloud, and do not treat one item as a pass condition: at threshold most items, not all, are shown."
- statement: qaa/librarianship-information-knowledge-records-and-archives-management-2025/4.9.b1
  forPractitioner: { text: "Postgraduate courses build mastery of advanced ideas that deepen students' grasp of complex issues and their engagement with current research and scholarship.", rewrite: light, force: describes, status: drafted }
  forBeneficiary: { text: "At postgraduate level, you work with advanced ideas that deepen your understanding of complex issues and draw you into current research and scholarship.", rewrite: full, force: describes, status: drafted }
  author-agent-written: "Treat this as a description, with no modal of its own, of what postgraduate certificate, diploma and master's study involves (the lead-in at 4.9 says \"expected\"). It holds at FHEQ level 7 (FQHEIS level 11, which shares the FHEQ text) and concerns deeper understanding and engagement with research. Cite it as (QAA, 2025, Librarianship, Information, Knowledge, Records and Archives Management Subject Benchmark Statement, para 4.9, first item). Do not present it as a regulatory requirement or as a standard for honours degrees, and set it beside the framework descriptor qaa/fheq-2024/4.17.b1 and spine:7 in the reference framework (std:ref:uk-framework, R8)."
  author-agent-dialogue: "Raise this when a postgraduate student asks what the course should leave them able to do about deeper understanding and engagement with research, or plans work that draws on it. With a student, put it plainly in the second person; with staff, frame it as an outcome the course must give students the chance to show. Ask, for example: \"Which piece of your work so far best shows what you can do on deeper understanding and engagement with research, and what would make it stronger?\" Avoid reading the issuer's list aloud, and do not treat one item as a pass condition: at threshold most items, not all, are shown."
- statement: qaa/librarianship-information-knowledge-records-and-archives-management-2025/4.9.b2
  forPractitioner: { text: "Postgraduate courses develop students' ability to apply knowledge to real cases that are poorly defined or call for innovation.", rewrite: light, force: describes, status: drafted }
  forBeneficiary: { text: "At postgraduate level, you learn to use what you know in real situations where the problem is unclear or a new solution is needed.", rewrite: full, force: describes, status: drafted }
  author-agent-written: "Treat this as a description, with no modal of its own, of what postgraduate certificate, diploma and master's study involves (the lead-in at 4.9 says \"expected\"). It holds at FHEQ level 7 (FQHEIS level 11, which shares the FHEQ text) and concerns applying knowledge where problems are ill-defined. Cite it as (QAA, 2025, Librarianship, Information, Knowledge, Records and Archives Management Subject Benchmark Statement, para 4.9, second item). Do not present it as a regulatory requirement or as a standard for honours degrees, and set it beside the framework descriptor qaa/fheq-2024/4.17.b5 and spine:7 in the reference framework (std:ref:uk-framework, R8)."
  author-agent-dialogue: "Raise this when a postgraduate student asks what the course should leave them able to do about applying knowledge where problems are ill-defined, or plans work that draws on it. With a student, put it plainly in the second person; with staff, frame it as an outcome the course must give students the chance to show. Ask, for example: \"Which piece of your work so far best shows what you can do on applying knowledge where problems are ill-defined, and what would make it stronger?\" Avoid reading the issuer's list aloud, and do not treat one item as a pass condition: at threshold most items, not all, are shown."
- statement: qaa/librarianship-information-knowledge-records-and-archives-management-2025/4.9.b3
  forPractitioner: { text: "Postgraduate courses stress original research: students carry it out, evaluate methodologies and propose new hypotheses.", rewrite: light, force: describes, status: drafted }
  forBeneficiary: { text: "At postgraduate level, you are expected to do original research, judge research methods and put forward new hypotheses of your own.", rewrite: full, force: describes, status: drafted }
  author-agent-written: "Treat this as a generic skill: a description, with no modal of its own, of what postgraduate certificate, diploma and master's study involves (the lead-in at 4.9 says \"expected\"). It holds at FHEQ level 7 (FQHEIS level 11, which shares the FHEQ text) and concerns original research and new hypotheses. Cite it as (QAA, 2025, Librarianship, Information, Knowledge, Records and Archives Management Subject Benchmark Statement, para 4.9, third item). Do not present it as a regulatory requirement or as a standard for honours degrees, and set it beside the framework descriptor qaa/fheq-2024/4.17.b4.2 and spine:7 in the reference framework (std:ref:uk-framework, R8)."
  author-agent-dialogue: "Raise this when a postgraduate student asks what the course should leave them able to do about original research and new hypotheses, or plans work that draws on it. With a student, put it plainly in the second person; with staff, frame it as an outcome the course must give students the chance to show. Ask, for example: \"Which piece of your work so far best shows what you can do on original research and new hypotheses, and what would make it stronger?\" Avoid reading the issuer's list aloud, and do not treat one item as a pass condition: at threshold most items, not all, are shown."
- statement: qaa/librarianship-information-knowledge-records-and-archives-management-2025/4.9.b4
  forPractitioner: { text: "Postgraduate courses centre on leadership: students learn to lead and influence change, advocate ethical practice and build strategic responses to complex challenges.", rewrite: light, force: describes, status: drafted }
  forBeneficiary: { text: "At postgraduate level, you learn to lead and influence change, speak up for ethical practice and work out strategic answers to complex problems.", rewrite: full, force: describes, status: drafted }
  author-agent-written: "Treat this as a generic skill: a description, with no modal of its own, of what postgraduate certificate, diploma and master's study involves (the lead-in at 4.9 says \"expected\"). It holds at FHEQ level 7 (FQHEIS level 11, which shares the FHEQ text) and concerns leading change and strategic solutions. Cite it as (QAA, 2025, Librarianship, Information, Knowledge, Records and Archives Management Subject Benchmark Statement, para 4.9, fourth item). Do not present it as a regulatory requirement or as a standard for honours degrees, and set it beside the framework descriptor qaa/fheq-2024/4.17.b8.1 and spine:7 in the reference framework (std:ref:uk-framework, R8)."
  author-agent-dialogue: "Raise this when a postgraduate student asks what the course should leave them able to do about leading change and strategic solutions, or plans work that draws on it. With a student, put it plainly in the second person; with staff, frame it as an outcome the course must give students the chance to show. Ask, for example: \"Which piece of your work so far best shows what you can do on leading change and strategic solutions, and what would make it stronger?\" Avoid reading the issuer's list aloud, and do not treat one item as a pass condition: at threshold most items, not all, are shown."
- statement: qaa/librarianship-information-knowledge-records-and-archives-management-2025/4.10.s1
  forPractitioner: { text: "Postgraduate students, many with first degrees in other fields, should show systematic and comprehensive understanding of the course's core knowledge; plan induction for those new to the subject.", rewrite: light, force: should, status: drafted }
  forBeneficiary: { text: "By the end of your postgraduate course, you should be able to show a thorough, well-organised understanding of the main knowledge it covers, even if your first degree was in another subject.", rewrite: full, force: should, status: drafted }
  author-agent-written: "Treat this as a master's threshold attribute, also covering the postgraduate certificate and diploma, worded with \"should\". It holds at FHEQ level 7 (FQHEIS level 11, which shares the FHEQ text) and concerns systematic and comprehensive core knowledge. Cite it as (QAA, 2025, Librarianship, Information, Knowledge, Records and Archives Management Subject Benchmark Statement, para 4.10, first sentence). Do not present it as a regulatory requirement or as a standard for honours degrees, and set it beside its counterpart 4.5.s1 at the other award, the framework descriptor qaa/fheq-2024/4.17.b1 and spine:7 in the reference framework (std:ref:uk-framework, R8)."
  author-agent-dialogue: "Raise this when a postgraduate student asks what the course should leave them able to do about systematic and comprehensive core knowledge, or plans work that draws on it. With a student, put it plainly in the second person; with staff, frame it as an outcome the course must give students the chance to show. Ask, for example: \"Coming from your first degree, which parts of the core knowledge were new to you, and how secure do they feel now?\" Avoid reading the issuer's list aloud, and do not treat one item as a pass condition: at threshold most items, not all, are shown."
- statement: qaa/librarianship-information-knowledge-records-and-archives-management-2025/4.10.s2
  forPractitioner: { text: "At master's level, students should apply and critically analyse the subject's key concepts and practices in complex, varied cases, with sound judgement over processes, materials and techniques.", rewrite: light, force: should, status: drafted }
  forBeneficiary: { text: "You should be able to analyse critically and use the main ideas and practices of your subject in complex and varied situations, judging well which methods and materials to use.", rewrite: full, force: should, status: drafted }
  author-agent-written: "Treat this as a master's threshold attribute, also covering the postgraduate certificate and diploma, worded with \"should\". It holds at FHEQ level 7 (FQHEIS level 11, which shares the FHEQ text) and concerns critical application in complex, varied cases. Cite it as (QAA, 2025, Librarianship, Information, Knowledge, Records and Archives Management Subject Benchmark Statement, para 4.10, second sentence). Do not present it as a regulatory requirement or as a standard for honours degrees, and set it beside its counterpart 4.5.s2 at the other award, the framework descriptor qaa/fheq-2024/4.17.b5 and spine:7 in the reference framework (std:ref:uk-framework, R8)."
  author-agent-dialogue: "Raise this when a postgraduate student asks what the course should leave them able to do about critical application in complex, varied cases, or plans work that draws on it. With a student, put it plainly in the second person; with staff, frame it as an outcome the course must give students the chance to show. Ask, for example: \"Think of a messy, real case you worked on: what made it complex, and how did you choose your approach?\" Avoid reading the issuer's list aloud, and do not treat one item as a pass condition: at threshold most items, not all, are shown."
- statement: qaa/librarianship-information-knowledge-records-and-archives-management-2025/4.10.s3
  forPractitioner: { text: "A master's course may also ask students to show strategic thinking and leadership and to undertake original research at a higher academic standard; decide whether yours does and say so.", rewrite: light, force: may, status: drafted }
  forBeneficiary: { text: "On a master's course you may also be asked to show strategic thinking and leadership, and to carry out original research to a higher standard.", rewrite: full, force: may, status: drafted }
  author-agent-written: "Treat this as an expectation worded with \"may\", for master's and other postgraduate awards: strategic thinking, leadership and original research. Cite it as (QAA, 2025, Librarianship, Information, Knowledge, Records and Archives Management Subject Benchmark Statement, para 4.10, third sentence). Do not claim it is a regulatory requirement or a rung of its own; set it beside the framework descriptor qaa/fheq-2024/4.17.b6."
  author-agent-dialogue: "Raise this when a student or team asks what the course expects about strategic thinking, leadership and original research. Put it plainly, in the second person for a student and as a course design question for staff. Ask, for example: \"Has your course asked you to lead anything or to plan research of your own, and how did it go?\" Do not read the issuer's wording aloud at length."
- statement: qaa/librarianship-information-knowledge-records-and-archives-management-2025/4.11.b1
  forPractitioner: { text: "In postgraduate certificate, diploma and master's courses, give students room to show they can understand, with nuance, the particular information needs and sources of different disciplines and professions, such as STEM, law, business and the arts and humanities; at threshold they will have shown most such attributes to some degree.", rewrite: light, force: will, status: drafted }
  forBeneficiary: { text: "By the end of your postgraduate course, you will have shown that you can understand in detail what information different disciplines and professions need, such as science and engineering, law, business or the arts, and where it is found.", rewrite: full, force: will, status: drafted }
  author-agent-written: "Treat this as a master's threshold attribute, also covering the postgraduate certificate and diploma, worded with \"will\", of which a threshold graduate will have shown most to some degree (4.11). It holds at FHEQ level 7 (FQHEIS level 11, which shares the FHEQ text) and concerns information needs across disciplines and fields. Cite it as (QAA, 2025, Librarianship, Information, Knowledge, Records and Archives Management Subject Benchmark Statement, para 4.11, first item). Do not present it as a regulatory requirement or as a standard for honours degrees, and set it beside the framework descriptor qaa/fheq-2024/4.17.b1 and spine:7 in the reference framework (std:ref:uk-framework, R8)."
  author-agent-dialogue: "Raise this when a postgraduate student asks what the course should leave them able to do about information needs across disciplines and fields, or plans work that draws on it. With a student, put it plainly in the second person; with staff, frame it as an outcome the course must give students the chance to show. Ask, for example: \"Which piece of your work so far best shows what you can do on information needs across disciplines and fields, and what would make it stronger?\" Avoid reading the issuer's list aloud, and do not treat one item as a pass condition: at threshold most items, not all, are shown."
- statement: qaa/librarianship-information-knowledge-records-and-archives-management-2025/4.11.s1
  forPractitioner: { text: "Read the master's lists as a profile: a threshold graduate will have shown some proficiency in most of the attributes, not every one.", rewrite: light, force: will, status: drafted }
  forBeneficiary: { text: "To reach the minimum level for your postgraduate award, you will have shown some skill in most, though not all, of the abilities set out for your subject.", rewrite: full, force: will, status: drafted }
  author-agent-written: "Treat this as a master's threshold attribute, also covering the postgraduate certificate and diploma, worded with \"will\", of which a threshold graduate will have shown most to some degree (4.11). It holds at FHEQ level 7 (FQHEIS level 11, which shares the FHEQ text) and concerns what the master's threshold means. Cite it as (QAA, 2025, Librarianship, Information, Knowledge, Records and Archives Management Subject Benchmark Statement, para 4.11, first sentence). Do not present it as a regulatory requirement or as a standard for honours degrees, and set it beside its counterpart 4.6 at the other award, the framework descriptor qaa/fheq-2024/4.17.b1 and spine:7 in the reference framework (std:ref:uk-framework, R8)."
  author-agent-dialogue: "Raise this when a postgraduate student asks what the course should leave them able to do about what the master's threshold means, or plans work that draws on it. With a student, put it plainly in the second person; with staff, frame it as an outcome the course must give students the chance to show. Ask, for example: \"Looking across the full list of abilities, which can you already evidence, and which are still to come?\" Avoid reading the issuer's list aloud, and do not treat one item as a pass condition: at threshold most items, not all, are shown."
- statement: qaa/librarianship-information-knowledge-records-and-archives-management-2025/4.11.b2
  forPractitioner: { text: "In postgraduate certificate, diploma and master's courses, give students room to show they can design and deliver outreach, programmes and services that respond to culture and fit the needs of diverse communities; at threshold they will have shown most such attributes to some degree.", rewrite: light, force: will, status: drafted }
  forBeneficiary: { text: "By the end of your postgraduate course, you will have shown that you can design and run outreach, events and services that respect different cultures and meet the needs of diverse communities.", rewrite: full, force: will, status: drafted }
  author-agent-written: "Treat this as a master's threshold attribute, also covering the postgraduate certificate and diploma, worded with \"will\", of which a threshold graduate will have shown most to some degree (4.11). It holds at FHEQ level 7 (FQHEIS level 11, which shares the FHEQ text) and concerns culturally responsive outreach and services. Cite it as (QAA, 2025, Librarianship, Information, Knowledge, Records and Archives Management Subject Benchmark Statement, para 4.11, second item). Do not present it as a regulatory requirement or as a standard for honours degrees, and set it beside the framework descriptor qaa/fheq-2024/4.17.b5 and spine:7 in the reference framework (std:ref:uk-framework, R8)."
  author-agent-dialogue: "Raise this when a postgraduate student asks what the course should leave them able to do about culturally responsive outreach and services, or plans work that draws on it. With a student, put it plainly in the second person; with staff, frame it as an outcome the course must give students the chance to show. Ask, for example: \"Which piece of your work so far best shows what you can do on culturally responsive outreach and services, and what would make it stronger?\" Avoid reading the issuer's list aloud, and do not treat one item as a pass condition: at threshold most items, not all, are shown."
- statement: qaa/librarianship-information-knowledge-records-and-archives-management-2025/4.11.b3
  forPractitioner: { text: "In postgraduate certificate, diploma and master's courses, give students room to show they can shape library spaces and collections, in person and online, so that they serve people with a wide spread of abilities and needs; at threshold they will have shown most such attributes to some degree.", rewrite: light, force: will, status: drafted }
  forBeneficiary: { text: "By the end of your postgraduate course, you will have shown that you can design library spaces and collections, physical and online, that work well for people with different abilities and needs.", rewrite: full, force: will, status: drafted }
  author-agent-written: "Treat this as a master's threshold attribute, also covering the postgraduate certificate and diploma, worded with \"will\", of which a threshold graduate will have shown most to some degree (4.11). It holds at FHEQ level 7 (FQHEIS level 11, which shares the FHEQ text) and concerns inclusive physical and online spaces and collections. Cite it as (QAA, 2025, Librarianship, Information, Knowledge, Records and Archives Management Subject Benchmark Statement, para 4.11, third item). Do not present it as a regulatory requirement or as a standard for honours degrees, and set it beside its counterpart 4.7.b3 at the other award, the framework descriptor qaa/fheq-2024/4.17.b5 and spine:7 in the reference framework (std:ref:uk-framework, R8)."
  author-agent-dialogue: "Raise this when a postgraduate student asks what the course should leave them able to do about inclusive physical and online spaces and collections, or plans work that draws on it. With a student, put it plainly in the second person; with staff, frame it as an outcome the course must give students the chance to show. Ask, for example: \"Which piece of your work so far best shows what you can do on inclusive physical and online spaces and collections, and what would make it stronger?\" Avoid reading the issuer's list aloud, and do not treat one item as a pass condition: at threshold most items, not all, are shown."
- statement: qaa/librarianship-information-knowledge-records-and-archives-management-2025/4.11.b4
  forPractitioner: { text: "In postgraduate certificate, diploma and master's courses, give students room to show they can work with community groups and teachers to advance academic, data, digital, media and information literacies among marginalised groups; at threshold they will have shown most such attributes to some degree.", rewrite: light, force: will, status: drafted }
  forBeneficiary: { text: "By the end of your postgraduate course, you will have shown that you can team up with community groups and teachers to help marginalised groups build their academic, data, digital, media and information skills.", rewrite: full, force: will, status: drafted }
  author-agent-written: "Treat this as a master's threshold attribute, also covering the postgraduate certificate and diploma, worded with \"will\", of which a threshold graduate will have shown most to some degree (4.11). It holds at FHEQ level 7 (FQHEIS level 11, which shares the FHEQ text) and concerns building literacies for marginalised groups. Cite it as (QAA, 2025, Librarianship, Information, Knowledge, Records and Archives Management Subject Benchmark Statement, para 4.11, fourth item). Do not present it as a regulatory requirement or as a standard for honours degrees, and set it beside its counterpart 4.7.b4 at the other award, the framework descriptor qaa/fheq-2024/4.17.b5 and spine:7 in the reference framework (std:ref:uk-framework, R8)."
  author-agent-dialogue: "Raise this when a postgraduate student asks what the course should leave them able to do about building literacies for marginalised groups, or plans work that draws on it. With a student, put it plainly in the second person; with staff, frame it as an outcome the course must give students the chance to show. Ask, for example: \"Which piece of your work so far best shows what you can do on building literacies for marginalised groups, and what would make it stronger?\" Avoid reading the issuer's list aloud, and do not treat one item as a pass condition: at threshold most items, not all, are shown."
- statement: qaa/librarianship-information-knowledge-records-and-archives-management-2025/4.11.b5
  forPractitioner: { text: "In postgraduate certificate, diploma and master's courses, give students room to show they can debate critically the decolonising of information practice and challenge structural inequality in knowledge systems; at threshold they will have shown most such attributes to some degree.", rewrite: light, force: will, status: drafted }
  forBeneficiary: { text: "By the end of your postgraduate course, you will have shown that you can discuss critically how information practice can be decolonised and challenge the inequalities built into knowledge systems.", rewrite: full, force: will, status: drafted }
  author-agent-written: "Treat this as a master's threshold attribute, also covering the postgraduate certificate and diploma, worded with \"will\", of which a threshold graduate will have shown most to some degree (4.11). It holds at FHEQ level 7 (FQHEIS level 11, which shares the FHEQ text) and concerns decolonising information practice. Cite it as (QAA, 2025, Librarianship, Information, Knowledge, Records and Archives Management Subject Benchmark Statement, para 4.11, fifth item). Do not present it as a regulatory requirement or as a standard for honours degrees, and set it beside its counterpart 4.7.b5 at the other award, the framework descriptor qaa/fheq-2024/4.17.b1 and spine:7 in the reference framework (std:ref:uk-framework, R8)."
  author-agent-dialogue: "Raise this when a postgraduate student asks what the course should leave them able to do about decolonising information practice, or plans work that draws on it. With a student, put it plainly in the second person; with staff, frame it as an outcome the course must give students the chance to show. Ask, for example: \"Which piece of your work so far best shows what you can do on decolonising information practice, and what would make it stronger?\" Avoid reading the issuer's list aloud, and do not treat one item as a pass condition: at threshold most items, not all, are shown."
- statement: qaa/librarianship-information-knowledge-records-and-archives-management-2025/4.11.b6
  forPractitioner: { text: "In postgraduate certificate, diploma and master's courses, give students room to show they can draw up retention schedules and full preservation plans for physical and digital holdings that keep them usable for the long term and plan for format migration; at threshold they will have shown most such attributes to some degree.", rewrite: light, force: will, status: drafted }
  forBeneficiary: { text: "By the end of your postgraduate course, you will have shown that you can write retention schedules and preservation plans for physical and digital material that keep it usable for years, including moving it to new formats.", rewrite: full, force: will, status: drafted }
  author-agent-written: "Treat this as a master's threshold attribute, also covering the postgraduate certificate and diploma, worded with \"will\", of which a threshold graduate will have shown most to some degree (4.11). It holds at FHEQ level 7 (FQHEIS level 11, which shares the FHEQ text) and concerns retention schedules and preservation plans. Cite it as (QAA, 2025, Librarianship, Information, Knowledge, Records and Archives Management Subject Benchmark Statement, para 4.11, sixth item). Do not present it as a regulatory requirement or as a standard for honours degrees, and set it beside its counterpart 4.7.b7 at the other award, the framework descriptor qaa/fheq-2024/4.17.b5 and spine:7 in the reference framework (std:ref:uk-framework, R8)."
  author-agent-dialogue: "Raise this when a postgraduate student asks what the course should leave them able to do about retention schedules and preservation plans, or plans work that draws on it. With a student, put it plainly in the second person; with staff, frame it as an outcome the course must give students the chance to show. Ask, for example: \"Which piece of your work so far best shows what you can do on retention schedules and preservation plans, and what would make it stronger?\" Avoid reading the issuer's list aloud, and do not treat one item as a pass condition: at threshold most items, not all, are shown."
- statement: qaa/librarianship-information-knowledge-records-and-archives-management-2025/4.11.b7
  forPractitioner: { text: "In postgraduate certificate, diploma and master's courses, give students room to show they can understand archival principles such as provenance and original order and use them when arranging and describing collections; at threshold they will have shown most such attributes to some degree.", rewrite: light, force: will, status: drafted }
  forBeneficiary: { text: "By the end of your postgraduate course, you will have shown that you can understand archival principles such as provenance and original order and use them when you arrange and describe material.", rewrite: full, force: will, status: drafted }
  author-agent-written: "Treat this as a master's threshold attribute, also covering the postgraduate certificate and diploma, worded with \"will\", of which a threshold graduate will have shown most to some degree (4.11). It holds at FHEQ level 7 (FQHEIS level 11, which shares the FHEQ text) and concerns archival principles in arrangement and description. Cite it as (QAA, 2025, Librarianship, Information, Knowledge, Records and Archives Management Subject Benchmark Statement, para 4.11, seventh item). Do not present it as a regulatory requirement or as a standard for honours degrees, and set it beside its counterpart 4.7.b8 at the other award, the framework descriptor qaa/fheq-2024/4.17.b1 and spine:7 in the reference framework (std:ref:uk-framework, R8)."
  author-agent-dialogue: "Raise this when a postgraduate student asks what the course should leave them able to do about archival principles in arrangement and description, or plans work that draws on it. With a student, put it plainly in the second person; with staff, frame it as an outcome the course must give students the chance to show. Ask, for example: \"Which piece of your work so far best shows what you can do on archival principles in arrangement and description, and what would make it stronger?\" Avoid reading the issuer's list aloud, and do not treat one item as a pass condition: at threshold most items, not all, are shown."
- statement: qaa/librarianship-information-knowledge-records-and-archives-management-2025/4.11.b8
  forPractitioner: { text: "In postgraduate certificate, diploma and master's courses, give students room to show they can put in place disaster preparedness, with risk assessment, backup strategies and recovery plans; at threshold they will have shown most such attributes to some degree.", rewrite: light, force: will, status: drafted }
  forBeneficiary: { text: "By the end of your postgraduate course, you will have shown that you can put disaster plans in place, with risk assessments, backups and plans for recovery.", rewrite: full, force: will, status: drafted }
  author-agent-written: "Treat this as a master's threshold attribute, also covering the postgraduate certificate and diploma, worded with \"will\", of which a threshold graduate will have shown most to some degree (4.11). It holds at FHEQ level 7 (FQHEIS level 11, which shares the FHEQ text) and concerns disaster preparedness and recovery. Cite it as (QAA, 2025, Librarianship, Information, Knowledge, Records and Archives Management Subject Benchmark Statement, para 4.11, eighth item). Do not present it as a regulatory requirement or as a standard for honours degrees, and set it beside the framework descriptor qaa/fheq-2024/4.17.b5 and spine:7 in the reference framework (std:ref:uk-framework, R8)."
  author-agent-dialogue: "Raise this when a postgraduate student asks what the course should leave them able to do about disaster preparedness and recovery, or plans work that draws on it. With a student, put it plainly in the second person; with staff, frame it as an outcome the course must give students the chance to show. Ask, for example: \"Which piece of your work so far best shows what you can do on disaster preparedness and recovery, and what would make it stronger?\" Avoid reading the issuer's list aloud, and do not treat one item as a pass condition: at threshold most items, not all, are shown."
- statement: qaa/librarianship-information-knowledge-records-and-archives-management-2025/4.11.b9
  forPractitioner: { text: "In postgraduate certificate, diploma and master's courses, give students room to show they can follow the sector's standards for keeping fragile or sensitive items, with the right environmental conditions and security; at threshold they will have shown most such attributes to some degree.", rewrite: light, force: will, status: drafted }
  forBeneficiary: { text: "By the end of your postgraduate course, you will have shown that you can follow the industry's standards for storing fragile or sensitive material, keeping conditions and security right.", rewrite: full, force: will, status: drafted }
  author-agent-written: "Treat this as a master's threshold attribute, also covering the postgraduate certificate and diploma, worded with \"will\", of which a threshold graduate will have shown most to some degree (4.11). It holds at FHEQ level 7 (FQHEIS level 11, which shares the FHEQ text) and concerns storage standards for fragile or sensitive items. Cite it as (QAA, 2025, Librarianship, Information, Knowledge, Records and Archives Management Subject Benchmark Statement, para 4.11, ninth item). Do not present it as a regulatory requirement or as a standard for honours degrees, and set it beside its counterpart 4.7.b9 at the other award, the framework descriptor qaa/fheq-2024/4.17.b5 and spine:7 in the reference framework (std:ref:uk-framework, R8)."
  author-agent-dialogue: "Raise this when a postgraduate student asks what the course should leave them able to do about storage standards for fragile or sensitive items, or plans work that draws on it. With a student, put it plainly in the second person; with staff, frame it as an outcome the course must give students the chance to show. Ask, for example: \"Which piece of your work so far best shows what you can do on storage standards for fragile or sensitive items, and what would make it stronger?\" Avoid reading the issuer's list aloud, and do not treat one item as a pass condition: at threshold most items, not all, are shown."
- statement: qaa/librarianship-information-knowledge-records-and-archives-management-2025/4.11.b10
  forPractitioner: { text: "In postgraduate certificate, diploma and master's courses, give students room to show they can command cataloguing, classification, description and metadata work securely, using controlled vocabularies and standards so resources are easier to find; at threshold they will have shown most such attributes to some degree.", rewrite: light, force: will, status: drafted }
  forBeneficiary: { text: "By the end of your postgraduate course, you will have shown that you can catalogue, classify and describe resources and create metadata skilfully, using controlled vocabularies and standards so that people can find things.", rewrite: full, force: will, status: drafted }
  author-agent-written: "Treat this as a master's threshold attribute, also covering the postgraduate certificate and diploma, worded with \"will\", of which a threshold graduate will have shown most to some degree (4.11). It holds at FHEQ level 7 (FQHEIS level 11, which shares the FHEQ text) and concerns cataloguing, classification and metadata. Cite it as (QAA, 2025, Librarianship, Information, Knowledge, Records and Archives Management Subject Benchmark Statement, para 4.11, tenth item). Do not present it as a regulatory requirement or as a standard for honours degrees, and set it beside its counterpart 4.7.b10 at the other award, the framework descriptor qaa/fheq-2024/4.17.b5 and spine:7 in the reference framework (std:ref:uk-framework, R8)."
  author-agent-dialogue: "Raise this when a postgraduate student asks what the course should leave them able to do about cataloguing, classification and metadata, or plans work that draws on it. With a student, put it plainly in the second person; with staff, frame it as an outcome the course must give students the chance to show. Ask, for example: \"Which piece of your work so far best shows what you can do on cataloguing, classification and metadata, and what would make it stronger?\" Avoid reading the issuer's list aloud, and do not treat one item as a pass condition: at threshold most items, not all, are shown."
- statement: qaa/librarianship-information-knowledge-records-and-archives-management-2025/4.11.b11
  forPractitioner: { text: "In postgraduate certificate, diploma and master's courses, give students room to show they can design and run content management systems, digital repositories and web platforms in line with good accessibility practice; at threshold they will have shown most such attributes to some degree.", rewrite: light, force: will, status: drafted }
  forBeneficiary: { text: "By the end of your postgraduate course, you will have shown that you can set up and run content management systems, digital repositories and websites that follow good accessibility practice.", rewrite: full, force: will, status: drafted }
  author-agent-written: "Treat this as a master's threshold attribute, also covering the postgraduate certificate and diploma, worded with \"will\", of which a threshold graduate will have shown most to some degree (4.11). It holds at FHEQ level 7 (FQHEIS level 11, which shares the FHEQ text) and concerns content systems, repositories and web platforms. Cite it as (QAA, 2025, Librarianship, Information, Knowledge, Records and Archives Management Subject Benchmark Statement, para 4.11, eleventh item). Do not present it as a regulatory requirement or as a standard for honours degrees, and set it beside its counterpart 4.7.b11 at the other award, the framework descriptor qaa/fheq-2024/4.17.b5 and spine:7 in the reference framework (std:ref:uk-framework, R8)."
  author-agent-dialogue: "Raise this when a postgraduate student asks what the course should leave them able to do about content systems, repositories and web platforms, or plans work that draws on it. With a student, put it plainly in the second person; with staff, frame it as an outcome the course must give students the chance to show. Ask, for example: \"Which piece of your work so far best shows what you can do on content systems, repositories and web platforms, and what would make it stronger?\" Avoid reading the issuer's list aloud, and do not treat one item as a pass condition: at threshold most items, not all, are shown."
- statement: qaa/librarianship-information-knowledge-records-and-archives-management-2025/4.11.b12
  forPractitioner: { text: "In postgraduate certificate, diploma and master's courses, give students room to show they can apply user-centred design and accessibility guidance so that online resources and services are intuitive and inclusive to use; at threshold they will have shown most such attributes to some degree.", rewrite: light, force: will, status: drafted }
  forBeneficiary: { text: "By the end of your postgraduate course, you will have shown that you can use user-centred design and accessibility guidelines to make online resources and services easy for everyone to use.", rewrite: full, force: will, status: drafted }
  author-agent-written: "Treat this as a master's threshold attribute, also covering the postgraduate certificate and diploma, worded with \"will\", of which a threshold graduate will have shown most to some degree (4.11). It holds at FHEQ level 7 (FQHEIS level 11, which shares the FHEQ text) and concerns user-centred, accessible interface design. Cite it as (QAA, 2025, Librarianship, Information, Knowledge, Records and Archives Management Subject Benchmark Statement, para 4.11, twelfth item). Do not present it as a regulatory requirement or as a standard for honours degrees, and set it beside its counterpart 4.7.b12 at the other award, the framework descriptor qaa/fheq-2024/4.17.b5 and spine:7 in the reference framework (std:ref:uk-framework, R8)."
  author-agent-dialogue: "Raise this when a postgraduate student asks what the course should leave them able to do about user-centred, accessible interface design, or plans work that draws on it. With a student, put it plainly in the second person; with staff, frame it as an outcome the course must give students the chance to show. Ask, for example: \"Which piece of your work so far best shows what you can do on user-centred, accessible interface design, and what would make it stronger?\" Avoid reading the issuer's list aloud, and do not treat one item as a pass condition: at threshold most items, not all, are shown."
- statement: qaa/librarianship-information-knowledge-records-and-archives-management-2025/4.11.b13
  forPractitioner: { text: "In postgraduate certificate, diploma and master's courses, give students room to show they can appraise new technologies for managing information critically and put them to use, weighing their ethical consequences; at threshold they will have shown most such attributes to some degree.", rewrite: light, force: will, status: drafted }
  forBeneficiary: { text: "By the end of your postgraduate course, you will have shown that you can weigh up new technologies for managing information, use them well and think through their ethical effects.", rewrite: full, force: will, status: drafted }
  author-agent-written: "Treat this as a master's threshold attribute, also covering the postgraduate certificate and diploma, worded with \"will\", of which a threshold graduate will have shown most to some degree (4.11). It holds at FHEQ level 7 (FQHEIS level 11, which shares the FHEQ text) and concerns judging new technologies ethically. Cite it as (QAA, 2025, Librarianship, Information, Knowledge, Records and Archives Management Subject Benchmark Statement, para 4.11, thirteenth item). Do not present it as a regulatory requirement or as a standard for honours degrees, and set it beside its counterpart 4.7.b13 at the other award, the framework descriptor qaa/fheq-2024/4.17.b5 and spine:7 in the reference framework (std:ref:uk-framework, R8)."
  author-agent-dialogue: "Raise this when a postgraduate student asks what the course should leave them able to do about judging new technologies ethically, or plans work that draws on it. With a student, put it plainly in the second person; with staff, frame it as an outcome the course must give students the chance to show. Ask, for example: \"Which piece of your work so far best shows what you can do on judging new technologies ethically, and what would make it stronger?\" Avoid reading the issuer's list aloud, and do not treat one item as a pass condition: at threshold most items, not all, are shown."
- statement: qaa/librarianship-information-knowledge-records-and-archives-management-2025/4.11.b14
  forPractitioner: { text: "In postgraduate certificate, diploma and master's courses, give students room to show they can build, with teaching staff and community partners, full information literacy and reader development programmes for varied levels of skill and need, children, adults and lifelong learners included; at threshold they will have shown most such attributes to some degree.", rewrite: light, force: will, status: drafted }
  forBeneficiary: { text: "By the end of your postgraduate course, you will have shown that you can work with teachers and community partners to build information literacy and reading programmes for people at different levels, from children to adults and lifelong learners.", rewrite: full, force: will, status: drafted }
  author-agent-written: "Treat this as a master's threshold attribute, also covering the postgraduate certificate and diploma, worded with \"will\", of which a threshold graduate will have shown most to some degree (4.11). It holds at FHEQ level 7 (FQHEIS level 11, which shares the FHEQ text) and concerns information literacy and reader development programmes. Cite it as (QAA, 2025, Librarianship, Information, Knowledge, Records and Archives Management Subject Benchmark Statement, para 4.11, fourteenth item). Do not present it as a regulatory requirement or as a standard for honours degrees, and set it beside its counterpart 4.7.b14 at the other award, the framework descriptor qaa/fheq-2024/4.17.b5 and spine:7 in the reference framework (std:ref:uk-framework, R8)."
  author-agent-dialogue: "Raise this when a postgraduate student asks what the course should leave them able to do about information literacy and reader development programmes, or plans work that draws on it. With a student, put it plainly in the second person; with staff, frame it as an outcome the course must give students the chance to show. Ask, for example: \"Which piece of your work so far best shows what you can do on information literacy and reader development programmes, and what would make it stronger?\" Avoid reading the issuer's list aloud, and do not treat one item as a pass condition: at threshold most items, not all, are shown."
- statement: qaa/librarianship-information-knowledge-records-and-archives-management-2025/4.11.b15
  forPractitioner: { text: "In postgraduate certificate, diploma and master's courses, give students room to show they can adjust critical information literacy teaching to what different audiences need, children, adults and lifelong learners among them; at threshold they will have shown most such attributes to some degree.", rewrite: light, force: will, status: drafted }
  forBeneficiary: { text: "By the end of your postgraduate course, you will have shown that you can adjust how you teach critical information literacy to what different groups need, such as children, adults and lifelong learners.", rewrite: full, force: will, status: drafted }
  author-agent-written: "Treat this as a master's threshold attribute, also covering the postgraduate certificate and diploma, worded with \"will\", of which a threshold graduate will have shown most to some degree (4.11). It holds at FHEQ level 7 (FQHEIS level 11, which shares the FHEQ text) and concerns critical information literacy for varied audiences. Cite it as (QAA, 2025, Librarianship, Information, Knowledge, Records and Archives Management Subject Benchmark Statement, para 4.11, fifteenth item). Do not present it as a regulatory requirement or as a standard for honours degrees, and set it beside its counterpart 4.7.b16 at the other award, the framework descriptor qaa/fheq-2024/4.17.b5 and spine:7 in the reference framework (std:ref:uk-framework, R8)."
  author-agent-dialogue: "Raise this when a postgraduate student asks what the course should leave them able to do about critical information literacy for varied audiences, or plans work that draws on it. With a student, put it plainly in the second person; with staff, frame it as an outcome the course must give students the chance to show. Ask, for example: \"Which piece of your work so far best shows what you can do on critical information literacy for varied audiences, and what would make it stronger?\" Avoid reading the issuer's list aloud, and do not treat one item as a pass condition: at threshold most items, not all, are shown."
- statement: qaa/librarianship-information-knowledge-records-and-archives-management-2025/4.11.b16
  forPractitioner: { text: "In postgraduate certificate, diploma and master's courses, give students room to show they can plan teaching and outreach that build critical thinking, media literacy and safe, responsible participation online; at threshold they will have shown most such attributes to some degree.", rewrite: light, force: will, status: drafted }
  forBeneficiary: { text: "By the end of your postgraduate course, you will have shown that you can plan teaching and outreach sessions that help people think critically, read the media well and take part safely and responsibly online.", rewrite: full, force: will, status: drafted }
  author-agent-written: "Treat this as a master's threshold attribute, also covering the postgraduate certificate and diploma, worded with \"will\", of which a threshold graduate will have shown most to some degree (4.11). It holds at FHEQ level 7 (FQHEIS level 11, which shares the FHEQ text) and concerns teaching and outreach for critical thinking. Cite it as (QAA, 2025, Librarianship, Information, Knowledge, Records and Archives Management Subject Benchmark Statement, para 4.11, sixteenth item). Do not present it as a regulatory requirement or as a standard for honours degrees, and set it beside its counterpart 4.7.b15 at the other award, the framework descriptor qaa/fheq-2024/4.17.b5 and spine:7 in the reference framework (std:ref:uk-framework, R8)."
  author-agent-dialogue: "Raise this when a postgraduate student asks what the course should leave them able to do about teaching and outreach for critical thinking, or plans work that draws on it. With a student, put it plainly in the second person; with staff, frame it as an outcome the course must give students the chance to show. Ask, for example: \"Which piece of your work so far best shows what you can do on teaching and outreach for critical thinking, and what would make it stronger?\" Avoid reading the issuer's list aloud, and do not treat one item as a pass condition: at threshold most items, not all, are shown."
- statement: qaa/librarianship-information-knowledge-records-and-archives-management-2025/4.11.b17
  forPractitioner: { text: "In postgraduate certificate, diploma and master's courses, give students room to show they can gather and analyse data on users, service performance and sector trends, and use it to ground decisions in evidence and keep improving; at threshold they will have shown most such attributes to some degree.", rewrite: light, force: will, status: drafted }
  forBeneficiary: { text: "By the end of your postgraduate course, you will have shown that you can gather and analyse data about users, how services perform and trends in the sector, and use it to make decisions and keep improving.", rewrite: full, force: will, status: drafted }
  author-agent-written: "Treat this as a master's threshold attribute, also covering the postgraduate certificate and diploma, worded with \"will\", of which a threshold graduate will have shown most to some degree (4.11). It holds at FHEQ level 7 (FQHEIS level 11, which shares the FHEQ text) and concerns user data and metrics for evidence-based improvement. Cite it as (QAA, 2025, Librarianship, Information, Knowledge, Records and Archives Management Subject Benchmark Statement, para 4.11, seventeenth item). Do not present it as a regulatory requirement or as a standard for honours degrees, and set it beside its counterpart 4.7.b17 at the other award, the framework descriptor qaa/fheq-2024/4.17.b5 and spine:7 in the reference framework (std:ref:uk-framework, R8)."
  author-agent-dialogue: "Raise this when a postgraduate student asks what the course should leave them able to do about user data and metrics for evidence-based improvement, or plans work that draws on it. With a student, put it plainly in the second person; with staff, frame it as an outcome the course must give students the chance to show. Ask, for example: \"Which piece of your work so far best shows what you can do on user data and metrics for evidence-based improvement, and what would make it stronger?\" Avoid reading the issuer's list aloud, and do not treat one item as a pass condition: at threshold most items, not all, are shown."
- statement: qaa/librarianship-information-knowledge-records-and-archives-management-2025/4.11.b18
  forPractitioner: { text: "In postgraduate certificate, diploma and master's courses, give students room to show they can build a habit of experiment, testing how new technologies and approaches could improve information services; at threshold they will have shown most such attributes to some degree.", rewrite: light, force: will, status: drafted }
  forBeneficiary: { text: "By the end of your postgraduate course, you will have shown that you can encourage a habit of trying things out, testing how new technologies and ideas could improve information services.", rewrite: full, force: will, status: drafted }
  author-agent-written: "Treat this as a master's threshold attribute, also covering the postgraduate certificate and diploma, worded with \"will\", of which a threshold graduate will have shown most to some degree (4.11). It holds at FHEQ level 7 (FQHEIS level 11, which shares the FHEQ text) and concerns a culture of experiment in services. Cite it as (QAA, 2025, Librarianship, Information, Knowledge, Records and Archives Management Subject Benchmark Statement, para 4.11, eighteenth item). Do not present it as a regulatory requirement or as a standard for honours degrees, and set it beside the framework descriptor qaa/fheq-2024/4.17.b5 and spine:7 in the reference framework (std:ref:uk-framework, R8)."
  author-agent-dialogue: "Raise this when a postgraduate student asks what the course should leave them able to do about a culture of experiment in services, or plans work that draws on it. With a student, put it plainly in the second person; with staff, frame it as an outcome the course must give students the chance to show. Ask, for example: \"Which piece of your work so far best shows what you can do on a culture of experiment in services, and what would make it stronger?\" Avoid reading the issuer's list aloud, and do not treat one item as a pass condition: at threshold most items, not all, are shown."
- statement: qaa/librarianship-information-knowledge-records-and-archives-management-2025/4.11.b19
  forPractitioner: { text: "In postgraduate certificate, diploma and master's courses, give students room to show they can look actively for chances to be entrepreneurial, creating new information products, services or ventures; at threshold they will have shown most such attributes to some degree.", rewrite: light, force: will, status: drafted }
  forBeneficiary: { text: "By the end of your postgraduate course, you will have shown that you can look out for chances to be enterprising and create new information products, services or businesses.", rewrite: full, force: will, status: drafted }
  author-agent-written: "Treat this as a master's threshold attribute, also covering the postgraduate certificate and diploma, worded with \"will\", of which a threshold graduate will have shown most to some degree (4.11). It holds at FHEQ level 7 (FQHEIS level 11, which shares the FHEQ text) and concerns spotting openings for enterprise. Cite it as (QAA, 2025, Librarianship, Information, Knowledge, Records and Archives Management Subject Benchmark Statement, para 4.11, nineteenth item). Do not present it as a regulatory requirement or as a standard for honours degrees, and set it beside the framework descriptor qaa/fheq-2024/4.17.b5 and spine:7 in the reference framework (std:ref:uk-framework, R8)."
  author-agent-dialogue: "Raise this when a postgraduate student asks what the course should leave them able to do about spotting openings for enterprise, or plans work that draws on it. With a student, put it plainly in the second person; with staff, frame it as an outcome the course must give students the chance to show. Ask, for example: \"Which piece of your work so far best shows what you can do on spotting openings for enterprise, and what would make it stronger?\" Avoid reading the issuer's list aloud, and do not treat one item as a pass condition: at threshold most items, not all, are shown."
- statement: qaa/librarianship-information-knowledge-records-and-archives-management-2025/4.11.b20
  forPractitioner: { text: "In postgraduate certificate, diploma and master's courses, give students room to show they can try out AI tools for automated work such as metadata generation and recommender systems, keeping ethical oversight in place; at threshold they will have shown most such attributes to some degree.", rewrite: light, force: will, status: drafted }
  forBeneficiary: { text: "By the end of your postgraduate course, you will have shown that you can try out AI tools for automatic tasks, such as creating metadata or recommending resources, while keeping an ethical check on how they are used.", rewrite: full, force: will, status: drafted }
  author-agent-written: "Treat this as a master's threshold attribute, also covering the postgraduate certificate and diploma, worded with \"will\", of which a threshold graduate will have shown most to some degree (4.11). It holds at FHEQ level 7 (FQHEIS level 11, which shares the FHEQ text) and concerns AI tools for automated tasks, with ethical oversight. Cite it as (QAA, 2025, Librarianship, Information, Knowledge, Records and Archives Management Subject Benchmark Statement, para 4.11, twentieth item). Do not present it as a regulatory requirement or as a standard for honours degrees, and set it beside its counterpart 4.7.b18 at the other award, the framework descriptor qaa/fheq-2024/4.17.b5 and spine:7 in the reference framework (std:ref:uk-framework, R8)."
  author-agent-dialogue: "Raise this when a postgraduate student asks what the course should leave them able to do about AI tools for automated tasks, with ethical oversight, or plans work that draws on it. With a student, put it plainly in the second person; with staff, frame it as an outcome the course must give students the chance to show. Ask, for example: \"Which piece of your work so far best shows what you can do on AI tools for automated tasks, with ethical oversight, and what would make it stronger?\" Avoid reading the issuer's list aloud, and do not treat one item as a pass condition: at threshold most items, not all, are shown."
- statement: qaa/librarianship-information-knowledge-records-and-archives-management-2025/4.11.b21
  forPractitioner: { text: "In postgraduate certificate, diploma and master's courses, give students room to show they can stand up for freedom of thought and expression, for the privacy of personal data, and for open access to information and data; at threshold they will have shown most such attributes to some degree.", rewrite: light, force: will, status: drafted }
  forBeneficiary: { text: "By the end of your postgraduate course, you will have shown that you can stand up for people's freedom of thought and expression, for the privacy of their data, and for open access to information and data.", rewrite: full, force: will, status: drafted }
  author-agent-written: "Treat this as a master's threshold attribute, also covering the postgraduate certificate and diploma, worded with \"will\", of which a threshold graduate will have shown most to some degree (4.11). It holds at FHEQ level 7 (FQHEIS level 11, which shares the FHEQ text) and concerns intellectual freedom, privacy and openness. Cite it as (QAA, 2025, Librarianship, Information, Knowledge, Records and Archives Management Subject Benchmark Statement, para 4.11, twenty-first item). Do not present it as a regulatory requirement or as a standard for honours degrees, and set it beside its counterpart 4.7.b19 at the other award, the framework descriptor qaa/fheq-2024/4.17.b5 and spine:7 in the reference framework (std:ref:uk-framework, R8)."
  author-agent-dialogue: "Raise this when a postgraduate student asks what the course should leave them able to do about intellectual freedom, privacy and openness, or plans work that draws on it. With a student, put it plainly in the second person; with staff, frame it as an outcome the course must give students the chance to show. Ask, for example: \"Which piece of your work so far best shows what you can do on intellectual freedom, privacy and openness, and what would make it stronger?\" Avoid reading the issuer's list aloud, and do not treat one item as a pass condition: at threshold most items, not all, are shown."
- statement: qaa/librarianship-information-knowledge-records-and-archives-management-2025/4.11.b22
  forPractitioner: { text: "In postgraduate certificate, diploma and master's courses, give students room to show they can help shape organisational policy on ethical information practice, responsible data governance and the rights of users; at threshold they will have shown most such attributes to some degree.", rewrite: light, force: will, status: drafted }
  forBeneficiary: { text: "By the end of your postgraduate course, you will have shown that you can help write your organisation's policies on the ethical use of information, careful handling of data and the rights of its users.", rewrite: full, force: will, status: drafted }
  author-agent-written: "Treat this as a master's threshold attribute, also covering the postgraduate certificate and diploma, worded with \"will\", of which a threshold graduate will have shown most to some degree (4.11). It holds at FHEQ level 7 (FQHEIS level 11, which shares the FHEQ text) and concerns organisational policy on information ethics. Cite it as (QAA, 2025, Librarianship, Information, Knowledge, Records and Archives Management Subject Benchmark Statement, para 4.11, twenty-second item). Do not present it as a regulatory requirement or as a standard for honours degrees, and set it beside its counterpart 4.7.b20 at the other award, the framework descriptor qaa/fheq-2024/4.17.b5 and spine:7 in the reference framework (std:ref:uk-framework, R8)."
  author-agent-dialogue: "Raise this when a postgraduate student asks what the course should leave them able to do about organisational policy on information ethics, or plans work that draws on it. With a student, put it plainly in the second person; with staff, frame it as an outcome the course must give students the chance to show. Ask, for example: \"Which piece of your work so far best shows what you can do on organisational policy on information ethics, and what would make it stronger?\" Avoid reading the issuer's list aloud, and do not treat one item as a pass condition: at threshold most items, not all, are shown."
- statement: qaa/librarianship-information-knowledge-records-and-archives-management-2025/4.11.b23
  forPractitioner: { text: "In postgraduate certificate, diploma and master's courses, give students room to show they can take part in local and national campaigning for laws that widen fair access to information and protect users' privacy; at threshold they will have shown most such attributes to some degree.", rewrite: light, force: will, status: drafted }
  forBeneficiary: { text: "By the end of your postgraduate course, you will have shown that you can take part in local and national campaigns for laws that give people fair access to information and protect their privacy.", rewrite: full, force: will, status: drafted }
  author-agent-written: "Treat this as a master's threshold attribute, also covering the postgraduate certificate and diploma, worded with \"will\", of which a threshold graduate will have shown most to some degree (4.11). It holds at FHEQ level 7 (FQHEIS level 11, which shares the FHEQ text) and concerns advocacy for fair access and privacy law. Cite it as (QAA, 2025, Librarianship, Information, Knowledge, Records and Archives Management Subject Benchmark Statement, para 4.11, twenty-third item). Do not present it as a regulatory requirement or as a standard for honours degrees, and set it beside its counterpart 4.7.b21 at the other award, the framework descriptor qaa/fheq-2024/4.17.b5 and spine:7 in the reference framework (std:ref:uk-framework, R8)."
  author-agent-dialogue: "Raise this when a postgraduate student asks what the course should leave them able to do about advocacy for fair access and privacy law, or plans work that draws on it. With a student, put it plainly in the second person; with staff, frame it as an outcome the course must give students the chance to show. Ask, for example: \"Which piece of your work so far best shows what you can do on advocacy for fair access and privacy law, and what would make it stronger?\" Avoid reading the issuer's list aloud, and do not treat one item as a pass condition: at threshold most items, not all, are shown."
- statement: qaa/librarianship-information-knowledge-records-and-archives-management-2025/4.11.b24
  forPractitioner: { text: "In postgraduate certificate, diploma and master's courses, give students room to show they can use strategic analysis and leadership to deliver, track and judge initiatives and grasp their effect on the communities or users concerned; at threshold they will have shown most such attributes to some degree.", rewrite: light, force: will, status: drafted }
  forBeneficiary: { text: "By the end of your postgraduate course, you will have shown that you can use strategic thinking and leadership to run, track and judge projects, and understand what they mean for the people they serve.", rewrite: full, force: will, status: drafted }
  author-agent-written: "Treat this as a master's threshold attribute, also covering the postgraduate certificate and diploma, worded with \"will\", of which a threshold graduate will have shown most to some degree (4.11). It holds at FHEQ level 7 (FQHEIS level 11, which shares the FHEQ text) and concerns strategic leadership of initiatives. Cite it as (QAA, 2025, Librarianship, Information, Knowledge, Records and Archives Management Subject Benchmark Statement, para 4.11, twenty-fourth item). Do not present it as a regulatory requirement or as a standard for honours degrees, and set it beside the framework descriptor qaa/fheq-2024/4.17.b5 and spine:7 in the reference framework (std:ref:uk-framework, R8)."
  author-agent-dialogue: "Raise this when a postgraduate student asks what the course should leave them able to do about strategic leadership of initiatives, or plans work that draws on it. With a student, put it plainly in the second person; with staff, frame it as an outcome the course must give students the chance to show. Ask, for example: \"Which piece of your work so far best shows what you can do on strategic leadership of initiatives, and what would make it stronger?\" Avoid reading the issuer's list aloud, and do not treat one item as a pass condition: at threshold most items, not all, are shown."
- statement: qaa/librarianship-information-knowledge-records-and-archives-management-2025/4.11.b25
  forPractitioner: { text: "In postgraduate certificate, diploma and master's courses, give students room to show they can draw on results to shape future services and outreach; at threshold they will have shown most such attributes to some degree.", rewrite: light, force: will, status: drafted }
  forBeneficiary: { text: "By the end of your postgraduate course, you will have shown that you can use what your projects achieved to shape future services and outreach.", rewrite: full, force: will, status: drafted }
  author-agent-written: "Treat this as a master's threshold attribute, also covering the postgraduate certificate and diploma, worded with \"will\", of which a threshold graduate will have shown most to some degree (4.11). It holds at FHEQ level 7 (FQHEIS level 11, which shares the FHEQ text) and concerns using results to plan future services. Cite it as (QAA, 2025, Librarianship, Information, Knowledge, Records and Archives Management Subject Benchmark Statement, para 4.11, twenty-fifth item). Do not present it as a regulatory requirement or as a standard for honours degrees, and set it beside the framework descriptor qaa/fheq-2024/4.17.b5 and spine:7 in the reference framework (std:ref:uk-framework, R8)."
  author-agent-dialogue: "Raise this when a postgraduate student asks what the course should leave them able to do about using results to plan future services, or plans work that draws on it. With a student, put it plainly in the second person; with staff, frame it as an outcome the course must give students the chance to show. Ask, for example: \"Which piece of your work so far best shows what you can do on using results to plan future services, and what would make it stronger?\" Avoid reading the issuer's list aloud, and do not treat one item as a pass condition: at threshold most items, not all, are shown."
- statement: qaa/librarianship-information-knowledge-records-and-archives-management-2025/4.12.b1
  forPractitioner: { text: "Postgraduate students should be able to show a full grasp of the research techniques their own research or advanced study needs, and a sound use of fitting research philosophies and methods; build it into the research and project work of the course.", rewrite: light, force: should, status: drafted }
  forBeneficiary: { text: "By the end of your master's course, you should be able to show a full understanding of the research techniques your own research needs, and that you can use suitable research philosophies and methods.", rewrite: full, force: should, status: drafted }
  author-agent-written: "Treat this as a generic skill: a master's threshold attribute, also covering the postgraduate certificate and diploma, worded with \"should\". It holds at FHEQ level 7 (FQHEIS level 11, which shares the FHEQ text) and concerns research techniques and philosophies. Cite it as (QAA, 2025, Librarianship, Information, Knowledge, Records and Archives Management Subject Benchmark Statement, para 4.12, first item). Do not present it as a regulatory requirement or as a standard for honours degrees, and set it beside the framework descriptor qaa/fheq-2024/4.17.b2 and spine:7 in the reference framework (std:ref:uk-framework, R8)."
  author-agent-dialogue: "Raise this when a postgraduate student asks what the course should leave them able to do about research techniques and philosophies, or plans work that draws on it. With a student, put it plainly in the second person; with staff, frame it as an outcome the course must give students the chance to show. Ask, for example: \"Which piece of your work so far best shows what you can do on research techniques and philosophies, and what would make it stronger?\" Avoid reading the issuer's list aloud, and do not treat one item as a pass condition: at threshold most items, not all, are shown."
- statement: qaa/librarianship-information-knowledge-records-and-archives-management-2025/4.12.b2
  forPractitioner: { text: "Postgraduate students should be able to show originality in the way they put knowledge to use; build it into the research and project work of the course.", rewrite: light, force: should, status: drafted }
  forBeneficiary: { text: "By the end of your master's course, you should be able to show originality in how you put your knowledge to use.", rewrite: full, force: should, status: drafted }
  author-agent-written: "Treat this as a generic skill: a master's threshold attribute, also covering the postgraduate certificate and diploma, worded with \"should\". It holds at FHEQ level 7 (FQHEIS level 11, which shares the FHEQ text) and concerns originality in applying knowledge. Cite it as (QAA, 2025, Librarianship, Information, Knowledge, Records and Archives Management Subject Benchmark Statement, para 4.12, second item). Do not present it as a regulatory requirement or as a standard for honours degrees, and set it beside the framework descriptor qaa/fheq-2024/4.17.b3 and spine:7 in the reference framework (std:ref:uk-framework, R8)."
  author-agent-dialogue: "Raise this when a postgraduate student asks what the course should leave them able to do about originality in applying knowledge, or plans work that draws on it. With a student, put it plainly in the second person; with staff, frame it as an outcome the course must give students the chance to show. Ask, for example: \"Which piece of your work so far best shows what you can do on originality in applying knowledge, and what would make it stronger?\" Avoid reading the issuer's list aloud, and do not treat one item as a pass condition: at threshold most items, not all, are shown."
- statement: qaa/librarianship-information-knowledge-records-and-archives-management-2025/4.12.b3
  forPractitioner: { text: "Postgraduate students should be able to show a working grasp of how established research and enquiry produce and test evidence that improves professional practice; build it into the research and project work of the course.", rewrite: light, force: should, status: drafted }
  forBeneficiary: { text: "By the end of your master's course, you should be able to show that you understand in practice how research methods produce and test evidence that improves professional work.", rewrite: full, force: should, status: drafted }
  author-agent-written: "Treat this as a generic skill: a master's threshold attribute, also covering the postgraduate certificate and diploma, worded with \"should\". It holds at FHEQ level 7 (FQHEIS level 11, which shares the FHEQ text) and concerns research as evidence for professional practice. Cite it as (QAA, 2025, Librarianship, Information, Knowledge, Records and Archives Management Subject Benchmark Statement, para 4.12, third item). Do not present it as a regulatory requirement or as a standard for honours degrees, and set it beside the framework descriptor qaa/fheq-2024/4.17.b3 and spine:7 in the reference framework (std:ref:uk-framework, R8)."
  author-agent-dialogue: "Raise this when a postgraduate student asks what the course should leave them able to do about research as evidence for professional practice, or plans work that draws on it. With a student, put it plainly in the second person; with staff, frame it as an outcome the course must give students the chance to show. Ask, for example: \"Which piece of your work so far best shows what you can do on research as evidence for professional practice, and what would make it stronger?\" Avoid reading the issuer's list aloud, and do not treat one item as a pass condition: at threshold most items, not all, are shown."
- statement: qaa/librarianship-information-knowledge-records-and-archives-management-2025/4.12.b4
  forPractitioner: { text: "Postgraduate students should be able to show that they can carry through, by independent study, a substantial critical piece of empirical research, a work-based project, a major review or a case study, which may add to research or solve a workplace problem; build it into the research and project work of the course.", rewrite: light, force: should, status: drafted }
  forBeneficiary: { text: "By the end of your master's course, you should be able to show that you can complete on your own a substantial piece of critical research, a work-based project, a major review or a case study, which might add to research or solve a problem at work.", rewrite: full, force: should, status: drafted }
  author-agent-written: "Treat this as a generic skill: a master's threshold attribute, also covering the postgraduate certificate and diploma, worded with \"should\". It holds at FHEQ level 7 (FQHEIS level 11, which shares the FHEQ text) and concerns an independent substantial project. Cite it as (QAA, 2025, Librarianship, Information, Knowledge, Records and Archives Management Subject Benchmark Statement, para 4.12, fourth item). Do not present it as a regulatory requirement or as a standard for honours degrees, and set it beside the framework descriptor qaa/fheq-2024/4.17.b6 and spine:7 in the reference framework (std:ref:uk-framework, R8)."
  author-agent-dialogue: "Raise this when a postgraduate student asks what the course should leave them able to do about an independent substantial project, or plans work that draws on it. With a student, put it plainly in the second person; with staff, frame it as an outcome the course must give students the chance to show. Ask, for example: \"Which piece of your work so far best shows what you can do on an independent substantial project, and what would make it stronger?\" Avoid reading the issuer's list aloud, and do not treat one item as a pass condition: at threshold most items, not all, are shown."
- statement: qaa/librarianship-information-knowledge-records-and-archives-management-2025/4.12.b6
  forPractitioner: { text: "Postgraduate students should be able to show a conceptual grasp that lets them judge current research and advanced scholarship in the field critically; build it into the research and project work of the course.", rewrite: light, force: should, status: drafted }
  forBeneficiary: { text: "By the end of your master's course, you should be able to show an understanding of ideas deep enough to judge current research and advanced study in your field critically.", rewrite: full, force: should, status: drafted }
  author-agent-written: "Treat this as a generic skill: a master's threshold attribute, also covering the postgraduate certificate and diploma, worded with \"should\". It holds at FHEQ level 7 (FQHEIS level 11, which shares the FHEQ text) and concerns evaluating current research critically. Cite it as (QAA, 2025, Librarianship, Information, Knowledge, Records and Archives Management Subject Benchmark Statement, para 4.12, sixth item). Do not present it as a regulatory requirement or as a standard for honours degrees, and set it beside the framework descriptor qaa/fheq-2024/4.17.b4.1 and spine:7 in the reference framework (std:ref:uk-framework, R8)."
  author-agent-dialogue: "Raise this when a postgraduate student asks what the course should leave them able to do about evaluating current research critically, or plans work that draws on it. With a student, put it plainly in the second person; with staff, frame it as an outcome the course must give students the chance to show. Ask, for example: \"Which piece of your work so far best shows what you can do on evaluating current research critically, and what would make it stronger?\" Avoid reading the issuer's list aloud, and do not treat one item as a pass condition: at threshold most items, not all, are shown."
- statement: qaa/librarianship-information-knowledge-records-and-archives-management-2025/4.12.b7
  forPractitioner: { text: "Postgraduate students should be able to show a conceptual grasp that lets them assess and critique research methods and, where fitting, put forward new hypotheses, which may mean knowing methods from neighbouring fields; build it into the research and project work of the course.", rewrite: light, force: should, status: drafted }
  forBeneficiary: { text: "By the end of your master's course, you should be able to show an understanding of ideas deep enough to assess and critique research methods and, where it fits, suggest new hypotheses, perhaps drawing on methods from related subjects.", rewrite: full, force: should, status: drafted }
  author-agent-written: "Treat this as a generic skill: a master's threshold attribute, also covering the postgraduate certificate and diploma, worded with \"should\". It holds at FHEQ level 7 (FQHEIS level 11, which shares the FHEQ text) and concerns critiquing methods and proposing hypotheses. Cite it as (QAA, 2025, Librarianship, Information, Knowledge, Records and Archives Management Subject Benchmark Statement, para 4.12, seventh item). Do not present it as a regulatory requirement or as a standard for honours degrees, and set it beside the framework descriptor qaa/fheq-2024/4.17.b4.2 and spine:7 in the reference framework (std:ref:uk-framework, R8)."
  author-agent-dialogue: "Raise this when a postgraduate student asks what the course should leave them able to do about critiquing methods and proposing hypotheses, or plans work that draws on it. With a student, put it plainly in the second person; with staff, frame it as an outcome the course must give students the chance to show. Ask, for example: \"Which piece of your work so far best shows what you can do on critiquing methods and proposing hypotheses, and what would make it stronger?\" Avoid reading the issuer's list aloud, and do not treat one item as a pass condition: at threshold most items, not all, are shown."
- statement: qaa/librarianship-information-knowledge-records-and-archives-management-2025/4.12.b8
  forPractitioner: { text: "Postgraduate students should be able to show that they can handle complex issues both methodically and inventively, judge soundly when data are incomplete, and explain their conclusions plainly to expert and general audiences; build it into the research and project work of the course.", rewrite: light, force: should, status: drafted }
  forBeneficiary: { text: "By the end of your master's course, you should be able to show that you can handle complex issues methodically and creatively, judge well when you lack some of the data, and explain your conclusions clearly to experts and non-experts.", rewrite: full, force: should, status: drafted }
  author-agent-written: "Treat this as a generic skill: a master's threshold attribute, also covering the postgraduate certificate and diploma, worded with \"should\". It holds at FHEQ level 7 (FQHEIS level 11, which shares the FHEQ text) and concerns complex issues, judgement and clear communication. Cite it as (QAA, 2025, Librarianship, Information, Knowledge, Records and Archives Management Subject Benchmark Statement, para 4.12, eighth item). Do not present it as a regulatory requirement or as a standard for honours degrees, and set it beside the framework descriptor qaa/fheq-2024/4.17.b5 and spine:7 in the reference framework (std:ref:uk-framework, R8)."
  author-agent-dialogue: "Raise this when a postgraduate student asks what the course should leave them able to do about complex issues, judgement and clear communication, or plans work that draws on it. With a student, put it plainly in the second person; with staff, frame it as an outcome the course must give students the chance to show. Ask, for example: \"Which piece of your work so far best shows what you can do on complex issues, judgement and clear communication, and what would make it stronger?\" Avoid reading the issuer's list aloud, and do not treat one item as a pass condition: at threshold most items, not all, are shown."
- statement: qaa/librarianship-information-knowledge-records-and-archives-management-2025/4.12.b9
  forPractitioner: { text: "Postgraduate students should be able to show that they direct themselves and work with creativity and originality; build it into the research and project work of the course.", rewrite: light, force: should, status: drafted }
  forBeneficiary: { text: "By the end of your master's course, you should be able to show that you direct your own work and bring creativity and originality to it.", rewrite: full, force: should, status: drafted }
  author-agent-written: "Treat this as a generic skill: a master's threshold attribute, also covering the postgraduate certificate and diploma, worded with \"should\". It holds at FHEQ level 7 (FQHEIS level 11, which shares the FHEQ text) and concerns self-direction and originality. Cite it as (QAA, 2025, Librarianship, Information, Knowledge, Records and Archives Management Subject Benchmark Statement, para 4.12, ninth item). Do not present it as a regulatory requirement or as a standard for honours degrees, and set it beside the framework descriptor qaa/fheq-2024/4.17.b6 and spine:7 in the reference framework (std:ref:uk-framework, R8)."
  author-agent-dialogue: "Raise this when a postgraduate student asks what the course should leave them able to do about self-direction and originality, or plans work that draws on it. With a student, put it plainly in the second person; with staff, frame it as an outcome the course must give students the chance to show. Ask, for example: \"Which piece of your work so far best shows what you can do on self-direction and originality, and what would make it stronger?\" Avoid reading the issuer's list aloud, and do not treat one item as a pass condition: at threshold most items, not all, are shown."
- statement: qaa/librarianship-information-knowledge-records-and-archives-management-2025/4.12.b10
  forPractitioner: { text: "Postgraduate students should be able to show skill in leading and advocating, aware of the shifting internal and external factors that bear on both; build it into the research and project work of the course.", rewrite: light, force: should, status: drafted }
  forBeneficiary: { text: "By the end of your master's course, you should be able to show that you can lead and speak up for a cause, aware of the changing pressures inside and outside an organisation that affect both.", rewrite: full, force: should, status: drafted }
  author-agent-written: "Treat this as a generic skill: a master's threshold attribute, also covering the postgraduate certificate and diploma, worded with \"should\". It holds at FHEQ level 7 (FQHEIS level 11, which shares the FHEQ text) and concerns leadership and advocacy. Cite it as (QAA, 2025, Librarianship, Information, Knowledge, Records and Archives Management Subject Benchmark Statement, para 4.12, tenth item). Do not present it as a regulatory requirement or as a standard for honours degrees, and set it beside the framework descriptor qaa/fheq-2024/4.17.b8.1 and spine:7 in the reference framework (std:ref:uk-framework, R8)."
  author-agent-dialogue: "Raise this when a postgraduate student asks what the course should leave them able to do about leadership and advocacy, or plans work that draws on it. With a student, put it plainly in the second person; with staff, frame it as an outcome the course must give students the chance to show. Ask, for example: \"Which piece of your work so far best shows what you can do on leadership and advocacy, and what would make it stronger?\" Avoid reading the issuer's list aloud, and do not treat one item as a pass condition: at threshold most items, not all, are shown."
- statement: qaa/librarianship-information-knowledge-records-and-archives-management-2025/4.12.b11
  forPractitioner: { text: "Postgraduate students should be able to show that they can use tools and processes to network effectively across the world; build it into the research and project work of the course.", rewrite: light, force: should, status: drafted }
  forBeneficiary: { text: "By the end of your master's course, you should be able to show that you can use tools and processes to build useful professional networks worldwide.", rewrite: full, force: should, status: drafted }
  author-agent-written: "Treat this as a generic skill: a master's threshold attribute, also covering the postgraduate certificate and diploma, worded with \"should\". It holds at FHEQ level 7 (FQHEIS level 11, which shares the FHEQ text) and concerns networking globally. Cite it as (QAA, 2025, Librarianship, Information, Knowledge, Records and Archives Management Subject Benchmark Statement, para 4.12, eleventh item). Do not present it as a regulatory requirement or as a standard for honours degrees, and set it beside the framework descriptor qaa/fheq-2024/4.17.b8.3 and spine:7 in the reference framework (std:ref:uk-framework, R8)."
  author-agent-dialogue: "Raise this when a postgraduate student asks what the course should leave them able to do about networking globally, or plans work that draws on it. With a student, put it plainly in the second person; with staff, frame it as an outcome the course must give students the chance to show. Ask, for example: \"Which piece of your work so far best shows what you can do on networking globally, and what would make it stronger?\" Avoid reading the issuer's list aloud, and do not treat one item as a pass condition: at threshold most items, not all, are shown."
- statement: qaa/librarianship-information-knowledge-records-and-archives-management-2025/4.12.b12
  forPractitioner: { text: "Postgraduate students should be able to show that they can question current practice and make the case for the changes they propose; build it into the research and project work of the course.", rewrite: light, force: should, status: drafted }
  forBeneficiary: { text: "By the end of your master's course, you should be able to show that you can question how things are done now and make the case for the changes you propose.", rewrite: full, force: should, status: drafted }
  author-agent-written: "Treat this as a generic skill: a master's threshold attribute, also covering the postgraduate certificate and diploma, worded with \"should\". It holds at FHEQ level 7 (FQHEIS level 11, which shares the FHEQ text) and concerns challenging practice and justifying change. Cite it as (QAA, 2025, Librarianship, Information, Knowledge, Records and Archives Management Subject Benchmark Statement, para 4.12, twelfth item). Do not present it as a regulatory requirement or as a standard for honours degrees, and set it beside the framework descriptor qaa/fheq-2024/4.17.b5 and spine:7 in the reference framework (std:ref:uk-framework, R8)."
  author-agent-dialogue: "Raise this when a postgraduate student asks what the course should leave them able to do about challenging practice and justifying change, or plans work that draws on it. With a student, put it plainly in the second person; with staff, frame it as an outcome the course must give students the chance to show. Ask, for example: \"Which piece of your work so far best shows what you can do on challenging practice and justifying change, and what would make it stronger?\" Avoid reading the issuer's list aloud, and do not treat one item as a pass condition: at threshold most items, not all, are shown."
```

### S5 Levels and alignment
<!-- label: both; status: drafted; basis: primary -->
```yaml
levels:
  - { id: "fheq:6", role: "cites", locator: "D1, 2.4 (undergraduate degree with honours)" }
  - { id: "fqheis:10", role: "cites", locator: "D1, 2.4" }
  - { id: "fheq:7", role: "cites", locator: "D1, 2.4 (integrated master's); the level of 4.9 to 4.12 is inferred from the awards named (Part E)" }
  - { id: "fqheis:11", role: "cites", locator: "D1, 2.4" }
  - { id: "fheq:4", role: "cites", locator: "D1, 2.7 (Certificate of Higher Education)" }
  - { id: "fheq:5", role: "cites", locator: "D1, 2.7 (Diploma of Higher Education)" }
  - { id: "fqheis:8", role: "cites", locator: "D1, 2.7, set beside the CertHE (Part E)" }
  - { id: "fqheis:9", role: "cites", locator: "D1, 2.7, set beside the DipHE (Part E)" }
crosswalks:
  - { from: "fheq:6", to: "fqheis:10", relation: "equivalent", basis: "stated (D1, 2.4); agrees with FHEQ Table 1" }
  - { from: "fheq:7", to: "fqheis:11", relation: "equivalent", basis: "stated (D1, 2.4); agrees with FHEQ Table 1" }
  - { from: "fheq:4", to: "fqheis:8", relation: "equivalent", basis: "stated (D1, 2.7); conflicts with FHEQ Table 1, which places the CertHE at fqheis:7 (Part E)" }
  - { from: "fheq:5", to: "fqheis:9", relation: "equivalent", basis: "stated (D1, 2.7); conflicts with FHEQ Table 1, which places the DipHE at fqheis:8 (Part E)" }
```

### S6 Themes
<!-- label: both; status: drafted; basis: primary -->
```yaml
- { id: "theme:edi", role: "carries", carriedIn: ["1.3", "1.4", "1.7", "1.8", "1.9", "1.10", "2.2"] }
- { id: "theme:accessibility", role: "carries", carriedIn: ["1.3", "1.4", "1.11", "2.9", "3.9"] }
- { id: "theme:esd", role: "carries", carriedIn: ["1.3", "1.4", "1.12", "1.13", "1.14", "1.20"] }
- { id: "theme:enterprise", role: "carries", carriedIn: ["1.3", "1.15", "1.16", "1.17", "1.18", "1.19", "3.10"] }
- { id: "theme:generative-ai", role: "carries", carriedIn: ["1.3", "1.20", "1.21", "3.10"] }
```

### S7 Relations
<!-- label: both; status: drafted; basis: primary -->
```yaml
- { rel: "partOf", target: "collection: QAA Subject Benchmark Statements", note: "one of 54 held by stan" }
- { rel: "supersedes", target: "std:doc:qaa-librarianship-information-knowledge-records-and-archives-management-<previous year>-benchmarks (not yet ingested)", note: "the front matter names key changes from the previous statement; section 6 names a 2019 minor update (Part E)" }
- { rel: "refersTo", target: "std:doc:qaa-fheq-2024-framework, Annex D", note: "the degree outcome classification descriptions for bachelor's degrees with honours (4.2)" }
- { rel: "refersTo", target: "std:doc:qaa-fheq-2024-framework", note: "FHEQ levels 4 to 7 (2.4, 2.7)" }
- { rel: "refersTo", target: "std:doc:qaa-fqheis-2024-framework", note: "FQHEIS levels 8 to 11 (2.4, 2.7)" }
- { rel: "refersTo", target: "QAA guidance on inclusive subject learning communities (not yet ingested)", note: "1.11" }
- { rel: "refersTo", target: "CILIP Professional Knowledge and Skills Base (not yet ingested)", note: "1.18, 2.15" }
- { rel: "refersTo", target: "CILIP Ethical Framework; ARA Code of Ethics (not yet ingested)", note: "1.21, 2.1" }
- { rel: "refersTo", target: "ARA Competency Framework (not yet ingested)", note: "2.15" }
- { rel: "themeReference", target: "theme:esd", note: "the UN Sustainable Development Goals, six named (1.12)" }
```

### S8 Currency and review
<!-- label: source; status: drafted; basis: primary -->
```yaml
published: "2025-04"
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
- A family of related disciplines concerned with representing, organising and communicating knowledge so that anyone can find, use, judge and share the information they need (D1, 1.7)
- Practice-based and vocational as well as academic, with many entering through postgraduate study; the field is mostly studied at postgraduate level (D1, front matter; 1.17; 2.2)
- Information itself is the object of study, so students turn a critical eye on their own use of it and on how sources change (D1, 2.3)
- Rests on distinctive ethical foundations set out by the professional bodies and on long-standing law, such as copyright, equalities, data protection and freedom of information (D1, 2.1)
- Social justice runs through it: tackling bias in collections and systems, decolonising practice and working for fair access for groups once marginalised (D1, 1.4; 1.9; 1.10)
- Combines theory with practice through case studies, problem-based learning, placements and partnerships with the profession (D1, 1.4; 2.14; 3.5)
- Technologically fluent: metadata, repositories, user experience, data and, increasingly, AI tools, always with ethical oversight (D1, 1.3; 1.4; 1.21)
- Careers span libraries in many sectors, archives and records work, curation, information governance and knowledge management (D1, 2.1; 2.13)

### SB2 Themes in this subject
<!-- label: both; status: drafted; basis: primary -->
```yaml
- theme: theme:edi
  inThisSubject: "Fair, unbiased access is the ethical core of the field: graduates work against bias in collections and knowledge systems, decolonise practice and serve marginalised groups (D1, 1.7 to 1.10)"
  statements: ["qaa/librarianship-information-knowledge-records-and-archives-management-2025/4.7.b1", "qaa/librarianship-information-knowledge-records-and-archives-management-2025/4.7.b2", "qaa/librarianship-information-knowledge-records-and-archives-management-2025/4.7.b3", "qaa/librarianship-information-knowledge-records-and-archives-management-2025/4.7.b4", "qaa/librarianship-information-knowledge-records-and-archives-management-2025/4.7.b5", "qaa/librarianship-information-knowledge-records-and-archives-management-2025/4.11.b2", "qaa/librarianship-information-knowledge-records-and-archives-management-2025/4.11.b3", "qaa/librarianship-information-knowledge-records-and-archives-management-2025/4.11.b4", "qaa/librarianship-information-knowledge-records-and-archives-management-2025/4.11.b5"]
- theme: theme:accessibility
  inThisSubject: "Accessibility is both how courses are run (varied, flexible, inclusive methods) and what graduates build (accessible systems, spaces and interfaces) (D1, 1.11; 2.9; 3.9)"
  statements: ["qaa/librarianship-information-knowledge-records-and-archives-management-2025/4.7.b2", "qaa/librarianship-information-knowledge-records-and-archives-management-2025/4.7.b3", "qaa/librarianship-information-knowledge-records-and-archives-management-2025/4.7.b11", "qaa/librarianship-information-knowledge-records-and-archives-management-2025/4.7.b12", "qaa/librarianship-information-knowledge-records-and-archives-management-2025/4.11.b3", "qaa/librarianship-information-knowledge-records-and-archives-management-2025/4.11.b11", "qaa/librarianship-information-knowledge-records-and-archives-management-2025/4.11.b12"]
- theme: theme:esd
  inThisSubject: "Preserving and giving access to recorded knowledge and heritage is itself a contribution to sustainability, with the UN goals and sector initiatives named (D1, 1.12 to 1.14)"
  statements: ["qaa/librarianship-information-knowledge-records-and-archives-management-2025/4.8.b17", "qaa/librarianship-information-knowledge-records-and-archives-management-2025/4.7.b7", "qaa/librarianship-information-knowledge-records-and-archives-management-2025/4.11.b6", "qaa/librarianship-information-knowledge-records-and-archives-management-2025/4.11.b8"]
- theme: theme:enterprise
  inThisSubject: "Enterprise is treated as core: service design, innovation and practical action, with authentic assessment and the professional skills base behind it (D1, 1.15 to 1.19)"
  statements: ["qaa/librarianship-information-knowledge-records-and-archives-management-2025/4.11.b18", "qaa/librarianship-information-knowledge-records-and-archives-management-2025/4.11.b19", "qaa/librarianship-information-knowledge-records-and-archives-management-2025/3.10.b3"]
- theme: theme:generative-ai
  inThisSubject: "AI is both a subject of critical, ethical study and a set of tools for metadata, discovery and services; students learn to use it and to teach others about it (D1, 1.20; 1.21)"
  statements: ["qaa/librarianship-information-knowledge-records-and-archives-management-2025/4.7.b18", "qaa/librarianship-information-knowledge-records-and-archives-management-2025/4.11.b20", "qaa/librarianship-information-knowledge-records-and-archives-management-2025/3.10.b5"]
```

### SB3 Content and delivery
<!-- label: both; status: drafted; basis: primary -->
```yaml
areas:
  - { component: "1.3", gloss: "seven areas courses are likely to address: safeguarding knowledge and records; the digital landscape; literacies; information equity; innovation; information rights; strategic thinking" }
  - { component: "1.4", gloss: "usual characteristics: interdisciplinarity, law and ethics, data ethics, theory with practice, user experience, social justice, technical fluency, lifelong learning" }
  - { component: "3.1", gloss: "breadth and depth vary by course and specialism" }
  - { component: "3.2", gloss: "the content gives every graduate a broad, relevant base" }
practices:
  - { component: "1.5", kind: "teaching", gloss: "varied teaching; each course sets its own outcomes" }
  - { component: "3.3", kind: "teaching", gloss: "face-to-face, distance, hybrid and blended teaching" }
  - { component: "3.4", kind: "teaching", gloss: "lectures, seminars, case studies, projects and workplace learning" }
  - { component: "3.5", kind: "teaching", gloss: "engagement with the profession: visits, guest lectures, work experience" }
  - { component: "3.6", kind: "learning", gloss: "independent learning and self-development" }
  - { component: "3.7", kind: "learning", gloss: "research training towards a research project" }
  - { component: "3.8", kind: "learning", gloss: "continuing professional development and lifelong learning" }
  - { component: "1.6", kind: "assessment", gloss: "clear assessment policies; formative and summative assessment" }
  - { component: "1.17", kind: "assessment", gloss: "authentic tasks: reports, policy, projects, reflective practice" }
  - { component: "3.9", kind: "assessment", gloss: "varied, inclusive and accessible assessment" }
  - { component: "3.10", kind: "assessment", gloss: "authentic assignments and the six kinds assessment will include" }
  - { component: "3.11", kind: "assessment", gloss: "tutor and peer feedback; giving and receiving feedback" }
```

### SB4 Benchmark standards
<!-- label: both; status: drafted; basis: primary -->
```yaml
rungs:
  - { rung: "threshold", leadIn: "4.5", award: "bachelor's with honours", items: 44 }
  - { rung: "threshold", leadIn: "4.11", award: "master's (with postgraduate certificate and diploma)", items: 43 }
  - { rung: "typical", leadIn: "none", award: "bachelor's with honours", items: 0 }
rungBases: "Threshold only, stated twice: honours (4.5, 4.6, 4.7, 4.8; 4.6 defines the third class as some proficiency in most attributes) and postgraduate (4.9, 4.10, 4.11, 4.12; 4.11 repeats the definition at master's). 1.1 says typical standards are set out and 4.1 that the threshold, shown over time, shows typical achievement, but no typical or excellent list is given; classes above the threshold are left to Annex D (4.2). Rung counts: honours 44 (4.5.s1, 4.5.s2, 4.5.b1 to b3, 4.6, 4.7.b1 to b21, 4.8.b1 to b17); postgraduate 43 (4.9.b1 to b4, 4.10.s1, 4.10.s2, 4.11.s1, 4.11.b1 to b25, 4.12.b1 to b4 and b6 to b12)."
outcomeLists:
  - { leadIn: "3.10", gloss: "what assessment will include", items: 6, award: ["honours", "postgraduate"] }
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
- { body: "Chartered Institute of Library and Information Professionals (CILIP)", says: "its diversity and inclusion principles, Green Libraries Manifesto, Ethical Framework, AI Hub and Professional Knowledge and Skills Base are named; it accredits courses, with professional registration and Chartership as later recognition (D1, 1.10; 1.14; 1.18; 1.21; 2.1; 2.8; 2.15)", requirements: "not yet ingested (Part E)" }
- { body: "Archives and Records Association (ARA)", says: "its diversity principles, Environmental Sustainability Group, Code of Ethics, Professional Development Programme and Competency Framework are named; it accredits courses and offers professional registration (D1, 1.10; 1.14; 2.1; 2.8; 2.15)", requirements: "not yet ingested (Part E)" }
- { body: "International Federation of Library Associations and Institutions (IFLA)", says: "its Environment, Sustainability and Libraries Section shows sustainability as a professional concern (D1, 1.14)", requirements: "not-applicable-by-design: named as evidence of a concern, not for requirements" }
- { body: "The Information and Records Management Society (IRMS)", says: "its accreditation programme is one route to vocational recognition (D1, 2.8)", requirements: "not yet ingested (Part E)" }
- { body: "Equality and Human Rights Commission", says: "providers setting competence standards should follow its latest guidance (D1, 4.4)", requirements: "not-applicable-by-design: guidance, not course requirements" }
- { body: "professional, statutory and regulatory bodies (PSRBs), unnamed", says: "courses with professional outcomes may need their accreditation, usually through site visits and desk review every few years; competence standards may draw on their requirements (D1, 2.20; 4.4)", requirements: "not-applicable-by-design: generic reference" }
```

### SB6 Cross-cutting references
<!-- label: both; status: drafted; basis: primary -->
```yaml
themes:
  - { id: "theme:edi", named: "Equality, diversity and inclusion (the front matter says \"equity, diversity, and inclusion\")", carriedIn: ["1.3", "1.4", "1.7", "1.8", "1.9", "1.10", "2.2"], statements: ["4.7.b1", "4.7.b2", "4.7.b3", "4.7.b4", "4.7.b5", "4.11.b2", "4.11.b3", "4.11.b4", "4.11.b5"] }
  - { id: "theme:accessibility", named: "Accessibility and the needs of disabled students", carriedIn: ["1.3", "1.4", "1.11", "2.9", "3.9"], statements: ["4.7.b2", "4.7.b3", "4.7.b11", "4.7.b12", "4.11.b3", "4.11.b11", "4.11.b12"] }
  - { id: "theme:esd", named: "Education for sustainable development", carriedIn: ["1.3", "1.4", "1.12", "1.13", "1.14", "1.20"], statements: ["4.8.b17"] }
  - { id: "theme:enterprise", named: "Employability, enterprise and entrepreneurship education", carriedIn: ["1.3", "1.15", "1.16", "1.17", "1.18", "1.19", "3.10"], statements: ["4.11.b18", "4.11.b19", "3.10.b3"] }
  - { id: "theme:generative-ai", named: "Generative artificial intelligence", carriedIn: ["1.3", "1.20", "1.21", "3.10"], statements: ["4.7.b18", "4.11.b20", "3.10.b5"] }
frameworks:
  - { framework: "fheq", levels: ["fheq:4", "fheq:5", "fheq:6", "fheq:7"], citedIn: ["2.4", "2.7", "4.2"] }
  - { framework: "scqf", levels: ["fqheis:8", "fqheis:9", "fqheis:10", "fqheis:11"], citedIn: ["2.4", "2.7"] }
bodies:
  - { body: "CILIP", citedIn: ["1.10", "1.14", "1.18", "1.21", "2.1", "2.8", "2.15"] }
  - { body: "Archives and Records Association (ARA)", citedIn: ["1.10", "1.14", "2.1", "2.8", "2.15"] }
  - { body: "IFLA", citedIn: ["1.14"] }
  - { body: "Information and Records Management Society (IRMS)", citedIn: ["2.8"] }
  - { body: "Equality and Human Rights Commission", citedIn: ["4.4"] }
  - { body: "PSRBs (unnamed)", citedIn: ["2.20", "4.4"] }
sharedDocuments:
  - { document: "std:doc:qaa-fheq-2024-framework, Annex D", named: "Annex D of the Frameworks for Higher Education Qualifications of UK Degree-Awarding Bodies", citedIn: ["4.2"], role: "how classes above the threshold are described" }
  - { document: "not yet ingested: listed in Part E", named: "QAA guidance on the creation of inclusive subject learning communities", citedIn: ["1.11"], role: "a reference for inclusive course development" }
  - { document: "this statement (as a Subject Benchmark Statement)", named: "Subject Benchmark Statements", citedIn: ["2.16", "2.19"], role: "an external reference point for review and for external examiners" }
```

## Part B Terminology
<!-- The statement has no glossary of its own unless Part E says so; these are terms it defines in its text. -->

### B1 Concepts
<!-- label: both; status: drafted; basis: primary -->
```yaml
- { slug: "formative-and-summative-assessment", definition: "assessment given as feedback on progress, set against assessment mainly for credit, progression and classification (D1, 1.6)", beneficiaryDefinition: "tasks that help you improve, and tasks that count towards your marks", scopeNote: "departments explain the relation between the two (1.6)", category: "unknown", practices: ["education"] }
- { slug: "information-architecture", definition: "the framework and standards within which information products, services and systems are made, analysed and judged for their users (D1, 1.8)", beneficiaryDefinition: "how information and systems are organised so people can use them", scopeNote: "set within effective information provision (1.8)", category: "unknown", practices: ["information-management"] }
- { slug: "monitoring-and-evaluation", definition: "periodic assessment of a course, internal or external, using current and past monitoring data (D1, 2.16)", beneficiaryDefinition: "how your course is checked and improved over time", scopeNote: "with the student voice central (2.17)", category: "unknown", practices: ["education"] }
- { slug: "threshold-standard", definition: "the standard a student will have shown when awarded the degree; at honours a third, with some proficiency in most attributes (D1, 4.1; 4.6; 4.11)", beneficiaryDefinition: "the minimum you need to show for your award", scopeNote: "not a competence standard (4.4)", category: "unknown", practices: ["education"] }
```

### B2a Terms as the issuer defines them
<!-- label: source; status: drafted; basis: primary -->
```yaml
- { concept: "formative-and-summative-assessment", form: "formative and summative assessment", lang: "en", partOfSpeech: "noun-phrase", termStatus: "preferred", register: "formal" }
- { concept: "information-architecture", form: "information architecture", lang: "en", partOfSpeech: "noun-phrase", termStatus: "preferred", register: "discipline-specific" }
- { concept: "monitoring-and-evaluation", form: "monitoring and evaluation", lang: "en", partOfSpeech: "noun-phrase", termStatus: "preferred", register: "formal" }
- { concept: "threshold-standard", form: "threshold level of attainment", lang: "en", partOfSpeech: "noun-phrase", termStatus: "preferred", register: "formal" }
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
  title: "Subject Benchmark Statement: Librarianship, Information, Knowledge, Records and Archives Management"
  edition: "Fifth edition, April 2025"
  year: 2025
  url: unknown (the QAA page; the text came by stan's extraction)
  retrieved: "held from stan: wkspc2615-QAAVector mapped/librarianship-information-knowledge-records-and-archives-management-2025/librarianship-information-knowledge-records-and-archives-management-2025.raw.txt, commit 366bcb99a01118f2c4c3ebfa2a8337596bddc455; received 2026-10-03"
  licence: QAA copyright
  tier: primary
  readVia: direct
  held: 9fa2e745227bc8ee1d311cdf78b47df194361d9f4ccd0f2876f383aebe7ac875
  heldFiles: ["wkspc2601-library/txt/qaa-2025-librarianship-information-knowledge-records-archives-management-standard.txt", "wkspc2601-library/txt/qaa-2025-librarianship-information-knowledge-records-archives-management-standard.norm.txt", "wkspc2601-library/records/qaa-2025-librarianship-information-knowledge-records-archives-management-standard.chunks.json", "wkspc2601-library/records/qaa-2025-librarianship-information-knowledge-records-archives-management-standard.held.json"]
  citedIn: [S1, S2, S3, S4, S4a, S5, S6, S7, SB1, SB2, SB3, SB4, SB5, SB6]
```

### D2 Research log
```yaml
- { ref: D1, tier: primary, consulted: 2026-10-03, pass: P1, outcome: "read whole, direct, from the normalised text; skeleton by tools/std_prep.py, document by tools/bm_build.py" }
- { ref: "ADAPT subj HESA stores, cah.json and hecos.json (designs/ingest/standards/subj/vocab)", tier: primary, consulted: 2026-10-03, pass: P1, outcome: "codes for statedSubjects and subjects" }
```

### D3 Wanted sources
```yaml
- { w: "W-std-0075", citation: "CILIP, The Professional Knowledge and Skills Base", settles: ["SB5", "S7"], asked: "2026-10-03", state: "wanted" }
- { w: "W-std-0076", citation: "CILIP's Ethical Framework", settles: ["SB5", "S7"], asked: "2026-10-03", state: "wanted" }
- { w: "W-std-0077", citation: "Archives and Records Association, Professional Registration Programme: Competency Framework", settles: ["SB5", "S7"], asked: "2026-10-03", state: "wanted" }
- { w: "W-std-0066", citation: "QAA, Creating Inclusive Subject Communities", settles: ["SB6", "S7"], asked: "2026-10-03", state: "wanted" }
```

## Part E Gaps and questions
- S4, rungs: one rung only, the threshold, stated for two awards (honours 4.5 to 4.8; postgraduate 4.9 to 4.12). 1.1 says the statement sets out "threshold and typical standards" but no typical list exists; SB4 records typical with no lead-in and 0 items. No excellent rung. Unlike Psychology.
- S4, master's: a separate master's section (4.9 to 4.12) covering postgraduate certificates, diplomas and master's degrees, with its own paragraph numbers, so no `.masters` id suffix was needed; level fheq:7 is inferred from the awards, not stated in section 4 (2.4 names FHEQ 7 only for the integrated master's).
- S4, threshold reading: 4.6 and 4.11 define threshold as "some degree of proficiency in the majority of the attributes", so no single list item is a pass condition; every aad says so. For Abbott: whether list items should carry force `threshold` instead of the lead-in modal.
- S4, force: the honours lists take "should be able to" (4.5, 4.7, 4.8); the master's subject list takes "will have demonstrated" from 4.11's first sentence (forceFrom 4.11), while its lead-in also says the attributes "may be understood as some or all of the ability to"; 4.12 takes "should".
- S4, force: 4.9's lead-in has no modal ("the standard of achievement expected of all students"); its four items are recorded with force `describes`. For Abbott: does "expected" read as `should`?
- S4, 4.10.s3 ("students may also be asked to demonstrate" strategic thinking, leadership and original research) is recorded as an expectation with force `may`, rung none: an option, not a threshold item.
- S4, cuts: 2.3, 4.5, 4.10 and 4.11 are cut into sentence records (.s1, .s2, .s3) where a stem or paragraph carries its own obligation; 4.12.b5 ("a conceptual understanding that enables them to:") is a stem, not a record, and its two sub-items are 4.12.b6 and 4.12.b7 (skeleton ids kept).
- S4, skeleton correction: 4.7.b21 and 4.11.b25 ran on into the next sub-heading ("Generic skills"); both are recut with `find` to end at the item.
- S4, not taken: 1.3's 26 bullets ("degrees ... are likely to address the following areas") are content areas, recorded in S3 and SB3, though 4.7 and 4.11 repeat most of them nearly word for word as outcomes.
- S4, not taken (plain-present provider norms, template open point 5): 1.4's eight characteristics ("typically include"), 1.5, 1.6 ("departments ... develop clear assessment policies"), 1.11 (accessible courses), 1.21, 3.5 to 3.8, 4.3 ("Published criteria and grade descriptors are available").
- S4, not taken (obliging words outside the five, or descriptive "will"): 2.4 ("it is expected that each level would see ..."), 2.5 ("it would be expected that a student ... would be capable of" postgraduate study), 2.8, 2.14, 2.15 ("encouraged"), 2.19 (external examiners "will be asked", introduced by "Typically"), 1.9 (practitioners "are able to"), 1.19 ("Graduates are reflective, proactive and positive"). For Abbott at P3.
- S4, 2.7 ("may exit earlier and be eligible for" a CertHE or DipHE) is a permission, not taken as a statement; its level citations are recorded in S5 and SB6.
- S4, 3.10: the six assessment items are recorded as expectations (force will, from "These will include assessments which:") with addressee both, since the student meets them as tasks; for Abbott whether they are provider duties (student version not applicable).
- S5, crosswalk conflict: 2.7 places the CertHE at "FHEQ Level 4; FQHEIS Level 8" and the DipHE at "FHEQ Level 5; FQHEIS Level 9"; FHEQ Table 1 (std:doc:qaa-fheq-2024-framework, S5) places them at fqheis:7 and fqheis:8. Recorded as stated; for P3.
- SB4, cross-award pairs (not gradeOf: a different award, not a rung): 18 honours items in 4.7 recur in 4.11 almost unchanged (4.7.b3 to b5 and b7 to b21 with 4.11.b3 to b5, b6, b7, b9 to b17 and b20 to b23); each aaw sets the pair beside each other. 4.11 adds disaster preparedness (b8), experimentation (b18), entrepreneurship (b19) and strategic leadership (b24, b25), all drawn from 1.3.
- S4, 4.12: its items restate the FHEQ's master's descriptor closely (4.12.b1 with qaa/fheq-2024/4.17.b2; b2 and b3 with 4.17.b3; b6 and b7 with 4.17.b4; b8 with 4.17.b5; b9 with 4.17.b6). Recorded as the benchmark's own statements; each aaw points to the FHEQ item.
- S4, verbs: 4.12.b2, b9 and b10 are noun phrases with no verb of their own (their lead-in verb "demonstrate" is outside the span); verbs left empty.
- Subjects: no HESA code is stated. 100913 librarianship and 100915 archives and records management are recorded as stated because the title names them; 100370 information management, 100916 information services and CAH24-01-01 are inferred. Knowledge management has no HECoS code of its own. For P3.
- Title: the issuer writes "Archives Management" in the title and sections 1 and 3 but "Archive Management" in sections 2 and 4 and the advisory group lists; 2.13 also says "Library, Information ...". Recorded as given; the document title follows the cover.
- SB6: the front matter calls the first theme "equity, diversity, and inclusion"; the section heading says "Equality, diversity and inclusion". One theme id, theme:edi.
- SB6, not recorded as bodies: the UN Sustainable Development Goals (1.12; carried under theme:esd and S7), the Lifelong Learning Entitlement (2.10) and the Equality Act 2010 (4.4: legislation, not a body). The QAA Quality Code and Glossary are named only in the excluded front matter; QAA Enterprise and Entrepreneurship Education only in the references list.
- SB6, sharedDocuments: QAA guidance on inclusive subject learning communities (1.11) is not yet ingested (D3).
- Pattern: section 4's honours threshold lead-in (4.5) is followed by a separate paragraph (4.6) defining the third class, and the subject list (4.7) repeats 1.3's content areas as outcomes; Psychology had no such duplication.
- Frameworks consulted: std:doc:qaa-fheq-2024-framework (S5, SL1 to SL7, 4.15, 4.17, Annex D), std:doc:qaa-fqheis-2024-framework (S5), std:doc:welsh-government-cqfw-2009-framework (S5; not cited by the statement) and std:ref:uk-framework (R2, R3, R8). The framework ids in each aaw are our readings (inferred).
- ST-12: versions here run to the lengths the content needs; no length range is yet set.

---

## Change notes
- 0.1.2, 3 October 2026, 21:02: moved with its held text from UNI to the source library repo (`wkspc2601-library/ingested/standards/`, texts in `txt/`, records in `records/`); paths only (Abbott, 20:56; std N-0119).
- 0.1.1, 3 October 2026, 20:20: obliging words outside the five read as must, "ought to" as should, on statements outside the rungs, each marked on its force line (Abbott, 20:17; D-std-0016).
- 0.1.0, 2026-10-03 17:45: researched by run frame 0.1.1-draft and standards run layer 0.7.0-draft, std, run 0117 (P1); built by tools/bm_build.py.
