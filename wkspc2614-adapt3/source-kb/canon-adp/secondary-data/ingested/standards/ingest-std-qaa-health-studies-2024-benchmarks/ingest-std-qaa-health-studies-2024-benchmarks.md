---
id: std:doc:qaa-health-studies-2024-benchmarks
title: "Subject Benchmark Statement Health Studies"
profile: standards/subject-benchmark
profileVersion: 0.2.0-draft
issuer: QAA
kind: subject-benchmark
jurisdiction: [UK]
subjectScope: subjects
subjects:
  - { scheme: "hecos", code: "100473", label: "health studies", basis: "stated" }
  - { scheme: "cah", code: "CAH15-04-03", label: "health studies", basis: "stated" }
  - { scheme: "cah", code: "CAH15-04", label: "health and social care", basis: "stated" }
  - { scheme: "cah", code: "CAH15", label: "social sciences", basis: "stated" }
  - { scheme: "hecos", code: "100476", label: "health and social care", basis: "inferred" }
edition: "April 2024 (fifth edition)"
published: 2024-04
status: current
supersedes: "Subject Benchmark Statement: Health Studies, fourth edition (2019), as the membership section names it"
heldText: { method: sha256-bytes, raw: 4e1b4d26208497dcf689448bcd3217b7f1a913a1da48e5e92be38fef924f6528, normalised: b70253b2b31e0328e818b33856b15db31e4d31c72ff5232952260e1a748b0903 }
heldTextStan: { method: sha256-stan, raw: 4e1b4d26208497dcf689448bcd3217b7f1a913a1da48e5e92be38fef924f6528, normalised: f1dc78eb8c1d6847c50f6a1b8d417661d0e9586ae177c3637966f29b03a42dd3 }
licence: "QAA copyright; held for study, private to the project, never published"
series: "QAA Subject Benchmark Statements; Health Studies fifth edition (April 2024), in the revision that adds the cross-cutting themes"
awardsCovered: ["bachelor's with honours", "master's"]
levelsCovered: ["fheq:6", "fheq:7", "fqheis:10", "fqheis:11"]
nations: ["England", "Wales", "Scotland", "Northern Ireland"]
parts:
  S: full
  B: "partial: no glossary in the document (it points to QAA's Glossary); terms it defines in passing"
  C: "not-applicable: the document sets expectations, not a procedure"
pins: { structure: 0.13.0-draft, template: 0.8.0-draft, benchmarkTemplate: 0.6.0-draft, runFrame: 0.1.1-draft, runLayer: 0.7.0-draft, standards: none yet, terminology: none yet }
lifecycle: drafted
researchedBy: run frame 0.1.1-draft; standards run layer 0.7.0-draft; std, run 0109 (tools/bm_build.py)
passes:
  P1: "2026-10-03 17:33"
  P2: "skipped: read direct from the held text; inferred codes and rung links are for P3"
  P3: open
version: 0.1.2
---

<!-- from INGEST wpk-0016-ingest-pd-template-standards.md 0.8.0-draft and wpk-0016-ingest-pd-template-standards-benchmark.md 0.6.0-draft; built by tools/bm_build.py from run-src/ -->
# Subject Benchmark Statement: Health Studies (QAA, April 2024)

> Run 0109, P1 by std. The issuer's words are held in the source library, `wkspc2601-library/txt/qaa-2024-health-studies-subject-benchmark-statement-standard.norm.txt`; each S4 record carries its statement in full (`source`) for language analysis, with its span. Paraphrases and versions are ours. Private to the project, never published. In front matter `status` is the issuer's; ours is `lifecycle`. Doubts are in Part E.

## Part 0 Summary

### 0.1 Agent definition
<!-- label: editorial; status: drafted; basis: primary -->
QAA's UK reference point for what a graduate in Health Studies should know, understand and be able to do at the end of an honours degree or a master's degree. Its standards are threshold lists only: subject knowledge and generic skills for honours, subject knowledge for master's and a list of what typical master's holders can do. Reach for it when designing, approving or reviewing a health studies course or writing its outcomes. It is not a curriculum, not a professional body's accreditation standard and not a regulatory requirement in England.

### 0.2 Summary
<!-- label: both; status: drafted; basis: primary -->
Published by QAA in April 2024 as the fifth edition, the statement describes the subject's context and purposes, its distinctive features (design, progression, flexibility, partnership, monitoring and review), its content, teaching, assessment and supervision, then benchmark standards at the threshold for bachelor's degrees with honours (FHEQ level 6, FQHEIS level 10) and master's degrees (FHEQ level 7, FQHEIS level 11). It states no typical or excellent rung for honours and points to Annex D of the Frameworks for achievement above the threshold; the master's generic skills are led in with 'Typically'. It carries the four cross-cutting themes (equality, diversity and inclusion; accessibility; sustainability, with the eight UNESCO competencies; enterprise and entrepreneurship education) and a passage on generative AI, and names PSRBs in general and four health bodies a graduate might join.

## Part S Standard

### S1 Identity
<!-- label: source; status: drafted; basis: primary -->
```yaml
issuer: The Quality Assurance Agency for Higher Education
title: "Subject Benchmark Statement Health Studies"
edition: "April 2024 (fifth edition)"
dates:
  published: 2024-04
  other: []
kind: subject-benchmark
jurisdiction: [UK]
authority: "reference: a sector reference point, not a regulatory requirement (D1, front matter); in England not a sector-recognised standard under the OfS framework; a key reference point in Wales and Scotland; part of quality requirements in Northern Ireland (D1, front matter: Relationship to legislation)"
licence: "QAA copyright; the document gives no re-use terms in its text (D1, front matter)"
copyrightNotice: { text: "© The Quality Assurance Agency for Higher Education 2024", locator: "D1, index" }
```

### S2 Purpose and scope
<!-- label: source; status: drafted; basis: primary -->
```yaml
governs: "what a Health Studies graduate can be expected to know, do and understand at the end of an honours degree or a master's degree, and the nature and characteristics of awards in the subject (D1, front matter: About this Statement; 4.1)"
appliesTo:
  awards: ["bachelor's degrees with honours", "master's degrees", "integrated master's (described, 2.15)", "postgraduate certificates and diplomas (reference point only, 4.6)"]
  levels: ["fheq:6", "fheq:7", "fqheis:10", "fqheis:11"]
  providers: ["UK higher education providers"]
whoMustUse: "none-stated; it is a reference point, not a requirement (D1, front matter)"
howUsed: ["design", "approval", "review", "other: external examining; PSRBs; information for prospective students and employers"]
doesNot: "it is not a national curriculum and does not prescribe teaching, learning or assessment; it carries no statutory or regulatory requirement (D1, front matter)"
beneficiary: the student
statedScope: "\"The term Health Studies throughout this document includes physical and mental health, well-being, and the study of ill health (illness) and disease.\" (D1, 1.2)"
statedSubjects:
  - { name: "Health Studies", locator: "(D1, title; 1.1; 1.2)", kind: "subject", codes: [{ scheme: "hecos", code: "100473", label: "health studies" }, { scheme: "cah", code: "CAH15-04-03", label: "health studies" }] }
  - { name: "multidisciplinary or joint courses of study, such as Health Studies with exercise or physical activity", locator: "(D1, 1.8)", kind: "programme title", codes: [{ scheme: "hecos", code: "100473", label: "health studies" }] }
  - { name: "combined or joint degree", locator: "(D1, 2.13)", kind: "programme title", codes: [{ scheme: "hecos", code: "100473", label: "health studies" }] }
  - { name: "Integrated master's degrees", locator: "(D1, 2.15)", kind: "programme title", codes: [{ scheme: "hecos", code: "100473", label: "health studies" }] }
  - { name: "Apprenticeship degrees", locator: "(D1, 2.22)", kind: "programme title", codes: [{ scheme: "hecos", code: "100473", label: "health studies" }] }
subjects: see front matter (subjectScope subjects)
```

### S3 Structure
<!-- label: both; status: drafted; basis: primary -->
```yaml
components:
  - { number: "1.1", order: 3, componentType: paragraph, parent: "section 1", heading: "Context and purposes of a Health Studies degree", gloss: "the subject spans daily life across the life-course and many communities" }
  - { number: "1.2", order: 4, componentType: paragraph, parent: "section 1", heading: "Context and purposes of a Health Studies degree", gloss: "a broad field: physical and mental health, illness, care; wide employment" }
  - { number: "1.3", order: 5, componentType: paragraph, parent: "section 1", heading: "Context and purposes of a Health Studies degree", gloss: "it draws on many disciplines and keeps growing" }
  - { number: "1.4", order: 6, componentType: paragraph, parent: "section 1", heading: "Context and purposes of a Health Studies degree", gloss: "what shapes health, from policy to personal experience" }
  - { number: "1.5", order: 7, componentType: paragraph, parent: "section 1", heading: "Context and purposes of a Health Studies degree", gloss: "aim: critical study of health, its education and promotion; integrated care" }
  - { number: "1.6", order: 8, componentType: paragraph, parent: "section 1", heading: "Context and purposes of a Health Studies degree", gloss: "local to global contexts; research across disciplines; independent learners" }
  - { number: "1.7", order: 9, componentType: paragraph, parent: "section 1", heading: "Context and purposes of a Health Studies degree", gloss: "many titles and pathways; content from conceptual to vocational" }
  - { number: "1.8", order: 10, componentType: paragraph, parent: "section 1", heading: "Context and purposes of a Health Studies degree", gloss: "use beside other statements for joint courses; contrasting views" }
  - { number: "1.9", order: 11, componentType: paragraph, parent: "section 1", heading: "Purposes and characteristics of a Health Studies degree", gloss: "meanings of health; no agreed definition; not the study of illness" }
  - { number: "1.10", order: 12, componentType: area, parent: "section 1", heading: "Purposes and characteristics of a Health Studies degree", gloss: "common themes: health as human experience; reflective, critical evaluation" }
  - { number: "1.11", order: 13, componentType: stem, parent: "section 1", heading: "Purposes and characteristics of a Health Studies degree", gloss: "aim: students as agents of change" }
  - { number: "1.12", order: 14, componentType: paragraph, parent: "section 1", heading: "Purposes and characteristics of a Health Studies degree", gloss: "research-based courses; critical reflection; research ethics" }
  - { number: "1.13", order: 15, componentType: paragraph, parent: "section 1", heading: "Purposes and characteristics of a Health Studies degree", gloss: "stakeholders in course work; employability skills" }
  - { number: "1.14", order: 16, componentType: paragraph, parent: "section 1", heading: "Purposes and characteristics of a Health Studies degree", gloss: "choosing a mix of disciplines; experience of care sectors" }
  - { number: "1.15", order: 17, componentType: paragraph, parent: "section 1", heading: "Purposes and characteristics of a Health Studies degree", gloss: "courses with a professional focus; working with professions and users" }
  - { number: "1.16", order: 18, componentType: area, parent: "section 1", heading: "Purposes and characteristics of a Health Studies degree", gloss: "the disciplines and subject areas it draws on" }
  - { number: "1.17", order: 19, componentType: paragraph, parent: "section 1", heading: "Equality, diversity and inclusion", gloss: "EDI: identity characteristics and intersectionality, embedded in the subject" }
  - { number: "1.18", order: 20, componentType: paragraph, parent: "section 1", heading: "Equality, diversity and inclusion", gloss: "an inclusive learning community; a proactive approach to EDI" }
  - { number: "1.19", order: 21, componentType: paragraph, parent: "section 1", heading: "Equality, diversity and inclusion", gloss: "why it is taught: EDI, inequality and the SDGs" }
  - { number: "1.20", order: 22, componentType: paragraph, parent: "section 1", heading: "Equality, diversity and inclusion", gloss: "what is taught: organisations and EDI; the legal duty; diverse content" }
  - { number: "1.21", order: 23, componentType: paragraph, parent: "section 1", heading: "Equality, diversity and inclusion", gloss: "how it is taught: inclusive design and modes of study" }
  - { number: "1.22", order: 24, componentType: stem, parent: "section 1", heading: "Equality, diversity and inclusion", gloss: "examples of EDI in practice" }
  - { number: "1.23", order: 25, componentType: paragraph, parent: "section 1", heading: "Equality, diversity and inclusion", gloss: "EDI as continuing review with students" }
  - { number: "1.24", order: 26, componentType: stem, parent: "section 1", heading: "Accessibility", gloss: "accessibility of every course requirement and what it may cover" }
  - { number: "1.25", order: 27, componentType: paragraph, parent: "section 1", heading: "Accessibility", gloss: "designing out barriers in advance" }
  - { number: "1.26", order: 28, componentType: paragraph, parent: "section 1", heading: "Accessibility", gloss: "equal access to workplace and international learning; digital access" }
  - { number: "1.27", order: 29, componentType: paragraph, parent: "section 1", heading: "Sustainability", gloss: "sustainability and planetary health; ESD defined; the SDGs" }
  - { number: "1.28", order: 30, componentType: paragraph, parent: "section 1", heading: "Sustainability", gloss: "ESD and the link between health, equality and environment" }
  - { number: "1.29", order: 31, componentType: paragraph, parent: "section 1", heading: "Sustainability", gloss: "weighing sustainability values; graduates as agents of change" }
  - { number: "1.30", order: 32, componentType: paragraph, parent: "section 1", heading: "Sustainability", gloss: "the person in context; critique of professional systems" }
  - { number: "1.31", order: 33, componentType: stem, parent: "section 1", heading: "Developing sustainable development competencies", gloss: "the eight UNESCO sustainability competencies" }
  - { number: "1.32", order: 34, componentType: paragraph, parent: "section 1", heading: "Developing sustainable development competencies", gloss: "competencies built into curricula" }
  - { number: "1.33", order: 35, componentType: paragraph, parent: "section 1", heading: "Developing learning environments to promote sustainable development", gloss: "facilities for self-directed adult learners" }
  - { number: "1.34", order: 36, componentType: practice, parent: "section 1", heading: "Developing learning environments to promote sustainable development", gloss: "teaching methods for ESD; authentic, interdisciplinary learning" }
  - { number: "1.35", order: 37, componentType: paragraph, parent: "section 1", heading: "Enterprise and entrepreneurship education", gloss: "EEE and careers; placements and employer links" }
  - { number: "1.36", order: 38, componentType: paragraph, parent: "section 1", heading: "Enterprise and entrepreneurship education", gloss: "EEE beyond employment" }
  - { number: "1.37", order: 39, componentType: paragraph, parent: "section 1", heading: "Enterprise and entrepreneurship education", gloss: "knowing and showing the worth of one's skills" }
  - { number: "1.38", order: 40, componentType: stem, parent: "section 1", heading: "Enterprise and entrepreneurship education", gloss: "what an entrepreneurial mindset in health means" }
  - { number: "1.39", order: 41, componentType: paragraph, parent: "section 1", heading: "Enterprise and entrepreneurship education", gloss: "EEE for an ethical career, employed or self-employed" }
  - { number: "1.40", order: 42, componentType: paragraph, parent: "section 1", heading: "Enterprise and entrepreneurship education", gloss: "enterprising behaviours" }
  - { number: "1.41", order: 43, componentType: paragraph, parent: "section 1", heading: "Enterprise and entrepreneurship education", gloss: "enterprising attributes" }
  - { number: "1.42", order: 44, componentType: paragraph, parent: "section 1", heading: "Enterprise and entrepreneurship education", gloss: "competencies for employed or self-employed practice" }
  - { number: "1.43", order: 45, componentType: paragraph, parent: "section 1", heading: "Enterprise and entrepreneurship education", gloss: "ethical digital competence" }
  - { number: "1.44", order: 46, componentType: paragraph, parent: "section 1", heading: "Enterprise and entrepreneurship education", gloss: "professional skills across the curriculum; dedicated modules" }
  - { number: "1.45", order: 47, componentType: paragraph, parent: "section 1", heading: "Enterprise and entrepreneurship education", gloss: "external speakers and practitioners" }
  - { number: "1.46", order: 48, componentType: paragraph, parent: "section 1", heading: "Enterprise and entrepreneurship education", gloss: "assignments that build business skills" }
  - { number: "1.47", order: 49, componentType: paragraph, parent: "section 1", heading: "Enterprise and entrepreneurship education", gloss: "work with placement providers and employers" }
  - { number: "1.48", order: 50, componentType: paragraph, parent: "section 1", heading: "Enterprise and entrepreneurship education", gloss: "placements as a bridge to an enterprising mindset" }
  - { number: "1.49", order: 51, componentType: paragraph, parent: "section 1", heading: "Enterprise and entrepreneurship education", gloss: "career pathways and confidence" }
  - { number: "2.1", order: 53, componentType: paragraph, parent: "section 2", heading: "Design", gloss: "multidisciplinary course design; other statements may apply" }
  - { number: "2.2", order: 54, componentType: paragraph, parent: "section 2", heading: "Design", gloss: "focus varies; place health in context; partnerships in design" }
  - { number: "2.3", order: 55, componentType: paragraph, parent: "section 2", heading: "Design", gloss: "design resting on frameworks and standards" }
  - { number: "2.4", order: 56, componentType: stem, parent: "section 2", heading: "Design", gloss: "EDI throughout the experience; further considerations" }
  - { number: "2.5", order: 57, componentType: paragraph, parent: "section 2", heading: "Design", gloss: "diverse patients' needs; decolonising the curriculum" }
  - { number: "2.6", order: 58, componentType: stem, parent: "section 2", heading: "Design", gloss: "plural ways of knowing, cultural safety, global health" }
  - { number: "2.7", order: 59, componentType: paragraph, parent: "section 2", heading: "Design", gloss: "ESD in curriculum design" }
  - { number: "2.8", order: 60, componentType: paragraph, parent: "section 2", heading: "Design", gloss: "employability and enterprise in design; placements" }
  - { number: "2.9", order: 61, componentType: paragraph, parent: "section 2", heading: "Design", gloss: "registers and professional bodies graduates may join" }
  - { number: "2.10", order: 62, componentType: paragraph, parent: "section 2", heading: "Progression", gloss: "progression through the honours levels" }
  - { number: "2.11", order: 63, componentType: stem, parent: "section 2", heading: "Progression", gloss: "from structured study to autonomy; progression strategies" }
  - { number: "2.12", order: 64, componentType: paragraph, parent: "section 2", heading: "Progression", gloss: "readiness for postgraduate study" }
  - { number: "2.13", order: 65, componentType: paragraph, parent: "section 2", heading: "Progression", gloss: "joint and combined degrees" }
  - { number: "2.14", order: 66, componentType: paragraph, parent: "section 2", heading: "Progression", gloss: "length of study, early exits and part-time routes" }
  - { number: "2.15", order: 67, componentType: paragraph, parent: "section 2", heading: "Progression", gloss: "integrated master's degrees" }
  - { number: "2.16", order: 68, componentType: paragraph, parent: "section 2", heading: "Flexibility", gloss: "flexible learning and delivery" }
  - { number: "2.17", order: 69, componentType: stem, parent: "section 2", heading: "Flexibility", gloss: "flexible formats, modes and entry points" }
  - { number: "2.18", order: 70, componentType: paragraph, parent: "section 2", heading: "Flexibility", gloss: "flexible design and review" }
  - { number: "2.19", order: 71, componentType: stem, parent: "section 2", heading: "Partnership", gloss: "stakeholders as partners and what partnership brings" }
  - { number: "2.20", order: 72, componentType: paragraph, parent: "section 2", heading: "Partnership", gloss: "aims for stakeholder involvement; regulatory alignment" }
  - { number: "2.21", order: 73, componentType: paragraph, parent: "section 2", heading: "Partnership", gloss: "employer engagement and work-related learning" }
  - { number: "2.22", order: 74, componentType: paragraph, parent: "section 2", heading: "Partnership", gloss: "apprenticeship degrees" }
  - { number: "2.23", order: 75, componentType: paragraph, parent: "section 2", heading: "Monitoring and review", gloss: "routine monitoring and periodic review" }
  - { number: "2.24", order: 76, componentType: paragraph, parent: "section 2", heading: "Monitoring and review", gloss: "external reviewers and threshold standards" }
  - { number: "2.25", order: 77, componentType: paragraph, parent: "section 2", heading: "Monitoring and review", gloss: "external examiners" }
  - { number: "2.26", order: 78, componentType: paragraph, parent: "section 2", heading: "Monitoring and review", gloss: "PSRB accreditation" }
  - { number: "2.27", order: 79, componentType: stem, parent: "section 2", heading: "Monitoring and review", gloss: "external reference points; uses of monitoring" }
  - { number: "2.28", order: 80, componentType: stem, parent: "section 2", heading: "Monitoring and review", gloss: "what monitoring and review support" }
  - { number: "2.29", order: 81, componentType: paragraph, parent: "section 2", heading: "Monitoring and review", gloss: "stakeholders in quality monitoring" }
  - { number: "2.30", order: 82, componentType: paragraph, parent: "section 2", heading: "Monitoring and review", gloss: "advisory boards and employer panels" }
  - { number: "3.1", order: 84, componentType: area, parent: "section 3", heading: "Content", gloss: "content and delivery for reflective, critical study" }
  - { number: "3.2", order: 85, componentType: area, parent: "section 3", heading: "Content", gloss: "flexible settings; specialising in a broad field" }
  - { number: "3.3", order: 86, componentType: practice, parent: "section 3", heading: "Teaching and learning", gloss: "blended, inclusive teaching strategies" }
  - { number: "3.4", order: 87, componentType: paragraph, parent: "section 3", heading: "Teaching and learning", gloss: "critical evaluation to build problem-solving and creativity" }
  - { number: "3.5", order: 88, componentType: practice, parent: "section 3", heading: "Teaching and learning", gloss: "scheduled activities and learning approaches" }
  - { number: "3.6", order: 89, componentType: paragraph, parent: "section 3", heading: "Teaching and learning", gloss: "the list does not prescribe" }
  - { number: "3.7", order: 90, componentType: practice, parent: "section 3", heading: "Assessment", gloss: "assessment strategy, adjustments and generative AI" }
  - { number: "3.8", order: 91, componentType: practice, parent: "section 3", heading: "Assessment", gloss: "assessment methods" }
  - { number: "3.9", order: 92, componentType: practice, parent: "section 3", heading: "Assessment", gloss: "feedback: qualities, timing, feed-in and feed-forward" }
  - { number: "3.10", order: 93, componentType: practice, parent: "section 3", heading: "Assessment", gloss: "what feedback should do" }
  - { number: "3.11", order: 94, componentType: practice, parent: "section 3", heading: "Supervision", gloss: "the role of supervision" }
  - { number: "3.12", order: 95, componentType: practice, parent: "section 3", heading: "Supervision", gloss: "what supervision needs" }
  - { number: "4.1", order: 97, componentType: paragraph, parent: "section 4", heading: "Introduction", gloss: "the standards are minimum thresholds for honours and master's" }
  - { number: "4.2", order: 98, componentType: paragraph, parent: "section 4", heading: "Introduction", gloss: "most go beyond the threshold; Annex D for classes" }
  - { number: "4.3", order: 99, componentType: paragraph, parent: "section 4", heading: "Introduction", gloss: "levels 6 and 7 thresholds as the minimum for an award" }
  - { number: "4.4", order: 100, componentType: stem, parent: "section 4", heading: "Threshold level: Subject knowledge, understanding and skills", gloss: "threshold subject knowledge, understanding and skills (honours)" }
  - { number: "4.5", order: 101, componentType: stem, parent: "section 4", heading: "Threshold level: Generic skills", gloss: "threshold generic skills (honours)" }
  - { number: "4.6", order: 102, componentType: paragraph, parent: "section 4", heading: "Benchmark standards for master's degrees", gloss: "master's standards as a level 7 reference point" }
  - { number: "4.7", order: 103, componentType: stem, parent: "section 4", heading: "Benchmark standards for master's degrees: Subject knowledge, understanding and skills", gloss: "master's subject knowledge" }
  - { number: "4.8", order: 104, componentType: stem, parent: "section 4", heading: "Benchmark standards for master's degrees: Generic skills", gloss: "master's generic skills of typical holders" }
  - { number: "1", componentType: section, parent: none, heading: "Context and purposes of a Health Studies degree", gloss: "section 1" }
  - { number: "2", componentType: section, parent: none, heading: "Distinctive features of the Health Studies degree", gloss: "section 2" }
  - { number: "3", componentType: section, parent: none, heading: "Content, structure and delivery", gloss: "section 3" }
  - { number: "4", componentType: section, parent: none, heading: "Benchmark standards", gloss: "section 4" }
excluded:
  - { number: "none", heading: "About this Statement; How can I use this document?; Relationship to legislation; Additional sector reference points", kind: "other: front matter, read for S1, S2 and S7" }
  - { number: "section headings 1 to 4", heading: "section heading lines", kind: "other: not document substance" }
  - { number: "5", heading: "List of references and further resources", kind: "other: bibliography, read for S7 and D3" }
  - { number: "6", heading: "Membership of the Advisory Group", kind: "other: names, read for supersedes and S8 only" }
```

