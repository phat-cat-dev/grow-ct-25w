---
id: std:doc:qaa-policing-in-partnership-with-2022-benchmarks
title: "Subject Benchmark Statement Policing"
profile: standards/subject-benchmark
profileVersion: 0.2.0-draft
issuer: QAA
kind: subject-benchmark
jurisdiction: [UK]
subjectScope: subjects
subjects:
  - { scheme: "hecos", code: "100486", label: "policing", basis: "stated" }
  - { scheme: "cah", code: "CAH16-01-01", label: "law", basis: "inferred" }
  - { scheme: "cah", code: "CAH16-01", label: "law", basis: "inferred" }
  - { scheme: "cah", code: "CAH16", label: "law", basis: "inferred" }
  - { scheme: "hecos", code: "100484", label: "criminology", basis: "inferred" }
  - { scheme: "hecos", code: "100483", label: "criminal justice", basis: "inferred" }
edition: "March 2022"
published: 2022-03
status: current
supersedes: "none-stated"
heldText: { method: sha256-bytes, raw: 340494318f152c022e244569f1d83083235f46e9d3294fe3f534ede5e6ffe403, normalised: 6d85ea00c9a6b807c3ab94e9954ea78b41a900c8b39448bb34eef9573c8786f0 }
heldTextStan: { method: sha256-stan, raw: 340494318f152c022e244569f1d83083235f46e9d3294fe3f534ede5e6ffe403, normalised: 11230b9e316c6d1a2c933cf9896e027df02d09137fcb0a526d273f2eda89ff36 }
licence: "QAA copyright; held for study, private to the project, never published"
series: "QAA Subject Benchmark Statements, 2022 series with cross-cutting themes (first edition for Policing, written in partnership with the College of Policing)"
awardsCovered: ["bachelor's with honours"]
levelsCovered: ["fheq:6", "fqheis:10"]
nations: ["England", "Wales", "Scotland", "Northern Ireland"]
parts:
  S: full
  B: "partial: no glossary in the document (it points to QAA's Glossary); terms it defines in passing"
  C: "not-applicable: the document sets expectations, not a procedure"
pins: { structure: 0.13.0-draft, template: 0.8.0-draft, benchmarkTemplate: 0.6.0-draft, runFrame: 0.1.1-draft, runLayer: 0.7.0-draft, standards: none yet, terminology: none yet }
lifecycle: drafted
researchedBy: run frame 0.1.1-draft; standards run layer 0.7.0-draft; std, run 0126 (tools/bm_build.py)
passes:
  P1: "2026-10-03 18:23"
  P2: "skipped: read direct from the held text; inferred codes and rung links are for P3"
  P3: open
version: 0.1.2
---

<!-- from INGEST wpk-0016-ingest-pd-template-standards.md 0.8.0-draft and wpk-0016-ingest-pd-template-standards-benchmark.md 0.6.0-draft; built by tools/bm_build.py from run-src/ -->
# Subject Benchmark Statement: Policing (QAA, March 2022)

> Run 0126, P1 by std. The issuer's words are held in the source library, `wkspc2601-library/txt/qaa-2022-policing-partnership-subject-benchmark-statement-standard.norm.txt`; each S4 record carries its statement in full (`source`) for language analysis, with its span. Paraphrases and versions are ours. Private to the project, never published. In front matter `status` is the issuer's; ours is `lifecycle`. Doubts are in Part E.

## Part 0 Summary

### 0.1 Agent definition
<!-- label: editorial; status: drafted; basis: primary -->
QAA's UK reference point for what an honours graduate in Policing should know and be able to do, written in partnership with the College of Policing. It sets one rung only, the threshold, as two lists (subject knowledge and skills; generic skills), and leaves achievement above it to Annex D of the qualifications frameworks. Reach for it when designing, reviewing or describing a Policing degree, including the College's licensed entry routes in England and Wales. It is not the National Policing Curriculum, not a licence condition and not regulation.

