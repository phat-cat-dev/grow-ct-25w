---
id: std:doc:qaa-public-policy-and-public-administration-2025-benchmarks
title: "Subject Benchmark Statement Public Policy and Public Administration"
profile: standards/subject-benchmark
profileVersion: 0.2.0-draft
issuer: QAA
kind: subject-benchmark
jurisdiction: [UK]
subjectScope: subjects
subjects:
  - { scheme: "hecos", code: "100647", label: "public policy", basis: "stated" }
  - { scheme: "hecos", code: "100090", label: "public administration", basis: "stated" }
  - { scheme: "cah", code: "CAH15-01-03", label: "social policy", basis: "inferred" }
  - { scheme: "cah", code: "CAH15-03-01", label: "politics", basis: "inferred" }
  - { scheme: "hecos", code: "100091", label: "public services", basis: "inferred" }
edition: "April 2025 (first edition)"
published: 2025-04
status: current
supersedes: "none: the statement calls itself new (front matter) and first edition (back matter)"
heldText: { method: sha256-bytes, raw: 1d1e51d877ceed31d4f4079fecdf7394c6071e4fcaf3e0d781cc9f4fbe36c215, normalised: 513332e49494cb13da851aa31faa8e833faf0817a791d0b1984c4bd5de062d35 }
heldTextStan: { method: sha256-stan, raw: 1d1e51d877ceed31d4f4079fecdf7394c6071e4fcaf3e0d781cc9f4fbe36c215, normalised: 98d87cf4c171686a8280e66402aacd95febed3f986f668f119275279a2143b15 }
licence: "QAA copyright; held for study, private to the project, never published"
series: "QAA Subject Benchmark Statements, 2025 series with five cross-cutting themes (first edition, published 10 April 2025)"
awardsCovered: ["bachelor's with honours", "master's"]
levelsCovered: ["fheq:6", "fqheis:10", "fheq:7", "fqheis:11"]
nations: ["England", "Wales", "Scotland", "Northern Ireland"]
parts:
  S: full
  B: "partial: no glossary in the document (it points to QAA's Glossary); terms it defines in passing"
  C: "not-applicable: the document sets expectations, not a procedure"
pins: { structure: 0.13.0-draft, template: 0.8.0-draft, benchmarkTemplate: 0.6.0-draft, runFrame: 0.1.1-draft, runLayer: 0.7.0-draft, standards: none yet, terminology: none yet }
lifecycle: drafted
researchedBy: run frame 0.1.1-draft; standards run layer 0.7.0-draft; std, run 0128 (tools/bm_build.py)
passes:
  P1: "2026-10-03 18:24"
  P2: "skipped: read direct from the held text; inferred codes and rung links are for P3"
  P3: open
version: 0.1.2
---

<!-- from INGEST wpk-0016-ingest-pd-template-standards.md 0.8.0-draft and wpk-0016-ingest-pd-template-standards-benchmark.md 0.6.0-draft; built by tools/bm_build.py from run-src/ -->
# Subject Benchmark Statement: Public Policy and Public Administration (QAA, April 2025)

> Run 0128, P1 by std. The issuer's words are held in the source library, `wkspc2601-library/txt/qaa-2025-public-policy-public-administration-subject-benchmark-standard.norm.txt`; each S4 record carries its statement in full (`source`) for language analysis, with its span. Paraphrases and versions are ours. Private to the project, never published. In front matter `status` is the issuer's; ours is `lifecycle`. Doubts are in Part E.

## Part 0 Summary

### 0.1 Agent definition
<!-- label: editorial; status: drafted; basis: primary -->
QAA's UK reference point for what a graduate in Public Policy or Public Administration should know, understand and be able to do, at honours and at master's level. Reach for it when designing, approving, reviewing or describing a course in either subject, or one that teaches them inside economics, politics, social policy or management. Its honours standards come at two levels, threshold and excellent, with no typical level; its master's standards are one list. It is not a regulatory requirement, not a competence standard and not a classification scheme, which it leaves to Annex D.

### 0.2 Summary
<!-- label: both; status: drafted; basis: primary -->
A new statement, published by QAA on 10 April 2025, covering Public Policy and Public Administration as linked but distinct subjects: policy as the study of what shapes government decisions, administration as how policy is formed and carried out. It sets the purposes of the degrees, five cross-cutting themes (equity, diversity and inclusion; accessibility; education for sustainable development; employability, entrepreneurship and enterprise; generative AI), distinctive features of design, progression, flexibility, partnership and review, 40 typical subfields and the teaching, learning and assessment used, and standards in three lists: a threshold list (15 items) and an excellent list (16) for honours, and a master's list (17 items under a lead-in). It names the Chartered Management Institute and three public administration accreditors (ICAPA, EAPAA, NASPAA) as routes to accreditation, and points to Annex D for classification.

## Part S Standard

### S1 Identity
<!-- label: source; status: drafted; basis: primary -->
```yaml
issuer: The Quality Assurance Agency for Higher Education
title: "Subject Benchmark Statement Public Policy and Public Administration"
edition: "April 2025 (first edition)"
dates:
  published: 2025-04
  other: []
kind: subject-benchmark
jurisdiction: [UK]
authority: "reference: a sector reference point, not a regulatory requirement (D1, front matter); in England not a sector-recognised standard under the OfS framework; part of the quality arrangements in Scotland, Wales and Northern Ireland (D1, Relationship to legislation)"
licence: "QAA copyright; the document gives no re-use terms in its text (D1, front matter)"
copyrightNotice: { text: "© The Quality Assurance Agency for Higher Education 2025", locator: "D1, index" }
```

### S2 Purpose and scope
<!-- label: source; status: drafted; basis: primary -->
```yaml
governs: "what can be expected of a graduate in Public Policy and/or Public Administration, at honours and master's level, and the nature of degrees in the two subjects (D1, front matter; 1.1; 4.1)"
appliesTo:
  awards: ["bachelor's degrees with honours, including joint and combined honours (2.7, 2.8)", "master's degrees, including MPA, MPP, MSc and executive MA or MSc (1.4, 2.11, 4.7)", "relevant to foundation degrees, with no standards set at their level (1.4)"]
  levels: ["fheq:6", "fqheis:10", "fheq:7", "fqheis:11"]
  providers: ["UK higher education providers"]
whoMustUse: "none-stated; it is a reference point, not a requirement (D1, front matter)"
howUsed: ["design", "approval", "review", "other: external examining (front matter, 2.21); PSRBs (front matter); prospective students, employers and scholars (front matter)"]
doesNot: "it is not a national curriculum and does not prescribe teaching, learning or assessment; it carries no statutory or regulatory requirement (D1, front matter)"
beneficiary: the student
statedScope: "\"This Subject Benchmark Statement sets out the context and purposes of degrees in Public Policy and in Public Administration, which are linked and at the same time distinct areas of study.\" (D1, 1.1)"
statedSubjects:
  - { name: "Public Policy", locator: "(D1, title; 1.1)", kind: "subject", codes: [{ scheme: "hecos", code: "100647", label: "public policy" }] }
  - { name: "Public Administration", locator: "(D1, title; 1.1)", kind: "subject", codes: [{ scheme: "hecos", code: "100090", label: "public administration" }] }
  - { name: "Master of Public Administration (MPA)", locator: "(D1, 2.11)", kind: "programme title", codes: [{ scheme: "hecos", code: "100090", label: "public administration" }] }
  - { name: "Master of Public Policy (MPP)", locator: "(D1, 2.11)", kind: "programme title", codes: [{ scheme: "hecos", code: "100647", label: "public policy" }] }
  - { name: "Police Leadership and Management; Healthcare Management; Local Government Management", locator: "(D1, 1.4)", kind: "programme title", codes: [] }
  - { name: "economics, finance, politics, public ethics, political geography, planning, urban studies, social policy, sociology, management, law and business", locator: "(D1, 1.3)", kind: "subject", codes: [{ scheme: "hecos", code: "100491", label: "politics" }, { scheme: "hecos", code: "100502", label: "social policy" }] }
subjects: see front matter (subjectScope subjects)
```

### S3 Structure
<!-- label: both; status: drafted; basis: primary -->
```yaml
components:
  - { number: "1.1", order: 3, componentType: paragraph, parent: "section 1", heading: "Context and purposes of a Public Policy and Public Administration degree", gloss: "policy and administration as linked, distinct subjects" }
  - { number: "1.2", order: 4, componentType: paragraph, parent: "section 1", heading: "Context and purposes of a Public Policy and Public Administration degree", gloss: "what the courses investigate and develop" }
  - { number: "1.3", order: 5, componentType: paragraph, parent: "section 1", heading: "Context and purposes of a Public Policy and Public Administration degree", gloss: "taught across many host disciplines" }
  - { number: "1.4", order: 6, componentType: stem, parent: "section 1", heading: "Context and purposes of a Public Policy and Public Administration degree", gloss: "degree types the statement serves" }
  - { number: "1.5", order: 7, componentType: paragraph, parent: "section 1", heading: "Context and purposes of a Public Policy and Public Administration degree", gloss: "governmental decisions, resources and levels of enquiry" }
  - { number: "1.6", order: 8, componentType: paragraph, parent: "section 1", heading: "Context and purposes of a Public Policy and Public Administration degree", gloss: "the policy cycle and fairness at its core" }
  - { number: "1.7", order: 9, componentType: paragraph, parent: "section 1", heading: "Context and purposes of a Public Policy and Public Administration degree", gloss: "principles of good public decision-making" }
  - { number: "1.8", order: 10, componentType: paragraph, parent: "section 1", heading: "Context and purposes of a Public Policy and Public Administration degree", gloss: "interdisciplinarity, co-design and collaboration" }
  - { number: "1.9", order: 11, componentType: stem, parent: "section 1", heading: "Purposes and characteristics of a Public Policy and Public Administration degree", gloss: "seven purposes of the degree" }
  - { number: "1.10", order: 12, componentType: paragraph, parent: "section 1", heading: "Purposes and characteristics of a Public Policy and Public Administration degree", gloss: "skills for uncertain settings and many jobs" }
  - { number: "1.11", order: 13, componentType: paragraph, parent: "section 1", heading: "Purposes and characteristics of a Public Policy and Public Administration degree", gloss: "public sector scale and critical evaluation" }
  - { number: "1.12", order: 14, componentType: paragraph, parent: "section 1", heading: "Equity, diversity and inclusion", gloss: "EDI in delivery and curriculum (should)" }
  - { number: "1.13", order: 15, componentType: paragraph, parent: "section 1", heading: "Equity, diversity and inclusion", gloss: "curricula that champion EDI" }
  - { number: "1.14", order: 16, componentType: paragraph, parent: "section 1", heading: "Equity, diversity and inclusion", gloss: "EDI in academic and administrative practice (should)" }
  - { number: "1.15", order: 17, componentType: paragraph, parent: "section 1", heading: "Accessibility and the needs of disabled students", gloss: "accessibility in degree design" }
  - { number: "1.16", order: 18, componentType: paragraph, parent: "section 1", heading: "Accessibility and the needs of disabled students", gloss: "reasonable adjustments and equal access" }
  - { number: "1.17", order: 19, componentType: paragraph, parent: "section 1", heading: "Accessibility and the needs of disabled students", gloss: "graduates' part in accessible services" }
  - { number: "1.18", order: 20, componentType: paragraph, parent: "section 1", heading: "Education for sustainable development", gloss: "the subject and sustainable development" }
  - { number: "1.19", order: 21, componentType: paragraph, parent: "section 1", heading: "Education for sustainable development", gloss: "pedagogies for ESD" }
  - { number: "1.20", order: 22, componentType: paragraph, parent: "section 1", heading: "Employability, entrepreneurship and enterprise education", gloss: "responsibilities of public roles; enterprise education" }
  - { number: "1.21", order: 23, componentType: stem, parent: "section 1", heading: "Employability, entrepreneurship and enterprise education", gloss: "what enterprise education can do (nine claims)" }
  - { number: "1.22", order: 24, componentType: paragraph, parent: "section 1", heading: "Employability, entrepreneurship and enterprise education", gloss: "links to enterprise; experienced students (must)" }
  - { number: "1.23", order: 25, componentType: paragraph, parent: "section 1", heading: "Employability, entrepreneurship and enterprise education", gloss: "graduates recognise and convey enterprise skills" }
  - { number: "1.24", order: 26, componentType: paragraph, parent: "section 1", heading: "Employability, entrepreneurship and enterprise education", gloss: "work with employers and stakeholders" }
  - { number: "1.25", order: 27, componentType: paragraph, parent: "section 1", heading: "Employability, entrepreneurship and enterprise education", gloss: "professional accreditation routes" }
  - { number: "1.22-2", order: 28, componentType: paragraph, parent: "section 1", heading: "Employability, entrepreneurship and enterprise education", gloss: "cross-sector skills and changing employer needs (second 1.22)" }
  - { number: "1.26", order: 29, componentType: paragraph, parent: "section 1", heading: "Generative artificial intelligence", gloss: "responding to generative AI (must)" }
  - { number: "1.27", order: 30, componentType: paragraph, parent: "section 1", heading: "Generative artificial intelligence", gloss: "responsible GenAI education" }
  - { number: "1.28", order: 31, componentType: paragraph, parent: "section 1", heading: "Generative artificial intelligence", gloss: "ethical use of technology" }
  - { number: "2.1", order: 33, componentType: paragraph, parent: "section 2", heading: "Design", gloss: "multidisciplinary study and career readiness" }
  - { number: "2.2", order: 34, componentType: paragraph, parent: "section 2", heading: "Design", gloss: "integrating policy with administration" }
  - { number: "2.3", order: 35, componentType: paragraph, parent: "section 2", heading: "Design", gloss: "skills and themes courses promote" }
  - { number: "2.4", order: 36, componentType: paragraph, parent: "section 2", heading: "Design", gloss: "multilevel governance and public value" }
  - { number: "2.5", order: 37, componentType: paragraph, parent: "section 2", heading: "Design", gloss: "practitioner teaching" }
  - { number: "2.6", order: 38, componentType: paragraph, parent: "section 2", heading: "Progression", gloss: "undergraduate provision across the UK" }
  - { number: "2.7", order: 39, componentType: paragraph, parent: "section 2", heading: "Progression", gloss: "progression through an honours degree" }
  - { number: "2.8", order: 40, componentType: paragraph, parent: "section 2", heading: "Progression", gloss: "joint and combined degrees" }
  - { number: "2.9", order: 41, componentType: paragraph, parent: "section 2", heading: "Progression", gloss: "exit awards" }
  - { number: "2.10", order: 42, componentType: paragraph, parent: "section 2", heading: "Progression", gloss: "degree length across the nations" }
  - { number: "2.11", order: 43, componentType: paragraph, parent: "section 2", heading: "Progression", gloss: "master's provision and cohorts" }
  - { number: "2.12", order: 44, componentType: paragraph, parent: "section 2", heading: "Progression", gloss: "integrated master's" }
  - { number: "2.13", order: 45, componentType: paragraph, parent: "section 2", heading: "Progression", gloss: "postgraduate entry" }
  - { number: "2.14", order: 46, componentType: paragraph, parent: "section 2", heading: "Progression", gloss: "graduates as policymakers and leaders" }
  - { number: "2.15", order: 47, componentType: paragraph, parent: "section 2", heading: "Flexibility", gloss: "flexible learning for working students" }
  - { number: "2.16", order: 48, componentType: paragraph, parent: "section 2", heading: "Flexibility", gloss: "forms of flexible learning; CPD accreditation" }
  - { number: "2.17", order: 49, componentType: stem, parent: "section 2", heading: "Partnership", gloss: "what partnerships create" }
  - { number: "2.18", order: 50, componentType: paragraph, parent: "section 2", heading: "Partnership", gloss: "partners and cross-sector collaboration" }
  - { number: "2.19", order: 51, componentType: paragraph, parent: "section 2", heading: "Monitoring and review", gloss: "monitoring, review and the student voice" }
  - { number: "2.20", order: 52, componentType: paragraph, parent: "section 2", heading: "Monitoring and review", gloss: "external reviewers" }
  - { number: "2.21", order: 53, componentType: paragraph, parent: "section 2", heading: "Monitoring and review", gloss: "external examiners" }
  - { number: "2.22", order: 54, componentType: paragraph, parent: "section 2", heading: "Monitoring and review", gloss: "advisory boards" }
  - { number: "2.23", order: 55, componentType: paragraph, parent: "section 2", heading: "Monitoring and review", gloss: "integrating accreditation requirements" }
  - { number: "3.1", order: 57, componentType: paragraph, parent: "section 3", heading: "Content, structure and delivery", gloss: "purpose of the section" }
  - { number: "3.2", order: 58, componentType: practice, parent: "section 3", heading: "Content, structure and delivery", gloss: "practice-based learning" }
  - { number: "3.3", order: 59, componentType: area, parent: "section 3", heading: "Content", gloss: "governance content and 40 typical subfields" }
  - { number: "3.4", order: 60, componentType: area, parent: "section 3", heading: "Content", gloss: "policy and administration emphases compared" }
  - { number: "3.5", order: 61, componentType: area, parent: "section 3", heading: "Content", gloss: "transferable capacities; vocational and theoretical range" }
  - { number: "3.6", order: 62, componentType: practice, parent: "section 3", heading: "Teaching and learning", gloss: "teaching environments and digital inclusion" }
  - { number: "3.7", order: 63, componentType: practice, parent: "section 3", heading: "Teaching and learning", gloss: "learning methods (eight kinds)" }
  - { number: "3.8", order: 64, componentType: practice, parent: "section 3", heading: "Teaching and learning", gloss: "learning environments, resources and digital literacy" }
  - { number: "3.9", order: 65, componentType: practice, parent: "section 3", heading: "Teaching and learning", gloss: "research-led teaching and practitioner input" }
  - { number: "3.10", order: 66, componentType: practice, parent: "section 3", heading: "Assessment and feedback", gloss: "assessment strategy and its alignment" }
  - { number: "3.11", order: 67, componentType: practice, parent: "section 3", heading: "Assessment and feedback", gloss: "plural assessment and adjustments" }
  - { number: "3.12", order: 68, componentType: practice, parent: "section 3", heading: "Assessment and feedback", gloss: "five kinds of assessment" }
  - { number: "3.13", order: 69, componentType: practice, parent: "section 3", heading: "Assessment and feedback", gloss: "feedback" }
  - { number: "4.1", order: 71, componentType: paragraph, parent: "section 4", heading: "Introduction", gloss: "what the standards set out" }
  - { number: "4.2", order: 72, componentType: paragraph, parent: "section 4", heading: "Introduction", gloss: "performance above threshold; Annex D" }
  - { number: "4.3", order: 73, componentType: paragraph, parent: "section 4", heading: "Introduction", gloss: "threshold standards are not competence standards" }
  - { number: "4.4", order: 74, componentType: paragraph, parent: "section 4", heading: "Introduction", gloss: "scope and use of the standards" }
  - { number: "4.5", order: 75, componentType: stem, parent: "section 4", heading: "Threshold level", gloss: "threshold list for honours (15 items)" }
  - { number: "4.6", order: 76, componentType: stem, parent: "section 4", heading: "Excellent level", gloss: "excellent list for honours (16 items)" }
  - { number: "4.7", order: 77, componentType: stem, parent: "section 4", heading: "Master's", gloss: "master's lead-in and list (17 items)" }
  - { number: "1", componentType: section, parent: none, heading: "Context and purposes of a Public Policy and Public Administration degree", gloss: "section 1" }
  - { number: "2", componentType: section, parent: none, heading: "Distinctive features of Public Policy and Public Administration degrees", gloss: "section 2" }
  - { number: "3", componentType: section, parent: none, heading: "Content, structure and delivery", gloss: "section 3" }
  - { number: "4", componentType: section, parent: none, heading: "Benchmark standards", gloss: "section 4" }
excluded:
  - { number: "none", heading: "About this Statement; How can I use this document?; Relationship to legislation; Additional sector reference points", kind: "other: front matter, read for S1, S2 and SB6" }
  - { number: "none", heading: "section heading lines 1 to 4", kind: "other: headings, recorded in SECTIONS" }
  - { number: "5", heading: "List of references and further resources", kind: "other: back matter, read for SB6 shared documents" }
  - { number: "6", heading: "Membership of the Advisory Group", kind: "other: back matter, read for S8 (first edition, 10 April 2025)" }
```

