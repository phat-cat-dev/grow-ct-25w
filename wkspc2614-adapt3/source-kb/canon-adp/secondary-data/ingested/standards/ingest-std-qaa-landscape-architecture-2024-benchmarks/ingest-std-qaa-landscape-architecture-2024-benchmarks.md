---
id: std:doc:qaa-landscape-architecture-2024-benchmarks
title: "Subject Benchmark Statement: Landscape Architecture"
profile: standards/subject-benchmark
profileVersion: 0.2.0-draft
issuer: QAA
kind: subject-benchmark
jurisdiction: [UK]
subjectScope: subjects
subjects:
  - { scheme: "hecos", code: "100124", label: "landscape architecture and design", basis: "inferred" }
  - { scheme: "cah", code: "CAH13-01-03", label: "landscape design", basis: "inferred" }
  - { scheme: "hecos", code: "100588", label: "landscape studies", basis: "inferred" }
edition: "April 2024 (fifth edition)"
published: 2024-04
status: current
supersedes: "Subject Benchmark Statement: Landscape Architecture, fourth edition (2019), as the advisory group list states"
heldText: { method: sha256-bytes, raw: 8ed7fbd1077ea06319c974e4bc7cdd35cf4785844ded756978f26e1ecddb81c2, normalised: cae0c5894821e6c110a19c33eb19e1978b57ae001374ee8d29bc4337b34a09e7 }
heldTextStan: { method: sha256-stan, raw: 8ed7fbd1077ea06319c974e4bc7cdd35cf4785844ded756978f26e1ecddb81c2, normalised: f1f325f08233108c814ae83173feee9c8f7ebf934dc3ada2f7bcb9c8f4eea27b }
licence: "QAA copyright; held for study, private to the project, never published"
series: "QAA Subject Benchmark Statements, 2024 revision with cross-cutting themes (fifth edition of this statement)"
awardsCovered: ["bachelor's with honours", "master's"]
levelsCovered: ["fheq:6", "fqheis:10", "fheq:7", "fqheis:11"]
nations: ["England", "Wales", "Scotland", "Northern Ireland"]
parts:
  S: full
  B: "partial: no glossary in the document (it points to QAA's Glossary); terms it defines in passing"
  C: "not-applicable: the document sets expectations, not a procedure"
pins: { structure: 0.13.0-draft, template: 0.8.0-draft, benchmarkTemplate: 0.6.0-draft, runFrame: 0.1.1-draft, runLayer: 0.7.0-draft, standards: none yet, terminology: none yet }
lifecycle: drafted
researchedBy: run frame 0.1.1-draft; standards run layer 0.7.0-draft; std, run 0114 (tools/bm_build.py)
passes:
  P1: "2026-10-03 17:44"
  P2: "skipped: read direct from the held text; inferred codes and rung links are for P3"
  P3: open
version: 0.1.2
---

<!-- from INGEST wpk-0016-ingest-pd-template-standards.md 0.8.0-draft and wpk-0016-ingest-pd-template-standards-benchmark.md 0.6.0-draft; built by tools/bm_build.py from run-src/ -->
# Subject Benchmark Statement: Landscape Architecture (QAA, April 2024)

> Run 0114, P1 by std. The issuer's words are held in the source library, `wkspc2601-library/txt/qaa-2024-landscape-architecture-subject-benchmark-statement-standard.norm.txt`; each S4 record carries its statement in full (`source`) for language analysis, with its span. Paraphrases and versions are ours. Private to the project, never published. In front matter `status` is the issuer's; ours is `lifecycle`. Doubts are in Part E.

## Part 0 Summary

### 0.1 Agent definition
<!-- label: editorial; status: drafted; basis: primary -->
This document records what the QAA expects a graduate in landscape architecture to know, understand and be able to do, chiefly at honours level, with a short list of further expectations for master's graduates. Use it to find a threshold, typical or excellent standard by id, to see how the four cross-cutting themes and generative AI show in the subject, and to trace the Landscape Institute's accreditation context. It is a sector reference point, not a regulation; each statement is cited by the issuer's paragraph number and set beside the FHEQ, FQHEIS and Annex D records it sits at.

### 0.2 Summary
<!-- label: both; status: drafted; basis: primary -->
Landscape architecture studies, plans, designs, manages and conserves landscapes of every type and scale, drawing on the arts, humanities and the natural and social sciences. The statement covers honours degrees (FHEQ level 6, FQHEIS level 10) and adds a threshold list for master's graduates (level 7, FQHEIS 11). It states three rungs for honours: a long threshold list of 56 items in seven skill groups (intellectual; analytical and data interpretation; practical; self-management and professional development; digital literacy; communication; interpersonal and teamwork), and three items each for typical and excellent that build on the whole threshold list. Its themes are equality, diversity and inclusion, accessibility, sustainability and employability, enterprise and entrepreneurship, with generative AI treated in assessment and in the digital skills. The Landscape Institute accredits courses and sets the competency framework; IFLA sets international principles.

## Part S Standard

### S1 Identity
<!-- label: source; status: drafted; basis: primary -->
```yaml
issuer: The Quality Assurance Agency for Higher Education
title: "Subject Benchmark Statement: Landscape Architecture"
edition: "April 2024 (fifth edition)"
dates:
  published: 2024-04
  other: []
kind: subject-benchmark
jurisdiction: [UK]
authority: "reference: a sector reference point, not a regulatory requirement; a key reference point for academic standards in Wales and Scotland, not a sector-recognised standard in England (D1, front matter)"
licence: "QAA copyright; the document gives no re-use terms in its text (D1, front matter)"
copyrightNotice: { text: "© The Quality Assurance Agency for Higher Education 2024", locator: "D1, index" }
```

### S2 Purpose and scope
<!-- label: source; status: drafted; basis: primary -->
```yaml
governs: "the academic standards and the scope of honours degrees in landscape architecture in the UK, with expectations for master's graduates"
appliesTo:
  awards: ["bachelor's with honours", "master's"]
  levels: ["fheq:6", "fqheis:10", "fheq:7", "fqheis:11"]
  providers: ["UK higher education providers"]
whoMustUse: "none-stated; it is a reference point, not a requirement (D1, front matter)"
howUsed: ["design", "approval", "review", "other: external examining; PSRBs; information for prospective students and employers"]
doesNot: "it is not a national curriculum and does not prescribe teaching, learning or assessment; it carries no statutory or regulatory requirement (D1, front matter)"
beneficiary: the student
statedScope: "\"This Subject Benchmark Statement aims to clarify the scope and standards of degree courses in Landscape Architecture.\" (D1, 1.1)"
statedSubjects:
  - { name: "Landscape Architecture", locator: "(D1, 1.1; 1.2)", kind: "subject", codes: [{ scheme: "hecos", code: "100124", label: "landscape architecture and design" }, { scheme: "cah", code: "CAH13-01-03", label: "landscape design" }] }
  - { name: "Landscape Architecture with Planning (dual honours)", locator: "(D1, 3.2)", kind: "programme title", codes: [{ scheme: "hecos", code: "100124", label: "landscape architecture and design" }, { scheme: "hecos", code: "100197", label: "planning" }] }
  - { name: "Planning, Urban Design or Ecology (subjects a course may be offered with)", locator: "(D1, 2.22)", kind: "subject", codes: [{ scheme: "hecos", code: "100197", label: "planning" }, { scheme: "hecos", code: "100347", label: "ecology" }] }
  - { name: "landscape planning, management, ecology and science (practitioner specialisms)", locator: "(D1, 1.10; 2.5)", kind: "specialism", codes: [{ scheme: "hecos", code: "100588", label: "landscape studies" }, { scheme: "hecos", code: "100864", label: "ecosystem ecology and land use" }] }
subjects: see front matter (subjectScope subjects)
```

### S3 Structure
<!-- label: both; status: drafted; basis: primary -->
```yaml
components:
  - { number: "1.1", order: 3, componentType: paragraph, parent: "section 1", heading: "Context and purposes of a Landscape Architecture degree", gloss: "the aim: scope and standards of degree courses" }
  - { number: "1.2", order: 4, componentType: paragraph, parent: "section 1", heading: "Context and purposes of a Landscape Architecture degree", gloss: "a profession and an academic subject drawing on many fields" }
  - { number: "1.3", order: 5, componentType: paragraph, parent: "section 1", heading: "Context and purposes of a Landscape Architecture degree", gloss: "what research and scholarship in the subject seek to understand" }
  - { number: "1.4", order: 6, componentType: paragraph, parent: "section 1", heading: "Context and purposes of a Landscape Architecture degree", gloss: "the work the discipline does, at every scale; policy role through the LI" }
  - { number: "1.5", order: 7, componentType: paragraph, parent: "section 1", heading: "Context and purposes of a Landscape Architecture degree", gloss: "how practitioners change places, from city parks to national infrastructure; the 2019 DEFRA review quoted" }
  - { number: "1.6", order: 8, componentType: area, parent: "section 1", heading: "Context and purposes of a Landscape Architecture degree", gloss: "a place-focused discipline: three sensitivities (natural systems, cultural identity, global and local decisions)" }
  - { number: "1.7", order: 9, componentType: stem, parent: "section 1", heading: "Context and purposes of a Landscape Architecture degree", gloss: "leading green infrastructure, with five kinds of place it aims to create" }
  - { number: "1.8", order: 10, componentType: paragraph, parent: "section 1", heading: "Context and purposes of a Landscape Architecture degree", gloss: "contributing to policy on protected landscapes" }
  - { number: "1.9", order: 11, componentType: paragraph, parent: "section 1", heading: "The professional body context", gloss: "two professional bodies: IFLA internationally, the LI in the UK" }
  - { number: "1.10", order: 12, componentType: paragraph, parent: "section 1", heading: "The professional body context: The Landscape Institute", gloss: "the LI as the chartered body and whom it represents" }
  - { number: "1.11", order: 13, componentType: paragraph, parent: "section 1", heading: "The professional body context: The Landscape Institute", gloss: "LI members follow its code of practice, tied to IFLA ethical principles" }
  - { number: "1.12", order: 14, componentType: paragraph, parent: "section 1", heading: "The professional body context: The Landscape Institute", gloss: "the LI accredits courses; its report on the core activities of the profession" }
  - { number: "1.13", order: 15, componentType: stem, parent: "section 1", heading: "The professional body context: The Landscape Institute", gloss: "the four cross-cutting themes of this edition" }
  - { number: "1.14", order: 16, componentType: paragraph, parent: "section 1", heading: "The professional body context: The Landscape Institute", gloss: "the themes complement each other and the statement" }
  - { number: "1.15", order: 17, componentType: stem, parent: "section 1", heading: "The professional body context: The Landscape Institute", gloss: "the LI competency framework covers all four themes, with four example competencies" }
  - { number: "1.16", order: 18, componentType: paragraph, parent: "section 1", heading: "The professional body context: The Landscape Institute", gloss: "employability and enterprise implicit in the competency framework" }
  - { number: "1.17", order: 19, componentType: paragraph, parent: "section 1", heading: "The professional body context: The Landscape Institute", gloss: "the code of practice repeated with the theme context" }
  - { number: "1.18", order: 20, componentType: stem, parent: "section 1", heading: "The professional body context: The Landscape Institute", gloss: "two LI steps on EDI: a built-environment memorandum and a landscape-sector declaration" }
  - { number: "1.19", order: 21, componentType: paragraph, parent: "section 1", heading: "The professional body context: The International Federation of Landscape Architects (IFLA)", gloss: "IFLA, its role in education and the IFLA/UNESCO charter definition" }
  - { number: "1.20", order: 22, componentType: paragraph, parent: "section 1", heading: "Key points in relation to the cross-cutting themes", gloss: "providers already bear legal duties on the themes and sector targets" }
  - { number: "1.21", order: 23, componentType: paragraph, parent: "section 1", heading: "Key points in relation to the cross-cutting themes", gloss: "section 4 names the standards; the theme expectations are set out here" }
  - { number: "1.22", order: 24, componentType: stem, parent: "section 1", heading: "Key points in relation to the cross-cutting themes", gloss: "three features of projects and briefs that serve all the themes" }
  - { number: "1.23", order: 25, componentType: paragraph, parent: "section 1", heading: "Equality, diversity and inclusion (EDI)", gloss: "inclusive curricula and pedagogy, widening participation, zero tolerance of discrimination" }
  - { number: "1.24", order: 26, componentType: stem, parent: "section 1", heading: "Equality, diversity and inclusion (EDI)", gloss: "students build EDI literacy through four kinds of inquiry" }
  - { number: "1.25", order: 27, componentType: stem, parent: "section 1", heading: "Accessibility", gloss: "accessibility in delivery, physical and academic" }
  - { number: "1.26", order: 28, componentType: stem, parent: "section 1", heading: "Sustainability", gloss: "course content and education for sustainability: seven areas of understanding" }
  - { number: "1.27", order: 29, componentType: stem, parent: "section 1", heading: "Employability, enterprise and entrepreneurship education", gloss: "courses may help students towards a rewarding professional life: four opportunities" }
  - { number: "2.1", order: 31, componentType: paragraph, parent: "section 2", heading: "Distinctive features of Landscape Architecture courses", gloss: "distinctiveness from the European Landscape Convention and its definition of landscape" }
  - { number: "2.2", order: 32, componentType: stem, parent: "section 2", heading: "Distinctive features of Landscape Architecture courses", gloss: "the convention obliges the UK to provide landscape training; three measures" }
  - { number: "2.3", order: 33, componentType: paragraph, parent: "section 2", heading: "Professional accreditation", gloss: "LI accreditation leading to chartered titles" }
  - { number: "2.4", order: 34, componentType: stem, parent: "section 2", heading: "Professional accreditation", gloss: "four areas of the LI accreditation criteria" }
  - { number: "2.5", order: 35, componentType: paragraph, parent: "section 2", heading: "Professional accreditation", gloss: "each course finds its own focus; accredited courses map to the competency framework" }
  - { number: "2.6", order: 36, componentType: paragraph, parent: "section 2", heading: "Professional accreditation", gloss: "credit and level for accreditation set in the LI procedures" }
  - { number: "2.7", order: 37, componentType: paragraph, parent: "section 2", heading: "Professional accreditation", gloss: "the LI lists accredited courses; some courses are not accredited" }
  - { number: "2.8", order: 38, componentType: paragraph, parent: "section 2", heading: "Professional accreditation", gloss: "meeting this statement is not accreditation; consult the LI" }
  - { number: "2.9", order: 39, componentType: paragraph, parent: "section 2", heading: "Professional accreditation", gloss: "accreditation decisions rest with the LI" }
  - { number: "2.10", order: 40, componentType: stem, parent: "section 2", heading: "Course design", gloss: "provider design frameworks and six features course design may have" }
  - { number: "2.11", order: 41, componentType: paragraph, parent: "section 2", heading: "Progression", gloss: "progression through the honours levels to the threshold; a second or above fits a student for postgraduate study" }
  - { number: "2.12", order: 42, componentType: paragraph, parent: "section 2", heading: "Progression", gloss: "joint and combined honours students reach core elements of the skills" }
  - { number: "2.13", order: 43, componentType: paragraph, parent: "section 2", heading: "Progression", gloss: "exit awards, three-year and four-year (Scottish) durations, part-time credit" }
  - { number: "2.14", order: 44, componentType: paragraph, parent: "section 2", heading: "Progression", gloss: "honours as a step towards the master's; some courses ask for a year in practice" }
  - { number: "2.15", order: 45, componentType: paragraph, parent: "section 2", heading: "Progression", gloss: "chartership route needs an accredited master's of 180 credits at level 7" }
  - { number: "2.16", order: 46, componentType: paragraph, parent: "section 2", heading: "Progression", gloss: "accredited master's graduates become LI associate members" }
  - { number: "2.17", order: 47, componentType: paragraph, parent: "section 2", heading: "Alternative routes", gloss: "four-year integrated undergraduate degrees" }
  - { number: "2.18", order: 48, componentType: paragraph, parent: "section 2", heading: "Alternative routes", gloss: "one-year conversion routes before the master's stage" }
  - { number: "2.19", order: 49, componentType: paragraph, parent: "section 2", heading: "Alternative routes", gloss: "integrated master's degrees over four years" }
  - { number: "2.20", order: 50, componentType: paragraph, parent: "section 2", heading: "Flexibility", gloss: "modes, timing and micro-credentials" }
  - { number: "2.21", order: 51, componentType: paragraph, parent: "section 2", heading: "Flexibility", gloss: "prospective students and funding arrangements" }
  - { number: "2.22", order: 52, componentType: paragraph, parent: "section 2", heading: "Partnerships", gloss: "courses vary in focus; joint subjects and dual accreditation" }
  - { number: "2.23", order: 53, componentType: paragraph, parent: "section 2", heading: "Apprenticeships", gloss: "the Level 3 Landscape Technician qualification as a possible entry route" }
  - { number: "2.24", order: 54, componentType: paragraph, parent: "section 2", heading: "Apprenticeships", gloss: "the Level 7 Chartered Landscape Professional apprenticeship" }
  - { number: "2.25", order: 55, componentType: paragraph, parent: "section 2", heading: "Monitoring and review: Internal", gloss: "internal monitoring and periodic review" }
  - { number: "2.26", order: 56, componentType: paragraph, parent: "section 2", heading: "Monitoring and review: Externality", gloss: "external reviewers in periodic review" }
  - { number: "2.27", order: 57, componentType: paragraph, parent: "section 2", heading: "Monitoring and review: Externality", gloss: "external examining in the subject, from practice and academia" }
  - { number: "2.28", order: 58, componentType: paragraph, parent: "section 2", heading: "Monitoring and review: Professional review", gloss: "professional review of accredited courses by an LI review group" }
  - { number: "3.1", order: 60, componentType: paragraph, parent: "section 3", heading: "Content, structure and delivery", gloss: "iterative processes students use to resolve problems" }
  - { number: "3.2", order: 61, componentType: area, parent: "section 3", heading: "Core areas common to all Landscape Architecture courses", gloss: "content by course focus; four groups of common areas (context, systems and process, stakeholders, delivery)" }
  - { number: "3.3", order: 62, componentType: practice, parent: "section 3", heading: "Teaching and learning", gloss: "teaching techniques and the studio-based culture" }
  - { number: "3.4", order: 63, componentType: practice, parent: "section 3", heading: "Teaching and learning", gloss: "projects simulate practice, from small sites to strategic planning" }
  - { number: "3.5", order: 64, componentType: practice, parent: "section 3", heading: "Teaching and learning", gloss: "a cumulative approach from survey to specification" }
  - { number: "3.6", order: 65, componentType: practice, parent: "section 3", heading: "Teaching and learning", gloss: "tutorials, presentations, the design studio and collaborative projects" }
  - { number: "3.7", order: 66, componentType: practice, parent: "section 3", heading: "Teaching and learning", gloss: "placements and visiting practitioners" }
  - { number: "3.8", order: 67, componentType: paragraph, parent: "section 3", heading: "Assessment", gloss: "assessment follows QAA principles and advice" }
  - { number: "3.9", order: 68, componentType: practice, parent: "section 3", heading: "Assessment", gloss: "formative and summative assessment at all levels" }
  - { number: "3.10", order: 69, componentType: practice, parent: "section 3", heading: "Assessment", gloss: "formative assessment defined" }
  - { number: "3.11", order: 70, componentType: practice, parent: "section 3", heading: "Assessment", gloss: "summative assessment defined" }
  - { number: "3.12", order: 71, componentType: practice, parent: "section 3", heading: "Assessment", gloss: "the range of assessment methods students meet" }
  - { number: "3.13", order: 72, componentType: practice, parent: "section 3", heading: "Assessment", gloss: "recognition of prior learning" }
  - { number: "3.14", order: 73, componentType: practice, parent: "section 3", heading: "Assessment", gloss: "generative AI: challenges to integrity and design, the need for openness" }
  - { number: "4.1", order: 75, componentType: paragraph, parent: "section 4", heading: "Introduction", gloss: "the threshold is the minimum for an honours award" }
  - { number: "4.2", order: 76, componentType: paragraph, parent: "section 4", heading: "Introduction", gloss: "most exceed the threshold; typical and excellent described; above threshold follows marking schemes" }
  - { number: "4.3", order: 77, componentType: paragraph, parent: "section 4", heading: "Introduction", gloss: "providers decide the evidence and refer to Annex D" }
  - { number: "4.4", order: 78, componentType: stem, parent: "section 4", heading: "Threshold level: Subject knowledge, understanding and skills", gloss: "threshold standard: seven skill groups" }
  - { number: "4.5", order: 79, componentType: stem, parent: "section 4", heading: "Typical standard", gloss: "typical standard: three items beyond threshold" }
  - { number: "4.6", order: 80, componentType: stem, parent: "section 4", heading: "Excellent standard", gloss: "excellent standard: three items beyond typical" }
  - { number: "4.7", order: 81, componentType: stem, parent: "section 4", heading: "Master's degrees", gloss: "master's graduates at threshold: eight further qualities" }
  - { number: "1", componentType: section, parent: none, heading: "Context and purposes of a Landscape Architecture degree", gloss: "section 1" }
  - { number: "2", componentType: section, parent: none, heading: "Distinctive features of Landscape Architecture courses", gloss: "section 2" }
  - { number: "3", componentType: section, parent: none, heading: "Content, structure and delivery", gloss: "section 3" }
  - { number: "4", componentType: section, parent: none, heading: "Benchmark standards", gloss: "section 4" }
excluded:
  - { number: "none", heading: "About this Statement; How can I use this document?; Relationship to legislation; Additional sector reference points", kind: "other: front matter, read for S1 and S2" }
  - { number: "none", heading: "Contents", kind: "other: table of contents" }
  - { number: "5", heading: "List of references and further resources", kind: "other: reference list, read for SB6 and D3" }
  - { number: "6", heading: "Membership of the Advisory Group", kind: "other: membership lists 2000 to 2024, read for supersedes" }
  - { number: "none", heading: "section heading lines", kind: "other: headings, recorded in SECTIONS and SUB" }
```

