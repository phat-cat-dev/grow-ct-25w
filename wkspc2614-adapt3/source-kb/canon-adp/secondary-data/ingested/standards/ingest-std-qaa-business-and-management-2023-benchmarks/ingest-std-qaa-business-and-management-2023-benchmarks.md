---
id: std:doc:qaa-business-and-management-2023-benchmarks
title: "Subject Benchmark Statement Business and Management"
profile: standards/subject-benchmark
profileVersion: 0.2.0-draft
issuer: QAA
kind: subject-benchmark
jurisdiction: [UK]
subjectScope: subjects
subjects:
  - { scheme: "hecos", code: "100078", label: "business and management", basis: "stated" }
  - { scheme: "cah", code: "CAH17-01-01", label: "business and management (non-specific)", basis: "stated" }
  - { scheme: "cah", code: "CAH17-01", label: "business and management", basis: "stated" }
  - { scheme: "cah", code: "CAH17", label: "business and management", basis: "stated" }
  - { scheme: "hecos", code: "100079", label: "business studies", basis: "inferred" }
  - { scheme: "hecos", code: "100089", label: "management studies", basis: "inferred" }
edition: "March 2023 (fifth edition)"
published: 2023-03
status: current
supersedes: "the fourth edition (2019), named in the membership section (section 6)"
heldText: { method: sha256-bytes, raw: 593f2b9d5e9ea16385308ba792eacfe50224b5a71603966adb80cbf9b22fb2ce, normalised: 624a67b291d1048d154bf3669d4904601d25917b74e3329472f78fc3bead8c15 }
heldTextStan: { method: sha256-stan, raw: 593f2b9d5e9ea16385308ba792eacfe50224b5a71603966adb80cbf9b22fb2ce, normalised: a117ec6593ad4733d6c87b31dc8fdaba338419dc3317a0e842b9c5009376b7d0 }
licence: "QAA copyright; held for study, private to the project, never published"
series: "QAA Subject Benchmark Statements, the 2022 onward revision with cross-cutting themes (fifth edition of this statement)"
awardsCovered: ["bachelor's with honours"]
levelsCovered: ["fheq:6", "fqheis:10"]
nations: ["England", "Wales", "Scotland", "Northern Ireland"]
parts:
  S: full
  B: "partial: no glossary in the document (it points to QAA's Glossary); terms it defines in passing"
  C: "not-applicable: the document sets expectations, not a procedure"
pins: { structure: 0.13.0-draft, template: 0.8.0-draft, benchmarkTemplate: 0.6.0-draft, runFrame: 0.1.1-draft, runLayer: 0.7.0-draft, standards: none yet, terminology: none yet }
lifecycle: drafted
researchedBy: run frame 0.1.1-draft; standards run layer 0.7.0-draft; std, run 0091 (tools/bm_build.py)
passes:
  P1: "2026-10-03 16:33"
  P2: "skipped: read direct from the held text; inferred codes and rung links are for P3"
  P3: open
version: 0.1.2
---

<!-- from INGEST wpk-0016-ingest-pd-template-standards.md 0.8.0-draft and wpk-0016-ingest-pd-template-standards-benchmark.md 0.6.0-draft; built by tools/bm_build.py from run-src/ -->
# Subject Benchmark Statement: Business and Management (QAA, March 2023)

> Run 0091, P1 by std. The issuer's words are held in the source library, `wkspc2601-library/txt/qaa-2023-business-management-subject-benchmark-statement-standard.norm.txt`; each S4 record carries its statement in full (`source`) for language analysis, with its span. Paraphrases and versions are ours. Private to the project, never published. In front matter `status` is the issuer's; ours is `lifecycle`. Doubts are in Part E.

## Part 0 Summary

### 0.1 Agent definition
<!-- label: editorial; status: drafted; basis: primary -->
QAA's UK reference point for what a graduate of a broad, general Business and Management honours degree should know and be able to do, with its standards at three rungs (threshold, typical, excellent) tied to the degree classes. Reach for it when designing, approving, reviewing or describing a general business or management course, its outcomes or its marking. It is not a curriculum, not an accrediting body's standard and not a regulatory requirement in England; function- or sector-specific courses may use it for their broad business content.

### 0.2 Summary
<!-- label: both; status: drafted; basis: primary -->
Published by QAA in March 2023 as the fifth edition, the statement sets out the purposes and characteristics of a Business and Management degree, its distinctive features (design, progression, flexibility, partnership, monitoring and review), its content, skills, teaching, learning and assessment, and benchmark standards for the honours degree at threshold (any honours degree), typical (second class) and excellent (first class) rungs, each in five categories (knowledge and understanding, skills, critical perspective, application, values). It carries four cross-cutting themes (equality, diversity and inclusion; accessibility; education for sustainable development; enterprise and entrepreneurship education), points to Annex D for the degree classes, and names professional, statutory and regulatory bodies in general and sector bodies (CABS, BAM, AACSB, EFMD, PRME) in particular.

## Part S Standard

### S1 Identity
<!-- label: source; status: drafted; basis: primary -->
```yaml
issuer: The Quality Assurance Agency for Higher Education
title: "Subject Benchmark Statement Business and Management"
edition: "March 2023 (fifth edition)"
dates:
  published: 2023-03
  other: []
kind: subject-benchmark
jurisdiction: [UK]
authority: "reference: a sector reference point, not a regulatory requirement (D1, front matter); in England not a sector-recognised standard under the OfS framework; a key reference point in Wales and Scotland; part of quality requirements in Northern Ireland (D1, front matter: Relationship to legislation)"
licence: "QAA copyright; the document gives no re-use terms in its text (D1, front matter)"
copyrightNotice: { text: "© The Quality Assurance Agency for Higher Education 2023", locator: "D1, index" }
```

### S2 Purpose and scope
<!-- label: source; status: drafted; basis: primary -->
```yaml
governs: "what a graduate of a broad, general Business and Management honours degree is expected to know, do and understand, and the standards at threshold, typical and excellent"
appliesTo:
  awards: ["bachelor's with honours", "integrated master's (first-degree elements only)", "degree apprenticeships in business and management"]
  levels: ["fheq:6", "fqheis:10"]
  providers: ["UK higher education providers"]
whoMustUse: "none-stated; it is a reference point, not a requirement (D1, front matter)"
howUsed: ["design", "approval", "review", "other: external examining; PSRBs; information for prospective students and employers"]
doesNot: "it is not a national curriculum and does not prescribe teaching, learning or assessment; it carries no statutory or regulatory requirement (D1, front matter)"
beneficiary: the student
statedScope: "\"The Statement is for Business and Management degree courses which are broad based and general in their scope rather than being oriented towards a particular business function (for example, marketing or finance) or sector (for example, tourism or construction management).\" (D1, 1.2)"
statedSubjects:
  - { name: "Business and Management", locator: "(D1, title; 1.1; 1.2)", kind: "subject", codes: [{ scheme: "hecos", code: "100078", label: "business and management" }, { scheme: "cah", code: "CAH17-01-01", label: "business and management (non-specific)" }] }
  - { name: "Degree Apprenticeships in business and management", locator: "(D1, 1.2)", kind: "programme title", codes: [{ scheme: "hecos", code: "100078", label: "business and management" }] }
  - { name: "marketing (a business function, named as outside the main scope)", locator: "(D1, 1.2)", kind: "specialism", codes: [{ scheme: "hecos", code: "100075", label: "marketing" }] }
  - { name: "tourism (a sector, named as outside the main scope)", locator: "(D1, 1.2)", kind: "specialism", codes: [{ scheme: "hecos", code: "100100", label: "tourism management" }] }
subjects: see front matter (subjectScope subjects)
```

### S3 Structure
<!-- label: both; status: drafted; basis: primary -->
```yaml
components:
  - { number: "1.1", order: 3, componentType: paragraph, parent: "section 1", heading: "Context", gloss: "what the statement sets out: graduate expectations and three rungs" }
  - { number: "1.2", order: 4, componentType: paragraph, parent: "section 1", heading: "Context", gloss: "scope: broad general courses; use by function and sector courses; integrated master's and apprenticeships; allied statements" }
  - { number: "1.3", order: 5, componentType: paragraph, parent: "section 1", heading: "Context", gloss: "a broad frame that keeps innovation and diversity in course design" }
  - { number: "1.4", order: 6, componentType: stem, parent: "section 1", heading: "Purposes", gloss: "the four purposes of a degree in the subject" }
  - { number: "1.5", order: 7, componentType: paragraph, parent: "section 1", heading: "Purposes", gloss: "organisations and business read broadly, every type and size" }
  - { number: "1.6", order: 8, componentType: paragraph, parent: "section 1", heading: "Purposes", gloss: "what responsible leadership takes in" }
  - { number: "1.7", order: 9, componentType: paragraph, parent: "section 1", heading: "Purposes", gloss: "what career preparation means: knowledge, skills, self-awareness, enterprise" }
  - { number: "1.8", order: 10, componentType: paragraph, parent: "section 1", heading: "Purposes", gloss: "skills and attributes as transferable, beyond business careers" }
  - { number: "1.9", order: 11, componentType: paragraph, parent: "section 1", heading: "Purposes", gloss: "courses balance the purposes differently, shown in their outcomes" }
  - { number: "1.10", order: 12, componentType: paragraph, parent: "section 1", heading: "Characteristics", gloss: "breadth, interdisciplinarity and variety of perspective" }
  - { number: "1.11", order: 13, componentType: paragraph, parent: "section 1", heading: "Characteristics", gloss: "theory and practice together" }
  - { number: "1.12", order: 14, componentType: paragraph, parent: "section 1", heading: "Characteristics", gloss: "a changing discipline reflected in course design" }
  - { number: "1.13", order: 15, componentType: paragraph, parent: "section 1", heading: "Characteristics", gloss: "a broad base for careers and further study" }
  - { number: "1.14", order: 16, componentType: paragraph, parent: "section 1", heading: "Characteristics", gloss: "the new theme sections and their reach across the statement" }
  - { number: "1.15", order: 17, componentType: paragraph, parent: "section 1", heading: "Equality, diversity and inclusion", gloss: "EDI defined broadly and built into the subject" }
  - { number: "1.16", order: 18, componentType: paragraph, parent: "section 1", heading: "Equality, diversity and inclusion", gloss: "principles for an inclusive learning community" }
  - { number: "1.17", order: 19, componentType: paragraph, parent: "section 1", heading: "Equality, diversity and inclusion", gloss: "why the subject is taught: EDI and the SDGs" }
  - { number: "1.18", order: 20, componentType: paragraph, parent: "section 1", heading: "Equality, diversity and inclusion", gloss: "what is taught: EDI content, diverse perspectives" }
  - { number: "1.19", order: 21, componentType: paragraph, parent: "section 1", heading: "Equality, diversity and inclusion", gloss: "how the subject is taught: inclusive design and modes of learning" }
  - { number: "1.20", order: 22, componentType: stem, parent: "section 1", heading: "Equality, diversity and inclusion", gloss: "examples of EDI in the learning community" }
  - { number: "1.21", order: 23, componentType: paragraph, parent: "section 1", heading: "Equality, diversity and inclusion", gloss: "EDI as ongoing review with students" }
  - { number: "1.22", order: 24, componentType: stem, parent: "section 1", heading: "Accessibility", gloss: "accessibility across the whole course, with examples" }
  - { number: "1.23", order: 25, componentType: paragraph, parent: "section 1", heading: "Accessibility", gloss: "designing out barriers in advance" }
  - { number: "1.24", order: 26, componentType: paragraph, parent: "section 1", heading: "Accessibility", gloss: "equal access to work-based, international and digital learning" }
  - { number: "1.25", order: 27, componentType: paragraph, parent: "section 1", heading: "Education for Sustainable Development", gloss: "the subject and sustainable development: SDGs, PRME, ERS" }
  - { number: "1.26", order: 28, componentType: stem, parent: "section 1", heading: "Education for Sustainable Development", gloss: "sustainable management as a curriculum duty, with example topics" }
  - { number: "1.27", order: 29, componentType: paragraph, parent: "section 1", heading: "Education for Sustainable Development", gloss: "ERS taught in dedicated spaces and throughout" }
  - { number: "1.28", order: 30, componentType: paragraph, parent: "section 1", heading: "Education for Sustainable Development", gloss: "core skills match the ESD guidance competencies" }
  - { number: "1.29", order: 31, componentType: paragraph, parent: "section 1", heading: "Enterprise and entrepreneurship education", gloss: "enterprise and entrepreneurship education defined" }
  - { number: "1.30", order: 32, componentType: paragraph, parent: "section 1", heading: "Enterprise and entrepreneurship education", gloss: "entrepreneurial capacity and mindset" }
  - { number: "1.31", order: 33, componentType: paragraph, parent: "section 1", heading: "Enterprise and entrepreneurship education", gloss: "enterprise theory and practice across sectors" }
  - { number: "1.32", order: 34, componentType: paragraph, parent: "section 1", heading: "Enterprise and entrepreneurship education", gloss: "experiential learning for ventures and innovation" }
  - { number: "1.33", order: 35, componentType: paragraph, parent: "section 1", heading: "Enterprise and entrepreneurship education", gloss: "enterprise for a self-directed working life" }
  - { number: "2.1", order: 37, componentType: paragraph, parent: "section 2", heading: "Design", gloss: "interdisciplinary and adaptable course design" }
  - { number: "2.2", order: 38, componentType: paragraph, parent: "section 2", heading: "Design", gloss: "knowledge joined with skills; vocational to theoretical" }
  - { number: "2.3", order: 39, componentType: paragraph, parent: "section 2", heading: "Design", gloss: "employability and a responsible professional mindset" }
  - { number: "2.4", order: 40, componentType: paragraph, parent: "section 2", heading: "Design", gloss: "responsible management practice built into courses" }
  - { number: "2.5", order: 41, componentType: paragraph, parent: "section 2", heading: "Design", gloss: "every kind of organisation covered" }
  - { number: "2.6", order: 42, componentType: paragraph, parent: "section 2", heading: "Design", gloss: "preparing for changing working life" }
  - { number: "2.7", order: 43, componentType: paragraph, parent: "section 2", heading: "Progression", gloss: "progression through the levels to threshold and beyond" }
  - { number: "2.8", order: 44, componentType: paragraph, parent: "section 2", heading: "Progression", gloss: "joint and combined routes" }
  - { number: "2.9", order: 45, componentType: paragraph, parent: "section 2", heading: "Progression", gloss: "course length, placements and exit awards" }
  - { number: "2.10", order: 46, componentType: paragraph, parent: "section 2", heading: "Progression", gloss: "integrated master's degrees in the subject" }
  - { number: "2.11", order: 47, componentType: paragraph, parent: "section 2", heading: "Flexibility", gloss: "flexible approaches for access and inclusion" }
  - { number: "2.12", order: 48, componentType: stem, parent: "section 2", heading: "Flexibility", gloss: "forms flexibility may take" }
  - { number: "2.13", order: 49, componentType: paragraph, parent: "section 2", heading: "Flexibility", gloss: "coherence kept in flexible routes" }
  - { number: "2.14", order: 50, componentType: stem, parent: "section 2", heading: "Partnership", gloss: "partnerships with organisations" }
  - { number: "2.15", order: 51, componentType: paragraph, parent: "section 2", heading: "Partnership", gloss: "recognition by professional bodies" }
  - { number: "2.16", order: 52, componentType: stem, parent: "section 2", heading: "Partnership", gloss: "networks and sector bodies" }
  - { number: "2.17", order: 53, componentType: paragraph, parent: "section 2", heading: "Monitoring and review", gloss: "monitoring and periodic review" }
  - { number: "2.18", order: 54, componentType: paragraph, parent: "section 2", heading: "Monitoring and review", gloss: "external reviewers in periodic review" }
  - { number: "2.19", order: 55, componentType: paragraph, parent: "section 2", heading: "Monitoring and review", gloss: "external examiners and threshold standards" }
  - { number: "2.20", order: 56, componentType: paragraph, parent: "section 2", heading: "Monitoring and review", gloss: "advisory boards and employer panels" }
  - { number: "2.21", order: 57, componentType: paragraph, parent: "section 2", heading: "Monitoring and review", gloss: "accreditation of professional and vocational courses" }
  - { number: "3.1", order: 59, componentType: paragraph, parent: "section 3", heading: "Content: knowledge and understanding", gloss: "broad, analytical, integrated study of business" }
  - { number: "3.2", order: 60, componentType: paragraph, parent: "section 3", heading: "Content: knowledge and understanding", gloss: "knowledge of organisations, environment and governance" }
  - { number: "3.3", order: 61, componentType: paragraph, parent: "section 3", heading: "Content: knowledge and understanding", gloss: "integration across areas of understanding" }
  - { number: "3.4", order: 62, componentType: area, parent: "section 3", heading: "Content: knowledge and understanding", gloss: "area: the business environment" }
  - { number: "3.5", order: 63, componentType: area, parent: "section 3", heading: "Content: knowledge and understanding", gloss: "area: organisations" }
  - { number: "3.6", order: 64, componentType: area, parent: "section 3", heading: "Content: knowledge and understanding", gloss: "area: responsible leadership and management" }
  - { number: "3.7", order: 65, componentType: stem, parent: "section 3", heading: "Content: knowledge and understanding", gloss: "ten areas of knowledge, understanding and critical evaluation" }
  - { number: "3.8", order: 66, componentType: paragraph, parent: "section 3", heading: "Skills and practice", gloss: "practice-related courses link skills to employability" }
  - { number: "3.9", order: 67, componentType: paragraph, parent: "section 3", heading: "Skills and practice", gloss: "cognitive, intellectual, personal and interpersonal skills" }
  - { number: "3.10", order: 68, componentType: stem, parent: "section 3", heading: "Skills and practice", gloss: "eight skills of particular relevance to the subject" }
  - { number: "3.11", order: 69, componentType: stem, parent: "section 3", heading: "Skills and practice", gloss: "seven other generic skills and attributes" }
  - { number: "3.12", order: 70, componentType: paragraph, parent: "section 3", heading: "Skills and practice", gloss: "national and international contexts" }
  - { number: "3.13", order: 71, componentType: paragraph, parent: "section 3", heading: "Skills and practice", gloss: "languages and cultural awareness before going abroad" }
  - { number: "3.14", order: 72, componentType: paragraph, parent: "section 3", heading: "Teaching and learning", gloss: "varied qualifications; emphasis shown in outcomes" }
  - { number: "3.15", order: 73, componentType: practice, parent: "section 3", heading: "Teaching and learning", gloss: "theory and practice joined; inputs from practitioners" }
  - { number: "3.16", order: 74, componentType: stem, parent: "section 3", heading: "Teaching and learning", gloss: "inclusive methods, modes and typical learning activities" }
  - { number: "3.17", order: 75, componentType: practice, parent: "section 3", heading: "Teaching and learning", gloss: "defined skills development and assessment" }
  - { number: "3.18", order: 76, componentType: practice, parent: "section 3", heading: "Assessment", gloss: "assessment for learning and timely feedback" }
  - { number: "3.19", order: 77, componentType: practice, parent: "section 3", heading: "Assessment", gloss: "inclusive assessment design" }
  - { number: "3.20", order: 78, componentType: stem, parent: "section 3", heading: "Assessment", gloss: "reliable, inclusive, varied assessment methods" }
  - { number: "3.21", order: 79, componentType: practice, parent: "section 3", heading: "Assessment", gloss: "online and in-person assessment" }
  - { number: "3.22", order: 80, componentType: practice, parent: "section 3", heading: "Assessment", gloss: "authentic assessment" }
  - { number: "3.23", order: 81, componentType: practice, parent: "section 3", heading: "Assessment", gloss: "group assessment and its weighting" }
  - { number: "3.24", order: 82, componentType: practice, parent: "section 3", heading: "Assessment", gloss: "peer review and assessment" }
  - { number: "3.25", order: 83, componentType: practice, parent: "section 3", heading: "Assessment", gloss: "transparent assessment and shared criteria" }
  - { number: "3.26", order: 84, componentType: practice, parent: "section 3", heading: "Assessment", gloss: "assessment and student workload" }
  - { number: "4.1", order: 86, componentType: paragraph, parent: "section 4", heading: "Introduction", gloss: "what the standards are and where content sits" }
  - { number: "4.2", order: 87, componentType: paragraph, parent: "section 4", heading: "Introduction", gloss: "most go beyond threshold; Annex D for classes" }
  - { number: "4.3", order: 88, componentType: paragraph, parent: "section 4", heading: "Introduction", gloss: "three categories; threshold as minimum, typical as the norm" }
  - { number: "4.4", order: 89, componentType: stem, parent: "section 4", heading: "Introduction", gloss: "five bases that separate the categories" }
  - { number: "4.5", order: 90, componentType: stem, parent: "section 4", heading: "Threshold level", gloss: "threshold rung, honours degree" }
  - { number: "4.6", order: 91, componentType: stem, parent: "section 4", heading: "Typical level", gloss: "typical rung, second class honours" }
  - { number: "4.7", order: 92, componentType: stem, parent: "section 4", heading: "Excellent level", gloss: "excellent rung, first class honours" }
  - { number: "1", componentType: section, parent: none, heading: "Context and purposes of a Business and Management degree", gloss: "section 1" }
  - { number: "2", componentType: section, parent: none, heading: "Distinctive features of a Business and Management degree", gloss: "section 2" }
  - { number: "3", componentType: section, parent: none, heading: "Content, structure and delivery", gloss: "section 3" }
  - { number: "4", componentType: section, parent: none, heading: "Benchmark standards", gloss: "section 4" }
excluded:
  - { number: "none", heading: "About this Statement; How can I use this document?; Relationship to legislation; Additional sector reference points", kind: "other: front matter, read for S1, S2 and SB6" }
  - { number: "none", heading: "section headings (1 to 4)", kind: "other: heading lines" }
  - { number: "5", heading: "List of references and further resources", kind: "other: references, read for S7 and SB6" }
  - { number: "6", heading: "Membership of the Advisory Groups for the Subject Benchmark Statement for Business and Management", kind: "other: membership, read for S7 (earlier editions)" }
```