### S4 Statements
<!-- label: both; status: drafted; basis: primary. Only standards (D-std-0002 (a)): 72 records. `source` is the issuer's statement exactly as its span holds it (D-std-0014). -->
```yaml
- id: qaa/public-policy-and-public-administration-2025/1.10
  locator: { number: "1.10", headingPath: ["Context and purposes of a Public Policy and Public Administration degree", "Purposes and characteristics of a Public Policy and Public Administration degree"] }
  span: { start: 15157, end: 15815 }
  source: "1.10 The study of Public Policy and/or Public Administration is concerned with providing students with skills, knowledge and capabilities that enable them to work in democratic or non-democratic environments characterised by uncertainty and challenge. Courses teach students to solve problems and identify solutions through strategic thinking, thereby equipping them with an awareness of how to hold governments and public service departments to account. While not every graduate will subsequently engage in a Public Policy and/or Public Administration focused career, the skills and attributes they acquire will prepare them for a wide range of occupations."
  stem: none
  statementType: expectation
  rung: none
  force: will
  level: none
  appliesTo: "graduates of the subject"
  addressee: learner
  verbs: ["prepare", "acquire"]
  about: "skills that prepare graduates for many occupations"
  themes: [none]
  domain: none
  award: ["none"]
  gradeOf: none
  paraphrase: "The subject gives students skills, knowledge and capabilities for work in democratic or non-democratic settings marked by uncertainty; courses teach strategic problem-solving and how to hold governments to account, and the skills graduates gain will ready them for many occupations, not only careers in the field."
  quote: full   # the issuer's statement is in `source` (D-std-0014)
  audience: both
  subjects: inherited
- id: qaa/public-policy-and-public-administration-2025/1.11
  locator: { number: "1.11", headingPath: ["Context and purposes of a Public Policy and Public Administration degree", "Purposes and characteristics of a Public Policy and Public Administration degree"] }
  span: { start: 15816, end: 16339 }
  source: "1.11 Governmental and public sector jobs make up approximately 20% of the contemporary economy in the regions and nations of the UK. Furthermore, public service delivery increasingly extends to providers in the non-profit and private sectors. Investment in the training and development of staff in the public sector is therefore crucial. Degrees in Public Policy and/or Public Administration will encourage students to critically evaluate policy and consider the overall effectiveness and productivity of the public sector."
  stem: none
  statementType: expectation
  rung: none
  force: will
  level: none
  appliesTo: "Public Policy and Public Administration courses and their students"
  addressee: both
  verbs: ["encourage", "evaluate", "consider"]
  about: "critical evaluation of policy and public sector performance"
  themes: [none]
  domain: understanding
  award: ["none"]
  gradeOf: none
  paraphrase: "With public sector jobs making up about a fifth of the UK economy and delivery spreading to non-profit and private bodies, investment in public staff matters; degrees will encourage students to evaluate policy critically and to weigh how effective and productive the public sector is."
  quote: full   # the issuer's statement is in `source` (D-std-0014)
  audience: both
  subjects: inherited
- id: qaa/public-policy-and-public-administration-2025/1.12
  locator: { number: "1.12", headingPath: ["Context and purposes of a Public Policy and Public Administration degree", "Equity, diversity and inclusion"] }
  span: { start: 16372, end: 17639 }
  source: "1.12 Degrees in Public Policy and/or Public Administration have a significant role to play in the organisation and governance of socially just societies and the delivery of fair policies, services and public support. They are also responsible for the development and maintenance of institutions and structures that create conditions for an equal, equitable and inclusive society. Accordingly, the creation and implementation of policies and public administrations which promote equal opportunities and fair outcomes, and which serve a population regardless of its members' backgrounds, is of paramount importance. All of these activities should recognise and be guided by Equity Diversity and Inclusion (EDI) principles. Therefore, degrees in Public Policy and/or Public Administration should observe, integrate and promote EDI in both delivery and curriculum. Equality, equity, diversity and inclusion should permeate knowledge production and pedagogies, curricular and assessment activities, and the creation of inclusive subject learning communities in which all staff and learners are welcome and feel a sense of belonging. Recognising the complexities involved in this task, QAA offers a useful resource on Creating Inclusive Subject Communities: New QAA Advice."
  stem: none
  statementType: requirement
  rung: none
  force: should
  level: none
  appliesTo: "Public Policy and Public Administration courses"
  addressee: provider
  verbs: ["recognise", "guided", "observe", "integrate", "promote"]
  about: "EDI in delivery and curriculum"
  themes: [theme:edi]
  domain: none
  award: ["none"]
  gradeOf: none
  paraphrase: "Because the subject serves fair policy and just institutions, its activities should be guided by EDI principles: degrees should observe, build in and advance EDI in teaching and curriculum, and equality, equity, diversity and inclusion should run through knowledge, pedagogy, curriculum, assessment and inclusive learning communities."
  quote: full   # the issuer's statement is in `source` (D-std-0014)
  audience: practitioner
  subjects: inherited
- id: qaa/public-policy-and-public-administration-2025/1.14
  locator: { number: "1.14", headingPath: ["Context and purposes of a Public Policy and Public Administration degree", "Equity, diversity and inclusion"] }
  span: { start: 18293, end: 18798 }
  source: "1.14 EDI principles should be at the forefront of academic, pedagogical and administrative practices, processes and behaviours in supporting teaching and learning practice in Public Policy and/or Public Administration degrees. This includes, but is not limited to, the use of inclusive language, pedagogies and assessment frameworks that recognise power asymmetries, facilitate the inclusion of diverse views and characteristics, promote ideas of social justice and foster inclusive learning environments."
  stem: none
  statementType: requirement
  rung: none
  force: should
  level: none
  appliesTo: "Public Policy and Public Administration courses"
  addressee: provider
  verbs: ["recognise", "facilitate", "promote", "foster"]
  about: "EDI in academic and administrative practice"
  themes: [theme:edi]
  domain: none
  award: ["none"]
  gradeOf: none
  paraphrase: "EDI should lead academic, teaching and administrative practice in the subject, through inclusive language and through teaching and assessment that acknowledge unequal power, bring in diverse views, advance social justice and create inclusive places to learn."
  quote: full   # the issuer's statement is in `source` (D-std-0014)
  audience: practitioner
  subjects: inherited
- id: qaa/public-policy-and-public-administration-2025/1.17
  locator: { number: "1.17", headingPath: ["Context and purposes of a Public Policy and Public Administration degree", "Accessibility and the needs of disabled students"] }
  span: { start: 20280, end: 20676 }
  source: "1.17 Public Policy and/or Public Administration graduates will play a central role in shaping policies and services in critical areas such as health, technology, innovation, finance, and crisis management. This goes beyond the realm of legal compliance, into building fully accessible and inclusive provision that is transparent, effective and enables the participation of all members of society."
  stem: none
  statementType: expectation
  rung: none
  force: will
  level: none
  appliesTo: "graduates of the subject"
  addressee: learner
  verbs: ["play", "shaping"]
  about: "graduates' role in accessible, inclusive services"
  themes: [theme:accessibility]
  domain: none
  award: ["none"]
  gradeOf: none
  paraphrase: "Graduates will play a central part in shaping policy and services in fields from health and technology to innovation, finance and crises, going beyond legal compliance to provision that is accessible, inclusive, transparent and effective and lets everyone take part."
  quote: full   # the issuer's statement is in `source` (D-std-0014)
  audience: both
  subjects: inherited
- id: qaa/public-policy-and-public-administration-2025/1.22
  locator: { number: "1.22", headingPath: ["Context and purposes of a Public Policy and Public Administration degree", "Employability, entrepreneurship and enterprise education"] }
  span: { start: 24962, end: 25427 }
  source: "1.22 Public Policy and especially Public Administration degrees for pre- and post- experience students are strongly related to practice, and therefore must provide clear links between degree content and enterprise and entrepreneurship. While degrees will have the capacity to develop career-ready students, they must also equip sector-experienced students with the knowledge, behaviours and skills that will enable them to develop and progress within the workplace."
  stem: none
  statementType: requirement
  rung: none
  force: must
  level: none
  appliesTo: "Public Policy and especially Public Administration degrees, pre- and post-experience"
  addressee: provider
  verbs: ["provide", "equip", "develop", "progress"]
  about: "links to enterprise and equipping experienced students"
  themes: [theme:enterprise]
  domain: none
  award: ["none"]
  gradeOf: none
  paraphrase: "Because the subject is closely tied to practice, its degrees for students before and after work experience must link content clearly to enterprise and entrepreneurship, and must give students already in the sector the knowledge, behaviours and skills to grow and advance at work."
  quote: full   # the issuer's statement is in `source` (D-std-0014)
  audience: practitioner
  subjects: inherited
- id: qaa/public-policy-and-public-administration-2025/1.23
  locator: { number: "1.23", headingPath: ["Context and purposes of a Public Policy and Public Administration degree", "Employability, entrepreneurship and enterprise education"] }
  span: { start: 25428, end: 25879 }
  source: "1.23 Public Policy and Public Administration graduates understand the value of the EEE skills that they have developed and/or advanced throughout their study. Courses can instil students with an understanding and appreciation of these skills, as well as their applicability and transferability; students are able to recognise, reflect on and develop them, as well as communicate them to potential and current employers and other relevant stakeholders."
  stem: none
  statementType: outcome
  rung: none
  force: will
  level: fheq:6
  appliesTo: "graduates of the subject"
  addressee: learner
  verbs: ["understand", "recognise", "reflect", "develop", "communicate"]
  about: "recognising and communicating enterprise and employability skills"
  themes: [theme:enterprise]
  domain: generic-skill
  award: ["bachelor's with honours"]
  gradeOf: none
  paraphrase: "Graduates understand the worth of the enterprise and employability skills they built during study; courses can deepen that understanding, and students will be able to recognise these skills, reflect on them, develop them and explain them to employers and other stakeholders."
  quote: full   # the issuer's statement is in `source` (D-std-0014)
  audience: both
  subjects: inherited
- id: qaa/public-policy-and-public-administration-2025/1.26
  locator: { number: "1.26", headingPath: ["Context and purposes of a Public Policy and Public Administration degree", "Generative artificial intelligence"] }
  span: { start: 27344, end: 28261 }
  source: "1.26 Public Policy and/or Public Administration degrees promote employability in a labour market that is becoming increasingly shaped by artificial intelligence (AI). They also prepare and equip students for work environments that require professionals to work alongside smart machines (Aoun, 2017). To ensure students can complete their studies responsibly and with integrity, and be equipped to enter a world increasingly impacted by generative AI ( GenAI), Public Policy and/or Public Administration degrees must recognise and respond to employer and workplace needs, and evolving teaching, assessment and feedback practices. When considering the relevance of GenAI in Public Policy and Public Administration degrees, course developers look beyond assessment security and consider how degrees can incorporate GenAI into wider learning and teaching practices and student activities, including authentic assessments."
  stem: none
  statementType: requirement
  rung: none
  force: must
  level: none
  appliesTo: "Public Policy and Public Administration courses"
  addressee: provider
  verbs: ["recognise", "respond"]
  about: "responding to generative AI in teaching and assessment"
  themes: [theme:generative-ai]
  domain: none
  award: ["none"]
  gradeOf: none
  paraphrase: "As AI reshapes the labour market and work alongside smart machines, degrees in the subject must recognise and respond to the needs of employers and workplaces and to changing teaching, assessment and feedback, so that students study responsibly and with integrity; course developers look past assessment security to bring GenAI into wider learning and authentic assessment."
  quote: full   # the issuer's statement is in `source` (D-std-0014)
  audience: practitioner
  subjects: inherited
- id: qaa/public-policy-and-public-administration-2025/2.4
  locator: { number: "2.4", headingPath: ["Distinctive features of Public Policy and Public Administration degrees", "Design"] }
  span: { start: 30509, end: 30977 }
  source: "2.4 Courses also examine multilevel governance, and the interplay between structure, systems and agency in the public sector, for example, the role of the state in the policy process and the experience of frontline workers and workforce challenges. They will also emphasise public and social value as characteristic of public policy and public administration. Themes such as public service motivation and ethos are also common features associated with the disciplines."
  stem: none
  statementType: expectation
  rung: none
  force: will
  level: none
  appliesTo: "Public Policy and Public Administration courses and their students"
  addressee: both
  verbs: ["examine", "emphasise"]
  about: "public and social value in courses"
  themes: [none]
  domain: none
  award: ["none"]
  gradeOf: none
  paraphrase: "Courses also study multilevel governance and how structure, systems and agency interact in the public sector, such as the state's part in policy and the experience of frontline staff; they will also stress public and social value as typical of the field, with public service motivation and ethos as common themes."
  quote: full   # the issuer's statement is in `source` (D-std-0014)
  audience: both
  subjects: inherited
- id: qaa/public-policy-and-public-administration-2025/2.7
  locator: { number: "2.7", headingPath: ["Distinctive features of Public Policy and Public Administration degrees", "Progression"] }
  span: { start: 31887, end: 32984 }
  source: "2.7 Over the duration of a degree with honours (FHEQ Level 6; FQHEIS Level 10), a student engaging with Public Policy and/or Public Administration will progress from one level of study to the next, in line with the regulations and processes for each institution. However, it is expected that each level would see the attainment of knowledge, expertise and\n\n10\nexperience that build towards the final achievement of meeting the threshold-level, subject- specific and generic skills listed in this Statement. This will usually include successful completion and the award of credit for the full range of learning and assessment, including any practical components. Upon graduation from an undergraduate degree, it would be expected that a student who had achieved a second-class degree or higher would be capable of, and equipped for, undertaking postgraduate study in Public Policy and/or Public Administration or a related discipline. Entry requirements to postgraduate degrees are, however, determined by individual providers and may require specified levels of achievement at undergraduate level."
  stem: none
  statementType: expectation
  rung: none
  force: will
  level: fheq:6
  appliesTo: "Public Policy and Public Administration courses and their students"
  addressee: both
  verbs: ["progress", "build", "include"]
  about: "progression through the honours levels towards the threshold"
  themes: [none]
  domain: none
  award: ["bachelor's with honours"]
  gradeOf: none
  paraphrase: "Over an honours degree (FHEQ level 6; FQHEIS level 10) students will progress level by level under each institution's rules, each level adding knowledge, expertise and experience towards the threshold subject and generic skills; this will usually mean completing all learning and assessment for credit, practical parts included, and a graduate with a second-class degree or better would be expected to be ready for postgraduate study, though providers set entry rules."
  quote: full   # the issuer's statement is in `source` (D-std-0014)
  audience: both
  subjects: inherited
- id: qaa/public-policy-and-public-administration-2025/2.8
  locator: { number: "2.8", headingPath: ["Distinctive features of Public Policy and Public Administration degrees", "Progression"] }
  span: { start: 32985, end: 33430 }
  source: "2.8 Undergraduates studying Public Policy and/or Public Administration as part of a combined or joint degree with other subjects will achieve core elements of the specific and generic skills outlined in this Statement, and will add others according to the topics covered in the other subject(s) of their degree. Additionally, they may explore the overlap between different disciplines, creating further opportunities for interdisciplinary study."
  stem: none
  statementType: outcome
  rung: none
  force: will
  level: fheq:6
  appliesTo: "joint or combined honours students"
  addressee: learner
  verbs: ["achieve", "add"]
  about: "joint and combined degrees"
  themes: [none]
  domain: none
  award: ["bachelor's with honours"]
  gradeOf: none
  paraphrase: "Undergraduates taking the subject in a joint or combined degree will reach the core of its specific and generic skills and add others from their other subject, and may explore where disciplines overlap."
  quote: full   # the issuer's statement is in `source` (D-std-0014)
  audience: both
  subjects: inherited
- id: qaa/public-policy-and-public-administration-2025/2.14
  locator: { number: "2.14", headingPath: ["Distinctive features of Public Policy and Public Administration degrees", "Progression"] }
  span: { start: 35434, end: 36084 }
  source: "2.14 It is anticipated that graduates will have the requisite skills to become effective policymakers, managers, leaders and change agents in the public, private and non-profit sectors. An important outcome for the discipline is to acknowledge public service and Public Administration as distinct professions, where professionals will have acquired the general skills to move between Public Administration and Public Policy domains. Students will be helped to understand that public services are delivered through multiagency models, including public, private and non-profit organisations and that collaborative working across sectors is commonplace."
  stem: none
  statementType: expectation
  rung: none
  force: will
  level: none
  appliesTo: "graduates of the subject"
  addressee: learner
  verbs: ["have", "become", "acquired", "helped", "understand"]
  about: "skills for policy, management and leadership across sectors"
  themes: [none]
  domain: understanding
  award: ["none"]
  gradeOf: none
  paraphrase: "Graduates are expected to be equipped to work well as policymakers, managers, leaders and agents of change across public, private and non-profit sectors; public service and public administration are distinct professions whose members can move between policy and administration, and students will be helped to see that services are delivered through multi-agency models where cross-sector working is normal."
  quote: full   # the issuer's statement is in `source` (D-std-0014)
  audience: both
  subjects: inherited
- id: qaa/public-policy-and-public-administration-2025/2.19
  locator: { number: "2.19", headingPath: ["Distinctive features of Public Policy and Public Administration degrees", "Monitoring and review"] }
  span: { start: 37754, end: 38505 }
  source: "2.19 Degree-awarding bodies and their collaborative partnerships routinely collect and analyse information and undertake periodic degree review, according to their own needs. Considering the student voice will form part of this. Degree-awarding bodies draw on a range of external reference points, including this Statement, to ensure that provision aligns with sector norms. Monitoring and evaluation constitute periodic assessment of a degree, conducted internally and/or by external independent evaluators. Evaluation uses information from both current and historic monitoring to develop an understanding of student achievement or inform future course planning. It can also include regular monitoring and review of EDI within the learning community."
  stem: none
  statementType: expectation
  rung: none
  force: will
  level: none
  appliesTo: "degree-awarding bodies and their collaborative partners"
  addressee: provider
  verbs: ["form"]
  about: "the student voice in monitoring and review"
  themes: [none]
  domain: none
  award: ["none"]
  gradeOf: none
  paraphrase: "Degree-awarding bodies and their partners routinely gather and analyse information and review degrees periodically, and the student voice will form part of this; they use external reference points, this statement among them, and evaluation can include regular review of EDI in the learning community."
  quote: full   # the issuer's statement is in `source` (D-std-0014)
  audience: practitioner
  subjects: inherited
- id: qaa/public-policy-and-public-administration-2025/2.20
  locator: { number: "2.20", headingPath: ["Distinctive features of Public Policy and Public Administration degrees", "Monitoring and review"] }
  span: { start: 38506, end: 38818 }
  source: "2.20 Externality is an essential component of the quality assurance system in the UK. Higher education providers will use external reviewers as part of periodic review to gain an external perspective on any proposed changes and ensure threshold standards are achieved, and content is appropriate for the subject."
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
  paraphrase: "Externality is a core part of UK quality assurance: providers will use external reviewers in periodic review to bring an outside view of proposed changes, check that threshold standards are met and confirm that content suits the subject."
  quote: full   # the issuer's statement is in `source` (D-std-0014)
  audience: practitioner
  subjects: inherited
- id: qaa/public-policy-and-public-administration-2025/2.23
  locator: { number: "2.23", headingPath: ["Distinctive features of Public Policy and Public Administration degrees", "Monitoring and review"] }
  span: { start: 40289, end: 40474 }
  source: "2.23 Courses with professional and or vocational outcomes requiring evaluation from professional and accrediting bodies will need to integrate these requirements into degree management."
  stem: none
  statementType: expectation
  rung: none
  force: will
  level: none
  appliesTo: "courses with professional or vocational outcomes evaluated by accrediting bodies"
  addressee: provider
  verbs: ["integrate"]
  about: "integrating accreditation requirements"
  themes: [none]
  domain: none
  award: ["none"]
  gradeOf: none
  paraphrase: "Courses whose professional or vocational outcomes are evaluated by professional and accrediting bodies will need to build those requirements into how the degree is managed."
  quote: full   # the issuer's statement is in `source` (D-std-0014)
  audience: practitioner
  subjects: inherited
- id: qaa/public-policy-and-public-administration-2025/3.2
  locator: { number: "3.2", headingPath: ["Content, structure and delivery", "Content, structure and delivery"] }
  span: { start: 40802, end: 41169 }
  source: "3.2 Students will typically learn about the evolution of policy making, public administration and decision making by exposure to practice-based learning. Here they will work on real- world problems and develop critical skills, drawn from pedagogies such as action learning and reflection, and through focused placements in public agencies and non-governmental bodies."
  stem: none
  statementType: expectation
  rung: none
  force: will
  level: none
  appliesTo: "Public Policy and Public Administration courses and their students"
  addressee: both
  verbs: ["learn", "work", "develop"]
  about: "practice-based learning"
  themes: [none]
  domain: none
  award: ["none"]
  gradeOf: none
  paraphrase: "Students will usually learn how policy making, public administration and decision making have developed through practice-based learning, working on real problems and building critical skills through approaches such as action learning and reflection and through placements in public and non-governmental bodies."
  quote: full   # the issuer's statement is in `source` (D-std-0014)
  audience: both
  subjects: inherited
- id: qaa/public-policy-and-public-administration-2025/3.3
  locator: { number: "3.3", headingPath: ["Content, structure and delivery", "Content"] }
  span: { start: 41178, end: 42634 }
  source: "3.3 Public Policy and/or Public Administration degrees introduce students to key ideas about the design and operation of governments, as well as public and voluntary sectors. No specific policy sectors or institutions are considered essential. Rather, it is expected that the study of Public Policy and Public Administration will include detailed engagement with substantive questions of governance and policy to develop knowledge and apply governance-related theories, concepts, values and principles in a range of contexts. This includes (but is not limited to), individual, local, regional, national and global contexts, as well as institutional, normative, social, political, economic, cultural, historical, ethical, philosophical, technological and ecological contexts. Both areas have their basis in legal, economic and political studies. More recently, their study has been shaped by broader social sciences, notably sociology and organisation and management studies. Despite the variation this generates, students taking Public Policy and/or Public Administration degrees all study the public sector conceptually and empirically, and across all levels of government in democratic and non-democratic countries. The scope and breadth of each degree varies, but students typically demonstrate a knowledge and understanding of a number of the following subfields which reflect both the foundational concepts and themes that address contemporary issues:"
  stem: none
  statementType: expectation
  rung: none
  force: will
  level: none
  appliesTo: "Public Policy and Public Administration courses and their students"
  addressee: both
  verbs: ["introduce", "include", "develop", "apply", "study", "demonstrate"]
  about: "engagement with governance and policy across contexts"
  themes: [none]
  domain: none
  award: ["none"]
  gradeOf: none
  paraphrase: "Degrees introduce the design and running of governments and of the public and voluntary sectors; no sector or institution is essential, but study will include close engagement with questions of governance and policy, applying theories, concepts, values and principles across many contexts; all students study the public sector conceptually and empirically at every tier of government, and typically know a number of the listed subfields."
  quote: full   # the issuer's statement is in `source` (D-std-0014)
  audience: both
  subjects: inherited
- id: qaa/public-policy-and-public-administration-2025/3.6
  locator: { number: "3.6", headingPath: ["Content, structure and delivery", "Teaching and learning"] }
  span: { start: 45043, end: 46210 }
  source: "3.6 The learning and teaching environments developed by different providers will reflect their respective approaches to Public Policy and/or Public Administration, and that may emphasise different types of ethos, context, skill sets and analytical approaches. Qualifications may be conventionally academic, or combine theory with practice-based elements. Learning and teaching methods are designed to best fit the subject matter at hand and the learning outcomes set, considering the needs of different learners. Learning and teaching methods embrace principles of sustainability, inclusion and diversity, accessibility, and enterprise and entrepreneurship (see section 1). They take account of the diverse learning and teaching cultures that students may have experienced and provide opportunities for students to understand and appreciate the global context in which they will be operating. Learning approaches may include a range of modes, including, but not limited to, in-person, digital, blended, block release, hybrid, experiential, full-time, part-time, synchronous and asynchronous. As far as possible, providers will ensure digital inclusivity for students."
  stem: none
  statementType: expectation
  rung: none
  force: will
  level: none
  appliesTo: "Public Policy and Public Administration courses"
  addressee: provider
  verbs: ["ensure", "reflect"]
  about: "learning environments and digital inclusivity"
  themes: [none]
  domain: none
  award: ["none"]
  gradeOf: none
  paraphrase: "Each provider's learning and teaching will reflect its own approach to the subject; methods fit the subject matter, the outcomes and learners' needs, embrace sustainability, inclusion, diversity, accessibility and enterprise, recognise students' prior learning cultures and the global context, and run across many modes; and providers will make digital learning inclusive wherever they can."
  quote: full   # the issuer's statement is in `source` (D-std-0014)
  audience: practitioner
  subjects: inherited
- id: qaa/public-policy-and-public-administration-2025/3.7
  locator: { number: "3.7", headingPath: ["Content, structure and delivery", "Teaching and learning"] }
  span: { start: 46211, end: 46653 }
  source: "3.7 Public Policy and/or Public Administration students will experience a range of learning environments, methods and activities that combine to develop ability to advance their cognitive and life skills, their knowledge base and to identify enterprising and entrepreneurial solutions to social challenges. Independent of mode of delivery, learning in Public Policy and/or Public Administration degrees typically includes some combination of:"
  stem: none
  statementType: expectation
  rung: none
  force: will
  level: none
  appliesTo: "Public Policy and Public Administration courses and their students"
  addressee: both
  verbs: ["experience", "combine", "develop", "advance", "identify"]
  about: "a range of learning environments and methods"
  themes: [none]
  domain: none
  award: ["none"]
  gradeOf: none
  paraphrase: "Students will meet a mix of learning settings, methods and activities that together build cognitive and life skills and knowledge and help them find enterprising answers to social challenges; whatever the mode, learning typically combines several of the listed methods."
  quote: full   # the issuer's statement is in `source` (D-std-0014)
  audience: both
  subjects: inherited
- id: qaa/public-policy-and-public-administration-2025/3.10
  locator: { number: "3.10", headingPath: ["Content, structure and delivery", "Assessment and feedback"] }
  span: { start: 48859, end: 49585 }
  source: "3.10 Assessment and feedback help students to deeply engage with Public Policy and/or Public Administration and showcase their understanding, analytical ability, insights and skills. A course's assessment strategy will reflect the knowledge, skills and understanding developed within its curriculum and align with its preferred methods of learning and teaching. Assessment as, and for, learning (as opposed to only assessment of learning) is promoted and developed. Assessment is linked to the specific learning outcomes of degrees and enables students to demonstrate progressive levels of attainment. It also enables the development of specific skills related to employability, professional practice and personal development."
  stem: none
  statementType: expectation
  rung: none
  force: will
  level: none
  appliesTo: "Public Policy and Public Administration courses"
  addressee: provider
  verbs: ["reflect", "align", "promoted", "linked", "enables"]
  about: "an assessment strategy aligned with curriculum and outcomes"
  themes: [none]
  domain: none
  award: ["none"]
  gradeOf: none
  paraphrase: "Assessment and feedback help students engage deeply and show their understanding, analysis, insight and skills; a course's assessment strategy will mirror the knowledge, skills and understanding in its curriculum and fit its teaching methods, with assessment for and as learning, tied to learning outcomes, showing rising attainment and building employability and professional skills."
  quote: full   # the issuer's statement is in `source` (D-std-0014)
  audience: practitioner
  subjects: inherited
- id: qaa/public-policy-and-public-administration-2025/3.13
  locator: { number: "3.13", headingPath: ["Content, structure and delivery", "Assessment and feedback"] }
  span: { start: 51567, end: 52164 }
  source: "3.13 Feedback is an essential part of the learning process and is designed to enable students to understand their progress and to further improve. Feedback will be constructive, consistent and specific. It will be given to students throughout their studies on both formative and summative work, in ways that allow them to feed forward to their learning practices on future assessments. To ensure equality and inclusion with respect to diverse student cohorts, a variety of feedback methods can be used, including written and spoken comments, technology-aided systems, and peer and self-assessment."
  stem: none
  statementType: expectation
  rung: none
  force: will
  level: none
  appliesTo: "Public Policy and Public Administration courses and their students"
  addressee: both
  verbs: ["designed", "given", "feed"]
  about: "constructive feedback throughout study"
  themes: [none]
  domain: none
  award: ["none"]
  gradeOf: none
  paraphrase: "Feedback is central to learning and helps students see their progress and improve; it will be constructive, consistent and specific, and will come throughout study on formative and summative work so that students can carry it forward; varied methods, from written and spoken comments to technology and peer and self-assessment, support equality and inclusion."
  quote: full   # the issuer's statement is in `source` (D-std-0014)
  audience: both
  subjects: inherited
- id: qaa/public-policy-and-public-administration-2025/4.2
  locator: { number: "4.2", headingPath: ["Benchmark standards", "Introduction"] }
  span: { start: 52778, end: 53595 }
  source: "4.2 The vast majority of students will perform significantly better than the minimum threshold standards. Each higher education provider has its own method of determining what appropriate evidence of this achievement will be and should refer to Annex D of The\n\nFrameworks for Higher Education Qualifications of UK Degree-Awarding Bodies which sets out the outcome classification descriptions for The Framework for Higher Education Qualifications of Degree-Awarding Bodies in England, Wales and Northern Ireland (FHEQ) Level 6 and The Framework for Qualifications of Higher Education Institutions in Scotland (FQHEIS) Level 10 degrees. These frameworks contain the common descriptions of the four main degree outcome classifications for bachelor's degrees with honours: 1st, 2:1, 2:2 and 3rd, and postgraduate degrees."
  stem: none
  statementType: requirement
  rung: none
  force: should
  level: fheq:6
  appliesTo: "each higher education provider"
  addressee: provider
  verbs: ["refer", "perform"]
  about: "using Annex D for classification"
  themes: [none]
  domain: none
  award: ["bachelor's with honours"]
  gradeOf: none
  paraphrase: "Most students will perform well above the minimum threshold; each provider decides what evidence shows this and should use Annex D of the 2024 Frameworks, the classification descriptions for FHEQ level 6 and FQHEIS level 10 degrees, which describe the four honours classes and postgraduate outcomes."
  quote: full   # the issuer's statement is in `source` (D-std-0014)
  audience: practitioner
  subjects: inherited
- id: qaa/public-policy-and-public-administration-2025/4.3
  locator: { number: "4.3", headingPath: ["Benchmark standards", "Introduction"] }
  span: { start: 53596, end: 54075 }
  source: "4.3 Please note that the minimum threshold standards are not intended to specify universal competence standards for a discipline. If a provider chooses to develop competence standards (as defined by the Equality Act 2010) as part of a programme specification, these can be informed by the relevant Subject Benchmark Statement along with any PSRB requirements. In these circumstances providers should follow the most recent guidance from the Equality and Human Rights Commission ."
  stem: none
  statementType: requirement
  rung: none
  force: should
  level: none
  appliesTo: "providers writing competence standards"
  addressee: provider
  verbs: ["follow", "informed"]
  about: "competence standards and EHRC guidance"
  themes: [none]
  domain: none
  award: ["none"]
  gradeOf: none
  paraphrase: "The minimum threshold standards are not universal competence standards; a provider that writes competence standards under the Equality Act 2010 into a programme specification may draw on this statement and any PSRB requirements, and should follow the Equality and Human Rights Commission's latest guidance."
  quote: full   # the issuer's statement is in `source` (D-std-0014)
  audience: practitioner
  subjects: inherited
- id: qaa/public-policy-and-public-administration-2025/4.5.b1
  locator: { number: "4.5.b1", headingPath: ["Benchmark standards", "Threshold level"] }
  span: { start: 54676, end: 54756 }
  source: "knowledge of key concepts and theories, as well as awareness of current evidence"
  stem: "4.5"
  statementType: threshold
  rung: threshold
  force: threshold
  level: fheq:6
  appliesTo: "honours graduates at threshold level"
  addressee: learner
  verbs: []
  about: "key concepts, theories and current evidence"
  themes: [none]
  domain: knowledge
  award: ["bachelor's with honours"]
  gradeOf: none
  paraphrase: "Threshold (the minimum for the award): Shows knowledge of the subject's main concepts and theories and an awareness of the evidence now available."
  quote: full   # the issuer's statement is in `source` (D-std-0014)
  audience: both
  subjects: inherited
- id: qaa/public-policy-and-public-administration-2025/4.5.b2
  locator: { number: "4.5.b2", headingPath: ["Benchmark standards", "Threshold level"] }
  span: { start: 54759, end: 54965 }
  source: "knowledge, understanding and awareness of current problems and/or new insights, much of which is at, or informed by, the forefront of the academic discipline, field of study or area of professional practice"
  stem: "4.5"
  statementType: threshold
  rung: threshold
  force: threshold
  level: fheq:6
  appliesTo: "honours graduates at threshold level"
  addressee: learner
  verbs: ["informed"]
  about: "current problems and new insights near the forefront"
  themes: [none]
  domain: understanding
  award: ["bachelor's with honours"]
  gradeOf: none
  paraphrase: "Threshold (the minimum for the award): Shows knowledge, understanding and awareness of present problems or fresh insights, much of it drawn from or shaped by leading work in the discipline or in professional practice."
  quote: full   # the issuer's statement is in `source` (D-std-0014)
  audience: both
  subjects: inherited
- id: qaa/public-policy-and-public-administration-2025/4.5.b3
  locator: { number: "4.5.b3", headingPath: ["Benchmark standards", "Threshold level"] }
  span: { start: 54968, end: 55063 }
  source: "an ability to construct an argument, synthesising relevant information and exercising judgement"
  stem: "4.5"
  statementType: threshold
  rung: threshold
  force: threshold
  level: fheq:6
  appliesTo: "honours graduates at threshold level"
  addressee: learner
  verbs: ["construct", "synthesising", "exercising"]
  about: "building an argument with judgement"
  themes: [none]
  domain: generic-skill
  award: ["bachelor's with honours"]
  gradeOf: none
  paraphrase: "Threshold (the minimum for the award): Can build an argument, bringing relevant information together and using judgement."
  quote: full   # the issuer's statement is in `source` (D-std-0014)
  audience: both
  subjects: inherited
- id: qaa/public-policy-and-public-administration-2025/4.5.b4
  locator: { number: "4.5.b4", headingPath: ["Benchmark standards", "Threshold level"] }
  span: { start: 55066, end: 55196 }
  source: "an ability to deal with complex issues both systematically and creatively, making sound judgements in the absence of complete data"
  stem: "4.5"
  statementType: threshold
  rung: threshold
  force: threshold
  level: fheq:6
  appliesTo: "honours graduates at threshold level"
  addressee: learner
  verbs: ["deal", "making"]
  about: "complex issues and judgement with incomplete data"
  themes: [none]
  domain: generic-skill
  award: ["bachelor's with honours"]
  gradeOf: none
  paraphrase: "Threshold (the minimum for the award): Can handle complex issues in an orderly and inventive way and reach sound judgements when data are incomplete."
  quote: full   # the issuer's statement is in `source` (D-std-0014)
  audience: both
  subjects: inherited
- id: qaa/public-policy-and-public-administration-2025/4.5.b5
  locator: { number: "4.5.b5", headingPath: ["Benchmark standards", "Threshold level"] }
  span: { start: 55199, end: 55308 }
  source: "an ability to identify, investigate and solve problems in relation to both practical and theoretical contexts"
  stem: "4.5"
  statementType: threshold
  rung: threshold
  force: threshold
  level: fheq:6
  appliesTo: "honours graduates at threshold level"
  addressee: learner
  verbs: ["identify", "investigate", "solve"]
  about: "problems in practical and theoretical contexts"
  themes: [none]
  domain: subject-skill
  award: ["bachelor's with honours"]
  gradeOf: none
  paraphrase: "Threshold (the minimum for the award): Can find, look into and resolve problems in both practical and theoretical settings."
  quote: full   # the issuer's statement is in `source` (D-std-0014)
  audience: both
  subjects: inherited
- id: qaa/public-policy-and-public-administration-2025/4.5.b6
  locator: { number: "4.5.b6", headingPath: ["Benchmark standards", "Threshold level"] }
  span: { start: 55315, end: 55412 }
  source: "an ability to evaluate and apply approaches to collecting, analysing and presenting relevant data"
  stem: "4.5"
  statementType: threshold
  rung: threshold
  force: threshold
  level: fheq:6
  appliesTo: "honours graduates at threshold level"
  addressee: learner
  verbs: ["evaluate", "apply", "collecting", "analysing", "presenting"]
  about: "approaches to collecting, analysing and presenting data"
  themes: [none]
  domain: subject-skill
  award: ["bachelor's with honours"]
  gradeOf: none
  paraphrase: "Threshold (the minimum for the award): Can judge and use suitable ways of gathering, analysing and presenting relevant data."
  quote: full   # the issuer's statement is in `source` (D-std-0014)
  audience: both
  subjects: inherited
- id: qaa/public-policy-and-public-administration-2025/4.5.b7
  locator: { number: "4.5.b7", headingPath: ["Benchmark standards", "Threshold level"] }
  span: { start: 55415, end: 55537 }
  source: "collaboration with others to achieve common goals through, for example, group work, group projects and group presentations"
  stem: "4.5"
  statementType: threshold
  rung: threshold
  force: threshold
  level: fheq:6
  appliesTo: "honours graduates at threshold level"
  addressee: learner
  verbs: ["achieve"]
  about: "collaboration towards shared goals"
  themes: [none]
  domain: generic-skill
  award: ["bachelor's with honours"]
  gradeOf: none
  paraphrase: "Threshold (the minimum for the award): Works with others towards shared aims, for instance in group tasks, projects and presentations."
  quote: full   # the issuer's statement is in `source` (D-std-0014)
  audience: both
  subjects: inherited
- id: qaa/public-policy-and-public-administration-2025/4.5.b8
  locator: { number: "4.5.b8", headingPath: ["Benchmark standards", "Threshold level"] }
  span: { start: 55540, end: 55629 }
  source: "communication through a variety of context-appropriate formats for a variety of audiences"
  stem: "4.5"
  statementType: threshold
  rung: threshold
  force: threshold
  level: fheq:6
  appliesTo: "honours graduates at threshold level"
  addressee: learner
  verbs: []
  about: "communication in varied formats and for varied audiences"
  themes: [none]
  domain: generic-skill
  award: ["bachelor's with honours"]
  gradeOf: none
  paraphrase: "Threshold (the minimum for the award): Communicates in formats suited to the context and to different audiences."
  quote: full   # the issuer's statement is in `source` (D-std-0014)
  audience: both
  subjects: inherited
- id: qaa/public-policy-and-public-administration-2025/4.5.b9
  locator: { number: "4.5.b9", headingPath: ["Benchmark standards", "Threshold level"] }
  span: { start: 55632, end: 55664 }
  source: "reflection on their own learning"
  stem: "4.5"
  statementType: threshold
  rung: threshold
  force: threshold
  level: fheq:6
  appliesTo: "honours graduates at threshold level"
  addressee: learner
  verbs: []
  about: "reflection on own learning"
  themes: [none]
  domain: generic-skill
  award: ["bachelor's with honours"]
  gradeOf: none
  paraphrase: "Threshold (the minimum for the award): Reflects on their own learning."
  quote: full   # the issuer's statement is in `source` (D-std-0014)
  audience: both
  subjects: inherited
- id: qaa/public-policy-and-public-administration-2025/4.5.b10
  locator: { number: "4.5.b10", headingPath: ["Benchmark standards", "Threshold level"] }
  span: { start: 55667, end: 55768 }
  source: "management of their own learning and projects effectively while working individually and collectively"
  stem: "4.5"
  statementType: threshold
  rung: threshold
  force: threshold
  level: fheq:6
  appliesTo: "honours graduates at threshold level"
  addressee: learner
  verbs: ["working"]
  about: "managing own learning and projects"
  themes: [none]
  domain: generic-skill
  award: ["bachelor's with honours"]
  gradeOf: none
  paraphrase: "Threshold (the minimum for the award): Manages their own learning and projects well, working alone and with others."
  quote: full   # the issuer's statement is in `source` (D-std-0014)
  audience: both
  subjects: inherited
- id: qaa/public-policy-and-public-administration-2025/4.5.b11
  locator: { number: "4.5.b11", headingPath: ["Benchmark standards", "Threshold level"] }
  span: { start: 55771, end: 55840 }
  source: "an ability to understand and apply the principles of ethical research"
  stem: "4.5"
  statementType: threshold
  rung: threshold
  force: threshold
  level: fheq:6
  appliesTo: "honours graduates at threshold level"
  addressee: learner
  verbs: ["understand", "apply"]
  about: "principles of ethical research"
  themes: [none]
  domain: subject-skill
  award: ["bachelor's with honours"]
  gradeOf: none
  paraphrase: "Threshold (the minimum for the award): Can understand and use the principles of ethical research."
  quote: full   # the issuer's statement is in `source` (D-std-0014)
  audience: both
  subjects: inherited
- id: qaa/public-policy-and-public-administration-2025/4.5.b12
  locator: { number: "4.5.b12", headingPath: ["Benchmark standards", "Threshold level"] }
  span: { start: 55843, end: 55952 }
  source: "organisation and deployment of evidence, data and information from a variety of secondary and primary sources"
  stem: "4.5"
  statementType: threshold
  rung: threshold
  force: threshold
  level: fheq:6
  appliesTo: "honours graduates at threshold level"
  addressee: learner
  verbs: []
  about: "organising and using evidence from primary and secondary sources"
  themes: [none]
  domain: subject-skill
  award: ["bachelor's with honours"]
  gradeOf: none
  paraphrase: "Threshold (the minimum for the award): Organises and uses evidence, data and information from a range of primary and secondary sources."
  quote: full   # the issuer's statement is in `source` (D-std-0014)
  audience: both
  subjects: inherited
- id: qaa/public-policy-and-public-administration-2025/4.5.b13
  locator: { number: "4.5.b13", headingPath: ["Benchmark standards", "Threshold level"] }
  span: { start: 55955, end: 56085 }
  source: "an ability to understand the importance of personal integrity and an awareness of the potential ethical impacts of decision-making"
  stem: "4.5"
  statementType: threshold
  rung: threshold
  force: threshold
  level: fheq:6
  appliesTo: "honours graduates at threshold level"
  addressee: learner
  verbs: ["understand"]
  about: "personal integrity and the ethics of decisions"
  themes: [none]
  domain: understanding
  award: ["bachelor's with honours"]
  gradeOf: none
  paraphrase: "Threshold (the minimum for the award): Can see why personal integrity matters and is aware of the ethical effects decisions may have."
  quote: full   # the issuer's statement is in `source` (D-std-0014)
  audience: both
  subjects: inherited
- id: qaa/public-policy-and-public-administration-2025/4.5.b14
  locator: { number: "4.5.b14", headingPath: ["Benchmark standards", "Threshold level"] }
  span: { start: 56088, end: 56134 }
  source: "understanding and use of constructive feedback"
  stem: "4.5"
  statementType: threshold
  rung: threshold
  force: threshold
  level: fheq:6
  appliesTo: "honours graduates at threshold level"
  addressee: learner
  verbs: []
  about: "using constructive feedback"
  themes: [none]
  domain: generic-skill
  award: ["bachelor's with honours"]
  gradeOf: none
  paraphrase: "Threshold (the minimum for the award): Understands and uses constructive feedback."
  quote: full   # the issuer's statement is in `source` (D-std-0014)
  audience: both
  subjects: inherited
- id: qaa/public-policy-and-public-administration-2025/4.5.b15
  locator: { number: "4.5.b15", headingPath: ["Benchmark standards", "Threshold level"] }
  span: { start: 56137, end: 56241 }
  source: "an ability to select and use appropriate communication, information and data analysis aids and software."
  stem: "4.5"
  statementType: threshold
  rung: threshold
  force: threshold
  level: fheq:6
  appliesTo: "honours graduates at threshold level"
  addressee: learner
  verbs: ["select", "use"]
  about: "communication, information and data tools and software"
  themes: [none]
  domain: generic-skill
  award: ["bachelor's with honours"]
  gradeOf: none
  paraphrase: "Threshold (the minimum for the award): Can choose and use suitable aids and software for communication, information and data analysis."
  quote: full   # the issuer's statement is in `source` (D-std-0014)
  audience: both
  subjects: inherited
- id: qaa/public-policy-and-public-administration-2025/4.6.b1
  locator: { number: "4.6.b1", headingPath: ["Benchmark standards", "Excellent level"] }
  span: { start: 56429, end: 56546 }
  source: "a consistent and detailed knowledge of key concepts and theories, as well as awareness of current evidence and issues"
  stem: "4.6"
  statementType: excellent
  rung: excellent
  force: will
  level: fheq:6
  appliesTo: "honours graduates at an excellent level"
  addressee: learner
  verbs: []
  about: "consistent, detailed knowledge of concepts, theories, evidence and issues"
  themes: [none]
  domain: knowledge
  award: ["bachelor's with honours"]
  gradeOf: { statement: qaa/public-policy-and-public-administration-2025/4.5.b1, basis: inferred }
  paraphrase: "Excellent level (will): Shows consistent and detailed knowledge of the main concepts and theories and awareness of current evidence and issues."
  quote: full   # the issuer's statement is in `source` (D-std-0014)
  audience: both
  subjects: inherited
- id: qaa/public-policy-and-public-administration-2025/4.6.b2
  locator: { number: "4.6.b2", headingPath: ["Benchmark standards", "Excellent level"] }
  span: { start: 56549, end: 56777 }
  source: "a systematic knowledge, understanding and critical awareness of current problems and/or new insights, much of which is at, or informed by, the forefront of the academic discipline, field of study or area of professional practice"
  stem: "4.6"
  statementType: excellent
  rung: excellent
  force: will
  level: fheq:6
  appliesTo: "honours graduates at an excellent level"
  addressee: learner
  verbs: ["informed"]
  about: "systematic, critical awareness of current problems and insights"
  themes: [none]
  domain: understanding
  award: ["bachelor's with honours"]
  gradeOf: { statement: qaa/public-policy-and-public-administration-2025/4.5.b2, basis: inferred }
  paraphrase: "Excellent level (will): Shows systematic knowledge and understanding, and a critical awareness, of present problems or new insights, much of it from leading work in the discipline or practice."
  quote: full   # the issuer's statement is in `source` (D-std-0014)
  audience: both
  subjects: inherited
- id: qaa/public-policy-and-public-administration-2025/4.6.b3
  locator: { number: "4.6.b3", headingPath: ["Benchmark standards", "Excellent level"] }
  span: { start: 56780, end: 56927 }
  source: "a sophisticated ability to collaborate with others to achieve common goals through, for example, group work, group projects and group presentations"
  stem: "4.6"
  statementType: excellent
  rung: excellent
  force: will
  level: fheq:6
  appliesTo: "honours graduates at an excellent level"
  addressee: learner
  verbs: ["collaborate", "achieve"]
  about: "sophisticated collaboration towards shared goals"
  themes: [none]
  domain: generic-skill
  award: ["bachelor's with honours"]
  gradeOf: { statement: qaa/public-policy-and-public-administration-2025/4.5.b7, basis: inferred }
  paraphrase: "Excellent level (will): Collaborates with others in a sophisticated way to reach shared aims, for instance in group work, projects and presentations."
  quote: full   # the issuer's statement is in `source` (D-std-0014)
  audience: both
  subjects: inherited
- id: qaa/public-policy-and-public-administration-2025/4.6.b4
  locator: { number: "4.6.b4", headingPath: ["Benchmark standards", "Excellent level"] }
  span: { start: 56930, end: 57040 }
  source: "a developed ability to communicate through a variety of context appropriate formats for a variety of audiences"
  stem: "4.6"
  statementType: excellent
  rung: excellent
  force: will
  level: fheq:6
  appliesTo: "honours graduates at an excellent level"
  addressee: learner
  verbs: ["communicate"]
  about: "developed communication in varied formats and for varied audiences"
  themes: [none]
  domain: generic-skill
  award: ["bachelor's with honours"]
  gradeOf: { statement: qaa/public-policy-and-public-administration-2025/4.5.b8, basis: inferred }
  paraphrase: "Excellent level (will): Communicates with developed skill in formats suited to the context and to varied audiences."
  quote: full   # the issuer's statement is in `source` (D-std-0014)
  audience: both
  subjects: inherited
- id: qaa/public-policy-and-public-administration-2025/4.6.b5
  locator: { number: "4.6.b5", headingPath: ["Benchmark standards", "Excellent level"] }
  span: { start: 57043, end: 57162 }
  source: "a strong capability to construct reasoned argument, synthesising relevant information and exercising critical judgement"
  stem: "4.6"
  statementType: excellent
  rung: excellent
  force: will
  level: fheq:6
  appliesTo: "honours graduates at an excellent level"
  addressee: learner
  verbs: ["construct", "synthesising", "exercising"]
  about: "strong reasoned argument with critical judgement"
  themes: [none]
  domain: generic-skill
  award: ["bachelor's with honours"]
  gradeOf: { statement: qaa/public-policy-and-public-administration-2025/4.5.b3, basis: inferred }
  paraphrase: "Excellent level (will): Shows a strong capacity to build reasoned arguments, drawing relevant information together and judging critically."
  quote: full   # the issuer's statement is in `source` (D-std-0014)
  audience: both
  subjects: inherited
- id: qaa/public-policy-and-public-administration-2025/4.6.b6
  locator: { number: "4.6.b6", headingPath: ["Benchmark standards", "Excellent level"] }
  span: { start: 57165, end: 57228 }
  source: "a developed ability to critically reflect on their own learning"
  stem: "4.6"
  statementType: excellent
  rung: excellent
  force: will
  level: fheq:6
  appliesTo: "honours graduates at an excellent level"
  addressee: learner
  verbs: ["reflect"]
  about: "critical reflection on own learning"
  themes: [none]
  domain: generic-skill
  award: ["bachelor's with honours"]
  gradeOf: { statement: qaa/public-policy-and-public-administration-2025/4.5.b9, basis: inferred }
  paraphrase: "Excellent level (will): Shows a developed capacity to reflect critically on their own learning."
  quote: full   # the issuer's statement is in `source` (D-std-0014)
  audience: both
  subjects: inherited
- id: qaa/public-policy-and-public-administration-2025/4.6.b7
  locator: { number: "4.6.b7", headingPath: ["Benchmark standards", "Excellent level"] }
  span: { start: 57231, end: 57360 }
  source: "effective handling of complex issues, both systematically and creatively, making sound judgements in the absence of complete data"
  stem: "4.6"
  statementType: excellent
  rung: excellent
  force: will
  level: fheq:6
  appliesTo: "honours graduates at an excellent level"
  addressee: learner
  verbs: ["making"]
  about: "effective handling of complex issues with incomplete data"
  themes: [none]
  domain: generic-skill
  award: ["bachelor's with honours"]
  gradeOf: { statement: qaa/public-policy-and-public-administration-2025/4.5.b4, basis: inferred }
  paraphrase: "Excellent level (will): Handles complex issues effectively, in an orderly and inventive way, reaching sound judgements when data are incomplete."
  quote: full   # the issuer's statement is in `source` (D-std-0014)
  audience: both
  subjects: inherited
- id: qaa/public-policy-and-public-administration-2025/4.6.b8
  locator: { number: "4.6.b8", headingPath: ["Benchmark standards", "Excellent level"] }
  span: { start: 57363, end: 57495 }
  source: "confidence in identifying, investigating and solving problems through thinking creatively in both practical and theoretical contexts"
  stem: "4.6"
  statementType: excellent
  rung: excellent
  force: will
  level: fheq:6
  appliesTo: "honours graduates at an excellent level"
  addressee: learner
  verbs: ["identifying", "investigating", "solving", "thinking"]
  about: "confident, creative problem-solving"
  themes: [none]
  domain: subject-skill
  award: ["bachelor's with honours"]
  gradeOf: { statement: qaa/public-policy-and-public-administration-2025/4.5.b5, basis: inferred }
  paraphrase: "Excellent level (will): Finds, looks into and resolves problems with confidence, thinking creatively in practical and theoretical settings."
  quote: full   # the issuer's statement is in `source` (D-std-0014)
  audience: both
  subjects: inherited
- id: qaa/public-policy-and-public-administration-2025/4.6.b9
  locator: { number: "4.6.b9", headingPath: ["Benchmark standards", "Excellent level"] }
  span: { start: 57498, end: 57605 }
  source: "an excellent ability to evaluate and apply approaches to collecting, analysing and presenting relevant data"
  stem: "4.6"
  statementType: excellent
  rung: excellent
  force: will
  level: fheq:6
  appliesTo: "honours graduates at an excellent level"
  addressee: learner
  verbs: ["evaluate", "apply", "collecting", "analysing", "presenting"]
  about: "excellent judgement of data approaches"
  themes: [none]
  domain: subject-skill
  award: ["bachelor's with honours"]
  gradeOf: { statement: qaa/public-policy-and-public-administration-2025/4.5.b6, basis: inferred }
  paraphrase: "Excellent level (will): Shows an excellent capacity to judge and use suitable ways of gathering, analysing and presenting data."
  quote: full   # the issuer's statement is in `source` (D-std-0014)
  audience: both
  subjects: inherited
- id: qaa/public-policy-and-public-administration-2025/4.6.b10
  locator: { number: "4.6.b10", headingPath: ["Benchmark standards", "Excellent level"] }
  span: { start: 57608, end: 57740 }
  source: "effective management of their own learning and projects in a timely and critical fashion while working individually and collectively"
  stem: "4.6"
  statementType: excellent
  rung: excellent
  force: will
  level: fheq:6
  appliesTo: "honours graduates at an excellent level"
  addressee: learner
  verbs: ["working"]
  about: "timely, critical management of own learning and projects"
  themes: [none]
  domain: generic-skill
  award: ["bachelor's with honours"]
  gradeOf: { statement: qaa/public-policy-and-public-administration-2025/4.5.b10, basis: inferred }
  paraphrase: "Excellent level (will): Manages their own learning and projects effectively, on time and critically, alone and with others."
  quote: full   # the issuer's statement is in `source` (D-std-0014)
  audience: both
  subjects: inherited
- id: qaa/public-policy-and-public-administration-2025/4.6.b11
  locator: { number: "4.6.b11", headingPath: ["Benchmark standards", "Excellent level"] }
  span: { start: 57743, end: 57815 }
  source: "clarity in understanding and applying the principles of ethical research"
  stem: "4.6"
  statementType: excellent
  rung: excellent
  force: will
  level: fheq:6
  appliesTo: "honours graduates at an excellent level"
  addressee: learner
  verbs: ["understanding", "applying"]
  about: "clear grasp and use of research ethics"
  themes: [none]
  domain: subject-skill
  award: ["bachelor's with honours"]
  gradeOf: { statement: qaa/public-policy-and-public-administration-2025/4.5.b11, basis: inferred }
  paraphrase: "Excellent level (will): Understands and uses the principles of ethical research with clarity."
  quote: full   # the issuer's statement is in `source` (D-std-0014)
  audience: both
  subjects: inherited
- id: qaa/public-policy-and-public-administration-2025/4.6.b12
  locator: { number: "4.6.b12", headingPath: ["Benchmark standards", "Excellent level"] }
  span: { start: 57818, end: 57937 }
  source: "effective organisation and deployment of evidence, data and information from a variety of secondary and primary sources"
  stem: "4.6"
  statementType: excellent
  rung: excellent
  force: will
  level: fheq:6
  appliesTo: "honours graduates at an excellent level"
  addressee: learner
  verbs: []
  about: "effective organisation and use of evidence from varied sources"
  themes: [none]
  domain: subject-skill
  award: ["bachelor's with honours"]
  gradeOf: { statement: qaa/public-policy-and-public-administration-2025/4.5.b12, basis: inferred }
  paraphrase: "Excellent level (will): Organises and uses evidence, data and information from a range of primary and secondary sources effectively."
  quote: full   # the issuer's statement is in `source` (D-std-0014)
  audience: both
  subjects: inherited
- id: qaa/public-policy-and-public-administration-2025/4.6.b13
  locator: { number: "4.6.b13", headingPath: ["Benchmark standards", "Excellent level"] }
  span: { start: 57944, end: 58074 }
  source: "evident understanding of the importance of personal integrity and an awareness of the potential ethical impacts of decision making"
  stem: "4.6"
  statementType: excellent
  rung: excellent
  force: will
  level: fheq:6
  appliesTo: "honours graduates at an excellent level"
  addressee: learner
  verbs: []
  about: "evident grasp of integrity and the ethics of decisions"
  themes: [none]
  domain: understanding
  award: ["bachelor's with honours"]
  gradeOf: { statement: qaa/public-policy-and-public-administration-2025/4.5.b13, basis: inferred }
  paraphrase: "Excellent level (will): Shows a clear understanding of why personal integrity matters and an awareness of the ethical effects decisions may have."
  quote: full   # the issuer's statement is in `source` (D-std-0014)
  audience: both
  subjects: inherited
- id: qaa/public-policy-and-public-administration-2025/4.6.b14
  locator: { number: "4.6.b14", headingPath: ["Benchmark standards", "Excellent level"] }
  span: { start: 58077, end: 58188 }
  source: "analytical evaluation of the relationship between academic practice and professional behaviour (where relevant)"
  stem: "4.6"
  statementType: excellent
  rung: excellent
  force: will
  level: fheq:6
  appliesTo: "honours graduates at an excellent level"
  addressee: learner
  verbs: []
  about: "academic practice and professional behaviour"
  themes: [none]
  domain: subject-skill
  award: ["bachelor's with honours"]
  gradeOf: none
  paraphrase: "Excellent level (will): Evaluates analytically, where relevant, how academic practice relates to professional conduct."
  quote: full   # the issuer's statement is in `source` (D-std-0014)
  audience: both
  subjects: inherited
- id: qaa/public-policy-and-public-administration-2025/4.6.b15
  locator: { number: "4.6.b15", headingPath: ["Benchmark standards", "Excellent level"] }
  span: { start: 58191, end: 58247 }
  source: "developed understanding and use of constructive feedback"
  stem: "4.6"
  statementType: excellent
  rung: excellent
  force: will
  level: fheq:6
  appliesTo: "honours graduates at an excellent level"
  addressee: learner
  verbs: []
  about: "developed use of constructive feedback"
  themes: [none]
  domain: generic-skill
  award: ["bachelor's with honours"]
  gradeOf: { statement: qaa/public-policy-and-public-administration-2025/4.5.b14, basis: inferred }
  paraphrase: "Excellent level (will): Shows a developed understanding and use of constructive feedback."
  quote: full   # the issuer's statement is in `source` (D-std-0014)
  audience: both
  subjects: inherited
- id: qaa/public-policy-and-public-administration-2025/4.6.b16
  locator: { number: "4.6.b16", headingPath: ["Benchmark standards", "Excellent level"] }
  span: { start: 58250, end: 58360 }
  source: "a strong ability to select and use appropriate communication, information and data analysis aids and software."
  stem: "4.6"
  statementType: excellent
  rung: excellent
  force: will
  level: fheq:6
  appliesTo: "honours graduates at an excellent level"
  addressee: learner
  verbs: ["select", "use"]
  about: "strong choice and use of tools and software"
  themes: [none]
  domain: generic-skill
  award: ["bachelor's with honours"]
  gradeOf: { statement: qaa/public-policy-and-public-administration-2025/4.5.b15, basis: inferred }
  paraphrase: "Excellent level (will): Shows a strong capacity to choose and use suitable aids and software for communication, information and data analysis."
  quote: full   # the issuer's statement is in `source` (D-std-0014)
  audience: both
  subjects: inherited
- id: qaa/public-policy-and-public-administration-2025/4.7
  locator: { number: "4.7", headingPath: ["Benchmark standards", "Master's"] }
  span: { start: 58370, end: 58605 }
  source: "4.7 Students graduating with a master's degree in Public Policy and/or Public Administration are expected to demonstrate graduate outcomes, command of one or more specialist areas of the subject, and independence in project-based work."
  stem: none
  statementType: threshold
  rung: threshold
  force: will
  level: fheq:7
  appliesTo: "master's graduates in the subject"
  addressee: learner
  verbs: ["demonstrate"]
  about: "specialist command and independent project work"
  themes: [none]
  domain: subject-skill
  award: ["master's"]
  gradeOf: none
  paraphrase: "Master's graduates in the subject are expected to show graduate outcomes, command of at least one specialist area and independence in project work."
  quote: full   # the issuer's statement is in `source` (D-std-0014)
  audience: both
  subjects: inherited
- id: qaa/public-policy-and-public-administration-2025/4.7.b1
  locator: { number: "4.7.b1", headingPath: ["Benchmark standards", "Master's"] }
  span: { start: 58711, end: 58852 }
  source: "a systematic and deep understanding of relevant knowledge about public sector organisations, their external context, and how they are managed"
  stem: "4.7"
  statementType: threshold
  rung: threshold
  force: will
  level: fheq:7
  appliesTo: "master's graduates in the subject"
  addressee: learner
  verbs: []
  about: "public sector organisations, their context and management"
  themes: [none]
  domain: knowledge
  award: ["master's"]
  gradeOf: none
  paraphrase: "Master's level (will): Understands systematically and in depth what is known about public sector organisations, their surroundings and how they are run."
  quote: full   # the issuer's statement is in `source` (D-std-0014)
  audience: both
  subjects: inherited
- id: qaa/public-policy-and-public-administration-2025/4.7.b2
  locator: { number: "4.7.b2", headingPath: ["Benchmark standards", "Master's"] }
  span: { start: 58855, end: 59012 }
  source: "a comprehensive and detailed understanding of techniques for detailed investigation, research and evaluation of, or advanced scholarship in, the subject area"
  stem: "4.7"
  statementType: threshold
  rung: threshold
  force: will
  level: fheq:7
  appliesTo: "master's graduates in the subject"
  addressee: learner
  verbs: []
  about: "techniques for investigation, research and evaluation"
  themes: [none]
  domain: understanding
  award: ["master's"]
  gradeOf: none
  paraphrase: "Master's level (will): Understands fully and in detail the techniques for close investigation, research and evaluation, or advanced scholarship, in the field."
  quote: full   # the issuer's statement is in `source` (D-std-0014)
  audience: both
  subjects: inherited
- id: qaa/public-policy-and-public-administration-2025/4.7.b3
  locator: { number: "4.7.b3", headingPath: ["Benchmark standards", "Master's"] }
  span: { start: 59015, end: 59089 }
  source: "an ability to demonstrate proactive and independent approaches to learning"
  stem: "4.7"
  statementType: threshold
  rung: threshold
  force: will
  level: fheq:7
  appliesTo: "master's graduates in the subject"
  addressee: learner
  verbs: ["demonstrate"]
  about: "proactive, independent learning"
  themes: [none]
  domain: generic-skill
  award: ["master's"]
  gradeOf: none
  paraphrase: "Master's level (will): Shows a proactive and independent approach to learning."
  quote: full   # the issuer's statement is in `source` (D-std-0014)
  audience: both
  subjects: inherited
- id: qaa/public-policy-and-public-administration-2025/4.7.b4
  locator: { number: "4.7.b4", headingPath: ["Benchmark standards", "Master's"] }
  span: { start: 59092, end: 59172 }
  source: "an ability to demonstrate agile, reflexive and innovative approaches to learning"
  stem: "4.7"
  statementType: threshold
  rung: threshold
  force: will
  level: fheq:7
  appliesTo: "master's graduates in the subject"
  addressee: learner
  verbs: ["demonstrate"]
  about: "agile, reflexive and innovative learning"
  themes: [none]
  domain: generic-skill
  award: ["master's"]
  gradeOf: none
  paraphrase: "Master's level (will): Shows an agile, reflexive and inventive approach to learning."
  quote: full   # the issuer's statement is in `source` (D-std-0014)
  audience: both
  subjects: inherited
- id: qaa/public-policy-and-public-administration-2025/4.7.b5
  locator: { number: "4.7.b5", headingPath: ["Benchmark standards", "Master's"] }
  span: { start: 59175, end: 59269 }
  source: "a critical and nuanced awareness of current issues, which is informed by research and practice"
  stem: "4.7"
  statementType: threshold
  rung: threshold
  force: will
  level: fheq:7
  appliesTo: "master's graduates in the subject"
  addressee: learner
  verbs: ["informed"]
  about: "critical awareness of current issues"
  themes: [none]
  domain: understanding
  award: ["master's"]
  gradeOf: none
  paraphrase: "Master's level (will): Is critically and subtly aware of current issues, drawing on research and practice."
  quote: full   # the issuer's statement is in `source` (D-std-0014)
  audience: both
  subjects: inherited
- id: qaa/public-policy-and-public-administration-2025/4.7.b6
  locator: { number: "4.7.b6", headingPath: ["Benchmark standards", "Master's"] }
  span: { start: 59272, end: 59372 }
  source: "conceptual competencies that enable critical evaluation of current research and advanced scholarship"
  stem: "4.7"
  statementType: threshold
  rung: threshold
  force: will
  level: fheq:7
  appliesTo: "master's graduates in the subject"
  addressee: learner
  verbs: ["enable"]
  about: "critically evaluating research and scholarship"
  themes: [none]
  domain: subject-skill
  award: ["master's"]
  gradeOf: none
  paraphrase: "Master's level (will): Has the conceptual competence to evaluate current research and advanced scholarship critically."
  quote: full   # the issuer's statement is in `source` (D-std-0014)
  audience: both
  subjects: inherited
- id: qaa/public-policy-and-public-administration-2025/4.7.b7
  locator: { number: "4.7.b7", headingPath: ["Benchmark standards", "Master's"] }
  span: { start: 59375, end: 59498 }
  source: "application of relevant knowledge to a range of complex situations, taking account of the subject area's hybrid environment"
  stem: "4.7"
  statementType: threshold
  rung: threshold
  force: will
  level: fheq:7
  appliesTo: "master's graduates in the subject"
  addressee: learner
  verbs: ["taking"]
  about: "applying knowledge to complex situations"
  themes: [none]
  domain: subject-skill
  award: ["master's"]
  gradeOf: none
  paraphrase: "Master's level (will): Applies relevant knowledge to a variety of complex situations, allowing for the field's mixed public, private and non-profit setting."
  quote: full   # the issuer's statement is in `source` (D-std-0014)
  audience: both
  subjects: inherited
- id: qaa/public-policy-and-public-administration-2025/4.7.b8
  locator: { number: "4.7.b8", headingPath: ["Benchmark standards", "Master's"] }
  span: { start: 59501, end: 59715 }
  source: "originality, creativity and entrepreneurship in the application of knowledge, together with a practical understanding of how established techniques of research and enquiry are used to create and interpret knowledge"
  stem: "4.7"
  statementType: threshold
  rung: threshold
  force: will
  level: fheq:7
  appliesTo: "master's graduates in the subject"
  addressee: learner
  verbs: ["used", "create", "interpret"]
  about: "originality, creativity and entrepreneurship with research techniques"
  themes: [none]
  domain: subject-skill
  award: ["master's"]
  gradeOf: none
  paraphrase: "Master's level (will): Applies knowledge with originality, creativity and entrepreneurship, and understands in practice how established research techniques produce and interpret knowledge."
  quote: full   # the issuer's statement is in `source` (D-std-0014)
  audience: both
  subjects: inherited
- id: qaa/public-policy-and-public-administration-2025/4.7.b9
  locator: { number: "4.7.b9", headingPath: ["Benchmark standards", "Master's"] }
  span: { start: 59718, end: 59816 }
  source: "an ability to evaluate and integrate theory, practice and experience in a wide range of situations"
  stem: "4.7"
  statementType: threshold
  rung: threshold
  force: will
  level: fheq:7
  appliesTo: "master's graduates in the subject"
  addressee: learner
  verbs: ["evaluate", "integrate"]
  about: "integrating theory, practice and experience"
  themes: [none]
  domain: subject-skill
  award: ["master's"]
  gradeOf: none
  paraphrase: "Master's level (will): Can assess and combine theory, practice and experience across many situations."
  quote: full   # the issuer's statement is in `source` (D-std-0014)
  audience: both
  subjects: inherited
- id: qaa/public-policy-and-public-administration-2025/4.7.b10
  locator: { number: "4.7.b10", headingPath: ["Benchmark standards", "Master's"] }
  span: { start: 59819, end: 59926 }
  source: "a comprehensive understanding of how the boundaries of knowledge are advanced through research and practice"
  stem: "4.7"
  statementType: threshold
  rung: threshold
  force: will
  level: fheq:7
  appliesTo: "master's graduates in the subject"
  addressee: learner
  verbs: ["advanced"]
  about: "how research and practice extend knowledge"
  themes: [none]
  domain: understanding
  award: ["master's"]
  gradeOf: none
  paraphrase: "Master's level (will): Understands fully how research and practice push forward the limits of knowledge."
  quote: full   # the issuer's statement is in `source` (D-std-0014)
  audience: both
  subjects: inherited
- id: qaa/public-policy-and-public-administration-2025/4.7.b11
  locator: { number: "4.7.b11", headingPath: ["Benchmark standards", "Master's"] }
  span: { start: 59929, end: 60068 }
  source: "a developed understanding of, and commitment to, public sector values and ethics, and the importance of acting with and promoting integrity"
  stem: "4.7"
  statementType: threshold
  rung: threshold
  force: will
  level: fheq:7
  appliesTo: "master's graduates in the subject"
  addressee: learner
  verbs: ["acting", "promoting"]
  about: "public sector values, ethics and integrity"
  themes: [none]
  domain: understanding
  award: ["master's"]
  gradeOf: none
  paraphrase: "Master's level (will): Understands, and is committed to, the values and ethics of public service, and sees why acting with integrity and encouraging it in others matters."
  quote: full   # the issuer's statement is in `source` (D-std-0014)
  audience: both
  subjects: inherited
- id: qaa/public-policy-and-public-administration-2025/4.7.b12
  locator: { number: "4.7.b12", headingPath: ["Benchmark standards", "Master's"] }
  span: { start: 60071, end: 60140 }
  source: "professional reflective capabilities to enhance professional practice"
  stem: "4.7"
  statementType: threshold
  rung: threshold
  force: will
  level: fheq:7
  appliesTo: "master's graduates in the subject"
  addressee: learner
  verbs: ["enhance"]
  about: "professional reflection"
  themes: [none]
  domain: generic-skill
  award: ["master's"]
  gradeOf: none
  paraphrase: "Master's level (will): Has professional reflective capacities that improve professional practice."
  quote: full   # the issuer's statement is in `source` (D-std-0014)
  audience: both
  subjects: inherited
- id: qaa/public-policy-and-public-administration-2025/4.7.b13
  locator: { number: "4.7.b13", headingPath: ["Benchmark standards", "Master's"] }
  span: { start: 60143, end: 60251 }
  source: "nuanced understanding of how Public Policy and/or Public Administration impact societies and the environment"
  stem: "4.7"
  statementType: threshold
  rung: threshold
  force: will
  level: fheq:7
  appliesTo: "master's graduates in the subject"
  addressee: learner
  verbs: ["impact"]
  about: "effects of policy and administration on societies and the environment"
  themes: [none]
  domain: understanding
  award: ["master's"]
  gradeOf: none
  paraphrase: "Master's level (will): Understands, with nuance, how policy and administration affect societies and the environment."
  quote: full   # the issuer's statement is in `source` (D-std-0014)
  audience: both
  subjects: inherited
- id: qaa/public-policy-and-public-administration-2025/4.7.b14
  locator: { number: "4.7.b14", headingPath: ["Benchmark standards", "Master's"] }
  span: { start: 60254, end: 60312 }
  source: "an ability to take an international and global perspective"
  stem: "4.7"
  statementType: threshold
  rung: threshold
  force: will
  level: fheq:7
  appliesTo: "master's graduates in the subject"
  addressee: learner
  verbs: ["take"]
  about: "an international and global perspective"
  themes: [none]
  domain: generic-skill
  award: ["master's"]
  gradeOf: none
  paraphrase: "Master's level (will): Can take an international and global view."
  quote: full   # the issuer's statement is in `source` (D-std-0014)
  audience: both
  subjects: inherited
- id: qaa/public-policy-and-public-administration-2025/4.7.b15
  locator: { number: "4.7.b15", headingPath: ["Benchmark standards", "Master's"] }
  span: { start: 60315, end: 60430 }
  source: "an ability to work, engage and lead in collaborative, multicultural, diverse environments domestically and globally"
  stem: "4.7"
  statementType: threshold
  rung: threshold
  force: will
  level: fheq:7
  appliesTo: "master's graduates in the subject"
  addressee: learner
  verbs: ["work", "engage", "lead"]
  about: "collaborative, diverse working and leadership"
  themes: [none]
  domain: generic-skill
  award: ["master's"]
  gradeOf: none
  paraphrase: "Master's level (will): Can work, engage and lead in collaborative, multicultural and diverse settings at home and abroad."
  quote: full   # the issuer's statement is in `source` (D-std-0014)
  audience: both
  subjects: inherited
- id: qaa/public-policy-and-public-administration-2025/4.7.b16
  locator: { number: "4.7.b16", headingPath: ["Benchmark standards", "Master's"] }
  span: { start: 60433, end: 60495 }
  source: "a capacity to negotiate and influence in professional contexts"
  stem: "4.7"
  statementType: threshold
  rung: threshold
  force: will
  level: fheq:7
  appliesTo: "master's graduates in the subject"
  addressee: learner
  verbs: ["negotiate", "influence"]
  about: "negotiation and influence"
  themes: [none]
  domain: generic-skill
  award: ["master's"]
  gradeOf: none
  paraphrase: "Master's level (will): Can negotiate and influence in professional settings."
  quote: full   # the issuer's statement is in `source` (D-std-0014)
  audience: both
  subjects: inherited
- id: qaa/public-policy-and-public-administration-2025/4.7.b17
  locator: { number: "4.7.b17", headingPath: ["Benchmark standards", "Master's"] }
  span: { start: 60498, end: 60576 }
  source: "independent learning ability required for continuing professional development."
  stem: "4.7"
  statementType: threshold
  rung: threshold
  force: will
  level: fheq:7
  appliesTo: "master's graduates in the subject"
  addressee: learner
  verbs: []
  about: "independent learning for continuing professional development"
  themes: [none]
  domain: generic-skill
  award: ["master's"]
  gradeOf: none
  paraphrase: "Master's level (will): Has the independent learning ability needed for continuing professional development."
  quote: full   # the issuer's statement is in `source` (D-std-0014)
  audience: both
  subjects: inherited
```