### S4 Statements
<!-- label: both; status: drafted; basis: primary. Only standards (D-std-0002 (a)): 88 records. `source` is the issuer's statement exactly as its span holds it (D-std-0014). -->
```yaml
- id: qaa/landscape-architecture-2024/1.25.b1
  locator: { number: "1.25.b1", headingPath: ["Context and purposes of a Landscape Architecture degree", "Accessibility"] }
  span: { start: 22337, end: 22397 }
  source: "physically to resources and facilities, including field work"
  stem: "1.25"
  statementType: expectation
  rung: none
  force: should
  level: none
  appliesTo: "courses in the subject"
  addressee: provider
  verbs: []
  about: "physical access to resources and fieldwork"
  themes: [theme:accessibility]
  domain: none
  award: ["none"]
  gradeOf: none
  paraphrase: "Courses should consider how inclusive, fair design opens physical access to resources and facilities, fieldwork among them."
  quote: full   # the issuer's statement is in `source` (D-std-0014)
  audience: practitioner
  subjects: inherited
- id: qaa/landscape-architecture-2024/1.25.b2
  locator: { number: "1.25.b2", headingPath: ["Context and purposes of a Landscape Architecture degree", "Accessibility"] }
  span: { start: 22400, end: 22505 }
  source: "academically where alternative forms of teaching, learning, assessment and feedback might be appropriate."
  stem: "1.25"
  statementType: expectation
  rung: none
  force: should
  level: none
  appliesTo: "courses in the subject"
  addressee: provider
  verbs: []
  about: "academic access through alternative forms of delivery"
  themes: [theme:accessibility]
  domain: none
  award: ["none"]
  gradeOf: none
  paraphrase: "Courses should consider how inclusive design opens academic access, offering other forms of teaching, learning, assessment or feedback where they suit."
  quote: full   # the issuer's statement is in `source` (D-std-0014)
  audience: practitioner
  subjects: inherited
- id: qaa/landscape-architecture-2024/1.26.b1
  locator: { number: "1.26.b1", headingPath: ["Context and purposes of a Landscape Architecture degree", "Sustainability"] }
  span: { start: 22736, end: 22865 }
  source: "sustainability values and actions which transform society and regenerative futures, as illustrated by the UN Sustainability Goals"
  stem: "1.26"
  statementType: expectation
  rung: none
  force: will
  level: none
  appliesTo: "students of the subject, through course content"
  addressee: both
  verbs: ["transform"]
  about: "values and actions for sustainability and the UN goals"
  themes: [theme:esd]
  domain: understanding
  award: ["none"]
  gradeOf: none
  paraphrase: "Course content will let students show they understand values and actions for sustainability that change society and lead to regenerative futures, as the UN goals illustrate."
  quote: full   # the issuer's statement is in `source` (D-std-0014)
  audience: both
  subjects: inherited
- id: qaa/landscape-architecture-2024/1.26.b2
  locator: { number: "1.26.b2", headingPath: ["Context and purposes of a Landscape Architecture degree", "Sustainability"] }
  span: { start: 22868, end: 23068 }
  source: "‘systems thinking’ with a focus on biodiversity, natural systems, natural capital and the ecosystems, goods and services that flow from these assets, and our interaction with them at a range of scales"
  stem: "1.26"
  statementType: expectation
  rung: none
  force: will
  level: none
  appliesTo: "students of the subject, through course content"
  addressee: both
  verbs: []
  about: "systems thinking: biodiversity and natural capital"
  themes: [theme:esd]
  domain: understanding
  award: ["none"]
  gradeOf: none
  paraphrase: "Course content will let students show they understand systems thinking centred on biodiversity, natural systems, natural capital and the ecosystem services that flow from them, at several scales."
  quote: full   # the issuer's statement is in `source` (D-std-0014)
  audience: both
  subjects: inherited
- id: qaa/landscape-architecture-2024/1.26.b3
  locator: { number: "1.26.b3", headingPath: ["Context and purposes of a Landscape Architecture degree", "Sustainability"] }
  span: { start: 23071, end: 23207 }
  source: "climate change, the causes and effects and the identification of opportunities for mitigation, adaptation and the building of resilience"
  stem: "1.26"
  statementType: expectation
  rung: none
  force: will
  level: none
  appliesTo: "students of the subject, through course content"
  addressee: both
  verbs: []
  about: "climate change: causes, effects, mitigation and adaptation"
  themes: [theme:esd]
  domain: understanding
  award: ["none"]
  gradeOf: none
  paraphrase: "Course content will let students show they understand the causes and effects of climate change and see chances for mitigation, adaptation and resilience."
  quote: full   # the issuer's statement is in `source` (D-std-0014)
  audience: both
  subjects: inherited
- id: qaa/landscape-architecture-2024/1.26.b4
  locator: { number: "1.26.b4", headingPath: ["Context and purposes of a Landscape Architecture degree", "Sustainability"] }
  span: { start: 23210, end: 23364 }
  source: "the context of international, national and local legislation, and historic, extant and emerging policy at a range of levels and across a range of subjects"
  stem: "1.26"
  statementType: expectation
  rung: none
  force: will
  level: none
  appliesTo: "students of the subject, through course content"
  addressee: both
  verbs: []
  about: "legislation and policy at many levels"
  themes: [theme:esd]
  domain: understanding
  award: ["none"]
  gradeOf: none
  paraphrase: "Course content will let students show they understand international, national and local law and past, current and emerging policy across levels and subjects."
  quote: full   # the issuer's statement is in `source` (D-std-0014)
  audience: both
  subjects: inherited
- id: qaa/landscape-architecture-2024/1.26.b5
  locator: { number: "1.26.b5", headingPath: ["Context and purposes of a Landscape Architecture degree", "Sustainability"] }
  span: { start: 23367, end: 23447 }
  source: "design for adaptation, resilience and regeneration of communities and landscapes"
  stem: "1.26"
  statementType: expectation
  rung: none
  force: will
  level: none
  appliesTo: "students of the subject, through course content"
  addressee: both
  verbs: []
  about: "design for adaptation, resilience and regeneration"
  themes: [theme:esd]
  domain: understanding
  award: ["none"]
  gradeOf: none
  paraphrase: "Course content will let students show they understand design that helps communities and landscapes adapt, become resilient and regenerate."
  quote: full   # the issuer's statement is in `source` (D-std-0014)
  audience: both
  subjects: inherited
- id: qaa/landscape-architecture-2024/1.26.b6
  locator: { number: "1.26.b6", headingPath: ["Context and purposes of a Landscape Architecture degree", "Sustainability"] }
  span: { start: 23450, end: 23701 }
  source: "case studies and best practice, illustrating sustainability across a range of scales and types of development; including, where possible, the exploration of live projects and living scenarios that deal with uncertainty and envision sustainable futures"
  stem: "1.26"
  statementType: expectation
  rung: none
  force: will
  level: none
  appliesTo: "students of the subject, through course content"
  addressee: both
  verbs: []
  about: "case studies, best practice and live projects"
  themes: [theme:esd]
  domain: understanding
  award: ["none"]
  gradeOf: none
  paraphrase: "Course content will let students show understanding through case studies and good practice across scales and kinds of development, with live projects where possible."
  quote: full   # the issuer's statement is in `source` (D-std-0014)
  audience: both
  subjects: inherited
- id: qaa/landscape-architecture-2024/1.26.b7
  locator: { number: "1.26.b7", headingPath: ["Context and purposes of a Landscape Architecture degree", "Sustainability"] }
  span: { start: 23704, end: 23846 }
  source: "materiality in relation to the main palettes of materials they might specify, including the extraction of raw materials and disposal of waste."
  stem: "1.26"
  statementType: expectation
  rung: none
  force: will
  level: none
  appliesTo: "students of the subject, through course content"
  addressee: both
  verbs: ["specify"]
  about: "materiality: extraction and waste"
  themes: [theme:esd]
  domain: understanding
  award: ["none"]
  gradeOf: none
  paraphrase: "Course content will let students show they understand the materials they may specify, from extracting raw materials to disposing of waste."
  quote: full   # the issuer's statement is in `source` (D-std-0014)
  audience: both
  subjects: inherited
- id: qaa/landscape-architecture-2024/2.5
  locator: { number: "2.5", headingPath: ["Distinctive features of Landscape Architecture courses", "Professional accreditation"] }
  span: { start: 26476, end: 26935 }
  source: "2.5 Each course will determine its own individual identity and focus within the broad spectrum of subject matters embraced by Landscape Architecture. Accredited courses are required to map their courses against the LI Competency Framework to demonstrate where relevant knowledge requirements are addressed. Some may be focused on design, while others focus on planning, management or ecology; each course will map against the competencies deemed appropriate.\n"
  stem: none
  statementType: requirement
  rung: none
  force: must
  level: none
  appliesTo: "courses seeking or holding LI accreditation"
  addressee: provider
  verbs: ["determine", "map", "demonstrate"]
  about: "mapping accredited courses to the LI competency framework"
  themes: [none]
  domain: none
  award: ["none"]
  gradeOf: none
  paraphrase: "Each course will set its own identity and focus; accredited courses must map themselves to the LI competency framework to show where knowledge requirements are met."
  quote: full   # the issuer's statement is in `source` (D-std-0014)
  audience: practitioner
  subjects: inherited
- id: qaa/landscape-architecture-2024/2.11
  locator: { number: "2.11", headingPath: ["Distinctive features of Landscape Architecture courses", "Progression"] }
  span: { start: 29391, end: 30353 }
  source: "2.11 Over the course of a degree with honours (FHEQ Level 6; FQHEIS Level 10) a Landscape Architecture student will progress from one level of study to the next, in line with the regulations and processes for each institution. It is expected that each level would see the attainment of knowledge, expertise and experience that builds towards the final achievement of meeting all the threshold-level subject-specific and generic skills listed in this Statement. This will usually include successful completion and the award of credits for the full range of learning and assessment, including any practical components. Upon graduation from an undergraduate degree, it would be expected that a student who had achieved a second-class degree or higher would be capable of, and equipped for, undertaking postgraduate study in Landscape Architecture or a related discipline. Entry requirements to postgraduate courses are, however, determined by individual providers.\n"
  stem: none
  statementType: expectation
  rung: none
  force: must   # D-std-0016: "requirements" read as must
  level: fheq:6
  appliesTo: "honours students of the subject"
  addressee: learner
  verbs: ["progress", "builds"]
  about: "progression through the levels to the threshold"
  themes: [none]
  domain: none
  award: ["bachelor's with honours"]
  gradeOf: none
  paraphrase: "Across an honours degree students move up level by level; each level is expected to build towards meeting every threshold skill, usually through credit for all learning and assessment."
  quote: full   # the issuer's statement is in `source` (D-std-0014)
  audience: both
  subjects: inherited
- id: qaa/landscape-architecture-2024/2.12
  locator: { number: "2.12", headingPath: ["Distinctive features of Landscape Architecture courses", "Progression"] }
  span: { start: 30353, end: 30786 }
  source: "2.12 Undergraduates studying Landscape Architecture courses as part of a combined or joint degree with other subjects will achieve core elements of the specific and generic skills outlined in this Statement and will add others according to the topics covered in the other subject(s) of their degree. Additionally, they may explore the overlap between different disciplines, creating further opportunities for interdisciplinary study."
  stem: none
  statementType: expectation
  rung: none
  force: will
  level: fheq:6
  appliesTo: "joint and combined honours students"
  addressee: learner
  verbs: ["achieve", "add", "explore"]
  about: "joint honours: core skills plus those of the other subject"
  themes: [none]
  domain: subject-skill
  award: ["bachelor's with honours"]
  gradeOf: none
  paraphrase: "Students on joint or combined honours will reach core elements of the subject and generic skills and add others from their other subject."
  quote: full   # the issuer's statement is in `source` (D-std-0014)
  audience: both
  subjects: inherited
- id: qaa/landscape-architecture-2024/2.15
  locator: { number: "2.15", headingPath: ["Distinctive features of Landscape Architecture courses", "Progression"] }
  span: { start: 31829, end: 32037 }
  source: "2.15 Eligibility to commence the Pathway to Chartership - the formal professional qualification route for Landscape Architects, requires an (LI accredited) master's degree of at least 180 credits at Level 7.\n"
  stem: none
  statementType: requirement
  rung: none
  force: must
  level: fheq:7
  appliesTo: "anyone starting the LI Pathway to Chartership"
  addressee: learner
  verbs: ["commence", "requires"]
  about: "the accredited master's for the chartership route"
  themes: [none]
  domain: none
  award: ["master's"]
  gradeOf: none
  paraphrase: "Starting the formal route to chartered status must begin from a master's the LI accredits, carrying 180 credits or more at level 7."
  quote: full   # the issuer's statement is in `source` (D-std-0014)
  audience: both
  subjects: inherited
- id: qaa/landscape-architecture-2024/2.21
  locator: { number: "2.21", headingPath: ["Distinctive features of Landscape Architecture courses", "Flexibility"] }
  span: { start: 33367, end: 33697 }
  source: "2.21 Prospective students should be aware that funding arrangements for study (including eligibility for fee and maintenance funds) will vary depending on the duration, mode of study and the country in which they study, and are advised to speak to the appropriate funding body and the institution before committing to a programme."
  stem: none
  statementType: expectation
  rung: none
  force: should
  level: none
  appliesTo: "prospective students"
  addressee: learner
  verbs: ["vary", "speak"]
  about: "checking funding before committing"
  themes: [none]
  domain: none
  award: ["none"]
  gradeOf: none
  paraphrase: "Prospective students should know funding varies with length, mode and country of study, and are advised to talk to the funding body and the institution first."
  quote: full   # the issuer's statement is in `source` (D-std-0014)
  audience: both
  subjects: inherited
- id: qaa/landscape-architecture-2024/2.26
  locator: { number: "2.26", headingPath: ["Distinctive features of Landscape Architecture courses", "Monitoring and review: Externality"] }
  span: { start: 35540, end: 35835 }
  source: "2.26 Externality is an essential component of the quality assurance system in the UK. Providers will use external reviewers as part of periodic review to gain an external perspective on any proposed changes and ensure threshold standards are achieved and content is appropriate for the subject.\n"
  stem: none
  statementType: expectation
  rung: none
  force: will
  level: none
  appliesTo: "providers in periodic review"
  addressee: provider
  verbs: ["use", "ensure"]
  about: "external reviewers in periodic review"
  themes: [none]
  domain: none
  award: ["none"]
  gradeOf: none
  paraphrase: "Providers will use external reviewers in periodic review to bring an outside view and make sure threshold standards are met and content fits the subject."
  quote: full   # the issuer's statement is in `source` (D-std-0014)
  audience: practitioner
  subjects: inherited
- id: qaa/landscape-architecture-2024/3.3
  locator: { number: "3.3", headingPath: ["Content, structure and delivery", "Teaching and learning"] }
  span: { start: 40268, end: 40846 }
  source: "3.3 All courses will employ a range of teaching techniques to impart key knowledge and skills, and stimulate/inspire personal learning, including, as appropriate, lectures, seminars, design exercises and workshops, site visits, tutorials, design charettes and group working. Landscape Architecture is characterised by an emphasis on a studio-based, collective learning culture, which forms the context for the application of newly acquired knowledge and skills in a progressive and integrated way, through a series of problem-solving projects of differing scale and complexity.\n"
  stem: none
  statementType: expectation
  rung: none
  force: will
  level: none
  appliesTo: "courses in the subject"
  addressee: provider
  verbs: ["employ", "impart", "stimulate/inspire"]
  about: "a range of teaching techniques and the design studio"
  themes: [none]
  domain: none
  award: ["none"]
  gradeOf: none
  paraphrase: "All courses will use a range of teaching methods; the subject is marked by a studio-based, shared learning culture with projects of rising scale and complexity."
  quote: full   # the issuer's statement is in `source` (D-std-0014)
  audience: practitioner
  subjects: inherited
- id: qaa/landscape-architecture-2024/3.9
  locator: { number: "3.9", headingPath: ["Content, structure and delivery", "Assessment"] }
  span: { start: 42693, end: 42794 }
  source: "3.9 Students at all levels of their degree study will experience formative and summative assessment.\n"
  stem: none
  statementType: expectation
  rung: none
  force: will
  level: none
  appliesTo: "students at every level of study"
  addressee: both
  verbs: ["experience"]
  about: "formative and summative assessment at all levels"
  themes: [none]
  domain: none
  award: ["none"]
  gradeOf: none
  paraphrase: "Students at every level will meet both formative and summative assessment."
  quote: full   # the issuer's statement is in `source` (D-std-0014)
  audience: both
  subjects: inherited
- id: qaa/landscape-architecture-2024/4.3
  locator: { number: "4.3", headingPath: ["Benchmark standards", "Introduction"] }
  span: { start: 47061, end: 47448 }
  source: "4.3 Each higher education provider has its own method of determining what appropriate evidence of this achievement will be and should refer to Annex D in The Frameworks for Higher Education Qualifications of UK Degree-Awarding Bodies. That Annex sets out common descriptions of the four main degree outcome classifications for bachelor's degrees with 1st, 2.1, 2.2 and 3rd class honours."
  stem: none
  statementType: requirement
  rung: none
  force: should
  level: fheq:6
  appliesTo: "providers judging achievement for the award"
  addressee: provider
  verbs: ["determining", "refer"]
  about: "providers refer to Annex D for evidence of achievement"
  themes: [none]
  domain: none
  award: ["bachelor's with honours"]
  gradeOf: none
  paraphrase: "Each provider decides what evidence shows achievement and should refer to Annex D of the Frameworks, which describes the four honours classifications."
  quote: full   # the issuer's statement is in `source` (D-std-0014)
  audience: practitioner
  subjects: inherited
- id: qaa/landscape-architecture-2024/4.4.b1
  locator: { number: "4.4.b1", headingPath: ["Benchmark standards", "Threshold level: Subject knowledge, understanding and skills"] }
  span: { start: 47715, end: 47791 }
  source: "analyse information, synthesising the outcomes to develop balanced arguments"
  stem: "4.4"
  statementType: threshold
  rung: threshold
  force: threshold
  level: fheq:6
  appliesTo: "honours graduates at the threshold"
  addressee: learner
  verbs: ["analyse", "synthesising", "develop"]
  about: "analysis and balanced argument"
  themes: [none]
  domain: generic-skill
  award: ["bachelor's with honours"]
  gradeOf: none
  paraphrase: "At threshold, can analyse information and draw its results together into a balanced case."
  quote: full   # the issuer's statement is in `source` (D-std-0014)
  audience: both
  subjects: inherited
- id: qaa/landscape-architecture-2024/4.4.b2
  locator: { number: "4.4.b2", headingPath: ["Benchmark standards", "Threshold level: Subject knowledge, understanding and skills"] }
  span: { start: 47794, end: 47859 }
  source: "demonstrate decision-making in complex and unpredictable contexts"
  stem: "4.4"
  statementType: threshold
  rung: threshold
  force: threshold
  level: fheq:6
  appliesTo: "honours graduates at the threshold"
  addressee: learner
  verbs: ["demonstrate"]
  about: "decisions in complex, unpredictable settings"
  themes: [none]
  domain: generic-skill
  award: ["bachelor's with honours"]
  gradeOf: none
  paraphrase: "At threshold, can show sound decision-making where situations are complex and hard to predict."
  quote: full   # the issuer's statement is in `source` (D-std-0014)
  audience: both
  subjects: inherited
- id: qaa/landscape-architecture-2024/4.4.b3
  locator: { number: "4.4.b3", headingPath: ["Benchmark standards", "Threshold level: Subject knowledge, understanding and skills"] }
  span: { start: 47862, end: 47964 }
  source: "apply critical thinking to develop an informed personal position as an aspiring landscape professional"
  stem: "4.4"
  statementType: threshold
  rung: threshold
  force: threshold
  level: fheq:6
  appliesTo: "honours graduates at the threshold"
  addressee: learner
  verbs: ["apply", "develop"]
  about: "critical thinking towards a professional position"
  themes: [none]
  domain: subject-skill
  award: ["bachelor's with honours"]
  gradeOf: none
  paraphrase: "At threshold, can think critically to reach an informed stance of their own as an emerging landscape professional."
  quote: full   # the issuer's statement is in `source` (D-std-0014)
  audience: both
  subjects: inherited
- id: qaa/landscape-architecture-2024/4.4.b4
  locator: { number: "4.4.b4", headingPath: ["Benchmark standards", "Threshold level: Subject knowledge, understanding and skills"] }
  span: { start: 47967, end: 48092 }
  source: "appreciate landscapes from the perspective of various stakeholders and integrate the needs of stakeholders into the proposals"
  stem: "4.4"
  statementType: threshold
  rung: threshold
  force: threshold
  level: fheq:6
  appliesTo: "honours graduates at the threshold"
  addressee: learner
  verbs: ["appreciate", "integrate"]
  about: "stakeholder perspectives in proposals"
  themes: [none]
  domain: subject-skill
  award: ["bachelor's with honours"]
  gradeOf: none
  paraphrase: "At threshold, can see a landscape as different stakeholders see it and build their needs into proposals."
  quote: full   # the issuer's statement is in `source` (D-std-0014)
  audience: both
  subjects: inherited
- id: qaa/landscape-architecture-2024/4.4.b5
  locator: { number: "4.4.b5", headingPath: ["Benchmark standards", "Threshold level: Subject knowledge, understanding and skills"] }
  span: { start: 48095, end: 48220 }
  source: "understand and allow for competing and alternative theories and priorities, to inform well-evidenced judgements and proposals"
  stem: "4.4"
  statementType: threshold
  rung: threshold
  force: threshold
  level: fheq:6
  appliesTo: "honours graduates at the threshold"
  addressee: learner
  verbs: ["understand", "allow", "inform"]
  about: "competing theories and priorities in judgement"
  themes: [none]
  domain: understanding
  award: ["bachelor's with honours"]
  gradeOf: none
  paraphrase: "At threshold, can understand and make room for rival theories and priorities so that judgements and proposals rest on good evidence."
  quote: full   # the issuer's statement is in `source` (D-std-0014)
  audience: both
  subjects: inherited
- id: qaa/landscape-architecture-2024/4.4.b6
  locator: { number: "4.4.b6", headingPath: ["Benchmark standards", "Threshold level: Subject knowledge, understanding and skills"] }
  span: { start: 48223, end: 48292 }
  source: "evaluate alternative proposals using appropriate tools and techniques"
  stem: "4.4"
  statementType: threshold
  rung: threshold
  force: threshold
  level: fheq:6
  appliesTo: "honours graduates at the threshold"
  addressee: learner
  verbs: ["evaluate", "using"]
  about: "evaluating alternative proposals"
  themes: [none]
  domain: subject-skill
  award: ["bachelor's with honours"]
  gradeOf: none
  paraphrase: "At threshold, can assess alternative proposals with suitable tools and techniques."
  quote: full   # the issuer's statement is in `source` (D-std-0014)
  audience: both
  subjects: inherited
- id: qaa/landscape-architecture-2024/4.4.b7
  locator: { number: "4.4.b7", headingPath: ["Benchmark standards", "Threshold level: Subject knowledge, understanding and skills"] }
  span: { start: 48295, end: 48436 }
  source: "formulate and interpret project briefs, identifying appropriate aims and objectives for familiar and unfamiliar problems at a range of scales"
  stem: "4.4"
  statementType: threshold
  rung: threshold
  force: threshold
  level: fheq:6
  appliesTo: "honours graduates at the threshold"
  addressee: learner
  verbs: ["formulate", "interpret", "identifying"]
  about: "project briefs and their aims"
  themes: [none]
  domain: subject-skill
  award: ["bachelor's with honours"]
  gradeOf: none
  paraphrase: "At threshold, can draft and read project briefs, setting suitable aims and objectives for known and new problems at varied scales."
  quote: full   # the issuer's statement is in `source` (D-std-0014)
  audience: both
  subjects: inherited
- id: qaa/landscape-architecture-2024/4.4.b8
  locator: { number: "4.4.b8", headingPath: ["Benchmark standards", "Threshold level: Subject knowledge, understanding and skills"] }
  span: { start: 48439, end: 48622 }
  source: "identify relevant theory, concepts, principles and techniques to generate appropriate policies, strategies, plans or practical interventions, at a range of spatial and temporal scales"
  stem: "4.4"
  statementType: threshold
  rung: threshold
  force: threshold
  level: fheq:6
  appliesTo: "honours graduates at the threshold"
  addressee: learner
  verbs: ["identify", "generate"]
  about: "from theory to policies, plans and interventions"
  themes: [none]
  domain: subject-skill
  award: ["bachelor's with honours"]
  gradeOf: none
  paraphrase: "At threshold, can pick the theory, concepts, principles and techniques that produce fitting policies, strategies, plans or interventions across scales of space and time."
  quote: full   # the issuer's statement is in `source` (D-std-0014)
  audience: both
  subjects: inherited
- id: qaa/landscape-architecture-2024/4.4.b9
  locator: { number: "4.4.b9", headingPath: ["Benchmark standards", "Threshold level: Subject knowledge, understanding and skills"] }
  span: { start: 48625, end: 48720 }
  source: "identify, research and apply knowledge to familiar and unfamiliar problems at a range of scales"
  stem: "4.4"
  statementType: threshold
  rung: threshold
  force: threshold
  level: fheq:6
  appliesTo: "honours graduates at the threshold"
  addressee: learner
  verbs: ["identify", "research", "apply"]
  about: "researching and applying knowledge to problems"
  themes: [none]
  domain: subject-skill
  award: ["bachelor's with honours"]
  gradeOf: none
  paraphrase: "At threshold, can find, research and use knowledge on known and new problems at a range of scales."
  quote: full   # the issuer's statement is in `source` (D-std-0014)
  audience: both
  subjects: inherited
- id: qaa/landscape-architecture-2024/4.4.b10
  locator: { number: "4.4.b10", headingPath: ["Benchmark standards", "Threshold level: Subject knowledge, understanding and skills"] }
  span: { start: 48727, end: 48904 }
  source: "appreciate and reflect on the ecosystem context of landscape-related projects and be able to formulate proposals which include the conservation and equilibrium of that ecosystem"
  stem: "4.4"
  statementType: threshold
  rung: threshold
  force: threshold
  level: fheq:6
  appliesTo: "honours graduates at the threshold"
  addressee: learner
  verbs: ["appreciate", "reflect", "formulate"]
  about: "the ecosystem context of projects"
  themes: [none]
  domain: subject-skill
  award: ["bachelor's with honours"]
  gradeOf: none
  paraphrase: "At threshold, can grasp and reflect on the ecosystem around a landscape project and frame proposals that conserve and balance it."
  quote: full   # the issuer's statement is in `source` (D-std-0014)
  audience: both
  subjects: inherited
- id: qaa/landscape-architecture-2024/4.4.b11
  locator: { number: "4.4.b11", headingPath: ["Benchmark standards", "Threshold level: Subject knowledge, understanding and skills"] }
  span: { start: 48907, end: 48969 }
  source: "demonstrate creativity and innovation in a sustainable context"
  stem: "4.4"
  statementType: threshold
  rung: threshold
  force: threshold
  level: fheq:6
  appliesTo: "honours graduates at the threshold"
  addressee: learner
  verbs: ["demonstrate"]
  about: "creativity and innovation for sustainability"
  themes: [none]
  domain: subject-skill
  award: ["bachelor's with honours"]
  gradeOf: none
  paraphrase: "At threshold, can show creativity and new ideas within a sustainable frame."
  quote: full   # the issuer's statement is in `source` (D-std-0014)
  audience: both
  subjects: inherited
- id: qaa/landscape-architecture-2024/4.4.b12
  locator: { number: "4.4.b12", headingPath: ["Benchmark standards", "Threshold level: Subject knowledge, understanding and skills"] }
  span: { start: 48972, end: 49052 }
  source: "plan and execute research, evaluating the outcomes and drawing valid conclusions"
  stem: "4.4"
  statementType: threshold
  rung: threshold
  force: threshold
  level: fheq:6
  appliesTo: "honours graduates at the threshold"
  addressee: learner
  verbs: ["plan", "execute", "evaluating", "drawing"]
  about: "planning and carrying out research"
  themes: [none]
  domain: generic-skill
  award: ["bachelor's with honours"]
  gradeOf: none
  paraphrase: "At threshold, can plan and conduct research, assess its results and reach sound conclusions."
  quote: full   # the issuer's statement is in `source` (D-std-0014)
  audience: both
  subjects: inherited
- id: qaa/landscape-architecture-2024/4.4.b13
  locator: { number: "4.4.b13", headingPath: ["Benchmark standards", "Threshold level: Subject knowledge, understanding and skills"] }
  span: { start: 49055, end: 49231 }
  source: "engage with secondary research sources, including the identification of appropriate supporting academic literature and reference sources in accordance with standard conventions"
  stem: "4.4"
  statementType: threshold
  rung: threshold
  force: threshold
  level: fheq:6
  appliesTo: "honours graduates at the threshold"
  addressee: learner
  verbs: ["engage"]
  about: "secondary sources and referencing"
  themes: [none]
  domain: generic-skill
  award: ["bachelor's with honours"]
  gradeOf: none
  paraphrase: "At threshold, can work with secondary research sources, finding suitable academic literature and citing it by standard conventions."
  quote: full   # the issuer's statement is in `source` (D-std-0014)
  audience: both
  subjects: inherited
- id: qaa/landscape-architecture-2024/4.4.b14
  locator: { number: "4.4.b14", headingPath: ["Benchmark standards", "Threshold level: Subject knowledge, understanding and skills"] }
  span: { start: 49234, end: 49301 }
  source: "understand where ethical, legal or data protection issues may arise"
  stem: "4.4"
  statementType: threshold
  rung: threshold
  force: threshold
  level: fheq:6
  appliesTo: "honours graduates at the threshold"
  addressee: learner
  verbs: ["understand", "arise"]
  about: "where ethical, legal or data issues arise"
  themes: [none]
  domain: understanding
  award: ["bachelor's with honours"]
  gradeOf: none
  paraphrase: "At threshold, can understand where questions of ethics, law or data protection may come up."
  quote: full   # the issuer's statement is in `source` (D-std-0014)
  audience: both
  subjects: inherited
- id: qaa/landscape-architecture-2024/4.4.b15
  locator: { number: "4.4.b15", headingPath: ["Benchmark standards", "Threshold level: Subject knowledge, understanding and skills"] }
  span: { start: 49304, end: 49395 }
  source: "understand the role and impact of intellectual property within creative design environments"
  stem: "4.4"
  statementType: threshold
  rung: threshold
  force: threshold
  level: fheq:6
  appliesTo: "honours graduates at the threshold"
  addressee: learner
  verbs: ["understand"]
  about: "intellectual property in design"
  themes: [none]
  domain: understanding
  award: ["bachelor's with honours"]
  gradeOf: none
  paraphrase: "At threshold, can understand what intellectual property is and how it affects creative design settings."
  quote: full   # the issuer's statement is in `source` (D-std-0014)
  audience: both
  subjects: inherited
- id: qaa/landscape-architecture-2024/4.4.b16
  locator: { number: "4.4.b16", headingPath: ["Benchmark standards", "Threshold level: Subject knowledge, understanding and skills"] }
  span: { start: 49398, end: 49468 }
  source: "identify, analyse and critique appropriate examples of precedent study"
  stem: "4.4"
  statementType: threshold
  rung: threshold
  force: threshold
  level: fheq:6
  appliesTo: "honours graduates at the threshold"
  addressee: learner
  verbs: ["identify", "analyse", "critique"]
  about: "precedent study"
  themes: [none]
  domain: subject-skill
  award: ["bachelor's with honours"]
  gradeOf: none
  paraphrase: "At threshold, can find, analyse and critique fitting precedents."
  quote: full   # the issuer's statement is in `source` (D-std-0014)
  audience: both
  subjects: inherited
- id: qaa/landscape-architecture-2024/4.4.b17
  locator: { number: "4.4.b17", headingPath: ["Benchmark standards", "Threshold level: Subject knowledge, understanding and skills"] }
  span: { start: 49471, end: 49558 }
  source: "identify and specify appropriate hard materials and vegetation for a range of proposals"
  stem: "4.4"
  statementType: threshold
  rung: threshold
  force: threshold
  level: fheq:6
  appliesTo: "honours graduates at the threshold"
  addressee: learner
  verbs: ["identify", "specify"]
  about: "specifying hard materials and planting"
  themes: [none]
  domain: subject-skill
  award: ["bachelor's with honours"]
  gradeOf: none
  paraphrase: "At threshold, can choose and specify suitable hard materials and planting for a range of proposals."
  quote: full   # the issuer's statement is in `source` (D-std-0014)
  audience: both
  subjects: inherited
- id: qaa/landscape-architecture-2024/4.4.b18
  locator: { number: "4.4.b18", headingPath: ["Benchmark standards", "Threshold level: Subject knowledge, understanding and skills"] }
  span: { start: 49561, end: 49698 }
  source: "understand the structural, performance and sustainability characteristics and the broad financial implications of material specification."
  stem: "4.4"
  statementType: threshold
  rung: threshold
  force: threshold
  level: fheq:6
  appliesTo: "honours graduates at the threshold"
  addressee: learner
  verbs: ["understand"]
  about: "material properties and cost"
  themes: [none]
  domain: knowledge
  award: ["bachelor's with honours"]
  gradeOf: none
  paraphrase: "At threshold, can understand how materials perform structurally and environmentally, and the broad cost of specifying them."
  quote: full   # the issuer's statement is in `source` (D-std-0014)
  audience: both
  subjects: inherited
- id: qaa/landscape-architecture-2024/4.4.b19
  locator: { number: "4.4.b19", headingPath: ["Benchmark standards", "Threshold level: Subject knowledge, understanding and skills"] }
  span: { start: 49763, end: 49881 }
  source: "identify appropriate geomatic information, namely the acquisition, modelling and analysis of spatially referenced data"
  stem: "4.4"
  statementType: threshold
  rung: threshold
  force: threshold
  level: fheq:6
  appliesTo: "honours graduates at the threshold"
  addressee: learner
  verbs: ["identify"]
  about: "geomatic information"
  themes: [none]
  domain: subject-skill
  award: ["bachelor's with honours"]
  gradeOf: none
  paraphrase: "At threshold, can identify suitable geomatic information: gathering, modelling and analysing data tied to location."
  quote: full   # the issuer's statement is in `source` (D-std-0014)
  audience: both
  subjects: inherited
- id: qaa/landscape-architecture-2024/4.4.b20
  locator: { number: "4.4.b20", headingPath: ["Benchmark standards", "Threshold level: Subject knowledge, understanding and skills"] }
  span: { start: 49884, end: 49972 }
  source: "identify and collate appropriate sources of evidence and make effective sample selection"
  stem: "4.4"
  statementType: threshold
  rung: threshold
  force: threshold
  level: fheq:6
  appliesTo: "honours graduates at the threshold"
  addressee: learner
  verbs: ["identify", "collate", "make"]
  about: "evidence sources and sampling"
  themes: [none]
  domain: subject-skill
  award: ["bachelor's with honours"]
  gradeOf: none
  paraphrase: "At threshold, can find and gather suitable sources of evidence and choose samples well."
  quote: full   # the issuer's statement is in `source` (D-std-0014)
  audience: both
  subjects: inherited
- id: qaa/landscape-architecture-2024/4.4.b21
  locator: { number: "4.4.b21", headingPath: ["Benchmark standards", "Threshold level: Subject knowledge, understanding and skills"] }
  span: { start: 49975, end: 50083 }
  source: "identify and apply the appropriate qualitative and/or quantitative techniques to the analysis of information"
  stem: "4.4"
  statementType: threshold
  rung: threshold
  force: threshold
  level: fheq:6
  appliesTo: "honours graduates at the threshold"
  addressee: learner
  verbs: ["identify", "apply"]
  about: "qualitative and quantitative analysis"
  themes: [none]
  domain: subject-skill
  award: ["bachelor's with honours"]
  gradeOf: none
  paraphrase: "At threshold, can choose and use fitting qualitative or quantitative techniques to analyse information."
  quote: full   # the issuer's statement is in `source` (D-std-0014)
  audience: both
  subjects: inherited
- id: qaa/landscape-architecture-2024/4.4.b22
  locator: { number: "4.4.b22", headingPath: ["Benchmark standards", "Threshold level: Subject knowledge, understanding and skills"] }
  span: { start: 50086, end: 50253 }
  source: "demonstrate appropriate levels of precision in the identification, recording and critical analysis of data in the field, laboratory or collation from secondary sources"
  stem: "4.4"
  statementType: threshold
  rung: threshold
  force: threshold
  level: fheq:6
  appliesTo: "honours graduates at the threshold"
  addressee: learner
  verbs: ["demonstrate"]
  about: "precision in recording and analysing data"
  themes: [none]
  domain: subject-skill
  award: ["bachelor's with honours"]
  gradeOf: none
  paraphrase: "At threshold, can show due precision when identifying, recording and critically analysing data from field, laboratory or secondary sources."
  quote: full   # the issuer's statement is in `source` (D-std-0014)
  audience: both
  subjects: inherited
- id: qaa/landscape-architecture-2024/4.4.b23
  locator: { number: "4.4.b23", headingPath: ["Benchmark standards", "Threshold level: Subject knowledge, understanding and skills"] }
  span: { start: 50256, end: 50343 }
  source: "prepare, process, interpret and present data, using appropriate techniques and software"
  stem: "4.4"
  statementType: threshold
  rung: threshold
  force: threshold
  level: fheq:6
  appliesTo: "honours graduates at the threshold"
  addressee: learner
  verbs: ["prepare", "process", "interpret", "present", "using"]
  about: "handling and presenting data with software"
  themes: [none]
  domain: subject-skill
  award: ["bachelor's with honours"]
  gradeOf: none
  paraphrase: "At threshold, can prepare, process, interpret and present data with suitable techniques and software."
  quote: full   # the issuer's statement is in `source` (D-std-0014)
  audience: both
  subjects: inherited
- id: qaa/landscape-architecture-2024/4.4.b24
  locator: { number: "4.4.b24", headingPath: ["Benchmark standards", "Threshold level: Subject knowledge, understanding and skills"] }
  span: { start: 50346, end: 50412 }
  source: "solve numerical problems using computer-based and other techniques"
  stem: "4.4"
  statementType: threshold
  rung: threshold
  force: threshold
  level: fheq:6
  appliesTo: "honours graduates at the threshold"
  addressee: learner
  verbs: ["solve", "using"]
  about: "numerical problem-solving"
  themes: [none]
  domain: generic-skill
  award: ["bachelor's with honours"]
  gradeOf: none
  paraphrase: "At threshold, can solve numerical problems with computer-based and other methods."
  quote: full   # the issuer's statement is in `source` (D-std-0014)
  audience: both
  subjects: inherited
- id: qaa/landscape-architecture-2024/4.4.b25
  locator: { number: "4.4.b25", headingPath: ["Benchmark standards", "Threshold level: Subject knowledge, understanding and skills"] }
  span: { start: 50415, end: 50561 }
  source: "identify, analyse and present financial information and use it in decision-making at a level appropriate to the nature and scale of the proposals."
  stem: "4.4"
  statementType: threshold
  rung: threshold
  force: threshold
  level: fheq:6
  appliesTo: "honours graduates at the threshold"
  addressee: learner
  verbs: ["identify", "analyse", "present", "use"]
  about: "financial information in decisions"
  themes: [none]
  domain: subject-skill
  award: ["bachelor's with honours"]
  gradeOf: none
  paraphrase: "At threshold, can find, analyse and present cost information and draw on it in decisions matched to the scale of the proposals."
  quote: full   # the issuer's statement is in `source` (D-std-0014)
  audience: both
  subjects: inherited
- id: qaa/landscape-architecture-2024/4.4.b26
  locator: { number: "4.4.b26", headingPath: ["Benchmark standards", "Threshold level: Subject knowledge, understanding and skills"] }
  span: { start: 50601, end: 50712 }
  source: "devise, plan and undertake desktop, field and studio investigations in a responsible, sensitive and safe manner"
  stem: "4.4"
  statementType: threshold
  rung: threshold
  force: threshold
  level: fheq:6
  appliesTo: "honours graduates at the threshold"
  addressee: learner
  verbs: ["devise", "plan", "undertake"]
  about: "safe desk, field and studio investigations"
  themes: [none]
  domain: subject-skill
  award: ["bachelor's with honours"]
  gradeOf: none
  paraphrase: "At threshold, can design, plan and carry out desk, field and studio investigations responsibly, sensitively and safely."
  quote: full   # the issuer's statement is in `source` (D-std-0014)
  audience: both
  subjects: inherited
- id: qaa/landscape-architecture-2024/4.4.b27
  locator: { number: "4.4.b27", headingPath: ["Benchmark standards", "Threshold level: Subject knowledge, understanding and skills"] }
  span: { start: 50715, end: 50892 }
  source: "understand and comply with rights of access and relevant health and safety requirements, including ethical considerations on research, working with people and in the environment"
  stem: "4.4"
  statementType: threshold
  rung: threshold
  force: threshold
  level: fheq:6
  appliesTo: "honours graduates at the threshold"
  addressee: learner
  verbs: ["understand", "comply"]
  about: "access rights, health and safety, research ethics"
  themes: [none]
  domain: subject-skill
  award: ["bachelor's with honours"]
  gradeOf: none
  paraphrase: "At threshold, can understand and keep to access rights and health and safety rules, with ethical care in research, with people and in the environment."
  quote: full   # the issuer's statement is in `source` (D-std-0014)
  audience: both
  subjects: inherited
- id: qaa/landscape-architecture-2024/4.4.b28
  locator: { number: "4.4.b28", headingPath: ["Benchmark standards", "Threshold level: Subject knowledge, understanding and skills"] }
  span: { start: 50895, end: 51008 }
  source: "demonstrate a clear and appropriate application of scale and proportion in the design or management of landscapes"
  stem: "4.4"
  statementType: threshold
  rung: threshold
  force: threshold
  level: fheq:6
  appliesTo: "honours graduates at the threshold"
  addressee: learner
  verbs: ["demonstrate"]
  about: "scale and proportion in design or management"
  themes: [none]
  domain: subject-skill
  award: ["bachelor's with honours"]
  gradeOf: none
  paraphrase: "At threshold, can show clear, fitting use of scale and proportion in designing or managing landscapes."
  quote: full   # the issuer's statement is in `source` (D-std-0014)
  audience: both
  subjects: inherited
- id: qaa/landscape-architecture-2024/4.4.b29
  locator: { number: "4.4.b29", headingPath: ["Benchmark standards", "Threshold level: Subject knowledge, understanding and skills"] }
  span: { start: 51011, end: 51225 }
  source: "in design subject areas, apply a practical and effective understanding of physical model-making skills, hand-drawing and other graphic representational skills to present proposals to professional and lay audiences."
  stem: "4.4"
  statementType: threshold
  rung: threshold
  force: threshold
  level: fheq:6
  appliesTo: "honours graduates at the threshold"
  addressee: learner
  verbs: ["apply", "present"]
  about: "models, hand drawing and graphics to present"
  themes: [none]
  domain: subject-skill
  award: ["bachelor's with honours"]
  gradeOf: none
  paraphrase: "At threshold, in design areas, can use model-making, hand drawing and other graphic skills to show proposals to expert and lay audiences."
  quote: full   # the issuer's statement is in `source` (D-std-0014)
  audience: both
  subjects: inherited
- id: qaa/landscape-architecture-2024/4.4.b30
  locator: { number: "4.4.b30", headingPath: ["Benchmark standards", "Threshold level: Subject knowledge, understanding and skills"] }
  span: { start: 51304, end: 51422 }
  source: "work effectively as an individual, using initiative, self-management, time and task management and personal reflection"
  stem: "4.4"
  statementType: threshold
  rung: threshold
  force: threshold
  level: fheq:6
  appliesTo: "honours graduates at the threshold"
  addressee: learner
  verbs: ["work", "using"]
  about: "working well as an individual"
  themes: [none]
  domain: generic-skill
  award: ["bachelor's with honours"]
  gradeOf: none
  paraphrase: "At threshold, can work well alone, showing initiative, managing self, time and tasks, and reflecting."
  quote: full   # the issuer's statement is in `source` (D-std-0014)
  audience: both
  subjects: inherited
- id: qaa/landscape-architecture-2024/4.4.b31
  locator: { number: "4.4.b31", headingPath: ["Benchmark standards", "Threshold level: Subject knowledge, understanding and skills"] }
  span: { start: 51425, end: 51471 }
  source: "identify individual goals and responsibilities"
  stem: "4.4"
  statementType: threshold
  rung: threshold
  force: threshold
  level: fheq:6
  appliesTo: "honours graduates at the threshold"
  addressee: learner
  verbs: ["identify"]
  about: "personal goals and responsibilities"
  themes: [none]
  domain: generic-skill
  award: ["bachelor's with honours"]
  gradeOf: none
  paraphrase: "At threshold, can name personal goals and responsibilities."
  quote: full   # the issuer's statement is in `source` (D-std-0014)
  audience: both
  subjects: inherited
- id: qaa/landscape-architecture-2024/4.4.b32
  locator: { number: "4.4.b32", headingPath: ["Benchmark standards", "Threshold level: Subject knowledge, understanding and skills"] }
  span: { start: 51474, end: 51571 }
  source: "set realistic targets and perform in a manner appropriate to allocated roles and responsibilities"
  stem: "4.4"
  statementType: threshold
  rung: threshold
  force: threshold
  level: fheq:6
  appliesTo: "honours graduates at the threshold"
  addressee: learner
  verbs: ["set", "perform"]
  about: "targets and allocated roles"
  themes: [none]
  domain: generic-skill
  award: ["bachelor's with honours"]
  gradeOf: none
  paraphrase: "At threshold, can set realistic targets and act as allocated roles and responsibilities require."
  quote: full   # the issuer's statement is in `source` (D-std-0014)
  audience: both
  subjects: inherited
- id: qaa/landscape-architecture-2024/4.4.b33
  locator: { number: "4.4.b33", headingPath: ["Benchmark standards", "Threshold level: Subject knowledge, understanding and skills"] }
  span: { start: 51574, end: 51619 }
  source: "reflect on and evaluate their own performance"
  stem: "4.4"
  statementType: threshold
  rung: threshold
  force: threshold
  level: fheq:6
  appliesTo: "honours graduates at the threshold"
  addressee: learner
  verbs: ["reflect", "evaluate"]
  about: "reflecting on own performance"
  themes: [none]
  domain: generic-skill
  award: ["bachelor's with honours"]
  gradeOf: none
  paraphrase: "At threshold, can reflect on and judge their own performance."
  quote: full   # the issuer's statement is in `source` (D-std-0014)
  audience: both
  subjects: inherited
- id: qaa/landscape-architecture-2024/4.4.b34
  locator: { number: "4.4.b34", headingPath: ["Benchmark standards", "Threshold level: Subject knowledge, understanding and skills"] }
  span: { start: 51622, end: 51682 }
  source: "develop an adaptable and flexible approach to study and work"
  stem: "4.4"
  statementType: threshold
  rung: threshold
  force: threshold
  level: fheq:6
  appliesTo: "honours graduates at the threshold"
  addressee: learner
  verbs: ["develop"]
  about: "adaptable approach to study and work"
  themes: [none]
  domain: generic-skill
  award: ["bachelor's with honours"]
  gradeOf: none
  paraphrase: "At threshold, can build an adaptable, flexible way of studying and working."
  quote: full   # the issuer's statement is in `source` (D-std-0014)
  audience: both
  subjects: inherited
- id: qaa/landscape-architecture-2024/4.4.b35
  locator: { number: "4.4.b35", headingPath: ["Benchmark standards", "Threshold level: Subject knowledge, understanding and skills"] }
  span: { start: 51685, end: 51794 }
  source: "develop effective time-management and organisational skills, including the planning and execution of workload"
  stem: "4.4"
  statementType: threshold
  rung: threshold
  force: threshold
  level: fheq:6
  appliesTo: "honours graduates at the threshold"
  addressee: learner
  verbs: ["develop"]
  about: "time management and organisation"
  themes: [none]
  domain: generic-skill
  award: ["bachelor's with honours"]
  gradeOf: none
  paraphrase: "At threshold, can build good time management and organisation, planning and carrying out a workload."
  quote: full   # the issuer's statement is in `source` (D-std-0014)
  audience: both
  subjects: inherited
- id: qaa/landscape-architecture-2024/4.4.b36
  locator: { number: "4.4.b36", headingPath: ["Benchmark standards", "Threshold level: Subject knowledge, understanding and skills"] }
  span: { start: 51797, end: 51928 }
  source: "demonstrate the competence, behaviour and attitude required in the profession and with reference to equity, diversity and inclusion"
  stem: "4.4"
  statementType: threshold
  rung: threshold
  force: threshold
  level: fheq:6
  appliesTo: "honours graduates at the threshold"
  addressee: learner
  verbs: ["demonstrate"]
  about: "professional competence and conduct, with EDI"
  themes: [none]
  domain: generic-skill
  award: ["bachelor's with honours"]
  gradeOf: none
  paraphrase: "At threshold, can show the competence, behaviour and attitude the profession needs, with regard to equity, diversity and inclusion."
  quote: full   # the issuer's statement is in `source` (D-std-0014)
  audience: both
  subjects: inherited
- id: qaa/landscape-architecture-2024/4.4.b37
  locator: { number: "4.4.b37", headingPath: ["Benchmark standards", "Threshold level: Subject knowledge, understanding and skills"] }
  span: { start: 51931, end: 52007 }
  source: "recognise, respect and work within appropriate professional codes of conduct"
  stem: "4.4"
  statementType: threshold
  rung: threshold
  force: threshold
  level: fheq:6
  appliesTo: "honours graduates at the threshold"
  addressee: learner
  verbs: ["recognise", "respect", "work"]
  about: "professional codes of conduct"
  themes: [none]
  domain: generic-skill
  award: ["bachelor's with honours"]
  gradeOf: none
  paraphrase: "At threshold, can recognise, respect and keep within fitting professional codes of conduct."
  quote: full   # the issuer's statement is in `source` (D-std-0014)
  audience: both
  subjects: inherited
- id: qaa/landscape-architecture-2024/4.4.b38
  locator: { number: "4.4.b38", headingPath: ["Benchmark standards", "Threshold level: Subject knowledge, understanding and skills"] }
  span: { start: 52010, end: 52103 }
  source: "recognise and respect the moral, ethical, ecological and social issues related to the subject"
  stem: "4.4"
  statementType: threshold
  rung: threshold
  force: threshold
  level: fheq:6
  appliesTo: "honours graduates at the threshold"
  addressee: learner
  verbs: ["recognise", "respect"]
  about: "moral, ethical, ecological and social issues"
  themes: [none]
  domain: generic-skill
  award: ["bachelor's with honours"]
  gradeOf: none
  paraphrase: "At threshold, can recognise and respect the moral, ethical, social and ecological questions the subject raises."
  quote: full   # the issuer's statement is in `source` (D-std-0014)
  audience: both
  subjects: inherited
- id: qaa/landscape-architecture-2024/4.4.b39
  locator: { number: "4.4.b39", headingPath: ["Benchmark standards", "Threshold level: Subject knowledge, understanding and skills"] }
  span: { start: 52106, end: 52260 }
  source: "develop and display the generic skills required to acquire new competencies for employability, career progression and continuing professional development."
  stem: "4.4"
  statementType: threshold
  rung: threshold
  force: threshold
  level: fheq:6
  appliesTo: "honours graduates at the threshold"
  addressee: learner
  verbs: ["develop", "display", "acquire"]
  about: "generic skills for employability and CPD"
  themes: [none]
  domain: generic-skill
  award: ["bachelor's with honours"]
  gradeOf: none
  paraphrase: "At threshold, can build and show the generic skills needed to gain new competences for work, career growth and continuing professional development."
  quote: full   # the issuer's statement is in `source` (D-std-0014)
  audience: both
  subjects: inherited
- id: qaa/landscape-architecture-2024/4.4.b40
  locator: { number: "4.4.b40", headingPath: ["Benchmark standards", "Threshold level: Subject knowledge, understanding and skills"] }
  span: { start: 52307, end: 52442 }
  source: "identify and apply hardware and software appropriate to the scale of work, to communicate proposals effectively to a range of audiences"
  stem: "4.4"
  statementType: threshold
  rung: threshold
  force: threshold
  level: fheq:6
  appliesTo: "honours graduates at the threshold"
  addressee: learner
  verbs: ["identify", "apply", "communicate"]
  about: "hardware and software to communicate"
  themes: [none]
  domain: generic-skill
  award: ["bachelor's with honours"]
  gradeOf: none
  paraphrase: "At threshold, can choose and use hardware and software suited to the scale of the work to communicate proposals well to different audiences."
  quote: full   # the issuer's statement is in `source` (D-std-0014)
  audience: both
  subjects: inherited
- id: qaa/landscape-architecture-2024/4.4.b41
  locator: { number: "4.4.b41", headingPath: ["Benchmark standards", "Threshold level: Subject knowledge, understanding and skills"] }
  span: { start: 52445, end: 52550 }
  source: "appropriately use the internet and social media, as a means of communication and a source of information."
  stem: "4.4"
  statementType: threshold
  rung: threshold
  force: threshold
  level: fheq:6
  appliesTo: "honours graduates at the threshold"
  addressee: learner
  verbs: ["use"]
  about: "internet and social media"
  themes: [none]
  domain: generic-skill
  award: ["bachelor's with honours"]
  gradeOf: none
  paraphrase: "At threshold, can use the internet and social media fittingly, to communicate and to find information."
  quote: full   # the issuer's statement is in `source` (D-std-0014)
  audience: both
  subjects: inherited
- id: qaa/landscape-architecture-2024/4.4.b42
  locator: { number: "4.4.b42", headingPath: ["Benchmark standards", "Threshold level: Subject knowledge, understanding and skills"] }
  span: { start: 52553, end: 52648 }
  source: "have an awareness of emerging technologies and effective and appropriate ways to implement them"
  stem: "4.4"
  statementType: threshold
  rung: threshold
  force: threshold
  level: fheq:6
  appliesTo: "honours graduates at the threshold"
  addressee: learner
  verbs: ["have", "implement"]
  about: "awareness of emerging technologies"
  themes: [none]
  domain: generic-skill
  award: ["bachelor's with honours"]
  gradeOf: none
  paraphrase: "At threshold, can show awareness of new technologies and of good, fitting ways to put them to use."
  quote: full   # the issuer's statement is in `source` (D-std-0014)
  audience: both
  subjects: inherited
- id: qaa/landscape-architecture-2024/4.4.b43
  locator: { number: "4.4.b43", headingPath: ["Benchmark standards", "Threshold level: Subject knowledge, understanding and skills"] }
  span: { start: 52651, end: 53522 }
  source: "effectively apply suitable technology in an appropriate and legal way for the production of work at various stages of the survey, analysis and design processes; including, for example, but not exclusively: − computer aided drafting (CAD) − visualisation and image manipulation − digital model making − geographic information systems (GIS) − building information modelling (BIM) − computer-based processing, including, for example, National Building Specification − data processing − CAD/CAM/CNC for model making, 3D printing and laser cutting − artificial intelligence (AI), including generative text and images − spatial computing, for example augmented reality (AR) / virtual reality (VR) − drones, for example site mapping and plant species identification − smartphone applications, including, for example, plant identification and other applications for site surveys."
  stem: "4.4"
  statementType: threshold
  rung: threshold
  force: threshold
  level: fheq:6
  appliesTo: "honours graduates at the threshold"
  addressee: learner
  verbs: ["apply"]
  about: "digital tools across survey, analysis and design"
  themes: [none]
  domain: subject-skill
  award: ["bachelor's with honours"]
  gradeOf: none
  paraphrase: "At threshold, can use suitable technology lawfully and well at each stage of survey, analysis and design, from CAD, GIS and BIM to drones, AI and spatial computing."
  quote: full   # the issuer's statement is in `source` (D-std-0014)
  audience: both
  subjects: inherited
- id: qaa/landscape-architecture-2024/4.4.b44
  locator: { number: "4.4.b44", headingPath: ["Benchmark standards", "Threshold level: Subject knowledge, understanding and skills"] }
  span: { start: 53566, end: 53703 }
  source: "identify and engage with the various and diverse stakeholders at appropriate stages of projects to test and inform research and proposals"
  stem: "4.4"
  statementType: threshold
  rung: threshold
  force: threshold
  level: fheq:6
  appliesTo: "honours graduates at the threshold"
  addressee: learner
  verbs: ["identify", "engage", "test", "inform"]
  about: "engaging diverse stakeholders"
  themes: [none]
  domain: subject-skill
  award: ["bachelor's with honours"]
  gradeOf: none
  paraphrase: "At threshold, can find and involve the many different stakeholders at the right stages of a project to test and shape research and proposals."
  quote: full   # the issuer's statement is in `source` (D-std-0014)
  audience: both
  subjects: inherited
- id: qaa/landscape-architecture-2024/4.4.b45
  locator: { number: "4.4.b45", headingPath: ["Benchmark standards", "Threshold level: Subject knowledge, understanding and skills"] }
  span: { start: 53710, end: 53845 }
  source: "understand, select and apply approaches, tools and techniques appropriate to the audience and the material being communicated/presented"
  stem: "4.4"
  statementType: threshold
  rung: threshold
  force: threshold
  level: fheq:6
  appliesTo: "honours graduates at the threshold"
  addressee: learner
  verbs: ["understand", "select", "apply"]
  about: "choosing communication methods for the audience"
  themes: [none]
  domain: generic-skill
  award: ["bachelor's with honours"]
  gradeOf: none
  paraphrase: "At threshold, can understand, choose and use approaches, tools and techniques that suit the audience and the material."
  quote: full   # the issuer's statement is in `source` (D-std-0014)
  audience: both
  subjects: inherited
- id: qaa/landscape-architecture-2024/4.4.b46
  locator: { number: "4.4.b46", headingPath: ["Benchmark standards", "Threshold level: Subject knowledge, understanding and skills"] }
  span: { start: 53848, end: 54050 }
  source: "ensure communications approaches and methods are inclusive and accessible to as diverse a range of people as possible, particularly where stakeholders include minority groups or those with diverse needs"
  stem: "4.4"
  statementType: threshold
  rung: threshold
  force: threshold
  level: fheq:6
  appliesTo: "honours graduates at the threshold"
  addressee: learner
  verbs: ["ensure"]
  about: "inclusive, accessible communication"
  themes: [none]
  domain: generic-skill
  award: ["bachelor's with honours"]
  gradeOf: none
  paraphrase: "At threshold, can make sure communication is inclusive and accessible to as many people as possible, above all where stakeholders include minorities or people with varied needs."
  quote: full   # the issuer's statement is in `source` (D-std-0014)
  audience: both
  subjects: inherited
- id: qaa/landscape-architecture-2024/4.4.b47
  locator: { number: "4.4.b47", headingPath: ["Benchmark standards", "Threshold level: Subject knowledge, understanding and skills"] }
  span: { start: 54053, end: 54268 }
  source: "communicate clearly, concisely, confidently and appropriately to a range of audiences in written, verbal and graphical forms, including the use of physical and digital models and other digital and other visual media"
  stem: "4.4"
  statementType: threshold
  rung: threshold
  force: threshold
  level: fheq:6
  appliesTo: "honours graduates at the threshold"
  addressee: learner
  verbs: ["communicate"]
  about: "clear communication in many forms"
  themes: [none]
  domain: generic-skill
  award: ["bachelor's with honours"]
  gradeOf: none
  paraphrase: "At threshold, can communicate clearly, briefly, confidently and fittingly to varied audiences in writing, speech and graphics, including physical and digital models."
  quote: full   # the issuer's statement is in `source` (D-std-0014)
  audience: both
  subjects: inherited
- id: qaa/landscape-architecture-2024/4.4.b48
  locator: { number: "4.4.b48", headingPath: ["Benchmark standards", "Threshold level: Subject knowledge, understanding and skills"] }
  span: { start: 54271, end: 54439 }
  source: "communicate accurately where possible and, where not (for example in the production of illustrative graphic communications) be clear on the limitations of these outputs"
  stem: "4.4"
  statementType: threshold
  rung: threshold
  force: threshold
  level: fheq:6
  appliesTo: "honours graduates at the threshold"
  addressee: learner
  verbs: ["communicate"]
  about: "accuracy and the limits of illustrative graphics"
  themes: [none]
  domain: generic-skill
  award: ["bachelor's with honours"]
  gradeOf: none
  paraphrase: "At threshold, can communicate accurately where possible and, where not, as with illustrative graphics, be open about the limits of the output."
  quote: full   # the issuer's statement is in `source` (D-std-0014)
  audience: both
  subjects: inherited
- id: qaa/landscape-architecture-2024/4.4.b49
  locator: { number: "4.4.b49", headingPath: ["Benchmark standards", "Threshold level: Subject knowledge, understanding and skills"] }
  span: { start: 54442, end: 54640 }
  source: "explore and capitalise on emerging digital tools (such as AI) in the preparation of communication materials and presentation while ensuring the appropriateness and accuracy of the outputs generated."
  stem: "4.4"
  statementType: threshold
  rung: threshold
  force: threshold
  level: fheq:6
  appliesTo: "honours graduates at the threshold"
  addressee: learner
  verbs: ["explore", "capitalise", "ensuring"]
  about: "AI and emerging tools in communication"
  themes: [none]
  domain: generic-skill
  award: ["bachelor's with honours"]
  gradeOf: none
  paraphrase: "At threshold, can try out and make use of new digital tools such as AI in preparing communication and presentations, while checking the outputs are fit and accurate."
  quote: full   # the issuer's statement is in `source` (D-std-0014)
  audience: both
  subjects: inherited
- id: qaa/landscape-architecture-2024/4.4.b50
  locator: { number: "4.4.b50", headingPath: ["Benchmark standards", "Threshold level: Subject knowledge, understanding and skills"] }
  span: { start: 54697, end: 54838 }
  source: "contribute confidently and effectively to the identification and setting of group aims and objectives and allocations of roles within a group"
  stem: "4.4"
  statementType: threshold
  rung: threshold
  force: threshold
  level: fheq:6
  appliesTo: "honours graduates at the threshold"
  addressee: learner
  verbs: ["contribute"]
  about: "setting group aims and roles"
  themes: [none]
  domain: generic-skill
  award: ["bachelor's with honours"]
  gradeOf: none
  paraphrase: "At threshold, can help confidently and well to set a group's aims, objectives and roles."
  quote: full   # the issuer's statement is in `source` (D-std-0014)
  audience: both
  subjects: inherited
- id: qaa/landscape-architecture-2024/4.4.b51
  locator: { number: "4.4.b51", headingPath: ["Benchmark standards", "Threshold level: Subject knowledge, understanding and skills"] }
  span: { start: 54841, end: 55046 }
  source: "contribute constructively and sensitively to group discussions, demonstrating the ability to consider, appreciate, respect and evaluate the views of others, particularly those with diverse life experiences"
  stem: "4.4"
  statementType: threshold
  rung: threshold
  force: threshold
  level: fheq:6
  appliesTo: "honours graduates at the threshold"
  addressee: learner
  verbs: ["contribute", "demonstrating", "consider", "appreciate", "respect", "evaluate"]
  about: "respectful group discussion"
  themes: [none]
  domain: generic-skill
  award: ["bachelor's with honours"]
  gradeOf: none
  paraphrase: "At threshold, can take part constructively and sensitively in group discussion, weighing and respecting others' views, especially those of people with varied life experience."
  quote: full   # the issuer's statement is in `source` (D-std-0014)
  audience: both
  subjects: inherited
- id: qaa/landscape-architecture-2024/4.4.b52
  locator: { number: "4.4.b52", headingPath: ["Benchmark standards", "Threshold level: Subject knowledge, understanding and skills"] }
  span: { start: 55049, end: 55185 }
  source: "apply knowledge, critical thinking and understanding to address multidisciplinary problems and provide comprehensive, holistic solutions"
  stem: "4.4"
  statementType: threshold
  rung: threshold
  force: threshold
  level: fheq:6
  appliesTo: "honours graduates at the threshold"
  addressee: learner
  verbs: ["apply", "address", "provide"]
  about: "multidisciplinary problems and holistic solutions"
  themes: [none]
  domain: generic-skill
  award: ["bachelor's with honours"]
  gradeOf: none
  paraphrase: "At threshold, can bring knowledge, critical thought and understanding to multidisciplinary problems and offer complete, joined-up solutions."
  quote: full   # the issuer's statement is in `source` (D-std-0014)
  audience: both
  subjects: inherited
- id: qaa/landscape-architecture-2024/4.4.b53
  locator: { number: "4.4.b53", headingPath: ["Benchmark standards", "Threshold level: Subject knowledge, understanding and skills"] }
  span: { start: 55188, end: 55282 }
  source: "contribute effectively to the production of group outputs, including reports and presentations"
  stem: "4.4"
  statementType: threshold
  rung: threshold
  force: threshold
  level: fheq:6
  appliesTo: "honours graduates at the threshold"
  addressee: learner
  verbs: ["contribute"]
  about: "contributing to group outputs"
  themes: [none]
  domain: generic-skill
  award: ["bachelor's with honours"]
  gradeOf: none
  paraphrase: "At threshold, can contribute well to a group's outputs, such as reports and presentations."
  quote: full   # the issuer's statement is in `source` (D-std-0014)
  audience: both
  subjects: inherited
- id: qaa/landscape-architecture-2024/4.4.b54
  locator: { number: "4.4.b54", headingPath: ["Benchmark standards", "Threshold level: Subject knowledge, understanding and skills"] }
  span: { start: 55285, end: 55347 }
  source: "demonstrate the ability to lead a group in a range of projects"
  stem: "4.4"
  statementType: threshold
  rung: threshold
  force: threshold
  level: fheq:6
  appliesTo: "honours graduates at the threshold"
  addressee: learner
  verbs: ["demonstrate", "lead"]
  about: "leading a group"
  themes: [none]
  domain: generic-skill
  award: ["bachelor's with honours"]
  gradeOf: none
  paraphrase: "At threshold, can show the ability to lead a group across a range of projects."
  quote: full   # the issuer's statement is in `source` (D-std-0014)
  audience: both
  subjects: inherited
- id: qaa/landscape-architecture-2024/4.4.b55
  locator: { number: "4.4.b55", headingPath: ["Benchmark standards", "Threshold level: Subject knowledge, understanding and skills"] }
  span: { start: 55350, end: 55431 }
  source: "demonstrate the ability to be led, as part of a group, within a range of projects"
  stem: "4.4"
  statementType: threshold
  rung: threshold
  force: threshold
  level: fheq:6
  appliesTo: "honours graduates at the threshold"
  addressee: learner
  verbs: ["demonstrate", "led"]
  about: "being led within a group"
  themes: [none]
  domain: generic-skill
  award: ["bachelor's with honours"]
  gradeOf: none
  paraphrase: "At threshold, can show the ability to be led as a group member across a range of projects."
  quote: full   # the issuer's statement is in `source` (D-std-0014)
  audience: both
  subjects: inherited
- id: qaa/landscape-architecture-2024/4.4.b56
  locator: { number: "4.4.b56", headingPath: ["Benchmark standards", "Threshold level: Subject knowledge, understanding and skills"] }
  span: { start: 55434, end: 55565 }
  source: "demonstrate an awareness of the interdisciplinary nature and processes involved in community engagement and consultation exercises."
  stem: "4.4"
  statementType: threshold
  rung: threshold
  force: threshold
  level: fheq:6
  appliesTo: "honours graduates at the threshold"
  addressee: learner
  verbs: ["demonstrate"]
  about: "community engagement and consultation"
  themes: [none]
  domain: understanding
  award: ["bachelor's with honours"]
  gradeOf: none
  paraphrase: "At threshold, can show awareness of the interdisciplinary character and processes of community engagement and consultation."
  quote: full   # the issuer's statement is in `source` (D-std-0014)
  audience: both
  subjects: inherited
- id: qaa/landscape-architecture-2024/4.5.b1
  locator: { number: "4.5.b1", headingPath: ["Benchmark standards", "Typical standard"] }
  span: { start: 55724, end: 55889 }
  source: "achieved all their required course learning outcomes and consistently demonstrated advanced knowledge and understanding, cognitive, practical and transferable skills"
  stem: "4.5"
  statementType: typical
  rung: typical
  force: describes
  level: fheq:6
  appliesTo: "honours graduates at the typical standard"
  addressee: learner
  verbs: ["achieved", "demonstrated"]
  about: "all outcomes met, with advanced knowledge and skills"
  themes: [none]
  domain: knowledge
  award: ["bachelor's with honours"]
  gradeOf: none
  paraphrase: "At the typical standard, has met every required course outcome and shown advanced knowledge, understanding and cognitive, practical and transferable skills consistently."
  quote: full   # the issuer's statement is in `source` (D-std-0014)
  audience: both
  subjects: inherited
- id: qaa/landscape-architecture-2024/4.5.b2
  locator: { number: "4.5.b2", headingPath: ["Benchmark standards", "Typical standard"] }
  span: { start: 55892, end: 56048 }
  source: "an understanding and application of the knowledge, understanding and skills listed above with more critical reflection, personal responsibility and autonomy"
  stem: "4.5"
  statementType: typical
  rung: typical
  force: describes
  level: fheq:6
  appliesTo: "honours graduates at the typical standard"
  addressee: learner
  verbs: []
  about: "more critical reflection, responsibility and autonomy"
  themes: [none]
  domain: generic-skill
  award: ["bachelor's with honours"]
  gradeOf: none
  paraphrase: "At the typical standard, applies the threshold knowledge, understanding and skills with more critical reflection, personal responsibility and autonomy."
  quote: full   # the issuer's statement is in `source` (D-std-0014)
  audience: both
  subjects: inherited
- id: qaa/landscape-architecture-2024/4.5.b3
  locator: { number: "4.5.b3", headingPath: ["Benchmark standards", "Typical standard"] }
  span: { start: 56051, end: 56279 }
  source: "demonstrated effective and appropriate application and execution of the knowledge, understanding and skills listed above, showing more insight, initiative, strong problem- solving ability and creativity in addressing their work."
  stem: "4.5"
  statementType: typical
  rung: typical
  force: describes
  level: fheq:6
  appliesTo: "honours graduates at the typical standard"
  addressee: learner
  verbs: ["demonstrated", "showing", "addressing"]
  about: "more insight, initiative, problem-solving and creativity"
  themes: [none]
  domain: subject-skill
  award: ["bachelor's with honours"]
  gradeOf: none
  paraphrase: "At the typical standard, applies and carries out the threshold knowledge and skills well and fittingly, with more insight, initiative, strong problem-solving and creativity."
  quote: full   # the issuer's statement is in `source` (D-std-0014)
  audience: both
  subjects: inherited
- id: qaa/landscape-architecture-2024/4.6.b1
  locator: { number: "4.6.b1", headingPath: ["Benchmark standards", "Excellent standard"] }
  span: { start: 56447, end: 56597 }
  source: "achieved all their required course learning outcomes and demonstrated strong knowledge and understanding, cognitive, practical and transferable skills"
  stem: "4.6"
  statementType: excellent
  rung: excellent
  force: describes
  level: fheq:6
  appliesTo: "honours graduates at the excellent standard"
  addressee: learner
  verbs: ["achieved", "demonstrated"]
  about: "all outcomes met, with strong knowledge and skills"
  themes: [none]
  domain: knowledge
  award: ["bachelor's with honours"]
  gradeOf: { statement: qaa/landscape-architecture-2024/4.5.b1, basis: inferred }
  paraphrase: "At the excellent standard, has met every required course outcome and shown strong knowledge, understanding and cognitive, practical and transferable skills."
  quote: full   # the issuer's statement is in `source` (D-std-0014)
  audience: both
  subjects: inherited
- id: qaa/landscape-architecture-2024/4.6.b2
  locator: { number: "4.6.b2", headingPath: ["Benchmark standards", "Excellent standard"] }
  span: { start: 56600, end: 56853 }
  source: "an understanding and application of the knowledge, understanding and skills listed above with a higher level of originality, independent critical reflection, personal responsibility, autonomy and leadership and a clear professional and ethical awareness"
  stem: "4.6"
  statementType: excellent
  rung: excellent
  force: describes
  level: fheq:6
  appliesTo: "honours graduates at the excellent standard"
  addressee: learner
  verbs: []
  about: "originality, independent reflection, leadership and ethics"
  themes: [none]
  domain: generic-skill
  award: ["bachelor's with honours"]
  gradeOf: { statement: qaa/landscape-architecture-2024/4.5.b2, basis: inferred }
  paraphrase: "At the excellent standard, applies the threshold knowledge and skills with more originality, independent critical reflection, responsibility, autonomy and leadership, and clear professional and ethical awareness."
  quote: full   # the issuer's statement is in `source` (D-std-0014)
  audience: both
  subjects: inherited
- id: qaa/landscape-architecture-2024/4.6.b3
  locator: { number: "4.6.b3", headingPath: ["Benchmark standards", "Excellent standard"] }
  span: { start: 56856, end: 57106 }
  source: "demonstrated effective, fluent and appropriate application and execution of the knowledge, understanding and skills listed above, showing higher levels of originality, insight, novel approaches, with exceptional initiative and problem-solving skills."
  stem: "4.6"
  statementType: excellent
  rung: excellent
  force: describes
  level: fheq:6
  appliesTo: "honours graduates at the excellent standard"
  addressee: learner
  verbs: ["demonstrated", "showing"]
  about: "fluent application with originality and exceptional initiative"
  themes: [none]
  domain: subject-skill
  award: ["bachelor's with honours"]
  gradeOf: { statement: qaa/landscape-architecture-2024/4.5.b3, basis: inferred }
  paraphrase: "At the excellent standard, applies and carries out the threshold knowledge and skills fluently and well, with more originality, insight, new approaches, exceptional initiative and problem-solving."
  quote: full   # the issuer's statement is in `source` (D-std-0014)
  audience: both
  subjects: inherited
- id: qaa/landscape-architecture-2024/4.7.b1
  locator: { number: "4.7.b1", headingPath: ["Benchmark standards", "Master's degrees"] }
  span: { start: 57242, end: 57277 }
  source: "a questioning and critical approach"
  stem: "4.7"
  statementType: threshold
  rung: threshold
  force: will
  level: fheq:7
  appliesTo: "master's graduates at the threshold"
  addressee: learner
  verbs: []
  about: "a questioning, critical approach"
  themes: [none]
  domain: generic-skill
  award: ["master's"]
  gradeOf: none
  paraphrase: "A master's graduate at threshold will also show a questioning, critical approach."
  quote: full   # the issuer's statement is in `source` (D-std-0014)
  audience: both
  subjects: inherited
- id: qaa/landscape-architecture-2024/4.7.b2
  locator: { number: "4.7.b2", headingPath: ["Benchmark standards", "Master's degrees"] }
  span: { start: 57280, end: 57314 }
  source: "a capacity for critical reflection"
  stem: "4.7"
  statementType: threshold
  rung: threshold
  force: will
  level: fheq:7
  appliesTo: "master's graduates at the threshold"
  addressee: learner
  verbs: []
  about: "capacity for critical reflection"
  themes: [none]
  domain: generic-skill
  award: ["master's"]
  gradeOf: none
  paraphrase: "A master's graduate at threshold will also show the capacity to reflect critically."
  quote: full   # the issuer's statement is in `source` (D-std-0014)
  audience: both
  subjects: inherited
- id: qaa/landscape-architecture-2024/4.7.b3
  locator: { number: "4.7.b3", headingPath: ["Benchmark standards", "Master's degrees"] }
  span: { start: 57317, end: 57363 }
  source: "a capacity for independent thinking and action"
  stem: "4.7"
  statementType: threshold
  rung: threshold
  force: will
  level: fheq:7
  appliesTo: "master's graduates at the threshold"
  addressee: learner
  verbs: []
  about: "independent thinking and action"
  themes: [none]
  domain: generic-skill
  award: ["master's"]
  gradeOf: none
  paraphrase: "A master's graduate at threshold will also show the capacity to think and act independently."
  quote: full   # the issuer's statement is in `source` (D-std-0014)
  audience: both
  subjects: inherited
- id: qaa/landscape-architecture-2024/4.7.b4
  locator: { number: "4.7.b4", headingPath: ["Benchmark standards", "Master's degrees"] }
  span: { start: 57366, end: 57428 }
  source: "a higher level of originality, insight and critical reflection"
  stem: "4.7"
  statementType: threshold
  rung: threshold
  force: will
  level: fheq:7
  appliesTo: "master's graduates at the threshold"
  addressee: learner
  verbs: []
  about: "more originality, insight and reflection"
  themes: [none]
  domain: subject-skill
  award: ["master's"]
  gradeOf: none
  paraphrase: "A master's graduate at threshold will also show more originality, insight and critical reflection."
  quote: full   # the issuer's statement is in `source` (D-std-0014)
  audience: both
  subjects: inherited
- id: qaa/landscape-architecture-2024/4.7.b5
  locator: { number: "4.7.b5", headingPath: ["Benchmark standards", "Master's degrees"] }
  span: { start: 57431, end: 57529 }
  source: "an ability to synthesise and integrate concepts and ideas and to relate them to practical contexts"
  stem: "4.7"
  statementType: threshold
  rung: threshold
  force: will
  level: fheq:7
  appliesTo: "master's graduates at the threshold"
  addressee: learner
  verbs: ["synthesise", "integrate", "relate"]
  about: "synthesising concepts and relating them to practice"
  themes: [none]
  domain: subject-skill
  award: ["master's"]
  gradeOf: none
  paraphrase: "A master's graduate at threshold will also be able to draw concepts and ideas together and connect them to practice."
  quote: full   # the issuer's statement is in `source` (D-std-0014)
  audience: both
  subjects: inherited
- id: qaa/landscape-architecture-2024/4.7.b6
  locator: { number: "4.7.b6", headingPath: ["Benchmark standards", "Master's degrees"] }
  span: { start: 57532, end: 57634 }
  source: "a good awareness and understanding of professional working, roles, responsibilities, ethics and values"
  stem: "4.7"
  statementType: threshold
  rung: threshold
  force: will
  level: fheq:7
  appliesTo: "master's graduates at the threshold"
  addressee: learner
  verbs: []
  about: "professional working, roles, ethics and values"
  themes: [none]
  domain: understanding
  award: ["master's"]
  gradeOf: none
  paraphrase: "A master's graduate at threshold will also show a good grasp of how professionals work, their roles and duties, and the ethics and values of practice."
  quote: full   # the issuer's statement is in `source` (D-std-0014)
  audience: both
  subjects: inherited
- id: qaa/landscape-architecture-2024/4.7.b7
  locator: { number: "4.7.b7", headingPath: ["Benchmark standards", "Master's degrees"] }
  span: { start: 57637, end: 57679 }
  source: "professionalism in undertaking assignments"
  stem: "4.7"
  statementType: threshold
  rung: threshold
  force: will
  level: fheq:7
  appliesTo: "master's graduates at the threshold"
  addressee: learner
  verbs: ["undertaking"]
  about: "professionalism in assignments"
  themes: [none]
  domain: generic-skill
  award: ["master's"]
  gradeOf: none
  paraphrase: "A master's graduate at threshold will also show professionalism in carrying out assignments."
  quote: full   # the issuer's statement is in `source` (D-std-0014)
  audience: both
  subjects: inherited
- id: qaa/landscape-architecture-2024/4.7.b8
  locator: { number: "4.7.b8", headingPath: ["Benchmark standards", "Master's degrees"] }
  span: { start: 57682, end: 57796 }
  source: "an understanding of the application of alternative methods of information retrieval, data collection and analysis."
  stem: "4.7"
  statementType: threshold
  rung: threshold
  force: will
  level: fheq:7
  appliesTo: "master's graduates at the threshold"
  addressee: learner
  verbs: []
  about: "alternative methods of retrieval, collection and analysis"
  themes: [none]
  domain: understanding
  award: ["master's"]
  gradeOf: none
  paraphrase: "A master's graduate at threshold will also show understanding of how to use other methods of finding information and collecting and analysing data."
  quote: full   # the issuer's statement is in `source` (D-std-0014)
  audience: both
  subjects: inherited
```