### S4 Statements
<!-- label: both; status: drafted; basis: primary. Only standards (D-std-0002 (a)): 124 records. `source` is the issuer's statement exactly as its span holds it (D-std-0014). -->
```yaml
- id: qaa/health-studies-2024/1.13
  locator: { number: "1.13", headingPath: ["Context and purposes of a Health Studies degree", "Purposes and characteristics of a Health Studies degree"] }
  span: { start: 14116, end: 14354 }
  source: "It is envisaged that in the process of planning, development, delivery and evaluation of courses, relevant stakeholders such as students, patients and the public, agencies and individuals, voluntary services and employers will be engaged."
  stem: none
  statementType: expectation
  rung: none
  force: will
  level: none
  appliesTo: "Health Studies courses and the teams who run them"
  addressee: provider
  verbs: ["envisaged", "engaged"]
  about: "stakeholders in course work"
  themes: [none]
  domain: none
  award: ["bachelor's with honours", "master's"]
  gradeOf: none
  paraphrase: "Students, patients, the public, community agencies, voluntary services and employers will take part in planning, building, running and evaluating courses."
  quote: full   # the issuer's statement is in `source` (D-std-0014)
  audience: practitioner
  subjects: inherited
- id: qaa/health-studies-2024/1.21
  locator: { number: "1.21", headingPath: ["Context and purposes of a Health Studies degree", "Equality, diversity and inclusion"] }
  span: { start: 19222, end: 19485 }
  source: "Courses in Health Studies should be designed to enable students to realise their potential, and feel represented and included, regardless of their race/ethnicity, religion, gender identity, sexual orientation, disability or social background (s ee paragraph 2.4)."
  stem: none
  statementType: requirement
  rung: none
  force: should
  level: none
  appliesTo: "Health Studies courses and the teams who run them"
  addressee: provider
  verbs: ["designed", "enable", "realise", "feel"]
  about: "inclusive course design"
  themes: [theme:edi]
  domain: none
  award: ["bachelor's with honours", "master's"]
  gradeOf: none
  paraphrase: "Courses should be built so that every student can reach their potential and feel represented and included, whatever their background, faith, ethnicity, disability, gender identity or sexuality."
  quote: full   # the issuer's statement is in `source` (D-std-0014)
  audience: practitioner
  subjects: inherited
- id: qaa/health-studies-2024/1.23
  locator: { number: "1.23", headingPath: ["Context and purposes of a Health Studies degree", "Equality, diversity and inclusion"] }
  span: { start: 21503, end: 21691 }
  source: "Course teams must regularly reflect upon how EDI can be further enhanced and, where possible, work in partnership with students in doing so (see paragraph 2.2 - relating to course design)."
  stem: none
  statementType: requirement
  rung: none
  force: must
  level: none
  appliesTo: "Health Studies courses and the teams who run them"
  addressee: provider
  verbs: ["reflect", "work"]
  about: "regular review of EDI with students"
  themes: [theme:edi]
  domain: none
  award: ["bachelor's with honours", "master's"]
  gradeOf: none
  paraphrase: "Course teams must keep reviewing how to strengthen equality, diversity and inclusion and, where they can, do it in partnership with students."
  quote: full   # the issuer's statement is in `source` (D-std-0014)
  audience: practitioner
  subjects: inherited
- id: qaa/health-studies-2024/1.24
  locator: { number: "1.24", headingPath: ["Context and purposes of a Health Studies degree", "Accessibility"] }
  span: { start: 22089, end: 22320 }
  source: "Accessibility should, as a minimum, meet regulatory requirements and will apply to all stages of the course, from providing pre-application information through to graduation and beyond (see paragraph 2.4 relating to course design)."
  stem: none
  statementType: requirement
  rung: none
  force: should
  level: none
  appliesTo: "Health Studies courses and the teams who run them"
  addressee: provider
  verbs: ["meet", "apply"]
  about: "accessibility at every stage"
  themes: [theme:accessibility]
  domain: none
  award: ["bachelor's with honours", "master's"]
  gradeOf: none
  paraphrase: "Accessibility should at least satisfy regulatory requirements and will cover every stage of the course, from information before application to graduation and after."
  quote: full   # the issuer's statement is in `source` (D-std-0014)
  audience: practitioner
  subjects: inherited
- id: qaa/health-studies-2024/1.27
  locator: { number: "1.27", headingPath: ["Context and purposes of a Health Studies degree", "Sustainability"] }
  span: { start: 23911, end: 24105 }
  source: "An understanding of the United Nation’s Sustainable Development Goals (SDGs) is essential to this vision and, where appropriate, the SDGs should be integrated holistically across the curriculum."
  stem: none
  statementType: requirement
  rung: none
  force: should
  level: none
  appliesTo: "Health Studies courses and the teams who run them"
  addressee: provider
  verbs: ["integrated"]
  about: "the SDGs across the curriculum"
  themes: [theme:esd]
  domain: none
  award: ["bachelor's with honours", "master's"]
  gradeOf: none
  paraphrase: "Understanding the UN Sustainable Development Goals is central to this vision, and where it fits the goals should run through the whole curriculum."
  quote: full   # the issuer's statement is in `source` (D-std-0014)
  audience: practitioner
  subjects: inherited
- id: qaa/health-studies-2024/1.31.b1
  locator: { number: "1.31.b1", headingPath: ["Context and purposes of a Health Studies degree", "Developing sustainable development competencies"] }
  span: { start: 26652, end: 26902 }
  source: "Systems thinking - Health Studies students can recognise and understand relationships within various levels and units in health, analyse complex systems, consider how systems are embedded within different domains and scales, and deal with uncertainty"
  stem: "1.31"
  statementType: outcome
  rung: none
  force: will
  level: fheq:6
  appliesTo: "students and graduates of the subject"
  addressee: learner
  verbs: ["recognise", "understand", "analyse", "consider", "deal"]
  about: "systems thinking"
  themes: [theme:esd]
  domain: generic-skill
  award: ["bachelor's with honours"]
  gradeOf: none
  paraphrase: "Students of the subject can see how levels and units in health relate, analyse complex systems across domains and scales and cope with uncertainty."
  quote: full   # the issuer's statement is in `source` (D-std-0014)
  audience: both
  subjects: inherited
- id: qaa/health-studies-2024/1.31.b2
  locator: { number: "1.31.b2", headingPath: ["Context and purposes of a Health Studies degree", "Developing sustainable development competencies"] }
  span: { start: 26905, end: 27153 }
  source: "Anticipatory or future thinking - Health Studies students can understand and evaluate multiple outcomes, create their own visions for the future, apply the precautionary principle, assess the consequences of actions, and deal with risks and changes"
  stem: "1.31"
  statementType: outcome
  rung: none
  force: will
  level: fheq:6
  appliesTo: "students and graduates of the subject"
  addressee: learner
  verbs: ["understand", "evaluate", "create", "apply", "assess", "deal"]
  about: "anticipatory thinking"
  themes: [theme:esd]
  domain: generic-skill
  award: ["bachelor's with honours"]
  gradeOf: none
  paraphrase: "Students of the subject can weigh possible futures, form their own visions of what is to come, use the precautionary principle, judge the effects of actions and handle risk and change."
  quote: full   # the issuer's statement is in `source` (D-std-0014)
  audience: both
  subjects: inherited
- id: qaa/health-studies-2024/1.31.b3
  locator: { number: "1.31.b3", headingPath: ["Context and purposes of a Health Studies degree", "Developing sustainable development competencies"] }
  span: { start: 27156, end: 27467 }
  source: "Normative thinking - Health Studies students can understand and reflect on the norms and values that underlie one’s actions; negotiate sustainable development values and principles; and set goals and targets, in a context of conflicts of interests, uncertain knowledge and contradictions within the health arena"
  stem: "1.31"
  statementType: outcome
  rung: none
  force: will
  level: fheq:6
  appliesTo: "students and graduates of the subject"
  addressee: learner
  verbs: ["understand", "reflect", "negotiate", "set"]
  about: "normative thinking"
  themes: [theme:esd]
  domain: generic-skill
  award: ["bachelor's with honours"]
  gradeOf: none
  paraphrase: "Students of the subject can reflect on the norms and values behind actions, work through the values of sustainable development with others and set goals where interests clash and knowledge is uncertain in health."
  quote: full   # the issuer's statement is in `source` (D-std-0014)
  audience: both
  subjects: inherited
- id: qaa/health-studies-2024/1.31.b4
  locator: { number: "1.31.b4", headingPath: ["Context and purposes of a Health Studies degree", "Developing sustainable development competencies"] }
  span: { start: 27470, end: 27647 }
  source: "Strategic thinking - Health Studies students are able to develop and implement innovative actions that further sustainable development both at the local level and further afield"
  stem: "1.31"
  statementType: outcome
  rung: none
  force: will
  level: fheq:6
  appliesTo: "students and graduates of the subject"
  addressee: learner
  verbs: ["develop", "implement", "further"]
  about: "strategic thinking"
  themes: [theme:esd]
  domain: generic-skill
  award: ["bachelor's with honours"]
  gradeOf: none
  paraphrase: "Students of the subject can devise and carry out new actions that advance sustainable development locally and beyond."
  quote: full   # the issuer's statement is in `source` (D-std-0014)
  audience: both
  subjects: inherited
- id: qaa/health-studies-2024/1.31.b5
  locator: { number: "1.31.b5", headingPath: ["Context and purposes of a Health Studies degree", "Developing sustainable development competencies"] }
  span: { start: 27650, end: 27987 }
  source: "Collaborative practice - Health Studies students can work together and learn from others, including peers and others inside and outside of their institution, understand\n\n9\nand respect the needs, perspectives and actions of others in the field, deal with conflicts in a group and facilitate collaborative and participatory problem-solving"
  stem: "1.31"
  statementType: outcome
  rung: none
  force: will
  level: fheq:6
  appliesTo: "students and graduates of the subject"
  addressee: learner
  verbs: ["work", "learn", "understand", "respect", "deal", "facilitate"]
  about: "collaborative practice"
  themes: [theme:esd]
  domain: generic-skill
  award: ["bachelor's with honours"]
  gradeOf: none
  paraphrase: "Students of the subject can work and learn with people inside and outside their institution, respect others' needs and views, handle conflict in groups and support shared problem-solving."
  quote: full   # the issuer's statement is in `source` (D-std-0014)
  audience: both
  subjects: inherited
- id: qaa/health-studies-2024/1.31.b6
  locator: { number: "1.31.b6", headingPath: ["Context and purposes of a Health Studies degree", "Developing sustainable development competencies"] }
  span: { start: 27990, end: 28200 }
  source: "Critical thinking - Health Studies students are able to question norms, practices and opinions, reflect on their own values, perceptions and actions, and take a position in the sustainable development discourse"
  stem: "1.31"
  statementType: outcome
  rung: none
  force: will
  level: fheq:6
  appliesTo: "students and graduates of the subject"
  addressee: learner
  verbs: ["question", "reflect", "take"]
  about: "critical thinking for sustainability"
  themes: [theme:esd]
  domain: generic-skill
  award: ["bachelor's with honours"]
  gradeOf: none
  paraphrase: "Students of the subject can question accepted norms, practices and opinions, examine their own values and actions and take a stance in the debate on sustainable development."
  quote: full   # the issuer's statement is in `source` (D-std-0014)
  audience: both
  subjects: inherited
- id: qaa/health-studies-2024/1.31.b7
  locator: { number: "1.31.b7", headingPath: ["Context and purposes of a Health Studies degree", "Developing sustainable development competencies"] }
  span: { start: 28203, end: 28475 }
  source: "Self-awareness - Health Studies students are able to reflect on their own values, perceptions and actions, consider their own role in the local community and global society, continually evaluate and further motivate their actions, and reflect on their feelings and desires"
  stem: "1.31"
  statementType: outcome
  rung: none
  force: will
  level: fheq:6
  appliesTo: "students and graduates of the subject"
  addressee: learner
  verbs: ["reflect", "consider", "evaluate", "motivate"]
  about: "self-awareness"
  themes: [theme:esd]
  domain: generic-skill
  award: ["bachelor's with honours"]
  gradeOf: none
  paraphrase: "Students of the subject can reflect on their own values, perceptions, actions, feelings and desires, consider their part in local and global society and keep judging and driving their own actions."
  quote: full   # the issuer's statement is in `source` (D-std-0014)
  audience: both
  subjects: inherited
- id: qaa/health-studies-2024/1.31.b8
  locator: { number: "1.31.b8", headingPath: ["Context and purposes of a Health Studies degree", "Developing sustainable development competencies"] }
  span: { start: 28478, end: 28765 }
  source: "Integrated problem-solving - Health Studies students can apply different problem- solving frameworks to complex sustainable development problems within the field of Health Studies, develop viable, inclusive and equitable solutions, and utilise appropriate competencies to solve problems."
  stem: "1.31"
  statementType: outcome
  rung: none
  force: will
  level: fheq:6
  appliesTo: "students and graduates of the subject"
  addressee: learner
  verbs: ["apply", "develop", "utilise", "solve"]
  about: "integrated problem-solving"
  themes: [theme:esd]
  domain: generic-skill
  award: ["bachelor's with honours"]
  gradeOf: none
  paraphrase: "Students of the subject can use several problem-solving frameworks on complex sustainability problems in health, devise workable, inclusive and fair solutions and draw on the right competences to resolve them."
  quote: full   # the issuer's statement is in `source` (D-std-0014)
  audience: both
  subjects: inherited
- id: qaa/health-studies-2024/1.32
  locator: { number: "1.32", headingPath: ["Context and purposes of a Health Studies degree", "Developing sustainable development competencies"] }
  span: { start: 28771, end: 28931 }
  source: "The learning environment for Health Studies therefore requires these competencies to be integral and exemplified within course curricula and learning resources."
  stem: none
  statementType: requirement
  rung: none
  force: must
  level: none
  appliesTo: "Health Studies courses and the teams who run them"
  addressee: provider
  verbs: ["requires"]
  about: "sustainability competencies in curricula"
  themes: [theme:esd]
  domain: none
  award: ["bachelor's with honours", "master's"]
  gradeOf: none
  paraphrase: "The subject's learning environment needs the sustainability competencies built into, and visible in, its curricula and learning resources."
  quote: full   # the issuer's statement is in `source` (D-std-0014)
  audience: practitioner
  subjects: inherited
- id: qaa/health-studies-2024/1.33
  locator: { number: "1.33", headingPath: ["Context and purposes of a Health Studies degree", "Developing learning environments to promote sustainable development"] }
  span: { start: 29005, end: 29130 }
  source: "Health Studies requires facilities that support learning and experiential training for adults who are self-directed learners."
  stem: none
  statementType: requirement
  rung: none
  force: must
  level: none
  appliesTo: "Health Studies courses and the teams who run them"
  addressee: provider
  verbs: ["requires", "support"]
  about: "facilities for self-directed adult learners"
  themes: [theme:esd]
  domain: none
  award: ["bachelor's with honours", "master's"]
  gradeOf: none
  paraphrase: "The subject needs facilities that support study and experiential training for adults who direct their own learning."
  quote: full   # the issuer's statement is in `source` (D-std-0014)
  audience: practitioner
  subjects: inherited
- id: qaa/health-studies-2024/1.37
  locator: { number: "1.37", headingPath: ["Context and purposes of a Health Studies degree", "Enterprise and entrepreneurship education"] }
  span: { start: 31576, end: 32054 }
  source: "Health Studies students should understand the commercial as well as practical value of their skillsets and be able to articulate and demonstrate them to potential employers and in plans for self-employment or private practice. They should also be encouraged to develop self-awareness of their own enterprising and entrepreneurial capabilities in the health sector, as well as the motivation and self-discipline to apply these flexibly in different ways and in changing contexts."
  stem: none
  statementType: expectation
  rung: none
  force: should
  level: fheq:6
  appliesTo: "students of the subject"
  addressee: learner
  verbs: ["understand", "articulate", "demonstrate", "encouraged", "develop", "apply"]
  about: "knowing and showing the worth of one's skills"
  themes: [theme:enterprise]
  domain: generic-skill
  award: ["bachelor's with honours"]
  gradeOf: none
  paraphrase: "Students should grasp the commercial and practical worth of their skills, be able to explain and show them to employers or in plans to work for themselves; they should also be encouraged to know their own enterprising strengths in health and use them flexibly."
  quote: full   # the issuer's statement is in `source` (D-std-0014)
  audience: both
  subjects: inherited
- id: qaa/health-studies-2024/1.43
  locator: { number: "1.43", headingPath: ["Context and purposes of a Health Studies degree", "Enterprise and entrepreneurship education"] }
  span: { start: 34745, end: 35005 }
  source: "Developing digital competency and transferable skills in Health Studies should include using digital technology ethically to communicate ideas creatively, innovatively and accessibly, in order to enhance academic success in the field, as well as employability."
  stem: none
  statementType: expectation
  rung: none
  force: should
  level: fheq:6
  appliesTo: "the curriculum and students of the subject"
  addressee: both
  verbs: ["include", "using", "communicate", "enhance"]
  about: "ethical digital communication"
  themes: [theme:enterprise]
  domain: generic-skill
  award: ["bachelor's with honours", "master's"]
  gradeOf: none
  paraphrase: "Building digital competence and transferable skills should involve using digital technology ethically to share ideas in creative, original and accessible ways, for academic success and for employability."
  quote: full   # the issuer's statement is in `source` (D-std-0014)
  audience: both
  subjects: inherited
- id: qaa/health-studies-2024/2.1
  locator: { number: "2.1", headingPath: ["Distinctive features of the Health Studies degree", "Design"] }
  span: { start: 37364, end: 37606 }
  source: "Given that Health Studies courses cover a broad subject area (see paragraph 1.16 for the academic disciplines and subject areas that Health Studies draws on), due consideration should be given to the nature of multidisciplinary course design."
  stem: none
  statementType: requirement
  rung: none
  force: should
  level: none
  appliesTo: "Health Studies courses and the teams who run them"
  addressee: provider
  verbs: ["given"]
  about: "multidisciplinary course design"
  themes: [none]
  domain: none
  award: ["bachelor's with honours", "master's"]
  gradeOf: none
  paraphrase: "Because the subject is broad, course design should give proper thought to how several disciplines are combined."
  quote: full   # the issuer's statement is in `source` (D-std-0014)
  audience: practitioner
  subjects: inherited
- id: qaa/health-studies-2024/2.3
  locator: { number: "2.3", headingPath: ["Distinctive features of the Health Studies degree", "Design"] }
  span: { start: 38919, end: 39172 }
  source: "The design of Health Studies courses will be underpinned by national qualifications frameworks and sector recognised standards to communicate the achievements and attributes represented by Health Studies awards to various stakeholders and service users."
  stem: none
  statementType: expectation
  rung: none
  force: will
  level: none
  appliesTo: "Health Studies courses and the teams who run them"
  addressee: provider
  verbs: ["underpinned", "communicate"]
  about: "design resting on frameworks and standards"
  themes: [none]
  domain: none
  award: ["bachelor's with honours", "master's"]
  gradeOf: none
  paraphrase: "Course design will rest on national qualifications frameworks and sector-recognised standards, so that what an award represents is clear to stakeholders and service users."
  quote: full   # the issuer's statement is in `source` (D-std-0014)
  audience: practitioner
  subjects: inherited
- id: qaa/health-studies-2024/2.4
  locator: { number: "2.4", headingPath: ["Distinctive features of the Health Studies degree", "Design"] }
  span: { start: 39177, end: 39395 }
  source: "Course teams should integrate the dimensions of EDI as outlined in section 1 within all aspects of the educational experience to ensure that students have an equal opportunity to participate in and complete the course."
  stem: none
  statementType: requirement
  rung: none
  force: should
  level: none
  appliesTo: "Health Studies courses and the teams who run them"
  addressee: provider
  verbs: ["integrate", "ensure", "participate", "complete"]
  about: "EDI throughout the student experience"
  themes: [theme:edi]
  domain: none
  award: ["bachelor's with honours", "master's"]
  gradeOf: none
  paraphrase: "Course teams should build the dimensions of equality, diversity and inclusion from section 1 into every part of the educational experience, so that all students have an equal chance to take part and finish."
  quote: full   # the issuer's statement is in `source` (D-std-0014)
  audience: practitioner
  subjects: inherited
- id: qaa/health-studies-2024/2.5
  locator: { number: "2.5", headingPath: ["Distinctive features of the Health Studies degree", "Design"] }
  span: { start: 42168, end: 42342 }
  source: "Students should be given ‘the opportunity to gain knowledge and understanding of the needs of patients from diverse social, cultural and ethnic backgrounds’ (GMC, 2015, p33)."
  stem: none
  statementType: requirement
  rung: none
  force: should
  level: none
  appliesTo: "Health Studies courses and the teams who run them"
  addressee: provider
  verbs: ["given", "gain"]
  about: "learning about diverse patients' needs"
  themes: [theme:edi]
  domain: none
  award: ["bachelor's with honours", "master's"]
  gradeOf: none
  paraphrase: "Students should have the chance to learn what patients from varied social, cultural and ethnic backgrounds need; the statement takes this wording from the GMC's standards for medical education."
  quote: full   # the issuer's statement is in `source` (D-std-0014)
  audience: practitioner
  subjects: inherited
- id: qaa/health-studies-2024/2.10
  locator: { number: "2.10", headingPath: ["Distinctive features of the Health Studies degree", "Progression"] }
  span: { start: 44926, end: 45749 }
  source: "2.10 Over the course of a degree with honours (FHEQ Level 6; FQHEIS Level 10) a Health Studies student will progress from one level of study to the next, in line with the regulations and processes for each institution. Initially, students will develop basic subject knowledge, and will progress on the course with the appropriate levels of depth, challenge, complexity and autonomy associated with the level of study. It is expected that each level would see the attainment of knowledge, understanding, skills, behaviours and values that build towards the final achievement of meeting the threshold-level, subject-specific and generic skills listed in this Statement. This will usually include successful completion and the award of credit for the full range of learning and assessment, including any practical components.\n"
  stem: none
  statementType: expectation
  rung: none
  force: will
  level: fheq:6
  appliesTo: "honours students of the subject"
  addressee: learner
  verbs: ["progress", "develop", "expected"]
  about: "progression through the honours levels"
  themes: [none]
  domain: none
  award: ["bachelor's with honours"]
  gradeOf: none
  paraphrase: "Across an honours degree at FHEQ level 6 (FQHEIS level 10), students will move up level by level, starting from basic subject knowledge and taking on more depth, challenge, complexity and autonomy, until they meet the threshold subject-specific and generic skills; this usually means passing all learning and assessment, practical parts included."
  quote: full   # the issuer's statement is in `source` (D-std-0014)
  audience: both
  subjects: inherited
- id: qaa/health-studies-2024/2.11
  locator: { number: "2.11", headingPath: ["Distinctive features of the Health Studies degree", "Progression"] }
  span: { start: 45754, end: 45995 }
  source: "Students will move gradually from highly structured, directed study which scaffolds learning and supports their transition to higher education, into a more autonomous position where they manage and take responsibility for their own learning."
  stem: none
  statementType: expectation
  rung: none
  force: will
  level: none
  appliesTo: "undergraduate students of the subject"
  addressee: learner
  verbs: ["move", "manage", "take"]
  about: "from structured study to autonomy"
  themes: [none]
  domain: none
  award: ["bachelor's with honours"]
  gradeOf: none
  paraphrase: "Students will move step by step from closely guided, structured study that eases their entry to higher education to a more independent position in which they run their own learning."
  quote: full   # the issuer's statement is in `source` (D-std-0014)
  audience: both
  subjects: inherited
- id: qaa/health-studies-2024/2.11.b1
  locator: { number: "2.11.b1", headingPath: ["Distinctive features of the Health Studies degree", "Progression"] }
  span: { start: 46056, end: 46132 }
  source: "recognise the diversity of prior experience and the challenges of transition"
  stem: "2.11"
  statementType: requirement
  rung: none
  force: should
  level: none
  appliesTo: "Health Studies courses and the teams who run them"
  addressee: provider
  verbs: ["recognise"]
  about: "prior experience and transition"
  themes: [none]
  domain: none
  award: ["bachelor's with honours", "master's"]
  gradeOf: none
  paraphrase: "Strategies for progression should take account of students' varied prior experience and of how hard the move into higher education can be."
  quote: full   # the issuer's statement is in `source` (D-std-0014)
  audience: practitioner
  subjects: inherited
- id: qaa/health-studies-2024/2.11.b2
  locator: { number: "2.11.b2", headingPath: ["Distinctive features of the Health Studies degree", "Progression"] }
  span: { start: 46135, end: 46285 }
  source: "allow all students to achieve their potential and realise their ambitions, irrespective of their background or motivations for studying Health Studies"
  stem: "2.11"
  statementType: requirement
  rung: none
  force: should
  level: none
  appliesTo: "Health Studies courses and the teams who run them"
  addressee: provider
  verbs: ["allow", "achieve", "realise"]
  about: "every student reaching their potential"
  themes: [none]
  domain: none
  award: ["bachelor's with honours", "master's"]
  gradeOf: none
  paraphrase: "They should let every student reach their potential and ambitions, whatever their background or reasons for choosing the subject."
  quote: full   # the issuer's statement is in `source` (D-std-0014)
  audience: practitioner
  subjects: inherited
- id: qaa/health-studies-2024/2.11.b3
  locator: { number: "2.11.b3", headingPath: ["Distinctive features of the Health Studies degree", "Progression"] }
  span: { start: 46288, end: 46370 }
  source: "support academic and personal development in addition to subject-specific learning"
  stem: "2.11"
  statementType: requirement
  rung: none
  force: should
  level: none
  appliesTo: "Health Studies courses and the teams who run them"
  addressee: provider
  verbs: ["support"]
  about: "academic and personal development"
  themes: [none]
  domain: none
  award: ["bachelor's with honours", "master's"]
  gradeOf: none
  paraphrase: "They should support academic and personal growth as well as learning in the subject itself."
  quote: full   # the issuer's statement is in `source` (D-std-0014)
  audience: practitioner
  subjects: inherited
- id: qaa/health-studies-2024/2.11.b4
  locator: { number: "2.11.b4", headingPath: ["Distinctive features of the Health Studies degree", "Progression"] }
  span: { start: 46373, end: 46457 }
  source: "are matched to the course learning outcomes or competencies for each level of study."
  stem: "2.11"
  statementType: requirement
  rung: none
  force: should
  level: none
  appliesTo: "Health Studies courses and the teams who run them"
  addressee: provider
  verbs: ["matched"]
  about: "fit with outcomes at each level"
  themes: [none]
  domain: none
  award: ["bachelor's with honours", "master's"]
  gradeOf: none
  paraphrase: "They should fit the course's learning outcomes or competences at each level of study."
  quote: full   # the issuer's statement is in `source` (D-std-0014)
  audience: practitioner
  subjects: inherited
- id: qaa/health-studies-2024/2.13
  locator: { number: "2.13", headingPath: ["Distinctive features of the Health Studies degree", "Progression"] }
  span: { start: 46871, end: 47297 }
  source: "2.13 Undergraduates studying Health Studies courses as part of a combined or joint degree with other subjects will achieve core elements of the specific and generic skills outlined in this Statement and will add others according to the topics covered in the other subject(s) of their degree. Additionally, they may explore the overlap between different disciplines, creating further opportunities for interdisciplinary study.\n"
  stem: none
  statementType: expectation
  rung: none
  force: will
  level: fheq:6
  appliesTo: "undergraduates on combined or joint degrees"
  addressee: learner
  verbs: ["achieve", "add", "explore"]
  about: "joint and combined degrees"
  themes: [none]
  domain: none
  award: ["bachelor's with honours"]
  gradeOf: none
  paraphrase: "Undergraduates who take the subject in a combined or joint degree will reach the core of this statement's specific and generic skills and add others from their other subject; they may also explore where the disciplines overlap."
  quote: full   # the issuer's statement is in `source` (D-std-0014)
  audience: both
  subjects: inherited
- id: qaa/health-studies-2024/2.16
  locator: { number: "2.16", headingPath: ["Distinctive features of the Health Studies degree", "Flexibility"] }
  span: { start: 48527, end: 48700 }
  source: "The range of delivery methods offered through Health Studies courses will be diverse and appropriate for the needs of the student, the taught material and their assessments."
  stem: none
  statementType: expectation
  rung: none
  force: will
  level: none
  appliesTo: "Health Studies courses and the teams who run them"
  addressee: provider
  verbs: ["offered"]
  about: "varied delivery methods"
  themes: [none]
  domain: none
  award: ["bachelor's with honours", "master's"]
  gradeOf: none
  paraphrase: "Courses will offer a varied range of delivery methods suited to the student, the material and how it is assessed."
  quote: full   # the issuer's statement is in `source` (D-std-0014)
  audience: practitioner
  subjects: inherited
- id: qaa/health-studies-2024/2.18
  locator: { number: "2.18", headingPath: ["Distinctive features of the Health Studies degree", "Flexibility"] }
  span: { start: 50530, end: 50744 }
  source: "Course design and review will be sufficiently flexible to allow course teams to address the needs of students, industry and society while considering requirements raised by external governing or accrediting bodies."
  stem: none
  statementType: expectation
  rung: none
  force: will
  level: none
  appliesTo: "Health Studies courses and the teams who run them"
  addressee: provider
  verbs: ["allow", "address", "considering"]
  about: "flexible design and review"
  themes: [none]
  domain: none
  award: ["bachelor's with honours", "master's"]
  gradeOf: none
  paraphrase: "Course design and review will be flexible enough for teams to meet the needs of students, industry and society while taking account of what external governing or accrediting bodies require."
  quote: full   # the issuer's statement is in `source` (D-std-0014)
  audience: practitioner
  subjects: inherited
- id: qaa/health-studies-2024/2.19
  locator: { number: "2.19", headingPath: ["Distinctive features of the Health Studies degree", "Partnership"] }
  span: { start: 50762, end: 50909 }
  source: "It is envisaged that relevant stakeholders will be engaged as partners in the process of planning, development, delivery and evaluation of courses."
  stem: none
  statementType: expectation
  rung: none
  force: will
  level: none
  appliesTo: "Health Studies courses and the teams who run them"
  addressee: provider
  verbs: ["envisaged", "engaged"]
  about: "stakeholders as partners"
  themes: [none]
  domain: none
  award: ["bachelor's with honours", "master's"]
  gradeOf: none
  paraphrase: "Stakeholders will be brought in as partners in planning, developing, delivering and evaluating courses."
  quote: full   # the issuer's statement is in `source` (D-std-0014)
  audience: practitioner
  subjects: inherited
- id: qaa/health-studies-2024/2.20
  locator: { number: "2.20", headingPath: ["Distinctive features of the Health Studies degree", "Partnership"] }
  span: { start: 52520, end: 52609 }
  source: "Where relevant, courses should be written in alignment with the relevant regulatory body."
  stem: none
  statementType: requirement
  rung: none
  force: should
  level: none
  appliesTo: "Health Studies courses and the teams who run them"
  addressee: provider
  verbs: ["written"]
  about: "alignment with the regulatory body"
  themes: [none]
  domain: none
  award: ["bachelor's with honours", "master's"]
  gradeOf: none
  paraphrase: "Where it applies, courses should be written to align with the relevant regulatory body."
  quote: full   # the issuer's statement is in `source` (D-std-0014)
  audience: practitioner
  subjects: inherited
- id: qaa/health-studies-2024/2.22
  locator: { number: "2.22", headingPath: ["Distinctive features of the Health Studies degree", "Partnership"] }
  span: { start: 53335, end: 53487 }
  source: "Employers and higher education providers will ensure apprentices are given the support necessary to achieve professional and/or occupational competence."
  stem: none
  statementType: expectation
  rung: none
  force: will
  level: none
  appliesTo: "employers and providers of apprenticeship degrees"
  addressee: provider
  verbs: ["ensure", "given", "achieve"]
  about: "support for apprentices"
  themes: [none]
  domain: none
  award: ["bachelor's with honours", "master's"]
  gradeOf: none
  paraphrase: "Employers and providers will make sure apprentices get the support they need to reach professional or occupational competence."
  quote: full   # the issuer's statement is in `source` (D-std-0014)
  audience: practitioner
  subjects: inherited
- id: qaa/health-studies-2024/2.23
  locator: { number: "2.23", headingPath: ["Distinctive features of the Health Studies degree", "Monitoring and review"] }
  span: { start: 53942, end: 53995 }
  source: "Considering the student voice will form part of this."
  stem: none
  statementType: expectation
  rung: none
  force: will
  level: none
  appliesTo: "Health Studies courses and the teams who run them"
  addressee: provider
  verbs: ["considering", "form"]
  about: "the student voice in review"
  themes: [none]
  domain: none
  award: ["bachelor's with honours", "master's"]
  gradeOf: none
  paraphrase: "Course review will take account of what students say."
  quote: full   # the issuer's statement is in `source` (D-std-0014)
  audience: practitioner
  subjects: inherited
- id: qaa/health-studies-2024/2.24
  locator: { number: "2.24", headingPath: ["Distinctive features of the Health Studies degree", "Monitoring and review"] }
  span: { start: 54496, end: 54704 }
  source: "Providers will use external reviewers as part of periodic review to gain an external perspective on any proposed changes and ensure threshold standards are achieved and content is appropriate for the subject."
  stem: none
  statementType: expectation
  rung: none
  force: will
  level: none
  appliesTo: "Health Studies courses and the teams who run them"
  addressee: provider
  verbs: ["use", "gain", "ensure"]
  about: "external reviewers in periodic review"
  themes: [none]
  domain: none
  award: ["bachelor's with honours", "master's"]
  gradeOf: none
  paraphrase: "Providers will bring external reviewers into periodic review for an outside view of proposed changes, to confirm that threshold standards are met and content suits the subject."
  quote: full   # the issuer's statement is in `source` (D-std-0014)
  audience: practitioner
  subjects: inherited
- id: qaa/health-studies-2024/2.27
  locator: { number: "2.27", headingPath: ["Distinctive features of the Health Studies degree", "Monitoring and review"] }
  span: { start: 55829, end: 56004 }
  source: "A range of external reference points, including this Subject Benchmark Statement, will be considered to ensure that higher education provision aligns with health sector norms."
  stem: none
  statementType: expectation
  rung: none
  force: will
  level: none
  appliesTo: "Health Studies courses and the teams who run them"
  addressee: provider
  verbs: ["considered", "ensure"]
  about: "external reference points in review"
  themes: [none]
  domain: none
  award: ["bachelor's with honours", "master's"]
  gradeOf: none
  paraphrase: "Review will weigh a range of external reference points, this statement among them, so that provision matches the norms of the health sector."
  quote: full   # the issuer's statement is in `source` (D-std-0014)
  audience: practitioner
  subjects: inherited
- id: qaa/health-studies-2024/2.28.b1
  locator: { number: "2.28.b1", headingPath: ["Distinctive features of the Health Studies degree", "Monitoring and review"] }
  span: { start: 56363, end: 56519 }
  source: "an inclusive curriculum by reviewing the alignment between the intended curriculum, the implemented curriculum, and the attained curriculum (QAA, 2021, p11)"
  stem: "2.28"
  statementType: expectation
  rung: none
  force: will
  level: none
  appliesTo: "Health Studies courses and the teams who run them"
  addressee: provider
  verbs: ["reviewing"]
  about: "an inclusive, aligned curriculum"
  themes: [none]
  domain: none
  award: ["bachelor's with honours", "master's"]
  gradeOf: none
  paraphrase: "Monitoring and review will support an inclusive curriculum by checking that the planned, delivered and achieved curriculum line up."
  quote: full   # the issuer's statement is in `source` (D-std-0014)
  audience: practitioner
  subjects: inherited
- id: qaa/health-studies-2024/2.28.b2
  locator: { number: "2.28.b2", headingPath: ["Distinctive features of the Health Studies degree", "Monitoring and review"] }
  span: { start: 56522, end: 56606 }
  source: "A dynamic and responsive curriculum that incorporates feedback from key stakeholders"
  stem: "2.28"
  statementType: expectation
  rung: none
  force: will
  level: none
  appliesTo: "Health Studies courses and the teams who run them"
  addressee: provider
  verbs: ["incorporates"]
  about: "a responsive curriculum"
  themes: [none]
  domain: none
  award: ["bachelor's with honours", "master's"]
  gradeOf: none
  paraphrase: "They will support a curriculum that responds to change and takes in feedback from key stakeholders."
  quote: full   # the issuer's statement is in `source` (D-std-0014)
  audience: practitioner
  subjects: inherited
- id: qaa/health-studies-2024/2.28.b3
  locator: { number: "2.28.b3", headingPath: ["Distinctive features of the Health Studies degree", "Monitoring and review"] }
  span: { start: 56609, end: 56708 }
  source: "the embedding of institutional goals and sector-wide best practice throughout the entire curriculum"
  stem: "2.28"
  statementType: expectation
  rung: none
  force: will
  level: none
  appliesTo: "Health Studies courses and the teams who run them"
  addressee: provider
  verbs: ["embedding"]
  about: "institutional goals and sector practice"
  themes: [none]
  domain: none
  award: ["bachelor's with honours", "master's"]
  gradeOf: none
  paraphrase: "They will support embedding the institution's goals and the sector's best practice across the curriculum."
  quote: full   # the issuer's statement is in `source` (D-std-0014)
  audience: practitioner
  subjects: inherited
- id: qaa/health-studies-2024/2.28.b4
  locator: { number: "2.28.b4", headingPath: ["Distinctive features of the Health Studies degree", "Monitoring and review"] }
  span: { start: 56711, end: 56822 }
  source: "academic standards in health studies to meet the requirements of the relevant national qualifications framework"
  stem: "2.28"
  statementType: expectation
  rung: none
  force: will
  level: none
  appliesTo: "Health Studies courses and the teams who run them"
  addressee: provider
  verbs: ["meet"]
  about: "standards meeting the qualifications framework"
  themes: [none]
  domain: none
  award: ["bachelor's with honours", "master's"]
  gradeOf: none
  paraphrase: "They will support academic standards that satisfy the relevant national qualifications framework."
  quote: full   # the issuer's statement is in `source` (D-std-0014)
  audience: practitioner
  subjects: inherited
- id: qaa/health-studies-2024/2.28.b5
  locator: { number: "2.28.b5", headingPath: ["Distinctive features of the Health Studies degree", "Monitoring and review"] }
  span: { start: 56825, end: 56867 }
  source: "internal and external moderation processes"
  stem: "2.28"
  statementType: expectation
  rung: none
  force: will
  level: none
  appliesTo: "Health Studies courses and the teams who run them"
  addressee: provider
  verbs: []
  about: "moderation"
  themes: [none]
  domain: none
  award: ["bachelor's with honours", "master's"]
  gradeOf: none
  paraphrase: "They will support moderation, inside the institution and from outside it."
  quote: full   # the issuer's statement is in `source` (D-std-0014)
  audience: practitioner
  subjects: inherited
- id: qaa/health-studies-2024/2.28.b6
  locator: { number: "2.28.b6", headingPath: ["Distinctive features of the Health Studies degree", "Monitoring and review"] }
  span: { start: 56870, end: 56900 }
  source: "institutional internal reviews"
  stem: "2.28"
  statementType: expectation
  rung: none
  force: will
  level: none
  appliesTo: "Health Studies courses and the teams who run them"
  addressee: provider
  verbs: []
  about: "internal reviews"
  themes: [none]
  domain: none
  award: ["bachelor's with honours", "master's"]
  gradeOf: none
  paraphrase: "They will support the institution's own internal reviews."
  quote: full   # the issuer's statement is in `source` (D-std-0014)
  audience: practitioner
  subjects: inherited
- id: qaa/health-studies-2024/2.28.b7
  locator: { number: "2.28.b7", headingPath: ["Distinctive features of the Health Studies degree", "Monitoring and review"] }
  span: { start: 56903, end: 56986 }
  source: "internal or external annual monitoring to align with professional body requirements"
  stem: "2.28"
  statementType: expectation
  rung: none
  force: will
  level: none
  appliesTo: "Health Studies courses and the teams who run them"
  addressee: provider
  verbs: ["align"]
  about: "annual monitoring and professional bodies"
  themes: [none]
  domain: none
  award: ["bachelor's with honours", "master's"]
  gradeOf: none
  paraphrase: "They will support annual monitoring, internal or external, in line with what professional bodies require."
  quote: full   # the issuer's statement is in `source` (D-std-0014)
  audience: practitioner
  subjects: inherited
- id: qaa/health-studies-2024/2.28.b8
  locator: { number: "2.28.b8", headingPath: ["Distinctive features of the Health Studies degree", "Monitoring and review"] }
  span: { start: 56989, end: 57068 }
  source: "transparent communication within teaching teams and across stakeholder partners"
  stem: "2.28"
  statementType: expectation
  rung: none
  force: will
  level: none
  appliesTo: "Health Studies courses and the teams who run them"
  addressee: provider
  verbs: []
  about: "open communication"
  themes: [none]
  domain: none
  award: ["bachelor's with honours", "master's"]
  gradeOf: none
  paraphrase: "They will support open communication within teaching teams and with stakeholder partners."
  quote: full   # the issuer's statement is in `source` (D-std-0014)
  audience: practitioner
  subjects: inherited
- id: qaa/health-studies-2024/2.28.b9
  locator: { number: "2.28.b9", headingPath: ["Distinctive features of the Health Studies degree", "Monitoring and review"] }
  span: { start: 57071, end: 57140 }
  source: "compliance with Competitions and Markets Authority (CMA) requirements"
  stem: "2.28"
  statementType: expectation
  rung: none
  force: will
  level: none
  appliesTo: "Health Studies courses and the teams who run them"
  addressee: provider
  verbs: []
  about: "consumer law compliance"
  themes: [none]
  domain: none
  award: ["bachelor's with honours", "master's"]
  gradeOf: none
  paraphrase: "They will support compliance with the requirements of the Competitions and Markets Authority."
  quote: full   # the issuer's statement is in `source` (D-std-0014)
  audience: practitioner
  subjects: inherited
- id: qaa/health-studies-2024/2.28.b10
  locator: { number: "2.28.b10", headingPath: ["Distinctive features of the Health Studies degree", "Monitoring and review"] }
  span: { start: 57143, end: 57391 }
  source: "feedback from external quality assurance and enhancement exercises, including, for example, the Teaching Excellence Framework (TEF), National Student Survey (NSS), and the Postgraduate Taught and Research Student Experience Surveys (PTES and PRES)."
  stem: "2.28"
  statementType: expectation
  rung: none
  force: will
  level: none
  appliesTo: "Health Studies courses and the teams who run them"
  addressee: provider
  verbs: []
  about: "feedback from external quality exercises"
  themes: [none]
  domain: none
  award: ["bachelor's with honours", "master's"]
  gradeOf: none
  paraphrase: "They will support use of feedback from external quality exercises such as the TEF, the NSS, PTES and PRES."
  quote: full   # the issuer's statement is in `source` (D-std-0014)
  audience: practitioner
  subjects: inherited
- id: qaa/health-studies-2024/3.3
  locator: { number: "3.3", headingPath: ["Content, structure and delivery", "Teaching and learning"] }
  span: { start: 59476, end: 59663 }
  source: "The learning and teaching strategies will be clearly specified within the course of study, and will consider the diverse learning and teaching cultures that students may have experienced."
  stem: none
  statementType: expectation
  rung: none
  force: will
  level: none
  appliesTo: "Health Studies courses and the teams who run them"
  addressee: provider
  verbs: ["specified", "consider"]
  about: "specified, culturally aware teaching strategies"
  themes: [none]
  domain: none
  award: ["bachelor's with honours", "master's"]
  gradeOf: none
  paraphrase: "Teaching and learning strategies will be set out clearly in the course and will take account of the different learning and teaching cultures students bring."
  quote: full   # the issuer's statement is in `source` (D-std-0014)
  audience: practitioner
  subjects: inherited
- id: qaa/health-studies-2024/3.4
  locator: { number: "3.4", headingPath: ["Content, structure and delivery", "Teaching and learning"] }
  span: { start: 59830, end: 60016 }
  source: "3.4 Health Studies courses should engage in critical evaluation and analysis to develop skills in students such as problem-solving, evaluating solutions, decision making and creativity.\n"
  stem: none
  statementType: requirement
  rung: none
  force: should
  level: none
  appliesTo: "Health Studies courses and the teams who run them"
  addressee: provider
  verbs: ["engage", "develop"]
  about: "critical evaluation to build skills"
  themes: [none]
  domain: none
  award: ["bachelor's with honours", "master's"]
  gradeOf: none
  paraphrase: "Courses should use critical evaluation and analysis to build students' skills in problem-solving, judging solutions, deciding and creativity."
  quote: full   # the issuer's statement is in `source` (D-std-0014)
  audience: practitioner
  subjects: inherited
- id: qaa/health-studies-2024/3.7.b1
  locator: { number: "3.7.b1", headingPath: ["Content, structure and delivery", "Assessment"] }
  span: { start: 60994, end: 61159 }
  source: "Assessment will be both\n\n20\nformative and summative. A range of assessment methods will reflect progression within the course of study and support graduate outcomes."
  stem: "3.7"
  statementType: expectation
  rung: none
  force: will
  level: none
  appliesTo: "Health Studies courses and the teams who run them"
  addressee: provider
  verbs: ["reflect", "support"]
  about: "formative and summative assessment"
  themes: [none]
  domain: none
  award: ["bachelor's with honours", "master's"]
  gradeOf: none
  paraphrase: "Assessment will be formative and summative, and a range of methods will track progression through the course and support graduate outcomes."
  quote: full   # the issuer's statement is in `source` (D-std-0014)
  audience: practitioner
  subjects: inherited
- id: qaa/health-studies-2024/3.7.b2
  locator: { number: "3.7.b2", headingPath: ["Content, structure and delivery", "Assessment"] }
  span: { start: 61490, end: 61684 }
  source: "Reasonable adjustments are necessary and should be appropriate to the demands of the curriculum, and sliding scales can be implemented to support inclusive assessment (see paragraphs 1.24-1.26)."
  stem: "3.7"
  statementType: requirement
  rung: none
  force: should
  level: none
  appliesTo: "Health Studies courses and the teams who run them"
  addressee: provider
  verbs: ["implemented", "support"]
  about: "reasonable adjustments in assessment"
  themes: [none]
  domain: none
  award: ["bachelor's with honours", "master's"]
  gradeOf: none
  paraphrase: "Reasonable adjustments are needed and should fit the curriculum's demands; sliding scales can help make assessment inclusive."
  quote: full   # the issuer's statement is in `source` (D-std-0014)
  audience: practitioner
  subjects: inherited
- id: qaa/health-studies-2024/3.7.b3
  locator: { number: "3.7.b3", headingPath: ["Content, structure and delivery", "Assessment"] }
  span: { start: 61685, end: 61850 }
  source: "Educators should consider the extent to which generative artificial intelligence (AI) tools are incorporated into their teaching, learning and assessment strategies."
  stem: "3.7"
  statementType: requirement
  rung: none
  force: should
  level: none
  appliesTo: "teaching staff on the course"
  addressee: provider
  verbs: ["consider", "incorporated"]
  about: "generative AI in teaching and assessment"
  themes: [none]
  domain: none
  award: ["bachelor's with honours", "master's"]
  gradeOf: none
  paraphrase: "Teaching staff should decide how far generative AI tools enter their teaching, learning and assessment."
  quote: full   # the issuer's statement is in `source` (D-std-0014)
  audience: practitioner
  subjects: inherited
- id: qaa/health-studies-2024/3.7.b4
  locator: { number: "3.7.b4", headingPath: ["Content, structure and delivery", "Assessment"] }
  span: { start: 61947, end: 62105 }
  source: "However, both educators and students must remain cognisant of the limitations and risks involved, with a view to exercising responsible and ethical practices."
  stem: "3.7"
  statementType: requirement
  rung: none
  force: must
  level: fheq:6
  appliesTo: "teaching staff and students"
  addressee: both
  verbs: ["remain", "exercising"]
  about: "the limits and risks of AI"
  themes: [none]
  domain: generic-skill
  award: ["bachelor's with honours", "master's"]
  gradeOf: none
  paraphrase: "Staff and students alike must stay aware of the limits and risks of AI tools so that their use stays responsible and ethical."
  quote: full   # the issuer's statement is in `source` (D-std-0014)
  audience: both
  subjects: inherited
- id: qaa/health-studies-2024/3.9.b1
  locator: { number: "3.9.b1", headingPath: ["Content, structure and delivery", "Assessment"] }
  span: { start: 63486, end: 63592 }
  source: "Effective feedback will be personal, individual, understandable, empowering, manageable and developmental."
  stem: "3.9"
  statementType: expectation
  rung: none
  force: will
  level: none
  appliesTo: "Health Studies courses and the teams who run them"
  addressee: provider
  verbs: []
  about: "qualities of good feedback"
  themes: [none]
  domain: none
  award: ["bachelor's with honours", "master's"]
  gradeOf: none
  paraphrase: "Good feedback will be personal to the student, clear, empowering, manageable and aimed at development."
  quote: full   # the issuer's statement is in `source` (D-std-0014)
  audience: practitioner
  subjects: inherited
- id: qaa/health-studies-2024/3.9.b2
  locator: { number: "3.9.b2", headingPath: ["Content, structure and delivery", "Assessment"] }
  span: { start: 63593, end: 63827 }
  source: "It should be timely, relevant to the assessment brief and accompanied by access to interpretative support/advice. Feedback should allow students the opportunity for supportive reflection on their academic and professional development."
  stem: "3.9"
  statementType: requirement
  rung: none
  force: should
  level: none
  appliesTo: "Health Studies courses and the teams who run them"
  addressee: provider
  verbs: ["accompanied", "allow"]
  about: "timely feedback that supports reflection"
  themes: [none]
  domain: none
  award: ["bachelor's with honours", "master's"]
  gradeOf: none
  paraphrase: "Feedback should be prompt, tied to the assessment brief and backed by help in interpreting it, and should give students room to reflect on their academic and professional growth."
  quote: full   # the issuer's statement is in `source` (D-std-0014)
  audience: practitioner
  subjects: inherited
- id: qaa/health-studies-2024/3.9.b3
  locator: { number: "3.9.b3", headingPath: ["Content, structure and delivery", "Assessment"] }
  span: { start: 63828, end: 63925 }
  source: "The nature, extent and timing of feedback for each assessment task will be made clear in advance."
  stem: "3.9"
  statementType: expectation
  rung: none
  force: will
  level: none
  appliesTo: "Health Studies courses and the teams who run them"
  addressee: provider
  verbs: ["made"]
  about: "feedback arrangements known in advance"
  themes: [none]
  domain: none
  award: ["bachelor's with honours", "master's"]
  gradeOf: none
  paraphrase: "Students will be told beforehand what feedback each task brings, how much and when."
  quote: full   # the issuer's statement is in `source` (D-std-0014)
  audience: practitioner
  subjects: inherited
- id: qaa/health-studies-2024/3.10.b1
  locator: { number: "3.10.b1", headingPath: ["Content, structure and delivery", "Assessment"] }
  span: { start: 64796, end: 64829 }
  source: "be valid, reliable and consistent"
  stem: "3.10"
  statementType: requirement
  rung: none
  force: should
  level: none
  appliesTo: "Health Studies courses and the teams who run them"
  addressee: provider
  verbs: ["be"]
  about: "valid, reliable, consistent feedback"
  themes: [none]
  domain: none
  award: ["bachelor's with honours", "master's"]
  gradeOf: none
  paraphrase: "Feedback should be sound, dependable and even across markers."
  quote: full   # the issuer's statement is in `source` (D-std-0014)
  audience: practitioner
  subjects: inherited
- id: qaa/health-studies-2024/3.10.b2
  locator: { number: "3.10.b2", headingPath: ["Content, structure and delivery", "Assessment"] }
  span: { start: 64832, end: 64854 }
  source: "be clear and available"
  stem: "3.10"
  statementType: requirement
  rung: none
  force: should
  level: none
  appliesTo: "Health Studies courses and the teams who run them"
  addressee: provider
  verbs: ["be"]
  about: "clear and available feedback"
  themes: [none]
  domain: none
  award: ["bachelor's with honours", "master's"]
  gradeOf: none
  paraphrase: "Feedback should be clear and easy for students to get hold of."
  quote: full   # the issuer's statement is in `source` (D-std-0014)
  audience: practitioner
  subjects: inherited
- id: qaa/health-studies-2024/3.10.b3
  locator: { number: "3.10.b3", headingPath: ["Content, structure and delivery", "Assessment"] }
  span: { start: 64857, end: 64949 }
  source: "take into account accessibility and EDI considerations, for example, specific learning needs"
  stem: "3.10"
  statementType: requirement
  rung: none
  force: should
  level: none
  appliesTo: "Health Studies courses and the teams who run them"
  addressee: provider
  verbs: ["take"]
  about: "accessibility and EDI in feedback"
  themes: [none]
  domain: none
  award: ["bachelor's with honours", "master's"]
  gradeOf: none
  paraphrase: "Feedback should allow for accessibility and equality, diversity and inclusion, such as particular learning needs."
  quote: full   # the issuer's statement is in `source` (D-std-0014)
  audience: practitioner
  subjects: inherited
- id: qaa/health-studies-2024/3.10.b4
  locator: { number: "3.10.b4", headingPath: ["Content, structure and delivery", "Assessment"] }
  span: { start: 64952, end: 65030 }
  source: "be integral to the course of study and clearly relate to the learning outcomes"
  stem: "3.10"
  statementType: requirement
  rung: none
  force: should
  level: none
  appliesTo: "Health Studies courses and the teams who run them"
  addressee: provider
  verbs: ["be", "relate"]
  about: "feedback tied to outcomes"
  themes: [none]
  domain: none
  award: ["bachelor's with honours", "master's"]
  gradeOf: none
  paraphrase: "Feedback should be part of the course and plainly linked to its learning outcomes."
  quote: full   # the issuer's statement is in `source` (D-std-0014)
  audience: practitioner
  subjects: inherited
- id: qaa/health-studies-2024/3.10.b5
  locator: { number: "3.10.b5", headingPath: ["Content, structure and delivery", "Assessment"] }
  span: { start: 65033, end: 65105 }
  source: "give the student the opportunity to validate knowledge and understanding"
  stem: "3.10"
  statementType: requirement
  rung: none
  force: should
  level: none
  appliesTo: "Health Studies courses and the teams who run them"
  addressee: provider
  verbs: ["give", "validate"]
  about: "confirming knowledge"
  themes: [none]
  domain: none
  award: ["bachelor's with honours", "master's"]
  gradeOf: none
  paraphrase: "Feedback should let students confirm what they know and understand."
  quote: full   # the issuer's statement is in `source` (D-std-0014)
  audience: practitioner
  subjects: inherited
- id: qaa/health-studies-2024/3.10.b6
  locator: { number: "3.10.b6", headingPath: ["Content, structure and delivery", "Assessment"] }
  span: { start: 65108, end: 65166 }
  source: "align with progression and PSRB requirements as necessary."
  stem: "3.10"
  statementType: requirement
  rung: none
  force: should
  level: none
  appliesTo: "Health Studies courses and the teams who run them"
  addressee: provider
  verbs: ["align"]
  about: "progression and PSRB requirements"
  themes: [none]
  domain: none
  award: ["bachelor's with honours", "master's"]
  gradeOf: none
  paraphrase: "Feedback should fit the rules on progression and any PSRB requirements that apply."
  quote: full   # the issuer's statement is in `source` (D-std-0014)
  audience: practitioner
  subjects: inherited
- id: qaa/health-studies-2024/3.11
  locator: { number: "3.11", headingPath: ["Content, structure and delivery", "Supervision"] }
  span: { start: 65655, end: 65888 }
  source: "The role of supervision will be developed in partnership with educators, employers, and work-based supervisors, allowing students to contextualise their learning and make a positive contribution to health in the professional context."
  stem: none
  statementType: expectation
  rung: none
  force: will
  level: none
  appliesTo: "Health Studies courses and the teams who run them"
  addressee: provider
  verbs: ["developed", "allowing", "contextualise", "make"]
  about: "supervision shaped in partnership"
  themes: [none]
  domain: none
  award: ["bachelor's with honours", "master's"]
  gradeOf: none
  paraphrase: "Supervision will be shaped jointly by teaching staff, employers and workplace supervisors, helping students put learning in context and contribute to health in professional settings."
  quote: full   # the issuer's statement is in `source` (D-std-0014)
  audience: practitioner
  subjects: inherited
- id: qaa/health-studies-2024/3.12.b1
  locator: { number: "3.12.b1", headingPath: ["Content, structure and delivery", "Supervision"] }
  span: { start: 65967, end: 66064 }
  source: "preparation of supervisors in understanding diverse learning styles and the nature of assessments"
  stem: "3.12"
  statementType: requirement
  rung: none
  force: must
  level: none
  appliesTo: "Health Studies courses and the teams who run them"
  addressee: provider
  verbs: ["understanding"]
  about: "preparing supervisors"
  themes: [none]
  domain: none
  award: ["bachelor's with honours", "master's"]
  gradeOf: none
  paraphrase: "Supervision must take account of preparing supervisors to understand varied learning styles and how students are assessed."
  quote: full   # the issuer's statement is in `source` (D-std-0014)
  audience: practitioner
  subjects: inherited
- id: qaa/health-studies-2024/3.12.b2
  locator: { number: "3.12.b2", headingPath: ["Content, structure and delivery", "Supervision"] }
  span: { start: 66067, end: 66218 }
  source: "adoption of a collaborative approach to supervision, that can be directly or indirectly influenced by local or contextual practices to enhance learning"
  stem: "3.12"
  statementType: requirement
  rung: none
  force: must
  level: none
  appliesTo: "Health Studies courses and the teams who run them"
  addressee: provider
  verbs: ["influenced", "enhance"]
  about: "collaborative supervision"
  themes: [none]
  domain: none
  award: ["bachelor's with honours", "master's"]
  gradeOf: none
  paraphrase: "It must take account of a collaborative approach that local or contextual practice can shape to improve learning."
  quote: full   # the issuer's statement is in `source` (D-std-0014)
  audience: practitioner
  subjects: inherited
- id: qaa/health-studies-2024/3.12.b3
  locator: { number: "3.12.b3", headingPath: ["Content, structure and delivery", "Supervision"] }
  span: { start: 66221, end: 66293 }
  source: "objective setting, progress monitoring and action planning with students"
  stem: "3.12"
  statementType: requirement
  rung: none
  force: must
  level: none
  appliesTo: "Health Studies courses and the teams who run them"
  addressee: provider
  verbs: ["setting"]
  about: "objectives and action plans"
  themes: [none]
  domain: none
  award: ["bachelor's with honours", "master's"]
  gradeOf: none
  paraphrase: "It must take account of setting objectives, tracking progress and planning actions with students."
  quote: full   # the issuer's statement is in `source` (D-std-0014)
  audience: practitioner
  subjects: inherited
- id: qaa/health-studies-2024/3.12.b4
  locator: { number: "3.12.b4", headingPath: ["Content, structure and delivery", "Supervision"] }
  span: { start: 66296, end: 66346 }
  source: "promotion of an organisational culture of learning"
  stem: "3.12"
  statementType: requirement
  rung: none
  force: must
  level: none
  appliesTo: "Health Studies courses and the teams who run them"
  addressee: provider
  verbs: []
  about: "a learning culture"
  themes: [none]
  domain: none
  award: ["bachelor's with honours", "master's"]
  gradeOf: none
  paraphrase: "It must take account of promoting a culture of learning in the organisation."
  quote: full   # the issuer's statement is in `source` (D-std-0014)
  audience: practitioner
  subjects: inherited
- id: qaa/health-studies-2024/3.12.b5
  locator: { number: "3.12.b5", headingPath: ["Content, structure and delivery", "Supervision"] }
  span: { start: 66349, end: 66382 }
  source: "advocacy and coaching of students"
  stem: "3.12"
  statementType: requirement
  rung: none
  force: must
  level: none
  appliesTo: "Health Studies courses and the teams who run them"
  addressee: provider
  verbs: []
  about: "advocacy and coaching"
  themes: [none]
  domain: none
  award: ["bachelor's with honours", "master's"]
  gradeOf: none
  paraphrase: "It must take account of advocating for and coaching students."
  quote: full   # the issuer's statement is in `source` (D-std-0014)
  audience: practitioner
  subjects: inherited
- id: qaa/health-studies-2024/3.12.b6
  locator: { number: "3.12.b6", headingPath: ["Content, structure and delivery", "Supervision"] }
  span: { start: 66385, end: 66462 }
  source: "providing opportunities for critical reflection which build on prior learning"
  stem: "3.12"
  statementType: requirement
  rung: none
  force: must
  level: none
  appliesTo: "Health Studies courses and the teams who run them"
  addressee: provider
  verbs: ["providing", "build"]
  about: "critical reflection on earlier learning"
  themes: [none]
  domain: none
  award: ["bachelor's with honours", "master's"]
  gradeOf: none
  paraphrase: "It must take account of chances for critical reflection that build on earlier learning."
  quote: full   # the issuer's statement is in `source` (D-std-0014)
  audience: practitioner
  subjects: inherited
- id: qaa/health-studies-2024/3.12.b7
  locator: { number: "3.12.b7", headingPath: ["Content, structure and delivery", "Supervision"] }
  span: { start: 66465, end: 66524 }
  source: "tripartite supervision with the industry/healthcare sector."
  stem: "3.12"
  statementType: requirement
  rung: none
  force: must
  level: none
  appliesTo: "Health Studies courses and the teams who run them"
  addressee: provider
  verbs: []
  about: "three-way supervision"
  themes: [none]
  domain: none
  award: ["bachelor's with honours", "master's"]
  gradeOf: none
  paraphrase: "It must take account of three-way supervision involving the industry or healthcare sector."
  quote: full   # the issuer's statement is in `source` (D-std-0014)
  audience: practitioner
  subjects: inherited
- id: qaa/health-studies-2024/4.2
  locator: { number: "4.2", headingPath: ["Benchmark standards", "Introduction"] }
  span: { start: 67208, end: 67436 }
  source: "Each higher education provider has the autonomy in determining what appropriate evidence of this achievement will be and should refer to Annex D in The Frameworks for Higher Education Qualifications of UK Degree-Awarding Bodies."
  stem: none
  statementType: requirement
  rung: none
  force: should
  level: none
  appliesTo: "higher education providers"
  addressee: provider
  verbs: ["refer"]
  about: "Annex D for achievement above the threshold"
  themes: [none]
  domain: none
  award: ["bachelor's with honours", "master's"]
  gradeOf: none
  paraphrase: "Each provider decides what counts as evidence of achievement above the threshold and should refer to Annex D of the Frameworks for Higher Education Qualifications."
  quote: full   # the issuer's statement is in `source` (D-std-0014)
  audience: practitioner
  subjects: inherited
- id: qaa/health-studies-2024/4.3
  locator: { number: "4.3", headingPath: ["Benchmark standards", "Introduction"] }
  span: { start: 67590, end: 67794 }
  source: "The undergraduate minimum threshold Level 6 and the postgraduate minimum threshold Level 7 describe the minimum acceptable level of achievement that a student must demonstrate to be eligible for an award."
  stem: none
  statementType: requirement
  rung: none
  force: must
  level: ['fheq:6', 'fheq:7']
  appliesTo: "students seeking an honours or master's award"
  addressee: learner
  verbs: ["describe", "demonstrate"]
  about: "the threshold as the minimum for an award"
  themes: [none]
  domain: none
  award: ["bachelor's with honours", "master's"]
  gradeOf: none
  paraphrase: "The threshold at level 6 for undergraduates and at level 7 for postgraduates marks the least a student must show to be eligible for an award."
  quote: full   # the issuer's statement is in `source` (D-std-0014)
  audience: both
  subjects: inherited
- id: qaa/health-studies-2024/4.4.b1
  locator: { number: "4.4.b1", headingPath: ["Benchmark standards", "Threshold level: Subject knowledge, understanding and skills"] }
  span: { start: 67945, end: 68195 }
  source: "apply knowledge and understanding in interrelated contexts (as outlined in section 3 on Content, structure and delivery) and integrate relevant theoretical concepts that inform Health Studies in respect of physical, psychosocial and mental well-being"
  stem: "4.4"
  statementType: threshold
  rung: threshold
  force: threshold
  level: fheq:6
  appliesTo: "honours graduates in the subject"
  addressee: learner
  verbs: ["apply", "integrate"]
  about: "applying and joining theory across settings"
  themes: [none]
  domain: subject-skill
  award: ["bachelor's with honours"]
  gradeOf: none
  paraphrase: "As a minimum for honours, a graduate should be able to use their knowledge across linked settings and bring together the theories behind the subject on physical, psychosocial and mental well-being."
  quote: full   # the issuer's statement is in `source` (D-std-0014)
  audience: both
  subjects: inherited
- id: qaa/health-studies-2024/4.4.b2
  locator: { number: "4.4.b2", headingPath: ["Benchmark standards", "Threshold level: Subject knowledge, understanding and skills"] }
  span: { start: 68198, end: 68298 }
  source: "demonstrate an understanding of the scope and breadth of the subject in solving real- world problems"
  stem: "4.4"
  statementType: threshold
  rung: threshold
  force: threshold
  level: fheq:6
  appliesTo: "honours graduates in the subject"
  addressee: learner
  verbs: ["demonstrate"]
  about: "the breadth of the subject in real problems"
  themes: [none]
  domain: knowledge
  award: ["bachelor's with honours"]
  gradeOf: none
  paraphrase: "As a minimum for honours, a graduate should be able to show they grasp how wide the subject is by using it on practical problems."
  quote: full   # the issuer's statement is in `source` (D-std-0014)
  audience: both
  subjects: inherited
- id: qaa/health-studies-2024/4.4.b3
  locator: { number: "4.4.b3", headingPath: ["Benchmark standards", "Threshold level: Subject knowledge, understanding and skills"] }
  span: { start: 68301, end: 68404 }
  source: "adopt multiple perspectives to evaluate and problem-solve issues identified in health- related contexts"
  stem: "4.4"
  statementType: threshold
  rung: threshold
  force: threshold
  level: fheq:6
  appliesTo: "honours graduates in the subject"
  addressee: learner
  verbs: ["adopt", "evaluate", "problem-solve"]
  about: "judging issues from several viewpoints"
  themes: [none]
  domain: subject-skill
  award: ["bachelor's with honours"]
  gradeOf: none
  paraphrase: "As a minimum for honours, a graduate should be able to take more than one viewpoint when judging and resolving issues that arise in health settings."
  quote: full   # the issuer's statement is in `source` (D-std-0014)
  audience: both
  subjects: inherited
- id: qaa/health-studies-2024/4.4.b4
  locator: { number: "4.4.b4", headingPath: ["Benchmark standards", "Threshold level: Subject knowledge, understanding and skills"] }
  span: { start: 68407, end: 68564 }
  source: "synthesise specialist and interrelated knowledge of the multidisciplinary nature of Health Studies to create innovative solutions in health and health issues"
  stem: "4.4"
  statementType: threshold
  rung: threshold
  force: threshold
  level: fheq:6
  appliesTo: "honours graduates in the subject"
  addressee: learner
  verbs: ["synthesise", "create"]
  about: "joining specialist knowledge for new solutions"
  themes: [none]
  domain: subject-skill
  award: ["bachelor's with honours"]
  gradeOf: none
  paraphrase: "As a minimum for honours, a graduate should be able to combine specialist and linked knowledge from the subject's many disciplines to devise new answers to health problems."
  quote: full   # the issuer's statement is in `source` (D-std-0014)
  audience: both
  subjects: inherited
- id: qaa/health-studies-2024/4.4.b5
  locator: { number: "4.4.b5", headingPath: ["Benchmark standards", "Threshold level: Subject knowledge, understanding and skills"] }
  span: { start: 68567, end: 68712 }
  source: "synthesise and integrate evidence-based knowledge with relevant national policies and guidelines to inform Health Studies as a subject discipline"
  stem: "4.4"
  statementType: threshold
  rung: threshold
  force: threshold
  level: fheq:6
  appliesTo: "honours graduates in the subject"
  addressee: learner
  verbs: ["synthesise", "integrate", "inform"]
  about: "evidence with national policy and guidance"
  themes: [none]
  domain: subject-skill
  award: ["bachelor's with honours"]
  gradeOf: none
  paraphrase: "As a minimum for honours, a graduate should be able to join research evidence with relevant national policy and guidance and use the result to shape the subject."
  quote: full   # the issuer's statement is in `source` (D-std-0014)
  audience: both
  subjects: inherited
- id: qaa/health-studies-2024/4.4.b6
  locator: { number: "4.4.b6", headingPath: ["Benchmark standards", "Threshold level: Subject knowledge, understanding and skills"] }
  span: { start: 68715, end: 68838 }
  source: "understand health from a global perspective that reflects population mobility created by travel, migration and displacement"
  stem: "4.4"
  statementType: threshold
  rung: threshold
  force: threshold
  level: fheq:6
  appliesTo: "honours graduates in the subject"
  addressee: learner
  verbs: ["understand", "reflects"]
  about: "health in a global, mobile world"
  themes: [none]
  domain: understanding
  award: ["bachelor's with honours"]
  gradeOf: none
  paraphrase: "As a minimum for honours, a graduate should be able to understand health globally, allowing for the way travel, migration and displacement move populations."
  quote: full   # the issuer's statement is in `source` (D-std-0014)
  audience: both
  subjects: inherited
- id: qaa/health-studies-2024/4.4.b7
  locator: { number: "4.4.b7", headingPath: ["Benchmark standards", "Threshold level: Subject knowledge, understanding and skills"] }
  span: { start: 68841, end: 68996 }
  source: "understand the multidimensional and shifting nature of health to include physical, mental and social well-being, and its contemporary issues and challenges"
  stem: "4.4"
  statementType: threshold
  rung: threshold
  force: threshold
  level: fheq:6
  appliesTo: "honours graduates in the subject"
  addressee: learner
  verbs: ["understand"]
  about: "the many dimensions of health"
  themes: [none]
  domain: understanding
  award: ["bachelor's with honours"]
  gradeOf: none
  paraphrase: "As a minimum for honours, a graduate should be able to understand that health has physical, mental and social sides that shift over time, and know the challenges it faces now."
  quote: full   # the issuer's statement is in `source` (D-std-0014)
  audience: both
  subjects: inherited
- id: qaa/health-studies-2024/4.4.b8
  locator: { number: "4.4.b8", headingPath: ["Benchmark standards", "Threshold level: Subject knowledge, understanding and skills"] }
  span: { start: 68999, end: 69094 }
  source: "demonstrate understanding of a range of theories of causality relating to health and ill health"
  stem: "4.4"
  statementType: threshold
  rung: threshold
  force: threshold
  level: fheq:6
  appliesTo: "honours graduates in the subject"
  addressee: learner
  verbs: ["demonstrate"]
  about: "theories of causality in health"
  themes: [none]
  domain: knowledge
  award: ["bachelor's with honours"]
  gradeOf: none
  paraphrase: "As a minimum for honours, a graduate should be able to show understanding of several theories of what causes health and ill health."
  quote: full   # the issuer's statement is in `source` (D-std-0014)
  audience: both
  subjects: inherited
- id: qaa/health-studies-2024/4.4.b9
  locator: { number: "4.4.b9", headingPath: ["Benchmark standards", "Threshold level: Subject knowledge, understanding and skills"] }
  span: { start: 69097, end: 69188 }
  source: "describe a range of theoretical and professional rationales concerning health interventions"
  stem: "4.4"
  statementType: threshold
  rung: threshold
  force: threshold
  level: fheq:6
  appliesTo: "honours graduates in the subject"
  addressee: learner
  verbs: ["describe"]
  about: "reasons given for health interventions"
  themes: [none]
  domain: knowledge
  award: ["bachelor's with honours"]
  gradeOf: none
  paraphrase: "As a minimum for honours, a graduate should be able to set out a variety of theoretical and professional reasons offered for health interventions."
  quote: full   # the issuer's statement is in `source` (D-std-0014)
  audience: both
  subjects: inherited
- id: qaa/health-studies-2024/4.4.b10
  locator: { number: "4.4.b10", headingPath: ["Benchmark standards", "Threshold level: Subject knowledge, understanding and skills"] }
  span: { start: 69191, end: 69313 }
  source: "collate, analyse and present evidence of the role played by health promotion in the development of autonomous life choices"
  stem: "4.4"
  statementType: threshold
  rung: threshold
  force: threshold
  level: fheq:6
  appliesTo: "honours graduates in the subject"
  addressee: learner
  verbs: ["collate", "analyse", "present"]
  about: "evidence on health promotion and autonomy"
  themes: [none]
  domain: subject-skill
  award: ["bachelor's with honours"]
  gradeOf: none
  paraphrase: "As a minimum for honours, a graduate should be able to gather, analyse and report evidence on how health promotion helps people make their own life choices."
  quote: full   # the issuer's statement is in `source` (D-std-0014)
  audience: both
  subjects: inherited
- id: qaa/health-studies-2024/4.4.b11
  locator: { number: "4.4.b11", headingPath: ["Benchmark standards", "Threshold level: Subject knowledge, understanding and skills"] }
  span: { start: 69320, end: 69402 }
  source: "describe the role of the individual and of institutions in affecting health status"
  stem: "4.4"
  statementType: threshold
  rung: threshold
  force: threshold
  level: fheq:6
  appliesTo: "honours graduates in the subject"
  addressee: learner
  verbs: ["describe"]
  about: "individuals and institutions shaping health"
  themes: [none]
  domain: knowledge
  award: ["bachelor's with honours"]
  gradeOf: none
  paraphrase: "As a minimum for honours, a graduate should be able to explain how individuals and institutions each shape health status."
  quote: full   # the issuer's statement is in `source` (D-std-0014)
  audience: both
  subjects: inherited
- id: qaa/health-studies-2024/4.4.b12
  locator: { number: "4.4.b12", headingPath: ["Benchmark standards", "Threshold level: Subject knowledge, understanding and skills"] }
  span: { start: 69405, end: 69477 }
  source: "appreciate the diversity of experience and values associated with health"
  stem: "4.4"
  statementType: threshold
  rung: threshold
  force: threshold
  level: fheq:6
  appliesTo: "honours graduates in the subject"
  addressee: learner
  verbs: ["appreciate"]
  about: "varied experiences and values of health"
  themes: [none]
  domain: understanding
  award: ["bachelor's with honours"]
  gradeOf: none
  paraphrase: "As a minimum for honours, a graduate should be able to recognise that people experience and value health in many different ways."
  quote: full   # the issuer's statement is in `source` (D-std-0014)
  audience: both
  subjects: inherited
- id: qaa/health-studies-2024/4.4.b13
  locator: { number: "4.4.b13", headingPath: ["Benchmark standards", "Threshold level: Subject knowledge, understanding and skills"] }
  span: { start: 69480, end: 69572 }
  source: "compare and contrast different healthcare systems and underpinning health policy development"
  stem: "4.4"
  statementType: threshold
  rung: threshold
  force: threshold
  level: fheq:6
  appliesTo: "honours graduates in the subject"
  addressee: learner
  verbs: ["compare", "contrast"]
  about: "healthcare systems and policy"
  themes: [none]
  domain: subject-skill
  award: ["bachelor's with honours"]
  gradeOf: none
  paraphrase: "As a minimum for honours, a graduate should be able to compare different healthcare systems and the policy-making behind them."
  quote: full   # the issuer's statement is in `source` (D-std-0014)
  audience: both
  subjects: inherited
- id: qaa/health-studies-2024/4.4.b14
  locator: { number: "4.4.b14", headingPath: ["Benchmark standards", "Threshold level: Subject knowledge, understanding and skills"] }
  span: { start: 69575, end: 69654 }
  source: "demonstrate awareness of a range of theoretical arguments within Health Studies"
  stem: "4.4"
  statementType: threshold
  rung: threshold
  force: threshold
  level: fheq:6
  appliesTo: "honours graduates in the subject"
  addressee: learner
  verbs: ["demonstrate"]
  about: "theoretical debates in the subject"
  themes: [none]
  domain: knowledge
  award: ["bachelor's with honours"]
  gradeOf: none
  paraphrase: "As a minimum for honours, a graduate should be able to show they know a variety of the subject's theoretical debates."
  quote: full   # the issuer's statement is in `source` (D-std-0014)
  audience: both
  subjects: inherited
- id: qaa/health-studies-2024/4.4.b15
  locator: { number: "4.4.b15", headingPath: ["Benchmark standards", "Threshold level: Subject knowledge, understanding and skills"] }
  span: { start: 69657, end: 69804 }
  source: "demonstrate an informed understanding of ethical perspectives and the diversity of values associated with health and physical and mental well-being"
  stem: "4.4"
  statementType: threshold
  rung: threshold
  force: threshold
  level: fheq:6
  appliesTo: "honours graduates in the subject"
  addressee: learner
  verbs: ["demonstrate"]
  about: "ethics and values in health"
  themes: [none]
  domain: understanding
  award: ["bachelor's with honours"]
  gradeOf: none
  paraphrase: "As a minimum for honours, a graduate should be able to show an informed grasp of ethical viewpoints and of the many values people attach to health and to well-being of body and mind."
  quote: full   # the issuer's statement is in `source` (D-std-0014)
  audience: both
  subjects: inherited
- id: qaa/health-studies-2024/4.4.b16
  locator: { number: "4.4.b16", headingPath: ["Benchmark standards", "Threshold level: Subject knowledge, understanding and skills"] }
  span: { start: 69807, end: 69979 }
  source: "discuss health inequalities within different populations and evaluate the impact of population interventions aimed at reducing health deficits in diverse ethnic communities"
  stem: "4.4"
  statementType: threshold
  rung: threshold
  force: threshold
  level: fheq:6
  appliesTo: "honours graduates in the subject"
  addressee: learner
  verbs: ["discuss", "evaluate"]
  about: "health inequalities and population interventions"
  themes: [none]
  domain: subject-skill
  award: ["bachelor's with honours"]
  gradeOf: none
  paraphrase: "As a minimum for honours, a graduate should be able to discuss inequalities in health between populations and judge how well population-wide action narrows health gaps in diverse ethnic communities."
  quote: full   # the issuer's statement is in `source` (D-std-0014)
  audience: both
  subjects: inherited
- id: qaa/health-studies-2024/4.4.b17
  locator: { number: "4.4.b17", headingPath: ["Benchmark standards", "Threshold level: Subject knowledge, understanding and skills"] }
  span: { start: 69982, end: 70037 }
  source: "appreciate the importance of research in Health Studies"
  stem: "4.4"
  statementType: threshold
  rung: threshold
  force: threshold
  level: fheq:6
  appliesTo: "honours graduates in the subject"
  addressee: learner
  verbs: ["appreciate"]
  about: "why research matters"
  themes: [none]
  domain: understanding
  award: ["bachelor's with honours"]
  gradeOf: none
  paraphrase: "As a minimum for honours, a graduate should be able to recognise why research matters to the subject."
  quote: full   # the issuer's statement is in `source` (D-std-0014)
  audience: both
  subjects: inherited
- id: qaa/health-studies-2024/4.4.b18
  locator: { number: "4.4.b18", headingPath: ["Benchmark standards", "Threshold level: Subject knowledge, understanding and skills"] }
  span: { start: 70040, end: 70175 }
  source: "apply cross-traditional subject boundaries drawing on appropriate knowledge from other academic disciplines to reflect on health issues"
  stem: "4.4"
  statementType: threshold
  rung: threshold
  force: threshold
  level: fheq:6
  appliesTo: "honours graduates in the subject"
  addressee: learner
  verbs: ["apply", "drawing", "reflect"]
  about: "working across disciplinary lines"
  themes: [none]
  domain: subject-skill
  award: ["bachelor's with honours"]
  gradeOf: none
  paraphrase: "As a minimum for honours, a graduate should be able to cross traditional subject lines, using knowledge from other disciplines to think about health issues."
  quote: full   # the issuer's statement is in `source` (D-std-0014)
  audience: both
  subjects: inherited
- id: qaa/health-studies-2024/4.4.b19
  locator: { number: "4.4.b19", headingPath: ["Benchmark standards", "Threshold level: Subject knowledge, understanding and skills"] }
  span: { start: 70178, end: 70322 }
  source: "demonstrate use of an integrated approach to an analysis of health and health issues in diverse populations with consideration of EDI principles"
  stem: "4.4"
  statementType: threshold
  rung: threshold
  force: threshold
  level: fheq:6
  appliesTo: "honours graduates in the subject"
  addressee: learner
  verbs: ["demonstrate"]
  about: "integrated analysis with EDI principles"
  themes: [none]
  domain: subject-skill
  award: ["bachelor's with honours"]
  gradeOf: none
  paraphrase: "As a minimum for honours, a graduate should be able to analyse health issues across diverse populations in a joined-up way that takes account of equality, diversity and inclusion."
  quote: full   # the issuer's statement is in `source` (D-std-0014)
  audience: both
  subjects: inherited
- id: qaa/health-studies-2024/4.4.b20
  locator: { number: "4.4.b20", headingPath: ["Benchmark standards", "Threshold level: Subject knowledge, understanding and skills"] }
  span: { start: 70325, end: 70512 }
  source: "demonstrate an understanding of the importance of the consideration of sociological and psychological aspects in effective public health communication to enable successful health outcomes"
  stem: "4.4"
  statementType: threshold
  rung: threshold
  force: threshold
  level: fheq:6
  appliesTo: "honours graduates in the subject"
  addressee: learner
  verbs: ["demonstrate"]
  about: "social and psychological sides of public health messages"
  themes: [none]
  domain: understanding
  award: ["bachelor's with honours"]
  gradeOf: none
  paraphrase: "As a minimum for honours, a graduate should be able to show they understand why social and psychological factors decide whether public health messages succeed."
  quote: full   # the issuer's statement is in `source` (D-std-0014)
  audience: both
  subjects: inherited
- id: qaa/health-studies-2024/4.4.b21
  locator: { number: "4.4.b21", headingPath: ["Benchmark standards", "Threshold level: Subject knowledge, understanding and skills"] }
  span: { start: 70515, end: 70588 }
  source: "consider contemporary issues and discourses in health research and debate"
  stem: "4.4"
  statementType: threshold
  rung: threshold
  force: threshold
  level: fheq:6
  appliesTo: "honours graduates in the subject"
  addressee: learner
  verbs: ["consider"]
  about: "current questions in health research"
  themes: [none]
  domain: understanding
  award: ["bachelor's with honours"]
  gradeOf: none
  paraphrase: "As a minimum for honours, a graduate should be able to weigh current questions and arguments in health research and debate."
  quote: full   # the issuer's statement is in `source` (D-std-0014)
  audience: both
  subjects: inherited
- id: qaa/health-studies-2024/4.4.b22
  locator: { number: "4.4.b22", headingPath: ["Benchmark standards", "Threshold level: Subject knowledge, understanding and skills"] }
  span: { start: 70591, end: 70810 }
  source: "analyse the impact and epidemiology of communicable and non-communicable diseases and demonstrate understanding of the role of surveillance systems available regionally, nationally and globally in gathering health data."
  stem: "4.4"
  statementType: threshold
  rung: threshold
  force: threshold
  level: fheq:6
  appliesTo: "honours graduates in the subject"
  addressee: learner
  verbs: ["analyse", "demonstrate"]
  about: "epidemiology and surveillance"
  themes: [none]
  domain: subject-skill
  award: ["bachelor's with honours"]
  gradeOf: none
  paraphrase: "As a minimum for honours, a graduate should be able to analyse the epidemiology and effects of communicable and non-communicable disease and show how regional, national and global surveillance systems collect health data."
  quote: full   # the issuer's statement is in `source` (D-std-0014)
  audience: both
  subjects: inherited
- id: qaa/health-studies-2024/4.5.b1
  locator: { number: "4.5.b1", headingPath: ["Benchmark standards", "Threshold level: Generic skills"] }
  span: { start: 70916, end: 71043 }
  source: "operate effectively in a range of complex work or practice contexts which reflect the multidimensional nature of Health Studies"
  stem: "4.5"
  statementType: threshold
  rung: threshold
  force: threshold
  level: fheq:6
  appliesTo: "honours graduates in the subject"
  addressee: learner
  verbs: ["operate"]
  about: "working in complex settings"
  themes: [none]
  domain: generic-skill
  award: ["bachelor's with honours"]
  gradeOf: none
  paraphrase: "As a minimum for honours, a graduate should be able to work well in varied, complex work or practice settings that show the many sides of the subject."
  quote: full   # the issuer's statement is in `source` (D-std-0014)
  audience: both
  subjects: inherited
- id: qaa/health-studies-2024/4.5.b2
  locator: { number: "4.5.b2", headingPath: ["Benchmark standards", "Threshold level: Generic skills"] }
  span: { start: 71046, end: 71123 }
  source: "work as part of a team, taking responsibility for personal and group outcomes"
  stem: "4.5"
  statementType: threshold
  rung: threshold
  force: threshold
  level: fheq:6
  appliesTo: "honours graduates in the subject"
  addressee: learner
  verbs: ["work", "taking"]
  about: "teamwork and shared responsibility"
  themes: [none]
  domain: generic-skill
  award: ["bachelor's with honours"]
  gradeOf: none
  paraphrase: "As a minimum for honours, a graduate should be able to work in a team and accept responsibility for their own and the group's results."
  quote: full   # the issuer's statement is in `source` (D-std-0014)
  audience: both
  subjects: inherited
- id: qaa/health-studies-2024/4.5.b3
  locator: { number: "4.5.b3", headingPath: ["Benchmark standards", "Threshold level: Generic skills"] }
  span: { start: 71126, end: 71234 }
  source: "bring together information and materials from a variety of sources in representative areas of Health Studies"
  stem: "4.5"
  statementType: threshold
  rung: threshold
  force: threshold
  level: fheq:6
  appliesTo: "honours graduates in the subject"
  addressee: learner
  verbs: ["bring"]
  about: "drawing information together"
  themes: [none]
  domain: generic-skill
  award: ["bachelor's with honours"]
  gradeOf: none
  paraphrase: "As a minimum for honours, a graduate should be able to assemble information and material from several sources across typical areas of the subject."
  quote: full   # the issuer's statement is in `source` (D-std-0014)
  audience: both
  subjects: inherited
- id: qaa/health-studies-2024/4.5.b4
  locator: { number: "4.5.b4", headingPath: ["Benchmark standards", "Threshold level: Generic skills"] }
  span: { start: 71237, end: 71302 }
  source: "identify problems and propose potential solutions, where relevant"
  stem: "4.5"
  statementType: threshold
  rung: threshold
  force: threshold
  level: fheq:6
  appliesTo: "honours graduates in the subject"
  addressee: learner
  verbs: ["identify", "propose"]
  about: "problems and possible solutions"
  themes: [none]
  domain: generic-skill
  award: ["bachelor's with honours"]
  gradeOf: none
  paraphrase: "As a minimum for honours, a graduate should be able to spot problems and suggest possible solutions where that fits."
  quote: full   # the issuer's statement is in `source` (D-std-0014)
  audience: both
  subjects: inherited
- id: qaa/health-studies-2024/4.5.b5
  locator: { number: "4.5.b5", headingPath: ["Benchmark standards", "Threshold level: Generic skills"] }
  span: { start: 71305, end: 71332 }
  source: "analyse factual information"
  stem: "4.5"
  statementType: threshold
  rung: threshold
  force: threshold
  level: fheq:6
  appliesTo: "honours graduates in the subject"
  addressee: learner
  verbs: ["analyse"]
  about: "analysing facts"
  themes: [none]
  domain: generic-skill
  award: ["bachelor's with honours"]
  gradeOf: none
  paraphrase: "As a minimum for honours, a graduate should be able to analyse factual information."
  quote: full   # the issuer's statement is in `source` (D-std-0014)
  audience: both
  subjects: inherited
- id: qaa/health-studies-2024/4.5.b6
  locator: { number: "4.5.b6", headingPath: ["Benchmark standards", "Threshold level: Generic skills"] }
  span: { start: 71335, end: 71396 }
  source: "recognise strengths and weaknesses in the arguments of others"
  stem: "4.5"
  statementType: threshold
  rung: threshold
  force: threshold
  level: fheq:6
  appliesTo: "honours graduates in the subject"
  addressee: learner
  verbs: ["recognise"]
  about: "judging others' arguments"
  themes: [none]
  domain: generic-skill
  award: ["bachelor's with honours"]
  gradeOf: none
  paraphrase: "As a minimum for honours, a graduate should be able to see where other people's arguments are strong and where they are weak."
  quote: full   # the issuer's statement is in `source` (D-std-0014)
  audience: both
  subjects: inherited
- id: qaa/health-studies-2024/4.5.b7
  locator: { number: "4.5.b7", headingPath: ["Benchmark standards", "Threshold level: Generic skills"] }
  span: { start: 71399, end: 71492 }
  source: "produce a synthesis of the state of knowledge on a particular subject or topic, with guidance"
  stem: "4.5"
  statementType: threshold
  rung: threshold
  force: threshold
  level: fheq:6
  appliesTo: "honours graduates in the subject"
  addressee: learner
  verbs: ["produce"]
  about: "summing up current knowledge with guidance"
  themes: [none]
  domain: generic-skill
  award: ["bachelor's with honours"]
  gradeOf: none
  paraphrase: "As a minimum for honours, a graduate should be able to with guidance, write a synthesis of what is known on a given subject or topic."
  quote: full   # the issuer's statement is in `source` (D-std-0014)
  audience: both
  subjects: inherited
- id: qaa/health-studies-2024/4.5.b8
  locator: { number: "4.5.b8", headingPath: ["Benchmark standards", "Threshold level: Generic skills"] }
  span: { start: 71495, end: 71524 }
  source: "undertake tasks independently"
  stem: "4.5"
  statementType: threshold
  rung: threshold
  force: threshold
  level: fheq:6
  appliesTo: "honours graduates in the subject"
  addressee: learner
  verbs: ["undertake"]
  about: "working independently"
  themes: [none]
  domain: generic-skill
  award: ["bachelor's with honours"]
  gradeOf: none
  paraphrase: "As a minimum for honours, a graduate should be able to carry out tasks on their own."
  quote: full   # the issuer's statement is in `source` (D-std-0014)
  audience: both
  subjects: inherited
- id: qaa/health-studies-2024/4.5.b9
  locator: { number: "4.5.b9", headingPath: ["Benchmark standards", "Threshold level: Generic skills"] }
  span: { start: 71527, end: 71623 }
  source: "critically reflect on their own progress and act on feedback provided from multiple perspectives"
  stem: "4.5"
  statementType: threshold
  rung: threshold
  force: threshold
  level: fheq:6
  appliesTo: "honours graduates in the subject"
  addressee: learner
  verbs: ["reflect", "act"]
  about: "reflection and acting on feedback"
  themes: [none]
  domain: generic-skill
  award: ["bachelor's with honours"]
  gradeOf: none
  paraphrase: "As a minimum for honours, a graduate should be able to reflect critically on their own progress and use feedback from different sources."
  quote: full   # the issuer's statement is in `source` (D-std-0014)
  audience: both
  subjects: inherited
- id: qaa/health-studies-2024/4.5.b10
  locator: { number: "4.5.b10", headingPath: ["Benchmark standards", "Threshold level: Generic skills"] }
  span: { start: 71626, end: 71799 }
  source: "express themselves clearly using appropriate and multiple modes of communication methods, which include verbal, non-verbal and digital technologies relevant to the situation"
  stem: "4.5"
  statementType: threshold
  rung: threshold
  force: threshold
  level: fheq:6
  appliesTo: "honours graduates in the subject"
  addressee: learner
  verbs: ["express"]
  about: "clear communication in several modes"
  themes: [none]
  domain: generic-skill
  award: ["bachelor's with honours"]
  gradeOf: none
  paraphrase: "As a minimum for honours, a graduate should be able to communicate clearly in modes suited to the situation: spoken, non-verbal and digital."
  quote: full   # the issuer's statement is in `source` (D-std-0014)
  audience: both
  subjects: inherited
- id: qaa/health-studies-2024/4.5.b11
  locator: { number: "4.5.b11", headingPath: ["Benchmark standards", "Threshold level: Generic skills"] }
  span: { start: 71806, end: 72017 }
  source: "recognise the role of verbal and non-verbal communication in the effective promotion of health-related issues and the consideration of equality, diversity and inclusivity principles in all communication channels"
  stem: "4.5"
  statementType: threshold
  rung: threshold
  force: threshold
  level: fheq:6
  appliesTo: "honours graduates in the subject"
  addressee: learner
  verbs: ["recognise"]
  about: "communication for health promotion and EDI"
  themes: [none]
  domain: generic-skill
  award: ["bachelor's with honours"]
  gradeOf: none
  paraphrase: "As a minimum for honours, a graduate should be able to recognise how spoken and non-verbal communication help promote health, and apply equality, diversity and inclusion principles across every channel."
  quote: full   # the issuer's statement is in `source` (D-std-0014)
  audience: both
  subjects: inherited
- id: qaa/health-studies-2024/4.5.b12
  locator: { number: "4.5.b12", headingPath: ["Benchmark standards", "Threshold level: Generic skills"] }
  span: { start: 72020, end: 72096 }
  source: "present knowledge, or an argument, in a way that is comprehensible to others"
  stem: "4.5"
  statementType: threshold
  rung: threshold
  force: threshold
  level: fheq:6
  appliesTo: "honours graduates in the subject"
  addressee: learner
  verbs: ["present"]
  about: "making knowledge understandable"
  themes: [none]
  domain: generic-skill
  award: ["bachelor's with honours"]
  gradeOf: none
  paraphrase: "As a minimum for honours, a graduate should be able to put knowledge or an argument across so that others can follow it."
  quote: full   # the issuer's statement is in `source` (D-std-0014)
  audience: both
  subjects: inherited
- id: qaa/health-studies-2024/4.5.b13
  locator: { number: "4.5.b13", headingPath: ["Benchmark standards", "Threshold level: Generic skills"] }
  span: { start: 72099, end: 72198 }
  source: "use relevant IT to collate, analyse, select and present information, demonstrating digital literacy"
  stem: "4.5"
  statementType: threshold
  rung: threshold
  force: threshold
  level: fheq:6
  appliesTo: "honours graduates in the subject"
  addressee: learner
  verbs: ["use", "collate", "analyse", "select", "present"]
  about: "IT and digital literacy"
  themes: [none]
  domain: generic-skill
  award: ["bachelor's with honours"]
  gradeOf: none
  paraphrase: "As a minimum for honours, a graduate should be able to use suitable IT to gather, analyse, choose and present information, showing digital literacy."
  quote: full   # the issuer's statement is in `source` (D-std-0014)
  audience: both
  subjects: inherited
- id: qaa/health-studies-2024/4.5.b14
  locator: { number: "4.5.b14", headingPath: ["Benchmark standards", "Threshold level: Generic skills"] }
  span: { start: 72201, end: 72259 }
  source: "appreciate the role of AI and other technologies in health"
  stem: "4.5"
  statementType: threshold
  rung: threshold
  force: threshold
  level: fheq:6
  appliesTo: "honours graduates in the subject"
  addressee: learner
  verbs: ["appreciate"]
  about: "AI and technology in health"
  themes: [none]
  domain: generic-skill
  award: ["bachelor's with honours"]
  gradeOf: none
  paraphrase: "As a minimum for honours, a graduate should be able to recognise what AI and other technologies do in health."
  quote: full   # the issuer's statement is in `source` (D-std-0014)
  audience: both
  subjects: inherited
- id: qaa/health-studies-2024/4.5.b15
  locator: { number: "4.5.b15", headingPath: ["Benchmark standards", "Threshold level: Generic skills"] }
  span: { start: 72262, end: 72354 }
  source: "demonstrate an ability to listen and comprehend when presented with new ideas or information"
  stem: "4.5"
  statementType: threshold
  rung: threshold
  force: threshold
  level: fheq:6
  appliesTo: "honours graduates in the subject"
  addressee: learner
  verbs: ["demonstrate"]
  about: "listening and comprehension"
  themes: [none]
  domain: generic-skill
  award: ["bachelor's with honours"]
  gradeOf: none
  paraphrase: "As a minimum for honours, a graduate should be able to show they can listen to and understand new ideas or information."
  quote: full   # the issuer's statement is in `source` (D-std-0014)
  audience: both
  subjects: inherited
- id: qaa/health-studies-2024/4.5.b16
  locator: { number: "4.5.b16", headingPath: ["Benchmark standards", "Threshold level: Generic skills"] }
  span: { start: 72357, end: 72414 }
  source: "demonstrate skills in recognising and describing material"
  stem: "4.5"
  statementType: threshold
  rung: threshold
  force: threshold
  level: fheq:6
  appliesTo: "honours graduates in the subject"
  addressee: learner
  verbs: ["demonstrate"]
  about: "identifying and describing material"
  themes: [none]
  domain: generic-skill
  award: ["bachelor's with honours"]
  gradeOf: none
  paraphrase: "As a minimum for honours, a graduate should be able to show skill in identifying and describing material."
  quote: full   # the issuer's statement is in `source` (D-std-0014)
  audience: both
  subjects: inherited
- id: qaa/health-studies-2024/4.5.b17
  locator: { number: "4.5.b17", headingPath: ["Benchmark standards", "Threshold level: Generic skills"] }
  span: { start: 72417, end: 72482 }
  source: "demonstrate skills in describing, categorising and collating data"
  stem: "4.5"
  statementType: threshold
  rung: threshold
  force: threshold
  level: fheq:6
  appliesTo: "honours graduates in the subject"
  addressee: learner
  verbs: ["demonstrate"]
  about: "handling data"
  themes: [none]
  domain: generic-skill
  award: ["bachelor's with honours"]
  gradeOf: none
  paraphrase: "As a minimum for honours, a graduate should be able to show skill in describing, sorting and gathering data."
  quote: full   # the issuer's statement is in `source` (D-std-0014)
  audience: both
  subjects: inherited
- id: qaa/health-studies-2024/4.5.b18
  locator: { number: "4.5.b18", headingPath: ["Benchmark standards", "Threshold level: Generic skills"] }
  span: { start: 72485, end: 72600 }
  source: "understand the importance of health and safety and of equality, diversity and inclusiveness in the work environment"
  stem: "4.5"
  statementType: threshold
  rung: threshold
  force: threshold
  level: fheq:6
  appliesTo: "honours graduates in the subject"
  addressee: learner
  verbs: ["understand"]
  about: "health and safety and EDI at work"
  themes: [none]
  domain: generic-skill
  award: ["bachelor's with honours"]
  gradeOf: none
  paraphrase: "As a minimum for honours, a graduate should be able to understand why health and safety and equality, diversity and inclusiveness matter at work."
  quote: full   # the issuer's statement is in `source` (D-std-0014)
  audience: both
  subjects: inherited
- id: qaa/health-studies-2024/4.5.b19
  locator: { number: "4.5.b19", headingPath: ["Benchmark standards", "Threshold level: Generic skills"] }
  span: { start: 72603, end: 72700 }
  source: "appreciate and engage in contemporary debates relating to global sustainability and employability"
  stem: "4.5"
  statementType: threshold
  rung: threshold
  force: threshold
  level: fheq:6
  appliesTo: "honours graduates in the subject"
  addressee: learner
  verbs: ["appreciate", "engage"]
  about: "debates on sustainability and employability"
  themes: [none]
  domain: generic-skill
  award: ["bachelor's with honours"]
  gradeOf: none
  paraphrase: "As a minimum for honours, a graduate should be able to understand and take part in current debates on global sustainability and employability."
  quote: full   # the issuer's statement is in `source` (D-std-0014)
  audience: both
  subjects: inherited
- id: qaa/health-studies-2024/4.5.b20
  locator: { number: "4.5.b20", headingPath: ["Benchmark standards", "Threshold level: Generic skills"] }
  span: { start: 72703, end: 72801 }
  source: "apply an in-depth awareness of ethical issues and professional codes of conduct in Health Studies."
  stem: "4.5"
  statementType: threshold
  rung: threshold
  force: threshold
  level: fheq:6
  appliesTo: "honours graduates in the subject"
  addressee: learner
  verbs: ["apply"]
  about: "ethics and professional codes"
  themes: [none]
  domain: generic-skill
  award: ["bachelor's with honours"]
  gradeOf: none
  paraphrase: "As a minimum for honours, a graduate should be able to bring a thorough grasp of ethical questions and professional conduct codes to their work in the subject."
  quote: full   # the issuer's statement is in `source` (D-std-0014)
  audience: both
  subjects: inherited
- id: qaa/health-studies-2024/4.6
  locator: { number: "4.6", headingPath: ["Benchmark standards", "Benchmark standards for master's degrees"] }
  span: { start: 72847, end: 73056 }
  source: "This qualification descriptor should also be used as a reference point for other qualifications at Level 7 of the FHEQ and Level 11 on the FQHEIS, including postgraduate certificates and postgraduate diplomas."
  stem: none
  statementType: requirement
  rung: none
  force: should
  level: fheq:7
  appliesTo: "postgraduate qualifications at level 7 in the subject"
  addressee: provider
  verbs: ["used"]
  about: "master's standards as a level 7 reference point"
  themes: [none]
  domain: none
  award: ["master's", "postgraduate certificate", "postgraduate diploma"]
  gradeOf: none
  paraphrase: "These master's standards should also act as a reference point for other qualifications at FHEQ level 7 and FQHEIS level 11, such as postgraduate certificates and diplomas."
  quote: full   # the issuer's statement is in `source` (D-std-0014)
  audience: practitioner
  subjects: inherited
- id: qaa/health-studies-2024/4.7.b1
  locator: { number: "4.7.b1", headingPath: ["Benchmark standards", "Benchmark standards for master's degrees: Subject knowledge, understanding and skills"] }
  span: { start: 73233, end: 73472 }
  source: "a systematic understanding of knowledge, and a critical awareness of current health problems and/or new insights, much of which informed by, or at the forefront of, their academic discipline, field of study or area of professional practice"
  stem: "4.7"
  statementType: threshold
  rung: threshold
  force: threshold
  level: fheq:7
  appliesTo: "master's graduates in the subject"
  addressee: learner
  verbs: ["informed"]
  about: "systematic understanding and critical awareness"
  themes: [none]
  domain: knowledge
  award: ["master's"]
  gradeOf: none
  paraphrase: "As a minimum for a master's award, a graduate should be able to show a systematic grasp of the field and a critical, up-to-date sense of today's health problems and fresh insights, much of it drawn from or at the leading edge of their discipline or practice."
  quote: full   # the issuer's statement is in `source` (D-std-0014)
  audience: both
  subjects: inherited
- id: qaa/health-studies-2024/4.7.b2
  locator: { number: "4.7.b2", headingPath: ["Benchmark standards", "Benchmark standards for master's degrees: Subject knowledge, understanding and skills"] }
  span: { start: 73475, end: 73575 }
  source: "a comprehensive understanding of techniques applicable to their own research or advanced scholarship"
  stem: "4.7"
  statementType: threshold
  rung: threshold
  force: threshold
  level: fheq:7
  appliesTo: "master's graduates in the subject"
  addressee: learner
  verbs: []
  about: "research techniques"
  themes: [none]
  domain: understanding
  award: ["master's"]
  gradeOf: none
  paraphrase: "As a minimum for a master's award, a graduate should be able to show full understanding of the techniques that suit their own research or advanced study."
  quote: full   # the issuer's statement is in `source` (D-std-0014)
  audience: both
  subjects: inherited
- id: qaa/health-studies-2024/4.7.b3
  locator: { number: "4.7.b3", headingPath: ["Benchmark standards", "Benchmark standards for master's degrees: Subject knowledge, understanding and skills"] }
  span: { start: 73578, end: 73765 }
  source: "originality in the application of knowledge, together with a practical understanding of how established techniques of research are used to create and interpret knowledge in the discipline"
  stem: "4.7"
  statementType: threshold
  rung: threshold
  force: threshold
  level: fheq:7
  appliesTo: "master's graduates in the subject"
  addressee: learner
  verbs: ["used", "create", "interpret"]
  about: "originality and how research makes knowledge"
  themes: [none]
  domain: understanding
  award: ["master's"]
  gradeOf: none
  paraphrase: "As a minimum for a master's award, a graduate should be able to apply knowledge with originality and understand in practice how established research techniques produce and interpret knowledge in the discipline."
  quote: full   # the issuer's statement is in `source` (D-std-0014)
  audience: both
  subjects: inherited
- id: qaa/health-studies-2024/4.7.b4
  locator: { number: "4.7.b4", headingPath: ["Benchmark standards", "Benchmark standards for master's degrees: Subject knowledge, understanding and skills"] }
  span: { start: 73768, end: 74002 }
  source: "a conceptual understanding that enables the student to critically evaluate current research and advanced scholarship in the discipline, to evaluate methodologies, to develop critiques and, where appropriate, to propose new hypotheses."
  stem: "4.7"
  statementType: threshold
  rung: threshold
  force: threshold
  level: fheq:7
  appliesTo: "master's graduates in the subject"
  addressee: learner
  verbs: ["enables", "evaluate", "develop", "propose"]
  about: "critical evaluation of research and methods"
  themes: [none]
  domain: understanding
  award: ["master's"]
  gradeOf: none
  paraphrase: "As a minimum for a master's award, a graduate should be able to hold a conceptual understanding that lets them critique current research, advanced scholarship and methods, form critiques and, where fitting, put forward new hypotheses."
  quote: full   # the issuer's statement is in `source` (D-std-0014)
  audience: both
  subjects: inherited
- id: qaa/health-studies-2024/4.8.b1
  locator: { number: "4.8.b1", headingPath: ["Benchmark standards", "Benchmark standards for master's degrees: Generic skills"] }
  span: { start: 74126, end: 74316 }
  source: "understanding and ability to deal with complex health issues both systematically and creatively, as well as manage uncertainty and unpredictability in the dynamic landscape of Health Studies"
  stem: "4.8"
  statementType: typical
  rung: typical
  force: will
  level: fheq:7
  appliesTo: "typical holders of a master's qualification in the subject"
  addressee: learner
  verbs: ["deal", "manage"]
  about: "complex issues and uncertainty"
  themes: [none]
  domain: generic-skill
  award: ["master's"]
  gradeOf: none
  paraphrase: "A typical holder of a master's qualification will be able to show that they can handle complex health issues systematically and creatively and manage uncertainty in a changing field."
  quote: full   # the issuer's statement is in `source` (D-std-0014)
  audience: both
  subjects: inherited
- id: qaa/health-studies-2024/4.8.b2
  locator: { number: "4.8.b2", headingPath: ["Benchmark standards", "Benchmark standards for master's degrees: Generic skills"] }
  span: { start: 74323, end: 74480 }
  source: "ability to make sound judgements in the absence of complete health data, and communicate their conclusions clearly to specialist and non-specialist audiences"
  stem: "4.8"
  statementType: typical
  rung: typical
  force: will
  level: fheq:7
  appliesTo: "typical holders of a master's qualification in the subject"
  addressee: learner
  verbs: ["make", "communicate"]
  about: "judgement with incomplete data"
  themes: [none]
  domain: generic-skill
  award: ["master's"]
  gradeOf: none
  paraphrase: "A typical holder of a master's qualification will be able to show that they can make sound judgements when health data are incomplete and explain their conclusions clearly to specialists and non-specialists."
  quote: full   # the issuer's statement is in `source` (D-std-0014)
  audience: both
  subjects: inherited
- id: qaa/health-studies-2024/4.8.b3
  locator: { number: "4.8.b3", headingPath: ["Benchmark standards", "Benchmark standards for master's degrees: Generic skills"] }
  span: { start: 74483, end: 74656 }
  source: "self-direction and originality in tackling and solving problems, and the ability to act autonomously in planning and implementing tasks at a professional or equivalent level"
  stem: "4.8"
  statementType: typical
  rung: typical
  force: will
  level: fheq:7
  appliesTo: "typical holders of a master's qualification in the subject"
  addressee: learner
  verbs: ["tackling", "solving", "act", "planning", "implementing"]
  about: "self-direction and autonomy"
  themes: [none]
  domain: generic-skill
  award: ["master's"]
  gradeOf: none
  paraphrase: "A typical holder of a master's qualification will be able to show that they can direct themselves, solve problems with originality and act on their own in planning and carrying out tasks at professional level."
  quote: full   # the issuer's statement is in `source` (D-std-0014)
  audience: both
  subjects: inherited
- id: qaa/health-studies-2024/4.8.b4
  locator: { number: "4.8.b4", headingPath: ["Benchmark standards", "Benchmark standards for master's degrees: Generic skills"] }
  span: { start: 74659, end: 74767 }
  source: "continuous advancement of their knowledge and understanding, and development of new skills at a higher level"
  stem: "4.8"
  statementType: typical
  rung: typical
  force: will
  level: fheq:7
  appliesTo: "typical holders of a master's qualification in the subject"
  addressee: learner
  verbs: []
  about: "continuing to advance knowledge and skills"
  themes: [none]
  domain: generic-skill
  award: ["master's"]
  gradeOf: none
  paraphrase: "A typical holder of a master's qualification will be able to show that they can keep advancing their knowledge and understanding and build new skills to a higher level."
  quote: full   # the issuer's statement is in `source` (D-std-0014)
  audience: both
  subjects: inherited
- id: qaa/health-studies-2024/4.8.b5
  locator: { number: "4.8.b5", headingPath: ["Benchmark standards", "Benchmark standards for master's degrees: Generic skills"] }
  span: { start: 74770, end: 74901 }
  source: "initiative, personal responsibility and decision-making in complex and unpredictable situations, including in professional contexts"
  stem: "4.8"
  statementType: typical
  rung: typical
  force: will
  level: fheq:7
  appliesTo: "typical holders of a master's qualification in the subject"
  addressee: learner
  verbs: []
  about: "initiative and decisions in complex situations"
  themes: [none]
  domain: generic-skill
  award: ["master's"]
  gradeOf: none
  paraphrase: "A typical holder of a master's qualification will be able to show that they can take initiative and personal responsibility and make decisions in complex, unpredictable situations, professional ones included."
  quote: full   # the issuer's statement is in `source` (D-std-0014)
  audience: both
  subjects: inherited
- id: qaa/health-studies-2024/4.8.b6
  locator: { number: "4.8.b6", headingPath: ["Benchmark standards", "Benchmark standards for master's degrees: Generic skills"] }
  span: { start: 74904, end: 74996 }
  source: "independent learning ability required for demonstrating continuing professional development."
  stem: "4.8"
  statementType: typical
  rung: typical
  force: will
  level: fheq:7
  appliesTo: "typical holders of a master's qualification in the subject"
  addressee: learner
  verbs: ["required", "demonstrating"]
  about: "independent learning for professional development"
  themes: [none]
  domain: generic-skill
  award: ["master's"]
  gradeOf: none
  paraphrase: "A typical holder of a master's qualification will be able to show that they can learn independently in the way continuing professional development needs."
  quote: full   # the issuer's statement is in `source` (D-std-0014)
  audience: both
  subjects: inherited
```