### S4a Audience versions
<!-- label: both; status: drafted; basis: primary. forPractitioner: for the programme designer or teacher. forBeneficiary: for the student, second person, naming no issuer. author-agent-written: instructions to an AI agent writing about the statement (a course document, a handbook, an outcome, a report). author-agent-dialogue: instructions to an AI agent using the statement in conversation (with a student, a teacher or a programme team). Written fresh from the held text alone (benchmark rule 6; Abbott, 15:42). -->
```yaml
- statement: qaa/public-policy-and-public-administration-2025/1.10
  forPractitioner: { text: "Teach strategic problem-solving and accountability so that the skills and attributes graduates gain will fit them for a wide range of jobs, including those outside policy and administration.", rewrite: light, force: will, status: drafted }
  forBeneficiary: { text: "The skills and qualities you build will prepare you for many kinds of work, whether or not you go on to a career in public policy or administration.", rewrite: full, force: will, status: drafted }
  author-agent-written: "Describe this as an expected outcome (will) of study in the subject: the skills gained prepare graduates for a wide range of occupations. It names no level or award; cite it as (QAA, 2025, Public Policy and Public Administration Subject Benchmark Statement, para 1.10). Do not claim it promises employment or that every graduate enters a policy career. Set it beside 1.23 and 2.14 and the FHEQ employment qualities qaa/fheq-2024/4.15.b9.1."
  author-agent-dialogue: "Raise it when a student doubts that the degree leads anywhere but government service. Tell them in plain words that the skills travel widely, and ask: \"Which of your skills would an employer outside government value most?\" Avoid promising a job or reading the paragraph aloud."
- statement: qaa/public-policy-and-public-administration-2025/1.11
  forPractitioner: { text: "Design learning so that students will critically evaluate policy and judge the effectiveness and productivity of the public sector, given its size and its growing reliance on non-profit and private delivery.", rewrite: light, force: will, status: drafted }
  forBeneficiary: { text: "You will be encouraged to judge policies critically and to weigh how well and how productively the public sector works.", rewrite: full, force: will, status: drafted }
  author-agent-written: "Describe this as a will-expectation on degrees in the subject: they encourage critical evaluation of policy and of public sector effectiveness and productivity. It holds for all awards in the subject without naming a level; cite it as (QAA, 2025, Public Policy and Public Administration Subject Benchmark Statement, para 1.11). Do not repeat the figure on public sector jobs as current fact without checking it. Set it beside the threshold items 4.5.b3 and 4.5.b5 and the FHEQ descriptor qaa/fheq-2024/4.15.b7."
  author-agent-dialogue: "Raise it when a student or teacher discusses what critical study of policy should look like. For a student, ask: \"When you judge a policy, how do you decide whether it worked and was good value?\" Avoid quoting the paragraph's statistic as settled and avoid long readings from the text."
- statement: qaa/public-policy-and-public-administration-2025/1.12
  forPractitioner: { text: "Embed EDI in both what you teach and how you teach it: let it shape the curriculum, pedagogy and assessment, and build a subject community where every student and member of staff belongs.", rewrite: light, force: should, status: drafted }
  forBeneficiary: { text: "not-applicable: a duty on the course and the people who design and run it, not a standard the student reaches", rewrite: full, force: should, status: drafted }
  author-agent-written: "Describe this as a should-duty on the course, not a student outcome: degrees in the subject observe, integrate and promote EDI in delivery and curriculum. It holds for every award in the subject and names no level; cite it as (QAA, 2025, Public Policy and Public Administration Subject Benchmark Statement, para 1.12). Do not present it as a legal requirement, and do not turn it into a learning outcome for students. Set it beside 1.14 and the shared theme record theme:edi."
  author-agent-dialogue: "Raise it with a programme team reviewing curriculum, teaching or assessment for inclusion. Use the practitioner framing and ask: \"Where in the course would a student from an under-represented group see their perspective taught as central?\" Do not put this duty to a student as something they must achieve, and do not read the paragraph out at length."
- statement: qaa/public-policy-and-public-administration-2025/1.14
  forPractitioner: { text: "Put EDI first in day-to-day practice: use inclusive language, choose teaching and assessment that address unequal power and invite diverse views and keep learning spaces inclusive.", rewrite: light, force: should, status: drafted }
  forBeneficiary: { text: "not-applicable: a duty on the course and the people who design and run it, not a standard the student reaches", rewrite: full, force: should, status: drafted }
  author-agent-written: "Describe this as a should-duty on staff practice and processes: EDI principles lead academic, pedagogical and administrative work in the subject. It names no level or award; cite it as (QAA, 2025, Public Policy and Public Administration Subject Benchmark Statement, para 1.14). Do not claim it prescribes particular methods, since it gives examples, not a checklist. Set it beside 1.12 and the assessment practice described in 3.11."
  author-agent-dialogue: "Raise it when a teacher or team plans language, teaching activities or assessment. Ask: \"Which of your assessment formats could put a student at a disadvantage, and what would you change?\" Keep it to staff; do not hand it to a student as their duty."
- statement: qaa/public-policy-and-public-administration-2025/1.17
  forPractitioner: { text: "Prepare students for the part graduates will play in shaping policy and services in areas like health, technology and crisis management, so that they design for full accessibility and participation, not only for legal compliance.", rewrite: light, force: will, status: drafted }
  forBeneficiary: { text: "You will play a central part in shaping policies and services, in areas such as health, technology and crisis management, and in making them open to everyone, beyond what the law demands.", rewrite: full, force: will, status: drafted }
  author-agent-written: "Describe this as a will-expectation about graduates' future role: shaping policies and services that are fully accessible and inclusive, beyond legal compliance. It sets no level or award; cite it as (QAA, 2025, Public Policy and Public Administration Subject Benchmark Statement, para 1.17). Do not present it as an assessed outcome or a guarantee of career roles. Set it beside the accessibility norms in 1.16 (a plain-present paragraph, Part E) and theme:accessibility."
  author-agent-dialogue: "Raise it when a student asks why accessibility matters in a policy course. Tell them plainly that they may design services others depend on, and ask: \"Who could be shut out by the service in your last case study, and how would you fix it?\" Avoid reducing accessibility to legal compliance."
- statement: qaa/public-policy-and-public-administration-2025/1.22
  forPractitioner: { text: "Make the link between content and enterprise explicit, and design for experienced practitioners as well as new entrants: they must leave with what they need to progress in their workplace.", rewrite: light, force: must, status: drafted }
  forBeneficiary: { text: "not-applicable: a duty on the course and the people who design and run it, not a standard the student reaches", rewrite: full, force: must, status: drafted }
  author-agent-written: "Describe this as a must-duty on degrees in the subject, especially Public Administration: clear links to enterprise and entrepreneurship, and provision that equips sector-experienced students to progress at work. It holds for undergraduate and postgraduate degrees alike; cite it as (QAA, 2025, Public Policy and Public Administration Subject Benchmark Statement, para 1.22, the first of two paragraphs so numbered). Do not claim it obliges a placement or a particular module. Set it beside 1.23, 3.10 and the FHEQ employment qualities qaa/fheq-2024/4.17.b8.1."
  author-agent-dialogue: "Raise it with a programme team designing for mixed cohorts of new and experienced students. Ask: \"Where does the course show an experienced public servant how to use what they learn to move on at work?\" Do not present this to a student as their duty."
- statement: qaa/public-policy-and-public-administration-2025/1.23
  forPractitioner: { text: "Give students repeated chances to name, reflect on and build their enterprise and employability skills, so that graduates will be able to explain them to current and future employers.", rewrite: light, force: will, status: drafted }
  forBeneficiary: { text: "You will be able to recognise the enterprise and employability skills you have built, reflect on them, keep developing them and explain them clearly to employers.", rewrite: full, force: will, status: drafted }
  author-agent-written: "Describe this as an outcome graduates will be able to show (are able to): recognising, reflecting on, developing and communicating their enterprise and employability skills. Read it at honours, FHEQ level 6 (FQHEIS level 10, spine:6), though the paragraph speaks of graduates generally; cite it as (QAA, 2025, Public Policy and Public Administration Subject Benchmark Statement, para 1.23). Do not claim it is a rung standard, since it sits in the context section. Set it beside the threshold items 4.5.b8 and 4.5.b9, the FHEQ descriptor qaa/fheq-2024/4.15.b9.1 and the Annex D cell qaa/fheq-2024/annex-d/transferable/r4/3rd."
  author-agent-dialogue: "Raise it when a student prepares an application, interview or placement, or a team plans employability work. Ask a student: \"Name a skill you built on the course and tell me how you would show an employer you have it.\" Avoid treating it as a graded standard and avoid long quotation."
- statement: qaa/public-policy-and-public-administration-2025/1.26
  forPractitioner: { text: "Treat generative AI as a curriculum matter, not only an integrity risk: align with what employers and workplaces need, adapt teaching, assessment and feedback and consider building GenAI into activities and authentic assessment.", rewrite: light, force: must, status: drafted }
  forBeneficiary: { text: "not-applicable: a duty on the course and the people who design and run it, not a standard the student reaches", rewrite: full, force: must, status: drafted }
  author-agent-written: "Describe this as a must-duty on degrees in the subject: they answer to what employers and workplaces need and to changing teaching, assessment and feedback in the face of generative AI. It names no level or award; cite it as (QAA, 2025, Public Policy and Public Administration Subject Benchmark Statement, para 1.26). Do not claim it bans or mandates any tool, or that it is a student outcome. Set it beside 1.27, 1.28, the assessment practice at 3.12 and theme:generative-ai."
  author-agent-dialogue: "Raise it with a team reviewing assessment design or its AI policy. Ask: \"Which of your assessments would still show a student's own judgement if they used GenAI openly?\" Do not turn this course duty into a rule for students."
- statement: qaa/public-policy-and-public-administration-2025/2.4
  forPractitioner: { text: "Cover multilevel governance and the interplay of structure, systems and agency, and make public and social value a visible thread, alongside public service motivation and ethos.", rewrite: light, force: will, status: drafted }
  forBeneficiary: { text: "Your course will give weight to public and social value, and you will look at how governance works across levels and how frontline staff experience the public sector.", rewrite: full, force: will, status: drafted }
  author-agent-written: "Describe this as a will-expectation on courses: they emphasise public and social value, alongside multilevel governance and the interplay of structure, systems and agency. It names no level or award; cite it as (QAA, 2025, Public Policy and Public Administration Subject Benchmark Statement, para 2.4). Do not present the topics named as a required syllabus. Set it beside the content paragraph 3.3 and the master's item 4.7.b11."
  author-agent-dialogue: "Raise it when a student or teacher asks what sets the subject apart from management or politics. Ask: \"How would you show the public value of a service, beyond its cost?\" Avoid listing the topics as a checklist."
- statement: qaa/public-policy-and-public-administration-2025/2.7
  forPractitioner: { text: "Plan each level so that it builds knowledge, expertise and experience towards the threshold subject-specific and generic skills by graduation, with credit earned across all learning and assessment, practical work included.", rewrite: light, force: will, status: drafted }
  forBeneficiary: { text: "As you move through each year of your honours degree, you will build the knowledge, expertise and experience that lead to the minimum standard by the end, completing all your learning and assessment, practical work included. With a second-class result or higher you would usually be ready for postgraduate study, though each university sets its own entry rules.", rewrite: full, force: will, status: drafted }
  author-agent-written: "Describe this as a will-expectation about progression through an honours degree at FHEQ level 6 (FQHEIS level 10): each level builds towards the threshold standards, normally through credit for all learning and assessment. Cite it as (QAA, 2025, Public Policy and Public Administration Subject Benchmark Statement, para 2.7). Do not claim it sets entry rules for postgraduate study, which it leaves to each provider. Set it beside the threshold list 4.5, the FHEQ honours descriptor qaa/fheq-2024/4.15.b1 and the progression threads in std:doc:qaa-fheq-2024-framework, SL4."
  author-agent-dialogue: "Raise it when a student asks how earlier years count or whether a 2:2 opens postgraduate study. Explain in plain words that each year builds towards the final standard, and ask: \"What did you learn last year that you now use without thinking?\" Avoid promising postgraduate entry, which each university decides."
- statement: qaa/public-policy-and-public-administration-2025/2.8
  forPractitioner: { text: "In joint or combined honours, make sure students will still attain the core subject-specific and generic skills of this statement, while the partner subject adds its own.", rewrite: light, force: will, status: drafted }
  forBeneficiary: { text: "If you study this subject as part of a joint or combined degree, you will gain its core subject and general skills and add others from your second subject.", rewrite: full, force: will, status: drafted }
  author-agent-written: "Describe this as a will-outcome for joint or combined honours students at FHEQ level 6 (FQHEIS level 10): they achieve the core of the subject's specific and generic skills. Cite it as (QAA, 2025, Public Policy and Public Administration Subject Benchmark Statement, para 2.8). Do not claim joint students must meet every item in 4.5, since the paragraph speaks of core elements. Set it beside the threshold list 4.5 and the FHEQ descriptor qaa/fheq-2024/4.15.b1."
  author-agent-dialogue: "Raise it when a joint honours student or course team asks how much of the subject must be covered. Ask: \"Which core skills of policy and administration does your half of the degree secure?\" Avoid suggesting that joint students are held to less than the core."
- statement: qaa/public-policy-and-public-administration-2025/2.14
  forPractitioner: { text: "Build skills for policymaking, management, leadership and change across sectors, and teach that services are delivered by multi-agency partnerships, so that graduates will have what they need to move between policy and administration roles.", rewrite: light, force: will, status: drafted }
  forBeneficiary: { text: "You will gain the skills to work as a policymaker, manager, leader or change agent in public, private or non-profit organisations, and you will learn how services are delivered by many agencies working together.", rewrite: full, force: will, status: drafted }
  author-agent-written: "Describe this as a will-expectation on graduates: the skills to work as policymakers, managers, leaders and change agents across sectors, with an understanding of multi-agency delivery. It names no level or award; cite it as (QAA, 2025, Public Policy and Public Administration Subject Benchmark Statement, para 2.14). Do not present it as a guarantee of a role or of seniority. Set it beside the master's items 4.7.b15 and 4.7.b16, the threshold item 4.5.b7 and the FHEQ employment qualities qaa/fheq-2024/4.15.b9.2."
  author-agent-dialogue: "Raise it when a student is weighing careers in the public, private or non-profit sector. Ask: \"Which agencies would need to work together to deliver the service you know best?\" Avoid implying that the degree alone makes someone a leader."
- statement: qaa/public-policy-and-public-administration-2025/2.19
  forPractitioner: { text: "Include students' views in routine monitoring and periodic review, use external reference points and consider reviewing EDI within the learning community as part of evaluation.", rewrite: light, force: will, status: drafted }
  forBeneficiary: { text: "not-applicable: a duty on the awarding body; students take part in review but do not reach it as a standard", rewrite: full, force: will, status: drafted }
  author-agent-written: "Describe this as a will-expectation on degree-awarding bodies: periodic review of the degree takes the student voice into account. It names no level or award; cite it as (QAA, 2025, Public Policy and Public Administration Subject Benchmark Statement, para 2.19). Do not claim it fixes a review cycle or method. Set it beside 2.20 and theme:edi."
  author-agent-dialogue: "Raise it with a programme team planning a periodic review. Ask: \"How will students' views reach the review panel, and what will change as a result?\" Do not present it to a student as an obligation."
- statement: qaa/public-policy-and-public-administration-2025/2.20
  forPractitioner: { text: "Bring external reviewers into periodic review to test proposed changes, confirm that threshold standards are achieved and check that the content fits the subject.", rewrite: light, force: will, status: drafted }
  forBeneficiary: { text: "not-applicable: a duty on the course and the people who design and run it, not a standard the student reaches", rewrite: full, force: will, status: drafted }
  author-agent-written: "Describe this as a will-expectation on higher education providers: external reviewers take part in periodic review to secure threshold standards and suitable content. It holds for all awards in the subject; cite it as (QAA, 2025, Public Policy and Public Administration Subject Benchmark Statement, para 2.20). Do not claim it describes the external examiner system, which 2.21 covers. Set it beside 2.19 and the threshold list 4.5."
  author-agent-dialogue: "Raise it when a team prepares for periodic review or chooses external reviewers. Ask: \"Who outside the institution will test whether your threshold standards hold?\" Keep it to staff and avoid long readings."
- statement: qaa/public-policy-and-public-administration-2025/2.23
  forPractitioner: { text: "Where professional or accrediting bodies evaluate the course, build their requirements into degree management from the start.", rewrite: light, force: will, status: drafted }
  forBeneficiary: { text: "not-applicable: a duty on the course and the people who design and run it, not a standard the student reaches", rewrite: full, force: will, status: drafted }
  author-agent-written: "Describe this as an obligation (will need to) on courses whose professional or vocational outcomes accrediting bodies evaluate: integrate those requirements into degree management. It names no level or award; cite it as (QAA, 2025, Public Policy and Public Administration Subject Benchmark Statement, para 2.23). Do not fold any body's requirements into the statement itself, since they are separate documents. Set it beside 1.25 and the bodies in SB5."
  author-agent-dialogue: "Raise it with a team seeking or holding accreditation. Ask: \"Where in your course management do the accrediting body's requirements get checked?\" Do not put this duty to a student."
- statement: qaa/public-policy-and-public-administration-2025/3.2
  forPractitioner: { text: "Use practice-based learning: real-world problems and action learning with reflection, plus focused placements in public and non-governmental organisations.", rewrite: light, force: will, status: drafted }
  forBeneficiary: { text: "You will usually learn through practice: working on real problems, reflecting on what you do and perhaps taking a placement in a public agency or a non-governmental organisation.", rewrite: full, force: will, status: drafted }
  author-agent-written: "Describe this as a will-expectation, qualified by typically, about how students learn in the subject: through practice-based learning, action learning, reflection and placements. It names no level or award; cite it as (QAA, 2025, Public Policy and Public Administration Subject Benchmark Statement, para 3.2). Do not claim it requires every student to take a placement. Set it beside the learning methods at 3.7 and the threshold items 4.5.b5 and 4.5.b9."
  author-agent-dialogue: "Raise it when a student asks how the course is taught or a team plans practice-based learning. Ask a student: \"Which real problem have you worked on so far, and what did reflecting on it teach you?\" Avoid presenting placements as guaranteed."
- statement: qaa/public-policy-and-public-administration-2025/3.3
  forPractitioner: { text: "Choose any sectors or institutions, but make sure students engage closely with governance and policy questions, apply theory across contexts from the individual to the global and study the public sector both conceptually and empirically, drawing on several of the listed subfields.", rewrite: light, force: will, status: drafted }
  forBeneficiary: { text: "You will study how governments and the public and voluntary sectors are designed and run, apply theories and principles to real questions of governance and policy in many settings and get to know several specialist areas of the field.", rewrite: full, force: will, status: drafted }
  author-agent-written: "Describe this as a will-expectation on the content of study: detailed engagement with governance and policy questions, applied across contexts, with the public sector studied conceptually and empirically. It names no level or award; cite it as (QAA, 2025, Public Policy and Public Administration Subject Benchmark Statement, para 3.3), and present the 40 subfields as a menu from which courses draw, not a core list. Do not claim any sector or institution is required. Set it beside the knowledge items 4.5.b1 and 4.6.b1 and the FHEQ descriptor qaa/fheq-2024/4.15.b1."
  author-agent-dialogue: "Raise it when a team designs or reviews the curriculum, or a student chooses options. Ask: \"Which subfields does your course cover, and how do they let you compare tiers of government?\" Avoid reading out the full list of subfields."
- statement: qaa/public-policy-and-public-administration-2025/3.6
  forPractitioner: { text: "Fit teaching methods to the content, outcomes and learners, build in sustainability, inclusion, accessibility and enterprise, use a mix of modes and do what you can to make digital learning inclusive for every student.", rewrite: light, force: will, status: drafted }
  forBeneficiary: { text: "not-applicable: a duty on the course and the people who design and run it, not a standard the student reaches", rewrite: full, force: will, status: drafted }
  author-agent-written: "Describe this as a will-expectation on providers: learning and teaching reflect each provider's approach and, as far as possible, secure digital inclusivity. It names no level or award; cite it as (QAA, 2025, Public Policy and Public Administration Subject Benchmark Statement, para 3.6). Do not claim it prescribes any mode of delivery. Set it beside 3.7, 1.14 and the themes theme:accessibility and theme:esd."
  author-agent-dialogue: "Raise it with a teacher or team planning blended, online or hybrid delivery. Ask: \"Which students might struggle to reach your digital materials, and what support do they get?\" Keep it as a staff duty."
- statement: qaa/public-policy-and-public-administration-2025/3.7
  forPractitioner: { text: "Offer a varied mix of settings and methods that build cognitive and life skills and enterprising responses to social challenges, drawing on lectures, seminars, case studies, simulations, placements, independent study, practitioner talks and fieldwork.", rewrite: light, force: will, status: drafted }
  forBeneficiary: { text: "You will learn in many ways, such as lectures, seminars, case studies, simulations, placements, guest talks and field trips, which together build your thinking, your life skills and your ideas for tackling social problems.", rewrite: full, force: will, status: drafted }
  author-agent-written: "Describe this as a will-expectation that students experience varied learning environments and methods, typically a combination drawn from the listed methods. It names no level or award; cite it as (QAA, 2025, Public Policy and Public Administration Subject Benchmark Statement, para 3.7). Do not present the list as compulsory. Set it beside 3.2, 3.6 and theme:enterprise."
  author-agent-dialogue: "Raise it when a student asks how they will be taught or a team reviews its mix of methods. Ask: \"Which way of learning has helped you most so far, and which have you not yet tried?\" Avoid reading the method list aloud."
- statement: qaa/public-policy-and-public-administration-2025/3.10
  forPractitioner: { text: "Align the assessment strategy with the curriculum and teaching, link each task to stated outcomes, use assessment for and as learning and let it show progression and build employability and professional skills.", rewrite: light, force: will, status: drafted }
  forBeneficiary: { text: "not-applicable: a duty on the course's assessment design; the student meets its effect", rewrite: full, force: will, status: drafted }
  author-agent-written: "Describe this as a will-expectation on each course's assessment strategy: it reflects the curriculum and aligns with teaching, linked to learning outcomes and progressive attainment. It names no level or award; cite it as (QAA, 2025, Public Policy and Public Administration Subject Benchmark Statement, para 3.10). Do not claim it prescribes assessment types, since 3.12 gives examples only. Set it beside 3.11, 3.12, 3.13 and theme:enterprise."
  author-agent-dialogue: "Raise it with a team mapping assessment to outcomes. Ask: \"Which outcome does each assessment test, and where does a student show progress from one level to the next?\" Keep it to staff; do not present it as a student's task."
- statement: qaa/public-policy-and-public-administration-2025/3.13
  forPractitioner: { text: "Give constructive, consistent and specific feedback on formative and summative work across the course, timed so that students can use it on later tasks and vary its form for a diverse cohort.", rewrite: light, force: will, status: drafted }
  forBeneficiary: { text: "You will get feedback that is constructive, consistent and specific on both practice and marked work throughout your studies, so that you can use it on your next tasks.", rewrite: full, force: will, status: drafted }
  author-agent-written: "Describe this as a will-expectation on the course: feedback is constructive, consistent and specific, given throughout study on formative and summative work so that students can feed it forward. It names no level or award; cite it as (QAA, 2025, Public Policy and Public Administration Subject Benchmark Statement, para 3.13). Do not claim it fixes turnaround times or formats. Set it beside the items on using feedback, 4.5.b14 and 4.6.b15, and theme:edi."
  author-agent-dialogue: "Raise it when a student is unsure what to do with feedback or a team reviews its feedback practice. Ask a student: \"What did your last piece of feedback tell you to do differently next time?\" Avoid suggesting that feedback must take one form."
- statement: qaa/public-policy-and-public-administration-2025/4.2
  forPractitioner: { text: "Decide how your institution evidences performance above threshold, and use Annex D of the 2024 Frameworks, the classification descriptions for honours at FHEQ level 6 and FQHEIS level 10, when setting class boundaries.", rewrite: light, force: should, status: drafted }
  forBeneficiary: { text: "not-applicable: a duty on the course and the people who design and run it, not a standard the student reaches", rewrite: full, force: should, status: drafted }
  author-agent-written: "Describe this as a should-duty on each provider: when judging achievement above the threshold, refer to the degree classification descriptions in Annex D. It holds for honours at FHEQ level 6 (FQHEIS level 10); cite it as (QAA, 2025, Public Policy and Public Administration Subject Benchmark Statement, para 4.2) and point to std:doc:qaa-fheq-2024-framework, Annex D (qaa/fheq-2024/annex-d/...). Do not claim the subject sets its own class descriptors, since it states only threshold and excellent levels. Set it beside 4.5, 4.6 and the classification bands in std:doc:qaa-fheq-2024-framework, SL6."
  author-agent-dialogue: "Raise it with a team or external examiner calibrating marks across classes. Ask: \"How do your marking criteria for a 2:1 relate to the Annex D description?\" Do not present classification rules to a student as this subject's own."
- statement: qaa/public-policy-and-public-administration-2025/4.3
  forPractitioner: { text: "If you write competence standards (Equality Act 2010) into a programme specification, you may draw on this statement and PSRB requirements, but follow the latest EHRC guidance and do not treat the threshold standards as competence standards.", rewrite: light, force: should, status: drafted }
  forBeneficiary: { text: "not-applicable: a duty on the course and the people who design and run it, not a standard the student reaches", rewrite: full, force: should, status: drafted }
  author-agent-written: "Describe this as a should-duty on providers that write competence standards: follow the latest guidance of the Equality and Human Rights Commission. It names no level; cite it as (QAA, 2025, Public Policy and Public Administration Subject Benchmark Statement, para 4.3). Do not call the threshold items in 4.5 competence standards. Set it beside 4.5 and theme:edi."
  author-agent-dialogue: "Raise it with a team drafting a programme specification that includes competence standards. Ask: \"Which of your requirements are competence standards in the legal sense, and have you checked them against the EHRC guidance?\" Keep it to staff."
- statement: qaa/public-policy-and-public-administration-2025/4.5.b1
  forPractitioner: { text: "At threshold, graduates show that they know the field's core concepts and theories and are aware of current evidence.", rewrite: light, force: threshold, status: drafted }
  forBeneficiary: { text: "To reach the minimum standard for your honours degree, you will show that you know the main concepts and theories of public policy and administration and are aware of current evidence.", rewrite: full, force: threshold, status: drafted }
  author-agent-written: "Describe this as part of the threshold standard for an honours degree in Public Policy or Public Administration, the least every graduate shows, at FHEQ level 6 (FQHEIS level 10, spine:6): key concepts, theories and current evidence. Cite it as (QAA, 2025, Public Policy and Public Administration Subject Benchmark Statement, para 4.5, item 1), and do not present it as a regulatory requirement, a competence standard (see 4.3) or a target for the higher classes. Set it beside the excellent-level item 4.6.b1, the FHEQ descriptor qaa/fheq-2024/4.15.b1 and the Annex D third-class cell qaa/fheq-2024/annex-d/knowledge/r2/3rd."
  author-agent-dialogue: "Raise it when a student or teacher asks what the minimum for an honours degree looks like in key concepts, theories and current evidence. Put it plainly, in the second person for a student, as something every graduate shows, and ask: \"Which two theories of the policy process could you explain and use on a current case?\" Avoid reading the statement aloud and avoid implying that meeting it earns more than a pass-level result."
- statement: qaa/public-policy-and-public-administration-2025/4.5.b2
  forPractitioner: { text: "At threshold, graduates show knowledge and understanding of present problems or new insights, much of it shaped by leading research or professional practice.", rewrite: light, force: threshold, status: drafted }
  forBeneficiary: { text: "To reach the minimum standard for your honours degree, you will know and understand today's problems and new thinking in the field, much of it drawn from leading research or practice.", rewrite: full, force: threshold, status: drafted }
  author-agent-written: "Describe this as part of the threshold standard for an honours degree in Public Policy or Public Administration, the least every graduate shows, at FHEQ level 6 (FQHEIS level 10, spine:6): current problems and new insights near the forefront. Cite it as (QAA, 2025, Public Policy and Public Administration Subject Benchmark Statement, para 4.5, item 2), and do not present it as a regulatory requirement, a competence standard (see 4.3) or a target for the higher classes. Set it beside the excellent-level item 4.6.b2, the FHEQ descriptor qaa/fheq-2024/4.15.b1 and the Annex D third-class cell qaa/fheq-2024/annex-d/knowledge/r1/3rd."
  author-agent-dialogue: "Raise it when a student or teacher asks what the minimum for an honours degree looks like in current problems and new insights near the forefront. Put it plainly, in the second person for a student, as something every graduate shows, and ask: \"What is one live problem in public services that recent research has changed your view of?\" Avoid reading the statement aloud and avoid implying that meeting it earns more than a pass-level result."
- statement: qaa/public-policy-and-public-administration-2025/4.5.b3
  forPractitioner: { text: "At threshold, graduates can build an argument that draws relevant information together and uses judgement.", rewrite: light, force: threshold, status: drafted }
  forBeneficiary: { text: "To reach the minimum standard for your honours degree, you will build an argument that brings together the relevant information and shows your own judgement.", rewrite: full, force: threshold, status: drafted }
  author-agent-written: "Describe this as part of the threshold standard for an honours degree in Public Policy or Public Administration, the least every graduate shows, at FHEQ level 6 (FQHEIS level 10, spine:6): building an argument with judgement. Cite it as (QAA, 2025, Public Policy and Public Administration Subject Benchmark Statement, para 4.5, item 3), and do not present it as a regulatory requirement, a competence standard (see 4.3) or a target for the higher classes. Set it beside the excellent-level item 4.6.b5, the FHEQ descriptor qaa/fheq-2024/4.15.b3.1 and the Annex D third-class cell qaa/fheq-2024/annex-d/cognitive/r2/3rd."
  author-agent-dialogue: "Raise it when a student or teacher asks what the minimum for an honours degree looks like in building an argument with judgement. Put it plainly, in the second person for a student, as something every graduate shows, and ask: \"What is the strongest objection to your argument, and how does your evidence answer it?\" Avoid reading the statement aloud and avoid implying that meeting it earns more than a pass-level result."
- statement: qaa/public-policy-and-public-administration-2025/4.5.b4
  forPractitioner: { text: "At threshold, graduates can handle complex issues methodically and inventively and judge soundly when information is missing.", rewrite: light, force: threshold, status: drafted }
  forBeneficiary: { text: "To reach the minimum standard for your honours degree, you will handle complex issues methodically and inventively, and reach sound judgements when some of the information is missing.", rewrite: full, force: threshold, status: drafted }
  author-agent-written: "Describe this as part of the threshold standard for an honours degree in Public Policy or Public Administration, the least every graduate shows, at FHEQ level 6 (FQHEIS level 10, spine:6): complex issues and judgement with incomplete data. Cite it as (QAA, 2025, Public Policy and Public Administration Subject Benchmark Statement, para 4.5, item 4), and do not present it as a regulatory requirement, a competence standard (see 4.3) or a target for the higher classes. Set it beside the excellent-level item 4.6.b7, the FHEQ descriptor qaa/fheq-2024/4.15.b7 and the Annex D third-class cell qaa/fheq-2024/annex-d/cognitive/r3/3rd."
  author-agent-dialogue: "Raise it when a student or teacher asks what the minimum for an honours degree looks like in complex issues and judgement with incomplete data. Put it plainly, in the second person for a student, as something every graduate shows, and ask: \"When you had to decide without all the facts, how did you make the gap visible in your reasoning?\" Avoid reading the statement aloud and avoid implying that meeting it earns more than a pass-level result."
- statement: qaa/public-policy-and-public-administration-2025/4.5.b5
  forPractitioner: { text: "At threshold, graduates can find, examine and resolve problems in practical and theoretical settings.", rewrite: light, force: threshold, status: drafted }
  forBeneficiary: { text: "To reach the minimum standard for your honours degree, you will spot, look into and resolve problems, in practice as well as in theory.", rewrite: full, force: threshold, status: drafted }
  author-agent-written: "Describe this as part of the threshold standard for an honours degree in Public Policy or Public Administration, the least every graduate shows, at FHEQ level 6 (FQHEIS level 10, spine:6): problems in practical and theoretical contexts. Cite it as (QAA, 2025, Public Policy and Public Administration Subject Benchmark Statement, para 4.5, item 5), and do not present it as a regulatory requirement, a competence standard (see 4.3) or a target for the higher classes. Set it beside the excellent-level item 4.6.b8, the FHEQ descriptor qaa/fheq-2024/4.15.b6 and the Annex D third-class cell qaa/fheq-2024/annex-d/cognitive/r3/3rd."
  author-agent-dialogue: "Raise it when a student or teacher asks what the minimum for an honours degree looks like in problems in practical and theoretical contexts. Put it plainly, in the second person for a student, as something every graduate shows, and ask: \"Can you take a problem from a placement or case and show how theory helped you solve it?\" Avoid reading the statement aloud and avoid implying that meeting it earns more than a pass-level result."
- statement: qaa/public-policy-and-public-administration-2025/4.5.b6
  forPractitioner: { text: "At threshold, graduates can assess and use methods for gathering, analysing and presenting relevant data.", rewrite: light, force: threshold, status: drafted }
  forBeneficiary: { text: "To reach the minimum standard for your honours degree, you will choose and use good ways to gather, analyse and present the data a question needs.", rewrite: full, force: threshold, status: drafted }
  author-agent-written: "Describe this as part of the threshold standard for an honours degree in Public Policy or Public Administration, the least every graduate shows, at FHEQ level 6 (FQHEIS level 10, spine:6): approaches to collecting, analysing and presenting data. Cite it as (QAA, 2025, Public Policy and Public Administration Subject Benchmark Statement, para 4.5, item 6), and do not present it as a regulatory requirement, a competence standard (see 4.3) or a target for the higher classes. Set it beside the excellent-level item 4.6.b9, the FHEQ descriptor qaa/fheq-2024/4.15.b2 and the Annex D third-class cell qaa/fheq-2024/annex-d/practical/r4/3rd."
  author-agent-dialogue: "Raise it when a student or teacher asks what the minimum for an honours degree looks like in approaches to collecting, analysing and presenting data. Put it plainly, in the second person for a student, as something every graduate shows, and ask: \"Why did you choose that method of collecting data, and what would another method have shown?\" Avoid reading the statement aloud and avoid implying that meeting it earns more than a pass-level result."
- statement: qaa/public-policy-and-public-administration-2025/4.5.b7
  forPractitioner: { text: "At threshold, graduates work with others towards shared aims, for example in group tasks, projects and presentations.", rewrite: light, force: threshold, status: drafted }
  forBeneficiary: { text: "To reach the minimum standard for your honours degree, you will work with others towards shared aims, for example in group work, projects and presentations.", rewrite: full, force: threshold, status: drafted }
  author-agent-written: "Describe this as part of the threshold standard for an honours degree in Public Policy or Public Administration, the least every graduate shows, at FHEQ level 6 (FQHEIS level 10, spine:6): collaboration towards shared goals. Cite it as (QAA, 2025, Public Policy and Public Administration Subject Benchmark Statement, para 4.5, item 7), and do not present it as a regulatory requirement, a competence standard (see 4.3) or a target for the higher classes. Set it beside the excellent-level item 4.6.b3, the FHEQ descriptor qaa/fheq-2024/4.15.b9.1 and the Annex D third-class cell qaa/fheq-2024/annex-d/transferable/r2/3rd."
  author-agent-dialogue: "Raise it when a student or teacher asks what the minimum for an honours degree looks like in collaboration towards shared goals. Put it plainly, in the second person for a student, as something every graduate shows, and ask: \"What did you contribute to your last group task, and what would you do differently?\" Avoid reading the statement aloud and avoid implying that meeting it earns more than a pass-level result."
- statement: qaa/public-policy-and-public-administration-2025/4.5.b8
  forPractitioner: { text: "At threshold, graduates communicate in formats that suit the context and different audiences.", rewrite: light, force: threshold, status: drafted }
  forBeneficiary: { text: "To reach the minimum standard for your honours degree, you will communicate in forms that suit the setting and the people you are addressing.", rewrite: full, force: threshold, status: drafted }
  author-agent-written: "Describe this as part of the threshold standard for an honours degree in Public Policy or Public Administration, the least every graduate shows, at FHEQ level 6 (FQHEIS level 10, spine:6): communication in varied formats and for varied audiences. Cite it as (QAA, 2025, Public Policy and Public Administration Subject Benchmark Statement, para 4.5, item 8), and do not present it as a regulatory requirement, a competence standard (see 4.3) or a target for the higher classes. Set it beside the excellent-level item 4.6.b4, the FHEQ descriptor qaa/fheq-2024/4.15.b8 and the Annex D third-class cell qaa/fheq-2024/annex-d/transferable/r1/3rd."
  author-agent-dialogue: "Raise it when a student or teacher asks what the minimum for an honours degree looks like in communication in varied formats and for varied audiences. Put it plainly, in the second person for a student, as something every graduate shows, and ask: \"How would you explain the same policy finding to a minister and to a service user?\" Avoid reading the statement aloud and avoid implying that meeting it earns more than a pass-level result."
- statement: qaa/public-policy-and-public-administration-2025/4.5.b9
  forPractitioner: { text: "At threshold, graduates reflect on their own learning.", rewrite: light, force: threshold, status: drafted }
  forBeneficiary: { text: "To reach the minimum standard for your honours degree, you will think about how you are learning and what that tells you.", rewrite: full, force: threshold, status: drafted }
  author-agent-written: "Describe this as part of the threshold standard for an honours degree in Public Policy or Public Administration, the least every graduate shows, at FHEQ level 6 (FQHEIS level 10, spine:6): reflection on own learning. Cite it as (QAA, 2025, Public Policy and Public Administration Subject Benchmark Statement, para 4.5, item 9), and do not present it as a regulatory requirement, a competence standard (see 4.3) or a target for the higher classes. Set it beside the excellent-level item 4.6.b6, the FHEQ descriptor qaa/fheq-2024/4.15.b5 and the Annex D third-class cell qaa/fheq-2024/annex-d/transferable/r5/3rd."
  author-agent-dialogue: "Raise it when a student or teacher asks what the minimum for an honours degree looks like in reflection on own learning. Put it plainly, in the second person for a student, as something every graduate shows, and ask: \"What have you learned about how you learn best?\" Avoid reading the statement aloud and avoid implying that meeting it earns more than a pass-level result."
- statement: qaa/public-policy-and-public-administration-2025/4.5.b10
  forPractitioner: { text: "At threshold, graduates manage their own learning and projects well, alone and with others.", rewrite: light, force: threshold, status: drafted }
  forBeneficiary: { text: "To reach the minimum standard for your honours degree, you will manage your own learning and projects well, on your own and with others.", rewrite: full, force: threshold, status: drafted }
  author-agent-written: "Describe this as part of the threshold standard for an honours degree in Public Policy or Public Administration, the least every graduate shows, at FHEQ level 6 (FQHEIS level 10, spine:6): managing own learning and projects. Cite it as (QAA, 2025, Public Policy and Public Administration Subject Benchmark Statement, para 4.5, item 10), and do not present it as a regulatory requirement, a competence standard (see 4.3) or a target for the higher classes. Set it beside the excellent-level item 4.6.b10, the FHEQ descriptor qaa/fheq-2024/4.15.b5 and 4.15.b6 and the Annex D third-class cell qaa/fheq-2024/annex-d/transferable/r3/3rd."
  author-agent-dialogue: "Raise it when a student or teacher asks what the minimum for an honours degree looks like in managing own learning and projects. Put it plainly, in the second person for a student, as something every graduate shows, and ask: \"How do you plan a project so that it is finished on time?\" Avoid reading the statement aloud and avoid implying that meeting it earns more than a pass-level result."
- statement: qaa/public-policy-and-public-administration-2025/4.5.b11
  forPractitioner: { text: "At threshold, graduates can understand and apply the principles of research ethics.", rewrite: light, force: threshold, status: drafted }
  forBeneficiary: { text: "To reach the minimum standard for your honours degree, you will understand the principles of ethical research and put them into practice.", rewrite: full, force: threshold, status: drafted }
  author-agent-written: "Describe this as part of the threshold standard for an honours degree in Public Policy or Public Administration, the least every graduate shows, at FHEQ level 6 (FQHEIS level 10, spine:6): principles of ethical research. Cite it as (QAA, 2025, Public Policy and Public Administration Subject Benchmark Statement, para 4.5, item 11), and do not present it as a regulatory requirement, a competence standard (see 4.3) or a target for the higher classes. Set it beside the excellent-level item 4.6.b11, the FHEQ descriptor qaa/fheq-2024/4.15.b2 and the Annex D third-class cell qaa/fheq-2024/annex-d/professional/r2/3rd-1st."
  author-agent-dialogue: "Raise it when a student or teacher asks what the minimum for an honours degree looks like in principles of ethical research. Put it plainly, in the second person for a student, as something every graduate shows, and ask: \"What ethical risks did your last piece of research raise, and how did you handle them?\" Avoid reading the statement aloud and avoid implying that meeting it earns more than a pass-level result."
- statement: qaa/public-policy-and-public-administration-2025/4.5.b12
  forPractitioner: { text: "At threshold, graduates organise and use evidence, data and information drawn from varied primary and secondary sources.", rewrite: light, force: threshold, status: drafted }
  forBeneficiary: { text: "To reach the minimum standard for your honours degree, you will organise and use evidence, data and information from many kinds of original and secondary sources.", rewrite: full, force: threshold, status: drafted }
  author-agent-written: "Describe this as part of the threshold standard for an honours degree in Public Policy or Public Administration, the least every graduate shows, at FHEQ level 6 (FQHEIS level 10, spine:6): organising and using evidence from primary and secondary sources. Cite it as (QAA, 2025, Public Policy and Public Administration Subject Benchmark Statement, para 4.5, item 12), and do not present it as a regulatory requirement, a competence standard (see 4.3) or a target for the higher classes. Set it beside the excellent-level item 4.6.b12, the FHEQ descriptor qaa/fheq-2024/4.15.b5 and the Annex D third-class cell qaa/fheq-2024/annex-d/cognitive/r1/3rd."
  author-agent-dialogue: "Raise it when a student or teacher asks what the minimum for an honours degree looks like in organising and using evidence from primary and secondary sources. Put it plainly, in the second person for a student, as something every graduate shows, and ask: \"Which primary source did you use most recently, and how did it change your argument?\" Avoid reading the statement aloud and avoid implying that meeting it earns more than a pass-level result."
- statement: qaa/public-policy-and-public-administration-2025/4.5.b13
  forPractitioner: { text: "At threshold, graduates can see why personal integrity matters and recognise the ethical effects that decisions may have.", rewrite: light, force: threshold, status: drafted }
  forBeneficiary: { text: "To reach the minimum standard for your honours degree, you will understand why personal integrity matters and be aware of the ethical consequences decisions can have.", rewrite: full, force: threshold, status: drafted }
  author-agent-written: "Describe this as part of the threshold standard for an honours degree in Public Policy or Public Administration, the least every graduate shows, at FHEQ level 6 (FQHEIS level 10, spine:6): personal integrity and the ethics of decisions. Cite it as (QAA, 2025, Public Policy and Public Administration Subject Benchmark Statement, para 4.5, item 13), and do not present it as a regulatory requirement, a competence standard (see 4.3) or a target for the higher classes. Set it beside the excellent-level item 4.6.b13, the FHEQ descriptor qaa/fheq-2024/4.15.b9.2 and the Annex D third-class cell qaa/fheq-2024/annex-d/professional/r2/3rd-1st."
  author-agent-dialogue: "Raise it when a student or teacher asks what the minimum for an honours degree looks like in personal integrity and the ethics of decisions. Put it plainly, in the second person for a student, as something every graduate shows, and ask: \"Think of a public decision you studied: who bore its ethical costs, and was that fair?\" Avoid reading the statement aloud and avoid implying that meeting it earns more than a pass-level result."
- statement: qaa/public-policy-and-public-administration-2025/4.5.b14
  forPractitioner: { text: "At threshold, graduates understand and act on constructive feedback.", rewrite: light, force: threshold, status: drafted }
  forBeneficiary: { text: "To reach the minimum standard for your honours degree, you will understand constructive feedback and act on it.", rewrite: full, force: threshold, status: drafted }
  author-agent-written: "Describe this as part of the threshold standard for an honours degree in Public Policy or Public Administration, the least every graduate shows, at FHEQ level 6 (FQHEIS level 10, spine:6): using constructive feedback. Cite it as (QAA, 2025, Public Policy and Public Administration Subject Benchmark Statement, para 4.5, item 14), and do not present it as a regulatory requirement, a competence standard (see 4.3) or a target for the higher classes. Set it beside the excellent-level item 4.6.b15, the FHEQ descriptor qaa/fheq-2024/4.15.b5 and the Annex D third-class cell qaa/fheq-2024/annex-d/transferable/r3/3rd."
  author-agent-dialogue: "Raise it when a student or teacher asks what the minimum for an honours degree looks like in using constructive feedback. Put it plainly, in the second person for a student, as something every graduate shows, and ask: \"Which piece of feedback have you acted on, and what changed as a result?\" Avoid reading the statement aloud and avoid implying that meeting it earns more than a pass-level result."
- statement: qaa/public-policy-and-public-administration-2025/4.5.b15
  forPractitioner: { text: "At threshold, graduates can choose and use suitable aids and software for communicating, handling information and analysing data.", rewrite: light, force: threshold, status: drafted }
  forBeneficiary: { text: "To reach the minimum standard for your honours degree, you will choose and use the right tools and software for communicating, handling information and analysing data.", rewrite: full, force: threshold, status: drafted }
  author-agent-written: "Describe this as part of the threshold standard for an honours degree in Public Policy or Public Administration, the least every graduate shows, at FHEQ level 6 (FQHEIS level 10, spine:6): communication, information and data tools and software. Cite it as (QAA, 2025, Public Policy and Public Administration Subject Benchmark Statement, para 4.5, item 15), and do not present it as a regulatory requirement, a competence standard (see 4.3) or a target for the higher classes. Set it beside the excellent-level item 4.6.b16, the FHEQ descriptor qaa/fheq-2024/4.15.b8 and the Annex D third-class cell qaa/fheq-2024/annex-d/transferable/r1/3rd."
  author-agent-dialogue: "Raise it when a student or teacher asks what the minimum for an honours degree looks like in communication, information and data tools and software. Put it plainly, in the second person for a student, as something every graduate shows, and ask: \"Which software do you use for data analysis, and what can you not yet do with it?\" Avoid reading the statement aloud and avoid implying that meeting it earns more than a pass-level result."
- statement: qaa/public-policy-and-public-administration-2025/4.6.b1
  forPractitioner: { text: "At the excellent level, graduates will show consistent, detailed knowledge of the core concepts and theories and awareness of current evidence and debates.", rewrite: light, force: will, status: drafted }
  forBeneficiary: { text: "At an excellent level, you will show detailed, consistent knowledge of the main concepts and theories and a good grasp of current evidence and debates.", rewrite: full, force: will, status: drafted }
  author-agent-written: "Describe this as the excellent level of attainment for an honours degree in Public Policy or Public Administration at FHEQ level 6 (FQHEIS level 10, spine:6): consistent, detailed knowledge of concepts, theories, evidence and issues; it is what the strongest graduates are expected to show, not a minimum. Cite it as (QAA, 2025, Public Policy and Public Administration Subject Benchmark Statement, para 4.6, item 1), and do not treat it as a pass requirement or as a first-class rule, since classification is left to Annex D (4.2). Set it beside the threshold item 4.5.b1, the FHEQ descriptor qaa/fheq-2024/4.15.b1 and the Annex D first-class cell qaa/fheq-2024/annex-d/knowledge/r2/1st."
  author-agent-dialogue: "Raise it when a student aims high or a teaching team calibrates top-band work on consistent, detailed knowledge of concepts, theories, evidence and issues. Frame it for a student as what outstanding work looks like, never as the minimum, and ask: \"Where could you go beyond the textbook account of a theory and show where it breaks down?\" Do not quote the statement at length, and point a student worried about passing to 4.5.b1 instead."
- statement: qaa/public-policy-and-public-administration-2025/4.6.b2
  forPractitioner: { text: "At the excellent level, graduates will show systematic knowledge and a critical awareness of current problems or new insights, much of it from leading research or practice.", rewrite: light, force: will, status: drafted }
  forBeneficiary: { text: "At an excellent level, you will show a systematic and critical grasp of today's problems and new thinking in the field, much of it from leading research or practice.", rewrite: full, force: will, status: drafted }
  author-agent-written: "Describe this as the excellent level of attainment for an honours degree in Public Policy or Public Administration at FHEQ level 6 (FQHEIS level 10, spine:6): systematic, critical awareness of current problems and insights; it is what the strongest graduates are expected to show, not a minimum. Cite it as (QAA, 2025, Public Policy and Public Administration Subject Benchmark Statement, para 4.6, item 2), and do not treat it as a pass requirement or as a first-class rule, since classification is left to Annex D (4.2). Set it beside the threshold item 4.5.b2, the FHEQ descriptor qaa/fheq-2024/4.15.b1 and the Annex D first-class cell qaa/fheq-2024/annex-d/knowledge/r1/1st."
  author-agent-dialogue: "Raise it when a student aims high or a teaching team calibrates top-band work on systematic, critical awareness of current problems and insights. Frame it for a student as what outstanding work looks like, never as the minimum, and ask: \"Which recent study would you challenge, and on what grounds?\" Do not quote the statement at length, and point a student worried about passing to 4.5.b2 instead."
- statement: qaa/public-policy-and-public-administration-2025/4.6.b3
  forPractitioner: { text: "At the excellent level, graduates will collaborate skilfully with others towards shared aims, for instance in group work, projects and presentations.", rewrite: light, force: will, status: drafted }
  forBeneficiary: { text: "At an excellent level, you will work with others skilfully to reach shared aims, for example in group projects and presentations.", rewrite: full, force: will, status: drafted }
  author-agent-written: "Describe this as the excellent level of attainment for an honours degree in Public Policy or Public Administration at FHEQ level 6 (FQHEIS level 10, spine:6): sophisticated collaboration towards shared goals; it is what the strongest graduates are expected to show, not a minimum. Cite it as (QAA, 2025, Public Policy and Public Administration Subject Benchmark Statement, para 4.6, item 3), and do not treat it as a pass requirement or as a first-class rule, since classification is left to Annex D (4.2). Set it beside the threshold item 4.5.b7, the FHEQ descriptor qaa/fheq-2024/4.15.b9.1 and the Annex D first-class cell qaa/fheq-2024/annex-d/transferable/r2/1st."
  author-agent-dialogue: "Raise it when a student aims high or a teaching team calibrates top-band work on sophisticated collaboration towards shared goals. Frame it for a student as what outstanding work looks like, never as the minimum, and ask: \"How did you help a group reach a goal it might have missed without you?\" Do not quote the statement at length, and point a student worried about passing to 4.5.b7 instead."
- statement: qaa/public-policy-and-public-administration-2025/4.6.b4
  forPractitioner: { text: "At the excellent level, graduates will communicate with developed skill in formats suited to the context and the audience.", rewrite: light, force: will, status: drafted }
  forBeneficiary: { text: "At an excellent level, you will communicate with real skill in forms that fit the setting and the people you are addressing.", rewrite: full, force: will, status: drafted }
  author-agent-written: "Describe this as the excellent level of attainment for an honours degree in Public Policy or Public Administration at FHEQ level 6 (FQHEIS level 10, spine:6): developed communication in varied formats and for varied audiences; it is what the strongest graduates are expected to show, not a minimum. Cite it as (QAA, 2025, Public Policy and Public Administration Subject Benchmark Statement, para 4.6, item 4), and do not treat it as a pass requirement or as a first-class rule, since classification is left to Annex D (4.2). Set it beside the threshold item 4.5.b8, the FHEQ descriptor qaa/fheq-2024/4.15.b8 and the Annex D first-class cell qaa/fheq-2024/annex-d/transferable/r1/1st."
  author-agent-dialogue: "Raise it when a student aims high or a teaching team calibrates top-band work on developed communication in varied formats and for varied audiences. Frame it for a student as what outstanding work looks like, never as the minimum, and ask: \"How did you adapt your last piece of work for an audience outside the university?\" Do not quote the statement at length, and point a student worried about passing to 4.5.b8 instead."
- statement: qaa/public-policy-and-public-administration-2025/4.6.b5
  forPractitioner: { text: "At the excellent level, graduates will show a strong capacity to build reasoned arguments that draw information together and judge it critically.", rewrite: light, force: will, status: drafted }
  forBeneficiary: { text: "At an excellent level, you will build strong, well-reasoned arguments that pull the relevant information together and weigh it critically.", rewrite: full, force: will, status: drafted }
  author-agent-written: "Describe this as the excellent level of attainment for an honours degree in Public Policy or Public Administration at FHEQ level 6 (FQHEIS level 10, spine:6): strong reasoned argument with critical judgement; it is what the strongest graduates are expected to show, not a minimum. Cite it as (QAA, 2025, Public Policy and Public Administration Subject Benchmark Statement, para 4.6, item 5), and do not treat it as a pass requirement or as a first-class rule, since classification is left to Annex D (4.2). Set it beside the threshold item 4.5.b3, the FHEQ descriptor qaa/fheq-2024/4.15.b3.1 and the Annex D first-class cell qaa/fheq-2024/annex-d/cognitive/r2/1st."
  author-agent-dialogue: "Raise it when a student aims high or a teaching team calibrates top-band work on strong reasoned argument with critical judgement. Frame it for a student as what outstanding work looks like, never as the minimum, and ask: \"Where in your argument did you weigh competing evidence, and why did one side win?\" Do not quote the statement at length, and point a student worried about passing to 4.5.b3 instead."
- statement: qaa/public-policy-and-public-administration-2025/4.6.b6
  forPractitioner: { text: "At the excellent level, graduates will show a developed capacity to reflect critically on how they learn.", rewrite: light, force: will, status: drafted }
  forBeneficiary: { text: "At an excellent level, you will reflect critically and in depth on your own learning.", rewrite: full, force: will, status: drafted }
  author-agent-written: "Describe this as the excellent level of attainment for an honours degree in Public Policy or Public Administration at FHEQ level 6 (FQHEIS level 10, spine:6): critical reflection on own learning; it is what the strongest graduates are expected to show, not a minimum. Cite it as (QAA, 2025, Public Policy and Public Administration Subject Benchmark Statement, para 4.6, item 6), and do not treat it as a pass requirement or as a first-class rule, since classification is left to Annex D (4.2). Set it beside the threshold item 4.5.b9, the FHEQ descriptor qaa/fheq-2024/4.15.b5 and the Annex D first-class cell qaa/fheq-2024/annex-d/transferable/r5/1st."
  author-agent-dialogue: "Raise it when a student aims high or a teaching team calibrates top-band work on critical reflection on own learning. Frame it for a student as what outstanding work looks like, never as the minimum, and ask: \"What have you changed in how you study because of your own reflection?\" Do not quote the statement at length, and point a student worried about passing to 4.5.b9 instead."
- statement: qaa/public-policy-and-public-administration-2025/4.6.b7
  forPractitioner: { text: "At the excellent level, graduates will handle complex issues effectively, methodically and inventively, judging soundly when information is incomplete.", rewrite: light, force: will, status: drafted }
  forBeneficiary: { text: "At an excellent level, you will handle complex issues effectively, methodically and creatively, and make sound judgements when information is missing.", rewrite: full, force: will, status: drafted }
  author-agent-written: "Describe this as the excellent level of attainment for an honours degree in Public Policy or Public Administration at FHEQ level 6 (FQHEIS level 10, spine:6): effective handling of complex issues with incomplete data; it is what the strongest graduates are expected to show, not a minimum. Cite it as (QAA, 2025, Public Policy and Public Administration Subject Benchmark Statement, para 4.6, item 7), and do not treat it as a pass requirement or as a first-class rule, since classification is left to Annex D (4.2). Set it beside the threshold item 4.5.b4, the FHEQ descriptor qaa/fheq-2024/4.15.b7 and the Annex D first-class cell qaa/fheq-2024/annex-d/cognitive/r3/1st."
  author-agent-dialogue: "Raise it when a student aims high or a teaching team calibrates top-band work on effective handling of complex issues with incomplete data. Frame it for a student as what outstanding work looks like, never as the minimum, and ask: \"How did you test the judgement you reached on a complex case with gaps in the data?\" Do not quote the statement at length, and point a student worried about passing to 4.5.b4 instead."
- statement: qaa/public-policy-and-public-administration-2025/4.6.b8
  forPractitioner: { text: "At the excellent level, graduates will find, examine and resolve problems with confidence, thinking creatively in practice and theory.", rewrite: light, force: will, status: drafted }
  forBeneficiary: { text: "At an excellent level, you will find, look into and solve problems with confidence, thinking creatively in practice and in theory.", rewrite: full, force: will, status: drafted }
  author-agent-written: "Describe this as the excellent level of attainment for an honours degree in Public Policy or Public Administration at FHEQ level 6 (FQHEIS level 10, spine:6): confident, creative problem-solving; it is what the strongest graduates are expected to show, not a minimum. Cite it as (QAA, 2025, Public Policy and Public Administration Subject Benchmark Statement, para 4.6, item 8), and do not treat it as a pass requirement or as a first-class rule, since classification is left to Annex D (4.2). Set it beside the threshold item 4.5.b5, the FHEQ descriptor qaa/fheq-2024/4.15.b6 and the Annex D first-class cell qaa/fheq-2024/annex-d/cognitive/r3/1st."
  author-agent-dialogue: "Raise it when a student aims high or a teaching team calibrates top-band work on confident, creative problem-solving. Frame it for a student as what outstanding work looks like, never as the minimum, and ask: \"What creative option did you find that others had not considered?\" Do not quote the statement at length, and point a student worried about passing to 4.5.b5 instead."
- statement: qaa/public-policy-and-public-administration-2025/4.6.b9
  forPractitioner: { text: "At the excellent level, graduates will show an excellent capacity to assess and use methods for gathering, analysing and presenting data.", rewrite: light, force: will, status: drafted }
  forBeneficiary: { text: "At an excellent level, you will judge and use methods for gathering, analysing and presenting data to an excellent standard.", rewrite: full, force: will, status: drafted }
  author-agent-written: "Describe this as the excellent level of attainment for an honours degree in Public Policy or Public Administration at FHEQ level 6 (FQHEIS level 10, spine:6): excellent judgement of data approaches; it is what the strongest graduates are expected to show, not a minimum. Cite it as (QAA, 2025, Public Policy and Public Administration Subject Benchmark Statement, para 4.6, item 9), and do not treat it as a pass requirement or as a first-class rule, since classification is left to Annex D (4.2). Set it beside the threshold item 4.5.b6, the FHEQ descriptor qaa/fheq-2024/4.15.b2 and the Annex D first-class cell qaa/fheq-2024/annex-d/practical/r4/1st."
  author-agent-dialogue: "Raise it when a student aims high or a teaching team calibrates top-band work on excellent judgement of data approaches. Frame it for a student as what outstanding work looks like, never as the minimum, and ask: \"Could you defend your choice of data method to a sceptical expert?\" Do not quote the statement at length, and point a student worried about passing to 4.5.b6 instead."
- statement: qaa/public-policy-and-public-administration-2025/4.6.b10
  forPractitioner: { text: "At the excellent level, graduates will manage their learning and projects effectively, on time and critically, alone and with others.", rewrite: light, force: will, status: drafted }
  forBeneficiary: { text: "At an excellent level, you will manage your learning and projects well, on time and with a critical eye, on your own and with others.", rewrite: full, force: will, status: drafted }
  author-agent-written: "Describe this as the excellent level of attainment for an honours degree in Public Policy or Public Administration at FHEQ level 6 (FQHEIS level 10, spine:6): timely, critical management of own learning and projects; it is what the strongest graduates are expected to show, not a minimum. Cite it as (QAA, 2025, Public Policy and Public Administration Subject Benchmark Statement, para 4.6, item 10), and do not treat it as a pass requirement or as a first-class rule, since classification is left to Annex D (4.2). Set it beside the threshold item 4.5.b10, the FHEQ descriptor qaa/fheq-2024/4.15.b5 and 4.15.b6 and the Annex D first-class cell qaa/fheq-2024/annex-d/transferable/r3/1st."
  author-agent-dialogue: "Raise it when a student aims high or a teaching team calibrates top-band work on timely, critical management of own learning and projects. Frame it for a student as what outstanding work looks like, never as the minimum, and ask: \"How do you check that a project is still asking the right question as it goes?\" Do not quote the statement at length, and point a student worried about passing to 4.5.b10 instead."
- statement: qaa/public-policy-and-public-administration-2025/4.6.b11
  forPractitioner: { text: "At the excellent level, graduates will understand and apply research ethics with clarity.", rewrite: light, force: will, status: drafted }
  forBeneficiary: { text: "At an excellent level, you will understand research ethics clearly and apply them with care.", rewrite: full, force: will, status: drafted }
  author-agent-written: "Describe this as the excellent level of attainment for an honours degree in Public Policy or Public Administration at FHEQ level 6 (FQHEIS level 10, spine:6): clear grasp and use of research ethics; it is what the strongest graduates are expected to show, not a minimum. Cite it as (QAA, 2025, Public Policy and Public Administration Subject Benchmark Statement, para 4.6, item 11), and do not treat it as a pass requirement or as a first-class rule, since classification is left to Annex D (4.2). Set it beside the threshold item 4.5.b11, the FHEQ descriptor qaa/fheq-2024/4.15.b2 and the Annex D first-class cell qaa/fheq-2024/annex-d/professional/r2/3rd-1st."
  author-agent-dialogue: "Raise it when a student aims high or a teaching team calibrates top-band work on clear grasp and use of research ethics. Frame it for a student as what outstanding work looks like, never as the minimum, and ask: \"Which ethical judgement in your research was hardest, and how did you resolve it?\" Do not quote the statement at length, and point a student worried about passing to 4.5.b11 instead."
- statement: qaa/public-policy-and-public-administration-2025/4.6.b12
  forPractitioner: { text: "At the excellent level, graduates will organise and use evidence, data and information from varied primary and secondary sources effectively.", rewrite: light, force: will, status: drafted }
  forBeneficiary: { text: "At an excellent level, you will organise and use evidence, data and information from many original and secondary sources effectively.", rewrite: full, force: will, status: drafted }
  author-agent-written: "Describe this as the excellent level of attainment for an honours degree in Public Policy or Public Administration at FHEQ level 6 (FQHEIS level 10, spine:6): effective organisation and use of evidence from varied sources; it is what the strongest graduates are expected to show, not a minimum. Cite it as (QAA, 2025, Public Policy and Public Administration Subject Benchmark Statement, para 4.6, item 12), and do not treat it as a pass requirement or as a first-class rule, since classification is left to Annex D (4.2). Set it beside the threshold item 4.5.b12, the FHEQ descriptor qaa/fheq-2024/4.15.b5 and the Annex D first-class cell qaa/fheq-2024/annex-d/cognitive/r1/1st."
  author-agent-dialogue: "Raise it when a student aims high or a teaching team calibrates top-band work on effective organisation and use of evidence from varied sources. Frame it for a student as what outstanding work looks like, never as the minimum, and ask: \"How did you bring together sources that disagreed?\" Do not quote the statement at length, and point a student worried about passing to 4.5.b12 instead."
- statement: qaa/public-policy-and-public-administration-2025/4.6.b13
  forPractitioner: { text: "At the excellent level, graduates will show a clear grasp of why personal integrity matters and of the ethical effects decisions may have.", rewrite: light, force: will, status: drafted }
  forBeneficiary: { text: "At an excellent level, you will show a clear grasp of why personal integrity matters and of the ethical consequences of decisions.", rewrite: full, force: will, status: drafted }
  author-agent-written: "Describe this as the excellent level of attainment for an honours degree in Public Policy or Public Administration at FHEQ level 6 (FQHEIS level 10, spine:6): evident grasp of integrity and the ethics of decisions; it is what the strongest graduates are expected to show, not a minimum. Cite it as (QAA, 2025, Public Policy and Public Administration Subject Benchmark Statement, para 4.6, item 13), and do not treat it as a pass requirement or as a first-class rule, since classification is left to Annex D (4.2). Set it beside the threshold item 4.5.b13, the FHEQ descriptor qaa/fheq-2024/4.15.b9.2 and the Annex D first-class cell qaa/fheq-2024/annex-d/professional/r2/3rd-1st."
  author-agent-dialogue: "Raise it when a student aims high or a teaching team calibrates top-band work on evident grasp of integrity and the ethics of decisions. Frame it for a student as what outstanding work looks like, never as the minimum, and ask: \"How would you advise a decision-maker facing a conflict between efficiency and fairness?\" Do not quote the statement at length, and point a student worried about passing to 4.5.b13 instead."
- statement: qaa/public-policy-and-public-administration-2025/4.6.b14
  forPractitioner: { text: "At the excellent level, graduates will evaluate analytically, where relevant, how academic practice relates to professional conduct.", rewrite: light, force: will, status: drafted }
  forBeneficiary: { text: "At an excellent level, you will weigh up analytically, where it applies, how academic work relates to how professionals behave.", rewrite: full, force: will, status: drafted }
  author-agent-written: "Describe this as the excellent level of attainment for an honours degree in Public Policy or Public Administration at FHEQ level 6 (FQHEIS level 10, spine:6): academic practice and professional behaviour; it is what the strongest graduates are expected to show, not a minimum. Cite it as (QAA, 2025, Public Policy and Public Administration Subject Benchmark Statement, para 4.6, item 14), and do not treat it as a pass requirement or as a first-class rule, since classification is left to Annex D (4.2). Set it beside the threshold list 4.5 (it has no threshold counterpart), the FHEQ descriptor qaa/fheq-2024/4.15.b9.1 and the Annex D first-class cell qaa/fheq-2024/annex-d/professional/r1/3rd-1st."
  author-agent-dialogue: "Raise it when a student aims high or a teaching team calibrates top-band work on academic practice and professional behaviour. Frame it for a student as what outstanding work looks like, never as the minimum, and ask: \"Where do the standards of good academic work and good professional conduct pull in different directions?\" Do not quote the statement at length, and point a student worried about passing to the threshold list 4.5 instead."
- statement: qaa/public-policy-and-public-administration-2025/4.6.b15
  forPractitioner: { text: "At the excellent level, graduates will show a developed understanding and use of constructive feedback.", rewrite: light, force: will, status: drafted }
  forBeneficiary: { text: "At an excellent level, you will understand constructive feedback well and use it to improve your work.", rewrite: full, force: will, status: drafted }
  author-agent-written: "Describe this as the excellent level of attainment for an honours degree in Public Policy or Public Administration at FHEQ level 6 (FQHEIS level 10, spine:6): developed use of constructive feedback; it is what the strongest graduates are expected to show, not a minimum. Cite it as (QAA, 2025, Public Policy and Public Administration Subject Benchmark Statement, para 4.6, item 15), and do not treat it as a pass requirement or as a first-class rule, since classification is left to Annex D (4.2). Set it beside the threshold item 4.5.b14, the FHEQ descriptor qaa/fheq-2024/4.15.b5 and the Annex D first-class cell qaa/fheq-2024/annex-d/transferable/r3/1st."
  author-agent-dialogue: "Raise it when a student aims high or a teaching team calibrates top-band work on developed use of constructive feedback. Frame it for a student as what outstanding work looks like, never as the minimum, and ask: \"Which feedback have you sought out yourself, and what did you do with it?\" Do not quote the statement at length, and point a student worried about passing to 4.5.b14 instead."
- statement: qaa/public-policy-and-public-administration-2025/4.6.b16
  forPractitioner: { text: "At the excellent level, graduates will show a strong capacity to choose and use aids and software for communication, information handling and data analysis.", rewrite: light, force: will, status: drafted }
  forBeneficiary: { text: "At an excellent level, you will choose and use the right tools and software for communication, information and data analysis with real skill.", rewrite: full, force: will, status: drafted }
  author-agent-written: "Describe this as the excellent level of attainment for an honours degree in Public Policy or Public Administration at FHEQ level 6 (FQHEIS level 10, spine:6): strong choice and use of tools and software; it is what the strongest graduates are expected to show, not a minimum. Cite it as (QAA, 2025, Public Policy and Public Administration Subject Benchmark Statement, para 4.6, item 16), and do not treat it as a pass requirement or as a first-class rule, since classification is left to Annex D (4.2). Set it beside the threshold item 4.5.b15, the FHEQ descriptor qaa/fheq-2024/4.15.b8 and the Annex D first-class cell qaa/fheq-2024/annex-d/transferable/r1/1st."
  author-agent-dialogue: "Raise it when a student aims high or a teaching team calibrates top-band work on strong choice and use of tools and software. Frame it for a student as what outstanding work looks like, never as the minimum, and ask: \"Which tool did you choose for your last analysis, and why that one?\" Do not quote the statement at length, and point a student worried about passing to 4.5.b15 instead."
- statement: qaa/public-policy-and-public-administration-2025/4.7
  forPractitioner: { text: "At master's level, graduates will show graduate outcomes, command of at least one specialist area and independent project-based work.", rewrite: light, force: will, status: drafted }
  forBeneficiary: { text: "On a master's in this subject, you will show that you command at least one specialist area and can carry out project work independently.", rewrite: full, force: will, status: drafted }
  author-agent-written: "Describe this as the lead outcome for a master's in Public Policy or Public Administration, read at FHEQ level 7 (FQHEIS level 11, spine:7): graduate outcomes, specialist command and independence in project work. Cite it as (QAA, 2025, Public Policy and Public Administration Subject Benchmark Statement, para 4.7), and do not claim the statement names a master's level or sets merit or distinction standards. Set it beside the list items 4.7.b1 to 4.7.b17 and the FHEQ master's descriptors qaa/fheq-2024/4.17.b1 and 4.17.b6."
  author-agent-dialogue: "Raise it when a master's student plans a dissertation or a team scopes specialist pathways. Ask: \"Which specialist area will your project show you command, and which decisions in it are yours alone?\" Avoid treating independence as working without supervision, and avoid reading the paragraph out."
- statement: qaa/public-policy-and-public-administration-2025/4.7.b1
  forPractitioner: { text: "At master's level, graduates will show a systematic, deep understanding of public sector organisations, their context and their management.", rewrite: light, force: will, status: drafted }
  forBeneficiary: { text: "On a master's in this subject, you will understand public sector organisations, their setting and how they are managed, systematically and in depth.", rewrite: full, force: will, status: drafted }
  author-agent-written: "Describe this as an outcome a master's graduate in Public Policy or Public Administration will show, read at FHEQ level 7 (FQHEIS level 11, spine:7): public sector organisations, their context and management. Cite it as (QAA, 2025, Public Policy and Public Administration Subject Benchmark Statement, para 4.7, item 1), and do not apply it to the honours degree or call it a regulatory rule; the level is our reading, since the statement names none for taught master's. Set it beside the FHEQ master's descriptor qaa/fheq-2024/4.17.b1 and, for the step up from honours, 4.6.b1."
  author-agent-dialogue: "Raise it with a master's student, or a team designing a master's course, when the talk turns to public sector organisations, their context and management. Put it in plain words as the step beyond honours that a master's should bring, and ask: \"Which model of public management best explains the organisation you know, and where does it fail?\" Avoid reading the statement out and avoid applying it to undergraduates."
- statement: qaa/public-policy-and-public-administration-2025/4.7.b2
  forPractitioner: { text: "At master's level, graduates will show a full, detailed understanding of the techniques used for close investigation, research and evaluation, or advanced scholarship, in the field.", rewrite: light, force: will, status: drafted }
  forBeneficiary: { text: "On a master's in this subject, you will understand fully the techniques for detailed investigation, research and evaluation in the field.", rewrite: full, force: will, status: drafted }
  author-agent-written: "Describe this as an outcome a master's graduate in Public Policy or Public Administration will show, read at FHEQ level 7 (FQHEIS level 11, spine:7): techniques for investigation, research and evaluation. Cite it as (QAA, 2025, Public Policy and Public Administration Subject Benchmark Statement, para 4.7, item 2), and do not apply it to the honours degree or call it a regulatory rule; the level is our reading, since the statement names none for taught master's. Set it beside the FHEQ master's descriptor qaa/fheq-2024/4.17.b2 and, for the step up from honours, 4.6.b9."
  author-agent-dialogue: "Raise it with a master's student, or a team designing a master's course, when the talk turns to techniques for investigation, research and evaluation. Put it in plain words as the step beyond honours that a master's should bring, and ask: \"Which evaluation technique suits your dissertation question, and why not the alternatives?\" Avoid reading the statement out and avoid applying it to undergraduates."
- statement: qaa/public-policy-and-public-administration-2025/4.7.b3
  forPractitioner: { text: "At master's level, graduates will show a proactive, independent approach to learning.", rewrite: light, force: will, status: drafted }
  forBeneficiary: { text: "On a master's in this subject, you will take charge of your learning, proactively and independently.", rewrite: full, force: will, status: drafted }
  author-agent-written: "Describe this as an outcome a master's graduate in Public Policy or Public Administration will show, read at FHEQ level 7 (FQHEIS level 11, spine:7): proactive, independent learning. Cite it as (QAA, 2025, Public Policy and Public Administration Subject Benchmark Statement, para 4.7, item 3), and do not apply it to the honours degree or call it a regulatory rule; the level is our reading, since the statement names none for taught master's. Set it beside the FHEQ master's descriptor qaa/fheq-2024/4.17.b6 and 4.17.b7 and, for the step up from honours, 4.6.b10."
  author-agent-dialogue: "Raise it with a master's student, or a team designing a master's course, when the talk turns to proactive, independent learning. Put it in plain words as the step beyond honours that a master's should bring, and ask: \"What have you learned this term that nobody asked you to learn?\" Avoid reading the statement out and avoid applying it to undergraduates."
- statement: qaa/public-policy-and-public-administration-2025/4.7.b4
  forPractitioner: { text: "At master's level, graduates will show an agile, reflexive and inventive approach to learning.", rewrite: light, force: will, status: drafted }
  forBeneficiary: { text: "On a master's in this subject, you will learn in a flexible, reflexive and inventive way.", rewrite: full, force: will, status: drafted }
  author-agent-written: "Describe this as an outcome a master's graduate in Public Policy or Public Administration will show, read at FHEQ level 7 (FQHEIS level 11, spine:7): agile, reflexive and innovative learning. Cite it as (QAA, 2025, Public Policy and Public Administration Subject Benchmark Statement, para 4.7, item 4), and do not apply it to the honours degree or call it a regulatory rule; the level is our reading, since the statement names none for taught master's. Set it beside the FHEQ master's descriptor qaa/fheq-2024/4.17.b7 and, for the step up from honours, 4.6.b6."
  author-agent-dialogue: "Raise it with a master's student, or a team designing a master's course, when the talk turns to agile, reflexive and innovative learning. Put it in plain words as the step beyond honours that a master's should bring, and ask: \"When did you change your approach mid-way because what you were doing was not working?\" Avoid reading the statement out and avoid applying it to undergraduates."
- statement: qaa/public-policy-and-public-administration-2025/4.7.b5
  forPractitioner: { text: "At master's level, graduates will show a critical, nuanced awareness of current issues, grounded in research and practice.", rewrite: light, force: will, status: drafted }
  forBeneficiary: { text: "On a master's in this subject, you will have a critical, nuanced awareness of current issues, grounded in research and practice.", rewrite: full, force: will, status: drafted }
  author-agent-written: "Describe this as an outcome a master's graduate in Public Policy or Public Administration will show, read at FHEQ level 7 (FQHEIS level 11, spine:7): critical awareness of current issues. Cite it as (QAA, 2025, Public Policy and Public Administration Subject Benchmark Statement, para 4.7, item 5), and do not apply it to the honours degree or call it a regulatory rule; the level is our reading, since the statement names none for taught master's. Set it beside the FHEQ master's descriptor qaa/fheq-2024/4.17.b1 and, for the step up from honours, 4.6.b2."
  author-agent-dialogue: "Raise it with a master's student, or a team designing a master's course, when the talk turns to critical awareness of current issues. Put it in plain words as the step beyond honours that a master's should bring, and ask: \"Which current issue in public policy is most misunderstood, and what does research say about it?\" Avoid reading the statement out and avoid applying it to undergraduates."
- statement: qaa/public-policy-and-public-administration-2025/4.7.b6
  forPractitioner: { text: "At master's level, graduates will show the conceptual competence to evaluate current research and advanced scholarship critically.", rewrite: light, force: will, status: drafted }
  forBeneficiary: { text: "On a master's in this subject, you will have the conceptual tools to evaluate current research and advanced scholarship critically.", rewrite: full, force: will, status: drafted }
  author-agent-written: "Describe this as an outcome a master's graduate in Public Policy or Public Administration will show, read at FHEQ level 7 (FQHEIS level 11, spine:7): critically evaluating research and scholarship. Cite it as (QAA, 2025, Public Policy and Public Administration Subject Benchmark Statement, para 4.7, item 6), and do not apply it to the honours degree or call it a regulatory rule; the level is our reading, since the statement names none for taught master's. Set it beside the FHEQ master's descriptor qaa/fheq-2024/4.17.b4.1 and, for the step up from honours, 4.6.b2."
  author-agent-dialogue: "Raise it with a master's student, or a team designing a master's course, when the talk turns to critically evaluating research and scholarship. Put it in plain words as the step beyond honours that a master's should bring, and ask: \"What are the weakest assumptions in the most-cited study you have read?\" Avoid reading the statement out and avoid applying it to undergraduates."
- statement: qaa/public-policy-and-public-administration-2025/4.7.b7
  forPractitioner: { text: "At master's level, graduates will show the ability to apply relevant knowledge to varied complex situations, allowing for the field's hybrid setting.", rewrite: light, force: will, status: drafted }
  forBeneficiary: { text: "On a master's in this subject, you will apply what you know to many complex situations, allowing for the mix of public, private and non-profit settings in the field.", rewrite: full, force: will, status: drafted }
  author-agent-written: "Describe this as an outcome a master's graduate in Public Policy or Public Administration will show, read at FHEQ level 7 (FQHEIS level 11, spine:7): applying knowledge to complex situations. Cite it as (QAA, 2025, Public Policy and Public Administration Subject Benchmark Statement, para 4.7, item 7), and do not apply it to the honours degree or call it a regulatory rule; the level is our reading, since the statement names none for taught master's. Set it beside the FHEQ master's descriptor qaa/fheq-2024/4.17.b5 and, for the step up from honours, 4.6.b7."
  author-agent-dialogue: "Raise it with a master's student, or a team designing a master's course, when the talk turns to applying knowledge to complex situations. Put it in plain words as the step beyond honours that a master's should bring, and ask: \"How would your recommendation change if the service were run by a charity instead of a council?\" Avoid reading the statement out and avoid applying it to undergraduates."
- statement: qaa/public-policy-and-public-administration-2025/4.7.b8
  forPractitioner: { text: "At master's level, graduates will show originality, creativity and entrepreneurship in applying knowledge, and a practical grasp of how established research techniques produce and interpret knowledge.", rewrite: light, force: will, status: drafted }
  forBeneficiary: { text: "On a master's in this subject, you will apply what you know with originality, creativity and enterprise, and understand in practice how research methods create and interpret knowledge.", rewrite: full, force: will, status: drafted }
  author-agent-written: "Describe this as an outcome a master's graduate in Public Policy or Public Administration will show, read at FHEQ level 7 (FQHEIS level 11, spine:7): originality, creativity and entrepreneurship with research techniques. Cite it as (QAA, 2025, Public Policy and Public Administration Subject Benchmark Statement, para 4.7, item 8), and do not apply it to the honours degree or call it a regulatory rule; the level is our reading, since the statement names none for taught master's. Set it beside the FHEQ master's descriptor qaa/fheq-2024/4.17.b3 and, for the step up from honours, 4.6.b8."
  author-agent-dialogue: "Raise it with a master's student, or a team designing a master's course, when the talk turns to originality, creativity and entrepreneurship with research techniques. Put it in plain words as the step beyond honours that a master's should bring, and ask: \"What is original in your approach, and which established method does it rest on?\" Avoid reading the statement out and avoid applying it to undergraduates."
- statement: qaa/public-policy-and-public-administration-2025/4.7.b9
  forPractitioner: { text: "At master's level, graduates will assess and combine theory, practice and experience across many situations.", rewrite: light, force: will, status: drafted }
  forBeneficiary: { text: "On a master's in this subject, you will assess and combine theory, practice and experience in many kinds of situation.", rewrite: full, force: will, status: drafted }
  author-agent-written: "Describe this as an outcome a master's graduate in Public Policy or Public Administration will show, read at FHEQ level 7 (FQHEIS level 11, spine:7): integrating theory, practice and experience. Cite it as (QAA, 2025, Public Policy and Public Administration Subject Benchmark Statement, para 4.7, item 9), and do not apply it to the honours degree or call it a regulatory rule; the level is our reading, since the statement names none for taught master's. Set it beside the FHEQ master's descriptor qaa/fheq-2024/4.17.b5 and, for the step up from honours, 4.6.b14."
  author-agent-dialogue: "Raise it with a master's student, or a team designing a master's course, when the talk turns to integrating theory, practice and experience. Put it in plain words as the step beyond honours that a master's should bring, and ask: \"Where has your own work experience challenged a theory you were taught?\" Avoid reading the statement out and avoid applying it to undergraduates."
- statement: qaa/public-policy-and-public-administration-2025/4.7.b10
  forPractitioner: { text: "At master's level, graduates will show a full understanding of how research and practice push forward the limits of knowledge.", rewrite: light, force: will, status: drafted }
  forBeneficiary: { text: "On a master's in this subject, you will understand fully how research and practice push knowledge forward.", rewrite: full, force: will, status: drafted }
  author-agent-written: "Describe this as an outcome a master's graduate in Public Policy or Public Administration will show, read at FHEQ level 7 (FQHEIS level 11, spine:7): how research and practice extend knowledge. Cite it as (QAA, 2025, Public Policy and Public Administration Subject Benchmark Statement, para 4.7, item 10), and do not apply it to the honours degree or call it a regulatory rule; the level is our reading, since the statement names none for taught master's. Set it beside the FHEQ master's descriptor qaa/fheq-2024/4.17.b3 and, for the step up from honours, 4.6.b2."
  author-agent-dialogue: "Raise it with a master's student, or a team designing a master's course, when the talk turns to how research and practice extend knowledge. Put it in plain words as the step beyond honours that a master's should bring, and ask: \"Can you name a change in practice that came from research, and one that came the other way?\" Avoid reading the statement out and avoid applying it to undergraduates."
- statement: qaa/public-policy-and-public-administration-2025/4.7.b11
  forPractitioner: { text: "At master's level, graduates will show a developed grasp of, and commitment to, the values and ethics of public service, acting with integrity and encouraging it in others.", rewrite: light, force: will, status: drafted }
  forBeneficiary: { text: "On a master's in this subject, you will understand and commit to public sector values and ethics, and act with integrity and encourage it in others.", rewrite: full, force: will, status: drafted }
  author-agent-written: "Describe this as an outcome a master's graduate in Public Policy or Public Administration will show, read at FHEQ level 7 (FQHEIS level 11, spine:7): public sector values, ethics and integrity. Cite it as (QAA, 2025, Public Policy and Public Administration Subject Benchmark Statement, para 4.7, item 11), and do not apply it to the honours degree or call it a regulatory rule; the level is our reading, since the statement names none for taught master's. Set it beside the FHEQ master's descriptor qaa/fheq-2024/4.17.b8.1 and, for the step up from honours, 4.6.b13."
  author-agent-dialogue: "Raise it with a master's student, or a team designing a master's course, when the talk turns to public sector values, ethics and integrity. Put it in plain words as the step beyond honours that a master's should bring, and ask: \"Which public service value would you defend even at a cost to efficiency?\" Avoid reading the statement out and avoid applying it to undergraduates."
- statement: qaa/public-policy-and-public-administration-2025/4.7.b12
  forPractitioner: { text: "At master's level, graduates will show professional reflective capacities that improve professional practice.", rewrite: light, force: will, status: drafted }
  forBeneficiary: { text: "On a master's in this subject, you will reflect as a professional in ways that improve your practice.", rewrite: full, force: will, status: drafted }
  author-agent-written: "Describe this as an outcome a master's graduate in Public Policy or Public Administration will show, read at FHEQ level 7 (FQHEIS level 11, spine:7): professional reflection. Cite it as (QAA, 2025, Public Policy and Public Administration Subject Benchmark Statement, para 4.7, item 12), and do not apply it to the honours degree or call it a regulatory rule; the level is our reading, since the statement names none for taught master's. Set it beside the FHEQ master's descriptor qaa/fheq-2024/4.17.b7 and, for the step up from honours, 4.6.b6."
  author-agent-dialogue: "Raise it with a master's student, or a team designing a master's course, when the talk turns to professional reflection. Put it in plain words as the step beyond honours that a master's should bring, and ask: \"What has reflecting on your work changed in how you practise?\" Avoid reading the statement out and avoid applying it to undergraduates."
- statement: qaa/public-policy-and-public-administration-2025/4.7.b13
  forPractitioner: { text: "At master's level, graduates will show a nuanced understanding of how policy and administration affect societies and the environment.", rewrite: light, force: will, status: drafted }
  forBeneficiary: { text: "On a master's in this subject, you will understand, with nuance, how policy and administration affect people, societies and the environment.", rewrite: full, force: will, status: drafted }
  author-agent-written: "Describe this as an outcome a master's graduate in Public Policy or Public Administration will show, read at FHEQ level 7 (FQHEIS level 11, spine:7): effects of policy and administration on societies and the environment. Cite it as (QAA, 2025, Public Policy and Public Administration Subject Benchmark Statement, para 4.7, item 13), and do not apply it to the honours degree or call it a regulatory rule; the level is our reading, since the statement names none for taught master's. Set it beside the FHEQ master's descriptor qaa/fheq-2024/4.17.b1 and, for the step up from honours, 4.6.b2."
  author-agent-dialogue: "Raise it with a master's student, or a team designing a master's course, when the talk turns to effects of policy and administration on societies and the environment. Put it in plain words as the step beyond honours that a master's should bring, and ask: \"Who gains and who loses, socially and environmentally, from the policy you know best?\" Avoid reading the statement out and avoid applying it to undergraduates."
- statement: qaa/public-policy-and-public-administration-2025/4.7.b14
  forPractitioner: { text: "At master's level, graduates will take an international and global view.", rewrite: light, force: will, status: drafted }
  forBeneficiary: { text: "On a master's in this subject, you will look at questions from an international and global point of view.", rewrite: full, force: will, status: drafted }
  author-agent-written: "Describe this as an outcome a master's graduate in Public Policy or Public Administration will show, read at FHEQ level 7 (FQHEIS level 11, spine:7): an international and global perspective. Cite it as (QAA, 2025, Public Policy and Public Administration Subject Benchmark Statement, para 4.7, item 14), and do not apply it to the honours degree or call it a regulatory rule; the level is our reading, since the statement names none for taught master's. Set it beside the FHEQ master's descriptor qaa/fheq-2024/4.17.b5 and, for the step up from honours, 4.6.b2."
  author-agent-dialogue: "Raise it with a master's student, or a team designing a master's course, when the talk turns to an international and global perspective. Put it in plain words as the step beyond honours that a master's should bring, and ask: \"How has another country tackled the problem you are studying, and could it work here?\" Avoid reading the statement out and avoid applying it to undergraduates."
- statement: qaa/public-policy-and-public-administration-2025/4.7.b15
  forPractitioner: { text: "At master's level, graduates will work, engage and lead in collaborative, multicultural and diverse settings at home and abroad.", rewrite: light, force: will, status: drafted }
  forBeneficiary: { text: "On a master's in this subject, you will work, engage and lead in collaborative, multicultural and diverse settings, in the UK and internationally.", rewrite: full, force: will, status: drafted }
  author-agent-written: "Describe this as an outcome a master's graduate in Public Policy or Public Administration will show, read at FHEQ level 7 (FQHEIS level 11, spine:7): collaborative, diverse working and leadership. Cite it as (QAA, 2025, Public Policy and Public Administration Subject Benchmark Statement, para 4.7, item 15), and do not apply it to the honours degree or call it a regulatory rule; the level is our reading, since the statement names none for taught master's. Set it beside the FHEQ master's descriptor qaa/fheq-2024/4.17.b8.2 and, for the step up from honours, 4.6.b3."
  author-agent-dialogue: "Raise it with a master's student, or a team designing a master's course, when the talk turns to collaborative, diverse working and leadership. Put it in plain words as the step beyond honours that a master's should bring, and ask: \"When have you led a group whose members saw the problem very differently?\" Avoid reading the statement out and avoid applying it to undergraduates."
- statement: qaa/public-policy-and-public-administration-2025/4.7.b16
  forPractitioner: { text: "At master's level, graduates will negotiate and influence in professional settings.", rewrite: light, force: will, status: drafted }
  forBeneficiary: { text: "On a master's in this subject, you will negotiate and influence others in professional settings.", rewrite: full, force: will, status: drafted }
  author-agent-written: "Describe this as an outcome a master's graduate in Public Policy or Public Administration will show, read at FHEQ level 7 (FQHEIS level 11, spine:7): negotiation and influence. Cite it as (QAA, 2025, Public Policy and Public Administration Subject Benchmark Statement, para 4.7, item 16), and do not apply it to the honours degree or call it a regulatory rule; the level is our reading, since the statement names none for taught master's. Set it beside the FHEQ master's descriptor qaa/fheq-2024/4.17.b5 and, for the step up from honours, 4.6.b4."
  author-agent-dialogue: "Raise it with a master's student, or a team designing a master's course, when the talk turns to negotiation and influence. Put it in plain words as the step beyond honours that a master's should bring, and ask: \"How would you persuade a reluctant partner agency to share data?\" Avoid reading the statement out and avoid applying it to undergraduates."
- statement: qaa/public-policy-and-public-administration-2025/4.7.b17
  forPractitioner: { text: "At master's level, graduates will show the independent learning ability needed for continuing professional development.", rewrite: light, force: will, status: drafted }
  forBeneficiary: { text: "On a master's in this subject, you will have the independent learning ability you need to keep developing professionally.", rewrite: full, force: will, status: drafted }
  author-agent-written: "Describe this as an outcome a master's graduate in Public Policy or Public Administration will show, read at FHEQ level 7 (FQHEIS level 11, spine:7): independent learning for continuing professional development. Cite it as (QAA, 2025, Public Policy and Public Administration Subject Benchmark Statement, para 4.7, item 17), and do not apply it to the honours degree or call it a regulatory rule; the level is our reading, since the statement names none for taught master's. Set it beside the FHEQ master's descriptor qaa/fheq-2024/4.17.b8.3 and, for the step up from honours, 4.6.b10."
  author-agent-dialogue: "Raise it with a master's student, or a team designing a master's course, when the talk turns to independent learning for continuing professional development. Put it in plain words as the step beyond honours that a master's should bring, and ask: \"What will you need to learn in the next five years, and how will you learn it?\" Avoid reading the statement out and avoid applying it to undergraduates."
```

