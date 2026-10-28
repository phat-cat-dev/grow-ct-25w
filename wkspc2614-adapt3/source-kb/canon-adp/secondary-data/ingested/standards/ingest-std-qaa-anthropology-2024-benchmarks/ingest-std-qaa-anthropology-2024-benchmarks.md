---
id: std:doc:qaa-anthropology-2024-benchmarks
title: "Subject Benchmark Statement Anthropology"
profile: standards/subject-benchmark
profileVersion: 0.2.0-draft
issuer: QAA
kind: subject-benchmark
jurisdiction: [UK]
subjectScope: subjects
subjects:
  - { scheme: "hecos", code: "100436", label: "anthropology", basis: "stated" }
  - { scheme: "cah", code: "CAH15-01-04", label: "anthropology", basis: "stated" }
  - { scheme: "cah", code: "CAH15-01", label: "sociology, social policy and anthropology", basis: "stated" }
  - { scheme: "hecos", code: "100437", label: "social anthropology", basis: "stated" }
  - { scheme: "hecos", code: "101218", label: "forensic anthropology", basis: "stated" }
  - { scheme: "hecos", code: "100663", label: "physical and biological anthropology", basis: "inferred" }
edition: "April 2024 (fifth edition)"
published: 2024-04
status: current
supersedes: "Subject Benchmark Statement for Anthropology, fourth edition (2019), as the text names it"
heldText: { method: sha256-bytes, raw: 2b6b5a5effdb16257b38616ae89d7a3a45c2d967edbf4b71c436333ab645dd64, normalised: 99882ad6e210470ee1e30c1c81c049a52de63d427b6d57a2a664b7b441828245 }
heldTextStan: { method: sha256-stan, raw: 2b6b5a5effdb16257b38616ae89d7a3a45c2d967edbf4b71c436333ab645dd64, normalised: 50788a49c582d1ee1bffb9653ccaceeade76354d48821a61cb9f994730f75897 }
licence: "QAA copyright; held for study, private to the project, never published"
series: "QAA Subject Benchmark Statements, April 2024 revision with the cross-cutting themes (fifth edition of this statement)"
awardsCovered: ["bachelor's with honours", "master's"]
levelsCovered: ["fheq:6", "fheq:7", "fqheis:10", "fqheis:11"]
nations: ["England", "Wales", "Scotland", "Northern Ireland"]
parts:
  S: full
  B: "partial: no glossary in the document (it points to QAA's Glossary); terms it defines in passing"
  C: "not-applicable: the document sets expectations, not a procedure"
pins: { structure: 0.13.0-draft, template: 0.8.0-draft, benchmarkTemplate: 0.6.0-draft, runFrame: 0.1.1-draft, runLayer: 0.7.0-draft, standards: none yet, terminology: none yet }
lifecycle: drafted
researchedBy: run frame 0.1.1-draft; standards run layer 0.7.0-draft; std, run 0084 (tools/bm_build.py)
passes:
  P1: "2026-10-03 16:19"
  P2: "skipped: read direct from the held text; inferred codes and rung links are for P3"
  P3: open
version: 0.1.2
---

<!-- from INGEST wpk-0016-ingest-pd-template-standards.md 0.8.0-draft and wpk-0016-ingest-pd-template-standards-benchmark.md 0.6.0-draft; built by tools/bm_build.py from run-src/ -->
# Subject Benchmark Statement: Anthropology (QAA, April 2024)

> Run 0084, P1 by std. The issuer's words are held in the source library, `wkspc2601-library/txt/qaa-2024-anthropology-subject-benchmark-statement-standard.norm.txt`; each S4 record carries its statement in full (`source`) for language analysis, with its span. Paraphrases and versions are ours. Private to the project, never published. In front matter `status` is the issuer's; ours is `lifecycle`. Doubts are in Part E.

## Part 0 Summary

### 0.1 Agent definition
<!-- label: editorial; status: drafted; basis: primary -->
QAA's UK reference point for what an honours graduate in Anthropology knows, understands and can do, with Social and Biological Anthropology rows beside the general ones. Its standards are three tables (knowledge and understanding, subject-specific skills, generic skills), each row stated at a threshold and at a strong/excellent level, the second also the master's expectation. Reach for it when designing, reviewing or describing an Anthropology course or its outcomes. It is not a curriculum and not a regulatory requirement in England.

### 0.2 Summary
<!-- label: both; status: drafted; basis: primary -->
Published by QAA in April 2024 as the fifth edition, the statement sets out the purposes of an Anthropology degree, its distinctive features (design, ethics, progression, partnership, review), its content, teaching and assessment and its benchmark standards for the bachelor's degree with honours: 45 outcomes in three tables, each at threshold and at strong/excellent (no separate typical rung), with general rows for all degrees and specific rows for degrees mainly in Social or Biological Anthropology. Master's students are expected to master the strong/excellent column. It carries the four cross-cutting themes (equality, diversity and inclusion; accessibility and flexibility; sustainability; enterprise and entrepreneurship education), cites the FHEQ and FQHEIS levels and Annex D, draws on the QAA and Advance HE ESD guidance and the SDGs, and names the Royal Anthropological Institute, the British Association for Biological Anthropology and Osteoarchaeology and the Association of Social Anthropologists.

## Part S Standard

### S1 Identity
<!-- label: source; status: drafted; basis: primary -->
```yaml
issuer: The Quality Assurance Agency for Higher Education
title: "Subject Benchmark Statement Anthropology"
edition: "April 2024 (fifth edition)"
dates:
  published: 2024-04
  other: []
kind: subject-benchmark
jurisdiction: [UK]
authority: "reference: a sector reference point, not a regulatory requirement (D1, front matter)"
licence: "QAA copyright; the document gives no re-use terms in its text (D1, front matter)"
copyrightNotice: { text: "© The Quality Assurance Agency for Higher Education 2024", locator: "D1, index" }
```

### S2 Purpose and scope
<!-- label: source; status: drafted; basis: primary -->
```yaml
governs: "what can be expected of an Anthropology graduate at the end of an honours degree, and of courses in the subject"
appliesTo:
  awards: ["bachelor's with honours", "master's"]
  levels: ["fheq:6", "fqheis:10", "fheq:7", "fqheis:11"]
  providers: ["UK higher education providers"]
whoMustUse: "none-stated; it is a reference point, not a requirement (D1, front matter)"
howUsed: ["design", "approval", "review", "other: external examining; PSRBs; information for prospective students and employers"]
doesNot: "it is not a national curriculum and does not prescribe teaching, learning or assessment; it carries no statutory or regulatory requirement (D1, front matter)"
beneficiary: the student
statedScope: "\"This document is a QAA Subject Benchmark Statement for Anthropology that defines what can be expected of a graduate in the subject, in terms of what they might know, do and understand at the end of their studies.\" (D1, front matter)"
statedSubjects:
  - { name: "Anthropology", locator: "(D1, front matter; 1.1)", kind: "subject", codes: [{ scheme: "hecos", code: "100436", label: "anthropology" }, { scheme: "cah", code: "CAH15-01-04", label: "anthropology" }] }
  - { name: "Social Anthropology", locator: "(D1, 2.2 to 2.5; 3.11; 4.6)", kind: "specialism", codes: [{ scheme: "hecos", code: "100437", label: "social anthropology" }] }
  - { name: "Biological Anthropology", locator: "(D1, 2.2; 2.6; 3.10; 4.6)", kind: "specialism", codes: [{ scheme: "hecos", code: "100663", label: "physical and biological anthropology (inferred: Part E)" }] }
  - { name: "Forensic Anthropology", locator: "(D1, 2.6)", kind: "specialism", codes: [{ scheme: "hecos", code: "101218", label: "forensic anthropology" }] }
  - { name: "joint honours, major-minor and combined studies", locator: "(D1, 1.13; 2.5; 2.12)", kind: "programme title", codes: [] }
subjects: see front matter (subjectScope subjects)
```

### S3 Structure
<!-- label: both; status: drafted; basis: primary -->
```yaml
components:
  - { number: "1.1", order: 3, componentType: paragraph, parent: "section 1", heading: "Context and purposes of an Anthropology degree", gloss: "purpose and authorship of the statement" }
  - { number: "1.2", order: 4, componentType: paragraph, parent: "section 1", heading: "Context and purposes of an Anthropology degree", gloss: "not prescriptive; support for course development" }
  - { number: "1.3", order: 5, componentType: paragraph, parent: "section 1", heading: "Purposes and characteristics of an Anthropology degree", gloss: "the subject's voice for human variety; ethics and inclusion" }
  - { number: "1.4", order: 6, componentType: paragraph, parent: "section 1", heading: "Purposes and characteristics of an Anthropology degree", gloss: "knowledge as situated; including many perspectives (a sentence repeated in the text)" }
  - { number: "1.5", order: 7, componentType: paragraph, parent: "section 1", heading: "Purposes and characteristics of an Anthropology degree", gloss: "students' lived experience as a resource; remains of the dead" }
  - { number: "1.6", order: 8, componentType: paragraph, parent: "section 1", heading: "Purposes and characteristics of an Anthropology degree", gloss: "research-led learning by doing in field and lab" }
  - { number: "1.7", order: 9, componentType: stem, parent: "section 1", heading: "Purposes and characteristics of an Anthropology degree", gloss: "four kinds of relationship the subject studies" }
  - { number: "1.8", order: 10, componentType: paragraph, parent: "section 1", heading: "Equality, diversity and inclusion", gloss: "colonial origins and the critique of power" }
  - { number: "1.9", order: 11, componentType: paragraph, parent: "section 1", heading: "Equality, diversity and inclusion", gloss: "agenda items: sex binaries, patriarchy, intersectionality" }
  - { number: "1.10", order: 12, componentType: paragraph, parent: "section 1", heading: "Equality, diversity and inclusion", gloss: "decolonial work; situating experience" }
  - { number: "1.11", order: 13, componentType: paragraph, parent: "section 1", heading: "Accessibility and flexibility", gloss: "flexible, accessible routes for diverse students" }
  - { number: "1.12", order: 14, componentType: paragraph, parent: "section 1", heading: "Accessibility and flexibility", gloss: "blended learning, optional modules, varied assessment" }
  - { number: "1.13", order: 15, componentType: paragraph, parent: "section 1", heading: "Accessibility and flexibility", gloss: "full and part-time, joint and combined modes" }
  - { number: "1.14", order: 16, componentType: paragraph, parent: "section 1", heading: "Sustainability", gloss: "sustainable development and what ESD secures" }
  - { number: "1.15", order: 17, componentType: paragraph, parent: "section 1", heading: "Sustainability", gloss: "six ESD competencies the subject develops, with SDG numbers" }
  - { number: "1.16", order: 18, componentType: paragraph, parent: "section 1", heading: "Enterprise and Entrepreneurship Education", gloss: "enterprise education and careers" }
  - { number: "1.17", order: 19, componentType: paragraph, parent: "section 1", heading: "Enterprise and Entrepreneurship Education", gloss: "competencies for a self-directed working life" }
  - { number: "1.18", order: 20, componentType: paragraph, parent: "section 1", heading: "Enterprise and Entrepreneurship Education", gloss: "global perspective; varied career paths" }
  - { number: "1.19", order: 21, componentType: paragraph, parent: "section 1", heading: "Enterprise and Entrepreneurship Education", gloss: "skills for understanding communities; social innovation" }
  - { number: "1.20", order: 22, componentType: paragraph, parent: "section 1", heading: "Enterprise and Entrepreneurship Education", gloss: "practical methods linking local and global scales" }
  - { number: "1.21", order: 23, componentType: paragraph, parent: "section 1", heading: "Enterprise and Entrepreneurship Education", gloss: "research projects from the start; communication skills" }
  - { number: "1.22", order: 24, componentType: paragraph, parent: "section 1", heading: "Enterprise and Entrepreneurship Education", gloss: "complex human behaviour; sectors of work" }
  - { number: "1.23", order: 25, componentType: paragraph, parent: "section 1", heading: "Practice", gloss: "a practical discipline learned by doing it" }
  - { number: "1.24", order: 26, componentType: paragraph, parent: "section 1", heading: "Practice", gloss: "field sites and transferable skills" }
  - { number: "1.25", order: 27, componentType: paragraph, parent: "section 1", heading: "Practice", gloss: "kinds of anthropologist and their methods" }
  - { number: "1.26", order: 28, componentType: paragraph, parent: "section 1", heading: "Practice", gloss: "core methods courses; reflexive practice" }
  - { number: "2.1", order: 30, componentType: paragraph, parent: "section 2", heading: "Design", gloss: "what the subject explores; its scope and insights" }
  - { number: "2.2", order: 31, componentType: paragraph, parent: "section 2", heading: "Design", gloss: "one sub-field or a general course; four organising themes" }
  - { number: "2.3", order: 32, componentType: area, parent: "section 2", heading: "Design: Social Anthropology", gloss: "Social Anthropology: theory, neighbours, sub-fields" }
  - { number: "2.4", order: 33, componentType: paragraph, parent: "section 2", heading: "Design: Social Anthropology", gloss: "general or specialised Social Anthropology degrees" }
  - { number: "2.5", order: 34, componentType: paragraph, parent: "section 2", heading: "Design: Social Anthropology", gloss: "Social Anthropology in joint honours; flexibility" }
  - { number: "2.6", order: 35, componentType: area, parent: "section 2", heading: "Design: Biological Anthropology", gloss: "Biological Anthropology: evolutionary theory, STEM links, sub-fields" }
  - { number: "2.7", order: 36, componentType: paragraph, parent: "section 2", heading: "Anthropology in practice: fieldwork and lab work", gloss: "training in collecting and analysing data" }
  - { number: "2.8", order: 37, componentType: paragraph, parent: "section 2", heading: "Anthropology in practice: fieldwork and lab work", gloss: "flexible training beyond the classroom; secondary data" }
  - { number: "2.9", order: 38, componentType: paragraph, parent: "section 2", heading: "Ethics", gloss: "ethical guidelines; chances to weigh fieldwork ethics" }
  - { number: "2.10", order: 39, componentType: paragraph, parent: "section 2", heading: "Ethics", gloss: "ethical outcomes by the end of the degree" }
  - { number: "2.11", order: 40, componentType: paragraph, parent: "section 2", heading: "Progression", gloss: "progression to honours and to postgraduate study" }
  - { number: "2.12", order: 41, componentType: paragraph, parent: "section 2", heading: "Progression", gloss: "joint and combined honours" }
  - { number: "2.13", order: 42, componentType: paragraph, parent: "section 2", heading: "Progression", gloss: "integrated master's degrees" }
  - { number: "2.14", order: 43, componentType: paragraph, parent: "section 2", heading: "Progression", gloss: "exit awards; four-year Scottish honours" }
  - { number: "2.15", order: 44, componentType: paragraph, parent: "section 2", heading: "Partnership", gloss: "partnerships and community co-production" }
  - { number: "2.16", order: 45, componentType: paragraph, parent: "section 2", heading: "Partnership", gloss: "careers after graduating" }
  - { number: "2.17", order: 46, componentType: paragraph, parent: "section 2", heading: "Partnership", gloss: "links with organisations; guest speakers; placements" }
  - { number: "2.18", order: 47, componentType: paragraph, parent: "section 2", heading: "Partnership", gloss: "professional organisations for students" }
  - { number: "2.19", order: 48, componentType: paragraph, parent: "section 2", heading: "Monitoring and review", gloss: "monitoring and periodic review" }
  - { number: "2.20", order: 49, componentType: paragraph, parent: "section 2", heading: "Monitoring and review", gloss: "external review in quality assurance" }
  - { number: "2.21", order: 50, componentType: paragraph, parent: "section 2", heading: "Monitoring and review", gloss: "external examiners and threshold standards" }
  - { number: "2.22", order: 51, componentType: paragraph, parent: "section 2", heading: "Monitoring and review", gloss: "professional accreditation of some courses" }
  - { number: "3.1", order: 53, componentType: paragraph, parent: "section 3", heading: "Content", gloss: "practical content; knowing and choosing methods" }
  - { number: "3.2", order: 54, componentType: area, parent: "section 3", heading: "Content", gloss: "history of the discipline in every course" }
  - { number: "3.3", order: 55, componentType: area, parent: "section 3", heading: "Content", gloss: "colonialism and decolonising" }
  - { number: "3.4", order: 56, componentType: paragraph, parent: "section 3", heading: "Content", gloss: "ethical conduct, power and equitable collaboration" }
  - { number: "3.5", order: 57, componentType: area, parent: "section 3", heading: "Content", gloss: "humans and their environments" }
  - { number: "3.6", order: 58, componentType: area, parent: "section 3", heading: "Content", gloss: "theoretical approaches" }
  - { number: "3.7", order: 59, componentType: area, parent: "section 3", heading: "Content", gloss: "other typical themes" }
  - { number: "3.8", order: 60, componentType: paragraph, parent: "section 3", heading: "Content", gloss: "value of knowing both branches" }
  - { number: "3.9", order: 61, componentType: paragraph, parent: "section 3", heading: "Content", gloss: "developments beyond the global North" }
  - { number: "3.10", order: 62, componentType: area, parent: "section 3", heading: "Content", gloss: "core content for Biological Anthropology (ten topics)" }
  - { number: "3.11", order: 63, componentType: area, parent: "section 3", heading: "Content", gloss: "core content for Social Anthropology (ten topics)" }
  - { number: "3.12", order: 64, componentType: area, parent: "section 3", heading: "Content", gloss: "further optional subjects (twelve examples)" }
  - { number: "3.13", order: 65, componentType: practice, parent: "section 3", heading: "Content", gloss: "learning fieldwork; an own fieldwork project" }
  - { number: "3.14", order: 66, componentType: practice, parent: "section 3", heading: "Teaching and learning", gloss: "hands-on, interactive pedagogy" }
  - { number: "3.15", order: 67, componentType: paragraph, parent: "section 3", heading: "Teaching and learning", gloss: "expertise and facilities needed" }
  - { number: "3.16", order: 68, componentType: paragraph, parent: "section 3", heading: "Teaching and learning", gloss: "health, safety and practical ethics training" }
  - { number: "3.17", order: 69, componentType: practice, parent: "section 3", heading: "Teaching and learning", gloss: "placements and practical projects" }
  - { number: "3.18", order: 70, componentType: paragraph, parent: "section 3", heading: "Teaching and learning", gloss: "inclusive pedagogy and reasonable adjustments" }
  - { number: "3.19", order: 71, componentType: practice, parent: "section 3", heading: "Teaching and learning", gloss: "teaching styles" }
  - { number: "3.20", order: 72, componentType: practice, parent: "section 3", heading: "Teaching and learning", gloss: "self-directed study and outside opportunities" }
  - { number: "3.21", order: 73, componentType: paragraph, parent: "section 3", heading: "Assessment", gloss: "assessment and feedback strategy; criteria in advance" }
  - { number: "3.22", order: 74, componentType: practice, parent: "section 3", heading: "Assessment", gloss: "formative assessment and feedback" }
  - { number: "3.23", order: 75, componentType: paragraph, parent: "section 3", heading: "Assessment", gloss: "flexible assessment that avoids disadvantage" }
  - { number: "3.24", order: 76, componentType: practice, parent: "section 3", heading: "Assessment", gloss: "varied assessment; marking group work" }
  - { number: "3.25", order: 77, componentType: paragraph, parent: "section 3", heading: "Assessment", gloss: "what all assessment emphasises" }
  - { number: "3.26", order: 78, componentType: practice, parent: "section 3", heading: "Assessment", gloss: "dissertation or extended project" }
  - { number: "3.27", order: 79, componentType: practice, parent: "section 3", heading: "Assessment", gloss: "practical, real-world assessment tasks" }
  - { number: "3.28", order: 80, componentType: practice, parent: "section 3", heading: "Assessment", gloss: "writing for many audiences" }
  - { number: "3.29", order: 81, componentType: practice, parent: "section 3", heading: "Assessment", gloss: "exams and tests still used" }
  - { number: "3.30", order: 82, componentType: practice, parent: "section 3", heading: "Assessment", gloss: "assessing practical work" }
  - { number: "3.31", order: 83, componentType: practice, parent: "section 3", heading: "Assessment", gloss: "creative outputs in assessment" }
  - { number: "3.32", order: 84, componentType: paragraph, parent: "section 3", heading: "Assessment", gloss: "digital and online outputs" }
  - { number: "3.33", order: 85, componentType: paragraph, parent: "section 3", heading: "Assessment", gloss: "portfolios" }
  - { number: "3.34", order: 86, componentType: paragraph, parent: "section 3", heading: "Assessment", gloss: "placement reports" }
  - { number: "4.1", order: 88, componentType: paragraph, parent: "section 4", heading: "Introduction", gloss: "threshold standards for the honours degree" }
  - { number: "4.2", order: 89, componentType: paragraph, parent: "section 4", heading: "Introduction", gloss: "most exceed the threshold; Annex D" }
  - { number: "4.3", order: 90, componentType: paragraph, parent: "section 4", heading: "Introduction", gloss: "three areas of performance" }
  - { number: "4.4", order: 91, componentType: paragraph, parent: "section 4", heading: "Introduction", gloss: "the tables: broad, not prescriptive or exhaustive" }
  - { number: "4.5", order: 92, componentType: paragraph, parent: "section 4", heading: "Introduction", gloss: "baseline and further skills" }
  - { number: "4.6", order: 93, componentType: paragraph, parent: "section 4", heading: "Introduction", gloss: "rows specific to Social or Biological Anthropology" }
  - { number: "4.7", order: 94, componentType: paragraph, parent: "section 4", heading: "Master's level study", gloss: "master's study" }
  - { number: "4.8", order: 95, componentType: paragraph, parent: "section 4", heading: "Master's level study", gloss: "master's expectation; then the three tables (the skeleton's span runs on through them)" }
  - { number: "1", componentType: section, parent: none, heading: "Context and purposes of an Anthropology degree", gloss: "section 1" }
  - { number: "2", componentType: section, parent: none, heading: "Distinctive features of an Anthropology degree", gloss: "section 2" }
  - { number: "3", componentType: section, parent: none, heading: "Content, structure and delivery", gloss: "section 3" }
  - { number: "4", componentType: section, parent: none, heading: "Benchmark standards", gloss: "section 4" }
  - { number: "ku", componentType: section, parent: none, heading: "4 Benchmark standards: Knowledge and understanding (table)", gloss: "section ku" }
  - { number: "ss", componentType: section, parent: none, heading: "4 Benchmark standards: Subject-specific skills (table)", gloss: "section ss" }
  - { number: "gs", componentType: section, parent: none, heading: "4 Benchmark standards: Generic skills (table)", gloss: "section gs" }
excluded:
  - { number: "none", heading: "Contents; About this Statement; How can I use this document?; Relationship to legislation; Additional sector reference points", kind: "other: front matter, read for S1, S2, S7 and SB6" }
  - { number: "1, 2, 3, 4", heading: "section heading lines", kind: "other: headings, recorded in SECTIONS" }
  - { number: "5", heading: "List of references and further resources", kind: "other: two references on decolonisation, read for SB6" }
  - { number: "6", heading: "Membership of the Advisory Group (2024, 2019, 2015, 2007, 2002)", kind: "other: authorship history, read for S7 supersedes" }
```

### S4 Statements
<!-- label: both; status: drafted; basis: primary. Only standards (D-std-0002 (a)): 117 records. `source` is the issuer's statement exactly as its span holds it (D-std-0014). -->
```yaml
- id: qaa/anthropology-2024/1.11
  locator: { number: "1.11", headingPath: ["Context and purposes of an Anthropology degree", "Accessibility and flexibility"] }
  span: { start: 13999, end: 14379 }
  source: "Anthropology degrees should be flexible, accessible and offer education pathways to students from non-traditional academic backgrounds, with a range of disabilities and neurodiversities. Support for such students will intersect with broader institutional support - for example, Additional Learning Support teams - but is facilitated by the diverse nature of the discipline itself."
  stem: none
  statementType: expectation
  rung: none
  force: should
  level: none
  appliesTo: "Anthropology degrees"
  addressee: provider
  verbs: ["offer"]
  about: "flexible, accessible routes for diverse students"
  themes: [theme:accessibility]
  domain: none
  award: ["bachelor's with honours"]
  gradeOf: none
  paraphrase: "Degrees in the subject should be flexible and accessible and open routes to students from non-traditional backgrounds and with a range of disabilities and neurodivergent conditions; institutional support works alongside, helped by the varied nature of the discipline."
  quote: full   # the issuer's statement is in `source` (D-std-0014)
  audience: practitioner
  subjects: inherited
- id: qaa/anthropology-2024/1.21
  locator: { number: "1.21", headingPath: ["Context and purposes of an Anthropology degree", "Enterprise and Entrepreneurship Education"] }
  span: { start: 21964, end: 23202 }
  source: "Anthropologists are required to design, conduct and complete research projects from the outset. This enables students to gain confidence in many skills. Anthropology students learn to pursue and critically analyse evidence, manage uncertainties, recognise ethical dilemmas, create collaborative solutions in action, pay attention to detail, negotiate, network, and understand the role the researcher plays in knowledge production and exchange. Anthropologists, therefore, develop multiple communication competencies that range from collecting, processing and presenting complex information effectively and imaginatively through to constructing narratives and co-producing work with a range of collaborators for diverse audiences. Depending on the focus and core methods taught within degree programmes, these competencies may include skills in manipulating text and in working with\n\n7\nmulti-modal forms of communication - including images, film, sound and a range of digital tools. Consequently, Anthropology students graduate with a suite of transferable skills such as adaptability, agility, confidence, curiosity, the capacity to manage and direct their ideas and stimulate change, and the ability to recognise and respect differences."
  stem: none
  statementType: requirement
  rung: none
  force: must
  level: fheq:6
  appliesTo: "students of the subject"
  addressee: learner
  verbs: ["required", "design", "conduct", "complete", "pursue", "analyse", "manage", "recognise", "negotiate", "network"]
  about: "research projects from the start and the skills they build"
  themes: [theme:enterprise]
  domain: subject-skill
  award: ["bachelor's with honours"]
  gradeOf: none
  paraphrase: "Students of the subject are required to design, carry out and finish research projects from the start of their studies; this builds skills in handling evidence and uncertainty, ethics, collaboration, detail, negotiation and networking, as well as a range of communication and transferable skills."
  quote: full   # the issuer's statement is in `source` (D-std-0014)
  audience: both
  subjects: inherited
- id: qaa/anthropology-2024/1.23
  locator: { number: "1.23", headingPath: ["Context and purposes of an Anthropology degree", "Practice"] }
  span: { start: 23741, end: 24094 }
  source: "Anthropology is an intensely practical discipline; students are required to do Anthropology rather than just learn about it. To become an anthropologist, students build skills and competencies in a range of data collection and analysis methods that are designed to allow understanding of how other people - even those long dead - experience their lives."
  stem: none
  statementType: requirement
  rung: none
  force: must
  level: fheq:6
  appliesTo: "students of the subject"
  addressee: learner
  verbs: ["required", "do", "build"]
  about: "learning the subject by doing it"
  themes: [none]
  domain: subject-skill
  award: ["bachelor's with honours"]
  gradeOf: none
  paraphrase: "The discipline is strongly practical: students are required to practise it, not only study it, building skills in a range of methods for collecting and analysing data that help them grasp how others, including the long dead, live their lives."
  quote: full   # the issuer's statement is in `source` (D-std-0014)
  audience: both
  subjects: inherited
- id: qaa/anthropology-2024/1.26
  locator: { number: "1.26", headingPath: ["Context and purposes of an Anthropology degree", "Practice"] }
  span: { start: 25952, end: 26744 }
  source: "These important practical skills are developed through methods courses which are delivered as a core part of Anthropology programmes and as appropriate to the sub- disciplinary focus of the degree. These are likely to integrate consideration not only of methods per se but also engagement with ethical questions including the opportunities for collaborative work with research participants and co-researchers that develop Anthropology students as reflexive practitioners able to operate within a wide range of social contexts and work settings. Anthropological methods also require students to challenge their own biases and assumptions, appreciate the historical and cultural situatedness of academic research, and understand how these shape interpretations of both the present and the past."
  stem: none
  statementType: requirement
  rung: none
  force: must
  level: fheq:6
  appliesTo: "students of the subject"
  addressee: learner
  verbs: ["require", "challenge", "appreciate", "understand"]
  about: "reflexive methods: confronting one's own biases"
  themes: [none]
  domain: understanding
  award: ["bachelor's with honours"]
  gradeOf: none
  paraphrase: "Practical skills come through core methods courses suited to the degree's focus, which bring in ethics and collaboration with participants and co-researchers; the methods require students to confront their own biases and assumptions, see how academic research is placed in history and culture and grasp how this shapes readings of present and past."
  quote: full   # the issuer's statement is in `source` (D-std-0014)
  audience: both
  subjects: inherited
- id: qaa/anthropology-2024/2.9
  locator: { number: "2.9", headingPath: ["Distinctive features of an Anthropology degree", "Ethics"] }
  span: { start: 31941, end: 32589 }
  source: "Anthropologists are held to strict ethical guidelines that recognise the privilege it is to study other humans and/or primates. The discussion of ethical frameworks is ideally incorporated throughout the degree though sometimes with explicit modules or courses on the topic. Anthropology students should be given opportunities in their degree programmes to consider how different forms of research practice - gathered under the broad heading of fieldwork - may be applied to different research questions and in different research contexts, how they produce different findings and outputs, and thus the different ethical considerations they involve."
  stem: none
  statementType: expectation
  rung: none
  force: should
  level: none
  appliesTo: "Anthropology degrees"
  addressee: provider
  verbs: ["given", "consider"]
  about: "chances to weigh the ethics of research practices"
  themes: [none]
  domain: none
  award: ["bachelor's with honours"]
  gradeOf: none
  paraphrase: "Anthropologists work to strict ethical guidelines; ethics is best woven through the degree, and students should be given chances to consider how different kinds of fieldwork suit different questions and settings, yield different findings and raise different ethical issues."
  quote: full   # the issuer's statement is in `source` (D-std-0014)
  audience: practitioner
  subjects: inherited
- id: qaa/anthropology-2024/2.10
  locator: { number: "2.10", headingPath: ["Distinctive features of an Anthropology degree", "Ethics"] }
  span: { start: 32595, end: 32850 }
  source: "By the end of their degree, students will have been exposed to and be experienced in handling sensitive topics, will be able to understand complex ethical issues in context, and evaluate and develop projects with reference to the highest ethical standards"
  stem: none
  statementType: outcome
  rung: none
  force: will
  level: fheq:6
  appliesTo: "students of the subject by the end of the degree"
  addressee: learner
  verbs: ["exposed", "understand", "evaluate", "develop"]
  about: "handling sensitive topics and complex ethics"
  themes: [none]
  domain: understanding
  award: ["bachelor's with honours"]
  gradeOf: none
  paraphrase: "By the end of the degree students will have met and gained experience in handling sensitive topics, will understand complex ethical issues in context and will judge and build projects to the highest ethical standards."
  quote: full   # the issuer's statement is in `source` (D-std-0014)
  audience: both
  subjects: inherited
- id: qaa/anthropology-2024/2.12
  locator: { number: "2.12", headingPath: ["Distinctive features of an Anthropology degree", "Progression"] }
  span: { start: 33687, end: 34150 }
  source: "In the case of degree programmes organised on the basis of joint honours, major- minor and other permutations of Combined Studies, undergraduates will achieve core elements of the specific and generic skills for the subject and will add others according to the subjects covered in joint courses. Additionally, they may explore the overlap between the\n\n10\nsubject areas covered by their specific courses, creating further opportunities for interdisciplinary study."
  stem: none
  statementType: outcome
  rung: none
  force: will
  level: fheq:6
  appliesTo: "joint honours, major-minor and combined studies students"
  addressee: learner
  verbs: ["achieve", "add"]
  about: "core skills on joint and combined degrees"
  themes: [none]
  domain: none
  award: ["bachelor's with honours"]
  gradeOf: none
  paraphrase: "Students on joint, major-minor or combined degrees will reach the core subject-specific and generic skills of the subject and add others from their other subjects, and may explore where the subjects overlap."
  quote: full   # the issuer's statement is in `source` (D-std-0014)
  audience: both
  subjects: inherited
- id: qaa/anthropology-2024/2.15
  locator: { number: "2.15", headingPath: ["Distinctive features of an Anthropology degree", "Partnership"] }
  span: { start: 34864, end: 36178 }
  source: "Anthropology courses are likely to provide students with the ability to develop partnerships and networks with a view to employability and community engagement, as well as expanding perspectives and skills. Because of the breadth of the discipline, collaborations and partnerships in Anthropology are numerous and diverse. Precise partnerships will depend on the specialisms of the provider; this section does not aim to be exhaustive but to provide an overview of the types of partnerships courses may incorporate. Most notably, fieldwork in Anthropology necessitates the engagement of local communities which should be acknowledged as partners and as co-producers of knowledge where appropriate. Working with stakeholder communities encourages meaningful and relevant outcomes and develops skills in research design, as well as developing wider employability skills such as communication, planning and public outreach. Throughout an Anthropology course, local community partners can take many forms. Depending on the expertise available at a particular institution, 'local communities' may be a population under study, a population living alongside primates, a descendent community of past populations, or others. Communities may be engaged with in-person or digitally, personally or anonymously, as appropriate."
  stem: none
  statementType: expectation
  rung: none
  force: should
  level: none
  appliesTo: "courses and students doing fieldwork"
  addressee: both
  verbs: ["acknowledged"]
  about: "communities as partners and co-producers"
  themes: [none]
  domain: none
  award: ["bachelor's with honours"]
  gradeOf: none
  paraphrase: "Courses are likely to help students build partnerships and networks for employability and community work; fieldwork needs local communities, which should be treated as partners and, where fitting, as co-producers of knowledge, and working with them builds research design and wider employability skills."
  quote: full   # the issuer's statement is in `source` (D-std-0014)
  audience: both
  subjects: inherited
- id: qaa/anthropology-2024/2.18
  locator: { number: "2.18", headingPath: ["Distinctive features of an Anthropology degree", "Partnership"] }
  span: { start: 37129, end: 37469 }
  source: "Anthropology students should also be introduced to the resources and networks provided by the various professional organisations appropriate to their studies as part of their studies and their career development (most notably the Royal Anthropological Institute and the British Association for Biological Anthropology and Osteoarchaeology)."
  stem: none
  statementType: expectation
  rung: none
  force: should
  level: none
  appliesTo: "Anthropology degrees"
  addressee: provider
  verbs: ["introduced"]
  about: "introduction to professional organisations"
  themes: [none]
  domain: none
  award: ["bachelor's with honours"]
  gradeOf: none
  paraphrase: "Students should be introduced, within their studies and career development, to the resources and networks of the professional organisations that fit their studies, chiefly the British Association for Biological Anthropology and Osteoarchaeology (BABAO) and the Royal Anthropological Institute (RAI)."
  quote: full   # the issuer's statement is in `source` (D-std-0014)
  audience: practitioner
  subjects: inherited
- id: qaa/anthropology-2024/3.1
  locator: { number: "3.1", headingPath: ["Content, structure and delivery", "Content"] }
  span: { start: 39552, end: 40446 }
  source: "As a practical subject discipline, all Anthropology degree courses are likely to cover significant elements of empirical, practical work and data collection. The content of individual degree courses within departments and providers is likely to vary depending on focus and expertise. However, this might include training and potentially also experience in the field and/or the laboratory; for example, in the form of participant observation, interviews, surveys, the collection of data on aspects of human or other primate biological diversity, diet and health, and/or other practical, hands-on engagement - such as, with objects and materials (see also the section on practice). While it is not expected that students will graduate as experts in all relevant methods, they should be aware of the range of methods available and able to identify appropriate ones for different research contexts."
  stem: none
  statementType: expectation
  rung: none
  force: should
  level: fheq:6
  appliesTo: "graduates of the subject"
  addressee: learner
  verbs: ["identify"]
  about: "knowing the range of methods and choosing them"
  themes: [none]
  domain: subject-skill
  award: ["bachelor's with honours"]
  gradeOf: none
  paraphrase: "Degrees are likely to include substantial practical and empirical work; students need not graduate expert in every method, but they should know the range of methods available and be able to pick suitable ones for different research settings."
  quote: full   # the issuer's statement is in `source` (D-std-0014)
  audience: both
  subjects: inherited
- id: qaa/anthropology-2024/3.2
  locator: { number: "3.2", headingPath: ["Content, structure and delivery", "Content"] }
  span: { start: 40451, end: 41113 }
  source: "All Anthropology degree courses will include material on the history of the discipline (including both Social and Biological Anthropology). This will usually include understanding the development of theoretical trends, the history of fieldwork and other practical techniques as well as the interpretation and use of anthropological data in historical discourses, and the ways that Anthropology has increasingly come to take an active stance in contemporary social, economic and environmental issues. The relevance of the discipline for a huge range of contemporary debates, from colonialism and other forms of inequality to the climate emergency, is highlighted."
  stem: none
  statementType: expectation
  rung: none
  force: will
  level: none
  appliesTo: "all Anthropology degree courses"
  addressee: provider
  verbs: ["include"]
  about: "the history of the discipline in every course"
  themes: [none]
  domain: none
  award: ["bachelor's with honours"]
  gradeOf: none
  paraphrase: "Every degree in the subject will include the history of the discipline, Social and Biological alike, usually covering how theory and fieldwork developed, how its data have been read and used in the past and how it now takes active positions on current issues."
  quote: full   # the issuer's statement is in `source` (D-std-0014)
  audience: practitioner
  subjects: inherited
- id: qaa/anthropology-2024/3.3
  locator: { number: "3.3", headingPath: ["Content, structure and delivery", "Content"] }
  span: { start: 41118, end: 41871 }
  source: "Anthropologists recognise that their discipline, like many others, has roots in European colonialism, and that this has affected how anthropologists have conducted their research. Students across Anthropology can expect to learn about how colonialism affected indigenous and local ways of life, and how it continues to be significant in cultural, economic and environmental terms. Anthropologists have been engaged in efforts to 'decolonise' both their discipline and wider structures of academia and students will learn about why and how this may be done, as well as being introduced to critiques emphasising the broader structural issues of academia more generally. Students will be encouraged and trained to develop their own voices in these debates."
  stem: none
  statementType: outcome
  rung: none
  force: will
  level: fheq:6
  appliesTo: "students of the subject"
  addressee: both
  verbs: ["learn", "encouraged", "trained", "develop"]
  about: "colonialism, decolonising and a voice of one's own"
  themes: [none]
  domain: understanding
  award: ["bachelor's with honours"]
  gradeOf: none
  paraphrase: "The discipline recognises its roots in European colonialism; students will learn why and how anthropologists try to decolonise the discipline and academia, meet critiques of academia's wider structures and be encouraged and trained to find their own voices in these debates."
  quote: full   # the issuer's statement is in `source` (D-std-0014)
  audience: both
  subjects: inherited
- id: qaa/anthropology-2024/3.4
  locator: { number: "3.4", headingPath: ["Content, structure and delivery", "Content"] }
  span: { start: 41876, end: 43000 }
  source: "Coupled with this focus on practice and method should be explicit recognition and debate around the ethical conduct required of anthropologists (both social and biological), who are typically relatively privileged in global terms, and a recognition of the likelihood of power imbalances between anthropologists and the peoples with whom they have traditionally worked. Ethical debates should stress the contested, dynamic nature of anthropological interpretation, but also emphasise that the communities with whom anthropologists work should be accorded the utmost respect and credit as collaborators in the production of anthropological knowledge, have the right to contest the ways in which they are represented, and that anthropologists have a responsibility to enter into, and much to gain from, genuinely equitable collaborations with them. Attention should also be paid to the debates surrounding the equitable sharing of data and research outcomes with populations under study, and of making data and analytical processes freely accessible for the purposes of reproducibility and reuse, where ethical and practicable."
  stem: none
  statementType: expectation
  rung: none
  force: should
  level: none
  appliesTo: "Anthropology degree courses"
  addressee: provider
  verbs: ["stress", "emphasise", "paid"]
  about: "ethical conduct, power and equitable collaboration"
  themes: [none]
  domain: none
  award: ["bachelor's with honours"]
  gradeOf: none
  paraphrase: "Teaching on practice and method should include open debate about anthropologists' ethical conduct and their likely privilege and power over those they study; it should stress that interpretation is contested, that communities deserve respect, credit and the right to contest how they are shown, and that equitable collaboration is owed and rewarding; data sharing and open data should also be discussed where ethical and practicable."
  quote: full   # the issuer's statement is in `source` (D-std-0014)
  audience: practitioner
  subjects: inherited
- id: qaa/anthropology-2024/3.5
  locator: { number: "3.5", headingPath: ["Content, structure and delivery", "Content"] }
  span: { start: 43005, end: 43468 }
  source: "A further significant focus of Anthropology degrees will be the reciprocal relationships between humans and their environments, including other animal species as well as vegetation and physical environments. Anthropology courses will typically encourage students to consider the economic, ecological, ideological and cultural aspects of those relationships, and their significance for debates around sustainability, conservation and the ongoing climate emergency."
  stem: none
  statementType: expectation
  rung: none
  force: will
  level: none
  appliesTo: "Anthropology degree courses"
  addressee: provider
  verbs: ["encourage", "consider"]
  about: "humans and their environments"
  themes: [none]
  domain: none
  award: ["bachelor's with honours"]
  gradeOf: none
  paraphrase: "A further major focus will be the two-way relations between people and their environments, other species included; courses will usually encourage students to weigh the economic, ecological, ideological and cultural sides of those relations and what they mean for sustainability, conservation and the climate emergency."
  quote: full   # the issuer's statement is in `source` (D-std-0014)
  audience: practitioner
  subjects: inherited
- id: qaa/anthropology-2024/3.6
  locator: { number: "3.6", headingPath: ["Content, structure and delivery", "Content"] }
  span: { start: 43477, end: 43791 }
  source: "Anthropology degree courses should produce familiarity with the range of theoretical approaches and perspectives available for interpretation of anthropological data. While such theoretical material may take the form of a standalone 'theory' module or course, it may also be built into more problem-oriented study."
  stem: none
  statementType: expectation
  rung: none
  force: should
  level: none
  appliesTo: "Anthropology degree courses"
  addressee: provider
  verbs: ["produce"]
  about: "familiarity with theoretical approaches"
  themes: [none]
  domain: none
  award: ["bachelor's with honours"]
  gradeOf: none
  paraphrase: "Courses should make students familiar with the range of theoretical approaches to interpreting anthropological data, whether in a separate theory module or within problem-based study."
  quote: full   # the issuer's statement is in `source` (D-std-0014)
  audience: practitioner
  subjects: inherited
- id: qaa/anthropology-2024/3.9
  locator: { number: "3.9", headingPath: ["Content, structure and delivery", "Content"] }
  span: { start: 44605, end: 44917 }
  source: "Given the global nature of Anthropology and the critical importance of a diversity of voices to building the discipline, attention should be paid to developments in the discipline beyond the global North and beyond the identification of differences in approach between Anthropology in the UK, Europe and the USA."
  stem: none
  statementType: expectation
  rung: none
  force: should
  level: none
  appliesTo: "Anthropology degree courses"
  addressee: provider
  verbs: ["paid"]
  about: "work beyond the global North"
  themes: [none]
  domain: none
  award: ["bachelor's with honours"]
  gradeOf: none
  paraphrase: "Because the discipline is global and needs many voices, courses should attend to work beyond the global North and look past contrasts between British, European and American traditions."
  quote: full   # the issuer's statement is in `source` (D-std-0014)
  audience: practitioner
  subjects: inherited
- id: qaa/anthropology-2024/3.11
  locator: { number: "3.11", headingPath: ["Content, structure and delivery", "Content"] }
  span: { start: 46616, end: 46929 }
  source: "Where degree programmes focus specifically on Social Anthropology, they will attend to the diversity and social significance of everyday practices. Courses should be expected to\n\n14\nexplore how social activities and institutions in a range of geographical and cultural settings are locally enacted and understood."
  stem: none
  statementType: expectation
  rung: none
  force: should
  level: none
  appliesTo: "degrees focused on Social Anthropology"
  addressee: provider
  verbs: ["attend", "explore"]
  about: "everyday practices in Social Anthropology degrees"
  themes: [none]
  domain: none
  award: ["bachelor's with honours"]
  gradeOf: none
  paraphrase: "Degrees focused on Social Anthropology will attend to the variety and social meaning of everyday practices, and courses should explore how social activities and institutions are enacted and understood locally in many places and cultures."
  quote: full   # the issuer's statement is in `source` (D-std-0014)
  audience: practitioner
  subjects: inherited
- id: qaa/anthropology-2024/3.17
  locator: { number: "3.17", headingPath: ["Content, structure and delivery", "Teaching and learning"] }
  span: { start: 49001, end: 49375 }
  source: "Aside from in-class teaching and formal degree elements, Anthropology students should be facilitated to engage in placements and practical research projects, including,\n\n15\nwhere appropriate and possible globally, in order to produce students who are engaged with the wider disciplinary community as well as with the diverse local communities with whom Anthropology engages."
  stem: none
  statementType: expectation
  rung: none
  force: should
  level: none
  appliesTo: "Anthropology degree courses"
  addressee: provider
  verbs: ["facilitated", "engage"]
  about: "placements and practical research projects"
  themes: [none]
  domain: none
  award: ["bachelor's with honours"]
  gradeOf: none
  paraphrase: "Beyond classes, students should be helped to take up placements and practical research projects, globally where possible, so that they engage with the wider discipline and with the local communities it works with."
  quote: full   # the issuer's statement is in `source` (D-std-0014)
  audience: practitioner
  subjects: inherited
- id: qaa/anthropology-2024/3.20
  locator: { number: "3.20", headingPath: ["Content, structure and delivery", "Teaching and learning"] }
  span: { start: 50097, end: 50591 }
  source: "Students should also be enabled to engage in a range of self-directed study activities, including via virtual learning environments, self-directed study, problem-based learning and group work, e-learning and distance learning, as well as, where appropriate, engaging with external volunteering, placement and workplace opportunities, and/or study exchange opportunities. Developing students' ability to engage in independent study further enables lifelong learning among Anthropology graduates."
  stem: none
  statementType: expectation
  rung: none
  force: should
  level: none
  appliesTo: "Anthropology degree courses"
  addressee: provider
  verbs: ["enabled", "engage"]
  about: "self-directed study and outside opportunities"
  themes: [none]
  domain: none
  award: ["bachelor's with honours"]
  gradeOf: none
  paraphrase: "Students should also be able to take part in varied self-directed study, online and through problem-based and group learning, and where fitting in volunteering, placements, work and exchanges; building independent study supports lifelong learning."
  quote: full   # the issuer's statement is in `source` (D-std-0014)
  audience: practitioner
  subjects: inherited
- id: qaa/anthropology-2024/3.21
  locator: { number: "3.21", headingPath: ["Content, structure and delivery", "Assessment"] }
  span: { start: 50608, end: 51047 }
  source: "Each degree programme will have a clear assessment and feedback strategy allowing students to demonstrate and reflect on their level of attainment and personal development, and to discuss their programme. For each assignment, the aims, requirements and generic and specific assessment criteria will be clearly defined and made available to students ahead of time in order to facilitate appropriate progression throughout the degree course."
  stem: none
  statementType: expectation
  rung: none
  force: will
  level: none
  appliesTo: "each degree programme"
  addressee: provider
  verbs: ["demonstrate", "reflect", "defined"]
  about: "assessment and feedback strategy; criteria in advance"
  themes: [none]
  domain: none
  award: ["bachelor's with honours"]
  gradeOf: none
  paraphrase: "Every programme will set out a clear strategy for assessment and feedback that lets students show and reflect on their attainment and development, and each assignment's aims, requirements and criteria will be set out and shared in advance."
  quote: full   # the issuer's statement is in `source` (D-std-0014)
  audience: practitioner
  subjects: inherited
- id: qaa/anthropology-2024/3.23
  locator: { number: "3.23", headingPath: ["Content, structure and delivery", "Assessment"] }
  span: { start: 51478, end: 52053 }
  source: "The varied educational and cultural backgrounds and learning needs of Anthropology students are recognised by flexibility in assessment strategies. The combinations of formal assessment methods used in any degree programme should be designed in such a way as to avoid systematically disadvantaging different groups of students. Furthermore, where individual students may be disadvantaged by particular assessment methods, adjustments to those assessments are considered, while ensuring learning outcomes are met in a fair and equitable way across the full cohort of students."
  stem: none
  statementType: expectation
  rung: none
  force: should
  level: none
  appliesTo: "each degree programme"
  addressee: provider
  verbs: ["designed", "avoid"]
  about: "assessment that avoids disadvantage"
  themes: [none]
  domain: none
  award: ["bachelor's with honours"]
  gradeOf: none
  paraphrase: "Assessment is flexible to suit students' varied backgrounds and needs; the mix of formal methods should be designed so as not to disadvantage groups of students systematically, and adjustments are considered for individuals while outcomes are met fairly across the cohort."
  quote: full   # the issuer's statement is in `source` (D-std-0014)
  audience: practitioner
  subjects: inherited
- id: qaa/anthropology-2024/3.24
  locator: { number: "3.24", headingPath: ["Content, structure and delivery", "Assessment"] }
  span: { start: 52059, end: 52661 }
  source: "Given the strongly practical and applied nature of Anthropology and its focus on the diversity of human experience, assessment styles have become extremely diverse and are moving away from traditional essays and exams. As a result, students can expect to encounter a wide range of assessment styles during Anthropology degrees depending on the specific learning outcomes of different programmes and modules. Such work may be individually completed and assessed, or may involve group work, in which case marking schemes will provide clear guidance regarding the distribution of credit among individuals."
  stem: none
  statementType: expectation
  rung: none
  force: will
  level: none
  appliesTo: "each degree programme"
  addressee: provider
  verbs: ["provide"]
  about: "varied assessment; marking group work"
  themes: [none]
  domain: none
  award: ["bachelor's with honours"]
  gradeOf: none
  paraphrase: "Assessment in the subject has become very varied and is moving away from traditional essays and exams; work may be individual or in groups, and for group work the marking scheme will make clear how credit is shared among individuals."
  quote: full   # the issuer's statement is in `source` (D-std-0014)
  audience: practitioner
  subjects: inherited
- id: qaa/anthropology-2024/3.25
  locator: { number: "3.25", headingPath: ["Content, structure and delivery", "Assessment"] }
  span: { start: 52667, end: 52953 }
  source: "Regardless of the specific mode of assessment, all Anthropology degrees will emphasise the development of reflective, critical analysis skills, and the evaluation and appropriate use of different sources of evidence, as well as potential applications for addressing real-world problems."
  stem: none
  statementType: expectation
  rung: none
  force: will
  level: none
  appliesTo: "all Anthropology degrees"
  addressee: provider
  verbs: ["emphasise"]
  about: "reflective, critical analysis and use of evidence"
  themes: [none]
  domain: none
  award: ["bachelor's with honours"]
  gradeOf: none
  paraphrase: "Whatever the form of assessment, every degree in the subject will stress reflective, critical analysis, the evaluation and fitting use of varied evidence and how it might help with real problems."
  quote: full   # the issuer's statement is in `source` (D-std-0014)
  audience: practitioner
  subjects: inherited
- id: qaa/anthropology-2024/3.26
  locator: { number: "3.26", headingPath: ["Content, structure and delivery", "Assessment"] }
  span: { start: 52963, end: 53862 }
  source: "Most students will carry out a dissertation or extended personal research project, typically in their final year of study. This enables them to demonstrate the skills gained from exposure across a range of modules to elements of the entire research process - from framing research questions, aims and objectives, and developing research proposals to communicating findings. A dissertation or project also typically demonstrates application of many of the other practical and research skills developed elsewhere in the course, including specific quantitative and/or qualitative anthropological research skills as well as more general time and project-management and communication skills. A practical data-collection, field and/or laboratory-work element should be encouraged and facilitated where appropriate, although extensive synthesis of secondary data may also form the basis for such a project."
  stem: none
  statementType: expectation
  rung: none
  force: should
  level: none
  appliesTo: "Anthropology degree courses"
  addressee: provider
  verbs: ["encouraged", "facilitated"]
  about: "dissertation and practical data collection"
  themes: [none]
  domain: none
  award: ["bachelor's with honours"]
  gradeOf: none
  paraphrase: "Most students will complete a dissertation or extended research project, usually in the final year, showing skills across the research process; a practical data-collection, field or laboratory element should be encouraged and supported where suitable, though a project may rest on synthesis of secondary data."
  quote: full   # the issuer's statement is in `source` (D-std-0014)
  audience: practitioner
  subjects: inherited
- id: qaa/anthropology-2024/4.2
  locator: { number: "4.2", headingPath: ["Benchmark standards", "Introduction"] }
  span: { start: 56190, end: 56670 }
  source: "The vast majority of students will perform significantly better than the minimum threshold standards. Each higher education provider has its own method of determining what appropriate evidence of this achievement will be and should refer to Annex D in The Frameworks for Higher Education Qualifications of UK Degree-Awarding Bodies. This Annex sets out common descriptions of the four main degree outcome classifications for bachelor's degrees with honours: 1st, 2.1, 2.2 and 3rd."
  stem: none
  statementType: expectation
  rung: none
  force: should
  level: none
  appliesTo: "each higher education provider"
  addressee: provider
  verbs: ["refer"]
  about: "using Annex D for achievement above threshold"
  themes: [none]
  domain: none
  award: ["bachelor's with honours"]
  gradeOf: none
  paraphrase: "Most students will perform well above the minimum; each provider decides how to evidence that and should refer to Annex D of the qualifications frameworks, which describes the four honours classifications."
  quote: full   # the issuer's statement is in `source` (D-std-0014)
  audience: practitioner
  subjects: inherited
- id: qaa/anthropology-2024/4.7
  locator: { number: "4.7", headingPath: ["Benchmark standards", "Master's level study"] }
  span: { start: 57964, end: 58365 }
  source: "Anthropology students may wish to continue their engagement to postgraduate level. Generally Anthropology courses become increasingly specialised at Level 7/11 and tend to be either research or taught in nature. Either format will require the capacity to independently manage a significant research project, the capacity for critical thinking and analysis, and demonstrate independent problem-solving."
  stem: none
  statementType: expectation
  rung: none
  force: will
  level: fheq:7
  appliesTo: "postgraduate students of the subject"
  addressee: learner
  verbs: ["require", "demonstrate"]
  about: "master's study: research, critical thinking, problem-solving"
  themes: [none]
  domain: generic-skill
  award: ["master's"]
  gradeOf: none
  paraphrase: "Postgraduate study at Level 7/11 grows more specialised and may be taught or research-based; either will call for the ability to manage a significant research project independently, to think and analyse critically and to solve problems independently."
  quote: full   # the issuer's statement is in `source` (D-std-0014)
  audience: both
  subjects: inherited
- id: qaa/anthropology-2024/4.8
  locator: { number: "4.8", headingPath: ["Benchmark standards", "Master's level study"] }
  span: { start: 58370, end: 58491 }
  source: "Overall, students at these levels will be expected to show mastery of the 's trong/excellent' skills in the tables below."
  stem: none
  statementType: expectation
  rung: none
  force: will
  level: fheq:7
  appliesTo: "master's students of the subject"
  addressee: learner
  verbs: ["expected", "show"]
  about: "mastery of the strong/excellent skills at master's level"
  themes: [none]
  domain: none
  award: ["master's"]
  gradeOf: none
  paraphrase: "Master's students will be expected to have mastered the skills set out in the strong/excellent column of the tables."
  quote: full   # the issuer's statement is in `source` (D-std-0014)
  audience: both
  subjects: inherited
- id: qaa/anthropology-2024/gs.1.e
  locator: { number: "gs.1.e", headingPath: ["4 Benchmark standards: Generic skills (table)", ""] }
  span: { start: 73313, end: 73531 }
  source: "Demonstrate strong communication and presentation skills, and the capacity to express one's own and others' ideas clearly and effectively in innovative ways, in a variety of media and to a range of different audiences."
  stem: none
  statementType: excellent
  rung: excellent
  force: describes
  level: fheq:6
  appliesTo: "all honours graduates in the subject"
  addressee: learner
  verbs: ["Demonstrate", "express"]
  about: "strong, inventive communication to varied audiences"
  themes: [none]
  domain: generic-skill
  award: ["bachelor's with honours"]
  gradeOf: { statement: qaa/anthropology-2024/gs.1.t, basis: inferred }
  paraphrase: "Strong or excellent performance goes beyond the threshold: the graduate can communicate and present strongly, expressing their own ideas and other people's clearly, effectively and inventively, in varied media and for different audiences."
  quote: full   # the issuer's statement is in `source` (D-std-0014)
  audience: both
  subjects: inherited
- id: qaa/anthropology-2024/gs.1.t
  locator: { number: "gs.1.t", headingPath: ["4 Benchmark standards: Generic skills (table)", ""] }
  span: { start: 73142, end: 73311 }
  source: "Demonstrate good communication and\npresentation skills, and capacity to express one's own ideas, to summarise the arguments of others and to distinguish between the two."
  stem: none
  statementType: threshold
  rung: threshold
  force: threshold
  level: fheq:6
  appliesTo: "all honours graduates in the subject"
  addressee: learner
  verbs: ["Demonstrate", "express", "summarise", "distinguish"]
  about: "communication and presentation"
  themes: [none]
  domain: generic-skill
  award: ["bachelor's with honours"]
  gradeOf: none
  paraphrase: "As the minimum for the honours degree, the graduate will have shown that they can communicate and present well, put across their own ideas, summarise other people's arguments and keep the two apart."
  quote: full   # the issuer's statement is in `source` (D-std-0014)
  audience: both
  subjects: inherited
- id: qaa/anthropology-2024/gs.2.e
  locator: { number: "gs.2.e", headingPath: ["4 Benchmark standards: Generic skills (table)", ""] }
  span: { start: 73639, end: 73829 }
  source: "Demonstrate independence of thought, analytical, critical and synoptic skills and be able to apply these to develop novel approaches, critiques and hypotheses based on\n\nindependent learning."
  stem: none
  statementType: excellent
  rung: excellent
  force: describes
  level: fheq:6
  appliesTo: "all honours graduates in the subject"
  addressee: learner
  verbs: ["Demonstrate", "apply", "develop"]
  about: "independent thought turned to new approaches"
  themes: [none]
  domain: generic-skill
  award: ["bachelor's with honours"]
  gradeOf: { statement: qaa/anthropology-2024/gs.2.t, basis: inferred }
  paraphrase: "Strong or excellent performance goes beyond the threshold: the graduate can think independently, analyse, criticise and synthesise, and use those skills to develop new approaches, critiques and hypotheses from independent study."
  quote: full   # the issuer's statement is in `source` (D-std-0014)
  audience: both
  subjects: inherited
- id: qaa/anthropology-2024/gs.2.t
  locator: { number: "gs.2.t", headingPath: ["4 Benchmark standards: Generic skills (table)", ""] }
  span: { start: 73534, end: 73637 }
  source: "Demonstrate independence of thought,\nindependent learning and analytical, critical and synoptic skills."
  stem: none
  statementType: threshold
  rung: threshold
  force: threshold
  level: fheq:6
  appliesTo: "all honours graduates in the subject"
  addressee: learner
  verbs: ["Demonstrate"]
  about: "independent thought and learning"
  themes: [none]
  domain: generic-skill
  award: ["bachelor's with honours"]
  gradeOf: none
  paraphrase: "As the minimum for the honours degree, the graduate will have shown that they can think and learn independently and analyse, criticise and synthesise."
  quote: full   # the issuer's statement is in `source` (D-std-0014)
  audience: both
  subjects: inherited
- id: qaa/anthropology-2024/gs.3.e
  locator: { number: "gs.3.e", headingPath: ["4 Benchmark standards: Generic skills (table)", ""] }
  span: { start: 73931, end: 74093 }
  source: "Demonstrate a thorough grasp of basic research skills and be able to apply them in innovative and flexible ways to the collation of primary and/or secondary data."
  stem: none
  statementType: excellent
  rung: excellent
  force: describes
  level: fheq:6
  appliesTo: "all honours graduates in the subject"
  addressee: learner
  verbs: ["Demonstrate", "apply"]
  about: "inventive use of research skills"
  themes: [none]
  domain: generic-skill
  award: ["bachelor's with honours"]
  gradeOf: { statement: qaa/anthropology-2024/gs.3.t, basis: inferred }
  paraphrase: "Strong or excellent performance goes beyond the threshold: the graduate can command basic research skills thoroughly and use them inventively and flexibly to collate primary or secondary data."
  quote: full   # the issuer's statement is in `source` (D-std-0014)
  audience: both
  subjects: inherited
- id: qaa/anthropology-2024/gs.3.t
  locator: { number: "gs.3.t", headingPath: ["4 Benchmark standards: Generic skills (table)", ""] }
  span: { start: 73832, end: 73929 }
  source: "Demonstrate good basic research skills in\ncollecting and collating primary and/or secondary data."
  stem: none
  statementType: threshold
  rung: threshold
  force: threshold
  level: fheq:6
  appliesTo: "all honours graduates in the subject"
  addressee: learner
  verbs: ["Demonstrate"]
  about: "basic research skills with data"
  themes: [none]
  domain: generic-skill
  award: ["bachelor's with honours"]
  gradeOf: none
  paraphrase: "As the minimum for the honours degree, the graduate will have shown that they can use sound basic research skills to collect and collate primary or secondary data."
  quote: full   # the issuer's statement is in `source` (D-std-0014)
  audience: both
  subjects: inherited
- id: qaa/anthropology-2024/gs.4.e
  locator: { number: "gs.4.e", headingPath: ["4 Benchmark standards: Generic skills (table)", ""] }
  span: { start: 74199, end: 74331 }
  source: "Be able to assess and analyse the ethical implications of research and design, and carry out rigorously ethical research activities."
  stem: none
  statementType: excellent
  rung: excellent
  force: describes
  level: fheq:6
  appliesTo: "all honours graduates in the subject"
  addressee: learner
  verbs: ["assess", "analyse", "carry"]
  about: "assessing ethics and conducting rigorous ethical research"
  themes: [none]
  domain: generic-skill
  award: ["bachelor's with honours"]
  gradeOf: { statement: qaa/anthropology-2024/gs.4.t, basis: inferred }
  paraphrase: "Strong or excellent performance goes beyond the threshold: the graduate can weigh up and analyse what research and its design mean ethically, and carry out research to a rigorous ethical standard."
  quote: full   # the issuer's statement is in `source` (D-std-0014)
  audience: both
  subjects: inherited
- id: qaa/anthropology-2024/gs.4.t
  locator: { number: "gs.4.t", headingPath: ["4 Benchmark standards: Generic skills (table)", ""] }
  span: { start: 74096, end: 74198 }
  source: "Appreciate the ethical implications of research\nand act in an ethical manner when conducting research."
  stem: none
  statementType: threshold
  rung: threshold
  force: threshold
  level: fheq:6
  appliesTo: "all honours graduates in the subject"
  addressee: learner
  verbs: ["Appreciate", "act"]
  about: "ethics in conducting research"
  themes: [none]
  domain: generic-skill
  award: ["bachelor's with honours"]
  gradeOf: none
  paraphrase: "As the minimum for the honours degree, the graduate will have shown that they can recognise what research means ethically and behave ethically when doing it."
  quote: full   # the issuer's statement is in `source` (D-std-0014)
  audience: both
  subjects: inherited
- id: qaa/anthropology-2024/gs.5.e
  locator: { number: "gs.5.e", headingPath: ["4 Benchmark standards: Generic skills (table)", ""] }
  span: { start: 74460, end: 74659 }
  source: "Be able to put together a rigorous and persuasive structured argument, critically evaluate and integrate multiple different lines of evidence, and properly and ethically reference the work of others."
  stem: none
  statementType: excellent
  rung: excellent
  force: describes
  level: fheq:6
  appliesTo: "all honours graduates in the subject"
  addressee: learner
  verbs: ["put", "evaluate", "integrate", "reference"]
  about: "rigorous, persuasive argument with combined evidence"
  themes: [none]
  domain: generic-skill
  award: ["bachelor's with honours"]
  gradeOf: { statement: qaa/anthropology-2024/gs.5.t, basis: inferred }
  paraphrase: "Strong or excellent performance goes beyond the threshold: the graduate can build a rigorous, persuasive structured argument, evaluate and combine several lines of evidence critically, and cite other people's work properly and ethically."
  quote: full   # the issuer's statement is in `source` (D-std-0014)
  audience: both
  subjects: inherited
- id: qaa/anthropology-2024/gs.5.t
  locator: { number: "gs.5.t", headingPath: ["4 Benchmark standards: Generic skills (table)", ""] }
  span: { start: 74338, end: 74458 }
  source: "Be able to make a structured argument,\nreference the works of others, and assess a range of different lines of evidence."
  stem: none
  statementType: threshold
  rung: threshold
  force: threshold
  level: fheq:6
  appliesTo: "all honours graduates in the subject"
  addressee: learner
  verbs: ["make", "reference", "assess"]
  about: "structured argument and referencing"
  themes: [none]
  domain: generic-skill
  award: ["bachelor's with honours"]
  gradeOf: none
  paraphrase: "As the minimum for the honours degree, the graduate will have shown that they can build a structured argument, cite other people's work and weigh several lines of evidence."
  quote: full   # the issuer's statement is in `source` (D-std-0014)
  audience: both
  subjects: inherited
- id: qaa/anthropology-2024/gs.6.e
  locator: { number: "gs.6.e", headingPath: ["4 Benchmark standards: Generic skills (table)", ""] }
  span: { start: 74771, end: 74867 }
  source: "Ability to engage in and lead constructive discussion in group situations and group-work skills."
  stem: none
  statementType: excellent
  rung: excellent
  force: describes
  level: fheq:6
  appliesTo: "all honours graduates in the subject"
  addressee: learner
  verbs: ["engage", "lead"]
  about: "leading group discussion"
  themes: [none]
  domain: generic-skill
  award: ["bachelor's with honours"]
  gradeOf: { statement: qaa/anthropology-2024/gs.6.t, basis: inferred }
  paraphrase: "Strong or excellent performance goes beyond the threshold: the graduate can take part in and lead constructive group discussion and work well in groups."
  quote: full   # the issuer's statement is in `source` (D-std-0014)
  audience: both
  subjects: inherited
- id: qaa/anthropology-2024/gs.6.t
  locator: { number: "gs.6.t", headingPath: ["4 Benchmark standards: Generic skills (table)", ""] }
  span: { start: 74662, end: 74769 }
  source: "Ability to engage, where appropriate, in\nconstructive discussion in group situations and group-work skills."
  stem: none
  statementType: threshold
  rung: threshold
  force: threshold
  level: fheq:6
  appliesTo: "all honours graduates in the subject"
  addressee: learner
  verbs: ["engage"]
  about: "group discussion and group work"
  themes: [none]
  domain: generic-skill
  award: ["bachelor's with honours"]
  gradeOf: none
  paraphrase: "As the minimum for the honours degree, the graduate will have shown that they can take part constructively, where it fits, in group discussion and group work."
  quote: full   # the issuer's statement is in `source` (D-std-0014)
  audience: both
  subjects: inherited
- id: qaa/anthropology-2024/gs.7.e
  locator: { number: "gs.7.e", headingPath: ["4 Benchmark standards: Generic skills (table)", ""] }
  span: { start: 75038, end: 75373 }
  source: "Be aware of and able to apply a range of analytical and computing techniques appropriately, design and conduct independent analyses in a robust and transparent fashion, and appreciate the benefits of sharing data with research collaborators and stakeholders, as well as making data freely accessible to all where ethical and practical."
  stem: none
  statementType: excellent
  rung: excellent
  force: describes
  level: fheq:6
  appliesTo: "all honours graduates in the subject"
  addressee: learner
  verbs: ["apply", "design", "conduct", "appreciate"]
  about: "robust, transparent analysis and data sharing"
  themes: [none]
  domain: generic-skill
  award: ["bachelor's with honours"]
  gradeOf: { statement: qaa/anthropology-2024/gs.7.t, basis: inferred }
  paraphrase: "Strong or excellent performance goes beyond the threshold: the graduate can know and use a range of analytical and computing techniques properly, design and run independent analyses robustly and transparently, and value sharing data with collaborators and stakeholders and opening it to all where that is ethical and practical."
  quote: full   # the issuer's statement is in `source` (D-std-0014)
  audience: both
  subjects: inherited
- id: qaa/anthropology-2024/gs.7.t
  locator: { number: "gs.7.t", headingPath: ["4 Benchmark standards: Generic skills (table)", ""] }
  span: { start: 74870, end: 75037 }
  source: "Be aware of and able to apply a range of\nanalytical and computing techniques appropriately. Be aware of debates around the ethics of accessibility and sharing of data."
  stem: none
  statementType: threshold
  rung: threshold
  force: threshold
  level: fheq:6
  appliesTo: "all honours graduates in the subject"
  addressee: learner
  verbs: ["apply"]
  about: "analytical and computing techniques; data ethics"
  themes: [none]
  domain: generic-skill
  award: ["bachelor's with honours"]
  gradeOf: none
  paraphrase: "As the minimum for the honours degree, the graduate will have shown that they can know and use a range of analytical and computing techniques properly, and know the arguments about the ethics of access to data and of sharing it."
  quote: full   # the issuer's statement is in `source` (D-std-0014)
  audience: both
  subjects: inherited
- id: qaa/anthropology-2024/gs.8.e
  locator: { number: "gs.8.e", headingPath: ["4 Benchmark standards: Generic skills (table)", ""] }
  span: { start: 75521, end: 75721 }
  source: "Demonstrate an ability to critically assess and understand one's own and collaborators' strengths and weaknesses, and be able to plan effectively means of improving and enhancing their own capacities."
  stem: none
  statementType: excellent
  rung: excellent
  force: describes
  level: fheq:6
  appliesTo: "all honours graduates in the subject"
  addressee: learner
  verbs: ["Demonstrate", "assess", "understand", "plan"]
  about: "assessing self and collaborators and planning improvement"
  themes: [none]
  domain: generic-skill
  award: ["bachelor's with honours"]
  gradeOf: { statement: qaa/anthropology-2024/gs.8.t, basis: inferred }
  paraphrase: "Strong or excellent performance goes beyond the threshold: the graduate can judge critically and understand their own strengths and weaknesses and those of collaborators, and plan well how to improve their own abilities."
  quote: full   # the issuer's statement is in `source` (D-std-0014)
  audience: both
  subjects: inherited
- id: qaa/anthropology-2024/gs.8.t
  locator: { number: "gs.8.t", headingPath: ["4 Benchmark standards: Generic skills (table)", ""] }
  span: { start: 75376, end: 75520 }
  source: "Demonstrate an ability to assess and\nunderstand one's own strengths and weaknesses, and to take action to improve and\n\nenhance their capacities."
  stem: none
  statementType: threshold
  rung: threshold
  force: threshold
  level: fheq:6
  appliesTo: "all honours graduates in the subject"
  addressee: learner
  verbs: ["Demonstrate", "assess", "understand", "take"]
  about: "self-assessment and improvement"
  themes: [none]
  domain: generic-skill
  award: ["bachelor's with honours"]
  gradeOf: none
  paraphrase: "As the minimum for the honours degree, the graduate will have shown that they can judge and understand their own strengths and weaknesses and act to build on their own abilities."
  quote: full   # the issuer's statement is in `source` (D-std-0014)
  audience: both
  subjects: inherited
- id: qaa/anthropology-2024/gs.9.e
  locator: { number: "gs.9.e", headingPath: ["4 Benchmark standards: Generic skills (table)", ""] }
  span: { start: 75870, end: 76044 }
  source: "Be able to identify, question and challenge cultural and ethnocentric assumptions and premises based on a deep and critical understanding of other ways of being in the world."
  stem: none
  statementType: excellent
  rung: excellent
  force: describes
  level: fheq:6
  appliesTo: "all honours graduates in the subject"
  addressee: learner
  verbs: ["identify", "question", "challenge"]
  about: "challenging assumptions from deep understanding"
  themes: [none]
  domain: generic-skill
  award: ["bachelor's with honours"]
  gradeOf: { statement: qaa/anthropology-2024/gs.9.t, basis: inferred }
  paraphrase: "Strong or excellent performance goes beyond the threshold: the graduate can spot, query and push back against assumptions rooted in culture or ethnocentrism, grounded in a thorough, critical grasp of other ways of living in the world."
  quote: full   # the issuer's statement is in `source` (D-std-0014)
  audience: both
  subjects: inherited
- id: qaa/anthropology-2024/gs.9.t
  locator: { number: "gs.9.t", headingPath: ["4 Benchmark standards: Generic skills (table)", ""] }
  span: { start: 75724, end: 75868 }
  source: "Be able to identify, question and challenge\ncultural and ethnocentric assumptions and premises, and appreciate other ways of being in the world."
  stem: none
  statementType: threshold
  rung: threshold
  force: threshold
  level: fheq:6
  appliesTo: "all honours graduates in the subject"
  addressee: learner
  verbs: ["identify", "question", "challenge", "appreciate"]
  about: "challenging ethnocentric assumptions"
  themes: [none]
  domain: generic-skill
  award: ["bachelor's with honours"]
  gradeOf: none
  paraphrase: "As the minimum for the honours degree, the graduate will have shown that they can spot, query and push back against assumptions rooted in culture or ethnocentrism, and value other ways of living in the world."
  quote: full   # the issuer's statement is in `source` (D-std-0014)
  audience: both
  subjects: inherited
- id: qaa/anthropology-2024/ku.1.e
  locator: { number: "ku.1.e", headingPath: ["4 Benchmark standards: Knowledge and understanding (table)", ""] }
  span: { start: 58745, end: 58913 }
  source: "Demonstrate critical awareness of some of the factors affecting human diversity and the ability to interpret the geographical and temporal patterning of such diversity."
  stem: none
  statementType: excellent
  rung: excellent
  force: describes
  level: fheq:6
  appliesTo: "all honours graduates in the subject"
  addressee: learner
  verbs: ["Demonstrate", "interpret"]
  about: "the forces behind human diversity and its patterning"
  themes: [none]
  domain: knowledge
  award: ["bachelor's with honours"]
  gradeOf: { statement: qaa/anthropology-2024/ku.1.t, basis: inferred }
  paraphrase: "Strong or excellent performance goes beyond the threshold: the graduate can explain critically some of the forces that shape human variation and read how that variation is distributed across places and over time."
  quote: full   # the issuer's statement is in `source` (D-std-0014)
  audience: both
  subjects: inherited
- id: qaa/anthropology-2024/ku.1.t
  locator: { number: "ku.1.t", headingPath: ["4 Benchmark standards: Knowledge and understanding (table)", ""] }
  span: { start: 58576, end: 58743 }
  source: "Appreciate the social, cultural and biological\ndiversity of human populations, its scope and complexity, and the richness of experience and potential that it provides."
  stem: none
  statementType: threshold
  rung: threshold
  force: threshold
  level: fheq:6
  appliesTo: "all honours graduates in the subject"
  addressee: learner
  verbs: ["Appreciate"]
  about: "human diversity and its range"
  themes: [none]
  domain: knowledge
  award: ["bachelor's with honours"]
  gradeOf: none
  paraphrase: "As the minimum for the honours degree, the graduate will have shown that they can recognise how socially, culturally and biologically varied human populations are, how far that variety reaches and what it offers to human life and experience."
  quote: full   # the issuer's statement is in `source` (D-std-0014)
  audience: both
  subjects: inherited
- id: qaa/anthropology-2024/ku.2.e
  locator: { number: "ku.2.e", headingPath: ["4 Benchmark standards: Knowledge and understanding (table)", ""] }
  span: { start: 59040, end: 59167 }
  source: "Show critical insight into the historical development of the subject and its implications for contemporary theory and practice."
  stem: none
  statementType: excellent
  rung: excellent
  force: describes
  level: fheq:6
  appliesTo: "all honours graduates in the subject"
  addressee: learner
  verbs: ["Show"]
  about: "the discipline's history and its bearing now"
  themes: [none]
  domain: knowledge
  award: ["bachelor's with honours"]
  gradeOf: { statement: qaa/anthropology-2024/ku.2.t, basis: inferred }
  paraphrase: "Strong or excellent performance goes beyond the threshold: the graduate can look critically at how the discipline has grown and judge what its past means for present thinking and practice."
  quote: full   # the issuer's statement is in `source` (D-std-0014)
  audience: both
  subjects: inherited
- id: qaa/anthropology-2024/ku.2.t
  locator: { number: "ku.2.t", headingPath: ["4 Benchmark standards: Knowledge and understanding (table)", ""] }
  span: { start: 58917, end: 59038 }
  source: "Describe the historical context and\ndevelopment of the subject and its implications for contemporary theory and practice."
  stem: none
  statementType: threshold
  rung: threshold
  force: threshold
  level: fheq:6
  appliesTo: "all honours graduates in the subject"
  addressee: learner
  verbs: ["Describe"]
  about: "the history of the discipline"
  themes: [none]
  domain: knowledge
  award: ["bachelor's with honours"]
  gradeOf: none
  paraphrase: "As the minimum for the honours degree, the graduate will have shown that they can give an account of how the discipline arose and changed over time, and of what that past means for how it is thought about and practised now."
  quote: full   # the issuer's statement is in `source` (D-std-0014)
  audience: both
  subjects: inherited
- id: qaa/anthropology-2024/ku.3.e
  locator: { number: "ku.3.e", headingPath: ["4 Benchmark standards: Knowledge and understanding (table)", ""] }
  span: { start: 59403, end: 59467 }
  source: "Evaluate and critique debates around key themes in Anthropology."
  stem: none
  statementType: excellent
  rung: excellent
  force: describes
  level: fheq:6
  appliesTo: "all honours graduates in the subject"
  addressee: learner
  verbs: ["Evaluate", "critique"]
  about: "evaluating debates on key themes"
  themes: [none]
  domain: knowledge
  award: ["bachelor's with honours"]
  gradeOf: { statement: qaa/anthropology-2024/ku.3.t, basis: inferred }
  paraphrase: "Strong or excellent performance goes beyond the threshold: the graduate can weigh up and criticise the arguments surrounding the subject's central themes."
  quote: full   # the issuer's statement is in `source` (D-std-0014)
  audience: both
  subjects: inherited
- id: qaa/anthropology-2024/ku.3.t
  locator: { number: "ku.3.t", headingPath: ["4 Benchmark standards: Knowledge and understanding (table)", ""] }
  span: { start: 59170, end: 59401 }
  source: "Demonstrate knowledge of specific themes in\nAnthropology and the key intellectual debates concerning them, such as gender, religion, kinship, nationalism, exchange, material culture, human genetics, evolution and primate behaviour."
  stem: none
  statementType: threshold
  rung: threshold
  force: threshold
  level: fheq:6
  appliesTo: "all honours graduates in the subject"
  addressee: learner
  verbs: ["Demonstrate"]
  about: "key themes and their debates"
  themes: [none]
  domain: knowledge
  award: ["bachelor's with honours"]
  gradeOf: none
  paraphrase: "As the minimum for the honours degree, the graduate will have shown that they can show knowledge of particular themes in the subject, such as kinship, gender, religion, exchange, evolution or primate behaviour, and of the main arguments about them."
  quote: full   # the issuer's statement is in `source` (D-std-0014)
  audience: both
  subjects: inherited
- id: qaa/anthropology-2024/ku.4.e
  locator: { number: "ku.4.e", headingPath: ["4 Benchmark standards: Knowledge and understanding (table)", ""] }
  span: { start: 59653, end: 60086 }
  source: "Show critical insight into one's own and others' cultural assumptions and their implications for contemporary anthropological theory and practice; appreciate the need for, but also the potential limits to, cultural relativism. Show critical insight into key points of contention and debate with a variety of people from diverse cultures and backgrounds, and sensitivity to the implications of these debates for contemporary lifeways."
  stem: none
  statementType: excellent
  rung: excellent
  force: describes
  level: fheq:6
  appliesTo: "all honours graduates in the subject"
  addressee: learner
  verbs: ["Show", "appreciate"]
  about: "assumptions and the limits of relativism"
  themes: [none]
  domain: understanding
  award: ["bachelor's with honours"]
  gradeOf: { statement: qaa/anthropology-2024/ku.4.t, basis: inferred }
  paraphrase: "Strong or excellent performance goes beyond the threshold: the graduate can reflect critically on cultural assumptions, their own and other people's, and on what they mean for current theory and practice; weigh both the value and the limits of cultural relativism; and handle points of disagreement with people from many cultures and backgrounds with insight and with care for how those debates affect lives today."
  quote: full   # the issuer's statement is in `source` (D-std-0014)
  audience: both
  subjects: inherited
- id: qaa/anthropology-2024/ku.4.t
  locator: { number: "ku.4.t", headingPath: ["4 Benchmark standards: Knowledge and understanding (table)", ""] }
  span: { start: 59470, end: 59651 }
  source: "Identify and question cultural assumptions,\nappreciate that knowledge is culturally situated and contested and the need for cultural relativism and to understand other perspectives."
  stem: none
  statementType: threshold
  rung: threshold
  force: threshold
  level: fheq:6
  appliesTo: "all honours graduates in the subject"
  addressee: learner
  verbs: ["Identify", "question", "appreciate", "understand"]
  about: "cultural assumptions and situated knowledge"
  themes: [none]
  domain: understanding
  award: ["bachelor's with honours"]
  gradeOf: none
  paraphrase: "As the minimum for the honours degree, the graduate will have shown that they can spot and question cultural assumptions, accept that knowledge depends on where it comes from and is open to dispute, and see why cultural relativism and attention to other viewpoints matter."
  quote: full   # the issuer's statement is in `source` (D-std-0014)
  audience: both
  subjects: inherited
- id: qaa/anthropology-2024/ku.5.e
  locator: { number: "ku.5.e", headingPath: ["4 Benchmark standards: Knowledge and understanding (table)", ""] }
  span: { start: 60202, end: 60310 }
  source: "Critically evaluate and devise potential applications of anthropological knowledge in a variety of contexts."
  stem: none
  statementType: excellent
  rung: excellent
  force: describes
  level: fheq:6
  appliesTo: "all honours graduates in the subject"
  addressee: learner
  verbs: ["evaluate", "devise"]
  about: "evaluating and devising applications"
  themes: [none]
  domain: understanding
  award: ["bachelor's with honours"]
  gradeOf: { statement: qaa/anthropology-2024/ku.5.t, basis: inferred }
  paraphrase: "Strong or excellent performance goes beyond the threshold: the graduate can judge critically, and invent, ways of putting anthropological knowledge to use in different settings."
  quote: full   # the issuer's statement is in `source` (D-std-0014)
  audience: both
  subjects: inherited
- id: qaa/anthropology-2024/ku.5.t
  locator: { number: "ku.5.t", headingPath: ["4 Benchmark standards: Knowledge and understanding (table)", ""] }
  span: { start: 60090, end: 60200 }
  source: "Demonstrate understanding of the potential\napplications of anthropological knowledge in a variety of contexts."
  stem: none
  statementType: threshold
  rung: threshold
  force: threshold
  level: fheq:6
  appliesTo: "all honours graduates in the subject"
  addressee: learner
  verbs: ["Demonstrate"]
  about: "uses of anthropological knowledge"
  themes: [none]
  domain: understanding
  award: ["bachelor's with honours"]
  gradeOf: none
  paraphrase: "As the minimum for the honours degree, the graduate will have shown that they can show an understanding of how anthropological knowledge might be put to use in different settings."
  quote: full   # the issuer's statement is in `source` (D-std-0014)
  audience: both
  subjects: inherited
- id: qaa/anthropology-2024/ku.6.e
  locator: { number: "ku.6.e", headingPath: ["4 Benchmark standards: Knowledge and understanding (table)", ""] }
  span: { start: 60454, end: 60600 }
  source: "Show critical awareness of the specific properties of different forms of data and how they may be integrated and generate novel forms in response."
  stem: none
  statementType: excellent
  rung: excellent
  force: describes
  level: fheq:6
  appliesTo: "all honours graduates in the subject"
  addressee: learner
  verbs: ["Show", "integrated", "generate"]
  about: "properties of data forms and combining them"
  themes: [none]
  domain: understanding
  award: ["bachelor's with honours"]
  gradeOf: { statement: qaa/anthropology-2024/ku.6.t, basis: inferred }
  paraphrase: "Strong or excellent performance goes beyond the threshold: the graduate can understand critically what sets different kinds of data apart and how they can be combined to produce new forms in reply."
  quote: full   # the issuer's statement is in `source` (D-std-0014)
  audience: both
  subjects: inherited
- id: qaa/anthropology-2024/ku.6.t
  locator: { number: "ku.6.t", headingPath: ["4 Benchmark standards: Knowledge and understanding (table)", ""] }
  span: { start: 60314, end: 60452 }
  source: "Interpret and analyse a variety of oral, textual,\nmusical, visual and other forms, and show awareness of the different properties of each."
  stem: none
  statementType: threshold
  rung: threshold
  force: threshold
  level: fheq:6
  appliesTo: "all honours graduates in the subject"
  addressee: learner
  verbs: ["Interpret", "analyse", "show"]
  about: "interpreting oral, textual, visual and other forms"
  themes: [none]
  domain: understanding
  award: ["bachelor's with honours"]
  gradeOf: none
  paraphrase: "As the minimum for the honours degree, the graduate will have shown that they can read and analyse many kinds of material, spoken, written, musical, visual and more, and know how each kind differs."
  quote: full   # the issuer's statement is in `source` (D-std-0014)
  audience: both
  subjects: inherited
- id: qaa/anthropology-2024/ku.7.e
  locator: { number: "ku.7.e", headingPath: ["4 Benchmark standards: Knowledge and understanding (table)", ""] }
  span: { start: 60693, end: 60820 }
  source: "Show critical ability to integrate and transcend multiple academic disciplines in understanding human physiology and behaviour."
  stem: none
  statementType: excellent
  rung: excellent
  force: describes
  level: fheq:6
  appliesTo: "all honours graduates in the subject"
  addressee: learner
  verbs: ["Show", "integrate", "transcend"]
  about: "integrating and going beyond disciplines"
  themes: [none]
  domain: understanding
  award: ["bachelor's with honours"]
  gradeOf: { statement: qaa/anthropology-2024/ku.7.t, basis: inferred }
  paraphrase: "Strong or excellent performance goes beyond the threshold: the graduate can draw several disciplines together, and move past their limits, to understand human bodies and behaviour."
  quote: full   # the issuer's statement is in `source` (D-std-0014)
  audience: both
  subjects: inherited
- id: qaa/anthropology-2024/ku.7.t
  locator: { number: "ku.7.t", headingPath: ["4 Benchmark standards: Knowledge and understanding (table)", ""] }
  span: { start: 60604, end: 60691 }
  source: "Indicate a critical awareness of how\nAnthropology is related to other cognate subjects."
  stem: none
  statementType: threshold
  rung: threshold
  force: threshold
  level: fheq:6
  appliesTo: "all honours graduates in the subject"
  addressee: learner
  verbs: ["Indicate"]
  about: "links with cognate subjects"
  themes: [none]
  domain: understanding
  award: ["bachelor's with honours"]
  gradeOf: none
  paraphrase: "As the minimum for the honours degree, the graduate will have shown that they can show critical awareness of how the subject connects with neighbouring disciplines."
  quote: full   # the issuer's statement is in `source` (D-std-0014)
  audience: both
  subjects: inherited
- id: qaa/anthropology-2024/ku.8.e
  locator: { number: "ku.8.e", headingPath: ["4 Benchmark standards: Knowledge and understanding (table)", ""] }
  span: { start: 60977, end: 61196 }
  source: "Show critical appreciation of, and be able to analyse using a variety of techniques, the complex interactions between human social and\n\ncultural systems, human physiological variability, and environments and ecosystems."
  stem: none
  statementType: excellent
  rung: excellent
  force: describes
  level: fheq:6
  appliesTo: "all honours graduates in the subject"
  addressee: learner
  verbs: ["Show", "analyse"]
  about: "analysing how culture, biology and environment interact"
  themes: [none]
  domain: understanding
  award: ["bachelor's with honours"]
  gradeOf: { statement: qaa/anthropology-2024/ku.8.t, basis: inferred }
  paraphrase: "Strong or excellent performance goes beyond the threshold: the graduate can appreciate critically, and analyse by several techniques, the complex ways in which social and cultural systems, human physical variation and ecosystems act on one another."
  quote: full   # the issuer's statement is in `source` (D-std-0014)
  audience: both
  subjects: inherited
- id: qaa/anthropology-2024/ku.8.t
  locator: { number: "ku.8.t", headingPath: ["4 Benchmark standards: Knowledge and understanding (table)", ""] }
  span: { start: 60824, end: 60975 }
  source: "Appreciate the dynamic interrelationship\nbetween human social and cultural diversity, physiological diversity and physical environments and ecosystems."
  stem: none
  statementType: threshold
  rung: threshold
  force: threshold
  level: fheq:6
  appliesTo: "all honours graduates in the subject"
  addressee: learner
  verbs: ["Appreciate"]
  about: "links between human diversity and environments"
  themes: [none]
  domain: understanding
  award: ["bachelor's with honours"]
  gradeOf: none
  paraphrase: "As the minimum for the honours degree, the graduate will have shown that they can recognise how social and cultural variety, bodily variety and the physical world and its ecosystems shape one another over time."
  quote: full   # the issuer's statement is in `source` (D-std-0014)
  audience: both
  subjects: inherited
- id: qaa/anthropology-2024/ku.9.e
  locator: { number: "ku.9.e", headingPath: ["4 Benchmark standards: Knowledge and understanding (table)", ""] }
  span: { start: 61423, end: 61808 }
  source: "Critically evaluate the implications of evidence for disparities in experience, including health, status among and between human, hominin and/or primate populations today and in the past; evaluate the significance for understanding social and cultural inequity; and consider the role of political and social\n\n19\nprocesses and how they might be mitigated among contemporary populations."
  stem: none
  statementType: excellent
  rung: excellent
  force: describes
  level: fheq:6
  appliesTo: "all honours graduates in the subject"
  addressee: learner
  verbs: ["evaluate", "consider", "mitigated"]
  about: "evidence for disparities and how to ease them"
  themes: [none]
  domain: knowledge
  award: ["bachelor's with honours"]
  gradeOf: { statement: qaa/anthropology-2024/ku.9.t, basis: inferred }
  paraphrase: "Strong or excellent performance goes beyond the threshold: the graduate can judge critically what the evidence on unequal experience, health and status among humans, hominins and primates implies; assess what it shows about social and cultural inequity; and consider how political and social processes play a part and might be eased in living populations."
  quote: full   # the issuer's statement is in `source` (D-std-0014)
  audience: both
  subjects: inherited
- id: qaa/anthropology-2024/ku.9.t
  locator: { number: "ku.9.t", headingPath: ["4 Benchmark standards: Knowledge and understanding (table)", ""] }
  span: { start: 61199, end: 61421 }
  source: "Demonstrate an awareness of the social,\ncultural and biological variables influencing disparities of experience, including health, status, within and between human, hominin and/or primate populations today and in the past."
  stem: none
  statementType: threshold
  rung: threshold
  force: threshold
  level: fheq:6
  appliesTo: "all honours graduates in the subject"
  addressee: learner
  verbs: ["Demonstrate"]
  about: "the factors behind unequal experience"
  themes: [none]
  domain: knowledge
  award: ["bachelor's with honours"]
  gradeOf: none
  paraphrase: "As the minimum for the honours degree, the graduate will have shown that they can show awareness of the social, cultural and biological factors behind differences in experience, such as health or status, within and across human, hominin or primate groups, past and present."
  quote: full   # the issuer's statement is in `source` (D-std-0014)
  audience: both
  subjects: inherited
- id: qaa/anthropology-2024/ku.10.e
  locator: { number: "ku.10.e", headingPath: ["4 Benchmark standards: Knowledge and understanding (table)", ""] }
  span: { start: 61983, end: 62159 }
  source: "Critically evaluate a range of key concepts, theories and research methods applicable across Anthropology, evaluate their use, and be able to apply some of these appropriately."
  stem: none
  statementType: excellent
  rung: excellent
  force: describes
  level: fheq:6
  appliesTo: "all honours graduates in the subject"
  addressee: learner
  verbs: ["evaluate", "apply"]
  about: "evaluating and applying concepts, theories and methods"
  themes: [none]
  domain: understanding
  award: ["bachelor's with honours"]
  gradeOf: { statement: qaa/anthropology-2024/ku.10.t, basis: inferred }
  paraphrase: "Strong or excellent performance goes beyond the threshold: the graduate can assess critically the subject's key concepts, theories and methods, judge how they are used and apply some of them well."
  quote: full   # the issuer's statement is in `source` (D-std-0014)
  audience: both
  subjects: inherited
- id: qaa/anthropology-2024/ku.10.t
  locator: { number: "ku.10.t", headingPath: ["4 Benchmark standards: Knowledge and understanding (table)", ""] }
  span: { start: 61812, end: 61982 }
  source: "Describe and appreciate the main strengths\nand weaknesses of a range of key concepts, theories and research methods applicable across Anthropology and evaluate their use."
  stem: none
  statementType: threshold
  rung: threshold
  force: threshold
  level: fheq:6
  appliesTo: "all honours graduates in the subject"
  addressee: learner
  verbs: ["Describe", "appreciate", "evaluate"]
  about: "strengths and weaknesses of concepts, theories and methods"
  themes: [none]
  domain: understanding
  award: ["bachelor's with honours"]
  gradeOf: none
  paraphrase: "As the minimum for the honours degree, the graduate will have shown that they can set out the main strengths and weaknesses of the subject's key concepts, theories and methods and judge how they are used."
  quote: full   # the issuer's statement is in `source` (D-std-0014)
  audience: both
  subjects: inherited
- id: qaa/anthropology-2024/ku.11.e
  locator: { number: "ku.11.e", headingPath: ["4 Benchmark standards: Knowledge and understanding (table)", ""] }
  span: { start: 62363, end: 62517 }
  source: "Show critical insight into past and ongoing debates on human societies and cultures and their application to studying human social and cultural diversity."
  stem: none
  statementType: excellent
  rung: excellent
  force: describes
  level: fheq:6
  appliesTo: "honours graduates on degrees mainly in Social Anthropology"
  addressee: learner
  verbs: ["Show"]
  about: "debates on human societies and their use"
  themes: [none]
  domain: knowledge
  award: ["bachelor's with honours"]
  gradeOf: { statement: qaa/anthropology-2024/ku.11.t, basis: inferred }
  paraphrase: "Strong or excellent performance goes beyond the threshold: the graduate can show critical insight into past and present arguments about human societies and cultures, and into how they help in studying social and cultural variety."
  quote: full   # the issuer's statement is in `source` (D-std-0014)
  audience: both
  subjects: inherited
- id: qaa/anthropology-2024/ku.11.t
  locator: { number: "ku.11.t", headingPath: ["4 Benchmark standards: Knowledge and understanding (table)", ""] }
  span: { start: 62222, end: 62361 }
  source: "Describe the historical development of Social\nAnthropology and social theory more generally and be aware of current debates in these areas."
  stem: none
  statementType: threshold
  rung: threshold
  force: threshold
  level: fheq:6
  appliesTo: "honours graduates on degrees mainly in Social Anthropology"
  addressee: learner
  verbs: ["Describe"]
  about: "the history of Social Anthropology and social theory"
  themes: [none]
  domain: knowledge
  award: ["bachelor's with honours"]
  gradeOf: none
  paraphrase: "As the minimum for the honours degree, the graduate will have shown that they can outline how Social Anthropology and wider social theory developed, and know the arguments now current in both."
  quote: full   # the issuer's statement is in `source` (D-std-0014)
  audience: both
  subjects: inherited
- id: qaa/anthropology-2024/ku.12.e
  locator: { number: "ku.12.e", headingPath: ["4 Benchmark standards: Knowledge and understanding (table)", ""] }
  span: { start: 62644, end: 62803 }
  source: "Critically evaluate and design analyses to understand the nature and causes of the social and cultural diversity of contemporary humans and their implications."
  stem: none
  statementType: excellent
  rung: excellent
  force: describes
  level: fheq:6
  appliesTo: "honours graduates on degrees mainly in Social Anthropology"
  addressee: learner
  verbs: ["evaluate", "design", "understand"]
  about: "designing analyses of social and cultural diversity"
  themes: [none]
  domain: understanding
  award: ["bachelor's with honours"]
  gradeOf: { statement: qaa/anthropology-2024/ku.12.t, basis: inferred }
  paraphrase: "Strong or excellent performance goes beyond the threshold: the graduate can evaluate critically, and design, analyses that explain the nature and causes of social and cultural variety among people today and what follows from it."
  quote: full   # the issuer's statement is in `source` (D-std-0014)
  audience: both
  subjects: inherited
- id: qaa/anthropology-2024/ku.12.t
  locator: { number: "ku.12.t", headingPath: ["4 Benchmark standards: Knowledge and understanding (table)", ""] }
  span: { start: 62522, end: 62643 }
  source: "Describe, analyse and discuss aspects of the\nsocial and cultural diversity of contemporary humans and their implications."
  stem: none
  statementType: threshold
  rung: threshold
  force: threshold
  level: fheq:6
  appliesTo: "honours graduates on degrees mainly in Social Anthropology"
  addressee: learner
  verbs: ["Describe", "analyse", "discuss"]
  about: "social and cultural diversity today"
  themes: [none]
  domain: understanding
  award: ["bachelor's with honours"]
  gradeOf: none
  paraphrase: "As the minimum for the honours degree, the graduate will have shown that they can describe, analyse and talk through aspects of social and cultural variety among people today and what follows from it."
  quote: full   # the issuer's statement is in `source` (D-std-0014)
  audience: both
  subjects: inherited
- id: qaa/anthropology-2024/ku.13.e
  locator: { number: "ku.13.e", headingPath: ["4 Benchmark standards: Knowledge and understanding (table)", ""] }
  span: { start: 62939, end: 63195 }
  source: "In-depth knowledge and understanding of a specific region, culture or group, or of a specific aspect of human culture and society, and ability to explain how this region, culture, group or aspect of culture fits into the broader picture of human diversity."
  stem: none
  statementType: excellent
  rung: excellent
  force: describes
  level: fheq:6
  appliesTo: "honours graduates on degrees mainly in Social Anthropology"
  addressee: learner
  verbs: ["explain"]
  about: "placing a specialism in the wider picture of diversity"
  themes: [none]
  domain: knowledge
  award: ["bachelor's with honours"]
  gradeOf: { statement: qaa/anthropology-2024/ku.13.t, basis: inferred }
  paraphrase: "Strong or excellent performance goes beyond the threshold: the graduate can hold that deep knowledge and also explain where the chosen region, culture, group or aspect sits within human variety as a whole."
  quote: full   # the issuer's statement is in `source` (D-std-0014)
  audience: both
  subjects: inherited
- id: qaa/anthropology-2024/ku.13.t
  locator: { number: "ku.13.t", headingPath: ["4 Benchmark standards: Knowledge and understanding (table)", ""] }
  span: { start: 62807, end: 62937 }
  source: "In-depth knowledge and understanding of a\nspecific region, culture or group, or of a specific aspect of human culture and society."
  stem: none
  statementType: threshold
  rung: threshold
  force: threshold
  level: fheq:6
  appliesTo: "honours graduates on degrees mainly in Social Anthropology"
  addressee: learner
  verbs: []
  about: "in-depth knowledge of a region, culture, group or aspect"
  themes: [none]
  domain: knowledge
  award: ["bachelor's with honours"]
  gradeOf: none
  paraphrase: "As the minimum for the honours degree, the graduate will have shown that they can show deep knowledge and understanding of one region, culture or group, or of one aspect of human society and culture."
  quote: full   # the issuer's statement is in `source` (D-std-0014)
  audience: both
  subjects: inherited
- id: qaa/anthropology-2024/ku.14.e
  locator: { number: "ku.14.e", headingPath: ["4 Benchmark standards: Knowledge and understanding (table)", ""] }
  span: { start: 63316, end: 63459 }
  source: "Appreciation and critical understanding of the ways in which human social and cultural diversity relates to human ecodynamics (and vice versa)."
  stem: none
  statementType: excellent
  rung: excellent
  force: describes
  level: fheq:6
  appliesTo: "honours graduates on degrees mainly in Social Anthropology"
  addressee: learner
  verbs: []
  about: "critical understanding of diversity and ecodynamics"
  themes: [none]
  domain: understanding
  award: ["bachelor's with honours"]
  gradeOf: { statement: qaa/anthropology-2024/ku.14.t, basis: inferred }
  paraphrase: "Strong or excellent performance goes beyond the threshold: the graduate can appreciate, and understand critically, how social and cultural variety and human ecodynamics bear on each other in both directions."
  quote: full   # the issuer's statement is in `source` (D-std-0014)
  audience: both
  subjects: inherited
- id: qaa/anthropology-2024/ku.14.t
  locator: { number: "ku.14.t", headingPath: ["4 Benchmark standards: Knowledge and understanding (table)", ""] }
  span: { start: 63199, end: 63315 }
  source: "Appreciation of the ways in which human\nsocial and cultural diversity relates to human ecodynamics (and vice versa)."
  stem: none
  statementType: threshold
  rung: threshold
  force: threshold
  level: fheq:6
  appliesTo: "honours graduates on degrees mainly in Social Anthropology"
  addressee: learner
  verbs: []
  about: "social diversity and human ecodynamics"
  themes: [none]
  domain: understanding
  award: ["bachelor's with honours"]
  gradeOf: none
  paraphrase: "As the minimum for the honours degree, the graduate will have shown that they can appreciate how social and cultural variety and human ecodynamics bear on each other in both directions."
  quote: full   # the issuer's statement is in `source` (D-std-0014)
  audience: both
  subjects: inherited
- id: qaa/anthropology-2024/ku.15.e
  locator: { number: "ku.15.e", headingPath: ["4 Benchmark standards: Knowledge and understanding (table)", ""] }
  span: { start: 63894, end: 64116 }
  source: "Show critical insight into ongoing debates on ethical practice of Biological Anthropology, evaluate others' research in this regard, and design and conduct ethical research, academic practice, dissemination and engagement."
  stem: none
  statementType: excellent
  rung: excellent
  force: describes
  level: fheq:6
  appliesTo: "honours graduates on degrees mainly in Biological Anthropology"
  addressee: learner
  verbs: ["Show", "evaluate", "design", "conduct"]
  about: "ethical research, evaluation and engagement"
  themes: [none]
  domain: understanding
  award: ["bachelor's with honours"]
  gradeOf: { statement: qaa/anthropology-2024/ku.15.t, basis: inferred }
  paraphrase: "Strong or excellent performance goes beyond the threshold: the graduate can show critical insight into current debates on ethics in Biological Anthropology, judge others' research on that basis and design and carry out ethical research, scholarship, dissemination and engagement."
  quote: full   # the issuer's statement is in `source` (D-std-0014)
  audience: both
  subjects: inherited
- id: qaa/anthropology-2024/ku.15.t
  locator: { number: "ku.15.t", headingPath: ["4 Benchmark standards: Knowledge and understanding (table)", ""] }
  span: { start: 63526, end: 63893 }
  source: "Describe key debates in the ethical practice\nof Biological Anthropology in the past and today, including not only in data collection but also the make-up of the international discipline and of the institution of academia generally; appreciate the relevance and importance of ethical practice and equitable collaboration with the 'subjects' of anthropological enquiry."
  stem: none
  statementType: threshold
  rung: threshold
  force: threshold
  level: fheq:6
  appliesTo: "honours graduates on degrees mainly in Biological Anthropology"
  addressee: learner
  verbs: ["Describe", "appreciate"]
  about: "ethical practice in Biological Anthropology"
  themes: [none]
  domain: understanding
  award: ["bachelor's with honours"]
  gradeOf: none
  paraphrase: "As the minimum for the honours degree, the graduate will have shown that they can describe past and present debates on ethics in Biological Anthropology, covering data collection, who makes up the international discipline and how academia is organised, and recognise why ethical practice and fair collaboration with the people studied matter."
  quote: full   # the issuer's statement is in `source` (D-std-0014)
  audience: both
  subjects: inherited
- id: qaa/anthropology-2024/ku.16.e
  locator: { number: "ku.16.e", headingPath: ["4 Benchmark standards: Knowledge and understanding (table)", ""] }
  span: { start: 64328, end: 64637 }
  source: "Critically evaluate and design analyses to understand the nature and causes of biological diversity and its sociocultural as well as ecological implications among contemporary humans and/or other primates, and the complex interplay between social, cultural and environmental variables from which these result."
  stem: none
  statementType: excellent
  rung: excellent
  force: describes
  level: fheq:6
  appliesTo: "honours graduates on degrees mainly in Biological Anthropology"
  addressee: learner
  verbs: ["evaluate", "design", "understand"]
  about: "designing analyses of biological diversity"
  themes: [none]
  domain: understanding
  award: ["bachelor's with honours"]
  gradeOf: { statement: qaa/anthropology-2024/ku.16.t, basis: inferred }
  paraphrase: "Strong or excellent performance goes beyond the threshold: the graduate can evaluate critically, and design, analyses that explain the nature and causes of biological variety among living humans or other primates, its social, cultural and ecological consequences and the tangle of social, cultural and environmental factors that produce it."
  quote: full   # the issuer's statement is in `source` (D-std-0014)
  audience: both
  subjects: inherited
- id: qaa/anthropology-2024/ku.16.t
  locator: { number: "ku.16.t", headingPath: ["4 Benchmark standards: Knowledge and understanding (table)", ""] }
  span: { start: 64120, end: 64327 }
  source: "Describe, analyse and discuss aspects of the\nbiological diversity of contemporary humans and other primates and show awareness of the social and cultural as well as ecological implications of such diversity."
  stem: none
  statementType: threshold
  rung: threshold
  force: threshold
  level: fheq:6
  appliesTo: "honours graduates on degrees mainly in Biological Anthropology"
  addressee: learner
  verbs: ["Describe", "analyse", "discuss", "show"]
  about: "biological diversity of humans and primates"
  themes: [none]
  domain: understanding
  award: ["bachelor's with honours"]
  gradeOf: none
  paraphrase: "As the minimum for the honours degree, the graduate will have shown that they can describe, analyse and discuss aspects of biological variety among living humans and other primates, aware of its social, cultural and ecological consequences."
  quote: full   # the issuer's statement is in `source` (D-std-0014)
  audience: both
  subjects: inherited
- id: qaa/anthropology-2024/ku.17.e
  locator: { number: "ku.17.e", headingPath: ["4 Benchmark standards: Knowledge and understanding (table)", ""] }
  span: { start: 64814, end: 64968 }
  source: "Show thorough and critical understanding of human physiology and be able to interpret variability, including evolutionary, developmental and pathological."
  stem: none
  statementType: excellent
  rung: excellent
  force: describes
  level: fheq:6
  appliesTo: "honours graduates on degrees mainly in Biological Anthropology"
  addressee: learner
  verbs: ["Show", "interpret"]
  about: "interpreting physiological variability"
  themes: [none]
  domain: knowledge
  award: ["bachelor's with honours"]
  gradeOf: { statement: qaa/anthropology-2024/ku.17.t, basis: inferred }
  paraphrase: "Strong or excellent performance goes beyond the threshold: the graduate can understand human physiology thoroughly and critically and interpret its variation, whether evolutionary, developmental or pathological."
  quote: full   # the issuer's statement is in `source` (D-std-0014)
  audience: both
  subjects: inherited
- id: qaa/anthropology-2024/ku.17.t
  locator: { number: "ku.17.t", headingPath: ["4 Benchmark standards: Knowledge and understanding (table)", ""] }
  span: { start: 64645, end: 64813 }
  source: "Demonstrate a good understanding of\n'normal' human physiology, including skeletal form, its variation and development, and be able to identify major forms of pathology."
  stem: none
  statementType: threshold
  rung: threshold
  force: threshold
  level: fheq:6
  appliesTo: "honours graduates on degrees mainly in Biological Anthropology"
  addressee: learner
  verbs: ["Demonstrate", "identify"]
  about: "normal human physiology and pathology"
  themes: [none]
  domain: knowledge
  award: ["bachelor's with honours"]
  gradeOf: none
  paraphrase: "As the minimum for the honours degree, the graduate will have shown that they can understand typical human physiology well, including the skeleton's form, variation and growth, and recognise the main forms of pathology."
  quote: full   # the issuer's statement is in `source` (D-std-0014)
  audience: both
  subjects: inherited
- id: qaa/anthropology-2024/ku.18.e
  locator: { number: "ku.18.e", headingPath: ["4 Benchmark standards: Knowledge and understanding (table)", ""] }
  span: { start: 65122, end: 65303 }
  source: "Show critical insight into past and ongoing debates on Biological Anthropology and evolutionary theory and their applications in studying human physiological and cultural diversity."
  stem: none
  statementType: excellent
  rung: excellent
  force: describes
  level: fheq:6
  appliesTo: "honours graduates on degrees mainly in Biological Anthropology"
  addressee: learner
  verbs: ["Show"]
  about: "debates on Biological Anthropology and evolutionary theory"
  themes: [none]
  domain: knowledge
  award: ["bachelor's with honours"]
  gradeOf: { statement: qaa/anthropology-2024/ku.18.t, basis: inferred }
  paraphrase: "Strong or excellent performance goes beyond the threshold: the graduate can show critical insight into past and present arguments in Biological Anthropology and evolutionary theory, and into how they help in studying human physical and cultural variety."
  quote: full   # the issuer's statement is in `source` (D-std-0014)
  audience: both
  subjects: inherited
- id: qaa/anthropology-2024/ku.18.t
  locator: { number: "ku.18.t", headingPath: ["4 Benchmark standards: Knowledge and understanding (table)", ""] }
  span: { start: 64972, end: 65121 }
  source: "Describe the historical development of\nBiological Anthropology and evolutionary theory more generally and be aware of current debates in these areas."
  stem: none
  statementType: threshold
  rung: threshold
  force: threshold
  level: fheq:6
  appliesTo: "honours graduates on degrees mainly in Biological Anthropology"
  addressee: learner
  verbs: ["Describe"]
  about: "the history of Biological Anthropology and evolutionary theory"
  themes: [none]
  domain: knowledge
  award: ["bachelor's with honours"]
  gradeOf: none
  paraphrase: "As the minimum for the honours degree, the graduate will have shown that they can outline how Biological Anthropology and wider evolutionary theory developed, and know the arguments now current in both."
  quote: full   # the issuer's statement is in `source` (D-std-0014)
  audience: both
  subjects: inherited
- id: qaa/anthropology-2024/ku.19.e
  locator: { number: "ku.19.e", headingPath: ["4 Benchmark standards: Knowledge and understanding (table)", ""] }
  span: { start: 65530, end: 65838 }
  source: "Critically apply evolutionary theory to understand how the dynamic interrelationship between human physiological, social and cultural evolution has shaped past and present human, hominin and primate physiology, behaviour and cognition; be able to explain how humans fit evolutionarily into the natural world."
  stem: none
  statementType: excellent
  rung: excellent
  force: describes
  level: fheq:6
  appliesTo: "honours graduates on degrees mainly in Biological Anthropology"
  addressee: learner
  verbs: ["apply", "understand", "explain"]
  about: "applying evolutionary theory to human evolution"
  themes: [none]
  domain: knowledge
  award: ["bachelor's with honours"]
  gradeOf: { statement: qaa/anthropology-2024/ku.19.t, basis: inferred }
  paraphrase: "Strong or excellent performance goes beyond the threshold: the graduate can use evolutionary theory critically to show how physical, social and cultural evolution together shaped the bodies, behaviour and cognition of humans, hominins and primates, past and present, and explain how humans fit into nature in evolutionary terms."
  quote: full   # the issuer's statement is in `source` (D-std-0014)
  audience: both
  subjects: inherited
- id: qaa/anthropology-2024/ku.19.t
  locator: { number: "ku.19.t", headingPath: ["4 Benchmark standards: Knowledge and understanding (table)", ""] }
  span: { start: 65307, end: 65529 }
  source: "Describe the basic principles of evolutionary\ntheory and the evolutionary development of human, hominin and primate physiology, behaviour and cognition; demonstrate knowledge of our species' place within the natural world."
  stem: none
  statementType: threshold
  rung: threshold
  force: threshold
  level: fheq:6
  appliesTo: "honours graduates on degrees mainly in Biological Anthropology"
  addressee: learner
  verbs: ["Describe", "demonstrate"]
  about: "evolutionary theory and our place in nature"
  themes: [none]
  domain: knowledge
  award: ["bachelor's with honours"]
  gradeOf: none
  paraphrase: "As the minimum for the honours degree, the graduate will have shown that they can describe the basics of evolutionary theory and how the bodies, behaviour and cognition of humans, hominins and primates evolved, and show knowledge of where our species stands in nature."
  quote: full   # the issuer's statement is in `source` (D-std-0014)
  audience: both
  subjects: inherited
- id: qaa/anthropology-2024/ku.20.e
  locator: { number: "ku.20.e", headingPath: ["4 Benchmark standards: Knowledge and understanding (table)", ""] }
  span: { start: 65986, end: 66235 }
  source: "Critically evaluate hypotheses around the adaptive significance of variability among hominin and other primate species, and to interpret varied information on aspects of human and/or primate biological diversity with regard to adaptive significance."
  stem: none
  statementType: excellent
  rung: excellent
  force: describes
  level: fheq:6
  appliesTo: "honours graduates on degrees mainly in Biological Anthropology"
  addressee: learner
  verbs: ["evaluate", "interpret"]
  about: "hypotheses on adaptive significance"
  themes: [none]
  domain: knowledge
  award: ["bachelor's with honours"]
  gradeOf: { statement: qaa/anthropology-2024/ku.20.t, basis: inferred }
  paraphrase: "Strong or excellent performance goes beyond the threshold: the graduate can evaluate critically hypotheses about why variation among hominins and other primates is adaptive, and interpret varied evidence on human or primate biological variety in those terms."
  quote: full   # the issuer's statement is in `source` (D-std-0014)
  audience: both
  subjects: inherited
- id: qaa/anthropology-2024/ku.20.t
  locator: { number: "ku.20.t", headingPath: ["4 Benchmark standards: Knowledge and understanding (table)", ""] }
  span: { start: 65842, end: 65985 }
  source: "Describe some of the similarities and\ncontrasts among and between humans, hominins and other primates, and discuss their adaptive significance."
  stem: none
  statementType: threshold
  rung: threshold
  force: threshold
  level: fheq:6
  appliesTo: "honours graduates on degrees mainly in Biological Anthropology"
  addressee: learner
  verbs: ["Describe", "discuss"]
  about: "similarities and contrasts among primates"
  themes: [none]
  domain: knowledge
  award: ["bachelor's with honours"]
  gradeOf: none
  paraphrase: "As the minimum for the honours degree, the graduate will have shown that they can describe some likenesses and differences between humans, hominins and other primates and discuss what they mean for adaptation."
  quote: full   # the issuer's statement is in `source` (D-std-0014)
  audience: both
  subjects: inherited
- id: qaa/anthropology-2024/ku.21.e
  locator: { number: "ku.21.e", headingPath: ["4 Benchmark standards: Knowledge and understanding (table)", ""] }
  span: { start: 66403, end: 66569 }
  source: "Show critical insights into the processes, mechanisms and potential causes of geographical and temporal variability during primate and/or hominin and human evolution."
  stem: none
  statementType: excellent
  rung: excellent
  force: describes
  level: fheq:6
  appliesTo: "honours graduates on degrees mainly in Biological Anthropology"
  addressee: learner
  verbs: ["Show"]
  about: "processes behind variability in evolution"
  themes: [none]
  domain: knowledge
  award: ["bachelor's with honours"]
  gradeOf: { statement: qaa/anthropology-2024/ku.21.t, basis: inferred }
  paraphrase: "Strong or excellent performance goes beyond the threshold: the graduate can show critical insight into the processes, mechanisms and likely causes of variation across place and time in primate, hominin and human evolution."
  quote: full   # the issuer's statement is in `source` (D-std-0014)
  audience: both
  subjects: inherited
- id: qaa/anthropology-2024/ku.21.t
  locator: { number: "ku.21.t", headingPath: ["4 Benchmark standards: Knowledge and understanding (table)", ""] }
  span: { start: 66239, end: 66402 }
  source: "Describe the temporal and spatial distribution\nand main physiological and behavioural characteristics of key primate and/or hominin general species as appropriate."
  stem: none
  statementType: threshold
  rung: threshold
  force: threshold
  level: fheq:6
  appliesTo: "honours graduates on degrees mainly in Biological Anthropology"
  addressee: learner
  verbs: ["Describe"]
  about: "distribution and traits of primate and hominin species"
  themes: [none]
  domain: knowledge
  award: ["bachelor's with honours"]
  gradeOf: none
  paraphrase: "As the minimum for the honours degree, the graduate will have shown that they can describe where and when key primate or hominin species lived and their main physical and behavioural traits, as fits the course."
  quote: full   # the issuer's statement is in `source` (D-std-0014)
  audience: both
  subjects: inherited
- id: qaa/anthropology-2024/ku.22.e
  locator: { number: "ku.22.e", headingPath: ["4 Benchmark standards: Knowledge and understanding (table)", ""] }
  span: { start: 66850, end: 67107 }
  source: "Evaluate and synthesise multiple lines of evidence and hypotheses as to the nature, causes and mechanisms of primate and/or hominin and human evolution and variability among homo sapiens, and understand the limitations to interpretations given current data."
  stem: none
  statementType: excellent
  rung: excellent
  force: describes
  level: fheq:6
  appliesTo: "honours graduates on degrees mainly in Biological Anthropology"
  addressee: learner
  verbs: ["Evaluate", "synthesise", "understand"]
  about: "synthesising evidence on evolution and variability"
  themes: [none]
  domain: understanding
  award: ["bachelor's with honours"]
  gradeOf: { statement: qaa/anthropology-2024/ku.22.t, basis: inferred }
  paraphrase: "Strong or excellent performance goes beyond the threshold: the graduate can evaluate and bring together several lines of evidence and hypotheses on how and why primate, hominin and human evolution and variation within our species happened, and know how far present data can support any reading."
  quote: full   # the issuer's statement is in `source` (D-std-0014)
  audience: both
  subjects: inherited
- id: qaa/anthropology-2024/ku.22.t
  locator: { number: "ku.22.t", headingPath: ["4 Benchmark standards: Knowledge and understanding (table)", ""] }
  span: { start: 66573, end: 66849 }
  source: "Appreciate the debates around interpretation\nof the hominin and human fossil and bioarchaeological record, its potential biases, and the role of taphonomy and its implications\n\nfor interpretation and understanding primate and/or hominin and human evolution and the human past."
  stem: none
  statementType: threshold
  rung: threshold
  force: threshold
  level: fheq:6
  appliesTo: "honours graduates on degrees mainly in Biological Anthropology"
  addressee: learner
  verbs: ["Appreciate"]
  about: "interpreting the fossil and bioarchaeological record"
  themes: [none]
  domain: understanding
  award: ["bachelor's with honours"]
  gradeOf: none
  paraphrase: "As the minimum for the honours degree, the graduate will have shown that they can appreciate the arguments over how the hominin and human fossil and bioarchaeological record is read, its likely biases and how taphonomy affects what can be said about evolution and the human past."
  quote: full   # the issuer's statement is in `source` (D-std-0014)
  audience: both
  subjects: inherited
- id: qaa/anthropology-2024/ku.23.e
  locator: { number: "ku.23.e", headingPath: ["4 Benchmark standards: Knowledge and understanding (table)", ""] }
  span: { start: 67292, end: 67408 }
  source: "Critically evaluate key debates around the integration of (palaeo)genetic data with fossil and behavioural datasets."
  stem: none
  statementType: excellent
  rung: excellent
  force: describes
  level: fheq:6
  appliesTo: "honours graduates on degrees mainly in Biological Anthropology"
  addressee: learner
  verbs: ["evaluate"]
  about: "integrating (palaeo)genetic data"
  themes: [none]
  domain: understanding
  award: ["bachelor's with honours"]
  gradeOf: { statement: qaa/anthropology-2024/ku.23.t, basis: inferred }
  paraphrase: "Strong or excellent performance goes beyond the threshold: the graduate can evaluate critically the arguments about combining (palaeo)genetic data with fossil and behavioural evidence."
  quote: full   # the issuer's statement is in `source` (D-std-0014)
  audience: both
  subjects: inherited
- id: qaa/anthropology-2024/ku.23.t
  locator: { number: "ku.23.t", headingPath: ["4 Benchmark standards: Knowledge and understanding (table)", ""] }
  span: { start: 67111, end: 67291 }
  source: "Appreciate the importance of genetic\nevolution and (palaeo)genetic research alongside traditional fossil and behavioural data to understanding human, hominin and primate evolution."
  stem: none
  statementType: threshold
  rung: threshold
  force: threshold
  level: fheq:6
  appliesTo: "honours graduates on degrees mainly in Biological Anthropology"
  addressee: learner
  verbs: ["Appreciate"]
  about: "genetic evidence beside fossil and behavioural data"
  themes: [none]
  domain: understanding
  award: ["bachelor's with honours"]
  gradeOf: none
  paraphrase: "As the minimum for the honours degree, the graduate will have shown that they can recognise why genetic evolution and (palaeo)genetic study matter, alongside fossil and behavioural evidence, for understanding the evolution of humans, hominins and primates."
  quote: full   # the issuer's statement is in `source` (D-std-0014)
  audience: both
  subjects: inherited
- id: qaa/anthropology-2024/ku.24.e
  locator: { number: "ku.24.e", headingPath: ["4 Benchmark standards: Knowledge and understanding (table)", ""] }
  span: { start: 67721, end: 67888 }
  source: "Critically evaluate key debates around the integration of different types of data; ability to evaluate and synthesise multiple lines of evidence into a coherent whole."
  stem: none
  statementType: excellent
  rung: excellent
  force: describes
  level: fheq:6
  appliesTo: "honours graduates on degrees mainly in Biological Anthropology"
  addressee: learner
  verbs: ["evaluate", "synthesise"]
  about: "integrating and synthesising types of evidence"
  themes: [none]
  domain: knowledge
  award: ["bachelor's with honours"]
  gradeOf: { statement: qaa/anthropology-2024/ku.24.t, basis: inferred }
  paraphrase: "Strong or excellent performance goes beyond the threshold: the graduate can evaluate critically the arguments about combining different kinds of data, and bring several lines of evidence together into a coherent account."
  quote: full   # the issuer's statement is in `source` (D-std-0014)
  audience: both
  subjects: inherited
- id: qaa/anthropology-2024/ku.24.t
  locator: { number: "ku.24.t", headingPath: ["4 Benchmark standards: Knowledge and understanding (table)", ""] }
  span: { start: 67412, end: 67720 }
  source: "Be aware of the multiple lines of evidence\navailable for understanding human, hominin and primate biological diversity, including fossil and skeletal evidence, ethology, primatology and ethnography, archaeological evidence, and (palaeo)genetics and molecular Anthropology, and their strengths and weaknesses."
  stem: none
  statementType: threshold
  rung: threshold
  force: threshold
  level: fheq:6
  appliesTo: "honours graduates on degrees mainly in Biological Anthropology"
  addressee: learner
  verbs: []
  about: "lines of evidence for biological diversity"
  themes: [none]
  domain: knowledge
  award: ["bachelor's with honours"]
  gradeOf: none
  paraphrase: "As the minimum for the honours degree, the graduate will have shown that they can know the many kinds of evidence for human, hominin and primate biological variety, from fossils and skeletons, behaviour studies, primatology and ethnography to archaeology, genetics and molecular work, with the strengths and weaknesses of each."
  quote: full   # the issuer's statement is in `source` (D-std-0014)
  audience: both
  subjects: inherited
- id: qaa/anthropology-2024/ss.1.e
  locator: { number: "ss.1.e", headingPath: ["4 Benchmark standards: Subject-specific skills (table)", ""] }
  span: { start: 68205, end: 68351 }
  source: "Be able to design and implement a programme of research from identification of appropriate research questions through to dissemination of results."
  stem: none
  statementType: excellent
  rung: excellent
  force: describes
  level: fheq:6
  appliesTo: "all honours graduates in the subject"
  addressee: learner
  verbs: ["design", "implement"]
  about: "designing and running a whole research programme"
  themes: [none]
  domain: subject-skill
  award: ["bachelor's with honours"]
  gradeOf: { statement: qaa/anthropology-2024/ss.1.t, basis: inferred }
  paraphrase: "Strong or excellent performance goes beyond the threshold: the graduate can plan and carry through a research programme, from choosing suitable questions to sharing the results."
  quote: full   # the issuer's statement is in `source` (D-std-0014)
  audience: both
  subjects: inherited
- id: qaa/anthropology-2024/ss.1.t
  locator: { number: "ss.1.t", headingPath: ["4 Benchmark standards: Subject-specific skills (table)", ""] }
  span: { start: 67970, end: 68203 }
  source: "Understand the main elements involved in the\ndesign and implementation of practical or field work in order to collect primary data, including ethical evaluation and risk assessment; be able to evaluate such research and its findings."
  stem: none
  statementType: threshold
  rung: threshold
  force: threshold
  level: fheq:6
  appliesTo: "all honours graduates in the subject"
  addressee: learner
  verbs: ["Understand", "evaluate"]
  about: "designing and running fieldwork and practical work"
  themes: [none]
  domain: subject-skill
  award: ["bachelor's with honours"]
  gradeOf: none
  paraphrase: "As the minimum for the honours degree, the graduate will have shown that they can understand what goes into planning and carrying out practical or field research to gather primary data, ethics review and risk assessment included, and evaluate such research and what it finds."
  quote: full   # the issuer's statement is in `source` (D-std-0014)
  audience: both
  subjects: inherited
- id: qaa/anthropology-2024/ss.2.e
  locator: { number: "ss.2.e", headingPath: ["4 Benchmark standards: Subject-specific skills (table)", ""] }
  span: { start: 68438, end: 68545 }
  source: "Be able to critically evaluate the linkages and influences and articulate how the two influence each other."
  stem: none
  statementType: excellent
  rung: excellent
  force: describes
  level: fheq:6
  appliesTo: "all honours graduates in the subject"
  addressee: learner
  verbs: ["evaluate", "articulate"]
  about: "evaluating how social and biological contexts interact"
  themes: [none]
  domain: subject-skill
  award: ["bachelor's with honours"]
  gradeOf: { statement: qaa/anthropology-2024/ss.2.t, basis: inferred }
  paraphrase: "Strong or excellent performance goes beyond the threshold: the graduate can evaluate those connections critically and explain clearly how each setting shapes the other."
  quote: full   # the issuer's statement is in `source` (D-std-0014)
  audience: both
  subjects: inherited
- id: qaa/anthropology-2024/ss.2.t
  locator: { number: "ss.2.t", headingPath: ["4 Benchmark standards: Subject-specific skills (table)", ""] }
  span: { start: 68355, end: 68437 }
  source: "Understand how social and biological contexts\nare linked and influence each other."
  stem: none
  statementType: threshold
  rung: threshold
  force: threshold
  level: fheq:6
  appliesTo: "all honours graduates in the subject"
  addressee: learner
  verbs: ["Understand"]
  about: "links between social and biological contexts"
  themes: [none]
  domain: subject-skill
  award: ["bachelor's with honours"]
  gradeOf: none
  paraphrase: "As the minimum for the honours degree, the graduate will have shown that they can understand how social and biological settings connect and shape each other."
  quote: full   # the issuer's statement is in `source` (D-std-0014)
  audience: both
  subjects: inherited
- id: qaa/anthropology-2024/ss.3.e
  locator: { number: "ss.3.e", headingPath: ["4 Benchmark standards: Subject-specific skills (table)", ""] }
  span: { start: 68679, end: 68814 }
  source: "Synthesise information and data and make well- reasoned interpretations in the context of current anthropological knowledge and theory."
  stem: none
  statementType: excellent
  rung: excellent
  force: describes
  level: fheq:6
  appliesTo: "all honours graduates in the subject"
  addressee: learner
  verbs: ["Synthesise", "make"]
  about: "synthesising data into well-argued interpretations"
  themes: [none]
  domain: subject-skill
  award: ["bachelor's with honours"]
  gradeOf: { statement: qaa/anthropology-2024/ss.3.t, basis: inferred }
  paraphrase: "Strong or excellent performance goes beyond the threshold: the graduate can synthesise information and data and draw well-argued readings from them in the light of what the subject currently knows and theorises."
  quote: full   # the issuer's statement is in `source` (D-std-0014)
  audience: both
  subjects: inherited
- id: qaa/anthropology-2024/ss.3.t
  locator: { number: "ss.3.t", headingPath: ["4 Benchmark standards: Subject-specific skills (table)", ""] }
  span: { start: 68549, end: 68677 }
  source: "Summarise information and data and make\nreasoned interpretations in the context of current anthropological knowledge and theory."
  stem: none
  statementType: threshold
  rung: threshold
  force: threshold
  level: fheq:6
  appliesTo: "all honours graduates in the subject"
  addressee: learner
  verbs: ["Summarise", "make"]
  about: "summarising and interpreting data"
  themes: [none]
  domain: subject-skill
  award: ["bachelor's with honours"]
  gradeOf: none
  paraphrase: "As the minimum for the honours degree, the graduate will have shown that they can summarise information and data and draw sensible readings from them in the light of what the subject currently knows and theorises."
  quote: full   # the issuer's statement is in `source` (D-std-0014)
  audience: both
  subjects: inherited
- id: qaa/anthropology-2024/ss.4.e
  locator: { number: "ss.4.e", headingPath: ["4 Benchmark standards: Subject-specific skills (table)", ""] }
  span: { start: 68982, end: 69170 }
  source: "Communicate anthropological ideas, principles, and theories effectively and fluently via a range of different media (including written, verbal and non-verbal and graphical) as appropriate."
  stem: none
  statementType: excellent
  rung: excellent
  force: describes
  level: fheq:6
  appliesTo: "all honours graduates in the subject"
  addressee: learner
  verbs: ["Communicate"]
  about: "communicating clearly and fluently in different media"
  themes: [none]
  domain: subject-skill
  award: ["bachelor's with honours"]
  gradeOf: { statement: qaa/anthropology-2024/ss.4.t, basis: inferred }
  paraphrase: "Strong or excellent performance goes beyond the threshold: the graduate can get anthropological ideas, principles and theories across clearly and fluently in different media, written, spoken, non-verbal and graphic, as suits the task."
  quote: full   # the issuer's statement is in `source` (D-std-0014)
  audience: both
  subjects: inherited
- id: qaa/anthropology-2024/ss.4.t
  locator: { number: "ss.4.t", headingPath: ["4 Benchmark standards: Subject-specific skills (table)", ""] }
  span: { start: 68818, end: 68980 }
  source: "Communicate anthropological ideas, principles\nand theories via a range of different media (including written, verbal and non-verbal and graphical) as appropriate."
  stem: none
  statementType: threshold
  rung: threshold
  force: threshold
  level: fheq:6
  appliesTo: "all honours graduates in the subject"
  addressee: learner
  verbs: ["Communicate"]
  about: "communicating ideas in different media"
  themes: [none]
  domain: subject-skill
  award: ["bachelor's with honours"]
  gradeOf: none
  paraphrase: "As the minimum for the honours degree, the graduate will have shown that they can get anthropological ideas, principles and theories across in different media, written, spoken, non-verbal and graphic, as suits the task."
  quote: full   # the issuer's statement is in `source` (D-std-0014)
  audience: both
  subjects: inherited
- id: qaa/anthropology-2024/ss.5.e
  locator: { number: "ss.5.e", headingPath: ["4 Benchmark standards: Subject-specific skills (table)", ""] }
  span: { start: 69352, end: 69543 }
  source: "Formulate, investigate and discuss anthropologically informed questions, use major theoretical perspectives and concepts in Anthropology and critically assess their strengths and limitations."
  stem: none
  statementType: excellent
  rung: excellent
  force: describes
  level: fheq:6
  appliesTo: "all honours graduates in the subject"
  addressee: learner
  verbs: ["Formulate", "investigate", "discuss", "use", "assess"]
  about: "framing questions and assessing theory critically"
  themes: [none]
  domain: subject-skill
  award: ["bachelor's with honours"]
  gradeOf: { statement: qaa/anthropology-2024/ss.5.t, basis: inferred }
  paraphrase: "Strong or excellent performance goes beyond the threshold: the graduate can frame, investigate and discuss questions shaped by anthropology, using the subject's main theories and concepts and judging their strengths and limits critically."
  quote: full   # the issuer's statement is in `source` (D-std-0014)
  audience: both
  subjects: inherited
- id: qaa/anthropology-2024/ss.5.t
  locator: { number: "ss.5.t", headingPath: ["4 Benchmark standards: Subject-specific skills (table)", ""] }
  span: { start: 69174, end: 69350 }
  source: "Investigate and discuss anthropologically\ninformed questions, use major theoretical perspectives and concepts in Anthropology and identify their main strengths and limitations."
  stem: none
  statementType: threshold
  rung: threshold
  force: threshold
  level: fheq:6
  appliesTo: "all honours graduates in the subject"
  addressee: learner
  verbs: ["Investigate", "discuss", "use", "identify"]
  about: "investigating questions with theory"
  themes: [none]
  domain: subject-skill
  award: ["bachelor's with honours"]
  gradeOf: none
  paraphrase: "As the minimum for the honours degree, the graduate will have shown that they can investigate and discuss questions shaped by anthropology, using the subject's main theories and concepts and naming what they do well and badly."
  quote: full   # the issuer's statement is in `source` (D-std-0014)
  audience: both
  subjects: inherited
- id: qaa/anthropology-2024/ss.6.e
  locator: { number: "ss.6.e", headingPath: ["4 Benchmark standards: Subject-specific skills (table)", ""] }
  span: { start: 69750, end: 70026 }
  source: "Meaningfully engage with cultures, populations and groups different from their own, without foregoing a sense of personal judgement, with an awareness of cultural assumptions, including their own, and an awareness of the ways in which these impact on interpretation of others."
  stem: none
  statementType: excellent
  rung: excellent
  force: describes
  level: fheq:6
  appliesTo: "all honours graduates in the subject"
  addressee: learner
  verbs: ["engage"]
  about: "engaging meaningfully with other cultures"
  themes: [none]
  domain: subject-skill
  award: ["bachelor's with honours"]
  gradeOf: { statement: qaa/anthropology-2024/ss.6.t, basis: inferred }
  paraphrase: "Strong or excellent performance goes beyond the threshold: the graduate can engage meaningfully with cultures, populations and groups unlike their own while keeping a personal judgement, aware of cultural assumptions, their own included, and of how they affect the reading of others."
  quote: full   # the issuer's statement is in `source` (D-std-0014)
  audience: both
  subjects: inherited
- id: qaa/anthropology-2024/ss.6.t
  locator: { number: "ss.6.t", headingPath: ["4 Benchmark standards: Subject-specific skills (table)", ""] }
  span: { start: 69546, end: 69749 }
  source: "Understand the main approaches for engaging\nwith cultures, populations and groups different from their own, and the ways in which cultural assumptions can impact on the interpretation of such engagement."
  stem: none
  statementType: threshold
  rung: threshold
  force: threshold
  level: fheq:6
  appliesTo: "all honours graduates in the subject"
  addressee: learner
  verbs: ["Understand"]
  about: "approaches to engaging with other cultures"
  themes: [none]
  domain: subject-skill
  award: ["bachelor's with honours"]
  gradeOf: none
  paraphrase: "As the minimum for the honours degree, the graduate will have shown that they can understand the main ways of engaging with cultures, populations and groups unlike their own, and how cultural assumptions can colour what is made of that engagement."
  quote: full   # the issuer's statement is in `source` (D-std-0014)
  audience: both
  subjects: inherited
- id: qaa/anthropology-2024/ss.7.e
  locator: { number: "ss.7.e", headingPath: ["4 Benchmark standards: Subject-specific skills (table)", ""] }
  span: { start: 70301, end: 70694 }
  source: "Critically read and interpret sources including print, oral, film, multimedia, within their historical, social, cultural and theoretical contexts and demonstrate practical awareness of the strengths and limitations of different types\n\nof source and individual sources. Be able to integrate and synthesise multiple such sources to create new responses and interpretations in a variety of media."
  stem: none
  statementType: excellent
  rung: excellent
  force: describes
  level: fheq:6
  appliesTo: "all honours graduates in the subject"
  addressee: learner
  verbs: ["read", "interpret", "demonstrate", "integrate", "synthesise", "create"]
  about: "combining sources into new interpretations"
  themes: [none]
  domain: subject-skill
  award: ["bachelor's with honours"]
  gradeOf: { statement: qaa/anthropology-2024/ss.7.t, basis: inferred }
  paraphrase: "Strong or excellent performance goes beyond the threshold: the graduate can do all that and also combine many such sources into fresh responses and interpretations in a range of media."
  quote: full   # the issuer's statement is in `source` (D-std-0014)
  audience: both
  subjects: inherited
- id: qaa/anthropology-2024/ss.7.t
  locator: { number: "ss.7.t", headingPath: ["4 Benchmark standards: Subject-specific skills (table)", ""] }
  span: { start: 70029, end: 70299 }
  source: "Critically read and interpret sources, including\nprint, oral, film, multimedia, within their historical, social, cultural and theoretical contexts, and demonstrate practical awareness\n\nof the strengths and limitations of different types of source and individual sources."
  stem: none
  statementType: threshold
  rung: threshold
  force: threshold
  level: fheq:6
  appliesTo: "all honours graduates in the subject"
  addressee: learner
  verbs: ["read", "interpret", "demonstrate"]
  about: "reading sources in context"
  themes: [none]
  domain: subject-skill
  award: ["bachelor's with honours"]
  gradeOf: none
  paraphrase: "As the minimum for the honours degree, the graduate will have shown that they can read and interpret sources of many kinds, print, oral, film and multimedia, critically and in their historical, social, cultural and theoretical settings, knowing in practice what each type and each source can and cannot offer."
  quote: full   # the issuer's statement is in `source` (D-std-0014)
  audience: both
  subjects: inherited
- id: qaa/anthropology-2024/ss.8.e
  locator: { number: "ss.8.e", headingPath: ["4 Benchmark standards: Subject-specific skills (table)", ""] }
  span: { start: 70835, end: 71016 }
  source: "Recognise and be able to evaluate applications of anthropological knowledge in a variety of contexts from the personal to international policy; be able to design novel applications."
  stem: none
  statementType: excellent
  rung: excellent
  force: describes
  level: fheq:6
  appliesTo: "all honours graduates in the subject"
  addressee: learner
  verbs: ["Recognise", "evaluate", "design"]
  about: "evaluating and designing applications"
  themes: [none]
  domain: subject-skill
  award: ["bachelor's with honours"]
  gradeOf: { statement: qaa/anthropology-2024/ss.8.t, basis: inferred }
  paraphrase: "Strong or excellent performance goes beyond the threshold: the graduate can recognise and evaluate uses of anthropological knowledge in settings from personal life to international policy, and design new ones."
  quote: full   # the issuer's statement is in `source` (D-std-0014)
  audience: both
  subjects: inherited
- id: qaa/anthropology-2024/ss.8.t
  locator: { number: "ss.8.t", headingPath: ["4 Benchmark standards: Subject-specific skills (table)", ""] }
  span: { start: 70697, end: 70833 }
  source: "Recognise the ways in which anthropological\nknowledge may be applied in a variety of contexts from the personal to international policy."
  stem: none
  statementType: threshold
  rung: threshold
  force: threshold
  level: fheq:6
  appliesTo: "all honours graduates in the subject"
  addressee: learner
  verbs: ["Recognise", "applied"]
  about: "applying knowledge from personal life to policy"
  themes: [none]
  domain: subject-skill
  award: ["bachelor's with honours"]
  gradeOf: none
  paraphrase: "As the minimum for the honours degree, the graduate will have shown that they can recognise how anthropological knowledge can be used in settings that range from personal life to international policy."
  quote: full   # the issuer's statement is in `source` (D-std-0014)
  audience: both
  subjects: inherited
- id: qaa/anthropology-2024/ss.9.e
  locator: { number: "ss.9.e", headingPath: ["4 Benchmark standards: Subject-specific skills (table)", ""] }
  span: { start: 71157, end: 71327 }
  source: "Recognise and be able to critically analyse the politics of language, indirect forms of communication and theoretical statements, forms of power, and claims to authority."
  stem: none
  statementType: excellent
  rung: excellent
  force: describes
  level: fheq:6
  appliesTo: "all honours graduates in the subject"
  addressee: learner
  verbs: ["Recognise", "analyse"]
  about: "analysing the politics of language and authority"
  themes: [none]
  domain: subject-skill
  award: ["bachelor's with honours"]
  gradeOf: { statement: qaa/anthropology-2024/ss.9.t, basis: inferred }
  paraphrase: "Strong or excellent performance goes beyond the threshold: the graduate can recognise and analyse critically the politics of language, indirect communication and theoretical claims, and the workings of power and claims to authority."
  quote: full   # the issuer's statement is in `source` (D-std-0014)
  audience: both
  subjects: inherited
- id: qaa/anthropology-2024/ss.9.t
  locator: { number: "ss.9.t", headingPath: ["4 Benchmark standards: Subject-specific skills (table)", ""] }
  span: { start: 71019, end: 71155 }
  source: "Recognise the politics of language, indirect\nforms of communication and theoretical statements, forms of power, and claims to authority."
  stem: none
  statementType: threshold
  rung: threshold
  force: threshold
  level: fheq:6
  appliesTo: "all honours graduates in the subject"
  addressee: learner
  verbs: ["Recognise"]
  about: "the politics of language and claims to authority"
  themes: [none]
  domain: subject-skill
  award: ["bachelor's with honours"]
  gradeOf: none
  paraphrase: "As the minimum for the honours degree, the graduate will have shown that they can recognise the politics of language, indirect communication and theoretical claims, and the workings of power and claims to authority."
  quote: full   # the issuer's statement is in `source` (D-std-0014)
  audience: both
  subjects: inherited
- id: qaa/anthropology-2024/ss.10.e
  locator: { number: "ss.10.e", headingPath: ["4 Benchmark standards: Subject-specific skills (table)", ""] }
  span: { start: 71668, end: 71957 }
  source: "Meaningfully engage with cultures, populations and groups different from their own, without foregoing a sense of personal judgement, with an awareness of cultural assumptions, including their own, and demonstrate an awareness of the ways in which these impact on interpretation\n\nof others."
  stem: none
  statementType: excellent
  rung: excellent
  force: describes
  level: fheq:6
  appliesTo: "honours graduates on degrees mainly in Social Anthropology"
  addressee: learner
  verbs: ["engage", "demonstrate"]
  about: "meaningful engagement with other cultures"
  themes: [none]
  domain: subject-skill
  award: ["bachelor's with honours"]
  gradeOf: { statement: qaa/anthropology-2024/ss.10.t, basis: inferred }
  paraphrase: "Strong or excellent performance goes beyond the threshold: the graduate can engage meaningfully with cultures, populations and groups unlike their own while keeping a personal judgement, aware of cultural assumptions, their own included, and show that they know how those assumptions affect the reading of others."
  quote: full   # the issuer's statement is in `source` (D-std-0014)
  audience: both
  subjects: inherited
- id: qaa/anthropology-2024/ss.10.t
  locator: { number: "ss.10.t", headingPath: ["4 Benchmark standards: Subject-specific skills (table)", ""] }
  span: { start: 71393, end: 71667 }
  source: "Engage with cultures, population and groups\ndifferent from their own, without foregoing a sense of personal judgement, with an awareness of cultural assumptions, including their own, and demonstrate an awareness of the ways in which these impact on interpretation of others."
  stem: none
  statementType: threshold
  rung: threshold
  force: threshold
  level: fheq:6
  appliesTo: "honours graduates on degrees mainly in Social Anthropology"
  addressee: learner
  verbs: ["Engage", "demonstrate"]
  about: "engaging with other cultures with self-awareness"
  themes: [none]
  domain: subject-skill
  award: ["bachelor's with honours"]
  gradeOf: none
  paraphrase: "As the minimum for the honours degree, the graduate will have shown that they can engage with cultures, populations and groups unlike their own while keeping a personal judgement, aware of cultural assumptions, their own included, and show that they know how those assumptions affect the reading of others."
  quote: full   # the issuer's statement is in `source` (D-std-0014)
  audience: both
  subjects: inherited
- id: qaa/anthropology-2024/ss.11.e
  locator: { number: "ss.11.e", headingPath: ["4 Benchmark standards: Subject-specific skills (table)", ""] }
  span: { start: 72213, end: 72394 }
  source: "Critically evaluate and select appropriate techniques for documenting and measuring human, hominin and/or primate physiological variability according to specific research questions."
  stem: none
  statementType: excellent
  rung: excellent
  force: describes
  level: fheq:6
  appliesTo: "honours graduates on degrees mainly in Biological Anthropology"
  addressee: learner
  verbs: ["evaluate", "select"]
  about: "choosing techniques for research questions"
  themes: [none]
  domain: subject-skill
  award: ["bachelor's with honours"]
  gradeOf: { statement: qaa/anthropology-2024/ss.11.t, basis: inferred }
  paraphrase: "Strong or excellent performance goes beyond the threshold: the graduate can evaluate critically and choose the right techniques for recording and measuring physical variation in humans, hominins or primates to suit a given research question."
  quote: full   # the issuer's statement is in `source` (D-std-0014)
  audience: both
  subjects: inherited
- id: qaa/anthropology-2024/ss.11.t
  locator: { number: "ss.11.t", headingPath: ["4 Benchmark standards: Subject-specific skills (table)", ""] }
  span: { start: 72023, end: 72212 }
  source: "Be aware of the diversity of different\ntechniques available to document and measure human, hominin and/or primate physiological variability, and the main strengths\n\nand limitations of each."
  stem: none
  statementType: threshold
  rung: threshold
  force: threshold
  level: fheq:6
  appliesTo: "honours graduates on degrees mainly in Biological Anthropology"
  addressee: learner
  verbs: ["document", "measure"]
  about: "techniques for measuring physical variability"
  themes: [none]
  domain: subject-skill
  award: ["bachelor's with honours"]
  gradeOf: none
  paraphrase: "As the minimum for the honours degree, the graduate will have shown that they can know the range of techniques for recording and measuring physical variation in humans, hominins or primates, with the main strengths and limits of each."
  quote: full   # the issuer's statement is in `source` (D-std-0014)
  audience: both
  subjects: inherited
- id: qaa/anthropology-2024/ss.12.e
  locator: { number: "ss.12.e", headingPath: ["4 Benchmark standards: Subject-specific skills (table)", ""] }
  span: { start: 72743, end: 73095 }
  source: "Appreciate the ethical issues associated with different methods and theories, including those associated with studying primates and hominins other than humans, with handling human remains, and with proposals for the evolutionary\n\nbasis of aspects of human behaviour, and be able to design and apply rigorous ethical standards at all stages of research."
  stem: none
  statementType: excellent
  rung: excellent
  force: describes
  level: fheq:6
  appliesTo: "honours graduates on degrees mainly in Biological Anthropology"
  addressee: learner
  verbs: ["Appreciate", "design", "apply"]
  about: "designing and applying strict ethical standards"
  themes: [none]
  domain: subject-skill
  award: ["bachelor's with honours"]
  gradeOf: { statement: qaa/anthropology-2024/ss.12.t, basis: inferred }
  paraphrase: "Strong or excellent performance goes beyond the threshold: the graduate can appreciate those ethical questions, including work with primates and hominins other than humans, and design and apply strict ethical standards at every stage of research."
  quote: full   # the issuer's statement is in `source` (D-std-0014)
  audience: both
  subjects: inherited
- id: qaa/anthropology-2024/ss.12.t
  locator: { number: "ss.12.t", headingPath: ["4 Benchmark standards: Subject-specific skills (table)", ""] }
  span: { start: 72399, end: 72742 }
  source: "Demonstrate an awareness of ethical issues\nassociated with different methods and theories, including those associated with studying non-human primates, with handling human remains, and with proposals for the evolutionary basis of aspects of human behaviour. Act in accordance with rigorous ethical standards during academic study and research."
  stem: none
  statementType: threshold
  rung: threshold
  force: threshold
  level: fheq:6
  appliesTo: "honours graduates on degrees mainly in Biological Anthropology"
  addressee: learner
  verbs: ["Demonstrate", "Act"]
  about: "ethical issues and conduct in research"
  themes: [none]
  domain: subject-skill
  award: ["bachelor's with honours"]
  gradeOf: none
  paraphrase: "As the minimum for the honours degree, the graduate will have shown that they can show awareness of the ethical questions raised by different methods and theories, including work with non-human primates, handling human remains and claims about the evolutionary roots of human behaviour, and keep to strict ethical standards in study and research."
  quote: full   # the issuer's statement is in `source` (D-std-0014)
  audience: both
  subjects: inherited
```

### S4a Audience versions
<!-- label: both; status: drafted; basis: primary. forPractitioner: for the programme designer or teacher. forBeneficiary: for the student, second person, naming no issuer. author-agent-written: instructions to an AI agent writing about the statement (a course document, a handbook, an outcome, a report). author-agent-dialogue: instructions to an AI agent using the statement in conversation (with a student, a teacher or a programme team). Written fresh from the held text alone (benchmark rule 6; Abbott, 15:42). -->
```yaml
- statement: qaa/anthropology-2024/1.11
  forPractitioner: { text: "Design the degree to be flexible and accessible, with routes in and through it for students from non-traditional backgrounds and for disabled and neurodivergent students; link this with the institution's own support services.", rewrite: light, force: should, status: drafted }
  forBeneficiary: { text: "not-applicable: a duty on the course and the institution; the student meets its effect, not a standard to reach", rewrite: full, force: should, status: drafted }
  author-agent-written: "Treat this as a provider expectation (should) under the accessibility theme, not a student outcome; it holds for the honours degree at every stage. Cite it as QAA (2024), Anthropology Subject Benchmark Statement, para 1.11. Do not claim it sets a legal duty or a measurable target. Set it beside 1.12 and 1.13 on flexible study and assessment, and beside qaa/anthropology-2024/3.23 on fair assessment."
  author-agent-dialogue: "Raise it with a programme team reviewing access, flexibility or support for disabled and neurodivergent students. Frame it for staff as a design expectation and ask: 'Which routes into and through the degree are closed to a student from a non-traditional background?' With a student, do not present it as something they must achieve; point to the support it implies."
- statement: qaa/anthropology-2024/1.21
  forPractitioner: { text: "Build research projects into the course from the first year: students are required to design, run and complete them, and through them develop skills in evidence, uncertainty, ethics, collaboration and communication across media.", rewrite: light, force: must, status: drafted }
  forBeneficiary: { text: "From the start of your studies you must plan, carry out and finish your own research projects; through them you build skills in working with evidence, handling uncertainty, spotting ethical problems, working with others and communicating in many forms.", rewrite: full, force: must, status: drafted }
  author-agent-written: "Treat this as a requirement on students (the issuer's word is 'required'), placed in the enterprise and employability section; it holds through the honours degree at FHEQ Level 6. Cite it as QAA (2024), Anthropology Subject Benchmark Statement, para 1.21. Do not claim it fixes the number or size of projects. Set it beside 1.23 and 3.26, qaa/anthropology-2024/ss.1.t and the FHEQ honours descriptor qaa/fheq-2024/4.15.b6."
  author-agent-dialogue: "Raise it when a student asks why research tasks start so early or what skills they build. Put it plainly: you design and run projects from the beginning, and each one trains skills employers value. Ask: 'Which skill from your last project could you describe to an employer?' Avoid listing the issuer's skills at length."
- statement: qaa/anthropology-2024/1.23
  forPractitioner: { text: "Teach the subject as practice: students are required to do anthropology and not only learn about it, so plan for them to build skills in a range of methods for collecting and analysing data.", rewrite: light, force: must, status: drafted }
  forBeneficiary: { text: "You must do anthropology, not only read about it: you build skills in several ways of collecting and analysing data so you can understand how other people, even those long dead, experience life.", rewrite: full, force: must, status: drafted }
  author-agent-written: "Treat this as a requirement on students ('required') that sets the practical character of the honours degree at FHEQ Level 6. Cite it as QAA (2024), Anthropology Subject Benchmark Statement, para 1.23. Do not claim it names particular methods or hours of practice. Set it beside 1.24 to 1.26, qaa/anthropology-2024/3.1 and the reference framework's strand:application at spine:6."
  author-agent-dialogue: "Raise it when a student or a team asks how much hands-on work the degree needs. Say plainly that the subject is learned by doing it, and ask: 'Which data collection method have you used yourself, not just read about?' Do not read the paragraph aloud."
- statement: qaa/anthropology-2024/1.26
  forPractitioner: { text: "Make methods courses a core part of the programme, matched to its sub-disciplinary focus, with ethics and collaborative work built in; the methods require students to examine their own biases, see research as placed in history and culture and understand how that shapes interpretation.", rewrite: light, force: must, status: drafted }
  forBeneficiary: { text: "Your methods training requires you to question your own biases and assumptions, see that research always comes from a particular time and culture, and understand how that shapes what we make of the present and the past.", rewrite: full, force: must, status: drafted }
  author-agent-written: "Treat this as a requirement on students carried by the methods training ('require'), with a description of how courses deliver it; it holds at FHEQ Level 6 for the honours degree. Cite it as QAA (2024), Anthropology Subject Benchmark Statement, para 1.26. Do not claim it prescribes a methods module of set size. Set it beside qaa/anthropology-2024/ku.4.t, qaa/anthropology-2024/gs.9.t and the FHEQ honours descriptor qaa/fheq-2024/4.15.b4."
  author-agent-dialogue: "Raise it in reflective work, methods teaching or a tutorial about fieldwork. Ask a student: 'Which of your own assumptions did your last piece of research expose?' With staff, frame it as what methods courses must make room for. Avoid lecturing the student in the issuer's words."
- statement: qaa/anthropology-2024/2.9
  forPractitioner: { text: "Weave ethics through the degree, with dedicated modules where useful, and give students chances to consider how different fieldwork practices fit different questions and contexts, produce different outputs and carry different ethical demands.", rewrite: light, force: should, status: drafted }
  forBeneficiary: { text: "not-applicable: a duty on the course to give opportunities; its outcome for the student is 2.10", rewrite: full, force: should, status: drafted }
  author-agent-written: "Treat this as a provider expectation (should) about the opportunities a course gives, not a student outcome. Cite it as QAA (2024), Anthropology Subject Benchmark Statement, para 2.9. Do not claim it requires a standalone ethics module: the issuer says ethics is ideally threaded through the degree. Set it beside the outcome in qaa/anthropology-2024/2.10, qaa/anthropology-2024/3.4 and qaa/anthropology-2024/gs.4.t."
  author-agent-dialogue: "Raise it with a programme team mapping where ethics is taught. Ask: 'At which points do students compare the ethics of different kinds of fieldwork?' Do not put it to a student as a duty of theirs; for students, use 2.10 instead."
- statement: qaa/anthropology-2024/2.10
  forPractitioner: { text: "By graduation, students will have handled sensitive topics, will understand complex ethical issues in their context and will evaluate and develop projects against the highest ethical standards; plan exposure and practice to match.", rewrite: light, force: will, status: drafted }
  forBeneficiary: { text: "By the end of your degree you will have dealt with sensitive topics, you will understand complex ethical questions in their setting and you will be able to judge and shape projects to the highest ethical standards.", rewrite: full, force: will, status: drafted }
  author-agent-written: "Treat this as an expected outcome (will) for every honours graduate at FHEQ Level 6, stated outside the section 4 tables. Cite it as QAA (2024), Anthropology Subject Benchmark Statement, para 2.10. Do not claim it is a threshold column item or that it holds below Level 6. Set it beside qaa/anthropology-2024/2.9, qaa/anthropology-2024/gs.4.t and gs.4.e and Annex D's qaa/fheq-2024/annex-d/cognitive/r3/3rd on deciding in complex situations."
  author-agent-dialogue: "Raise it when a student prepares a project on a sensitive subject or asks what ethical skill the degree expects. Ask: 'What makes this topic sensitive, and how would you protect the people involved?' Keep to plain words and do not read the paragraph aloud."
- statement: qaa/anthropology-2024/2.12
  forPractitioner: { text: "On joint, major-minor and combined routes, students will achieve the core subject-specific and generic skills and add others from the partner subjects; design for interdisciplinary overlap where it helps.", rewrite: light, force: will, status: drafted }
  forBeneficiary: { text: "If you study the subject jointly or as part of a combined degree, you will gain its core subject and general skills and add others from your other subjects, with chances to explore where they meet.", rewrite: full, force: will, status: drafted }
  author-agent-written: "Treat this as an expected outcome (will) for joint, major-minor and combined honours students at FHEQ Level 6. Cite it as QAA (2024), Anthropology Subject Benchmark Statement, para 2.12. Do not claim it says which skills count as core: the tables do not mark them (4.5). Set it beside 4.5, 4.6 and the general rows, for example qaa/anthropology-2024/ss.1.t and qaa/anthropology-2024/gs.1.t."
  author-agent-dialogue: "Raise it when a joint honours student asks whether they meet the same standards as single honours students. Ask: 'Which core skills from this subject does your combination build, and what does your other subject add?' Avoid suggesting they must meet every row of every table."
- statement: qaa/anthropology-2024/2.15
  forPractitioner: { text: "Plan partnerships with communities and organisations that suit the provider's specialisms; in fieldwork, local communities should be treated as partners and, where appropriate, as co-producers of knowledge, engaged in person or online as fits.", rewrite: light, force: should, status: drafted }
  forBeneficiary: { text: "When your fieldwork involves a community, you should treat its members as partners and, where it fits, as people who create knowledge with you; working this way also builds your skills in research design, communication and planning.", rewrite: full, force: should, status: drafted }
  author-agent-written: "Treat this as an expectation (should) on how fieldwork treats local communities, for courses and students alike, at honours level. Cite it as QAA (2024), Anthropology Subject Benchmark Statement, para 2.15. Do not claim it lists required partners: the issuer says its overview is not exhaustive. Set it beside qaa/anthropology-2024/3.4 on equitable collaboration, qaa/anthropology-2024/ku.15.t and the enterprise theme (1.16)."
  author-agent-dialogue: "Raise it when a student plans fieldwork or a team designs community partnerships. Ask: 'How will the community you work with shape the project and share in what it produces?' Do not read the issuer's list of community types aloud."
- statement: qaa/anthropology-2024/2.18
  forPractitioner: { text: "Introduce students, within the course and their career planning, to the resources and networks of the relevant professional organisations, chiefly BABAO and the RAI.", rewrite: light, force: should, status: drafted }
  forBeneficiary: { text: "not-applicable: a duty on the course; the student benefits from the introduction", rewrite: full, force: should, status: drafted }
  author-agent-written: "Treat this as a provider expectation (should) for the honours degree, not a student outcome. Cite it as QAA (2024), Anthropology Subject Benchmark Statement, para 2.18. Do not claim these bodies accredit the degree: the statement names them as professional organisations only. Set it beside 2.15 and 2.16 on partnership and careers."
  author-agent-dialogue: "Raise it when a programme team plans careers support or a student asks about the subject's professional bodies. With staff ask: 'Where in the course do students meet the RAI or BABAO and their networks?' With a student, point to the bodies as resources, not requirements."
- statement: qaa/anthropology-2024/3.1
  forPractitioner: { text: "Include practical, empirical data collection suited to the department's focus; graduates should know the range of methods and be able to choose suitable ones for a given research context, without being expert in all.", rewrite: light, force: should, status: drafted }
  forBeneficiary: { text: "You will not need to master every method, but you should know the range of methods available and be able to choose the right ones for different kinds of research.", rewrite: full, force: should, status: drafted }
  author-agent-written: "Treat this as an expectation (should) on what honours graduates know of methods at FHEQ Level 6, set in a description of practical content. Cite it as QAA (2024), Anthropology Subject Benchmark Statement, para 3.1. Do not claim it requires expertise in every method: the issuer rules that out. Set it beside qaa/anthropology-2024/ss.1.t, qaa/anthropology-2024/ss.11.t and qaa/fheq-2024/4.15.b2."
  author-agent-dialogue: "Raise it when a student worries about not mastering every method or a team plans methods teaching. Ask: 'For your research question, which methods could work, and why would you choose one over another?' Do not suggest that mastering all methods is expected."
- statement: qaa/anthropology-2024/3.2
  forPractitioner: { text: "Include the history of the discipline, both Social and Biological Anthropology, in every course: theoretical trends, fieldwork and practical techniques, past uses of data and the discipline's present engagement with social, economic and environmental questions.", rewrite: light, force: will, status: drafted }
  forBeneficiary: { text: "not-applicable: a statement of what the course includes; its outcomes for the student are knowledge and understanding items 2, 11 and 18", rewrite: full, force: will, status: drafted }
  author-agent-written: "Treat this as an expectation (will) on course content for every honours course in the subject, not a student outcome. Cite it as QAA (2024), Anthropology Subject Benchmark Statement, para 3.2. Do not claim it fixes how the history is taught or in which year. Set it beside the outcomes it supports: qaa/anthropology-2024/ku.2.t, ku.11.t and ku.18.t."
  author-agent-dialogue: "Raise it when a team maps where the discipline's history is taught. Ask staff: 'Where does the course cover the history of both Social and Biological Anthropology, and how the discipline is used now?' Do not present it to a student as a duty of theirs."
- statement: qaa/anthropology-2024/3.3
  forPractitioner: { text: "Teach how colonialism shaped the discipline and the lives it studied, and why and how decolonising work is done; students will be supported and trained to form positions of their own in these debates.", rewrite: light, force: will, status: drafted }
  forBeneficiary: { text: "You will learn how colonialism shaped the subject and the communities it studied and why and how people work to decolonise the discipline and universities, and you will be helped to find your own voice in these debates.", rewrite: full, force: will, status: drafted }
  author-agent-written: "Treat this as an expected outcome (will) on colonialism and decolonisation for honours students at FHEQ Level 6, set within a content paragraph. Cite it as QAA (2024), Anthropology Subject Benchmark Statement, para 3.3. Do not claim it prescribes a decolonised curriculum. Set it beside the EDI paragraphs 1.8 to 1.10, qaa/anthropology-2024/ku.4.t and qaa/fheq-2024/4.15.b7."
  author-agent-dialogue: "Raise it when a student asks about the discipline's colonial past or a team reviews its curriculum. Ask a student: 'What is your own view on how the discipline should deal with its colonial history?' Avoid giving a single correct answer: the aim is the student's own voice."
- statement: qaa/anthropology-2024/3.4
  forPractitioner: { text: "Pair methods teaching with explicit debate on ethical conduct and power imbalances; stress contested interpretation, respect and credit for communities as collaborators and their right to contest representation; and cover equitable sharing of data and outcomes, and open data, where ethical and practicable.", rewrite: light, force: should, status: drafted }
  forBeneficiary: { text: "not-applicable: a duty on teaching; the student meets its outcome in knowledge and understanding item 15 and subject-specific skills item 12", rewrite: full, force: should, status: drafted }
  author-agent-written: "Treat this as a provider expectation (should) on the content of ethics teaching in every honours course. Cite it as QAA (2024), Anthropology Subject Benchmark Statement, para 3.4. Do not claim it sets a research ethics procedure or a legal rule. Set it beside qaa/anthropology-2024/2.9, qaa/anthropology-2024/2.15, the outcomes qaa/anthropology-2024/ku.15.t and ss.12.t, and qaa/anthropology-2024/gs.7.e on data sharing."
  author-agent-dialogue: "Raise it when a programme team reviews ethics teaching or data-sharing practice. Ask: 'Where do students debate power and credit in their relations with communities?' Do not put it to a student as their duty; for students, use the related outcomes."
- statement: qaa/anthropology-2024/3.5
  forPractitioner: { text: "Make the relations between people and environments, other species included, a major focus, and encourage students to consider their economic, ecological, ideological and cultural aspects and what they mean for sustainability, conservation and climate.", rewrite: light, force: will, status: drafted }
  forBeneficiary: { text: "not-applicable: a statement of course focus; the student meets its outcomes in knowledge and understanding items 8 and 14", rewrite: full, force: will, status: drafted }
  author-agent-written: "Treat this as an expectation (will) on course focus for honours courses, carrying the sustainability theme outside its own section. Cite it as QAA (2024), Anthropology Subject Benchmark Statement, para 3.5. Do not claim it sets an ESD outcome by itself. Set it beside 1.14 and 1.15, qaa/anthropology-2024/ku.8.t and ku.14.t and the QAA and Advance HE ESD guidance (std:doc:qaa-advancehe-esd-2021-guidance)."
  author-agent-dialogue: "Raise it when a team maps sustainability across the course. Ask staff: 'Where do students consider how people and environments shape each other, and what that means for climate and conservation?' Do not present it to a student as a standard they must reach."
- statement: qaa/anthropology-2024/3.6
  forPractitioner: { text: "See that students become familiar with the range of theoretical approaches for interpreting data, through a dedicated theory module or built into problem-oriented teaching.", rewrite: light, force: should, status: drafted }
  forBeneficiary: { text: "not-applicable: a duty on the course; the student meets its outcomes in knowledge and understanding item 10 and subject-specific skills item 5", rewrite: full, force: should, status: drafted }
  author-agent-written: "Treat this as a provider expectation (should) on theory content for honours courses. Cite it as QAA (2024), Anthropology Subject Benchmark Statement, para 3.6. Do not claim it requires a standalone theory module. Set it beside qaa/anthropology-2024/ku.10.t and qaa/anthropology-2024/ss.5.t."
  author-agent-dialogue: "Raise it when a team decides where theory is taught. Ask: 'Where do students meet the range of theories, and do they use them on real problems?' Do not present it to a student as their duty."
- statement: qaa/anthropology-2024/3.9
  forPractitioner: { text: "Include developments in the discipline from beyond the global North, not only differences between UK, European and US traditions.", rewrite: light, force: should, status: drafted }
  forBeneficiary: { text: "not-applicable: a duty on curriculum design; the student meets it as content", rewrite: full, force: should, status: drafted }
  author-agent-written: "Treat this as a provider expectation (should) on the breadth of the curriculum. Cite it as QAA (2024), Anthropology Subject Benchmark Statement, para 3.9. Do not claim it names required authors or regions. Set it beside the EDI paragraphs 1.8 to 1.10 and qaa/anthropology-2024/3.3."
  author-agent-dialogue: "Raise it in a curriculum or reading-list review. Ask staff: 'Whose work from beyond the global North do students read, and where?' Do not put it to a student as their duty."
- statement: qaa/anthropology-2024/3.11
  forPractitioner: { text: "In a degree focused on Social Anthropology, cover the variety and social meaning of everyday practices and explore how social activities and institutions are enacted and understood locally across settings, using topics such as those listed in 3.11.", rewrite: light, force: should, status: drafted }
  forBeneficiary: { text: "not-applicable: a statement of course content; the student meets its outcomes in knowledge and understanding items 11 to 14", rewrite: full, force: should, status: drafted }
  author-agent-written: "Treat this as an expectation (will, then should) on the content of degrees mainly in Social Anthropology. Cite it as QAA (2024), Anthropology Subject Benchmark Statement, para 3.11; its listed topics are examples, not requirements. Do not apply it to Biological Anthropology degrees, which have 3.10. Set it beside qaa/anthropology-2024/ku.11.t to ku.14.t and 3.12."
  author-agent-dialogue: "Raise it when a Social Anthropology team checks content coverage. Ask: 'Which everyday practices, in which settings, do students study?' Do not present the topic list as compulsory."
- statement: qaa/anthropology-2024/3.17
  forPractitioner: { text: "Make placements and practical research projects available, abroad too where appropriate and possible, so students engage with the disciplinary community and with local communities.", rewrite: light, force: should, status: drafted }
  forBeneficiary: { text: "not-applicable: a duty on the course to facilitate; the student chooses whether to take it up", rewrite: full, force: should, status: drafted }
  author-agent-written: "Treat this as a provider expectation (should) on placement and project opportunities. Cite it as QAA (2024), Anthropology Subject Benchmark Statement, para 3.17. Do not claim placements are compulsory. Set it beside 2.17 on fieldwork placements, qaa/anthropology-2024/3.20 and the enterprise theme in 1.16."
  author-agent-dialogue: "Raise it when a team reviews placements or a student asks about opportunities beyond class. With staff ask: 'What placements and practical projects can students reach, and who misses out?' With a student, describe the chances on offer rather than a duty."
- statement: qaa/anthropology-2024/3.20
  forPractitioner: { text: "Enable a range of self-directed study, including virtual learning environments, problem-based and group learning, e-learning and distance learning, and where appropriate volunteering, placements, workplace and exchange opportunities.", rewrite: light, force: should, status: drafted }
  forBeneficiary: { text: "not-applicable: a duty on the course to enable; the student meets its outcome in generic skills item 2", rewrite: full, force: should, status: drafted }
  author-agent-written: "Treat this as a provider expectation (should) on learning opportunities. Cite it as QAA (2024), Anthropology Subject Benchmark Statement, para 3.20. Do not claim it requires distance learning or exchanges. Set it beside qaa/anthropology-2024/gs.2.t and qaa/fheq-2024/4.15.b5 on managing one's own learning."
  author-agent-dialogue: "Raise it when a team plans independent study. Ask: 'Which self-directed activities do students have, and how do they lead to independent learning?' Do not present it to a student as a duty."
- statement: qaa/anthropology-2024/3.21
  forPractitioner: { text: "Set a clear assessment and feedback strategy for the programme, and for every assignment define its aims, requirements and generic and specific criteria and share them with students ahead of time.", rewrite: light, force: will, status: drafted }
  forBeneficiary: { text: "not-applicable: a duty on the programme; the student benefits from clear criteria", rewrite: full, force: will, status: drafted }
  author-agent-written: "Treat this as an expectation (will) on each programme's assessment and feedback. Cite it as QAA (2024), Anthropology Subject Benchmark Statement, para 3.21. Do not claim it sets the form of criteria or a date for publishing them. Set it beside 3.22 on formative assessment, qaa/anthropology-2024/3.23 and Annex D (qaa/fheq-2024/annex-d) for classification."
  author-agent-dialogue: "Raise it in assessment review or when a student cannot find an assignment's criteria. With staff ask: 'Are the aims, requirements and criteria for every assignment available before students start?' With a student, help them find and read the criteria, not the policy."
- statement: qaa/anthropology-2024/3.23
  forPractitioner: { text: "Design the combination of assessment methods so it does not systematically disadvantage any group of students, and consider adjustments for individuals while keeping outcomes fair and equitable across the cohort.", rewrite: light, force: should, status: drafted }
  forBeneficiary: { text: "not-applicable: a duty on assessment design; the student may ask about adjustments", rewrite: full, force: should, status: drafted }
  author-agent-written: "Treat this as a provider expectation (should) on assessment design, carrying equality and accessibility outside their theme sections. Cite it as QAA (2024), Anthropology Subject Benchmark Statement, para 3.23. Do not claim it sets a legal standard for adjustments. Set it beside qaa/anthropology-2024/1.11, 1.12 and 3.18."
  author-agent-dialogue: "Raise it when a team reviews its assessment mix for fairness. Ask: 'Which group of students might this combination of methods disadvantage, and what would change that?' With a student asking about adjustments, explain that they are considered and point to the support route."
- statement: qaa/anthropology-2024/3.24
  forPractitioner: { text: "Use a wide range of assessment styles suited to each programme's outcomes; where work is done in groups, make sure the marking scheme states clearly how credit is split among individuals.", rewrite: light, force: will, status: drafted }
  forBeneficiary: { text: "not-applicable: a duty on assessment design; the student meets its effect in clear marking", rewrite: full, force: will, status: drafted }
  author-agent-written: "Treat this as an expectation (will) on marking group work, set within a description of varied assessment. Cite it as QAA (2024), Anthropology Subject Benchmark Statement, para 3.24. Do not claim it rules out essays or exams: 3.29 keeps them. Set it beside qaa/anthropology-2024/3.21, 3.29 and qaa/anthropology-2024/gs.6.t on group work."
  author-agent-dialogue: "Raise it when a team designs group assessment or a student asks how group marks are shared. With staff ask: 'Does the marking scheme say exactly how credit is split?' Avoid implying that traditional exams are no longer used."
- statement: qaa/anthropology-2024/3.25
  forPractitioner: { text: "Across all assessment, emphasise reflective and critical analysis, the evaluation and appropriate use of different kinds of evidence and its application to real-world problems.", rewrite: light, force: will, status: drafted }
  forBeneficiary: { text: "not-applicable: a statement of what assessment emphasises; its outcomes for the student are subject-specific skills items 3 and 7 and generic skills item 5", rewrite: full, force: will, status: drafted }
  author-agent-written: "Treat this as an expectation (will) on what all assessment emphasises in honours courses. Cite it as QAA (2024), Anthropology Subject Benchmark Statement, para 3.25. Do not claim it names assessment types. Set it beside qaa/anthropology-2024/ss.3.t, ss.7.t and gs.5.t and Annex D's qaa/fheq-2024/annex-d/cognitive/r1/3rd."
  author-agent-dialogue: "Raise it when staff write assessment briefs or criteria. Ask: 'Does this task reward critical use of evidence and its application to a real problem?' Do not present it to a student as a duty."
- statement: qaa/anthropology-2024/3.26
  forPractitioner: { text: "Offer a dissertation or extended research project, usually in the final year, covering the research process from framing questions to communicating findings; encourage and support a practical field, laboratory or data-collection element where appropriate, while allowing projects built on secondary data.", rewrite: light, force: should, status: drafted }
  forBeneficiary: { text: "not-applicable: a duty on the course to encourage and support; the dissertation is described for most students, not required of all", rewrite: full, force: should, status: drafted }
  author-agent-written: "Treat this as a provider expectation (should) on supporting practical elements in the final project, with a description of the dissertation most students do. Cite it as QAA (2024), Anthropology Subject Benchmark Statement, para 3.26. Do not claim a dissertation is compulsory: the issuer says most students do one. Set it beside qaa/anthropology-2024/1.21, qaa/anthropology-2024/ss.1.t and ss.1.e and qaa/fheq-2024/4.15.b6."
  author-agent-dialogue: "Raise it when a student plans a dissertation or a team designs the final-year project. Ask a student: 'Could your project include data you collect yourself, in the field or lab, or will it build on existing data?' Do not tell a student a practical element is required."
- statement: qaa/anthropology-2024/4.2
  forPractitioner: { text: "Decide how achievement above threshold is evidenced and refer to Annex D of the qualifications frameworks, with its descriptions of first, upper second, lower second and third-class honours.", rewrite: light, force: should, status: drafted }
  forBeneficiary: { text: "not-applicable: a duty on the provider; the student meets it through classification", rewrite: full, force: should, status: drafted }
  author-agent-written: "Treat this as a provider expectation (should) to use Annex D when judging achievement above threshold in the honours degree at FHEQ Level 6. Cite it as QAA (2024), Anthropology Subject Benchmark Statement, para 4.2. Do not claim the statement sets its own classification bands. Set it beside qaa/fheq-2024/annex-d (the four honours classes) and the strong/excellent column, for example qaa/anthropology-2024/ku.1.e."
  author-agent-dialogue: "Raise it when a team aligns its marking with degree classes. Ask: 'How do your criteria for each class draw on Annex D?' Do not present it to a student as their duty."
- statement: qaa/anthropology-2024/4.7
  forPractitioner: { text: "At master's level, taught or research, students will need to manage a substantial research project on their own, think and analyse critically and solve problems independently.", rewrite: light, force: will, status: drafted }
  forBeneficiary: { text: "If you go on to master's study, taught or by research, you will need to run a substantial research project on your own, think and analyse critically and solve problems independently.", rewrite: full, force: will, status: drafted }
  author-agent-written: "Treat this as an expectation (will) for master's study in the subject at FHEQ Level 7 or FQHEIS Level 11; with 4.8 it is the only master's standard the statement sets. Cite it as QAA (2024), Anthropology Subject Benchmark Statement, para 4.7. Do not claim it applies to the honours degree. Set it beside qaa/anthropology-2024/4.8, the FHEQ master's descriptor qaa/fheq-2024/4.17.b1 to 4.17.b8.3 and spine:7."
  author-agent-dialogue: "Raise it when a student weighs postgraduate study or a master's team checks its aims. Ask: 'What would you need to manage a large research project on your own?' Do not use it to judge an undergraduate."
- statement: qaa/anthropology-2024/4.8
  forPractitioner: { text: "In master's courses, expect students to master the skills described in the strong/excellent column of section 4's tables.", rewrite: light, force: will, status: drafted }
  forBeneficiary: { text: "If you take a master's in the subject, you will be expected to have mastered the skills described for strong and excellent work at honours level.", rewrite: full, force: will, status: drafted }
  author-agent-written: "Treat this as an expectation (will) that turns the honours strong/excellent column into the master's standard at FHEQ Level 7 or FQHEIS Level 11. Cite it as QAA (2024), Anthropology Subject Benchmark Statement, para 4.8. Do not claim the strong/excellent column is the honours pass standard. Set it beside qaa/anthropology-2024/4.7, the strong/excellent records such as qaa/anthropology-2024/ku.1.e and the FHEQ master's descriptor qaa/fheq-2024/4.17.b1."
  author-agent-dialogue: "Raise it when a student moves from honours to master's study or a master's team sets its outcomes. Ask: 'Which strong/excellent skills do you already show, and which need work?' Avoid telling an undergraduate that this column is the minimum."
- statement: qaa/anthropology-2024/gs.1.e
  forPractitioner: { text: "Above threshold, and as the expectation for master's study (4.8), look for evidence that the student can communicate and present strongly, expressing their own ideas and other people's clearly, effectively and inventively, in varied media and for different audiences.", rewrite: light, force: describes, status: drafted }
  forBeneficiary: { text: "To reach strong or excellent work, you would go further and communicate and present strongly, expressing your own ideas and other people's clearly, effectively and inventively, in varied media and for different audiences.", rewrite: full, force: describes, status: drafted }
  author-agent-written: "Treat this as the strong or excellent form of item 1 on strong, inventive communication to varied audiences: a description of performance above the threshold for the honours degree at FHEQ Level 6, and what 4.8 expects of master's students at Level 7/11. Cite it as QAA (2024), Anthropology Subject Benchmark Statement, section 4, Generic skills table, Anthropology (general), item 1, strong/excellent column. Do not present it as the pass standard or as a requirement for the award. Set it beside the threshold form qaa/anthropology-2024/gs.1.t, Annex D's upper rows qaa/fheq-2024/annex-d/transferable/r1/2.1 and /1st and, for master's work, qaa/fheq-2024/4.17.b1."
  author-agent-dialogue: "Raise it when a student who has met the minimum on communication and presentation asks how to do better, or when staff plan stretch tasks or master's study. Present it as a step above the threshold, never as the minimum: in plain words to a student and as a design aim to staff. Ask: 'How would you present the same idea to a specialist panel and to a school class?' Avoid reading the issuer's wording aloud or implying that a student fails without it."
- statement: qaa/anthropology-2024/gs.1.t
  forPractitioner: { text: "Threshold: plan teaching and assessment so that every honours graduate shows they can communicate and present well, put across their own ideas, summarise other people's arguments and keep the two apart.", rewrite: light, force: threshold, status: drafted }
  forBeneficiary: { text: "By the end of your honours degree you will, as a minimum, be able to communicate and present well, put across your own ideas, summarise other people's arguments and keep the two apart.", rewrite: full, force: threshold, status: drafted }
  author-agent-written: "Treat this as a threshold standard: the least an honours graduate will have shown on communication and presentation, for any Anthropology honours degree, at FHEQ Level 6 (FQHEIS Level 10). Cite it as QAA (2024), Anthropology Subject Benchmark Statement, section 4, Generic skills table, Anthropology (general), item 1, threshold column. Do not call it a regulatory requirement, a full curriculum or a master's standard. Set it beside its strong/excellent form qaa/anthropology-2024/gs.1.e, the FHEQ honours descriptor qaa/fheq-2024/4.15.b8 and Annex D's third-class row qaa/fheq-2024/annex-d/transferable/r1/3rd (spine:6, strand:communication)."
  author-agent-dialogue: "Raise it when a student asks what they must at least be able to do on communication and presentation, or when a programme team checks a module against the threshold for any Anthropology honours degree. With a student, put it plainly in the second person; with staff, frame it as the minimum the course must evidence. Ask: 'In your last essay, where did your own view end and the authors' begin?' Do not read the table out at length or offer the strong/excellent column as the pass mark."
- statement: qaa/anthropology-2024/gs.2.e
  forPractitioner: { text: "Above threshold, and as the expectation for master's study (4.8), look for evidence that the student can think independently, analyse, criticise and synthesise, and use those skills to develop new approaches, critiques and hypotheses from independent study.", rewrite: light, force: describes, status: drafted }
  forBeneficiary: { text: "To reach strong or excellent work, you would go further and think independently, analyse, criticise and synthesise, and use those skills to develop new approaches, critiques and hypotheses from independent study.", rewrite: full, force: describes, status: drafted }
  author-agent-written: "Treat this as the strong or excellent form of item 2 on independent thought turned to new approaches: a description of performance above the threshold for the honours degree at FHEQ Level 6, and what 4.8 expects of master's students at Level 7/11. Cite it as QAA (2024), Anthropology Subject Benchmark Statement, section 4, Generic skills table, Anthropology (general), item 2, strong/excellent column. Do not present it as the pass standard or as a requirement for the award. Set it beside the threshold form qaa/anthropology-2024/gs.2.t, Annex D's upper rows qaa/fheq-2024/annex-d/transferable/r3/2.1 and /1st and, for master's work, qaa/fheq-2024/4.17.b1."
  author-agent-dialogue: "Raise it when a student who has met the minimum on independent thought and learning asks how to do better, or when staff plan stretch tasks or master's study. Present it as a step above the threshold, never as the minimum: in plain words to a student and as a design aim to staff. Ask: 'What new hypothesis or critique has your own reading led you to?' Avoid reading the issuer's wording aloud or implying that a student fails without it."
- statement: qaa/anthropology-2024/gs.2.t
  forPractitioner: { text: "Threshold: plan teaching and assessment so that every honours graduate shows they can think and learn independently and analyse, criticise and synthesise.", rewrite: light, force: threshold, status: drafted }
  forBeneficiary: { text: "By the end of your honours degree you will, as a minimum, be able to think and learn independently and analyse, criticise and synthesise.", rewrite: full, force: threshold, status: drafted }
  author-agent-written: "Treat this as a threshold standard: the least an honours graduate will have shown on independent thought and learning, for any Anthropology honours degree, at FHEQ Level 6 (FQHEIS Level 10). Cite it as QAA (2024), Anthropology Subject Benchmark Statement, section 4, Generic skills table, Anthropology (general), item 2, threshold column. Do not call it a regulatory requirement, a full curriculum or a master's standard. Set it beside its strong/excellent form qaa/anthropology-2024/gs.2.e, the FHEQ honours descriptor qaa/fheq-2024/4.15.b5 and Annex D's third-class row qaa/fheq-2024/annex-d/transferable/r3/3rd (spine:6, strand:autonomy)."
  author-agent-dialogue: "Raise it when a student asks what they must at least be able to do on independent thought and learning, or when a programme team checks a module against the threshold for any Anthropology honours degree. With a student, put it plainly in the second person; with staff, frame it as the minimum the course must evidence. Ask: 'What have you learned recently that no one set for you?' Do not read the table out at length or offer the strong/excellent column as the pass mark."
- statement: qaa/anthropology-2024/gs.3.e
  forPractitioner: { text: "Above threshold, and as the expectation for master's study (4.8), look for evidence that the student can command basic research skills thoroughly and use them inventively and flexibly to collate primary or secondary data.", rewrite: light, force: describes, status: drafted }
  forBeneficiary: { text: "To reach strong or excellent work, you would go further and command basic research skills thoroughly and use them inventively and flexibly to collate primary or secondary data.", rewrite: full, force: describes, status: drafted }
  author-agent-written: "Treat this as the strong or excellent form of item 3 on inventive use of research skills: a description of performance above the threshold for the honours degree at FHEQ Level 6, and what 4.8 expects of master's students at Level 7/11. Cite it as QAA (2024), Anthropology Subject Benchmark Statement, section 4, Generic skills table, Anthropology (general), item 3, strong/excellent column. Do not present it as the pass standard or as a requirement for the award. Set it beside the threshold form qaa/anthropology-2024/gs.3.t, Annex D's upper rows qaa/fheq-2024/annex-d/practical/r1/2.1 and /1st and, for master's work, qaa/fheq-2024/4.17.b1."
  author-agent-dialogue: "Raise it when a student who has met the minimum on basic research skills with data asks how to do better, or when staff plan stretch tasks or master's study. Present it as a step above the threshold, never as the minimum: in plain words to a student and as a design aim to staff. Ask: 'What would you do differently, and more inventively, if you collected those data again?' Avoid reading the issuer's wording aloud or implying that a student fails without it."
- statement: qaa/anthropology-2024/gs.3.t
  forPractitioner: { text: "Threshold: plan teaching and assessment so that every honours graduate shows they can use sound basic research skills to collect and collate primary or secondary data.", rewrite: light, force: threshold, status: drafted }
  forBeneficiary: { text: "By the end of your honours degree you will, as a minimum, be able to use sound basic research skills to collect and collate primary or secondary data.", rewrite: full, force: threshold, status: drafted }
  author-agent-written: "Treat this as a threshold standard: the least an honours graduate will have shown on basic research skills with data, for any Anthropology honours degree, at FHEQ Level 6 (FQHEIS Level 10). Cite it as QAA (2024), Anthropology Subject Benchmark Statement, section 4, Generic skills table, Anthropology (general), item 3, threshold column. Do not call it a regulatory requirement, a full curriculum or a master's standard. Set it beside its strong/excellent form qaa/anthropology-2024/gs.3.e, the FHEQ honours descriptor qaa/fheq-2024/4.15.b2 and Annex D's third-class row qaa/fheq-2024/annex-d/practical/r1/3rd (spine:6, strand:application)."
  author-agent-dialogue: "Raise it when a student asks what they must at least be able to do on basic research skills with data, or when a programme team checks a module against the threshold for any Anthropology honours degree. With a student, put it plainly in the second person; with staff, frame it as the minimum the course must evidence. Ask: 'How did you collect and organise the data in your last project?' Do not read the table out at length or offer the strong/excellent column as the pass mark."
- statement: qaa/anthropology-2024/gs.4.e
  forPractitioner: { text: "Above threshold, and as the expectation for master's study (4.8), look for evidence that the student can weigh up and analyse what research and its design mean ethically, and carry out research to a rigorous ethical standard.", rewrite: light, force: describes, status: drafted }
  forBeneficiary: { text: "To reach strong or excellent work, you would go further and weigh up and analyse what research and its design mean ethically, and carry out research to a rigorous ethical standard.", rewrite: full, force: describes, status: drafted }
  author-agent-written: "Treat this as the strong or excellent form of item 4 on assessing ethics and conducting rigorous ethical research: a description of performance above the threshold for the honours degree at FHEQ Level 6, and what 4.8 expects of master's students at Level 7/11. Cite it as QAA (2024), Anthropology Subject Benchmark Statement, section 4, Generic skills table, Anthropology (general), item 4, strong/excellent column. Do not present it as the pass standard or as a requirement for the award. Set it beside the threshold form qaa/anthropology-2024/gs.4.t, Annex D's upper rows qaa/fheq-2024/annex-d/summary/r2/2.1 and /1st and, for master's work, qaa/fheq-2024/4.17.b1."
  author-agent-dialogue: "Raise it when a student who has met the minimum on ethics in conducting research asks how to do better, or when staff plan stretch tasks or master's study. Present it as a step above the threshold, never as the minimum: in plain words to a student and as a design aim to staff. Ask: 'How would you test the ethics of a research design before it starts?' Avoid reading the issuer's wording aloud or implying that a student fails without it."
- statement: qaa/anthropology-2024/gs.4.t
  forPractitioner: { text: "Threshold: plan teaching and assessment so that every honours graduate shows they can recognise what research means ethically and behave ethically when doing it.", rewrite: light, force: threshold, status: drafted }
  forBeneficiary: { text: "By the end of your honours degree you will, as a minimum, be able to recognise what research means ethically and behave ethically when doing it.", rewrite: full, force: threshold, status: drafted }
  author-agent-written: "Treat this as a threshold standard: the least an honours graduate will have shown on ethics in conducting research, for any Anthropology honours degree, at FHEQ Level 6 (FQHEIS Level 10). Cite it as QAA (2024), Anthropology Subject Benchmark Statement, section 4, Generic skills table, Anthropology (general), item 4, threshold column. Do not call it a regulatory requirement, a full curriculum or a master's standard. Set it beside its strong/excellent form qaa/anthropology-2024/gs.4.e, the FHEQ honours descriptor qaa/fheq-2024/4.15.b9.2 and Annex D's third-class row qaa/fheq-2024/annex-d/summary/r2/3rd (spine:6, strand:autonomy)."
  author-agent-dialogue: "Raise it when a student asks what they must at least be able to do on ethics in conducting research, or when a programme team checks a module against the threshold for any Anthropology honours degree. With a student, put it plainly in the second person; with staff, frame it as the minimum the course must evidence. Ask: 'What ethical choice did you have to make in your research, and how did you handle it?' Do not read the table out at length or offer the strong/excellent column as the pass mark."
- statement: qaa/anthropology-2024/gs.5.e
  forPractitioner: { text: "Above threshold, and as the expectation for master's study (4.8), look for evidence that the student can build a rigorous, persuasive structured argument, evaluate and combine several lines of evidence critically, and cite other people's work properly and ethically.", rewrite: light, force: describes, status: drafted }
  forBeneficiary: { text: "To reach strong or excellent work, you would go further and build a rigorous, persuasive structured argument, evaluate and combine several lines of evidence critically, and cite other people's work properly and ethically.", rewrite: full, force: describes, status: drafted }
  author-agent-written: "Treat this as the strong or excellent form of item 5 on rigorous, persuasive argument with combined evidence: a description of performance above the threshold for the honours degree at FHEQ Level 6, and what 4.8 expects of master's students at Level 7/11. Cite it as QAA (2024), Anthropology Subject Benchmark Statement, section 4, Generic skills table, Anthropology (general), item 5, strong/excellent column. Do not present it as the pass standard or as a requirement for the award. Set it beside the threshold form qaa/anthropology-2024/gs.5.t, Annex D's upper rows qaa/fheq-2024/annex-d/cognitive/r2/2.1 and /1st and, for master's work, qaa/fheq-2024/4.17.b1."
  author-agent-dialogue: "Raise it when a student who has met the minimum on structured argument and referencing asks how to do better, or when staff plan stretch tasks or master's study. Present it as a step above the threshold, never as the minimum: in plain words to a student and as a design aim to staff. Ask: 'Where does your strongest argument rely on combining evidence, and how did you check it?' Avoid reading the issuer's wording aloud or implying that a student fails without it."
- statement: qaa/anthropology-2024/gs.5.t
  forPractitioner: { text: "Threshold: plan teaching and assessment so that every honours graduate shows they can build a structured argument, cite other people's work and weigh several lines of evidence.", rewrite: light, force: threshold, status: drafted }
  forBeneficiary: { text: "By the end of your honours degree you will, as a minimum, be able to build a structured argument, cite other people's work and weigh several lines of evidence.", rewrite: full, force: threshold, status: drafted }
  author-agent-written: "Treat this as a threshold standard: the least an honours graduate will have shown on structured argument and referencing, for any Anthropology honours degree, at FHEQ Level 6 (FQHEIS Level 10). Cite it as QAA (2024), Anthropology Subject Benchmark Statement, section 4, Generic skills table, Anthropology (general), item 5, threshold column. Do not call it a regulatory requirement, a full curriculum or a master's standard. Set it beside its strong/excellent form qaa/anthropology-2024/gs.5.e, the FHEQ honours descriptor qaa/fheq-2024/4.15.b3.1 and Annex D's third-class row qaa/fheq-2024/annex-d/cognitive/r2/3rd (spine:6, strand:thinking)."
  author-agent-dialogue: "Raise it when a student asks what they must at least be able to do on structured argument and referencing, or when a programme team checks a module against the threshold for any Anthropology honours degree. With a student, put it plainly in the second person; with staff, frame it as the minimum the course must evidence. Ask: 'How is your argument structured, and which evidence carries the most weight?' Do not read the table out at length or offer the strong/excellent column as the pass mark."
- statement: qaa/anthropology-2024/gs.6.e
  forPractitioner: { text: "Above threshold, and as the expectation for master's study (4.8), look for evidence that the student can take part in and lead constructive group discussion and work well in groups.", rewrite: light, force: describes, status: drafted }
  forBeneficiary: { text: "To reach strong or excellent work, you would go further and take part in and lead constructive group discussion and work well in groups.", rewrite: full, force: describes, status: drafted }
  author-agent-written: "Treat this as the strong or excellent form of item 6 on leading group discussion: a description of performance above the threshold for the honours degree at FHEQ Level 6, and what 4.8 expects of master's students at Level 7/11. Cite it as QAA (2024), Anthropology Subject Benchmark Statement, section 4, Generic skills table, Anthropology (general), item 6, strong/excellent column. Do not present it as the pass standard or as a requirement for the award. Set it beside the threshold form qaa/anthropology-2024/gs.6.t, Annex D's upper rows qaa/fheq-2024/annex-d/transferable/r2/2.1 and /1st and, for master's work, qaa/fheq-2024/4.17.b1."
  author-agent-dialogue: "Raise it when a student who has met the minimum on group discussion and group work asks how to do better, or when staff plan stretch tasks or master's study. Present it as a step above the threshold, never as the minimum: in plain words to a student and as a design aim to staff. Ask: 'When have you led a group discussion, and what made it work?' Avoid reading the issuer's wording aloud or implying that a student fails without it."
- statement: qaa/anthropology-2024/gs.6.t
  forPractitioner: { text: "Threshold: plan teaching and assessment so that every honours graduate shows they can take part constructively, where it fits, in group discussion and group work.", rewrite: light, force: threshold, status: drafted }
  forBeneficiary: { text: "By the end of your honours degree you will, as a minimum, be able to take part constructively, where it fits, in group discussion and group work.", rewrite: full, force: threshold, status: drafted }
  author-agent-written: "Treat this as a threshold standard: the least an honours graduate will have shown on group discussion and group work, for any Anthropology honours degree, at FHEQ Level 6 (FQHEIS Level 10). Cite it as QAA (2024), Anthropology Subject Benchmark Statement, section 4, Generic skills table, Anthropology (general), item 6, threshold column. Do not call it a regulatory requirement, a full curriculum or a master's standard. Set it beside its strong/excellent form qaa/anthropology-2024/gs.6.e, the FHEQ honours descriptor qaa/fheq-2024/4.15.b9.1 and Annex D's third-class row qaa/fheq-2024/annex-d/transferable/r2/3rd (spine:6, strand:communication)."
  author-agent-dialogue: "Raise it when a student asks what they must at least be able to do on group discussion and group work, or when a programme team checks a module against the threshold for any Anthropology honours degree. With a student, put it plainly in the second person; with staff, frame it as the minimum the course must evidence. Ask: 'What did you contribute to your last group task?' Do not read the table out at length or offer the strong/excellent column as the pass mark."
- statement: qaa/anthropology-2024/gs.7.e
  forPractitioner: { text: "Above threshold, and as the expectation for master's study (4.8), look for evidence that the student can know and use a range of analytical and computing techniques properly, design and run independent analyses robustly and transparently, and value sharing data with collaborators and stakeholders and opening it to all where that is ethical and practical.", rewrite: light, force: describes, status: drafted }
  forBeneficiary: { text: "To reach strong or excellent work, you would go further and know and use a range of analytical and computing techniques properly, design and run independent analyses robustly and transparently, and value sharing data with collaborators and stakeholders and opening it to all where that is ethical and practical.", rewrite: full, force: describes, status: drafted }
  author-agent-written: "Treat this as the strong or excellent form of item 7 on robust, transparent analysis and data sharing: a description of performance above the threshold for the honours degree at FHEQ Level 6, and what 4.8 expects of master's students at Level 7/11. Cite it as QAA (2024), Anthropology Subject Benchmark Statement, section 4, Generic skills table, Anthropology (general), item 7, strong/excellent column. Do not present it as the pass standard or as a requirement for the award. Set it beside the threshold form qaa/anthropology-2024/gs.7.t, Annex D's upper rows qaa/fheq-2024/annex-d/transferable/r1/2.1 and /1st and, for master's work, qaa/fheq-2024/4.17.b1."
  author-agent-dialogue: "Raise it when a student who has met the minimum on analytical and computing techniques; data ethics asks how to do better, or when staff plan stretch tasks or master's study. Present it as a step above the threshold, never as the minimum: in plain words to a student and as a design aim to staff. Ask: 'How would you make your analysis transparent enough for someone else to repeat?' Avoid reading the issuer's wording aloud or implying that a student fails without it."
- statement: qaa/anthropology-2024/gs.7.t
  forPractitioner: { text: "Threshold: plan teaching and assessment so that every honours graduate shows they can know and use a range of analytical and computing techniques properly, and know the arguments about the ethics of access to data and of sharing it.", rewrite: light, force: threshold, status: drafted }
  forBeneficiary: { text: "By the end of your honours degree you will, as a minimum, be able to know and use a range of analytical and computing techniques properly, and know the arguments about the ethics of access to data and of sharing it.", rewrite: full, force: threshold, status: drafted }
  author-agent-written: "Treat this as a threshold standard: the least an honours graduate will have shown on analytical and computing techniques; data ethics, for any Anthropology honours degree, at FHEQ Level 6 (FQHEIS Level 10). Cite it as QAA (2024), Anthropology Subject Benchmark Statement, section 4, Generic skills table, Anthropology (general), item 7, threshold column. Do not call it a regulatory requirement, a full curriculum or a master's standard. Set it beside its strong/excellent form qaa/anthropology-2024/gs.7.e, the FHEQ honours descriptor qaa/fheq-2024/4.15.b2 and Annex D's third-class row qaa/fheq-2024/annex-d/transferable/r1/3rd (spine:6, strand:application)."
  author-agent-dialogue: "Raise it when a student asks what they must at least be able to do on analytical and computing techniques; data ethics, or when a programme team checks a module against the threshold for any Anthropology honours degree. With a student, put it plainly in the second person; with staff, frame it as the minimum the course must evidence. Ask: 'Which analytical or computing tools can you use, and what are the ethics of sharing your data?' Do not read the table out at length or offer the strong/excellent column as the pass mark."
- statement: qaa/anthropology-2024/gs.8.e
  forPractitioner: { text: "Above threshold, and as the expectation for master's study (4.8), look for evidence that the student can judge critically and understand their own strengths and weaknesses and those of collaborators, and plan well how to improve their own abilities.", rewrite: light, force: describes, status: drafted }
  forBeneficiary: { text: "To reach strong or excellent work, you would go further and judge critically and understand your own strengths and weaknesses and those of collaborators, and plan well how to improve your own abilities.", rewrite: full, force: describes, status: drafted }
  author-agent-written: "Treat this as the strong or excellent form of item 8 on assessing self and collaborators and planning improvement: a description of performance above the threshold for the honours degree at FHEQ Level 6, and what 4.8 expects of master's students at Level 7/11. Cite it as QAA (2024), Anthropology Subject Benchmark Statement, section 4, Generic skills table, Anthropology (general), item 8, strong/excellent column. Do not present it as the pass standard or as a requirement for the award. Set it beside the threshold form qaa/anthropology-2024/gs.8.t, Annex D's upper rows qaa/fheq-2024/annex-d/transferable/r5/2.1 and /1st and, for master's work, qaa/fheq-2024/4.17.b1."
  author-agent-dialogue: "Raise it when a student who has met the minimum on self-assessment and improvement asks how to do better, or when staff plan stretch tasks or master's study. Present it as a step above the threshold, never as the minimum: in plain words to a student and as a design aim to staff. Ask: 'How do you judge the strengths of the people you work with, and plan your own development around them?' Avoid reading the issuer's wording aloud or implying that a student fails without it."
- statement: qaa/anthropology-2024/gs.8.t
  forPractitioner: { text: "Threshold: plan teaching and assessment so that every honours graduate shows they can judge and understand their own strengths and weaknesses and act to build on their own abilities.", rewrite: light, force: threshold, status: drafted }
  forBeneficiary: { text: "By the end of your honours degree you will, as a minimum, be able to judge and understand your own strengths and weaknesses and act to build on your own abilities.", rewrite: full, force: threshold, status: drafted }
  author-agent-written: "Treat this as a threshold standard: the least an honours graduate will have shown on self-assessment and improvement, for any Anthropology honours degree, at FHEQ Level 6 (FQHEIS Level 10). Cite it as QAA (2024), Anthropology Subject Benchmark Statement, section 4, Generic skills table, Anthropology (general), item 8, threshold column. Do not call it a regulatory requirement, a full curriculum or a master's standard. Set it beside its strong/excellent form qaa/anthropology-2024/gs.8.e, the FHEQ honours descriptor qaa/fheq-2024/4.15.b9.3 and Annex D's third-class row qaa/fheq-2024/annex-d/transferable/r5/3rd (spine:6, strand:autonomy)."
  author-agent-dialogue: "Raise it when a student asks what they must at least be able to do on self-assessment and improvement, or when a programme team checks a module against the threshold for any Anthropology honours degree. With a student, put it plainly in the second person; with staff, frame it as the minimum the course must evidence. Ask: 'What is one weakness you have noticed in your work, and what are you doing about it?' Do not read the table out at length or offer the strong/excellent column as the pass mark."
- statement: qaa/anthropology-2024/gs.9.e
  forPractitioner: { text: "Above threshold, and as the expectation for master's study (4.8), look for evidence that the student can spot, query and push back against assumptions rooted in culture or ethnocentrism, grounded in a thorough, critical grasp of other ways of living in the world.", rewrite: light, force: describes, status: drafted }
  forBeneficiary: { text: "To reach strong or excellent work, you would go further and spot, query and push back against assumptions rooted in culture or ethnocentrism, grounded in a thorough, critical grasp of other ways of living in the world.", rewrite: full, force: describes, status: drafted }
  author-agent-written: "Treat this as the strong or excellent form of item 9 on challenging assumptions from deep understanding: a description of performance above the threshold for the honours degree at FHEQ Level 6, and what 4.8 expects of master's students at Level 7/11. Cite it as QAA (2024), Anthropology Subject Benchmark Statement, section 4, Generic skills table, Anthropology (general), item 9, strong/excellent column. Do not present it as the pass standard or as a requirement for the award. Set it beside the threshold form qaa/anthropology-2024/gs.9.t, Annex D's upper rows qaa/fheq-2024/annex-d/summary/r3/2.1 and /1st and, for master's work, qaa/fheq-2024/4.17.b1."
  author-agent-dialogue: "Raise it when a student who has met the minimum on challenging ethnocentric assumptions asks how to do better, or when staff plan stretch tasks or master's study. Present it as a step above the threshold, never as the minimum: in plain words to a student and as a design aim to staff. Ask: 'How does knowing another way of life well change the challenge you would make?' Avoid reading the issuer's wording aloud or implying that a student fails without it."
- statement: qaa/anthropology-2024/gs.9.t
  forPractitioner: { text: "Threshold: plan teaching and assessment so that every honours graduate shows they can spot, query and push back against assumptions rooted in culture or ethnocentrism, and value other ways of living in the world.", rewrite: light, force: threshold, status: drafted }
  forBeneficiary: { text: "By the end of your honours degree you will, as a minimum, be able to spot, query and push back against assumptions rooted in culture or ethnocentrism, and value other ways of living in the world.", rewrite: full, force: threshold, status: drafted }
  author-agent-written: "Treat this as a threshold standard: the least an honours graduate will have shown on challenging ethnocentric assumptions, for any Anthropology honours degree, at FHEQ Level 6 (FQHEIS Level 10). Cite it as QAA (2024), Anthropology Subject Benchmark Statement, section 4, Generic skills table, Anthropology (general), item 9, threshold column. Do not call it a regulatory requirement, a full curriculum or a master's standard. Set it beside its strong/excellent form qaa/anthropology-2024/gs.9.e, the FHEQ honours descriptor qaa/fheq-2024/4.15.b4 and Annex D's third-class row qaa/fheq-2024/annex-d/summary/r3/3rd (spine:6, strand:thinking)."
  author-agent-dialogue: "Raise it when a student asks what they must at least be able to do on challenging ethnocentric assumptions, or when a programme team checks a module against the threshold for any Anthropology honours degree. With a student, put it plainly in the second person; with staff, frame it as the minimum the course must evidence. Ask: 'What ethnocentric assumption have you caught in your own thinking?' Do not read the table out at length or offer the strong/excellent column as the pass mark."
- statement: qaa/anthropology-2024/ku.1.e
  forPractitioner: { text: "Above threshold, and as the expectation for master's study (4.8), look for evidence that the student can explain critically some of the forces that shape human variation and read how that variation is distributed across places and over time.", rewrite: light, force: describes, status: drafted }
  forBeneficiary: { text: "To reach strong or excellent work, you would go further and explain critically some of the forces that shape human variation and read how that variation is distributed across places and over time.", rewrite: full, force: describes, status: drafted }
  author-agent-written: "Treat this as the strong or excellent form of item 1 on the forces behind human diversity and its patterning: a description of performance above the threshold for the honours degree at FHEQ Level 6, and what 4.8 expects of master's students at Level 7/11. Cite it as QAA (2024), Anthropology Subject Benchmark Statement, section 4, Knowledge and understanding table, Anthropology (general), item 1, strong/excellent column. Do not present it as the pass standard or as a requirement for the award. Set it beside the threshold form qaa/anthropology-2024/ku.1.t, Annex D's upper rows qaa/fheq-2024/annex-d/knowledge/r1/2.1 and /1st and, for master's work, qaa/fheq-2024/4.17.b1."
  author-agent-dialogue: "Raise it when a student who has met the minimum on human diversity and its range asks how to do better, or when staff plan stretch tasks or master's study. Present it as a step above the threshold, never as the minimum: in plain words to a student and as a design aim to staff. Ask: 'Which forces behind human variation could you explain, and how does that variation change across regions or periods?' Avoid reading the issuer's wording aloud or implying that a student fails without it."
- statement: qaa/anthropology-2024/ku.1.t
  forPractitioner: { text: "Threshold: plan teaching and assessment so that every honours graduate shows they can recognise how socially, culturally and biologically varied human populations are, how far that variety reaches and what it offers to human life and experience.", rewrite: light, force: threshold, status: drafted }
  forBeneficiary: { text: "By the end of your honours degree you will, as a minimum, be able to recognise how socially, culturally and biologically varied human populations are, how far that variety reaches and what it offers to human life and experience.", rewrite: full, force: threshold, status: drafted }
  author-agent-written: "Treat this as a threshold standard: the least an honours graduate will have shown on human diversity and its range, for any Anthropology honours degree, at FHEQ Level 6 (FQHEIS Level 10). Cite it as QAA (2024), Anthropology Subject Benchmark Statement, section 4, Knowledge and understanding table, Anthropology (general), item 1, threshold column. Do not call it a regulatory requirement, a full curriculum or a master's standard. Set it beside its strong/excellent form qaa/anthropology-2024/ku.1.e, the FHEQ honours descriptor qaa/fheq-2024/4.15.b1 and Annex D's third-class row qaa/fheq-2024/annex-d/knowledge/r1/3rd (spine:6, strand:knowledge)."
  author-agent-dialogue: "Raise it when a student asks what they must at least be able to do on human diversity and its range, or when a programme team checks a module against the threshold for any Anthropology honours degree. With a student, put it plainly in the second person; with staff, frame it as the minimum the course must evidence. Ask: 'Can you give an example of human variation that is social, one that is cultural and one that is biological?' Do not read the table out at length or offer the strong/excellent column as the pass mark."
- statement: qaa/anthropology-2024/ku.2.e
  forPractitioner: { text: "Above threshold, and as the expectation for master's study (4.8), look for evidence that the student can look critically at how the discipline has grown and judge what its past means for present thinking and practice.", rewrite: light, force: describes, status: drafted }
  forBeneficiary: { text: "To reach strong or excellent work, you would go further and look critically at how the discipline has grown and judge what its past means for present thinking and practice.", rewrite: full, force: describes, status: drafted }
  author-agent-written: "Treat this as the strong or excellent form of item 2 on the discipline's history and its bearing now: a description of performance above the threshold for the honours degree at FHEQ Level 6, and what 4.8 expects of master's students at Level 7/11. Cite it as QAA (2024), Anthropology Subject Benchmark Statement, section 4, Knowledge and understanding table, Anthropology (general), item 2, strong/excellent column. Do not present it as the pass standard or as a requirement for the award. Set it beside the threshold form qaa/anthropology-2024/ku.2.t, Annex D's upper rows qaa/fheq-2024/annex-d/knowledge/r2/2.1 and /1st and, for master's work, qaa/fheq-2024/4.17.b1."
  author-agent-dialogue: "Raise it when a student who has met the minimum on the history of the discipline asks how to do better, or when staff plan stretch tasks or master's study. Present it as a step above the threshold, never as the minimum: in plain words to a student and as a design aim to staff. Ask: 'Where does the discipline's past still shape its theory or practice, and what is your view of that influence?' Avoid reading the issuer's wording aloud or implying that a student fails without it."
- statement: qaa/anthropology-2024/ku.2.t
  forPractitioner: { text: "Threshold: plan teaching and assessment so that every honours graduate shows they can give an account of how the discipline arose and changed over time, and of what that past means for how it is thought about and practised now.", rewrite: light, force: threshold, status: drafted }
  forBeneficiary: { text: "By the end of your honours degree you will, as a minimum, be able to give an account of how the discipline arose and changed over time, and of what that past means for how it is thought about and practised now.", rewrite: full, force: threshold, status: drafted }
  author-agent-written: "Treat this as a threshold standard: the least an honours graduate will have shown on the history of the discipline, for any Anthropology honours degree, at FHEQ Level 6 (FQHEIS Level 10). Cite it as QAA (2024), Anthropology Subject Benchmark Statement, section 4, Knowledge and understanding table, Anthropology (general), item 2, threshold column. Do not call it a regulatory requirement, a full curriculum or a master's standard. Set it beside its strong/excellent form qaa/anthropology-2024/ku.2.e, the FHEQ honours descriptor qaa/fheq-2024/4.15.b1 and Annex D's third-class row qaa/fheq-2024/annex-d/knowledge/r2/3rd (spine:6, strand:knowledge)."
  author-agent-dialogue: "Raise it when a student asks what they must at least be able to do on the history of the discipline, or when a programme team checks a module against the threshold for any Anthropology honours degree. With a student, put it plainly in the second person; with staff, frame it as the minimum the course must evidence. Ask: 'How would you outline where the discipline came from, and why does that history matter for how it works now?' Do not read the table out at length or offer the strong/excellent column as the pass mark."
- statement: qaa/anthropology-2024/ku.3.e
  forPractitioner: { text: "Above threshold, and as the expectation for master's study (4.8), look for evidence that the student can weigh up and criticise the arguments surrounding the subject's central themes.", rewrite: light, force: describes, status: drafted }
  forBeneficiary: { text: "To reach strong or excellent work, you would go further and weigh up and criticise the arguments surrounding the subject's central themes.", rewrite: full, force: describes, status: drafted }
  author-agent-written: "Treat this as the strong or excellent form of item 3 on evaluating debates on key themes: a description of performance above the threshold for the honours degree at FHEQ Level 6, and what 4.8 expects of master's students at Level 7/11. Cite it as QAA (2024), Anthropology Subject Benchmark Statement, section 4, Knowledge and understanding table, Anthropology (general), item 3, strong/excellent column. Do not present it as the pass standard or as a requirement for the award. Set it beside the threshold form qaa/anthropology-2024/ku.3.t, Annex D's upper rows qaa/fheq-2024/annex-d/knowledge/r2/2.1 and /1st and, for master's work, qaa/fheq-2024/4.17.b1."
  author-agent-dialogue: "Raise it when a student who has met the minimum on key themes and their debates asks how to do better, or when staff plan stretch tasks or master's study. Present it as a step above the threshold, never as the minimum: in plain words to a student and as a design aim to staff. Ask: 'Pick one central debate: whose argument do you find weakest, and why?' Avoid reading the issuer's wording aloud or implying that a student fails without it."
- statement: qaa/anthropology-2024/ku.3.t
  forPractitioner: { text: "Threshold: plan teaching and assessment so that every honours graduate shows they can show knowledge of particular themes in the subject, such as kinship, gender, religion, exchange, evolution or primate behaviour, and of the main arguments about them.", rewrite: light, force: threshold, status: drafted }
  forBeneficiary: { text: "By the end of your honours degree you will, as a minimum, be able to show knowledge of particular themes in the subject, such as kinship, gender, religion, exchange, evolution or primate behaviour, and of the main arguments about them.", rewrite: full, force: threshold, status: drafted }
  author-agent-written: "Treat this as a threshold standard: the least an honours graduate will have shown on key themes and their debates, for any Anthropology honours degree, at FHEQ Level 6 (FQHEIS Level 10). Cite it as QAA (2024), Anthropology Subject Benchmark Statement, section 4, Knowledge and understanding table, Anthropology (general), item 3, threshold column. Do not call it a regulatory requirement, a full curriculum or a master's standard. Set it beside its strong/excellent form qaa/anthropology-2024/ku.3.e, the FHEQ honours descriptor qaa/fheq-2024/4.15.b3.1 and Annex D's third-class row qaa/fheq-2024/annex-d/knowledge/r2/3rd (spine:6, strand:knowledge)."
  author-agent-dialogue: "Raise it when a student asks what they must at least be able to do on key themes and their debates, or when a programme team checks a module against the threshold for any Anthropology honours degree. With a student, put it plainly in the second person; with staff, frame it as the minimum the course must evidence. Ask: 'Which two themes in the subject do you know best, and what are people arguing about in each?' Do not read the table out at length or offer the strong/excellent column as the pass mark."
- statement: qaa/anthropology-2024/ku.4.e
  forPractitioner: { text: "Above threshold, and as the expectation for master's study (4.8), look for evidence that the student can reflect critically on cultural assumptions, their own and other people's, and on what they mean for current theory and practice; weigh both the value and the limits of cultural relativism; and handle points of disagreement with people from many cultures and backgrounds with insight and with care for how those debates affect lives today.", rewrite: light, force: describes, status: drafted }
  forBeneficiary: { text: "To reach strong or excellent work, you would go further and reflect critically on cultural assumptions, your own and other people's, and on what they mean for current theory and practice; weigh both the value and the limits of cultural relativism; and handle points of disagreement with people from many cultures and backgrounds with insight and with care for how those debates affect lives today.", rewrite: full, force: describes, status: drafted }
  author-agent-written: "Treat this as the strong or excellent form of item 4 on assumptions and the limits of relativism: a description of performance above the threshold for the honours degree at FHEQ Level 6, and what 4.8 expects of master's students at Level 7/11. Cite it as QAA (2024), Anthropology Subject Benchmark Statement, section 4, Knowledge and understanding table, Anthropology (general), item 4, strong/excellent column. Do not present it as the pass standard or as a requirement for the award. Set it beside the threshold form qaa/anthropology-2024/ku.4.t, Annex D's upper rows qaa/fheq-2024/annex-d/cognitive/r1/2.1 and /1st and, for master's work, qaa/fheq-2024/4.17.b1."
  author-agent-dialogue: "Raise it when a student who has met the minimum on cultural assumptions and situated knowledge asks how to do better, or when staff plan stretch tasks or master's study. Present it as a step above the threshold, never as the minimum: in plain words to a student and as a design aim to staff. Ask: 'Where would you say cultural relativism stops being helpful, and how would you handle that disagreement with someone?' Avoid reading the issuer's wording aloud or implying that a student fails without it."
- statement: qaa/anthropology-2024/ku.4.t
  forPractitioner: { text: "Threshold: plan teaching and assessment so that every honours graduate shows they can spot and question cultural assumptions, accept that knowledge depends on where it comes from and is open to dispute, and see why cultural relativism and attention to other viewpoints matter.", rewrite: light, force: threshold, status: drafted }
  forBeneficiary: { text: "By the end of your honours degree you will, as a minimum, be able to spot and question cultural assumptions, accept that knowledge depends on where it comes from and is open to dispute, and see why cultural relativism and attention to other viewpoints matter.", rewrite: full, force: threshold, status: drafted }
  author-agent-written: "Treat this as a threshold standard: the least an honours graduate will have shown on cultural assumptions and situated knowledge, for any Anthropology honours degree, at FHEQ Level 6 (FQHEIS Level 10). Cite it as QAA (2024), Anthropology Subject Benchmark Statement, section 4, Knowledge and understanding table, Anthropology (general), item 4, threshold column. Do not call it a regulatory requirement, a full curriculum or a master's standard. Set it beside its strong/excellent form qaa/anthropology-2024/ku.4.e, the FHEQ honours descriptor qaa/fheq-2024/4.15.b4 and Annex D's third-class row qaa/fheq-2024/annex-d/cognitive/r1/3rd (spine:6, strand:thinking)."
  author-agent-dialogue: "Raise it when a student asks what they must at least be able to do on cultural assumptions and situated knowledge, or when a programme team checks a module against the threshold for any Anthropology honours degree. With a student, put it plainly in the second person; with staff, frame it as the minimum the course must evidence. Ask: 'Can you name an assumption from your own culture that shaped how you first read another way of life?' Do not read the table out at length or offer the strong/excellent column as the pass mark."
- statement: qaa/anthropology-2024/ku.5.e
  forPractitioner: { text: "Above threshold, and as the expectation for master's study (4.8), look for evidence that the student can judge critically, and invent, ways of putting anthropological knowledge to use in different settings.", rewrite: light, force: describes, status: drafted }
  forBeneficiary: { text: "To reach strong or excellent work, you would go further and judge critically, and invent, ways of putting anthropological knowledge to use in different settings.", rewrite: full, force: describes, status: drafted }
  author-agent-written: "Treat this as the strong or excellent form of item 5 on evaluating and devising applications: a description of performance above the threshold for the honours degree at FHEQ Level 6, and what 4.8 expects of master's students at Level 7/11. Cite it as QAA (2024), Anthropology Subject Benchmark Statement, section 4, Knowledge and understanding table, Anthropology (general), item 5, strong/excellent column. Do not present it as the pass standard or as a requirement for the award. Set it beside the threshold form qaa/anthropology-2024/ku.5.t, Annex D's upper rows qaa/fheq-2024/annex-d/cognitive/r3/2.1 and /1st and, for master's work, qaa/fheq-2024/4.17.b1."
  author-agent-dialogue: "Raise it when a student who has met the minimum on uses of anthropological knowledge asks how to do better, or when staff plan stretch tasks or master's study. Present it as a step above the threshold, never as the minimum: in plain words to a student and as a design aim to staff. Ask: 'Can you design a new use for something you have learned, and say what might go wrong with it?' Avoid reading the issuer's wording aloud or implying that a student fails without it."
- statement: qaa/anthropology-2024/ku.5.t
  forPractitioner: { text: "Threshold: plan teaching and assessment so that every honours graduate shows they can show an understanding of how anthropological knowledge might be put to use in different settings.", rewrite: light, force: threshold, status: drafted }
  forBeneficiary: { text: "By the end of your honours degree you will, as a minimum, be able to show an understanding of how anthropological knowledge might be put to use in different settings.", rewrite: full, force: threshold, status: drafted }
  author-agent-written: "Treat this as a threshold standard: the least an honours graduate will have shown on uses of anthropological knowledge, for any Anthropology honours degree, at FHEQ Level 6 (FQHEIS Level 10). Cite it as QAA (2024), Anthropology Subject Benchmark Statement, section 4, Knowledge and understanding table, Anthropology (general), item 5, threshold column. Do not call it a regulatory requirement, a full curriculum or a master's standard. Set it beside its strong/excellent form qaa/anthropology-2024/ku.5.e, the FHEQ honours descriptor qaa/fheq-2024/4.15.b6 and Annex D's third-class row qaa/fheq-2024/annex-d/cognitive/r3/3rd (spine:6, strand:application)."
  author-agent-dialogue: "Raise it when a student asks what they must at least be able to do on uses of anthropological knowledge, or when a programme team checks a module against the threshold for any Anthropology honours degree. With a student, put it plainly in the second person; with staff, frame it as the minimum the course must evidence. Ask: 'Where outside the university could anthropological knowledge make a difference, and how?' Do not read the table out at length or offer the strong/excellent column as the pass mark."
- statement: qaa/anthropology-2024/ku.6.e
  forPractitioner: { text: "Above threshold, and as the expectation for master's study (4.8), look for evidence that the student can understand critically what sets different kinds of data apart and how they can be combined to produce new forms in reply.", rewrite: light, force: describes, status: drafted }
  forBeneficiary: { text: "To reach strong or excellent work, you would go further and understand critically what sets different kinds of data apart and how they can be combined to produce new forms in reply.", rewrite: full, force: describes, status: drafted }
  author-agent-written: "Treat this as the strong or excellent form of item 6 on properties of data forms and combining them: a description of performance above the threshold for the honours degree at FHEQ Level 6, and what 4.8 expects of master's students at Level 7/11. Cite it as QAA (2024), Anthropology Subject Benchmark Statement, section 4, Knowledge and understanding table, Anthropology (general), item 6, strong/excellent column. Do not present it as the pass standard or as a requirement for the award. Set it beside the threshold form qaa/anthropology-2024/ku.6.t, Annex D's upper rows qaa/fheq-2024/annex-d/practical/r4/2.1 and /1st and, for master's work, qaa/fheq-2024/4.17.b1."
  author-agent-dialogue: "Raise it when a student who has met the minimum on interpreting oral, textual, visual and other forms asks how to do better, or when staff plan stretch tasks or master's study. Present it as a step above the threshold, never as the minimum: in plain words to a student and as a design aim to staff. Ask: 'How might you combine two kinds of data, say interviews and images, into something new?' Avoid reading the issuer's wording aloud or implying that a student fails without it."
- statement: qaa/anthropology-2024/ku.6.t
  forPractitioner: { text: "Threshold: plan teaching and assessment so that every honours graduate shows they can read and analyse many kinds of material, spoken, written, musical, visual and more, and know how each kind differs.", rewrite: light, force: threshold, status: drafted }
  forBeneficiary: { text: "By the end of your honours degree you will, as a minimum, be able to read and analyse many kinds of material, spoken, written, musical, visual and more, and know how each kind differs.", rewrite: full, force: threshold, status: drafted }
  author-agent-written: "Treat this as a threshold standard: the least an honours graduate will have shown on interpreting oral, textual, visual and other forms, for any Anthropology honours degree, at FHEQ Level 6 (FQHEIS Level 10). Cite it as QAA (2024), Anthropology Subject Benchmark Statement, section 4, Knowledge and understanding table, Anthropology (general), item 6, threshold column. Do not call it a regulatory requirement, a full curriculum or a master's standard. Set it beside its strong/excellent form qaa/anthropology-2024/ku.6.e, the FHEQ honours descriptor qaa/fheq-2024/4.15.b2 and Annex D's third-class row qaa/fheq-2024/annex-d/practical/r4/3rd (spine:6, strand:application)."
  author-agent-dialogue: "Raise it when a student asks what they must at least be able to do on interpreting oral, textual, visual and other forms, or when a programme team checks a module against the threshold for any Anthropology honours degree. With a student, put it plainly in the second person; with staff, frame it as the minimum the course must evidence. Ask: 'What different kinds of material have you analysed, and what did each let you see that the others did not?' Do not read the table out at length or offer the strong/excellent column as the pass mark."
- statement: qaa/anthropology-2024/ku.7.e
  forPractitioner: { text: "Above threshold, and as the expectation for master's study (4.8), look for evidence that the student can draw several disciplines together, and move past their limits, to understand human bodies and behaviour.", rewrite: light, force: describes, status: drafted }
  forBeneficiary: { text: "To reach strong or excellent work, you would go further and draw several disciplines together, and move past their limits, to understand human bodies and behaviour.", rewrite: full, force: describes, status: drafted }
  author-agent-written: "Treat this as the strong or excellent form of item 7 on integrating and going beyond disciplines: a description of performance above the threshold for the honours degree at FHEQ Level 6, and what 4.8 expects of master's students at Level 7/11. Cite it as QAA (2024), Anthropology Subject Benchmark Statement, section 4, Knowledge and understanding table, Anthropology (general), item 7, strong/excellent column. Do not present it as the pass standard or as a requirement for the award. Set it beside the threshold form qaa/anthropology-2024/ku.7.t, Annex D's upper rows qaa/fheq-2024/annex-d/knowledge/r3/2.1 and /1st and, for master's work, qaa/fheq-2024/4.17.b1."
  author-agent-dialogue: "Raise it when a student who has met the minimum on links with cognate subjects asks how to do better, or when staff plan stretch tasks or master's study. Present it as a step above the threshold, never as the minimum: in plain words to a student and as a design aim to staff. Ask: 'Can you show a case where combining two disciplines told you something neither could alone?' Avoid reading the issuer's wording aloud or implying that a student fails without it."
- statement: qaa/anthropology-2024/ku.7.t
  forPractitioner: { text: "Threshold: plan teaching and assessment so that every honours graduate shows they can show critical awareness of how the subject connects with neighbouring disciplines.", rewrite: light, force: threshold, status: drafted }
  forBeneficiary: { text: "By the end of your honours degree you will, as a minimum, be able to show critical awareness of how the subject connects with neighbouring disciplines.", rewrite: full, force: threshold, status: drafted }
  author-agent-written: "Treat this as a threshold standard: the least an honours graduate will have shown on links with cognate subjects, for any Anthropology honours degree, at FHEQ Level 6 (FQHEIS Level 10). Cite it as QAA (2024), Anthropology Subject Benchmark Statement, section 4, Knowledge and understanding table, Anthropology (general), item 7, threshold column. Do not call it a regulatory requirement, a full curriculum or a master's standard. Set it beside its strong/excellent form qaa/anthropology-2024/ku.7.e, the FHEQ honours descriptor qaa/fheq-2024/4.15.b1 and Annex D's third-class row qaa/fheq-2024/annex-d/knowledge/r3/3rd (spine:6, strand:knowledge)."
  author-agent-dialogue: "Raise it when a student asks what they must at least be able to do on links with cognate subjects, or when a programme team checks a module against the threshold for any Anthropology honours degree. With a student, put it plainly in the second person; with staff, frame it as the minimum the course must evidence. Ask: 'Which neighbouring subjects does your work borrow from, and where do they differ from Anthropology?' Do not read the table out at length or offer the strong/excellent column as the pass mark."
- statement: qaa/anthropology-2024/ku.8.e
  forPractitioner: { text: "Above threshold, and as the expectation for master's study (4.8), look for evidence that the student can appreciate critically, and analyse by several techniques, the complex ways in which social and cultural systems, human physical variation and ecosystems act on one another.", rewrite: light, force: describes, status: drafted }
  forBeneficiary: { text: "To reach strong or excellent work, you would go further and appreciate critically, and analyse by several techniques, the complex ways in which social and cultural systems, human physical variation and ecosystems act on one another.", rewrite: full, force: describes, status: drafted }
  author-agent-written: "Treat this as the strong or excellent form of item 8 on analysing how culture, biology and environment interact: a description of performance above the threshold for the honours degree at FHEQ Level 6, and what 4.8 expects of master's students at Level 7/11. Cite it as QAA (2024), Anthropology Subject Benchmark Statement, section 4, Knowledge and understanding table, Anthropology (general), item 8, strong/excellent column. Do not present it as the pass standard or as a requirement for the award. Set it beside the threshold form qaa/anthropology-2024/ku.8.t, Annex D's upper rows qaa/fheq-2024/annex-d/knowledge/r2/2.1 and /1st and, for master's work, qaa/fheq-2024/4.17.b1."
  author-agent-dialogue: "Raise it when a student who has met the minimum on links between human diversity and environments asks how to do better, or when staff plan stretch tasks or master's study. Present it as a step above the threshold, never as the minimum: in plain words to a student and as a design aim to staff. Ask: 'Which techniques would you use to analyse that interaction, and what would each miss?' Avoid reading the issuer's wording aloud or implying that a student fails without it."
- statement: qaa/anthropology-2024/ku.8.t
  forPractitioner: { text: "Threshold: plan teaching and assessment so that every honours graduate shows they can recognise how social and cultural variety, bodily variety and the physical world and its ecosystems shape one another over time.", rewrite: light, force: threshold, status: drafted }
  forBeneficiary: { text: "By the end of your honours degree you will, as a minimum, be able to recognise how social and cultural variety, bodily variety and the physical world and its ecosystems shape one another over time.", rewrite: full, force: threshold, status: drafted }
  author-agent-written: "Treat this as a threshold standard: the least an honours graduate will have shown on links between human diversity and environments, for any Anthropology honours degree, at FHEQ Level 6 (FQHEIS Level 10). Cite it as QAA (2024), Anthropology Subject Benchmark Statement, section 4, Knowledge and understanding table, Anthropology (general), item 8, threshold column. Do not call it a regulatory requirement, a full curriculum or a master's standard. Set it beside its strong/excellent form qaa/anthropology-2024/ku.8.e, the FHEQ honours descriptor qaa/fheq-2024/4.15.b1 and Annex D's third-class row qaa/fheq-2024/annex-d/knowledge/r2/3rd (spine:6, strand:knowledge)."
  author-agent-dialogue: "Raise it when a student asks what they must at least be able to do on links between human diversity and environments, or when a programme team checks a module against the threshold for any Anthropology honours degree. With a student, put it plainly in the second person; with staff, frame it as the minimum the course must evidence. Ask: 'Can you give an example where environment, biology and culture shaped each other?' Do not read the table out at length or offer the strong/excellent column as the pass mark."
- statement: qaa/anthropology-2024/ku.9.e
  forPractitioner: { text: "Above threshold, and as the expectation for master's study (4.8), look for evidence that the student can judge critically what the evidence on unequal experience, health and status among humans, hominins and primates implies; assess what it shows about social and cultural inequity; and consider how political and social processes play a part and might be eased in living populations.", rewrite: light, force: describes, status: drafted }
  forBeneficiary: { text: "To reach strong or excellent work, you would go further and judge critically what the evidence on unequal experience, health and status among humans, hominins and primates implies; assess what it shows about social and cultural inequity; and consider how political and social processes play a part and might be eased in living populations.", rewrite: full, force: describes, status: drafted }
  author-agent-written: "Treat this as the strong or excellent form of item 9 on evidence for disparities and how to ease them: a description of performance above the threshold for the honours degree at FHEQ Level 6, and what 4.8 expects of master's students at Level 7/11. Cite it as QAA (2024), Anthropology Subject Benchmark Statement, section 4, Knowledge and understanding table, Anthropology (general), item 9, strong/excellent column. Do not present it as the pass standard or as a requirement for the award. Set it beside the threshold form qaa/anthropology-2024/ku.9.t, Annex D's upper rows qaa/fheq-2024/annex-d/knowledge/r3/2.1 and /1st and, for master's work, qaa/fheq-2024/4.17.b1."
  author-agent-dialogue: "Raise it when a student who has met the minimum on the factors behind unequal experience asks how to do better, or when staff plan stretch tasks or master's study. Present it as a step above the threshold, never as the minimum: in plain words to a student and as a design aim to staff. Ask: 'What does the evidence on one inequality tell you, and what could reduce it today?' Avoid reading the issuer's wording aloud or implying that a student fails without it."
- statement: qaa/anthropology-2024/ku.9.t
  forPractitioner: { text: "Threshold: plan teaching and assessment so that every honours graduate shows they can show awareness of the social, cultural and biological factors behind differences in experience, such as health or status, within and across human, hominin or primate groups, past and present.", rewrite: light, force: threshold, status: drafted }
  forBeneficiary: { text: "By the end of your honours degree you will, as a minimum, be able to show awareness of the social, cultural and biological factors behind differences in experience, such as health or status, within and across human, hominin or primate groups, past and present.", rewrite: full, force: threshold, status: drafted }
  author-agent-written: "Treat this as a threshold standard: the least an honours graduate will have shown on the factors behind unequal experience, for any Anthropology honours degree, at FHEQ Level 6 (FQHEIS Level 10). Cite it as QAA (2024), Anthropology Subject Benchmark Statement, section 4, Knowledge and understanding table, Anthropology (general), item 9, threshold column. Do not call it a regulatory requirement, a full curriculum or a master's standard. Set it beside its strong/excellent form qaa/anthropology-2024/ku.9.e, the FHEQ honours descriptor qaa/fheq-2024/4.15.b4 and Annex D's third-class row qaa/fheq-2024/annex-d/knowledge/r3/3rd (spine:6, strand:knowledge)."
  author-agent-dialogue: "Raise it when a student asks what they must at least be able to do on the factors behind unequal experience, or when a programme team checks a module against the threshold for any Anthropology honours degree. With a student, put it plainly in the second person; with staff, frame it as the minimum the course must evidence. Ask: 'What factors would you look at to explain why health differs between two groups?' Do not read the table out at length or offer the strong/excellent column as the pass mark."
- statement: qaa/anthropology-2024/ku.10.e
  forPractitioner: { text: "Above threshold, and as the expectation for master's study (4.8), look for evidence that the student can assess critically the subject's key concepts, theories and methods, judge how they are used and apply some of them well.", rewrite: light, force: describes, status: drafted }
  forBeneficiary: { text: "To reach strong or excellent work, you would go further and assess critically the subject's key concepts, theories and methods, judge how they are used and apply some of them well.", rewrite: full, force: describes, status: drafted }
  author-agent-written: "Treat this as the strong or excellent form of item 10 on evaluating and applying concepts, theories and methods: a description of performance above the threshold for the honours degree at FHEQ Level 6, and what 4.8 expects of master's students at Level 7/11. Cite it as QAA (2024), Anthropology Subject Benchmark Statement, section 4, Knowledge and understanding table, Anthropology (general), item 10, strong/excellent column. Do not present it as the pass standard or as a requirement for the award. Set it beside the threshold form qaa/anthropology-2024/ku.10.t, Annex D's upper rows qaa/fheq-2024/annex-d/cognitive/r2/2.1 and /1st and, for master's work, qaa/fheq-2024/4.17.b1."
  author-agent-dialogue: "Raise it when a student who has met the minimum on strengths and weaknesses of concepts, theories and methods asks how to do better, or when staff plan stretch tasks or master's study. Present it as a step above the threshold, never as the minimum: in plain words to a student and as a design aim to staff. Ask: 'Which theory would you choose for your own project, and why over the alternatives?' Avoid reading the issuer's wording aloud or implying that a student fails without it."
- statement: qaa/anthropology-2024/ku.10.t
  forPractitioner: { text: "Threshold: plan teaching and assessment so that every honours graduate shows they can set out the main strengths and weaknesses of the subject's key concepts, theories and methods and judge how they are used.", rewrite: light, force: threshold, status: drafted }
  forBeneficiary: { text: "By the end of your honours degree you will, as a minimum, be able to set out the main strengths and weaknesses of the subject's key concepts, theories and methods and judge how they are used.", rewrite: full, force: threshold, status: drafted }
  author-agent-written: "Treat this as a threshold standard: the least an honours graduate will have shown on strengths and weaknesses of concepts, theories and methods, for any Anthropology honours degree, at FHEQ Level 6 (FQHEIS Level 10). Cite it as QAA (2024), Anthropology Subject Benchmark Statement, section 4, Knowledge and understanding table, Anthropology (general), item 10, threshold column. Do not call it a regulatory requirement, a full curriculum or a master's standard. Set it beside its strong/excellent form qaa/anthropology-2024/ku.10.e, the FHEQ honours descriptor qaa/fheq-2024/4.15.b7 and Annex D's third-class row qaa/fheq-2024/annex-d/cognitive/r2/3rd (spine:6, strand:thinking)."
  author-agent-dialogue: "Raise it when a student asks what they must at least be able to do on strengths and weaknesses of concepts, theories and methods, or when a programme team checks a module against the threshold for any Anthropology honours degree. With a student, put it plainly in the second person; with staff, frame it as the minimum the course must evidence. Ask: 'Pick one method you have used: what is it good at and where does it fall short?' Do not read the table out at length or offer the strong/excellent column as the pass mark."
- statement: qaa/anthropology-2024/ku.11.e
  forPractitioner: { text: "Above threshold, and as the expectation for master's study (4.8), look for evidence that the student can show critical insight into past and present arguments about human societies and cultures, and into how they help in studying social and cultural variety.", rewrite: light, force: describes, status: drafted }
  forBeneficiary: { text: "To reach strong or excellent work, you would go further and show critical insight into past and present arguments about human societies and cultures, and into how they help in studying social and cultural variety.", rewrite: full, force: describes, status: drafted }
  author-agent-written: "Treat this as the strong or excellent form of item 11 on debates on human societies and their use: a description of performance above the threshold for the honours degree at FHEQ Level 6, and what 4.8 expects of master's students at Level 7/11. Cite it as QAA (2024), Anthropology Subject Benchmark Statement, section 4, Knowledge and understanding table, Social Anthropology (specific), item 11, strong/excellent column. Do not present it as the pass standard or as a requirement for the award. Set it beside the threshold form qaa/anthropology-2024/ku.11.t, Annex D's upper rows qaa/fheq-2024/annex-d/knowledge/r2/2.1 and /1st and, for master's work, qaa/fheq-2024/4.17.b1."
  author-agent-dialogue: "Raise it when a student who has met the minimum on the history of Social Anthropology and social theory asks how to do better, or when staff plan stretch tasks or master's study. Present it as a step above the threshold, never as the minimum: in plain words to a student and as a design aim to staff. Ask: 'Which current debate about societies most changes how you study cultural variety?' Avoid reading the issuer's wording aloud or implying that a student fails without it."
- statement: qaa/anthropology-2024/ku.11.t
  forPractitioner: { text: "Threshold: plan teaching and assessment so that every honours graduate on a degree mainly in Social Anthropology shows they can outline how Social Anthropology and wider social theory developed, and know the arguments now current in both.", rewrite: light, force: threshold, status: drafted }
  forBeneficiary: { text: "By the end of your honours degree you will, as a minimum, be able to outline how Social Anthropology and wider social theory developed, and know the arguments now current in both.", rewrite: full, force: threshold, status: drafted }
  author-agent-written: "Treat this as a threshold standard: the least an honours graduate will have shown on the history of Social Anthropology and social theory, for degrees mainly in Social Anthropology (4.6), at FHEQ Level 6 (FQHEIS Level 10). Cite it as QAA (2024), Anthropology Subject Benchmark Statement, section 4, Knowledge and understanding table, Social Anthropology (specific), item 11, threshold column. Do not call it a regulatory requirement, a full curriculum or a master's standard. Set it beside its strong/excellent form qaa/anthropology-2024/ku.11.e, the FHEQ honours descriptor qaa/fheq-2024/4.15.b3.2 and Annex D's third-class row qaa/fheq-2024/annex-d/knowledge/r2/3rd (spine:6, strand:knowledge)."
  author-agent-dialogue: "Raise it when a student asks what they must at least be able to do on the history of Social Anthropology and social theory, or when a programme team checks a module against the threshold for degrees mainly in Social Anthropology (4.6). With a student, put it plainly in the second person; with staff, frame it as the minimum the course must evidence. Ask: 'How would you summarise the main turns in social theory, and which debates are live now?' Do not read the table out at length or offer the strong/excellent column as the pass mark."
- statement: qaa/anthropology-2024/ku.12.e
  forPractitioner: { text: "Above threshold, and as the expectation for master's study (4.8), look for evidence that the student can evaluate critically, and design, analyses that explain the nature and causes of social and cultural variety among people today and what follows from it.", rewrite: light, force: describes, status: drafted }
  forBeneficiary: { text: "To reach strong or excellent work, you would go further and evaluate critically, and design, analyses that explain the nature and causes of social and cultural variety among people today and what follows from it.", rewrite: full, force: describes, status: drafted }
  author-agent-written: "Treat this as the strong or excellent form of item 12 on designing analyses of social and cultural diversity: a description of performance above the threshold for the honours degree at FHEQ Level 6, and what 4.8 expects of master's students at Level 7/11. Cite it as QAA (2024), Anthropology Subject Benchmark Statement, section 4, Knowledge and understanding table, Social Anthropology (specific), item 12, strong/excellent column. Do not present it as the pass standard or as a requirement for the award. Set it beside the threshold form qaa/anthropology-2024/ku.12.t, Annex D's upper rows qaa/fheq-2024/annex-d/cognitive/r1/2.1 and /1st and, for master's work, qaa/fheq-2024/4.17.b1."
  author-agent-dialogue: "Raise it when a student who has met the minimum on social and cultural diversity today asks how to do better, or when staff plan stretch tasks or master's study. Present it as a step above the threshold, never as the minimum: in plain words to a student and as a design aim to staff. Ask: 'How would you design a study to explain why one social difference exists?' Avoid reading the issuer's wording aloud or implying that a student fails without it."
- statement: qaa/anthropology-2024/ku.12.t
  forPractitioner: { text: "Threshold: plan teaching and assessment so that every honours graduate on a degree mainly in Social Anthropology shows they can describe, analyse and talk through aspects of social and cultural variety among people today and what follows from it.", rewrite: light, force: threshold, status: drafted }
  forBeneficiary: { text: "By the end of your honours degree you will, as a minimum, be able to describe, analyse and talk through aspects of social and cultural variety among people today and what follows from it.", rewrite: full, force: threshold, status: drafted }
  author-agent-written: "Treat this as a threshold standard: the least an honours graduate will have shown on social and cultural diversity today, for degrees mainly in Social Anthropology (4.6), at FHEQ Level 6 (FQHEIS Level 10). Cite it as QAA (2024), Anthropology Subject Benchmark Statement, section 4, Knowledge and understanding table, Social Anthropology (specific), item 12, threshold column. Do not call it a regulatory requirement, a full curriculum or a master's standard. Set it beside its strong/excellent form qaa/anthropology-2024/ku.12.e, the FHEQ honours descriptor qaa/fheq-2024/4.15.b7 and Annex D's third-class row qaa/fheq-2024/annex-d/cognitive/r1/3rd (spine:6, strand:thinking)."
  author-agent-dialogue: "Raise it when a student asks what they must at least be able to do on social and cultural diversity today, or when a programme team checks a module against the threshold for degrees mainly in Social Anthropology (4.6). With a student, put it plainly in the second person; with staff, frame it as the minimum the course must evidence. Ask: 'What aspect of present-day social variety have you analysed, and what did it imply?' Do not read the table out at length or offer the strong/excellent column as the pass mark."
- statement: qaa/anthropology-2024/ku.13.e
  forPractitioner: { text: "Above threshold, and as the expectation for master's study (4.8), look for evidence that the student can hold that deep knowledge and also explain where the chosen region, culture, group or aspect sits within human variety as a whole.", rewrite: light, force: describes, status: drafted }
  forBeneficiary: { text: "To reach strong or excellent work, you would go further and hold that deep knowledge and also explain where the chosen region, culture, group or aspect sits within human variety as a whole.", rewrite: full, force: describes, status: drafted }
  author-agent-written: "Treat this as the strong or excellent form of item 13 on placing a specialism in the wider picture of diversity: a description of performance above the threshold for the honours degree at FHEQ Level 6, and what 4.8 expects of master's students at Level 7/11. Cite it as QAA (2024), Anthropology Subject Benchmark Statement, section 4, Knowledge and understanding table, Social Anthropology (specific), item 13, strong/excellent column. Do not present it as the pass standard or as a requirement for the award. Set it beside the threshold form qaa/anthropology-2024/ku.13.t, Annex D's upper rows qaa/fheq-2024/annex-d/knowledge/r1/2.1 and /1st and, for master's work, qaa/fheq-2024/4.17.b1."
  author-agent-dialogue: "Raise it when a student who has met the minimum on in-depth knowledge of a region, culture, group or aspect asks how to do better, or when staff plan stretch tasks or master's study. Present it as a step above the threshold, never as the minimum: in plain words to a student and as a design aim to staff. Ask: 'How does your specialist area change or confirm the wider picture of human variety?' Avoid reading the issuer's wording aloud or implying that a student fails without it."
- statement: qaa/anthropology-2024/ku.13.t
  forPractitioner: { text: "Threshold: plan teaching and assessment so that every honours graduate on a degree mainly in Social Anthropology shows they can show deep knowledge and understanding of one region, culture or group, or of one aspect of human society and culture.", rewrite: light, force: threshold, status: drafted }
  forBeneficiary: { text: "By the end of your honours degree you will, as a minimum, be able to show deep knowledge and understanding of one region, culture or group, or of one aspect of human society and culture.", rewrite: full, force: threshold, status: drafted }
  author-agent-written: "Treat this as a threshold standard: the least an honours graduate will have shown on in-depth knowledge of a region, culture, group or aspect, for degrees mainly in Social Anthropology (4.6), at FHEQ Level 6 (FQHEIS Level 10). Cite it as QAA (2024), Anthropology Subject Benchmark Statement, section 4, Knowledge and understanding table, Social Anthropology (specific), item 13, threshold column. Do not call it a regulatory requirement, a full curriculum or a master's standard. Set it beside its strong/excellent form qaa/anthropology-2024/ku.13.e, the FHEQ honours descriptor qaa/fheq-2024/4.15.b1 and Annex D's third-class row qaa/fheq-2024/annex-d/knowledge/r1/3rd (spine:6, strand:knowledge)."
  author-agent-dialogue: "Raise it when a student asks what they must at least be able to do on in-depth knowledge of a region, culture, group or aspect, or when a programme team checks a module against the threshold for degrees mainly in Social Anthropology (4.6). With a student, put it plainly in the second person; with staff, frame it as the minimum the course must evidence. Ask: 'Which region, group or aspect do you know in most depth, and how did you build that knowledge?' Do not read the table out at length or offer the strong/excellent column as the pass mark."
- statement: qaa/anthropology-2024/ku.14.e
  forPractitioner: { text: "Above threshold, and as the expectation for master's study (4.8), look for evidence that the student can appreciate, and understand critically, how social and cultural variety and human ecodynamics bear on each other in both directions.", rewrite: light, force: describes, status: drafted }
  forBeneficiary: { text: "To reach strong or excellent work, you would go further and appreciate, and understand critically, how social and cultural variety and human ecodynamics bear on each other in both directions.", rewrite: full, force: describes, status: drafted }
  author-agent-written: "Treat this as the strong or excellent form of item 14 on critical understanding of diversity and ecodynamics: a description of performance above the threshold for the honours degree at FHEQ Level 6, and what 4.8 expects of master's students at Level 7/11. Cite it as QAA (2024), Anthropology Subject Benchmark Statement, section 4, Knowledge and understanding table, Social Anthropology (specific), item 14, strong/excellent column. Do not present it as the pass standard or as a requirement for the award. Set it beside the threshold form qaa/anthropology-2024/ku.14.t, Annex D's upper rows qaa/fheq-2024/annex-d/knowledge/r2/2.1 and /1st and, for master's work, qaa/fheq-2024/4.17.b1."
  author-agent-dialogue: "Raise it when a student who has met the minimum on social diversity and human ecodynamics asks how to do better, or when staff plan stretch tasks or master's study. Present it as a step above the threshold, never as the minimum: in plain words to a student and as a design aim to staff. Ask: 'What would a critic say is missing from that account of people and environment?' Avoid reading the issuer's wording aloud or implying that a student fails without it."
- statement: qaa/anthropology-2024/ku.14.t
  forPractitioner: { text: "Threshold: plan teaching and assessment so that every honours graduate on a degree mainly in Social Anthropology shows they can appreciate how social and cultural variety and human ecodynamics bear on each other in both directions.", rewrite: light, force: threshold, status: drafted }
  forBeneficiary: { text: "By the end of your honours degree you will, as a minimum, be able to appreciate how social and cultural variety and human ecodynamics bear on each other in both directions.", rewrite: full, force: threshold, status: drafted }
  author-agent-written: "Treat this as a threshold standard: the least an honours graduate will have shown on social diversity and human ecodynamics, for degrees mainly in Social Anthropology (4.6), at FHEQ Level 6 (FQHEIS Level 10). Cite it as QAA (2024), Anthropology Subject Benchmark Statement, section 4, Knowledge and understanding table, Social Anthropology (specific), item 14, threshold column. Do not call it a regulatory requirement, a full curriculum or a master's standard. Set it beside its strong/excellent form qaa/anthropology-2024/ku.14.e, the FHEQ honours descriptor qaa/fheq-2024/4.15.b1 and Annex D's third-class row qaa/fheq-2024/annex-d/knowledge/r2/3rd (spine:6, strand:knowledge)."
  author-agent-dialogue: "Raise it when a student asks what they must at least be able to do on social diversity and human ecodynamics, or when a programme team checks a module against the threshold for degrees mainly in Social Anthropology (4.6). With a student, put it plainly in the second person; with staff, frame it as the minimum the course must evidence. Ask: 'Can you give a case where a way of life changed an ecosystem, and the ecosystem changed it back?' Do not read the table out at length or offer the strong/excellent column as the pass mark."
- statement: qaa/anthropology-2024/ku.15.e
  forPractitioner: { text: "Above threshold, and as the expectation for master's study (4.8), look for evidence that the student can show critical insight into current debates on ethics in Biological Anthropology, judge others' research on that basis and design and carry out ethical research, scholarship, dissemination and engagement.", rewrite: light, force: describes, status: drafted }
  forBeneficiary: { text: "To reach strong or excellent work, you would go further and show critical insight into current debates on ethics in Biological Anthropology, judge others' research on that basis and design and carry out ethical research, scholarship, dissemination and engagement.", rewrite: full, force: describes, status: drafted }
  author-agent-written: "Treat this as the strong or excellent form of item 15 on ethical research, evaluation and engagement: a description of performance above the threshold for the honours degree at FHEQ Level 6, and what 4.8 expects of master's students at Level 7/11. Cite it as QAA (2024), Anthropology Subject Benchmark Statement, section 4, Knowledge and understanding table, Biological Anthropology (specific), item 15, strong/excellent column. Do not present it as the pass standard or as a requirement for the award. Set it beside the threshold form qaa/anthropology-2024/ku.15.t, Annex D's upper rows qaa/fheq-2024/annex-d/cognitive/r1/2.1 and /1st and, for master's work, qaa/fheq-2024/4.17.b1."
  author-agent-dialogue: "Raise it when a student who has met the minimum on ethical practice in Biological Anthropology asks how to do better, or when staff plan stretch tasks or master's study. Present it as a step above the threshold, never as the minimum: in plain words to a student and as a design aim to staff. Ask: 'How would you build fair collaboration with the people you study into your own project?' Avoid reading the issuer's wording aloud or implying that a student fails without it."
- statement: qaa/anthropology-2024/ku.15.t
  forPractitioner: { text: "Threshold: plan teaching and assessment so that every honours graduate on a degree mainly in Biological Anthropology shows they can describe past and present debates on ethics in Biological Anthropology, covering data collection, who makes up the international discipline and how academia is organised, and recognise why ethical practice and fair collaboration with the people studied matter.", rewrite: light, force: threshold, status: drafted }
  forBeneficiary: { text: "By the end of your honours degree you will, as a minimum, be able to describe past and present debates on ethics in Biological Anthropology, covering data collection, who makes up the international discipline and how academia is organised, and recognise why ethical practice and fair collaboration with the people studied matter.", rewrite: full, force: threshold, status: drafted }
  author-agent-written: "Treat this as a threshold standard: the least an honours graduate will have shown on ethical practice in Biological Anthropology, for degrees mainly in Biological Anthropology (4.6), at FHEQ Level 6 (FQHEIS Level 10). Cite it as QAA (2024), Anthropology Subject Benchmark Statement, section 4, Knowledge and understanding table, Biological Anthropology (specific), item 15, threshold column. Do not call it a regulatory requirement, a full curriculum or a master's standard. Set it beside its strong/excellent form qaa/anthropology-2024/ku.15.e, the FHEQ honours descriptor qaa/fheq-2024/4.15.b4 and Annex D's third-class row qaa/fheq-2024/annex-d/cognitive/r1/3rd (spine:6, strand:thinking)."
  author-agent-dialogue: "Raise it when a student asks what they must at least be able to do on ethical practice in Biological Anthropology, or when a programme team checks a module against the threshold for degrees mainly in Biological Anthropology (4.6). With a student, put it plainly in the second person; with staff, frame it as the minimum the course must evidence. Ask: 'What ethical debate in the field do you find most pressing, and who is affected by it?' Do not read the table out at length or offer the strong/excellent column as the pass mark."
- statement: qaa/anthropology-2024/ku.16.e
  forPractitioner: { text: "Above threshold, and as the expectation for master's study (4.8), look for evidence that the student can evaluate critically, and design, analyses that explain the nature and causes of biological variety among living humans or other primates, its social, cultural and ecological consequences and the tangle of social, cultural and environmental factors that produce it.", rewrite: light, force: describes, status: drafted }
  forBeneficiary: { text: "To reach strong or excellent work, you would go further and evaluate critically, and design, analyses that explain the nature and causes of biological variety among living humans or other primates, its social, cultural and ecological consequences and the tangle of social, cultural and environmental factors that produce it.", rewrite: full, force: describes, status: drafted }
  author-agent-written: "Treat this as the strong or excellent form of item 16 on designing analyses of biological diversity: a description of performance above the threshold for the honours degree at FHEQ Level 6, and what 4.8 expects of master's students at Level 7/11. Cite it as QAA (2024), Anthropology Subject Benchmark Statement, section 4, Knowledge and understanding table, Biological Anthropology (specific), item 16, strong/excellent column. Do not present it as the pass standard or as a requirement for the award. Set it beside the threshold form qaa/anthropology-2024/ku.16.t, Annex D's upper rows qaa/fheq-2024/annex-d/cognitive/r1/2.1 and /1st and, for master's work, qaa/fheq-2024/4.17.b1."
  author-agent-dialogue: "Raise it when a student who has met the minimum on biological diversity of humans and primates asks how to do better, or when staff plan stretch tasks or master's study. Present it as a step above the threshold, never as the minimum: in plain words to a student and as a design aim to staff. Ask: 'How would you design an analysis that separates environmental from social causes of a biological difference?' Avoid reading the issuer's wording aloud or implying that a student fails without it."
- statement: qaa/anthropology-2024/ku.16.t
  forPractitioner: { text: "Threshold: plan teaching and assessment so that every honours graduate on a degree mainly in Biological Anthropology shows they can describe, analyse and discuss aspects of biological variety among living humans and other primates, aware of its social, cultural and ecological consequences.", rewrite: light, force: threshold, status: drafted }
  forBeneficiary: { text: "By the end of your honours degree you will, as a minimum, be able to describe, analyse and discuss aspects of biological variety among living humans and other primates, aware of its social, cultural and ecological consequences.", rewrite: full, force: threshold, status: drafted }
  author-agent-written: "Treat this as a threshold standard: the least an honours graduate will have shown on biological diversity of humans and primates, for degrees mainly in Biological Anthropology (4.6), at FHEQ Level 6 (FQHEIS Level 10). Cite it as QAA (2024), Anthropology Subject Benchmark Statement, section 4, Knowledge and understanding table, Biological Anthropology (specific), item 16, threshold column. Do not call it a regulatory requirement, a full curriculum or a master's standard. Set it beside its strong/excellent form qaa/anthropology-2024/ku.16.e, the FHEQ honours descriptor qaa/fheq-2024/4.15.b7 and Annex D's third-class row qaa/fheq-2024/annex-d/cognitive/r1/3rd (spine:6, strand:thinking)."
  author-agent-dialogue: "Raise it when a student asks what they must at least be able to do on biological diversity of humans and primates, or when a programme team checks a module against the threshold for degrees mainly in Biological Anthropology (4.6). With a student, put it plainly in the second person; with staff, frame it as the minimum the course must evidence. Ask: 'What example of biological variation have you studied, and what social consequences does it have?' Do not read the table out at length or offer the strong/excellent column as the pass mark."
- statement: qaa/anthropology-2024/ku.17.e
  forPractitioner: { text: "Above threshold, and as the expectation for master's study (4.8), look for evidence that the student can understand human physiology thoroughly and critically and interpret its variation, whether evolutionary, developmental or pathological.", rewrite: light, force: describes, status: drafted }
  forBeneficiary: { text: "To reach strong or excellent work, you would go further and understand human physiology thoroughly and critically and interpret its variation, whether evolutionary, developmental or pathological.", rewrite: full, force: describes, status: drafted }
  author-agent-written: "Treat this as the strong or excellent form of item 17 on interpreting physiological variability: a description of performance above the threshold for the honours degree at FHEQ Level 6, and what 4.8 expects of master's students at Level 7/11. Cite it as QAA (2024), Anthropology Subject Benchmark Statement, section 4, Knowledge and understanding table, Biological Anthropology (specific), item 17, strong/excellent column. Do not present it as the pass standard or as a requirement for the award. Set it beside the threshold form qaa/anthropology-2024/ku.17.t, Annex D's upper rows qaa/fheq-2024/annex-d/knowledge/r1/2.1 and /1st and, for master's work, qaa/fheq-2024/4.17.b1."
  author-agent-dialogue: "Raise it when a student who has met the minimum on normal human physiology and pathology asks how to do better, or when staff plan stretch tasks or master's study. Present it as a step above the threshold, never as the minimum: in plain words to a student and as a design aim to staff. Ask: 'Faced with an unusual bone, how would you decide whether its form is developmental, evolutionary or pathological?' Avoid reading the issuer's wording aloud or implying that a student fails without it."
- statement: qaa/anthropology-2024/ku.17.t
  forPractitioner: { text: "Threshold: plan teaching and assessment so that every honours graduate on a degree mainly in Biological Anthropology shows they can understand typical human physiology well, including the skeleton's form, variation and growth, and recognise the main forms of pathology.", rewrite: light, force: threshold, status: drafted }
  forBeneficiary: { text: "By the end of your honours degree you will, as a minimum, be able to understand typical human physiology well, including the skeleton's form, variation and growth, and recognise the main forms of pathology.", rewrite: full, force: threshold, status: drafted }
  author-agent-written: "Treat this as a threshold standard: the least an honours graduate will have shown on normal human physiology and pathology, for degrees mainly in Biological Anthropology (4.6), at FHEQ Level 6 (FQHEIS Level 10). Cite it as QAA (2024), Anthropology Subject Benchmark Statement, section 4, Knowledge and understanding table, Biological Anthropology (specific), item 17, threshold column. Do not call it a regulatory requirement, a full curriculum or a master's standard. Set it beside its strong/excellent form qaa/anthropology-2024/ku.17.e, the FHEQ honours descriptor qaa/fheq-2024/4.15.b1 and Annex D's third-class row qaa/fheq-2024/annex-d/knowledge/r1/3rd (spine:6, strand:knowledge)."
  author-agent-dialogue: "Raise it when a student asks what they must at least be able to do on normal human physiology and pathology, or when a programme team checks a module against the threshold for degrees mainly in Biological Anthropology (4.6). With a student, put it plainly in the second person; with staff, frame it as the minimum the course must evidence. Ask: 'Could you identify the main signs of pathology on a skeleton, and what would you need to check?' Do not read the table out at length or offer the strong/excellent column as the pass mark."
- statement: qaa/anthropology-2024/ku.18.e
  forPractitioner: { text: "Above threshold, and as the expectation for master's study (4.8), look for evidence that the student can show critical insight into past and present arguments in Biological Anthropology and evolutionary theory, and into how they help in studying human physical and cultural variety.", rewrite: light, force: describes, status: drafted }
  forBeneficiary: { text: "To reach strong or excellent work, you would go further and show critical insight into past and present arguments in Biological Anthropology and evolutionary theory, and into how they help in studying human physical and cultural variety.", rewrite: full, force: describes, status: drafted }
  author-agent-written: "Treat this as the strong or excellent form of item 18 on debates on Biological Anthropology and evolutionary theory: a description of performance above the threshold for the honours degree at FHEQ Level 6, and what 4.8 expects of master's students at Level 7/11. Cite it as QAA (2024), Anthropology Subject Benchmark Statement, section 4, Knowledge and understanding table, Biological Anthropology (specific), item 18, strong/excellent column. Do not present it as the pass standard or as a requirement for the award. Set it beside the threshold form qaa/anthropology-2024/ku.18.t, Annex D's upper rows qaa/fheq-2024/annex-d/knowledge/r2/2.1 and /1st and, for master's work, qaa/fheq-2024/4.17.b1."
  author-agent-dialogue: "Raise it when a student who has met the minimum on the history of Biological Anthropology and evolutionary theory asks how to do better, or when staff plan stretch tasks or master's study. Present it as a step above the threshold, never as the minimum: in plain words to a student and as a design aim to staff. Ask: 'Which current debate in evolutionary theory most changes how you read human variation?' Avoid reading the issuer's wording aloud or implying that a student fails without it."
- statement: qaa/anthropology-2024/ku.18.t
  forPractitioner: { text: "Threshold: plan teaching and assessment so that every honours graduate on a degree mainly in Biological Anthropology shows they can outline how Biological Anthropology and wider evolutionary theory developed, and know the arguments now current in both.", rewrite: light, force: threshold, status: drafted }
  forBeneficiary: { text: "By the end of your honours degree you will, as a minimum, be able to outline how Biological Anthropology and wider evolutionary theory developed, and know the arguments now current in both.", rewrite: full, force: threshold, status: drafted }
  author-agent-written: "Treat this as a threshold standard: the least an honours graduate will have shown on the history of Biological Anthropology and evolutionary theory, for degrees mainly in Biological Anthropology (4.6), at FHEQ Level 6 (FQHEIS Level 10). Cite it as QAA (2024), Anthropology Subject Benchmark Statement, section 4, Knowledge and understanding table, Biological Anthropology (specific), item 18, threshold column. Do not call it a regulatory requirement, a full curriculum or a master's standard. Set it beside its strong/excellent form qaa/anthropology-2024/ku.18.e, the FHEQ honours descriptor qaa/fheq-2024/4.15.b3.2 and Annex D's third-class row qaa/fheq-2024/annex-d/knowledge/r2/3rd (spine:6, strand:knowledge)."
  author-agent-dialogue: "Raise it when a student asks what they must at least be able to do on the history of Biological Anthropology and evolutionary theory, or when a programme team checks a module against the threshold for degrees mainly in Biological Anthropology (4.6). With a student, put it plainly in the second person; with staff, frame it as the minimum the course must evidence. Ask: 'What are the main stages in the history of evolutionary thinking about humans?' Do not read the table out at length or offer the strong/excellent column as the pass mark."
- statement: qaa/anthropology-2024/ku.19.e
  forPractitioner: { text: "Above threshold, and as the expectation for master's study (4.8), look for evidence that the student can use evolutionary theory critically to show how physical, social and cultural evolution together shaped the bodies, behaviour and cognition of humans, hominins and primates, past and present, and explain how humans fit into nature in evolutionary terms.", rewrite: light, force: describes, status: drafted }
  forBeneficiary: { text: "To reach strong or excellent work, you would go further and use evolutionary theory critically to show how physical, social and cultural evolution together shaped the bodies, behaviour and cognition of humans, hominins and primates, past and present, and explain how humans fit into nature in evolutionary terms.", rewrite: full, force: describes, status: drafted }
  author-agent-written: "Treat this as the strong or excellent form of item 19 on applying evolutionary theory to human evolution: a description of performance above the threshold for the honours degree at FHEQ Level 6, and what 4.8 expects of master's students at Level 7/11. Cite it as QAA (2024), Anthropology Subject Benchmark Statement, section 4, Knowledge and understanding table, Biological Anthropology (specific), item 19, strong/excellent column. Do not present it as the pass standard or as a requirement for the award. Set it beside the threshold form qaa/anthropology-2024/ku.19.t, Annex D's upper rows qaa/fheq-2024/annex-d/knowledge/r2/2.1 and /1st and, for master's work, qaa/fheq-2024/4.17.b1."
  author-agent-dialogue: "Raise it when a student who has met the minimum on evolutionary theory and our place in nature asks how to do better, or when staff plan stretch tasks or master's study. Present it as a step above the threshold, never as the minimum: in plain words to a student and as a design aim to staff. Ask: 'Can you show how social and physical evolution might have shaped one human trait together?' Avoid reading the issuer's wording aloud or implying that a student fails without it."
- statement: qaa/anthropology-2024/ku.19.t
  forPractitioner: { text: "Threshold: plan teaching and assessment so that every honours graduate on a degree mainly in Biological Anthropology shows they can describe the basics of evolutionary theory and how the bodies, behaviour and cognition of humans, hominins and primates evolved, and show knowledge of where our species stands in nature.", rewrite: light, force: threshold, status: drafted }
  forBeneficiary: { text: "By the end of your honours degree you will, as a minimum, be able to describe the basics of evolutionary theory and how the bodies, behaviour and cognition of humans, hominins and primates evolved, and show knowledge of where our species stands in nature.", rewrite: full, force: threshold, status: drafted }
  author-agent-written: "Treat this as a threshold standard: the least an honours graduate will have shown on evolutionary theory and our place in nature, for degrees mainly in Biological Anthropology (4.6), at FHEQ Level 6 (FQHEIS Level 10). Cite it as QAA (2024), Anthropology Subject Benchmark Statement, section 4, Knowledge and understanding table, Biological Anthropology (specific), item 19, threshold column. Do not call it a regulatory requirement, a full curriculum or a master's standard. Set it beside its strong/excellent form qaa/anthropology-2024/ku.19.e, the FHEQ honours descriptor qaa/fheq-2024/4.15.b1 and Annex D's third-class row qaa/fheq-2024/annex-d/knowledge/r2/3rd (spine:6, strand:knowledge)."
  author-agent-dialogue: "Raise it when a student asks what they must at least be able to do on evolutionary theory and our place in nature, or when a programme team checks a module against the threshold for degrees mainly in Biological Anthropology (4.6). With a student, put it plainly in the second person; with staff, frame it as the minimum the course must evidence. Ask: 'How would you explain to a friend where humans sit among the primates?' Do not read the table out at length or offer the strong/excellent column as the pass mark."
- statement: qaa/anthropology-2024/ku.20.e
  forPractitioner: { text: "Above threshold, and as the expectation for master's study (4.8), look for evidence that the student can evaluate critically hypotheses about why variation among hominins and other primates is adaptive, and interpret varied evidence on human or primate biological variety in those terms.", rewrite: light, force: describes, status: drafted }
  forBeneficiary: { text: "To reach strong or excellent work, you would go further and evaluate critically hypotheses about why variation among hominins and other primates is adaptive, and interpret varied evidence on human or primate biological variety in those terms.", rewrite: full, force: describes, status: drafted }
  author-agent-written: "Treat this as the strong or excellent form of item 20 on hypotheses on adaptive significance: a description of performance above the threshold for the honours degree at FHEQ Level 6, and what 4.8 expects of master's students at Level 7/11. Cite it as QAA (2024), Anthropology Subject Benchmark Statement, section 4, Knowledge and understanding table, Biological Anthropology (specific), item 20, strong/excellent column. Do not present it as the pass standard or as a requirement for the award. Set it beside the threshold form qaa/anthropology-2024/ku.20.t, Annex D's upper rows qaa/fheq-2024/annex-d/cognitive/r2/2.1 and /1st and, for master's work, qaa/fheq-2024/4.17.b1."
  author-agent-dialogue: "Raise it when a student who has met the minimum on similarities and contrasts among primates asks how to do better, or when staff plan stretch tasks or master's study. Present it as a step above the threshold, never as the minimum: in plain words to a student and as a design aim to staff. Ask: 'What evidence would make you doubt an adaptive explanation you have read?' Avoid reading the issuer's wording aloud or implying that a student fails without it."
- statement: qaa/anthropology-2024/ku.20.t
  forPractitioner: { text: "Threshold: plan teaching and assessment so that every honours graduate on a degree mainly in Biological Anthropology shows they can describe some likenesses and differences between humans, hominins and other primates and discuss what they mean for adaptation.", rewrite: light, force: threshold, status: drafted }
  forBeneficiary: { text: "By the end of your honours degree you will, as a minimum, be able to describe some likenesses and differences between humans, hominins and other primates and discuss what they mean for adaptation.", rewrite: full, force: threshold, status: drafted }
  author-agent-written: "Treat this as a threshold standard: the least an honours graduate will have shown on similarities and contrasts among primates, for degrees mainly in Biological Anthropology (4.6), at FHEQ Level 6 (FQHEIS Level 10). Cite it as QAA (2024), Anthropology Subject Benchmark Statement, section 4, Knowledge and understanding table, Biological Anthropology (specific), item 20, threshold column. Do not call it a regulatory requirement, a full curriculum or a master's standard. Set it beside its strong/excellent form qaa/anthropology-2024/ku.20.e, the FHEQ honours descriptor qaa/fheq-2024/4.15.b7 and Annex D's third-class row qaa/fheq-2024/annex-d/cognitive/r2/3rd (spine:6, strand:thinking)."
  author-agent-dialogue: "Raise it when a student asks what they must at least be able to do on similarities and contrasts among primates, or when a programme team checks a module against the threshold for degrees mainly in Biological Anthropology (4.6). With a student, put it plainly in the second person; with staff, frame it as the minimum the course must evidence. Ask: 'Which difference between humans and another primate do you think matters most for adaptation?' Do not read the table out at length or offer the strong/excellent column as the pass mark."
- statement: qaa/anthropology-2024/ku.21.e
  forPractitioner: { text: "Above threshold, and as the expectation for master's study (4.8), look for evidence that the student can show critical insight into the processes, mechanisms and likely causes of variation across place and time in primate, hominin and human evolution.", rewrite: light, force: describes, status: drafted }
  forBeneficiary: { text: "To reach strong or excellent work, you would go further and show critical insight into the processes, mechanisms and likely causes of variation across place and time in primate, hominin and human evolution.", rewrite: full, force: describes, status: drafted }
  author-agent-written: "Treat this as the strong or excellent form of item 21 on processes behind variability in evolution: a description of performance above the threshold for the honours degree at FHEQ Level 6, and what 4.8 expects of master's students at Level 7/11. Cite it as QAA (2024), Anthropology Subject Benchmark Statement, section 4, Knowledge and understanding table, Biological Anthropology (specific), item 21, strong/excellent column. Do not present it as the pass standard or as a requirement for the award. Set it beside the threshold form qaa/anthropology-2024/ku.21.t, Annex D's upper rows qaa/fheq-2024/annex-d/knowledge/r1/2.1 and /1st and, for master's work, qaa/fheq-2024/4.17.b1."
  author-agent-dialogue: "Raise it when a student who has met the minimum on distribution and traits of primate and hominin species asks how to do better, or when staff plan stretch tasks or master's study. Present it as a step above the threshold, never as the minimum: in plain words to a student and as a design aim to staff. Ask: 'What do you think best explains why one species spread and another did not?' Avoid reading the issuer's wording aloud or implying that a student fails without it."
- statement: qaa/anthropology-2024/ku.21.t
  forPractitioner: { text: "Threshold: plan teaching and assessment so that every honours graduate on a degree mainly in Biological Anthropology shows they can describe where and when key primate or hominin species lived and their main physical and behavioural traits, as fits the course.", rewrite: light, force: threshold, status: drafted }
  forBeneficiary: { text: "By the end of your honours degree you will, as a minimum, be able to describe where and when key primate or hominin species lived and their main physical and behavioural traits, as fits the course.", rewrite: full, force: threshold, status: drafted }
  author-agent-written: "Treat this as a threshold standard: the least an honours graduate will have shown on distribution and traits of primate and hominin species, for degrees mainly in Biological Anthropology (4.6), at FHEQ Level 6 (FQHEIS Level 10). Cite it as QAA (2024), Anthropology Subject Benchmark Statement, section 4, Knowledge and understanding table, Biological Anthropology (specific), item 21, threshold column. Do not call it a regulatory requirement, a full curriculum or a master's standard. Set it beside its strong/excellent form qaa/anthropology-2024/ku.21.e, the FHEQ honours descriptor qaa/fheq-2024/4.15.b1 and Annex D's third-class row qaa/fheq-2024/annex-d/knowledge/r1/3rd (spine:6, strand:knowledge)."
  author-agent-dialogue: "Raise it when a student asks what they must at least be able to do on distribution and traits of primate and hominin species, or when a programme team checks a module against the threshold for degrees mainly in Biological Anthropology (4.6). With a student, put it plainly in the second person; with staff, frame it as the minimum the course must evidence. Ask: 'Could you place three hominin species in time and space and say how they differed?' Do not read the table out at length or offer the strong/excellent column as the pass mark."
- statement: qaa/anthropology-2024/ku.22.e
  forPractitioner: { text: "Above threshold, and as the expectation for master's study (4.8), look for evidence that the student can evaluate and bring together several lines of evidence and hypotheses on how and why primate, hominin and human evolution and variation within our species happened, and know how far present data can support any reading.", rewrite: light, force: describes, status: drafted }
  forBeneficiary: { text: "To reach strong or excellent work, you would go further and evaluate and bring together several lines of evidence and hypotheses on how and why primate, hominin and human evolution and variation within our species happened, and know how far present data can support any reading.", rewrite: full, force: describes, status: drafted }
  author-agent-written: "Treat this as the strong or excellent form of item 22 on synthesising evidence on evolution and variability: a description of performance above the threshold for the honours degree at FHEQ Level 6, and what 4.8 expects of master's students at Level 7/11. Cite it as QAA (2024), Anthropology Subject Benchmark Statement, section 4, Knowledge and understanding table, Biological Anthropology (specific), item 22, strong/excellent column. Do not present it as the pass standard or as a requirement for the award. Set it beside the threshold form qaa/anthropology-2024/ku.22.t, Annex D's upper rows qaa/fheq-2024/annex-d/knowledge/r3/2.1 and /1st and, for master's work, qaa/fheq-2024/4.17.b1."
  author-agent-dialogue: "Raise it when a student who has met the minimum on interpreting the fossil and bioarchaeological record asks how to do better, or when staff plan stretch tasks or master's study. Present it as a step above the threshold, never as the minimum: in plain words to a student and as a design aim to staff. Ask: 'Where two lines of evidence disagree, how do you decide what the data can bear?' Avoid reading the issuer's wording aloud or implying that a student fails without it."
- statement: qaa/anthropology-2024/ku.22.t
  forPractitioner: { text: "Threshold: plan teaching and assessment so that every honours graduate on a degree mainly in Biological Anthropology shows they can appreciate the arguments over how the hominin and human fossil and bioarchaeological record is read, its likely biases and how taphonomy affects what can be said about evolution and the human past.", rewrite: light, force: threshold, status: drafted }
  forBeneficiary: { text: "By the end of your honours degree you will, as a minimum, be able to appreciate the arguments over how the hominin and human fossil and bioarchaeological record is read, its likely biases and how taphonomy affects what can be said about evolution and the human past.", rewrite: full, force: threshold, status: drafted }
  author-agent-written: "Treat this as a threshold standard: the least an honours graduate will have shown on interpreting the fossil and bioarchaeological record, for degrees mainly in Biological Anthropology (4.6), at FHEQ Level 6 (FQHEIS Level 10). Cite it as QAA (2024), Anthropology Subject Benchmark Statement, section 4, Knowledge and understanding table, Biological Anthropology (specific), item 22, threshold column. Do not call it a regulatory requirement, a full curriculum or a master's standard. Set it beside its strong/excellent form qaa/anthropology-2024/ku.22.e, the FHEQ honours descriptor qaa/fheq-2024/4.15.b4 and Annex D's third-class row qaa/fheq-2024/annex-d/knowledge/r3/3rd (spine:6, strand:knowledge)."
  author-agent-dialogue: "Raise it when a student asks what they must at least be able to do on interpreting the fossil and bioarchaeological record, or when a programme team checks a module against the threshold for degrees mainly in Biological Anthropology (4.6). With a student, put it plainly in the second person; with staff, frame it as the minimum the course must evidence. Ask: 'What biases in the fossil record should make you cautious about a claim?' Do not read the table out at length or offer the strong/excellent column as the pass mark."
- statement: qaa/anthropology-2024/ku.23.e
  forPractitioner: { text: "Above threshold, and as the expectation for master's study (4.8), look for evidence that the student can evaluate critically the arguments about combining (palaeo)genetic data with fossil and behavioural evidence.", rewrite: light, force: describes, status: drafted }
  forBeneficiary: { text: "To reach strong or excellent work, you would go further and evaluate critically the arguments about combining (palaeo)genetic data with fossil and behavioural evidence.", rewrite: full, force: describes, status: drafted }
  author-agent-written: "Treat this as the strong or excellent form of item 23 on integrating (palaeo)genetic data: a description of performance above the threshold for the honours degree at FHEQ Level 6, and what 4.8 expects of master's students at Level 7/11. Cite it as QAA (2024), Anthropology Subject Benchmark Statement, section 4, Knowledge and understanding table, Biological Anthropology (specific), item 23, strong/excellent column. Do not present it as the pass standard or as a requirement for the award. Set it beside the threshold form qaa/anthropology-2024/ku.23.t, Annex D's upper rows qaa/fheq-2024/annex-d/knowledge/r1/2.1 and /1st and, for master's work, qaa/fheq-2024/4.17.b1."
  author-agent-dialogue: "Raise it when a student who has met the minimum on genetic evidence beside fossil and behavioural data asks how to do better, or when staff plan stretch tasks or master's study. Present it as a step above the threshold, never as the minimum: in plain words to a student and as a design aim to staff. Ask: 'Where do genetic and fossil evidence pull in different directions, and how would you weigh them?' Avoid reading the issuer's wording aloud or implying that a student fails without it."
- statement: qaa/anthropology-2024/ku.23.t
  forPractitioner: { text: "Threshold: plan teaching and assessment so that every honours graduate on a degree mainly in Biological Anthropology shows they can recognise why genetic evolution and (palaeo)genetic study matter, alongside fossil and behavioural evidence, for understanding the evolution of humans, hominins and primates.", rewrite: light, force: threshold, status: drafted }
  forBeneficiary: { text: "By the end of your honours degree you will, as a minimum, be able to recognise why genetic evolution and (palaeo)genetic study matter, alongside fossil and behavioural evidence, for understanding the evolution of humans, hominins and primates.", rewrite: full, force: threshold, status: drafted }
  author-agent-written: "Treat this as a threshold standard: the least an honours graduate will have shown on genetic evidence beside fossil and behavioural data, for degrees mainly in Biological Anthropology (4.6), at FHEQ Level 6 (FQHEIS Level 10). Cite it as QAA (2024), Anthropology Subject Benchmark Statement, section 4, Knowledge and understanding table, Biological Anthropology (specific), item 23, threshold column. Do not call it a regulatory requirement, a full curriculum or a master's standard. Set it beside its strong/excellent form qaa/anthropology-2024/ku.23.e, the FHEQ honours descriptor qaa/fheq-2024/4.15.b1 and Annex D's third-class row qaa/fheq-2024/annex-d/knowledge/r1/3rd (spine:6, strand:knowledge)."
  author-agent-dialogue: "Raise it when a student asks what they must at least be able to do on genetic evidence beside fossil and behavioural data, or when a programme team checks a module against the threshold for degrees mainly in Biological Anthropology (4.6). With a student, put it plainly in the second person; with staff, frame it as the minimum the course must evidence. Ask: 'What has genetic evidence added that fossils alone could not tell us?' Do not read the table out at length or offer the strong/excellent column as the pass mark."
- statement: qaa/anthropology-2024/ku.24.e
  forPractitioner: { text: "Above threshold, and as the expectation for master's study (4.8), look for evidence that the student can evaluate critically the arguments about combining different kinds of data, and bring several lines of evidence together into a coherent account.", rewrite: light, force: describes, status: drafted }
  forBeneficiary: { text: "To reach strong or excellent work, you would go further and evaluate critically the arguments about combining different kinds of data, and bring several lines of evidence together into a coherent account.", rewrite: full, force: describes, status: drafted }
  author-agent-written: "Treat this as the strong or excellent form of item 24 on integrating and synthesising types of evidence: a description of performance above the threshold for the honours degree at FHEQ Level 6, and what 4.8 expects of master's students at Level 7/11. Cite it as QAA (2024), Anthropology Subject Benchmark Statement, section 4, Knowledge and understanding table, Biological Anthropology (specific), item 24, strong/excellent column. Do not present it as the pass standard or as a requirement for the award. Set it beside the threshold form qaa/anthropology-2024/ku.24.t, Annex D's upper rows qaa/fheq-2024/annex-d/knowledge/r3/2.1 and /1st and, for master's work, qaa/fheq-2024/4.17.b1."
  author-agent-dialogue: "Raise it when a student who has met the minimum on lines of evidence for biological diversity asks how to do better, or when staff plan stretch tasks or master's study. Present it as a step above the threshold, never as the minimum: in plain words to a student and as a design aim to staff. Ask: 'How would you combine three kinds of evidence into one account without hiding their conflicts?' Avoid reading the issuer's wording aloud or implying that a student fails without it."
- statement: qaa/anthropology-2024/ku.24.t
  forPractitioner: { text: "Threshold: plan teaching and assessment so that every honours graduate on a degree mainly in Biological Anthropology shows they can know the many kinds of evidence for human, hominin and primate biological variety, from fossils and skeletons, behaviour studies, primatology and ethnography to archaeology, genetics and molecular work, with the strengths and weaknesses of each.", rewrite: light, force: threshold, status: drafted }
  forBeneficiary: { text: "By the end of your honours degree you will, as a minimum, be able to know the many kinds of evidence for human, hominin and primate biological variety, from fossils and skeletons, behaviour studies, primatology and ethnography to archaeology, genetics and molecular work, with the strengths and weaknesses of each.", rewrite: full, force: threshold, status: drafted }
  author-agent-written: "Treat this as a threshold standard: the least an honours graduate will have shown on lines of evidence for biological diversity, for degrees mainly in Biological Anthropology (4.6), at FHEQ Level 6 (FQHEIS Level 10). Cite it as QAA (2024), Anthropology Subject Benchmark Statement, section 4, Knowledge and understanding table, Biological Anthropology (specific), item 24, threshold column. Do not call it a regulatory requirement, a full curriculum or a master's standard. Set it beside its strong/excellent form qaa/anthropology-2024/ku.24.e, the FHEQ honours descriptor qaa/fheq-2024/4.15.b1 and Annex D's third-class row qaa/fheq-2024/annex-d/knowledge/r3/3rd (spine:6, strand:knowledge)."
  author-agent-dialogue: "Raise it when a student asks what they must at least be able to do on lines of evidence for biological diversity, or when a programme team checks a module against the threshold for degrees mainly in Biological Anthropology (4.6). With a student, put it plainly in the second person; with staff, frame it as the minimum the course must evidence. Ask: 'Which kinds of evidence have you worked with, and what can each not tell you?' Do not read the table out at length or offer the strong/excellent column as the pass mark."
- statement: qaa/anthropology-2024/ss.1.e
  forPractitioner: { text: "Above threshold, and as the expectation for master's study (4.8), look for evidence that the student can plan and carry through a research programme, from choosing suitable questions to sharing the results.", rewrite: light, force: describes, status: drafted }
  forBeneficiary: { text: "To reach strong or excellent work, you would go further and plan and carry through a research programme, from choosing suitable questions to sharing the results.", rewrite: full, force: describes, status: drafted }
  author-agent-written: "Treat this as the strong or excellent form of item 1 on designing and running a whole research programme: a description of performance above the threshold for the honours degree at FHEQ Level 6, and what 4.8 expects of master's students at Level 7/11. Cite it as QAA (2024), Anthropology Subject Benchmark Statement, section 4, Subject-specific skills table, Anthropology (general), item 1, strong/excellent column. Do not present it as the pass standard or as a requirement for the award. Set it beside the threshold form qaa/anthropology-2024/ss.1.t, Annex D's upper rows qaa/fheq-2024/annex-d/practical/r1/2.1 and /1st and, for master's work, qaa/fheq-2024/4.17.b1."
  author-agent-dialogue: "Raise it when a student who has met the minimum on designing and running fieldwork and practical work asks how to do better, or when staff plan stretch tasks or master's study. Present it as a step above the threshold, never as the minimum: in plain words to a student and as a design aim to staff. Ask: 'What question would you build a full project around, and how would you get from it to sharing results?' Avoid reading the issuer's wording aloud or implying that a student fails without it."
- statement: qaa/anthropology-2024/ss.1.t
  forPractitioner: { text: "Threshold: plan teaching and assessment so that every honours graduate shows they can understand what goes into planning and carrying out practical or field research to gather primary data, ethics review and risk assessment included, and evaluate such research and what it finds.", rewrite: light, force: threshold, status: drafted }
  forBeneficiary: { text: "By the end of your honours degree you will, as a minimum, be able to understand what goes into planning and carrying out practical or field research to gather primary data, ethics review and risk assessment included, and evaluate such research and what it finds.", rewrite: full, force: threshold, status: drafted }
  author-agent-written: "Treat this as a threshold standard: the least an honours graduate will have shown on designing and running fieldwork and practical work, for any Anthropology honours degree, at FHEQ Level 6 (FQHEIS Level 10). Cite it as QAA (2024), Anthropology Subject Benchmark Statement, section 4, Subject-specific skills table, Anthropology (general), item 1, threshold column. Do not call it a regulatory requirement, a full curriculum or a master's standard. Set it beside its strong/excellent form qaa/anthropology-2024/ss.1.e, the FHEQ honours descriptor qaa/fheq-2024/4.15.b6 and Annex D's third-class row qaa/fheq-2024/annex-d/practical/r1/3rd (spine:6, strand:application)."
  author-agent-dialogue: "Raise it when a student asks what they must at least be able to do on designing and running fieldwork and practical work, or when a programme team checks a module against the threshold for any Anthropology honours degree. With a student, put it plainly in the second person; with staff, frame it as the minimum the course must evidence. Ask: 'Walk me through how you would plan a short piece of fieldwork, including its ethics and risks.' Do not read the table out at length or offer the strong/excellent column as the pass mark."
- statement: qaa/anthropology-2024/ss.2.e
  forPractitioner: { text: "Above threshold, and as the expectation for master's study (4.8), look for evidence that the student can evaluate those connections critically and explain clearly how each setting shapes the other.", rewrite: light, force: describes, status: drafted }
  forBeneficiary: { text: "To reach strong or excellent work, you would go further and evaluate those connections critically and explain clearly how each setting shapes the other.", rewrite: full, force: describes, status: drafted }
  author-agent-written: "Treat this as the strong or excellent form of item 2 on evaluating how social and biological contexts interact: a description of performance above the threshold for the honours degree at FHEQ Level 6, and what 4.8 expects of master's students at Level 7/11. Cite it as QAA (2024), Anthropology Subject Benchmark Statement, section 4, Subject-specific skills table, Anthropology (general), item 2, strong/excellent column. Do not present it as the pass standard or as a requirement for the award. Set it beside the threshold form qaa/anthropology-2024/ss.2.t, Annex D's upper rows qaa/fheq-2024/annex-d/cognitive/r1/2.1 and /1st and, for master's work, qaa/fheq-2024/4.17.b1."
  author-agent-dialogue: "Raise it when a student who has met the minimum on links between social and biological contexts asks how to do better, or when staff plan stretch tasks or master's study. Present it as a step above the threshold, never as the minimum: in plain words to a student and as a design aim to staff. Ask: 'In your example, how strong is the evidence for influence in each direction?' Avoid reading the issuer's wording aloud or implying that a student fails without it."
- statement: qaa/anthropology-2024/ss.2.t
  forPractitioner: { text: "Threshold: plan teaching and assessment so that every honours graduate shows they can understand how social and biological settings connect and shape each other.", rewrite: light, force: threshold, status: drafted }
  forBeneficiary: { text: "By the end of your honours degree you will, as a minimum, be able to understand how social and biological settings connect and shape each other.", rewrite: full, force: threshold, status: drafted }
  author-agent-written: "Treat this as a threshold standard: the least an honours graduate will have shown on links between social and biological contexts, for any Anthropology honours degree, at FHEQ Level 6 (FQHEIS Level 10). Cite it as QAA (2024), Anthropology Subject Benchmark Statement, section 4, Subject-specific skills table, Anthropology (general), item 2, threshold column. Do not call it a regulatory requirement, a full curriculum or a master's standard. Set it beside its strong/excellent form qaa/anthropology-2024/ss.2.e, the FHEQ honours descriptor qaa/fheq-2024/4.15.b7 and Annex D's third-class row qaa/fheq-2024/annex-d/cognitive/r1/3rd (spine:6, strand:thinking)."
  author-agent-dialogue: "Raise it when a student asks what they must at least be able to do on links between social and biological contexts, or when a programme team checks a module against the threshold for any Anthropology honours degree. With a student, put it plainly in the second person; with staff, frame it as the minimum the course must evidence. Ask: 'Can you give an example where a social setting changed something biological?' Do not read the table out at length or offer the strong/excellent column as the pass mark."
- statement: qaa/anthropology-2024/ss.3.e
  forPractitioner: { text: "Above threshold, and as the expectation for master's study (4.8), look for evidence that the student can synthesise information and data and draw well-argued readings from them in the light of what the subject currently knows and theorises.", rewrite: light, force: describes, status: drafted }
  forBeneficiary: { text: "To reach strong or excellent work, you would go further and synthesise information and data and draw well-argued readings from them in the light of what the subject currently knows and theorises.", rewrite: full, force: describes, status: drafted }
  author-agent-written: "Treat this as the strong or excellent form of item 3 on synthesising data into well-argued interpretations: a description of performance above the threshold for the honours degree at FHEQ Level 6, and what 4.8 expects of master's students at Level 7/11. Cite it as QAA (2024), Anthropology Subject Benchmark Statement, section 4, Subject-specific skills table, Anthropology (general), item 3, strong/excellent column. Do not present it as the pass standard or as a requirement for the award. Set it beside the threshold form qaa/anthropology-2024/ss.3.t, Annex D's upper rows qaa/fheq-2024/annex-d/cognitive/r2/2.1 and /1st and, for master's work, qaa/fheq-2024/4.17.b1."
  author-agent-dialogue: "Raise it when a student who has met the minimum on summarising and interpreting data asks how to do better, or when staff plan stretch tasks or master's study. Present it as a step above the threshold, never as the minimum: in plain words to a student and as a design aim to staff. Ask: 'How did you bring several sources together, and where does your interpretation go beyond them?' Avoid reading the issuer's wording aloud or implying that a student fails without it."
- statement: qaa/anthropology-2024/ss.3.t
  forPractitioner: { text: "Threshold: plan teaching and assessment so that every honours graduate shows they can summarise information and data and draw sensible readings from them in the light of what the subject currently knows and theorises.", rewrite: light, force: threshold, status: drafted }
  forBeneficiary: { text: "By the end of your honours degree you will, as a minimum, be able to summarise information and data and draw sensible readings from them in the light of what the subject currently knows and theorises.", rewrite: full, force: threshold, status: drafted }
  author-agent-written: "Treat this as a threshold standard: the least an honours graduate will have shown on summarising and interpreting data, for any Anthropology honours degree, at FHEQ Level 6 (FQHEIS Level 10). Cite it as QAA (2024), Anthropology Subject Benchmark Statement, section 4, Subject-specific skills table, Anthropology (general), item 3, threshold column. Do not call it a regulatory requirement, a full curriculum or a master's standard. Set it beside its strong/excellent form qaa/anthropology-2024/ss.3.e, the FHEQ honours descriptor qaa/fheq-2024/4.15.b3.1 and Annex D's third-class row qaa/fheq-2024/annex-d/cognitive/r2/3rd (spine:6, strand:thinking)."
  author-agent-dialogue: "Raise it when a student asks what they must at least be able to do on summarising and interpreting data, or when a programme team checks a module against the threshold for any Anthropology honours degree. With a student, put it plainly in the second person; with staff, frame it as the minimum the course must evidence. Ask: 'What did your data show, and what existing theory helped you read it?' Do not read the table out at length or offer the strong/excellent column as the pass mark."
- statement: qaa/anthropology-2024/ss.4.e
  forPractitioner: { text: "Above threshold, and as the expectation for master's study (4.8), look for evidence that the student can get anthropological ideas, principles and theories across clearly and fluently in different media, written, spoken, non-verbal and graphic, as suits the task.", rewrite: light, force: describes, status: drafted }
  forBeneficiary: { text: "To reach strong or excellent work, you would go further and get anthropological ideas, principles and theories across clearly and fluently in different media, written, spoken, non-verbal and graphic, as suits the task.", rewrite: full, force: describes, status: drafted }
  author-agent-written: "Treat this as the strong or excellent form of item 4 on communicating clearly and fluently in different media: a description of performance above the threshold for the honours degree at FHEQ Level 6, and what 4.8 expects of master's students at Level 7/11. Cite it as QAA (2024), Anthropology Subject Benchmark Statement, section 4, Subject-specific skills table, Anthropology (general), item 4, strong/excellent column. Do not present it as the pass standard or as a requirement for the award. Set it beside the threshold form qaa/anthropology-2024/ss.4.t, Annex D's upper rows qaa/fheq-2024/annex-d/transferable/r1/2.1 and /1st and, for master's work, qaa/fheq-2024/4.17.b1."
  author-agent-dialogue: "Raise it when a student who has met the minimum on communicating ideas in different media asks how to do better, or when staff plan stretch tasks or master's study. Present it as a step above the threshold, never as the minimum: in plain words to a student and as a design aim to staff. Ask: 'How would you adapt one argument for a poster, a talk and a short film?' Avoid reading the issuer's wording aloud or implying that a student fails without it."
- statement: qaa/anthropology-2024/ss.4.t
  forPractitioner: { text: "Threshold: plan teaching and assessment so that every honours graduate shows they can get anthropological ideas, principles and theories across in different media, written, spoken, non-verbal and graphic, as suits the task.", rewrite: light, force: threshold, status: drafted }
  forBeneficiary: { text: "By the end of your honours degree you will, as a minimum, be able to get anthropological ideas, principles and theories across in different media, written, spoken, non-verbal and graphic, as suits the task.", rewrite: full, force: threshold, status: drafted }
  author-agent-written: "Treat this as a threshold standard: the least an honours graduate will have shown on communicating ideas in different media, for any Anthropology honours degree, at FHEQ Level 6 (FQHEIS Level 10). Cite it as QAA (2024), Anthropology Subject Benchmark Statement, section 4, Subject-specific skills table, Anthropology (general), item 4, threshold column. Do not call it a regulatory requirement, a full curriculum or a master's standard. Set it beside its strong/excellent form qaa/anthropology-2024/ss.4.e, the FHEQ honours descriptor qaa/fheq-2024/4.15.b8 and Annex D's third-class row qaa/fheq-2024/annex-d/transferable/r1/3rd (spine:6, strand:communication)."
  author-agent-dialogue: "Raise it when a student asks what they must at least be able to do on communicating ideas in different media, or when a programme team checks a module against the threshold for any Anthropology honours degree. With a student, put it plainly in the second person; with staff, frame it as the minimum the course must evidence. Ask: 'In which media have you presented your ideas, and which felt hardest?' Do not read the table out at length or offer the strong/excellent column as the pass mark."
- statement: qaa/anthropology-2024/ss.5.e
  forPractitioner: { text: "Above threshold, and as the expectation for master's study (4.8), look for evidence that the student can frame, investigate and discuss questions shaped by anthropology, using the subject's main theories and concepts and judging their strengths and limits critically.", rewrite: light, force: describes, status: drafted }
  forBeneficiary: { text: "To reach strong or excellent work, you would go further and frame, investigate and discuss questions shaped by anthropology, using the subject's main theories and concepts and judging their strengths and limits critically.", rewrite: full, force: describes, status: drafted }
  author-agent-written: "Treat this as the strong or excellent form of item 5 on framing questions and assessing theory critically: a description of performance above the threshold for the honours degree at FHEQ Level 6, and what 4.8 expects of master's students at Level 7/11. Cite it as QAA (2024), Anthropology Subject Benchmark Statement, section 4, Subject-specific skills table, Anthropology (general), item 5, strong/excellent column. Do not present it as the pass standard or as a requirement for the award. Set it beside the threshold form qaa/anthropology-2024/ss.5.t, Annex D's upper rows qaa/fheq-2024/annex-d/cognitive/r2/2.1 and /1st and, for master's work, qaa/fheq-2024/4.17.b1."
  author-agent-dialogue: "Raise it when a student who has met the minimum on investigating questions with theory asks how to do better, or when staff plan stretch tasks or master's study. Present it as a step above the threshold, never as the minimum: in plain words to a student and as a design aim to staff. Ask: 'If you framed that question again, which theory would you test it against, and why?' Avoid reading the issuer's wording aloud or implying that a student fails without it."
- statement: qaa/anthropology-2024/ss.5.t
  forPractitioner: { text: "Threshold: plan teaching and assessment so that every honours graduate shows they can investigate and discuss questions shaped by anthropology, using the subject's main theories and concepts and naming what they do well and badly.", rewrite: light, force: threshold, status: drafted }
  forBeneficiary: { text: "By the end of your honours degree you will, as a minimum, be able to investigate and discuss questions shaped by anthropology, using the subject's main theories and concepts and naming what they do well and badly.", rewrite: full, force: threshold, status: drafted }
  author-agent-written: "Treat this as a threshold standard: the least an honours graduate will have shown on investigating questions with theory, for any Anthropology honours degree, at FHEQ Level 6 (FQHEIS Level 10). Cite it as QAA (2024), Anthropology Subject Benchmark Statement, section 4, Subject-specific skills table, Anthropology (general), item 5, threshold column. Do not call it a regulatory requirement, a full curriculum or a master's standard. Set it beside its strong/excellent form qaa/anthropology-2024/ss.5.e, the FHEQ honours descriptor qaa/fheq-2024/4.15.b7 and Annex D's third-class row qaa/fheq-2024/annex-d/cognitive/r2/3rd (spine:6, strand:thinking)."
  author-agent-dialogue: "Raise it when a student asks what they must at least be able to do on investigating questions with theory, or when a programme team checks a module against the threshold for any Anthropology honours degree. With a student, put it plainly in the second person; with staff, frame it as the minimum the course must evidence. Ask: 'What question have you investigated, and which concept helped most?' Do not read the table out at length or offer the strong/excellent column as the pass mark."
- statement: qaa/anthropology-2024/ss.6.e
  forPractitioner: { text: "Above threshold, and as the expectation for master's study (4.8), look for evidence that the student can engage meaningfully with cultures, populations and groups unlike their own while keeping a personal judgement, aware of cultural assumptions, their own included, and of how they affect the reading of others.", rewrite: light, force: describes, status: drafted }
  forBeneficiary: { text: "To reach strong or excellent work, you would go further and engage meaningfully with cultures, populations and groups unlike your own while keeping a personal judgement, aware of cultural assumptions, your own included, and of how they affect the reading of others.", rewrite: full, force: describes, status: drafted }
  author-agent-written: "Treat this as the strong or excellent form of item 6 on engaging meaningfully with other cultures: a description of performance above the threshold for the honours degree at FHEQ Level 6, and what 4.8 expects of master's students at Level 7/11. Cite it as QAA (2024), Anthropology Subject Benchmark Statement, section 4, Subject-specific skills table, Anthropology (general), item 6, strong/excellent column. Do not present it as the pass standard or as a requirement for the award. Set it beside the threshold form qaa/anthropology-2024/ss.6.t, Annex D's upper rows qaa/fheq-2024/annex-d/summary/r3/2.1 and /1st and, for master's work, qaa/fheq-2024/4.17.b1."
  author-agent-dialogue: "Raise it when a student who has met the minimum on approaches to engaging with other cultures asks how to do better, or when staff plan stretch tasks or master's study. Present it as a step above the threshold, never as the minimum: in plain words to a student and as a design aim to staff. Ask: 'When did one of your own assumptions change how you read someone else, and what did you do about it?' Avoid reading the issuer's wording aloud or implying that a student fails without it."
- statement: qaa/anthropology-2024/ss.6.t
  forPractitioner: { text: "Threshold: plan teaching and assessment so that every honours graduate shows they can understand the main ways of engaging with cultures, populations and groups unlike their own, and how cultural assumptions can colour what is made of that engagement.", rewrite: light, force: threshold, status: drafted }
  forBeneficiary: { text: "By the end of your honours degree you will, as a minimum, be able to understand the main ways of engaging with cultures, populations and groups unlike your own, and how cultural assumptions can colour what is made of that engagement.", rewrite: full, force: threshold, status: drafted }
  author-agent-written: "Treat this as a threshold standard: the least an honours graduate will have shown on approaches to engaging with other cultures, for any Anthropology honours degree, at FHEQ Level 6 (FQHEIS Level 10). Cite it as QAA (2024), Anthropology Subject Benchmark Statement, section 4, Subject-specific skills table, Anthropology (general), item 6, threshold column. Do not call it a regulatory requirement, a full curriculum or a master's standard. Set it beside its strong/excellent form qaa/anthropology-2024/ss.6.e, the FHEQ honours descriptor qaa/fheq-2024/4.15.b4 and Annex D's third-class row qaa/fheq-2024/annex-d/summary/r3/3rd (spine:6, strand:thinking)."
  author-agent-dialogue: "Raise it when a student asks what they must at least be able to do on approaches to engaging with other cultures, or when a programme team checks a module against the threshold for any Anthropology honours degree. With a student, put it plainly in the second person; with staff, frame it as the minimum the course must evidence. Ask: 'How would you prepare to work with a group whose ways differ from yours?' Do not read the table out at length or offer the strong/excellent column as the pass mark."
- statement: qaa/anthropology-2024/ss.7.e
  forPractitioner: { text: "Above threshold, and as the expectation for master's study (4.8), look for evidence that the student can do all that and also combine many such sources into fresh responses and interpretations in a range of media.", rewrite: light, force: describes, status: drafted }
  forBeneficiary: { text: "To reach strong or excellent work, you would go further and do all that and also combine many such sources into fresh responses and interpretations in a range of media.", rewrite: full, force: describes, status: drafted }
  author-agent-written: "Treat this as the strong or excellent form of item 7 on combining sources into new interpretations: a description of performance above the threshold for the honours degree at FHEQ Level 6, and what 4.8 expects of master's students at Level 7/11. Cite it as QAA (2024), Anthropology Subject Benchmark Statement, section 4, Subject-specific skills table, Anthropology (general), item 7, strong/excellent column. Do not present it as the pass standard or as a requirement for the award. Set it beside the threshold form qaa/anthropology-2024/ss.7.t, Annex D's upper rows qaa/fheq-2024/annex-d/cognitive/r1/2.1 and /1st and, for master's work, qaa/fheq-2024/4.17.b1."
  author-agent-dialogue: "Raise it when a student who has met the minimum on reading sources in context asks how to do better, or when staff plan stretch tasks or master's study. Present it as a step above the threshold, never as the minimum: in plain words to a student and as a design aim to staff. Ask: 'How could you combine a film, an archive and an interview into a new interpretation?' Avoid reading the issuer's wording aloud or implying that a student fails without it."
- statement: qaa/anthropology-2024/ss.7.t
  forPractitioner: { text: "Threshold: plan teaching and assessment so that every honours graduate shows they can read and interpret sources of many kinds, print, oral, film and multimedia, critically and in their historical, social, cultural and theoretical settings, knowing in practice what each type and each source can and cannot offer.", rewrite: light, force: threshold, status: drafted }
  forBeneficiary: { text: "By the end of your honours degree you will, as a minimum, be able to read and interpret sources of many kinds, print, oral, film and multimedia, critically and in their historical, social, cultural and theoretical settings, knowing in practice what each type and each source can and cannot offer.", rewrite: full, force: threshold, status: drafted }
  author-agent-written: "Treat this as a threshold standard: the least an honours graduate will have shown on reading sources in context, for any Anthropology honours degree, at FHEQ Level 6 (FQHEIS Level 10). Cite it as QAA (2024), Anthropology Subject Benchmark Statement, section 4, Subject-specific skills table, Anthropology (general), item 7, threshold column. Do not call it a regulatory requirement, a full curriculum or a master's standard. Set it beside its strong/excellent form qaa/anthropology-2024/ss.7.e, the FHEQ honours descriptor qaa/fheq-2024/4.15.b5 and Annex D's third-class row qaa/fheq-2024/annex-d/cognitive/r1/3rd (spine:6, strand:thinking)."
  author-agent-dialogue: "Raise it when a student asks what they must at least be able to do on reading sources in context, or when a programme team checks a module against the threshold for any Anthropology honours degree. With a student, put it plainly in the second person; with staff, frame it as the minimum the course must evidence. Ask: 'Take one source you used: what context do you need to read it well?' Do not read the table out at length or offer the strong/excellent column as the pass mark."
- statement: qaa/anthropology-2024/ss.8.e
  forPractitioner: { text: "Above threshold, and as the expectation for master's study (4.8), look for evidence that the student can recognise and evaluate uses of anthropological knowledge in settings from personal life to international policy, and design new ones.", rewrite: light, force: describes, status: drafted }
  forBeneficiary: { text: "To reach strong or excellent work, you would go further and recognise and evaluate uses of anthropological knowledge in settings from personal life to international policy, and design new ones.", rewrite: full, force: describes, status: drafted }
  author-agent-written: "Treat this as the strong or excellent form of item 8 on evaluating and designing applications: a description of performance above the threshold for the honours degree at FHEQ Level 6, and what 4.8 expects of master's students at Level 7/11. Cite it as QAA (2024), Anthropology Subject Benchmark Statement, section 4, Subject-specific skills table, Anthropology (general), item 8, strong/excellent column. Do not present it as the pass standard or as a requirement for the award. Set it beside the threshold form qaa/anthropology-2024/ss.8.t, Annex D's upper rows qaa/fheq-2024/annex-d/cognitive/r3/2.1 and /1st and, for master's work, qaa/fheq-2024/4.17.b1."
  author-agent-dialogue: "Raise it when a student who has met the minimum on applying knowledge from personal life to policy asks how to do better, or when staff plan stretch tasks or master's study. Present it as a step above the threshold, never as the minimum: in plain words to a student and as a design aim to staff. Ask: 'What new use of anthropology would you propose for a policy problem you care about?' Avoid reading the issuer's wording aloud or implying that a student fails without it."
- statement: qaa/anthropology-2024/ss.8.t
  forPractitioner: { text: "Threshold: plan teaching and assessment so that every honours graduate shows they can recognise how anthropological knowledge can be used in settings that range from personal life to international policy.", rewrite: light, force: threshold, status: drafted }
  forBeneficiary: { text: "By the end of your honours degree you will, as a minimum, be able to recognise how anthropological knowledge can be used in settings that range from personal life to international policy.", rewrite: full, force: threshold, status: drafted }
  author-agent-written: "Treat this as a threshold standard: the least an honours graduate will have shown on applying knowledge from personal life to policy, for any Anthropology honours degree, at FHEQ Level 6 (FQHEIS Level 10). Cite it as QAA (2024), Anthropology Subject Benchmark Statement, section 4, Subject-specific skills table, Anthropology (general), item 8, threshold column. Do not call it a regulatory requirement, a full curriculum or a master's standard. Set it beside its strong/excellent form qaa/anthropology-2024/ss.8.e, the FHEQ honours descriptor qaa/fheq-2024/4.15.b6 and Annex D's third-class row qaa/fheq-2024/annex-d/cognitive/r3/3rd (spine:6, strand:application)."
  author-agent-dialogue: "Raise it when a student asks what they must at least be able to do on applying knowledge from personal life to policy, or when a programme team checks a module against the threshold for any Anthropology honours degree. With a student, put it plainly in the second person; with staff, frame it as the minimum the course must evidence. Ask: 'Where have you seen anthropology used, from someone's own life up to policy?' Do not read the table out at length or offer the strong/excellent column as the pass mark."
- statement: qaa/anthropology-2024/ss.9.e
  forPractitioner: { text: "Above threshold, and as the expectation for master's study (4.8), look for evidence that the student can recognise and analyse critically the politics of language, indirect communication and theoretical claims, and the workings of power and claims to authority.", rewrite: light, force: describes, status: drafted }
  forBeneficiary: { text: "To reach strong or excellent work, you would go further and recognise and analyse critically the politics of language, indirect communication and theoretical claims, and the workings of power and claims to authority.", rewrite: full, force: describes, status: drafted }
  author-agent-written: "Treat this as the strong or excellent form of item 9 on analysing the politics of language and authority: a description of performance above the threshold for the honours degree at FHEQ Level 6, and what 4.8 expects of master's students at Level 7/11. Cite it as QAA (2024), Anthropology Subject Benchmark Statement, section 4, Subject-specific skills table, Anthropology (general), item 9, strong/excellent column. Do not present it as the pass standard or as a requirement for the award. Set it beside the threshold form qaa/anthropology-2024/ss.9.t, Annex D's upper rows qaa/fheq-2024/annex-d/cognitive/r1/2.1 and /1st and, for master's work, qaa/fheq-2024/4.17.b1."
  author-agent-dialogue: "Raise it when a student who has met the minimum on the politics of language and claims to authority asks how to do better, or when staff plan stretch tasks or master's study. Present it as a step above the threshold, never as the minimum: in plain words to a student and as a design aim to staff. Ask: 'How would you analyse the way power works through the language of one policy or theory?' Avoid reading the issuer's wording aloud or implying that a student fails without it."
- statement: qaa/anthropology-2024/ss.9.t
  forPractitioner: { text: "Threshold: plan teaching and assessment so that every honours graduate shows they can recognise the politics of language, indirect communication and theoretical claims, and the workings of power and claims to authority.", rewrite: light, force: threshold, status: drafted }
  forBeneficiary: { text: "By the end of your honours degree you will, as a minimum, be able to recognise the politics of language, indirect communication and theoretical claims, and the workings of power and claims to authority.", rewrite: full, force: threshold, status: drafted }
  author-agent-written: "Treat this as a threshold standard: the least an honours graduate will have shown on the politics of language and claims to authority, for any Anthropology honours degree, at FHEQ Level 6 (FQHEIS Level 10). Cite it as QAA (2024), Anthropology Subject Benchmark Statement, section 4, Subject-specific skills table, Anthropology (general), item 9, threshold column. Do not call it a regulatory requirement, a full curriculum or a master's standard. Set it beside its strong/excellent form qaa/anthropology-2024/ss.9.e, the FHEQ honours descriptor qaa/fheq-2024/4.15.b7 and Annex D's third-class row qaa/fheq-2024/annex-d/cognitive/r1/3rd (spine:6, strand:thinking)."
  author-agent-dialogue: "Raise it when a student asks what they must at least be able to do on the politics of language and claims to authority, or when a programme team checks a module against the threshold for any Anthropology honours degree. With a student, put it plainly in the second person; with staff, frame it as the minimum the course must evidence. Ask: 'In a text you read, who was claiming authority and how could you tell?' Do not read the table out at length or offer the strong/excellent column as the pass mark."
- statement: qaa/anthropology-2024/ss.10.e
  forPractitioner: { text: "Above threshold, and as the expectation for master's study (4.8), look for evidence that the student can engage meaningfully with cultures, populations and groups unlike their own while keeping a personal judgement, aware of cultural assumptions, their own included, and show that they know how those assumptions affect the reading of others.", rewrite: light, force: describes, status: drafted }
  forBeneficiary: { text: "To reach strong or excellent work, you would go further and engage meaningfully with cultures, populations and groups unlike your own while keeping a personal judgement, aware of cultural assumptions, your own included, and show that they know how those assumptions affect the reading of others.", rewrite: full, force: describes, status: drafted }
  author-agent-written: "Treat this as the strong or excellent form of item 10 on meaningful engagement with other cultures: a description of performance above the threshold for the honours degree at FHEQ Level 6, and what 4.8 expects of master's students at Level 7/11. Cite it as QAA (2024), Anthropology Subject Benchmark Statement, section 4, Subject-specific skills table, Social Anthropology (specific), item 10, strong/excellent column. Do not present it as the pass standard or as a requirement for the award. Set it beside the threshold form qaa/anthropology-2024/ss.10.t, Annex D's upper rows qaa/fheq-2024/annex-d/summary/r3/2.1 and /1st and, for master's work, qaa/fheq-2024/4.17.b1."
  author-agent-dialogue: "Raise it when a student who has met the minimum on engaging with other cultures with self-awareness asks how to do better, or when staff plan stretch tasks or master's study. Present it as a step above the threshold, never as the minimum: in plain words to a student and as a design aim to staff. Ask: 'How did you make that engagement meaningful for the people involved, not only for your study?' Avoid reading the issuer's wording aloud or implying that a student fails without it."
- statement: qaa/anthropology-2024/ss.10.t
  forPractitioner: { text: "Threshold: plan teaching and assessment so that every honours graduate on a degree mainly in Social Anthropology shows they can engage with cultures, populations and groups unlike their own while keeping a personal judgement, aware of cultural assumptions, their own included, and show that they know how those assumptions affect the reading of others.", rewrite: light, force: threshold, status: drafted }
  forBeneficiary: { text: "By the end of your honours degree you will, as a minimum, be able to engage with cultures, populations and groups unlike your own while keeping a personal judgement, aware of cultural assumptions, your own included, and show that they know how those assumptions affect the reading of others.", rewrite: full, force: threshold, status: drafted }
  author-agent-written: "Treat this as a threshold standard: the least an honours graduate will have shown on engaging with other cultures with self-awareness, for degrees mainly in Social Anthropology (4.6), at FHEQ Level 6 (FQHEIS Level 10). Cite it as QAA (2024), Anthropology Subject Benchmark Statement, section 4, Subject-specific skills table, Social Anthropology (specific), item 10, threshold column. Do not call it a regulatory requirement, a full curriculum or a master's standard. Set it beside its strong/excellent form qaa/anthropology-2024/ss.10.e, the FHEQ honours descriptor qaa/fheq-2024/4.15.b4 and Annex D's third-class row qaa/fheq-2024/annex-d/summary/r3/3rd (spine:6, strand:thinking)."
  author-agent-dialogue: "Raise it when a student asks what they must at least be able to do on engaging with other cultures with self-awareness, or when a programme team checks a module against the threshold for degrees mainly in Social Anthropology (4.6). With a student, put it plainly in the second person; with staff, frame it as the minimum the course must evidence. Ask: 'What did you notice about your own assumptions during fieldwork or group work?' Do not read the table out at length or offer the strong/excellent column as the pass mark."
- statement: qaa/anthropology-2024/ss.11.e
  forPractitioner: { text: "Above threshold, and as the expectation for master's study (4.8), look for evidence that the student can evaluate critically and choose the right techniques for recording and measuring physical variation in humans, hominins or primates to suit a given research question.", rewrite: light, force: describes, status: drafted }
  forBeneficiary: { text: "To reach strong or excellent work, you would go further and evaluate critically and choose the right techniques for recording and measuring physical variation in humans, hominins or primates to suit a given research question.", rewrite: full, force: describes, status: drafted }
  author-agent-written: "Treat this as the strong or excellent form of item 11 on choosing techniques for research questions: a description of performance above the threshold for the honours degree at FHEQ Level 6, and what 4.8 expects of master's students at Level 7/11. Cite it as QAA (2024), Anthropology Subject Benchmark Statement, section 4, Subject-specific skills table, Biological Anthropology (specific), item 11, strong/excellent column. Do not present it as the pass standard or as a requirement for the award. Set it beside the threshold form qaa/anthropology-2024/ss.11.t, Annex D's upper rows qaa/fheq-2024/annex-d/practical/r1/2.1 and /1st and, for master's work, qaa/fheq-2024/4.17.b1."
  author-agent-dialogue: "Raise it when a student who has met the minimum on techniques for measuring physical variability asks how to do better, or when staff plan stretch tasks or master's study. Present it as a step above the threshold, never as the minimum: in plain words to a student and as a design aim to staff. Ask: 'For your research question, which technique would you choose, and why not the others?' Avoid reading the issuer's wording aloud or implying that a student fails without it."
- statement: qaa/anthropology-2024/ss.11.t
  forPractitioner: { text: "Threshold: plan teaching and assessment so that every honours graduate on a degree mainly in Biological Anthropology shows they can know the range of techniques for recording and measuring physical variation in humans, hominins or primates, with the main strengths and limits of each.", rewrite: light, force: threshold, status: drafted }
  forBeneficiary: { text: "By the end of your honours degree you will, as a minimum, be able to know the range of techniques for recording and measuring physical variation in humans, hominins or primates, with the main strengths and limits of each.", rewrite: full, force: threshold, status: drafted }
  author-agent-written: "Treat this as a threshold standard: the least an honours graduate will have shown on techniques for measuring physical variability, for degrees mainly in Biological Anthropology (4.6), at FHEQ Level 6 (FQHEIS Level 10). Cite it as QAA (2024), Anthropology Subject Benchmark Statement, section 4, Subject-specific skills table, Biological Anthropology (specific), item 11, threshold column. Do not call it a regulatory requirement, a full curriculum or a master's standard. Set it beside its strong/excellent form qaa/anthropology-2024/ss.11.e, the FHEQ honours descriptor qaa/fheq-2024/4.15.b2 and Annex D's third-class row qaa/fheq-2024/annex-d/practical/r1/3rd (spine:6, strand:application)."
  author-agent-dialogue: "Raise it when a student asks what they must at least be able to do on techniques for measuring physical variability, or when a programme team checks a module against the threshold for degrees mainly in Biological Anthropology (4.6). With a student, put it plainly in the second person; with staff, frame it as the minimum the course must evidence. Ask: 'Which measurement techniques do you know, and what does each get wrong?' Do not read the table out at length or offer the strong/excellent column as the pass mark."
- statement: qaa/anthropology-2024/ss.12.e
  forPractitioner: { text: "Above threshold, and as the expectation for master's study (4.8), look for evidence that the student can appreciate those ethical questions, including work with primates and hominins other than humans, and design and apply strict ethical standards at every stage of research.", rewrite: light, force: describes, status: drafted }
  forBeneficiary: { text: "To reach strong or excellent work, you would go further and appreciate those ethical questions, including work with primates and hominins other than humans, and design and apply strict ethical standards at every stage of research.", rewrite: full, force: describes, status: drafted }
  author-agent-written: "Treat this as the strong or excellent form of item 12 on designing and applying strict ethical standards: a description of performance above the threshold for the honours degree at FHEQ Level 6, and what 4.8 expects of master's students at Level 7/11. Cite it as QAA (2024), Anthropology Subject Benchmark Statement, section 4, Subject-specific skills table, Biological Anthropology (specific), item 12, strong/excellent column. Do not present it as the pass standard or as a requirement for the award. Set it beside the threshold form qaa/anthropology-2024/ss.12.t, Annex D's upper rows qaa/fheq-2024/annex-d/cognitive/r1/2.1 and /1st and, for master's work, qaa/fheq-2024/4.17.b1."
  author-agent-dialogue: "Raise it when a student who has met the minimum on ethical issues and conduct in research asks how to do better, or when staff plan stretch tasks or master's study. Present it as a step above the threshold, never as the minimum: in plain words to a student and as a design aim to staff. Ask: 'How would you build ethical checks into each stage of a project, not only at the start?' Avoid reading the issuer's wording aloud or implying that a student fails without it."
- statement: qaa/anthropology-2024/ss.12.t
  forPractitioner: { text: "Threshold: plan teaching and assessment so that every honours graduate on a degree mainly in Biological Anthropology shows they can show awareness of the ethical questions raised by different methods and theories, including work with non-human primates, handling human remains and claims about the evolutionary roots of human behaviour, and keep to strict ethical standards in study and research.", rewrite: light, force: threshold, status: drafted }
  forBeneficiary: { text: "By the end of your honours degree you will, as a minimum, be able to show awareness of the ethical questions raised by different methods and theories, including work with non-human primates, handling human remains and claims about the evolutionary roots of human behaviour, and keep to strict ethical standards in study and research.", rewrite: full, force: threshold, status: drafted }
  author-agent-written: "Treat this as a threshold standard: the least an honours graduate will have shown on ethical issues and conduct in research, for degrees mainly in Biological Anthropology (4.6), at FHEQ Level 6 (FQHEIS Level 10). Cite it as QAA (2024), Anthropology Subject Benchmark Statement, section 4, Subject-specific skills table, Biological Anthropology (specific), item 12, threshold column. Do not call it a regulatory requirement, a full curriculum or a master's standard. Set it beside its strong/excellent form qaa/anthropology-2024/ss.12.e, the FHEQ honours descriptor qaa/fheq-2024/4.15.b9.2 and Annex D's third-class row qaa/fheq-2024/annex-d/cognitive/r1/3rd (spine:6, strand:thinking)."
  author-agent-dialogue: "Raise it when a student asks what they must at least be able to do on ethical issues and conduct in research, or when a programme team checks a module against the threshold for degrees mainly in Biological Anthropology (4.6). With a student, put it plainly in the second person; with staff, frame it as the minimum the course must evidence. Ask: 'What ethical questions would handling human remains raise in your project?' Do not read the table out at length or offer the strong/excellent column as the pass mark."
```

### S5 Levels and alignment
<!-- label: both; status: drafted; basis: primary -->
```yaml
levels:
  - { id: "fheq:6", role: "cites", locator: "D1, 2.11" }
  - { id: "fqheis:10", role: "cites", locator: "D1, 2.11" }
  - { id: "fheq:7", role: "cites", locator: "D1, 2.13; 4.7 (\"Level 7/11\")" }
  - { id: "fqheis:11", role: "cites", locator: "D1, 2.13; 4.7 (\"Level 7/11\")" }
crosswalks:
  - { from: "fheq:6", to: "fqheis:10", relation: "equivalent", basis: "stated (D1, 2.11: \"FHEQ Level 6; FQHEIS Level 10\" for the honours degree); matches std:doc:qaa-fheq-2024-framework Table 1" }
  - { from: "fheq:7", to: "fqheis:11", relation: "equivalent", basis: "stated (D1, 2.13 for integrated master's; 4.7 'Level 7/11'); matches std:doc:qaa-fheq-2024-framework S5 (shared descriptor 4.17)" }
```

### S6 Themes
<!-- label: both; status: drafted; basis: primary -->
```yaml
- { id: "theme:edi", role: "carries", carriedIn: ["1.3", "1.4", "1.8", "1.9", "1.10", "3.18", "3.23"] }
- { id: "theme:accessibility", role: "carries", carriedIn: ["1.11", "1.12", "1.13", "3.18"] }
- { id: "theme:esd", role: "carries", carriedIn: ["1.14", "1.15", "1.24", "3.5"] }
- { id: "theme:enterprise", role: "carries", carriedIn: ["1.16", "1.17", "1.18", "1.19", "1.20", "1.21", "1.22", "2.15"] }
```

### S7 Relations
<!-- label: both; status: drafted; basis: primary -->
```yaml
- { rel: "partOf", target: "collection: QAA Subject Benchmark Statements", note: "one of 54 held by stan" }
- { rel: "supersedes", target: "std:doc:qaa-anthropology-2019-benchmarks (not ingested)", note: "the advisory group pages name the fourth edition of 2019; the closing line names this the fifth edition (D1, section 6)" }
- { rel: "refersTo", target: "std:doc:qaa-fheq-2024-framework, Annex D", note: "the four honours classifications, for achievement above threshold (D1, 4.2)" }
- { rel: "refersTo", target: "std:doc:qaa-fheq-2024-framework", note: "FHEQ Levels 6 and 7 (D1, 2.11, 2.13)" }
- { rel: "refersTo", target: "std:doc:qaa-fqheis-2024-framework", note: "FQHEIS Levels 10 and 11 (D1, 2.11, 2.13)" }
- { rel: "refersTo", target: "std:doc:qaa-advancehe-esd-2021-guidance", note: "\"QAA and Advance HE ESD\", the source of the competencies in 1.15" }
- { rel: "refersTo", target: "QAA Quality Code, Advice and Guidance (not ingested)", note: "front matter" }
- { rel: "refersTo", target: "Association of Social Anthropologists and BABAO codes of practice (not ingested)", note: "D1, 1.15" }
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
- The study of what it is to be human, past and present, from the microscopic to the global, drawing on many disciplines and on students' own lived experience (D1, 2.1, 1.5).
- Its outlook is global and comparative, avoids ranking cultural practices and holds that knowledge is situated, so many perspectives must be heard (D1, 1.3, 1.4).
- Two main branches, Social and Biological Anthropology, with Anthropology in practice and Ethics as organising themes; courses may be general or focus on one sub-field (D1, 2.2 to 2.6).
- Intensely practical: it is learned by doing, through fieldwork, laboratory work and research projects from the start of study (D1, 1.6, 1.21, 1.23 to 1.25, 2.7, 2.8).
- Ethics and reflexivity are central: privilege in studying humans and primates, power imbalances with communities and students' own biases (D1, 1.26, 2.9, 3.4).
- Self-critical about its colonial origins and committed to decolonial work and to voices beyond the global North (D1, 1.8, 1.10, 3.3, 3.9).
- It studies dynamic relationships among people, primates, hominins, things, bodies, environments and infrastructures (D1, 1.7, 3.5).

### SB2 Themes in this subject
<!-- label: both; status: drafted; basis: primary -->
```yaml
- theme: theme:edi
  inThisSubject: "the discipline faces its colonial history and the structures of power behind inequality, names agenda items (binary frameworks for sex, patriarchy, intersectionality) and calls for decolonial work; inclusion and fair assessment recur in pedagogy (D1, 1.3, 1.4, 1.8 to 1.10, 3.18, 3.23)"
  statements: ["qaa/anthropology-2024/3.23"]
- theme: theme:accessibility
  inThisSubject: "headed Accessibility and flexibility: routes for non-traditional, disabled and neurodivergent students, blended and multimodal learning, varied assessment and flexible modes of study; reasonable adjustments in teaching (D1, 1.11 to 1.13, 3.18)"
  statements: ["qaa/anthropology-2024/1.11"]
- theme: theme:esd
  inThisSubject: "headed Sustainability: what ESD secures for students and six competencies the subject builds (reflexivity, systems thinking, anticipation, strategy, collaboration, self-awareness), keyed to SDG numbers; human-environment relations as a major focus (D1, 1.14, 1.15, 1.24, 3.5)"
  statements: ["qaa/anthropology-2024/3.5"]
- theme: theme:enterprise
  inThisSubject: "headed Enterprise and Entrepreneurship Education: careers, social innovation, research projects from the start and transferable skills; community partnerships build employability (D1, 1.16 to 1.22, 2.15)"
  statements: ["qaa/anthropology-2024/1.21", "qaa/anthropology-2024/2.15"]
```

### SB3 Content and delivery
<!-- label: both; status: drafted; basis: primary -->
```yaml
areas:
  - { component: "2.3", gloss: "Social Anthropology: social theory, neighbouring disciplines and sub-fields" }
  - { component: "2.6", gloss: "Biological Anthropology: evolutionary theory, STEM links and sub-fields such as forensic anthropology and primatology" }
  - { component: "3.2", gloss: "history of the discipline, both branches" }
  - { component: "3.3", gloss: "colonialism and decolonising" }
  - { component: "3.5", gloss: "humans, other species and environments" }
  - { component: "3.6", gloss: "theoretical approaches to interpreting data" }
  - { component: "3.7", gloss: "other typical themes: identity, kinship, gender, power, exchange, material culture, health, technology, art" }
  - { component: "3.10", gloss: "Biological Anthropology core: biology and skeletal biology, pathology, lifeways, forensics, evolution, fossils, origins research, molecular methods" }
  - { component: "3.11", gloss: "Social Anthropology core: body and gender, relatedness, exchange, politics, language, digital worlds, environment, subsistence, belief" }
  - { component: "3.12", gloss: "further optional subjects, from art and ritual to artificial intelligence and tourism" }
practices:
  - { component: "3.13", kind: "learning", gloss: "learning fieldwork and designing an own fieldwork project" }
  - { component: "3.14", kind: "teaching", gloss: "hands-on, interactive research and professional practice" }
  - { component: "3.17", kind: "learning", gloss: "placements and practical research projects" }
  - { component: "3.19", kind: "teaching", gloss: "lectures, seminars, group work, problem-solving, laboratory and field sessions" }
  - { component: "3.20", kind: "learning", gloss: "self-directed and online study, volunteering, placements, exchanges" }
  - { component: "3.22", kind: "assessment", gloss: "formative assessment, feedback and feedforward" }
  - { component: "3.24", kind: "assessment", gloss: "diverse styles; marking group work" }
  - { component: "3.26", kind: "assessment", gloss: "dissertation or extended project" }
  - { component: "3.27", kind: "assessment", gloss: "policy documents, press releases, briefings, technical reports" }
  - { component: "3.28", kind: "assessment", gloss: "writing for many audiences" }
  - { component: "3.29", kind: "assessment", gloss: "exams and unseen tests" }
  - { component: "3.30", kind: "assessment", gloss: "field and laboratory notebooks, observation, portfolios" }
  - { component: "3.31", kind: "assessment", gloss: "creative and multimodal outputs" }
```

### SB4 Benchmark standards
<!-- label: both; status: drafted; basis: primary -->
```yaml
rungs:
  - { rung: "threshold", named: "Threshold", leadIn: "4.4", award: "bachelor's with honours", items: 45 }
  - { rung: "typical", leadIn: "none", award: "bachelor's with honours", items: 0 }
  - { rung: "excellent", named: "Strong/excellent", leadIn: "4.4", award: "bachelor's with honours", items: 45 }
rungBases: "4.1: the threshold is the minimum for the honours degree; 4.2: most students do significantly better, judged by each provider with Annex D; 4.4: the tables state outcomes at the end of the honours degree, in broad terms; 4.5: they mix baseline skills every graduate has with further skills, without marking which are which; 4.6: the Social and Biological rows apply to degrees mainly in that branch; 4.8: master's students are expected to master the strong/excellent column"
outcomeLists: []
outcomes:
  - { outcome: "human diversity", threshold: "qaa/anthropology-2024/ku.1.t", typical: "none", excellent: "qaa/anthropology-2024/ku.1.e", basis: "stated", domain: "knowledge", award: "bachelor's with honours" }
  - { outcome: "history of the discipline", threshold: "qaa/anthropology-2024/ku.2.t", typical: "none", excellent: "qaa/anthropology-2024/ku.2.e", basis: "stated", domain: "knowledge", award: "bachelor's with honours" }
  - { outcome: "key themes and debates", threshold: "qaa/anthropology-2024/ku.3.t", typical: "none", excellent: "qaa/anthropology-2024/ku.3.e", basis: "stated", domain: "knowledge", award: "bachelor's with honours" }
  - { outcome: "cultural assumptions and relativism", threshold: "qaa/anthropology-2024/ku.4.t", typical: "none", excellent: "qaa/anthropology-2024/ku.4.e", basis: "stated", domain: "understanding", award: "bachelor's with honours" }
  - { outcome: "applying anthropological knowledge", threshold: "qaa/anthropology-2024/ku.5.t", typical: "none", excellent: "qaa/anthropology-2024/ku.5.e", basis: "stated", domain: "understanding", award: "bachelor's with honours" }
  - { outcome: "forms of material and data", threshold: "qaa/anthropology-2024/ku.6.t", typical: "none", excellent: "qaa/anthropology-2024/ku.6.e", basis: "stated", domain: "understanding", award: "bachelor's with honours" }
  - { outcome: "cognate disciplines", threshold: "qaa/anthropology-2024/ku.7.t", typical: "none", excellent: "qaa/anthropology-2024/ku.7.e", basis: "stated", domain: "understanding", award: "bachelor's with honours" }
  - { outcome: "diversity and environments", threshold: "qaa/anthropology-2024/ku.8.t", typical: "none", excellent: "qaa/anthropology-2024/ku.8.e", basis: "stated", domain: "understanding", award: "bachelor's with honours" }
  - { outcome: "disparities of experience", threshold: "qaa/anthropology-2024/ku.9.t", typical: "none", excellent: "qaa/anthropology-2024/ku.9.e", basis: "stated", domain: "knowledge", award: "bachelor's with honours" }
  - { outcome: "concepts, theories and methods", threshold: "qaa/anthropology-2024/ku.10.t", typical: "none", excellent: "qaa/anthropology-2024/ku.10.e", basis: "stated", domain: "understanding", award: "bachelor's with honours" }
  - { outcome: "history of Social Anthropology", threshold: "qaa/anthropology-2024/ku.11.t", typical: "none", excellent: "qaa/anthropology-2024/ku.11.e", basis: "stated", domain: "knowledge", award: "bachelor's with honours" }
  - { outcome: "social and cultural diversity", threshold: "qaa/anthropology-2024/ku.12.t", typical: "none", excellent: "qaa/anthropology-2024/ku.12.e", basis: "stated", domain: "understanding", award: "bachelor's with honours" }
  - { outcome: "a specialist region, group or aspect", threshold: "qaa/anthropology-2024/ku.13.t", typical: "none", excellent: "qaa/anthropology-2024/ku.13.e", basis: "stated", domain: "knowledge", award: "bachelor's with honours" }
  - { outcome: "diversity and ecodynamics", threshold: "qaa/anthropology-2024/ku.14.t", typical: "none", excellent: "qaa/anthropology-2024/ku.14.e", basis: "stated", domain: "understanding", award: "bachelor's with honours" }
  - { outcome: "ethics in Biological Anthropology", threshold: "qaa/anthropology-2024/ku.15.t", typical: "none", excellent: "qaa/anthropology-2024/ku.15.e", basis: "stated", domain: "understanding", award: "bachelor's with honours" }
  - { outcome: "biological diversity", threshold: "qaa/anthropology-2024/ku.16.t", typical: "none", excellent: "qaa/anthropology-2024/ku.16.e", basis: "stated", domain: "understanding", award: "bachelor's with honours" }
  - { outcome: "human physiology", threshold: "qaa/anthropology-2024/ku.17.t", typical: "none", excellent: "qaa/anthropology-2024/ku.17.e", basis: "stated", domain: "knowledge", award: "bachelor's with honours" }
  - { outcome: "history of Biological Anthropology", threshold: "qaa/anthropology-2024/ku.18.t", typical: "none", excellent: "qaa/anthropology-2024/ku.18.e", basis: "stated", domain: "knowledge", award: "bachelor's with honours" }
  - { outcome: "evolutionary theory", threshold: "qaa/anthropology-2024/ku.19.t", typical: "none", excellent: "qaa/anthropology-2024/ku.19.e", basis: "stated", domain: "knowledge", award: "bachelor's with honours" }
  - { outcome: "adaptive significance", threshold: "qaa/anthropology-2024/ku.20.t", typical: "none", excellent: "qaa/anthropology-2024/ku.20.e", basis: "stated", domain: "knowledge", award: "bachelor's with honours" }
  - { outcome: "species distribution and variability", threshold: "qaa/anthropology-2024/ku.21.t", typical: "none", excellent: "qaa/anthropology-2024/ku.21.e", basis: "stated", domain: "knowledge", award: "bachelor's with honours" }
  - { outcome: "the fossil and bioarchaeological record", threshold: "qaa/anthropology-2024/ku.22.t", typical: "none", excellent: "qaa/anthropology-2024/ku.22.e", basis: "stated", domain: "understanding", award: "bachelor's with honours" }
  - { outcome: "genetic evidence", threshold: "qaa/anthropology-2024/ku.23.t", typical: "none", excellent: "qaa/anthropology-2024/ku.23.e", basis: "stated", domain: "understanding", award: "bachelor's with honours" }
  - { outcome: "lines of evidence", threshold: "qaa/anthropology-2024/ku.24.t", typical: "none", excellent: "qaa/anthropology-2024/ku.24.e", basis: "stated", domain: "knowledge", award: "bachelor's with honours" }
  - { outcome: "research design and fieldwork", threshold: "qaa/anthropology-2024/ss.1.t", typical: "none", excellent: "qaa/anthropology-2024/ss.1.e", basis: "stated", domain: "subject-skill", award: "bachelor's with honours" }
  - { outcome: "social and biological contexts", threshold: "qaa/anthropology-2024/ss.2.t", typical: "none", excellent: "qaa/anthropology-2024/ss.2.e", basis: "stated", domain: "subject-skill", award: "bachelor's with honours" }
  - { outcome: "interpreting data", threshold: "qaa/anthropology-2024/ss.3.t", typical: "none", excellent: "qaa/anthropology-2024/ss.3.e", basis: "stated", domain: "subject-skill", award: "bachelor's with honours" }
  - { outcome: "communicating in media", threshold: "qaa/anthropology-2024/ss.4.t", typical: "none", excellent: "qaa/anthropology-2024/ss.4.e", basis: "stated", domain: "subject-skill", award: "bachelor's with honours" }
  - { outcome: "questions and theory", threshold: "qaa/anthropology-2024/ss.5.t", typical: "none", excellent: "qaa/anthropology-2024/ss.5.e", basis: "stated", domain: "subject-skill", award: "bachelor's with honours" }
  - { outcome: "engaging with other cultures", threshold: "qaa/anthropology-2024/ss.6.t", typical: "none", excellent: "qaa/anthropology-2024/ss.6.e", basis: "stated", domain: "subject-skill", award: "bachelor's with honours" }
  - { outcome: "reading sources", threshold: "qaa/anthropology-2024/ss.7.t", typical: "none", excellent: "qaa/anthropology-2024/ss.7.e", basis: "stated", domain: "subject-skill", award: "bachelor's with honours" }
  - { outcome: "applications of knowledge", threshold: "qaa/anthropology-2024/ss.8.t", typical: "none", excellent: "qaa/anthropology-2024/ss.8.e", basis: "stated", domain: "subject-skill", award: "bachelor's with honours" }
  - { outcome: "language, power and authority", threshold: "qaa/anthropology-2024/ss.9.t", typical: "none", excellent: "qaa/anthropology-2024/ss.9.e", basis: "stated", domain: "subject-skill", award: "bachelor's with honours" }
  - { outcome: "engagement with self-awareness", threshold: "qaa/anthropology-2024/ss.10.t", typical: "none", excellent: "qaa/anthropology-2024/ss.10.e", basis: "stated", domain: "subject-skill", award: "bachelor's with honours" }
  - { outcome: "measurement techniques", threshold: "qaa/anthropology-2024/ss.11.t", typical: "none", excellent: "qaa/anthropology-2024/ss.11.e", basis: "stated", domain: "subject-skill", award: "bachelor's with honours" }
  - { outcome: "research ethics", threshold: "qaa/anthropology-2024/ss.12.t", typical: "none", excellent: "qaa/anthropology-2024/ss.12.e", basis: "stated", domain: "subject-skill", award: "bachelor's with honours" }
  - { outcome: "communication and presentation", threshold: "qaa/anthropology-2024/gs.1.t", typical: "none", excellent: "qaa/anthropology-2024/gs.1.e", basis: "stated", domain: "generic-skill", award: "bachelor's with honours" }
  - { outcome: "independence of thought", threshold: "qaa/anthropology-2024/gs.2.t", typical: "none", excellent: "qaa/anthropology-2024/gs.2.e", basis: "stated", domain: "generic-skill", award: "bachelor's with honours" }
  - { outcome: "research skills", threshold: "qaa/anthropology-2024/gs.3.t", typical: "none", excellent: "qaa/anthropology-2024/gs.3.e", basis: "stated", domain: "generic-skill", award: "bachelor's with honours" }
  - { outcome: "ethical research", threshold: "qaa/anthropology-2024/gs.4.t", typical: "none", excellent: "qaa/anthropology-2024/gs.4.e", basis: "stated", domain: "generic-skill", award: "bachelor's with honours" }
  - { outcome: "argument and evidence", threshold: "qaa/anthropology-2024/gs.5.t", typical: "none", excellent: "qaa/anthropology-2024/gs.5.e", basis: "stated", domain: "generic-skill", award: "bachelor's with honours" }
  - { outcome: "group work", threshold: "qaa/anthropology-2024/gs.6.t", typical: "none", excellent: "qaa/anthropology-2024/gs.6.e", basis: "stated", domain: "generic-skill", award: "bachelor's with honours" }
  - { outcome: "analysis and data", threshold: "qaa/anthropology-2024/gs.7.t", typical: "none", excellent: "qaa/anthropology-2024/gs.7.e", basis: "stated", domain: "generic-skill", award: "bachelor's with honours" }
  - { outcome: "self-assessment", threshold: "qaa/anthropology-2024/gs.8.t", typical: "none", excellent: "qaa/anthropology-2024/gs.8.e", basis: "stated", domain: "generic-skill", award: "bachelor's with honours" }
  - { outcome: "challenging assumptions", threshold: "qaa/anthropology-2024/gs.9.t", typical: "none", excellent: "qaa/anthropology-2024/gs.9.e", basis: "stated", domain: "generic-skill", award: "bachelor's with honours" }
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
- { body: "Royal Anthropological Institute (RAI)", says: "a professional organisation whose resources and networks students should meet (D1, 2.18); a member of the 2024 advisory group came from it (D1, section 6)", requirements: "not yet ingested (Part E)" }
- { body: "British Association for Biological Anthropology and Osteoarchaeology (BABAO)", says: "its codes of practice set professional standards for collaborative work with communities; a professional organisation for students to meet (D1, 1.15, 2.18)", requirements: "not yet ingested (Part E)" }
- { body: "Association of Social Anthropologists (ASA)", says: "its codes of practice set professional standards for collaborative work with communities (D1, 1.15)", requirements: "not yet ingested (Part E)" }
- { body: "professional, statutory and regulatory bodies (PSRBs), unnamed", says: "the statement supports them on academic standards; their requirements are further reference points; courses with professional outcomes may need their accreditation (D1, front matter, 2.22)", requirements: "not-applicable-by-design: no body named (Part E)" }
```

### SB6 Cross-cutting references
<!-- label: both; status: drafted; basis: primary -->
```yaml
themes:
  - { id: "theme:edi", named: "Equality, diversity and inclusion", carriedIn: ["1.3", "1.4", "1.8", "1.9", "1.10", "3.18", "3.23"], statements: ["3.23"] }
  - { id: "theme:accessibility", named: "Accessibility and flexibility (front matter: accessibility and the needs of disabled students)", carriedIn: ["1.11", "1.12", "1.13", "3.18"], statements: ["1.11"] }
  - { id: "theme:esd", named: "Sustainability (front matter: education for sustainable development)", carriedIn: ["1.14", "1.15", "1.24", "3.5"], statements: ["3.5"] }
  - { id: "theme:enterprise", named: "Enterprise and Entrepreneurship Education (front matter: employability, entrepreneurship and enterprise education)", carriedIn: ["1.16", "1.17", "1.18", "1.19", "1.20", "1.21", "1.22", "2.15"], statements: ["1.21", "2.15"] }
frameworks:
  - { framework: "fheq", levels: ["fheq:6", "fheq:7"], citedIn: ["2.11", "2.13", "4.2"] }
  - { framework: "scqf", levels: ["fqheis:10", "fqheis:11"], citedIn: ["2.11", "2.13"] }
bodies:
  - { body: "Royal Anthropological Institute", citedIn: ["2.18"] }
  - { body: "British Association for Biological Anthropology and Osteoarchaeology", citedIn: ["1.15", "2.18"] }
  - { body: "Association of Social Anthropologists", citedIn: ["1.15"] }
  - { body: "PSRBs (unnamed)", citedIn: ["front matter", "2.22"] }
  - { body: "Office for Students (regulator, England)", citedIn: ["front matter"] }
sharedDocuments:
  - { document: "std:doc:qaa-fheq-2024-framework, Annex D", named: "Annex D in The Frameworks for Higher Education Qualifications of UK Degree-Awarding Bodies", citedIn: ["4.2"], role: "descriptions of the four honours classifications (1st, 2.1, 2.2, 3rd), for achievement above threshold" }
  - { document: "std:doc:qaa-advancehe-esd-2021-guidance", named: "QAA and Advance HE ESD", citedIn: ["1.15"], role: "source of the key competencies the subject develops for sustainability" }
  - { document: "UN Sustainable Development Goals (external)", named: "2015 United Nations Sustainable Development Goals (SDGs)", citedIn: ["1.15"], role: "frame for the sustainability competencies, by SDG number" }
  - { document: "QAA Quality Code, Advice and Guidance (not yet ingested)", named: "Advice and Guidance to support the Quality Code for Higher Education", citedIn: ["front matter"], role: "course design, teaching, external expertise, monitoring" }
  - { document: "QAA Glossary (not ingested)", named: "QAA's Glossary", citedIn: ["front matter"], role: "explains unfamiliar terms" }
  - { document: "Quality Assessment Framework for Wales; Quality Enhancement Framework (Scotland) (not ingested)", named: "the same", citedIn: ["front matter"], role: "where the statement is a key reference point" }
```

## Part B Terminology
<!-- The statement has no glossary of its own unless Part E says so; these are terms it defines in its text. -->

### B1 Concepts
<!-- label: both; status: drafted; basis: primary -->
```yaml
- { slug: "threshold-standard", definition: "the minimum a student will have demonstrated to be awarded the honours degree (D1, 4.1)", beneficiaryDefinition: "the least you must have shown by the end of your honours degree", scopeNote: "the first column of the section 4 tables", category: "unknown", practices: ["education"] }
- { slug: "strong-excellent", definition: "the performance column above threshold in the section 4 tables, also the expectation for master's students (D1, 2.11, 4.8)", beneficiaryDefinition: "what strong or excellent work looks like, beyond the minimum", scopeNote: "one column for strong and excellent; no separate typical level", category: "unknown", practices: ["education"] }
- { slug: "baseline-skills", definition: "skills every graduate in the subject will have, as distinct from the further skills that vary with modules and specialisms (D1, 4.5)", scopeNote: "the tables do not mark which rows are baseline (Part E)", category: "unknown", practices: ["education"] }
- { slug: "local-communities", definition: "the people a course works with in fieldwork: a population under study, people living alongside primates, descendants of past populations or others (D1, 2.15)", scopeNote: "to be treated as partners and, where fitting, co-producers of knowledge", category: "unknown", practices: ["education"] }
- { slug: "fieldwork", definition: "the broad heading for the forms of research practice students learn and apply, from participant observation to laboratory work (D1, 1.25, 2.9)", category: "unknown", practices: ["education"] }
```

### B2a Terms as the issuer defines them
<!-- label: source; status: drafted; basis: primary -->
```yaml
- { concept: "threshold-standard", form: "minimum threshold standards", lang: "en", partOfSpeech: "noun-phrase", termStatus: "preferred", register: "formal" }
- { concept: "strong-excellent", form: "Strong/excellent", lang: "en", partOfSpeech: "noun-phrase", termStatus: "preferred", register: "formal" }
- { concept: "baseline-skills", form: "'baseline' skills", lang: "en", partOfSpeech: "noun-phrase", termStatus: "preferred", register: "formal" }
- { concept: "local-communities", form: "'local communities'", lang: "en", partOfSpeech: "noun-phrase", termStatus: "preferred", register: "discipline-specific" }
- { concept: "fieldwork", form: "fieldwork", lang: "en", partOfSpeech: "noun", termStatus: "preferred", register: "discipline-specific" }
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
  title: "Subject Benchmark Statement Anthropology"
  edition: "April 2024 (fifth edition)"
  year: 2024
  url: unknown (the QAA page; the text came by stan's extraction)
  retrieved: "held from stan: wkspc2615-QAAVector mapped/anthropology-2024/anthropology-2024.raw.txt, commit 366bcb99a01118f2c4c3ebfa2a8337596bddc455; received 2026-10-03"
  licence: QAA copyright
  tier: primary
  readVia: direct
  held: 2b6b5a5effdb16257b38616ae89d7a3a45c2d967edbf4b71c436333ab645dd64
  heldFiles: ["wkspc2601-library/txt/qaa-2024-anthropology-subject-benchmark-statement-standard.txt", "wkspc2601-library/txt/qaa-2024-anthropology-subject-benchmark-statement-standard.norm.txt", "wkspc2601-library/records/qaa-2024-anthropology-subject-benchmark-statement-standard.chunks.json", "wkspc2601-library/records/qaa-2024-anthropology-subject-benchmark-statement-standard.held.json"]
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
- SB4, rung shape new to the series: two columns, Threshold and Strong/excellent, in three tables (knowledge and understanding 24 rows, subject-specific skills 12, generic skills 9), each row once in each column. The second column is recorded as rung `excellent` with `named: Strong/excellent`; there is no typical rung (SB4 `typical: none`). Each `gradeOf` therefore skips a rung (excellent to threshold); for Abbott at P3: keep `excellent` or map the column to `typical`?
- SB4, gradeOf basis: the issuer pairs each threshold and strong/excellent cell in one row, so SB4 records the 45 links as `basis: stated`; the builder writes every S4 `gradeOf` as `inferred`. The pairing is the issuer's, not ours.
- S4, ids: table rows have no paragraph numbers; the records are cut as `<table>.<row>.<t|e>` (ku knowledge and understanding, ss subject-specific skills, gs generic skills; t threshold, e strong/excellent) in the issuer's row numbering, each restarting at 1. The builder sorts them as text, so ku.10 comes before ku.2.
- S4, skeleton correction: the skeleton's component 4.8 runs from 4.8 to the end of section 4 and holds all three tables; it found no rung lead-ins and no table items. Every table cell is cut here by `find`, cell by cell; 4.8's own statement is its first sentence only.
- S4, cell boundaries judged where the extraction runs two cells together: ku.10, ku.12, ku.14 to ku.24, ss.2, ss.6, ss.10, ss.12 and gs.7. In ss.12 the sentence 'Act in accordance with rigorous ethical standards' is placed in the threshold cell; in gs.7 the sentence on the ethics of data access is placed in the threshold cell.
- S4, `source` carries page numbers and breaks the extraction left inside a cell (ku.9.e holds '19'; ku.8.e, ku.22.t, ss.7.t, ss.10.e, ss.11.t, gs.2.e and gs.8.t hold paragraph breaks). 4.8's source keeps the extraction's "'s trong/excellent'".
- S4, force: threshold cells take `threshold` from 4.1 ('minimum threshold standards'); strong/excellent cells take `describes`, since the column describes performance above the minimum for the honours degree (4.2) and is an expectation only for master's students (4.8). For Abbott at P3.
- S4, unlisted obliging words: 'required' and 'require' (1.21, 1.23, 1.26, 4.7) recorded as `must` (1.21, 1.23, 1.26) or kept under the paragraph's 'will' (4.7); 'can expect' (1.5, 1.24, 3.3, 3.13, 3.24) and 'will usually' (1.13, 3.2) not taken as obliging words.
- S4, D-std-0002 (a) judgements not taken as statements: 1.2 and 1.4 (the discipline 'should' address issues, perspectives 'must' be included: claims about the discipline, not standards); 1.10 and 1.15 a) ('requires' inside descriptions of the discipline and of an ESD competency); 1.14 (what ESD 'ensures' for students in general); 2.6 ('will introduce' inside a description of Biological Anthropology courses); 2.11, 2.17, 2.20, 2.21 and 3.19 (predictive or descriptive 'will'); 3.13 ('can expect'). Taken: the provider norms in 'will' that cover every course (3.2, 3.5, 3.21, 3.24, 3.25), under open point 5.
- S4, 3.10 and 3.12: the skeleton's list items are content topics (areas, SB3), not outcomes, so none is a statement; 3.10.b9's 'will be able to' is a hedge on courses ('not all courses will be able to offer'). 3.11 is one statement cut from its stem, the topic list left as an area.
- S4, 4.5: the tables mix 'baseline' skills every graduate has with further skills, but no row is marked baseline; each threshold record therefore applies to all graduates of its sub-table, pending P3.
- S4, ss.6.e is near word for word ss.10.e (general and Social Anthropology tables), and ss.10's two cells differ only by 'Meaningfully' and 'population'/'populations': the issuer's repetition, kept.
- S4, domain: ku rows split between knowledge and understanding by our reading (not stated); ku.13.t, ku.14.t and ku.14.e are noun phrases with no verb, ku.24.t and ss.11.t open with 'Be aware', so `verbs` holds only what the cell gives.
- S4, 4.7 and 4.8 are master's expectations at 'Level 7/11', a level the text does not tie to a framework by name in 4.7; recorded as fheq:7 and fqheis:11 from 2.13 and the FHEQ document's shared descriptor 4.17. 4.7 is `generic-skill` at fheq:7.
- S3: 1.4's last sentence repeats its first word for word; the repetition is in the held text, kept as the issuer's.
- S3, sections: the three tables are listed in SECTIONS as ku, ss and gs (sub-parts of section 4) so the records' heading paths name them; they are not numbered sections of the issuer.
- S2, subjects: 'Biological Anthropology' has no HECoS term of its own; physical and biological anthropology (100663) is the nearest and is entered as inferred. Primatology and palaeoanthropology (2.6) have no HECoS code. 'Anthropology', 'Social Anthropology' and 'Forensic Anthropology' are named in the text and their codes entered as stated.
- SB2 and SB6, themes: TH tags in S4 only the statements inside a theme's own section (1.11 accessibility, 1.21 enterprise); SB2 and SB6 also list statements whose paragraph carries a theme elsewhere (3.5 sustainability, 3.23 equality and inclusion, 2.15 employability). 1.24 is listed for sustainability because it points to that section. 'accessibility' in gs.7.t and 3.4 concerns data access, not the theme, and is not tagged.
- SB6, frameworks: CQFW is not cited. FQHEIS appears by that name in 2.11 and 2.13; 4.7's 'Level 7/11' and the reference to 'Scottish bachelor's degrees with honours' (2.14) name no framework and are not counted.
- SB5: the RAI, BABAO and the ASA are named; their own codes and requirements are not yet ingested. PSRBs are mentioned only generically (front matter, 2.22). The Office for Students is named in the front matter as England's regulator, not as a body for the subject.
- S7, supersedes: the 2019 fourth edition is named in section 6; earlier editions (2015, 2007, 2002) appear only as advisory group lists.
- Patterns differing from Psychology: two-column tables in place of three rung lists; no typical rung; rows split by sub-discipline (general, Social, Biological); master's study stated through 4.7 and 4.8, not a conversion course; no outcome lists ('are able to') outside the tables; obligations in 'required' as well as must and should.
- S9: not researched in P1.
- S1, licence: the text gives a copyright notice and no re-use terms; QAA's terms for holding and chunking are still to check.
- ST-12: versions here run to the lengths the content needs; no length range is yet set.

---

## Change notes
- 0.1.2, 3 October 2026, 21:02: moved with its held text from UNI to the source library repo (`wkspc2601-library/ingested/standards/`, texts in `txt/`, records in `records/`); paths only (Abbott, 20:56; std N-0119).
- 0.1.1, 3 October 2026, 20:20: obliging words outside the five read as must, "ought to" as should, on statements outside the rungs, each marked on its force line (Abbott, 20:17; D-std-0016).
- 0.1.0, 2026-10-03 16:19: researched by run frame 0.1.1-draft and standards run layer 0.7.0-draft, std, run 0084 (P1); built by tools/bm_build.py.