### S4a Audience versions
<!-- label: both; status: drafted; basis: primary. forPractitioner: for the programme designer or teacher. forBeneficiary: for the student, second person, naming no issuer. author-agent-written: instructions to an AI agent writing about the statement (a course document, a handbook, an outcome, a report). author-agent-dialogue: instructions to an AI agent using the statement in conversation (with a student, a teacher or a programme team). Written fresh from the held text alone (benchmark rule 6; Abbott, 15:42). -->
```yaml
- statement: qaa/health-studies-2024/1.13
  forPractitioner: { text: "Bring students, patients and the public, voluntary services and employers into each stage of the course, from planning through to evaluation.", rewrite: light, force: will, status: drafted }
  forBeneficiary: { text: "not-applicable: a duty on the course team or provider; the student meets its effect, not a standard to reach", rewrite: full, force: will, status: drafted }
  author-agent-written: "Describe this as a duty on the course team or provider, stated with 'will': what the subject community expects to happen; it sets no outcome a student must show and carries no level. Cite it as QAA, 2024, Health Studies Subject Benchmark Statement, para 1.13. Do not present it as a statutory or regulatory requirement. Set it beside 2.19, 2.20 and 2.29."
  author-agent-dialogue: "Raise it with a programme team or reviewer when a team plans a new course or a periodic review. Frame it for staff as a check on course design or review and ask: Which stakeholders took part in the last revision, and at what stage? Do not hand it to a student as their task or quote the paragraph at length."
- statement: qaa/health-studies-2024/1.21
  forPractitioner: { text: "Design the course so each student can reach their potential and sees themselves represented and included, whatever their ethnicity, faith, gender identity, sexuality, disability or class.", rewrite: light, force: should, status: drafted }
  forBeneficiary: { text: "not-applicable: a duty on the course team or provider; the student meets its effect, not a standard to reach", rewrite: full, force: should, status: drafted }
  author-agent-written: "Describe this as a duty on the course team or provider, stated with 'should': a firm recommendation that leaves room for the provider's judgement; it sets no outcome a student must show and carries no level. Cite it as QAA, 2024, Health Studies Subject Benchmark Statement, para 1.21. Do not present it as a statutory or regulatory requirement. Set it beside 1.22, 1.23 and 2.4."
  author-agent-dialogue: "Raise it with a programme team or reviewer when a team designs or revises modules, modes of study or assessment. Frame it for staff as a check on course design or review and ask: Which students might not see themselves in this module's content or modes of study? Do not hand it to a student as their task or quote the paragraph at length."
- statement: qaa/health-studies-2024/1.23
  forPractitioner: { text: "Review at set points how the course can do more on equality, diversity and inclusion, and involve students in the review where possible.", rewrite: light, force: must, status: drafted }
  forBeneficiary: { text: "not-applicable: a duty on the course team or provider; the student meets its effect, not a standard to reach", rewrite: full, force: must, status: drafted }
  author-agent-written: "Describe this as a duty on the course team or provider, stated with 'must', the statement's firmest word; it sets no outcome a student must show and carries no level. Cite it as QAA, 2024, Health Studies Subject Benchmark Statement, para 1.23. Do not present it as a statutory or regulatory requirement. Set it beside 1.21, 2.4 and 2.28.b1."
  author-agent-dialogue: "Raise it with a programme team or reviewer when a team plans its annual review or a course change. Frame it for staff as a check on course design or review and ask: When did the team last review its EDI practice, and were students part of it? Do not hand it to a student as their task or quote the paragraph at length."
- statement: qaa/health-studies-2024/1.24
  forPractitioner: { text: "Treat regulatory accessibility requirements as the minimum and plan accessibility for each stage, from pre-application information to graduation and beyond.", rewrite: light, force: should, status: drafted }
  forBeneficiary: { text: "not-applicable: a duty on the course team or provider; the student meets its effect, not a standard to reach", rewrite: full, force: should, status: drafted }
  author-agent-written: "Describe this as a duty on the course team or provider, stated with 'should': a firm recommendation that leaves room for the provider's judgement; it sets no outcome a student must show and carries no level. Cite it as QAA, 2024, Health Studies Subject Benchmark Statement, para 1.24. Do not present it as a statutory or regulatory requirement. Set it beside 1.25, 1.26 and 3.7.b2."
  author-agent-dialogue: "Raise it with a programme team or reviewer when a team reviews accessibility from admissions information through to graduation. Frame it for staff as a check on course design or review and ask: Which stage of the course has had the least attention to accessibility? Do not hand it to a student as their task or quote the paragraph at length."
- statement: qaa/health-studies-2024/1.27
  forPractitioner: { text: "Where appropriate, weave the Sustainable Development Goals through the curriculum as a whole rather than confining them to one module.", rewrite: light, force: should, status: drafted }
  forBeneficiary: { text: "not-applicable: a duty on the course team or provider; the student meets its effect, not a standard to reach", rewrite: full, force: should, status: drafted }
  author-agent-written: "Describe this as a duty on the course team or provider, stated with 'should': a firm recommendation that leaves room for the provider's judgement; it sets no outcome a student must show and carries no level. Cite it as QAA, 2024, Health Studies Subject Benchmark Statement, para 1.27. Do not present it as a statutory or regulatory requirement. Set it beside 1.31.b1 to 1.31.b8, 2.7 and the ESD guidance (std:doc:qaa-advancehe-esd-2021-guidance)."
  author-agent-dialogue: "Raise it with a programme team or reviewer when a team maps sustainability across a course. Frame it for staff as a check on course design or review and ask: Which of the Goals does the curriculum touch, and in which modules? Do not hand it to a student as their task or quote the paragraph at length."
- statement: qaa/health-studies-2024/1.31.b1
  forPractitioner: { text: "Give students chances to see how levels and units in health relate, analyse complex systems across domains and scales and cope with uncertainty, and show where the course builds this competence.", rewrite: light, force: will, status: drafted }
  forBeneficiary: { text: "You will be able to see how the parts and levels of health systems connect, analyse complex systems and cope with uncertainty.", rewrite: full, force: will, status: drafted }
  author-agent-written: "Present this as one of the eight UNESCO sustainability competencies (2017) that the statement names as valuable for every graduate in the subject; it is an outcome without a rung, read here at honours (FHEQ level 6), which the text does not state. Cite it as QAA, 2024, Health Studies Subject Benchmark Statement, para 1.31 (item 1), crediting UNESCO for the competence. Do not present it as a threshold standard from section 4. Set it beside 1.32, 2.7, strand:thinking, qaa/fheq-2024/4.15.b4 and spine:6."
  author-agent-dialogue: "Raise it when a student or team discusses sustainability and health, or plans an ESD activity. Use plain words, second person for a student, and ask: Can you map the parts of a health system involved in one problem you studied? Avoid lecturing on the UNESCO framework and do not treat the competence as a pass condition."
- statement: qaa/health-studies-2024/1.31.b2
  forPractitioner: { text: "Give students chances to weigh possible futures, form their own visions of what is to come, use the precautionary principle, judge the effects of actions and handle risk and change, and show where the course builds this competence.", rewrite: light, force: will, status: drafted }
  forBeneficiary: { text: "You will be able to weigh up possible futures, form your own vision, act with care where effects are uncertain, judge the results of actions and handle risk and change.", rewrite: full, force: will, status: drafted }
  author-agent-written: "Present this as one of the eight UNESCO sustainability competencies (2017) that the statement names as valuable for every graduate in the subject; it is an outcome without a rung, read here at honours (FHEQ level 6), which the text does not state. Cite it as QAA, 2024, Health Studies Subject Benchmark Statement, para 1.31 (item 2), crediting UNESCO for the competence. Do not present it as a threshold standard from section 4. Set it beside 1.32, 2.7, strand:thinking, qaa/fheq-2024/4.15.b4 and spine:6."
  author-agent-dialogue: "Raise it when a student or team discusses sustainability and health, or plans an ESD activity. Use plain words, second person for a student, and ask: What future health risk in your area worries you, and what would you do about it now? Avoid lecturing on the UNESCO framework and do not treat the competence as a pass condition."
- statement: qaa/health-studies-2024/1.31.b3
  forPractitioner: { text: "Give students chances to reflect on the norms and values behind actions, work through the values of sustainable development with others and set goals where interests clash and knowledge is uncertain in health, and show where the course builds this competence.", rewrite: light, force: will, status: drafted }
  forBeneficiary: { text: "You will be able to reflect on the norms and values behind what people do, work through sustainability values with others and set goals when interests clash and knowledge is uncertain.", rewrite: full, force: will, status: drafted }
  author-agent-written: "Present this as one of the eight UNESCO sustainability competencies (2017) that the statement names as valuable for every graduate in the subject; it is an outcome without a rung, read here at honours (FHEQ level 6), which the text does not state. Cite it as QAA, 2024, Health Studies Subject Benchmark Statement, para 1.31 (item 3), crediting UNESCO for the competence. Do not present it as a threshold standard from section 4. Set it beside 1.32, 2.7, strand:thinking, qaa/fheq-2024/4.15.b7 and spine:6."
  author-agent-dialogue: "Raise it when a student or team discusses sustainability and health, or plans an ESD activity. Use plain words, second person for a student, and ask: Which values clash in a health decision you know, and how would you set a goal between them? Avoid lecturing on the UNESCO framework and do not treat the competence as a pass condition."
- statement: qaa/health-studies-2024/1.31.b4
  forPractitioner: { text: "Give students chances to devise and carry out new actions that advance sustainable development locally and beyond, and show where the course builds this competence.", rewrite: light, force: will, status: drafted }
  forBeneficiary: { text: "You will be able to plan and carry out new actions that move sustainable development forward, near home and further away.", rewrite: full, force: will, status: drafted }
  author-agent-written: "Present this as one of the eight UNESCO sustainability competencies (2017) that the statement names as valuable for every graduate in the subject; it is an outcome without a rung, read here at honours (FHEQ level 6), which the text does not state. Cite it as QAA, 2024, Health Studies Subject Benchmark Statement, para 1.31 (item 4), crediting UNESCO for the competence. Do not present it as a threshold standard from section 4. Set it beside 1.32, 2.7, strand:application, qaa/fheq-2024/4.15.b6 and spine:6."
  author-agent-dialogue: "Raise it when a student or team discusses sustainability and health, or plans an ESD activity. Use plain words, second person for a student, and ask: What practical step towards sustainability could you lead in a health setting? Avoid lecturing on the UNESCO framework and do not treat the competence as a pass condition."
- statement: qaa/health-studies-2024/1.31.b5
  forPractitioner: { text: "Give students chances to work and learn with people inside and outside their institution, respect others' needs and views, handle conflict in groups and support shared problem-solving, and show where the course builds this competence.", rewrite: light, force: will, status: drafted }
  forBeneficiary: { text: "You will be able to work and learn with people inside and outside your institution, respect their needs and views, handle conflict in a group and help others solve problems together.", rewrite: full, force: will, status: drafted }
  author-agent-written: "Present this as one of the eight UNESCO sustainability competencies (2017) that the statement names as valuable for every graduate in the subject; it is an outcome without a rung, read here at honours (FHEQ level 6), which the text does not state. Cite it as QAA, 2024, Health Studies Subject Benchmark Statement, para 1.31 (item 5), crediting UNESCO for the competence. Do not present it as a threshold standard from section 4. Set it beside 1.32, 2.7, strand:communication, qaa/fheq-2024/4.15.b9.1 and spine:6."
  author-agent-dialogue: "Raise it when a student or team discusses sustainability and health, or plans an ESD activity. Use plain words, second person for a student, and ask: How did your last group handle disagreement, and what part did you play? Avoid lecturing on the UNESCO framework and do not treat the competence as a pass condition."
- statement: qaa/health-studies-2024/1.31.b6
  forPractitioner: { text: "Give students chances to question accepted norms, practices and opinions, examine their own values and actions and take a stance in the debate on sustainable development, and show where the course builds this competence.", rewrite: light, force: will, status: drafted }
  forBeneficiary: { text: "You will be able to question accepted ideas and practices, look hard at your own values and take a position in debates about sustainable development.", rewrite: full, force: will, status: drafted }
  author-agent-written: "Present this as one of the eight UNESCO sustainability competencies (2017) that the statement names as valuable for every graduate in the subject; it is an outcome without a rung, read here at honours (FHEQ level 6), which the text does not state. Cite it as QAA, 2024, Health Studies Subject Benchmark Statement, para 1.31 (item 6), crediting UNESCO for the competence. Do not present it as a threshold standard from section 4. Set it beside 1.32, 2.7, strand:thinking, qaa/fheq-2024/4.15.b7 and spine:6."
  author-agent-dialogue: "Raise it when a student or team discusses sustainability and health, or plans an ESD activity. Use plain words, second person for a student, and ask: Where do you stand on one sustainability debate in health, and what shaped your view? Avoid lecturing on the UNESCO framework and do not treat the competence as a pass condition."
- statement: qaa/health-studies-2024/1.31.b7
  forPractitioner: { text: "Give students chances to reflect on their own values, perceptions, actions, feelings and desires, consider their part in local and global society and keep judging and driving their own actions, and show where the course builds this competence.", rewrite: light, force: will, status: drafted }
  forBeneficiary: { text: "You will be able to reflect on your values, actions and feelings, think about your part in your community and the wider world and keep checking and driving your own actions.", rewrite: full, force: will, status: drafted }
  author-agent-written: "Present this as one of the eight UNESCO sustainability competencies (2017) that the statement names as valuable for every graduate in the subject; it is an outcome without a rung, read here at honours (FHEQ level 6), which the text does not state. Cite it as QAA, 2024, Health Studies Subject Benchmark Statement, para 1.31 (item 7), crediting UNESCO for the competence. Do not present it as a threshold standard from section 4. Set it beside 1.32, 2.7, strand:autonomy, qaa/fheq-2024/4.15.b9.3 and spine:6."
  author-agent-dialogue: "Raise it when a student or team discusses sustainability and health, or plans an ESD activity. Use plain words, second person for a student, and ask: What part do you want to play in your community's health, and what keeps you going? Avoid lecturing on the UNESCO framework and do not treat the competence as a pass condition."
- statement: qaa/health-studies-2024/1.31.b8
  forPractitioner: { text: "Give students chances to use several problem-solving frameworks on complex sustainability problems in health, devise workable, inclusive and fair solutions and draw on the right competences to resolve them, and show where the course builds this competence.", rewrite: light, force: will, status: drafted }
  forBeneficiary: { text: "You will be able to use different problem-solving approaches on complex sustainability problems in health and work out solutions that are workable, inclusive and fair.", rewrite: full, force: will, status: drafted }
  author-agent-written: "Present this as one of the eight UNESCO sustainability competencies (2017) that the statement names as valuable for every graduate in the subject; it is an outcome without a rung, read here at honours (FHEQ level 6), which the text does not state. Cite it as QAA, 2024, Health Studies Subject Benchmark Statement, para 1.31 (item 8), crediting UNESCO for the competence. Do not present it as a threshold standard from section 4. Set it beside 1.32, 2.7, strand:application, qaa/fheq-2024/4.15.b3.1 and spine:6."
  author-agent-dialogue: "Raise it when a student or team discusses sustainability and health, or plans an ESD activity. Use plain words, second person for a student, and ask: Which framework did you use on your last complex problem, and was the result fair to everyone affected? Avoid lecturing on the UNESCO framework and do not treat the competence as a pass condition."
- statement: qaa/health-studies-2024/1.32
  forPractitioner: { text: "Build the eight sustainability competencies into the curriculum and learning resources and make them visible there.", rewrite: light, force: must, status: drafted }
  forBeneficiary: { text: "not-applicable: a duty on the course team or provider; the student meets its effect, not a standard to reach", rewrite: full, force: must, status: drafted }
  author-agent-written: "Describe this as a duty on the course team or provider, stated with 'must', the statement's firmest word; it sets no outcome a student must show and carries no level. Cite it as QAA, 2024, Health Studies Subject Benchmark Statement, para 1.32. Do not present it as a statutory or regulatory requirement; the text says 'requires', which this record reads as must (Part E). Set it beside 1.31.b1 to 1.31.b8 and 2.7."
  author-agent-dialogue: "Raise it with a programme team or reviewer when a team audits its curriculum for sustainability. Frame it for staff as a check on course design or review and ask: Where in the curriculum does each of the eight competencies appear? Do not hand it to a student as their task or quote the paragraph at length."
- statement: qaa/health-studies-2024/1.33
  forPractitioner: { text: "Provide facilities for study and experiential training that suit self-directed adult learners, across digital, individual, group and community settings.", rewrite: light, force: must, status: drafted }
  forBeneficiary: { text: "not-applicable: a duty on the course team or provider; the student meets its effect, not a standard to reach", rewrite: full, force: must, status: drafted }
  author-agent-written: "Describe this as a duty on the course team or provider, stated with 'must', the statement's firmest word; it sets no outcome a student must show and carries no level. Cite it as QAA, 2024, Health Studies Subject Benchmark Statement, para 1.33. Do not present it as a statutory or regulatory requirement; the text says 'requires', which this record reads as must (Part E). Set it beside 1.34 and 2.16."
  author-agent-dialogue: "Raise it with a programme team or reviewer when a team plans learning spaces, placements or online resources. Frame it for staff as a check on course design or review and ask: Do the facilities serve learners who direct their own study, on and off campus? Do not hand it to a student as their task or quote the paragraph at length."
- statement: qaa/health-studies-2024/1.37
  forPractitioner: { text: "Help students learn what their skills are worth commercially and in practice, rehearse presenting them to employers and in self-employment plans and reflect on their enterprising strengths in the health sector.", rewrite: light, force: should, status: drafted }
  forBeneficiary: { text: "You should understand what your skills are worth, commercially and in practice, and be able to explain and show them to employers or in a plan to work for yourself; you should also be helped to recognise your own enterprising strengths in health.", rewrite: full, force: should, status: drafted }
  author-agent-written: "Present this as a 'should' expectation of students, set in the enterprise and entrepreneurship section; it is a generic skill read at honours (FHEQ level 6), a level the paragraph does not state. Cite it as QAA, 2024, Health Studies Subject Benchmark Statement, para 1.37. Do not present it as a threshold standard, since the section 4 lists hold the threshold. Set it beside 1.38, 4.5.b19, qaa/fheq-2024/4.15.b9.1 and spine:6."
  author-agent-dialogue: "Raise it when a student talks about careers, placements or self-employment, or when a team plans employability teaching. Ask a student which of their skills an employer would pay for and how they would prove it; ask staff where students practise presenting their skills. Do not treat it as a pass requirement or read the paragraph aloud."
- statement: qaa/health-studies-2024/1.43
  forPractitioner: { text: "Include the ethical use of digital technology for creative, original and accessible communication in the course's work on digital and transferable skills.", rewrite: light, force: should, status: drafted }
  forBeneficiary: { text: "Your course should help you use digital technology ethically to share ideas in creative, original and accessible ways, for your studies and your career.", rewrite: full, force: should, status: drafted }
  author-agent-written: "Present this as a 'should' on how the course builds digital and transferable skills, read for honours and master's alike; it names no level. Cite it as QAA, 2024, Health Studies Subject Benchmark Statement, para 1.43. Do not present it as a standalone threshold outcome or a regulatory duty. Set it beside 4.5.b13, 4.5.b14 and qaa/fheq-2024/4.15.b8."
  author-agent-dialogue: "Raise it when a team plans digital skills teaching or a student asks how to present work online responsibly. With staff, ask where students practise ethical, accessible digital communication; with a student, ask which digital format they would choose for a health message and how they would make it accessible. Do not read the paragraph aloud or treat it as a pass condition."
- statement: qaa/health-studies-2024/2.1
  forPractitioner: { text: "Think through how the course combines its disciplines; 1.16 lists those the subject draws on.", rewrite: light, force: should, status: drafted }
  forBeneficiary: { text: "not-applicable: a duty on the course team or provider; the student meets its effect, not a standard to reach", rewrite: full, force: should, status: drafted }
  author-agent-written: "Describe this as a duty on the course team or provider, stated with 'should': a firm recommendation that leaves room for the provider's judgement; it sets no outcome a student must show and carries no level. Cite it as QAA, 2024, Health Studies Subject Benchmark Statement, para 2.1. Do not present it as a statutory or regulatory requirement. Set it beside 1.16, 2.2 and 2.13."
  author-agent-dialogue: "Raise it with a programme team or reviewer when a team designs a new course or a joint award. Frame it for staff as a check on course design or review and ask: Which disciplines does the course draw on, and how are they joined rather than set side by side? Do not hand it to a student as their task or quote the paragraph at length."
- statement: qaa/health-studies-2024/2.3
  forPractitioner: { text: "Ground the design in the national qualifications frameworks and sector-recognised standards and use them to show stakeholders and service users what the award stands for.", rewrite: light, force: will, status: drafted }
  forBeneficiary: { text: "not-applicable: a duty on the course team or provider; the student meets its effect, not a standard to reach", rewrite: full, force: will, status: drafted }
  author-agent-written: "Describe this as a duty on the course team or provider, stated with 'will': what the subject community expects to happen; it sets no outcome a student must show and carries no level. Cite it as QAA, 2024, Health Studies Subject Benchmark Statement, para 2.3. Do not present it as a statutory or regulatory requirement. Set it beside 4.3, 4.6 and the FHEQ (std:doc:qaa-fheq-2024-framework, S5)."
  author-agent-dialogue: "Raise it with a programme team or reviewer when a team writes a programme specification or maps outcomes to levels. Frame it for staff as a check on course design or review and ask: Which framework level descriptor does each exit award map to? Do not hand it to a student as their task or quote the paragraph at length."
- statement: qaa/health-studies-2024/2.4
  forPractitioner: { text: "Build the EDI dimensions set out in section 1 into all parts of the student experience so every student has an equal chance to take part and finish.", rewrite: light, force: should, status: drafted }
  forBeneficiary: { text: "not-applicable: a duty on the course team or provider; the student meets its effect, not a standard to reach", rewrite: full, force: should, status: drafted }
  author-agent-written: "Describe this as a duty on the course team or provider, stated with 'should': a firm recommendation that leaves room for the provider's judgement; it sets no outcome a student must show and carries no level. Cite it as QAA, 2024, Health Studies Subject Benchmark Statement, para 2.4. Do not present it as a statutory or regulatory requirement. Set it beside 1.21, 1.22 and 1.23."
  author-agent-dialogue: "Raise it with a programme team or reviewer when a team reviews the student experience for equal opportunity. Frame it for staff as a check on course design or review and ask: Where do students disengage or leave early, and does it differ between groups? Do not hand it to a student as their task or quote the paragraph at length."
- statement: qaa/health-studies-2024/2.5
  forPractitioner: { text: "Give students the chance to learn what patients from varied social, cultural and ethnic backgrounds need; decolonising the curriculum is one route the paragraph offers.", rewrite: light, force: should, status: drafted }
  forBeneficiary: { text: "not-applicable: a duty on the course to give the opportunity; the student meets its effect", rewrite: full, force: should, status: drafted }
  author-agent-written: "Describe this as a duty on the course team or provider, stated with 'should': a firm recommendation that leaves room for the provider's judgement; it sets no outcome a student must show and carries no level. Cite it as QAA, 2024, Health Studies Subject Benchmark Statement, para 2.5. Do not present it as a statutory or regulatory requirement. Set it beside 2.4, 2.6 and the GMC's Promoting Excellence (2015; not yet ingested)."
  author-agent-dialogue: "Raise it with a programme team or reviewer when a team plans content on patient diversity or on decolonising the curriculum. Frame it for staff as a check on course design or review and ask: Where do students meet the needs of patients from backgrounds unlike their own? Do not hand it to a student as their task or quote the paragraph at length."
- statement: qaa/health-studies-2024/2.10
  forPractitioner: { text: "Plan each level so that knowledge, understanding, skills, behaviours and values build towards the section 4 threshold, with depth, challenge and autonomy rising from one level to the next, and credit for all components, practical ones too.", rewrite: light, force: will, status: drafted }
  forBeneficiary: { text: "You will start with the basics of the subject and take on more depth, challenge and independence at each level, building towards the minimum skills you need to graduate.", rewrite: full, force: will, status: drafted }
  author-agent-written: "Present this as an expectation ('will') about how students progress through an honours degree, with the honours level stated as FHEQ level 6 and FQHEIS level 10. Cite it as QAA, 2024, Health Studies Subject Benchmark Statement, para 2.10. Do not treat it as an outcome in itself or as a rule on credit; the outcomes are in 4.4 and 4.5. Set it beside 2.11, 4.3, the level descriptors qaa/fheq-2024/4.10, 4.12 and 4.15, and spine:4 to spine:6."
  author-agent-dialogue: "Raise it when a student asks how the levels of the degree differ, or when a team plans the step up between years. With a student, explain in plain words that each year asks for more depth and independence, and ask what they now do on their own that they could not do last year. Do not read out the paragraph or suggest that the final threshold applies in the first year."
- statement: qaa/health-studies-2024/2.11
  forPractitioner: { text: "Plan for a gradual shift from tightly structured, directed study in the first year to students managing and owning their learning by the end.", rewrite: light, force: will, status: drafted }
  forBeneficiary: { text: "You will move gradually from closely guided study, which helps you settle in, to managing and taking charge of your own learning.", rewrite: full, force: will, status: drafted }
  author-agent-written: "Present this as an expectation ('will') about the shift towards autonomous learning over the degree; it names no level. Cite it as QAA, 2024, Health Studies Subject Benchmark Statement, para 2.11. Do not present it as a threshold outcome. Set it beside 2.10, 2.11.b1 to 2.11.b4, 4.5.b8 and qaa/fheq-2024/4.15.b5."
  author-agent-dialogue: "Raise it when a student finds the change to independent study hard, or when a team plans transition support. In plain words, ask a student which parts of their learning they now plan for themselves and where they still need structure. Do not imply that needing support early on is a failing."
- statement: qaa/health-studies-2024/2.11.b1
  forPractitioner: { text: "Make progression strategies allow for students' different prior experience and for the challenges of transition.", rewrite: light, force: should, status: drafted }
  forBeneficiary: { text: "not-applicable: a duty on the course team or provider; the student meets its effect, not a standard to reach", rewrite: full, force: should, status: drafted }
  author-agent-written: "Describe this as a duty on the course team or provider, stated with 'should': a firm recommendation that leaves room for the provider's judgement; it sets no outcome a student must show and carries no level. Cite it as QAA, 2024, Health Studies Subject Benchmark Statement, para 2.11 (item 1). Do not present it as a statutory or regulatory requirement. Set it beside 2.10, 2.11 and the level descriptors qaa/fheq-2024/4.10, 4.12 and 4.15."
  author-agent-dialogue: "Raise it with a programme team or reviewer when a team plans progression and transition support. Frame it for staff as a check on course design or review and ask: How does the course find out what experience each student brings? Do not hand it to a student as their task or quote the paragraph at length."
- statement: qaa/health-studies-2024/2.11.b2
  forPractitioner: { text: "Check that progression support lets every student reach their potential, whatever their background or motive for study.", rewrite: light, force: should, status: drafted }
  forBeneficiary: { text: "not-applicable: a duty on the course team or provider; the student meets its effect, not a standard to reach", rewrite: full, force: should, status: drafted }
  author-agent-written: "Describe this as a duty on the course team or provider, stated with 'should': a firm recommendation that leaves room for the provider's judgement; it sets no outcome a student must show and carries no level. Cite it as QAA, 2024, Health Studies Subject Benchmark Statement, para 2.11 (item 2). Do not present it as a statutory or regulatory requirement. Set it beside 2.10, 2.11 and the level descriptors qaa/fheq-2024/4.10, 4.12 and 4.15."
  author-agent-dialogue: "Raise it with a programme team or reviewer when a team plans progression and transition support. Frame it for staff as a check on course design or review and ask: Do progression rates differ by background, and what is the course doing about it? Do not hand it to a student as their task or quote the paragraph at length."
- statement: qaa/health-studies-2024/2.11.b3
  forPractitioner: { text: "Support academic and personal development alongside subject learning, for example through tutoring and skills provision.", rewrite: light, force: should, status: drafted }
  forBeneficiary: { text: "not-applicable: a duty on the course team or provider; the student meets its effect, not a standard to reach", rewrite: full, force: should, status: drafted }
  author-agent-written: "Describe this as a duty on the course team or provider, stated with 'should': a firm recommendation that leaves room for the provider's judgement; it sets no outcome a student must show and carries no level. Cite it as QAA, 2024, Health Studies Subject Benchmark Statement, para 2.11 (item 3). Do not present it as a statutory or regulatory requirement. Set it beside 2.10, 2.11 and the level descriptors qaa/fheq-2024/4.10, 4.12 and 4.15."
  author-agent-dialogue: "Raise it with a programme team or reviewer when a team plans progression and transition support. Frame it for staff as a check on course design or review and ask: Where does the course support personal development, not only subject learning? Do not hand it to a student as their task or quote the paragraph at length."
- statement: qaa/health-studies-2024/2.11.b4
  forPractitioner: { text: "Align progression strategies with the learning outcomes or competences set for each level.", rewrite: light, force: should, status: drafted }
  forBeneficiary: { text: "not-applicable: a duty on the course team or provider; the student meets its effect, not a standard to reach", rewrite: full, force: should, status: drafted }
  author-agent-written: "Describe this as a duty on the course team or provider, stated with 'should': a firm recommendation that leaves room for the provider's judgement; it sets no outcome a student must show and carries no level. Cite it as QAA, 2024, Health Studies Subject Benchmark Statement, para 2.11 (item 4). Do not present it as a statutory or regulatory requirement. Set it beside 2.10, 2.11 and the level descriptors qaa/fheq-2024/4.10, 4.12 and 4.15."
  author-agent-dialogue: "Raise it with a programme team or reviewer when a team plans progression and transition support. Frame it for staff as a check on course design or review and ask: Which outcomes does the progression support at each level aim at? Do not hand it to a student as their task or quote the paragraph at length."
- statement: qaa/health-studies-2024/2.13
  forPractitioner: { text: "In joint and combined awards, make sure students reach the core subject-specific and generic skills here, and let the other subject add its own.", rewrite: light, force: will, status: drafted }
  forBeneficiary: { text: "If you study health as part of a joint or combined degree, you will reach the core subject and general skills described here and add others from your other subject.", rewrite: full, force: will, status: drafted }
  author-agent-written: "Present this as an expectation ('will') for honours students on joint or combined degrees at FHEQ level 6: they reach the core of 4.4 and 4.5, not every item. Cite it as QAA, 2024, Health Studies Subject Benchmark Statement, para 2.13. Do not claim that joint students meet the full lists, or that the paragraph defines which items are core. Set it beside 2.1, 4.4, 4.5 and qaa/fheq-2024/4.15."
  author-agent-dialogue: "Raise it when a joint-honours student asks what they must cover in health, or when two departments plan a combined award. Ask a student which health skills they have built so far and what their other subject adds. Do not tell a joint student they must meet every item of the single-honours lists."
- statement: qaa/health-studies-2024/2.16
  forPractitioner: { text: "Offer a varied range of delivery methods chosen to suit students, the content and its assessment.", rewrite: light, force: will, status: drafted }
  forBeneficiary: { text: "not-applicable: a duty on the course team or provider; the student meets its effect, not a standard to reach", rewrite: full, force: will, status: drafted }
  author-agent-written: "Describe this as a duty on the course team or provider, stated with 'will': what the subject community expects to happen; it sets no outcome a student must show and carries no level. Cite it as QAA, 2024, Health Studies Subject Benchmark Statement, para 2.16. Do not present it as a statutory or regulatory requirement. Set it beside 2.17, 3.3 and 3.5."
  author-agent-dialogue: "Raise it with a programme team or reviewer when a team chooses delivery modes or reviews flexibility. Frame it for staff as a check on course design or review and ask: Does the mix of delivery modes suit the students actually enrolled? Do not hand it to a student as their task or quote the paragraph at length."
- statement: qaa/health-studies-2024/2.18
  forPractitioner: { text: "Keep design and review flexible so the team can respond to students, industry and society and to changes from governing or accrediting bodies.", rewrite: light, force: will, status: drafted }
  forBeneficiary: { text: "not-applicable: a duty on the course team or provider; the student meets its effect, not a standard to reach", rewrite: full, force: will, status: drafted }
  author-agent-written: "Describe this as a duty on the course team or provider, stated with 'will': what the subject community expects to happen; it sets no outcome a student must show and carries no level. Cite it as QAA, 2024, Health Studies Subject Benchmark Statement, para 2.18. Do not present it as a statutory or regulatory requirement. Set it beside 2.16, 2.20 and 2.26."
  author-agent-dialogue: "Raise it with a programme team or reviewer when a course faces an accrediting body or new industry needs. Frame it for staff as a check on course design or review and ask: Can the course change quickly enough when an accrediting body changes its requirements? Do not hand it to a student as their task or quote the paragraph at length."
- statement: qaa/health-studies-2024/2.19
  forPractitioner: { text: "Engage relevant stakeholders as partners across the life of the course, at a depth of partnership that suits the context, from consultation to co-delivery.", rewrite: light, force: will, status: drafted }
  forBeneficiary: { text: "not-applicable: a duty on the course team or provider; the student meets its effect, not a standard to reach", rewrite: full, force: will, status: drafted }
  author-agent-written: "Describe this as a duty on the course team or provider, stated with 'will': what the subject community expects to happen; it sets no outcome a student must show and carries no level. Cite it as QAA, 2024, Health Studies Subject Benchmark Statement, para 2.19. Do not present it as a statutory or regulatory requirement. Set it beside 1.13, 2.20 and 2.29."
  author-agent-dialogue: "Raise it with a programme team or reviewer when a team sets up partnership with employers, service users or students. Frame it for staff as a check on course design or review and ask: At what depth are stakeholders involved now: consulted, co-creating or co-delivering? Do not hand it to a student as their task or quote the paragraph at length."
- statement: qaa/health-studies-2024/2.20
  forPractitioner: { text: "Where a regulatory body is relevant, write the course in line with its requirements.", rewrite: light, force: should, status: drafted }
  forBeneficiary: { text: "not-applicable: a duty on the course team or provider; the student meets its effect, not a standard to reach", rewrite: full, force: should, status: drafted }
  author-agent-written: "Describe this as a duty on the course team or provider, stated with 'should': a firm recommendation that leaves room for the provider's judgement; it sets no outcome a student must show and carries no level. Cite it as QAA, 2024, Health Studies Subject Benchmark Statement, para 2.20. Do not present it as a statutory or regulatory requirement. Set it beside 2.18, 2.26 and 3.10.b6."
  author-agent-dialogue: "Raise it with a programme team or reviewer when a course leads to a regulated or professional role. Frame it for staff as a check on course design or review and ask: Which regulatory body, if any, does this course need to align with? Do not hand it to a student as their task or quote the paragraph at length."
- statement: qaa/health-studies-2024/2.22
  forPractitioner: { text: "Agree with employers how apprentices are supported to reach professional or occupational competence and who coordinates that support.", rewrite: light, force: will, status: drafted }
  forBeneficiary: { text: "not-applicable: a duty on the course team or provider; the student meets its effect, not a standard to reach", rewrite: full, force: will, status: drafted }
  author-agent-written: "Describe this as a duty on the course team or provider, stated with 'will': what the subject community expects to happen; it sets no outcome a student must show and carries no level. Cite it as QAA, 2024, Health Studies Subject Benchmark Statement, para 2.22. Do not present it as a statutory or regulatory requirement. Set it beside 3.11 and QAA's Higher Education Apprenticeships Characteristics Statement (not yet ingested)."
  author-agent-dialogue: "Raise it with a programme team or reviewer when a team designs or reviews an apprenticeship degree. Frame it for staff as a check on course design or review and ask: Who coordinates support for each apprentice between employer and university? Do not hand it to a student as their task or quote the paragraph at length."
- statement: qaa/health-studies-2024/2.23
  forPractitioner: { text: "Include the student voice in routine monitoring and in periodic course review.", rewrite: light, force: will, status: drafted }
  forBeneficiary: { text: "not-applicable: a duty on the course team or provider; the student meets its effect, not a standard to reach", rewrite: full, force: will, status: drafted }
  author-agent-written: "Describe this as a duty on the course team or provider, stated with 'will': what the subject community expects to happen; it sets no outcome a student must show and carries no level. Cite it as QAA, 2024, Health Studies Subject Benchmark Statement, para 2.23. Do not present it as a statutory or regulatory requirement. Set it beside 2.20, 2.27 and 2.29."
  author-agent-dialogue: "Raise it with a programme team or reviewer when a team plans periodic review. Frame it for staff as a check on course design or review and ask: How does student feedback reach the review, and what changed because of it? Do not hand it to a student as their task or quote the paragraph at length."
- statement: qaa/health-studies-2024/2.24
  forPractitioner: { text: "Use external reviewers in periodic review to test proposed changes, confirm the threshold standards are met and check the content fits the subject.", rewrite: light, force: will, status: drafted }
  forBeneficiary: { text: "not-applicable: a duty on the course team or provider; the student meets its effect, not a standard to reach", rewrite: full, force: will, status: drafted }
  author-agent-written: "Describe this as a duty on the course team or provider, stated with 'will': what the subject community expects to happen; it sets no outcome a student must show and carries no level. Cite it as QAA, 2024, Health Studies Subject Benchmark Statement, para 2.24. Do not present it as a statutory or regulatory requirement. Set it beside 2.25, 2.27 and 4.3."
  author-agent-dialogue: "Raise it with a programme team or reviewer when a team prepares for periodic review. Frame it for staff as a check on course design or review and ask: Who is the external reviewer, and what will they check against the threshold standards? Do not hand it to a student as their task or quote the paragraph at length."
- statement: qaa/health-studies-2024/2.27
  forPractitioner: { text: "Name the external reference points the review uses, this statement among them, and check provision against health sector norms.", rewrite: light, force: will, status: drafted }
  forBeneficiary: { text: "not-applicable: a duty on the course team or provider; the student meets its effect, not a standard to reach", rewrite: full, force: will, status: drafted }
  author-agent-written: "Describe this as a duty on the course team or provider, stated with 'will': what the subject community expects to happen; it sets no outcome a student must show and carries no level. Cite it as QAA, 2024, Health Studies Subject Benchmark Statement, para 2.27. Do not present it as a statutory or regulatory requirement. Set it beside 2.23, 2.24 and 2.28.b1 to 2.28.b10."
  author-agent-dialogue: "Raise it with a programme team or reviewer when a team chooses the reference points for review. Frame it for staff as a check on course design or review and ask: Which external reference points does the review use besides this statement? Do not hand it to a student as their task or quote the paragraph at length."
- statement: qaa/health-studies-2024/2.28.b1
  forPractitioner: { text: "Use review to compare what the curriculum intends, what is delivered and what students achieve, with inclusion in view.", rewrite: light, force: will, status: drafted }
  forBeneficiary: { text: "not-applicable: a duty on the course team or provider; the student meets its effect, not a standard to reach", rewrite: full, force: will, status: drafted }
  author-agent-written: "Describe this as a duty on the course team or provider, stated with 'will': what the subject community expects to happen; it sets no outcome a student must show and carries no level. Cite it as QAA, 2024, Health Studies Subject Benchmark Statement, para 2.28 (item 1). Do not present it as a statutory or regulatory requirement. Set it beside 2.27, 2.29 and 2.24."
  author-agent-dialogue: "Raise it with a programme team or reviewer when a team plans or audits its monitoring and review cycle. Frame it for staff as a check on course design or review and ask: Where do the planned and the achieved curriculum part company, and for whom? Do not hand it to a student as their task or quote the paragraph at length."
- statement: qaa/health-studies-2024/2.28.b2
  forPractitioner: { text: "Feed stakeholder feedback into the curriculum through each review cycle.", rewrite: light, force: will, status: drafted }
  forBeneficiary: { text: "not-applicable: a duty on the course team or provider; the student meets its effect, not a standard to reach", rewrite: full, force: will, status: drafted }
  author-agent-written: "Describe this as a duty on the course team or provider, stated with 'will': what the subject community expects to happen; it sets no outcome a student must show and carries no level. Cite it as QAA, 2024, Health Studies Subject Benchmark Statement, para 2.28 (item 2). Do not present it as a statutory or regulatory requirement. Set it beside 2.27, 2.29 and 2.24."
  author-agent-dialogue: "Raise it with a programme team or reviewer when a team plans or audits its monitoring and review cycle. Frame it for staff as a check on course design or review and ask: What did the last cycle change in response to stakeholders? Do not hand it to a student as their task or quote the paragraph at length."
- statement: qaa/health-studies-2024/2.28.b3
  forPractitioner: { text: "Check through review that institutional goals and sector good practice reach every part of the curriculum.", rewrite: light, force: will, status: drafted }
  forBeneficiary: { text: "not-applicable: a duty on the course team or provider; the student meets its effect, not a standard to reach", rewrite: full, force: will, status: drafted }
  author-agent-written: "Describe this as a duty on the course team or provider, stated with 'will': what the subject community expects to happen; it sets no outcome a student must show and carries no level. Cite it as QAA, 2024, Health Studies Subject Benchmark Statement, para 2.28 (item 3). Do not present it as a statutory or regulatory requirement. Set it beside 2.27, 2.29 and 2.24."
  author-agent-dialogue: "Raise it with a programme team or reviewer when a team plans or audits its monitoring and review cycle. Frame it for staff as a check on course design or review and ask: Which institutional goal is least visible in the curriculum? Do not hand it to a student as their task or quote the paragraph at length."
- statement: qaa/health-studies-2024/2.28.b4
  forPractitioner: { text: "Use review to confirm that academic standards meet the relevant national qualifications framework.", rewrite: light, force: will, status: drafted }
  forBeneficiary: { text: "not-applicable: a duty on the course team or provider; the student meets its effect, not a standard to reach", rewrite: full, force: will, status: drafted }
  author-agent-written: "Describe this as a duty on the course team or provider, stated with 'will': what the subject community expects to happen; it sets no outcome a student must show and carries no level. Cite it as QAA, 2024, Health Studies Subject Benchmark Statement, para 2.28 (item 4). Do not present it as a statutory or regulatory requirement. Set it beside 2.27, 2.29 and 2.24."
  author-agent-dialogue: "Raise it with a programme team or reviewer when a team plans or audits its monitoring and review cycle. Frame it for staff as a check on course design or review and ask: How does the review confirm each award meets its framework level? Do not hand it to a student as their task or quote the paragraph at length."
- statement: qaa/health-studies-2024/2.28.b5
  forPractitioner: { text: "Run internal and external moderation as part of monitoring and review.", rewrite: light, force: will, status: drafted }
  forBeneficiary: { text: "not-applicable: a duty on the course team or provider; the student meets its effect, not a standard to reach", rewrite: full, force: will, status: drafted }
  author-agent-written: "Describe this as a duty on the course team or provider, stated with 'will': what the subject community expects to happen; it sets no outcome a student must show and carries no level. Cite it as QAA, 2024, Health Studies Subject Benchmark Statement, para 2.28 (item 5). Do not present it as a statutory or regulatory requirement. Set it beside 2.27, 2.29 and 2.24."
  author-agent-dialogue: "Raise it with a programme team or reviewer when a team plans or audits its monitoring and review cycle. Frame it for staff as a check on course design or review and ask: How are marks moderated, and what did the last external moderation find? Do not hand it to a student as their task or quote the paragraph at length."
- statement: qaa/health-studies-2024/2.28.b6
  forPractitioner: { text: "Link course monitoring to the institution's internal review process.", rewrite: light, force: will, status: drafted }
  forBeneficiary: { text: "not-applicable: a duty on the course team or provider; the student meets its effect, not a standard to reach", rewrite: full, force: will, status: drafted }
  author-agent-written: "Describe this as a duty on the course team or provider, stated with 'will': what the subject community expects to happen; it sets no outcome a student must show and carries no level. Cite it as QAA, 2024, Health Studies Subject Benchmark Statement, para 2.28 (item 6). Do not present it as a statutory or regulatory requirement. Set it beside 2.27, 2.29 and 2.24."
  author-agent-dialogue: "Raise it with a programme team or reviewer when a team plans or audits its monitoring and review cycle. Frame it for staff as a check on course design or review and ask: When is the next internal review, and what evidence will it use? Do not hand it to a student as their task or quote the paragraph at length."
- statement: qaa/health-studies-2024/2.28.b7
  forPractitioner: { text: "Align annual monitoring, internal or external, with professional body requirements.", rewrite: light, force: will, status: drafted }
  forBeneficiary: { text: "not-applicable: a duty on the course team or provider; the student meets its effect, not a standard to reach", rewrite: full, force: will, status: drafted }
  author-agent-written: "Describe this as a duty on the course team or provider, stated with 'will': what the subject community expects to happen; it sets no outcome a student must show and carries no level. Cite it as QAA, 2024, Health Studies Subject Benchmark Statement, para 2.28 (item 7). Do not present it as a statutory or regulatory requirement. Set it beside 2.27, 2.29 and 2.24."
  author-agent-dialogue: "Raise it with a programme team or reviewer when a team plans or audits its monitoring and review cycle. Frame it for staff as a check on course design or review and ask: Which professional body's requirements does annual monitoring check? Do not hand it to a student as their task or quote the paragraph at length."
- statement: qaa/health-studies-2024/2.28.b8
  forPractitioner: { text: "Keep communication open inside the teaching team and with stakeholder partners through the review cycle.", rewrite: light, force: will, status: drafted }
  forBeneficiary: { text: "not-applicable: a duty on the course team or provider; the student meets its effect, not a standard to reach", rewrite: full, force: will, status: drafted }
  author-agent-written: "Describe this as a duty on the course team or provider, stated with 'will': what the subject community expects to happen; it sets no outcome a student must show and carries no level. Cite it as QAA, 2024, Health Studies Subject Benchmark Statement, para 2.28 (item 8). Do not present it as a statutory or regulatory requirement. Set it beside 2.27, 2.29 and 2.24."
  author-agent-dialogue: "Raise it with a programme team or reviewer when a team plans or audits its monitoring and review cycle. Frame it for staff as a check on course design or review and ask: How do stakeholder partners hear what the review found? Do not hand it to a student as their task or quote the paragraph at length."
- statement: qaa/health-studies-2024/2.28.b9
  forPractitioner: { text: "Check through review that course information and terms meet Competitions and Markets Authority requirements.", rewrite: light, force: will, status: drafted }
  forBeneficiary: { text: "not-applicable: a duty on the course team or provider; the student meets its effect, not a standard to reach", rewrite: full, force: will, status: drafted }
  author-agent-written: "Describe this as a duty on the course team or provider, stated with 'will': what the subject community expects to happen; it sets no outcome a student must show and carries no level. Cite it as QAA, 2024, Health Studies Subject Benchmark Statement, para 2.28 (item 9). Do not present it as a statutory or regulatory requirement. Set it beside 2.27, 2.29 and 2.24."
  author-agent-dialogue: "Raise it with a programme team or reviewer when a team plans or audits its monitoring and review cycle. Frame it for staff as a check on course design or review and ask: When were course information and terms last checked for consumer law? Do not hand it to a student as their task or quote the paragraph at length."
- statement: qaa/health-studies-2024/2.28.b10
  forPractitioner: { text: "Use results from the TEF, the NSS, PTES and PRES in monitoring and review.", rewrite: light, force: will, status: drafted }
  forBeneficiary: { text: "not-applicable: a duty on the course team or provider; the student meets its effect, not a standard to reach", rewrite: full, force: will, status: drafted }
  author-agent-written: "Describe this as a duty on the course team or provider, stated with 'will': what the subject community expects to happen; it sets no outcome a student must show and carries no level. Cite it as QAA, 2024, Health Studies Subject Benchmark Statement, para 2.28 (item 10). Do not present it as a statutory or regulatory requirement. Set it beside 2.27, 2.29 and 2.24."
  author-agent-dialogue: "Raise it with a programme team or reviewer when a team plans or audits its monitoring and review cycle. Frame it for staff as a check on course design or review and ask: What did the latest survey results show, and what has the team done about them? Do not hand it to a student as their task or quote the paragraph at length."
- statement: qaa/health-studies-2024/3.3
  forPractitioner: { text: "State the teaching and learning strategies clearly in the course documents and allow for the learning cultures students arrive with.", rewrite: light, force: will, status: drafted }
  forBeneficiary: { text: "not-applicable: a duty on the course team or provider; the student meets its effect, not a standard to reach", rewrite: full, force: will, status: drafted }
  author-agent-written: "Describe this as a duty on the course team or provider, stated with 'will': what the subject community expects to happen; it sets no outcome a student must show and carries no level. Cite it as QAA, 2024, Health Studies Subject Benchmark Statement, para 3.3. Do not present it as a statutory or regulatory requirement. Set it beside 3.4, 3.5 and 2.16."
  author-agent-dialogue: "Raise it with a programme team or reviewer when a team writes or revises its teaching and learning strategy. Frame it for staff as a check on course design or review and ask: Where are the teaching strategies stated, and how do they allow for students' earlier learning cultures? Do not hand it to a student as their task or quote the paragraph at length."
- statement: qaa/health-studies-2024/3.4
  forPractitioner: { text: "Build critical evaluation and analysis into teaching so students develop problem-solving, judgement of solutions, decision-making and creativity.", rewrite: light, force: should, status: drafted }
  forBeneficiary: { text: "not-applicable: a duty on the course team or provider; the student meets its effect, not a standard to reach", rewrite: full, force: should, status: drafted }
  author-agent-written: "Describe this as a duty on the course team or provider, stated with 'should': a firm recommendation that leaves room for the provider's judgement; it sets no outcome a student must show and carries no level. Cite it as QAA, 2024, Health Studies Subject Benchmark Statement, para 3.4. Do not present it as a statutory or regulatory requirement. Set it beside 4.4.b3, 4.5.b4 and 4.5.b6."
  author-agent-dialogue: "Raise it with a programme team or reviewer when a team plans teaching activities for higher-order skills. Frame it for staff as a check on course design or review and ask: Which activities ask students to judge solutions and decide, not only to describe? Do not hand it to a student as their task or quote the paragraph at length."
- statement: qaa/health-studies-2024/3.7.b1
  forPractitioner: { text: "Use both formative and summative assessment, and a range of methods that show progression and support graduate outcomes.", rewrite: light, force: will, status: drafted }
  forBeneficiary: { text: "not-applicable: a duty on the course team or provider; the student meets its effect, not a standard to reach", rewrite: full, force: will, status: drafted }
  author-agent-written: "Describe this as a duty on the course team or provider, stated with 'will': what the subject community expects to happen; it sets no outcome a student must show and carries no level. Cite it as QAA, 2024, Health Studies Subject Benchmark Statement, para 3.7 (item 1). Do not present it as a statutory or regulatory requirement. Set it beside 3.8, 3.9.b1 and 2.10."
  author-agent-dialogue: "Raise it with a programme team or reviewer when a team designs an assessment strategy. Frame it for staff as a check on course design or review and ask: Where does formative assessment come before each summative task? Do not hand it to a student as their task or quote the paragraph at length."
- statement: qaa/health-studies-2024/3.7.b2
  forPractitioner: { text: "Make reasonable adjustments to assessment that fit what the curriculum demands, and consider sliding scales for inclusive assessment.", rewrite: light, force: should, status: drafted }
  forBeneficiary: { text: "not-applicable: a duty on the course team or provider; the student meets its effect, not a standard to reach", rewrite: full, force: should, status: drafted }
  author-agent-written: "Describe this as a duty on the course team or provider, stated with 'should': a firm recommendation that leaves room for the provider's judgement; it sets no outcome a student must show and carries no level. Cite it as QAA, 2024, Health Studies Subject Benchmark Statement, para 3.7 (item 2). Do not present it as a statutory or regulatory requirement. Set it beside 1.24, 2.4.b8 and 3.10.b3."
  author-agent-dialogue: "Raise it with a programme team or reviewer when a team sets or reviews assessment adjustments. Frame it for staff as a check on course design or review and ask: How are adjustments decided, and do they keep to what the module must assess? Do not hand it to a student as their task or quote the paragraph at length."
- statement: qaa/health-studies-2024/3.7.b3
  forPractitioner: { text: "Decide, and state, how far generative AI tools are part of teaching, learning and assessment on the course.", rewrite: light, force: should, status: drafted }
  forBeneficiary: { text: "not-applicable: a duty on the course team or provider; the student meets its effect, not a standard to reach", rewrite: full, force: should, status: drafted }
  author-agent-written: "Describe this as a duty on the course team or provider, stated with 'should': a firm recommendation that leaves room for the provider's judgement; it sets no outcome a student must show and carries no level. Cite it as QAA, 2024, Health Studies Subject Benchmark Statement, para 3.7 (item 3). Do not present it as a statutory or regulatory requirement. Set it beside 3.7.b4, 3.8 and 4.5.b14."
  author-agent-dialogue: "Raise it with a programme team or reviewer when a team sets its position on generative AI. Frame it for staff as a check on course design or review and ask: What does each module tell students about using generative AI? Do not hand it to a student as their task or quote the paragraph at length."
- statement: qaa/health-studies-2024/3.7.b4
  forPractitioner: { text: "Make sure staff and students know the limits and risks of the AI tools in use, and set out what responsible, ethical use looks like.", rewrite: light, force: must, status: drafted }
  forBeneficiary: { text: "You must stay aware of the limits and risks of AI tools and use them responsibly and ethically.", rewrite: full, force: must, status: drafted }
  author-agent-written: "Present this as a 'must' that binds staff and students alike: awareness of the limits and risks of AI tools, for responsible and ethical use; it names no level and is read here for honours and master's. Cite it as QAA, 2024, Health Studies Subject Benchmark Statement, para 3.7, the sentence on AI risks. Do not present it as a ban on AI or as a regulatory rule. Set it beside 3.7.b3, 4.5.b14 and qaa/fheq-2024/4.15.b4."
  author-agent-dialogue: "Raise it whenever a student or teacher plans to use an AI tool for learning, assessment or marking. Ask a student what the tool could get wrong in their task and how they would check it; ask staff how the course explains those risks. Do not present AI as forbidden, and do not read the paragraph aloud."
- statement: qaa/health-studies-2024/3.9.b1
  forPractitioner: { text: "Write feedback that is personal, clear, empowering, manageable and points to next steps.", rewrite: light, force: will, status: drafted }
  forBeneficiary: { text: "not-applicable: a duty on the course team or provider; the student meets its effect, not a standard to reach", rewrite: full, force: will, status: drafted }
  author-agent-written: "Describe this as a duty on the course team or provider, stated with 'will': what the subject community expects to happen; it sets no outcome a student must show and carries no level. Cite it as QAA, 2024, Health Studies Subject Benchmark Statement, para 3.9 (item 1). Do not present it as a statutory or regulatory requirement. Set it beside 3.9.b2, 3.9.b3 and 3.10.b1 to 3.10.b6."
  author-agent-dialogue: "Raise it with a programme team or reviewer when a team reviews its feedback practice. Frame it for staff as a check on course design or review and ask: Would a student know what to do next after reading this feedback? Do not hand it to a student as their task or quote the paragraph at length."
- statement: qaa/health-studies-2024/3.9.b2
  forPractitioner: { text: "Return feedback promptly, link it to the brief, offer help in reading it and leave students room to reflect on their development.", rewrite: light, force: should, status: drafted }
  forBeneficiary: { text: "not-applicable: a duty on the course team or provider; the student meets its effect, not a standard to reach", rewrite: full, force: should, status: drafted }
  author-agent-written: "Describe this as a duty on the course team or provider, stated with 'should': a firm recommendation that leaves room for the provider's judgement; it sets no outcome a student must show and carries no level. Cite it as QAA, 2024, Health Studies Subject Benchmark Statement, para 3.9 (item 2). Do not present it as a statutory or regulatory requirement. Set it beside 3.9.b1, 3.10.b5 and 4.5.b9."
  author-agent-dialogue: "Raise it with a programme team or reviewer when a team sets feedback turnaround or support. Frame it for staff as a check on course design or review and ask: How soon does feedback arrive, and who helps students make sense of it? Do not hand it to a student as their task or quote the paragraph at length."
- statement: qaa/health-studies-2024/3.9.b3
  forPractitioner: { text: "Publish the nature, amount and timing of feedback for each assessment before the task is set.", rewrite: light, force: will, status: drafted }
  forBeneficiary: { text: "not-applicable: a duty on the course team or provider; the student meets its effect, not a standard to reach", rewrite: full, force: will, status: drafted }
  author-agent-written: "Describe this as a duty on the course team or provider, stated with 'will': what the subject community expects to happen; it sets no outcome a student must show and carries no level. Cite it as QAA, 2024, Health Studies Subject Benchmark Statement, para 3.9 (item 3). Do not present it as a statutory or regulatory requirement. Set it beside 3.9.b1, 3.9.b2 and 3.10.b2."
  author-agent-dialogue: "Raise it with a programme team or reviewer when a team writes assessment briefs. Frame it for staff as a check on course design or review and ask: Does each brief say what feedback will come, and when? Do not hand it to a student as their task or quote the paragraph at length."
- statement: qaa/health-studies-2024/3.10.b1
  forPractitioner: { text: "Check that feedback is valid, reliable and consistent across markers and modules.", rewrite: light, force: should, status: drafted }
  forBeneficiary: { text: "not-applicable: a duty on the course team or provider; the student meets its effect, not a standard to reach", rewrite: full, force: should, status: drafted }
  author-agent-written: "Describe this as a duty on the course team or provider, stated with 'should': a firm recommendation that leaves room for the provider's judgement; it sets no outcome a student must show and carries no level. Cite it as QAA, 2024, Health Studies Subject Benchmark Statement, para 3.10 (item 1). Do not present it as a statutory or regulatory requirement. Set it beside 3.9.b1 to 3.9.b3 and 3.10."
  author-agent-dialogue: "Raise it with a programme team or reviewer when a team reviews its feedback policy. Frame it for staff as a check on course design or review and ask: How does the team check that markers give consistent feedback? Do not hand it to a student as their task or quote the paragraph at length."
- statement: qaa/health-studies-2024/3.10.b2
  forPractitioner: { text: "Make feedback clear and easy to find.", rewrite: light, force: should, status: drafted }
  forBeneficiary: { text: "not-applicable: a duty on the course team or provider; the student meets its effect, not a standard to reach", rewrite: full, force: should, status: drafted }
  author-agent-written: "Describe this as a duty on the course team or provider, stated with 'should': a firm recommendation that leaves room for the provider's judgement; it sets no outcome a student must show and carries no level. Cite it as QAA, 2024, Health Studies Subject Benchmark Statement, para 3.10 (item 2). Do not present it as a statutory or regulatory requirement. Set it beside 3.9.b1 to 3.9.b3 and 3.10."
  author-agent-dialogue: "Raise it with a programme team or reviewer when a team reviews its feedback policy. Frame it for staff as a check on course design or review and ask: Where do students find their feedback, and can they read it easily? Do not hand it to a student as their task or quote the paragraph at length."
- statement: qaa/health-studies-2024/3.10.b3
  forPractitioner: { text: "Adapt feedback to accessibility needs and EDI, such as specific learning needs.", rewrite: light, force: should, status: drafted }
  forBeneficiary: { text: "not-applicable: a duty on the course team or provider; the student meets its effect, not a standard to reach", rewrite: full, force: should, status: drafted }
  author-agent-written: "Describe this as a duty on the course team or provider, stated with 'should': a firm recommendation that leaves room for the provider's judgement; it sets no outcome a student must show and carries no level. Cite it as QAA, 2024, Health Studies Subject Benchmark Statement, para 3.10 (item 3). Do not present it as a statutory or regulatory requirement. Set it beside 3.9.b1 to 3.9.b3 and 3.10."
  author-agent-dialogue: "Raise it with a programme team or reviewer when a team reviews its feedback policy. Frame it for staff as a check on course design or review and ask: How is feedback adapted for students with specific learning needs? Do not hand it to a student as their task or quote the paragraph at length."
- statement: qaa/health-studies-2024/3.10.b4
  forPractitioner: { text: "Link feedback to the learning outcomes and make it part of the course design.", rewrite: light, force: should, status: drafted }
  forBeneficiary: { text: "not-applicable: a duty on the course team or provider; the student meets its effect, not a standard to reach", rewrite: full, force: should, status: drafted }
  author-agent-written: "Describe this as a duty on the course team or provider, stated with 'should': a firm recommendation that leaves room for the provider's judgement; it sets no outcome a student must show and carries no level. Cite it as QAA, 2024, Health Studies Subject Benchmark Statement, para 3.10 (item 4). Do not present it as a statutory or regulatory requirement. Set it beside 3.9.b1 to 3.9.b3 and 3.10."
  author-agent-dialogue: "Raise it with a programme team or reviewer when a team reviews its feedback policy. Frame it for staff as a check on course design or review and ask: Does the feedback name the outcome it addresses? Do not hand it to a student as their task or quote the paragraph at length."
- statement: qaa/health-studies-2024/3.10.b5
  forPractitioner: { text: "Use feedback to let students confirm their knowledge and understanding.", rewrite: light, force: should, status: drafted }
  forBeneficiary: { text: "not-applicable: a duty on the course team or provider; the student meets its effect, not a standard to reach", rewrite: full, force: should, status: drafted }
  author-agent-written: "Describe this as a duty on the course team or provider, stated with 'should': a firm recommendation that leaves room for the provider's judgement; it sets no outcome a student must show and carries no level. Cite it as QAA, 2024, Health Studies Subject Benchmark Statement, para 3.10 (item 5). Do not present it as a statutory or regulatory requirement. Set it beside 3.9.b1 to 3.9.b3 and 3.10."
  author-agent-dialogue: "Raise it with a programme team or reviewer when a team reviews its feedback policy. Frame it for staff as a check on course design or review and ask: Does the feedback tell students what they have got right, not only what to fix? Do not hand it to a student as their task or quote the paragraph at length."
- statement: qaa/health-studies-2024/3.10.b6
  forPractitioner: { text: "Align feedback with progression rules and with PSRB requirements where they apply.", rewrite: light, force: should, status: drafted }
  forBeneficiary: { text: "not-applicable: a duty on the course team or provider; the student meets its effect, not a standard to reach", rewrite: full, force: should, status: drafted }
  author-agent-written: "Describe this as a duty on the course team or provider, stated with 'should': a firm recommendation that leaves room for the provider's judgement; it sets no outcome a student must show and carries no level. Cite it as QAA, 2024, Health Studies Subject Benchmark Statement, para 3.10 (item 6). Do not present it as a statutory or regulatory requirement. Set it beside 3.9.b1 to 3.9.b3 and 3.10."
  author-agent-dialogue: "Raise it with a programme team or reviewer when a team reviews its feedback policy. Frame it for staff as a check on course design or review and ask: Which PSRB requirements, if any, shape feedback on this course? Do not hand it to a student as their task or quote the paragraph at length."
- statement: qaa/health-studies-2024/3.11
  forPractitioner: { text: "Develop the supervision role with employers and workplace supervisors so students can place their learning in context and contribute in practice.", rewrite: light, force: will, status: drafted }
  forBeneficiary: { text: "not-applicable: a duty on the course team or provider; the student meets its effect, not a standard to reach", rewrite: full, force: will, status: drafted }
  author-agent-written: "Describe this as a duty on the course team or provider, stated with 'will': what the subject community expects to happen; it sets no outcome a student must show and carries no level. Cite it as QAA, 2024, Health Studies Subject Benchmark Statement, para 3.11. Do not present it as a statutory or regulatory requirement. Set it beside 3.12.b1 to 3.12.b7 and 2.22."
  author-agent-dialogue: "Raise it with a programme team or reviewer when a team sets up placements or work-based supervision. Frame it for staff as a check on course design or review and ask: Who agreed the supervision arrangements, and does each party know its role? Do not hand it to a student as their task or quote the paragraph at length."
- statement: qaa/health-studies-2024/3.12.b1
  forPractitioner: { text: "Prepare supervisors on varied learning styles and on the assessments students face.", rewrite: light, force: must, status: drafted }
  forBeneficiary: { text: "not-applicable: a duty on the course team or provider; the student meets its effect, not a standard to reach", rewrite: full, force: must, status: drafted }
  author-agent-written: "Describe this as a duty on the course team or provider, stated with 'must', the statement's firmest word; it sets no outcome a student must show and carries no level. Cite it as QAA, 2024, Health Studies Subject Benchmark Statement, para 3.12 (item 1). Do not present it as a statutory or regulatory requirement; the lead-in says 'requires consideration of', which this record reads as must (Part E). Set it beside 3.11 and 3.12."
  author-agent-dialogue: "Raise it with a programme team or reviewer when a team designs supervision for placements or practice. Frame it for staff as a check on course design or review and ask: How are new supervisors prepared before they take a student? Do not hand it to a student as their task or quote the paragraph at length."
- statement: qaa/health-studies-2024/3.12.b2
  forPractitioner: { text: "Use a collaborative approach to supervision that can adapt to local practice.", rewrite: light, force: must, status: drafted }
  forBeneficiary: { text: "not-applicable: a duty on the course team or provider; the student meets its effect, not a standard to reach", rewrite: full, force: must, status: drafted }
  author-agent-written: "Describe this as a duty on the course team or provider, stated with 'must', the statement's firmest word; it sets no outcome a student must show and carries no level. Cite it as QAA, 2024, Health Studies Subject Benchmark Statement, para 3.12 (item 2). Do not present it as a statutory or regulatory requirement; the lead-in says 'requires consideration of', which this record reads as must (Part E). Set it beside 3.11 and 3.12."
  author-agent-dialogue: "Raise it with a programme team or reviewer when a team designs supervision for placements or practice. Frame it for staff as a check on course design or review and ask: How does supervision adapt to the practice setting? Do not hand it to a student as their task or quote the paragraph at length."
- statement: qaa/health-studies-2024/3.12.b3
  forPractitioner: { text: "Set objectives, monitor progress and plan actions with each student.", rewrite: light, force: must, status: drafted }
  forBeneficiary: { text: "not-applicable: a duty on the course team or provider; the student meets its effect, not a standard to reach", rewrite: full, force: must, status: drafted }
  author-agent-written: "Describe this as a duty on the course team or provider, stated with 'must', the statement's firmest word; it sets no outcome a student must show and carries no level. Cite it as QAA, 2024, Health Studies Subject Benchmark Statement, para 3.12 (item 3). Do not present it as a statutory or regulatory requirement; the lead-in says 'requires consideration of', which this record reads as must (Part E). Set it beside 3.11 and 3.12."
  author-agent-dialogue: "Raise it with a programme team or reviewer when a team designs supervision for placements or practice. Frame it for staff as a check on course design or review and ask: Does each student have objectives and an action plan agreed with their supervisor? Do not hand it to a student as their task or quote the paragraph at length."
- statement: qaa/health-studies-2024/3.12.b4
  forPractitioner: { text: "Promote a culture of learning in the host organisation.", rewrite: light, force: must, status: drafted }
  forBeneficiary: { text: "not-applicable: a duty on the course team or provider; the student meets its effect, not a standard to reach", rewrite: full, force: must, status: drafted }
  author-agent-written: "Describe this as a duty on the course team or provider, stated with 'must', the statement's firmest word; it sets no outcome a student must show and carries no level. Cite it as QAA, 2024, Health Studies Subject Benchmark Statement, para 3.12 (item 4). Do not present it as a statutory or regulatory requirement; the lead-in says 'requires consideration of', which this record reads as must (Part E). Set it beside 3.11 and 3.12."
  author-agent-dialogue: "Raise it with a programme team or reviewer when a team designs supervision for placements or practice. Frame it for staff as a check on course design or review and ask: What does the host organisation do to support learning? Do not hand it to a student as their task or quote the paragraph at length."
- statement: qaa/health-studies-2024/3.12.b5
  forPractitioner: { text: "Make advocacy for, and coaching of, students part of the supervisor role.", rewrite: light, force: must, status: drafted }
  forBeneficiary: { text: "not-applicable: a duty on the course team or provider; the student meets its effect, not a standard to reach", rewrite: full, force: must, status: drafted }
  author-agent-written: "Describe this as a duty on the course team or provider, stated with 'must', the statement's firmest word; it sets no outcome a student must show and carries no level. Cite it as QAA, 2024, Health Studies Subject Benchmark Statement, para 3.12 (item 5). Do not present it as a statutory or regulatory requirement; the lead-in says 'requires consideration of', which this record reads as must (Part E). Set it beside 3.11 and 3.12."
  author-agent-dialogue: "Raise it with a programme team or reviewer when a team designs supervision for placements or practice. Frame it for staff as a check on course design or review and ask: Who speaks up for the student if a placement goes wrong? Do not hand it to a student as their task or quote the paragraph at length."
- statement: qaa/health-studies-2024/3.12.b6
  forPractitioner: { text: "Give students structured chances for critical reflection that draw on what they already know.", rewrite: light, force: must, status: drafted }
  forBeneficiary: { text: "not-applicable: a duty on the course team or provider; the student meets its effect, not a standard to reach", rewrite: full, force: must, status: drafted }
  author-agent-written: "Describe this as a duty on the course team or provider, stated with 'must', the statement's firmest word; it sets no outcome a student must show and carries no level. Cite it as QAA, 2024, Health Studies Subject Benchmark Statement, para 3.12 (item 6). Do not present it as a statutory or regulatory requirement; the lead-in says 'requires consideration of', which this record reads as must (Part E). Set it beside 3.11 and 3.12."
  author-agent-dialogue: "Raise it with a programme team or reviewer when a team designs supervision for placements or practice. Frame it for staff as a check on course design or review and ask: When do students reflect with their supervisor, and on what? Do not hand it to a student as their task or quote the paragraph at length."
- statement: qaa/health-studies-2024/3.12.b7
  forPractitioner: { text: "Arrange three-way supervision between student, course and the industry or healthcare setting.", rewrite: light, force: must, status: drafted }
  forBeneficiary: { text: "not-applicable: a duty on the course team or provider; the student meets its effect, not a standard to reach", rewrite: full, force: must, status: drafted }
  author-agent-written: "Describe this as a duty on the course team or provider, stated with 'must', the statement's firmest word; it sets no outcome a student must show and carries no level. Cite it as QAA, 2024, Health Studies Subject Benchmark Statement, para 3.12 (item 7). Do not present it as a statutory or regulatory requirement; the lead-in says 'requires consideration of', which this record reads as must (Part E). Set it beside 3.11 and 3.12."
  author-agent-dialogue: "Raise it with a programme team or reviewer when a team designs supervision for placements or practice. Frame it for staff as a check on course design or review and ask: Is the workplace a full party to supervision, with the student and the course? Do not hand it to a student as their task or quote the paragraph at length."
- statement: qaa/health-studies-2024/4.2
  forPractitioner: { text: "Use Annex D's classification descriptions when deciding what evidence shows achievement above the threshold; the statement gives no rungs above it.", rewrite: light, force: should, status: drafted }
  forBeneficiary: { text: "not-applicable: a duty on the course team or provider; the student meets its effect, not a standard to reach", rewrite: full, force: should, status: drafted }
  author-agent-written: "Describe this as a duty on the course team or provider, stated with 'should': a firm recommendation that leaves room for the provider's judgement; it sets no outcome a student must show and carries no level. Cite it as QAA, 2024, Health Studies Subject Benchmark Statement, para 4.2. Do not present it as a statutory or regulatory requirement. Set it beside 4.3, qaa/fheq-2024/annex-d/summary and std:ref:uk-assesscriteria (band axis)."
  author-agent-dialogue: "Raise it with a programme team or reviewer when a team writes classification criteria or marking descriptors. Frame it for staff as a check on course design or review and ask: How do the course's classification criteria use Annex D? Do not hand it to a student as their task or quote the paragraph at length."
- statement: qaa/health-studies-2024/4.3
  forPractitioner: { text: "Treat the section 4 threshold lists as what every student must show for the award: level 6 for honours, level 7 for master's.", rewrite: light, force: must, status: drafted }
  forBeneficiary: { text: "To be awarded your degree, you must show at least the threshold level: level 6 for an undergraduate degree, level 7 for a master's.", rewrite: full, force: must, status: drafted }
  author-agent-written: "Present this as the 'must' that defines the threshold: the minimum a student shows to be eligible for an honours award (level 6) or a master's award (level 7). Cite it as QAA, 2024, Health Studies Subject Benchmark Statement, para 4.3. Do not claim it sets a pass mark or classifications; those rest with the provider and Annex D (4.2). Set it beside 4.4, 4.5, 4.7, qaa/fheq-2024/4.15, qaa/fheq-2024/4.17 and qaa/fheq-2024/annex-d/summary/r1/3rd."
  author-agent-dialogue: "Raise it when a student asks what they must achieve to graduate, or when a team debates whether an outcome is essential. Tell a student plainly that the threshold lists are the minimum for the award, and ask which items they feel least sure of. Do not confuse the threshold with a class of degree or read the lists aloud."
- statement: qaa/health-studies-2024/4.4.b1
  forPractitioner: { text: "Teach and assess the course so that every honours graduate can use their knowledge across linked settings and bring together the theories behind the subject on physical, psychosocial and mental well-being; this belongs to the minimum, not to the higher classes.", rewrite: light, force: threshold, status: drafted }
  forBeneficiary: { text: "As a minimum for your honours degree, you should be able to use what you know across connected settings and combine the theories behind health on body, mind and social well-being.", rewrite: full, force: threshold, status: drafted }
  author-agent-written: "Present this as a threshold outcome in subject knowledge, understanding or skills for the bachelor's degree with honours at FHEQ level 6 (FQHEIS level 10): every graduate in the subject should show it, so it is the floor and not a mark of distinction. Cite it as QAA, 2024, Health Studies Subject Benchmark Statement, para 4.4 (item 1). Do not call it a regulatory requirement or claim it for master's awards, which have their own lists at 4.7 and 4.8. Set it beside 4.4.b4 and 4.4.b18, the honours descriptor item qaa/fheq-2024/4.15.b3.1, Annex D's third-class column (qaa/fheq-2024/annex-d/summary/r1/3rd) and spine:6."
  author-agent-dialogue: "Bring it up when a student asks what an honours graduate must manage on applying and joining theory across settings, or when a programme team checks module outcomes against the exit standard. With a student, put it plainly as a minimum to reach by graduation; with staff, ask where the course teaches and assesses it. Ask: Which piece of work shows you combining more than one theory to explain a health question? Avoid reading the issuer's list aloud, and do not treat higher achievement as what the minimum demands."
- statement: qaa/health-studies-2024/4.4.b2
  forPractitioner: { text: "Teach and assess the course so that every honours graduate can show they grasp how wide the subject is by using it on practical problems; this belongs to the minimum, not to the higher classes.", rewrite: light, force: threshold, status: drafted }
  forBeneficiary: { text: "As a minimum for your honours degree, you should be able to show how wide the field of health is by using it to tackle practical problems.", rewrite: full, force: threshold, status: drafted }
  author-agent-written: "Present this as a threshold outcome in subject knowledge, understanding or skills for the bachelor's degree with honours at FHEQ level 6 (FQHEIS level 10): every graduate in the subject should show it, so it is the floor and not a mark of distinction. Cite it as QAA, 2024, Health Studies Subject Benchmark Statement, para 4.4 (item 2). Do not call it a regulatory requirement or claim it for master's awards, which have their own lists at 4.7 and 4.8. Set it beside 4.4.b1 and 4.4.b7, the honours descriptor item qaa/fheq-2024/4.15.b1, Annex D's third-class column (qaa/fheq-2024/annex-d/summary/r1/3rd) and spine:6."
  author-agent-dialogue: "Bring it up when a student asks what an honours graduate must manage on the breadth of the subject in real problems, or when a programme team checks module outcomes against the exit standard. With a student, put it plainly as a minimum to reach by graduation; with staff, ask where the course teaches and assesses it. Ask: Can you name a real problem you worked on and the parts of the subject you drew on? Avoid reading the issuer's list aloud, and do not treat higher achievement as what the minimum demands."
- statement: qaa/health-studies-2024/4.4.b3
  forPractitioner: { text: "Teach and assess the course so that every honours graduate can take more than one viewpoint when judging and resolving issues that arise in health settings; this belongs to the minimum, not to the higher classes.", rewrite: light, force: threshold, status: drafted }
  forBeneficiary: { text: "As a minimum for your honours degree, you should be able to look at health issues from several viewpoints when you judge them and work out what to do.", rewrite: full, force: threshold, status: drafted }
  author-agent-written: "Present this as a threshold outcome in subject knowledge, understanding or skills for the bachelor's degree with honours at FHEQ level 6 (FQHEIS level 10): every graduate in the subject should show it, so it is the floor and not a mark of distinction. Cite it as QAA, 2024, Health Studies Subject Benchmark Statement, para 4.4 (item 3). Do not call it a regulatory requirement or claim it for master's awards, which have their own lists at 4.7 and 4.8. Set it beside 4.4.b16 and 4.5.b4, the honours descriptor item qaa/fheq-2024/4.15.b7, Annex D's third-class column (qaa/fheq-2024/annex-d/summary/r4/3rd) and spine:6."
  author-agent-dialogue: "Bring it up when a student asks what an honours graduate must manage on judging issues from several viewpoints, or when a programme team checks module outcomes against the exit standard. With a student, put it plainly as a minimum to reach by graduation; with staff, ask where the course teaches and assesses it. Ask: When you last analysed a health issue, which viewpoints did you weigh and which did you leave out? Avoid reading the issuer's list aloud, and do not treat higher achievement as what the minimum demands."
- statement: qaa/health-studies-2024/4.4.b4
  forPractitioner: { text: "Teach and assess the course so that every honours graduate can combine specialist and linked knowledge from the subject's many disciplines to devise new answers to health problems; this belongs to the minimum, not to the higher classes.", rewrite: light, force: threshold, status: drafted }
  forBeneficiary: { text: "As a minimum for your honours degree, you should be able to draw together knowledge from the different disciplines in health to come up with new answers to health problems.", rewrite: full, force: threshold, status: drafted }
  author-agent-written: "Present this as a threshold outcome in subject knowledge, understanding or skills for the bachelor's degree with honours at FHEQ level 6 (FQHEIS level 10): every graduate in the subject should show it, so it is the floor and not a mark of distinction. Cite it as QAA, 2024, Health Studies Subject Benchmark Statement, para 4.4 (item 4). Do not call it a regulatory requirement or claim it for master's awards, which have their own lists at 4.7 and 4.8. Set it beside 4.4.b1 and 4.4.b18, the honours descriptor item qaa/fheq-2024/4.15.b3.1, Annex D's third-class column (qaa/fheq-2024/annex-d/summary/r4/3rd) and spine:6."
  author-agent-dialogue: "Bring it up when a student asks what an honours graduate must manage on joining specialist knowledge for new solutions, or when a programme team checks module outcomes against the exit standard. With a student, put it plainly as a minimum to reach by graduation; with staff, ask where the course teaches and assesses it. Ask: Where have you joined ideas from two disciplines to propose something new? Avoid reading the issuer's list aloud, and do not treat higher achievement as what the minimum demands."
- statement: qaa/health-studies-2024/4.4.b5
  forPractitioner: { text: "Teach and assess the course so that every honours graduate can join research evidence with relevant national policy and guidance and use the result to shape the subject; this belongs to the minimum, not to the higher classes.", rewrite: light, force: threshold, status: drafted }
  forBeneficiary: { text: "As a minimum for your honours degree, you should be able to connect research evidence with national health policy and guidance.", rewrite: full, force: threshold, status: drafted }
  author-agent-written: "Present this as a threshold outcome in subject knowledge, understanding or skills for the bachelor's degree with honours at FHEQ level 6 (FQHEIS level 10): every graduate in the subject should show it, so it is the floor and not a mark of distinction. Cite it as QAA, 2024, Health Studies Subject Benchmark Statement, para 4.4 (item 5). Do not call it a regulatory requirement or claim it for master's awards, which have their own lists at 4.7 and 4.8. Set it beside 4.4.b13, the honours descriptor item qaa/fheq-2024/4.15.b1, Annex D's third-class column (qaa/fheq-2024/annex-d/summary/r1/3rd) and spine:6."
  author-agent-dialogue: "Bring it up when a student asks what an honours graduate must manage on evidence with national policy and guidance, or when a programme team checks module outcomes against the exit standard. With a student, put it plainly as a minimum to reach by graduation; with staff, ask where the course teaches and assesses it. Ask: Which national policy or guideline have you tested against the evidence, and what did you find? Avoid reading the issuer's list aloud, and do not treat higher achievement as what the minimum demands."
- statement: qaa/health-studies-2024/4.4.b6
  forPractitioner: { text: "Teach and assess the course so that every honours graduate can understand health globally, allowing for the way travel, migration and displacement move populations; this belongs to the minimum, not to the higher classes.", rewrite: light, force: threshold, status: drafted }
  forBeneficiary: { text: "As a minimum for your honours degree, you should be able to understand health in a global way, including how travel, migration and displacement move people around.", rewrite: full, force: threshold, status: drafted }
  author-agent-written: "Present this as a threshold outcome in subject knowledge, understanding or skills for the bachelor's degree with honours at FHEQ level 6 (FQHEIS level 10): every graduate in the subject should show it, so it is the floor and not a mark of distinction. Cite it as QAA, 2024, Health Studies Subject Benchmark Statement, para 4.4 (item 6). Do not call it a regulatory requirement or claim it for master's awards, which have their own lists at 4.7 and 4.8. Set it beside 4.4.b16, the honours descriptor item qaa/fheq-2024/4.15.b1, Annex D's third-class column (qaa/fheq-2024/annex-d/summary/r1/3rd) and spine:6."
  author-agent-dialogue: "Bring it up when a student asks what an honours graduate must manage on health in a global, mobile world, or when a programme team checks module outcomes against the exit standard. With a student, put it plainly as a minimum to reach by graduation; with staff, ask where the course teaches and assesses it. Ask: How does population movement change the health question you are studying? Avoid reading the issuer's list aloud, and do not treat higher achievement as what the minimum demands."
- statement: qaa/health-studies-2024/4.4.b7
  forPractitioner: { text: "Teach and assess the course so that every honours graduate can understand that health has physical, mental and social sides that shift over time, and know the challenges it faces now; this belongs to the minimum, not to the higher classes.", rewrite: light, force: threshold, status: drafted }
  forBeneficiary: { text: "As a minimum for your honours degree, you should be able to understand that health covers body, mind and social life, changes over time and faces current challenges.", rewrite: full, force: threshold, status: drafted }
  author-agent-written: "Present this as a threshold outcome in subject knowledge, understanding or skills for the bachelor's degree with honours at FHEQ level 6 (FQHEIS level 10): every graduate in the subject should show it, so it is the floor and not a mark of distinction. Cite it as QAA, 2024, Health Studies Subject Benchmark Statement, para 4.4 (item 7). Do not call it a regulatory requirement or claim it for master's awards, which have their own lists at 4.7 and 4.8. Set it beside 4.4.b2, the honours descriptor item qaa/fheq-2024/4.15.b1, Annex D's third-class column (qaa/fheq-2024/annex-d/summary/r1/3rd) and spine:6."
  author-agent-dialogue: "Bring it up when a student asks what an honours graduate must manage on the many dimensions of health, or when a programme team checks module outcomes against the exit standard. With a student, put it plainly as a minimum to reach by graduation; with staff, ask where the course teaches and assesses it. Ask: Which current health challenge can you explain from its physical, mental and social sides? Avoid reading the issuer's list aloud, and do not treat higher achievement as what the minimum demands."
- statement: qaa/health-studies-2024/4.4.b8
  forPractitioner: { text: "Teach and assess the course so that every honours graduate can show understanding of several theories of what causes health and ill health; this belongs to the minimum, not to the higher classes.", rewrite: light, force: threshold, status: drafted }
  forBeneficiary: { text: "As a minimum for your honours degree, you should be able to explain several theories of what makes people healthy or ill.", rewrite: full, force: threshold, status: drafted }
  author-agent-written: "Present this as a threshold outcome in subject knowledge, understanding or skills for the bachelor's degree with honours at FHEQ level 6 (FQHEIS level 10): every graduate in the subject should show it, so it is the floor and not a mark of distinction. Cite it as QAA, 2024, Health Studies Subject Benchmark Statement, para 4.4 (item 8). Do not call it a regulatory requirement or claim it for master's awards, which have their own lists at 4.7 and 4.8. Set it beside 4.4.b14, the honours descriptor item qaa/fheq-2024/4.15.b1, Annex D's third-class column (qaa/fheq-2024/annex-d/summary/r1/3rd) and spine:6."
  author-agent-dialogue: "Bring it up when a student asks what an honours graduate must manage on theories of causality in health, or when a programme team checks module outcomes against the exit standard. With a student, put it plainly as a minimum to reach by graduation; with staff, ask where the course teaches and assesses it. Ask: Which two theories of the causes of ill health can you compare, and where do they disagree? Avoid reading the issuer's list aloud, and do not treat higher achievement as what the minimum demands."
- statement: qaa/health-studies-2024/4.4.b9
  forPractitioner: { text: "Teach and assess the course so that every honours graduate can set out a variety of theoretical and professional reasons offered for health interventions; this belongs to the minimum, not to the higher classes.", rewrite: light, force: threshold, status: drafted }
  forBeneficiary: { text: "As a minimum for your honours degree, you should be able to explain the different theoretical and professional reasons people give for health interventions.", rewrite: full, force: threshold, status: drafted }
  author-agent-written: "Present this as a threshold outcome in subject knowledge, understanding or skills for the bachelor's degree with honours at FHEQ level 6 (FQHEIS level 10): every graduate in the subject should show it, so it is the floor and not a mark of distinction. Cite it as QAA, 2024, Health Studies Subject Benchmark Statement, para 4.4 (item 9). Do not call it a regulatory requirement or claim it for master's awards, which have their own lists at 4.7 and 4.8. Set it beside 4.4.b10, the honours descriptor item qaa/fheq-2024/4.15.b3.2, Annex D's third-class column (qaa/fheq-2024/annex-d/summary/r1/3rd) and spine:6."
  author-agent-dialogue: "Bring it up when a student asks what an honours graduate must manage on reasons given for health interventions, or when a programme team checks module outcomes against the exit standard. With a student, put it plainly as a minimum to reach by graduation; with staff, ask where the course teaches and assesses it. Ask: For one intervention you know, what reasons were given for it, and by whom? Avoid reading the issuer's list aloud, and do not treat higher achievement as what the minimum demands."
- statement: qaa/health-studies-2024/4.4.b10
  forPractitioner: { text: "Teach and assess the course so that every honours graduate can gather, analyse and report evidence on how health promotion helps people make their own life choices; this belongs to the minimum, not to the higher classes.", rewrite: light, force: threshold, status: drafted }
  forBeneficiary: { text: "As a minimum for your honours degree, you should be able to gather, analyse and present evidence on how health promotion helps people make their own choices.", rewrite: full, force: threshold, status: drafted }
  author-agent-written: "Present this as a threshold outcome in subject knowledge, understanding or skills for the bachelor's degree with honours at FHEQ level 6 (FQHEIS level 10): every graduate in the subject should show it, so it is the floor and not a mark of distinction. Cite it as QAA, 2024, Health Studies Subject Benchmark Statement, para 4.4 (item 10). Do not call it a regulatory requirement or claim it for master's awards, which have their own lists at 4.7 and 4.8. Set it beside 4.4.b9, the honours descriptor item qaa/fheq-2024/4.15.b6, Annex D's third-class column (qaa/fheq-2024/annex-d/summary/r1/3rd) and spine:6."
  author-agent-dialogue: "Bring it up when a student asks what an honours graduate must manage on evidence on health promotion and autonomy, or when a programme team checks module outcomes against the exit standard. With a student, put it plainly as a minimum to reach by graduation; with staff, ask where the course teaches and assesses it. Ask: What evidence have you gathered on a health promotion campaign, and how did you present it? Avoid reading the issuer's list aloud, and do not treat higher achievement as what the minimum demands."
- statement: qaa/health-studies-2024/4.4.b11
  forPractitioner: { text: "Teach and assess the course so that every honours graduate can explain how individuals and institutions each shape health status; this belongs to the minimum, not to the higher classes.", rewrite: light, force: threshold, status: drafted }
  forBeneficiary: { text: "As a minimum for your honours degree, you should be able to explain how both individuals and institutions affect how healthy people are.", rewrite: full, force: threshold, status: drafted }
  author-agent-written: "Present this as a threshold outcome in subject knowledge, understanding or skills for the bachelor's degree with honours at FHEQ level 6 (FQHEIS level 10): every graduate in the subject should show it, so it is the floor and not a mark of distinction. Cite it as QAA, 2024, Health Studies Subject Benchmark Statement, para 4.4 (item 11). Do not call it a regulatory requirement or claim it for master's awards, which have their own lists at 4.7 and 4.8. Set it beside 4.4.b13, the honours descriptor item qaa/fheq-2024/4.15.b1, Annex D's third-class column (qaa/fheq-2024/annex-d/summary/r1/3rd) and spine:6."
  author-agent-dialogue: "Bring it up when a student asks what an honours graduate must manage on individuals and institutions shaping health, or when a programme team checks module outcomes against the exit standard. With a student, put it plainly as a minimum to reach by graduation; with staff, ask where the course teaches and assesses it. Ask: In a case you know, what did individuals do and what did institutions do to change health? Avoid reading the issuer's list aloud, and do not treat higher achievement as what the minimum demands."
- statement: qaa/health-studies-2024/4.4.b12
  forPractitioner: { text: "Teach and assess the course so that every honours graduate can recognise that people experience and value health in many different ways; this belongs to the minimum, not to the higher classes.", rewrite: light, force: threshold, status: drafted }
  forBeneficiary: { text: "As a minimum for your honours degree, you should be able to recognise that people, you included, experience and value health in different ways.", rewrite: full, force: threshold, status: drafted }
  author-agent-written: "Present this as a threshold outcome in subject knowledge, understanding or skills for the bachelor's degree with honours at FHEQ level 6 (FQHEIS level 10): every graduate in the subject should show it, so it is the floor and not a mark of distinction. Cite it as QAA, 2024, Health Studies Subject Benchmark Statement, para 4.4 (item 12). Do not call it a regulatory requirement or claim it for master's awards, which have their own lists at 4.7 and 4.8. Set it beside 4.4.b15, the honours descriptor item qaa/fheq-2024/4.15.b4, Annex D's third-class column (qaa/fheq-2024/annex-d/summary/r1/3rd) and spine:6."
  author-agent-dialogue: "Bring it up when a student asks what an honours graduate must manage on varied experiences and values of health, or when a programme team checks module outcomes against the exit standard. With a student, put it plainly as a minimum to reach by graduation; with staff, ask where the course teaches and assesses it. Ask: How might someone from a different background see the health issue you are working on? Avoid reading the issuer's list aloud, and do not treat higher achievement as what the minimum demands."
- statement: qaa/health-studies-2024/4.4.b13
  forPractitioner: { text: "Teach and assess the course so that every honours graduate can compare different healthcare systems and the policy-making behind them; this belongs to the minimum, not to the higher classes.", rewrite: light, force: threshold, status: drafted }
  forBeneficiary: { text: "As a minimum for your honours degree, you should be able to compare healthcare systems and the policies that shape them.", rewrite: full, force: threshold, status: drafted }
  author-agent-written: "Present this as a threshold outcome in subject knowledge, understanding or skills for the bachelor's degree with honours at FHEQ level 6 (FQHEIS level 10): every graduate in the subject should show it, so it is the floor and not a mark of distinction. Cite it as QAA, 2024, Health Studies Subject Benchmark Statement, para 4.4 (item 13). Do not call it a regulatory requirement or claim it for master's awards, which have their own lists at 4.7 and 4.8. Set it beside 4.4.b5, the honours descriptor item qaa/fheq-2024/4.15.b7, Annex D's third-class column (qaa/fheq-2024/annex-d/summary/r4/3rd) and spine:6."
  author-agent-dialogue: "Bring it up when a student asks what an honours graduate must manage on healthcare systems and policy, or when a programme team checks module outcomes against the exit standard. With a student, put it plainly as a minimum to reach by graduation; with staff, ask where the course teaches and assesses it. Ask: Which two healthcare systems could you compare, and on what points? Avoid reading the issuer's list aloud, and do not treat higher achievement as what the minimum demands."
- statement: qaa/health-studies-2024/4.4.b14
  forPractitioner: { text: "Teach and assess the course so that every honours graduate can show they know a variety of the subject's theoretical debates; this belongs to the minimum, not to the higher classes.", rewrite: light, force: threshold, status: drafted }
  forBeneficiary: { text: "As a minimum for your honours degree, you should be able to show you know the main theoretical debates in your subject.", rewrite: full, force: threshold, status: drafted }
  author-agent-written: "Present this as a threshold outcome in subject knowledge, understanding or skills for the bachelor's degree with honours at FHEQ level 6 (FQHEIS level 10): every graduate in the subject should show it, so it is the floor and not a mark of distinction. Cite it as QAA, 2024, Health Studies Subject Benchmark Statement, para 4.4 (item 14). Do not call it a regulatory requirement or claim it for master's awards, which have their own lists at 4.7 and 4.8. Set it beside 4.4.b8, the honours descriptor item qaa/fheq-2024/4.15.b3.1, Annex D's third-class column (qaa/fheq-2024/annex-d/summary/r1/3rd) and spine:6."
  author-agent-dialogue: "Bring it up when a student asks what an honours graduate must manage on theoretical debates in the subject, or when a programme team checks module outcomes against the exit standard. With a student, put it plainly as a minimum to reach by graduation; with staff, ask where the course teaches and assesses it. Ask: Which theoretical debate in the subject could you sum up for a fellow student? Avoid reading the issuer's list aloud, and do not treat higher achievement as what the minimum demands."
- statement: qaa/health-studies-2024/4.4.b15
  forPractitioner: { text: "Teach and assess the course so that every honours graduate can show an informed grasp of ethical viewpoints and of the many values people attach to health and to well-being of body and mind; this belongs to the minimum, not to the higher classes.", rewrite: light, force: threshold, status: drafted }
  forBeneficiary: { text: "As a minimum for your honours degree, you should be able to show you understand ethical viewpoints and the range of values people hold about health and well-being.", rewrite: full, force: threshold, status: drafted }
  author-agent-written: "Present this as a threshold outcome in subject knowledge, understanding or skills for the bachelor's degree with honours at FHEQ level 6 (FQHEIS level 10): every graduate in the subject should show it, so it is the floor and not a mark of distinction. Cite it as QAA, 2024, Health Studies Subject Benchmark Statement, para 4.4 (item 15). Do not call it a regulatory requirement or claim it for master's awards, which have their own lists at 4.7 and 4.8. Set it beside 4.4.b12 and 4.5.b20, the honours descriptor item qaa/fheq-2024/4.15.b4, Annex D's third-class column (qaa/fheq-2024/annex-d/summary/r1/3rd) and spine:6."
  author-agent-dialogue: "Bring it up when a student asks what an honours graduate must manage on ethics and values in health, or when a programme team checks module outcomes against the exit standard. With a student, put it plainly as a minimum to reach by graduation; with staff, ask where the course teaches and assesses it. Ask: Which ethical question in your area divides people, and what values sit on each side? Avoid reading the issuer's list aloud, and do not treat higher achievement as what the minimum demands."
- statement: qaa/health-studies-2024/4.4.b16
  forPractitioner: { text: "Teach and assess the course so that every honours graduate can discuss inequalities in health between populations and judge how well population-wide action narrows health gaps in diverse ethnic communities; this belongs to the minimum, not to the higher classes.", rewrite: light, force: threshold, status: drafted }
  forBeneficiary: { text: "As a minimum for your honours degree, you should be able to discuss health inequalities between groups and judge how well population-wide action narrows them in diverse ethnic communities.", rewrite: full, force: threshold, status: drafted }
  author-agent-written: "Present this as a threshold outcome in subject knowledge, understanding or skills for the bachelor's degree with honours at FHEQ level 6 (FQHEIS level 10): every graduate in the subject should show it, so it is the floor and not a mark of distinction. Cite it as QAA, 2024, Health Studies Subject Benchmark Statement, para 4.4 (item 16). Do not call it a regulatory requirement or claim it for master's awards, which have their own lists at 4.7 and 4.8. Set it beside 4.4.b19, the honours descriptor item qaa/fheq-2024/4.15.b7, Annex D's third-class column (qaa/fheq-2024/annex-d/summary/r4/3rd) and spine:6."
  author-agent-dialogue: "Bring it up when a student asks what an honours graduate must manage on health inequalities and population interventions, or when a programme team checks module outcomes against the exit standard. With a student, put it plainly as a minimum to reach by graduation; with staff, ask where the course teaches and assesses it. Ask: Which intervention aimed at a health gap have you assessed, and what did it achieve? Avoid reading the issuer's list aloud, and do not treat higher achievement as what the minimum demands."
- statement: qaa/health-studies-2024/4.4.b17
  forPractitioner: { text: "Teach and assess the course so that every honours graduate can recognise why research matters to the subject; this belongs to the minimum, not to the higher classes.", rewrite: light, force: threshold, status: drafted }
  forBeneficiary: { text: "As a minimum for your honours degree, you should be able to recognise why research matters in the study of health.", rewrite: full, force: threshold, status: drafted }
  author-agent-written: "Present this as a threshold outcome in subject knowledge, understanding or skills for the bachelor's degree with honours at FHEQ level 6 (FQHEIS level 10): every graduate in the subject should show it, so it is the floor and not a mark of distinction. Cite it as QAA, 2024, Health Studies Subject Benchmark Statement, para 4.4 (item 17). Do not call it a regulatory requirement or claim it for master's awards, which have their own lists at 4.7 and 4.8. Set it beside 4.4.b21, the honours descriptor item qaa/fheq-2024/4.15.b3.2, Annex D's third-class column (qaa/fheq-2024/annex-d/summary/r1/3rd) and spine:6."
  author-agent-dialogue: "Bring it up when a student asks what an honours graduate must manage on why research matters, or when a programme team checks module outcomes against the exit standard. With a student, put it plainly as a minimum to reach by graduation; with staff, ask where the course teaches and assesses it. Ask: How has a research finding changed what you think about a health question? Avoid reading the issuer's list aloud, and do not treat higher achievement as what the minimum demands."
- statement: qaa/health-studies-2024/4.4.b18
  forPractitioner: { text: "Teach and assess the course so that every honours graduate can cross traditional subject lines, using knowledge from other disciplines to think about health issues; this belongs to the minimum, not to the higher classes.", rewrite: light, force: threshold, status: drafted }
  forBeneficiary: { text: "As a minimum for your honours degree, you should be able to cross the lines between subjects, using ideas from other disciplines to think about health issues.", rewrite: full, force: threshold, status: drafted }
  author-agent-written: "Present this as a threshold outcome in subject knowledge, understanding or skills for the bachelor's degree with honours at FHEQ level 6 (FQHEIS level 10): every graduate in the subject should show it, so it is the floor and not a mark of distinction. Cite it as QAA, 2024, Health Studies Subject Benchmark Statement, para 4.4 (item 18). Do not call it a regulatory requirement or claim it for master's awards, which have their own lists at 4.7 and 4.8. Set it beside 4.4.b4, the honours descriptor item qaa/fheq-2024/4.15.b6, Annex D's third-class column (qaa/fheq-2024/annex-d/summary/r1/3rd) and spine:6."
  author-agent-dialogue: "Bring it up when a student asks what an honours graduate must manage on working across disciplinary lines, or when a programme team checks module outcomes against the exit standard. With a student, put it plainly as a minimum to reach by graduation; with staff, ask where the course teaches and assesses it. Ask: Which other discipline has helped you most with a health issue, and how? Avoid reading the issuer's list aloud, and do not treat higher achievement as what the minimum demands."
- statement: qaa/health-studies-2024/4.4.b19
  forPractitioner: { text: "Teach and assess the course so that every honours graduate can analyse health issues across diverse populations in a joined-up way that takes account of equality, diversity and inclusion; this belongs to the minimum, not to the higher classes.", rewrite: light, force: threshold, status: drafted }
  forBeneficiary: { text: "As a minimum for your honours degree, you should be able to analyse health issues across diverse groups in a joined-up way, with equality, diversity and inclusion in mind.", rewrite: full, force: threshold, status: drafted }
  author-agent-written: "Present this as a threshold outcome in subject knowledge, understanding or skills for the bachelor's degree with honours at FHEQ level 6 (FQHEIS level 10): every graduate in the subject should show it, so it is the floor and not a mark of distinction. Cite it as QAA, 2024, Health Studies Subject Benchmark Statement, para 4.4 (item 19). Do not call it a regulatory requirement or claim it for master's awards, which have their own lists at 4.7 and 4.8. Set it beside 4.4.b16 and 4.5.b18, the honours descriptor item qaa/fheq-2024/4.15.b7, Annex D's third-class column (qaa/fheq-2024/annex-d/summary/r4/3rd) and spine:6."
  author-agent-dialogue: "Bring it up when a student asks what an honours graduate must manage on integrated analysis with EDI principles, or when a programme team checks module outcomes against the exit standard. With a student, put it plainly as a minimum to reach by graduation; with staff, ask where the course teaches and assesses it. Ask: In your last analysis, how did you check that it held for different groups? Avoid reading the issuer's list aloud, and do not treat higher achievement as what the minimum demands."
- statement: qaa/health-studies-2024/4.4.b20
  forPractitioner: { text: "Teach and assess the course so that every honours graduate can show they understand why social and psychological factors decide whether public health messages succeed; this belongs to the minimum, not to the higher classes.", rewrite: light, force: threshold, status: drafted }
  forBeneficiary: { text: "As a minimum for your honours degree, you should be able to show you understand why social and psychological factors decide whether public health messages work.", rewrite: full, force: threshold, status: drafted }
  author-agent-written: "Present this as a threshold outcome in subject knowledge, understanding or skills for the bachelor's degree with honours at FHEQ level 6 (FQHEIS level 10): every graduate in the subject should show it, so it is the floor and not a mark of distinction. Cite it as QAA, 2024, Health Studies Subject Benchmark Statement, para 4.4 (item 20). Do not call it a regulatory requirement or claim it for master's awards, which have their own lists at 4.7 and 4.8. Set it beside 4.5.b11, the honours descriptor item qaa/fheq-2024/4.15.b8, Annex D's third-class column (qaa/fheq-2024/annex-d/summary/r1/3rd) and spine:6."
  author-agent-dialogue: "Bring it up when a student asks what an honours graduate must manage on social and psychological sides of public health messages, or when a programme team checks module outcomes against the exit standard. With a student, put it plainly as a minimum to reach by graduation; with staff, ask where the course teaches and assesses it. Ask: Think of a public health message: why did it work, or fail, with its audience? Avoid reading the issuer's list aloud, and do not treat higher achievement as what the minimum demands."
- statement: qaa/health-studies-2024/4.4.b21
  forPractitioner: { text: "Teach and assess the course so that every honours graduate can weigh current questions and arguments in health research and debate; this belongs to the minimum, not to the higher classes.", rewrite: light, force: threshold, status: drafted }
  forBeneficiary: { text: "As a minimum for your honours degree, you should be able to think through current questions and arguments in health research.", rewrite: full, force: threshold, status: drafted }
  author-agent-written: "Present this as a threshold outcome in subject knowledge, understanding or skills for the bachelor's degree with honours at FHEQ level 6 (FQHEIS level 10): every graduate in the subject should show it, so it is the floor and not a mark of distinction. Cite it as QAA, 2024, Health Studies Subject Benchmark Statement, para 4.4 (item 21). Do not call it a regulatory requirement or claim it for master's awards, which have their own lists at 4.7 and 4.8. Set it beside 4.4.b17, the honours descriptor item qaa/fheq-2024/4.15.b3.2, Annex D's third-class column (qaa/fheq-2024/annex-d/summary/r1/3rd) and spine:6."
  author-agent-dialogue: "Bring it up when a student asks what an honours graduate must manage on current questions in health research, or when a programme team checks module outcomes against the exit standard. With a student, put it plainly as a minimum to reach by graduation; with staff, ask where the course teaches and assesses it. Ask: Which current debate in health research do you follow, and where do you stand? Avoid reading the issuer's list aloud, and do not treat higher achievement as what the minimum demands."
- statement: qaa/health-studies-2024/4.4.b22
  forPractitioner: { text: "Teach and assess the course so that every honours graduate can analyse the epidemiology and effects of communicable and non-communicable disease and show how regional, national and global surveillance systems collect health data; this belongs to the minimum, not to the higher classes.", rewrite: light, force: threshold, status: drafted }
  forBeneficiary: { text: "As a minimum for your honours degree, you should be able to analyse how communicable and non-communicable diseases spread and affect people, and understand how surveillance systems at regional, national and global level collect health data.", rewrite: full, force: threshold, status: drafted }
  author-agent-written: "Present this as a threshold outcome in subject knowledge, understanding or skills for the bachelor's degree with honours at FHEQ level 6 (FQHEIS level 10): every graduate in the subject should show it, so it is the floor and not a mark of distinction. Cite it as QAA, 2024, Health Studies Subject Benchmark Statement, para 4.4 (item 22). Do not call it a regulatory requirement or claim it for master's awards, which have their own lists at 4.7 and 4.8. Set it beside 4.4.b8, the honours descriptor item qaa/fheq-2024/4.15.b2, Annex D's third-class column (qaa/fheq-2024/annex-d/summary/r1/3rd) and spine:6."
  author-agent-dialogue: "Bring it up when a student asks what an honours graduate must manage on epidemiology and surveillance, or when a programme team checks module outcomes against the exit standard. With a student, put it plainly as a minimum to reach by graduation; with staff, ask where the course teaches and assesses it. Ask: Which surveillance data have you used, and what did they tell you about a disease? Avoid reading the issuer's list aloud, and do not treat higher achievement as what the minimum demands."
- statement: qaa/health-studies-2024/4.5.b1
  forPractitioner: { text: "Teach and assess the course so that every honours graduate can work well in varied, complex work or practice settings that show the many sides of the subject; this belongs to the minimum, not to the higher classes.", rewrite: light, force: threshold, status: drafted }
  forBeneficiary: { text: "As a minimum for your honours degree, you should be able to work well in different complex work or practice settings across health.", rewrite: full, force: threshold, status: drafted }
  author-agent-written: "Present this as a threshold generic skill for the bachelor's degree with honours at FHEQ level 6 (FQHEIS level 10): every graduate in the subject should show it, so it is the floor and not a mark of distinction. Cite it as QAA, 2024, Health Studies Subject Benchmark Statement, para 4.5 (item 1). Do not call it a regulatory requirement or claim it for master's awards, which have their own lists at 4.7 and 4.8. Set it beside 4.5.b8, the honours descriptor item qaa/fheq-2024/4.15.b9.2, Annex D's third-class column (qaa/fheq-2024/annex-d/summary/r2/3rd) and spine:6."
  author-agent-dialogue: "Bring it up when a student asks what an honours graduate must manage on working in complex settings, or when a programme team checks module outcomes against the exit standard. With a student, put it plainly as a minimum to reach by graduation; with staff, ask where the course teaches and assesses it. Ask: Which placement or work setting has tested you most, and how did you cope? Avoid reading the issuer's list aloud, and do not treat higher achievement as what the minimum demands."
- statement: qaa/health-studies-2024/4.5.b2
  forPractitioner: { text: "Teach and assess the course so that every honours graduate can work in a team and accept responsibility for their own and the group's results; this belongs to the minimum, not to the higher classes.", rewrite: light, force: threshold, status: drafted }
  forBeneficiary: { text: "As a minimum for your honours degree, you should be able to work in a team and take responsibility for your own part and for the group's results.", rewrite: full, force: threshold, status: drafted }
  author-agent-written: "Present this as a threshold generic skill for the bachelor's degree with honours at FHEQ level 6 (FQHEIS level 10): every graduate in the subject should show it, so it is the floor and not a mark of distinction. Cite it as QAA, 2024, Health Studies Subject Benchmark Statement, para 4.5 (item 2). Do not call it a regulatory requirement or claim it for master's awards, which have their own lists at 4.7 and 4.8. Set it beside 4.5.b1, the honours descriptor item qaa/fheq-2024/4.15.b9.1, Annex D's third-class column (qaa/fheq-2024/annex-d/summary/r2/3rd) and spine:6."
  author-agent-dialogue: "Bring it up when a student asks what an honours graduate must manage on teamwork and shared responsibility, or when a programme team checks module outcomes against the exit standard. With a student, put it plainly as a minimum to reach by graduation; with staff, ask where the course teaches and assesses it. Ask: In your last group task, what were you responsible for, and how did the group do? Avoid reading the issuer's list aloud, and do not treat higher achievement as what the minimum demands."
- statement: qaa/health-studies-2024/4.5.b3
  forPractitioner: { text: "Teach and assess the course so that every honours graduate can assemble information and material from several sources across typical areas of the subject; this belongs to the minimum, not to the higher classes.", rewrite: light, force: threshold, status: drafted }
  forBeneficiary: { text: "As a minimum for your honours degree, you should be able to pull together information from several sources across the main areas of health.", rewrite: full, force: threshold, status: drafted }
  author-agent-written: "Present this as a threshold generic skill for the bachelor's degree with honours at FHEQ level 6 (FQHEIS level 10): every graduate in the subject should show it, so it is the floor and not a mark of distinction. Cite it as QAA, 2024, Health Studies Subject Benchmark Statement, para 4.5 (item 3). Do not call it a regulatory requirement or claim it for master's awards, which have their own lists at 4.7 and 4.8. Set it beside 4.5.b7, the honours descriptor item qaa/fheq-2024/4.15.b5, Annex D's third-class column (qaa/fheq-2024/annex-d/summary/r1/3rd) and spine:6."
  author-agent-dialogue: "Bring it up when a student asks what an honours graduate must manage on drawing information together, or when a programme team checks module outcomes against the exit standard. With a student, put it plainly as a minimum to reach by graduation; with staff, ask where the course teaches and assesses it. Ask: For your last assignment, how many kinds of source did you combine? Avoid reading the issuer's list aloud, and do not treat higher achievement as what the minimum demands."
- statement: qaa/health-studies-2024/4.5.b4
  forPractitioner: { text: "Teach and assess the course so that every honours graduate can spot problems and suggest possible solutions where that fits; this belongs to the minimum, not to the higher classes.", rewrite: light, force: threshold, status: drafted }
  forBeneficiary: { text: "As a minimum for your honours degree, you should be able to spot problems and suggest ways to solve them.", rewrite: full, force: threshold, status: drafted }
  author-agent-written: "Present this as a threshold generic skill for the bachelor's degree with honours at FHEQ level 6 (FQHEIS level 10): every graduate in the subject should show it, so it is the floor and not a mark of distinction. Cite it as QAA, 2024, Health Studies Subject Benchmark Statement, para 4.5 (item 4). Do not call it a regulatory requirement or claim it for master's awards, which have their own lists at 4.7 and 4.8. Set it beside 4.4.b3, the honours descriptor item qaa/fheq-2024/4.15.b7, Annex D's third-class column (qaa/fheq-2024/annex-d/summary/r4/3rd) and spine:6."
  author-agent-dialogue: "Bring it up when a student asks what an honours graduate must manage on problems and possible solutions, or when a programme team checks module outcomes against the exit standard. With a student, put it plainly as a minimum to reach by graduation; with staff, ask where the course teaches and assesses it. Ask: What problem have you spotted recently, and what did you suggest? Avoid reading the issuer's list aloud, and do not treat higher achievement as what the minimum demands."
- statement: qaa/health-studies-2024/4.5.b5
  forPractitioner: { text: "Teach and assess the course so that every honours graduate can analyse factual information; this belongs to the minimum, not to the higher classes.", rewrite: light, force: threshold, status: drafted }
  forBeneficiary: { text: "As a minimum for your honours degree, you should be able to analyse factual information.", rewrite: full, force: threshold, status: drafted }
  author-agent-written: "Present this as a threshold generic skill for the bachelor's degree with honours at FHEQ level 6 (FQHEIS level 10): every graduate in the subject should show it, so it is the floor and not a mark of distinction. Cite it as QAA, 2024, Health Studies Subject Benchmark Statement, para 4.5 (item 5). Do not call it a regulatory requirement or claim it for master's awards, which have their own lists at 4.7 and 4.8. Set it beside 4.5.b17, the honours descriptor item qaa/fheq-2024/4.15.b7, Annex D's third-class column (qaa/fheq-2024/annex-d/summary/r4/3rd) and spine:6."
  author-agent-dialogue: "Bring it up when a student asks what an honours graduate must manage on analysing facts, or when a programme team checks module outcomes against the exit standard. With a student, put it plainly as a minimum to reach by graduation; with staff, ask where the course teaches and assesses it. Ask: Which facts or data have you analysed this term, and what did you conclude? Avoid reading the issuer's list aloud, and do not treat higher achievement as what the minimum demands."
- statement: qaa/health-studies-2024/4.5.b6
  forPractitioner: { text: "Teach and assess the course so that every honours graduate can see where other people's arguments are strong and where they are weak; this belongs to the minimum, not to the higher classes.", rewrite: light, force: threshold, status: drafted }
  forBeneficiary: { text: "As a minimum for your honours degree, you should be able to see where other people's arguments are strong and where they fall short.", rewrite: full, force: threshold, status: drafted }
  author-agent-written: "Present this as a threshold generic skill for the bachelor's degree with honours at FHEQ level 6 (FQHEIS level 10): every graduate in the subject should show it, so it is the floor and not a mark of distinction. Cite it as QAA, 2024, Health Studies Subject Benchmark Statement, para 4.5 (item 6). Do not call it a regulatory requirement or claim it for master's awards, which have their own lists at 4.7 and 4.8. Set it beside 4.4.b14, the honours descriptor item qaa/fheq-2024/4.15.b7, Annex D's third-class column (qaa/fheq-2024/annex-d/summary/r4/3rd) and spine:6."
  author-agent-dialogue: "Bring it up when a student asks what an honours graduate must manage on judging others' arguments, or when a programme team checks module outcomes against the exit standard. With a student, put it plainly as a minimum to reach by graduation; with staff, ask where the course teaches and assesses it. Ask: Which argument in your reading did you find weakest, and why? Avoid reading the issuer's list aloud, and do not treat higher achievement as what the minimum demands."
- statement: qaa/health-studies-2024/4.5.b7
  forPractitioner: { text: "Teach and assess the course so that every honours graduate can with guidance, write a synthesis of what is known on a given subject or topic; this belongs to the minimum, not to the higher classes.", rewrite: light, force: threshold, status: drafted }
  forBeneficiary: { text: "As a minimum for your honours degree, you should be able to with guidance, write a summary that brings together what is known on a topic.", rewrite: full, force: threshold, status: drafted }
  author-agent-written: "Present this as a threshold generic skill for the bachelor's degree with honours at FHEQ level 6 (FQHEIS level 10): every graduate in the subject should show it, so it is the floor and not a mark of distinction. Cite it as QAA, 2024, Health Studies Subject Benchmark Statement, para 4.5 (item 7). Do not call it a regulatory requirement or claim it for master's awards, which have their own lists at 4.7 and 4.8. Set it beside 4.5.b3, the honours descriptor item qaa/fheq-2024/4.15.b5, Annex D's third-class column (qaa/fheq-2024/annex-d/summary/r1/3rd) and spine:6."
  author-agent-dialogue: "Bring it up when a student asks what an honours graduate must manage on summing up current knowledge with guidance, or when a programme team checks module outcomes against the exit standard. With a student, put it plainly as a minimum to reach by graduation; with staff, ask where the course teaches and assesses it. Ask: Have you written a review of what is known on a topic, and how much help did you need? Avoid reading the issuer's list aloud, and do not treat higher achievement as what the minimum demands."
- statement: qaa/health-studies-2024/4.5.b8
  forPractitioner: { text: "Teach and assess the course so that every honours graduate can carry out tasks on their own; this belongs to the minimum, not to the higher classes.", rewrite: light, force: threshold, status: drafted }
  forBeneficiary: { text: "As a minimum for your honours degree, you should be able to carry out tasks on your own.", rewrite: full, force: threshold, status: drafted }
  author-agent-written: "Present this as a threshold generic skill for the bachelor's degree with honours at FHEQ level 6 (FQHEIS level 10): every graduate in the subject should show it, so it is the floor and not a mark of distinction. Cite it as QAA, 2024, Health Studies Subject Benchmark Statement, para 4.5 (item 8). Do not call it a regulatory requirement or claim it for master's awards, which have their own lists at 4.7 and 4.8. Set it beside 4.5.b2, the honours descriptor item qaa/fheq-2024/4.15.b9.1, Annex D's third-class column (qaa/fheq-2024/annex-d/summary/r2/3rd) and spine:6."
  author-agent-dialogue: "Bring it up when a student asks what an honours graduate must manage on working independently, or when a programme team checks module outcomes against the exit standard. With a student, put it plainly as a minimum to reach by graduation; with staff, ask where the course teaches and assesses it. Ask: Which piece of work have you done with little or no direction? Avoid reading the issuer's list aloud, and do not treat higher achievement as what the minimum demands."
- statement: qaa/health-studies-2024/4.5.b9
  forPractitioner: { text: "Teach and assess the course so that every honours graduate can reflect critically on their own progress and use feedback from different sources; this belongs to the minimum, not to the higher classes.", rewrite: light, force: threshold, status: drafted }
  forBeneficiary: { text: "As a minimum for your honours degree, you should be able to reflect critically on your progress and act on feedback from different people.", rewrite: full, force: threshold, status: drafted }
  author-agent-written: "Present this as a threshold generic skill for the bachelor's degree with honours at FHEQ level 6 (FQHEIS level 10): every graduate in the subject should show it, so it is the floor and not a mark of distinction. Cite it as QAA, 2024, Health Studies Subject Benchmark Statement, para 4.5 (item 9). Do not call it a regulatory requirement or claim it for master's awards, which have their own lists at 4.7 and 4.8. Set it beside 3.10.b5, the honours descriptor item qaa/fheq-2024/4.15.b9.3, Annex D's third-class column (qaa/fheq-2024/annex-d/summary/r3/3rd) and spine:6."
  author-agent-dialogue: "Bring it up when a student asks what an honours graduate must manage on reflection and acting on feedback, or when a programme team checks module outcomes against the exit standard. With a student, put it plainly as a minimum to reach by graduation; with staff, ask where the course teaches and assesses it. Ask: What feedback have you acted on recently, and what changed as a result? Avoid reading the issuer's list aloud, and do not treat higher achievement as what the minimum demands."
- statement: qaa/health-studies-2024/4.5.b10
  forPractitioner: { text: "Teach and assess the course so that every honours graduate can communicate clearly in modes suited to the situation: spoken, non-verbal and digital; this belongs to the minimum, not to the higher classes.", rewrite: light, force: threshold, status: drafted }
  forBeneficiary: { text: "As a minimum for your honours degree, you should be able to communicate clearly in ways that suit the situation, in speech, body language and digital media.", rewrite: full, force: threshold, status: drafted }
  author-agent-written: "Present this as a threshold generic skill for the bachelor's degree with honours at FHEQ level 6 (FQHEIS level 10): every graduate in the subject should show it, so it is the floor and not a mark of distinction. Cite it as QAA, 2024, Health Studies Subject Benchmark Statement, para 4.5 (item 10). Do not call it a regulatory requirement or claim it for master's awards, which have their own lists at 4.7 and 4.8. Set it beside 4.5.b12, the honours descriptor item qaa/fheq-2024/4.15.b8, Annex D's third-class column (qaa/fheq-2024/annex-d/summary/r1/3rd) and spine:6."
  author-agent-dialogue: "Bring it up when a student asks what an honours graduate must manage on clear communication in several modes, or when a programme team checks module outcomes against the exit standard. With a student, put it plainly as a minimum to reach by graduation; with staff, ask where the course teaches and assesses it. Ask: Which modes of communication have you used in assessed work so far? Avoid reading the issuer's list aloud, and do not treat higher achievement as what the minimum demands."
- statement: qaa/health-studies-2024/4.5.b11
  forPractitioner: { text: "Teach and assess the course so that every honours graduate can recognise how spoken and non-verbal communication help promote health, and apply equality, diversity and inclusion principles across every channel; this belongs to the minimum, not to the higher classes.", rewrite: light, force: threshold, status: drafted }
  forBeneficiary: { text: "As a minimum for your honours degree, you should be able to recognise how spoken and unspoken communication can promote health, and keep your communication inclusive in every channel.", rewrite: full, force: threshold, status: drafted }
  author-agent-written: "Present this as a threshold generic skill for the bachelor's degree with honours at FHEQ level 6 (FQHEIS level 10): every graduate in the subject should show it, so it is the floor and not a mark of distinction. Cite it as QAA, 2024, Health Studies Subject Benchmark Statement, para 4.5 (item 11). Do not call it a regulatory requirement or claim it for master's awards, which have their own lists at 4.7 and 4.8. Set it beside 4.4.b20, the honours descriptor item qaa/fheq-2024/4.15.b8, Annex D's third-class column (qaa/fheq-2024/annex-d/summary/r1/3rd) and spine:6."
  author-agent-dialogue: "Bring it up when a student asks what an honours graduate must manage on communication for health promotion and EDI, or when a programme team checks module outcomes against the exit standard. With a student, put it plainly as a minimum to reach by graduation; with staff, ask where the course teaches and assesses it. Ask: How would you adapt a health message so it reaches and respects different groups? Avoid reading the issuer's list aloud, and do not treat higher achievement as what the minimum demands."
- statement: qaa/health-studies-2024/4.5.b12
  forPractitioner: { text: "Teach and assess the course so that every honours graduate can put knowledge or an argument across so that others can follow it; this belongs to the minimum, not to the higher classes.", rewrite: light, force: threshold, status: drafted }
  forBeneficiary: { text: "As a minimum for your honours degree, you should be able to put across what you know, or an argument, so that others can follow it.", rewrite: full, force: threshold, status: drafted }
  author-agent-written: "Present this as a threshold generic skill for the bachelor's degree with honours at FHEQ level 6 (FQHEIS level 10): every graduate in the subject should show it, so it is the floor and not a mark of distinction. Cite it as QAA, 2024, Health Studies Subject Benchmark Statement, para 4.5 (item 12). Do not call it a regulatory requirement or claim it for master's awards, which have their own lists at 4.7 and 4.8. Set it beside 4.5.b10, the honours descriptor item qaa/fheq-2024/4.15.b8, Annex D's third-class column (qaa/fheq-2024/annex-d/summary/r1/3rd) and spine:6."
  author-agent-dialogue: "Bring it up when a student asks what an honours graduate must manage on making knowledge understandable, or when a programme team checks module outcomes against the exit standard. With a student, put it plainly as a minimum to reach by graduation; with staff, ask where the course teaches and assesses it. Ask: Who outside your course could follow your last piece of work, and how do you know? Avoid reading the issuer's list aloud, and do not treat higher achievement as what the minimum demands."
- statement: qaa/health-studies-2024/4.5.b13
  forPractitioner: { text: "Teach and assess the course so that every honours graduate can use suitable IT to gather, analyse, choose and present information, showing digital literacy; this belongs to the minimum, not to the higher classes.", rewrite: light, force: threshold, status: drafted }
  forBeneficiary: { text: "As a minimum for your honours degree, you should be able to use suitable digital tools to gather, analyse, choose and present information.", rewrite: full, force: threshold, status: drafted }
  author-agent-written: "Present this as a threshold generic skill for the bachelor's degree with honours at FHEQ level 6 (FQHEIS level 10): every graduate in the subject should show it, so it is the floor and not a mark of distinction. Cite it as QAA, 2024, Health Studies Subject Benchmark Statement, para 4.5 (item 13). Do not call it a regulatory requirement or claim it for master's awards, which have their own lists at 4.7 and 4.8. Set it beside 4.5.b14 and 1.43, the honours descriptor item qaa/fheq-2024/4.15.b2, Annex D's third-class column (qaa/fheq-2024/annex-d/summary/r1/3rd) and spine:6."
  author-agent-dialogue: "Bring it up when a student asks what an honours graduate must manage on IT and digital literacy, or when a programme team checks module outcomes against the exit standard. With a student, put it plainly as a minimum to reach by graduation; with staff, ask where the course teaches and assesses it. Ask: Which digital tools do you use to handle information, and how confident are you with them? Avoid reading the issuer's list aloud, and do not treat higher achievement as what the minimum demands."
- statement: qaa/health-studies-2024/4.5.b14
  forPractitioner: { text: "Teach and assess the course so that every honours graduate can recognise what AI and other technologies do in health; this belongs to the minimum, not to the higher classes.", rewrite: light, force: threshold, status: drafted }
  forBeneficiary: { text: "As a minimum for your honours degree, you should be able to recognise what artificial intelligence and other technologies do in health.", rewrite: full, force: threshold, status: drafted }
  author-agent-written: "Present this as a threshold generic skill for the bachelor's degree with honours at FHEQ level 6 (FQHEIS level 10): every graduate in the subject should show it, so it is the floor and not a mark of distinction. Cite it as QAA, 2024, Health Studies Subject Benchmark Statement, para 4.5 (item 14). Do not call it a regulatory requirement or claim it for master's awards, which have their own lists at 4.7 and 4.8. Set it beside 3.7.b3 and 3.7.b4, the honours descriptor item qaa/fheq-2024/4.15.b4, Annex D's third-class column (qaa/fheq-2024/annex-d/summary/r1/3rd) and spine:6."
  author-agent-dialogue: "Bring it up when a student asks what an honours graduate must manage on AI and technology in health, or when a programme team checks module outcomes against the exit standard. With a student, put it plainly as a minimum to reach by graduation; with staff, ask where the course teaches and assesses it. Ask: Where have you seen AI used in health, and what were its limits? Avoid reading the issuer's list aloud, and do not treat higher achievement as what the minimum demands."
- statement: qaa/health-studies-2024/4.5.b15
  forPractitioner: { text: "Teach and assess the course so that every honours graduate can show they can listen to and understand new ideas or information; this belongs to the minimum, not to the higher classes.", rewrite: light, force: threshold, status: drafted }
  forBeneficiary: { text: "As a minimum for your honours degree, you should be able to show you can listen to and make sense of new ideas or information.", rewrite: full, force: threshold, status: drafted }
  author-agent-written: "Present this as a threshold generic skill for the bachelor's degree with honours at FHEQ level 6 (FQHEIS level 10): every graduate in the subject should show it, so it is the floor and not a mark of distinction. Cite it as QAA, 2024, Health Studies Subject Benchmark Statement, para 4.5 (item 15). Do not call it a regulatory requirement or claim it for master's awards, which have their own lists at 4.7 and 4.8. Set it beside 4.5.b12, the honours descriptor item qaa/fheq-2024/4.15.b5, Annex D's third-class column (qaa/fheq-2024/annex-d/summary/r3/3rd) and spine:6."
  author-agent-dialogue: "Bring it up when a student asks what an honours graduate must manage on listening and comprehension, or when a programme team checks module outcomes against the exit standard. With a student, put it plainly as a minimum to reach by graduation; with staff, ask where the course teaches and assesses it. Ask: When did you last change your mind after hearing a new idea? Avoid reading the issuer's list aloud, and do not treat higher achievement as what the minimum demands."
- statement: qaa/health-studies-2024/4.5.b16
  forPractitioner: { text: "Teach and assess the course so that every honours graduate can show skill in identifying and describing material; this belongs to the minimum, not to the higher classes.", rewrite: light, force: threshold, status: drafted }
  forBeneficiary: { text: "As a minimum for your honours degree, you should be able to show you can identify and describe material accurately.", rewrite: full, force: threshold, status: drafted }
  author-agent-written: "Present this as a threshold generic skill for the bachelor's degree with honours at FHEQ level 6 (FQHEIS level 10): every graduate in the subject should show it, so it is the floor and not a mark of distinction. Cite it as QAA, 2024, Health Studies Subject Benchmark Statement, para 4.5 (item 16). Do not call it a regulatory requirement or claim it for master's awards, which have their own lists at 4.7 and 4.8. Set it beside 4.5.b17, the honours descriptor item qaa/fheq-2024/4.15.b3.2, Annex D's third-class column (qaa/fheq-2024/annex-d/summary/r1/3rd) and spine:6."
  author-agent-dialogue: "Bring it up when a student asks what an honours graduate must manage on identifying and describing material, or when a programme team checks module outcomes against the exit standard. With a student, put it plainly as a minimum to reach by graduation; with staff, ask where the course teaches and assesses it. Ask: Can you describe a source you used in a few accurate sentences? Avoid reading the issuer's list aloud, and do not treat higher achievement as what the minimum demands."
- statement: qaa/health-studies-2024/4.5.b17
  forPractitioner: { text: "Teach and assess the course so that every honours graduate can show skill in describing, sorting and gathering data; this belongs to the minimum, not to the higher classes.", rewrite: light, force: threshold, status: drafted }
  forBeneficiary: { text: "As a minimum for your honours degree, you should be able to show you can describe, sort and gather data.", rewrite: full, force: threshold, status: drafted }
  author-agent-written: "Present this as a threshold generic skill for the bachelor's degree with honours at FHEQ level 6 (FQHEIS level 10): every graduate in the subject should show it, so it is the floor and not a mark of distinction. Cite it as QAA, 2024, Health Studies Subject Benchmark Statement, para 4.5 (item 17). Do not call it a regulatory requirement or claim it for master's awards, which have their own lists at 4.7 and 4.8. Set it beside 4.5.b5, the honours descriptor item qaa/fheq-2024/4.15.b6, Annex D's third-class column (qaa/fheq-2024/annex-d/summary/r1/3rd) and spine:6."
  author-agent-dialogue: "Bring it up when a student asks what an honours graduate must manage on handling data, or when a programme team checks module outcomes against the exit standard. With a student, put it plainly as a minimum to reach by graduation; with staff, ask where the course teaches and assesses it. Ask: How did you organise the data in your last project? Avoid reading the issuer's list aloud, and do not treat higher achievement as what the minimum demands."
- statement: qaa/health-studies-2024/4.5.b18
  forPractitioner: { text: "Teach and assess the course so that every honours graduate can understand why health and safety and equality, diversity and inclusiveness matter at work; this belongs to the minimum, not to the higher classes.", rewrite: light, force: threshold, status: drafted }
  forBeneficiary: { text: "As a minimum for your honours degree, you should be able to understand why health and safety and equality, diversity and inclusion matter in the workplace.", rewrite: full, force: threshold, status: drafted }
  author-agent-written: "Present this as a threshold generic skill for the bachelor's degree with honours at FHEQ level 6 (FQHEIS level 10): every graduate in the subject should show it, so it is the floor and not a mark of distinction. Cite it as QAA, 2024, Health Studies Subject Benchmark Statement, para 4.5 (item 18). Do not call it a regulatory requirement or claim it for master's awards, which have their own lists at 4.7 and 4.8. Set it beside 4.4.b19, the honours descriptor item qaa/fheq-2024/4.15.b9.1, Annex D's third-class column (qaa/fheq-2024/annex-d/summary/r2/3rd) and spine:6."
  author-agent-dialogue: "Bring it up when a student asks what an honours graduate must manage on health and safety and EDI at work, or when a programme team checks module outcomes against the exit standard. With a student, put it plainly as a minimum to reach by graduation; with staff, ask where the course teaches and assesses it. Ask: What would you check first on health and safety and on inclusion in a new workplace? Avoid reading the issuer's list aloud, and do not treat higher achievement as what the minimum demands."
- statement: qaa/health-studies-2024/4.5.b19
  forPractitioner: { text: "Teach and assess the course so that every honours graduate can understand and take part in current debates on global sustainability and employability; this belongs to the minimum, not to the higher classes.", rewrite: light, force: threshold, status: drafted }
  forBeneficiary: { text: "As a minimum for your honours degree, you should be able to follow and take part in current debates on global sustainability and on work.", rewrite: full, force: threshold, status: drafted }
  author-agent-written: "Present this as a threshold generic skill for the bachelor's degree with honours at FHEQ level 6 (FQHEIS level 10): every graduate in the subject should show it, so it is the floor and not a mark of distinction. Cite it as QAA, 2024, Health Studies Subject Benchmark Statement, para 4.5 (item 19). Do not call it a regulatory requirement or claim it for master's awards, which have their own lists at 4.7 and 4.8. Set it beside 1.31.b6 and 1.37, the honours descriptor item qaa/fheq-2024/4.15.b9.3, Annex D's third-class column (qaa/fheq-2024/annex-d/summary/r2/3rd) and spine:6."
  author-agent-dialogue: "Bring it up when a student asks what an honours graduate must manage on debates on sustainability and employability, or when a programme team checks module outcomes against the exit standard. With a student, put it plainly as a minimum to reach by graduation; with staff, ask where the course teaches and assesses it. Ask: Which debate on sustainability and health have you joined, and what did you argue? Avoid reading the issuer's list aloud, and do not treat higher achievement as what the minimum demands."
- statement: qaa/health-studies-2024/4.5.b20
  forPractitioner: { text: "Teach and assess the course so that every honours graduate can bring a thorough grasp of ethical questions and professional conduct codes to their work in the subject; this belongs to the minimum, not to the higher classes.", rewrite: light, force: threshold, status: drafted }
  forBeneficiary: { text: "As a minimum for your honours degree, you should be able to apply a thorough grasp of ethics and professional codes of conduct in your work.", rewrite: full, force: threshold, status: drafted }
  author-agent-written: "Present this as a threshold generic skill for the bachelor's degree with honours at FHEQ level 6 (FQHEIS level 10): every graduate in the subject should show it, so it is the floor and not a mark of distinction. Cite it as QAA, 2024, Health Studies Subject Benchmark Statement, para 4.5 (item 20). Do not call it a regulatory requirement or claim it for master's awards, which have their own lists at 4.7 and 4.8. Set it beside 4.4.b15, the honours descriptor item qaa/fheq-2024/4.15.b9.3, Annex D's third-class column (qaa/fheq-2024/annex-d/summary/r2/3rd) and spine:6."
  author-agent-dialogue: "Bring it up when a student asks what an honours graduate must manage on ethics and professional codes, or when a programme team checks module outcomes against the exit standard. With a student, put it plainly as a minimum to reach by graduation; with staff, ask where the course teaches and assesses it. Ask: Which professional code applies to the work you want to do, and what does it ask of you? Avoid reading the issuer's list aloud, and do not treat higher achievement as what the minimum demands."
- statement: qaa/health-studies-2024/4.6
  forPractitioner: { text: "Use the master's lists as a reference point when designing postgraduate certificates and diplomas in the subject.", rewrite: light, force: should, status: drafted }
  forBeneficiary: { text: "not-applicable: a duty on the course team or provider; the student meets its effect, not a standard to reach", rewrite: full, force: should, status: drafted }
  author-agent-written: "Describe this as a duty on the course team or provider, stated with 'should': a firm recommendation that leaves room for the provider's judgement; it sets no outcome a student must show and carries no level. Cite it as QAA, 2024, Health Studies Subject Benchmark Statement, para 4.6. Do not present it as a statutory or regulatory requirement. Set it beside 4.7, 4.8 and qaa/fheq-2024/4.17.i2."
  author-agent-dialogue: "Raise it with a programme team or reviewer when a team designs a postgraduate certificate or diploma in health. Frame it for staff as a check on course design or review and ask: Which master's outcomes does the shorter award draw on, and which does it leave out? Do not hand it to a student as their task or quote the paragraph at length."
- statement: qaa/health-studies-2024/4.7.b1
  forPractitioner: { text: "Design and assess the master's course so that every graduate can show a systematic grasp of the field and a critical, up-to-date sense of today's health problems and fresh insights, much of it drawn from or at the leading edge of their discipline or practice; this is the level 7 floor.", rewrite: light, force: threshold, status: drafted }
  forBeneficiary: { text: "As a minimum for your master's degree, you should be able to show a systematic grasp of your field and a critical sense of today's health problems and fresh insights, much of it at or near the leading edge.", rewrite: full, force: threshold, status: drafted }
  author-agent-written: "Present this as a threshold outcome for the master's degree at FHEQ level 7 (FQHEIS level 11); para 4.6 also makes the master's lists a reference point for postgraduate certificates and diplomas. Cite it as QAA, 2024, Health Studies Subject Benchmark Statement, para 4.7 (item 1). Do not claim it as an honours outcome or a regulatory requirement, and note that the issuer's wording follows the FHEQ master's descriptor closely. Set it beside 4.7.b2 and 4.4.b2, qaa/fheq-2024/4.17.b1 and spine:7."
  author-agent-dialogue: "Raise it when a master's student or team asks what the degree must show on systematic understanding and critical awareness. Speak to a student in the second person about the minimum for the award; with staff, ask which module assesses it at level 7. Ask: Which current problem in your field could you explain at the level of the latest research? Avoid reciting the descriptor and do not present it as an honours expectation."
- statement: qaa/health-studies-2024/4.7.b2
  forPractitioner: { text: "Design and assess the master's course so that every graduate can show full understanding of the techniques that suit their own research or advanced study; this is the level 7 floor.", rewrite: light, force: threshold, status: drafted }
  forBeneficiary: { text: "As a minimum for your master's degree, you should be able to show you fully understand the techniques that fit your own research or advanced study.", rewrite: full, force: threshold, status: drafted }
  author-agent-written: "Present this as a threshold outcome for the master's degree at FHEQ level 7 (FQHEIS level 11); para 4.6 also makes the master's lists a reference point for postgraduate certificates and diplomas. Cite it as QAA, 2024, Health Studies Subject Benchmark Statement, para 4.7 (item 2). Do not claim it as an honours outcome or a regulatory requirement, and note that the issuer's wording follows the FHEQ master's descriptor closely. Set it beside 4.7.b3, qaa/fheq-2024/4.17.b2 and spine:7."
  author-agent-dialogue: "Raise it when a master's student or team asks what the degree must show on research techniques. Speak to a student in the second person about the minimum for the award; with staff, ask which module assesses it at level 7. Ask: Which methods suit your own research question, and why those rather than others? Avoid reciting the descriptor and do not present it as an honours expectation."
- statement: qaa/health-studies-2024/4.7.b3
  forPractitioner: { text: "Design and assess the master's course so that every graduate can apply knowledge with originality and understand in practice how established research techniques produce and interpret knowledge in the discipline; this is the level 7 floor.", rewrite: light, force: threshold, status: drafted }
  forBeneficiary: { text: "As a minimum for your master's degree, you should be able to apply what you know in original ways and understand how research methods build and interpret knowledge in your field.", rewrite: full, force: threshold, status: drafted }
  author-agent-written: "Present this as a threshold outcome for the master's degree at FHEQ level 7 (FQHEIS level 11); para 4.6 also makes the master's lists a reference point for postgraduate certificates and diplomas. Cite it as QAA, 2024, Health Studies Subject Benchmark Statement, para 4.7 (item 3). Do not claim it as an honours outcome or a regulatory requirement, and note that the issuer's wording follows the FHEQ master's descriptor closely. Set it beside 4.7.b2 and 4.8.b3, qaa/fheq-2024/4.17.b3 and spine:7."
  author-agent-dialogue: "Raise it when a master's student or team asks what the degree must show on originality and how research makes knowledge. Speak to a student in the second person about the minimum for the award; with staff, ask which module assesses it at level 7. Ask: Where in your work have you applied knowledge in a way your sources did not? Avoid reciting the descriptor and do not present it as an honours expectation."
- statement: qaa/health-studies-2024/4.7.b4
  forPractitioner: { text: "Design and assess the master's course so that every graduate can hold a conceptual understanding that lets them critique current research, advanced scholarship and methods, form critiques and, where fitting, put forward new hypotheses; this is the level 7 floor.", rewrite: light, force: threshold, status: drafted }
  forBeneficiary: { text: "As a minimum for your master's degree, you should be able to understand ideas well enough to critique current research and its methods and, where it fits, suggest new hypotheses.", rewrite: full, force: threshold, status: drafted }
  author-agent-written: "Present this as a threshold outcome for the master's degree at FHEQ level 7 (FQHEIS level 11); para 4.6 also makes the master's lists a reference point for postgraduate certificates and diplomas. Cite it as QAA, 2024, Health Studies Subject Benchmark Statement, para 4.7 (item 4). Do not claim it as an honours outcome or a regulatory requirement, and note that the issuer's wording follows the FHEQ master's descriptor closely. Set it beside 4.7.b1 and 4.4.b21, qaa/fheq-2024/4.17.b4.1 and spine:7."
  author-agent-dialogue: "Raise it when a master's student or team asks what the degree must show on critical evaluation of research and methods. Speak to a student in the second person about the minimum for the award; with staff, ask which module assesses it at level 7. Ask: Which study in your area would you challenge, and what hypothesis would you test instead? Avoid reciting the descriptor and do not present it as an honours expectation."
- statement: qaa/health-studies-2024/4.8.b1
  forPractitioner: { text: "Expect most master's graduates to handle complex health issues systematically and creatively and manage uncertainty in a changing field, and give them chances to show it; it describes typical holders, above the 4.7 minimum.", rewrite: light, force: will, status: drafted }
  forBeneficiary: { text: "By the end of a master's, you will typically be able to handle complex health issues in a systematic and creative way and cope with uncertainty in a changing field.", rewrite: full, force: will, status: drafted }
  author-agent-written: "Present this as a typical expectation of master's holders at FHEQ level 7 (FQHEIS level 11), led in with 'Typically' and 'will': it describes most graduates, not the minimum every graduate must reach. Cite it as QAA, 2024, Health Studies Subject Benchmark Statement, para 4.8 (item 1). Do not write it into a programme as a pass condition, and do not claim it for honours. Set it beside 4.8.b2 and 4.5.b1, qaa/fheq-2024/4.17.b5 and spine:7."
  author-agent-dialogue: "Bring it up when a master's student wants to know what a strong, typical graduate can do on complex issues and uncertainty, or when staff plan stretch in a module. Speak to a student in the second person; with staff, frame it as what most of the cohort should reach. Ask: Which complex health issue have you worked through, and how did you handle what was unknown? Do not present it as the minimum for the award."
- statement: qaa/health-studies-2024/4.8.b2
  forPractitioner: { text: "Expect most master's graduates to make sound judgements when health data are incomplete and explain their conclusions clearly to specialists and non-specialists, and give them chances to show it; it describes typical holders, above the 4.7 minimum.", rewrite: light, force: will, status: drafted }
  forBeneficiary: { text: "By the end of a master's, you will typically be able to make sound judgements when the health data are incomplete, and explain your conclusions clearly to experts and non-experts.", rewrite: full, force: will, status: drafted }
  author-agent-written: "Present this as a typical expectation of master's holders at FHEQ level 7 (FQHEIS level 11), led in with 'Typically' and 'will': it describes most graduates, not the minimum every graduate must reach. Cite it as QAA, 2024, Health Studies Subject Benchmark Statement, para 4.8 (item 2). Do not write it into a programme as a pass condition, and do not claim it for honours. Set it beside 4.8.b1 and 4.5.b12, qaa/fheq-2024/4.17.b5 and spine:7."
  author-agent-dialogue: "Bring it up when a master's student wants to know what a strong, typical graduate can do on judgement with incomplete data, or when staff plan stretch in a module. Speak to a student in the second person; with staff, frame it as what most of the cohort should reach. Ask: When did you last decide something without all the data, and how did you explain it? Do not present it as the minimum for the award."
- statement: qaa/health-studies-2024/4.8.b3
  forPractitioner: { text: "Expect most master's graduates to direct themselves, solve problems with originality and act on their own in planning and carrying out tasks at professional level, and give them chances to show it; it describes typical holders, above the 4.7 minimum.", rewrite: light, force: will, status: drafted }
  forBeneficiary: { text: "By the end of a master's, you will typically be able to direct yourself, solve problems with originality and plan and carry out tasks on your own at a professional level.", rewrite: full, force: will, status: drafted }
  author-agent-written: "Present this as a typical expectation of master's holders at FHEQ level 7 (FQHEIS level 11), led in with 'Typically' and 'will': it describes most graduates, not the minimum every graduate must reach. Cite it as QAA, 2024, Health Studies Subject Benchmark Statement, para 4.8 (item 3). Do not write it into a programme as a pass condition, and do not claim it for honours. Set it beside 4.7.b3 and 4.5.b8, qaa/fheq-2024/4.17.b6 and spine:7."
  author-agent-dialogue: "Bring it up when a master's student wants to know what a strong, typical graduate can do on self-direction and autonomy, or when staff plan stretch in a module. Speak to a student in the second person; with staff, frame it as what most of the cohort should reach. Ask: Which task have you planned and carried through entirely on your own? Do not present it as the minimum for the award."
- statement: qaa/health-studies-2024/4.8.b4
  forPractitioner: { text: "Expect most master's graduates to keep advancing their knowledge and understanding and build new skills to a higher level, and give them chances to show it; it describes typical holders, above the 4.7 minimum.", rewrite: light, force: will, status: drafted }
  forBeneficiary: { text: "By the end of a master's, you will typically be able to keep extending what you know and building new skills to a higher level.", rewrite: full, force: will, status: drafted }
  author-agent-written: "Present this as a typical expectation of master's holders at FHEQ level 7 (FQHEIS level 11), led in with 'Typically' and 'will': it describes most graduates, not the minimum every graduate must reach. Cite it as QAA, 2024, Health Studies Subject Benchmark Statement, para 4.8 (item 4). Do not write it into a programme as a pass condition, and do not claim it for honours. Set it beside 4.8.b6, qaa/fheq-2024/4.17.b7 and spine:7."
  author-agent-dialogue: "Bring it up when a master's student wants to know what a strong, typical graduate can do on continuing to advance knowledge and skills, or when staff plan stretch in a module. Speak to a student in the second person; with staff, frame it as what most of the cohort should reach. Ask: What new skill are you building now, and how will you know it has reached a higher level? Do not present it as the minimum for the award."
- statement: qaa/health-studies-2024/4.8.b5
  forPractitioner: { text: "Expect most master's graduates to take initiative and personal responsibility and make decisions in complex, unpredictable situations, professional ones included, and give them chances to show it; it describes typical holders, above the 4.7 minimum.", rewrite: light, force: will, status: drafted }
  forBeneficiary: { text: "By the end of a master's, you will typically be able to take the initiative, take responsibility and make decisions in complex, unpredictable situations, including at work.", rewrite: full, force: will, status: drafted }
  author-agent-written: "Present this as a typical expectation of master's holders at FHEQ level 7 (FQHEIS level 11), led in with 'Typically' and 'will': it describes most graduates, not the minimum every graduate must reach. Cite it as QAA, 2024, Health Studies Subject Benchmark Statement, para 4.8 (item 5). Do not write it into a programme as a pass condition, and do not claim it for honours. Set it beside 4.8.b3 and 4.5.b1, qaa/fheq-2024/4.17.b8.2 and spine:7."
  author-agent-dialogue: "Bring it up when a master's student wants to know what a strong, typical graduate can do on initiative and decisions in complex situations, or when staff plan stretch in a module. Speak to a student in the second person; with staff, frame it as what most of the cohort should reach. Ask: Describe a time you had to decide something while the situation kept changing. Do not present it as the minimum for the award."
- statement: qaa/health-studies-2024/4.8.b6
  forPractitioner: { text: "Expect most master's graduates to learn independently in the way continuing professional development needs, and give them chances to show it; it describes typical holders, above the 4.7 minimum.", rewrite: light, force: will, status: drafted }
  forBeneficiary: { text: "By the end of a master's, you will typically be able to learn independently in the way that continuing professional development needs.", rewrite: full, force: will, status: drafted }
  author-agent-written: "Present this as a typical expectation of master's holders at FHEQ level 7 (FQHEIS level 11), led in with 'Typically' and 'will': it describes most graduates, not the minimum every graduate must reach. Cite it as QAA, 2024, Health Studies Subject Benchmark Statement, para 4.8 (item 6). Do not write it into a programme as a pass condition, and do not claim it for honours. Set it beside 4.8.b4 and 4.5.b9, qaa/fheq-2024/4.17.b8.3 and spine:7."
  author-agent-dialogue: "Bring it up when a master's student wants to know what a strong, typical graduate can do on independent learning for professional development, or when staff plan stretch in a module. Speak to a student in the second person; with staff, frame it as what most of the cohort should reach. Ask: How will you plan your own learning once no course sets it for you? Do not present it as the minimum for the award."
```