### S4a Audience versions
<!-- label: both; status: drafted; basis: primary. forPractitioner: for the programme designer or teacher. forBeneficiary: for the student, second person, naming no issuer. author-agent-written: instructions to an AI agent writing about the statement (a course document, a handbook, an outcome, a report). author-agent-dialogue: instructions to an AI agent using the statement in conversation (with a student, a teacher or a programme team). Written fresh from the held text alone (benchmark rule 6; Abbott, 15:42). -->
```yaml
- statement: qaa/landscape-architecture-2024/1.25.b1
  forPractitioner: { text: "Consider how your course should open physical access to its resources and facilities, fieldwork included, through inclusive design in every part of delivery.", rewrite: light, force: should, status: drafted }
  forBeneficiary: { text: "not-applicable: a duty on the course; the student meets its effect, not a standard to reach", rewrite: full, force: should, status: drafted }
  author-agent-written: "Present this as a provider expectation with should-force (QAA, 2024, Landscape Architecture Subject Benchmark Statement, para 1.25), on physical access, not as a student outcome or a legal duty. It holds for the course at any level. Set it beside 1.25.b2 on academic access and 4.4.b46 on inclusive communication, and note that the legal duties sit with the provider (1.20)."
  author-agent-dialogue: "Raise it with a programme team planning studios, site visits or fieldwork. Ask: which sites, rooms and field trips would a disabled student find hard to reach, and what is the alternative? Put it as a design question for staff; do not hand it to a student as something they must achieve."
- statement: qaa/landscape-architecture-2024/1.25.b2
  forPractitioner: { text: "Consider how your course should open academic access, by offering alternative ways of teaching, learning, assessing and giving feedback where these fit.", rewrite: light, force: should, status: drafted }
  forBeneficiary: { text: "not-applicable: a duty on the course; the student meets its effect, not a standard to reach", rewrite: full, force: should, status: drafted }
  author-agent-written: "Present this as a provider expectation with should-force (QAA, 2024, Landscape Architecture Subject Benchmark Statement, para 1.25) on academic access through alternative forms of delivery; it is not a student outcome. Do not claim it requires any one adjustment. Set it beside 1.25.b1 and the assessment range in 3.12."
  author-agent-dialogue: "Raise it when a programme team reviews assessment or feedback. Ask: where could a student show the same outcome another way, and is that option written into the module? Keep it with staff; do not present it to a student as their responsibility."
- statement: qaa/landscape-architecture-2024/1.26.b1
  forPractitioner: { text: "Course content will give students chances to show they understand sustainability values and actions that change society towards regenerative futures, with the UN goals as illustration.", rewrite: light, force: will, status: drafted }
  forBeneficiary: { text: "You will have chances to show you understand the values and actions that move society towards a regenerative, sustainable future, using the UN goals as examples.", rewrite: full, force: will, status: drafted }
  author-agent-written: "Present this as a will-statement on what course content will give students the chance to show (QAA, 2024, Landscape Architecture Subject Benchmark Statement, para 1.26): understanding of sustainability values and actions, illustrated by the UN goals. It is part of the sustainability theme, not a threshold item, and names no level; do not present it as a separate assessed outcome. Set it beside 1.26.b2 and 4.4.b11, the ESD guidance the statement lists, and the FHEQ honours descriptor on systematic understanding (qaa/fheq-2024/4.15.b1)."
  author-agent-dialogue: "Raise it when a student or a team talks about sustainability in projects. To a student, say what the course will let you show; to staff, ask where the course gives that chance. Ask: \"Which of the UN goals does your current project touch, and how?\" Do not read the list aloud; pick the item that fits the conversation."
- statement: qaa/landscape-architecture-2024/1.26.b2
  forPractitioner: { text: "Course content will give students chances to show systems thinking about biodiversity, natural capital and ecosystem services, and how people interact with them at different scales.", rewrite: light, force: will, status: drafted }
  forBeneficiary: { text: "You will have chances to show you can think in systems about biodiversity, natural capital and the services ecosystems give us, at different scales.", rewrite: full, force: will, status: drafted }
  author-agent-written: "Present this as a will-statement on what course content will give students the chance to show (QAA, 2024, Landscape Architecture Subject Benchmark Statement, para 1.26): understanding of systems thinking on biodiversity, natural capital and ecosystem services. It is part of the sustainability theme, not a threshold item, and names no level; do not present it as a separate assessed outcome. Set it beside 1.26.b1 and 4.4.b10, the ESD guidance the statement lists, and the FHEQ honours descriptor on systematic understanding (qaa/fheq-2024/4.15.b1)."
  author-agent-dialogue: "Raise it when a student or a team talks about sustainability in projects. To a student, say what the course will let you show; to staff, ask where the course gives that chance. Ask: \"What does your site give people and wildlife, and what would change if you altered it?\" Do not read the list aloud; pick the item that fits the conversation."
- statement: qaa/landscape-architecture-2024/1.26.b3
  forPractitioner: { text: "Course content will give students chances to show they understand climate change and can spot openings for mitigation, adaptation and resilience.", rewrite: light, force: will, status: drafted }
  forBeneficiary: { text: "You will have chances to show you understand what causes climate change, what it does, and where design can reduce it or help places adapt.", rewrite: full, force: will, status: drafted }
  author-agent-written: "Present this as a will-statement on what course content will give students the chance to show (QAA, 2024, Landscape Architecture Subject Benchmark Statement, para 1.26): understanding of climate change and the openings for mitigation, adaptation and resilience. It is part of the sustainability theme, not a threshold item, and names no level; do not present it as a separate assessed outcome. Set it beside 1.26.b5, the ESD guidance the statement lists, and the FHEQ honours descriptor on systematic understanding (qaa/fheq-2024/4.15.b1)."
  author-agent-dialogue: "Raise it when a student or a team talks about sustainability in projects. To a student, say what the course will let you show; to staff, ask where the course gives that chance. Ask: \"Where in your scheme could you cut emissions or help the place cope with a changing climate?\" Do not read the list aloud; pick the item that fits the conversation."
- statement: qaa/landscape-architecture-2024/1.26.b4
  forPractitioner: { text: "Course content will give students chances to show they understand law at international, national and local level and policy past, present and emerging.", rewrite: light, force: will, status: drafted }
  forBeneficiary: { text: "You will have chances to show you understand the law and policy, from global to local, that shape sustainable landscape work.", rewrite: full, force: will, status: drafted }
  author-agent-written: "Present this as a will-statement on what course content will give students the chance to show (QAA, 2024, Landscape Architecture Subject Benchmark Statement, para 1.26): understanding of the legislative and policy context of sustainability. It is part of the sustainability theme, not a threshold item, and names no level; do not present it as a separate assessed outcome. Set it beside 3.2 (legislative and planning policy context), the ESD guidance the statement lists, and the FHEQ honours descriptor on systematic understanding (qaa/fheq-2024/4.15.b1)."
  author-agent-dialogue: "Raise it when a student or a team talks about sustainability in projects. To a student, say what the course will let you show; to staff, ask where the course gives that chance. Ask: \"Which law or policy sets limits or opportunities for your project?\" Do not read the list aloud; pick the item that fits the conversation."
- statement: qaa/landscape-architecture-2024/1.26.b5
  forPractitioner: { text: "Course content will give students chances to show they understand design that helps communities and landscapes adapt, become resilient and regenerate.", rewrite: light, force: will, status: drafted }
  forBeneficiary: { text: "You will have chances to show you understand how design can help communities and landscapes adapt, recover and renew.", rewrite: full, force: will, status: drafted }
  author-agent-written: "Present this as a will-statement on what course content will give students the chance to show (QAA, 2024, Landscape Architecture Subject Benchmark Statement, para 1.26): understanding of design for adaptation, resilience and regeneration. It is part of the sustainability theme, not a threshold item, and names no level; do not present it as a separate assessed outcome. Set it beside 1.26.b3, the ESD guidance the statement lists, and the FHEQ honours descriptor on systematic understanding (qaa/fheq-2024/4.15.b1)."
  author-agent-dialogue: "Raise it when a student or a team talks about sustainability in projects. To a student, say what the course will let you show; to staff, ask where the course gives that chance. Ask: \"How would your design help this community or landscape recover from a shock?\" Do not read the list aloud; pick the item that fits the conversation."
- statement: qaa/landscape-architecture-2024/1.26.b6
  forPractitioner: { text: "Course content will give students chances to show understanding through case studies and good practice at many scales, and live projects that face uncertainty where possible.", rewrite: light, force: will, status: drafted }
  forBeneficiary: { text: "You will have chances to show what you understand through case studies, good practice and, where possible, live projects that imagine sustainable futures.", rewrite: full, force: will, status: drafted }
  author-agent-written: "Present this as a will-statement on what course content will give students the chance to show (QAA, 2024, Landscape Architecture Subject Benchmark Statement, para 1.26): understanding of sustainability through case studies, best practice and live projects. It is part of the sustainability theme, not a threshold item, and names no level; do not present it as a separate assessed outcome. Set it beside 4.4.b16 on precedent study, the ESD guidance the statement lists, and the FHEQ honours descriptor on systematic understanding (qaa/fheq-2024/4.15.b1)."
  author-agent-dialogue: "Raise it when a student or a team talks about sustainability in projects. To a student, say what the course will let you show; to staff, ask where the course gives that chance. Ask: \"Which precedent shows sustainability at the scale you are working at?\" Do not read the list aloud; pick the item that fits the conversation."
- statement: qaa/landscape-architecture-2024/1.26.b7
  forPractitioner: { text: "Course content will give students chances to show they understand materiality in the palettes they may specify, including extraction and waste.", rewrite: light, force: will, status: drafted }
  forBeneficiary: { text: "You will have chances to show you understand where the materials you might specify come from and what happens to them as waste.", rewrite: full, force: will, status: drafted }
  author-agent-written: "Present this as a will-statement on what course content will give students the chance to show (QAA, 2024, Landscape Architecture Subject Benchmark Statement, para 1.26): understanding of materiality across the life of the materials students may specify. It is part of the sustainability theme, not a threshold item, and names no level; do not present it as a separate assessed outcome. Set it beside 4.4.b17 and 4.4.b18, the ESD guidance the statement lists, and the FHEQ honours descriptor on systematic understanding (qaa/fheq-2024/4.15.b1)."
  author-agent-dialogue: "Raise it when a student or a team talks about sustainability in projects. To a student, say what the course will let you show; to staff, ask where the course gives that chance. Ask: \"Where does this material come from, and where will it end up?\" Do not read the list aloud; pick the item that fits the conversation."
- statement: qaa/landscape-architecture-2024/2.5
  forPractitioner: { text: "Your course sets its own focus (design, planning, management or ecology); if it is accredited it must map to the LI competency framework, showing where each knowledge requirement is met.", rewrite: light, force: must, status: drafted }
  forBeneficiary: { text: "not-applicable: a requirement on accredited courses, set by the professional body", rewrite: full, force: must, status: drafted }
  author-agent-written: "Present this as a requirement on accredited courses (QAA, 2024, Landscape Architecture Subject Benchmark Statement, para 2.5), set by the Landscape Institute, not by the statement; \"required\" is read as must. Do not claim that meeting the statement brings accreditation (2.8). Set it beside 2.4 and the LI competency framework (not yet ingested)."
  author-agent-dialogue: "Raise it with a programme team seeking or renewing LI accreditation. Ask: where in the course map does each competency get taught and assessed? Frame it for staff; do not give it to a student as a requirement on them."
- statement: qaa/landscape-architecture-2024/2.11
  forPractitioner: { text: "Plan each level so it builds towards all the threshold skills, with credit for the full range of learning and assessment; a second or above usually fits a graduate for postgraduate study.", rewrite: light, force: must, status: drafted }
  forBeneficiary: { text: "As you move through each year, what you learn and do should build towards the full set of threshold skills; a second-class result or better usually prepares you for postgraduate study.", rewrite: full, force: must, status: drafted }
  author-agent-written: "Present this as the issuer's expectation on progression (QAA, 2024, Landscape Architecture Subject Benchmark Statement, para 2.11), worded with \"expected\" and \"would\", so read as describes, not must. It is at FHEQ level 6 (FQHEIS 10) for honours. Set it beside the threshold list 4.4, Annex D 3rd cells (qaa/fheq-2024/annex-d/summary/r1/3rd) and spine:6; do not claim it sets entry rules for postgraduate study."
  author-agent-dialogue: "Raise it when a student asks how the years fit together or whether they can go on to a master's. Ask: which threshold skills has each year built so far? Avoid presenting a second-class result as a guarantee of a place."
- statement: qaa/landscape-architecture-2024/2.12
  forPractitioner: { text: "Joint or combined honours students will reach core elements of the specific and generic skills and add skills from their other subject.", rewrite: light, force: will, status: drafted }
  forBeneficiary: { text: "If you study the subject with another, you will reach the core skills and add others from your second subject, with room to explore where they meet.", rewrite: full, force: will, status: drafted }
  author-agent-written: "Present this as a will-expectation for joint and combined honours (QAA, 2024, Landscape Architecture Subject Benchmark Statement, para 2.12) at FHEQ level 6. Do not claim joint students meet every threshold item in 4.4; the statement says core elements. Set it beside 4.4 and the FHEQ honours descriptor qaa/fheq-2024/4.15.i1."
  author-agent-dialogue: "Raise it with a joint honours student unsure what is expected of them. Ask: which of the core skills does your landscape half cover, and what does your other subject add? Avoid implying they must cover the whole single-honours list."
- statement: qaa/landscape-architecture-2024/2.15
  forPractitioner: { text: "Tell students that the Pathway to Chartership must begin from an LI-accredited master's of at least 180 credits at level 7.", rewrite: light, force: must, status: drafted }
  forBeneficiary: { text: "If you want to become a chartered landscape architect, you must first complete a master's the professional body accredits, worth 180 credits or more at level 7.", rewrite: full, force: must, status: drafted }
  author-agent-written: "Present this as a professional body requirement (QAA, 2024, Landscape Architecture Subject Benchmark Statement, para 2.15), \"requires\" read as must; it is the LI's rule, not an academic standard. It concerns the master's at FHEQ level 7 (spine:7). Set it beside 2.16 and the master's list 4.7; do not claim an honours degree alone opens the route."
  author-agent-dialogue: "Raise it when a student asks how to become chartered. Ask: are you planning an accredited master's, and does the one you have in mind carry at least 180 credits at level 7? Keep it plain and point them to the LI for detail."
- statement: qaa/landscape-architecture-2024/2.21
  forPractitioner: { text: "Prospective students should be told that funding differs by duration, mode and nation, and pointed to the funding body and the institution before they commit.", rewrite: light, force: should, status: drafted }
  forBeneficiary: { text: "Before you commit, you should know that funding depends on how long, how and where you study; talk to the funding body and the university first.", rewrite: full, force: should, status: drafted }
  author-agent-written: "Present this as advice with should-force to prospective students (QAA, 2024, Landscape Architecture Subject Benchmark Statement, para 2.21); it is not an academic standard. Do not state funding rules; the statement gives none. Set it beside 2.20 on modes of study."
  author-agent-dialogue: "Raise it when an applicant asks about part-time or four-year routes. Ask: have you checked with your funding body how your choice of mode and length affects support? Do not give funding figures."
- statement: qaa/landscape-architecture-2024/2.26
  forPractitioner: { text: "In periodic review your institution will bring in external reviewers for an outside view, checking that threshold standards are met and content suits the subject.", rewrite: light, force: will, status: drafted }
  forBeneficiary: { text: "not-applicable: a duty on the provider in quality review", rewrite: full, force: will, status: drafted }
  author-agent-written: "Present this as a will-expectation on providers (QAA, 2024, Landscape Architecture Subject Benchmark Statement, para 2.26) about externality in review; it is a quality process, not a student outcome. Set it beside 2.27 on external examining and 4.4 as the threshold reviewers check."
  author-agent-dialogue: "Raise it with a programme team preparing for periodic review. Ask: who will give the outside view, and will they test the course against the threshold list? Do not raise it with students as a standard."
- statement: qaa/landscape-architecture-2024/3.3
  forPractitioner: { text: "Your course will use varied teaching methods, from lectures to design charettes, within a studio-based culture where projects grow in scale and complexity.", rewrite: light, force: will, status: drafted }
  forBeneficiary: { text: "not-applicable: a duty on the course in how it teaches", rewrite: full, force: will, status: drafted }
  author-agent-written: "Present this as a will-expectation on courses (QAA, 2024, Landscape Architecture Subject Benchmark Statement, para 3.3) about teaching methods; the statement does not prescribe any one method. Set it beside 3.4 to 3.6 on projects and the studio, and do not claim a set studio contact time."
  author-agent-dialogue: "Raise it with staff designing teaching. Ask: where does the studio let students apply new knowledge in projects of rising scale? Keep it for staff; a student meets it as their timetable, not as a target."
- statement: qaa/landscape-architecture-2024/3.9
  forPractitioner: { text: "At every level your course will give students both formative and summative assessment.", rewrite: light, force: will, status: drafted }
  forBeneficiary: { text: "At every stage you will have both practice assessment with feedback and assessment that counts towards your marks.", rewrite: full, force: will, status: drafted }
  author-agent-written: "Present this as a will-expectation (QAA, 2024, Landscape Architecture Subject Benchmark Statement, para 3.9) for every level of study; 3.10 and 3.11 define the two kinds. Do not claim a set ratio between them. Set it beside 3.12 on methods."
  author-agent-dialogue: "Raise it when a student asks whether a task counts. Ask: is this piece for feedback only, or does it count, and how will you use the feedback? Explain the difference plainly."
- statement: qaa/landscape-architecture-2024/4.3
  forPractitioner: { text: "Your institution decides what counts as evidence of achievement and should refer to Annex D of the Frameworks, with its descriptions of first, upper second, lower second and third.", rewrite: light, force: should, status: drafted }
  forBeneficiary: { text: "not-applicable: a duty on the provider in judging achievement", rewrite: full, force: should, status: drafted }
  author-agent-written: "Present this as a should-duty on providers (QAA, 2024, Landscape Architecture Subject Benchmark Statement, para 4.3) to read the honours classes against Annex D (std:doc:qaa-fheq-2024-framework, qaa/fheq-2024/annex-d/...). It holds at FHEQ level 6 and FQHEIS 10. Do not claim the statement sets its own marking scale; set it beside 4.1, 4.2 and the rungs 4.4 to 4.6."
  author-agent-dialogue: "Raise it with a team writing marking criteria. Ask: does each band in your criteria line up with the Annex D class it stands for? Keep it for staff, not students."
- statement: qaa/landscape-architecture-2024/4.4.b1
  forPractitioner: { text: "At threshold, graduates can analyse information and combine what they find into balanced arguments.", rewrite: light, force: threshold, status: drafted }
  forBeneficiary: { text: "To reach the threshold, you will be able to analyse information and pull the results together into a fair, balanced argument.", rewrite: full, force: threshold, status: drafted }
  author-agent-written: "Present this as a threshold standard: the least every honours graduate in the subject has shown, at FHEQ level 6 and FQHEIS level 10, under the intellectual group (QAA, 2024, Landscape Architecture Subject Benchmark Statement, para 4.4). Describe it as analysing information and building balanced arguments; do not call it a regulation or apply it to the master's list in 4.7. Set it beside the honours descriptor qaa/fheq-2024/4.15.b7, the Annex D third-class cell qaa/fheq-2024/annex-d/cognitive/r2/3rd, spine:6, the neighbouring items 4.4.b2 and the typical rung 4.5.b2."
  author-agent-dialogue: "Raise it when a student or a module team asks what honours expects on analysing information and building balanced arguments. Put it plainly: to a student, what you need to be able to do by the end; to staff, what the course must give evidence of. Ask: \"Where in your last report did you weigh both sides before concluding?\" Do not read the list aloud, and present it as the floor, not the goal."
- statement: qaa/landscape-architecture-2024/4.4.b2
  forPractitioner: { text: "At threshold, graduates can show they make decisions in complex, unpredictable settings.", rewrite: light, force: threshold, status: drafted }
  forBeneficiary: { text: "To reach the threshold, you will be able to show that you can make decisions when a situation is complex and hard to predict.", rewrite: full, force: threshold, status: drafted }
  author-agent-written: "Present this as a threshold standard: the least every honours graduate in the subject has shown, at FHEQ level 6 and FQHEIS level 10, under the intellectual group (QAA, 2024, Landscape Architecture Subject Benchmark Statement, para 4.4). Describe it as decision-making in complex, unpredictable settings; do not call it a regulation or apply it to the master's list in 4.7. Set it beside the honours descriptor qaa/fheq-2024/4.15.b9.2, the Annex D third-class cell qaa/fheq-2024/annex-d/cognitive/r3/3rd, spine:6, the neighbouring items 4.4.b1, 4.4.b3 and the typical rung 4.5.b2."
  author-agent-dialogue: "Raise it when a student or a module team asks what honours expects on decision-making in complex, unpredictable settings. Put it plainly: to a student, what you need to be able to do by the end; to staff, what the course must give evidence of. Ask: \"Tell me about a design decision you made when the site or brief kept changing.\" Do not read the list aloud, and present it as the floor, not the goal."
- statement: qaa/landscape-architecture-2024/4.4.b3
  forPractitioner: { text: "At threshold, graduates can use critical thinking to form their own informed position as future landscape professionals.", rewrite: light, force: threshold, status: drafted }
  forBeneficiary: { text: "To reach the threshold, you will be able to think critically and reach your own informed view as someone entering the landscape profession.", rewrite: full, force: threshold, status: drafted }
  author-agent-written: "Present this as a threshold standard: the least every honours graduate in the subject has shown, at FHEQ level 6 and FQHEIS level 10, under the intellectual group (QAA, 2024, Landscape Architecture Subject Benchmark Statement, para 4.4). Describe it as critical thinking towards a personal professional position; do not call it a regulation or apply it to the master's list in 4.7. Set it beside the honours descriptor qaa/fheq-2024/4.15.b7, the Annex D third-class cell qaa/fheq-2024/annex-d/cognitive/r2/3rd, spine:6, the neighbouring items 4.4.b2, 4.4.b4 and the typical rung 4.5.b3."
  author-agent-dialogue: "Raise it when a student or a module team asks what honours expects on critical thinking towards a personal professional position. Put it plainly: to a student, what you need to be able to do by the end; to staff, what the course must give evidence of. Ask: \"What do you stand for as a landscape professional, and what shaped that view?\" Do not read the list aloud, and present it as the floor, not the goal."
- statement: qaa/landscape-architecture-2024/4.4.b4
  forPractitioner: { text: "At threshold, graduates can view landscapes through different stakeholders' eyes and fold their needs into proposals.", rewrite: light, force: threshold, status: drafted }
  forBeneficiary: { text: "To reach the threshold, you will be able to see a landscape as the different people with a stake in it see it, and build their needs into your proposals.", rewrite: full, force: threshold, status: drafted }
  author-agent-written: "Present this as a threshold standard: the least every honours graduate in the subject has shown, at FHEQ level 6 and FQHEIS level 10, under the intellectual group (QAA, 2024, Landscape Architecture Subject Benchmark Statement, para 4.4). Describe it as stakeholder perspectives in proposals; do not call it a regulation or apply it to the master's list in 4.7. Set it beside the honours descriptor qaa/fheq-2024/4.15.b3.1, the Annex D third-class cell qaa/fheq-2024/annex-d/knowledge/r3/3rd, spine:6, the neighbouring items 4.4.b3, 4.4.b5 and the typical rung 4.5.b3."
  author-agent-dialogue: "Raise it when a student or a module team asks what honours expects on stakeholder perspectives in proposals. Put it plainly: to a student, what you need to be able to do by the end; to staff, what the course must give evidence of. Ask: \"Whose view of this site did your proposal leave out, and how could you include it?\" Do not read the list aloud, and present it as the floor, not the goal."
- statement: qaa/landscape-architecture-2024/4.4.b5
  forPractitioner: { text: "At threshold, graduates understand and allow for competing theories and priorities, so their judgements and proposals are well evidenced.", rewrite: light, force: threshold, status: drafted }
  forBeneficiary: { text: "To reach the threshold, you will be able to understand rival theories and priorities and take them into account so your judgements rest on good evidence.", rewrite: full, force: threshold, status: drafted }
  author-agent-written: "Present this as a threshold standard: the least every honours graduate in the subject has shown, at FHEQ level 6 and FQHEIS level 10, under the intellectual group (QAA, 2024, Landscape Architecture Subject Benchmark Statement, para 4.4). Describe it as weighing competing theories and priorities; do not call it a regulation or apply it to the master's list in 4.7. Set it beside the honours descriptor qaa/fheq-2024/4.15.b4, the Annex D third-class cell qaa/fheq-2024/annex-d/knowledge/r2/3rd, spine:6, the neighbouring items 4.4.b4, 4.4.b6 and the typical rung 4.5.b1."
  author-agent-dialogue: "Raise it when a student or a module team asks what honours expects on weighing competing theories and priorities. Put it plainly: to a student, what you need to be able to do by the end; to staff, what the course must give evidence of. Ask: \"Which competing priority did you have to trade off, and on what evidence?\" Do not read the list aloud, and present it as the floor, not the goal."
- statement: qaa/landscape-architecture-2024/4.4.b6
  forPractitioner: { text: "At threshold, graduates can evaluate alternative proposals with fitting tools and techniques.", rewrite: light, force: threshold, status: drafted }
  forBeneficiary: { text: "To reach the threshold, you will be able to compare and judge different proposals using the right tools and techniques.", rewrite: full, force: threshold, status: drafted }
  author-agent-written: "Present this as a threshold standard: the least every honours graduate in the subject has shown, at FHEQ level 6 and FQHEIS level 10, under the intellectual group (QAA, 2024, Landscape Architecture Subject Benchmark Statement, para 4.4). Describe it as evaluating alternative proposals; do not call it a regulation or apply it to the master's list in 4.7. Set it beside the honours descriptor qaa/fheq-2024/4.15.b7, the Annex D third-class cell qaa/fheq-2024/annex-d/cognitive/r2/3rd, spine:6, the neighbouring items 4.4.b5, 4.4.b7 and the typical rung 4.5.b3."
  author-agent-dialogue: "Raise it when a student or a module team asks what honours expects on evaluating alternative proposals. Put it plainly: to a student, what you need to be able to do by the end; to staff, what the course must give evidence of. Ask: \"How did you decide between your two options, and what tool did you use to compare them?\" Do not read the list aloud, and present it as the floor, not the goal."
- statement: qaa/landscape-architecture-2024/4.4.b7
  forPractitioner: { text: "At threshold, graduates can write and interpret project briefs, setting aims and objectives for familiar and new problems at many scales.", rewrite: light, force: threshold, status: drafted }
  forBeneficiary: { text: "To reach the threshold, you will be able to write and read project briefs, setting sensible aims and objectives for problems old and new, small and large.", rewrite: full, force: threshold, status: drafted }
  author-agent-written: "Present this as a threshold standard: the least every honours graduate in the subject has shown, at FHEQ level 6 and FQHEIS level 10, under the intellectual group (QAA, 2024, Landscape Architecture Subject Benchmark Statement, para 4.4). Describe it as formulating and interpreting project briefs; do not call it a regulation or apply it to the master's list in 4.7. Set it beside the honours descriptor qaa/fheq-2024/4.15.b7, the Annex D third-class cell qaa/fheq-2024/annex-d/cognitive/r3/3rd, spine:6, the neighbouring items 4.4.b6, 4.4.b8 and the typical rung 4.5.b3."
  author-agent-dialogue: "Raise it when a student or a module team asks what honours expects on formulating and interpreting project briefs. Put it plainly: to a student, what you need to be able to do by the end; to staff, what the course must give evidence of. Ask: \"If you rewrote this brief, what aims would you set and why?\" Do not read the list aloud, and present it as the floor, not the goal."
- statement: qaa/landscape-architecture-2024/4.4.b8
  forPractitioner: { text: "At threshold, graduates can find the relevant theory and techniques and turn them into policies, strategies, plans or interventions at varied spatial and time scales.", rewrite: light, force: threshold, status: drafted }
  forBeneficiary: { text: "To reach the threshold, you will be able to choose the theory and techniques that lead to good policies, strategies, plans or practical changes, at scales of space and time.", rewrite: full, force: threshold, status: drafted }
  author-agent-written: "Present this as a threshold standard: the least every honours graduate in the subject has shown, at FHEQ level 6 and FQHEIS level 10, under the intellectual group (QAA, 2024, Landscape Architecture Subject Benchmark Statement, para 4.4). Describe it as turning theory into policies, plans and interventions; do not call it a regulation or apply it to the master's list in 4.7. Set it beside the honours descriptor qaa/fheq-2024/4.15.b3.1, the Annex D third-class cell qaa/fheq-2024/annex-d/knowledge/r2/3rd, spine:6, the neighbouring items 4.4.b7, 4.4.b9 and the typical rung 4.5.b3."
  author-agent-dialogue: "Raise it when a student or a module team asks what honours expects on turning theory into policies, plans and interventions. Put it plainly: to a student, what you need to be able to do by the end; to staff, what the course must give evidence of. Ask: \"Which principle drove your strategy, and does it hold over twenty years as well as one?\" Do not read the list aloud, and present it as the floor, not the goal."
- statement: qaa/landscape-architecture-2024/4.4.b9
  forPractitioner: { text: "At threshold, graduates can identify and research what they need to know and apply it to familiar and new problems of varied scale.", rewrite: light, force: threshold, status: drafted }
  forBeneficiary: { text: "To reach the threshold, you will be able to work out what you need to know, research it and use it on familiar and new problems of any size.", rewrite: full, force: threshold, status: drafted }
  author-agent-written: "Present this as a threshold standard: the least every honours graduate in the subject has shown, at FHEQ level 6 and FQHEIS level 10, under the intellectual group (QAA, 2024, Landscape Architecture Subject Benchmark Statement, para 4.4). Describe it as researching and applying knowledge to problems; do not call it a regulation or apply it to the master's list in 4.7. Set it beside the honours descriptor qaa/fheq-2024/4.15.b6, the Annex D third-class cell qaa/fheq-2024/annex-d/cognitive/r3/3rd, spine:6, the neighbouring items 4.4.b8, 4.4.b10 and the typical rung 4.5.b3."
  author-agent-dialogue: "Raise it when a student or a module team asks what honours expects on researching and applying knowledge to problems. Put it plainly: to a student, what you need to be able to do by the end; to staff, what the course must give evidence of. Ask: \"What did you need to find out for this project, and how did you find it?\" Do not read the list aloud, and present it as the floor, not the goal."
- statement: qaa/landscape-architecture-2024/4.4.b10
  forPractitioner: { text: "At threshold, graduates appreciate and reflect on a project's ecosystem context and can frame proposals that conserve it and keep it in balance.", rewrite: light, force: threshold, status: drafted }
  forBeneficiary: { text: "To reach the threshold, you will be able to understand and reflect on the ecosystem your project sits in, and design proposals that protect it and keep it in balance.", rewrite: full, force: threshold, status: drafted }
  author-agent-written: "Present this as a threshold standard: the least every honours graduate in the subject has shown, at FHEQ level 6 and FQHEIS level 10, under the intellectual group (QAA, 2024, Landscape Architecture Subject Benchmark Statement, para 4.4). Describe it as the ecosystem context of projects; do not call it a regulation or apply it to the master's list in 4.7. Set it beside the honours descriptor qaa/fheq-2024/4.15.b1, the Annex D third-class cell qaa/fheq-2024/annex-d/knowledge/r1/3rd, spine:6, the neighbouring items 4.4.b9, 4.4.b11 and the typical rung 4.5.b3."
  author-agent-dialogue: "Raise it when a student or a module team asks what honours expects on the ecosystem context of projects. Put it plainly: to a student, what you need to be able to do by the end; to staff, what the course must give evidence of. Ask: \"What ecosystem does your site belong to, and how does your proposal keep it in balance?\" Do not read the list aloud, and present it as the floor, not the goal."
- statement: qaa/landscape-architecture-2024/4.4.b11
  forPractitioner: { text: "At threshold, graduates can show creativity and innovation in a sustainable context.", rewrite: light, force: threshold, status: drafted }
  forBeneficiary: { text: "To reach the threshold, you will be able to show creative, new thinking that also respects sustainability.", rewrite: full, force: threshold, status: drafted }
  author-agent-written: "Present this as a threshold standard: the least every honours graduate in the subject has shown, at FHEQ level 6 and FQHEIS level 10, under the intellectual group (QAA, 2024, Landscape Architecture Subject Benchmark Statement, para 4.4). Describe it as creativity and innovation within a sustainable context; do not call it a regulation or apply it to the master's list in 4.7. Set it beside the honours descriptor qaa/fheq-2024/4.15.b6, the Annex D third-class cell qaa/fheq-2024/annex-d/cognitive/r4/3rd, spine:6, the neighbouring items 4.4.b10, 4.4.b12 and the typical rung 4.5.b3."
  author-agent-dialogue: "Raise it when a student or a module team asks what honours expects on creativity and innovation within a sustainable context. Put it plainly: to a student, what you need to be able to do by the end; to staff, what the course must give evidence of. Ask: \"What is new in your scheme, and what makes it sustainable as well?\" Do not read the list aloud, and present it as the floor, not the goal."
- statement: qaa/landscape-architecture-2024/4.4.b12
  forPractitioner: { text: "At threshold, graduates can plan and carry out research, evaluate the outcomes and draw valid conclusions.", rewrite: light, force: threshold, status: drafted }
  forBeneficiary: { text: "To reach the threshold, you will be able to plan and carry out research, judge what it shows and reach sound conclusions.", rewrite: full, force: threshold, status: drafted }
  author-agent-written: "Present this as a threshold standard: the least every honours graduate in the subject has shown, at FHEQ level 6 and FQHEIS level 10, under the intellectual group (QAA, 2024, Landscape Architecture Subject Benchmark Statement, para 4.4). Describe it as planning and carrying out research; do not call it a regulation or apply it to the master's list in 4.7. Set it beside the honours descriptor qaa/fheq-2024/4.15.b6, the Annex D third-class cell qaa/fheq-2024/annex-d/knowledge/r3/3rd, spine:6, the neighbouring items 4.4.b11, 4.4.b13 and the typical rung 4.5.b2."
  author-agent-dialogue: "Raise it when a student or a module team asks what honours expects on planning and carrying out research. Put it plainly: to a student, what you need to be able to do by the end; to staff, what the course must give evidence of. Ask: \"How did you check that your conclusions follow from what you found?\" Do not read the list aloud, and present it as the floor, not the goal."
- statement: qaa/landscape-architecture-2024/4.4.b13
  forPractitioner: { text: "At threshold, graduates can use secondary sources, find suitable academic literature and reference it to standard conventions.", rewrite: light, force: threshold, status: drafted }
  forBeneficiary: { text: "To reach the threshold, you will be able to find and use published research and academic reading, and reference it properly.", rewrite: full, force: threshold, status: drafted }
  author-agent-written: "Present this as a threshold standard: the least every honours graduate in the subject has shown, at FHEQ level 6 and FQHEIS level 10, under the intellectual group (QAA, 2024, Landscape Architecture Subject Benchmark Statement, para 4.4). Describe it as using secondary sources and referencing; do not call it a regulation or apply it to the master's list in 4.7. Set it beside the honours descriptor qaa/fheq-2024/4.15.b5, the Annex D third-class cell qaa/fheq-2024/annex-d/cognitive/r1/3rd, spine:6, the neighbouring items 4.4.b12, 4.4.b14 and the typical rung 4.5.b2."
  author-agent-dialogue: "Raise it when a student or a module team asks what honours expects on using secondary sources and referencing. Put it plainly: to a student, what you need to be able to do by the end; to staff, what the course must give evidence of. Ask: \"Which sources did you lean on most, and how did you know they were sound?\" Do not read the list aloud, and present it as the floor, not the goal."
- statement: qaa/landscape-architecture-2024/4.4.b14
  forPractitioner: { text: "At threshold, graduates understand where questions of ethics, law or data protection may arise in their work.", rewrite: light, force: threshold, status: drafted }
  forBeneficiary: { text: "To reach the threshold, you will be able to tell where ethical, legal or data protection questions may come up in your work.", rewrite: full, force: threshold, status: drafted }
  author-agent-written: "Present this as a threshold standard: the least every honours graduate in the subject has shown, at FHEQ level 6 and FQHEIS level 10, under the intellectual group (QAA, 2024, Landscape Architecture Subject Benchmark Statement, para 4.4). Describe it as where questions of ethics, law or data protection may arise; do not call it a regulation or apply it to the master's list in 4.7. Set it beside the honours descriptor qaa/fheq-2024/4.15.b4, the Annex D third-class cell qaa/fheq-2024/annex-d/knowledge/r2/3rd, spine:6, the neighbouring items 4.4.b13, 4.4.b15 and the typical rung 4.5.b1."
  author-agent-dialogue: "Raise it when a student or a module team asks what honours expects on where questions of ethics, law or data protection may arise. Put it plainly: to a student, what you need to be able to do by the end; to staff, what the course must give evidence of. Ask: \"Did your survey or consultation raise any data protection question?\" Do not read the list aloud, and present it as the floor, not the goal."
- statement: qaa/landscape-architecture-2024/4.4.b15
  forPractitioner: { text: "At threshold, graduates understand the role and effect of intellectual property in creative design work.", rewrite: light, force: threshold, status: drafted }
  forBeneficiary: { text: "To reach the threshold, you will be able to understand how intellectual property works in design and how it affects your work and others'.", rewrite: full, force: threshold, status: drafted }
  author-agent-written: "Present this as a threshold standard: the least every honours graduate in the subject has shown, at FHEQ level 6 and FQHEIS level 10, under the intellectual group (QAA, 2024, Landscape Architecture Subject Benchmark Statement, para 4.4). Describe it as intellectual property in creative design; do not call it a regulation or apply it to the master's list in 4.7. Set it beside the honours descriptor qaa/fheq-2024/4.15.b1, the Annex D third-class cell qaa/fheq-2024/annex-d/knowledge/r2/3rd, spine:6, the neighbouring items 4.4.b14, 4.4.b16 and the typical rung 4.5.b1."
  author-agent-dialogue: "Raise it when a student or a module team asks what honours expects on intellectual property in creative design. Put it plainly: to a student, what you need to be able to do by the end; to staff, what the course must give evidence of. Ask: \"Whose ideas or images did you draw on, and how did you credit them?\" Do not read the list aloud, and present it as the floor, not the goal."
- statement: qaa/landscape-architecture-2024/4.4.b16
  forPractitioner: { text: "At threshold, graduates can identify, analyse and critique suitable precedent studies.", rewrite: light, force: threshold, status: drafted }
  forBeneficiary: { text: "To reach the threshold, you will be able to find good precedents, analyse them and judge what they do well or badly.", rewrite: full, force: threshold, status: drafted }
  author-agent-written: "Present this as a threshold standard: the least every honours graduate in the subject has shown, at FHEQ level 6 and FQHEIS level 10, under the intellectual group (QAA, 2024, Landscape Architecture Subject Benchmark Statement, para 4.4). Describe it as precedent study; do not call it a regulation or apply it to the master's list in 4.7. Set it beside the honours descriptor qaa/fheq-2024/4.15.b3.2, the Annex D third-class cell qaa/fheq-2024/annex-d/cognitive/r1/3rd, spine:6, the neighbouring items 4.4.b15, 4.4.b17 and the typical rung 4.5.b3."
  author-agent-dialogue: "Raise it when a student or a module team asks what honours expects on precedent study. Put it plainly: to a student, what you need to be able to do by the end; to staff, what the course must give evidence of. Ask: \"Which precedent taught you most, and what would you do differently from it?\" Do not read the list aloud, and present it as the floor, not the goal."
- statement: qaa/landscape-architecture-2024/4.4.b17
  forPractitioner: { text: "At threshold, graduates can identify and specify suitable hard materials and vegetation for varied proposals.", rewrite: light, force: threshold, status: drafted }
  forBeneficiary: { text: "To reach the threshold, you will be able to choose and specify the right hard materials and plants for different proposals.", rewrite: full, force: threshold, status: drafted }
  author-agent-written: "Present this as a threshold standard: the least every honours graduate in the subject has shown, at FHEQ level 6 and FQHEIS level 10, under the intellectual group (QAA, 2024, Landscape Architecture Subject Benchmark Statement, para 4.4). Describe it as specifying hard materials and vegetation; do not call it a regulation or apply it to the master's list in 4.7. Set it beside the honours descriptor qaa/fheq-2024/4.15.b2, the Annex D third-class cell qaa/fheq-2024/annex-d/practical/r1/3rd, spine:6, the neighbouring items 4.4.b16, 4.4.b18 and the typical rung 4.5.b3."
  author-agent-dialogue: "Raise it when a student or a module team asks what honours expects on specifying hard materials and vegetation. Put it plainly: to a student, what you need to be able to do by the end; to staff, what the course must give evidence of. Ask: \"Why did you choose these plants and surfaces for this site?\" Do not read the list aloud, and present it as the floor, not the goal."
- statement: qaa/landscape-architecture-2024/4.4.b18
  forPractitioner: { text: "At threshold, graduates understand the structural, performance and sustainability qualities of materials and the broad financial effects of specifying them.", rewrite: light, force: threshold, status: drafted }
  forBeneficiary: { text: "To reach the threshold, you will be able to understand how materials perform, how sustainable they are and roughly what specifying them costs.", rewrite: full, force: threshold, status: drafted }
  author-agent-written: "Present this as a threshold standard: the least every honours graduate in the subject has shown, at FHEQ level 6 and FQHEIS level 10, under the intellectual group (QAA, 2024, Landscape Architecture Subject Benchmark Statement, para 4.4). Describe it as the properties and cost of specified materials; do not call it a regulation or apply it to the master's list in 4.7. Set it beside the honours descriptor qaa/fheq-2024/4.15.b1, the Annex D third-class cell qaa/fheq-2024/annex-d/knowledge/r1/3rd, spine:6, the neighbouring items 4.4.b17 and the typical rung 4.5.b1."
  author-agent-dialogue: "Raise it when a student or a module team asks what honours expects on the properties and cost of specified materials. Put it plainly: to a student, what you need to be able to do by the end; to staff, what the course must give evidence of. Ask: \"What would this surface cost over its life, and how long will it last?\" Do not read the list aloud, and present it as the floor, not the goal."
- statement: qaa/landscape-architecture-2024/4.4.b19
  forPractitioner: { text: "At threshold, graduates can identify suitable geomatic information, that is acquiring, modelling and analysing spatially referenced data.", rewrite: light, force: threshold, status: drafted }
  forBeneficiary: { text: "To reach the threshold, you will be able to identify the right spatial data for a task and know how it is gathered, modelled and analysed.", rewrite: full, force: threshold, status: drafted }
  author-agent-written: "Present this as a threshold standard: the least every honours graduate in the subject has shown, at FHEQ level 6 and FQHEIS level 10, under the analytical and data interpretation group (QAA, 2024, Landscape Architecture Subject Benchmark Statement, para 4.4). Describe it as geomatic information and spatial data; do not call it a regulation or apply it to the master's list in 4.7. Set it beside the honours descriptor qaa/fheq-2024/4.15.b2, the Annex D third-class cell qaa/fheq-2024/annex-d/practical/r4/3rd, spine:6, the neighbouring items 4.4.b20 and the typical rung 4.5.b3."
  author-agent-dialogue: "Raise it when a student or a module team asks what honours expects on geomatic information and spatial data. Put it plainly: to a student, what you need to be able to do by the end; to staff, what the course must give evidence of. Ask: \"What spatial data did you use for this site, and where did it come from?\" Do not read the list aloud, and present it as the floor, not the goal."
- statement: qaa/landscape-architecture-2024/4.4.b20
  forPractitioner: { text: "At threshold, graduates can identify and collate suitable evidence and select samples effectively.", rewrite: light, force: threshold, status: drafted }
  forBeneficiary: { text: "To reach the threshold, you will be able to find and gather the right evidence and choose your samples sensibly.", rewrite: full, force: threshold, status: drafted }
  author-agent-written: "Present this as a threshold standard: the least every honours graduate in the subject has shown, at FHEQ level 6 and FQHEIS level 10, under the analytical and data interpretation group (QAA, 2024, Landscape Architecture Subject Benchmark Statement, para 4.4). Describe it as sources of evidence and sample selection; do not call it a regulation or apply it to the master's list in 4.7. Set it beside the honours descriptor qaa/fheq-2024/4.15.b2, the Annex D third-class cell qaa/fheq-2024/annex-d/knowledge/r3/3rd, spine:6, the neighbouring items 4.4.b19, 4.4.b21 and the typical rung 4.5.b3."
  author-agent-dialogue: "Raise it when a student or a module team asks what honours expects on sources of evidence and sample selection. Put it plainly: to a student, what you need to be able to do by the end; to staff, what the course must give evidence of. Ask: \"How did you choose where and what to sample?\" Do not read the list aloud, and present it as the floor, not the goal."
- statement: qaa/landscape-architecture-2024/4.4.b21
  forPractitioner: { text: "At threshold, graduates can identify and apply suitable qualitative or quantitative analysis techniques.", rewrite: light, force: threshold, status: drafted }
  forBeneficiary: { text: "To reach the threshold, you will be able to choose and use the right qualitative or numerical methods to analyse information.", rewrite: full, force: threshold, status: drafted }
  author-agent-written: "Present this as a threshold standard: the least every honours graduate in the subject has shown, at FHEQ level 6 and FQHEIS level 10, under the analytical and data interpretation group (QAA, 2024, Landscape Architecture Subject Benchmark Statement, para 4.4). Describe it as qualitative and quantitative analysis; do not call it a regulation or apply it to the master's list in 4.7. Set it beside the honours descriptor qaa/fheq-2024/4.15.b2, the Annex D third-class cell qaa/fheq-2024/annex-d/practical/r4/3rd, spine:6, the neighbouring items 4.4.b20, 4.4.b22 and the typical rung 4.5.b3."
  author-agent-dialogue: "Raise it when a student or a module team asks what honours expects on qualitative and quantitative analysis. Put it plainly: to a student, what you need to be able to do by the end; to staff, what the course must give evidence of. Ask: \"Why was that method the right one for this data?\" Do not read the list aloud, and present it as the floor, not the goal."
- statement: qaa/landscape-architecture-2024/4.4.b22
  forPractitioner: { text: "At threshold, graduates can show suitable precision in identifying, recording and critically analysing data from field, lab or secondary sources.", rewrite: light, force: threshold, status: drafted }
  forBeneficiary: { text: "To reach the threshold, you will be able to record and analyse data from the field, the lab or published sources with the care and accuracy the task needs.", rewrite: full, force: threshold, status: drafted }
  author-agent-written: "Present this as a threshold standard: the least every honours graduate in the subject has shown, at FHEQ level 6 and FQHEIS level 10, under the analytical and data interpretation group (QAA, 2024, Landscape Architecture Subject Benchmark Statement, para 4.4). Describe it as precision with data from field, laboratory and secondary sources; do not call it a regulation or apply it to the master's list in 4.7. Set it beside the honours descriptor qaa/fheq-2024/4.15.b2, the Annex D third-class cell qaa/fheq-2024/annex-d/practical/r2/3rd, spine:6, the neighbouring items 4.4.b21, 4.4.b23 and the typical rung 4.5.b3."
  author-agent-dialogue: "Raise it when a student or a module team asks what honours expects on precision with data from field, laboratory and secondary sources. Put it plainly: to a student, what you need to be able to do by the end; to staff, what the course must give evidence of. Ask: \"How accurate did your survey need to be, and was it?\" Do not read the list aloud, and present it as the floor, not the goal."
- statement: qaa/landscape-architecture-2024/4.4.b23
  forPractitioner: { text: "At threshold, graduates can prepare, process, interpret and present data using fitting techniques and software.", rewrite: light, force: threshold, status: drafted }
  forBeneficiary: { text: "To reach the threshold, you will be able to prepare, process, interpret and present data using the right techniques and software.", rewrite: full, force: threshold, status: drafted }
  author-agent-written: "Present this as a threshold standard: the least every honours graduate in the subject has shown, at FHEQ level 6 and FQHEIS level 10, under the analytical and data interpretation group (QAA, 2024, Landscape Architecture Subject Benchmark Statement, para 4.4). Describe it as preparing, interpreting and presenting data; do not call it a regulation or apply it to the master's list in 4.7. Set it beside the honours descriptor qaa/fheq-2024/4.15.b2, the Annex D third-class cell qaa/fheq-2024/annex-d/practical/r4/3rd, spine:6, the neighbouring items 4.4.b22, 4.4.b24 and the typical rung 4.5.b3."
  author-agent-dialogue: "Raise it when a student or a module team asks what honours expects on preparing, interpreting and presenting data. Put it plainly: to a student, what you need to be able to do by the end; to staff, what the course must give evidence of. Ask: \"What does this chart or map tell a reader in one glance?\" Do not read the list aloud, and present it as the floor, not the goal."
- statement: qaa/landscape-architecture-2024/4.4.b24
  forPractitioner: { text: "At threshold, graduates can solve numerical problems using computers and other techniques.", rewrite: light, force: threshold, status: drafted }
  forBeneficiary: { text: "To reach the threshold, you will be able to solve number problems, with a computer or by other means.", rewrite: full, force: threshold, status: drafted }
  author-agent-written: "Present this as a threshold standard: the least every honours graduate in the subject has shown, at FHEQ level 6 and FQHEIS level 10, under the analytical and data interpretation group (QAA, 2024, Landscape Architecture Subject Benchmark Statement, para 4.4). Describe it as solving numerical problems; do not call it a regulation or apply it to the master's list in 4.7. Set it beside the honours descriptor qaa/fheq-2024/4.15.b3.1, the Annex D third-class cell qaa/fheq-2024/annex-d/transferable/r1/3rd, spine:6, the neighbouring items 4.4.b23, 4.4.b25 and the typical rung 4.5.b2."
  author-agent-dialogue: "Raise it when a student or a module team asks what honours expects on solving numerical problems. Put it plainly: to a student, what you need to be able to do by the end; to staff, what the course must give evidence of. Ask: \"Which calculations did the project need, and how did you check them?\" Do not read the list aloud, and present it as the floor, not the goal."
- statement: qaa/landscape-architecture-2024/4.4.b25
  forPractitioner: { text: "At threshold, graduates can find, analyse and present financial data and draw on it in decisions fitted to the nature and scale of proposals.", rewrite: light, force: threshold, status: drafted }
  forBeneficiary: { text: "To reach the threshold, you will be able to find, analyse and present cost information and use it in decisions that suit the size of the proposal.", rewrite: full, force: threshold, status: drafted }
  author-agent-written: "Present this as a threshold standard: the least every honours graduate in the subject has shown, at FHEQ level 6 and FQHEIS level 10, under the analytical and data interpretation group (QAA, 2024, Landscape Architecture Subject Benchmark Statement, para 4.4). Describe it as financial information in decision-making; do not call it a regulation or apply it to the master's list in 4.7. Set it beside the honours descriptor qaa/fheq-2024/4.15.b9.2, the Annex D third-class cell qaa/fheq-2024/annex-d/practical/r4/3rd, spine:6, the neighbouring items 4.4.b24 and the typical rung 4.5.b3."
  author-agent-dialogue: "Raise it when a student or a module team asks what honours expects on financial information in decision-making. Put it plainly: to a student, what you need to be able to do by the end; to staff, what the course must give evidence of. Ask: \"How did cost shape the choices you made in this scheme?\" Do not read the list aloud, and present it as the floor, not the goal."
- statement: qaa/landscape-architecture-2024/4.4.b26
  forPractitioner: { text: "At threshold, graduates can design, plan and carry out investigations at the desk, in the field and in the studio, responsibly, sensitively and safely.", rewrite: light, force: threshold, status: drafted }
  forBeneficiary: { text: "To reach the threshold, you will be able to design, plan and carry out desk, field and studio investigations in a careful, responsible and safe way.", rewrite: full, force: threshold, status: drafted }
  author-agent-written: "Present this as a threshold standard: the least every honours graduate in the subject has shown, at FHEQ level 6 and FQHEIS level 10, under the practical group (QAA, 2024, Landscape Architecture Subject Benchmark Statement, para 4.4). Describe it as safe and responsible investigations; do not call it a regulation or apply it to the master's list in 4.7. Set it beside the honours descriptor qaa/fheq-2024/4.15.b6, the Annex D third-class cell qaa/fheq-2024/annex-d/practical/r2/3rd, spine:6, the neighbouring items 4.4.b27 and the typical rung 4.5.b3."
  author-agent-dialogue: "Raise it when a student or a module team asks what honours expects on safe and responsible investigations. Put it plainly: to a student, what you need to be able to do by the end; to staff, what the course must give evidence of. Ask: \"What did you do to keep yourself and others safe on your last site visit?\" Do not read the list aloud, and present it as the floor, not the goal."
- statement: qaa/landscape-architecture-2024/4.4.b27
  forPractitioner: { text: "At threshold, graduates understand and comply with rights of access and health and safety requirements, including ethics in research, with people and in the environment.", rewrite: light, force: threshold, status: drafted }
  forBeneficiary: { text: "To reach the threshold, you will be able to understand and follow rules on access to land and on health and safety, and act ethically when working with people and places.", rewrite: full, force: threshold, status: drafted }
  author-agent-written: "Present this as a threshold standard: the least every honours graduate in the subject has shown, at FHEQ level 6 and FQHEIS level 10, under the practical group (QAA, 2024, Landscape Architecture Subject Benchmark Statement, para 4.4). Describe it as access rights, health and safety and research ethics; do not call it a regulation or apply it to the master's list in 4.7. Set it beside the honours descriptor qaa/fheq-2024/4.15.b2, the Annex D third-class cell qaa/fheq-2024/annex-d/practical/r1/3rd, spine:6, the neighbouring items 4.4.b26, 4.4.b28 and the typical rung 4.5.b3."
  author-agent-dialogue: "Raise it when a student or a module team asks what honours expects on access rights, health and safety and research ethics. Put it plainly: to a student, what you need to be able to do by the end; to staff, what the course must give evidence of. Ask: \"Did you have the right to be on that land, and who did you need to ask?\" Do not read the list aloud, and present it as the floor, not the goal."
- statement: qaa/landscape-architecture-2024/4.4.b28
  forPractitioner: { text: "At threshold, graduates can show a clear, suitable use of scale and proportion in landscape design or management.", rewrite: light, force: threshold, status: drafted }
  forBeneficiary: { text: "To reach the threshold, you will be able to use scale and proportion clearly and well when you design or manage a landscape.", rewrite: full, force: threshold, status: drafted }
  author-agent-written: "Present this as a threshold standard: the least every honours graduate in the subject has shown, at FHEQ level 6 and FQHEIS level 10, under the practical group (QAA, 2024, Landscape Architecture Subject Benchmark Statement, para 4.4). Describe it as scale and proportion; do not call it a regulation or apply it to the master's list in 4.7. Set it beside the honours descriptor qaa/fheq-2024/4.15.b2, the Annex D third-class cell qaa/fheq-2024/annex-d/practical/r3/3rd, spine:6, the neighbouring items 4.4.b27, 4.4.b29 and the typical rung 4.5.b3."
  author-agent-dialogue: "Raise it when a student or a module team asks what honours expects on scale and proportion. Put it plainly: to a student, what you need to be able to do by the end; to staff, what the course must give evidence of. Ask: \"How does a person standing in your space feel its size?\" Do not read the list aloud, and present it as the floor, not the goal."
- statement: qaa/landscape-architecture-2024/4.4.b29
  forPractitioner: { text: "At threshold, in design subject areas, graduates can apply model-making, hand drawing and other graphic skills to put proposals before expert and lay audiences.", rewrite: light, force: threshold, status: drafted }
  forBeneficiary: { text: "To reach the threshold, you will be able to in design work, use models, hand drawing and other graphics to show your proposals to experts and the public.", rewrite: full, force: threshold, status: drafted }
  author-agent-written: "Present this as a threshold standard: the least every honours graduate in the subject has shown, at FHEQ level 6 and FQHEIS level 10, under the practical group (QAA, 2024, Landscape Architecture Subject Benchmark Statement, para 4.4). Describe it as physical models, hand drawing and graphics; do not call it a regulation or apply it to the master's list in 4.7. Set it beside the honours descriptor qaa/fheq-2024/4.15.b8, the Annex D third-class cell qaa/fheq-2024/annex-d/practical/r3/3rd, spine:6, the neighbouring items 4.4.b28 and the typical rung 4.5.b3."
  author-agent-dialogue: "Raise it when a student or a module team asks what honours expects on physical models, hand drawing and graphics. Put it plainly: to a student, what you need to be able to do by the end; to staff, what the course must give evidence of. Ask: \"Which drawing or model best explains your idea to someone outside the profession?\" Do not read the list aloud, and present it as the floor, not the goal."
- statement: qaa/landscape-architecture-2024/4.4.b30
  forPractitioner: { text: "At threshold, graduates can work effectively on their own, showing initiative, managing themselves, their time and their tasks, and reflecting.", rewrite: light, force: threshold, status: drafted }
  forBeneficiary: { text: "To reach the threshold, you will be able to work well on your own, using initiative, managing your time and tasks and reflecting on how it went.", rewrite: full, force: threshold, status: drafted }
  author-agent-written: "Present this as a threshold standard: the least every honours graduate in the subject has shown, at FHEQ level 6 and FQHEIS level 10, under the self-management and professional development group (QAA, 2024, Landscape Architecture Subject Benchmark Statement, para 4.4). Describe it as working effectively as an individual; do not call it a regulation or apply it to the master's list in 4.7. Set it beside the honours descriptor qaa/fheq-2024/4.15.b9.1, the Annex D third-class cell qaa/fheq-2024/annex-d/transferable/r3/3rd, spine:6, the neighbouring items 4.4.b31 and the typical rung 4.5.b2."
  author-agent-dialogue: "Raise it when a student or a module team asks what honours expects on working effectively as an individual. Put it plainly: to a student, what you need to be able to do by the end; to staff, what the course must give evidence of. Ask: \"How did you plan your own time on the last long project?\" Do not read the list aloud, and present it as the floor, not the goal."
- statement: qaa/landscape-architecture-2024/4.4.b31
  forPractitioner: { text: "At threshold, graduates can identify their individual goals and responsibilities.", rewrite: light, force: threshold, status: drafted }
  forBeneficiary: { text: "To reach the threshold, you will be able to set out your own goals and what you are responsible for.", rewrite: full, force: threshold, status: drafted }
  author-agent-written: "Present this as a threshold standard: the least every honours graduate in the subject has shown, at FHEQ level 6 and FQHEIS level 10, under the self-management and professional development group (QAA, 2024, Landscape Architecture Subject Benchmark Statement, para 4.4). Describe it as individual goals and responsibilities; do not call it a regulation or apply it to the master's list in 4.7. Set it beside the honours descriptor qaa/fheq-2024/4.15.b9.1, the Annex D third-class cell qaa/fheq-2024/annex-d/transferable/r4/3rd, spine:6, the neighbouring items 4.4.b30, 4.4.b32 and the typical rung 4.5.b2."
  author-agent-dialogue: "Raise it when a student or a module team asks what honours expects on individual goals and responsibilities. Put it plainly: to a student, what you need to be able to do by the end; to staff, what the course must give evidence of. Ask: \"What are you aiming for this term, and what is yours to deliver?\" Do not read the list aloud, and present it as the floor, not the goal."
- statement: qaa/landscape-architecture-2024/4.4.b32
  forPractitioner: { text: "At threshold, graduates can set realistic targets and perform as their allocated roles and responsibilities need.", rewrite: light, force: threshold, status: drafted }
  forBeneficiary: { text: "To reach the threshold, you will be able to set realistic targets and do what your role in a team asks of you.", rewrite: full, force: threshold, status: drafted }
  author-agent-written: "Present this as a threshold standard: the least every honours graduate in the subject has shown, at FHEQ level 6 and FQHEIS level 10, under the self-management and professional development group (QAA, 2024, Landscape Architecture Subject Benchmark Statement, para 4.4). Describe it as realistic targets and allocated roles; do not call it a regulation or apply it to the master's list in 4.7. Set it beside the honours descriptor qaa/fheq-2024/4.15.b9.1, the Annex D third-class cell qaa/fheq-2024/annex-d/transferable/r4/3rd, spine:6, the neighbouring items 4.4.b31, 4.4.b33 and the typical rung 4.5.b2."
  author-agent-dialogue: "Raise it when a student or a module team asks what honours expects on realistic targets and allocated roles. Put it plainly: to a student, what you need to be able to do by the end; to staff, what the course must give evidence of. Ask: \"Was the target you set yourself realistic, and how do you know?\" Do not read the list aloud, and present it as the floor, not the goal."
- statement: qaa/landscape-architecture-2024/4.4.b33
  forPractitioner: { text: "At threshold, graduates can reflect on and evaluate their own performance.", rewrite: light, force: threshold, status: drafted }
  forBeneficiary: { text: "To reach the threshold, you will be able to look back on your own work and judge how well you did.", rewrite: full, force: threshold, status: drafted }
  author-agent-written: "Present this as a threshold standard: the least every honours graduate in the subject has shown, at FHEQ level 6 and FQHEIS level 10, under the self-management and professional development group (QAA, 2024, Landscape Architecture Subject Benchmark Statement, para 4.4). Describe it as reflecting on and evaluating their own performance; do not call it a regulation or apply it to the master's list in 4.7. Set it beside the honours descriptor qaa/fheq-2024/4.15.b5, the Annex D third-class cell qaa/fheq-2024/annex-d/transferable/r5/3rd, spine:6, the neighbouring items 4.4.b32, 4.4.b34 and the typical rung 4.5.b2."
  author-agent-dialogue: "Raise it when a student or a module team asks what honours expects on reflecting on and evaluating their own performance. Put it plainly: to a student, what you need to be able to do by the end; to staff, what the course must give evidence of. Ask: \"What would you change if you started that project again?\" Do not read the list aloud, and present it as the floor, not the goal."
- statement: qaa/landscape-architecture-2024/4.4.b34
  forPractitioner: { text: "At threshold, graduates can develop an adaptable, flexible approach to study and work.", rewrite: light, force: threshold, status: drafted }
  forBeneficiary: { text: "To reach the threshold, you will be able to adapt how you study and work when things change.", rewrite: full, force: threshold, status: drafted }
  author-agent-written: "Present this as a threshold standard: the least every honours graduate in the subject has shown, at FHEQ level 6 and FQHEIS level 10, under the self-management and professional development group (QAA, 2024, Landscape Architecture Subject Benchmark Statement, para 4.4). Describe it as an adaptable, flexible approach to study and work; do not call it a regulation or apply it to the master's list in 4.7. Set it beside the honours descriptor qaa/fheq-2024/4.15.b9.3, the Annex D third-class cell qaa/fheq-2024/annex-d/transferable/r3/3rd, spine:6, the neighbouring items 4.4.b33, 4.4.b35 and the typical rung 4.5.b2."
  author-agent-dialogue: "Raise it when a student or a module team asks what honours expects on an adaptable, flexible approach to study and work. Put it plainly: to a student, what you need to be able to do by the end; to staff, what the course must give evidence of. Ask: \"When the brief changed, how did you adjust your way of working?\" Do not read the list aloud, and present it as the floor, not the goal."
- statement: qaa/landscape-architecture-2024/4.4.b35
  forPractitioner: { text: "At threshold, graduates can develop effective time management and organisation, including planning and executing a workload.", rewrite: light, force: threshold, status: drafted }
  forBeneficiary: { text: "To reach the threshold, you will be able to manage your time and organise your workload from plan to finish.", rewrite: full, force: threshold, status: drafted }
  author-agent-written: "Present this as a threshold standard: the least every honours graduate in the subject has shown, at FHEQ level 6 and FQHEIS level 10, under the self-management and professional development group (QAA, 2024, Landscape Architecture Subject Benchmark Statement, para 4.4). Describe it as time management and organisation; do not call it a regulation or apply it to the master's list in 4.7. Set it beside the honours descriptor qaa/fheq-2024/4.15.b9.1, the Annex D third-class cell qaa/fheq-2024/annex-d/transferable/r3/3rd, spine:6, the neighbouring items 4.4.b34, 4.4.b36 and the typical rung 4.5.b2."
  author-agent-dialogue: "Raise it when a student or a module team asks what honours expects on time management and organisation. Put it plainly: to a student, what you need to be able to do by the end; to staff, what the course must give evidence of. Ask: \"How did you plan your workload across deadlines this term?\" Do not read the list aloud, and present it as the floor, not the goal."
- statement: qaa/landscape-architecture-2024/4.4.b36
  forPractitioner: { text: "At threshold, graduates can show the competence, behaviour and attitude the profession requires, with attention to equity, diversity and inclusion.", rewrite: light, force: threshold, status: drafted }
  forBeneficiary: { text: "To reach the threshold, you will be able to show the skills, conduct and attitude the profession expects, including fairness and respect for everyone.", rewrite: full, force: threshold, status: drafted }
  author-agent-written: "Present this as a threshold standard: the least every honours graduate in the subject has shown, at FHEQ level 6 and FQHEIS level 10, under the self-management and professional development group (QAA, 2024, Landscape Architecture Subject Benchmark Statement, para 4.4). Describe it as professional competence, behaviour and attitude, with equity, diversity and inclusion; do not call it a regulation or apply it to the master's list in 4.7. Set it beside the honours descriptor qaa/fheq-2024/4.15.b9.1, the Annex D third-class cell qaa/fheq-2024/annex-d/transferable/r4/3rd, spine:6, the neighbouring items 4.4.b35, 4.4.b37 and the typical rung 4.5.b2."
  author-agent-dialogue: "Raise it when a student or a module team asks what honours expects on professional competence, behaviour and attitude, with equity, diversity and inclusion. Put it plainly: to a student, what you need to be able to do by the end; to staff, what the course must give evidence of. Ask: \"How did you make sure everyone in your team and your consultation was treated fairly?\" Do not read the list aloud, and present it as the floor, not the goal."
- statement: qaa/landscape-architecture-2024/4.4.b37
  forPractitioner: { text: "At threshold, graduates can recognise, respect and work within suitable professional codes of conduct.", rewrite: light, force: threshold, status: drafted }
  forBeneficiary: { text: "To reach the threshold, you will be able to know, respect and work within the codes of conduct of the profession.", rewrite: full, force: threshold, status: drafted }
  author-agent-written: "Present this as a threshold standard: the least every honours graduate in the subject has shown, at FHEQ level 6 and FQHEIS level 10, under the self-management and professional development group (QAA, 2024, Landscape Architecture Subject Benchmark Statement, para 4.4). Describe it as professional codes of conduct; do not call it a regulation or apply it to the master's list in 4.7. Set it beside the honours descriptor qaa/fheq-2024/4.15.b9.2, the Annex D third-class cell qaa/fheq-2024/annex-d/transferable/r4/3rd, spine:6, the neighbouring items 4.4.b36, 4.4.b38 and the typical rung 4.5.b2."
  author-agent-dialogue: "Raise it when a student or a module team asks what honours expects on professional codes of conduct. Put it plainly: to a student, what you need to be able to do by the end; to staff, what the course must give evidence of. Ask: \"Which part of the professional code applied to your work this term?\" Do not read the list aloud, and present it as the floor, not the goal."
- statement: qaa/landscape-architecture-2024/4.4.b38
  forPractitioner: { text: "At threshold, graduates can recognise and respect the ethical, moral, social and ecological issues of the subject.", rewrite: light, force: threshold, status: drafted }
  forBeneficiary: { text: "To reach the threshold, you will be able to see and respect the moral, ethical, ecological and social questions landscape work raises.", rewrite: full, force: threshold, status: drafted }
  author-agent-written: "Present this as a threshold standard: the least every honours graduate in the subject has shown, at FHEQ level 6 and FQHEIS level 10, under the self-management and professional development group (QAA, 2024, Landscape Architecture Subject Benchmark Statement, para 4.4). Describe it as the moral, ethical, ecological and social issues of the subject; do not call it a regulation or apply it to the master's list in 4.7. Set it beside the honours descriptor qaa/fheq-2024/4.15.b4, the Annex D third-class cell qaa/fheq-2024/annex-d/transferable/r5/3rd, spine:6, the neighbouring items 4.4.b37, 4.4.b39 and the typical rung 4.5.b2."
  author-agent-dialogue: "Raise it when a student or a module team asks what honours expects on the moral, ethical, ecological and social issues of the subject. Put it plainly: to a student, what you need to be able to do by the end; to staff, what the course must give evidence of. Ask: \"Who gains and who loses from this scheme, people and nature alike?\" Do not read the list aloud, and present it as the floor, not the goal."
- statement: qaa/landscape-architecture-2024/4.4.b39
  forPractitioner: { text: "At threshold, graduates can develop and display generic skills to gain new competencies for employability, career progression and CPD.", rewrite: light, force: threshold, status: drafted }
  forBeneficiary: { text: "To reach the threshold, you will be able to build and show the general skills you need to keep learning for work, career and professional development.", rewrite: full, force: threshold, status: drafted }
  author-agent-written: "Present this as a threshold standard: the least every honours graduate in the subject has shown, at FHEQ level 6 and FQHEIS level 10, under the self-management and professional development group (QAA, 2024, Landscape Architecture Subject Benchmark Statement, para 4.4). Describe it as generic skills for employability and professional development; do not call it a regulation or apply it to the master's list in 4.7. Set it beside the honours descriptor qaa/fheq-2024/4.15.b9.3, the Annex D third-class cell qaa/fheq-2024/annex-d/transferable/r3/3rd, spine:6, the neighbouring items 4.4.b38 and the typical rung 4.5.b2."
  author-agent-dialogue: "Raise it when a student or a module team asks what honours expects on generic skills for employability and professional development. Put it plainly: to a student, what you need to be able to do by the end; to staff, what the course must give evidence of. Ask: \"Which skill will you need next in your career, and how will you get it?\" Do not read the list aloud, and present it as the floor, not the goal."
- statement: qaa/landscape-architecture-2024/4.4.b40
  forPractitioner: { text: "At threshold, graduates can identify and apply hardware and software fitted to the scale of work to communicate proposals to varied audiences.", rewrite: light, force: threshold, status: drafted }
  forBeneficiary: { text: "To reach the threshold, you will be able to choose and use the right hardware and software for the job to share your proposals with different audiences.", rewrite: full, force: threshold, status: drafted }
  author-agent-written: "Present this as a threshold standard: the least every honours graduate in the subject has shown, at FHEQ level 6 and FQHEIS level 10, under the digital literacy group (QAA, 2024, Landscape Architecture Subject Benchmark Statement, para 4.4). Describe it as hardware and software for communicating proposals; do not call it a regulation or apply it to the master's list in 4.7. Set it beside the honours descriptor qaa/fheq-2024/4.15.b8, the Annex D third-class cell qaa/fheq-2024/annex-d/transferable/r1/3rd, spine:6, the neighbouring items 4.4.b41 and the typical rung 4.5.b2."
  author-agent-dialogue: "Raise it when a student or a module team asks what honours expects on hardware and software for communicating proposals. Put it plainly: to a student, what you need to be able to do by the end; to staff, what the course must give evidence of. Ask: \"Why did you pick this software for this audience?\" Do not read the list aloud, and present it as the floor, not the goal."
- statement: qaa/landscape-architecture-2024/4.4.b41
  forPractitioner: { text: "At threshold, graduates can use the internet and social media appropriately for communication and as an information source.", rewrite: light, force: threshold, status: drafted }
  forBeneficiary: { text: "To reach the threshold, you will be able to use the internet and social media sensibly to communicate and find information.", rewrite: full, force: threshold, status: drafted }
  author-agent-written: "Present this as a threshold standard: the least every honours graduate in the subject has shown, at FHEQ level 6 and FQHEIS level 10, under the digital literacy group (QAA, 2024, Landscape Architecture Subject Benchmark Statement, para 4.4). Describe it as the internet and social media; do not call it a regulation or apply it to the master's list in 4.7. Set it beside the honours descriptor qaa/fheq-2024/4.15.b8, the Annex D third-class cell qaa/fheq-2024/annex-d/transferable/r1/3rd, spine:6, the neighbouring items 4.4.b40, 4.4.b42 and the typical rung 4.5.b2."
  author-agent-dialogue: "Raise it when a student or a module team asks what honours expects on the internet and social media. Put it plainly: to a student, what you need to be able to do by the end; to staff, what the course must give evidence of. Ask: \"How do you check that what you find online is reliable?\" Do not read the list aloud, and present it as the floor, not the goal."
- statement: qaa/landscape-architecture-2024/4.4.b42
  forPractitioner: { text: "At threshold, graduates are aware of emerging technologies and of effective, suitable ways to implement them.", rewrite: light, force: threshold, status: drafted }
  forBeneficiary: { text: "To reach the threshold, you will be able to keep aware of new technologies and how to use them well.", rewrite: full, force: threshold, status: drafted }
  author-agent-written: "Present this as a threshold standard: the least every honours graduate in the subject has shown, at FHEQ level 6 and FQHEIS level 10, under the digital literacy group (QAA, 2024, Landscape Architecture Subject Benchmark Statement, para 4.4). Describe it as awareness of emerging technologies; do not call it a regulation or apply it to the master's list in 4.7. Set it beside the honours descriptor qaa/fheq-2024/4.15.b9.3, the Annex D third-class cell qaa/fheq-2024/annex-d/transferable/r1/3rd, spine:6, the neighbouring items 4.4.b41, 4.4.b43 and the typical rung 4.5.b2."
  author-agent-dialogue: "Raise it when a student or a module team asks what honours expects on awareness of emerging technologies. Put it plainly: to a student, what you need to be able to do by the end; to staff, what the course must give evidence of. Ask: \"Which new tool have you tried lately, and was it worth it?\" Do not read the list aloud, and present it as the floor, not the goal."
- statement: qaa/landscape-architecture-2024/4.4.b43
  forPractitioner: { text: "At threshold, graduates can apply suitable technology legally and appropriately across survey, analysis and design: CAD, visualisation, GIS, BIM, fabrication, AI, AR and VR, drones and apps among them.", rewrite: light, force: threshold, status: drafted }
  forBeneficiary: { text: "To reach the threshold, you will be able to use the right digital tools legally and well through survey, analysis and design, such as CAD, GIS, BIM, 3D printing, AI, drones and survey apps.", rewrite: full, force: threshold, status: drafted }
  author-agent-written: "Present this as a threshold standard: the least every honours graduate in the subject has shown, at FHEQ level 6 and FQHEIS level 10, under the digital literacy group (QAA, 2024, Landscape Architecture Subject Benchmark Statement, para 4.4). Describe it as digital tools across survey, analysis and design; do not call it a regulation or apply it to the master's list in 4.7. Set it beside the honours descriptor qaa/fheq-2024/4.15.b2, the Annex D third-class cell qaa/fheq-2024/annex-d/practical/r3/3rd, spine:6, the neighbouring items 4.4.b42 and the typical rung 4.5.b3."
  author-agent-dialogue: "Raise it when a student or a module team asks what honours expects on digital tools across survey, analysis and design. Put it plainly: to a student, what you need to be able to do by the end; to staff, what the course must give evidence of. Ask: \"Which digital tool did you use at each stage of your last project, and was its use legal and fitting?\" Do not read the list aloud, and present it as the floor, not the goal."
- statement: qaa/landscape-architecture-2024/4.4.b44
  forPractitioner: { text: "At threshold, graduates can identify and engage diverse stakeholders at suitable project stages to test and inform research and proposals.", rewrite: light, force: threshold, status: drafted }
  forBeneficiary: { text: "To reach the threshold, you will be able to find and involve the different people with a stake in a project at the right moments, to test and shape your ideas.", rewrite: full, force: threshold, status: drafted }
  author-agent-written: "Present this as a threshold standard: the least every honours graduate in the subject has shown, at FHEQ level 6 and FQHEIS level 10, under the communication group (QAA, 2024, Landscape Architecture Subject Benchmark Statement, para 4.4). Describe it as engaging diverse stakeholders; do not call it a regulation or apply it to the master's list in 4.7. Set it beside the honours descriptor qaa/fheq-2024/4.15.b8, the Annex D third-class cell qaa/fheq-2024/annex-d/transferable/r2/3rd, spine:6, the neighbouring items 4.4.b45 and the typical rung 4.5.b3."
  author-agent-dialogue: "Raise it when a student or a module team asks what honours expects on engaging diverse stakeholders. Put it plainly: to a student, what you need to be able to do by the end; to staff, what the course must give evidence of. Ask: \"Who did you consult, at which stage, and what changed as a result?\" Do not read the list aloud, and present it as the floor, not the goal."
- statement: qaa/landscape-architecture-2024/4.4.b45
  forPractitioner: { text: "At threshold, graduates can understand, select and apply approaches, tools and techniques suited to the audience and the material.", rewrite: light, force: threshold, status: drafted }
  forBeneficiary: { text: "To reach the threshold, you will be able to choose and use ways of communicating that suit both the audience and what you are showing.", rewrite: full, force: threshold, status: drafted }
  author-agent-written: "Present this as a threshold standard: the least every honours graduate in the subject has shown, at FHEQ level 6 and FQHEIS level 10, under the communication group (QAA, 2024, Landscape Architecture Subject Benchmark Statement, para 4.4). Describe it as matching communication to audience and material; do not call it a regulation or apply it to the master's list in 4.7. Set it beside the honours descriptor qaa/fheq-2024/4.15.b8, the Annex D third-class cell qaa/fheq-2024/annex-d/practical/r4/3rd, spine:6, the neighbouring items 4.4.b44, 4.4.b46 and the typical rung 4.5.b2."
  author-agent-dialogue: "Raise it when a student or a module team asks what honours expects on matching communication to audience and material. Put it plainly: to a student, what you need to be able to do by the end; to staff, what the course must give evidence of. Ask: \"How would you present this scheme differently to a council committee and to residents?\" Do not read the list aloud, and present it as the floor, not the goal."
- statement: qaa/landscape-architecture-2024/4.4.b46
  forPractitioner: { text: "At threshold, graduates can make communication inclusive and accessible to as wide a range of people as possible, particularly minority groups and those with diverse needs.", rewrite: light, force: threshold, status: drafted }
  forBeneficiary: { text: "To reach the threshold, you will be able to make your communication inclusive and accessible to as many people as possible, especially those often left out.", rewrite: full, force: threshold, status: drafted }
  author-agent-written: "Present this as a threshold standard: the least every honours graduate in the subject has shown, at FHEQ level 6 and FQHEIS level 10, under the communication group (QAA, 2024, Landscape Architecture Subject Benchmark Statement, para 4.4). Describe it as inclusive and accessible communication; do not call it a regulation or apply it to the master's list in 4.7. Set it beside the honours descriptor qaa/fheq-2024/4.15.b8, the Annex D third-class cell qaa/fheq-2024/annex-d/transferable/r1/3rd, spine:6, the neighbouring items 4.4.b45, 4.4.b47 and the typical rung 4.5.b2."
  author-agent-dialogue: "Raise it when a student or a module team asks what honours expects on inclusive and accessible communication. Put it plainly: to a student, what you need to be able to do by the end; to staff, what the course must give evidence of. Ask: \"Who might not be able to read or reach your materials, and what would help them?\" Do not read the list aloud, and present it as the floor, not the goal."
- statement: qaa/landscape-architecture-2024/4.4.b47
  forPractitioner: { text: "At threshold, graduates can communicate clearly, concisely, confidently and appropriately to varied audiences in written, spoken and graphic forms, including models and visual media.", rewrite: light, force: threshold, status: drafted }
  forBeneficiary: { text: "To reach the threshold, you will be able to communicate clearly, briefly and confidently in writing, speech, drawings and models to different audiences.", rewrite: full, force: threshold, status: drafted }
  author-agent-written: "Present this as a threshold standard: the least every honours graduate in the subject has shown, at FHEQ level 6 and FQHEIS level 10, under the communication group (QAA, 2024, Landscape Architecture Subject Benchmark Statement, para 4.4). Describe it as clear communication in written, verbal and graphic forms; do not call it a regulation or apply it to the master's list in 4.7. Set it beside the honours descriptor qaa/fheq-2024/4.15.b8, the Annex D third-class cell qaa/fheq-2024/annex-d/transferable/r1/3rd, spine:6, the neighbouring items 4.4.b46, 4.4.b48 and the typical rung 4.5.b2."
  author-agent-dialogue: "Raise it when a student or a module team asks what honours expects on clear communication in written, verbal and graphic forms. Put it plainly: to a student, what you need to be able to do by the end; to staff, what the course must give evidence of. Ask: \"Could someone grasp your main idea from your boards in a minute?\" Do not read the list aloud, and present it as the floor, not the goal."
- statement: qaa/landscape-architecture-2024/4.4.b48
  forPractitioner: { text: "At threshold, graduates can communicate accurately where they can, and where they cannot (as with illustrative graphics) make the limits of the output clear.", rewrite: light, force: threshold, status: drafted }
  forBeneficiary: { text: "To reach the threshold, you will be able to be accurate where you can, and where an image is only illustrative, say so clearly.", rewrite: full, force: threshold, status: drafted }
  author-agent-written: "Present this as a threshold standard: the least every honours graduate in the subject has shown, at FHEQ level 6 and FQHEIS level 10, under the communication group (QAA, 2024, Landscape Architecture Subject Benchmark Statement, para 4.4). Describe it as accuracy and the limits of illustrative outputs; do not call it a regulation or apply it to the master's list in 4.7. Set it beside the honours descriptor qaa/fheq-2024/4.15.b8, the Annex D third-class cell qaa/fheq-2024/annex-d/practical/r4/3rd, spine:6, the neighbouring items 4.4.b47, 4.4.b49 and the typical rung 4.5.b2."
  author-agent-dialogue: "Raise it when a student or a module team asks what honours expects on accuracy and the limits of illustrative outputs. Put it plainly: to a student, what you need to be able to do by the end; to staff, what the course must give evidence of. Ask: \"What does this visualisation show accurately, and what is artistic licence?\" Do not read the list aloud, and present it as the floor, not the goal."
- statement: qaa/landscape-architecture-2024/4.4.b49
  forPractitioner: { text: "At threshold, graduates can explore and use emerging digital tools such as AI to prepare communication and presentations, ensuring the outputs are appropriate and accurate.", rewrite: light, force: threshold, status: drafted }
  forBeneficiary: { text: "To reach the threshold, you will be able to try new digital tools such as AI when preparing material, and check that what they produce is accurate and fit to use.", rewrite: full, force: threshold, status: drafted }
  author-agent-written: "Present this as a threshold standard: the least every honours graduate in the subject has shown, at FHEQ level 6 and FQHEIS level 10, under the communication group (QAA, 2024, Landscape Architecture Subject Benchmark Statement, para 4.4). Describe it as using AI and emerging digital tools in communication; do not call it a regulation or apply it to the master's list in 4.7. Set it beside the honours descriptor qaa/fheq-2024/4.15.b8, the Annex D third-class cell qaa/fheq-2024/annex-d/transferable/r1/3rd, spine:6, the neighbouring items 4.4.b48 and the typical rung 4.5.b2."
  author-agent-dialogue: "Raise it when a student or a module team asks what honours expects on using AI and emerging digital tools in communication. Put it plainly: to a student, what you need to be able to do by the end; to staff, what the course must give evidence of. Ask: \"Where did AI help your presentation, and how did you check its output?\" Do not read the list aloud, and present it as the floor, not the goal."
- statement: qaa/landscape-architecture-2024/4.4.b50
  forPractitioner: { text: "At threshold, graduates can contribute confidently and effectively to setting group aims, objectives and roles.", rewrite: light, force: threshold, status: drafted }
  forBeneficiary: { text: "To reach the threshold, you will be able to help your group agree its aims and who does what, with confidence.", rewrite: full, force: threshold, status: drafted }
  author-agent-written: "Present this as a threshold standard: the least every honours graduate in the subject has shown, at FHEQ level 6 and FQHEIS level 10, under the interpersonal and teamwork group (QAA, 2024, Landscape Architecture Subject Benchmark Statement, para 4.4). Describe it as setting group aims and roles; do not call it a regulation or apply it to the master's list in 4.7. Set it beside the honours descriptor qaa/fheq-2024/4.15.b9.1, the Annex D third-class cell qaa/fheq-2024/annex-d/transferable/r2/3rd, spine:6, the neighbouring items 4.4.b51 and the typical rung 4.5.b2."
  author-agent-dialogue: "Raise it when a student or a module team asks what honours expects on setting group aims and roles. Put it plainly: to a student, what you need to be able to do by the end; to staff, what the course must give evidence of. Ask: \"How did your group agree who would do what?\" Do not read the list aloud, and present it as the floor, not the goal."
- statement: qaa/landscape-architecture-2024/4.4.b51
  forPractitioner: { text: "At threshold, graduates can contribute constructively and sensitively to group discussion, considering and respecting others' views, particularly from diverse life experiences.", rewrite: light, force: threshold, status: drafted }
  forBeneficiary: { text: "To reach the threshold, you will be able to take part in group discussions constructively and with care, listening to and respecting views unlike your own.", rewrite: full, force: threshold, status: drafted }
  author-agent-written: "Present this as a threshold standard: the least every honours graduate in the subject has shown, at FHEQ level 6 and FQHEIS level 10, under the interpersonal and teamwork group (QAA, 2024, Landscape Architecture Subject Benchmark Statement, para 4.4). Describe it as respectful, constructive group discussion; do not call it a regulation or apply it to the master's list in 4.7. Set it beside the honours descriptor qaa/fheq-2024/4.15.b9.1, the Annex D third-class cell qaa/fheq-2024/annex-d/transferable/r2/3rd, spine:6, the neighbouring items 4.4.b50, 4.4.b52 and the typical rung 4.5.b2."
  author-agent-dialogue: "Raise it when a student or a module team asks what honours expects on respectful, constructive group discussion. Put it plainly: to a student, what you need to be able to do by the end; to staff, what the course must give evidence of. Ask: \"When someone in your group disagreed, how did you weigh their view?\" Do not read the list aloud, and present it as the floor, not the goal."
- statement: qaa/landscape-architecture-2024/4.4.b52
  forPractitioner: { text: "At threshold, graduates can apply knowledge and critical thinking to multidisciplinary problems and offer comprehensive, holistic solutions.", rewrite: light, force: threshold, status: drafted }
  forBeneficiary: { text: "To reach the threshold, you will be able to bring what you know and think to problems that cross disciplines, and offer joined-up answers.", rewrite: full, force: threshold, status: drafted }
  author-agent-written: "Present this as a threshold standard: the least every honours graduate in the subject has shown, at FHEQ level 6 and FQHEIS level 10, under the interpersonal and teamwork group (QAA, 2024, Landscape Architecture Subject Benchmark Statement, para 4.4). Describe it as multidisciplinary problems and holistic solutions; do not call it a regulation or apply it to the master's list in 4.7. Set it beside the honours descriptor qaa/fheq-2024/4.15.b3.1, the Annex D third-class cell qaa/fheq-2024/annex-d/cognitive/r3/3rd, spine:6, the neighbouring items 4.4.b51, 4.4.b53 and the typical rung 4.5.b2."
  author-agent-dialogue: "Raise it when a student or a module team asks what honours expects on multidisciplinary problems and holistic solutions. Put it plainly: to a student, what you need to be able to do by the end; to staff, what the course must give evidence of. Ask: \"Which other discipline did your solution depend on, and how did you work with it?\" Do not read the list aloud, and present it as the floor, not the goal."
- statement: qaa/landscape-architecture-2024/4.4.b53
  forPractitioner: { text: "At threshold, graduates can contribute effectively to group outputs, including reports and presentations.", rewrite: light, force: threshold, status: drafted }
  forBeneficiary: { text: "To reach the threshold, you will be able to play your full part in producing a group's reports and presentations.", rewrite: full, force: threshold, status: drafted }
  author-agent-written: "Present this as a threshold standard: the least every honours graduate in the subject has shown, at FHEQ level 6 and FQHEIS level 10, under the interpersonal and teamwork group (QAA, 2024, Landscape Architecture Subject Benchmark Statement, para 4.4). Describe it as contributing to group outputs; do not call it a regulation or apply it to the master's list in 4.7. Set it beside the honours descriptor qaa/fheq-2024/4.15.b8, the Annex D third-class cell qaa/fheq-2024/annex-d/transferable/r2/3rd, spine:6, the neighbouring items 4.4.b52, 4.4.b54 and the typical rung 4.5.b2."
  author-agent-dialogue: "Raise it when a student or a module team asks what honours expects on contributing to group outputs. Put it plainly: to a student, what you need to be able to do by the end; to staff, what the course must give evidence of. Ask: \"What was your part in the group report?\" Do not read the list aloud, and present it as the floor, not the goal."
- statement: qaa/landscape-architecture-2024/4.4.b54
  forPractitioner: { text: "At threshold, graduates can show they can lead a group in a range of projects.", rewrite: light, force: threshold, status: drafted }
  forBeneficiary: { text: "To reach the threshold, you will be able to lead a group on different kinds of project.", rewrite: full, force: threshold, status: drafted }
  author-agent-written: "Present this as a threshold standard: the least every honours graduate in the subject has shown, at FHEQ level 6 and FQHEIS level 10, under the interpersonal and teamwork group (QAA, 2024, Landscape Architecture Subject Benchmark Statement, para 4.4). Describe it as leading a group; do not call it a regulation or apply it to the master's list in 4.7. Set it beside the honours descriptor qaa/fheq-2024/4.15.b9.1, the Annex D third-class cell qaa/fheq-2024/annex-d/transferable/r2/3rd, spine:6, the neighbouring items 4.4.b53, 4.4.b55 and the typical rung 4.5.b2."
  author-agent-dialogue: "Raise it when a student or a module team asks what honours expects on leading a group. Put it plainly: to a student, what you need to be able to do by the end; to staff, what the course must give evidence of. Ask: \"When did you last lead a group, and what did you learn?\" Do not read the list aloud, and present it as the floor, not the goal."
- statement: qaa/landscape-architecture-2024/4.4.b55
  forPractitioner: { text: "At threshold, graduates can show they can work under another's lead in a group across varied projects.", rewrite: light, force: threshold, status: drafted }
  forBeneficiary: { text: "To reach the threshold, you will be able to work well under someone else's lead in a group.", rewrite: full, force: threshold, status: drafted }
  author-agent-written: "Present this as a threshold standard: the least every honours graduate in the subject has shown, at FHEQ level 6 and FQHEIS level 10, under the interpersonal and teamwork group (QAA, 2024, Landscape Architecture Subject Benchmark Statement, para 4.4). Describe it as being led as part of a group; do not call it a regulation or apply it to the master's list in 4.7. Set it beside the honours descriptor qaa/fheq-2024/4.15.b9.1, the Annex D third-class cell qaa/fheq-2024/annex-d/transferable/r2/3rd, spine:6, the neighbouring items 4.4.b54, 4.4.b56 and the typical rung 4.5.b2."
  author-agent-dialogue: "Raise it when a student or a module team asks what honours expects on being led as part of a group. Put it plainly: to a student, what you need to be able to do by the end; to staff, what the course must give evidence of. Ask: \"How did you support the person leading your group?\" Do not read the list aloud, and present it as the floor, not the goal."
- statement: qaa/landscape-architecture-2024/4.4.b56
  forPractitioner: { text: "At threshold, graduates can show awareness of the interdisciplinary nature and processes of community engagement and consultation.", rewrite: light, force: threshold, status: drafted }
  forBeneficiary: { text: "To reach the threshold, you will be able to show you understand how community engagement and consultation work and who takes part in them.", rewrite: full, force: threshold, status: drafted }
  author-agent-written: "Present this as a threshold standard: the least every honours graduate in the subject has shown, at FHEQ level 6 and FQHEIS level 10, under the interpersonal and teamwork group (QAA, 2024, Landscape Architecture Subject Benchmark Statement, para 4.4). Describe it as community engagement and consultation; do not call it a regulation or apply it to the master's list in 4.7. Set it beside the honours descriptor qaa/fheq-2024/4.15.b1, the Annex D third-class cell qaa/fheq-2024/annex-d/knowledge/r3/3rd, spine:6, the neighbouring items 4.4.b55 and the typical rung 4.5.b1."
  author-agent-dialogue: "Raise it when a student or a module team asks what honours expects on community engagement and consultation. Put it plainly: to a student, what you need to be able to do by the end; to staff, what the course must give evidence of. Ask: \"Which professions took part in the consultation you saw, and what did each bring?\" Do not read the list aloud, and present it as the floor, not the goal."
- statement: qaa/landscape-architecture-2024/4.5.b1
  forPractitioner: { text: "At the typical standard, graduates have met all required course outcomes and shown advanced knowledge, understanding and cognitive, practical and transferable skills, consistently.", rewrite: light, force: describes, status: drafted }
  forBeneficiary: { text: "At the typical standard, you have met every outcome your course sets and shown advanced knowledge and skills, consistently.", rewrite: full, force: describes, status: drafted }
  author-agent-written: "Present this as the typical standard, which the statement describes as going beyond threshold for honours, at FHEQ level 6 and FQHEIS level 10 (QAA, 2024, Landscape Architecture Subject Benchmark Statement, para 4.5). It builds on the whole threshold list in 4.4, not on one item, and the issuer gives it no modal: do not present it as a requirement for the award. Set it beside 4.6.b1, the Annex D upper second (2.1) cell qaa/fheq-2024/annex-d/summary/r1/2.1 and spine:6."
  author-agent-dialogue: "Raise it when a student who has met the basics asks how to do better, or when staff write criteria above the pass. Put it to a student as what stronger work looks like for you; to staff, as a description to calibrate against. Ask: \"Across your modules, where have you gone past simply meeting the outcomes?\" Never present this rung as the minimum."
- statement: qaa/landscape-architecture-2024/4.5.b2
  forPractitioner: { text: "At the typical standard, graduates apply the threshold knowledge, understanding and skills with more critical reflection, personal responsibility and independence.", rewrite: light, force: describes, status: drafted }
  forBeneficiary: { text: "At the typical standard, you use the threshold knowledge and skills with more critical reflection and take more responsibility for your own work.", rewrite: full, force: describes, status: drafted }
  author-agent-written: "Present this as the typical standard, which the statement describes as going beyond threshold for honours, at FHEQ level 6 and FQHEIS level 10 (QAA, 2024, Landscape Architecture Subject Benchmark Statement, para 4.5). It builds on the whole threshold list in 4.4, not on one item, and the issuer gives it no modal: do not present it as a requirement for the award. Set it beside 4.6.b2, the Annex D upper second (2.1) cell qaa/fheq-2024/annex-d/summary/r3/2.1 and spine:6."
  author-agent-dialogue: "Raise it when a student who has met the basics asks how to do better, or when staff write criteria above the pass. Put it to a student as what stronger work looks like for you; to staff, as a description to calibrate against. Ask: \"Where did you decide something for yourself rather than wait to be told?\" Never present this rung as the minimum."
- statement: qaa/landscape-architecture-2024/4.5.b3
  forPractitioner: { text: "At the typical standard, graduates apply and execute the threshold knowledge and skills effectively, showing more insight, initiative, strong problem-solving and creativity.", rewrite: light, force: describes, status: drafted }
  forBeneficiary: { text: "At the typical standard, you put the threshold skills to work well, with more insight, initiative, creativity and strong problem-solving.", rewrite: full, force: describes, status: drafted }
  author-agent-written: "Present this as the typical standard, which the statement describes as going beyond threshold for honours, at FHEQ level 6 and FQHEIS level 10 (QAA, 2024, Landscape Architecture Subject Benchmark Statement, para 4.5). It builds on the whole threshold list in 4.4, not on one item, and the issuer gives it no modal: do not present it as a requirement for the award. Set it beside 4.6.b3, the Annex D upper second (2.1) cell qaa/fheq-2024/annex-d/summary/r4/2.1 and spine:6."
  author-agent-dialogue: "Raise it when a student who has met the basics asks how to do better, or when staff write criteria above the pass. Put it to a student as what stronger work looks like for you; to staff, as a description to calibrate against. Ask: \"Which problem in your project did you solve in a way you are proud of?\" Never present this rung as the minimum."
- statement: qaa/landscape-architecture-2024/4.6.b1
  forPractitioner: { text: "At the excellent standard, graduates have met all required course outcomes and shown strong knowledge, understanding and cognitive, practical and transferable skills.", rewrite: light, force: describes, status: drafted }
  forBeneficiary: { text: "At the excellent standard, you have met every outcome your course sets and shown strong knowledge and skills across the board.", rewrite: full, force: describes, status: drafted }
  author-agent-written: "Present this as the excellent standard, which the statement describes as going beyond typical for honours, at FHEQ level 6 and FQHEIS level 10 (QAA, 2024, Landscape Architecture Subject Benchmark Statement, para 4.6). It builds on the whole threshold list in 4.4, not on one item, and the issuer gives it no modal: do not present it as a requirement for the award. Set it beside 4.5.b1, the Annex D first (1st) cell qaa/fheq-2024/annex-d/summary/r1/1st and spine:6."
  author-agent-dialogue: "Raise it when a student who has met the basics asks how to do better, or when staff write criteria above the pass. Put it to a student as what stronger work looks like for you; to staff, as a description to calibrate against. Ask: \"What would show an examiner that your knowledge is strong, not only sufficient?\" Never present this rung as the minimum."
- statement: qaa/landscape-architecture-2024/4.6.b2
  forPractitioner: { text: "At the excellent standard, graduates apply the threshold knowledge and skills with greater originality, independent critical reflection, responsibility, autonomy and leadership, and clear professional and ethical awareness.", rewrite: light, force: describes, status: drafted }
  forBeneficiary: { text: "At the excellent standard, you use the threshold knowledge and skills with real originality, reflect critically on your own, lead others and show clear professional and ethical judgement.", rewrite: full, force: describes, status: drafted }
  author-agent-written: "Present this as the excellent standard, which the statement describes as going beyond typical for honours, at FHEQ level 6 and FQHEIS level 10 (QAA, 2024, Landscape Architecture Subject Benchmark Statement, para 4.6). It builds on the whole threshold list in 4.4, not on one item, and the issuer gives it no modal: do not present it as a requirement for the award. Set it beside 4.5.b2, the Annex D first (1st) cell qaa/fheq-2024/annex-d/summary/r3/1st and spine:6."
  author-agent-dialogue: "Raise it when a student who has met the basics asks how to do better, or when staff write criteria above the pass. Put it to a student as what stronger work looks like for you; to staff, as a description to calibrate against. Ask: \"Where did you lead, and what ethical judgement did you have to make?\" Never present this rung as the minimum."
- statement: qaa/landscape-architecture-2024/4.6.b3
  forPractitioner: { text: "At the excellent standard, graduates apply and execute the threshold knowledge and skills fluently and effectively, with greater originality, insight, novel approaches and exceptional initiative and problem-solving.", rewrite: light, force: describes, status: drafted }
  forBeneficiary: { text: "At the excellent standard, you put the threshold skills to work fluently, with original insight, new approaches and exceptional initiative in solving problems.", rewrite: full, force: describes, status: drafted }
  author-agent-written: "Present this as the excellent standard, which the statement describes as going beyond typical for honours, at FHEQ level 6 and FQHEIS level 10 (QAA, 2024, Landscape Architecture Subject Benchmark Statement, para 4.6). It builds on the whole threshold list in 4.4, not on one item, and the issuer gives it no modal: do not present it as a requirement for the award. Set it beside 4.5.b3, the Annex D first (1st) cell qaa/fheq-2024/annex-d/summary/r4/1st and spine:6."
  author-agent-dialogue: "Raise it when a student who has met the basics asks how to do better, or when staff write criteria above the pass. Put it to a student as what stronger work looks like for you; to staff, as a description to calibrate against. Ask: \"What in your work did nobody show you how to do?\" Never present this rung as the minimum."
- statement: qaa/landscape-architecture-2024/4.7.b1
  forPractitioner: { text: "Master's graduates at threshold will also show a questioning and critical approach.", rewrite: light, force: will, status: drafted }
  forBeneficiary: { text: "As a master's graduate, you will show that you question and think critically.", rewrite: full, force: will, status: drafted }
  author-agent-written: "Present this as a threshold standard for master's graduates in the subject, at FHEQ level 7 and FQHEIS level 11, held in addition to the honours list (QAA, 2024, Landscape Architecture Subject Benchmark Statement, para 4.7). It carries will-force; do not apply it to the honours award or claim it is the LI's accreditation rule. Set it beside the master's descriptor qaa/fheq-2024/4.17.b4.1, spine:7 and the neighbouring items 4.7.b2."
  author-agent-dialogue: "Raise it with a master's student, or a team designing a master's, when the talk turns to what lifts work above honours. Put it plainly, in the second person for a student and as an outcome to evidence for staff. Ask: \"What assumption in your field have you questioned this year?\" Do not read the list aloud or treat it as an aspiration; it is the master's minimum."
- statement: qaa/landscape-architecture-2024/4.7.b2
  forPractitioner: { text: "Master's graduates at threshold will also show a capacity for critical reflection.", rewrite: light, force: will, status: drafted }
  forBeneficiary: { text: "As a master's graduate, you will show that you can reflect critically on your work and ideas.", rewrite: full, force: will, status: drafted }
  author-agent-written: "Present this as a threshold standard for master's graduates in the subject, at FHEQ level 7 and FQHEIS level 11, held in addition to the honours list (QAA, 2024, Landscape Architecture Subject Benchmark Statement, para 4.7). It carries will-force; do not apply it to the honours award or claim it is the LI's accreditation rule. Set it beside the master's descriptor qaa/fheq-2024/4.17.b4.1, spine:7 and the neighbouring items 4.7.b1, 4.7.b3."
  author-agent-dialogue: "Raise it with a master's student, or a team designing a master's, when the talk turns to what lifts work above honours. Put it plainly, in the second person for a student and as an outcome to evidence for staff. Ask: \"What did reflecting on that project change in how you work?\" Do not read the list aloud or treat it as an aspiration; it is the master's minimum."
- statement: qaa/landscape-architecture-2024/4.7.b3
  forPractitioner: { text: "Master's graduates at threshold will also show a capacity for independent thought and action.", rewrite: light, force: will, status: drafted }
  forBeneficiary: { text: "As a master's graduate, you will show that you can think and act on your own.", rewrite: full, force: will, status: drafted }
  author-agent-written: "Present this as a threshold standard for master's graduates in the subject, at FHEQ level 7 and FQHEIS level 11, held in addition to the honours list (QAA, 2024, Landscape Architecture Subject Benchmark Statement, para 4.7). It carries will-force; do not apply it to the honours award or claim it is the LI's accreditation rule. Set it beside the master's descriptor qaa/fheq-2024/4.17.b6, spine:7 and the neighbouring items 4.7.b2, 4.7.b4."
  author-agent-dialogue: "Raise it with a master's student, or a team designing a master's, when the talk turns to what lifts work above honours. Put it plainly, in the second person for a student and as an outcome to evidence for staff. Ask: \"Which part of your project did you steer entirely yourself?\" Do not read the list aloud or treat it as an aspiration; it is the master's minimum."
- statement: qaa/landscape-architecture-2024/4.7.b4
  forPractitioner: { text: "Master's graduates at threshold will also show greater originality, insight and critical reflection than at honours.", rewrite: light, force: will, status: drafted }
  forBeneficiary: { text: "As a master's graduate, you will show more originality, insight and critical reflection than at honours.", rewrite: full, force: will, status: drafted }
  author-agent-written: "Present this as a threshold standard for master's graduates in the subject, at FHEQ level 7 and FQHEIS level 11, held in addition to the honours list (QAA, 2024, Landscape Architecture Subject Benchmark Statement, para 4.7). It carries will-force; do not apply it to the honours award or claim it is the LI's accreditation rule. Set it beside the master's descriptor qaa/fheq-2024/4.17.b3, spine:7 and the neighbouring items 4.7.b3, 4.7.b5."
  author-agent-dialogue: "Raise it with a master's student, or a team designing a master's, when the talk turns to what lifts work above honours. Put it plainly, in the second person for a student and as an outcome to evidence for staff. Ask: \"What is original in your proposal?\" Do not read the list aloud or treat it as an aspiration; it is the master's minimum."
- statement: qaa/landscape-architecture-2024/4.7.b5
  forPractitioner: { text: "Master's graduates at threshold will also be able to synthesise and integrate concepts and ideas and relate them to practical contexts.", rewrite: light, force: will, status: drafted }
  forBeneficiary: { text: "As a master's graduate, you will show that you can bring ideas together and connect them to real practice.", rewrite: full, force: will, status: drafted }
  author-agent-written: "Present this as a threshold standard for master's graduates in the subject, at FHEQ level 7 and FQHEIS level 11, held in addition to the honours list (QAA, 2024, Landscape Architecture Subject Benchmark Statement, para 4.7). It carries will-force; do not apply it to the honours award or claim it is the LI's accreditation rule. Set it beside the master's descriptor qaa/fheq-2024/4.17.b3, spine:7 and the neighbouring items 4.7.b4, 4.7.b6."
  author-agent-dialogue: "Raise it with a master's student, or a team designing a master's, when the talk turns to what lifts work above honours. Put it plainly, in the second person for a student and as an outcome to evidence for staff. Ask: \"How does the theory you used change what happens on site?\" Do not read the list aloud or treat it as an aspiration; it is the master's minimum."
- statement: qaa/landscape-architecture-2024/4.7.b6
  forPractitioner: { text: "Master's graduates at threshold will also show good awareness and understanding of professional practice, roles, responsibilities, ethics and values.", rewrite: light, force: will, status: drafted }
  forBeneficiary: { text: "As a master's graduate, you will show a good grasp of how the profession works: its roles, duties, ethics and values.", rewrite: full, force: will, status: drafted }
  author-agent-written: "Present this as a threshold standard for master's graduates in the subject, at FHEQ level 7 and FQHEIS level 11, held in addition to the honours list (QAA, 2024, Landscape Architecture Subject Benchmark Statement, para 4.7). It carries will-force; do not apply it to the honours award or claim it is the LI's accreditation rule. Set it beside the master's descriptor qaa/fheq-2024/4.17.b8.1, spine:7 and the neighbouring items 4.7.b5, 4.7.b7."
  author-agent-dialogue: "Raise it with a master's student, or a team designing a master's, when the talk turns to what lifts work above honours. Put it plainly, in the second person for a student and as an outcome to evidence for staff. Ask: \"What would your responsibilities be on a live project, and to whom?\" Do not read the list aloud or treat it as an aspiration; it is the master's minimum."
- statement: qaa/landscape-architecture-2024/4.7.b7
  forPractitioner: { text: "Master's graduates at threshold will also show professionalism in undertaking assignments.", rewrite: light, force: will, status: drafted }
  forBeneficiary: { text: "As a master's graduate, you will show professionalism in how you carry out your assignments.", rewrite: full, force: will, status: drafted }
  author-agent-written: "Present this as a threshold standard for master's graduates in the subject, at FHEQ level 7 and FQHEIS level 11, held in addition to the honours list (QAA, 2024, Landscape Architecture Subject Benchmark Statement, para 4.7). It carries will-force; do not apply it to the honours award or claim it is the LI's accreditation rule. Set it beside the master's descriptor qaa/fheq-2024/4.17.b8.1, spine:7 and the neighbouring items 4.7.b6, 4.7.b8."
  author-agent-dialogue: "Raise it with a master's student, or a team designing a master's, when the talk turns to what lifts work above honours. Put it plainly, in the second person for a student and as an outcome to evidence for staff. Ask: \"Would a client be happy with how you handled your last assignment?\" Do not read the list aloud or treat it as an aspiration; it is the master's minimum."
- statement: qaa/landscape-architecture-2024/4.7.b8
  forPractitioner: { text: "Master's graduates at threshold will also understand how to apply other methods for retrieving information and for collecting and analysing data.", rewrite: light, force: will, status: drafted }
  forBeneficiary: { text: "As a master's graduate, you will show that you understand different ways to find information and to collect and analyse data.", rewrite: full, force: will, status: drafted }
  author-agent-written: "Present this as a threshold standard for master's graduates in the subject, at FHEQ level 7 and FQHEIS level 11, held in addition to the honours list (QAA, 2024, Landscape Architecture Subject Benchmark Statement, para 4.7). It carries will-force; do not apply it to the honours award or claim it is the LI's accreditation rule. Set it beside the master's descriptor qaa/fheq-2024/4.17.b2, spine:7 and the neighbouring items 4.7.b7."
  author-agent-dialogue: "Raise it with a master's student, or a team designing a master's, when the talk turns to what lifts work above honours. Put it plainly, in the second person for a student and as an outcome to evidence for staff. Ask: \"Which other method could have answered your research question, and why did you not use it?\" Do not read the list aloud or treat it as an aspiration; it is the master's minimum."
```