### S4 Statements
<!-- label: both; status: drafted; basis: primary. Only standards (D-std-0002 (a)): 67 records. `source` is the issuer's statement exactly as its span holds it (D-std-0014). -->
```yaml
- id: qaa/business-and-management-2023/1.3
  locator: { number: "1.3", headingPath: ["Context and purposes of a Business and Management degree", "Context"] }
  span: { start: 9878, end: 10682 }
  source: "1.3 The Statement provides a broad framework within which higher education providers can develop and deliver relevant and challenging Business and Management courses that respond to the needs of students and employers and reflect current knowledge and good practice. It is not intended to be so prescriptive that it constrains innovation in course design and delivery. Innovation, adaptability and diversity are hallmarks of Business and Management courses, and this facet should be maintained (see paragraph 2.2). The Statement will be of assistance to providers in the design of high-quality Business and Management courses, to ensure that the standard of such degrees is maintained and the quality of their graduates enhanced. Purposes and characteristics of a Business and Management degree Purposes\n"
  stem: none
  statementType: expectation
  rung: none
  force: should
  level: none
  appliesTo: "courses in the subject"
  addressee: provider
  verbs: ["maintained", "develop", "deliver"]
  about: "keeping innovation and variety in course design"
  themes: [none]
  domain: none
  award: ["bachelor's with honours"]
  gradeOf: none
  paraphrase: "The statement is a broad, non-prescriptive frame for building and running courses; innovation, adaptability and variety mark the subject's courses, and that quality should be kept."
  quote: full   # the issuer's statement is in `source` (D-std-0014)
  audience: practitioner
  subjects: inherited
- id: qaa/business-and-management-2023/1.8
  locator: { number: "1.8", headingPath: ["Context and purposes of a Business and Management degree", "Purposes"] }
  span: { start: 12626, end: 13349 }
  source: "1.8 Not every graduate will engage subsequently in a business and management career, nor will have entered directly from secondary education. Therefore, 'skills and attributes' should be understood to include the development and enhancement of a range of transferable academic and professional skills, which, while being highly appropriate to a career in business and management, are not restricted to this. The skills will also equip students to become effective, impactful and responsible employees, work colleagues, leaders and global citizens. Courses are likely to incorporate continued reflection and self- awareness, acknowledgement of the value of lifelong learning and appreciation of others and their well-being.\n"
  stem: none
  statementType: expectation
  rung: none
  force: will
  level: fheq:6
  appliesTo: "graduates of the subject"
  addressee: learner
  verbs: ["equip"]
  about: "transferable skills for any career"
  themes: [none]
  domain: generic-skill
  award: ["bachelor's with honours"]
  gradeOf: none
  paraphrase: "Skills and attributes here mean transferable academic and professional skills, suited to business careers but not confined to them; these skills will also prepare students to work well and responsibly as employees, colleagues, leaders and citizens of the world."
  quote: full   # the issuer's statement is in `source` (D-std-0014)
  audience: both
  subjects: inherited
- id: qaa/business-and-management-2023/1.9
  locator: { number: "1.9", headingPath: ["Context and purposes of a Business and Management degree", "Purposes"] }
  span: { start: 13349, end: 13744 }
  source: "1.9 While general degree courses in Business and Management cover these purposes, the actual balance will vary among individual higher education providers and courses, and may also reflect the requirements for recognition by professional bodies. The balance being delivered should be explicable and demonstrable in terms of the specified learning outcomes of particular courses. Characteristics\n"
  stem: none
  statementType: expectation
  rung: none
  force: should
  level: none
  appliesTo: "each course in the subject"
  addressee: provider
  verbs: ["vary", "reflect"]
  about: "the balance of purposes, shown in learning outcomes"
  themes: [none]
  domain: none
  award: ["bachelor's with honours"]
  gradeOf: none
  paraphrase: "Courses cover the purposes in differing balance, which may follow what professional bodies ask for recognition; whatever balance a course strikes should be explainable and shown through its stated learning outcomes."
  quote: full   # the issuer's statement is in `source` (D-std-0014)
  audience: practitioner
  subjects: inherited
- id: qaa/business-and-management-2023/1.10
  locator: { number: "1.10", headingPath: ["Context and purposes of a Business and Management degree", "Characteristics"] }
  span: { start: 13744, end: 14047 }
  source: "1.10 Business and Management degree courses are characterised by their diversity in terms of content, interdisciplinarity and range of perspectives. They are broad in scope and should give an insight into a wide range of business areas. This knowledge and understanding can be applied to many contexts.\n"
  stem: none
  statementType: expectation
  rung: none
  force: should
  level: none
  appliesTo: "courses in the subject"
  addressee: both
  verbs: ["give", "applied"]
  about: "broad insight across business areas"
  themes: [none]
  domain: none
  award: ["bachelor's with honours"]
  gradeOf: none
  paraphrase: "The subject's courses are marked by variety of content, interdisciplinarity and range of view; they are broad and should give insight into many areas of business, knowledge that carries into many settings."
  quote: full   # the issuer's statement is in `source` (D-std-0014)
  audience: both
  subjects: inherited
- id: qaa/business-and-management-2023/1.13
  locator: { number: "1.13", headingPath: ["Context and purposes of a Business and Management degree", "Characteristics"] }
  span: { start: 14587, end: 14869 }
  source: "1.13 Business and Management degree courses provide a broad foundation on which students will be prepared for a range of future careers and roles in a wide range of organisations. They may also provide a starting point for further postgraduate study in a wide range of specialisms.\n"
  stem: none
  statementType: expectation
  rung: none
  force: will
  level: fheq:6
  appliesTo: "students of the subject"
  addressee: learner
  verbs: ["prepared", "provide"]
  about: "a broad base for careers and further study"
  themes: [none]
  domain: none
  award: ["bachelor's with honours"]
  gradeOf: none
  paraphrase: "The subject's courses lay a broad base from which students will be ready for many future careers and roles across organisations of every kind, and may lead on to postgraduate study in many specialisms."
  quote: full   # the issuer's statement is in `source` (D-std-0014)
  audience: both
  subjects: inherited
- id: qaa/business-and-management-2023/1.15
  locator: { number: "1.15", headingPath: ["Context and purposes of a Business and Management degree", "Equality, diversity and inclusion"] }
  span: { start: 15254, end: 15814 }
  source: "1.15 Equality, diversity and inclusion (EDI) encompass a wide range of identity characteristics, including, but not limited to, race/ethnicity, gender, sexual orientation, religion and belief, disability, age, and socio-economic background. It is recognised that there are many forms of difference and that these are, in part, reflected in legal equality duties but go beyond that to recognise intersectionalities across the student and staff population. EDI should be a meaningful concept that is embedded within the culture and practice of the subject area.\n"
  stem: none
  statementType: expectation
  rung: none
  force: should
  level: none
  appliesTo: "the subject area and its courses"
  addressee: provider
  verbs: ["embedded", "recognise"]
  about: "EDI built into the culture and practice of the subject"
  themes: [theme:edi]
  domain: none
  award: ["bachelor's with honours"]
  gradeOf: none
  paraphrase: "EDI covers many identity characteristics and kinds of difference, reaching past legal duties to intersections across students and staff; it should be a real concept built into the subject's culture and practice."
  quote: full   # the issuer's statement is in `source` (D-std-0014)
  audience: practitioner
  subjects: inherited
- id: qaa/business-and-management-2023/1.17
  locator: { number: "1.17", headingPath: ["Context and purposes of a Business and Management degree", "Equality, diversity and inclusion"] }
  span: { start: 16341, end: 17190 }
  source: "1.17 Why the subject is taught: Through a focus on equality, diversity and inclusion, business and management education can support the progress of organisations (including private, public and third sector) in addressing inequality and disadvantage as captured by the UN Sustainable Development Goals , such as decent work and economic growth, gender equality and reduced inequalities. Instilling the principles of equality, diversity and inclusion, along with an appreciation of the importance of continued reflective practice, equips students to flourish in an increasingly diverse and global world, and to foster an inclusive approach in their future contributions to organisations and society. The study of Business and Management will embed the principles of equality, diversity and inclusion in future managers and leaders (see paragraph 1.6)\n"
  stem: none
  statementType: expectation
  rung: none
  force: will
  level: fheq:6
  appliesTo: "future managers and leaders studying the subject"
  addressee: learner
  verbs: ["embed", "equips", "support"]
  about: "EDI principles in future managers and leaders"
  themes: [theme:edi]
  domain: generic-skill
  award: ["bachelor's with honours"]
  gradeOf: none
  paraphrase: "A focus on EDI lets business education help organisations tackle inequality and disadvantage, in line with the SDGs; joined with reflective practice it readies students for a diverse, global world, and study of the subject will instil EDI principles in future managers and leaders."
  quote: full   # the issuer's statement is in `source` (D-std-0014)
  audience: both
  subjects: inherited
- id: qaa/business-and-management-2023/1.18
  locator: { number: "1.18", headingPath: ["Context and purposes of a Business and Management degree", "Equality, diversity and inclusion"] }
  span: { start: 17190, end: 18587 }
  source: "1.18 What is taught: Business and Management courses ensure that students gain a critical understanding of the role that organisations, and the leaders within them, play in promoting equality, diversity and inclusion. Business and Management graduates should not only be aware of the legal requirement to protect people from discrimination, but also equipped with the knowledge and skills needed to foster inclusive workplaces to meet the economic, social and environmental objectives of organisations and wider stakeholders. Courses can ensure that students have an appreciation of the role of business and management in addressing global challenges. As part of a commitment to EDI, courses should also ensure that the content covered is diverse and offers a critical examination of dominant approaches to the discipline, raising awareness of the ways in which they can perpetuate exclusion and exploring alternatives to such approaches. In doing so, it is important that a wide and diverse range of perspectives is recognised and drawn upon, such as from the Global South, marginalised communities and local/regional/national issues. Using examples and cases that are representative of both the diversity of the student cohort and society more widely not only enriches the educational provision for all students, but also helps foster greater engagement and a sense of belonging among students.\n"
  stem: none
  statementType: expectation
  rung: none
  force: should
  level: fheq:6
  appliesTo: "graduates and courses in the subject"
  addressee: both
  verbs: ["ensure", "gain", "equipped", "offers"]
  about: "what is taught on EDI: law, inclusive workplaces, diverse content"
  themes: [theme:edi]
  domain: understanding
  award: ["bachelor's with honours"]
  gradeOf: none
  paraphrase: "Courses make sure students critically grasp how organisations and their leaders advance EDI; graduates should know the legal duty to prevent discrimination and have the knowledge and skills to build inclusive workplaces; courses should also offer diverse content that questions dominant approaches, drawing on perspectives such as the Global South and marginalised communities."
  quote: full   # the issuer's statement is in `source` (D-std-0014)
  audience: both
  subjects: inherited
- id: qaa/business-and-management-2023/1.19
  locator: { number: "1.19", headingPath: ["Context and purposes of a Business and Management degree", "Equality, diversity and inclusion"] }
  span: { start: 18587, end: 19826 }
  source: "1.19 How the subject is taught: Courses in Business and Management should be designed to enable students from all backgrounds to realise their potential and for all students regardless of their race/ethnicity, religion, gender, sexual orientation, disability or social background to feel represented and included. It is also important that how the subject is taught and assessed is reflective of inclusive principles and that issues such as the mode of learning (for example, in-person, digital, blended, hybrid, hyflex, experiential, block release, full/part-time; synchronous/asynchronous) are considered carefully, as all pose different opportunities and challenges. The mode of learning and course structure can help make education more accessible and inclusive (see also paragraphs 1.22-1.24). Assessment design can provide opportunities for different types of students to succeed. How\n\n6\nthe subject is taught should reflect an awareness of EDI in terms of different pedagogical approaches, and the teaching approaches adopted can enable the diversity of the cohort to enrich the experience for all students. Approaches to teaching and learning include the ethical consideration of each person’s multiple identities and experiences.\n"
  stem: none
  statementType: requirement
  rung: none
  force: should
  level: none
  appliesTo: "course design and teaching"
  addressee: provider
  verbs: ["designed", "enable", "considered"]
  about: "inclusive design, teaching and modes of learning"
  themes: [theme:edi]
  domain: none
  award: ["bachelor's with honours"]
  gradeOf: none
  paraphrase: "Courses should be built so that students of every background can reach their potential and feel represented; teaching and assessment should follow inclusive principles, with modes of learning chosen with care, and teaching should show awareness of EDI in its pedagogy."
  quote: full   # the issuer's statement is in `source` (D-std-0014)
  audience: practitioner
  subjects: inherited
- id: qaa/business-and-management-2023/1.21
  locator: { number: "1.21", headingPath: ["Context and purposes of a Business and Management degree", "Equality, diversity and inclusion"] }
  span: { start: 21642, end: 22107 }
  source: "1.21 Consideration of EDI within courses is not a one-off activity. Course teams should regularly reflect upon how EDI can be further enhanced and, where possible, work in partnership with students in doing so. Equality and diversity form the basis for disciplinary practice and inclusivity is an ongoing process of quality review and enhancement. The process to approve changes to courses can consider completing a formal equality impact assessment. Accessibility\n"
  stem: none
  statementType: requirement
  rung: none
  force: should
  level: none
  appliesTo: "course teams"
  addressee: provider
  verbs: ["reflect", "work"]
  about: "EDI review as an ongoing process with students"
  themes: [theme:edi]
  domain: none
  award: ["bachelor's with honours"]
  gradeOf: none
  paraphrase: "Attention to EDI is continuous: course teams should reflect regularly on improving it and, where they can, do so in partnership with students; changes to courses may include an equality impact assessment."
  quote: full   # the issuer's statement is in `source` (D-std-0014)
  audience: practitioner
  subjects: inherited
- id: qaa/business-and-management-2023/1.22
  locator: { number: "1.22", headingPath: ["Context and purposes of a Business and Management degree", "Accessibility"] }
  span: { start: 22230, end: 22415 }
  source: "Accessibility should, as a minimum, meet regulatory requirements and will apply to all stages of the course, from providing pre-application information through to graduation and beyond."
  stem: none
  statementType: requirement
  rung: none
  force: should
  level: none
  appliesTo: "every stage of the course"
  addressee: provider
  verbs: ["meet", "apply"]
  about: "accessibility meets regulation and covers the whole course"
  themes: [theme:accessibility]
  domain: none
  award: ["bachelor's with honours"]
  gradeOf: none
  paraphrase: "At the least, accessibility should satisfy what regulation requires, and it will reach every stage of the course, from information before application to graduation and after."
  quote: full   # the issuer's statement is in `source` (D-std-0014)
  audience: practitioner
  subjects: inherited
- id: qaa/business-and-management-2023/1.24
  locator: { number: "1.24", headingPath: ["Context and purposes of a Business and Management degree", "Accessibility"] }
  span: { start: 23207, end: 23461 }
  source: "1.24 Accessibility should include enabling the same opportunities for workplace and international learning for all students, as well as providing students with inclusive digital accessibility without discrimination. Education for Sustainable Development\n"
  stem: none
  statementType: requirement
  rung: none
  force: should
  level: none
  appliesTo: "courses in the subject"
  addressee: provider
  verbs: ["include", "enabling", "providing"]
  about: "equal access to work and international learning, and digital access"
  themes: [theme:accessibility]
  domain: none
  award: ["bachelor's with honours"]
  gradeOf: none
  paraphrase: "Accessibility should give every student the same chances of workplace and international learning, and digital access that is inclusive and free of discrimination."
  quote: full   # the issuer's statement is in `source` (D-std-0014)
  audience: practitioner
  subjects: inherited
- id: qaa/business-and-management-2023/1.26
  locator: { number: "1.26", headingPath: ["Context and purposes of a Business and Management degree", "Education for Sustainable Development"] }
  span: { start: 25122, end: 25299 }
  source: "Management for economic, social and environmental sustainability needs to be integrated systematically within the Business and Management curriculum and across functional areas."
  stem: none
  statementType: requirement
  rung: none
  force: must   # D-std-0016: "needs to" read as must
  level: none
  appliesTo: "the curriculum of the subject"
  addressee: provider
  verbs: ["integrated"]
  about: "sustainability built into the curriculum across functions"
  themes: [theme:esd]
  domain: none
  award: ["bachelor's with honours"]
  gradeOf: none
  paraphrase: "Managing for economic, social and environmental sustainability needs to run systematically through the curriculum and across business functions (the issuer's 'needs to', recorded as describes)."
  quote: full   # the issuer's statement is in `source` (D-std-0014)
  audience: practitioner
  subjects: inherited
- id: qaa/business-and-management-2023/2.7
  locator: { number: "2.7", headingPath: ["Distinctive features of a Business and Management degree", "Progression"] }
  span: { start: 31427, end: 32538 }
  source: "2.7 Over the course of a degree with honours (FHEQ Level 6; FQHEIS Level 10) a Business and Management student will progress from one level of study to the next, in line with the regulations and processes for each institution. However, it is expected that each level would see the attainment of certain levels of knowledge, understanding and skills that build towards the final achievement of meeting the threshold-level subject-specific standards listed in this Statement. This will usually include successful completion and the award of credit for the full range of learning and assessment, including any practical components. Upon graduation from an undergraduate degree, it would be expected that a student who had achieved a typical degree or higher would be capable of, and equipped for, undertaking postgraduate study in a more specialist, a more applied, or a more advanced Business and Management subject, or one in a cognate discipline. Entry requirements to postgraduate courses are, however, determined by individual providers and may require specified levels of achievement at undergraduate level.\n"
  stem: none
  statementType: expectation
  rung: none
  force: will
  level: fheq:6
  appliesTo: "students progressing through the degree"
  addressee: learner
  verbs: ["progress", "build", "undertaking"]
  about: "progression to threshold and readiness for postgraduate study"
  themes: [none]
  domain: none
  award: ["bachelor's with honours"]
  gradeOf: none
  paraphrase: "An honours student will move from level to level under each institution's rules, each level building toward the threshold standards; a student reaching the typical standard or above would be expected to be ready for postgraduate study, though entry is for each provider to decide."
  quote: full   # the issuer's statement is in `source` (D-std-0014)
  audience: both
  subjects: inherited
- id: qaa/business-and-management-2023/2.8
  locator: { number: "2.8", headingPath: ["Distinctive features of a Business and Management degree", "Progression"] }
  span: { start: 32538, end: 32895 }
  source: "2.8 Undergraduates studying a combined, joint or major-minor route will achieve core elements of the specific and generic skills for the subject and will add others according to the\n\n10\nsubjects covered in joint courses. Additionally, they may explore the overlap between their two subject areas, creating further opportunities for interdisciplinary study.\n"
  stem: none
  statementType: expectation
  rung: none
  force: will
  level: fheq:6
  appliesTo: "students on joint, combined or major-minor routes"
  addressee: learner
  verbs: ["achieve", "add", "explore"]
  about: "core skills on joint and combined routes"
  themes: [none]
  domain: subject-skill
  award: ["bachelor's with honours"]
  gradeOf: none
  paraphrase: "Students on combined, joint or major-minor routes will gain the core elements of the subject's specific and generic skills and add others from their second subject, possibly exploring where the two overlap."
  quote: full   # the issuer's statement is in `source` (D-std-0014)
  audience: both
  subjects: inherited
- id: qaa/business-and-management-2023/2.18
  locator: { number: "2.18", headingPath: ["Distinctive features of a Business and Management degree", "Monitoring and review"] }
  span: { start: 38480, end: 38792 }
  source: "2.18 Externality is an essential component of the quality assurance system in the UK. Higher education providers will use external reviewers as part of periodic review to gain an external perspective on any proposed changes and ensure threshold standards are achieved and content is appropriate for the subject.\n"
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
  award: ["bachelor's with honours"]
  gradeOf: none
  paraphrase: "Externality is central to UK quality assurance: providers will bring in external reviewers during periodic review to gain an outside view of proposed changes and confirm that threshold standards are met and content suits the subject."
  quote: full   # the issuer's statement is in `source` (D-std-0014)
  audience: practitioner
  subjects: inherited
- id: qaa/business-and-management-2023/3.2
  locator: { number: "3.2", headingPath: ["Content, structure and delivery", "Content: knowledge and understanding"] }
  span: { start: 40972, end: 41459 }
  source: "3.2 Graduates should reasonably be expected to demonstrate relevant knowledge and understanding of a range of organisations, the wider business environment and communities in which they operate, and their governance and management. Courses emphasise understanding, responding to and shaping the dynamic and changing nature of work and the consideration of the future of organisations within the global business environment, including the management of risk, and their impact on society.\n"
  stem: none
  statementType: outcome
  rung: none
  force: should
  level: fheq:6
  appliesTo: "graduates of the subject"
  addressee: learner
  verbs: ["demonstrate", "emphasise"]
  about: "knowledge of organisations, their environment and governance"
  themes: [none]
  domain: knowledge
  award: ["bachelor's with honours"]
  gradeOf: none
  paraphrase: "Graduates should reasonably be able to show knowledge and understanding of varied organisations, their wider business setting and communities, and how they are governed and managed; courses stress the changing nature of work, the future of organisations globally, risk and their effect on society."
  quote: full   # the issuer's statement is in `source` (D-std-0014)
  audience: both
  subjects: inherited
- id: qaa/business-and-management-2023/3.3
  locator: { number: "3.3", headingPath: ["Content, structure and delivery", "Content: knowledge and understanding"] }
  span: { start: 41459, end: 41721 }
  source: "3.3 The interrelationships among, and the integration between, different areas of understanding are very important within the overall student learning experience, and should be demonstrated in the capabilities of successful graduates from all modes of learning.\n"
  stem: none
  statementType: outcome
  rung: none
  force: should
  level: fheq:6
  appliesTo: "successful graduates from every mode of learning"
  addressee: both
  verbs: ["demonstrated"]
  about: "integrating areas of understanding"
  themes: [none]
  domain: understanding
  award: ["bachelor's with honours"]
  gradeOf: none
  paraphrase: "How areas of understanding relate and fit together matters greatly in the learning experience and should show in what successful graduates can do, whatever their mode of study."
  quote: full   # the issuer's statement is in `source` (D-std-0014)
  audience: both
  subjects: inherited
- id: qaa/business-and-management-2023/3.7.b1
  locator: { number: "3.7.b1", headingPath: ["Content, structure and delivery", "Content: knowledge and understanding"] }
  span: { start: 43197, end: 43402 }
  source: "ethics, responsibility and sustainability: managing responsibly and behaving ethically, particularly in relation to social, cultural, legal, economic and environmental issues (see also paragraphs 1.25-2 8)"
  stem: "3.7"
  statementType: outcome
  rung: none
  force: should
  level: fheq:6
  appliesTo: "graduates of the subject"
  addressee: learner
  verbs: ["managing", "behaving"]
  about: "ethics, responsibility and sustainability"
  themes: [none]
  domain: knowledge
  award: ["bachelor's with honours"]
  gradeOf: none
  paraphrase: "Should show knowledge and critical evaluation of managing responsibly and acting ethically, above all on social, cultural, legal, economic and environmental questions."
  quote: full   # the issuer's statement is in `source` (D-std-0014)
  audience: both
  subjects: inherited
- id: qaa/business-and-management-2023/3.7.b2
  locator: { number: "3.7.b2", headingPath: ["Content, structure and delivery", "Content: knowledge and understanding"] }
  span: { start: 43405, end: 43570 }
  source: "markets and economies: the development, access and operation of markets for resources, goods and services. This includes market failure, externalities and fair trade"
  stem: "3.7"
  statementType: outcome
  rung: none
  force: should
  level: fheq:6
  appliesTo: "graduates of the subject"
  addressee: learner
  verbs: []
  about: "markets and economies"
  themes: [none]
  domain: knowledge
  award: ["bachelor's with honours"]
  gradeOf: none
  paraphrase: "Should show knowledge and critical evaluation of how markets for resources, goods and services form, are reached and work, including market failure, externalities and fair trade."
  quote: full   # the issuer's statement is in `source` (D-std-0014)
  audience: both
  subjects: inherited
- id: qaa/business-and-management-2023/3.7.b3
  locator: { number: "3.7.b3", headingPath: ["Content, structure and delivery", "Content: knowledge and understanding"] }
  span: { start: 43573, end: 43813 }
  source: "marketing, sales, negotiation and customers: management of customer relationships, consumer behaviour, different approaches for segmentation, targeting, positioning, generating sales and the need for innovation in product and service design"
  stem: "3.7"
  statementType: outcome
  rung: none
  force: should
  level: fheq:6
  appliesTo: "graduates of the subject"
  addressee: learner
  verbs: ["generating"]
  about: "marketing, sales, negotiation and customers"
  themes: [none]
  domain: knowledge
  award: ["bachelor's with honours"]
  gradeOf: none
  paraphrase: "Should show knowledge and critical evaluation of managing customer relationships, consumer behaviour, segmenting, targeting and positioning, selling and innovating in products and services."
  quote: full   # the issuer's statement is in `source` (D-std-0014)
  audience: both
  subjects: inherited
- id: qaa/business-and-management-2023/3.7.b4
  locator: { number: "3.7.b4", headingPath: ["Content, structure and delivery", "Content: knowledge and understanding"] }
  span: { start: 43820, end: 44016 }
  source: "finance and accounting: the sources, practises and management of finance and the use of accounting and other information systems for planning, control, decision- making and managing financial risk"
  stem: "3.7"
  statementType: outcome
  rung: none
  force: should
  level: fheq:6
  appliesTo: "graduates of the subject"
  addressee: learner
  verbs: []
  about: "finance and accounting"
  themes: [none]
  domain: knowledge
  award: ["bachelor's with honours"]
  gradeOf: none
  paraphrase: "Should show knowledge and critical evaluation of where finance comes from, how it is managed, and how accounting and other information systems support planning, control, decisions and financial risk."
  quote: full   # the issuer's statement is in `source` (D-std-0014)
  audience: both
  subjects: inherited
- id: qaa/business-and-management-2023/3.7.b5
  locator: { number: "3.7.b5", headingPath: ["Content, structure and delivery", "Content: knowledge and understanding"] }
  span: { start: 44019, end: 44449 }
  source: "people and organisational behaviour: responsible, inclusive and ethical leadership (see paragraph 1.6), management and development of people and organisations, including employee engagement and the implications of the legal context. This requires recognition of the design and development of organisations, grounded in an understanding of cross-cultural issues, and equality, diversity and inclusion (see also paragraphs 1.14-2 0)"
  stem: "3.7"
  statementType: outcome
  rung: none
  force: should
  level: fheq:6
  appliesTo: "graduates of the subject"
  addressee: learner
  verbs: ["grounded"]
  about: "people, organisational behaviour and EDI"
  themes: [none]
  domain: knowledge
  award: ["bachelor's with honours"]
  gradeOf: none
  paraphrase: "Should show knowledge and critical evaluation of responsible, inclusive and ethical leadership, managing and developing people and organisations, employee engagement and employment law, grounded in cross-cultural understanding and EDI."
  quote: full   # the issuer's statement is in `source` (D-std-0014)
  audience: both
  subjects: inherited
- id: qaa/business-and-management-2023/3.7.b6
  locator: { number: "3.7.b6", headingPath: ["Content, structure and delivery", "Content: knowledge and understanding"] }
  span: { start: 44452, end: 44645 }
  source: "operations and business innovation: the management of resources, the supply chain, procurement, logistics, outsourcing, quality systems, development of service excellence and project management"
  stem: "3.7"
  statementType: outcome
  rung: none
  force: should
  level: fheq:6
  appliesTo: "graduates of the subject"
  addressee: learner
  verbs: []
  about: "operations and business innovation"
  themes: [none]
  domain: knowledge
  award: ["bachelor's with honours"]
  gradeOf: none
  paraphrase: "Should show knowledge and critical evaluation of managing resources, supply chains, procurement, logistics, outsourcing, quality systems, service excellence and projects."
  quote: full   # the issuer's statement is in `source` (D-std-0014)
  audience: both
  subjects: inherited
- id: qaa/business-and-management-2023/3.7.b7
  locator: { number: "3.7.b7", headingPath: ["Content, structure and delivery", "Content: knowledge and understanding"] }
  span: { start: 44648, end: 44979 }
  source: "data analytics, statistics, digital business, information systems and business intelligence: the development of strategic priorities to deliver business at speed through the management, application and implementation of information systems and their impact upon organisations, and to enable data-driven and informed decision-making"
  stem: "3.7"
  statementType: outcome
  rung: none
  force: should
  level: fheq:6
  appliesTo: "graduates of the subject"
  addressee: learner
  verbs: ["deliver", "enable"]
  about: "data, digital business and information systems"
  themes: [none]
  domain: knowledge
  award: ["bachelor's with honours"]
  gradeOf: none
  paraphrase: "Should show knowledge and critical evaluation of setting strategic priorities for fast delivery through managing and applying information systems, their effect on organisations, and data-led decisions."
  quote: full   # the issuer's statement is in `source` (D-std-0014)
  audience: both
  subjects: inherited
- id: qaa/business-and-management-2023/3.7.b8
  locator: { number: "3.7.b8", headingPath: ["Content, structure and delivery", "Content: knowledge and understanding"] }
  span: { start: 44982, end: 45302 }
  source: "business policy and strategy: the development of appropriate policies and strategies within a changing environment to meet stakeholder interests, and the use of risk and crisis management techniques, business continuity planning and communication techniques and tools to help maximise achievement of strategic objectives"
  stem: "3.7"
  statementType: outcome
  rung: none
  force: should
  level: fheq:6
  appliesTo: "graduates of the subject"
  addressee: learner
  verbs: []
  about: "business policy and strategy"
  themes: [none]
  domain: knowledge
  award: ["bachelor's with honours"]
  gradeOf: none
  paraphrase: "Should show knowledge and critical evaluation of forming policies and strategies for a changing setting and stakeholder interests, with risk and crisis management, continuity planning and communication used to reach strategic aims."
  quote: full   # the issuer's statement is in `source` (D-std-0014)
  audience: both
  subjects: inherited
- id: qaa/business-and-management-2023/3.7.b9
  locator: { number: "3.7.b9", headingPath: ["Content, structure and delivery", "Content: knowledge and understanding"] }
  span: { start: 45305, end: 45635 }
  source: "public and non-profit management: the distinct roles and practices of public service organisations and the voluntary and community sector, including approaches to governance, financial management, public leadership, community empowerment, coproduction, public values and ethics and hybrid organisations for public service delivery"
  stem: "3.7"
  statementType: outcome
  rung: none
  force: should
  level: fheq:6
  appliesTo: "graduates of the subject"
  addressee: learner
  verbs: []
  about: "public and non-profit management"
  themes: [none]
  domain: knowledge
  award: ["bachelor's with honours"]
  gradeOf: none
  paraphrase: "Should show knowledge and critical evaluation of what is distinct in public service bodies and the voluntary and community sector: governance, finance, public leadership, community empowerment, coproduction, public value and hybrid delivery."
  quote: full   # the issuer's statement is in `source` (D-std-0014)
  audience: both
  subjects: inherited
- id: qaa/business-and-management-2023/3.7.b10
  locator: { number: "3.7.b10", headingPath: ["Content, structure and delivery", "Content: knowledge and understanding"] }
  span: { start: 45638, end: 45991 }
  source: "entrepreneurship and enterprise development: taking innovative business ideas to create or co-create new products, services or organisations that will generate a return on financial and/or social investment - this includes, but is not limited to, the identification of intellectual property and appreciation of its value (see also paragraphs 1.29-1.33)."
  stem: "3.7"
  statementType: outcome
  rung: none
  force: should
  level: fheq:6
  appliesTo: "graduates of the subject"
  addressee: learner
  verbs: ["taking", "create", "generate"]
  about: "entrepreneurship and enterprise development"
  themes: [none]
  domain: knowledge
  award: ["bachelor's with honours"]
  gradeOf: none
  paraphrase: "Should show knowledge and critical evaluation of turning new business ideas into products, services or organisations that return financial or social value, including spotting intellectual property and valuing it."
  quote: full   # the issuer's statement is in `source` (D-std-0014)
  audience: both
  subjects: inherited
- id: qaa/business-and-management-2023/3.9
  locator: { number: "3.9", headingPath: ["Content, structure and delivery", "Skills and practice"] }
  span: { start: 46191, end: 46489 }
  source: "3.9 Graduates should be able to demonstrate a range of cognitive and intellectual skills together with competencies specific to business and management. Graduates should also be able to demonstrate relevant personal and interpersonal skills. These include both subject-specific and generic skills.\n"
  stem: none
  statementType: outcome
  rung: none
  force: should
  level: fheq:6
  appliesTo: "graduates of the subject"
  addressee: learner
  verbs: ["demonstrate"]
  about: "cognitive, subject-specific, personal and interpersonal skills"
  themes: [none]
  domain: subject-skill
  award: ["bachelor's with honours"]
  gradeOf: none
  paraphrase: "Graduates should be able to show cognitive and intellectual skills with competencies particular to business and management, and also personal and interpersonal skills, both subject-specific and generic."
  quote: full   # the issuer's statement is in `source` (D-std-0014)
  audience: both
  subjects: inherited
- id: qaa/business-and-management-2023/3.10.b1
  locator: { number: "3.10.b1", headingPath: ["Content, structure and delivery", "Skills and practice"] }
  span: { start: 46563, end: 46717 }
  source: "people management: communications, team building, resilience and well-being, leadership and motivating others, nurturing equality, diversity and inclusion"
  stem: "3.10"
  statementType: outcome
  rung: none
  force: describes
  level: fheq:6
  appliesTo: "graduates of the subject"
  addressee: learner
  verbs: ["nurturing"]
  about: "people management"
  themes: [none]
  domain: subject-skill
  award: ["bachelor's with honours"]
  gradeOf: none
  paraphrase: "People management: communicating, building teams, resilience and well-being, leading and motivating, and fostering EDI."
  quote: full   # the issuer's statement is in `source` (D-std-0014)
  audience: both
  subjects: inherited
- id: qaa/business-and-management-2023/3.10.b2
  locator: { number: "3.10.b2", headingPath: ["Content, structure and delivery", "Skills and practice"] }
  span: { start: 46720, end: 46894 }
  source: "problem-solving and critical analysis: analysing facts and circumstances to determine the cause of a problem, decision-making and selecting appropriate, sustainable solutions"
  stem: "3.10"
  statementType: outcome
  rung: none
  force: describes
  level: fheq:6
  appliesTo: "graduates of the subject"
  addressee: learner
  verbs: ["analysing", "determine", "selecting"]
  about: "problem-solving and critical analysis"
  themes: [none]
  domain: subject-skill
  award: ["bachelor's with honours"]
  gradeOf: none
  paraphrase: "Problem-solving and critical analysis: examining facts and circumstances to find a problem's cause, then deciding on fitting, sustainable solutions."
  quote: full   # the issuer's statement is in `source` (D-std-0014)
  audience: both
  subjects: inherited
- id: qaa/business-and-management-2023/3.10.b3
  locator: { number: "3.10.b3", headingPath: ["Content, structure and delivery", "Skills and practice"] }
  span: { start: 46897, end: 47156 }
  source: "research: the ability to analyse and evaluate a range of data, sources of information and appropriate methodologies, which includes the need for strong digital literacy,\n\n15\nand to use that research for evidence-based, responsible and ethical decision- making"
  stem: "3.10"
  statementType: outcome
  rung: none
  force: describes
  level: fheq:6
  appliesTo: "graduates of the subject"
  addressee: learner
  verbs: ["analyse", "evaluate", "use"]
  about: "research and evidence-based decisions"
  themes: [none]
  domain: subject-skill
  award: ["bachelor's with honours"]
  gradeOf: none
  paraphrase: "Research: analysing and judging data, information sources and suitable methods, with strong digital literacy, and using the findings for decisions that are evidence-based, responsible and ethical."
  quote: full   # the issuer's statement is in `source` (D-std-0014)
  audience: both
  subjects: inherited
- id: qaa/business-and-management-2023/3.10.b4
  locator: { number: "3.10.b4", headingPath: ["Content, structure and delivery", "Skills and practice"] }
  span: { start: 47159, end: 47362 }
  source: "commercial acumen: based on an awareness of the key drivers for business success, causes of failure and the importance of providing customer satisfaction and building customer loyalty in sustainable ways"
  stem: "3.10"
  statementType: outcome
  rung: none
  force: describes
  level: fheq:6
  appliesTo: "graduates of the subject"
  addressee: learner
  verbs: ["based"]
  about: "commercial acumen"
  themes: [none]
  domain: subject-skill
  award: ["bachelor's with honours"]
  gradeOf: none
  paraphrase: "Commercial acumen: grounded in awareness of what drives business success and failure, and why customer satisfaction and loyalty matter, pursued sustainably."
  quote: full   # the issuer's statement is in `source` (D-std-0014)
  audience: both
  subjects: inherited
- id: qaa/business-and-management-2023/3.10.b5
  locator: { number: "3.10.b5", headingPath: ["Content, structure and delivery", "Skills and practice"] }
  span: { start: 47365, end: 47587 }
  source: "innovation, creativity and enterprise: the ability to act entrepreneurially to generate, develop and communicate ideas, manage and exploit intellectual property, gain support and deliver successful and sustainable outcomes"
  stem: "3.10"
  statementType: outcome
  rung: none
  force: describes
  level: fheq:6
  appliesTo: "graduates of the subject"
  addressee: learner
  verbs: ["act", "generate", "develop", "communicate", "manage", "exploit", "gain", "deliver"]
  about: "innovation, creativity and enterprise"
  themes: [none]
  domain: subject-skill
  award: ["bachelor's with honours"]
  gradeOf: none
  paraphrase: "Innovation, creativity and enterprise: acting entrepreneurially to produce, develop and share ideas, handle and use intellectual property, win support and achieve sustainable results."
  quote: full   # the issuer's statement is in `source` (D-std-0014)
  audience: both
  subjects: inherited
- id: qaa/business-and-management-2023/3.10.b6
  locator: { number: "3.10.b6", headingPath: ["Content, structure and delivery", "Skills and practice"] }
  span: { start: 47590, end: 47722 }
  source: "numeracy: the use of quantitative skills to manipulate data, evaluate, estimate and model business problems, functions and phenomena"
  stem: "3.10"
  statementType: outcome
  rung: none
  force: describes
  level: fheq:6
  appliesTo: "graduates of the subject"
  addressee: learner
  verbs: ["manipulate", "evaluate", "estimate", "model"]
  about: "numeracy and quantitative skills"
  themes: [none]
  domain: subject-skill
  award: ["bachelor's with honours"]
  gradeOf: none
  paraphrase: "Numeracy: using quantitative skills to work with data and to judge, estimate and model the problems and functions of a business."
  quote: full   # the issuer's statement is in `source` (D-std-0014)
  audience: both
  subjects: inherited
- id: qaa/business-and-management-2023/3.10.b7
  locator: { number: "3.10.b7", headingPath: ["Content, structure and delivery", "Skills and practice"] }
  span: { start: 47725, end: 47889 }
  source: "networking: an awareness of the interpersonal skills of effective listening, negotiating, persuasion and presentation and their use in cultivating business contacts"
  stem: "3.10"
  statementType: outcome
  rung: none
  force: describes
  level: fheq:6
  appliesTo: "graduates of the subject"
  addressee: learner
  verbs: ["cultivating"]
  about: "networking and interpersonal skills"
  themes: [none]
  domain: subject-skill
  award: ["bachelor's with honours"]
  gradeOf: none
  paraphrase: "Networking: awareness of listening, negotiating, persuading and presenting, and using them to build business contacts."
  quote: full   # the issuer's statement is in `source` (D-std-0014)
  audience: both
  subjects: inherited
- id: qaa/business-and-management-2023/3.10.b8
  locator: { number: "3.10.b8", headingPath: ["Content, structure and delivery", "Skills and practice"] }
  span: { start: 47892, end: 48048 }
  source: "leadership: boundary-spanning, influencing, relational and collaborative working, including ability to work in partnerships across organisation and sectors."
  stem: "3.10"
  statementType: outcome
  rung: none
  force: describes
  level: fheq:6
  appliesTo: "graduates of the subject"
  addressee: learner
  verbs: ["including"]
  about: "boundary-spanning and collaborative leadership"
  themes: [none]
  domain: subject-skill
  award: ["bachelor's with honours"]
  gradeOf: none
  paraphrase: "Leadership: spanning boundaries, influencing, relating and collaborating, including partnership working across organisations and sectors."
  quote: full   # the issuer's statement is in `source` (D-std-0014)
  audience: both
  subjects: inherited
- id: qaa/business-and-management-2023/3.11.b1
  locator: { number: "3.11.b1", headingPath: ["Content, structure and delivery", "Skills and practice"] }
  span: { start: 48101, end: 48193 }
  source: "ability to work collaboratively and inclusively with both internal and external stakeholders"
  stem: "3.11"
  statementType: outcome
  rung: none
  force: describes
  level: fheq:6
  appliesTo: "graduates of the subject"
  addressee: learner
  verbs: []
  about: "collaborative and inclusive working"
  themes: [none]
  domain: generic-skill
  award: ["bachelor's with honours"]
  gradeOf: none
  paraphrase: "Working together, inclusively, with stakeholders inside and outside the organisation."
  quote: full   # the issuer's statement is in `source` (D-std-0014)
  audience: both
  subjects: inherited
- id: qaa/business-and-management-2023/3.11.b2
  locator: { number: "3.11.b2", headingPath: ["Content, structure and delivery", "Skills and practice"] }
  span: { start: 48196, end: 48240 }
  source: "verbal, non-verbal and digital communication"
  stem: "3.11"
  statementType: outcome
  rung: none
  force: describes
  level: fheq:6
  appliesTo: "graduates of the subject"
  addressee: learner
  verbs: []
  about: "verbal, non-verbal and digital communication"
  themes: [none]
  domain: generic-skill
  award: ["bachelor's with honours"]
  gradeOf: none
  paraphrase: "Communicating in speech, without words and through digital means."
  quote: full   # the issuer's statement is in `source` (D-std-0014)
  audience: both
  subjects: inherited
- id: qaa/business-and-management-2023/3.11.b3
  locator: { number: "3.11.b3", headingPath: ["Content, structure and delivery", "Skills and practice"] }
  span: { start: 48243, end: 48266 }
  source: "empathy and inclusivity"
  stem: "3.11"
  statementType: outcome
  rung: none
  force: describes
  level: fheq:6
  appliesTo: "graduates of the subject"
  addressee: learner
  verbs: []
  about: "empathy and inclusivity"
  themes: [none]
  domain: generic-skill
  award: ["bachelor's with honours"]
  gradeOf: none
  paraphrase: "Empathy and inclusivity."
  quote: full   # the issuer's statement is in `source` (D-std-0014)
  audience: both
  subjects: inherited
- id: qaa/business-and-management-2023/3.11.b4
  locator: { number: "3.11.b4", headingPath: ["Content, structure and delivery", "Skills and practice"] }
  span: { start: 48269, end: 48299 }
  source: "digital literacy and etiquette"
  stem: "3.11"
  statementType: outcome
  rung: none
  force: describes
  level: fheq:6
  appliesTo: "graduates of the subject"
  addressee: learner
  verbs: []
  about: "digital literacy and etiquette"
  themes: [none]
  domain: generic-skill
  award: ["bachelor's with honours"]
  gradeOf: none
  paraphrase: "Using digital tools capably and behaving appropriately online."
  quote: full   # the issuer's statement is in `source` (D-std-0014)
  audience: both
  subjects: inherited
- id: qaa/business-and-management-2023/3.11.b5
  locator: { number: "3.11.b5", headingPath: ["Content, structure and delivery", "Skills and practice"] }
  span: { start: 48302, end: 48380 }
  source: "conceptual, systemic and critical thinking, analysis, synthesis and evaluation"
  stem: "3.11"
  statementType: outcome
  rung: none
  force: describes
  level: fheq:6
  appliesTo: "graduates of the subject"
  addressee: learner
  verbs: []
  about: "conceptual, systemic and critical thinking"
  themes: [none]
  domain: generic-skill
  award: ["bachelor's with honours"]
  gradeOf: none
  paraphrase: "Conceptual, systems and critical thinking, with analysis, synthesis and evaluation."
  quote: full   # the issuer's statement is in `source` (D-std-0014)
  audience: both
  subjects: inherited
- id: qaa/business-and-management-2023/3.11.b6
  locator: { number: "3.11.b6", headingPath: ["Content, structure and delivery", "Skills and practice"] }
  span: { start: 48383, end: 48656 }
  source: "self -management: development as independent learners, a readiness to accept responsibility and flexibility, to tolerate uncertainty, handle complexity, challenge assumptions, use evidence to inform critical thinking, be resilient, self-starting and appropriately assertive"
  stem: "3.11"
  statementType: outcome
  rung: none
  force: describes
  level: fheq:6
  appliesTo: "graduates of the subject"
  addressee: learner
  verbs: ["accept", "tolerate", "handle", "challenge", "use"]
  about: "self-management and independent learning"
  themes: [none]
  domain: generic-skill
  award: ["bachelor's with honours"]
  gradeOf: none
  paraphrase: "Self-management: growing as an independent learner, ready to take responsibility, be flexible, live with uncertainty, handle complexity, question assumptions, think critically from evidence, and be resilient, self-starting and suitably assertive."
  quote: full   # the issuer's statement is in `source` (D-std-0014)
  audience: both
  subjects: inherited
- id: qaa/business-and-management-2023/3.11.b7
  locator: { number: "3.11.b7", headingPath: ["Content, structure and delivery", "Skills and practice"] }
  span: { start: 48659, end: 48819 }
  source: "self -reflection: self-analysis and an awareness/sensitivity to diversity in terms of people and cultures - this includes a continuing appetite for development."
  stem: "3.11"
  statementType: outcome
  rung: none
  force: describes
  level: fheq:6
  appliesTo: "graduates of the subject"
  addressee: learner
  verbs: []
  about: "self-reflection and sensitivity to diversity"
  themes: [none]
  domain: generic-skill
  award: ["bachelor's with honours"]
  gradeOf: none
  paraphrase: "Self-reflection: analysing oneself, awareness of and sensitivity to differences between people and cultures, and a lasting wish to develop."
  quote: full   # the issuer's statement is in `source` (D-std-0014)
  audience: both
  subjects: inherited
- id: qaa/business-and-management-2023/3.18
  locator: { number: "3.18", headingPath: ["Content, structure and delivery", "Assessment"] }
  span: { start: 51813, end: 52090 }
  source: "3.18 Assessment should form part of the learning process and student learning is assisted through the provision of feedback on formative and summative work. Feedback should be provided in a timely actionable manner, enabling development both within a module/unit and a course.\n"
  stem: none
  statementType: requirement
  rung: none
  force: should
  level: none
  appliesTo: "assessment in the course"
  addressee: provider
  verbs: ["form", "provided", "enabling"]
  about: "assessment for learning and timely, usable feedback"
  themes: [none]
  domain: none
  award: ["bachelor's with honours"]
  gradeOf: none
  paraphrase: "Assessment should be part of learning, helped by feedback on formative and summative work; feedback should come in good time and be usable, supporting development within a module and across the course."
  quote: full   # the issuer's statement is in `source` (D-std-0014)
  audience: practitioner
  subjects: inherited
- id: qaa/business-and-management-2023/3.20
  locator: { number: "3.20", headingPath: ["Content, structure and delivery", "Assessment"] }
  span: { start: 52741, end: 52949 }
  source: "While assessment methods need to be a reliable means of assessing the intended learning outcomes and be inclusive in design, they can be diverse, innovative and assist in developing skills in their own right."
  stem: none
  statementType: requirement
  rung: none
  force: must   # D-std-0016: "need to" read as must
  level: none
  appliesTo: "assessment methods"
  addressee: provider
  verbs: ["assessing", "developing"]
  about: "reliable, inclusive and varied assessment methods"
  themes: [none]
  domain: none
  award: ["bachelor's with honours"]
  gradeOf: none
  paraphrase: "Assessment methods need to assess the intended outcomes reliably and be inclusively designed (the issuer's 'need to', recorded as describes), and may also be varied, new and skill-building in themselves."
  quote: full   # the issuer's statement is in `source` (D-std-0014)
  audience: practitioner
  subjects: inherited
- id: qaa/business-and-management-2023/3.23
  locator: { number: "3.23", headingPath: ["Content, structure and delivery", "Assessment"] }
  span: { start: 53789, end: 54018 }
  source: "3.23 Where assessment is completed in groups, careful consideration should be given to the extent of group work in a course, to its authenticity and fit for the task assigned and the attribution of group versus individual marks.\n"
  stem: none
  statementType: requirement
  rung: none
  force: should
  level: none
  appliesTo: "group assessment"
  addressee: provider
  verbs: ["given"]
  about: "extent, fit and marking of group work"
  themes: [none]
  domain: none
  award: ["bachelor's with honours"]
  gradeOf: none
  paraphrase: "When assessment is done in groups, care should go into how much group work a course has, how authentic and suited to its task it is, and how marks are split between group and individual."
  quote: full   # the issuer's statement is in `source` (D-std-0014)
  audience: practitioner
  subjects: inherited
- id: qaa/business-and-management-2023/3.24
  locator: { number: "3.24", headingPath: ["Content, structure and delivery", "Assessment"] }
  span: { start: 54018, end: 54327 }
  source: "3.24 Peer review and assessment can play an important role in assessment and learning by promoting student engagement with their course. Whether undertaken for formative or summative purposes, clear guidance should be provided to students, and limits set on the weighting of peer assessment in a unit/module.\n"
  stem: none
  statementType: requirement
  rung: none
  force: should
  level: none
  appliesTo: "peer review and assessment"
  addressee: provider
  verbs: ["provided", "set"]
  about: "guidance and weighting limits for peer assessment"
  themes: [none]
  domain: none
  award: ["bachelor's with honours"]
  gradeOf: none
  paraphrase: "Peer review and assessment can engage students in assessment and learning; whether formative or summative, students should get clear guidance and the weight of peer marks in a unit or module should be capped."
  quote: full   # the issuer's statement is in `source` (D-std-0014)
  audience: practitioner
  subjects: inherited
- id: qaa/business-and-management-2023/3.25
  locator: { number: "3.25", headingPath: ["Content, structure and delivery", "Assessment"] }
  span: { start: 54327, end: 54596 }
  source: "3.25 Details of assessment should be transparent and shared with students along with the relevant marking criteria. There may also be opportunities for collaborative or participative approaches whereby students may co-design assessments with their tutors and/or peers.\n"
  stem: none
  statementType: requirement
  rung: none
  force: should
  level: none
  appliesTo: "assessment information"
  addressee: provider
  verbs: ["shared", "co-design"]
  about: "transparent assessment and shared marking criteria"
  themes: [none]
  domain: none
  award: ["bachelor's with honours"]
  gradeOf: none
  paraphrase: "Assessment details should be open and given to students with the marking criteria; students may also co-design assessments with tutors or peers."
  quote: full   # the issuer's statement is in `source` (D-std-0014)
  audience: practitioner
  subjects: inherited
- id: qaa/business-and-management-2023/3.26
  locator: { number: "3.26", headingPath: ["Content, structure and delivery", "Assessment"] }
  span: { start: 54596, end: 54670 }
  source: "3.26 Assessment should be designed with the student workload in mind.\n\n18\n"
  stem: none
  statementType: requirement
  rung: none
  force: should
  level: none
  appliesTo: "assessment design"
  addressee: provider
  verbs: ["designed"]
  about: "assessment designed with workload in mind"
  themes: [none]
  domain: none
  award: ["bachelor's with honours"]
  gradeOf: none
  paraphrase: "Assessment design should take account of how much work students carry."
  quote: full   # the issuer's statement is in `source` (D-std-0014)
  audience: practitioner
  subjects: inherited
- id: qaa/business-and-management-2023/4.2
  locator: { number: "4.2", headingPath: ["Benchmark standards", "Introduction"] }
  span: { start: 55218, end: 55702 }
  source: "4.2 The vast majority of students will perform significantly better than the minimum threshold standards. Each higher education provider has its own method of determining what appropriate evidence of this achievement will be and should refer to Annex D: Outcome classification descriptions for FHEQ Level 6 and FQHEIS Level 10 degrees. This Annex sets out common descriptions of the four main degree outcome classifications for bachelor's degrees with honours: 1st, 2.1, 2.2 and 3rd.\n"
  stem: none
  statementType: requirement
  rung: none
  force: should
  level: fheq:6
  appliesTo: "higher education providers"
  addressee: provider
  verbs: ["perform", "refer"]
  about: "most exceed threshold; refer to Annex D for degree classes"
  themes: [none]
  domain: none
  award: ["bachelor's with honours"]
  gradeOf: none
  paraphrase: "Most students will do much better than the minimum threshold; each provider decides what evidence shows achievement and should refer to Annex D, which describes the four honours classes (1st, 2.1, 2.2, 3rd) for FHEQ level 6 and FQHEIS level 10."
  quote: full   # the issuer's statement is in `source` (D-std-0014)
  audience: practitioner
  subjects: inherited
- id: qaa/business-and-management-2023/4.3
  locator: { number: "4.3", headingPath: ["Benchmark standards", "Introduction"] }
  span: { start: 55702, end: 56372 }
  source: "4.3 Three categories which differentiate graduate achievement have been identified, namely threshold, typical and excellent, and these standards are intended to reflect the performance of individual students. The standards are based upon the perceived national norms, operating across the business and management area. 'Threshold' describes the minimum to be achieved by all honours graduates, and it is expected that most students should achieve the 'Typical' standard. Paragraphs 4.5-4.7 seek to describe, particularly for the benefit of employing organisations, the capabilities that can be expected of graduates at ‘Threshold’, ‘Typical’ and ‘Excellent’ categories.\n"
  stem: none
  statementType: expectation
  rung: none
  force: should
  level: fheq:6
  appliesTo: "honours graduates of the subject"
  addressee: both
  verbs: ["differentiate", "achieve", "describe"]
  about: "threshold as minimum, typical as the expected norm"
  themes: [none]
  domain: none
  award: ["bachelor's with honours"]
  gradeOf: none
  paraphrase: "Three categories, threshold, typical and excellent, set apart graduates' achievement and rest on perceived national norms in the subject; threshold is the minimum for all honours graduates, and most students should reach typical."
  quote: full   # the issuer's statement is in `source` (D-std-0014)
  audience: both
  subjects: inherited
- id: qaa/business-and-management-2023/4.5.b1
  locator: { number: "4.5.b1", headingPath: ["Benchmark standards", "Threshold level"] }
  span: { start: 57000, end: 57155 }
  source: "knowledge and understanding: knowledge and understanding of the key areas of business and management, the relationships between these and their application"
  stem: "4.5"
  statementType: threshold
  rung: threshold
  force: will
  level: fheq:6
  appliesTo: "honours graduates at the threshold rung"
  addressee: learner
  verbs: []
  about: "key areas, their relationships and application"
  themes: [none]
  domain: knowledge
  award: ["bachelor's with honours"]
  gradeOf: none
  paraphrase: "Will have shown knowledge and understanding of the main areas of business and management, how they relate and how they are applied."
  quote: full   # the issuer's statement is in `source` (D-std-0014)
  audience: both
  subjects: inherited
- id: qaa/business-and-management-2023/4.5.b2
  locator: { number: "4.5.b2", headingPath: ["Benchmark standards", "Threshold level"] }
  span: { start: 57158, end: 57247 }
  source: "skills: competence within the range of subject-specific and generic skills and attributes"
  stem: "4.5"
  statementType: threshold
  rung: threshold
  force: will
  level: fheq:6
  appliesTo: "honours graduates at the threshold rung"
  addressee: learner
  verbs: []
  about: "competence across subject-specific and generic skills"
  themes: [none]
  domain: subject-skill
  award: ["bachelor's with honours"]
  gradeOf: none
  paraphrase: "Will have shown competence across the subject's own skills and its generic skills and attributes."
  quote: full   # the issuer's statement is in `source` (D-std-0014)
  audience: both
  subjects: inherited
- id: qaa/business-and-management-2023/4.5.b3
  locator: { number: "4.5.b3", headingPath: ["Benchmark standards", "Threshold level"] }
  span: { start: 57250, end: 57401 }
  source: "critical perspective: a view of business and management which is predominantly influenced by guided learning with some evidence of critical perspective"
  stem: "4.5"
  statementType: threshold
  rung: threshold
  force: will
  level: fheq:6
  appliesTo: "honours graduates at the threshold rung"
  addressee: learner
  verbs: ["influenced"]
  about: "a mainly guided view with some critical perspective"
  themes: [none]
  domain: understanding
  award: ["bachelor's with honours"]
  gradeOf: none
  paraphrase: "Will have shown a view of the subject shaped mostly by guided learning, with some sign of a critical stance."
  quote: full   # the issuer's statement is in `source` (D-std-0014)
  audience: both
  subjects: inherited
- id: qaa/business-and-management-2023/4.5.b4
  locator: { number: "4.5.b4", headingPath: ["Benchmark standards", "Threshold level"] }
  span: { start: 57404, end: 57505 }
  source: "application: the skills and abilities to apply knowledge in a contemporary organisational environment"
  stem: "4.5"
  statementType: threshold
  rung: threshold
  force: will
  level: fheq:6
  appliesTo: "honours graduates at the threshold rung"
  addressee: learner
  verbs: ["apply"]
  about: "applying knowledge in a current organisational setting"
  themes: [none]
  domain: subject-skill
  award: ["bachelor's with honours"]
  gradeOf: none
  paraphrase: "Will have shown the skills and abilities to use knowledge in a present-day organisational setting."
  quote: full   # the issuer's statement is in `source` (D-std-0014)
  audience: both
  subjects: inherited
- id: qaa/business-and-management-2023/4.5.b5
  locator: { number: "4.5.b5", headingPath: ["Benchmark standards", "Threshold level"] }
  span: { start: 57508, end: 57582 }
  source: "values: a capacity to practise the values of global social responsibility."
  stem: "4.5"
  statementType: threshold
  rung: threshold
  force: will
  level: fheq:6
  appliesTo: "honours graduates at the threshold rung"
  addressee: learner
  verbs: ["practise"]
  about: "practising global social responsibility"
  themes: [none]
  domain: generic-skill
  award: ["bachelor's with honours"]
  gradeOf: none
  paraphrase: "Will have shown the capacity to act on the values of global social responsibility."
  quote: full   # the issuer's statement is in `source` (D-std-0014)
  audience: both
  subjects: inherited
- id: qaa/business-and-management-2023/4.6.b1
  locator: { number: "4.6.b1", headingPath: ["Benchmark standards", "Typical level"] }
  span: { start: 57727, end: 57940 }
  source: "knowledge and understanding: a solid and substantial knowledge and understanding of the broad range of areas of business and management and the complex relationships between these and their application to practice"
  stem: "4.6"
  statementType: typical
  rung: typical
  force: will
  level: fheq:6
  appliesTo: "honours graduates at the typical rung"
  addressee: learner
  verbs: []
  about: "solid knowledge of a broad range and complex relationships"
  themes: [none]
  domain: knowledge
  award: ["bachelor's with honours"]
  gradeOf: { statement: qaa/business-and-management-2023/4.5.b1, basis: stated }
  paraphrase: "Will typically have shown solid, substantial knowledge and understanding across a broad range of business and management areas, the complex links between them and how they are applied in practice."
  quote: full   # the issuer's statement is in `source` (D-std-0014)
  audience: both
  subjects: inherited
- id: qaa/business-and-management-2023/4.6.b2
  locator: { number: "4.6.b2", headingPath: ["Benchmark standards", "Typical level"] }
  span: { start: 57943, end: 58043 }
  source: "skills: a command of subject-specific skills as well as proficiency in generic skills and attributes"
  stem: "4.6"
  statementType: typical
  rung: typical
  force: will
  level: fheq:6
  appliesTo: "honours graduates at the typical rung"
  addressee: learner
  verbs: []
  about: "command of subject skills, proficiency in generic skills"
  themes: [none]
  domain: subject-skill
  award: ["bachelor's with honours"]
  gradeOf: { statement: qaa/business-and-management-2023/4.5.b2, basis: stated }
  paraphrase: "Will typically have shown command of subject-specific skills and proficiency in generic skills and attributes."
  quote: full   # the issuer's statement is in `source` (D-std-0014)
  audience: both
  subjects: inherited
- id: qaa/business-and-management-2023/4.6.b3
  locator: { number: "4.6.b3", headingPath: ["Benchmark standards", "Typical level"] }
  span: { start: 58046, end: 58252 }
  source: "critical perspective: a view of business and management which is influenced by a wide range of appropriate learning sources, including evidence of an independent approach to learning and critical evaluation"
  stem: "4.6"
  statementType: typical
  rung: typical
  force: will
  level: fheq:6
  appliesTo: "honours graduates at the typical rung"
  addressee: learner
  verbs: ["influenced"]
  about: "a view drawn from wide sources, with independence and critical evaluation"
  themes: [none]
  domain: understanding
  award: ["bachelor's with honours"]
  gradeOf: { statement: qaa/business-and-management-2023/4.5.b3, basis: stated }
  paraphrase: "Will typically have shown a view of the subject drawn from a wide range of fitting sources, with evidence of independent learning and critical evaluation."
  quote: full   # the issuer's statement is in `source` (D-std-0014)
  audience: both
  subjects: inherited
- id: qaa/business-and-management-2023/4.6.b4
  locator: { number: "4.6.b4", headingPath: ["Benchmark standards", "Typical level"] }
  span: { start: 58255, end: 58582 }
  source: "application: the skills and abilities to apply knowledge in complex and contemporary organisational environments, and some capacity to develop and apply their own perspectives to their studies, to deal with uncertainty and complexity, to explore alternative solutions, to demonstrate critical evaluation and to integrate theory"
  stem: "4.6"
  statementType: typical
  rung: typical
  force: will
  level: fheq:6
  appliesTo: "honours graduates at the typical rung"
  addressee: learner
  verbs: ["apply", "develop", "deal", "explore", "demonstrate", "integrate"]
  about: "applying knowledge in complex settings, with own perspectives"
  themes: [none]
  domain: subject-skill
  award: ["bachelor's with honours"]
  gradeOf: { statement: qaa/business-and-management-2023/4.5.b4, basis: stated }
  paraphrase: "Will typically have shown the ability to use knowledge in complex, current organisational settings, and some capacity to form and use their own views, handle uncertainty and complexity, look at alternative answers, evaluate critically and bring theory in."
  quote: full   # the issuer's statement is in `source` (D-std-0014)
  audience: both
  subjects: inherited
- id: qaa/business-and-management-2023/4.6.b5
  locator: { number: "4.6.b5", headingPath: ["Benchmark standards", "Typical level"] }
  span: { start: 58585, end: 58660 }
  source: "values: an ability to integrate the values of global social responsibility."
  stem: "4.6"
  statementType: typical
  rung: typical
  force: will
  level: fheq:6
  appliesTo: "honours graduates at the typical rung"
  addressee: learner
  verbs: ["integrate"]
  about: "integrating global social responsibility"
  themes: [none]
  domain: generic-skill
  award: ["bachelor's with honours"]
  gradeOf: { statement: qaa/business-and-management-2023/4.5.b5, basis: stated }
  paraphrase: "Will typically have shown the ability to build the values of global social responsibility into their work."
  quote: full   # the issuer's statement is in `source` (D-std-0014)
  audience: both
  subjects: inherited
- id: qaa/business-and-management-2023/4.7.b1
  locator: { number: "4.7.b1", headingPath: ["Benchmark standards", "Excellent level"] }
  span: { start: 58792, end: 59001 }
  source: "knowledge and understanding: an advanced knowledge and critical understanding of a broad range of areas of business and management and the detailed relationships between these and their application to practice"
  stem: "4.7"
  statementType: excellent
  rung: excellent
  force: will
  level: fheq:6
  appliesTo: "honours graduates at the excellent rung"
  addressee: learner
  verbs: []
  about: "advanced, critical knowledge and detailed relationships"
  themes: [none]
  domain: knowledge
  award: ["bachelor's with honours"]
  gradeOf: { statement: qaa/business-and-management-2023/4.6.b1, basis: stated }
  paraphrase: "Will have shown advanced knowledge and critical understanding across a broad range of business and management areas, the detailed links between them and their application in practice."
  quote: full   # the issuer's statement is in `source` (D-std-0014)
  audience: both
  subjects: inherited
- id: qaa/business-and-management-2023/4.7.b2
  locator: { number: "4.7.b2", headingPath: ["Benchmark standards", "Excellent level"] }
  span: { start: 59004, end: 59115 }
  source: "skills: an excellent command of subject-specific skills as well as proficiency in generic skills and attributes"
  stem: "4.7"
  statementType: excellent
  rung: excellent
  force: will
  level: fheq:6
  appliesTo: "honours graduates at the excellent rung"
  addressee: learner
  verbs: []
  about: "excellent command of subject skills, proficiency in generic skills"
  themes: [none]
  domain: subject-skill
  award: ["bachelor's with honours"]
  gradeOf: { statement: qaa/business-and-management-2023/4.6.b2, basis: stated }
  paraphrase: "Will have shown excellent command of subject-specific skills and proficiency in generic skills and attributes."
  quote: full   # the issuer's statement is in `source` (D-std-0014)
  audience: both
  subjects: inherited
- id: qaa/business-and-management-2023/4.7.b3
  locator: { number: "4.7.b3", headingPath: ["Benchmark standards", "Excellent level"] }
  span: { start: 59118, end: 59356 }
  source: "critical perspective: a view of business and management which is influenced by analysis of a wide range of learning sources, based on a proactive and independent approach to learning; challenging assumptions and questioning the status quo"
  stem: "4.7"
  statementType: excellent
  rung: excellent
  force: will
  level: fheq:6
  appliesTo: "honours graduates at the excellent rung"
  addressee: learner
  verbs: ["influenced", "challenging", "questioning"]
  about: "a proactive, independent view that challenges assumptions"
  themes: [none]
  domain: understanding
  award: ["bachelor's with honours"]
  gradeOf: { statement: qaa/business-and-management-2023/4.6.b3, basis: stated }
  paraphrase: "Will have shown a view of the subject built from analysing wide sources, through proactive, independent learning that challenges assumptions and questions the status quo."
  quote: full   # the issuer's statement is in `source` (D-std-0014)
  audience: both
  subjects: inherited
- id: qaa/business-and-management-2023/4.7.b4
  locator: { number: "4.7.b4", headingPath: ["Benchmark standards", "Excellent level"] }
  span: { start: 59359, end: 59631 }
  source: "application: exceptional capacity to develop and apply their own perspectives to their studies, to deal with uncertainty and complexity, to explore alternative solutions, to demonstrate critical evaluation and to integrate theory and practice in a wide range of situations"
  stem: "4.7"
  statementType: excellent
  rung: excellent
  force: will
  level: fheq:6
  appliesTo: "honours graduates at the excellent rung"
  addressee: learner
  verbs: ["develop", "apply", "deal", "explore", "demonstrate", "integrate"]
  about: "exceptional own perspective and integration of theory and practice"
  themes: [none]
  domain: subject-skill
  award: ["bachelor's with honours"]
  gradeOf: { statement: qaa/business-and-management-2023/4.6.b4, basis: stated }
  paraphrase: "Will have shown exceptional ability to form and use their own views, handle uncertainty and complexity, look at alternative answers, evaluate critically and join theory with practice in many situations."
  quote: full   # the issuer's statement is in `source` (D-std-0014)
  audience: both
  subjects: inherited
- id: qaa/business-and-management-2023/4.7.b5
  locator: { number: "4.7.b5", headingPath: ["Benchmark standards", "Excellent level"] }
  span: { start: 59634, end: 59868 }
  source: "values: an ability to challenge assumptions, champion the values of global social responsibility while also appreciating the debates and potential contradictory views that this presents in complex business and management environments."
  stem: "4.7"
  statementType: excellent
  rung: excellent
  force: will
  level: fheq:6
  appliesTo: "honours graduates at the excellent rung"
  addressee: learner
  verbs: ["challenge", "champion", "appreciating"]
  about: "championing global social responsibility while weighing its debates"
  themes: [none]
  domain: generic-skill
  award: ["bachelor's with honours"]
  gradeOf: { statement: qaa/business-and-management-2023/4.6.b5, basis: stated }
  paraphrase: "Will have shown the ability to challenge assumptions and champion global social responsibility while recognising the debates and conflicting views it raises in complex business settings."
  quote: full   # the issuer's statement is in `source` (D-std-0014)
  audience: both
  subjects: inherited
```