### S5 Levels and alignment
<!-- label: both; status: drafted; basis: primary -->
```yaml
levels:
  - { id: "fheq:6", role: "cites", locator: "D1, 2.7; 4.2 (honours); 4.5 and 4.6 read as level 6" }
  - { id: "fqheis:10", role: "cites", locator: "D1, 2.7; 4.2" }
  - { id: "fheq:7", role: "cites", locator: "D1, 2.12 (integrated master's); 4.7 read as level 7 (inferred for taught master's)" }
  - { id: "fqheis:11", role: "cites", locator: "D1, 2.12" }
  - { id: "fheq:4", role: "cites", locator: "D1, 2.9 (CertHE exit award)" }
  - { id: "fqheis:8", role: "cites", locator: "D1, 2.9" }
  - { id: "fheq:5", role: "cites", locator: "D1, 2.9 (DipHE exit award)" }
  - { id: "fqheis:9", role: "cites", locator: "D1, 2.9" }
crosswalks:
  - { from: "fheq:6", to: "fqheis:10", relation: "equivalent", basis: "stated (D1, 2.7: honours at FHEQ Level 6, FQHEIS Level 10; 4.2)" }
  - { from: "fheq:7", to: "fqheis:11", relation: "equivalent", basis: "stated (D1, 2.12: integrated master's at FHEQ Level 7, FQHEIS Level 11)" }
  - { from: "fheq:4", to: "fqheis:8", relation: "equivalent", basis: "stated (D1, 2.9: CertHE at FHEQ Level 4, FQHEIS Level 8)" }
  - { from: "fheq:5", to: "fqheis:9", relation: "equivalent", basis: "stated (D1, 2.9: DipHE at FHEQ Level 5, FQHEIS Level 9)" }
  - { from: "4.5 threshold", to: "Annex D 3rd (pass or threshold)", relation: "thresholdAt", basis: "inferred: 4.2 ties performance above the minimum threshold to Annex D; the statement does not map its levels to classes" }
  - { from: "fheq:6, fheq:7", to: "spine:6, spine:7", relation: "levelEquivalent", basis: "inferred from std:ref:uk-framework R2" }
```