### S5 Levels and alignment
<!-- label: both; status: drafted; basis: primary -->
```yaml
levels:
  - { id: "fheq:6", role: "cites", locator: "D1, 2.11" }
  - { id: "fqheis:10", role: "cites", locator: "D1, 2.11" }
  - { id: "fheq:7", role: "cites", locator: "D1, 2.14; 2.15; 2.19" }
  - { id: "fqheis:11", role: "cites", locator: "D1, 2.14; 2.19" }
  - { id: "fheq:4", role: "cites", locator: "D1, 2.19 (integrated master's, Levels 4 to 7)" }
  - { id: "fheq:5", role: "cites", locator: "D1, 2.19 (integrated master's, Levels 4 to 7)" }
  - { id: "fqheis:7", role: "cites", locator: "D1, 2.17 (FQHEIS Levels 7 to 10)" }
  - { id: "fqheis:8", role: "cites", locator: "D1, 2.17; 2.19" }
  - { id: "fqheis:9", role: "cites", locator: "D1, 2.17; 2.19" }
  - { id: "spine:6", role: "refers", locator: "std:ref:uk-framework R2 (honours standards, generic skills)" }
  - { id: "spine:7", role: "refers", locator: "std:ref:uk-framework R2 (master's standards in 4.7)" }
crosswalks:
  - { from: "fheq:6", to: "fqheis:10", relation: "equivalent", basis: "stated (D1, 2.11: degree with honours, FHEQ Level 6; FQHEIS Level 10)" }
  - { from: "fheq:7", to: "fqheis:11", relation: "equivalent", basis: "stated (D1, 2.14: Level 7 (FHEQ) or Level 11 (FQHEIS); 2.19)" }
```