### S5 Levels and alignment
<!-- label: both; status: drafted; basis: primary -->
```yaml
levels:
  - { id: "fheq:6", role: "cites", locator: "D1, 2.10; 4.3 (as Level 6)" }
  - { id: "fqheis:10", role: "cites", locator: "D1, 2.10" }
  - { id: "fheq:7", role: "cites", locator: "D1, 2.15; 4.6; 4.3 (as Level 7)" }
  - { id: "fqheis:11", role: "cites", locator: "D1, 2.15; 4.6" }
  - { id: "spine:6", role: "refers (inferred)", locator: "std:ref:uk-framework R2, R8: the step for honours standards" }
  - { id: "spine:7", role: "refers (inferred)", locator: "std:ref:uk-framework R2, R8: the step for master's standards" }
crosswalks:
  - { from: "fheq:6", to: "fqheis:10", relation: "equivalent", basis: "stated (D1, 2.10: a degree with honours (FHEQ Level 6; FQHEIS Level 10))" }
  - { from: "fheq:7", to: "fqheis:11", relation: "equivalent", basis: "stated (D1, 2.15 integrated master's; 4.6 Level 7 of the FHEQ and Level 11 on the FQHEIS)" }
```

### S6 Themes
<!-- label: both; status: drafted; basis: primary -->
```yaml
- { id: "theme:edi", role: "carries", carriedIn: ["1.17", "1.18", "1.19", "1.20", "1.21", "1.22", "1.23", "2.4", "2.5", "2.6", "2.28", "2.30", "3.7", "3.10", "4.4", "4.5"] }
- { id: "theme:accessibility", role: "carries", carriedIn: ["1.21", "1.22", "1.24", "1.25", "1.26", "2.4", "2.16", "2.17", "2.21", "3.7", "3.10"] }
- { id: "theme:esd", role: "carries", carriedIn: ["1.16", "1.19", "1.27", "1.28", "1.29", "1.30", "1.31", "1.32", "1.33", "1.34", "2.7", "2.17", "2.19", "2.30", "4.5"] }
- { id: "theme:enterprise", role: "carries", carriedIn: ["1.35", "1.36", "1.37", "1.38", "1.39", "1.40", "1.41", "1.42", "1.43", "1.44", "1.45", "1.46", "1.47", "1.48", "1.49", "2.8"] }
- { id: "theme:generative-ai", role: "carries", carriedIn: ["3.7", "3.8", "4.5"] }
```