### S6 Themes
<!-- label: both; status: drafted; basis: primary -->
```yaml
- { id: "theme:edi", role: "carries", carriedIn: ["front matter", "1.6", "1.12", "1.13", "1.14", "1.15", "1.16", "1.17", "1.21", "2.15", "2.19", "2.22", "3.3", "3.6", "3.8", "3.11", "3.13", "4.3", "4.7"] }
- { id: "theme:accessibility", role: "carries", carriedIn: ["front matter", "1.6", "1.15", "1.16", "1.17", "3.6", "3.11"] }
- { id: "theme:esd", role: "carries", carriedIn: ["front matter", "1.6", "1.18", "1.19", "2.22", "3.3", "3.6"] }
- { id: "theme:enterprise", role: "carries", carriedIn: ["front matter", "1.19", "1.20", "1.21", "1.22", "1.22 (second)", "1.23", "1.24", "1.25", "1.26", "2.22", "3.5", "3.6", "3.7", "3.10", "3.12", "4.7"] }
- { id: "theme:generative-ai", role: "carries", carriedIn: ["front matter", "1.26", "1.27", "1.28", "3.8", "3.12"] }
```

### S7 Relations
<!-- label: both; status: drafted; basis: primary -->
```yaml
- { rel: "partOf", target: "collection: QAA Subject Benchmark Statements", note: "one of 54 held by stan" }
- { rel: "refersTo", target: "std:doc:qaa-fheq-2024-framework, Annex D", note: "the classification descriptions providers should refer to for performance above threshold (4.2)" }
- { rel: "cites", target: "std:doc:qaa-fheq-2024-framework", note: "FHEQ levels 4 to 7 named (2.7, 2.9, 2.12, 4.2); the 2024 Frameworks in the references" }
- { rel: "cites", target: "std:doc:qaa-fqheis-2024-framework", note: "FQHEIS levels 8 to 11 named (2.7, 2.9, 2.12, 4.2)" }
- { rel: "cites", target: "std:doc:qaa-advancehe-esd-2021-guidance", note: "its definitions of sustainable development and ESD are quoted (1.18)" }
- { rel: "cites", target: "std:doc:qaa-enterprise-2018-guidance", note: "listed in the references (back matter)" }
- { rel: "refersTo", target: "QAA (2020) Characteristics Statement: Master's Degree (not ingested)", note: "listed in the references only" }
- { rel: "relatedTo", target: "std:ref:uk-framework", note: "spine:6 and spine:7 for the honours and master's lists (inferred)" }
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
- Public Policy and Public Administration are joined but separate: policy studies what shapes the decisions of governments and regulators, administration studies how policy is formed and put into effect (D1, 1.1).
- The subjects study systems, processes, governance and management of public decisions at every tier of government, in democratic and non-democratic states, including the effects of decisions on citizens (D1, 1.2, 1.5, 3.3).
- They are taught in many host disciplines, among them economics, politics, social policy, sociology, planning, management, law and business (D1, 1.3).
- Study follows the policy cycle from problem definition and agenda-setting through design, transfer, instruments and implementation to evaluation, using several theories and comparisons across sectors and systems (D1, 1.6, 2.2).
- Fairness and social justice are central, including the UK public sector equality duty, and principles such as legality, accountability, proportionality and impartiality frame the judgement of public bodies (D1, 1.6, 1.7).
- The subjects are interdisciplinary, join theory with practice and stress effectiveness, efficiency and equity in service design, with co-design, co-production and collaboration between agencies (D1, 1.8, 2.1, 2.3).
- Public and social value, public service motivation and ethos are characteristic themes; courses are often taught with practitioners and use real cases (D1, 2.4, 2.5, 2.17, 2.18).
- Most provision is postgraduate (MSc, MPA, MPP), with pre- and post-experience cohorts; undergraduate Public Administration degrees are few, and public sector content is common in foundation degrees (D1, 2.6, 2.11).

### SB2 Themes in this subject
<!-- label: both; status: drafted; basis: primary -->
```yaml
- theme: theme:edi
  inThisSubject: "equity is part of the subject matter: fair policy, just institutions and the public sector equality duty; EDI in curriculum, pedagogy and assessment, voices of subjugated groups, inclusive feedback and advisory input (D1, 1.6, 1.12 to 1.14, 3.13)"
  statements: ["qaa/public-policy-and-public-administration-2025/1.12", "qaa/public-policy-and-public-administration-2025/1.14", "qaa/public-policy-and-public-administration-2025/3.13", "qaa/public-policy-and-public-administration-2025/4.3", "qaa/public-policy-and-public-administration-2025/4.7.b15"]