### S6 Themes
<!-- label: both; status: drafted; basis: primary -->
```yaml
- { id: "theme:edi", role: "carries", carriedIn: ["1.13", "1.15", "1.18", "1.22", "1.23", "1.24", "2.23", "4.4"] }
- { id: "theme:accessibility", role: "carries", carriedIn: ["1.13", "1.15", "1.20", "1.22", "1.25", "2.23", "4.4"] }
- { id: "theme:esd", role: "carries", carriedIn: ["1.13", "1.15", "1.22", "1.26", "4.4"] }
- { id: "theme:enterprise", role: "carries", carriedIn: ["1.13", "1.16", "1.20", "1.22", "1.27", "2.10", "4.4"] }
- { id: "theme:generative-ai", role: "carries", carriedIn: ["3.14", "4.4"] }
```

### S7 Relations
<!-- label: both; status: drafted; basis: primary -->
```yaml
- { rel: "partOf", target: "collection: QAA Subject Benchmark Statements", note: "one of 54 held by stan" }
- { rel: "supersedes", target: "std:doc:qaa-landscape-architecture-2019-benchmarks (not yet ingested)", note: "the fourth edition, 2019, named in the advisory group list (section 6)" }
- { rel: "refersTo", target: "std:doc:qaa-fheq-2024-framework, Annex D", note: "the honours classification descriptions providers should refer to (4.3); also the Frameworks named in 4.2" }
- { rel: "refersTo", target: "std:doc:qaa-fheq-2024-framework", note: "FHEQ levels 4 to 7 (2.11, 2.14, 2.17, 2.19)" }
- { rel: "refersTo", target: "std:doc:qaa-fqheis-2024-framework", note: "FQHEIS levels 7 to 11 (2.11, 2.14, 2.17, 2.19)" }
- { rel: "thresholdAt", target: "std:ref:uk-framework, spine:6 and spine:7", note: "inferred: the honours rungs at spine:6, the master's list at spine:7" }
- { rel: "refersTo", target: "Landscape Institute competency framework, code of practice and accreditation criteria (not yet ingested)", note: "1.11, 1.15 to 1.17, 2.4 to 2.6" }
- { rel: "refersTo", target: "QAA Quality Code Advice and Guidance on Assessment; QAA Guiding Principles; External Examining Principles (not yet ingested)", note: "3.8; 2.27; front matter" }
- { rel: "readWith", target: "std:doc:qaa-advancehe-esd-2021-guidance", note: "inferred: listed in section 5 as Education for Sustainable Development Guidance; the sustainability theme (1.26)" }
- { rel: "readWith", target: "std:doc:qaa-enterprise-2018-guidance", note: "inferred: listed in section 5; the employability, enterprise and entrepreneurship theme (1.27)" }
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
- Both a long-standing profession and an academic subject, grounded in research across the arts, humanities and the physical, natural, environmental and social sciences, with analogue and digital representation as tools of analysis and communication (D1, 1.2).
- It asks what landscape means, how it forms and changes, how people use it, and how to conserve, restore and manage existing landscapes and create sustainable, resilient, inclusive ones for the future (D1, 1.3).
- It works on landscapes of every kind and scale, urban, rural and in between, across assessment, planning, design, management and conservation, and feeds national policy (D1, 1.4, 1.8).
- A place-focused discipline linking human and natural systems, sensitive to natural systems, cultural identity and heritage, and the pull between global and local decisions (D1, 1.6).
- It sees itself as the profession best placed to lead green infrastructure, making places rich in nature, healthy, thriving, well drained and climate positive (D1, 1.7).
- Its definition of landscape comes from the European Landscape Convention, which the UK has signed; the IFLA/UNESCO charter defines the landscape architect's role (D1, 1.19, 2.1, 2.2).
- Teaching centres on the design studio and on projects of rising scale and complexity that simulate practice, from site survey to specification (D1, 3.3 to 3.6).
- The professional route runs through LI accreditation and an accredited master's to chartered status (D1, 2.3, 2.15, 2.16).

### SB2 Themes in this subject
<!-- label: both; status: drafted; basis: primary -->
```yaml
- theme: theme:edi
  inThisSubject: "the LI's competencies on equality, diversity and inclusivity, its built-environment memorandum and landscape-sector declaration; inclusive curricula and EDI literacy for students; professional conduct with regard to equity, diversity and inclusion and inclusive group work (D1, 1.15, 1.18, 1.23, 1.24; 4.4)"
  statements: ["qaa/landscape-architecture-2024/4.4.b36", "qaa/landscape-architecture-2024/4.4.b46", "qaa/landscape-architecture-2024/4.4.b51"]