### 0.2 Summary
<!-- label: both; status: drafted; basis: primary -->
Published by QAA in March 2022 as the first Policing statement, it sets out the context of policing education in each UK nation (the PEQF entry routes in England and Wales, Police Scotland's own training, the PSNI degree), the purposes and characteristics of a degree, its distinctive features (design, employer involvement, progression, flexibility, partnership, monitoring), content, teaching and assessment, and 29 threshold standards for the bachelor's degree with honours (FHEQ level 6, FQHEIS level 10). No typical or excellent rung is stated. It treats equality, diversity and inclusion, accessibility, sustainability (with horizon scanning) and employability, and names the College of Policing as the professional body throughout.

## Part S Standard

### S1 Identity
<!-- label: source; status: drafted; basis: primary -->
```yaml
issuer: The Quality Assurance Agency for Higher Education
title: "Subject Benchmark Statement Policing"
edition: "March 2022"
dates:
  published: 2022-03
  other: []
kind: subject-benchmark
jurisdiction: [UK]
authority: "reference: a sector reference point; not a sector-recognised standard in England, a key reference point in Wales and Scotland, part of the quality requirements in Northern Ireland; reviewed by the College of Policing (D1, front matter)"
licence: "QAA copyright; the document gives no re-use terms in its text (D1, front matter)"
copyrightNotice: { text: "© The Quality Assurance Agency for Higher Education 2022", locator: "D1, index" }
```

### S2 Purpose and scope
<!-- label: source; status: drafted; basis: primary -->
```yaml
governs: "the bachelor's degree with honours in Policing: its context, purposes, distinctive features, content and delivery, and threshold standards"
appliesTo:
  awards: ["bachelor's with honours"]
  levels: ["fheq:6", "fqheis:10"]
  providers: ["UK higher education providers"]
whoMustUse: "none-stated; it is a reference point, not a requirement (D1, front matter)"
howUsed: ["design", "approval", "review", "other: external examining; PSRBs; information for prospective students and employers"]
doesNot: "it is not a national curriculum and does not prescribe teaching, learning or assessment; it carries no statutory or regulatory requirement (D1, front matter)"
beneficiary: the student
statedScope: "\"This document is a QAA Subject Benchmark Statement for Policing that defines what can be expected of a graduate in the subject, in terms of what they might know, do and understand at the end of their studies.\" (D1, front matter)"
statedSubjects:
  - { name: "Policing", locator: "(D1, front matter; 1.10)", kind: "subject", codes: [{ scheme: "hecos", code: "100486", label: "policing" }] }
  - { name: "BSc (Hons) Policing and Criminology (Applied Practice)", locator: "(D1, 1.8)", kind: "programme title", codes: [{ scheme: "hecos", code: "100486", label: "policing" }, { scheme: "hecos", code: "100484", label: "criminology" }] }
  - { name: "policing, criminal justice and criminology programmes", locator: "(D1, 2.14)", kind: "specialism", codes: [{ scheme: "hecos", code: "100484", label: "criminology" }, { scheme: "hecos", code: "100483", label: "criminal justice" }] }
subjects: see front matter (subjectScope subjects)
```

### S3 Structure
<!-- label: both; status: drafted; basis: primary -->
```yaml
components:
  - { number: "1.1", order: 3, componentType: paragraph, parent: "section 1", heading: "Context", gloss: "the stated mission of UK policing today" }
  - { number: "1.2", order: 4, componentType: paragraph, parent: "section 1", heading: "Context", gloss: "professionalising policing; core capabilities the service needs" }
  - { number: "1.3", order: 5, componentType: paragraph, parent: "section 1", heading: "Context: England and Wales", gloss: "the College of Policing and its standard-setting role" }
  - { number: "1.4", order: 6, componentType: paragraph, parent: "section 1", heading: "Context: England and Wales", gloss: "the PEQF and its three entry routes to constable" }
  - { number: "1.5", order: 7, componentType: paragraph, parent: "section 1", heading: "Context: England and Wales", gloss: "unlicensed Policing degrees still have value" }
  - { number: "1.6", order: 8, componentType: paragraph, parent: "section 1", heading: "Context: Scotland", gloss: "Scotland: no higher education entry route; Police Scotland College" }
  - { number: "1.7", order: 9, componentType: paragraph, parent: "section 1", heading: "Context: Scotland", gloss: "Scottish degrees designed with Police Scotland; special constables" }
  - { number: "1.8", order: 10, componentType: paragraph, parent: "section 1", heading: "Context: Northern Ireland", gloss: "Northern Ireland: the PSNI degree and graduate certificate" }
  - { number: "1.9", order: 11, componentType: paragraph, parent: "section 1", heading: "Context: Northern Ireland", gloss: "theory beneath applied practice; reflective, integrated curriculum" }
  - { number: "1.10", order: 12, componentType: paragraph, parent: "section 1", heading: "Purposes of a Policing degree", gloss: "the main purpose: competent policing professionals" }
  - { number: "1.11", order: 13, componentType: paragraph, parent: "section 1", heading: "Purposes of a Policing degree", gloss: "what programmes introduce students to" }
  - { number: "1.12", order: 14, componentType: paragraph, parent: "section 1", heading: "Purposes of a Policing degree", gloss: "a protected space for communication skills" }
  - { number: "1.13", order: 15, componentType: paragraph, parent: "section 1", heading: "Characteristics of a Policing degree", gloss: "constable capabilities aligned to honours level" }
  - { number: "1.14", order: 16, componentType: paragraph, parent: "section 1", heading: "Characteristics of a Policing degree", gloss: "alignment to CVF, Peelian Principles and Code of Ethics" }
  - { number: "1.15", order: 17, componentType: paragraph, parent: "section 1", heading: "Characteristics of a Policing degree", gloss: "what a holder of the degree can do" }
  - { number: "1.16", order: 18, componentType: paragraph, parent: "section 1", heading: "Characteristics of a Policing degree", gloss: "a degree that excludes no group" }
  - { number: "1.17", order: 19, componentType: paragraph, parent: "section 1", heading: "Equality, diversity and inclusion", gloss: "EDI at the core; equality duties; impact assessment" }
  - { number: "1.18", order: 20, componentType: paragraph, parent: "section 1", heading: "Equality, diversity and inclusion", gloss: "EDI and ethics embedded; students own their conduct" }
  - { number: "1.19", order: 21, componentType: paragraph, parent: "section 1", heading: "Equality, diversity and inclusion", gloss: "inclusive teaching and assessment planned from the start" }
  - { number: "1.20", order: 22, componentType: paragraph, parent: "section 1", heading: "Accessibility", gloss: "widening access; physical and digital barriers" }
  - { number: "1.21", order: 23, componentType: paragraph, parent: "section 1", heading: "Accessibility", gloss: "inclusion for all rather than target groups" }
  - { number: "1.22", order: 24, componentType: paragraph, parent: "section 1", heading: "Accessibility", gloss: "varied routes and flexible delivery for access" }
  - { number: "1.23", order: 25, componentType: stem, parent: "section 1", heading: "Accessibility", gloss: "accessibility law and what online provision lets students do" }
  - { number: "1.24", order: 26, componentType: paragraph, parent: "section 1", heading: "Sustainability and horizon scanning: Sustainability", gloss: "honours programmes and sustainable development" }
  - { number: "1.25", order: 27, componentType: paragraph, parent: "section 1", heading: "Sustainability and horizon scanning: Sustainability", gloss: "what education for sustainable development is" }
  - { number: "1.26", order: 28, componentType: stem, parent: "section 1", heading: "Sustainability and horizon scanning: Sustainability", gloss: "programmes designed with the SDGs; eight themes" }
  - { number: "1.27", order: 29, componentType: paragraph, parent: "section 1", heading: "Sustainability and horizon scanning: Horizon scanning", gloss: "future challenges feeding programme review" }
  - { number: "1.28", order: 30, componentType: paragraph, parent: "section 1", heading: "Sustainability and horizon scanning: Horizon scanning", gloss: "trends the College of Policing foresees" }
  - { number: "1.29", order: 31, componentType: paragraph, parent: "section 1", heading: "Sustainability and horizon scanning: Horizon scanning", gloss: "other changes that may reshape programmes" }
  - { number: "2.1", order: 33, componentType: paragraph, parent: "section 2", heading: "Design", gloss: "programmes designed for progressive learning" }
  - { number: "2.2", order: 34, componentType: stem, parent: "section 2", heading: "Design", gloss: "what programmes enable graduates to do" }
  - { number: "2.3", order: 35, componentType: paragraph, parent: "section 2", heading: "Design", gloss: "skills planned across every module" }
  - { number: "2.4", order: 36, componentType: paragraph, parent: "section 2", heading: "Design", gloss: "the National Policing Curriculum in licensed programmes" }
  - { number: "2.5", order: 37, componentType: paragraph, parent: "section 2", heading: "Employer involvement", gloss: "employer and professional body involvement; trust" }
  - { number: "2.6", order: 38, componentType: paragraph, parent: "section 2", heading: "Employer involvement", gloss: "staff associations and volunteers in programme review" }
  - { number: "2.7", order: 39, componentType: paragraph, parent: "section 2", heading: "Employer involvement", gloss: "engaging and upskilling the existing workforce" }
  - { number: "2.8", order: 40, componentType: paragraph, parent: "section 2", heading: "Employer involvement", gloss: "operational deployments; workplace tutors and assessors" }
  - { number: "2.9", order: 41, componentType: paragraph, parent: "section 2", heading: "Employer involvement", gloss: "research and practitioner-researchers shaping degrees" }
  - { number: "2.10", order: 42, componentType: paragraph, parent: "section 2", heading: "Progression", gloss: "progression year by year to the threshold" }
  - { number: "2.11", order: 43, componentType: paragraph, parent: "section 2", heading: "Progression", gloss: "joint honours students" }
  - { number: "2.12", order: 44, componentType: paragraph, parent: "section 2", heading: "Progression", gloss: "exit awards; four-year Scottish honours" }
  - { number: "2.13", order: 45, componentType: practice, parent: "section 2", heading: "Flexibility", gloss: "varied teaching methods; independent and work-based learning" }
  - { number: "2.14", order: 46, componentType: practice, parent: "section 2", heading: "Flexibility", gloss: "the final-year independent project or dissertation" }
  - { number: "2.15", order: 47, componentType: paragraph, parent: "section 2", heading: "Partnership", gloss: "what a partnership is" }
  - { number: "2.16", order: 48, componentType: paragraph, parent: "section 2", heading: "Partnership", gloss: "an institutional strategy for partnerships" }
  - { number: "2.17", order: 49, componentType: paragraph, parent: "section 2", heading: "Partnership", gloss: "partners and the national qualifications framework" }
  - { number: "2.18", order: 50, componentType: paragraph, parent: "section 2", heading: "Partnership", gloss: "awarding body safeguards for standards and experience" }
  - { number: "2.19", order: 51, componentType: paragraph, parent: "section 2", heading: "Partnership", gloss: "written agreements, due diligence and records" }
  - { number: "2.20", order: 52, componentType: paragraph, parent: "section 2", heading: "Monitoring and review", gloss: "monitoring and periodic review" }
  - { number: "2.21", order: 53, componentType: paragraph, parent: "section 2", heading: "Monitoring and review", gloss: "external reviewers in periodic review" }
  - { number: "2.22", order: 54, componentType: paragraph, parent: "section 2", heading: "Monitoring and review", gloss: "external examiners and threshold standards" }
  - { number: "2.23", order: 55, componentType: paragraph, parent: "section 2", heading: "Monitoring and review", gloss: "professional accreditation for vocational courses" }
  - { number: "3.1", order: 57, componentType: area, parent: "section 3", heading: "Content", gloss: "a constantly evolving subject" }
  - { number: "3.2", order: 58, componentType: area, parent: "section 3", heading: "Content", gloss: "five core themes for every policing award" }
  - { number: "3.3", order: 59, componentType: area, parent: "section 3", heading: "Content", gloss: "sixteen indicative topics" }
  - { number: "3.4", order: 60, componentType: practice, parent: "section 3", heading: "Teaching and learning", gloss: "from teacher-centred to learner-centred police education" }
  - { number: "3.5", order: 61, componentType: practice, parent: "section 3", heading: "Teaching and learning", gloss: "student-centred and experiential learning" }
  - { number: "3.6", order: 62, componentType: practice, parent: "section 3", heading: "Teaching and learning", gloss: "the Student as Producer model" }
  - { number: "3.7", order: 63, componentType: paragraph, parent: "section 3", heading: "Teaching and learning", gloss: "students as producers of knowledge" }
  - { number: "3.8", order: 64, componentType: paragraph, parent: "section 3", heading: "Teaching and learning", gloss: "academic and practitioner knowledge combined" }
  - { number: "3.9", order: 65, componentType: paragraph, parent: "section 3", heading: "Teaching and learning", gloss: "conditions for co-producing knowledge" }
  - { number: "3.10", order: 66, componentType: paragraph, parent: "section 3", heading: "Teaching and learning", gloss: "practice and academia merged; reflective practice" }
  - { number: "3.11", order: 67, componentType: paragraph, parent: "section 3", heading: "Assessment", gloss: "assessment in licensed PEQF programmes" }
  - { number: "3.12", order: 68, componentType: paragraph, parent: "section 3", heading: "Assessment", gloss: "other programmes may not need practical skills" }
  - { number: "3.13", order: 69, componentType: practice, parent: "section 3", heading: "Assessment", gloss: "applied assessment for every Policing degree" }
  - { number: "3.14", order: 70, componentType: stem, parent: "section 3", heading: "Assessment strategy", gloss: "co-designed assessment; strategy principles and safeguards" }
  - { number: "3.15", order: 71, componentType: practice, parent: "section 3", heading: "Assessment strategy: Forms of assessment", gloss: "varied, inclusive assessment with student voice" }
  - { number: "3.16", order: 72, componentType: practice, parent: "section 3", heading: "Assessment strategy: Forms of assessment", gloss: "full assessment information; balance of methods" }
  - { number: "3.17", order: 73, componentType: paragraph, parent: "section 3", heading: "Assessment strategy: Forms of assessment", gloss: "regular review of assessments" }
  - { number: "4.1", order: 75, componentType: paragraph, parent: "section 4", heading: "Introduction", gloss: "the threshold as a minimum for honours" }
  - { number: "4.2", order: 76, componentType: paragraph, parent: "section 4", heading: "Introduction", gloss: "most exceed it; Annex D for the classes" }
  - { number: "4.3", order: 77, componentType: stem, parent: "section 4", heading: "Threshold level: Subject knowledge, understanding and skills", gloss: "threshold subject knowledge, understanding and skills" }
  - { number: "4.4", order: 78, componentType: stem, parent: "section 4", heading: "Threshold level: Generic skills", gloss: "threshold generic skills" }
  - { number: "1", componentType: section, parent: none, heading: "Context and purposes of a Policing degree", gloss: "section 1" }
  - { number: "2", componentType: section, parent: none, heading: "Distinctive features of a Policing degree", gloss: "section 2" }
  - { number: "3", componentType: section, parent: none, heading: "Content, structure and delivery", gloss: "section 3" }
  - { number: "4", componentType: section, parent: none, heading: "Benchmark standards", gloss: "section 4" }
excluded:
  - { number: "none", heading: "Contents; About this Statement; How can I use this document?; Relationship to legislation; Additional sector reference points", kind: "other: front matter, read for S1, S2 and SB6" }
  - { number: "none", heading: "section heading lines (sections 1 to 4)", kind: "other: headings, recorded in S3 as sections" }
  - { number: "5", heading: "List of references", kind: "references" }
  - { number: "6", heading: "Membership of the Advisory Group", kind: "other: membership, College of Policing EDI note and acknowledgements; read for S1 and S8" }
```

### S4 Statements
<!-- label: both; status: drafted; basis: primary. Only standards (D-std-0002 (a)): 89 records. `source` is the issuer's statement exactly as its span holds it (D-std-0014). -->
```yaml
- id: qaa/policing-in-partnership-with-2022/1.10
  locator: { number: "1.10", headingPath: ["Context and purposes of a Policing degree", "Purposes of a Policing degree"] }
  span: { start: 13811, end: 14186 }
  source: "1.10 The primary purpose of a degree in Policing is to provide students with the knowledge, skills and behaviours to become competent policing professionals. Throughout their studies, students will develop and demonstrate understanding of the policing profession along with the regulatory and legal context within which policing and the criminal justice system is situated.\n\n"
  stem: none
  statementType: outcome
  rung: none
  force: will
  level: fheq:6
  appliesTo: "students of the subject"
  addressee: learner
  verbs: ["develop", "demonstrate"]
  about: "understanding of the profession and its legal setting"
  themes: [none]
  domain: understanding
  award: ["bachelor's with honours"]
  gradeOf: none
  paraphrase: "The degree's main aim is to equip students with the knowledge, skills and behaviours of competent policing professionals; across the course students will build and show an understanding of the profession and of the legal and regulatory setting of policing and criminal justice."
  quote: full   # the issuer's statement is in `source` (D-std-0014)
  audience: both
  subjects: inherited
- id: qaa/policing-in-partnership-with-2022/1.12
  locator: { number: "1.12", headingPath: ["Context and purposes of a Policing degree", "Purposes of a Policing degree"] }
  span: { start: 14591, end: 14959 }
  source: "1.12 Through the use of a protected learning environment in which to explore ideas and skillsets, students will develop effective communication and interpersonal skills. Utilising a wide range of learning scenarios will prepare students for the challenges and opportunities they are likely to encounter as policing professionals.\n\nCharacteristics of a Policing degree\n"
  stem: none
  statementType: outcome
  rung: none
  force: will
  level: fheq:6
  appliesTo: "students of the subject"
  addressee: learner
  verbs: ["develop"]
  about: "communication and interpersonal skills"
  themes: [none]
  domain: generic-skill
  award: ["bachelor's with honours"]
  gradeOf: none
  paraphrase: "In a safe space for trying out ideas and skills, students will develop effective communication and interpersonal skills, and many varied scenarios will ready them for what they meet as policing professionals."
  quote: full   # the issuer's statement is in `source` (D-std-0014)
  audience: both
  subjects: inherited
- id: qaa/policing-in-partnership-with-2022/1.15
  locator: { number: "1.15", headingPath: ["Context and purposes of a Policing degree", "Characteristics of a Policing degree"] }
  span: { start: 15782, end: 16790 }
  source: "1.15 The holder of a degree in Policing will be able to evaluate evidence, arguments and assumptions, to reach sound judgements and to communicate them effectively. Holders of such a degree will have the qualities needed for employment in situations requiring the exercise of personal responsibility, and evidence-informed decision-making in complex and unpredictable circumstances. As with all academic degrees, the holder should be able to develop analytically-sound research, evidence-based practice techniques and problem-solving skills that can be applied in their occupation, with Pepper et al (2021) highlighting how such problem-solving techniques and sound approaches to evidence-based research are increasingly important for application across local, regional and national policing. It is therefore important for the holder of a degree in Policing to be able to establish links between theory and professional practice, alongside the requisite application of transferable skills to the workplace.\n\n"
  stem: none
  statementType: outcome
  rung: none
  force: will
  level: fheq:6
  appliesTo: "holders of a Policing degree"
  addressee: learner
  verbs: ["evaluate", "reach", "communicate", "develop", "establish"]
  about: "judgement, evidence-informed decisions and linking theory to practice"
  themes: [none]
  domain: generic-skill
  award: ["bachelor's with honours"]
  gradeOf: none
  paraphrase: "A Policing graduate will be able to weigh evidence, arguments and assumptions, judge soundly and convey those judgements well, and will have the qualities for work that calls for personal responsibility and decisions based on evidence in complex, unpredictable conditions; the graduate should also be able to build sound research, evidence-based techniques and problem-solving skills, and to connect theory with professional practice."
  quote: full   # the issuer's statement is in `source` (D-std-0014)
  audience: both
  subjects: inherited
- id: qaa/policing-in-partnership-with-2022/1.16
  locator: { number: "1.16", headingPath: ["Context and purposes of a Policing degree", "Characteristics of a Policing degree"] }
  span: { start: 16790, end: 17157 }
  source: "1.16 The characteristics of a Policing degree should evidence a system that does not discriminate, stratify or exclude groups based on age, disability, gender reassignment, race, religion or belief, sex, sexual orientation, marriage and civil partnership, pregnancy and maternity or paternity, socioeconomic background or location.\n\nEquality, diversity and inclusion\n"
  stem: none
  statementType: expectation
  rung: none
  force: should
  level: none
  appliesTo: "those who design and run Policing degrees"
  addressee: provider
  verbs: ["evidence"]
  about: "a degree that excludes no group"
  themes: [none]
  domain: none
  award: ["bachelor's with honours"]
  gradeOf: none
  paraphrase: "The characteristics of a Policing degree should show a system that neither discriminates against, ranks nor shuts out any group on grounds of protected characteristics, socioeconomic background or location."
  quote: full   # the issuer's statement is in `source` (D-std-0014)
  audience: practitioner
  subjects: inherited
- id: qaa/policing-in-partnership-with-2022/1.17
  locator: { number: "1.17", headingPath: ["Context and purposes of a Policing degree", "Equality, diversity and inclusion"] }
  span: { start: 17157, end: 18005 }
  source: "1.17 Policing as a subject area has, at its core, a curriculum which embraces and champions equality, diversity and inclusion (EDI). All students and stakeholders must be treated openly, fairly, and with dignity and respect. Higher education institutions (HEIs), the College of Policing and local police forces are all subject to the Public Sector Equality Duty (PSED) under the Equality Act 2010; additional duties may also apply to bodies operating in Wales and Scotland. Institutions in Northern Ireland have similar obligations under Section 75 of the Northern Ireland Act 1998. Those designing and implementing Policing courses should also consider completing an Equality Impact Assessment (EIA). Where a course is being co-created in a partnership with a police force, the EIA may be completed collaboratively between the force and the HEI.\n\n"
  stem: none
  statementType: requirement
  rung: none
  force: must
  level: none
  appliesTo: "those who design and run Policing degrees"
  addressee: provider
  verbs: ["treated", "consider", "completing"]
  about: "fair treatment and equality impact assessment"
  themes: [theme:edi]
  domain: none
  award: ["bachelor's with honours"]
  gradeOf: none
  paraphrase: "The subject's curriculum champions equality, diversity and inclusion; every student and stakeholder must be treated with openness, fairness, dignity and respect, and those designing courses should also consider an Equality Impact Assessment, done jointly with the force where a course is co-created."
  quote: full   # the issuer's statement is in `source` (D-std-0014)
  audience: practitioner
  subjects: inherited
- id: qaa/policing-in-partnership-with-2022/1.18
  locator: { number: "1.18", headingPath: ["Context and purposes of a Policing degree", "Equality, diversity and inclusion"] }
  span: { start: 18005, end: 18742 }
  source: "1.18 EDI should be meaningful concepts that are embedded in culture and practice within the subject area, whether the degree programmes are operational or non-operational in design. Building upon the foundations of EDI across the curriculum is a common thread of ethics, recognising the importance of ethics within all aspects of policing. Ethical behaviour comes from the values, beliefs, attitudes and knowledge that guide the judgements of each individual. All students of Policing must understand the importance of ethics as exemplary standards, as a result translating their learning into everyday practice, by taking responsibility for their own professional behaviour and ensuring that they embody the highest ethical standards.\n\n"
  stem: none
  statementType: requirement
  rung: none
  force: must
  level: fheq:6
  appliesTo: "all students of Policing"
  addressee: both
  verbs: ["understand", "embody"]
  about: "ethics as the highest standard of conduct"
  themes: [theme:edi]
  domain: understanding
  award: ["bachelor's with honours"]
  gradeOf: none
  paraphrase: "EDI should be real concepts built into the culture and practice of the subject, with ethics running through the curriculum; all Policing students must understand why ethics matter as the highest standards and carry their learning into practice by owning their professional conduct."
  quote: full   # the issuer's statement is in `source` (D-std-0014)
  audience: both
  subjects: inherited
- id: qaa/policing-in-partnership-with-2022/1.19
  locator: { number: "1.19", headingPath: ["Context and purposes of a Policing degree", "Equality, diversity and inclusion"] }
  span: { start: 18742, end: 19797 }
  source: "1.19 Policing as a subject area recognises that students learn best in different ways and progress at different rates. Teaching inclusively enables all students, whatever their circumstances, to enjoy the fullest possible learning experience. It benefits all students because it values their individual strengths and contributions, and makes the learning experience richer and more diverse for everyone. Thorough the use of innovative curriculum design, students will experience a range of inclusive teaching styles and assessment procedures which will take them through all levels of study and maximise their potential to\n\n6\n\nsucceed. It should, however, be noted that offering a variety of teaching and assessment styles, while good practice, may not necessarily be 'inclusive' for all. As a result, teaching and assessment methods should be designed and planned to be inclusive and accessible from the outset, aligning with good practice, meeting and responding to student needs, while ensuring the fullest possible learning experience.\n\nAccessibility\n"
  stem: none
  statementType: expectation
  rung: none
  force: should
  level: none
  appliesTo: "those who design and run Policing degrees"
  addressee: provider
  verbs: ["designed", "planned"]
  about: "inclusive and accessible teaching and assessment"
  themes: [theme:edi, theme:accessibility]
  domain: none
  award: ["bachelor's with honours"]
  gradeOf: none
  paraphrase: "The subject accepts that students learn in different ways and at different rates; inclusive teaching benefits everyone, and because variety alone may still exclude some, methods of teaching and assessment should be planned from the start to be inclusive and accessible."
  quote: full   # the issuer's statement is in `source` (D-std-0014)
  audience: practitioner
  subjects: inherited
- id: qaa/policing-in-partnership-with-2022/1.20
  locator: { number: "1.20", headingPath: ["Context and purposes of a Policing degree", "Accessibility"] }
  span: { start: 19797, end: 20811 }
  source: "1.20 Providers of policing as a subject area must demonstrate their commitment to widening access and ensuring that all students can achieve their full potential. Students are entitled to a learning experience that respects diversity and enables their full participation, within an inclusive and supportive learning environment. When inclusion is referred to, it is often in relation to physical factors relating to the learning environment, such as access to a room or building, or printing resources with a particular font. As study becomes more blended or entirely online, there is also the need to explore and address digital divides, such as the ownership or access to digital devices and the subsequent connectivity of students (Cullinan et al, 2021). However, it is also important to consider the various elements of teaching and learning more holistically, to explore how to best enable Policing students to assimilate, process, recall and synthesise knowledge, in ways that are meaningful and effective.\n\n"
  stem: none
  statementType: requirement
  rung: none
  force: must
  level: none
  appliesTo: "those who design and run Policing degrees"
  addressee: provider
  verbs: ["demonstrate"]
  about: "commitment to widening access"
  themes: [theme:accessibility]
  domain: none
  award: ["bachelor's with honours"]
  gradeOf: none
  paraphrase: "Those offering Policing must show their commitment to widening access and to every student reaching their potential, attending to physical and digital barriers as well as to how students best take in and use knowledge."
  quote: full   # the issuer's statement is in `source` (D-std-0014)
  audience: practitioner
  subjects: inherited
- id: qaa/policing-in-partnership-with-2022/1.22
  locator: { number: "1.22", headingPath: ["Context and purposes of a Policing degree", "Accessibility"] }
  span: { start: 21244, end: 21864 }
  source: "1.22 The provision of policing routes that allow different pathways to promote accessibility to police education will assist in widening participation and increased opportunities - for example, offering programmes as a work-based learning route, a non-practice knowledge and skills focused route, or a route for those who have already acquired a degree and experience in a different discipline. Providers should place an emphasis on promoting flexibility of delivery methodology to support the accessibility of learning and the subsequent recruitment of a diverse workforce (more) representative of communities served.\n\n"
  stem: none
  statementType: expectation
  rung: none
  force: should
  level: none
  appliesTo: "those who design and run Policing degrees"
  addressee: provider
  verbs: ["place"]
  about: "flexible delivery and varied routes"
  themes: [theme:accessibility]
  domain: none
  award: ["bachelor's with honours"]
  gradeOf: none
  paraphrase: "Offering varied routes into police education widens participation; those offering the subject should stress flexible delivery so learning is accessible and the workforce recruited is more diverse and closer to the communities it serves."
  quote: full   # the issuer's statement is in `source` (D-std-0014)
  audience: practitioner
  subjects: inherited
- id: qaa/policing-in-partnership-with-2022/1.23.b1
  locator: { number: "1.23.b1", headingPath: ["Context and purposes of a Policing degree", "Accessibility"] }
  span: { start: 22403, end: 22579 }
  source: "access course support material online in order to work around unanticipated challenges due to illness, transport difficulties or dealing with family or other caring commitments"
  stem: "1.23"
  statementType: expectation
  rung: none
  force: should
  level: none
  appliesTo: "students, through the accessible provision of the course"
  addressee: provider
  verbs: ["access"]
  about: "course support available online"
  themes: [theme:accessibility]
  domain: none
  award: ["bachelor's with honours"]
  gradeOf: none
  paraphrase: "Students should be able to reach course support online so they can work round illness, travel problems or caring duties."
  quote: full   # the issuer's statement is in `source` (D-std-0014)
  audience: practitioner
  subjects: inherited
- id: qaa/policing-in-partnership-with-2022/1.23.b2
  locator: { number: "1.23.b2", headingPath: ["Context and purposes of a Policing degree", "Accessibility"] }
  span: { start: 22582, end: 22712 }
  source: "keep pace with the speed or complexity of information being provided due to the ability to pause, rewind and review course content"
  stem: "1.23"
  statementType: expectation
  rung: none
  force: should
  level: none
  appliesTo: "students, through the accessible provision of the course"
  addressee: provider
  verbs: ["keep"]
  about: "pausing and replaying content"
  themes: [theme:accessibility]
  domain: none
  award: ["bachelor's with honours"]
  gradeOf: none
  paraphrase: "Students should be able to keep up with fast or complex content because they can pause, rewind and revisit it."
  quote: full   # the issuer's statement is in `source` (D-std-0014)
  audience: practitioner
  subjects: inherited
- id: qaa/policing-in-partnership-with-2022/1.23.b3
  locator: { number: "1.23.b3", headingPath: ["Context and purposes of a Policing degree", "Accessibility"] }
  span: { start: 22715, end: 22833 }
  source: "review course content multiple times to deepen learning, particularly prior to assessments in a work-based environment"
  stem: "1.23"
  statementType: expectation
  rung: none
  force: should
  level: none
  appliesTo: "students, through the accessible provision of the course"
  addressee: provider
  verbs: ["review"]
  about: "revisiting content before work-based assessment"
  themes: [theme:accessibility]
  domain: none
  award: ["bachelor's with honours"]
  gradeOf: none
  paraphrase: "Students should be able to go over course content repeatedly to deepen learning, above all before assessments in the workplace."
  quote: full   # the issuer's statement is in `source` (D-std-0014)
  audience: practitioner
  subjects: inherited
- id: qaa/policing-in-partnership-with-2022/1.23.b4
  locator: { number: "1.23.b4", headingPath: ["Context and purposes of a Policing degree", "Accessibility"] }
  span: { start: 22836, end: 23074 }
  source: "reflect on course content and research concepts before potentially posing questions in a discussion forum (if available); this may suit certain learners who like or need time to deliberate, or students whose first language is not English."
  stem: "1.23"
  statementType: expectation
  rung: none
  force: should
  level: none
  appliesTo: "students, through the accessible provision of the course"
  addressee: provider
  verbs: ["reflect"]
  about: "time to reflect before posting questions"
  themes: [theme:accessibility]
  domain: none
  award: ["bachelor's with honours"]
  gradeOf: none
  paraphrase: "Students should be able to reflect on content and research ideas before asking questions in a discussion forum, which suits those who need time to think or who are working in a second language."
  quote: full   # the issuer's statement is in `source` (D-std-0014)
  audience: practitioner
  subjects: inherited
- id: qaa/policing-in-partnership-with-2022/1.26
  locator: { number: "1.26", headingPath: ["Context and purposes of a Policing degree", "Sustainability and horizon scanning: Sustainability"] }
  span: { start: 23769, end: 24002 }
  source: "Programmes should be designed with reference to the United Nations 17 sustainable development goals (SDGs) (United Nations, 2021) from which the following provide the opportunity to be explicitly placed within the Policing curricula:"
  stem: none
  statementType: expectation
  rung: none
  force: should
  level: none
  appliesTo: "those who design and run Policing degrees"
  addressee: provider
  verbs: ["designed"]
  about: "designing programmes with the SDGs"
  themes: [theme:esd]
  domain: none
  award: ["bachelor's with honours"]
  gradeOf: none
  paraphrase: "Programmes should be designed with the UN's 17 Sustainable Development Goals in mind; the statement names eight themes from them that a Policing curriculum can take up explicitly, from wellbeing and inclusive education to safe communities, environmental impact, just societies and partnership."
  quote: full   # the issuer's statement is in `source` (D-std-0014)
  audience: practitioner
  subjects: inherited
- id: qaa/policing-in-partnership-with-2022/1.27
  locator: { number: "1.27", headingPath: ["Context and purposes of a Policing degree", "Sustainability and horizon scanning: Horizon scanning"] }
  span: { start: 24690, end: 25075 }
  source: "1.27 To ensure a contemporary and relevant Policing Level 6 (FHEQ) or Level 10 (FQHEIS) qualification, the current and future challenges to policing, and the wider criminal justice system, should inform the ongoing review of programmes, thus enabling future graduates to be equipped with the required up-to-date knowledge, understanding and skills for their chosen or future careers.\n\n"
  stem: none
  statementType: expectation
  rung: none
  force: should
  level: none
  appliesTo: "those who design and run Policing degrees"
  addressee: provider
  verbs: ["inform"]
  about: "future challenges in programme review"
  themes: [none]
  domain: none
  award: ["bachelor's with honours"]
  gradeOf: none
  paraphrase: "To keep the honours qualification current, present and coming challenges to policing and criminal justice should shape the regular review of programmes, so that graduates leave with up-to-date knowledge and skills."
  quote: full   # the issuer's statement is in `source` (D-std-0014)
  audience: practitioner
  subjects: inherited
- id: qaa/policing-in-partnership-with-2022/2.2.b1
  locator: { number: "2.2.b1", headingPath: ["Distinctive features of a Policing degree", "Design"] }
  span: { start: 26316, end: 26442 }
  source: "comprehend the requirement for the highest professional standards when conducting lawful, ethical, safe and effective policing"
  stem: "2.2"
  statementType: outcome
  rung: none
  force: will
  level: fheq:6
  appliesTo: "graduates of the subject"
  addressee: learner
  verbs: ["comprehend"]
  about: "the highest professional standards"
  themes: [none]
  domain: understanding
  award: ["bachelor's with honours"]
  gradeOf: none
  paraphrase: "Graduates will grasp why lawful, ethical, safe and effective policing demands the highest professional standards."
  quote: full   # the issuer's statement is in `source` (D-std-0014)
  audience: both
  subjects: inherited
- id: qaa/policing-in-partnership-with-2022/2.2.b2
  locator: { number: "2.2.b2", headingPath: ["Distinctive features of a Policing degree", "Design"] }
  span: { start: 26445, end: 26476 }
  source: "conduct evidence-based research"
  stem: "2.2"
  statementType: outcome
  rung: none
  force: will
  level: fheq:6
  appliesTo: "graduates of the subject"
  addressee: learner
  verbs: ["conduct"]
  about: "evidence-based research"
  themes: [none]
  domain: subject-skill
  award: ["bachelor's with honours"]
  gradeOf: none
  paraphrase: "Graduates will be able to carry out research grounded in evidence."
  quote: full   # the issuer's statement is in `source` (D-std-0014)
  audience: both
  subjects: inherited
- id: qaa/policing-in-partnership-with-2022/2.2.b3
  locator: { number: "2.2.b3", headingPath: ["Distinctive features of a Policing degree", "Design"] }
  span: { start: 26479, end: 26550 }
  source: "develop an understanding of evidence-based policing and problem solving"
  stem: "2.2"
  statementType: outcome
  rung: none
  force: will
  level: fheq:6
  appliesTo: "graduates of the subject"
  addressee: learner
  verbs: ["develop"]
  about: "evidence-based policing and problem solving"
  themes: [none]
  domain: understanding
  award: ["bachelor's with honours"]
  gradeOf: none
  paraphrase: "Graduates will come to understand evidence-based policing and problem-solving."
  quote: full   # the issuer's statement is in `source` (D-std-0014)
  audience: both
  subjects: inherited
- id: qaa/policing-in-partnership-with-2022/2.2.b4
  locator: { number: "2.2.b4", headingPath: ["Distinctive features of a Policing degree", "Design"] }
  span: { start: 26553, end: 26624 }
  source: "develop knowledge of a number of front-line professional policing areas"
  stem: "2.2"
  statementType: outcome
  rung: none
  force: will
  level: fheq:6
  appliesTo: "graduates of the subject"
  addressee: learner
  verbs: ["develop"]
  about: "front-line policing areas"
  themes: [none]
  domain: knowledge
  award: ["bachelor's with honours"]
  gradeOf: none
  paraphrase: "Graduates will gain knowledge of several areas of front-line professional policing."
  quote: full   # the issuer's statement is in `source` (D-std-0014)
  audience: both
  subjects: inherited
- id: qaa/policing-in-partnership-with-2022/2.2.b5
  locator: { number: "2.2.b5", headingPath: ["Distinctive features of a Policing degree", "Design"] }
  span: { start: 26627, end: 26694 }
  source: "proactively embed equality, diversity, inclusivity and human rights"
  stem: "2.2"
  statementType: outcome
  rung: none
  force: will
  level: fheq:6
  appliesTo: "graduates of the subject"
  addressee: learner
  verbs: ["embed"]
  about: "equality, diversity, inclusion and human rights"
  themes: [none]
  domain: subject-skill
  award: ["bachelor's with honours"]
  gradeOf: none
  paraphrase: "Graduates will actively build equality, diversity, inclusivity and human rights into what they do."
  quote: full   # the issuer's statement is in `source` (D-std-0014)
  audience: both
  subjects: inherited
- id: qaa/policing-in-partnership-with-2022/2.2.b6
  locator: { number: "2.2.b6", headingPath: ["Distinctive features of a Policing degree", "Design"] }
  span: { start: 26697, end: 26763 }
  source: "understand the importance of wellbeing and professional resilience"
  stem: "2.2"
  statementType: outcome
  rung: none
  force: will
  level: fheq:6
  appliesTo: "graduates of the subject"
  addressee: learner
  verbs: ["understand"]
  about: "wellbeing and professional resilience"
  themes: [none]
  domain: understanding
  award: ["bachelor's with honours"]
  gradeOf: none
  paraphrase: "Graduates will understand why wellbeing and professional resilience matter."
  quote: full   # the issuer's statement is in `source` (D-std-0014)
  audience: both
  subjects: inherited
- id: qaa/policing-in-partnership-with-2022/2.2.b7
  locator: { number: "2.2.b7", headingPath: ["Distinctive features of a Policing degree", "Design"] }
  span: { start: 26766, end: 26833 }
  source: "understand the concepts of digital policing and cyber-enabled crime"
  stem: "2.2"
  statementType: outcome
  rung: none
  force: will
  level: fheq:6
  appliesTo: "graduates of the subject"
  addressee: learner
  verbs: ["understand"]
  about: "digital policing and cyber-enabled crime"
  themes: [none]
  domain: knowledge
  award: ["bachelor's with honours"]
  gradeOf: none
  paraphrase: "Graduates will understand digital policing and crime enabled by cyber means."
  quote: full   # the issuer's statement is in `source` (D-std-0014)
  audience: both
  subjects: inherited
- id: qaa/policing-in-partnership-with-2022/2.2.b8
  locator: { number: "2.2.b8", headingPath: ["Distinctive features of a Policing degree", "Design"] }
  span: { start: 26836, end: 26913 }
  source: "develop comprehensive knowledge of policing, criminal justice and criminology"
  stem: "2.2"
  statementType: outcome
  rung: none
  force: will
  level: fheq:6
  appliesTo: "graduates of the subject"
  addressee: learner
  verbs: ["develop"]
  about: "policing, criminal justice and criminology"
  themes: [none]
  domain: knowledge
  award: ["bachelor's with honours"]
  gradeOf: none
  paraphrase: "Graduates will gain thorough knowledge of policing, criminal justice and criminology."
  quote: full   # the issuer's statement is in `source` (D-std-0014)
  audience: both
  subjects: inherited
- id: qaa/policing-in-partnership-with-2022/2.2.b9
  locator: { number: "2.2.b9", headingPath: ["Distinctive features of a Policing degree", "Design"] }
  span: { start: 26916, end: 26978 }
  source: "understand the criminal justice system in relation to policing"
  stem: "2.2"
  statementType: outcome
  rung: none
  force: will
  level: fheq:6
  appliesTo: "graduates of the subject"
  addressee: learner
  verbs: ["understand"]
  about: "the criminal justice system and policing"
  themes: [none]
  domain: understanding
  award: ["bachelor's with honours"]
  gradeOf: none
  paraphrase: "Graduates will understand how the criminal justice system relates to policing."
  quote: full   # the issuer's statement is in `source` (D-std-0014)
  audience: both
  subjects: inherited
- id: qaa/policing-in-partnership-with-2022/2.2.b10
  locator: { number: "2.2.b10", headingPath: ["Distinctive features of a Policing degree", "Design"] }
  span: { start: 26981, end: 27070 }
  source: "develop knowledge of legislation, powers, policy and application in professional practice"
  stem: "2.2"
  statementType: outcome
  rung: none
  force: will
  level: fheq:6
  appliesTo: "graduates of the subject"
  addressee: learner
  verbs: ["develop"]
  about: "legislation, powers and policy in practice"
  themes: [none]
  domain: knowledge
  award: ["bachelor's with honours"]
  gradeOf: none
  paraphrase: "Graduates will know legislation, police powers and policy and how they apply in professional practice."
  quote: full   # the issuer's statement is in `source` (D-std-0014)
  audience: both
  subjects: inherited
- id: qaa/policing-in-partnership-with-2022/2.2.b11
  locator: { number: "2.2.b11", headingPath: ["Distinctive features of a Policing degree", "Design"] }
  span: { start: 27073, end: 27220 }
  source: "recognise the fundamental responsibility of the police service to identify and provide professional support to those who are vulnerable and at risk"
  stem: "2.2"
  statementType: outcome
  rung: none
  force: will
  level: fheq:6
  appliesTo: "graduates of the subject"
  addressee: learner
  verbs: ["recognise"]
  about: "protecting people who are vulnerable or at risk"
  themes: [none]
  domain: understanding
  award: ["bachelor's with honours"]
  gradeOf: none
  paraphrase: "Graduates will recognise that the police service has a basic duty to identify and professionally support people who are vulnerable or at risk."
  quote: full   # the issuer's statement is in `source` (D-std-0014)
  audience: both
  subjects: inherited
- id: qaa/policing-in-partnership-with-2022/2.2.b12
  locator: { number: "2.2.b12", headingPath: ["Distinctive features of a Policing degree", "Design"] }
  span: { start: 27223, end: 27337 }
  source: "select and apply relevant specialist strategies and techniques to support individuals in need of public protection"
  stem: "2.2"
  statementType: outcome
  rung: none
  force: will
  level: fheq:6
  appliesTo: "graduates of the subject"
  addressee: learner
  verbs: ["select", "apply"]
  about: "specialist strategies for public protection"
  themes: [none]
  domain: subject-skill
  award: ["bachelor's with honours"]
  gradeOf: none
  paraphrase: "Graduates will be able to choose and use suitable specialist strategies and techniques to support people who need public protection."
  quote: full   # the issuer's statement is in `source` (D-std-0014)
  audience: both
  subjects: inherited
- id: qaa/policing-in-partnership-with-2022/2.2.b13
  locator: { number: "2.2.b13", headingPath: ["Distinctive features of a Policing degree", "Design"] }
  span: { start: 27340, end: 27417 }
  source: "develop knowledge of national policing strategies, such as counter terrorism."
  stem: "2.2"
  statementType: outcome
  rung: none
  force: will
  level: fheq:6
  appliesTo: "graduates of the subject"
  addressee: learner
  verbs: ["develop"]
  about: "national strategies such as counter terrorism"
  themes: [none]
  domain: knowledge
  award: ["bachelor's with honours"]
  gradeOf: none
  paraphrase: "Graduates will know national policing strategies, counter terrorism among them."
  quote: full   # the issuer's statement is in `source` (D-std-0014)
  audience: both
  subjects: inherited
- id: qaa/policing-in-partnership-with-2022/2.3
  locator: { number: "2.3", headingPath: ["Distinctive features of a Policing degree", "Design"] }
  span: { start: 27418, end: 28002 }
  source: "2.3 Programme design should be holistically planned to develop, assess and enhance graduate skills and attributes, while embedding a wide range of skills transferable to policing and other professions. As a professional subject, the design across all modules in Policing should consider ongoing reflective practice; critical thinking; decision-making; skills of communication; ethics; equality, diversity and inclusion; evidence-based practice; problem solving techniques; approaches to leadership (for example, inclusive, systematic, transactional, transformational); and teamwork.\n\n"
  stem: none
  statementType: expectation
  rung: none
  force: should
  level: none
  appliesTo: "those who design and run Policing degrees"
  addressee: provider
  verbs: ["planned", "consider"]
  about: "skills planned across all modules"
  themes: [none]
  domain: none
  award: ["bachelor's with honours"]
  gradeOf: none
  paraphrase: "Programme design should be planned as a whole to build, assess and strengthen graduate skills that transfer to policing and beyond; every module should take account of reflection, critical thinking, decisions, communication, ethics, EDI, evidence-based practice, problem solving, leadership and teamwork."
  quote: full   # the issuer's statement is in `source` (D-std-0014)
  audience: practitioner
  subjects: inherited
- id: qaa/policing-in-partnership-with-2022/2.4
  locator: { number: "2.4", headingPath: ["Distinctive features of a Policing degree", "Design"] }
  span: { start: 28002, end: 28457 }
  source: "2.4 The College of Policing sets out the NPC requirements for professionally-licensed programmes. If the programme is seeking licensing by the professional body, the design must ensure that this curriculum is built into the degree programme and will map learning effectively to ensure that all elements of the curriculum are incorporated in the design. There is also a formal professional body process for regular and annual review.\n\nEmployer involvement\n"
  stem: none
  statementType: requirement
  rung: none
  force: must
  level: none
  appliesTo: "those who design and run Policing degrees"
  addressee: provider
  verbs: ["ensure", "map"]
  about: "the National Policing Curriculum in licensed programmes"
  themes: [none]
  domain: none
  award: ["bachelor's with honours"]
  gradeOf: none
  paraphrase: "For a programme seeking the professional body's licence, the design must build the College of Policing's National Policing Curriculum into the degree and map learning so every element is covered; licensed programmes are also reviewed regularly and yearly by the body."
  quote: full   # the issuer's statement is in `source` (D-std-0014)
  audience: practitioner
  subjects: inherited
- id: qaa/policing-in-partnership-with-2022/2.6
  locator: { number: "2.6", headingPath: ["Distinctive features of a Policing degree", "Employer involvement"] }
  span: { start: 29013, end: 30079 }
  source: "2.6 The role of staff associations is also critical in landing any message across policing. The staff associations represent all across policing and so those who join the service and\n\n9\n\nare trained following the PEQF model, will require support and understanding from their representative peers. In addition, with the recognition of the range of roles and importance of volunteers in policing (along with the potential benefits of volunteering to higher education studies), volunteers should also be formally represented in consultations developing and reviewing programmes. For example, students undertaking a Professional Policing Degree who also volunteer (such as special constables or police support volunteers) may be an additional means of representing the views and needs of those who volunteer within policing. The changing emphasis in the careers marketplace, and the expectations of a modern workforce, has reinforced the argument for a closer relationship and understanding between the intrinsic value of a degree-level qualification and the employer.\n\n"
  stem: none
  statementType: expectation
  rung: none
  force: should
  level: none
  appliesTo: "those who design and run Policing degrees"
  addressee: provider
  verbs: ["represented"]
  about: "volunteers in programme consultation"
  themes: [none]
  domain: none
  award: ["bachelor's with honours"]
  gradeOf: none
  paraphrase: "Staff associations matter for change across policing, and volunteers should also be formally represented when programmes are developed and reviewed, for example through students who volunteer as special constables."
  quote: full   # the issuer's statement is in `source` (D-std-0014)
  audience: practitioner
  subjects: inherited
- id: qaa/policing-in-partnership-with-2022/2.9
  locator: { number: "2.9", headingPath: ["Distinctive features of a Policing degree", "Employer involvement"] }
  span: { start: 31355, end: 31779 }
  source: "2.9 Contemporary and discipline-specific research also plays a crucial part forming the creation and informing employers of the benefits of a degree in Policing. Such an evidence-based approach for those creating degrees must mirror other professions where experienced practitioner-researchers inform professional practice, increasing the validity and transferability of subject-specific graduate level skills.\n\nProgression\n"
  stem: none
  statementType: requirement
  rung: none
  force: must
  level: none
  appliesTo: "those who design and run Policing degrees"
  addressee: provider
  verbs: ["mirror"]
  about: "practitioner-researchers informing degree design"
  themes: [none]
  domain: none
  award: ["bachelor's with honours"]
  gradeOf: none
  paraphrase: "Current research in the discipline shapes how degrees are made and shows employers their worth; an evidence-based approach to creating degrees must follow other professions where experienced practitioner-researchers inform practice."
  quote: full   # the issuer's statement is in `source` (D-std-0014)
  audience: practitioner
  subjects: inherited
- id: qaa/policing-in-partnership-with-2022/2.11
  locator: { number: "2.11", headingPath: ["Distinctive features of a Policing degree", "Progression"] }
  span: { start: 32292, end: 32613 }
  source: "2.11 Joint honours undergraduates will achieve core elements of the specific and generic skills for the subject, and will add others according to the subjects covered in joint courses. Additionally, they may explore the overlap between their two subject areas, creating further opportunities for interdisciplinary study.\n"
  stem: none
  statementType: outcome
  rung: none
  force: will
  level: fheq:6
  appliesTo: "joint honours students"
  addressee: learner
  verbs: ["achieve", "add"]
  about: "joint honours students and the core skills"
  themes: [none]
  domain: subject-skill
  award: ["bachelor's with honours"]
  gradeOf: none
  paraphrase: "Joint honours students will reach the core subject-specific and generic skills of Policing and add others from their second subject, and may explore where the two overlap."
  quote: full   # the issuer's statement is in `source` (D-std-0014)
  audience: both
  subjects: inherited
- id: qaa/policing-in-partnership-with-2022/2.14
  locator: { number: "2.14", headingPath: ["Distinctive features of a Policing degree", "Flexibility"] }
  span: { start: 34299, end: 35021 }
  source: "2.14 In the final year of most policing, criminal justice and criminology programmes offered across England, Wales, Scotland (4th year) and Northern Ireland, students are required to design, undertake and complete a piece of independent research in the form of a problem-based project or dissertation. These projects or dissertations are normally expected to demonstrate a student's maturation of ability; to navigate the practical, ethical and organisational dimensions of policing, criminal justice or criminological research; to critically engage with research evidence, academic literature, legislation, and policy; and to make meaningful connections between research, practice and relevant policy areas.\n\nPartnership\n"
  stem: none
  statementType: requirement
  rung: none
  force: must
  level: fheq:6
  appliesTo: "final-year students on most policing, criminal justice and criminology programmes"
  addressee: learner
  verbs: ["design", "undertake", "complete"]
  about: "the independent final-year project or dissertation"
  themes: [none]
  domain: subject-skill
  award: ["bachelor's with honours"]
  gradeOf: none
  paraphrase: "In the last year of most programmes in policing, criminal justice or criminology, students must design, carry out and finish an independent problem-based project or dissertation, normally showing maturity, handling the practical, ethical and organisational sides of research, engaging critically with evidence, literature, law and policy, and linking research to practice and policy."
  quote: full   # the issuer's statement is in `source` (D-std-0014)
  audience: both
  subjects: inherited
- id: qaa/policing-in-partnership-with-2022/2.16
  locator: { number: "2.16", headingPath: ["Distinctive features of a Policing degree", "Partnership"] }
  span: { start: 35484, end: 36086 }
  source: "2.16 There should be a clear institutional strategy for working in partnership with other agencies, which assists in setting the parameters and provides guidance for those considering entering into partnership arrangements. Such arrangements may apply to the delivery of whole courses or to different elements of courses, including work placements, with institutions recognising the value of work-based learning to student employability (QAA, 2018). Consequently, alternative sites and contexts for learning or assessment, or specialist support, resources or facilities for learning, may be required.\n\n"
  stem: none
  statementType: expectation
  rung: none
  force: should
  level: none
  appliesTo: "those who design and run Policing degrees"
  addressee: provider
  verbs: ["provides"]
  about: "an institutional strategy for partnerships"
  themes: [none]
  domain: none
  award: ["bachelor's with honours"]
  gradeOf: none
  paraphrase: "There should be a clear institutional strategy for partnership with other agencies that guides anyone entering such arrangements, which may cover whole courses or parts such as placements and may call for other sites, support or facilities."
  quote: full   # the issuer's statement is in `source` (D-std-0014)
  audience: practitioner
  subjects: inherited
- id: qaa/policing-in-partnership-with-2022/2.17
  locator: { number: "2.17", headingPath: ["Distinctive features of a Policing degree", "Partnership"] }
  span: { start: 36086, end: 36366 }
  source: "2.17 Partners involved in the co-creation and/or completion of policing educational awards must meet the requirements of the relevant national qualification framework and it should be the responsibility of the awarding organisation to ensure that the required standards are met.\n\n"
  stem: none
  statementType: requirement
  rung: none
  force: must
  level: none
  appliesTo: "those who design and run Policing degrees"
  addressee: provider
  verbs: ["meet", "ensure"]
  about: "partners and the national qualifications framework"
  themes: [none]
  domain: none
  award: ["bachelor's with honours"]
  gradeOf: none
  paraphrase: "Partners co-creating or delivering policing awards must satisfy the national qualifications framework that applies, and the awarding organisation should be responsible for making sure the standards are met."
  quote: full   # the issuer's statement is in `source` (D-std-0014)
  audience: practitioner
  subjects: inherited
- id: qaa/policing-in-partnership-with-2022/2.18
  locator: { number: "2.18", headingPath: ["Distinctive features of a Policing degree", "Partnership"] }
  span: { start: 36366, end: 36953 }
  source: "2.18 The awarding body must also ensure arrangements are in place for measures to maintain the academic standard of the policing qualification that is being awarded. Partnership input into the policing award should also provide an opportunity for enhancing the experience of the student. In particular, where a partnership arrangement exists where part or all of the course requirements are delivered by other agencies, there should be an\n\n11\n\neffective process in place for the management and oversight of all aspects of the student experience to ensure it is of the required quality.\n\n"
  stem: none
  statementType: requirement
  rung: none
  force: must
  level: none
  appliesTo: "those who design and run Policing degrees"
  addressee: provider
  verbs: ["ensure"]
  about: "standards and student experience in partnerships"
  themes: [none]
  domain: none
  award: ["bachelor's with honours"]
  gradeOf: none
  paraphrase: "The awarding body must make arrangements to keep the academic standard of the policing award; partnership input should also enrich the student experience, and where other agencies deliver some or all of the course there should be an effective process for managing and overseeing that experience."
  quote: full   # the issuer's statement is in `source` (D-std-0014)
  audience: practitioner
  subjects: inherited
- id: qaa/policing-in-partnership-with-2022/2.19
  locator: { number: "2.19", headingPath: ["Distinctive features of a Policing degree", "Partnership"] }
  span: { start: 36953, end: 37456 }
  source: "2.19 Partnerships between awarding bodies for police qualifications should include legally-binding written agreements with detailed arrangements, including any risks involved. These should be subject to due diligence enquiries during the partnership and prior to any renewal. In terms of records kept, governance procedures should be recorded and kept up-to-date, with awarding institutions monitoring and evaluating all aspects of partnership arrangements on a continuous basis.\n\nMonitoring and review\n"
  stem: none
  statementType: expectation
  rung: none
  force: should
  level: none
  appliesTo: "those who design and run Policing degrees"
  addressee: provider
  verbs: ["include"]
  about: "written partnership agreements and due diligence"
  themes: [none]
  domain: none
  award: ["bachelor's with honours"]
  gradeOf: none
  paraphrase: "Partnerships for police qualifications should rest on legally binding written agreements setting out detailed arrangements and risks, with due diligence during the partnership and before renewal, governance recorded and kept current, and continuous monitoring by the awarding institution."
  quote: full   # the issuer's statement is in `source` (D-std-0014)
  audience: practitioner
  subjects: inherited
- id: qaa/policing-in-partnership-with-2022/3.2.b1
  locator: { number: "3.2.b1", headingPath: ["Content, structure and delivery", "Content"] }
  span: { start: 40260, end: 40487 }
  source: "Impartiality - The course should be designed so students can understand the context of the profession, upholding professional policing standards, while making decisions on objective impartial criteria without bias or prejudice."
  stem: "3.2"
  statementType: expectation
  rung: none
  force: should
  level: none
  appliesTo: "those who design and run Policing degrees"
  addressee: provider
  verbs: ["designed", "understand", "upholding", "making"]
  about: "impartiality"
  themes: [none]
  domain: none
  award: ["bachelor's with honours"]
  gradeOf: none
  paraphrase: "Impartiality: the course should be designed so that students understand the context of the profession, uphold its standards and decide on objective grounds free of bias."
  quote: full   # the issuer's statement is in `source` (D-std-0014)
  audience: practitioner
  subjects: inherited
- id: qaa/policing-in-partnership-with-2022/3.2.b2
  locator: { number: "3.2.b2", headingPath: ["Content, structure and delivery", "Content"] }
  span: { start: 40490, end: 40707 }
  source: "Integrity - Course contents should reflect the highest standards required by those working within policing, including being a role model, which will affect the importance of meeting the highest professional standards."
  stem: "3.2"
  statementType: expectation
  rung: none
  force: should
  level: none
  appliesTo: "those who design and run Policing degrees"
  addressee: provider
  verbs: ["reflect"]
  about: "integrity"
  themes: [none]
  domain: none
  award: ["bachelor's with honours"]
  gradeOf: none
  paraphrase: "Integrity: course content should reflect the highest standards expected of people in policing, including acting as a role model."
  quote: full   # the issuer's statement is in `source` (D-std-0014)
  audience: practitioner
  subjects: inherited
- id: qaa/policing-in-partnership-with-2022/3.2.b3
  locator: { number: "3.2.b3", headingPath: ["Content, structure and delivery", "Content"] }
  span: { start: 40710, end: 40878 }
  source: "Public service - Course content should reflect the fact that those within policing have the responsibility to ensure they act in the best interests of society as whole."
  stem: "3.2"
  statementType: expectation
  rung: none
  force: should
  level: none
  appliesTo: "those who design and run Policing degrees"
  addressee: provider
  verbs: ["reflect", "act"]
  about: "public service"
  themes: [none]
  domain: none
  award: ["bachelor's with honours"]
  gradeOf: none
  paraphrase: "Public service: course content should reflect that people in policing are responsible for acting in the best interests of society as a whole."
  quote: full   # the issuer's statement is in `source` (D-std-0014)
  audience: practitioner
  subjects: inherited
- id: qaa/policing-in-partnership-with-2022/3.2.b4
  locator: { number: "3.2.b4", headingPath: ["Content, structure and delivery", "Content"] }
  span: { start: 40881, end: 41106 }
  source: "Transparency - Policing awards should be designed to ensure that students understand the need for those working or volunteering within policing to be transparent in their actions, decisions and communications with all people."
  stem: "3.2"
  statementType: expectation
  rung: none
  force: should
  level: none
  appliesTo: "those who design and run Policing degrees"
  addressee: provider
  verbs: ["designed", "understand"]
  about: "transparency"
  themes: [none]
  domain: none
  award: ["bachelor's with honours"]
  gradeOf: none
  paraphrase: "Transparency: policing awards should be designed so students understand why those working or volunteering in policing need to be open in their actions, decisions and communications."
  quote: full   # the issuer's statement is in `source` (D-std-0014)
  audience: practitioner
  subjects: inherited
- id: qaa/policing-in-partnership-with-2022/3.2.b5
  locator: { number: "3.2.b5", headingPath: ["Content, structure and delivery", "Content"] }
  span: { start: 41109, end: 41265 }
  source: "Diversity - Policing awards should be designed to include the need for students to understand and champion equality, diversity and inclusion within society."
  stem: "3.2"
  statementType: expectation
  rung: none
  force: should
  level: none
  appliesTo: "those who design and run Policing degrees"
  addressee: provider
  verbs: ["designed", "include", "understand", "champion"]
  about: "diversity"
  themes: [none]
  domain: none
  award: ["bachelor's with honours"]
  gradeOf: none
  paraphrase: "Diversity: policing awards should be designed so students understand and champion equality, diversity and inclusion in society."
  quote: full   # the issuer's statement is in `source` (D-std-0014)
  audience: practitioner
  subjects: inherited
- id: qaa/policing-in-partnership-with-2022/3.11
  locator: { number: "3.11", headingPath: ["Content, structure and delivery", "Assessment"] }
  span: { start: 46154, end: 47067 }
  source: "3.11 Assessment of students undertaking degrees in Policing will be partially determined by whether the degree is a licensed programme of study as defined within the PEQF or not. Policing degrees that fall under the category of College of Policing licensed PEQF programmes will require assessment strategies that blend the theoretical learning with the application of the learning outcomes. Licensed PCDA/DHEP qualifications require assessments which integrate the requirements of the specific policing environment of the student, demonstrable links to the National Policing Curriculum (NPC), along with the requirements of the academic accreditation provider for the assessment. Where applicable, such assessments for licensed programmes should map the theoretical learning to professional practice with new constables also achieving both Independent Patrol Status (IPS) and Full-Occupational Competence (FOC).\n\n"
  stem: none
  statementType: requirement
  rung: none
  force: must
  level: none
  appliesTo: "those who design and run Policing degrees"
  addressee: provider
  verbs: ["require", "integrate", "map"]
  about: "assessment in licensed PEQF programmes"
  themes: [none]
  domain: none
  award: ["bachelor's with honours"]
  gradeOf: none
  paraphrase: "How a Policing degree is assessed depends partly on whether it is a licensed PEQF programme; licensed programmes require assessment that blends theory with the applied outcomes, ties to the workplace and the NPC and meets the academic provider's needs, and where it applies such assessment should map theory to practice as new constables also reach Independent Patrol Status and Full Occupational Competence."
  quote: full   # the issuer's statement is in `source` (D-std-0014)
  audience: practitioner
  subjects: inherited
- id: qaa/policing-in-partnership-with-2022/3.13
  locator: { number: "3.13", headingPath: ["Content, structure and delivery", "Assessment"] }
  span: { start: 47178, end: 48379 }
  source: "3.13 However, it is worth noting that academic and practical skills are not distinct - they are complementary. Learning and assessment that does not attempt to make both relevant is harmful for both research and practice (Bartunek and Rynes, 2014). Therefore, all assessments, whether they are licensed or other degrees in Policing, should focus on applied learning and provide students with the opportunity to demonstrate a grounding in blended theory and applied practice. Assessments should test a mix of academic study and skills that are relevant for the broad contemporary policing and criminal justice workforce, enabling individuals to become professional and reflective practitioners in a range of settings. All students should have the opportunity to engage in a critical exploration of contemporary policing as they develop the skills which can be applied in professional practice. Discussions and the critique of policing concepts alongside a focus on contemporary research should underpin the students' learning and assessment environment, where autonomous thinking is encouraged and individuality nurtured in creating more engaged, critical and reflective students.\n\nAssessment strategy\n"
  stem: none
  statementType: expectation
  rung: none
  force: should
  level: none
  appliesTo: "those who design and run Policing degrees"
  addressee: provider
  verbs: ["focus", "provide", "test"]
  about: "applied assessment blending theory and practice"
  themes: [none]
  domain: none
  award: ["bachelor's with honours"]
  gradeOf: none
  paraphrase: "Academic and practical skills complement each other, so every Policing assessment, licensed or not, should centre on applied learning, let students show grounded theory and practice, test a mix of study and workforce-relevant skills, and give all students the chance to explore contemporary policing critically."
  quote: full   # the issuer's statement is in `source` (D-std-0014)
  audience: practitioner
  subjects: inherited
- id: qaa/policing-in-partnership-with-2022/3.14
  locator: { number: "3.14", headingPath: ["Content, structure and delivery", "Assessment strategy"] }
  span: { start: 48384, end: 48847 }
  source: "All providers of degrees in Policing must be able to demonstrate that assessments have been co-designed with either policing practitioners or other employers to ensure that assessments are designed with a practice-based focus to enhance student employability. All degrees must provide an assessment strategy that enables students to demonstrate that they have achieved an appropriate level in the required areas of the degree programme and to facilitate learning."
  stem: none
  statementType: requirement
  rung: none
  force: must
  level: none
  appliesTo: "those who design and run Policing degrees"
  addressee: provider
  verbs: ["demonstrate", "provide"]
  about: "co-designed assessment and an assessment strategy"
  themes: [none]
  domain: none
  award: ["bachelor's with honours"]
  gradeOf: none
  paraphrase: "Every provider of a Policing degree must be able to show that assessments were co-designed with police practitioners or other employers for a practice focus that helps employability, and every degree must have an assessment strategy that lets students show they have reached the right level and that supports learning."
  quote: full   # the issuer's statement is in `source` (D-std-0014)
  audience: practitioner
  subjects: inherited
- id: qaa/policing-in-partnership-with-2022/3.14.b1
  locator: { number: "3.14.b1", headingPath: ["Content, structure and delivery", "Assessment strategy"] }
  span: { start: 48935, end: 49018 }
  source: "Assessments should link directly to the learning outcomes of the module and course."
  stem: "3.14"
  statementType: expectation
  rung: none
  force: should
  level: none
  appliesTo: "those who design and run Policing degrees"
  addressee: provider
  verbs: ["link"]
  about: "assessment aligned to outcomes"
  themes: [none]
  domain: none
  award: ["bachelor's with honours"]
  gradeOf: none
  paraphrase: "Assessments should tie straight to the module's and the course's learning outcomes."
  quote: full   # the issuer's statement is in `source` (D-std-0014)
  audience: practitioner
  subjects: inherited
- id: qaa/policing-in-partnership-with-2022/3.14.b2
  locator: { number: "3.14.b2", headingPath: ["Content, structure and delivery", "Assessment strategy"] }
  span: { start: 49021, end: 49168 }
  source: "Assessments should measure the outcome of student learning, in terms of knowledge acquired, understanding developed and skills or abilities gained."
  stem: "3.14"
  statementType: expectation
  rung: none
  force: should
  level: none
  appliesTo: "those who design and run Policing degrees"
  addressee: provider
  verbs: ["measure"]
  about: "measuring knowledge, understanding and skills"
  themes: [none]
  domain: none
  award: ["bachelor's with honours"]
  gradeOf: none
  paraphrase: "Assessments should measure what students have learned: knowledge gained, understanding built and skills or abilities acquired."
  quote: full   # the issuer's statement is in `source` (D-std-0014)
  audience: practitioner
  subjects: inherited
- id: qaa/policing-in-partnership-with-2022/3.14.b3
  locator: { number: "3.14.b3", headingPath: ["Content, structure and delivery", "Assessment strategy"] }
  span: { start: 49171, end: 49274 }
  source: "Students should be assessed on the central aspects of the learning outcomes, what is taught and learnt."
  stem: "3.14"
  statementType: expectation
  rung: none
  force: should
  level: none
  appliesTo: "those who design and run Policing degrees"
  addressee: provider
  verbs: ["assessed"]
  about: "assessing the central aspects of outcomes"
  themes: [none]
  domain: none
  award: ["bachelor's with honours"]
  gradeOf: none
  paraphrase: "Students should be assessed on the central parts of the learning outcomes, on what is taught and learned."
  quote: full   # the issuer's statement is in `source` (D-std-0014)
  audience: practitioner
  subjects: inherited
- id: qaa/policing-in-partnership-with-2022/3.14.b4
  locator: { number: "3.14.b4", headingPath: ["Content, structure and delivery", "Assessment strategy"] }
  span: { start: 49277, end: 49356 }
  source: "There should be consistency and equity in assessment workload and credit value."
  stem: "3.14"
  statementType: expectation
  rung: none
  force: should
  level: none
  appliesTo: "those who design and run Policing degrees"
  addressee: provider
  verbs: []
  about: "consistent workload and credit"
  themes: [none]
  domain: none
  award: ["bachelor's with honours"]
  gradeOf: none
  paraphrase: "Assessment workload should be consistent and fair relative to credit value."
  quote: full   # the issuer's statement is in `source` (D-std-0014)
  audience: practitioner
  subjects: inherited
- id: qaa/policing-in-partnership-with-2022/3.14.b5
  locator: { number: "3.14.b5", headingPath: ["Content, structure and delivery", "Assessment strategy"] }
  span: { start: 49359, end: 49459 }
  source: "Assessments should facilitate a progressive development path for students across modules and levels."
  stem: "3.14"
  statementType: expectation
  rung: none
  force: should
  level: none
  appliesTo: "those who design and run Policing degrees"
  addressee: provider
  verbs: ["facilitate"]
  about: "progression across modules and levels"
  themes: [none]
  domain: none
  award: ["bachelor's with honours"]
  gradeOf: none
  paraphrase: "Assessments should support a path of progressive development for students across modules and levels."
  quote: full   # the issuer's statement is in `source` (D-std-0014)
  audience: practitioner
  subjects: inherited
- id: qaa/policing-in-partnership-with-2022/3.14.b6
  locator: { number: "3.14.b6", headingPath: ["Content, structure and delivery", "Assessment strategy"] }
  span: { start: 49462, end: 49525 }
  source: "Assessments should emphasise deep, active, reflective learning."
  stem: "3.14"
  statementType: expectation
  rung: none
  force: should
  level: none
  appliesTo: "those who design and run Policing degrees"
  addressee: provider
  verbs: ["emphasise"]
  about: "deep, active, reflective learning"
  themes: [none]
  domain: none
  award: ["bachelor's with honours"]
  gradeOf: none
  paraphrase: "Assessments should stress deep, active and reflective learning."
  quote: full   # the issuer's statement is in `source` (D-std-0014)
  audience: practitioner
  subjects: inherited
- id: qaa/policing-in-partnership-with-2022/3.14.b7
  locator: { number: "3.14.b7", headingPath: ["Content, structure and delivery", "Assessment strategy"] }
  span: { start: 49528, end: 49600 }
  source: "Assessments should actively and constructively improve student learning."
  stem: "3.14"
  statementType: expectation
  rung: none
  force: should
  level: none
  appliesTo: "those who design and run Policing degrees"
  addressee: provider
  verbs: ["improve"]
  about: "assessment that improves learning"
  themes: [none]
  domain: none
  award: ["bachelor's with honours"]
  gradeOf: none
  paraphrase: "Assessments should actively and constructively improve how students learn."
  quote: full   # the issuer's statement is in `source` (D-std-0014)
  audience: practitioner
  subjects: inherited
- id: qaa/policing-in-partnership-with-2022/3.14.b8
  locator: { number: "3.14.b8", headingPath: ["Content, structure and delivery", "Assessment strategy"] }
  span: { start: 49603, end: 49659 }
  source: "Assessments should focus upon skills and their transfer."
  stem: "3.14"
  statementType: expectation
  rung: none
  force: should
  level: none
  appliesTo: "those who design and run Policing degrees"
  addressee: provider
  verbs: ["focus"]
  about: "skills and their transfer"
  themes: [none]
  domain: none
  award: ["bachelor's with honours"]
  gradeOf: none
  paraphrase: "Assessments should centre on skills and on their transfer."
  quote: full   # the issuer's statement is in `source` (D-std-0014)
  audience: practitioner
  subjects: inherited
- id: qaa/policing-in-partnership-with-2022/3.14.b9
  locator: { number: "3.14.b9", headingPath: ["Content, structure and delivery", "Assessment strategy"] }
  span: { start: 49667, end: 49805 }
  source: "Assessments must ensure inclusivity at the core so the learning styles of all students are accommodated and there is parity of experience."
  stem: "3.14"
  statementType: requirement
  rung: none
  force: must
  level: none
  appliesTo: "those who design and run Policing degrees"
  addressee: provider
  verbs: ["ensure", "accommodated"]
  about: "inclusive assessment"
  themes: [none]
  domain: none
  award: ["bachelor's with honours"]
  gradeOf: none
  paraphrase: "Assessments must put inclusivity at their core so all students' ways of learning are catered for and experience is equal."
  quote: full   # the issuer's statement is in `source` (D-std-0014)
  audience: practitioner
  subjects: inherited
- id: qaa/policing-in-partnership-with-2022/3.14.b10
  locator: { number: "3.14.b10", headingPath: ["Content, structure and delivery", "Assessment strategy"] }
  span: { start: 49808, end: 49920 }
  source: "Assessment strategies must demonstrate the provision of timely, detailed and relevant feedback for all students."
  stem: "3.14"
  statementType: requirement
  rung: none
  force: must
  level: none
  appliesTo: "those who design and run Policing degrees"
  addressee: provider
  verbs: ["demonstrate"]
  about: "timely, detailed feedback"
  themes: [none]
  domain: none
  award: ["bachelor's with honours"]
  gradeOf: none
  paraphrase: "Assessment strategies must show that every student gets timely, detailed and relevant feedback."
  quote: full   # the issuer's statement is in `source` (D-std-0014)
  audience: practitioner
  subjects: inherited
- id: qaa/policing-in-partnership-with-2022/3.15
  locator: { number: "3.15", headingPath: ["Content, structure and delivery", "Assessment strategy: Forms of assessment"] }
  span: { start: 49943, end: 50954 }
  source: "3.15 Providers should strive to use a mix of assessments and innovative methods that encourage active participation and critical reflection by students. Students should be given opportunities to demonstrate their skills and understanding in writing, orally and visually, individually and through collaborative group work, as well as undertaking independent research. To accommodate this, the assessment methods should be varied. Matthews (2016) argues that if graduates are to be problem solvers then students must have opportunities to co-create their learning experiences. Providers should show how they incorporate the student voice into the design of assessments for students, and that inclusive assessment is taken into account by all stakeholders. The core of good inclusive design for degrees in Policing is parallel to the principles of all good assessment design - constructive alignment, clear criteria, timely, able to adapt to meet the needs of students and the provision of constructive feedback.\n\n"
  stem: none
  statementType: expectation
  rung: none
  force: should
  level: none
  appliesTo: "those who design and run Policing degrees"
  addressee: provider
  verbs: ["use", "show"]
  about: "varied, participative and inclusive assessment"
  themes: [none]
  domain: none
  award: ["bachelor's with honours"]
  gradeOf: none
  paraphrase: "Those offering the degree should aim for a mix of assessments and new methods that draw students into active participation and critical reflection, with chances to show skills in writing, speech and visual form, alone and in groups and through independent research; they should show how student voice shapes the design of assessment and that inclusive assessment is considered."
  quote: full   # the issuer's statement is in `source` (D-std-0014)
  audience: practitioner
  subjects: inherited
- id: qaa/policing-in-partnership-with-2022/3.16
  locator: { number: "3.16", headingPath: ["Content, structure and delivery", "Assessment strategy: Forms of assessment"] }
  span: { start: 50954, end: 51933 }
  source: "3.16 Throughout the course, students must be given full detail of the assessments being conducted and the assessment criteria/rubric being used. There should be an appropriate balance of diagnostic, formative and summative assessment methods within the degree programmes. Students should be provided with opportunities in taught classes or online to respond to challenging questions that stimulate and promote the type of thinking and debate needed for approaching assessments. As a range of assessments should be co-designed between the provider and employers, the students will be frequently introduced to content that is particularly relevant to current operational policing; this means that the class debates, which draw on theoretical concepts, will be applied in terms of content. Applied assessments can take many forms and may include reflective writing, the development of policy briefs, applied case studies, audio-visual presentations, or the use digital portfolios.\n\n"
  stem: none
  statementType: requirement
  rung: none
  force: must
  level: none
  appliesTo: "those who design and run Policing degrees"
  addressee: provider
  verbs: ["given"]
  about: "full assessment information and a balance of methods"
  themes: [none]
  domain: none
  award: ["bachelor's with honours"]
  gradeOf: none
  paraphrase: "Throughout the course students must receive full details of each assessment and the criteria or rubric used; there should be a fitting balance of diagnostic, formative and summative methods and chances in class or online to tackle challenging questions; applied assessment may take forms such as reflective writing, policy briefs, case studies, presentations or digital portfolios."
  quote: full   # the issuer's statement is in `source` (D-std-0014)
  audience: practitioner
  subjects: inherited
- id: qaa/policing-in-partnership-with-2022/3.17
  locator: { number: "3.17", headingPath: ["Content, structure and delivery", "Assessment strategy: Forms of assessment"] }
  span: { start: 51933, end: 52113 }
  source: "3.17 Assessments should be regularly reviewed in order to ensure that they are current and valid, and to minimise any issues that may arise in relation to academic integrity.\n\n16\n\n"
  stem: none
  statementType: expectation
  rung: none
  force: should
  level: none
  appliesTo: "those who design and run Policing degrees"
  addressee: provider
  verbs: ["reviewed"]
  about: "reviewing assessments for currency and integrity"
  themes: [none]
  domain: none
  award: ["bachelor's with honours"]
  gradeOf: none
  paraphrase: "Assessments should be reviewed regularly to keep them current and valid and to reduce risks to academic integrity."
  quote: full   # the issuer's statement is in `source` (D-std-0014)
  audience: practitioner
  subjects: inherited
- id: qaa/policing-in-partnership-with-2022/4.2
  locator: { number: "4.2", headingPath: ["Benchmark standards", "Introduction"] }
  span: { start: 52492, end: 53039 }
  source: "4.2 The vast majority of students will perform significantly better than the minimum threshold standards. Each higher education provider has its own method of determining what appropriate evidence of this achievement will be and should refer to Annex D: Outcome classification descriptions for FHEQ Level 6 and FQHEIS Level 10 degrees. This Annex sets out common descriptions of the four main degree outcome classifications for bachelor's degrees with honours - 1st, 2:1, 2:2 and 3rd.\n\nThreshold level Subject knowledge, understanding and skills\n\n"
  stem: none
  statementType: expectation
  rung: none
  force: should
  level: fheq:6
  appliesTo: "those who design and run Policing degrees"
  addressee: provider
  verbs: ["refer"]
  about: "Annex D for achievement above the threshold"
  themes: [none]
  domain: none
  award: ["bachelor's with honours"]
  gradeOf: none
  paraphrase: "Most students will do much better than the minimum threshold; each provider decides what evidence shows this and should refer to Annex D, which describes the four honours classes (1st, 2:1, 2:2 and 3rd) for honours at FHEQ level 6 and FQHEIS level 10."
  quote: full   # the issuer's statement is in `source` (D-std-0014)
  audience: practitioner
  subjects: inherited
- id: qaa/policing-in-partnership-with-2022/4.3.b1
  locator: { number: "4.3.b1", headingPath: ["Benchmark standards", "Threshold level: Subject knowledge, understanding and skills"] }
  span: { start: 53124, end: 53290 }
  source: "apply an in-depth understanding of the interdisciplinary nature of policing, criminal justice and criminology to their current or future professional responsibilities"
  stem: "4.3"
  statementType: threshold
  rung: threshold
  force: threshold
  level: fheq:6
  appliesTo: "honours graduates at the threshold level"
  addressee: learner
  verbs: ["apply"]
  about: "the interdisciplinary nature of policing"
  themes: [none]
  domain: understanding
  award: ["bachelor's with honours"]
  gradeOf: none
  paraphrase: "At threshold, applies a deep understanding of how policing, criminal justice and criminology connect to present or future professional duties."
  quote: full   # the issuer's statement is in `source` (D-std-0014)
  audience: both
  subjects: inherited
- id: qaa/policing-in-partnership-with-2022/4.3.b2
  locator: { number: "4.3.b2", headingPath: ["Benchmark standards", "Threshold level: Subject knowledge, understanding and skills"] }
  span: { start: 53293, end: 53360 }
  source: "understand and evaluate the application of criminal law to policing"
  stem: "4.3"
  statementType: threshold
  rung: threshold
  force: threshold
  level: fheq:6
  appliesTo: "honours graduates at the threshold level"
  addressee: learner
  verbs: ["understand", "evaluate"]
  about: "criminal law applied to policing"
  themes: [none]
  domain: understanding
  award: ["bachelor's with honours"]
  gradeOf: none
  paraphrase: "At threshold, understands and judges how criminal law is applied in policing."
  quote: full   # the issuer's statement is in `source` (D-std-0014)
  audience: both
  subjects: inherited
- id: qaa/policing-in-partnership-with-2022/4.3.b3
  locator: { number: "4.3.b3", headingPath: ["Benchmark standards", "Threshold level: Subject knowledge, understanding and skills"] }
  span: { start: 53363, end: 53444 }
  source: "apply in-depth knowledge and understanding of safe, lawful and effective policing"
  stem: "4.3"
  statementType: threshold
  rung: threshold
  force: threshold
  level: fheq:6
  appliesTo: "honours graduates at the threshold level"
  addressee: learner
  verbs: ["apply"]
  about: "safe, lawful and effective policing"
  themes: [none]
  domain: knowledge
  award: ["bachelor's with honours"]
  gradeOf: none
  paraphrase: "At threshold, applies thorough knowledge and understanding of policing that is safe, lawful and effective."
  quote: full   # the issuer's statement is in `source` (D-std-0014)
  audience: both
  subjects: inherited
- id: qaa/policing-in-partnership-with-2022/4.3.b4
  locator: { number: "4.3.b4", headingPath: ["Benchmark standards", "Threshold level: Subject knowledge, understanding and skills"] }
  span: { start: 53447, end: 53589 }
  source: "understand a range of policing specialisms such as response, community, roads, information and intelligence, and the conduct of investigations"
  stem: "4.3"
  statementType: threshold
  rung: threshold
  force: threshold
  level: fheq:6
  appliesTo: "honours graduates at the threshold level"
  addressee: learner
  verbs: ["understand"]
  about: "policing specialisms"
  themes: [none]
  domain: knowledge
  award: ["bachelor's with honours"]
  gradeOf: none
  paraphrase: "At threshold, understands several specialisms within policing, for example response, community and roads policing, intelligence and investigation."
  quote: full   # the issuer's statement is in `source` (D-std-0014)
  audience: both
  subjects: inherited
- id: qaa/policing-in-partnership-with-2022/4.3.b5
  locator: { number: "4.3.b5", headingPath: ["Benchmark standards", "Threshold level: Subject knowledge, understanding and skills"] }
  span: { start: 53592, end: 53690 }
  source: "select and apply appropriate contemporary policing strategies to complex and interrelated contexts"
  stem: "4.3"
  statementType: threshold
  rung: threshold
  force: threshold
  level: fheq:6
  appliesTo: "honours graduates at the threshold level"
  addressee: learner
  verbs: ["select", "apply"]
  about: "choosing strategies for complex contexts"
  themes: [none]
  domain: subject-skill
  award: ["bachelor's with honours"]
  gradeOf: none
  paraphrase: "At threshold, chooses and uses suitable current policing strategies in complex, interrelated contexts."
  quote: full   # the issuer's statement is in `source` (D-std-0014)
  audience: both
  subjects: inherited
- id: qaa/policing-in-partnership-with-2022/4.3.b6
  locator: { number: "4.3.b6", headingPath: ["Benchmark standards", "Threshold level: Subject knowledge, understanding and skills"] }
  span: { start: 53693, end: 53781 }
  source: "apply broad knowledge and understanding of digital policing and technology-related crime"
  stem: "4.3"
  statementType: threshold
  rung: threshold
  force: threshold
  level: fheq:6
  appliesTo: "honours graduates at the threshold level"
  addressee: learner
  verbs: ["apply"]
  about: "digital policing and technology-related crime"
  themes: [none]
  domain: knowledge
  award: ["bachelor's with honours"]
  gradeOf: none
  paraphrase: "At threshold, applies broad knowledge and understanding of digital policing and crime involving technology."
  quote: full   # the issuer's statement is in `source` (D-std-0014)
  audience: both
  subjects: inherited
- id: qaa/policing-in-partnership-with-2022/4.3.b7
  locator: { number: "4.3.b7", headingPath: ["Benchmark standards", "Threshold level: Subject knowledge, understanding and skills"] }
  span: { start: 53784, end: 53904 }
  source: "understand and adopt an ethical approach, reflecting the highest professional values and standards of the police service"
  stem: "4.3"
  statementType: threshold
  rung: threshold
  force: threshold
  level: fheq:6
  appliesTo: "honours graduates at the threshold level"
  addressee: learner
  verbs: ["understand", "adopt"]
  about: "an ethical approach and professional values"
  themes: [none]
  domain: understanding
  award: ["bachelor's with honours"]
  gradeOf: none
  paraphrase: "At threshold, understands and takes an ethical approach in line with the police service's highest professional values and standards."
  quote: full   # the issuer's statement is in `source` (D-std-0014)
  audience: both
  subjects: inherited
- id: qaa/policing-in-partnership-with-2022/4.3.b8
  locator: { number: "4.3.b8", headingPath: ["Benchmark standards", "Threshold level: Subject knowledge, understanding and skills"] }
  span: { start: 53907, end: 53999 }
  source: "take personal responsibility for promoting equality, diversity, inclusivity and human rights"
  stem: "4.3"
  statementType: threshold
  rung: threshold
  force: threshold
  level: fheq:6
  appliesTo: "honours graduates at the threshold level"
  addressee: learner
  verbs: ["take"]
  about: "promoting equality, diversity, inclusion and human rights"
  themes: [none]
  domain: subject-skill
  award: ["bachelor's with honours"]
  gradeOf: none
  paraphrase: "At threshold, takes personal responsibility for advancing equality, diversity, inclusivity and human rights."
  quote: full   # the issuer's statement is in `source` (D-std-0014)
  audience: both
  subjects: inherited
- id: qaa/policing-in-partnership-with-2022/4.3.b9
  locator: { number: "4.3.b9", headingPath: ["Benchmark standards", "Threshold level: Subject knowledge, understanding and skills"] }
  span: { start: 54002, end: 54174 }
  source: "synthesise specialist interrelated contemporary theories, ideas and methods which can be adopted to provide support to victims, witnesses, the vulnerable, and those at risk"
  stem: "4.3"
  statementType: threshold
  rung: threshold
  force: threshold
  level: fheq:6
  appliesTo: "honours graduates at the threshold level"
  addressee: learner
  verbs: ["synthesise"]
  about: "supporting victims, witnesses and the vulnerable"
  themes: [none]
  domain: subject-skill
  award: ["bachelor's with honours"]
  gradeOf: none
  paraphrase: "At threshold, brings together specialist current theories, ideas and methods that can be used to support victims, witnesses, vulnerable people and those at risk."
  quote: full   # the issuer's statement is in `source` (D-std-0014)
  audience: both
  subjects: inherited
- id: qaa/policing-in-partnership-with-2022/4.3.b10
  locator: { number: "4.3.b10", headingPath: ["Benchmark standards", "Threshold level: Subject knowledge, understanding and skills"] }
  span: { start: 54177, end: 54309 }
  source: "adopt specialist interrelated contemporary theories, ideas and methods to prevent and detect crime, deal with suspects and offenders"
  stem: "4.3"
  statementType: threshold
  rung: threshold
  force: threshold
  level: fheq:6
  appliesTo: "honours graduates at the threshold level"
  addressee: learner
  verbs: ["adopt"]
  about: "preventing and detecting crime; suspects and offenders"
  themes: [none]
  domain: subject-skill
  award: ["bachelor's with honours"]
  gradeOf: none
  paraphrase: "At threshold, uses specialist current theories and methods to prevent crime, detect it, and deal with suspects and offenders."
  quote: full   # the issuer's statement is in `source` (D-std-0014)
  audience: both
  subjects: inherited
- id: qaa/policing-in-partnership-with-2022/4.3.b11
  locator: { number: "4.3.b11", headingPath: ["Benchmark standards", "Threshold level: Subject knowledge, understanding and skills"] }
  span: { start: 54312, end: 54397 }
  source: "critically evaluate and apply evidence-based research to the complexities of policing"
  stem: "4.3"
  statementType: threshold
  rung: threshold
  force: threshold
  level: fheq:6
  appliesTo: "honours graduates at the threshold level"
  addressee: learner
  verbs: ["evaluate", "apply"]
  about: "evidence-based research in policing"
  themes: [none]
  domain: subject-skill
  award: ["bachelor's with honours"]
  gradeOf: none
  paraphrase: "At threshold, critically judges evidence-based research and applies it to the complexities of policing."
  quote: full   # the issuer's statement is in `source` (D-std-0014)
  audience: both
  subjects: inherited
- id: qaa/policing-in-partnership-with-2022/4.3.b12
  locator: { number: "4.3.b12", headingPath: ["Benchmark standards", "Threshold level: Subject knowledge, understanding and skills"] }
  span: { start: 54400, end: 54514 }
  source: "select and apply specialist strategies, methods and evidence-based research to the complexities of problem solving"
  stem: "4.3"
  statementType: threshold
  rung: threshold
  force: threshold
  level: fheq:6
  appliesTo: "honours graduates at the threshold level"
  addressee: learner
  verbs: ["select", "apply"]
  about: "problem solving with evidence"
  themes: [none]
  domain: subject-skill
  award: ["bachelor's with honours"]
  gradeOf: none
  paraphrase: "At threshold, chooses and uses specialist strategies, methods and research evidence to solve complex problems."
  quote: full   # the issuer's statement is in `source` (D-std-0014)
  audience: both
  subjects: inherited
- id: qaa/policing-in-partnership-with-2022/4.3.b13
  locator: { number: "4.3.b13", headingPath: ["Benchmark standards", "Threshold level: Subject knowledge, understanding and skills"] }
  span: { start: 54517, end: 54648 }
  source: "make informed decisions in complex, unpredictable and interrelated situations, founded upon critical thinking and the evidence-base"
  stem: "4.3"
  statementType: threshold
  rung: threshold
  force: threshold
  level: fheq:6
  appliesTo: "honours graduates at the threshold level"
  addressee: learner
  verbs: ["make"]
  about: "informed decisions in complex situations"
  themes: [none]
  domain: subject-skill
  award: ["bachelor's with honours"]
  gradeOf: none
  paraphrase: "At threshold, makes informed decisions in complex, unpredictable and interrelated situations, based on critical thinking and evidence."
  quote: full   # the issuer's statement is in `source` (D-std-0014)
  audience: both
  subjects: inherited
- id: qaa/policing-in-partnership-with-2022/4.3.b14
  locator: { number: "4.3.b14", headingPath: ["Benchmark standards", "Threshold level: Subject knowledge, understanding and skills"] }
  span: { start: 54651, end: 54715 }
  source: "act within selected guidelines and apply professional discretion"
  stem: "4.3"
  statementType: threshold
  rung: threshold
  force: threshold
  level: fheq:6
  appliesTo: "honours graduates at the threshold level"
  addressee: learner
  verbs: ["act", "apply"]
  about: "guidelines and professional discretion"
  themes: [none]
  domain: subject-skill
  award: ["bachelor's with honours"]
  gradeOf: none
  paraphrase: "At threshold, works within chosen guidelines and uses professional discretion."
  quote: full   # the issuer's statement is in `source` (D-std-0014)
  audience: both
  subjects: inherited
- id: qaa/policing-in-partnership-with-2022/4.3.b15
  locator: { number: "4.3.b15", headingPath: ["Benchmark standards", "Threshold level: Subject knowledge, understanding and skills"] }
  span: { start: 54718, end: 54772 }
  source: "understand and apply the skills of conflict management"
  stem: "4.3"
  statementType: threshold
  rung: threshold
  force: threshold
  level: fheq:6
  appliesTo: "honours graduates at the threshold level"
  addressee: learner
  verbs: ["understand", "apply"]
  about: "conflict management"
  themes: [none]
  domain: subject-skill
  award: ["bachelor's with honours"]
  gradeOf: none
  paraphrase: "At threshold, understands and uses conflict management skills."
  quote: full   # the issuer's statement is in `source` (D-std-0014)
  audience: both
  subjects: inherited
- id: qaa/policing-in-partnership-with-2022/4.3.b16
  locator: { number: "4.3.b16", headingPath: ["Benchmark standards", "Threshold level: Subject knowledge, understanding and skills"] }
  span: { start: 54775, end: 54850 }
  source: "apply an in-depth understanding of leadership, team and partnership-working"
  stem: "4.3"
  statementType: threshold
  rung: threshold
  force: threshold
  level: fheq:6
  appliesTo: "honours graduates at the threshold level"
  addressee: learner
  verbs: ["apply"]
  about: "leadership, teams and partnership working"
  themes: [none]
  domain: understanding
  award: ["bachelor's with honours"]
  gradeOf: none
  paraphrase: "At threshold, applies a deep understanding of leadership, teamwork and working in partnership."
  quote: full   # the issuer's statement is in `source` (D-std-0014)
  audience: both
  subjects: inherited
- id: qaa/policing-in-partnership-with-2022/4.3.b17
  locator: { number: "4.3.b17", headingPath: ["Benchmark standards", "Threshold level: Subject knowledge, understanding and skills"] }
  span: { start: 54853, end: 54960 }
  source: "understand and apply techniques to ensure the wellbeing and resilience of self and others in all situations"
  stem: "4.3"
  statementType: threshold
  rung: threshold
  force: threshold
  level: fheq:6
  appliesTo: "honours graduates at the threshold level"
  addressee: learner
  verbs: ["understand", "apply"]
  about: "wellbeing and resilience of self and others"
  themes: [none]
  domain: subject-skill
  award: ["bachelor's with honours"]
  gradeOf: none
  paraphrase: "At threshold, understands and uses techniques that protect their own and others' wellbeing and resilience in every situation."
  quote: full   # the issuer's statement is in `source` (D-std-0014)
  audience: both
  subjects: inherited
- id: qaa/policing-in-partnership-with-2022/4.3.b18
  locator: { number: "4.3.b18", headingPath: ["Benchmark standards", "Threshold level: Subject knowledge, understanding and skills"] }
  span: { start: 54963, end: 55053 }
  source: "actively engage in continual self-reflection, evolving strategies to improve own practice."
  stem: "4.3"
  statementType: threshold
  rung: threshold
  force: threshold
  level: fheq:6
  appliesTo: "honours graduates at the threshold level"
  addressee: learner
  verbs: ["engage"]
  about: "continual self-reflection to improve practice"
  themes: [none]
  domain: subject-skill
  award: ["bachelor's with honours"]
  gradeOf: none
  paraphrase: "At threshold, reflects on self actively and continually, developing ways to improve own practice."
  quote: full   # the issuer's statement is in `source` (D-std-0014)
  audience: both
  subjects: inherited
- id: qaa/policing-in-partnership-with-2022/4.4.b1
  locator: { number: "4.4.b1", headingPath: ["Benchmark standards", "Threshold level: Generic skills"] }
  span: { start: 55160, end: 55279 }
  source: "accurately deploy a range of established techniques for the design, collection, analysis and interpretation of research"
  stem: "4.4"
  statementType: threshold
  rung: threshold
  force: threshold
  level: fheq:6
  appliesTo: "honours graduates at the threshold level"
  addressee: learner
  verbs: ["deploy"]
  about: "research design, collection, analysis and interpretation"
  themes: [none]
  domain: generic-skill
  award: ["bachelor's with honours"]
  gradeOf: none
  paraphrase: "At threshold, uses a range of established techniques accurately to design research and to collect, analyse and interpret data."
  quote: full   # the issuer's statement is in `source` (D-std-0014)
  audience: both
  subjects: inherited
- id: qaa/policing-in-partnership-with-2022/4.4.b2
  locator: { number: "4.4.b2", headingPath: ["Benchmark standards", "Threshold level: Generic skills"] }
  span: { start: 55282, end: 55386 }
  source: "organise and communicate interrelated information to a range of specialist and non- specialist audiences"
  stem: "4.4"
  statementType: threshold
  rung: threshold
  force: threshold
  level: fheq:6
  appliesTo: "honours graduates at the threshold level"
  addressee: learner
  verbs: ["organise", "communicate"]
  about: "communicating to specialist and lay audiences"
  themes: [none]
  domain: generic-skill
  award: ["bachelor's with honours"]
  gradeOf: none
  paraphrase: "At threshold, organises and conveys connected information for specialist and non-specialist audiences."
  quote: full   # the issuer's statement is in `source` (D-std-0014)
  audience: both
  subjects: inherited
- id: qaa/policing-in-partnership-with-2022/4.4.b3
  locator: { number: "4.4.b3", headingPath: ["Benchmark standards", "Threshold level: Generic skills"] }
  span: { start: 55389, end: 55484 }
  source: "critically evaluate arguments, assumptions and abstract concepts to identify possible solutions"
  stem: "4.4"
  statementType: threshold
  rung: threshold
  force: threshold
  level: fheq:6
  appliesTo: "honours graduates at the threshold level"
  addressee: learner
  verbs: ["evaluate", "identify"]
  about: "critical evaluation to find solutions"
  themes: [none]
  domain: generic-skill
  award: ["bachelor's with honours"]
  gradeOf: none
  paraphrase: "At threshold, critically judges arguments, assumptions and abstract ideas to find possible solutions."
  quote: full   # the issuer's statement is in `source` (D-std-0014)
  audience: both
  subjects: inherited
- id: qaa/policing-in-partnership-with-2022/4.4.b4
  locator: { number: "4.4.b4", headingPath: ["Benchmark standards", "Threshold level: Generic skills"] }
  span: { start: 55487, end: 55589 }
  source: "act autonomously and take responsibility for achieving personal and/or group tasks in complex contexts"
  stem: "4.4"
  statementType: threshold
  rung: threshold
  force: threshold
  level: fheq:6
  appliesTo: "honours graduates at the threshold level"
  addressee: learner
  verbs: ["act", "take"]
  about: "autonomy and responsibility in complex contexts"
  themes: [none]
  domain: generic-skill
  award: ["bachelor's with honours"]
  gradeOf: none
  paraphrase: "At threshold, works independently and takes responsibility for personal or group tasks in complex settings."
  quote: full   # the issuer's statement is in `source` (D-std-0014)
  audience: both
  subjects: inherited
- id: qaa/policing-in-partnership-with-2022/4.4.b5
  locator: { number: "4.4.b5", headingPath: ["Benchmark standards", "Threshold level: Generic skills"] }
  span: { start: 55592, end: 55728 }
  source: "appreciate the current political, economic, social, technological, environmental, legal and ethical discussions impacting the discipline"
  stem: "4.4"
  statementType: threshold
  rung: threshold
  force: threshold
  level: fheq:6
  appliesTo: "honours graduates at the threshold level"
  addressee: learner
  verbs: ["appreciate"]
  about: "political, economic, social, technological, environmental, legal and ethical debates"
  themes: [none]
  domain: generic-skill
  award: ["bachelor's with honours"]
  gradeOf: none
  paraphrase: "At threshold, appreciates today's debates affecting the discipline, whether political, economic, social, technological, environmental, legal or ethical."
  quote: full   # the issuer's statement is in `source` (D-std-0014)
  audience: both
  subjects: inherited
- id: qaa/policing-in-partnership-with-2022/4.4.b6
  locator: { number: "4.4.b6", headingPath: ["Benchmark standards", "Threshold level: Generic skills"] }
  span: { start: 55731, end: 55827 }
  source: "understand contemporary debates with regard to equality, diversity, inclusion and sustainability"
  stem: "4.4"
  statementType: threshold
  rung: threshold
  force: threshold
  level: fheq:6
  appliesTo: "honours graduates at the threshold level"
  addressee: learner
  verbs: ["understand"]
  about: "debates on EDI and sustainability"
  themes: [none]
  domain: generic-skill
  award: ["bachelor's with honours"]
  gradeOf: none
  paraphrase: "At threshold, understands current debates on equality, diversity, inclusion and sustainability."
  quote: full   # the issuer's statement is in `source` (D-std-0014)
  audience: both
  subjects: inherited
- id: qaa/policing-in-partnership-with-2022/4.4.b7
  locator: { number: "4.4.b7", headingPath: ["Benchmark standards", "Threshold level: Generic skills"] }
  span: { start: 55830, end: 55883 }
  source: "understand the impact of culture on working practices"
  stem: "4.4"
  statementType: threshold
  rung: threshold
  force: threshold
  level: fheq:6
  appliesTo: "honours graduates at the threshold level"
  addressee: learner
  verbs: ["understand"]
  about: "culture and working practices"
  themes: [none]
  domain: generic-skill
  award: ["bachelor's with honours"]
  gradeOf: none
  paraphrase: "At threshold, understands how culture affects ways of working."
  quote: full   # the issuer's statement is in `source` (D-std-0014)
  audience: both
  subjects: inherited
- id: qaa/policing-in-partnership-with-2022/4.4.b8
  locator: { number: "4.4.b8", headingPath: ["Benchmark standards", "Threshold level: Generic skills"] }
  span: { start: 55886, end: 55958 }
  source: "apply a range of innovative methods and techniques learned to employment"
  stem: "4.4"
  statementType: threshold
  rung: threshold
  force: threshold
  level: fheq:6
  appliesTo: "honours graduates at the threshold level"
  addressee: learner
  verbs: ["apply"]
  about: "innovative methods in employment"
  themes: [none]
  domain: generic-skill
  award: ["bachelor's with honours"]
  gradeOf: none
  paraphrase: "At threshold, uses at work a range of innovative methods and techniques learned on the course."
  quote: full   # the issuer's statement is in `source` (D-std-0014)
  audience: both
  subjects: inherited
- id: qaa/policing-in-partnership-with-2022/4.4.b9
  locator: { number: "4.4.b9", headingPath: ["Benchmark standards", "Threshold level: Generic skills"] }
  span: { start: 55961, end: 56035 }
  source: "select and apply a range of digital skills and techniques in the workplace"
  stem: "4.4"
  statementType: threshold
  rung: threshold
  force: threshold
  level: fheq:6
  appliesTo: "honours graduates at the threshold level"
  addressee: learner
  verbs: ["select", "apply"]
  about: "digital skills at work"
  themes: [none]
  domain: generic-skill
  award: ["bachelor's with honours"]
  gradeOf: none
  paraphrase: "At threshold, chooses and uses a range of digital skills and techniques at work."
  quote: full   # the issuer's statement is in `source` (D-std-0014)
  audience: both
  subjects: inherited
- id: qaa/policing-in-partnership-with-2022/4.4.b10
  locator: { number: "4.4.b10", headingPath: ["Benchmark standards", "Threshold level: Generic skills"] }
  span: { start: 56038, end: 56116 }
  source: "actively engage in self-reflection, to identify and address own learning needs"
  stem: "4.4"
  statementType: threshold
  rung: threshold
  force: threshold
  level: fheq:6
  appliesTo: "honours graduates at the threshold level"
  addressee: learner
  verbs: ["engage", "identify", "address"]
  about: "self-reflection on learning needs"
  themes: [none]
  domain: generic-skill
  award: ["bachelor's with honours"]
  gradeOf: none
  paraphrase: "At threshold, reflects actively on self to find and meet own learning needs."
  quote: full   # the issuer's statement is in `source` (D-std-0014)
  audience: both
  subjects: inherited
- id: qaa/policing-in-partnership-with-2022/4.4.b11
  locator: { number: "4.4.b11", headingPath: ["Benchmark standards", "Threshold level: Generic skills"] }
  span: { start: 56119, end: 56198 }
  source: "understand the importance of engaging with continuing professional development."
  stem: "4.4"
  statementType: threshold
  rung: threshold
  force: threshold
  level: fheq:6
  appliesTo: "honours graduates at the threshold level"
  addressee: learner
  verbs: ["understand"]
  about: "continuing professional development"
  themes: [none]
  domain: generic-skill
  award: ["bachelor's with honours"]
  gradeOf: none
  paraphrase: "At threshold, understands why continuing professional development matters."
  quote: full   # the issuer's statement is in `source` (D-std-0014)
  audience: both
  subjects: inherited
```

### S4a Audience versions
<!-- label: both; status: drafted; basis: primary. forPractitioner: for the programme designer or teacher. forBeneficiary: for the student, second person, naming no issuer. author-agent-written: instructions to an AI agent writing about the statement (a course document, a handbook, an outcome, a report). author-agent-dialogue: instructions to an AI agent using the statement in conversation (with a student, a teacher or a programme team). Written fresh from the held text alone (benchmark rule 6; Abbott, 15:42). -->
```yaml
- statement: qaa/policing-in-partnership-with-2022/1.10
  forPractitioner: { text: "Plan the course so that, from start to finish, students will build and show an understanding of the policing profession and of the law and regulation that frame policing and the criminal justice system.", rewrite: light, force: will, status: drafted }
  forBeneficiary: { text: "Across your course you will build and show an understanding of policing as a profession and of the laws and rules that shape policing and criminal justice.", rewrite: full, force: will, status: drafted }
  author-agent-written: "Describe this as an outcome the statement expects ('will') of students of the subject at honours level (FHEQ 6, FQHEIS 10), about understanding of the profession and its legal setting. Cite it as QAA (2022), Policing Subject Benchmark Statement, para 1.10, and set it beside 1.15, 2.2.b9 and 4.3.b2, and the FHEQ honours descriptor qaa/fheq-2024/4.15.b1. Do not call it one of the threshold standards of section 4 or a regulatory rule; it sits in the statement's discussion of the degree."
  author-agent-dialogue: "Raise it when a student asks what the degree is for, or a team sets the overall aims of the course. With a student, put it plainly in the second person; with staff, frame it as an outcome the course should make possible. Ask: \"Where in your work so far have you shown how the law shapes a policing decision?\" Avoid quoting the paragraph at length or treating it as a pass mark."
- statement: qaa/policing-in-partnership-with-2022/1.12
  forPractitioner: { text: "Give students a protected setting and a wide range of scenarios in which they will develop effective communication and interpersonal skills for professional policing.", rewrite: light, force: will, status: drafted }
  forBeneficiary: { text: "In a safe setting with many practice scenarios, you will develop the communication and people skills that policing work needs.", rewrite: full, force: will, status: drafted }
  author-agent-written: "Describe this as an outcome the statement expects ('will') of students of the subject at honours level (FHEQ 6, FQHEIS 10), about communication and interpersonal skills. Cite it as QAA (2022), Policing Subject Benchmark Statement, para 1.12, and set it beside 4.4.b2, qaa/fheq-2024/4.15.b8 and spine:6. Do not call it one of the threshold standards of section 4 or a regulatory rule; it sits in the statement's discussion of the degree."
  author-agent-dialogue: "Raise it when a student worries about speaking, interviewing or dealing with the public, or staff plan scenario-based teaching. With a student, put it plainly in the second person; with staff, frame it as an outcome the course should make possible. Ask: \"Which scenario so far tested your communication most, and what would you do differently next time?\" Avoid quoting the paragraph at length or treating it as a pass mark."
- statement: qaa/policing-in-partnership-with-2022/1.15
  forPractitioner: { text: "Graduates will be able to evaluate evidence and argument, judge soundly, communicate well and decide responsibly on evidence in complex situations; they should also be able to use research, evidence-based practice and problem-solving at work and tie theory to practice.", rewrite: light, force: will, status: drafted }
  forBeneficiary: { text: "You will be able to weigh up evidence and arguments, reach sound judgements, explain them clearly and make responsible decisions based on evidence in complex situations, linking what you learn to policing practice.", rewrite: full, force: will, status: drafted }
  author-agent-written: "Describe this as an outcome the statement expects ('will') of holders of a Policing degree at honours level (FHEQ 6, FQHEIS 10), about judgement, evidence-informed decisions and linking theory to practice. Cite it as QAA (2022), Policing Subject Benchmark Statement, para 1.15, and set it beside 4.3.b13 and 4.4.b3, and qaa/fheq-2024/4.15.b7 and 4.15.b9.2. Do not call it one of the threshold standards of section 4 or a regulatory rule; it sits in the statement's discussion of the degree."
  author-agent-dialogue: "Raise it when a student asks what employers expect from a policing graduate, or a team writes programme-level outcomes. With a student, put it plainly in the second person; with staff, frame it as an outcome the course should make possible. Ask: \"Can you show a decision you made where the evidence was incomplete, and how you justified it?\" Avoid quoting the paragraph at length or treating it as a pass mark."
- statement: qaa/policing-in-partnership-with-2022/1.16
  forPractitioner: { text: "Check admissions, curriculum, teaching and assessment so the degree should show no discrimination, stratification or exclusion by protected characteristic, social background or where students live.", rewrite: light, force: should, status: drafted }
  forBeneficiary: { text: "not-applicable: a duty on those who design and run the course; the student meets its effect, not a standard to reach", rewrite: full, force: should, status: drafted }
  author-agent-written: "Describe this as an expectation ('should') on those who design and run Policing degrees, about a degree that excludes no group: a course duty, not a student outcome. Cite it as QAA (2022), Policing Subject Benchmark Statement, para 1.16, and set it beside 1.17, 1.19 and 1.20, and the equality theme in SB2. Do not state it as law or as something students achieve; the statement is a sector reference point, not regulation."
  author-agent-dialogue: "Raise it when a team reviews admissions, curriculum or assessment for fairness. Frame it for the programme team as a design or delivery duty; with a student, explain only what it means for their own experience. Ask: \"Which of the course's processes could disadvantage a student because of background or location?\" Do not give it to a student as something they must achieve."
- statement: qaa/policing-in-partnership-with-2022/1.17
  forPractitioner: { text: "Treat every student and partner openly, fairly and with dignity: that is a must. Keep in view the Public Sector Equality Duty (Section 75 in Northern Ireland) and consider an Equality Impact Assessment, shared with the police force where you co-create the course.", rewrite: light, force: must, status: drafted }
  forBeneficiary: { text: "not-applicable: a duty on those who design and run the course; the student meets its effect, not a standard to reach", rewrite: full, force: must, status: drafted }
  author-agent-written: "Describe this as a requirement ('must') on those who design and run Policing degrees, about fair treatment and equality impact assessment: a course duty, not a student outcome. Cite it as QAA (2022), Policing Subject Benchmark Statement, para 1.17, and set it beside 1.16, 1.18 and 3.2.b5, with the Equality Act 2010 as listed in SB6. Do not state it as law or as something students achieve; the statement is a sector reference point, not regulation."
  author-agent-dialogue: "Raise it when a team designs a course, especially with a police force partner, or a student raises unfair treatment. Frame it for the programme team as a design or delivery duty; with a student, explain only what it means for their own experience. Ask: \"Has an Equality Impact Assessment been done for this course, and who took part in it?\" Do not give it to a student as something they must achieve."
- statement: qaa/policing-in-partnership-with-2022/1.18
  forPractitioner: { text: "Embed EDI in the culture and practice of the course, operational or not, with ethics as a thread throughout; every student must understand ethics as the top standard and carry it into daily conduct, taking responsibility for their own behaviour.", rewrite: light, force: must, status: drafted }
  forBeneficiary: { text: "You must understand why ethics sit at the heart of policing, put your learning into practice every day and take responsibility for behaving to the highest ethical standards.", rewrite: full, force: must, status: drafted }
  author-agent-written: "Describe this as a requirement ('must') of all students of Policing at honours level (FHEQ 6, FQHEIS 10), about ethics as the highest standard of conduct. Cite it as QAA (2022), Policing Subject Benchmark Statement, para 1.18, and set it beside 4.3.b7, 2.2.b1 and qaa/fheq-2024/annex-d/professional/r2/3rd. Do not call it one of the threshold standards of section 4 or a regulatory rule; it sits in the statement's discussion of the degree."
  author-agent-dialogue: "Raise it when a student faces an ethical dilemma on placement or in a scenario, or staff plan where ethics appears in each module. With a student, put it plainly in the second person; with staff, frame it as an outcome the course should make possible. Ask: \"What would you do if a colleague's conduct fell short of the standards you have learned?\" Avoid quoting the paragraph at length or treating it as a pass mark."
- statement: qaa/policing-in-partnership-with-2022/1.19
  forPractitioner: { text: "Design and plan teaching and assessment to be inclusive and accessible from the outset rather than adding variety later; varied styles on their own may still exclude some students.", rewrite: light, force: should, status: drafted }
  forBeneficiary: { text: "not-applicable: a duty on those who design and run the course; the student meets its effect, not a standard to reach", rewrite: full, force: should, status: drafted }
  author-agent-written: "Describe this as an expectation ('should') on those who design and run Policing degrees, about inclusive and accessible teaching and assessment: a course duty, not a student outcome. Cite it as QAA (2022), Policing Subject Benchmark Statement, para 1.19, and set it beside 1.20, 3.14.b9 and 3.15. Do not state it as law or as something students achieve; the statement is a sector reference point, not regulation."
  author-agent-dialogue: "Raise it when a team designs modules or assessments, or asks why some groups do less well. Frame it for the programme team as a design or delivery duty; with a student, explain only what it means for their own experience. Ask: \"Which assessment in this module would be hardest for a student with a disability or caring duties, and why?\" Do not give it to a student as something they must achieve."
- statement: qaa/policing-in-partnership-with-2022/1.20
  forPractitioner: { text: "Show, with evidence, a commitment to widening access: address physical access, digital divides (devices and connectivity) and the wider design of teaching so every student can reach their potential.", rewrite: light, force: must, status: drafted }
  forBeneficiary: { text: "not-applicable: a duty on those who design and run the course; the student meets its effect, not a standard to reach", rewrite: full, force: must, status: drafted }
  author-agent-written: "Describe this as a requirement ('must') on those who design and run Policing degrees, about commitment to widening access: a course duty, not a student outcome. Cite it as QAA (2022), Policing Subject Benchmark Statement, para 1.20, and set it beside 1.19, 1.22 and 1.23.b1 to 1.23.b4. Do not state it as law or as something students achieve; the statement is a sector reference point, not regulation."
  author-agent-dialogue: "Raise it when a team plans blended or online delivery or reviews widening access. Frame it for the programme team as a design or delivery duty; with a student, explain only what it means for their own experience. Ask: \"What evidence shows that students without reliable devices or connectivity can still take full part?\" Do not give it to a student as something they must achieve."
- statement: qaa/policing-in-partnership-with-2022/1.22
  forPractitioner: { text: "Stress flexible delivery and varied routes (work-based, knowledge-focused, graduate entry) so learning is accessible and recruits better reflect the communities they will serve.", rewrite: light, force: should, status: drafted }
  forBeneficiary: { text: "not-applicable: a duty on those who design and run the course; the student meets its effect, not a standard to reach", rewrite: full, force: should, status: drafted }
  author-agent-written: "Describe this as an expectation ('should') on those who design and run Policing degrees, about flexible delivery and varied routes: a course duty, not a student outcome. Cite it as QAA (2022), Policing Subject Benchmark Statement, para 1.22, and set it beside 1.20, 1.4 (the three entry routes) and 2.13. Do not state it as law or as something students achieve; the statement is a sector reference point, not regulation."
  author-agent-dialogue: "Raise it when a team weighs entry routes or modes of delivery. Frame it for the programme team as a design or delivery duty; with a student, explain only what it means for their own experience. Ask: \"Which entry route or mode of study would widen who can join this course?\" Do not give it to a student as something they must achieve."
- statement: qaa/policing-in-partnership-with-2022/1.23.b1
  forPractitioner: { text: "Put support material online so students can keep studying through illness, transport trouble or family and caring commitments.", rewrite: light, force: should, status: drafted }
  forBeneficiary: { text: "not-applicable: a duty on those who design and run the course; the student meets its effect, not a standard to reach", rewrite: full, force: should, status: drafted }
  author-agent-written: "Describe this as an expectation ('should') on those who design and run Policing degrees, about course support available online: a course duty, not a student outcome. Cite it as QAA (2022), Policing Subject Benchmark Statement, para 1.23, item 1, and set it beside 1.20, 1.23.b2 to 1.23.b4 and the Accessibility Regulations 2018 listed in SB6. Do not state it as law or as something students achieve; the statement is a sector reference point, not regulation."
  author-agent-dialogue: "Raise it when a student's illness, travel or caring duties threaten their study. Frame it for the programme team as a design or delivery duty; with a student, explain only what it means for their own experience. Ask: \"Can a student who misses a session reach all of its support material online?\" Do not give it to a student as something they must achieve."
- statement: qaa/policing-in-partnership-with-2022/1.23.b2
  forPractitioner: { text: "Provide recorded or online content that students can pause, rewind and revisit to keep up with its pace and complexity.", rewrite: light, force: should, status: drafted }
  forBeneficiary: { text: "not-applicable: a duty on those who design and run the course; the student meets its effect, not a standard to reach", rewrite: full, force: should, status: drafted }
  author-agent-written: "Describe this as an expectation ('should') on those who design and run Policing degrees, about pausing and replaying content: a course duty, not a student outcome. Cite it as QAA (2022), Policing Subject Benchmark Statement, para 1.23, item 2, and set it beside 1.23.b1, 1.23.b3 and 1.20. Do not state it as law or as something students achieve; the statement is a sector reference point, not regulation."
  author-agent-dialogue: "Raise it when content is delivered quickly or is technically dense. Frame it for the programme team as a design or delivery duty; with a student, explain only what it means for their own experience. Ask: \"Can students pause and replay the hardest parts of this module?\" Do not give it to a student as something they must achieve."
- statement: qaa/policing-in-partnership-with-2022/1.23.b3
  forPractitioner: { text: "Let students revisit content as often as they need, especially before assessments set in the workplace.", rewrite: light, force: should, status: drafted }
  forBeneficiary: { text: "not-applicable: a duty on those who design and run the course; the student meets its effect, not a standard to reach", rewrite: full, force: should, status: drafted }
  author-agent-written: "Describe this as an expectation ('should') on those who design and run Policing degrees, about revisiting content before work-based assessment: a course duty, not a student outcome. Cite it as QAA (2022), Policing Subject Benchmark Statement, para 1.23, item 3, and set it beside 1.23.b2, 3.11 and 3.14.b9. Do not state it as law or as something students achieve; the statement is a sector reference point, not regulation."
  author-agent-dialogue: "Raise it when students prepare for assessments in the workplace. Frame it for the programme team as a design or delivery duty; with a student, explain only what it means for their own experience. Ask: \"How often can a student revisit content before a work-based assessment?\" Do not give it to a student as something they must achieve."
- statement: qaa/policing-in-partnership-with-2022/1.23.b4
  forPractitioner: { text: "Where a forum exists, give students time to reflect before they post questions; this helps those who deliberate and those working in a second language.", rewrite: light, force: should, status: drafted }
  forBeneficiary: { text: "not-applicable: a duty on those who design and run the course; the student meets its effect, not a standard to reach", rewrite: full, force: should, status: drafted }
  author-agent-written: "Describe this as an expectation ('should') on those who design and run Policing degrees, about time to reflect before posting questions: a course duty, not a student outcome. Cite it as QAA (2022), Policing Subject Benchmark Statement, para 1.23, item 4, and set it beside 1.19, 1.23.b3 and 3.15. Do not state it as law or as something students achieve; the statement is a sector reference point, not regulation."
  author-agent-dialogue: "Raise it when a module uses online discussion. Frame it for the programme team as a design or delivery duty; with a student, explain only what it means for their own experience. Ask: \"Do quieter students, or those using a second language, get time to think before they post?\" Do not give it to a student as something they must achieve."
- statement: qaa/policing-in-partnership-with-2022/1.26
  forPractitioner: { text: "Design the programme with reference to the SDGs, placing the eight named themes (wellbeing, inclusive education, equity, economic vitality and skills, safe communities, environmental impact, access to justice, partnership) openly in the curriculum.", rewrite: light, force: should, status: drafted }
  forBeneficiary: { text: "not-applicable: a duty on those who design and run the course; the student meets its effect, not a standard to reach", rewrite: full, force: should, status: drafted }
  author-agent-written: "Describe this as an expectation ('should') on those who design and run Policing degrees, about designing programmes with the SDGs: a course duty, not a student outcome. Cite it as QAA (2022), Policing Subject Benchmark Statement, para 1.26, and set it beside 1.24, 1.25, 4.4.b6 and the sustainability theme in SB2. Do not state it as law or as something students achieve; the statement is a sector reference point, not regulation."
  author-agent-dialogue: "Raise it when a team maps sustainability into modules. Frame it for the programme team as a design or delivery duty; with a student, explain only what it means for their own experience. Ask: \"Which of the eight SDG themes does each core module address, and where?\" Do not give it to a student as something they must achieve."
- statement: qaa/policing-in-partnership-with-2022/1.27
  forPractitioner: { text: "Feed current and emerging challenges (such as climate change, inequality and technological change, 1.28) into each programme review so content stays current.", rewrite: light, force: should, status: drafted }
  forBeneficiary: { text: "not-applicable: a duty on those who design and run the course; the student meets its effect, not a standard to reach", rewrite: full, force: should, status: drafted }
  author-agent-written: "Describe this as an expectation ('should') on those who design and run Policing degrees, about future challenges in programme review: a course duty, not a student outcome. Cite it as QAA (2022), Policing Subject Benchmark Statement, para 1.27, and set it beside 1.28, 1.29 and 3.17. Do not state it as law or as something students achieve; the statement is a sector reference point, not regulation."
  author-agent-dialogue: "Raise it when a team plans periodic review or refreshes content. Frame it for the programme team as a design or delivery duty; with a student, explain only what it means for their own experience. Ask: \"Which emerging trend in policing changed this course at its last review?\" Do not give it to a student as something they must achieve."
- statement: qaa/policing-in-partnership-with-2022/2.2.b1
  forPractitioner: { text: "Programmes will enable graduates to comprehend why the highest professional standards govern lawful, ethical, safe and effective policing.", rewrite: light, force: will, status: drafted }
  forBeneficiary: { text: "You will understand why policing has to meet the highest professional standards to be lawful, ethical, safe and effective.", rewrite: full, force: will, status: drafted }
  author-agent-written: "Describe this as an outcome the statement expects ('will') of graduates of the subject at honours level (FHEQ 6, FQHEIS 10), about the highest professional standards. Cite it as QAA (2022), Policing Subject Benchmark Statement, para 2.2, item 1, and set it beside 4.3.b3, 4.3.b7 and 3.2.b2. Do not call it one of the threshold standards of section 4 or a regulatory rule; it sits in the statement's discussion of the degree."
  author-agent-dialogue: "Raise it when a student asks why professional standards are taught so heavily. With a student, put it plainly in the second person; with staff, frame it as an outcome the course should make possible. Ask: \"Where have you seen a professional standard change how a task was done?\" Avoid quoting the paragraph at length or treating it as a pass mark."
- statement: qaa/policing-in-partnership-with-2022/2.2.b2
  forPractitioner: { text: "Programmes will enable graduates to conduct research based on evidence.", rewrite: light, force: will, status: drafted }
  forBeneficiary: { text: "You will be able to carry out your own research based on evidence.", rewrite: full, force: will, status: drafted }
  author-agent-written: "Describe this as an outcome the statement expects ('will') of graduates of the subject at honours level (FHEQ 6, FQHEIS 10), about evidence-based research. Cite it as QAA (2022), Policing Subject Benchmark Statement, para 2.2, item 2, and set it beside 2.14, 4.3.b11 and 4.4.b1. Do not call it one of the threshold standards of section 4 or a regulatory rule; it sits in the statement's discussion of the degree."
  author-agent-dialogue: "Raise it when a student begins research methods or the final project. With a student, put it plainly in the second person; with staff, frame it as an outcome the course should make possible. Ask: \"What question about policing would you most like to research, and what evidence would answer it?\" Avoid quoting the paragraph at length or treating it as a pass mark."
- statement: qaa/policing-in-partnership-with-2022/2.2.b3
  forPractitioner: { text: "Programmes will enable graduates to develop an understanding of evidence-based policing and of problem-solving.", rewrite: light, force: will, status: drafted }
  forBeneficiary: { text: "You will come to understand how evidence-based policing and problem-solving work.", rewrite: full, force: will, status: drafted }
  author-agent-written: "Describe this as an outcome the statement expects ('will') of graduates of the subject at honours level (FHEQ 6, FQHEIS 10), about evidence-based policing and problem solving. Cite it as QAA (2022), Policing Subject Benchmark Statement, para 2.2, item 3, and set it beside 4.3.b11 and 4.3.b12. Do not call it one of the threshold standards of section 4 or a regulatory rule; it sits in the statement's discussion of the degree."
  author-agent-dialogue: "Raise it when a student meets evidence-based policing for the first time. With a student, put it plainly in the second person; with staff, frame it as an outcome the course should make possible. Ask: \"How would you test whether a policing tactic actually works?\" Avoid quoting the paragraph at length or treating it as a pass mark."
- statement: qaa/policing-in-partnership-with-2022/2.2.b4
  forPractitioner: { text: "Programmes will enable graduates to develop knowledge of several front-line areas of professional policing.", rewrite: light, force: will, status: drafted }
  forBeneficiary: { text: "You will learn about several areas of front-line policing.", rewrite: full, force: will, status: drafted }
  author-agent-written: "Describe this as an outcome the statement expects ('will') of graduates of the subject at honours level (FHEQ 6, FQHEIS 10), about front-line policing areas. Cite it as QAA (2022), Policing Subject Benchmark Statement, para 2.2, item 4, and set it beside 4.3.b4 and 3.3. Do not call it one of the threshold standards of section 4 or a regulatory rule; it sits in the statement's discussion of the degree."
  author-agent-dialogue: "Raise it when a student chooses options or asks about front-line roles. With a student, put it plainly in the second person; with staff, frame it as an outcome the course should make possible. Ask: \"Which front-line area do you know least about so far?\" Avoid quoting the paragraph at length or treating it as a pass mark."
- statement: qaa/policing-in-partnership-with-2022/2.2.b5
  forPractitioner: { text: "Programmes will enable graduates to embed equality, diversity, inclusion and human rights in their practice, actively and without waiting to be asked.", rewrite: light, force: will, status: drafted }
  forBeneficiary: { text: "You will actively build equality, diversity, inclusion and human rights into how you work.", rewrite: full, force: will, status: drafted }
  author-agent-written: "Describe this as an outcome the statement expects ('will') of graduates of the subject at honours level (FHEQ 6, FQHEIS 10), about equality, diversity, inclusion and human rights. Cite it as QAA (2022), Policing Subject Benchmark Statement, para 2.2, item 5, and set it beside 4.3.b8, 3.2.b5 and 1.18. Do not call it one of the threshold standards of section 4 or a regulatory rule; it sits in the statement's discussion of the degree."
  author-agent-dialogue: "Raise it when a scenario or placement raises fairness or rights. With a student, put it plainly in the second person; with staff, frame it as an outcome the course should make possible. Ask: \"How did you take human rights into account in your last scenario exercise?\" Avoid quoting the paragraph at length or treating it as a pass mark."
- statement: qaa/policing-in-partnership-with-2022/2.2.b6
  forPractitioner: { text: "Programmes will enable graduates to understand the importance of wellbeing and professional resilience.", rewrite: light, force: will, status: drafted }
  forBeneficiary: { text: "You will understand why looking after your wellbeing and resilience matters in policing.", rewrite: full, force: will, status: drafted }
  author-agent-written: "Describe this as an outcome the statement expects ('will') of graduates of the subject at honours level (FHEQ 6, FQHEIS 10), about wellbeing and professional resilience. Cite it as QAA (2022), Policing Subject Benchmark Statement, para 2.2, item 6, and set it beside 4.3.b17. Do not call it one of the threshold standards of section 4 or a regulatory rule; it sits in the statement's discussion of the degree."
  author-agent-dialogue: "Raise it when a student finds placement or study demanding. With a student, put it plainly in the second person; with staff, frame it as an outcome the course should make possible. Ask: \"What helps you recover after a difficult shift or deadline?\" Avoid quoting the paragraph at length or treating it as a pass mark."
- statement: qaa/policing-in-partnership-with-2022/2.2.b7
  forPractitioner: { text: "Programmes will enable graduates to understand the ideas behind digital policing and cyber-enabled crime.", rewrite: light, force: will, status: drafted }
  forBeneficiary: { text: "You will understand how policing works in the digital world and how crime uses online tools.", rewrite: full, force: will, status: drafted }
  author-agent-written: "Describe this as an outcome the statement expects ('will') of graduates of the subject at honours level (FHEQ 6, FQHEIS 10), about digital policing and cyber-enabled crime. Cite it as QAA (2022), Policing Subject Benchmark Statement, para 2.2, item 7, and set it beside 4.3.b6 and 4.4.b9. Do not call it one of the threshold standards of section 4 or a regulatory rule; it sits in the statement's discussion of the degree."
  author-agent-dialogue: "Raise it when a student studies digital evidence or online crime. With a student, put it plainly in the second person; with staff, frame it as an outcome the course should make possible. Ask: \"How would you explain cyber-enabled crime to a victim with no technical background?\" Avoid quoting the paragraph at length or treating it as a pass mark."
- statement: qaa/policing-in-partnership-with-2022/2.2.b8
  forPractitioner: { text: "Programmes will enable graduates to develop broad and thorough knowledge across policing, criminal justice and criminology.", rewrite: light, force: will, status: drafted }
  forBeneficiary: { text: "You will build a thorough knowledge of policing, criminal justice and criminology.", rewrite: full, force: will, status: drafted }
  author-agent-written: "Describe this as an outcome the statement expects ('will') of graduates of the subject at honours level (FHEQ 6, FQHEIS 10), about policing, criminal justice and criminology. Cite it as QAA (2022), Policing Subject Benchmark Statement, para 2.2, item 8, and set it beside 4.3.b1 and qaa/fheq-2024/4.15.b1. Do not call it one of the threshold standards of section 4 or a regulatory rule; it sits in the statement's discussion of the degree."
  author-agent-dialogue: "Raise it when a student asks how criminology modules fit the degree. With a student, put it plainly in the second person; with staff, frame it as an outcome the course should make possible. Ask: \"Which criminological theory helps you most to explain a policing problem?\" Avoid quoting the paragraph at length or treating it as a pass mark."
- statement: qaa/policing-in-partnership-with-2022/2.2.b9
  forPractitioner: { text: "Programmes will enable graduates to understand the criminal justice system as it bears on policing.", rewrite: light, force: will, status: drafted }
  forBeneficiary: { text: "You will understand how policing fits into the wider criminal justice system.", rewrite: full, force: will, status: drafted }
  author-agent-written: "Describe this as an outcome the statement expects ('will') of graduates of the subject at honours level (FHEQ 6, FQHEIS 10), about the criminal justice system and policing. Cite it as QAA (2022), Policing Subject Benchmark Statement, para 2.2, item 9, and set it beside 1.10 and 4.3.b2. Do not call it one of the threshold standards of section 4 or a regulatory rule; it sits in the statement's discussion of the degree."
  author-agent-dialogue: "Raise it when a student follows a case from arrest to court. With a student, put it plainly in the second person; with staff, frame it as an outcome the course should make possible. Ask: \"What happens to a case after the police pass it on?\" Avoid quoting the paragraph at length or treating it as a pass mark."
- statement: qaa/policing-in-partnership-with-2022/2.2.b10
  forPractitioner: { text: "Programmes will enable graduates to develop knowledge of legislation, powers and policy and of their use in practice.", rewrite: light, force: will, status: drafted }
  forBeneficiary: { text: "You will know the laws, powers and policies that govern policing and how they are used in practice.", rewrite: full, force: will, status: drafted }
  author-agent-written: "Describe this as an outcome the statement expects ('will') of graduates of the subject at honours level (FHEQ 6, FQHEIS 10), about legislation, powers and policy in practice. Cite it as QAA (2022), Policing Subject Benchmark Statement, para 2.2, item 10, and set it beside 4.3.b2 and 4.3.b14. Do not call it one of the threshold standards of section 4 or a regulatory rule; it sits in the statement's discussion of the degree."
  author-agent-dialogue: "Raise it when a student is unsure which power applies in a scenario. With a student, put it plainly in the second person; with staff, frame it as an outcome the course should make possible. Ask: \"Which power would you rely on here, and what limits it?\" Avoid quoting the paragraph at length or treating it as a pass mark."
- statement: qaa/policing-in-partnership-with-2022/2.2.b11
  forPractitioner: { text: "Programmes will enable graduates to recognise the service's core duty to identify and support vulnerable people and those at risk.", rewrite: light, force: will, status: drafted }
  forBeneficiary: { text: "You will recognise that a core duty of the police is to spot and support people who are vulnerable or at risk.", rewrite: full, force: will, status: drafted }
  author-agent-written: "Describe this as an outcome the statement expects ('will') of graduates of the subject at honours level (FHEQ 6, FQHEIS 10), about protecting people who are vulnerable or at risk. Cite it as QAA (2022), Policing Subject Benchmark Statement, para 2.2, item 11, and set it beside 4.3.b9 and 3.3. Do not call it one of the threshold standards of section 4 or a regulatory rule; it sits in the statement's discussion of the degree."
  author-agent-dialogue: "Raise it when a scenario involves a vulnerable person. With a student, put it plainly in the second person; with staff, frame it as an outcome the course should make possible. Ask: \"What signs of vulnerability might be easy to miss in this situation?\" Avoid quoting the paragraph at length or treating it as a pass mark."
- statement: qaa/policing-in-partnership-with-2022/2.2.b12
  forPractitioner: { text: "Programmes will enable graduates to select and apply specialist strategies and techniques that protect people in need.", rewrite: light, force: will, status: drafted }
  forBeneficiary: { text: "You will be able to choose and use specialist strategies to protect and support people who need it.", rewrite: full, force: will, status: drafted }
  author-agent-written: "Describe this as an outcome the statement expects ('will') of graduates of the subject at honours level (FHEQ 6, FQHEIS 10), about specialist strategies for public protection. Cite it as QAA (2022), Policing Subject Benchmark Statement, para 2.2, item 12, and set it beside 4.3.b5 and 4.3.b9. Do not call it one of the threshold standards of section 4 or a regulatory rule; it sits in the statement's discussion of the degree."
  author-agent-dialogue: "Raise it when a student plans a response to a safeguarding case. With a student, put it plainly in the second person; with staff, frame it as an outcome the course should make possible. Ask: \"Which strategy would you choose to protect this person, and why that one?\" Avoid quoting the paragraph at length or treating it as a pass mark."
- statement: qaa/policing-in-partnership-with-2022/2.2.b13
  forPractitioner: { text: "Programmes will enable graduates to develop knowledge of national policing strategies, for instance on counter terrorism.", rewrite: light, force: will, status: drafted }
  forBeneficiary: { text: "You will learn about national policing strategies, such as those on counter terrorism.", rewrite: full, force: will, status: drafted }
  author-agent-written: "Describe this as an outcome the statement expects ('will') of graduates of the subject at honours level (FHEQ 6, FQHEIS 10), about national strategies such as counter terrorism. Cite it as QAA (2022), Policing Subject Benchmark Statement, para 2.2, item 13, and set it beside 4.3.b5 and 4.4.b5. Do not call it one of the threshold standards of section 4 or a regulatory rule; it sits in the statement's discussion of the degree."
  author-agent-dialogue: "Raise it when a student asks how local policing links to national priorities. With a student, put it plainly in the second person; with staff, frame it as an outcome the course should make possible. Ask: \"How does a national strategy show up in everyday local policing?\" Avoid quoting the paragraph at length or treating it as a pass mark."
- statement: qaa/policing-in-partnership-with-2022/2.3
  forPractitioner: { text: "Plan the programme as a whole: each module should attend to reflective practice, critical thinking, decision-making, communication, ethics, EDI, evidence-based practice, problem-solving, styles of leadership and teamwork.", rewrite: light, force: should, status: drafted }
  forBeneficiary: { text: "not-applicable: a duty on those who design and run the course; the student meets its effect, not a standard to reach", rewrite: full, force: should, status: drafted }
  author-agent-written: "Describe this as an expectation ('should') on those who design and run Policing degrees, about skills planned across all modules: a course duty, not a student outcome. Cite it as QAA (2022), Policing Subject Benchmark Statement, para 2.3, and set it beside 2.2, 4.4 and qaa/fheq-2024/4.15.b9.1. Do not state it as law or as something students achieve; the statement is a sector reference point, not regulation."
  author-agent-dialogue: "Raise it when a team maps skills across modules. Frame it for the programme team as a design or delivery duty; with a student, explain only what it means for their own experience. Ask: \"Which module builds leadership and teamwork, and how is it assessed?\" Do not give it to a student as something they must achieve."
- statement: qaa/policing-in-partnership-with-2022/2.4
  forPractitioner: { text: "If you seek College of Policing licensing, you must build the NPC into the degree and map learning so every element appears in the design; expect regular and annual professional review.", rewrite: light, force: must, status: drafted }
  forBeneficiary: { text: "not-applicable: a duty on those who design and run the course; the student meets its effect, not a standard to reach", rewrite: full, force: must, status: drafted }
  author-agent-written: "Describe this as a requirement ('must') on those who design and run Policing degrees, about the National Policing Curriculum in licensed programmes: a course duty, not a student outcome. Cite it as QAA (2022), Policing Subject Benchmark Statement, para 2.4, and set it beside 1.4, 3.11 and the College of Policing in SB5. Do not state it as law or as something students achieve; the statement is a sector reference point, not regulation. Do not extend it to Policing degrees that do not seek a licence."
  author-agent-dialogue: "Raise it when a team plans to seek College of Policing licensing. Frame it for the programme team as a design or delivery duty; with a student, explain only what it means for their own experience. Ask: \"Where does the curriculum map show each NPC element taught and assessed?\" Do not give it to a student as something they must achieve."
- statement: qaa/policing-in-partnership-with-2022/2.6
  forPractitioner: { text: "Formally involve volunteers, such as special constables and police support volunteers, in the consultations that develop and review the programme, alongside staff associations.", rewrite: light, force: should, status: drafted }
  forBeneficiary: { text: "not-applicable: a duty on those who design and run the course; the student meets its effect, not a standard to reach", rewrite: full, force: should, status: drafted }
  author-agent-written: "Describe this as an expectation ('should') on those who design and run Policing degrees, about volunteers in programme consultation: a course duty, not a student outcome. Cite it as QAA (2022), Policing Subject Benchmark Statement, para 2.6, and set it beside 2.5, 2.7 and 2.20. Do not state it as law or as something students achieve; the statement is a sector reference point, not regulation."
  author-agent-dialogue: "Raise it when a team sets up programme consultation or review panels. Frame it for the programme team as a design or delivery duty; with a student, explain only what it means for their own experience. Ask: \"Who speaks for volunteers when this programme is reviewed?\" Do not give it to a student as something they must achieve."
- statement: qaa/policing-in-partnership-with-2022/2.9
  forPractitioner: { text: "When creating the degree, follow other professions in drawing on experienced practitioner-researchers; that evidence-based approach is a must and helps graduate skills transfer.", rewrite: light, force: must, status: drafted }
  forBeneficiary: { text: "not-applicable: a duty on those who design and run the course; the student meets its effect, not a standard to reach", rewrite: full, force: must, status: drafted }
  author-agent-written: "Describe this as a requirement ('must') on those who design and run Policing degrees, about practitioner-researchers informing degree design: a course duty, not a student outcome. Cite it as QAA (2022), Policing Subject Benchmark Statement, para 2.9, and set it beside 2.2.b2, 4.3.b11 and 3.13. Do not state it as law or as something students achieve; the statement is a sector reference point, not regulation."
  author-agent-dialogue: "Raise it when a team recruits staff or plans research-informed teaching. Frame it for the programme team as a design or delivery duty; with a student, explain only what it means for their own experience. Ask: \"Which practitioner-researchers shape the content of this degree?\" Do not give it to a student as something they must achieve."
- statement: qaa/policing-in-partnership-with-2022/2.11
  forPractitioner: { text: "Joint honours students will achieve the core subject and generic skills of Policing, adding others from the partner subject; leave room to explore the overlap.", rewrite: light, force: will, status: drafted }
  forBeneficiary: { text: "If you study Policing with another subject, you will gain the core skills of Policing, add others from your second subject and can explore where the two meet.", rewrite: full, force: will, status: drafted }
  author-agent-written: "Describe this as an outcome the statement expects ('will') of joint honours students at honours level (FHEQ 6, FQHEIS 10), about joint honours students and the core skills. Cite it as QAA (2022), Policing Subject Benchmark Statement, para 2.11, and set it beside 4.3, 4.4 and 2.10. Do not call it one of the threshold standards of section 4 or a regulatory rule; it sits in the statement's discussion of the degree."
  author-agent-dialogue: "Raise it when a joint honours student asks what they must cover. With a student, put it plainly in the second person; with staff, frame it as an outcome the course should make possible. Ask: \"Which of the threshold skills does your Policing half cover, and which come from your other subject?\" Avoid quoting the paragraph at length or treating it as a pass mark."
- statement: qaa/policing-in-partnership-with-2022/2.14
  forPractitioner: { text: "Require a final-year independent project or dissertation that each student must design, conduct and complete, in which they normally show mature research judgement, critical use of evidence, law and policy, and links to practice.", rewrite: light, force: must, status: drafted }
  forBeneficiary: { text: "In your final year you must design, carry out and complete your own research project or dissertation, dealing with its practical and ethical sides and linking research to policing practice and policy.", rewrite: full, force: must, status: drafted }
  author-agent-written: "Describe this as a requirement ('must') of final-year students on most policing, criminal justice and criminology programmes at honours level (FHEQ 6, FQHEIS 10), about the independent final-year project or dissertation. Cite it as QAA (2022), Policing Subject Benchmark Statement, para 2.14, and set it beside 2.2.b2, 4.4.b1 and qaa/fheq-2024/4.15.b6. Do not call it one of the threshold standards of section 4 or a regulatory rule; it sits in the statement's discussion of the degree."
  author-agent-dialogue: "Raise it when a student plans the final-year project. With a student, put it plainly in the second person; with staff, frame it as an outcome the course should make possible. Ask: \"What policing problem will your project tackle, and what ethical or access issues must you settle first?\" Avoid quoting the paragraph at length or treating it as a pass mark."
- statement: qaa/policing-in-partnership-with-2022/2.16
  forPractitioner: { text: "Set a clear institutional strategy for partnerships with agencies, covering whole courses or parts such as work placements, and plan for the sites, support and facilities they need.", rewrite: light, force: should, status: drafted }
  forBeneficiary: { text: "not-applicable: a duty on those who design and run the course; the student meets its effect, not a standard to reach", rewrite: full, force: should, status: drafted }
  author-agent-written: "Describe this as an expectation ('should') on those who design and run Policing degrees, about an institutional strategy for partnerships: a course duty, not a student outcome. Cite it as QAA (2022), Policing Subject Benchmark Statement, para 2.16, and set it beside 2.15, 2.17 to 2.19 and the QAA work-based learning guidance in SB6. Do not state it as law or as something students achieve; the statement is a sector reference point, not regulation."
  author-agent-dialogue: "Raise it when a team plans a partnership or work placements. Frame it for the programme team as a design or delivery duty; with a student, explain only what it means for their own experience. Ask: \"Which institutional strategy governs this partnership, and does it cover placements?\" Do not give it to a student as something they must achieve."
- statement: qaa/policing-in-partnership-with-2022/2.17
  forPractitioner: { text: "Partners must meet the relevant national qualifications framework (FHEQ or FQHEIS); the awarding organisation should carry the responsibility for assuring the standards.", rewrite: light, force: must, status: drafted }
  forBeneficiary: { text: "not-applicable: a duty on those who design and run the course; the student meets its effect, not a standard to reach", rewrite: full, force: must, status: drafted }
  author-agent-written: "Describe this as a requirement ('must') on those who design and run Policing degrees, about partners and the national qualifications framework: a course duty, not a student outcome. Cite it as QAA (2022), Policing Subject Benchmark Statement, para 2.17, and set it beside 2.18, 2.19 and the FHEQ honours descriptor (qaa/fheq-2024/4.15) and spine:6. Do not state it as law or as something students achieve; the statement is a sector reference point, not regulation."
  author-agent-dialogue: "Raise it when a team sets up co-created delivery with a police force. Frame it for the programme team as a design or delivery duty; with a student, explain only what it means for their own experience. Ask: \"How does the awarding body check that partner-delivered modules meet honours level?\" Do not give it to a student as something they must achieve."
- statement: qaa/policing-in-partnership-with-2022/2.18
  forPractitioner: { text: "As awarding body you must have arrangements that hold the academic standard of the award; where agencies deliver part or all of the course, run an effective process to manage and oversee the whole student experience.", rewrite: light, force: must, status: drafted }
  forBeneficiary: { text: "not-applicable: a duty on those who design and run the course; the student meets its effect, not a standard to reach", rewrite: full, force: must, status: drafted }
  author-agent-written: "Describe this as a requirement ('must') on those who design and run Policing degrees, about standards and student experience in partnerships: a course duty, not a student outcome. Cite it as QAA (2022), Policing Subject Benchmark Statement, para 2.18, and set it beside 2.17, 2.19 and 2.21. Do not state it as law or as something students achieve; the statement is a sector reference point, not regulation."
  author-agent-dialogue: "Raise it when another agency delivers part of the course. Frame it for the programme team as a design or delivery duty; with a student, explain only what it means for their own experience. Ask: \"Who oversees the student experience on the modules a partner delivers?\" Do not give it to a student as something they must achieve."
- statement: qaa/policing-in-partnership-with-2022/2.19
  forPractitioner: { text: "Put each partnership on a legally binding written agreement that sets out arrangements and risks; carry out due diligence during it and before renewal; keep governance records current and monitor continuously.", rewrite: light, force: should, status: drafted }
  forBeneficiary: { text: "not-applicable: a duty on those who design and run the course; the student meets its effect, not a standard to reach", rewrite: full, force: should, status: drafted }
  author-agent-written: "Describe this as an expectation ('should') on those who design and run Policing degrees, about written partnership agreements and due diligence: a course duty, not a student outcome. Cite it as QAA (2022), Policing Subject Benchmark Statement, para 2.19, and set it beside 2.16, 2.17 and 2.18. Do not state it as law or as something students achieve; the statement is a sector reference point, not regulation."
  author-agent-dialogue: "Raise it when a partnership is agreed or comes up for renewal. Frame it for the programme team as a design or delivery duty; with a student, explain only what it means for their own experience. Ask: \"When was due diligence last done on this partnership, and what did it find?\" Do not give it to a student as something they must achieve."
- statement: qaa/policing-in-partnership-with-2022/3.2.b1
  forPractitioner: { text: "Design the course so students learn to uphold professional standards and to decide on objective, impartial grounds, without bias or prejudice.", rewrite: light, force: should, status: drafted }
  forBeneficiary: { text: "not-applicable: a duty on course design; the student outcomes it serves are in 4.3", rewrite: full, force: should, status: drafted }
  author-agent-written: "Describe this as an expectation ('should') on those who design and run Policing degrees, about impartiality: a course duty, not a student outcome. Cite it as QAA (2022), Policing Subject Benchmark Statement, para 3.2, item 1, and set it beside 4.3.b7 and 4.3.b14. Do not state it as law or as something students achieve; the statement is a sector reference point, not regulation."
  author-agent-dialogue: "Raise it when a team checks core content against the five themes. Frame it for the programme team as a design or delivery duty; with a student, explain only what it means for their own experience. Ask: \"Where does the course make students test their own decisions for bias?\" Do not give it to a student as something they must achieve."
- statement: qaa/policing-in-partnership-with-2022/3.2.b2
  forPractitioner: { text: "Make content reflect the highest standards expected of people in policing, including being a role model.", rewrite: light, force: should, status: drafted }
  forBeneficiary: { text: "not-applicable: a duty on course design; the student outcomes it serves are in 4.3", rewrite: full, force: should, status: drafted }
  author-agent-written: "Describe this as an expectation ('should') on those who design and run Policing degrees, about integrity: a course duty, not a student outcome. Cite it as QAA (2022), Policing Subject Benchmark Statement, para 3.2, item 2, and set it beside 1.18 and 4.3.b7. Do not state it as law or as something students achieve; the statement is a sector reference point, not regulation."
  author-agent-dialogue: "Raise it when a team checks core content against the five themes. Frame it for the programme team as a design or delivery duty; with a student, explain only what it means for their own experience. Ask: \"Which module asks students to consider what being a role model means?\" Do not give it to a student as something they must achieve."
- statement: qaa/policing-in-partnership-with-2022/3.2.b3
  forPractitioner: { text: "Make content show that people in policing carry a responsibility to act in the best interests of society as a whole.", rewrite: light, force: should, status: drafted }
  forBeneficiary: { text: "not-applicable: a duty on course design; the student outcomes it serves are in 4.3", rewrite: full, force: should, status: drafted }
  author-agent-written: "Describe this as an expectation ('should') on those who design and run Policing degrees, about public service: a course duty, not a student outcome. Cite it as QAA (2022), Policing Subject Benchmark Statement, para 3.2, item 3, and set it beside 1.1 and 2.2.b11. Do not state it as law or as something students achieve; the statement is a sector reference point, not regulation."
  author-agent-dialogue: "Raise it when a team checks core content against the five themes. Frame it for the programme team as a design or delivery duty; with a student, explain only what it means for their own experience. Ask: \"How does the course show the tension between public service and other pressures?\" Do not give it to a student as something they must achieve."
- statement: qaa/policing-in-partnership-with-2022/3.2.b4
  forPractitioner: { text: "Design the award so students see why openness in actions, decisions and communication is needed of everyone working or volunteering in policing.", rewrite: light, force: should, status: drafted }
  forBeneficiary: { text: "not-applicable: a duty on course design; the student outcomes it serves are in 4.3", rewrite: full, force: should, status: drafted }
  author-agent-written: "Describe this as an expectation ('should') on those who design and run Policing degrees, about transparency: a course duty, not a student outcome. Cite it as QAA (2022), Policing Subject Benchmark Statement, para 3.2, item 4, and set it beside 4.3.b7 and 4.4.b2. Do not state it as law or as something students achieve; the statement is a sector reference point, not regulation."
  author-agent-dialogue: "Raise it when a team checks core content against the five themes. Frame it for the programme team as a design or delivery duty; with a student, explain only what it means for their own experience. Ask: \"Where do students practise explaining a decision openly to the public?\" Do not give it to a student as something they must achieve."
- statement: qaa/policing-in-partnership-with-2022/3.2.b5
  forPractitioner: { text: "Design the award so students both understand equality, diversity and inclusion and champion them in society.", rewrite: light, force: should, status: drafted }
  forBeneficiary: { text: "not-applicable: a duty on course design; the student outcomes it serves are in 4.3", rewrite: full, force: should, status: drafted }
  author-agent-written: "Describe this as an expectation ('should') on those who design and run Policing degrees, about diversity: a course duty, not a student outcome. Cite it as QAA (2022), Policing Subject Benchmark Statement, para 3.2, item 5, and set it beside 2.2.b5 and 4.3.b8. Do not state it as law or as something students achieve; the statement is a sector reference point, not regulation."
  author-agent-dialogue: "Raise it when a team checks core content against the five themes. Frame it for the programme team as a design or delivery duty; with a student, explain only what it means for their own experience. Ask: \"How does the course prepare students to champion inclusion, not only describe it?\" Do not give it to a student as something they must achieve."
- statement: qaa/policing-in-partnership-with-2022/3.11
  forPractitioner: { text: "For licensed PEQF programmes (PCDA, DHEP) assessment is required to blend theory with application, reflect the student's own policing setting, link to the NPC and meet the academic awarding body's rules; it should map theory to practice alongside IPS and FOC.", rewrite: light, force: must, status: drafted }
  forBeneficiary: { text: "not-applicable: a duty on those who design and run the course; the student meets its effect, not a standard to reach", rewrite: full, force: must, status: drafted }
  author-agent-written: "Describe this as a requirement ('must') on those who design and run Policing degrees, about assessment in licensed PEQF programmes: a course duty, not a student outcome. Cite it as QAA (2022), Policing Subject Benchmark Statement, para 3.11, and set it beside 2.4, 3.12 and 3.13. Do not state it as law or as something students achieve; the statement is a sector reference point, not regulation. Do not apply it to unlicensed degrees, which may not assess practical policing skills (3.12)."
  author-agent-dialogue: "Raise it when a team designs assessment for a PCDA or DHEP. Frame it for the programme team as a design or delivery duty; with a student, explain only what it means for their own experience. Ask: \"How does each assessment show progress towards Independent Patrol Status as well as academic credit?\" Do not give it to a student as something they must achieve."
- statement: qaa/policing-in-partnership-with-2022/3.13
  forPractitioner: { text: "Make every assessment applied: blend theory and practice, test academic and workforce-relevant skills together, and let all students explore contemporary policing critically, with debate and current research behind their learning.", rewrite: light, force: should, status: drafted }
  forBeneficiary: { text: "not-applicable: a duty on those who design and run the course; the student meets its effect, not a standard to reach", rewrite: full, force: should, status: drafted }
  author-agent-written: "Describe this as an expectation ('should') on those who design and run Policing degrees, about applied assessment blending theory and practice: a course duty, not a student outcome. Cite it as QAA (2022), Policing Subject Benchmark Statement, para 3.13, and set it beside 3.14.b1 to 3.14.b10, 3.15 and 4.3.b11. Do not state it as law or as something students achieve; the statement is a sector reference point, not regulation."
  author-agent-dialogue: "Raise it when a team reviews whether assessments are applied enough. Frame it for the programme team as a design or delivery duty; with a student, explain only what it means for their own experience. Ask: \"Which assessment in this module asks students to apply theory to a real policing problem?\" Do not give it to a student as something they must achieve."
- statement: qaa/policing-in-partnership-with-2022/3.14
  forPractitioner: { text: "Co-design assessments with police practitioners or other employers and keep the evidence: that is a must. Have an assessment strategy that shows students reaching the required level and supports their learning.", rewrite: light, force: must, status: drafted }
  forBeneficiary: { text: "not-applicable: a duty on those who design and run the course; the student meets its effect, not a standard to reach", rewrite: full, force: must, status: drafted }
  author-agent-written: "Describe this as a requirement ('must') on those who design and run Policing degrees, about co-designed assessment and an assessment strategy: a course duty, not a student outcome. Cite it as QAA (2022), Policing Subject Benchmark Statement, para 3.14, and set it beside 3.14.b1 to 3.14.b10, 3.16 and 2.5. Do not state it as law or as something students achieve; the statement is a sector reference point, not regulation."
  author-agent-dialogue: "Raise it when a team plans or revalidates its assessment strategy. Frame it for the programme team as a design or delivery duty; with a student, explain only what it means for their own experience. Ask: \"Which employer helped design this assessment, and what record shows it?\" Do not give it to a student as something they must achieve."
- statement: qaa/policing-in-partnership-with-2022/3.14.b1
  forPractitioner: { text: "Align each assessment directly with the module and course learning outcomes.", rewrite: light, force: should, status: drafted }
  forBeneficiary: { text: "not-applicable: a duty on those who design and run the course; the student meets its effect, not a standard to reach", rewrite: full, force: should, status: drafted }
  author-agent-written: "Describe this as an expectation ('should') on those who design and run Policing degrees, about assessment aligned to outcomes: a course duty, not a student outcome. Cite it as QAA (2022), Policing Subject Benchmark Statement, para 3.14, item 1, and set it beside 3.14.b2 and 3.14.b3. Do not state it as law or as something students achieve; the statement is a sector reference point, not regulation."
  author-agent-dialogue: "Raise it when a team checks its assessment strategy against the principles and safeguards. Frame it for the programme team as a design or delivery duty; with a student, explain only what it means for their own experience. Ask: \"Which learning outcome does this assessment test, and is any outcome left untested?\" Do not give it to a student as something they must achieve."
- statement: qaa/policing-in-partnership-with-2022/3.14.b2
  forPractitioner: { text: "Make assessments measure the knowledge, understanding and skills students have actually gained.", rewrite: light, force: should, status: drafted }
  forBeneficiary: { text: "not-applicable: a duty on those who design and run the course; the student meets its effect, not a standard to reach", rewrite: full, force: should, status: drafted }
  author-agent-written: "Describe this as an expectation ('should') on those who design and run Policing degrees, about measuring knowledge, understanding and skills: a course duty, not a student outcome. Cite it as QAA (2022), Policing Subject Benchmark Statement, para 3.14, item 2, and set it beside 4.3 and 4.4. Do not state it as law or as something students achieve; the statement is a sector reference point, not regulation."
  author-agent-dialogue: "Raise it when a team checks its assessment strategy against the principles and safeguards. Frame it for the programme team as a design or delivery duty; with a student, explain only what it means for their own experience. Ask: \"What does this assessment tell you about a student's skills, not only their knowledge?\" Do not give it to a student as something they must achieve."
- statement: qaa/policing-in-partnership-with-2022/3.14.b3
  forPractitioner: { text: "Assess students on the core of the learning outcomes and on what the course actually teaches.", rewrite: light, force: should, status: drafted }
  forBeneficiary: { text: "not-applicable: a duty on those who design and run the course; the student meets its effect, not a standard to reach", rewrite: full, force: should, status: drafted }
  author-agent-written: "Describe this as an expectation ('should') on those who design and run Policing degrees, about assessing the central aspects of outcomes: a course duty, not a student outcome. Cite it as QAA (2022), Policing Subject Benchmark Statement, para 3.14, item 3, and set it beside 3.14.b1. Do not state it as law or as something students achieve; the statement is a sector reference point, not regulation."
  author-agent-dialogue: "Raise it when a team checks its assessment strategy against the principles and safeguards. Frame it for the programme team as a design or delivery duty; with a student, explain only what it means for their own experience. Ask: \"Does this assessment test something the module never taught?\" Do not give it to a student as something they must achieve."
- statement: qaa/policing-in-partnership-with-2022/3.14.b4
  forPractitioner: { text: "Keep assessment workload consistent and fair across modules of the same credit value.", rewrite: light, force: should, status: drafted }
  forBeneficiary: { text: "not-applicable: a duty on those who design and run the course; the student meets its effect, not a standard to reach", rewrite: full, force: should, status: drafted }
  author-agent-written: "Describe this as an expectation ('should') on those who design and run Policing degrees, about consistent workload and credit: a course duty, not a student outcome. Cite it as QAA (2022), Policing Subject Benchmark Statement, para 3.14, item 4, and set it beside 3.14.b5. Do not state it as law or as something students achieve; the statement is a sector reference point, not regulation."
  author-agent-dialogue: "Raise it when a team checks its assessment strategy against the principles and safeguards. Frame it for the programme team as a design or delivery duty; with a student, explain only what it means for their own experience. Ask: \"Do two modules of equal credit ask for very different amounts of assessed work?\" Do not give it to a student as something they must achieve."
- statement: qaa/policing-in-partnership-with-2022/3.14.b5
  forPractitioner: { text: "Sequence assessments so they build students' development from module to module and level to level.", rewrite: light, force: should, status: drafted }
  forBeneficiary: { text: "not-applicable: a duty on those who design and run the course; the student meets its effect, not a standard to reach", rewrite: full, force: should, status: drafted }
  author-agent-written: "Describe this as an expectation ('should') on those who design and run Policing degrees, about progression across modules and levels: a course duty, not a student outcome. Cite it as QAA (2022), Policing Subject Benchmark Statement, para 3.14, item 5, and set it beside 2.10 and spine:6. Do not state it as law or as something students achieve; the statement is a sector reference point, not regulation."
  author-agent-dialogue: "Raise it when a team checks its assessment strategy against the principles and safeguards. Frame it for the programme team as a design or delivery duty; with a student, explain only what it means for their own experience. Ask: \"How does the final-year assessment build on what was assessed in earlier years?\" Do not give it to a student as something they must achieve."
- statement: qaa/policing-in-partnership-with-2022/3.14.b6
  forPractitioner: { text: "Set assessments that reward deep, active and reflective learning rather than recall.", rewrite: light, force: should, status: drafted }
  forBeneficiary: { text: "not-applicable: a duty on those who design and run the course; the student meets its effect, not a standard to reach", rewrite: full, force: should, status: drafted }
  author-agent-written: "Describe this as an expectation ('should') on those who design and run Policing degrees, about deep, active, reflective learning: a course duty, not a student outcome. Cite it as QAA (2022), Policing Subject Benchmark Statement, para 3.14, item 6, and set it beside 3.15 and 4.3.b18. Do not state it as law or as something students achieve; the statement is a sector reference point, not regulation."
  author-agent-dialogue: "Raise it when a team checks its assessment strategy against the principles and safeguards. Frame it for the programme team as a design or delivery duty; with a student, explain only what it means for their own experience. Ask: \"Could a student pass this assessment by memorising alone?\" Do not give it to a student as something they must achieve."
- statement: qaa/policing-in-partnership-with-2022/3.14.b7
  forPractitioner: { text: "Use assessment to improve student learning, not only to grade it.", rewrite: light, force: should, status: drafted }
  forBeneficiary: { text: "not-applicable: a duty on those who design and run the course; the student meets its effect, not a standard to reach", rewrite: full, force: should, status: drafted }
  author-agent-written: "Describe this as an expectation ('should') on those who design and run Policing degrees, about assessment that improves learning: a course duty, not a student outcome. Cite it as QAA (2022), Policing Subject Benchmark Statement, para 3.14, item 7, and set it beside 3.14.b10 and 3.16. Do not state it as law or as something students achieve; the statement is a sector reference point, not regulation."
  author-agent-dialogue: "Raise it when a team checks its assessment strategy against the principles and safeguards. Frame it for the programme team as a design or delivery duty; with a student, explain only what it means for their own experience. Ask: \"What does a student learn from doing this assessment, beyond the mark?\" Do not give it to a student as something they must achieve."
- statement: qaa/policing-in-partnership-with-2022/3.14.b8
  forPractitioner: { text: "Assess skills and whether students can carry them into new settings.", rewrite: light, force: should, status: drafted }
  forBeneficiary: { text: "not-applicable: a duty on those who design and run the course; the student meets its effect, not a standard to reach", rewrite: full, force: should, status: drafted }
  author-agent-written: "Describe this as an expectation ('should') on those who design and run Policing degrees, about skills and their transfer: a course duty, not a student outcome. Cite it as QAA (2022), Policing Subject Benchmark Statement, para 3.14, item 8, and set it beside 4.4.b8 and 3.13. Do not state it as law or as something students achieve; the statement is a sector reference point, not regulation."
  author-agent-dialogue: "Raise it when a team checks its assessment strategy against the principles and safeguards. Frame it for the programme team as a design or delivery duty; with a student, explain only what it means for their own experience. Ask: \"Where does an assessment ask students to use a skill in a new setting?\" Do not give it to a student as something they must achieve."
- statement: qaa/policing-in-partnership-with-2022/3.14.b9
  forPractitioner: { text: "Build inclusion into the core of every assessment so all learning styles are met and students have a comparable experience: a must.", rewrite: light, force: must, status: drafted }
  forBeneficiary: { text: "not-applicable: a duty on those who design and run the course; the student meets its effect, not a standard to reach", rewrite: full, force: must, status: drafted }
  author-agent-written: "Describe this as a requirement ('must') on those who design and run Policing degrees, about inclusive assessment: a course duty, not a student outcome. Cite it as QAA (2022), Policing Subject Benchmark Statement, para 3.14, item 9, and set it beside 1.19 and 3.15. Do not state it as law or as something students achieve; the statement is a sector reference point, not regulation."
  author-agent-dialogue: "Raise it when a team checks its assessment strategy against the principles and safeguards. Frame it for the programme team as a design or delivery duty; with a student, explain only what it means for their own experience. Ask: \"Which students might this assessment disadvantage, and what is the alternative?\" Do not give it to a student as something they must achieve."
- statement: qaa/policing-in-partnership-with-2022/3.14.b10
  forPractitioner: { text: "Show in the assessment strategy that every student receives timely, detailed and relevant feedback: a must.", rewrite: light, force: must, status: drafted }
  forBeneficiary: { text: "not-applicable: a duty on those who design and run the course; the student meets its effect, not a standard to reach", rewrite: full, force: must, status: drafted }
  author-agent-written: "Describe this as a requirement ('must') on those who design and run Policing degrees, about timely, detailed feedback: a course duty, not a student outcome. Cite it as QAA (2022), Policing Subject Benchmark Statement, para 3.14, item 10, and set it beside 3.16 and 3.14.b7. Do not state it as law or as something students achieve; the statement is a sector reference point, not regulation."
  author-agent-dialogue: "Raise it when a team checks its assessment strategy against the principles and safeguards. Frame it for the programme team as a design or delivery duty; with a student, explain only what it means for their own experience. Ask: \"How long do students wait for feedback, and can they use it before the next assessment?\" Do not give it to a student as something they must achieve."
- statement: qaa/policing-in-partnership-with-2022/3.15
  forPractitioner: { text: "Use varied and innovative assessment (written, oral, visual; individual and group; independent research), show how student voice informs its design, and build in constructive alignment, clear criteria, timeliness, adaptability and constructive feedback.", rewrite: light, force: should, status: drafted }
  forBeneficiary: { text: "not-applicable: a duty on those who design and run the course; the student meets its effect, not a standard to reach", rewrite: full, force: should, status: drafted }
  author-agent-written: "Describe this as an expectation ('should') on those who design and run Policing degrees, about varied, participative and inclusive assessment: a course duty, not a student outcome. Cite it as QAA (2022), Policing Subject Benchmark Statement, para 3.15, and set it beside 3.14.b9, 3.16 and 1.19. Do not state it as law or as something students achieve; the statement is a sector reference point, not regulation."
  author-agent-dialogue: "Raise it when a team redesigns assessment or gathers student views. Frame it for the programme team as a design or delivery duty; with a student, explain only what it means for their own experience. Ask: \"How did students' views shape the assessments in this programme?\" Do not give it to a student as something they must achieve."
- statement: qaa/policing-in-partnership-with-2022/3.16
  forPractitioner: { text: "Give students full details of every assessment and its criteria or rubric (a must); balance diagnostic, formative and summative assessment; give practice with challenging questions; consider applied forms such as policy briefs and digital portfolios.", rewrite: light, force: must, status: drafted }
  forBeneficiary: { text: "not-applicable: a duty on those who design and run the course; the student meets its effect, not a standard to reach", rewrite: full, force: must, status: drafted }
  author-agent-written: "Describe this as a requirement ('must') on those who design and run Policing degrees, about full assessment information and a balance of methods: a course duty, not a student outcome. Cite it as QAA (2022), Policing Subject Benchmark Statement, para 3.16, and set it beside 3.14.b10, 3.15 and 3.17. Do not state it as law or as something students achieve; the statement is a sector reference point, not regulation."
  author-agent-dialogue: "Raise it when a student is unsure how they will be assessed, or a team writes module guides. Frame it for the programme team as a design or delivery duty; with a student, explain only what it means for their own experience. Ask: \"Where can a student find the full brief and rubric for each assessment?\" Do not give it to a student as something they must achieve."
- statement: qaa/policing-in-partnership-with-2022/3.17
  forPractitioner: { text: "Review assessments on a regular cycle so they stay current and valid and give little room for academic misconduct.", rewrite: light, force: should, status: drafted }
  forBeneficiary: { text: "not-applicable: a duty on those who design and run the course; the student meets its effect, not a standard to reach", rewrite: full, force: should, status: drafted }
  author-agent-written: "Describe this as an expectation ('should') on those who design and run Policing degrees, about reviewing assessments for currency and integrity: a course duty, not a student outcome. Cite it as QAA (2022), Policing Subject Benchmark Statement, para 3.17, and set it beside 1.27, 2.20 and 3.14. Do not state it as law or as something students achieve; the statement is a sector reference point, not regulation."
  author-agent-dialogue: "Raise it when a team runs its annual review or meets an integrity concern. Frame it for the programme team as a design or delivery duty; with a student, explain only what it means for their own experience. Ask: \"When was this assessment last reviewed, and what changed?\" Do not give it to a student as something they must achieve."
- statement: qaa/policing-in-partnership-with-2022/4.2
  forPractitioner: { text: "Decide what evidence shows achievement above the threshold, and use the Annex D descriptions of the four honours classes when you judge it.", rewrite: light, force: should, status: drafted }
  forBeneficiary: { text: "not-applicable: tells the course how to judge achievement above the threshold; the student-facing standards are 4.3 and 4.4", rewrite: full, force: should, status: drafted }
  author-agent-written: "Describe this as an expectation ('should') on those who design and run Policing degrees, about Annex D for achievement above the threshold: a course duty, not a student outcome. Cite it as QAA (2022), Policing Subject Benchmark Statement, para 4.2, and set it beside 4.1, 4.3, 4.4 and the Annex D bands (qaa/fheq-2024/annex-d; SL6 of std:doc:qaa-fheq-2024-framework). Do not state it as law or as something students achieve; the statement is a sector reference point, not regulation."
  author-agent-dialogue: "Raise it when a team sets marking criteria or a student asks what a good degree looks like. Frame it for the programme team as a design or delivery duty; with a student, explain only what it means for their own experience. Ask: \"How do your marking criteria separate a 2:1 from a 2:2 in this module?\" Do not give it to a student as something they must achieve."
- statement: qaa/policing-in-partnership-with-2022/4.3.b1
  forPractitioner: { text: "At threshold, graduates apply an in-depth grasp of how policing, criminal justice and criminology interlock to their professional responsibilities, now or later.", rewrite: light, force: threshold, status: drafted }
  forBeneficiary: { text: "At the threshold, you can apply a deep understanding of how policing, criminal justice and criminology fit together to your current or future work.", rewrite: full, force: threshold, status: drafted }
  author-agent-written: "Describe this as a threshold standard for the honours degree in Policing (FHEQ level 6, FQHEIS level 10): the minimum a graduate has shown, here the interdisciplinary nature of policing. Cite it as QAA (2022), Policing Subject Benchmark Statement, para 4.3, item 1, and set it beside 2.2.b8 and qaa/fheq-2024/4.15.b1 (qaa/fqheis-2024/4.16.b1). Do not present it as a regulatory rule or as the level most graduates reach, since most exceed it; for the classes above it point to Annex D (qaa/fheq-2024/annex-d)."
  author-agent-dialogue: "Raise it when a student asks how criminology modules connect to policing work. With a student, say in plain second-person words what it asks of them; with staff, frame it as the least every honours graduate must be able to show. Ask: \"Can you show how a criminological idea changed how you would handle a policing task?\" Do not read the issuer's list aloud or imply that this minimum is what most students reach."
- statement: qaa/policing-in-partnership-with-2022/4.3.b2
  forPractitioner: { text: "At threshold, graduates understand and evaluate the way criminal law is applied to policing.", rewrite: light, force: threshold, status: drafted }
  forBeneficiary: { text: "At the threshold, you understand how criminal law is applied in policing and can judge how well it is applied.", rewrite: full, force: threshold, status: drafted }
  author-agent-written: "Describe this as a threshold standard for the honours degree in Policing (FHEQ level 6, FQHEIS level 10): the minimum a graduate has shown, here criminal law applied to policing. Cite it as QAA (2022), Policing Subject Benchmark Statement, para 4.3, item 2, and set it beside 2.2.b10 and qaa/fheq-2024/4.15.b7. Do not present it as a regulatory rule or as the level most graduates reach, since most exceed it; for the classes above it point to Annex D (qaa/fheq-2024/annex-d)."
  author-agent-dialogue: "Raise it when a student studies powers, offences or case law. With a student, say in plain second-person words what it asks of them; with staff, frame it as the least every honours graduate must be able to show. Ask: \"In this case, was the law applied well, and how would you judge it?\" Do not read the issuer's list aloud or imply that this minimum is what most students reach."
- statement: qaa/policing-in-partnership-with-2022/4.3.b3
  forPractitioner: { text: "At threshold, graduates bring a deep knowledge of what makes policing safe, lawful and effective to bear on practice.", rewrite: light, force: threshold, status: drafted }
  forBeneficiary: { text: "At the threshold, you can use detailed knowledge of what makes policing safe, lawful and effective.", rewrite: full, force: threshold, status: drafted }
  author-agent-written: "Describe this as a threshold standard for the honours degree in Policing (FHEQ level 6, FQHEIS level 10): the minimum a graduate has shown, here safe, lawful and effective policing. Cite it as QAA (2022), Policing Subject Benchmark Statement, para 4.3, item 3, and set it beside 2.2.b1 and qaa/fheq-2024/4.15.b1. Do not present it as a regulatory rule or as the level most graduates reach, since most exceed it; for the classes above it point to Annex D (qaa/fheq-2024/annex-d)."
  author-agent-dialogue: "Raise it when a student reviews an incident or scenario. With a student, say in plain second-person words what it asks of them; with staff, frame it as the least every honours graduate must be able to show. Ask: \"What made this response safe, lawful and effective, or not?\" Do not read the issuer's list aloud or imply that this minimum is what most students reach."
- statement: qaa/policing-in-partnership-with-2022/4.3.b4
  forPractitioner: { text: "At threshold, graduates understand several policing specialisms, for example response, neighbourhood, roads, intelligence and investigation.", rewrite: light, force: threshold, status: drafted }
  forBeneficiary: { text: "At the threshold, you understand several policing specialisms, such as response, community and roads policing, intelligence and investigation.", rewrite: full, force: threshold, status: drafted }
  author-agent-written: "Describe this as a threshold standard for the honours degree in Policing (FHEQ level 6, FQHEIS level 10): the minimum a graduate has shown, here policing specialisms. Cite it as QAA (2022), Policing Subject Benchmark Statement, para 4.3, item 4, and set it beside 2.2.b4 and 3.3. Do not present it as a regulatory rule or as the level most graduates reach, since most exceed it; for the classes above it point to Annex D (qaa/fheq-2024/annex-d)."
  author-agent-dialogue: "Raise it when a student considers which area of policing to work in. With a student, say in plain second-person words what it asks of them; with staff, frame it as the least every honours graduate must be able to show. Ask: \"Which specialism could you explain to a new recruit, and which could you not yet?\" Do not read the issuer's list aloud or imply that this minimum is what most students reach."
- statement: qaa/policing-in-partnership-with-2022/4.3.b5
  forPractitioner: { text: "At threshold, graduates select and apply fitting contemporary policing strategies to complex, interconnected situations.", rewrite: light, force: threshold, status: drafted }
  forBeneficiary: { text: "At the threshold, you can choose and use suitable modern policing strategies in complex situations where many factors interact.", rewrite: full, force: threshold, status: drafted }
  author-agent-written: "Describe this as a threshold standard for the honours degree in Policing (FHEQ level 6, FQHEIS level 10): the minimum a graduate has shown, here choosing strategies for complex contexts. Cite it as QAA (2022), Policing Subject Benchmark Statement, para 4.3, item 5, and set it beside 2.2.b12 and qaa/fheq-2024/4.15.b9.2. Do not present it as a regulatory rule or as the level most graduates reach, since most exceed it; for the classes above it point to Annex D (qaa/fheq-2024/annex-d)."
  author-agent-dialogue: "Raise it when a student plans a response to a complex scenario. With a student, say in plain second-person words what it asks of them; with staff, frame it as the least every honours graduate must be able to show. Ask: \"Why did you choose that strategy over the alternatives here?\" Do not read the issuer's list aloud or imply that this minimum is what most students reach."
- statement: qaa/policing-in-partnership-with-2022/4.3.b6
  forPractitioner: { text: "At threshold, graduates apply broad knowledge of digital policing and of crime that involves technology.", rewrite: light, force: threshold, status: drafted }
  forBeneficiary: { text: "At the threshold, you can use a broad knowledge of digital policing and of crime that involves technology.", rewrite: full, force: threshold, status: drafted }
  author-agent-written: "Describe this as a threshold standard for the honours degree in Policing (FHEQ level 6, FQHEIS level 10): the minimum a graduate has shown, here digital policing and technology-related crime. Cite it as QAA (2022), Policing Subject Benchmark Statement, para 4.3, item 6, and set it beside 2.2.b7 and 4.4.b9. Do not present it as a regulatory rule or as the level most graduates reach, since most exceed it; for the classes above it point to Annex D (qaa/fheq-2024/annex-d)."
  author-agent-dialogue: "Raise it when a student meets digital evidence or online offending. With a student, say in plain second-person words what it asks of them; with staff, frame it as the least every honours graduate must be able to show. Ask: \"What digital evidence would you look for in this case, and how would you secure it?\" Do not read the issuer's list aloud or imply that this minimum is what most students reach."
- statement: qaa/policing-in-partnership-with-2022/4.3.b7
  forPractitioner: { text: "At threshold, graduates understand and adopt an ethical stance matching the service's highest professional values and standards.", rewrite: light, force: threshold, status: drafted }
  forBeneficiary: { text: "At the threshold, you understand and take an ethical approach that matches the highest professional values of the police service.", rewrite: full, force: threshold, status: drafted }
  author-agent-written: "Describe this as a threshold standard for the honours degree in Policing (FHEQ level 6, FQHEIS level 10): the minimum a graduate has shown, here an ethical approach and professional values. Cite it as QAA (2022), Policing Subject Benchmark Statement, para 4.3, item 7, and set it beside 1.18, 3.2.b2 and qaa/fheq-2024/annex-d/professional/r2/3rd. Do not present it as a regulatory rule or as the level most graduates reach, since most exceed it; for the classes above it point to Annex D (qaa/fheq-2024/annex-d)."
  author-agent-dialogue: "Raise it when a student faces an ethical dilemma or discusses misconduct. With a student, say in plain second-person words what it asks of them; with staff, frame it as the least every honours graduate must be able to show. Ask: \"Which professional value guided your choice here?\" Do not read the issuer's list aloud or imply that this minimum is what most students reach."
- statement: qaa/policing-in-partnership-with-2022/4.3.b8
  forPractitioner: { text: "At threshold, graduates take personal responsibility for promoting equality, diversity, inclusion and human rights.", rewrite: light, force: threshold, status: drafted }
  forBeneficiary: { text: "At the threshold, you take personal responsibility for promoting equality, diversity, inclusion and human rights.", rewrite: full, force: threshold, status: drafted }
  author-agent-written: "Describe this as a threshold standard for the honours degree in Policing (FHEQ level 6, FQHEIS level 10): the minimum a graduate has shown, here promoting equality, diversity, inclusion and human rights. Cite it as QAA (2022), Policing Subject Benchmark Statement, para 4.3, item 8, and set it beside 2.2.b5, 3.2.b5 and 4.4.b6. Do not present it as a regulatory rule or as the level most graduates reach, since most exceed it; for the classes above it point to Annex D (qaa/fheq-2024/annex-d)."
  author-agent-dialogue: "Raise it when a scenario raises fairness, bias or rights. With a student, say in plain second-person words what it asks of them; with staff, frame it as the least every honours graduate must be able to show. Ask: \"What did you personally do in that situation to protect someone's rights?\" Do not read the issuer's list aloud or imply that this minimum is what most students reach."
- statement: qaa/policing-in-partnership-with-2022/4.3.b9
  forPractitioner: { text: "At threshold, graduates synthesise specialist, interconnected theories and methods for supporting victims, witnesses and people who are vulnerable or at risk.", rewrite: light, force: threshold, status: drafted }
  forBeneficiary: { text: "At the threshold, you can combine specialist theories and methods to support victims, witnesses and people who are vulnerable or at risk.", rewrite: full, force: threshold, status: drafted }
  author-agent-written: "Describe this as a threshold standard for the honours degree in Policing (FHEQ level 6, FQHEIS level 10): the minimum a graduate has shown, here supporting victims, witnesses and the vulnerable. Cite it as QAA (2022), Policing Subject Benchmark Statement, para 4.3, item 9, and set it beside 2.2.b11 and qaa/fheq-2024/4.15.b3.1. Do not present it as a regulatory rule or as the level most graduates reach, since most exceed it; for the classes above it point to Annex D (qaa/fheq-2024/annex-d)."
  author-agent-dialogue: "Raise it when a student works on a victim or safeguarding case. With a student, say in plain second-person words what it asks of them; with staff, frame it as the least every honours graduate must be able to show. Ask: \"Which ideas did you draw together to decide how to support this person?\" Do not read the issuer's list aloud or imply that this minimum is what most students reach."
- statement: qaa/policing-in-partnership-with-2022/4.3.b10
  forPractitioner: { text: "At threshold, graduates adopt specialist, interconnected theories and methods to prevent and detect crime and to handle suspects and offenders.", rewrite: light, force: threshold, status: drafted }
  forBeneficiary: { text: "At the threshold, you can use specialist theories and methods to prevent and detect crime and to deal with suspects and offenders.", rewrite: full, force: threshold, status: drafted }
  author-agent-written: "Describe this as a threshold standard for the honours degree in Policing (FHEQ level 6, FQHEIS level 10): the minimum a graduate has shown, here preventing and detecting crime; suspects and offenders. Cite it as QAA (2022), Policing Subject Benchmark Statement, para 4.3, item 10, and set it beside 4.3.b9 and 2.2.b10. Do not present it as a regulatory rule or as the level most graduates reach, since most exceed it; for the classes above it point to Annex D (qaa/fheq-2024/annex-d)."
  author-agent-dialogue: "Raise it when a student plans an investigation or crime prevention measure. With a student, say in plain second-person words what it asks of them; with staff, frame it as the least every honours graduate must be able to show. Ask: \"What theory supports the prevention approach you chose?\" Do not read the issuer's list aloud or imply that this minimum is what most students reach."
- statement: qaa/policing-in-partnership-with-2022/4.3.b11
  forPractitioner: { text: "At threshold, graduates critically evaluate evidence-based research and apply it to complex policing problems.", rewrite: light, force: threshold, status: drafted }
  forBeneficiary: { text: "At the threshold, you can critically judge research evidence and use it on complex policing problems.", rewrite: full, force: threshold, status: drafted }
  author-agent-written: "Describe this as a threshold standard for the honours degree in Policing (FHEQ level 6, FQHEIS level 10): the minimum a graduate has shown, here evidence-based research in policing. Cite it as QAA (2022), Policing Subject Benchmark Statement, para 4.3, item 11, and set it beside 2.2.b2, 2.2.b3 and qaa/fheq-2024/4.15.b3.2. Do not present it as a regulatory rule or as the level most graduates reach, since most exceed it; for the classes above it point to Annex D (qaa/fheq-2024/annex-d)."
  author-agent-dialogue: "Raise it when a student cites research in an assignment or proposes a change in practice. With a student, say in plain second-person words what it asks of them; with staff, frame it as the least every honours graduate must be able to show. Ask: \"How strong is the evidence behind that study, and does it fit this setting?\" Do not read the issuer's list aloud or imply that this minimum is what most students reach."
- statement: qaa/policing-in-partnership-with-2022/4.3.b12
  forPractitioner: { text: "At threshold, graduates select and apply specialist strategies, methods and research evidence to complex problem solving.", rewrite: light, force: threshold, status: drafted }
  forBeneficiary: { text: "At the threshold, you can choose and use specialist methods and research evidence to work through complex problems.", rewrite: full, force: threshold, status: drafted }
  author-agent-written: "Describe this as a threshold standard for the honours degree in Policing (FHEQ level 6, FQHEIS level 10): the minimum a graduate has shown, here problem solving with evidence. Cite it as QAA (2022), Policing Subject Benchmark Statement, para 4.3, item 12, and set it beside 2.2.b3 and qaa/fheq-2024/4.15.b7. Do not present it as a regulatory rule or as the level most graduates reach, since most exceed it; for the classes above it point to Annex D (qaa/fheq-2024/annex-d)."
  author-agent-dialogue: "Raise it when a student tackles a recurring local problem. With a student, say in plain second-person words what it asks of them; with staff, frame it as the least every honours graduate must be able to show. Ask: \"What evidence told you this approach would solve the problem?\" Do not read the issuer's list aloud or imply that this minimum is what most students reach."
- statement: qaa/policing-in-partnership-with-2022/4.3.b13
  forPractitioner: { text: "At threshold, graduates make informed decisions in complex, unpredictable, interconnected situations, grounded in critical thinking and evidence.", rewrite: light, force: threshold, status: drafted }
  forBeneficiary: { text: "At the threshold, you can make informed decisions in complex and unpredictable situations, based on critical thinking and evidence.", rewrite: full, force: threshold, status: drafted }
  author-agent-written: "Describe this as a threshold standard for the honours degree in Policing (FHEQ level 6, FQHEIS level 10): the minimum a graduate has shown, here informed decisions in complex situations. Cite it as QAA (2022), Policing Subject Benchmark Statement, para 4.3, item 13, and set it beside 1.15 and qaa/fheq-2024/4.15.b9.2 (qaa/fqheis-2024/4.16.b9.2). Do not present it as a regulatory rule or as the level most graduates reach, since most exceed it; for the classes above it point to Annex D (qaa/fheq-2024/annex-d)."
  author-agent-dialogue: "Raise it when a student reflects on a decision under pressure. With a student, say in plain second-person words what it asks of them; with staff, frame it as the least every honours graduate must be able to show. Ask: \"What did you know, and not know, when you made that decision?\" Do not read the issuer's list aloud or imply that this minimum is what most students reach."
- statement: qaa/policing-in-partnership-with-2022/4.3.b14
  forPractitioner: { text: "At threshold, graduates act within selected guidelines and exercise professional discretion.", rewrite: light, force: threshold, status: drafted }
  forBeneficiary: { text: "At the threshold, you can work within the relevant guidelines and use professional discretion well.", rewrite: full, force: threshold, status: drafted }
  author-agent-written: "Describe this as a threshold standard for the honours degree in Policing (FHEQ level 6, FQHEIS level 10): the minimum a graduate has shown, here guidelines and professional discretion. Cite it as QAA (2022), Policing Subject Benchmark Statement, para 4.3, item 14, and set it beside 3.2.b1 and qaa/fheq-2024/annex-d/professional/r2/3rd. Do not present it as a regulatory rule or as the level most graduates reach, since most exceed it; for the classes above it point to Annex D (qaa/fheq-2024/annex-d)."
  author-agent-dialogue: "Raise it when a scenario leaves room for discretion. With a student, say in plain second-person words what it asks of them; with staff, frame it as the least every honours graduate must be able to show. Ask: \"Where did the guidance stop, and how did you use your discretion?\" Do not read the issuer's list aloud or imply that this minimum is what most students reach."
- statement: qaa/policing-in-partnership-with-2022/4.3.b15
  forPractitioner: { text: "At threshold, graduates understand and apply the skills of managing conflict.", rewrite: light, force: threshold, status: drafted }
  forBeneficiary: { text: "At the threshold, you understand and can use the skills of managing conflict.", rewrite: full, force: threshold, status: drafted }
  author-agent-written: "Describe this as a threshold standard for the honours degree in Policing (FHEQ level 6, FQHEIS level 10): the minimum a graduate has shown, here conflict management. Cite it as QAA (2022), Policing Subject Benchmark Statement, para 4.3, item 15, and set it beside 1.12 and 4.4.b2. Do not present it as a regulatory rule or as the level most graduates reach, since most exceed it; for the classes above it point to Annex D (qaa/fheq-2024/annex-d)."
  author-agent-dialogue: "Raise it when a student prepares for or debriefs a confrontation. With a student, say in plain second-person words what it asks of them; with staff, frame it as the least every honours graduate must be able to show. Ask: \"What did you do to calm that situation, and what would you change?\" Do not read the issuer's list aloud or imply that this minimum is what most students reach."
- statement: qaa/policing-in-partnership-with-2022/4.3.b16
  forPractitioner: { text: "At threshold, graduates apply an in-depth understanding of leadership, team working and partnership working.", rewrite: light, force: threshold, status: drafted }
  forBeneficiary: { text: "At the threshold, you can use a deep understanding of leadership, teamwork and working with partner agencies.", rewrite: full, force: threshold, status: drafted }
  author-agent-written: "Describe this as a threshold standard for the honours degree in Policing (FHEQ level 6, FQHEIS level 10): the minimum a graduate has shown, here leadership, teams and partnership working. Cite it as QAA (2022), Policing Subject Benchmark Statement, para 4.3, item 16, and set it beside 2.3 and 4.4.b4. Do not present it as a regulatory rule or as the level most graduates reach, since most exceed it; for the classes above it point to Annex D (qaa/fheq-2024/annex-d)."
  author-agent-dialogue: "Raise it when a student leads a group task or works with another agency. With a student, say in plain second-person words what it asks of them; with staff, frame it as the least every honours graduate must be able to show. Ask: \"What kind of leadership did that task need, and did you provide it?\" Do not read the issuer's list aloud or imply that this minimum is what most students reach."
- statement: qaa/policing-in-partnership-with-2022/4.3.b17
  forPractitioner: { text: "At threshold, graduates understand and apply techniques that keep themselves and others well and resilient in all situations.", rewrite: light, force: threshold, status: drafted }
  forBeneficiary: { text: "At the threshold, you understand and use techniques to look after your own and others' wellbeing and resilience in any situation.", rewrite: full, force: threshold, status: drafted }
  author-agent-written: "Describe this as a threshold standard for the honours degree in Policing (FHEQ level 6, FQHEIS level 10): the minimum a graduate has shown, here wellbeing and resilience of self and others. Cite it as QAA (2022), Policing Subject Benchmark Statement, para 4.3, item 17, and set it beside 2.2.b6. Do not present it as a regulatory rule or as the level most graduates reach, since most exceed it; for the classes above it point to Annex D (qaa/fheq-2024/annex-d)."
  author-agent-dialogue: "Raise it when a student is under strain or supports a struggling peer. With a student, say in plain second-person words what it asks of them; with staff, frame it as the least every honours graduate must be able to show. Ask: \"What do you do to look after yourself and others after a hard day?\" Do not read the issuer's list aloud or imply that this minimum is what most students reach."
- statement: qaa/policing-in-partnership-with-2022/4.3.b18
  forPractitioner: { text: "At threshold, graduates engage actively in continual self-reflection and develop strategies to improve their practice.", rewrite: light, force: threshold, status: drafted }
  forBeneficiary: { text: "At the threshold, you reflect on your own work actively and continually and find ways to improve it.", rewrite: full, force: threshold, status: drafted }
  author-agent-written: "Describe this as a threshold standard for the honours degree in Policing (FHEQ level 6, FQHEIS level 10): the minimum a graduate has shown, here continual self-reflection to improve practice. Cite it as QAA (2022), Policing Subject Benchmark Statement, para 4.3, item 18, and set it beside 4.4.b10 and qaa/fheq-2024/annex-d/transferable/r5/3rd. Do not present it as a regulatory rule or as the level most graduates reach, since most exceed it; for the classes above it point to Annex D (qaa/fheq-2024/annex-d)."
  author-agent-dialogue: "Raise it when a student writes a reflective account or debriefs a placement. With a student, say in plain second-person words what it asks of them; with staff, frame it as the least every honours graduate must be able to show. Ask: \"What will you do differently next time, and why?\" Do not read the issuer's list aloud or imply that this minimum is what most students reach."
- statement: qaa/policing-in-partnership-with-2022/4.4.b1
  forPractitioner: { text: "At threshold, graduates accurately deploy established techniques to design research and to gather, analyse and interpret its data.", rewrite: light, force: threshold, status: drafted }
  forBeneficiary: { text: "At the threshold, you can use established research techniques accurately to design a study and to gather, analyse and interpret data.", rewrite: full, force: threshold, status: drafted }
  author-agent-written: "Describe this as a threshold standard for the honours degree in Policing (FHEQ level 6, FQHEIS level 10): the minimum a graduate has shown, here research design, collection, analysis and interpretation. Cite it as QAA (2022), Policing Subject Benchmark Statement, para 4.4, item 1, and set it beside qaa/fheq-2024/4.15.b2 (qaa/fqheis-2024/4.16.b4) and 2.14. Do not present it as a regulatory rule or as the level most graduates reach, since most exceed it; for the classes above it point to Annex D (qaa/fheq-2024/annex-d)."
  author-agent-dialogue: "Raise it when a student plans research methods or analyses data. With a student, say in plain second-person words what it asks of them; with staff, frame it as the least every honours graduate must be able to show. Ask: \"Why is that method the right one for your question?\" Do not read the issuer's list aloud or imply that this minimum is what most students reach."
- statement: qaa/policing-in-partnership-with-2022/4.4.b2
  forPractitioner: { text: "At threshold, graduates organise and communicate interconnected information to specialist and lay audiences.", rewrite: light, force: threshold, status: drafted }
  forBeneficiary: { text: "At the threshold, you can organise connected information and explain it to experts and to people outside policing.", rewrite: full, force: threshold, status: drafted }
  author-agent-written: "Describe this as a threshold standard for the honours degree in Policing (FHEQ level 6, FQHEIS level 10): the minimum a graduate has shown, here communicating to specialist and lay audiences. Cite it as QAA (2022), Policing Subject Benchmark Statement, para 4.4, item 2, and set it beside qaa/fheq-2024/4.15.b8 (qaa/fqheis-2024/4.16.b7) and 1.12. Do not present it as a regulatory rule or as the level most graduates reach, since most exceed it; for the classes above it point to Annex D (qaa/fheq-2024/annex-d)."
  author-agent-dialogue: "Raise it when a student prepares a briefing, report or presentation. With a student, say in plain second-person words what it asks of them; with staff, frame it as the least every honours graduate must be able to show. Ask: \"How would you change this briefing for a community meeting rather than a senior officer?\" Do not read the issuer's list aloud or imply that this minimum is what most students reach."
- statement: qaa/policing-in-partnership-with-2022/4.4.b3
  forPractitioner: { text: "At threshold, graduates critically evaluate arguments, assumptions and abstract concepts to find possible solutions.", rewrite: light, force: threshold, status: drafted }
  forBeneficiary: { text: "At the threshold, you can critically judge arguments, assumptions and abstract ideas to find possible solutions.", rewrite: full, force: threshold, status: drafted }
  author-agent-written: "Describe this as a threshold standard for the honours degree in Policing (FHEQ level 6, FQHEIS level 10): the minimum a graduate has shown, here critical evaluation to find solutions. Cite it as QAA (2022), Policing Subject Benchmark Statement, para 4.4, item 3, and set it beside qaa/fheq-2024/4.15.b7 and 4.3.b12. Do not present it as a regulatory rule or as the level most graduates reach, since most exceed it; for the classes above it point to Annex D (qaa/fheq-2024/annex-d)."
  author-agent-dialogue: "Raise it when a student weighs competing arguments. With a student, say in plain second-person words what it asks of them; with staff, frame it as the least every honours graduate must be able to show. Ask: \"What assumption sits beneath that argument, and does it hold?\" Do not read the issuer's list aloud or imply that this minimum is what most students reach."
- statement: qaa/policing-in-partnership-with-2022/4.4.b4
  forPractitioner: { text: "At threshold, graduates act autonomously and take responsibility for individual or group tasks in complex settings.", rewrite: light, force: threshold, status: drafted }
  forBeneficiary: { text: "At the threshold, you can work on your own initiative and take responsibility for your own and group tasks in complex settings.", rewrite: full, force: threshold, status: drafted }
  author-agent-written: "Describe this as a threshold standard for the honours degree in Policing (FHEQ level 6, FQHEIS level 10): the minimum a graduate has shown, here autonomy and responsibility in complex contexts. Cite it as QAA (2022), Policing Subject Benchmark Statement, para 4.4, item 4, and set it beside qaa/fheq-2024/4.15.b9.1 and 4.15.b9.2, and spine:6. Do not present it as a regulatory rule or as the level most graduates reach, since most exceed it; for the classes above it point to Annex D (qaa/fheq-2024/annex-d)."
  author-agent-dialogue: "Raise it when a student manages a group project or independent task. With a student, say in plain second-person words what it asks of them; with staff, frame it as the least every honours graduate must be able to show. Ask: \"What did you take responsibility for in that task, without being told?\" Do not read the issuer's list aloud or imply that this minimum is what most students reach."
- statement: qaa/policing-in-partnership-with-2022/4.4.b5
  forPractitioner: { text: "At threshold, graduates appreciate the live political, economic, social, technological, environmental, legal and ethical debates that shape policing as a discipline.", rewrite: light, force: threshold, status: drafted }
  forBeneficiary: { text: "At the threshold, you understand today's debates that affect policing, whether political, economic, social, technological, environmental, legal or ethical.", rewrite: full, force: threshold, status: drafted }
  author-agent-written: "Describe this as a threshold standard for the honours degree in Policing (FHEQ level 6, FQHEIS level 10): the minimum a graduate has shown, here political, economic, social, technological, environmental, legal and ethical debates. Cite it as QAA (2022), Policing Subject Benchmark Statement, para 4.4, item 5, and set it beside 3.1 and qaa/fheq-2024/4.15.b4. Do not present it as a regulatory rule or as the level most graduates reach, since most exceed it; for the classes above it point to Annex D (qaa/fheq-2024/annex-d)."
  author-agent-dialogue: "Raise it when a student discusses current affairs or policy change. With a student, say in plain second-person words what it asks of them; with staff, frame it as the least every honours graduate must be able to show. Ask: \"Which current debate do you think will most change policing in five years?\" Do not read the issuer's list aloud or imply that this minimum is what most students reach."
- statement: qaa/policing-in-partnership-with-2022/4.4.b6
  forPractitioner: { text: "At threshold, graduates understand contemporary debates on equality, diversity, inclusion and sustainability.", rewrite: light, force: threshold, status: drafted }
  forBeneficiary: { text: "At the threshold, you understand current debates about equality, diversity, inclusion and sustainability.", rewrite: full, force: threshold, status: drafted }
  author-agent-written: "Describe this as a threshold standard for the honours degree in Policing (FHEQ level 6, FQHEIS level 10): the minimum a graduate has shown, here debates on EDI and sustainability. Cite it as QAA (2022), Policing Subject Benchmark Statement, para 4.4, item 6, and set it beside 4.3.b8, 1.26 and the themes in SB2. Do not present it as a regulatory rule or as the level most graduates reach, since most exceed it; for the classes above it point to Annex D (qaa/fheq-2024/annex-d)."
  author-agent-dialogue: "Raise it when a student meets a debate about fairness or sustainability in policing. With a student, say in plain second-person words what it asks of them; with staff, frame it as the least every honours graduate must be able to show. Ask: \"What are the strongest arguments on each side of that debate?\" Do not read the issuer's list aloud or imply that this minimum is what most students reach."
- statement: qaa/policing-in-partnership-with-2022/4.4.b7
  forPractitioner: { text: "At threshold, graduates understand the effect of culture on working practices.", rewrite: light, force: threshold, status: drafted }
  forBeneficiary: { text: "At the threshold, you understand how culture shapes the way people work.", rewrite: full, force: threshold, status: drafted }
  author-agent-written: "Describe this as a threshold standard for the honours degree in Policing (FHEQ level 6, FQHEIS level 10): the minimum a graduate has shown, here culture and working practices. Cite it as QAA (2022), Policing Subject Benchmark Statement, para 4.4, item 7, and set it beside 2.5 and 2.7. Do not present it as a regulatory rule or as the level most graduates reach, since most exceed it; for the classes above it point to Annex D (qaa/fheq-2024/annex-d)."
  author-agent-dialogue: "Raise it when a student reflects on workplace culture on placement. With a student, say in plain second-person words what it asks of them; with staff, frame it as the least every honours graduate must be able to show. Ask: \"How did the culture of the team you worked with shape what people did?\" Do not read the issuer's list aloud or imply that this minimum is what most students reach."
- statement: qaa/policing-in-partnership-with-2022/4.4.b8
  forPractitioner: { text: "At threshold, graduates apply a range of innovative methods and techniques they have learned to employment.", rewrite: light, force: threshold, status: drafted }
  forBeneficiary: { text: "At the threshold, you can use a range of new methods and techniques you have learned in your work.", rewrite: full, force: threshold, status: drafted }
  author-agent-written: "Describe this as a threshold standard for the honours degree in Policing (FHEQ level 6, FQHEIS level 10): the minimum a graduate has shown, here innovative methods in employment. Cite it as QAA (2022), Policing Subject Benchmark Statement, para 4.4, item 8, and set it beside qaa/fheq-2024/4.15.b6 and 4.15.b9.3. Do not present it as a regulatory rule or as the level most graduates reach, since most exceed it; for the classes above it point to Annex D (qaa/fheq-2024/annex-d)."
  author-agent-dialogue: "Raise it when a student links coursework to a job or placement. With a student, say in plain second-person words what it asks of them; with staff, frame it as the least every honours graduate must be able to show. Ask: \"Which method from your course have you used at work, and how did it go?\" Do not read the issuer's list aloud or imply that this minimum is what most students reach."
- statement: qaa/policing-in-partnership-with-2022/4.4.b9
  forPractitioner: { text: "At threshold, graduates choose and use a range of digital skills and techniques at work.", rewrite: light, force: threshold, status: drafted }
  forBeneficiary: { text: "At the threshold, you can choose and use a range of digital skills and tools at work.", rewrite: full, force: threshold, status: drafted }
  author-agent-written: "Describe this as a threshold standard for the honours degree in Policing (FHEQ level 6, FQHEIS level 10): the minimum a graduate has shown, here digital skills at work. Cite it as QAA (2022), Policing Subject Benchmark Statement, para 4.4, item 9, and set it beside 4.3.b6 and qaa/fheq-2024/annex-d/transferable/r1/3rd. Do not present it as a regulatory rule or as the level most graduates reach, since most exceed it; for the classes above it point to Annex D (qaa/fheq-2024/annex-d)."
  author-agent-dialogue: "Raise it when a student uses digital systems on placement or in study. With a student, say in plain second-person words what it asks of them; with staff, frame it as the least every honours graduate must be able to show. Ask: \"Which digital tool do you rely on, and which would you like to learn?\" Do not read the issuer's list aloud or imply that this minimum is what most students reach."
- statement: qaa/policing-in-partnership-with-2022/4.4.b10
  forPractitioner: { text: "At threshold, graduates engage actively in self-reflection to identify and address their own learning needs.", rewrite: light, force: threshold, status: drafted }
  forBeneficiary: { text: "At the threshold, you reflect actively on yourself to spot and meet your own learning needs.", rewrite: full, force: threshold, status: drafted }
  author-agent-written: "Describe this as a threshold standard for the honours degree in Policing (FHEQ level 6, FQHEIS level 10): the minimum a graduate has shown, here self-reflection on learning needs. Cite it as QAA (2022), Policing Subject Benchmark Statement, para 4.4, item 10, and set it beside 4.3.b18 and qaa/fheq-2024/4.15.b5. Do not present it as a regulatory rule or as the level most graduates reach, since most exceed it; for the classes above it point to Annex D (qaa/fheq-2024/annex-d)."
  author-agent-dialogue: "Raise it when a student plans their personal development. With a student, say in plain second-person words what it asks of them; with staff, frame it as the least every honours graduate must be able to show. Ask: \"What is the one thing you most need to learn next, and how will you learn it?\" Do not read the issuer's list aloud or imply that this minimum is what most students reach."
- statement: qaa/policing-in-partnership-with-2022/4.4.b11
  forPractitioner: { text: "At threshold, graduates understand the importance of engaging in continuing professional development.", rewrite: light, force: threshold, status: drafted }
  forBeneficiary: { text: "At the threshold, you understand why it matters to keep developing professionally throughout your career.", rewrite: full, force: threshold, status: drafted }
  author-agent-written: "Describe this as a threshold standard for the honours degree in Policing (FHEQ level 6, FQHEIS level 10): the minimum a graduate has shown, here continuing professional development. Cite it as QAA (2022), Policing Subject Benchmark Statement, para 4.4, item 11, and set it beside qaa/fheq-2024/4.15.b9.3 and 1.29. Do not present it as a regulatory rule or as the level most graduates reach, since most exceed it; for the classes above it point to Annex D (qaa/fheq-2024/annex-d)."
  author-agent-dialogue: "Raise it when a student asks about life after graduation. With a student, say in plain second-person words what it asks of them; with staff, frame it as the least every honours graduate must be able to show. Ask: \"How will you keep your knowledge current after you graduate?\" Do not read the issuer's list aloud or imply that this minimum is what most students reach."
```

### S5 Levels and alignment
<!-- label: both; status: drafted; basis: primary -->
```yaml
levels:
  - { id: "fheq:6", role: "cites", locator: "D1, 1.4; 1.13; 1.24; 1.27; 2.10; 4.2" }
  - { id: "fqheis:10", role: "cites", locator: "D1, 1.4; 1.13; 1.24; 1.27; 2.10; 4.2" }
crosswalks:
  - { from: "fheq:6", to: "fqheis:10", relation: "equivalent", basis: "stated (D1, 1.13: constable capabilities align to Level 6 (FHEQ) and Level 10 (FQHEIS); 2.10: a degree with honours at both)" }
```

### S6 Themes
<!-- label: both; status: drafted; basis: primary -->
```yaml
- { id: "theme:edi", role: "carries", carriedIn: ["front matter", "1.16", "1.17", "1.18", "1.19", "2.2", "2.3", "3.2", "3.3", "3.14", "3.15", "4.3", "4.4"] }
- { id: "theme:accessibility", role: "carries", carriedIn: ["1.19", "1.20", "1.21", "1.22", "1.23"] }
- { id: "theme:esd", role: "carries", carriedIn: ["front matter", "1.24", "1.25", "1.26", "4.4"] }
- { id: "theme:enterprise", role: "carries", carriedIn: ["front matter", "1.26", "2.6", "2.16", "3.14"] }
```

### S7 Relations
<!-- label: both; status: drafted; basis: primary -->
```yaml
- { rel: "partOf", target: "collection: QAA Subject Benchmark Statements", note: "one of 54 held by stan" }
- { rel: "refersTo", target: "std:doc:qaa-fheq-2024-framework, Annex D", note: "the outcome classification descriptions for FHEQ level 6 and FQHEIS level 10 degrees (4.2)" }
- { rel: "refersTo", target: "std:doc:qaa-fheq-2024-framework", note: "Level 6 (1.4, 1.13, 1.24, 1.27, 2.10)" }
- { rel: "refersTo", target: "std:doc:qaa-fqheis-2024-framework", note: "Level 10 (1.4, 1.13, 1.24, 1.27, 2.10)" }
- { rel: "refersTo", target: "College of Policing: PEQF and the National Policing Curriculum (not yet ingested; Part E)", note: "1.4, 2.4, 3.11" }
- { rel: "refersTo", target: "QAA Quality Code, Advice and Guidance: Work-based Learning (2018) (not yet ingested)", note: "front matter; 2.8; 2.16" }
- { rel: "overlaps", target: "std:doc:qaa-criminology-2022-benchmarks", note: "inferred, not cited: shared ground in criminology and criminal justice (2.2.b8, 4.3.b1)" }
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
- Policing education serves a profession whose stated mission is safer communities through fair and firm law enforcement, crime prevention, keeping the peace, protection and bringing offenders to justice (D1, 1.1).
- It is professional education, shaped by a national drive to recognise policing as a profession, with the College of Policing setting standards in England and Wales (D1, 1.2, 1.3).
- Its routes differ by nation: three licensed PEQF entry routes in England and Wales, no higher education entry route in Scotland, and a PSNI degree in Northern Ireland; unlicensed degrees still have value (D1, 1.4 to 1.8).
- Theory underpins applied practice: critical thinking, analysis and reflective learning through a curriculum that integrates theory and practice (D1, 1.9, 1.11).
- Ethics and the Code of Ethics, the Peelian Principles and the Competency Values Framework are foundations of the learning (D1, 1.14, 1.18).
- Evidence-based policing, problem-solving and research by practitioner-researchers are central (D1, 1.15, 2.2, 2.9).
- Employers and the professional body are closely involved, sometimes co-creating the degree with a police force (D1, 2.5 to 2.8, 3.14).
- Teaching has moved from teacher-centred to learner-centred, experiential and co-produced learning (D1, 3.4 to 3.10).

### SB2 Themes in this subject
<!-- label: both; status: drafted; basis: primary -->
```yaml
- theme: theme:edi
  inThisSubject: "EDI is set at the core of the curriculum with ethics as a common thread; all students and stakeholders are to be treated fairly under the Public Sector Equality Duty, and students are to promote EDI and human rights in practice (D1, 1.16 to 1.19, 2.2, 3.2, 4.3)"
  statements: ["qaa/policing-in-partnership-with-2022/1.16", "qaa/policing-in-partnership-with-2022/1.17", "qaa/policing-in-partnership-with-2022/1.18", "qaa/policing-in-partnership-with-2022/1.19", "qaa/policing-in-partnership-with-2022/2.2.b5", "qaa/policing-in-partnership-with-2022/3.2.b5", "qaa/policing-in-partnership-with-2022/3.14.b9", "qaa/policing-in-partnership-with-2022/4.3.b8", "qaa/policing-in-partnership-with-2022/4.4.b6"]
- theme: theme:accessibility
  inThisSubject: "widening access across physical and digital barriers, varied entry routes and flexible delivery, the 2018 accessibility regulations, and online provision suited to students with shift work, caring duties or a second language (D1, 1.19 to 1.23)"
  statements: ["qaa/policing-in-partnership-with-2022/1.19", "qaa/policing-in-partnership-with-2022/1.20", "qaa/policing-in-partnership-with-2022/1.22", "qaa/policing-in-partnership-with-2022/1.23.b1", "qaa/policing-in-partnership-with-2022/1.23.b2", "qaa/policing-in-partnership-with-2022/1.23.b3", "qaa/policing-in-partnership-with-2022/1.23.b4"]
- theme: theme:esd
  inThisSubject: "headed Sustainability, beside horizon scanning: programmes designed with the SDGs, with eight themes named for the Policing curriculum, including the environmental impact of policing and access to justice (D1, 1.24 to 1.26)"
  statements: ["qaa/policing-in-partnership-with-2022/1.26", "qaa/policing-in-partnership-with-2022/4.4.b6"]
- theme: theme:enterprise
  inThisSubject: "named as employability in the front matter: assessment co-designed with employers to enhance employability, the value of work-based learning, and job market skills among the SDG themes (D1, front matter, 1.26, 2.16, 3.14)"
  statements: ["qaa/policing-in-partnership-with-2022/2.16", "qaa/policing-in-partnership-with-2022/3.14"]
```

### SB3 Content and delivery
<!-- label: both; status: drafted; basis: primary -->
```yaml
areas:
  - { component: "3.1", gloss: "a changing subject responding to political, economic, social, technological, environmental and ethical change" }
  - { component: "3.2", gloss: "five core themes: impartiality, integrity, public service, transparency, diversity" }
  - { component: "3.3", gloss: "sixteen indicative topics, from operational policing and investigation to cyber crime, intelligence and public protection" }
practices:
  - { component: "2.13", kind: "teaching", gloss: "varied methods; classroom, work-based and field-based learning; independent learning" }
  - { component: "2.14", kind: "learning", gloss: "final-year independent problem-based project or dissertation" }
  - { component: "3.4", kind: "teaching", gloss: "a shift to learner-centred police education" }
  - { component: "3.5", kind: "learning", gloss: "student-centred and experiential learning cycles" }
  - { component: "3.6", kind: "teaching", gloss: "the Student as Producer model and collaborative teaching" }
  - { component: "3.13", kind: "assessment", gloss: "applied assessment blending theory and practice" }
  - { component: "3.15", kind: "assessment", gloss: "varied, innovative and inclusive forms with student voice" }
  - { component: "3.16", kind: "assessment", gloss: "full information, balanced diagnostic, formative and summative methods, applied forms" }
```

### SB4 Benchmark standards
<!-- label: both; status: drafted; basis: primary -->
```yaml
rungs:
  - { rung: "threshold", leadIn: "4.3 and 4.4 (heading: Threshold level)", award: "bachelor's with honours", items: 29 }
rungBases: "4.1 defines the threshold as the minimum an honours graduate will have shown; 4.2 says most students perform well above it and sends the classes above it to Annex D. No typical or excellent rung is stated."
outcomeLists:
  - { leadIn: "2.2", gloss: "what programmes will enable graduates to do", items: 13, award: ["honours"] }
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
- { body: "College of Policing", says: "the professional body for policing in England and Wales, an arm's-length body of the Home Office; partner in writing and reviewing the statement; sets the PEQF, licenses programmes that follow the National Policing Curriculum and reviews them; its Code of Ethics underpins the learning (D1, front matter, 1.3 to 1.5, 1.14, 2.4, 2.13, 3.11)", requirements: "not yet ingested (Part E)" }
- { body: "Police Scotland and the Scottish Police College", says: "trains recruits in-house at Tulliallan; works with universities and offers credit-rated awards on the SCQF; helps design some criminology-focused degrees (D1, 1.6, 1.7)", requirements: "not-applicable-by-design (Part E)" }
- { body: "Scottish Institute for Policing Research", says: "works with Police Scotland and universities on research and knowledge exchange (D1, 1.6)", requirements: "not-applicable-by-design (Part E)" }
- { body: "Police Service of Northern Ireland", says: "has its own degree-level qualification for all new entrants, a BSc (Hons) and a graduate certificate (D1, 1.8)", requirements: "not yet ingested (Part E)" }
- { body: "Jisc", says: "issues sector guidance on accessible websites and apps (D1, 1.23)", requirements: "not-applicable-by-design (Part E)" }
- { body: "Office for Students", says: "in England the statement is not a sector-recognised standard under its regulatory framework (D1, front matter)", requirements: "not-applicable-by-design (Part E)" }
- { body: "Association of Police and Crime Commissioners and National Police Chiefs' Council", says: "source of the stated mission of policing (D1, 1.1)", requirements: "not-applicable-by-design (Part E)" }
```

### SB6 Cross-cutting references
<!-- label: both; status: drafted; basis: primary -->
```yaml
themes:
  - { id: "theme:edi", named: "Equality, diversity and inclusion", carriedIn: ["front matter", "1.16", "1.17", "1.18", "1.19", "2.2", "2.3", "3.2", "3.3", "3.14", "3.15", "4.3", "4.4"], statements: ["1.16", "1.17", "1.18", "1.19", "2.2.b5", "3.2.b5", "3.14.b9", "4.3.b8", "4.4.b6"] }
  - { id: "theme:accessibility", named: "Accessibility", carriedIn: ["1.19", "1.20", "1.21", "1.22", "1.23"], statements: ["1.19", "1.20", "1.22", "1.23.b1", "1.23.b2", "1.23.b3", "1.23.b4"] }
  - { id: "theme:esd", named: "Sustainability (front matter: education for sustainable development)", carriedIn: ["front matter", "1.24", "1.25", "1.26", "4.4"], statements: ["1.26", "4.4.b6"] }
  - { id: "theme:enterprise", named: "employability (front matter; no enterprise heading in the body)", carriedIn: ["front matter", "1.26", "2.6", "2.16", "3.14"], statements: ["2.16", "3.14"] }
frameworks:
  - { framework: "fheq", levels: ["fheq:6"], citedIn: ["1.4", "1.13", "1.24", "1.27", "2.10", "4.2"] }
  - { framework: "scqf", levels: ["fqheis:10"], citedIn: ["1.4", "1.6", "1.13", "1.24", "1.27", "2.10", "4.2"] }
  - { framework: "other: Policing Education Qualifications Framework (PEQF)", levels: [], citedIn: ["1.4", "1.6", "1.8", "2.6", "3.11"] }
  - { framework: "other: Competency Values Framework (CVF)", levels: [], citedIn: ["1.14"] }
  - { framework: "other: the relevant national qualification framework, unnamed", levels: [], citedIn: ["2.17"] }
bodies:
  - { body: "College of Policing", citedIn: ["front matter", "1.3", "1.4", "1.5", "1.14", "1.17", "1.28", "2.4", "2.13", "3.11"] }
  - { body: "Police Scotland and the Scottish Police College", citedIn: ["1.6", "1.7"] }
  - { body: "Scottish Institute for Policing Research", citedIn: ["1.6"] }
  - { body: "Police Service of Northern Ireland", citedIn: ["1.8"] }
  - { body: "Home Office", citedIn: ["1.3"] }
  - { body: "Jisc", citedIn: ["1.23"] }
  - { body: "Office for Students", citedIn: ["front matter"] }
  - { body: "PSRBs, unnamed", citedIn: ["front matter", "2.23"] }
sharedDocuments:
  - { document: "std:doc:qaa-fheq-2024-framework, Annex D", named: "Annex D: Outcome classification descriptions for FHEQ Level 6 and FQHEIS Level 10 degrees", citedIn: ["4.2"], role: "descriptions of the four honours classes, for achievement above the threshold" }
  - { document: "QAA Quality Code, Advice and Guidance (not yet ingested)", named: "Advice and Guidance to support the UK Quality Code; Work-based Learning (QAA, 2018)", citedIn: ["front matter", "2.8", "2.16"], role: "course design, work-based learning and professional codes" }
  - { document: "QAA Glossary (not ingested)", named: "QAA's Glossary", citedIn: ["front matter"], role: "explains unfamiliar terms" }
  - { document: "College of Policing National Policing Curriculum (not yet ingested)", named: "National Policing Curriculum (NPC)", citedIn: ["1.4", "2.4", "3.11"], role: "curriculum for licensed programmes" }
  - { document: "College of Policing Code of Ethics (not ingested)", named: "College of Policing Code of Ethics", citedIn: ["1.14"], role: "principles of professional behaviour" }
  - { document: "Equality Act 2010 (law)", named: "Equality Act 2010; Public Sector Equality Duty", citedIn: ["1.17"], role: "equality duties" }
  - { document: "Northern Ireland Act 1998 (law)", named: "Section 75 of the Northern Ireland Act 1998", citedIn: ["1.17"], role: "equality duties in Northern Ireland" }
  - { document: "Public Sector Bodies (Websites and Mobile Applications) (No. 2) Accessibility Regulations 2018 (law)", named: "the Accessibility Regulations 2018", citedIn: ["1.23"], role: "accessible websites and apps" }
  - { document: "UN Sustainable Development Goals (external)", named: "United Nations 17 sustainable development goals", citedIn: ["1.26"], role: "frame of the sustainability theme" }
  - { document: "quality frameworks of the nations (not ingested)", named: "Office for Students' regulatory framework; Quality Assessment Framework for Wales; Quality Enhancement Framework (Scotland)", citedIn: ["front matter"], role: "the regulatory status of the statement in each nation" }
```

## Part B Terminology
<!-- The statement has no glossary of its own unless Part E says so; these are terms it defines in its text. -->

### B1 Concepts
<!-- label: both; status: drafted; basis: primary -->
```yaml
- { slug: "partnership-arrangement", definition: "an arrangement between two or more organisations to deliver parts of teaching, learning, assessment and student support (D1, 2.15)", beneficiaryDefinition: "when another organisation, such as a police force, delivers part of your course with the university", scopeNote: "governed by 2.16 to 2.19", category: "unknown", practices: ["education"] }
- { slug: "education-for-sustainable-development", definition: "building curriculum and content that equip learners to take informed, responsible decisions for the environment, the economy and a just society (D1, 1.25)", beneficiaryDefinition: "learning that helps you make responsible choices for people and the planet", scopeNote: "the ESD theme", category: "unknown", practices: ["education"] }
- { slug: "peqf", definition: "the College of Policing's framework for a standardised approach to the initial education of constables in England and Wales, with three entry routes (D1, 1.4)", beneficiaryDefinition: "the framework that sets the routes to becoming a police constable in England and Wales", scopeNote: "not applicable in Scotland or Northern Ireland (1.6, 1.8)", category: "unknown", practices: ["education", "policing"] }
- { slug: "monitoring-and-evaluation", definition: "a periodic assessment of a course, internal or external, using current and past monitoring to understand achievement and plan the course (D1, 2.20)", scopeNote: "part of quality assurance", category: "unknown", practices: ["education"] }
- { slug: "threshold-standard", definition: "the minimum a student of Policing will have shown when awarded honours (D1, 4.1)", scopeNote: "the one rung the statement sets", category: "unknown", practices: ["education"] }
```

### B2a Terms as the issuer defines them
<!-- label: source; status: drafted; basis: primary -->
```yaml
- { concept: "partnership-arrangement", form: "partnership", lang: "en", partOfSpeech: "noun", termStatus: "preferred", register: "formal" }
- { concept: "education-for-sustainable-development", form: "Education for sustainable development", lang: "en", partOfSpeech: "noun-phrase", termStatus: "preferred", register: "formal" }
- { concept: "peqf", form: "Policing Education and Qualification Framework", lang: "en", partOfSpeech: "noun-phrase", termStatus: "preferred", register: "discipline-specific" }
- { concept: "peqf", form: "PEQF", lang: "en", partOfSpeech: "noun", termStatus: "admitted", register: "discipline-specific" }
- { concept: "monitoring-and-evaluation", form: "Monitoring and evaluation", lang: "en", partOfSpeech: "noun-phrase", termStatus: "preferred", register: "formal" }
- { concept: "threshold-standard", form: "minimum threshold standards", lang: "en", partOfSpeech: "noun-phrase", termStatus: "preferred", register: "formal" }
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
  title: "Subject Benchmark Statement Policing"
  edition: "March 2022"
  year: 2022
  url: unknown (the QAA page; the text came by stan's extraction)
  retrieved: "held from stan: wkspc2615-QAAVector mapped/policing-in-partnership-with-2022/policing-in-partnership-with-2022.raw.txt, commit 366bcb99a01118f2c4c3ebfa2a8337596bddc455; received 2026-10-03"
  licence: QAA copyright
  tier: primary
  readVia: direct
  held: 340494318f152c022e244569f1d83083235f46e9d3294fe3f534ede5e6ffe403
  heldFiles: ["wkspc2601-library/txt/qaa-2022-policing-partnership-subject-benchmark-statement-standard.txt", "wkspc2601-library/txt/qaa-2022-policing-partnership-subject-benchmark-statement-standard.norm.txt", "wkspc2601-library/records/qaa-2022-policing-partnership-subject-benchmark-statement-standard.chunks.json", "wkspc2601-library/records/qaa-2022-policing-partnership-subject-benchmark-statement-standard.held.json"]
  citedIn: [S1, S2, S3, S4, S4a, S5, S6, S7, SB1, SB2, SB3, SB4, SB5, SB6]
```

### D2 Research log
```yaml
- { ref: D1, tier: primary, consulted: 2026-10-03, pass: P1, outcome: "read whole, direct, from the normalised text; skeleton by tools/std_prep.py, document by tools/bm_build.py" }
- { ref: "ADAPT subj HESA stores, cah.json and hecos.json (designs/ingest/standards/subj/vocab)", tier: primary, consulted: 2026-10-03, pass: P1, outcome: "codes for statedSubjects and subjects" }
```

### D3 Wanted sources
```yaml
- { w: "W-std-0093", citation: "College of Policing, Policing Education Qualifications Framework and National Policing Curriculum (current editions)", settles: ["SB5", "S7"], asked: "2026-10-03", state: "wanted" }
- { w: "W-std-0052", citation: "QAA (2018) UK Quality Code for Higher Education, Advice and Guidance: Work-based Learning", settles: ["SB6", "S7"], asked: "2026-10-03", state: "wanted" }
```

## Part E Gaps and questions
- Title: the cover reads 'Subject Benchmark Statement Policing In partnership with' followed by the College of Policing's logo, lost in extraction; the slug's 'in-partnership-with' comes from that line. Title recorded as 'Subject Benchmark Statement Policing'.
- Edition: the back matter says 'First edition, Published 30 March 2022', yet the front matter lists 'Key changes from the previous Subject Benchmark Statement'. supersedes is left none-stated; for P3.
- Rungs (differs from Psychology): one rung only, threshold, as two lists under the heading 'Threshold level': 4.3 subject knowledge, understanding and skills (18 items) and 4.4 generic skills (11 items). No typical or excellent rung; 4.2 hands the classes above threshold to Annex D (the Archaeology shape). The skeleton counted no rungs: corrected to threshold 29.
- Rungs, force: both threshold lead-ins say 'students should be able to', while 4.1 defines the list as the minimum threshold standards; force recorded as threshold with forceFrom 4.1 (batch 1 convention). For P3: should these read 'should'?
- Outcome list (differs from Psychology): 2.2 'Programmes will therefore enable graduates to' gives 13 graduate outcomes in a programme-design lead-in; recorded as outcomes (rung none, force will).
- Section order (differs from Psychology): section 1 has subsections per nation (England and Wales, Scotland, Northern Ireland) and the themes; section 2 'Distinctive features' is mostly provider matter (design, employer involvement, progression, flexibility, partnership, monitoring); assessment strategy (3.14 to 3.17) carries many obliging items.
- S4, obliging words outside the five, not taken as statements, for Abbott: 1.13 'needs to develop'; 1.15 'it is therefore important' (1.15 taken for its 'will' and 'should'); 1.23 stem 'are expected to adhere'; 1.24 'need to develop'; 2.5 'It is essential that'; 2.7 'There is a necessity'; 2.8 'Students need to prepare' and 'It is therefore essential'; 2.10 'it is expected that'; 2.21 'an essential component'.
- S4, 'required': 2.14 'students are required to design, undertake and complete' read as must (batch 1 convention).
- S4, provider 'will' norms not taken as statements: 1.14 'will align', 2.1 'Programmes will be designed', 2.21 'providers will use external reviewers', 2.22 'external examiners will be asked'; predictive or design norms, not outcomes. For P3.
- S4, plain-present provider norms, not statements (template open point 5): 2.13 (programmes 'include a diverse range' of methods), 2.20 (awarding bodies 'routinely collect and analyse'), 3.12 ('may not require').
- S4, list items: 1.23's four items ('students who should be able to' access, keep pace, review and reflect) read as accessible provision, addressee provider, student version not applicable. 1.26's eight SDG items are topics for the curriculum, not statements: the stem is the statement, cut by find. 3.3's sixteen indicative topics ('may include') are an S3 area, not statements.
- S4, 3.14: the stem's own two 'must' sentences are one statement (cut by find, without the 'should incorporate' lead-in); its ten items are statements, b1 to b8 'should', b9 and b10 'must'.
- S4, 3.15: 'students must have opportunities to co-create' is Matthews' (2016) argument as cited, not the issuer's obligation; force recorded should.
- S4, 3.11: force must from 'will require' and 'require' for licensed PEQF programmes; it also carries 'should map'. Licensed and unlicensed programmes differ (3.12).
- S4, 1.18: addressee both (EDI 'should' on the subject; 'must understand' ethics on students); force must.
- S4a: 41 of 89 statements are provider duties with no student version; their student-facing effect is in 4.3, 4.4 and 2.2.
- SB6, themes: the front matter names three cross-cutting themes, EDI, ESD and employability; employability is recorded under theme:enterprise (as in Psychology), though no enterprise heading appears. Accessibility is a body heading not named in the front matter. Horizon scanning (1.27 to 1.29) is beside sustainability but not a theme id; generative AI is not mentioned.
- SB6, frameworks: PEQF and the Competency Values Framework are professional frameworks with no levels; 2.17's 'relevant national qualification framework' names none. The SCQF is named in 1.6 with no level; FQHEIS Level 10 in six paragraphs.
- Levels: 2.12 names the Certificate and Diploma of Higher Education as exit awards (fheq:4, fheq:5) and 1.8 the PSNI Graduate Certificate; none is covered by the standards, so they are not in levelsCovered.
- Subjects: HECoS 100486 policing is stated; CAH16-01-01, CAH16-01 and CAH16 (law, the CAH home of policing in the HESA store), HECoS 100484 criminology and 100483 criminal justice are inferred, from 1.8, 2.14, 2.2.b8 and 4.3.b1; for P3 confirmation.
- SB5: the College of Policing's own requirements (PEQF, NPC, licensing) and the PSNI's are not yet ingested (D3). The other bodies set no requirements on courses: not-applicable-by-design.
- S7: overlap with the Criminology 2022 statement inferred, not cited.
- Pedagogy named for theory ingest, not ingested here: learner-centred and student-centred learning (3.4, 3.5), experiential learning (3.5), Student as Producer (Jameson et al, 2012; 3.6 to 3.10), students as partners (Matthews, 2016; 3.15), constructive alignment (3.15), inclusive learning and teaching (Thomas and May, 2010; Hockings, 2010; 1.21).
- Held text: extraction faults kept as held: 'hor izon' (contents), 'twenty-f irst' (1.1), 'inf luencing' (1.4), 'shif t' (3.4); 'Thorough the use' (1.19) is the issuer's typo.
- S1, licence: copyright notice only, no re-use terms; QAA's terms for holding and chunking are to check.
- S9: not researched in P1.
- ST-12: versions here run to the lengths the content needs; no length range is yet set.

---

## Change notes
- 0.1.2, 3 October 2026, 21:02: moved with its held text from UNI to the source library repo (`wkspc2601-library/ingested/standards/`, texts in `txt/`, records in `records/`); paths only (Abbott, 20:56; std N-0119).
- 0.1.1, 3 October 2026, 20:20: obliging words outside the five read as must, "ought to" as should, on statements outside the rungs, each marked on its force line (Abbott, 20:17; D-std-0016).
- 0.1.0, 2026-10-03 18:23: researched by run frame 0.1.1-draft and standards run layer 0.7.0-draft, std, run 0126 (P1); built by tools/bm_build.py.
