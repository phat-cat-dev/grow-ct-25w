---
id: std:doc:qaa-education-studies-2025-benchmarks
title: "Subject Benchmark Statement Education Studies"
profile: standards/subject-benchmark
profileVersion: 0.2.0-draft
issuer: QAA
kind: subject-benchmark
jurisdiction: [UK]
subjectScope: subjects
subjects:
  - { scheme: "hecos", code: "100459", label: "education studies", basis: "stated" }
  - { scheme: "cah", code: "CAH22-01-01", label: "education", basis: "stated" }
  - { scheme: "cah", code: "CAH22-01-02", label: "teacher training", basis: "inferred" }
  - { scheme: "hecos", code: "101246", label: "professional practice in education", basis: "inferred" }
edition: "April 2025 (fifth edition)"
published: 2025-04
status: current
supersedes: "the Education Studies statement of 2019 (a minor update of the 2015 edition; earlier editions 2007 and 2000; dates from the advisory group lists, back matter)"
heldText: { method: sha256-bytes, raw: cc48a3bcc38c112292ced85a22babe5ecd87418e2eddbb449bd03385a311a1c0, normalised: 8be97c2eb247c8debb4de4d4f3828f5e1f7de9db5c9b9cf72e45f6be55330e34 }
heldTextStan: { method: sha256-stan, raw: cc48a3bcc38c112292ced85a22babe5ecd87418e2eddbb449bd03385a311a1c0, normalised: 30bd6f3bf1d6c51c3a1fc5bfe6838457cc00dea67cf9e0c5b37bdc7a55e4838f }
licence: "QAA copyright; held for study, private to the project, never published"
series: "QAA Subject Benchmark Statements, fifth edition series with cross-cutting themes (published 10 April 2025)"
awardsCovered: ["bachelor's with honours", "master's", "integrated master's"]
levelsCovered: ["fheq:6", "fheq:7", "fqheis:10", "fqheis:11"]
nations: ["England", "Wales", "Scotland", "Northern Ireland"]
parts:
  S: full
  B: "partial: no glossary in the document (it points to QAA's Glossary); terms it defines in passing"
  C: "not-applicable: the document sets expectations, not a procedure"
pins: { structure: 0.13.0-draft, template: 0.8.0-draft, benchmarkTemplate: 0.6.0-draft, runFrame: 0.1.1-draft, runLayer: 0.7.0-draft, standards: none yet, terminology: none yet }
lifecycle: drafted
researchedBy: run frame 0.1.1-draft; standards run layer 0.7.0-draft; std, run 0103 (tools/bm_build.py)
passes:
  P1: "2026-10-03 17:11"
  P2: "skipped: read direct from the held text; inferred codes and rung links are for P3"
  P3: open
version: 0.1.2
---

<!-- from INGEST wpk-0016-ingest-pd-template-standards.md 0.8.0-draft and wpk-0016-ingest-pd-template-standards-benchmark.md 0.6.0-draft; built by tools/bm_build.py from run-src/ -->
# Subject Benchmark Statement: Education Studies (QAA, April 2025)

> Run 0103, P1 by std. The issuer's words are held in the source library, `wkspc2601-library/txt/qaa-2025-education-studies-subject-benchmark-statement-standard.norm.txt`; each S4 record carries its statement in full (`source`) for language analysis, with its span. Paraphrases and versions are ours. Private to the project, never published. In front matter `status` is the issuer's; ours is `lifecycle`. Doubts are in Part E.

## Part 0 Summary

### 0.1 Agent definition
<!-- label: editorial; status: drafted; basis: primary -->
QAA's UK reference point for what an Education Studies graduate should know, understand and be able to do, at honours and at master's level. Reach for it when designing, approving, reviewing or describing an Education Studies course, its outcomes or its assessment. Its standards are one table of twenty rows in three groups (subject-specific, practical and practice-based, transversal), each row at four columns: threshold, typical and excellent for honours, and a postgraduate master's column the statement asks institutions to treat as a guide. It is not a regulatory requirement, not a teacher training standard and not a mark scheme.

### 0.2 Summary
<!-- label: both; status: drafted; basis: primary -->
Published by QAA on 10 April 2025, the statement covers Education Studies as a subject, field or discipline concerned with how people learn across life, the nature of knowledge and the contexts of education, at honours and master's level. It sets five cross-cutting themes (equity, diversity and inclusion; accessibility and the needs of disabled students; education for sustainable development; employability, entrepreneurship and enterprise education; artificial intelligence), distinctive features of progression, flexibility, partnership and review, three curricula (subject-specific, practice-based and transversal) and its standards as one table at threshold, typical, excellent and master's, with a pass-or-not row for professional competence on PSRB-accredited routes. It names PSRBs, the Office for Students and the Equality and Human Rights Commission, and points to Annex D of the FHEQ.

## Part S Standard

### S1 Identity
<!-- label: source; status: drafted; basis: primary -->
```yaml
issuer: The Quality Assurance Agency for Higher Education
title: "Subject Benchmark Statement Education Studies"
edition: "April 2025 (fifth edition)"
dates:
  published: 2025-04
  other: []
kind: subject-benchmark
jurisdiction: [UK]
authority: "reference: a sector reference point, not a regulatory requirement (D1, front matter); in England not a sector-recognised standard under the OfS framework; part of quality arrangements in Scotland, Wales and Northern Ireland (D1, Relationship to legislation)"
licence: "QAA copyright; the document gives no re-use terms in its text (D1, front matter)"
copyrightNotice: { text: "© The Quality Assurance Agency for Higher Education 2025", locator: "D1, index" }
```

### S2 Purpose and scope
<!-- label: source; status: drafted; basis: primary -->
```yaml
governs: "what can be expected of a graduate in Education Studies at honours and master's level, and the nature of awards in the subject (D1, front matter; 4.1)"
appliesTo:
  awards: ["bachelor's degrees with honours, including joint and combined degrees and professionally focused courses (2.4, 4.1, 4.2)", "master's", "integrated master's (2.2)"]
  levels: ["fheq:6", "fheq:7", "fqheis:10", "fqheis:11"]
  providers: ["UK higher education providers"]
whoMustUse: "none-stated; it is a reference point, not a requirement (D1, front matter)"
howUsed: ["design", "approval", "review", "other: external examining (front matter, 2.12); PSRBs (front matter); prospective students and employers (front matter)"]
doesNot: "it does not prescribe teaching, learning or assessment, interpret legislation or carry statutory or regulatory requirements; its standards are not universal competence standards (D1, front matter; 4.5)"
beneficiary: the student
statedScope: "\"This QAA Subject Benchmark Statement for Education Studies defines what can be expected of a graduate in terms of what they might know, do and understand at the end of their studies.\" (D1, front matter); \"The following benchmark standards are defined for students studying a single honours or master's degree in Education Studies.\" (D1, 4.1)"
statedSubjects:
  - { name: "Education Studies", locator: "(D1, title; 1.1; 4.1)", kind: "subject", codes: [{ scheme: "hecos", code: "100459", label: "education studies" }, { scheme: "cah", code: "CAH22-01-01", label: "education" }] }
  - { name: "allied areas including teacher training", locator: "(D1, front matter)", kind: "subject", codes: [{ scheme: "cah", code: "CAH22-01-02", label: "teacher training" }] }
  - { name: "teaching studies; programmes that offer qualified teacher status", locator: "(D1, 3.3; 3.7)", kind: "programme title", codes: [{ scheme: "hecos", code: "101246", label: "professional practice in education" }] }
  - { name: "mathematics education, inclusive education, lifelong learning", locator: "(D1, 4.2)", kind: "specialism", codes: [] }
subjects: see front matter (subjectScope subjects)
```

### S3 Structure
<!-- label: both; status: drafted; basis: primary -->
```yaml
components:
  - { number: "1.1", order: 3, componentType: paragraph, parent: "section 1", heading: "Context and purposes of an Education Studies degree", gloss: "what the subject studies; its contexts" }
  - { number: "1.2", order: 4, componentType: paragraph, parent: "section 1", heading: "Purposes and characteristics of an Education Studies degree", gloss: "transformative purpose; praxis" }
  - { number: "1.3", order: 5, componentType: paragraph, parent: "section 1", heading: "Purposes and characteristics of an Education Studies degree", gloss: "subject, field or discipline" }
  - { number: "1.4", order: 6, componentType: paragraph, parent: "section 1", heading: "Purposes and characteristics of an Education Studies degree", gloss: "ethics throughout; a changing subject" }
  - { number: "1.5", order: 7, componentType: paragraph, parent: "section 1", heading: "Purposes and characteristics of an Education Studies degree", gloss: "diverse perspectives; reciprocal learning" }
  - { number: "1.6", order: 8, componentType: paragraph, parent: "section 1", heading: "Purposes and characteristics of an Education Studies degree", gloss: "debate, critical capability and careers" }
  - { number: "1.7", order: 9, componentType: paragraph, parent: "section 1", heading: "Equity, diversity and inclusion", gloss: "EDI vision" }
  - { number: "1.8", order: 10, componentType: paragraph, parent: "section 1", heading: "Equity, diversity and inclusion", gloss: "co-constructing equitable curricula" }
  - { number: "1.9", order: 11, componentType: paragraph, parent: "section 1", heading: "Equity, diversity and inclusion", gloss: "questioning dominant language and knowledge" }
  - { number: "1.10", order: 12, componentType: paragraph, parent: "section 1", heading: "Equity, diversity and inclusion", gloss: "learning across the lifespan" }
  - { number: "1.11", order: 13, componentType: paragraph, parent: "section 1", heading: "Equity, diversity and inclusion", gloss: "EDI and a just society" }
  - { number: "1.12", order: 14, componentType: paragraph, parent: "section 1", heading: "Equity, diversity and inclusion", gloss: "unique contributions; ideologies and communities" }
  - { number: "1.13", order: 15, componentType: paragraph, parent: "section 1", heading: "Equity, diversity and inclusion", gloss: "agency, reflection, respect" }
  - { number: "1.14", order: 16, componentType: paragraph, parent: "section 1", heading: "Equity, diversity and inclusion", gloss: "digital technologies and AI through an EDI lens" }
  - { number: "1.15", order: 17, componentType: paragraph, parent: "section 1", heading: "Accessibility and the needs of disabled students", gloss: "Equality Act duty to anticipate" }
  - { number: "1.16", order: 18, componentType: paragraph, parent: "section 1", heading: "Accessibility and the needs of disabled students", gloss: "open to all; accessibility a must" }
  - { number: "1.17", order: 19, componentType: paragraph, parent: "section 1", heading: "Accessibility and the needs of disabled students", gloss: "design fits mode of delivery" }
  - { number: "1.18", order: 20, componentType: paragraph, parent: "section 1", heading: "Accessibility and the needs of disabled students", gloss: "non-standard routes; equal access" }
  - { number: "1.19", order: 21, componentType: paragraph, parent: "section 1", heading: "Accessibility and the needs of disabled students", gloss: "professional advice and student voice" }
  - { number: "1.20", order: 22, componentType: paragraph, parent: "section 1", heading: "Accessibility and the needs of disabled students", gloss: "accessible curriculum; clear assessment" }
  - { number: "1.21", order: 23, componentType: paragraph, parent: "section 1", heading: "Accessibility and the needs of disabled students", gloss: "anticipating barriers" }
  - { number: "1.22", order: 24, componentType: paragraph, parent: "section 1", heading: "Accessibility and the needs of disabled students", gloss: "anticipatory reasonable adjustments" }
  - { number: "1.23", order: 25, componentType: paragraph, parent: "section 1", heading: "Accessibility and the needs of disabled students", gloss: "access in person and online" }
  - { number: "1.24", order: 26, componentType: paragraph, parent: "section 1", heading: "Accessibility and the needs of disabled students", gloss: "accessible placements" }
  - { number: "1.25", order: 27, componentType: paragraph, parent: "section 1", heading: "Education for sustainable development", gloss: "ESD vision" }
  - { number: "1.26", order: 28, componentType: paragraph, parent: "section 1", heading: "Education for sustainable development", gloss: "UN SDGs and ESD guidance" }
  - { number: "1.27", order: 29, componentType: paragraph, parent: "section 1", heading: "Education for sustainable development", gloss: "competences for sustainable practice" }
  - { number: "1.28", order: 30, componentType: paragraph, parent: "section 1", heading: "Education for sustainable development", gloss: "interdisciplinary basis of sustainability" }
  - { number: "1.29", order: 31, componentType: paragraph, parent: "section 1", heading: "Education for sustainable development", gloss: "complexities of sustainability" }
  - { number: "1.30", order: 32, componentType: paragraph, parent: "section 1", heading: "Education for sustainable development", gloss: "education for a sustainable future" }
  - { number: "1.31", order: 33, componentType: paragraph, parent: "section 1", heading: "Education for sustainable development", gloss: "personal sustainability and well-being" }
  - { number: "1.32", order: 34, componentType: paragraph, parent: "section 1", heading: "Employability, entrepreneurship and enterprise education", gloss: "employability and enterprise vision" }
  - { number: "1.33", order: 35, componentType: paragraph, parent: "section 1", heading: "Employability, entrepreneurship and enterprise education", gloss: "entrepreneurship beyond employment" }
  - { number: "1.34", order: 36, componentType: paragraph, parent: "section 1", heading: "Employability, entrepreneurship and enterprise education", gloss: "qualities the subject fosters" }
  - { number: "1.35", order: 37, componentType: paragraph, parent: "section 1", heading: "Employability, entrepreneurship and enterprise education", gloss: "education in its widest sense" }
  - { number: "1.36", order: 38, componentType: paragraph, parent: "section 1", heading: "Employability, entrepreneurship and enterprise education", gloss: "graduate destinations" }
  - { number: "1.37", order: 39, componentType: paragraph, parent: "section 1", heading: "Employability, entrepreneurship and enterprise education", gloss: "enterprise embedded, not added" }
  - { number: "1.38", order: 40, componentType: paragraph, parent: "section 1", heading: "Employability, entrepreneurship and enterprise education", gloss: "innovation and adaptability" }
  - { number: "1.39", order: 41, componentType: paragraph, parent: "section 1", heading: "Employability, entrepreneurship and enterprise education", gloss: "ethical entrepreneurial disposition" }
  - { number: "1.40", order: 42, componentType: stem, parent: "section 1", heading: "Employability, entrepreneurship and enterprise education", gloss: "four aims of the subject" }
  - { number: "1.41", order: 43, componentType: paragraph, parent: "section 1", heading: "Artificial intelligence", gloss: "AI vision" }
  - { number: "1.42", order: 44, componentType: stem, parent: "section 1", heading: "Artificial intelligence", gloss: "eleven principles for understanding AI" }
  - { number: "1.43", order: 45, componentType: paragraph, parent: "section 1", heading: "Artificial intelligence", gloss: "course teams and the AI principles" }
  - { number: "2.1", order: 47, componentType: stem, parent: "section 2", heading: "Distinctive features of the Education Studies course", gloss: "eleven common features of courses" }
  - { number: "2.2", order: 48, componentType: paragraph, parent: "section 2", heading: "Progression", gloss: "progression through levels" }
  - { number: "2.3", order: 49, componentType: paragraph, parent: "section 2", heading: "Progression", gloss: "readiness for postgraduate study" }
  - { number: "2.4", order: 50, componentType: paragraph, parent: "section 2", heading: "Progression", gloss: "joint and combined degrees" }
  - { number: "2.5", order: 51, componentType: paragraph, parent: "section 2", heading: "Progression", gloss: "exit awards" }
  - { number: "2.6", order: 52, componentType: paragraph, parent: "section 2", heading: "Flexibility", gloss: "course length by nation; part-time" }
  - { number: "2.7", order: 53, componentType: paragraph, parent: "section 2", heading: "Flexibility", gloss: "modes, formats and credit" }
  - { number: "2.8", order: 54, componentType: paragraph, parent: "section 2", heading: "Partnership", gloss: "partnership delivery" }
  - { number: "2.9", order: 55, componentType: paragraph, parent: "section 2", heading: "Monitoring and review", gloss: "periodic review; student voice" }
  - { number: "2.10", order: 56, componentType: paragraph, parent: "section 2", heading: "Monitoring and review", gloss: "externality" }
  - { number: "2.11", order: 57, componentType: paragraph, parent: "section 2", heading: "Monitoring and review", gloss: "professional accreditation" }
  - { number: "2.12", order: 58, componentType: paragraph, parent: "section 2", heading: "Monitoring and review", gloss: "external examining" }
  - { number: "3.1", order: 60, componentType: paragraph, parent: "section 3", heading: "Content, structure and delivery", gloss: "how content shapes teaching and assessment" }
  - { number: "3.2", order: 61, componentType: paragraph, parent: "section 3", heading: "Content", gloss: "skills for study and employment" }
  - { number: "3.3", order: 62, componentType: area, parent: "section 3", heading: "Content", gloss: "three curricular areas; Figure 1" }
  - { number: "3.4", order: 63, componentType: paragraph, parent: "section 3", heading: "Content", gloss: "fluid boundaries between the areas" }
  - { number: "3.5", order: 64, componentType: paragraph, parent: "section 3", heading: "Subject-specific curriculum", gloss: "programmes choose their focus" }
  - { number: "3.6", order: 65, componentType: area, parent: "section 3", heading: "Subject-specific curriculum", gloss: "twenty subject-specific knowledge areas" }
  - { number: "3.7", order: 66, componentType: paragraph, parent: "section 3", heading: "Practice-based curriculum", gloss: "placements and practice" }
  - { number: "3.8", order: 67, componentType: area, parent: "section 3", heading: "Practice-based curriculum", gloss: "fourteen practice-based opportunities" }
  - { number: "3.9", order: 68, componentType: paragraph, parent: "section 3", heading: "Transversal curriculum", gloss: "transversal knowledge and skills" }
  - { number: "3.10", order: 69, componentType: area, parent: "section 3", heading: "Transversal curriculum", gloss: "twenty-three transversal areas" }
  - { number: "3.11", order: 70, componentType: practice, parent: "section 3", heading: "Teaching and learning", gloss: "inclusive, interactive, reflective teaching" }
  - { number: "3.12", order: 71, componentType: practice, parent: "section 3", heading: "Teaching and learning", gloss: "seven ways courses support success" }
  - { number: "3.13", order: 72, componentType: practice, parent: "section 3", heading: "Teaching and learning", gloss: "modelling effective practice" }
  - { number: "3.14", order: 73, componentType: paragraph, parent: "section 3", heading: "Teaching and learning", gloss: "alignment with professional bodies" }
  - { number: "3.15", order: 74, componentType: paragraph, parent: "section 3", heading: "Teaching and learning", gloss: "contemporary issues and the themes" }
  - { number: "3.16", order: 75, componentType: paragraph, parent: "section 3", heading: "Assessment", gloss: "assessment aligned to outcomes" }
  - { number: "3.17", order: 76, componentType: practice, parent: "section 3", heading: "Assessment", gloss: "twenty-three assessment methods" }
  - { number: "3.18", order: 77, componentType: practice, parent: "section 3", heading: "Assessment", gloss: "academic integrity and AI" }
  - { number: "3.19", order: 78, componentType: practice, parent: "section 3", heading: "Assessment", gloss: "accessible, inclusive assessment" }
  - { number: "3.20", order: 79, componentType: paragraph, parent: "section 3", heading: "Assessment", gloss: "staff workload and sustainable courses" }
  - { number: "3.21", order: 80, componentType: practice, parent: "section 3", heading: "Assessment", gloss: "authentic assessment" }
  - { number: "3.22", order: 81, componentType: practice, parent: "section 3", heading: "Assessment", gloss: "assessed placements" }
  - { number: "3.23", order: 82, componentType: paragraph, parent: "section 3", heading: "Assessment", gloss: "a varied assessment diet" }
  - { number: "3.24", order: 83, componentType: practice, parent: "section 3", heading: "Assessment", gloss: "forward-facing feedback" }
  - { number: "4.1", order: 85, componentType: paragraph, parent: "section 4", heading: "Introduction", gloss: "who the standards are for" }
  - { number: "4.2", order: 86, componentType: paragraph, parent: "section 4", heading: "Introduction", gloss: "professional training contexts" }
  - { number: "4.3", order: 87, componentType: paragraph, parent: "section 4", heading: "Introduction", gloss: "threshold, typical and excellent defined; Annex D" }
  - { number: "4.4", order: 88, componentType: paragraph, parent: "section 4", heading: "Introduction", gloss: "master's standards as a guide" }
  - { number: "4.5", order: 89, componentType: paragraph, parent: "section 4", heading: "Introduction", gloss: "not competence standards; the standards table follows" }
  - { number: "4.6", order: 90, componentType: paragraph, parent: "section 4", heading: "Threshold level", gloss: "professional competences row" }
  - { number: "4.7", order: 91, componentType: paragraph, parent: "section 4", heading: "Threshold level", gloss: "professional competence for accredited awards; back matter follows" }
  - { number: "1", componentType: section, parent: none, heading: "Context and purposes of an Education Studies degree", gloss: "section 1" }
  - { number: "2", componentType: section, parent: none, heading: "Distinctive features of the Education Studies course", gloss: "section 2" }
  - { number: "3", componentType: section, parent: none, heading: "Content, structure and delivery", gloss: "section 3" }
  - { number: "4", componentType: section, parent: none, heading: "Benchmark standards", gloss: "section 4" }
excluded:
  - { number: "none", heading: "About this Statement; How can I use this document?; Relationship to legislation; Additional sector reference points", kind: "other: front matter, read for S1, S2 and SB6" }
  - { number: "none", heading: "section heading lines 1 to 4", kind: "other: headings, recorded in SECTIONS" }
  - { number: "none", heading: "Figure 1: The knowledge areas of education studies", kind: "other: figure labels held inside 3.3, read for SB3" }
  - { number: "none", heading: "Membership of the Advisory Group", kind: "other: back matter held inside the skeleton's 4.7 span, read for S7 and S8 (editions 2019 minor update, 2015, 2007, 2000)" }
```

### S4 Statements
<!-- label: both; status: drafted; basis: primary. Only standards (D-std-0002 (a)): 130 records. `source` is the issuer's statement exactly as its span holds it (D-std-0014). -->
```yaml
- id: qaa/education-studies-2025/1.6
  locator: { number: "1.6", headingPath: ["Context and purposes of an Education Studies degree", "Purposes and characteristics of an Education Studies degree"] }
  span: { start: 9994, end: 10577 }
  source: "1.6 Students can participate in, construct and contest discourses, exemplified by reference to debate about values, personal and social engagement, educational practices and how these relate to communities and societies. Students have opportunities to develop their critical capabilities through the selection, analysis and synthesis of various perspectives, and are able therefore to position themselves in a reasoned manner in a changing world. Students are prepared for a broad range of careers and are equipped to engage in lifelong learning in the course of their working lives."
  stem: none
  statementType: outcome
  rung: none
  force: will
  level: fheq:6
  appliesTo: "students of Education Studies"
  addressee: learner
  verbs: ["participate", "construct", "contest", "develop", "position"]
  about: "taking a reasoned position in educational debate"
  themes: [none]
  domain: understanding
  award: ["bachelor's with honours"]
  gradeOf: none
  paraphrase: "Students take part in, build and challenge debates about values, engagement, educational practice and community; by choosing, analysing and combining viewpoints they grow critical capability and so can hold a reasoned stance in a world that keeps changing, ready for many careers and for learning across working life."
  quote: full   # the issuer's statement is in `source` (D-std-0014)
  audience: both
  subjects: inherited
- id: qaa/education-studies-2025/1.9
  locator: { number: "1.9", headingPath: ["Context and purposes of an Education Studies degree", "Equity, diversity and inclusion"] }
  span: { start: 11185, end: 11418 }
  source: "1.9 Students are able to interrogate key concepts and terms, acknowledging the entrenchment of dominant systems of language, knowledge and thought in both historical and current contexts in both formal, informal and hidden curricula."
  stem: none
  statementType: outcome
  rung: none
  force: will
  level: fheq:6
  appliesTo: "students of Education Studies"
  addressee: learner
  verbs: ["interrogate", "acknowledging"]
  about: "questioning entrenched language, knowledge and thought"
  themes: [theme:edi]
  domain: understanding
  award: ["bachelor's with honours"]
  gradeOf: none
  paraphrase: "Students can question core concepts and terms, recognising how dominant ways of speaking, knowing and thinking have become fixed, in the past and now, across formal, informal and hidden curricula."
  quote: full   # the issuer's statement is in `source` (D-std-0014)
  audience: both
  subjects: inherited
- id: qaa/education-studies-2025/1.11
  locator: { number: "1.11", headingPath: ["Context and purposes of an Education Studies degree", "Equity, diversity and inclusion"] }
  span: { start: 11640, end: 11889 }
  source: "1.11 Students are able to engage with issues of EDI, appreciating what it is to contribute to a just society, recognising diverse standpoints, and defining their own position within and beyond the context of rights, duties, responsibilities and law."
  stem: none
  statementType: outcome
  rung: none
  force: will
  level: fheq:6
  appliesTo: "students of Education Studies"
  addressee: learner
  verbs: ["engage", "appreciating", "recognising", "defining"]
  about: "engaging with EDI and taking a position on justice"
  themes: [theme:edi]
  domain: understanding
  award: ["bachelor's with honours"]
  gradeOf: none
  paraphrase: "Students can work with questions of equity, diversity and inclusion, seeing what helping to build a just society involves, recognising differing standpoints and setting out where they stand, both in terms of rights, duties, responsibilities and law and beyond them."
  quote: full   # the issuer's statement is in `source` (D-std-0014)
  audience: both
  subjects: inherited
- id: qaa/education-studies-2025/1.13
  locator: { number: "1.13", headingPath: ["Context and purposes of an Education Studies degree", "Equity, diversity and inclusion"] }
  span: { start: 12224, end: 12460 }
  source: "1.13 Courses provide students with agency to reflect, question and engage. Students are skilled in reflection and able to understand their own uniqueness, while demonstrating due respect for differing and divergent opinions from others."
  stem: none
  statementType: outcome
  rung: none
  force: will
  level: fheq:6
  appliesTo: "Education Studies courses and their students"
  addressee: both
  verbs: ["reflect", "question", "engage", "understand", "demonstrating"]
  about: "reflection, self-understanding and respect for divergent views"
  themes: [theme:edi]
  domain: generic-skill
  award: ["bachelor's with honours"]
  gradeOf: none
  paraphrase: "Courses give students the agency to reflect, question and take part; students are practised in reflection and can see what is distinctive about themselves while showing proper respect for views that differ from or oppose their own."
  quote: full   # the issuer's statement is in `source` (D-std-0014)
  audience: both
  subjects: inherited
- id: qaa/education-studies-2025/1.15
  locator: { number: "1.15", headingPath: ["Context and purposes of an Education Studies degree", "Accessibility and the needs of disabled students"] }
  span: { start: 12929, end: 13134 }
  source: "1.15 The Equality Act 2010 places a legal duty on education providers to adopt a proactive rather than reactive approach, where issues of accessibility in teaching, learning and assessment are anticipated."
  stem: none
  statementType: requirement
  rung: none
  force: must   # D-std-0016: "duty" read as must
  level: none
  appliesTo: "Education Studies courses and their teams"
  addressee: provider
  verbs: ["places", "adopt", "anticipated"]
  about: "the Equality Act duty to anticipate accessibility issues"
  themes: [theme:accessibility]
  domain: none
  award: ["none"]
  gradeOf: none
  paraphrase: "The Equality Act 2010 puts a legal duty on education providers to act ahead of need rather than after it, foreseeing accessibility issues in teaching, learning and assessment."
  quote: full   # the issuer's statement is in `source` (D-std-0014)
  audience: practitioner
  subjects: inherited
- id: qaa/education-studies-2025/1.16
  locator: { number: "1.16", headingPath: ["Context and purposes of an Education Studies degree", "Accessibility and the needs of disabled students"] }
  span: { start: 13142, end: 13574 }
  source: "1.16 Education Studies is an inclusive discipline, and is open to all individuals, including students from a wide range of social and economic backgrounds, students with a broad spectrum of specific learning needs, students with access requirements, and neurodivergent students. Accessibility is a moral and legal imperative, and accessibility must be considered in course design as well as in planning the wider student experience."
  stem: none
  statementType: requirement
  rung: none
  force: must
  level: none
  appliesTo: "Education Studies courses and their teams"
  addressee: provider
  verbs: ["considered"]
  about: "accessibility in course design and the wider student experience"
  themes: [theme:accessibility]
  domain: none
  award: ["none"]
  gradeOf: none
  paraphrase: "The subject is inclusive and open to everyone, including students from varied social and economic backgrounds, with specific learning needs, neurodivergent students and those who need particular access arrangements; it treats accessibility as both a moral and a legal imperative that must be considered in course design and in planning the wider student experience."
  quote: full   # the issuer's statement is in `source` (D-std-0014)
  audience: practitioner
  subjects: inherited
- id: qaa/education-studies-2025/1.20
  locator: { number: "1.20", headingPath: ["Context and purposes of an Education Studies degree", "Accessibility and the needs of disabled students"] }
  span: { start: 14125, end: 14393 }
  source: "1.20 Course curriculum, content and assessment need to be accessible to all learners, including those of diverse cultures, disabilities, neurodivergencies, identities and demographics. All assessments should be characterised by clarity of both purpose and expectation."
  stem: none
  statementType: requirement
  rung: none
  force: should
  level: none
  appliesTo: "Education Studies courses and their teams"
  addressee: provider
  verbs: ["characterised"]
  about: "accessible curriculum and clear assessment"
  themes: [theme:accessibility]
  domain: none
  award: ["none"]
  gradeOf: none
  paraphrase: "Course curriculum, content and assessment need to be open to every learner, whatever their culture, disability, neurodivergence, identity or background, and every assessment should be clear about its purpose and what it expects."
  quote: full   # the issuer's statement is in `source` (D-std-0014)
  audience: practitioner
  subjects: inherited
- id: qaa/education-studies-2025/1.21
  locator: { number: "1.21", headingPath: ["Context and purposes of an Education Studies degree", "Accessibility and the needs of disabled students"] }
  span: { start: 14394, end: 14642 }
  source: "1.21 Course teams will need to anticipate potential barriers which may be experienced by learners. Strategies for delivery can include the provision of support plans, working closely with institutional support, and signposting to relevant services."
  stem: none
  statementType: requirement
  rung: none
  force: will
  level: none
  appliesTo: "Education Studies courses and their teams"
  addressee: provider
  verbs: ["anticipate"]
  about: "anticipating barriers to learning"
  themes: [theme:accessibility]
  domain: none
  award: ["none"]
  gradeOf: none
  paraphrase: "Course teams will need to foresee barriers learners might meet; delivery strategies can include support plans, close work with institutional support services and signposting to them."
  quote: full   # the issuer's statement is in `source` (D-std-0014)
  audience: practitioner
  subjects: inherited
- id: qaa/education-studies-2025/1.22
  locator: { number: "1.22", headingPath: ["Context and purposes of an Education Studies degree", "Accessibility and the needs of disabled students"] }
  span: { start: 14643, end: 14862 }
  source: "1.22 In line with the Equality Act 2010, all courses should make anticipatory reasonable adjustments to teaching, learning and assessment in enabling all students to achieve the intended learning outcomes of the course."
  stem: none
  statementType: requirement
  rung: none
  force: should
  level: none
  appliesTo: "Education Studies courses and their teams"
  addressee: provider
  verbs: ["make"]
  about: "anticipatory reasonable adjustments"
  themes: [theme:accessibility]
  domain: none
  award: ["none"]
  gradeOf: none
  paraphrase: "In line with the Equality Act 2010, every course should adjust its teaching, learning and assessment in advance and reasonably, so that all students can reach its intended learning outcomes."
  quote: full   # the issuer's statement is in `source` (D-std-0014)
  audience: practitioner
  subjects: inherited
- id: qaa/education-studies-2025/1.23
  locator: { number: "1.23", headingPath: ["Context and purposes of an Education Studies degree", "Accessibility and the needs of disabled students"] }
  span: { start: 14863, end: 15114 }
  source: "1.23 Course teams should consider accessibility for all students, both in person and through digital modes of delivery, ensuring that all students have access to learning resources, including assistive technology, to support their individual learning."
  stem: none
  statementType: requirement
  rung: none
  force: should
  level: none
  appliesTo: "Education Studies courses and their teams"
  addressee: provider
  verbs: ["consider", "ensuring"]
  about: "accessibility in person and online, including assistive technology"
  themes: [theme:accessibility]
  domain: none
  award: ["none"]
  gradeOf: none
  paraphrase: "Course teams should think about accessibility for every student, face to face and through digital delivery, so that all can reach the learning resources they need, assistive technology included."
  quote: full   # the issuer's statement is in `source` (D-std-0014)
  audience: practitioner
  subjects: inherited
- id: qaa/education-studies-2025/1.24
  locator: { number: "1.24", headingPath: ["Context and purposes of an Education Studies degree", "Accessibility and the needs of disabled students"] }
  span: { start: 15115, end: 15427 }
  source: "1.24 Where a placement element is offered, effective practice in accessibility and student well-being should be considered. This may include the consideration of other options, a choice in assessment, and ensuring that employment and careers guidance and opportunities are cognisant of the needs of all students."
  stem: none
  statementType: requirement
  rung: none
  force: should
  level: none
  appliesTo: "Education Studies courses and their teams"
  addressee: provider
  verbs: ["offered", "considered"]
  about: "accessibility and well-being on placements"
  themes: [theme:accessibility]
  domain: none
  award: ["none"]
  gradeOf: none
  paraphrase: "Where a course offers a placement, it should consider good practice on accessibility and on students' well-being, which may mean alternative options, choice in assessment and careers guidance and openings that take account of every student's needs."
  quote: full   # the issuer's statement is in `source` (D-std-0014)
  audience: practitioner
  subjects: inherited
- id: qaa/education-studies-2025/1.30
  locator: { number: "1.30", headingPath: ["Context and purposes of an Education Studies degree", "Education for sustainable development"] }
  span: { start: 17153, end: 17572 }
  source: "1.30 Education Studies students understand the unique and essential role of education in delivering a sustainable future through the provision of learning across the lifespan and throughout diverse contexts inclusive of formal and informal education. Although there can be discrete parts of programmes that engage with such themes, course teams should consider teaching, content and assessment within a broader context."
  stem: none
  statementType: expectation
  rung: none
  force: should
  level: fheq:6
  appliesTo: "Education Studies courses and their students"
  addressee: both
  verbs: ["understand", "consider"]
  about: "education and a sustainable future"
  themes: [theme:esd]
  domain: understanding
  award: ["bachelor's with honours"]
  gradeOf: none
  paraphrase: "Students understand the distinctive and vital part education plays in a sustainable future, through learning across life and in many formal and informal settings; although some parts of a course may treat these themes on their own, course teams should consider teaching, content and assessment in a broader frame."
  quote: full   # the issuer's statement is in `source` (D-std-0014)
  audience: both
  subjects: inherited
- id: qaa/education-studies-2025/1.31
  locator: { number: "1.31", headingPath: ["Context and purposes of an Education Studies degree", "Education for sustainable development"] }
  span: { start: 17573, end: 17808 }
  source: "1.31 Education Studies students can craft their own personal sustainability from both an ecological and psychological perspective, working reflectively to monitor and manage their own well-being and that of others in their environment."
  stem: none
  statementType: outcome
  rung: none
  force: will
  level: fheq:6
  appliesTo: "students of Education Studies"
  addressee: learner
  verbs: ["craft", "working", "monitor", "manage"]
  about: "personal sustainability and well-being"
  themes: [theme:esd]
  domain: generic-skill
  award: ["bachelor's with honours"]
  gradeOf: none
  paraphrase: "Students can build a personal sustainability of their own, both ecological and psychological, keeping watch over and looking after their own well-being and the well-being of people around them, reflectively."
  quote: full   # the issuer's statement is in `source` (D-std-0014)
  audience: both
  subjects: inherited
- id: qaa/education-studies-2025/1.43
  locator: { number: "1.43", headingPath: ["Context and purposes of an Education Studies degree", "Artificial intelligence"] }
  span: { start: 22698, end: 23187 }
  source: "1.43 Course teams should also engage with the above principles for the purposes of curriculum design, assessment, recruitment and research. It may be advantageous for course teams to consider sustained engagement with AI throughout their programmes, as opposed to limiting it to specific modules or stages of study. They may acknowledge that AI creates opportunities, as well as creating issues, and that t here needs to be critical engagement with its potential strengths and limitations."
  stem: none
  statementType: requirement
  rung: none
  force: should
  level: none
  appliesTo: "Education Studies courses and their teams"
  addressee: provider
  verbs: ["engage"]
  about: "course teams applying the AI principles"
  themes: [theme:generative-ai]
  domain: none
  award: ["none"]
  gradeOf: none
  paraphrase: "Course teams should also work with the AI principles of 1.42 in curriculum design, assessment, recruitment and research; they may find value in engaging with AI across a whole programme rather than in particular modules or stages, recognising that AI brings both openings and problems and calls for critical engagement with its strengths and limits."
  quote: full   # the issuer's statement is in `source` (D-std-0014)
  audience: practitioner
  subjects: inherited
- id: qaa/education-studies-2025/2.2
  locator: { number: "2.2", headingPath: ["Distinctive features of the Education Studies course", "Progression"] }
  span: { start: 26075, end: 26825 }
  source: "2.2 Over the course of a standard undergraduate degree with honours (FHEQ Level 6; FQHEIS Level 10) or, if available, an integrated master's degree (FHEQ Level 7; FQHEIS Level 11), Education Studies students will progress from one level of study to the next, in line with the regulations and processes for each institution. However, it is expected that each level would see the attainment of knowledge, expertise and experience that builds towards\n\n10\nthe final achievement of meeting the threshold (and, if specified, higher-level) subject- specific and generic skills listed in this Statement. This will usually include successful completion and the award of credit for the full range of learning and assessment, including any practical components."
  stem: none
  statementType: expectation
  rung: none
  force: will
  level: fheq:6
  appliesTo: "students on honours and integrated master's courses"
  addressee: both
  verbs: ["progress", "include"]
  about: "progression through the levels to the threshold"
  themes: [none]
  domain: none
  award: ["bachelor's with honours", "integrated master's"]
  gradeOf: none
  paraphrase: "Students on an honours degree (FHEQ Level 6; FQHEIS Level 10) or, where offered, an integrated master's (FHEQ Level 7; FQHEIS Level 11) will move through the levels under each institution's rules, each level adding knowledge, expertise and experience towards meeting the threshold skills of the statement (and any higher ones set); this will usually mean passing, and gaining credit for, all learning and assessment, practical parts included."
  quote: full   # the issuer's statement is in `source` (D-std-0014)
  audience: both
  subjects: inherited
- id: qaa/education-studies-2025/2.3
  locator: { number: "2.3", headingPath: ["Distinctive features of the Education Studies course", "Progression"] }
  span: { start: 26826, end: 27232 }
  source: "2.3 Upon graduation from an undergraduate degree, it would be expected that a student who had achieved a second-class degree or higher would be capable of, and equipped for, undertaking postgraduate study in education or a related discipline. Entry requirements to postgraduate courses are, however, determined by individual providers and may require specified levels of achievement at undergraduate level."
  stem: none
  statementType: outcome
  rung: none
  force: must   # D-std-0016: "requirements" read as must
  level: fheq:6
  appliesTo: "students of Education Studies"
  addressee: learner
  verbs: ["undertaking", "determined"]
  about: "readiness for postgraduate study"
  themes: [none]
  domain: none
  award: ["bachelor's with honours"]
  gradeOf: none
  paraphrase: "A graduate with a second-class degree or better would be expected to be ready and able to take on postgraduate study in education or a related field, though entry rules belong to each institution and may ask for set levels of undergraduate achievement."
  quote: full   # the issuer's statement is in `source` (D-std-0014)
  audience: both
  subjects: inherited
- id: qaa/education-studies-2025/2.4
  locator: { number: "2.4", headingPath: ["Distinctive features of the Education Studies course", "Progression"] }
  span: { start: 27233, end: 27710 }
  source: "2.4 Students studying Education Studies courses as part of a combined or joint degree with other subjects (including courses that specify major and minor options) will achieve core elements of the specific and generic skills outlined in this Statement and will add others according to the areas covered in the other subject(s) of their degree. Additionally, they may explore the overlap between different disciplines, creating further opportunities for interdisciplinary study."
  stem: none
  statementType: outcome
  rung: none
  force: will
  level: fheq:6
  appliesTo: "students of Education Studies in joint or combined degrees"
  addressee: learner
  verbs: ["achieve", "add", "explore"]
  about: "core skills in joint and combined degrees"
  themes: [none]
  domain: none
  award: ["bachelor's with honours"]
  gradeOf: none
  paraphrase: "Students taking Education Studies within a joint or combined degree, major and minor routes included, will reach the core subject-specific and generic skills of the statement and add others from the rest of their degree, with the chance to explore where disciplines overlap."
  quote: full   # the issuer's statement is in `source` (D-std-0014)
  audience: both
  subjects: inherited
- id: qaa/education-studies-2025/2.9
  locator: { number: "2.9", headingPath: ["Distinctive features of the Education Studies course", "Monitoring and review"] }
  span: { start: 29772, end: 30418 }
  source: "2.9 Degree-awarding bodies, and their collaborative partnerships, routinely collect and analyse information and undertake periodic course review according to their own needs. Considering the student voice will form part of this. They draw on a range of external\n\n11\nreference points, including this Statement, to ensure that their provision aligns with sector norms. Monitoring and evaluation are a periodic assessment of a course, conducted internally or by external independent evaluators. Evaluation uses information from both current and historic monitoring to develop an understanding of student achievement or inform future course planning."
  stem: none
  statementType: requirement
  rung: none
  force: will
  level: none
  appliesTo: "Education Studies courses and their teams"
  addressee: provider
  verbs: ["form", "draw"]
  about: "periodic review and the student voice"
  themes: [none]
  domain: none
  award: ["none"]
  gradeOf: none
  paraphrase: "Degree-awarding bodies and their partners gather and analyse information and review courses periodically for their own needs; the student voice will form part of this, and they draw on external reference points, this statement among them, to keep provision in line with sector norms."
  quote: full   # the issuer's statement is in `source` (D-std-0014)
  audience: practitioner
  subjects: inherited
- id: qaa/education-studies-2025/2.10
  locator: { number: "2.10", headingPath: ["Distinctive features of the Education Studies course", "Monitoring and review"] }
  span: { start: 30419, end: 30716 }
  source: "2.10 Externality is an essential component of the quality assurance system in the UK. Providers will use external reviewers as part of periodic review to gain an independent perspective on any proposed changes and ensure threshold standards are achieved and content is appropriate for the subject."
  stem: none
  statementType: requirement
  rung: none
  force: will
  level: none
  appliesTo: "Education Studies courses and their teams"
  addressee: provider
  verbs: ["use", "ensure"]
  about: "external reviewers in periodic review"
  themes: [none]
  domain: none
  award: ["none"]
  gradeOf: none
  paraphrase: "Externality is essential to quality assurance in the UK: providers will use external reviewers in periodic review to gain an independent view of proposed changes and to make sure threshold standards are met and content suits the subject."
  quote: full   # the issuer's statement is in `source` (D-std-0014)
  audience: practitioner
  subjects: inherited
- id: qaa/education-studies-2025/3.9
  locator: { number: "3.9", headingPath: ["Content, structure and delivery", "Transversal curriculum"] }
  span: { start: 38646, end: 38972 }
  source: "3.9 Transversal knowledge and skills may not always be related to a particular job, task or discipline and can be used in a wider range of situations and work settings. As Education Studies is an interdisciplinary field, students will develop a wide range of transversal knowledge and skills that are useful for the workplace."
  stem: none
  statementType: outcome
  rung: none
  force: will
  level: fheq:6
  appliesTo: "students of Education Studies"
  addressee: learner
  verbs: ["develop"]
  about: "transversal knowledge and skills"
  themes: [none]
  domain: generic-skill
  award: ["bachelor's with honours"]
  gradeOf: none
  paraphrase: "Transversal knowledge and skills need not belong to one job, task or discipline and serve across many situations and workplaces; because Education Studies is interdisciplinary, students will build a broad set of them that help them at work."
  quote: full   # the issuer's statement is in `source` (D-std-0014)
  audience: both
  subjects: inherited
- id: qaa/education-studies-2025/3.10.b1
  locator: { number: "3.10.b1", headingPath: ["Content, structure and delivery", "Transversal curriculum"] }
  span: { start: 39180, end: 39284 }
  source: "apply numerical skills and work confidently with numbers, interpreting and analysing data as appropriate"
  stem: "3.10"
  statementType: expectation
  rung: none
  force: should
  level: fheq:6
  appliesTo: "Education Studies courses and their students"
  addressee: both
  verbs: ["apply", "work", "interpreting", "analysing"]
  about: "numeracy and data"
  themes: [none]
  domain: generic-skill
  award: ["bachelor's with honours"]
  gradeOf: none
  paraphrase: "Course teams should consider giving students opportunities to handle numbers with confidence, and interpret and analyse data where it fits."
  quote: full   # the issuer's statement is in `source` (D-std-0014)
  audience: both
  subjects: inherited
- id: qaa/education-studies-2025/3.10.b2
  locator: { number: "3.10.b2", headingPath: ["Content, structure and delivery", "Transversal curriculum"] }
  span: { start: 39287, end: 39363 }
  source: "be accountable and honest, able to take responsibility for their own actions"
  stem: "3.10"
  statementType: expectation
  rung: none
  force: should
  level: fheq:6
  appliesTo: "Education Studies courses and their students"
  addressee: both
  verbs: ["take"]
  about: "accountability and honesty"
  themes: [none]
  domain: generic-skill
  award: ["bachelor's with honours"]
  gradeOf: none
  paraphrase: "Course teams should consider giving students opportunities to be honest and answerable, owning the results of their own actions."
  quote: full   # the issuer's statement is in `source` (D-std-0014)
  audience: both
  subjects: inherited
- id: qaa/education-studies-2025/3.10.b3
  locator: { number: "3.10.b3", headingPath: ["Content, structure and delivery", "Transversal curriculum"] }
  span: { start: 39366, end: 39499 }
  source: "communicate for different purposes, including, but not limited to, description, explanation, persuasion, evaluation and summarisation"
  stem: "3.10"
  statementType: expectation
  rung: none
  force: should
  level: fheq:6
  appliesTo: "Education Studies courses and their students"
  addressee: both
  verbs: ["communicate"]
  about: "communicating for different purposes"
  themes: [none]
  domain: generic-skill
  award: ["bachelor's with honours"]
  gradeOf: none
  paraphrase: "Course teams should consider giving students opportunities to communicate for varied ends, such as describing, explaining, persuading, judging and summing up."
  quote: full   # the issuer's statement is in `source` (D-std-0014)
  audience: both
  subjects: inherited
- id: qaa/education-studies-2025/3.10.b4
  locator: { number: "3.10.b4", headingPath: ["Content, structure and delivery", "Transversal curriculum"] }
  span: { start: 39502, end: 39573 }
  source: "comprehend, critically evaluate and utilise data in a range of contexts"
  stem: "3.10"
  statementType: expectation
  rung: none
  force: should
  level: fheq:6
  appliesTo: "Education Studies courses and their students"
  addressee: both
  verbs: ["comprehend", "evaluate", "utilise"]
  about: "understanding and using data"
  themes: [none]
  domain: generic-skill
  award: ["bachelor's with honours"]
  gradeOf: none
  paraphrase: "Course teams should consider giving students opportunities to understand, judge critically and use data in many settings."
  quote: full   # the issuer's statement is in `source` (D-std-0014)
  audience: both
  subjects: inherited
- id: qaa/education-studies-2025/3.10.b5
  locator: { number: "3.10.b5", headingPath: ["Content, structure and delivery", "Transversal curriculum"] }
  span: { start: 39576, end: 39642 }
  source: "critically evaluate sources to determine their relevance and value"
  stem: "3.10"
  statementType: expectation
  rung: none
  force: should
  level: fheq:6
  appliesTo: "Education Studies courses and their students"
  addressee: both
  verbs: ["evaluate", "determine"]
  about: "judging sources"
  themes: [none]
  domain: generic-skill
  award: ["bachelor's with honours"]
  gradeOf: none
  paraphrase: "Course teams should consider giving students opportunities to judge sources critically for how relevant and useful they are."
  quote: full   # the issuer's statement is in `source` (D-std-0014)
  audience: both
  subjects: inherited
- id: qaa/education-studies-2025/3.10.b6
  locator: { number: "3.10.b6", headingPath: ["Content, structure and delivery", "Transversal curriculum"] }
  span: { start: 39645, end: 39785 }
  source: "demonstrate an awareness of global competence and intercultural understanding, sensitive to the needs, backgrounds and experiences of others"
  stem: "3.10"
  statementType: expectation
  rung: none
  force: should
  level: fheq:6
  appliesTo: "Education Studies courses and their students"
  addressee: both
  verbs: ["demonstrate"]
  about: "global competence and intercultural understanding"
  themes: [none]
  domain: generic-skill
  award: ["bachelor's with honours"]
  gradeOf: none
  paraphrase: "Course teams should consider giving students opportunities to show global competence and intercultural understanding, alert to other people's needs, backgrounds and experiences."
  quote: full   # the issuer's statement is in `source` (D-std-0014)
  audience: both
  subjects: inherited
- id: qaa/education-studies-2025/3.10.b7
  locator: { number: "3.10.b7", headingPath: ["Content, structure and delivery", "Transversal curriculum"] }
  span: { start: 39788, end: 39847 }
  source: "demonstrate empathy through connection and active listening"
  stem: "3.10"
  statementType: expectation
  rung: none
  force: should
  level: fheq:6
  appliesTo: "Education Studies courses and their students"
  addressee: both
  verbs: ["demonstrate"]
  about: "empathy and active listening"
  themes: [none]
  domain: generic-skill
  award: ["bachelor's with honours"]
  gradeOf: none
  paraphrase: "Course teams should consider giving students opportunities to show empathy by connecting with others and listening actively."
  quote: full   # the issuer's statement is in `source` (D-std-0014)
  audience: both
  subjects: inherited
- id: qaa/education-studies-2025/3.10.b8
  locator: { number: "3.10.b8", headingPath: ["Content, structure and delivery", "Transversal curriculum"] }
  span: { start: 39850, end: 39947 }
  source: "engage in debate, negotiation and persuasion in a way that is respectful, helpful and appropriate"
  stem: "3.10"
  statementType: expectation
  rung: none
  force: should
  level: fheq:6
  appliesTo: "Education Studies courses and their students"
  addressee: both
  verbs: ["engage"]
  about: "respectful debate and negotiation"
  themes: [none]
  domain: generic-skill
  award: ["bachelor's with honours"]
  gradeOf: none
  paraphrase: "Course teams should consider giving students opportunities to debate, negotiate and persuade in ways that are respectful, helpful and fitting."
  quote: full   # the issuer's statement is in `source` (D-std-0014)
  audience: both
  subjects: inherited
- id: qaa/education-studies-2025/3.10.b9
  locator: { number: "3.10.b9", headingPath: ["Content, structure and delivery", "Transversal curriculum"] }
  span: { start: 39950, end: 40108 }
  source: "engage in verbal and/or non-verbal, visual and written skilled communications with others, demonstrating awareness of their audience and mode of communication"
  stem: "3.10"
  statementType: expectation
  rung: none
  force: should
  level: fheq:6
  appliesTo: "Education Studies courses and their students"
  addressee: both
  verbs: ["engage", "demonstrating"]
  about: "skilled communication across modes"
  themes: [none]
  domain: generic-skill
  award: ["bachelor's with honours"]
  gradeOf: none
  paraphrase: "Course teams should consider giving students opportunities to communicate skilfully in spoken, non-verbal, visual and written forms, with an eye to audience and medium."
  quote: full   # the issuer's statement is in `source` (D-std-0014)
  audience: both
  subjects: inherited
- id: qaa/education-studies-2025/3.10.b10
  locator: { number: "3.10.b10", headingPath: ["Content, structure and delivery", "Transversal curriculum"] }
  span: { start: 40111, end: 40285 }
  source: "engage in practices of self-care and resilience, and demonstrate the ability to look after themselves in the context of a field deeply situated within broader social contexts"
  stem: "3.10"
  statementType: expectation
  rung: none
  force: should
  level: fheq:6
  appliesTo: "Education Studies courses and their students"
  addressee: both
  verbs: ["engage", "demonstrate"]
  about: "self-care and resilience"
  themes: [none]
  domain: generic-skill
  award: ["bachelor's with honours"]
  gradeOf: none
  paraphrase: "Course teams should consider giving students opportunities to practise self-care and resilience and look after their own well-being in a field bound up with wider society."
  quote: full   # the issuer's statement is in `source` (D-std-0014)
  audience: both
  subjects: inherited
- id: qaa/education-studies-2025/3.10.b11
  locator: { number: "3.10.b11", headingPath: ["Content, structure and delivery", "Transversal curriculum"] }
  span: { start: 40288, end: 40351 }
  source: "engage with reflection, reflexivity and critical self-awareness"
  stem: "3.10"
  statementType: expectation
  rung: none
  force: should
  level: fheq:6
  appliesTo: "Education Studies courses and their students"
  addressee: both
  verbs: ["engage"]
  about: "reflection and reflexivity"
  themes: [none]
  domain: generic-skill
  award: ["bachelor's with honours"]
  gradeOf: none
  paraphrase: "Course teams should consider giving students opportunities to reflect, be reflexive and build critical self-awareness."
  quote: full   # the issuer's statement is in `source` (D-std-0014)
  audience: both
  subjects: inherited
- id: qaa/education-studies-2025/3.10.b12
  locator: { number: "3.10.b12", headingPath: ["Content, structure and delivery", "Transversal curriculum"] }
  span: { start: 40354, end: 40392 }
  source: "facilitate inclusion and accessibility"
  stem: "3.10"
  statementType: expectation
  rung: none
  force: should
  level: fheq:6
  appliesTo: "Education Studies courses and their students"
  addressee: both
  verbs: ["facilitate"]
  about: "inclusion and accessibility"
  themes: [none]
  domain: generic-skill
  award: ["bachelor's with honours"]
  gradeOf: none
  paraphrase: "Course teams should consider giving students opportunities to help bring about inclusion and accessibility."
  quote: full   # the issuer's statement is in `source` (D-std-0014)
  audience: both
  subjects: inherited
- id: qaa/education-studies-2025/3.10.b13
  locator: { number: "3.10.b13", headingPath: ["Content, structure and delivery", "Transversal curriculum"] }
  span: { start: 40395, end: 40491 }
  source: "identify problems and develop solutions, leveraging the best of creative thinking and enterprise"
  stem: "3.10"
  statementType: expectation
  rung: none
  force: should
  level: fheq:6
  appliesTo: "Education Studies courses and their students"
  addressee: both
  verbs: ["identify", "develop", "leveraging"]
  about: "creative problem-solving and enterprise"
  themes: [none]
  domain: generic-skill
  award: ["bachelor's with honours"]
  gradeOf: none
  paraphrase: "Course teams should consider giving students opportunities to spot problems and work out solutions using creative and enterprising thinking."
  quote: full   # the issuer's statement is in `source` (D-std-0014)
  audience: both
  subjects: inherited
- id: qaa/education-studies-2025/3.10.b14
  locator: { number: "3.10.b14", headingPath: ["Content, structure and delivery", "Transversal curriculum"] }
  span: { start: 40494, end: 40610 }
  source: "i mprove their own learning performance, with the ability to identify areas for development and ways to achieve this"
  stem: "3.10"
  statementType: expectation
  rung: none
  force: should
  level: fheq:6
  appliesTo: "Education Studies courses and their students"
  addressee: both
  verbs: ["identify"]
  about: "improving own learning"
  themes: [none]
  domain: generic-skill
  award: ["bachelor's with honours"]
  gradeOf: none
  paraphrase: "Course teams should consider giving students opportunities to raise their own learning performance by seeing what to develop and how to get there."
  quote: full   # the issuer's statement is in `source` (D-std-0014)
  audience: both
  subjects: inherited
- id: qaa/education-studies-2025/3.10.b15
  locator: { number: "3.10.b15", headingPath: ["Content, structure and delivery", "Transversal curriculum"] }
  span: { start: 40613, end: 40690 }
  source: "maintain a professional attitude, showing respect for others in the workplace"
  stem: "3.10"
  statementType: expectation
  rung: none
  force: should
  level: fheq:6
  appliesTo: "Education Studies courses and their students"
  addressee: both
  verbs: ["maintain", "showing"]
  about: "professional attitude"
  themes: [none]
  domain: generic-skill
  award: ["bachelor's with honours"]
  gradeOf: none
  paraphrase: "Course teams should consider giving students opportunities to keep a professional attitude and treat colleagues at work with respect."
  quote: full   # the issuer's statement is in `source` (D-std-0014)
  audience: both
  subjects: inherited
- id: qaa/education-studies-2025/3.10.b16
  locator: { number: "3.10.b16", headingPath: ["Content, structure and delivery", "Transversal curriculum"] }
  span: { start: 40693, end: 40832 }
  source: "organise, manage and appropriately arrange information, ensuring files, notes and documents are retrievable or discoverable at a later date"
  stem: "3.10"
  statementType: expectation
  rung: none
  force: should
  level: fheq:6
  appliesTo: "Education Studies courses and their students"
  addressee: both
  verbs: ["organise", "manage", "arrange"]
  about: "managing information"
  themes: [none]
  domain: generic-skill
  award: ["bachelor's with honours"]
  gradeOf: none
  paraphrase: "Course teams should consider giving students opportunities to organise and manage information so that files, notes and documents can be found again later."
  quote: full   # the issuer's statement is in `source` (D-std-0014)
  audience: both
  subjects: inherited
- id: qaa/education-studies-2025/3.10.b17
  locator: { number: "3.10.b17", headingPath: ["Content, structure and delivery", "Transversal curriculum"] }
  span: { start: 40835, end: 40924 }
  source: "take initiative in appropriate contexts, aware of their own responsibilities and autonomy"
  stem: "3.10"
  statementType: expectation
  rung: none
  force: should
  level: fheq:6
  appliesTo: "Education Studies courses and their students"
  addressee: both
  verbs: ["take"]
  about: "initiative and autonomy"
  themes: [none]
  domain: generic-skill
  award: ["bachelor's with honours"]
  gradeOf: none
  paraphrase: "Course teams should consider giving students opportunities to use initiative where it fits, knowing the limits of their role and their freedom to act."
  quote: full   # the issuer's statement is in `source` (D-std-0014)
  audience: both
  subjects: inherited
- id: qaa/education-studies-2025/3.10.b18
  locator: { number: "3.10.b18", headingPath: ["Content, structure and delivery", "Transversal curriculum"] }
  span: { start: 40927, end: 40982 }
  source: "take responsibility, with accountability and leadership"
  stem: "3.10"
  statementType: expectation
  rung: none
  force: should
  level: fheq:6
  appliesTo: "Education Studies courses and their students"
  addressee: both
  verbs: ["take"]
  about: "responsibility and leadership"
  themes: [none]
  domain: generic-skill
  award: ["bachelor's with honours"]
  gradeOf: none
  paraphrase: "Course teams should consider giving students opportunities to accept responsibility, answer for their actions and give a lead."
  quote: full   # the issuer's statement is in `source` (D-std-0014)
  audience: both
  subjects: inherited
- id: qaa/education-studies-2025/3.10.b19
  locator: { number: "3.10.b19", headingPath: ["Content, structure and delivery", "Transversal curriculum"] }
  span: { start: 40985, end: 41105 }
  source: "use critical questions in practice, developing their own line of questioning to make critical judgements and evaluations"
  stem: "3.10"
  statementType: expectation
  rung: none
  force: should
  level: fheq:6
  appliesTo: "Education Studies courses and their students"
  addressee: both
  verbs: ["use", "developing", "make"]
  about: "critical questioning in practice"
  themes: [none]
  domain: generic-skill
  award: ["bachelor's with honours"]
  gradeOf: none
  paraphrase: "Course teams should consider giving students opportunities to ask critical questions in practice, building their own line of enquiry to reach critical judgements."
  quote: full   # the issuer's statement is in `source` (D-std-0014)
  audience: both
  subjects: inherited
- id: qaa/education-studies-2025/3.10.b20
  locator: { number: "3.10.b20", headingPath: ["Content, structure and delivery", "Transversal curriculum"] }
  span: { start: 41108, end: 41177 }
  source: "use digital and social media technologies in the appropriate contexts"
  stem: "3.10"
  statementType: expectation
  rung: none
  force: should
  level: fheq:6
  appliesTo: "Education Studies courses and their students"
  addressee: both
  verbs: ["use"]
  about: "digital and social media"
  themes: [none]
  domain: generic-skill
  award: ["bachelor's with honours"]
  gradeOf: none
  paraphrase: "Course teams should consider giving students opportunities to use digital and social media where suitable."
  quote: full   # the issuer's statement is in `source` (D-std-0014)
  audience: both
  subjects: inherited
- id: qaa/education-studies-2025/3.10.b21
  locator: { number: "3.10.b21", headingPath: ["Content, structure and delivery", "Transversal curriculum"] }
  span: { start: 41180, end: 41248 }
  source: "use evidence-informed practices to develop an informed point of view"
  stem: "3.10"
  statementType: expectation
  rung: none
  force: should
  level: fheq:6
  appliesTo: "Education Studies courses and their students"
  addressee: both
  verbs: ["use", "develop"]
  about: "evidence-informed views"
  themes: [none]
  domain: generic-skill
  award: ["bachelor's with honours"]
  gradeOf: none
  paraphrase: "Course teams should consider giving students opportunities to draw on evidence-informed practice to form a reasoned view."
  quote: full   # the issuer's statement is in `source` (D-std-0014)
  audience: both
  subjects: inherited
- id: qaa/education-studies-2025/3.10.b22
  locator: { number: "3.10.b22", headingPath: ["Content, structure and delivery", "Transversal curriculum"] }
  span: { start: 41251, end: 41291 }
  source: "utilise AI critically, in an ethical way"
  stem: "3.10"
  statementType: expectation
  rung: none
  force: should
  level: fheq:6
  appliesTo: "Education Studies courses and their students"
  addressee: both
  verbs: ["utilise"]
  about: "critical and ethical use of AI"
  themes: [none]
  domain: generic-skill
  award: ["bachelor's with honours"]
  gradeOf: none
  paraphrase: "Course teams should consider giving students opportunities to use AI critically and ethically."
  quote: full   # the issuer's statement is in `source` (D-std-0014)
  audience: both
  subjects: inherited
- id: qaa/education-studies-2025/3.10.b23
  locator: { number: "3.10.b23", headingPath: ["Content, structure and delivery", "Transversal curriculum"] }
  span: { start: 41294, end: 41327 }
  source: "work collaboratively with others."
  stem: "3.10"
  statementType: expectation
  rung: none
  force: should
  level: fheq:6
  appliesTo: "Education Studies courses and their students"
  addressee: both
  verbs: ["work"]
  about: "collaboration"
  themes: [none]
  domain: generic-skill
  award: ["bachelor's with honours"]
  gradeOf: none
  paraphrase: "Course teams should consider giving students opportunities to work with others collaboratively."
  quote: full   # the issuer's statement is in `source` (D-std-0014)
  audience: both
  subjects: inherited
- id: qaa/education-studies-2025/3.16
  locator: { number: "3.16", headingPath: ["Content, structure and delivery", "Assessment"] }
  span: { start: 43227, end: 43492 }
  source: "3.16 The assessment strategy for Education Studies programmes reflects the broad range of skills, knowledges and values reflected in this S tatement. Assessment should be clearly aligned with the desired outcomes, learning objectives or competencies being assessed."
  stem: none
  statementType: requirement
  rung: none
  force: should
  level: none
  appliesTo: "Education Studies courses and their teams"
  addressee: provider
  verbs: ["aligned"]
  about: "aligning assessment with outcomes"
  themes: [none]
  domain: none
  award: ["none"]
  gradeOf: none
  paraphrase: "The assessment strategy mirrors the wide range of skills, knowledge and values the statement sets out, and assessment should line up clearly with the outcomes, objectives or competencies it tests."
  quote: full   # the issuer's statement is in `source` (D-std-0014)
  audience: practitioner
  subjects: inherited
- id: qaa/education-studies-2025/4.1
  locator: { number: "4.1", headingPath: ["Benchmark standards", "Introduction"] }
  span: { start: 46637, end: 47303 }
  source: "4.1 The following benchmark standards are defined for students studying a single honours or master's degree in Education Studies. It is understood that students may follow an Education Studies course in a wide range of academic and professional contexts, including, for example: a joint honours course; courses with 'major' and 'minor' studies; or a professionally focused honours course. No judgement is made about how much subject knowledge and understanding may be required in a joint honours course. Where students study Education Studies as a part of a degree course, higher education providers clarify the extent to which the benchmark standards should be met."
  stem: none
  statementType: requirement
  rung: none
  force: should
  level: fheq:6
  appliesTo: "Education Studies courses and their teams"
  addressee: provider
  verbs: ["defined", "clarify", "met"]
  about: "who the standards apply to; joint degrees"
  themes: [none]
  domain: none
  award: ["bachelor's with honours", "master's"]
  gradeOf: none
  paraphrase: "The standards are set for students taking Education Studies as a single honours or master's degree; the subject is also studied in joint, major and minor and professionally focused courses, and no view is taken on how much subject knowledge a joint course needs; where Education Studies is one part of a degree, the institution makes clear how far the standards should be met."
  quote: full   # the issuer's statement is in `source` (D-std-0014)
  audience: practitioner
  subjects: inherited
- id: qaa/education-studies-2025/4.3
  locator: { number: "4.3", headingPath: ["Benchmark standards", "Introduction"] }
  span: { start: 48163, end: 49056 }
  source: "4.3 In the tables below, the threshold standards specify performance for a student successfully completing a course leading to an undergraduate honours award or master's degree. The threshold standards set the expectation that, as a minimum, all students are able to demonstrate achievement in all of these areas. The vast majority of students will perform significantly better than the minimum threshold standards. Each higher education provider has its own method of determining what appropriate evidence of this achievement will be and should refer to Annex D in The Frameworks for Higher Education Qualifications of UK Degree-Awarding Bodies. The tables also describe expected levels of typical and excellent performance at undergraduate level. Furthermore, a student in Education Studies may demonstrate achievement of these outcomes at different levels and to a greater or lesser extent."
  stem: none
  statementType: requirement
  rung: none
  force: should
  level: fheq:6
  appliesTo: "Education Studies courses and their teams"
  addressee: provider
  verbs: ["specify", "demonstrate", "refer", "describe"]
  about: "the threshold as minimum; evidence by Annex D"
  themes: [none]
  domain: none
  award: ["bachelor's with honours", "master's"]
  gradeOf: none
  paraphrase: "The threshold standards set the least every student completing an honours or master's course can show in each area, and most will do much better; each institution decides what evidence shows this and should refer to Annex D of the Frameworks for Higher Education Qualifications; the tables also describe typical and excellent undergraduate performance, and a student may reach the outcomes at different levels and to differing degrees."
  quote: full   # the issuer's statement is in `source` (D-std-0014)
  audience: practitioner
  subjects: inherited
- id: qaa/education-studies-2025/4.5
  locator: { number: "4.5", headingPath: ["Benchmark standards", "Introduction"] }
  span: { start: 49520, end: 50023 }
  source: "4.5 Please note that the minimum threshold, typical and excellent standards are not intended to specify universal competence standards for a discipline. If a provider chooses to develop competence standards ( as defined by the Equality Act 2010) as part of a programme specification, these can be informed by the relevant Subject B enchmark Statement along with any PSRB requirements. In these circumstances providers should follow the most recent guidance from the Equality and Human Rights Commission."
  stem: none
  statementType: requirement
  rung: none
  force: should
  level: none
  appliesTo: "Education Studies courses and their teams"
  addressee: provider
  verbs: ["follow", "informed"]
  about: "competence standards and the Equality Act"
  themes: [none]
  domain: none
  award: ["none"]
  gradeOf: none
  paraphrase: "The minimum threshold, typical and excellent standards do not set universal competence standards for the discipline; a provider that writes competence standards (in the Equality Act 2010 sense) into a programme specification may draw on the statement and any PSRB requirements, and should then follow the latest Equality and Human Rights Commission guidance."
  quote: full   # the issuer's statement is in `source` (D-std-0014)
  audience: practitioner
  subjects: inherited
- id: qaa/education-studies-2025/4.5.b1
  locator: { number: "4.5.b1", headingPath: ["Benchmark standards", "Introduction"] }
  span: { start: 50183, end: 50321 }
  source: "The student can demonstrate a coherent understanding of significant theories, concepts and ideas relating to education in its widest sense"
  stem: "4.5"
  statementType: threshold
  rung: threshold
  force: threshold
  level: fheq:6
  appliesTo: "honours students at the threshold standard"
  addressee: learner
  verbs: ["demonstrate"]
  about: "theories, concepts and ideas about education"
  themes: [none]
  domain: knowledge
  award: ["bachelor's with honours"]
  gradeOf: none
  paraphrase: "As the minimum for an honours degree in Education Studies, the student can show a coherent grasp of the major theories, concepts and ideas about education, taken in its broadest sense."
  quote: full   # the issuer's statement is in `source` (D-std-0014)
  audience: both
  subjects: inherited
- id: qaa/education-studies-2025/4.5.b1.excellent
  locator: { number: "4.5.b1.excellent", headingPath: ["Benchmark standards", "Introduction"] }
  span: { start: 50456, end: 50628 }
  source: "The student can demonstrate deep understanding of significant theories, concepts and ideas relating to education in its widest sense, informed by the forefront of the field"
  stem: "4.5"
  statementType: excellent
  rung: excellent
  force: will
  level: fheq:6
  appliesTo: "honours students at the excellent standard"
  addressee: learner
  verbs: ["demonstrate"]
  about: "theories, concepts and ideas about education"
  themes: [none]
  domain: knowledge
  award: ["bachelor's with honours"]
  gradeOf: { statement: qaa/education-studies-2025/4.5.b1.typical, basis: stated }
  paraphrase: "At the excellent level of honours performance, the student can show a deep grasp of the major theories, concepts and ideas about education, taken in its broadest sense, drawing on the leading edge of the field."
  quote: full   # the issuer's statement is in `source` (D-std-0014)
  audience: both
  subjects: inherited
- id: qaa/education-studies-2025/4.5.b1.masters
  locator: { number: "4.5.b1.masters", headingPath: ["Benchmark standards", "Introduction"] }
  span: { start: 50629, end: 50815 }
  source: "The student can demonstrate systematic understanding of significant theories, concepts and ideas relating to education in its widest sense, much of which is at the forefront of the field"
  stem: "4.5"
  statementType: threshold
  rung: threshold
  force: will
  level: fheq:7
  appliesTo: "students completing a master's degree in Education Studies"
  addressee: learner
  verbs: ["demonstrate"]
  about: "theories, concepts and ideas about education"
  themes: [none]
  domain: knowledge
  award: ["master's"]
  gradeOf: none
  paraphrase: "For a master's degree in Education Studies, the student can show a systematic grasp of the major theories, concepts and ideas about education, taken in its broadest sense, much of it from the leading edge of the field."
  quote: full   # the issuer's statement is in `source` (D-std-0014)
  audience: both
  subjects: inherited
- id: qaa/education-studies-2025/4.5.b1.typical
  locator: { number: "4.5.b1.typical", headingPath: ["Benchmark standards", "Introduction"] }
  span: { start: 50322, end: 50455 }
  source: "The student can demonstrate sound understanding of significant theories, concepts and ideas relating to education in its widest sense"
  stem: "4.5"
  statementType: typical
  rung: typical
  force: will
  level: fheq:6
  appliesTo: "honours students at the typical standard"
  addressee: learner
  verbs: ["demonstrate"]
  about: "theories, concepts and ideas about education"
  themes: [none]
  domain: knowledge
  award: ["bachelor's with honours"]
  gradeOf: { statement: qaa/education-studies-2025/4.5.b1, basis: stated }
  paraphrase: "At the typical level of honours performance, the student can show a sound grasp of the major theories, concepts and ideas about education, taken in its broadest sense."
  quote: full   # the issuer's statement is in `source` (D-std-0014)
  audience: both
  subjects: inherited
- id: qaa/education-studies-2025/4.5.b2
  locator: { number: "4.5.b2", headingPath: ["Benchmark standards", "Introduction"] }
  span: { start: 50835, end: 50969 }
  source: "The student can demonstrate a coherent understanding of the uncertainties, ambiguities and limits of knowledge and theory in the field"
  stem: "4.5"
  statementType: threshold
  rung: threshold
  force: threshold
  level: fheq:6
  appliesTo: "honours students at the threshold standard"
  addressee: learner
  verbs: ["demonstrate"]
  about: "the uncertainty and limits of knowledge in education"
  themes: [none]
  domain: understanding
  award: ["bachelor's with honours"]
  gradeOf: none
  paraphrase: "As the minimum for an honours degree in Education Studies, the student can show a coherent grasp of where knowledge and theory in education are uncertain, ambiguous or limited."
  quote: full   # the issuer's statement is in `source` (D-std-0014)
  audience: both
  subjects: inherited
- id: qaa/education-studies-2025/4.5.b2.excellent
  locator: { number: "4.5.b2.excellent", headingPath: ["Benchmark standards", "Introduction"] }
  span: { start: 51100, end: 51228 }
  source: "The student can demonstrate deep understanding of the uncertainties, ambiguities and limits of knowledge and theory in the field"
  stem: "4.5"
  statementType: excellent
  rung: excellent
  force: will
  level: fheq:6
  appliesTo: "honours students at the excellent standard"
  addressee: learner
  verbs: ["demonstrate"]
  about: "the uncertainty and limits of knowledge in education"
  themes: [none]
  domain: understanding
  award: ["bachelor's with honours"]
  gradeOf: { statement: qaa/education-studies-2025/4.5.b2.typical, basis: stated }
  paraphrase: "At the excellent level of honours performance, the student can show a deep grasp of where knowledge and theory in education are uncertain, ambiguous or limited."
  quote: full   # the issuer's statement is in `source` (D-std-0014)
  audience: both
  subjects: inherited
- id: qaa/education-studies-2025/4.5.b2.masters
  locator: { number: "4.5.b2.masters", headingPath: ["Benchmark standards", "Introduction"] }
  span: { start: 51229, end: 51315 }
  source: "The student can critically evaluate knowledge and theory at the forefront of the field"
  stem: "4.5"
  statementType: threshold
  rung: threshold
  force: will
  level: fheq:7
  appliesTo: "students completing a master's degree in Education Studies"
  addressee: learner
  verbs: ["evaluate"]
  about: "the uncertainty and limits of knowledge in education"
  themes: [none]
  domain: understanding
  award: ["master's"]
  gradeOf: none
  paraphrase: "For a master's degree in Education Studies, the student can judge critically the knowledge and theory at the leading edge of the field."
  quote: full   # the issuer's statement is in `source` (D-std-0014)
  audience: both
  subjects: inherited
- id: qaa/education-studies-2025/4.5.b2.typical
  locator: { number: "4.5.b2.typical", headingPath: ["Benchmark standards", "Introduction"] }
  span: { start: 50970, end: 51099 }
  source: "The student can demonstrate sound understanding of the uncertainties, ambiguities and limits of knowledge and theory in the field"
  stem: "4.5"
  statementType: typical
  rung: typical
  force: will
  level: fheq:6
  appliesTo: "honours students at the typical standard"
  addressee: learner
  verbs: ["demonstrate"]
  about: "the uncertainty and limits of knowledge in education"
  themes: [none]
  domain: understanding
  award: ["bachelor's with honours"]
  gradeOf: { statement: qaa/education-studies-2025/4.5.b2, basis: stated }
  paraphrase: "At the typical level of honours performance, the student can show a sound grasp of where knowledge and theory in education are uncertain, ambiguous or limited."
  quote: full   # the issuer's statement is in `source` (D-std-0014)
  audience: both
  subjects: inherited
- id: qaa/education-studies-2025/4.5.b3
  locator: { number: "4.5.b3", headingPath: ["Benchmark standards", "Introduction"] }
  span: { start: 51336, end: 51440 }
  source: "The student can identify critical questions relating to education using bodies of knowledge and evidence"
  stem: "4.5"
  statementType: threshold
  rung: threshold
  force: threshold
  level: fheq:6
  appliesTo: "honours students at the threshold standard"
  addressee: learner
  verbs: ["identify"]
  about: "critical questions and arguments about education"
  themes: [none]
  domain: subject-skill
  award: ["bachelor's with honours"]
  gradeOf: none
  paraphrase: "As the minimum for an honours degree in Education Studies, the student can pick out critical questions about education by drawing on knowledge and evidence."
  quote: full   # the issuer's statement is in `source` (D-std-0014)
  audience: both
  subjects: inherited
- id: qaa/education-studies-2025/4.5.b3.excellent
  locator: { number: "4.5.b3.excellent", headingPath: ["Benchmark standards", "Introduction"] }
  span: { start: 51570, end: 51709 }
  source: "The student can devise and sustain critical arguments relating to education using multiple bodies of knowledge and evidence in complex ways"
  stem: "4.5"
  statementType: excellent
  rung: excellent
  force: will
  level: fheq:6
  appliesTo: "honours students at the excellent standard"
  addressee: learner
  verbs: ["devise", "sustain"]
  about: "critical questions and arguments about education"
  themes: [none]
  domain: subject-skill
  award: ["bachelor's with honours"]
  gradeOf: { statement: qaa/education-studies-2025/4.5.b3.typical, basis: stated }
  paraphrase: "At the excellent level of honours performance, the student can build and keep up critical arguments about education that draw on several bodies of knowledge and evidence in complex ways."
  quote: full   # the issuer's statement is in `source` (D-std-0014)
  audience: both
  subjects: inherited
- id: qaa/education-studies-2025/4.5.b3.masters
  locator: { number: "4.5.b3.masters", headingPath: ["Benchmark standards", "Introduction"] }
  span: { start: 51710, end: 51801 }
  source: "The student can synthesize complex bodies of knowledge and evidence to produce new insights"
  stem: "4.5"
  statementType: threshold
  rung: threshold
  force: will
  level: fheq:7
  appliesTo: "students completing a master's degree in Education Studies"
  addressee: learner
  verbs: ["synthesize"]
  about: "critical questions and arguments about education"
  themes: [none]
  domain: subject-skill
  award: ["master's"]
  gradeOf: none
  paraphrase: "For a master's degree in Education Studies, the student can bring complex knowledge and evidence together to reach new insights."
  quote: full   # the issuer's statement is in `source` (D-std-0014)
  audience: both
  subjects: inherited
- id: qaa/education-studies-2025/4.5.b3.typical
  locator: { number: "4.5.b3.typical", headingPath: ["Benchmark standards", "Introduction"] }
  span: { start: 51441, end: 51569 }
  source: "The student can devise critical arguments relating to education using multiple bodies of knowledge and evidence in detailed ways"
  stem: "4.5"
  statementType: typical
  rung: typical
  force: will
  level: fheq:6
  appliesTo: "honours students at the typical standard"
  addressee: learner
  verbs: ["devise"]
  about: "critical questions and arguments about education"
  themes: [none]
  domain: subject-skill
  award: ["bachelor's with honours"]
  gradeOf: { statement: qaa/education-studies-2025/4.5.b3, basis: stated }
  paraphrase: "At the typical level of honours performance, the student can build critical arguments about education that draw in detail on several bodies of knowledge and evidence."
  quote: full   # the issuer's statement is in `source` (D-std-0014)
  audience: both
  subjects: inherited
- id: qaa/education-studies-2025/4.5.b4
  locator: { number: "4.5.b4", headingPath: ["Benchmark standards", "Introduction"] }
  span: { start: 51814, end: 51911 }
  source: "The student can apply significant theories, concepts and ideas to real- world issues in education"
  stem: "4.5"
  statementType: threshold
  rung: threshold
  force: threshold
  level: fheq:6
  appliesTo: "honours students at the threshold standard"
  addressee: learner
  verbs: ["apply"]
  about: "applying theory to real problems in education"
  themes: [none]
  domain: subject-skill
  award: ["bachelor's with honours"]
  gradeOf: none
  paraphrase: "As the minimum for an honours degree in Education Studies, the student can use major theories, concepts and ideas on real problems in education."
  quote: full   # the issuer's statement is in `source` (D-std-0014)
  audience: both
  subjects: inherited
- id: qaa/education-studies-2025/4.5.b4.excellent
  locator: { number: "4.5.b4.excellent", headingPath: ["Benchmark standards", "Introduction"] }
  span: { start: 52026, end: 52138 }
  source: "The student can apply significant theories, concepts and ideas in complex ways to real-world issues in education"
  stem: "4.5"
  statementType: excellent
  rung: excellent
  force: will
  level: fheq:6
  appliesTo: "honours students at the excellent standard"
  addressee: learner
  verbs: ["apply"]
  about: "applying theory to real problems in education"
  themes: [none]
  domain: subject-skill
  award: ["bachelor's with honours"]
  gradeOf: { statement: qaa/education-studies-2025/4.5.b4.typical, basis: stated }
  paraphrase: "At the excellent level of honours performance, the student can use major theories, concepts and ideas on real problems in education, in complex ways."
  quote: full   # the issuer's statement is in `source` (D-std-0014)
  audience: both
  subjects: inherited
- id: qaa/education-studies-2025/4.5.b4.masters
  locator: { number: "4.5.b4.masters", headingPath: ["Benchmark standards", "Introduction"] }
  span: { start: 52139, end: 52274 }
  source: "The student can demonstrate originality in the application of significant theories and ideas to complex real- world issues in education"
  stem: "4.5"
  statementType: threshold
  rung: threshold
  force: will
  level: fheq:7
  appliesTo: "students completing a master's degree in Education Studies"
  addressee: learner
  verbs: ["demonstrate"]
  about: "applying theory to real problems in education"
  themes: [none]
  domain: subject-skill
  award: ["master's"]
  gradeOf: none
  paraphrase: "For a master's degree in Education Studies, the student can show originality in using major theories and ideas on complex real problems in education."
  quote: full   # the issuer's statement is in `source` (D-std-0014)
  audience: both
  subjects: inherited
- id: qaa/education-studies-2025/4.5.b4.typical
  locator: { number: "4.5.b4.typical", headingPath: ["Benchmark standards", "Introduction"] }
  span: { start: 51912, end: 52025 }
  source: "The student can apply significant theories, concepts and ideas in detailed ways to real-world issues in education"
  stem: "4.5"
  statementType: typical
  rung: typical
  force: will
  level: fheq:6
  appliesTo: "honours students at the typical standard"
  addressee: learner
  verbs: ["apply"]
  about: "applying theory to real problems in education"
  themes: [none]
  domain: subject-skill
  award: ["bachelor's with honours"]
  gradeOf: { statement: qaa/education-studies-2025/4.5.b4, basis: stated }
  paraphrase: "At the typical level of honours performance, the student can use major theories, concepts and ideas on real problems in education, in detail."
  quote: full   # the issuer's statement is in `source` (D-std-0014)
  audience: both
  subjects: inherited
- id: qaa/education-studies-2025/4.5.b5
  locator: { number: "4.5.b5", headingPath: ["Benchmark standards", "Introduction"] }
  span: { start: 52402, end: 52521 }
  source: "The student can demonstrate a coherent understanding of ethical tensions, dilemmas and challenges surrounding education"
  stem: "4.5"
  statementType: threshold
  rung: threshold
  force: threshold
  level: fheq:6
  appliesTo: "honours students at the threshold standard"
  addressee: learner
  verbs: ["demonstrate"]
  about: "ethical tensions in education"
  themes: [none]
  domain: understanding
  award: ["bachelor's with honours"]
  gradeOf: none
  paraphrase: "As the minimum for an honours degree in Education Studies, the student can show a coherent grasp of the ethical dilemmas, tensions and challenges in education."
  quote: full   # the issuer's statement is in `source` (D-std-0014)
  audience: both
  subjects: inherited
- id: qaa/education-studies-2025/4.5.b5.excellent
  locator: { number: "4.5.b5.excellent", headingPath: ["Benchmark standards", "Introduction"] }
  span: { start: 52637, end: 52750 }
  source: "The student can demonstrate deep understanding of ethical tensions, dilemmas and challenges surrounding education"
  stem: "4.5"
  statementType: excellent
  rung: excellent
  force: will
  level: fheq:6
  appliesTo: "honours students at the excellent standard"
  addressee: learner
  verbs: ["demonstrate"]
  about: "ethical tensions in education"
  themes: [none]
  domain: understanding
  award: ["bachelor's with honours"]
  gradeOf: { statement: qaa/education-studies-2025/4.5.b5.typical, basis: stated }
  paraphrase: "At the excellent level of honours performance, the student can show a deep grasp of the ethical dilemmas, tensions and challenges in education."
  quote: full   # the issuer's statement is in `source` (D-std-0014)
  audience: both
  subjects: inherited
- id: qaa/education-studies-2025/4.5.b5.masters
  locator: { number: "4.5.b5.masters", headingPath: ["Benchmark standards", "Introduction"] }
  span: { start: 52751, end: 52888 }
  source: "The student can demonstrate originality in the analysis and resolution of ethical tensions, dilemmas and challenges surrounding education"
  stem: "4.5"
  statementType: threshold
  rung: threshold
  force: will
  level: fheq:7
  appliesTo: "students completing a master's degree in Education Studies"
  addressee: learner
  verbs: ["demonstrate"]
  about: "ethical tensions in education"
  themes: [none]
  domain: understanding
  award: ["master's"]
  gradeOf: none
  paraphrase: "For a master's degree in Education Studies, the student can show originality in analysing and resolving ethical dilemmas, tensions and challenges in education."
  quote: full   # the issuer's statement is in `source` (D-std-0014)
  audience: both
  subjects: inherited
- id: qaa/education-studies-2025/4.5.b5.typical
  locator: { number: "4.5.b5.typical", headingPath: ["Benchmark standards", "Introduction"] }
  span: { start: 52522, end: 52636 }
  source: "The student can demonstrate sound understanding of ethical tensions, dilemmas and challenges surrounding education"
  stem: "4.5"
  statementType: typical
  rung: typical
  force: will
  level: fheq:6
  appliesTo: "honours students at the typical standard"
  addressee: learner
  verbs: ["demonstrate"]
  about: "ethical tensions in education"
  themes: [none]
  domain: understanding
  award: ["bachelor's with honours"]
  gradeOf: { statement: qaa/education-studies-2025/4.5.b5, basis: stated }
  paraphrase: "At the typical level of honours performance, the student can show a sound grasp of the ethical dilemmas, tensions and challenges in education."
  quote: full   # the issuer's statement is in `source` (D-std-0014)
  audience: both
  subjects: inherited
- id: qaa/education-studies-2025/4.5.b6
  locator: { number: "4.5.b6", headingPath: ["Benchmark standards", "Introduction"] }
  span: { start: 52918, end: 53022 }
  source: "The student can recognise the need to assess their own skills and to reflect on them for future learning"
  stem: "4.5"
  statementType: threshold
  rung: threshold
  force: threshold
  level: fheq:6
  appliesTo: "honours students at the threshold standard"
  addressee: learner
  verbs: ["recognise", "assess", "reflect"]
  about: "evaluating own learning skills"
  themes: [none]
  domain: subject-skill
  award: ["bachelor's with honours"]
  gradeOf: none
  paraphrase: "As the minimum for an honours degree in Education Studies, the student can accept the value of weighing up their own skills and reflecting on them to guide later learning."
  quote: full   # the issuer's statement is in `source` (D-std-0014)
  audience: both
  subjects: inherited
- id: qaa/education-studies-2025/4.5.b6.excellent
  locator: { number: "4.5.b6.excellent", headingPath: ["Benchmark standards", "Introduction"] }
  span: { start: 53171, end: 53324 }
  source: "The student shows sophistication in taking charge of their own learning, reflect on personal strengths and weaknesses for the purposes of future learning"
  stem: "4.5"
  statementType: excellent
  rung: excellent
  force: will
  level: fheq:6
  appliesTo: "honours students at the excellent standard"
  addressee: learner
  verbs: ["taking", "reflect"]
  about: "evaluating own learning skills"
  themes: [none]
  domain: subject-skill
  award: ["bachelor's with honours"]
  gradeOf: { statement: qaa/education-studies-2025/4.5.b6.typical, basis: stated }
  paraphrase: "At the excellent level of honours performance, the student can take control of their own learning with sophistication, reflecting on their strengths and weaknesses to guide later learning."
  quote: full   # the issuer's statement is in `source` (D-std-0014)
  audience: both
  subjects: inherited
- id: qaa/education-studies-2025/4.5.b6.masters
  locator: { number: "4.5.b6.masters", headingPath: ["Benchmark standards", "Introduction"] }
  span: { start: 53325, end: 53492 }
  source: "The student shows sophistication in leading their own learning, evaluating and being reflexive of personal strengths and weaknesses for the purposes of future learning"
  stem: "4.5"
  statementType: threshold
  rung: threshold
  force: will
  level: fheq:7
  appliesTo: "students completing a master's degree in Education Studies"
  addressee: learner
  verbs: ["leading", "evaluating"]
  about: "evaluating own learning skills"
  themes: [none]
  domain: subject-skill
  award: ["master's"]
  gradeOf: none
  paraphrase: "For a master's degree in Education Studies, the student can lead their own learning with sophistication, judging their strengths and weaknesses reflexively to guide later learning."
  quote: full   # the issuer's statement is in `source` (D-std-0014)
  audience: both
  subjects: inherited
- id: qaa/education-studies-2025/4.5.b6.typical
  locator: { number: "4.5.b6.typical", headingPath: ["Benchmark standards", "Introduction"] }
  span: { start: 53023, end: 53170 }
  source: "The student can take charge of their own learning and reflect on and evaluate personal strengths and weaknesses for the purposes of future learning"
  stem: "4.5"
  statementType: typical
  rung: typical
  force: will
  level: fheq:6
  appliesTo: "honours students at the typical standard"
  addressee: learner
  verbs: ["take", "reflect", "evaluate"]
  about: "evaluating own learning skills"
  themes: [none]
  domain: subject-skill
  award: ["bachelor's with honours"]
  gradeOf: { statement: qaa/education-studies-2025/4.5.b6, basis: stated }
  paraphrase: "At the typical level of honours performance, the student can take control of their own learning, reflecting on and judging their personal strengths and weaknesses to guide later learning."
  quote: full   # the issuer's statement is in `source` (D-std-0014)
  audience: both
  subjects: inherited
- id: qaa/education-studies-2025/4.5.b7
  locator: { number: "4.5.b7", headingPath: ["Benchmark standards", "Introduction"] }
  span: { start: 53506, end: 53633 }
  source: "The student can demonstrate and apply knowledge of the methods required for systematic study and research relative to education"
  stem: "4.5"
  statementType: threshold
  rung: threshold
  force: threshold
  level: fheq:6
  appliesTo: "honours students at the threshold standard"
  addressee: learner
  verbs: ["demonstrate", "apply"]
  about: "methods for systematic study and research"
  themes: [none]
  domain: subject-skill
  award: ["bachelor's with honours"]
  gradeOf: none
  paraphrase: "As the minimum for an honours degree in Education Studies, the student can know and use the methods that systematic study and research in education call for."
  quote: full   # the issuer's statement is in `source` (D-std-0014)
  audience: both
  subjects: inherited
- id: qaa/education-studies-2025/4.5.b7.excellent
  locator: { number: "4.5.b7.excellent", headingPath: ["Benchmark standards", "Introduction"] }
  span: { start: 53840, end: 54076 }
  source: "The student can demonstrate and apply a deep working knowledge of the methods required for systematic study and research relative to education. The student can demonstrate improvement resulting from their self- evaluation of such skills"
  stem: "4.5"
  statementType: excellent
  rung: excellent
  force: will
  level: fheq:6
  appliesTo: "honours students at the excellent standard"
  addressee: learner
  verbs: ["demonstrate", "apply"]
  about: "methods for systematic study and research"
  themes: [none]
  domain: subject-skill
  award: ["bachelor's with honours"]
  gradeOf: { statement: qaa/education-studies-2025/4.5.b7.typical, basis: stated }
  paraphrase: "At the excellent level of honours performance, the student can know and use, with a deep working grasp, the methods for systematic study and research in education, and show that judging their own skills has improved them."
  quote: full   # the issuer's statement is in `source` (D-std-0014)
  audience: both
  subjects: inherited
- id: qaa/education-studies-2025/4.5.b7.masters
  locator: { number: "4.5.b7.masters", headingPath: ["Benchmark standards", "Introduction"] }
  span: { start: 54077, end: 54241 }
  source: "The student can demonstrate and apply a critically reflexive evaluation of the methods required for systematic study, research and application relative to education"
  stem: "4.5"
  statementType: threshold
  rung: threshold
  force: will
  level: fheq:7
  appliesTo: "students completing a master's degree in Education Studies"
  addressee: learner
  verbs: ["demonstrate", "apply"]
  about: "methods for systematic study and research"
  themes: [none]
  domain: subject-skill
  award: ["master's"]
  gradeOf: none
  paraphrase: "For a master's degree in Education Studies, the student can judge in a critically reflexive way, and use, the methods for systematic study, research and application in education."
  quote: full   # the issuer's statement is in `source` (D-std-0014)
  audience: both
  subjects: inherited
- id: qaa/education-studies-2025/4.5.b7.typical
  locator: { number: "4.5.b7.typical", headingPath: ["Benchmark standards", "Introduction"] }
  span: { start: 53634, end: 53839 }
  source: "The student can demonstrate and apply a sound working knowledge of the methods required for systematic study and research relative to education. The student can evaluate their own strengths and weaknesses."
  stem: "4.5"
  statementType: typical
  rung: typical
  force: will
  level: fheq:6
  appliesTo: "honours students at the typical standard"
  addressee: learner
  verbs: ["demonstrate", "apply", "evaluate"]
  about: "methods for systematic study and research"
  themes: [none]
  domain: subject-skill
  award: ["bachelor's with honours"]
  gradeOf: { statement: qaa/education-studies-2025/4.5.b7, basis: stated }
  paraphrase: "At the typical level of honours performance, the student can know and use, with a sound working grasp, the methods for systematic study and research in education, and judge their own strengths and weaknesses."
  quote: full   # the issuer's statement is in `source` (D-std-0014)
  audience: both
  subjects: inherited
- id: qaa/education-studies-2025/4.5.b8
  locator: { number: "4.5.b8", headingPath: ["Benchmark standards", "Introduction"] }
  span: { start: 54253, end: 54337 }
  source: "The student can demonstrate the use of creative approaches in the study of education"
  stem: "4.5"
  statementType: threshold
  rung: threshold
  force: threshold
  level: fheq:6
  appliesTo: "honours students at the threshold standard"
  addressee: learner
  verbs: ["demonstrate"]
  about: "creative approaches to studying education"
  themes: [none]
  domain: subject-skill
  award: ["bachelor's with honours"]
  gradeOf: none
  paraphrase: "As the minimum for an honours degree in Education Studies, the student can take creative approaches to studying education."
  quote: full   # the issuer's statement is in `source` (D-std-0014)
  audience: both
  subjects: inherited
- id: qaa/education-studies-2025/4.5.b8.excellent
  locator: { number: "4.5.b8.excellent", headingPath: ["Benchmark standards", "Introduction"] }
  span: { start: 54433, end: 54524 }
  source: "The student can demonstrate the use of highly creative approaches to the study of education"
  stem: "4.5"
  statementType: excellent
  rung: excellent
  force: will
  level: fheq:6
  appliesTo: "honours students at the excellent standard"
  addressee: learner
  verbs: ["demonstrate"]
  about: "creative approaches to studying education"
  themes: [none]
  domain: subject-skill
  award: ["bachelor's with honours"]
  gradeOf: { statement: qaa/education-studies-2025/4.5.b8.typical, basis: stated }
  paraphrase: "At the excellent level of honours performance, the student can take highly creative approaches to studying education."
  quote: full   # the issuer's statement is in `source` (D-std-0014)
  audience: both
  subjects: inherited
- id: qaa/education-studies-2025/4.5.b8.masters
  locator: { number: "4.5.b8.masters", headingPath: ["Benchmark standards", "Introduction"] }
  span: { start: 54525, end: 54629 }
  source: "The student can demonstrate the use of highly creative and original approaches in the study of education"
  stem: "4.5"
  statementType: threshold
  rung: threshold
  force: will
  level: fheq:7
  appliesTo: "students completing a master's degree in Education Studies"
  addressee: learner
  verbs: ["demonstrate"]
  about: "creative approaches to studying education"
  themes: [none]
  domain: subject-skill
  award: ["master's"]
  gradeOf: none
  paraphrase: "For a master's degree in Education Studies, the student can take highly creative and original approaches to studying education."
  quote: full   # the issuer's statement is in `source` (D-std-0014)
  audience: both
  subjects: inherited
- id: qaa/education-studies-2025/4.5.b8.typical
  locator: { number: "4.5.b8.typical", headingPath: ["Benchmark standards", "Introduction"] }
  span: { start: 54338, end: 54432 }
  source: "The student can demonstrate the effective use of creative approaches in the study of education"
  stem: "4.5"
  statementType: typical
  rung: typical
  force: will
  level: fheq:6
  appliesTo: "honours students at the typical standard"
  addressee: learner
  verbs: ["demonstrate"]
  about: "creative approaches to studying education"
  themes: [none]
  domain: subject-skill
  award: ["bachelor's with honours"]
  gradeOf: { statement: qaa/education-studies-2025/4.5.b8, basis: stated }
  paraphrase: "At the typical level of honours performance, the student can take creative approaches to studying education, and to good effect."
  quote: full   # the issuer's statement is in `source` (D-std-0014)
  audience: both
  subjects: inherited
- id: qaa/education-studies-2025/4.5.b9
  locator: { number: "4.5.b9", headingPath: ["Benchmark standards", "Introduction"] }
  span: { start: 54766, end: 54901 }
  source: "The student can demonstrate the ability to plan for, and implement, suitable collaborations with students, staff and other stakeholders"
  stem: "4.5"
  statementType: threshold
  rung: threshold
  force: threshold
  level: fheq:6
  appliesTo: "honours students at the threshold standard"
  addressee: learner
  verbs: ["demonstrate", "plan", "implement"]
  about: "planning and carrying out collaborations"
  themes: [none]
  domain: subject-skill
  award: ["bachelor's with honours"]
  gradeOf: none
  paraphrase: "As the minimum for an honours degree in Education Studies, the student can plan and carry out suitable collaborations with fellow students, staff and wider stakeholders."
  quote: full   # the issuer's statement is in `source` (D-std-0014)
  audience: both
  subjects: inherited
- id: qaa/education-studies-2025/4.5.b9.excellent
  locator: { number: "4.5.b9.excellent", headingPath: ["Benchmark standards", "Introduction"] }
  span: { start: 55050, end: 55199 }
  source: "The student can demonstrate a highly developed ability to plan for and implement effective collaborations with students, staff and other stakeholders"
  stem: "4.5"
  statementType: excellent
  rung: excellent
  force: will
  level: fheq:6
  appliesTo: "honours students at the excellent standard"
  addressee: learner
  verbs: ["demonstrate", "plan", "implement"]
  about: "planning and carrying out collaborations"
  themes: [none]
  domain: subject-skill
  award: ["bachelor's with honours"]
  gradeOf: { statement: qaa/education-studies-2025/4.5.b9.typical, basis: stated }
  paraphrase: "At the excellent level of honours performance, the student can show a highly developed ability to plan and carry out effective collaborations with fellow students, staff and wider stakeholders."
  quote: full   # the issuer's statement is in `source` (D-std-0014)
  audience: both
  subjects: inherited
- id: qaa/education-studies-2025/4.5.b9.masters
  locator: { number: "4.5.b9.masters", headingPath: ["Benchmark standards", "Introduction"] }
  span: { start: 55200, end: 55378 }
  source: "The student can demonstrate an excellent ability to plan for and implement effective collaborations with students, staff and other stakeholders inside and outside an organisation"
  stem: "4.5"
  statementType: threshold
  rung: threshold
  force: will
  level: fheq:7
  appliesTo: "students completing a master's degree in Education Studies"
  addressee: learner
  verbs: ["demonstrate", "plan", "implement"]
  about: "planning and carrying out collaborations"
  themes: [none]
  domain: subject-skill
  award: ["master's"]
  gradeOf: none
  paraphrase: "For a master's degree in Education Studies, the student can show an excellent ability to plan and carry out effective collaborations with fellow students, staff and wider stakeholders, within and beyond an organisation."
  quote: full   # the issuer's statement is in `source` (D-std-0014)
  audience: both
  subjects: inherited
- id: qaa/education-studies-2025/4.5.b9.typical
  locator: { number: "4.5.b9.typical", headingPath: ["Benchmark standards", "Introduction"] }
  span: { start: 54902, end: 55049 }
  source: "The student can demonstrate a well-developed ability to plan for and implement effective collaborations with students, staff and other stakeholders"
  stem: "4.5"
  statementType: typical
  rung: typical
  force: will
  level: fheq:6
  appliesTo: "honours students at the typical standard"
  addressee: learner
  verbs: ["demonstrate", "plan", "implement"]
  about: "planning and carrying out collaborations"
  themes: [none]
  domain: subject-skill
  award: ["bachelor's with honours"]
  gradeOf: { statement: qaa/education-studies-2025/4.5.b9, basis: stated }
  paraphrase: "At the typical level of honours performance, the student can show a well-developed ability to plan and carry out effective collaborations with fellow students, staff and wider stakeholders."
  quote: full   # the issuer's statement is in `source` (D-std-0014)
  audience: both
  subjects: inherited
- id: qaa/education-studies-2025/4.5.b10
  locator: { number: "4.5.b10", headingPath: ["Benchmark standards", "Introduction"] }
  span: { start: 55394, end: 55481 }
  source: "The student can identify challenges and identify appropriate approaches to resolve them"
  stem: "4.5"
  statementType: threshold
  rung: threshold
  force: threshold
  level: fheq:6
  appliesTo: "honours students at the threshold standard"
  addressee: learner
  verbs: ["identify", "resolve"]
  about: "identifying challenges and resolving them"
  themes: [none]
  domain: subject-skill
  award: ["bachelor's with honours"]
  gradeOf: none
  paraphrase: "As the minimum for an honours degree in Education Studies, the student can spot challenges and find suitable ways to resolve them."
  quote: full   # the issuer's statement is in `source` (D-std-0014)
  audience: both
  subjects: inherited
- id: qaa/education-studies-2025/4.5.b10.excellent
  locator: { number: "4.5.b10.excellent", headingPath: ["Benchmark standards", "Introduction"] }
  span: { start: 55580, end: 55688 }
  source: "The student can identify challenges, and suggest and lead in applying appropriate approaches to resolve them"
  stem: "4.5"
  statementType: excellent
  rung: excellent
  force: will
  level: fheq:6
  appliesTo: "honours students at the excellent standard"
  addressee: learner
  verbs: ["identify", "suggest", "lead", "resolve"]
  about: "identifying challenges and resolving them"
  themes: [none]
  domain: subject-skill
  award: ["bachelor's with honours"]
  gradeOf: { statement: qaa/education-studies-2025/4.5.b10.typical, basis: stated }
  paraphrase: "At the excellent level of honours performance, the student can spot challenges, then propose suitable ways to resolve them and lead their use."
  quote: full   # the issuer's statement is in `source` (D-std-0014)
  audience: both
  subjects: inherited
- id: qaa/education-studies-2025/4.5.b10.masters
  locator: { number: "4.5.b10.masters", headingPath: ["Benchmark standards", "Introduction"] }
  span: { start: 55689, end: 55804 }
  source: "The student can demonstrate a deep understanding of challenges and suggest and apply original means to resolve them"
  stem: "4.5"
  statementType: threshold
  rung: threshold
  force: will
  level: fheq:7
  appliesTo: "students completing a master's degree in Education Studies"
  addressee: learner
  verbs: ["demonstrate", "suggest", "apply", "resolve"]
  about: "identifying challenges and resolving them"
  themes: [none]
  domain: subject-skill
  award: ["master's"]
  gradeOf: none
  paraphrase: "For a master's degree in Education Studies, the student can understand challenges deeply and propose and use original ways to resolve them."
  quote: full   # the issuer's statement is in `source` (D-std-0014)
  audience: both
  subjects: inherited
- id: qaa/education-studies-2025/4.5.b10.typical
  locator: { number: "4.5.b10.typical", headingPath: ["Benchmark standards", "Introduction"] }
  span: { start: 55482, end: 55579 }
  source: "The student can identify challenges, and suggest and apply appropriate approaches to resolve them"
  stem: "4.5"
  statementType: typical
  rung: typical
  force: will
  level: fheq:6
  appliesTo: "honours students at the typical standard"
  addressee: learner
  verbs: ["identify", "suggest", "apply", "resolve"]
  about: "identifying challenges and resolving them"
  themes: [none]
  domain: subject-skill
  award: ["bachelor's with honours"]
  gradeOf: { statement: qaa/education-studies-2025/4.5.b10, basis: stated }
  paraphrase: "At the typical level of honours performance, the student can spot challenges, then propose and use suitable ways to resolve them."
  quote: full   # the issuer's statement is in `source` (D-std-0014)
  audience: both
  subjects: inherited
- id: qaa/education-studies-2025/4.5.b11
  locator: { number: "4.5.b11", headingPath: ["Benchmark standards", "Introduction"] }
  span: { start: 55965, end: 56196 }
  source: "The student can demonstrate the skills needed to search for, identify and use a range of information, including written, numerical, visual and verbal and/or non-verbal outputs, emanating from digital, analogue and empirical sources"
  stem: "4.5"
  statementType: threshold
  rung: threshold
  force: threshold
  level: fheq:6
  appliesTo: "honours students at the threshold standard"
  addressee: learner
  verbs: ["demonstrate", "search", "identify", "use"]
  about: "finding and using information"
  themes: [none]
  domain: subject-skill
  award: ["bachelor's with honours"]
  gradeOf: none
  paraphrase: "As the minimum for an honours degree in Education Studies, the student can search for, find and use a range of information, whether written, numerical, visual, spoken or non-verbal, from digital, analogue and empirical sources."
  quote: full   # the issuer's statement is in `source` (D-std-0014)
  audience: both
  subjects: inherited
- id: qaa/education-studies-2025/4.5.b11.excellent
  locator: { number: "4.5.b11.excellent", headingPath: ["Benchmark standards", "Introduction"] }
  span: { start: 56451, end: 56721 }
  source: "The student consistently and insightfully demonstrates the\n\nskills needed to critically search for, identify and use a range of information, including written, numerical, visual and verbal and/or non-verbal outputs, emanating from digital, analogue and empirical sources"
  stem: "4.5"
  statementType: excellent
  rung: excellent
  force: will
  level: fheq:6
  appliesTo: "honours students at the excellent standard"
  addressee: learner
  verbs: ["demonstrates", "search", "identify", "use"]
  about: "finding and using information"
  themes: [none]
  domain: subject-skill
  award: ["bachelor's with honours"]
  gradeOf: { statement: qaa/education-studies-2025/4.5.b11.typical, basis: stated }
  paraphrase: "At the excellent level of honours performance, the student can consistently and with insight search critically for, find and use such a range of information from digital, analogue and empirical sources."
  quote: full   # the issuer's statement is in `source` (D-std-0014)
  audience: both
  subjects: inherited
- id: qaa/education-studies-2025/4.5.b11.masters
  locator: { number: "4.5.b11.masters", headingPath: ["Benchmark standards", "Introduction"] }
  span: { start: 56722, end: 56988 }
  source: "The student can use advanced search techniques to identify and use a wide range of information sources critically and with insight, including from written, numerical, visual and verbal and/or non-verbal outputs, emanating from digital, analogue and empirical sources"
  stem: "4.5"
  statementType: threshold
  rung: threshold
  force: will
  level: fheq:7
  appliesTo: "students completing a master's degree in Education Studies"
  addressee: learner
  verbs: ["use", "identify"]
  about: "finding and using information"
  themes: [none]
  domain: subject-skill
  award: ["master's"]
  gradeOf: none
  paraphrase: "For a master's degree in Education Studies, the student can apply advanced search techniques to locate a broad spread of information sources, of every kind, and use them critically and with insight."
  quote: full   # the issuer's statement is in `source` (D-std-0014)
  audience: both
  subjects: inherited
- id: qaa/education-studies-2025/4.5.b11.typical
  locator: { number: "4.5.b11.typical", headingPath: ["Benchmark standards", "Introduction"] }
  span: { start: 56197, end: 56450 }
  source: "The student consistently demonstrates the\n\nskills needed to critically search for, identify and use a range of information, including written, numerical, visual and verbal and/or non-verbal outputs, emanating from digital, analogue and empirical sources"
  stem: "4.5"
  statementType: typical
  rung: typical
  force: will
  level: fheq:6
  appliesTo: "honours students at the typical standard"
  addressee: learner
  verbs: ["demonstrates", "search", "identify", "use"]
  about: "finding and using information"
  themes: [none]
  domain: subject-skill
  award: ["bachelor's with honours"]
  gradeOf: { statement: qaa/education-studies-2025/4.5.b11, basis: stated }
  paraphrase: "At the typical level of honours performance, the student can consistently search critically for, find and use such a range of information from digital, analogue and empirical sources."
  quote: full   # the issuer's statement is in `source` (D-std-0014)
  audience: both
  subjects: inherited
- id: qaa/education-studies-2025/4.5.b12
  locator: { number: "4.5.b12", headingPath: ["Benchmark standards", "Introduction"] }
  span: { start: 57109, end: 57303 }
  source: "The student can organise and articulate information, opinions and arguments in speech, writing, visual and other appropriate means, with evidence of relevant specialist vocabulary and expression"
  stem: "4.5"
  statementType: threshold
  rung: threshold
  force: threshold
  level: fheq:6
  appliesTo: "honours students at the threshold standard"
  addressee: learner
  verbs: ["organise", "articulate"]
  about: "communicating and presenting"
  themes: [none]
  domain: subject-skill
  award: ["bachelor's with honours"]
  gradeOf: none
  paraphrase: "As the minimum for an honours degree in Education Studies, the student can set out and express information, opinions and arguments in speech, writing, visuals and other suitable forms, using the subject's specialist terms."
  quote: full   # the issuer's statement is in `source` (D-std-0014)
  audience: both
  subjects: inherited
- id: qaa/education-studies-2025/4.5.b12.excellent
  locator: { number: "4.5.b12.excellent", headingPath: ["Benchmark standards", "Introduction"] }
  span: { start: 57506, end: 57727 }
  source: "The student can organise and articulate information, opinions, and arguments in speech, writing, visual and other appropriate means, with evidence of the sophisticated use\n\nof relevant specialist vocabulary and expression"
  stem: "4.5"
  statementType: excellent
  rung: excellent
  force: will
  level: fheq:6
  appliesTo: "honours students at the excellent standard"
  addressee: learner
  verbs: ["organise", "articulate"]
  about: "communicating and presenting"
  themes: [none]
  domain: subject-skill
  award: ["bachelor's with honours"]
  gradeOf: { statement: qaa/education-studies-2025/4.5.b12.typical, basis: stated }
  paraphrase: "At the excellent level of honours performance, the student can set out and express information, opinions and arguments in speech, writing, visuals and other suitable forms, using the subject's specialist terms with sophistication."
  quote: full   # the issuer's statement is in `source` (D-std-0014)
  audience: both
  subjects: inherited
- id: qaa/education-studies-2025/4.5.b12.masters
  locator: { number: "4.5.b12.masters", headingPath: ["Benchmark standards", "Introduction"] }
  span: { start: 57728, end: 58053 }
  source: "The student can organise and articulate information, opinions and arguments in speech, writing, visual and other appropriate means, with evidence of the sophisticated use\n\nof relevant specialist vocabulary and expression. They\n\ncan critically justify the reasons for the choice of such means of communication and presentation"
  stem: "4.5"
  statementType: threshold
  rung: threshold
  force: will
  level: fheq:7
  appliesTo: "students completing a master's degree in Education Studies"
  addressee: learner
  verbs: ["organise", "articulate", "justify"]
  about: "communicating and presenting"
  themes: [none]
  domain: subject-skill
  award: ["master's"]
  gradeOf: none
  paraphrase: "For a master's degree in Education Studies, the student can set out and express information, opinions and arguments in speech, writing, visuals and other suitable forms with sophisticated use of specialist terms, and justify critically why those forms were chosen."
  quote: full   # the issuer's statement is in `source` (D-std-0014)
  audience: both
  subjects: inherited
- id: qaa/education-studies-2025/4.5.b12.typical
  locator: { number: "4.5.b12.typical", headingPath: ["Benchmark standards", "Introduction"] }
  span: { start: 57304, end: 57505 }
  source: "The student can organise and articulate information, opinions, and arguments in speech, writing, visual and other appropriate means, with consistent use of relevant specialist vocabulary and expression"
  stem: "4.5"
  statementType: typical
  rung: typical
  force: will
  level: fheq:6
  appliesTo: "honours students at the typical standard"
  addressee: learner
  verbs: ["organise", "articulate"]
  about: "communicating and presenting"
  themes: [none]
  domain: subject-skill
  award: ["bachelor's with honours"]
  gradeOf: { statement: qaa/education-studies-2025/4.5.b12, basis: stated }
  paraphrase: "At the typical level of honours performance, the student can set out and express information, opinions and arguments in speech, writing, visuals and other suitable forms, using the subject's specialist terms consistently."
  quote: full   # the issuer's statement is in `source` (D-std-0014)
  audience: both
  subjects: inherited
- id: qaa/education-studies-2025/4.5.b13
  locator: { number: "4.5.b13", headingPath: ["Benchmark standards", "Introduction"] }
  span: { start: 58076, end: 58195 }
  source: "The student can present a range of theoretical positions and demonstrate how\n\nthey might impact on educational practice"
  stem: "4.5"
  statementType: threshold
  rung: threshold
  force: threshold
  level: fheq:6
  appliesTo: "honours students at the threshold standard"
  addressee: learner
  verbs: ["present", "demonstrate"]
  about: "theoretical positions and educational practice"
  themes: [none]
  domain: subject-skill
  award: ["bachelor's with honours"]
  gradeOf: none
  paraphrase: "As the minimum for an honours degree in Education Studies, the student can set out a range of theoretical positions and show how each might bear on educational practice."
  quote: full   # the issuer's statement is in `source` (D-std-0014)
  audience: both
  subjects: inherited
- id: qaa/education-studies-2025/4.5.b13.excellent
  locator: { number: "4.5.b13.excellent", headingPath: ["Benchmark standards", "Introduction"] }
  span: { start: 58358, end: 58531 }
  source: "The student can present a wide range of theoretical positions and offer and justify a\n\ncritically well- informed argument as to how they might impact on educational practice"
  stem: "4.5"
  statementType: excellent
  rung: excellent
  force: will
  level: fheq:6
  appliesTo: "honours students at the excellent standard"
  addressee: learner
  verbs: ["present", "offer", "justify"]
  about: "theoretical positions and educational practice"
  themes: [none]
  domain: subject-skill
  award: ["bachelor's with honours"]
  gradeOf: { statement: qaa/education-studies-2025/4.5.b13.typical, basis: stated }
  paraphrase: "At the excellent level of honours performance, the student can set out a wide range of theoretical positions and make and justify a critically well-informed case for how each might bear on educational practice."
  quote: full   # the issuer's statement is in `source` (D-std-0014)
  audience: both
  subjects: inherited
- id: qaa/education-studies-2025/4.5.b13.masters
  locator: { number: "4.5.b13.masters", headingPath: ["Benchmark standards", "Introduction"] }
  span: { start: 58533, end: 58757 }
  source: "The student can demonstrate detailed and accurate knowledge of a wide range of theoretical positions and be able to articulate and justify a well- informed, critical and insightful point of view with\n\nelements of originality"
  stem: "4.5"
  statementType: threshold
  rung: threshold
  force: will
  level: fheq:7
  appliesTo: "students completing a master's degree in Education Studies"
  addressee: learner
  verbs: ["demonstrate", "articulate", "justify"]
  about: "theoretical positions and educational practice"
  themes: [none]
  domain: subject-skill
  award: ["master's"]
  gradeOf: none
  paraphrase: "For a master's degree in Education Studies, the student can show accurate and detailed knowledge of many theoretical positions and argue for and justify a critical, insightful and well-informed view that has some originality."
  quote: full   # the issuer's statement is in `source` (D-std-0014)
  audience: both
  subjects: inherited
- id: qaa/education-studies-2025/4.5.b13.typical
  locator: { number: "4.5.b13.typical", headingPath: ["Benchmark standards", "Introduction"] }
  span: { start: 58196, end: 58357 }
  source: "The student can present a wide range of theoretical positions and offer and justify a\n\nwell-informed argument as to how they might impact on educational practice"
  stem: "4.5"
  statementType: typical
  rung: typical
  force: will
  level: fheq:6
  appliesTo: "honours students at the typical standard"
  addressee: learner
  verbs: ["present", "offer", "justify"]
  about: "theoretical positions and educational practice"
  themes: [none]
  domain: subject-skill
  award: ["bachelor's with honours"]
  gradeOf: { statement: qaa/education-studies-2025/4.5.b13, basis: stated }
  paraphrase: "At the typical level of honours performance, the student can set out a wide range of theoretical positions and make and justify a well-informed case for how each might bear on educational practice."
  quote: full   # the issuer's statement is in `source` (D-std-0014)
  audience: both
  subjects: inherited
- id: qaa/education-studies-2025/4.5.b14
  locator: { number: "4.5.b14", headingPath: ["Benchmark standards", "Introduction"] }
  span: { start: 58800, end: 58927 }
  source: "The student can use digital technologies effectively and ethically to enhance a variety of approaches to the study of education"
  stem: "4.5"
  statementType: threshold
  rung: threshold
  force: threshold
  level: fheq:6
  appliesTo: "honours students at the threshold standard"
  addressee: learner
  verbs: ["use", "enhance"]
  about: "digital technologies, including AI, in study"
  themes: [none]
  domain: subject-skill
  award: ["bachelor's with honours"]
  gradeOf: none
  paraphrase: "As the minimum for an honours degree in Education Studies, the student can use digital technologies well and ethically to strengthen a range of approaches to studying education."
  quote: full   # the issuer's statement is in `source` (D-std-0014)
  audience: both
  subjects: inherited
- id: qaa/education-studies-2025/4.5.b14.excellent
  locator: { number: "4.5.b14.excellent", headingPath: ["Benchmark standards", "Introduction"] }
  span: { start: 59094, end: 59268 }
  source: "The student can demonstrate sophisticated, ethical, critically informed and effective use of digital technologies to enhance a variety of approaches to the study of education"
  stem: "4.5"
  statementType: excellent
  rung: excellent
  force: will
  level: fheq:6
  appliesTo: "honours students at the excellent standard"
  addressee: learner
  verbs: ["demonstrate", "enhance"]
  about: "digital technologies, including AI, in study"
  themes: [none]
  domain: subject-skill
  award: ["bachelor's with honours"]
  gradeOf: { statement: qaa/education-studies-2025/4.5.b14.typical, basis: stated }
  paraphrase: "At the excellent level of honours performance, the student can use digital technologies in a sophisticated, ethical, critically informed and effective way to strengthen a range of approaches to studying education."
  quote: full   # the issuer's statement is in `source` (D-std-0014)
  audience: both
  subjects: inherited
- id: qaa/education-studies-2025/4.5.b14.masters
  locator: { number: "4.5.b14.masters", headingPath: ["Benchmark standards", "Introduction"] }
  span: { start: 59269, end: 59440 }
  source: "The student can demonstrate sophisticated, ethical, self- directed, critically\n\ninformed and effective use of digital technologies to enhance critical and reflective study"
  stem: "4.5"
  statementType: threshold
  rung: threshold
  force: will
  level: fheq:7
  appliesTo: "students completing a master's degree in Education Studies"
  addressee: learner
  verbs: ["demonstrate", "enhance"]
  about: "digital technologies, including AI, in study"
  themes: [none]
  domain: subject-skill
  award: ["master's"]
  gradeOf: none
  paraphrase: "For a master's degree in Education Studies, the student can use digital technologies in a sophisticated, ethical, self-directed and critically informed way to strengthen critical and reflective study."
  quote: full   # the issuer's statement is in `source` (D-std-0014)
  audience: both
  subjects: inherited
- id: qaa/education-studies-2025/4.5.b14.typical
  locator: { number: "4.5.b14.typical", headingPath: ["Benchmark standards", "Introduction"] }
  span: { start: 58928, end: 59093 }
  source: "The student can demonstrate confident, ethical and effective use\n\nof digital technologies to systematically enhance a variety of approaches to the study of education"
  stem: "4.5"
  statementType: typical
  rung: typical
  force: will
  level: fheq:6
  appliesTo: "honours students at the typical standard"
  addressee: learner
  verbs: ["demonstrate", "enhance"]
  about: "digital technologies, including AI, in study"
  themes: [none]
  domain: subject-skill
  award: ["bachelor's with honours"]
  gradeOf: { statement: qaa/education-studies-2025/4.5.b14, basis: stated }
  paraphrase: "At the typical level of honours performance, the student can use digital technologies with confidence, ethically and well, to strengthen in a systematic way a range of approaches to studying education."
  quote: full   # the issuer's statement is in `source` (D-std-0014)
  audience: both
  subjects: inherited
- id: qaa/education-studies-2025/4.5.b15
  locator: { number: "4.5.b15", headingPath: ["Benchmark standards", "Introduction"] }
  span: { start: 59601, end: 59777 }
  source: "A student can demonstrate how to process, organise and articulate opinions and arguments to create, present and justify a chosen position, having drawn on relevant perspectives"
  stem: "4.5"
  statementType: threshold
  rung: threshold
  force: threshold
  level: fheq:6
  appliesTo: "honours students at the threshold standard"
  addressee: learner
  verbs: ["demonstrate", "process", "organise", "articulate"]
  about: "building and justifying a position"
  themes: [none]
  domain: generic-skill
  award: ["bachelor's with honours"]
  gradeOf: none
  paraphrase: "As the minimum for an honours degree in Education Studies, the student can show how to process, order and express opinions and arguments so as to build, present and defend a chosen stance that draws on relevant perspectives."
  quote: full   # the issuer's statement is in `source` (D-std-0014)
  audience: both
  subjects: inherited
- id: qaa/education-studies-2025/4.5.b15.excellent
  locator: { number: "4.5.b15.excellent", headingPath: ["Benchmark standards", "Introduction"] }
  span: { start: 60017, end: 60275 }
  source: "A student can demonstrate a deep understanding of how to process, synthesise, organise and articulate opinions and arguments using a range of sources to create\n\nnew syntheses and to present and justify a chosen position, having drawn on relevant perspectives"
  stem: "4.5"
  statementType: excellent
  rung: excellent
  force: will
  level: fheq:6
  appliesTo: "honours students at the excellent standard"
  addressee: learner
  verbs: ["demonstrate", "process", "synthesise", "organise", "articulate"]
  about: "building and justifying a position"
  themes: [none]
  domain: generic-skill
  award: ["bachelor's with honours"]
  gradeOf: { statement: qaa/education-studies-2025/4.5.b15.typical, basis: stated }
  paraphrase: "At the excellent level of honours performance, the student can show a deep grasp of how to process, synthesise, order and express opinions and arguments from varied sources so as to form new syntheses and argue for and defend a chosen stance."
  quote: full   # the issuer's statement is in `source` (D-std-0014)
  audience: both
  subjects: inherited
- id: qaa/education-studies-2025/4.5.b15.masters
  locator: { number: "4.5.b15.masters", headingPath: ["Benchmark standards", "Introduction"] }
  span: { start: 60276, end: 60538 }
  source: "A student can demonstrate a critical understanding of how to process, synthesise, organise and articulate opinions and arguments using a range of sources to create\n\nnew syntheses and to present and justify a chosen position, having drawn on relevant perspectives"
  stem: "4.5"
  statementType: threshold
  rung: threshold
  force: will
  level: fheq:7
  appliesTo: "students completing a master's degree in Education Studies"
  addressee: learner
  verbs: ["demonstrate", "process", "synthesise", "organise", "articulate"]
  about: "building and justifying a position"
  themes: [none]
  domain: generic-skill
  award: ["master's"]
  gradeOf: none
  paraphrase: "For a master's degree in Education Studies, the student can show a critical grasp of how to process, synthesise, order and express opinions and arguments from varied sources so as to form new syntheses and argue for and defend a chosen stance."
  quote: full   # the issuer's statement is in `source` (D-std-0014)
  audience: both
  subjects: inherited
- id: qaa/education-studies-2025/4.5.b15.typical
  locator: { number: "4.5.b15.typical", headingPath: ["Benchmark standards", "Introduction"] }
  span: { start: 59778, end: 60016 }
  source: "A student can demonstrate a sound understanding of how to process, synthesise, organise and articulate opinions and arguments using a range of sources to present and justify a chosen position, having drawn on theory- relevant perspectives"
  stem: "4.5"
  statementType: typical
  rung: typical
  force: will
  level: fheq:6
  appliesTo: "honours students at the typical standard"
  addressee: learner
  verbs: ["demonstrate", "process", "synthesise", "organise", "articulate"]
  about: "building and justifying a position"
  themes: [none]
  domain: generic-skill
  award: ["bachelor's with honours"]
  gradeOf: { statement: qaa/education-studies-2025/4.5.b15, basis: stated }
  paraphrase: "At the typical level of honours performance, the student can show a sound grasp of how to process, synthesise, order and express opinions and arguments, drawing on varied sources, to argue for and defend a chosen stance grounded in theory."
  quote: full   # the issuer's statement is in `source` (D-std-0014)
  audience: both
  subjects: inherited
- id: qaa/education-studies-2025/4.5.b16
  locator: { number: "4.5.b16", headingPath: ["Benchmark standards", "Introduction"] }
  span: { start: 60553, end: 60795 }
  source: "A student can demonstrate how to effectively communicate through respectful interactions with diverse groups of\n\npeople and be able to plan work\n\nwithin a specified role, helping to build trust within a team, to fulfil agreed responsibilities"
  stem: "4.5"
  statementType: threshold
  rung: threshold
  force: threshold
  level: fheq:6
  appliesTo: "honours students at the threshold standard"
  addressee: learner
  verbs: ["demonstrate", "communicate", "plan"]
  about: "communicating and working in a team"
  themes: [none]
  domain: generic-skill
  award: ["bachelor's with honours"]
  gradeOf: none
  paraphrase: "As the minimum for an honours degree in Education Studies, the student can show how to communicate well through respectful exchanges with diverse groups, and plan work within a set role that builds trust in a team and meets agreed responsibilities."
  quote: full   # the issuer's statement is in `source` (D-std-0014)
  audience: both
  subjects: inherited
- id: qaa/education-studies-2025/4.5.b16.excellent
  locator: { number: "4.5.b16.excellent", headingPath: ["Benchmark standards", "Introduction"] }
  span: { start: 61065, end: 61332 }
  source: "A student can demonstrate a deep understanding of how to effectively\n\ncommunicate through respectful interactions with diverse groups of\n\npeople and be able to plan work\n\nwithin a specified role, helping to build trust within a team, to fulfil agreed responsibilities"
  stem: "4.5"
  statementType: excellent
  rung: excellent
  force: will
  level: fheq:6
  appliesTo: "honours students at the excellent standard"
  addressee: learner
  verbs: ["demonstrate", "communicate", "plan"]
  about: "communicating and working in a team"
  themes: [none]
  domain: generic-skill
  award: ["bachelor's with honours"]
  gradeOf: { statement: qaa/education-studies-2025/4.5.b16.typical, basis: stated }
  paraphrase: "At the excellent level of honours performance, the student can show a deep grasp of how to communicate well through respectful exchanges with diverse groups, and plan work within a set role that builds trust in a team and meets agreed responsibilities."
  quote: full   # the issuer's statement is in `source` (D-std-0014)
  audience: both
  subjects: inherited
- id: qaa/education-studies-2025/4.5.b16.masters
  locator: { number: "4.5.b16.masters", headingPath: ["Benchmark standards", "Introduction"] }
  span: { start: 61333, end: 61604 }
  source: "A student can demonstrate a critical understanding of how to effectively\n\ncommunicate through respectful interactions with diverse groups of\n\npeople and be able to plan work\n\nwithin a specified role, helping to build trust within a team, to fulfil agreed responsibilities"
  stem: "4.5"
  statementType: threshold
  rung: threshold
  force: will
  level: fheq:7
  appliesTo: "students completing a master's degree in Education Studies"
  addressee: learner
  verbs: ["demonstrate", "communicate", "plan"]
  about: "communicating and working in a team"
  themes: [none]
  domain: generic-skill
  award: ["master's"]
  gradeOf: none
  paraphrase: "For a master's degree in Education Studies, the student can show a critical grasp of how to communicate well through respectful exchanges with diverse groups, and plan work within a set role that builds trust in a team and meets agreed responsibilities."
  quote: full   # the issuer's statement is in `source` (D-std-0014)
  audience: both
  subjects: inherited
- id: qaa/education-studies-2025/4.5.b16.typical
  locator: { number: "4.5.b16.typical", headingPath: ["Benchmark standards", "Introduction"] }
  span: { start: 60796, end: 61064 }
  source: "A student can demonstrate a sound understanding of how to effectively\n\ncommunicate through respectful interactions with diverse groups of\n\npeople and be able to plan work\n\nwithin a specified role, helping to build trust within a team, to fulfil agreed responsibilities"
  stem: "4.5"
  statementType: typical
  rung: typical
  force: will
  level: fheq:6
  appliesTo: "honours students at the typical standard"
  addressee: learner
  verbs: ["demonstrate", "communicate", "plan"]
  about: "communicating and working in a team"
  themes: [none]
  domain: generic-skill
  award: ["bachelor's with honours"]
  gradeOf: { statement: qaa/education-studies-2025/4.5.b16, basis: stated }
  paraphrase: "At the typical level of honours performance, the student can show a sound grasp of how to communicate well through respectful exchanges with diverse groups, and plan work within a set role that builds trust in a team and meets agreed responsibilities."
  quote: full   # the issuer's statement is in `source` (D-std-0014)
  audience: both
  subjects: inherited
- id: qaa/education-studies-2025/4.5.b17
  locator: { number: "4.5.b17", headingPath: ["Benchmark standards", "Introduction"] }
  span: { start: 61753, end: 61992 }
  source: "A student can demonstrate how to access information from appropriate sources, a critical\n\nawareness of those information\n\nsources, how to use digital tools and software appropriately, an ethical awareness and understanding of online safety"
  stem: "4.5"
  statementType: threshold
  rung: threshold
  force: threshold
  level: fheq:6
  appliesTo: "honours students at the threshold standard"
  addressee: learner
  verbs: ["demonstrate", "access", "use"]
  about: "accessing information safely and ethically"
  themes: [none]
  domain: generic-skill
  award: ["bachelor's with honours"]
  gradeOf: none
  paraphrase: "As the minimum for an honours degree in Education Studies, the student can show how to get information from suitable sources with a critical eye on those sources, the proper use of digital tools and software, ethical awareness and an understanding of staying safe online."
  quote: full   # the issuer's statement is in `source` (D-std-0014)
  audience: both
  subjects: inherited
- id: qaa/education-studies-2025/4.5.b17.excellent
  locator: { number: "4.5.b17.excellent", headingPath: ["Benchmark standards", "Introduction"] }
  span: { start: 62258, end: 62521 }
  source: "A student can demonstrate a deep understanding of how to access information from appropriate sources, a critical\n\nawareness of those information\n\nsources, how to use digital tools and software appropriately, an ethical awareness and understanding of online safety"
  stem: "4.5"
  statementType: excellent
  rung: excellent
  force: will
  level: fheq:6
  appliesTo: "honours students at the excellent standard"
  addressee: learner
  verbs: ["demonstrate", "access", "use"]
  about: "accessing information safely and ethically"
  themes: [none]
  domain: generic-skill
  award: ["bachelor's with honours"]
  gradeOf: { statement: qaa/education-studies-2025/4.5.b17.typical, basis: stated }
  paraphrase: "At the excellent level of honours performance, the student can show a deep grasp of how to get information from suitable sources with a critical eye on those sources, the proper use of digital tools and software, ethical awareness and an understanding of staying safe online."
  quote: full   # the issuer's statement is in `source` (D-std-0014)
  audience: both
  subjects: inherited
- id: qaa/education-studies-2025/4.5.b17.masters
  locator: { number: "4.5.b17.masters", headingPath: ["Benchmark standards", "Introduction"] }
  span: { start: 62522, end: 62791 }
  source: "A student can demonstrate a systematic understanding of how to access information from appropriate sources, a critical\n\nawareness of those information\n\nsources, how to use digital tools and software appropriately, an ethical awareness and understanding of online safety"
  stem: "4.5"
  statementType: threshold
  rung: threshold
  force: will
  level: fheq:7
  appliesTo: "students completing a master's degree in Education Studies"
  addressee: learner
  verbs: ["demonstrate", "access", "use"]
  about: "accessing information safely and ethically"
  themes: [none]
  domain: generic-skill
  award: ["master's"]
  gradeOf: none
  paraphrase: "For a master's degree in Education Studies, the student can show a systematic grasp of how to get information from suitable sources with a critical eye on those sources, the proper use of digital tools and software, ethical awareness and an understanding of staying safe online."
  quote: full   # the issuer's statement is in `source` (D-std-0014)
  audience: both
  subjects: inherited
- id: qaa/education-studies-2025/4.5.b17.typical
  locator: { number: "4.5.b17.typical", headingPath: ["Benchmark standards", "Introduction"] }
  span: { start: 61993, end: 62257 }
  source: "A student can demonstrate a sound understanding of how to access information from appropriate sources, a critical\n\nawareness of those information\n\nsources, how to use digital tools and software appropriately, an ethical awareness and understanding of online safety"
  stem: "4.5"
  statementType: typical
  rung: typical
  force: will
  level: fheq:6
  appliesTo: "honours students at the typical standard"
  addressee: learner
  verbs: ["demonstrate", "access", "use"]
  about: "accessing information safely and ethically"
  themes: [none]
  domain: generic-skill
  award: ["bachelor's with honours"]
  gradeOf: { statement: qaa/education-studies-2025/4.5.b17, basis: stated }
  paraphrase: "At the typical level of honours performance, the student can show a sound grasp of how to get information from suitable sources with a critical eye on those sources, the proper use of digital tools and software, ethical awareness and an understanding of staying safe online."
  quote: full   # the issuer's statement is in `source` (D-std-0014)
  audience: both
  subjects: inherited
- id: qaa/education-studies-2025/4.5.b18
  locator: { number: "4.5.b18", headingPath: ["Benchmark standards", "Introduction"] }
  span: { start: 62810, end: 63006 }
  source: "A student can demonstrate how to collect, analyse, interpret, apply and present data in a variety of verbal and non- verbal formats, both appropriately and\n\nethically for the task and the audience"
  stem: "4.5"
  statementType: threshold
  rung: threshold
  force: threshold
  level: fheq:6
  appliesTo: "honours students at the threshold standard"
  addressee: learner
  verbs: ["demonstrate", "collect", "analyse", "interpret", "apply", "present"]
  about: "working with data across formats"
  themes: [none]
  domain: generic-skill
  award: ["bachelor's with honours"]
  gradeOf: none
  paraphrase: "As the minimum for an honours degree in Education Studies, the student can show how to gather data, then analyse, interpret, apply and present it in varied verbal and non-verbal forms, suited to the task and audience and handled ethically."
  quote: full   # the issuer's statement is in `source` (D-std-0014)
  audience: both
  subjects: inherited
- id: qaa/education-studies-2025/4.5.b18.excellent
  locator: { number: "4.5.b18.excellent", headingPath: ["Benchmark standards", "Introduction"] }
  span: { start: 63220, end: 63431 }
  source: "A student can demonstrate a deep understanding of how to analyse, interpret, apply and present data in a variety of verbal and non- verbal formats, both appropriately and\n\nethically for the task and the audience"
  stem: "4.5"
  statementType: excellent
  rung: excellent
  force: will
  level: fheq:6
  appliesTo: "honours students at the excellent standard"
  addressee: learner
  verbs: ["demonstrate", "analyse", "interpret", "apply", "present"]
  about: "working with data across formats"
  themes: [none]
  domain: generic-skill
  award: ["bachelor's with honours"]
  gradeOf: { statement: qaa/education-studies-2025/4.5.b18.typical, basis: stated }
  paraphrase: "At the excellent level of honours performance, the student can show a deep grasp of analysing, interpreting, applying and presenting data in varied verbal and non-verbal forms, suited to the task and audience and handled ethically."
  quote: full   # the issuer's statement is in `source` (D-std-0014)
  audience: both
  subjects: inherited
- id: qaa/education-studies-2025/4.5.b18.masters
  locator: { number: "4.5.b18.masters", headingPath: ["Benchmark standards", "Introduction"] }
  span: { start: 63432, end: 63647 }
  source: "A student can demonstrate a critical understanding of how to analyse, interpret, apply and present data in a variety of verbal and non- verbal formats, both appropriately and\n\nethically for the task and the audience"
  stem: "4.5"
  statementType: threshold
  rung: threshold
  force: will
  level: fheq:7
  appliesTo: "students completing a master's degree in Education Studies"
  addressee: learner
  verbs: ["demonstrate", "analyse", "interpret", "apply", "present"]
  about: "working with data across formats"
  themes: [none]
  domain: generic-skill
  award: ["master's"]
  gradeOf: none
  paraphrase: "For a master's degree in Education Studies, the student can show a critical grasp of analysing, interpreting, applying and presenting data in varied verbal and non-verbal forms, suited to the task and audience and handled ethically."
  quote: full   # the issuer's statement is in `source` (D-std-0014)
  audience: both
  subjects: inherited
- id: qaa/education-studies-2025/4.5.b18.typical
  locator: { number: "4.5.b18.typical", headingPath: ["Benchmark standards", "Introduction"] }
  span: { start: 63007, end: 63219 }
  source: "A student can demonstrate a sound understanding of how to analyse, interpret, apply and present data in a variety of verbal and non- verbal formats, both appropriately and\n\nethically for the task and the audience"
  stem: "4.5"
  statementType: typical
  rung: typical
  force: will
  level: fheq:6
  appliesTo: "honours students at the typical standard"
  addressee: learner
  verbs: ["demonstrate", "analyse", "interpret", "apply", "present"]
  about: "working with data across formats"
  themes: [none]
  domain: generic-skill
  award: ["bachelor's with honours"]
  gradeOf: { statement: qaa/education-studies-2025/4.5.b18, basis: stated }
  paraphrase: "At the typical level of honours performance, the student can show a sound grasp of analysing, interpreting, applying and presenting data in varied verbal and non-verbal forms, suited to the task and audience and handled ethically."
  quote: full   # the issuer's statement is in `source` (D-std-0014)
  audience: both
  subjects: inherited
- id: qaa/education-studies-2025/4.5.b19
  locator: { number: "4.5.b19", headingPath: ["Benchmark standards", "Introduction"] }
  span: { start: 63669, end: 63876 }
  source: "A student can demonstrate flexibility, adaptability and personal responsibility to engage in ongoing self- reflection, lifelong\n\nlearning, understanding the importance of empathy, active listening and action"
  stem: "4.5"
  statementType: threshold
  rung: threshold
  force: threshold
  level: fheq:6
  appliesTo: "honours students at the threshold standard"
  addressee: learner
  verbs: ["demonstrate", "engage"]
  about: "flexibility, self-reflection and lifelong learning"
  themes: [none]
  domain: generic-skill
  award: ["bachelor's with honours"]
  gradeOf: none
  paraphrase: "As the minimum for an honours degree in Education Studies, the student can show flexibility, adaptability and the personal responsibility to keep up self-reflection and learning throughout life, seeing why empathy, active listening and action matter."
  quote: full   # the issuer's statement is in `source` (D-std-0014)
  audience: both
  subjects: inherited
- id: qaa/education-studies-2025/4.5.b19.excellent
  locator: { number: "4.5.b19.excellent", headingPath: ["Benchmark standards", "Introduction"] }
  span: { start: 64110, end: 64341 }
  source: "A student can demonstrate a deep understanding of flexibility, adaptability and personal responsibility to engage in ongoing self- reflection, lifelong\n\nlearning, understanding the importance of empathy, active listening and action"
  stem: "4.5"
  statementType: excellent
  rung: excellent
  force: will
  level: fheq:6
  appliesTo: "honours students at the excellent standard"
  addressee: learner
  verbs: ["demonstrate", "engage"]
  about: "flexibility, self-reflection and lifelong learning"
  themes: [none]
  domain: generic-skill
  award: ["bachelor's with honours"]
  gradeOf: { statement: qaa/education-studies-2025/4.5.b19.typical, basis: stated }
  paraphrase: "At the excellent level of honours performance, the student can show a deep grasp of flexibility, adaptability and the personal responsibility to keep up self-reflection and learning throughout life, seeing why empathy, active listening and action matter."
  quote: full   # the issuer's statement is in `source` (D-std-0014)
  audience: both
  subjects: inherited
- id: qaa/education-studies-2025/4.5.b19.masters
  locator: { number: "4.5.b19.masters", headingPath: ["Benchmark standards", "Introduction"] }
  span: { start: 64342, end: 64578 }
  source: "A student can demonstrate a systematic understanding of flexibility adaptability and personal responsibility to engage in ongoing self- reflection, lifelong\n\nlearning, understanding the importance of empathy, active listening and action"
  stem: "4.5"
  statementType: threshold
  rung: threshold
  force: will
  level: fheq:7
  appliesTo: "students completing a master's degree in Education Studies"
  addressee: learner
  verbs: ["demonstrate", "engage"]
  about: "flexibility, self-reflection and lifelong learning"
  themes: [none]
  domain: generic-skill
  award: ["master's"]
  gradeOf: none
  paraphrase: "For a master's degree in Education Studies, the student can show a systematic grasp of flexibility, adaptability and the personal responsibility to keep up self-reflection and learning throughout life, seeing why empathy, active listening and action matter."
  quote: full   # the issuer's statement is in `source` (D-std-0014)
  audience: both
  subjects: inherited
- id: qaa/education-studies-2025/4.5.b19.typical
  locator: { number: "4.5.b19.typical", headingPath: ["Benchmark standards", "Introduction"] }
  span: { start: 63877, end: 64109 }
  source: "A student can demonstrate a sound understanding of flexibility, adaptability and personal responsibility to engage in ongoing self- reflection, lifelong\n\nlearning, understanding the importance of empathy, active listening and action"
  stem: "4.5"
  statementType: typical
  rung: typical
  force: will
  level: fheq:6
  appliesTo: "honours students at the typical standard"
  addressee: learner
  verbs: ["demonstrate", "engage"]
  about: "flexibility, self-reflection and lifelong learning"
  themes: [none]
  domain: generic-skill
  award: ["bachelor's with honours"]
  gradeOf: { statement: qaa/education-studies-2025/4.5.b19, basis: stated }
  paraphrase: "At the typical level of honours performance, the student can show a sound grasp of flexibility, adaptability and the personal responsibility to keep up self-reflection and learning throughout life, seeing why empathy, active listening and action matter."
  quote: full   # the issuer's statement is in `source` (D-std-0014)
  audience: both
  subjects: inherited
- id: qaa/education-studies-2025/4.5.b20
  locator: { number: "4.5.b20", headingPath: ["Benchmark standards", "Introduction"] }
  span: { start: 64712, end: 64891 }
  source: "A student can demonstrate engagement in change processes, being\n\nable to anticipate and reconcile tensions, dilemmas and complexity, and understand the concept of futures thinking"
  stem: "4.5"
  statementType: threshold
  rung: threshold
  force: threshold
  level: fheq:6
  appliesTo: "honours students at the threshold standard"
  addressee: learner
  verbs: ["demonstrate", "anticipate", "reconcile", "understand"]
  about: "taking part in change; futures thinking"
  themes: [none]
  domain: generic-skill
  award: ["bachelor's with honours"]
  gradeOf: none
  paraphrase: "As the minimum for an honours degree in Education Studies, the student can show engagement in processes of change, foreseeing and reconciling tensions, dilemmas and complexity, and grasp what futures thinking means."
  quote: full   # the issuer's statement is in `source` (D-std-0014)
  audience: both
  subjects: inherited
- id: qaa/education-studies-2025/4.5.b20.excellent
  locator: { number: "4.5.b20.excellent", headingPath: ["Benchmark standards", "Introduction"] }
  span: { start: 65100, end: 65306 }
  source: "A student can demonstrate a deep understanding of how to engage in change processes, being\n\nable to anticipate and reconcile tensions, dilemmas and complexity, and understand the concept of futures thinking"
  stem: "4.5"
  statementType: excellent
  rung: excellent
  force: will
  level: fheq:6
  appliesTo: "honours students at the excellent standard"
  addressee: learner
  verbs: ["demonstrate", "engage", "anticipate", "reconcile", "understand"]
  about: "taking part in change; futures thinking"
  themes: [none]
  domain: generic-skill
  award: ["bachelor's with honours"]
  gradeOf: { statement: qaa/education-studies-2025/4.5.b20.typical, basis: stated }
  paraphrase: "At the excellent level of honours performance, the student can show a deep grasp of how to take part in processes of change, foreseeing and reconciling tensions, dilemmas and complexity, and grasp what futures thinking means."
  quote: full   # the issuer's statement is in `source` (D-std-0014)
  audience: both
  subjects: inherited
- id: qaa/education-studies-2025/4.5.b20.masters
  locator: { number: "4.5.b20.masters", headingPath: ["Benchmark standards", "Introduction"] }
  span: { start: 65307, end: 65519 }
  source: "A student can demonstrate a systematic understanding of how to engage in change processes, being\n\nable to anticipate and reconcile tensions, dilemmas and complexity, and understand the concept of futures thinking"
  stem: "4.5"
  statementType: threshold
  rung: threshold
  force: will
  level: fheq:7
  appliesTo: "students completing a master's degree in Education Studies"
  addressee: learner
  verbs: ["demonstrate", "engage", "anticipate", "reconcile", "understand"]
  about: "taking part in change; futures thinking"
  themes: [none]
  domain: generic-skill
  award: ["master's"]
  gradeOf: none
  paraphrase: "For a master's degree in Education Studies, the student can show a systematic grasp of how to take part in processes of change, foreseeing and reconciling tensions, dilemmas and complexity, and grasp what futures thinking means."
  quote: full   # the issuer's statement is in `source` (D-std-0014)
  audience: both
  subjects: inherited
- id: qaa/education-studies-2025/4.5.b20.typical
  locator: { number: "4.5.b20.typical", headingPath: ["Benchmark standards", "Introduction"] }
  span: { start: 64892, end: 65099 }
  source: "A student can demonstrate a sound understanding of how to engage in change processes, being\n\nable to anticipate and reconcile tensions, dilemmas and complexity, and understand the concept of futures thinking"
  stem: "4.5"
  statementType: typical
  rung: typical
  force: will
  level: fheq:6
  appliesTo: "honours students at the typical standard"
  addressee: learner
  verbs: ["demonstrate", "engage", "anticipate", "reconcile", "understand"]
  about: "taking part in change; futures thinking"
  themes: [none]
  domain: generic-skill
  award: ["bachelor's with honours"]
  gradeOf: { statement: qaa/education-studies-2025/4.5.b20, basis: stated }
  paraphrase: "At the typical level of honours performance, the student can show a sound grasp of how to take part in processes of change, foreseeing and reconciling tensions, dilemmas and complexity, and grasp what futures thinking means."
  quote: full   # the issuer's statement is in `source` (D-std-0014)
  audience: both
  subjects: inherited
- id: qaa/education-studies-2025/4.7
  locator: { number: "4.7", headingPath: ["Benchmark standards", "Threshold level"] }
  span: { start: 65623, end: 65925 }
  source: "4.7 The specific professional requirements and learning ability needed to undertake appropriate further training of a professional or equivalent nature. Where a degree award requires an assessment of professional competencies, a PSRB-accredited award will not be made if the student does not meet them."
  stem: none
  statementType: requirement
  rung: none
  force: will
  level: fheq:6
  appliesTo: "students on PSRB-accredited courses"
  addressee: both
  verbs: ["requires", "made", "meet"]
  about: "professional competence as a condition of a PSRB-accredited award"
  themes: [none]
  domain: none
  award: ["bachelor's with honours"]
  gradeOf: none
  paraphrase: "This row covers the professional requirements and the learning ability needed for further professional training; where a degree calls for professional competencies to be assessed, the PSRB-accredited award will not be made unless the student meets them."
  quote: full   # the issuer's statement is in `source` (D-std-0014)
  audience: both
  subjects: inherited
- id: qaa/education-studies-2025/4.7.b1
  locator: { number: "4.7.b1", headingPath: ["Benchmark standards", "Threshold level"] }
  span: { start: 66121, end: 66238 }
  source: "The student has demonstrated achievement of professional competence when assessed against the requirements of a PSRB."
  stem: "4.7"
  statementType: threshold
  rung: threshold
  force: threshold
  level: fheq:6
  appliesTo: "students on PSRB-accredited courses"
  addressee: learner
  verbs: ["demonstrated", "assessed"]
  about: "professional competence met"
  themes: [none]
  domain: subject-skill
  award: ["bachelor's with honours"]
  gradeOf: none
  paraphrase: "To succeed, the student has shown professional competence when judged against what a professional, statutory or regulatory body asks for."
  quote: full   # the issuer's statement is in `source` (D-std-0014)
  audience: both
  subjects: inherited
- id: qaa/education-studies-2025/4.7.b2
  locator: { number: "4.7.b2", headingPath: ["Benchmark standards", "Threshold level"] }
  span: { start: 66352, end: 66454 }
  source: "The student has adhered to the appropriate rules and/or conventions set by regulators or the industry."
  stem: "4.7"
  statementType: threshold
  rung: threshold
  force: threshold
  level: fheq:6
  appliesTo: "students on PSRB-accredited courses"
  addressee: learner
  verbs: ["adhered", "set"]
  about: "keeping to regulators' and industry rules"
  themes: [none]
  domain: subject-skill
  award: ["bachelor's with honours"]
  gradeOf: none
  paraphrase: "To succeed, the student has kept to the rules or conventions that regulators or the industry lay down."
  quote: full   # the issuer's statement is in `source` (D-std-0014)
  audience: both
  subjects: inherited
```

### S4a Audience versions
<!-- label: both; status: drafted; basis: primary. forPractitioner: for the programme designer or teacher. forBeneficiary: for the student, second person, naming no issuer. author-agent-written: instructions to an AI agent writing about the statement (a course document, a handbook, an outcome, a report). author-agent-dialogue: instructions to an AI agent using the statement in conversation (with a student, a teacher or a programme team). Written fresh from the held text alone (benchmark rule 6; Abbott, 15:42). -->
```yaml
- statement: qaa/education-studies-2025/1.6
  forPractitioner: { text: "Give students room to join, shape and contest debates on values and practice, and to choose, analyse and combine viewpoints until they can hold and defend a reasoned stance; tie this to their future careers and continued learning.", rewrite: light, force: will, status: drafted }
  forBeneficiary: { text: "You can take part in, shape and question debates about values, practice and communities, and you learn to choose, analyse and combine viewpoints so that you can argue for a reasoned stance of your own.", rewrite: full, force: will, status: drafted }
  author-agent-written: "Write about this as an expected outcome or feature worded with \"will\" or \"can\" for the honours degree, at FHEQ Level 6 (FQHEIS Level 10, spine:6), on taking a reasoned position in educational debate. Cite it as QAA, 2025, Education Studies Subject Benchmark Statement, para 1.6. Do not claim it is a regulatory requirement, a rung of the standards table or a standard at another level. Set it beside qaa/education-studies-2025/1.9 and the framework descriptor qaa/fheq-2024/4.15.b4 and 4.15.b7."
  author-agent-dialogue: "Bring it up when a student asks about taking a reasoned position in educational debate, or when staff check a module or outcome against it. Tell a student in plain words, as 'you', what it means for their course; for staff, frame it as an expected outcome or feature worded with \"will\" or \"can\". Ask: Which debate in education have you taken a stance on, and which viewpoints brought you there? Avoid long quotation of the issuer's text."
- statement: qaa/education-studies-2025/1.9
  forPractitioner: { text: "Build in tasks where students question the key terms and concepts of education and trace how dominant language and knowledge have taken hold in formal, informal and hidden curricula.", rewrite: light, force: will, status: drafted }
  forBeneficiary: { text: "You can question the key ideas and terms you meet, and see how dominant ways of speaking, knowing and thinking have taken hold in what is taught openly, informally and in the hidden curriculum.", rewrite: full, force: will, status: drafted }
  author-agent-written: "Write about this as an expected outcome or feature worded with \"will\" or \"can\" for the honours degree, at FHEQ Level 6 (FQHEIS Level 10, spine:6), on questioning entrenched language, knowledge and thought. Cite it as QAA, 2025, Education Studies Subject Benchmark Statement, para 1.9. Do not claim it is a regulatory requirement, a rung of the standards table or a standard at another level. Set it beside qaa/education-studies-2025/1.6 and qaa/education-studies-2025/1.11 and the framework descriptor qaa/fheq-2024/4.15.b4 and 4.15.b7."
  author-agent-dialogue: "Bring it up when a student asks about questioning entrenched language, knowledge and thought, or when staff check a module or outcome against it. Tell a student in plain words, as 'you', what it means for their course; for staff, frame it as an expected outcome or feature worded with \"will\" or \"can\". Ask: Which taken-for-granted term in education would you question first, and why? Avoid long quotation of the issuer's text."
- statement: qaa/education-studies-2025/1.11
  forPractitioner: { text: "Ask students to work through EDI questions, weigh different standpoints and state their own position with reference to rights, duties, responsibilities and the law, and also beyond those frames.", rewrite: light, force: will, status: drafted }
  forBeneficiary: { text: "You can work with questions of equity, diversity and inclusion, see what it takes to help build a fairer society, recognise other people's standpoints and say clearly where you stand.", rewrite: full, force: will, status: drafted }
  author-agent-written: "Write about this as an expected outcome or feature worded with \"will\" or \"can\" for the honours degree, at FHEQ Level 6 (FQHEIS Level 10, spine:6), on engaging with EDI and taking a position on justice. Cite it as QAA, 2025, Education Studies Subject Benchmark Statement, para 1.11. Do not claim it is a regulatory requirement, a rung of the standards table or a standard at another level. Set it beside qaa/education-studies-2025/1.9 and qaa/education-studies-2025/1.13 and the framework descriptor qaa/fheq-2024/4.15.b4 and 4.15.b7."
  author-agent-dialogue: "Bring it up when a student asks about engaging with EDI and taking a position on justice, or when staff check a module or outcome against it. Tell a student in plain words, as 'you', what it means for their course; for staff, frame it as an expected outcome or feature worded with \"will\" or \"can\". Ask: Where do you stand on one EDI question in education, and how does the law shape or fail to shape your view? Avoid long quotation of the issuer's text."
- statement: qaa/education-studies-2025/1.13
  forPractitioner: { text: "Give students real scope to reflect, question and take part, and assess reflection that pairs self-understanding with respect for views far from their own.", rewrite: light, force: will, status: drafted }
  forBeneficiary: { text: "Your course gives you room to reflect, question and take part, and you can become skilled at reflection, understanding what is distinctive about you while respecting views that differ sharply from yours.", rewrite: full, force: will, status: drafted }
  author-agent-written: "Write about this as an expected outcome or feature worded with \"will\" or \"can\" for the honours degree, at FHEQ Level 6 (FQHEIS Level 10, spine:6), on reflection, self-understanding and respect for divergent views. Cite it as QAA, 2025, Education Studies Subject Benchmark Statement, para 1.13. Do not claim it is a regulatory requirement, a rung of the standards table or a standard at another level. Set it beside qaa/education-studies-2025/1.11 and qaa/education-studies-2025/1.15 and the framework descriptor qaa/fheq-2024/4.15.b9.1 and 4.15.b9.3."
  author-agent-dialogue: "Bring it up when a student asks about reflection, self-understanding and respect for divergent views, or when staff check a module or outcome against it. Tell a student in plain words, as 'you', what it means for their course; for staff, frame it as an expected outcome or feature worded with \"will\" or \"can\". Ask: When did a view you disagreed with change how you see your own position? Avoid long quotation of the issuer's text."
- statement: qaa/education-studies-2025/1.15
  forPractitioner: { text: "Treat accessibility in teaching, learning and assessment as something to plan for in advance, as the Equality Act 2010 requires of the institution, not something to fix once a problem appears.", rewrite: light, force: must, status: drafted }
  forBeneficiary: { text: "not-applicable: a duty on the course team or the institution, not a standard the student reaches", rewrite: full, force: must, status: drafted }
  author-agent-written: "Write about this as a statement without one of the five obliging words (force recorded as describes) on the course and its team, on the Equality Act duty to anticipate accessibility issues, holding for any Education Studies course the statement covers. Cite it as QAA, 2025, Education Studies Subject Benchmark Statement, para 1.15. Do not present it as a regulatory requirement, and do not turn it into an outcome a student must show. Set it beside qaa/education-studies-2025/1.13 and qaa/education-studies-2025/1.16, and where it shapes outcomes beside the honours and master's descriptors qaa/fheq-2024/4.15.b1 and qaa/fheq-2024/4.17.b1 at spine:6 and spine:7."
  author-agent-dialogue: "Raise it with a programme team or teacher who is designing, reviewing or defending the course's approach to the Equality Act duty to anticipate accessibility issues. Frame it for staff as a statement without one of the five obliging words (force recorded as describes), and ask: Which accessibility barriers in the current design were found only after a student raised them? Do not quote the issuer at length, and do not put this duty to a student as something they have to achieve."
- statement: qaa/education-studies-2025/1.16
  forPractitioner: { text: "Build accessibility into the course design itself and into planning the wider student experience, for students with specific learning needs, access requirements or neurodivergence and from every background: this is a must, not an option.", rewrite: light, force: must, status: drafted }
  forBeneficiary: { text: "not-applicable: a duty on the course team or the institution, not a standard the student reaches", rewrite: full, force: must, status: drafted }
  author-agent-written: "Write about this as a requirement worded with \"must\" on the course and its team, on accessibility in course design and the wider student experience, holding for any Education Studies course the statement covers. Cite it as QAA, 2025, Education Studies Subject Benchmark Statement, para 1.16. Do not present it as a regulatory requirement, and do not turn it into an outcome a student must show. Set it beside qaa/education-studies-2025/1.15 and qaa/education-studies-2025/1.20, and where it shapes outcomes beside the honours and master's descriptors qaa/fheq-2024/4.15.b1 and qaa/fheq-2024/4.17.b1 at spine:6 and spine:7."
  author-agent-dialogue: "Raise it with a programme team or teacher who is designing, reviewing or defending the course's approach to accessibility in course design and the wider student experience. Frame it for staff as a requirement worded with \"must\", and ask: Where in the design and approval documents is accessibility shown to have been considered? Do not quote the issuer at length, and do not put this duty to a student as something they have to achieve."
- statement: qaa/education-studies-2025/1.20
  forPractitioner: { text: "Check curriculum, content and assessment for access across cultures, disabilities, neurodivergence, identities and backgrounds, and make each assessment brief state its purpose and expectations clearly.", rewrite: light, force: should, status: drafted }
  forBeneficiary: { text: "not-applicable: a duty on the course team or the institution, not a standard the student reaches", rewrite: full, force: should, status: drafted }
  author-agent-written: "Write about this as an expectation worded with \"should\" on the course and its team, on accessible curriculum and clear assessment, holding for any Education Studies course the statement covers. Cite it as QAA, 2025, Education Studies Subject Benchmark Statement, para 1.20. Do not present it as a regulatory requirement, and do not turn it into an outcome a student must show. Set it beside qaa/education-studies-2025/1.16 and qaa/education-studies-2025/1.21, and where it shapes outcomes beside the honours and master's descriptors qaa/fheq-2024/4.15.b1 and qaa/fheq-2024/4.17.b1 at spine:6 and spine:7."
  author-agent-dialogue: "Raise it with a programme team or teacher who is designing, reviewing or defending the course's approach to accessible curriculum and clear assessment. Frame it for staff as an expectation worded with \"should\", and ask: Could a student read each assessment brief and say what it is for and what a good answer looks like? Do not quote the issuer at length, and do not put this duty to a student as something they have to achieve."
- statement: qaa/education-studies-2025/1.21
  forPractitioner: { text: "Map the barriers learners may meet before they arise, and plan responses such as support plans, joint work with institutional support and clear signposting to services.", rewrite: light, force: will, status: drafted }
  forBeneficiary: { text: "not-applicable: a duty on the course team or the institution, not a standard the student reaches", rewrite: full, force: will, status: drafted }
  author-agent-written: "Write about this as an expected outcome or feature worded with \"will\" or \"can\" on the course and its team, on anticipating barriers to learning, holding for any Education Studies course the statement covers. Cite it as QAA, 2025, Education Studies Subject Benchmark Statement, para 1.21. Do not present it as a regulatory requirement, and do not turn it into an outcome a student must show. Set it beside qaa/education-studies-2025/1.20 and qaa/education-studies-2025/1.22, and where it shapes outcomes beside the honours and master's descriptors qaa/fheq-2024/4.15.b1 and qaa/fheq-2024/4.17.b1 at spine:6 and spine:7."
  author-agent-dialogue: "Raise it with a programme team or teacher who is designing, reviewing or defending the course's approach to anticipating barriers to learning. Frame it for staff as an expected outcome or feature worded with \"will\" or \"can\", and ask: Which barriers has the team anticipated this year, and what is in place for each? Do not quote the issuer at length, and do not put this duty to a student as something they have to achieve."
- statement: qaa/education-studies-2025/1.22
  forPractitioner: { text: "Plan reasonable adjustments to teaching, learning and assessment ahead of need, so that every student has a fair route to the intended learning outcomes.", rewrite: light, force: should, status: drafted }
  forBeneficiary: { text: "not-applicable: a duty on the course team or the institution, not a standard the student reaches", rewrite: full, force: should, status: drafted }
  author-agent-written: "Write about this as an expectation worded with \"should\" on the course and its team, on anticipatory reasonable adjustments, holding for any Education Studies course the statement covers. Cite it as QAA, 2025, Education Studies Subject Benchmark Statement, para 1.22. Do not present it as a regulatory requirement, and do not turn it into an outcome a student must show. Set it beside qaa/education-studies-2025/1.21 and qaa/education-studies-2025/1.23, and where it shapes outcomes beside the honours and master's descriptors qaa/fheq-2024/4.15.b1 and qaa/fheq-2024/4.17.b1 at spine:6 and spine:7."
  author-agent-dialogue: "Raise it with a programme team or teacher who is designing, reviewing or defending the course's approach to anticipatory reasonable adjustments. Frame it for staff as an expectation worded with \"should\", and ask: Which adjustments are built into the course by default rather than arranged case by case? Do not quote the issuer at length, and do not put this duty to a student as something they have to achieve."
- statement: qaa/education-studies-2025/1.23
  forPractitioner: { text: "Review access to learning resources in person and online, including assistive technology, so that every student can use what they need for their own learning.", rewrite: light, force: should, status: drafted }
  forBeneficiary: { text: "not-applicable: a duty on the course team or the institution, not a standard the student reaches", rewrite: full, force: should, status: drafted }
  author-agent-written: "Write about this as an expectation worded with \"should\" on the course and its team, on accessibility in person and online, including assistive technology, holding for any Education Studies course the statement covers. Cite it as QAA, 2025, Education Studies Subject Benchmark Statement, para 1.23. Do not present it as a regulatory requirement, and do not turn it into an outcome a student must show. Set it beside qaa/education-studies-2025/1.22 and qaa/education-studies-2025/1.24, and where it shapes outcomes beside the honours and master's descriptors qaa/fheq-2024/4.15.b1 and qaa/fheq-2024/4.17.b1 at spine:6 and spine:7."
  author-agent-dialogue: "Raise it with a programme team or teacher who is designing, reviewing or defending the course's approach to accessibility in person and online, including assistive technology. Frame it for staff as an expectation worded with \"should\", and ask: Can every student reach every learning resource, online and on campus, with the assistive technology they use? Do not quote the issuer at length, and do not put this duty to a student as something they have to achieve."
- statement: qaa/education-studies-2025/1.24
  forPractitioner: { text: "For any placement element, plan for accessibility and well-being: offer alternatives where needed, allow a choice of assessment and make careers guidance and openings fit the needs of all students.", rewrite: light, force: should, status: drafted }
  forBeneficiary: { text: "not-applicable: a duty on the course team or the institution, not a standard the student reaches", rewrite: full, force: should, status: drafted }
  author-agent-written: "Write about this as an expectation worded with \"should\" on the course and its team, on accessibility and well-being on placements, holding for any Education Studies course the statement covers. Cite it as QAA, 2025, Education Studies Subject Benchmark Statement, para 1.24. Do not present it as a regulatory requirement, and do not turn it into an outcome a student must show. Set it beside qaa/education-studies-2025/1.23 and qaa/education-studies-2025/1.30, and where it shapes outcomes beside the honours and master's descriptors qaa/fheq-2024/4.15.b1 and qaa/fheq-2024/4.17.b1 at spine:6 and spine:7."
  author-agent-dialogue: "Raise it with a programme team or teacher who is designing, reviewing or defending the course's approach to accessibility and well-being on placements. Frame it for staff as an expectation worded with \"should\", and ask: What does a student who cannot take the standard placement do instead, and is it assessed fairly? Do not quote the issuer at length, and do not put this duty to a student as something they have to achieve."
- statement: qaa/education-studies-2025/1.30
  forPractitioner: { text: "Spread sustainability across teaching, content and assessment rather than leaving it to one module, and help students see how learning across life and settings serves a sustainable future.", rewrite: light, force: should, status: drafted }
  forBeneficiary: { text: "You will come to understand the part education plays in a sustainable future, through learning at every age and in many settings, and your course should weave sustainability through its teaching, content and assessment.", rewrite: full, force: should, status: drafted }
  author-agent-written: "Write about this as an expectation worded with \"should\" for the honours degree, at FHEQ Level 6 (FQHEIS Level 10, spine:6), on education and a sustainable future. Cite it as QAA, 2025, Education Studies Subject Benchmark Statement, para 1.30. Do not claim it is a regulatory requirement, a rung of the standards table or a standard at another level. Set it beside qaa/education-studies-2025/1.24 and qaa/education-studies-2025/1.31 and the framework descriptor qaa/fheq-2024/4.15.b4 and 4.15.b7."
  author-agent-dialogue: "Bring it up when a student asks about education and a sustainable future, or when staff check a module or outcome against it. Tell a student in plain words, as 'you', what it means for their course; for staff, frame it as an expectation worded with \"should\". Ask: Where outside a sustainability module does your course ask you to think about a sustainable future? Avoid long quotation of the issuer's text."
- statement: qaa/education-studies-2025/1.31
  forPractitioner: { text: "Help students develop habits of personal sustainability, ecological and psychological, and reflective ways of tracking and caring for their own and others' well-being.", rewrite: light, force: will, status: drafted }
  forBeneficiary: { text: "You can build your own personal sustainability, ecological and psychological, by reflecting on and looking after your own well-being and the well-being of people around you.", rewrite: full, force: will, status: drafted }
  author-agent-written: "Write about this as an expected outcome or feature worded with \"will\" or \"can\" for the honours degree, at FHEQ Level 6 (FQHEIS Level 10, spine:6), on personal sustainability and well-being. Cite it as QAA, 2025, Education Studies Subject Benchmark Statement, para 1.31. Do not claim it is a regulatory requirement, a rung of the standards table or a standard at another level. Set it beside qaa/education-studies-2025/1.30 and qaa/education-studies-2025/1.43 and the framework descriptor qaa/fheq-2024/4.15.b9.1 and 4.15.b9.3."
  author-agent-dialogue: "Bring it up when a student asks about personal sustainability and well-being, or when staff check a module or outcome against it. Tell a student in plain words, as 'you', what it means for their course; for staff, frame it as an expected outcome or feature worded with \"will\" or \"can\". Ask: What do you do to keep track of your own well-being, and how do you notice when others around you need support? Avoid long quotation of the issuer's text."
- statement: qaa/education-studies-2025/1.43
  forPractitioner: { text: "Apply the AI principles of 1.42 to your own curriculum design, assessment, recruitment and research, and consider threading AI through the programme rather than confining it to one module or stage.", rewrite: light, force: should, status: drafted }
  forBeneficiary: { text: "not-applicable: a duty on the course team or the institution, not a standard the student reaches", rewrite: full, force: should, status: drafted }
  author-agent-written: "Write about this as an expectation worded with \"should\" on the course and its team, on course teams applying the AI principles, holding for any Education Studies course the statement covers. Cite it as QAA, 2025, Education Studies Subject Benchmark Statement, para 1.43. Do not present it as a regulatory requirement, and do not turn it into an outcome a student must show. Set it beside qaa/education-studies-2025/1.31, and where it shapes outcomes beside the honours and master's descriptors qaa/fheq-2024/4.15.b1 and qaa/fheq-2024/4.17.b1 at spine:6 and spine:7."
  author-agent-dialogue: "Raise it with a programme team or teacher who is designing, reviewing or defending the course's approach to course teams applying the AI principles. Frame it for staff as an expectation worded with \"should\", and ask: Where does AI appear across the programme, and is it confined to one module? Do not quote the issuer at length, and do not put this duty to a student as something they have to achieve."
- statement: qaa/education-studies-2025/2.2
  forPractitioner: { text: "Design each level so that it builds knowledge, expertise and experience towards the threshold standards, and make the credit rules clear: students will usually need to pass every element, practical ones included.", rewrite: light, force: will, status: drafted }
  forBeneficiary: { text: "You will move from one level of study to the next, each one building your knowledge, expertise and experience towards the standards for your degree, and you will usually need to pass every part, practical work included.", rewrite: full, force: will, status: drafted }
  author-agent-written: "Write about this as an expected outcome or feature worded with \"will\" or \"can\" for the honours degree and the integrated master's, at FHEQ Level 6 (FQHEIS Level 10, spine:6), on progression through the levels to the threshold. Cite it as QAA, 2025, Education Studies Subject Benchmark Statement, para 2.2. Do not claim it is a regulatory requirement, a rung of the standards table or a standard at another level. Set it beside qaa/education-studies-2025/2.3 and the framework descriptor qaa/fheq-2024/4.15.b1 and 4.15.b9.3."
  author-agent-dialogue: "Bring it up when a student asks about progression through the levels to the threshold, or when staff check a module or outcome against it. Tell a student in plain words, as 'you', what it means for their course; for staff, frame it as an expected outcome or feature worded with \"will\" or \"can\". Ask: How does each year of the course build towards the final standards, and where is the practical work assessed? Avoid long quotation of the issuer's text."
- statement: qaa/education-studies-2025/2.3
  forPractitioner: { text: "Prepare students so that those with a second-class degree or better are ready for postgraduate study in education or a related field, and advise them that each postgraduate course sets its own entry rules.", rewrite: light, force: must, status: drafted }
  forBeneficiary: { text: "If you graduate with at least a second-class degree, you would be expected to be ready for postgraduate study in education or a related subject, though each postgraduate course sets its own entry rules.", rewrite: full, force: must, status: drafted }
  author-agent-written: "Write about this as a statement without one of the five obliging words (force recorded as describes) for the honours degree, at FHEQ Level 6 (FQHEIS Level 10, spine:6), on readiness for postgraduate study. Cite it as QAA, 2025, Education Studies Subject Benchmark Statement, para 2.3. Do not claim it is a regulatory requirement, a rung of the standards table or a standard at another level. Set it beside qaa/education-studies-2025/2.2 and qaa/education-studies-2025/2.4 and the framework descriptor qaa/fheq-2024/4.15.b1 and 4.15.b9.3."
  author-agent-dialogue: "Bring it up when a student asks about readiness for postgraduate study, or when staff check a module or outcome against it. Tell a student in plain words, as 'you', what it means for their course; for staff, frame it as a statement without one of the five obliging words (force recorded as describes). Ask: What would you need to show a postgraduate admissions tutor about your readiness for further study? Avoid long quotation of the issuer's text."
- statement: qaa/education-studies-2025/2.4
  forPractitioner: { text: "In a joint or combined design, secure the core subject-specific and generic skills of Education Studies, and use the partner subject to add skills and to open up interdisciplinary study.", rewrite: light, force: will, status: drafted }
  forBeneficiary: { text: "If you study Education Studies alongside another subject, you will gain its core subject and general skills, add others from your second subject and can explore where the two meet.", rewrite: full, force: will, status: drafted }
  author-agent-written: "Write about this as an expected outcome or feature worded with \"will\" or \"can\" for the honours degree, at FHEQ Level 6 (FQHEIS Level 10, spine:6), on core skills in joint and combined degrees. Cite it as QAA, 2025, Education Studies Subject Benchmark Statement, para 2.4. Do not claim it is a regulatory requirement, a rung of the standards table or a standard at another level. Set it beside qaa/education-studies-2025/2.3 and qaa/education-studies-2025/2.9 and the framework descriptor qaa/fheq-2024/4.15.b1 and 4.15.b9.3."
  author-agent-dialogue: "Bring it up when a student asks about core skills in joint and combined degrees, or when staff check a module or outcome against it. Tell a student in plain words, as 'you', what it means for their course; for staff, frame it as an expected outcome or feature worded with \"will\" or \"can\". Ask: Which core Education Studies skills does the joint course secure, and where does the partner subject add to them? Avoid long quotation of the issuer's text."
- statement: qaa/education-studies-2025/2.9
  forPractitioner: { text: "Include the student voice in every periodic review, and use external reference points, this statement among them, to test the course against sector norms.", rewrite: light, force: will, status: drafted }
  forBeneficiary: { text: "not-applicable: a duty on the course team or the institution, not a standard the student reaches", rewrite: full, force: will, status: drafted }
  author-agent-written: "Write about this as an expected outcome or feature worded with \"will\" or \"can\" on the course and its team, on periodic review and the student voice, holding for any Education Studies course the statement covers. Cite it as QAA, 2025, Education Studies Subject Benchmark Statement, para 2.9. Do not present it as a regulatory requirement, and do not turn it into an outcome a student must show. Set it beside qaa/education-studies-2025/2.4 and qaa/education-studies-2025/2.10, and where it shapes outcomes beside the honours and master's descriptors qaa/fheq-2024/4.15.b1 and qaa/fheq-2024/4.17.b1 at spine:6 and spine:7."
  author-agent-dialogue: "Raise it with a programme team or teacher who is designing, reviewing or defending the course's approach to periodic review and the student voice. Frame it for staff as an expected outcome or feature worded with \"will\" or \"can\", and ask: How did students' views shape the last periodic review, and which external reference points were used? Do not quote the issuer at length, and do not put this duty to a student as something they have to achieve."
- statement: qaa/education-studies-2025/2.10
  forPractitioner: { text: "Bring external reviewers into periodic review so that proposed changes get an independent view and the course is shown to meet threshold standards with content fit for the subject.", rewrite: light, force: will, status: drafted }
  forBeneficiary: { text: "not-applicable: a duty on the course team or the institution, not a standard the student reaches", rewrite: full, force: will, status: drafted }
  author-agent-written: "Write about this as an expected outcome or feature worded with \"will\" or \"can\" on the course and its team, on external reviewers in periodic review, holding for any Education Studies course the statement covers. Cite it as QAA, 2025, Education Studies Subject Benchmark Statement, para 2.10. Do not present it as a regulatory requirement, and do not turn it into an outcome a student must show. Set it beside qaa/education-studies-2025/2.9, and where it shapes outcomes beside the honours and master's descriptors qaa/fheq-2024/4.15.b1 and qaa/fheq-2024/4.17.b1 at spine:6 and spine:7."
  author-agent-dialogue: "Raise it with a programme team or teacher who is designing, reviewing or defending the course's approach to external reviewers in periodic review. Frame it for staff as an expected outcome or feature worded with \"will\" or \"can\", and ask: What did the external reviewer say about threshold standards and subject content at the last review? Do not quote the issuer at length, and do not put this duty to a student as something they have to achieve."
- statement: qaa/education-studies-2025/3.9
  forPractitioner: { text: "Make the transversal knowledge and skills explicit in the course, since students will build a broad set of them that carry across jobs, tasks and settings.", rewrite: light, force: will, status: drafted }
  forBeneficiary: { text: "Because Education Studies draws on many disciplines, you will build a broad set of knowledge and skills that carry across jobs, tasks and workplaces.", rewrite: full, force: will, status: drafted }
  author-agent-written: "Write about this as an expected outcome or feature worded with \"will\" or \"can\" for the honours degree, at FHEQ Level 6 (FQHEIS Level 10, spine:6), on transversal knowledge and skills. Cite it as QAA, 2025, Education Studies Subject Benchmark Statement, para 3.9. Do not claim it is a regulatory requirement, a rung of the standards table or a standard at another level. Set it beside qaa/education-studies-2025/3.10.b1 and the framework descriptor qaa/fheq-2024/4.15.b9.1 and 4.15.b9.3."
  author-agent-dialogue: "Bring it up when a student asks about transversal knowledge and skills, or when staff check a module or outcome against it. Tell a student in plain words, as 'you', what it means for their course; for staff, frame it as an expected outcome or feature worded with \"will\" or \"can\". Ask: Which of your skills from this course would you use in a job outside education? Avoid long quotation of the issuer's text."
- statement: qaa/education-studies-2025/3.10.b1
  forPractitioner: { text: "Consider where the transversal curriculum lets students handle numbers with confidence, and interpret and analyse data where it fits, and how that is taught and assessed.", rewrite: light, force: should, status: drafted }
  forBeneficiary: { text: "Your course should give you chances to handle numbers with confidence, and interpret and analyse data where it fits.", rewrite: full, force: should, status: drafted }
  author-agent-written: "Write about this as an expectation worded with \"should\" for the honours degree, at FHEQ Level 6 (FQHEIS Level 10, spine:6), on numeracy and data. Cite it as QAA, 2025, Education Studies Subject Benchmark Statement, para 3.10, bullet 1. Do not claim it is a regulatory requirement, a rung of the standards table or a standard at another level. Set it beside qaa/education-studies-2025/3.9 and qaa/education-studies-2025/3.10.b2 and the framework descriptor qaa/fheq-2024/4.15.b9.1 and 4.15.b9.3."
  author-agent-dialogue: "Bring it up when a student asks about numeracy and data, or when staff check a module or outcome against it. Tell a student in plain words, as 'you', what it means for their course; for staff, frame it as an expectation worded with \"should\". Ask: Where have you had to make sense of numbers or data in your studies so far? Avoid long quotation of the issuer's text."
- statement: qaa/education-studies-2025/3.10.b2
  forPractitioner: { text: "Consider where the transversal curriculum lets students be honest and answerable, owning the results of their own actions, and how that is taught and assessed.", rewrite: light, force: should, status: drafted }
  forBeneficiary: { text: "Your course should give you chances to be honest and answerable, owning the results of your own actions.", rewrite: full, force: should, status: drafted }
  author-agent-written: "Write about this as an expectation worded with \"should\" for the honours degree, at FHEQ Level 6 (FQHEIS Level 10, spine:6), on accountability and honesty. Cite it as QAA, 2025, Education Studies Subject Benchmark Statement, para 3.10, bullet 2. Do not claim it is a regulatory requirement, a rung of the standards table or a standard at another level. Set it beside qaa/education-studies-2025/3.10.b1 and qaa/education-studies-2025/3.10.b3 and the framework descriptor qaa/fheq-2024/4.15.b9.1 and 4.15.b9.3."
  author-agent-dialogue: "Bring it up when a student asks about accountability and honesty, or when staff check a module or outcome against it. Tell a student in plain words, as 'you', what it means for their course; for staff, frame it as an expectation worded with \"should\". Ask: When did you last have to own a mistake, and what did you do next? Avoid long quotation of the issuer's text."
- statement: qaa/education-studies-2025/3.10.b3
  forPractitioner: { text: "Consider where the transversal curriculum lets students communicate for varied ends, such as describing, explaining, persuading, judging and summing up, and how that is taught and assessed.", rewrite: light, force: should, status: drafted }
  forBeneficiary: { text: "Your course should give you chances to communicate for varied ends, such as describing, explaining, persuading, judging and summing up.", rewrite: full, force: should, status: drafted }
  author-agent-written: "Write about this as an expectation worded with \"should\" for the honours degree, at FHEQ Level 6 (FQHEIS Level 10, spine:6), on communicating for different purposes. Cite it as QAA, 2025, Education Studies Subject Benchmark Statement, para 3.10, bullet 3. Do not claim it is a regulatory requirement, a rung of the standards table or a standard at another level. Set it beside qaa/education-studies-2025/3.10.b2 and qaa/education-studies-2025/3.10.b4 and the framework descriptor qaa/fheq-2024/4.15.b9.1 and 4.15.b9.3."
  author-agent-dialogue: "Bring it up when a student asks about communicating for different purposes, or when staff check a module or outcome against it. Tell a student in plain words, as 'you', what it means for their course; for staff, frame it as an expectation worded with \"should\". Ask: Which kind of writing or speaking do you find hardest: explaining, persuading or summing up? Avoid long quotation of the issuer's text."
- statement: qaa/education-studies-2025/3.10.b4
  forPractitioner: { text: "Consider where the transversal curriculum lets students understand, judge critically and use data in many settings, and how that is taught and assessed.", rewrite: light, force: should, status: drafted }
  forBeneficiary: { text: "Your course should give you chances to understand, judge critically and use data in many settings.", rewrite: full, force: should, status: drafted }
  author-agent-written: "Write about this as an expectation worded with \"should\" for the honours degree, at FHEQ Level 6 (FQHEIS Level 10, spine:6), on understanding and using data. Cite it as QAA, 2025, Education Studies Subject Benchmark Statement, para 3.10, bullet 4. Do not claim it is a regulatory requirement, a rung of the standards table or a standard at another level. Set it beside qaa/education-studies-2025/3.10.b3 and qaa/education-studies-2025/3.10.b5 and the framework descriptor qaa/fheq-2024/4.15.b9.1 and 4.15.b9.3."
  author-agent-dialogue: "Bring it up when a student asks about understanding and using data, or when staff check a module or outcome against it. Tell a student in plain words, as 'you', what it means for their course; for staff, frame it as an expectation worded with \"should\". Ask: What data have you used in an assignment, and how did you judge whether to trust it? Avoid long quotation of the issuer's text."
- statement: qaa/education-studies-2025/3.10.b5
  forPractitioner: { text: "Consider where the transversal curriculum lets students judge sources critically for how relevant and useful they are, and how that is taught and assessed.", rewrite: light, force: should, status: drafted }
  forBeneficiary: { text: "Your course should give you chances to judge sources critically for how relevant and useful they are.", rewrite: full, force: should, status: drafted }
  author-agent-written: "Write about this as an expectation worded with \"should\" for the honours degree, at FHEQ Level 6 (FQHEIS Level 10, spine:6), on judging sources. Cite it as QAA, 2025, Education Studies Subject Benchmark Statement, para 3.10, bullet 5. Do not claim it is a regulatory requirement, a rung of the standards table or a standard at another level. Set it beside qaa/education-studies-2025/3.10.b4 and qaa/education-studies-2025/3.10.b6 and the framework descriptor qaa/fheq-2024/4.15.b9.1 and 4.15.b9.3."
  author-agent-dialogue: "Bring it up when a student asks about judging sources, or when staff check a module or outcome against it. Tell a student in plain words, as 'you', what it means for their course; for staff, frame it as an expectation worded with \"should\". Ask: How do you decide whether a source is worth using? Avoid long quotation of the issuer's text."
- statement: qaa/education-studies-2025/3.10.b6
  forPractitioner: { text: "Consider where the transversal curriculum lets students show global competence and intercultural understanding, alert to other people's needs, backgrounds and experiences, and how that is taught and assessed.", rewrite: light, force: should, status: drafted }
  forBeneficiary: { text: "Your course should give you chances to show global competence and intercultural understanding, alert to other people's needs, backgrounds and experiences.", rewrite: full, force: should, status: drafted }
  author-agent-written: "Write about this as an expectation worded with \"should\" for the honours degree, at FHEQ Level 6 (FQHEIS Level 10, spine:6), on global competence and intercultural understanding. Cite it as QAA, 2025, Education Studies Subject Benchmark Statement, para 3.10, bullet 6. Do not claim it is a regulatory requirement, a rung of the standards table or a standard at another level. Set it beside qaa/education-studies-2025/3.10.b5 and qaa/education-studies-2025/3.10.b7 and the framework descriptor qaa/fheq-2024/4.15.b9.1 and 4.15.b9.3."
  author-agent-dialogue: "Bring it up when a student asks about global competence and intercultural understanding, or when staff check a module or outcome against it. Tell a student in plain words, as 'you', what it means for their course; for staff, frame it as an expectation worded with \"should\". Ask: When has learning about another culture changed how you see education? Avoid long quotation of the issuer's text."
- statement: qaa/education-studies-2025/3.10.b7
  forPractitioner: { text: "Consider where the transversal curriculum lets students show empathy by connecting with others and listening actively, and how that is taught and assessed.", rewrite: light, force: should, status: drafted }
  forBeneficiary: { text: "Your course should give you chances to show empathy by connecting with others and listening actively.", rewrite: full, force: should, status: drafted }
  author-agent-written: "Write about this as an expectation worded with \"should\" for the honours degree, at FHEQ Level 6 (FQHEIS Level 10, spine:6), on empathy and active listening. Cite it as QAA, 2025, Education Studies Subject Benchmark Statement, para 3.10, bullet 7. Do not claim it is a regulatory requirement, a rung of the standards table or a standard at another level. Set it beside qaa/education-studies-2025/3.10.b6 and qaa/education-studies-2025/3.10.b8 and the framework descriptor qaa/fheq-2024/4.15.b9.1 and 4.15.b9.3."
  author-agent-dialogue: "Bring it up when a student asks about empathy and active listening, or when staff check a module or outcome against it. Tell a student in plain words, as 'you', what it means for their course; for staff, frame it as an expectation worded with \"should\". Ask: How do you show someone you are really listening? Avoid long quotation of the issuer's text."
- statement: qaa/education-studies-2025/3.10.b8
  forPractitioner: { text: "Consider where the transversal curriculum lets students debate, negotiate and persuade in ways that are respectful, helpful and fitting, and how that is taught and assessed.", rewrite: light, force: should, status: drafted }
  forBeneficiary: { text: "Your course should give you chances to debate, negotiate and persuade in ways that are respectful, helpful and fitting.", rewrite: full, force: should, status: drafted }
  author-agent-written: "Write about this as an expectation worded with \"should\" for the honours degree, at FHEQ Level 6 (FQHEIS Level 10, spine:6), on respectful debate and negotiation. Cite it as QAA, 2025, Education Studies Subject Benchmark Statement, para 3.10, bullet 8. Do not claim it is a regulatory requirement, a rung of the standards table or a standard at another level. Set it beside qaa/education-studies-2025/3.10.b7 and qaa/education-studies-2025/3.10.b9 and the framework descriptor qaa/fheq-2024/4.15.b9.1 and 4.15.b9.3."
  author-agent-dialogue: "Bring it up when a student asks about respectful debate and negotiation, or when staff check a module or outcome against it. Tell a student in plain words, as 'you', what it means for their course; for staff, frame it as an expectation worded with \"should\". Ask: When did you last change someone's mind, or have yours changed, in a respectful debate? Avoid long quotation of the issuer's text."
- statement: qaa/education-studies-2025/3.10.b9
  forPractitioner: { text: "Consider where the transversal curriculum lets students communicate skilfully in spoken, non-verbal, visual and written forms, with an eye to audience and medium, and how that is taught and assessed.", rewrite: light, force: should, status: drafted }
  forBeneficiary: { text: "Your course should give you chances to communicate skilfully in spoken, non-verbal, visual and written forms, with an eye to audience and medium.", rewrite: full, force: should, status: drafted }
  author-agent-written: "Write about this as an expectation worded with \"should\" for the honours degree, at FHEQ Level 6 (FQHEIS Level 10, spine:6), on skilled communication across modes. Cite it as QAA, 2025, Education Studies Subject Benchmark Statement, para 3.10, bullet 9. Do not claim it is a regulatory requirement, a rung of the standards table or a standard at another level. Set it beside qaa/education-studies-2025/3.10.b8 and qaa/education-studies-2025/3.10.b10 and the framework descriptor qaa/fheq-2024/4.15.b9.1 and 4.15.b9.3."
  author-agent-dialogue: "Bring it up when a student asks about skilled communication across modes, or when staff check a module or outcome against it. Tell a student in plain words, as 'you', what it means for their course; for staff, frame it as an expectation worded with \"should\". Ask: How do you change the way you communicate for a different audience? Avoid long quotation of the issuer's text."
- statement: qaa/education-studies-2025/3.10.b10
  forPractitioner: { text: "Consider where the transversal curriculum lets students practise self-care and resilience and look after their own well-being in a field bound up with wider society, and how that is taught and assessed.", rewrite: light, force: should, status: drafted }
  forBeneficiary: { text: "Your course should give you chances to practise self-care and resilience and look after your own well-being in a field bound up with wider society.", rewrite: full, force: should, status: drafted }
  author-agent-written: "Write about this as an expectation worded with \"should\" for the honours degree, at FHEQ Level 6 (FQHEIS Level 10, spine:6), on self-care and resilience. Cite it as QAA, 2025, Education Studies Subject Benchmark Statement, para 3.10, bullet 10. Do not claim it is a regulatory requirement, a rung of the standards table or a standard at another level. Set it beside qaa/education-studies-2025/3.10.b9 and qaa/education-studies-2025/3.10.b11 and the framework descriptor qaa/fheq-2024/4.15.b9.1 and 4.15.b9.3."
  author-agent-dialogue: "Bring it up when a student asks about self-care and resilience, or when staff check a module or outcome against it. Tell a student in plain words, as 'you', what it means for their course; for staff, frame it as an expectation worded with \"should\". Ask: What do you do to stay well and resilient when the work is heavy? Avoid long quotation of the issuer's text."
- statement: qaa/education-studies-2025/3.10.b11
  forPractitioner: { text: "Consider where the transversal curriculum lets students reflect, be reflexive and build critical self-awareness, and how that is taught and assessed.", rewrite: light, force: should, status: drafted }
  forBeneficiary: { text: "Your course should give you chances to reflect, be reflexive and build critical self-awareness.", rewrite: full, force: should, status: drafted }
  author-agent-written: "Write about this as an expectation worded with \"should\" for the honours degree, at FHEQ Level 6 (FQHEIS Level 10, spine:6), on reflection and reflexivity. Cite it as QAA, 2025, Education Studies Subject Benchmark Statement, para 3.10, bullet 11. Do not claim it is a regulatory requirement, a rung of the standards table or a standard at another level. Set it beside qaa/education-studies-2025/3.10.b10 and qaa/education-studies-2025/3.10.b12 and the framework descriptor qaa/fheq-2024/4.15.b9.1 and 4.15.b9.3."
  author-agent-dialogue: "Bring it up when a student asks about reflection and reflexivity, or when staff check a module or outcome against it. Tell a student in plain words, as 'you', what it means for their course; for staff, frame it as an expectation worded with \"should\". Ask: What has reflection on your own learning shown you this year? Avoid long quotation of the issuer's text."
- statement: qaa/education-studies-2025/3.10.b12
  forPractitioner: { text: "Consider where the transversal curriculum lets students help bring about inclusion and accessibility, and how that is taught and assessed.", rewrite: light, force: should, status: drafted }
  forBeneficiary: { text: "Your course should give you chances to help bring about inclusion and accessibility.", rewrite: full, force: should, status: drafted }
  author-agent-written: "Write about this as an expectation worded with \"should\" for the honours degree, at FHEQ Level 6 (FQHEIS Level 10, spine:6), on inclusion and accessibility. Cite it as QAA, 2025, Education Studies Subject Benchmark Statement, para 3.10, bullet 12. Do not claim it is a regulatory requirement, a rung of the standards table or a standard at another level. Set it beside qaa/education-studies-2025/3.10.b11 and qaa/education-studies-2025/3.10.b13 and the framework descriptor qaa/fheq-2024/4.15.b9.1 and 4.15.b9.3."
  author-agent-dialogue: "Bring it up when a student asks about inclusion and accessibility, or when staff check a module or outcome against it. Tell a student in plain words, as 'you', what it means for their course; for staff, frame it as an expectation worded with \"should\". Ask: What have you done to make a learning setting more inclusive or accessible? Avoid long quotation of the issuer's text."
- statement: qaa/education-studies-2025/3.10.b13
  forPractitioner: { text: "Consider where the transversal curriculum lets students spot problems and work out solutions using creative and enterprising thinking, and how that is taught and assessed.", rewrite: light, force: should, status: drafted }
  forBeneficiary: { text: "Your course should give you chances to spot problems and work out solutions using creative and enterprising thinking.", rewrite: full, force: should, status: drafted }
  author-agent-written: "Write about this as an expectation worded with \"should\" for the honours degree, at FHEQ Level 6 (FQHEIS Level 10, spine:6), on creative problem-solving and enterprise. Cite it as QAA, 2025, Education Studies Subject Benchmark Statement, para 3.10, bullet 13. Do not claim it is a regulatory requirement, a rung of the standards table or a standard at another level. Set it beside qaa/education-studies-2025/3.10.b12 and qaa/education-studies-2025/3.10.b14 and the framework descriptor qaa/fheq-2024/4.15.b9.1 and 4.15.b9.3."
  author-agent-dialogue: "Bring it up when a student asks about creative problem-solving and enterprise, or when staff check a module or outcome against it. Tell a student in plain words, as 'you', what it means for their course; for staff, frame it as an expectation worded with \"should\". Ask: Which problem have you solved by thinking creatively rather than following a set method? Avoid long quotation of the issuer's text."
- statement: qaa/education-studies-2025/3.10.b14
  forPractitioner: { text: "Consider where the transversal curriculum lets students raise their own learning performance by seeing what to develop and how to get there, and how that is taught and assessed.", rewrite: light, force: should, status: drafted }
  forBeneficiary: { text: "Your course should give you chances to raise your own learning performance by seeing what to develop and how to get there.", rewrite: full, force: should, status: drafted }
  author-agent-written: "Write about this as an expectation worded with \"should\" for the honours degree, at FHEQ Level 6 (FQHEIS Level 10, spine:6), on improving own learning. Cite it as QAA, 2025, Education Studies Subject Benchmark Statement, para 3.10, bullet 14. Do not claim it is a regulatory requirement, a rung of the standards table or a standard at another level. Set it beside qaa/education-studies-2025/3.10.b13 and qaa/education-studies-2025/3.10.b15 and the framework descriptor qaa/fheq-2024/4.15.b9.1 and 4.15.b9.3."
  author-agent-dialogue: "Bring it up when a student asks about improving own learning, or when staff check a module or outcome against it. Tell a student in plain words, as 'you', what it means for their course; for staff, frame it as an expectation worded with \"should\". Ask: Which area of your learning are you working to improve, and how? Avoid long quotation of the issuer's text."
- statement: qaa/education-studies-2025/3.10.b15
  forPractitioner: { text: "Consider where the transversal curriculum lets students keep a professional attitude and treat colleagues at work with respect, and how that is taught and assessed.", rewrite: light, force: should, status: drafted }
  forBeneficiary: { text: "Your course should give you chances to keep a professional attitude and treat colleagues at work with respect.", rewrite: full, force: should, status: drafted }
  author-agent-written: "Write about this as an expectation worded with \"should\" for the honours degree, at FHEQ Level 6 (FQHEIS Level 10, spine:6), on professional attitude. Cite it as QAA, 2025, Education Studies Subject Benchmark Statement, para 3.10, bullet 15. Do not claim it is a regulatory requirement, a rung of the standards table or a standard at another level. Set it beside qaa/education-studies-2025/3.10.b14 and qaa/education-studies-2025/3.10.b16 and the framework descriptor qaa/fheq-2024/4.15.b9.1 and 4.15.b9.3."
  author-agent-dialogue: "Bring it up when a student asks about professional attitude, or when staff check a module or outcome against it. Tell a student in plain words, as 'you', what it means for their course; for staff, frame it as an expectation worded with \"should\". Ask: What does acting professionally mean for you on placement or in group work? Avoid long quotation of the issuer's text."
- statement: qaa/education-studies-2025/3.10.b16
  forPractitioner: { text: "Consider where the transversal curriculum lets students organise and manage information so that files, notes and documents can be found again later, and how that is taught and assessed.", rewrite: light, force: should, status: drafted }
  forBeneficiary: { text: "Your course should give you chances to organise and manage information so that files, notes and documents can be found again later.", rewrite: full, force: should, status: drafted }
  author-agent-written: "Write about this as an expectation worded with \"should\" for the honours degree, at FHEQ Level 6 (FQHEIS Level 10, spine:6), on managing information. Cite it as QAA, 2025, Education Studies Subject Benchmark Statement, para 3.10, bullet 16. Do not claim it is a regulatory requirement, a rung of the standards table or a standard at another level. Set it beside qaa/education-studies-2025/3.10.b15 and qaa/education-studies-2025/3.10.b17 and the framework descriptor qaa/fheq-2024/4.15.b9.1 and 4.15.b9.3."
  author-agent-dialogue: "Bring it up when a student asks about managing information, or when staff check a module or outcome against it. Tell a student in plain words, as 'you', what it means for their course; for staff, frame it as an expectation worded with \"should\". Ask: Could you find your notes from last term's module in under a minute? Avoid long quotation of the issuer's text."
- statement: qaa/education-studies-2025/3.10.b17
  forPractitioner: { text: "Consider where the transversal curriculum lets students use initiative where it fits, knowing the limits of their role and their freedom to act, and how that is taught and assessed.", rewrite: light, force: should, status: drafted }
  forBeneficiary: { text: "Your course should give you chances to use initiative where it fits, knowing the limits of your role and your freedom to act.", rewrite: full, force: should, status: drafted }
  author-agent-written: "Write about this as an expectation worded with \"should\" for the honours degree, at FHEQ Level 6 (FQHEIS Level 10, spine:6), on initiative and autonomy. Cite it as QAA, 2025, Education Studies Subject Benchmark Statement, para 3.10, bullet 17. Do not claim it is a regulatory requirement, a rung of the standards table or a standard at another level. Set it beside qaa/education-studies-2025/3.10.b16 and qaa/education-studies-2025/3.10.b18 and the framework descriptor qaa/fheq-2024/4.15.b9.1 and 4.15.b9.3."
  author-agent-dialogue: "Bring it up when a student asks about initiative and autonomy, or when staff check a module or outcome against it. Tell a student in plain words, as 'you', what it means for their course; for staff, frame it as an expectation worded with \"should\". Ask: When have you taken the initiative, and how did you know it was your call to make? Avoid long quotation of the issuer's text."
- statement: qaa/education-studies-2025/3.10.b18
  forPractitioner: { text: "Consider where the transversal curriculum lets students accept responsibility, answer for their actions and give a lead, and how that is taught and assessed.", rewrite: light, force: should, status: drafted }
  forBeneficiary: { text: "Your course should give you chances to accept responsibility, answer for your actions and give a lead.", rewrite: full, force: should, status: drafted }
  author-agent-written: "Write about this as an expectation worded with \"should\" for the honours degree, at FHEQ Level 6 (FQHEIS Level 10, spine:6), on responsibility and leadership. Cite it as QAA, 2025, Education Studies Subject Benchmark Statement, para 3.10, bullet 18. Do not claim it is a regulatory requirement, a rung of the standards table or a standard at another level. Set it beside qaa/education-studies-2025/3.10.b17 and qaa/education-studies-2025/3.10.b19 and the framework descriptor qaa/fheq-2024/4.15.b9.1 and 4.15.b9.3."
  author-agent-dialogue: "Bring it up when a student asks about responsibility and leadership, or when staff check a module or outcome against it. Tell a student in plain words, as 'you', what it means for their course; for staff, frame it as an expectation worded with \"should\". Ask: When have you taken the lead and answered for the outcome? Avoid long quotation of the issuer's text."
- statement: qaa/education-studies-2025/3.10.b19
  forPractitioner: { text: "Consider where the transversal curriculum lets students ask critical questions in practice, building their own line of enquiry to reach critical judgements, and how that is taught and assessed.", rewrite: light, force: should, status: drafted }
  forBeneficiary: { text: "Your course should give you chances to ask critical questions in practice, building your own line of enquiry to reach critical judgements.", rewrite: full, force: should, status: drafted }
  author-agent-written: "Write about this as an expectation worded with \"should\" for the honours degree, at FHEQ Level 6 (FQHEIS Level 10, spine:6), on critical questioning in practice. Cite it as QAA, 2025, Education Studies Subject Benchmark Statement, para 3.10, bullet 19. Do not claim it is a regulatory requirement, a rung of the standards table or a standard at another level. Set it beside qaa/education-studies-2025/3.10.b18 and qaa/education-studies-2025/3.10.b20 and the framework descriptor qaa/fheq-2024/4.15.b9.1 and 4.15.b9.3."
  author-agent-dialogue: "Bring it up when a student asks about critical questioning in practice, or when staff check a module or outcome against it. Tell a student in plain words, as 'you', what it means for their course; for staff, frame it as an expectation worded with \"should\". Ask: What question would you ask to test a practice you observed? Avoid long quotation of the issuer's text."
- statement: qaa/education-studies-2025/3.10.b20
  forPractitioner: { text: "Consider where the transversal curriculum lets students use digital and social media where suitable, and how that is taught and assessed.", rewrite: light, force: should, status: drafted }
  forBeneficiary: { text: "Your course should give you chances to use digital and social media where suitable.", rewrite: full, force: should, status: drafted }
  author-agent-written: "Write about this as an expectation worded with \"should\" for the honours degree, at FHEQ Level 6 (FQHEIS Level 10, spine:6), on digital and social media. Cite it as QAA, 2025, Education Studies Subject Benchmark Statement, para 3.10, bullet 20. Do not claim it is a regulatory requirement, a rung of the standards table or a standard at another level. Set it beside qaa/education-studies-2025/3.10.b19 and qaa/education-studies-2025/3.10.b21 and the framework descriptor qaa/fheq-2024/4.15.b9.1 and 4.15.b9.3."
  author-agent-dialogue: "Bring it up when a student asks about digital and social media, or when staff check a module or outcome against it. Tell a student in plain words, as 'you', what it means for their course; for staff, frame it as an expectation worded with \"should\". Ask: How do you decide which digital or social media tools fit a task? Avoid long quotation of the issuer's text."
- statement: qaa/education-studies-2025/3.10.b21
  forPractitioner: { text: "Consider where the transversal curriculum lets students draw on evidence-informed practice to form a reasoned view, and how that is taught and assessed.", rewrite: light, force: should, status: drafted }
  forBeneficiary: { text: "Your course should give you chances to draw on evidence-informed practice to form a reasoned view.", rewrite: full, force: should, status: drafted }
  author-agent-written: "Write about this as an expectation worded with \"should\" for the honours degree, at FHEQ Level 6 (FQHEIS Level 10, spine:6), on evidence-informed views. Cite it as QAA, 2025, Education Studies Subject Benchmark Statement, para 3.10, bullet 21. Do not claim it is a regulatory requirement, a rung of the standards table or a standard at another level. Set it beside qaa/education-studies-2025/3.10.b20 and qaa/education-studies-2025/3.10.b22 and the framework descriptor qaa/fheq-2024/4.15.b9.1 and 4.15.b9.3."
  author-agent-dialogue: "Bring it up when a student asks about evidence-informed views, or when staff check a module or outcome against it. Tell a student in plain words, as 'you', what it means for their course; for staff, frame it as an expectation worded with \"should\". Ask: What evidence lies behind a view you hold about education? Avoid long quotation of the issuer's text."
- statement: qaa/education-studies-2025/3.10.b22
  forPractitioner: { text: "Consider where the transversal curriculum lets students use AI critically and ethically, and how that is taught and assessed.", rewrite: light, force: should, status: drafted }
  forBeneficiary: { text: "Your course should give you chances to use AI critically and ethically.", rewrite: full, force: should, status: drafted }
  author-agent-written: "Write about this as an expectation worded with \"should\" for the honours degree, at FHEQ Level 6 (FQHEIS Level 10, spine:6), on critical and ethical use of AI. Cite it as QAA, 2025, Education Studies Subject Benchmark Statement, para 3.10, bullet 22. Do not claim it is a regulatory requirement, a rung of the standards table or a standard at another level. Set it beside qaa/education-studies-2025/3.10.b21 and qaa/education-studies-2025/3.10.b23 and the framework descriptor qaa/fheq-2024/4.15.b9.1 and 4.15.b9.3."
  author-agent-dialogue: "Bring it up when a student asks about critical and ethical use of AI, or when staff check a module or outcome against it. Tell a student in plain words, as 'you', what it means for their course; for staff, frame it as an expectation worded with \"should\". Ask: When is it right to use AI in your work, and when not? Avoid long quotation of the issuer's text."
- statement: qaa/education-studies-2025/3.10.b23
  forPractitioner: { text: "Consider where the transversal curriculum lets students work with others collaboratively, and how that is taught and assessed.", rewrite: light, force: should, status: drafted }
  forBeneficiary: { text: "Your course should give you chances to work with others collaboratively.", rewrite: full, force: should, status: drafted }
  author-agent-written: "Write about this as an expectation worded with \"should\" for the honours degree, at FHEQ Level 6 (FQHEIS Level 10, spine:6), on collaboration. Cite it as QAA, 2025, Education Studies Subject Benchmark Statement, para 3.10, bullet 23. Do not claim it is a regulatory requirement, a rung of the standards table or a standard at another level. Set it beside qaa/education-studies-2025/3.10.b22 and qaa/education-studies-2025/3.16 and the framework descriptor qaa/fheq-2024/4.15.b9.1 and 4.15.b9.3."
  author-agent-dialogue: "Bring it up when a student asks about collaboration, or when staff check a module or outcome against it. Tell a student in plain words, as 'you', what it means for their course; for staff, frame it as an expectation worded with \"should\". Ask: What made your last piece of group work succeed or struggle? Avoid long quotation of the issuer's text."
- statement: qaa/education-studies-2025/3.16
  forPractitioner: { text: "Map each assessment to the outcomes, objectives or competencies it tests, and check that the strategy as a whole covers the skills, knowledge and values the subject asks for.", rewrite: light, force: should, status: drafted }
  forBeneficiary: { text: "not-applicable: a duty on the course team or the institution, not a standard the student reaches", rewrite: full, force: should, status: drafted }
  author-agent-written: "Write about this as an expectation worded with \"should\" on the course and its team, on aligning assessment with outcomes, holding for any Education Studies course the statement covers. Cite it as QAA, 2025, Education Studies Subject Benchmark Statement, para 3.16. Do not present it as a regulatory requirement, and do not turn it into an outcome a student must show. Set it beside qaa/education-studies-2025/3.10.b23, and where it shapes outcomes beside the honours and master's descriptors qaa/fheq-2024/4.15.b1 and qaa/fheq-2024/4.17.b1 at spine:6 and spine:7."
  author-agent-dialogue: "Raise it with a programme team or teacher who is designing, reviewing or defending the course's approach to aligning assessment with outcomes. Frame it for staff as an expectation worded with \"should\", and ask: For each assessment, which outcomes does it test, and is any outcome left untested? Do not quote the issuer at length, and do not put this duty to a student as something they have to achieve."
- statement: qaa/education-studies-2025/4.1
  forPractitioner: { text: "If Education Studies is one part of a degree, state in the course documents how far the standards should be met, since the statement leaves that to the institution.", rewrite: light, force: should, status: drafted }
  forBeneficiary: { text: "not-applicable: a duty on the course team or the institution, not a standard the student reaches", rewrite: full, force: should, status: drafted }
  author-agent-written: "Write about this as an expectation worded with \"should\" on the course and its team, on who the standards apply to; joint degrees, holding for the honours degree and the master's degree. Cite it as QAA, 2025, Education Studies Subject Benchmark Statement, para 4.1. Do not present it as a regulatory requirement, and do not turn it into an outcome a student must show. Set it beside qaa/education-studies-2025/4.3, and where it shapes outcomes beside qaa/fheq-2024/4.15.b1 and 4.15.b9.3."
  author-agent-dialogue: "Raise it with a programme team or teacher who is designing, reviewing or defending the course's approach to who the standards apply to; joint degrees. Frame it for staff as an expectation worded with \"should\", and ask: Where do the course documents say how far a joint honours student should meet these standards? Do not quote the issuer at length, and do not put this duty to a student as something they have to achieve."
- statement: qaa/education-studies-2025/4.3
  forPractitioner: { text: "Treat the threshold column as the floor for every graduate, use the typical and excellent columns to describe performance above it, and refer to Annex D of the FHEQ when deciding what evidence shows each standard is met.", rewrite: light, force: should, status: drafted }
  forBeneficiary: { text: "not-applicable: a duty on the course team or the institution, not a standard the student reaches", rewrite: full, force: should, status: drafted }
  author-agent-written: "Write about this as an expectation worded with \"should\" on the course and its team, on the threshold as minimum; evidence by Annex D, holding for the honours degree and the master's degree. Cite it as QAA, 2025, Education Studies Subject Benchmark Statement, para 4.3. Do not present it as a regulatory requirement, and do not turn it into an outcome a student must show. Set it beside qaa/education-studies-2025/4.1 and qaa/education-studies-2025/4.5, and where it shapes outcomes beside qaa/fheq-2024/4.15.b1 and 4.15.b9.3."
  author-agent-dialogue: "Raise it with a programme team or teacher who is designing, reviewing or defending the course's approach to the threshold as minimum; evidence by Annex D. Frame it for staff as an expectation worded with \"should\", and ask: How do the course's marking criteria line up with the threshold, typical and excellent columns and with Annex D? Do not quote the issuer at length, and do not put this duty to a student as something they have to achieve."
- statement: qaa/education-studies-2025/4.5
  forPractitioner: { text: "Do not treat the standards as competence standards; if you write competence standards into a programme specification, draw on the statement and any PSRB requirements and follow current Equality and Human Rights Commission guidance.", rewrite: light, force: should, status: drafted }
  forBeneficiary: { text: "not-applicable: a duty on the course team or the institution, not a standard the student reaches", rewrite: full, force: should, status: drafted }
  author-agent-written: "Write about this as an expectation worded with \"should\" on the course and its team, on competence standards and the Equality Act, holding for any Education Studies course the statement covers. Cite it as QAA, 2025, Education Studies Subject Benchmark Statement, para 4.5. Do not present it as a regulatory requirement, and do not turn it into an outcome a student must show. Set it beside qaa/education-studies-2025/4.3 and qaa/education-studies-2025/4.7, and where it shapes outcomes beside the honours and master's descriptors qaa/fheq-2024/4.15.b1 and qaa/fheq-2024/4.17.b1 at spine:6 and spine:7."
  author-agent-dialogue: "Raise it with a programme team or teacher who is designing, reviewing or defending the course's approach to competence standards and the Equality Act. Frame it for staff as an expectation worded with \"should\", and ask: Does the programme specification set any competence standards, and were they checked against current EHRC guidance? Do not quote the issuer at length, and do not put this duty to a student as something they have to achieve."
- statement: qaa/education-studies-2025/4.5.b1
  forPractitioner: { text: "Check that every student awarded honours can show a coherent grasp of the major theories, concepts and ideas about education, taken in its broadest sense.", rewrite: light, force: threshold, status: drafted }
  forBeneficiary: { text: "To meet the minimum for your honours degree, you can show a coherent grasp of the major theories, concepts and ideas about education, taken in its broadest sense.", rewrite: full, force: threshold, status: drafted }
  author-agent-written: "Write about this as the threshold, the least every honours graduate shows for theories, concepts and ideas about education, in an honours degree in Education Studies at FHEQ Level 6 (FQHEIS Level 10, spine:6). Cite it as QAA, 2025, Education Studies Subject Benchmark Statement, section 4, the standards table after para 4.5, row \"Knowledge\", Threshold standard column. Do not present it as a regulatory requirement or a mark scheme, and do not apply it to master's awards. Set it beside qaa/education-studies-2025/4.5.b1.typical, the Annex D band qaa/fheq-2024/annex-d/knowledge/r2/3rd (the threshold class) and the descriptor qaa/fheq-2024/4.15.b1 at spine:6 (strand:knowledge)."
  author-agent-dialogue: "Raise it when a student asks what threshold work looks like for theories, concepts and ideas about education, or when markers compare work across the columns. Tell a student plainly what this level asks of them; with staff, treat it as a description of performance, not a mark scheme. Ask: Which theory of education could you explain to a friend, and where would it struggle? Make clear that this is the floor every honours graduate reaches, not the target."
- statement: qaa/education-studies-2025/4.5.b1.excellent
  forPractitioner: { text: "Recognise excellent honours work where students can show a deep grasp of the major theories, concepts and ideas about education, taken in its broadest sense, drawing on the leading edge of the field.", rewrite: light, force: will, status: drafted }
  forBeneficiary: { text: "At the excellent level for an honours degree, you can show a deep grasp of the major theories, concepts and ideas about education, taken in its broadest sense, drawing on the leading edge of the field.", rewrite: full, force: will, status: drafted }
  author-agent-written: "Write about this as the excellent standard, the top of the honours range for theories, concepts and ideas about education, in an honours degree in Education Studies at FHEQ Level 6 (FQHEIS Level 10, spine:6). Cite it as QAA, 2025, Education Studies Subject Benchmark Statement, section 4, the standards table after para 4.5, row \"Knowledge\", Excellent standard column. Do not present it as a regulatory requirement or a mark scheme, or as the minimum to pass, and do not apply it to master's awards. Set it beside qaa/education-studies-2025/4.5.b1.typical, the Annex D row qaa/fheq-2024/annex-d/knowledge/r2 (the statement ties no class to this column) and the descriptor qaa/fheq-2024/4.15.b1 at spine:6 (strand:knowledge)."
  author-agent-dialogue: "Raise it when a student asks what excellent work looks like for theories, concepts and ideas about education, or when markers compare work across the columns. Tell a student plainly what this level asks of them; with staff, treat it as a description of performance, not a mark scheme. Ask: Which theory of education could you explain to a friend, and where would it struggle? Never present this column as what is needed simply to pass."
- statement: qaa/education-studies-2025/4.5.b1.masters
  forPractitioner: { text: "On a master's course, plan for students to be able to show a systematic grasp of the major theories, concepts and ideas about education, taken in its broadest sense, much of it from the leading edge of the field, treating the column as a guide, as 4.4 asks.", rewrite: light, force: will, status: drafted }
  forBeneficiary: { text: "For a master's degree, you can show a systematic grasp of the major theories, concepts and ideas about education, taken in its broadest sense, much of it from the leading edge of the field.", rewrite: full, force: will, status: drafted }
  author-agent-written: "Write about this as the master's standard for theories, concepts and ideas about education at FHEQ Level 7 (FQHEIS Level 11, spine:7), the postgraduate column the statement asks institutions to treat as a guide (4.4). Cite it as QAA, 2025, Education Studies Subject Benchmark Statement, section 4, the standards table after para 4.5, row \"Knowledge\", Postgraduate master's column. Do not present it as a regulatory requirement, as an honours standard or as a merit or distinction band. Set it beside qaa/education-studies-2025/4.5.b1.excellent, the honours cell it reaches past, and the descriptor qaa/fheq-2024/4.17.b1 at spine:7 (strand:knowledge)."
  author-agent-dialogue: "Raise it when a master's student or course team asks what is expected for theories, concepts and ideas about education. Put it in plain words to a student and, with staff, as a guide the course may adapt, since not every course offers the chance to meet every row. Ask: Which ideas at the leading edge of education research shape your own work? Do not read the cell aloud at length or use an honours column for a master's student."
- statement: qaa/education-studies-2025/4.5.b1.typical
  forPractitioner: { text: "Plan for students working at the typical honours level to be able to show a sound grasp of the major theories, concepts and ideas about education, taken in its broadest sense.", rewrite: light, force: will, status: drafted }
  forBeneficiary: { text: "At the typical level for an honours degree, you can show a sound grasp of the major theories, concepts and ideas about education, taken in its broadest sense.", rewrite: full, force: will, status: drafted }
  author-agent-written: "Write about this as the typical standard, above the threshold for theories, concepts and ideas about education, in an honours degree in Education Studies at FHEQ Level 6 (FQHEIS Level 10, spine:6). Cite it as QAA, 2025, Education Studies Subject Benchmark Statement, section 4, the standards table after para 4.5, row \"Knowledge\", Typical standard column. Do not present it as a regulatory requirement or a mark scheme, or as the minimum to pass, and do not apply it to master's awards. Set it beside qaa/education-studies-2025/4.5.b1 and qaa/education-studies-2025/4.5.b1.excellent, the Annex D row qaa/fheq-2024/annex-d/knowledge/r2 (the statement ties no class to this column) and the descriptor qaa/fheq-2024/4.15.b1 at spine:6 (strand:knowledge)."
  author-agent-dialogue: "Raise it when a student asks what typical work looks like for theories, concepts and ideas about education, or when markers compare work across the columns. Tell a student plainly what this level asks of them; with staff, treat it as a description of performance, not a mark scheme. Ask: Which theory of education could you explain to a friend, and where would it struggle? Never present this column as what is needed simply to pass."
- statement: qaa/education-studies-2025/4.5.b2
  forPractitioner: { text: "Check that every student awarded honours can show a coherent grasp of where knowledge and theory in education are uncertain, ambiguous or limited.", rewrite: light, force: threshold, status: drafted }
  forBeneficiary: { text: "To meet the minimum for your honours degree, you can show a coherent grasp of where knowledge and theory in education are uncertain, ambiguous or limited.", rewrite: full, force: threshold, status: drafted }
  author-agent-written: "Write about this as the threshold, the least every honours graduate shows for the uncertainty and limits of knowledge in education, in an honours degree in Education Studies at FHEQ Level 6 (FQHEIS Level 10, spine:6). Cite it as QAA, 2025, Education Studies Subject Benchmark Statement, section 4, the standards table after para 4.5, row \"Critical awareness\", Threshold standard column. Do not present it as a regulatory requirement or a mark scheme, and do not apply it to master's awards. Set it beside qaa/education-studies-2025/4.5.b2.typical, the Annex D band qaa/fheq-2024/annex-d/knowledge/r2/3rd (the threshold class) and the descriptor qaa/fheq-2024/4.15.b4 at spine:6 (strand:thinking)."
  author-agent-dialogue: "Raise it when a student asks what threshold work looks like for the uncertainty and limits of knowledge in education, or when markers compare work across the columns. Tell a student plainly what this level asks of them; with staff, treat it as a description of performance, not a mark scheme. Ask: Where does what we know about education run out, or rest on shaky ground? Make clear that this is the floor every honours graduate reaches, not the target."
- statement: qaa/education-studies-2025/4.5.b2.excellent
  forPractitioner: { text: "Recognise excellent honours work where students can show a deep grasp of where knowledge and theory in education are uncertain, ambiguous or limited.", rewrite: light, force: will, status: drafted }
  forBeneficiary: { text: "At the excellent level for an honours degree, you can show a deep grasp of where knowledge and theory in education are uncertain, ambiguous or limited.", rewrite: full, force: will, status: drafted }
  author-agent-written: "Write about this as the excellent standard, the top of the honours range for the uncertainty and limits of knowledge in education, in an honours degree in Education Studies at FHEQ Level 6 (FQHEIS Level 10, spine:6). Cite it as QAA, 2025, Education Studies Subject Benchmark Statement, section 4, the standards table after para 4.5, row \"Critical awareness\", Excellent standard column. Do not present it as a regulatory requirement or a mark scheme, or as the minimum to pass, and do not apply it to master's awards. Set it beside qaa/education-studies-2025/4.5.b2.typical, the Annex D row qaa/fheq-2024/annex-d/knowledge/r2 (the statement ties no class to this column) and the descriptor qaa/fheq-2024/4.15.b4 at spine:6 (strand:thinking)."
  author-agent-dialogue: "Raise it when a student asks what excellent work looks like for the uncertainty and limits of knowledge in education, or when markers compare work across the columns. Tell a student plainly what this level asks of them; with staff, treat it as a description of performance, not a mark scheme. Ask: Where does what we know about education run out, or rest on shaky ground? Never present this column as what is needed simply to pass."
- statement: qaa/education-studies-2025/4.5.b2.masters
  forPractitioner: { text: "On a master's course, plan for students to be able to judge critically the knowledge and theory at the leading edge of the field, treating the column as a guide, as 4.4 asks.", rewrite: light, force: will, status: drafted }
  forBeneficiary: { text: "For a master's degree, you can judge critically the knowledge and theory at the leading edge of the field.", rewrite: full, force: will, status: drafted }
  author-agent-written: "Write about this as the master's standard for the uncertainty and limits of knowledge in education at FHEQ Level 7 (FQHEIS Level 11, spine:7), the postgraduate column the statement asks institutions to treat as a guide (4.4). Cite it as QAA, 2025, Education Studies Subject Benchmark Statement, section 4, the standards table after para 4.5, row \"Critical awareness\", Postgraduate master's column. Do not present it as a regulatory requirement, as an honours standard or as a merit or distinction band. Set it beside qaa/education-studies-2025/4.5.b2.excellent, the honours cell it reaches past, and the descriptor qaa/fheq-2024/4.17.b1 at spine:7 (strand:thinking)."
  author-agent-dialogue: "Raise it when a master's student or course team asks what is expected for the uncertainty and limits of knowledge in education. Put it in plain words to a student and, with staff, as a guide the course may adapt, since not every course offers the chance to meet every row. Ask: Which claim at the forefront of your field would you challenge, and on what grounds? Do not read the cell aloud at length or use an honours column for a master's student."
- statement: qaa/education-studies-2025/4.5.b2.typical
  forPractitioner: { text: "Plan for students working at the typical honours level to be able to show a sound grasp of where knowledge and theory in education are uncertain, ambiguous or limited.", rewrite: light, force: will, status: drafted }
  forBeneficiary: { text: "At the typical level for an honours degree, you can show a sound grasp of where knowledge and theory in education are uncertain, ambiguous or limited.", rewrite: full, force: will, status: drafted }
  author-agent-written: "Write about this as the typical standard, above the threshold for the uncertainty and limits of knowledge in education, in an honours degree in Education Studies at FHEQ Level 6 (FQHEIS Level 10, spine:6). Cite it as QAA, 2025, Education Studies Subject Benchmark Statement, section 4, the standards table after para 4.5, row \"Critical awareness\", Typical standard column. Do not present it as a regulatory requirement or a mark scheme, or as the minimum to pass, and do not apply it to master's awards. Set it beside qaa/education-studies-2025/4.5.b2 and qaa/education-studies-2025/4.5.b2.excellent, the Annex D row qaa/fheq-2024/annex-d/knowledge/r2 (the statement ties no class to this column) and the descriptor qaa/fheq-2024/4.15.b4 at spine:6 (strand:thinking)."
  author-agent-dialogue: "Raise it when a student asks what typical work looks like for the uncertainty and limits of knowledge in education, or when markers compare work across the columns. Tell a student plainly what this level asks of them; with staff, treat it as a description of performance, not a mark scheme. Ask: Where does what we know about education run out, or rest on shaky ground? Never present this column as what is needed simply to pass."
- statement: qaa/education-studies-2025/4.5.b3
  forPractitioner: { text: "Check that every student awarded honours can pick out critical questions about education by drawing on knowledge and evidence.", rewrite: light, force: threshold, status: drafted }
  forBeneficiary: { text: "To meet the minimum for your honours degree, you can pick out critical questions about education by drawing on knowledge and evidence.", rewrite: full, force: threshold, status: drafted }
  author-agent-written: "Write about this as the threshold, the least every honours graduate shows for critical questions and arguments about education, in an honours degree in Education Studies at FHEQ Level 6 (FQHEIS Level 10, spine:6). Cite it as QAA, 2025, Education Studies Subject Benchmark Statement, section 4, the standards table after para 4.5, row \"Critical evaluation\", Threshold standard column. Do not present it as a regulatory requirement or a mark scheme, and do not apply it to master's awards. Set it beside qaa/education-studies-2025/4.5.b3.typical, the Annex D band qaa/fheq-2024/annex-d/cognitive/r2/3rd (the threshold class) and the descriptor qaa/fheq-2024/4.15.b7 at spine:6 (strand:thinking)."
  author-agent-dialogue: "Raise it when a student asks what threshold work looks like for critical questions and arguments about education, or when markers compare work across the columns. Tell a student plainly what this level asks of them; with staff, treat it as a description of performance, not a mark scheme. Ask: What is the strongest counter-argument to the case you made in your last essay? Make clear that this is the floor every honours graduate reaches, not the target."
- statement: qaa/education-studies-2025/4.5.b3.excellent
  forPractitioner: { text: "Recognise excellent honours work where students can build and keep up critical arguments about education that draw on several bodies of knowledge and evidence in complex ways.", rewrite: light, force: will, status: drafted }
  forBeneficiary: { text: "At the excellent level for an honours degree, you can build and keep up critical arguments about education that draw on several bodies of knowledge and evidence in complex ways.", rewrite: full, force: will, status: drafted }
  author-agent-written: "Write about this as the excellent standard, the top of the honours range for critical questions and arguments about education, in an honours degree in Education Studies at FHEQ Level 6 (FQHEIS Level 10, spine:6). Cite it as QAA, 2025, Education Studies Subject Benchmark Statement, section 4, the standards table after para 4.5, row \"Critical evaluation\", Excellent standard column. Do not present it as a regulatory requirement or a mark scheme, or as the minimum to pass, and do not apply it to master's awards. Set it beside qaa/education-studies-2025/4.5.b3.typical, the Annex D row qaa/fheq-2024/annex-d/cognitive/r2 (the statement ties no class to this column) and the descriptor qaa/fheq-2024/4.15.b7 at spine:6 (strand:thinking)."
  author-agent-dialogue: "Raise it when a student asks what excellent work looks like for critical questions and arguments about education, or when markers compare work across the columns. Tell a student plainly what this level asks of them; with staff, treat it as a description of performance, not a mark scheme. Ask: What is the strongest counter-argument to the case you made in your last essay? Never present this column as what is needed simply to pass."
- statement: qaa/education-studies-2025/4.5.b3.masters
  forPractitioner: { text: "On a master's course, plan for students to be able to bring complex knowledge and evidence together to reach new insights, treating the column as a guide, as 4.4 asks.", rewrite: light, force: will, status: drafted }
  forBeneficiary: { text: "For a master's degree, you can bring complex knowledge and evidence together to reach new insights.", rewrite: full, force: will, status: drafted }
  author-agent-written: "Write about this as the master's standard for critical questions and arguments about education at FHEQ Level 7 (FQHEIS Level 11, spine:7), the postgraduate column the statement asks institutions to treat as a guide (4.4). Cite it as QAA, 2025, Education Studies Subject Benchmark Statement, section 4, the standards table after para 4.5, row \"Critical evaluation\", Postgraduate master's column. Do not present it as a regulatory requirement, as an honours standard or as a merit or distinction band. Set it beside qaa/education-studies-2025/4.5.b3.excellent, the honours cell it reaches past, and the descriptor qaa/fheq-2024/4.17.b4.1 at spine:7 (strand:thinking)."
  author-agent-dialogue: "Raise it when a master's student or course team asks what is expected for critical questions and arguments about education. Put it in plain words to a student and, with staff, as a guide the course may adapt, since not every course offers the chance to meet every row. Ask: What new insight did bringing two bodies of evidence together give you? Do not read the cell aloud at length or use an honours column for a master's student."
- statement: qaa/education-studies-2025/4.5.b3.typical
  forPractitioner: { text: "Plan for students working at the typical honours level to be able to build critical arguments about education that draw in detail on several bodies of knowledge and evidence.", rewrite: light, force: will, status: drafted }
  forBeneficiary: { text: "At the typical level for an honours degree, you can build critical arguments about education that draw in detail on several bodies of knowledge and evidence.", rewrite: full, force: will, status: drafted }
  author-agent-written: "Write about this as the typical standard, above the threshold for critical questions and arguments about education, in an honours degree in Education Studies at FHEQ Level 6 (FQHEIS Level 10, spine:6). Cite it as QAA, 2025, Education Studies Subject Benchmark Statement, section 4, the standards table after para 4.5, row \"Critical evaluation\", Typical standard column. Do not present it as a regulatory requirement or a mark scheme, or as the minimum to pass, and do not apply it to master's awards. Set it beside qaa/education-studies-2025/4.5.b3 and qaa/education-studies-2025/4.5.b3.excellent, the Annex D row qaa/fheq-2024/annex-d/cognitive/r2 (the statement ties no class to this column) and the descriptor qaa/fheq-2024/4.15.b7 at spine:6 (strand:thinking)."
  author-agent-dialogue: "Raise it when a student asks what typical work looks like for critical questions and arguments about education, or when markers compare work across the columns. Tell a student plainly what this level asks of them; with staff, treat it as a description of performance, not a mark scheme. Ask: What is the strongest counter-argument to the case you made in your last essay? Never present this column as what is needed simply to pass."
- statement: qaa/education-studies-2025/4.5.b4
  forPractitioner: { text: "Check that every student awarded honours can use major theories, concepts and ideas on real problems in education.", rewrite: light, force: threshold, status: drafted }
  forBeneficiary: { text: "To meet the minimum for your honours degree, you can use major theories, concepts and ideas on real problems in education.", rewrite: full, force: threshold, status: drafted }
  author-agent-written: "Write about this as the threshold, the least every honours graduate shows for applying theory to real problems in education, in an honours degree in Education Studies at FHEQ Level 6 (FQHEIS Level 10, spine:6). Cite it as QAA, 2025, Education Studies Subject Benchmark Statement, section 4, the standards table after para 4.5, row \"Application\", Threshold standard column. Do not present it as a regulatory requirement or a mark scheme, and do not apply it to master's awards. Set it beside qaa/education-studies-2025/4.5.b4.typical, the Annex D band qaa/fheq-2024/annex-d/cognitive/r3/3rd (the threshold class) and the descriptor qaa/fheq-2024/4.15.b3.1 at spine:6 (strand:application)."
  author-agent-dialogue: "Raise it when a student asks what threshold work looks like for applying theory to real problems in education, or when markers compare work across the columns. Tell a student plainly what this level asks of them; with staff, treat it as a description of performance, not a mark scheme. Ask: Which real problem in education have you explained with a theory, and did the theory fit? Make clear that this is the floor every honours graduate reaches, not the target."
- statement: qaa/education-studies-2025/4.5.b4.excellent
  forPractitioner: { text: "Recognise excellent honours work where students can use major theories, concepts and ideas on real problems in education, in complex ways.", rewrite: light, force: will, status: drafted }
  forBeneficiary: { text: "At the excellent level for an honours degree, you can use major theories, concepts and ideas on real problems in education, in complex ways.", rewrite: full, force: will, status: drafted }
  author-agent-written: "Write about this as the excellent standard, the top of the honours range for applying theory to real problems in education, in an honours degree in Education Studies at FHEQ Level 6 (FQHEIS Level 10, spine:6). Cite it as QAA, 2025, Education Studies Subject Benchmark Statement, section 4, the standards table after para 4.5, row \"Application\", Excellent standard column. Do not present it as a regulatory requirement or a mark scheme, or as the minimum to pass, and do not apply it to master's awards. Set it beside qaa/education-studies-2025/4.5.b4.typical, the Annex D row qaa/fheq-2024/annex-d/cognitive/r3 (the statement ties no class to this column) and the descriptor qaa/fheq-2024/4.15.b3.1 at spine:6 (strand:application)."
  author-agent-dialogue: "Raise it when a student asks what excellent work looks like for applying theory to real problems in education, or when markers compare work across the columns. Tell a student plainly what this level asks of them; with staff, treat it as a description of performance, not a mark scheme. Ask: Which real problem in education have you explained with a theory, and did the theory fit? Never present this column as what is needed simply to pass."
- statement: qaa/education-studies-2025/4.5.b4.masters
  forPractitioner: { text: "On a master's course, plan for students to be able to show originality in using major theories and ideas on complex real problems in education, treating the column as a guide, as 4.4 asks.", rewrite: light, force: will, status: drafted }
  forBeneficiary: { text: "For a master's degree, you can show originality in using major theories and ideas on complex real problems in education.", rewrite: full, force: will, status: drafted }
  author-agent-written: "Write about this as the master's standard for applying theory to real problems in education at FHEQ Level 7 (FQHEIS Level 11, spine:7), the postgraduate column the statement asks institutions to treat as a guide (4.4). Cite it as QAA, 2025, Education Studies Subject Benchmark Statement, section 4, the standards table after para 4.5, row \"Application\", Postgraduate master's column. Do not present it as a regulatory requirement, as an honours standard or as a merit or distinction band. Set it beside qaa/education-studies-2025/4.5.b4.excellent, the honours cell it reaches past, and the descriptor qaa/fheq-2024/4.17.b3 at spine:7 (strand:application)."
  author-agent-dialogue: "Raise it when a master's student or course team asks what is expected for applying theory to real problems in education. Put it in plain words to a student and, with staff, as a guide the course may adapt, since not every course offers the chance to meet every row. Ask: Where have you applied a theory in a way others had not tried? Do not read the cell aloud at length or use an honours column for a master's student."
- statement: qaa/education-studies-2025/4.5.b4.typical
  forPractitioner: { text: "Plan for students working at the typical honours level to be able to use major theories, concepts and ideas on real problems in education, in detail.", rewrite: light, force: will, status: drafted }
  forBeneficiary: { text: "At the typical level for an honours degree, you can use major theories, concepts and ideas on real problems in education, in detail.", rewrite: full, force: will, status: drafted }
  author-agent-written: "Write about this as the typical standard, above the threshold for applying theory to real problems in education, in an honours degree in Education Studies at FHEQ Level 6 (FQHEIS Level 10, spine:6). Cite it as QAA, 2025, Education Studies Subject Benchmark Statement, section 4, the standards table after para 4.5, row \"Application\", Typical standard column. Do not present it as a regulatory requirement or a mark scheme, or as the minimum to pass, and do not apply it to master's awards. Set it beside qaa/education-studies-2025/4.5.b4 and qaa/education-studies-2025/4.5.b4.excellent, the Annex D row qaa/fheq-2024/annex-d/cognitive/r3 (the statement ties no class to this column) and the descriptor qaa/fheq-2024/4.15.b3.1 at spine:6 (strand:application)."
  author-agent-dialogue: "Raise it when a student asks what typical work looks like for applying theory to real problems in education, or when markers compare work across the columns. Tell a student plainly what this level asks of them; with staff, treat it as a description of performance, not a mark scheme. Ask: Which real problem in education have you explained with a theory, and did the theory fit? Never present this column as what is needed simply to pass."
- statement: qaa/education-studies-2025/4.5.b5
  forPractitioner: { text: "Check that every student awarded honours can show a coherent grasp of the ethical dilemmas, tensions and challenges in education.", rewrite: light, force: threshold, status: drafted }
  forBeneficiary: { text: "To meet the minimum for your honours degree, you can show a coherent grasp of the ethical dilemmas, tensions and challenges in education.", rewrite: full, force: threshold, status: drafted }
  author-agent-written: "Write about this as the threshold, the least every honours graduate shows for ethical tensions in education, in an honours degree in Education Studies at FHEQ Level 6 (FQHEIS Level 10, spine:6). Cite it as QAA, 2025, Education Studies Subject Benchmark Statement, section 4, the standards table after para 4.5, row \"Ethical awareness\", Threshold standard column. Do not present it as a regulatory requirement or a mark scheme, and do not apply it to master's awards. Set it beside qaa/education-studies-2025/4.5.b5.typical, the Annex D band qaa/fheq-2024/annex-d/knowledge/r2/3rd (the threshold class) and the descriptor qaa/fheq-2024/4.15.b4 at spine:6 (strand:thinking)."
  author-agent-dialogue: "Raise it when a student asks what threshold work looks like for ethical tensions in education, or when markers compare work across the columns. Tell a student plainly what this level asks of them; with staff, treat it as a description of performance, not a mark scheme. Ask: Which ethical dilemma in education do you find hardest to resolve, and why? Make clear that this is the floor every honours graduate reaches, not the target."
- statement: qaa/education-studies-2025/4.5.b5.excellent
  forPractitioner: { text: "Recognise excellent honours work where students can show a deep grasp of the ethical dilemmas, tensions and challenges in education.", rewrite: light, force: will, status: drafted }
  forBeneficiary: { text: "At the excellent level for an honours degree, you can show a deep grasp of the ethical dilemmas, tensions and challenges in education.", rewrite: full, force: will, status: drafted }
  author-agent-written: "Write about this as the excellent standard, the top of the honours range for ethical tensions in education, in an honours degree in Education Studies at FHEQ Level 6 (FQHEIS Level 10, spine:6). Cite it as QAA, 2025, Education Studies Subject Benchmark Statement, section 4, the standards table after para 4.5, row \"Ethical awareness\", Excellent standard column. Do not present it as a regulatory requirement or a mark scheme, or as the minimum to pass, and do not apply it to master's awards. Set it beside qaa/education-studies-2025/4.5.b5.typical, the Annex D row qaa/fheq-2024/annex-d/knowledge/r2 (the statement ties no class to this column) and the descriptor qaa/fheq-2024/4.15.b4 at spine:6 (strand:thinking)."
  author-agent-dialogue: "Raise it when a student asks what excellent work looks like for ethical tensions in education, or when markers compare work across the columns. Tell a student plainly what this level asks of them; with staff, treat it as a description of performance, not a mark scheme. Ask: Which ethical dilemma in education do you find hardest to resolve, and why? Never present this column as what is needed simply to pass."
- statement: qaa/education-studies-2025/4.5.b5.masters
  forPractitioner: { text: "On a master's course, plan for students to be able to show originality in analysing and resolving ethical dilemmas, tensions and challenges in education, treating the column as a guide, as 4.4 asks.", rewrite: light, force: will, status: drafted }
  forBeneficiary: { text: "For a master's degree, you can show originality in analysing and resolving ethical dilemmas, tensions and challenges in education.", rewrite: full, force: will, status: drafted }
  author-agent-written: "Write about this as the master's standard for ethical tensions in education at FHEQ Level 7 (FQHEIS Level 11, spine:7), the postgraduate column the statement asks institutions to treat as a guide (4.4). Cite it as QAA, 2025, Education Studies Subject Benchmark Statement, section 4, the standards table after para 4.5, row \"Ethical awareness\", Postgraduate master's column. Do not present it as a regulatory requirement, as an honours standard or as a merit or distinction band. Set it beside qaa/education-studies-2025/4.5.b5.excellent, the honours cell it reaches past, and the descriptor qaa/fheq-2024/4.17.b5 at spine:7 (strand:thinking)."
  author-agent-dialogue: "Raise it when a master's student or course team asks what is expected for ethical tensions in education. Put it in plain words to a student and, with staff, as a guide the course may adapt, since not every course offers the chance to meet every row. Ask: How would you resolve an ethical dilemma you met in your own research or practice? Do not read the cell aloud at length or use an honours column for a master's student."
- statement: qaa/education-studies-2025/4.5.b5.typical
  forPractitioner: { text: "Plan for students working at the typical honours level to be able to show a sound grasp of the ethical dilemmas, tensions and challenges in education.", rewrite: light, force: will, status: drafted }
  forBeneficiary: { text: "At the typical level for an honours degree, you can show a sound grasp of the ethical dilemmas, tensions and challenges in education.", rewrite: full, force: will, status: drafted }
  author-agent-written: "Write about this as the typical standard, above the threshold for ethical tensions in education, in an honours degree in Education Studies at FHEQ Level 6 (FQHEIS Level 10, spine:6). Cite it as QAA, 2025, Education Studies Subject Benchmark Statement, section 4, the standards table after para 4.5, row \"Ethical awareness\", Typical standard column. Do not present it as a regulatory requirement or a mark scheme, or as the minimum to pass, and do not apply it to master's awards. Set it beside qaa/education-studies-2025/4.5.b5 and qaa/education-studies-2025/4.5.b5.excellent, the Annex D row qaa/fheq-2024/annex-d/knowledge/r2 (the statement ties no class to this column) and the descriptor qaa/fheq-2024/4.15.b4 at spine:6 (strand:thinking)."
  author-agent-dialogue: "Raise it when a student asks what typical work looks like for ethical tensions in education, or when markers compare work across the columns. Tell a student plainly what this level asks of them; with staff, treat it as a description of performance, not a mark scheme. Ask: Which ethical dilemma in education do you find hardest to resolve, and why? Never present this column as what is needed simply to pass."
- statement: qaa/education-studies-2025/4.5.b6
  forPractitioner: { text: "Check that every student awarded honours can accept the value of weighing up their own skills and reflecting on them to guide later learning.", rewrite: light, force: threshold, status: drafted }
  forBeneficiary: { text: "To meet the minimum for your honours degree, you can accept the value of weighing up your own skills and reflecting on them to guide later learning.", rewrite: full, force: threshold, status: drafted }
  author-agent-written: "Write about this as the threshold, the least every honours graduate shows for evaluating own learning skills, in an honours degree in Education Studies at FHEQ Level 6 (FQHEIS Level 10, spine:6). Cite it as QAA, 2025, Education Studies Subject Benchmark Statement, section 4, the standards table after para 4.5, row \"Evaluate own learning skills\", Threshold standard column. Do not present it as a regulatory requirement or a mark scheme, and do not apply it to master's awards. Set it beside qaa/education-studies-2025/4.5.b6.typical, the Annex D band qaa/fheq-2024/annex-d/transferable/r5/3rd (the threshold class) and the descriptor qaa/fheq-2024/4.15.b5 at spine:6 (strand:autonomy)."
  author-agent-dialogue: "Raise it when a student asks what threshold work looks like for evaluating own learning skills, or when markers compare work across the columns. Tell a student plainly what this level asks of them; with staff, treat it as a description of performance, not a mark scheme. Ask: What is one strength and one weakness in how you learn, and what will you do about the weakness? Make clear that this is the floor every honours graduate reaches, not the target."
- statement: qaa/education-studies-2025/4.5.b6.excellent
  forPractitioner: { text: "Recognise excellent honours work where students can take control of their own learning with sophistication, reflecting on their strengths and weaknesses to guide later learning.", rewrite: light, force: will, status: drafted }
  forBeneficiary: { text: "At the excellent level for an honours degree, you can take control of your own learning with sophistication, reflecting on their strengths and weaknesses to guide later learning.", rewrite: full, force: will, status: drafted }
  author-agent-written: "Write about this as the excellent standard, the top of the honours range for evaluating own learning skills, in an honours degree in Education Studies at FHEQ Level 6 (FQHEIS Level 10, spine:6). Cite it as QAA, 2025, Education Studies Subject Benchmark Statement, section 4, the standards table after para 4.5, row \"Evaluate own learning skills\", Excellent standard column. Do not present it as a regulatory requirement or a mark scheme, or as the minimum to pass, and do not apply it to master's awards. Set it beside qaa/education-studies-2025/4.5.b6.typical, the Annex D row qaa/fheq-2024/annex-d/transferable/r5 (the statement ties no class to this column) and the descriptor qaa/fheq-2024/4.15.b5 at spine:6 (strand:autonomy)."
  author-agent-dialogue: "Raise it when a student asks what excellent work looks like for evaluating own learning skills, or when markers compare work across the columns. Tell a student plainly what this level asks of them; with staff, treat it as a description of performance, not a mark scheme. Ask: What is one strength and one weakness in how you learn, and what will you do about the weakness? Never present this column as what is needed simply to pass."
- statement: qaa/education-studies-2025/4.5.b6.masters
  forPractitioner: { text: "On a master's course, plan for students to be able to lead their own learning with sophistication, judging their strengths and weaknesses reflexively to guide later learning, treating the column as a guide, as 4.4 asks.", rewrite: light, force: will, status: drafted }
  forBeneficiary: { text: "For a master's degree, you can lead your own learning with sophistication, judging their strengths and weaknesses reflexively to guide later learning.", rewrite: full, force: will, status: drafted }
  author-agent-written: "Write about this as the master's standard for evaluating own learning skills at FHEQ Level 7 (FQHEIS Level 11, spine:7), the postgraduate column the statement asks institutions to treat as a guide (4.4). Cite it as QAA, 2025, Education Studies Subject Benchmark Statement, section 4, the standards table after para 4.5, row \"Evaluate own learning skills\", Postgraduate master's column. Do not present it as a regulatory requirement, as an honours standard or as a merit or distinction band. Set it beside qaa/education-studies-2025/4.5.b6.excellent, the honours cell it reaches past, and the descriptor qaa/fheq-2024/4.17.b8.3 at spine:7 (strand:autonomy)."
  author-agent-dialogue: "Raise it when a master's student or course team asks what is expected for evaluating own learning skills. Put it in plain words to a student and, with staff, as a guide the course may adapt, since not every course offers the chance to meet every row. Ask: How do you decide what to learn next, without anyone setting it for you? Do not read the cell aloud at length or use an honours column for a master's student."
- statement: qaa/education-studies-2025/4.5.b6.typical
  forPractitioner: { text: "Plan for students working at the typical honours level to be able to take control of their own learning, reflecting on and judging their personal strengths and weaknesses to guide later learning.", rewrite: light, force: will, status: drafted }
  forBeneficiary: { text: "At the typical level for an honours degree, you can take control of your own learning, reflecting on and judging their personal strengths and weaknesses to guide later learning.", rewrite: full, force: will, status: drafted }
  author-agent-written: "Write about this as the typical standard, above the threshold for evaluating own learning skills, in an honours degree in Education Studies at FHEQ Level 6 (FQHEIS Level 10, spine:6). Cite it as QAA, 2025, Education Studies Subject Benchmark Statement, section 4, the standards table after para 4.5, row \"Evaluate own learning skills\", Typical standard column. Do not present it as a regulatory requirement or a mark scheme, or as the minimum to pass, and do not apply it to master's awards. Set it beside qaa/education-studies-2025/4.5.b6 and qaa/education-studies-2025/4.5.b6.excellent, the Annex D row qaa/fheq-2024/annex-d/transferable/r5 (the statement ties no class to this column) and the descriptor qaa/fheq-2024/4.15.b5 at spine:6 (strand:autonomy)."
  author-agent-dialogue: "Raise it when a student asks what typical work looks like for evaluating own learning skills, or when markers compare work across the columns. Tell a student plainly what this level asks of them; with staff, treat it as a description of performance, not a mark scheme. Ask: What is one strength and one weakness in how you learn, and what will you do about the weakness? Never present this column as what is needed simply to pass."
- statement: qaa/education-studies-2025/4.5.b7
  forPractitioner: { text: "Check that every student awarded honours can know and use the methods that systematic study and research in education call for.", rewrite: light, force: threshold, status: drafted }
  forBeneficiary: { text: "To meet the minimum for your honours degree, you can know and use the methods that systematic study and research in education call for.", rewrite: full, force: threshold, status: drafted }
  author-agent-written: "Write about this as the threshold, the least every honours graduate shows for methods for systematic study and research, in an honours degree in Education Studies at FHEQ Level 6 (FQHEIS Level 10, spine:6). Cite it as QAA, 2025, Education Studies Subject Benchmark Statement, section 4, the standards table after para 4.5, row \"Study skills\", Threshold standard column. Do not present it as a regulatory requirement or a mark scheme, and do not apply it to master's awards. Set it beside qaa/education-studies-2025/4.5.b7.typical, the Annex D band qaa/fheq-2024/annex-d/knowledge/r3/3rd (the threshold class) and the descriptor qaa/fheq-2024/4.15.b2 at spine:6 (strand:application)."
  author-agent-dialogue: "Raise it when a student asks what threshold work looks like for methods for systematic study and research, or when markers compare work across the columns. Tell a student plainly what this level asks of them; with staff, treat it as a description of performance, not a mark scheme. Ask: Which research method could you use well today, and which would you need to learn? Make clear that this is the floor every honours graduate reaches, not the target."
- statement: qaa/education-studies-2025/4.5.b7.excellent
  forPractitioner: { text: "Recognise excellent honours work where students can know and use, with a deep working grasp, the methods for systematic study and research in education, and show that judging their own skills has improved them.", rewrite: light, force: will, status: drafted }
  forBeneficiary: { text: "At the excellent level for an honours degree, you can know and use, with a deep working grasp, the methods for systematic study and research in education, and show that judging your own skills has improved them.", rewrite: full, force: will, status: drafted }
  author-agent-written: "Write about this as the excellent standard, the top of the honours range for methods for systematic study and research, in an honours degree in Education Studies at FHEQ Level 6 (FQHEIS Level 10, spine:6). Cite it as QAA, 2025, Education Studies Subject Benchmark Statement, section 4, the standards table after para 4.5, row \"Study skills\", Excellent standard column. Do not present it as a regulatory requirement or a mark scheme, or as the minimum to pass, and do not apply it to master's awards. Set it beside qaa/education-studies-2025/4.5.b7.typical, the Annex D row qaa/fheq-2024/annex-d/knowledge/r3 (the statement ties no class to this column) and the descriptor qaa/fheq-2024/4.15.b2 at spine:6 (strand:application)."
  author-agent-dialogue: "Raise it when a student asks what excellent work looks like for methods for systematic study and research, or when markers compare work across the columns. Tell a student plainly what this level asks of them; with staff, treat it as a description of performance, not a mark scheme. Ask: Which research method could you use well today, and which would you need to learn? Never present this column as what is needed simply to pass."
- statement: qaa/education-studies-2025/4.5.b7.masters
  forPractitioner: { text: "On a master's course, plan for students to be able to judge in a critically reflexive way, and use, the methods for systematic study, research and application in education, treating the column as a guide, as 4.4 asks.", rewrite: light, force: will, status: drafted }
  forBeneficiary: { text: "For a master's degree, you can judge in a critically reflexive way, and use, the methods for systematic study, research and application in education.", rewrite: full, force: will, status: drafted }
  author-agent-written: "Write about this as the master's standard for methods for systematic study and research at FHEQ Level 7 (FQHEIS Level 11, spine:7), the postgraduate column the statement asks institutions to treat as a guide (4.4). Cite it as QAA, 2025, Education Studies Subject Benchmark Statement, section 4, the standards table after para 4.5, row \"Study skills\", Postgraduate master's column. Do not present it as a regulatory requirement, as an honours standard or as a merit or distinction band. Set it beside qaa/education-studies-2025/4.5.b7.excellent, the honours cell it reaches past, and the descriptor qaa/fheq-2024/4.17.b2 at spine:7 (strand:application)."
  author-agent-dialogue: "Raise it when a master's student or course team asks what is expected for methods for systematic study and research. Put it in plain words to a student and, with staff, as a guide the course may adapt, since not every course offers the chance to meet every row. Ask: How would you defend your choice of method to a sceptical examiner? Do not read the cell aloud at length or use an honours column for a master's student."
- statement: qaa/education-studies-2025/4.5.b7.typical
  forPractitioner: { text: "Plan for students working at the typical honours level to be able to know and use, with a sound working grasp, the methods for systematic study and research in education, and judge their own strengths and weaknesses.", rewrite: light, force: will, status: drafted }
  forBeneficiary: { text: "At the typical level for an honours degree, you can know and use, with a sound working grasp, the methods for systematic study and research in education, and judge your own strengths and weaknesses.", rewrite: full, force: will, status: drafted }
  author-agent-written: "Write about this as the typical standard, above the threshold for methods for systematic study and research, in an honours degree in Education Studies at FHEQ Level 6 (FQHEIS Level 10, spine:6). Cite it as QAA, 2025, Education Studies Subject Benchmark Statement, section 4, the standards table after para 4.5, row \"Study skills\", Typical standard column. Do not present it as a regulatory requirement or a mark scheme, or as the minimum to pass, and do not apply it to master's awards. Set it beside qaa/education-studies-2025/4.5.b7 and qaa/education-studies-2025/4.5.b7.excellent, the Annex D row qaa/fheq-2024/annex-d/knowledge/r3 (the statement ties no class to this column) and the descriptor qaa/fheq-2024/4.15.b2 at spine:6 (strand:application)."
  author-agent-dialogue: "Raise it when a student asks what typical work looks like for methods for systematic study and research, or when markers compare work across the columns. Tell a student plainly what this level asks of them; with staff, treat it as a description of performance, not a mark scheme. Ask: Which research method could you use well today, and which would you need to learn? Never present this column as what is needed simply to pass."
- statement: qaa/education-studies-2025/4.5.b8
  forPractitioner: { text: "Check that every student awarded honours can take creative approaches to studying education.", rewrite: light, force: threshold, status: drafted }
  forBeneficiary: { text: "To meet the minimum for your honours degree, you can take creative approaches to studying education.", rewrite: full, force: threshold, status: drafted }
  author-agent-written: "Write about this as the threshold, the least every honours graduate shows for creative approaches to studying education, in an honours degree in Education Studies at FHEQ Level 6 (FQHEIS Level 10, spine:6). Cite it as QAA, 2025, Education Studies Subject Benchmark Statement, section 4, the standards table after para 4.5, row \"Creativity\", Threshold standard column. Do not present it as a regulatory requirement or a mark scheme, and do not apply it to master's awards. Set it beside qaa/education-studies-2025/4.5.b8.typical, the Annex D band qaa/fheq-2024/annex-d/cognitive/r4/3rd (the threshold class) and the descriptor qaa/fheq-2024/4.15.b6 at spine:6 (strand:thinking)."
  author-agent-dialogue: "Raise it when a student asks what threshold work looks like for creative approaches to studying education, or when markers compare work across the columns. Tell a student plainly what this level asks of them; with staff, treat it as a description of performance, not a mark scheme. Ask: Where have you taken a creative approach in your studies, and did it work? Make clear that this is the floor every honours graduate reaches, not the target."
- statement: qaa/education-studies-2025/4.5.b8.excellent
  forPractitioner: { text: "Recognise excellent honours work where students can take highly creative approaches to studying education.", rewrite: light, force: will, status: drafted }
  forBeneficiary: { text: "At the excellent level for an honours degree, you can take highly creative approaches to studying education.", rewrite: full, force: will, status: drafted }
  author-agent-written: "Write about this as the excellent standard, the top of the honours range for creative approaches to studying education, in an honours degree in Education Studies at FHEQ Level 6 (FQHEIS Level 10, spine:6). Cite it as QAA, 2025, Education Studies Subject Benchmark Statement, section 4, the standards table after para 4.5, row \"Creativity\", Excellent standard column. Do not present it as a regulatory requirement or a mark scheme, or as the minimum to pass, and do not apply it to master's awards. Set it beside qaa/education-studies-2025/4.5.b8.typical, the Annex D row qaa/fheq-2024/annex-d/cognitive/r4 (the statement ties no class to this column) and the descriptor qaa/fheq-2024/4.15.b6 at spine:6 (strand:thinking)."
  author-agent-dialogue: "Raise it when a student asks what excellent work looks like for creative approaches to studying education, or when markers compare work across the columns. Tell a student plainly what this level asks of them; with staff, treat it as a description of performance, not a mark scheme. Ask: Where have you taken a creative approach in your studies, and did it work? Never present this column as what is needed simply to pass."
- statement: qaa/education-studies-2025/4.5.b8.masters
  forPractitioner: { text: "On a master's course, plan for students to be able to take highly creative and original approaches to studying education, treating the column as a guide, as 4.4 asks.", rewrite: light, force: will, status: drafted }
  forBeneficiary: { text: "For a master's degree, you can take highly creative and original approaches to studying education.", rewrite: full, force: will, status: drafted }
  author-agent-written: "Write about this as the master's standard for creative approaches to studying education at FHEQ Level 7 (FQHEIS Level 11, spine:7), the postgraduate column the statement asks institutions to treat as a guide (4.4). Cite it as QAA, 2025, Education Studies Subject Benchmark Statement, section 4, the standards table after para 4.5, row \"Creativity\", Postgraduate master's column. Do not present it as a regulatory requirement, as an honours standard or as a merit or distinction band. Set it beside qaa/education-studies-2025/4.5.b8.excellent, the honours cell it reaches past, and the descriptor qaa/fheq-2024/4.17.b6 at spine:7 (strand:thinking)."
  author-agent-dialogue: "Raise it when a master's student or course team asks what is expected for creative approaches to studying education. Put it in plain words to a student and, with staff, as a guide the course may adapt, since not every course offers the chance to meet every row. Ask: What is original about the approach you took in your recent work? Do not read the cell aloud at length or use an honours column for a master's student."
- statement: qaa/education-studies-2025/4.5.b8.typical
  forPractitioner: { text: "Plan for students working at the typical honours level to be able to take creative approaches to studying education, and to good effect.", rewrite: light, force: will, status: drafted }
  forBeneficiary: { text: "At the typical level for an honours degree, you can take creative approaches to studying education, and to good effect.", rewrite: full, force: will, status: drafted }
  author-agent-written: "Write about this as the typical standard, above the threshold for creative approaches to studying education, in an honours degree in Education Studies at FHEQ Level 6 (FQHEIS Level 10, spine:6). Cite it as QAA, 2025, Education Studies Subject Benchmark Statement, section 4, the standards table after para 4.5, row \"Creativity\", Typical standard column. Do not present it as a regulatory requirement or a mark scheme, or as the minimum to pass, and do not apply it to master's awards. Set it beside qaa/education-studies-2025/4.5.b8 and qaa/education-studies-2025/4.5.b8.excellent, the Annex D row qaa/fheq-2024/annex-d/cognitive/r4 (the statement ties no class to this column) and the descriptor qaa/fheq-2024/4.15.b6 at spine:6 (strand:thinking)."
  author-agent-dialogue: "Raise it when a student asks what typical work looks like for creative approaches to studying education, or when markers compare work across the columns. Tell a student plainly what this level asks of them; with staff, treat it as a description of performance, not a mark scheme. Ask: Where have you taken a creative approach in your studies, and did it work? Never present this column as what is needed simply to pass."
- statement: qaa/education-studies-2025/4.5.b9
  forPractitioner: { text: "Check that every student awarded honours can plan and carry out suitable collaborations with fellow students, staff and wider stakeholders.", rewrite: light, force: threshold, status: drafted }
  forBeneficiary: { text: "To meet the minimum for your honours degree, you can plan and carry out suitable collaborations with fellow students, staff and wider stakeholders.", rewrite: full, force: threshold, status: drafted }
  author-agent-written: "Write about this as the threshold, the least every honours graduate shows for planning and carrying out collaborations, in an honours degree in Education Studies at FHEQ Level 6 (FQHEIS Level 10, spine:6). Cite it as QAA, 2025, Education Studies Subject Benchmark Statement, section 4, the standards table after para 4.5, row \"Planning for collaboration\", Threshold standard column. Do not present it as a regulatory requirement or a mark scheme, and do not apply it to master's awards. Set it beside qaa/education-studies-2025/4.5.b9.typical, the Annex D band qaa/fheq-2024/annex-d/transferable/r2/3rd (the threshold class) and the descriptor qaa/fheq-2024/4.15.b9.1 at spine:6 (strand:autonomy)."
  author-agent-dialogue: "Raise it when a student asks what threshold work looks like for planning and carrying out collaborations, or when markers compare work across the columns. Tell a student plainly what this level asks of them; with staff, treat it as a description of performance, not a mark scheme. Ask: Who have you collaborated with on your course, and what did you plan together? Make clear that this is the floor every honours graduate reaches, not the target."
- statement: qaa/education-studies-2025/4.5.b9.excellent
  forPractitioner: { text: "Recognise excellent honours work where students can show a highly developed ability to plan and carry out effective collaborations with fellow students, staff and wider stakeholders.", rewrite: light, force: will, status: drafted }
  forBeneficiary: { text: "At the excellent level for an honours degree, you can show a highly developed ability to plan and carry out effective collaborations with fellow students, staff and wider stakeholders.", rewrite: full, force: will, status: drafted }
  author-agent-written: "Write about this as the excellent standard, the top of the honours range for planning and carrying out collaborations, in an honours degree in Education Studies at FHEQ Level 6 (FQHEIS Level 10, spine:6). Cite it as QAA, 2025, Education Studies Subject Benchmark Statement, section 4, the standards table after para 4.5, row \"Planning for collaboration\", Excellent standard column. Do not present it as a regulatory requirement or a mark scheme, or as the minimum to pass, and do not apply it to master's awards. Set it beside qaa/education-studies-2025/4.5.b9.typical, the Annex D row qaa/fheq-2024/annex-d/transferable/r2 (the statement ties no class to this column) and the descriptor qaa/fheq-2024/4.15.b9.1 at spine:6 (strand:autonomy)."
  author-agent-dialogue: "Raise it when a student asks what excellent work looks like for planning and carrying out collaborations, or when markers compare work across the columns. Tell a student plainly what this level asks of them; with staff, treat it as a description of performance, not a mark scheme. Ask: Who have you collaborated with on your course, and what did you plan together? Never present this column as what is needed simply to pass."
- statement: qaa/education-studies-2025/4.5.b9.masters
  forPractitioner: { text: "On a master's course, plan for students to be able to show an excellent ability to plan and carry out effective collaborations with fellow students, staff and wider stakeholders, within and beyond an organisation, treating the column as a guide, as 4.4 asks.", rewrite: light, force: will, status: drafted }
  forBeneficiary: { text: "For a master's degree, you can show an excellent ability to plan and carry out effective collaborations with fellow students, staff and wider stakeholders, within and beyond an organisation.", rewrite: full, force: will, status: drafted }
  author-agent-written: "Write about this as the master's standard for planning and carrying out collaborations at FHEQ Level 7 (FQHEIS Level 11, spine:7), the postgraduate column the statement asks institutions to treat as a guide (4.4). Cite it as QAA, 2025, Education Studies Subject Benchmark Statement, section 4, the standards table after para 4.5, row \"Planning for collaboration\", Postgraduate master's column. Do not present it as a regulatory requirement, as an honours standard or as a merit or distinction band. Set it beside qaa/education-studies-2025/4.5.b9.excellent, the honours cell it reaches past, and the descriptor qaa/fheq-2024/4.17.b8.1 at spine:7 (strand:autonomy)."
  author-agent-dialogue: "Raise it when a master's student or course team asks what is expected for planning and carrying out collaborations. Put it in plain words to a student and, with staff, as a guide the course may adapt, since not every course offers the chance to meet every row. Ask: Which partner outside your organisation have you worked with, and what made it work? Do not read the cell aloud at length or use an honours column for a master's student."
- statement: qaa/education-studies-2025/4.5.b9.typical
  forPractitioner: { text: "Plan for students working at the typical honours level to be able to show a well-developed ability to plan and carry out effective collaborations with fellow students, staff and wider stakeholders.", rewrite: light, force: will, status: drafted }
  forBeneficiary: { text: "At the typical level for an honours degree, you can show a well-developed ability to plan and carry out effective collaborations with fellow students, staff and wider stakeholders.", rewrite: full, force: will, status: drafted }
  author-agent-written: "Write about this as the typical standard, above the threshold for planning and carrying out collaborations, in an honours degree in Education Studies at FHEQ Level 6 (FQHEIS Level 10, spine:6). Cite it as QAA, 2025, Education Studies Subject Benchmark Statement, section 4, the standards table after para 4.5, row \"Planning for collaboration\", Typical standard column. Do not present it as a regulatory requirement or a mark scheme, or as the minimum to pass, and do not apply it to master's awards. Set it beside qaa/education-studies-2025/4.5.b9 and qaa/education-studies-2025/4.5.b9.excellent, the Annex D row qaa/fheq-2024/annex-d/transferable/r2 (the statement ties no class to this column) and the descriptor qaa/fheq-2024/4.15.b9.1 at spine:6 (strand:autonomy)."
  author-agent-dialogue: "Raise it when a student asks what typical work looks like for planning and carrying out collaborations, or when markers compare work across the columns. Tell a student plainly what this level asks of them; with staff, treat it as a description of performance, not a mark scheme. Ask: Who have you collaborated with on your course, and what did you plan together? Never present this column as what is needed simply to pass."
- statement: qaa/education-studies-2025/4.5.b10
  forPractitioner: { text: "Check that every student awarded honours can spot challenges and find suitable ways to resolve them.", rewrite: light, force: threshold, status: drafted }
  forBeneficiary: { text: "To meet the minimum for your honours degree, you can spot challenges and find suitable ways to resolve them.", rewrite: full, force: threshold, status: drafted }
  author-agent-written: "Write about this as the threshold, the least every honours graduate shows for identifying challenges and resolving them, in an honours degree in Education Studies at FHEQ Level 6 (FQHEIS Level 10, spine:6). Cite it as QAA, 2025, Education Studies Subject Benchmark Statement, section 4, the standards table after para 4.5, row \"Solution focus\", Threshold standard column. Do not present it as a regulatory requirement or a mark scheme, and do not apply it to master's awards. Set it beside qaa/education-studies-2025/4.5.b10.typical, the Annex D band qaa/fheq-2024/annex-d/cognitive/r3/3rd (the threshold class) and the descriptor qaa/fheq-2024/4.15.b7 at spine:6 (strand:application)."
  author-agent-dialogue: "Raise it when a student asks what threshold work looks like for identifying challenges and resolving them, or when markers compare work across the columns. Tell a student plainly what this level asks of them; with staff, treat it as a description of performance, not a mark scheme. Ask: Which challenge have you spotted on placement or in a project, and what did you suggest? Make clear that this is the floor every honours graduate reaches, not the target."
- statement: qaa/education-studies-2025/4.5.b10.excellent
  forPractitioner: { text: "Recognise excellent honours work where students can spot challenges, then propose suitable ways to resolve them and lead their use.", rewrite: light, force: will, status: drafted }
  forBeneficiary: { text: "At the excellent level for an honours degree, you can spot challenges, then propose suitable ways to resolve them and lead their use.", rewrite: full, force: will, status: drafted }
  author-agent-written: "Write about this as the excellent standard, the top of the honours range for identifying challenges and resolving them, in an honours degree in Education Studies at FHEQ Level 6 (FQHEIS Level 10, spine:6). Cite it as QAA, 2025, Education Studies Subject Benchmark Statement, section 4, the standards table after para 4.5, row \"Solution focus\", Excellent standard column. Do not present it as a regulatory requirement or a mark scheme, or as the minimum to pass, and do not apply it to master's awards. Set it beside qaa/education-studies-2025/4.5.b10.typical, the Annex D row qaa/fheq-2024/annex-d/cognitive/r3 (the statement ties no class to this column) and the descriptor qaa/fheq-2024/4.15.b7 at spine:6 (strand:application)."
  author-agent-dialogue: "Raise it when a student asks what excellent work looks like for identifying challenges and resolving them, or when markers compare work across the columns. Tell a student plainly what this level asks of them; with staff, treat it as a description of performance, not a mark scheme. Ask: Which challenge have you spotted on placement or in a project, and what did you suggest? Never present this column as what is needed simply to pass."
- statement: qaa/education-studies-2025/4.5.b10.masters
  forPractitioner: { text: "On a master's course, plan for students to be able to understand challenges deeply and propose and use original ways to resolve them, treating the column as a guide, as 4.4 asks.", rewrite: light, force: will, status: drafted }
  forBeneficiary: { text: "For a master's degree, you can understand challenges deeply and propose and use original ways to resolve them.", rewrite: full, force: will, status: drafted }
  author-agent-written: "Write about this as the master's standard for identifying challenges and resolving them at FHEQ Level 7 (FQHEIS Level 11, spine:7), the postgraduate column the statement asks institutions to treat as a guide (4.4). Cite it as QAA, 2025, Education Studies Subject Benchmark Statement, section 4, the standards table after para 4.5, row \"Solution focus\", Postgraduate master's column. Do not present it as a regulatory requirement, as an honours standard or as a merit or distinction band. Set it beside qaa/education-studies-2025/4.5.b10.excellent, the honours cell it reaches past, and the descriptor qaa/fheq-2024/4.17.b5 at spine:7 (strand:application)."
  author-agent-dialogue: "Raise it when a master's student or course team asks what is expected for identifying challenges and resolving them. Put it in plain words to a student and, with staff, as a guide the course may adapt, since not every course offers the chance to meet every row. Ask: What original way of resolving a problem have you proposed and tested? Do not read the cell aloud at length or use an honours column for a master's student."
- statement: qaa/education-studies-2025/4.5.b10.typical
  forPractitioner: { text: "Plan for students working at the typical honours level to be able to spot challenges, then propose and use suitable ways to resolve them.", rewrite: light, force: will, status: drafted }
  forBeneficiary: { text: "At the typical level for an honours degree, you can spot challenges, then propose and use suitable ways to resolve them.", rewrite: full, force: will, status: drafted }
  author-agent-written: "Write about this as the typical standard, above the threshold for identifying challenges and resolving them, in an honours degree in Education Studies at FHEQ Level 6 (FQHEIS Level 10, spine:6). Cite it as QAA, 2025, Education Studies Subject Benchmark Statement, section 4, the standards table after para 4.5, row \"Solution focus\", Typical standard column. Do not present it as a regulatory requirement or a mark scheme, or as the minimum to pass, and do not apply it to master's awards. Set it beside qaa/education-studies-2025/4.5.b10 and qaa/education-studies-2025/4.5.b10.excellent, the Annex D row qaa/fheq-2024/annex-d/cognitive/r3 (the statement ties no class to this column) and the descriptor qaa/fheq-2024/4.15.b7 at spine:6 (strand:application)."
  author-agent-dialogue: "Raise it when a student asks what typical work looks like for identifying challenges and resolving them, or when markers compare work across the columns. Tell a student plainly what this level asks of them; with staff, treat it as a description of performance, not a mark scheme. Ask: Which challenge have you spotted on placement or in a project, and what did you suggest? Never present this column as what is needed simply to pass."
- statement: qaa/education-studies-2025/4.5.b11
  forPractitioner: { text: "Check that every student awarded honours can search for, find and use a range of information, whether written, numerical, visual, spoken or non-verbal, from digital, analogue and empirical sources.", rewrite: light, force: threshold, status: drafted }
  forBeneficiary: { text: "To meet the minimum for your honours degree, you can search for, find and use a range of information, whether written, numerical, visual, spoken or non-verbal, from digital, analogue and empirical sources.", rewrite: full, force: threshold, status: drafted }
  author-agent-written: "Write about this as the threshold, the least every honours graduate shows for finding and using information, in an honours degree in Education Studies at FHEQ Level 6 (FQHEIS Level 10, spine:6). Cite it as QAA, 2025, Education Studies Subject Benchmark Statement, section 4, the standards table after para 4.5, row \"Information retrieval and application\", Threshold standard column. Do not present it as a regulatory requirement or a mark scheme, and do not apply it to master's awards. Set it beside qaa/education-studies-2025/4.5.b11.typical, the Annex D band qaa/fheq-2024/annex-d/cognitive/r1/3rd (the threshold class) and the descriptor qaa/fheq-2024/4.15.b5 at spine:6 (strand:knowledge)."
  author-agent-dialogue: "Raise it when a student asks what threshold work looks like for finding and using information, or when markers compare work across the columns. Tell a student plainly what this level asks of them; with staff, treat it as a description of performance, not a mark scheme. Ask: How did you find the sources for your last assignment, and how did you judge them? Make clear that this is the floor every honours graduate reaches, not the target."
- statement: qaa/education-studies-2025/4.5.b11.excellent
  forPractitioner: { text: "Recognise excellent honours work where students can consistently and with insight search critically for, find and use such a range of information from digital, analogue and empirical sources.", rewrite: light, force: will, status: drafted }
  forBeneficiary: { text: "At the excellent level for an honours degree, you can consistently and with insight search critically for, find and use such a range of information from digital, analogue and empirical sources.", rewrite: full, force: will, status: drafted }
  author-agent-written: "Write about this as the excellent standard, the top of the honours range for finding and using information, in an honours degree in Education Studies at FHEQ Level 6 (FQHEIS Level 10, spine:6). Cite it as QAA, 2025, Education Studies Subject Benchmark Statement, section 4, the standards table after para 4.5, row \"Information retrieval and application\", Excellent standard column. Do not present it as a regulatory requirement or a mark scheme, or as the minimum to pass, and do not apply it to master's awards. Set it beside qaa/education-studies-2025/4.5.b11.typical, the Annex D row qaa/fheq-2024/annex-d/cognitive/r1 (the statement ties no class to this column) and the descriptor qaa/fheq-2024/4.15.b5 at spine:6 (strand:knowledge)."
  author-agent-dialogue: "Raise it when a student asks what excellent work looks like for finding and using information, or when markers compare work across the columns. Tell a student plainly what this level asks of them; with staff, treat it as a description of performance, not a mark scheme. Ask: How did you find the sources for your last assignment, and how did you judge them? Never present this column as what is needed simply to pass."
- statement: qaa/education-studies-2025/4.5.b11.masters
  forPractitioner: { text: "On a master's course, plan for students to be able to apply advanced search techniques to locate a broad spread of information sources, of every kind, and use them critically and with insight, treating the column as a guide, as 4.4 asks.", rewrite: light, force: will, status: drafted }
  forBeneficiary: { text: "For a master's degree, you can apply advanced search techniques to locate a broad spread of information sources, of every kind, and use them critically and with insight.", rewrite: full, force: will, status: drafted }
  author-agent-written: "Write about this as the master's standard for finding and using information at FHEQ Level 7 (FQHEIS Level 11, spine:7), the postgraduate column the statement asks institutions to treat as a guide (4.4). Cite it as QAA, 2025, Education Studies Subject Benchmark Statement, section 4, the standards table after para 4.5, row \"Information retrieval and application\", Postgraduate master's column. Do not present it as a regulatory requirement, as an honours standard or as a merit or distinction band. Set it beside qaa/education-studies-2025/4.5.b11.excellent, the honours cell it reaches past, and the descriptor qaa/fheq-2024/4.17.b2 at spine:7 (strand:knowledge)."
  author-agent-dialogue: "Raise it when a master's student or course team asks what is expected for finding and using information. Put it in plain words to a student and, with staff, as a guide the course may adapt, since not every course offers the chance to meet every row. Ask: Which advanced search technique has changed what you find? Do not read the cell aloud at length or use an honours column for a master's student."
- statement: qaa/education-studies-2025/4.5.b11.typical
  forPractitioner: { text: "Plan for students working at the typical honours level to be able to consistently search critically for, find and use such a range of information from digital, analogue and empirical sources.", rewrite: light, force: will, status: drafted }
  forBeneficiary: { text: "At the typical level for an honours degree, you can consistently search critically for, find and use such a range of information from digital, analogue and empirical sources.", rewrite: full, force: will, status: drafted }
  author-agent-written: "Write about this as the typical standard, above the threshold for finding and using information, in an honours degree in Education Studies at FHEQ Level 6 (FQHEIS Level 10, spine:6). Cite it as QAA, 2025, Education Studies Subject Benchmark Statement, section 4, the standards table after para 4.5, row \"Information retrieval and application\", Typical standard column. Do not present it as a regulatory requirement or a mark scheme, or as the minimum to pass, and do not apply it to master's awards. Set it beside qaa/education-studies-2025/4.5.b11 and qaa/education-studies-2025/4.5.b11.excellent, the Annex D row qaa/fheq-2024/annex-d/cognitive/r1 (the statement ties no class to this column) and the descriptor qaa/fheq-2024/4.15.b5 at spine:6 (strand:knowledge)."
  author-agent-dialogue: "Raise it when a student asks what typical work looks like for finding and using information, or when markers compare work across the columns. Tell a student plainly what this level asks of them; with staff, treat it as a description of performance, not a mark scheme. Ask: How did you find the sources for your last assignment, and how did you judge them? Never present this column as what is needed simply to pass."
- statement: qaa/education-studies-2025/4.5.b12
  forPractitioner: { text: "Check that every student awarded honours can set out and express information, opinions and arguments in speech, writing, visuals and other suitable forms, using the subject's specialist terms.", rewrite: light, force: threshold, status: drafted }
  forBeneficiary: { text: "To meet the minimum for your honours degree, you can set out and express information, opinions and arguments in speech, writing, visuals and other suitable forms, using the subject's specialist terms.", rewrite: full, force: threshold, status: drafted }
  author-agent-written: "Write about this as the threshold, the least every honours graduate shows for communicating and presenting, in an honours degree in Education Studies at FHEQ Level 6 (FQHEIS Level 10, spine:6). Cite it as QAA, 2025, Education Studies Subject Benchmark Statement, section 4, the standards table after para 4.5, row \"Communication and presentation\", Threshold standard column. Do not present it as a regulatory requirement or a mark scheme, and do not apply it to master's awards. Set it beside qaa/education-studies-2025/4.5.b12.typical, the Annex D band qaa/fheq-2024/annex-d/transferable/r1/3rd (the threshold class) and the descriptor qaa/fheq-2024/4.15.b8 at spine:6 (strand:communication)."
  author-agent-dialogue: "Raise it when a student asks what threshold work looks like for communicating and presenting, or when markers compare work across the columns. Tell a student plainly what this level asks of them; with staff, treat it as a description of performance, not a mark scheme. Ask: How do you choose the right words and format for a given audience? Make clear that this is the floor every honours graduate reaches, not the target."
- statement: qaa/education-studies-2025/4.5.b12.excellent
  forPractitioner: { text: "Recognise excellent honours work where students can set out and express information, opinions and arguments in speech, writing, visuals and other suitable forms, using the subject's specialist terms with sophistication.", rewrite: light, force: will, status: drafted }
  forBeneficiary: { text: "At the excellent level for an honours degree, you can set out and express information, opinions and arguments in speech, writing, visuals and other suitable forms, using the subject's specialist terms with sophistication.", rewrite: full, force: will, status: drafted }
  author-agent-written: "Write about this as the excellent standard, the top of the honours range for communicating and presenting, in an honours degree in Education Studies at FHEQ Level 6 (FQHEIS Level 10, spine:6). Cite it as QAA, 2025, Education Studies Subject Benchmark Statement, section 4, the standards table after para 4.5, row \"Communication and presentation\", Excellent standard column. Do not present it as a regulatory requirement or a mark scheme, or as the minimum to pass, and do not apply it to master's awards. Set it beside qaa/education-studies-2025/4.5.b12.typical, the Annex D row qaa/fheq-2024/annex-d/transferable/r1 (the statement ties no class to this column) and the descriptor qaa/fheq-2024/4.15.b8 at spine:6 (strand:communication)."
  author-agent-dialogue: "Raise it when a student asks what excellent work looks like for communicating and presenting, or when markers compare work across the columns. Tell a student plainly what this level asks of them; with staff, treat it as a description of performance, not a mark scheme. Ask: How do you choose the right words and format for a given audience? Never present this column as what is needed simply to pass."
- statement: qaa/education-studies-2025/4.5.b12.masters
  forPractitioner: { text: "On a master's course, plan for students to be able to set out and express information, opinions and arguments in speech, writing, visuals and other suitable forms with sophisticated use of specialist terms, and justify critically why those forms were chosen, treating the column as a guide, as 4.4 asks.", rewrite: light, force: will, status: drafted }
  forBeneficiary: { text: "For a master's degree, you can set out and express information, opinions and arguments in speech, writing, visuals and other suitable forms with sophisticated use of specialist terms, and justify critically why those forms were chosen.", rewrite: full, force: will, status: drafted }
  author-agent-written: "Write about this as the master's standard for communicating and presenting at FHEQ Level 7 (FQHEIS Level 11, spine:7), the postgraduate column the statement asks institutions to treat as a guide (4.4). Cite it as QAA, 2025, Education Studies Subject Benchmark Statement, section 4, the standards table after para 4.5, row \"Communication and presentation\", Postgraduate master's column. Do not present it as a regulatory requirement, as an honours standard or as a merit or distinction band. Set it beside qaa/education-studies-2025/4.5.b12.excellent, the honours cell it reaches past, and the descriptor qaa/fheq-2024/4.17.b5 at spine:7 (strand:communication)."
  author-agent-dialogue: "Raise it when a master's student or course team asks what is expected for communicating and presenting. Put it in plain words to a student and, with staff, as a guide the course may adapt, since not every course offers the chance to meet every row. Ask: Why did you choose the form you used to present your last piece of work? Do not read the cell aloud at length or use an honours column for a master's student."
- statement: qaa/education-studies-2025/4.5.b12.typical
  forPractitioner: { text: "Plan for students working at the typical honours level to be able to set out and express information, opinions and arguments in speech, writing, visuals and other suitable forms, using the subject's specialist terms consistently.", rewrite: light, force: will, status: drafted }
  forBeneficiary: { text: "At the typical level for an honours degree, you can set out and express information, opinions and arguments in speech, writing, visuals and other suitable forms, using the subject's specialist terms consistently.", rewrite: full, force: will, status: drafted }
  author-agent-written: "Write about this as the typical standard, above the threshold for communicating and presenting, in an honours degree in Education Studies at FHEQ Level 6 (FQHEIS Level 10, spine:6). Cite it as QAA, 2025, Education Studies Subject Benchmark Statement, section 4, the standards table after para 4.5, row \"Communication and presentation\", Typical standard column. Do not present it as a regulatory requirement or a mark scheme, or as the minimum to pass, and do not apply it to master's awards. Set it beside qaa/education-studies-2025/4.5.b12 and qaa/education-studies-2025/4.5.b12.excellent, the Annex D row qaa/fheq-2024/annex-d/transferable/r1 (the statement ties no class to this column) and the descriptor qaa/fheq-2024/4.15.b8 at spine:6 (strand:communication)."
  author-agent-dialogue: "Raise it when a student asks what typical work looks like for communicating and presenting, or when markers compare work across the columns. Tell a student plainly what this level asks of them; with staff, treat it as a description of performance, not a mark scheme. Ask: How do you choose the right words and format for a given audience? Never present this column as what is needed simply to pass."
- statement: qaa/education-studies-2025/4.5.b13
  forPractitioner: { text: "Check that every student awarded honours can set out a range of theoretical positions and show how each might bear on educational practice.", rewrite: light, force: threshold, status: drafted }
  forBeneficiary: { text: "To meet the minimum for your honours degree, you can set out a range of theoretical positions and show how each might bear on educational practice.", rewrite: full, force: threshold, status: drafted }
  author-agent-written: "Write about this as the threshold, the least every honours graduate shows for theoretical positions and educational practice, in an honours degree in Education Studies at FHEQ Level 6 (FQHEIS Level 10, spine:6). Cite it as QAA, 2025, Education Studies Subject Benchmark Statement, section 4, the standards table after para 4.5, row \"Application of theory\", Threshold standard column. Do not present it as a regulatory requirement or a mark scheme, and do not apply it to master's awards. Set it beside qaa/education-studies-2025/4.5.b13.typical, the Annex D band qaa/fheq-2024/annex-d/cognitive/r2/3rd (the threshold class) and the descriptor qaa/fheq-2024/4.15.b3.1 at spine:6 (strand:application)."
  author-agent-dialogue: "Raise it when a student asks what threshold work looks like for theoretical positions and educational practice, or when markers compare work across the columns. Tell a student plainly what this level asks of them; with staff, treat it as a description of performance, not a mark scheme. Ask: How might one theory you have studied change what happens in a classroom? Make clear that this is the floor every honours graduate reaches, not the target."
- statement: qaa/education-studies-2025/4.5.b13.excellent
  forPractitioner: { text: "Recognise excellent honours work where students can set out a wide range of theoretical positions and make and justify a critically well-informed case for how each might bear on educational practice.", rewrite: light, force: will, status: drafted }
  forBeneficiary: { text: "At the excellent level for an honours degree, you can set out a wide range of theoretical positions and make and justify a critically well-informed case for how each might bear on educational practice.", rewrite: full, force: will, status: drafted }
  author-agent-written: "Write about this as the excellent standard, the top of the honours range for theoretical positions and educational practice, in an honours degree in Education Studies at FHEQ Level 6 (FQHEIS Level 10, spine:6). Cite it as QAA, 2025, Education Studies Subject Benchmark Statement, section 4, the standards table after para 4.5, row \"Application of theory\", Excellent standard column. Do not present it as a regulatory requirement or a mark scheme, or as the minimum to pass, and do not apply it to master's awards. Set it beside qaa/education-studies-2025/4.5.b13.typical, the Annex D row qaa/fheq-2024/annex-d/cognitive/r2 (the statement ties no class to this column) and the descriptor qaa/fheq-2024/4.15.b3.1 at spine:6 (strand:application)."
  author-agent-dialogue: "Raise it when a student asks what excellent work looks like for theoretical positions and educational practice, or when markers compare work across the columns. Tell a student plainly what this level asks of them; with staff, treat it as a description of performance, not a mark scheme. Ask: How might one theory you have studied change what happens in a classroom? Never present this column as what is needed simply to pass."
- statement: qaa/education-studies-2025/4.5.b13.masters
  forPractitioner: { text: "On a master's course, plan for students to be able to show accurate and detailed knowledge of many theoretical positions and argue for and justify a critical, insightful and well-informed view that has some originality, treating the column as a guide, as 4.4 asks.", rewrite: light, force: will, status: drafted }
  forBeneficiary: { text: "For a master's degree, you can show accurate and detailed knowledge of many theoretical positions and argue for and justify a critical, insightful and well-informed view that has some originality.", rewrite: full, force: will, status: drafted }
  author-agent-written: "Write about this as the master's standard for theoretical positions and educational practice at FHEQ Level 7 (FQHEIS Level 11, spine:7), the postgraduate column the statement asks institutions to treat as a guide (4.4). Cite it as QAA, 2025, Education Studies Subject Benchmark Statement, section 4, the standards table after para 4.5, row \"Application of theory\", Postgraduate master's column. Do not present it as a regulatory requirement, as an honours standard or as a merit or distinction band. Set it beside qaa/education-studies-2025/4.5.b13.excellent, the honours cell it reaches past, and the descriptor qaa/fheq-2024/4.17.b3 at spine:7 (strand:application)."
  author-agent-dialogue: "Raise it when a master's student or course team asks what is expected for theoretical positions and educational practice. Put it in plain words to a student and, with staff, as a guide the course may adapt, since not every course offers the chance to meet every row. Ask: What is original in your view of how theory should shape practice? Do not read the cell aloud at length or use an honours column for a master's student."
- statement: qaa/education-studies-2025/4.5.b13.typical
  forPractitioner: { text: "Plan for students working at the typical honours level to be able to set out a wide range of theoretical positions and make and justify a well-informed case for how each might bear on educational practice.", rewrite: light, force: will, status: drafted }
  forBeneficiary: { text: "At the typical level for an honours degree, you can set out a wide range of theoretical positions and make and justify a well-informed case for how each might bear on educational practice.", rewrite: full, force: will, status: drafted }
  author-agent-written: "Write about this as the typical standard, above the threshold for theoretical positions and educational practice, in an honours degree in Education Studies at FHEQ Level 6 (FQHEIS Level 10, spine:6). Cite it as QAA, 2025, Education Studies Subject Benchmark Statement, section 4, the standards table after para 4.5, row \"Application of theory\", Typical standard column. Do not present it as a regulatory requirement or a mark scheme, or as the minimum to pass, and do not apply it to master's awards. Set it beside qaa/education-studies-2025/4.5.b13 and qaa/education-studies-2025/4.5.b13.excellent, the Annex D row qaa/fheq-2024/annex-d/cognitive/r2 (the statement ties no class to this column) and the descriptor qaa/fheq-2024/4.15.b3.1 at spine:6 (strand:application)."
  author-agent-dialogue: "Raise it when a student asks what typical work looks like for theoretical positions and educational practice, or when markers compare work across the columns. Tell a student plainly what this level asks of them; with staff, treat it as a description of performance, not a mark scheme. Ask: How might one theory you have studied change what happens in a classroom? Never present this column as what is needed simply to pass."
- statement: qaa/education-studies-2025/4.5.b14
  forPractitioner: { text: "Check that every student awarded honours can use digital technologies well and ethically to strengthen a range of approaches to studying education.", rewrite: light, force: threshold, status: drafted }
  forBeneficiary: { text: "To meet the minimum for your honours degree, you can use digital technologies well and ethically to strengthen a range of approaches to studying education.", rewrite: full, force: threshold, status: drafted }
  author-agent-written: "Write about this as the threshold, the least every honours graduate shows for digital technologies, including AI, in study, in an honours degree in Education Studies at FHEQ Level 6 (FQHEIS Level 10, spine:6). Cite it as QAA, 2025, Education Studies Subject Benchmark Statement, section 4, the standards table after para 4.5, row \"Use of digital technologies, including AI\", Threshold standard column. Do not present it as a regulatory requirement or a mark scheme, and do not apply it to master's awards. Set it beside qaa/education-studies-2025/4.5.b14.typical, the Annex D band qaa/fheq-2024/annex-d/transferable/r1/3rd (the threshold class) and the descriptor qaa/fheq-2024/4.15.b2 at spine:6 (strand:application)."
  author-agent-dialogue: "Raise it when a student asks what threshold work looks like for digital technologies, including AI, in study, or when markers compare work across the columns. Tell a student plainly what this level asks of them; with staff, treat it as a description of performance, not a mark scheme. Ask: Which digital tool, AI included, has improved how you study, and where did you draw the line? Make clear that this is the floor every honours graduate reaches, not the target."
- statement: qaa/education-studies-2025/4.5.b14.excellent
  forPractitioner: { text: "Recognise excellent honours work where students can use digital technologies in a sophisticated, ethical, critically informed and effective way to strengthen a range of approaches to studying education.", rewrite: light, force: will, status: drafted }
  forBeneficiary: { text: "At the excellent level for an honours degree, you can use digital technologies in a sophisticated, ethical, critically informed and effective way to strengthen a range of approaches to studying education.", rewrite: full, force: will, status: drafted }
  author-agent-written: "Write about this as the excellent standard, the top of the honours range for digital technologies, including AI, in study, in an honours degree in Education Studies at FHEQ Level 6 (FQHEIS Level 10, spine:6). Cite it as QAA, 2025, Education Studies Subject Benchmark Statement, section 4, the standards table after para 4.5, row \"Use of digital technologies, including AI\", Excellent standard column. Do not present it as a regulatory requirement or a mark scheme, or as the minimum to pass, and do not apply it to master's awards. Set it beside qaa/education-studies-2025/4.5.b14.typical, the Annex D row qaa/fheq-2024/annex-d/transferable/r1 (the statement ties no class to this column) and the descriptor qaa/fheq-2024/4.15.b2 at spine:6 (strand:application)."
  author-agent-dialogue: "Raise it when a student asks what excellent work looks like for digital technologies, including AI, in study, or when markers compare work across the columns. Tell a student plainly what this level asks of them; with staff, treat it as a description of performance, not a mark scheme. Ask: Which digital tool, AI included, has improved how you study, and where did you draw the line? Never present this column as what is needed simply to pass."
- statement: qaa/education-studies-2025/4.5.b14.masters
  forPractitioner: { text: "On a master's course, plan for students to be able to use digital technologies in a sophisticated, ethical, self-directed and critically informed way to strengthen critical and reflective study, treating the column as a guide, as 4.4 asks.", rewrite: light, force: will, status: drafted }
  forBeneficiary: { text: "For a master's degree, you can use digital technologies in a sophisticated, ethical, self-directed and critically informed way to strengthen critical and reflective study.", rewrite: full, force: will, status: drafted }
  author-agent-written: "Write about this as the master's standard for digital technologies, including AI, in study at FHEQ Level 7 (FQHEIS Level 11, spine:7), the postgraduate column the statement asks institutions to treat as a guide (4.4). Cite it as QAA, 2025, Education Studies Subject Benchmark Statement, section 4, the standards table after para 4.5, row \"Use of digital technologies, including AI\", Postgraduate master's column. Do not present it as a regulatory requirement, as an honours standard or as a merit or distinction band. Set it beside qaa/education-studies-2025/4.5.b14.excellent, the honours cell it reaches past, and the descriptor qaa/fheq-2024/4.17.b7 at spine:7 (strand:application)."
  author-agent-dialogue: "Raise it when a master's student or course team asks what is expected for digital technologies, including AI, in study. Put it in plain words to a student and, with staff, as a guide the course may adapt, since not every course offers the chance to meet every row. Ask: How do digital tools, AI included, support your critical and reflective study? Do not read the cell aloud at length or use an honours column for a master's student."
- statement: qaa/education-studies-2025/4.5.b14.typical
  forPractitioner: { text: "Plan for students working at the typical honours level to be able to use digital technologies with confidence, ethically and well, to strengthen in a systematic way a range of approaches to studying education.", rewrite: light, force: will, status: drafted }
  forBeneficiary: { text: "At the typical level for an honours degree, you can use digital technologies with confidence, ethically and well, to strengthen in a systematic way a range of approaches to studying education.", rewrite: full, force: will, status: drafted }
  author-agent-written: "Write about this as the typical standard, above the threshold for digital technologies, including AI, in study, in an honours degree in Education Studies at FHEQ Level 6 (FQHEIS Level 10, spine:6). Cite it as QAA, 2025, Education Studies Subject Benchmark Statement, section 4, the standards table after para 4.5, row \"Use of digital technologies, including AI\", Typical standard column. Do not present it as a regulatory requirement or a mark scheme, or as the minimum to pass, and do not apply it to master's awards. Set it beside qaa/education-studies-2025/4.5.b14 and qaa/education-studies-2025/4.5.b14.excellent, the Annex D row qaa/fheq-2024/annex-d/transferable/r1 (the statement ties no class to this column) and the descriptor qaa/fheq-2024/4.15.b2 at spine:6 (strand:application)."
  author-agent-dialogue: "Raise it when a student asks what typical work looks like for digital technologies, including AI, in study, or when markers compare work across the columns. Tell a student plainly what this level asks of them; with staff, treat it as a description of performance, not a mark scheme. Ask: Which digital tool, AI included, has improved how you study, and where did you draw the line? Never present this column as what is needed simply to pass."
- statement: qaa/education-studies-2025/4.5.b15
  forPractitioner: { text: "Check that every student awarded honours can show how to process, order and express opinions and arguments so as to build, present and defend a chosen stance that draws on relevant perspectives.", rewrite: light, force: threshold, status: drafted }
  forBeneficiary: { text: "To meet the minimum for your honours degree, you can show how to process, order and express opinions and arguments so as to build, present and defend a chosen stance that draws on relevant perspectives.", rewrite: full, force: threshold, status: drafted }
  author-agent-written: "Write about this as the threshold, the least every honours graduate shows for building and justifying a position, in an honours degree in Education Studies at FHEQ Level 6 (FQHEIS Level 10, spine:6). Cite it as QAA, 2025, Education Studies Subject Benchmark Statement, section 4, the standards table after para 4.5, row \"Analytical and creative competence\", Threshold standard column. Do not present it as a regulatory requirement or a mark scheme, and do not apply it to master's awards. Set it beside qaa/education-studies-2025/4.5.b15.typical, the Annex D band qaa/fheq-2024/annex-d/cognitive/r2/3rd (the threshold class) and the descriptor qaa/fheq-2024/4.15.b7 at spine:6 (strand:thinking)."
  author-agent-dialogue: "Raise it when a student asks what threshold work looks like for building and justifying a position, or when markers compare work across the columns. Tell a student plainly what this level asks of them; with staff, treat it as a description of performance, not a mark scheme. Ask: What position have you argued for, and which perspectives did you draw on? Make clear that this is the floor every honours graduate reaches, not the target."
- statement: qaa/education-studies-2025/4.5.b15.excellent
  forPractitioner: { text: "Recognise excellent honours work where students can show a deep grasp of how to process, synthesise, order and express opinions and arguments from varied sources so as to form new syntheses and argue for and defend a chosen stance.", rewrite: light, force: will, status: drafted }
  forBeneficiary: { text: "At the excellent level for an honours degree, you can show a deep grasp of how to process, synthesise, order and express opinions and arguments from varied sources so as to form new syntheses and argue for and defend a chosen stance.", rewrite: full, force: will, status: drafted }
  author-agent-written: "Write about this as the excellent standard, the top of the honours range for building and justifying a position, in an honours degree in Education Studies at FHEQ Level 6 (FQHEIS Level 10, spine:6). Cite it as QAA, 2025, Education Studies Subject Benchmark Statement, section 4, the standards table after para 4.5, row \"Analytical and creative competence\", Excellent standard column. Do not present it as a regulatory requirement or a mark scheme, or as the minimum to pass, and do not apply it to master's awards. Set it beside qaa/education-studies-2025/4.5.b15.typical, the Annex D row qaa/fheq-2024/annex-d/cognitive/r2 (the statement ties no class to this column) and the descriptor qaa/fheq-2024/4.15.b7 at spine:6 (strand:thinking)."
  author-agent-dialogue: "Raise it when a student asks what excellent work looks like for building and justifying a position, or when markers compare work across the columns. Tell a student plainly what this level asks of them; with staff, treat it as a description of performance, not a mark scheme. Ask: What position have you argued for, and which perspectives did you draw on? Never present this column as what is needed simply to pass."
- statement: qaa/education-studies-2025/4.5.b15.masters
  forPractitioner: { text: "On a master's course, plan for students to be able to show a critical grasp of how to process, synthesise, order and express opinions and arguments from varied sources so as to form new syntheses and argue for and defend a chosen stance, treating the column as a guide, as 4.4 asks.", rewrite: light, force: will, status: drafted }
  forBeneficiary: { text: "For a master's degree, you can show a critical grasp of how to process, synthesise, order and express opinions and arguments from varied sources so as to form new syntheses and argue for and defend a chosen stance.", rewrite: full, force: will, status: drafted }
  author-agent-written: "Write about this as the master's standard for building and justifying a position at FHEQ Level 7 (FQHEIS Level 11, spine:7), the postgraduate column the statement asks institutions to treat as a guide (4.4). Cite it as QAA, 2025, Education Studies Subject Benchmark Statement, section 4, the standards table after para 4.5, row \"Analytical and creative competence\", Postgraduate master's column. Do not present it as a regulatory requirement, as an honours standard or as a merit or distinction band. Set it beside qaa/education-studies-2025/4.5.b15.excellent, the honours cell it reaches past, and the descriptor qaa/fheq-2024/4.17.b5 at spine:7 (strand:thinking)."
  author-agent-dialogue: "Raise it when a master's student or course team asks what is expected for building and justifying a position. Put it in plain words to a student and, with staff, as a guide the course may adapt, since not every course offers the chance to meet every row. Ask: Which new synthesis of sources did your last argument produce? Do not read the cell aloud at length or use an honours column for a master's student."
- statement: qaa/education-studies-2025/4.5.b15.typical
  forPractitioner: { text: "Plan for students working at the typical honours level to be able to show a sound grasp of how to process, synthesise, order and express opinions and arguments, drawing on varied sources, to argue for and defend a chosen stance grounded in theory.", rewrite: light, force: will, status: drafted }
  forBeneficiary: { text: "At the typical level for an honours degree, you can show a sound grasp of how to process, synthesise, order and express opinions and arguments, drawing on varied sources, to argue for and defend a chosen stance grounded in theory.", rewrite: full, force: will, status: drafted }
  author-agent-written: "Write about this as the typical standard, above the threshold for building and justifying a position, in an honours degree in Education Studies at FHEQ Level 6 (FQHEIS Level 10, spine:6). Cite it as QAA, 2025, Education Studies Subject Benchmark Statement, section 4, the standards table after para 4.5, row \"Analytical and creative competence\", Typical standard column. Do not present it as a regulatory requirement or a mark scheme, or as the minimum to pass, and do not apply it to master's awards. Set it beside qaa/education-studies-2025/4.5.b15 and qaa/education-studies-2025/4.5.b15.excellent, the Annex D row qaa/fheq-2024/annex-d/cognitive/r2 (the statement ties no class to this column) and the descriptor qaa/fheq-2024/4.15.b7 at spine:6 (strand:thinking)."
  author-agent-dialogue: "Raise it when a student asks what typical work looks like for building and justifying a position, or when markers compare work across the columns. Tell a student plainly what this level asks of them; with staff, treat it as a description of performance, not a mark scheme. Ask: What position have you argued for, and which perspectives did you draw on? Never present this column as what is needed simply to pass."
- statement: qaa/education-studies-2025/4.5.b16
  forPractitioner: { text: "Check that every student awarded honours can show how to communicate well through respectful exchanges with diverse groups, and plan work within a set role that builds trust in a team and meets agreed responsibilities.", rewrite: light, force: threshold, status: drafted }
  forBeneficiary: { text: "To meet the minimum for your honours degree, you can show how to communicate well through respectful exchanges with diverse groups, and plan work within a set role that builds trust in a team and meets agreed responsibilities.", rewrite: full, force: threshold, status: drafted }
  author-agent-written: "Write about this as the threshold, the least every honours graduate shows for communicating and working in a team, in an honours degree in Education Studies at FHEQ Level 6 (FQHEIS Level 10, spine:6). Cite it as QAA, 2025, Education Studies Subject Benchmark Statement, section 4, the standards table after para 4.5, row \"Collaboration\", Threshold standard column. Do not present it as a regulatory requirement or a mark scheme, and do not apply it to master's awards. Set it beside qaa/education-studies-2025/4.5.b16.typical, the Annex D band qaa/fheq-2024/annex-d/transferable/r2/3rd (the threshold class) and the descriptor qaa/fheq-2024/4.15.b9.1 at spine:6 (strand:communication)."
  author-agent-dialogue: "Raise it when a student asks what threshold work looks like for communicating and working in a team, or when markers compare work across the columns. Tell a student plainly what this level asks of them; with staff, treat it as a description of performance, not a mark scheme. Ask: What role did you take in your last team, and how did you build trust? Make clear that this is the floor every honours graduate reaches, not the target."
- statement: qaa/education-studies-2025/4.5.b16.excellent
  forPractitioner: { text: "Recognise excellent honours work where students can show a deep grasp of how to communicate well through respectful exchanges with diverse groups, and plan work within a set role that builds trust in a team and meets agreed responsibilities.", rewrite: light, force: will, status: drafted }
  forBeneficiary: { text: "At the excellent level for an honours degree, you can show a deep grasp of how to communicate well through respectful exchanges with diverse groups, and plan work within a set role that builds trust in a team and meets agreed responsibilities.", rewrite: full, force: will, status: drafted }
  author-agent-written: "Write about this as the excellent standard, the top of the honours range for communicating and working in a team, in an honours degree in Education Studies at FHEQ Level 6 (FQHEIS Level 10, spine:6). Cite it as QAA, 2025, Education Studies Subject Benchmark Statement, section 4, the standards table after para 4.5, row \"Collaboration\", Excellent standard column. Do not present it as a regulatory requirement or a mark scheme, or as the minimum to pass, and do not apply it to master's awards. Set it beside qaa/education-studies-2025/4.5.b16.typical, the Annex D row qaa/fheq-2024/annex-d/transferable/r2 (the statement ties no class to this column) and the descriptor qaa/fheq-2024/4.15.b9.1 at spine:6 (strand:communication)."
  author-agent-dialogue: "Raise it when a student asks what excellent work looks like for communicating and working in a team, or when markers compare work across the columns. Tell a student plainly what this level asks of them; with staff, treat it as a description of performance, not a mark scheme. Ask: What role did you take in your last team, and how did you build trust? Never present this column as what is needed simply to pass."
- statement: qaa/education-studies-2025/4.5.b16.masters
  forPractitioner: { text: "On a master's course, plan for students to be able to show a critical grasp of how to communicate well through respectful exchanges with diverse groups, and plan work within a set role that builds trust in a team and meets agreed responsibilities, treating the column as a guide, as 4.4 asks.", rewrite: light, force: will, status: drafted }
  forBeneficiary: { text: "For a master's degree, you can show a critical grasp of how to communicate well through respectful exchanges with diverse groups, and plan work within a set role that builds trust in a team and meets agreed responsibilities.", rewrite: full, force: will, status: drafted }
  author-agent-written: "Write about this as the master's standard for communicating and working in a team at FHEQ Level 7 (FQHEIS Level 11, spine:7), the postgraduate column the statement asks institutions to treat as a guide (4.4). Cite it as QAA, 2025, Education Studies Subject Benchmark Statement, section 4, the standards table after para 4.5, row \"Collaboration\", Postgraduate master's column. Do not present it as a regulatory requirement, as an honours standard or as a merit or distinction band. Set it beside qaa/education-studies-2025/4.5.b16.excellent, the honours cell it reaches past, and the descriptor qaa/fheq-2024/4.17.b8.1 at spine:7 (strand:communication)."
  author-agent-dialogue: "Raise it when a master's student or course team asks what is expected for communicating and working in a team. Put it in plain words to a student and, with staff, as a guide the course may adapt, since not every course offers the chance to meet every row. Ask: How have you helped a diverse team to trust one another and deliver? Do not read the cell aloud at length or use an honours column for a master's student."
- statement: qaa/education-studies-2025/4.5.b16.typical
  forPractitioner: { text: "Plan for students working at the typical honours level to be able to show a sound grasp of how to communicate well through respectful exchanges with diverse groups, and plan work within a set role that builds trust in a team and meets agreed responsibilities.", rewrite: light, force: will, status: drafted }
  forBeneficiary: { text: "At the typical level for an honours degree, you can show a sound grasp of how to communicate well through respectful exchanges with diverse groups, and plan work within a set role that builds trust in a team and meets agreed responsibilities.", rewrite: full, force: will, status: drafted }
  author-agent-written: "Write about this as the typical standard, above the threshold for communicating and working in a team, in an honours degree in Education Studies at FHEQ Level 6 (FQHEIS Level 10, spine:6). Cite it as QAA, 2025, Education Studies Subject Benchmark Statement, section 4, the standards table after para 4.5, row \"Collaboration\", Typical standard column. Do not present it as a regulatory requirement or a mark scheme, or as the minimum to pass, and do not apply it to master's awards. Set it beside qaa/education-studies-2025/4.5.b16 and qaa/education-studies-2025/4.5.b16.excellent, the Annex D row qaa/fheq-2024/annex-d/transferable/r2 (the statement ties no class to this column) and the descriptor qaa/fheq-2024/4.15.b9.1 at spine:6 (strand:communication)."
  author-agent-dialogue: "Raise it when a student asks what typical work looks like for communicating and working in a team, or when markers compare work across the columns. Tell a student plainly what this level asks of them; with staff, treat it as a description of performance, not a mark scheme. Ask: What role did you take in your last team, and how did you build trust? Never present this column as what is needed simply to pass."
- statement: qaa/education-studies-2025/4.5.b17
  forPractitioner: { text: "Check that every student awarded honours can show how to get information from suitable sources with a critical eye on those sources, the proper use of digital tools and software, ethical awareness and an understanding of staying safe online.", rewrite: light, force: threshold, status: drafted }
  forBeneficiary: { text: "To meet the minimum for your honours degree, you can show how to get information from suitable sources with a critical eye on those sources, the proper use of digital tools and software, ethical awareness and an understanding of staying safe online.", rewrite: full, force: threshold, status: drafted }
  author-agent-written: "Write about this as the threshold, the least every honours graduate shows for accessing information safely and ethically, in an honours degree in Education Studies at FHEQ Level 6 (FQHEIS Level 10, spine:6). Cite it as QAA, 2025, Education Studies Subject Benchmark Statement, section 4, the standards table after para 4.5, row \"Data access skills (analogue and digital)\", Threshold standard column. Do not present it as a regulatory requirement or a mark scheme, and do not apply it to master's awards. Set it beside qaa/education-studies-2025/4.5.b17.typical, the Annex D band qaa/fheq-2024/annex-d/practical/r4/3rd (the threshold class) and the descriptor qaa/fheq-2024/4.15.b5 at spine:6 (strand:knowledge)."
  author-agent-dialogue: "Raise it when a student asks what threshold work looks like for accessing information safely and ethically, or when markers compare work across the columns. Tell a student plainly what this level asks of them; with staff, treat it as a description of performance, not a mark scheme. Ask: How do you check that an online source is trustworthy, and how do you keep yourself safe online? Make clear that this is the floor every honours graduate reaches, not the target."
- statement: qaa/education-studies-2025/4.5.b17.excellent
  forPractitioner: { text: "Recognise excellent honours work where students can show a deep grasp of how to get information from suitable sources with a critical eye on those sources, the proper use of digital tools and software, ethical awareness and an understanding of staying safe online.", rewrite: light, force: will, status: drafted }
  forBeneficiary: { text: "At the excellent level for an honours degree, you can show a deep grasp of how to get information from suitable sources with a critical eye on those sources, the proper use of digital tools and software, ethical awareness and an understanding of staying safe online.", rewrite: full, force: will, status: drafted }
  author-agent-written: "Write about this as the excellent standard, the top of the honours range for accessing information safely and ethically, in an honours degree in Education Studies at FHEQ Level 6 (FQHEIS Level 10, spine:6). Cite it as QAA, 2025, Education Studies Subject Benchmark Statement, section 4, the standards table after para 4.5, row \"Data access skills (analogue and digital)\", Excellent standard column. Do not present it as a regulatory requirement or a mark scheme, or as the minimum to pass, and do not apply it to master's awards. Set it beside qaa/education-studies-2025/4.5.b17.typical, the Annex D row qaa/fheq-2024/annex-d/practical/r4 (the statement ties no class to this column) and the descriptor qaa/fheq-2024/4.15.b5 at spine:6 (strand:knowledge)."
  author-agent-dialogue: "Raise it when a student asks what excellent work looks like for accessing information safely and ethically, or when markers compare work across the columns. Tell a student plainly what this level asks of them; with staff, treat it as a description of performance, not a mark scheme. Ask: How do you check that an online source is trustworthy, and how do you keep yourself safe online? Never present this column as what is needed simply to pass."
- statement: qaa/education-studies-2025/4.5.b17.masters
  forPractitioner: { text: "On a master's course, plan for students to be able to show a systematic grasp of how to get information from suitable sources with a critical eye on those sources, the proper use of digital tools and software, ethical awareness and an understanding of staying safe online, treating the column as a guide, as 4.4 asks.", rewrite: light, force: will, status: drafted }
  forBeneficiary: { text: "For a master's degree, you can show a systematic grasp of how to get information from suitable sources with a critical eye on those sources, the proper use of digital tools and software, ethical awareness and an understanding of staying safe online.", rewrite: full, force: will, status: drafted }
  author-agent-written: "Write about this as the master's standard for accessing information safely and ethically at FHEQ Level 7 (FQHEIS Level 11, spine:7), the postgraduate column the statement asks institutions to treat as a guide (4.4). Cite it as QAA, 2025, Education Studies Subject Benchmark Statement, section 4, the standards table after para 4.5, row \"Data access skills (analogue and digital)\", Postgraduate master's column. Do not present it as a regulatory requirement, as an honours standard or as a merit or distinction band. Set it beside qaa/education-studies-2025/4.5.b17.excellent, the honours cell it reaches past, and the descriptor qaa/fheq-2024/4.17.b2 at spine:7 (strand:knowledge)."
  author-agent-dialogue: "Raise it when a master's student or course team asks what is expected for accessing information safely and ethically. Put it in plain words to a student and, with staff, as a guide the course may adapt, since not every course offers the chance to meet every row. Ask: How do you judge the reliability of the information systems your work depends on? Do not read the cell aloud at length or use an honours column for a master's student."
- statement: qaa/education-studies-2025/4.5.b17.typical
  forPractitioner: { text: "Plan for students working at the typical honours level to be able to show a sound grasp of how to get information from suitable sources with a critical eye on those sources, the proper use of digital tools and software, ethical awareness and an understanding of staying safe online.", rewrite: light, force: will, status: drafted }
  forBeneficiary: { text: "At the typical level for an honours degree, you can show a sound grasp of how to get information from suitable sources with a critical eye on those sources, the proper use of digital tools and software, ethical awareness and an understanding of staying safe online.", rewrite: full, force: will, status: drafted }
  author-agent-written: "Write about this as the typical standard, above the threshold for accessing information safely and ethically, in an honours degree in Education Studies at FHEQ Level 6 (FQHEIS Level 10, spine:6). Cite it as QAA, 2025, Education Studies Subject Benchmark Statement, section 4, the standards table after para 4.5, row \"Data access skills (analogue and digital)\", Typical standard column. Do not present it as a regulatory requirement or a mark scheme, or as the minimum to pass, and do not apply it to master's awards. Set it beside qaa/education-studies-2025/4.5.b17 and qaa/education-studies-2025/4.5.b17.excellent, the Annex D row qaa/fheq-2024/annex-d/practical/r4 (the statement ties no class to this column) and the descriptor qaa/fheq-2024/4.15.b5 at spine:6 (strand:knowledge)."
  author-agent-dialogue: "Raise it when a student asks what typical work looks like for accessing information safely and ethically, or when markers compare work across the columns. Tell a student plainly what this level asks of them; with staff, treat it as a description of performance, not a mark scheme. Ask: How do you check that an online source is trustworthy, and how do you keep yourself safe online? Never present this column as what is needed simply to pass."
- statement: qaa/education-studies-2025/4.5.b18
  forPractitioner: { text: "Check that every student awarded honours can show how to gather data, then analyse, interpret, apply and present it in varied verbal and non-verbal forms, suited to the task and audience and handled ethically.", rewrite: light, force: threshold, status: drafted }
  forBeneficiary: { text: "To meet the minimum for your honours degree, you can show how to gather data, then analyse, interpret, apply and present it in varied verbal and non-verbal forms, suited to the task and audience and handled ethically.", rewrite: full, force: threshold, status: drafted }
  author-agent-written: "Write about this as the threshold, the least every honours graduate shows for working with data across formats, in an honours degree in Education Studies at FHEQ Level 6 (FQHEIS Level 10, spine:6). Cite it as QAA, 2025, Education Studies Subject Benchmark Statement, section 4, the standards table after para 4.5, row \"Hybrid literacies\", Threshold standard column. Do not present it as a regulatory requirement or a mark scheme, and do not apply it to master's awards. Set it beside qaa/education-studies-2025/4.5.b18.typical, the Annex D band qaa/fheq-2024/annex-d/practical/r4/3rd (the threshold class) and the descriptor qaa/fheq-2024/4.15.b8 at spine:6 (strand:communication)."
  author-agent-dialogue: "Raise it when a student asks what threshold work looks like for working with data across formats, or when markers compare work across the columns. Tell a student plainly what this level asks of them; with staff, treat it as a description of performance, not a mark scheme. Ask: How did you present the data in your last project, and why that format? Make clear that this is the floor every honours graduate reaches, not the target."
- statement: qaa/education-studies-2025/4.5.b18.excellent
  forPractitioner: { text: "Recognise excellent honours work where students can show a deep grasp of analysing, interpreting, applying and presenting data in varied verbal and non-verbal forms, suited to the task and audience and handled ethically.", rewrite: light, force: will, status: drafted }
  forBeneficiary: { text: "At the excellent level for an honours degree, you can show a deep grasp of analysing, interpreting, applying and presenting data in varied verbal and non-verbal forms, suited to the task and audience and handled ethically.", rewrite: full, force: will, status: drafted }
  author-agent-written: "Write about this as the excellent standard, the top of the honours range for working with data across formats, in an honours degree in Education Studies at FHEQ Level 6 (FQHEIS Level 10, spine:6). Cite it as QAA, 2025, Education Studies Subject Benchmark Statement, section 4, the standards table after para 4.5, row \"Hybrid literacies\", Excellent standard column. Do not present it as a regulatory requirement or a mark scheme, or as the minimum to pass, and do not apply it to master's awards. Set it beside qaa/education-studies-2025/4.5.b18.typical, the Annex D row qaa/fheq-2024/annex-d/practical/r4 (the statement ties no class to this column) and the descriptor qaa/fheq-2024/4.15.b8 at spine:6 (strand:communication)."
  author-agent-dialogue: "Raise it when a student asks what excellent work looks like for working with data across formats, or when markers compare work across the columns. Tell a student plainly what this level asks of them; with staff, treat it as a description of performance, not a mark scheme. Ask: How did you present the data in your last project, and why that format? Never present this column as what is needed simply to pass."
- statement: qaa/education-studies-2025/4.5.b18.masters
  forPractitioner: { text: "On a master's course, plan for students to be able to show a critical grasp of analysing, interpreting, applying and presenting data in varied verbal and non-verbal forms, suited to the task and audience and handled ethically, treating the column as a guide, as 4.4 asks.", rewrite: light, force: will, status: drafted }
  forBeneficiary: { text: "For a master's degree, you can show a critical grasp of analysing, interpreting, applying and presenting data in varied verbal and non-verbal forms, suited to the task and audience and handled ethically.", rewrite: full, force: will, status: drafted }
  author-agent-written: "Write about this as the master's standard for working with data across formats at FHEQ Level 7 (FQHEIS Level 11, spine:7), the postgraduate column the statement asks institutions to treat as a guide (4.4). Cite it as QAA, 2025, Education Studies Subject Benchmark Statement, section 4, the standards table after para 4.5, row \"Hybrid literacies\", Postgraduate master's column. Do not present it as a regulatory requirement, as an honours standard or as a merit or distinction band. Set it beside qaa/education-studies-2025/4.5.b18.excellent, the honours cell it reaches past, and the descriptor qaa/fheq-2024/4.17.b5 at spine:7 (strand:communication)."
  author-agent-dialogue: "Raise it when a master's student or course team asks what is expected for working with data across formats. Put it in plain words to a student and, with staff, as a guide the course may adapt, since not every course offers the chance to meet every row. Ask: How do you make complex data clear and ethical for a given audience? Do not read the cell aloud at length or use an honours column for a master's student."
- statement: qaa/education-studies-2025/4.5.b18.typical
  forPractitioner: { text: "Plan for students working at the typical honours level to be able to show a sound grasp of analysing, interpreting, applying and presenting data in varied verbal and non-verbal forms, suited to the task and audience and handled ethically.", rewrite: light, force: will, status: drafted }
  forBeneficiary: { text: "At the typical level for an honours degree, you can show a sound grasp of analysing, interpreting, applying and presenting data in varied verbal and non-verbal forms, suited to the task and audience and handled ethically.", rewrite: full, force: will, status: drafted }
  author-agent-written: "Write about this as the typical standard, above the threshold for working with data across formats, in an honours degree in Education Studies at FHEQ Level 6 (FQHEIS Level 10, spine:6). Cite it as QAA, 2025, Education Studies Subject Benchmark Statement, section 4, the standards table after para 4.5, row \"Hybrid literacies\", Typical standard column. Do not present it as a regulatory requirement or a mark scheme, or as the minimum to pass, and do not apply it to master's awards. Set it beside qaa/education-studies-2025/4.5.b18 and qaa/education-studies-2025/4.5.b18.excellent, the Annex D row qaa/fheq-2024/annex-d/practical/r4 (the statement ties no class to this column) and the descriptor qaa/fheq-2024/4.15.b8 at spine:6 (strand:communication)."
  author-agent-dialogue: "Raise it when a student asks what typical work looks like for working with data across formats, or when markers compare work across the columns. Tell a student plainly what this level asks of them; with staff, treat it as a description of performance, not a mark scheme. Ask: How did you present the data in your last project, and why that format? Never present this column as what is needed simply to pass."
- statement: qaa/education-studies-2025/4.5.b19
  forPractitioner: { text: "Check that every student awarded honours can show flexibility, adaptability and the personal responsibility to keep up self-reflection and learning throughout life, seeing why empathy, active listening and action matter.", rewrite: light, force: threshold, status: drafted }
  forBeneficiary: { text: "To meet the minimum for your honours degree, you can show flexibility, adaptability and the personal responsibility to keep up self-reflection and learning throughout life, seeing why empathy, active listening and action matter.", rewrite: full, force: threshold, status: drafted }
  author-agent-written: "Write about this as the threshold, the least every honours graduate shows for flexibility, self-reflection and lifelong learning, in an honours degree in Education Studies at FHEQ Level 6 (FQHEIS Level 10, spine:6). Cite it as QAA, 2025, Education Studies Subject Benchmark Statement, section 4, the standards table after para 4.5, row \"Personal competences\", Threshold standard column. Do not present it as a regulatory requirement or a mark scheme, and do not apply it to master's awards. Set it beside qaa/education-studies-2025/4.5.b19.typical, the Annex D band qaa/fheq-2024/annex-d/transferable/r3/3rd (the threshold class) and the descriptor qaa/fheq-2024/4.15.b9.3 at spine:6 (strand:autonomy)."
  author-agent-dialogue: "Raise it when a student asks what threshold work looks like for flexibility, self-reflection and lifelong learning, or when markers compare work across the columns. Tell a student plainly what this level asks of them; with staff, treat it as a description of performance, not a mark scheme. Ask: When did you have to adapt quickly, and what did you learn about yourself? Make clear that this is the floor every honours graduate reaches, not the target."
- statement: qaa/education-studies-2025/4.5.b19.excellent
  forPractitioner: { text: "Recognise excellent honours work where students can show a deep grasp of flexibility, adaptability and the personal responsibility to keep up self-reflection and learning throughout life, seeing why empathy, active listening and action matter.", rewrite: light, force: will, status: drafted }
  forBeneficiary: { text: "At the excellent level for an honours degree, you can show a deep grasp of flexibility, adaptability and the personal responsibility to keep up self-reflection and learning throughout life, seeing why empathy, active listening and action matter.", rewrite: full, force: will, status: drafted }
  author-agent-written: "Write about this as the excellent standard, the top of the honours range for flexibility, self-reflection and lifelong learning, in an honours degree in Education Studies at FHEQ Level 6 (FQHEIS Level 10, spine:6). Cite it as QAA, 2025, Education Studies Subject Benchmark Statement, section 4, the standards table after para 4.5, row \"Personal competences\", Excellent standard column. Do not present it as a regulatory requirement or a mark scheme, or as the minimum to pass, and do not apply it to master's awards. Set it beside qaa/education-studies-2025/4.5.b19.typical, the Annex D row qaa/fheq-2024/annex-d/transferable/r3 (the statement ties no class to this column) and the descriptor qaa/fheq-2024/4.15.b9.3 at spine:6 (strand:autonomy)."
  author-agent-dialogue: "Raise it when a student asks what excellent work looks like for flexibility, self-reflection and lifelong learning, or when markers compare work across the columns. Tell a student plainly what this level asks of them; with staff, treat it as a description of performance, not a mark scheme. Ask: When did you have to adapt quickly, and what did you learn about yourself? Never present this column as what is needed simply to pass."
- statement: qaa/education-studies-2025/4.5.b19.masters
  forPractitioner: { text: "On a master's course, plan for students to be able to show a systematic grasp of flexibility, adaptability and the personal responsibility to keep up self-reflection and learning throughout life, seeing why empathy, active listening and action matter, treating the column as a guide, as 4.4 asks.", rewrite: light, force: will, status: drafted }
  forBeneficiary: { text: "For a master's degree, you can show a systematic grasp of flexibility, adaptability and the personal responsibility to keep up self-reflection and learning throughout life, seeing why empathy, active listening and action matter.", rewrite: full, force: will, status: drafted }
  author-agent-written: "Write about this as the master's standard for flexibility, self-reflection and lifelong learning at FHEQ Level 7 (FQHEIS Level 11, spine:7), the postgraduate column the statement asks institutions to treat as a guide (4.4). Cite it as QAA, 2025, Education Studies Subject Benchmark Statement, section 4, the standards table after para 4.5, row \"Personal competences\", Postgraduate master's column. Do not present it as a regulatory requirement, as an honours standard or as a merit or distinction band. Set it beside qaa/education-studies-2025/4.5.b19.excellent, the honours cell it reaches past, and the descriptor qaa/fheq-2024/4.17.b8.3 at spine:7 (strand:autonomy)."
  author-agent-dialogue: "Raise it when a master's student or course team asks what is expected for flexibility, self-reflection and lifelong learning. Put it in plain words to a student and, with staff, as a guide the course may adapt, since not every course offers the chance to meet every row. Ask: How do you keep learning and reflecting in your professional life? Do not read the cell aloud at length or use an honours column for a master's student."
- statement: qaa/education-studies-2025/4.5.b19.typical
  forPractitioner: { text: "Plan for students working at the typical honours level to be able to show a sound grasp of flexibility, adaptability and the personal responsibility to keep up self-reflection and learning throughout life, seeing why empathy, active listening and action matter.", rewrite: light, force: will, status: drafted }
  forBeneficiary: { text: "At the typical level for an honours degree, you can show a sound grasp of flexibility, adaptability and the personal responsibility to keep up self-reflection and learning throughout life, seeing why empathy, active listening and action matter.", rewrite: full, force: will, status: drafted }
  author-agent-written: "Write about this as the typical standard, above the threshold for flexibility, self-reflection and lifelong learning, in an honours degree in Education Studies at FHEQ Level 6 (FQHEIS Level 10, spine:6). Cite it as QAA, 2025, Education Studies Subject Benchmark Statement, section 4, the standards table after para 4.5, row \"Personal competences\", Typical standard column. Do not present it as a regulatory requirement or a mark scheme, or as the minimum to pass, and do not apply it to master's awards. Set it beside qaa/education-studies-2025/4.5.b19 and qaa/education-studies-2025/4.5.b19.excellent, the Annex D row qaa/fheq-2024/annex-d/transferable/r3 (the statement ties no class to this column) and the descriptor qaa/fheq-2024/4.15.b9.3 at spine:6 (strand:autonomy)."
  author-agent-dialogue: "Raise it when a student asks what typical work looks like for flexibility, self-reflection and lifelong learning, or when markers compare work across the columns. Tell a student plainly what this level asks of them; with staff, treat it as a description of performance, not a mark scheme. Ask: When did you have to adapt quickly, and what did you learn about yourself? Never present this column as what is needed simply to pass."
- statement: qaa/education-studies-2025/4.5.b20
  forPractitioner: { text: "Check that every student awarded honours can show engagement in processes of change, foreseeing and reconciling tensions, dilemmas and complexity, and grasp what futures thinking means.", rewrite: light, force: threshold, status: drafted }
  forBeneficiary: { text: "To meet the minimum for your honours degree, you can show engagement in processes of change, foreseeing and reconciling tensions, dilemmas and complexity, and grasp what futures thinking means.", rewrite: full, force: threshold, status: drafted }
  author-agent-written: "Write about this as the threshold, the least every honours graduate shows for taking part in change; futures thinking, in an honours degree in Education Studies at FHEQ Level 6 (FQHEIS Level 10, spine:6). Cite it as QAA, 2025, Education Studies Subject Benchmark Statement, section 4, the standards table after para 4.5, row \"Transformative competences\", Threshold standard column. Do not present it as a regulatory requirement or a mark scheme, and do not apply it to master's awards. Set it beside qaa/education-studies-2025/4.5.b20.typical, the Annex D band qaa/fheq-2024/annex-d/transferable/r4/3rd (the threshold class) and the descriptor qaa/fheq-2024/4.15.b9.2 at spine:6 (strand:autonomy)."
  author-agent-dialogue: "Raise it when a student asks what threshold work looks like for taking part in change; futures thinking, or when markers compare work across the columns. Tell a student plainly what this level asks of them; with staff, treat it as a description of performance, not a mark scheme. Ask: What change in education have you been part of, and what tensions did it raise? Make clear that this is the floor every honours graduate reaches, not the target."
- statement: qaa/education-studies-2025/4.5.b20.excellent
  forPractitioner: { text: "Recognise excellent honours work where students can show a deep grasp of how to take part in processes of change, foreseeing and reconciling tensions, dilemmas and complexity, and grasp what futures thinking means.", rewrite: light, force: will, status: drafted }
  forBeneficiary: { text: "At the excellent level for an honours degree, you can show a deep grasp of how to take part in processes of change, foreseeing and reconciling tensions, dilemmas and complexity, and grasp what futures thinking means.", rewrite: full, force: will, status: drafted }
  author-agent-written: "Write about this as the excellent standard, the top of the honours range for taking part in change; futures thinking, in an honours degree in Education Studies at FHEQ Level 6 (FQHEIS Level 10, spine:6). Cite it as QAA, 2025, Education Studies Subject Benchmark Statement, section 4, the standards table after para 4.5, row \"Transformative competences\", Excellent standard column. Do not present it as a regulatory requirement or a mark scheme, or as the minimum to pass, and do not apply it to master's awards. Set it beside qaa/education-studies-2025/4.5.b20.typical, the Annex D row qaa/fheq-2024/annex-d/transferable/r4 (the statement ties no class to this column) and the descriptor qaa/fheq-2024/4.15.b9.2 at spine:6 (strand:autonomy)."
  author-agent-dialogue: "Raise it when a student asks what excellent work looks like for taking part in change; futures thinking, or when markers compare work across the columns. Tell a student plainly what this level asks of them; with staff, treat it as a description of performance, not a mark scheme. Ask: What change in education have you been part of, and what tensions did it raise? Never present this column as what is needed simply to pass."
- statement: qaa/education-studies-2025/4.5.b20.masters
  forPractitioner: { text: "On a master's course, plan for students to be able to show a systematic grasp of how to take part in processes of change, foreseeing and reconciling tensions, dilemmas and complexity, and grasp what futures thinking means, treating the column as a guide, as 4.4 asks.", rewrite: light, force: will, status: drafted }
  forBeneficiary: { text: "For a master's degree, you can show a systematic grasp of how to take part in processes of change, foreseeing and reconciling tensions, dilemmas and complexity, and grasp what futures thinking means.", rewrite: full, force: will, status: drafted }
  author-agent-written: "Write about this as the master's standard for taking part in change; futures thinking at FHEQ Level 7 (FQHEIS Level 11, spine:7), the postgraduate column the statement asks institutions to treat as a guide (4.4). Cite it as QAA, 2025, Education Studies Subject Benchmark Statement, section 4, the standards table after para 4.5, row \"Transformative competences\", Postgraduate master's column. Do not present it as a regulatory requirement, as an honours standard or as a merit or distinction band. Set it beside qaa/education-studies-2025/4.5.b20.excellent, the honours cell it reaches past, and the descriptor qaa/fheq-2024/4.17.b8.2 at spine:7 (strand:autonomy)."
  author-agent-dialogue: "Raise it when a master's student or course team asks what is expected for taking part in change; futures thinking. Put it in plain words to a student and, with staff, as a guide the course may adapt, since not every course offers the chance to meet every row. Ask: How would you use futures thinking to plan a change in your setting? Do not read the cell aloud at length or use an honours column for a master's student."
- statement: qaa/education-studies-2025/4.5.b20.typical
  forPractitioner: { text: "Plan for students working at the typical honours level to be able to show a sound grasp of how to take part in processes of change, foreseeing and reconciling tensions, dilemmas and complexity, and grasp what futures thinking means.", rewrite: light, force: will, status: drafted }
  forBeneficiary: { text: "At the typical level for an honours degree, you can show a sound grasp of how to take part in processes of change, foreseeing and reconciling tensions, dilemmas and complexity, and grasp what futures thinking means.", rewrite: full, force: will, status: drafted }
  author-agent-written: "Write about this as the typical standard, above the threshold for taking part in change; futures thinking, in an honours degree in Education Studies at FHEQ Level 6 (FQHEIS Level 10, spine:6). Cite it as QAA, 2025, Education Studies Subject Benchmark Statement, section 4, the standards table after para 4.5, row \"Transformative competences\", Typical standard column. Do not present it as a regulatory requirement or a mark scheme, or as the minimum to pass, and do not apply it to master's awards. Set it beside qaa/education-studies-2025/4.5.b20 and qaa/education-studies-2025/4.5.b20.excellent, the Annex D row qaa/fheq-2024/annex-d/transferable/r4 (the statement ties no class to this column) and the descriptor qaa/fheq-2024/4.15.b9.2 at spine:6 (strand:autonomy)."
  author-agent-dialogue: "Raise it when a student asks what typical work looks like for taking part in change; futures thinking, or when markers compare work across the columns. Tell a student plainly what this level asks of them; with staff, treat it as a description of performance, not a mark scheme. Ask: What change in education have you been part of, and what tensions did it raise? Never present this column as what is needed simply to pass."
- statement: qaa/education-studies-2025/4.7
  forPractitioner: { text: "Where the course carries PSRB accreditation that assesses professional competencies, make clear to students that the accredited award will not be made without them, and assess them separately from the academic standards.", rewrite: light, force: will, status: drafted }
  forBeneficiary: { text: "If your course leads to an award accredited by a professional body, you will not receive that accredited award unless you meet its professional competencies.", rewrite: full, force: will, status: drafted }
  author-agent-written: "Write about this as an expected outcome or feature worded with \"will\" or \"can\" for the honours degree, at FHEQ Level 6 (FQHEIS Level 10, spine:6), on professional competence as a condition of a PSRB-accredited award. Cite it as QAA, 2025, Education Studies Subject Benchmark Statement, para 4.7. Do not claim it is a regulatory requirement, a rung of the standards table or a standard at another level. Set it beside qaa/education-studies-2025/4.5 and the framework descriptor qaa/fheq-2024/4.15.b1 and 4.15.b9.3."
  author-agent-dialogue: "Bring it up when a student asks about professional competence as a condition of a PSRB-accredited award, or when staff check a module or outcome against it. Tell a student in plain words, as 'you', what it means for their course; for staff, frame it as an expected outcome or feature worded with \"will\" or \"can\". Ask: Does your course lead to a professionally accredited award, and do you know which competencies it assesses? Avoid long quotation of the issuer's text."
- statement: qaa/education-studies-2025/4.7.b1
  forPractitioner: { text: "On a PSRB-accredited course, record a pass on this row only where the student has been assessed against the body's requirements and met them.", rewrite: light, force: threshold, status: drafted }
  forBeneficiary: { text: "To succeed on a professionally accredited route, you need to have shown your professional competence when it is judged against the professional body's requirements.", rewrite: full, force: threshold, status: drafted }
  author-agent-written: "Write about this as a pass condition on a professionally accredited honours route at FHEQ Level 6 (FQHEIS Level 10, spine:6): professional competence met. Cite it as QAA, 2025, Education Studies Subject Benchmark Statement, para 4.7, the professional competences table, \"Successful\" column. Do not apply it to courses without PSRB accreditation or present it as an academic grade. Set it beside qaa/education-studies-2025/4.7, qaa/education-studies-2025/4.7.b1 and qaa/education-studies-2025/4.7.b2 together, and the Annex D row qaa/fheq-2024/annex-d/professional/r1/3rd-1st it reproduces."
  author-agent-dialogue: "Raise it only with a student or team on a professionally accredited route, when they ask what the professional body needs. Put it plainly as pass or not, separate from the academic standards. Ask: Which professional body assesses your competence, and how will you be judged against its requirements? Do not suggest it applies to every Education Studies student."
- statement: qaa/education-studies-2025/4.7.b2
  forPractitioner: { text: "On a PSRB-accredited course, check that the student has kept to the rules and conventions regulators or the sector set, and record failure to do so as not successful.", rewrite: light, force: threshold, status: drafted }
  forBeneficiary: { text: "To succeed on a professionally accredited route, you need to have kept to the rules and conventions that regulators or the sector set.", rewrite: full, force: threshold, status: drafted }
  author-agent-written: "Write about this as a pass condition on a professionally accredited honours route at FHEQ Level 6 (FQHEIS Level 10, spine:6): keeping to regulators' and industry rules. Cite it as QAA, 2025, Education Studies Subject Benchmark Statement, para 4.7, the professional competences table, \"Successful\" column. Do not apply it to courses without PSRB accreditation or present it as an academic grade. Set it beside qaa/education-studies-2025/4.7, qaa/education-studies-2025/4.7.b1 and qaa/education-studies-2025/4.7.b2 together, and the Annex D row qaa/fheq-2024/annex-d/professional/r2/3rd-1st it reproduces."
  author-agent-dialogue: "Raise it only with a student or team on a professionally accredited route, when they ask what the professional body needs. Put it plainly as pass or not, separate from the academic standards. Ask: Which rules or conventions from regulators or the sector apply to your practice, and how do you show you keep them? Do not suggest it applies to every Education Studies student."
```

### S5 Levels and alignment
<!-- label: both; status: drafted; basis: primary -->
```yaml
levels:
  - { id: "fheq:6", role: "cites", locator: "D1, 2.2 (honours); the honours columns of the table (4.3)" }
  - { id: "fqheis:10", role: "cites", locator: "D1, 2.2" }
  - { id: "fheq:7", role: "cites", locator: "D1, 2.2 (integrated master's); 4.4 (Level 7, framework not named)" }
  - { id: "fqheis:11", role: "cites", locator: "D1, 2.2; 4.4 (Level 11 in Scotland)" }
  - { id: "fheq:4", role: "cites", locator: "D1, 2.5 (CertHE exit award)" }
  - { id: "fqheis:8", role: "cites", locator: "D1, 2.5 (given for the CertHE; Part E)" }
  - { id: "fheq:5", role: "cites", locator: "D1, 2.5 (DipHE exit award)" }
  - { id: "fqheis:9", role: "cites", locator: "D1, 2.5 (given for the DipHE; Part E)" }
crosswalks:
  - { from: "fheq:6", to: "fqheis:10", relation: "equivalent", basis: "stated (D1, 2.2: honours at FHEQ Level 6, FQHEIS Level 10)" }
  - { from: "fheq:7", to: "fqheis:11", relation: "equivalent", basis: "stated (D1, 2.2: integrated master's at FHEQ Level 7, FQHEIS Level 11; 4.4: Level 7 and Level 11)" }
  - { from: "fheq:4", to: "fqheis:8", relation: "equivalent", basis: "stated (D1, 2.5, CertHE); the FHEQ document's Table 1 gives the CertHE at fqheis:7 (Part E)" }
  - { from: "fheq:5", to: "fqheis:9", relation: "equivalent", basis: "stated (D1, 2.5, DipHE); the FHEQ document's Table 1 gives the DipHE at fqheis:8 (Part E)" }
  - { from: "threshold column", to: "Annex D 3rd (threshold)", relation: "thresholdAt", basis: "inferred: 4.3 sends institutions to Annex D for evidence; the statement ties no class to typical or excellent" }
```

### S6 Themes
<!-- label: both; status: drafted; basis: primary -->
```yaml
- { id: "theme:edi", role: "carries", carriedIn: ["front matter", "1.7", "1.8", "1.9", "1.10", "1.11", "1.12", "1.13", "1.14", "1.20", "3.10", "3.12", "3.15", "3.19"] }
- { id: "theme:accessibility", role: "carries", carriedIn: ["front matter", "1.7", "1.15", "1.16", "1.17", "1.18", "1.19", "1.20", "1.21", "1.22", "1.23", "1.24", "1.42", "3.10", "3.12", "3.19", "4.5"] }
- { id: "theme:esd", role: "carries", carriedIn: ["front matter", "1.4", "1.25", "1.26", "1.27", "1.28", "1.29", "1.30", "1.31", "1.42", "3.6", "3.15"] }
- { id: "theme:enterprise", role: "carries", carriedIn: ["front matter", "1.32", "1.33", "1.34", "1.35", "1.36", "1.37", "1.38", "1.39", "1.40", "2.1", "3.10", "3.12", "3.15"] }
- { id: "theme:generative-ai", role: "carries", carriedIn: ["front matter", "1.14", "1.41", "1.42", "1.43", "3.8", "3.10", "3.15", "3.18", "section 4 table, row \"Use of digital technologies, including AI\""] }
```

### S7 Relations
<!-- label: both; status: drafted; basis: primary -->
```yaml
- { rel: "partOf", target: "collection: QAA Subject Benchmark Statements", note: "one of 54 held by stan" }
- { rel: "supersedes", target: "std:doc:qaa-education-studies-2019-benchmarks (not held)", note: "the front matter lists key changes from the previous statement; advisory groups are named for 2019 (minor update), 2015, 2007 and 2000 (back matter)" }
- { rel: "refersTo", target: "std:doc:qaa-fheq-2024-framework, Annex D", note: "4.3: institutions should refer to Annex D when deciding what evidence shows the standards are met" }
- { rel: "refersTo", target: "std:doc:qaa-fheq-2024-framework", note: "levels 4 to 7 (2.2, 2.5, 4.4)" }
- { rel: "refersTo", target: "std:doc:qaa-fqheis-2024-framework", note: "levels 8 to 11 (2.2, 2.5, 4.4)" }
- { rel: "themeReference", target: "std:doc:qaa-advancehe-esd-2021-guidance", note: "1.26: named as a resource for shaping the offer (the QAA and Advance HE Education for Sustainable Development Guidance)" }
- { rel: "refersTo", target: "QAA Quality Code (2024) (not ingested)", note: "front matter" }
- { rel: "refersTo", target: "Equality Act 2010 (law; not a standards document)", note: "1.15, 1.22, 4.5" }
- { rel: "refersTo", target: "PSRB requirements (not yet ingested)", note: "front matter, 2.8, 2.11, 3.14, 3.17, 3.22, 4.5, 4.7" }
```

### S8 Currency and review
<!-- label: source; status: drafted; basis: primary -->
```yaml
published: "2025-04"
lastReviewed: "none-stated"
reviewCycle: "none-stated"
consultation: "none-stated; an advisory group and a student focus group are listed (back matter)"
replacedBy: "none"
```

### S9 Commentary (optional)
<!-- label: editorial; status: drafted; basis: secondary -->
`unknown`: not researched in P1 (Part E).

### SB1 The subject
<!-- label: both; status: drafted; basis: primary -->
- Education Studies studies how people develop and learn across their lives, the nature of knowledge and ways of knowing and educational processes and systems in their cultural, social, technological, political, philosophical, environmental, historical and economic settings, always with critique of policy and practice (D1, 1.1).
- It joins theory and scholarly practice (praxis) and aims to change lives and society for the better, preparing students to act as agents of change (D1, 1.2).
- It can be read as a subject defined by content, a field drawing on psychology, sociology, philosophy, history, language, politics and economics, or a discipline with its own discourses and methods (D1, 1.3).
- Ethics runs through all of it, and it is always changing (D1, 1.4).
- Learning is reciprocal: students bring diverse perspectives that feed critical debate (D1, 1.5).
- It treats education in its widest sense, well beyond schools, colleges and universities, and its graduates go into many sectors, not only teaching (D1, 1.35, 1.36).
- Its curriculum spans three overlapping areas, subject-specific, practice-based and transversal, where transformative learning happens at their meeting point (D1, 3.3, 3.4, Figure 1).

### SB2 Themes in this subject
<!-- label: both; status: drafted; basis: primary -->
```yaml
- theme: theme:edi
  inThisSubject: "EDI as a founding tenet of the field: co-constructed equitable curricula, questioning dominant language and knowledge, defining a position on justice, reflection with respect for others and EDI in the use of digital technologies (D1, 1.7 to 1.14, 3.12)"
  statements: ["qaa/education-studies-2025/1.9", "qaa/education-studies-2025/1.11", "qaa/education-studies-2025/1.13", "qaa/education-studies-2025/3.10.b6", "qaa/education-studies-2025/3.10.b12"]
- theme: theme:accessibility
  inThisSubject: "an inclusive discipline open to all: the Equality Act duty to anticipate, accessibility a must in design, anticipatory adjustments, digital access and assistive technology, accessible placements and competence standards under the Equality Act (D1, 1.15 to 1.24, 3.19, 4.5)"
  statements: ["qaa/education-studies-2025/1.15", "qaa/education-studies-2025/1.16", "qaa/education-studies-2025/1.20", "qaa/education-studies-2025/1.21", "qaa/education-studies-2025/1.22", "qaa/education-studies-2025/1.23", "qaa/education-studies-2025/1.24", "qaa/education-studies-2025/3.10.b12", "qaa/education-studies-2025/4.5"]
- theme: theme:esd
  inThisSubject: "education as a driver of sustainable practice, the UN SDGs (SDG 4 in particular), interdisciplinary knowledge of sustainability and students' personal sustainability and well-being (D1, 1.25 to 1.31, 3.6)"
  statements: ["qaa/education-studies-2025/1.30", "qaa/education-studies-2025/1.31"]
- theme: theme:enterprise
  inThisSubject: "employability, entrepreneurship and enterprise embedded rather than added, for destinations far beyond teaching, with an ethical entrepreneurial disposition (D1, 1.32 to 1.40, 2.1, 3.12)"
  statements: ["qaa/education-studies-2025/3.10.b13"]
- theme: theme:generative-ai
  inThisSubject: "artificial intelligence as its own theme: eleven principles for critical, ethical and transparent use, applied by course teams across the programme, academic integrity in assessment and a standards row on digital technologies including AI (D1, 1.41 to 1.43, 3.18; the standards table)"
  statements: ["qaa/education-studies-2025/1.43", "qaa/education-studies-2025/3.10.b22", "qaa/education-studies-2025/4.5.b14", "qaa/education-studies-2025/4.5.b14.typical", "qaa/education-studies-2025/4.5.b14.excellent", "qaa/education-studies-2025/4.5.b14.masters"]
```

### SB3 Content and delivery
<!-- label: both; status: drafted; basis: primary -->
```yaml
areas:
  - { component: "3.3", gloss: "three curricular areas: subject-specific, practice-based and transversal, shown in Figure 1" }
  - { component: "3.6", gloss: "twenty subject-specific knowledge areas, from research methods and curriculum design to safeguarding, SEND, social justice and educational technologies" }
  - { component: "3.8", gloss: "fourteen practice-based opportunities: adapting practice, reasonable adjustments, ethics, safeguarding, student voice, technology, reflection, observation" }
  - { component: "3.10", gloss: "twenty-three transversal areas, from numeracy and communication to self-care, AI and collaboration" }
practices:
  - { component: "3.11", kind: "teaching", gloss: "inclusive, interactive and reflective methods drawing on practice, theory and evidence" }
  - { component: "3.12", kind: "learning", gloss: "independent learning, self-assessment, accessibility, support services, employability, inclusive environment, scaffolding" }
  - { component: "3.13", kind: "teaching", gloss: "programmes modelling effective teaching practice" }
  - { component: "3.17", kind: "assessment", gloss: "twenty-three methods, from posters and podcasts to game-based outputs, portfolios and vivas" }
  - { component: "3.18", kind: "assessment", gloss: "academic integrity, especially with GenAI" }
  - { component: "3.19", kind: "assessment", gloss: "accessible and inclusive assessment; student well-being" }
  - { component: "3.21", kind: "assessment", gloss: "authentic assessment in real-world settings" }
  - { component: "3.22", kind: "assessment", gloss: "assessed placements and work-based practice with reflection" }
  - { component: "3.24", kind: "assessment", gloss: "formative and summative feedback that looks forward" }
```

### SB4 Benchmark standards
<!-- label: both; status: drafted; basis: primary -->
```yaml
rungs:
  - { rung: "threshold", leadIn: "4.3", award: "bachelor's with honours", items: 20, label: "Threshold standard" }
  - { rung: "typical", leadIn: "4.3", award: "bachelor's with honours", items: 20, label: "Typical standard" }
  - { rung: "excellent", leadIn: "4.3", award: "bachelor's with honours", items: 20, label: "Excellent standard" }
  - { rung: "threshold", leadIn: "4.4", award: "master's", items: 20, label: "Postgraduate master's (read as the master's threshold: 4.3, 4.4)" }
  - { rung: "threshold", leadIn: "4.7", award: "bachelor's with honours", items: 2, label: "Professional competences, Successful (PSRB-accredited routes only)" }
rungBases: "4.3: the threshold standards set the minimum every student completing an honours or master's course can show; most perform well above it; the tables also describe typical and excellent undergraduate performance, and institutions refer to Annex D for evidence. 4.4: the postgraduate column is for a master's at Level 7 (Level 11 in Scotland), to be used as a guide only. One table after 4.5 lists twenty rows in three groups (Subject-specific skills: Knowledge and understanding, 10 rows; Practical and practice-based skills, 4 rows; Transversal skills: Transferable competences, 6 rows), each across the four columns; the issuer pairs the cells by row. 4.6 and 4.7 add a pass-or-not row for professional competence that reproduces Annex D's professional rows."
outcomeLists:
  - { leadIn: "3.10", gloss: "twenty-three transversal areas course teams should consider", items: 23, award: ["bachelor's with honours"] }
outcomes:
  - { outcome: "Knowledge: theories, concepts and ideas about education", threshold: "qaa/education-studies-2025/4.5.b1", typical: "qaa/education-studies-2025/4.5.b1.typical", excellent: "qaa/education-studies-2025/4.5.b1.excellent", masters: "qaa/education-studies-2025/4.5.b1.masters", basis: "stated", domain: "knowledge", award: "bachelor's with honours" }
  - { outcome: "Critical awareness: the uncertainty and limits of knowledge in education", threshold: "qaa/education-studies-2025/4.5.b2", typical: "qaa/education-studies-2025/4.5.b2.typical", excellent: "qaa/education-studies-2025/4.5.b2.excellent", masters: "qaa/education-studies-2025/4.5.b2.masters", basis: "stated", domain: "understanding", award: "bachelor's with honours" }
  - { outcome: "Critical evaluation: critical questions and arguments about education", threshold: "qaa/education-studies-2025/4.5.b3", typical: "qaa/education-studies-2025/4.5.b3.typical", excellent: "qaa/education-studies-2025/4.5.b3.excellent", masters: "qaa/education-studies-2025/4.5.b3.masters", basis: "stated", domain: "subject-skill", award: "bachelor's with honours" }
  - { outcome: "Application: applying theory to real problems in education", threshold: "qaa/education-studies-2025/4.5.b4", typical: "qaa/education-studies-2025/4.5.b4.typical", excellent: "qaa/education-studies-2025/4.5.b4.excellent", masters: "qaa/education-studies-2025/4.5.b4.masters", basis: "stated", domain: "subject-skill", award: "bachelor's with honours" }
  - { outcome: "Ethical awareness: ethical tensions in education", threshold: "qaa/education-studies-2025/4.5.b5", typical: "qaa/education-studies-2025/4.5.b5.typical", excellent: "qaa/education-studies-2025/4.5.b5.excellent", masters: "qaa/education-studies-2025/4.5.b5.masters", basis: "stated", domain: "understanding", award: "bachelor's with honours" }
  - { outcome: "Evaluate own learning skills: evaluating own learning skills", threshold: "qaa/education-studies-2025/4.5.b6", typical: "qaa/education-studies-2025/4.5.b6.typical", excellent: "qaa/education-studies-2025/4.5.b6.excellent", masters: "qaa/education-studies-2025/4.5.b6.masters", basis: "stated", domain: "subject-skill", award: "bachelor's with honours" }
  - { outcome: "Study skills: methods for systematic study and research", threshold: "qaa/education-studies-2025/4.5.b7", typical: "qaa/education-studies-2025/4.5.b7.typical", excellent: "qaa/education-studies-2025/4.5.b7.excellent", masters: "qaa/education-studies-2025/4.5.b7.masters", basis: "stated", domain: "subject-skill", award: "bachelor's with honours" }
  - { outcome: "Creativity: creative approaches to studying education", threshold: "qaa/education-studies-2025/4.5.b8", typical: "qaa/education-studies-2025/4.5.b8.typical", excellent: "qaa/education-studies-2025/4.5.b8.excellent", masters: "qaa/education-studies-2025/4.5.b8.masters", basis: "stated", domain: "subject-skill", award: "bachelor's with honours" }
  - { outcome: "Planning for collaboration: planning and carrying out collaborations", threshold: "qaa/education-studies-2025/4.5.b9", typical: "qaa/education-studies-2025/4.5.b9.typical", excellent: "qaa/education-studies-2025/4.5.b9.excellent", masters: "qaa/education-studies-2025/4.5.b9.masters", basis: "stated", domain: "subject-skill", award: "bachelor's with honours" }
  - { outcome: "Solution focus: identifying challenges and resolving them", threshold: "qaa/education-studies-2025/4.5.b10", typical: "qaa/education-studies-2025/4.5.b10.typical", excellent: "qaa/education-studies-2025/4.5.b10.excellent", masters: "qaa/education-studies-2025/4.5.b10.masters", basis: "stated", domain: "subject-skill", award: "bachelor's with honours" }
  - { outcome: "Information retrieval and application: finding and using information", threshold: "qaa/education-studies-2025/4.5.b11", typical: "qaa/education-studies-2025/4.5.b11.typical", excellent: "qaa/education-studies-2025/4.5.b11.excellent", masters: "qaa/education-studies-2025/4.5.b11.masters", basis: "stated", domain: "subject-skill", award: "bachelor's with honours" }
  - { outcome: "Communication and presentation: communicating and presenting", threshold: "qaa/education-studies-2025/4.5.b12", typical: "qaa/education-studies-2025/4.5.b12.typical", excellent: "qaa/education-studies-2025/4.5.b12.excellent", masters: "qaa/education-studies-2025/4.5.b12.masters", basis: "stated", domain: "subject-skill", award: "bachelor's with honours" }
  - { outcome: "Application of theory: theoretical positions and educational practice", threshold: "qaa/education-studies-2025/4.5.b13", typical: "qaa/education-studies-2025/4.5.b13.typical", excellent: "qaa/education-studies-2025/4.5.b13.excellent", masters: "qaa/education-studies-2025/4.5.b13.masters", basis: "stated", domain: "subject-skill", award: "bachelor's with honours" }
  - { outcome: "Use of digital technologies, including AI: digital technologies, including AI, in study", threshold: "qaa/education-studies-2025/4.5.b14", typical: "qaa/education-studies-2025/4.5.b14.typical", excellent: "qaa/education-studies-2025/4.5.b14.excellent", masters: "qaa/education-studies-2025/4.5.b14.masters", basis: "stated", domain: "subject-skill", award: "bachelor's with honours" }
  - { outcome: "Analytical and creative competence: building and justifying a position", threshold: "qaa/education-studies-2025/4.5.b15", typical: "qaa/education-studies-2025/4.5.b15.typical", excellent: "qaa/education-studies-2025/4.5.b15.excellent", masters: "qaa/education-studies-2025/4.5.b15.masters", basis: "stated", domain: "generic-skill", award: "bachelor's with honours" }
  - { outcome: "Collaboration: communicating and working in a team", threshold: "qaa/education-studies-2025/4.5.b16", typical: "qaa/education-studies-2025/4.5.b16.typical", excellent: "qaa/education-studies-2025/4.5.b16.excellent", masters: "qaa/education-studies-2025/4.5.b16.masters", basis: "stated", domain: "generic-skill", award: "bachelor's with honours" }
  - { outcome: "Data access skills (analogue and digital): accessing information safely and ethically", threshold: "qaa/education-studies-2025/4.5.b17", typical: "qaa/education-studies-2025/4.5.b17.typical", excellent: "qaa/education-studies-2025/4.5.b17.excellent", masters: "qaa/education-studies-2025/4.5.b17.masters", basis: "stated", domain: "generic-skill", award: "bachelor's with honours" }
  - { outcome: "Hybrid literacies: working with data across formats", threshold: "qaa/education-studies-2025/4.5.b18", typical: "qaa/education-studies-2025/4.5.b18.typical", excellent: "qaa/education-studies-2025/4.5.b18.excellent", masters: "qaa/education-studies-2025/4.5.b18.masters", basis: "stated", domain: "generic-skill", award: "bachelor's with honours" }
  - { outcome: "Personal competences: flexibility, self-reflection and lifelong learning", threshold: "qaa/education-studies-2025/4.5.b19", typical: "qaa/education-studies-2025/4.5.b19.typical", excellent: "qaa/education-studies-2025/4.5.b19.excellent", masters: "qaa/education-studies-2025/4.5.b19.masters", basis: "stated", domain: "generic-skill", award: "bachelor's with honours" }
  - { outcome: "Transformative competences: taking part in change; futures thinking", threshold: "qaa/education-studies-2025/4.5.b20", typical: "qaa/education-studies-2025/4.5.b20.typical", excellent: "qaa/education-studies-2025/4.5.b20.excellent", masters: "qaa/education-studies-2025/4.5.b20.masters", basis: "stated", domain: "generic-skill", award: "bachelor's with honours" }
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
- { body: "professional, statutory and regulatory bodies (PSRBs)", says: "the statement can support their definitions of academic standards; courses may be delivered with them, may need their evaluation and accreditation, may align to their requirements; a PSRB-accredited award is not made without the professional competencies they assess (D1, front matter, 2.8, 2.11, 3.14, 3.17, 3.22, 4.5, 4.7)", requirements: "not yet ingested (Part E)" }
- { body: "Office for Students", says: "in England the statement is not a sector-recognised standard under its regulatory framework (D1, front matter)", requirements: "not-applicable-by-design" }
- { body: "Equality and Human Rights Commission", says: "providers writing competence standards should follow its latest guidance (D1, 4.5)", requirements: "not-applicable-by-design: guidance, not course requirements" }
```

### SB6 Cross-cutting references
<!-- label: both; status: drafted; basis: primary -->
```yaml
themes:
  - { id: "theme:edi", named: "Equity, diversity and inclusion (EDI)", carriedIn: ["front matter", "1.7", "1.8", "1.9", "1.10", "1.11", "1.12", "1.13", "1.14", "1.20", "3.10", "3.12", "3.15", "3.19"], statements: ["qaa/education-studies-2025/1.9", "qaa/education-studies-2025/1.11", "qaa/education-studies-2025/1.13", "qaa/education-studies-2025/3.10.b6", "qaa/education-studies-2025/3.10.b12"] }
  - { id: "theme:accessibility", named: "Accessibility and the needs of disabled students", carriedIn: ["front matter", "1.7", "1.15", "1.16", "1.17", "1.18", "1.19", "1.20", "1.21", "1.22", "1.23", "1.24", "1.42", "3.10", "3.12", "3.19", "4.5"], statements: ["qaa/education-studies-2025/1.15", "qaa/education-studies-2025/1.16", "qaa/education-studies-2025/1.20", "qaa/education-studies-2025/1.21", "qaa/education-studies-2025/1.22", "qaa/education-studies-2025/1.23", "qaa/education-studies-2025/1.24", "qaa/education-studies-2025/3.10.b12", "qaa/education-studies-2025/4.5"] }
  - { id: "theme:esd", named: "Education for sustainable development", carriedIn: ["front matter", "1.4", "1.25", "1.26", "1.27", "1.28", "1.29", "1.30", "1.31", "1.42", "3.6", "3.15"], statements: ["qaa/education-studies-2025/1.30", "qaa/education-studies-2025/1.31"] }
  - { id: "theme:enterprise", named: "Employability, entrepreneurship and enterprise education", carriedIn: ["front matter", "1.32", "1.33", "1.34", "1.35", "1.36", "1.37", "1.38", "1.39", "1.40", "2.1", "3.10", "3.12", "3.15"], statements: ["qaa/education-studies-2025/3.10.b13"] }
  - { id: "theme:generative-ai", named: "Artificial intelligence (front matter: generative artificial intelligence)", carriedIn: ["front matter", "1.14", "1.41", "1.42", "1.43", "3.8", "3.10", "3.15", "3.18", "section 4 table, row \"Use of digital technologies, including AI\""], statements: ["qaa/education-studies-2025/1.43", "qaa/education-studies-2025/3.10.b22", "qaa/education-studies-2025/4.5.b14", "qaa/education-studies-2025/4.5.b14.typical", "qaa/education-studies-2025/4.5.b14.excellent", "qaa/education-studies-2025/4.5.b14.masters"] }
frameworks:
  - { framework: "fheq", levels: ["fheq:4", "fheq:5", "fheq:6", "fheq:7"], citedIn: ["2.2", "2.5", "4.3", "4.4"] }
  - { framework: "scqf", levels: ["fqheis:8", "fqheis:9", "fqheis:10", "fqheis:11"], citedIn: ["2.2", "2.5", "4.4"] }
bodies:
  - { body: "PSRBs (generic)", citedIn: ["front matter", "2.8", "2.11", "3.14", "3.17", "3.22", "4.5", "4.7"] }
  - { body: "Office for Students", citedIn: ["front matter"] }
  - { body: "Equality and Human Rights Commission", citedIn: ["4.5"] }
sharedDocuments:
  - { document: "std:doc:qaa-fheq-2024-framework, Annex D", named: "Annex D in The Frameworks for Higher Education Qualifications of UK Degree-Awarding Bodies", citedIn: ["4.3", "4.6", "4.7"], role: "evidence of achievement against the standards (4.3); the professional competence rows reproduced in 4.6 and 4.7" }
  - { document: "std:doc:qaa-advancehe-esd-2021-guidance", named: "the QAA and Advance HE Education for Sustainable Development Guidance", citedIn: ["1.26"], role: "a resource for the sustainability theme" }
  - { document: "QAA Quality Code 2024 (not ingested)", named: "the Quality Code (2024 update)", citedIn: ["front matter"], role: "sector reference point read with the statement" }
  - { document: "QAA Glossary (not ingested)", named: "QAA's Glossary", citedIn: ["front matter"], role: "explains unfamiliar terms" }
  - { document: "std:doc:qaa-education-studies-2019-benchmarks (not held)", named: "the previous Subject Benchmark Statement", citedIn: ["front matter"], role: "the edition this one revises" }
  - { document: "UN Sustainable Development Goals (external)", named: "the current United Nations Sustainable Development Goals (SDG 4 Quality Education)", citedIn: ["1.26"], role: "frame for the sustainability theme" }
  - { document: "Equality Act 2010 (law)", named: "The Equality Act 2010", citedIn: ["1.15", "1.22", "4.5"], role: "the anticipatory duty, reasonable adjustments and competence standards" }
```

## Part B Terminology
<!-- The statement has no glossary of its own unless Part E says so; these are terms it defines in its text. -->

### B1 Concepts
<!-- label: both; status: drafted; basis: primary -->
```yaml
- { slug: "praxis", definition: "theory joined with scholarly practice in the study of education (D1, 1.2)", beneficiaryDefinition: "putting theory and practice together", scopeNote: "the route to varied professional futures", category: "unknown", practices: ["education"] }
- { slug: "transversal-curriculum", definition: "abilities learned for use in almost any work, crossing fields and industries rather than tied to one subject (D1, 3.3, 3.9)", beneficiaryDefinition: "skills that carry across jobs and settings", scopeNote: "one of three curricular areas with subject-specific and practice-based", category: "unknown", practices: ["education"] }
- { slug: "threshold-standard", definition: "the minimum every student completing an honours or master's course can show in each area of the standards table (D1, 4.3)", beneficiaryDefinition: "the least you need to show for your degree", scopeNote: "typical and excellent describe undergraduate performance above it", category: "unknown", practices: ["education"] }
- { slug: "artificial-intelligence", definition: "technology that produces human-like outputs and responses, including large language models, chatbots and generative AI (D1, 1.41)", beneficiaryDefinition: "tools that answer, write or make things in a human-like way", scopeNote: "the fifth cross-cutting theme", category: "unknown", practices: ["education"] }
- { slug: "monitoring-and-evaluation", definition: "periodic assessment of a course, internal or external, drawing on current and past monitoring to understand achievement and plan ahead (D1, 2.9)", beneficiaryDefinition: "checking how well a course works and improving it", scopeNote: "read with externality (2.10)", category: "unknown", practices: ["education"] }
```

### B2a Terms as the issuer defines them
<!-- label: source; status: drafted; basis: primary -->
```yaml
- { concept: "praxis", form: "praxis", lang: "en", partOfSpeech: "noun", termStatus: "preferred", register: "discipline-specific" }
- { concept: "transversal-curriculum", form: "transversal curricula", lang: "en", partOfSpeech: "noun-phrase", termStatus: "preferred", register: "formal" }
- { concept: "threshold-standard", form: "threshold standards", lang: "en", partOfSpeech: "noun-phrase", termStatus: "preferred", register: "formal" }
- { concept: "artificial-intelligence", form: "Artificial intelligence (AI)", lang: "en", partOfSpeech: "noun-phrase", termStatus: "preferred", register: "formal" }
- { concept: "monitoring-and-evaluation", form: "Monitoring and evaluation", lang: "en", partOfSpeech: "noun-phrase", termStatus: "preferred", register: "formal" }
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
  title: "Subject Benchmark Statement Education Studies"
  edition: "April 2025 (fifth edition)"
  year: 2025
  url: unknown (the QAA page; the text came by stan's extraction)
  retrieved: "held from stan: wkspc2615-QAAVector mapped/education-studies-2025/education-studies-2025.raw.txt, commit 366bcb99a01118f2c4c3ebfa2a8337596bddc455; received 2026-10-03"
  licence: QAA copyright
  tier: primary
  readVia: direct
  held: cc48a3bcc38c112292ced85a22babe5ecd87418e2eddbb449bd03385a311a1c0
  heldFiles: ["wkspc2601-library/txt/qaa-2025-education-studies-subject-benchmark-statement-standard.txt", "wkspc2601-library/txt/qaa-2025-education-studies-subject-benchmark-statement-standard.norm.txt", "wkspc2601-library/records/qaa-2025-education-studies-subject-benchmark-statement-standard.chunks.json", "wkspc2601-library/records/qaa-2025-education-studies-subject-benchmark-statement-standard.held.json"]
  citedIn: [S1, S2, S3, S4, S4a, S5, S6, S7, SB1, SB2, SB3, SB4, SB5, SB6]
```

### D2 Research log
```yaml
- { ref: D1, tier: primary, consulted: 2026-10-03, pass: P1, outcome: "read whole, direct, from the normalised text; skeleton by tools/std_prep.py, document by tools/bm_build.py" }
- { ref: "ADAPT subj HESA stores, cah.json and hecos.json (designs/ingest/standards/subj/vocab)", tier: primary, consulted: 2026-10-03, pass: P1, outcome: "codes for statedSubjects and subjects" }
```

### D3 Wanted sources
```yaml
- { w: "W-std-0056", citation: "QAA (2019) Subject Benchmark Statement: Education Studies", settles: ["S7", "S8"], asked: "2026-10-03", state: "wanted: to confirm supersedes" }
```

## Part E Gaps and questions
- SB4, shape: the standards are one untitled, unnumbered table after 4.5, of twenty rows in three groups (Subject-specific skills: Knowledge and understanding, 10; Practical and practice-based skills, 4; Transversal skills: Transferable competences, 6) across four columns: threshold, typical and excellent for honours, and postgraduate master's. Recorded as 80 S4 records, 4.5.b1 to 4.5.b20 for the threshold cells in reading order, with `.typical`, `.excellent` and `.masters` on the same row; the ids follow batch 1's convention and are ours, not the issuer's.
- SB4, master's column: recorded as `rung: threshold`, award master's, level fheq:7, read with 4.3 (the threshold standards cover honours and master's) and 4.4 (the postgraduate standards, to be used "as a guideline only"). Force recorded as `will` from the cells' "can", not `threshold`, since 4.4 softens it. `.masters` is a new id suffix: for a ruling. No gradeOf: there is no master's rung below it; each master's cell reads as going past the excellent honours cell in the same row (inferred, not recorded).
- SB4, gradeOf: the issuer pairs the cells by row, so each typical cell names the threshold cell and each excellent cell the typical cell, `basis: stated` (40 links).
- S4, force: threshold cells take `threshold` (4.3 defines them as the minimum for all students); typical, excellent and master's cells take `will` from their own "can"; every cell carries forceFrom 4.3. The cells headed "The student consistently demonstrates" (row 11) and "The student shows sophistication" (row 6) have no modal of their own.
- S4, domains: rows 1 to 14 sit under the issuer's Subject-specific and Practical headings and are recorded as knowledge, understanding or subject-skill; rows 15 to 20 (Transversal skills) are generic-skill. Rows 6 (Evaluate own learning skills), 9 (Planning for collaboration) and 14 (Use of digital technologies, including AI) read as generic but follow the issuer's grouping: for P3.
- S4, held text: the typical cell of row 15 reads "theory- relevant perspectives" where the other columns have "relevant perspectives"; row 6 excellent has "reflect" where "reflecting" is meant; row 11's excellent column head is "Excellent" without "standard" on pages 21 and 22. Kept as held.
- S4, 4.6 and 4.7: they reproduce Annex D's professional competence rows (qaa/fheq-2024/annex-d/professional/r1 and r2). 4.7's lead sentence is one record (force will: the accredited award "will not be made"); the two Successful cells are 4.7.b1 and 4.7.b2, threshold, PSRB-accredited routes only, recorded as a fifth SB4 rung entry; the two Not successful cells are failure descriptions, not statements. 4.6 is a row label only.
- S4, outcome paragraphs in sections 1 to 3 taken as statements: 1.6 ("can" and "are able therefore to"), 1.9 and 1.11 ("are able to"), 1.13 ("able to"), 1.31 ("can"), 2.4 and 3.9 ("will"); recorded force `will`. For Abbott: whether "can" in a narrative paragraph counts as an outcome statement.
- S4, force outside the five: 1.15 ("a legal duty", the Equality Act's) is recorded as `describes`; 2.3 ("it would be expected that") is recorded as `describes`; 1.21 ("will need to") as `will`. 4.7 ("requires", "will not be made") as `will`.
- S4, not taken: obliging words outside the five in 1.38 and 1.41 ("there is a need"), 4.4 ("It is important ... as a guideline only") and 2.10's "essential" (2.10 is taken for its "will").
- S4, plain-present provider norms, not statements (template open point 5): 1.1 ("Courses include"), 1.8, 1.12, 1.17, 1.18, 1.19, 1.26, 1.39, 2.1 ("Courses ... commonly", 11 bullets), 2.7, 3.12 ("Courses are designed to", 7 bullets), 3.18, 3.19, 3.20, 3.24, 4.2.
- S4, lists not taken: 1.40 (four aims of the subject, no modal); 1.42 (eleven AI principles under "Programme teams consider", a plain-present lead-in, though 1.43 then says course teams "should also engage with the above principles"; 1.43 is the record, and the skeleton's 1.42 candidates are not); 3.6 ("consider and may incorporate") and 3.8 ("consider"; "typically provide"), permissive; 3.17 ("may include"). 3.10's lead-in obliges ("should consider"), so its 23 bullets are records 3.10.b1 to b23; its stem is not a record.
- S4, permissive or descriptive and not taken: 1.3, 1.14, 2.5, 2.8, 2.11 ("may also require"), 2.12 (describes the external examining system), 3.7, 3.11 ("will vary"), 3.14, 3.22 ("may be required"), 3.23.
- S4, 4.1: "providers clarify the extent to which the benchmark standards should be met" is recorded as a provider statement with force `should`; the clarifying itself is plain present.
- S4, spans: the skeleton's paragraph spans run on into sub-headings and page numbers, and 4.5's runs on through the whole table, 4.7's through the back matter; records use `find` with the paragraph text alone. Page numbers inside a span (2.2, 2.9) stay in `source`.
- S5, crosswalk: 2.5 gives the CertHE at FQHEIS Level 8 and the DipHE at FQHEIS Level 9; the FHEQ document's Table 1 (std:doc:qaa-fheq-2024-framework, S5) gives them at SCQF 7 and SCQF 8. Recorded as stated; the issuer's text looks one level out. For Abbott.
- S5: 4.4 names "Level 7" and "Level 11" without naming the frameworks; read as FHEQ and FQHEIS (inferred). CQFW is not named; Wales appears for course length (2.6) and the quality arrangements (front matter).
- S6, SB6: the AI theme is headed "Artificial intelligence" in section 1 and "generative artificial intelligence" in the front matter; recorded under the one shared id theme:generative-ai (batch 1 convention). The front matter and section 1 both name the EDI theme "Equity", not "Equality".
- S6, SB2: theme:enterprise is carried by no obliging statement in its own paragraphs (1.32 to 1.40 are descriptive); its only statement is 3.10.b13.
- S2, subjects: HECoS 100459 education studies and CAH22-01-01 are named by the statement (its subject); CAH22-01-02 teacher training (front matter: "allied areas including teacher training") and HECoS 101246 professional practice in education (3.3 teaching studies; 3.7 qualified teacher status) are inferred and wait for P3.
- SB5: no PSRB is named; the statement speaks of PSRBs in general. None of their requirements is ingested.
- S7, S8: the previous statement's date is not given in the body; the back matter names advisory groups for 2019 (minor update), 2015, 2007 and 2000, and the cover note says "Fifth Edition Published - 10 April 2025". supersedes points to a 2019 statement not held.
- S4, levels: learner and both statements in sections 1 to 3 are recorded at fheq:6 for the honours degree; they also bear on master's students. Provider duties carry level none, except 4.1 and 4.3, which set the scope of the standards (fheq:6, with master's in award).
- Patterns against Psychology: the standards are one four-column table, not lists; the honours rungs share one lead-in (4.3) and are paired by row; a master's column sits beside the honours columns as a guide; a pass-or-not professional competence row copied from Annex D; cells open "The student can" or "A student can"; a fifth theme (artificial intelligence); most obliging paragraphs in sections 1 to 3 are provider duties (student version not applicable); three curricula (subject-specific, practice-based, transversal) with a figure.
- ST-12: versions here run to the lengths the content needs; no length range is yet set.

---

## Change notes
- 0.1.2, 3 October 2026, 21:02: moved with its held text from UNI to the source library repo (`wkspc2601-library/ingested/standards/`, texts in `txt/`, records in `records/`); paths only (Abbott, 20:56; std N-0119).
- 0.1.1, 3 October 2026, 20:20: obliging words outside the five read as must, "ought to" as should, on statements outside the rungs, each marked on its force line (Abbott, 20:17; D-std-0016).
- 0.1.0, 2026-10-03 17:11: researched by run frame 0.1.1-draft and standards run layer 0.7.0-draft, std, run 0103 (P1); built by tools/bm_build.py.