- theme: theme:accessibility
  inThisSubject: "the LI competency on inclusive environments; access to studios, resources and fieldwork and alternative forms of teaching and assessment; communication that reaches people with diverse needs; the LI broadening entry routes (D1, 1.15, 1.25, 2.23; 4.4)"
  statements: ["qaa/landscape-architecture-2024/1.25.b1", "qaa/landscape-architecture-2024/1.25.b2", "qaa/landscape-architecture-2024/4.4.b46"]
- theme: theme:esd
  inThisSubject: "named sustainability and education for sustainability: climate, resilience, systems thinking on biodiversity and natural capital, policy, regenerative design, case studies and materiality; creativity in a sustainable context and the sustainability of materials (D1, 1.15, 1.26; 4.4)"
  statements: ["qaa/landscape-architecture-2024/1.26.b1", "qaa/landscape-architecture-2024/1.26.b2", "qaa/landscape-architecture-2024/1.26.b3", "qaa/landscape-architecture-2024/1.26.b4", "qaa/landscape-architecture-2024/1.26.b5", "qaa/landscape-architecture-2024/1.26.b6", "qaa/landscape-architecture-2024/1.26.b7", "qaa/landscape-architecture-2024/4.4.b10", "qaa/landscape-architecture-2024/4.4.b11", "qaa/landscape-architecture-2024/4.4.b18"]