### S4a Audience versions
<!-- label: both; status: drafted; basis: primary. forPractitioner: for the programme designer or teacher. forBeneficiary: for the student, second person, naming no issuer. author-agent-written: instructions to an AI agent writing about the statement (a course document, a handbook, an outcome, a report). author-agent-dialogue: instructions to an AI agent using the statement in conversation (with a student, a teacher or a programme team). Written fresh from the held text alone (benchmark rule 6; Abbott, 15:42). -->
```yaml
- statement: qaa/business-and-management-2023/1.3
  forPractitioner: { text: "Use the statement as a broad frame rather than a template: when you design or revise a course, the innovation, adaptability and variety typical of the subject should be kept.", rewrite: light, force: should, status: drafted }
  forBeneficiary: { text: "not-applicable: a duty on those who design courses; it sets no outcome for the student", rewrite: full, force: should, status: drafted }
  author-agent-written: "Describe this as an expectation (should) on course teams at bachelor's honours level: that innovation, adaptability and variety in course design be kept. Cite it as (QAA, 2023, Business and Management Subject Benchmark Statement, para 1.3) and read it with para 2.2, to which it points, and the design features in paras 2.1 to 2.6. Do not claim that it sets a curriculum or a regulatory rule."
  author-agent-dialogue: "Raise it with a programme team that worries the statement will force a standard course. Put it as both permission and expectation: their course should stay distinctive. Ask what makes the course different and whether a planned change would remove that. Do not bring it to students as something they have to meet."
- statement: qaa/business-and-management-2023/1.8
  forPractitioner: { text: "Read skills and attributes as transferable academic and professional skills: they serve a business career and any other, and they will ready students to act effectively and responsibly at work, as leaders and as global citizens.", rewrite: light, force: will, status: drafted }
  forBeneficiary: { text: "You will build academic and professional skills that carry over to any career, not only business, and that ready you to be an effective, responsible employee, colleague, leader and citizen of the world.", rewrite: full, force: will, status: drafted }
  author-agent-written: "Present this as a stated expectation (will) for honours graduates at FHEQ level 6: the subject's skills transfer beyond business careers. Cite it as (QAA, 2023, Business and Management Subject Benchmark Statement, para 1.8) and set it beside the generic skills in paras 3.11.b1 to 3.11.b7 and the employment qualities in qaa/fheq-2024/4.15.b9.1 to 4.15.b9.3. Do not claim that every graduate goes into business or management, which the paragraph itself rules out."
  author-agent-dialogue: "Bring it up when a student doubts the degree's worth outside business, or when staff plan careers support. Tell a student plainly that these skills travel, then ask which two skills they would point to for a role outside business. Avoid suggesting the degree leads only to management jobs."
- statement: qaa/business-and-management-2023/1.9
  forPractitioner: { text: "Decide how your course weights the four purposes in 1.4, noting any professional recognition that shapes it, and make that weighting explainable and visible in its specified learning outcomes.", rewrite: light, force: should, status: drafted }
  forBeneficiary: { text: "not-applicable: a duty on the course team in writing outcomes", rewrite: full, force: should, status: drafted }
  author-agent-written: "Describe this as an expectation (should) on each honours course: the mix of purposes it delivers should be explainable through its learning outcomes. Cite it as (QAA, 2023, Business and Management Subject Benchmark Statement, para 1.9) and set it beside the purposes listed in paras 1.4.b1 to 1.4.b4. Do not claim the statement fixes the balance; it leaves the mix to the course and asks only that it be shown."
  author-agent-dialogue: "Raise it when a programme team writes or revises its learning outcomes. Ask which of the purposes in 1.4 the course leans towards, and where in the outcomes a reader could see that. Keep it for staff; it is a design duty, not a student standard."
- statement: qaa/business-and-management-2023/1.10
  forPractitioner: { text: "Keep the course broad: it should give students insight into a wide spread of business areas, drawing on varied content and disciplines so that what they learn carries into many settings.", rewrite: light, force: should, status: drafted }
  forBeneficiary: { text: "Your course should give you a view across many areas of business, not just one, so that what you learn can be used in many settings.", rewrite: full, force: should, status: drafted }
  author-agent-written: "Describe this as an expectation (should) that an honours course in the subject gives insight across many business areas. Cite it as (QAA, 2023, Business and Management Subject Benchmark Statement, para 1.10) and set it beside the area list in paras 3.7.b1 to 3.7.b10 and the scope note in para 1.2. Do not claim it bars a course with a particular emphasis; para 2.1 allows that."
  author-agent-dialogue: "Raise it when a student asks why they study areas outside their interest, or when staff narrow a course. For a student, explain that breadth is part of the subject and ask which area outside their favourite has surprised them. For staff, ask which business areas the course leaves out. Avoid treating breadth as a list of compulsory modules."
- statement: qaa/business-and-management-2023/1.13
  forPractitioner: { text: "Design the course as a broad base: students will be ready for varied careers and roles in many kinds of organisation, and the course may also lead to specialist postgraduate study.", rewrite: light, force: will, status: drafted }
  forBeneficiary: { text: "Your studies will give you a broad base for many kinds of career and role, in many kinds of organisation, and may lead on to postgraduate study in a specialism.", rewrite: full, force: will, status: drafted }
  author-agent-written: "State it as an expectation (will) about honours graduates at FHEQ level 6: a broad base for many careers, with further study possible (may). Cite it as (QAA, 2023, Business and Management Subject Benchmark Statement, para 1.13) and set it beside para 2.7 on readiness for postgraduate study and qaa/fheq-2024/4.15.b9.3. Do not turn the 'may' about postgraduate study into a promise."
  author-agent-dialogue: "Bring it up when a student is unsure where the degree leads. Ask them which kinds of organisation they could picture working in, and whether a specialist master's appeals. Avoid promising entry to further study, which each institution decides."
- statement: qaa/business-and-management-2023/1.15
  forPractitioner: { text: "Treat EDI as more than legal compliance: it should be a real presence in how the subject is taught and practised, attentive to intersecting identities among students and staff.", rewrite: light, force: should, status: drafted }
  forBeneficiary: { text: "not-applicable: a duty on the subject community and course teams", rewrite: full, force: should, status: drafted }
  author-agent-written: "Describe this as an expectation (should) on the subject community and its course teams: EDI built into culture and practice, not only met as a legal duty. Cite it as (QAA, 2023, Business and Management Subject Benchmark Statement, para 1.15) and set it beside paras 1.18, 1.19 and 1.21, which say what is taught, how it is taught and how it is reviewed. Do not present it as a student outcome or as a legal requirement in its own right."
  author-agent-dialogue: "Raise it with a programme team reviewing culture, curriculum or teaching. Ask where EDI shows in day-to-day practice beyond policy, and whose differences the course has not yet noticed. Do not hand it to a student as a standard they must meet."
- statement: qaa/business-and-management-2023/1.17
  forPractitioner: { text: "Teach the subject so that EDI and reflective practice prepare students to work in a diverse, global world and to help organisations reduce inequality; the study will instil EDI principles in those who go on to manage and lead.", rewrite: light, force: will, status: drafted }
  forBeneficiary: { text: "Your studies will build equality, diversity and inclusion into how you manage and lead, so that you can help organisations reduce inequality and do well in a diverse, global world.", rewrite: full, force: will, status: drafted }
  author-agent-written: "Present this as an expected outcome (will) of honours study at FHEQ level 6: EDI principles held by future managers and leaders. Cite it as (QAA, 2023, Business and Management Subject Benchmark Statement, para 1.17), noting its link to responsible leadership in para 1.6, and set it beside paras 3.10.b1 and 3.11.b3 and the decision-making quality in qaa/fheq-2024/4.15.b9.2. Do not claim it is a measured rung outcome; it states why the subject is taught."
  author-agent-dialogue: "Raise it when a student asks why EDI appears in a business degree, or when staff link teaching to the SDGs. With a student, ask how they would make a team they led more inclusive. Avoid lecturing; let the student connect it to work they know."
- statement: qaa/business-and-management-2023/1.18
  forPractitioner: { text: "Teach a critical understanding of organisations' role in EDI; graduates should know anti-discrimination law and be able to foster inclusive workplaces; and the course content should be diverse, question dominant approaches and use cases that reflect the cohort and society.", rewrite: light, force: should, status: drafted }
  forBeneficiary: { text: "You should come to understand the law against discrimination and gain the knowledge and skills to build inclusive workplaces; your course should also show you a wide range of perspectives and question the dominant ways the subject has been taught.", rewrite: full, force: should, status: drafted }
  author-agent-written: "Describe this as an expectation (should) at honours level with two parts: what graduates should know and be able to do on EDI, and what course content should offer. Cite it as (QAA, 2023, Business and Management Subject Benchmark Statement, para 1.18) and set it beside para 3.7.b5 (people and organisational behaviour), para 3.10.b1 and the level 6 understanding in qaa/fheq-2024/4.15.b1. Do not claim the course alone must satisfy legal compliance training; the text asks for awareness and capability."
  author-agent-dialogue: "Raise it when a student asks what they should know about inclusion at work, or when a team reviews reading lists and cases. Ask a student whether they could explain an employer's duty not to discriminate and name one way to make a workplace more inclusive; ask staff whose voices their cases leave out. Avoid reading the paragraph out; choose the part that fits the person."
- statement: qaa/business-and-management-2023/1.19
  forPractitioner: { text: "Design the course so students from all backgrounds can succeed and feel included; choose modes of learning and assessment designs with their different opportunities and barriers in mind, and let teaching approaches draw on the cohort's diversity.", rewrite: light, force: should, status: drafted }
  forBeneficiary: { text: "not-applicable: a duty on course design and teaching", rewrite: full, force: should, status: drafted }
  author-agent-written: "Describe this as a provider expectation (should) for honours courses: inclusive design, inclusive teaching and assessment, and careful choice of learning mode. Cite it as (QAA, 2023, Business and Management Subject Benchmark Statement, para 1.19) and set it beside paras 1.22 to 1.24 on accessibility and para 3.19 on inclusive assessment. Do not present it as a student outcome."
  author-agent-dialogue: "Raise it when a team chooses delivery modes or redesigns assessment. Ask which students a planned mode would help and which it would hinder, and what assessment choice would widen success. Keep it for staff; a student meets its effect, not the duty."
- statement: qaa/business-and-management-2023/1.21
  forPractitioner: { text: "Build EDI into regular course review: reflect on how to strengthen it, involve students as partners where possible, and consider an equality impact assessment when approving changes.", rewrite: light, force: should, status: drafted }
  forBeneficiary: { text: "not-applicable: a duty on course teams; students may take part as partners", rewrite: full, force: should, status: drafted }
  author-agent-written: "Describe this as an expectation (should) on course teams: regular reflection on EDI, with students where possible. Cite it as (QAA, 2023, Business and Management Subject Benchmark Statement, para 1.21) and set it beside para 2.17 on monitoring and review. Do not state that an equality impact assessment is required; the text says it can be considered."
  author-agent-dialogue: "Raise it at annual review or course approval. Ask when the team last looked at EDI in the course and which students took part. Avoid giving students the duty itself; invite them only as partners."
- statement: qaa/business-and-management-2023/1.22
  forPractitioner: { text: "Make accessibility at least compliant with regulation and apply it end to end: pre-application information, teaching, assessment, graduation and beyond.", rewrite: light, force: should, status: drafted }
  forBeneficiary: { text: "not-applicable: a duty on the provider; the student meets its effect", rewrite: full, force: should, status: drafted }
  author-agent-written: "Describe this as a provider expectation (should, with will for its reach) that accessibility meets regulatory requirements at minimum and runs through every stage of the course. Cite it as (QAA, 2023, Business and Management Subject Benchmark Statement, para 1.22) and set it beside paras 1.23, 1.24 and 3.19. Do not present the paragraph's examples as required actions; they are given as what accessibility may include."
  author-agent-dialogue: "Raise it when a team reviews information, spaces, resources or assessment. Ask where in the student journey, from applying to graduating, access is weakest. Do not put this duty to a student; if a student raises a barrier, point them to support."
- statement: qaa/business-and-management-2023/1.24
  forPractitioner: { text: "Check that placements, work-based learning and study abroad are open to every student on equal terms, and that digital provision is inclusive and accessible.", rewrite: light, force: should, status: drafted }
  forBeneficiary: { text: "not-applicable: a duty on the provider; the student meets its effect", rewrite: full, force: should, status: drafted }
  author-agent-written: "Describe this as a provider expectation (should) that work-based, international and digital learning are open to all students alike. Cite it as (QAA, 2023, Business and Management Subject Benchmark Statement, para 1.24) and set it beside paras 1.22 and 2.14 on partnerships and placements. Do not present it as a student standard."
  author-agent-dialogue: "Raise it when a team plans placements, study abroad or online delivery. Ask which students might be unable to take up a placement or trip, and what would change that. Keep the duty with staff."
- statement: qaa/business-and-management-2023/1.26
  forPractitioner: { text: "Weave sustainability through the curriculum, in every functional area rather than one module, covering its economic, social and environmental sides.", rewrite: light, force: must, status: drafted }
  forBeneficiary: { text: "not-applicable: a duty on curriculum design", rewrite: full, force: must, status: drafted }
  author-agent-written: "Describe this as a curriculum expectation stated with 'needs to', recorded here as describes because the word is outside the five modals. Cite it as (QAA, 2023, Business and Management Subject Benchmark Statement, para 1.26) and set it beside paras 1.25, 1.27, 1.28 and the area in para 3.7.b1, and the guidance std:doc:qaa-advancehe-esd-2021-guidance. Do not claim the example topics listed after it are required; the text calls the list not exhaustive."
  author-agent-dialogue: "Raise it when a team maps where sustainability sits in the course. Ask which functional modules, such as finance or operations, touch it at all. Do not give it to students as a duty."
- statement: qaa/business-and-management-2023/2.7
  forPractitioner: { text: "Plan each level so attainment builds towards the threshold standards at FHEQ level 6 (FQHEIS level 10); students at typical or above would be expected to be ready for further study in the subject or a cognate one.", rewrite: light, force: will, status: drafted }
  forBeneficiary: { text: "You will move up level by level, building towards at least the minimum standard for your honours degree; if you reach the typical standard or higher, you should be ready for postgraduate study, though each institution sets its own entry rules.", rewrite: full, force: will, status: drafted }
  author-agent-written: "Present this as an expectation (will, with 'it is expected') on progression through an honours degree at FHEQ level 6 and FQHEIS level 10, as the paragraph states both. Cite it as (QAA, 2023, Business and Management Subject Benchmark Statement, para 2.7) and set it beside the rungs in paras 4.5 to 4.7 and qaa/fheq-2024/4.15. Do not claim it guarantees postgraduate entry; the text leaves entry to each provider."
  author-agent-dialogue: "Raise it when a student asks how their current level relates to the final degree or to a master's. Ask where they think they sit now against the minimum and the typical standard. Avoid presenting the typical standard as the pass mark."
- statement: qaa/business-and-management-2023/2.8
  forPractitioner: { text: "On joint and combined routes, ensure students will still reach the core specific and generic skills of the subject, and use the overlap with the second subject for interdisciplinary work.", rewrite: light, force: will, status: drafted }
  forBeneficiary: { text: "If you study business and management alongside another subject, you will still gain its core skills, add skills from your other subject and may explore where the two meet.", rewrite: full, force: will, status: drafted }
  author-agent-written: "Present this as an expectation (will) for joint, combined and major-minor honours routes at FHEQ level 6: the core of the subject's skills is still reached. Cite it as (QAA, 2023, Business and Management Subject Benchmark Statement, para 2.8) and set it beside paras 3.10 and 3.11. Do not claim joint students must meet every item of the single-subject lists; the text says core elements."
  author-agent-dialogue: "Raise it when a joint-honours student worries they are missing out, or a team designs a joint route. Ask which core skills the route secures and which come from the other subject. Avoid implying a joint degree is a lesser award."
- statement: qaa/business-and-management-2023/2.18
  forPractitioner: { text: "Include external reviewers in periodic review so that proposed changes get an outside view and threshold standards and content are confirmed.", rewrite: light, force: will, status: drafted }
  forBeneficiary: { text: "not-applicable: a duty on the provider in review", rewrite: full, force: will, status: drafted }
  author-agent-written: "Describe this as a provider expectation (will) about periodic review. Cite it as (QAA, 2023, Business and Management Subject Benchmark Statement, para 2.18) and set it beside paras 2.17 and 2.19 on review and external examining. Do not present it as a student outcome."
  author-agent-dialogue: "Raise it with a team preparing periodic review. Ask who their external reviewer is and what they will be asked to confirm about threshold standards. Keep it with staff."
- statement: qaa/business-and-management-2023/3.2
  forPractitioner: { text: "Graduates should be able to show they know and understand a range of organisations, their environment and governance; teach the changing nature of work, risk and organisations' impact on society.", rewrite: light, force: should, status: drafted }
  forBeneficiary: { text: "You should be able to show that you know and understand many kinds of organisation, the wider business world and communities around them, and how they are run and governed, including risk and their effect on society.", rewrite: full, force: should, status: drafted }
  author-agent-written: "State it as an outcome graduates should reasonably be expected to show at FHEQ level 6 (FQHEIS level 10): knowledge of organisations, environment and governance. Cite it as (QAA, 2023, Business and Management Subject Benchmark Statement, para 3.2) and set it beside the areas in paras 3.4 to 3.7 and qaa/fheq-2024/4.15.b1. Do not claim it holds at a lower level of study or as a standalone module."
  author-agent-dialogue: "Raise it when a student asks what they should know by the end of the degree. Ask them to name an organisation unlike the ones they know best and explain how it is governed. Avoid reading out the paragraph; use one example."
- statement: qaa/business-and-management-2023/3.3
  forPractitioner: { text: "Build integration across areas into the course and its assessment; successful graduates from every mode should be able to show it.", rewrite: light, force: should, status: drafted }
  forBeneficiary: { text: "You should be able to show how the different areas of business you study connect and work together, whichever way you study.", rewrite: full, force: should, status: drafted }
  author-agent-written: "Describe this as an outcome (should) for successful honours graduates at FHEQ level 6 in every mode of study: integration across areas. Cite it as (QAA, 2023, Business and Management Subject Benchmark Statement, para 3.3) and set it beside the rung items on relationships between areas, paras 4.5.b1, 4.6.b1 and 4.7.b1. Do not claim it applies only to full-time or in-person students."
  author-agent-dialogue: "Raise it when a student treats modules as separate boxes, or a team plans synoptic assessment. Ask the student how a decision in marketing would affect finance or operations. Avoid making integration sound like an extra topic."
- statement: qaa/business-and-management-2023/3.7.b1
  forPractitioner: { text: "Graduates should be able to show and critically evaluate responsible management and ethical conduct across social, cultural, legal, economic and environmental issues.", rewrite: light, force: should, status: drafted }
  forBeneficiary: { text: "You should be able to show you understand, and can critically judge, what it means to manage responsibly and act ethically on social, cultural, legal, economic and environmental questions.", rewrite: full, force: should, status: drafted }
  author-agent-written: "Treat this as a knowledge area in which honours graduates should be able to show knowledge, understanding and critical evaluation at FHEQ level 6 (FQHEIS level 10): ethics, responsibility and sustainability. Cite it as (QAA, 2023, Business and Management Subject Benchmark Statement, para 3.7), naming the area. Do not claim every course must teach it as a separate module, or that it holds below honours level. Set it beside paras 1.25 to 1.28 and the level 6 knowledge descriptors qaa/fheq-2024/4.15.b1 and qaa/fqheis-2024/4.16.b2."
  author-agent-dialogue: "Raise it when a student or a team asks what a broad business degree should cover in ethics, responsibility and sustainability. With a student, ask: what would a responsible choice look like in a decision you have studied? With staff, ask where this area is taught and assessed. Avoid reading the whole list aloud; take the one area in question."
- statement: qaa/business-and-management-2023/3.7.b2
  forPractitioner: { text: "Graduates should be able to show and critically evaluate how markets develop and operate, with market failure, externalities and fair trade.", rewrite: light, force: should, status: drafted }
  forBeneficiary: { text: "You should be able to show you understand how markets for resources, goods and services grow and work, including when they fail, their side effects and fair trade.", rewrite: full, force: should, status: drafted }
  author-agent-written: "Treat this as a knowledge area in which honours graduates should be able to show knowledge, understanding and critical evaluation at FHEQ level 6 (FQHEIS level 10): markets and economies. Cite it as (QAA, 2023, Business and Management Subject Benchmark Statement, para 3.7), naming the area. Do not claim every course must teach it as a separate module, or that it holds below honours level. Set it beside para 3.4 on the business environment and the level 6 knowledge descriptors qaa/fheq-2024/4.15.b1 and qaa/fqheis-2024/4.16.b2."
  author-agent-dialogue: "Raise it when a student or a team asks what a broad business degree should cover in markets and economies. With a student, ask: can you explain one market failure and who bears its cost? With staff, ask where this area is taught and assessed. Avoid reading the whole list aloud; take the one area in question."
- statement: qaa/business-and-management-2023/3.7.b3
  forPractitioner: { text: "Graduates should be able to show and critically evaluate customer relationship management, consumer behaviour, segmentation, targeting and positioning, sales and product and service innovation.", rewrite: light, force: should, status: drafted }
  forBeneficiary: { text: "You should be able to show you understand, and can judge critically, how organisations manage customers, how consumers behave, how markets are segmented and targeted, how sales are made and why products need innovation.", rewrite: full, force: should, status: drafted }
  author-agent-written: "Treat this as a knowledge area in which honours graduates should be able to show knowledge, understanding and critical evaluation at FHEQ level 6 (FQHEIS level 10): marketing, sales, negotiation and customers. Cite it as (QAA, 2023, Business and Management Subject Benchmark Statement, para 3.7), naming the area. Do not claim every course must teach it as a separate module, or that it holds below honours level. Set it beside paras 3.10.b4 (commercial acumen) and 3.10.b7 (networking) and the level 6 knowledge descriptors qaa/fheq-2024/4.15.b1 and qaa/fqheis-2024/4.16.b2."
  author-agent-dialogue: "Raise it when a student or a team asks what a broad business degree should cover in marketing, sales, negotiation and customers. With a student, ask: how would you decide which customers a product is for? With staff, ask where this area is taught and assessed. Avoid reading the whole list aloud; take the one area in question."
- statement: qaa/business-and-management-2023/3.7.b4
  forPractitioner: { text: "Graduates should be able to show and critically evaluate where finance comes from and how it is managed, and how accounting and information systems serve planning, control, decisions and financial risk.", rewrite: light, force: should, status: drafted }
  forBeneficiary: { text: "You should be able to show you understand where money for an organisation comes from, how it is managed, and how accounts and information systems help plan, control, decide and manage financial risk.", rewrite: full, force: should, status: drafted }
  author-agent-written: "Treat this as a knowledge area in which honours graduates should be able to show knowledge, understanding and critical evaluation at FHEQ level 6 (FQHEIS level 10): finance and accounting. Cite it as (QAA, 2023, Business and Management Subject Benchmark Statement, para 3.7), naming the area. Do not claim every course must teach it as a separate module, or that it holds below honours level. Set it beside para 3.10.b6 (numeracy) and the level 6 knowledge descriptors qaa/fheq-2024/4.15.b1 and qaa/fqheis-2024/4.16.b2."
  author-agent-dialogue: "Raise it when a student or a team asks what a broad business degree should cover in finance and accounting. With a student, ask: what would the accounts tell you about the risk in a decision? With staff, ask where this area is taught and assessed. Avoid reading the whole list aloud; take the one area in question."
- statement: qaa/business-and-management-2023/3.7.b5
  forPractitioner: { text: "Graduates should be able to show and critically evaluate inclusive, ethical leadership, people management and development, engagement and the legal context, with cross-cultural and EDI understanding.", rewrite: light, force: should, status: drafted }
  forBeneficiary: { text: "You should be able to show you understand, and can judge critically, how people are led, managed and developed in organisations, how staff are engaged, what the law requires, and how culture and inclusion shape this.", rewrite: full, force: should, status: drafted }
  author-agent-written: "Treat this as a knowledge area in which honours graduates should be able to show knowledge, understanding and critical evaluation at FHEQ level 6 (FQHEIS level 10): people and organisational behaviour. Cite it as (QAA, 2023, Business and Management Subject Benchmark Statement, para 3.7), naming the area. Do not claim every course must teach it as a separate module, or that it holds below honours level. Set it beside paras 1.6 and 1.15 to 1.20, to which the item points and the level 6 knowledge descriptors qaa/fheq-2024/4.15.b1 and qaa/fqheis-2024/4.16.b2."
  author-agent-dialogue: "Raise it when a student or a team asks what a broad business degree should cover in people and organisational behaviour. With a student, ask: how would you keep a diverse team engaged? With staff, ask where this area is taught and assessed. Avoid reading the whole list aloud; take the one area in question."
- statement: qaa/business-and-management-2023/3.7.b6
  forPractitioner: { text: "Graduates should be able to show and critically evaluate operations: resources, supply chain, procurement, logistics, outsourcing, quality, service and project management.", rewrite: light, force: should, status: drafted }
  forBeneficiary: { text: "You should be able to show you understand, and can judge critically, how organisations manage resources, supply chains, buying, logistics, outsourcing, quality, service and projects.", rewrite: full, force: should, status: drafted }
  author-agent-written: "Treat this as a knowledge area in which honours graduates should be able to show knowledge, understanding and critical evaluation at FHEQ level 6 (FQHEIS level 10): operations and business innovation. Cite it as (QAA, 2023, Business and Management Subject Benchmark Statement, para 3.7), naming the area. Do not claim every course must teach it as a separate module, or that it holds below honours level. Set it beside para 1.26.b1 (sustainable supply chains, as an example topic) and the level 6 knowledge descriptors qaa/fheq-2024/4.15.b1 and qaa/fqheis-2024/4.16.b2."
  author-agent-dialogue: "Raise it when a student or a team asks what a broad business degree should cover in operations and business innovation. With a student, ask: where would you look first to improve how an organisation delivers its service? With staff, ask where this area is taught and assessed. Avoid reading the whole list aloud; take the one area in question."
- statement: qaa/business-and-management-2023/3.7.b7
  forPractitioner: { text: "Graduates should be able to show and critically evaluate data analytics, statistics, digital business and information systems, their organisational impact and data-driven decision-making.", rewrite: light, force: should, status: drafted }
  forBeneficiary: { text: "You should be able to show you understand, and can judge critically, how data, statistics and information systems are used in business and how they help organisations make decisions.", rewrite: full, force: should, status: drafted }
  author-agent-written: "Treat this as a knowledge area in which honours graduates should be able to show knowledge, understanding and critical evaluation at FHEQ level 6 (FQHEIS level 10): data analytics, digital business and information systems. Cite it as (QAA, 2023, Business and Management Subject Benchmark Statement, para 3.7), naming the area. Do not claim every course must teach it as a separate module, or that it holds below honours level. Set it beside paras 3.10.b3 (research), 3.10.b6 (numeracy) and 3.11.b4 (digital literacy) and the level 6 knowledge descriptors qaa/fheq-2024/4.15.b1 and qaa/fqheis-2024/4.16.b2."
  author-agent-dialogue: "Raise it when a student or a team asks what a broad business degree should cover in data analytics, digital business and information systems. With a student, ask: what data would you want before making a decision in your project? With staff, ask where this area is taught and assessed. Avoid reading the whole list aloud; take the one area in question."
- statement: qaa/business-and-management-2023/3.7.b8
  forPractitioner: { text: "Graduates should be able to show and critically evaluate how policies and strategies are developed for changing environments, with risk, crisis, continuity and communication methods.", rewrite: light, force: should, status: drafted }
  forBeneficiary: { text: "You should be able to show you understand, and can judge critically, how organisations set policy and strategy in a changing world, manage risk and crises, keep going through disruption and communicate their plans.", rewrite: full, force: should, status: drafted }
  author-agent-written: "Treat this as a knowledge area in which honours graduates should be able to show knowledge, understanding and critical evaluation at FHEQ level 6 (FQHEIS level 10): business policy and strategy. Cite it as (QAA, 2023, Business and Management Subject Benchmark Statement, para 3.7), naming the area. Do not claim every course must teach it as a separate module, or that it holds below honours level. Set it beside para 3.2 on risk and para 3.4 on the business environment and the level 6 knowledge descriptors qaa/fheq-2024/4.15.b1 and qaa/fqheis-2024/4.16.b2."
  author-agent-dialogue: "Raise it when a student or a team asks what a broad business degree should cover in business policy and strategy. With a student, ask: how would a strategy you know change if a crisis hit? With staff, ask where this area is taught and assessed. Avoid reading the whole list aloud; take the one area in question."
- statement: qaa/business-and-management-2023/3.7.b9
  forPractitioner: { text: "Graduates should be able to show and critically evaluate public and non-profit management: governance, finance, leadership, empowerment, coproduction, public values and hybrid service delivery.", rewrite: light, force: should, status: drafted }
  forBeneficiary: { text: "You should be able to show you understand, and can judge critically, how public services and voluntary and community organisations are run, funded, led and governed, and how they work with communities.", rewrite: full, force: should, status: drafted }
  author-agent-written: "Treat this as a knowledge area in which honours graduates should be able to show knowledge, understanding and critical evaluation at FHEQ level 6 (FQHEIS level 10): public and non-profit management. Cite it as (QAA, 2023, Business and Management Subject Benchmark Statement, para 3.7), naming the area. Do not claim every course must teach it as a separate module, or that it holds below honours level. Set it beside para 1.5 on organisations read broadly and para 2.5 and the level 6 knowledge descriptors qaa/fheq-2024/4.15.b1 and qaa/fqheis-2024/4.16.b2."
  author-agent-dialogue: "Raise it when a student or a team asks what a broad business degree should cover in public and non-profit management. With a student, ask: how does running a charity differ from running a company? With staff, ask where this area is taught and assessed. Avoid reading the whole list aloud; take the one area in question."
- statement: qaa/business-and-management-2023/3.7.b10
  forPractitioner: { text: "Graduates should be able to show and critically evaluate how new ventures, products and services are created for financial or social return, including intellectual property.", rewrite: light, force: should, status: drafted }
  forBeneficiary: { text: "You should be able to show you understand, and can judge critically, how new business ideas become products, services or organisations that pay back financially or socially, and why intellectual property matters.", rewrite: full, force: should, status: drafted }
  author-agent-written: "Treat this as a knowledge area in which honours graduates should be able to show knowledge, understanding and critical evaluation at FHEQ level 6 (FQHEIS level 10): entrepreneurship and enterprise development. Cite it as (QAA, 2023, Business and Management Subject Benchmark Statement, para 3.7), naming the area. Do not claim every course must teach it as a separate module, or that it holds below honours level. Set it beside paras 1.29 to 1.33, para 3.10.b5 and std:doc:qaa-enterprise-2018-guidance, and the level 6 descriptor qaa/fheq-2024/4.15.b1."
  author-agent-dialogue: "Raise it when a student is thinking about a venture or a team plans enterprise teaching. With a student, ask: who would pay for your idea, and what part of it could you protect? With staff, ask where this area is taught and assessed. Avoid treating it as only for students who want to start a business."
- statement: qaa/business-and-management-2023/3.9
  forPractitioner: { text: "Graduates should be able to show intellectual skills and business competencies, and personal and interpersonal skills; plan for subject-specific and generic skills alike (listed in 3.10 and 3.11).", rewrite: light, force: should, status: drafted }
  forBeneficiary: { text: "You should be able to show thinking skills and business competencies, and personal and interpersonal skills, both specific to business and useful anywhere.", rewrite: full, force: should, status: drafted }
  author-agent-written: "Describe this as an outcome (should) for honours graduates at FHEQ level 6: the skill set that paras 3.10 and 3.11 then list. Cite it as (QAA, 2023, Business and Management Subject Benchmark Statement, para 3.9) and set it beside the rung items on skills, paras 4.5.b2, 4.6.b2 and 4.7.b2, and qaa/fheq-2024/4.15.b6 to 4.15.b9.3. Do not claim each listed skill is a separate threshold requirement; the lists name skills, the rungs set the standard."
  author-agent-dialogue: "Raise it when a student is mapping their skills for a placement or CV. Ask them to sort their skills into business-specific and general, and to give one example of each. Avoid presenting the lists in 3.10 and 3.11 as a checklist they must tick off."
- statement: qaa/business-and-management-2023/3.10.b1
  forPractitioner: { text: "Develop people management: communication, team building, resilience and well-being, leading and motivating others, and nurturing EDI.", rewrite: light, force: describes, status: drafted }
  forBeneficiary: { text: "You develop skills in managing people: communicating, building teams, looking after resilience and well-being, leading and motivating others, and making teams inclusive.", rewrite: full, force: describes, status: drafted }
  author-agent-written: "Present this as a skill of particular relevance to the subject (people management), which the list describes and para 3.9 says graduates should be able to show, at honours level FHEQ 6. Cite it as (QAA, 2023, Business and Management Subject Benchmark Statement, para 3.10), naming the skill. Do not claim it is a threshold requirement on its own; set it beside paras 3.7.b5 and 1.18, and the employment qualities in qaa/fheq-2024/4.15.b9.1."
  author-agent-dialogue: "Raise it when a student reflects on people management or a team plans where it is developed. Ask: when did you last motivate someone, and what worked? Avoid reading the list out or treating it as a checklist."
- statement: qaa/business-and-management-2023/3.10.b2
  forPractitioner: { text: "Develop problem-solving and critical analysis: diagnosing causes from facts and circumstances, then deciding on sustainable solutions.", rewrite: light, force: describes, status: drafted }
  forBeneficiary: { text: "You develop skills in solving problems and analysing critically: working out what caused a problem, making decisions and choosing sustainable solutions.", rewrite: full, force: describes, status: drafted }
  author-agent-written: "Present this as a skill of particular relevance to the subject (problem-solving and critical analysis), which the list describes and para 3.9 says graduates should be able to show, at honours level FHEQ 6. Cite it as (QAA, 2023, Business and Management Subject Benchmark Statement, para 3.10), naming the skill. Do not claim it is a threshold requirement on its own; set it beside qaa/fheq-2024/4.15.b3.1 and 4.15.b7 and Annex D qaa/fheq-2024/annex-d/cognitive/r3/3rd."
  author-agent-dialogue: "Raise it when a student reflects on problem-solving and critical analysis or a team plans where it is developed. Ask: how did you find the real cause of a problem you faced? Avoid reading the list out or treating it as a checklist."
- statement: qaa/business-and-management-2023/3.10.b3
  forPractitioner: { text: "Develop research skills: analysing and evaluating data, sources and methods, with strong digital literacy, and applying findings to responsible, ethical, evidence-based decisions.", rewrite: light, force: describes, status: drafted }
  forBeneficiary: { text: "You develop research skills: analysing and weighing up data, sources and methods, using digital tools well, and basing responsible, ethical decisions on the evidence.", rewrite: full, force: describes, status: drafted }
  author-agent-written: "Present this as a skill of particular relevance to the subject (research), which the list describes and para 3.9 says graduates should be able to show, at honours level FHEQ 6. Cite it as (QAA, 2023, Business and Management Subject Benchmark Statement, para 3.10), naming the skill. Do not claim it requires a dissertation; set it beside para 3.7.b7, qaa/fheq-2024/4.15.b3.2 and 4.15.b6, and qaa/fqheis-2024/4.16.b5."
  author-agent-dialogue: "Raise it when a student plans a project or a team designs research teaching. Ask: what evidence would change your mind about your recommendation? Avoid reading the list out or treating it as a checklist."
- statement: qaa/business-and-management-2023/3.10.b4
  forPractitioner: { text: "Develop commercial acumen: awareness of the drivers of success, causes of failure, and sustainable customer satisfaction and loyalty.", rewrite: light, force: describes, status: drafted }
  forBeneficiary: { text: "You develop commercial sense: knowing what makes businesses succeed or fail and why keeping customers satisfied and loyal, in sustainable ways, matters.", rewrite: full, force: describes, status: drafted }
  author-agent-written: "Present this as a skill of particular relevance to the subject (commercial acumen), which the list describes and para 3.9 says graduates should be able to show, at honours level FHEQ 6. Cite it as (QAA, 2023, Business and Management Subject Benchmark Statement, para 3.10), naming the skill. Do not claim it is a threshold requirement on its own; set it beside para 3.7.b3 and the threshold application item 4.5.b4."
  author-agent-dialogue: "Raise it when a student reflects on commercial acumen or a team plans where it is developed. Ask: what would you say drives success in a business you know? Avoid reading the list out or treating it as a checklist."
- statement: qaa/business-and-management-2023/3.10.b5
  forPractitioner: { text: "Develop innovation, creativity and enterprise: entrepreneurial action to generate and communicate ideas, manage intellectual property, gain backing and deliver sustainable outcomes.", rewrite: light, force: describes, status: drafted }
  forBeneficiary: { text: "You develop enterprise skills: coming up with and sharing ideas, protecting and using intellectual property, winning support and delivering lasting results.", rewrite: full, force: describes, status: drafted }
  author-agent-written: "Present this as a skill of particular relevance to the subject (innovation, creativity and enterprise), which the list describes and para 3.9 says graduates should be able to show, at honours level FHEQ 6. Cite it as (QAA, 2023, Business and Management Subject Benchmark Statement, para 3.10), naming the skill. Do not claim it is a threshold requirement on its own; set it beside paras 1.29 to 1.33, para 3.7.b10 and std:doc:qaa-enterprise-2018-guidance."
  author-agent-dialogue: "Raise it when a student reflects on innovation, creativity and enterprise or a team plans where it is developed. Ask: which of your ideas could you turn into something real, and who would back it? Avoid reading the list out or treating it as a checklist."
- statement: qaa/business-and-management-2023/3.10.b6
  forPractitioner: { text: "Develop numeracy: quantitative skills to handle data and to evaluate, estimate and model business problems.", rewrite: light, force: describes, status: drafted }
  forBeneficiary: { text: "You develop number skills: working with data and estimating, evaluating and modelling business problems.", rewrite: full, force: describes, status: drafted }
  author-agent-written: "Present this as a skill of particular relevance to the subject (numeracy), which the list describes and para 3.9 says graduates should be able to show, at honours level FHEQ 6. Cite it as (QAA, 2023, Business and Management Subject Benchmark Statement, para 3.10), naming the skill. Do not claim it is a threshold requirement on its own; set it beside para 3.7.b4 and Annex D qaa/fheq-2024/annex-d/transferable/r1/3rd."
  author-agent-dialogue: "Raise it when a student reflects on numeracy or a team plans where it is developed. Ask: how confident are you building a simple model of a business problem? Avoid reading the list out or treating it as a checklist."
- statement: qaa/business-and-management-2023/3.10.b7
  forPractitioner: { text: "Develop networking: listening, negotiation, persuasion and presentation used to cultivate business contacts.", rewrite: light, force: describes, status: drafted }
  forBeneficiary: { text: "You develop networking skills: listening well, negotiating, persuading and presenting, and using these to build business contacts.", rewrite: full, force: describes, status: drafted }
  author-agent-written: "Present this as a skill of particular relevance to the subject (networking), which the list describes and para 3.9 says graduates should be able to show, at honours level FHEQ 6. Cite it as (QAA, 2023, Business and Management Subject Benchmark Statement, para 3.10), naming the skill. Do not claim it is a threshold requirement on its own; set it beside para 3.7.b3 and qaa/fheq-2024/4.15.b8."
  author-agent-dialogue: "Raise it when a student reflects on networking or a team plans where it is developed. Ask: who in your field would you most like to meet, and how would you approach them? Avoid reading the list out or treating it as a checklist."
- statement: qaa/business-and-management-2023/3.10.b8
  forPractitioner: { text: "Develop leadership: boundary-spanning, influence, relational and collaborative work and partnership across organisations and sectors.", rewrite: light, force: describes, status: drafted }
  forBeneficiary: { text: "You develop leadership skills: working across boundaries, influencing others, building relationships and partnering with other organisations and sectors.", rewrite: full, force: describes, status: drafted }
  author-agent-written: "Present this as a skill of particular relevance to the subject (leadership), which the list describes and para 3.9 says graduates should be able to show, at honours level FHEQ 6. Cite it as (QAA, 2023, Business and Management Subject Benchmark Statement, para 3.10), naming the skill. Do not claim it is a threshold requirement on its own; set it beside paras 1.6 and 1.26 and qaa/fheq-2024/4.15.b9.2."
  author-agent-dialogue: "Raise it when a student reflects on leadership or a team plans where it is developed. Ask: when have you had to lead people who did not report to you? Avoid reading the list out or treating it as a checklist."
- statement: qaa/business-and-management-2023/3.11.b1
  forPractitioner: { text: "Develop collaborative, inclusive working with internal and external stakeholders.", rewrite: light, force: describes, status: drafted }
  forBeneficiary: { text: "You learn to work with others inclusively, both inside your organisation and beyond it.", rewrite: full, force: describes, status: drafted }
  author-agent-written: "Present this as one of the other generic skills and attributes (collaborative and inclusive working), which the list describes and para 3.9 says graduates should be able to show, at honours level FHEQ 6. Cite it as (QAA, 2023, Business and Management Subject Benchmark Statement, para 3.11), naming the skill. Do not claim it is a threshold requirement on its own; set it beside Annex D qaa/fheq-2024/annex-d/transferable/r2/3rd and spine:6."
  author-agent-dialogue: "Raise it when a student reflects on collaborative and inclusive working or a team plans where it is developed. Ask: how do you make sure everyone in a group can contribute? Avoid reading the list out or treating it as a checklist."
- statement: qaa/business-and-management-2023/3.11.b2
  forPractitioner: { text: "Develop verbal, non-verbal and digital communication.", rewrite: light, force: describes, status: drafted }
  forBeneficiary: { text: "You learn to communicate well in speech, through body language and online.", rewrite: full, force: describes, status: drafted }
  author-agent-written: "Present this as one of the other generic skills and attributes (communication), which the list describes and para 3.9 says graduates should be able to show, at honours level FHEQ 6. Cite it as (QAA, 2023, Business and Management Subject Benchmark Statement, para 3.11), naming the skill. Do not claim it is a threshold requirement on its own; set it beside qaa/fheq-2024/4.15.b8 and Annex D qaa/fheq-2024/annex-d/transferable/r1/3rd."
  author-agent-dialogue: "Raise it when a student reflects on communication or a team plans where it is developed. Ask: which audience do you find hardest to communicate with? Avoid reading the list out or treating it as a checklist."
- statement: qaa/business-and-management-2023/3.11.b3
  forPractitioner: { text: "Develop empathy and inclusivity.", rewrite: light, force: describes, status: drafted }
  forBeneficiary: { text: "You learn to understand how others feel and to include them.", rewrite: full, force: describes, status: drafted }
  author-agent-written: "Present this as one of the other generic skills and attributes (empathy and inclusivity), which the list describes and para 3.9 says graduates should be able to show, at honours level FHEQ 6. Cite it as (QAA, 2023, Business and Management Subject Benchmark Statement, para 3.11), naming the skill. Do not claim it is a threshold requirement on its own; set it beside paras 1.17 and 1.18 and spine:6."
  author-agent-dialogue: "Raise it when a student reflects on empathy and inclusivity or a team plans where it is developed. Ask: how do you notice when someone feels left out? Avoid reading the list out or treating it as a checklist."
- statement: qaa/business-and-management-2023/3.11.b4
  forPractitioner: { text: "Develop digital literacy and appropriate digital conduct.", rewrite: light, force: describes, status: drafted }
  forBeneficiary: { text: "You learn to use digital tools well and to behave appropriately online.", rewrite: full, force: describes, status: drafted }
  author-agent-written: "Present this as one of the other generic skills and attributes (digital literacy and etiquette), which the list describes and para 3.9 says graduates should be able to show, at honours level FHEQ 6. Cite it as (QAA, 2023, Business and Management Subject Benchmark Statement, para 3.11), naming the skill. Do not claim it is a threshold requirement on its own; set it beside paras 3.7.b7 and 3.10.b3 and Annex D qaa/fheq-2024/annex-d/transferable/r1/3rd."
  author-agent-dialogue: "Raise it when a student reflects on digital literacy and etiquette or a team plans where it is developed. Ask: which digital tools do you rely on, and which would you like to master? Avoid reading the list out or treating it as a checklist."
- statement: qaa/business-and-management-2023/3.11.b5
  forPractitioner: { text: "Develop thinking that is conceptual, systemic and critical, with analysis, synthesis and evaluation.", rewrite: light, force: describes, status: drafted }
  forBeneficiary: { text: "You learn to think in concepts and systems, and critically: analysing, bringing ideas together and judging them.", rewrite: full, force: describes, status: drafted }
  author-agent-written: "Present this as one of the other generic skills and attributes (conceptual, systemic and critical thinking), which the list describes and para 3.9 says graduates should be able to show, at honours level FHEQ 6. Cite it as (QAA, 2023, Business and Management Subject Benchmark Statement, para 3.11), naming the skill. Do not claim it is a threshold requirement on its own; set it beside qaa/fheq-2024/4.15.b7 and Annex D qaa/fheq-2024/annex-d/cognitive/r2/3rd."
  author-agent-dialogue: "Raise it when a student reflects on conceptual, systemic and critical thinking or a team plans where it is developed. Ask: can you trace how one change ripples through a whole organisation? Avoid reading the list out or treating it as a checklist."
- statement: qaa/business-and-management-2023/3.11.b6
  forPractitioner: { text: "Develop self-management: independent learning, responsibility, flexibility, tolerance of uncertainty, handling complexity, challenging assumptions, evidence-led critical thinking, resilience and appropriate assertiveness.", rewrite: light, force: describes, status: drafted }
  forBeneficiary: { text: "You learn to manage yourself: learning independently, taking responsibility, staying flexible, coping with uncertainty and complexity, questioning assumptions, using evidence, bouncing back and speaking up when you need to.", rewrite: full, force: describes, status: drafted }
  author-agent-written: "Present this as one of the other generic skills and attributes (self-management), which the list describes and para 3.9 says graduates should be able to show, at honours level FHEQ 6. Cite it as (QAA, 2023, Business and Management Subject Benchmark Statement, para 3.11), naming the skill. Do not claim it is a threshold requirement on its own; set it beside qaa/fheq-2024/4.15.b5 and 4.15.b9.1 and Annex D qaa/fheq-2024/annex-d/transferable/r3/3rd."
  author-agent-dialogue: "Raise it when a student reflects on self-management or a team plans where it is developed. Ask: when did you last cope well with not knowing the answer? Avoid reading the list out or treating it as a checklist."
- statement: qaa/business-and-management-2023/3.11.b7
  forPractitioner: { text: "Develop self-reflection: self-analysis, sensitivity to diversity in people and cultures, and continuing appetite for development.", rewrite: light, force: describes, status: drafted }
  forBeneficiary: { text: "You learn to reflect on yourself, to be aware of and sensitive to differences between people and cultures, and to keep wanting to grow.", rewrite: full, force: describes, status: drafted }
  author-agent-written: "Present this as one of the other generic skills and attributes (self-reflection), which the list describes and para 3.9 says graduates should be able to show, at honours level FHEQ 6. Cite it as (QAA, 2023, Business and Management Subject Benchmark Statement, para 3.11), naming the skill. Do not claim it is a threshold requirement on its own; set it beside Annex D qaa/fheq-2024/annex-d/transferable/r5/3rd and spine:6."
  author-agent-dialogue: "Raise it when a student reflects on self-reflection or a team plans where it is developed. Ask: what have you learned about yourself from working with people unlike you? Avoid reading the list out or treating it as a checklist."
- statement: qaa/business-and-management-2023/3.18
  forPractitioner: { text: "Make assessment part of learning: give feedback on formative and summative work, promptly and in a form students can act on within the module and across the course.", rewrite: light, force: should, status: drafted }
  forBeneficiary: { text: "not-applicable: a duty on those who set and mark assessment", rewrite: full, force: should, status: drafted }
  author-agent-written: "Describe this as an expectation (should) on assessment design and feedback in honours courses. Cite it as (QAA, 2023, Business and Management Subject Benchmark Statement, para 3.18) and set it beside paras 3.19, 3.20 and 3.25. Do not present it as a student outcome."
  author-agent-dialogue: "Raise it when a team reviews feedback turnaround or format. Ask whether students can act on the feedback before their next assessment. Keep the duty with staff."
- statement: qaa/business-and-management-2023/3.20
  forPractitioner: { text: "Choose assessment methods that reliably test the intended outcomes and are inclusive by design; they can also be varied and innovative and build skills in their own right.", rewrite: light, force: must, status: drafted }
  forBeneficiary: { text: "not-applicable: a duty on those who design assessment", rewrite: full, force: must, status: drafted }
  author-agent-written: "Describe this as an expectation on assessment design stated with 'need to', recorded as describes. Cite it as (QAA, 2023, Business and Management Subject Benchmark Statement, para 3.20) and set it beside paras 3.18, 3.19 and 3.22. Do not present the list of typical methods that follows as required."
  author-agent-dialogue: "Raise it when a team chooses or changes assessment methods. Ask how a method shows the outcome reliably and who might be disadvantaged by it. Keep it for staff."
- statement: qaa/business-and-management-2023/3.23
  forPractitioner: { text: "Weigh the amount of group assessment across the course, its authenticity and fit to the task, and how group and individual marks are attributed.", rewrite: light, force: should, status: drafted }
  forBeneficiary: { text: "not-applicable: a duty on assessment design", rewrite: full, force: should, status: drafted }
  author-agent-written: "Describe this as an expectation (should) on group assessment design. Cite it as (QAA, 2023, Business and Management Subject Benchmark Statement, para 3.23) and set it beside paras 3.24 on peer assessment and 3.10.b8 on collaborative working. Do not present it as a student standard."
  author-agent-dialogue: "Raise it when a team adds or reviews group assessment. Ask how individual contribution is recognised in the mark. Keep it for staff; a student worried about group marks can be pointed to the course's rules."
- statement: qaa/business-and-management-2023/3.24
  forPractitioner: { text: "When using peer assessment, give students clear guidance and cap the weight of peer marks in a module.", rewrite: light, force: should, status: drafted }
  forBeneficiary: { text: "not-applicable: a duty on assessment design", rewrite: full, force: should, status: drafted }
  author-agent-written: "Describe this as an expectation (should) on peer assessment: clear guidance and limited weighting. Cite it as (QAA, 2023, Business and Management Subject Benchmark Statement, para 3.24) and set it beside paras 3.23 and 3.25. Do not present it as a student standard."
  author-agent-dialogue: "Raise it when a team plans peer assessment. Ask what share of the module mark peer marks would carry and what guidance students get. Keep it with staff."
- statement: qaa/business-and-management-2023/3.25
  forPractitioner: { text: "Share assessment details and marking criteria with students openly, and consider co-designing assessments with them.", rewrite: light, force: should, status: drafted }
  forBeneficiary: { text: "not-applicable: a duty on the course team; students meet its effect", rewrite: full, force: should, status: drafted }
  author-agent-written: "Describe this as an expectation (should) that assessment details and criteria are shared, with co-design as an option (may). Cite it as (QAA, 2023, Business and Management Subject Benchmark Statement, para 3.25) and set it beside para 3.18. Do not claim co-design is required."
  author-agent-dialogue: "Raise it when students say they do not know how they are marked. With staff, ask where the criteria are published and when students see them. Do not put the duty on students."
- statement: qaa/business-and-management-2023/3.26
  forPractitioner: { text: "Plan assessment with the student's whole workload in view, across modules and deadlines.", rewrite: light, force: should, status: drafted }
  forBeneficiary: { text: "not-applicable: a duty on assessment design", rewrite: full, force: should, status: drafted }
  author-agent-written: "Describe this as an expectation (should) on assessment design. Cite it as (QAA, 2023, Business and Management Subject Benchmark Statement, para 3.26) and set it beside paras 3.18 to 3.25. Do not present it as a student standard."
  author-agent-dialogue: "Raise it when deadlines cluster or a team adds assessment. Ask what a student's weeks look like at peak assessment. Keep it with staff."
- statement: qaa/business-and-management-2023/4.2
  forPractitioner: { text: "Set your own evidence of achievement, but refer to Annex D's descriptions of the four honours classes; expect most students to perform well above the threshold.", rewrite: light, force: should, status: drafted }
  forBeneficiary: { text: "not-applicable: a duty on the provider in setting classification evidence", rewrite: full, force: should, status: drafted }
  author-agent-written: "Describe this as a provider expectation (should) to refer to Annex D, with a stated expectation (will) that most students exceed the threshold, at FHEQ level 6 and FQHEIS level 10. Cite it as (QAA, 2023, Business and Management Subject Benchmark Statement, para 4.2) and set it beside qaa/fheq-2024/annex-d/summary/r1/3rd to r1/1st and the FHEQ document's SL6 bands. Do not claim the statement itself sets the class boundaries."
  author-agent-dialogue: "Raise it when a team aligns its marking criteria to degree classes. Ask how their criteria for a 2.1 compare with Annex D's description. Keep it with staff."
- statement: qaa/business-and-management-2023/4.3
  forPractitioner: { text: "Use the three categories for individual performance: threshold is the floor for every honours graduate, and most students should reach the typical standard.", rewrite: light, force: should, status: drafted }
  forBeneficiary: { text: "If you complete an honours degree you will have reached at least the minimum standard, and, like most students, you should reach the typical standard.", rewrite: full, force: should, status: drafted }
  author-agent-written: "Describe this as the statement's own reading of its rungs at FHEQ level 6: threshold the minimum for every honours graduate, typical what most should reach (should). Cite it as (QAA, 2023, Business and Management Subject Benchmark Statement, para 4.3) and set it beside paras 4.5 to 4.7 and the Annex D bands qaa/fheq-2024/annex-d/summary/r1/3rd to r1/1st. Do not claim typical is a pass requirement."
  author-agent-dialogue: "Raise it when a student asks what is expected of them or whether the minimum is enough. Ask them which standard they are aiming for and why. Never present the typical or excellent standard as the minimum."
- statement: qaa/business-and-management-2023/4.5.b1
  forPractitioner: { text: "At threshold, graduates will have shown they know and understand the key areas of the subject, how they interrelate and how they apply.", rewrite: light, force: will, status: drafted }
  forBeneficiary: { text: "To reach the minimum standard, you will have shown that you know and understand the main areas of business and management, how they link and how they are used.", rewrite: full, force: will, status: drafted }
  author-agent-written: "Treat this as the threshold every honours graduate will have shown (will) for knowledge and understanding, for any honours degree (the 3rd class marks the threshold in Annex D) in this subject at FHEQ level 6 (FQHEIS level 10). Cite it as (QAA, 2023, Business and Management Subject Benchmark Statement, para 4.5, knowledge and understanding). Do not present it as the expected standard, since most students go well beyond it (para 4.2). Set it beside 4.6.b1 (the same category at the next rung), the level descriptors qaa/fheq-2024/4.15.b1 and qaa/fqheis-2024/4.16.b1, and Annex D qaa/fheq-2024/annex-d/knowledge/r1 at the 3rd band."
  author-agent-dialogue: "Raise it when a student asks what threshold work looks like in knowledge and understanding, or when staff write marking criteria for it. Put it plainly, in the second person for a student and as what the course lets students show for staff. Ask: how many areas of business can you explain, and how do they connect in practice? Avoid suggesting the minimum is the goal most students should settle for."
- statement: qaa/business-and-management-2023/4.5.b2
  forPractitioner: { text: "At threshold, graduates will have shown competence across the subject-specific and generic skills and attributes.", rewrite: light, force: will, status: drafted }
  forBeneficiary: { text: "To reach the minimum standard, you will have shown that you are competent in the range of business skills and general skills.", rewrite: full, force: will, status: drafted }
  author-agent-written: "Treat this as the threshold every honours graduate will have shown (will) for skills, for any honours degree (the 3rd class marks the threshold in Annex D) in this subject at FHEQ level 6 (FQHEIS level 10). Cite it as (QAA, 2023, Business and Management Subject Benchmark Statement, para 4.5, skills). Do not present it as the expected standard, since most students go well beyond it (para 4.2). Set it beside 4.6.b2 (the same category at the next rung), the level descriptors qaa/fheq-2024/4.15.b2 and 4.15.b6, and Annex D qaa/fheq-2024/annex-d/practical/r1 at the 3rd band."
  author-agent-dialogue: "Raise it when a student asks what threshold work looks like in skills, or when staff write marking criteria for it. Put it plainly, in the second person for a student and as what the course lets students show for staff. Ask: which subject skills could you show an employer evidence for today? Avoid suggesting the minimum is the goal most students should settle for."
- statement: qaa/business-and-management-2023/4.5.b3
  forPractitioner: { text: "At threshold, graduates will hold a view of the subject formed largely through guided learning, with some evidence of critical perspective.", rewrite: light, force: will, status: drafted }
  forBeneficiary: { text: "To reach the minimum standard, your view of business will come mostly from what you have been guided to learn, with some signs that you question it.", rewrite: full, force: will, status: drafted }
  author-agent-written: "Treat this as the threshold every honours graduate will have shown (will) for critical perspective, for any honours degree (the 3rd class marks the threshold in Annex D) in this subject at FHEQ level 6 (FQHEIS level 10). Cite it as (QAA, 2023, Business and Management Subject Benchmark Statement, para 4.5, critical perspective). Do not present it as the expected standard, since most students go well beyond it (para 4.2). Set it beside 4.6.b3 (the same category at the next rung), the level descriptors qaa/fheq-2024/4.15.b7 and 4.15.b5, and Annex D qaa/fheq-2024/annex-d/cognitive/r2 at the 3rd band."
  author-agent-dialogue: "Raise it when a student asks what threshold work looks like in critical perspective, or when staff write marking criteria for it. Put it plainly, in the second person for a student and as what the course lets students show for staff. Ask: whose view of business do you rely on most, and when did you last question it? Avoid suggesting the minimum is the goal most students should settle for."
- statement: qaa/business-and-management-2023/4.5.b4
  forPractitioner: { text: "At threshold, graduates will have shown they can apply their knowledge in a contemporary organisation.", rewrite: light, force: will, status: drafted }
  forBeneficiary: { text: "To reach the minimum standard, you will have shown that you can use what you know in a present-day organisation.", rewrite: full, force: will, status: drafted }
  author-agent-written: "Treat this as the threshold every honours graduate will have shown (will) for application, for any honours degree (the 3rd class marks the threshold in Annex D) in this subject at FHEQ level 6 (FQHEIS level 10). Cite it as (QAA, 2023, Business and Management Subject Benchmark Statement, para 4.5, application). Do not present it as the expected standard, since most students go well beyond it (para 4.2). Set it beside 4.6.b4 (the same category at the next rung), the level descriptors qaa/fheq-2024/4.15.b3.1 and 4.15.b9.2, and Annex D qaa/fheq-2024/annex-d/cognitive/r3 at the 3rd band."
  author-agent-dialogue: "Raise it when a student asks what threshold work looks like in application, or when staff write marking criteria for it. Put it plainly, in the second person for a student and as what the course lets students show for staff. Ask: when did you last apply theory to a real organisation, and what did it show you? Avoid suggesting the minimum is the goal most students should settle for."
- statement: qaa/business-and-management-2023/4.5.b5
  forPractitioner: { text: "At threshold, graduates will have shown a capacity to practise global social responsibility.", rewrite: light, force: will, status: drafted }
  forBeneficiary: { text: "To reach the minimum standard, you will have shown that you can put the values of global social responsibility into practice.", rewrite: full, force: will, status: drafted }
  author-agent-written: "Treat this as the threshold every honours graduate will have shown (will) for values, for any honours degree (the 3rd class marks the threshold in Annex D) in this subject at FHEQ level 6 (FQHEIS level 10). Cite it as (QAA, 2023, Business and Management Subject Benchmark Statement, para 4.5, values). Do not present it as the expected standard, since most students go well beyond it (para 4.2). Set it beside 4.6.b5 (the same category at the next rung), the level descriptors qaa/fheq-2024/4.15.b9.1 and spine:6 (strand:autonomy), and Annex D qaa/fheq-2024/annex-d/transferable/r4 at the 3rd band."
  author-agent-dialogue: "Raise it when a student asks what threshold work looks like in values, or when staff write marking criteria for it. Put it plainly, in the second person for a student and as what the course lets students show for staff. Ask: where in your work have you acted on global social responsibility, not only discussed it? Avoid suggesting the minimum is the goal most students should settle for."
- statement: qaa/business-and-management-2023/4.6.b1
  forPractitioner: { text: "At the typical rung, graduates will usually have shown solid, substantial knowledge across many areas, their complex interrelations and their use in practice.", rewrite: light, force: will, status: drafted }
  forBeneficiary: { text: "To reach the typical standard, you will usually have shown solid, substantial knowledge across a broad range of business areas, the complex ways they link and how they work in practice.", rewrite: full, force: will, status: drafted }
  author-agent-written: "Treat this as the typical standard most graduates will have shown (will typically), above the minimum for knowledge and understanding, for a second class honours degree in this subject at FHEQ level 6 (FQHEIS level 10). Cite it as (QAA, 2023, Business and Management Subject Benchmark Statement, para 4.6, knowledge and understanding). Do not present it as the minimum for an honours degree; that is the threshold item. Set it beside 4.5.b1 and 4.7.b1 (the same category at the next rung), the level descriptors qaa/fheq-2024/4.15.b1 and qaa/fqheis-2024/4.16.b1, and Annex D qaa/fheq-2024/annex-d/knowledge/r1 at the 2.2 and 2.1 band."
  author-agent-dialogue: "Raise it when a student asks what typical work looks like in knowledge and understanding, or when staff write marking criteria for it. Put it plainly, in the second person for a student and as what the course lets students show for staff. Ask: how many areas of business can you explain, and how do they connect in practice? Never treat this as the pass standard."
- statement: qaa/business-and-management-2023/4.6.b2
  forPractitioner: { text: "At the typical rung, graduates will usually have shown command of the subject's skills and proficiency in generic ones.", rewrite: light, force: will, status: drafted }
  forBeneficiary: { text: "To reach the typical standard, you will usually have shown command of business skills and real proficiency in general skills.", rewrite: full, force: will, status: drafted }
  author-agent-written: "Treat this as the typical standard most graduates will have shown (will typically), above the minimum for skills, for a second class honours degree in this subject at FHEQ level 6 (FQHEIS level 10). Cite it as (QAA, 2023, Business and Management Subject Benchmark Statement, para 4.6, skills). Do not present it as the minimum for an honours degree; that is the threshold item. Set it beside 4.5.b2 and 4.7.b2 (the same category at the next rung), the level descriptors qaa/fheq-2024/4.15.b2 and 4.15.b6, and Annex D qaa/fheq-2024/annex-d/practical/r1 at the 2.2 and 2.1 band."
  author-agent-dialogue: "Raise it when a student asks what typical work looks like in skills, or when staff write marking criteria for it. Put it plainly, in the second person for a student and as what the course lets students show for staff. Ask: which subject skills could you show an employer evidence for today? Never treat this as the pass standard."
- statement: qaa/business-and-management-2023/4.6.b3
  forPractitioner: { text: "At the typical rung, graduates will usually have a view informed by wide, appropriate sources, showing independent learning and critical evaluation.", rewrite: light, force: will, status: drafted }
  forBeneficiary: { text: "To reach the typical standard, your view of business will usually draw on many suitable sources, showing that you learn independently and judge critically.", rewrite: full, force: will, status: drafted }
  author-agent-written: "Treat this as the typical standard most graduates will have shown (will typically), above the minimum for critical perspective, for a second class honours degree in this subject at FHEQ level 6 (FQHEIS level 10). Cite it as (QAA, 2023, Business and Management Subject Benchmark Statement, para 4.6, critical perspective). Do not present it as the minimum for an honours degree; that is the threshold item. Set it beside 4.5.b3 and 4.7.b3 (the same category at the next rung), the level descriptors qaa/fheq-2024/4.15.b7 and 4.15.b5, and Annex D qaa/fheq-2024/annex-d/cognitive/r2 at the 2.2 and 2.1 band."
  author-agent-dialogue: "Raise it when a student asks what typical work looks like in critical perspective, or when staff write marking criteria for it. Put it plainly, in the second person for a student and as what the course lets students show for staff. Ask: whose view of business do you rely on most, and when did you last question it? Never treat this as the pass standard."
- statement: qaa/business-and-management-2023/4.6.b4
  forPractitioner: { text: "At the typical rung, graduates will usually apply knowledge in complex organisations and show some capacity for their own perspective, coping with uncertainty, weighing alternatives, critical evaluation and integrating theory.", rewrite: light, force: will, status: drafted }
  forBeneficiary: { text: "To reach the typical standard, you will usually be able to use what you know in complex organisations, and show some ability to form your own views, cope with uncertainty, weigh up alternatives, judge critically and draw on theory.", rewrite: full, force: will, status: drafted }
  author-agent-written: "Treat this as the typical standard most graduates will have shown (will typically), above the minimum for application, for a second class honours degree in this subject at FHEQ level 6 (FQHEIS level 10). Cite it as (QAA, 2023, Business and Management Subject Benchmark Statement, para 4.6, application). Do not present it as the minimum for an honours degree; that is the threshold item. Set it beside 4.5.b4 and 4.7.b4 (the same category at the next rung), the level descriptors qaa/fheq-2024/4.15.b3.1 and 4.15.b9.2, and Annex D qaa/fheq-2024/annex-d/cognitive/r3 at the 2.2 and 2.1 band."
  author-agent-dialogue: "Raise it when a student asks what typical work looks like in application, or when staff write marking criteria for it. Put it plainly, in the second person for a student and as what the course lets students show for staff. Ask: when did you last apply theory to a real organisation, and what did it show you? Never treat this as the pass standard."
- statement: qaa/business-and-management-2023/4.6.b5
  forPractitioner: { text: "At the typical rung, graduates will usually have shown they can integrate the values of global social responsibility.", rewrite: light, force: will, status: drafted }
  forBeneficiary: { text: "To reach the typical standard, you will usually have shown that you can build the values of global social responsibility into what you do.", rewrite: full, force: will, status: drafted }
  author-agent-written: "Treat this as the typical standard most graduates will have shown (will typically), above the minimum for values, for a second class honours degree in this subject at FHEQ level 6 (FQHEIS level 10). Cite it as (QAA, 2023, Business and Management Subject Benchmark Statement, para 4.6, values). Do not present it as the minimum for an honours degree; that is the threshold item. Set it beside 4.5.b5 and 4.7.b5 (the same category at the next rung), the level descriptors qaa/fheq-2024/4.15.b9.1 and spine:6 (strand:autonomy), and Annex D qaa/fheq-2024/annex-d/transferable/r4 at the 2.2 and 2.1 band."
  author-agent-dialogue: "Raise it when a student asks what typical work looks like in values, or when staff write marking criteria for it. Put it plainly, in the second person for a student and as what the course lets students show for staff. Ask: where in your work have you acted on global social responsibility, not only discussed it? Never treat this as the pass standard."
- statement: qaa/business-and-management-2023/4.7.b1
  forPractitioner: { text: "At the excellent rung, graduates will have shown advanced knowledge and critical understanding of many areas, their detailed interrelations and their use in practice.", rewrite: light, force: will, status: drafted }
  forBeneficiary: { text: "To reach the excellent standard, you will have shown advanced knowledge and a critical grasp of a broad range of business areas, the detailed ways they link and how they apply in practice.", rewrite: full, force: will, status: drafted }
  author-agent-written: "Treat this as the excellent standard shown at first class (will), an aspiration rather than a requirement for knowledge and understanding, for a first class honours degree in this subject at FHEQ level 6 (FQHEIS level 10). Cite it as (QAA, 2023, Business and Management Subject Benchmark Statement, para 4.7, knowledge and understanding). Do not present it as the minimum or as expected of most students. Set it beside 4.6.b1 (the same category at the next rung), the level descriptors qaa/fheq-2024/4.15.b1 and qaa/fqheis-2024/4.16.b1, and Annex D qaa/fheq-2024/annex-d/knowledge/r1 at the 1st band."
  author-agent-dialogue: "Raise it when a student asks what excellent work looks like in knowledge and understanding, or when staff write marking criteria for it. Put it plainly, in the second person for a student and as what the course lets students show for staff. Ask: how many areas of business can you explain, and how do they connect in practice? Never present this as what everyone must reach."
- statement: qaa/business-and-management-2023/4.7.b2
  forPractitioner: { text: "At the excellent rung, graduates will have shown excellent command of the subject's skills and proficiency in generic ones.", rewrite: light, force: will, status: drafted }
  forBeneficiary: { text: "To reach the excellent standard, you will have shown excellent command of business skills and real proficiency in general skills.", rewrite: full, force: will, status: drafted }
  author-agent-written: "Treat this as the excellent standard shown at first class (will), an aspiration rather than a requirement for skills, for a first class honours degree in this subject at FHEQ level 6 (FQHEIS level 10). Cite it as (QAA, 2023, Business and Management Subject Benchmark Statement, para 4.7, skills). Do not present it as the minimum or as expected of most students. Set it beside 4.6.b2 (the same category at the next rung), the level descriptors qaa/fheq-2024/4.15.b2 and 4.15.b6, and Annex D qaa/fheq-2024/annex-d/practical/r1 at the 1st band."
  author-agent-dialogue: "Raise it when a student asks what excellent work looks like in skills, or when staff write marking criteria for it. Put it plainly, in the second person for a student and as what the course lets students show for staff. Ask: which subject skills could you show an employer evidence for today? Never present this as what everyone must reach."
- statement: qaa/business-and-management-2023/4.7.b3
  forPractitioner: { text: "At the excellent rung, graduates will hold a view formed by analysing wide sources, learning proactively and independently, challenging assumptions and questioning accepted practice.", rewrite: light, force: will, status: drafted }
  forBeneficiary: { text: "To reach the excellent standard, your view of business will come from analysing many sources, learning on your own initiative, challenging assumptions and questioning the way things are done.", rewrite: full, force: will, status: drafted }
  author-agent-written: "Treat this as the excellent standard shown at first class (will), an aspiration rather than a requirement for critical perspective, for a first class honours degree in this subject at FHEQ level 6 (FQHEIS level 10). Cite it as (QAA, 2023, Business and Management Subject Benchmark Statement, para 4.7, critical perspective). Do not present it as the minimum or as expected of most students. Set it beside 4.6.b3 (the same category at the next rung), the level descriptors qaa/fheq-2024/4.15.b7 and 4.15.b5, and Annex D qaa/fheq-2024/annex-d/cognitive/r2 at the 1st band."
  author-agent-dialogue: "Raise it when a student asks what excellent work looks like in critical perspective, or when staff write marking criteria for it. Put it plainly, in the second person for a student and as what the course lets students show for staff. Ask: whose view of business do you rely on most, and when did you last question it? Never present this as what everyone must reach."
- statement: qaa/business-and-management-2023/4.7.b4
  forPractitioner: { text: "At the excellent rung, graduates will have shown exceptional capacity for their own perspective, for uncertainty and complexity, alternatives, critical evaluation and integrating theory and practice widely.", rewrite: light, force: will, status: drafted }
  forBeneficiary: { text: "To reach the excellent standard, you will have shown an exceptional ability to form your own views, cope with uncertainty and complexity, weigh up alternatives, judge critically and join theory with practice in many situations.", rewrite: full, force: will, status: drafted }
  author-agent-written: "Treat this as the excellent standard shown at first class (will), an aspiration rather than a requirement for application, for a first class honours degree in this subject at FHEQ level 6 (FQHEIS level 10). Cite it as (QAA, 2023, Business and Management Subject Benchmark Statement, para 4.7, application). Do not present it as the minimum or as expected of most students. Set it beside 4.6.b4 (the same category at the next rung), the level descriptors qaa/fheq-2024/4.15.b3.1 and 4.15.b9.2, and Annex D qaa/fheq-2024/annex-d/cognitive/r3 at the 1st band."
  author-agent-dialogue: "Raise it when a student asks what excellent work looks like in application, or when staff write marking criteria for it. Put it plainly, in the second person for a student and as what the course lets students show for staff. Ask: when did you last apply theory to a real organisation, and what did it show you? Never present this as what everyone must reach."
- statement: qaa/business-and-management-2023/4.7.b5
  forPractitioner: { text: "At the excellent rung, graduates will have shown they can challenge assumptions and champion global social responsibility while appreciating its debates and tensions in complex settings.", rewrite: light, force: will, status: drafted }
  forBeneficiary: { text: "To reach the excellent standard, you will have shown that you can challenge assumptions and champion global social responsibility, while seeing the debates and disagreements it raises in complex business settings.", rewrite: full, force: will, status: drafted }
  author-agent-written: "Treat this as the excellent standard shown at first class (will), an aspiration rather than a requirement for values, for a first class honours degree in this subject at FHEQ level 6 (FQHEIS level 10). Cite it as (QAA, 2023, Business and Management Subject Benchmark Statement, para 4.7, values). Do not present it as the minimum or as expected of most students. Set it beside 4.6.b5 (the same category at the next rung), the level descriptors qaa/fheq-2024/4.15.b9.1 and spine:6 (strand:autonomy), and Annex D qaa/fheq-2024/annex-d/transferable/r4 at the 1st band."
  author-agent-dialogue: "Raise it when a student asks what excellent work looks like in values, or when staff write marking criteria for it. Put it plainly, in the second person for a student and as what the course lets students show for staff. Ask: where in your work have you acted on global social responsibility, not only discussed it? Never present this as what everyone must reach."
```

