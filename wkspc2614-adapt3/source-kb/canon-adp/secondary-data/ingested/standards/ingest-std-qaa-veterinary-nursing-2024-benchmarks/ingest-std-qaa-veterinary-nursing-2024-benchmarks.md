---
id: std:doc:qaa-veterinary-nursing-2024-benchmarks
title: "Subject Benchmark Statement Veterinary Nursing"
profile: standards/subject-benchmark
profileVersion: 0.2.0-draft
issuer: QAA
kind: subject-benchmark
jurisdiction: [UK]
subjectScope: subjects
subjects:
  - { scheme: "hecos", code: "100532", label: "veterinary nursing", basis: "stated" }
  - { scheme: "cah", code: "CAH05-01-02", label: "others in veterinary sciences", basis: "inferred" }
edition: "April 2024 (third edition)"
published: 2024-04
status: current
supersedes: "the second edition, 2019 (D1, section 6); first edition 2015"
heldText: { method: sha256-bytes, raw: 429fe4f71226a5bc708925e16ffe80c35e0c704c40f197712c3b05e70842aa71, normalised: 1c5d4baddba62e505e8fad2e35027395d5f9ea28aa69061e289b0acec85991eb }
heldTextStan: { method: sha256-stan, raw: 429fe4f71226a5bc708925e16ffe80c35e0c704c40f197712c3b05e70842aa71, normalised: e75e5ba6363622542b5953f6d402e8ef4f0008876b8ef156c05c53e98c76350f }
licence: "QAA copyright; held for study, private to the project, never published"
series: "QAA Subject Benchmark Statements, 2024 revision (third edition for this subject)"
awardsCovered: ["foundation degree", "bachelor's with honours", "master's"]
levelsCovered: ["fheq:5", "fheq:6", "fheq:7", "fqheis:10", "fqheis:11"]
nations: ["England", "Wales", "Scotland", "Northern Ireland"]
parts:
  S: full
  B: "partial: no glossary in the document (it points to QAA's Glossary); terms it defines in passing"
  C: "not-applicable: the document sets expectations, not a procedure"
pins: { structure: 0.13.0-draft, template: 0.8.0-draft, benchmarkTemplate: 0.6.0-draft, runFrame: 0.1.1-draft, runLayer: 0.7.0-draft, standards: none yet, terminology: none yet }
lifecycle: drafted
researchedBy: run frame 0.1.1-draft; standards run layer 0.7.0-draft; std, run 0134 (tools/bm_build.py)
passes:
  P1: "2026-10-03 18:44"
  P2: "skipped: read direct from the held text; inferred codes and rung links are for P3"
  P3: open
version: 0.1.2
---

<!-- from INGEST wpk-0016-ingest-pd-template-standards.md 0.8.0-draft and wpk-0016-ingest-pd-template-standards-benchmark.md 0.6.0-draft; built by tools/bm_build.py from run-src/ -->
# Subject Benchmark Statement: Veterinary Nursing (QAA, April 2024)

> Run 0134, P1 by std. The issuer's words are held in the source library, `wkspc2601-library/txt/qaa-2024-veterinary-nursing-subject-benchmark-statement-standard.norm.txt`; each S4 record carries its statement in full (`source`) for language analysis, with its span. Paraphrases and versions are ours. Private to the project, never published. In front matter `status` is the issuer's; ours is `lifecycle`. Doubts are in Part E.

## Part 0 Summary

### 0.1 Agent definition
<!-- label: editorial; status: drafted; basis: primary -->
This document records what the 2024 Veterinary Nursing statement expects of graduates at three awards: a foundation degree (FHEQ level 5), a bachelor's degree with honours (FHEQ level 6, SCQF level 10) and a master's degree (FHEQ level 7, SCQF level 11). Its standards are all threshold standards, set out in four tables with one column per award, beside the duties on course design that sections 1 to 3 place on providers. An agent should use the statement ids here when it writes or talks about a veterinary nursing course, keep each award's column to that award, and read the RCVS requirements as separate documents.

### 0.2 Summary
<!-- label: both; status: drafted; basis: primary -->
A science-based, strongly vocational subject whose courses should prepare graduates to register as veterinary nurses with the RCVS on graduating. The statement sets threshold standards only (no typical or excellent rungs), for three awards side by side in four tables: generic skills; principles and concepts in application; subject knowledge, understanding and skills; and working as a professional veterinary nurse. Sections 1 to 3 add course duties on the RCVS Day One Competences, Skills and Professional Behaviours, placements, partnership, assessment and minimum content. Themes: equality, diversity and inclusion; accessibility; sustainability; enterprise and entrepreneurship education. Bodies: the RCVS (PSRB) and the Office for Students. Annex D of the FHEQ is cited for honours classification.

## Part S Standard

### S1 Identity
<!-- label: source; status: drafted; basis: primary -->
```yaml
issuer: The Quality Assurance Agency for Higher Education
title: "Subject Benchmark Statement Veterinary Nursing"
edition: "April 2024 (third edition)"
dates:
  published: 2024-04
  other: []
kind: subject-benchmark
jurisdiction: [UK]
authority: "reference: a sector reference point, not a regulatory requirement; a key reference point in Wales and Scotland and part of quality requirements in Northern Ireland, not a sector-recognised standard in England (D1, front matter)"
licence: "QAA copyright; the document gives no re-use terms in its text (D1, front matter)"
copyrightNotice: { text: "© The Quality Assurance Agency for Higher Education 2024", locator: "D1, index" }
```

### S2 Purpose and scope
<!-- label: source; status: drafted; basis: primary -->
```yaml
governs: "what a Veterinary Nursing graduate can be expected to know, do and understand at the end of a foundation degree, a bachelor's degree with honours or a master's degree, and the nature of awards in the subject (D1, front matter; 1.6; 1.9; 4.1)"
appliesTo:
  awards: ["foundation degree", "bachelor's degree with honours", "master's degree"]
  levels: ["fheq:5", "fheq:6", "fheq:7", "fqheis:10", "fqheis:11"]
  providers: ["UK higher education providers"]
whoMustUse: "none-stated; it is a reference point, not a requirement (D1, front matter)"
howUsed: ["design", "approval", "review", "other: external examining; PSRBs; information for prospective students and employers"]
doesNot: "it does not prescribe teaching, learning or assessment, does not interpret legislation and carries no statutory or regulatory requirement (D1, front matter)"
beneficiary: the student
statedScope: "\"The purpose of this Subject Benchmark Statement is to make explicit the nature and the academic standards of degrees in Veterinary Nursing.\" (D1, 1.6)"
statedSubjects:
  - { name: "Veterinary Nursing", locator: "(D1, 1.6)", kind: "subject", codes: [{ scheme: "hecos", code: "100532", label: "veterinary nursing" }] }
  - { name: "small animal Veterinary Nursing", locator: "(D1, 3.3)", kind: "specialism", codes: [{ scheme: "hecos", code: "100532", label: "veterinary nursing" }] }
  - { name: "equine Veterinary Nursing", locator: "(D1, 3.4)", kind: "specialism", codes: [{ scheme: "hecos", code: "100532", label: "veterinary nursing" }] }
subjects: see front matter (subjectScope subjects)
```

### S3 Structure
<!-- label: both; status: drafted; basis: primary -->
```yaml
components:
  - { number: "1.1", order: 3, componentType: paragraph, parent: "section 1", heading: "Context", gloss: "what veterinary nurses do and where they work" }
  - { number: "1.2", order: 4, componentType: paragraph, parent: "section 1", heading: "Context", gloss: "the aims of veterinary nursing: health, welfare, comfort" }
  - { number: "1.3", order: 5, componentType: stem, parent: "section 1", heading: "Context", gloss: "the scope of a registered veterinary nurse's role" }
  - { number: "1.4", order: 6, componentType: paragraph, parent: "section 1", heading: "Context", gloss: "RCVS registration, code and accountability" }
  - { number: "1.5", order: 7, componentType: stem, parent: "section 1", heading: "Context", gloss: "the five principles in the code of conduct" }
  - { number: "1.6", order: 8, componentType: paragraph, parent: "section 1", heading: "Purposes and characteristics of a Veterinary Nursing degree", gloss: "purpose of the statement; a vocational science degree leading to registration" }
  - { number: "1.7", order: 9, componentType: paragraph, parent: "section 1", heading: "Purposes and characteristics of a Veterinary Nursing degree", gloss: "licence to practise courses and the Day One requirements" }
  - { number: "1.8", order: 10, componentType: paragraph, parent: "section 1", heading: "Purposes and characteristics of a Veterinary Nursing degree", gloss: "what the statement describes and which awards it covers" }
  - { number: "1.9", order: 11, componentType: paragraph, parent: "section 1", heading: "Purposes and characteristics of a Veterinary Nursing degree", gloss: "awards and framework levels covered" }
  - { number: "1.10", order: 12, componentType: paragraph, parent: "section 1", heading: "Purposes and characteristics of a Veterinary Nursing degree", gloss: "room for variety in course design" }
  - { number: "1.11", order: 13, componentType: paragraph, parent: "section 1", heading: "Equality, diversity and inclusion", gloss: "the statement's stance on equity and diversity" }
  - { number: "1.12", order: 14, componentType: paragraph, parent: "section 1", heading: "Equality, diversity and inclusion", gloss: "inclusive learning and placement environments" }
  - { number: "1.13", order: 15, componentType: paragraph, parent: "section 1", heading: "Equality, diversity and inclusion", gloss: "programmes that build personal responsibility for inclusion" }
  - { number: "1.14", order: 16, componentType: stem, parent: "section 1", heading: "Accessibility", gloss: "accessibility across the whole course, with examples" }
  - { number: "1.15", order: 17, componentType: paragraph, parent: "section 1", heading: "Accessibility", gloss: "flexible, inclusive design that avoids barriers" }
  - { number: "1.16", order: 18, componentType: paragraph, parent: "section 1", heading: "Accessibility", gloss: "equal workplace learning and inclusive digital access" }
  - { number: "1.17", order: 19, componentType: paragraph, parent: "section 1", heading: "Sustainability", gloss: "the profession and sustainable development; ethics, responsibility and sustainability" }
  - { number: "1.18", order: 20, componentType: paragraph, parent: "section 1", heading: "Sustainability", gloss: "climate action and sustainable management in the curriculum" }
  - { number: "1.19", order: 21, componentType: stem, parent: "section 1", heading: "Sustainability", gloss: "example sustainability topics for courses" }
  - { number: "1.20", order: 22, componentType: paragraph, parent: "section 1", heading: "Enterprise and entrepreneurship education", gloss: "what enterprise education offers students" }
  - { number: "1.21", order: 23, componentType: paragraph, parent: "section 1", heading: "Enterprise and entrepreneurship education", gloss: "entrepreneurial competencies beyond employment" }
  - { number: "1.22", order: 24, componentType: paragraph, parent: "section 1", heading: "Enterprise and entrepreneurship education", gloss: "designing enterprise education with employers and others" }
  - { number: "2.1", order: 26, componentType: stem, parent: "section 2", heading: "Design", gloss: "minimum subject areas a course should include" }
  - { number: "2.2", order: 27, componentType: paragraph, parent: "section 2", heading: "Design", gloss: "meeting the Day One requirements as a condition of accreditation" }
  - { number: "2.3", order: 28, componentType: paragraph, parent: "section 2", heading: "Design", gloss: "how the focus differs by award" }
  - { number: "2.4", order: 29, componentType: paragraph, parent: "section 2", heading: "Design", gloss: "extensive practical teaching across the Day One skills" }
  - { number: "2.5", order: 30, componentType: paragraph, parent: "section 2", heading: "Design", gloss: "clinical placement time in approved training practices" }
  - { number: "2.6", order: 31, componentType: paragraph, parent: "section 2", heading: "Progression", gloss: "progression through the levels and on to postgraduate study" }
  - { number: "2.7", order: 32, componentType: paragraph, parent: "section 2", heading: "Flexibility", gloss: "modes, formats and credit" }
  - { number: "2.8", order: 33, componentType: paragraph, parent: "section 2", heading: "Partnership", gloss: "partnership with the RCVS on accreditation" }
  - { number: "2.9", order: 34, componentType: paragraph, parent: "section 2", heading: "Partnership", gloss: "partnerships with further education colleges and their oversight" }
  - { number: "2.10", order: 35, componentType: paragraph, parent: "section 2", heading: "Partnership", gloss: "students as partners; the student voice" }
  - { number: "2.11", order: 36, componentType: paragraph, parent: "section 2", heading: "Partnership", gloss: "partnership with placement providers; written agreements" }
  - { number: "2.12", order: 37, componentType: paragraph, parent: "section 2", heading: "Partnership", gloss: "approving training practices and training clinical supervisors" }
  - { number: "2.13", order: 38, componentType: paragraph, parent: "section 2", heading: "Monitoring and review", gloss: "monitoring, evaluation and periodic review" }
  - { number: "2.14", order: 39, componentType: paragraph, parent: "section 2", heading: "Monitoring and review", gloss: "external reviewers in periodic review" }
  - { number: "2.15", order: 40, componentType: paragraph, parent: "section 2", heading: "Monitoring and review", gloss: "the role of external examiners" }
  - { number: "3.1", order: 42, componentType: area, parent: "section 3", heading: "Content", gloss: "areas of knowledge across species" }
  - { number: "3.2", order: 43, componentType: area, parent: "section 3", heading: "Research and evidence-based practice", gloss: "research and evidence-based practice activities" }
  - { number: "3.3", order: 44, componentType: stem, parent: "section 3", heading: "Research and evidence-based practice", gloss: "species for small animal nursing degrees" }
  - { number: "3.4", order: 45, componentType: paragraph, parent: "section 3", heading: "Research and evidence-based practice", gloss: "equine nursing degrees" }
  - { number: "3.5", order: 46, componentType: area, parent: "section 3", heading: "Research and evidence-based practice", gloss: "farm animal husbandry in some curricula" }
  - { number: "3.6", order: 47, componentType: paragraph, parent: "section 3", heading: "Research and evidence-based practice", gloss: "the range of skills students build" }
  - { number: "3.7", order: 48, componentType: area, parent: "section 3", heading: "Clinical and technical skills", gloss: "clinical and technical skills developed" }
  - { number: "3.8", order: 49, componentType: practice, parent: "section 3", heading: "Clinical and technical skills", gloss: "skills learned in class and on placement" }
  - { number: "3.9", order: 50, componentType: area, parent: "section 3", heading: "Personal and professional skills and behaviours", gloss: "ethics, culture, law and professional duties in course design" }
  - { number: "3.10", order: 51, componentType: stem, parent: "section 3", heading: "Personal and professional skills and behaviours", gloss: "personal and professional abilities to develop" }
  - { number: "3.11", order: 52, componentType: practice, parent: "section 3", heading: "Teaching and learning", gloss: "teaching and assessment set locally with the RCVS" }
  - { number: "3.12", order: 53, componentType: practice, parent: "section 3", heading: "Teaching and learning", gloss: "reflective, critical, student-centred learning" }
  - { number: "3.13", order: 54, componentType: paragraph, parent: "section 3", heading: "Teaching and learning", gloss: "skills teaching should build; the research project" }
  - { number: "3.14", order: 55, componentType: paragraph, parent: "section 3", heading: "Assessment", gloss: "aligned assessment that separates threshold from higher achievement" }
  - { number: "3.15", order: 56, componentType: paragraph, parent: "section 3", heading: "Assessment", gloss: "progressive, varied, authentic and inclusive assessment" }
  - { number: "3.16", order: 57, componentType: practice, parent: "section 3", heading: "Assessment", gloss: "formative and summative assessment" }
  - { number: "3.17", order: 58, componentType: practice, parent: "section 3", heading: "Assessment", gloss: "assessing competence and fitness to practise; clinical placement" }
  - { number: "3.18", order: 59, componentType: paragraph, parent: "section 3", heading: "Assessment", gloss: "emphasis at postgraduate level on applied evidence and research skills" }
  - { number: "4.1", order: 61, componentType: paragraph, parent: "section 4", heading: "Introduction", gloss: "threshold standards for the three awards" }
  - { number: "4.2", order: 62, componentType: paragraph, parent: "section 4", heading: "Introduction", gloss: "performance above threshold; Annex D; then the four standards tables" }
  - { number: "1", componentType: section, parent: none, heading: "Context and purposes of a Veterinary Nursing degree", gloss: "section 1" }
  - { number: "2", componentType: section, parent: none, heading: "Distinctive features of a Veterinary Nursing degree", gloss: "section 2" }
  - { number: "3", componentType: section, parent: none, heading: "Content, structure and delivery", gloss: "section 3" }
  - { number: "4", componentType: section, parent: none, heading: "Benchmark standards", gloss: "section 4" }
excluded:
  - { number: "none", heading: "Contents; About this Statement; How can I use this document?; Relationship to legislation; Additional sector reference points", kind: "other: front matter, read for S1, S2, SB5 and SB6" }
  - { number: "section headings 1 to 4", heading: "the section heading lines", kind: "other: headings, recorded in SECTIONS" }
  - { number: "5", heading: "List of references and further resources", kind: "other: references, read for SB6 and D3" }
  - { number: "6", heading: "Membership of the Advisory Group", kind: "other: authorship and edition history, read for S8" }
```

### S4 Statements
<!-- label: both; status: drafted; basis: primary. Only standards (D-std-0002 (a)): 177 records. `source` is the issuer's statement exactly as its span holds it (D-std-0014). -->
```yaml
- id: qaa/veterinary-nursing-2024/1.4
  locator: { number: "1.4", headingPath: ["Context and purposes of a Veterinary Nursing degree", "Context"] }
  span: { start: 10859, end: 11435 }
  source: "1.4 The Royal College of Veterinary Surgeons (RCVS) maintains a non-statutory register of veterinary nurses. Veterinary nurses who wish to practise in the UK must be registered as a veterinary nurse with the RCVS. They must agree to adhere to the RCVS Code of Professional Conduct and be accountable for their actions as professionals as well as maintaining their skills and knowledge by undertaking, and reflecting on, regular and relevant continuing professional development. They are accountable for their professional conduct through the mechanism of fitness to practise.\n"
  stem: none
  statementType: requirement
  rung: none
  force: must
  level: none
  appliesTo: "veterinary nurses who wish to practise in the UK"
  addressee: learner
  verbs: ["registered", "agree", "adhere"]
  about: "registration, the code of conduct and accountability"
  themes: [none]
  domain: none
  award: ["none"]
  gradeOf: none
  paraphrase: "Anyone who wants to practise as a veterinary nurse in the UK must be on the RCVS register and must commit to its code of conduct, answering for their actions and keeping their knowledge current through reflective continuing professional development; fitness to practise procedures hold them to account."
  quote: full   # the issuer's statement is in `source` (D-std-0014)
  audience: both
  subjects: inherited
- id: qaa/veterinary-nursing-2024/1.6
  locator: { number: "1.6", headingPath: ["Context and purposes of a Veterinary Nursing degree", "Purposes and characteristics of a Veterinary Nursing degree"] }
  span: { start: 11900, end: 12236 }
  source: "1.6 The purpose of this Subject Benchmark Statement is to make explicit the nature and the academic standards of degrees in Veterinary Nursing. A course in Veterinary Nursing is a science-based degree with a strong vocational focus, which should equip graduates to become a registered veterinary nurse (RVN) at the point of graduation.\n"
  stem: none
  statementType: expectation
  rung: none
  force: should
  level: none
  appliesTo: "Veterinary Nursing courses"
  addressee: provider
  verbs: ["equip"]
  about: "courses that prepare graduates for registration on graduating"
  themes: [none]
  domain: none
  award: ["foundation degree", "bachelor's with honours", "master's"]
  gradeOf: none
  paraphrase: "The statement sets out the nature and academic standards of veterinary nursing degrees: a science-based, strongly vocational course that should prepare graduates to register as veterinary nurses on graduating."
  quote: full   # the issuer's statement is in `source` (D-std-0014)
  audience: practitioner
  subjects: inherited
- id: qaa/veterinary-nursing-2024/1.7
  locator: { number: "1.7", headingPath: ["Context and purposes of a Veterinary Nursing degree", "Purposes and characteristics of a Veterinary Nursing degree"] }
  span: { start: 12236, end: 12672 }
  source: "1.7 A Licence to Practise Veterinary Nursing course accredited by the RCVS should be designed to enable graduates to acquire and evidence the Day One Competences (DOC), Day One Skills List (DOS) and Professional Behaviours and Attributes (PB) for Veterinary Nurses. These are the minimum essential requirements set out by the RCVS that all student veterinary nurses must meet in order to join the RCVS register of veterinary nurses.\n\n4\n"
  stem: none
  statementType: expectation
  rung: none
  force: should
  level: none
  appliesTo: "licence to practise courses accredited by the RCVS"
  addressee: both
  verbs: ["designed", "acquire", "evidence", "meet"]
  about: "the Day One Competences, Skills and Professional Behaviours"
  themes: [none]
  domain: none
  award: ["foundation degree", "bachelor's with honours"]
  gradeOf: none
  paraphrase: "An RCVS-accredited licence to practise course should be built so that graduates can gain and show the Day One Competences, the Day One Skills List and the Professional Behaviours and Attributes, the RCVS minimum that every student veterinary nurse must meet to join its register."
  quote: full   # the issuer's statement is in `source` (D-std-0014)
  audience: both
  subjects: inherited
- id: qaa/veterinary-nursing-2024/1.12
  locator: { number: "1.12", headingPath: ["Context and purposes of a Veterinary Nursing degree", "Equality, diversity and inclusion"] }
  span: { start: 14211, end: 14612 }
  source: "1.12 An inclusive environment for learning, including clinical placement, anticipates and accommodates the varied requirements of students. Courses should be proactively and flexibly designed to ensure equitable access to educational opportunities. Course providers, staff and students all have a role in, and responsibility for, promoting equity and diversity and challenging biases and stereotypes.\n"
  stem: none
  statementType: expectation
  rung: none
  force: should
  level: none
  appliesTo: "course design"
  addressee: provider
  verbs: ["designed", "ensure"]
  about: "equitable access through proactive, flexible design"
  themes: [theme:edi]
  domain: none
  award: ["foundation degree", "bachelor's with honours", "master's"]
  gradeOf: none
  paraphrase: "Learning settings, placements included, should be inclusive; courses should be designed proactively and flexibly for equitable access, and providers, staff and students share responsibility for promoting equity and challenging bias."
  quote: full   # the issuer's statement is in `source` (D-std-0014)
  audience: practitioner
  subjects: inherited
- id: qaa/veterinary-nursing-2024/1.13
  locator: { number: "1.13", headingPath: ["Context and purposes of a Veterinary Nursing degree", "Equality, diversity and inclusion"] }
  span: { start: 14612, end: 15089 }
  source: "1.13 Veterinary nursing programmes should be designed to create an environment that encourages openness and participation, and which fosters an individual’s understanding of their personal responsibility for equity and inclusive practice, both as a student veterinary nurse and as an RVN. This should be considered a professional responsibility when working as part of a professional team and when supporting and educating animal owners or members of the public. Accessibility\n"
  stem: none
  statementType: expectation
  rung: none
  force: should
  level: none
  appliesTo: "veterinary nursing programmes and their students"
  addressee: both
  verbs: ["designed", "considered"]
  about: "personal responsibility for equity and inclusive practice"
  themes: [theme:edi]
  domain: none
  award: ["foundation degree", "bachelor's with honours", "master's"]
  gradeOf: none
  paraphrase: "Programmes should be designed to encourage openness and participation and to build each person's sense of responsibility for equity and inclusive practice, as a student and as a registered nurse; this should be treated as a professional responsibility in teams and with the public."
  quote: full   # the issuer's statement is in `source` (D-std-0014)
  audience: both
  subjects: inherited
- id: qaa/veterinary-nursing-2024/1.14
  locator: { number: "1.14", headingPath: ["Context and purposes of a Veterinary Nursing degree", "Accessibility"] }
  span: { start: 15089, end: 15945 }
  source: "1.14 Accessibility considers whether all aspects of a course, however they are encountered, can be understood by everyone. Accessibility should, as a minimum, meet any regulatory requirements and should apply to all stages of the course, from providing pre-application information through to graduation and beyond. It may include, but is not limited to:\n• taking actions to ensure that all elements of the course curriculum are accessible to all students\n• ensuring that all students have access to appropriate and safe learning spaces and resources that support their learning\n• using a variety of assessments, which can be adjusted to meet the needs of individual students, to ensure that all students have the opportunity to succeed in order to meet the RCVS requirement for DOC/DOS/PB and be eligible to join the RCVS register of veterinary nurses.\n\n5\n"
  stem: none
  statementType: expectation
  rung: none
  force: should
  level: none
  appliesTo: "all stages of the course"
  addressee: provider
  verbs: ["meet", "apply"]
  about: "accessibility from pre-application to graduation"
  themes: [theme:accessibility]
  domain: none
  award: ["foundation degree", "bachelor's with honours", "master's"]
  gradeOf: none
  paraphrase: "Accessibility asks whether everything in a course can be understood by everyone; it should meet any regulatory requirement as a minimum and should run from pre-application information to graduation and beyond, for example through accessible curricula, safe learning spaces and adjustable assessment that lets every student meet the RCVS requirements."
  quote: full   # the issuer's statement is in `source` (D-std-0014)
  audience: practitioner
  subjects: inherited
- id: qaa/veterinary-nursing-2024/1.15
  locator: { number: "1.15", headingPath: ["Context and purposes of a Veterinary Nursing degree", "Accessibility"] }
  span: { start: 15945, end: 16189 }
  source: "1.15 Proactive and innovative approaches should be taken in the design of courses, modules, teaching practices and assessments to build in flexibility and inclusivity and avoid creating barriers for students with specific learning differences.\n"
  stem: none
  statementType: expectation
  rung: none
  force: should
  level: none
  appliesTo: "course, module, teaching and assessment design"
  addressee: provider
  verbs: ["taken", "build", "avoid"]
  about: "flexible, inclusive design for specific learning differences"
  themes: [theme:accessibility]
  domain: none
  award: ["foundation degree", "bachelor's with honours", "master's"]
  gradeOf: none
  paraphrase: "Proactive and innovative approaches should be used in designing courses, modules, teaching and assessment so that flexibility and inclusion are built in and students with specific learning differences meet no needless barriers."
  quote: full   # the issuer's statement is in `source` (D-std-0014)
  audience: practitioner
  subjects: inherited
- id: qaa/veterinary-nursing-2024/1.16
  locator: { number: "1.16", headingPath: ["Context and purposes of a Veterinary Nursing degree", "Accessibility"] }
  span: { start: 16189, end: 16402 }
  source: "1.16 Accessibility should include enabling the same opportunities for workplace learning for all students, as well as providing students with inclusive digital accessibility without discrimination. Sustainability\n"
  stem: none
  statementType: expectation
  rung: none
  force: should
  level: none
  appliesTo: "workplace learning and digital provision"
  addressee: provider
  verbs: ["include", "enabling", "providing"]
  about: "equal workplace learning and inclusive digital access"
  themes: [theme:accessibility]
  domain: none
  award: ["foundation degree", "bachelor's with honours", "master's"]
  gradeOf: none
  paraphrase: "Accessibility should give every student the same chance of workplace learning and inclusive digital access free of discrimination."
  quote: full   # the issuer's statement is in `source` (D-std-0014)
  audience: practitioner
  subjects: inherited
- id: qaa/veterinary-nursing-2024/1.17
  locator: { number: "1.17", headingPath: ["Context and purposes of a Veterinary Nursing degree", "Sustainability"] }
  span: { start: 16402, end: 17081 }
  source: "1.17 The Veterinary Nursing profession can contribute towards responsible and sustainable development as envisaged by the UN Sustainable Development Goals , partly in terms of disciplinary content, and partly via disciplinary method (see QAA and Advance HE’s Education for Sustainable Development Guidance, 2021). Specifically, Veterinary Nursing courses can draw on the UN Principles for Responsible Management Education (PRME) to develop the capabilities of students so that they become future generators of a sustainable veterinary profession. There is an expectation that ethics, responsibility and sustainability (ERS) are integrated into the Veterinary Nursing curriculum.\n"
  stem: none
  statementType: expectation
  rung: none
  force: describes
  level: none
  appliesTo: "the Veterinary Nursing curriculum"
  addressee: provider
  verbs: ["contribute", "draw", "develop", "integrated"]
  about: "ethics, responsibility and sustainability in the curriculum"
  themes: [theme:esd]
  domain: none
  award: ["foundation degree", "bachelor's with honours", "master's"]
  gradeOf: none
  paraphrase: "The profession can support sustainable development as the UN goals frame it, through content and method; courses can use the UN principles for responsible management education, and the statement sets an expectation that ethics, responsibility and sustainability are woven into the curriculum."
  quote: full   # the issuer's statement is in `source` (D-std-0014)
  audience: practitioner
  subjects: inherited
- id: qaa/veterinary-nursing-2024/1.18
  locator: { number: "1.18", headingPath: ["Context and purposes of a Veterinary Nursing degree", "Sustainability"] }
  span: { start: 17081, end: 17772 }
  source: "1.18 Sustainable management is required for planetary survival, and organisations, including higher education providers and veterinary practices, will play a key role in meeting targets set to halve global emissions by 2030 (IPCC, 2022). Veterinary nurses should be equipped to engage meaningfully with climate challenges and embed climate solutions in veterinary functions and processes. The principles of sustainable management extend to the wider issue of sustainable development articulated by the UN Sustainable Development Goals. Consequently, management for the purpose of economic, social and environmental sustainability should be integrated into the Veterinary Nursing curriculum.\n"
  stem: none
  statementType: expectation
  rung: none
  force: should
  level: none
  appliesTo: "veterinary nurses and the curriculum"
  addressee: both
  verbs: ["equipped", "engage", "embed", "integrated"]
  about: "climate action and sustainable management"
  themes: [theme:esd]
  domain: none
  award: ["foundation degree", "bachelor's with honours", "master's"]
  gradeOf: none
  paraphrase: "Sustainable management is needed for the planet, and organisations including practices will help meet emission targets; veterinary nurses should be equipped to act on climate challenges in their work, and sustainability management should be built into the curriculum."
  quote: full   # the issuer's statement is in `source` (D-std-0014)
  audience: both
  subjects: inherited
- id: qaa/veterinary-nursing-2024/1.22
  locator: { number: "1.22", headingPath: ["Context and purposes of a Veterinary Nursing degree", "Enterprise and entrepreneurship education"] }
  span: { start: 19500, end: 20415 }
  source: "1.22 Involving employers in curriculum and assessment design will support graduate employability. Entrepreneurship focuses on competencies and transferable themes, including business awareness, professional ethics, leadership and personal motivation as examples. Entrepreneurship education should be designed in consultation with stakeholders such as employers, professional bodies and service users. A range of important themes can be considered, such as project planning and management, sustainability, innovation and career development, reflection, and personal development. Themes may be considered using veterinary-specific applications and examples. Collaborative student work should be encouraged, promoting team working, negotiation and leadership skills. Students can be encouraged to consider their personal and professional development as well as supporting the development of others, as appropriate.\n\n7\n"
  stem: none
  statementType: expectation
  rung: none
  force: should
  level: none
  appliesTo: "enterprise and entrepreneurship education"
  addressee: provider
  verbs: ["designed", "encouraged"]
  about: "enterprise education designed with stakeholders"
  themes: [theme:enterprise]
  domain: none
  award: ["foundation degree", "bachelor's with honours", "master's"]
  gradeOf: none
  paraphrase: "Employer involvement helps employability; enterprise education should be designed together with employers, professional bodies, service users and other stakeholders, and collaborative student work should be encouraged to build teamwork, negotiation and leadership."
  quote: full   # the issuer's statement is in `source` (D-std-0014)
  audience: practitioner
  subjects: inherited
- id: qaa/veterinary-nursing-2024/2.1.b1
  locator: { number: "2.1.b1", headingPath: ["Distinctive features of a Veterinary Nursing degree", "Design"] }
  span: { start: 20638, end: 20651 }
  source: "communication"
  stem: "2.1"
  statementType: requirement
  rung: none
  force: should
  level: none
  appliesTo: "Veterinary Nursing courses"
  addressee: provider
  verbs: []
  about: "minimum content: communication"
  themes: [none]
  domain: knowledge
  award: ["foundation degree", "bachelor's with honours", "master's"]
  gradeOf: none
  paraphrase: "As a minimum, a veterinary nursing course should include the subject area of communication."
  quote: full   # the issuer's statement is in `source` (D-std-0014)
  audience: practitioner
  subjects: inherited
- id: qaa/veterinary-nursing-2024/2.1.b2
  locator: { number: "2.1.b2", headingPath: ["Distinctive features of a Veterinary Nursing degree", "Design"] }
  span: { start: 20654, end: 20671 }
  source: "animal physiology"
  stem: "2.1"
  statementType: requirement
  rung: none
  force: should
  level: none
  appliesTo: "Veterinary Nursing courses"
  addressee: provider
  verbs: []
  about: "minimum content: animal physiology"
  themes: [none]
  domain: knowledge
  award: ["foundation degree", "bachelor's with honours", "master's"]
  gradeOf: none
  paraphrase: "As a minimum, a veterinary nursing course should include the subject area of animal physiology."
  quote: full   # the issuer's statement is in `source` (D-std-0014)
  audience: practitioner
  subjects: inherited
- id: qaa/veterinary-nursing-2024/2.1.b3
  locator: { number: "2.1.b3", headingPath: ["Distinctive features of a Veterinary Nursing degree", "Design"] }
  span: { start: 20674, end: 20683 }
  source: "husbandry"
  stem: "2.1"
  statementType: requirement
  rung: none
  force: should
  level: none
  appliesTo: "Veterinary Nursing courses"
  addressee: provider
  verbs: []
  about: "minimum content: husbandry"
  themes: [none]
  domain: knowledge
  award: ["foundation degree", "bachelor's with honours", "master's"]
  gradeOf: none
  paraphrase: "As a minimum, a veterinary nursing course should include the subject area of husbandry."
  quote: full   # the issuer's statement is in `source` (D-std-0014)
  audience: practitioner
  subjects: inherited
- id: qaa/veterinary-nursing-2024/2.1.b4
  locator: { number: "2.1.b4", headingPath: ["Distinctive features of a Veterinary Nursing degree", "Design"] }
  span: { start: 20686, end: 20707 }
  source: "welfare and behaviour"
  stem: "2.1"
  statementType: requirement
  rung: none
  force: should
  level: none
  appliesTo: "Veterinary Nursing courses"
  addressee: provider
  verbs: []
  about: "minimum content: welfare and behaviour"
  themes: [none]
  domain: knowledge
  award: ["foundation degree", "bachelor's with honours", "master's"]
  gradeOf: none
  paraphrase: "As a minimum, a veterinary nursing course should include the subject area of welfare and behaviour."
  quote: full   # the issuer's statement is in `source` (D-std-0014)
  audience: practitioner
  subjects: inherited
- id: qaa/veterinary-nursing-2024/2.1.b5
  locator: { number: "2.1.b5", headingPath: ["Distinctive features of a Veterinary Nursing degree", "Design"] }
  span: { start: 20710, end: 20727 }
  source: "infection control"
  stem: "2.1"
  statementType: requirement
  rung: none
  force: should
  level: none
  appliesTo: "Veterinary Nursing courses"
  addressee: provider
  verbs: []
  about: "minimum content: infection control"
  themes: [none]
  domain: knowledge
  award: ["foundation degree", "bachelor's with honours", "master's"]
  gradeOf: none
  paraphrase: "As a minimum, a veterinary nursing course should include the subject area of infection control."
  quote: full   # the issuer's statement is in `source` (D-std-0014)
  audience: practitioner
  subjects: inherited
- id: qaa/veterinary-nursing-2024/2.1.b6
  locator: { number: "2.1.b6", headingPath: ["Distinctive features of a Veterinary Nursing degree", "Design"] }
  span: { start: 20730, end: 20741 }
  source: "anaesthesia"
  stem: "2.1"
  statementType: requirement
  rung: none
  force: should
  level: none
  appliesTo: "Veterinary Nursing courses"
  addressee: provider
  verbs: []
  about: "minimum content: anaesthesia"
  themes: [none]
  domain: knowledge
  award: ["foundation degree", "bachelor's with honours", "master's"]
  gradeOf: none
  paraphrase: "As a minimum, a veterinary nursing course should include the subject area of anaesthesia."
  quote: full   # the issuer's statement is in `source` (D-std-0014)
  audience: practitioner
  subjects: inherited
- id: qaa/veterinary-nursing-2024/2.1.b7
  locator: { number: "2.1.b7", headingPath: ["Distinctive features of a Veterinary Nursing degree", "Design"] }
  span: { start: 20744, end: 20781 }
  source: "surgical nursing and theatre practice"
  stem: "2.1"
  statementType: requirement
  rung: none
  force: should
  level: none
  appliesTo: "Veterinary Nursing courses"
  addressee: provider
  verbs: []
  about: "minimum content: surgical nursing and theatre practice"
  themes: [none]
  domain: knowledge
  award: ["foundation degree", "bachelor's with honours", "master's"]
  gradeOf: none
  paraphrase: "As a minimum, a veterinary nursing course should include the subject area of surgical nursing and theatre practice."
  quote: full   # the issuer's statement is in `source` (D-std-0014)
  audience: practitioner
  subjects: inherited
- id: qaa/veterinary-nursing-2024/2.1.b8
  locator: { number: "2.1.b8", headingPath: ["Distinctive features of a Veterinary Nursing degree", "Design"] }
  span: { start: 20784, end: 20796 }
  source: "pharmacology"
  stem: "2.1"
  statementType: requirement
  rung: none
  force: should
  level: none
  appliesTo: "Veterinary Nursing courses"
  addressee: provider
  verbs: []
  about: "minimum content: pharmacology"
  themes: [none]
  domain: knowledge
  award: ["foundation degree", "bachelor's with honours", "master's"]
  gradeOf: none
  paraphrase: "As a minimum, a veterinary nursing course should include the subject area of pharmacology."
  quote: full   # the issuer's statement is in `source` (D-std-0014)
  audience: practitioner
  subjects: inherited
- id: qaa/veterinary-nursing-2024/2.1.b9
  locator: { number: "2.1.b9", headingPath: ["Distinctive features of a Veterinary Nursing degree", "Design"] }
  span: { start: 20799, end: 20835 }
  source: "laboratory and diagnostic techniques"
  stem: "2.1"
  statementType: requirement
  rung: none
  force: should
  level: none
  appliesTo: "Veterinary Nursing courses"
  addressee: provider
  verbs: []
  about: "minimum content: laboratory and diagnostic techniques"
  themes: [none]
  domain: knowledge
  award: ["foundation degree", "bachelor's with honours", "master's"]
  gradeOf: none
  paraphrase: "As a minimum, a veterinary nursing course should include the subject area of laboratory and diagnostic techniques."
  quote: full   # the issuer's statement is in `source` (D-std-0014)
  audience: practitioner
  subjects: inherited
- id: qaa/veterinary-nursing-2024/2.1.b10
  locator: { number: "2.1.b10", headingPath: ["Distinctive features of a Veterinary Nursing degree", "Design"] }
  span: { start: 20838, end: 20844 }
  source: "ethics"
  stem: "2.1"
  statementType: requirement
  rung: none
  force: should
  level: none
  appliesTo: "Veterinary Nursing courses"
  addressee: provider
  verbs: []
  about: "minimum content: ethics"
  themes: [none]
  domain: knowledge
  award: ["foundation degree", "bachelor's with honours", "master's"]
  gradeOf: none
  paraphrase: "As a minimum, a veterinary nursing course should include the subject area of ethics."
  quote: full   # the issuer's statement is in `source` (D-std-0014)
  audience: practitioner
  subjects: inherited
- id: qaa/veterinary-nursing-2024/2.1.b11
  locator: { number: "2.1.b11", headingPath: ["Distinctive features of a Veterinary Nursing degree", "Design"] }
  span: { start: 20847, end: 20885 }
  source: "principles of evidence-based practice."
  stem: "2.1"
  statementType: requirement
  rung: none
  force: should
  level: none
  appliesTo: "Veterinary Nursing courses"
  addressee: provider
  verbs: []
  about: "minimum content: principles of evidence-based practice"
  themes: [none]
  domain: knowledge
  award: ["foundation degree", "bachelor's with honours", "master's"]
  gradeOf: none
  paraphrase: "As a minimum, a veterinary nursing course should include the subject area of principles of evidence-based practice."
  quote: full   # the issuer's statement is in `source` (D-std-0014)
  audience: practitioner
  subjects: inherited
- id: qaa/veterinary-nursing-2024/2.2
  locator: { number: "2.2", headingPath: ["Distinctive features of a Veterinary Nursing degree", "Design"] }
  span: { start: 20886, end: 21200 }
  source: "2.2 The delivery and assessment of these subject areas affords graduates the opportunity to meet the requirements of the RCVS DOC/DOS/PB. This is a requirement for a Veterinary Nursing course to gain RCVS accreditation (Licence to Practise) and allow graduates to apply to join the RCVS Veterinary Nurse register.\n"
  stem: none
  statementType: requirement
  rung: none
  force: must
  level: none
  appliesTo: "courses seeking RCVS accreditation"
  addressee: provider
  verbs: ["affords", "meet"]
  about: "meeting the Day One requirements as a condition of accreditation"
  themes: [none]
  domain: none
  award: ["foundation degree", "bachelor's with honours"]
  gradeOf: none
  paraphrase: "Teaching and assessing these subject areas lets graduates meet the RCVS Day One requirements, which a course is required to do to gain RCVS accreditation as a licence to practise and let its graduates apply to the register."
  quote: full   # the issuer's statement is in `source` (D-std-0014)
  audience: practitioner
  subjects: inherited
- id: qaa/veterinary-nursing-2024/2.3
  locator: { number: "2.3", headingPath: ["Distinctive features of a Veterinary Nursing degree", "Design"] }
  span: { start: 21200, end: 21626 }
  source: "2.3 Foundation degree level courses will mainly focus on the subject content that supports the learning and assessment of the RCVS DOC/DOS/PB. Honours degree courses will incorporate additional subjects that recognise the wide-ranging clinical role of an RVN and/or the running and operation of a veterinary practice as a commercial business. Master’s level courses should build further on these areas of specialism or focus.\n"
  stem: none
  statementType: expectation
  rung: none
  force: will
  level: none
  appliesTo: "courses at each award"
  addressee: provider
  verbs: ["focus", "incorporate", "build"]
  about: "the focus of content at each award"
  themes: [none]
  domain: none
  award: ["foundation degree", "bachelor's with honours", "master's"]
  gradeOf: none
  paraphrase: "Foundation degree courses will concentrate on content that supports the Day One requirements; honours courses will add subjects reflecting the wider clinical role and running a practice as a business; master's courses should build further on these specialisms."
  quote: full   # the issuer's statement is in `source` (D-std-0014)
  audience: practitioner
  subjects: inherited
- id: qaa/veterinary-nursing-2024/2.4
  locator: { number: "2.4", headingPath: ["Distinctive features of a Veterinary Nursing degree", "Design"] }
  span: { start: 21626, end: 21777 }
  source: "2.4 Due to the vocational nature of a Veterinary Nursing degree, all courses will require extensive practical teaching to cover the full range of DOS.\n"
  stem: none
  statementType: expectation
  rung: none
  force: will
  level: none
  appliesTo: "all Veterinary Nursing courses"
  addressee: provider
  verbs: ["require", "cover"]
  about: "extensive practical teaching across the Day One skills"
  themes: [none]
  domain: none
  award: ["foundation degree", "bachelor's with honours", "master's"]
  gradeOf: none
  paraphrase: "Because the subject is vocational, every course will need extensive practical teaching that covers all the Day One skills."
  quote: full   # the issuer's statement is in `source` (D-std-0014)
  audience: practitioner
  subjects: inherited
- id: qaa/veterinary-nursing-2024/2.5
  locator: { number: "2.5", headingPath: ["Distinctive features of a Veterinary Nursing degree", "Design"] }
  span: { start: 21777, end: 22244 }
  source: "2.5 Sufficient clinical placement time in an approved training practice (TP) must be built into the design of any Licence to Practise course to ensure that students can complete the number of hours of pre-registration practice required by the RCVS prior to graduation. Time spent in clinical placements allows for practice and refinement of the DOC/DOS/PB which will help ensure that graduates are ready for the role of an RVN at the point of graduation. Progression\n"
  stem: none
  statementType: requirement
  rung: none
  force: must
  level: none
  appliesTo: "licence to practise courses"
  addressee: provider
  verbs: ["built", "complete"]
  about: "clinical placement hours in approved training practices"
  themes: [none]
  domain: none
  award: ["foundation degree", "bachelor's with honours"]
  gradeOf: none
  paraphrase: "Enough placement time in an approved training practice must be built into any licence to practise course for students to complete the RCVS pre-registration hours before graduating; that time lets them practise and refine the Day One requirements so they will be ready for the role."
  quote: full   # the issuer's statement is in `source` (D-std-0014)
  audience: practitioner
  subjects: inherited
- id: qaa/veterinary-nursing-2024/2.6
  locator: { number: "2.6", headingPath: ["Distinctive features of a Veterinary Nursing degree", "Progression"] }
  span: { start: 22244, end: 23641 }
  source: "2.6 Over the course of a foundation degree (FHEQ Level 5) or a bachelor’s degree with honours (FHEQ Level 6; FQHEIS Level 10) a Veterinary Nursing student will progress from one level of study to the next, in line with the regulations and processes for each institution. However, it is expected that each level would see the attainment of knowledge, expertise and experience that builds towards the final achievement of meeting the threshold-level subject-specific and generic skills listed in this Statement. This will usually include successful completion and the award of credit for the full range of learning and assessment, including any practical components. Upon graduation from an undergraduate degree, it would be expected that a student who had achieved a second-class degree or higher would be capable of, and equipped for, undertaking postgraduate study in Veterinary Nursing or a related discipline. Entry requirements to postgraduate courses are, however, determined by individual providers and may require specified levels of achievement at undergraduate level. Upon graduation, postgraduate students will be expected to contribute to the advancement\n\n8\nof the profession through innovation, within legal and professional boundaries. Holders of a master’s degree in Veterinary Nursing will develop the knowledge base and demonstrate excellence in research and practice. Flexibility\n"
  stem: none
  statementType: outcome
  rung: none
  force: will
  level: fheq:7
  appliesTo: "holders of a master's degree in Veterinary Nursing"
  addressee: learner
  verbs: ["progress", "contribute", "develop", "demonstrate"]
  about: "progression and the master's contribution to the profession"
  themes: [none]
  domain: subject-skill
  award: ["master's"]
  gradeOf: none
  paraphrase: "Students progress level by level towards the threshold standards; a second-class honours graduate would be expected to be ready for postgraduate study; postgraduate students will be expected to advance the profession through innovation, and master's holders will build the knowledge base and show excellence in research and practice."
  quote: full   # the issuer's statement is in `source` (D-std-0014)
  audience: both
  subjects: inherited
- id: qaa/veterinary-nursing-2024/2.8
  locator: { number: "2.8", headingPath: ["Distinctive features of a Veterinary Nursing degree", "Partnership"] }
  span: { start: 24166, end: 24402 }
  source: "2.8 Higher education providers should work in partnership with the RCVS to ensure that accreditation and quality assurance requirements are met, thereby enabling completing students to be eligible to register as RVN or Cert AVN Nurses.\n"
  stem: none
  statementType: expectation
  rung: none
  force: should
  level: none
  appliesTo: "higher education providers"
  addressee: provider
  verbs: ["work", "ensure"]
  about: "partnership with the RCVS on accreditation"
  themes: [none]
  domain: none
  award: ["foundation degree", "bachelor's with honours", "master's"]
  gradeOf: none
  paraphrase: "Providers should work with the RCVS so that accreditation and quality requirements are met and completing students can register as veterinary nurses or with the advanced certificate."
  quote: full   # the issuer's statement is in `source` (D-std-0014)
  audience: practitioner
  subjects: inherited
- id: qaa/veterinary-nursing-2024/2.9
  locator: { number: "2.9", headingPath: ["Distinctive features of a Veterinary Nursing degree", "Partnership"] }
  span: { start: 24402, end: 24734 }
  source: "2.9 Providers may operate in partnership with further education colleges, enabling students to study at various geographical locations and improving course accessibility. Providers are expected to develop processes for oversight to ensure that partners involved in degree delivery meet all the academic and RCVS standards required.\n"
  stem: none
  statementType: expectation
  rung: none
  force: must   # D-std-0016: "are expected to" read as must
  level: none
  appliesTo: "providers working with further education colleges"
  addressee: provider
  verbs: ["operate", "develop", "ensure"]
  about: "oversight of partner colleges"
  themes: [none]
  domain: none
  award: ["foundation degree", "bachelor's with honours", "master's"]
  gradeOf: none
  paraphrase: "Providers may partner with further education colleges, widening access; they are expected to set up oversight so that partners meet all academic and RCVS standards."
  quote: full   # the issuer's statement is in `source` (D-std-0014)
  audience: practitioner
  subjects: inherited
- id: qaa/veterinary-nursing-2024/2.10
  locator: { number: "2.10", headingPath: ["Distinctive features of a Veterinary Nursing degree", "Partnership"] }
  span: { start: 24734, end: 24967 }
  source: "2.10 Students should also work in partnership with their provider and in particular their own course teams. The student voice should play a significant role in course development, delivery, review and the overall student experience.\n"
  stem: none
  statementType: expectation
  rung: none
  force: should
  level: none
  appliesTo: "students and their course teams"
  addressee: both
  verbs: ["work", "play"]
  about: "students as partners; the student voice"
  themes: [none]
  domain: none
  award: ["foundation degree", "bachelor's with honours", "master's"]
  gradeOf: none
  paraphrase: "Students should work in partnership with their provider and course team, and their voice should count for much in course development, delivery, review and experience."
  quote: full   # the issuer's statement is in `source` (D-std-0014)
  audience: both
  subjects: inherited
- id: qaa/veterinary-nursing-2024/2.11
  locator: { number: "2.11", headingPath: ["Distinctive features of a Veterinary Nursing degree", "Partnership"] }
  span: { start: 24967, end: 25358 }
  source: "2.11 All course providers work in partnership with clinical placement providers to allow the required access to clinical cases and the veterinary practice environment. This is necessary to complete the DOC/DOS/PB and the required hours in clinical placement. There should be a collaborative written agreement between clinical supervisors, course providers, placement providers and students.\n"
  stem: none
  statementType: expectation
  rung: none
  force: should
  level: none
  appliesTo: "course providers, placement providers, supervisors and students"
  addressee: provider
  verbs: ["work", "complete"]
  about: "written placement agreements"
  themes: [none]
  domain: none
  award: ["foundation degree", "bachelor's with honours"]
  gradeOf: none
  paraphrase: "Course providers partner with placement providers for access to clinical cases and practice settings, needed for the Day One requirements and placement hours; there should be a written collaborative agreement among supervisors, course and placement providers and students."
  quote: full   # the issuer's statement is in `source` (D-std-0014)
  audience: practitioner
  subjects: inherited
- id: qaa/veterinary-nursing-2024/2.12
  locator: { number: "2.12", headingPath: ["Distinctive features of a Veterinary Nursing degree", "Partnership"] }
  span: { start: 25358, end: 25668 }
  source: "2.12 Approval and monitoring of training practices and auxiliary training practices should be undertaken by course providers to ensure that clinical learning facilities are, and remain, appropriate. Course providers should ensure the training and standardisation of clinical supervisors. Monitoring and review\n"
  stem: none
  statementType: expectation
  rung: none
  force: should
  level: none
  appliesTo: "course providers"
  addressee: provider
  verbs: ["undertaken", "ensure"]
  about: "approving training practices and training supervisors"
  themes: [none]
  domain: none
  award: ["foundation degree", "bachelor's with honours"]
  gradeOf: none
  paraphrase: "Course providers should approve and monitor training practices and auxiliary training practices so that clinical learning settings are and stay fit for purpose, and should ensure clinical supervisors are trained and standardised."
  quote: full   # the issuer's statement is in `source` (D-std-0014)
  audience: practitioner
  subjects: inherited
- id: qaa/veterinary-nursing-2024/2.14
  locator: { number: "2.14", headingPath: ["Distinctive features of a Veterinary Nursing degree", "Monitoring and review"] }
  span: { start: 26342, end: 26640 }
  source: "2.14 Externality is an essential component of the quality assurance system in the UK. Providers will use external reviewers as part of periodic review to gain an external perspective on any proposed changes and ensure threshold standards are achieved and content is appropriate for the subject.\n\n9\n"
  stem: none
  statementType: expectation
  rung: none
  force: will
  level: none
  appliesTo: "providers in periodic review"
  addressee: provider
  verbs: ["use", "gain", "ensure"]
  about: "external reviewers in periodic review"
  themes: [none]
  domain: none
  award: ["foundation degree", "bachelor's with honours", "master's"]
  gradeOf: none
  paraphrase: "Externality is central to UK quality assurance; providers will use external reviewers in periodic review to gain an outside view of changes and to make sure threshold standards are reached and content suits the subject."
  quote: full   # the issuer's statement is in `source` (D-std-0014)
  audience: practitioner
  subjects: inherited
- id: qaa/veterinary-nursing-2024/3.3
  locator: { number: "3.3", headingPath: ["Content, structure and delivery", "Research and evidence-based practice"] }
  span: { start: 29020, end: 29209 }
  source: "3.3 It is anticipated that holders of degrees in small animal Veterinary Nursing are proficient in delivering nursing care to a range of species, including:\n• cats\n• dogs\n• exotic species.\n"
  stem: none
  statementType: outcome
  rung: none
  force: must   # D-std-0016: "anticipated" read as must
  level: none
  appliesTo: "holders of degrees in small animal Veterinary Nursing"
  addressee: learner
  verbs: ["delivering"]
  about: "nursing cats, dogs and exotic species"
  themes: [none]
  domain: subject-skill
  award: ["foundation degree", "bachelor's with honours"]
  gradeOf: none
  paraphrase: "Holders of small animal veterinary nursing degrees are expected (the issuer says anticipated) to be proficient in nursing a range of species, including cats, dogs and exotics."
  quote: full   # the issuer's statement is in `source` (D-std-0014)
  audience: both
  subjects: inherited
- id: qaa/veterinary-nursing-2024/3.4
  locator: { number: "3.4", headingPath: ["Content, structure and delivery", "Research and evidence-based practice"] }
  span: { start: 29209, end: 29342 }
  source: "3.4 It is also anticipated that holders of degrees in equine Veterinary Nursing are proficient in delivering nursing care to horses.\n"
  stem: none
  statementType: outcome
  rung: none
  force: must   # D-std-0016: "anticipated" read as must
  level: none
  appliesTo: "holders of degrees in equine Veterinary Nursing"
  addressee: learner
  verbs: ["delivering"]
  about: "nursing horses"
  themes: [none]
  domain: subject-skill
  award: ["foundation degree", "bachelor's with honours"]
  gradeOf: none
  paraphrase: "Holders of equine veterinary nursing degrees are expected (anticipated) to be proficient in nursing horses."
  quote: full   # the issuer's statement is in `source` (D-std-0014)
  audience: both
  subjects: inherited
- id: qaa/veterinary-nursing-2024/3.10.b1
  locator: { number: "3.10.b1", headingPath: ["Content, structure and delivery", "Personal and professional skills and behaviours"] }
  span: { start: 30902, end: 31217 }
  source: "work as part of a multidisciplinary team to deliver health care services to patients and clients. This requires excellent communication skills and the ability to maintain a professional relationship with clients, colleagues, the public and external stakeholders even when subject to emotional and economic pressures"
  stem: "3.10"
  statementType: outcome
  rung: none
  force: should
  level: fheq:5
  appliesTo: "students of the subject"
  addressee: learner
  verbs: ["work", "deliver", "maintain"]
  about: "multidisciplinary teamwork and professional relationships"
  themes: [none]
  domain: generic-skill
  award: ["foundation degree", "bachelor's with honours"]
  gradeOf: none
  paraphrase: "Should be able to work in a multidisciplinary team to care for patients and clients, which calls for excellent communication and steady professional relationships with clients, colleagues, the public and others, even under emotional and financial strain."
  quote: full   # the issuer's statement is in `source` (D-std-0014)
  audience: both
  subjects: inherited
- id: qaa/veterinary-nursing-2024/3.10.b2
  locator: { number: "3.10.b2", headingPath: ["Content, structure and delivery", "Personal and professional skills and behaviours"] }
  span: { start: 31220, end: 31436 }
  source: "respond appropriately to situations and circumstances that require the application of an ethical and moral standpoint, recognising the potential risks and, where necessary, utilising knowledge of relevant legislation"
  stem: "3.10"
  statementType: outcome
  rung: none
  force: should
  level: fheq:5
  appliesTo: "students of the subject"
  addressee: learner
  verbs: ["respond", "recognising", "utilising"]
  about: "ethical judgement and legislation"
  themes: [none]
  domain: subject-skill
  award: ["foundation degree", "bachelor's with honours"]
  gradeOf: none
  paraphrase: "Should be able to respond fittingly to situations that call for an ethical and moral stance, seeing the risks and using relevant law where needed."
  quote: full   # the issuer's statement is in `source` (D-std-0014)
  audience: both
  subjects: inherited
- id: qaa/veterinary-nursing-2024/3.10.b3
  locator: { number: "3.10.b3", headingPath: ["Content, structure and delivery", "Personal and professional skills and behaviours"] }
  span: { start: 31439, end: 31533 }
  source: "act as an advocate for patients and clients while always maintaining a confidential standpoint"
  stem: "3.10"
  statementType: outcome
  rung: none
  force: should
  level: fheq:5
  appliesTo: "students of the subject"
  addressee: learner
  verbs: ["act", "maintaining"]
  about: "advocacy with confidentiality"
  themes: [none]
  domain: subject-skill
  award: ["foundation degree", "bachelor's with honours"]
  gradeOf: none
  paraphrase: "Should be able to speak up for patients and clients while always keeping confidentiality."
  quote: full   # the issuer's statement is in `source` (D-std-0014)
  audience: both
  subjects: inherited
- id: qaa/veterinary-nursing-2024/3.10.b4
  locator: { number: "3.10.b4", headingPath: ["Content, structure and delivery", "Personal and professional skills and behaviours"] }
  span: { start: 31536, end: 31642 }
  source: "use research and current data to inform decision-making and take personal responsibility for their actions"
  stem: "3.10"
  statementType: outcome
  rung: none
  force: should
  level: fheq:5
  appliesTo: "students of the subject"
  addressee: learner
  verbs: ["use", "inform", "take"]
  about: "evidence-informed decisions and responsibility"
  themes: [none]
  domain: generic-skill
  award: ["foundation degree", "bachelor's with honours"]
  gradeOf: none
  paraphrase: "Should be able to use research and current data in decisions and take personal responsibility for what they do."
  quote: full   # the issuer's statement is in `source` (D-std-0014)
  audience: both
  subjects: inherited
- id: qaa/veterinary-nursing-2024/3.10.b5
  locator: { number: "3.10.b5", headingPath: ["Content, structure and delivery", "Personal and professional skills and behaviours"] }
  span: { start: 31645, end: 31779 }
  source: "maintain a reflective approach to their professional practice to identify areas for improvement and development. Teaching and learning"
  stem: "3.10"
  statementType: outcome
  rung: none
  force: should
  level: fheq:5
  appliesTo: "students of the subject"
  addressee: learner
  verbs: ["maintain", "identify"]
  about: "reflective practice"
  themes: [none]
  domain: generic-skill
  award: ["foundation degree", "bachelor's with honours"]
  gradeOf: none
  paraphrase: "Should be able to keep reflecting on their professional practice to find what to improve and develop."
  quote: full   # the issuer's statement is in `source` (D-std-0014)
  audience: both
  subjects: inherited
- id: qaa/veterinary-nursing-2024/3.13
  locator: { number: "3.13", headingPath: ["Content, structure and delivery", "Teaching and learning"] }
  span: { start: 32398, end: 32856 }
  source: "3.13 Teaching and learning should enable students to acquire skills in effective communication, information technology, team working, problem-solving and evidence-based practice. Where appropriate, students will have the opportunity to develop skills in research methodology. Typically, courses leading to a bachelor's degree with honours incorporate a short research project or independent study that forms the basis of a dissertation or report. Assessment\n"
  stem: none
  statementType: expectation
  rung: none
  force: should
  level: none
  appliesTo: "teaching and learning"
  addressee: both
  verbs: ["enable", "acquire", "develop"]
  about: "skills teaching and the research project"
  themes: [none]
  domain: none
  award: ["foundation degree", "bachelor's with honours"]
  gradeOf: none
  paraphrase: "Teaching and learning should let students gain skills in communication, information technology, teamwork, problem-solving and evidence-based practice; where fitting, students will have the chance to build research method skills, and honours courses typically include a short research project or dissertation."
  quote: full   # the issuer's statement is in `source` (D-std-0014)
  audience: both
  subjects: inherited
- id: qaa/veterinary-nursing-2024/3.14
  locator: { number: "3.14", headingPath: ["Content, structure and delivery", "Assessment"] }
  span: { start: 32856, end: 33251 }
  source: "3.14 Assessment strategies should ensure alignment between learning outcomes, learning and teaching methods, and competencies, and discriminate between achievement at threshold and higher levels. A variety of assessment styles may be employed to test the wide range of knowledge and skills required by an RVN. Assessment methods should help prepare the student for Day One in clinical practice.\n"
  stem: none
  statementType: expectation
  rung: none
  force: should
  level: none
  appliesTo: "assessment strategies"
  addressee: provider
  verbs: ["ensure", "discriminate", "help"]
  about: "aligned assessment that separates threshold from higher achievement"
  themes: [none]
  domain: none
  award: ["foundation degree", "bachelor's with honours", "master's"]
  gradeOf: none
  paraphrase: "Assessment strategies should align outcomes, teaching and competencies and should tell threshold achievement apart from higher; varied assessment may be used, and methods should prepare students for their first day in practice."
  quote: full   # the issuer's statement is in `source` (D-std-0014)
  audience: practitioner
  subjects: inherited
- id: qaa/veterinary-nursing-2024/3.15
  locator: { number: "3.15", headingPath: ["Content, structure and delivery", "Assessment"] }
  span: { start: 33251, end: 34063 }
  source: "3.15 Assessment should be progressive in terms of level and content and generate effective feedback that enables students to develop their knowledge and skills, including a range of transferable skills that includes critical digital literacy. Course teams should take advantage of these subject-specific and transferable skills and diversify how students are assessed, using a range of methodologies that allow students from all backgrounds and characteristics to demonstrate their learning and development. Where possible, assessments should be authentic, with real-world applications to enhance employability skills and professional development. They should also permit reasonable adjustments to ensure inclusivity while ensuring that students are able to demonstrate competence in all requirements of an RVN.\n"
  stem: none
  statementType: expectation
  rung: none
  force: should
  level: none
  appliesTo: "assessment and course teams"
  addressee: provider
  verbs: ["progressive", "diversify", "permit"]
  about: "progressive, varied, authentic and inclusive assessment"
  themes: [none]
  domain: none
  award: ["foundation degree", "bachelor's with honours", "master's"]
  gradeOf: none
  paraphrase: "Assessment should progress in level and content and give useful feedback, building transferable skills including critical digital literacy; course teams should vary methods so students of every background can show their learning, make assessment authentic where possible, and allow reasonable adjustments while students still show every competence a registered nurse needs."
  quote: full   # the issuer's statement is in `source` (D-std-0014)
  audience: practitioner
  subjects: inherited
- id: qaa/veterinary-nursing-2024/3.18
  locator: { number: "3.18", headingPath: ["Content, structure and delivery", "Assessment"] }
  span: { start: 34645, end: 35002 }
  source: "3.18 At postgraduate level, there should be a strong emphasis on requiring students to apply evidence-based subject-specific knowledge to decision making and solutions to complex and unfamiliar problems. Assessment of a range of research skills is also considered crucial when determining whether a student has met postgraduate-level learning outcomes.\n\n13\n"
  stem: none
  statementType: expectation
  rung: none
  force: should
  level: fheq:7
  appliesTo: "postgraduate courses"
  addressee: provider
  verbs: ["apply", "requiring"]
  about: "applied evidence and research skills at postgraduate level"
  themes: [none]
  domain: none
  award: ["master's"]
  gradeOf: none
  paraphrase: "At postgraduate level there should be strong weight on requiring students to apply evidence-based subject knowledge to decisions and to complex, unfamiliar problems; assessing research skills is held crucial in judging whether postgraduate outcomes are met."
  quote: full   # the issuer's statement is in `source` (D-std-0014)
  audience: practitioner
  subjects: inherited
- id: qaa/veterinary-nursing-2024/4.2
  locator: { number: "4.2", headingPath: ["Benchmark standards", "Introduction"] }
  span: { start: 35452, end: 35988 }
  source: "4.2 The vast majority of students who graduate with a bachelor's degree with honours will perform significantly better than the minimum threshold standards. Each higher education provider has its own method of determining what appropriate evidence of this achievement will be and should refer to Annex D in The Frameworks for Higher Education Qualifications of UK Degree-Awarding Bodies . This Annex sets out common descriptions of the four main degree outcome classifications for bachelor's degrees with honours: 1st, 2.1, 2.2 and 3rd."
  stem: none
  statementType: expectation
  rung: none
  force: should
  level: fheq:6
  appliesTo: "higher education providers"
  addressee: provider
  verbs: ["refer"]
  about: "judging achievement above threshold with Annex D"
  themes: [none]
  domain: none
  award: ["bachelor's with honours"]
  gradeOf: none
  paraphrase: "Most honours graduates will do much better than the threshold; each provider decides how to evidence this and should refer to Annex D of the qualifications frameworks, which describes the four honours classifications."
  quote: full   # the issuer's statement is in `source` (D-std-0014)
  audience: practitioner
  subjects: inherited
- id: qaa/veterinary-nursing-2024/4.2.b1
  locator: { number: "4.2.b1", headingPath: ["Benchmark standards", "Introduction"] }
  span: { start: 36244, end: 36408 }
  source: "Articulate opinions and formulate arguments effectively both verbally and in writing to provide compelling debate with other professionals as the patient’s advocate"
  stem: "4.2"
  statementType: threshold
  rung: threshold
  force: threshold
  level: fheq:6
  appliesTo: "honours degree graduates (section 4 table: Generic skills)"
  addressee: learner
  verbs: ["articulate", "formulate", "provide"]
  about: "arguing a case for the patient (honours degree)"
  themes: [none]
  domain: generic-skill
  award: ["bachelor's with honours"]
  gradeOf: none
  paraphrase: "Graduates of a honours degree should be able to put forward views and build arguments in speech and writing strong enough to carry a debate with other professionals on the patient's behalf, as the minimum for the award."
  quote: full   # the issuer's statement is in `source` (D-std-0014)
  audience: both
  subjects: inherited
- id: qaa/veterinary-nursing-2024/4.2.b1.foundation
  locator: { number: "4.2.b1.foundation", headingPath: ["Benchmark standards", "Introduction"] }
  span: { start: 36159, end: 36243 }
  source: "Articulate opinions and formulate arguments effectively both verbally and in writing"
  stem: "4.2"
  statementType: threshold
  rung: threshold
  force: threshold
  level: fheq:5
  appliesTo: "foundation degree graduates (section 4 table: Generic skills)"
  addressee: learner
  verbs: ["articulate", "formulate"]
  about: "arguing a case for the patient (foundation degree)"
  themes: [none]
  domain: generic-skill
  award: ["foundation degree"]
  gradeOf: none
  paraphrase: "Graduates of a foundation degree should be able to put forward views and build sound arguments, in speech and on paper, as the minimum for the award."
  quote: full   # the issuer's statement is in `source` (D-std-0014)
  audience: both
  subjects: inherited
- id: qaa/veterinary-nursing-2024/4.2.b1.masters
  locator: { number: "4.2.b1.masters", headingPath: ["Benchmark standards", "Introduction"] }
  span: { start: 36409, end: 36507 }
  source: "Debate effectively both verbally and in writing as the patient’s advocate with other professionals"
  stem: "4.2"
  statementType: threshold
  rung: threshold
  force: threshold
  level: fheq:7
  appliesTo: "master's degree graduates (section 4 table: Generic skills)"
  addressee: learner
  verbs: ["debate"]
  about: "arguing a case for the patient (master's degree)"
  themes: [none]
  domain: generic-skill
  award: ["master's"]
  gradeOf: none
  paraphrase: "Graduates of a master's degree should be able to hold their own in spoken and written debate with fellow professionals, speaking up for the patient, as the minimum for the award."
  quote: full   # the issuer's statement is in `source` (D-std-0014)
  audience: both
  subjects: inherited
- id: qaa/veterinary-nursing-2024/4.2.b2
  locator: { number: "4.2.b2", headingPath: ["Benchmark standards", "Introduction"] }
  span: { start: 36564, end: 36641 }
  source: "Learn independently and demonstrate an analytical approach to problem-solving"
  stem: "4.2"
  statementType: threshold
  rung: threshold
  force: threshold
  level: fheq:6
  appliesTo: "honours degree graduates (section 4 table: Generic skills)"
  addressee: learner
  verbs: ["learn", "demonstrate"]
  about: "independent learning and problem-solving (honours degree)"
  themes: [none]
  domain: generic-skill
  award: ["bachelor's with honours"]
  gradeOf: none
  paraphrase: "Graduates of a honours degree should be able to study on their own and show an analytical way of solving problems, as the minimum for the award."
  quote: full   # the issuer's statement is in `source` (D-std-0014)
  audience: both
  subjects: inherited
- id: qaa/veterinary-nursing-2024/4.2.b2.foundation
  locator: { number: "4.2.b2.foundation", headingPath: ["Benchmark standards", "Introduction"] }
  span: { start: 36509, end: 36563 }
  source: "Learn independently and utilise problem-solving skills"
  stem: "4.2"
  statementType: threshold
  rung: threshold
  force: threshold
  level: fheq:5
  appliesTo: "foundation degree graduates (section 4 table: Generic skills)"
  addressee: learner
  verbs: ["learn", "utilise"]
  about: "independent learning and problem-solving (foundation degree)"
  themes: [none]
  domain: generic-skill
  award: ["foundation degree"]
  gradeOf: none
  paraphrase: "Graduates of a foundation degree should be able to study on their own and use problem-solving skills, as the minimum for the award."
  quote: full   # the issuer's statement is in `source` (D-std-0014)
  audience: both
  subjects: inherited
- id: qaa/veterinary-nursing-2024/4.2.b2.masters
  locator: { number: "4.2.b2.masters", headingPath: ["Benchmark standards", "Introduction"] }
  span: { start: 36642, end: 36717 }
  source: "Learn independently and implement an analytical approach to problem-solving"
  stem: "4.2"
  statementType: threshold
  rung: threshold
  force: threshold
  level: fheq:7
  appliesTo: "master's degree graduates (section 4 table: Generic skills)"
  addressee: learner
  verbs: ["learn", "implement"]
  about: "independent learning and problem-solving (master's degree)"
  themes: [none]
  domain: generic-skill
  award: ["master's"]
  gradeOf: none
  paraphrase: "Graduates of a master's degree should be able to study on their own and put an analytical way of solving problems into action, as the minimum for the award."
  quote: full   # the issuer's statement is in `source` (D-std-0014)
  audience: both
  subjects: inherited
- id: qaa/veterinary-nursing-2024/4.2.b3
  locator: { number: "4.2.b3", headingPath: ["Benchmark standards", "Introduction"] }
  span: { start: 36773, end: 36917 }
  source: "Apply the concept of evidence-based practice in the clinical environment. Critically evaluate arguments, assumptions, abstract concepts and data"
  stem: "4.2"
  statementType: threshold
  rung: threshold
  force: threshold
  level: fheq:6
  appliesTo: "honours degree graduates (section 4 table: Generic skills)"
  addressee: learner
  verbs: ["apply", "evaluate"]
  about: "evidence-based practice (honours degree)"
  themes: [none]
  domain: generic-skill
  award: ["bachelor's with honours"]
  gradeOf: none
  paraphrase: "Graduates of a honours degree should be able to use evidence-based practice in the clinic and weigh up arguments, assumptions, abstract ideas and data critically, as the minimum for the award."
  quote: full   # the issuer's statement is in `source` (D-std-0014)
  audience: both
  subjects: inherited
- id: qaa/veterinary-nursing-2024/4.2.b3.foundation
  locator: { number: "4.2.b3.foundation", headingPath: ["Benchmark standards", "Introduction"] }
  span: { start: 36718, end: 36772 }
  source: "Demonstrate the principles of evidence- based practice"
  stem: "4.2"
  statementType: threshold
  rung: threshold
  force: threshold
  level: fheq:5
  appliesTo: "foundation degree graduates (section 4 table: Generic skills)"
  addressee: learner
  verbs: ["demonstrate"]
  about: "evidence-based practice (foundation degree)"
  themes: [none]
  domain: generic-skill
  award: ["foundation degree"]
  gradeOf: none
  paraphrase: "Graduates of a foundation degree should be able to show what evidence-based practice rests on, as the minimum for the award."
  quote: full   # the issuer's statement is in `source` (D-std-0014)
  audience: both
  subjects: inherited
- id: qaa/veterinary-nursing-2024/4.2.b3.masters
  locator: { number: "4.2.b3.masters", headingPath: ["Benchmark standards", "Introduction"] }
  span: { start: 36919, end: 37002 }
  source: "Create and critique evidence to establish best practice in the clinical environment"
  stem: "4.2"
  statementType: threshold
  rung: threshold
  force: threshold
  level: fheq:7
  appliesTo: "master's degree graduates (section 4 table: Generic skills)"
  addressee: learner
  verbs: ["create", "critique"]
  about: "evidence-based practice (master's degree)"
  themes: [none]
  domain: generic-skill
  award: ["master's"]
  gradeOf: none
  paraphrase: "Graduates of a master's degree should be able to generate and critique evidence that sets the best clinical practice, as the minimum for the award."
  quote: full   # the issuer's statement is in `source` (D-std-0014)
  audience: both
  subjects: inherited
- id: qaa/veterinary-nursing-2024/4.2.b4
  locator: { number: "4.2.b4", headingPath: ["Benchmark standards", "Introduction"] }
  span: { start: 37055, end: 37116 }
  source: "Contribute proactively to the aims and organisation of a team"
  stem: "4.2"
  statementType: threshold
  rung: threshold
  force: threshold
  level: fheq:6
  appliesTo: "honours degree graduates (section 4 table: Generic skills)"
  addressee: learner
  verbs: ["contribute"]
  about: "teamwork (honours degree)"
  themes: [none]
  domain: generic-skill
  award: ["bachelor's with honours"]
  gradeOf: none
  paraphrase: "Graduates of a honours degree should be able to take an active part in setting a team's goals and organising it, as the minimum for the award."
  quote: full   # the issuer's statement is in `source` (D-std-0014)
  audience: both
  subjects: inherited
- id: qaa/veterinary-nursing-2024/4.2.b4.foundation
  locator: { number: "4.2.b4.foundation", headingPath: ["Benchmark standards", "Introduction"] }
  span: { start: 37004, end: 37054 }
  source: "Collaborate and contribute to the work of the team"
  stem: "4.2"
  statementType: threshold
  rung: threshold
  force: threshold
  level: fheq:5
  appliesTo: "foundation degree graduates (section 4 table: Generic skills)"
  addressee: learner
  verbs: ["collaborate", "contribute"]
  about: "teamwork (foundation degree)"
  themes: [none]
  domain: generic-skill
  award: ["foundation degree"]
  gradeOf: none
  paraphrase: "Graduates of a foundation degree should be able to work with others and play a part in what the team does, as the minimum for the award."
  quote: full   # the issuer's statement is in `source` (D-std-0014)
  audience: both
  subjects: inherited
- id: qaa/veterinary-nursing-2024/4.2.b4.masters
  locator: { number: "4.2.b4.masters", headingPath: ["Benchmark standards", "Introduction"] }
  span: { start: 37117, end: 37176 }
  source: "Lead the development of the aims and organisation of a team"
  stem: "4.2"
  statementType: threshold
  rung: threshold
  force: threshold
  level: fheq:7
  appliesTo: "master's degree graduates (section 4 table: Generic skills)"
  addressee: learner
  verbs: ["lead"]
  about: "teamwork (master's degree)"
  themes: [none]
  domain: generic-skill
  award: ["master's"]
  gradeOf: none
  paraphrase: "Graduates of a master's degree should be able to lead the shaping of a team's goals and how it is organised, as the minimum for the award."
  quote: full   # the issuer's statement is in `source` (D-std-0014)
  audience: both
  subjects: inherited
- id: qaa/veterinary-nursing-2024/4.2.b5
  locator: { number: "4.2.b5", headingPath: ["Benchmark standards", "Introduction"] }
  span: { start: 37306, end: 37425 }
  source: "Use digital skills to enhance presentations and to facilitate data analysis in line with legal and ethical requirements"
  stem: "4.2"
  statementType: threshold
  rung: threshold
  force: threshold
  level: fheq:6
  appliesTo: "honours degree graduates (section 4 table: Generic skills)"
  addressee: learner
  verbs: ["use"]
  about: "digital skills (honours degree)"
  themes: [none]
  domain: generic-skill
  award: ["bachelor's with honours"]
  gradeOf: none
  paraphrase: "Graduates of a honours degree should be able to use digital tools to strengthen presentations and support data analysis, within legal and ethical limits, as the minimum for the award."
  quote: full   # the issuer's statement is in `source` (D-std-0014)
  audience: both
  subjects: inherited
- id: qaa/veterinary-nursing-2024/4.2.b5.foundation
  locator: { number: "4.2.b5.foundation", headingPath: ["Benchmark standards", "Introduction"] }
  span: { start: 37181, end: 37304 }
  source: "Use digital skills competently and effectively to include information gathering in line with legal and ethical requirements"
  stem: "4.2"
  statementType: threshold
  rung: threshold
  force: threshold
  level: fheq:5
  appliesTo: "foundation degree graduates (section 4 table: Generic skills)"
  addressee: learner
  verbs: ["use"]
  about: "digital skills (foundation degree)"
  themes: [none]
  domain: generic-skill
  award: ["foundation degree"]
  gradeOf: none
  paraphrase: "Graduates of a foundation degree should be able to use digital tools capably, including to find information, within legal and ethical limits, as the minimum for the award."
  quote: full   # the issuer's statement is in `source` (D-std-0014)
  audience: both
  subjects: inherited
- id: qaa/veterinary-nursing-2024/4.2.b5.masters
  locator: { number: "4.2.b5.masters", headingPath: ["Benchmark standards", "Introduction"] }
  span: { start: 37426, end: 37560 }
  source: "Create digitally enhanced presentations and use digital skills to facilitate data analysis in line with legal and ethical requirements"
  stem: "4.2"
  statementType: threshold
  rung: threshold
  force: threshold
  level: fheq:7
  appliesTo: "master's degree graduates (section 4 table: Generic skills)"
  addressee: learner
  verbs: ["create", "use"]
  about: "digital skills (master's degree)"
  themes: [none]
  domain: generic-skill
  award: ["master's"]
  gradeOf: none
  paraphrase: "Graduates of a master's degree should be able to produce digitally enriched presentations and analyse data with digital tools, within legal and ethical limits, as the minimum for the award."
  quote: full   # the issuer's statement is in `source` (D-std-0014)
  audience: both
  subjects: inherited
- id: qaa/veterinary-nursing-2024/4.2.b6
  locator: { number: "4.2.b6", headingPath: ["Benchmark standards", "Introduction"] }
  span: { start: 37638, end: 37756 }
  source: "Demonstrate management of confidential information in line with legal requirements, guiding colleagues where necessary"
  stem: "4.2"
  statementType: threshold
  rung: threshold
  force: threshold
  level: fheq:6
  appliesTo: "honours degree graduates (section 4 table: Generic skills)"
  addressee: learner
  verbs: ["demonstrate"]
  about: "confidential information (honours degree)"
  themes: [none]
  domain: generic-skill
  award: ["bachelor's with honours"]
  gradeOf: none
  paraphrase: "Graduates of a honours degree should be able to handle confidential information as the law requires and guide colleagues when needed, as the minimum for the award."
  quote: full   # the issuer's statement is in `source` (D-std-0014)
  audience: both
  subjects: inherited
- id: qaa/veterinary-nursing-2024/4.2.b6.foundation
  locator: { number: "4.2.b6.foundation", headingPath: ["Benchmark standards", "Introduction"] }
  span: { start: 37561, end: 37636 }
  source: "Demonstrate management of confidential information in an appropriate manner"
  stem: "4.2"
  statementType: threshold
  rung: threshold
  force: threshold
  level: fheq:5
  appliesTo: "foundation degree graduates (section 4 table: Generic skills)"
  addressee: learner
  verbs: ["demonstrate"]
  about: "confidential information (foundation degree)"
  themes: [none]
  domain: generic-skill
  award: ["foundation degree"]
  gradeOf: none
  paraphrase: "Graduates of a foundation degree should be able to handle confidential information properly, as the minimum for the award."
  quote: full   # the issuer's statement is in `source` (D-std-0014)
  audience: both
  subjects: inherited
- id: qaa/veterinary-nursing-2024/4.2.b6.masters
  locator: { number: "4.2.b6.masters", headingPath: ["Benchmark standards", "Introduction"] }
  span: { start: 37757, end: 37869 }
  source: "Manage confidential information in line with legal requirements, supporting colleagues in maintaining this ethos"
  stem: "4.2"
  statementType: threshold
  rung: threshold
  force: threshold
  level: fheq:7
  appliesTo: "master's degree graduates (section 4 table: Generic skills)"
  addressee: learner
  verbs: ["manage"]
  about: "confidential information (master's degree)"
  themes: [none]
  domain: generic-skill
  award: ["master's"]
  gradeOf: none
  paraphrase: "Graduates of a master's degree should be able to manage confidential information as the law requires and help colleagues keep to that standard, as the minimum for the award."
  quote: full   # the issuer's statement is in `source` (D-std-0014)
  audience: both
  subjects: inherited
- id: qaa/veterinary-nursing-2024/4.2.b7
  locator: { number: "4.2.b7", headingPath: ["Benchmark standards", "Introduction"] }
  span: { start: 37947, end: 38022 }
  source: "Demonstrate self-awareness and self- confidence in the clinical environment"
  stem: "4.2"
  statementType: threshold
  rung: threshold
  force: threshold
  level: fheq:6
  appliesTo: "honours degree graduates (section 4 table: Generic skills)"
  addressee: learner
  verbs: ["demonstrate"]
  about: "self-awareness and confidence in the clinic (honours degree)"
  themes: [none]
  domain: generic-skill
  award: ["bachelor's with honours"]
  gradeOf: none
  paraphrase: "Graduates of a honours degree should be able to show self-awareness and self-assurance in clinical settings, as the minimum for the award."
  quote: full   # the issuer's statement is in `source` (D-std-0014)
  audience: both
  subjects: inherited
- id: qaa/veterinary-nursing-2024/4.2.b7.foundation
  locator: { number: "4.2.b7.foundation", headingPath: ["Benchmark standards", "Introduction"] }
  span: { start: 37871, end: 37945 }
  source: "Demonstrate self-awareness and self-confidence in the clinical environment"
  stem: "4.2"
  statementType: threshold
  rung: threshold
  force: threshold
  level: fheq:5
  appliesTo: "foundation degree graduates (section 4 table: Generic skills)"
  addressee: learner
  verbs: ["demonstrate"]
  about: "self-awareness and confidence in the clinic (foundation degree)"
  themes: [none]
  domain: generic-skill
  award: ["foundation degree"]
  gradeOf: none
  paraphrase: "Graduates of a foundation degree should be able to show self-awareness and self-assurance in clinical settings, as the minimum for the award."
  quote: full   # the issuer's statement is in `source` (D-std-0014)
  audience: both
  subjects: inherited
- id: qaa/veterinary-nursing-2024/4.2.b7.masters
  locator: { number: "4.2.b7.masters", headingPath: ["Benchmark standards", "Introduction"] }
  span: { start: 38023, end: 38098 }
  source: "Demonstrate self-awareness and self- confidence in the clinical environment"
  stem: "4.2"
  statementType: threshold
  rung: threshold
  force: threshold
  level: fheq:7
  appliesTo: "master's degree graduates (section 4 table: Generic skills)"
  addressee: learner
  verbs: ["demonstrate"]
  about: "self-awareness and confidence in the clinic (master's degree)"
  themes: [none]
  domain: generic-skill
  award: ["master's"]
  gradeOf: none
  paraphrase: "Graduates of a master's degree should be able to show self-awareness and self-assurance in clinical settings, as the minimum for the award."
  quote: full   # the issuer's statement is in `source` (D-std-0014)
  audience: both
  subjects: inherited
- id: qaa/veterinary-nursing-2024/4.2.b8
  locator: { number: "4.2.b8", headingPath: ["Benchmark standards", "Introduction"] }
  span: { start: 38263, end: 38425 }
  source: "Demonstrate knowledge of, and advocate respect for, diverse cultures, values, views and beliefs. Role model behaviours that underpin anti-discriminatory practices"
  stem: "4.2"
  statementType: threshold
  rung: threshold
  force: threshold
  level: fheq:6
  appliesTo: "honours degree graduates (section 4 table: Generic skills)"
  addressee: learner
  verbs: ["demonstrate", "advocate"]
  about: "respect for diversity and anti-discriminatory behaviour (honours degree)"
  themes: [none]
  domain: generic-skill
  award: ["bachelor's with honours"]
  gradeOf: none
  paraphrase: "Graduates of a honours degree should be able to know about and promote respect for the variety of cultures, values, outlooks and beliefs, and model the behaviours that anti-discriminatory practice depends on, as the minimum for the award."
  quote: full   # the issuer's statement is in `source` (D-std-0014)
  audience: both
  subjects: inherited
- id: qaa/veterinary-nursing-2024/4.2.b8.foundation
  locator: { number: "4.2.b8.foundation", headingPath: ["Benchmark standards", "Introduction"] }
  span: { start: 38099, end: 38261 }
  source: "Demonstrate knowledge of, and advocate respect for, diverse cultures, values, views and beliefs. Role model behaviours that underpin anti-discriminatory practices"
  stem: "4.2"
  statementType: threshold
  rung: threshold
  force: threshold
  level: fheq:5
  appliesTo: "foundation degree graduates (section 4 table: Generic skills)"
  addressee: learner
  verbs: ["demonstrate", "advocate"]
  about: "respect for diversity and anti-discriminatory behaviour (foundation degree)"
  themes: [none]
  domain: generic-skill
  award: ["foundation degree"]
  gradeOf: none
  paraphrase: "Graduates of a foundation degree should be able to know about and promote respect for the variety of cultures, values, outlooks and beliefs, and model the behaviours that anti-discriminatory practice depends on, as the minimum for the award."
  quote: full   # the issuer's statement is in `source` (D-std-0014)
  audience: both
  subjects: inherited
- id: qaa/veterinary-nursing-2024/4.2.b8.masters
  locator: { number: "4.2.b8.masters", headingPath: ["Benchmark standards", "Introduction"] }
  span: { start: 38426, end: 38588 }
  source: "Demonstrate knowledge of, and advocate respect for, diverse cultures, values, views and beliefs. Role model behaviours that underpin anti-discriminatory practices"
  stem: "4.2"
  statementType: threshold
  rung: threshold
  force: threshold
  level: fheq:7
  appliesTo: "master's degree graduates (section 4 table: Generic skills)"
  addressee: learner
  verbs: ["demonstrate", "advocate"]
  about: "respect for diversity and anti-discriminatory behaviour (master's degree)"
  themes: [none]
  domain: generic-skill
  award: ["master's"]
  gradeOf: none
  paraphrase: "Graduates of a master's degree should be able to know about and promote respect for the variety of cultures, values, outlooks and beliefs, and model the behaviours that anti-discriminatory practice depends on, as the minimum for the award."
  quote: full   # the issuer's statement is in `source` (D-std-0014)
  audience: both
  subjects: inherited
- id: qaa/veterinary-nursing-2024/4.2.b9
  locator: { number: "4.2.b9", headingPath: ["Benchmark standards", "Introduction"] }
  span: { start: 38687, end: 38785 }
  source: "Analyse and take action to address any identified barriers to those with protected characteristics"
  stem: "4.2"
  statementType: threshold
  rung: threshold
  force: threshold
  level: fheq:6
  appliesTo: "honours degree graduates (section 4 table: Generic skills)"
  addressee: learner
  verbs: ["analyse", "take", "address"]
  about: "barriers for people with protected characteristics (honours degree)"
  themes: [none]
  domain: generic-skill
  award: ["bachelor's with honours"]
  gradeOf: none
  paraphrase: "Graduates of a honours degree should be able to analyse barriers found for people with protected characteristics and act to remove them, as the minimum for the award."
  quote: full   # the issuer's statement is in `source` (D-std-0014)
  audience: both
  subjects: inherited
- id: qaa/veterinary-nursing-2024/4.2.b9.foundation
  locator: { number: "4.2.b9.foundation", headingPath: ["Benchmark standards", "Introduction"] }
  span: { start: 38590, end: 38686 }
  source: "Recognise barriers for those with protected characteristics and understand how to minimise these"
  stem: "4.2"
  statementType: threshold
  rung: threshold
  force: threshold
  level: fheq:5
  appliesTo: "foundation degree graduates (section 4 table: Generic skills)"
  addressee: learner
  verbs: ["recognise", "understand", "minimise"]
  about: "barriers for people with protected characteristics (foundation degree)"
  themes: [none]
  domain: generic-skill
  award: ["foundation degree"]
  gradeOf: none
  paraphrase: "Graduates of a foundation degree should be able to spot the barriers facing people with protected characteristics and know how to reduce them, as the minimum for the award."
  quote: full   # the issuer's statement is in `source` (D-std-0014)
  audience: both
  subjects: inherited
- id: qaa/veterinary-nursing-2024/4.2.b9.masters
  locator: { number: "4.2.b9.masters", headingPath: ["Benchmark standards", "Introduction"] }
  span: { start: 38786, end: 38886 }
  source: "Evaluate potential barriers to those with protected characteristics and identify appropriate actions"
  stem: "4.2"
  statementType: threshold
  rung: threshold
  force: threshold
  level: fheq:7
  appliesTo: "master's degree graduates (section 4 table: Generic skills)"
  addressee: learner
  verbs: ["evaluate", "identify"]
  about: "barriers for people with protected characteristics (master's degree)"
  themes: [none]
  domain: generic-skill
  award: ["master's"]
  gradeOf: none
  paraphrase: "Graduates of a master's degree should be able to evaluate possible barriers for people with protected characteristics and decide on fitting actions, as the minimum for the award."
  quote: full   # the issuer's statement is in `source` (D-std-0014)
  audience: both
  subjects: inherited
- id: qaa/veterinary-nursing-2024/4.2.b10
  locator: { number: "4.2.b10", headingPath: ["Benchmark standards", "Introduction"] }
  span: { start: 39037, end: 39186 }
  source: "Maintain a non-judgmental position in all aspects of work and avoid stigmatising any category of veterinary client, members of the team or the public"
  stem: "4.2"
  statementType: threshold
  rung: threshold
  force: threshold
  level: fheq:6
  appliesTo: "honours degree graduates (section 4 table: Generic skills)"
  addressee: learner
  verbs: ["maintain", "avoid"]
  about: "non-judgemental practice (honours degree)"
  themes: [none]
  domain: generic-skill
  award: ["bachelor's with honours"]
  gradeOf: none
  paraphrase: "Graduates of a honours degree should be able to stay non-judgemental in all their work and avoid stigmatising any group of clients, team members or the public, as the minimum for the award."
  quote: full   # the issuer's statement is in `source` (D-std-0014)
  audience: both
  subjects: inherited
- id: qaa/veterinary-nursing-2024/4.2.b10.foundation
  locator: { number: "4.2.b10.foundation", headingPath: ["Benchmark standards", "Introduction"] }
  span: { start: 38887, end: 39036 }
  source: "Maintain a non-judgmental position in all aspects of work and avoid stigmatising any category of veterinary client, members of the team or the public"
  stem: "4.2"
  statementType: threshold
  rung: threshold
  force: threshold
  level: fheq:5
  appliesTo: "foundation degree graduates (section 4 table: Generic skills)"
  addressee: learner
  verbs: ["maintain", "avoid"]
  about: "non-judgemental practice (foundation degree)"
  themes: [none]
  domain: generic-skill
  award: ["foundation degree"]
  gradeOf: none
  paraphrase: "Graduates of a foundation degree should be able to stay non-judgemental in all their work and avoid stigmatising any group of clients, team members or the public, as the minimum for the award."
  quote: full   # the issuer's statement is in `source` (D-std-0014)
  audience: both
  subjects: inherited
- id: qaa/veterinary-nursing-2024/4.2.b10.masters
  locator: { number: "4.2.b10.masters", headingPath: ["Benchmark standards", "Introduction"] }
  span: { start: 39187, end: 39336 }
  source: "Maintain a non-judgmental position in all aspects of work and avoid stigmatising any category of veterinary client, members of the team or the public"
  stem: "4.2"
  statementType: threshold
  rung: threshold
  force: threshold
  level: fheq:7
  appliesTo: "master's degree graduates (section 4 table: Generic skills)"
  addressee: learner
  verbs: ["maintain", "avoid"]
  about: "non-judgemental practice (master's degree)"
  themes: [none]
  domain: generic-skill
  award: ["master's"]
  gradeOf: none
  paraphrase: "Graduates of a master's degree should be able to stay non-judgemental in all their work and avoid stigmatising any group of clients, team members or the public, as the minimum for the award."
  quote: full   # the issuer's statement is in `source` (D-std-0014)
  audience: both
  subjects: inherited
- id: qaa/veterinary-nursing-2024/4.2.b11
  locator: { number: "4.2.b11", headingPath: ["Benchmark standards", "Introduction"] }
  span: { start: 39412, end: 39488 }
  source: "Develop a sustainable approach to all aspects of Veterinary Nursing practice"
  stem: "4.2"
  statementType: threshold
  rung: threshold
  force: threshold
  level: fheq:6
  appliesTo: "honours degree graduates (section 4 table: Generic skills)"
  addressee: learner
  verbs: ["develop"]
  about: "sustainable practice (honours degree)"
  themes: [none]
  domain: generic-skill
  award: ["bachelor's with honours"]
  gradeOf: none
  paraphrase: "Graduates of a honours degree should be able to build a sustainable approach across every part of veterinary nursing work, as the minimum for the award."
  quote: full   # the issuer's statement is in `source` (D-std-0014)
  audience: both
  subjects: inherited
- id: qaa/veterinary-nursing-2024/4.2.b11.foundation
  locator: { number: "4.2.b11.foundation", headingPath: ["Benchmark standards", "Introduction"] }
  span: { start: 39337, end: 39411 }
  source: "Adopt a sustainable approach to all aspects of Veterinary Nursing practice"
  stem: "4.2"
  statementType: threshold
  rung: threshold
  force: threshold
  level: fheq:5
  appliesTo: "foundation degree graduates (section 4 table: Generic skills)"
  addressee: learner
  verbs: ["adopt"]
  about: "sustainable practice (foundation degree)"
  themes: [none]
  domain: generic-skill
  award: ["foundation degree"]
  gradeOf: none
  paraphrase: "Graduates of a foundation degree should be able to take a sustainable approach across every part of veterinary nursing work, as the minimum for the award."
  quote: full   # the issuer's statement is in `source` (D-std-0014)
  audience: both
  subjects: inherited
- id: qaa/veterinary-nursing-2024/4.2.b11.masters
  locator: { number: "4.2.b11.masters", headingPath: ["Benchmark standards", "Introduction"] }
  span: { start: 39489, end: 39578 }
  source: "Innovate and develop a sustainable approach to all aspects of Veterinary Nursing practice"
  stem: "4.2"
  statementType: threshold
  rung: threshold
  force: threshold
  level: fheq:7
  appliesTo: "master's degree graduates (section 4 table: Generic skills)"
  addressee: learner
  verbs: ["innovate", "develop"]
  about: "sustainable practice (master's degree)"
  themes: [none]
  domain: generic-skill
  award: ["master's"]
  gradeOf: none
  paraphrase: "Graduates of a master's degree should be able to innovate and build a sustainable approach across every part of veterinary nursing work, as the minimum for the award."
  quote: full   # the issuer's statement is in `source` (D-std-0014)
  audience: both
  subjects: inherited
- id: qaa/veterinary-nursing-2024/4.2.b12
  locator: { number: "4.2.b12", headingPath: ["Benchmark standards", "Introduction"] }
  span: { start: 39731, end: 39919 }
  source: "Adopt a reflective approach to professional practice in both self and others within the team, including improvement of patient care practices and the management of the clinical environment"
  stem: "4.2"
  statementType: threshold
  rung: threshold
  force: threshold
  level: fheq:6
  appliesTo: "honours degree graduates (section 4 table: Generic skills)"
  addressee: learner
  verbs: ["adopt"]
  about: "reflective practice (honours degree)"
  themes: [none]
  domain: generic-skill
  award: ["bachelor's with honours"]
  gradeOf: none
  paraphrase: "Graduates of a honours degree should be able to reflect on professional practice, their own and that of team members, to improve patient care and how the clinical setting is run, as the minimum for the award."
  quote: full   # the issuer's statement is in `source` (D-std-0014)
  audience: both
  subjects: inherited
- id: qaa/veterinary-nursing-2024/4.2.b12.foundation
  locator: { number: "4.2.b12.foundation", headingPath: ["Benchmark standards", "Introduction"] }
  span: { start: 39580, end: 39729 }
  source: "Adopt a reflective approach to professional practice, including the identification of opportunities to improve individual and team- working practices"
  stem: "4.2"
  statementType: threshold
  rung: threshold
  force: threshold
  level: fheq:5
  appliesTo: "foundation degree graduates (section 4 table: Generic skills)"
  addressee: learner
  verbs: ["adopt"]
  about: "reflective practice (foundation degree)"
  themes: [none]
  domain: generic-skill
  award: ["foundation degree"]
  gradeOf: none
  paraphrase: "Graduates of a foundation degree should be able to reflect on professional practice and find chances to improve both individual and team working, as the minimum for the award."
  quote: full   # the issuer's statement is in `source` (D-std-0014)
  audience: both
  subjects: inherited
- id: qaa/veterinary-nursing-2024/4.2.b12.masters
  locator: { number: "4.2.b12.masters", headingPath: ["Benchmark standards", "Introduction"] }
  span: { start: 39920, end: 40107 }
  source: "Lead a reflective approach to professional practice in both self and others within the team, including improvement of patient care practices and the management of the clinical environment"
  stem: "4.2"
  statementType: threshold
  rung: threshold
  force: threshold
  level: fheq:7
  appliesTo: "master's degree graduates (section 4 table: Generic skills)"
  addressee: learner
  verbs: ["lead"]
  about: "reflective practice (master's degree)"
  themes: [none]
  domain: generic-skill
  award: ["master's"]
  gradeOf: none
  paraphrase: "Graduates of a master's degree should be able to lead reflection on professional practice, their own and the team's, to improve patient care and how the clinical setting is run, as the minimum for the award."
  quote: full   # the issuer's statement is in `source` (D-std-0014)
  audience: both
  subjects: inherited
- id: qaa/veterinary-nursing-2024/4.2.b13
  locator: { number: "4.2.b13", headingPath: ["Benchmark standards", "Introduction"] }
  span: { start: 40222, end: 40349 }
  source: "Adopt well-being practices to maintain fitness to practise in self and others, recognising where additional support is required"
  stem: "4.2"
  statementType: threshold
  rung: threshold
  force: threshold
  level: fheq:6
  appliesTo: "honours degree graduates (section 4 table: Generic skills)"
  addressee: learner
  verbs: ["adopt", "recognising"]
  about: "well-being and fitness to practise (honours degree)"
  themes: [none]
  domain: generic-skill
  award: ["bachelor's with honours"]
  gradeOf: none
  paraphrase: "Graduates of a honours degree should be able to use well-being habits to keep themselves and others fit to practise, knowing when more support is needed, as the minimum for the award."
  quote: full   # the issuer's statement is in `source` (D-std-0014)
  audience: both
  subjects: inherited
- id: qaa/veterinary-nursing-2024/4.2.b13.foundation
  locator: { number: "4.2.b13.foundation", headingPath: ["Benchmark standards", "Introduction"] }
  span: { start: 40112, end: 40220 }
  source: "Adopt well-being practices to maintain fitness to practise, recognising where additional support is required"
  stem: "4.2"
  statementType: threshold
  rung: threshold
  force: threshold
  level: fheq:5
  appliesTo: "foundation degree graduates (section 4 table: Generic skills)"
  addressee: learner
  verbs: ["adopt", "recognising"]
  about: "well-being and fitness to practise (foundation degree)"
  themes: [none]
  domain: generic-skill
  award: ["foundation degree"]
  gradeOf: none
  paraphrase: "Graduates of a foundation degree should be able to use well-being habits to stay fit to practise, knowing when to seek more support, as the minimum for the award."
  quote: full   # the issuer's statement is in `source` (D-std-0014)
  audience: both
  subjects: inherited
- id: qaa/veterinary-nursing-2024/4.2.b13.masters
  locator: { number: "4.2.b13.masters", headingPath: ["Benchmark standards", "Introduction"] }
  span: { start: 40351, end: 40478 }
  source: "Adopt well-being practices to maintain fitness to practise in self and others, recognising where additional support is required"
  stem: "4.2"
  statementType: threshold
  rung: threshold
  force: threshold
  level: fheq:7
  appliesTo: "master's degree graduates (section 4 table: Generic skills)"
  addressee: learner
  verbs: ["adopt", "recognising"]
  about: "well-being and fitness to practise (master's degree)"
  themes: [none]
  domain: generic-skill
  award: ["master's"]
  gradeOf: none
  paraphrase: "Graduates of a master's degree should be able to use well-being habits to keep themselves and others fit to practise, knowing when more support is needed, as the minimum for the award."
  quote: full   # the issuer's statement is in `source` (D-std-0014)
  audience: both
  subjects: inherited
- id: qaa/veterinary-nursing-2024/4.2.b14
  locator: { number: "4.2.b14", headingPath: ["Benchmark standards", "Introduction"] }
  span: { start: 40767, end: 40903 }
  source: "Select and apply theories, concepts and principles, evaluating the most appropriate frameworks to deliver holistic veterinary healthcare"
  stem: "4.2"
  statementType: threshold
  rung: threshold
  force: threshold
  level: fheq:6
  appliesTo: "honours degree graduates (section 4 table: Principles and concepts: application)"
  addressee: learner
  verbs: ["select", "apply", "evaluating"]
  about: "theory in holistic care (honours degree)"
  themes: [none]
  domain: subject-skill
  award: ["bachelor's with honours"]
  gradeOf: none
  paraphrase: "Graduates of a honours degree should be able to choose and use theories, concepts and principles, judging which frameworks best support holistic veterinary care, as the minimum for the award."
  quote: full   # the issuer's statement is in `source` (D-std-0014)
  audience: both
  subjects: inherited
- id: qaa/veterinary-nursing-2024/4.2.b14.foundation
  locator: { number: "4.2.b14.foundation", headingPath: ["Benchmark standards", "Introduction"] }
  span: { start: 40673, end: 40765 }
  source: "Select and apply theories, concepts and principles to deliver holistic veterinary healthcare"
  stem: "4.2"
  statementType: threshold
  rung: threshold
  force: threshold
  level: fheq:5
  appliesTo: "foundation degree graduates (section 4 table: Principles and concepts: application)"
  addressee: learner
  verbs: ["select", "apply"]
  about: "theory in holistic care (foundation degree)"
  themes: [none]
  domain: subject-skill
  award: ["foundation degree"]
  gradeOf: none
  paraphrase: "Graduates of a foundation degree should be able to choose and use theories, concepts and principles to give holistic veterinary care, as the minimum for the award."
  quote: full   # the issuer's statement is in `source` (D-std-0014)
  audience: both
  subjects: inherited
- id: qaa/veterinary-nursing-2024/4.2.b14.masters
  locator: { number: "4.2.b14.masters", headingPath: ["Benchmark standards", "Introduction"] }
  span: { start: 40904, end: 41074 }
  source: "Select and apply advanced theories, concepts and principles that incorporate other relevant disciplines in providing holistic care in complex and unpredictable situations"
  stem: "4.2"
  statementType: threshold
  rung: threshold
  force: threshold
  level: fheq:7
  appliesTo: "master's degree graduates (section 4 table: Principles and concepts: application)"
  addressee: learner
  verbs: ["select", "apply", "incorporate"]
  about: "theory in holistic care (master's degree)"
  themes: [none]
  domain: subject-skill
  award: ["master's"]
  gradeOf: none
  paraphrase: "Graduates of a master's degree should be able to choose and use advanced theory, drawing on other relevant disciplines, to give holistic care in complex, unpredictable situations, as the minimum for the award."
  quote: full   # the issuer's statement is in `source` (D-std-0014)
  audience: both
  subjects: inherited
- id: qaa/veterinary-nursing-2024/4.2.b15
  locator: { number: "4.2.b15", headingPath: ["Benchmark standards", "Introduction"] }
  span: { start: 41181, end: 41330 }
  source: "Recognise potential risk, appropriate interventions, and the need to develop protocols to minimise risk while providing quality veterinary healthcare"
  stem: "4.2"
  statementType: threshold
  rung: threshold
  force: threshold
  level: fheq:6
  appliesTo: "honours degree graduates (section 4 table: Principles and concepts: application)"
  addressee: learner
  verbs: ["recognise", "develop", "minimise"]
  about: "managing clinical risk (honours degree)"
  themes: [none]
  domain: subject-skill
  award: ["bachelor's with honours"]
  gradeOf: none
  paraphrase: "Graduates of a honours degree should be able to recognise possible risks, suitable interventions and the need for protocols that reduce risk in good-quality care, as the minimum for the award."
  quote: full   # the issuer's statement is in `source` (D-std-0014)
  audience: both
  subjects: inherited
- id: qaa/veterinary-nursing-2024/4.2.b15.foundation
  locator: { number: "4.2.b15.foundation", headingPath: ["Benchmark standards", "Introduction"] }
  span: { start: 41075, end: 41180 }
  source: "Recognise potential risk and appropriate interventions to prevent complications occurring, where possible"
  stem: "4.2"
  statementType: threshold
  rung: threshold
  force: threshold
  level: fheq:5
  appliesTo: "foundation degree graduates (section 4 table: Principles and concepts: application)"
  addressee: learner
  verbs: ["recognise", "prevent"]
  about: "managing clinical risk (foundation degree)"
  themes: [none]
  domain: subject-skill
  award: ["foundation degree"]
  gradeOf: none
  paraphrase: "Graduates of a foundation degree should be able to recognise possible risks and the interventions that can head off complications, as the minimum for the award."
  quote: full   # the issuer's statement is in `source` (D-std-0014)
  audience: both
  subjects: inherited
- id: qaa/veterinary-nursing-2024/4.2.b15.masters
  locator: { number: "4.2.b15.masters", headingPath: ["Benchmark standards", "Introduction"] }
  span: { start: 41331, end: 41480 }
  source: "Critically evaluate and enhance current protocols of the management of risk in the veterinary practice, while informing strategic level and direction"
  stem: "4.2"
  statementType: threshold
  rung: threshold
  force: threshold
  level: fheq:7
  appliesTo: "master's degree graduates (section 4 table: Principles and concepts: application)"
  addressee: learner
  verbs: ["evaluate", "enhance", "informing"]
  about: "managing clinical risk (master's degree)"
  themes: [none]
  domain: subject-skill
  award: ["master's"]
  gradeOf: none
  paraphrase: "Graduates of a master's degree should be able to critically evaluate and improve a practice's risk-management protocols while shaping its strategy and direction, as the minimum for the award."
  quote: full   # the issuer's statement is in `source` (D-std-0014)
  audience: both
  subjects: inherited
- id: qaa/veterinary-nursing-2024/4.2.b16
  locator: { number: "4.2.b16", headingPath: ["Benchmark standards", "Introduction"] }
  span: { start: 41608, end: 41675 }
  source: "Critically analyse contemporary issues in animal health and welfare"
  stem: "4.2"
  statementType: threshold
  rung: threshold
  force: threshold
  level: fheq:6
  appliesTo: "honours degree graduates (section 4 table: Principles and concepts: application)"
  addressee: learner
  verbs: ["analyse"]
  about: "promoting animal health and welfare (honours degree)"
  themes: [none]
  domain: subject-skill
  award: ["bachelor's with honours"]
  gradeOf: none
  paraphrase: "Graduates of a honours degree should be able to critically analyse current issues in the health and welfare of animals, as the minimum for the award."
  quote: full   # the issuer's statement is in `source` (D-std-0014)
  audience: both
  subjects: inherited
- id: qaa/veterinary-nursing-2024/4.2.b16.foundation
  locator: { number: "4.2.b16.foundation", headingPath: ["Benchmark standards", "Introduction"] }
  span: { start: 41481, end: 41607 }
  source: "Analyse and interpret relevant educational/promotional information and use this knowledge to promote animal health and welfare"
  stem: "4.2"
  statementType: threshold
  rung: threshold
  force: threshold
  level: fheq:5
  appliesTo: "foundation degree graduates (section 4 table: Principles and concepts: application)"
  addressee: learner
  verbs: ["analyse", "interpret", "use", "promote"]
  about: "promoting animal health and welfare (foundation degree)"
  themes: [none]
  domain: subject-skill
  award: ["foundation degree"]
  gradeOf: none
  paraphrase: "Graduates of a foundation degree should be able to analyse and interpret educational and promotional material and draw on it to advance the health and welfare of animals, as the minimum for the award."
  quote: full   # the issuer's statement is in `source` (D-std-0014)
  audience: both
  subjects: inherited
- id: qaa/veterinary-nursing-2024/4.2.b16.masters
  locator: { number: "4.2.b16.masters", headingPath: ["Benchmark standards", "Introduction"] }
  span: { start: 41676, end: 41780 }
  source: "Develop innovative strategies to promote animal health and welfare in line with evidenced-based practice"
  stem: "4.2"
  statementType: threshold
  rung: threshold
  force: threshold
  level: fheq:7
  appliesTo: "master's degree graduates (section 4 table: Principles and concepts: application)"
  addressee: learner
  verbs: ["develop", "promote"]
  about: "promoting animal health and welfare (master's degree)"
  themes: [none]
  domain: subject-skill
  award: ["master's"]
  gradeOf: none
  paraphrase: "Graduates of a master's degree should be able to devise new strategies, grounded in evidence-based practice, to advance the health and welfare of animals, as the minimum for the award."
  quote: full   # the issuer's statement is in `source` (D-std-0014)
  audience: both
  subjects: inherited
- id: qaa/veterinary-nursing-2024/4.2.b17
  locator: { number: "4.2.b17", headingPath: ["Benchmark standards", "Introduction"] }
  span: { start: 41872, end: 42020 }
  source: "Articulate and justify decision-making and problem-solving processes associated with Veterinary Nursing practice even where there is incomplete data"
  stem: "4.2"
  statementType: threshold
  rung: threshold
  force: threshold
  level: fheq:6
  appliesTo: "honours degree graduates (section 4 table: Principles and concepts: application)"
  addressee: learner
  verbs: ["articulate", "justify"]
  about: "evidence behind clinical decisions (honours degree)"
  themes: [none]
  domain: subject-skill
  award: ["bachelor's with honours"]
  gradeOf: none
  paraphrase: "Graduates of a honours degree should be able to explain and justify the decisions and problem-solving behind veterinary nursing practice, even when the data are incomplete, as the minimum for the award."
  quote: full   # the issuer's statement is in `source` (D-std-0014)
  audience: both
  subjects: inherited
- id: qaa/veterinary-nursing-2024/4.2.b17.foundation
  locator: { number: "4.2.b17.foundation", headingPath: ["Benchmark standards", "Introduction"] }
  span: { start: 41781, end: 41870 }
  source: "Use appropriate research and suitable evidence to underpin and justify clinical decisions"
  stem: "4.2"
  statementType: threshold
  rung: threshold
  force: threshold
  level: fheq:5
  appliesTo: "foundation degree graduates (section 4 table: Principles and concepts: application)"
  addressee: learner
  verbs: ["use", "underpin", "justify"]
  about: "evidence behind clinical decisions (foundation degree)"
  themes: [none]
  domain: subject-skill
  award: ["foundation degree"]
  gradeOf: none
  paraphrase: "Graduates of a foundation degree should be able to draw on suitable research and evidence to support and justify clinical decisions, as the minimum for the award."
  quote: full   # the issuer's statement is in `source` (D-std-0014)
  audience: both
  subjects: inherited
- id: qaa/veterinary-nursing-2024/4.2.b17.masters
  locator: { number: "4.2.b17.masters", headingPath: ["Benchmark standards", "Introduction"] }
  span: { start: 42021, end: 42146 }
  source: "Systematically synthesise advanced and specialist information to develop innovative proposals to address complex patient care"
  stem: "4.2"
  statementType: threshold
  rung: threshold
  force: threshold
  level: fheq:7
  appliesTo: "master's degree graduates (section 4 table: Principles and concepts: application)"
  addressee: learner
  verbs: ["synthesise", "develop", "address"]
  about: "evidence behind clinical decisions (master's degree)"
  themes: [none]
  domain: subject-skill
  award: ["master's"]
  gradeOf: none
  paraphrase: "Graduates of a master's degree should be able to bring advanced, specialist information together systematically to propose new ways of meeting complex patient care needs, as the minimum for the award."
  quote: full   # the issuer's statement is in `source` (D-std-0014)
  audience: both
  subjects: inherited
- id: qaa/veterinary-nursing-2024/4.2.b18
  locator: { number: "4.2.b18", headingPath: ["Benchmark standards", "Introduction"] }
  span: { start: 42275, end: 42466 }
  source: "Use relevant theoretical and research evidence to undertake and document a comprehensive, systematic nursing assessment considering the needs of the patient and, where applicable, their owner"
  stem: "4.2"
  statementType: threshold
  rung: threshold
  force: threshold
  level: fheq:6
  appliesTo: "honours degree graduates (section 4 table: Principles and concepts: application)"
  addressee: learner
  verbs: ["use", "undertake", "document"]
  about: "nursing assessment (honours degree)"
  themes: [none]
  domain: subject-skill
  award: ["bachelor's with honours"]
  gradeOf: none
  paraphrase: "Graduates of a honours degree should be able to use theory and research to carry out and record a full, systematic nursing assessment that takes account of the patient's needs and, where relevant, the owner's, as the minimum for the award."
  quote: full   # the issuer's statement is in `source` (D-std-0014)
  audience: both
  subjects: inherited
- id: qaa/veterinary-nursing-2024/4.2.b18.foundation
  locator: { number: "4.2.b18.foundation", headingPath: ["Benchmark standards", "Introduction"] }
  span: { start: 42148, end: 42274 }
  source: "Undertake and document a systematic nursing assessment considering the needs of the patient and, where applicable, their owner"
  stem: "4.2"
  statementType: threshold
  rung: threshold
  force: threshold
  level: fheq:5
  appliesTo: "foundation degree graduates (section 4 table: Principles and concepts: application)"
  addressee: learner
  verbs: ["undertake", "document"]
  about: "nursing assessment (foundation degree)"
  themes: [none]
  domain: subject-skill
  award: ["foundation degree"]
  gradeOf: none
  paraphrase: "Graduates of a foundation degree should be able to carry out and record a systematic nursing assessment that takes account of the patient's needs and, where relevant, the owner's, as the minimum for the award."
  quote: full   # the issuer's statement is in `source` (D-std-0014)
  audience: both
  subjects: inherited
- id: qaa/veterinary-nursing-2024/4.2.b18.masters
  locator: { number: "4.2.b18.masters", headingPath: ["Benchmark standards", "Introduction"] }
  span: { start: 42467, end: 42621 }
  source: "Develop a systematic and evidence-based framework to assess the needs of the patient and owner (regardless of their cultural and socioeconomic background)"
  stem: "4.2"
  statementType: threshold
  rung: threshold
  force: threshold
  level: fheq:7
  appliesTo: "master's degree graduates (section 4 table: Principles and concepts: application)"
  addressee: learner
  verbs: ["develop", "assess"]
  about: "nursing assessment (master's degree)"
  themes: [none]
  domain: subject-skill
  award: ["master's"]
  gradeOf: none
  paraphrase: "Graduates of a master's degree should be able to build a systematic, evidence-based framework for assessing what patient and owner need, whatever their cultural or socioeconomic background, as the minimum for the award."
  quote: full   # the issuer's statement is in `source` (D-std-0014)
  audience: both
  subjects: inherited
- id: qaa/veterinary-nursing-2024/4.2.b19
  locator: { number: "4.2.b19", headingPath: ["Benchmark standards", "Introduction"] }
  span: { start: 42718, end: 42818 }
  source: "Evaluate evolving priorities within a complex and changing environment and communicate appropriately"
  stem: "4.2"
  statementType: threshold
  rung: threshold
  force: threshold
  level: fheq:6
  appliesTo: "honours degree graduates (section 4 table: Principles and concepts: application)"
  addressee: learner
  verbs: ["evaluate", "communicate"]
  about: "priorities and care delivery (honours degree)"
  themes: [none]
  domain: subject-skill
  award: ["bachelor's with honours"]
  gradeOf: none
  paraphrase: "Graduates of a honours degree should be able to evaluate shifting priorities in a complex, changing setting and communicate suitably, as the minimum for the award."
  quote: full   # the issuer's statement is in `source` (D-std-0014)
  audience: both
  subjects: inherited
- id: qaa/veterinary-nursing-2024/4.2.b19.foundation
  locator: { number: "4.2.b19.foundation", headingPath: ["Benchmark standards", "Introduction"] }
  span: { start: 42626, end: 42717 }
  source: "Assess priorities in nursing practice and deliver care competently to meet identified needs"
  stem: "4.2"
  statementType: threshold
  rung: threshold
  force: threshold
  level: fheq:5
  appliesTo: "foundation degree graduates (section 4 table: Principles and concepts: application)"
  addressee: learner
  verbs: ["assess", "deliver"]
  about: "priorities and care delivery (foundation degree)"
  themes: [none]
  domain: subject-skill
  award: ["foundation degree"]
  gradeOf: none
  paraphrase: "Graduates of a foundation degree should be able to judge nursing priorities and give competent care that meets the needs found, as the minimum for the award."
  quote: full   # the issuer's statement is in `source` (D-std-0014)
  audience: both
  subjects: inherited
- id: qaa/veterinary-nursing-2024/4.2.b19.masters
  locator: { number: "4.2.b19.masters", headingPath: ["Benchmark standards", "Introduction"] }
  span: { start: 42819, end: 42925 }
  source: "Facilitate team development, demonstrating leadership skills to ensure the team delivers the care required"
  stem: "4.2"
  statementType: threshold
  rung: threshold
  force: threshold
  level: fheq:7
  appliesTo: "master's degree graduates (section 4 table: Principles and concepts: application)"
  addressee: learner
  verbs: ["facilitate", "demonstrating", "delivers"]
  about: "priorities and care delivery (master's degree)"
  themes: [none]
  domain: subject-skill
  award: ["master's"]
  gradeOf: none
  paraphrase: "Graduates of a master's degree should be able to develop the team and show leadership so that the team gives the care needed, as the minimum for the award."
  quote: full   # the issuer's statement is in `source` (D-std-0014)
  audience: both
  subjects: inherited
- id: qaa/veterinary-nursing-2024/4.2.b20
  locator: { number: "4.2.b20", headingPath: ["Benchmark standards", "Introduction"] }
  span: { start: 43069, end: 43154 }
  source: "Critically evaluate research findings and use these to inform changes to planned care"
  stem: "4.2"
  statementType: threshold
  rung: threshold
  force: threshold
  level: fheq:6
  appliesTo: "honours degree graduates (section 4 table: Principles and concepts: application)"
  addressee: learner
  verbs: ["evaluate", "use", "inform"]
  about: "care planning and research (honours degree)"
  themes: [none]
  domain: subject-skill
  award: ["bachelor's with honours"]
  gradeOf: none
  paraphrase: "Graduates of a honours degree should be able to critically evaluate research findings and use them to change planned care, as the minimum for the award."
  quote: full   # the issuer's statement is in `source` (D-std-0014)
  audience: both
  subjects: inherited
- id: qaa/veterinary-nursing-2024/4.2.b20.foundation
  locator: { number: "4.2.b20.foundation", headingPath: ["Benchmark standards", "Introduction"] }
  span: { start: 42926, end: 43068 }
  source: "Formulate and document a plan of care with the collaboration of the veterinary team and consent of clients in the best interest of the patient"
  stem: "4.2"
  statementType: threshold
  rung: threshold
  force: threshold
  level: fheq:5
  appliesTo: "foundation degree graduates (section 4 table: Principles and concepts: application)"
  addressee: learner
  verbs: ["formulate", "document"]
  about: "care planning and research (foundation degree)"
  themes: [none]
  domain: subject-skill
  award: ["foundation degree"]
  gradeOf: none
  paraphrase: "Graduates of a foundation degree should be able to draw up and record a care plan with the veterinary team and the client's consent, in the patient's best interest, as the minimum for the award."
  quote: full   # the issuer's statement is in `source` (D-std-0014)
  audience: both
  subjects: inherited
- id: qaa/veterinary-nursing-2024/4.2.b20.masters
  locator: { number: "4.2.b20.masters", headingPath: ["Benchmark standards", "Introduction"] }
  span: { start: 43155, end: 43214 }
  source: "Create research and contribute and add to the evidence base"
  stem: "4.2"
  statementType: threshold
  rung: threshold
  force: threshold
  level: fheq:7
  appliesTo: "master's degree graduates (section 4 table: Principles and concepts: application)"
  addressee: learner
  verbs: ["create", "contribute", "add"]
  about: "care planning and research (master's degree)"
  themes: [none]
  domain: subject-skill
  award: ["master's"]
  gradeOf: none
  paraphrase: "Graduates of a master's degree should be able to produce research that adds to the evidence base, as the minimum for the award."
  quote: full   # the issuer's statement is in `source` (D-std-0014)
  audience: both
  subjects: inherited
- id: qaa/veterinary-nursing-2024/4.2.b21
  locator: { number: "4.2.b21", headingPath: ["Benchmark standards", "Introduction"] }
  span: { start: 43367, end: 43546 }
  source: "Demonstrate an ability to critically challenge the veterinary healthcare delivered, considering dynamic social, cultural, spiritual, legal, political, economic and welfare factors"
  stem: "4.2"
  statementType: threshold
  rung: threshold
  force: threshold
  level: fheq:6
  appliesTo: "honours degree graduates (section 4 table: Principles and concepts: application)"
  addressee: learner
  verbs: ["demonstrate", "challenge"]
  about: "accountability and the context of care (honours degree)"
  themes: [none]
  domain: subject-skill
  award: ["bachelor's with honours"]
  gradeOf: none
  paraphrase: "Graduates of a honours degree should be able to challenge critically the care delivered, weighing the shifting social, cultural, spiritual, legal, political and economic factors and animal welfare, as the minimum for the award."
  quote: full   # the issuer's statement is in `source` (D-std-0014)
  audience: both
  subjects: inherited
- id: qaa/veterinary-nursing-2024/4.2.b21.foundation
  locator: { number: "4.2.b21.foundation", headingPath: ["Benchmark standards", "Introduction"] }
  span: { start: 43215, end: 43366 }
  source: "Demonstrate accountability for veterinary healthcare delivered, considering social, cultural, spiritual, legal, political, economic and welfare factors"
  stem: "4.2"
  statementType: threshold
  rung: threshold
  force: threshold
  level: fheq:5
  appliesTo: "foundation degree graduates (section 4 table: Principles and concepts: application)"
  addressee: learner
  verbs: ["demonstrate"]
  about: "accountability and the context of care (foundation degree)"
  themes: [none]
  domain: subject-skill
  award: ["foundation degree"]
  gradeOf: none
  paraphrase: "Graduates of a foundation degree should be able to show accountability for the care given, weighing the social, cultural, spiritual, legal, political and economic factors and animal welfare, as the minimum for the award."
  quote: full   # the issuer's statement is in `source` (D-std-0014)
  audience: both
  subjects: inherited
- id: qaa/veterinary-nursing-2024/4.2.b21.masters
  locator: { number: "4.2.b21.masters", headingPath: ["Benchmark standards", "Introduction"] }
  span: { start: 43547, end: 43718 }
  source: "Act autonomously to make strategic decisions and develop appropriate practice guidelines, taking responsibility for outcomes in abstract and unpredictably complex contexts"
  stem: "4.2"
  statementType: threshold
  rung: threshold
  force: threshold
  level: fheq:7
  appliesTo: "master's degree graduates (section 4 table: Principles and concepts: application)"
  addressee: learner
  verbs: ["act", "make", "develop", "taking"]
  about: "accountability and the context of care (master's degree)"
  themes: [none]
  domain: subject-skill
  award: ["master's"]
  gradeOf: none
  paraphrase: "Graduates of a master's degree should be able to act autonomously in making strategic decisions and setting practice guidelines, owning the results in abstract, highly complex and unpredictable settings, as the minimum for the award."
  quote: full   # the issuer's statement is in `source` (D-std-0014)
  audience: both
  subjects: inherited
- id: qaa/veterinary-nursing-2024/4.2.b22
  locator: { number: "4.2.b22", headingPath: ["Benchmark standards", "Introduction"] }
  span: { start: 43795, end: 43900 }
  source: "Critically evaluate outcomes of professional interventions, adjusting Veterinary Nursing care accordingly"
  stem: "4.2"
  statementType: threshold
  rung: threshold
  force: threshold
  level: fheq:6
  appliesTo: "honours degree graduates (section 4 table: Principles and concepts: application)"
  addressee: learner
  verbs: ["evaluate", "adjusting"]
  about: "outcomes of interventions (honours degree)"
  themes: [none]
  domain: subject-skill
  award: ["bachelor's with honours"]
  gradeOf: none
  paraphrase: "Graduates of a honours degree should be able to critically evaluate the results of professional interventions and adjust nursing care to match, as the minimum for the award."
  quote: full   # the issuer's statement is in `source` (D-std-0014)
  audience: both
  subjects: inherited
- id: qaa/veterinary-nursing-2024/4.2.b22.foundation
  locator: { number: "4.2.b22.foundation", headingPath: ["Benchmark standards", "Introduction"] }
  span: { start: 43719, end: 43794 }
  source: "Accurately document and evaluate the outcomes of professional interventions"
  stem: "4.2"
  statementType: threshold
  rung: threshold
  force: threshold
  level: fheq:5
  appliesTo: "foundation degree graduates (section 4 table: Principles and concepts: application)"
  addressee: learner
  verbs: ["document", "evaluate"]
  about: "outcomes of interventions (foundation degree)"
  themes: [none]
  domain: subject-skill
  award: ["foundation degree"]
  gradeOf: none
  paraphrase: "Graduates of a foundation degree should be able to record accurately and evaluate the results of professional interventions, as the minimum for the award."
  quote: full   # the issuer's statement is in `source` (D-std-0014)
  audience: both
  subjects: inherited
- id: qaa/veterinary-nursing-2024/4.2.b22.masters
  locator: { number: "4.2.b22.masters", headingPath: ["Benchmark standards", "Introduction"] }
  span: { start: 43901, end: 44023 }
  source: "Use outcomes of interventions to inform development of self and others and disseminate/lead as part of clinical governance"
  stem: "4.2"
  statementType: threshold
  rung: threshold
  force: threshold
  level: fheq:7
  appliesTo: "master's degree graduates (section 4 table: Principles and concepts: application)"
  addressee: learner
  verbs: ["use", "inform", "disseminate", "lead"]
  about: "outcomes of interventions (master's degree)"
  themes: [none]
  domain: subject-skill
  award: ["master's"]
  gradeOf: none
  paraphrase: "Graduates of a master's degree should be able to use the results of interventions to develop themselves and others, and share findings or lead within clinical governance, as the minimum for the award."
  quote: full   # the issuer's statement is in `source` (D-std-0014)
  audience: both
  subjects: inherited
- id: qaa/veterinary-nursing-2024/4.2.b23
  locator: { number: "4.2.b23", headingPath: ["Benchmark standards", "Introduction"] }
  span: { start: 44152, end: 44261 }
  source: "Contribute with skill and confidence to effective multidisciplinary working, providing direction as necessary"
  stem: "4.2"
  statementType: threshold
  rung: threshold
  force: threshold
  level: fheq:6
  appliesTo: "honours degree graduates (section 4 table: Principles and concepts: application)"
  addressee: learner
  verbs: ["contribute", "providing"]
  about: "multidisciplinary teamwork (honours degree)"
  themes: [none]
  domain: subject-skill
  award: ["bachelor's with honours"]
  gradeOf: none
  paraphrase: "Graduates of a honours degree should be able to contribute skilfully and confidently to multidisciplinary work, giving direction where needed, as the minimum for the award."
  quote: full   # the issuer's statement is in `source` (D-std-0014)
  audience: both
  subjects: inherited
- id: qaa/veterinary-nursing-2024/4.2.b23.foundation
  locator: { number: "4.2.b23.foundation", headingPath: ["Benchmark standards", "Introduction"] }
  span: { start: 44024, end: 44151 }
  source: "Participate in teamwork that respects and uses the contributions of colleagues in a variety of veterinary healthcare situations"
  stem: "4.2"
  statementType: threshold
  rung: threshold
  force: threshold
  level: fheq:5
  appliesTo: "foundation degree graduates (section 4 table: Principles and concepts: application)"
  addressee: learner
  verbs: ["participate", "respects", "uses"]
  about: "multidisciplinary teamwork (foundation degree)"
  themes: [none]
  domain: subject-skill
  award: ["foundation degree"]
  gradeOf: none
  paraphrase: "Graduates of a foundation degree should be able to take part in teamwork that values and makes use of colleagues' contributions across veterinary care settings, as the minimum for the award."
  quote: full   # the issuer's statement is in `source` (D-std-0014)
  audience: both
  subjects: inherited
- id: qaa/veterinary-nursing-2024/4.2.b23.masters
  locator: { number: "4.2.b23.masters", headingPath: ["Benchmark standards", "Introduction"] }
  span: { start: 44262, end: 44460 }
  source: "Apply and develop advanced interpersonal, team and networking skills to strategically enhance team performance in unpredictably complex contexts and contribute to specialist professional communities"
  stem: "4.2"
  statementType: threshold
  rung: threshold
  force: threshold
  level: fheq:7
  appliesTo: "master's degree graduates (section 4 table: Principles and concepts: application)"
  addressee: learner
  verbs: ["apply", "develop", "enhance", "contribute"]
  about: "multidisciplinary teamwork (master's degree)"
  themes: [none]
  domain: subject-skill
  award: ["master's"]
  gradeOf: none
  paraphrase: "Graduates of a master's degree should be able to use and grow advanced interpersonal, team and networking skills to lift team performance strategically in highly complex settings and to take part in specialist professional communities, as the minimum for the award."
  quote: full   # the issuer's statement is in `source` (D-std-0014)
  audience: both
  subjects: inherited
- id: qaa/veterinary-nursing-2024/4.2.b24
  locator: { number: "4.2.b24", headingPath: ["Benchmark standards", "Introduction"] }
  span: { start: 44539, end: 44658 }
  source: "Critically evaluate the moral and ethical issues that relate to veterinary patient care and advocate for animal welfare"
  stem: "4.2"
  statementType: threshold
  rung: threshold
  force: threshold
  level: fheq:6
  appliesTo: "honours degree graduates (section 4 table: Principles and concepts: application)"
  addressee: learner
  verbs: ["evaluate", "advocate"]
  about: "ethics in patient care (honours degree)"
  themes: [none]
  domain: subject-skill
  award: ["bachelor's with honours"]
  gradeOf: none
  paraphrase: "Graduates of a honours degree should be able to critically evaluate the moral and ethical questions in caring for veterinary patients and speak up for animal welfare, as the minimum for the award."
  quote: full   # the issuer's statement is in `source` (D-std-0014)
  audience: both
  subjects: inherited
- id: qaa/veterinary-nursing-2024/4.2.b24.foundation
  locator: { number: "4.2.b24.foundation", headingPath: ["Benchmark standards", "Introduction"] }
  span: { start: 44461, end: 44538 }
  source: "Recognise the moral and ethical issues that relate to veterinary patient care"
  stem: "4.2"
  statementType: threshold
  rung: threshold
  force: threshold
  level: fheq:5
  appliesTo: "foundation degree graduates (section 4 table: Principles and concepts: application)"
  addressee: learner
  verbs: ["recognise"]
  about: "ethics in patient care (foundation degree)"
  themes: [none]
  domain: subject-skill
  award: ["foundation degree"]
  gradeOf: none
  paraphrase: "Graduates of a foundation degree should be able to recognise the moral and ethical questions in caring for veterinary patients, as the minimum for the award."
  quote: full   # the issuer's statement is in `source` (D-std-0014)
  audience: both
  subjects: inherited
- id: qaa/veterinary-nursing-2024/4.2.b24.masters
  locator: { number: "4.2.b24.masters", headingPath: ["Benchmark standards", "Introduction"] }
  span: { start: 44659, end: 44963 }
  source: "Systematically apply an advanced awareness of ethical and professional values and codes of conduct, to personal and strategic decisions, actions, responsibilities, outcomes and dilemmas, while working proactively with others to suggest and advocate appropriate solutions in unpredictably complex contexts"
  stem: "4.2"
  statementType: threshold
  rung: threshold
  force: threshold
  level: fheq:7
  appliesTo: "master's degree graduates (section 4 table: Principles and concepts: application)"
  addressee: learner
  verbs: ["apply", "working", "suggest", "advocate"]
  about: "ethics in patient care (master's degree)"
  themes: [none]
  domain: subject-skill
  award: ["master's"]
  gradeOf: none
  paraphrase: "Graduates of a master's degree should be able to apply an advanced grasp of ethical and professional values and codes systematically to personal and strategic decisions and dilemmas, working with others to propose and argue for solutions in highly complex settings, as the minimum for the award."
  quote: full   # the issuer's statement is in `source` (D-std-0014)
  audience: both
  subjects: inherited
- id: qaa/veterinary-nursing-2024/4.2.b25
  locator: { number: "4.2.b25", headingPath: ["Benchmark standards", "Introduction"] }
  span: { start: 45360, end: 45636 }
  source: "Demonstrate a robust knowledge of the fundamental subjects which underpin Veterinary Nursing, apply the knowledge and skills required of a veterinary nurse in everyday practice, and continually evaluate nursing care provision to inform the enhancement of professional practise"
  stem: "4.2"
  statementType: threshold
  rung: threshold
  force: threshold
  level: fheq:6
  appliesTo: "honours degree graduates (section 4 table: Subject knowledge, understanding and associated skills)"
  addressee: learner
  verbs: ["demonstrate", "apply", "evaluate"]
  about: "core subject knowledge (honours degree)"
  themes: [none]
  domain: knowledge
  award: ["bachelor's with honours"]
  gradeOf: none
  paraphrase: "Graduates of a honours degree should be able to show robust knowledge of the core subjects behind veterinary nursing, use a veterinary nurse's knowledge and skills in daily practice and keep evaluating nursing care to improve professional practice, as the minimum for the award."
  quote: full   # the issuer's statement is in `source` (D-std-0014)
  audience: both
  subjects: inherited
- id: qaa/veterinary-nursing-2024/4.2.b25.foundation
  locator: { number: "4.2.b25.foundation", headingPath: ["Benchmark standards", "Introduction"] }
  span: { start: 45179, end: 45358 }
  source: "Demonstrate a sound knowledge of the fundamental subjects which underpin Veterinary Nursing, and apply the knowledge and skills required of a veterinary nurse in everyday practice"
  stem: "4.2"
  statementType: threshold
  rung: threshold
  force: threshold
  level: fheq:5
  appliesTo: "foundation degree graduates (section 4 table: Subject knowledge, understanding and associated skills)"
  addressee: learner
  verbs: ["demonstrate", "apply"]
  about: "core subject knowledge (foundation degree)"
  themes: [none]
  domain: knowledge
  award: ["foundation degree"]
  gradeOf: none
  paraphrase: "Graduates of a foundation degree should be able to show sound knowledge of the core subjects behind veterinary nursing and use a veterinary nurse's knowledge and skills in daily practice, as the minimum for the award."
  quote: full   # the issuer's statement is in `source` (D-std-0014)
  audience: both
  subjects: inherited
- id: qaa/veterinary-nursing-2024/4.2.b25.masters
  locator: { number: "4.2.b25.masters", headingPath: ["Benchmark standards", "Introduction"] }
  span: { start: 45637, end: 45727 }
  source: "Be cognisant of the knowledge, skills and behaviours aligned to professional practitioners"
  stem: "4.2"
  statementType: threshold
  rung: threshold
  force: threshold
  level: fheq:7
  appliesTo: "master's degree graduates (section 4 table: Subject knowledge, understanding and associated skills)"
  addressee: learner
  verbs: ["be"]
  about: "core subject knowledge (master's degree)"
  themes: [none]
  domain: knowledge
  award: ["master's"]
  gradeOf: none
  paraphrase: "Graduates of a master's degree should be able to be aware of the knowledge, skills and behaviours expected of professional practitioners, as the minimum for the award."
  quote: full   # the issuer's statement is in `source` (D-std-0014)
  audience: both
  subjects: inherited
- id: qaa/veterinary-nursing-2024/4.2.b26
  locator: { number: "4.2.b26", headingPath: ["Benchmark standards", "Introduction"] }
  span: { start: 45847, end: 45970 }
  source: "Critically analyse the diversity of experience and values of groups and individuals to advance anti-discriminatory practice"
  stem: "4.2"
  statementType: threshold
  rung: threshold
  force: threshold
  level: fheq:6
  appliesTo: "honours degree graduates (section 4 table: Subject knowledge, understanding and associated skills)"
  addressee: learner
  verbs: ["analyse", "advance"]
  about: "cultural awareness and anti-discriminatory practice (honours degree)"
  themes: [none]
  domain: subject-skill
  award: ["bachelor's with honours"]
  gradeOf: none
  paraphrase: "Graduates of a honours degree should be able to critically analyse how experience and values differ across groups and individuals to further anti-discriminatory practice, as the minimum for the award."
  quote: full   # the issuer's statement is in `source` (D-std-0014)
  audience: both
  subjects: inherited
- id: qaa/veterinary-nursing-2024/4.2.b26.foundation
  locator: { number: "4.2.b26.foundation", headingPath: ["Benchmark standards", "Introduction"] }
  span: { start: 45728, end: 45845 }
  source: "Demonstrate the skills of cultural awareness and role modelling behaviours that underpin anti-discriminatory practice"
  stem: "4.2"
  statementType: threshold
  rung: threshold
  force: threshold
  level: fheq:5
  appliesTo: "foundation degree graduates (section 4 table: Subject knowledge, understanding and associated skills)"
  addressee: learner
  verbs: ["demonstrate"]
  about: "cultural awareness and anti-discriminatory practice (foundation degree)"
  themes: [none]
  domain: subject-skill
  award: ["foundation degree"]
  gradeOf: none
  paraphrase: "Graduates of a foundation degree should be able to show cultural awareness and model the behaviours that anti-discriminatory practice depends on, as the minimum for the award."
  quote: full   # the issuer's statement is in `source` (D-std-0014)
  audience: both
  subjects: inherited
- id: qaa/veterinary-nursing-2024/4.2.b26.masters
  locator: { number: "4.2.b26.masters", headingPath: ["Benchmark standards", "Introduction"] }
  span: { start: 45971, end: 46064 }
  source: "Apply the skills of inclusivity and adaptation in the pursuit of anti-discriminatory practice"
  stem: "4.2"
  statementType: threshold
  rung: threshold
  force: threshold
  level: fheq:7
  appliesTo: "master's degree graduates (section 4 table: Subject knowledge, understanding and associated skills)"
  addressee: learner
  verbs: ["apply"]
  about: "cultural awareness and anti-discriminatory practice (master's degree)"
  themes: [none]
  domain: subject-skill
  award: ["master's"]
  gradeOf: none
  paraphrase: "Graduates of a master's degree should be able to apply inclusive and adaptive skills in pursuing anti-discriminatory practice, as the minimum for the award."
  quote: full   # the issuer's statement is in `source` (D-std-0014)
  audience: both
  subjects: inherited
- id: qaa/veterinary-nursing-2024/4.2.b27
  locator: { number: "4.2.b27", headingPath: ["Benchmark standards", "Introduction"] }
  span: { start: 46190, end: 46310 }
  source: "Articulately present robust evidence in written and verbal format, using technology which supports sound decision-making"
  stem: "4.2"
  statementType: threshold
  rung: threshold
  force: threshold
  level: fheq:6
  appliesTo: "honours degree graduates (section 4 table: Subject knowledge, understanding and associated skills)"
  addressee: learner
  verbs: ["present", "using", "supports"]
  about: "communication and evidence-based decisions (honours degree)"
  themes: [none]
  domain: generic-skill
  award: ["bachelor's with honours"]
  gradeOf: none
  paraphrase: "Graduates of a honours degree should be able to present strong evidence clearly in writing and speech, using technology that supports sound decisions, as the minimum for the award."
  quote: full   # the issuer's statement is in `source` (D-std-0014)
  audience: both
  subjects: inherited
- id: qaa/veterinary-nursing-2024/4.2.b27.foundation
  locator: { number: "4.2.b27.foundation", headingPath: ["Benchmark standards", "Introduction"] }
  span: { start: 46065, end: 46189 }
  source: "Communicate effectively with others in a clear and articulate manner, to a wide variety of audiences, using a range of media"
  stem: "4.2"
  statementType: threshold
  rung: threshold
  force: threshold
  level: fheq:5
  appliesTo: "foundation degree graduates (section 4 table: Subject knowledge, understanding and associated skills)"
  addressee: learner
  verbs: ["communicate"]
  about: "communication and evidence-based decisions (foundation degree)"
  themes: [none]
  domain: generic-skill
  award: ["foundation degree"]
  gradeOf: none
  paraphrase: "Graduates of a foundation degree should be able to communicate clearly and articulately with many kinds of audience through a range of media, as the minimum for the award."
  quote: full   # the issuer's statement is in `source` (D-std-0014)
  audience: both
  subjects: inherited
- id: qaa/veterinary-nursing-2024/4.2.b27.masters
  locator: { number: "4.2.b27.masters", headingPath: ["Benchmark standards", "Introduction"] }
  span: { start: 46311, end: 46393 }
  source: "Demonstrate decision-making using evidence, criticality and originality in thought"
  stem: "4.2"
  statementType: threshold
  rung: threshold
  force: threshold
  level: fheq:7
  appliesTo: "master's degree graduates (section 4 table: Subject knowledge, understanding and associated skills)"
  addressee: learner
  verbs: ["demonstrate"]
  about: "communication and evidence-based decisions (master's degree)"
  themes: [none]
  domain: generic-skill
  award: ["master's"]
  gradeOf: none
  paraphrase: "Graduates of a master's degree should be able to show decision-making that uses evidence and is critical and original in its thinking, as the minimum for the award."
  quote: full   # the issuer's statement is in `source` (D-std-0014)
  audience: both
  subjects: inherited
- id: qaa/veterinary-nursing-2024/4.2.b28
  locator: { number: "4.2.b28", headingPath: ["Benchmark standards", "Introduction"] }
  span: { start: 46532, end: 46682 }
  source: "Enhance therapeutic interpersonal relationships with a diverse range of clients through creative use of concepts and theories\n\nand critical reflection"
  stem: "4.2"
  statementType: threshold
  rung: threshold
  force: threshold
  level: fheq:6
  appliesTo: "honours degree graduates (section 4 table: Subject knowledge, understanding and associated skills)"
  addressee: learner
  verbs: ["enhance"]
  about: "therapeutic client relationships (honours degree)"
  themes: [none]
  domain: subject-skill
  award: ["bachelor's with honours"]
  gradeOf: none
  paraphrase: "Graduates of a honours degree should be able to strengthen therapeutic relationships with a wide range of clients by creative use of concepts and theory and by critical reflection, as the minimum for the award."
  quote: full   # the issuer's statement is in `source` (D-std-0014)
  audience: both
  subjects: inherited
- id: qaa/veterinary-nursing-2024/4.2.b28.foundation
  locator: { number: "4.2.b28.foundation", headingPath: ["Benchmark standards", "Introduction"] }
  span: { start: 46394, end: 46531 }
  source: "Develop and maintain therapeutic interpersonal relationships with clients considering diversity, environments and other impacting factors"
  stem: "4.2"
  statementType: threshold
  rung: threshold
  force: threshold
  level: fheq:5
  appliesTo: "foundation degree graduates (section 4 table: Subject knowledge, understanding and associated skills)"
  addressee: learner
  verbs: ["develop", "maintain"]
  about: "therapeutic client relationships (foundation degree)"
  themes: [none]
  domain: subject-skill
  award: ["foundation degree"]
  gradeOf: none
  paraphrase: "Graduates of a foundation degree should be able to build and keep therapeutic relationships with clients, taking account of diversity, settings and other influences, as the minimum for the award."
  quote: full   # the issuer's statement is in `source` (D-std-0014)
  audience: both
  subjects: inherited
- id: qaa/veterinary-nursing-2024/4.2.b28.masters
  locator: { number: "4.2.b28.masters", headingPath: ["Benchmark standards", "Introduction"] }
  span: { start: 46683, end: 46773 }
  source: "Demonstrate inclusive and adaptive behaviours aligned with professional interrelationships"
  stem: "4.2"
  statementType: threshold
  rung: threshold
  force: threshold
  level: fheq:7
  appliesTo: "master's degree graduates (section 4 table: Subject knowledge, understanding and associated skills)"
  addressee: learner
  verbs: ["demonstrate"]
  about: "therapeutic client relationships (master's degree)"
  themes: [none]
  domain: subject-skill
  award: ["master's"]
  gradeOf: none
  paraphrase: "Graduates of a master's degree should be able to show inclusive, adaptive behaviour in professional relationships, as the minimum for the award."
  quote: full   # the issuer's statement is in `source` (D-std-0014)
  audience: both
  subjects: inherited
- id: qaa/veterinary-nursing-2024/4.2.b29
  locator: { number: "4.2.b29", headingPath: ["Benchmark standards", "Introduction"] }
  span: { start: 46913, end: 47111 }
  source: "Demonstrate robust and evidence-based modern and contemporary Veterinary Nursing using critical judgement to evaluate, inform decision-making and synthesise new approaches to enhance quality of care"
  stem: "4.2"
  statementType: threshold
  rung: threshold
  force: threshold
  level: fheq:6
  appliesTo: "honours degree graduates (section 4 table: Subject knowledge, understanding and associated skills)"
  addressee: learner
  verbs: ["demonstrate", "using", "evaluate", "inform", "synthesise", "enhance"]
  about: "contemporary evidence-based nursing (honours degree)"
  themes: [none]
  domain: subject-skill
  award: ["bachelor's with honours"]
  gradeOf: none
  paraphrase: "Graduates of a honours degree should be able to show robust, up-to-date, evidence-based veterinary nursing, using critical judgement to evaluate, guide decisions and combine new approaches that raise the quality of care, as the minimum for the award."
  quote: full   # the issuer's statement is in `source` (D-std-0014)
  audience: both
  subjects: inherited
- id: qaa/veterinary-nursing-2024/4.2.b29.foundation
  locator: { number: "4.2.b29.foundation", headingPath: ["Benchmark standards", "Introduction"] }
  span: { start: 46774, end: 46911 }
  source: "Reflect upon and provide modern, contemporary and evidence-based Veterinary Nursing through practical skills and application of knowledge"
  stem: "4.2"
  statementType: threshold
  rung: threshold
  force: threshold
  level: fheq:5
  appliesTo: "foundation degree graduates (section 4 table: Subject knowledge, understanding and associated skills)"
  addressee: learner
  verbs: ["reflect", "provide"]
  about: "contemporary evidence-based nursing (foundation degree)"
  themes: [none]
  domain: subject-skill
  award: ["foundation degree"]
  gradeOf: none
  paraphrase: "Graduates of a foundation degree should be able to reflect on and give up-to-date, evidence-based veterinary nursing through practical skill and applied knowledge, as the minimum for the award."
  quote: full   # the issuer's statement is in `source` (D-std-0014)
  audience: both
  subjects: inherited
- id: qaa/veterinary-nursing-2024/4.2.b29.masters
  locator: { number: "4.2.b29.masters", headingPath: ["Benchmark standards", "Introduction"] }
  span: { start: 47112, end: 47210 }
  source: "Articulate judgements using thoughtful, evidence-based and critical reasoning as a reflective base"
  stem: "4.2"
  statementType: threshold
  rung: threshold
  force: threshold
  level: fheq:7
  appliesTo: "master's degree graduates (section 4 table: Subject knowledge, understanding and associated skills)"
  addressee: learner
  verbs: ["articulate", "using"]
  about: "contemporary evidence-based nursing (master's degree)"
  themes: [none]
  domain: subject-skill
  award: ["master's"]
  gradeOf: none
  paraphrase: "Graduates of a master's degree should be able to express judgements through careful, evidence-based, critical reasoning grounded in reflection, as the minimum for the award."
  quote: full   # the issuer's statement is in `source` (D-std-0014)
  audience: both
  subjects: inherited
- id: qaa/veterinary-nursing-2024/4.2.b30
  locator: { number: "4.2.b30", headingPath: ["Benchmark standards", "Introduction"] }
  span: { start: 47316, end: 47470 }
  source: "Apply the skills of critical analysis and syntheses, using robust evidence and data in the creation of new theory, in the pursuit of healthcare excellence"
  stem: "4.2"
  statementType: threshold
  rung: threshold
  force: threshold
  level: fheq:6
  appliesTo: "honours degree graduates (section 4 table: Subject knowledge, understanding and associated skills)"
  addressee: learner
  verbs: ["apply", "using"]
  about: "evidence and data in judgement (honours degree)"
  themes: [none]
  domain: subject-skill
  award: ["bachelor's with honours"]
  gradeOf: none
  paraphrase: "Graduates of a honours degree should be able to apply critical analysis and synthesis, using strong evidence and data to build new theory in pursuit of excellent care, as the minimum for the award."
  quote: full   # the issuer's statement is in `source` (D-std-0014)
  audience: both
  subjects: inherited
- id: qaa/veterinary-nursing-2024/4.2.b30.foundation
  locator: { number: "4.2.b30.foundation", headingPath: ["Benchmark standards", "Introduction"] }
  span: { start: 47215, end: 47314 }
  source: "Use evidence, data and a range of technology to inform judgements and enhance veterinary healthcare"
  stem: "4.2"
  statementType: threshold
  rung: threshold
  force: threshold
  level: fheq:5
  appliesTo: "foundation degree graduates (section 4 table: Subject knowledge, understanding and associated skills)"
  addressee: learner
  verbs: ["use", "inform", "enhance"]
  about: "evidence and data in judgement (foundation degree)"
  themes: [none]
  domain: subject-skill
  award: ["foundation degree"]
  gradeOf: none
  paraphrase: "Graduates of a foundation degree should be able to use evidence, data and technology to inform judgements and improve veterinary care, as the minimum for the award."
  quote: full   # the issuer's statement is in `source` (D-std-0014)
  audience: both
  subjects: inherited
- id: qaa/veterinary-nursing-2024/4.2.b30.masters
  locator: { number: "4.2.b30.masters", headingPath: ["Benchmark standards", "Introduction"] }
  span: { start: 47471, end: 47611 }
  source: "Apply the skills of evaluation to apply critical reasoning to justify evidence-based judgements in the advancement of health care excellence"
  stem: "4.2"
  statementType: threshold
  rung: threshold
  force: threshold
  level: fheq:7
  appliesTo: "master's degree graduates (section 4 table: Subject knowledge, understanding and associated skills)"
  addressee: learner
  verbs: ["apply", "justify"]
  about: "evidence and data in judgement (master's degree)"
  themes: [none]
  domain: subject-skill
  award: ["master's"]
  gradeOf: none
  paraphrase: "Graduates of a master's degree should be able to apply evaluation and critical reasoning to justify evidence-based judgements that advance excellent care, as the minimum for the award."
  quote: full   # the issuer's statement is in `source` (D-std-0014)
  audience: both
  subjects: inherited
- id: qaa/veterinary-nursing-2024/4.2.b31
  locator: { number: "4.2.b31", headingPath: ["Benchmark standards", "Introduction"] }
  span: { start: 47690, end: 47858 }
  source: "Adopt a reflective approach to self- improvement using critical evaluation and analysis with consideration to the impact on colleagues, to enhance professional practice"
  stem: "4.2"
  statementType: threshold
  rung: threshold
  force: threshold
  level: fheq:6
  appliesTo: "honours degree graduates (section 4 table: Subject knowledge, understanding and associated skills)"
  addressee: learner
  verbs: ["adopt", "using", "enhance"]
  about: "reflection for self-improvement (honours degree)"
  themes: [none]
  domain: generic-skill
  award: ["bachelor's with honours"]
  gradeOf: none
  paraphrase: "Graduates of a honours degree should be able to reflect on their own improvement through critical evaluation and analysis, weighing the effect on colleagues, to strengthen professional practice, as the minimum for the award."
  quote: full   # the issuer's statement is in `source` (D-std-0014)
  audience: both
  subjects: inherited
- id: qaa/veterinary-nursing-2024/4.2.b31.foundation
  locator: { number: "4.2.b31.foundation", headingPath: ["Benchmark standards", "Introduction"] }
  span: { start: 47612, end: 47689 }
  source: "Apply skills of introspection and reflection to improve professional practice"
  stem: "4.2"
  statementType: threshold
  rung: threshold
  force: threshold
  level: fheq:5
  appliesTo: "foundation degree graduates (section 4 table: Subject knowledge, understanding and associated skills)"
  addressee: learner
  verbs: ["apply", "improve"]
  about: "reflection for self-improvement (foundation degree)"
  themes: [none]
  domain: generic-skill
  award: ["foundation degree"]
  gradeOf: none
  paraphrase: "Graduates of a foundation degree should be able to use introspection and reflection to improve professional practice, as the minimum for the award."
  quote: full   # the issuer's statement is in `source` (D-std-0014)
  audience: both
  subjects: inherited
- id: qaa/veterinary-nursing-2024/4.2.b31.masters
  locator: { number: "4.2.b31.masters", headingPath: ["Benchmark standards", "Introduction"] }
  span: { start: 47859, end: 47961 }
  source: "Consider an evaluative and critically reflective approach to self-improvement to professional practice"
  stem: "4.2"
  statementType: threshold
  rung: threshold
  force: threshold
  level: fheq:7
  appliesTo: "master's degree graduates (section 4 table: Subject knowledge, understanding and associated skills)"
  addressee: learner
  verbs: ["consider"]
  about: "reflection for self-improvement (master's degree)"
  themes: [none]
  domain: generic-skill
  award: ["master's"]
  gradeOf: none
  paraphrase: "Graduates of a master's degree should be able to take an evaluative, critically reflective approach to improving themselves in professional practice, as the minimum for the award."
  quote: full   # the issuer's statement is in `source` (D-std-0014)
  audience: both
  subjects: inherited
- id: qaa/veterinary-nursing-2024/4.2.b32
  locator: { number: "4.2.b32", headingPath: ["Benchmark standards", "Introduction"] }
  span: { start: 48349, end: 48546 }
  source: "Manage themselves, their own professional practise and that of others in accordance with the Code of Professional Conduct, and critically evaluate and reflect on their own abilities and limitations"
  stem: "4.2"
  statementType: threshold
  rung: threshold
  force: threshold
  level: fheq:6
  appliesTo: "honours degree graduates (section 4 table: Working as a professional veterinary nurse: expectations)"
  addressee: learner
  verbs: ["manage", "evaluate", "reflect"]
  about: "managing self and others under the code (honours degree)"
  themes: [none]
  domain: subject-skill
  award: ["bachelor's with honours"]
  gradeOf: none
  paraphrase: "Graduates of a honours degree should be able to manage themselves, their practice and that of others in line with the professional code of conduct, and weigh up critically, and reflect on, their own strengths and limits, as the minimum for the award."
  quote: full   # the issuer's statement is in `source` (D-std-0014)
  audience: both
  subjects: inherited
- id: qaa/veterinary-nursing-2024/4.2.b32.foundation
  locator: { number: "4.2.b32.foundation", headingPath: ["Benchmark standards", "Introduction"] }
  span: { start: 48176, end: 48347 }
  source: "Manage themselves, their own professional practise and that of others, in accordance with the Code of Professional Conduct, recognising their own abilities and limitations"
  stem: "4.2"
  statementType: threshold
  rung: threshold
  force: threshold
  level: fheq:5
  appliesTo: "foundation degree graduates (section 4 table: Working as a professional veterinary nurse: expectations)"
  addressee: learner
  verbs: ["manage", "recognising"]
  about: "managing self and others under the code (foundation degree)"
  themes: [none]
  domain: subject-skill
  award: ["foundation degree"]
  gradeOf: none
  paraphrase: "Graduates of a foundation degree should be able to manage themselves, their practice and that of others in line with the professional code of conduct, knowing their own strengths and limits, as the minimum for the award."
  quote: full   # the issuer's statement is in `source` (D-std-0014)
  audience: both
  subjects: inherited
- id: qaa/veterinary-nursing-2024/4.2.b32.masters
  locator: { number: "4.2.b32.masters", headingPath: ["Benchmark standards", "Introduction"] }
  span: { start: 48548, end: 48766 }
  source: "Manage themselves, their own professional practise and that of others in accordance with the Code of Professional Conduct. Critically evaluate and reflect on the importance of educating and promoting these expectations"
  stem: "4.2"
  statementType: threshold
  rung: threshold
  force: threshold
  level: fheq:7
  appliesTo: "master's degree graduates (section 4 table: Working as a professional veterinary nurse: expectations)"
  addressee: learner
  verbs: ["manage", "evaluate", "reflect"]
  about: "managing self and others under the code (master's degree)"
  themes: [none]
  domain: subject-skill
  award: ["master's"]
  gradeOf: none
  paraphrase: "Graduates of a master's degree should be able to manage themselves, their practice and that of others in line with the professional code of conduct, and critically evaluate and reflect on why teaching and promoting those expectations matters, as the minimum for the award."
  quote: full   # the issuer's statement is in `source` (D-std-0014)
  audience: both
  subjects: inherited
- id: qaa/veterinary-nursing-2024/4.2.b33
  locator: { number: "4.2.b33", headingPath: ["Benchmark standards", "Introduction"] }
  span: { start: 48866, end: 48963 }
  source: "Select and apply knowledge and skills to a variety of clinical settings and unexpected situations"
  stem: "4.2"
  statementType: threshold
  rung: threshold
  force: threshold
  level: fheq:6
  appliesTo: "honours degree graduates (section 4 table: Working as a professional veterinary nurse: expectations)"
  addressee: learner
  verbs: ["select", "apply"]
  about: "applying knowledge across clinical settings (honours degree)"
  themes: [none]
  domain: subject-skill
  award: ["bachelor's with honours"]
  gradeOf: none
  paraphrase: "Graduates of a honours degree should be able to choose and apply knowledge and skills across different clinical settings and unforeseen situations, as the minimum for the award."
  quote: full   # the issuer's statement is in `source` (D-std-0014)
  audience: both
  subjects: inherited
- id: qaa/veterinary-nursing-2024/4.2.b33.foundation
  locator: { number: "4.2.b33.foundation", headingPath: ["Benchmark standards", "Introduction"] }
  span: { start: 48767, end: 48864 }
  source: "Select and apply knowledge and skills to a variety of clinical settings and unexpected situations"
  stem: "4.2"
  statementType: threshold
  rung: threshold
  force: threshold
  level: fheq:5
  appliesTo: "foundation degree graduates (section 4 table: Working as a professional veterinary nurse: expectations)"
  addressee: learner
  verbs: ["select", "apply"]
  about: "applying knowledge across clinical settings (foundation degree)"
  themes: [none]
  domain: subject-skill
  award: ["foundation degree"]
  gradeOf: none
  paraphrase: "Graduates of a foundation degree should be able to choose and apply knowledge and skills across different clinical settings and unforeseen situations, as the minimum for the award."
  quote: full   # the issuer's statement is in `source` (D-std-0014)
  audience: both
  subjects: inherited
- id: qaa/veterinary-nursing-2024/4.2.b33.masters
  locator: { number: "4.2.b33.masters", headingPath: ["Benchmark standards", "Introduction"] }
  span: { start: 48965, end: 49111 }
  source: "Develop knowledge and skills through contribution to evidence-based Veterinary Nursing to a variety of clinical settings and unexpected situations"
  stem: "4.2"
  statementType: threshold
  rung: threshold
  force: threshold
  level: fheq:7
  appliesTo: "master's degree graduates (section 4 table: Working as a professional veterinary nurse: expectations)"
  addressee: learner
  verbs: ["develop"]
  about: "applying knowledge across clinical settings (master's degree)"
  themes: [none]
  domain: subject-skill
  award: ["master's"]
  gradeOf: none
  paraphrase: "Graduates of a master's degree should be able to extend knowledge and skills by contributing to evidence-based veterinary nursing across different clinical settings and unforeseen situations, as the minimum for the award."
  quote: full   # the issuer's statement is in `source` (D-std-0014)
  audience: both
  subjects: inherited
- id: qaa/veterinary-nursing-2024/4.2.b34
  locator: { number: "4.2.b34", headingPath: ["Benchmark standards", "Introduction"] }
  span: { start: 49284, end: 49488 }
  source: "Implement strategies to promote and evaluate collaborative working with patients, clients and colleagues to identify and provide therapeutic and preventative veterinary healthcare requirements of patients"
  stem: "4.2"
  statementType: threshold
  rung: threshold
  force: threshold
  level: fheq:6
  appliesTo: "honours degree graduates (section 4 table: Working as a professional veterinary nurse: expectations)"
  addressee: learner
  verbs: ["implement", "promote", "evaluate"]
  about: "collaborative therapeutic and preventive care (honours degree)"
  themes: [none]
  domain: subject-skill
  award: ["bachelor's with honours"]
  gradeOf: none
  paraphrase: "Graduates of a honours degree should be able to put in place strategies that promote and evaluate collaboration with patients, clients and colleagues in identifying and giving therapeutic and preventive care, as the minimum for the award."
  quote: full   # the issuer's statement is in `source` (D-std-0014)
  audience: both
  subjects: inherited
- id: qaa/veterinary-nursing-2024/4.2.b34.foundation
  locator: { number: "4.2.b34.foundation", headingPath: ["Benchmark standards", "Introduction"] }
  span: { start: 49112, end: 49283 }
  source: "Work in collaboration with clients and colleagues to identify and provide the therapeutic and preventative veterinary healthcare requirements to meet the needs of patients"
  stem: "4.2"
  statementType: threshold
  rung: threshold
  force: threshold
  level: fheq:5
  appliesTo: "foundation degree graduates (section 4 table: Working as a professional veterinary nurse: expectations)"
  addressee: learner
  verbs: ["work", "identify", "provide"]
  about: "collaborative therapeutic and preventive care (foundation degree)"
  themes: [none]
  domain: subject-skill
  award: ["foundation degree"]
  gradeOf: none
  paraphrase: "Graduates of a foundation degree should be able to work with clients and colleagues to identify and give the therapeutic and preventive care patients need, as the minimum for the award."
  quote: full   # the issuer's statement is in `source` (D-std-0014)
  audience: both
  subjects: inherited
- id: qaa/veterinary-nursing-2024/4.2.b34.masters
  locator: { number: "4.2.b34.masters", headingPath: ["Benchmark standards", "Introduction"] }
  span: { start: 49489, end: 49694 }
  source: "Synthesise strategies to promote and evaluate collaborative working with patients, clients and colleagues to identify and provide therapeutic and preventative veterinary healthcare requirements of patients"
  stem: "4.2"
  statementType: threshold
  rung: threshold
  force: threshold
  level: fheq:7
  appliesTo: "master's degree graduates (section 4 table: Working as a professional veterinary nurse: expectations)"
  addressee: learner
  verbs: ["synthesise", "promote", "evaluate"]
  about: "collaborative therapeutic and preventive care (master's degree)"
  themes: [none]
  domain: subject-skill
  award: ["master's"]
  gradeOf: none
  paraphrase: "Graduates of a master's degree should be able to synthesise strategies that promote and evaluate collaboration with patients, clients and colleagues in identifying and giving therapeutic and preventive care, as the minimum for the award."
  quote: full   # the issuer's statement is in `source` (D-std-0014)
  audience: both
  subjects: inherited
- id: qaa/veterinary-nursing-2024/4.2.b35
  locator: { number: "4.2.b35", headingPath: ["Benchmark standards", "Introduction"] }
  span: { start: 49814, end: 49968 }
  source: "Anticipate and deal with challenging situations, involving patients, clients and colleagues, in an empathetic manner while minimising risk where necessary"
  stem: "4.2"
  statementType: threshold
  rung: threshold
  force: threshold
  level: fheq:6
  appliesTo: "honours degree graduates (section 4 table: Working as a professional veterinary nurse: expectations)"
  addressee: learner
  verbs: ["anticipate", "deal", "minimising"]
  about: "empathy in challenging situations (honours degree)"
  themes: [none]
  domain: subject-skill
  award: ["bachelor's with honours"]
  gradeOf: none
  paraphrase: "Graduates of a honours degree should be able to foresee and handle difficult situations with patients, clients and colleagues with empathy, reducing risk where needed, as the minimum for the award."
  quote: full   # the issuer's statement is in `source` (D-std-0014)
  audience: both
  subjects: inherited
- id: qaa/veterinary-nursing-2024/4.2.b35.foundation
  locator: { number: "4.2.b35.foundation", headingPath: ["Benchmark standards", "Introduction"] }
  span: { start: 49699, end: 49812 }
  source: "Provide empathetic support to patients, clients and colleagues in changing and potentially challenging situations"
  stem: "4.2"
  statementType: threshold
  rung: threshold
  force: threshold
  level: fheq:5
  appliesTo: "foundation degree graduates (section 4 table: Working as a professional veterinary nurse: expectations)"
  addressee: learner
  verbs: ["provide"]
  about: "empathy in challenging situations (foundation degree)"
  themes: [none]
  domain: subject-skill
  award: ["foundation degree"]
  gradeOf: none
  paraphrase: "Graduates of a foundation degree should be able to give empathetic support to patients, clients and colleagues when situations change or become difficult, as the minimum for the award."
  quote: full   # the issuer's statement is in `source` (D-std-0014)
  audience: both
  subjects: inherited
- id: qaa/veterinary-nursing-2024/4.2.b35.masters
  locator: { number: "4.2.b35.masters", headingPath: ["Benchmark standards", "Introduction"] }
  span: { start: 49970, end: 50157 }
  source: "Lead and support colleagues through a diverse range of challenging situations, involving patients, clients and colleagues, in an empathetic manner while minimising risk, where appropriate"
  stem: "4.2"
  statementType: threshold
  rung: threshold
  force: threshold
  level: fheq:7
  appliesTo: "master's degree graduates (section 4 table: Working as a professional veterinary nurse: expectations)"
  addressee: learner
  verbs: ["lead", "support"]
  about: "empathy in challenging situations (master's degree)"
  themes: [none]
  domain: subject-skill
  award: ["master's"]
  gradeOf: none
  paraphrase: "Graduates of a master's degree should be able to lead and support colleagues through many kinds of difficult situation with patients, clients and colleagues, with empathy and with risk kept low where fitting, as the minimum for the award."
  quote: full   # the issuer's statement is in `source` (D-std-0014)
  audience: both
  subjects: inherited
- id: qaa/veterinary-nursing-2024/4.2.b36
  locator: { number: "4.2.b36", headingPath: ["Benchmark standards", "Introduction"] }
  span: { start: 50234, end: 50366 }
  source: "Recognise the complexity of the professional, ethical and legal framework and its impact on decision-making and practise accordingly"
  stem: "4.2"
  statementType: threshold
  rung: threshold
  force: threshold
  level: fheq:6
  appliesTo: "honours degree graduates (section 4 table: Working as a professional veterinary nurse: expectations)"
  addressee: learner
  verbs: ["recognise", "practise"]
  about: "the professional, ethical and legal framework (honours degree)"
  themes: [none]
  domain: subject-skill
  award: ["bachelor's with honours"]
  gradeOf: none
  paraphrase: "Graduates of a honours degree should be able to recognise how complex the professional, ethical and legal framework is and how it bears on decisions, and practise to match, as the minimum for the award."
  quote: full   # the issuer's statement is in `source` (D-std-0014)
  audience: both
  subjects: inherited
- id: qaa/veterinary-nursing-2024/4.2.b36.foundation
  locator: { number: "4.2.b36.foundation", headingPath: ["Benchmark standards", "Introduction"] }
  span: { start: 50159, end: 50232 }
  source: "Practise in accordance with the professional, ethical and legal framework"
  stem: "4.2"
  statementType: threshold
  rung: threshold
  force: threshold
  level: fheq:5
  appliesTo: "foundation degree graduates (section 4 table: Working as a professional veterinary nurse: expectations)"
  addressee: learner
  verbs: ["practise"]
  about: "the professional, ethical and legal framework (foundation degree)"
  themes: [none]
  domain: subject-skill
  award: ["foundation degree"]
  gradeOf: none
  paraphrase: "Graduates of a foundation degree should be able to practise within the professional, ethical and legal framework, as the minimum for the award."
  quote: full   # the issuer's statement is in `source` (D-std-0014)
  audience: both
  subjects: inherited
- id: qaa/veterinary-nursing-2024/4.2.b36.masters
  locator: { number: "4.2.b36.masters", headingPath: ["Benchmark standards", "Introduction"] }
  span: { start: 50368, end: 50534 }
  source: "Appraise the complexity of the professional, ethical and legal frameworks. Provide guidance and leadership to colleagues in relation to the impacts of decision-making"
  stem: "4.2"
  statementType: threshold
  rung: threshold
  force: threshold
  level: fheq:7
  appliesTo: "master's degree graduates (section 4 table: Working as a professional veterinary nurse: expectations)"
  addressee: learner
  verbs: ["appraise", "provide"]
  about: "the professional, ethical and legal framework (master's degree)"
  themes: [none]
  domain: subject-skill
  award: ["master's"]
  gradeOf: none
  paraphrase: "Graduates of a master's degree should be able to appraise how complex the professional, ethical and legal frameworks are, and guide and lead colleagues on what decisions entail, as the minimum for the award."
  quote: full   # the issuer's statement is in `source` (D-std-0014)
  audience: both
  subjects: inherited
- id: qaa/veterinary-nursing-2024/4.2.b37
  locator: { number: "4.2.b37", headingPath: ["Benchmark standards", "Introduction"] }
  span: { start: 50625, end: 50719 }
  source: "Critically reflect on personal responsibility and decision-making across a range of situations"
  stem: "4.2"
  statementType: threshold
  rung: threshold
  force: threshold
  level: fheq:6
  appliesTo: "honours degree graduates (section 4 table: Working as a professional veterinary nurse: expectations)"
  addressee: learner
  verbs: ["reflect"]
  about: "responsibility and impartial decisions (honours degree)"
  themes: [none]
  domain: subject-skill
  award: ["bachelor's with honours"]
  gradeOf: none
  paraphrase: "Graduates of a honours degree should be able to reflect critically on personal responsibility and decision-making in many situations, as the minimum for the award."
  quote: full   # the issuer's statement is in `source` (D-std-0014)
  audience: both
  subjects: inherited
- id: qaa/veterinary-nursing-2024/4.2.b37.foundation
  locator: { number: "4.2.b37.foundation", headingPath: ["Benchmark standards", "Introduction"] }
  span: { start: 50535, end: 50624 }
  source: "Uphold personal responsibility and impartial decision-making across a range of situations"
  stem: "4.2"
  statementType: threshold
  rung: threshold
  force: threshold
  level: fheq:5
  appliesTo: "foundation degree graduates (section 4 table: Working as a professional veterinary nurse: expectations)"
  addressee: learner
  verbs: ["uphold"]
  about: "responsibility and impartial decisions (foundation degree)"
  themes: [none]
  domain: subject-skill
  award: ["foundation degree"]
  gradeOf: none
  paraphrase: "Graduates of a foundation degree should be able to uphold personal responsibility and impartial decisions in many situations, as the minimum for the award."
  quote: full   # the issuer's statement is in `source` (D-std-0014)
  audience: both
  subjects: inherited
- id: qaa/veterinary-nursing-2024/4.2.b37.masters
  locator: { number: "4.2.b37.masters", headingPath: ["Benchmark standards", "Introduction"] }
  span: { start: 50720, end: 50854 }
  source: "Critically reflect and evaluate on both personal and interprofessional responsibility and decision-making across a range of situations"
  stem: "4.2"
  statementType: threshold
  rung: threshold
  force: threshold
  level: fheq:7
  appliesTo: "master's degree graduates (section 4 table: Working as a professional veterinary nurse: expectations)"
  addressee: learner
  verbs: ["reflect", "evaluate"]
  about: "responsibility and impartial decisions (master's degree)"
  themes: [none]
  domain: subject-skill
  award: ["master's"]
  gradeOf: none
  paraphrase: "Graduates of a master's degree should be able to reflect critically on, and evaluate, personal and interprofessional responsibility and decision-making in many situations, as the minimum for the award."
  quote: full   # the issuer's statement is in `source` (D-std-0014)
  audience: both
  subjects: inherited
- id: qaa/veterinary-nursing-2024/4.2.b38
  locator: { number: "4.2.b38", headingPath: ["Benchmark standards", "Introduction"] }
  span: { start: 50944, end: 51068 }
  source: "Select and implement a range of risk management strategies to create and maintain a safe clinical environment for protection"
  stem: "4.2"
  statementType: threshold
  rung: threshold
  force: threshold
  level: fheq:6
  appliesTo: "honours degree graduates (section 4 table: Working as a professional veterinary nurse: expectations)"
  addressee: learner
  verbs: ["select", "implement", "create", "maintain"]
  about: "a safe clinical environment (honours degree)"
  themes: [none]
  domain: subject-skill
  award: ["bachelor's with honours"]
  gradeOf: none
  paraphrase: "Graduates of a honours degree should be able to choose and put in place several risk-management strategies that create and keep a safe clinical environment, as the minimum for the award."
  quote: full   # the issuer's statement is in `source` (D-std-0014)
  audience: both
  subjects: inherited
- id: qaa/veterinary-nursing-2024/4.2.b38.foundation
  locator: { number: "4.2.b38.foundation", headingPath: ["Benchmark standards", "Introduction"] }
  span: { start: 50855, end: 50942 }
  source: "Contribute to public protection by creating and maintaining a safe clinical environment"
  stem: "4.2"
  statementType: threshold
  rung: threshold
  force: threshold
  level: fheq:5
  appliesTo: "foundation degree graduates (section 4 table: Working as a professional veterinary nurse: expectations)"
  addressee: learner
  verbs: ["contribute", "creating", "maintaining"]
  about: "a safe clinical environment (foundation degree)"
  themes: [none]
  domain: subject-skill
  award: ["foundation degree"]
  gradeOf: none
  paraphrase: "Graduates of a foundation degree should be able to help protect the public by creating and keeping a safe clinical environment, as the minimum for the award."
  quote: full   # the issuer's statement is in `source` (D-std-0014)
  audience: both
  subjects: inherited
- id: qaa/veterinary-nursing-2024/4.2.b38.masters
  locator: { number: "4.2.b38.masters", headingPath: ["Benchmark standards", "Introduction"] }
  span: { start: 51070, end: 51234 }
  source: "Analyse and inform processes to improve a range of risk and management strategies to create and maintain a safe clinical environment, taking into account one health"
  stem: "4.2"
  statementType: threshold
  rung: threshold
  force: threshold
  level: fheq:7
  appliesTo: "master's degree graduates (section 4 table: Working as a professional veterinary nurse: expectations)"
  addressee: learner
  verbs: ["analyse", "inform", "improve"]
  about: "a safe clinical environment (master's degree)"
  themes: [none]
  domain: subject-skill
  award: ["master's"]
  gradeOf: none
  paraphrase: "Graduates of a master's degree should be able to analyse and shape processes that improve risk-management strategies for a safe clinical environment, with one health in view, as the minimum for the award."
  quote: full   # the issuer's statement is in `source` (D-std-0014)
  audience: both
  subjects: inherited
- id: qaa/veterinary-nursing-2024/4.2.b39
  locator: { number: "4.2.b39", headingPath: ["Benchmark standards", "Introduction"] }
  span: { start: 51321, end: 51464 }
  source: "Provide guidance, role-modelling, mentorship and support to others in the veterinary environment, ensuring effective supervision and monitoring"
  stem: "4.2"
  statementType: threshold
  rung: threshold
  force: threshold
  level: fheq:6
  appliesTo: "honours degree graduates (section 4 table: Working as a professional veterinary nurse: expectations)"
  addressee: learner
  verbs: ["provide", "ensuring"]
  about: "guidance, role-modelling and mentorship (honours degree)"
  themes: [none]
  domain: subject-skill
  award: ["bachelor's with honours"]
  gradeOf: none
  paraphrase: "Graduates of a honours degree should be able to guide, set an example for, mentor and support others in the veterinary setting, making sure supervision and monitoring work, as the minimum for the award."
  quote: full   # the issuer's statement is in `source` (D-std-0014)
  audience: both
  subjects: inherited
- id: qaa/veterinary-nursing-2024/4.2.b39.foundation
  locator: { number: "4.2.b39.foundation", headingPath: ["Benchmark standards", "Introduction"] }
  span: { start: 51235, end: 51319 }
  source: "Provide guidance, role-modelling and support to others in the veterinary environment"
  stem: "4.2"
  statementType: threshold
  rung: threshold
  force: threshold
  level: fheq:5
  appliesTo: "foundation degree graduates (section 4 table: Working as a professional veterinary nurse: expectations)"
  addressee: learner
  verbs: ["provide"]
  about: "guidance, role-modelling and mentorship (foundation degree)"
  themes: [none]
  domain: subject-skill
  award: ["foundation degree"]
  gradeOf: none
  paraphrase: "Graduates of a foundation degree should be able to guide, set an example for and support others in the veterinary setting, as the minimum for the award."
  quote: full   # the issuer's statement is in `source` (D-std-0014)
  audience: both
  subjects: inherited
- id: qaa/veterinary-nursing-2024/4.2.b39.masters
  locator: { number: "4.2.b39.masters", headingPath: ["Benchmark standards", "Introduction"] }
  span: { start: 51466, end: 51600 }
  source: "Inspire self and others to act as ambassadors to uphold the reputation of the profession both in and out of the veterinary environment"
  stem: "4.2"
  statementType: threshold
  rung: threshold
  force: threshold
  level: fheq:7
  appliesTo: "master's degree graduates (section 4 table: Working as a professional veterinary nurse: expectations)"
  addressee: learner
  verbs: ["inspire", "act", "uphold"]
  about: "guidance, role-modelling and mentorship (master's degree)"
  themes: [none]
  domain: subject-skill
  award: ["master's"]
  gradeOf: none
  paraphrase: "Graduates of a master's degree should be able to inspire themselves and others to act as ambassadors who uphold the profession's reputation inside and outside the veterinary setting, as the minimum for the award."
  quote: full   # the issuer's statement is in `source` (D-std-0014)
  audience: both
  subjects: inherited
- id: qaa/veterinary-nursing-2024/4.2.b40
  locator: { number: "4.2.b40", headingPath: ["Benchmark standards", "Introduction"] }
  span: { start: 51718, end: 51830 }
  source: "Critically analyse roles of self and of others, including appropriate delegation, supervision and seeking advice"
  stem: "4.2"
  statementType: threshold
  rung: threshold
  force: threshold
  level: fheq:6
  appliesTo: "honours degree graduates (section 4 table: Working as a professional veterinary nurse: expectations)"
  addressee: learner
  verbs: ["analyse"]
  about: "roles, delegation and supervision (honours degree)"
  themes: [none]
  domain: subject-skill
  award: ["bachelor's with honours"]
  gradeOf: none
  paraphrase: "Graduates of a honours degree should be able to critically analyse their own role and others', including suitable delegation, supervision and advice-seeking, as the minimum for the award."
  quote: full   # the issuer's statement is in `source` (D-std-0014)
  audience: both
  subjects: inherited
- id: qaa/veterinary-nursing-2024/4.2.b40.foundation
  locator: { number: "4.2.b40.foundation", headingPath: ["Benchmark standards", "Introduction"] }
  span: { start: 51601, end: 51716 }
  source: "Understand the role of self and of others, including when delegation, supervision and seeking advice is appropriate"
  stem: "4.2"
  statementType: threshold
  rung: threshold
  force: threshold
  level: fheq:5
  appliesTo: "foundation degree graduates (section 4 table: Working as a professional veterinary nurse: expectations)"
  addressee: learner
  verbs: ["understand"]
  about: "roles, delegation and supervision (foundation degree)"
  themes: [none]
  domain: subject-skill
  award: ["foundation degree"]
  gradeOf: none
  paraphrase: "Graduates of a foundation degree should be able to understand their own role and others', including when to delegate, supervise or ask for advice, as the minimum for the award."
  quote: full   # the issuer's statement is in `source` (D-std-0014)
  audience: both
  subjects: inherited
- id: qaa/veterinary-nursing-2024/4.2.b40.masters
  locator: { number: "4.2.b40.masters", headingPath: ["Benchmark standards", "Introduction"] }
  span: { start: 51832, end: 51979 }
  source: "Critically evaluate and reflect upon roles of self and of others, providing guidance on appropriate delegation, supervision and when to seek advice"
  stem: "4.2"
  statementType: threshold
  rung: threshold
  force: threshold
  level: fheq:7
  appliesTo: "master's degree graduates (section 4 table: Working as a professional veterinary nurse: expectations)"
  addressee: learner
  verbs: ["evaluate", "reflect", "providing"]
  about: "roles, delegation and supervision (master's degree)"
  themes: [none]
  domain: subject-skill
  award: ["master's"]
  gradeOf: none
  paraphrase: "Graduates of a master's degree should be able to critically evaluate and reflect on their own role and others', guiding others on suitable delegation, supervision and when to seek advice, as the minimum for the award."
  quote: full   # the issuer's statement is in `source` (D-std-0014)
  audience: both
  subjects: inherited
- id: qaa/veterinary-nursing-2024/4.2.b41
  locator: { number: "4.2.b41", headingPath: ["Benchmark standards", "Introduction"] }
  span: { start: 52159, end: 52329 }
  source: "Provide advice to clients and act as an advocate for them and the patient, when appropriate, with an appreciation for their own\n\nmental and physical health and well-being"
  stem: "4.2"
  statementType: threshold
  rung: threshold
  force: threshold
  level: fheq:6
  appliesTo: "honours degree graduates (section 4 table: Working as a professional veterinary nurse: expectations)"
  addressee: learner
  verbs: ["provide", "act"]
  about: "advocacy, advice and well-being (honours degree)"
  themes: [none]
  domain: subject-skill
  award: ["bachelor's with honours"]
  gradeOf: none
  paraphrase: "Graduates of a honours degree should be able to advise clients and advocate for them and the patient where fitting, mindful of their own mental and physical health, as the minimum for the award."
  quote: full   # the issuer's statement is in `source` (D-std-0014)
  audience: both
  subjects: inherited
- id: qaa/veterinary-nursing-2024/4.2.b41.foundation
  locator: { number: "4.2.b41.foundation", headingPath: ["Benchmark standards", "Introduction"] }
  span: { start: 51984, end: 52157 }
  source: "Demonstrate empathy with patients and clients and act as an advocate for them, when appropriate, with an appreciation for their own mental and physical health and well-being"
  stem: "4.2"
  statementType: threshold
  rung: threshold
  force: threshold
  level: fheq:5
  appliesTo: "foundation degree graduates (section 4 table: Working as a professional veterinary nurse: expectations)"
  addressee: learner
  verbs: ["demonstrate", "act"]
  about: "advocacy, advice and well-being (foundation degree)"
  themes: [none]
  domain: subject-skill
  award: ["foundation degree"]
  gradeOf: none
  paraphrase: "Graduates of a foundation degree should be able to show empathy with patients and clients and advocate for them where fitting, mindful of their own mental and physical health, as the minimum for the award."
  quote: full   # the issuer's statement is in `source` (D-std-0014)
  audience: both
  subjects: inherited
- id: qaa/veterinary-nursing-2024/4.2.b41.masters
  locator: { number: "4.2.b41.masters", headingPath: ["Benchmark standards", "Introduction"] }
  span: { start: 52330, end: 52542 }
  source: "Awareness of factors that impact on mental and physical health and well-being. Implement strategies to support others to provide advice to clients and act as an advocate for them and the patient, when appropriate"
  stem: "4.2"
  statementType: threshold
  rung: threshold
  force: threshold
  level: fheq:7
  appliesTo: "master's degree graduates (section 4 table: Working as a professional veterinary nurse: expectations)"
  addressee: learner
  verbs: ["implement", "support", "provide", "act"]
  about: "advocacy, advice and well-being (master's degree)"
  themes: [none]
  domain: subject-skill
  award: ["master's"]
  gradeOf: none
  paraphrase: "Graduates of a master's degree should be able to be aware of what affects mental and physical health, and put in place strategies that help others advise clients and advocate for them and the patient, as the minimum for the award."
  quote: full   # the issuer's statement is in `source` (D-std-0014)
  audience: both
  subjects: inherited
- id: qaa/veterinary-nursing-2024/4.2.b42
  locator: { number: "4.2.b42", headingPath: ["Benchmark standards", "Introduction"] }
  span: { start: 52659, end: 52774 }
  source: "Plan and execute research and development work, including the development of an evidence base for clinical practice"
  stem: "4.2"
  statementType: threshold
  rung: threshold
  force: threshold
  level: fheq:6
  appliesTo: "honours degree graduates (section 4 table: Working as a professional veterinary nurse: expectations)"
  addressee: learner
  verbs: ["plan", "execute"]
  about: "research and the evidence base (honours degree)"
  themes: [none]
  domain: subject-skill
  award: ["bachelor's with honours"]
  gradeOf: none
  paraphrase: "Graduates of a honours degree should be able to plan and carry out research and development, including building an evidence base for clinical practice, as the minimum for the award."
  quote: full   # the issuer's statement is in `source` (D-std-0014)
  audience: both
  subjects: inherited
- id: qaa/veterinary-nursing-2024/4.2.b42.foundation
  locator: { number: "4.2.b42.foundation", headingPath: ["Benchmark standards", "Introduction"] }
  span: { start: 52543, end: 52657 }
  source: "Participate in the development of an evidence base in clinical practice and understand the importance of such work"
  stem: "4.2"
  statementType: threshold
  rung: threshold
  force: threshold
  level: fheq:5
  appliesTo: "foundation degree graduates (section 4 table: Working as a professional veterinary nurse: expectations)"
  addressee: learner
  verbs: ["participate", "understand"]
  about: "research and the evidence base (foundation degree)"
  themes: [none]
  domain: subject-skill
  award: ["foundation degree"]
  gradeOf: none
  paraphrase: "Graduates of a foundation degree should be able to take part in building an evidence base in clinical practice and understand why that work matters, as the minimum for the award."
  quote: full   # the issuer's statement is in `source` (D-std-0014)
  audience: both
  subjects: inherited
- id: qaa/veterinary-nursing-2024/4.2.b42.masters
  locator: { number: "4.2.b42.masters", headingPath: ["Benchmark standards", "Introduction"] }
  span: { start: 52776, end: 52934 }
  source: "Propose new approaches to the continual development of evidence- based Veterinary Nursing. Evaluate the impact of their research and dissemination of concepts"
  stem: "4.2"
  statementType: threshold
  rung: threshold
  force: threshold
  level: fheq:7
  appliesTo: "master's degree graduates (section 4 table: Working as a professional veterinary nurse: expectations)"
  addressee: learner
  verbs: ["propose", "evaluate"]
  about: "research and the evidence base (master's degree)"
  themes: [none]
  domain: subject-skill
  award: ["master's"]
  gradeOf: none
  paraphrase: "Graduates of a master's degree should be able to propose new approaches to keep developing evidence-based veterinary nursing and evaluate the impact of their research and of sharing its ideas, as the minimum for the award."
  quote: full   # the issuer's statement is in `source` (D-std-0014)
  audience: both
  subjects: inherited
- id: qaa/veterinary-nursing-2024/4.2.b43
  locator: { number: "4.2.b43", headingPath: ["Benchmark standards", "Introduction"] }
  span: { start: 53033, end: 53129 }
  source: "Adopt and promote equality, diversity and inclusion within the veterinary environment and beyond"
  stem: "4.2"
  statementType: threshold
  rung: threshold
  force: threshold
  level: fheq:6
  appliesTo: "honours degree graduates (section 4 table: Working as a professional veterinary nurse: expectations)"
  addressee: learner
  verbs: ["adopt", "promote"]
  about: "equality, diversity and inclusion in practice (honours degree)"
  themes: [none]
  domain: subject-skill
  award: ["bachelor's with honours"]
  gradeOf: none
  paraphrase: "Graduates of a honours degree should be able to take up and promote equality, diversity and inclusion in the veterinary setting and beyond it, as the minimum for the award."
  quote: full   # the issuer's statement is in `source` (D-std-0014)
  audience: both
  subjects: inherited
- id: qaa/veterinary-nursing-2024/4.2.b43.foundation
  locator: { number: "4.2.b43.foundation", headingPath: ["Benchmark standards", "Introduction"] }
  span: { start: 52935, end: 53031 }
  source: "Adopt and promote equality, diversity and inclusion within the veterinary environment and beyond"
  stem: "4.2"
  statementType: threshold
  rung: threshold
  force: threshold
  level: fheq:5
  appliesTo: "foundation degree graduates (section 4 table: Working as a professional veterinary nurse: expectations)"
  addressee: learner
  verbs: ["adopt", "promote"]
  about: "equality, diversity and inclusion in practice (foundation degree)"
  themes: [none]
  domain: subject-skill
  award: ["foundation degree"]
  gradeOf: none
  paraphrase: "Graduates of a foundation degree should be able to take up and promote equality, diversity and inclusion in the veterinary setting and beyond it, as the minimum for the award."
  quote: full   # the issuer's statement is in `source` (D-std-0014)
  audience: both
  subjects: inherited
- id: qaa/veterinary-nursing-2024/4.2.b43.masters
  locator: { number: "4.2.b43.masters", headingPath: ["Benchmark standards", "Introduction"] }
  span: { start: 53131, end: 53227 }
  source: "Adopt and promote equality, diversity and inclusion within the veterinary environment and beyond"
  stem: "4.2"
  statementType: threshold
  rung: threshold
  force: threshold
  level: fheq:7
  appliesTo: "master's degree graduates (section 4 table: Working as a professional veterinary nurse: expectations)"
  addressee: learner
  verbs: ["adopt", "promote"]
  about: "equality, diversity and inclusion in practice (master's degree)"
  themes: [none]
  domain: subject-skill
  award: ["master's"]
  gradeOf: none
  paraphrase: "Graduates of a master's degree should be able to take up and promote equality, diversity and inclusion in the veterinary setting and beyond it, as the minimum for the award."
  quote: full   # the issuer's statement is in `source` (D-std-0014)
  audience: both
  subjects: inherited
- id: qaa/veterinary-nursing-2024/4.2.b44
  locator: { number: "4.2.b44", headingPath: ["Benchmark standards", "Introduction"] }
  span: { start: 53374, end: 53542 }
  source: "Critically evaluate own skills and recognise and engage with the opportunities to develop and acquire new competences in line with professional development requirements"
  stem: "4.2"
  statementType: threshold
  rung: threshold
  force: threshold
  level: fheq:6
  appliesTo: "honours degree graduates (section 4 table: Working as a professional veterinary nurse: expectations)"
  addressee: learner
  verbs: ["evaluate", "recognise", "engage"]
  about: "professional development (honours degree)"
  themes: [none]
  domain: generic-skill
  award: ["bachelor's with honours"]
  gradeOf: none
  paraphrase: "Graduates of a honours degree should be able to critically evaluate their own skills and see and take chances to develop and gain new competences as professional development requires, as the minimum for the award."
  quote: full   # the issuer's statement is in `source` (D-std-0014)
  audience: both
  subjects: inherited
- id: qaa/veterinary-nursing-2024/4.2.b44.foundation
  locator: { number: "4.2.b44.foundation", headingPath: ["Benchmark standards", "Introduction"] }
  span: { start: 53229, end: 53372 }
  source: "Reflect on own skills and recognise the opportunities to develop and acquire new competences in line with professional development requirements"
  stem: "4.2"
  statementType: threshold
  rung: threshold
  force: threshold
  level: fheq:5
  appliesTo: "foundation degree graduates (section 4 table: Working as a professional veterinary nurse: expectations)"
  addressee: learner
  verbs: ["reflect", "recognise"]
  about: "professional development (foundation degree)"
  themes: [none]
  domain: generic-skill
  award: ["foundation degree"]
  gradeOf: none
  paraphrase: "Graduates of a foundation degree should be able to reflect on their own skills and see chances to develop and gain new competences as professional development requires, as the minimum for the award."
  quote: full   # the issuer's statement is in `source` (D-std-0014)
  audience: both
  subjects: inherited
- id: qaa/veterinary-nursing-2024/4.2.b44.masters
  locator: { number: "4.2.b44.masters", headingPath: ["Benchmark standards", "Introduction"] }
  span: { start: 53543, end: 53707 }
  source: "Support and lead colleagues to recognise and engage with the opportunities to develop and acquire new competences in line with professional development requirements"
  stem: "4.2"
  statementType: threshold
  rung: threshold
  force: threshold
  level: fheq:7
  appliesTo: "master's degree graduates (section 4 table: Working as a professional veterinary nurse: expectations)"
  addressee: learner
  verbs: ["support", "lead", "recognise", "engage"]
  about: "professional development (master's degree)"
  themes: [none]
  domain: generic-skill
  award: ["master's"]
  gradeOf: none
  paraphrase: "Graduates of a master's degree should be able to support and lead colleagues in seeing and taking chances to develop and gain new competences as professional development requires, as the minimum for the award."
  quote: full   # the issuer's statement is in `source` (D-std-0014)
  audience: both
  subjects: inherited
```

### S4a Audience versions
<!-- label: both; status: drafted; basis: primary. forPractitioner: for the programme designer or teacher. forBeneficiary: for the student, second person, naming no issuer. author-agent-written: instructions to an AI agent writing about the statement (a course document, a handbook, an outcome, a report). author-agent-dialogue: instructions to an AI agent using the statement in conversation (with a student, a teacher or a programme team). Written fresh from the held text alone (benchmark rule 6; Abbott, 15:42). -->
```yaml
- statement: qaa/veterinary-nursing-2024/1.4
  forPractitioner: { text: "Practice in the UK must rest on RCVS registration, a commitment to its code, accountability and regular reflective CPD; the course is where students first meet these professional obligations.", rewrite: light, force: must, status: drafted }
  forBeneficiary: { text: "To work as a veterinary nurse in the UK you must join the RCVS register, keep to its code of conduct, answer for what you do and keep your skills current through professional development that you reflect on.", rewrite: full, force: must, status: drafted }
  author-agent-written: "Present this as a condition of professional practice that the statement reports (a must, set by the RCVS, not by the statement), holding for anyone entering practice after any of the three awards. Cite it as QAA (2024), Veterinary Nursing Subject Benchmark Statement, para 1.4. Do not claim that the degree alone confers registration or that the statement itself imposes this duty. Set it beside 1.7 and 2.2 on the Day One requirements and qaa/fheq-2024/4.12.b8 and 4.15.b9.1 on personal responsibility."
  author-agent-dialogue: "Raise it when a student asks what they need beyond the degree to work as a veterinary nurse. Put it plainly, in the second person to a student, and as a teaching and assessment question to staff. Ask: \"What do you understand about registering with the RCVS and keeping up your professional development once you qualify?\" Avoid reading the paragraph aloud at length or making it sound stricter than it is."
- statement: qaa/veterinary-nursing-2024/1.6
  forPractitioner: { text: "Design the course as science-based and strongly vocational so that it should leave graduates ready to register as veterinary nurses on the day they graduate.", rewrite: light, force: should, status: drafted }
  forBeneficiary: { text: "not-applicable: a duty on the course and its provider; the student meets its effect, not a standard to reach", rewrite: full, force: should, status: drafted }
  author-agent-written: "Present this as a course aim with the force of should, holding for courses at all three awards. Cite it as QAA (2024), Veterinary Nursing Subject Benchmark Statement, para 1.6. Do not claim that every award listed leads to registration or that the statement sets accreditation rules. Set it beside 1.7, 2.2 and 2.5 on accreditation and placement, and the RCVS requirements recorded in SB5."
  author-agent-dialogue: "Raise it when a programme team asks what the overall purpose of a veterinary nursing course should be. Put it to the programme team as a design question; with a student, say only what it means for their course. Ask: \"How does your course leave graduates ready to register at the point they finish?\" Avoid presenting this duty to a student as something they must do, or reading the paragraph aloud at length."
- statement: qaa/veterinary-nursing-2024/1.7
  forPractitioner: { text: "Build an accredited licence to practise course so that students should be able to gain and evidence the Day One Competences, Skills and Professional Behaviours; the RCVS sets these as the minimum for joining its register.", rewrite: light, force: should, status: drafted }
  forBeneficiary: { text: "Your course should be set up so that you can gain and show the Day One Competences, the Day One Skills and the professional behaviours; the RCVS requires you to meet them before you can join its register.", rewrite: full, force: should, status: drafted }
  author-agent-written: "Present this as a course design expectation (should) resting on an RCVS minimum (must), holding for licence to practise courses. Cite it as QAA (2024), Veterinary Nursing Subject Benchmark Statement, para 1.7. Do not claim that the statement defines the Day One requirements; they are the RCVS's and are recorded as a separate document (SB5). Set it beside 2.2, 2.5, 2.11 and 1.14 on the same requirements."
  author-agent-dialogue: "Raise it when a student or team asks what the Day One requirements are and how the course covers them. Put it plainly, in the second person to a student, and as a teaching and assessment question to staff. Ask: \"Which of the Day One Competences and Skills have you already evidenced, and which are still to come?\" Avoid reading the paragraph aloud at length or making it sound stricter than it is."
- statement: qaa/veterinary-nursing-2024/1.12
  forPractitioner: { text: "Design the course, placements included, proactively and flexibly so that access to learning should be equitable; staff and students share the work of promoting equity and challenging stereotypes.", rewrite: light, force: should, status: drafted }
  forBeneficiary: { text: "not-applicable: a duty on the course and its provider; the student meets its effect, not a standard to reach", rewrite: full, force: should, status: drafted }
  author-agent-written: "Present this as a provider duty (should) under the equality, diversity and inclusion theme, holding for courses at all three awards. Cite it as QAA (2024), Veterinary Nursing Subject Benchmark Statement, para 1.12. Do not claim that it sets a legal standard; it is a sector expectation. Set it beside 1.13, the inclusion rows of the generic skills table (4.2.b8 to 4.2.b10) and 4.2.b43."
  author-agent-dialogue: "Raise it when a programme team reviews whether its course and placements are inclusive by design. Put it to the programme team as a design question; with a student, say only what it means for their course. Ask: \"Where might a student meet a barrier in your course or placements, and how is the design meant to remove it?\" Avoid presenting this duty to a student as something they must do, or reading the paragraph aloud at length."
- statement: qaa/veterinary-nursing-2024/1.13
  forPractitioner: { text: "Design the programme so that it should foster openness and each student's responsibility for equity and inclusion, framed as a professional duty in teamwork and in educating owners and the public.", rewrite: light, force: should, status: drafted }
  forBeneficiary: { text: "Your course should help you see equity and inclusion as part of your own professional responsibility, in your team and when you advise animal owners and the public.", rewrite: full, force: should, status: drafted }
  author-agent-written: "Present this as an expectation (should) on programme design with a student-facing aim, holding for all three awards. Cite it as QAA (2024), Veterinary Nursing Subject Benchmark Statement, para 1.13. Do not claim that it is a competence assessed in its own right; the tables carry the assessed forms. Set it beside 1.12, 4.2.b8 to 4.2.b10 and 4.2.b43."
  author-agent-dialogue: "Raise it when a student asks why inclusion matters in a clinical role, or a team plans how to teach it. Put it plainly, in the second person to a student, and as a teaching and assessment question to staff. Ask: \"Can you think of a time at work or on placement when you made sure a client or colleague was treated fairly?\" Avoid reading the paragraph aloud at length or making it sound stricter than it is."
- statement: qaa/veterinary-nursing-2024/1.14
  forPractitioner: { text: "Make every stage accessible: as a minimum it should meet regulatory requirements and should cover information before application through to after graduation, including the curriculum, learning spaces and adjustable assessment.", rewrite: light, force: should, status: drafted }
  forBeneficiary: { text: "not-applicable: a duty on the course and its provider; the student meets its effect, not a standard to reach", rewrite: full, force: should, status: drafted }
  author-agent-written: "Present this as a provider duty (should) under the accessibility theme, holding for courses at all three awards. Cite it as QAA (2024), Veterinary Nursing Subject Benchmark Statement, para 1.14. Do not claim that the listed examples are a complete or required set; the paragraph says it may include them. Set it beside 1.15, 1.16 and 3.15 on adjusted assessment."
  author-agent-dialogue: "Raise it when a team checks accessibility across the student journey. Put it to the programme team as a design question; with a student, say only what it means for their course. Ask: \"Which stage of your course, from application to graduation, is hardest for a disabled student to use, and what changes would help?\" Avoid presenting this duty to a student as something they must do, or reading the paragraph aloud at length."
- statement: qaa/veterinary-nursing-2024/1.15
  forPractitioner: { text: "Use proactive, innovative design for courses, modules, teaching and assessment that should build in flexibility and inclusion from the start and avoid barriers for students with specific learning differences.", rewrite: light, force: should, status: drafted }
  forBeneficiary: { text: "not-applicable: a duty on the course and its provider; the student meets its effect, not a standard to reach", rewrite: full, force: should, status: drafted }
  author-agent-written: "Present this as a provider duty (should) under the accessibility theme, holding for courses at all three awards. Cite it as QAA (2024), Veterinary Nursing Subject Benchmark Statement, para 1.15. Do not claim that it requires any particular method. Set it beside 1.14, 1.16 and 3.15."
  author-agent-dialogue: "Raise it when a team designs or revises a module or assessment. Put it to the programme team as a design question; with a student, say only what it means for their course. Ask: \"If a student with dyslexia took this module, where would they first struggle, and what would you change?\" Avoid presenting this duty to a student as something they must do, or reading the paragraph aloud at length."
- statement: qaa/veterinary-nursing-2024/1.16
  forPractitioner: { text: "Accessibility should extend to placements, so every student has the same workplace learning opportunities, and to digital provision that is inclusive and free of discrimination.", rewrite: light, force: should, status: drafted }
  forBeneficiary: { text: "not-applicable: a duty on the course and its provider; the student meets its effect, not a standard to reach", rewrite: full, force: should, status: drafted }
  author-agent-written: "Present this as a provider duty (should) under the accessibility theme, holding for courses at all three awards. Cite it as QAA (2024), Veterinary Nursing Subject Benchmark Statement, para 1.16. Do not claim that it guarantees any particular placement. Set it beside 1.14, 1.15, 2.5 and 2.11 on placements."
  author-agent-dialogue: "Raise it when a team plans placements or digital learning. Put it to the programme team as a design question; with a student, say only what it means for their course. Ask: \"Do all your students get the same quality of placement and digital access, and how do you know?\" Avoid presenting this duty to a student as something they must do, or reading the paragraph aloud at length."
- statement: qaa/veterinary-nursing-2024/1.17
  forPractitioner: { text: "Weave ethics, responsibility and sustainability through the curriculum, as the statement expects, drawing if useful on the UN principles for responsible management education so students can help sustain the profession.", rewrite: light, force: describes, status: drafted }
  forBeneficiary: { text: "not-applicable: a duty on the course and its provider; the student meets its effect, not a standard to reach", rewrite: full, force: describes, status: drafted }
  author-agent-written: "Present this as an expectation on the curriculum stated as \"an expectation\", outside the five modal words (recorded as describes), holding for courses at all three awards. Cite it as QAA (2024), Veterinary Nursing Subject Benchmark Statement, para 1.17. Do not claim that it is a must or a should. Set it beside 1.18, the sustainability row 4.2.b11 and the ESD guidance std:doc:qaa-advancehe-esd-2021-guidance."
  author-agent-dialogue: "Raise it when a team asks how sustainability should feature in a veterinary nursing course. Put it to the programme team as a design question; with a student, say only what it means for their course. Ask: \"Where in your curriculum do students meet the ethics and sustainability of veterinary work?\" Avoid presenting this duty to a student as something they must do, or reading the paragraph aloud at length."
- statement: qaa/veterinary-nursing-2024/1.18
  forPractitioner: { text: "The curriculum should cover economic, social and environmental sustainability management, and should equip students to take on climate challenges and build climate solutions into veterinary processes.", rewrite: light, force: should, status: drafted }
  forBeneficiary: { text: "You should leave your course ready to take on climate challenges and to build greener ways of working into everyday veterinary tasks.", rewrite: full, force: should, status: drafted }
  author-agent-written: "Present this as an expectation (should) under the sustainability theme, with a student-facing aim, holding for all three awards. Cite it as QAA (2024), Veterinary Nursing Subject Benchmark Statement, para 1.18. Do not claim that it sets targets for practices or students. Set it beside 1.17, 1.19's example topics and 4.2.b11."
  author-agent-dialogue: "Raise it when a student asks what sustainability has to do with veterinary nursing. Put it plainly, in the second person to a student, and as a teaching and assessment question to staff. Ask: \"What is one change in a clinic you know that would cut waste or emissions without risking patient care?\" Avoid reading the paragraph aloud at length or making it sound stricter than it is."
- statement: qaa/veterinary-nursing-2024/1.22
  forPractitioner: { text: "Design enterprise and entrepreneurship education with employers, professional bodies and service users, as it should be, and encourage group work that develops teamwork, negotiation and leadership.", rewrite: light, force: should, status: drafted }
  forBeneficiary: { text: "not-applicable: a duty on the course and its provider; the student meets its effect, not a standard to reach", rewrite: full, force: should, status: drafted }
  author-agent-written: "Present this as a provider duty (should) under the enterprise theme, holding for courses at all three awards. Cite it as QAA (2024), Veterinary Nursing Subject Benchmark Statement, para 1.22. Do not claim that it requires any particular enterprise module. Set it beside 1.20, 1.21, the teamwork rows 4.2.b4 and 4.2.b23, and std:doc:qaa-enterprise-2018-guidance."
  author-agent-dialogue: "Raise it when a team plans employability or enterprise content. Put it to the programme team as a design question; with a student, say only what it means for their course. Ask: \"Which employers or service users helped shape your enterprise teaching, and what did they change?\" Avoid presenting this duty to a student as something they must do, or reading the paragraph aloud at length."
- statement: qaa/veterinary-nursing-2024/2.1.b1
  forPractitioner: { text: "Include communication in the curriculum; it is one of the subject areas a course should cover at the least.", rewrite: light, force: should, status: drafted }
  forBeneficiary: { text: "not-applicable: a minimum of course content set for the course, not an outcome for the student", rewrite: full, force: should, status: drafted }
  author-agent-written: "Present this as one of the minimum subject areas a course should include (communication), a duty on the course rather than a student outcome, holding for every award the statement covers. Cite it as QAA (2024), Veterinary Nursing Subject Benchmark Statement, para 2.1. Do not claim that it sets the depth, hours or level of the topic, or that the list is complete. Set it beside 3.1, the content areas the course aims to develop, and the outcomes in the four section 4 tables."
  author-agent-dialogue: "Raise it when a programme team checks its curriculum against the minimum content. Put it to the programme team as a design question; with a student, say only what it means for their course. Ask: \"Where in your course is communication taught and assessed, and at what depth for each award?\" Avoid presenting this duty to a student as something they must do, or reading the paragraph aloud at length."
- statement: qaa/veterinary-nursing-2024/2.1.b2
  forPractitioner: { text: "Include animal physiology in the curriculum; it is one of the subject areas a course should cover at the least.", rewrite: light, force: should, status: drafted }
  forBeneficiary: { text: "not-applicable: a minimum of course content set for the course, not an outcome for the student", rewrite: full, force: should, status: drafted }
  author-agent-written: "Present this as one of the minimum subject areas a course should include (animal physiology), a duty on the course rather than a student outcome, holding for every award the statement covers. Cite it as QAA (2024), Veterinary Nursing Subject Benchmark Statement, para 2.1. Do not claim that it sets the depth, hours or level of the topic, or that the list is complete. Set it beside 3.1, the content areas the course aims to develop, and the outcomes in the four section 4 tables."
  author-agent-dialogue: "Raise it when a programme team checks its curriculum against the minimum content. Put it to the programme team as a design question; with a student, say only what it means for their course. Ask: \"Where in your course is animal physiology taught and assessed, and at what depth for each award?\" Avoid presenting this duty to a student as something they must do, or reading the paragraph aloud at length."
- statement: qaa/veterinary-nursing-2024/2.1.b3
  forPractitioner: { text: "Include husbandry in the curriculum; it is one of the subject areas a course should cover at the least.", rewrite: light, force: should, status: drafted }
  forBeneficiary: { text: "not-applicable: a minimum of course content set for the course, not an outcome for the student", rewrite: full, force: should, status: drafted }
  author-agent-written: "Present this as one of the minimum subject areas a course should include (husbandry), a duty on the course rather than a student outcome, holding for every award the statement covers. Cite it as QAA (2024), Veterinary Nursing Subject Benchmark Statement, para 2.1. Do not claim that it sets the depth, hours or level of the topic, or that the list is complete. Set it beside 3.1, the content areas the course aims to develop, and the outcomes in the four section 4 tables."
  author-agent-dialogue: "Raise it when a programme team checks its curriculum against the minimum content. Put it to the programme team as a design question; with a student, say only what it means for their course. Ask: \"Where in your course is husbandry taught and assessed, and at what depth for each award?\" Avoid presenting this duty to a student as something they must do, or reading the paragraph aloud at length."
- statement: qaa/veterinary-nursing-2024/2.1.b4
  forPractitioner: { text: "Include welfare and behaviour in the curriculum; it is one of the subject areas a course should cover at the least.", rewrite: light, force: should, status: drafted }
  forBeneficiary: { text: "not-applicable: a minimum of course content set for the course, not an outcome for the student", rewrite: full, force: should, status: drafted }
  author-agent-written: "Present this as one of the minimum subject areas a course should include (welfare and behaviour), a duty on the course rather than a student outcome, holding for every award the statement covers. Cite it as QAA (2024), Veterinary Nursing Subject Benchmark Statement, para 2.1. Do not claim that it sets the depth, hours or level of the topic, or that the list is complete. Set it beside 3.1, the content areas the course aims to develop, and the outcomes in the four section 4 tables."
  author-agent-dialogue: "Raise it when a programme team checks its curriculum against the minimum content. Put it to the programme team as a design question; with a student, say only what it means for their course. Ask: \"Where in your course is welfare and behaviour taught and assessed, and at what depth for each award?\" Avoid presenting this duty to a student as something they must do, or reading the paragraph aloud at length."
- statement: qaa/veterinary-nursing-2024/2.1.b5
  forPractitioner: { text: "Include infection control in the curriculum; it is one of the subject areas a course should cover at the least.", rewrite: light, force: should, status: drafted }
  forBeneficiary: { text: "not-applicable: a minimum of course content set for the course, not an outcome for the student", rewrite: full, force: should, status: drafted }
  author-agent-written: "Present this as one of the minimum subject areas a course should include (infection control), a duty on the course rather than a student outcome, holding for every award the statement covers. Cite it as QAA (2024), Veterinary Nursing Subject Benchmark Statement, para 2.1. Do not claim that it sets the depth, hours or level of the topic, or that the list is complete. Set it beside 3.1, the content areas the course aims to develop, and the outcomes in the four section 4 tables."
  author-agent-dialogue: "Raise it when a programme team checks its curriculum against the minimum content. Put it to the programme team as a design question; with a student, say only what it means for their course. Ask: \"Where in your course is infection control taught and assessed, and at what depth for each award?\" Avoid presenting this duty to a student as something they must do, or reading the paragraph aloud at length."
- statement: qaa/veterinary-nursing-2024/2.1.b6
  forPractitioner: { text: "Include anaesthesia in the curriculum; it is one of the subject areas a course should cover at the least.", rewrite: light, force: should, status: drafted }
  forBeneficiary: { text: "not-applicable: a minimum of course content set for the course, not an outcome for the student", rewrite: full, force: should, status: drafted }
  author-agent-written: "Present this as one of the minimum subject areas a course should include (anaesthesia), a duty on the course rather than a student outcome, holding for every award the statement covers. Cite it as QAA (2024), Veterinary Nursing Subject Benchmark Statement, para 2.1. Do not claim that it sets the depth, hours or level of the topic, or that the list is complete. Set it beside 3.1, the content areas the course aims to develop, and the outcomes in the four section 4 tables."
  author-agent-dialogue: "Raise it when a programme team checks its curriculum against the minimum content. Put it to the programme team as a design question; with a student, say only what it means for their course. Ask: \"Where in your course is anaesthesia taught and assessed, and at what depth for each award?\" Avoid presenting this duty to a student as something they must do, or reading the paragraph aloud at length."
- statement: qaa/veterinary-nursing-2024/2.1.b7
  forPractitioner: { text: "Include surgical nursing and theatre practice in the curriculum; it is one of the subject areas a course should cover at the least.", rewrite: light, force: should, status: drafted }
  forBeneficiary: { text: "not-applicable: a minimum of course content set for the course, not an outcome for the student", rewrite: full, force: should, status: drafted }
  author-agent-written: "Present this as one of the minimum subject areas a course should include (surgical nursing and theatre practice), a duty on the course rather than a student outcome, holding for every award the statement covers. Cite it as QAA (2024), Veterinary Nursing Subject Benchmark Statement, para 2.1. Do not claim that it sets the depth, hours or level of the topic, or that the list is complete. Set it beside 3.1, the content areas the course aims to develop, and the outcomes in the four section 4 tables."
  author-agent-dialogue: "Raise it when a programme team checks its curriculum against the minimum content. Put it to the programme team as a design question; with a student, say only what it means for their course. Ask: \"Where in your course is surgical nursing and theatre practice taught and assessed, and at what depth for each award?\" Avoid presenting this duty to a student as something they must do, or reading the paragraph aloud at length."
- statement: qaa/veterinary-nursing-2024/2.1.b8
  forPractitioner: { text: "Include pharmacology in the curriculum; it is one of the subject areas a course should cover at the least.", rewrite: light, force: should, status: drafted }
  forBeneficiary: { text: "not-applicable: a minimum of course content set for the course, not an outcome for the student", rewrite: full, force: should, status: drafted }
  author-agent-written: "Present this as one of the minimum subject areas a course should include (pharmacology), a duty on the course rather than a student outcome, holding for every award the statement covers. Cite it as QAA (2024), Veterinary Nursing Subject Benchmark Statement, para 2.1. Do not claim that it sets the depth, hours or level of the topic, or that the list is complete. Set it beside 3.1, the content areas the course aims to develop, and the outcomes in the four section 4 tables."
  author-agent-dialogue: "Raise it when a programme team checks its curriculum against the minimum content. Put it to the programme team as a design question; with a student, say only what it means for their course. Ask: \"Where in your course is pharmacology taught and assessed, and at what depth for each award?\" Avoid presenting this duty to a student as something they must do, or reading the paragraph aloud at length."
- statement: qaa/veterinary-nursing-2024/2.1.b9
  forPractitioner: { text: "Include laboratory and diagnostic techniques in the curriculum; it is one of the subject areas a course should cover at the least.", rewrite: light, force: should, status: drafted }
  forBeneficiary: { text: "not-applicable: a minimum of course content set for the course, not an outcome for the student", rewrite: full, force: should, status: drafted }
  author-agent-written: "Present this as one of the minimum subject areas a course should include (laboratory and diagnostic techniques), a duty on the course rather than a student outcome, holding for every award the statement covers. Cite it as QAA (2024), Veterinary Nursing Subject Benchmark Statement, para 2.1. Do not claim that it sets the depth, hours or level of the topic, or that the list is complete. Set it beside 3.1, the content areas the course aims to develop, and the outcomes in the four section 4 tables."
  author-agent-dialogue: "Raise it when a programme team checks its curriculum against the minimum content. Put it to the programme team as a design question; with a student, say only what it means for their course. Ask: \"Where in your course is laboratory and diagnostic techniques taught and assessed, and at what depth for each award?\" Avoid presenting this duty to a student as something they must do, or reading the paragraph aloud at length."
- statement: qaa/veterinary-nursing-2024/2.1.b10
  forPractitioner: { text: "Include ethics in the curriculum; it is one of the subject areas a course should cover at the least.", rewrite: light, force: should, status: drafted }
  forBeneficiary: { text: "not-applicable: a minimum of course content set for the course, not an outcome for the student", rewrite: full, force: should, status: drafted }
  author-agent-written: "Present this as one of the minimum subject areas a course should include (ethics), a duty on the course rather than a student outcome, holding for every award the statement covers. Cite it as QAA (2024), Veterinary Nursing Subject Benchmark Statement, para 2.1. Do not claim that it sets the depth, hours or level of the topic, or that the list is complete. Set it beside 3.1, the content areas the course aims to develop, and the outcomes in the four section 4 tables."
  author-agent-dialogue: "Raise it when a programme team checks its curriculum against the minimum content. Put it to the programme team as a design question; with a student, say only what it means for their course. Ask: \"Where in your course is ethics taught and assessed, and at what depth for each award?\" Avoid presenting this duty to a student as something they must do, or reading the paragraph aloud at length."
- statement: qaa/veterinary-nursing-2024/2.1.b11
  forPractitioner: { text: "Include principles of evidence-based practice in the curriculum; it is one of the subject areas a course should cover at the least.", rewrite: light, force: should, status: drafted }
  forBeneficiary: { text: "not-applicable: a minimum of course content set for the course, not an outcome for the student", rewrite: full, force: should, status: drafted }
  author-agent-written: "Present this as one of the minimum subject areas a course should include (principles of evidence-based practice), a duty on the course rather than a student outcome, holding for every award the statement covers. Cite it as QAA (2024), Veterinary Nursing Subject Benchmark Statement, para 2.1. Do not claim that it sets the depth, hours or level of the topic, or that the list is complete. Set it beside 3.1, the content areas the course aims to develop, and the outcomes in the four section 4 tables."
  author-agent-dialogue: "Raise it when a programme team checks its curriculum against the minimum content. Put it to the programme team as a design question; with a student, say only what it means for their course. Ask: \"Where in your course is principles of evidence-based practice taught and assessed, and at what depth for each award?\" Avoid presenting this duty to a student as something they must do, or reading the paragraph aloud at length."
- statement: qaa/veterinary-nursing-2024/2.2
  forPractitioner: { text: "For RCVS accreditation, a course is required to give every graduate the chance to meet the Day One Competences, Skills and Professional Behaviours through the subject areas it teaches and assesses.", rewrite: light, force: must, status: drafted }
  forBeneficiary: { text: "not-applicable: a condition on the course's accreditation; the student-facing point is in 1.7", rewrite: full, force: must, status: drafted }
  author-agent-written: "Present this as a condition of accreditation that the statement reports (required: recorded as must), holding for licence to practise courses. Cite it as QAA (2024), Veterinary Nursing Subject Benchmark Statement, para 2.2. Do not claim that the statement itself accredits courses. Set it beside 1.7, 2.5 and the RCVS requirements in SB5."
  author-agent-dialogue: "Raise it when a team prepares for RCVS accreditation. Put it to the programme team as a design question; with a student, say only what it means for their course. Ask: \"Can you map each Day One requirement to where your course teaches and assesses it?\" Avoid presenting this duty to a student as something they must do, or reading the paragraph aloud at length."
- statement: qaa/veterinary-nursing-2024/2.3
  forPractitioner: { text: "Pitch content by award: foundation degrees will centre on the Day One requirements, honours degrees will add the wider clinical and business side of practice, and master's courses should deepen chosen specialisms.", rewrite: light, force: will, status: drafted }
  forBeneficiary: { text: "not-applicable: a duty on the course and its provider; the student meets its effect, not a standard to reach", rewrite: full, force: will, status: drafted }
  author-agent-written: "Present this as an expectation on content by award (will for foundation and honours, should for master's), holding for each of the three awards in turn. Cite it as QAA (2024), Veterinary Nursing Subject Benchmark Statement, para 2.3. Do not claim that one award's content is required at another. Set it beside 2.1, 3.1 and the three columns of the section 4 tables."
  author-agent-dialogue: "Raise it when a team compares what its foundation, honours and master's courses cover. Put it to the programme team as a design question; with a student, say only what it means for their course. Ask: \"What does your honours course add to the foundation degree, and what does the master's build on?\" Avoid presenting this duty to a student as something they must do, or reading the paragraph aloud at length."
- statement: qaa/veterinary-nursing-2024/2.4
  forPractitioner: { text: "Plan extensive practical teaching: every course will need it to cover the full Day One Skills List.", rewrite: light, force: will, status: drafted }
  forBeneficiary: { text: "not-applicable: a duty on the course and its provider; the student meets its effect, not a standard to reach", rewrite: full, force: will, status: drafted }
  author-agent-written: "Present this as an expectation (will) on how courses teach, holding for courses at all three awards. Cite it as QAA (2024), Veterinary Nursing Subject Benchmark Statement, para 2.4. Do not claim that it fixes any number of hours. Set it beside 2.5, 3.7 and 3.8."
  author-agent-dialogue: "Raise it when a team plans practical classes and skills sessions. Put it to the programme team as a design question; with a student, say only what it means for their course. Ask: \"Which Day One skills get the least hands-on practice in your course now?\" Avoid presenting this duty to a student as something they must do, or reading the paragraph aloud at length."
- statement: qaa/veterinary-nursing-2024/2.5
  forPractitioner: { text: "Build enough clinical placement in approved training practices into the course to let every student complete the RCVS pre-registration hours before graduating, as must be done; use the time to practise and refine the Day One requirements.", rewrite: light, force: must, status: drafted }
  forBeneficiary: { text: "not-applicable: a duty on the course; the student meets its effect through placement", rewrite: full, force: must, status: drafted }
  author-agent-written: "Present this as a provider requirement (must) for licence to practise courses, holding for foundation and honours licence to practise courses. Cite it as QAA (2024), Veterinary Nursing Subject Benchmark Statement, para 2.5. Do not claim a number of hours; the RCVS sets them. Set it beside 2.11, 2.12, 1.16 on equal workplace learning and 3.17."
  author-agent-dialogue: "Raise it when a team plans the placement pattern or a student asks why placement is so long. Put it to the programme team as a design question; with a student, say only what it means for their course. Ask: \"Does your placement plan let every student finish the required hours before the exam board?\" Avoid presenting this duty to a student as something they must do, or reading the paragraph aloud at length."
- statement: qaa/veterinary-nursing-2024/2.6
  forPractitioner: { text: "Plan progression so each level builds towards the threshold; at master's level graduates will add to the knowledge base and show excellence in research and practice, advancing the profession within legal and professional limits.", rewrite: light, force: will, status: drafted }
  forBeneficiary: { text: "If you take a master's in veterinary nursing, you will add to what the profession knows and show excellence in both research and practice.", rewrite: full, force: will, status: drafted }
  author-agent-written: "Present this as an expected outcome (will) for master's holders, inside a paragraph on progression, holding for the master's degree (FHEQ level 7, SCQF level 11). Cite it as QAA (2024), Veterinary Nursing Subject Benchmark Statement, para 2.6. Do not claim that a second-class degree guarantees entry to postgraduate study; entry is for each provider. Set it beside the master's column of the tables, 3.18 and qaa/fheq-2024/4.17.b3 and 4.17.b7 (spine:7)."
  author-agent-dialogue: "Raise it when a student weighs up a master's or asks what it adds. Put it plainly, in the second person to a student, and as a teaching and assessment question to staff. Ask: \"What question from your practice would you most like to research, and how would it change care?\" Avoid reading the paragraph aloud at length or making it sound stricter than it is."
- statement: qaa/veterinary-nursing-2024/2.8
  forPractitioner: { text: "Work in partnership with the RCVS, as the provider should, so that accreditation and quality assurance requirements are met and completing students are eligible to register.", rewrite: light, force: should, status: drafted }
  forBeneficiary: { text: "not-applicable: a duty on the course and its provider; the student meets its effect, not a standard to reach", rewrite: full, force: should, status: drafted }
  author-agent-written: "Present this as a provider duty (should), holding for courses at all three awards. Cite it as QAA (2024), Veterinary Nursing Subject Benchmark Statement, para 2.8. Do not claim that the statement sets RCVS requirements. Set it beside 2.2, 2.9 and SB5."
  author-agent-dialogue: "Raise it when a team plans its accreditation relationship. Put it to the programme team as a design question; with a student, say only what it means for their course. Ask: \"Who in your team owns the RCVS relationship, and how often do you meet?\" Avoid presenting this duty to a student as something they must do, or reading the paragraph aloud at length."
- statement: qaa/veterinary-nursing-2024/2.9
  forPractitioner: { text: "Where you deliver with further education colleges, set up oversight processes, as the statement expects, so that partners meet every academic and RCVS standard.", rewrite: light, force: must, status: drafted }
  forBeneficiary: { text: "not-applicable: a duty on the course and its provider; the student meets its effect, not a standard to reach", rewrite: full, force: must, status: drafted }
  author-agent-written: "Present this as an expectation on providers stated as \"are expected to\", outside the five modal words (recorded as describes), holding for courses delivered in partnership. Cite it as QAA (2024), Veterinary Nursing Subject Benchmark Statement, para 2.9. Do not claim that it is a must or a should. Set it beside 2.8, 2.11 and 2.12."
  author-agent-dialogue: "Raise it when a team delivers through a partner college. Put it to the programme team as a design question; with a student, say only what it means for their course. Ask: \"How do you check that your partner college meets the same RCVS standards you do?\" Avoid presenting this duty to a student as something they must do, or reading the paragraph aloud at length."
- statement: qaa/veterinary-nursing-2024/2.10
  forPractitioner: { text: "Treat students as partners: they should work with the course team, and their views should carry real weight in developing, delivering and reviewing the course.", rewrite: light, force: should, status: drafted }
  forBeneficiary: { text: "You should work with your course team as a partner, and your views should help shape how the course is built, taught and reviewed.", rewrite: full, force: should, status: drafted }
  author-agent-written: "Present this as an expectation (should) on students and course teams, holding for all three awards. Cite it as QAA (2024), Veterinary Nursing Subject Benchmark Statement, para 2.10. Do not claim that students carry responsibility for course quality. Set it beside 2.13 and 1.12."
  author-agent-dialogue: "Raise it when a student asks how they can influence their course. Put it plainly, in the second person to a student, and as a teaching and assessment question to staff. Ask: \"What is one thing about your course you would change, and who could you raise it with?\" Avoid reading the paragraph aloud at length or making it sound stricter than it is."
- statement: qaa/veterinary-nursing-2024/2.11
  forPractitioner: { text: "Put in place a written collaborative agreement, as there should be, between clinical supervisors, the course, placement providers and students, so that placements give the access to cases the Day One requirements need.", rewrite: light, force: should, status: drafted }
  forBeneficiary: { text: "not-applicable: a duty on the course and its provider; the student meets its effect, not a standard to reach", rewrite: full, force: should, status: drafted }
  author-agent-written: "Present this as a provider duty (should); the first sentence is a plain-present norm, holding for licence to practise courses. Cite it as QAA (2024), Veterinary Nursing Subject Benchmark Statement, para 2.11. Do not claim that the statement sets the content of the agreement. Set it beside 2.5, 2.12 and 1.16."
  author-agent-dialogue: "Raise it when a team sets up or reviews placement agreements. Put it to the programme team as a design question; with a student, say only what it means for their course. Ask: \"Does every student on placement have a signed agreement that names their supervisor's role?\" Avoid presenting this duty to a student as something they must do, or reading the paragraph aloud at length."
- statement: qaa/veterinary-nursing-2024/2.12
  forPractitioner: { text: "Approve and monitor training practices, as the course provider should, so placements stay suitable, and train and standardise clinical supervisors.", rewrite: light, force: should, status: drafted }
  forBeneficiary: { text: "not-applicable: a duty on the course and its provider; the student meets its effect, not a standard to reach", rewrite: full, force: should, status: drafted }
  author-agent-written: "Present this as a provider duty (should), holding for licence to practise courses. Cite it as QAA (2024), Veterinary Nursing Subject Benchmark Statement, para 2.12. Do not claim that it replaces RCVS approval rules. Set it beside 2.5, 2.11 and 3.17."
  author-agent-dialogue: "Raise it when a team reviews placement quality. Put it to the programme team as a design question; with a student, say only what it means for their course. Ask: \"When did you last check a training practice, and how are new supervisors prepared?\" Avoid presenting this duty to a student as something they must do, or reading the paragraph aloud at length."
- statement: qaa/veterinary-nursing-2024/2.14
  forPractitioner: { text: "Use external reviewers in periodic review, as providers will, for an outside view of planned changes and to confirm that threshold standards are met and content is right for the subject.", rewrite: light, force: will, status: drafted }
  forBeneficiary: { text: "not-applicable: a duty on the course and its provider; the student meets its effect, not a standard to reach", rewrite: full, force: will, status: drafted }
  author-agent-written: "Present this as a provider expectation (will) about review, holding for courses at all three awards. Cite it as QAA (2024), Veterinary Nursing Subject Benchmark Statement, para 2.14. Do not claim that it sets a review cycle. Set it beside 2.13, 2.15 and 4.1."
  author-agent-dialogue: "Raise it when a team prepares for periodic review. Put it to the programme team as a design question; with a student, say only what it means for their course. Ask: \"Who will act as your external reviewer, and which proposed change do you most want them to test?\" Avoid presenting this duty to a student as something they must do, or reading the paragraph aloud at length."
- statement: qaa/veterinary-nursing-2024/3.3
  forPractitioner: { text: "Prepare small animal graduates to nurse cats, dogs and exotic species proficiently, which the statement anticipates of them.", rewrite: light, force: must, status: drafted }
  forBeneficiary: { text: "On a small animal course you are expected to become skilled at nursing cats, dogs and exotic species.", rewrite: full, force: must, status: drafted }
  author-agent-written: "Present this as an expected outcome stated as \"anticipated\", outside the five modal words (recorded as describes), holding for small animal veterinary nursing degrees. Cite it as QAA (2024), Veterinary Nursing Subject Benchmark Statement, para 3.3. Do not claim that it is a must, or that the species list is complete. Set it beside 3.4, 3.1 and 3.7."
  author-agent-dialogue: "Raise it when a student asks which species their course covers. Put it plainly, in the second person to a student, and as a teaching and assessment question to staff. Ask: \"Which species do you feel least confident nursing, and how could you get more practice?\" Avoid reading the paragraph aloud at length or making it sound stricter than it is."
- statement: qaa/veterinary-nursing-2024/3.4
  forPractitioner: { text: "Prepare equine graduates to nurse horses proficiently, which the statement anticipates of them.", rewrite: light, force: must, status: drafted }
  forBeneficiary: { text: "On an equine course you are expected to become skilled at nursing horses.", rewrite: full, force: must, status: drafted }
  author-agent-written: "Present this as an expected outcome stated as \"anticipated\" (recorded as describes), holding for equine veterinary nursing degrees. Cite it as QAA (2024), Veterinary Nursing Subject Benchmark Statement, para 3.4. Do not claim that it is a must. Set it beside 3.3 and 3.7."
  author-agent-dialogue: "Raise it when a student on an equine route asks what is expected of them. Put it plainly, in the second person to a student, and as a teaching and assessment question to staff. Ask: \"Which equine nursing tasks have you done on placement so far?\" Avoid reading the paragraph aloud at length or making it sound stricter than it is."
- statement: qaa/veterinary-nursing-2024/3.10.b1
  forPractitioner: { text: "Students should develop the ability to work in multidisciplinary teams, with strong communication and professional relationships that hold up under emotional and economic pressure.", rewrite: light, force: should, status: drafted }
  forBeneficiary: { text: "You should become able to work in a team of different professionals, communicate very well and keep professional relationships with clients, colleagues and the public, even when things are emotionally or financially tense.", rewrite: full, force: should, status: drafted }
  author-agent-written: "Present this as an outcome students should develop (should), holding for foundation and honours study. Cite it as QAA (2024), Veterinary Nursing Subject Benchmark Statement, para 3.10. Do not claim that it is a separate threshold from the tables. Set it beside 4.2.b4, 4.2.b23 and 4.2.b27 and qaa/fheq-2024/4.12.b6 (spine:5, strand:communication)."
  author-agent-dialogue: "Raise it when a student reflects on teamwork or a hard client conversation. Put it plainly, in the second person to a student, and as a teaching and assessment question to staff. Ask: \"When did you last keep a conversation professional under pressure, and what helped?\" Avoid reading the paragraph aloud at length or making it sound stricter than it is."
- statement: qaa/veterinary-nursing-2024/3.10.b2
  forPractitioner: { text: "Students should develop the ability to respond to ethical situations appropriately, recognising risk and applying the relevant legislation.", rewrite: light, force: should, status: drafted }
  forBeneficiary: { text: "You should become able to handle situations that need an ethical stance, seeing the risks and using the relevant law when you need to.", rewrite: full, force: should, status: drafted }
  author-agent-written: "Present this as an outcome students should develop (should), holding for foundation and honours study. Cite it as QAA (2024), Veterinary Nursing Subject Benchmark Statement, para 3.10. Do not claim that it is a legal competence. Set it beside 4.2.b24 and 4.2.b36 (spine:5, strand:thinking)."
  author-agent-dialogue: "Raise it when a student meets an ethical dilemma in practice. Put it plainly, in the second person to a student, and as a teaching and assessment question to staff. Ask: \"What made that situation an ethical one, and which law or rule applied?\" Avoid reading the paragraph aloud at length or making it sound stricter than it is."
- statement: qaa/veterinary-nursing-2024/3.10.b3
  forPractitioner: { text: "Students should develop the ability to advocate for patients and clients while always keeping matters confidential.", rewrite: light, force: should, status: drafted }
  forBeneficiary: { text: "You should become able to speak up for patients and clients while always keeping their information confidential.", rewrite: full, force: should, status: drafted }
  author-agent-written: "Present this as an outcome students should develop (should), holding for foundation and honours study. Cite it as QAA (2024), Veterinary Nursing Subject Benchmark Statement, para 3.10. Do not claim that advocacy overrides confidentiality. Set it beside 4.2.b6 and 4.2.b41 (spine:5)."
  author-agent-dialogue: "Raise it when a student asks how to advocate for an animal when the owner disagrees. Put it plainly, in the second person to a student, and as a teaching and assessment question to staff. Ask: \"How would you speak up for this patient without sharing anything you should not?\" Avoid reading the paragraph aloud at length or making it sound stricter than it is."
- statement: qaa/veterinary-nursing-2024/3.10.b4
  forPractitioner: { text: "Students should develop the ability to base decisions on research and current data and to own their actions.", rewrite: light, force: should, status: drafted }
  forBeneficiary: { text: "You should become able to base your decisions on research and up-to-date data and take responsibility for what you do.", rewrite: full, force: should, status: drafted }
  author-agent-written: "Present this as an outcome students should develop (should), holding for foundation and honours study. Cite it as QAA (2024), Veterinary Nursing Subject Benchmark Statement, para 3.10. Do not claim that it is a research competence. Set it beside 4.2.b17 and 4.2.b37 and qaa/fheq-2024/4.12.b8 (spine:5, strand:autonomy)."
  author-agent-dialogue: "Raise it when a student explains a clinical decision. Put it plainly, in the second person to a student, and as a teaching and assessment question to staff. Ask: \"What evidence did you use for that decision, and would you make it again?\" Avoid reading the paragraph aloud at length or making it sound stricter than it is."
- statement: qaa/veterinary-nursing-2024/3.10.b5
  forPractitioner: { text: "Students should develop the ability to reflect on their practice to identify areas for improvement.", rewrite: light, force: should, status: drafted }
  forBeneficiary: { text: "You should become able to keep reflecting on your own practice to see what to improve next.", rewrite: full, force: should, status: drafted }
  author-agent-written: "Present this as an outcome students should develop (should), holding for foundation and honours study. Cite it as QAA (2024), Veterinary Nursing Subject Benchmark Statement, para 3.10. Do not claim that a single reflective log meets it. Set it beside 4.2.b12, 4.2.b31 and 4.2.b44 (spine:5, strand:autonomy)."
  author-agent-dialogue: "Raise it when a student writes a reflection or plans development. Put it plainly, in the second person to a student, and as a teaching and assessment question to staff. Ask: \"What is one thing you would do differently after your last shift, and why?\" Avoid reading the paragraph aloud at length or making it sound stricter than it is."
- statement: qaa/veterinary-nursing-2024/3.13
  forPractitioner: { text: "Teaching should give students communication, IT, teamwork, problem-solving and evidence-based practice skills; where suitable, students will be able to develop research method skills, often through an honours project.", rewrite: light, force: should, status: drafted }
  forBeneficiary: { text: "Your course should help you build skills in communication, IT, teamwork, problem-solving and using evidence, and where it fits you will get the chance to learn research methods.", rewrite: full, force: should, status: drafted }
  author-agent-written: "Present this as an expectation (should) on teaching, with a will on research opportunity, holding for foundation and honours study. Cite it as QAA (2024), Veterinary Nursing Subject Benchmark Statement, para 3.13. Do not claim that every course must include a dissertation; the statement says typically. Set it beside the generic skills table (4.2.b1 to 4.2.b13) and 4.2.b42."
  author-agent-dialogue: "Raise it when a student asks what skills the course builds beyond clinical ones. Put it plainly, in the second person to a student, and as a teaching and assessment question to staff. Ask: \"Which of these skills do you use most on placement, and which least?\" Avoid reading the paragraph aloud at length or making it sound stricter than it is."
- statement: qaa/veterinary-nursing-2024/3.14
  forPractitioner: { text: "Align assessment with outcomes, teaching and competencies, as it should be, and make it discriminate between threshold and higher achievement; methods should prepare students for day one in practice.", rewrite: light, force: should, status: drafted }
  forBeneficiary: { text: "not-applicable: a duty on the course and its provider; the student meets its effect, not a standard to reach", rewrite: full, force: should, status: drafted }
  author-agent-written: "Present this as a provider duty (should) on assessment, holding for courses at all three awards. Cite it as QAA (2024), Veterinary Nursing Subject Benchmark Statement, para 3.14. Do not claim that the statement defines grades above threshold; it points to Annex D (4.2). Set it beside 3.15, 4.1, 4.2 and qaa/fheq-2024 Annex D (SL6)."
  author-agent-dialogue: "Raise it when a team designs an assessment strategy. Put it to the programme team as a design question; with a student, say only what it means for their course. Ask: \"How does this assessment tell a threshold performance apart from a strong one?\" Avoid presenting this duty to a student as something they must do, or reading the paragraph aloud at length."
- statement: qaa/veterinary-nursing-2024/3.15
  forPractitioner: { text: "Make assessment progressive with useful feedback; vary methods so all students can show what they have learned; make tasks authentic where possible; and allow reasonable adjustments, as assessment should, without lowering the competences a registered nurse needs.", rewrite: light, force: should, status: drafted }
  forBeneficiary: { text: "not-applicable: a duty on the course and its provider; the student meets its effect, not a standard to reach", rewrite: full, force: should, status: drafted }
  author-agent-written: "Present this as a provider duty (should) on assessment, holding for courses at all three awards. Cite it as QAA (2024), Veterinary Nursing Subject Benchmark Statement, para 3.15. Do not claim that adjustments may waive a competence. Set it beside 1.14, 1.15, 3.14 and 4.2.b5."
  author-agent-dialogue: "Raise it when a team reviews feedback, variety or adjustments in assessment. Put it to the programme team as a design question; with a student, say only what it means for their course. Ask: \"Could a student with an adjustment still show every competence through this task?\" Avoid presenting this duty to a student as something they must do, or reading the paragraph aloud at length."
- statement: qaa/veterinary-nursing-2024/3.18
  forPractitioner: { text: "At postgraduate level, teaching and assessment should stress applying evidence-based knowledge to complex, unfamiliar problems and should assess research skills.", rewrite: light, force: should, status: drafted }
  forBeneficiary: { text: "not-applicable: a duty on the course and its provider; the student meets its effect, not a standard to reach", rewrite: full, force: should, status: drafted }
  author-agent-written: "Present this as a provider expectation (should) on postgraduate assessment, holding for postgraduate study, including the master's (FHEQ level 7). Cite it as QAA (2024), Veterinary Nursing Subject Benchmark Statement, para 3.18. Do not claim that it applies to foundation or honours courses. Set it beside 2.6, the master's column of the tables and qaa/fheq-2024/4.17.b5 (spine:7)."
  author-agent-dialogue: "Raise it when a postgraduate team designs assessment. Put it to the programme team as a design question; with a student, say only what it means for their course. Ask: \"Where do your students meet a complex, unfamiliar case, and how are their research skills assessed?\" Avoid presenting this duty to a student as something they must do, or reading the paragraph aloud at length."
- statement: qaa/veterinary-nursing-2024/4.2
  forPractitioner: { text: "When judging achievement above threshold for honours, use your own method and refer to Annex D of the Frameworks, as you should, for the shared descriptions of the four classes.", rewrite: light, force: should, status: drafted }
  forBeneficiary: { text: "not-applicable: a duty on the course and its provider; the student meets its effect, not a standard to reach", rewrite: full, force: should, status: drafted }
  author-agent-written: "Present this as a provider expectation (should) pointing to a shared document, holding for the honours degree (FHEQ level 6, SCQF level 10). Cite it as QAA (2024), Veterinary Nursing Subject Benchmark Statement, para 4.2. Do not claim that the statement defines classification bands itself. Set it beside std:doc:qaa-fheq-2024-framework Annex D (qaa/fheq-2024/annex-d/..., SL6) and 3.14."
  author-agent-dialogue: "Raise it when a team sets classification criteria. Put it to the programme team as a design question; with a student, say only what it means for their course. Ask: \"How do your marking criteria line up with the Annex D descriptions of each class?\" Avoid presenting this duty to a student as something they must do, or reading the paragraph aloud at length."
- statement: qaa/veterinary-nursing-2024/4.2.b1
  forPractitioner: { text: "The minimum for a honours degree (FHEQ level 6, SCQF level 10): teach and assess so that every graduate should be able to put forward views and build arguments in speech and writing strong enough to carry a debate with other professionals on the patient's behalf.", rewrite: light, force: threshold, status: drafted }
  forBeneficiary: { text: "As the minimum for your honours degree, you should be able to put forward views and build arguments in speech and writing strong enough to carry a debate with other professionals on the patient's behalf.", rewrite: full, force: threshold, status: drafted }
  author-agent-written: "Treat this as a threshold standard: the minimum a honours degree in veterinary nursing asks at FHEQ level 6, SCQF level 10, on arguing a case for the patient. Cite it as QAA (2024), Veterinary Nursing Subject Benchmark Statement, section 4, table \"Generic skills\", honours degree column. Do not present it as an RCVS or regulatory requirement, or as holding for another award. Set it beside the same row's other columns (4.2.b1.foundation, 4.2.b1.masters) and the framework descriptor qaa/fheq-2024/4.15.b8 and qaa/fqheis-2024/4.16.b7 (spine:6, strand:communication)."
  author-agent-dialogue: "Raise it when an honours student or tutor asks what arguing a case for the patient should look like by the end of the honours degree. Put it plainly: to a student, that by the end you should be able to put forward views and build arguments in speech and writing strong enough to carry a debate with other professionals on the patient's behalf; to staff, as where the course teaches and assesses it. Ask: \"When did you last make the case for a patient to a vet or colleague, and how did it go?\" Avoid reading the table aloud and holding anyone to another award's column as if it were their minimum."
- statement: qaa/veterinary-nursing-2024/4.2.b1.foundation
  forPractitioner: { text: "The minimum for a foundation degree (FHEQ level 5): teach and assess so that every graduate should be able to put forward views and build sound arguments, in speech and on paper.", rewrite: light, force: threshold, status: drafted }
  forBeneficiary: { text: "As the minimum for your foundation degree, you should be able to put forward views and build sound arguments, in speech and on paper.", rewrite: full, force: threshold, status: drafted }
  author-agent-written: "Treat this as a threshold standard: the minimum a foundation degree in veterinary nursing asks at FHEQ level 5, on arguing a case for the patient. Cite it as QAA (2024), Veterinary Nursing Subject Benchmark Statement, section 4, table \"Generic skills\", foundation degree column. Do not present it as an RCVS or regulatory requirement, or as holding for another award. Set it beside the same row's other columns (4.2.b1, 4.2.b1.masters) and the framework descriptor qaa/fheq-2024/4.12.b6 (spine:5, strand:communication)."
  author-agent-dialogue: "Raise it when a foundation degree student or tutor asks what arguing a case for the patient should look like by the end of the foundation degree. Put it plainly: to a student, that by the end you should be able to put forward views and build sound arguments, in speech and on paper; to staff, as where the course teaches and assesses it. Ask: \"When did you last make the case for a patient to a vet or colleague, and how did it go?\" Avoid reading the table aloud and holding anyone to another award's column as if it were their minimum."
- statement: qaa/veterinary-nursing-2024/4.2.b1.masters
  forPractitioner: { text: "The minimum for a master's degree (FHEQ level 7, SCQF level 11): teach and assess so that every graduate should be able to hold their own in spoken and written debate with fellow professionals, speaking up for the patient.", rewrite: light, force: threshold, status: drafted }
  forBeneficiary: { text: "As the minimum for your master's degree, you should be able to hold your own in spoken and written debate with fellow professionals, speaking up for the patient.", rewrite: full, force: threshold, status: drafted }
  author-agent-written: "Treat this as a threshold standard: the minimum a master's degree in veterinary nursing asks at FHEQ level 7, SCQF level 11, on arguing a case for the patient. Cite it as QAA (2024), Veterinary Nursing Subject Benchmark Statement, section 4, table \"Generic skills\", master's degree column. Do not present it as an RCVS or regulatory requirement, or as holding for another award. Set it beside the same row's other columns (4.2.b1.foundation, 4.2.b1) and the framework descriptor qaa/fheq-2024/4.17.b5 (spine:7, strand:communication)."
  author-agent-dialogue: "Raise it when a master's student or tutor asks what arguing a case for the patient should look like by the end of the master's degree. Put it plainly: to a student, that by the end you should be able to hold your own in spoken and written debate with fellow professionals, speaking up for the patient; to staff, as where the course teaches and assesses it. Ask: \"When did you last make the case for a patient to a vet or colleague, and how did it go?\" Avoid reading the table aloud and holding anyone to another award's column as if it were their minimum."
- statement: qaa/veterinary-nursing-2024/4.2.b2
  forPractitioner: { text: "The minimum for a honours degree (FHEQ level 6, SCQF level 10): teach and assess so that every graduate should be able to study on their own and show an analytical way of solving problems.", rewrite: light, force: threshold, status: drafted }
  forBeneficiary: { text: "As the minimum for your honours degree, you should be able to study on your own and show an analytical way of solving problems.", rewrite: full, force: threshold, status: drafted }
  author-agent-written: "Treat this as a threshold standard: the minimum a honours degree in veterinary nursing asks at FHEQ level 6, SCQF level 10, on independent learning and problem-solving. Cite it as QAA (2024), Veterinary Nursing Subject Benchmark Statement, section 4, table \"Generic skills\", honours degree column. Do not present it as an RCVS or regulatory requirement, or as holding for another award. Set it beside the same row's other columns (4.2.b2.foundation, 4.2.b2.masters) and the framework descriptor qaa/fheq-2024/4.15.b9.2 and qaa/fqheis-2024/4.16.b9.2 (spine:6, strand:autonomy)."
  author-agent-dialogue: "Raise it when an honours student or tutor asks what independent learning and problem-solving should look like by the end of the honours degree. Put it plainly: to a student, that by the end you should be able to study on your own and show an analytical way of solving problems; to staff, as where the course teaches and assesses it. Ask: \"What did you last learn on your own, and how did you tackle the problem it helped with?\" Avoid reading the table aloud and holding anyone to another award's column as if it were their minimum."
- statement: qaa/veterinary-nursing-2024/4.2.b2.foundation
  forPractitioner: { text: "The minimum for a foundation degree (FHEQ level 5): teach and assess so that every graduate should be able to study on their own and use problem-solving skills.", rewrite: light, force: threshold, status: drafted }
  forBeneficiary: { text: "As the minimum for your foundation degree, you should be able to study on your own and use problem-solving skills.", rewrite: full, force: threshold, status: drafted }
  author-agent-written: "Treat this as a threshold standard: the minimum a foundation degree in veterinary nursing asks at FHEQ level 5, on independent learning and problem-solving. Cite it as QAA (2024), Veterinary Nursing Subject Benchmark Statement, section 4, table \"Generic skills\", foundation degree column. Do not present it as an RCVS or regulatory requirement, or as holding for another award. Set it beside the same row's other columns (4.2.b2, 4.2.b2.masters) and the framework descriptor qaa/fheq-2024/4.12.b8 (spine:5, strand:autonomy)."
  author-agent-dialogue: "Raise it when a foundation degree student or tutor asks what independent learning and problem-solving should look like by the end of the foundation degree. Put it plainly: to a student, that by the end you should be able to study on your own and use problem-solving skills; to staff, as where the course teaches and assesses it. Ask: \"What did you last learn on your own, and how did you tackle the problem it helped with?\" Avoid reading the table aloud and holding anyone to another award's column as if it were their minimum."
- statement: qaa/veterinary-nursing-2024/4.2.b2.masters
  forPractitioner: { text: "The minimum for a master's degree (FHEQ level 7, SCQF level 11): teach and assess so that every graduate should be able to study on their own and put an analytical way of solving problems into action.", rewrite: light, force: threshold, status: drafted }
  forBeneficiary: { text: "As the minimum for your master's degree, you should be able to study on your own and put an analytical way of solving problems into action.", rewrite: full, force: threshold, status: drafted }
  author-agent-written: "Treat this as a threshold standard: the minimum a master's degree in veterinary nursing asks at FHEQ level 7, SCQF level 11, on independent learning and problem-solving. Cite it as QAA (2024), Veterinary Nursing Subject Benchmark Statement, section 4, table \"Generic skills\", master's degree column. Do not present it as an RCVS or regulatory requirement, or as holding for another award. Set it beside the same row's other columns (4.2.b2.foundation, 4.2.b2) and the framework descriptor qaa/fheq-2024/4.17.b8.2 (spine:7, strand:autonomy)."
  author-agent-dialogue: "Raise it when a master's student or tutor asks what independent learning and problem-solving should look like by the end of the master's degree. Put it plainly: to a student, that by the end you should be able to study on your own and put an analytical way of solving problems into action; to staff, as where the course teaches and assesses it. Ask: \"What did you last learn on your own, and how did you tackle the problem it helped with?\" Avoid reading the table aloud and holding anyone to another award's column as if it were their minimum."
- statement: qaa/veterinary-nursing-2024/4.2.b3
  forPractitioner: { text: "The minimum for a honours degree (FHEQ level 6, SCQF level 10): teach and assess so that every graduate should be able to use evidence-based practice in the clinic and weigh up arguments, assumptions, abstract ideas and data critically.", rewrite: light, force: threshold, status: drafted }
  forBeneficiary: { text: "As the minimum for your honours degree, you should be able to use evidence-based practice in the clinic and weigh up arguments, assumptions, abstract ideas and data critically.", rewrite: full, force: threshold, status: drafted }
  author-agent-written: "Treat this as a threshold standard: the minimum a honours degree in veterinary nursing asks at FHEQ level 6, SCQF level 10, on evidence-based practice. Cite it as QAA (2024), Veterinary Nursing Subject Benchmark Statement, section 4, table \"Generic skills\", honours degree column. Do not present it as an RCVS or regulatory requirement, or as holding for another award. Set it beside the same row's other columns (4.2.b3.foundation, 4.2.b3.masters) and the framework descriptor qaa/fheq-2024/4.15.b7 and qaa/fqheis-2024/4.16.b6 (spine:6, strand:thinking)."
  author-agent-dialogue: "Raise it when an honours student or tutor asks what evidence-based practice should look like by the end of the honours degree. Put it plainly: to a student, that by the end you should be able to use evidence-based practice in the clinic and weigh up arguments, assumptions, abstract ideas and data critically; to staff, as where the course teaches and assesses it. Ask: \"Which piece of evidence has most changed how you nurse, and how did you judge it?\" Avoid reading the table aloud and holding anyone to another award's column as if it were their minimum."
- statement: qaa/veterinary-nursing-2024/4.2.b3.foundation
  forPractitioner: { text: "The minimum for a foundation degree (FHEQ level 5): teach and assess so that every graduate should be able to show what evidence-based practice rests on.", rewrite: light, force: threshold, status: drafted }
  forBeneficiary: { text: "As the minimum for your foundation degree, you should be able to show what evidence-based practice rests on.", rewrite: full, force: threshold, status: drafted }
  author-agent-written: "Treat this as a threshold standard: the minimum a foundation degree in veterinary nursing asks at FHEQ level 5, on evidence-based practice. Cite it as QAA (2024), Veterinary Nursing Subject Benchmark Statement, section 4, table \"Generic skills\", foundation degree column. Do not present it as an RCVS or regulatory requirement, or as holding for another award. Set it beside the same row's other columns (4.2.b3, 4.2.b3.masters) and the framework descriptor qaa/fheq-2024/4.12.b5 (spine:5, strand:thinking)."
  author-agent-dialogue: "Raise it when a foundation degree student or tutor asks what evidence-based practice should look like by the end of the foundation degree. Put it plainly: to a student, that by the end you should be able to show what evidence-based practice rests on; to staff, as where the course teaches and assesses it. Ask: \"Which piece of evidence has most changed how you nurse, and how did you judge it?\" Avoid reading the table aloud and holding anyone to another award's column as if it were their minimum."
- statement: qaa/veterinary-nursing-2024/4.2.b3.masters
  forPractitioner: { text: "The minimum for a master's degree (FHEQ level 7, SCQF level 11): teach and assess so that every graduate should be able to generate and critique evidence that sets the best clinical practice.", rewrite: light, force: threshold, status: drafted }
  forBeneficiary: { text: "As the minimum for your master's degree, you should be able to generate and critique evidence that sets the best clinical practice.", rewrite: full, force: threshold, status: drafted }
  author-agent-written: "Treat this as a threshold standard: the minimum a master's degree in veterinary nursing asks at FHEQ level 7, SCQF level 11, on evidence-based practice. Cite it as QAA (2024), Veterinary Nursing Subject Benchmark Statement, section 4, table \"Generic skills\", master's degree column. Do not present it as an RCVS or regulatory requirement, or as holding for another award. Set it beside the same row's other columns (4.2.b3.foundation, 4.2.b3) and the framework descriptor qaa/fheq-2024/4.17.b5 (spine:7, strand:thinking)."
  author-agent-dialogue: "Raise it when a master's student or tutor asks what evidence-based practice should look like by the end of the master's degree. Put it plainly: to a student, that by the end you should be able to generate and critique evidence that sets the best clinical practice; to staff, as where the course teaches and assesses it. Ask: \"Which piece of evidence has most changed how you nurse, and how did you judge it?\" Avoid reading the table aloud and holding anyone to another award's column as if it were their minimum."
- statement: qaa/veterinary-nursing-2024/4.2.b4
  forPractitioner: { text: "The minimum for a honours degree (FHEQ level 6, SCQF level 10): teach and assess so that every graduate should be able to take an active part in setting a team's goals and organising it.", rewrite: light, force: threshold, status: drafted }
  forBeneficiary: { text: "As the minimum for your honours degree, you should be able to take an active part in setting a team's goals and organising it.", rewrite: full, force: threshold, status: drafted }
  author-agent-written: "Treat this as a threshold standard: the minimum a honours degree in veterinary nursing asks at FHEQ level 6, SCQF level 10, on teamwork. Cite it as QAA (2024), Veterinary Nursing Subject Benchmark Statement, section 4, table \"Generic skills\", honours degree column. Do not present it as an RCVS or regulatory requirement, or as holding for another award. Set it beside the same row's other columns (4.2.b4.foundation, 4.2.b4.masters) and the framework descriptor qaa/fheq-2024/4.15.b9.2 and qaa/fqheis-2024/4.16.b9.2 (spine:6, strand:autonomy)."
  author-agent-dialogue: "Raise it when an honours student or tutor asks what teamwork should look like by the end of the honours degree. Put it plainly: to a student, that by the end you should be able to take an active part in setting a team's goals and organising it; to staff, as where the course teaches and assesses it. Ask: \"What part did you play in your team this week, and what would you take on next?\" Avoid reading the table aloud and holding anyone to another award's column as if it were their minimum."
- statement: qaa/veterinary-nursing-2024/4.2.b4.foundation
  forPractitioner: { text: "The minimum for a foundation degree (FHEQ level 5): teach and assess so that every graduate should be able to work with others and play a part in what the team does.", rewrite: light, force: threshold, status: drafted }
  forBeneficiary: { text: "As the minimum for your foundation degree, you should be able to work with others and play a part in what the team does.", rewrite: full, force: threshold, status: drafted }
  author-agent-written: "Treat this as a threshold standard: the minimum a foundation degree in veterinary nursing asks at FHEQ level 5, on teamwork. Cite it as QAA (2024), Veterinary Nursing Subject Benchmark Statement, section 4, table \"Generic skills\", foundation degree column. Do not present it as an RCVS or regulatory requirement, or as holding for another award. Set it beside the same row's other columns (4.2.b4, 4.2.b4.masters) and the framework descriptor qaa/fheq-2024/4.12.b8 (spine:5, strand:autonomy)."
  author-agent-dialogue: "Raise it when a foundation degree student or tutor asks what teamwork should look like by the end of the foundation degree. Put it plainly: to a student, that by the end you should be able to work with others and play a part in what the team does; to staff, as where the course teaches and assesses it. Ask: \"What part did you play in your team this week, and what would you take on next?\" Avoid reading the table aloud and holding anyone to another award's column as if it were their minimum."
- statement: qaa/veterinary-nursing-2024/4.2.b4.masters
  forPractitioner: { text: "The minimum for a master's degree (FHEQ level 7, SCQF level 11): teach and assess so that every graduate should be able to lead the shaping of a team's goals and how it is organised.", rewrite: light, force: threshold, status: drafted }
  forBeneficiary: { text: "As the minimum for your master's degree, you should be able to lead the shaping of a team's goals and how it is organised.", rewrite: full, force: threshold, status: drafted }
  author-agent-written: "Treat this as a threshold standard: the minimum a master's degree in veterinary nursing asks at FHEQ level 7, SCQF level 11, on teamwork. Cite it as QAA (2024), Veterinary Nursing Subject Benchmark Statement, section 4, table \"Generic skills\", master's degree column. Do not present it as an RCVS or regulatory requirement, or as holding for another award. Set it beside the same row's other columns (4.2.b4.foundation, 4.2.b4) and the framework descriptor qaa/fheq-2024/4.17.b8.2 (spine:7, strand:autonomy)."
  author-agent-dialogue: "Raise it when a master's student or tutor asks what teamwork should look like by the end of the master's degree. Put it plainly: to a student, that by the end you should be able to lead the shaping of a team's goals and how it is organised; to staff, as where the course teaches and assesses it. Ask: \"What part did you play in your team this week, and what would you take on next?\" Avoid reading the table aloud and holding anyone to another award's column as if it were their minimum."
- statement: qaa/veterinary-nursing-2024/4.2.b5
  forPractitioner: { text: "The minimum for a honours degree (FHEQ level 6, SCQF level 10): teach and assess so that every graduate should be able to use digital tools to strengthen presentations and support data analysis, within legal and ethical limits.", rewrite: light, force: threshold, status: drafted }
  forBeneficiary: { text: "As the minimum for your honours degree, you should be able to use digital tools to strengthen presentations and support data analysis, within legal and ethical limits.", rewrite: full, force: threshold, status: drafted }
  author-agent-written: "Treat this as a threshold standard: the minimum a honours degree in veterinary nursing asks at FHEQ level 6, SCQF level 10, on digital skills. Cite it as QAA (2024), Veterinary Nursing Subject Benchmark Statement, section 4, table \"Generic skills\", honours degree column. Do not present it as an RCVS or regulatory requirement, or as holding for another award. Set it beside the same row's other columns (4.2.b5.foundation, 4.2.b5.masters) and the framework descriptor qaa/fheq-2024/4.15.b8 and qaa/fqheis-2024/4.16.b7 (spine:6, strand:communication)."
  author-agent-dialogue: "Raise it when an honours student or tutor asks what digital skills should look like by the end of the honours degree. Put it plainly: to a student, that by the end you should be able to use digital tools to strengthen presentations and support data analysis, within legal and ethical limits; to staff, as where the course teaches and assesses it. Ask: \"Which digital tool do you rely on most, and how do you keep data use within the law?\" Avoid reading the table aloud and holding anyone to another award's column as if it were their minimum."
- statement: qaa/veterinary-nursing-2024/4.2.b5.foundation
  forPractitioner: { text: "The minimum for a foundation degree (FHEQ level 5): teach and assess so that every graduate should be able to use digital tools capably, including to find information, within legal and ethical limits.", rewrite: light, force: threshold, status: drafted }
  forBeneficiary: { text: "As the minimum for your foundation degree, you should be able to use digital tools capably, including to find information, within legal and ethical limits.", rewrite: full, force: threshold, status: drafted }
  author-agent-written: "Treat this as a threshold standard: the minimum a foundation degree in veterinary nursing asks at FHEQ level 5, on digital skills. Cite it as QAA (2024), Veterinary Nursing Subject Benchmark Statement, section 4, table \"Generic skills\", foundation degree column. Do not present it as an RCVS or regulatory requirement, or as holding for another award. Set it beside the same row's other columns (4.2.b5, 4.2.b5.masters) and the framework descriptor qaa/fheq-2024/4.12.b6 (spine:5, strand:communication)."
  author-agent-dialogue: "Raise it when a foundation degree student or tutor asks what digital skills should look like by the end of the foundation degree. Put it plainly: to a student, that by the end you should be able to use digital tools capably, including to find information, within legal and ethical limits; to staff, as where the course teaches and assesses it. Ask: \"Which digital tool do you rely on most, and how do you keep data use within the law?\" Avoid reading the table aloud and holding anyone to another award's column as if it were their minimum."
- statement: qaa/veterinary-nursing-2024/4.2.b5.masters
  forPractitioner: { text: "The minimum for a master's degree (FHEQ level 7, SCQF level 11): teach and assess so that every graduate should be able to produce digitally enriched presentations and analyse data with digital tools, within legal and ethical limits.", rewrite: light, force: threshold, status: drafted }
  forBeneficiary: { text: "As the minimum for your master's degree, you should be able to produce digitally enriched presentations and analyse data with digital tools, within legal and ethical limits.", rewrite: full, force: threshold, status: drafted }
  author-agent-written: "Treat this as a threshold standard: the minimum a master's degree in veterinary nursing asks at FHEQ level 7, SCQF level 11, on digital skills. Cite it as QAA (2024), Veterinary Nursing Subject Benchmark Statement, section 4, table \"Generic skills\", master's degree column. Do not present it as an RCVS or regulatory requirement, or as holding for another award. Set it beside the same row's other columns (4.2.b5.foundation, 4.2.b5) and the framework descriptor qaa/fheq-2024/4.17.b5 (spine:7, strand:communication)."
  author-agent-dialogue: "Raise it when a master's student or tutor asks what digital skills should look like by the end of the master's degree. Put it plainly: to a student, that by the end you should be able to produce digitally enriched presentations and analyse data with digital tools, within legal and ethical limits; to staff, as where the course teaches and assesses it. Ask: \"Which digital tool do you rely on most, and how do you keep data use within the law?\" Avoid reading the table aloud and holding anyone to another award's column as if it were their minimum."
- statement: qaa/veterinary-nursing-2024/4.2.b6
  forPractitioner: { text: "The minimum for a honours degree (FHEQ level 6, SCQF level 10): teach and assess so that every graduate should be able to handle confidential information as the law requires and guide colleagues when needed.", rewrite: light, force: threshold, status: drafted }
  forBeneficiary: { text: "As the minimum for your honours degree, you should be able to handle confidential information as the law requires and guide colleagues when needed.", rewrite: full, force: threshold, status: drafted }
  author-agent-written: "Treat this as a threshold standard: the minimum a honours degree in veterinary nursing asks at FHEQ level 6, SCQF level 10, on confidential information. Cite it as QAA (2024), Veterinary Nursing Subject Benchmark Statement, section 4, table \"Generic skills\", honours degree column. Do not present it as an RCVS or regulatory requirement, or as holding for another award. Set it beside the same row's other columns (4.2.b6.foundation, 4.2.b6.masters) and the framework descriptor qaa/fheq-2024/4.15.b9.2 and qaa/fqheis-2024/4.16.b9.2 (spine:6, strand:autonomy)."
  author-agent-dialogue: "Raise it when an honours student or tutor asks what confidential information should look like by the end of the honours degree. Put it plainly: to a student, that by the end you should be able to handle confidential information as the law requires and guide colleagues when needed; to staff, as where the course teaches and assesses it. Ask: \"What would you do if a colleague shared a client's details where they should not?\" Avoid reading the table aloud and holding anyone to another award's column as if it were their minimum."
- statement: qaa/veterinary-nursing-2024/4.2.b6.foundation
  forPractitioner: { text: "The minimum for a foundation degree (FHEQ level 5): teach and assess so that every graduate should be able to handle confidential information properly.", rewrite: light, force: threshold, status: drafted }
  forBeneficiary: { text: "As the minimum for your foundation degree, you should be able to handle confidential information properly.", rewrite: full, force: threshold, status: drafted }
  author-agent-written: "Treat this as a threshold standard: the minimum a foundation degree in veterinary nursing asks at FHEQ level 5, on confidential information. Cite it as QAA (2024), Veterinary Nursing Subject Benchmark Statement, section 4, table \"Generic skills\", foundation degree column. Do not present it as an RCVS or regulatory requirement, or as holding for another award. Set it beside the same row's other columns (4.2.b6, 4.2.b6.masters) and the framework descriptor qaa/fheq-2024/4.12.b8 (spine:5, strand:autonomy)."
  author-agent-dialogue: "Raise it when a foundation degree student or tutor asks what confidential information should look like by the end of the foundation degree. Put it plainly: to a student, that by the end you should be able to handle confidential information properly; to staff, as where the course teaches and assesses it. Ask: \"What would you do if a colleague shared a client's details where they should not?\" Avoid reading the table aloud and holding anyone to another award's column as if it were their minimum."
- statement: qaa/veterinary-nursing-2024/4.2.b6.masters
  forPractitioner: { text: "The minimum for a master's degree (FHEQ level 7, SCQF level 11): teach and assess so that every graduate should be able to manage confidential information as the law requires and help colleagues keep to that standard.", rewrite: light, force: threshold, status: drafted }
  forBeneficiary: { text: "As the minimum for your master's degree, you should be able to manage confidential information as the law requires and help colleagues keep to that standard.", rewrite: full, force: threshold, status: drafted }
  author-agent-written: "Treat this as a threshold standard: the minimum a master's degree in veterinary nursing asks at FHEQ level 7, SCQF level 11, on confidential information. Cite it as QAA (2024), Veterinary Nursing Subject Benchmark Statement, section 4, table \"Generic skills\", master's degree column. Do not present it as an RCVS or regulatory requirement, or as holding for another award. Set it beside the same row's other columns (4.2.b6.foundation, 4.2.b6) and the framework descriptor qaa/fheq-2024/4.17.b8.2 (spine:7, strand:autonomy)."
  author-agent-dialogue: "Raise it when a master's student or tutor asks what confidential information should look like by the end of the master's degree. Put it plainly: to a student, that by the end you should be able to manage confidential information as the law requires and help colleagues keep to that standard; to staff, as where the course teaches and assesses it. Ask: \"What would you do if a colleague shared a client's details where they should not?\" Avoid reading the table aloud and holding anyone to another award's column as if it were their minimum."
- statement: qaa/veterinary-nursing-2024/4.2.b7
  forPractitioner: { text: "The minimum for a honours degree (FHEQ level 6, SCQF level 10): teach and assess so that every graduate should be able to show self-awareness and self-assurance in clinical settings.", rewrite: light, force: threshold, status: drafted }
  forBeneficiary: { text: "As the minimum for your honours degree, you should be able to show self-awareness and self-assurance in clinical settings.", rewrite: full, force: threshold, status: drafted }
  author-agent-written: "Treat this as a threshold standard: the minimum a honours degree in veterinary nursing asks at FHEQ level 6, SCQF level 10, on self-awareness and confidence in the clinic. Cite it as QAA (2024), Veterinary Nursing Subject Benchmark Statement, section 4, table \"Generic skills\", honours degree column. Do not present it as an RCVS or regulatory requirement, or as holding for another award. Set it beside the same row's other columns (4.2.b7.foundation, 4.2.b7.masters) and the framework descriptor qaa/fheq-2024/4.15.b9.2 and qaa/fqheis-2024/4.16.b9.2 (spine:6, strand:autonomy)."
  author-agent-dialogue: "Raise it when an honours student or tutor asks what self-awareness and confidence in the clinic should look like by the end of the honours degree. Put it plainly: to a student, that by the end you should be able to show self-awareness and self-assurance in clinical settings; to staff, as where the course teaches and assesses it. Ask: \"Where in the clinic do you feel most and least sure of yourself, and why?\" Avoid reading the table aloud and holding anyone to another award's column as if it were their minimum."
- statement: qaa/veterinary-nursing-2024/4.2.b7.foundation
  forPractitioner: { text: "The minimum for a foundation degree (FHEQ level 5): teach and assess so that every graduate should be able to show self-awareness and self-assurance in clinical settings.", rewrite: light, force: threshold, status: drafted }
  forBeneficiary: { text: "As the minimum for your foundation degree, you should be able to show self-awareness and self-assurance in clinical settings.", rewrite: full, force: threshold, status: drafted }
  author-agent-written: "Treat this as a threshold standard: the minimum a foundation degree in veterinary nursing asks at FHEQ level 5, on self-awareness and confidence in the clinic. Cite it as QAA (2024), Veterinary Nursing Subject Benchmark Statement, section 4, table \"Generic skills\", foundation degree column. Do not present it as an RCVS or regulatory requirement, or as holding for another award. Set it beside the same row's other columns (4.2.b7, 4.2.b7.masters) and the framework descriptor qaa/fheq-2024/4.12.b8 (spine:5, strand:autonomy)."
  author-agent-dialogue: "Raise it when a foundation degree student or tutor asks what self-awareness and confidence in the clinic should look like by the end of the foundation degree. Put it plainly: to a student, that by the end you should be able to show self-awareness and self-assurance in clinical settings; to staff, as where the course teaches and assesses it. Ask: \"Where in the clinic do you feel most and least sure of yourself, and why?\" Avoid reading the table aloud and holding anyone to another award's column as if it were their minimum."
- statement: qaa/veterinary-nursing-2024/4.2.b7.masters
  forPractitioner: { text: "The minimum for a master's degree (FHEQ level 7, SCQF level 11): teach and assess so that every graduate should be able to show self-awareness and self-assurance in clinical settings.", rewrite: light, force: threshold, status: drafted }
  forBeneficiary: { text: "As the minimum for your master's degree, you should be able to show self-awareness and self-assurance in clinical settings.", rewrite: full, force: threshold, status: drafted }
  author-agent-written: "Treat this as a threshold standard: the minimum a master's degree in veterinary nursing asks at FHEQ level 7, SCQF level 11, on self-awareness and confidence in the clinic. Cite it as QAA (2024), Veterinary Nursing Subject Benchmark Statement, section 4, table \"Generic skills\", master's degree column. Do not present it as an RCVS or regulatory requirement, or as holding for another award. Set it beside the same row's other columns (4.2.b7.foundation, 4.2.b7) and the framework descriptor qaa/fheq-2024/4.17.b8.2 (spine:7, strand:autonomy)."
  author-agent-dialogue: "Raise it when a master's student or tutor asks what self-awareness and confidence in the clinic should look like by the end of the master's degree. Put it plainly: to a student, that by the end you should be able to show self-awareness and self-assurance in clinical settings; to staff, as where the course teaches and assesses it. Ask: \"Where in the clinic do you feel most and least sure of yourself, and why?\" Avoid reading the table aloud and holding anyone to another award's column as if it were their minimum."
- statement: qaa/veterinary-nursing-2024/4.2.b8
  forPractitioner: { text: "The minimum for a honours degree (FHEQ level 6, SCQF level 10): teach and assess so that every graduate should be able to know about and promote respect for the variety of cultures, values, outlooks and beliefs, and model the behaviours that anti-discriminatory practice depends on.", rewrite: light, force: threshold, status: drafted }
  forBeneficiary: { text: "As the minimum for your honours degree, you should be able to know about and promote respect for the variety of cultures, values, outlooks and beliefs, and model the behaviours that anti-discriminatory practice depends on.", rewrite: full, force: threshold, status: drafted }
  author-agent-written: "Treat this as a threshold standard: the minimum a honours degree in veterinary nursing asks at FHEQ level 6, SCQF level 10, on respect for diversity and anti-discriminatory behaviour. Cite it as QAA (2024), Veterinary Nursing Subject Benchmark Statement, section 4, table \"Generic skills\", honours degree column. Do not present it as an RCVS or regulatory requirement, or as holding for another award. Set it beside the same row's other columns (4.2.b8.foundation, 4.2.b8.masters) and the framework descriptor qaa/fheq-2024/4.15.b9.2 and qaa/fqheis-2024/4.16.b9.2 (spine:6, strand:autonomy)."
  author-agent-dialogue: "Raise it when an honours student or tutor asks what respect for diversity and anti-discriminatory behaviour should look like by the end of the honours degree. Put it plainly: to a student, that by the end you should be able to know about and promote respect for the variety of cultures, values, outlooks and beliefs, and model the behaviours that anti-discriminatory practice depends on; to staff, as where the course teaches and assesses it. Ask: \"How do you show respect for a client whose views on animal care differ from yours?\" Avoid reading the table aloud and holding anyone to another award's column as if it were their minimum."
- statement: qaa/veterinary-nursing-2024/4.2.b8.foundation
  forPractitioner: { text: "The minimum for a foundation degree (FHEQ level 5): teach and assess so that every graduate should be able to know about and promote respect for the variety of cultures, values, outlooks and beliefs, and model the behaviours that anti-discriminatory practice depends on.", rewrite: light, force: threshold, status: drafted }
  forBeneficiary: { text: "As the minimum for your foundation degree, you should be able to know about and promote respect for the variety of cultures, values, outlooks and beliefs, and model the behaviours that anti-discriminatory practice depends on.", rewrite: full, force: threshold, status: drafted }
  author-agent-written: "Treat this as a threshold standard: the minimum a foundation degree in veterinary nursing asks at FHEQ level 5, on respect for diversity and anti-discriminatory behaviour. Cite it as QAA (2024), Veterinary Nursing Subject Benchmark Statement, section 4, table \"Generic skills\", foundation degree column. Do not present it as an RCVS or regulatory requirement, or as holding for another award. Set it beside the same row's other columns (4.2.b8, 4.2.b8.masters) and the framework descriptor qaa/fheq-2024/4.12.b8 (spine:5, strand:autonomy)."
  author-agent-dialogue: "Raise it when a foundation degree student or tutor asks what respect for diversity and anti-discriminatory behaviour should look like by the end of the foundation degree. Put it plainly: to a student, that by the end you should be able to know about and promote respect for the variety of cultures, values, outlooks and beliefs, and model the behaviours that anti-discriminatory practice depends on; to staff, as where the course teaches and assesses it. Ask: \"How do you show respect for a client whose views on animal care differ from yours?\" Avoid reading the table aloud and holding anyone to another award's column as if it were their minimum."
- statement: qaa/veterinary-nursing-2024/4.2.b8.masters
  forPractitioner: { text: "The minimum for a master's degree (FHEQ level 7, SCQF level 11): teach and assess so that every graduate should be able to know about and promote respect for the variety of cultures, values, outlooks and beliefs, and model the behaviours that anti-discriminatory practice depends on.", rewrite: light, force: threshold, status: drafted }
  forBeneficiary: { text: "As the minimum for your master's degree, you should be able to know about and promote respect for the variety of cultures, values, outlooks and beliefs, and model the behaviours that anti-discriminatory practice depends on.", rewrite: full, force: threshold, status: drafted }
  author-agent-written: "Treat this as a threshold standard: the minimum a master's degree in veterinary nursing asks at FHEQ level 7, SCQF level 11, on respect for diversity and anti-discriminatory behaviour. Cite it as QAA (2024), Veterinary Nursing Subject Benchmark Statement, section 4, table \"Generic skills\", master's degree column. Do not present it as an RCVS or regulatory requirement, or as holding for another award. Set it beside the same row's other columns (4.2.b8.foundation, 4.2.b8) and the framework descriptor qaa/fheq-2024/4.17.b8.2 (spine:7, strand:autonomy)."
  author-agent-dialogue: "Raise it when a master's student or tutor asks what respect for diversity and anti-discriminatory behaviour should look like by the end of the master's degree. Put it plainly: to a student, that by the end you should be able to know about and promote respect for the variety of cultures, values, outlooks and beliefs, and model the behaviours that anti-discriminatory practice depends on; to staff, as where the course teaches and assesses it. Ask: \"How do you show respect for a client whose views on animal care differ from yours?\" Avoid reading the table aloud and holding anyone to another award's column as if it were their minimum."
- statement: qaa/veterinary-nursing-2024/4.2.b9
  forPractitioner: { text: "The minimum for a honours degree (FHEQ level 6, SCQF level 10): teach and assess so that every graduate should be able to analyse barriers found for people with protected characteristics and act to remove them.", rewrite: light, force: threshold, status: drafted }
  forBeneficiary: { text: "As the minimum for your honours degree, you should be able to analyse barriers found for people with protected characteristics and act to remove them.", rewrite: full, force: threshold, status: drafted }
  author-agent-written: "Treat this as a threshold standard: the minimum a honours degree in veterinary nursing asks at FHEQ level 6, SCQF level 10, on barriers for people with protected characteristics. Cite it as QAA (2024), Veterinary Nursing Subject Benchmark Statement, section 4, table \"Generic skills\", honours degree column. Do not present it as an RCVS or regulatory requirement, or as holding for another award. Set it beside the same row's other columns (4.2.b9.foundation, 4.2.b9.masters) and the framework descriptor qaa/fheq-2024/4.15.b7 and qaa/fqheis-2024/4.16.b6 (spine:6, strand:thinking)."
  author-agent-dialogue: "Raise it when an honours student or tutor asks what barriers for people with protected characteristics should look like by the end of the honours degree. Put it plainly: to a student, that by the end you should be able to analyse barriers found for people with protected characteristics and act to remove them; to staff, as where the course teaches and assesses it. Ask: \"What barrier might a disabled client or colleague face in your clinic, and what could change?\" Avoid reading the table aloud and holding anyone to another award's column as if it were their minimum."
- statement: qaa/veterinary-nursing-2024/4.2.b9.foundation
  forPractitioner: { text: "The minimum for a foundation degree (FHEQ level 5): teach and assess so that every graduate should be able to spot the barriers facing people with protected characteristics and know how to reduce them.", rewrite: light, force: threshold, status: drafted }
  forBeneficiary: { text: "As the minimum for your foundation degree, you should be able to spot the barriers facing people with protected characteristics and know how to reduce them.", rewrite: full, force: threshold, status: drafted }
  author-agent-written: "Treat this as a threshold standard: the minimum a foundation degree in veterinary nursing asks at FHEQ level 5, on barriers for people with protected characteristics. Cite it as QAA (2024), Veterinary Nursing Subject Benchmark Statement, section 4, table \"Generic skills\", foundation degree column. Do not present it as an RCVS or regulatory requirement, or as holding for another award. Set it beside the same row's other columns (4.2.b9, 4.2.b9.masters) and the framework descriptor qaa/fheq-2024/4.12.b5 (spine:5, strand:thinking)."
  author-agent-dialogue: "Raise it when a foundation degree student or tutor asks what barriers for people with protected characteristics should look like by the end of the foundation degree. Put it plainly: to a student, that by the end you should be able to spot the barriers facing people with protected characteristics and know how to reduce them; to staff, as where the course teaches and assesses it. Ask: \"What barrier might a disabled client or colleague face in your clinic, and what could change?\" Avoid reading the table aloud and holding anyone to another award's column as if it were their minimum."
- statement: qaa/veterinary-nursing-2024/4.2.b9.masters
  forPractitioner: { text: "The minimum for a master's degree (FHEQ level 7, SCQF level 11): teach and assess so that every graduate should be able to evaluate possible barriers for people with protected characteristics and decide on fitting actions.", rewrite: light, force: threshold, status: drafted }
  forBeneficiary: { text: "As the minimum for your master's degree, you should be able to evaluate possible barriers for people with protected characteristics and decide on fitting actions.", rewrite: full, force: threshold, status: drafted }
  author-agent-written: "Treat this as a threshold standard: the minimum a master's degree in veterinary nursing asks at FHEQ level 7, SCQF level 11, on barriers for people with protected characteristics. Cite it as QAA (2024), Veterinary Nursing Subject Benchmark Statement, section 4, table \"Generic skills\", master's degree column. Do not present it as an RCVS or regulatory requirement, or as holding for another award. Set it beside the same row's other columns (4.2.b9.foundation, 4.2.b9) and the framework descriptor qaa/fheq-2024/4.17.b5 (spine:7, strand:thinking)."
  author-agent-dialogue: "Raise it when a master's student or tutor asks what barriers for people with protected characteristics should look like by the end of the master's degree. Put it plainly: to a student, that by the end you should be able to evaluate possible barriers for people with protected characteristics and decide on fitting actions; to staff, as where the course teaches and assesses it. Ask: \"What barrier might a disabled client or colleague face in your clinic, and what could change?\" Avoid reading the table aloud and holding anyone to another award's column as if it were their minimum."
- statement: qaa/veterinary-nursing-2024/4.2.b10
  forPractitioner: { text: "The minimum for a honours degree (FHEQ level 6, SCQF level 10): teach and assess so that every graduate should be able to stay non-judgemental in all their work and avoid stigmatising any group of clients, team members or the public.", rewrite: light, force: threshold, status: drafted }
  forBeneficiary: { text: "As the minimum for your honours degree, you should be able to stay non-judgemental in all your work and avoid stigmatising any group of clients, team members or the public.", rewrite: full, force: threshold, status: drafted }
  author-agent-written: "Treat this as a threshold standard: the minimum a honours degree in veterinary nursing asks at FHEQ level 6, SCQF level 10, on non-judgemental practice. Cite it as QAA (2024), Veterinary Nursing Subject Benchmark Statement, section 4, table \"Generic skills\", honours degree column. Do not present it as an RCVS or regulatory requirement, or as holding for another award. Set it beside the same row's other columns (4.2.b10.foundation, 4.2.b10.masters) and the framework descriptor qaa/fheq-2024/4.15.b9.2 and qaa/fqheis-2024/4.16.b9.2 (spine:6, strand:autonomy)."
  author-agent-dialogue: "Raise it when an honours student or tutor asks what non-judgemental practice should look like by the end of the honours degree. Put it plainly: to a student, that by the end you should be able to stay non-judgemental in all your work and avoid stigmatising any group of clients, team members or the public; to staff, as where the course teaches and assesses it. Ask: \"Can you recall a moment when you caught yourself judging a client, and what you did next?\" Avoid reading the table aloud and holding anyone to another award's column as if it were their minimum."
- statement: qaa/veterinary-nursing-2024/4.2.b10.foundation
  forPractitioner: { text: "The minimum for a foundation degree (FHEQ level 5): teach and assess so that every graduate should be able to stay non-judgemental in all their work and avoid stigmatising any group of clients, team members or the public.", rewrite: light, force: threshold, status: drafted }
  forBeneficiary: { text: "As the minimum for your foundation degree, you should be able to stay non-judgemental in all your work and avoid stigmatising any group of clients, team members or the public.", rewrite: full, force: threshold, status: drafted }
  author-agent-written: "Treat this as a threshold standard: the minimum a foundation degree in veterinary nursing asks at FHEQ level 5, on non-judgemental practice. Cite it as QAA (2024), Veterinary Nursing Subject Benchmark Statement, section 4, table \"Generic skills\", foundation degree column. Do not present it as an RCVS or regulatory requirement, or as holding for another award. Set it beside the same row's other columns (4.2.b10, 4.2.b10.masters) and the framework descriptor qaa/fheq-2024/4.12.b8 (spine:5, strand:autonomy)."
  author-agent-dialogue: "Raise it when a foundation degree student or tutor asks what non-judgemental practice should look like by the end of the foundation degree. Put it plainly: to a student, that by the end you should be able to stay non-judgemental in all your work and avoid stigmatising any group of clients, team members or the public; to staff, as where the course teaches and assesses it. Ask: \"Can you recall a moment when you caught yourself judging a client, and what you did next?\" Avoid reading the table aloud and holding anyone to another award's column as if it were their minimum."
- statement: qaa/veterinary-nursing-2024/4.2.b10.masters
  forPractitioner: { text: "The minimum for a master's degree (FHEQ level 7, SCQF level 11): teach and assess so that every graduate should be able to stay non-judgemental in all their work and avoid stigmatising any group of clients, team members or the public.", rewrite: light, force: threshold, status: drafted }
  forBeneficiary: { text: "As the minimum for your master's degree, you should be able to stay non-judgemental in all your work and avoid stigmatising any group of clients, team members or the public.", rewrite: full, force: threshold, status: drafted }
  author-agent-written: "Treat this as a threshold standard: the minimum a master's degree in veterinary nursing asks at FHEQ level 7, SCQF level 11, on non-judgemental practice. Cite it as QAA (2024), Veterinary Nursing Subject Benchmark Statement, section 4, table \"Generic skills\", master's degree column. Do not present it as an RCVS or regulatory requirement, or as holding for another award. Set it beside the same row's other columns (4.2.b10.foundation, 4.2.b10) and the framework descriptor qaa/fheq-2024/4.17.b8.2 (spine:7, strand:autonomy)."
  author-agent-dialogue: "Raise it when a master's student or tutor asks what non-judgemental practice should look like by the end of the master's degree. Put it plainly: to a student, that by the end you should be able to stay non-judgemental in all your work and avoid stigmatising any group of clients, team members or the public; to staff, as where the course teaches and assesses it. Ask: \"Can you recall a moment when you caught yourself judging a client, and what you did next?\" Avoid reading the table aloud and holding anyone to another award's column as if it were their minimum."
- statement: qaa/veterinary-nursing-2024/4.2.b11
  forPractitioner: { text: "The minimum for a honours degree (FHEQ level 6, SCQF level 10): teach and assess so that every graduate should be able to build a sustainable approach across every part of veterinary nursing work.", rewrite: light, force: threshold, status: drafted }
  forBeneficiary: { text: "As the minimum for your honours degree, you should be able to build a sustainable approach across every part of veterinary nursing work.", rewrite: full, force: threshold, status: drafted }
  author-agent-written: "Treat this as a threshold standard: the minimum a honours degree in veterinary nursing asks at FHEQ level 6, SCQF level 10, on sustainable practice. Cite it as QAA (2024), Veterinary Nursing Subject Benchmark Statement, section 4, table \"Generic skills\", honours degree column. Do not present it as an RCVS or regulatory requirement, or as holding for another award. Set it beside the same row's other columns (4.2.b11.foundation, 4.2.b11.masters) and the framework descriptor qaa/fheq-2024/4.15.b6 and qaa/fqheis-2024/4.16.b4 (spine:6, strand:application)."
  author-agent-dialogue: "Raise it when an honours student or tutor asks what sustainable practice should look like by the end of the honours degree. Put it plainly: to a student, that by the end you should be able to build a sustainable approach across every part of veterinary nursing work; to staff, as where the course teaches and assesses it. Ask: \"What is one practice in your clinic you could make more sustainable without harming care?\" Avoid reading the table aloud and holding anyone to another award's column as if it were their minimum."
- statement: qaa/veterinary-nursing-2024/4.2.b11.foundation
  forPractitioner: { text: "The minimum for a foundation degree (FHEQ level 5): teach and assess so that every graduate should be able to take a sustainable approach across every part of veterinary nursing work.", rewrite: light, force: threshold, status: drafted }
  forBeneficiary: { text: "As the minimum for your foundation degree, you should be able to take a sustainable approach across every part of veterinary nursing work.", rewrite: full, force: threshold, status: drafted }
  author-agent-written: "Treat this as a threshold standard: the minimum a foundation degree in veterinary nursing asks at FHEQ level 5, on sustainable practice. Cite it as QAA (2024), Veterinary Nursing Subject Benchmark Statement, section 4, table \"Generic skills\", foundation degree column. Do not present it as an RCVS or regulatory requirement, or as holding for another award. Set it beside the same row's other columns (4.2.b11, 4.2.b11.masters) and the framework descriptor qaa/fheq-2024/4.12.b2 (spine:5, strand:application)."
  author-agent-dialogue: "Raise it when a foundation degree student or tutor asks what sustainable practice should look like by the end of the foundation degree. Put it plainly: to a student, that by the end you should be able to take a sustainable approach across every part of veterinary nursing work; to staff, as where the course teaches and assesses it. Ask: \"What is one practice in your clinic you could make more sustainable without harming care?\" Avoid reading the table aloud and holding anyone to another award's column as if it were their minimum."
- statement: qaa/veterinary-nursing-2024/4.2.b11.masters
  forPractitioner: { text: "The minimum for a master's degree (FHEQ level 7, SCQF level 11): teach and assess so that every graduate should be able to innovate and build a sustainable approach across every part of veterinary nursing work.", rewrite: light, force: threshold, status: drafted }
  forBeneficiary: { text: "As the minimum for your master's degree, you should be able to innovate and build a sustainable approach across every part of veterinary nursing work.", rewrite: full, force: threshold, status: drafted }
  author-agent-written: "Treat this as a threshold standard: the minimum a master's degree in veterinary nursing asks at FHEQ level 7, SCQF level 11, on sustainable practice. Cite it as QAA (2024), Veterinary Nursing Subject Benchmark Statement, section 4, table \"Generic skills\", master's degree column. Do not present it as an RCVS or regulatory requirement, or as holding for another award. Set it beside the same row's other columns (4.2.b11.foundation, 4.2.b11) and the framework descriptor qaa/fheq-2024/4.17.b3 (spine:7, strand:application)."
  author-agent-dialogue: "Raise it when a master's student or tutor asks what sustainable practice should look like by the end of the master's degree. Put it plainly: to a student, that by the end you should be able to innovate and build a sustainable approach across every part of veterinary nursing work; to staff, as where the course teaches and assesses it. Ask: \"What is one practice in your clinic you could make more sustainable without harming care?\" Avoid reading the table aloud and holding anyone to another award's column as if it were their minimum."
- statement: qaa/veterinary-nursing-2024/4.2.b12
  forPractitioner: { text: "The minimum for a honours degree (FHEQ level 6, SCQF level 10): teach and assess so that every graduate should be able to reflect on professional practice, their own and that of team members, to improve patient care and how the clinical setting is run.", rewrite: light, force: threshold, status: drafted }
  forBeneficiary: { text: "As the minimum for your honours degree, you should be able to reflect on professional practice, your own and that of team members, to improve patient care and how the clinical setting is run.", rewrite: full, force: threshold, status: drafted }
  author-agent-written: "Treat this as a threshold standard: the minimum a honours degree in veterinary nursing asks at FHEQ level 6, SCQF level 10, on reflective practice. Cite it as QAA (2024), Veterinary Nursing Subject Benchmark Statement, section 4, table \"Generic skills\", honours degree column. Do not present it as an RCVS or regulatory requirement, or as holding for another award. Set it beside the same row's other columns (4.2.b12.foundation, 4.2.b12.masters) and the framework descriptor qaa/fheq-2024/4.15.b9.2 and qaa/fqheis-2024/4.16.b9.2 (spine:6, strand:autonomy)."
  author-agent-dialogue: "Raise it when an honours student or tutor asks what reflective practice should look like by the end of the honours degree. Put it plainly: to a student, that by the end you should be able to reflect on professional practice, your own and that of team members, to improve patient care and how the clinical setting is run; to staff, as where the course teaches and assesses it. Ask: \"What did your last reflection change in how you or your team work?\" Avoid reading the table aloud and holding anyone to another award's column as if it were their minimum."
- statement: qaa/veterinary-nursing-2024/4.2.b12.foundation
  forPractitioner: { text: "The minimum for a foundation degree (FHEQ level 5): teach and assess so that every graduate should be able to reflect on professional practice and find chances to improve both individual and team working.", rewrite: light, force: threshold, status: drafted }
  forBeneficiary: { text: "As the minimum for your foundation degree, you should be able to reflect on professional practice and find chances to improve both individual and team working.", rewrite: full, force: threshold, status: drafted }
  author-agent-written: "Treat this as a threshold standard: the minimum a foundation degree in veterinary nursing asks at FHEQ level 5, on reflective practice. Cite it as QAA (2024), Veterinary Nursing Subject Benchmark Statement, section 4, table \"Generic skills\", foundation degree column. Do not present it as an RCVS or regulatory requirement, or as holding for another award. Set it beside the same row's other columns (4.2.b12, 4.2.b12.masters) and the framework descriptor qaa/fheq-2024/4.12.b8 (spine:5, strand:autonomy)."
  author-agent-dialogue: "Raise it when a foundation degree student or tutor asks what reflective practice should look like by the end of the foundation degree. Put it plainly: to a student, that by the end you should be able to reflect on professional practice and find chances to improve both individual and team working; to staff, as where the course teaches and assesses it. Ask: \"What did your last reflection change in how you or your team work?\" Avoid reading the table aloud and holding anyone to another award's column as if it were their minimum."
- statement: qaa/veterinary-nursing-2024/4.2.b12.masters
  forPractitioner: { text: "The minimum for a master's degree (FHEQ level 7, SCQF level 11): teach and assess so that every graduate should be able to lead reflection on professional practice, their own and the team's, to improve patient care and how the clinical setting is run.", rewrite: light, force: threshold, status: drafted }
  forBeneficiary: { text: "As the minimum for your master's degree, you should be able to lead reflection on professional practice, your own and the team's, to improve patient care and how the clinical setting is run.", rewrite: full, force: threshold, status: drafted }
  author-agent-written: "Treat this as a threshold standard: the minimum a master's degree in veterinary nursing asks at FHEQ level 7, SCQF level 11, on reflective practice. Cite it as QAA (2024), Veterinary Nursing Subject Benchmark Statement, section 4, table \"Generic skills\", master's degree column. Do not present it as an RCVS or regulatory requirement, or as holding for another award. Set it beside the same row's other columns (4.2.b12.foundation, 4.2.b12) and the framework descriptor qaa/fheq-2024/4.17.b8.2 (spine:7, strand:autonomy)."
  author-agent-dialogue: "Raise it when a master's student or tutor asks what reflective practice should look like by the end of the master's degree. Put it plainly: to a student, that by the end you should be able to lead reflection on professional practice, your own and the team's, to improve patient care and how the clinical setting is run; to staff, as where the course teaches and assesses it. Ask: \"What did your last reflection change in how you or your team work?\" Avoid reading the table aloud and holding anyone to another award's column as if it were their minimum."
- statement: qaa/veterinary-nursing-2024/4.2.b13
  forPractitioner: { text: "The minimum for a honours degree (FHEQ level 6, SCQF level 10): teach and assess so that every graduate should be able to use well-being habits to keep themselves and others fit to practise, knowing when more support is needed.", rewrite: light, force: threshold, status: drafted }
  forBeneficiary: { text: "As the minimum for your honours degree, you should be able to use well-being habits to keep yourself and others fit to practise, knowing when more support is needed.", rewrite: full, force: threshold, status: drafted }
  author-agent-written: "Treat this as a threshold standard: the minimum a honours degree in veterinary nursing asks at FHEQ level 6, SCQF level 10, on well-being and fitness to practise. Cite it as QAA (2024), Veterinary Nursing Subject Benchmark Statement, section 4, table \"Generic skills\", honours degree column. Do not present it as an RCVS or regulatory requirement, or as holding for another award. Set it beside the same row's other columns (4.2.b13.foundation, 4.2.b13.masters) and the framework descriptor qaa/fheq-2024/4.15.b9.2 and qaa/fqheis-2024/4.16.b9.2 (spine:6, strand:autonomy)."
  author-agent-dialogue: "Raise it when an honours student or tutor asks what well-being and fitness to practise should look like by the end of the honours degree. Put it plainly: to a student, that by the end you should be able to use well-being habits to keep yourself and others fit to practise, knowing when more support is needed; to staff, as where the course teaches and assesses it. Ask: \"How do you notice when you or a colleague needs more support, and who would you turn to?\" Avoid reading the table aloud and holding anyone to another award's column as if it were their minimum."
- statement: qaa/veterinary-nursing-2024/4.2.b13.foundation
  forPractitioner: { text: "The minimum for a foundation degree (FHEQ level 5): teach and assess so that every graduate should be able to use well-being habits to stay fit to practise, knowing when to seek more support.", rewrite: light, force: threshold, status: drafted }
  forBeneficiary: { text: "As the minimum for your foundation degree, you should be able to use well-being habits to stay fit to practise, knowing when to seek more support.", rewrite: full, force: threshold, status: drafted }
  author-agent-written: "Treat this as a threshold standard: the minimum a foundation degree in veterinary nursing asks at FHEQ level 5, on well-being and fitness to practise. Cite it as QAA (2024), Veterinary Nursing Subject Benchmark Statement, section 4, table \"Generic skills\", foundation degree column. Do not present it as an RCVS or regulatory requirement, or as holding for another award. Set it beside the same row's other columns (4.2.b13, 4.2.b13.masters) and the framework descriptor qaa/fheq-2024/4.12.b8 (spine:5, strand:autonomy)."
  author-agent-dialogue: "Raise it when a foundation degree student or tutor asks what well-being and fitness to practise should look like by the end of the foundation degree. Put it plainly: to a student, that by the end you should be able to use well-being habits to stay fit to practise, knowing when to seek more support; to staff, as where the course teaches and assesses it. Ask: \"How do you notice when you or a colleague needs more support, and who would you turn to?\" Avoid reading the table aloud and holding anyone to another award's column as if it were their minimum."
- statement: qaa/veterinary-nursing-2024/4.2.b13.masters
  forPractitioner: { text: "The minimum for a master's degree (FHEQ level 7, SCQF level 11): teach and assess so that every graduate should be able to use well-being habits to keep themselves and others fit to practise, knowing when more support is needed.", rewrite: light, force: threshold, status: drafted }
  forBeneficiary: { text: "As the minimum for your master's degree, you should be able to use well-being habits to keep yourself and others fit to practise, knowing when more support is needed.", rewrite: full, force: threshold, status: drafted }
  author-agent-written: "Treat this as a threshold standard: the minimum a master's degree in veterinary nursing asks at FHEQ level 7, SCQF level 11, on well-being and fitness to practise. Cite it as QAA (2024), Veterinary Nursing Subject Benchmark Statement, section 4, table \"Generic skills\", master's degree column. Do not present it as an RCVS or regulatory requirement, or as holding for another award. Set it beside the same row's other columns (4.2.b13.foundation, 4.2.b13) and the framework descriptor qaa/fheq-2024/4.17.b8.2 (spine:7, strand:autonomy)."
  author-agent-dialogue: "Raise it when a master's student or tutor asks what well-being and fitness to practise should look like by the end of the master's degree. Put it plainly: to a student, that by the end you should be able to use well-being habits to keep yourself and others fit to practise, knowing when more support is needed; to staff, as where the course teaches and assesses it. Ask: \"How do you notice when you or a colleague needs more support, and who would you turn to?\" Avoid reading the table aloud and holding anyone to another award's column as if it were their minimum."
- statement: qaa/veterinary-nursing-2024/4.2.b14
  forPractitioner: { text: "The minimum for a honours degree (FHEQ level 6, SCQF level 10): teach and assess so that every graduate should be able to choose and use theories, concepts and principles, judging which frameworks best support holistic veterinary care.", rewrite: light, force: threshold, status: drafted }
  forBeneficiary: { text: "As the minimum for your honours degree, you should be able to choose and use theories, concepts and principles, judging which frameworks best support holistic veterinary care.", rewrite: full, force: threshold, status: drafted }
  author-agent-written: "Treat this as a threshold standard: the minimum a honours degree in veterinary nursing asks at FHEQ level 6, SCQF level 10, on theory in holistic care. Cite it as QAA (2024), Veterinary Nursing Subject Benchmark Statement, section 4, table \"Principles and concepts: application\", honours degree column. Do not present it as an RCVS or regulatory requirement, or as holding for another award. Set it beside the same row's other columns (4.2.b14.foundation, 4.2.b14.masters) and the framework descriptor qaa/fheq-2024/4.15.b6 and qaa/fqheis-2024/4.16.b4 (spine:6, strand:application)."
  author-agent-dialogue: "Raise it when an honours student or tutor asks what theory in holistic care should look like by the end of the honours degree. Put it plainly: to a student, that by the end you should be able to choose and use theories, concepts and principles, judging which frameworks best support holistic veterinary care; to staff, as where the course teaches and assesses it. Ask: \"Which theory or model shaped the last care plan you wrote, and why that one?\" Avoid reading the table aloud and holding anyone to another award's column as if it were their minimum."
- statement: qaa/veterinary-nursing-2024/4.2.b14.foundation
  forPractitioner: { text: "The minimum for a foundation degree (FHEQ level 5): teach and assess so that every graduate should be able to choose and use theories, concepts and principles to give holistic veterinary care.", rewrite: light, force: threshold, status: drafted }
  forBeneficiary: { text: "As the minimum for your foundation degree, you should be able to choose and use theories, concepts and principles to give holistic veterinary care.", rewrite: full, force: threshold, status: drafted }
  author-agent-written: "Treat this as a threshold standard: the minimum a foundation degree in veterinary nursing asks at FHEQ level 5, on theory in holistic care. Cite it as QAA (2024), Veterinary Nursing Subject Benchmark Statement, section 4, table \"Principles and concepts: application\", foundation degree column. Do not present it as an RCVS or regulatory requirement, or as holding for another award. Set it beside the same row's other columns (4.2.b14, 4.2.b14.masters) and the framework descriptor qaa/fheq-2024/4.12.b2 (spine:5, strand:application)."
  author-agent-dialogue: "Raise it when a foundation degree student or tutor asks what theory in holistic care should look like by the end of the foundation degree. Put it plainly: to a student, that by the end you should be able to choose and use theories, concepts and principles to give holistic veterinary care; to staff, as where the course teaches and assesses it. Ask: \"Which theory or model shaped the last care plan you wrote, and why that one?\" Avoid reading the table aloud and holding anyone to another award's column as if it were their minimum."
- statement: qaa/veterinary-nursing-2024/4.2.b14.masters
  forPractitioner: { text: "The minimum for a master's degree (FHEQ level 7, SCQF level 11): teach and assess so that every graduate should be able to choose and use advanced theory, drawing on other relevant disciplines, to give holistic care in complex, unpredictable situations.", rewrite: light, force: threshold, status: drafted }
  forBeneficiary: { text: "As the minimum for your master's degree, you should be able to choose and use advanced theory, drawing on other relevant disciplines, to give holistic care in complex, unpredictable situations.", rewrite: full, force: threshold, status: drafted }
  author-agent-written: "Treat this as a threshold standard: the minimum a master's degree in veterinary nursing asks at FHEQ level 7, SCQF level 11, on theory in holistic care. Cite it as QAA (2024), Veterinary Nursing Subject Benchmark Statement, section 4, table \"Principles and concepts: application\", master's degree column. Do not present it as an RCVS or regulatory requirement, or as holding for another award. Set it beside the same row's other columns (4.2.b14.foundation, 4.2.b14) and the framework descriptor qaa/fheq-2024/4.17.b3 (spine:7, strand:application)."
  author-agent-dialogue: "Raise it when a master's student or tutor asks what theory in holistic care should look like by the end of the master's degree. Put it plainly: to a student, that by the end you should be able to choose and use advanced theory, drawing on other relevant disciplines, to give holistic care in complex, unpredictable situations; to staff, as where the course teaches and assesses it. Ask: \"Which theory or model shaped the last care plan you wrote, and why that one?\" Avoid reading the table aloud and holding anyone to another award's column as if it were their minimum."
- statement: qaa/veterinary-nursing-2024/4.2.b15
  forPractitioner: { text: "The minimum for a honours degree (FHEQ level 6, SCQF level 10): teach and assess so that every graduate should be able to recognise possible risks, suitable interventions and the need for protocols that reduce risk in good-quality care.", rewrite: light, force: threshold, status: drafted }
  forBeneficiary: { text: "As the minimum for your honours degree, you should be able to recognise possible risks, suitable interventions and the need for protocols that reduce risk in good-quality care.", rewrite: full, force: threshold, status: drafted }
  author-agent-written: "Treat this as a threshold standard: the minimum a honours degree in veterinary nursing asks at FHEQ level 6, SCQF level 10, on managing clinical risk. Cite it as QAA (2024), Veterinary Nursing Subject Benchmark Statement, section 4, table \"Principles and concepts: application\", honours degree column. Do not present it as an RCVS or regulatory requirement, or as holding for another award. Set it beside the same row's other columns (4.2.b15.foundation, 4.2.b15.masters) and the framework descriptor qaa/fheq-2024/4.15.b7 and qaa/fqheis-2024/4.16.b6 (spine:6, strand:thinking)."
  author-agent-dialogue: "Raise it when an honours student or tutor asks what managing clinical risk should look like by the end of the honours degree. Put it plainly: to a student, that by the end you should be able to recognise possible risks, suitable interventions and the need for protocols that reduce risk in good-quality care; to staff, as where the course teaches and assesses it. Ask: \"What risk did you spot early on a recent case, and what did you do about it?\" Avoid reading the table aloud and holding anyone to another award's column as if it were their minimum."
- statement: qaa/veterinary-nursing-2024/4.2.b15.foundation
  forPractitioner: { text: "The minimum for a foundation degree (FHEQ level 5): teach and assess so that every graduate should be able to recognise possible risks and the interventions that can head off complications.", rewrite: light, force: threshold, status: drafted }
  forBeneficiary: { text: "As the minimum for your foundation degree, you should be able to recognise possible risks and the interventions that can head off complications.", rewrite: full, force: threshold, status: drafted }
  author-agent-written: "Treat this as a threshold standard: the minimum a foundation degree in veterinary nursing asks at FHEQ level 5, on managing clinical risk. Cite it as QAA (2024), Veterinary Nursing Subject Benchmark Statement, section 4, table \"Principles and concepts: application\", foundation degree column. Do not present it as an RCVS or regulatory requirement, or as holding for another award. Set it beside the same row's other columns (4.2.b15, 4.2.b15.masters) and the framework descriptor qaa/fheq-2024/4.12.b5 (spine:5, strand:thinking)."
  author-agent-dialogue: "Raise it when a foundation degree student or tutor asks what managing clinical risk should look like by the end of the foundation degree. Put it plainly: to a student, that by the end you should be able to recognise possible risks and the interventions that can head off complications; to staff, as where the course teaches and assesses it. Ask: \"What risk did you spot early on a recent case, and what did you do about it?\" Avoid reading the table aloud and holding anyone to another award's column as if it were their minimum."
- statement: qaa/veterinary-nursing-2024/4.2.b15.masters
  forPractitioner: { text: "The minimum for a master's degree (FHEQ level 7, SCQF level 11): teach and assess so that every graduate should be able to critically evaluate and improve a practice's risk-management protocols while shaping its strategy and direction.", rewrite: light, force: threshold, status: drafted }
  forBeneficiary: { text: "As the minimum for your master's degree, you should be able to critically evaluate and improve a practice's risk-management protocols while shaping its strategy and direction.", rewrite: full, force: threshold, status: drafted }
  author-agent-written: "Treat this as a threshold standard: the minimum a master's degree in veterinary nursing asks at FHEQ level 7, SCQF level 11, on managing clinical risk. Cite it as QAA (2024), Veterinary Nursing Subject Benchmark Statement, section 4, table \"Principles and concepts: application\", master's degree column. Do not present it as an RCVS or regulatory requirement, or as holding for another award. Set it beside the same row's other columns (4.2.b15.foundation, 4.2.b15) and the framework descriptor qaa/fheq-2024/4.17.b5 (spine:7, strand:thinking)."
  author-agent-dialogue: "Raise it when a master's student or tutor asks what managing clinical risk should look like by the end of the master's degree. Put it plainly: to a student, that by the end you should be able to critically evaluate and improve a practice's risk-management protocols while shaping its strategy and direction; to staff, as where the course teaches and assesses it. Ask: \"What risk did you spot early on a recent case, and what did you do about it?\" Avoid reading the table aloud and holding anyone to another award's column as if it were their minimum."
- statement: qaa/veterinary-nursing-2024/4.2.b16
  forPractitioner: { text: "The minimum for a honours degree (FHEQ level 6, SCQF level 10): teach and assess so that every graduate should be able to critically analyse current issues in the health and welfare of animals.", rewrite: light, force: threshold, status: drafted }
  forBeneficiary: { text: "As the minimum for your honours degree, you should be able to critically analyse current issues in the health and welfare of animals.", rewrite: full, force: threshold, status: drafted }
  author-agent-written: "Treat this as a threshold standard: the minimum a honours degree in veterinary nursing asks at FHEQ level 6, SCQF level 10, on promoting animal health and welfare. Cite it as QAA (2024), Veterinary Nursing Subject Benchmark Statement, section 4, table \"Principles and concepts: application\", honours degree column. Do not present it as an RCVS or regulatory requirement, or as holding for another award. Set it beside the same row's other columns (4.2.b16.foundation, 4.2.b16.masters) and the framework descriptor qaa/fheq-2024/4.15.b6 and qaa/fqheis-2024/4.16.b4 (spine:6, strand:application)."
  author-agent-dialogue: "Raise it when an honours student or tutor asks what promoting animal health and welfare should look like by the end of the honours degree. Put it plainly: to a student, that by the end you should be able to critically analyse current issues in the health and welfare of animals; to staff, as where the course teaches and assesses it. Ask: \"What health message do owners most need from you, and how do you know it works?\" Avoid reading the table aloud and holding anyone to another award's column as if it were their minimum."
- statement: qaa/veterinary-nursing-2024/4.2.b16.foundation
  forPractitioner: { text: "The minimum for a foundation degree (FHEQ level 5): teach and assess so that every graduate should be able to analyse and interpret educational and promotional material and draw on it to advance the health and welfare of animals.", rewrite: light, force: threshold, status: drafted }
  forBeneficiary: { text: "As the minimum for your foundation degree, you should be able to analyse and interpret educational and promotional material and draw on it to advance the health and welfare of animals.", rewrite: full, force: threshold, status: drafted }
  author-agent-written: "Treat this as a threshold standard: the minimum a foundation degree in veterinary nursing asks at FHEQ level 5, on promoting animal health and welfare. Cite it as QAA (2024), Veterinary Nursing Subject Benchmark Statement, section 4, table \"Principles and concepts: application\", foundation degree column. Do not present it as an RCVS or regulatory requirement, or as holding for another award. Set it beside the same row's other columns (4.2.b16, 4.2.b16.masters) and the framework descriptor qaa/fheq-2024/4.12.b2 (spine:5, strand:application)."
  author-agent-dialogue: "Raise it when a foundation degree student or tutor asks what promoting animal health and welfare should look like by the end of the foundation degree. Put it plainly: to a student, that by the end you should be able to analyse and interpret educational and promotional material and draw on it to advance the health and welfare of animals; to staff, as where the course teaches and assesses it. Ask: \"What health message do owners most need from you, and how do you know it works?\" Avoid reading the table aloud and holding anyone to another award's column as if it were their minimum."
- statement: qaa/veterinary-nursing-2024/4.2.b16.masters
  forPractitioner: { text: "The minimum for a master's degree (FHEQ level 7, SCQF level 11): teach and assess so that every graduate should be able to devise new strategies, grounded in evidence-based practice, to advance the health and welfare of animals.", rewrite: light, force: threshold, status: drafted }
  forBeneficiary: { text: "As the minimum for your master's degree, you should be able to devise new strategies, grounded in evidence-based practice, to advance the health and welfare of animals.", rewrite: full, force: threshold, status: drafted }
  author-agent-written: "Treat this as a threshold standard: the minimum a master's degree in veterinary nursing asks at FHEQ level 7, SCQF level 11, on promoting animal health and welfare. Cite it as QAA (2024), Veterinary Nursing Subject Benchmark Statement, section 4, table \"Principles and concepts: application\", master's degree column. Do not present it as an RCVS or regulatory requirement, or as holding for another award. Set it beside the same row's other columns (4.2.b16.foundation, 4.2.b16) and the framework descriptor qaa/fheq-2024/4.17.b3 (spine:7, strand:application)."
  author-agent-dialogue: "Raise it when a master's student or tutor asks what promoting animal health and welfare should look like by the end of the master's degree. Put it plainly: to a student, that by the end you should be able to devise new strategies, grounded in evidence-based practice, to advance the health and welfare of animals; to staff, as where the course teaches and assesses it. Ask: \"What health message do owners most need from you, and how do you know it works?\" Avoid reading the table aloud and holding anyone to another award's column as if it were their minimum."
- statement: qaa/veterinary-nursing-2024/4.2.b17
  forPractitioner: { text: "The minimum for a honours degree (FHEQ level 6, SCQF level 10): teach and assess so that every graduate should be able to explain and justify the decisions and problem-solving behind veterinary nursing practice, even when the data are incomplete.", rewrite: light, force: threshold, status: drafted }
  forBeneficiary: { text: "As the minimum for your honours degree, you should be able to explain and justify the decisions and problem-solving behind veterinary nursing practice, even when the data are incomplete.", rewrite: full, force: threshold, status: drafted }
  author-agent-written: "Treat this as a threshold standard: the minimum a honours degree in veterinary nursing asks at FHEQ level 6, SCQF level 10, on evidence behind clinical decisions. Cite it as QAA (2024), Veterinary Nursing Subject Benchmark Statement, section 4, table \"Principles and concepts: application\", honours degree column. Do not present it as an RCVS or regulatory requirement, or as holding for another award. Set it beside the same row's other columns (4.2.b17.foundation, 4.2.b17.masters) and the framework descriptor qaa/fheq-2024/4.15.b7 and qaa/fqheis-2024/4.16.b6 (spine:6, strand:thinking)."
  author-agent-dialogue: "Raise it when an honours student or tutor asks what evidence behind clinical decisions should look like by the end of the honours degree. Put it plainly: to a student, that by the end you should be able to explain and justify the decisions and problem-solving behind veterinary nursing practice, even when the data are incomplete; to staff, as where the course teaches and assesses it. Ask: \"Talk me through a decision you made with only part of the information: what did you weigh?\" Avoid reading the table aloud and holding anyone to another award's column as if it were their minimum."
- statement: qaa/veterinary-nursing-2024/4.2.b17.foundation
  forPractitioner: { text: "The minimum for a foundation degree (FHEQ level 5): teach and assess so that every graduate should be able to draw on suitable research and evidence to support and justify clinical decisions.", rewrite: light, force: threshold, status: drafted }
  forBeneficiary: { text: "As the minimum for your foundation degree, you should be able to draw on suitable research and evidence to support and justify clinical decisions.", rewrite: full, force: threshold, status: drafted }
  author-agent-written: "Treat this as a threshold standard: the minimum a foundation degree in veterinary nursing asks at FHEQ level 5, on evidence behind clinical decisions. Cite it as QAA (2024), Veterinary Nursing Subject Benchmark Statement, section 4, table \"Principles and concepts: application\", foundation degree column. Do not present it as an RCVS or regulatory requirement, or as holding for another award. Set it beside the same row's other columns (4.2.b17, 4.2.b17.masters) and the framework descriptor qaa/fheq-2024/4.12.b5 (spine:5, strand:thinking)."
  author-agent-dialogue: "Raise it when a foundation degree student or tutor asks what evidence behind clinical decisions should look like by the end of the foundation degree. Put it plainly: to a student, that by the end you should be able to draw on suitable research and evidence to support and justify clinical decisions; to staff, as where the course teaches and assesses it. Ask: \"Talk me through a decision you made with only part of the information: what did you weigh?\" Avoid reading the table aloud and holding anyone to another award's column as if it were their minimum."
- statement: qaa/veterinary-nursing-2024/4.2.b17.masters
  forPractitioner: { text: "The minimum for a master's degree (FHEQ level 7, SCQF level 11): teach and assess so that every graduate should be able to bring advanced, specialist information together systematically to propose new ways of meeting complex patient care needs.", rewrite: light, force: threshold, status: drafted }
  forBeneficiary: { text: "As the minimum for your master's degree, you should be able to bring advanced, specialist information together systematically to propose new ways of meeting complex patient care needs.", rewrite: full, force: threshold, status: drafted }
  author-agent-written: "Treat this as a threshold standard: the minimum a master's degree in veterinary nursing asks at FHEQ level 7, SCQF level 11, on evidence behind clinical decisions. Cite it as QAA (2024), Veterinary Nursing Subject Benchmark Statement, section 4, table \"Principles and concepts: application\", master's degree column. Do not present it as an RCVS or regulatory requirement, or as holding for another award. Set it beside the same row's other columns (4.2.b17.foundation, 4.2.b17) and the framework descriptor qaa/fheq-2024/4.17.b5 (spine:7, strand:thinking)."
  author-agent-dialogue: "Raise it when a master's student or tutor asks what evidence behind clinical decisions should look like by the end of the master's degree. Put it plainly: to a student, that by the end you should be able to bring advanced, specialist information together systematically to propose new ways of meeting complex patient care needs; to staff, as where the course teaches and assesses it. Ask: \"Talk me through a decision you made with only part of the information: what did you weigh?\" Avoid reading the table aloud and holding anyone to another award's column as if it were their minimum."
- statement: qaa/veterinary-nursing-2024/4.2.b18
  forPractitioner: { text: "The minimum for a honours degree (FHEQ level 6, SCQF level 10): teach and assess so that every graduate should be able to use theory and research to carry out and record a full, systematic nursing assessment that takes account of the patient's needs and, where relevant, the owner's.", rewrite: light, force: threshold, status: drafted }
  forBeneficiary: { text: "As the minimum for your honours degree, you should be able to use theory and research to carry out and record a full, systematic nursing assessment that takes account of the patient's needs and, where relevant, the owner's.", rewrite: full, force: threshold, status: drafted }
  author-agent-written: "Treat this as a threshold standard: the minimum a honours degree in veterinary nursing asks at FHEQ level 6, SCQF level 10, on nursing assessment. Cite it as QAA (2024), Veterinary Nursing Subject Benchmark Statement, section 4, table \"Principles and concepts: application\", honours degree column. Do not present it as an RCVS or regulatory requirement, or as holding for another award. Set it beside the same row's other columns (4.2.b18.foundation, 4.2.b18.masters) and the framework descriptor qaa/fheq-2024/4.15.b6 and qaa/fqheis-2024/4.16.b4 (spine:6, strand:application)."
  author-agent-dialogue: "Raise it when an honours student or tutor asks what nursing assessment should look like by the end of the honours degree. Put it plainly: to a student, that by the end you should be able to use theory and research to carry out and record a full, systematic nursing assessment that takes account of the patient's needs and, where relevant, the owner's; to staff, as where the course teaches and assesses it. Ask: \"What did your last nursing assessment miss at first, and how did you find it?\" Avoid reading the table aloud and holding anyone to another award's column as if it were their minimum."
- statement: qaa/veterinary-nursing-2024/4.2.b18.foundation
  forPractitioner: { text: "The minimum for a foundation degree (FHEQ level 5): teach and assess so that every graduate should be able to carry out and record a systematic nursing assessment that takes account of the patient's needs and, where relevant, the owner's.", rewrite: light, force: threshold, status: drafted }
  forBeneficiary: { text: "As the minimum for your foundation degree, you should be able to carry out and record a systematic nursing assessment that takes account of the patient's needs and, where relevant, the owner's.", rewrite: full, force: threshold, status: drafted }
  author-agent-written: "Treat this as a threshold standard: the minimum a foundation degree in veterinary nursing asks at FHEQ level 5, on nursing assessment. Cite it as QAA (2024), Veterinary Nursing Subject Benchmark Statement, section 4, table \"Principles and concepts: application\", foundation degree column. Do not present it as an RCVS or regulatory requirement, or as holding for another award. Set it beside the same row's other columns (4.2.b18, 4.2.b18.masters) and the framework descriptor qaa/fheq-2024/4.12.b2 (spine:5, strand:application)."
  author-agent-dialogue: "Raise it when a foundation degree student or tutor asks what nursing assessment should look like by the end of the foundation degree. Put it plainly: to a student, that by the end you should be able to carry out and record a systematic nursing assessment that takes account of the patient's needs and, where relevant, the owner's; to staff, as where the course teaches and assesses it. Ask: \"What did your last nursing assessment miss at first, and how did you find it?\" Avoid reading the table aloud and holding anyone to another award's column as if it were their minimum."
- statement: qaa/veterinary-nursing-2024/4.2.b18.masters
  forPractitioner: { text: "The minimum for a master's degree (FHEQ level 7, SCQF level 11): teach and assess so that every graduate should be able to build a systematic, evidence-based framework for assessing what patient and owner need, whatever their cultural or socioeconomic background.", rewrite: light, force: threshold, status: drafted }
  forBeneficiary: { text: "As the minimum for your master's degree, you should be able to build a systematic, evidence-based framework for assessing what patient and owner need, whatever their cultural or socioeconomic background.", rewrite: full, force: threshold, status: drafted }
  author-agent-written: "Treat this as a threshold standard: the minimum a master's degree in veterinary nursing asks at FHEQ level 7, SCQF level 11, on nursing assessment. Cite it as QAA (2024), Veterinary Nursing Subject Benchmark Statement, section 4, table \"Principles and concepts: application\", master's degree column. Do not present it as an RCVS or regulatory requirement, or as holding for another award. Set it beside the same row's other columns (4.2.b18.foundation, 4.2.b18) and the framework descriptor qaa/fheq-2024/4.17.b3 (spine:7, strand:application)."
  author-agent-dialogue: "Raise it when a master's student or tutor asks what nursing assessment should look like by the end of the master's degree. Put it plainly: to a student, that by the end you should be able to build a systematic, evidence-based framework for assessing what patient and owner need, whatever their cultural or socioeconomic background; to staff, as where the course teaches and assesses it. Ask: \"What did your last nursing assessment miss at first, and how did you find it?\" Avoid reading the table aloud and holding anyone to another award's column as if it were their minimum."
- statement: qaa/veterinary-nursing-2024/4.2.b19
  forPractitioner: { text: "The minimum for a honours degree (FHEQ level 6, SCQF level 10): teach and assess so that every graduate should be able to evaluate shifting priorities in a complex, changing setting and communicate suitably.", rewrite: light, force: threshold, status: drafted }
  forBeneficiary: { text: "As the minimum for your honours degree, you should be able to evaluate shifting priorities in a complex, changing setting and communicate suitably.", rewrite: full, force: threshold, status: drafted }
  author-agent-written: "Treat this as a threshold standard: the minimum a honours degree in veterinary nursing asks at FHEQ level 6, SCQF level 10, on priorities and care delivery. Cite it as QAA (2024), Veterinary Nursing Subject Benchmark Statement, section 4, table \"Principles and concepts: application\", honours degree column. Do not present it as an RCVS or regulatory requirement, or as holding for another award. Set it beside the same row's other columns (4.2.b19.foundation, 4.2.b19.masters) and the framework descriptor qaa/fheq-2024/4.15.b9.2 and qaa/fqheis-2024/4.16.b9.2 (spine:6, strand:autonomy)."
  author-agent-dialogue: "Raise it when an honours student or tutor asks what priorities and care delivery should look like by the end of the honours degree. Put it plainly: to a student, that by the end you should be able to evaluate shifting priorities in a complex, changing setting and communicate suitably; to staff, as where the course teaches and assesses it. Ask: \"On a busy shift, how do you decide what comes first, and who do you tell?\" Avoid reading the table aloud and holding anyone to another award's column as if it were their minimum."
- statement: qaa/veterinary-nursing-2024/4.2.b19.foundation
  forPractitioner: { text: "The minimum for a foundation degree (FHEQ level 5): teach and assess so that every graduate should be able to judge nursing priorities and give competent care that meets the needs found.", rewrite: light, force: threshold, status: drafted }
  forBeneficiary: { text: "As the minimum for your foundation degree, you should be able to judge nursing priorities and give competent care that meets the needs found.", rewrite: full, force: threshold, status: drafted }
  author-agent-written: "Treat this as a threshold standard: the minimum a foundation degree in veterinary nursing asks at FHEQ level 5, on priorities and care delivery. Cite it as QAA (2024), Veterinary Nursing Subject Benchmark Statement, section 4, table \"Principles and concepts: application\", foundation degree column. Do not present it as an RCVS or regulatory requirement, or as holding for another award. Set it beside the same row's other columns (4.2.b19, 4.2.b19.masters) and the framework descriptor qaa/fheq-2024/4.12.b8 (spine:5, strand:autonomy)."
  author-agent-dialogue: "Raise it when a foundation degree student or tutor asks what priorities and care delivery should look like by the end of the foundation degree. Put it plainly: to a student, that by the end you should be able to judge nursing priorities and give competent care that meets the needs found; to staff, as where the course teaches and assesses it. Ask: \"On a busy shift, how do you decide what comes first, and who do you tell?\" Avoid reading the table aloud and holding anyone to another award's column as if it were their minimum."
- statement: qaa/veterinary-nursing-2024/4.2.b19.masters
  forPractitioner: { text: "The minimum for a master's degree (FHEQ level 7, SCQF level 11): teach and assess so that every graduate should be able to develop the team and show leadership so that the team gives the care needed.", rewrite: light, force: threshold, status: drafted }
  forBeneficiary: { text: "As the minimum for your master's degree, you should be able to develop the team and show leadership so that the team gives the care needed.", rewrite: full, force: threshold, status: drafted }
  author-agent-written: "Treat this as a threshold standard: the minimum a master's degree in veterinary nursing asks at FHEQ level 7, SCQF level 11, on priorities and care delivery. Cite it as QAA (2024), Veterinary Nursing Subject Benchmark Statement, section 4, table \"Principles and concepts: application\", master's degree column. Do not present it as an RCVS or regulatory requirement, or as holding for another award. Set it beside the same row's other columns (4.2.b19.foundation, 4.2.b19) and the framework descriptor qaa/fheq-2024/4.17.b8.2 (spine:7, strand:autonomy)."
  author-agent-dialogue: "Raise it when a master's student or tutor asks what priorities and care delivery should look like by the end of the master's degree. Put it plainly: to a student, that by the end you should be able to develop the team and show leadership so that the team gives the care needed; to staff, as where the course teaches and assesses it. Ask: \"On a busy shift, how do you decide what comes first, and who do you tell?\" Avoid reading the table aloud and holding anyone to another award's column as if it were their minimum."
- statement: qaa/veterinary-nursing-2024/4.2.b20
  forPractitioner: { text: "The minimum for a honours degree (FHEQ level 6, SCQF level 10): teach and assess so that every graduate should be able to critically evaluate research findings and use them to change planned care.", rewrite: light, force: threshold, status: drafted }
  forBeneficiary: { text: "As the minimum for your honours degree, you should be able to critically evaluate research findings and use them to change planned care.", rewrite: full, force: threshold, status: drafted }
  author-agent-written: "Treat this as a threshold standard: the minimum a honours degree in veterinary nursing asks at FHEQ level 6, SCQF level 10, on care planning and research. Cite it as QAA (2024), Veterinary Nursing Subject Benchmark Statement, section 4, table \"Principles and concepts: application\", honours degree column. Do not present it as an RCVS or regulatory requirement, or as holding for another award. Set it beside the same row's other columns (4.2.b20.foundation, 4.2.b20.masters) and the framework descriptor qaa/fheq-2024/4.15.b3.2 and qaa/fqheis-2024/4.16.b5 (spine:6, strand:application)."
  author-agent-dialogue: "Raise it when an honours student or tutor asks what care planning and research should look like by the end of the honours degree. Put it plainly: to a student, that by the end you should be able to critically evaluate research findings and use them to change planned care; to staff, as where the course teaches and assesses it. Ask: \"Which research finding would you use to change a care plan, and how would you check it worked?\" Avoid reading the table aloud and holding anyone to another award's column as if it were their minimum."
- statement: qaa/veterinary-nursing-2024/4.2.b20.foundation
  forPractitioner: { text: "The minimum for a foundation degree (FHEQ level 5): teach and assess so that every graduate should be able to draw up and record a care plan with the veterinary team and the client's consent, in the patient's best interest.", rewrite: light, force: threshold, status: drafted }
  forBeneficiary: { text: "As the minimum for your foundation degree, you should be able to draw up and record a care plan with the veterinary team and the client's consent, in the patient's best interest.", rewrite: full, force: threshold, status: drafted }
  author-agent-written: "Treat this as a threshold standard: the minimum a foundation degree in veterinary nursing asks at FHEQ level 5, on care planning and research. Cite it as QAA (2024), Veterinary Nursing Subject Benchmark Statement, section 4, table \"Principles and concepts: application\", foundation degree column. Do not present it as an RCVS or regulatory requirement, or as holding for another award. Set it beside the same row's other columns (4.2.b20, 4.2.b20.masters) and the framework descriptor qaa/fheq-2024/4.12.b3 (spine:5, strand:application)."
  author-agent-dialogue: "Raise it when a foundation degree student or tutor asks what care planning and research should look like by the end of the foundation degree. Put it plainly: to a student, that by the end you should be able to draw up and record a care plan with the veterinary team and the client's consent, in the patient's best interest; to staff, as where the course teaches and assesses it. Ask: \"Which research finding would you use to change a care plan, and how would you check it worked?\" Avoid reading the table aloud and holding anyone to another award's column as if it were their minimum."
- statement: qaa/veterinary-nursing-2024/4.2.b20.masters
  forPractitioner: { text: "The minimum for a master's degree (FHEQ level 7, SCQF level 11): teach and assess so that every graduate should be able to produce research that adds to the evidence base.", rewrite: light, force: threshold, status: drafted }
  forBeneficiary: { text: "As the minimum for your master's degree, you should be able to produce research that adds to the evidence base.", rewrite: full, force: threshold, status: drafted }
  author-agent-written: "Treat this as a threshold standard: the minimum a master's degree in veterinary nursing asks at FHEQ level 7, SCQF level 11, on care planning and research. Cite it as QAA (2024), Veterinary Nursing Subject Benchmark Statement, section 4, table \"Principles and concepts: application\", master's degree column. Do not present it as an RCVS or regulatory requirement, or as holding for another award. Set it beside the same row's other columns (4.2.b20.foundation, 4.2.b20) and the framework descriptor qaa/fheq-2024/4.17.b4.1 (spine:7, strand:application)."
  author-agent-dialogue: "Raise it when a master's student or tutor asks what care planning and research should look like by the end of the master's degree. Put it plainly: to a student, that by the end you should be able to produce research that adds to the evidence base; to staff, as where the course teaches and assesses it. Ask: \"Which research finding would you use to change a care plan, and how would you check it worked?\" Avoid reading the table aloud and holding anyone to another award's column as if it were their minimum."
- statement: qaa/veterinary-nursing-2024/4.2.b21
  forPractitioner: { text: "The minimum for a honours degree (FHEQ level 6, SCQF level 10): teach and assess so that every graduate should be able to challenge critically the care delivered, weighing the shifting social, cultural, spiritual, legal, political and economic factors and animal welfare.", rewrite: light, force: threshold, status: drafted }
  forBeneficiary: { text: "As the minimum for your honours degree, you should be able to challenge critically the care delivered, weighing the shifting social, cultural, spiritual, legal, political and economic factors and animal welfare.", rewrite: full, force: threshold, status: drafted }
  author-agent-written: "Treat this as a threshold standard: the minimum a honours degree in veterinary nursing asks at FHEQ level 6, SCQF level 10, on accountability and the context of care. Cite it as QAA (2024), Veterinary Nursing Subject Benchmark Statement, section 4, table \"Principles and concepts: application\", honours degree column. Do not present it as an RCVS or regulatory requirement, or as holding for another award. Set it beside the same row's other columns (4.2.b21.foundation, 4.2.b21.masters) and the framework descriptor qaa/fheq-2024/4.15.b9.2 and qaa/fqheis-2024/4.16.b9.2 (spine:6, strand:autonomy)."
  author-agent-dialogue: "Raise it when an honours student or tutor asks what accountability and the context of care should look like by the end of the honours degree. Put it plainly: to a student, that by the end you should be able to challenge critically the care delivered, weighing the shifting social, cultural, spiritual, legal, political and economic factors and animal welfare; to staff, as where the course teaches and assesses it. Ask: \"Which outside factor, such as cost or culture, most shaped care you gave recently?\" Avoid reading the table aloud and holding anyone to another award's column as if it were their minimum."
- statement: qaa/veterinary-nursing-2024/4.2.b21.foundation
  forPractitioner: { text: "The minimum for a foundation degree (FHEQ level 5): teach and assess so that every graduate should be able to show accountability for the care given, weighing the social, cultural, spiritual, legal, political and economic factors and animal welfare.", rewrite: light, force: threshold, status: drafted }
  forBeneficiary: { text: "As the minimum for your foundation degree, you should be able to show accountability for the care given, weighing the social, cultural, spiritual, legal, political and economic factors and animal welfare.", rewrite: full, force: threshold, status: drafted }
  author-agent-written: "Treat this as a threshold standard: the minimum a foundation degree in veterinary nursing asks at FHEQ level 5, on accountability and the context of care. Cite it as QAA (2024), Veterinary Nursing Subject Benchmark Statement, section 4, table \"Principles and concepts: application\", foundation degree column. Do not present it as an RCVS or regulatory requirement, or as holding for another award. Set it beside the same row's other columns (4.2.b21, 4.2.b21.masters) and the framework descriptor qaa/fheq-2024/4.12.b8 (spine:5, strand:autonomy)."
  author-agent-dialogue: "Raise it when a foundation degree student or tutor asks what accountability and the context of care should look like by the end of the foundation degree. Put it plainly: to a student, that by the end you should be able to show accountability for the care given, weighing the social, cultural, spiritual, legal, political and economic factors and animal welfare; to staff, as where the course teaches and assesses it. Ask: \"Which outside factor, such as cost or culture, most shaped care you gave recently?\" Avoid reading the table aloud and holding anyone to another award's column as if it were their minimum."
- statement: qaa/veterinary-nursing-2024/4.2.b21.masters
  forPractitioner: { text: "The minimum for a master's degree (FHEQ level 7, SCQF level 11): teach and assess so that every graduate should be able to act autonomously in making strategic decisions and setting practice guidelines, owning the results in abstract, highly complex and unpredictable settings.", rewrite: light, force: threshold, status: drafted }
  forBeneficiary: { text: "As the minimum for your master's degree, you should be able to act autonomously in making strategic decisions and setting practice guidelines, owning the results in abstract, highly complex and unpredictable settings.", rewrite: full, force: threshold, status: drafted }
  author-agent-written: "Treat this as a threshold standard: the minimum a master's degree in veterinary nursing asks at FHEQ level 7, SCQF level 11, on accountability and the context of care. Cite it as QAA (2024), Veterinary Nursing Subject Benchmark Statement, section 4, table \"Principles and concepts: application\", master's degree column. Do not present it as an RCVS or regulatory requirement, or as holding for another award. Set it beside the same row's other columns (4.2.b21.foundation, 4.2.b21) and the framework descriptor qaa/fheq-2024/4.17.b8.2 (spine:7, strand:autonomy)."
  author-agent-dialogue: "Raise it when a master's student or tutor asks what accountability and the context of care should look like by the end of the master's degree. Put it plainly: to a student, that by the end you should be able to act autonomously in making strategic decisions and setting practice guidelines, owning the results in abstract, highly complex and unpredictable settings; to staff, as where the course teaches and assesses it. Ask: \"Which outside factor, such as cost or culture, most shaped care you gave recently?\" Avoid reading the table aloud and holding anyone to another award's column as if it were their minimum."
- statement: qaa/veterinary-nursing-2024/4.2.b22
  forPractitioner: { text: "The minimum for a honours degree (FHEQ level 6, SCQF level 10): teach and assess so that every graduate should be able to critically evaluate the results of professional interventions and adjust nursing care to match.", rewrite: light, force: threshold, status: drafted }
  forBeneficiary: { text: "As the minimum for your honours degree, you should be able to critically evaluate the results of professional interventions and adjust nursing care to match.", rewrite: full, force: threshold, status: drafted }
  author-agent-written: "Treat this as a threshold standard: the minimum a honours degree in veterinary nursing asks at FHEQ level 6, SCQF level 10, on outcomes of interventions. Cite it as QAA (2024), Veterinary Nursing Subject Benchmark Statement, section 4, table \"Principles and concepts: application\", honours degree column. Do not present it as an RCVS or regulatory requirement, or as holding for another award. Set it beside the same row's other columns (4.2.b22.foundation, 4.2.b22.masters) and the framework descriptor qaa/fheq-2024/4.15.b7 and qaa/fqheis-2024/4.16.b6 (spine:6, strand:thinking)."
  author-agent-dialogue: "Raise it when an honours student or tutor asks what outcomes of interventions should look like by the end of the honours degree. Put it plainly: to a student, that by the end you should be able to critically evaluate the results of professional interventions and adjust nursing care to match; to staff, as where the course teaches and assesses it. Ask: \"How did you know whether your last intervention worked, and what did you change?\" Avoid reading the table aloud and holding anyone to another award's column as if it were their minimum."
- statement: qaa/veterinary-nursing-2024/4.2.b22.foundation
  forPractitioner: { text: "The minimum for a foundation degree (FHEQ level 5): teach and assess so that every graduate should be able to record accurately and evaluate the results of professional interventions.", rewrite: light, force: threshold, status: drafted }
  forBeneficiary: { text: "As the minimum for your foundation degree, you should be able to record accurately and evaluate the results of professional interventions.", rewrite: full, force: threshold, status: drafted }
  author-agent-written: "Treat this as a threshold standard: the minimum a foundation degree in veterinary nursing asks at FHEQ level 5, on outcomes of interventions. Cite it as QAA (2024), Veterinary Nursing Subject Benchmark Statement, section 4, table \"Principles and concepts: application\", foundation degree column. Do not present it as an RCVS or regulatory requirement, or as holding for another award. Set it beside the same row's other columns (4.2.b22, 4.2.b22.masters) and the framework descriptor qaa/fheq-2024/4.12.b5 (spine:5, strand:thinking)."
  author-agent-dialogue: "Raise it when a foundation degree student or tutor asks what outcomes of interventions should look like by the end of the foundation degree. Put it plainly: to a student, that by the end you should be able to record accurately and evaluate the results of professional interventions; to staff, as where the course teaches and assesses it. Ask: \"How did you know whether your last intervention worked, and what did you change?\" Avoid reading the table aloud and holding anyone to another award's column as if it were their minimum."
- statement: qaa/veterinary-nursing-2024/4.2.b22.masters
  forPractitioner: { text: "The minimum for a master's degree (FHEQ level 7, SCQF level 11): teach and assess so that every graduate should be able to use the results of interventions to develop themselves and others, and share findings or lead within clinical governance.", rewrite: light, force: threshold, status: drafted }
  forBeneficiary: { text: "As the minimum for your master's degree, you should be able to use the results of interventions to develop yourself and others, and share findings or lead within clinical governance.", rewrite: full, force: threshold, status: drafted }
  author-agent-written: "Treat this as a threshold standard: the minimum a master's degree in veterinary nursing asks at FHEQ level 7, SCQF level 11, on outcomes of interventions. Cite it as QAA (2024), Veterinary Nursing Subject Benchmark Statement, section 4, table \"Principles and concepts: application\", master's degree column. Do not present it as an RCVS or regulatory requirement, or as holding for another award. Set it beside the same row's other columns (4.2.b22.foundation, 4.2.b22) and the framework descriptor qaa/fheq-2024/4.17.b5 (spine:7, strand:thinking)."
  author-agent-dialogue: "Raise it when a master's student or tutor asks what outcomes of interventions should look like by the end of the master's degree. Put it plainly: to a student, that by the end you should be able to use the results of interventions to develop yourself and others, and share findings or lead within clinical governance; to staff, as where the course teaches and assesses it. Ask: \"How did you know whether your last intervention worked, and what did you change?\" Avoid reading the table aloud and holding anyone to another award's column as if it were their minimum."
- statement: qaa/veterinary-nursing-2024/4.2.b23
  forPractitioner: { text: "The minimum for a honours degree (FHEQ level 6, SCQF level 10): teach and assess so that every graduate should be able to contribute skilfully and confidently to multidisciplinary work, giving direction where needed.", rewrite: light, force: threshold, status: drafted }
  forBeneficiary: { text: "As the minimum for your honours degree, you should be able to contribute skilfully and confidently to multidisciplinary work, giving direction where needed.", rewrite: full, force: threshold, status: drafted }
  author-agent-written: "Treat this as a threshold standard: the minimum a honours degree in veterinary nursing asks at FHEQ level 6, SCQF level 10, on multidisciplinary teamwork. Cite it as QAA (2024), Veterinary Nursing Subject Benchmark Statement, section 4, table \"Principles and concepts: application\", honours degree column. Do not present it as an RCVS or regulatory requirement, or as holding for another award. Set it beside the same row's other columns (4.2.b23.foundation, 4.2.b23.masters) and the framework descriptor qaa/fheq-2024/4.15.b8 and qaa/fqheis-2024/4.16.b7 (spine:6, strand:communication)."
  author-agent-dialogue: "Raise it when an honours student or tutor asks what multidisciplinary teamwork should look like by the end of the honours degree. Put it plainly: to a student, that by the end you should be able to contribute skilfully and confidently to multidisciplinary work, giving direction where needed; to staff, as where the course teaches and assesses it. Ask: \"Whose contribution in the team do you rely on most, and how do you make use of it?\" Avoid reading the table aloud and holding anyone to another award's column as if it were their minimum."
- statement: qaa/veterinary-nursing-2024/4.2.b23.foundation
  forPractitioner: { text: "The minimum for a foundation degree (FHEQ level 5): teach and assess so that every graduate should be able to take part in teamwork that values and makes use of colleagues' contributions across veterinary care settings.", rewrite: light, force: threshold, status: drafted }
  forBeneficiary: { text: "As the minimum for your foundation degree, you should be able to take part in teamwork that values and makes use of colleagues' contributions across veterinary care settings.", rewrite: full, force: threshold, status: drafted }
  author-agent-written: "Treat this as a threshold standard: the minimum a foundation degree in veterinary nursing asks at FHEQ level 5, on multidisciplinary teamwork. Cite it as QAA (2024), Veterinary Nursing Subject Benchmark Statement, section 4, table \"Principles and concepts: application\", foundation degree column. Do not present it as an RCVS or regulatory requirement, or as holding for another award. Set it beside the same row's other columns (4.2.b23, 4.2.b23.masters) and the framework descriptor qaa/fheq-2024/4.12.b6 (spine:5, strand:communication)."
  author-agent-dialogue: "Raise it when a foundation degree student or tutor asks what multidisciplinary teamwork should look like by the end of the foundation degree. Put it plainly: to a student, that by the end you should be able to take part in teamwork that values and makes use of colleagues' contributions across veterinary care settings; to staff, as where the course teaches and assesses it. Ask: \"Whose contribution in the team do you rely on most, and how do you make use of it?\" Avoid reading the table aloud and holding anyone to another award's column as if it were their minimum."
- statement: qaa/veterinary-nursing-2024/4.2.b23.masters
  forPractitioner: { text: "The minimum for a master's degree (FHEQ level 7, SCQF level 11): teach and assess so that every graduate should be able to use and grow advanced interpersonal, team and networking skills to lift team performance strategically in highly complex settings and to take part in specialist professional communities.", rewrite: light, force: threshold, status: drafted }
  forBeneficiary: { text: "As the minimum for your master's degree, you should be able to use and grow advanced interpersonal, team and networking skills to lift team performance strategically in highly complex settings and to take part in specialist professional communities.", rewrite: full, force: threshold, status: drafted }
  author-agent-written: "Treat this as a threshold standard: the minimum a master's degree in veterinary nursing asks at FHEQ level 7, SCQF level 11, on multidisciplinary teamwork. Cite it as QAA (2024), Veterinary Nursing Subject Benchmark Statement, section 4, table \"Principles and concepts: application\", master's degree column. Do not present it as an RCVS or regulatory requirement, or as holding for another award. Set it beside the same row's other columns (4.2.b23.foundation, 4.2.b23) and the framework descriptor qaa/fheq-2024/4.17.b5 (spine:7, strand:communication)."
  author-agent-dialogue: "Raise it when a master's student or tutor asks what multidisciplinary teamwork should look like by the end of the master's degree. Put it plainly: to a student, that by the end you should be able to use and grow advanced interpersonal, team and networking skills to lift team performance strategically in highly complex settings and to take part in specialist professional communities; to staff, as where the course teaches and assesses it. Ask: \"Whose contribution in the team do you rely on most, and how do you make use of it?\" Avoid reading the table aloud and holding anyone to another award's column as if it were their minimum."
- statement: qaa/veterinary-nursing-2024/4.2.b24
  forPractitioner: { text: "The minimum for a honours degree (FHEQ level 6, SCQF level 10): teach and assess so that every graduate should be able to critically evaluate the moral and ethical questions in caring for veterinary patients and speak up for animal welfare.", rewrite: light, force: threshold, status: drafted }
  forBeneficiary: { text: "As the minimum for your honours degree, you should be able to critically evaluate the moral and ethical questions in caring for veterinary patients and speak up for animal welfare.", rewrite: full, force: threshold, status: drafted }
  author-agent-written: "Treat this as a threshold standard: the minimum a honours degree in veterinary nursing asks at FHEQ level 6, SCQF level 10, on ethics in patient care. Cite it as QAA (2024), Veterinary Nursing Subject Benchmark Statement, section 4, table \"Principles and concepts: application\", honours degree column. Do not present it as an RCVS or regulatory requirement, or as holding for another award. Set it beside the same row's other columns (4.2.b24.foundation, 4.2.b24.masters) and the framework descriptor qaa/fheq-2024/4.15.b7 and qaa/fqheis-2024/4.16.b6 (spine:6, strand:thinking)."
  author-agent-dialogue: "Raise it when an honours student or tutor asks what ethics in patient care should look like by the end of the honours degree. Put it plainly: to a student, that by the end you should be able to critically evaluate the moral and ethical questions in caring for veterinary patients and speak up for animal welfare; to staff, as where the course teaches and assesses it. Ask: \"What ethical question came up on a recent case, and how was it settled?\" Avoid reading the table aloud and holding anyone to another award's column as if it were their minimum."
- statement: qaa/veterinary-nursing-2024/4.2.b24.foundation
  forPractitioner: { text: "The minimum for a foundation degree (FHEQ level 5): teach and assess so that every graduate should be able to recognise the moral and ethical questions in caring for veterinary patients.", rewrite: light, force: threshold, status: drafted }
  forBeneficiary: { text: "As the minimum for your foundation degree, you should be able to recognise the moral and ethical questions in caring for veterinary patients.", rewrite: full, force: threshold, status: drafted }
  author-agent-written: "Treat this as a threshold standard: the minimum a foundation degree in veterinary nursing asks at FHEQ level 5, on ethics in patient care. Cite it as QAA (2024), Veterinary Nursing Subject Benchmark Statement, section 4, table \"Principles and concepts: application\", foundation degree column. Do not present it as an RCVS or regulatory requirement, or as holding for another award. Set it beside the same row's other columns (4.2.b24, 4.2.b24.masters) and the framework descriptor qaa/fheq-2024/4.12.b5 (spine:5, strand:thinking)."
  author-agent-dialogue: "Raise it when a foundation degree student or tutor asks what ethics in patient care should look like by the end of the foundation degree. Put it plainly: to a student, that by the end you should be able to recognise the moral and ethical questions in caring for veterinary patients; to staff, as where the course teaches and assesses it. Ask: \"What ethical question came up on a recent case, and how was it settled?\" Avoid reading the table aloud and holding anyone to another award's column as if it were their minimum."
- statement: qaa/veterinary-nursing-2024/4.2.b24.masters
  forPractitioner: { text: "The minimum for a master's degree (FHEQ level 7, SCQF level 11): teach and assess so that every graduate should be able to apply an advanced grasp of ethical and professional values and codes systematically to personal and strategic decisions and dilemmas, working with others to propose and argue for solutions in highly complex settings.", rewrite: light, force: threshold, status: drafted }
  forBeneficiary: { text: "As the minimum for your master's degree, you should be able to apply an advanced grasp of ethical and professional values and codes systematically to personal and strategic decisions and dilemmas, working with others to propose and argue for solutions in highly complex settings.", rewrite: full, force: threshold, status: drafted }
  author-agent-written: "Treat this as a threshold standard: the minimum a master's degree in veterinary nursing asks at FHEQ level 7, SCQF level 11, on ethics in patient care. Cite it as QAA (2024), Veterinary Nursing Subject Benchmark Statement, section 4, table \"Principles and concepts: application\", master's degree column. Do not present it as an RCVS or regulatory requirement, or as holding for another award. Set it beside the same row's other columns (4.2.b24.foundation, 4.2.b24) and the framework descriptor qaa/fheq-2024/4.17.b5 (spine:7, strand:thinking)."
  author-agent-dialogue: "Raise it when a master's student or tutor asks what ethics in patient care should look like by the end of the master's degree. Put it plainly: to a student, that by the end you should be able to apply an advanced grasp of ethical and professional values and codes systematically to personal and strategic decisions and dilemmas, working with others to propose and argue for solutions in highly complex settings; to staff, as where the course teaches and assesses it. Ask: \"What ethical question came up on a recent case, and how was it settled?\" Avoid reading the table aloud and holding anyone to another award's column as if it were their minimum."
- statement: qaa/veterinary-nursing-2024/4.2.b25
  forPractitioner: { text: "The minimum for a honours degree (FHEQ level 6, SCQF level 10): teach and assess so that every graduate should be able to show robust knowledge of the core subjects behind veterinary nursing, use a veterinary nurse's knowledge and skills in daily practice and keep evaluating nursing care to improve professional practice.", rewrite: light, force: threshold, status: drafted }
  forBeneficiary: { text: "As the minimum for your honours degree, you should be able to show robust knowledge of the core subjects behind veterinary nursing, use a veterinary nurse's knowledge and skills in daily practice and keep evaluating nursing care to improve professional practice.", rewrite: full, force: threshold, status: drafted }
  author-agent-written: "Treat this as a threshold standard: the minimum a honours degree in veterinary nursing asks at FHEQ level 6, SCQF level 10, on core subject knowledge. Cite it as QAA (2024), Veterinary Nursing Subject Benchmark Statement, section 4, table \"Subject knowledge, understanding and associated skills\", honours degree column. Do not present it as an RCVS or regulatory requirement, or as holding for another award. Set it beside the same row's other columns (4.2.b25.foundation, 4.2.b25.masters) and the framework descriptor qaa/fheq-2024/4.15.b1 and qaa/fqheis-2024/4.16.b1 (spine:6, strand:knowledge)."
  author-agent-dialogue: "Raise it when an honours student or tutor asks what core subject knowledge should look like by the end of the honours degree. Put it plainly: to a student, that by the end you should be able to show robust knowledge of the core subjects behind veterinary nursing, use a veterinary nurse's knowledge and skills in daily practice and keep evaluating nursing care to improve professional practice; to staff, as where the course teaches and assesses it. Ask: \"Which underpinning subject do you find hardest to use on the ward, and why?\" Avoid reading the table aloud and holding anyone to another award's column as if it were their minimum."
- statement: qaa/veterinary-nursing-2024/4.2.b25.foundation
  forPractitioner: { text: "The minimum for a foundation degree (FHEQ level 5): teach and assess so that every graduate should be able to show sound knowledge of the core subjects behind veterinary nursing and use a veterinary nurse's knowledge and skills in daily practice.", rewrite: light, force: threshold, status: drafted }
  forBeneficiary: { text: "As the minimum for your foundation degree, you should be able to show sound knowledge of the core subjects behind veterinary nursing and use a veterinary nurse's knowledge and skills in daily practice.", rewrite: full, force: threshold, status: drafted }
  author-agent-written: "Treat this as a threshold standard: the minimum a foundation degree in veterinary nursing asks at FHEQ level 5, on core subject knowledge. Cite it as QAA (2024), Veterinary Nursing Subject Benchmark Statement, section 4, table \"Subject knowledge, understanding and associated skills\", foundation degree column. Do not present it as an RCVS or regulatory requirement, or as holding for another award. Set it beside the same row's other columns (4.2.b25, 4.2.b25.masters) and the framework descriptor qaa/fheq-2024/4.12.b1 (spine:5, strand:knowledge)."
  author-agent-dialogue: "Raise it when a foundation degree student or tutor asks what core subject knowledge should look like by the end of the foundation degree. Put it plainly: to a student, that by the end you should be able to show sound knowledge of the core subjects behind veterinary nursing and use a veterinary nurse's knowledge and skills in daily practice; to staff, as where the course teaches and assesses it. Ask: \"Which underpinning subject do you find hardest to use on the ward, and why?\" Avoid reading the table aloud and holding anyone to another award's column as if it were their minimum."
- statement: qaa/veterinary-nursing-2024/4.2.b25.masters
  forPractitioner: { text: "The minimum for a master's degree (FHEQ level 7, SCQF level 11): teach and assess so that every graduate should be able to be aware of the knowledge, skills and behaviours expected of professional practitioners.", rewrite: light, force: threshold, status: drafted }
  forBeneficiary: { text: "As the minimum for your master's degree, you should be able to be aware of the knowledge, skills and behaviours expected of professional practitioners.", rewrite: full, force: threshold, status: drafted }
  author-agent-written: "Treat this as a threshold standard: the minimum a master's degree in veterinary nursing asks at FHEQ level 7, SCQF level 11, on core subject knowledge. Cite it as QAA (2024), Veterinary Nursing Subject Benchmark Statement, section 4, table \"Subject knowledge, understanding and associated skills\", master's degree column. Do not present it as an RCVS or regulatory requirement, or as holding for another award. Set it beside the same row's other columns (4.2.b25.foundation, 4.2.b25) and the framework descriptor qaa/fheq-2024/4.17.b1 (spine:7, strand:knowledge)."
  author-agent-dialogue: "Raise it when a master's student or tutor asks what core subject knowledge should look like by the end of the master's degree. Put it plainly: to a student, that by the end you should be able to be aware of the knowledge, skills and behaviours expected of professional practitioners; to staff, as where the course teaches and assesses it. Ask: \"Which underpinning subject do you find hardest to use on the ward, and why?\" Avoid reading the table aloud and holding anyone to another award's column as if it were their minimum."
- statement: qaa/veterinary-nursing-2024/4.2.b26
  forPractitioner: { text: "The minimum for a honours degree (FHEQ level 6, SCQF level 10): teach and assess so that every graduate should be able to critically analyse how experience and values differ across groups and individuals to further anti-discriminatory practice.", rewrite: light, force: threshold, status: drafted }
  forBeneficiary: { text: "As the minimum for your honours degree, you should be able to critically analyse how experience and values differ across groups and individuals to further anti-discriminatory practice.", rewrite: full, force: threshold, status: drafted }
  author-agent-written: "Treat this as a threshold standard: the minimum a honours degree in veterinary nursing asks at FHEQ level 6, SCQF level 10, on cultural awareness and anti-discriminatory practice. Cite it as QAA (2024), Veterinary Nursing Subject Benchmark Statement, section 4, table \"Subject knowledge, understanding and associated skills\", honours degree column. Do not present it as an RCVS or regulatory requirement, or as holding for another award. Set it beside the same row's other columns (4.2.b26.foundation, 4.2.b26.masters) and the framework descriptor qaa/fheq-2024/4.15.b7 and qaa/fqheis-2024/4.16.b6 (spine:6, strand:thinking)."
  author-agent-dialogue: "Raise it when an honours student or tutor asks what cultural awareness and anti-discriminatory practice should look like by the end of the honours degree. Put it plainly: to a student, that by the end you should be able to critically analyse how experience and values differ across groups and individuals to further anti-discriminatory practice; to staff, as where the course teaches and assesses it. Ask: \"How might a client's background shape what they need from you, and how would you find out?\" Avoid reading the table aloud and holding anyone to another award's column as if it were their minimum."
- statement: qaa/veterinary-nursing-2024/4.2.b26.foundation
  forPractitioner: { text: "The minimum for a foundation degree (FHEQ level 5): teach and assess so that every graduate should be able to show cultural awareness and model the behaviours that anti-discriminatory practice depends on.", rewrite: light, force: threshold, status: drafted }
  forBeneficiary: { text: "As the minimum for your foundation degree, you should be able to show cultural awareness and model the behaviours that anti-discriminatory practice depends on.", rewrite: full, force: threshold, status: drafted }
  author-agent-written: "Treat this as a threshold standard: the minimum a foundation degree in veterinary nursing asks at FHEQ level 5, on cultural awareness and anti-discriminatory practice. Cite it as QAA (2024), Veterinary Nursing Subject Benchmark Statement, section 4, table \"Subject knowledge, understanding and associated skills\", foundation degree column. Do not present it as an RCVS or regulatory requirement, or as holding for another award. Set it beside the same row's other columns (4.2.b26, 4.2.b26.masters) and the framework descriptor qaa/fheq-2024/4.12.b5 (spine:5, strand:thinking)."
  author-agent-dialogue: "Raise it when a foundation degree student or tutor asks what cultural awareness and anti-discriminatory practice should look like by the end of the foundation degree. Put it plainly: to a student, that by the end you should be able to show cultural awareness and model the behaviours that anti-discriminatory practice depends on; to staff, as where the course teaches and assesses it. Ask: \"How might a client's background shape what they need from you, and how would you find out?\" Avoid reading the table aloud and holding anyone to another award's column as if it were their minimum."
- statement: qaa/veterinary-nursing-2024/4.2.b26.masters
  forPractitioner: { text: "The minimum for a master's degree (FHEQ level 7, SCQF level 11): teach and assess so that every graduate should be able to apply inclusive and adaptive skills in pursuing anti-discriminatory practice.", rewrite: light, force: threshold, status: drafted }
  forBeneficiary: { text: "As the minimum for your master's degree, you should be able to apply inclusive and adaptive skills in pursuing anti-discriminatory practice.", rewrite: full, force: threshold, status: drafted }
  author-agent-written: "Treat this as a threshold standard: the minimum a master's degree in veterinary nursing asks at FHEQ level 7, SCQF level 11, on cultural awareness and anti-discriminatory practice. Cite it as QAA (2024), Veterinary Nursing Subject Benchmark Statement, section 4, table \"Subject knowledge, understanding and associated skills\", master's degree column. Do not present it as an RCVS or regulatory requirement, or as holding for another award. Set it beside the same row's other columns (4.2.b26.foundation, 4.2.b26) and the framework descriptor qaa/fheq-2024/4.17.b5 (spine:7, strand:thinking)."
  author-agent-dialogue: "Raise it when a master's student or tutor asks what cultural awareness and anti-discriminatory practice should look like by the end of the master's degree. Put it plainly: to a student, that by the end you should be able to apply inclusive and adaptive skills in pursuing anti-discriminatory practice; to staff, as where the course teaches and assesses it. Ask: \"How might a client's background shape what they need from you, and how would you find out?\" Avoid reading the table aloud and holding anyone to another award's column as if it were their minimum."
- statement: qaa/veterinary-nursing-2024/4.2.b27
  forPractitioner: { text: "The minimum for a honours degree (FHEQ level 6, SCQF level 10): teach and assess so that every graduate should be able to present strong evidence clearly in writing and speech, using technology that supports sound decisions.", rewrite: light, force: threshold, status: drafted }
  forBeneficiary: { text: "As the minimum for your honours degree, you should be able to present strong evidence clearly in writing and speech, using technology that supports sound decisions.", rewrite: full, force: threshold, status: drafted }
  author-agent-written: "Treat this as a threshold standard: the minimum a honours degree in veterinary nursing asks at FHEQ level 6, SCQF level 10, on communication and evidence-based decisions. Cite it as QAA (2024), Veterinary Nursing Subject Benchmark Statement, section 4, table \"Subject knowledge, understanding and associated skills\", honours degree column. Do not present it as an RCVS or regulatory requirement, or as holding for another award. Set it beside the same row's other columns (4.2.b27.foundation, 4.2.b27.masters) and the framework descriptor qaa/fheq-2024/4.15.b8 and qaa/fqheis-2024/4.16.b7 (spine:6, strand:communication)."
  author-agent-dialogue: "Raise it when an honours student or tutor asks what communication and evidence-based decisions should look like by the end of the honours degree. Put it plainly: to a student, that by the end you should be able to present strong evidence clearly in writing and speech, using technology that supports sound decisions; to staff, as where the course teaches and assesses it. Ask: \"How would you explain this decision to an owner, and how to a vet?\" Avoid reading the table aloud and holding anyone to another award's column as if it were their minimum."
- statement: qaa/veterinary-nursing-2024/4.2.b27.foundation
  forPractitioner: { text: "The minimum for a foundation degree (FHEQ level 5): teach and assess so that every graduate should be able to communicate clearly and articulately with many kinds of audience through a range of media.", rewrite: light, force: threshold, status: drafted }
  forBeneficiary: { text: "As the minimum for your foundation degree, you should be able to communicate clearly and articulately with many kinds of audience through a range of media.", rewrite: full, force: threshold, status: drafted }
  author-agent-written: "Treat this as a threshold standard: the minimum a foundation degree in veterinary nursing asks at FHEQ level 5, on communication and evidence-based decisions. Cite it as QAA (2024), Veterinary Nursing Subject Benchmark Statement, section 4, table \"Subject knowledge, understanding and associated skills\", foundation degree column. Do not present it as an RCVS or regulatory requirement, or as holding for another award. Set it beside the same row's other columns (4.2.b27, 4.2.b27.masters) and the framework descriptor qaa/fheq-2024/4.12.b6 (spine:5, strand:communication)."
  author-agent-dialogue: "Raise it when a foundation degree student or tutor asks what communication and evidence-based decisions should look like by the end of the foundation degree. Put it plainly: to a student, that by the end you should be able to communicate clearly and articulately with many kinds of audience through a range of media; to staff, as where the course teaches and assesses it. Ask: \"How would you explain this decision to an owner, and how to a vet?\" Avoid reading the table aloud and holding anyone to another award's column as if it were their minimum."
- statement: qaa/veterinary-nursing-2024/4.2.b27.masters
  forPractitioner: { text: "The minimum for a master's degree (FHEQ level 7, SCQF level 11): teach and assess so that every graduate should be able to show decision-making that uses evidence and is critical and original in its thinking.", rewrite: light, force: threshold, status: drafted }
  forBeneficiary: { text: "As the minimum for your master's degree, you should be able to show decision-making that uses evidence and is critical and original in its thinking.", rewrite: full, force: threshold, status: drafted }
  author-agent-written: "Treat this as a threshold standard: the minimum a master's degree in veterinary nursing asks at FHEQ level 7, SCQF level 11, on communication and evidence-based decisions. Cite it as QAA (2024), Veterinary Nursing Subject Benchmark Statement, section 4, table \"Subject knowledge, understanding and associated skills\", master's degree column. Do not present it as an RCVS or regulatory requirement, or as holding for another award. Set it beside the same row's other columns (4.2.b27.foundation, 4.2.b27) and the framework descriptor qaa/fheq-2024/4.17.b5 (spine:7, strand:communication)."
  author-agent-dialogue: "Raise it when a master's student or tutor asks what communication and evidence-based decisions should look like by the end of the master's degree. Put it plainly: to a student, that by the end you should be able to show decision-making that uses evidence and is critical and original in its thinking; to staff, as where the course teaches and assesses it. Ask: \"How would you explain this decision to an owner, and how to a vet?\" Avoid reading the table aloud and holding anyone to another award's column as if it were their minimum."
- statement: qaa/veterinary-nursing-2024/4.2.b28
  forPractitioner: { text: "The minimum for a honours degree (FHEQ level 6, SCQF level 10): teach and assess so that every graduate should be able to strengthen therapeutic relationships with a wide range of clients by creative use of concepts and theory and by critical reflection.", rewrite: light, force: threshold, status: drafted }
  forBeneficiary: { text: "As the minimum for your honours degree, you should be able to strengthen therapeutic relationships with a wide range of clients by creative use of concepts and theory and by critical reflection.", rewrite: full, force: threshold, status: drafted }
  author-agent-written: "Treat this as a threshold standard: the minimum a honours degree in veterinary nursing asks at FHEQ level 6, SCQF level 10, on therapeutic client relationships. Cite it as QAA (2024), Veterinary Nursing Subject Benchmark Statement, section 4, table \"Subject knowledge, understanding and associated skills\", honours degree column. Do not present it as an RCVS or regulatory requirement, or as holding for another award. Set it beside the same row's other columns (4.2.b28.foundation, 4.2.b28.masters) and the framework descriptor qaa/fheq-2024/4.15.b8 and qaa/fqheis-2024/4.16.b7 (spine:6, strand:communication)."
  author-agent-dialogue: "Raise it when an honours student or tutor asks what therapeutic client relationships should look like by the end of the honours degree. Put it plainly: to a student, that by the end you should be able to strengthen therapeutic relationships with a wide range of clients by creative use of concepts and theory and by critical reflection; to staff, as where the course teaches and assesses it. Ask: \"What helps an anxious owner trust you, and what gets in the way?\" Avoid reading the table aloud and holding anyone to another award's column as if it were their minimum."
- statement: qaa/veterinary-nursing-2024/4.2.b28.foundation
  forPractitioner: { text: "The minimum for a foundation degree (FHEQ level 5): teach and assess so that every graduate should be able to build and keep therapeutic relationships with clients, taking account of diversity, settings and other influences.", rewrite: light, force: threshold, status: drafted }
  forBeneficiary: { text: "As the minimum for your foundation degree, you should be able to build and keep therapeutic relationships with clients, taking account of diversity, settings and other influences.", rewrite: full, force: threshold, status: drafted }
  author-agent-written: "Treat this as a threshold standard: the minimum a foundation degree in veterinary nursing asks at FHEQ level 5, on therapeutic client relationships. Cite it as QAA (2024), Veterinary Nursing Subject Benchmark Statement, section 4, table \"Subject knowledge, understanding and associated skills\", foundation degree column. Do not present it as an RCVS or regulatory requirement, or as holding for another award. Set it beside the same row's other columns (4.2.b28, 4.2.b28.masters) and the framework descriptor qaa/fheq-2024/4.12.b6 (spine:5, strand:communication)."
  author-agent-dialogue: "Raise it when a foundation degree student or tutor asks what therapeutic client relationships should look like by the end of the foundation degree. Put it plainly: to a student, that by the end you should be able to build and keep therapeutic relationships with clients, taking account of diversity, settings and other influences; to staff, as where the course teaches and assesses it. Ask: \"What helps an anxious owner trust you, and what gets in the way?\" Avoid reading the table aloud and holding anyone to another award's column as if it were their minimum."
- statement: qaa/veterinary-nursing-2024/4.2.b28.masters
  forPractitioner: { text: "The minimum for a master's degree (FHEQ level 7, SCQF level 11): teach and assess so that every graduate should be able to show inclusive, adaptive behaviour in professional relationships.", rewrite: light, force: threshold, status: drafted }
  forBeneficiary: { text: "As the minimum for your master's degree, you should be able to show inclusive, adaptive behaviour in professional relationships.", rewrite: full, force: threshold, status: drafted }
  author-agent-written: "Treat this as a threshold standard: the minimum a master's degree in veterinary nursing asks at FHEQ level 7, SCQF level 11, on therapeutic client relationships. Cite it as QAA (2024), Veterinary Nursing Subject Benchmark Statement, section 4, table \"Subject knowledge, understanding and associated skills\", master's degree column. Do not present it as an RCVS or regulatory requirement, or as holding for another award. Set it beside the same row's other columns (4.2.b28.foundation, 4.2.b28) and the framework descriptor qaa/fheq-2024/4.17.b5 (spine:7, strand:communication)."
  author-agent-dialogue: "Raise it when a master's student or tutor asks what therapeutic client relationships should look like by the end of the master's degree. Put it plainly: to a student, that by the end you should be able to show inclusive, adaptive behaviour in professional relationships; to staff, as where the course teaches and assesses it. Ask: \"What helps an anxious owner trust you, and what gets in the way?\" Avoid reading the table aloud and holding anyone to another award's column as if it were their minimum."
- statement: qaa/veterinary-nursing-2024/4.2.b29
  forPractitioner: { text: "The minimum for a honours degree (FHEQ level 6, SCQF level 10): teach and assess so that every graduate should be able to show robust, up-to-date, evidence-based veterinary nursing, using critical judgement to evaluate, guide decisions and combine new approaches that raise the quality of care.", rewrite: light, force: threshold, status: drafted }
  forBeneficiary: { text: "As the minimum for your honours degree, you should be able to show robust, up-to-date, evidence-based veterinary nursing, using critical judgement to evaluate, guide decisions and combine new approaches that raise the quality of care.", rewrite: full, force: threshold, status: drafted }
  author-agent-written: "Treat this as a threshold standard: the minimum a honours degree in veterinary nursing asks at FHEQ level 6, SCQF level 10, on contemporary evidence-based nursing. Cite it as QAA (2024), Veterinary Nursing Subject Benchmark Statement, section 4, table \"Subject knowledge, understanding and associated skills\", honours degree column. Do not present it as an RCVS or regulatory requirement, or as holding for another award. Set it beside the same row's other columns (4.2.b29.foundation, 4.2.b29.masters) and the framework descriptor qaa/fheq-2024/4.15.b6 and qaa/fqheis-2024/4.16.b4 (spine:6, strand:application)."
  author-agent-dialogue: "Raise it when an honours student or tutor asks what contemporary evidence-based nursing should look like by the end of the honours degree. Put it plainly: to a student, that by the end you should be able to show robust, up-to-date, evidence-based veterinary nursing, using critical judgement to evaluate, guide decisions and combine new approaches that raise the quality of care; to staff, as where the course teaches and assesses it. Ask: \"What part of your nursing have you updated because of newer evidence?\" Avoid reading the table aloud and holding anyone to another award's column as if it were their minimum."
- statement: qaa/veterinary-nursing-2024/4.2.b29.foundation
  forPractitioner: { text: "The minimum for a foundation degree (FHEQ level 5): teach and assess so that every graduate should be able to reflect on and give up-to-date, evidence-based veterinary nursing through practical skill and applied knowledge.", rewrite: light, force: threshold, status: drafted }
  forBeneficiary: { text: "As the minimum for your foundation degree, you should be able to reflect on and give up-to-date, evidence-based veterinary nursing through practical skill and applied knowledge.", rewrite: full, force: threshold, status: drafted }
  author-agent-written: "Treat this as a threshold standard: the minimum a foundation degree in veterinary nursing asks at FHEQ level 5, on contemporary evidence-based nursing. Cite it as QAA (2024), Veterinary Nursing Subject Benchmark Statement, section 4, table \"Subject knowledge, understanding and associated skills\", foundation degree column. Do not present it as an RCVS or regulatory requirement, or as holding for another award. Set it beside the same row's other columns (4.2.b29, 4.2.b29.masters) and the framework descriptor qaa/fheq-2024/4.12.b2 (spine:5, strand:application)."
  author-agent-dialogue: "Raise it when a foundation degree student or tutor asks what contemporary evidence-based nursing should look like by the end of the foundation degree. Put it plainly: to a student, that by the end you should be able to reflect on and give up-to-date, evidence-based veterinary nursing through practical skill and applied knowledge; to staff, as where the course teaches and assesses it. Ask: \"What part of your nursing have you updated because of newer evidence?\" Avoid reading the table aloud and holding anyone to another award's column as if it were their minimum."
- statement: qaa/veterinary-nursing-2024/4.2.b29.masters
  forPractitioner: { text: "The minimum for a master's degree (FHEQ level 7, SCQF level 11): teach and assess so that every graduate should be able to express judgements through careful, evidence-based, critical reasoning grounded in reflection.", rewrite: light, force: threshold, status: drafted }
  forBeneficiary: { text: "As the minimum for your master's degree, you should be able to express judgements through careful, evidence-based, critical reasoning grounded in reflection.", rewrite: full, force: threshold, status: drafted }
  author-agent-written: "Treat this as a threshold standard: the minimum a master's degree in veterinary nursing asks at FHEQ level 7, SCQF level 11, on contemporary evidence-based nursing. Cite it as QAA (2024), Veterinary Nursing Subject Benchmark Statement, section 4, table \"Subject knowledge, understanding and associated skills\", master's degree column. Do not present it as an RCVS or regulatory requirement, or as holding for another award. Set it beside the same row's other columns (4.2.b29.foundation, 4.2.b29) and the framework descriptor qaa/fheq-2024/4.17.b3 (spine:7, strand:application)."
  author-agent-dialogue: "Raise it when a master's student or tutor asks what contemporary evidence-based nursing should look like by the end of the master's degree. Put it plainly: to a student, that by the end you should be able to express judgements through careful, evidence-based, critical reasoning grounded in reflection; to staff, as where the course teaches and assesses it. Ask: \"What part of your nursing have you updated because of newer evidence?\" Avoid reading the table aloud and holding anyone to another award's column as if it were their minimum."
- statement: qaa/veterinary-nursing-2024/4.2.b30
  forPractitioner: { text: "The minimum for a honours degree (FHEQ level 6, SCQF level 10): teach and assess so that every graduate should be able to apply critical analysis and synthesis, using strong evidence and data to build new theory in pursuit of excellent care.", rewrite: light, force: threshold, status: drafted }
  forBeneficiary: { text: "As the minimum for your honours degree, you should be able to apply critical analysis and synthesis, using strong evidence and data to build new theory in pursuit of excellent care.", rewrite: full, force: threshold, status: drafted }
  author-agent-written: "Treat this as a threshold standard: the minimum a honours degree in veterinary nursing asks at FHEQ level 6, SCQF level 10, on evidence and data in judgement. Cite it as QAA (2024), Veterinary Nursing Subject Benchmark Statement, section 4, table \"Subject knowledge, understanding and associated skills\", honours degree column. Do not present it as an RCVS or regulatory requirement, or as holding for another award. Set it beside the same row's other columns (4.2.b30.foundation, 4.2.b30.masters) and the framework descriptor qaa/fheq-2024/4.15.b7 and qaa/fqheis-2024/4.16.b6 (spine:6, strand:thinking)."
  author-agent-dialogue: "Raise it when an honours student or tutor asks what evidence and data in judgement should look like by the end of the honours degree. Put it plainly: to a student, that by the end you should be able to apply critical analysis and synthesis, using strong evidence and data to build new theory in pursuit of excellent care; to staff, as where the course teaches and assesses it. Ask: \"Which data do you trust most when judging a patient's progress, and why?\" Avoid reading the table aloud and holding anyone to another award's column as if it were their minimum."
- statement: qaa/veterinary-nursing-2024/4.2.b30.foundation
  forPractitioner: { text: "The minimum for a foundation degree (FHEQ level 5): teach and assess so that every graduate should be able to use evidence, data and technology to inform judgements and improve veterinary care.", rewrite: light, force: threshold, status: drafted }
  forBeneficiary: { text: "As the minimum for your foundation degree, you should be able to use evidence, data and technology to inform judgements and improve veterinary care.", rewrite: full, force: threshold, status: drafted }
  author-agent-written: "Treat this as a threshold standard: the minimum a foundation degree in veterinary nursing asks at FHEQ level 5, on evidence and data in judgement. Cite it as QAA (2024), Veterinary Nursing Subject Benchmark Statement, section 4, table \"Subject knowledge, understanding and associated skills\", foundation degree column. Do not present it as an RCVS or regulatory requirement, or as holding for another award. Set it beside the same row's other columns (4.2.b30, 4.2.b30.masters) and the framework descriptor qaa/fheq-2024/4.12.b5 (spine:5, strand:thinking)."
  author-agent-dialogue: "Raise it when a foundation degree student or tutor asks what evidence and data in judgement should look like by the end of the foundation degree. Put it plainly: to a student, that by the end you should be able to use evidence, data and technology to inform judgements and improve veterinary care; to staff, as where the course teaches and assesses it. Ask: \"Which data do you trust most when judging a patient's progress, and why?\" Avoid reading the table aloud and holding anyone to another award's column as if it were their minimum."
- statement: qaa/veterinary-nursing-2024/4.2.b30.masters
  forPractitioner: { text: "The minimum for a master's degree (FHEQ level 7, SCQF level 11): teach and assess so that every graduate should be able to apply evaluation and critical reasoning to justify evidence-based judgements that advance excellent care.", rewrite: light, force: threshold, status: drafted }
  forBeneficiary: { text: "As the minimum for your master's degree, you should be able to apply evaluation and critical reasoning to justify evidence-based judgements that advance excellent care.", rewrite: full, force: threshold, status: drafted }
  author-agent-written: "Treat this as a threshold standard: the minimum a master's degree in veterinary nursing asks at FHEQ level 7, SCQF level 11, on evidence and data in judgement. Cite it as QAA (2024), Veterinary Nursing Subject Benchmark Statement, section 4, table \"Subject knowledge, understanding and associated skills\", master's degree column. Do not present it as an RCVS or regulatory requirement, or as holding for another award. Set it beside the same row's other columns (4.2.b30.foundation, 4.2.b30) and the framework descriptor qaa/fheq-2024/4.17.b5 (spine:7, strand:thinking)."
  author-agent-dialogue: "Raise it when a master's student or tutor asks what evidence and data in judgement should look like by the end of the master's degree. Put it plainly: to a student, that by the end you should be able to apply evaluation and critical reasoning to justify evidence-based judgements that advance excellent care; to staff, as where the course teaches and assesses it. Ask: \"Which data do you trust most when judging a patient's progress, and why?\" Avoid reading the table aloud and holding anyone to another award's column as if it were their minimum."
- statement: qaa/veterinary-nursing-2024/4.2.b31
  forPractitioner: { text: "The minimum for a honours degree (FHEQ level 6, SCQF level 10): teach and assess so that every graduate should be able to reflect on their own improvement through critical evaluation and analysis, weighing the effect on colleagues, to strengthen professional practice.", rewrite: light, force: threshold, status: drafted }
  forBeneficiary: { text: "As the minimum for your honours degree, you should be able to reflect on your own improvement through critical evaluation and analysis, weighing the effect on colleagues, to strengthen professional practice.", rewrite: full, force: threshold, status: drafted }
  author-agent-written: "Treat this as a threshold standard: the minimum a honours degree in veterinary nursing asks at FHEQ level 6, SCQF level 10, on reflection for self-improvement. Cite it as QAA (2024), Veterinary Nursing Subject Benchmark Statement, section 4, table \"Subject knowledge, understanding and associated skills\", honours degree column. Do not present it as an RCVS or regulatory requirement, or as holding for another award. Set it beside the same row's other columns (4.2.b31.foundation, 4.2.b31.masters) and the framework descriptor qaa/fheq-2024/4.15.b9.2 and qaa/fqheis-2024/4.16.b9.2 (spine:6, strand:autonomy)."
  author-agent-dialogue: "Raise it when an honours student or tutor asks what reflection for self-improvement should look like by the end of the honours degree. Put it plainly: to a student, that by the end you should be able to reflect on your own improvement through critical evaluation and analysis, weighing the effect on colleagues, to strengthen professional practice; to staff, as where the course teaches and assesses it. Ask: \"What feedback has most changed your practice, and how did you act on it?\" Avoid reading the table aloud and holding anyone to another award's column as if it were their minimum."
- statement: qaa/veterinary-nursing-2024/4.2.b31.foundation
  forPractitioner: { text: "The minimum for a foundation degree (FHEQ level 5): teach and assess so that every graduate should be able to use introspection and reflection to improve professional practice.", rewrite: light, force: threshold, status: drafted }
  forBeneficiary: { text: "As the minimum for your foundation degree, you should be able to use introspection and reflection to improve professional practice.", rewrite: full, force: threshold, status: drafted }
  author-agent-written: "Treat this as a threshold standard: the minimum a foundation degree in veterinary nursing asks at FHEQ level 5, on reflection for self-improvement. Cite it as QAA (2024), Veterinary Nursing Subject Benchmark Statement, section 4, table \"Subject knowledge, understanding and associated skills\", foundation degree column. Do not present it as an RCVS or regulatory requirement, or as holding for another award. Set it beside the same row's other columns (4.2.b31, 4.2.b31.masters) and the framework descriptor qaa/fheq-2024/4.12.b8 (spine:5, strand:autonomy)."
  author-agent-dialogue: "Raise it when a foundation degree student or tutor asks what reflection for self-improvement should look like by the end of the foundation degree. Put it plainly: to a student, that by the end you should be able to use introspection and reflection to improve professional practice; to staff, as where the course teaches and assesses it. Ask: \"What feedback has most changed your practice, and how did you act on it?\" Avoid reading the table aloud and holding anyone to another award's column as if it were their minimum."
- statement: qaa/veterinary-nursing-2024/4.2.b31.masters
  forPractitioner: { text: "The minimum for a master's degree (FHEQ level 7, SCQF level 11): teach and assess so that every graduate should be able to take an evaluative, critically reflective approach to improving themselves in professional practice.", rewrite: light, force: threshold, status: drafted }
  forBeneficiary: { text: "As the minimum for your master's degree, you should be able to take an evaluative, critically reflective approach to improving yourself in professional practice.", rewrite: full, force: threshold, status: drafted }
  author-agent-written: "Treat this as a threshold standard: the minimum a master's degree in veterinary nursing asks at FHEQ level 7, SCQF level 11, on reflection for self-improvement. Cite it as QAA (2024), Veterinary Nursing Subject Benchmark Statement, section 4, table \"Subject knowledge, understanding and associated skills\", master's degree column. Do not present it as an RCVS or regulatory requirement, or as holding for another award. Set it beside the same row's other columns (4.2.b31.foundation, 4.2.b31) and the framework descriptor qaa/fheq-2024/4.17.b8.2 (spine:7, strand:autonomy)."
  author-agent-dialogue: "Raise it when a master's student or tutor asks what reflection for self-improvement should look like by the end of the master's degree. Put it plainly: to a student, that by the end you should be able to take an evaluative, critically reflective approach to improving yourself in professional practice; to staff, as where the course teaches and assesses it. Ask: \"What feedback has most changed your practice, and how did you act on it?\" Avoid reading the table aloud and holding anyone to another award's column as if it were their minimum."
- statement: qaa/veterinary-nursing-2024/4.2.b32
  forPractitioner: { text: "The minimum for a honours degree (FHEQ level 6, SCQF level 10): teach and assess so that every graduate should be able to manage themselves, their practice and that of others in line with the professional code of conduct, and weigh up critically, and reflect on, their own strengths and limits.", rewrite: light, force: threshold, status: drafted }
  forBeneficiary: { text: "As the minimum for your honours degree, you should be able to manage yourself, your practice and that of others in line with the professional code of conduct, and weigh up critically, and reflect on, your own strengths and limits.", rewrite: full, force: threshold, status: drafted }
  author-agent-written: "Treat this as a threshold standard: the minimum a honours degree in veterinary nursing asks at FHEQ level 6, SCQF level 10, on managing self and others under the code. Cite it as QAA (2024), Veterinary Nursing Subject Benchmark Statement, section 4, table \"Working as a professional veterinary nurse: expectations\", honours degree column. Do not present it as an RCVS or regulatory requirement, or as holding for another award. Set it beside the same row's other columns (4.2.b32.foundation, 4.2.b32.masters) and the framework descriptor qaa/fheq-2024/4.15.b9.2 and qaa/fqheis-2024/4.16.b9.2 (spine:6, strand:autonomy)."
  author-agent-dialogue: "Raise it when an honours student or tutor asks what managing self and others under the code should look like by the end of the honours degree. Put it plainly: to a student, that by the end you should be able to manage yourself, your practice and that of others in line with the professional code of conduct, and weigh up critically, and reflect on, your own strengths and limits; to staff, as where the course teaches and assesses it. Ask: \"Where are the limits of what you can safely do on your own, and how do you know?\" Avoid reading the table aloud and holding anyone to another award's column as if it were their minimum."
- statement: qaa/veterinary-nursing-2024/4.2.b32.foundation
  forPractitioner: { text: "The minimum for a foundation degree (FHEQ level 5): teach and assess so that every graduate should be able to manage themselves, their practice and that of others in line with the professional code of conduct, knowing their own strengths and limits.", rewrite: light, force: threshold, status: drafted }
  forBeneficiary: { text: "As the minimum for your foundation degree, you should be able to manage yourself, your practice and that of others in line with the professional code of conduct, knowing your own strengths and limits.", rewrite: full, force: threshold, status: drafted }
  author-agent-written: "Treat this as a threshold standard: the minimum a foundation degree in veterinary nursing asks at FHEQ level 5, on managing self and others under the code. Cite it as QAA (2024), Veterinary Nursing Subject Benchmark Statement, section 4, table \"Working as a professional veterinary nurse: expectations\", foundation degree column. Do not present it as an RCVS or regulatory requirement, or as holding for another award. Set it beside the same row's other columns (4.2.b32, 4.2.b32.masters) and the framework descriptor qaa/fheq-2024/4.12.b8 (spine:5, strand:autonomy)."
  author-agent-dialogue: "Raise it when a foundation degree student or tutor asks what managing self and others under the code should look like by the end of the foundation degree. Put it plainly: to a student, that by the end you should be able to manage yourself, your practice and that of others in line with the professional code of conduct, knowing your own strengths and limits; to staff, as where the course teaches and assesses it. Ask: \"Where are the limits of what you can safely do on your own, and how do you know?\" Avoid reading the table aloud and holding anyone to another award's column as if it were their minimum."
- statement: qaa/veterinary-nursing-2024/4.2.b32.masters
  forPractitioner: { text: "The minimum for a master's degree (FHEQ level 7, SCQF level 11): teach and assess so that every graduate should be able to manage themselves, their practice and that of others in line with the professional code of conduct, and critically evaluate and reflect on why teaching and promoting those expectations matters.", rewrite: light, force: threshold, status: drafted }
  forBeneficiary: { text: "As the minimum for your master's degree, you should be able to manage yourself, your practice and that of others in line with the professional code of conduct, and critically evaluate and reflect on why teaching and promoting those expectations matters.", rewrite: full, force: threshold, status: drafted }
  author-agent-written: "Treat this as a threshold standard: the minimum a master's degree in veterinary nursing asks at FHEQ level 7, SCQF level 11, on managing self and others under the code. Cite it as QAA (2024), Veterinary Nursing Subject Benchmark Statement, section 4, table \"Working as a professional veterinary nurse: expectations\", master's degree column. Do not present it as an RCVS or regulatory requirement, or as holding for another award. Set it beside the same row's other columns (4.2.b32.foundation, 4.2.b32) and the framework descriptor qaa/fheq-2024/4.17.b8.2 (spine:7, strand:autonomy)."
  author-agent-dialogue: "Raise it when a master's student or tutor asks what managing self and others under the code should look like by the end of the master's degree. Put it plainly: to a student, that by the end you should be able to manage yourself, your practice and that of others in line with the professional code of conduct, and critically evaluate and reflect on why teaching and promoting those expectations matters; to staff, as where the course teaches and assesses it. Ask: \"Where are the limits of what you can safely do on your own, and how do you know?\" Avoid reading the table aloud and holding anyone to another award's column as if it were their minimum."
- statement: qaa/veterinary-nursing-2024/4.2.b33
  forPractitioner: { text: "The minimum for a honours degree (FHEQ level 6, SCQF level 10): teach and assess so that every graduate should be able to choose and apply knowledge and skills across different clinical settings and unforeseen situations.", rewrite: light, force: threshold, status: drafted }
  forBeneficiary: { text: "As the minimum for your honours degree, you should be able to choose and apply knowledge and skills across different clinical settings and unforeseen situations.", rewrite: full, force: threshold, status: drafted }
  author-agent-written: "Treat this as a threshold standard: the minimum a honours degree in veterinary nursing asks at FHEQ level 6, SCQF level 10, on applying knowledge across clinical settings. Cite it as QAA (2024), Veterinary Nursing Subject Benchmark Statement, section 4, table \"Working as a professional veterinary nurse: expectations\", honours degree column. Do not present it as an RCVS or regulatory requirement, or as holding for another award. Set it beside the same row's other columns (4.2.b33.foundation, 4.2.b33.masters) and the framework descriptor qaa/fheq-2024/4.15.b6 and qaa/fqheis-2024/4.16.b4 (spine:6, strand:application)."
  author-agent-dialogue: "Raise it when an honours student or tutor asks what applying knowledge across clinical settings should look like by the end of the honours degree. Put it plainly: to a student, that by the end you should be able to choose and apply knowledge and skills across different clinical settings and unforeseen situations; to staff, as where the course teaches and assesses it. Ask: \"What happened the last time a case went off script, and what did you draw on?\" Avoid reading the table aloud and holding anyone to another award's column as if it were their minimum."
- statement: qaa/veterinary-nursing-2024/4.2.b33.foundation
  forPractitioner: { text: "The minimum for a foundation degree (FHEQ level 5): teach and assess so that every graduate should be able to choose and apply knowledge and skills across different clinical settings and unforeseen situations.", rewrite: light, force: threshold, status: drafted }
  forBeneficiary: { text: "As the minimum for your foundation degree, you should be able to choose and apply knowledge and skills across different clinical settings and unforeseen situations.", rewrite: full, force: threshold, status: drafted }
  author-agent-written: "Treat this as a threshold standard: the minimum a foundation degree in veterinary nursing asks at FHEQ level 5, on applying knowledge across clinical settings. Cite it as QAA (2024), Veterinary Nursing Subject Benchmark Statement, section 4, table \"Working as a professional veterinary nurse: expectations\", foundation degree column. Do not present it as an RCVS or regulatory requirement, or as holding for another award. Set it beside the same row's other columns (4.2.b33, 4.2.b33.masters) and the framework descriptor qaa/fheq-2024/4.12.b2 (spine:5, strand:application)."
  author-agent-dialogue: "Raise it when a foundation degree student or tutor asks what applying knowledge across clinical settings should look like by the end of the foundation degree. Put it plainly: to a student, that by the end you should be able to choose and apply knowledge and skills across different clinical settings and unforeseen situations; to staff, as where the course teaches and assesses it. Ask: \"What happened the last time a case went off script, and what did you draw on?\" Avoid reading the table aloud and holding anyone to another award's column as if it were their minimum."
- statement: qaa/veterinary-nursing-2024/4.2.b33.masters
  forPractitioner: { text: "The minimum for a master's degree (FHEQ level 7, SCQF level 11): teach and assess so that every graduate should be able to extend knowledge and skills by contributing to evidence-based veterinary nursing across different clinical settings and unforeseen situations.", rewrite: light, force: threshold, status: drafted }
  forBeneficiary: { text: "As the minimum for your master's degree, you should be able to extend knowledge and skills by contributing to evidence-based veterinary nursing across different clinical settings and unforeseen situations.", rewrite: full, force: threshold, status: drafted }
  author-agent-written: "Treat this as a threshold standard: the minimum a master's degree in veterinary nursing asks at FHEQ level 7, SCQF level 11, on applying knowledge across clinical settings. Cite it as QAA (2024), Veterinary Nursing Subject Benchmark Statement, section 4, table \"Working as a professional veterinary nurse: expectations\", master's degree column. Do not present it as an RCVS or regulatory requirement, or as holding for another award. Set it beside the same row's other columns (4.2.b33.foundation, 4.2.b33) and the framework descriptor qaa/fheq-2024/4.17.b3 (spine:7, strand:application)."
  author-agent-dialogue: "Raise it when a master's student or tutor asks what applying knowledge across clinical settings should look like by the end of the master's degree. Put it plainly: to a student, that by the end you should be able to extend knowledge and skills by contributing to evidence-based veterinary nursing across different clinical settings and unforeseen situations; to staff, as where the course teaches and assesses it. Ask: \"What happened the last time a case went off script, and what did you draw on?\" Avoid reading the table aloud and holding anyone to another award's column as if it were their minimum."
- statement: qaa/veterinary-nursing-2024/4.2.b34
  forPractitioner: { text: "The minimum for a honours degree (FHEQ level 6, SCQF level 10): teach and assess so that every graduate should be able to put in place strategies that promote and evaluate collaboration with patients, clients and colleagues in identifying and giving therapeutic and preventive care.", rewrite: light, force: threshold, status: drafted }
  forBeneficiary: { text: "As the minimum for your honours degree, you should be able to put in place strategies that promote and evaluate collaboration with patients, clients and colleagues in identifying and giving therapeutic and preventive care.", rewrite: full, force: threshold, status: drafted }
  author-agent-written: "Treat this as a threshold standard: the minimum a honours degree in veterinary nursing asks at FHEQ level 6, SCQF level 10, on collaborative therapeutic and preventive care. Cite it as QAA (2024), Veterinary Nursing Subject Benchmark Statement, section 4, table \"Working as a professional veterinary nurse: expectations\", honours degree column. Do not present it as an RCVS or regulatory requirement, or as holding for another award. Set it beside the same row's other columns (4.2.b34.foundation, 4.2.b34.masters) and the framework descriptor qaa/fheq-2024/4.15.b6 and qaa/fqheis-2024/4.16.b4 (spine:6, strand:application)."
  author-agent-dialogue: "Raise it when an honours student or tutor asks what collaborative therapeutic and preventive care should look like by the end of the honours degree. Put it plainly: to a student, that by the end you should be able to put in place strategies that promote and evaluate collaboration with patients, clients and colleagues in identifying and giving therapeutic and preventive care; to staff, as where the course teaches and assesses it. Ask: \"How do you bring the client into decisions about preventive care?\" Avoid reading the table aloud and holding anyone to another award's column as if it were their minimum."
- statement: qaa/veterinary-nursing-2024/4.2.b34.foundation
  forPractitioner: { text: "The minimum for a foundation degree (FHEQ level 5): teach and assess so that every graduate should be able to work with clients and colleagues to identify and give the therapeutic and preventive care patients need.", rewrite: light, force: threshold, status: drafted }
  forBeneficiary: { text: "As the minimum for your foundation degree, you should be able to work with clients and colleagues to identify and give the therapeutic and preventive care patients need.", rewrite: full, force: threshold, status: drafted }
  author-agent-written: "Treat this as a threshold standard: the minimum a foundation degree in veterinary nursing asks at FHEQ level 5, on collaborative therapeutic and preventive care. Cite it as QAA (2024), Veterinary Nursing Subject Benchmark Statement, section 4, table \"Working as a professional veterinary nurse: expectations\", foundation degree column. Do not present it as an RCVS or regulatory requirement, or as holding for another award. Set it beside the same row's other columns (4.2.b34, 4.2.b34.masters) and the framework descriptor qaa/fheq-2024/4.12.b2 (spine:5, strand:application)."
  author-agent-dialogue: "Raise it when a foundation degree student or tutor asks what collaborative therapeutic and preventive care should look like by the end of the foundation degree. Put it plainly: to a student, that by the end you should be able to work with clients and colleagues to identify and give the therapeutic and preventive care patients need; to staff, as where the course teaches and assesses it. Ask: \"How do you bring the client into decisions about preventive care?\" Avoid reading the table aloud and holding anyone to another award's column as if it were their minimum."
- statement: qaa/veterinary-nursing-2024/4.2.b34.masters
  forPractitioner: { text: "The minimum for a master's degree (FHEQ level 7, SCQF level 11): teach and assess so that every graduate should be able to synthesise strategies that promote and evaluate collaboration with patients, clients and colleagues in identifying and giving therapeutic and preventive care.", rewrite: light, force: threshold, status: drafted }
  forBeneficiary: { text: "As the minimum for your master's degree, you should be able to synthesise strategies that promote and evaluate collaboration with patients, clients and colleagues in identifying and giving therapeutic and preventive care.", rewrite: full, force: threshold, status: drafted }
  author-agent-written: "Treat this as a threshold standard: the minimum a master's degree in veterinary nursing asks at FHEQ level 7, SCQF level 11, on collaborative therapeutic and preventive care. Cite it as QAA (2024), Veterinary Nursing Subject Benchmark Statement, section 4, table \"Working as a professional veterinary nurse: expectations\", master's degree column. Do not present it as an RCVS or regulatory requirement, or as holding for another award. Set it beside the same row's other columns (4.2.b34.foundation, 4.2.b34) and the framework descriptor qaa/fheq-2024/4.17.b3 (spine:7, strand:application)."
  author-agent-dialogue: "Raise it when a master's student or tutor asks what collaborative therapeutic and preventive care should look like by the end of the master's degree. Put it plainly: to a student, that by the end you should be able to synthesise strategies that promote and evaluate collaboration with patients, clients and colleagues in identifying and giving therapeutic and preventive care; to staff, as where the course teaches and assesses it. Ask: \"How do you bring the client into decisions about preventive care?\" Avoid reading the table aloud and holding anyone to another award's column as if it were their minimum."
- statement: qaa/veterinary-nursing-2024/4.2.b35
  forPractitioner: { text: "The minimum for a honours degree (FHEQ level 6, SCQF level 10): teach and assess so that every graduate should be able to foresee and handle difficult situations with patients, clients and colleagues with empathy, reducing risk where needed.", rewrite: light, force: threshold, status: drafted }
  forBeneficiary: { text: "As the minimum for your honours degree, you should be able to foresee and handle difficult situations with patients, clients and colleagues with empathy, reducing risk where needed.", rewrite: full, force: threshold, status: drafted }
  author-agent-written: "Treat this as a threshold standard: the minimum a honours degree in veterinary nursing asks at FHEQ level 6, SCQF level 10, on empathy in challenging situations. Cite it as QAA (2024), Veterinary Nursing Subject Benchmark Statement, section 4, table \"Working as a professional veterinary nurse: expectations\", honours degree column. Do not present it as an RCVS or regulatory requirement, or as holding for another award. Set it beside the same row's other columns (4.2.b35.foundation, 4.2.b35.masters) and the framework descriptor qaa/fheq-2024/4.15.b9.2 and qaa/fqheis-2024/4.16.b9.2 (spine:6, strand:autonomy)."
  author-agent-dialogue: "Raise it when an honours student or tutor asks what empathy in challenging situations should look like by the end of the honours degree. Put it plainly: to a student, that by the end you should be able to foresee and handle difficult situations with patients, clients and colleagues with empathy, reducing risk where needed; to staff, as where the course teaches and assesses it. Ask: \"Think of a hard conversation with an owner: what did you do that helped?\" Avoid reading the table aloud and holding anyone to another award's column as if it were their minimum."
- statement: qaa/veterinary-nursing-2024/4.2.b35.foundation
  forPractitioner: { text: "The minimum for a foundation degree (FHEQ level 5): teach and assess so that every graduate should be able to give empathetic support to patients, clients and colleagues when situations change or become difficult.", rewrite: light, force: threshold, status: drafted }
  forBeneficiary: { text: "As the minimum for your foundation degree, you should be able to give empathetic support to patients, clients and colleagues when situations change or become difficult.", rewrite: full, force: threshold, status: drafted }
  author-agent-written: "Treat this as a threshold standard: the minimum a foundation degree in veterinary nursing asks at FHEQ level 5, on empathy in challenging situations. Cite it as QAA (2024), Veterinary Nursing Subject Benchmark Statement, section 4, table \"Working as a professional veterinary nurse: expectations\", foundation degree column. Do not present it as an RCVS or regulatory requirement, or as holding for another award. Set it beside the same row's other columns (4.2.b35, 4.2.b35.masters) and the framework descriptor qaa/fheq-2024/4.12.b8 (spine:5, strand:autonomy)."
  author-agent-dialogue: "Raise it when a foundation degree student or tutor asks what empathy in challenging situations should look like by the end of the foundation degree. Put it plainly: to a student, that by the end you should be able to give empathetic support to patients, clients and colleagues when situations change or become difficult; to staff, as where the course teaches and assesses it. Ask: \"Think of a hard conversation with an owner: what did you do that helped?\" Avoid reading the table aloud and holding anyone to another award's column as if it were their minimum."
- statement: qaa/veterinary-nursing-2024/4.2.b35.masters
  forPractitioner: { text: "The minimum for a master's degree (FHEQ level 7, SCQF level 11): teach and assess so that every graduate should be able to lead and support colleagues through many kinds of difficult situation with patients, clients and colleagues, with empathy and with risk kept low where fitting.", rewrite: light, force: threshold, status: drafted }
  forBeneficiary: { text: "As the minimum for your master's degree, you should be able to lead and support colleagues through many kinds of difficult situation with patients, clients and colleagues, with empathy and with risk kept low where fitting.", rewrite: full, force: threshold, status: drafted }
  author-agent-written: "Treat this as a threshold standard: the minimum a master's degree in veterinary nursing asks at FHEQ level 7, SCQF level 11, on empathy in challenging situations. Cite it as QAA (2024), Veterinary Nursing Subject Benchmark Statement, section 4, table \"Working as a professional veterinary nurse: expectations\", master's degree column. Do not present it as an RCVS or regulatory requirement, or as holding for another award. Set it beside the same row's other columns (4.2.b35.foundation, 4.2.b35) and the framework descriptor qaa/fheq-2024/4.17.b8.2 (spine:7, strand:autonomy)."
  author-agent-dialogue: "Raise it when a master's student or tutor asks what empathy in challenging situations should look like by the end of the master's degree. Put it plainly: to a student, that by the end you should be able to lead and support colleagues through many kinds of difficult situation with patients, clients and colleagues, with empathy and with risk kept low where fitting; to staff, as where the course teaches and assesses it. Ask: \"Think of a hard conversation with an owner: what did you do that helped?\" Avoid reading the table aloud and holding anyone to another award's column as if it were their minimum."
- statement: qaa/veterinary-nursing-2024/4.2.b36
  forPractitioner: { text: "The minimum for a honours degree (FHEQ level 6, SCQF level 10): teach and assess so that every graduate should be able to recognise how complex the professional, ethical and legal framework is and how it bears on decisions, and practise to match.", rewrite: light, force: threshold, status: drafted }
  forBeneficiary: { text: "As the minimum for your honours degree, you should be able to recognise how complex the professional, ethical and legal framework is and how it bears on decisions, and practise to match.", rewrite: full, force: threshold, status: drafted }
  author-agent-written: "Treat this as a threshold standard: the minimum a honours degree in veterinary nursing asks at FHEQ level 6, SCQF level 10, on the professional, ethical and legal framework. Cite it as QAA (2024), Veterinary Nursing Subject Benchmark Statement, section 4, table \"Working as a professional veterinary nurse: expectations\", honours degree column. Do not present it as an RCVS or regulatory requirement, or as holding for another award. Set it beside the same row's other columns (4.2.b36.foundation, 4.2.b36.masters) and the framework descriptor qaa/fheq-2024/4.15.b7 and qaa/fqheis-2024/4.16.b6 (spine:6, strand:thinking)."
  author-agent-dialogue: "Raise it when an honours student or tutor asks what the professional, ethical and legal framework should look like by the end of the honours degree. Put it plainly: to a student, that by the end you should be able to recognise how complex the professional, ethical and legal framework is and how it bears on decisions, and practise to match; to staff, as where the course teaches and assesses it. Ask: \"Which rule or law most often shapes what you can do for a patient?\" Avoid reading the table aloud and holding anyone to another award's column as if it were their minimum."
- statement: qaa/veterinary-nursing-2024/4.2.b36.foundation
  forPractitioner: { text: "The minimum for a foundation degree (FHEQ level 5): teach and assess so that every graduate should be able to practise within the professional, ethical and legal framework.", rewrite: light, force: threshold, status: drafted }
  forBeneficiary: { text: "As the minimum for your foundation degree, you should be able to practise within the professional, ethical and legal framework.", rewrite: full, force: threshold, status: drafted }
  author-agent-written: "Treat this as a threshold standard: the minimum a foundation degree in veterinary nursing asks at FHEQ level 5, on the professional, ethical and legal framework. Cite it as QAA (2024), Veterinary Nursing Subject Benchmark Statement, section 4, table \"Working as a professional veterinary nurse: expectations\", foundation degree column. Do not present it as an RCVS or regulatory requirement, or as holding for another award. Set it beside the same row's other columns (4.2.b36, 4.2.b36.masters) and the framework descriptor qaa/fheq-2024/4.12.b5 (spine:5, strand:thinking)."
  author-agent-dialogue: "Raise it when a foundation degree student or tutor asks what the professional, ethical and legal framework should look like by the end of the foundation degree. Put it plainly: to a student, that by the end you should be able to practise within the professional, ethical and legal framework; to staff, as where the course teaches and assesses it. Ask: \"Which rule or law most often shapes what you can do for a patient?\" Avoid reading the table aloud and holding anyone to another award's column as if it were their minimum."
- statement: qaa/veterinary-nursing-2024/4.2.b36.masters
  forPractitioner: { text: "The minimum for a master's degree (FHEQ level 7, SCQF level 11): teach and assess so that every graduate should be able to appraise how complex the professional, ethical and legal frameworks are, and guide and lead colleagues on what decisions entail.", rewrite: light, force: threshold, status: drafted }
  forBeneficiary: { text: "As the minimum for your master's degree, you should be able to appraise how complex the professional, ethical and legal frameworks are, and guide and lead colleagues on what decisions entail.", rewrite: full, force: threshold, status: drafted }
  author-agent-written: "Treat this as a threshold standard: the minimum a master's degree in veterinary nursing asks at FHEQ level 7, SCQF level 11, on the professional, ethical and legal framework. Cite it as QAA (2024), Veterinary Nursing Subject Benchmark Statement, section 4, table \"Working as a professional veterinary nurse: expectations\", master's degree column. Do not present it as an RCVS or regulatory requirement, or as holding for another award. Set it beside the same row's other columns (4.2.b36.foundation, 4.2.b36) and the framework descriptor qaa/fheq-2024/4.17.b5 (spine:7, strand:thinking)."
  author-agent-dialogue: "Raise it when a master's student or tutor asks what the professional, ethical and legal framework should look like by the end of the master's degree. Put it plainly: to a student, that by the end you should be able to appraise how complex the professional, ethical and legal frameworks are, and guide and lead colleagues on what decisions entail; to staff, as where the course teaches and assesses it. Ask: \"Which rule or law most often shapes what you can do for a patient?\" Avoid reading the table aloud and holding anyone to another award's column as if it were their minimum."
- statement: qaa/veterinary-nursing-2024/4.2.b37
  forPractitioner: { text: "The minimum for a honours degree (FHEQ level 6, SCQF level 10): teach and assess so that every graduate should be able to reflect critically on personal responsibility and decision-making in many situations.", rewrite: light, force: threshold, status: drafted }
  forBeneficiary: { text: "As the minimum for your honours degree, you should be able to reflect critically on personal responsibility and decision-making in many situations.", rewrite: full, force: threshold, status: drafted }
  author-agent-written: "Treat this as a threshold standard: the minimum a honours degree in veterinary nursing asks at FHEQ level 6, SCQF level 10, on responsibility and impartial decisions. Cite it as QAA (2024), Veterinary Nursing Subject Benchmark Statement, section 4, table \"Working as a professional veterinary nurse: expectations\", honours degree column. Do not present it as an RCVS or regulatory requirement, or as holding for another award. Set it beside the same row's other columns (4.2.b37.foundation, 4.2.b37.masters) and the framework descriptor qaa/fheq-2024/4.15.b9.2 and qaa/fqheis-2024/4.16.b9.2 (spine:6, strand:autonomy)."
  author-agent-dialogue: "Raise it when an honours student or tutor asks what responsibility and impartial decisions should look like by the end of the honours degree. Put it plainly: to a student, that by the end you should be able to reflect critically on personal responsibility and decision-making in many situations; to staff, as where the course teaches and assesses it. Ask: \"When did you last have to stay impartial, and how did you manage it?\" Avoid reading the table aloud and holding anyone to another award's column as if it were their minimum."
- statement: qaa/veterinary-nursing-2024/4.2.b37.foundation
  forPractitioner: { text: "The minimum for a foundation degree (FHEQ level 5): teach and assess so that every graduate should be able to uphold personal responsibility and impartial decisions in many situations.", rewrite: light, force: threshold, status: drafted }
  forBeneficiary: { text: "As the minimum for your foundation degree, you should be able to uphold personal responsibility and impartial decisions in many situations.", rewrite: full, force: threshold, status: drafted }
  author-agent-written: "Treat this as a threshold standard: the minimum a foundation degree in veterinary nursing asks at FHEQ level 5, on responsibility and impartial decisions. Cite it as QAA (2024), Veterinary Nursing Subject Benchmark Statement, section 4, table \"Working as a professional veterinary nurse: expectations\", foundation degree column. Do not present it as an RCVS or regulatory requirement, or as holding for another award. Set it beside the same row's other columns (4.2.b37, 4.2.b37.masters) and the framework descriptor qaa/fheq-2024/4.12.b8 (spine:5, strand:autonomy)."
  author-agent-dialogue: "Raise it when a foundation degree student or tutor asks what responsibility and impartial decisions should look like by the end of the foundation degree. Put it plainly: to a student, that by the end you should be able to uphold personal responsibility and impartial decisions in many situations; to staff, as where the course teaches and assesses it. Ask: \"When did you last have to stay impartial, and how did you manage it?\" Avoid reading the table aloud and holding anyone to another award's column as if it were their minimum."
- statement: qaa/veterinary-nursing-2024/4.2.b37.masters
  forPractitioner: { text: "The minimum for a master's degree (FHEQ level 7, SCQF level 11): teach and assess so that every graduate should be able to reflect critically on, and evaluate, personal and interprofessional responsibility and decision-making in many situations.", rewrite: light, force: threshold, status: drafted }
  forBeneficiary: { text: "As the minimum for your master's degree, you should be able to reflect critically on, and evaluate, personal and interprofessional responsibility and decision-making in many situations.", rewrite: full, force: threshold, status: drafted }
  author-agent-written: "Treat this as a threshold standard: the minimum a master's degree in veterinary nursing asks at FHEQ level 7, SCQF level 11, on responsibility and impartial decisions. Cite it as QAA (2024), Veterinary Nursing Subject Benchmark Statement, section 4, table \"Working as a professional veterinary nurse: expectations\", master's degree column. Do not present it as an RCVS or regulatory requirement, or as holding for another award. Set it beside the same row's other columns (4.2.b37.foundation, 4.2.b37) and the framework descriptor qaa/fheq-2024/4.17.b8.2 (spine:7, strand:autonomy)."
  author-agent-dialogue: "Raise it when a master's student or tutor asks what responsibility and impartial decisions should look like by the end of the master's degree. Put it plainly: to a student, that by the end you should be able to reflect critically on, and evaluate, personal and interprofessional responsibility and decision-making in many situations; to staff, as where the course teaches and assesses it. Ask: \"When did you last have to stay impartial, and how did you manage it?\" Avoid reading the table aloud and holding anyone to another award's column as if it were their minimum."
- statement: qaa/veterinary-nursing-2024/4.2.b38
  forPractitioner: { text: "The minimum for a honours degree (FHEQ level 6, SCQF level 10): teach and assess so that every graduate should be able to choose and put in place several risk-management strategies that create and keep a safe clinical environment.", rewrite: light, force: threshold, status: drafted }
  forBeneficiary: { text: "As the minimum for your honours degree, you should be able to choose and put in place several risk-management strategies that create and keep a safe clinical environment.", rewrite: full, force: threshold, status: drafted }
  author-agent-written: "Treat this as a threshold standard: the minimum a honours degree in veterinary nursing asks at FHEQ level 6, SCQF level 10, on a safe clinical environment. Cite it as QAA (2024), Veterinary Nursing Subject Benchmark Statement, section 4, table \"Working as a professional veterinary nurse: expectations\", honours degree column. Do not present it as an RCVS or regulatory requirement, or as holding for another award. Set it beside the same row's other columns (4.2.b38.foundation, 4.2.b38.masters) and the framework descriptor qaa/fheq-2024/4.15.b6 and qaa/fqheis-2024/4.16.b4 (spine:6, strand:application)."
  author-agent-dialogue: "Raise it when an honours student or tutor asks what a safe clinical environment should look like by the end of the honours degree. Put it plainly: to a student, that by the end you should be able to choose and put in place several risk-management strategies that create and keep a safe clinical environment; to staff, as where the course teaches and assesses it. Ask: \"What hazard in your clinic worries you most, and what would reduce it?\" Avoid reading the table aloud and holding anyone to another award's column as if it were their minimum."
- statement: qaa/veterinary-nursing-2024/4.2.b38.foundation
  forPractitioner: { text: "The minimum for a foundation degree (FHEQ level 5): teach and assess so that every graduate should be able to help protect the public by creating and keeping a safe clinical environment.", rewrite: light, force: threshold, status: drafted }
  forBeneficiary: { text: "As the minimum for your foundation degree, you should be able to help protect the public by creating and keeping a safe clinical environment.", rewrite: full, force: threshold, status: drafted }
  author-agent-written: "Treat this as a threshold standard: the minimum a foundation degree in veterinary nursing asks at FHEQ level 5, on a safe clinical environment. Cite it as QAA (2024), Veterinary Nursing Subject Benchmark Statement, section 4, table \"Working as a professional veterinary nurse: expectations\", foundation degree column. Do not present it as an RCVS or regulatory requirement, or as holding for another award. Set it beside the same row's other columns (4.2.b38, 4.2.b38.masters) and the framework descriptor qaa/fheq-2024/4.12.b2 (spine:5, strand:application)."
  author-agent-dialogue: "Raise it when a foundation degree student or tutor asks what a safe clinical environment should look like by the end of the foundation degree. Put it plainly: to a student, that by the end you should be able to help protect the public by creating and keeping a safe clinical environment; to staff, as where the course teaches and assesses it. Ask: \"What hazard in your clinic worries you most, and what would reduce it?\" Avoid reading the table aloud and holding anyone to another award's column as if it were their minimum."
- statement: qaa/veterinary-nursing-2024/4.2.b38.masters
  forPractitioner: { text: "The minimum for a master's degree (FHEQ level 7, SCQF level 11): teach and assess so that every graduate should be able to analyse and shape processes that improve risk-management strategies for a safe clinical environment, with one health in view.", rewrite: light, force: threshold, status: drafted }
  forBeneficiary: { text: "As the minimum for your master's degree, you should be able to analyse and shape processes that improve risk-management strategies for a safe clinical environment, with one health in view.", rewrite: full, force: threshold, status: drafted }
  author-agent-written: "Treat this as a threshold standard: the minimum a master's degree in veterinary nursing asks at FHEQ level 7, SCQF level 11, on a safe clinical environment. Cite it as QAA (2024), Veterinary Nursing Subject Benchmark Statement, section 4, table \"Working as a professional veterinary nurse: expectations\", master's degree column. Do not present it as an RCVS or regulatory requirement, or as holding for another award. Set it beside the same row's other columns (4.2.b38.foundation, 4.2.b38) and the framework descriptor qaa/fheq-2024/4.17.b3 (spine:7, strand:application)."
  author-agent-dialogue: "Raise it when a master's student or tutor asks what a safe clinical environment should look like by the end of the master's degree. Put it plainly: to a student, that by the end you should be able to analyse and shape processes that improve risk-management strategies for a safe clinical environment, with one health in view; to staff, as where the course teaches and assesses it. Ask: \"What hazard in your clinic worries you most, and what would reduce it?\" Avoid reading the table aloud and holding anyone to another award's column as if it were their minimum."
- statement: qaa/veterinary-nursing-2024/4.2.b39
  forPractitioner: { text: "The minimum for a honours degree (FHEQ level 6, SCQF level 10): teach and assess so that every graduate should be able to guide, set an example for, mentor and support others in the veterinary setting, making sure supervision and monitoring work.", rewrite: light, force: threshold, status: drafted }
  forBeneficiary: { text: "As the minimum for your honours degree, you should be able to guide, set an example for, mentor and support others in the veterinary setting, making sure supervision and monitoring work.", rewrite: full, force: threshold, status: drafted }
  author-agent-written: "Treat this as a threshold standard: the minimum a honours degree in veterinary nursing asks at FHEQ level 6, SCQF level 10, on guidance, role-modelling and mentorship. Cite it as QAA (2024), Veterinary Nursing Subject Benchmark Statement, section 4, table \"Working as a professional veterinary nurse: expectations\", honours degree column. Do not present it as an RCVS or regulatory requirement, or as holding for another award. Set it beside the same row's other columns (4.2.b39.foundation, 4.2.b39.masters) and the framework descriptor qaa/fheq-2024/4.15.b9.2 and qaa/fqheis-2024/4.16.b9.2 (spine:6, strand:autonomy)."
  author-agent-dialogue: "Raise it when an honours student or tutor asks what guidance, role-modelling and mentorship should look like by the end of the honours degree. Put it plainly: to a student, that by the end you should be able to guide, set an example for, mentor and support others in the veterinary setting, making sure supervision and monitoring work; to staff, as where the course teaches and assesses it. Ask: \"Who have you helped learn something recently, and how did you go about it?\" Avoid reading the table aloud and holding anyone to another award's column as if it were their minimum."
- statement: qaa/veterinary-nursing-2024/4.2.b39.foundation
  forPractitioner: { text: "The minimum for a foundation degree (FHEQ level 5): teach and assess so that every graduate should be able to guide, set an example for and support others in the veterinary setting.", rewrite: light, force: threshold, status: drafted }
  forBeneficiary: { text: "As the minimum for your foundation degree, you should be able to guide, set an example for and support others in the veterinary setting.", rewrite: full, force: threshold, status: drafted }
  author-agent-written: "Treat this as a threshold standard: the minimum a foundation degree in veterinary nursing asks at FHEQ level 5, on guidance, role-modelling and mentorship. Cite it as QAA (2024), Veterinary Nursing Subject Benchmark Statement, section 4, table \"Working as a professional veterinary nurse: expectations\", foundation degree column. Do not present it as an RCVS or regulatory requirement, or as holding for another award. Set it beside the same row's other columns (4.2.b39, 4.2.b39.masters) and the framework descriptor qaa/fheq-2024/4.12.b8 (spine:5, strand:autonomy)."
  author-agent-dialogue: "Raise it when a foundation degree student or tutor asks what guidance, role-modelling and mentorship should look like by the end of the foundation degree. Put it plainly: to a student, that by the end you should be able to guide, set an example for and support others in the veterinary setting; to staff, as where the course teaches and assesses it. Ask: \"Who have you helped learn something recently, and how did you go about it?\" Avoid reading the table aloud and holding anyone to another award's column as if it were their minimum."
- statement: qaa/veterinary-nursing-2024/4.2.b39.masters
  forPractitioner: { text: "The minimum for a master's degree (FHEQ level 7, SCQF level 11): teach and assess so that every graduate should be able to inspire themselves and others to act as ambassadors who uphold the profession's reputation inside and outside the veterinary setting.", rewrite: light, force: threshold, status: drafted }
  forBeneficiary: { text: "As the minimum for your master's degree, you should be able to inspire yourself and others to act as ambassadors who uphold the profession's reputation inside and outside the veterinary setting.", rewrite: full, force: threshold, status: drafted }
  author-agent-written: "Treat this as a threshold standard: the minimum a master's degree in veterinary nursing asks at FHEQ level 7, SCQF level 11, on guidance, role-modelling and mentorship. Cite it as QAA (2024), Veterinary Nursing Subject Benchmark Statement, section 4, table \"Working as a professional veterinary nurse: expectations\", master's degree column. Do not present it as an RCVS or regulatory requirement, or as holding for another award. Set it beside the same row's other columns (4.2.b39.foundation, 4.2.b39) and the framework descriptor qaa/fheq-2024/4.17.b8.2 (spine:7, strand:autonomy)."
  author-agent-dialogue: "Raise it when a master's student or tutor asks what guidance, role-modelling and mentorship should look like by the end of the master's degree. Put it plainly: to a student, that by the end you should be able to inspire yourself and others to act as ambassadors who uphold the profession's reputation inside and outside the veterinary setting; to staff, as where the course teaches and assesses it. Ask: \"Who have you helped learn something recently, and how did you go about it?\" Avoid reading the table aloud and holding anyone to another award's column as if it were their minimum."
- statement: qaa/veterinary-nursing-2024/4.2.b40
  forPractitioner: { text: "The minimum for a honours degree (FHEQ level 6, SCQF level 10): teach and assess so that every graduate should be able to critically analyse their own role and others', including suitable delegation, supervision and advice-seeking.", rewrite: light, force: threshold, status: drafted }
  forBeneficiary: { text: "As the minimum for your honours degree, you should be able to critically analyse your own role and others', including suitable delegation, supervision and advice-seeking.", rewrite: full, force: threshold, status: drafted }
  author-agent-written: "Treat this as a threshold standard: the minimum a honours degree in veterinary nursing asks at FHEQ level 6, SCQF level 10, on roles, delegation and supervision. Cite it as QAA (2024), Veterinary Nursing Subject Benchmark Statement, section 4, table \"Working as a professional veterinary nurse: expectations\", honours degree column. Do not present it as an RCVS or regulatory requirement, or as holding for another award. Set it beside the same row's other columns (4.2.b40.foundation, 4.2.b40.masters) and the framework descriptor qaa/fheq-2024/4.15.b9.2 and qaa/fqheis-2024/4.16.b9.2 (spine:6, strand:autonomy)."
  author-agent-dialogue: "Raise it when an honours student or tutor asks what roles, delegation and supervision should look like by the end of the honours degree. Put it plainly: to a student, that by the end you should be able to critically analyse your own role and others', including suitable delegation, supervision and advice-seeking; to staff, as where the course teaches and assesses it. Ask: \"What would you delegate, and what would you never delegate, and why?\" Avoid reading the table aloud and holding anyone to another award's column as if it were their minimum."
- statement: qaa/veterinary-nursing-2024/4.2.b40.foundation
  forPractitioner: { text: "The minimum for a foundation degree (FHEQ level 5): teach and assess so that every graduate should be able to understand their own role and others', including when to delegate, supervise or ask for advice.", rewrite: light, force: threshold, status: drafted }
  forBeneficiary: { text: "As the minimum for your foundation degree, you should be able to understand your own role and others', including when to delegate, supervise or ask for advice.", rewrite: full, force: threshold, status: drafted }
  author-agent-written: "Treat this as a threshold standard: the minimum a foundation degree in veterinary nursing asks at FHEQ level 5, on roles, delegation and supervision. Cite it as QAA (2024), Veterinary Nursing Subject Benchmark Statement, section 4, table \"Working as a professional veterinary nurse: expectations\", foundation degree column. Do not present it as an RCVS or regulatory requirement, or as holding for another award. Set it beside the same row's other columns (4.2.b40, 4.2.b40.masters) and the framework descriptor qaa/fheq-2024/4.12.b8 (spine:5, strand:autonomy)."
  author-agent-dialogue: "Raise it when a foundation degree student or tutor asks what roles, delegation and supervision should look like by the end of the foundation degree. Put it plainly: to a student, that by the end you should be able to understand your own role and others', including when to delegate, supervise or ask for advice; to staff, as where the course teaches and assesses it. Ask: \"What would you delegate, and what would you never delegate, and why?\" Avoid reading the table aloud and holding anyone to another award's column as if it were their minimum."
- statement: qaa/veterinary-nursing-2024/4.2.b40.masters
  forPractitioner: { text: "The minimum for a master's degree (FHEQ level 7, SCQF level 11): teach and assess so that every graduate should be able to critically evaluate and reflect on their own role and others', guiding others on suitable delegation, supervision and when to seek advice.", rewrite: light, force: threshold, status: drafted }
  forBeneficiary: { text: "As the minimum for your master's degree, you should be able to critically evaluate and reflect on your own role and others', guiding others on suitable delegation, supervision and when to seek advice.", rewrite: full, force: threshold, status: drafted }
  author-agent-written: "Treat this as a threshold standard: the minimum a master's degree in veterinary nursing asks at FHEQ level 7, SCQF level 11, on roles, delegation and supervision. Cite it as QAA (2024), Veterinary Nursing Subject Benchmark Statement, section 4, table \"Working as a professional veterinary nurse: expectations\", master's degree column. Do not present it as an RCVS or regulatory requirement, or as holding for another award. Set it beside the same row's other columns (4.2.b40.foundation, 4.2.b40) and the framework descriptor qaa/fheq-2024/4.17.b8.2 (spine:7, strand:autonomy)."
  author-agent-dialogue: "Raise it when a master's student or tutor asks what roles, delegation and supervision should look like by the end of the master's degree. Put it plainly: to a student, that by the end you should be able to critically evaluate and reflect on your own role and others', guiding others on suitable delegation, supervision and when to seek advice; to staff, as where the course teaches and assesses it. Ask: \"What would you delegate, and what would you never delegate, and why?\" Avoid reading the table aloud and holding anyone to another award's column as if it were their minimum."
- statement: qaa/veterinary-nursing-2024/4.2.b41
  forPractitioner: { text: "The minimum for a honours degree (FHEQ level 6, SCQF level 10): teach and assess so that every graduate should be able to advise clients and advocate for them and the patient where fitting, mindful of their own mental and physical health.", rewrite: light, force: threshold, status: drafted }
  forBeneficiary: { text: "As the minimum for your honours degree, you should be able to advise clients and advocate for them and the patient where fitting, mindful of your own mental and physical health.", rewrite: full, force: threshold, status: drafted }
  author-agent-written: "Treat this as a threshold standard: the minimum a honours degree in veterinary nursing asks at FHEQ level 6, SCQF level 10, on advocacy, advice and well-being. Cite it as QAA (2024), Veterinary Nursing Subject Benchmark Statement, section 4, table \"Working as a professional veterinary nurse: expectations\", honours degree column. Do not present it as an RCVS or regulatory requirement, or as holding for another award. Set it beside the same row's other columns (4.2.b41.foundation, 4.2.b41.masters) and the framework descriptor qaa/fheq-2024/4.15.b8 and qaa/fqheis-2024/4.16.b7 (spine:6, strand:communication)."
  author-agent-dialogue: "Raise it when an honours student or tutor asks what advocacy, advice and well-being should look like by the end of the honours degree. Put it plainly: to a student, that by the end you should be able to advise clients and advocate for them and the patient where fitting, mindful of your own mental and physical health; to staff, as where the course teaches and assesses it. Ask: \"When you advise an owner, how do you speak up for the animal while looking after yourself?\" Avoid reading the table aloud and holding anyone to another award's column as if it were their minimum."
- statement: qaa/veterinary-nursing-2024/4.2.b41.foundation
  forPractitioner: { text: "The minimum for a foundation degree (FHEQ level 5): teach and assess so that every graduate should be able to show empathy with patients and clients and advocate for them where fitting, mindful of their own mental and physical health.", rewrite: light, force: threshold, status: drafted }
  forBeneficiary: { text: "As the minimum for your foundation degree, you should be able to show empathy with patients and clients and advocate for them where fitting, mindful of your own mental and physical health.", rewrite: full, force: threshold, status: drafted }
  author-agent-written: "Treat this as a threshold standard: the minimum a foundation degree in veterinary nursing asks at FHEQ level 5, on advocacy, advice and well-being. Cite it as QAA (2024), Veterinary Nursing Subject Benchmark Statement, section 4, table \"Working as a professional veterinary nurse: expectations\", foundation degree column. Do not present it as an RCVS or regulatory requirement, or as holding for another award. Set it beside the same row's other columns (4.2.b41, 4.2.b41.masters) and the framework descriptor qaa/fheq-2024/4.12.b6 (spine:5, strand:communication)."
  author-agent-dialogue: "Raise it when a foundation degree student or tutor asks what advocacy, advice and well-being should look like by the end of the foundation degree. Put it plainly: to a student, that by the end you should be able to show empathy with patients and clients and advocate for them where fitting, mindful of your own mental and physical health; to staff, as where the course teaches and assesses it. Ask: \"When you advise an owner, how do you speak up for the animal while looking after yourself?\" Avoid reading the table aloud and holding anyone to another award's column as if it were their minimum."
- statement: qaa/veterinary-nursing-2024/4.2.b41.masters
  forPractitioner: { text: "The minimum for a master's degree (FHEQ level 7, SCQF level 11): teach and assess so that every graduate should be able to be aware of what affects mental and physical health, and put in place strategies that help others advise clients and advocate for them and the patient.", rewrite: light, force: threshold, status: drafted }
  forBeneficiary: { text: "As the minimum for your master's degree, you should be able to be aware of what affects mental and physical health, and put in place strategies that help others advise clients and advocate for them and the patient.", rewrite: full, force: threshold, status: drafted }
  author-agent-written: "Treat this as a threshold standard: the minimum a master's degree in veterinary nursing asks at FHEQ level 7, SCQF level 11, on advocacy, advice and well-being. Cite it as QAA (2024), Veterinary Nursing Subject Benchmark Statement, section 4, table \"Working as a professional veterinary nurse: expectations\", master's degree column. Do not present it as an RCVS or regulatory requirement, or as holding for another award. Set it beside the same row's other columns (4.2.b41.foundation, 4.2.b41) and the framework descriptor qaa/fheq-2024/4.17.b5 (spine:7, strand:communication)."
  author-agent-dialogue: "Raise it when a master's student or tutor asks what advocacy, advice and well-being should look like by the end of the master's degree. Put it plainly: to a student, that by the end you should be able to be aware of what affects mental and physical health, and put in place strategies that help others advise clients and advocate for them and the patient; to staff, as where the course teaches and assesses it. Ask: \"When you advise an owner, how do you speak up for the animal while looking after yourself?\" Avoid reading the table aloud and holding anyone to another award's column as if it were their minimum."
- statement: qaa/veterinary-nursing-2024/4.2.b42
  forPractitioner: { text: "The minimum for a honours degree (FHEQ level 6, SCQF level 10): teach and assess so that every graduate should be able to plan and carry out research and development, including building an evidence base for clinical practice.", rewrite: light, force: threshold, status: drafted }
  forBeneficiary: { text: "As the minimum for your honours degree, you should be able to plan and carry out research and development, including building an evidence base for clinical practice.", rewrite: full, force: threshold, status: drafted }
  author-agent-written: "Treat this as a threshold standard: the minimum a honours degree in veterinary nursing asks at FHEQ level 6, SCQF level 10, on research and the evidence base. Cite it as QAA (2024), Veterinary Nursing Subject Benchmark Statement, section 4, table \"Working as a professional veterinary nurse: expectations\", honours degree column. Do not present it as an RCVS or regulatory requirement, or as holding for another award. Set it beside the same row's other columns (4.2.b42.foundation, 4.2.b42.masters) and the framework descriptor qaa/fheq-2024/4.15.b3.2 and qaa/fqheis-2024/4.16.b5 (spine:6, strand:application)."
  author-agent-dialogue: "Raise it when an honours student or tutor asks what research and the evidence base should look like by the end of the honours degree. Put it plainly: to a student, that by the end you should be able to plan and carry out research and development, including building an evidence base for clinical practice; to staff, as where the course teaches and assesses it. Ask: \"What clinical question would you most like answered by research, and how would you start?\" Avoid reading the table aloud and holding anyone to another award's column as if it were their minimum."
- statement: qaa/veterinary-nursing-2024/4.2.b42.foundation
  forPractitioner: { text: "The minimum for a foundation degree (FHEQ level 5): teach and assess so that every graduate should be able to take part in building an evidence base in clinical practice and understand why that work matters.", rewrite: light, force: threshold, status: drafted }
  forBeneficiary: { text: "As the minimum for your foundation degree, you should be able to take part in building an evidence base in clinical practice and understand why that work matters.", rewrite: full, force: threshold, status: drafted }
  author-agent-written: "Treat this as a threshold standard: the minimum a foundation degree in veterinary nursing asks at FHEQ level 5, on research and the evidence base. Cite it as QAA (2024), Veterinary Nursing Subject Benchmark Statement, section 4, table \"Working as a professional veterinary nurse: expectations\", foundation degree column. Do not present it as an RCVS or regulatory requirement, or as holding for another award. Set it beside the same row's other columns (4.2.b42, 4.2.b42.masters) and the framework descriptor qaa/fheq-2024/4.12.b3 (spine:5, strand:application)."
  author-agent-dialogue: "Raise it when a foundation degree student or tutor asks what research and the evidence base should look like by the end of the foundation degree. Put it plainly: to a student, that by the end you should be able to take part in building an evidence base in clinical practice and understand why that work matters; to staff, as where the course teaches and assesses it. Ask: \"What clinical question would you most like answered by research, and how would you start?\" Avoid reading the table aloud and holding anyone to another award's column as if it were their minimum."
- statement: qaa/veterinary-nursing-2024/4.2.b42.masters
  forPractitioner: { text: "The minimum for a master's degree (FHEQ level 7, SCQF level 11): teach and assess so that every graduate should be able to propose new approaches to keep developing evidence-based veterinary nursing and evaluate the impact of their research and of sharing its ideas.", rewrite: light, force: threshold, status: drafted }
  forBeneficiary: { text: "As the minimum for your master's degree, you should be able to propose new approaches to keep developing evidence-based veterinary nursing and evaluate the impact of your research and of sharing its ideas.", rewrite: full, force: threshold, status: drafted }
  author-agent-written: "Treat this as a threshold standard: the minimum a master's degree in veterinary nursing asks at FHEQ level 7, SCQF level 11, on research and the evidence base. Cite it as QAA (2024), Veterinary Nursing Subject Benchmark Statement, section 4, table \"Working as a professional veterinary nurse: expectations\", master's degree column. Do not present it as an RCVS or regulatory requirement, or as holding for another award. Set it beside the same row's other columns (4.2.b42.foundation, 4.2.b42) and the framework descriptor qaa/fheq-2024/4.17.b4.1 (spine:7, strand:application)."
  author-agent-dialogue: "Raise it when a master's student or tutor asks what research and the evidence base should look like by the end of the master's degree. Put it plainly: to a student, that by the end you should be able to propose new approaches to keep developing evidence-based veterinary nursing and evaluate the impact of your research and of sharing its ideas; to staff, as where the course teaches and assesses it. Ask: \"What clinical question would you most like answered by research, and how would you start?\" Avoid reading the table aloud and holding anyone to another award's column as if it were their minimum."
- statement: qaa/veterinary-nursing-2024/4.2.b43
  forPractitioner: { text: "The minimum for a honours degree (FHEQ level 6, SCQF level 10): teach and assess so that every graduate should be able to take up and promote equality, diversity and inclusion in the veterinary setting and beyond it.", rewrite: light, force: threshold, status: drafted }
  forBeneficiary: { text: "As the minimum for your honours degree, you should be able to take up and promote equality, diversity and inclusion in the veterinary setting and beyond it.", rewrite: full, force: threshold, status: drafted }
  author-agent-written: "Treat this as a threshold standard: the minimum a honours degree in veterinary nursing asks at FHEQ level 6, SCQF level 10, on equality, diversity and inclusion in practice. Cite it as QAA (2024), Veterinary Nursing Subject Benchmark Statement, section 4, table \"Working as a professional veterinary nurse: expectations\", honours degree column. Do not present it as an RCVS or regulatory requirement, or as holding for another award. Set it beside the same row's other columns (4.2.b43.foundation, 4.2.b43.masters) and the framework descriptor qaa/fheq-2024/4.15.b9.2 and qaa/fqheis-2024/4.16.b9.2 (spine:6, strand:autonomy)."
  author-agent-dialogue: "Raise it when an honours student or tutor asks what equality, diversity and inclusion in practice should look like by the end of the honours degree. Put it plainly: to a student, that by the end you should be able to take up and promote equality, diversity and inclusion in the veterinary setting and beyond it; to staff, as where the course teaches and assesses it. Ask: \"What have you done, or seen done, to make your workplace more inclusive?\" Avoid reading the table aloud and holding anyone to another award's column as if it were their minimum."
- statement: qaa/veterinary-nursing-2024/4.2.b43.foundation
  forPractitioner: { text: "The minimum for a foundation degree (FHEQ level 5): teach and assess so that every graduate should be able to take up and promote equality, diversity and inclusion in the veterinary setting and beyond it.", rewrite: light, force: threshold, status: drafted }
  forBeneficiary: { text: "As the minimum for your foundation degree, you should be able to take up and promote equality, diversity and inclusion in the veterinary setting and beyond it.", rewrite: full, force: threshold, status: drafted }
  author-agent-written: "Treat this as a threshold standard: the minimum a foundation degree in veterinary nursing asks at FHEQ level 5, on equality, diversity and inclusion in practice. Cite it as QAA (2024), Veterinary Nursing Subject Benchmark Statement, section 4, table \"Working as a professional veterinary nurse: expectations\", foundation degree column. Do not present it as an RCVS or regulatory requirement, or as holding for another award. Set it beside the same row's other columns (4.2.b43, 4.2.b43.masters) and the framework descriptor qaa/fheq-2024/4.12.b8 (spine:5, strand:autonomy)."
  author-agent-dialogue: "Raise it when a foundation degree student or tutor asks what equality, diversity and inclusion in practice should look like by the end of the foundation degree. Put it plainly: to a student, that by the end you should be able to take up and promote equality, diversity and inclusion in the veterinary setting and beyond it; to staff, as where the course teaches and assesses it. Ask: \"What have you done, or seen done, to make your workplace more inclusive?\" Avoid reading the table aloud and holding anyone to another award's column as if it were their minimum."
- statement: qaa/veterinary-nursing-2024/4.2.b43.masters
  forPractitioner: { text: "The minimum for a master's degree (FHEQ level 7, SCQF level 11): teach and assess so that every graduate should be able to take up and promote equality, diversity and inclusion in the veterinary setting and beyond it.", rewrite: light, force: threshold, status: drafted }
  forBeneficiary: { text: "As the minimum for your master's degree, you should be able to take up and promote equality, diversity and inclusion in the veterinary setting and beyond it.", rewrite: full, force: threshold, status: drafted }
  author-agent-written: "Treat this as a threshold standard: the minimum a master's degree in veterinary nursing asks at FHEQ level 7, SCQF level 11, on equality, diversity and inclusion in practice. Cite it as QAA (2024), Veterinary Nursing Subject Benchmark Statement, section 4, table \"Working as a professional veterinary nurse: expectations\", master's degree column. Do not present it as an RCVS or regulatory requirement, or as holding for another award. Set it beside the same row's other columns (4.2.b43.foundation, 4.2.b43) and the framework descriptor qaa/fheq-2024/4.17.b8.2 (spine:7, strand:autonomy)."
  author-agent-dialogue: "Raise it when a master's student or tutor asks what equality, diversity and inclusion in practice should look like by the end of the master's degree. Put it plainly: to a student, that by the end you should be able to take up and promote equality, diversity and inclusion in the veterinary setting and beyond it; to staff, as where the course teaches and assesses it. Ask: \"What have you done, or seen done, to make your workplace more inclusive?\" Avoid reading the table aloud and holding anyone to another award's column as if it were their minimum."
- statement: qaa/veterinary-nursing-2024/4.2.b44
  forPractitioner: { text: "The minimum for a honours degree (FHEQ level 6, SCQF level 10): teach and assess so that every graduate should be able to critically evaluate their own skills and see and take chances to develop and gain new competences as professional development requires.", rewrite: light, force: threshold, status: drafted }
  forBeneficiary: { text: "As the minimum for your honours degree, you should be able to critically evaluate your own skills and see and take chances to develop and gain new competences as professional development requires.", rewrite: full, force: threshold, status: drafted }
  author-agent-written: "Treat this as a threshold standard: the minimum a honours degree in veterinary nursing asks at FHEQ level 6, SCQF level 10, on professional development. Cite it as QAA (2024), Veterinary Nursing Subject Benchmark Statement, section 4, table \"Working as a professional veterinary nurse: expectations\", honours degree column. Do not present it as an RCVS or regulatory requirement, or as holding for another award. Set it beside the same row's other columns (4.2.b44.foundation, 4.2.b44.masters) and the framework descriptor qaa/fheq-2024/4.15.b9.2 and qaa/fqheis-2024/4.16.b9.2 (spine:6, strand:autonomy)."
  author-agent-dialogue: "Raise it when an honours student or tutor asks what professional development should look like by the end of the honours degree. Put it plainly: to a student, that by the end you should be able to critically evaluate your own skills and see and take chances to develop and gain new competences as professional development requires; to staff, as where the course teaches and assesses it. Ask: \"What new competence do you want next, and how will you get it?\" Avoid reading the table aloud and holding anyone to another award's column as if it were their minimum."
- statement: qaa/veterinary-nursing-2024/4.2.b44.foundation
  forPractitioner: { text: "The minimum for a foundation degree (FHEQ level 5): teach and assess so that every graduate should be able to reflect on their own skills and see chances to develop and gain new competences as professional development requires.", rewrite: light, force: threshold, status: drafted }
  forBeneficiary: { text: "As the minimum for your foundation degree, you should be able to reflect on your own skills and see chances to develop and gain new competences as professional development requires.", rewrite: full, force: threshold, status: drafted }
  author-agent-written: "Treat this as a threshold standard: the minimum a foundation degree in veterinary nursing asks at FHEQ level 5, on professional development. Cite it as QAA (2024), Veterinary Nursing Subject Benchmark Statement, section 4, table \"Working as a professional veterinary nurse: expectations\", foundation degree column. Do not present it as an RCVS or regulatory requirement, or as holding for another award. Set it beside the same row's other columns (4.2.b44, 4.2.b44.masters) and the framework descriptor qaa/fheq-2024/4.12.b8 (spine:5, strand:autonomy)."
  author-agent-dialogue: "Raise it when a foundation degree student or tutor asks what professional development should look like by the end of the foundation degree. Put it plainly: to a student, that by the end you should be able to reflect on your own skills and see chances to develop and gain new competences as professional development requires; to staff, as where the course teaches and assesses it. Ask: \"What new competence do you want next, and how will you get it?\" Avoid reading the table aloud and holding anyone to another award's column as if it were their minimum."
- statement: qaa/veterinary-nursing-2024/4.2.b44.masters
  forPractitioner: { text: "The minimum for a master's degree (FHEQ level 7, SCQF level 11): teach and assess so that every graduate should be able to support and lead colleagues in seeing and taking chances to develop and gain new competences as professional development requires.", rewrite: light, force: threshold, status: drafted }
  forBeneficiary: { text: "As the minimum for your master's degree, you should be able to support and lead colleagues in seeing and taking chances to develop and gain new competences as professional development requires.", rewrite: full, force: threshold, status: drafted }
  author-agent-written: "Treat this as a threshold standard: the minimum a master's degree in veterinary nursing asks at FHEQ level 7, SCQF level 11, on professional development. Cite it as QAA (2024), Veterinary Nursing Subject Benchmark Statement, section 4, table \"Working as a professional veterinary nurse: expectations\", master's degree column. Do not present it as an RCVS or regulatory requirement, or as holding for another award. Set it beside the same row's other columns (4.2.b44.foundation, 4.2.b44) and the framework descriptor qaa/fheq-2024/4.17.b8.2 (spine:7, strand:autonomy)."
  author-agent-dialogue: "Raise it when a master's student or tutor asks what professional development should look like by the end of the master's degree. Put it plainly: to a student, that by the end you should be able to support and lead colleagues in seeing and taking chances to develop and gain new competences as professional development requires; to staff, as where the course teaches and assesses it. Ask: \"What new competence do you want next, and how will you get it?\" Avoid reading the table aloud and holding anyone to another award's column as if it were their minimum."
```

### S5 Levels and alignment
<!-- label: both; status: drafted; basis: primary -->
```yaml
levels:
  - { id: "fheq:5", role: "cites", locator: "D1, 1.9; 2.6; 4.2 (column headings)" }
  - { id: "fheq:6", role: "cites", locator: "D1, 1.9; 2.6; 4.2 (column headings)" }
  - { id: "fheq:7", role: "cites", locator: "D1, 1.9; 4.2 (column headings)" }
  - { id: "fqheis:10", role: "cites", locator: "D1, 1.9 (SCQF Level 10); 2.6 (FQHEIS Level 10); 4.2 (SCQF Level 10)" }
  - { id: "fqheis:11", role: "cites", locator: "D1, 1.9 (SCQF Level 11)" }
crosswalks:
  - { from: "fheq:6", to: "fqheis:10", relation: "equivalent", basis: "stated (D1, 1.9; 2.6; the honours column heading in 4.2: FHEQ Level 6 / SCQF Level 10)" }
  - { from: "fheq:7", to: "fqheis:11", relation: "equivalent", basis: "stated (D1, 1.9: master's level courses at Level 7 on the FHEQ and Level 11 on the SCQF)" }
```

### S6 Themes
<!-- label: both; status: drafted; basis: primary -->
```yaml
- { id: "theme:edi", role: "carries", carriedIn: ["1.11", "1.12", "1.13", "1.15", "1.19", "2.13", "3.1", "3.15", "4.2"] }
- { id: "theme:accessibility", role: "carries", carriedIn: ["1.14", "1.15", "1.16", "2.9"] }
- { id: "theme:esd", role: "carries", carriedIn: ["1.17", "1.18", "1.19", "1.22", "4.2"] }
- { id: "theme:enterprise", role: "carries", carriedIn: ["1.20", "1.21", "1.22", "3.15"] }
```

### S7 Relations
<!-- label: both; status: drafted; basis: primary -->
```yaml
- { rel: "partOf", target: "collection: QAA Subject Benchmark Statements", note: "one of 54 held by stan" }
- { rel: "supersedes", target: "std:doc:qaa-veterinary-nursing-2019-benchmarks (not yet ingested)", note: "the second edition, 2019, revised by QAA to align with the 2018 Quality Code; the first edition was 2015 (section 6)" }
- { rel: "refersTo", target: "std:doc:qaa-fheq-2024-framework, Annex D", note: "degree classification descriptions for honours, cited in 4.2" }
- { rel: "refersTo", target: "std:doc:qaa-fheq-2024-framework", note: "levels 5, 6 and 7 (1.9, 2.6, 4.2)" }
- { rel: "refersTo", target: "std:doc:qaa-fqheis-2024-framework", note: "SCQF levels 10 and 11 (1.9, 2.6, 4.2)" }
- { rel: "refersTo", target: "std:doc:qaa-advancehe-esd-2021-guidance", note: "Education for Sustainable Development Guidance (1.17)" }
- { rel: "refersTo", target: "std:doc:qaa-enterprise-2018-guidance", note: "Enterprise and Entrepreneurship Education guidance (section 5 references only)" }
- { rel: "refersTo", target: "RCVS Day One Competences, Skills and Professional Behaviours for Veterinary Nurses (not yet ingested)", note: "1.7, 1.14, 2.2, 2.3, 2.4, 2.5, 2.11" }
- { rel: "refersTo", target: "RCVS Code of Professional Conduct for Veterinary Nurses (not yet ingested)", note: "1.4, 1.5, 3.9; the professional expectations table" }
- { rel: "refersTo", target: "RCVS Standards Framework for Veterinary Nurse Education and Training (not yet ingested)", note: "front matter" }
- { rel: "refersTo", target: "QAA Quality Code, Advice and Guidance", note: "front matter" }
```

### S8 Currency and review
<!-- label: source; status: drafted; basis: primary -->
```yaml
published: "2024-04"
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
- A science-based degree with a strong vocational focus, meant to make graduates ready to register as veterinary nurses when they graduate (D1, 1.6)
- Veterinary nurses give professional care grounded in knowledge of each patient's condition, across many settings and every life stage, mindful of the owner or keeper (D1, 1.1)
- The work aims at animal health, welfare and quality of life with as little pain and suffering as possible, and can be proactive or reactive, autonomous or collaborative (D1, 1.2)
- Registered nurses may give medical treatment and minor surgery that does not enter a body cavity, under a veterinary surgeon's direction, and educate owners and the public (D1, 1.3)
- Practice is regulated through RCVS registration, a code of conduct with five principles, continuing development and fitness to practise (D1, 1.4, 1.5)
- Licence to practise courses are built around the RCVS Day One Competences, Skills and Professional Behaviours and long clinical placements in approved training practices (D1, 1.7, 2.4, 2.5)
- Courses cover a range of species, with small animal and equine routes and, in some places, farm animal husbandry (D1, 3.1, 3.3 to 3.5)
- The statement covers three awards side by side: foundation degree, honours degree and master's degree (D1, 1.8, 1.9, 4.1)

### SB2 Themes in this subject
<!-- label: both; status: drafted; basis: primary -->
```yaml
- theme: theme:edi
  inThisSubject: "inclusive learning and placement settings; equity treated as a professional duty towards teams, owners and the public; respect for cultures and anti-discriminatory practice at every award, with barriers for people with protected characteristics analysed (D1, 1.11 to 1.13; 3.1; 4.2 tables)"
  statements: ["qaa/veterinary-nursing-2024/1.12", "qaa/veterinary-nursing-2024/1.13", "qaa/veterinary-nursing-2024/4.2.b8.foundation", "qaa/veterinary-nursing-2024/4.2.b8", "qaa/veterinary-nursing-2024/4.2.b8.masters", "qaa/veterinary-nursing-2024/4.2.b9.foundation", "qaa/veterinary-nursing-2024/4.2.b9", "qaa/veterinary-nursing-2024/4.2.b9.masters", "qaa/veterinary-nursing-2024/4.2.b10.foundation", "qaa/veterinary-nursing-2024/4.2.b10", "qaa/veterinary-nursing-2024/4.2.b10.masters", "qaa/veterinary-nursing-2024/4.2.b26.foundation", "qaa/veterinary-nursing-2024/4.2.b26", "qaa/veterinary-nursing-2024/4.2.b26.masters", "qaa/veterinary-nursing-2024/4.2.b43.foundation", "qaa/veterinary-nursing-2024/4.2.b43", "qaa/veterinary-nursing-2024/4.2.b43.masters"]
- theme: theme:accessibility
  inThisSubject: "accessibility from pre-application to after graduation, including equal workplace learning on placement and adjustable assessment that still lets every student meet the RCVS requirements (D1, 1.14 to 1.16; 2.9)"
  statements: ["qaa/veterinary-nursing-2024/1.14", "qaa/veterinary-nursing-2024/1.15", "qaa/veterinary-nursing-2024/1.16"]
- theme: theme:esd
  inThisSubject: "animal welfare as a sustainability goal; climate action, antimicrobial resistance, zoonoses and clinical waste; a sustainable approach to practice at every award (D1, 1.17 to 1.19; 4.2 table)"
  statements: ["qaa/veterinary-nursing-2024/1.17", "qaa/veterinary-nursing-2024/1.18", "qaa/veterinary-nursing-2024/4.2.b11.foundation", "qaa/veterinary-nursing-2024/4.2.b11", "qaa/veterinary-nursing-2024/4.2.b11.masters"]
- theme: theme:enterprise
  inThisSubject: "enterprise education designed with employers, professional bodies and service users, with group work building teamwork, negotiation and leadership, and authentic assessment for employability (D1, 1.20 to 1.22; 3.15)"
  statements: ["qaa/veterinary-nursing-2024/1.22"]
```

### SB3 Content and delivery
<!-- label: both; status: drafted; basis: primary -->
```yaml
areas:
  - { component: "3.1", gloss: "knowledge areas across species, from anatomy to legislation and anti-discriminatory practice" }
  - { component: "3.2", gloss: "appraising, applying and producing research" }
  - { component: "3.5", gloss: "basic farm animal husbandry in some curricula" }
  - { component: "3.7", gloss: "clinical and technical skills, from handling to maintaining anaesthesia" }
  - { component: "3.9", gloss: "ethics, cultural diversity, law and the professional code in course design" }
practices:
  - { component: "3.8", kind: "learning", gloss: "nursing skills learned in class and on placement" }
  - { component: "3.11", kind: "teaching", gloss: "methods chosen locally with the RCVS requirements" }
  - { component: "3.12", kind: "learning", gloss: "student-centred, reflective and critical learning for lifelong learning" }
  - { component: "3.16", kind: "assessment", gloss: "formative, self and peer assessment beside summative" }
  - { component: "3.17", kind: "assessment", gloss: "competence and fitness to practise judged by academic and clinical staff together" }
```

### SB4 Benchmark standards
<!-- label: both; status: drafted; basis: primary -->
```yaml
rungs:
  - { rung: "threshold", leadIn: "4.1", award: ["foundation degree", "bachelor's with honours", "master's"], items: 132 }
rungBases: "4.1 sets the minimum threshold standards for all three awards; each of the four tables (Generic skills; Principles and concepts: application; Subject knowledge, understanding and associated skills; Working as a professional veterinary nurse: expectations) carries the lead-in \"Graduates should be able to:\" and one column per award, so one row is one outcome at three awards. No typical or excellent rung is stated; 4.2 leaves achievement above threshold to each provider with Annex D. Rows by table: Generic skills 4.2.b1 to 4.2.b13; Principles and concepts: application 4.2.b14 to 4.2.b24; Subject knowledge, understanding and associated skills 4.2.b25 to 4.2.b31; Working as a professional veterinary nurse: expectations 4.2.b32 to 4.2.b44."
outcomeLists:
  - { leadIn: "3.10", gloss: "personal and professional abilities students should develop", items: 5, award: ["foundation degree", "bachelor's with honours"] }
outcomes:
  - { outcome: "arguing a case for the patient", threshold: "qaa/veterinary-nursing-2024/4.2.b1", typical: "none", excellent: "none", foundation: "qaa/veterinary-nursing-2024/4.2.b1.foundation", masters: "qaa/veterinary-nursing-2024/4.2.b1.masters", basis: "stated: one table row, columns placed by reading the flattened row", domain: "generic-skill", award: ["foundation degree", "bachelor's with honours", "master's"] }
  - { outcome: "independent learning and problem-solving", threshold: "qaa/veterinary-nursing-2024/4.2.b2", typical: "none", excellent: "none", foundation: "qaa/veterinary-nursing-2024/4.2.b2.foundation", masters: "qaa/veterinary-nursing-2024/4.2.b2.masters", basis: "stated: one table row, columns placed by reading the flattened row", domain: "generic-skill", award: ["foundation degree", "bachelor's with honours", "master's"] }
  - { outcome: "evidence-based practice", threshold: "qaa/veterinary-nursing-2024/4.2.b3", typical: "none", excellent: "none", foundation: "qaa/veterinary-nursing-2024/4.2.b3.foundation", masters: "qaa/veterinary-nursing-2024/4.2.b3.masters", basis: "stated: one table row, columns placed by reading the flattened row", domain: "generic-skill", award: ["foundation degree", "bachelor's with honours", "master's"] }
  - { outcome: "teamwork", threshold: "qaa/veterinary-nursing-2024/4.2.b4", typical: "none", excellent: "none", foundation: "qaa/veterinary-nursing-2024/4.2.b4.foundation", masters: "qaa/veterinary-nursing-2024/4.2.b4.masters", basis: "stated: one table row, columns placed by reading the flattened row", domain: "generic-skill", award: ["foundation degree", "bachelor's with honours", "master's"] }
  - { outcome: "digital skills", threshold: "qaa/veterinary-nursing-2024/4.2.b5", typical: "none", excellent: "none", foundation: "qaa/veterinary-nursing-2024/4.2.b5.foundation", masters: "qaa/veterinary-nursing-2024/4.2.b5.masters", basis: "stated: one table row, columns placed by reading the flattened row", domain: "generic-skill", award: ["foundation degree", "bachelor's with honours", "master's"] }
  - { outcome: "confidential information", threshold: "qaa/veterinary-nursing-2024/4.2.b6", typical: "none", excellent: "none", foundation: "qaa/veterinary-nursing-2024/4.2.b6.foundation", masters: "qaa/veterinary-nursing-2024/4.2.b6.masters", basis: "stated: one table row, columns placed by reading the flattened row", domain: "generic-skill", award: ["foundation degree", "bachelor's with honours", "master's"] }
  - { outcome: "self-awareness and confidence in the clinic", threshold: "qaa/veterinary-nursing-2024/4.2.b7", typical: "none", excellent: "none", foundation: "qaa/veterinary-nursing-2024/4.2.b7.foundation", masters: "qaa/veterinary-nursing-2024/4.2.b7.masters", basis: "stated: one table row, columns placed by reading the flattened row", domain: "generic-skill", award: ["foundation degree", "bachelor's with honours", "master's"] }
  - { outcome: "respect for diversity and anti-discriminatory behaviour", threshold: "qaa/veterinary-nursing-2024/4.2.b8", typical: "none", excellent: "none", foundation: "qaa/veterinary-nursing-2024/4.2.b8.foundation", masters: "qaa/veterinary-nursing-2024/4.2.b8.masters", basis: "stated: one table row, columns placed by reading the flattened row", domain: "generic-skill", award: ["foundation degree", "bachelor's with honours", "master's"] }
  - { outcome: "barriers for people with protected characteristics", threshold: "qaa/veterinary-nursing-2024/4.2.b9", typical: "none", excellent: "none", foundation: "qaa/veterinary-nursing-2024/4.2.b9.foundation", masters: "qaa/veterinary-nursing-2024/4.2.b9.masters", basis: "stated: one table row, columns placed by reading the flattened row", domain: "generic-skill", award: ["foundation degree", "bachelor's with honours", "master's"] }
  - { outcome: "non-judgemental practice", threshold: "qaa/veterinary-nursing-2024/4.2.b10", typical: "none", excellent: "none", foundation: "qaa/veterinary-nursing-2024/4.2.b10.foundation", masters: "qaa/veterinary-nursing-2024/4.2.b10.masters", basis: "stated: one table row, columns placed by reading the flattened row", domain: "generic-skill", award: ["foundation degree", "bachelor's with honours", "master's"] }
  - { outcome: "sustainable practice", threshold: "qaa/veterinary-nursing-2024/4.2.b11", typical: "none", excellent: "none", foundation: "qaa/veterinary-nursing-2024/4.2.b11.foundation", masters: "qaa/veterinary-nursing-2024/4.2.b11.masters", basis: "stated: one table row, columns placed by reading the flattened row", domain: "generic-skill", award: ["foundation degree", "bachelor's with honours", "master's"] }
  - { outcome: "reflective practice", threshold: "qaa/veterinary-nursing-2024/4.2.b12", typical: "none", excellent: "none", foundation: "qaa/veterinary-nursing-2024/4.2.b12.foundation", masters: "qaa/veterinary-nursing-2024/4.2.b12.masters", basis: "stated: one table row, columns placed by reading the flattened row", domain: "generic-skill", award: ["foundation degree", "bachelor's with honours", "master's"] }
  - { outcome: "well-being and fitness to practise", threshold: "qaa/veterinary-nursing-2024/4.2.b13", typical: "none", excellent: "none", foundation: "qaa/veterinary-nursing-2024/4.2.b13.foundation", masters: "qaa/veterinary-nursing-2024/4.2.b13.masters", basis: "stated: one table row, columns placed by reading the flattened row", domain: "generic-skill", award: ["foundation degree", "bachelor's with honours", "master's"] }
  - { outcome: "theory in holistic care", threshold: "qaa/veterinary-nursing-2024/4.2.b14", typical: "none", excellent: "none", foundation: "qaa/veterinary-nursing-2024/4.2.b14.foundation", masters: "qaa/veterinary-nursing-2024/4.2.b14.masters", basis: "stated: one table row, columns placed by reading the flattened row", domain: "subject-skill", award: ["foundation degree", "bachelor's with honours", "master's"] }
  - { outcome: "managing clinical risk", threshold: "qaa/veterinary-nursing-2024/4.2.b15", typical: "none", excellent: "none", foundation: "qaa/veterinary-nursing-2024/4.2.b15.foundation", masters: "qaa/veterinary-nursing-2024/4.2.b15.masters", basis: "stated: one table row, columns placed by reading the flattened row", domain: "subject-skill", award: ["foundation degree", "bachelor's with honours", "master's"] }
  - { outcome: "promoting animal health and welfare", threshold: "qaa/veterinary-nursing-2024/4.2.b16", typical: "none", excellent: "none", foundation: "qaa/veterinary-nursing-2024/4.2.b16.foundation", masters: "qaa/veterinary-nursing-2024/4.2.b16.masters", basis: "stated: one table row, columns placed by reading the flattened row", domain: "subject-skill", award: ["foundation degree", "bachelor's with honours", "master's"] }
  - { outcome: "evidence behind clinical decisions", threshold: "qaa/veterinary-nursing-2024/4.2.b17", typical: "none", excellent: "none", foundation: "qaa/veterinary-nursing-2024/4.2.b17.foundation", masters: "qaa/veterinary-nursing-2024/4.2.b17.masters", basis: "stated: one table row, columns placed by reading the flattened row", domain: "subject-skill", award: ["foundation degree", "bachelor's with honours", "master's"] }
  - { outcome: "nursing assessment", threshold: "qaa/veterinary-nursing-2024/4.2.b18", typical: "none", excellent: "none", foundation: "qaa/veterinary-nursing-2024/4.2.b18.foundation", masters: "qaa/veterinary-nursing-2024/4.2.b18.masters", basis: "stated: one table row, columns placed by reading the flattened row", domain: "subject-skill", award: ["foundation degree", "bachelor's with honours", "master's"] }
  - { outcome: "priorities and care delivery", threshold: "qaa/veterinary-nursing-2024/4.2.b19", typical: "none", excellent: "none", foundation: "qaa/veterinary-nursing-2024/4.2.b19.foundation", masters: "qaa/veterinary-nursing-2024/4.2.b19.masters", basis: "stated: one table row, columns placed by reading the flattened row", domain: "subject-skill", award: ["foundation degree", "bachelor's with honours", "master's"] }
  - { outcome: "care planning and research", threshold: "qaa/veterinary-nursing-2024/4.2.b20", typical: "none", excellent: "none", foundation: "qaa/veterinary-nursing-2024/4.2.b20.foundation", masters: "qaa/veterinary-nursing-2024/4.2.b20.masters", basis: "stated: one table row, columns placed by reading the flattened row", domain: "subject-skill", award: ["foundation degree", "bachelor's with honours", "master's"] }
  - { outcome: "accountability and the context of care", threshold: "qaa/veterinary-nursing-2024/4.2.b21", typical: "none", excellent: "none", foundation: "qaa/veterinary-nursing-2024/4.2.b21.foundation", masters: "qaa/veterinary-nursing-2024/4.2.b21.masters", basis: "stated: one table row, columns placed by reading the flattened row", domain: "subject-skill", award: ["foundation degree", "bachelor's with honours", "master's"] }
  - { outcome: "outcomes of interventions", threshold: "qaa/veterinary-nursing-2024/4.2.b22", typical: "none", excellent: "none", foundation: "qaa/veterinary-nursing-2024/4.2.b22.foundation", masters: "qaa/veterinary-nursing-2024/4.2.b22.masters", basis: "stated: one table row, columns placed by reading the flattened row", domain: "subject-skill", award: ["foundation degree", "bachelor's with honours", "master's"] }
  - { outcome: "multidisciplinary teamwork", threshold: "qaa/veterinary-nursing-2024/4.2.b23", typical: "none", excellent: "none", foundation: "qaa/veterinary-nursing-2024/4.2.b23.foundation", masters: "qaa/veterinary-nursing-2024/4.2.b23.masters", basis: "stated: one table row, columns placed by reading the flattened row", domain: "subject-skill", award: ["foundation degree", "bachelor's with honours", "master's"] }
  - { outcome: "ethics in patient care", threshold: "qaa/veterinary-nursing-2024/4.2.b24", typical: "none", excellent: "none", foundation: "qaa/veterinary-nursing-2024/4.2.b24.foundation", masters: "qaa/veterinary-nursing-2024/4.2.b24.masters", basis: "stated: one table row, columns placed by reading the flattened row", domain: "subject-skill", award: ["foundation degree", "bachelor's with honours", "master's"] }
  - { outcome: "core subject knowledge", threshold: "qaa/veterinary-nursing-2024/4.2.b25", typical: "none", excellent: "none", foundation: "qaa/veterinary-nursing-2024/4.2.b25.foundation", masters: "qaa/veterinary-nursing-2024/4.2.b25.masters", basis: "stated: one table row, columns placed by reading the flattened row", domain: "knowledge", award: ["foundation degree", "bachelor's with honours", "master's"] }
  - { outcome: "cultural awareness and anti-discriminatory practice", threshold: "qaa/veterinary-nursing-2024/4.2.b26", typical: "none", excellent: "none", foundation: "qaa/veterinary-nursing-2024/4.2.b26.foundation", masters: "qaa/veterinary-nursing-2024/4.2.b26.masters", basis: "stated: one table row, columns placed by reading the flattened row", domain: "subject-skill", award: ["foundation degree", "bachelor's with honours", "master's"] }
  - { outcome: "communication and evidence-based decisions", threshold: "qaa/veterinary-nursing-2024/4.2.b27", typical: "none", excellent: "none", foundation: "qaa/veterinary-nursing-2024/4.2.b27.foundation", masters: "qaa/veterinary-nursing-2024/4.2.b27.masters", basis: "stated: one table row, columns placed by reading the flattened row", domain: "generic-skill", award: ["foundation degree", "bachelor's with honours", "master's"] }
  - { outcome: "therapeutic client relationships", threshold: "qaa/veterinary-nursing-2024/4.2.b28", typical: "none", excellent: "none", foundation: "qaa/veterinary-nursing-2024/4.2.b28.foundation", masters: "qaa/veterinary-nursing-2024/4.2.b28.masters", basis: "stated: one table row, columns placed by reading the flattened row", domain: "subject-skill", award: ["foundation degree", "bachelor's with honours", "master's"] }
  - { outcome: "contemporary evidence-based nursing", threshold: "qaa/veterinary-nursing-2024/4.2.b29", typical: "none", excellent: "none", foundation: "qaa/veterinary-nursing-2024/4.2.b29.foundation", masters: "qaa/veterinary-nursing-2024/4.2.b29.masters", basis: "stated: one table row, columns placed by reading the flattened row", domain: "subject-skill", award: ["foundation degree", "bachelor's with honours", "master's"] }
  - { outcome: "evidence and data in judgement", threshold: "qaa/veterinary-nursing-2024/4.2.b30", typical: "none", excellent: "none", foundation: "qaa/veterinary-nursing-2024/4.2.b30.foundation", masters: "qaa/veterinary-nursing-2024/4.2.b30.masters", basis: "stated: one table row, columns placed by reading the flattened row", domain: "subject-skill", award: ["foundation degree", "bachelor's with honours", "master's"] }
  - { outcome: "reflection for self-improvement", threshold: "qaa/veterinary-nursing-2024/4.2.b31", typical: "none", excellent: "none", foundation: "qaa/veterinary-nursing-2024/4.2.b31.foundation", masters: "qaa/veterinary-nursing-2024/4.2.b31.masters", basis: "stated: one table row, columns placed by reading the flattened row", domain: "generic-skill", award: ["foundation degree", "bachelor's with honours", "master's"] }
  - { outcome: "managing self and others under the code", threshold: "qaa/veterinary-nursing-2024/4.2.b32", typical: "none", excellent: "none", foundation: "qaa/veterinary-nursing-2024/4.2.b32.foundation", masters: "qaa/veterinary-nursing-2024/4.2.b32.masters", basis: "stated: one table row, columns placed by reading the flattened row", domain: "subject-skill", award: ["foundation degree", "bachelor's with honours", "master's"] }
  - { outcome: "applying knowledge across clinical settings", threshold: "qaa/veterinary-nursing-2024/4.2.b33", typical: "none", excellent: "none", foundation: "qaa/veterinary-nursing-2024/4.2.b33.foundation", masters: "qaa/veterinary-nursing-2024/4.2.b33.masters", basis: "stated: one table row, columns placed by reading the flattened row", domain: "subject-skill", award: ["foundation degree", "bachelor's with honours", "master's"] }
  - { outcome: "collaborative therapeutic and preventive care", threshold: "qaa/veterinary-nursing-2024/4.2.b34", typical: "none", excellent: "none", foundation: "qaa/veterinary-nursing-2024/4.2.b34.foundation", masters: "qaa/veterinary-nursing-2024/4.2.b34.masters", basis: "stated: one table row, columns placed by reading the flattened row", domain: "subject-skill", award: ["foundation degree", "bachelor's with honours", "master's"] }
  - { outcome: "empathy in challenging situations", threshold: "qaa/veterinary-nursing-2024/4.2.b35", typical: "none", excellent: "none", foundation: "qaa/veterinary-nursing-2024/4.2.b35.foundation", masters: "qaa/veterinary-nursing-2024/4.2.b35.masters", basis: "stated: one table row, columns placed by reading the flattened row", domain: "subject-skill", award: ["foundation degree", "bachelor's with honours", "master's"] }
  - { outcome: "the professional, ethical and legal framework", threshold: "qaa/veterinary-nursing-2024/4.2.b36", typical: "none", excellent: "none", foundation: "qaa/veterinary-nursing-2024/4.2.b36.foundation", masters: "qaa/veterinary-nursing-2024/4.2.b36.masters", basis: "stated: one table row, columns placed by reading the flattened row", domain: "subject-skill", award: ["foundation degree", "bachelor's with honours", "master's"] }
  - { outcome: "responsibility and impartial decisions", threshold: "qaa/veterinary-nursing-2024/4.2.b37", typical: "none", excellent: "none", foundation: "qaa/veterinary-nursing-2024/4.2.b37.foundation", masters: "qaa/veterinary-nursing-2024/4.2.b37.masters", basis: "stated: one table row, columns placed by reading the flattened row", domain: "subject-skill", award: ["foundation degree", "bachelor's with honours", "master's"] }
  - { outcome: "a safe clinical environment", threshold: "qaa/veterinary-nursing-2024/4.2.b38", typical: "none", excellent: "none", foundation: "qaa/veterinary-nursing-2024/4.2.b38.foundation", masters: "qaa/veterinary-nursing-2024/4.2.b38.masters", basis: "stated: one table row, columns placed by reading the flattened row", domain: "subject-skill", award: ["foundation degree", "bachelor's with honours", "master's"] }
  - { outcome: "guidance, role-modelling and mentorship", threshold: "qaa/veterinary-nursing-2024/4.2.b39", typical: "none", excellent: "none", foundation: "qaa/veterinary-nursing-2024/4.2.b39.foundation", masters: "qaa/veterinary-nursing-2024/4.2.b39.masters", basis: "stated: one table row, columns placed by reading the flattened row", domain: "subject-skill", award: ["foundation degree", "bachelor's with honours", "master's"] }
  - { outcome: "roles, delegation and supervision", threshold: "qaa/veterinary-nursing-2024/4.2.b40", typical: "none", excellent: "none", foundation: "qaa/veterinary-nursing-2024/4.2.b40.foundation", masters: "qaa/veterinary-nursing-2024/4.2.b40.masters", basis: "stated: one table row, columns placed by reading the flattened row", domain: "subject-skill", award: ["foundation degree", "bachelor's with honours", "master's"] }
  - { outcome: "advocacy, advice and well-being", threshold: "qaa/veterinary-nursing-2024/4.2.b41", typical: "none", excellent: "none", foundation: "qaa/veterinary-nursing-2024/4.2.b41.foundation", masters: "qaa/veterinary-nursing-2024/4.2.b41.masters", basis: "stated: one table row, columns placed by reading the flattened row", domain: "subject-skill", award: ["foundation degree", "bachelor's with honours", "master's"] }
  - { outcome: "research and the evidence base", threshold: "qaa/veterinary-nursing-2024/4.2.b42", typical: "none", excellent: "none", foundation: "qaa/veterinary-nursing-2024/4.2.b42.foundation", masters: "qaa/veterinary-nursing-2024/4.2.b42.masters", basis: "stated: one table row, columns placed by reading the flattened row", domain: "subject-skill", award: ["foundation degree", "bachelor's with honours", "master's"] }
  - { outcome: "equality, diversity and inclusion in practice", threshold: "qaa/veterinary-nursing-2024/4.2.b43", typical: "none", excellent: "none", foundation: "qaa/veterinary-nursing-2024/4.2.b43.foundation", masters: "qaa/veterinary-nursing-2024/4.2.b43.masters", basis: "stated: one table row, columns placed by reading the flattened row", domain: "subject-skill", award: ["foundation degree", "bachelor's with honours", "master's"] }
  - { outcome: "professional development", threshold: "qaa/veterinary-nursing-2024/4.2.b44", typical: "none", excellent: "none", foundation: "qaa/veterinary-nursing-2024/4.2.b44.foundation", masters: "qaa/veterinary-nursing-2024/4.2.b44.masters", basis: "stated: one table row, columns placed by reading the flattened row", domain: "generic-skill", award: ["foundation degree", "bachelor's with honours", "master's"] }
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
- { body: "Royal College of Veterinary Surgeons (RCVS)", says: "the PSRB for the subject; keeps the non-statutory register of veterinary nurses and its code of conduct; sets the Standards Framework for Veterinary Nurse Education and the Day One Competences, Skills and Professional Behaviours; accredits licence to practise courses, training practices and post-registration qualifications; registered nurses use RVN or Cert AVN (D1, front matter; 1.4; 1.7; 1.14; 2.2 to 2.5; 2.8; 2.9; 2.11; 3.9; 3.11; 3.17)", requirements: "not yet ingested (Part E)" }
- { body: "Office for Students", says: "in England, Subject Benchmark Statements are not sector-recognised standards under its regulatory framework (D1, front matter)", requirements: "not yet ingested (Part E)" }
```

### SB6 Cross-cutting references
<!-- label: both; status: drafted; basis: primary -->
```yaml
themes:
  - { id: "theme:edi", named: "Equality, diversity and inclusion", carriedIn: ["1.11", "1.12", "1.13", "1.15", "1.19", "2.13", "3.1", "3.15", "4.2"], statements: ["1.12", "1.13", "4.2.b8.foundation", "4.2.b8", "4.2.b8.masters", "4.2.b9.foundation", "4.2.b9", "4.2.b9.masters", "4.2.b10.foundation", "4.2.b10", "4.2.b10.masters", "4.2.b26.foundation", "4.2.b26", "4.2.b26.masters", "4.2.b43.foundation", "4.2.b43", "4.2.b43.masters"] }
  - { id: "theme:accessibility", named: "Accessibility (front matter: accessibility and the needs of disabled students)", carriedIn: ["1.14", "1.15", "1.16", "2.9"], statements: ["1.14", "1.15", "1.16"] }
  - { id: "theme:esd", named: "Sustainability (front matter: education for sustainable development)", carriedIn: ["1.17", "1.18", "1.19", "1.22", "4.2"], statements: ["1.17", "1.18", "4.2.b11.foundation", "4.2.b11", "4.2.b11.masters"] }
  - { id: "theme:enterprise", named: "Enterprise and entrepreneurship education (front matter: employability, entrepreneurship and enterprise education)", carriedIn: ["1.20", "1.21", "1.22", "3.15"], statements: ["1.22"] }
frameworks:
  - { framework: "fheq", levels: ["fheq:5", "fheq:6", "fheq:7"], citedIn: ["1.9", "2.6", "4.2"] }
  - { framework: "scqf", levels: ["fqheis:10", "fqheis:11"], citedIn: ["1.9", "2.6", "4.2"] }
bodies:
  - { body: "Royal College of Veterinary Surgeons", citedIn: ["front matter", "1.4", "1.7", "1.14", "2.2", "2.3", "2.5", "2.8", "2.9", "3.9", "3.11", "3.17"] }
  - { body: "Office for Students", citedIn: ["front matter"] }
sharedDocuments:
  - { document: "std:doc:qaa-fheq-2024-framework, Annex D", named: "Annex D in The Frameworks for Higher Education Qualifications of UK Degree-Awarding Bodies", citedIn: ["4.2"], role: "common descriptions of the four honours classifications, for judging achievement above threshold" }
  - { document: "std:doc:qaa-fheq-2024-framework", named: "The Frameworks for Higher Education Qualifications (FHEQ; FQHEIS; SCQF levels)", citedIn: ["1.9", "2.6", "4.2"], role: "the levels of the three awards" }
  - { document: "std:doc:qaa-advancehe-esd-2021-guidance", named: "QAA and Advance HE's Education for Sustainable Development Guidance, 2021", citedIn: ["1.17"], role: "the frame for the sustainability theme" }
  - { document: "std:doc:qaa-enterprise-2018-guidance", named: "Enterprise and Entrepreneurship Education: Guidance for UK Higher Education Providers (2018)", citedIn: ["section 5"], role: "listed as a further resource for the enterprise theme" }
  - { document: "QAA Quality Code, Advice and Guidance (not yet ingested)", named: "Advice and Guidance to support the Quality Code", citedIn: ["front matter"], role: "course design, teaching, external expertise, monitoring" }
  - { document: "QAA Glossary (not ingested)", named: "QAA's Glossary", citedIn: ["front matter"], role: "explains unfamiliar terms" }
  - { document: "Quality Assessment Framework for Wales; Quality Enhancement Framework (Scotland) (not ingested)", named: "Quality Assessment Framework for Wales; Quality Enhancement Framework", citedIn: ["front matter"], role: "the statement's status in Wales and Scotland" }
  - { document: "RCVS documents (not yet ingested: Part E, D3)", named: "Day One Competences, Day One Skills List, Professional Behaviours and Attributes; Code of Professional Conduct for Veterinary Nurses; Standards Framework for Veterinary Nurse Education; Veterinary Nurse Registration Rules 2017; Post-registration Framework for Veterinary Nursing", citedIn: ["front matter", "1.4", "1.5", "1.7", "1.14", "2.2", "2.3", "2.5", "3.9"], role: "the professional body's requirements for registration and accreditation" }
  - { document: "UN Sustainable Development Goals; UN Principles for Responsible Management Education (external)", named: "UN Sustainable Development Goals; PRME", citedIn: ["1.17", "1.18"], role: "the frame of sustainable development and responsible management" }
  - { document: "IPCC (2022) (external)", named: "IPCC, 2022", citedIn: ["1.18"], role: "the emissions target" }
  - { document: "Vet Sustain (2020) (external)", named: "Vet Sustain 2020", citedIn: ["1.19"], role: "source of the example sustainability topics" }
```

## Part B Terminology
<!-- The statement has no glossary of its own unless Part E says so; these are terms it defines in its text. -->

### B1 Concepts
<!-- label: both; status: drafted; basis: primary -->
```yaml
- { slug: "day-one-competences", definition: "the RCVS list of competences a student veterinary nurse must gain and evidence to join the register, abbreviated DOC (D1, 1.7)", beneficiaryDefinition: "the abilities you must show before you can register as a veterinary nurse", scopeNote: "set by the RCVS; with DOS and PB", category: "unknown", practices: ["education"] }
- { slug: "day-one-skills-list", definition: "the RCVS list of practical skills a student veterinary nurse must meet to register, abbreviated DOS (D1, 1.7, 2.4)", beneficiaryDefinition: "the hands-on skills you must master before you can register", scopeNote: "set by the RCVS", category: "unknown", practices: ["education"] }
- { slug: "professional-behaviours-and-attributes", definition: "the RCVS professional behaviours required for registration, abbreviated PB (D1, 1.7)", beneficiaryDefinition: "how you are expected to behave as a professional before you can register", scopeNote: "set by the RCVS", category: "unknown", practices: ["education"] }
- { slug: "registered-veterinary-nurse", definition: "a veterinary nurse on the RCVS register, entitled to the postnominals RVN (D1, front matter; 1.6)", beneficiaryDefinition: "a qualified veterinary nurse on the professional register", scopeNote: "Cert AVN marks an accredited post-registration qualification", category: "unknown", practices: ["education"] }
- { slug: "licence-to-practise-qualification", definition: "a course fully accredited by the RCVS whose graduates may apply to the register (D1, front matter; 1.7; 2.2)", beneficiaryDefinition: "a course that lets you apply to register when you finish", scopeNote: "the issuer spells it Licence and License", category: "unknown", practices: ["education"] }
- { slug: "training-practice", definition: "a veterinary practice approved for clinical placement, abbreviated TP, with auxiliary training practices beside it (D1, 2.5, 2.12)", beneficiaryDefinition: "the approved clinic where you do your placement", scopeNote: "approved and monitored by course providers (2.12)", category: "unknown", practices: ["education"] }
- { slug: "accessibility", definition: "whether every part of a course, however met, can be understood by everyone (D1, 1.14)", beneficiaryDefinition: "whether every part of your course works for you, whatever your needs", scopeNote: "a cross-cutting theme", category: "unknown", practices: ["education"] }
```

### B2a Terms as the issuer defines them
<!-- label: source; status: drafted; basis: primary -->
```yaml
- { concept: "day-one-competences", form: "Day One Competences", lang: "en", partOfSpeech: "noun-phrase", termStatus: "preferred", register: "discipline-specific" }
- { concept: "day-one-competences", form: "DOC", lang: "en", partOfSpeech: "noun", termStatus: "admitted", register: "discipline-specific" }
- { concept: "day-one-skills-list", form: "Day One Skills List", lang: "en", partOfSpeech: "noun-phrase", termStatus: "preferred", register: "discipline-specific" }
- { concept: "day-one-skills-list", form: "DOS", lang: "en", partOfSpeech: "noun", termStatus: "admitted", register: "discipline-specific" }
- { concept: "professional-behaviours-and-attributes", form: "Professional Behaviours and Attributes", lang: "en", partOfSpeech: "noun-phrase", termStatus: "preferred", register: "discipline-specific" }
- { concept: "professional-behaviours-and-attributes", form: "PB", lang: "en", partOfSpeech: "noun", termStatus: "admitted", register: "discipline-specific" }
- { concept: "registered-veterinary-nurse", form: "registered veterinary nurse", lang: "en", partOfSpeech: "noun-phrase", termStatus: "preferred", register: "formal" }
- { concept: "registered-veterinary-nurse", form: "RVN", lang: "en", partOfSpeech: "noun", termStatus: "admitted", register: "discipline-specific" }
- { concept: "licence-to-practise-qualification", form: "License to Practise Qualification", lang: "en", partOfSpeech: "noun-phrase", termStatus: "preferred", register: "discipline-specific" }
- { concept: "training-practice", form: "training practice", lang: "en", partOfSpeech: "noun-phrase", termStatus: "preferred", register: "discipline-specific" }
- { concept: "training-practice", form: "TP", lang: "en", partOfSpeech: "noun", termStatus: "admitted", register: "discipline-specific" }
- { concept: "accessibility", form: "accessibility", lang: "en", partOfSpeech: "noun", termStatus: "preferred", register: "formal" }
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
  title: "Subject Benchmark Statement Veterinary Nursing"
  edition: "April 2024 (third edition)"
  year: 2024
  url: unknown (the QAA page; the text came by stan's extraction)
  retrieved: "held from stan: wkspc2615-QAAVector mapped/veterinary-nursing-2024/veterinary-nursing-2024.raw.txt, commit 366bcb99a01118f2c4c3ebfa2a8337596bddc455; received 2026-10-03"
  licence: QAA copyright
  tier: primary
  readVia: direct
  held: 429fe4f71226a5bc708925e16ffe80c35e0c704c40f197712c3b05e70842aa71
  heldFiles: ["wkspc2601-library/txt/qaa-2024-veterinary-nursing-subject-benchmark-statement-standard.txt", "wkspc2601-library/txt/qaa-2024-veterinary-nursing-subject-benchmark-statement-standard.norm.txt", "wkspc2601-library/records/qaa-2024-veterinary-nursing-subject-benchmark-statement-standard.chunks.json", "wkspc2601-library/records/qaa-2024-veterinary-nursing-subject-benchmark-statement-standard.held.json"]
  citedIn: [S1, S2, S3, S4, S4a, S5, S6, S7, SB1, SB2, SB3, SB4, SB5, SB6]
```

### D2 Research log
```yaml
- { ref: D1, tier: primary, consulted: 2026-10-03, pass: P1, outcome: "read whole, direct, from the normalised text; skeleton by tools/std_prep.py, document by tools/bm_build.py" }
- { ref: "ADAPT subj HESA stores, cah.json and hecos.json (designs/ingest/standards/subj/vocab)", tier: primary, consulted: 2026-10-03, pass: P1, outcome: "codes for statedSubjects and subjects" }
```

### D3 Wanted sources
```yaml
- { w: "W-std-0104", citation: "Royal College of Veterinary Surgeons, Day One Competences, Skills and Professional Behaviours for Veterinary Nurses", settles: ["SB5", "S7"], asked: "2026-10-03", state: "wanted" }
- { w: "W-std-0105", citation: "Royal College of Veterinary Surgeons, Code of Professional Conduct for Veterinary Nurses", settles: ["SB5", "S7"], asked: "2026-10-03", state: "wanted" }
- { w: "W-std-0106", citation: "Royal College of Veterinary Surgeons, Standards Framework for Veterinary Nurse Education and Training", settles: ["SB5", "S7"], asked: "2026-10-03", state: "wanted" }
- { w: "W-std-0107", citation: "Royal College of Veterinary Surgeons, Post Registration Framework for Veterinary Nursing; Veterinary Nurse Registration Rules 2017", settles: ["SB5"], asked: "2026-10-03", state: "wanted" }
- { w: "W-std-0108", citation: "QAA, Subject Benchmark Statement: Veterinary Nursing, second edition (2019)", settles: ["S7"], asked: "2026-10-03", state: "wanted" }
```

## Part E Gaps and questions
- SB4, rungs: no typical or excellent rung. 4.1 states minimum threshold standards for three awards; the four section 4 tables give one column per award (foundation degree, FHEQ 5; honours, FHEQ 6 / SCQF 10; master's, FHEQ 7), not per rung. Recorded as rung threshold throughout, 132 cells in 44 rows (pattern differs from Psychology).
- S4, ids: the tables carry no issuer numbers and sit after 4.2 under their own headings. Rows are numbered 4.2.b1 to 4.2.b44 in held-text order (tables listed in SB4 rungBases); the honours cell keeps the base id, the master's cell takes .masters (brief convention) and the foundation cell takes .foundation, a new suffix for a third award column: for std to confirm.
- S4, force: each table cell is recorded as threshold with forceFrom 4.1 (the minimum for the award); the tables' own lead-in is "Graduates should be able to:", kept in every version as should.
- S4, flattened tables: cells placed by reading each row in column order. Doubtful placements for P3: generic skills row 3 (4.2.b3), where "Critically evaluate arguments, assumptions, abstract concepts and data" is read as the second sentence of the honours cell, not a cell of its own; professional expectations row 10 (4.2.b41), where "Awareness of factors that impact on mental and physical health and well-being." is read as the start of the master's cell; subject knowledge row 6 (4.2.b30), where the honours cell (creating new theory) reads as more advanced than the master's cell (evaluation), kept as placed.
- S4, identical cells: rows 4.2.b7, 4.2.b8, 4.2.b10, 4.2.b13 (honours and master's), 4.2.b33 (foundation and honours) and 4.2.b43 repeat the same wording in more than one column; each column is still its own record with the same paraphrase.
- SB4, outcomes: each row links its three award cells (foundation, masters keys beside threshold) with basis stated, since the issuer's table rows pair them; gradeOf is not used because the columns are awards, not rungs. No GRADE links.
- S4, held text: the issuer spells "practise" as a noun in "professional practise" (4.2.b25, honours; all three cells of 4.2.b32) and "evidenced-based" in 4.2.b16; kept in source, corrected in our words.
- S4, statements taken from sections 1 to 3 (D-std-0002 (a)): obliging paragraphs 1.4, 1.6, 1.7, 1.12 to 1.16, 1.18, 1.22, 2.2 to 2.5, 2.8, 2.10 to 2.12, 2.14, 3.13 to 3.15, 3.18 and 4.2's first part; the 2.1 minimum content list (11 items); the 3.10 outcome list (5 items); 2.6 for its master's outcome in will.
- S4, obliging words outside the five, recorded as describes for Abbott: 1.17 "There is an expectation that" ERS are integrated; 2.9 "Providers are expected to" set up oversight; 3.3 and 3.4 "It is anticipated that" holders are proficient. 2.6 also uses "it is expected that" and "would be expected", taken with its will sentence.
- S4, required read as must: 2.2 ("This is a requirement for ... accreditation").
- S4, mixed force: 2.3 is will for foundation and honours and should for master's, recorded as will; 1.7 is should on the course, must from the RCVS on the student, recorded as should.
- S4, not statements: 1.3 ("Veterinary nurses are able to") describes the registered profession, not graduates; 1.5 lists the code's principles; 1.8 and 1.9 describe the statement; 1.19 lists topics that "could usefully be incorporated"; 2.15 describes external examining; 3.2 ("can cover") and 3.5 describe content; 4.1 is the threshold lead-in.
- S4, plain-present provider norms not taken as statements (template open point 5): 2.7, 2.11's first sentence, 2.13 ("will form part" of review), 3.1 ("aim to develop"), 3.6, 3.7, 3.8, 3.9 ("Courses are designed to ensure"), 3.11, 3.12, 3.16, 3.17.
- S4, items under a may: 1.14's three examples follow "It may include", so 1.14 is one record over its whole span, not three item records.
- S4, 3.3 is one record over the stem and its species list (cats, dogs, exotic species), since the items are species, not outcomes.
- S4, levels inferred: 3.10's items take fheq:5 and the awards foundation and honours, because section 3 frames content for foundation and honours courses (3.1, 3.11); the list names no award.
- S4, 4.2: recorded by find over its own paragraph only; the skeleton's 4.2 span ran to the end of the tables.
- S3, headings: the four table headings (Generic skills; Principles and concepts: application; Subject knowledge, understanding and associated skills; Working as a professional veterinary nurse: expectations) are not numbered components; the builder shows 4.2's heading, Introduction, in each cell's headingPath. Each cell names its table in appliesTo.
- S3, skeleton: the 3.3 to 3.6 paragraphs fall under the issuer's heading Research and evidence-based practice although they concern species and skills; recorded as the issuer places them.
- Subjects: HECoS 100532 veterinary nursing matches the stated subject; CAH05-01-02 (others in veterinary sciences) is inferred from the HECoS mapping, held back from lookups until P3.
- S5: no Scottish level is stated for the foundation degree (the FHEQ's Table 1 has none); fqheis:11 for master's is stated in 1.9 only, not in the table heading.
- SB5, SB6: the RCVS requirements (Day One Competences, Skills and Professional Behaviours; the code of conduct; the Standards Framework; the registration rules; the post-registration framework) are not yet ingested (D3). The Office for Students' regulatory framework is not ingested.
- SB6, themes: generative AI and other themes are not named. Mental health and well-being appear (1.19; the tables) but no shared theme id exists for them; not tagged.
- SB6: the enterprise guidance (2018) is cited only in section 5's list of references, twice.
- Front matter: the edition line reads "Third edition, April 2024"; section 6 dates the earlier editions 2019 and 2015.
- S1, licence: the text gives a copyright notice and no re-use terms.
- S9: not researched in P1.
- Patterns that differ from Psychology: threshold only, three awards in table columns (foundation, honours, master's); a PSRB (RCVS) whose Day One requirements run through the design sections; many provider duties in should; no rung lists in prose.
- ST-12: versions here run to the lengths the content needs; no length range is yet set.

---

## Change notes
- 0.1.2, 3 October 2026, 21:02: moved with its held text from UNI to the source library repo (`wkspc2601-library/ingested/standards/`, texts in `txt/`, records in `records/`); paths only (Abbott, 20:56; std N-0119).
- 0.1.1, 3 October 2026, 20:20: obliging words outside the five read as must, "ought to" as should, on statements outside the rungs, each marked on its force line (Abbott, 20:17; D-std-0016).
- 0.1.0, 2026-10-03 18:44: researched by run frame 0.1.1-draft and standards run layer 0.7.0-draft, std, run 0134 (P1); built by tools/bm_build.py.