- theme: theme:enterprise
  inThisSubject: "implicit in the LI competencies (practice types, business, contracts, indemnity); courses may offer professional networks, industry standards, ethical practice and CPD; course design reflecting industry and employability (D1, 1.16, 1.27, 2.10; 4.4)"
  statements: ["qaa/landscape-architecture-2024/4.4.b39"]
- theme: theme:generative-ai
  inThisSubject: "generative AI challenges academic integrity and the design process, so openness and critical reflection are central; AI appears among the digital tools students use and in preparing communication (D1, 3.14; 4.4)"
  statements: ["qaa/landscape-architecture-2024/4.4.b43", "qaa/landscape-architecture-2024/4.4.b49"]
```

### SB3 Content and delivery
<!-- label: both; status: drafted; basis: primary -->
```yaml
areas:
  - { component: "1.6", gloss: "the sensitivities the discipline draws on: natural systems, cultural identity and heritage, global and local decision-making" }
  - { component: "3.2", gloss: "context: global to local; social, cultural, economic and environmental; law and planning policy; history; professional and ethical" }
  - { component: "3.2", gloss: "systems and process: landscape change, protected landscapes, green infrastructure, management, natural capital" }
  - { component: "3.2", gloss: "stakeholders: interdisciplinary working, users and uses, community participation" }
  - { component: "3.2", gloss: "delivery: research methods, site survey, landscape assessment, site design at many scales, masterplanning, placemaking, materials, contract administration, communication" }