### S5 Levels and alignment
<!-- label: both; status: drafted; basis: primary -->
```yaml
levels:
  - { id: "fheq:6", role: "cites", locator: "D1, 2.7; 4.2" }
  - { id: "fqheis:10", role: "cites", locator: "D1, 2.7; 4.2" }
  - { id: "fheq:7", role: "cites", locator: "D1, 2.10 (integrated master's)" }
  - { id: "fqheis:11", role: "cites", locator: "D1, 2.10 (integrated master's)" }
  - { id: "fheq:4", role: "inferred: CertHE named as an exit award (D1, 2.9); level from std:doc:qaa-fheq-2024-framework S5", locator: "D1, 2.9" }
  - { id: "fheq:5", role: "inferred: DipHE named as an exit award (D1, 2.9); level from std:doc:qaa-fheq-2024-framework S5", locator: "D1, 2.9" }
  - { id: "spine:6", role: "inferred: the reference framework step for the honours standards (std:ref:uk-framework R2, R8)", locator: "D1, 4.5 to 4.7" }
crosswalks:
  - { from: "fheq:6", to: "fqheis:10", relation: "equivalent", basis: "stated (D1, 2.7: \"(FHEQ Level 6; FQHEIS Level 10)\"; 4.2)" }
  - { from: "fheq:7", to: "fqheis:11", relation: "equivalent", basis: "stated (D1, 2.10)" }
  - { from: "fheq:6", to: "cqfw:6", relation: "compares-with", basis: "inferred from std:doc:qaa-fheq-2024-framework S5 (its 2.24); the statement does not name the CQFW (Part E)" }
```