- theme: theme:accessibility
  inThisSubject: "graduates will design accessible services beyond legal compliance; courses make reasonable adjustments, accessible spaces, resources, visits and careers support, and digital inclusion (D1, 1.15 to 1.17, 3.6, 3.11)"
  statements: ["qaa/public-policy-and-public-administration-2025/1.17", "qaa/public-policy-and-public-administration-2025/3.6"]
- theme: theme:esd
  inThisSubject: "the subject equips future public managers and policymakers to realise the sustainable development goals; ESD pedagogies and UNESCO learning objectives; SDGs among the subfields (D1, 1.18, 1.19, 3.3)"
  statements: ["qaa/public-policy-and-public-administration-2025/3.3", "qaa/public-policy-and-public-administration-2025/3.6", "qaa/public-policy-and-public-administration-2025/4.7.b13"]
- theme: theme:enterprise
  inThisSubject: "named employability, entrepreneurship and enterprise education (EEE): practice links required for pre- and post-experience students, graduates able to articulate their skills, employer work and accreditation routes (D1, 1.20 to 1.25, 3.10)"
  statements: ["qaa/public-policy-and-public-administration-2025/1.22", "qaa/public-policy-and-public-administration-2025/1.23", "qaa/public-policy-and-public-administration-2025/3.7", "qaa/public-policy-and-public-administration-2025/3.10", "qaa/public-policy-and-public-administration-2025/4.7.b8"]