### S7 Relations
<!-- label: both; status: drafted; basis: primary -->
```yaml
- { rel: "partOf", target: "collection: QAA Subject Benchmark Statements", note: "one of 54 held by stan" }
- { rel: "supersedes", target: "std:doc:qaa-health-studies-2019-benchmarks (not yet ingested)", note: "the fourth edition, 2019, named in section 6; earlier editions 2016, 2007 and 2002" }
- { rel: "refersTo", target: "std:doc:qaa-fheq-2024-framework, Annex D", note: "the classification descriptions, for evidence above the threshold (4.2)" }
- { rel: "refersTo", target: "std:doc:qaa-fheq-2024-framework", note: "levels 6 and 7 (2.10, 2.15, 4.6); the master's lists 4.7 and 4.8 follow descriptor 4.17 closely" }
- { rel: "refersTo", target: "std:doc:qaa-fqheis-2024-framework", note: "levels 10 and 11 (2.10, 2.15, 4.6)" }
- { rel: "themeReference", target: "std:doc:qaa-advancehe-esd-2021-guidance", note: "definitions of sustainable development and ESD (1.27)" }
- { rel: "refersTo", target: "QAA Higher Education Apprenticeships Characteristics Statement, 2022 (not yet ingested)", note: "2.22" }
- { rel: "refersTo", target: "QAA, Creating Inclusive Subject Learning Communities, 2021 (not yet ingested)", note: "2.28.b1" }
- { rel: "refersTo", target: "GMC, Promoting Excellence: standards for medical education and training, 2015 (not yet ingested)", note: "quoted in 2.5" }
- { rel: "refersTo", target: "QAA Quality Code, Advice and Guidance; QAA Glossary (not yet ingested)", note: "front matter" }
- { rel: "readWith", target: "other QAA Subject Benchmark Statements", note: "for multidisciplinary and joint courses (1.8, 2.1)" }
```