### S6 Themes
<!-- label: both; status: drafted; basis: primary -->
```yaml
- { id: "theme:edi", role: "carries", carriedIn: ["1.6", "1.14", "1.15", "1.16", "1.17", "1.18", "1.19", "1.20", "1.21", "1.23", "2.4", "2.11", "2.17", "2.20", "3.7", "3.10", "3.11", "3.16", "3.19", "3.20"] }
- { id: "theme:accessibility", role: "carries", carriedIn: ["1.19", "1.20", "1.22", "1.23", "1.24", "2.11", "2.12", "3.19"] }
- { id: "theme:esd", role: "carries", carriedIn: ["1.6", "1.14", "1.17", "1.25", "1.26", "1.27", "1.28", "1.33", "2.4", "3.4", "3.7", "3.10"] }
- { id: "theme:enterprise", role: "carries", carriedIn: ["1.7", "1.14", "1.29", "1.30", "1.31", "1.32", "1.33", "3.7", "3.10", "3.16"] }
```

### S7 Relations
<!-- label: both; status: drafted; basis: primary -->
```yaml
- { rel: "partOf", target: "collection: QAA Subject Benchmark Statements", note: "one of 54 held by stan" }
- { rel: "supersedes", target: "std:doc:qaa-business-and-management-2019-benchmarks (not held)", note: "the fourth edition, 2019, named in section 6; earlier editions 2015, 2007 and 2000 are named there too" }
- { rel: "refersTo", target: "std:doc:qaa-fheq-2024-framework, Annex D", note: "the degree outcome classification descriptions for FHEQ level 6 and FQHEIS level 10, cited as QAA 2019 (4.2; section 5); now part of the 2024 Frameworks" }
- { rel: "refersTo", target: "std:doc:qaa-fheq-2024-framework", note: "FHEQ levels 6 and 7 (2.7, 2.10, 4.2)" }
- { rel: "refersTo", target: "std:doc:qaa-fqheis-2024-framework", note: "FQHEIS levels 10 and 11 (2.7, 2.10, 4.2)" }
- { rel: "themeReference", target: "std:doc:qaa-advancehe-esd-2021-guidance", note: "Education for Sustainable Development Guidance, QAA and Advance HE 2021 (1.25, 1.28)" }
- { rel: "themeReference", target: "std:doc:qaa-enterprise-2018-guidance", note: "Enterprise and Entrepreneurship Education guidance, QAA 2018 (1.32)" }
- { rel: "refersTo", target: "QAA Characteristics Statement: Higher Education in Apprenticeships, 2022 (not yet ingested)", note: "1.2" }
- { rel: "refersTo", target: "QAA Characteristics Statement: Micro-Credentials (not yet ingested)", note: "2.12" }
- { rel: "refersTo", target: "QAA Quality Code, Advice and Guidance; QAA Glossary (not ingested)", note: "front matter" }
- { rel: "relatedTo", target: "the allied Subject Benchmark Statements for Accounting, Economics, Finance, and Events, Hospitality, Leisure, Sport and Tourism", note: "named in 1.2 without editions; held: std:doc:qaa-accounting-2025-benchmarks, std:doc:qaa-economics-2023-benchmarks, std:doc:qaa-finance-2025-benchmarks (inferred editions, Part E)" }
- { rel: "refersTo", target: "UN Sustainable Development Goals; UN Principles for Responsible Management Education; UN Curriculum on Governance for the SDGs; IPCC 2022 (not standards documents)", note: "1.17, 1.25, 1.26, 1.27" }
```

