---
id: std:doc:qaa-architectural-technology-2022-benchmarks
title: "Subject Benchmark Statement Architectural Technology"
profile: standards/subject-benchmark
profileVersion: 0.2.0-draft
issuer: QAA
kind: subject-benchmark
jurisdiction: [UK]
subjectScope: subjects
subjects:
  - { scheme: "hecos", code: "100121", label: "architectural technology", basis: "stated" }
  - { scheme: "cah", code: "CAH13-01-01", label: "architecture", basis: "stated" }
  - { scheme: "cah", code: "CAH13-01", label: "architecture, building and planning", basis: "stated" }
  - { scheme: "cah", code: "CAH13", label: "architecture, building and planning", basis: "stated" }
edition: "March 2022 (fifth edition)"
published: 2022-03
status: current
supersedes: "the fourth edition, 2019 (D1, back matter); not held"
heldText: { method: sha256-bytes, raw: 00009ae5d76a069d056e2af0a027e326c739e398df4037a948cbb542f96884ab, normalised: a91856ac1413ff27c5d2e63120ea9284281edee11c13fb5a9b33592ee27f9d04 }
heldTextStan: { method: sha256-stan, raw: 00009ae5d76a069d056e2af0a027e326c739e398df4037a948cbb542f96884ab, normalised: 4986de09e0fafeb6221e2676c7375bf778e477b612026cf5ae831183fe3f4a3f }
licence: "QAA copyright; held for study, private to the project, never published"
series: "QAA Subject Benchmark Statements, 2022 revision with cross-cutting themes (this subject's fifth edition)"
awardsCovered: ["bachelor's with honours", "master's"]
levelsCovered: ["fheq:6", "fheq:7", "fqheis:10", "fqheis:11"]
nations: ["England", "Wales", "Scotland", "Northern Ireland"]
parts:
  S: full
  B: "partial: no glossary in the document (it points to QAA's Glossary); terms it defines in passing"
  C: "not-applicable: the document sets expectations, not a procedure"
pins: { structure: 0.13.0-draft, template: 0.8.0-draft, benchmarkTemplate: 0.6.0-draft, runFrame: 0.1.1-draft, runLayer: 0.7.0-draft, standards: none yet, terminology: none yet }
lifecycle: drafted
researchedBy: run frame 0.1.1-draft; standards run layer 0.7.0-draft; std, run 0086 (tools/bm_build.py)
passes:
  P1: "2026-10-03 16:15"
  P2: "skipped: read direct from the held text; inferred codes and rung links are for P3"
  P3: open
version: 0.1.2
---

<!-- from INGEST wpk-0016-ingest-pd-template-standards.md 0.8.0-draft and wpk-0016-ingest-pd-template-standards-benchmark.md 0.6.0-draft; built by tools/bm_build.py from run-src/ -->
# Subject Benchmark Statement: Architectural Technology (QAA, March 2022)

> Run 0086, P1 by std. The issuer's words are held in the source library, `wkspc2601-library/txt/qaa-2022-architectural-technology-subject-benchmark-statement-standard.norm.txt`; each S4 record carries its statement in full (`source`) for language analysis, with its span. Paraphrases and versions are ours. Private to the project, never published. In front matter `status` is the issuer's; ours is `lifecycle`. Doubts are in Part E.

## Part 0 Summary