### S8 Currency and review
<!-- label: source; status: drafted; basis: primary -->
```yaml
published: "2024-04"
lastReviewed: "none-stated"
reviewCycle: "none-stated"
consultation: "none-stated; an advisory group of 17 members is listed (section 6)"
replacedBy: "none"
```

### S9 Commentary (optional)
<!-- label: editorial; status: drafted; basis: secondary -->
`unknown`: not researched in P1 (Part E).

### SB1 The subject
<!-- label: both; status: drafted; basis: primary -->
- The study of health across the life-course in individuals, families, communities and populations, from local to global, taking in physical and mental health, well-being, illness, rehabilitation and palliative care (D1, 1.1, 1.2, 1.6).
- Health is treated as more than the absence of disease and has no single agreed definition; studying it is not the same as studying illness or training to care for the sick (D1, 1.9).
- Multidisciplinary and interdisciplinary: it draws on over 30 disciplines, from epidemiology and public health to sociology, law and ethics, and courses choose their own mix (D1, 1.3, 1.14, 1.16, 2.1, 2.2).
- Reflective and reflexive critical evaluation of health and how it is represented sits at its centre (D1, 1.10, 1.12).
- An integrated, interprofessional care approach, with patients, service users and carers as partners (D1, 1.5, 1.11).
- Research-based, with attention to research ethics and to how research informs clinical practice and its governance (D1, 1.6, 1.12).
- Courses range from conceptual to applied and vocational, some shaped by professional standards; the aim is to make students agents of change (D1, 1.7, 1.11, 1.15, 1.29).