### S8 Currency and review
<!-- label: source; status: drafted; basis: primary -->
```yaml
published: "2023-03"
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
- A broad, general study of organisations, their cultures, structures and management in economic, environmental and social context, rather than one function or sector (D1, 1.2, 1.4).
- Organisations and business are read widely: public, private, non-profit, community and social enterprises of every size, from start-ups to global firms (D1, 1.5, 2.5).
- Responsible leadership runs through it: values-led, inclusive, ethical and sustainable, with attention to climate change and net zero (D1, 1.6, 3.6).
- Interdisciplinary and varied, drawing on the social sciences, humanities and sciences, with theory always set beside practice (D1, 1.10, 1.11, 2.1).
- Courses range from vocational study for business to research-oriented study of business, most combining the two (D1, 2.2, 3.14).
- Strongly tied to practice and employability, through partnerships, placements, live projects and practitioner input (D1, 2.14, 3.8, 3.15).
- A dynamic, changing discipline whose courses are expected to keep innovating (D1, 1.3, 1.12, 2.6).

### SB2 Themes in this subject
<!-- label: both; status: drafted; basis: primary -->
```yaml
- theme: theme:edi
  inThisSubject: "framed through why, what and how the subject is taught: business education as a lever against inequality (with the SDGs), anti-discrimination law and inclusive workplaces as content, diverse cases including the Global South, and inclusive modes and assessment; reviewed with students (D1, 1.15 to 1.21)"
  statements: ["qaa/business-and-management-2023/1.15", "qaa/business-and-management-2023/1.17", "qaa/business-and-management-2023/1.18", "qaa/business-and-management-2023/1.19", "qaa/business-and-management-2023/1.21", "qaa/business-and-management-2023/3.7.b5", "qaa/business-and-management-2023/3.10.b1", "qaa/business-and-management-2023/3.11.b1", "qaa/business-and-management-2023/3.11.b3"]