practices:
  - { component: "3.3", kind: "teaching", gloss: "lectures, seminars, design exercises, site visits, tutorials, charettes and group work in a studio culture" }
  - { component: "3.4", kind: "learning", gloss: "projects that simulate practice, small and strategic" }
  - { component: "3.5", kind: "teaching", gloss: "cumulative projects from survey to management proposals" }
  - { component: "3.6", kind: "learning", gloss: "tutorials, critiques, peer discussion in the studio, collaborative projects with other courses or practices" }
  - { component: "3.7", kind: "learning", gloss: "placements and visiting practitioners" }
  - { component: "3.9", kind: "assessment", gloss: "formative and summative assessment at every level (3.10, 3.11 define them)" }
  - { component: "3.12", kind: "assessment", gloss: "portfolios, studio, lab and field work, writing, presentations, digital resources, examinations, a final self-led project, work-integrated assessment" }
  - { component: "3.13", kind: "assessment", gloss: "recognition of prior learning" }
  - { component: "3.14", kind: "assessment", gloss: "generative AI, integrity and openness" }
```

### SB4 Benchmark standards
<!-- label: both; status: drafted; basis: primary -->
```yaml
rungs:
  - { rung: "threshold", leadIn: "4.4", award: "bachelor's with honours", items: 56 }
  - { rung: "threshold", leadIn: "4.7", award: "master's", items: 8 }
  - { rung: "typical", leadIn: "4.5", award: "bachelor's with honours", items: 3 }
  - { rung: "excellent", leadIn: "4.6", award: "bachelor's with honours", items: 3 }
rungBases: "4.1: the threshold is the minimum for the honours award; 4.2: most students exceed it and the statement also describes typical and excellent standards, judged by the provider's marking schemes; typical and excellent each build on the whole threshold list (\"listed above\"), so no threshold item is paired with them. Threshold records: 64 in all, 56 honours and 8 master's."
outcomeLists:
  - { leadIn: "1.26", gloss: "understanding course content gives students chances to show, for sustainability", items: 7, award: ["none"] }
outcomes:
  - { outcome: "all outcomes met, with advanced then strong knowledge and skills", threshold: "none", typical: "qaa/landscape-architecture-2024/4.5.b1", excellent: "qaa/landscape-architecture-2024/4.6.b1", basis: "inferred", domain: "knowledge", award: "bachelor's with honours" }
  - { outcome: "reflection, responsibility and autonomy", threshold: "none", typical: "qaa/landscape-architecture-2024/4.5.b2", excellent: "qaa/landscape-architecture-2024/4.6.b2", basis: "inferred", domain: "generic-skill", award: "bachelor's with honours" }
  - { outcome: "application with insight, initiative and problem-solving", threshold: "none", typical: "qaa/landscape-architecture-2024/4.5.b3", excellent: "qaa/landscape-architecture-2024/4.6.b3", basis: "inferred", domain: "subject-skill", award: "bachelor's with honours" }
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
- { body: "Landscape Institute (LI)", says: "the royal chartered professional body for the landscape profession in the UK; a statutory consultee on national policy; sets the code of practice and the competency framework (which covers the four themes); accredits undergraduate and postgraduate courses against criteria; accredited courses map to the competency framework; reviews accredited courses through a Professional Review Group; the chartership route needs an accredited 180-credit level 7 master's; accredited master's graduates become associate members; leads EDI work in the sector (D1, 1.4, 1.9 to 1.12, 1.15 to 1.18, 2.3 to 2.9, 2.15, 2.16, 2.23, 2.28)", requirements: "not yet ingested: LI competency framework, code of practice and accreditation criteria (Part E)" }
- { body: "International Federation of Landscape Architects (IFLA)", says: "the international federation; does not accredit but sets broad standards for national accreditation; its global ethical principles align with the LI code; its charter with UNESCO defines the profession (D1, 1.9, 1.11, 1.17, 1.19)", requirements: "not yet ingested: IFLA/UNESCO charter and IFLA Global Ethical Principles (Part E)" }
- { body: "Royal Town Planning Institute (RTPI)", says: "a signatory of the 2022 built-environment EDI memorandum; a body some courses seek dual accreditation from (D1, 1.18, 2.22)", requirements: "not yet ingested (Part E)" }
- { body: "Royal Institute of British Architects (RIBA)", says: "a signatory of the 2022 EDI memorandum; a possible second accrediting body (D1, 1.18, 2.22)", requirements: "not yet ingested (Part E)" }
- { body: "Chartered Institute of Building (CIOB); Institution of Civil Engineers (ICE); Royal Institution of Chartered Surveyors (RICS)", says: "co-signatories of the 2022 EDI memorandum with the LI (D1, 1.18)", requirements: "not-applicable-by-design: named only as signatories" }
- { body: "Association of Professional Landscapers (APL); British Association of Landscape Industries (BALI); Society of Garden Designers (SGD)", says: "joined the LI in a 2022 declaration for a more diverse, inclusive landscape industry (D1, 1.18)", requirements: "not-applicable-by-design: named only as signatories" }
```

### SB6 Cross-cutting references
<!-- label: both; status: drafted; basis: primary -->
```yaml
themes:
  - { id: "theme:edi", named: "Equality, diversity and inclusion (EDI)", carriedIn: ["1.13", "1.15", "1.18", "1.22", "1.23", "1.24", "2.23", "4.4"], statements: ["4.4.b36", "4.4.b46", "4.4.b51"] }
  - { id: "theme:accessibility", named: "Accessibility (front matter: accessibility and the needs of disabled students)", carriedIn: ["1.13", "1.15", "1.20", "1.22", "1.25", "2.23", "4.4"], statements: ["1.25.b1", "1.25.b2", "4.4.b46"] }
  - { id: "theme:esd", named: "Sustainability; education for sustainability (front matter: education for sustainable development)", carriedIn: ["1.13", "1.15", "1.22", "1.26", "4.4"], statements: ["1.26.b1", "1.26.b2", "1.26.b3", "1.26.b4", "1.26.b5", "1.26.b6", "1.26.b7", "4.4.b10", "4.4.b11", "4.4.b18"] }
  - { id: "theme:enterprise", named: "Employability, enterprise and entrepreneurship education", carriedIn: ["1.13", "1.16", "1.20", "1.22", "1.27", "2.10", "4.4"], statements: ["4.4.b39"] }
  - { id: "theme:generative-ai", named: "Generative AI", carriedIn: ["3.14", "4.4"], statements: ["4.4.b43", "4.4.b49"] }
frameworks:
  - { framework: "fheq", levels: ["fheq:4", "fheq:5", "fheq:6", "fheq:7"], citedIn: ["2.11", "2.14", "2.17", "2.19", "4.2", "4.3"] }
  - { framework: "scqf", levels: ["fqheis:7", "fqheis:8", "fqheis:9", "fqheis:10", "fqheis:11"], citedIn: ["2.11", "2.14", "2.17", "2.19"] }
bodies:
  - { body: "Landscape Institute", citedIn: ["1.4", "1.9", "1.10", "1.11", "1.12", "1.15", "1.17", "1.18", "2.3", "2.4", "2.5", "2.6", "2.7", "2.8", "2.9", "2.10", "2.15", "2.16", "2.22", "2.23", "2.28"] }
  - { body: "International Federation of Landscape Architects", citedIn: ["1.9", "1.11", "1.17", "1.19"] }
  - { body: "Royal Town Planning Institute", citedIn: ["1.18", "2.22"] }
  - { body: "Royal Institute of British Architects", citedIn: ["1.18", "2.22"] }
  - { body: "Chartered Institute of Building; Institution of Civil Engineers; Royal Institution of Chartered Surveyors", citedIn: ["1.18"] }
  - { body: "Association of Professional Landscapers; British Association of Landscape Industries; Society of Garden Designers", citedIn: ["1.18"] }
sharedDocuments:
  - { document: "std:doc:qaa-fheq-2024-framework, Annex D", named: "Annex D in The Frameworks for Higher Education Qualifications of UK Degree-Awarding Bodies", citedIn: ["4.3"], role: "the four honours classifications providers should refer to" }
  - { document: "std:doc:qaa-fheq-2024-framework; std:doc:qaa-fqheis-2024-framework", named: "the Frameworks for Higher Education Qualifications of UK Degree-Awarding Bodies", citedIn: ["4.2", "4.3"], role: "marking above threshold in line with provider schemes" }
  - { document: "OfS Sector Recognised Standards (not ingested; regulator's, England)", named: "the Office for Students' Sector Recognised Standards", citedIn: ["4.2"], role: "standards in use in England" }
  - { document: "QAA Quality Code Advice and Guidance, Assessment; QAA Guiding Principles (not yet ingested)", named: "the QAA Guiding Principles and the Advice and Guidance document on Assessment", citedIn: ["3.8"], role: "design and delivery of assessment" }
  - { document: "QAA External Examining Principles (not yet ingested)", named: "the principles set out by QAA", citedIn: ["2.27"], role: "external examination" }
  - { document: "QAA Glossary (not ingested)", named: "QAA's Glossary", citedIn: ["front matter"], role: "explains unfamiliar terms" }
  - { document: "UN Sustainable Development Goals (external)", named: "the UN Sustainability Goals", citedIn: ["1.26"], role: "illustrate sustainability values and actions" }
  - { document: "European Landscape Convention (Council of Europe; external)", named: "European Landscape Convention (ELC)", citedIn: ["2.1", "2.2"], role: "definition of landscape; the duty to provide training" }
  - { document: "IFLA/UNESCO Charter for Landscape Architectural Education (not ingested)", named: "IFLA/UNESCO Charter for Landscape Architectural Education", citedIn: ["1.19"], role: "defines the profession" }
  - { document: "LI Competency Framework; Professional Code of Practice; Procedures and Guidelines for Higher Education Accreditation; Skills for Greener Places (not yet ingested)", named: "as named in the text", citedIn: ["1.11", "1.12", "1.15", "1.16", "1.17", "2.5", "2.6"], role: "the professional body's requirements and context" }
  - { document: "DEFRA Landscape Review Final Report, 2019 (external)", named: "the 2019 Landscape Review of DEFRA", citedIn: ["1.5"], role: "quoted on the changing countryside" }
  - { document: "Advance HE inclusive curricula guidance (not ingested)", named: "Advance HE", citedIn: ["1.23"], role: "definition of inclusive curricula and pedagogy" }
```

## Part B Terminology
<!-- The statement has no glossary of its own unless Part E says so; these are terms it defines in its text. -->

### B1 Concepts
<!-- label: both; status: drafted; basis: primary -->
```yaml
- { slug: "landscape", definition: "an area as people perceive it, whose character comes from natural and human factors acting and interacting, as the European Landscape Convention defines it (D1, 2.1)", beneficiaryDefinition: "a place as people see it, shaped by nature and by people together", scopeNote: "the statement takes the convention's definition", category: "unknown", practices: ["education", "landscape architecture"] }
- { slug: "green-infrastructure", definition: "the network of green spaces whose principles the profession leads, linking towns and cities with the surrounding landscape (D1, 1.7; 3.2)", beneficiaryDefinition: "the connected parks, green spaces and natural features in and around towns", scopeNote: "named, not defined, in the text", category: "unknown", practices: ["landscape architecture"] }
- { slug: "geomatic-information", definition: "the acquisition, modelling and analysis of data referenced to location (D1, 4.4)", beneficiaryDefinition: "data tied to places on the ground, and how it is gathered and analysed", scopeNote: "defined in passing in threshold item 4.4.b19", category: "unknown", practices: ["landscape architecture"] }
- { slug: "formative-assessment", definition: "assessment for development, giving feedback to help learning; it does not count to final marks (D1, 3.10)", beneficiaryDefinition: "practice tasks that give you feedback but do not count to your marks", scopeNote: "set against summative assessment", category: "unknown", practices: ["education"] }
- { slug: "summative-assessment", definition: "assessment showing how far a learner has met intended outcomes, with marks counting to the final mark (D1, 3.11)", beneficiaryDefinition: "assessment that counts towards your marks", scopeNote: "uses assessment criteria", category: "unknown", practices: ["education"] }
- { slug: "recognition-of-prior-learning", definition: "entry with credit for learning gained elsewhere, in or outside education (D1, 3.13)", beneficiaryDefinition: "getting credit for what you have already learned before you join", scopeNote: "also called accreditation of prior learning (APL)", category: "unknown", practices: ["education"] }
- { slug: "externality", definition: "an outside view in quality assurance, through external reviewers and examiners (D1, 2.26, 2.27)", beneficiaryDefinition: "people from outside your university checking its courses and marks", scopeNote: "", category: "unknown", practices: ["education"] }
- { slug: "pathway-to-chartership", definition: "the LI's formal professional qualification route for landscape architects, entered from an accredited master's (D1, 2.15)", beneficiaryDefinition: "the route to becoming a chartered landscape architect", scopeNote: "", category: "unknown", practices: ["landscape architecture"] }
```

### B2a Terms as the issuer defines them
<!-- label: source; status: drafted; basis: primary -->
```yaml
- { concept: "landscape", form: "Landscape", lang: "en", partOfSpeech: "noun", termStatus: "preferred", register: "formal" }
- { concept: "green-infrastructure", form: "green infrastructure", lang: "en", partOfSpeech: "noun-phrase", termStatus: "preferred", register: "formal" }
- { concept: "geomatic-information", form: "geomatic information", lang: "en", partOfSpeech: "noun-phrase", termStatus: "preferred", register: "formal" }
- { concept: "formative-assessment", form: "Formative assessment", lang: "en", partOfSpeech: "noun-phrase", termStatus: "preferred", register: "formal" }
- { concept: "summative-assessment", form: "Summative assessment", lang: "en", partOfSpeech: "noun-phrase", termStatus: "preferred", register: "formal" }
- { concept: "recognition-of-prior-learning", form: "recognition of prior learning (RPL)", lang: "en", partOfSpeech: "noun-phrase", termStatus: "preferred", register: "formal" }
- { concept: "recognition-of-prior-learning", form: "accreditation of prior learning (APL)", lang: "en", partOfSpeech: "noun-phrase", termStatus: "admitted", register: "formal" }
- { concept: "externality", form: "Externality", lang: "en", partOfSpeech: "noun", termStatus: "preferred", register: "formal" }
- { concept: "pathway-to-chartership", form: "Pathway to Chartership", lang: "en", partOfSpeech: "noun-phrase", termStatus: "preferred", register: "formal" }
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
  title: "Subject Benchmark Statement: Landscape Architecture"
  edition: "April 2024 (fifth edition)"
  year: 2024
  url: unknown (the QAA page; the text came by stan's extraction)
  retrieved: "held from stan: wkspc2615-QAAVector mapped/landscape-architecture-2024/landscape-architecture-2024.raw.txt, commit 366bcb99a01118f2c4c3ebfa2a8337596bddc455; received 2026-10-03"
  licence: QAA copyright
  tier: primary
  readVia: direct
  held: 8ed7fbd1077ea06319c974e4bc7cdd35cf4785844ded756978f26e1ecddb81c2
  heldFiles: ["wkspc2601-library/txt/qaa-2024-landscape-architecture-subject-benchmark-statement-standard.txt", "wkspc2601-library/txt/qaa-2024-landscape-architecture-subject-benchmark-statement-standard.norm.txt", "wkspc2601-library/records/qaa-2024-landscape-architecture-subject-benchmark-statement-standard.chunks.json", "wkspc2601-library/records/qaa-2024-landscape-architecture-subject-benchmark-statement-standard.held.json"]
  citedIn: [S1, S2, S3, S4, S4a, S5, S6, S7, SB1, SB2, SB3, SB4, SB5, SB6]
```

### D2 Research log
```yaml
- { ref: D1, tier: primary, consulted: 2026-10-03, pass: P1, outcome: "read whole, direct, from the normalised text; skeleton by tools/std_prep.py, document by tools/bm_build.py" }
- { ref: "ADAPT subj HESA stores, cah.json and hecos.json (designs/ingest/standards/subj/vocab)", tier: primary, consulted: 2026-10-03, pass: P1, outcome: "codes for statedSubjects and subjects" }
```

### D3 Wanted sources
```yaml
- { w: "W-std-0071", source: "Landscape Institute Competency Framework", why: "SB5 requirements; the four theme competencies (1.15) and accreditation mapping (2.5)", url: "www.landscapeinstitute.org/education/introducing-the-new-entry-standards-and-competency-framework/" }
- { w: "W-std-0072", source: "Landscape Institute (2022) Criteria for Accreditation of Higher Education Programmes; Procedures and guidelines for higher education accreditation", why: "SB5 requirements (2.4, 2.6)", url: "landscapeinstitute.org (links in section 5)" }
- { w: "W-std-0043", source: "IFLA/UNESCO Charter for Landscape Architectural Education; IFLA Global Ethical Principles", why: "SB5 requirements for IFLA (1.11, 1.19)", url: "www.iflaworld.com" }
```

## Part E Gaps and questions
- Subject codes inferred (SB-2): the text names no HECoS or CAH code; 100124 landscape architecture and design, CAH13-01-03 landscape design and 100588 landscape studies are inferred from the HESA stores, as are 100197 planning, 100347 ecology and 100864 in statedSubjects; for P3.
- Rungs: threshold (4.4, 56 items in seven headed groups), typical (4.5, 3 items) and excellent (4.6, 3 items) for honours, plus a master's threshold list (4.7, 8 items, award master's, fheq:7). The skeleton's count of 64 threshold items is 56 honours plus 8 master's.
- Pattern differing from Psychology: the threshold lead-in (4.4) has no modal ("demonstrate ... through which they can"); force recorded as threshold with forceFrom 4.1, which defines the threshold as the minimum for the award.
- Pattern differing from Psychology: typical (4.5) and excellent (4.6) lead-ins have no modal ("demonstrate they have"); 4.2 says the statement "describes" them, so force is describes, not will. For Abbott.
- Pattern differing from Psychology: typical and excellent items build on the whole threshold list ("listed above"), so no gradeOf to a single threshold item; excellent to typical links (4.6.b1 to b3 onto 4.5.b1 to b3) are inferred from their parallel wording, not paired by the issuer.
- Pattern: the master's list is its own numbered paragraph (4.7), so its ids are 4.7.b1 to b8, not the .masters suffix the batch 1 convention gives to master's columns in a table; rung threshold, award master's, force will from its lead-in.
- Pattern: the threshold list is split by seven sub-headings that the held text runs onto the end of the item before; the skeleton spans for 4.4.b18, b25, b39, b43, b49 and b56, 4.5.b3, 4.6.b3, 1.25.b2 and 1.26.b7 carried the next heading, and the paragraph spans of 2.12, 2.21 and 4.3 a page number or the next heading; all were re-cut with find; 4.4.b17 was re-cut the same way for safety. Domains within the groups are our assignment (intellectual mostly subject-skill; self-management, communication and teamwork generic-skill), for P3.
- Typo in the held text: 4.2 reads "typical end excellent standards" (for "and"); kept in source.
- Statements cut outside the rungs: 1.25.b1 and b2 (should, provider), 1.26.b1 to b7 (will, course content giving students chances to show understanding), 2.5 (required, read as must), 2.11 (expected, would: describes), 2.12 (will), 2.15 (requires, read as must, a professional body rule), 2.21 (should), 2.26 and 3.3 (will, provider), 3.9 (will), 4.3 (should). Doubtful cuts for P3: 2.26 and 3.3 read like plain provider norms with will; 1.26 is a will on course content rather than an outcome list.
- Obliging words outside the five (for Abbott): "expected to" (1.11, 1.17: LI members; 2.11: progression, recorded as describes); "required"/"requires" (1.15, 2.5, 2.15, 2.28); "It is important that" (1.23); "advised" (2.8, 2.21); "encouraged" (2.24, 2.28); "obliged" (2.2, the UK government under the ELC).
- Not statements, by rule: 1.15 bullets and 1.11/1.17 are the LI's requirements on its members, not on students or courses (recorded in SB5); 2.4 lists the LI's accreditation criteria; 2.28 the review group's duties; 2.2 the government's duty under the ELC.
- Plain-present or hedged provider norms, not statements (template open point 5): 2.10 (course design might), 2.25, 2.27 (external examiners typically), 3.2 (courses are likely to address), 3.5 (will often), 3.7 (most courses will offer), 3.8 (assessment aligns), 3.12 (likely to experience), 3.13 (will usually offer RPL), 1.22 (can), 1.27 (might); 4.1 and 4.2 define the rungs and are recorded as lead-ins, not statements.
- Level mismatch in the held text: 2.17 gives a four-year integrated undergraduate degree as Levels 3 to 6 (FQHEIS 7 to 10), while 2.19 gives the integrated master's as Levels 4 to 7 (FQHEIS 8 to 11). FHEQ defines no Level 3; cqfw:3 would be the nearest shared id. Not recorded as a crosswalk; S5 records only the stated 6 to 10 and 7 to 11 equivalences.
- Apprenticeship levels in 2.23 and 2.24 (Level 3 Landscape Technician, Level 6 award, Level 7 Chartered Landscape Professional) name no framework (likely RQF or the apprenticeship levels); not mapped to level ids.
- Theme words outside the themes (SB-10): "sustainable" (1.3), "accessible green spaces" (1.5) and "ecological sustainability" (1.19) describe the discipline, not the theme; recorded in SB1, not SB6. Front matter names the four themes (excluded matter).
- Generative AI recorded as theme:generative-ai (3.14 and in 4.4.b43, b49), per the batch 1 convention.
- Frameworks: FHEQ and FQHEIS cited (FQHEIS by name, filed under scqf); CQFW and SCQF by name not cited. Annex D cited in 4.3 and listed in section 5 as QAA (2019); now in the 2024 Frameworks (std:doc:qaa-fheq-2024-framework).
- Generic-skill levels (SB-4): every generic-skill item takes fheq:6 (honours) or fheq:7 (master's), both in S5; the descriptor each refines is named in its author-agent-written instruction (qaa/fheq-2024/4.15.* or 4.17.*), with spine:6 or spine:7 from the reference framework; the Annex D third-class cell named for each threshold item is our reading, for P3.
- Supersedes: the 2019 fourth edition is named only in the advisory group list (section 6); the front matter lists key changes without its date.
- Bodies requirements not yet ingested (SB-9): LI competency framework, code of practice and accreditation criteria; IFLA charter and ethical principles; RTPI and RIBA accreditation (D3).
- Verbs: noun-phrase items (4.5.b2, 4.6.b2, 4.7.b1 to b4, b6, b8 and several 1.26 items) carry no verb of their own; verbs recorded as empty rather than borrowed from the lead-in.
- S9 commentary not researched in P1.
- ST-12: versions here run to the lengths the content needs; no length range is yet set.

---

## Change notes
- 0.1.2, 3 October 2026, 21:02: moved with its held text from UNI to the source library repo (`wkspc2601-library/ingested/standards/`, texts in `txt/`, records in `records/`); paths only (Abbott, 20:56; std N-0119).
- 0.1.1, 3 October 2026, 20:20: obliging words outside the five read as must, "ought to" as should, on statements outside the rungs, each marked on its force line (Abbott, 20:17; D-std-0016).
- 0.1.0, 2026-10-03 17:44: researched by run frame 0.1.1-draft and standards run layer 0.7.0-draft, std, run 0114 (P1); built by tools/bm_build.py.