### SB2 Themes in this subject
<!-- label: both; status: drafted; basis: primary -->
```yaml
- theme: theme:edi
  inThisSubject: "treated as part of the culture of the subject, set out as why, what and how it is taught; health inequalities, decolonising the curriculum, culturally safe care and the legal duty against discrimination (D1, 1.17 to 1.23, 2.4 to 2.6)"
  statements: ["qaa/health-studies-2024/1.21", "qaa/health-studies-2024/1.23", "qaa/health-studies-2024/2.4", "qaa/health-studies-2024/2.5", "qaa/health-studies-2024/3.10.b3", "qaa/health-studies-2024/4.4.b16", "qaa/health-studies-2024/4.4.b19", "qaa/health-studies-2024/4.5.b11", "qaa/health-studies-2024/4.5.b18"]
- theme: theme:accessibility
  inThisSubject: "every course requirement open to every student from pre-application to graduation; alternative assessments, reasonable adjustments, digital access and equal access to placements and international learning (D1, 1.24 to 1.26, 2.17, 3.7)"
  statements: ["qaa/health-studies-2024/1.24", "qaa/health-studies-2024/3.7.b2", "qaa/health-studies-2024/3.10.b3"]
- theme: theme:esd
  inThisSubject: "headed Sustainability: planetary health and the link between sustainability, equity and health; the SDGs across the curriculum; the eight UNESCO competencies as outcomes; problem-based and interprofessional ESD teaching (D1, 1.27 to 1.34, 2.7)"
  statements: ["qaa/health-studies-2024/1.27", "qaa/health-studies-2024/1.31.b1", "qaa/health-studies-2024/1.31.b2", "qaa/health-studies-2024/1.31.b3", "qaa/health-studies-2024/1.31.b4", "qaa/health-studies-2024/1.31.b5", "qaa/health-studies-2024/1.31.b6", "qaa/health-studies-2024/1.31.b7", "qaa/health-studies-2024/1.31.b8", "qaa/health-studies-2024/1.32", "qaa/health-studies-2024/1.33", "qaa/health-studies-2024/4.5.b19"]
- theme: theme:enterprise
  inThisSubject: "enterprise and entrepreneurship for employed and self-employed health careers: an entrepreneurial mindset, placements, external speakers and business-focused assignments (D1, 1.35 to 1.49, 2.8)"
  statements: ["qaa/health-studies-2024/1.37", "qaa/health-studies-2024/1.43", "qaa/health-studies-2024/4.5.b19"]
- theme: theme:generative-ai
  inThisSubject: "not a section of its own: one passage on how far generative AI enters teaching, learning and assessment and on staying alert to its limits; AI tools among assessment methods; the role of AI in health among the generic skills (D1, 3.7, 3.8, 4.5)"
  statements: ["qaa/health-studies-2024/3.7.b3", "qaa/health-studies-2024/3.7.b4", "qaa/health-studies-2024/4.5.b14"]
```