- theme: theme:accessibility
  inThisSubject: "regulatory minimum and whole-journey reach, reasonable adjustments in assessment, mindfulness of digital poverty and caring duties, and equal access to placements and international learning (D1, 1.22 to 1.24, 2.11, 2.12)"
  statements: ["qaa/business-and-management-2023/1.22", "qaa/business-and-management-2023/1.24"]
- theme: theme:esd
  inThisSubject: "sustainable management as a condition of planetary survival, the SDGs and PRME, ethics, responsibility and sustainability (ERS) expected by some accreditors, carbon literacy and sustainable supply chains as example topics (D1, 1.25 to 1.28, 2.4)"
  statements: ["qaa/business-and-management-2023/1.26", "qaa/business-and-management-2023/3.7.b1"]
- theme: theme:enterprise
  inThisSubject: "entrepreneurship as a subject area and enterprise as a set of behaviours: venture creation, innovation inside established organisations, social enterprise and experiential learning; the front matter joins it with employability (D1, 1.29 to 1.33, 3.7, 3.10)"
  statements: ["qaa/business-and-management-2023/3.7.b10", "qaa/business-and-management-2023/3.10.b5"]
```

### SB3 Content and delivery
<!-- label: both; status: drafted; basis: primary -->
```yaml
areas:
  - { component: "3.4", gloss: "the business environment: local to international factors acting on organisations" }
  - { component: "3.5", gloss: "organisations: internal functions, structures, governance, cultures" }
  - { component: "3.6", gloss: "responsible leadership and management: theories, models and roles" }
  - { component: "3.7", gloss: "ten areas, from ethics, responsibility and sustainability to entrepreneurship and enterprise development" }