### 0.1 Agent definition
<!-- label: editorial; status: drafted; basis: primary -->
QAA's UK reference point for what a graduate in Architectural Technology should know and be able to do at the end of an honours degree or a master's degree. It states one rung only, the threshold, for each award (honours in 4.6, master's in 4.7), with a list of generic skills for honours graduates (4.8) and lists of course aims (3.6) and master's abilities (3.7). Reach for it when designing, reviewing or describing a course in the subject or its outcomes. It is not a curriculum and not a regulatory requirement in England, though the lead professional body bases its accreditation on it.

### 0.2 Summary
<!-- label: both; status: drafted; basis: primary -->
Published by QAA in March 2022 for the sector, the statement describes architectural technology as a design discipline rooted in science and engineering that links design and construction, and sets out its context, purposes, distinctive features, content, teaching, learning and assessment. Its benchmark standards are threshold only: one list for bachelor's degrees with honours (FHEQ Level 6, FQHEIS Level 10) and an added list for master's degrees, with honours generic skills beside them; performance above threshold is left to the degree classification descriptions (Annex D). It carries the four cross-cutting themes (equality, diversity and inclusion, framed by its own EDI Vision Statement; accessibility; sustainability; enterprise and entrepreneurship with employability) and names the Chartered Institute of Architectural Technologists (CIAT) as the lead PSRB, whose accreditation and Chartered Membership standards rest on it.

## Part S Standard

### S1 Identity
<!-- label: source; status: drafted; basis: primary -->
```yaml
issuer: The Quality Assurance Agency for Higher Education
title: "Subject Benchmark Statement Architectural Technology"
edition: "March 2022 (fifth edition)"
dates:
  published: 2022-03
  other: []
kind: subject-benchmark
jurisdiction: [UK]
authority: "reference: a sector reference point; in England not a sector-recognised standard under the OfS framework; a key reference point in Wales and Scotland; part of quality requirements in Northern Ireland; the basis of CIAT's accreditation and of its standards of education for Chartered Membership (D1, front matter: Relationship to legislation)"
licence: "QAA copyright; the document gives no re-use terms in its text (D1, front matter)"
copyrightNotice: { text: "© The Quality Assurance Agency for Higher Education 2022", locator: "D1, index" }
```

### S2 Purpose and scope
<!-- label: source; status: drafted; basis: primary -->
```yaml
governs: "what an Architectural Technology graduate can be expected to know, do and understand at the end of an honours or a master's degree, and the nature and characteristics of awards in the subject (D1, front matter: About this Statement; 4.1)"
appliesTo:
  awards: ["bachelor's degrees with honours", "master's degrees, generalist and specialist, conversion or specialising (2.7; 4.5)", "graduate and degree apprenticeships (4.1)"]
  levels: ["fheq:6", "fheq:7", "fqheis:10", "fqheis:11"]
  providers: ["UK higher education providers"]
whoMustUse: "none-stated; it is a reference point, not a requirement (D1, front matter)"
howUsed: ["design", "approval", "review", "other: external examining; PSRB accreditation (CIAT); information for prospective students and employers"]
doesNot: "it is not a national curriculum and does not prescribe teaching, learning or assessment; it carries no statutory or regulatory requirement (D1, front matter)"
beneficiary: the student
statedScope: "\"The ever-increasing professional diversity within architectural technology is recognised in this Statement alongside the need and demand to develop the subject at honours and master's degree level.\" (D1, front matter: About this Statement)"
statedSubjects:
  - { name: "Architectural Technology", locator: "(D1, title; 1.1)", kind: "subject", codes: [{ scheme: "hecos", code: "100121", label: "architectural technology" }, { scheme: "cah", code: "CAH13-01-01", label: "architecture" }] }
  - { name: "honours and master's degree level qualifications in Architectural Technology or related subjects", locator: "(D1, front matter: Relationship to legislation)", kind: "programme title", codes: [{ scheme: "hecos", code: "100121", label: "architectural technology" }] }
  - { name: "graduate and degree apprenticeship programmes", locator: "(D1, 4.1; 1.39)", kind: "programme title", codes: [{ scheme: "hecos", code: "100121", label: "architectural technology" }] }
  - { name: "Sustainable Design", locator: "(D1, 2.16)", kind: "specialism", codes: [] }
  - { name: "Fire Safety", locator: "(D1, 2.16)", kind: "specialism", codes: [] }
  - { name: "Architectural Engineering", locator: "(D1, 2.16)", kind: "specialism", codes: [{ scheme: "hecos", code: "100120", label: "architectural engineering" }] }
  - { name: "Building Performance", locator: "(D1, 2.16)", kind: "specialism", codes: [] }
  - { name: "Design Management", locator: "(D1, 2.16)", kind: "specialism", codes: [] }
  - { name: "Project Management", locator: "(D1, 2.16)", kind: "specialism", codes: [{ scheme: "hecos", code: "100812", label: "project management" }] }
  - { name: "Retrofit Design", locator: "(D1, 2.16)", kind: "specialism", codes: [] }
  - { name: "Conservation", locator: "(D1, 2.16)", kind: "specialism", codes: [] }
subjects: see front matter (subjectScope subjects)
```

### S3 Structure
<!-- label: both; status: drafted; basis: primary -->
```yaml
components:
  - { number: "1.1", order: 3, componentType: paragraph, parent: "section 1", heading: "Context", gloss: "the discipline defined: how buildings are put together and perform, grounded in science and engineering; growing weight on retrofit and energy" }
  - { number: "1.2", order: 4, componentType: paragraph, parent: "section 1", heading: "Context", gloss: "building and life safety after major failures; new law and standards reach education and practice" }
  - { number: "1.3", order: 5, componentType: paragraph, parent: "section 1", heading: "Context", gloss: "the climate emergency will change how professionals in the field think and work" }
  - { number: "1.4", order: 6, componentType: paragraph, parent: "section 1", heading: "Context", gloss: "a changing built environment calls for more diverse and specialised education" }
  - { number: "1.5", order: 7, componentType: paragraph, parent: "section 1", heading: "Context", gloss: "effects on design, construction and use: retrofit, carbon, safety, advanced and offsite methods" }
  - { number: "1.6", order: 8, componentType: paragraph, parent: "section 1", heading: "Context", gloss: "decisions driven by data across the building process, reducing risk and overruns" }
  - { number: "1.7", order: 9, componentType: paragraph, parent: "section 1", heading: "Context", gloss: "reliable, usable data and information management support design; the move to digital working" }
  - { number: "1.8", order: 10, componentType: paragraph, parent: "section 1", heading: "Context", gloss: "the role widens to embed new technology and help prevent safety, cost and performance failures" }
  - { number: "1.9", order: 11, componentType: paragraph, parent: "section 1", heading: "Context", gloss: "this changing focus frames the next standards of education and leaves institutions room to design" }
  - { number: "1.10", order: 12, componentType: paragraph, parent: "section 1", heading: "Context", gloss: "the specifications are a broad framework for responsive, challenging courses" }
  - { number: "1.11", order: 13, componentType: paragraph, parent: "section 1", heading: "Purposes of an Architectural Technology degree", gloss: "purpose: an independent design discipline linking design and construction within the built environment" }
  - { number: "1.12", order: 14, componentType: paragraph, parent: "section 1", heading: "Purposes of an Architectural Technology degree", gloss: "the field in project and design management across the life cycle, and in the digital age" }
  - { number: "1.13", order: 15, componentType: paragraph, parent: "section 1", heading: "Purposes of an Architectural Technology degree", gloss: "leading roles as designers, lead or principal designers; degrees build critical understanding of design, technology, leadership and practice" }
  - { number: "1.14", order: 16, componentType: paragraph, parent: "section 1", heading: "Purposes of an Architectural Technology degree", gloss: "diverse careers; the standards as a broad framework for agility and employability; inclusive design and wellbeing" }
  - { number: "1.15", order: 17, componentType: paragraph, parent: "section 1", heading: "Characteristics of an Architectural Technology degree", gloss: "characteristics: a real-world, vocational curriculum preparing professionals for building design and delivery" }
  - { number: "1.16", order: 18, componentType: paragraph, parent: "section 1", heading: "Characteristics of an Architectural Technology degree", gloss: "numeracy, literacy, industry awareness and technical competence underpin study; subject and wider skills" }
  - { number: "1.17", order: 19, componentType: paragraph, parent: "section 1", heading: "Characteristics of an Architectural Technology degree", gloss: "a distinct subject with four educational components (theoretical, experiential, professional, ethical)" }
  - { number: "1.18", order: 20, componentType: paragraph, parent: "section 1", heading: "Characteristics of an Architectural Technology degree", gloss: "a pointer to the front matter on PSRB accreditation" }
  - { number: "1.19", order: 21, componentType: paragraph, parent: "section 1", heading: "Equality, diversity and inclusion (EDI)", gloss: "a record of widening participation; a duty on providers to make curricula inclusive" }
  - { number: "1.20", order: 22, componentType: paragraph, parent: "section 1", heading: "Equality, diversity and inclusion (EDI)", gloss: "CIAT uses inclusivity in accreditation; the subject's EDI vision, set within the Equality Act 2010, runs across the statement" }
  - { number: "1.21", order: 23, componentType: paragraph, parent: "section 1", heading: "Architectural Technology EDI Vision Statement", gloss: "the vision: wider participation and a commitment to equality, diversity and inclusion" }
  - { number: "1.22", order: 24, componentType: paragraph, parent: "section 1", heading: "Architectural Technology EDI Vision Statement", gloss: "the whole life cycle of a project includes the changing lives of its end-users" }
  - { number: "1.23", order: 25, componentType: paragraph, parent: "section 1", heading: "Architectural Technology EDI Vision Statement", gloss: "inclusive design as a requirement; EDI to be embedded like health and safety (S4)" }
  - { number: "1.24", order: 26, componentType: paragraph, parent: "section 1", heading: "Architectural Technology EDI Vision Statement", gloss: "honesty, integrity and respect for a diverse population at the core of practice" }
  - { number: "1.25", order: 27, componentType: paragraph, parent: "section 1", heading: "Architectural Technology EDI Vision Statement", gloss: "the profession's widening participation record should inform how it is promoted" }
  - { number: "1.26", order: 28, componentType: paragraph, parent: "section 1", heading: "Architectural Technology EDI Vision Statement", gloss: "inquisitive professionals who weigh the effect of decisions on users' comfort, safety and wellbeing" }
  - { number: "1.27", order: 29, componentType: paragraph, parent: "section 1", heading: "Sustainability", gloss: "core skills match the ESD guidance's outcomes (Advance HE and QAA, 2021)" }
  - { number: "1.28", order: 30, componentType: paragraph, parent: "section 1", heading: "Sustainability", gloss: "the discipline's key part in sustainability; the three pillars early in a career" }
  - { number: "1.29", order: 31, componentType: paragraph, parent: "section 1", heading: "Sustainability", gloss: "UNESCO's eight sustainability competencies to be aligned with outcomes (S4)" }
  - { number: "1.30", order: 32, componentType: paragraph, parent: "section 1", heading: "Sustainability", gloss: "the vision of integrated sustainability; real-life case studies and reflection (S4)" }
  - { number: "1.31", order: 33, componentType: paragraph, parent: "section 1", heading: "Sustainability", gloss: "an ESD framework may renew pedagogy and raise real-world application" }
  - { number: "1.32", order: 34, componentType: paragraph, parent: "section 1", heading: "Sustainability", gloss: "problem-based learning; balance soft and hard skills; software not at the expense of sustainability" }
  - { number: "1.33", order: 35, componentType: paragraph, parent: "section 1", heading: "Sustainability", gloss: "collaborative and enquiry-based learning; working with industry stakeholders (S4)" }
  - { number: "1.34", order: 36, componentType: paragraph, parent: "section 1", heading: "Sustainability", gloss: "interdisciplinary and independent learning; theory with practical projects; partnerships with industry (S4)" }
  - { number: "1.35", order: 37, componentType: paragraph, parent: "section 1", heading: "Entrepreneurship, enterprise and employment", gloss: "enterprise and entrepreneurship education as QAA (2018) defines them" }
  - { number: "1.36", order: 38, componentType: paragraph, parent: "section 1", heading: "Entrepreneurship, enterprise and employment", gloss: "enterprise education adds value to careers and to society" }
  - { number: "1.37", order: 39, componentType: paragraph, parent: "section 1", heading: "Entrepreneurship, enterprise and employment", gloss: "the subject is well placed for enterprise through live projects and visiting expertise" }
  - { number: "1.38", order: 40, componentType: paragraph, parent: "section 1", heading: "Entrepreneurship, enterprise and employment", gloss: "the degree prepares for work and inspires creative, critical thinking; teams encouraged to build this in" }
  - { number: "1.39", order: 41, componentType: paragraph, parent: "section 1", heading: "Entrepreneurship, enterprise and employment", gloss: "employer engagement, required in CIAT accreditation; apprenticeships; the aspirATion network" }
  - { number: "1.40", order: 42, componentType: paragraph, parent: "section 1", heading: "Entrepreneurship, enterprise and employment", gloss: "involving employers of different sizes and sectors; corporate social responsibility (S4)" }
  - { number: "2.1", order: 44, componentType: paragraph, parent: "section 2", heading: "Design of courses", gloss: "the statement as dialogue for course design; adaptability and specialisms for a fast-changing industry (S4)" }
  - { number: "2.2", order: 45, componentType: paragraph, parent: "section 2", heading: "Design of courses", gloss: "master's degrees: deeper, professional or interdisciplinary variants" }
  - { number: "2.3", order: 46, componentType: paragraph, parent: "section 2", heading: "Design of courses", gloss: "restates the subject and its four educational components (see 1.17)" }
  - { number: "2.4", order: 47, componentType: paragraph, parent: "section 2", heading: "Design of courses", gloss: "inclusive design and awareness of health, safety, welfare and ethics" }
  - { number: "2.5", order: 48, componentType: paragraph, parent: "section 2", heading: "Design of courses", gloss: "national and international context; an international dimension in courses; CIAT accredits overseas (S4)" }
  - { number: "2.6", order: 49, componentType: paragraph, parent: "section 2", heading: "Design of courses", gloss: "technology's growing effect calls for modelling and coordination across the whole building process" }
  - { number: "2.7", order: 50, componentType: paragraph, parent: "section 2", heading: "Design of courses", gloss: "generalist (broader) and specialist (deeper) master's degrees" }
  - { number: "2.8", order: 51, componentType: paragraph, parent: "section 2", heading: "Accessibility", gloss: "an obligation on all providers to make study accessible, onsite and online" }
  - { number: "2.9", order: 52, componentType: stem, parent: "section 2", heading: "Accessibility", gloss: "support expected of institutions: screening, specialist support, mentors, adjustments, claims, accessible curricula" }
  - { number: "2.10", order: 53, componentType: paragraph, parent: "section 2", heading: "Accessibility", gloss: "those services as the basic minimum (S4)" }
  - { number: "2.11", order: 54, componentType: paragraph, parent: "section 2", heading: "Accessibility", gloss: "design-led modules bring varied learning and assessment types and outputs" }
  - { number: "2.12", order: 55, componentType: paragraph, parent: "section 2", heading: "Accessibility", gloss: "adjustments for presentation-based design assessment (S4)" }
  - { number: "2.13", order: 56, componentType: paragraph, parent: "section 2", heading: "Accessibility", gloss: "clear assessment expectations; a digital route for students who cannot afford physical models" }
  - { number: "2.14", order: 57, componentType: paragraph, parent: "section 2", heading: "Accessibility", gloss: "remote and blended learning widen access; attention to digital poverty (S4)" }
  - { number: "2.15", order: 58, componentType: paragraph, parent: "section 2", heading: "Progression", gloss: "progression through honours (FHEQ 6, FQHEIS 10) towards all the threshold skills" }
  - { number: "2.16", order: 59, componentType: paragraph, parent: "section 2", heading: "Progression", gloss: "master's specialisms named, such as fire safety and retrofit design" }
  - { number: "2.17", order: 60, componentType: paragraph, parent: "section 2", heading: "Progression", gloss: "exit awards; four-year Scottish honours; a second-class degree fits a student for postgraduate study" }
  - { number: "2.18", order: 61, componentType: practice, parent: "section 2", heading: "Flexibility", gloss: "modes of delivery and a range of teaching methods" }
  - { number: "2.19", order: 62, componentType: paragraph, parent: "section 2", heading: "Flexibility", gloss: "industry input; a design project or dissertation expected of students (S4)" }
  - { number: "2.20", order: 63, componentType: paragraph, parent: "section 2", heading: "Partnership", gloss: "partnership with employers and the organisations around them" }
  - { number: "2.21", order: 64, componentType: paragraph, parent: "section 2", heading: "Partnership", gloss: "ways employers take part, and the burden on small firms" }
  - { number: "2.22", order: 65, componentType: paragraph, parent: "section 2", heading: "Monitoring and review", gloss: "monitoring and periodic review, with this statement as an external reference point" }
  - { number: "2.23", order: 66, componentType: paragraph, parent: "section 2", heading: "Monitoring and review", gloss: "external reviewers in periodic review" }
  - { number: "2.24", order: 67, componentType: paragraph, parent: "section 2", heading: "Monitoring and review", gloss: "external examiners and how the statement supports them" }
  - { number: "2.25", order: 68, componentType: paragraph, parent: "section 2", heading: "Monitoring and review", gloss: "accreditation by CIAT through visits and desk reviews" }
  - { number: "3.1", order: 70, componentType: area, parent: "section 3", heading: "Content", gloss: "content: a creative design discipline of building systems, materials and BIM across the life cycle" }
  - { number: "3.2", order: 71, componentType: area, parent: "section 3", heading: "Content", gloss: "efficient, low-carbon, safe buildings and the social and ethical demands on the profession" }
  - { number: "3.3", order: 72, componentType: area, parent: "section 3", heading: "Content", gloss: "inclusive design and the needs of all stakeholders (repeats 2.4)" }
  - { number: "3.4", order: 73, componentType: area, parent: "section 3", heading: "Content", gloss: "researching needs and requirements, including social needs and life safety" }
  - { number: "3.5", order: 74, componentType: area, parent: "section 3", heading: "Content", gloss: "modelling, procurement and services make design and construction complex; degrees develop understanding in context (S4)" }
  - { number: "3.6", order: 75, componentType: stem, parent: "section 3", heading: "Structure and aims of Architectural Technology honours degrees", gloss: "course aims for honours degrees: fourteen things students learn how to do (S4 items)" }
  - { number: "3.7", order: 76, componentType: stem, parent: "section 3", heading: "Structure and aims of Architectural Technology master's degrees", gloss: "master's entry assumes broad understanding; eight added subject-specific abilities (S4 items)" }
  - { number: "3.8", order: 77, componentType: practice, parent: "section 3", heading: "Teaching and learning", gloss: "teaching that joins theory, practice and employability; case studies, live sites, simulations" }
  - { number: "3.9", order: 78, componentType: practice, parent: "section 3", heading: "Teaching and learning", gloss: "studio-based, problem-based learning with input from industry" }
  - { number: "3.10", order: 79, componentType: practice, parent: "section 3", heading: "Teaching and learning", gloss: "knowledge of context, core concepts and theories, plus subject and wider skills" }
  - { number: "3.11", order: 80, componentType: practice, parent: "section 3", heading: "Teaching and learning", gloss: "simulation, interdisciplinary work and practical sessions; problem-based studio learning" }
  - { number: "3.12", order: 81, componentType: practice, parent: "section 3", heading: "Teaching and learning", gloss: "active and reflective learning; a final collaborative interdisciplinary project" }
  - { number: "3.13", order: 82, componentType: practice, parent: "section 3", heading: "Teaching and learning", gloss: "master's level: debate on current and emerging topics" }
  - { number: "3.14", order: 83, componentType: practice, parent: "section 3", heading: "Teaching and learning", gloss: "master's level: critical understanding, creative response, learner-centred study" }
  - { number: "3.15", order: 84, componentType: paragraph, parent: "section 3", heading: "Teaching and learning", gloss: "master's courses widen and refine knowledge; professional, ethical and practical issues (S4)" }
  - { number: "3.16", order: 85, componentType: practice, parent: "section 3", heading: "Teaching and learning", gloss: "master's level: advanced research, analytical and practical techniques" }
  - { number: "3.17", order: 86, componentType: paragraph, parent: "section 3", heading: "Teaching and learning", gloss: "master's research: an advanced project and communicating it professionally (S4)" }
  - { number: "3.18", order: 87, componentType: practice, parent: "section 3", heading: "Assessment", gloss: "a wide range of assessment methods suited to a vocational subject" }
  - { number: "3.19", order: 88, componentType: practice, parent: "section 3", heading: "Assessment", gloss: "an explicit assessment strategy tied to learning outcomes (S4)" }
  - { number: "3.20", order: 89, componentType: practice, parent: "section 3", heading: "Assessment", gloss: "accessible assessment, adjustments and fairness; coverage, coursework and feedback (S4)" }
  - { number: "3.21", order: 90, componentType: stem, parent: "section 3", heading: "Assessment", gloss: "a range of methods matched to outcomes, with an indicative list of ten (S4 for the lead sentence)" }
  - { number: "3.22", order: 91, componentType: practice, parent: "section 3", heading: "Assessment", gloss: "master's level: the major project as the decisive assessment" }
  - { number: "4.1", order: 93, componentType: paragraph, parent: "section 4", heading: "Introduction", gloss: "the standards as threshold, the baseline for all honours and master's graduates, apprenticeships included" }
  - { number: "4.2", order: 94, componentType: paragraph, parent: "section 4", heading: "Introduction", gloss: "most students exceed threshold; providers refer to Annex D for the classifications (S4)" }
  - { number: "4.3", order: 95, componentType: paragraph, parent: "section 4", heading: "Introduction", gloss: "the standards can be met in several ways and do not map onto single modules" }
  - { number: "4.4", order: 96, componentType: paragraph, parent: "section 4", heading: "Introduction", gloss: "courses enable fluency in design, technology, management and practice (S4)" }
  - { number: "4.5", order: 97, componentType: paragraph, parent: "section 4", heading: "Introduction", gloss: "master's degrees, conversion or specialising, share one set of standards" }
  - { number: "4.6", order: 98, componentType: stem, parent: "section 4", heading: "Benchmark standards for honours degrees (threshold)", gloss: "honours threshold: ten areas of knowledge and ability (S4 items)" }
  - { number: "4.7", order: 99, componentType: stem, parent: "section 4", heading: "Benchmark standards for master's degrees (threshold)", gloss: "master's threshold: five added items (S4 items)" }
  - { number: "4.8", order: 100, componentType: stem, parent: "section 4", heading: "Generic skills for Architectural Technology graduates", gloss: "generic skills of honours graduates: seventeen items (S4 items)" }
  - { number: "1", componentType: section, parent: none, heading: "Context and purposes of an Architectural Technology degree", gloss: "section 1" }
  - { number: "2", componentType: section, parent: none, heading: "Distinctive features of an Architectural Technology degree", gloss: "section 2" }
  - { number: "3", componentType: section, parent: none, heading: "Content, structure and delivery", gloss: "section 3" }
  - { number: "4", componentType: section, parent: none, heading: "Benchmark standards", gloss: "section 4" }
excluded:
  - { number: "none", heading: "About this Statement; How can I use this document?; Relationship to legislation; Additional sector reference points; Architectural technology course accreditation; Chartered Architectural Technologist: protected title; CIAT's Chartered Standards", kind: "other: front matter, read for S1, S2, S7, SB5 and SB6" }
  - { number: "section headings", heading: "headings of sections 1 to 4", kind: "other: heading lines" }
  - { number: "5", heading: "List of references and further resources", kind: "other: back matter, read for S7 and SB6" }
  - { number: "6", heading: "Membership of the Advisory Group for the Subject Benchmark Statement for Architectural Technology", kind: "other: back matter, read for S1 (editions) and S8" }
```

### S4 Statements
<!-- label: both; status: drafted; basis: primary. Only standards (D-std-0002 (a)): 75 records. `source` is the issuer's statement exactly as its span holds it (D-std-0014). -->
```yaml
- id: qaa/architectural-technology-2022/1.23
  locator: { number: "1.23", headingPath: ["Context and purposes of an Architectural Technology degree", "Architectural Technology EDI Vision Statement"] }
  span: { start: 26189, end: 26752 }
  source: "1.23 There already exists an expectation of inclusive design being embedded as a requirement of education and practice; understanding that poor structures make for poor experiences, and that these poor experiences make for a poorer society with potentially systemic and fatal consequences. Therefore, equality, diversity and inclusion should be as demonstrably embedded across education and practice as health and safety is and sustainability must be. Architectural technology professionals should be able to accessibly communicate the value of inclusive design.\n"
  stem: none
  statementType: requirement
  rung: none
  force: should
  level: none
  appliesTo: "education and practice in the subject"
  addressee: both
  verbs: ["embedded", "communicate"]
  about: "EDI embedded like health and safety; communicating the value of inclusive design"
  themes: [theme:edi]
  domain: subject-skill
  award: ["bachelor's with honours", "master's"]
  gradeOf: none
  paraphrase: "Equality, diversity and inclusion should be built into education and practice as visibly as health and safety, since poorly designed buildings harm people and society; professionals in the field should be able to explain the worth of inclusive design in an accessible way."
  quote: full   # the issuer's statement is in `source` (D-std-0014)
  audience: both
  subjects: inherited
- id: qaa/architectural-technology-2022/1.29
  locator: { number: "1.29", headingPath: ["Context and purposes of an Architectural Technology degree", "Sustainability"] }
  span: { start: 29129, end: 29599 }
  source: "1.29 The eight UNESCO key competencies for sustainability - systems thinking, anticipatory (futures thinking), critical thinking, strategic, collaboration, integrated problem-solving, self -awareness and normative competencies - should be aligned with appropriate learning outcomes within the curriculum. This will help transform how staff and students appreciate issues related to sustainable development and apply this to their ways of thinking, practising and being.\n"
  stem: none
  statementType: requirement
  rung: none
  force: should
  level: none
  appliesTo: "curricula in the subject"
  addressee: provider
  verbs: ["aligned"]
  about: "UNESCO sustainability competencies aligned with outcomes"
  themes: [theme:esd]
  domain: none
  award: ["bachelor's with honours", "master's"]
  gradeOf: none
  paraphrase: "The eight UNESCO competencies for sustainability should be matched to suitable learning outcomes in the curriculum, to change how staff and students think about and practise sustainable development."
  quote: full   # the issuer's statement is in `source` (D-std-0014)
  audience: practitioner
  subjects: inherited
- id: qaa/architectural-technology-2022/1.30
  locator: { number: "1.30", headingPath: ["Context and purposes of an Architectural Technology degree", "Sustainability"] }
  span: { start: 29599, end: 30084 }
  source: "1.30 The vision is that all Architectural Technology courses contain a fully balanced, integrated and interdisciplinary approach to sustainability themes. These will produce graduates who are aware of the sustainability goals that they can contribute towards, and achieve them in a confident, efficient manner. Learners should be engaged in real-life case studies to support and develop critical evaluation of available and innovative solutions, and reflection as learning approaches.\n"
  stem: none
  statementType: requirement
  rung: none
  force: should
  level: none
  appliesTo: "courses in the subject"
  addressee: provider
  verbs: ["engaged", "support", "develop"]
  about: "integrated sustainability and real-life case studies"
  themes: [theme:esd]
  domain: none
  award: ["bachelor's with honours", "master's"]
  gradeOf: none
  paraphrase: "Every course is meant to treat sustainability in a balanced, integrated and interdisciplinary way, so graduates know the goals they can serve; learners should work on real cases that build critical judgement of current and new solutions, and reflection."
  quote: full   # the issuer's statement is in `source` (D-std-0014)
  audience: practitioner
  subjects: inherited
- id: qaa/architectural-technology-2022/1.33
  locator: { number: "1.33", headingPath: ["Context and purposes of an Architectural Technology degree", "Sustainability"] }
  span: { start: 31141, end: 31843 }
  source: "1.33 Learners should also be encouraged to confidently disseminate their learning experience and knowledge in their profession through 'collaborative learning' with their peers, as well as outside the classroom - within their communities and social networks. They need to be introduced to new ways of working collaboratively with other stakeholders in the construction industry, including clients, contractors and suppliers. 'Enquiry-based learning' may also be considered as another approach where students investigate topics, relevant to architectural technology, within real-life scenarios in which they develop skills of experimental design, data collection, critical analysis and problem-solving.\n"
  stem: none
  statementType: requirement
  rung: none
  force: should
  level: none
  appliesTo: "teaching in the subject"
  addressee: provider
  verbs: ["encouraged", "disseminate", "introduced"]
  about: "collaborative and enquiry-based learning"
  themes: [theme:esd]
  domain: none
  award: ["bachelor's with honours", "master's"]
  gradeOf: none
  paraphrase: "Learners should be encouraged to share what they learn with peers and in their communities through collaborative learning, and be introduced to working with clients, contractors and suppliers; enquiry-based learning on real scenarios may also be used."
  quote: full   # the issuer's statement is in `source` (D-std-0014)
  audience: practitioner
  subjects: inherited
- id: qaa/architectural-technology-2022/1.34
  locator: { number: "1.34", headingPath: ["Context and purposes of an Architectural Technology degree", "Sustainability"] }
  span: { start: 31843, end: 32807 }
  source: "1.34 Architectural Technology courses need to involve both interdisciplinary work and independent learning aspects to develop well-rounded students. 'Problem-based learning' may be adopted to facilitate creative environments for interdisciplinary learning in which students work together to address complex, multifaceted problems. New curricula should ensure that theory is combined with practical projects to achieve environmentally sustainable design objectives and enhance student learning experience. Academic-industry partnerships should be fostered by Architectural Technology courses. These are hugely beneficial for the development of student confidence and allow the real-world application of the theory taught by higher education providers in a professional setting. In addition, these will develop student employability skills and readiness for industry which will ensure sustainably aware graduates are employed where they can make a real-world impact."
  stem: none
  statementType: requirement
  rung: none
  force: should
  level: none
  appliesTo: "curricula and courses in the subject"
  addressee: provider
  verbs: ["ensure", "combined", "fostered"]
  about: "theory with practical projects; partnerships with industry"
  themes: [theme:esd]
  domain: none
  award: ["bachelor's with honours", "master's"]
  gradeOf: none
  paraphrase: "Courses need both interdisciplinary and independent learning; new curricula should join theory to practical projects with sustainable design aims, and courses should build partnerships with industry, which grow confidence and employability."
  quote: full   # the issuer's statement is in `source` (D-std-0014)
  audience: practitioner
  subjects: inherited
- id: qaa/architectural-technology-2022/1.40
  locator: { number: "1.40", headingPath: ["Context and purposes of an Architectural Technology degree", "Entrepreneurship, enterprise and employment"] }
  span: { start: 36292, end: 37071 }
  source: "1.40 Higher education providers should consider the benefits of involving employers of different sizes and from different sectors through a variety of modes of engagement, including subgroups, that work on specific employer-related issues, which meet less frequently and use electronic communication. A key driver of employer involvement is corporate social responsibility (CSR). The CSR ethos of businesses is a key driver of employer involvement, with emphasis on widening participation, local employment for local people, and activity being driven by 'finding the right job for the right person'. There are\n\n10\n\nbenefits of employer involvement for both the course and employers. Learning from employer perspectives brings a kind of 'business realism' to the student learning."
  stem: none
  statementType: requirement
  rung: none
  force: should
  level: none
  appliesTo: "higher education providers"
  addressee: provider
  verbs: ["consider"]
  about: "involving varied employers"
  themes: [theme:enterprise]
  domain: none
  award: ["bachelor's with honours", "master's"]
  gradeOf: none
  paraphrase: "Providers should weigh the gains of involving employers of varied size and sector in several ways, including small groups on employer issues; corporate social responsibility drives much of that involvement, and employer views bring commercial realism to learning."
  quote: full   # the issuer's statement is in `source` (D-std-0014)
  audience: practitioner
  subjects: inherited
- id: qaa/architectural-technology-2022/2.1
  locator: { number: "2.1", headingPath: ["Distinctive features of an Architectural Technology degree", "Design of courses"] }
  span: { start: 37156, end: 38044 }
  source: "2.1 The Subject Benchmark Statement represents general expectations about standards within Architectural Technology and it is intended, in dialogic mode, to encourage collaborative relationships in course design. This would include areas of interest to which the Subject Benchmark Statement applies and within the related built environment subject areas more generally. It is predicted that an architectural technology career pathway and job functions will be diverse and evolve within an industry that is likely to go through major changes. In recognition of the professional diversity and employability of those working within architectural technology, this should be reflected through encouraging adaptability, agility, diversity and specialisms in a f ast-changing industry and workplace with an attempt to future-proof knowledge and the development of new competencies and contexts.\n"
  stem: none
  statementType: requirement
  rung: none
  force: should
  level: none
  appliesTo: "course design in the subject"
  addressee: provider
  verbs: ["reflected", "encouraging"]
  about: "adaptability and specialisms in course design"
  themes: [none]
  domain: none
  award: ["bachelor's with honours", "master's"]
  gradeOf: none
  paraphrase: "The statement sets general expectations and invites collaborative course design; since careers will be diverse and the industry will change, course design should foster adaptability, agility, diversity and specialisms to keep knowledge current."
  quote: full   # the issuer's statement is in `source` (D-std-0014)
  audience: practitioner
  subjects: inherited
- id: qaa/architectural-technology-2022/2.5
  locator: { number: "2.5", headingPath: ["Distinctive features of an Architectural Technology degree", "Design of courses"] }
  span: { start: 40184, end: 41375 }
  source: "2.5 Architectural technology encompasses the impact of changing social, economic, legal, cultural, environmental, technological, business and political frameworks on the built and natural environment. It is anticipated that all Architectural Technology degrees will develop students' knowledge and critical understanding relating to design, technology and practice within a national and international context. This understanding supports the ability of practitioners to make an effective contribution within local, national, European and global contexts. Architectural technology professionals are engaged in projects globally and many spend time working both nationally and internationally. It is, therefore, important that an international dimension is included in Architectural Technology courses to ensure graduates are aware of the international context of their subject. The Chartered Institute of Architectural\n\n12\n\nTechnologists (CIAT) utilises this Subject Benchmark Statement in a global context to develop and accredit courses in countries outside of the UK jurisdiction, including in the EU, Australia, UAE, India, Hong Kong and China where it has been translated into Mandarin.\n"
  stem: none
  statementType: expectation
  rung: none
  force: will
  level: none
  appliesTo: "students of the subject"
  addressee: learner
  verbs: ["develop", "included"]
  about: "design, technology and practice in national and international context"
  themes: [none]
  domain: understanding
  award: ["bachelor's with honours", "master's"]
  gradeOf: none
  paraphrase: "All degrees in the subject are expected to develop students' knowledge and critical understanding of design, technology and practice in national and international settings, and courses need an international dimension so graduates know the global context of their field."
  quote: full   # the issuer's statement is in `source` (D-std-0014)
  audience: both
  subjects: inherited
- id: qaa/architectural-technology-2022/2.10
  locator: { number: "2.10", headingPath: ["Distinctive features of an Architectural Technology degree", "Accessibility"] }
  span: { start: 43120, end: 43211 }
  source: "2.10 While not an exhaustive list, these should be the basic services supporting students.\n"
  stem: none
  statementType: requirement
  rung: none
  force: should
  level: none
  appliesTo: "institutions offering the subject"
  addressee: provider
  verbs: ["supporting"]
  about: "basic support services for students"
  themes: [theme:accessibility]
  domain: none
  award: ["bachelor's with honours", "master's"]
  gradeOf: none
  paraphrase: "The support set out in 2.9 (screening, specialist help, mentors, reasonable adjustments, help with claims, accessible curricula) should be the minimum services for students, and the list is not complete."
  quote: full   # the issuer's statement is in `source` (D-std-0014)
  audience: practitioner
  subjects: inherited
- id: qaa/architectural-technology-2022/2.12
  locator: { number: "2.12", headingPath: ["Distinctive features of an Architectural Technology degree", "Accessibility"] }
  span: { start: 43571, end: 44340 }
  source: "2.12 Specific adjustments for the types of assessments associated with these courses should sit alongside the expectations for adjustments to exams and assessments detailed above at any education establishment. With regard to a design module, for example, to create a convincing studio or client engagement scenario, students are expected to verbally and visually present their design and technology solutions to the assessment tasks they are set. For students with learning differences or conditions such as anxiety, adjustments can be made to the nature of these presentations, and can, for instance, include a progression across an academic year from one-on-one sessions to a growing number of peers being present at each subsequent presentation to boost confidence."
  stem: none
  statementType: requirement
  rung: none
  force: should
  level: none
  appliesTo: "assessment in the subject"
  addressee: provider
  verbs: ["sit", "present", "made"]
  about: "adjustments for presentation-based design assessment"
  themes: [theme:accessibility]
  domain: none
  award: ["bachelor's with honours", "master's"]
  gradeOf: none
  paraphrase: "Adjustments suited to the subject's own assessments, such as presenting design work in person, should sit beside the usual exam adjustments; for students with learning differences or anxiety, presentations can build from one-to-one sessions to larger audiences over the year."
  quote: full   # the issuer's statement is in `source` (D-std-0014)
  audience: practitioner
  subjects: inherited
- id: qaa/architectural-technology-2022/2.14
  locator: { number: "2.14", headingPath: ["Distinctive features of an Architectural Technology degree", "Accessibility"] }
  span: { start: 45541, end: 45827 }
  source: "Such considerations should always be mindful of the circumstances of individual students, with progressive higher education providers making use of funding support for those experiencing forms of digital poverty, including access to suitable equipment, and data and bandwidth provision."
  stem: none
  statementType: requirement
  rung: none
  force: should
  level: none
  appliesTo: "institutions offering the subject"
  addressee: provider
  verbs: ["making"]
  about: "digital poverty and individual circumstances"
  themes: [theme:accessibility]
  domain: none
  award: ["bachelor's with honours", "master's"]
  gradeOf: none
  paraphrase: "Remote and blended learning widen access, but their use should always take account of each student's situation, with funding used to help those short of equipment, data or bandwidth."
  quote: full   # the issuer's statement is in `source` (D-std-0014)
  audience: practitioner
  subjects: inherited
- id: qaa/architectural-technology-2022/2.19
  locator: { number: "2.19", headingPath: ["Distinctive features of an Architectural Technology degree", "Flexibility"] }
  span: { start: 47990, end: 48320 }
  source: "Within Architectural Technology courses, there is an expectation that students will undertake a design project and/or a dissertation. This part\n\n14\n\nof the student's learning requires them to demonstrate critical analysis, evaluation and reflection to address potential risks and ethical issues associated with a proposed project."
  stem: none
  statementType: expectation
  rung: none
  force: will
  level: none
  appliesTo: "students of the subject"
  addressee: learner
  verbs: ["undertake", "demonstrate", "address"]
  about: "a design project or dissertation with critical analysis of risks and ethics"
  themes: [none]
  domain: subject-skill
  award: ["bachelor's with honours", "master's"]
  gradeOf: none
  paraphrase: "Students are expected to complete a design project, a dissertation or both, showing critical analysis, evaluation and reflection on the risks and ethical questions a proposed project raises."
  quote: full   # the issuer's statement is in `source` (D-std-0014)
  audience: both
  subjects: inherited
- id: qaa/architectural-technology-2022/3.5
  locator: { number: "3.5", headingPath: ["Content, structure and delivery", "Content"] }
  span: { start: 55522, end: 55742 }
  source: "It is anticipated that all Architectural Technology degrees will develop students' knowledge and critical understanding relating to design, technology, management and practice within a national and international context."
  stem: none
  statementType: expectation
  rung: none
  force: will
  level: none
  appliesTo: "students of the subject"
  addressee: learner
  verbs: ["develop"]
  about: "design, technology, management and practice in context"
  themes: [none]
  domain: understanding
  award: ["bachelor's with honours", "master's"]
  gradeOf: none
  paraphrase: "All degrees in the subject are expected to develop knowledge and critical understanding of design, technology, management and practice in UK and international settings."
  quote: full   # the issuer's statement is in `source` (D-std-0014)
  audience: both
  subjects: inherited
- id: qaa/architectural-technology-2022/3.6.b1
  locator: { number: "3.6.b1", headingPath: ["Content, structure and delivery", "Structure and aims of Architectural Technology honours degrees"] }
  span: { start: 55894, end: 56207 }
  source: "create economical, environmentally-sustainable, efficient and effective processes and design solutions to complex and complicated architectural design and construction challenges, from concept through to design realisation and project completion for the optimisation of the production and performance of buildings"
  stem: "3.6"
  statementType: expectation
  rung: none
  force: should
  level: fheq:6
  appliesTo: "honours courses and their students"
  addressee: both
  verbs: ["create"]
  about: "economical, sustainable processes and solutions from concept to completion"
  themes: [none]
  domain: subject-skill
  award: ["bachelor's with honours"]
  gradeOf: none
  paraphrase: "Courses should help students learn to devise economical, environmentally sustainable, efficient processes and design solutions for complex design and construction problems, from concept to completion, to optimise how buildings are produced and perform."
  quote: full   # the issuer's statement is in `source` (D-std-0014)
  audience: both
  subjects: inherited
- id: qaa/architectural-technology-2022/3.6.b2
  locator: { number: "3.6.b2", headingPath: ["Content, structure and delivery", "Structure and aims of Architectural Technology honours degrees"] }
  span: { start: 56210, end: 56423 }
  source: "adopt innovative design approaches that seek to respond to the climate emergency and contribute to reducing the impact of building and construction on the natural and built environment, minimising carbon emissions"
  stem: "3.6"
  statementType: expectation
  rung: none
  force: should
  level: fheq:6
  appliesTo: "honours courses and their students"
  addressee: both
  verbs: ["adopt", "respond", "minimising"]
  about: "innovative design for the climate emergency"
  themes: [none]
  domain: subject-skill
  award: ["bachelor's with honours"]
  gradeOf: none
  paraphrase: "Courses should help students learn to take innovative design approaches that answer the climate emergency and cut the effect of building on natural and built environments, reducing carbon emissions."
  quote: full   # the issuer's statement is in `source` (D-std-0014)
  audience: both
  subjects: inherited
- id: qaa/architectural-technology-2022/3.6.b3
  locator: { number: "3.6.b3", headingPath: ["Content, structure and delivery", "Structure and aims of Architectural Technology honours degrees"] }
  span: { start: 56426, end: 56654 }
  source: "develop a broad range of communication skills across a wide variety of graphical and textual means, both manual and digital, as well as mastering oral presentation skills transferable to any public or private setting in practice"
  stem: "3.6"
  statementType: expectation
  rung: none
  force: should
  level: fheq:6
  appliesTo: "honours courses and their students"
  addressee: both
  verbs: ["develop", "mastering"]
  about: "graphical, written, digital and oral communication"
  themes: [none]
  domain: generic-skill
  award: ["bachelor's with honours"]
  gradeOf: none
  paraphrase: "Courses should help students learn to build a wide range of communication skills, graphical and written, by hand and digitally, and to master oral presentation for any setting."
  quote: full   # the issuer's statement is in `source` (D-std-0014)
  audience: both
  subjects: inherited
- id: qaa/architectural-technology-2022/3.6.b4
  locator: { number: "3.6.b4", headingPath: ["Content, structure and delivery", "Structure and aims of Architectural Technology honours degrees"] }
  span: { start: 56657, end: 56898 }
  source: "manage the design and construction process based upon the integration of architectural technology and the utilisation of digital technologies relating to new buildings and structures, and the retrofitting of existing buildings and structures"
  stem: "3.6"
  statementType: expectation
  rung: none
  force: should
  level: fheq:6
  appliesTo: "honours courses and their students"
  addressee: both
  verbs: ["manage"]
  about: "managing design and construction with digital technologies"
  themes: [none]
  domain: subject-skill
  award: ["bachelor's with honours"]
  gradeOf: none
  paraphrase: "Courses should help students learn to manage design and construction by integrating architectural technology and digital tools, for new buildings and for retrofit."
  quote: full   # the issuer's statement is in `source` (D-std-0014)
  audience: both
  subjects: inherited
- id: qaa/architectural-technology-2022/3.6.b5
  locator: { number: "3.6.b5", headingPath: ["Content, structure and delivery", "Structure and aims of Architectural Technology honours degrees"] }
  span: { start: 56901, end: 57089 }
  source: "respond with agility and intelligence to the social, economic, environmental, technical, cultural and political context, including climate change at local, national and international level"
  stem: "3.6"
  statementType: expectation
  rung: none
  force: should
  level: fheq:6
  appliesTo: "honours courses and their students"
  addressee: both
  verbs: ["respond"]
  about: "responding to wider context, including climate change"
  themes: [none]
  domain: understanding
  award: ["bachelor's with honours"]
  gradeOf: none
  paraphrase: "Courses should help students learn to respond quickly and intelligently to social, economic, environmental, technical, cultural and political contexts, climate change included, at every scale from local to international."
  quote: full   # the issuer's statement is in `source` (D-std-0014)
  audience: both
  subjects: inherited
- id: qaa/architectural-technology-2022/3.6.b6
  locator: { number: "3.6.b6", headingPath: ["Content, structure and delivery", "Structure and aims of Architectural Technology honours degrees"] }
  span: { start: 57092, end: 57314 }
  source: "adopt a systematic approach for the process of producing accurate design information that satisfies standards and relevant legislation, and integrating the exterior envelope and interior with structure, fabric and services"
  stem: "3.6"
  statementType: expectation
  rung: none
  force: should
  level: fheq:6
  appliesTo: "honours courses and their students"
  addressee: both
  verbs: ["adopt", "satisfies", "integrating"]
  about: "accurate design information that meets standards"
  themes: [none]
  domain: subject-skill
  award: ["bachelor's with honours"]
  gradeOf: none
  paraphrase: "Courses should help students learn to work systematically in producing accurate design information that meets standards and law, integrating envelope and interior with structure, fabric and services."
  quote: full   # the issuer's statement is in `source` (D-std-0014)
  audience: both
  subjects: inherited
- id: qaa/architectural-technology-2022/3.6.b7
  locator: { number: "3.6.b7", headingPath: ["Content, structure and delivery", "Structure and aims of Architectural Technology honours degrees"] }
  span: { start: 57317, end: 57456 }
  source: "adopt strategies to optimise the management of the building life cycle through the use of information management systems for safety and use"
  stem: "3.6"
  statementType: expectation
  rung: none
  force: should
  level: fheq:6
  appliesTo: "honours courses and their students"
  addressee: both
  verbs: ["adopt", "optimise"]
  about: "managing the building life cycle with information systems"
  themes: [none]
  domain: subject-skill
  award: ["bachelor's with honours"]
  gradeOf: none
  paraphrase: "Courses should help students learn strategies that use information management systems to run the building life cycle well, for safety and use."
  quote: full   # the issuer's statement is in `source` (D-std-0014)
  audience: both
  subjects: inherited
- id: qaa/architectural-technology-2022/3.6.b8
  locator: { number: "3.6.b8", headingPath: ["Content, structure and delivery", "Structure and aims of Architectural Technology honours degrees"] }
  span: { start: 57459, end: 57634 }
  source: "embrace new and emerging concepts, technologies and practices that impact on the long-term production, performance and maintenance of new and existing buildings and structures"
  stem: "3.6"
  statementType: expectation
  rung: none
  force: should
  level: fheq:6
  appliesTo: "honours courses and their students"
  addressee: both
  verbs: ["embrace"]
  about: "new concepts, technologies and practices"
  themes: [none]
  domain: understanding
  award: ["bachelor's with honours"]
  gradeOf: none
  paraphrase: "Courses should help students learn to take up new concepts, technologies and practices that affect long-term production, performance and upkeep of buildings, new and existing."
  quote: full   # the issuer's statement is in `source` (D-std-0014)
  audience: both
  subjects: inherited
- id: qaa/architectural-technology-2022/3.6.b9
  locator: { number: "3.6.b9", headingPath: ["Content, structure and delivery", "Structure and aims of Architectural Technology honours degrees"] }
  span: { start: 57637, end: 57804 }
  source: "evaluate existing structures through building diagnostics and pathology to ensure that design solutions are compatible with the existing structure, fabric and services"
  stem: "3.6"
  statementType: expectation
  rung: none
  force: should
  level: fheq:6
  appliesTo: "honours courses and their students"
  addressee: both
  verbs: ["evaluate", "ensure"]
  about: "diagnosing existing structures"
  themes: [none]
  domain: subject-skill
  award: ["bachelor's with honours"]
  gradeOf: none
  paraphrase: "Courses should help students learn to assess existing structures through building diagnostics and pathology so that solutions suit the existing structure, fabric and services."
  quote: full   # the issuer's statement is in `source` (D-std-0014)
  audience: both
  subjects: inherited
- id: qaa/architectural-technology-2022/3.6.b10
  locator: { number: "3.6.b10", headingPath: ["Content, structure and delivery", "Structure and aims of Architectural Technology honours degrees"] }
  span: { start: 57807, end: 57966 }
  source: "embed health and safety practices from first principles through to occupation and maintenance, including, but not limited to, fire, life safety and legislation"
  stem: "3.6"
  statementType: expectation
  rung: none
  force: should
  level: fheq:6
  appliesTo: "honours courses and their students"
  addressee: both
  verbs: ["embed"]
  about: "health and safety from first principles to occupation"
  themes: [none]
  domain: subject-skill
  award: ["bachelor's with honours"]
  gradeOf: none
  paraphrase: "Courses should help students learn to build health and safety practice in from first principles through occupation and maintenance, fire and life safety and legislation among them."
  quote: full   # the issuer's statement is in `source` (D-std-0014)
  audience: both
  subjects: inherited
- id: qaa/architectural-technology-2022/3.6.b11
  locator: { number: "3.6.b11", headingPath: ["Content, structure and delivery", "Structure and aims of Architectural Technology honours degrees"] }
  span: { start: 57969, end: 58175 }
  source: "develop business and management skills, including industry and professional practice standards, client engagement, project procurement and working with other professionals, service providers and authorities"
  stem: "3.6"
  statementType: expectation
  rung: none
  force: should
  level: fheq:6
  appliesTo: "honours courses and their students"
  addressee: both
  verbs: ["develop"]
  about: "business and management skills for practice"
  themes: [none]
  domain: generic-skill
  award: ["bachelor's with honours"]
  gradeOf: none
  paraphrase: "Courses should help students learn to build business and management skills, covering industry and professional standards, client engagement, procurement and work with other professionals, service providers and authorities."
  quote: full   # the issuer's statement is in `source` (D-std-0014)
  audience: both
  subjects: inherited
- id: qaa/architectural-technology-2022/3.6.b12
  locator: { number: "3.6.b12", headingPath: ["Content, structure and delivery", "Structure and aims of Architectural Technology honours degrees"] }
  span: { start: 58178, end: 58299 }
  source: "embrace and promote the principles of equality, diversity and inclusion to ensure fairness in treatment and opportunities"
  stem: "3.6"
  statementType: expectation
  rung: none
  force: should
  level: fheq:6
  appliesTo: "honours courses and their students"
  addressee: both
  verbs: ["embrace", "promote", "ensure"]
  about: "promoting equality, diversity and inclusion"
  themes: [none]
  domain: generic-skill
  award: ["bachelor's with honours"]
  gradeOf: none
  paraphrase: "Courses should help students learn to take up and champion equality, diversity and inclusion so that people are treated fairly and given fair chances."
  quote: full   # the issuer's statement is in `source` (D-std-0014)
  audience: both
  subjects: inherited
- id: qaa/architectural-technology-2022/3.6.b13
  locator: { number: "3.6.b13", headingPath: ["Content, structure and delivery", "Structure and aims of Architectural Technology honours degrees"] }
  span: { start: 58302, end: 58486 }
  source: "recognise, respect and celebrate differences; create an environment where everyone feels welcome, included and valued, irrespective of identity; understand and prevent unconscious bias"
  stem: "3.6"
  statementType: expectation
  rung: none
  force: should
  level: fheq:6
  appliesTo: "honours courses and their students"
  addressee: both
  verbs: ["recognise", "respect", "celebrate", "create", "understand", "prevent"]
  about: "respecting difference and preventing unconscious bias"
  themes: [none]
  domain: generic-skill
  award: ["bachelor's with honours"]
  gradeOf: none
  paraphrase: "Courses should help students learn to recognise and value difference, make settings where all feel welcome and valued whatever their identity, and understand and guard against unconscious bias."
  quote: full   # the issuer's statement is in `source` (D-std-0014)
  audience: both
  subjects: inherited
- id: qaa/architectural-technology-2022/3.6.b14
  locator: { number: "3.6.b14", headingPath: ["Content, structure and delivery", "Structure and aims of Architectural Technology honours degrees"] }
  span: { start: 58489, end: 58675 }
  source: "behave in an ethical, professional and responsible manner, demonstrating awareness of the principles of social justice, ethical issues, collaborative working and effective communication."
  stem: "3.6"
  statementType: expectation
  rung: none
  force: should
  level: fheq:6
  appliesTo: "honours courses and their students"
  addressee: both
  verbs: ["behave", "demonstrating"]
  about: "ethical, professional and responsible conduct"
  themes: [none]
  domain: generic-skill
  award: ["bachelor's with honours"]
  gradeOf: none
  paraphrase: "Courses should help students learn to act ethically, professionally and responsibly, aware of social justice and ethics and working collaboratively and communicating well."
  quote: full   # the issuer's statement is in `source` (D-std-0014)
  audience: both
  subjects: inherited
- id: qaa/architectural-technology-2022/3.7.b1
  locator: { number: "3.7.b1", headingPath: ["Content, structure and delivery", "Structure and aims of Architectural Technology master's degrees"] }
  span: { start: 59097, end: 59226 }
  source: "make critically-informed choices about issues and considerations which influence the delivery of sustainable and inclusive design"
  stem: "3.7"
  statementType: outcome
  rung: none
  force: describes
  level: fheq:7
  appliesTo: "master's graduates in the subject"
  addressee: learner
  verbs: ["make", "influence"]
  about: "critically informed choices for sustainable, inclusive design"
  themes: [none]
  domain: subject-skill
  award: ["master's"]
  gradeOf: none
  paraphrase: "Make choices grounded in critical thought about the factors that shape the delivery of sustainable and inclusive design."
  quote: full   # the issuer's statement is in `source` (D-std-0014)
  audience: both
  subjects: inherited
- id: qaa/architectural-technology-2022/3.7.b2
  locator: { number: "3.7.b2", headingPath: ["Content, structure and delivery", "Structure and aims of Architectural Technology master's degrees"] }
  span: { start: 59229, end: 59429 }
  source: "research, analyse and critically appraise design methodologies relating to the building fabric and envelope, and identify relationships and influences on a healthy and comfortable building environment"
  stem: "3.7"
  statementType: outcome
  rung: none
  force: describes
  level: fheq:7
  appliesTo: "master's graduates in the subject"
  addressee: learner
  verbs: ["research", "analyse", "appraise", "identify"]
  about: "appraising fabric and envelope methods for healthy buildings"
  themes: [none]
  domain: subject-skill
  award: ["master's"]
  gradeOf: none
  paraphrase: "Research, analyse and critically judge design methods for building fabric and envelope, and find how they bear on a healthy, comfortable indoor environment."
  quote: full   # the issuer's statement is in `source` (D-std-0014)
  audience: both
  subjects: inherited
- id: qaa/architectural-technology-2022/3.7.b3
  locator: { number: "3.7.b3", headingPath: ["Content, structure and delivery", "Structure and aims of Architectural Technology master's degrees"] }
  span: { start: 59432, end: 59698 }
  source: "articulate, in a critically-informed manner, development of more complex architectural technology, construction, materials and services related to sustainability and in relation to advancements in the built environment and wider community, including inclusive design"
  stem: "3.7"
  statementType: outcome
  rung: none
  force: describes
  level: fheq:7
  appliesTo: "master's graduates in the subject"
  addressee: learner
  verbs: ["articulate"]
  about: "articulating advanced technology linked to sustainability and inclusion"
  themes: [none]
  domain: subject-skill
  award: ["master's"]
  gradeOf: none
  paraphrase: "Explain, with critical judgement, the growth of more complex technology, construction, materials and services tied to sustainability and to advances in the built environment and community, inclusive design among them."
  quote: full   # the issuer's statement is in `source` (D-std-0014)
  audience: both
  subjects: inherited
- id: qaa/architectural-technology-2022/3.7.b4
  locator: { number: "3.7.b4", headingPath: ["Content, structure and delivery", "Structure and aims of Architectural Technology master's degrees"] }
  span: { start: 59701, end: 59914 }
  source: "acquire a critical awareness of the complexities and interdependencies of sustainable design and the constraints involved in applying the theories of sustainability into practice at a variety of development scales"
  stem: "3.7"
  statementType: outcome
  rung: none
  force: describes
  level: fheq:7
  appliesTo: "master's graduates in the subject"
  addressee: learner
  verbs: ["acquire", "applying"]
  about: "complexity and constraints of sustainable design"
  themes: [none]
  domain: understanding
  award: ["master's"]
  gradeOf: none
  paraphrase: "Gain critical awareness of how the parts of sustainable design depend on one another and of the limits met when theory is put into practice at different scales."
  quote: full   # the issuer's statement is in `source` (D-std-0014)
  audience: both
  subjects: inherited
- id: qaa/architectural-technology-2022/3.7.b5
  locator: { number: "3.7.b5", headingPath: ["Content, structure and delivery", "Structure and aims of Architectural Technology master's degrees"] }
  span: { start: 59917, end: 60092 }
  source: "critically examine the relationship of architectural technology to design and construction methods, materials and components to the climate and the natural world and resources"
  stem: "3.7"
  statementType: outcome
  rung: none
  force: describes
  level: fheq:7
  appliesTo: "master's graduates in the subject"
  addressee: learner
  verbs: ["examine"]
  about: "technology, construction and materials in relation to climate and resources"
  themes: [none]
  domain: understanding
  award: ["master's"]
  gradeOf: none
  paraphrase: "Examine critically how architectural technology relates design and construction methods, materials and components to climate, the natural world and resources."
  quote: full   # the issuer's statement is in `source` (D-std-0014)
  audience: both
  subjects: inherited
- id: qaa/architectural-technology-2022/3.7.b6
  locator: { number: "3.7.b6", headingPath: ["Content, structure and delivery", "Structure and aims of Architectural Technology master's degrees"] }
  span: { start: 60095, end: 60241 }
  source: "demonstrate a critical awareness of sustainable design principles and emergent technologies and concepts using a wide range of information sources"
  stem: "3.7"
  statementType: outcome
  rung: none
  force: describes
  level: fheq:7
  appliesTo: "master's graduates in the subject"
  addressee: learner
  verbs: ["demonstrate", "using"]
  about: "sustainable design principles and emerging technologies"
  themes: [none]
  domain: knowledge
  award: ["master's"]
  gradeOf: none
  paraphrase: "Show critical awareness of the principles of sustainable design and of new technologies and ideas, drawing on many kinds of source."
  quote: full   # the issuer's statement is in `source` (D-std-0014)
  audience: both
  subjects: inherited
- id: qaa/architectural-technology-2022/3.7.b7
  locator: { number: "3.7.b7", headingPath: ["Content, structure and delivery", "Structure and aims of Architectural Technology master's degrees"] }
  span: { start: 60244, end: 60460 }
  source: "critically evaluate the theoretical approaches and form considered judgements relevant to the spatial, aesthetic, technical and social qualities of a sustainable design within the scope and scale of wider development"
  stem: "3.7"
  statementType: outcome
  rung: none
  force: describes
  level: fheq:7
  appliesTo: "master's graduates in the subject"
  addressee: learner
  verbs: ["evaluate", "form"]
  about: "judging theory and the qualities of sustainable design at scale"
  themes: [none]
  domain: subject-skill
  award: ["master's"]
  gradeOf: none
  paraphrase: "Evaluate theoretical approaches critically and reach reasoned judgements on how a sustainable design works in space, appearance, technique and society at the scale of wider development."
  quote: full   # the issuer's statement is in `source` (D-std-0014)
  audience: both
  subjects: inherited
- id: qaa/architectural-technology-2022/3.7.b8
  locator: { number: "3.7.b8", headingPath: ["Content, structure and delivery", "Structure and aims of Architectural Technology master's degrees"] }
  span: { start: 60463, end: 60663 }
  source: "define objectives pertinent to the chosen architectural technology research problem, critically evaluate and apply established techniques of research and enquiry in pursuing those research objectives."
  stem: "3.7"
  statementType: outcome
  rung: none
  force: describes
  level: fheq:7
  appliesTo: "master's graduates in the subject"
  addressee: learner
  verbs: ["define", "evaluate", "apply", "pursuing"]
  about: "research objectives and methods"
  themes: [none]
  domain: subject-skill
  award: ["master's"]
  gradeOf: none
  paraphrase: "Set objectives for a chosen research problem in the subject, then judge critically and use established research techniques to meet them."
  quote: full   # the issuer's statement is in `source` (D-std-0014)
  audience: both
  subjects: inherited
- id: qaa/architectural-technology-2022/3.15
  locator: { number: "3.15", headingPath: ["Content, structure and delivery", "Teaching and learning"] }
  span: { start: 64143, end: 64255 }
  source: "Students will further develop their subject with a consideration of professional, ethical, and practical issues."
  stem: none
  statementType: outcome
  rung: none
  force: will
  level: fheq:7
  appliesTo: "master's students in the subject"
  addressee: learner
  verbs: ["develop"]
  about: "professional, ethical and practical issues at master's level"
  themes: [none]
  domain: understanding
  award: ["master's"]
  gradeOf: none
  paraphrase: "Master's students will deepen their subject while weighing its professional, ethical and practical questions."
  quote: full   # the issuer's statement is in `source` (D-std-0014)
  audience: both
  subjects: inherited
- id: qaa/architectural-technology-2022/3.17
  locator: { number: "3.17", headingPath: ["Content, structure and delivery", "Teaching and learning"] }
  span: { start: 64673, end: 65195 }
  source: "Students will develop their research skills further completing an advanced research or design project. Students are challenged to think in critical, creative and applied ways, devise research questions, design and conduct a research methodology, and produce original knowledge which will be important to the discipline. As well as conducting their own research project, students will communicate their research professionally to the academic and/or professional community using professional written, oral and visual means."
  stem: none
  statementType: outcome
  rung: none
  force: will
  level: fheq:7
  appliesTo: "master's students in the subject"
  addressee: learner
  verbs: ["develop", "completing", "communicate"]
  about: "an advanced research or design project, communicated professionally"
  themes: [none]
  domain: subject-skill
  award: ["master's"]
  gradeOf: none
  paraphrase: "Master's students will strengthen their research skills through an advanced research or design project, thinking critically and creatively, framing questions, designing a method and producing original knowledge, and will present the work to academic or professional audiences in writing, speech and visuals."
  quote: full   # the issuer's statement is in `source` (D-std-0014)
  audience: both
  subjects: inherited
- id: qaa/architectural-technology-2022/3.19
  locator: { number: "3.19", headingPath: ["Content, structure and delivery", "Assessment"] }
  span: { start: 65420, end: 65910 }
  source: "3.19 Architectural Technology courses should contain an explicit assessment strategy as part of their curriculum design. This strategy will clearly and directly reflect the learning\n\n19\n\noutcomes of the course components, support student learning, and enable students to demonstrate progressive levels of attainment. The strategy will reflect the variety of abilities and skills developed within the curriculum tied to the methods of teaching and learning adopted by the particular course.\n"
  stem: none
  statementType: requirement
  rung: none
  force: should
  level: none
  appliesTo: "courses in the subject"
  addressee: provider
  verbs: ["contain", "reflect", "support", "enable", "demonstrate"]
  about: "an explicit assessment strategy"
  themes: [none]
  domain: none
  award: ["bachelor's with honours", "master's"]
  gradeOf: none
  paraphrase: "Courses should have a clear assessment strategy in their design that follows the learning outcomes, supports learning, lets students show rising attainment and matches the teaching methods used."
  quote: full   # the issuer's statement is in `source` (D-std-0014)
  audience: practitioner
  subjects: inherited
- id: qaa/architectural-technology-2022/3.20
  locator: { number: "3.20", headingPath: ["Content, structure and delivery", "Assessment"] }
  span: { start: 65915, end: 66165 }
  source: "The assessment strategies and vehicles of assessment of Architectural Technology courses should include a mix of methods that are, overall, accessible to students from varying educational and cultural backgrounds within different learning situations."
  stem: none
  statementType: requirement
  rung: none
  force: should
  level: none
  appliesTo: "assessment in the subject"
  addressee: provider
  verbs: ["include"]
  about: "an accessible mix of assessment methods"
  themes: [none]
  domain: none
  award: ["bachelor's with honours", "master's"]
  gradeOf: none
  paraphrase: "Assessment in the subject should use a mix of methods that, taken together, students from different educational and cultural backgrounds can access."
  quote: full   # the issuer's statement is in `source` (D-std-0014)
  audience: practitioner
  subjects: inherited
- id: qaa/architectural-technology-2022/3.20.s2
  locator: { number: "3.20.s2", headingPath: ["Content, structure and delivery", "Assessment"] }
  span: { start: 66166, end: 66388 }
  source: "Where individual students may be disadvantaged by particular assessment methods, adjustments to those assessments must be considered in discussion with the student concerned, while ensuring fairness across the full cohort."
  stem: none
  statementType: requirement
  rung: none
  force: must
  level: none
  appliesTo: "assessment in the subject"
  addressee: provider
  verbs: ["considered", "ensuring"]
  about: "adjustments discussed with the student"
  themes: [none]
  domain: none
  award: ["bachelor's with honours", "master's"]
  gradeOf: none
  paraphrase: "Where a method of assessment may disadvantage a student, adjustments must be considered together with that student, keeping the whole cohort fairly treated."
  quote: full   # the issuer's statement is in `source` (D-std-0014)
  audience: practitioner
  subjects: inherited
- id: qaa/architectural-technology-2022/3.21
  locator: { number: "3.21", headingPath: ["Content, structure and delivery", "Assessment"] }
  span: { start: 67039, end: 67175 }
  source: "Architectural Technology courses should use a range of assessment methods during the course that reflect the range of learning outcomes."
  stem: none
  statementType: requirement
  rung: none
  force: should
  level: none
  appliesTo: "courses in the subject"
  addressee: provider
  verbs: ["use", "reflect"]
  about: "a range of assessment methods matched to outcomes"
  themes: [none]
  domain: none
  award: ["bachelor's with honours", "master's"]
  gradeOf: none
  paraphrase: "Courses should use varied assessment methods that match the variety of their learning outcomes; the ten methods listed after it are an indication of practice, not a checklist."
  quote: full   # the issuer's statement is in `source` (D-std-0014)
  audience: practitioner
  subjects: inherited
- id: qaa/architectural-technology-2022/4.2
  locator: { number: "4.2", headingPath: ["Benchmark standards", "Introduction"] }
  span: { start: 69297, end: 69781 }
  source: "4.2 The vast majority of students will perform significantly better than the minimum threshold standards. Each higher education provider has its own method of determining what appropriate evidence of this achievement will be and should refer to Annex D: Outcome classification descriptions for FHEQ Level 6 and FQHEIS Level 10 degrees. This Annex sets out common descriptions of the four main degree outcome classifications for bachelor's degrees with honours: 1st, 2.1, 2.2 and 3rd.\n"
  stem: none
  statementType: requirement
  rung: none
  force: should
  level: fheq:6
  appliesTo: "higher education providers"
  addressee: provider
  verbs: ["refer"]
  about: "Annex D for performance above threshold"
  themes: [none]
  domain: none
  award: ["bachelor's with honours"]
  gradeOf: none
  paraphrase: "Most students will do far better than threshold; each provider decides what evidence shows this and should refer to the degree classification descriptions in Annex D for FHEQ Level 6 and FQHEIS Level 10."
  quote: full   # the issuer's statement is in `source` (D-std-0014)
  audience: practitioner
  subjects: inherited
- id: qaa/architectural-technology-2022/4.4
  locator: { number: "4.4", headingPath: ["Benchmark standards", "Introduction"] }
  span: { start: 70241, end: 70438 }
  source: "It is anticipated that all courses in Architectural Technology will enable students to become conversant with the main aspects of the subject (that is, design, technology, management and practice)."
  stem: none
  statementType: expectation
  rung: none
  force: will
  level: none
  appliesTo: "students of the subject"
  addressee: learner
  verbs: ["enable", "become"]
  about: "fluency in design, technology, management and practice"
  themes: [none]
  domain: knowledge
  award: ["bachelor's with honours", "master's"]
  gradeOf: none
  paraphrase: "All courses are expected to make students fluent in the four main aspects of the subject: design, technology, management and practice."
  quote: full   # the issuer's statement is in `source` (D-std-0014)
  audience: both
  subjects: inherited
- id: qaa/architectural-technology-2022/4.6.b1
  locator: { number: "4.6.b1", headingPath: ["Benchmark standards", "Benchmark standards for honours degrees (threshold)"] }
  span: { start: 71432, end: 71663 }
  source: "context, which includes the social, technological, environmental, economic, political, legal and ethical factors that inform and influence the discipline and practice of architectural technology at local, regional and global levels"
  stem: "4.6"
  statementType: threshold
  rung: threshold
  force: threshold
  level: fheq:6
  appliesTo: "honours graduates at threshold"
  addressee: learner
  verbs: ["inform", "influence"]
  about: "the wider factors shaping the discipline"
  themes: [none]
  domain: understanding
  award: ["bachelor's with honours"]
  gradeOf: none
  paraphrase: "At threshold, the graduate shows grasp of the wider forces (social, economic, environmental, political, legal, ethical and technical) acting on the discipline and its practice at local, regional and global scale."
  quote: full   # the issuer's statement is in `source` (D-std-0014)
  audience: both
  subjects: inherited
- id: qaa/architectural-technology-2022/4.6.b2
  locator: { number: "4.6.b2", headingPath: ["Benchmark standards", "Benchmark standards for honours degrees (threshold)"] }
  span: { start: 71666, end: 71908 }
  source: "professional behaviours, conduct and ethics, architectural practice, design leadership and management functions (for example, principal/lead designer, design management, information management), procurement methods and contract administration"
  stem: "4.6"
  statementType: threshold
  rung: threshold
  force: threshold
  level: fheq:6
  appliesTo: "honours graduates at threshold"
  addressee: learner
  verbs: []
  about: "professional conduct, practice, design leadership, procurement and contracts"
  themes: [none]
  domain: knowledge
  award: ["bachelor's with honours"]
  gradeOf: none
  paraphrase: "At threshold, the graduate shows grasp of professional conduct and ethics, how practice works, design leadership and management roles (such as lead or principal designer, design and information management), procurement routes and contract administration."
  quote: full   # the issuer's statement is in `source` (D-std-0014)
  audience: both
  subjects: inherited
- id: qaa/architectural-technology-2022/4.6.b3
  locator: { number: "4.6.b3", headingPath: ["Benchmark standards", "Benchmark standards for honours degrees (threshold)"] }
  span: { start: 71911, end: 72135 }
  source: "technologies and interrelation of building elements, systems, components, materials and methods used in the construction and adaptation of different building typologies, and how these contribute to the functions of buildings"
  stem: "4.6"
  statementType: threshold
  rung: threshold
  force: threshold
  level: fheq:6
  appliesTo: "honours graduates at threshold"
  addressee: learner
  verbs: ["used", "contribute"]
  about: "building technologies and how elements interrelate"
  themes: [none]
  domain: knowledge
  award: ["bachelor's with honours"]
  gradeOf: none
  paraphrase: "At threshold, the graduate shows grasp of building technologies and how elements, systems, components, materials and methods fit together across building types, in new construction and adaptation, and serve the building's functions."
  quote: full   # the issuer's statement is in `source` (D-std-0014)
  audience: both
  subjects: inherited
- id: qaa/architectural-technology-2022/4.6.b4
  locator: { number: "4.6.b4", headingPath: ["Benchmark standards", "Benchmark standards for honours degrees (threshold)"] }
  span: { start: 72143, end: 72405 }
  source: "architectural and technological design principles, science (that is, fundamentals of building physics and pathology) and values that drive approaches taken in works to new and existing buildings (for example, conservation, maintenance, renovation and adaptation)"
  stem: "4.6"
  statementType: threshold
  rung: threshold
  force: threshold
  level: fheq:6
  appliesTo: "honours graduates at threshold"
  addressee: learner
  verbs: ["drive"]
  about: "design principles, building science and values for new and existing buildings"
  themes: [none]
  domain: understanding
  award: ["bachelor's with honours"]
  gradeOf: none
  paraphrase: "At threshold, the graduate shows grasp of architectural and technical design principles, building science (the basics of building physics and pathology) and the values guiding work on new and existing buildings, such as conservation, renovation and adaptation."
  quote: full   # the issuer's statement is in `source` (D-std-0014)
  audience: both
  subjects: inherited
- id: qaa/architectural-technology-2022/4.6.b5
  locator: { number: "4.6.b5", headingPath: ["Benchmark standards", "Benchmark standards for honours degrees (threshold)"] }
  span: { start: 72408, end: 72692 }
  source: "designing holistically, including the ability to detail the design from first principles, for production, performance, sustainability and better environmental performance and in response to regulatory requirements, health and safety, wellbeing and advances in sustainable technologies"
  stem: "4.6"
  statementType: threshold
  rung: threshold
  force: threshold
  level: fheq:6
  appliesTo: "honours graduates at threshold"
  addressee: learner
  verbs: ["designing", "detail"]
  about: "holistic design and detailing from first principles"
  themes: [none]
  domain: subject-skill
  award: ["bachelor's with honours"]
  gradeOf: none
  paraphrase: "At threshold, the graduate shows the ability to design as a whole and detail from first principles for production, performance and sustainability, responding to regulation, health and safety, wellbeing and new sustainable technologies."
  quote: full   # the issuer's statement is in `source` (D-std-0014)
  audience: both
  subjects: inherited
- id: qaa/architectural-technology-2022/4.6.b6
  locator: { number: "4.6.b6", headingPath: ["Benchmark standards", "Benchmark standards for honours degrees (threshold)"] }
  span: { start: 72695, end: 72856 }
  source: "client, user and stakeholder needs, analysing and interpreting the nature of a development, and evaluating context to determine the responsive scope of a project"
  stem: "4.6"
  statementType: threshold
  rung: threshold
  force: threshold
  level: fheq:6
  appliesTo: "honours graduates at threshold"
  addressee: learner
  verbs: ["analysing", "interpreting", "evaluating", "determine"]
  about: "client, user and stakeholder needs and project scope"
  themes: [none]
  domain: subject-skill
  award: ["bachelor's with honours"]
  gradeOf: none
  paraphrase: "At threshold, the graduate shows the ability to work with client, user and stakeholder needs, analysing a development and reading its context to set a fitting project scope."
  quote: full   # the issuer's statement is in `source` (D-std-0014)
  audience: both
  subjects: inherited
- id: qaa/architectural-technology-2022/4.6.b7
  locator: { number: "4.6.b7", headingPath: ["Benchmark standards", "Benchmark standards for honours degrees (threshold)"] }
  span: { start: 72859, end: 73121 }
  source: "health and safety requirements within a regulatory system, identifying, analysing, and evaluating hazards and risks when generating solutions to ensure health, safety, welfare and security during the life cycles of buildings, including compliance and enforcement"
  stem: "4.6"
  statementType: threshold
  rung: threshold
  force: threshold
  level: fheq:6
  appliesTo: "honours graduates at threshold"
  addressee: learner
  verbs: ["identifying", "analysing", "evaluating", "ensure"]
  about: "health and safety, hazards and risk over the life cycle"
  themes: [none]
  domain: subject-skill
  award: ["bachelor's with honours"]
  gradeOf: none
  paraphrase: "At threshold, the graduate shows the ability to work within regulatory health and safety requirements, finding, analysing and judging hazards and risks when designing, to secure health, safety, welfare and security over a building's life, compliance and enforcement included."
  quote: full   # the issuer's statement is in `source` (D-std-0014)
  audience: both
  subjects: inherited
- id: qaa/architectural-technology-2022/4.6.b8
  locator: { number: "4.6.b8", headingPath: ["Benchmark standards", "Benchmark standards for honours degrees (threshold)"] }
  span: { start: 73124, end: 73362 }
  source: "creating resilient, sustainable and inclusive design solutions as whole systems and in detail in response to varied situations, which are informed by current understandings within the discipline and wider context, including climate change"
  stem: "4.6"
  statementType: threshold
  rung: threshold
  force: threshold
  level: fheq:6
  appliesTo: "honours graduates at threshold"
  addressee: learner
  verbs: ["creating"]
  about: "resilient, sustainable, inclusive solutions"
  themes: [none]
  domain: subject-skill
  award: ["bachelor's with honours"]
  gradeOf: none
  paraphrase: "At threshold, the graduate shows the ability to produce design solutions that are resilient, sustainable and inclusive, both as complete systems and in detail, for varied situations, informed by current thinking and by climate change."
  quote: full   # the issuer's statement is in `source` (D-std-0014)
  audience: both
  subjects: inherited
- id: qaa/architectural-technology-2022/4.6.b9
  locator: { number: "4.6.b9", headingPath: ["Benchmark standards", "Benchmark standards for honours degrees (threshold)"] }
  span: { start: 73365, end: 73573 }
  source: "current philosophies, processes and technologies for the modelling, communication, and management of information and to apply them in a collaborative working environment to support data-driven decision-making"
  stem: "4.6"
  statementType: threshold
  rung: threshold
  force: threshold
  level: fheq:6
  appliesTo: "honours graduates at threshold"
  addressee: learner
  verbs: ["apply", "support"]
  about: "modelling and information management in collaborative work"
  themes: [none]
  domain: subject-skill
  award: ["bachelor's with honours"]
  gradeOf: none
  paraphrase: "At threshold, the graduate shows grasp of current approaches, processes and technologies for modelling, communicating and managing information, and applies them in collaborative work to support decisions driven by data."
  quote: full   # the issuer's statement is in `source` (D-std-0014)
  audience: both
  subjects: inherited
- id: qaa/architectural-technology-2022/4.6.b10
  locator: { number: "4.6.b10", headingPath: ["Benchmark standards", "Benchmark standards for honours degrees (threshold)"] }
  span: { start: 73576, end: 73938 }
  source: "current and emerging topics, technologies and practices (including regulations and standards) that inform the architectural technology discipline through self-reflection, identification of personal development needs, and action planning to maintain awareness and currency, and to accommodate specialisation in light of new and emerging professional environments."
  stem: "4.6"
  statementType: threshold
  rung: threshold
  force: threshold
  level: fheq:6
  appliesTo: "honours graduates at threshold"
  addressee: learner
  verbs: ["inform", "maintain", "accommodate"]
  about: "staying current through reflection and development planning"
  themes: [none]
  domain: generic-skill
  award: ["bachelor's with honours"]
  gradeOf: none
  paraphrase: "At threshold, the graduate shows awareness of current and new topics, technologies and practices, regulations and standards included, kept up through reflecting on oneself, naming development needs and planning action, so as to stay current and to specialise."
  quote: full   # the issuer's statement is in `source` (D-std-0014)
  audience: both
  subjects: inherited
- id: qaa/architectural-technology-2022/4.7.b1
  locator: { number: "4.7.b1", headingPath: ["Benchmark standards", "Benchmark standards for master's degrees (threshold)"] }
  span: { start: 74121, end: 74357 }
  source: "critical awareness of the historical and contemporary context, and the underpinning social, technological, environmental, economic, political, legal and ethical theories that inform and influence the practice of architectural technology"
  stem: "4.7"
  statementType: threshold
  rung: threshold
  force: threshold
  level: fheq:7
  appliesTo: "master's graduates at threshold"
  addressee: learner
  verbs: ["inform", "influence"]
  about: "critical awareness of context and underpinning theories"
  themes: [none]
  domain: knowledge
  award: ["master's"]
  gradeOf: none
  paraphrase: "At threshold, the master's graduate shows critical awareness of the past and present context and of the social, economic, environmental, political, legal, ethical and technical theories shaping practice."
  quote: full   # the issuer's statement is in `source` (D-std-0014)
  audience: both
  subjects: inherited
- id: qaa/architectural-technology-2022/4.7.b2
  locator: { number: "4.7.b2", headingPath: ["Benchmark standards", "Benchmark standards for master's degrees (threshold)"] }
  span: { start: 74360, end: 74516 }
  source: "systematic understanding and critical awareness of current and emerging trends in architectural technology such as, but not limited to, digital construction"
  stem: "4.7"
  statementType: threshold
  rung: threshold
  force: threshold
  level: fheq:7
  appliesTo: "master's graduates at threshold"
  addressee: learner
  verbs: []
  about: "current and emerging trends such as digital construction"
  themes: [none]
  domain: knowledge
  award: ["master's"]
  gradeOf: none
  paraphrase: "At threshold, the master's graduate shows systematic understanding and critical awareness of present and emerging trends, digital construction among them."
  quote: full   # the issuer's statement is in `source` (D-std-0014)
  audience: both
  subjects: inherited
- id: qaa/architectural-technology-2022/4.7.b3
  locator: { number: "4.7.b3", headingPath: ["Benchmark standards", "Benchmark standards for master's degrees (threshold)"] }
  span: { start: 74519, end: 74592 }
  source: "evaluation of appropriate methodologies for dealing with complex problems"
  stem: "4.7"
  statementType: threshold
  rung: threshold
  force: threshold
  level: fheq:7
  appliesTo: "master's graduates at threshold"
  addressee: learner
  verbs: ["dealing"]
  about: "evaluating methods for complex problems"
  themes: [none]
  domain: subject-skill
  award: ["master's"]
  gradeOf: none
  paraphrase: "At threshold, the master's graduate shows the ability to weigh up suitable methods for handling complex problems."
  quote: full   # the issuer's statement is in `source` (D-std-0014)
  audience: both
  subjects: inherited
- id: qaa/architectural-technology-2022/4.7.b4
  locator: { number: "4.7.b4", headingPath: ["Benchmark standards", "Benchmark standards for master's degrees (threshold)"] }
  span: { start: 74595, end: 74717 }
  source: "independent analysis of complex concepts applied in the generation of critical discussion by working with some originality"
  stem: "4.7"
  statementType: threshold
  rung: threshold
  force: threshold
  level: fheq:7
  appliesTo: "master's graduates at threshold"
  addressee: learner
  verbs: ["applied", "working"]
  about: "independent analysis with some originality"
  themes: [none]
  domain: subject-skill
  award: ["master's"]
  gradeOf: none
  paraphrase: "At threshold, the master's graduate shows independent analysis of complex ideas, used to drive critical discussion, with some originality."
  quote: full   # the issuer's statement is in `source` (D-std-0014)
  audience: both
  subjects: inherited
- id: qaa/architectural-technology-2022/4.7.b5
  locator: { number: "4.7.b5", headingPath: ["Benchmark standards", "Benchmark standards for master's degrees (threshold)"] }
  span: { start: 74720, end: 74851 }
  source: "completion of a major piece of design work, or substantial research project, informed by thorough understandings of the discipline."
  stem: "4.7"
  statementType: threshold
  rung: threshold
  force: threshold
  level: fheq:7
  appliesTo: "master's graduates at threshold"
  addressee: learner
  verbs: ["informed"]
  about: "a major design work or substantial research project"
  themes: [none]
  domain: subject-skill
  award: ["master's"]
  gradeOf: none
  paraphrase: "At threshold, the master's graduate has completed a major design work or a substantial research project grounded in a thorough grasp of the discipline."
  quote: full   # the issuer's statement is in `source` (D-std-0014)
  audience: both
  subjects: inherited
- id: qaa/architectural-technology-2022/4.8.b1
  locator: { number: "4.8.b1", headingPath: ["Benchmark standards", "Generic skills for Architectural Technology graduates"] }
  span: { start: 75006, end: 75046 }
  source: "perform assigned tasks as part of a team"
  stem: "4.8"
  statementType: outcome
  rung: none
  force: should
  level: fheq:6
  appliesTo: "honours graduates of the subject"
  addressee: learner
  verbs: ["perform"]
  about: "teamwork on assigned tasks"
  themes: [none]
  domain: generic-skill
  award: ["bachelor's with honours"]
  gradeOf: none
  paraphrase: "Should be able to carry out the tasks given to them within a team."
  quote: full   # the issuer's statement is in `source` (D-std-0014)
  audience: both
  subjects: inherited
- id: qaa/architectural-technology-2022/4.8.b2
  locator: { number: "4.8.b2", headingPath: ["Benchmark standards", "Generic skills for Architectural Technology graduates"] }
  span: { start: 75049, end: 75112 }
  source: "bring together information and materials from different sources"
  stem: "4.8"
  statementType: outcome
  rung: none
  force: should
  level: fheq:6
  appliesTo: "honours graduates of the subject"
  addressee: learner
  verbs: ["bring"]
  about: "combining information from several sources"
  themes: [none]
  domain: generic-skill
  award: ["bachelor's with honours"]
  gradeOf: none
  paraphrase: "Should be able to gather information and material from varied sources into one whole."
  quote: full   # the issuer's statement is in `source` (D-std-0014)
  audience: both
  subjects: inherited
- id: qaa/architectural-technology-2022/4.8.b3
  locator: { number: "4.8.b3", headingPath: ["Benchmark standards", "Generic skills for Architectural Technology graduates"] }
  span: { start: 75115, end: 75146 }
  source: "identify problems and questions"
  stem: "4.8"
  statementType: outcome
  rung: none
  force: should
  level: fheq:6
  appliesTo: "honours graduates of the subject"
  addressee: learner
  verbs: ["identify"]
  about: "identifying problems and questions"
  themes: [none]
  domain: generic-skill
  award: ["bachelor's with honours"]
  gradeOf: none
  paraphrase: "Should be able to spot problems and the questions they raise."
  quote: full   # the issuer's statement is in `source` (D-std-0014)
  audience: both
  subjects: inherited
- id: qaa/architectural-technology-2022/4.8.b4
  locator: { number: "4.8.b4", headingPath: ["Benchmark standards", "Generic skills for Architectural Technology graduates"] }
  span: { start: 75149, end: 75194 }
  source: "undertake the analysis of factual information"
  stem: "4.8"
  statementType: outcome
  rung: none
  force: should
  level: fheq:6
  appliesTo: "honours graduates of the subject"
  addressee: learner
  verbs: ["undertake"]
  about: "analysing factual information"
  themes: [none]
  domain: generic-skill
  award: ["bachelor's with honours"]
  gradeOf: none
  paraphrase: "Should be able to analyse information of a factual kind."
  quote: full   # the issuer's statement is in `source` (D-std-0014)
  audience: both
  subjects: inherited
- id: qaa/architectural-technology-2022/4.8.b5
  locator: { number: "4.8.b5", headingPath: ["Benchmark standards", "Generic skills for Architectural Technology graduates"] }
  span: { start: 75202, end: 75263 }
  source: "recognise strengths and weaknesses in the arguments of others"
  stem: "4.8"
  statementType: outcome
  rung: none
  force: should
  level: fheq:6
  appliesTo: "honours graduates of the subject"
  addressee: learner
  verbs: ["recognise"]
  about: "judging others' arguments"
  themes: [none]
  domain: generic-skill
  award: ["bachelor's with honours"]
  gradeOf: none
  paraphrase: "Should be able to see where the arguments of other people are strong and where weak."
  quote: full   # the issuer's statement is in `source` (D-std-0014)
  audience: both
  subjects: inherited
- id: qaa/architectural-technology-2022/4.8.b6
  locator: { number: "4.8.b6", headingPath: ["Benchmark standards", "Generic skills for Architectural Technology graduates"] }
  span: { start: 75266, end: 75344 }
  source: "produce a synthesis of the state of knowledge on a particular subject or topic"
  stem: "4.8"
  statementType: outcome
  rung: none
  force: should
  level: fheq:6
  appliesTo: "honours graduates of the subject"
  addressee: learner
  verbs: ["produce"]
  about: "synthesising what is known on a topic"
  themes: [none]
  domain: generic-skill
  award: ["bachelor's with honours"]
  gradeOf: none
  paraphrase: "Should be able to draw together what is currently known about a given subject or topic."
  quote: full   # the issuer's statement is in `source` (D-std-0014)
  audience: both
  subjects: inherited
- id: qaa/architectural-technology-2022/4.8.b7
  locator: { number: "4.8.b7", headingPath: ["Benchmark standards", "Generic skills for Architectural Technology graduates"] }
  span: { start: 75347, end: 75391 }
  source: "with guidance, undertake tasks independently"
  stem: "4.8"
  statementType: outcome
  rung: none
  force: should
  level: fheq:6
  appliesTo: "honours graduates of the subject"
  addressee: learner
  verbs: ["undertake"]
  about: "working independently with guidance"
  themes: [none]
  domain: generic-skill
  award: ["bachelor's with honours"]
  gradeOf: none
  paraphrase: "Should be able, with guidance, to carry out tasks on their own."
  quote: full   # the issuer's statement is in `source` (D-std-0014)
  audience: both
  subjects: inherited
- id: qaa/architectural-technology-2022/4.8.b8
  locator: { number: "4.8.b8", headingPath: ["Benchmark standards", "Generic skills for Architectural Technology graduates"] }
  span: { start: 75394, end: 75457 }
  source: "reflect on their own progress and make use of feedback provided"
  stem: "4.8"
  statementType: outcome
  rung: none
  force: should
  level: fheq:6
  appliesTo: "honours graduates of the subject"
  addressee: learner
  verbs: ["reflect", "make"]
  about: "reflection and using feedback"
  themes: [none]
  domain: generic-skill
  award: ["bachelor's with honours"]
  gradeOf: none
  paraphrase: "Should be able to review their own progress and act on the feedback given."
  quote: full   # the issuer's statement is in `source` (D-std-0014)
  audience: both
  subjects: inherited
- id: qaa/architectural-technology-2022/4.8.b9
  locator: { number: "4.8.b9", headingPath: ["Benchmark standards", "Generic skills for Architectural Technology graduates"] }
  span: { start: 75460, end: 75524 }
  source: "express themselves effectively both verbally and/or non-verbally"
  stem: "4.8"
  statementType: outcome
  rung: none
  force: should
  level: fheq:6
  appliesTo: "honours graduates of the subject"
  addressee: learner
  verbs: ["express"]
  about: "communicating verbally and non-verbally"
  themes: [none]
  domain: generic-skill
  award: ["bachelor's with honours"]
  gradeOf: none
  paraphrase: "Should be able to communicate well in speech, in other forms, or both."
  quote: full   # the issuer's statement is in `source` (D-std-0014)
  audience: both
  subjects: inherited
- id: qaa/architectural-technology-2022/4.8.b10
  locator: { number: "4.8.b10", headingPath: ["Benchmark standards", "Generic skills for Architectural Technology graduates"] }
  span: { start: 75527, end: 75601 }
  source: "present knowledge or an argument in a way that is comprehensible to others"
  stem: "4.8"
  statementType: outcome
  rung: none
  force: should
  level: fheq:6
  appliesTo: "honours graduates of the subject"
  addressee: learner
  verbs: ["present"]
  about: "presenting so others understand"
  themes: [none]
  domain: generic-skill
  award: ["bachelor's with honours"]
  gradeOf: none
  paraphrase: "Should be able to set out knowledge or an argument so other people can follow it."
  quote: full   # the issuer's statement is in `source` (D-std-0014)
  audience: both
  subjects: inherited
- id: qaa/architectural-technology-2022/4.8.b11
  locator: { number: "4.8.b11", headingPath: ["Benchmark standards", "Generic skills for Architectural Technology graduates"] }
  span: { start: 75604, end: 75684 }
  source: "use relevant digital systems to collate, analyse, select and present information"
  stem: "4.8"
  statementType: outcome
  rung: none
  force: should
  level: fheq:6
  appliesTo: "honours graduates of the subject"
  addressee: learner
  verbs: ["use", "collate", "analyse", "select", "present"]
  about: "digital information handling"
  themes: [none]
  domain: generic-skill
  award: ["bachelor's with honours"]
  gradeOf: none
  paraphrase: "Should be able to use suitable digital systems to gather, analyse, choose and present information."
  quote: full   # the issuer's statement is in `source` (D-std-0014)
  audience: both
  subjects: inherited
- id: qaa/architectural-technology-2022/4.8.b12
  locator: { number: "4.8.b12", headingPath: ["Benchmark standards", "Generic skills for Architectural Technology graduates"] }
  span: { start: 75687, end: 75745 }
  source: "deliver presentations utilising visual aids and multimedia"
  stem: "4.8"
  statementType: outcome
  rung: none
  force: should
  level: fheq:6
  appliesTo: "honours graduates of the subject"
  addressee: learner
  verbs: ["deliver", "utilising"]
  about: "presentations with visual aids and media"
  themes: [none]
  domain: generic-skill
  award: ["bachelor's with honours"]
  gradeOf: none
  paraphrase: "Should be able to give presentations supported by visual aids and media."
  quote: full   # the issuer's statement is in `source` (D-std-0014)
  audience: both
  subjects: inherited
- id: qaa/architectural-technology-2022/4.8.b13
  locator: { number: "4.8.b13", headingPath: ["Benchmark standards", "Generic skills for Architectural Technology graduates"] }
  span: { start: 75748, end: 75829 }
  source: "demonstrate an ability to comprehend when presented with new ideas or information"
  stem: "4.8"
  statementType: outcome
  rung: none
  force: should
  level: fheq:6
  appliesTo: "honours graduates of the subject"
  addressee: learner
  verbs: ["demonstrate", "comprehend"]
  about: "grasping new ideas and information"
  themes: [none]
  domain: generic-skill
  award: ["bachelor's with honours"]
  gradeOf: none
  paraphrase: "Should be able to show they can grasp new ideas or information when met."
  quote: full   # the issuer's statement is in `source` (D-std-0014)
  audience: both
  subjects: inherited
- id: qaa/architectural-technology-2022/4.8.b14
  locator: { number: "4.8.b14", headingPath: ["Benchmark standards", "Generic skills for Architectural Technology graduates"] }
  span: { start: 75832, end: 75889 }
  source: "demonstrate skills in recognising and describing material"
  stem: "4.8"
  statementType: outcome
  rung: none
  force: should
  level: fheq:6
  appliesTo: "honours graduates of the subject"
  addressee: learner
  verbs: ["demonstrate", "recognising", "describing"]
  about: "recognising and describing material"
  themes: [none]
  domain: generic-skill
  award: ["bachelor's with honours"]
  gradeOf: none
  paraphrase: "Should be able to show skill in identifying and describing material."
  quote: full   # the issuer's statement is in `source` (D-std-0014)
  audience: both
  subjects: inherited
- id: qaa/architectural-technology-2022/4.8.b15
  locator: { number: "4.8.b15", headingPath: ["Benchmark standards", "Generic skills for Architectural Technology graduates"] }
  span: { start: 75892, end: 76008 }
  source: "understand the importance of health and safety, and of equality, diversity and inclusiveness in the work environment"
  stem: "4.8"
  statementType: outcome
  rung: none
  force: should
  level: fheq:6
  appliesTo: "honours graduates of the subject"
  addressee: learner
  verbs: ["understand"]
  about: "health and safety and EDI at work"
  themes: [none]
  domain: generic-skill
  award: ["bachelor's with honours"]
  gradeOf: none
  paraphrase: "Should be able to understand why health and safety, and equality, diversity and inclusion, matter at work."
  quote: full   # the issuer's statement is in `source` (D-std-0014)
  audience: both
  subjects: inherited
- id: qaa/architectural-technology-2022/4.8.b16
  locator: { number: "4.8.b16", headingPath: ["Benchmark standards", "Generic skills for Architectural Technology graduates"] }
  span: { start: 76011, end: 76164 }
  source: "appreciate and engage in contemporary debates relating to sustainability, employability and global perspectives, including decolonisation and anti-racism"
  stem: "4.8"
  statementType: outcome
  rung: none
  force: should
  level: fheq:6
  appliesTo: "honours graduates of the subject"
  addressee: learner
  verbs: ["appreciate", "engage"]
  about: "current debates on sustainability, employability and global perspectives"
  themes: [none]
  domain: generic-skill
  award: ["bachelor's with honours"]
  gradeOf: none
  paraphrase: "Should be able to value and take part in current debates on sustainability, employability and global outlooks, decolonisation and anti-racism included."
  quote: full   # the issuer's statement is in `source` (D-std-0014)
  audience: both
  subjects: inherited
- id: qaa/architectural-technology-2022/4.8.b17
  locator: { number: "4.8.b17", headingPath: ["Benchmark standards", "Generic skills for Architectural Technology graduates"] }
  span: { start: 76167, end: 76260 }
  source: "appreciate the need to act in a sustainable manner and display ethical behaviour and conduct."
  stem: "4.8"
  statementType: outcome
  rung: none
  force: should
  level: fheq:6
  appliesTo: "honours graduates of the subject"
  addressee: learner
  verbs: ["appreciate", "act", "display"]
  about: "acting sustainably and ethically"
  themes: [none]
  domain: generic-skill
  award: ["bachelor's with honours"]
  gradeOf: none
  paraphrase: "Should be able to see the need to act sustainably and to behave and conduct themselves ethically."
  quote: full   # the issuer's statement is in `source` (D-std-0014)
  audience: both
  subjects: inherited
```

### S4a Audience versions
<!-- label: both; status: drafted; basis: primary. forPractitioner: for the programme designer or teacher. forBeneficiary: for the student, second person, naming no issuer. author-agent-written: instructions to an AI agent writing about the statement (a course document, a handbook, an outcome, a report). author-agent-dialogue: instructions to an AI agent using the statement in conversation (with a student, a teacher or a programme team). Written fresh from the held text alone (benchmark rule 6; Abbott, 15:42). -->
```yaml
- statement: qaa/architectural-technology-2022/1.23
  forPractitioner: { text: "Build equality, diversity and inclusion into the curriculum as firmly as health and safety, and give students practice in explaining, accessibly, why inclusive design matters.", rewrite: light, force: should, status: drafted }
  forBeneficiary: { text: "You should come to treat inclusion as seriously as safety in your design work, and be able to explain clearly to anyone why designing for everyone matters.", rewrite: full, force: should, status: drafted }
  author-agent-written: "Present this as a should-level expectation on courses and on professionals, part of the EDI Vision Statement (1.21 to 1.26), for honours and master's study alike. Cite it as (QAA, 2022, Architectural Technology Subject Benchmark Statement, para 1.23). Do not claim that it is a legal duty in itself or that it sets a level of attainment. Set it beside para 4.8 (item 15), para 3.6 (items 12 and 13) and the honours descriptor qaa/fheq-2024/4.15.b8 on communication."
  author-agent-dialogue: "Raise it when a team reviews how inclusion appears in studio briefs or a student asks why inclusive design is assessed. With a student, say it in plain second-person words; with staff, frame it as a curriculum commitment on a par with health and safety. Ask: Where in your project could you show who the building serves and who it might shut out? How would you explain that choice to a client? Avoid presenting it as a box to tick, or reading the Vision Statement out in full."
- statement: qaa/architectural-technology-2022/1.29
  forPractitioner: { text: "Map UNESCO's eight sustainability competencies (systems, futures, critical, strategic, collaborative, integrated problem-solving, self-awareness, normative) onto your module learning outcomes.", rewrite: light, force: should, status: drafted }
  forBeneficiary: { text: "not-applicable: a duty on curriculum design; the student meets its effect in their outcomes", rewrite: full, force: should, status: drafted }
  author-agent-written: "Present this as a should-level duty on curriculum design within the sustainability theme, applying to every course in the subject. Cite it as (QAA, 2022, Architectural Technology Subject Benchmark Statement, para 1.29). Do not claim that students are assessed on the UNESCO list itself, or that the duty is regulatory. Set it beside paras 1.27 and 1.30, the ESD guidance std:doc:qaa-advancehe-esd-2021-guidance, and para 4.8 (items 16 and 17)."
  author-agent-dialogue: "Raise it when a programme team maps sustainability across its modules. With a programme team or teacher, frame it as a design and delivery duty on the course; with a student, mention only the support or practice they can expect from it. Ask: Which of the eight competencies does each core module already develop, and which have no home yet? Avoid handing this duty to a student as something they must achieve, or reading the paragraph aloud."
- statement: qaa/architectural-technology-2022/1.30
  forPractitioner: { text: "Thread sustainability through the whole course rather than one module, and use real case studies that make students judge existing and novel solutions and reflect on their choices.", rewrite: light, force: should, status: drafted }
  forBeneficiary: { text: "not-applicable: a duty on course design and teaching; the student meets it as case-study work", rewrite: full, force: should, status: drafted }
  author-agent-written: "Present this as a should-level expectation on teaching within the sustainability theme, for all courses in the subject. Cite it as (QAA, 2022, Architectural Technology Subject Benchmark Statement, para 1.30). Do not claim that a single sustainability module meets it, or that it is a student outcome. Set it beside paras 1.29, 1.32 and 1.34 and the honours items in para 4.6 (items 5 and 8)."
  author-agent-dialogue: "Raise it when staff plan case studies or ask how sustainability should run through the course. With a programme team or teacher, frame it as a design and delivery duty on the course; with a student, mention only the support or practice they can expect from it. Ask: Where does each year of the course use a real project to test sustainable solutions? Where do students reflect on those choices? Avoid handing this duty to a student as something they must achieve, or reading the paragraph aloud."
- statement: qaa/architectural-technology-2022/1.33
  forPractitioner: { text: "Give students chances to share their learning with peers and beyond the classroom, bring in clients, contractors and suppliers, and consider enquiry-based projects set in real situations.", rewrite: light, force: should, status: drafted }
  forBeneficiary: { text: "not-applicable: a teaching approach the course adopts; not a standard for the student to reach", rewrite: full, force: should, status: drafted }
  author-agent-written: "Present this as a should-level expectation on teaching methods under the sustainability theme, with enquiry-based learning as a may. Cite it as (QAA, 2022, Architectural Technology Subject Benchmark Statement, para 1.33). Do not claim that it requires a particular pedagogy, or that the may-clause is binding. Set it beside paras 1.32 and 1.34 and para 3.9 on studio and problem-based learning."
  author-agent-dialogue: "Raise it when a team designs group or community-facing work. With a programme team or teacher, frame it as a design and delivery duty on the course; with a student, mention only the support or practice they can expect from it. Ask: Where do students meet clients, contractors or suppliers in the course? How do they share what they learn outside the class? Avoid handing this duty to a student as something they must achieve, or reading the paragraph aloud."
- statement: qaa/architectural-technology-2022/1.34
  forPractitioner: { text: "Pair interdisciplinary and independent work, join theory to practical projects with sustainable design aims, and build partnerships with industry so students apply theory in professional settings.", rewrite: light, force: should, status: drafted }
  forBeneficiary: { text: "not-applicable: a duty on curriculum design; the student meets it as projects and industry links", rewrite: full, force: should, status: drafted }
  author-agent-written: "Present this as a should-level duty on curricula under the sustainability theme, with problem-based learning as a may and \"need to\" for the interdisciplinary mix (Part E). Cite it as (QAA, 2022, Architectural Technology Subject Benchmark Statement, para 1.34). Do not claim that partnerships with industry are a condition of the award. Set it beside paras 1.33, 1.39 and 3.9."
  author-agent-dialogue: "Raise it when a team reviews live projects or industry partnerships. With a programme team or teacher, frame it as a design and delivery duty on the course; with a student, mention only the support or practice they can expect from it. Ask: Which projects tie theory to a sustainable design goal? Which employers or firms work with students, and how often? Avoid handing this duty to a student as something they must achieve, or reading the paragraph aloud."
- statement: qaa/architectural-technology-2022/1.40
  forPractitioner: { text: "Consider engaging employers of different sizes and sectors in light-touch ways, such as small working groups meeting online, and use their perspective to give learning commercial realism.", rewrite: light, force: should, status: drafted }
  forBeneficiary: { text: "not-applicable: a duty on the institution in engaging employers", rewrite: full, force: should, status: drafted }
  author-agent-written: "Present this as a should-level matter for the institution to consider, under the enterprise and employment theme. Cite it as (QAA, 2022, Architectural Technology Subject Benchmark Statement, para 1.40). Do not claim that particular modes of employer engagement are required. Set it beside paras 1.39, 2.20 and 2.21."
  author-agent-dialogue: "Raise it when a team plans an employer forum or asks how to involve small firms. With a programme team or teacher, frame it as a design and delivery duty on the course; with a student, mention only the support or practice they can expect from it. Ask: Which sizes and sectors of employer are missing from your current links? What low-effort way could bring them in? Avoid handing this duty to a student as something they must achieve, or reading the paragraph aloud."
- statement: qaa/architectural-technology-2022/2.1
  forPractitioner: { text: "Use the statement as a starting point for shared course design, and build in room for adaptability, specialisms and new competencies so the course keeps pace with industry change.", rewrite: light, force: should, status: drafted }
  forBeneficiary: { text: "not-applicable: a duty on course design", rewrite: full, force: should, status: drafted }
  author-agent-written: "Present this as a should-level expectation on course design, framing the statement as general and dialogic. Cite it as (QAA, 2022, Architectural Technology Subject Benchmark Statement, para 2.1). Do not claim that the statement prescribes content or structure. Set it beside paras 1.4, 1.14, 2.2 and 2.7."
  author-agent-dialogue: "Raise it when a team asks how much the statement constrains its design or how to plan for specialisms. With a programme team or teacher, frame it as a design and delivery duty on the course; with a student, mention only the support or practice they can expect from it. Ask: How does the course let a student start to specialise? What will you change when industry practice shifts? Avoid handing this duty to a student as something they must achieve, or reading the paragraph aloud."
- statement: qaa/architectural-technology-2022/2.5
  forPractitioner: { text: "Students will build knowledge and critical understanding of design, technology and practice at home and abroad; include an international dimension so graduates understand where their profession works globally.", rewrite: light, force: will, status: drafted }
  forBeneficiary: { text: "You will build knowledge and a critical understanding of design, technology and practice, both in the UK and internationally, and learn how your profession works across borders.", rewrite: full, force: will, status: drafted }
  author-agent-written: "Present this as an expected outcome in the issuer's will, for honours and master's students alike, with the international dimension as something important for courses to include. Cite it as (QAA, 2022, Architectural Technology Subject Benchmark Statement, para 2.5). Do not claim that it fixes a level of attainment by itself. Set it beside paras 3.5 and 4.4, para 4.6 (item 1) and para 4.7 (item 1)."
  author-agent-dialogue: "Raise it when a student asks why international examples matter, or a team checks its international content. With a student, put it plainly in the second person; with a programme team, frame it as what the course has to let every graduate show. Ask: Which projects or case studies from outside the UK have you met so far? How do rules and practice differ there? Avoid reading the issuer's wording out at length, or treating this minimum as the mark of a good degree."
- statement: qaa/architectural-technology-2022/2.10
  forPractitioner: { text: "Treat screening for learning differences, specialist support, mentoring, reasonable adjustments, help with external claims and accessible curricula as the minimum support you offer.", rewrite: light, force: should, status: drafted }
  forBeneficiary: { text: "not-applicable: a duty on the institution; the student meets it as support they can ask for", rewrite: full, force: should, status: drafted }
  author-agent-written: "Present this as a should-level duty on the institution, setting the services listed in 2.9 as a floor, under the accessibility theme. Cite it as (QAA, 2022, Architectural Technology Subject Benchmark Statement, para 2.10). Do not claim that the list is exhaustive or that it is a student outcome. Set it beside paras 2.8, 2.9 and 2.12."
  author-agent-dialogue: "Raise it when staff review student support or a student asks what help exists. With a programme team or teacher, frame it as a design and delivery duty on the course; with a student, mention only the support or practice they can expect from it. Ask: Which of these services can your students reach today, and how would a student find them? Avoid handing this duty to a student as something they must achieve, or reading the paragraph aloud."
- statement: qaa/architectural-technology-2022/2.12
  forPractitioner: { text: "Plan adjustments for design presentations as well as for exams: for example, let a student with anxiety start with one-to-one crits and build up to a full audience across the year.", rewrite: light, force: should, status: drafted }
  forBeneficiary: { text: "not-applicable: a duty on assessment design; a student may ask for the adjustment", rewrite: full, force: should, status: drafted }
  author-agent-written: "Present this as a should-level duty on assessment design under the accessibility theme. Cite it as (QAA, 2022, Architectural Technology Subject Benchmark Statement, para 2.12). Do not claim that the example given is the only acceptable adjustment. Set it beside paras 2.11, 2.13 and 3.20."
  author-agent-dialogue: "Raise it when staff design a studio crit or a student worries about presenting work. With a programme team or teacher, frame it as a design and delivery duty on the course; with a student, mention only the support or practice they can expect from it. Ask: How could the presentation be staged so the student builds confidence step by step? Avoid handing this duty to a student as something they must achieve, or reading the paragraph aloud."
- statement: qaa/architectural-technology-2022/2.14
  forPractitioner: { text: "When moving teaching online or blended, check each student's access to equipment, data and bandwidth and use available funds to close the gaps.", rewrite: light, force: should, status: drafted }
  forBeneficiary: { text: "not-applicable: a duty on the institution; the student meets it as support with equipment and data", rewrite: full, force: should, status: drafted }
  author-agent-written: "Present this as a should-level duty on the institution under the accessibility theme. Cite it as (QAA, 2022, Architectural Technology Subject Benchmark Statement, para 2.14). Do not claim that blended delivery is required. Set it beside paras 2.13 and 2.18."
  author-agent-dialogue: "Raise it when a team plans blended delivery or a student lacks equipment. With a programme team or teacher, frame it as a design and delivery duty on the course; with a student, mention only the support or practice they can expect from it. Ask: Which students on the course might lack a suitable device, data or connection, and what fund could help? Avoid handing this duty to a student as something they must achieve, or reading the paragraph aloud."
- statement: qaa/architectural-technology-2022/2.19
  forPractitioner: { text: "Students will complete a design project, a dissertation or both, in which they analyse, evaluate and reflect critically on the risks and ethics of a proposal.", rewrite: light, force: will, status: drafted }
  forBeneficiary: { text: "You will complete a design project, a dissertation or both, in which you analyse and reflect critically on the risks and ethical questions your proposal raises.", rewrite: full, force: will, status: drafted }
  author-agent-written: "Present this as an expected outcome in the issuer's will, for honours and master's courses. Cite it as (QAA, 2022, Architectural Technology Subject Benchmark Statement, para 2.19). Do not claim that both a project and a dissertation are required, or that the form is fixed. Set it beside paras 3.12, 3.17 and 3.22 and para 4.7 (item 5)."
  author-agent-dialogue: "Raise it when a student chooses a final project or asks what it must cover. With a student, put it plainly in the second person; with a programme team, frame it as what the course has to let every graduate show. Ask: What risks and ethical questions does your proposal raise? How will your project show that you weighed them? Avoid reading the issuer's wording out at length, or treating this minimum as the mark of a good degree."
- statement: qaa/architectural-technology-2022/3.5
  forPractitioner: { text: "Students will gain knowledge and critical understanding across all four aspects (design, technology, management, practice), set in UK and international contexts.", rewrite: light, force: will, status: drafted }
  forBeneficiary: { text: "You will build knowledge and a critical understanding of design, technology, management and practice, in the UK and abroad.", rewrite: full, force: will, status: drafted }
  author-agent-written: "Present this as an expected outcome in the issuer's will for all degrees in the subject; it adds management to the three aspects named in 2.5. Cite it as (QAA, 2022, Architectural Technology Subject Benchmark Statement, para 3.5). Do not claim that it sets separate standards beyond those in section 4. Set it beside paras 2.5 and 4.4 and para 4.6 (items 1 to 3)."
  author-agent-dialogue: "Raise it when a student asks what the four aspects of the subject are. With a student, put it plainly in the second person; with a programme team, frame it as what the course has to let every graduate show. Ask: Which of the four aspects do you feel strongest in, and which have you met least? Avoid reading the issuer's wording out at length, or treating this minimum as the mark of a good degree."
- statement: qaa/architectural-technology-2022/3.6.b1
  forPractitioner: { text: "Design the course so students learn to produce economical, sustainable and efficient solutions to complex design and construction problems, carried from concept through to completion.", rewrite: light, force: should, status: drafted }
  forBeneficiary: { text: "Your course should teach you to create cost-effective, sustainable and efficient design solutions to complex building problems, from the first idea to the finished project.", rewrite: full, force: should, status: drafted }
  author-agent-written: "Present this as a course aim with the force should: honours courses are typically designed so that students learn how to do it, at FHEQ Level 6 (FQHEIS Level 10). Cite it as (QAA, 2022, Architectural Technology Subject Benchmark Statement, para 3.6 (item 1)). Do not claim that it is a threshold standard or a condition of the award. Set it beside para 4.6 (items 5 and 8) and the honours descriptor qaa/fheq-2024/4.15.b6."
  author-agent-dialogue: "Raise it when a student plans a whole design from concept to completion. With a student, say it in the second person as something the course should help them learn; with staff, frame it as an aim the design should serve. Ask: How does your scheme balance cost, sustainability and efficiency from concept to handover? Avoid reading the issuer's list aloud, or turning a should into a must."
- statement: qaa/architectural-technology-2022/3.6.b2
  forPractitioner: { text: "Give students practice in innovative design that responds to the climate emergency and reduces carbon and environmental harm.", rewrite: light, force: should, status: drafted }
  forBeneficiary: { text: "Your course should teach you to use new design approaches that respond to the climate emergency and cut carbon emissions.", rewrite: full, force: should, status: drafted }
  author-agent-written: "Present this as a course aim with the force should: honours courses are typically designed so that students learn how to do it, at FHEQ Level 6 (FQHEIS Level 10). Cite it as (QAA, 2022, Architectural Technology Subject Benchmark Statement, para 3.6 (item 2)). Do not claim that it is a threshold standard or a condition of the award. Set it beside para 3.7 (items 1 and 4) and para 4.6 (item 8)."
  author-agent-dialogue: "Raise it when a student asks how design can answer the climate emergency. With a student, say it in the second person as something the course should help them learn; with staff, frame it as an aim the design should serve. Ask: Which design decisions in your project cut carbon most, and how do you know? Avoid reading the issuer's list aloud, or turning a should into a must."
- statement: qaa/architectural-technology-2022/3.6.b3
  forPractitioner: { text: "Develop students' communication across drawing, writing, manual and digital media, and their spoken presentation to public and private audiences.", rewrite: light, force: should, status: drafted }
  forBeneficiary: { text: "Your course should help you communicate well through drawings, writing and digital media, by hand and on screen, and present confidently to any audience.", rewrite: full, force: should, status: drafted }
  author-agent-written: "Present this as a course aim with the force should: honours courses are typically designed so that students learn how to do it, at FHEQ Level 6 (FQHEIS Level 10). Cite it as (QAA, 2022, Architectural Technology Subject Benchmark Statement, para 3.6 (item 3)). Do not claim that it is a threshold standard or a condition of the award. Set it beside para 4.8 (items 9, 10 and 12) and qaa/fheq-2024/4.15.b8."
  author-agent-dialogue: "Raise it when a student works on drawings, reports or a presentation. With a student, say it in the second person as something the course should help them learn; with staff, frame it as an aim the design should serve. Ask: Which forms of communication, drawn, written, digital or spoken, are you least confident in? Avoid reading the issuer's list aloud, or turning a should into a must."
- statement: qaa/architectural-technology-2022/3.6.b4
  forPractitioner: { text: "Teach students to manage the design and construction process using architectural technology and digital tools, on new-build and retrofit work.", rewrite: light, force: should, status: drafted }
  forBeneficiary: { text: "Your course should teach you to manage design and construction using digital tools, both for new buildings and for updating existing ones.", rewrite: full, force: should, status: drafted }
  author-agent-written: "Present this as a course aim with the force should: honours courses are typically designed so that students learn how to do it, at FHEQ Level 6 (FQHEIS Level 10). Cite it as (QAA, 2022, Architectural Technology Subject Benchmark Statement, para 3.6 (item 4)). Do not claim that it is a threshold standard or a condition of the award. Set it beside para 4.6 (items 2 and 9)."
  author-agent-dialogue: "Raise it when a student meets digital design management or retrofit work. With a student, say it in the second person as something the course should help them learn; with staff, frame it as an aim the design should serve. Ask: How would you manage the design process for a retrofit compared with a new building? Avoid reading the issuer's list aloud, or turning a should into a must."
- statement: qaa/architectural-technology-2022/3.6.b5
  forPractitioner: { text: "Help students read and respond to the wider setting of a project (its social, cultural, economic, political, technical and environmental sides), climate change included, from local to global.", rewrite: light, force: should, status: drafted }
  forBeneficiary: { text: "Your course should teach you to respond thoughtfully to the wider context of a project, from local to global, including climate change.", rewrite: full, force: should, status: drafted }
  author-agent-written: "Present this as a course aim with the force should: honours courses are typically designed so that students learn how to do it, at FHEQ Level 6 (FQHEIS Level 10). Cite it as (QAA, 2022, Architectural Technology Subject Benchmark Statement, para 3.6 (item 5)). Do not claim that it is a threshold standard or a condition of the award. Set it beside para 4.6 (item 1) and para 4.7 (item 1)."
  author-agent-dialogue: "Raise it when a student considers the wider context of a site or brief. With a student, say it in the second person as something the course should help them learn; with staff, frame it as an aim the design should serve. Ask: What social, economic or political factors on this site would change your design? Avoid reading the issuer's list aloud, or turning a should into a must."
- statement: qaa/architectural-technology-2022/3.6.b6
  forPractitioner: { text: "Teach a systematic method for producing accurate design information that complies with standards and law and coordinates envelope, interior, structure, fabric and services.", rewrite: light, force: should, status: drafted }
  forBeneficiary: { text: "Your course should teach you to produce accurate design information that meets standards and the law, fitting the outside, inside, structure and services together.", rewrite: full, force: should, status: drafted }
  author-agent-written: "Present this as a course aim with the force should: honours courses are typically designed so that students learn how to do it, at FHEQ Level 6 (FQHEIS Level 10). Cite it as (QAA, 2022, Architectural Technology Subject Benchmark Statement, para 3.6 (item 6)). Do not claim that it is a threshold standard or a condition of the award. Set it beside para 4.6 (items 5 and 7)."
  author-agent-dialogue: "Raise it when a student prepares technical drawings or specifications. With a student, say it in the second person as something the course should help them learn; with staff, frame it as an aim the design should serve. Ask: How do you check that your design information meets the relevant standards and law? Avoid reading the issuer's list aloud, or turning a should into a must."
- statement: qaa/architectural-technology-2022/3.6.b7
  forPractitioner: { text: "Give students strategies for using information management systems to manage a building across its life cycle, for safety and use.", rewrite: light, force: should, status: drafted }
  forBeneficiary: { text: "Your course should teach you to use information systems to manage a building well across its whole life, for safety and everyday use.", rewrite: full, force: should, status: drafted }
  author-agent-written: "Present this as a course aim with the force should: honours courses are typically designed so that students learn how to do it, at FHEQ Level 6 (FQHEIS Level 10). Cite it as (QAA, 2022, Architectural Technology Subject Benchmark Statement, para 3.6 (item 7)). Do not claim that it is a threshold standard or a condition of the award. Set it beside para 4.6 (item 9)."
  author-agent-dialogue: "Raise it when a student meets information management or building operation. With a student, say it in the second person as something the course should help them learn; with staff, frame it as an aim the design should serve. Ask: How could the information you produce help the people who run and maintain the building safely? Avoid reading the issuer's list aloud, or turning a should into a must."
- statement: qaa/architectural-technology-2022/3.6.b8
  forPractitioner: { text: "Prepare students to adopt new concepts, technologies and practices that bear over time on how buildings are produced, how they perform and how they are maintained.", rewrite: light, force: should, status: drafted }
  forBeneficiary: { text: "Your course should help you take up new ideas, technologies and practices that affect how buildings are made, perform and are maintained over time.", rewrite: full, force: should, status: drafted }
  author-agent-written: "Present this as a course aim with the force should: honours courses are typically designed so that students learn how to do it, at FHEQ Level 6 (FQHEIS Level 10). Cite it as (QAA, 2022, Architectural Technology Subject Benchmark Statement, para 3.6 (item 8)). Do not claim that it is a threshold standard or a condition of the award. Set it beside para 4.6 (item 10)."
  author-agent-dialogue: "Raise it when a student asks how to keep up with new technology. With a student, say it in the second person as something the course should help them learn; with staff, frame it as an aim the design should serve. Ask: Which emerging technology or practice could change how your project is built or maintained? Avoid reading the issuer's list aloud, or turning a should into a must."
- statement: qaa/architectural-technology-2022/3.6.b9
  forPractitioner: { text: "Teach building diagnostics and pathology so students can assess existing structures and make proposals that fit them.", rewrite: light, force: should, status: drafted }
  forBeneficiary: { text: "Your course should teach you to diagnose the condition of existing buildings so that your designs suit what is already there.", rewrite: full, force: should, status: drafted }
  author-agent-written: "Present this as a course aim with the force should: honours courses are typically designed so that students learn how to do it, at FHEQ Level 6 (FQHEIS Level 10). Cite it as (QAA, 2022, Architectural Technology Subject Benchmark Statement, para 3.6 (item 9)). Do not claim that it is a threshold standard or a condition of the award. Set it beside para 4.6 (item 4)."
  author-agent-dialogue: "Raise it when a student works on an existing building. With a student, say it in the second person as something the course should help them learn; with staff, frame it as an aim the design should serve. Ask: What did your survey of the existing structure reveal, and how did it shape your proposal? Avoid reading the issuer's list aloud, or turning a should into a must."
- statement: qaa/architectural-technology-2022/3.6.b10
  forPractitioner: { text: "Teach students to embed health and safety, including fire and life safety and the law, from first design principles through occupation and maintenance.", rewrite: light, force: should, status: drafted }
  forBeneficiary: { text: "Your course should teach you to build health and safety, including fire and life safety, into your designs from the start through to how the building is used and maintained.", rewrite: full, force: should, status: drafted }
  author-agent-written: "Present this as a course aim with the force should: honours courses are typically designed so that students learn how to do it, at FHEQ Level 6 (FQHEIS Level 10). Cite it as (QAA, 2022, Architectural Technology Subject Benchmark Statement, para 3.6 (item 10)). Do not claim that it is a threshold standard or a condition of the award. Set it beside para 4.6 (item 7) and paras 1.2 and 4.8 (item 15)."
  author-agent-dialogue: "Raise it when a student considers fire or life safety in a design. With a student, say it in the second person as something the course should help them learn; with staff, frame it as an aim the design should serve. Ask: Where in your design did health and safety thinking start, and what does it mean for the people who maintain it? Avoid reading the issuer's list aloud, or turning a should into a must."
- statement: qaa/architectural-technology-2022/3.6.b11
  forPractitioner: { text: "Develop students' business and management skills: professional and industry standards, clients, procurement and working with other professionals and authorities.", rewrite: light, force: should, status: drafted }
  forBeneficiary: { text: "Your course should help you build business and management skills, from working with clients and other professionals to how projects are procured.", rewrite: full, force: should, status: drafted }
  author-agent-written: "Present this as a course aim with the force should: honours courses are typically designed so that students learn how to do it, at FHEQ Level 6 (FQHEIS Level 10). Cite it as (QAA, 2022, Architectural Technology Subject Benchmark Statement, para 3.6 (item 11)). Do not claim that it is a threshold standard or a condition of the award. Set it beside para 4.6 (item 2)."
  author-agent-dialogue: "Raise it when a student asks about professional practice, clients or procurement. With a student, say it in the second person as something the course should help them learn; with staff, frame it as an aim the design should serve. Ask: How would you manage a client relationship and work with other professionals on this project? Avoid reading the issuer's list aloud, or turning a should into a must."
- statement: qaa/architectural-technology-2022/3.6.b12
  forPractitioner: { text: "Help students adopt and champion equality, diversity and inclusion so that treatment and opportunity are fair.", rewrite: light, force: should, status: drafted }
  forBeneficiary: { text: "Your course should help you champion equality, diversity and inclusion, so that people are treated fairly and get fair chances.", rewrite: full, force: should, status: drafted }
  author-agent-written: "Present this as a course aim with the force should: honours courses are typically designed so that students learn how to do it, at FHEQ Level 6 (FQHEIS Level 10). Cite it as (QAA, 2022, Architectural Technology Subject Benchmark Statement, para 3.6 (item 12)). Do not claim that it is a threshold standard or a condition of the award. Set it beside para 1.23, para 4.8 (item 15) and the EDI Vision Statement (1.21 to 1.26)."
  author-agent-dialogue: "Raise it when inclusion comes up in teamwork or design choices. With a student, say it in the second person as something the course should help them learn; with staff, frame it as an aim the design should serve. Ask: How does your team make sure everyone has a fair chance to contribute? Avoid reading the issuer's list aloud, or turning a should into a must."
- statement: qaa/architectural-technology-2022/3.6.b13
  forPractitioner: { text: "Help students value difference, build welcoming settings for people of every identity, and understand and counter unconscious bias.", rewrite: light, force: should, status: drafted }
  forBeneficiary: { text: "Your course should help you value people's differences, make everyone feel welcome whoever they are, and notice and guard against your own unconscious bias.", rewrite: full, force: should, status: drafted }
  author-agent-written: "Present this as a course aim with the force should: honours courses are typically designed so that students learn how to do it, at FHEQ Level 6 (FQHEIS Level 10). Cite it as (QAA, 2022, Architectural Technology Subject Benchmark Statement, para 3.6 (item 13)). Do not claim that it is a threshold standard or a condition of the award. Set it beside para 3.6 (item 12) and para 4.8 (item 16)."
  author-agent-dialogue: "Raise it when a student works in a diverse group or asks about bias. With a student, say it in the second person as something the course should help them learn; with staff, frame it as an aim the design should serve. Ask: Where might unconscious bias shape who gets heard in your group, and what would you change? Avoid reading the issuer's list aloud, or turning a should into a must."
- statement: qaa/architectural-technology-2022/3.6.b14
  forPractitioner: { text: "Help students conduct themselves ethically, professionally and responsibly, aware of social justice, working collaboratively and communicating effectively.", rewrite: light, force: should, status: drafted }
  forBeneficiary: { text: "Your course should help you act ethically, professionally and responsibly, with an eye to social justice, working well with others and communicating clearly.", rewrite: full, force: should, status: drafted }
  author-agent-written: "Present this as a course aim with the force should: honours courses are typically designed so that students learn how to do it, at FHEQ Level 6 (FQHEIS Level 10). Cite it as (QAA, 2022, Architectural Technology Subject Benchmark Statement, para 3.6 (item 14)). Do not claim that it is a threshold standard or a condition of the award. Set it beside para 4.8 (item 17) and para 1.24."
  author-agent-dialogue: "Raise it when conduct, ethics or social justice arise in project work. With a student, say it in the second person as something the course should help them learn; with staff, frame it as an aim the design should serve. Ask: What ethical choice did your last project involve, and who did it affect? Avoid reading the issuer's list aloud, or turning a should into a must."
- statement: qaa/architectural-technology-2022/3.7.b1
  forPractitioner: { text: "Master's graduates make critically grounded choices on the factors shaping sustainable and inclusive design.", rewrite: light, force: describes, status: drafted }
  forBeneficiary: { text: "At master's level, you can make well-argued choices about what shapes sustainable and inclusive design.", rewrite: full, force: describes, status: drafted }
  author-agent-written: "Present this as an additional subject-specific ability shown at master's level, FHEQ Level 7 (SCQF 11); the text states it without a modal verb (Part E). Cite it as (QAA, 2022, Architectural Technology Subject Benchmark Statement, para 3.7 (item 1)). Do not claim that it applies to honours graduates. Set it beside para 3.6 (item 2), para 4.7 and the master's descriptor qaa/fheq-2024/4.17.b5."
  author-agent-dialogue: "Raise it when a master's student weighs sustainability or inclusion in a design decision. With a master's student, say it plainly in the second person; with staff, frame it as something the master's course has to give students room to show. Ask: What evidence did you weigh before your last sustainable or inclusive design choice? Avoid reading the issuer's wording out at length, or treating this minimum as the mark of a good degree."
- statement: qaa/architectural-technology-2022/3.7.b2
  forPractitioner: { text: "Master's graduates investigate and critically judge design methods for fabric and envelope and trace their effect on health and comfort indoors.", rewrite: light, force: describes, status: drafted }
  forBeneficiary: { text: "At master's level, you can research and critically judge ways of designing a building's fabric and envelope, and show how they affect health and comfort inside.", rewrite: full, force: describes, status: drafted }
  author-agent-written: "Present this as an additional subject-specific ability shown at master's level, FHEQ Level 7 (SCQF 11); the text states it without a modal verb (Part E). Cite it as (QAA, 2022, Architectural Technology Subject Benchmark Statement, para 3.7 (item 2)). Do not claim that it applies to honours graduates. Set it beside para 4.6 (item 4) and qaa/fheq-2024/4.17.b4.2."
  author-agent-dialogue: "Raise it when a master's student studies building fabric, envelope or indoor comfort. With a master's student, say it plainly in the second person; with staff, frame it as something the master's course has to give students room to show. Ask: Which design methods for the envelope have you compared, and what did they show about comfort and health? Avoid reading the issuer's wording out at length, or treating this minimum as the mark of a good degree."
- statement: qaa/architectural-technology-2022/3.7.b3
  forPractitioner: { text: "Master's graduates explain critically the development of more complex technology, construction, materials and services in relation to sustainability, inclusive design and wider community advances.", rewrite: light, force: describes, status: drafted }
  forBeneficiary: { text: "At master's level, you can explain critically how more advanced technology, materials and services develop in relation to sustainability, inclusion and the wider community.", rewrite: full, force: describes, status: drafted }
  author-agent-written: "Present this as an additional subject-specific ability shown at master's level, FHEQ Level 7 (SCQF 11); the text states it without a modal verb (Part E). Cite it as (QAA, 2022, Architectural Technology Subject Benchmark Statement, para 3.7 (item 3)). Do not claim that it applies to honours graduates. Set it beside para 4.7 (item 2) and qaa/fheq-2024/4.17.b1."
  author-agent-dialogue: "Raise it when a master's student explains advanced technology, materials or services. With a master's student, say it plainly in the second person; with staff, frame it as something the master's course has to give students room to show. Ask: How would you argue for a new material or system in a way an expert would accept? Avoid reading the issuer's wording out at length, or treating this minimum as the mark of a good degree."
- statement: qaa/architectural-technology-2022/3.7.b4
  forPractitioner: { text: "Master's graduates understand critically how sustainable design's parts interlock and the constraints on applying its theory at scales from building to district.", rewrite: light, force: describes, status: drafted }
  forBeneficiary: { text: "At master's level, you understand how the parts of sustainable design depend on each other and why theory meets limits in practice at different scales.", rewrite: full, force: describes, status: drafted }
  author-agent-written: "Present this as an additional subject-specific ability shown at master's level, FHEQ Level 7 (SCQF 11); the text states it without a modal verb (Part E). Cite it as (QAA, 2022, Architectural Technology Subject Benchmark Statement, para 3.7 (item 4)). Do not claim that it applies to honours graduates. Set it beside para 3.7 (items 1 and 7) and qaa/fheq-2024/4.17.b5."
  author-agent-dialogue: "Raise it when a master's student meets trade-offs in sustainable design. With a master's student, say it plainly in the second person; with staff, frame it as something the master's course has to give students room to show. Ask: Where did sustainability theory meet a practical constraint in your project, and how did you resolve it? Avoid reading the issuer's wording out at length, or treating this minimum as the mark of a good degree."
- statement: qaa/architectural-technology-2022/3.7.b5
  forPractitioner: { text: "Master's graduates examine critically how the discipline links construction methods, materials and components to climate, nature and resources.", rewrite: light, force: describes, status: drafted }
  forBeneficiary: { text: "At master's level, you can examine critically how building methods and materials relate to the climate, the natural world and its resources.", rewrite: full, force: describes, status: drafted }
  author-agent-written: "Present this as an additional subject-specific ability shown at master's level, FHEQ Level 7 (SCQF 11); the text states it without a modal verb (Part E). Cite it as (QAA, 2022, Architectural Technology Subject Benchmark Statement, para 3.7 (item 5)). Do not claim that it applies to honours graduates. Set it beside para 3.6 (item 2) and qaa/fheq-2024/4.17.b1."
  author-agent-dialogue: "Raise it when a master's student considers climate, resources and the natural world. With a master's student, say it plainly in the second person; with staff, frame it as something the master's course has to give students room to show. Ask: How do your choices of method and material tie back to climate and natural resources? Avoid reading the issuer's wording out at length, or treating this minimum as the mark of a good degree."
- statement: qaa/architectural-technology-2022/3.7.b6
  forPractitioner: { text: "Master's graduates show critical awareness of sustainable design principles and emerging technologies, drawn from a wide range of sources.", rewrite: light, force: describes, status: drafted }
  forBeneficiary: { text: "At master's level, you show critical awareness of sustainable design principles and new technologies, drawing on many sources.", rewrite: full, force: describes, status: drafted }
  author-agent-written: "Present this as an additional subject-specific ability shown at master's level, FHEQ Level 7 (SCQF 11); the text states it without a modal verb (Part E). Cite it as (QAA, 2022, Architectural Technology Subject Benchmark Statement, para 3.7 (item 6)). Do not claim that it applies to honours graduates. Set it beside para 4.7 (item 2) and qaa/fheq-2024/4.17.b1."
  author-agent-dialogue: "Raise it when a master's student reviews emerging sustainable technologies. With a master's student, say it plainly in the second person; with staff, frame it as something the master's course has to give students room to show. Ask: Which sources did you use to judge a new technology, and how far do you trust each? Avoid reading the issuer's wording out at length, or treating this minimum as the mark of a good degree."
- statement: qaa/architectural-technology-2022/3.7.b7
  forPractitioner: { text: "Master's graduates evaluate theories critically and judge the spatial, aesthetic, technical and social qualities of sustainable design in its wider setting.", rewrite: light, force: describes, status: drafted }
  forBeneficiary: { text: "At master's level, you can critically weigh theories and judge how a sustainable design works spatially, visually, technically and socially in its wider setting.", rewrite: full, force: describes, status: drafted }
  author-agent-written: "Present this as an additional subject-specific ability shown at master's level, FHEQ Level 7 (SCQF 11); the text states it without a modal verb (Part E). Cite it as (QAA, 2022, Architectural Technology Subject Benchmark Statement, para 3.7 (item 7)). Do not claim that it applies to honours graduates. Set it beside para 4.7 (item 4) and qaa/fheq-2024/4.17.b4.1."
  author-agent-dialogue: "Raise it when a master's student judges a design or theory at a larger scale. With a master's student, say it plainly in the second person; with staff, frame it as something the master's course has to give students room to show. Ask: How would you judge the spatial, technical and social qualities of a scheme at the scale of its neighbourhood? Avoid reading the issuer's wording out at length, or treating this minimum as the mark of a good degree."
- statement: qaa/architectural-technology-2022/3.7.b8
  forPractitioner: { text: "Master's graduates set research objectives for their problem and critically choose and apply established research techniques to pursue them.", rewrite: light, force: describes, status: drafted }
  forBeneficiary: { text: "At master's level, you can set objectives for a research problem in your field and choose and use established research methods to meet them.", rewrite: full, force: describes, status: drafted }
  author-agent-written: "Present this as an additional subject-specific ability shown at master's level, FHEQ Level 7 (SCQF 11); the text states it without a modal verb (Part E). Cite it as (QAA, 2022, Architectural Technology Subject Benchmark Statement, para 3.7 (item 8)). Do not claim that it applies to honours graduates. Set it beside para 3.17, para 4.7 (item 5) and qaa/fheq-2024/4.17.b2."
  author-agent-dialogue: "Raise it when a master's student plans a dissertation or research project. With a master's student, say it plainly in the second person; with staff, frame it as something the master's course has to give students room to show. Ask: What are your research objectives, and which established method fits them best? Avoid reading the issuer's wording out at length, or treating this minimum as the mark of a good degree."
- statement: qaa/architectural-technology-2022/3.15
  forPractitioner: { text: "Master's students will extend their command of the subject and weigh its professional, ethical and practical questions as they do so.", rewrite: light, force: will, status: drafted }
  forBeneficiary: { text: "At master's level, you will take your subject further while weighing the professional, ethical and practical questions it raises.", rewrite: full, force: will, status: drafted }
  author-agent-written: "Present this as an expected outcome in the issuer's will for master's students, at FHEQ Level 7 (SCQF 11). Cite it as (QAA, 2022, Architectural Technology Subject Benchmark Statement, para 3.15). Do not claim that it applies at honours level. Set it beside paras 3.14 and 3.16, para 4.7 and the master's descriptor qaa/fheq-2024/4.17.b3."
  author-agent-dialogue: "Raise it when a master's student plans their study or a team describes its master's aims. With a student, put it plainly in the second person; with a programme team, frame it as what the course has to let every graduate show. Ask: Which professional or ethical question in your specialism do you want to explore further? Avoid reading the issuer's wording out at length, or treating this minimum as the mark of a good degree."
- statement: qaa/architectural-technology-2022/3.17
  forPractitioner: { text: "Master's students will complete an advanced research or design project with their own questions and method, aiming at original knowledge, and will present it professionally in written, spoken and visual forms.", rewrite: light, force: will, status: drafted }
  forBeneficiary: { text: "At master's level, you will carry out an advanced research or design project with your own questions and methods, aim to add something new to the field, and present it professionally in writing, in person and visually.", rewrite: full, force: will, status: drafted }
  author-agent-written: "Present this as an expected outcome in the issuer's will for master's students, at FHEQ Level 7. Cite it as (QAA, 2022, Architectural Technology Subject Benchmark Statement, para 3.17). Do not claim that every master's project must be research rather than design. Set it beside para 3.22, para 4.7 (item 5), para 3.7 (item 8) and the descriptors qaa/fheq-2024/4.17.b2 and qaa/fheq-2024/4.17.b3."
  author-agent-dialogue: "Raise it when a master's student shapes a research question or plans how to present findings. With a student, put it plainly in the second person; with a programme team, frame it as what the course has to let every graduate show. Ask: What is your question, and what method will answer it? Who outside the course should hear your findings, and in what form? Avoid reading the issuer's wording out at length, or treating this minimum as the mark of a good degree."
- statement: qaa/architectural-technology-2022/3.19
  forPractitioner: { text: "Write an explicit assessment strategy into the course design, tied to the outcomes and the teaching methods, that lets students show progress level by level.", rewrite: light, force: should, status: drafted }
  forBeneficiary: { text: "not-applicable: a duty on course design", rewrite: full, force: should, status: drafted }
  author-agent-written: "Present this as a should-level duty on course design. Cite it as (QAA, 2022, Architectural Technology Subject Benchmark Statement, para 3.19). Do not claim that it prescribes particular assessment types. Set it beside paras 3.18, 3.20 and 3.21."
  author-agent-dialogue: "Raise it when a team prepares for validation or reviews assessment. With a programme team or teacher, frame it as a design and delivery duty on the course; with a student, mention only the support or practice they can expect from it. Ask: Can you show, module by module, which outcome each task assesses and how the demand rises across the years? Avoid handing this duty to a student as something they must achieve, or reading the paragraph aloud."
- statement: qaa/architectural-technology-2022/3.20
  forPractitioner: { text: "Use a varied mix of assessment methods so that, across the course, students from different educational and cultural backgrounds are not shut out.", rewrite: light, force: should, status: drafted }
  forBeneficiary: { text: "not-applicable: a duty on assessment design", rewrite: full, force: should, status: drafted }
  author-agent-written: "Present this as a should-level duty on assessment design, under the accessibility theme; the next sentence (3.20.s2) carries a must. Cite it as (QAA, 2022, Architectural Technology Subject Benchmark Statement, para 3.20). Do not claim that every single task must suit every student. Set it beside paras 2.12, 2.13 and 3.21."
  author-agent-dialogue: "Raise it when a team reviews the balance of its assessment types. With a programme team or teacher, frame it as a design and delivery duty on the course; with a student, mention only the support or practice they can expect from it. Ask: Would a student from a different educational background meet tasks they recognise somewhere in each year? Avoid handing this duty to a student as something they must achieve, or reading the paragraph aloud."
- statement: qaa/architectural-technology-2022/3.20.s2
  forPractitioner: { text: "If an assessment method could disadvantage a student, you must discuss possible adjustments with them, while keeping things fair for the rest of the cohort.", rewrite: light, force: must, status: drafted }
  forBeneficiary: { text: "not-applicable: a duty on the course; the student takes part in the discussion it requires", rewrite: full, force: must, status: drafted }
  author-agent-written: "Present this as a must-level duty on the course under the accessibility theme: adjustments have to be considered, with the student. Cite it as (QAA, 2022, Architectural Technology Subject Benchmark Statement, para 3.20, second sentence). Do not claim that an adjustment must always be granted. Set it beside paras 2.9, 2.12 and 3.20."
  author-agent-dialogue: "Raise it when a student says a task puts them at a disadvantage, or staff handle an adjustment request. With staff, frame it as a must: the conversation with the student has to happen; with a student, say they can expect to be asked what would help. Ask: Has the student been asked what would help? Does the change keep the task fair for the others? Avoid handing this duty to a student as something they must achieve, or reading the paragraph aloud."
- statement: qaa/architectural-technology-2022/3.21
  forPractitioner: { text: "Match the variety of assessment methods to the variety of learning outcomes; the listed methods (design projects, exams, reports, presentations, portfolios and others) show current practice, not a required set.", rewrite: light, force: should, status: drafted }
  forBeneficiary: { text: "not-applicable: a duty on course design", rewrite: full, force: should, status: drafted }
  author-agent-written: "Present this as a should-level duty on course design; its list of methods is indicative only. Cite it as (QAA, 2022, Architectural Technology Subject Benchmark Statement, para 3.21). Do not claim that every listed method must appear in a course. Set it beside paras 3.19, 3.20 and 3.22."
  author-agent-dialogue: "Raise it when a team audits its assessment types. With a programme team or teacher, frame it as a design and delivery duty on the course; with a student, mention only the support or practice they can expect from it. Ask: Which outcomes are assessed only by one kind of task? Which listed methods have you not tried? Avoid handing this duty to a student as something they must achieve, or reading the paragraph aloud."
- statement: qaa/architectural-technology-2022/4.2
  forPractitioner: { text: "When setting marking criteria above the pass, refer to Annex D's descriptions of the four honours classifications rather than to this statement, which stops at threshold.", rewrite: light, force: should, status: drafted }
  forBeneficiary: { text: "not-applicable: a duty on the provider in setting classification criteria", rewrite: full, force: should, status: drafted }
  author-agent-written: "Present this as a should-level duty on the provider for honours degrees, at FHEQ Level 6 (FQHEIS Level 10). Cite it as (QAA, 2022, Architectural Technology Subject Benchmark Statement, para 4.2). Do not claim that the statement itself defines the classes. Set it beside the Annex D bands in std:doc:qaa-fheq-2024-framework (SL6; for example qaa/fheq-2024/annex-d/summary/r1/3rd) and para 4.6."
  author-agent-dialogue: "Raise it when a team writes grade descriptors or asks what a first looks like in the subject. With a programme team or teacher, frame it as a design and delivery duty on the course; with a student, mention only the support or practice they can expect from it. Ask: Which Annex D band does each of your grade descriptors draw on? Where does the subject's own detail enter? Avoid handing this duty to a student as something they must achieve, or reading the paragraph aloud."
- statement: qaa/architectural-technology-2022/4.4
  forPractitioner: { text: "Students will become fluent in the four main aspects of the subject (design, technology, management, practice); the standards are met by showing understanding of these and applying them.", rewrite: light, force: will, status: drafted }
  forBeneficiary: { text: "You will become at home in the four main parts of the subject: design, technology, management and practice.", rewrite: full, force: will, status: drafted }
  author-agent-written: "Present this as an expected outcome in the issuer's will for honours and master's students, the frame for the threshold lists in 4.6 and 4.7. Cite it as (QAA, 2022, Architectural Technology Subject Benchmark Statement, para 4.4). Do not claim that it sets a level beyond threshold. Set it beside paras 2.5, 3.5, 4.6 and 4.7."
  author-agent-dialogue: "Raise it when a student asks what the course is meant to make them good at. With a student, put it plainly in the second person; with a programme team, frame it as what the course has to let every graduate show. Ask: Which of the four, design, technology, management or practice, could you explain best to someone outside the field? Avoid reading the issuer's wording out at length, or treating this minimum as the mark of a good degree."
- statement: qaa/architectural-technology-2022/4.6.b1
  forPractitioner: { text: "At threshold, honours graduates understand the social, economic, environmental, political, legal, ethical and technical forces on the discipline, from local to global.", rewrite: light, force: threshold, status: drafted }
  forBeneficiary: { text: "To reach the threshold for your honours degree, you will show that you understand the social, economic, environmental, political, legal, ethical and technical forces on your field, locally and globally.", rewrite: full, force: threshold, status: drafted }
  author-agent-written: "Present this as a threshold standard: every honours graduate in the subject is expected to have reached it, at FHEQ Level 6 (FQHEIS Level 10, spine:6). Cite it as (QAA, 2022, Architectural Technology Subject Benchmark Statement, para 4.6 (item 1)). Do not claim that it describes a good or typical degree, or that it is a regulatory requirement. Set it beside para 4.7 (item 1), the honours descriptor qaa/fheq-2024/4.15.b1 and the Annex D cell qaa/fheq-2024/annex-d/knowledge/r2/3rd."
  author-agent-dialogue: "Raise it when a student studies context, regulation or policy. With a student, put it plainly in the second person; with a programme team, frame it as what the course has to let every graduate show. Ask: Which social, economic or legal factor most shaped your last project, and at what scale? Avoid reading the issuer's wording out at length, or treating this minimum as the mark of a good degree."
- statement: qaa/architectural-technology-2022/4.6.b2
  forPractitioner: { text: "At threshold, honours graduates know professional conduct and ethics, practice, design leadership and management roles, procurement and contract administration.", rewrite: light, force: threshold, status: drafted }
  forBeneficiary: { text: "To reach the threshold for your honours degree, you will show that you know how to behave professionally and ethically, how practice runs, what design leaders and managers do, and how projects are procured and contracts run.", rewrite: full, force: threshold, status: drafted }
  author-agent-written: "Present this as a threshold standard: every honours graduate in the subject is expected to have reached it, at FHEQ Level 6 (FQHEIS Level 10, spine:6). Cite it as (QAA, 2022, Architectural Technology Subject Benchmark Statement, para 4.6 (item 2)). Do not claim that it describes a good or typical degree, or that it is a regulatory requirement. Set it beside para 3.6 (item 11) and qaa/fheq-2024/4.15.b9.1."
  author-agent-dialogue: "Raise it when a student asks about professional roles, procurement or contracts. With a student, put it plainly in the second person; with a programme team, frame it as what the course has to let every graduate show. Ask: What does a principal designer do, and how does the procurement route change your role? Avoid reading the issuer's wording out at length, or treating this minimum as the mark of a good degree."
- statement: qaa/architectural-technology-2022/4.6.b3
  forPractitioner: { text: "At threshold, honours graduates know construction technologies and how elements, systems, components and materials interact across building types and serve their function.", rewrite: light, force: threshold, status: drafted }
  forBeneficiary: { text: "To reach the threshold for your honours degree, you will show that you understand how building parts, systems and materials fit together in different kinds of building and what each does.", rewrite: full, force: threshold, status: drafted }
  author-agent-written: "Present this as a threshold standard: every honours graduate in the subject is expected to have reached it, at FHEQ Level 6 (FQHEIS Level 10, spine:6). Cite it as (QAA, 2022, Architectural Technology Subject Benchmark Statement, para 4.6 (item 3)). Do not claim that it describes a good or typical degree, or that it is a regulatory requirement. Set it beside para 4.6 (item 4) and qaa/fheq-2024/4.15.b1."
  author-agent-dialogue: "Raise it when a student studies building elements, systems and materials. With a student, put it plainly in the second person; with a programme team, frame it as what the course has to let every graduate show. Ask: How do the elements of the building you are designing work together to serve its function? Avoid reading the issuer's wording out at length, or treating this minimum as the mark of a good degree."
- statement: qaa/architectural-technology-2022/4.6.b4
  forPractitioner: { text: "At threshold, honours graduates understand design principles, the basics of building physics and pathology, and the values behind work on new and existing buildings.", rewrite: light, force: threshold, status: drafted }
  forBeneficiary: { text: "To reach the threshold for your honours degree, you will show that you understand design principles, the basic science of how buildings behave and decay, and what guides work on old and new buildings.", rewrite: full, force: threshold, status: drafted }
  author-agent-written: "Present this as a threshold standard: every honours graduate in the subject is expected to have reached it, at FHEQ Level 6 (FQHEIS Level 10, spine:6). Cite it as (QAA, 2022, Architectural Technology Subject Benchmark Statement, para 4.6 (item 4)). Do not claim that it describes a good or typical degree, or that it is a regulatory requirement. Set it beside para 3.6 (item 9) and qaa/fheq-2024/4.15.b1."
  author-agent-dialogue: "Raise it when a student works on building physics, pathology or an existing building. With a student, put it plainly in the second person; with a programme team, frame it as what the course has to let every graduate show. Ask: Which principles of building physics explain the defect or design choice in front of you? Avoid reading the issuer's wording out at length, or treating this minimum as the mark of a good degree."
- statement: qaa/architectural-technology-2022/4.6.b5
  forPractitioner: { text: "At threshold, honours graduates design holistically and detail from first principles for production, performance and sustainability, meeting regulation, safety and wellbeing.", rewrite: light, force: threshold, status: drafted }
  forBeneficiary: { text: "To reach the threshold for your honours degree, you will show that you can design a building as a whole and work out its details from first principles, so it can be built, performs well and is sustainable, safe and healthy.", rewrite: full, force: threshold, status: drafted }
  author-agent-written: "Present this as a threshold standard: every honours graduate in the subject is expected to have reached it, at FHEQ Level 6 (FQHEIS Level 10, spine:6). Cite it as (QAA, 2022, Architectural Technology Subject Benchmark Statement, para 4.6 (item 5)). Do not claim that it describes a good or typical degree, or that it is a regulatory requirement. Set it beside para 3.6 (items 1, 2 and 6) and qaa/fheq-2024/4.15.b6."
  author-agent-dialogue: "Raise it when a student details a design or asks how far detailing must go. With a student, put it plainly in the second person; with a programme team, frame it as what the course has to let every graduate show. Ask: Can you take one junction in your design from first principles to a buildable detail, and say why it performs? Avoid reading the issuer's wording out at length, or treating this minimum as the mark of a good degree."
- statement: qaa/architectural-technology-2022/4.6.b6
  forPractitioner: { text: "At threshold, honours graduates analyse client, user and stakeholder needs and the setting of a development to define its scope.", rewrite: light, force: threshold, status: drafted }
  forBeneficiary: { text: "To reach the threshold for your honours degree, you will show that you can work out what clients, users and others need, analyse the proposal and its setting, and decide what the project should cover.", rewrite: full, force: threshold, status: drafted }
  author-agent-written: "Present this as a threshold standard: every honours graduate in the subject is expected to have reached it, at FHEQ Level 6 (FQHEIS Level 10, spine:6). Cite it as (QAA, 2022, Architectural Technology Subject Benchmark Statement, para 4.6 (item 6)). Do not claim that it describes a good or typical degree, or that it is a regulatory requirement. Set it beside qaa/fheq-2024/4.15.b7 and the Annex D cell qaa/fheq-2024/annex-d/cognitive/r3/3rd."
  author-agent-dialogue: "Raise it when a student works from a brief or meets a client. With a student, put it plainly in the second person; with a programme team, frame it as what the course has to let every graduate show. Ask: Whose needs does the brief serve, and how did you decide the scope of the project? Avoid reading the issuer's wording out at length, or treating this minimum as the mark of a good degree."
- statement: qaa/architectural-technology-2022/4.6.b7
  forPractitioner: { text: "At threshold, honours graduates apply regulatory health and safety requirements, assessing hazards and risks in design for safety and security across the building life cycle.", rewrite: light, force: threshold, status: drafted }
  forBeneficiary: { text: "To reach the threshold for your honours degree, you will show that you can spot and assess hazards and risks in your designs and keep people safe and secure throughout a building's life, within the law.", rewrite: full, force: threshold, status: drafted }
  author-agent-written: "Present this as a threshold standard: every honours graduate in the subject is expected to have reached it, at FHEQ Level 6 (FQHEIS Level 10, spine:6). Cite it as (QAA, 2022, Architectural Technology Subject Benchmark Statement, para 4.6 (item 7)). Do not claim that it describes a good or typical degree, or that it is a regulatory requirement. Set it beside para 3.6 (item 10) and qaa/fheq-2024/4.15.b9.2."
  author-agent-dialogue: "Raise it when a student considers risk, compliance or fire safety. With a student, put it plainly in the second person; with a programme team, frame it as what the course has to let every graduate show. Ask: Which hazards did you find in your design, and how does your solution manage them over the building's life? Avoid reading the issuer's wording out at length, or treating this minimum as the mark of a good degree."
- statement: qaa/architectural-technology-2022/4.6.b8
  forPractitioner: { text: "At threshold, honours graduates create resilient, sustainable and inclusive solutions, whole and detailed, informed by current knowledge and climate change.", rewrite: light, force: threshold, status: drafted }
  forBeneficiary: { text: "To reach the threshold for your honours degree, you will show that you can create designs that are resilient, sustainable and inclusive, both as a whole and in detail, with climate change in mind.", rewrite: full, force: threshold, status: drafted }
  author-agent-written: "Present this as a threshold standard: every honours graduate in the subject is expected to have reached it, at FHEQ Level 6 (FQHEIS Level 10, spine:6). Cite it as (QAA, 2022, Architectural Technology Subject Benchmark Statement, para 4.6 (item 8)). Do not claim that it describes a good or typical degree, or that it is a regulatory requirement. Set it beside para 3.7 (item 1) and qaa/fheq-2024/4.15.b3.1."
  author-agent-dialogue: "Raise it when a student designs for resilience, sustainability or inclusion. With a student, put it plainly in the second person; with a programme team, frame it as what the course has to let every graduate show. Ask: How does your design hold up as a whole system and in the detail, and for whom? Avoid reading the issuer's wording out at length, or treating this minimum as the mark of a good degree."
- statement: qaa/architectural-technology-2022/4.6.b9
  forPractitioner: { text: "At threshold, honours graduates understand and apply current methods and tools for modelling and managing information in collaboration, for data-driven decisions.", rewrite: light, force: threshold, status: drafted }
  forBeneficiary: { text: "To reach the threshold for your honours degree, you will show that you understand and use current tools for modelling and sharing information in a team, so decisions rest on data.", rewrite: full, force: threshold, status: drafted }
  author-agent-written: "Present this as a threshold standard: every honours graduate in the subject is expected to have reached it, at FHEQ Level 6 (FQHEIS Level 10, spine:6). Cite it as (QAA, 2022, Architectural Technology Subject Benchmark Statement, para 4.6 (item 9)). Do not claim that it describes a good or typical degree, or that it is a regulatory requirement. Set it beside para 3.6 (item 7) and qaa/fheq-2024/4.15.b8."
  author-agent-dialogue: "Raise it when a student uses BIM, modelling or shared information. With a student, put it plainly in the second person; with a programme team, frame it as what the course has to let every graduate show. Ask: How did shared information change a decision in your last team project? Avoid reading the issuer's wording out at length, or treating this minimum as the mark of a good degree."
- statement: qaa/architectural-technology-2022/4.6.b10
  forPractitioner: { text: "At threshold, honours graduates track current and emerging topics, technology, regulation and standards, and use reflection and development planning to stay current and specialise.", rewrite: light, force: threshold, status: drafted }
  forBeneficiary: { text: "To reach the threshold for your honours degree, you will show that you keep up with new topics, technologies, rules and standards by reflecting on your own needs and planning how to develop.", rewrite: full, force: threshold, status: drafted }
  author-agent-written: "Present this as a threshold standard: every honours graduate in the subject is expected to have reached it, at FHEQ Level 6 (FQHEIS Level 10, spine:6). Cite it as (QAA, 2022, Architectural Technology Subject Benchmark Statement, para 4.6 (item 10)). Do not claim that it describes a good or typical degree, or that it is a regulatory requirement. Set it beside para 3.6 (item 8), qaa/fheq-2024/4.15.b5 and the Annex D cell qaa/fheq-2024/annex-d/transferable/r5/3rd."
  author-agent-dialogue: "Raise it when a student plans their development or asks how to stay current. With a student, put it plainly in the second person; with a programme team, frame it as what the course has to let every graduate show. Ask: Which new regulation or technology do you need to learn next, and what is your plan? Avoid reading the issuer's wording out at length, or treating this minimum as the mark of a good degree."
- statement: qaa/architectural-technology-2022/4.7.b1
  forPractitioner: { text: "At threshold, master's graduates show critical awareness of historical and current context and of the theories behind practice.", rewrite: light, force: threshold, status: drafted }
  forBeneficiary: { text: "To reach the threshold for your master's degree, you will show critical awareness of your field's history and present context and of the theories that shape its practice.", rewrite: full, force: threshold, status: drafted }
  author-agent-written: "Present this as a threshold standard for a master's degree in the subject, at FHEQ Level 7 (SCQF 11, spine:7), held on top of the honours list in para 4.6. Cite it as (QAA, 2022, Architectural Technology Subject Benchmark Statement, para 4.7 (item 1)). Do not claim that it describes a merit or distinction, or that it applies to honours graduates. Set it beside para 4.6 (item 1) and the master's descriptor qaa/fheq-2024/4.17.b1."
  author-agent-dialogue: "Raise it when a master's student reads history or theory of the discipline. With a master's student, say it plainly in the second person; with staff, frame it as the least every master's graduate has to show. Ask: Which theory best explains how your area of practice got where it is today? Avoid reading the issuer's wording out at length, or treating this minimum as the mark of a good degree."
- statement: qaa/architectural-technology-2022/4.7.b2
  forPractitioner: { text: "At threshold, master's graduates understand systematically and critically the current and emerging trends in the field, such as digital construction.", rewrite: light, force: threshold, status: drafted }
  forBeneficiary: { text: "To reach the threshold for your master's degree, you will show a systematic, critical understanding of current and emerging trends in your field, such as digital construction.", rewrite: full, force: threshold, status: drafted }
  author-agent-written: "Present this as a threshold standard for a master's degree in the subject, at FHEQ Level 7 (SCQF 11, spine:7), held on top of the honours list in para 4.6. Cite it as (QAA, 2022, Architectural Technology Subject Benchmark Statement, para 4.7 (item 2)). Do not claim that it describes a merit or distinction, or that it applies to honours graduates. Set it beside para 3.7 (item 6) and qaa/fheq-2024/4.17.b1."
  author-agent-dialogue: "Raise it when a master's student explores digital construction or other trends. With a master's student, say it plainly in the second person; with staff, frame it as the least every master's graduate has to show. Ask: Which current trend in the field do you understand best, and what are its limits? Avoid reading the issuer's wording out at length, or treating this minimum as the mark of a good degree."
- statement: qaa/architectural-technology-2022/4.7.b3
  forPractitioner: { text: "At threshold, master's graduates evaluate which methods suit complex problems.", rewrite: light, force: threshold, status: drafted }
  forBeneficiary: { text: "To reach the threshold for your master's degree, you will show that you can weigh up which methods suit complex problems.", rewrite: full, force: threshold, status: drafted }
  author-agent-written: "Present this as a threshold standard for a master's degree in the subject, at FHEQ Level 7 (SCQF 11, spine:7), held on top of the honours list in para 4.6. Cite it as (QAA, 2022, Architectural Technology Subject Benchmark Statement, para 4.7 (item 3)). Do not claim that it describes a merit or distinction, or that it applies to honours graduates. Set it beside qaa/fheq-2024/4.17.b4.2 and qaa/fheq-2024/4.17.b5."
  author-agent-dialogue: "Raise it when a master's student chooses how to tackle a complex problem. With a master's student, say it plainly in the second person; with staff, frame it as the least every master's graduate has to show. Ask: Which methods did you consider for this problem, and why did you reject the others? Avoid reading the issuer's wording out at length, or treating this minimum as the mark of a good degree."
- statement: qaa/architectural-technology-2022/4.7.b4
  forPractitioner: { text: "At threshold, master's graduates analyse complex concepts independently and bring some originality to critical discussion.", rewrite: light, force: threshold, status: drafted }
  forBeneficiary: { text: "To reach the threshold for your master's degree, you will show that you can analyse complex ideas on your own and add something original to critical debate.", rewrite: full, force: threshold, status: drafted }
  author-agent-written: "Present this as a threshold standard for a master's degree in the subject, at FHEQ Level 7 (SCQF 11, spine:7), held on top of the honours list in para 4.6. Cite it as (QAA, 2022, Architectural Technology Subject Benchmark Statement, para 4.7 (item 4)). Do not claim that it describes a merit or distinction, or that it applies to honours graduates. Set it beside qaa/fheq-2024/4.17.b3 and qaa/fheq-2024/4.17.b6."
  author-agent-dialogue: "Raise it when a master's student builds an argument or critique. With a master's student, say it plainly in the second person; with staff, frame it as the least every master's graduate has to show. Ask: Where in your argument did you go beyond the sources to say something of your own? Avoid reading the issuer's wording out at length, or treating this minimum as the mark of a good degree."
- statement: qaa/architectural-technology-2022/4.7.b5
  forPractitioner: { text: "At threshold, master's graduates complete a major design or substantial research project based on thorough disciplinary understanding.", rewrite: light, force: threshold, status: drafted }
  forBeneficiary: { text: "To reach the threshold for your master's degree, you will complete a major design or research project that rests on a thorough understanding of your field.", rewrite: full, force: threshold, status: drafted }
  author-agent-written: "Present this as a threshold standard for a master's degree in the subject, at FHEQ Level 7 (SCQF 11, spine:7), held on top of the honours list in para 4.6. Cite it as (QAA, 2022, Architectural Technology Subject Benchmark Statement, para 4.7 (item 5)). Do not claim that it describes a merit or distinction, or that it applies to honours graduates. Set it beside paras 3.17 and 3.22 and qaa/fheq-2024/4.17.b2."
  author-agent-dialogue: "Raise it when a master's student plans the major project. With a master's student, say it plainly in the second person; with staff, frame it as the least every master's graduate has to show. Ask: What will your major project show about your grasp of the discipline? Avoid reading the issuer's wording out at length, or treating this minimum as the mark of a good degree."
- statement: qaa/architectural-technology-2022/4.8.b1
  forPractitioner: { text: "Honours graduates should be able to complete the tasks they are given as team members.", rewrite: light, force: should, status: drafted }
  forBeneficiary: { text: "By the end of your honours degree, you should be able to carry out your share of the work in a team.", rewrite: full, force: should, status: drafted }
  author-agent-written: "Present this as a generic skill an honours graduate in the subject should have, at FHEQ Level 6 (FQHEIS Level 10, spine:6); the force is should. Cite it as (QAA, 2022, Architectural Technology Subject Benchmark Statement, para 4.8 (item 1)). Do not claim that it is subject-specific, or that it is a must. Set it beside the Annex D cell qaa/fheq-2024/annex-d/transferable/r2/3rd."
  author-agent-dialogue: "Raise it when group work is planned or goes wrong. With a student, put it in plain second-person words; with staff, frame it as a skill the course should build and give chances to show. Ask: What task did you own in your last group project, and did you deliver it? Avoid reading the issuer's list aloud, or turning a should into a must."
- statement: qaa/architectural-technology-2022/4.8.b2
  forPractitioner: { text: "Honours graduates should be able to combine information and material from several sources.", rewrite: light, force: should, status: drafted }
  forBeneficiary: { text: "By the end of your honours degree, you should be able to pull together information and material from different sources.", rewrite: full, force: should, status: drafted }
  author-agent-written: "Present this as a generic skill an honours graduate in the subject should have, at FHEQ Level 6 (FQHEIS Level 10, spine:6); the force is should. Cite it as (QAA, 2022, Architectural Technology Subject Benchmark Statement, para 4.8 (item 2)). Do not claim that it is subject-specific, or that it is a must. Set it beside the Annex D cell qaa/fheq-2024/annex-d/cognitive/r1/3rd."
  author-agent-dialogue: "Raise it when a student researches a topic. With a student, put it in plain second-person words; with staff, frame it as a skill the course should build and give chances to show. Ask: Which sources did you combine, and how did they fit together? Avoid reading the issuer's list aloud, or turning a should into a must."
- statement: qaa/architectural-technology-2022/4.8.b3
  forPractitioner: { text: "Honours graduates should be able to identify problems and frame questions.", rewrite: light, force: should, status: drafted }
  forBeneficiary: { text: "By the end of your honours degree, you should be able to spot problems and work out the right questions to ask.", rewrite: full, force: should, status: drafted }
  author-agent-written: "Present this as a generic skill an honours graduate in the subject should have, at FHEQ Level 6 (FQHEIS Level 10, spine:6); the force is should. Cite it as (QAA, 2022, Architectural Technology Subject Benchmark Statement, para 4.8 (item 3)). Do not claim that it is subject-specific, or that it is a must. Set it beside qaa/fheq-2024/4.15.b7."
  author-agent-dialogue: "Raise it when a student starts a project or brief. With a student, put it in plain second-person words; with staff, frame it as a skill the course should build and give chances to show. Ask: What is the real problem here, and what question would you ask first? Avoid reading the issuer's list aloud, or turning a should into a must."
- statement: qaa/architectural-technology-2022/4.8.b4
  forPractitioner: { text: "Honours graduates should be able to analyse factual information.", rewrite: light, force: should, status: drafted }
  forBeneficiary: { text: "By the end of your honours degree, you should be able to analyse facts and data.", rewrite: full, force: should, status: drafted }
  author-agent-written: "Present this as a generic skill an honours graduate in the subject should have, at FHEQ Level 6 (FQHEIS Level 10, spine:6); the force is should. Cite it as (QAA, 2022, Architectural Technology Subject Benchmark Statement, para 4.8 (item 4)). Do not claim that it is subject-specific, or that it is a must. Set it beside the Annex D cell qaa/fheq-2024/annex-d/cognitive/r1/3rd."
  author-agent-dialogue: "Raise it when a student handles data or facts. With a student, put it in plain second-person words; with staff, frame it as a skill the course should build and give chances to show. Ask: What does this data tell you, and what does it not? Avoid reading the issuer's list aloud, or turning a should into a must."
- statement: qaa/architectural-technology-2022/4.8.b5
  forPractitioner: { text: "Honours graduates should be able to judge the strengths and weaknesses of others' arguments.", rewrite: light, force: should, status: drafted }
  forBeneficiary: { text: "By the end of your honours degree, you should be able to see what is strong and what is weak in other people's arguments.", rewrite: full, force: should, status: drafted }
  author-agent-written: "Present this as a generic skill an honours graduate in the subject should have, at FHEQ Level 6 (FQHEIS Level 10, spine:6); the force is should. Cite it as (QAA, 2022, Architectural Technology Subject Benchmark Statement, para 4.8 (item 5)). Do not claim that it is subject-specific, or that it is a must. Set it beside the Annex D cell qaa/fheq-2024/annex-d/cognitive/r2/3rd."
  author-agent-dialogue: "Raise it when a student reviews others' work or literature. With a student, put it in plain second-person words; with staff, frame it as a skill the course should build and give chances to show. Ask: Where is this author's argument strongest, and where is it weakest? Avoid reading the issuer's list aloud, or turning a should into a must."
- statement: qaa/architectural-technology-2022/4.8.b6
  forPractitioner: { text: "Honours graduates should be able to synthesise the current state of knowledge on a topic.", rewrite: light, force: should, status: drafted }
  forBeneficiary: { text: "By the end of your honours degree, you should be able to sum up and draw together what is known about a topic.", rewrite: full, force: should, status: drafted }
  author-agent-written: "Present this as a generic skill an honours graduate in the subject should have, at FHEQ Level 6 (FQHEIS Level 10, spine:6); the force is should. Cite it as (QAA, 2022, Architectural Technology Subject Benchmark Statement, para 4.8 (item 6)). Do not claim that it is subject-specific, or that it is a must. Set it beside the Annex D cell qaa/fheq-2024/annex-d/knowledge/r3/3rd."
  author-agent-dialogue: "Raise it when a student writes a literature review. With a student, put it in plain second-person words; with staff, frame it as a skill the course should build and give chances to show. Ask: How would you sum up what is known on your topic in a page? Avoid reading the issuer's list aloud, or turning a should into a must."
- statement: qaa/architectural-technology-2022/4.8.b7
  forPractitioner: { text: "Honours graduates should be able to work on tasks independently, with guidance available.", rewrite: light, force: should, status: drafted }
  forBeneficiary: { text: "By the end of your honours degree, you should be able to work on tasks on your own, with guidance when you need it.", rewrite: full, force: should, status: drafted }
  author-agent-written: "Present this as a generic skill an honours graduate in the subject should have, at FHEQ Level 6 (FQHEIS Level 10, spine:6); the force is should. Cite it as (QAA, 2022, Architectural Technology Subject Benchmark Statement, para 4.8 (item 7)). Do not claim that it is subject-specific, or that it is a must. Set it beside the Annex D cell qaa/fheq-2024/annex-d/transferable/r3/3rd."
  author-agent-dialogue: "Raise it when a student works alone between supervisions. With a student, put it in plain second-person words; with staff, frame it as a skill the course should build and give chances to show. Ask: What can you take forward on your own before we next meet? Avoid reading the issuer's list aloud, or turning a should into a must."
- statement: qaa/architectural-technology-2022/4.8.b8
  forPractitioner: { text: "Honours graduates should be able to reflect on their progress and use feedback.", rewrite: light, force: should, status: drafted }
  forBeneficiary: { text: "By the end of your honours degree, you should be able to reflect on how you are progressing and act on the feedback you get.", rewrite: full, force: should, status: drafted }
  author-agent-written: "Present this as a generic skill an honours graduate in the subject should have, at FHEQ Level 6 (FQHEIS Level 10, spine:6); the force is should. Cite it as (QAA, 2022, Architectural Technology Subject Benchmark Statement, para 4.8 (item 8)). Do not claim that it is subject-specific, or that it is a must. Set it beside the Annex D cell qaa/fheq-2024/annex-d/transferable/r5/3rd."
  author-agent-dialogue: "Raise it when a student receives feedback. With a student, put it in plain second-person words; with staff, frame it as a skill the course should build and give chances to show. Ask: What did the last feedback ask you to change, and what did you change? Avoid reading the issuer's list aloud, or turning a should into a must."
- statement: qaa/architectural-technology-2022/4.8.b9
  forPractitioner: { text: "Honours graduates should be able to communicate effectively verbally, non-verbally or both.", rewrite: light, force: should, status: drafted }
  forBeneficiary: { text: "By the end of your honours degree, you should be able to express yourself clearly, in speech and in other ways.", rewrite: full, force: should, status: drafted }
  author-agent-written: "Present this as a generic skill an honours graduate in the subject should have, at FHEQ Level 6 (FQHEIS Level 10, spine:6); the force is should. Cite it as (QAA, 2022, Architectural Technology Subject Benchmark Statement, para 4.8 (item 9)). Do not claim that it is subject-specific, or that it is a must. Set it beside the Annex D cell qaa/fheq-2024/annex-d/transferable/r1/3rd."
  author-agent-dialogue: "Raise it when a student presents or discusses work. With a student, put it in plain second-person words; with staff, frame it as a skill the course should build and give chances to show. Ask: How did your audience react, and what would make your point clearer? Avoid reading the issuer's list aloud, or turning a should into a must."
- statement: qaa/architectural-technology-2022/4.8.b10
  forPractitioner: { text: "Honours graduates should be able to present knowledge or an argument clearly to others.", rewrite: light, force: should, status: drafted }
  forBeneficiary: { text: "By the end of your honours degree, you should be able to present what you know, or an argument, so others can follow it.", rewrite: full, force: should, status: drafted }
  author-agent-written: "Present this as a generic skill an honours graduate in the subject should have, at FHEQ Level 6 (FQHEIS Level 10, spine:6); the force is should. Cite it as (QAA, 2022, Architectural Technology Subject Benchmark Statement, para 4.8 (item 10)). Do not claim that it is subject-specific, or that it is a must. Set it beside qaa/fheq-2024/4.15.b8."
  author-agent-dialogue: "Raise it when a student explains an argument to others. With a student, put it in plain second-person words; with staff, frame it as a skill the course should build and give chances to show. Ask: Could someone outside the field follow your argument? Where might they lose the thread? Avoid reading the issuer's list aloud, or turning a should into a must."
- statement: qaa/architectural-technology-2022/4.8.b11
  forPractitioner: { text: "Honours graduates should be able to gather, analyse, choose and present information with suitable digital systems.", rewrite: light, force: should, status: drafted }
  forBeneficiary: { text: "By the end of your honours degree, you should be able to use the right digital systems to gather, analyse, choose and present information.", rewrite: full, force: should, status: drafted }
  author-agent-written: "Present this as a generic skill an honours graduate in the subject should have, at FHEQ Level 6 (FQHEIS Level 10, spine:6); the force is should. Cite it as (QAA, 2022, Architectural Technology Subject Benchmark Statement, para 4.8 (item 11)). Do not claim that it is subject-specific, or that it is a must. Set it beside the Annex D cell qaa/fheq-2024/annex-d/transferable/r1/3rd and para 4.6 (item 9)."
  author-agent-dialogue: "Raise it when a student handles information digitally. With a student, put it in plain second-person words; with staff, frame it as a skill the course should build and give chances to show. Ask: Which digital tool do you use to organise and present information, and how well? Avoid reading the issuer's list aloud, or turning a should into a must."
- statement: qaa/architectural-technology-2022/4.8.b12
  forPractitioner: { text: "Honours graduates should be able to deliver presentations using visual aids and multimedia.", rewrite: light, force: should, status: drafted }
  forBeneficiary: { text: "By the end of your honours degree, you should be able to give presentations using visuals and multimedia.", rewrite: full, force: should, status: drafted }
  author-agent-written: "Present this as a generic skill an honours graduate in the subject should have, at FHEQ Level 6 (FQHEIS Level 10, spine:6); the force is should. Cite it as (QAA, 2022, Architectural Technology Subject Benchmark Statement, para 4.8 (item 12)). Do not claim that it is subject-specific, or that it is a must. Set it beside the Annex D cell qaa/fheq-2024/annex-d/practical/r4/3rd."
  author-agent-dialogue: "Raise it when a student prepares a presentation. With a student, put it in plain second-person words; with staff, frame it as a skill the course should build and give chances to show. Ask: What visual or media support will make your presentation clearer? Avoid reading the issuer's list aloud, or turning a should into a must."
- statement: qaa/architectural-technology-2022/4.8.b13
  forPractitioner: { text: "Honours graduates should be able to show they understand new ideas or information.", rewrite: light, force: should, status: drafted }
  forBeneficiary: { text: "By the end of your honours degree, you should be able to show that you can grasp new ideas and information.", rewrite: full, force: should, status: drafted }
  author-agent-written: "Present this as a generic skill an honours graduate in the subject should have, at FHEQ Level 6 (FQHEIS Level 10, spine:6); the force is should. Cite it as (QAA, 2022, Architectural Technology Subject Benchmark Statement, para 4.8 (item 13)). Do not claim that it is subject-specific, or that it is a must. Set it beside the Annex D cell qaa/fheq-2024/annex-d/knowledge/r2/3rd."
  author-agent-dialogue: "Raise it when a student meets new ideas or unfamiliar material. With a student, put it in plain second-person words; with staff, frame it as a skill the course should build and give chances to show. Ask: What is the main new idea here, in your own words? Avoid reading the issuer's list aloud, or turning a should into a must."
- statement: qaa/architectural-technology-2022/4.8.b14
  forPractitioner: { text: "Honours graduates should be able to show skill in recognising and describing material.", rewrite: light, force: should, status: drafted }
  forBeneficiary: { text: "By the end of your honours degree, you should be able to show skill in recognising and describing what you are looking at.", rewrite: full, force: should, status: drafted }
  author-agent-written: "Present this as a generic skill an honours graduate in the subject should have, at FHEQ Level 6 (FQHEIS Level 10, spine:6); the force is should. Cite it as (QAA, 2022, Architectural Technology Subject Benchmark Statement, para 4.8 (item 14)). Do not claim that it is subject-specific, or that it is a must. Set it beside the Annex D cell qaa/fheq-2024/annex-d/knowledge/r3/3rd."
  author-agent-dialogue: "Raise it when a student surveys or describes material, a building or a sample. With a student, put it in plain second-person words; with staff, frame it as a skill the course should build and give chances to show. Ask: What do you see here, and how would you describe it precisely? Avoid reading the issuer's list aloud, or turning a should into a must."
- statement: qaa/architectural-technology-2022/4.8.b15
  forPractitioner: { text: "Honours graduates should be able to explain why health and safety, and equality, diversity and inclusion, matter in the workplace.", rewrite: light, force: should, status: drafted }
  forBeneficiary: { text: "By the end of your honours degree, you should be able to understand why health and safety, and equality, diversity and inclusion, matter at work.", rewrite: full, force: should, status: drafted }
  author-agent-written: "Present this as a generic skill an honours graduate in the subject should have, at FHEQ Level 6 (FQHEIS Level 10, spine:6); the force is should. Cite it as (QAA, 2022, Architectural Technology Subject Benchmark Statement, para 4.8 (item 15)). Do not claim that it is subject-specific, or that it is a must. Set it beside para 1.23, para 3.6 (items 10 and 12) and para 4.6 (item 7)."
  author-agent-dialogue: "Raise it when workplace safety or inclusion comes up. With a student, put it in plain second-person words; with staff, frame it as a skill the course should build and give chances to show. Ask: Why do health and safety and inclusion both matter in a design office or on site? Avoid reading the issuer's list aloud, or turning a should into a must."
- statement: qaa/architectural-technology-2022/4.8.b16
  forPractitioner: { text: "Honours graduates should be able to appreciate and join current debates on sustainability, on employability and on global outlooks, decolonisation and anti-racism among them.", rewrite: light, force: should, status: drafted }
  forBeneficiary: { text: "By the end of your honours degree, you should be able to understand and join current debates on sustainability, careers and global perspectives, including decolonisation and anti-racism.", rewrite: full, force: should, status: drafted }
  author-agent-written: "Present this as a generic skill an honours graduate in the subject should have, at FHEQ Level 6 (FQHEIS Level 10, spine:6); the force is should. Cite it as (QAA, 2022, Architectural Technology Subject Benchmark Statement, para 4.8 (item 16)). Do not claim that it is subject-specific, or that it is a must. Set it beside paras 1.29 and 1.36 and para 3.6 (item 13)."
  author-agent-dialogue: "Raise it when current debates on sustainability, careers or decolonisation arise. With a student, put it in plain second-person words; with staff, frame it as a skill the course should build and give chances to show. Ask: Which current debate in the field do you have a view on, and what is it? Avoid reading the issuer's list aloud, or turning a should into a must."
- statement: qaa/architectural-technology-2022/4.8.b17
  forPractitioner: { text: "Honours graduates should be able to appreciate the need for sustainable action and show ethical behaviour.", rewrite: light, force: should, status: drafted }
  forBeneficiary: { text: "By the end of your honours degree, you should be able to see why acting sustainably matters and behave ethically.", rewrite: full, force: should, status: drafted }
  author-agent-written: "Present this as a generic skill an honours graduate in the subject should have, at FHEQ Level 6 (FQHEIS Level 10, spine:6); the force is should. Cite it as (QAA, 2022, Architectural Technology Subject Benchmark Statement, para 4.8 (item 17)). Do not claim that it is subject-specific, or that it is a must. Set it beside para 3.6 (item 14) and paras 1.24 and 1.30."
  author-agent-dialogue: "Raise it when ethics or sustainable behaviour arises. With a student, put it in plain second-person words; with staff, frame it as a skill the course should build and give chances to show. Ask: What would acting sustainably and ethically look like in your next project? Avoid reading the issuer's list aloud, or turning a should into a must."
```

### S5 Levels and alignment
<!-- label: both; status: drafted; basis: primary -->
```yaml
levels:
  - { id: "fheq:6", role: "cites", locator: "D1, 2.15; 4.2" }
  - { id: "fqheis:10", role: "cites", locator: "D1, 2.15; 4.2" }
  - { id: "fheq:7", role: "inferred", locator: "D1, 2.2; 3.7; 4.5; 4.7 (master's degrees; no level named): std:doc:qaa-fheq-2024-framework S5, 4.17" }
  - { id: "fqheis:11", role: "inferred", locator: "D1, as fheq:7: std:doc:qaa-fqheis-2024-framework S5 (shared descriptor 4.17)" }
crosswalks:
  - { from: "fheq:6", to: "fqheis:10", relation: "equivalent", basis: "stated (D1, 2.15: \"FHEQ Level 6; FQHEIS Level 10\"; 4.2)" }
  - { from: "fheq:7", to: "fqheis:11", relation: "equivalent", basis: "inferred: std:doc:qaa-fheq-2024-framework S5 (shared descriptor; Table 1); Part E" }
```

### S6 Themes
<!-- label: both; status: drafted; basis: primary -->
```yaml
- { id: "theme:edi", role: "carries", carriedIn: ["front matter", "1.14", "1.19", "1.20", "1.21", "1.22", "1.23", "1.24", "1.25", "1.26", "2.4", "2.8", "3.3", "3.6", "3.7", "4.6", "4.8"] }
- { id: "theme:accessibility", role: "carries", carriedIn: ["1.19", "2.8", "2.9", "2.10", "2.11", "2.12", "2.13", "2.14", "3.20"] }
- { id: "theme:esd", role: "carries", carriedIn: ["front matter", "1.1", "1.3", "1.11", "1.12", "1.27", "1.28", "1.29", "1.30", "1.31", "1.32", "1.33", "1.34", "3.2", "3.6", "3.7", "4.6", "4.8"] }
- { id: "theme:enterprise", role: "carries", carriedIn: ["front matter", "1.35", "1.36", "1.37", "1.38", "1.39", "1.40", "4.8"] }
```

### S7 Relations
<!-- label: both; status: drafted; basis: primary -->
```yaml
- { rel: "partOf", target: "collection: QAA Subject Benchmark Statements", note: "one of 54 held by stan" }
- { rel: "supersedes", target: "std:doc:qaa-architectural-technology-2019-benchmarks (not held)", note: "the fourth edition, 2019, named in the back matter; earlier editions 2014, 2007 and 2000" }
- { rel: "refersTo", target: "std:doc:qaa-fheq-2024-framework, Annex D", note: "the degree classification descriptions for FHEQ Level 6 and FQHEIS Level 10 degrees, cited in 4.2 for performance above threshold" }
- { rel: "refersTo", target: "std:doc:qaa-fheq-2024-framework", note: "FHEQ Level 6 (2.15; 4.2); exit awards CertHE and DipHE (2.17)" }
- { rel: "refersTo", target: "std:doc:qaa-fqheis-2024-framework", note: "FQHEIS Level 10 (2.15; 4.2); four-year Scottish honours (2.17)" }
- { rel: "cites", target: "std:doc:qaa-advancehe-esd-2021-guidance", note: "1.27: the core skills align with its learning outcomes" }
- { rel: "cites", target: "std:doc:qaa-enterprise-2018-guidance", note: "1.35: its definitions of enterprise and entrepreneurship education" }
- { rel: "refersTo", target: "CIAT accreditation requirements and Standards of Education (not yet ingested)", note: "front matter; 1.20; 1.39; 2.5; 2.25" }
- { rel: "refersTo", target: "QAA Quality Code, Advice and Guidance (not yet ingested)", note: "front matter" }
- { rel: "readWith", target: "QAA Subject Benchmark Statements for Town and Country Planning; Architecture; Landscape Architecture; Engineering; Land, Construction, Real Estate and Surveying", note: "front matter: a suite of built environment subjects; the editions held (std:doc:qaa-town-and-country-planning-2024-benchmarks, std:doc:qaa-architecture-2026-benchmarks, std:doc:qaa-landscape-architecture-2024-benchmarks, std:doc:qaa-engineering-2023-benchmarks, std:doc:qaa-land-construction-real-estate-and-surveying-2024-benchmarks) are later than those current in 2022" }
```

### S8 Currency and review
<!-- label: source; status: drafted; basis: primary -->
```yaml
published: "2022-03"
lastReviewed: "none-stated"
reviewCycle: "none-stated"
consultation: "none-stated; the 2022 advisory group is listed (D1, back matter)"
replacedBy: "none"
```

### S9 Commentary (optional)
<!-- label: editorial; status: drafted; basis: secondary -->
`unknown`: not researched in P1 (Part E).

### SB1 The subject
<!-- label: both; status: drafted; basis: primary -->
- An essential professional design discipline about how buildings are put together and perform (structure, systems, materials, fabric and services), rooted in science and engineering (D1, 1.1, 1.17, 3.1).
- The link between design and construction, optimising production and long-term performance across the building life cycle (D1, 1.11, 1.12, 3.2).
- Four educational components, theoretical, experiential, professional and ethical, tied to design, technology and practice; four main aspects, design, technology, management and practice (D1, 1.17, 2.3, 4.4).
- Shaped now by building and life safety law, the climate emergency, retrofit and data-driven, digital working such as BIM (D1, 1.2, 1.3, 1.6, 1.7, 3.1).
- Vocational and competency based: its standards are threshold only, and a lead PSRB, CIAT, accredits courses and confers the protected title (D1, 1.15, 4.1, front matter).
- Inclusive design at its heart, with a record of widening participation (D1, 1.19, 1.23, 2.4, 3.3).

### SB2 Themes in this subject
<!-- label: both; status: drafted; basis: primary -->
```yaml
- theme: theme:edi
  inThisSubject: "framed by the discipline's own EDI Vision Statement and the Equality Act 2010: wider participation, whole-life care for diverse end-users, inclusive design as a requirement on a par with health and safety; course aims on fairness and unconscious bias, generic skill on EDI at work (D1, 1.19 to 1.26, 3.6, 4.8)"
  statements: ["qaa/architectural-technology-2022/1.23", "qaa/architectural-technology-2022/3.6.b12", "qaa/architectural-technology-2022/3.6.b13", "qaa/architectural-technology-2022/3.7.b1", "qaa/architectural-technology-2022/3.7.b3", "qaa/architectural-technology-2022/4.6.b8", "qaa/architectural-technology-2022/4.8.b15", "qaa/architectural-technology-2022/4.8.b16"]
- theme: theme:accessibility
  inThisSubject: "a provider obligation onsite and online; a floor of support services; adjustments for presentation-led design assessment; digital routes for students short of money for models or of data and equipment (D1, 2.8 to 2.14, 3.20)"
  statements: ["qaa/architectural-technology-2022/2.10", "qaa/architectural-technology-2022/2.12", "qaa/architectural-technology-2022/2.14", "qaa/architectural-technology-2022/3.20", "qaa/architectural-technology-2022/3.20.s2"]
- theme: theme:esd
  inThisSubject: "headed Sustainability: the discipline's key part in a sustainable built environment, the three pillars, UNESCO's eight competencies aligned with outcomes, real cases and problem-based learning; carried into the climate-emergency aims and the sustainable design items at both awards (D1, 1.27 to 1.34, 3.6, 3.7, 4.6, 4.8)"
  statements: ["qaa/architectural-technology-2022/1.29", "qaa/architectural-technology-2022/1.30", "qaa/architectural-technology-2022/1.33", "qaa/architectural-technology-2022/1.34", "qaa/architectural-technology-2022/3.6.b1", "qaa/architectural-technology-2022/3.6.b2", "qaa/architectural-technology-2022/3.7.b1", "qaa/architectural-technology-2022/3.7.b3", "qaa/architectural-technology-2022/3.7.b4", "qaa/architectural-technology-2022/3.7.b5", "qaa/architectural-technology-2022/3.7.b6", "qaa/architectural-technology-2022/3.7.b7", "qaa/architectural-technology-2022/4.6.b5", "qaa/architectural-technology-2022/4.6.b8", "qaa/architectural-technology-2022/4.8.b16", "qaa/architectural-technology-2022/4.8.b17"]
- theme: theme:enterprise
  inThisSubject: "headed Entrepreneurship, enterprise and employment: QAA's 2018 definitions, live and community projects, employer engagement required by CIAT accreditation, apprenticeships and the aspirATion network (D1, 1.35 to 1.40)"
  statements: ["qaa/architectural-technology-2022/1.40", "qaa/architectural-technology-2022/4.8.b16"]
```

### SB3 Content and delivery
<!-- label: both; status: drafted; basis: primary -->
```yaml
areas:
  - { component: "3.1", gloss: "the design function: systems, materials and components for new and existing buildings; BIM across the life cycle" }
  - { component: "3.2", gloss: "performance, comfort, energy, waste and carbon; collaboration and social and ethical awareness" }
  - { component: "3.3", gloss: "inclusive design; health, safety and welfare; the needs of all stakeholders" }
  - { component: "3.4", gloss: "identifying and evaluating requirements, social needs and life safety; new materials and modelling" }
  - { component: "3.5", gloss: "whole-life modelling, procurement and services; design, technology, management and practice" }
  - { component: "3.6", gloss: "fourteen honours aims, from sustainable design and detailing to ethics and EDI" }
  - { component: "3.7", gloss: "eight added master's abilities centred on sustainable and inclusive design and research" }
practices:
  - { component: "2.18", kind: "teaching", gloss: "full-time, sandwich, part-time, online, blended, apprenticeship and distance modes" }
  - { component: "3.8", kind: "teaching", gloss: "case studies, live sites, project simulations, interdisciplinary projects" }
  - { component: "3.9", kind: "teaching", gloss: "studio teaching, team and individual projects, problem-based learning with industry input" }
  - { component: "3.11", kind: "learning", gloss: "simulated real projects, practical sessions, problem-based studio learning" }
  - { component: "3.12", kind: "learning", gloss: "active and reflective learning; a final collaborative interdisciplinary project" }
  - { component: "3.14", kind: "learning", gloss: "master's: critical understanding and learner-centred work joining theory and practice" }
  - { component: "3.16", kind: "learning", gloss: "master's: advanced research, analytical and practical techniques" }
  - { component: "3.18", kind: "assessment", gloss: "a wide range of methods suited to a vocational subject" }
  - { component: "3.19", kind: "assessment", gloss: "an explicit assessment strategy tied to outcomes" }
  - { component: "3.20", kind: "assessment", gloss: "accessible mix, adjustments, practical and portfolio work, formative and peer feedback" }
  - { component: "3.21", kind: "assessment", gloss: "indicative list: long design projects, essays, exams, reports, oral and graphical presentations, other media, online tests, portfolios, placement reports" }
  - { component: "3.22", kind: "assessment", gloss: "master's: the major design or research project as the key assessment" }
```

### SB4 Benchmark standards
<!-- label: both; status: drafted; basis: primary -->
```yaml
rungs:
  - { rung: "threshold", leadIn: "4.6", award: "bachelor's with honours", items: 10 }
  - { rung: "threshold", leadIn: "4.7", award: "master's", items: 5 }
  - { rung: "typical", leadIn: "none", award: "none", items: 0 }
  - { rung: "excellent", leadIn: "none", award: "none", items: 0 }
rungBases: "threshold only (4.1 to 4.3): the standards are the baseline for all honours and master's graduates, apprenticeships included; 4.2 leaves performance above threshold to Annex D; 4.7's master's items are held in addition to 4.6's honours items. Threshold items total 15 (10 honours, 5 master's)."
outcomeLists:
  - { leadIn: "3.6", gloss: "honours course aims: what students should learn how to do", items: 14, award: ["honours"] }
  - { leadIn: "3.7", gloss: "additional subject-specific abilities at master's level", items: 8, award: ["master's"] }
  - { leadIn: "4.8", gloss: "generic skills of honours graduates", items: 17, award: ["honours"] }
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
- { body: "Chartered Institute of Architectural Technologists (CIAT)", says: "the lead PSRB; bases its accreditation of honours and master's courses and its standards of education for Chartered Membership on the statement; alone awards the protected title Chartered Architectural Technologist; accredited graduates are exempt from its Standards of Education; Centre of Excellence status for providers offering both awards; uses inclusivity in assessing student work; requires links with the profession; runs the aspirATion network; accredits courses outside the UK (D1, front matter, 1.18, 1.20, 1.39, 2.5, 2.25)", requirements: "not yet ingested (Part E)" }
```

### SB6 Cross-cutting references
<!-- label: both; status: drafted; basis: primary -->
```yaml
themes:
  - { id: "theme:edi", named: "Equality, diversity and inclusion (EDI); the Architectural Technology EDI Vision Statement", carriedIn: ["front matter", "1.14", "1.19", "1.20", "1.21", "1.22", "1.23", "1.24", "1.25", "1.26", "2.4", "2.8", "3.3", "3.6", "3.7", "4.6", "4.8"], statements: ["1.23", "3.6.b12", "3.6.b13", "3.7.b1", "3.7.b3", "4.6.b8", "4.8.b15", "4.8.b16"] }
  - { id: "theme:accessibility", named: "Accessibility", carriedIn: ["1.19", "2.8", "2.9", "2.10", "2.11", "2.12", "2.13", "2.14", "3.20"], statements: ["2.10", "2.12", "2.14", "3.20", "3.20.s2"] }
  - { id: "theme:esd", named: "Sustainability (front matter: education for sustainable development)", carriedIn: ["front matter", "1.1", "1.3", "1.11", "1.12", "1.27", "1.28", "1.29", "1.30", "1.31", "1.32", "1.33", "1.34", "3.2", "3.6", "3.7", "4.6", "4.8"], statements: ["1.29", "1.30", "1.33", "1.34", "3.6.b1", "3.6.b2", "3.7.b1", "3.7.b3", "3.7.b4", "3.7.b5", "3.7.b6", "3.7.b7", "4.6.b5", "4.6.b8", "4.8.b16", "4.8.b17"] }
  - { id: "theme:enterprise", named: "Entrepreneurship, enterprise and employment (front matter: employability, entrepreneurship and enterprise education)", carriedIn: ["front matter", "1.35", "1.36", "1.37", "1.38", "1.39", "1.40", "4.8"], statements: ["1.40", "4.8.b16"] }
frameworks:
  - { framework: "fheq", levels: ["fheq:6"], citedIn: ["2.15", "4.2"] }
  - { framework: "scqf", levels: ["fqheis:10"], citedIn: ["2.15", "4.2"] }
bodies:
  - { body: "Chartered Institute of Architectural Technologists (CIAT)", citedIn: ["front matter", "1.18", "1.20", "1.39", "2.5", "2.25"] }
  - { body: "Office for Students (its regulatory framework)", citedIn: ["front matter"] }
  - { body: "Advance HE (co-author of the ESD guidance)", citedIn: ["1.27"] }
  - { body: "UNESCO (key competencies for sustainability)", citedIn: ["1.29"] }
sharedDocuments:
  - { document: "std:doc:qaa-fheq-2024-framework, Annex D", named: "Annex D: Outcome classification descriptions for FHEQ Level 6 and FQHEIS Level 10 degrees", citedIn: ["4.2"], role: "descriptions of the four honours classifications, for performance above threshold" }
  - { document: "std:doc:qaa-advancehe-esd-2021-guidance", named: "Education for Sustainable Development Guidance (Advance HE and QAA, March 2021)", citedIn: ["1.27"], role: "the core skills align with its suggested learning outcomes" }
  - { document: "std:doc:qaa-enterprise-2018-guidance", named: "QAA 2018 (Enterprise and Entrepreneurship Education)", citedIn: ["1.35"], role: "definitions of entrepreneurship education and enterprise" }
  - { document: "QAA Quality Code, Advice and Guidance (not yet ingested: listed in Part E)", named: "Advice and Guidance to support the Quality Code", citedIn: ["front matter"], role: "course design, teaching, external expertise, monitoring" }
  - { document: "QAA Glossary (not ingested)", named: "QAA's Glossary", citedIn: ["front matter"], role: "explains unfamiliar terms" }
  - { document: "other QAA Subject Benchmark Statements (S7 readWith)", named: "Town and Country Planning; Architecture; Landscape Architecture; Engineering; and Land, Construction, Real Estate and Surveying", citedIn: ["front matter"], role: "a suite of built environment subjects, read for context and shared curricula" }
  - { document: "Equality Act 2010 (law)", named: "Equality Act 2010", citedIn: ["1.20"], role: "frames the EDI Vision Statement" }
  - { document: "OfS regulatory framework; Quality Assessment Framework for Wales; Quality Enhancement Framework (Scotland)", named: "as named", citedIn: ["front matter"], role: "the statement's regulatory status in each nation" }
```

## Part B Terminology
<!-- The statement has no glossary of its own unless Part E says so; these are terms it defines in its text. -->

### B1 Concepts
<!-- label: both; status: drafted; basis: primary -->
```yaml
- { slug: "architectural-technology", definition: "a professional design discipline about how buildings are put together and perform, grounded in science and engineering and linking design to construction (D1, 1.1, 1.11, 3.1)", beneficiaryDefinition: "the field that works out how a building is put together, made and kept performing well", scopeNote: "independent of, but beside, the other built environment disciplines", category: "unknown", practices: ["education"] }
- { slug: "inclusive-design", definition: "design that puts people at the centre so every user can have the same experience of a building or place whatever their ability, age, gender or faith (D1, 2.4, 3.3)", beneficiaryDefinition: "designing so that everyone can use and enjoy a place equally", scopeNote: "a requirement of education and practice in the EDI Vision Statement (1.23)", category: "unknown", practices: ["education"] }
- { slug: "generalist-and-specialist-masters", definition: "master's degrees differing in balance: generalist ones broader, specialist ones deeper (D1, 2.7)", scopeNote: "both covered by the master's standards (4.5)", category: "unknown", practices: ["education"] }
- { slug: "threshold-standard", definition: "the baseline performance expected of every honours and master's graduate (D1, 4.1, 4.3)", scopeNote: "the only rung the statement states", category: "unknown", practices: ["education"] }
- { slug: "chartered-architectural-technologist", definition: "the protected professional title only CIAT may award (D1, front matter)", scopeNote: "reached after practice experience; accredited degrees exempt holders from CIAT's Standards of Education", category: "unknown", practices: ["education"] }
```

### B2a Terms as the issuer defines them
<!-- label: source; status: drafted; basis: primary -->
```yaml
- { concept: "architectural-technology", form: "architectural technology", lang: "en", partOfSpeech: "noun-phrase", termStatus: "preferred", register: "discipline-specific" }
- { concept: "inclusive-design", form: "inclusive design", lang: "en", partOfSpeech: "noun-phrase", termStatus: "preferred", register: "discipline-specific" }
- { concept: "generalist-and-specialist-masters", form: "'generalist' and 'specialist' master's degrees", lang: "en", partOfSpeech: "noun-phrase", termStatus: "preferred", register: "formal" }
- { concept: "threshold-standard", form: "threshold level of performance", lang: "en", partOfSpeech: "noun-phrase", termStatus: "preferred", register: "formal" }
- { concept: "chartered-architectural-technologist", form: "Chartered Architectural Technologist", lang: "en", partOfSpeech: "noun-phrase", termStatus: "preferred", register: "discipline-specific" }
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
  title: "Subject Benchmark Statement Architectural Technology"
  edition: "March 2022 (fifth edition)"
  year: 2022
  url: unknown (the QAA page; the text came by stan's extraction)
  retrieved: "held from stan: wkspc2615-QAAVector mapped/architectural-technology-2022/architectural-technology-2022.raw.txt, commit 366bcb99a01118f2c4c3ebfa2a8337596bddc455; received 2026-10-03"
  licence: QAA copyright
  tier: primary
  readVia: direct
  held: 00009ae5d76a069d056e2af0a027e326c739e398df4037a948cbb542f96884ab
  heldFiles: ["wkspc2601-library/txt/qaa-2022-architectural-technology-subject-benchmark-statement-standard.txt", "wkspc2601-library/txt/qaa-2022-architectural-technology-subject-benchmark-statement-standard.norm.txt", "wkspc2601-library/records/qaa-2022-architectural-technology-subject-benchmark-statement-standard.chunks.json", "wkspc2601-library/records/qaa-2022-architectural-technology-subject-benchmark-statement-standard.held.json"]
  citedIn: [S1, S2, S3, S4, S4a, S5, S6, S7, SB1, SB2, SB3, SB4, SB5, SB6]
```

### D2 Research log
```yaml
- { ref: D1, tier: primary, consulted: 2026-10-03, pass: P1, outcome: "read whole, direct, from the normalised text; skeleton by tools/std_prep.py, document by tools/bm_build.py" }
- { ref: "ADAPT subj HESA stores, cah.json and hecos.json (designs/ingest/standards/subj/vocab)", tier: primary, consulted: 2026-10-03, pass: P1, outcome: "codes for statedSubjects and subjects" }
```

### D3 Wanted sources
```yaml
- { w: "W-std-0029", citation: "CIAT, Standards of Education and accreditation requirements for honours and master's courses", settles: ["SB5", "S7"], asked: "2026-10-03", state: "wanted" }
```

## Part E Gaps and questions
- Rungs: threshold only, at two awards (4.6 honours, 10 items; 4.7 master's, 5 items, "in addition to" 4.6); no typical or excellent lists; above threshold is left to Annex D (4.2). Like Archaeology, unlike Psychology.
- Rungs: the lead-ins name the rung only in the headings ("(threshold)"); 4.6 uses plain present ("demonstrate"), 4.7 "can demonstrate". Both recorded with force threshold, from the headings and 4.1; "can" is outside the five force words.
- Rungs: 2.15 calls the generic skills "threshold-level", but 4.8's lead-in names no rung ("students should be able to"), so its 17 items are an outcome list with rung none and force should; for P3: move them to the threshold rung?
- gradeOf: none. The two threshold lists are for different awards, and no typical or excellent rung exists, so no outcome can be linked one rung below.
- Force: 3.7's master's list ("to be demonstrated ... are the ability to") has no modal; recorded force describes and listed here; for Abbott: read as will?
- Force: 3.6's course aims ("Courses should typically be designed to allow students to understand how to") taken as statements with force should and addressee both, since each item names what students learn; the ben versions keep should.
- Force, not taken as statements: 1.19 "Providers have a duty", 2.8 "have an obligation", 1.32 "need to ensure", 1.34 "need to involve" (inside a should paragraph that is taken), 1.13 "it is important", 2.15 "it is expected", 3.12 "is expected", 2.9 "an expectation of such institutions" (its items, as the list 2.10 calls basic services). For Abbott: should duty, obligation and expectation read as must or should?
- Force: 3.4 "must also recognise" binds project requirements, not courses or students: read as content (SB3 area), not a statement.
- S4: 3.20 split in two: 3.20 (should, the accessible mix) and 3.20.s2 (must, adjustments considered with the student), since one paragraph carries both modals; the id 3.20.s2 is ours, in the issuer's numbering.
- S4: 2.5 and 3.5 state the same expected outcome; 3.5 adds management. Both kept, each in its own paragraph; 4.4 restates the four aspects.
- S4, predictive "will" not taken: 1.14, 1.30 (second sentence, inside a taken should paragraph), 2.18 (courses "will offer" methods), 2.22, 2.23 and 2.24 (providers and examiners "will" use reference points and reviewers): descriptions of practice, not standards.
- Skeleton: the spans of 3.7.b8, 4.6.b10 and 4.7.b5 ran on into the next heading ("Teaching and learning"; "Benchmark standards for master's degrees (threshold)"; "Generic skills for Architectural Technology graduates"); recut with find. 1.34, 1.40, 2.12, 2.14, 2.19, 3.17 recut to drop trailing headings or to take the obliging sentence.
- S3: headings are run into the paragraph text above them by the extraction (for example "Purposes of an Architectural Technology degree" at the end of 1.10); SUB records them by range. A blank line before 3.13 may hide a lost sub-heading on master's teaching.
- S3: 2.3 repeats 1.17 almost whole and 3.3 repeats 2.4 almost whole: the issuer's repetition.
- Edition: the cover reads March 2022, the colophon "Fifth edition, September 2022". Recorded as March 2022 (the cover); for P3.
- Levels: the statement names FHEQ Level 6 and FQHEIS Level 10 (2.15, 4.2) and no level for master's degrees; fheq:7 and fqheis:11 are inferred from the frameworks (std:doc:qaa-fheq-2024-framework S5, 4.17; shared descriptor), as is the crosswalk fheq:7 to fqheis:11.
- Levels: 2.17 names exit awards (Certificate and Diploma of Higher Education, fheq:4 and fheq:5) and four-year Scottish honours; not levels the statement covers, so not in levelsCovered.
- Subjects: HECoS 100121 architectural technology names the subject; CAH codes follow from it. The master's specialisms of 2.16 are recorded in statedSubjects, with HECoS codes only where the term matches (100120 architectural engineering, 100812 project management); Fire Safety (perhaps 100183 fire safety engineering) and Conservation (perhaps 100585 conservation of buildings) are inferred and left out of the front matter, for P3. HECoS 100584 building technology is a close neighbour, not named.
- SB5: CIAT's own requirements (accreditation, Standards of Education) are not yet ingested (D3).
- SB6: named outside the excluded matter but not bodies of the subject: Office for Students, Advance HE and UNESCO recorded in SB6 bodies; the back matter names the Disabled Students' Commission, the Construction Industry Council, the British Standards Institution, the Institute for Apprenticeships and Technical Education and Skills Development Scotland (excluded matter, not recorded).
- SB6: the front matter names the cross-cutting themes as three ("equality, diversity and inclusion", "education for sustainable development", "employability, entrepreneurship and enterprise education"); accessibility is a section of its own (2.8 to 2.14). Building and life safety runs through the text as a subject theme with no shared theme id: a new id (theme:safety?) is for Abbott.
- S7: the built environment benchmarks it asks to be read with are held only in later editions than those current in 2022.
- Themes on statements: S4 `themes` tags only statements inside a theme's own paragraphs (TH); list items that carry a theme are in SB2 and SB6.
- S9: not researched in P1.
- Pattern against Psychology: threshold only, at two awards, with master's standards in the same document (benchmark open point 1); lead-ins without "will"; a should-list of course aims (3.6); a master's list with no modal (3.7); generic skills as a separate should list (4.8); the subject's own EDI Vision Statement inside section 1.
- ST-12: versions here run to the lengths the content needs; no length range is yet set.

---

## Change notes
- 0.1.2, 3 October 2026, 21:02: moved with its held text from UNI to the source library repo (`wkspc2601-library/ingested/standards/`, texts in `txt/`, records in `records/`); paths only (Abbott, 20:56; std N-0119).
- 0.1.1, 3 October 2026, 20:20: obliging words outside the five read as must, "ought to" as should, on statements outside the rungs, each marked on its force line (Abbott, 20:17; D-std-0016).
- 0.1.0, 2026-10-03 16:15: researched by run frame 0.1.1-draft and standards run layer 0.7.0-draft, std, run 0086 (P1); built by tools/bm_build.py.