### SB3 Content and delivery
<!-- label: both; status: drafted; basis: primary -->
```yaml
areas:
  - { component: "1.10", gloss: "common themes: health as human experience in its contexts; reflective and critical evaluation of health and its representations" }
  - { component: "1.16", gloss: "32 contributing disciplines and subject areas, from allied health, epidemiology and public health to sociology, social policy and social work" }
  - { component: "3.1", gloss: "content for reflective, critical study of health, well-being and illness" }
  - { component: "3.2", gloss: "specialising within a broad field; integration with social care" }
practices:
  - { component: "1.34", kind: "teaching", gloss: "ESD methods: problem-based and interprofessional learning, simulations, field trips, placements" }
  - { component: "3.3", kind: "teaching", gloss: "blended, communicative and inclusive strategies; synchronous and asynchronous" }
  - { component: "3.5", kind: "learning", gloss: "lectures, seminars, labs, case-based patient-led seminars, tutorials; peer, self-directed, work-based and inter-professional learning" }
  - { component: "3.7", kind: "assessment", gloss: "formative and summative; inclusive; reasonable adjustments; generative AI" }
  - { component: "3.8", kind: "assessment", gloss: "essays, online resources, presentations, projects, examinations, portfolios, work-based and practical assessment" }
  - { component: "3.9", kind: "assessment", gloss: "feedback qualities and timing; feed-in, feed-forward and feedback" }
  - { component: "3.10", kind: "assessment", gloss: "six things feedback should do" }
  - { component: "3.11", kind: "learning", gloss: "supervision in practice, developed with employers" }
  - { component: "3.12", kind: "learning", gloss: "what supervision needs: preparation, objectives, coaching, tripartite arrangements" }
```

### SB4 Benchmark standards
<!-- label: both; status: drafted; basis: primary -->
```yaml
rungs:
  - { rung: "threshold", leadIn: "4.4; 4.5 (defined as the minimum in 4.1 and 4.3)", award: "bachelor's with honours", items: 42 }
  - { rung: "threshold", leadIn: "4.7 (defined as the minimum in 4.3)", award: "master's", items: 4 }
  - { rung: "typical", leadIn: "4.8 ('Typically, holders ... will be able to')", award: "master's", items: 6 }
  - { rung: "excellent", leadIn: "none", award: "none", items: 0 }
rungBases: "threshold 46 records in all (honours 4.4: 22, 4.5: 20; master's 4.7: 4); typical 6 (master's 4.8); no typical or excellent rung for honours: 4.2 leaves achievement above the threshold to the provider and Annex D"
outcomeLists:
  - { leadIn: "1.31", gloss: "the eight UNESCO sustainability competencies, as what students can do", items: 8, award: ["honours (inferred)"] }
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
- { body: "professional, statutory and regulatory bodies (PSRBs), unnamed", says: "may evaluate and accredit courses with professional or vocational outcomes; courses align with a relevant regulatory body where one applies; feedback and monitoring align with their requirements (D1, 2.18, 2.20, 2.26, 2.28, 3.10)", requirements: "not yet ingested (Part E)" }
- { body: "Academy for Healthcare Science", says: "one of the registers or bodies graduates might join (D1, 2.9)", requirements: "not yet ingested (Part E)" }
- { body: "Faculty of Public Health", says: "one of the bodies graduates might join (D1, 2.9)", requirements: "not yet ingested (Part E)" }
- { body: "Royal Society of Public Health", says: "one of the bodies graduates might join; named so in the text (D1, 2.9)", requirements: "not yet ingested (Part E)" }
- { body: "Institute of Health Promotion and Education", says: "one of the bodies graduates might join (D1, 2.9)", requirements: "not yet ingested (Part E)" }
- { body: "General Medical Council (GMC)", says: "its 2015 standards for medical education are quoted on learning the needs of diverse patients (D1, 2.5)", requirements: "not yet ingested (Part E)" }
- { body: "Competitions and Markets Authority (CMA)", says: "monitoring and review support compliance with its requirements (D1, 2.28)", requirements: "not yet ingested (Part E)" }
- { body: "Advance HE", says: "co-issuer of the ESD guidance; its term for an inclusive environment in curriculum design (D1, 1.27, 2.4)", requirements: "std:doc:qaa-advancehe-esd-2021-guidance" }
- { body: "UNESCO", says: "source of the eight sustainability competencies (D1, 1.31)", requirements: "not yet ingested (Part E)" }
```

### SB6 Cross-cutting references
<!-- label: both; status: drafted; basis: primary -->
```yaml
themes:
  - { id: "theme:edi", named: "Equality, diversity and inclusion (EDI)", carriedIn: ["1.17", "1.18", "1.19", "1.20", "1.21", "1.22", "1.23", "2.4", "2.5", "2.6", "2.28", "2.30", "3.7", "3.10", "4.4", "4.5"], statements: ["1.21", "1.23", "2.4", "2.5", "3.10.b3", "4.4.b16", "4.4.b19", "4.5.b11", "4.5.b18"] }
  - { id: "theme:accessibility", named: "Accessibility (front matter: accessibility and the needs of disabled students)", carriedIn: ["1.21", "1.22", "1.24", "1.25", "1.26", "2.4", "2.16", "2.17", "2.21", "3.7", "3.10"], statements: ["1.24", "3.7.b2", "3.10.b3"] }
  - { id: "theme:esd", named: "Sustainability; Education for Sustainable Development (ESD)", carriedIn: ["1.16", "1.19", "1.27", "1.28", "1.29", "1.30", "1.31", "1.32", "1.33", "1.34", "2.7", "2.17", "2.19", "2.30", "4.5"], statements: ["1.27", "1.31.b1", "1.31.b2", "1.31.b3", "1.31.b4", "1.31.b5", "1.31.b6", "1.31.b7", "1.31.b8", "1.32", "1.33", "4.5.b19"] }
  - { id: "theme:enterprise", named: "Enterprise and entrepreneurship education (EEE); front matter: employability, entrepreneurship and enterprise education", carriedIn: ["1.35", "1.36", "1.37", "1.38", "1.39", "1.40", "1.41", "1.42", "1.43", "1.44", "1.45", "1.46", "1.47", "1.48", "1.49", "2.8"], statements: ["1.37", "1.43", "4.5.b19"] }
  - { id: "theme:generative-ai", named: "generative artificial intelligence (AI) tools", carriedIn: ["3.7", "3.8", "4.5"], statements: ["3.7.b3", "3.7.b4", "4.5.b14"] }
frameworks:
  - { framework: "fheq", levels: ["fheq:6", "fheq:7"], citedIn: ["2.10", "2.15", "4.2", "4.6"] }
  - { framework: "scqf", levels: ["fqheis:10", "fqheis:11"], citedIn: ["2.10", "2.15", "4.2", "4.6"] }
  - { framework: "other: national qualifications frameworks, unnamed", levels: [], citedIn: ["2.3", "2.28"] }
bodies:
  - { body: "PSRBs (unnamed)", citedIn: ["2.18", "2.20", "2.26", "2.28", "3.10"] }
  - { body: "Academy for Healthcare Science", citedIn: ["2.9"] }
  - { body: "Faculty of Public Health", citedIn: ["2.9"] }
  - { body: "Royal Society of Public Health", citedIn: ["2.9"] }
  - { body: "Institute of Health Promotion and Education", citedIn: ["2.9"] }
  - { body: "General Medical Council", citedIn: ["2.5"] }
  - { body: "Competitions and Markets Authority", citedIn: ["2.28"] }
  - { body: "Advance HE", citedIn: ["1.27", "2.4"] }
  - { body: "UNESCO", citedIn: ["1.31"] }
sharedDocuments:
  - { document: "std:doc:qaa-fheq-2024-framework, Annex D", named: "Annex D in The Frameworks for Higher Education Qualifications of UK Degree-Awarding Bodies", citedIn: ["4.2"], role: "descriptions of the four honours classifications, for evidence of achievement above the threshold" }
  - { document: "std:doc:qaa-fheq-2024-framework", named: "FHEQ", citedIn: ["2.10", "2.15", "4.6"], role: "levels 6 and 7" }
  - { document: "std:doc:qaa-fqheis-2024-framework", named: "FQHEIS", citedIn: ["2.10", "2.15", "4.6"], role: "levels 10 and 11" }
  - { document: "std:doc:qaa-advancehe-esd-2021-guidance", named: "QAA and Advance HE's Education for Sustainable Development Guidance, 2021", citedIn: ["1.27"], role: "definitions of sustainable development and ESD" }
  - { document: "not yet ingested: listed in Part E", named: "QAA's Higher Education Apprenticeships Characteristics Statement", citedIn: ["2.22"], role: "describes apprenticeship degrees" }
  - { document: "not yet ingested: listed in Part E", named: "QAA, 2021, p11 (Creating Inclusive Subject Learning Communities, by the reference list)", citedIn: ["2.28"], role: "intended, implemented and attained curriculum" }
  - { document: "other QAA Subject Benchmark Statements", named: "other relevant Subject Benchmark Statements", citedIn: ["1.8", "2.1"], role: "for multidisciplinary and joint courses" }
```

## Part B Terminology
<!-- The statement has no glossary of its own unless Part E says so; these are terms it defines in its text. -->

### B1 Concepts
<!-- label: both; status: drafted; basis: primary -->
```yaml
- { slug: "health", definition: "wholeness and physical and mental well-being, carrying senses of contentment, equity and justice, and going beyond freedom from disease; it has no single agreed definition (D1, 1.9)", beneficiaryDefinition: "health means more than not being ill: being well in body and mind, and living fairly", scopeNote: "studying health is set apart from studying illness or training in care", category: "unknown", practices: ["health"] }
- { slug: "reflective-and-reflexive-self-awareness", definition: "reflective awareness notices one's own biases and preferences; reflexive awareness asks how one's own history and culture shape dealings with others (D1, 1.10)", beneficiaryDefinition: "being reflective means noticing your own biases; being reflexive means seeing how your background shapes how you treat others", scopeNote: "the two are linked and complementary", category: "unknown", practices: ["health", "education"] }
- { slug: "equality-diversity-and-inclusion", definition: "a wide set of identity characteristics, with attention to intersectionality, embedded in the culture and practice of the subject (D1, 1.17)", beneficiaryDefinition: "fair treatment and a sense of belonging for everyone, whatever their identity", scopeNote: "abbreviated EDI", category: "unknown", practices: ["education"] }
- { slug: "accessibility", definition: "whether every requirement of a course, however met, can be understood and completed by all students (D1, 1.24)", beneficiaryDefinition: "whether you can understand and complete everything the course asks of you", scopeNote: "at least the regulatory minimum; every stage of the course", category: "unknown", practices: ["education"] }
- { slug: "education-for-sustainable-development", definition: "building curriculum structures and content that support and enact sustainable development, as QAA and Advance HE's 2021 guidance defines it (D1, 1.27)", beneficiaryDefinition: "learning that helps you work towards a fairer, more sustainable world", scopeNote: "abbreviated ESD", category: "unknown", practices: ["education"] }
- { slug: "enterprise-and-entrepreneurship-education", definition: "education for the behaviours, attributes and competencies that support successful and self-determined careers (D1, 1.35, 1.36)", beneficiaryDefinition: "learning that builds the enterprising qualities you need for your career, employed or self-employed", scopeNote: "abbreviated EEE", category: "unknown", practices: ["education"] }
- { slug: "apprenticeship-degree", definition: "a degree that combines taught study with work-based learning, the workplace being the main source of learning (D1, 2.22)", beneficiaryDefinition: "a degree you take mostly through your job, with study alongside", scopeNote: "QAA describes these further in a separate statement", category: "unknown", practices: ["education"] }
```

### B2a Terms as the issuer defines them
<!-- label: source; status: drafted; basis: primary -->
```yaml
- { concept: "equality-diversity-and-inclusion", form: "Equality, diversity and inclusion (EDI)", lang: "en", partOfSpeech: "noun-phrase", termStatus: "preferred", register: "formal" }
- { concept: "education-for-sustainable-development", form: "Education for Sustainable Development (ESD)", lang: "en", partOfSpeech: "noun-phrase", termStatus: "preferred", register: "formal" }
- { concept: "enterprise-and-entrepreneurship-education", form: "Enterprise and entrepreneurship education (EEE)", lang: "en", partOfSpeech: "noun-phrase", termStatus: "preferred", register: "formal" }
- { concept: "reflective-and-reflexive-self-awareness", form: "reflexive self-awareness", lang: "en", partOfSpeech: "noun-phrase", termStatus: "preferred", register: "formal" }
- { concept: "apprenticeship-degree", form: "Apprenticeship degrees", lang: "en", partOfSpeech: "noun-phrase", termStatus: "preferred", register: "formal" }
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
  title: "Subject Benchmark Statement Health Studies"
  edition: "April 2024 (fifth edition)"
  year: 2024
  url: unknown (the QAA page; the text came by stan's extraction)
  retrieved: "held from stan: wkspc2615-QAAVector mapped/health-studies-2024/health-studies-2024.raw.txt, commit 366bcb99a01118f2c4c3ebfa2a8337596bddc455; received 2026-10-03"
  licence: QAA copyright
  tier: primary
  readVia: direct
  held: 4e1b4d26208497dcf689448bcd3217b7f1a913a1da48e5e92be38fef924f6528
  heldFiles: ["wkspc2601-library/txt/qaa-2024-health-studies-subject-benchmark-statement-standard.txt", "wkspc2601-library/txt/qaa-2024-health-studies-subject-benchmark-statement-standard.norm.txt", "wkspc2601-library/records/qaa-2024-health-studies-subject-benchmark-statement-standard.chunks.json", "wkspc2601-library/records/qaa-2024-health-studies-subject-benchmark-statement-standard.held.json"]
  citedIn: [S1, S2, S3, S4, S4a, S5, S6, S7, SB1, SB2, SB3, SB4, SB5, SB6]
```

### D2 Research log
```yaml
- { ref: D1, tier: primary, consulted: 2026-10-03, pass: P1, outcome: "read whole, direct, from the normalised text; skeleton by tools/std_prep.py, document by tools/bm_build.py" }
- { ref: "ADAPT subj HESA stores, cah.json and hecos.json (designs/ingest/standards/subj/vocab)", tier: primary, consulted: 2026-10-03, pass: P1, outcome: "codes for statedSubjects and subjects" }
```

### D3 Wanted sources
```yaml
- { w: "W-std-0065", source: "Subject Benchmark Statement: Health Studies, fourth edition (QAA, 2019)", why: "the superseded edition, for supersedes and change analysis" }
- { w: "W-std-0036", source: "QAA Higher Education Apprenticeships Characteristics Statement (2022)", why: "cited at 2.22" }
- { w: "W-std-0066", source: "QAA, Creating Inclusive Subject Learning Communities (2021)", why: "cited at 2.28 as QAA, 2021" }
- { w: "W-std-0067", source: "GMC, Promoting Excellence: standards for medical education and training (2015)", why: "quoted at 2.5" }
- { w: "W-std-0043", source: "UNESCO, Education for Sustainable Development Goals: learning objectives (2017)", why: "source of the eight competencies at 1.31" }
```

## Part E Gaps and questions
- Rungs: honours has a threshold rung only (4.4 subject, 4.5 generic); no typical or excellent rung. 4.2 leaves achievement above the threshold to the provider and Annex D. Differs from Psychology, which states three rungs.
- Master's: the statement covers master's degrees with their own lists (4.7 subject knowledge, 4.8 generic skills); recorded as award master's, level fheq:7. They have their own paragraph numbers, so no `.masters` suffix is needed.
- 4.8 lead-in reads 'Typically, holders of a qualification in Health Studies will be able to demonstrate skills that show': recorded as rung typical with force will, after the FHEQ's split between threshold outcomes and what typical holders can do (std:doc:qaa-fheq-2024-framework, SL5). Alternative reading for P3: the threshold generic skills for master's, parallel to 4.5. Doubtful cut.
- 4.7 and 4.8 restate the FHEQ master's descriptor (qaa/fheq-2024/4.17.b1 to 4.17.b8.3) almost word for word, with 'health' added; 4.6 calls them 'This qualification descriptor'.
- Threshold force: the 4.4, 4.5 and 4.7 lead-ins say 'should be able to'; recorded force threshold with forceFrom 4.3, which defines the threshold as the minimum a student 'must demonstrate to be eligible for an award' (brief convention).
- No gradeOf links: the only typical list (4.8, generic skills, master's) has no threshold list of the same domain and award below it (4.7 is knowledge and understanding). SB4 outcomes left empty.
- Outcome list 1.31: the UNESCO competencies, items in 'can' or 'are able to'; recorded rung none, award honours and level fheq:6 inferred (the paragraph names no award).
- 1.31.b5: the skeleton cut the item at the page break after 'understand'; re-cut with find to the item's end, page number 9 included in the span.
- Skeleton spans with a glued heading re-cut with find: 3.10.b6 ('Supervision'), 4.4.b22 ('Generic skills'), 4.5.b20 (the master's heading), 4.7.b4 ('Generic skills').
- Paragraph statements cut to their obliging sentence with find (1.13, 1.21, 1.23, 1.24, 1.27, 1.32, 1.33, 1.37, 1.43, 2.1, 2.3, 2.4, 2.5, 2.11, 2.16, 2.18 to 2.24, 2.27, 3.3, 3.11, 4.2, 4.3, 4.6). 2.10 and 2.13 take the whole paragraph; 3.4 takes the skeleton's span.
- 3.7 and 3.9 hold several modals; each obliging sentence is its own record, numbered 3.7.b1 to 3.7.b4 and 3.9.b1 to 3.9.b3. These are sentence records, not list items: for P3.
- Obliging words outside the five: 'requires' (1.32, 1.33) and 'requires consideration of' (3.12 lead-in) recorded as must; 'essential' (1.12 critical reflection, 1.27 the SDGs, 2.24 externality, 3.9 feedback) and 'it will be important' (2.2) not recorded as statements: for Abbott.
- 'Will want to' (2.20 first sentence, 2.21) and 'would be expected' (2.12) read as soft and not recorded as statements: for Abbott.
- Not statements, by the brief: plain-present provider norms (for example 1.20 'courses ensure', 1.29, 2.23 'routinely collect', 3.1, 3.2); 1.3 'students are required to draw on a wide variety of subject disciplines' read as a description of the subject's breadth; 1.11 aims ('being given the opportunity to'); 1.28 and 1.30 'will' about what awareness or reflection does; 1.35 'It will prepare' (a prediction about EEE); 2.19 and 2.27 list items (what partnership and monitoring help to do); 2.25 external examiners' duties.
- Not statements: the 'may include' lists (1.22, 1.24.b1 to b4, 2.4.b1 to b12, 2.6, 2.17, 3.5, 3.8) and the entrepreneurial mindset list (1.38).
- 2.28.b1 to b10 recorded as provider expectations under the lead-in 'will support and enable'.
- 2.11.b1 to b4 recorded as provider duties under 'should be reinforced by strategies that'.
- Generic-skill records outside section 4 (1.37, 1.43, 3.7.b4, 1.31.b1 to b8) carry level fheq:6 inferred, so that SB-4 holds; the paragraphs name no level.
- 4.3 carries level [fheq:6, fheq:7] as a list: it states both thresholds.
- Theme generative AI: no section of its own; tagged from 3.7, 3.8 and 4.5 under theme:generative-ai.
- Theme names: front matter lists 'employability, entrepreneurship and enterprise education'; the section is headed 'Enterprise and entrepreneurship education'. Sustainability is headed 'Sustainability' and names ESD.
- Bodies: the statement names four bodies a graduate might join (2.9), quotes the GMC (2.5) and names the CMA (2.28); none is a professional body that accredits the subject, and PSRBs are named only in general. Requirements not ingested.
- Advance HE and UNESCO recorded in SB5 and SB6 though neither is a PSRB: Advance HE co-issues the ESD guidance; UNESCO is the source of the competencies.
- 'Royal Society of Public Health' as the text names it (recall: the body styles itself Royal Society for Public Health; to check).
- Shared QAA documents not yet ingested: Higher Education Apprenticeships Characteristics Statement (2.22); Creating Inclusive Subject Learning Communities (2.28, cited as QAA, 2021, p11); the Quality Code's Advice and Guidance and the Glossary (front matter). QAA's Enterprise and Entrepreneurship Education (std:doc:qaa-enterprise-2018-guidance) appears only in the reference list, so it is not in SB6.
- Subjects: hecos 100473 health studies stated by title; CAH15-04-03 and its parents by the HECoS mapping; hecos 100476 health and social care inferred (related code; social care named in 1.16 and 3.2), held back until P3 confirms it.
- Supersedes: the fourth edition (2019) from section 6, which is excluded matter read only for this; no date of the previous edition appears in the front matter.
- 1.21 source keeps the extraction's '(s ee paragraph 2.4)' as held.
- Levels 4 and 5 (CertHE and DipHE exits, 2.14) are named as awards but not as levels; not recorded in S5.
- S9 commentary not researched in P1.
- ST-12: versions here run to the lengths the content needs; no length range is yet set.

---

## Change notes
- 0.1.2, 3 October 2026, 21:02: moved with its held text from UNI to the source library repo (`wkspc2601-library/ingested/standards/`, texts in `txt/`, records in `records/`); paths only (Abbott, 20:56; std N-0119).
- 0.1.1, 3 October 2026, 20:20: obliging words outside the five read as must, "ought to" as should, on statements outside the rungs, each marked on its force line (Abbott, 20:17; D-std-0016).
- 0.1.0, 2026-10-03 17:33: researched by run frame 0.1.1-draft and standards run layer 0.7.0-draft, std, run 0109 (P1); built by tools/bm_build.py.