practices:
  - { component: "3.15", kind: "teaching", gloss: "theory joined with practice; inputs from managers, entrepreneurs and stakeholders" }
  - { component: "3.16", kind: "learning", gloss: "inclusive methods and modes; lectures, seminars, workshops, placements, live projects, simulations, mentoring, start-up" }
  - { component: "3.17", kind: "assessment", gloss: "skills development defined and assessed, as process or product" }
  - { component: "3.18", kind: "assessment", gloss: "assessment for learning with timely feedback" }
  - { component: "3.19", kind: "assessment", gloss: "inclusive assessment design that anticipates needs" }
  - { component: "3.20", kind: "assessment", gloss: "reliable, inclusive, varied methods: reports, exams, presentations, dissertations, portfolios" }
  - { component: "3.22", kind: "assessment", gloss: "authentic assessment" }
  - { component: "3.23", kind: "assessment", gloss: "group work: extent, fit and attribution of marks" }
  - { component: "3.24", kind: "assessment", gloss: "peer assessment with guidance and capped weighting" }
  - { component: "3.25", kind: "assessment", gloss: "transparent criteria; co-designed assessment" }
```

### SB4 Benchmark standards
<!-- label: both; status: drafted; basis: primary -->
```yaml
rungs:
  - { rung: "threshold", leadIn: "4.5", award: "bachelor's with honours", items: 5 }
  - { rung: "typical", leadIn: "4.6", award: "bachelor's with honours", items: 5 }
  - { rung: "excellent", leadIn: "4.7", award: "bachelor's with honours", items: 5 }
rungBases: "4.4: the categories differ by range and consistency in showing breadth, depth, integration and application of knowledge; competence in subject-specific, academic and professional skills; depth of critical perspective; ability to apply knowledge and skills; capacity to practise global social responsibility. 4.3: threshold is the minimum for all honours graduates; most should reach typical. The lead-ins tie the rungs to degree classes: honours (threshold), second class (typical), first class (excellent)."
outcomeLists:
  - { leadIn: "3.7", gloss: "ten areas of knowledge, understanding and critical evaluation (should)", items: 10, award: ["honours"] }
  - { leadIn: "3.10", gloss: "eight skills of particular relevance to the subject (describes; 3.9 carries should)", items: 8, award: ["honours"] }
  - { leadIn: "3.11", gloss: "seven other generic skills and attributes (describes; 3.9 carries should)", items: 7, award: ["honours"] }
outcomes:
  - { outcome: "knowledge and understanding", threshold: "qaa/business-and-management-2023/4.5.b1", typical: "qaa/business-and-management-2023/4.6.b1", excellent: "qaa/business-and-management-2023/4.7.b1", basis: "stated", domain: "knowledge", award: "bachelor's with honours" }
  - { outcome: "skills", threshold: "qaa/business-and-management-2023/4.5.b2", typical: "qaa/business-and-management-2023/4.6.b2", excellent: "qaa/business-and-management-2023/4.7.b2", basis: "stated", domain: "subject-skill", award: "bachelor's with honours" }
  - { outcome: "critical perspective", threshold: "qaa/business-and-management-2023/4.5.b3", typical: "qaa/business-and-management-2023/4.6.b3", excellent: "qaa/business-and-management-2023/4.7.b3", basis: "stated", domain: "understanding", award: "bachelor's with honours" }
  - { outcome: "application", threshold: "qaa/business-and-management-2023/4.5.b4", typical: "qaa/business-and-management-2023/4.6.b4", excellent: "qaa/business-and-management-2023/4.7.b4", basis: "stated", domain: "subject-skill", award: "bachelor's with honours" }
  - { outcome: "values", threshold: "qaa/business-and-management-2023/4.5.b5", typical: "qaa/business-and-management-2023/4.6.b5", excellent: "qaa/business-and-management-2023/4.7.b5", basis: "stated", domain: "generic-skill", award: "bachelor's with honours" }
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
- { body: "professional, statutory and regulatory bodies (PSRBs), in general", says: "the statement supports PSRBs on academic standards; courses may reflect their requirements for recognition, which helps learners apply management skills at work; vocational courses may need their accreditation (D1, front matter, 1.9, 2.15, 2.21)", requirements: "not-applicable-by-design: no body named" }
- { body: "accrediting bodies (unnamed)", says: "some expect ethics, responsibility and sustainability to be integrated into business school curricula (D1, 1.25)", requirements: "not-applicable-by-design: no body named" }
- { body: "Principles for Responsible Management Education (PRME)", says: "a UN initiative courses can draw on to build students' capacity to create sustainable value; one of the networks providers may engage with (D1, 1.25, 2.16)", requirements: "not yet ingested (Part E)" }
- { body: "Chartered Association of Business Schools (CABS)", says: "a network providers may engage with for good practice and development (D1, 2.16 and its footnote)", requirements: "not yet ingested (Part E)" }
- { body: "British Academy of Management (BAM)", says: "a learned society providers may engage with (D1, 2.16 and its footnote)", requirements: "not yet ingested (Part E)" }
- { body: "Association to Advance Collegiate Schools of Business (AACSB)", says: "an accreditation body for business schools providers may engage with (D1, 2.16 and its footnote)", requirements: "not yet ingested (Part E)" }
- { body: "European Foundation for Management Development (EFMD)", says: "a body providers may engage with (D1, 2.16 and its footnote); its EQUIS and programme accreditation are listed in section 5", requirements: "not yet ingested (Part E)" }
- { body: "Chartered Management Institute (CMI)", says: "named only in the references (its professional standards for management and leadership) and the advisory group, not in the numbered text (D1, section 5)", requirements: "not yet ingested (Part E)" }
```

### SB6 Cross-cutting references
<!-- label: both; status: drafted; basis: primary -->
```yaml
themes:
  - { id: "theme:edi", named: "Equality, diversity and inclusion", carriedIn: ["front matter", "1.6", "1.14", "1.15", "1.16", "1.17", "1.18", "1.19", "1.20", "1.21", "1.23", "2.4", "2.11", "2.17", "2.20", "3.7", "3.10", "3.11", "3.16", "3.19", "3.20"], statements: ["1.15", "1.17", "1.18", "1.19", "1.21", "3.7.b5", "3.10.b1", "3.11.b1", "3.11.b3"] }
  - { id: "theme:accessibility", named: "Accessibility (front matter: accessibility and the needs of disabled students)", carriedIn: ["front matter", "1.19", "1.20", "1.22", "1.23", "1.24", "2.11", "2.12", "3.19"], statements: ["1.22", "1.24"] }
  - { id: "theme:esd", named: "Education for Sustainable Development", carriedIn: ["front matter", "1.6", "1.14", "1.17", "1.25", "1.26", "1.27", "1.28", "1.33", "2.4", "3.4", "3.7", "3.10"], statements: ["1.26", "3.7.b1"] }
  - { id: "theme:enterprise", named: "Enterprise and entrepreneurship education (front matter: employability, entrepreneurship and enterprise education)", carriedIn: ["front matter", "1.7", "1.14", "1.29", "1.30", "1.31", "1.32", "1.33", "3.7", "3.10", "3.16"], statements: ["3.7.b10", "3.10.b5"] }
frameworks:
  - { framework: "fheq", levels: ["fheq:6", "fheq:7"], citedIn: ["2.7", "2.10", "4.2"] }
  - { framework: "scqf", levels: ["fqheis:10", "fqheis:11"], citedIn: ["2.7", "2.10", "4.2"] }
bodies:
  - { body: "professional, statutory and regulatory bodies (PSRBs)", citedIn: ["front matter", "1.9", "2.15", "2.21"] }
  - { body: "accrediting bodies (unnamed)", citedIn: ["1.25"] }
  - { body: "Principles for Responsible Management Education (PRME)", citedIn: ["1.25", "2.16"] }
  - { body: "Chartered Association of Business Schools (CABS)", citedIn: ["2.16"] }
  - { body: "British Academy of Management (BAM)", citedIn: ["2.16"] }
  - { body: "Association to Advance Collegiate Schools of Business (AACSB)", citedIn: ["2.16"] }
  - { body: "European Foundation for Management Development (EFMD)", citedIn: ["2.16"] }
  - { body: "Office for Students (regulatory framework, England)", citedIn: ["front matter"] }
sharedDocuments:
  - { document: "std:doc:qaa-fheq-2024-framework, Annex D", named: "Annex D: Outcome classification descriptions for FHEQ Level 6 and FQHEIS Level 10 degrees", citedIn: ["4.2"], role: "descriptions of the four honours classes (1st, 2.1, 2.2, 3rd) that providers should refer to when setting evidence of achievement" }
  - { document: "std:doc:qaa-advancehe-esd-2021-guidance", named: "QAA and Advance HE's Education for Sustainable Development Guidance, 2021", citedIn: ["1.25", "1.28"], role: "the competencies the subject's core skills align with; disciplinary method for sustainability" }
  - { document: "std:doc:qaa-enterprise-2018-guidance", named: "enterprise behaviours, attributes and competencies (as defined by QAA, 2018)", citedIn: ["1.32"], role: "source of the enterprise competencies reflected in the skills of 3.9" }
  - { document: "QAA Characteristics Statement: Higher Education in Apprenticeships, 2022 (not yet ingested: Part E)", named: "Higher Education in Apprenticeships Characteristic Statement, QAA, 2022", citedIn: ["1.2"], role: "for degree apprenticeships in the subject" }
  - { document: "QAA Characteristics Statement: Micro-Credentials (not yet ingested: Part E)", named: "QAA's Characteristics Statement: Micro-Credentials", citedIn: ["2.12"], role: "flexible credit alongside modular credit" }
  - { document: "QAA Quality Code, Advice and Guidance (not yet ingested)", named: "Advice and Guidance to support the Quality Code", citedIn: ["front matter"], role: "course design, teaching, external expertise, monitoring and evaluation" }
  - { document: "QAA Glossary (not ingested)", named: "QAA's Glossary", citedIn: ["front matter"], role: "explains unfamiliar terms" }
```

## Part B Terminology
<!-- The statement has no glossary of its own unless Part E says so; these are terms it defines in its text. -->

### B1 Concepts
<!-- label: both; status: drafted; basis: primary -->
```yaml
- { slug: "organisations", definition: "read broadly: public, private, non-profit, community-based and social enterprises of every size and structure, from start-ups to global firms (D1, 1.5)", beneficiaryDefinition: "every kind of organisation, from a small charity or start-up to a global company or public body", scopeNote: "business is read just as broadly (1.5)", category: "unknown", practices: ["business and management"] }
- { slug: "responsible-leadership", definition: "leadership that is values-led, inclusive, ethical, sustainable, systemic and transformative, weighing stakeholders now and in future and addressing climate change (D1, 1.6)", beneficiaryDefinition: "leading in a way that is ethical, inclusive and sustainable and thinks about everyone affected, now and later", scopeNote: "used in 1.4, 3.6 and 3.7", category: "unknown", practices: ["business and management"] }
- { slug: "preparation-for-a-career-in-business-and-management", definition: "building knowledge and skills for career readiness, self-awareness and personal development, and a constructive attitude to change and enterprise (D1, 1.7)", beneficiaryDefinition: "getting ready for work in any organisation, knowing yourself and being open to change", scopeNote: "", category: "unknown", practices: ["business and management"] }
- { slug: "skills-and-attributes", definition: "transferable academic and professional skills suited to, but not limited to, business careers (D1, 1.8)", beneficiaryDefinition: "skills you can carry into any career", scopeNote: "", category: "unknown", practices: ["business and management"] }
- { slug: "ethics-responsibility-and-sustainability", definition: "ERS: the triad some accrediting bodies expect business school curricula to integrate (D1, 1.25, 1.27)", beneficiaryDefinition: "acting ethically, responsibly and sustainably in business", scopeNote: "also the first area in 3.7", category: "unknown", practices: ["business and management"] }
- { slug: "enterprise-and-entrepreneurship-education", definition: "EED: education building the behaviours, attributes and competencies for successful careers, venture creation and innovation (D1, 1.29)", beneficiaryDefinition: "learning to spot opportunities and turn ideas into value, in a new venture or an existing organisation", scopeNote: "", category: "unknown", practices: ["business and management"] }
- { slug: "threshold-typical-excellent", definition: "the three categories of graduate achievement: threshold the minimum for every honours graduate, typical what most should reach, excellent the highest (D1, 4.3)", beneficiaryDefinition: "the minimum, the usual and the highest standard for your honours degree", scopeNote: "tied to honours, second class and first class in 4.5 to 4.7", category: "unknown", practices: ["education"] }
```

### B2a Terms as the issuer defines them
<!-- label: source; status: drafted; basis: primary -->
```yaml
- { concept: "organisations", form: "'Organisations'", lang: "en", partOfSpeech: "noun", termStatus: "preferred", register: "formal" }
- { concept: "responsible-leadership", form: "'responsible leadership'", lang: "en", partOfSpeech: "noun-phrase", termStatus: "preferred", register: "formal" }
- { concept: "preparation-for-a-career-in-business-and-management", form: "'Preparation for a career in business and management'", lang: "en", partOfSpeech: "noun-phrase", termStatus: "preferred", register: "formal" }
- { concept: "skills-and-attributes", form: "'skills and attributes'", lang: "en", partOfSpeech: "noun-phrase", termStatus: "preferred", register: "formal" }
- { concept: "ethics-responsibility-and-sustainability", form: "ethics, responsibility and sustainability (ERS)", lang: "en", partOfSpeech: "noun-phrase", termStatus: "preferred", register: "formal" }
- { concept: "enterprise-and-entrepreneurship-education", form: "Enterprise and entrepreneurship education (EED)", lang: "en", partOfSpeech: "noun-phrase", termStatus: "preferred", register: "formal" }
- { concept: "threshold-typical-excellent", form: "'Threshold', 'Typical', 'Excellent'", lang: "en", partOfSpeech: "noun", termStatus: "preferred", register: "formal" }
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
  title: "Subject Benchmark Statement Business and Management"
  edition: "March 2023 (fifth edition)"
  year: 2023
  url: unknown (the QAA page; the text came by stan's extraction)
  retrieved: "held from stan: wkspc2615-QAAVector mapped/business-and-management-2023/business-and-management-2023.raw.txt, commit 366bcb99a01118f2c4c3ebfa2a8337596bddc455; received 2026-10-03"
  licence: QAA copyright
  tier: primary
  readVia: direct
  held: 593f2b9d5e9ea16385308ba792eacfe50224b5a71603966adb80cbf9b22fb2ce
  heldFiles: ["wkspc2601-library/txt/qaa-2023-business-management-subject-benchmark-statement-standard.txt", "wkspc2601-library/txt/qaa-2023-business-management-subject-benchmark-statement-standard.norm.txt", "wkspc2601-library/records/qaa-2023-business-management-subject-benchmark-statement-standard.chunks.json", "wkspc2601-library/records/qaa-2023-business-management-subject-benchmark-statement-standard.held.json"]
  citedIn: [S1, S2, S3, S4, S4a, S5, S6, S7, SB1, SB2, SB3, SB4, SB5, SB6]
```

### D2 Research log
```yaml
- { ref: D1, tier: primary, consulted: 2026-10-03, pass: P1, outcome: "read whole, direct, from the normalised text; skeleton by tools/std_prep.py, document by tools/bm_build.py" }
- { ref: "ADAPT subj HESA stores, cah.json and hecos.json (designs/ingest/standards/subj/vocab)", tier: primary, consulted: 2026-10-03, pass: P1, outcome: "codes for statedSubjects and subjects" }
```

### D3 Wanted sources
```yaml
- { w: "W-std-0036", source: "QAA Characteristics Statement: Higher Education in Apprenticeships (2022)", why: "cited in 1.2 for degree apprenticeships; not ingested" }
- { w: "W-std-0038", source: "QAA Characteristics Statement: Micro-Credentials", why: "cited in 2.12; not ingested" }
- { w: "W-std-0040", source: "QAA Subject Benchmark Statement: Business and Management (2019, fourth edition)", why: "the edition this one supersedes, for the change comparison" }
```

## Part E Gaps and questions
- Rungs: three, each a lead-in with five items in five named categories (knowledge and understanding, skills, critical perspective, application, values); the lead-ins tie each rung to a degree class (honours, second class, first class), which Psychology does not do. gradeOf recorded as stated, since the issuer labels each item with the same category at every rung; P3 to confirm that the shared label counts as pairing.
- Typical lead-in (4.6) reads "will typically have demonstrated" and names "a second class honours degree" without splitting 2.1 and 2.2; recorded as force will and set beside Annex D at both 2.2 and 2.1.
- Domains on the rungs: the "skills" items (4.5.b2, 4.6.b2, 4.7.b2) cover subject-specific and generic skills together; recorded as subject-skill. "Critical perspective" recorded as understanding, "application" as subject-skill, "values" (global social responsibility) as generic-skill at fheq:6. All inferred: P3.
- Outcome list 3.7 (lead-in "should reasonably be expected to be able to demonstrate"): ten areas, force should; a new lead-in wording against Psychology ("are able to").
- Lists 3.10 and 3.11 have no modal in their lead-ins ("include"); recorded as outcome items with force describes, since 3.9 ("should be able to demonstrate") governs them; P3 to rule whether they take 3.9's should.
- Obliging words outside the five, recorded as describes: 1.26 "needs to be integrated" (also "imperative", "a requirement for planetary survival"); 3.20 "need to be a reliable means". Not cut: 3.16 "They need to take account" (across a page break, a plain-present teaching norm), 3.19 "It is important that", 1.16 "It is important that", 2.7 "it is expected that" (recorded with will), 4.3 "it is expected that most students should".
- Plain-present provider norms, not statements (template open point 5): 1.4 the four purposes ("are to"), 1.11, 2.1 to 2.6, 2.17, 3.1, 3.8, 3.12 ("the course enables graduates to develop and demonstrate"), 3.14, 3.15, 3.16, 3.17, 3.21, 3.22.
- Not statements, judged: 1.5 and 1.7 ("should be understood", definitions, to Part B); 1.6 ("will incorporate", a definition); 1.20, 1.22 items, 1.26 items, 2.12 items, 2.14 items, 3.16 items and 3.20 items (examples or options with may, could or typically); 2.19 (describes external examining); 4.1 (introduces the rungs); 4.4 (rung bases, in SB4).
- 1.22 cut by find to its obliging sentence only; its list (taking actions, ensuring access, confirming assessments, remaining mindful) follows "It may include" and is not cut.
- Skeleton corrections: 3.7.b10 ended in the heading "Skills and practice" and 4.6.b5 in "Excellent level"; both recut by find. 3.10.b3 was cut at a page break; recut by find to include its second half (the span holds the page number 15). 4.4.b5 holds the heading "Threshold level" but 4.4 is not a statement.
- Skeleton candidate 2.16.b1 is the tail of 2.16 after a footnote marker, not a list item; 2.16 is descriptive (may).
- Repeated numbers: the footnote marker "1" after 2.16 and its text (the expansions of CABS, BAM, AACSB, EFMD, PRME) sit inside 2.16 and 2.19 in the held text; not statements.
- Inferred subject codes (P3 to confirm; held back from lookup): hecos 100079 business studies, hecos 100089 management studies.
- Awards: honours is the award of the rungs; 1.2 extends use to the first-degree elements of integrated master's (FHEQ 7, FQHEIS 11, 2.10) and to degree apprenticeships; awardsCovered keeps honours only. CertHE and DipHE (2.9) are exit awards; fheq:4 and fheq:5 inferred.
- CQFW: not named in the text, though the statement is a key reference point in Wales; fheq:6 to cqfw:6 recorded as inferred from the FHEQ document.
- Annex D is cited as QAA 2019 (section 5); linked to its current home in std:doc:qaa-fheq-2024-framework (recall that the 2024 Frameworks carry it: confirmed in that document's SL6).
- Allied statements in 1.2 are named without editions; the held editions (accounting 2025, economics 2023, finance 2025) may postdate this statement. No events, hospitality, leisure, sport and tourism statement is held.
- Masters Degrees in Business and Management (2023) is a separate statement, not named in this text; any link is inferred and left for P3.
- Theme: employability is named in the front matter with enterprise ("employability, entrepreneurship and enterprise education"); recorded under theme:enterprise as Psychology did. No generative AI section.
- Bodies: PRME, CABS, BAM, AACSB and EFMD are named in 2.16 and its footnote; CMI appears only in section 5 and the advisory group; the Office for Students only in the front matter. Accrediting bodies (1.25) and PSRBs are unnamed. None of their requirements is ingested.
- S9 commentary not researched in P1.
- Licence: QAA copyright; the document gives no re-use terms in its text.
- ST-12: versions here run to the lengths the content needs; no length range is yet set.

---

## Change notes
- 0.1.2, 3 October 2026, 21:02: moved with its held text from UNI to the source library repo (`wkspc2601-library/ingested/standards/`, texts in `txt/`, records in `records/`); paths only (Abbott, 20:56; std N-0119).
- 0.1.1, 3 October 2026, 20:20: obliging words outside the five read as must, "ought to" as should, on statements outside the rungs, each marked on its force line (Abbott, 20:17; D-std-0016).
- 0.1.0, 2026-10-03 16:33: researched by run frame 0.1.1-draft and standards run layer 0.7.0-draft, std, run 0091 (P1); built by tools/bm_build.py.