- theme: theme:generative-ai
  inThisSubject: "degrees must respond to an AI-shaped labour market and changing assessment; ethical, responsible use of GenAI, including in authentic assessment (D1, 1.26 to 1.28, 3.8, 3.12)"
  statements: ["qaa/public-policy-and-public-administration-2025/1.26"]
```

### SB3 Content and delivery
<!-- label: both; status: drafted; basis: primary -->
```yaml
areas:
  - { component: "3.3", gloss: "governance and policy across contexts; 40 typical subfields from administrative law to voluntary sector administration, of which courses cover a number" }
  - { component: "3.4", gloss: "policy degrees lean to the policy cycle and evaluation, administration degrees to leadership, management, project management and finance" }
  - { component: "3.5", gloss: "transferable cognitive, behavioural and affective capacities; vocational to theoretical range" }
practices:
  - { component: "3.2", kind: "learning", gloss: "practice-based learning, action learning, reflection and placements" }
  - { component: "3.6", kind: "teaching", gloss: "methods fitted to content and learners; many modes; digital inclusion" }
  - { component: "3.7", kind: "learning", gloss: "lectures, seminars, cases, simulations, work-based learning, independent study, practitioner talks, fieldwork" }
  - { component: "3.8", kind: "learning", gloss: "diverse sources and digital tools, with support for critical and ethical use, GenAI included" }
  - { component: "3.9", kind: "teaching", gloss: "research-led teaching and practitioner co-creation" }
  - { component: "3.10", kind: "assessment", gloss: "strategy aligned with curriculum and outcomes; assessment for and as learning" }
  - { component: "3.11", kind: "assessment", gloss: "plural assessment, workload and reasonable adjustments" }
  - { component: "3.12", kind: "assessment", gloss: "five kinds: critical analysis, communication, independent research, authentic practice tasks, reflection" }
  - { component: "3.13", kind: "assessment", gloss: "constructive, consistent and specific feedback throughout" }
```

### SB4 Benchmark standards
<!-- label: both; status: drafted; basis: primary -->
```yaml
rungs:
  - { rung: "threshold", leadIn: "4.5", award: "bachelor's with honours", items: 15, label: "Threshold level" }
  - { rung: "typical", leadIn: "none", award: "bachelor's with honours", items: 0, label: "not stated" }
  - { rung: "excellent", leadIn: "4.6", award: "bachelor's with honours", items: 16, label: "Excellent level" }
  - { rung: "threshold", leadIn: "4.7", award: "master's", items: 18, label: "Master's (no rung named; recorded as threshold by convention)" }
rungBases: "4.5 and 4.6 are separate lists for honours graduates at threshold and at an excellent level of attainment; there is no typical list. 4.2 calls the threshold the minimum and refers classification to Annex D. 4.7 is one master's list under a lead-in whose first sentence names three outcomes of its own (recorded as 4.7). 4.4: the standards are not a checklist and carry no weighting."
outcomeLists: []
outcomes:
  - { outcome: [], threshold: "qaa/public-policy-and-public-administration-2025/4.5.b1", typical: "none", excellent: "qaa/public-policy-and-public-administration-2025/4.6.b1", basis: "inferred", domain: "knowledge", award: "bachelor's with honours" }
  - { outcome: ["informed"], threshold: "qaa/public-policy-and-public-administration-2025/4.5.b2", typical: "none", excellent: "qaa/public-policy-and-public-administration-2025/4.6.b2", basis: "inferred", domain: "understanding", award: "bachelor's with honours" }
  - { outcome: ["collaborate", "achieve"], threshold: "qaa/public-policy-and-public-administration-2025/4.5.b7", typical: "none", excellent: "qaa/public-policy-and-public-administration-2025/4.6.b3", basis: "inferred", domain: "generic-skill", award: "bachelor's with honours" }
  - { outcome: ["communicate"], threshold: "qaa/public-policy-and-public-administration-2025/4.5.b8", typical: "none", excellent: "qaa/public-policy-and-public-administration-2025/4.6.b4", basis: "inferred", domain: "generic-skill", award: "bachelor's with honours" }
  - { outcome: ["construct", "synthesising", "exercising"], threshold: "qaa/public-policy-and-public-administration-2025/4.5.b3", typical: "none", excellent: "qaa/public-policy-and-public-administration-2025/4.6.b5", basis: "inferred", domain: "generic-skill", award: "bachelor's with honours" }
  - { outcome: ["reflect"], threshold: "qaa/public-policy-and-public-administration-2025/4.5.b9", typical: "none", excellent: "qaa/public-policy-and-public-administration-2025/4.6.b6", basis: "inferred", domain: "generic-skill", award: "bachelor's with honours" }
  - { outcome: ["making"], threshold: "qaa/public-policy-and-public-administration-2025/4.5.b4", typical: "none", excellent: "qaa/public-policy-and-public-administration-2025/4.6.b7", basis: "inferred", domain: "generic-skill", award: "bachelor's with honours" }
  - { outcome: ["identifying", "investigating", "solving", "thinking"], threshold: "qaa/public-policy-and-public-administration-2025/4.5.b5", typical: "none", excellent: "qaa/public-policy-and-public-administration-2025/4.6.b8", basis: "inferred", domain: "subject-skill", award: "bachelor's with honours" }
  - { outcome: ["evaluate", "apply", "collecting", "analysing", "presenting"], threshold: "qaa/public-policy-and-public-administration-2025/4.5.b6", typical: "none", excellent: "qaa/public-policy-and-public-administration-2025/4.6.b9", basis: "inferred", domain: "subject-skill", award: "bachelor's with honours" }
  - { outcome: ["working"], threshold: "qaa/public-policy-and-public-administration-2025/4.5.b10", typical: "none", excellent: "qaa/public-policy-and-public-administration-2025/4.6.b10", basis: "inferred", domain: "generic-skill", award: "bachelor's with honours" }
  - { outcome: ["understanding", "applying"], threshold: "qaa/public-policy-and-public-administration-2025/4.5.b11", typical: "none", excellent: "qaa/public-policy-and-public-administration-2025/4.6.b11", basis: "inferred", domain: "subject-skill", award: "bachelor's with honours" }
  - { outcome: [], threshold: "qaa/public-policy-and-public-administration-2025/4.5.b12", typical: "none", excellent: "qaa/public-policy-and-public-administration-2025/4.6.b12", basis: "inferred", domain: "subject-skill", award: "bachelor's with honours" }
  - { outcome: [], threshold: "qaa/public-policy-and-public-administration-2025/4.5.b13", typical: "none", excellent: "qaa/public-policy-and-public-administration-2025/4.6.b13", basis: "inferred", domain: "understanding", award: "bachelor's with honours" }
  - { outcome: [], threshold: "qaa/public-policy-and-public-administration-2025/4.5.b14", typical: "none", excellent: "qaa/public-policy-and-public-administration-2025/4.6.b15", basis: "inferred", domain: "generic-skill", award: "bachelor's with honours" }
  - { outcome: ["select", "use"], threshold: "qaa/public-policy-and-public-administration-2025/4.5.b15", typical: "none", excellent: "qaa/public-policy-and-public-administration-2025/4.6.b16", basis: "inferred", domain: "generic-skill", award: "bachelor's with honours" }
  - { outcome: "academic practice and professional behaviour", threshold: "none", typical: "none", excellent: "qaa/public-policy-and-public-administration-2025/4.6.b14", basis: "inferred", domain: "subject-skill", award: "bachelor's with honours" }
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
- { body: "professional, statutory and regulatory bodies (PSRBs)", says: "the statement can support their definitions of academic standards; their requirements are among the reference points providers use and may inform competence standards (D1, front matter, 4.3)", requirements: "not yet ingested (Part E)" }
- { body: "Chartered Management Institute (CMI)", says: "a professional accreditation providers may combine with degrees (D1, 1.25)", requirements: "not yet ingested (Part E)" }
- { body: "International Commission on the Accreditation of Public Administration and Training (ICAPA)", says: "a route to additional academic accreditation (D1, 1.25)", requirements: "not yet ingested (Part E)" }
- { body: "European Association for Public Administration Accreditation (EAPAA)", says: "a route to additional academic accreditation (D1, 1.25)", requirements: "not yet ingested (Part E)" }
- { body: "Network of Schools of Public Policy, Affairs and Administration (NASPAA)", says: "a route to additional academic accreditation (D1, 1.25)", requirements: "not yet ingested (Part E)" }
- { body: "professional and accrediting bodies (generic)", says: "where they evaluate professional or vocational outcomes, courses build their requirements into degree management; degrees may be accredited for CPD; course teams may engage with professional bodies (D1, 2.16, 2.23, 3.9)", requirements: "not yet ingested (Part E)" }
- { body: "Equality and Human Rights Commission", says: "providers writing competence standards should follow its latest guidance (D1, 4.3)", requirements: "not-applicable-by-design: guidance, not course requirements" }
- { body: "Office for Students", says: "in England the statement is not a sector-recognised standard under its regulatory framework (D1, front matter)", requirements: "not-applicable-by-design" }
```

### SB6 Cross-cutting references
<!-- label: both; status: drafted; basis: primary -->
```yaml
themes:
  - { id: "theme:edi", named: "Equity, diversity and inclusion (EDI)", carriedIn: ["front matter", "1.6", "1.12", "1.13", "1.14", "1.15", "1.16", "1.17", "1.21", "2.15", "2.19", "2.22", "3.3", "3.6", "3.8", "3.11", "3.13", "4.3", "4.7"], statements: ["qaa/public-policy-and-public-administration-2025/1.12", "qaa/public-policy-and-public-administration-2025/1.14", "qaa/public-policy-and-public-administration-2025/3.13", "qaa/public-policy-and-public-administration-2025/4.3", "qaa/public-policy-and-public-administration-2025/4.7.b15"] }
  - { id: "theme:accessibility", named: "Accessibility and the needs of disabled students", carriedIn: ["front matter", "1.6", "1.15", "1.16", "1.17", "3.6", "3.11"], statements: ["qaa/public-policy-and-public-administration-2025/1.17", "qaa/public-policy-and-public-administration-2025/3.6"] }
  - { id: "theme:esd", named: "Education for sustainable development (ESD)", carriedIn: ["front matter", "1.6", "1.18", "1.19", "2.22", "3.3", "3.6"], statements: ["qaa/public-policy-and-public-administration-2025/3.3", "qaa/public-policy-and-public-administration-2025/3.6", "qaa/public-policy-and-public-administration-2025/4.7.b13"] }
  - { id: "theme:enterprise", named: "Employability, entrepreneurship and enterprise education (EEE)", carriedIn: ["front matter", "1.19", "1.20", "1.21", "1.22", "1.22 (second)", "1.23", "1.24", "1.25", "1.26", "2.22", "3.5", "3.6", "3.7", "3.10", "3.12", "4.7"], statements: ["qaa/public-policy-and-public-administration-2025/1.22", "qaa/public-policy-and-public-administration-2025/1.23", "qaa/public-policy-and-public-administration-2025/3.7", "qaa/public-policy-and-public-administration-2025/3.10", "qaa/public-policy-and-public-administration-2025/4.7.b8"] }
  - { id: "theme:generative-ai", named: "Generative artificial intelligence (Gen AI)", carriedIn: ["front matter", "1.26", "1.27", "1.28", "3.8", "3.12"], statements: ["qaa/public-policy-and-public-administration-2025/1.26"] }
frameworks:
  - { framework: "fheq", levels: ["fheq:4", "fheq:5", "fheq:6", "fheq:7"], citedIn: ["2.7", "2.9", "2.12", "4.2"] }
  - { framework: "scqf", levels: ["fqheis:8", "fqheis:9", "fqheis:10", "fqheis:11"], citedIn: ["2.7", "2.9", "2.12", "4.2"] }
bodies:
  - { body: "PSRBs (generic)", citedIn: ["front matter", "4.3"] }
  - { body: "Chartered Management Institute (CMI)", citedIn: ["1.25", "back matter: references"] }
  - { body: "ICAPA", citedIn: ["1.25", "back matter: references"] }
  - { body: "EAPAA", citedIn: ["1.25", "back matter: references"] }
  - { body: "NASPAA", citedIn: ["1.25", "back matter: references"] }
  - { body: "professional and accrediting bodies (generic)", citedIn: ["2.16", "2.23", "3.9"] }
  - { body: "Equality and Human Rights Commission", citedIn: ["4.3"] }
  - { body: "Office for Students", citedIn: ["front matter"] }
sharedDocuments:
  - { document: "std:doc:qaa-fheq-2024-framework, Annex D", named: "Annex D of The Frameworks for Higher Education Qualifications of UK Degree-Awarding Bodies", citedIn: ["4.2"], role: "the classification descriptions for performance above threshold" }
  - { document: "std:doc:qaa-fheq-2024-framework", named: "The Frameworks for Higher Education Qualifications of UK Degree-Awarding Bodies (2024)", citedIn: ["4.2", "back matter: references"], role: "FHEQ and FQHEIS levels" }
  - { document: "std:doc:qaa-advancehe-esd-2021-guidance", named: "QAA and Advance HE's Education for Sustainable Development Guidance (2021)", citedIn: ["1.18", "back matter: references"], role: "definitions of sustainable development and ESD; curriculum review" }
  - { document: "std:doc:qaa-enterprise-2018-guidance", named: "Enterprise and Entrepreneurship Education: Guidance for UK Higher Education Providers (2018)", citedIn: ["back matter: references"], role: "the enterprise theme" }
  - { document: "QAA Creating Inclusive Subject Communities (2021) (not ingested: Part E)", named: "Creating Inclusive Subject Communities: New QAA Advice", citedIn: ["1.12", "back matter: references"], role: "EDI resource" }
  - { document: "QAA Characteristics Statement: Master's Degree (2020) (not ingested: Part E)", named: "Characteristics Statement: Master's Degree", citedIn: ["back matter: references"], role: "background to the master's list" }
  - { document: "QAA Quality Code 2024 (not ingested)", named: "the Quality Code (2024 update)", citedIn: ["front matter"], role: "sector reference point" }
  - { document: "QAA Glossary (not ingested)", named: "QAA's Glossary", citedIn: ["front matter"], role: "explains unfamiliar terms" }
  - { document: "QAA Academic integrity (not ingested)", named: "Academic integrity", citedIn: ["back matter: references"], role: "integrity, read with the GenAI theme" }
  - { document: "UN Sustainable Development Goals (external)", named: "United Nations Sustainable Development Goals (SDGs)", citedIn: ["1.18", "3.3", "back matter: references"], role: "frame for ESD" }
  - { document: "UNESCO (2017) Education for Sustainable Development Goals: Learning Objectives (external)", named: "UNESCO's ESD Learning Objectives", citedIn: ["1.19", "back matter: references"], role: "learning objectives for ESD pedagogy" }
  - { document: "World Economic Forum (2023) Future of Jobs Report (external)", named: "World Economic Forum Future Jobs Report (2023)", citedIn: ["1.22 (second)", "back matter: references"], role: "changing employer priorities" }
  - { document: "Equality Act 2010 (law)", named: "Equality Act 2010", citedIn: ["4.3"], role: "defines competence standards" }
  - { document: "public sector equality duty (law)", named: "public sector equality duty (PSED)", citedIn: ["1.6", "back matter: references (Government Equalities Office)"], role: "UK duty framing EDI in the subject" }
```

## Part B Terminology
<!-- The statement has no glossary of its own unless Part E says so; these are terms it defines in its text. -->

### B1 Concepts
<!-- label: both; status: drafted; basis: primary -->
```yaml
- { slug: "employability-entrepreneurship-and-enterprise-education", definition: "the cross-cutting theme, shortened to EEE, that builds the capacities students need for careers and for adding social, cultural and economic value (D1, 1.20, 1.21)", beneficiaryDefinition: "learning that prepares you for work and for creating value of your own", scopeNote: "the statement lists nine benefits it can bring (1.21)", category: "unknown", practices: ["education"] }
- { slug: "education-for-sustainable-development", definition: "building curricula and subject content that support sustainable development, as the statement takes it from the 2021 ESD guidance (D1, 1.18)", beneficiaryDefinition: "learning that helps you tackle social, environmental and economic problems for the future", scopeNote: "sustainable development itself is defined there as an ongoing, aspirational process (1.18)", category: "unknown", practices: ["education"] }
- { slug: "public-sector-equality-duty", definition: "the UK duty on public bodies, shortened to PSED, named as the immediate setting for equality in the subject (D1, 1.6)", beneficiaryDefinition: "the legal duty on public bodies to consider equality", scopeNote: "detailed in the Government Equalities Office guidance in the references", category: "unknown", practices: ["public administration"] }
```

### B2a Terms as the issuer defines them
<!-- label: source; status: drafted; basis: primary -->
```yaml
- { concept: "employability-entrepreneurship-and-enterprise-education", form: "employability, entrepreneurship and enterprise education (EEE)", lang: "en", partOfSpeech: "noun-phrase", termStatus: "preferred", register: "formal" }
- { concept: "education-for-sustainable-development", form: "Education for Sustainable Development (ESD)", lang: "en", partOfSpeech: "noun-phrase", termStatus: "preferred", register: "formal" }
- { concept: "public-sector-equality-duty", form: "public sector equality duty (PSED)", lang: "en", partOfSpeech: "noun-phrase", termStatus: "preferred", register: "formal" }
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
  title: "Subject Benchmark Statement Public Policy and Public Administration"
  edition: "April 2025 (first edition)"
  year: 2025
  url: unknown (the QAA page; the text came by stan's extraction)
  retrieved: "held from stan: wkspc2615-QAAVector mapped/public-policy-and-public-administration-2025/public-policy-and-public-administration-2025.raw.txt, commit 366bcb99a01118f2c4c3ebfa2a8337596bddc455; received 2026-10-03"
  licence: QAA copyright
  tier: primary
  readVia: direct
  held: 1d1e51d877ceed31d4f4079fecdf7394c6071e4fcaf3e0d781cc9f4fbe36c215
  heldFiles: ["wkspc2601-library/txt/qaa-2025-public-policy-public-administration-subject-benchmark-standard.txt", "wkspc2601-library/txt/qaa-2025-public-policy-public-administration-subject-benchmark-standard.norm.txt", "wkspc2601-library/records/qaa-2025-public-policy-public-administration-subject-benchmark-standard.chunks.json", "wkspc2601-library/records/qaa-2025-public-policy-public-administration-subject-benchmark-standard.held.json"]
  citedIn: [S1, S2, S3, S4, S4a, S5, S6, S7, SB1, SB2, SB3, SB4, SB5, SB6]
```

### D2 Research log
```yaml
- { ref: D1, tier: primary, consulted: 2026-10-03, pass: P1, outcome: "read whole, direct, from the normalised text; skeleton by tools/std_prep.py, document by tools/bm_build.py" }
- { ref: "ADAPT subj HESA stores, cah.json and hecos.json (designs/ingest/standards/subj/vocab)", tier: primary, consulted: 2026-10-03, pass: P1, outcome: "codes for statedSubjects and subjects" }
```

### D3 Wanted sources
```yaml
- { w: "W-std-0066", citation: "QAA (2021) Creating Inclusive Subject Communities: New QAA Advice", settles: ["SB6"], asked: "2026-10-03", state: "not held" }
- { w: "W-std-0026", citation: "QAA (2020) Characteristics Statement: Master's Degree", settles: ["SB6", "S5"], asked: "2026-10-03", state: "not held" }
- { w: "W-std-0095", citation: "The requirements of CMI, ICAPA, EAPAA and NASPAA", settles: ["SB5"], asked: "2026-10-03", state: "not held" }
```

## Part E Gaps and questions
- Rungs: two for honours, threshold (4.5, 15 items) and excellent (4.6, 16 items); no typical rung. Pattern differs from Psychology (three rungs).
- Master's: one list (4.7, 17 items) under a lead-in with no rung named; recorded as rung threshold, award master's, level fheq:7 by convention. Ids kept as the issuer's 4.7.b<k> (unique, own paragraph) rather than the .masters suffix, which the convention gives for shared table spans. The level is inferred: 4.7 names no level; 2.12 states FHEQ 7 / FQHEIS 11 only for integrated master's.
- 4.7's lead-in first sentence states three outcomes of its own (graduate outcomes, specialist command, independence in project work): recorded as statement 4.7 (find on that sentence), counted in the master's rung (18 records). Its force word is 'are expected to' (outside the five); recorded as will from the lead-in's second sentence (forceFrom 4.7). For P3.
- Lead-in wording new against Psychology: 'are expected to be able to demonstrate' (4.5, 4.6) and 'are expected to demonstrate ... They will also have extended' (4.7). 'Expected to' is outside the five force words: threshold items take force threshold (4.2 and 4.3 call these the minimum threshold standards); excellent items take will (from 'able to'); master's items will.
- gradeOf (inferred, by content, not position): 15 excellent items link to the threshold item below (no typical rung, so excellent links straight to threshold): 4.6.b1-4.5.b1, b2-b2, b3-b7, b4-b8, b5-b3, b6-b9, b7-b4, b8-b5, b9-b6, b10-b10, b11-b11, b12-b12, b13-b13, b15-b14, b16-b15. 4.6.b14 (academic practice and professional behaviour) has no threshold counterpart. All for P3.
- Duplicate numbering: the issuer numbers two paragraphs 1.22 (the second, after 1.25, on cross-sector skills); the skeleton keys it 1.22-2. Statement 1.22 is the first; the second is a plain-present paragraph, not a statement.
- Statements cut: 23 paragraph records (must 2: 1.22, 1.26; should 4: 1.12, 1.14, 4.2, 4.3; will 17) plus 49 rung records = 72. 3.3 and 3.7 are recorded on their stems (find); their list items are SB3 areas and practices, not statements.
- Not statements (D-std-0002 (a); template open point 5), listed for Abbott's P3 on plain-present provider norms: 1.13, 1.15, 1.16, 1.20, 1.22 (second), 3.8, 3.11, 3.12 (assessments courses include) and the 'can' and 'may' paragraphs 1.24, 1.25, 1.27, 1.28, 2.1, 2.9, 2.16, 2.17, 2.18, 2.22. 1.22 (second) and 1.20 state graduate or student outcomes in the plain present ('graduates recognise and demonstrate these skills'): a doubtful exclusion.
- Not statements, doubtful: 1.9 (seven purposes of the degree, 'to develop', no modal: an intended-outcomes list in all but form); 1.21 (nine things EEE 'can' do: claims about the theme, cut by the skeleton as candidates, dropped); 1.4 (degree types); 2.21 and 3.4, 3.5 ('will' used descriptively of typical practice); 4.1 (introduction to the rungs, 'will' framing).
- Included on 'will' with weak standard content, for P3: 1.10 and 1.17 (predictions about graduates' careers), 2.19 (student voice 'will form part of' review), 3.2 ('will typically learn').
- 2.23 'will need to' integrate accrediting bodies' requirements: an obliging phrase outside the five; force recorded as will (the issuer's own modal); nearest meaning must. For Abbott.
- 2.7 'it is expected that each level would see ...' and 'it would be expected that a student ... would be capable of': obliging wording outside the five, under the paragraph's will; recorded as will.
- 1.23 speaks of graduates generally (1.20 names undergraduate and postgraduate students); recorded at honours, fheq:6 (inferred) so the generic skill carries a level.
- Codes: hecos 100647 public policy and 100090 public administration match the subject names the statement gives (stated). CAH15-01-03 (social policy) and CAH15-03-01 (politics) are the CAH parents of those codes, inferred; hecos 100091 public services inferred from the subject's focus on public service delivery (1.2, 2.1). All inferred codes held back for P3.
- Foundation degrees: 1.4 says the statement is relevant to them and 2.6 notes public sector content in foundation degrees, but no standard is set at fheq:5; awardsCovered lists honours and master's only.
- Exit awards (2.9: CertHE at FHEQ 4 / FQHEIS 8; DipHE at FHEQ 5 / FQHEIS 9) recorded in S5 as cited levels and crosswalks; no standards at those levels.
- Theme id: generative AI recorded as theme:generative-ai (batch convention). The front matter names five themes; EEE is the issuer's name for the enterprise theme (theme:enterprise).
- Annex D thresholdAt link (S5): inferred; the statement does not map threshold or excellent to classes. Agent instructions point threshold items to Annex D 3rd cells and excellent items to 1st cells, by our reading of content (std:doc:qaa-fheq-2024-framework).
- Verbs: several rung items are noun phrases with no verb in their span (for example 4.5.b1, 4.5.b8, 4.6.b12); their verbs list is empty, as the check requires each verb to be in the span.
- Bodies: CMI, ICAPA, EAPAA and NASPAA (1.25) are named as accreditation routes; their requirements are not ingested (D3). The Local Government Association appears only as an advisory group member's affiliation (back matter), not recorded.
- References name EAPAA as 'EAPPA' (back matter typo); recorded as EAPAA, the body's name in 1.25.
- CQFW: not named in the statement; not cited in SB6. Levels checked against the FHEQ (4.15, 4.17, Annex D), FQHEIS (4.16) and the reference framework (R2 spine, R8).
- S9 commentary not researched in P1.
- ST-12: versions here run to the lengths the content needs; no length range is yet set.

---

## Change notes
- 0.1.2, 3 October 2026, 21:02: moved with its held text from UNI to the source library repo (`wkspc2601-library/ingested/standards/`, texts in `txt/`, records in `records/`); paths only (Abbott, 20:56; std N-0119).
- 0.1.1, 3 October 2026, 20:20: obliging words outside the five read as must, "ought to" as should, on statements outside the rungs, each marked on its force line (Abbott, 20:17; D-std-0016).
- 0.1.0, 2026-10-03 18:24: researched by run frame 0.1.1-draft and standards run layer 0.7.0-draft, std, run 0128 (P1); built by tools/bm_build.py.
