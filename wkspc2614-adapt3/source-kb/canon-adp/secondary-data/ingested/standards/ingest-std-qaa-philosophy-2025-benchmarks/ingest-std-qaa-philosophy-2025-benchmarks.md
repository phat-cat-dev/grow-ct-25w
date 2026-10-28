---
id: std:doc:qaa-philosophy-2025-benchmarks
title: "Subject Benchmark Statement Philosophy"
profile: standards/subject-benchmark
profileVersion: 0.2.0-draft
issuer: QAA
kind: subject-benchmark
jurisdiction: [UK]
subjectScope: subjects
subjects:
  - { scheme: "hecos", code: "100337", label: "philosophy", basis: "stated" }
  - { scheme: "cah", code: "CAH20-02-01", label: "philosophy", basis: "stated" }
  - { scheme: "hecos", code: "101441", label: "metaphysics", basis: "stated" }
  - { scheme: "hecos", code: "101442", label: "epistemology", basis: "stated" }
  - { scheme: "hecos", code: "100793", label: "ethics", basis: "stated" }
  - { scheme: "hecos", code: "100792", label: "social philosophy", basis: "stated" }
  - { scheme: "hecos", code: "100338", label: "philosophy of science", basis: "stated" }
  - { scheme: "hecos", code: "100791", label: "mental philosophy", basis: "inferred" }
edition: "April 2025"
published: 2025-04
status: current
supersedes: "the previous Philosophy statement (named only as \"the previous Subject Benchmark Statement\"; 2019 minor update by the advisory group lists: Part E)"
heldText: { method: sha256-bytes, raw: 08aa2558e79693d680e19c26a51391ac58b6e1925c502159fe8265b42ad7ad86, normalised: b6dd7181c2bd0ee3651b13a3be752fb9e5b9c2901c199b823456876560b0b807 }
heldTextStan: { method: sha256-stan, raw: 08aa2558e79693d680e19c26a51391ac58b6e1925c502159fe8265b42ad7ad86, normalised: a8ec849457c099172b9c59129acff1a2c08293e4b79068f9cc5bf65065d37a1d }
licence: "QAA copyright; held for study, private to the project, never published"
series: "QAA Subject Benchmark Statements, with the cross-cutting themes; this statement's fifth edition (D1, back matter)"
awardsCovered: ["bachelor's with honours", "master's"]
levelsCovered: ["fheq:6", "fheq:7", "fqheis:10", "fqheis:11"]
nations: ["England", "Wales", "Scotland", "Northern Ireland"]
parts:
  S: full
  B: "partial: no glossary in the document (it points to QAA's Glossary); terms it defines in passing"
  C: "not-applicable: the document sets expectations, not a procedure"
pins: { structure: 0.13.0-draft, template: 0.8.0-draft, benchmarkTemplate: 0.6.0-draft, runFrame: 0.1.1-draft, runLayer: 0.7.0-draft, standards: none yet, terminology: none yet }
lifecycle: drafted
researchedBy: run frame 0.1.1-draft; standards run layer 0.7.0-draft; std, run 0124 (tools/bm_build.py)
passes:
  P1: "2026-10-03 18:26"
  P2: "skipped: read direct from the held text; inferred codes and rung links are for P3"
  P3: open
version: 0.1.2
---

<!-- from INGEST wpk-0016-ingest-pd-template-standards.md 0.8.0-draft and wpk-0016-ingest-pd-template-standards-benchmark.md 0.6.0-draft; built by tools/bm_build.py from run-src/ -->
# Subject Benchmark Statement: Philosophy (QAA, April 2025)

> Run 0124, P1 by std. The issuer's words are held in the source library, `wkspc2601-library/txt/qaa-2025-philosophy-subject-benchmark-statement-standard.norm.txt`; each S4 record carries its statement in full (`source`) for language analysis, with its span. Paraphrases and versions are ours. Private to the project, never published. In front matter `status` is the issuer's; ours is `lifecycle`. Doubts are in Part E.

## Part 0 Summary

### 0.1 Agent definition
<!-- label: editorial; status: drafted; basis: primary -->
QAA's UK reference point for what a Philosophy graduate knows and can do at the end of a single honours degree, with a shorter list for the master's degree. Its core is two rung tables (knowledge and understanding; subject and intellectual skills), each row given at threshold, typical and excellent, matched to third, second and first-class degrees, plus a list of generic skills. Reach for it when designing, reviewing or describing a philosophy course or its outcomes. It is not a curriculum, not a set of competence standards and not a regulatory requirement in England.

### 0.2 Summary
<!-- label: both; status: drafted; basis: primary -->
Published by QAA in April 2025, the statement describes philosophy as a pluralistic sense-making discipline, sets out the five cross-cutting themes (equity, diversity and inclusion; accessibility and the needs of disabled students; education for sustainable development; employability, enterprise and entrepreneurship education; generative artificial intelligence) and the degree's design, progression and delivery. Its benchmark standards for bachelor's degrees with honours are a knowledge table of five rows and a skills table of nine rows, each at threshold, typical and excellent, and a list of twelve generic skills; a further twelve outcomes are given for master's degrees. It cites the FHEQ and the FQHEIS levels, points providers to Annex D of the 2024 Frameworks for the degree classes and to the 2021 Advance HE and QAA guidance on education for sustainable development. No professional body accredits the subject; PSRBs are named only in general.

## Part S Standard

### S1 Identity
<!-- label: source; status: drafted; basis: primary -->
```yaml
issuer: The Quality Assurance Agency for Higher Education
title: "Subject Benchmark Statement Philosophy"
edition: "April 2025"
dates:
  published: 2025-04
  other: []
kind: subject-benchmark
jurisdiction: [UK]
authority: "reference: a sector reference point, \"not a regulatory requirement\" (D1, front matter); in England not a sector-recognised standard under the OfS regulatory framework; part of the current quality arrangements in Scotland, Wales and Northern Ireland (D1, front matter: Relationship to legislation)"
licence: "QAA copyright; the document gives no re-use terms in its text (D1, front matter)"
copyrightNotice: { text: "© The Quality Assurance Agency for Higher Education 2024", locator: "D1, index" }
```

### S2 Purpose and scope
<!-- label: source; status: drafted; basis: primary -->
```yaml
governs: "what a Philosophy graduate can be expected to know, do and understand at the end of an honours degree and the nature of awards in the subject, with outcomes for a master's degree (D1, front matter: About this Statement; 4.1; 4.11)"
appliesTo:
  awards: ["bachelor's degrees with honours, single honours above all (4.5)", "joint and combined honours (2.9, 4.5)", "master's degrees (2.11, 4.11)", "integrated master's (described, 2.7, 2.13)"]
  levels: ["fheq:6", "fheq:7", "fqheis:10", "fqheis:11"]
  providers: ["UK higher education providers"]
whoMustUse: "none-stated; it is a reference point, not a requirement (D1, front matter)"
howUsed: ["design", "approval", "review", "other: external examining; PSRBs; information for prospective students and employers"]
doesNot: "it does not prescribe teaching, learning or assessment or interpret legislation; it carries no statutory or regulatory requirements; its rungs are not universal competence standards (D1, front matter; 4.3)"
beneficiary: the student
statedScope: "\"This QAA Subject Benchmark Statement for Philosophy defines what can be expected of a graduate in terms of what they might know, do and understand at the end of their studies.\" (D1, front matter: About this Statement)"
statedSubjects:
  - { name: "Philosophy", locator: "(D1, title; 1.1)", kind: "subject", codes: [{ scheme: "hecos", code: "100337", label: "philosophy" }, { scheme: "cah", code: "CAH20-02-01", label: "philosophy" }] }
  - { name: "logic, metaphysics, epistemology or philosophy of mind", locator: "(D1, 3.6; 4.6)", kind: "specialism", codes: [{ scheme: "hecos", code: "101441", label: "metaphysics" }, { scheme: "hecos", code: "101442", label: "epistemology" }, { scheme: "hecos", code: "100791", label: "mental philosophy" }] }
  - { name: "moral, political or social philosophy", locator: "(D1, 3.6; 4.6)", kind: "specialism", codes: [{ scheme: "hecos", code: "100793", label: "ethics" }, { scheme: "hecos", code: "100792", label: "social philosophy" }] }
  - { name: "applied ethics", locator: "(D1, 3.3)", kind: "specialism", codes: [{ scheme: "hecos", code: "100793", label: "ethics" }] }
  - { name: "aesthetics", locator: "(D1, 3.6)", kind: "specialism", codes: [] }
  - { name: "history and philosophy of science", locator: "(D1, 3.7)", kind: "programme title", codes: [{ scheme: "hecos", code: "100338", label: "philosophy of science" }] }
  - { name: "joint programmes with Business Studies, Classical Civilisations, Economics and others", locator: "(D1, 1.22)", kind: "programme title", codes: [{ scheme: "hecos", code: "100337", label: "philosophy" }] }
  - { name: "Foundation and Liberal Arts programmes that have Philosophy as a part", locator: "(D1, 1.22)", kind: "programme title", codes: [{ scheme: "hecos", code: "100065", label: "liberal arts" }] }
subjects: see front matter (subjectScope subjects)
```

### S3 Structure
<!-- label: both; status: drafted; basis: primary -->
```yaml
components:
  - { number: "1.1", order: 3, componentType: paragraph, parent: "section 1", heading: "Context and purposes of a Philosophy degree", gloss: "philosophy as sense-making that underpins other fields and joins the humanities and the sciences" }
  - { number: "1.2", order: 4, componentType: paragraph, parent: "section 1", heading: "Purposes and characteristics", gloss: "the large questions and the clarifying, dialogue-building role" }
  - { number: "1.3", order: 5, componentType: stem, parent: "section 1", heading: "Purposes and characteristics", gloss: "fourteen benefits of studying the subject, from analysis to applying it in policy" }
  - { number: "1.4", order: 6, componentType: stem, parent: "section 1", heading: "Purposes and characteristics", gloss: "ten wider social purposes of the degree, from logic training to democratic life" }
  - { number: "1.5", order: 7, componentType: paragraph, parent: "section 1", heading: "Equity, diversity and inclusion: Enabling potential", gloss: "little school-level philosophy, so courses serve beginners and those with a prior qualification" }
  - { number: "1.6", order: 8, componentType: paragraph, parent: "section 1", heading: "Equity, diversity and inclusion: Enabling potential", gloss: "varied materials, flexible activities, asynchronous options and a widening range of assessment" }
  - { number: "1.7", order: 9, componentType: paragraph, parent: "section 1", heading: "Equity, diversity and inclusion: Enabling potential", gloss: "a safe environment for controversial views and attention to opponents" }
  - { number: "1.8", order: 10, componentType: paragraph, parent: "section 1", heading: "Equity, diversity and inclusion: Enabling potential", gloss: "a co-created, inclusive community of enquiry; changing one's mind takes time" }
  - { number: "1.9", order: 11, componentType: paragraph, parent: "section 1", heading: "Equity, diversity and inclusion: Nurturing belonging and engagement", gloss: "diversifying a curriculum long dominated by privileged European men" }
  - { number: "1.10", order: 12, componentType: paragraph, parent: "section 1", heading: "Equity, diversity and inclusion: Nurturing belonging and engagement", gloss: "the risk of an adversarial culture; the Equality Act 2010 and the Public Sector Equality Duty" }
  - { number: "1.11", order: 13, componentType: paragraph, parent: "section 1", heading: "Equity, diversity and inclusion: Increasing awareness and understanding", gloss: "outward-looking comparison of traditions; graduates should be adept at it" }
  - { number: "1.12", order: 14, componentType: paragraph, parent: "section 1", heading: "Equity, diversity and inclusion: Developing self-reflection", gloss: "plurality, situating one's own view, reflective logs" }
  - { number: "1.13", order: 15, componentType: stem, parent: "section 1", heading: "Accessibility and the needs of disabled students", gloss: "an anticipatory approach to accessibility in three practices" }
  - { number: "1.14", order: 16, componentType: paragraph, parent: "section 1", heading: "Accessibility and the needs of disabled students", gloss: "reasonable adjustments so all students feel at home" }
  - { number: "1.15", order: 17, componentType: paragraph, parent: "section 1", heading: "Accessibility and the needs of disabled students", gloss: "audio and audiovisual material and library resourcing" }
  - { number: "1.16", order: 18, componentType: paragraph, parent: "section 1", heading: "Accessibility and the needs of disabled students", gloss: "disabled students' insight as a contribution to debate" }
  - { number: "1.17", order: 19, componentType: paragraph, parent: "section 1", heading: "Education for sustainable development", gloss: "sustainability defined as a moral attribute of acts and institutions" }
  - { number: "1.18", order: 20, componentType: paragraph, parent: "section 1", heading: "Education for sustainable development", gloss: "the UN SDGs and the 2021 ESD guidance as a core resource" }
  - { number: "1.19", order: 21, componentType: paragraph, parent: "section 1", heading: "Education for sustainable development", gloss: "two roles: critique of the concept and resources for sustainable living" }
  - { number: "1.20", order: 22, componentType: paragraph, parent: "section 1", heading: "Employability, enterprise and entrepreneurship education", gloss: "what employability, enterprise and entrepreneurship education does" }
  - { number: "1.21", order: 23, componentType: paragraph, parent: "section 1", heading: "Employability, enterprise and entrepreneurship education", gloss: "clear thinking, logic and argument as employability skills" }
  - { number: "1.22", order: 24, componentType: paragraph, parent: "section 1", heading: "Employability, enterprise and entrepreneurship education", gloss: "joint, foundation and liberal arts programmes" }
  - { number: "1.23", order: 25, componentType: paragraph, parent: "section 1", heading: "Employability, enterprise and entrepreneurship education", gloss: "placement years, internships and years abroad" }
  - { number: "1.24", order: 26, componentType: paragraph, parent: "section 1", heading: "Employability, enterprise and entrepreneurship education", gloss: "assessments that build employability, such as policy briefs" }
  - { number: "1.25", order: 27, componentType: paragraph, parent: "section 1", heading: "Employability, enterprise and entrepreneurship education", gloss: "funding and support for social enterprise" }
  - { number: "1.26", order: 28, componentType: paragraph, parent: "section 1", heading: "Employability, enterprise and entrepreneurship education", gloss: "leadership strengths of graduates" }
  - { number: "1.27", order: 29, componentType: paragraph, parent: "section 1", heading: "Employability, enterprise and entrepreneurship education", gloss: "the sectors graduates enter" }
  - { number: "1.28", order: 30, componentType: paragraph, parent: "section 1", heading: "Generative artificial intelligence", gloss: "GenAI set against the principal skills of the degree" }
  - { number: "1.29", order: 31, componentType: stem, parent: "section 1", heading: "Generative artificial intelligence", gloss: "three formative benefits of GenAI" }
  - { number: "1.30", order: 32, componentType: stem, parent: "section 1", heading: "Generative artificial intelligence", gloss: "four risks of GenAI to learning" }
  - { number: "1.31", order: 33, componentType: stem, parent: "section 1", heading: "Generative artificial intelligence", gloss: "GenAI in assessment: the essay challenge and three opportunities" }
  - { number: "1.32", order: 34, componentType: stem, parent: "section 1", heading: "Generative artificial intelligence", gloss: "two assessment risks: integrity and autonomous writing" }
  - { number: "1.33", order: 35, componentType: stem, parent: "section 1", heading: "Generative artificial intelligence", gloss: "GenAI as more than a tool: three points of focus" }
  - { number: "2.1", order: 37, componentType: paragraph, parent: "section 2", heading: "Design", gloss: "three or four levels of historical, thematic and skills modules" }
  - { number: "2.2", order: 38, componentType: paragraph, parent: "section 2", heading: "Design", gloss: "first-year design at FHEQ 4 and FQHEIS 7" }
  - { number: "2.3", order: 39, componentType: paragraph, parent: "section 2", heading: "Design", gloss: "second-year design at FHEQ 5 and FQHEIS 8" }
  - { number: "2.4", order: 40, componentType: paragraph, parent: "section 2", heading: "Design", gloss: "final-year design at FHEQ 6 and FQHEIS 9 or 10" }
  - { number: "2.5", order: 41, componentType: paragraph, parent: "section 2", heading: "Design", gloss: "interdisciplinary learning in joint and combined degrees" }
  - { number: "2.6", order: 42, componentType: paragraph, parent: "section 2", heading: "Design", gloss: "philosophers teaching concepts within other disciplines' accredited degrees" }
  - { number: "2.7", order: 43, componentType: paragraph, parent: "section 2", heading: "Progression", gloss: "progression through the levels towards the threshold skills" }
  - { number: "2.8", order: 44, componentType: paragraph, parent: "section 2", heading: "Progression", gloss: "a second or better as readiness for postgraduate study" }
  - { number: "2.9", order: 45, componentType: paragraph, parent: "section 2", heading: "Progression", gloss: "joint and combined students reach the core skills and add others" }
  - { number: "2.10", order: 46, componentType: paragraph, parent: "section 2", heading: "Progression", gloss: "early exit with a CertHE or DipHE" }
  - { number: "2.11", order: 47, componentType: paragraph, parent: "section 2", heading: "Progression", gloss: "the master's degree: advanced optional and some compulsory modules" }
  - { number: "2.12", order: 48, componentType: paragraph, parent: "section 2", heading: "Progression", gloss: "a merit or better as readiness for doctoral study" }
  - { number: "2.13", order: 49, componentType: paragraph, parent: "section 2", heading: "Flexibility", gloss: "typical course lengths across the UK nations; part-time credit" }
  - { number: "2.14", order: 50, componentType: paragraph, parent: "section 2", heading: "Flexibility", gloss: "modes of delivery and ways of accumulating credit" }
  - { number: "2.15", order: 51, componentType: paragraph, parent: "section 2", heading: "Partnership", gloss: "partnership delivery through validation and franchising" }
  - { number: "2.16", order: 52, componentType: paragraph, parent: "section 2", heading: "Monitoring and review", gloss: "routine monitoring, periodic review and the student voice" }
  - { number: "2.17", order: 53, componentType: paragraph, parent: "section 2", heading: "Monitoring and review", gloss: "external reviewers in periodic review" }
  - { number: "2.18", order: 54, componentType: paragraph, parent: "section 2", heading: "Monitoring and review", gloss: "external examiners and threshold standards" }
  - { number: "2.19", order: 55, componentType: paragraph, parent: "section 2", heading: "Monitoring and review", gloss: "accreditation for courses with professional outcomes" }
  - { number: "3.1", order: 57, componentType: paragraph, parent: "section 3", heading: "Content, structure and delivery", gloss: "what this section covers" }
  - { number: "3.2", order: 58, componentType: area, parent: "section 3", heading: "Content", gloss: "traditions and methods of a pluralistic subject" }
  - { number: "3.3", order: 59, componentType: area, parent: "section 3", heading: "Content", gloss: "three typical areas of study" }
  - { number: "3.4", order: 60, componentType: paragraph, parent: "section 3", heading: "Content", gloss: "traditions share features and are not to be assumed opposed" }
  - { number: "3.5", order: 61, componentType: paragraph, parent: "section 3", heading: "Content", gloss: "study is necessarily selective" }
  - { number: "3.6", order: 62, componentType: area, parent: "section 3", heading: "Content", gloss: "five things single honours courses typically include" }
  - { number: "3.7", order: 63, componentType: area, parent: "section 3", heading: "Content", gloss: "joint honours, specialist courses and interdisciplinary modules" }
  - { number: "3.8", order: 64, componentType: practice, parent: "section 3", heading: "Teaching and learning", gloss: "doing philosophy; balancing knowledge with discussion and response" }
  - { number: "3.9", order: 65, componentType: practice, parent: "section 3", heading: "Teaching and learning", gloss: "student-led research, peer exchange and self-direction in every programme" }
  - { number: "3.10", order: 66, componentType: practice, parent: "section 3", heading: "Teaching and learning: Learning in Philosophy is an active process", gloss: "three active modes of learning in any module" }
  - { number: "3.11", order: 67, componentType: practice, parent: "section 3", heading: "Teaching and learning: Learning in Philosophy is an active process", gloss: "formal methods learned through graded exercises" }
  - { number: "3.12", order: 68, componentType: practice, parent: "section 3", heading: "Teaching and learning: Learning in Philosophy is progressive", gloss: "two orderings of progression" }
  - { number: "3.13", order: 69, componentType: practice, parent: "section 3", heading: "Teaching and learning: Learning in Philosophy is progressive", gloss: "two-year cycles; bringing diverse students together" }
  - { number: "3.14", order: 70, componentType: practice, parent: "section 3", heading: "Teaching and learning: Learning in Philosophy is progressive", gloss: "eight typical teaching and learning methods" }
  - { number: "3.15", order: 71, componentType: practice, parent: "section 3", heading: "Assessment", gloss: "what the suite of assessments tests" }
  - { number: "3.16", order: 72, componentType: practice, parent: "section 3", heading: "Assessment", gloss: "diverse ways of meeting learning outcomes" }
  - { number: "3.17", order: 73, componentType: practice, parent: "section 3", heading: "Assessment", gloss: "co-created, reflective assessment and eleven example methods" }
  - { number: "3.18", order: 74, componentType: practice, parent: "section 3", heading: "Assessment", gloss: "accessible alternatives and student-proposed assessment" }
  - { number: "3.19", order: 75, componentType: practice, parent: "section 3", heading: "Assessment", gloss: "integrity through authentic assessment; transparency with technology" }
  - { number: "4.1", order: 77, componentType: paragraph, parent: "section 4", heading: "Introduction", gloss: "the standards shown at the award of honours" }
  - { number: "4.2", order: 78, componentType: paragraph, parent: "section 4", heading: "Introduction", gloss: "most exceed threshold; providers refer to Annex D" }
  - { number: "4.3", order: 79, componentType: paragraph, parent: "section 4", heading: "Introduction", gloss: "rungs are not competence standards; EHRC guidance" }
  - { number: "4.4", order: 80, componentType: stem, parent: "section 4", heading: "Introduction", gloss: "the three rungs defined and matched to degree classes" }
  - { number: "4.5", order: 81, componentType: paragraph, parent: "section 4", heading: "Introduction", gloss: "rungs written for single honours; any module brings some competence" }
  - { number: "4.6", order: 82, componentType: paragraph, parent: "section 4", heading: "Subject-specific knowledge and understanding", gloss: "the knowledge and understanding table: five rows at three rungs" }
  - { number: "4.7", order: 83, componentType: paragraph, parent: "section 4", heading: "Subject-specific knowledge and understanding", gloss: "higher knowledge rungs include the lower" }
  - { number: "4.8", order: 84, componentType: paragraph, parent: "section 4", heading: "Subject-specific and intellectual skills", gloss: "the subject and intellectual skills table: nine rows at three rungs" }
  - { number: "4.9", order: 85, componentType: paragraph, parent: "section 4", heading: "Subject-specific and intellectual skills", gloss: "higher skill rungs include the lower" }
  - { number: "4.10", order: 86, componentType: stem, parent: "section 4", heading: "Generic skills", gloss: "twelve generic skills at undergraduate level" }
  - { number: "4.11", order: 87, componentType: stem, parent: "section 4", heading: "Master's level", gloss: "twelve outcomes for the master's degree" }
  - { number: "1", componentType: section, parent: none, heading: "Context and purposes of a Philosophy degree", gloss: "section 1" }
  - { number: "2", componentType: section, parent: none, heading: "Distinctive features of the Philosophy degree", gloss: "section 2" }
  - { number: "3", componentType: section, parent: none, heading: "Content, structure and delivery", gloss: "section 3" }
  - { number: "4", componentType: section, parent: none, heading: "Benchmark standards", gloss: "section 4" }
excluded:
  - { number: "none", heading: "About this Statement; How can I use this document?; Relationship to legislation; Additional sector reference points", kind: "other: front matter, read for S1, S2, SB5 and SB6" }
  - { number: "none", heading: "Contents", kind: "other: table of contents" }
  - { number: "section headings 1 to 4", heading: "section heading lines", kind: "other: headings, recorded in SECTIONS" }
  - { number: "5", heading: "List of references and further resources", kind: "other: back matter, read for SB6 and Part E" }
  - { number: "6", heading: "Membership of the Advisory Group", kind: "other: back matter, read for S7 (earlier editions) and S1 (publication date)" }
```

### S4 Statements
<!-- label: both; status: drafted; basis: primary. Only standards (D-std-0002 (a)): 81 records. `source` is the issuer's statement exactly as its span holds it (D-std-0014). -->
```yaml
- id: qaa/philosophy-2025/1.11
  locator: { number: "1.11", headingPath: ["Context and purposes of a Philosophy degree", "Equity, diversity and inclusion: Increasing awareness and understanding"] }
  span: { start: 16356, end: 16978 }
  source: "1.11 Philosophical discussion thrives when it is outward-looking, comparing and assessing alternative perspectives from different cultures and traditions. Philosophy teachers acknowledge this by including known alternative perspectives into the learning materials and discussions. Philosophy graduates should be adept at comparing and assessing alternative perspectives from different cultures and traditions. Philosophy courses employ different tools, teaching strategies and technologies to ensure that all students can have their voice heard in, and make contributions to, ongoing dialogues. Developing self-reflection\n"
  stem: none
  statementType: expectation
  rung: none
  force: should
  level: fheq:6
  appliesTo: "graduates of the subject"
  addressee: learner
  verbs: ["comparing", "assessing"]
  about: "comparing perspectives across cultures and traditions"
  themes: [theme:edi]
  domain: subject-skill
  award: ["bachelor's with honours"]
  gradeOf: none
  paraphrase: "Philosophical discussion flourishes when it looks outward; teachers bring views from other cultures and traditions into materials and discussion; graduates should be skilled at comparing and judging such views; courses use varied tools so every student is heard."
  quote: full   # the issuer's statement is in `source` (D-std-0014)
  audience: both
  subjects: inherited
- id: qaa/philosophy-2025/1.18
  locator: { number: "1.18", headingPath: ["Context and purposes of a Philosophy degree", "Education for sustainable development"] }
  span: { start: 20028, end: 20758 }
  source: "1.18 Some unsustainable acts and processes demand greater attention than others. This Subject Benchmark Statement takes its lead from the UN Sustainable Development Goals (SDGs), which, among other things, prioritise taking urgent action to combat climate change and its impacts; protect and restore terrestrial ecosystems; conserve the oceans and seas; make human settlements inclusive, safe and resilient; end poverty in all its forms everywhere; and empower and promote the social, economic and political inclusion of all. Philosophy aligns with the skills and learning outcomes of the Education f or Sustainable Development Guidance produced by Advance HE and QAA (March 2021) which should be consulted as a core resource.\n\n7\n"
  stem: none
  statementType: expectation
  rung: none
  force: should
  level: none
  appliesTo: "course teams in the subject"
  addressee: provider
  verbs: ["consulted"]
  about: "the 2021 ESD guidance as a core resource"
  themes: [theme:esd]
  domain: none
  award: ["none"]
  gradeOf: none
  paraphrase: "The statement follows the UN Sustainable Development Goals and their priorities on climate, ecosystems, oceans, settlements, poverty and inclusion; the subject fits the skills and outcomes of the 2021 Advance HE and QAA guidance on education for sustainable development, which course teams should consult as a core resource."
  quote: full   # the issuer's statement is in `source` (D-std-0014)
  audience: practitioner
  subjects: inherited
- id: qaa/philosophy-2025/2.9
  locator: { number: "2.9", headingPath: ["Distinctive features of the Philosophy degree", "Progression"] }
  span: { start: 33794, end: 34275 }
  source: "2.9 Undergraduates studying Philosophy as part of a combined or joint degree course with other subjects, including courses that provide for major and minor options, will achieve core elements of the specific and generic skills outlined in this Statement and will add others according to the areas covered in the other subject(s) of their degree. Additionally, they may explore the overlap between different disciplines, creating further opportunities for interdisciplinary study.\n\n"
  stem: none
  statementType: outcome
  rung: none
  force: will
  level: fheq:6
  appliesTo: "joint and combined honours students"
  addressee: learner
  verbs: ["achieve", "add"]
  about: "joint honours students reach the core skills"
  themes: [none]
  domain: subject-skill
  award: ["bachelor's with honours"]
  gradeOf: none
  paraphrase: "Students taking philosophy in a combined or joint degree, major and minor routes included, will reach the core of the subject-specific and generic skills the statement sets out and will add others from their other subject; they may also explore where the disciplines overlap."
  quote: full   # the issuer's statement is in `source` (D-std-0014)
  audience: both
  subjects: inherited
- id: qaa/philosophy-2025/2.17
  locator: { number: "2.17", headingPath: ["Distinctive features of the Philosophy degree", "Monitoring and review"] }
  span: { start: 37868, end: 38167 }
  source: "2.17 Externality is an essential component of the quality assurance system in the UK. Providers will use external reviewers as part of periodic review to gain an independent perspective on any proposed changes and ensure threshold standards are achieved and content is appropriate for the subject.\n\n"
  stem: none
  statementType: expectation
  rung: none
  force: will
  level: none
  appliesTo: "providers of the subject"
  addressee: provider
  verbs: ["use", "ensure"]
  about: "external reviewers in periodic review"
  themes: [none]
  domain: none
  award: ["none"]
  gradeOf: none
  paraphrase: "Externality is a core part of UK quality assurance; providers will bring in external reviewers during periodic review for an independent view of planned changes and to confirm that threshold standards are met and the content fits the subject."
  quote: full   # the issuer's statement is in `source` (D-std-0014)
  audience: practitioner
  subjects: inherited
- id: qaa/philosophy-2025/3.4
  locator: { number: "3.4", headingPath: ["Content, structure and delivery", "Content"] }
  span: { start: 41148, end: 41611 }
  source: "3.4 There is a variety of philosophical traditions, each with its own style, approach and characteristic concerns. However, there are a number of distinctive features common to the work of authors working within all these traditions, such as the emphasis on precision and clarity of expression, and the degree of self-reflection. It should not be assumed that these distinct traditions are inherently opposed to one another or cannot engage in fruitful dialogue.\n"
  stem: none
  statementType: expectation
  rung: none
  force: should
  level: none
  appliesTo: "anyone studying or teaching the subject"
  addressee: both
  verbs: ["assumed", "engage"]
  about: "traditions not to be assumed opposed"
  themes: [none]
  domain: understanding
  award: ["none"]
  gradeOf: none
  paraphrase: "Philosophy has many traditions, each with its own style and concerns, yet all share features such as precision, clarity and self-reflection; it should not be taken for granted that the traditions are at odds or unable to talk to each other."
  quote: full   # the issuer's statement is in `source` (D-std-0014)
  audience: both
  subjects: inherited
- id: qaa/philosophy-2025/3.8
  locator: { number: "3.8", headingPath: ["Content, structure and delivery", "Teaching and learning"] }
  span: { start: 43727, end: 44245 }
  source: "3.8 Philosophy programmes develop skills that enable students to do Philosophy rather than merely study a body of knowledge. It is therefore important that the teaching and learning strategies used model the practice of Philosophy and provide opportunities for students to develop skills and competencies in doing Philosophy. Opportunities to acquire knowledge and understanding of philosophical topics and thinkers must be balanced with opportunities for students to discuss, analyse and develop their own responses.\n"
  stem: none
  statementType: requirement
  rung: none
  force: must
  level: none
  appliesTo: "teaching and learning in the subject"
  addressee: provider
  verbs: ["balanced"]
  about: "balancing knowledge with doing philosophy"
  themes: [none]
  domain: none
  award: ["none"]
  gradeOf: none
  paraphrase: "Programmes build the skills to do philosophy, not only to study it, so it matters that teaching models philosophical practice; time for gaining knowledge of topics and thinkers must be balanced with time in which students discuss, analyse and work out their own responses."
  quote: full   # the issuer's statement is in `source` (D-std-0014)
  audience: practitioner
  subjects: inherited
- id: qaa/philosophy-2025/3.9
  locator: { number: "3.9", headingPath: ["Content, structure and delivery", "Teaching and learning"] }
  span: { start: 44245, end: 44717 }
  source: "3.9 Philosophy programmes will vary in size depending on the higher education provider. Consequently, there may be differences in the balance between online and in-person teaching and the variety of topics covered. However, all Philosophy programmes will incorporate a degree of student-led research, opportunities to exchange ideas with peers and allow students to be self-directed in questions addressed within their studies. Learning in Philosophy is an active process\n"
  stem: none
  statementType: expectation
  rung: none
  force: will
  level: none
  appliesTo: "every programme in the subject"
  addressee: provider
  verbs: ["incorporate", "allow"]
  about: "student-led research, peer exchange and self-direction"
  themes: [none]
  domain: none
  award: ["none"]
  gradeOf: none
  paraphrase: "Programmes differ in size, so the mix of online and in-person teaching and the range of topics vary; all programmes will nonetheless include some student-led research, chances to exchange ideas with peers and freedom for students to choose the questions they pursue."
  quote: full   # the issuer's statement is in `source` (D-std-0014)
  audience: practitioner
  subjects: inherited
- id: qaa/philosophy-2025/3.13
  locator: { number: "3.13", headingPath: ["Content, structure and delivery", "Teaching and learning: Learning in Philosophy is progressive"] }
  span: { start: 45972, end: 46717 }
  source: "3.13 It is recognised that many departments teach a variety of subjects in a two-year cycle in order to allow greater breadth of provision in the two final years. In such courses there is a progression in difficulty from the first year of study to the two final years. Teaching strategies in Philosophy rely on the diversity of thinkers and, therefore, teaching strategies will involve bringing students with different backgrounds together to tackle shared problems. In Philosophy, students are celebrated for their different perspectives. To ensure students are equally able to participate and develop skills, it is important that a range of different modes and opportunities are provided to facilitate discussion, whether online or in person.\n"
  stem: none
  statementType: expectation
  rung: none
  force: will
  level: none
  appliesTo: "teaching in the subject"
  addressee: provider
  verbs: ["involve", "bringing"]
  about: "bringing students of different backgrounds together"
  themes: [none]
  domain: none
  award: ["none"]
  gradeOf: none
  paraphrase: "Many departments teach some subjects in a two-year cycle, with difficulty rising towards the final years; because philosophy draws on diverse thinkers, teaching strategies will involve gathering students from different backgrounds around shared problems, and it is important to offer varied modes of discussion, online or in person."
  quote: full   # the issuer's statement is in `source` (D-std-0014)
  audience: practitioner
  subjects: inherited
- id: qaa/philosophy-2025/3.15.b1
  locator: { number: "3.15.b1", headingPath: ["Content, structure and delivery", "Assessment"] }
  span: { start: 47694, end: 47721 }
  source: "knowledge and understanding"
  stem: "3.15"
  statementType: expectation
  rung: none
  force: will
  level: none
  appliesTo: "the assessment suite of every programme"
  addressee: provider
  verbs: []
  about: "assessment tests knowledge and understanding"
  themes: [none]
  domain: none
  award: ["none"]
  gradeOf: none
  paraphrase: "Each programme's set of assessments will test students' knowledge and understanding, balanced against their competence in philosophical skills and methods."
  quote: full   # the issuer's statement is in `source` (D-std-0014)
  audience: practitioner
  subjects: inherited
- id: qaa/philosophy-2025/3.15.b2
  locator: { number: "3.15.b2", headingPath: ["Content, structure and delivery", "Assessment"] }
  span: { start: 47724, end: 47835 }
  source: "argument and analysis: demonstrating the ability to reason rigorously, critically, creatively and independently"
  stem: "3.15"
  statementType: expectation
  rung: none
  force: will
  level: none
  appliesTo: "the assessment suite of every programme"
  addressee: provider
  verbs: ["demonstrating", "reason"]
  about: "assessment tests argument and analysis"
  themes: [none]
  domain: none
  award: ["none"]
  gradeOf: none
  paraphrase: "Each programme's assessments will test argument and analysis: reasoning with rigour, critically, creatively and independently."
  quote: full   # the issuer's statement is in `source` (D-std-0014)
  audience: practitioner
  subjects: inherited
- id: qaa/philosophy-2025/3.15.b3
  locator: { number: "3.15.b3", headingPath: ["Content, structure and delivery", "Assessment"] }
  span: { start: 47838, end: 47927 }
  source: "presentation: demonstrating the ability to communicate clearly, reliably and effectively."
  stem: "3.15"
  statementType: expectation
  rung: none
  force: will
  level: none
  appliesTo: "the assessment suite of every programme"
  addressee: provider
  verbs: ["demonstrating", "communicate"]
  about: "assessment tests presentation"
  themes: [none]
  domain: none
  award: ["none"]
  gradeOf: none
  paraphrase: "Each programme's assessments will test presentation: getting ideas across clearly, reliably and effectively."
  quote: full   # the issuer's statement is in `source` (D-std-0014)
  audience: practitioner
  subjects: inherited
- id: qaa/philosophy-2025/3.19
  locator: { number: "3.19", headingPath: ["Content, structure and delivery", "Assessment"] }
  span: { start: 49554, end: 50207 }
  source: "3.19 Academic integrity is promoted through the emphasis on authentic assessment, developing novel examples and drawing on personal experience to support the arguments and analysis of the course material. Students are encouraged to respond to the work of others rather than merely reporting its content, thereby promoting good practices in referencing, citation and research. Where technologies are used in assessment, transparency must be ensured. To support learning, in particular the development of philosophical skills and competencies, opportunities are provided for self and peer assessment, with clear marking criteria provided to students.\n\n17\n"
  stem: none
  statementType: requirement
  rung: none
  force: must
  level: none
  appliesTo: "assessment in the subject"
  addressee: provider
  verbs: ["ensured", "promoted"]
  about: "transparency where technology is used in assessment"
  themes: [none]
  domain: none
  award: ["none"]
  gradeOf: none
  paraphrase: "Authentic assessment, fresh examples and personal experience promote academic integrity, and students respond to others' work rather than report it; any use of technology in assessment must be transparent; self and peer assessment with clear marking criteria support learning."
  quote: full   # the issuer's statement is in `source` (D-std-0014)
  audience: practitioner
  subjects: inherited
- id: qaa/philosophy-2025/4.2
  locator: { number: "4.2", headingPath: ["Benchmark standards", "Introduction"] }
  span: { start: 50590, end: 51043 }
  source: "4.2 Most students will attain more than the minimum threshold standards. Each higher education provider has its own method of determining what appropriate evidence of this achievement will be and should refer to Annex D of the Frameworks for Higher Education Qualifications of UK Degree-Awarding Bodies. This Annex sets out common descriptions of the four main degree outcome classifications for bachelor's degrees with honours: 1st, 2.1,\n2.2 and 3 rd.\n"
  stem: none
  statementType: expectation
  rung: none
  force: should
  level: fheq:6
  appliesTo: "providers awarding honours in the subject"
  addressee: provider
  verbs: ["refer"]
  about: "referring to Annex D for achievement above threshold"
  themes: [none]
  domain: none
  award: ["bachelor's with honours"]
  gradeOf: none
  paraphrase: "Most students will go beyond the minimum threshold; each provider decides what counts as evidence of that and should refer to Annex D of the UK degree frameworks, which describes the four main honours classifications."
  quote: full   # the issuer's statement is in `source` (D-std-0014)
  audience: practitioner
  subjects: inherited
- id: qaa/philosophy-2025/4.3
  locator: { number: "4.3", headingPath: ["Benchmark standards", "Introduction"] }
  span: { start: 51043, end: 51584 }
  source: "4.3 Please note that the minimum threshold, typical and excellent standards for undergraduate and master's level are not intended to specify universal competence standards for a discipline. If a provider chooses to develop competence standards (as defined by the Equality Act 2010) as part of a programme specification, these can be informed by the relevant Subject B enchmark S tatement along with any PSRB requirements. In these circumstances providers should follow the most recent guidance from the Equality and Human Rights Commission.\n"
  stem: none
  statementType: expectation
  rung: none
  force: should
  level: none
  appliesTo: "providers that write competence standards"
  addressee: provider
  verbs: ["follow"]
  about: "competence standards and EHRC guidance"
  themes: [none]
  domain: none
  award: ["bachelor's with honours", "master's"]
  gradeOf: none
  paraphrase: "The three rungs, for undergraduate and master's study alike, do not set universal competence standards; a provider that develops competence standards under the Equality Act 2010 may draw on the statement and any PSRB requirements, and should then follow the latest Equality and Human Rights Commission guidance."
  quote: full   # the issuer's statement is in `source` (D-std-0014)
  audience: practitioner
  subjects: inherited
- id: qaa/philosophy-2025/4.5
  locator: { number: "4.5", headingPath: ["Benchmark standards", "Introduction"] }
  span: { start: 52037, end: 52679 }
  source: "4.5 Students study P hilosophy in single and joint honours degree courses, and as an element in modular degrees with other subject components. The descriptions given of attainment levels are intended to apply to single honours courses. The range of knowledge expected and the scope and measure of skills achieved by students studying Philosophy in lower proportions varies correspondingly. Students completing any philosophical module are expected to have competence in some general philosophical skills, and to have knowledge of texts and topics identified in the description of the module.\n\n18\nSubject-specific k nowledge and understanding\n"
  stem: none
  statementType: expectation
  rung: none
  force: must   # D-std-0016: "are expected to" read as must
  level: none
  appliesTo: "students completing any philosophy module"
  addressee: learner
  verbs: ["completing", "have"]
  about: "competence expected from any philosophy module"
  themes: [none]
  domain: subject-skill
  award: ["none"]
  gradeOf: none
  paraphrase: "Philosophy is studied in single and joint honours and within modular degrees; the rung descriptions are meant for single honours, and what is expected of students taking less philosophy scales accordingly; anyone completing a philosophy module is expected to have some general philosophical skills and to know the texts and topics in its description."
  quote: full   # the issuer's statement is in `source` (D-std-0014)
  audience: both
  subjects: inherited
- id: qaa/philosophy-2025/4.6.b1
  locator: { number: "4.6.b1", headingPath: ["Benchmark standards", "Subject-specific knowledge and understanding"] }
  span: { start: 52802, end: 52842 }
  source: "The writings of some major philosophers."
  stem: "4.6"
  statementType: threshold
  rung: threshold
  force: threshold
  level: fheq:6
  appliesTo: "single honours graduates at the threshold level"
  addressee: learner
  verbs: []
  about: "writings of some major philosophers"
  themes: [none]
  domain: knowledge
  award: ["bachelor's with honours"]
  gradeOf: none
  paraphrase: "At threshold, graduates will know and understand the work of a number of major philosophers, as set down in their own texts."
  quote: full   # the issuer's statement is in `source` (D-std-0014)
  audience: both
  subjects: inherited
- id: qaa/philosophy-2025/4.6.b1.excellent
  locator: { number: "4.6.b1.excellent", headingPath: ["Benchmark standards", "Subject-specific knowledge and understanding"] }
  span: { start: 53002, end: 53197 }
  source: "The theories and arguments of major philosophers, the associated important areas of interpretative controversy, plus an original interpretation that demonstrates a close reading of primary texts."
  stem: "4.6"
  statementType: excellent
  rung: excellent
  force: will
  level: fheq:6
  appliesTo: "single honours graduates at the excellent level"
  addressee: learner
  verbs: ["demonstrates"]
  about: "an original interpretation from close reading"
  themes: [none]
  domain: knowledge
  award: ["bachelor's with honours"]
  gradeOf: { statement: qaa/philosophy-2025/4.6.b1.typical, basis: stated }
  paraphrase: "At the excellent level, graduates will know major philosophers' theories, arguments and interpretative disputes and will offer a reading of their own grounded in close study of the original texts."
  quote: full   # the issuer's statement is in `source` (D-std-0014)
  audience: both
  subjects: inherited
- id: qaa/philosophy-2025/4.6.b1.typical
  locator: { number: "4.6.b1.typical", headingPath: ["Benchmark standards", "Subject-specific knowledge and understanding"] }
  span: { start: 52843, end: 53000 }
  source: "The theories and arguments of major philosophers, encountered in their own writings, along with the associated important areas of interpretative controversy."
  stem: "4.6"
  statementType: typical
  rung: typical
  force: will
  level: fheq:6
  appliesTo: "single honours graduates at the typical level"
  addressee: learner
  verbs: ["encountered"]
  about: "theories of major philosophers and the disputes over reading them"
  themes: [none]
  domain: knowledge
  award: ["bachelor's with honours"]
  gradeOf: { statement: qaa/philosophy-2025/4.6.b1, basis: stated }
  paraphrase: "Typically, graduates will know the theories and arguments of major philosophers, met in the original texts, together with the main disputes over how to read them."
  quote: full   # the issuer's statement is in `source` (D-std-0014)
  audience: both
  subjects: inherited
- id: qaa/philosophy-2025/4.6.b2
  locator: { number: "4.6.b2", headingPath: ["Benchmark standards", "Subject-specific knowledge and understanding"] }
  span: { start: 53198, end: 53326 }
  source: "Some central theories and arguments in the fields of logic, metaphysics, epistemology or philosophy of mind, broadly understood."
  stem: "4.6"
  statementType: threshold
  rung: threshold
  force: threshold
  level: fheq:6
  appliesTo: "single honours graduates at the threshold level"
  addressee: learner
  verbs: []
  about: "core theories in logic, metaphysics, epistemology or mind"
  themes: [none]
  domain: knowledge
  award: ["bachelor's with honours"]
  gradeOf: none
  paraphrase: "At threshold, graduates will know some core theories and arguments from logic, epistemology, metaphysics or the philosophy of mind, each taken in a wide sense."
  quote: full   # the issuer's statement is in `source` (D-std-0014)
  audience: both
  subjects: inherited
- id: qaa/philosophy-2025/4.6.b2.excellent
  locator: { number: "4.6.b2.excellent", headingPath: ["Benchmark standards", "Subject-specific knowledge and understanding"] }
  span: { start: 53464, end: 53705 }
  source: "Many of the theories and arguments in the fields of logic, metaphysics, epistemology or philosophy of mind, broadly understood, in a systematic, extensive and comparative way, demonstrating knowledge that may\n\nbe beyond what has been taught."
  stem: "4.6"
  statementType: excellent
  rung: excellent
  force: will
  level: fheq:6
  appliesTo: "single honours graduates at the excellent level"
  addressee: learner
  verbs: ["demonstrating"]
  about: "systematic, comparative command of theoretical philosophy"
  themes: [none]
  domain: knowledge
  award: ["bachelor's with honours"]
  gradeOf: { statement: qaa/philosophy-2025/4.6.b2.typical, basis: stated }
  paraphrase: "At the excellent level, graduates will know many theories and arguments in logic, epistemology, metaphysics or the philosophy of mind, systematically, widely and by comparison, possibly reaching past what they were taught."
  quote: full   # the issuer's statement is in `source` (D-std-0014)
  audience: both
  subjects: inherited
- id: qaa/philosophy-2025/4.6.b2.typical
  locator: { number: "4.6.b2.typical", headingPath: ["Benchmark standards", "Subject-specific knowledge and understanding"] }
  span: { start: 53327, end: 53462 }
  source: "More of the central theories and arguments in the fields of logic, metaphysics, epistemology or philosophy of mind, broadly understood."
  stem: "4.6"
  statementType: typical
  rung: typical
  force: will
  level: fheq:6
  appliesTo: "single honours graduates at the typical level"
  addressee: learner
  verbs: []
  about: "more of the core theories in theoretical philosophy"
  themes: [none]
  domain: knowledge
  award: ["bachelor's with honours"]
  gradeOf: { statement: qaa/philosophy-2025/4.6.b2, basis: stated }
  paraphrase: "Typically, graduates will know a wider share of the core theories and arguments in logic, epistemology, metaphysics or the philosophy of mind."
  quote: full   # the issuer's statement is in `source` (D-std-0014)
  audience: both
  subjects: inherited
- id: qaa/philosophy-2025/4.6.b3
  locator: { number: "4.6.b3", headingPath: ["Benchmark standards", "Subject-specific knowledge and understanding"] }
  span: { start: 53707, end: 53818 }
  source: "Some central theories and arguments in the fields of moral, political or social philosophy, broadly understood."
  stem: "4.6"
  statementType: threshold
  rung: threshold
  force: threshold
  level: fheq:6
  appliesTo: "single honours graduates at the threshold level"
  addressee: learner
  verbs: []
  about: "core theories in moral, political or social philosophy"
  themes: [none]
  domain: knowledge
  award: ["bachelor's with honours"]
  gradeOf: none
  paraphrase: "At threshold, graduates will know some core theories and arguments in ethics, political philosophy or social philosophy, each in a wide sense."
  quote: full   # the issuer's statement is in `source` (D-std-0014)
  audience: both
  subjects: inherited
- id: qaa/philosophy-2025/4.6.b3.excellent
  locator: { number: "4.6.b3.excellent", headingPath: ["Benchmark standards", "Subject-specific knowledge and understanding"] }
  span: { start: 53938, end: 54161 }
  source: "Many of the theories and arguments in the fields of moral, political or social philosophy, broadly understood, in a systematic, extensive and comparative way, demonstrating knowledge that may be beyond what has been taught."
  stem: "4.6"
  statementType: excellent
  rung: excellent
  force: will
  level: fheq:6
  appliesTo: "single honours graduates at the excellent level"
  addressee: learner
  verbs: ["demonstrating"]
  about: "systematic, comparative command of practical philosophy"
  themes: [none]
  domain: knowledge
  award: ["bachelor's with honours"]
  gradeOf: { statement: qaa/philosophy-2025/4.6.b3.typical, basis: stated }
  paraphrase: "At the excellent level, graduates will know many theories and arguments in ethics, political or social philosophy, systematically, widely and by comparison, possibly reaching past what they were taught."
  quote: full   # the issuer's statement is in `source` (D-std-0014)
  audience: both
  subjects: inherited
- id: qaa/philosophy-2025/4.6.b3.typical
  locator: { number: "4.6.b3.typical", headingPath: ["Benchmark standards", "Subject-specific knowledge and understanding"] }
  span: { start: 53819, end: 53937 }
  source: "More of the central theories and arguments in the fields of moral, political or social philosophy, broadly understood."
  stem: "4.6"
  statementType: typical
  rung: typical
  force: will
  level: fheq:6
  appliesTo: "single honours graduates at the typical level"
  addressee: learner
  verbs: []
  about: "more of the core theories in practical philosophy"
  themes: [none]
  domain: knowledge
  award: ["bachelor's with honours"]
  gradeOf: { statement: qaa/philosophy-2025/4.6.b3, basis: stated }
  paraphrase: "Typically, graduates will know a wider share of the core theories and arguments in ethics, political philosophy or social philosophy."
  quote: full   # the issuer's statement is in `source` (D-std-0014)
  audience: both
  subjects: inherited
- id: qaa/philosophy-2025/4.6.b4
  locator: { number: "4.6.b4", headingPath: ["Benchmark standards", "Subject-specific knowledge and understanding"] }
  span: { start: 54163, end: 54220 }
  source: "A limited range of techniques in philosophical reasoning."
  stem: "4.6"
  statementType: threshold
  rung: threshold
  force: threshold
  level: fheq:6
  appliesTo: "single honours graduates at the threshold level"
  addressee: learner
  verbs: []
  about: "a few techniques of philosophical reasoning"
  themes: [none]
  domain: understanding
  award: ["bachelor's with honours"]
  gradeOf: none
  paraphrase: "At threshold, graduates will know a narrow set of methods of philosophical reasoning."
  quote: full   # the issuer's statement is in `source` (D-std-0014)
  audience: both
  subjects: inherited
- id: qaa/philosophy-2025/4.6.b4.excellent
  locator: { number: "4.6.b4.excellent", headingPath: ["Benchmark standards", "Subject-specific knowledge and understanding"] }
  span: { start: 54347, end: 54495 }
  source: "An extensive range of techniques of philosophical reasoning, and of the philosophical critiques of, and debates around, philosophical methodologies."
  stem: "4.6"
  statementType: excellent
  rung: excellent
  force: will
  level: fheq:6
  appliesTo: "single honours graduates at the excellent level"
  addressee: learner
  verbs: []
  about: "an extensive repertoire and the debates over method"
  themes: [none]
  domain: understanding
  award: ["bachelor's with honours"]
  gradeOf: { statement: qaa/philosophy-2025/4.6.b4.typical, basis: stated }
  paraphrase: "At the excellent level, graduates will know a wide array of reasoning techniques together with the critiques of, and debates over, philosophical method."
  quote: full   # the issuer's statement is in `source` (D-std-0014)
  audience: both
  subjects: inherited
- id: qaa/philosophy-2025/4.6.b4.typical
  locator: { number: "4.6.b4.typical", headingPath: ["Benchmark standards", "Subject-specific knowledge and understanding"] }
  span: { start: 54221, end: 54345 }
  source: "A broader range of techniques of philosophical reasoning, and of the philosophical critiques of philosophical methodologies."
  stem: "4.6"
  statementType: typical
  rung: typical
  force: will
  level: fheq:6
  appliesTo: "single honours graduates at the typical level"
  addressee: learner
  verbs: []
  about: "wider techniques and critiques of method"
  themes: [none]
  domain: understanding
  award: ["bachelor's with honours"]
  gradeOf: { statement: qaa/philosophy-2025/4.6.b4, basis: stated }
  paraphrase: "Typically, graduates will know a wider set of reasoning techniques and the philosophical criticisms made of philosophy's own methods."
  quote: full   # the issuer's statement is in `source` (D-std-0014)
  audience: both
  subjects: inherited
- id: qaa/philosophy-2025/4.6.b5
  locator: { number: "4.6.b5", headingPath: ["Benchmark standards", "Subject-specific knowledge and understanding"] }
  span: { start: 54496, end: 54585 }
  source: "Some of the major issues currently at the frontiers of philosophical debate and research."
  stem: "4.6"
  statementType: threshold
  rung: threshold
  force: threshold
  level: fheq:6
  appliesTo: "single honours graduates at the threshold level"
  addressee: learner
  verbs: []
  about: "some leading current issues"
  themes: [none]
  domain: knowledge
  award: ["bachelor's with honours"]
  gradeOf: none
  paraphrase: "At threshold, graduates will know some of the leading open questions in present-day philosophical debate and research."
  quote: full   # the issuer's statement is in `source` (D-std-0014)
  audience: both
  subjects: inherited
- id: qaa/philosophy-2025/4.6.b5.excellent
  locator: { number: "4.6.b5.excellent", headingPath: ["Benchmark standards", "Subject-specific knowledge and understanding"] }
  span: { start: 54706, end: 54936 }
  source: "Many of the major issues currently at the frontiers of philosophical debate and research and their critical assessment based on a close reading of the primary text, demonstrating knowledge that may\n\nbe beyond what has been taught."
  stem: "4.6"
  statementType: excellent
  rung: excellent
  force: will
  level: fheq:6
  appliesTo: "single honours graduates at the excellent level"
  addressee: learner
  verbs: ["demonstrating"]
  about: "current issues assessed from close reading, beyond the taught"
  themes: [none]
  domain: knowledge
  award: ["bachelor's with honours"]
  gradeOf: { statement: qaa/philosophy-2025/4.6.b5.typical, basis: stated }
  paraphrase: "At the excellent level, graduates will know and critically assess many leading current questions, working from close reading of the primary literature and possibly beyond what was taught."
  quote: full   # the issuer's statement is in `source` (D-std-0014)
  audience: both
  subjects: inherited
- id: qaa/philosophy-2025/4.6.b5.typical
  locator: { number: "4.6.b5.typical", headingPath: ["Benchmark standards", "Subject-specific knowledge and understanding"] }
  span: { start: 54586, end: 54705 }
  source: "Many of the major issues currently at the frontiers of philosophical debate and research and their critical assessment."
  stem: "4.6"
  statementType: typical
  rung: typical
  force: will
  level: fheq:6
  appliesTo: "single honours graduates at the typical level"
  addressee: learner
  verbs: []
  about: "many current issues, critically assessed"
  themes: [none]
  domain: knowledge
  award: ["bachelor's with honours"]
  gradeOf: { statement: qaa/philosophy-2025/4.6.b5, basis: stated }
  paraphrase: "Typically, graduates will know many of the leading current questions in philosophy and will be able to assess them critically."
  quote: full   # the issuer's statement is in `source` (D-std-0014)
  audience: both
  subjects: inherited
- id: qaa/philosophy-2025/4.8.b1
  locator: { number: "4.8.b1", headingPath: ["Benchmark standards", "Subject-specific and intellectual skills"] }
  span: { start: 55397, end: 55448 }
  source: "Select and comment on readings and primary sources."
  stem: "4.8"
  statementType: threshold
  rung: threshold
  force: threshold
  level: fheq:6
  appliesTo: "single honours graduates at the threshold level"
  addressee: learner
  verbs: ["select", "comment"]
  about: "choosing and commenting on readings"
  themes: [none]
  domain: subject-skill
  award: ["bachelor's with honours"]
  gradeOf: none
  paraphrase: "At threshold, graduates will choose readings and primary sources and comment on them."
  quote: full   # the issuer's statement is in `source` (D-std-0014)
  audience: both
  subjects: inherited
- id: qaa/philosophy-2025/4.8.b1.excellent
  locator: { number: "4.8.b1.excellent", headingPath: ["Benchmark standards", "Subject-specific and intellectual skills"] }
  span: { start: 55540, end: 55765 }
  source: "Critically evaluate and synthesise a broad range of readings and primary sources, drawing on relevant material which may come from a range of different subdisciplines or traditions within Philosophy or from other disciplines."
  stem: "4.8"
  statementType: excellent
  rung: excellent
  force: will
  level: fheq:6
  appliesTo: "single honours graduates at the excellent level"
  addressee: learner
  verbs: ["evaluate", "synthesise", "drawing"]
  about: "synthesising wide reading across fields"
  themes: [none]
  domain: subject-skill
  award: ["bachelor's with honours"]
  gradeOf: { statement: qaa/philosophy-2025/4.8.b1.typical, basis: stated }
  paraphrase: "At the excellent level, graduates will critically evaluate and bring together a wide body of readings and primary sources, drawing in material from other branches or traditions of philosophy or from other subjects."
  quote: full   # the issuer's statement is in `source` (D-std-0014)
  audience: both
  subjects: inherited
- id: qaa/philosophy-2025/4.8.b1.typical
  locator: { number: "4.8.b1.typical", headingPath: ["Benchmark standards", "Subject-specific and intellectual skills"] }
  span: { start: 55449, end: 55539 }
  source: "Select, comment and evaluate readings and primary sources, sometimes beyond the set range."
  stem: "4.8"
  statementType: typical
  rung: typical
  force: will
  level: fheq:6
  appliesTo: "single honours graduates at the typical level"
  addressee: learner
  verbs: ["select", "comment", "evaluate"]
  about: "evaluating readings, sometimes beyond the list"
  themes: [none]
  domain: subject-skill
  award: ["bachelor's with honours"]
  gradeOf: { statement: qaa/philosophy-2025/4.8.b1, basis: stated }
  paraphrase: "Typically, graduates will choose, comment on and evaluate readings and primary sources, at times going past the set list."
  quote: full   # the issuer's statement is in `source` (D-std-0014)
  audience: both
  subjects: inherited
- id: qaa/philosophy-2025/4.8.b2
  locator: { number: "4.8.b2", headingPath: ["Benchmark standards", "Subject-specific and intellectual skills"] }
  span: { start: 55787, end: 55840 }
  source: "Understand the importance of interpretation of texts."
  stem: "4.8"
  statementType: threshold
  rung: threshold
  force: threshold
  level: fheq:6
  appliesTo: "single honours graduates at the threshold level"
  addressee: learner
  verbs: ["understand"]
  about: "why interpretation matters"
  themes: [none]
  domain: subject-skill
  award: ["bachelor's with honours"]
  gradeOf: none
  paraphrase: "At threshold, graduates will understand why interpreting texts matters."
  quote: full   # the issuer's statement is in `source` (D-std-0014)
  audience: both
  subjects: inherited
- id: qaa/philosophy-2025/4.8.b2.excellent
  locator: { number: "4.8.b2.excellent", headingPath: ["Benchmark standards", "Subject-specific and intellectual skills"] }
  span: { start: 56063, end: 56253 }
  source: "Draw sophisticated interpretations across various eras and traditions, and critically examine their underpinnings and broader philosophical implications with exceptional clarity and insight."
  stem: "4.8"
  statementType: excellent
  rung: excellent
  force: will
  level: fheq:6
  appliesTo: "single honours graduates at the excellent level"
  addressee: learner
  verbs: ["draw", "examine"]
  about: "sophisticated interpretation across eras and traditions"
  themes: [none]
  domain: subject-skill
  award: ["bachelor's with honours"]
  gradeOf: { statement: qaa/philosophy-2025/4.8.b2.typical, basis: stated }
  paraphrase: "At the excellent level, graduates will draw sophisticated readings across periods and traditions and critically examine their foundations and wider philosophical consequences with great clarity and insight."
  quote: full   # the issuer's statement is in `source` (D-std-0014)
  audience: both
  subjects: inherited
- id: qaa/philosophy-2025/4.8.b2.typical
  locator: { number: "4.8.b2.typical", headingPath: ["Benchmark standards", "Subject-specific and intellectual skills"] }
  span: { start: 55841, end: 56062 }
  source: "Read carefully and interpret texts drawn from a variety of ages and/or traditions with a sensitivity to context, plus identify textually based arguments and subject their structure and implications to rigorous assessment."
  stem: "4.8"
  statementType: typical
  rung: typical
  force: will
  level: fheq:6
  appliesTo: "single honours graduates at the typical level"
  addressee: learner
  verbs: ["read", "interpret", "identify"]
  about: "contextual reading and rigorous assessment of textual arguments"
  themes: [none]
  domain: subject-skill
  award: ["bachelor's with honours"]
  gradeOf: { statement: qaa/philosophy-2025/4.8.b2, basis: stated }
  paraphrase: "Typically, graduates will read and interpret texts from different periods or traditions with attention to context, pick out the arguments in them and test their structure and consequences rigorously."
  quote: full   # the issuer's statement is in `source` (D-std-0014)
  audience: both
  subjects: inherited
- id: qaa/philosophy-2025/4.8.b3
  locator: { number: "4.8.b3", headingPath: ["Benchmark standards", "Subject-specific and intellectual skills"] }
  span: { start: 56267, end: 56308 }
  source: "Use philosophical terminology accurately."
  stem: "4.8"
  statementType: threshold
  rung: threshold
  force: threshold
  level: fheq:6
  appliesTo: "single honours graduates at the threshold level"
  addressee: learner
  verbs: ["use"]
  about: "accurate use of terms"
  themes: [none]
  domain: subject-skill
  award: ["bachelor's with honours"]
  gradeOf: none
  paraphrase: "At threshold, graduates will use the technical vocabulary of philosophy correctly."
  quote: full   # the issuer's statement is in `source` (D-std-0014)
  audience: both
  subjects: inherited
- id: qaa/philosophy-2025/4.8.b3.excellent
  locator: { number: "4.8.b3.excellent", headingPath: ["Benchmark standards", "Subject-specific and intellectual skills"] }
  span: { start: 56390, end: 56519 }
  source: "Use generic and specialised philosophical terminology precisely and, where appropriate,\n\nintroduce new philosophical terminology."
  stem: "4.8"
  statementType: excellent
  rung: excellent
  force: will
  level: fheq:6
  appliesTo: "single honours graduates at the excellent level"
  addressee: learner
  verbs: ["use", "introduce"]
  about: "precise use and new terms where apt"
  themes: [none]
  domain: subject-skill
  award: ["bachelor's with honours"]
  gradeOf: { statement: qaa/philosophy-2025/4.8.b3.typical, basis: stated }
  paraphrase: "At the excellent level, graduates will use general and specialist philosophical vocabulary precisely and, where it helps, coin new terms."
  quote: full   # the issuer's statement is in `source` (D-std-0014)
  audience: both
  subjects: inherited
- id: qaa/philosophy-2025/4.8.b3.typical
  locator: { number: "4.8.b3.typical", headingPath: ["Benchmark standards", "Subject-specific and intellectual skills"] }
  span: { start: 56309, end: 56389 }
  source: "Use philosophical terminology precisely, including some specialised terminology."
  stem: "4.8"
  statementType: typical
  rung: typical
  force: will
  level: fheq:6
  appliesTo: "single honours graduates at the typical level"
  addressee: learner
  verbs: ["use"]
  about: "precise use, some specialist terms"
  themes: [none]
  domain: subject-skill
  award: ["bachelor's with honours"]
  gradeOf: { statement: qaa/philosophy-2025/4.8.b3, basis: stated }
  paraphrase: "Typically, graduates will use philosophical vocabulary with precision, some specialist terms included."
  quote: full   # the issuer's statement is in `source` (D-std-0014)
  audience: both
  subjects: inherited
- id: qaa/philosophy-2025/4.8.b4
  locator: { number: "4.8.b4", headingPath: ["Benchmark standards", "Subject-specific and intellectual skills"] }
  span: { start: 56543, end: 56618 }
  source: "Present an argument, showing an awareness of the nature of sound arguments."
  stem: "4.8"
  statementType: threshold
  rung: threshold
  force: threshold
  level: fheq:6
  appliesTo: "single honours graduates at the threshold level"
  addressee: learner
  verbs: ["present", "showing"]
  about: "presenting an argument, aware of soundness"
  themes: [none]
  domain: subject-skill
  award: ["bachelor's with honours"]
  gradeOf: none
  paraphrase: "At threshold, graduates will put forward an argument and show they know what makes an argument sound."
  quote: full   # the issuer's statement is in `source` (D-std-0014)
  audience: both
  subjects: inherited
- id: qaa/philosophy-2025/4.8.b4.excellent
  locator: { number: "4.8.b4.excellent", headingPath: ["Benchmark standards", "Subject-specific and intellectual skills"] }
  span: { start: 56774, end: 57070 }
  source: "Formulate sophisticated, nuanced arguments with precision and rigour, drawing well-justified conclusions based on sound reasoning and a comprehensive understanding of relevant concepts and theories that exhibit depth, clarity and an acute awareness of the\n\ncomplexities and implications involved."
  stem: "4.8"
  statementType: excellent
  rung: excellent
  force: will
  level: fheq:6
  appliesTo: "single honours graduates at the excellent level"
  addressee: learner
  verbs: ["formulate", "drawing", "exhibit"]
  about: "sophisticated, rigorous and nuanced argument"
  themes: [none]
  domain: subject-skill
  award: ["bachelor's with honours"]
  gradeOf: { statement: qaa/philosophy-2025/4.8.b4.typical, basis: stated }
  paraphrase: "At the excellent level, graduates will construct subtle arguments precisely and rigorously, reaching well-supported conclusions from sound reasoning and a full grasp of the relevant concepts and theories, with depth, clarity and keen awareness of complexity and consequence."
  quote: full   # the issuer's statement is in `source` (D-std-0014)
  audience: both
  subjects: inherited
- id: qaa/philosophy-2025/4.8.b4.typical
  locator: { number: "4.8.b4.typical", headingPath: ["Benchmark standards", "Subject-specific and intellectual skills"] }
  span: { start: 56619, end: 56773 }
  source: "Formulate arguments carefully and scrupulously, drawing only warranted conclusions and predict\n\npossible objections and defend the arguments against them."
  stem: "4.8"
  statementType: typical
  rung: typical
  force: will
  level: fheq:6
  appliesTo: "single honours graduates at the typical level"
  addressee: learner
  verbs: ["formulate", "drawing", "predict", "defend"]
  about: "careful arguments that anticipate objections"
  themes: [none]
  domain: subject-skill
  award: ["bachelor's with honours"]
  gradeOf: { statement: qaa/philosophy-2025/4.8.b4, basis: stated }
  paraphrase: "Typically, graduates will build arguments with care, draw only conclusions the premises support, anticipate objections and defend against them."
  quote: full   # the issuer's statement is in `source` (D-std-0014)
  audience: both
  subjects: inherited
- id: qaa/philosophy-2025/4.8.b5
  locator: { number: "4.8.b5", headingPath: ["Benchmark standards", "Subject-specific and intellectual skills"] }
  span: { start: 57140, end: 57174 }
  source: "Explain complex matters and ideas."
  stem: "4.8"
  statementType: threshold
  rung: threshold
  force: threshold
  level: fheq:6
  appliesTo: "single honours graduates at the threshold level"
  addressee: learner
  verbs: ["explain"]
  about: "explaining complex matters"
  themes: [none]
  domain: subject-skill
  award: ["bachelor's with honours"]
  gradeOf: none
  paraphrase: "At threshold, graduates will explain complicated matters and ideas."
  quote: full   # the issuer's statement is in `source` (D-std-0014)
  audience: both
  subjects: inherited
- id: qaa/philosophy-2025/4.8.b5.excellent
  locator: { number: "4.8.b5.excellent", headingPath: ["Benchmark standards", "Subject-specific and intellectual skills"] }
  span: { start: 57315, end: 57383 }
  source: "Tailor explanations to diverse audiences without oversimplification."
  stem: "4.8"
  statementType: excellent
  rung: excellent
  force: will
  level: fheq:6
  appliesTo: "single honours graduates at the excellent level"
  addressee: learner
  verbs: ["tailor"]
  about: "explanations fitted to varied audiences"
  themes: [none]
  domain: subject-skill
  award: ["bachelor's with honours"]
  gradeOf: { statement: qaa/philosophy-2025/4.8.b5.typical, basis: stated }
  paraphrase: "At the excellent level, graduates will adapt their explanations to different audiences without oversimplifying."
  quote: full   # the issuer's statement is in `source` (D-std-0014)
  audience: both
  subjects: inherited
- id: qaa/philosophy-2025/4.8.b5.typical
  locator: { number: "4.8.b5.typical", headingPath: ["Benchmark standards", "Subject-specific and intellectual skills"] }
  span: { start: 57175, end: 57313 }
  source: "Clearly explain complex matters and ideas, and appropriately simplify complex matters and ideas and illustrate them with helpful examples."
  stem: "4.8"
  statementType: typical
  rung: typical
  force: will
  level: fheq:6
  appliesTo: "single honours graduates at the typical level"
  addressee: learner
  verbs: ["explain", "simplify", "illustrate"]
  about: "clear explanation, apt simplification and examples"
  themes: [none]
  domain: subject-skill
  award: ["bachelor's with honours"]
  gradeOf: { statement: qaa/philosophy-2025/4.8.b5, basis: stated }
  paraphrase: "Typically, graduates will explain complex matters and ideas clearly, simplify them where fitting and illustrate them with useful examples."
  quote: full   # the issuer's statement is in `source` (D-std-0014)
  audience: both
  subjects: inherited
- id: qaa/philosophy-2025/4.8.b6
  locator: { number: "4.8.b6", headingPath: ["Benchmark standards", "Subject-specific and intellectual skills"] }
  span: { start: 57397, end: 57430 }
  source: "Display some limited originality."
  stem: "4.8"
  statementType: threshold
  rung: threshold
  force: threshold
  level: fheq:6
  appliesTo: "single honours graduates at the threshold level"
  addressee: learner
  verbs: ["display"]
  about: "a little originality"
  themes: [none]
  domain: subject-skill
  award: ["bachelor's with honours"]
  gradeOf: none
  paraphrase: "At threshold, graduates will show a little originality."
  quote: full   # the issuer's statement is in `source` (D-std-0014)
  audience: both
  subjects: inherited
- id: qaa/philosophy-2025/4.8.b6.excellent
  locator: { number: "4.8.b6.excellent", headingPath: ["Benchmark standards", "Subject-specific and intellectual skills"] }
  span: { start: 57474, end: 57532 }
  source: "Develop in depth original and plausible lines of argument."
  stem: "4.8"
  statementType: excellent
  rung: excellent
  force: will
  level: fheq:6
  appliesTo: "single honours graduates at the excellent level"
  addressee: learner
  verbs: ["develop"]
  about: "original, plausible lines of argument in depth"
  themes: [none]
  domain: subject-skill
  award: ["bachelor's with honours"]
  gradeOf: { statement: qaa/philosophy-2025/4.8.b6.typical, basis: stated }
  paraphrase: "At the excellent level, graduates will work out original and plausible lines of argument in depth."
  quote: full   # the issuer's statement is in `source` (D-std-0014)
  audience: both
  subjects: inherited
- id: qaa/philosophy-2025/4.8.b6.typical
  locator: { number: "4.8.b6.typical", headingPath: ["Benchmark standards", "Subject-specific and intellectual skills"] }
  span: { start: 57431, end: 57473 }
  source: "Develop some original ideas and arguments."
  stem: "4.8"
  statementType: typical
  rung: typical
  force: will
  level: fheq:6
  appliesTo: "single honours graduates at the typical level"
  addressee: learner
  verbs: ["develop"]
  about: "some original ideas and arguments"
  themes: [none]
  domain: subject-skill
  award: ["bachelor's with honours"]
  gradeOf: { statement: qaa/philosophy-2025/4.8.b6, basis: stated }
  paraphrase: "Typically, graduates will work out some ideas and arguments of their own."
  quote: full   # the issuer's statement is in `source` (D-std-0014)
  audience: both
  subjects: inherited
- id: qaa/philosophy-2025/4.8.b7
  locator: { number: "4.8.b7", headingPath: ["Benchmark standards", "Subject-specific and intellectual skills"] }
  span: { start: 57551, end: 57645 }
  source: "Identify the strengths and weaknesses of arguments on both sides of a philosophical\n\nquestion."
  stem: "4.8"
  statementType: threshold
  rung: threshold
  force: threshold
  level: fheq:6
  appliesTo: "single honours graduates at the threshold level"
  addressee: learner
  verbs: ["identify"]
  about: "strengths and weaknesses on both sides"
  themes: [none]
  domain: subject-skill
  award: ["bachelor's with honours"]
  gradeOf: none
  paraphrase: "At threshold, graduates will pick out what is strong and weak in the arguments on each side of a philosophical question."
  quote: full   # the issuer's statement is in `source` (D-std-0014)
  audience: both
  subjects: inherited
- id: qaa/philosophy-2025/4.8.b7.excellent
  locator: { number: "4.8.b7.excellent", headingPath: ["Benchmark standards", "Subject-specific and intellectual skills"] }
  span: { start: 57740, end: 57915 }
  source: "Suspend judgement and approach novel perspectives with an open and inquisitive mindset, coupled with the intellectual honesty to revise firmly held convictions when warranted."
  stem: "4.8"
  statementType: excellent
  rung: excellent
  force: will
  level: fheq:6
  appliesTo: "single honours graduates at the excellent level"
  addressee: learner
  verbs: ["suspend", "approach", "revise"]
  about: "suspending judgement and revising firm views"
  themes: [none]
  domain: subject-skill
  award: ["bachelor's with honours"]
  gradeOf: { statement: qaa/philosophy-2025/4.8.b7.typical, basis: stated }
  paraphrase: "At the excellent level, graduates will hold back judgement, meet new perspectives with open curiosity and have the honesty to revise even firm convictions when the case requires it."
  quote: full   # the issuer's statement is in `source` (D-std-0014)
  audience: both
  subjects: inherited
- id: qaa/philosophy-2025/4.8.b7.typical
  locator: { number: "4.8.b7.typical", headingPath: ["Benchmark standards", "Subject-specific and intellectual skills"] }
  span: { start: 57646, end: 57739 }
  source: "Review unfamiliar ideas with an open mind and a willingness to change\n\nmind when appropriate."
  stem: "4.8"
  statementType: typical
  rung: typical
  force: will
  level: fheq:6
  appliesTo: "single honours graduates at the typical level"
  addressee: learner
  verbs: ["review"]
  about: "open review of unfamiliar ideas"
  themes: [none]
  domain: subject-skill
  award: ["bachelor's with honours"]
  gradeOf: { statement: qaa/philosophy-2025/4.8.b7, basis: stated }
  paraphrase: "Typically, graduates will consider unfamiliar ideas openly and be ready to change their minds when that is warranted."
  quote: full   # the issuer's statement is in `source` (D-std-0014)
  audience: both
  subjects: inherited
- id: qaa/philosophy-2025/4.8.b8
  locator: { number: "4.8.b8", headingPath: ["Benchmark standards", "Subject-specific and intellectual skills"] }
  span: { start: 57937, end: 58050 }
  source: "Identify some of the ways in which philosophical work can inform, and be informed\n\nby, work in other disciplines."
  stem: "4.8"
  statementType: threshold
  rung: threshold
  force: threshold
  level: fheq:6
  appliesTo: "single honours graduates at the threshold level"
  addressee: learner
  verbs: ["identify", "inform"]
  about: "two-way links with other disciplines"
  themes: [none]
  domain: subject-skill
  award: ["bachelor's with honours"]
  gradeOf: none
  paraphrase: "At threshold, graduates will name some ways philosophy and other disciplines can shape each other."
  quote: full   # the issuer's statement is in `source` (D-std-0014)
  audience: both
  subjects: inherited
- id: qaa/philosophy-2025/4.8.b8.excellent
  locator: { number: "4.8.b8.excellent", headingPath: ["Benchmark standards", "Subject-specific and intellectual skills"] }
  span: { start: 58177, end: 58353 }
  source: "Describe, explain and critique philosophical doctrines in non- philosophical work, and\n\nto see the relevance of non-philosophical ideas\n\nand research for philosophical debates."
  stem: "4.8"
  statementType: excellent
  rung: excellent
  force: will
  level: fheq:6
  appliesTo: "single honours graduates at the excellent level"
  addressee: learner
  verbs: ["describe", "explain", "critique", "see"]
  about: "critiquing philosophy in other fields and the reverse"
  themes: [none]
  domain: subject-skill
  award: ["bachelor's with honours"]
  gradeOf: { statement: qaa/philosophy-2025/4.8.b8.typical, basis: stated }
  paraphrase: "At the excellent level, graduates will describe, explain and critique the philosophical assumptions at work in other fields and see how ideas and research from outside philosophy bear on its debates."
  quote: full   # the issuer's statement is in `source` (D-std-0014)
  audience: both
  subjects: inherited
- id: qaa/philosophy-2025/4.8.b8.typical
  locator: { number: "4.8.b8.typical", headingPath: ["Benchmark standards", "Subject-specific and intellectual skills"] }
  span: { start: 58051, end: 58176 }
  source: "Describe and explain some of the ways in which philosophical work can inform, and be informed by, work in\n\nother disciplines."
  stem: "4.8"
  statementType: typical
  rung: typical
  force: will
  level: fheq:6
  appliesTo: "single honours graduates at the typical level"
  addressee: learner
  verbs: ["describe", "explain", "inform"]
  about: "describing and explaining those links"
  themes: [none]
  domain: subject-skill
  award: ["bachelor's with honours"]
  gradeOf: { statement: qaa/philosophy-2025/4.8.b8, basis: stated }
  paraphrase: "Typically, graduates will describe and explain some ways philosophy and other disciplines shape each other."
  quote: full   # the issuer's statement is in `source` (D-std-0014)
  audience: both
  subjects: inherited
- id: qaa/philosophy-2025/4.8.b9
  locator: { number: "4.8.b9", headingPath: ["Benchmark standards", "Subject-specific and intellectual skills"] }
  span: { start: 58368, end: 58465 }
  source: "State some of the ways in which philosophical work can engage with the concerns of ordinary life."
  stem: "4.8"
  statementType: threshold
  rung: threshold
  force: threshold
  level: fheq:6
  appliesTo: "single honours graduates at the threshold level"
  addressee: learner
  verbs: ["state", "engage"]
  about: "naming links to ordinary life"
  themes: [none]
  domain: subject-skill
  award: ["bachelor's with honours"]
  gradeOf: none
  paraphrase: "At threshold, graduates will say how philosophy can bear on some everyday concerns."
  quote: full   # the issuer's statement is in `source` (D-std-0014)
  audience: both
  subjects: inherited
- id: qaa/philosophy-2025/4.8.b9.excellent
  locator: { number: "4.8.b9.excellent", headingPath: ["Benchmark standards", "Subject-specific and intellectual skills"] }
  span: { start: 58579, end: 58763 }
  source: "Exhibit a nuanced grasp of philosophy's relevance to everyday lived experiences, applying philosophical insights to illuminate and address real-world complexities and ethical dilemmas."
  stem: "4.8"
  statementType: excellent
  rung: excellent
  force: will
  level: fheq:6
  appliesTo: "single honours graduates at the excellent level"
  addressee: learner
  verbs: ["exhibit", "applying", "illuminate", "address"]
  about: "applying philosophy to real problems and dilemmas"
  themes: [none]
  domain: subject-skill
  award: ["bachelor's with honours"]
  gradeOf: { statement: qaa/philosophy-2025/4.8.b9.typical, basis: stated }
  paraphrase: "At the excellent level, graduates will show a subtle understanding of how philosophy matters to lived experience, using its insights to clarify and tackle real-world complexity and ethical dilemmas."
  quote: full   # the issuer's statement is in `source` (D-std-0014)
  audience: both
  subjects: inherited
- id: qaa/philosophy-2025/4.8.b9.typical
  locator: { number: "4.8.b9.typical", headingPath: ["Benchmark standards", "Subject-specific and intellectual skills"] }
  span: { start: 58466, end: 58578 }
  source: "Describe and explain some of the ways in which philosophical work can engage with the concerns of ordinary life."
  stem: "4.8"
  statementType: typical
  rung: typical
  force: will
  level: fheq:6
  appliesTo: "single honours graduates at the typical level"
  addressee: learner
  verbs: ["describe", "explain", "engage"]
  about: "explaining links to ordinary life"
  themes: [none]
  domain: subject-skill
  award: ["bachelor's with honours"]
  gradeOf: { statement: qaa/philosophy-2025/4.8.b9, basis: stated }
  paraphrase: "Typically, graduates will describe and explain some ways philosophy bears on everyday concerns."
  quote: full   # the issuer's statement is in `source` (D-std-0014)
  audience: both
  subjects: inherited
- id: qaa/philosophy-2025/4.10.b1
  locator: { number: "4.10.b1", headingPath: ["Benchmark standards", "Generic skills"] }
  span: { start: 59203, end: 59242 }
  source: "identify issues, questions and problems"
  stem: "4.10"
  statementType: outcome
  rung: none
  force: will
  level: fheq:6
  appliesTo: "undergraduate graduates of the subject"
  addressee: learner
  verbs: ["identify"]
  about: "spotting issues and problems"
  themes: [none]
  domain: generic-skill
  award: ["bachelor's with honours"]
  gradeOf: none
  paraphrase: "Will be able to recognise the issues, questions and problems a topic raises."
  quote: full   # the issuer's statement is in `source` (D-std-0014)
  audience: both
  subjects: inherited
- id: qaa/philosophy-2025/4.10.b2
  locator: { number: "4.10.b2", headingPath: ["Benchmark standards", "Generic skills"] }
  span: { start: 59245, end: 59307 }
  source: "identify gaps in their own knowledge and acquire new knowledge"
  stem: "4.10"
  statementType: outcome
  rung: none
  force: will
  level: fheq:6
  appliesTo: "undergraduate graduates of the subject"
  addressee: learner
  verbs: ["identify", "acquire"]
  about: "finding and filling gaps in knowledge"
  themes: [none]
  domain: generic-skill
  award: ["bachelor's with honours"]
  gradeOf: none
  paraphrase: "Will be able to see where their own knowledge falls short and learn what is missing."
  quote: full   # the issuer's statement is in `source` (D-std-0014)
  audience: both
  subjects: inherited
- id: qaa/philosophy-2025/4.10.b3
  locator: { number: "4.10.b3", headingPath: ["Benchmark standards", "Generic skills"] }
  span: { start: 59310, end: 59358 }
  source: "understand and analyse knowledge and information"
  stem: "4.10"
  statementType: outcome
  rung: none
  force: will
  level: fheq:6
  appliesTo: "undergraduate graduates of the subject"
  addressee: learner
  verbs: ["understand", "analyse"]
  about: "analysing knowledge and information"
  themes: [none]
  domain: generic-skill
  award: ["bachelor's with honours"]
  gradeOf: none
  paraphrase: "Will be able to grasp and break down knowledge and information."
  quote: full   # the issuer's statement is in `source` (D-std-0014)
  audience: both
  subjects: inherited
- id: qaa/philosophy-2025/4.10.b4
  locator: { number: "4.10.b4", headingPath: ["Benchmark standards", "Generic skills"] }
  span: { start: 59361, end: 59416 }
  source: "synthesise the state of knowledge on a particular topic"
  stem: "4.10"
  statementType: outcome
  rung: none
  force: will
  level: fheq:6
  appliesTo: "undergraduate graduates of the subject"
  addressee: learner
  verbs: ["synthesise"]
  about: "synthesising the state of knowledge"
  themes: [none]
  domain: generic-skill
  award: ["bachelor's with honours"]
  gradeOf: none
  paraphrase: "Will be able to draw together what is known on a given topic."
  quote: full   # the issuer's statement is in `source` (D-std-0014)
  audience: both
  subjects: inherited
- id: qaa/philosophy-2025/4.10.b5
  locator: { number: "4.10.b5", headingPath: ["Benchmark standards", "Generic skills"] }
  span: { start: 59423, end: 59489 }
  source: "apply knowledge and understanding to provide evidenced conclusions"
  stem: "4.10"
  statementType: outcome
  rung: none
  force: will
  level: fheq:6
  appliesTo: "undergraduate graduates of the subject"
  addressee: learner
  verbs: ["apply", "provide"]
  about: "reaching evidenced conclusions"
  themes: [none]
  domain: generic-skill
  award: ["bachelor's with honours"]
  gradeOf: none
  paraphrase: "Will be able to use knowledge and understanding to reach conclusions backed by evidence."
  quote: full   # the issuer's statement is in `source` (D-std-0014)
  audience: both
  subjects: inherited
- id: qaa/philosophy-2025/4.10.b6
  locator: { number: "4.10.b6", headingPath: ["Benchmark standards", "Generic skills"] }
  span: { start: 59492, end: 59562 }
  source: "communicate effectively and appropriately verbally and/or non-verbally"
  stem: "4.10"
  statementType: outcome
  rung: none
  force: will
  level: fheq:6
  appliesTo: "undergraduate graduates of the subject"
  addressee: learner
  verbs: ["communicate"]
  about: "communicating in speech or other forms"
  themes: [none]
  domain: generic-skill
  award: ["bachelor's with honours"]
  gradeOf: none
  paraphrase: "Will be able to communicate well and fittingly, in speech or by other means."
  quote: full   # the issuer's statement is in `source` (D-std-0014)
  audience: both
  subjects: inherited
- id: qaa/philosophy-2025/4.10.b7
  locator: { number: "4.10.b7", headingPath: ["Benchmark standards", "Generic skills"] }
  span: { start: 59565, end: 59639 }
  source: "present knowledge or an argument in a way that is comprehensible to others"
  stem: "4.10"
  statementType: outcome
  rung: none
  force: will
  level: fheq:6
  appliesTo: "undergraduate graduates of the subject"
  addressee: learner
  verbs: ["present"]
  about: "presenting knowledge or arguments to others"
  themes: [none]
  domain: generic-skill
  award: ["bachelor's with honours"]
  gradeOf: none
  paraphrase: "Will be able to set out knowledge or an argument so that others can follow it."
  quote: full   # the issuer's statement is in `source` (D-std-0014)
  audience: both
  subjects: inherited
- id: qaa/philosophy-2025/4.10.b8
  locator: { number: "4.10.b8", headingPath: ["Benchmark standards", "Generic skills"] }
  span: { start: 59642, end: 59755 }
  source: "critically engage with a range of forms of digital technology to collate, analyse, select and present information"
  stem: "4.10"
  statementType: outcome
  rung: none
  force: will
  level: fheq:6
  appliesTo: "undergraduate graduates of the subject"
  addressee: learner
  verbs: ["engage", "collate", "analyse", "select", "present"]
  about: "critical use of digital technology"
  themes: [none]
  domain: generic-skill
  award: ["bachelor's with honours"]
  gradeOf: none
  paraphrase: "Will be able to use a range of digital technologies critically to gather, analyse, choose and present information."
  quote: full   # the issuer's statement is in `source` (D-std-0014)
  audience: both
  subjects: inherited
- id: qaa/philosophy-2025/4.10.b9
  locator: { number: "4.10.b9", headingPath: ["Benchmark standards", "Generic skills"] }
  span: { start: 59758, end: 59945 }
  source: "assert intellectual independence, including undertaking tasks independently (with appropriate guidance and support), conducting self-directed research and demonstrating critical judgement"
  stem: "4.10"
  statementType: outcome
  rung: none
  force: will
  level: fheq:6
  appliesTo: "undergraduate graduates of the subject"
  addressee: learner
  verbs: ["assert", "undertaking", "conducting", "demonstrating"]
  about: "intellectual independence"
  themes: [none]
  domain: generic-skill
  award: ["bachelor's with honours"]
  gradeOf: none
  paraphrase: "Will be able to show intellectual independence: working alone with suitable guidance and support, researching on their own initiative and judging critically."
  quote: full   # the issuer's statement is in `source` (D-std-0014)
  audience: both
  subjects: inherited
- id: qaa/philosophy-2025/4.10.b10
  locator: { number: "4.10.b10", headingPath: ["Benchmark standards", "Generic skills"] }
  span: { start: 59948, end: 60051 }
  source: "work collaboratively, including undertaking work in a group or team and/or participating in discussions"
  stem: "4.10"
  statementType: outcome
  rung: none
  force: will
  level: fheq:6
  appliesTo: "undergraduate graduates of the subject"
  addressee: learner
  verbs: ["work", "undertaking", "participating"]
  about: "collaboration in groups and discussion"
  themes: [none]
  domain: generic-skill
  award: ["bachelor's with honours"]
  gradeOf: none
  paraphrase: "Will be able to work with others, in a group or team or by taking part in discussion."
  quote: full   # the issuer's statement is in `source` (D-std-0014)
  audience: both
  subjects: inherited
- id: qaa/philosophy-2025/4.10.b11
  locator: { number: "4.10.b11", headingPath: ["Benchmark standards", "Generic skills"] }
  span: { start: 60054, end: 60126 }
  source: "reflect on their own progress, including questions of academic integrity"
  stem: "4.10"
  statementType: outcome
  rung: none
  force: will
  level: fheq:6
  appliesTo: "undergraduate graduates of the subject"
  addressee: learner
  verbs: ["reflect"]
  about: "reflecting on progress and academic integrity"
  themes: [none]
  domain: generic-skill
  award: ["bachelor's with honours"]
  gradeOf: none
  paraphrase: "Will be able to reflect on how they are progressing, academic integrity included."
  quote: full   # the issuer's statement is in `source` (D-std-0014)
  audience: both
  subjects: inherited
- id: qaa/philosophy-2025/4.10.b12
  locator: { number: "4.10.b12", headingPath: ["Benchmark standards", "Generic skills"] }
  span: { start: 60129, end: 60245 }
  source: "identify and examine underlying values and ethics within culture and society and on a personal level. Master's level"
  stem: "4.10"
  statementType: outcome
  rung: none
  force: will
  level: fheq:6
  appliesTo: "undergraduate graduates of the subject"
  addressee: learner
  verbs: ["identify", "examine"]
  about: "examining underlying values and ethics"
  themes: [none]
  domain: generic-skill
  award: ["bachelor's with honours"]
  gradeOf: none
  paraphrase: "Will be able to recognise and examine the values and ethics beneath culture and society and in their own lives."
  quote: full   # the issuer's statement is in `source` (D-std-0014)
  audience: both
  subjects: inherited
- id: qaa/philosophy-2025/4.11.b1.masters
  locator: { number: "4.11.b1.masters", headingPath: ["Benchmark standards", "Master's level"] }
  span: { start: 60314, end: 60515 }
  source: "a sophisticated and comprehensive understanding of key concepts, theories, issues and debates within the discipline of Philosophy, informed by familiarity with current research and advanced scholarship"
  stem: "4.11"
  statementType: threshold
  rung: threshold
  force: will
  level: fheq:7
  appliesTo: "holders of a master's degree in the subject"
  addressee: learner
  verbs: ["informed"]
  about: "comprehensive understanding informed by current research"
  themes: [none]
  domain: understanding
  award: ["master's"]
  gradeOf: none
  paraphrase: "Will show a sophisticated, thorough understanding of the discipline's key concepts, theories, issues and debates, shaped by current research and advanced scholarship."
  quote: full   # the issuer's statement is in `source` (D-std-0014)
  audience: both
  subjects: inherited
- id: qaa/philosophy-2025/4.11.b2.masters
  locator: { number: "4.11.b2.masters", headingPath: ["Benchmark standards", "Master's level"] }
  span: { start: 60518, end: 60605 }
  source: "knowledge of appropriate research methods and employment of appropriate research skills"
  stem: "4.11"
  statementType: threshold
  rung: threshold
  force: will
  level: fheq:7
  appliesTo: "holders of a master's degree in the subject"
  addressee: learner
  verbs: []
  about: "research methods and skills"
  themes: [none]
  domain: subject-skill
  award: ["master's"]
  gradeOf: none
  paraphrase: "Will show knowledge of suitable research methods and use fitting research skills."
  quote: full   # the issuer's statement is in `source` (D-std-0014)
  audience: both
  subjects: inherited
- id: qaa/philosophy-2025/4.11.b3.masters
  locator: { number: "4.11.b3.masters", headingPath: ["Benchmark standards", "Master's level"] }
  span: { start: 60608, end: 60786 }
  source: "the ability to formulate, evaluate and critically analyse complex philosophical arguments, texts, positions and problems at an advanced level using rigorous philosophical methods"
  stem: "4.11"
  statementType: threshold
  rung: threshold
  force: will
  level: fheq:7
  appliesTo: "holders of a master's degree in the subject"
  addressee: learner
  verbs: ["formulate", "evaluate", "analyse", "using"]
  about: "advanced analysis of arguments and texts"
  themes: [none]
  domain: subject-skill
  award: ["master's"]
  gradeOf: none
  paraphrase: "Will be able to construct, assess and critically analyse demanding arguments, texts, positions and problems in philosophy at an advanced standard, with rigorous method."
  quote: full   # the issuer's statement is in `source` (D-std-0014)
  audience: both
  subjects: inherited
- id: qaa/philosophy-2025/4.11.b4.masters
  locator: { number: "4.11.b4.masters", headingPath: ["Benchmark standards", "Master's level"] }
  span: { start: 60789, end: 60895 }
  source: "expertise in one or more specialised areas or philosophical traditions through in-depth study and research"
  stem: "4.11"
  statementType: threshold
  rung: threshold
  force: will
  level: fheq:7
  appliesTo: "holders of a master's degree in the subject"
  addressee: learner
  verbs: []
  about: "specialist expertise"
  themes: [none]
  domain: knowledge
  award: ["master's"]
  gradeOf: none
  paraphrase: "Will show expertise in at least one specialist area or tradition, gained through deep study and research."
  quote: full   # the issuer's statement is in `source` (D-std-0014)
  audience: both
  subjects: inherited
- id: qaa/philosophy-2025/4.11.b5.masters
  locator: { number: "4.11.b5.masters", headingPath: ["Benchmark standards", "Master's level"] }
  span: { start: 60898, end: 61020 }
  source: "the capacity to conceptualise, design and execute a sustained philosophical research project that contributes to the field"
  stem: "4.11"
  statementType: threshold
  rung: threshold
  force: will
  level: fheq:7
  appliesTo: "holders of a master's degree in the subject"
  addressee: learner
  verbs: ["conceptualise", "design", "execute", "contributes"]
  about: "a sustained research project"
  themes: [none]
  domain: subject-skill
  award: ["master's"]
  gradeOf: none
  paraphrase: "Will show the capacity to conceive, plan and carry out a sustained piece of philosophical research that adds to the field."
  quote: full   # the issuer's statement is in `source` (D-std-0014)
  audience: both
  subjects: inherited
- id: qaa/philosophy-2025/4.11.b6.masters
  locator: { number: "4.11.b6.masters", headingPath: ["Benchmark standards", "Master's level"] }
  span: { start: 61023, end: 61180 }
  source: "highly developed skills in rational and logical analysis, interpretation of complex ideas, and construction of sophisticated arguments and lines of reasoning"
  stem: "4.11"
  statementType: threshold
  rung: threshold
  force: will
  level: fheq:7
  appliesTo: "holders of a master's degree in the subject"
  addressee: learner
  verbs: []
  about: "advanced analysis, interpretation and argument"
  themes: [none]
  domain: subject-skill
  award: ["master's"]
  gradeOf: none
  paraphrase: "Will show well-developed skill in rational and logical analysis, in interpreting complex ideas and in building sophisticated arguments and chains of reasoning."
  quote: full   # the issuer's statement is in `source` (D-std-0014)
  audience: both
  subjects: inherited
- id: qaa/philosophy-2025/4.11.b7.masters
  locator: { number: "4.11.b7.masters", headingPath: ["Benchmark standards", "Master's level"] }
  span: { start: 61183, end: 61337 }
  source: "an appreciation of the broader significance and implications of philosophical ideas in relation to other disciplinary perspectives and real-world contexts"
  stem: "4.11"
  statementType: threshold
  rung: threshold
  force: will
  level: fheq:7
  appliesTo: "holders of a master's degree in the subject"
  addressee: learner
  verbs: []
  about: "wider significance of philosophical ideas"
  themes: [none]
  domain: understanding
  award: ["master's"]
  gradeOf: none
  paraphrase: "Will show an appreciation of what philosophical ideas mean beyond philosophy, for other disciplines and for real situations."
  quote: full   # the issuer's statement is in `source` (D-std-0014)
  audience: both
  subjects: inherited
- id: qaa/philosophy-2025/4.11.b8.masters
  locator: { number: "4.11.b8.masters", headingPath: ["Benchmark standards", "Master's level"] }
  span: { start: 61340, end: 61506 }
  source: "advanced skills in philosophical writing and verbal and/or non-verbal presentation to effectively communicate complex ideas to specialist and non-specialist audiences"
  stem: "4.11"
  statementType: threshold
  rung: threshold
  force: will
  level: fheq:7
  appliesTo: "holders of a master's degree in the subject"
  addressee: learner
  verbs: ["communicate"]
  about: "communicating complex ideas to all audiences"
  themes: [none]
  domain: generic-skill
  award: ["master's"]
  gradeOf: none
  paraphrase: "Will show advanced writing and presentation skills, spoken or otherwise, that convey complex ideas well to specialists and non-specialists."
  quote: full   # the issuer's statement is in `source` (D-std-0014)
  audience: both
  subjects: inherited
- id: qaa/philosophy-2025/4.11.b9.masters
  locator: { number: "4.11.b9.masters", headingPath: ["Benchmark standards", "Master's level"] }
  span: { start: 61509, end: 61600 }
  source: "the ability to engage in sustained philosophical dialogue, debate and collaborative inquiry"
  stem: "4.11"
  statementType: threshold
  rung: threshold
  force: will
  level: fheq:7
  appliesTo: "holders of a master's degree in the subject"
  addressee: learner
  verbs: ["engage"]
  about: "sustained dialogue and collaborative inquiry"
  themes: [none]
  domain: subject-skill
  award: ["master's"]
  gradeOf: none
  paraphrase: "Will show the ability to take part in long philosophical dialogue, debate and shared inquiry."
  quote: full   # the issuer's statement is in `source` (D-std-0014)
  audience: both
  subjects: inherited
- id: qaa/philosophy-2025/4.11.b10.masters
  locator: { number: "4.11.b10.masters", headingPath: ["Benchmark standards", "Master's level"] }
  span: { start: 61603, end: 61751 }
  source: "a reflective understanding of the nature of Philosophy as a discipline, its methods, presuppositions, and its relationship to other forms of inquiry"
  stem: "4.11"
  statementType: threshold
  rung: threshold
  force: will
  level: fheq:7
  appliesTo: "holders of a master's degree in the subject"
  addressee: learner
  verbs: []
  about: "philosophy's nature, methods and presuppositions"
  themes: [none]
  domain: understanding
  award: ["master's"]
  gradeOf: none
  paraphrase: "Will show a reflective grasp of what philosophy is as a discipline, its methods and assumptions, and how it relates to other kinds of inquiry."
  quote: full   # the issuer's statement is in `source` (D-std-0014)
  audience: both
  subjects: inherited
- id: qaa/philosophy-2025/4.11.b11.masters
  locator: { number: "4.11.b11.masters", headingPath: ["Benchmark standards", "Master's level"] }
  span: { start: 61754, end: 61926 }
  source: "ethical reasoning skills and an appreciation of the moral dimensions of philosophical problems and the role of Philosophy in addressing ethical, social and political issues"
  stem: "4.11"
  statementType: threshold
  rung: threshold
  force: will
  level: fheq:7
  appliesTo: "holders of a master's degree in the subject"
  addressee: learner
  verbs: ["addressing"]
  about: "ethical reasoning and philosophy's social role"
  themes: [none]
  domain: subject-skill
  award: ["master's"]
  gradeOf: none
  paraphrase: "Will show skill in ethical reasoning and an appreciation of the moral side of philosophical problems and of philosophy's part in tackling ethical, social and political issues."
  quote: full   # the issuer's statement is in `source` (D-std-0014)
  audience: both
  subjects: inherited
- id: qaa/philosophy-2025/4.11.b12.masters
  locator: { number: "4.11.b12.masters", headingPath: ["Benchmark standards", "Master's level"] }
  span: { start: 61929, end: 62069 }
  source: "independent learning and research skills to identify, evaluate and synthesise relevant sources and continue their philosophical development."
  stem: "4.11"
  statementType: threshold
  rung: threshold
  force: will
  level: fheq:7
  appliesTo: "holders of a master's degree in the subject"
  addressee: learner
  verbs: ["identify", "evaluate", "synthesise", "continue"]
  about: "independent learning and continuing development"
  themes: [none]
  domain: generic-skill
  award: ["master's"]
  gradeOf: none
  paraphrase: "Will show the independent learning and research skills to find, assess and combine relevant sources and to keep developing as a philosopher."
  quote: full   # the issuer's statement is in `source` (D-std-0014)
  audience: both
  subjects: inherited
```

### S4a Audience versions
<!-- label: both; status: drafted; basis: primary. forPractitioner: for the programme designer or teacher. forBeneficiary: for the student, second person, naming no issuer. author-agent-written: instructions to an AI agent writing about the statement (a course document, a handbook, an outcome, a report). author-agent-dialogue: instructions to an AI agent using the statement in conversation (with a student, a teacher or a programme team). Written fresh from the held text alone (benchmark rule 6; Abbott, 15:42). -->
```yaml
- statement: qaa/philosophy-2025/1.11
  forPractitioner: { text: "Bring views from other cultures and traditions into materials and discussion, since graduates should be skilled at comparing and judging them; use varied tools and strategies so that every student can speak and contribute.", rewrite: light, force: should, status: drafted }
  forBeneficiary: { text: "You should become skilled at comparing and weighing up philosophical views from different cultures and traditions.", rewrite: full, force: should, status: drafted }
  author-agent-written: "Present this as an expectation (should) in the statement's equity, diversity and inclusion section: honours graduates ought to be skilled at weighing views from other cultures and traditions, at FHEQ level 6 (FQHEIS level 10). Cite it as QAA (2025), Philosophy Subject Benchmark Statement, para 1.11. Do not present it as a rung of the benchmark standards or as a regulatory duty. Set it beside 4.8.b7, 4.8.b1.excellent, theme:edi and the FHEQ descriptor qaa/fheq-2024/4.15.b7."
  author-agent-dialogue: "Raise it when a student's reading or essay draws on one tradition only, or when a team reviews how diverse its curriculum is. To a student, say plainly that you should be able to compare and weigh views from different cultures; to staff, frame it as a curriculum and teaching expectation. Ask: Which tradition outside the one you mostly study have you read, and how would it answer your question? Avoid reading the paragraph aloud or treating it as a box to tick."
- statement: qaa/philosophy-2025/1.18
  forPractitioner: { text: "Use the Advance HE and QAA guidance on education for sustainable development (March 2021) as a core resource when you design the course; the subject aligns with its skills and outcomes, read against the UN Sustainable Development Goals.", rewrite: light, force: should, status: drafted }
  forBeneficiary: { text: "not-applicable: a duty on the course team to consult a guidance document; the student meets its effect", rewrite: full, force: should, status: drafted }
  author-agent-written: "Present this as a should addressed to course teams: consult the 2021 Advance HE and QAA guidance on education for sustainable development as a core resource; it holds for course design at every level and is not a student outcome. Cite it as QAA (2025), Philosophy Subject Benchmark Statement, para 1.18, and the guidance as std:doc:qaa-advancehe-esd-2021-guidance. Do not claim it makes the guidance mandatory or sets sustainability outcomes of its own. Set it beside theme:esd and beside 1.17 and 1.19 on how the subject treats sustainability."
  author-agent-dialogue: "Raise it with a programme team planning or reviewing where sustainability appears in the curriculum, not with a student as a requirement. Frame it for staff as the guidance the statement expects them to work from. Ask: Where in your modules do students analyse the idea of sustainability or test claims made in its name? Avoid reading the list of goals aloud and avoid presenting the guidance as binding."
- statement: qaa/philosophy-2025/2.9
  forPractitioner: { text: "Joint and combined honours students will achieve the core subject-specific and generic skills of the statement and add skills from their other subject; plan chances for them to work across the overlap.", rewrite: light, force: will, status: drafted }
  forBeneficiary: { text: "If you study philosophy alongside another subject, you will gain the core philosophical and general skills described here, add skills from your other subject and may explore where the two meet.", rewrite: full, force: will, status: drafted }
  author-agent-written: "Present this as an expected outcome (will) for joint and combined honours students: they reach the core of the specific and generic skills, not the whole single honours set, at FHEQ level 6 (FQHEIS level 10). Cite it as QAA (2025), Philosophy Subject Benchmark Statement, para 2.9. Do not claim the rung tables in 4.6 and 4.8 apply in full to joint honours, since 4.5 says they are written for single honours. Set it beside 4.5, the generic skills 4.10.b1 to 4.10.b12 and spine:6."
  author-agent-dialogue: "Raise it when a joint honours student asks whether they are held to the same standard as single honours students, or when a joint programme team plans its outcomes. Tell a student plainly that you will be expected to reach the core skills, with breadth added from the other subject; frame it for staff as a question of scope. Ask: Which philosophical skills does your other subject strengthen, and which need more practice? Avoid implying a joint student must cover everything a single honours student does."
- statement: qaa/philosophy-2025/2.17
  forPractitioner: { text: "In periodic review, providers will involve external reviewers, who give an independent view on proposed changes and check that threshold standards are reached and the content suits philosophy.", rewrite: light, force: will, status: drafted }
  forBeneficiary: { text: "not-applicable: a duty on the provider in course review", rewrite: full, force: will, status: drafted }
  author-agent-written: "Present this as a provider expectation (will) about periodic course review, not a student outcome and not tied to a level. Cite it as QAA (2025), Philosophy Subject Benchmark Statement, para 2.17. Do not claim it sets the review cycle or the form of external review, which each degree-awarding body decides. Set it beside 2.16 and 2.18 on monitoring and external examining; set it also beside the threshold cells of 4.6 and 4.8, which reviewers check."
  author-agent-dialogue: "Raise it with a programme team or quality officer preparing a periodic review, never with a student as something they must do. Frame it as the independent check on threshold standards and on fit to the subject. Ask: Who will act as your external reviewer, and which threshold cells will you ask them to look at? Avoid reading the paragraph aloud or treating it as a regulatory rule."
- statement: qaa/philosophy-2025/3.4
  forPractitioner: { text: "Teach the traditions as distinct but compatible: share their common stress on precision, clarity and self-reflection, and do not assume they are at odds or cannot engage productively.", rewrite: light, force: should, status: drafted }
  forBeneficiary: { text: "You should not assume that different philosophical traditions are opposed or cannot learn from each other; they share a concern with precision, clarity and self-reflection.", rewrite: full, force: should, status: drafted }
  author-agent-written: "Present this as a should addressed to students and staff alike: do not treat philosophy's traditions as opposed or unable to engage; it is a principle for the degree at any level, not a rung. Cite it as QAA (2025), Philosophy Subject Benchmark Statement, para 3.4. Do not claim it requires every course to teach several traditions; 3.6 only values some acquaintance with another. Set it beside 3.2, 3.6 and the open-mindedness row 4.8.b7."
  author-agent-dialogue: "Raise it when a student dismisses a whole tradition, analytic, continental or comparative, or when a team debates which traditions to teach. Say plainly to a student that you should not assume the traditions cannot talk to each other; to staff, put it as a design principle. Ask: What does the other tradition do well that yours does not? Avoid taking sides between traditions."
- statement: qaa/philosophy-2025/3.8
  forPractitioner: { text: "Model the practice of philosophy in teaching: time spent acquiring knowledge of topics and thinkers must be balanced with time in which students discuss, analyse and work out their own responses.", rewrite: light, force: must, status: drafted }
  forBeneficiary: { text: "not-applicable: a duty on the course in how teaching is balanced; the student meets its effect", rewrite: full, force: must, status: drafted }
  author-agent-written: "Present this as a must on the provider: teaching has to balance acquiring knowledge of topics and thinkers with students discussing, analysing and responding for themselves; it holds for teaching at every level of the degree. Cite it as QAA (2025), Philosophy Subject Benchmark Statement, para 3.8. Do not turn it into a student outcome or a fixed ratio of contact types. Set it beside 3.9, 3.10 and 3.14 on teaching methods and the reference framework's strand:thinking."
  author-agent-dialogue: "Raise it with a programme or module team reviewing a teaching plan, for example one built mostly on lectures. Frame it for staff as the one teaching must in this section. Ask: Where in each week do students argue and respond, not only listen? Avoid giving it to a student as their duty."
- statement: qaa/philosophy-2025/3.9
  forPractitioner: { text: "Whatever its size, every programme will include student-led research, peer exchange of ideas and room for students to direct the questions they pursue.", rewrite: light, force: will, status: drafted }
  forBeneficiary: { text: "not-applicable: a duty on the programme; the student meets its effect as research, discussion and choice", rewrite: full, force: will, status: drafted }
  author-agent-written: "Present this as a provider expectation (will) that holds for every philosophy programme whatever its size or mode: some student-led research, peer exchange and self-chosen questions. Cite it as QAA (2025), Philosophy Subject Benchmark Statement, para 3.9. Do not claim it fixes how much research there is or which delivery mode is used. Set it beside 3.8, 3.17 on co-created assessment and the generic skill 4.10.b9."
  author-agent-dialogue: "Raise it with a team designing a small or largely online programme, where peer exchange and student-led research are easiest to lose. Frame it for staff as a floor every programme keeps. Ask: Where can students choose their own question, and where do they exchange ideas with peers? Avoid presenting it to students as a task they owe."
- statement: qaa/philosophy-2025/3.13
  forPractitioner: { text: "Teaching strategies will bring students from different backgrounds together to work on shared problems; offer several modes and occasions for discussion, online and in person, so everyone can take part.", rewrite: light, force: will, status: drafted }
  forBeneficiary: { text: "not-applicable: a duty on the provider in teaching strategy", rewrite: full, force: will, status: drafted }
  author-agent-written: "Present this as a provider expectation (will) about teaching strategy: students of different backgrounds work together on shared problems, with varied modes of discussion; it holds across the degree, not at one level. Cite it as QAA (2025), Philosophy Subject Benchmark Statement, para 3.13. Do not read its 'it is important that' as a must; record it as the issuer's emphasis. Set it beside 1.7, 1.8 and 1.11 on inclusive enquiry and the generic skill 4.10.b10."
  author-agent-dialogue: "Raise it with a team planning seminars or group work, especially where some students struggle to take part. Frame it for staff as how teaching is expected to use the range of students' backgrounds. Ask: Which discussion formats do you offer besides live seminars, and who uses them? Avoid presenting it to a student as an obligation."
- statement: qaa/philosophy-2025/3.15.b1
  forPractitioner: { text: "Make sure the suite of assessments will test knowledge and understanding, alongside philosophical skills and methods.", rewrite: light, force: will, status: drafted }
  forBeneficiary: { text: "not-applicable: a duty on the programme in designing assessment", rewrite: full, force: will, status: drafted }
  author-agent-written: "Present this as a provider expectation (will): every programme's assessments test knowledge and understanding; it holds for assessment across the degree. Cite it as QAA (2025), Philosophy Subject Benchmark Statement, para 3.15, item 1. Do not claim it names particular assessment methods; 3.17 lists methods as examples only. Set it beside the knowledge rows 4.6.b1 to 4.6.b5 and qaa/fheq-2024/annex-d/knowledge/r1/3rd."
  author-agent-dialogue: "Raise it when a team maps its assessments, to check that knowledge and understanding is tested somewhere in each year. Frame it for staff as coverage, not as a list of methods. Ask: Which assessment in your programme tests knowledge and understanding, and how would a marker see it? Avoid putting it to a student as their duty."
- statement: qaa/philosophy-2025/3.15.b2
  forPractitioner: { text: "Make sure the suite of assessments will test argument and analysis, showing rigorous, critical, creative and independent reasoning.", rewrite: light, force: will, status: drafted }
  forBeneficiary: { text: "not-applicable: a duty on the programme in designing assessment", rewrite: full, force: will, status: drafted }
  author-agent-written: "Present this as a provider expectation (will): every programme's assessments test argument and analysis; it holds for assessment across the degree. Cite it as QAA (2025), Philosophy Subject Benchmark Statement, para 3.15, item 2. Do not claim it names particular assessment methods; 3.17 lists methods as examples only. Set it beside the argument row 4.8.b4, the generic skill 4.10.b9 and qaa/fheq-2024/annex-d/cognitive/r2/3rd."
  author-agent-dialogue: "Raise it when a team maps its assessments, to check that argument and analysis is tested somewhere in each year. Frame it for staff as coverage, not as a list of methods. Ask: Which assessment in your programme tests argument and analysis, and how would a marker see it? Avoid putting it to a student as their duty."
- statement: qaa/philosophy-2025/3.15.b3
  forPractitioner: { text: "Make sure the suite of assessments will test presentation: clear, reliable and effective communication.", rewrite: light, force: will, status: drafted }
  forBeneficiary: { text: "not-applicable: a duty on the programme in designing assessment", rewrite: full, force: will, status: drafted }
  author-agent-written: "Present this as a provider expectation (will): every programme's assessments test presentation; it holds for assessment across the degree. Cite it as QAA (2025), Philosophy Subject Benchmark Statement, para 3.15, item 3. Do not claim it names particular assessment methods; 3.17 lists methods as examples only. Set it beside the explaining row 4.8.b5, the generic skills 4.10.b6 and 4.10.b7 and qaa/fheq-2024/annex-d/transferable/r1/3rd."
  author-agent-dialogue: "Raise it when a team maps its assessments, to check that presentation is tested somewhere in each year. Frame it for staff as coverage, not as a list of methods. Ask: Which assessment in your programme tests presentation, and how would a marker see it? Avoid putting it to a student as their duty."
- statement: qaa/philosophy-2025/3.19
  forPractitioner: { text: "Make any use of technology in assessment transparent, which the paragraph makes a must; promote integrity through authentic tasks and personal examples, and give students self and peer assessment against clear criteria.", rewrite: light, force: must, status: drafted }
  forBeneficiary: { text: "not-applicable: a duty on the provider in how assessment uses technology", rewrite: full, force: must, status: drafted }
  author-agent-written: "Present this as a must on the provider: where technologies, which may include generative AI, are used in assessment, their use has to be transparent; it holds for assessment at every level. Cite it as QAA (2025), Philosophy Subject Benchmark Statement, para 3.19. Do not claim the paragraph bans any technology or says who must disclose what; it states only that transparency is required. Set it beside 1.31 and 1.32 on generative AI in assessment, theme:generative-ai and the generic skill 4.10.b11."
  author-agent-dialogue: "Raise it when a team writes assessment briefs or a policy on technology, or when a student asks whether they may use a tool in an assignment. To staff, frame it as the one must on technology in assessment; to a student, explain plainly how the course says tools may be used and declared, without making the duty theirs. Ask: Does each assessment brief say which tools are allowed and how their use is shown? Avoid reading the paragraph aloud or inventing rules it does not state."
- statement: qaa/philosophy-2025/4.2
  forPractitioner: { text: "Most students exceed the threshold; the provider decides what evidence shows this and should use Annex D of the 2024 UK degree frameworks, with its descriptions of the 1st, 2.1, 2.2 and 3rd classes.", rewrite: light, force: should, status: drafted }
  forBeneficiary: { text: "not-applicable: a duty on the provider in judging classifications", rewrite: full, force: should, status: drafted }
  author-agent-written: "Present this as a should on the provider: when judging achievement above the threshold, refer to Annex D's descriptions of the four honours classes, at FHEQ level 6 (FQHEIS level 10). Cite it as QAA (2025), Philosophy Subject Benchmark Statement, para 4.2, and Annex D as std:doc:qaa-fheq-2024-framework, Annex D. Do not claim the statement sets mark ranges; each provider sets its own method. Set it beside 4.4, which defines the rungs, and the Annex D summary cells qaa/fheq-2024/annex-d/summary/r1/3rd to qaa/fheq-2024/annex-d/summary/r1/1st."
  author-agent-dialogue: "Raise it with a team or exam board calibrating degree classifications against the rung tables. Frame it for staff as the cross-check between the subject's rungs and the national class descriptions. Ask: Where does your marking scheme draw on Annex D, and does it agree with the rung definitions in 4.4? Avoid giving this to a student as their responsibility."
- statement: qaa/philosophy-2025/4.3
  forPractitioner: { text: "Do not treat the rungs as competence standards; if you write competence standards into a programme specification under the Equality Act 2010, draw on this statement and any PSRB requirements and follow the latest EHRC guidance.", rewrite: light, force: should, status: drafted }
  forBeneficiary: { text: "not-applicable: a duty on the provider in writing competence standards", rewrite: full, force: should, status: drafted }
  author-agent-written: "Present this as a should on the provider: if it writes competence standards in the Equality Act sense, it follows the latest Equality and Human Rights Commission guidance; it holds for undergraduate and master's study. Cite it as QAA (2025), Philosophy Subject Benchmark Statement, para 4.3. Do not claim the rung tables are competence standards or that the statement requires any. Set it beside 4.4, theme:accessibility and 1.13 and 1.14 on anticipatory adjustments."
  author-agent-dialogue: "Raise it with a programme team drafting a programme specification or reviewing reasonable adjustments, when someone proposes treating a rung as a fixed competence. Frame it for staff as a caution and a pointer to EHRC guidance. Ask: Is this requirement a genuine competence standard, and have you checked it against the current EHRC guidance? Avoid putting it to a student, and avoid reading the paragraph aloud."
- statement: qaa/philosophy-2025/4.5
  forPractitioner: { text: "Write the rung descriptions into single honours outcomes; for joint, modular and elective students scale the expectations, but anyone finishing a philosophy module is expected to show some general philosophical skills and knowledge of the module's texts and topics.", rewrite: light, force: must, status: drafted }
  forBeneficiary: { text: "If you complete any philosophy module, you are expected to have some general philosophical skills and to know the texts and topics the module describes.", rewrite: full, force: must, status: drafted }
  author-agent-written: "Present this as an expectation phrased 'expected to', recorded with force describes: anyone who completes a philosophy module has some general philosophical skills and knows the module's listed texts and topics; it holds for any module, not a level. Cite it as QAA (2025), Philosophy Subject Benchmark Statement, para 4.5. Do not claim the rung tables apply in full to joint honours or single modules; the paragraph says they are written for single honours. Set it beside 2.9 and the threshold cells 4.6.b1 and 4.8.b1."
  author-agent-dialogue: "Raise it when a student from another subject takes a philosophy module and asks what is expected, or when a team writes outcomes for an elective. Tell a student plainly what you are expected to show at the end of the module; frame it for staff as the floor for any module. Ask: Which texts and topics does the module description name, and which general skill will you practise most? Avoid applying the single honours rungs to them."
- statement: qaa/philosophy-2025/4.6.b1
  forPractitioner: { text: "At threshold, graduates will show knowledge and understanding of the texts of several of the great philosophers.", rewrite: light, force: threshold, status: drafted }
  forBeneficiary: { text: "To reach the threshold standard, you will know and understand what several major philosophers wrote.", rewrite: full, force: threshold, status: drafted }
  author-agent-written: "Present this as the threshold cell of the 'major philosophers' row in the knowledge and understanding table: the floor every single honours graduate in philosophy reaches, which the issuer matches to a third-class degree, at FHEQ level 6 (FQHEIS level 10). Cite it as QAA (2025), Philosophy Subject Benchmark Statement, para 4.6, major philosophers row, threshold column. Do not call it a regulatory requirement, and do not apply it to a master's award or a joint honours course without noting that the issuer wrote the rungs for single honours (4.5). Set it beside the row's other cells (4.6.b1.typical and 4.6.b1.excellent), the descriptor qaa/fheq-2024/4.15.b1 and qaa/fqheis-2024/4.16.b1, Annex D's 3rd cell (qaa/fheq-2024/annex-d/knowledge/r1/3rd) and spine:6."
  author-agent-dialogue: "Raise it when a student asks what they must show at the least in reading the major philosophers to gain an honours degree, or when staff check that every student can reach it. Put it plainly and in the second person to a student, and to staff as the floor the course must make reachable. Ask: Which philosopher have you read in their own words, rather than through a summary? Where do readers disagree about that philosopher, and which reading do you find stronger? Avoid reading the table aloud; give this one cell and name the typical cell (4.6.b1.typical) only as the next step up."
- statement: qaa/philosophy-2025/4.6.b1.excellent
  forPractitioner: { text: "At the excellent level, graduates will add to knowledge of the theories and the interpretative debates an original interpretation of their own, built on close reading of the primary sources.", rewrite: light, force: will, status: drafted }
  forBeneficiary: { text: "To reach the excellent standard, you will also put forward your own original reading of the philosophers you study, based on close attention to what they actually wrote.", rewrite: full, force: will, status: drafted }
  author-agent-written: "Present this as the excellent cell of the 'major philosophers' row in the knowledge and understanding table: what the strongest single honours graduates in philosophy reach (will), which the issuer matches to a first-class degree, at FHEQ level 6 (FQHEIS level 10); it is an aspiration, not a requirement. Cite it as QAA (2025), Philosophy Subject Benchmark Statement, para 4.6, major philosophers row, excellent column. Do not call it a regulatory requirement, and do not apply it to a master's award or a joint honours course without noting that the issuer wrote the rungs for single honours (4.5). Set it beside the row's other cells (4.6.b1 and 4.6.b1.typical), the descriptor qaa/fheq-2024/4.15.b1 and qaa/fqheis-2024/4.16.b1, Annex D's 1st cell (qaa/fheq-2024/annex-d/knowledge/r1/1st) and spine:6."
  author-agent-dialogue: "Raise it with a student aiming for a first in reading the major philosophers, or with markers deciding what earns one. Put it plainly and in the second person to a student, and to staff as what marks out the strongest work. Ask: Which philosopher have you read in their own words, rather than through a summary? Where do readers disagree about that philosopher, and which reading do you find stronger? Avoid treating it as what everyone must reach, and do not read the issuer's wording aloud at length."
- statement: qaa/philosophy-2025/4.6.b1.typical
  forPractitioner: { text: "At the typical level, graduates will understand major philosophers' theories and arguments from their own texts and the key debates about how those texts are interpreted.", rewrite: light, force: will, status: drafted }
  forBeneficiary: { text: "To reach the typical standard, you will know the main theories and arguments of major philosophers from reading them directly, and where scholars disagree about how to read them.", rewrite: full, force: will, status: drafted }
  author-agent-written: "Present this as the typical cell of the 'major philosophers' row in the knowledge and understanding table: what most single honours graduates in philosophy reach (will), which the issuer matches to a second-class degree, at FHEQ level 6 (FQHEIS level 10); it is an expectation above the pass line. Cite it as QAA (2025), Philosophy Subject Benchmark Statement, para 4.6, major philosophers row, typical column. Do not call it a regulatory requirement, and do not apply it to a master's award or a joint honours course without noting that the issuer wrote the rungs for single honours (4.5). Set it beside the row's other cells (4.6.b1 and 4.6.b1.excellent), the descriptor qaa/fheq-2024/4.15.b1 and qaa/fqheis-2024/4.16.b1, Annex D's 2.2 and 2.1 cell (qaa/fheq-2024/annex-d/knowledge/r1/2.2 and qaa/fheq-2024/annex-d/knowledge/r1/2.1) and spine:6."
  author-agent-dialogue: "Raise it when a student wants to move from a pass towards a second-class result in reading the major philosophers, or when a team calibrates marking for the middle of the range. Put it plainly and in the second person to a student, and to staff as the standard most graduates reach. Ask: Which philosopher have you read in their own words, rather than through a summary? Where do readers disagree about that philosopher, and which reading do you find stronger? Avoid presenting it as the minimum: the threshold cell (4.6.b1) is the floor."
- statement: qaa/philosophy-2025/4.6.b2
  forPractitioner: { text: "At threshold, graduates will understand some of the principal theories and arguments in theoretical philosophy: logic, epistemology, metaphysics or the philosophy of mind.", rewrite: light, force: threshold, status: drafted }
  forBeneficiary: { text: "To reach the threshold standard, you will know some of the main theories and arguments about logic, knowledge, reality or the mind.", rewrite: full, force: threshold, status: drafted }
  author-agent-written: "Present this as the threshold cell of the 'theoretical philosophy' row in the knowledge and understanding table: the floor every single honours graduate in philosophy reaches, which the issuer matches to a third-class degree, at FHEQ level 6 (FQHEIS level 10). Cite it as QAA (2025), Philosophy Subject Benchmark Statement, para 4.6, theoretical philosophy row, threshold column. Do not call it a regulatory requirement, and do not apply it to a master's award or a joint honours course without noting that the issuer wrote the rungs for single honours (4.5). Set it beside the row's other cells (4.6.b2.typical and 4.6.b2.excellent), the descriptor qaa/fheq-2024/4.15.b1 and qaa/fqheis-2024/4.16.b1, Annex D's 3rd cell (qaa/fheq-2024/annex-d/knowledge/r1/3rd) and spine:6."
  author-agent-dialogue: "Raise it when a student asks what they must show at the least in logic, metaphysics, epistemology or philosophy of mind to gain an honours degree, or when staff check that every student can reach it. Put it plainly and in the second person to a student, and to staff as the floor the course must make reachable. Ask: Which theory in this area could you explain and defend now? How does it compare with a rival view you have studied? Avoid reading the table aloud; give this one cell and name the typical cell (4.6.b2.typical) only as the next step up."
- statement: qaa/philosophy-2025/4.6.b2.excellent
  forPractitioner: { text: "At the excellent level, graduates will command many theories and arguments in theoretical philosophy, compare them systematically and may show knowledge beyond the taught curriculum.", rewrite: light, force: will, status: drafted }
  forBeneficiary: { text: "To reach the excellent standard, you will know many theories and arguments about logic, knowledge, reality or the mind, compare them carefully and often go beyond what your course covered.", rewrite: full, force: will, status: drafted }
  author-agent-written: "Present this as the excellent cell of the 'theoretical philosophy' row in the knowledge and understanding table: what the strongest single honours graduates in philosophy reach (will), which the issuer matches to a first-class degree, at FHEQ level 6 (FQHEIS level 10); it is an aspiration, not a requirement. Cite it as QAA (2025), Philosophy Subject Benchmark Statement, para 4.6, theoretical philosophy row, excellent column. Do not call it a regulatory requirement, and do not apply it to a master's award or a joint honours course without noting that the issuer wrote the rungs for single honours (4.5). Set it beside the row's other cells (4.6.b2 and 4.6.b2.typical), the descriptor qaa/fheq-2024/4.15.b1 and qaa/fqheis-2024/4.16.b1, Annex D's 1st cell (qaa/fheq-2024/annex-d/knowledge/r1/1st) and spine:6."
  author-agent-dialogue: "Raise it with a student aiming for a first in logic, metaphysics, epistemology or philosophy of mind, or with markers deciding what earns one. Put it plainly and in the second person to a student, and to staff as what marks out the strongest work. Ask: Which theory in this area could you explain and defend now? How does it compare with a rival view you have studied? Avoid treating it as what everyone must reach, and do not read the issuer's wording aloud at length."
- statement: qaa/philosophy-2025/4.6.b2.typical
  forPractitioner: { text: "At the typical level, graduates will understand more of the principal theories and arguments in theoretical philosophy than the threshold asks.", rewrite: light, force: will, status: drafted }
  forBeneficiary: { text: "To reach the typical standard, you will know more of the main theories and arguments about logic, knowledge, reality or the mind.", rewrite: full, force: will, status: drafted }
  author-agent-written: "Present this as the typical cell of the 'theoretical philosophy' row in the knowledge and understanding table: what most single honours graduates in philosophy reach (will), which the issuer matches to a second-class degree, at FHEQ level 6 (FQHEIS level 10); it is an expectation above the pass line. Cite it as QAA (2025), Philosophy Subject Benchmark Statement, para 4.6, theoretical philosophy row, typical column. Do not call it a regulatory requirement, and do not apply it to a master's award or a joint honours course without noting that the issuer wrote the rungs for single honours (4.5). Set it beside the row's other cells (4.6.b2 and 4.6.b2.excellent), the descriptor qaa/fheq-2024/4.15.b1 and qaa/fqheis-2024/4.16.b1, Annex D's 2.2 and 2.1 cell (qaa/fheq-2024/annex-d/knowledge/r1/2.2 and qaa/fheq-2024/annex-d/knowledge/r1/2.1) and spine:6."
  author-agent-dialogue: "Raise it when a student wants to move from a pass towards a second-class result in logic, metaphysics, epistemology or philosophy of mind, or when a team calibrates marking for the middle of the range. Put it plainly and in the second person to a student, and to staff as the standard most graduates reach. Ask: Which theory in this area could you explain and defend now? How does it compare with a rival view you have studied? Avoid presenting it as the minimum: the threshold cell (4.6.b2) is the floor."
- statement: qaa/philosophy-2025/4.6.b3
  forPractitioner: { text: "At threshold, graduates will understand some principal theories and arguments in practical philosophy: moral, political or social.", rewrite: light, force: threshold, status: drafted }
  forBeneficiary: { text: "To reach the threshold standard, you will know some of the main theories and arguments about ethics, politics or society.", rewrite: full, force: threshold, status: drafted }
  author-agent-written: "Present this as the threshold cell of the 'practical philosophy' row in the knowledge and understanding table: the floor every single honours graduate in philosophy reaches, which the issuer matches to a third-class degree, at FHEQ level 6 (FQHEIS level 10). Cite it as QAA (2025), Philosophy Subject Benchmark Statement, para 4.6, practical philosophy row, threshold column. Do not call it a regulatory requirement, and do not apply it to a master's award or a joint honours course without noting that the issuer wrote the rungs for single honours (4.5). Set it beside the row's other cells (4.6.b3.typical and 4.6.b3.excellent), the descriptor qaa/fheq-2024/4.15.b1 and qaa/fqheis-2024/4.16.b1, Annex D's 3rd cell (qaa/fheq-2024/annex-d/knowledge/r1/3rd) and spine:6."
  author-agent-dialogue: "Raise it when a student asks what they must show at the least in moral, political or social philosophy to gain an honours degree, or when staff check that every student can reach it. Put it plainly and in the second person to a student, and to staff as the floor the course must make reachable. Ask: Which theory in ethics, politics or society could you set out and test against an objection? Where does it stand against the main alternative you have met? Avoid reading the table aloud; give this one cell and name the typical cell (4.6.b3.typical) only as the next step up."
- statement: qaa/philosophy-2025/4.6.b3.excellent
  forPractitioner: { text: "At the excellent level, graduates will command many theories and arguments in practical philosophy, compare them systematically and may show knowledge beyond the taught curriculum.", rewrite: light, force: will, status: drafted }
  forBeneficiary: { text: "To reach the excellent standard, you will know many theories and arguments about ethics, politics or society, compare them carefully and often go beyond what your course covered.", rewrite: full, force: will, status: drafted }
  author-agent-written: "Present this as the excellent cell of the 'practical philosophy' row in the knowledge and understanding table: what the strongest single honours graduates in philosophy reach (will), which the issuer matches to a first-class degree, at FHEQ level 6 (FQHEIS level 10); it is an aspiration, not a requirement. Cite it as QAA (2025), Philosophy Subject Benchmark Statement, para 4.6, practical philosophy row, excellent column. Do not call it a regulatory requirement, and do not apply it to a master's award or a joint honours course without noting that the issuer wrote the rungs for single honours (4.5). Set it beside the row's other cells (4.6.b3 and 4.6.b3.typical), the descriptor qaa/fheq-2024/4.15.b1 and qaa/fqheis-2024/4.16.b1, Annex D's 1st cell (qaa/fheq-2024/annex-d/knowledge/r1/1st) and spine:6."
  author-agent-dialogue: "Raise it with a student aiming for a first in moral, political or social philosophy, or with markers deciding what earns one. Put it plainly and in the second person to a student, and to staff as what marks out the strongest work. Ask: Which theory in ethics, politics or society could you set out and test against an objection? Where does it stand against the main alternative you have met? Avoid treating it as what everyone must reach, and do not read the issuer's wording aloud at length."
- statement: qaa/philosophy-2025/4.6.b3.typical
  forPractitioner: { text: "At the typical level, graduates will understand more of the principal theories and arguments in practical philosophy than the threshold asks.", rewrite: light, force: will, status: drafted }
  forBeneficiary: { text: "To reach the typical standard, you will know more of the main theories and arguments about ethics, politics or society.", rewrite: full, force: will, status: drafted }
  author-agent-written: "Present this as the typical cell of the 'practical philosophy' row in the knowledge and understanding table: what most single honours graduates in philosophy reach (will), which the issuer matches to a second-class degree, at FHEQ level 6 (FQHEIS level 10); it is an expectation above the pass line. Cite it as QAA (2025), Philosophy Subject Benchmark Statement, para 4.6, practical philosophy row, typical column. Do not call it a regulatory requirement, and do not apply it to a master's award or a joint honours course without noting that the issuer wrote the rungs for single honours (4.5). Set it beside the row's other cells (4.6.b3 and 4.6.b3.excellent), the descriptor qaa/fheq-2024/4.15.b1 and qaa/fqheis-2024/4.16.b1, Annex D's 2.2 and 2.1 cell (qaa/fheq-2024/annex-d/knowledge/r1/2.2 and qaa/fheq-2024/annex-d/knowledge/r1/2.1) and spine:6."
  author-agent-dialogue: "Raise it when a student wants to move from a pass towards a second-class result in moral, political or social philosophy, or when a team calibrates marking for the middle of the range. Put it plainly and in the second person to a student, and to staff as the standard most graduates reach. Ask: Which theory in ethics, politics or society could you set out and test against an objection? Where does it stand against the main alternative you have met? Avoid presenting it as the minimum: the threshold cell (4.6.b3) is the floor."
- statement: qaa/philosophy-2025/4.6.b4
  forPractitioner: { text: "At threshold, graduates will understand a small number of techniques of philosophical reasoning.", rewrite: light, force: threshold, status: drafted }
  forBeneficiary: { text: "To reach the threshold standard, you will know a few of the methods philosophers use to reason.", rewrite: full, force: threshold, status: drafted }
  author-agent-written: "Present this as the threshold cell of the 'techniques of reasoning' row in the knowledge and understanding table: the floor every single honours graduate in philosophy reaches, which the issuer matches to a third-class degree, at FHEQ level 6 (FQHEIS level 10). Cite it as QAA (2025), Philosophy Subject Benchmark Statement, para 4.6, techniques of reasoning row, threshold column. Do not call it a regulatory requirement, and do not apply it to a master's award or a joint honours course without noting that the issuer wrote the rungs for single honours (4.5). Set it beside the row's other cells (4.6.b4.typical and 4.6.b4.excellent), the descriptor qaa/fheq-2024/4.15.b2 and qaa/fqheis-2024/4.16.b4, Annex D's 3rd cell (qaa/fheq-2024/annex-d/knowledge/r2/3rd) and spine:6."
  author-agent-dialogue: "Raise it when a student asks what they must show at the least in the methods of philosophical reasoning to gain an honours degree, or when staff check that every student can reach it. Put it plainly and in the second person to a student, and to staff as the floor the course must make reachable. Ask: Which reasoning technique, such as a counterexample, a reductio or a thought experiment, do you use most confidently? What is one criticism of a philosophical method you rely on? Avoid reading the table aloud; give this one cell and name the typical cell (4.6.b4.typical) only as the next step up."
- statement: qaa/philosophy-2025/4.6.b4.excellent
  forPractitioner: { text: "At the excellent level, graduates will understand an extensive repertoire of reasoning techniques and the critiques and debates surrounding philosophical method.", rewrite: light, force: will, status: drafted }
  forBeneficiary: { text: "To reach the excellent standard, you will know a wide range of reasoning methods and the arguments about how philosophy should be done.", rewrite: full, force: will, status: drafted }
  author-agent-written: "Present this as the excellent cell of the 'techniques of reasoning' row in the knowledge and understanding table: what the strongest single honours graduates in philosophy reach (will), which the issuer matches to a first-class degree, at FHEQ level 6 (FQHEIS level 10); it is an aspiration, not a requirement. Cite it as QAA (2025), Philosophy Subject Benchmark Statement, para 4.6, techniques of reasoning row, excellent column. Do not call it a regulatory requirement, and do not apply it to a master's award or a joint honours course without noting that the issuer wrote the rungs for single honours (4.5). Set it beside the row's other cells (4.6.b4 and 4.6.b4.typical), the descriptor qaa/fheq-2024/4.15.b2 and qaa/fqheis-2024/4.16.b4, Annex D's 1st cell (qaa/fheq-2024/annex-d/knowledge/r2/1st) and spine:6."
  author-agent-dialogue: "Raise it with a student aiming for a first in the methods of philosophical reasoning, or with markers deciding what earns one. Put it plainly and in the second person to a student, and to staff as what marks out the strongest work. Ask: Which reasoning technique, such as a counterexample, a reductio or a thought experiment, do you use most confidently? What is one criticism of a philosophical method you rely on? Avoid treating it as what everyone must reach, and do not read the issuer's wording aloud at length."
- statement: qaa/philosophy-2025/4.6.b4.typical
  forPractitioner: { text: "At the typical level, graduates will understand a wider range of reasoning techniques and how philosophers have criticised the discipline's methods.", rewrite: light, force: will, status: drafted }
  forBeneficiary: { text: "To reach the typical standard, you will know more reasoning methods and how philosophers have questioned the methods of philosophy itself.", rewrite: full, force: will, status: drafted }
  author-agent-written: "Present this as the typical cell of the 'techniques of reasoning' row in the knowledge and understanding table: what most single honours graduates in philosophy reach (will), which the issuer matches to a second-class degree, at FHEQ level 6 (FQHEIS level 10); it is an expectation above the pass line. Cite it as QAA (2025), Philosophy Subject Benchmark Statement, para 4.6, techniques of reasoning row, typical column. Do not call it a regulatory requirement, and do not apply it to a master's award or a joint honours course without noting that the issuer wrote the rungs for single honours (4.5). Set it beside the row's other cells (4.6.b4 and 4.6.b4.excellent), the descriptor qaa/fheq-2024/4.15.b2 and qaa/fqheis-2024/4.16.b4, Annex D's 2.2 and 2.1 cell (qaa/fheq-2024/annex-d/knowledge/r2/2.2 and qaa/fheq-2024/annex-d/knowledge/r2/2.1) and spine:6."
  author-agent-dialogue: "Raise it when a student wants to move from a pass towards a second-class result in the methods of philosophical reasoning, or when a team calibrates marking for the middle of the range. Put it plainly and in the second person to a student, and to staff as the standard most graduates reach. Ask: Which reasoning technique, such as a counterexample, a reductio or a thought experiment, do you use most confidently? What is one criticism of a philosophical method you rely on? Avoid presenting it as the minimum: the threshold cell (4.6.b4) is the floor."
- statement: qaa/philosophy-2025/4.6.b5
  forPractitioner: { text: "At threshold, graduates will be aware of some major issues in current philosophical research.", rewrite: light, force: threshold, status: drafted }
  forBeneficiary: { text: "To reach the threshold standard, you will know some of the big questions philosophers are debating and researching now.", rewrite: full, force: threshold, status: drafted }
  author-agent-written: "Present this as the threshold cell of the 'current debates' row in the knowledge and understanding table: the floor every single honours graduate in philosophy reaches, which the issuer matches to a third-class degree, at FHEQ level 6 (FQHEIS level 10). Cite it as QAA (2025), Philosophy Subject Benchmark Statement, para 4.6, current debates row, threshold column. Do not call it a regulatory requirement, and do not apply it to a master's award or a joint honours course without noting that the issuer wrote the rungs for single honours (4.5). Set it beside the row's other cells (4.6.b5.typical and 4.6.b5.excellent), the descriptor qaa/fheq-2024/4.15.b1, qaa/fheq-2024/4.15.b3.2 and qaa/fqheis-2024/4.16.b2, Annex D's 3rd cell (qaa/fheq-2024/annex-d/knowledge/r1/3rd) and spine:6."
  author-agent-dialogue: "Raise it when a student asks what they must show at the least in today's philosophical debates to gain an honours degree, or when staff check that every student can reach it. Put it plainly and in the second person to a student, and to staff as the floor the course must make reachable. Ask: Which live debate in philosophy today could you summarise, with the positions taken? What do you think of it, and on what reading is that view based? Avoid reading the table aloud; give this one cell and name the typical cell (4.6.b5.typical) only as the next step up."
- statement: qaa/philosophy-2025/4.6.b5.excellent
  forPractitioner: { text: "At the excellent level, graduates will assess many current research issues critically from close reading of primary sources, often reaching past the taught material.", rewrite: light, force: will, status: drafted }
  forBeneficiary: { text: "To reach the excellent standard, you will judge many current debates critically from your own close reading of the original texts, often going beyond your course.", rewrite: full, force: will, status: drafted }
  author-agent-written: "Present this as the excellent cell of the 'current debates' row in the knowledge and understanding table: what the strongest single honours graduates in philosophy reach (will), which the issuer matches to a first-class degree, at FHEQ level 6 (FQHEIS level 10); it is an aspiration, not a requirement. Cite it as QAA (2025), Philosophy Subject Benchmark Statement, para 4.6, current debates row, excellent column. Do not call it a regulatory requirement, and do not apply it to a master's award or a joint honours course without noting that the issuer wrote the rungs for single honours (4.5). Set it beside the row's other cells (4.6.b5 and 4.6.b5.typical), the descriptor qaa/fheq-2024/4.15.b1, qaa/fheq-2024/4.15.b3.2 and qaa/fqheis-2024/4.16.b2, Annex D's 1st cell (qaa/fheq-2024/annex-d/knowledge/r1/1st) and spine:6."
  author-agent-dialogue: "Raise it with a student aiming for a first in today's philosophical debates, or with markers deciding what earns one. Put it plainly and in the second person to a student, and to staff as what marks out the strongest work. Ask: Which live debate in philosophy today could you summarise, with the positions taken? What do you think of it, and on what reading is that view based? Avoid treating it as what everyone must reach, and do not read the issuer's wording aloud at length."
- statement: qaa/philosophy-2025/4.6.b5.typical
  forPractitioner: { text: "At the typical level, graduates will know many major issues in current research and assess them critically.", rewrite: light, force: will, status: drafted }
  forBeneficiary: { text: "To reach the typical standard, you will know many of the big questions in current philosophy and be able to judge them critically.", rewrite: full, force: will, status: drafted }
  author-agent-written: "Present this as the typical cell of the 'current debates' row in the knowledge and understanding table: what most single honours graduates in philosophy reach (will), which the issuer matches to a second-class degree, at FHEQ level 6 (FQHEIS level 10); it is an expectation above the pass line. Cite it as QAA (2025), Philosophy Subject Benchmark Statement, para 4.6, current debates row, typical column. Do not call it a regulatory requirement, and do not apply it to a master's award or a joint honours course without noting that the issuer wrote the rungs for single honours (4.5). Set it beside the row's other cells (4.6.b5 and 4.6.b5.excellent), the descriptor qaa/fheq-2024/4.15.b1, qaa/fheq-2024/4.15.b3.2 and qaa/fqheis-2024/4.16.b2, Annex D's 2.2 and 2.1 cell (qaa/fheq-2024/annex-d/knowledge/r1/2.2 and qaa/fheq-2024/annex-d/knowledge/r1/2.1) and spine:6."
  author-agent-dialogue: "Raise it when a student wants to move from a pass towards a second-class result in today's philosophical debates, or when a team calibrates marking for the middle of the range. Put it plainly and in the second person to a student, and to staff as the standard most graduates reach. Ask: Which live debate in philosophy today could you summarise, with the positions taken? What do you think of it, and on what reading is that view based? Avoid presenting it as the minimum: the threshold cell (4.6.b5) is the floor."
- statement: qaa/philosophy-2025/4.8.b1
  forPractitioner: { text: "At threshold, graduates will select readings and primary texts and offer comment on them.", rewrite: light, force: threshold, status: drafted }
  forBeneficiary: { text: "To reach the threshold standard, you will pick suitable readings and original sources and say something useful about them.", rewrite: full, force: threshold, status: drafted }
  author-agent-written: "Present this as the threshold cell of the 'Selecting readings' row in the subject-specific and intellectual skills table: the floor every single honours graduate in philosophy reaches, which the issuer matches to a third-class degree, at FHEQ level 6 (FQHEIS level 10). Cite it as QAA (2025), Philosophy Subject Benchmark Statement, para 4.8, Selecting readings row, threshold column. Do not call it a regulatory requirement, and do not apply it to a master's award or a joint honours course without noting that the issuer wrote the rungs for single honours (4.5). Set it beside the row's other cells (4.8.b1.typical and 4.8.b1.excellent), the descriptor qaa/fheq-2024/4.15.b5, Annex D's 3rd cell (qaa/fheq-2024/annex-d/cognitive/r1/3rd) and spine:6."
  author-agent-dialogue: "Raise it when a student asks what they must show at the least in choosing and using sources to gain an honours degree, or when staff check that every student can reach it. Put it plainly and in the second person to a student, and to staff as the floor the course must make reachable. Ask: How did you choose the sources for your last essay, and which came from outside the reading list? What did you make of the strongest source, rather than only report it? Avoid reading the table aloud; give this one cell and name the typical cell (4.8.b1.typical) only as the next step up."
- statement: qaa/philosophy-2025/4.8.b1.excellent
  forPractitioner: { text: "At the excellent level, graduates will critically evaluate and synthesise wide reading, using relevant work from other subfields, other traditions or other disciplines.", rewrite: light, force: will, status: drafted }
  forBeneficiary: { text: "To reach the excellent standard, you will critically assess and pull together a wide range of reading, including relevant work from other parts of philosophy or other subjects.", rewrite: full, force: will, status: drafted }
  author-agent-written: "Present this as the excellent cell of the 'Selecting readings' row in the subject-specific and intellectual skills table: what the strongest single honours graduates in philosophy reach (will), which the issuer matches to a first-class degree, at FHEQ level 6 (FQHEIS level 10); it is an aspiration, not a requirement. Cite it as QAA (2025), Philosophy Subject Benchmark Statement, para 4.8, Selecting readings row, excellent column. Do not call it a regulatory requirement, and do not apply it to a master's award or a joint honours course without noting that the issuer wrote the rungs for single honours (4.5). Set it beside the row's other cells (4.8.b1 and 4.8.b1.typical), the descriptor qaa/fheq-2024/4.15.b5, Annex D's 1st cell (qaa/fheq-2024/annex-d/cognitive/r1/1st) and spine:6."
  author-agent-dialogue: "Raise it with a student aiming for a first in choosing and using sources, or with markers deciding what earns one. Put it plainly and in the second person to a student, and to staff as what marks out the strongest work. Ask: How did you choose the sources for your last essay, and which came from outside the reading list? What did you make of the strongest source, rather than only report it? Avoid treating it as what everyone must reach, and do not read the issuer's wording aloud at length."
- statement: qaa/philosophy-2025/4.8.b1.typical
  forPractitioner: { text: "At the typical level, graduates will select, comment on and evaluate readings and primary texts, sometimes from outside the reading list.", rewrite: light, force: will, status: drafted }
  forBeneficiary: { text: "To reach the typical standard, you will choose, comment on and assess readings and original sources, sometimes going beyond your reading list.", rewrite: full, force: will, status: drafted }
  author-agent-written: "Present this as the typical cell of the 'Selecting readings' row in the subject-specific and intellectual skills table: what most single honours graduates in philosophy reach (will), which the issuer matches to a second-class degree, at FHEQ level 6 (FQHEIS level 10); it is an expectation above the pass line. Cite it as QAA (2025), Philosophy Subject Benchmark Statement, para 4.8, Selecting readings row, typical column. Do not call it a regulatory requirement, and do not apply it to a master's award or a joint honours course without noting that the issuer wrote the rungs for single honours (4.5). Set it beside the row's other cells (4.8.b1 and 4.8.b1.excellent), the descriptor qaa/fheq-2024/4.15.b5, Annex D's 2.2 and 2.1 cell (qaa/fheq-2024/annex-d/cognitive/r1/2.2 and qaa/fheq-2024/annex-d/cognitive/r1/2.1) and spine:6."
  author-agent-dialogue: "Raise it when a student wants to move from a pass towards a second-class result in choosing and using sources, or when a team calibrates marking for the middle of the range. Put it plainly and in the second person to a student, and to staff as the standard most graduates reach. Ask: How did you choose the sources for your last essay, and which came from outside the reading list? What did you make of the strongest source, rather than only report it? Avoid presenting it as the minimum: the threshold cell (4.8.b1) is the floor."
- statement: qaa/philosophy-2025/4.8.b2
  forPractitioner: { text: "At threshold, graduates will grasp why textual interpretation matters in philosophy.", rewrite: light, force: threshold, status: drafted }
  forBeneficiary: { text: "To reach the threshold standard, you will understand why the way you interpret a text matters.", rewrite: full, force: threshold, status: drafted }
  author-agent-written: "Present this as the threshold cell of the 'Interpreting texts' row in the subject-specific and intellectual skills table: the floor every single honours graduate in philosophy reaches, which the issuer matches to a third-class degree, at FHEQ level 6 (FQHEIS level 10). Cite it as QAA (2025), Philosophy Subject Benchmark Statement, para 4.8, Interpreting texts row, threshold column. Do not call it a regulatory requirement, and do not apply it to a master's award or a joint honours course without noting that the issuer wrote the rungs for single honours (4.5). Set it beside the row's other cells (4.8.b2.typical and 4.8.b2.excellent), the descriptor qaa/fheq-2024/4.15.b7, Annex D's 3rd cell (qaa/fheq-2024/annex-d/cognitive/r2/3rd) and spine:6."
  author-agent-dialogue: "Raise it when a student asks what they must show at the least in reading and interpreting texts to gain an honours degree, or when staff check that every student can reach it. Put it plainly and in the second person to a student, and to staff as the floor the course must make reachable. Ask: How does the context in which a text was written change how you read it? Can you set out the argument of a passage step by step and say where it is weakest? Avoid reading the table aloud; give this one cell and name the typical cell (4.8.b2.typical) only as the next step up."
- statement: qaa/philosophy-2025/4.8.b2.excellent
  forPractitioner: { text: "At the excellent level, graduates will produce sophisticated interpretations spanning periods and traditions and examine critically what they rest on and imply, with exceptional clarity.", rewrite: light, force: will, status: drafted }
  forBeneficiary: { text: "To reach the excellent standard, you will offer sophisticated readings across periods and traditions and examine clearly and insightfully what they rest on and what they imply.", rewrite: full, force: will, status: drafted }
  author-agent-written: "Present this as the excellent cell of the 'Interpreting texts' row in the subject-specific and intellectual skills table: what the strongest single honours graduates in philosophy reach (will), which the issuer matches to a first-class degree, at FHEQ level 6 (FQHEIS level 10); it is an aspiration, not a requirement. Cite it as QAA (2025), Philosophy Subject Benchmark Statement, para 4.8, Interpreting texts row, excellent column. Do not call it a regulatory requirement, and do not apply it to a master's award or a joint honours course without noting that the issuer wrote the rungs for single honours (4.5). Set it beside the row's other cells (4.8.b2 and 4.8.b2.typical), the descriptor qaa/fheq-2024/4.15.b7, Annex D's 1st cell (qaa/fheq-2024/annex-d/cognitive/r2/1st) and spine:6."
  author-agent-dialogue: "Raise it with a student aiming for a first in reading and interpreting texts, or with markers deciding what earns one. Put it plainly and in the second person to a student, and to staff as what marks out the strongest work. Ask: How does the context in which a text was written change how you read it? Can you set out the argument of a passage step by step and say where it is weakest? Avoid treating it as what everyone must reach, and do not read the issuer's wording aloud at length."
- statement: qaa/philosophy-2025/4.8.b2.typical
  forPractitioner: { text: "At the typical level, graduates will interpret texts from various periods or traditions in context, identify their arguments and rigorously assess how those arguments are built and what follows from them.", rewrite: light, force: will, status: drafted }
  forBeneficiary: { text: "To reach the typical standard, you will read texts from different times and traditions carefully and in context, find the arguments in them and test how they work and what follows.", rewrite: full, force: will, status: drafted }
  author-agent-written: "Present this as the typical cell of the 'Interpreting texts' row in the subject-specific and intellectual skills table: what most single honours graduates in philosophy reach (will), which the issuer matches to a second-class degree, at FHEQ level 6 (FQHEIS level 10); it is an expectation above the pass line. Cite it as QAA (2025), Philosophy Subject Benchmark Statement, para 4.8, Interpreting texts row, typical column. Do not call it a regulatory requirement, and do not apply it to a master's award or a joint honours course without noting that the issuer wrote the rungs for single honours (4.5). Set it beside the row's other cells (4.8.b2 and 4.8.b2.excellent), the descriptor qaa/fheq-2024/4.15.b7, Annex D's 2.2 and 2.1 cell (qaa/fheq-2024/annex-d/cognitive/r2/2.2 and qaa/fheq-2024/annex-d/cognitive/r2/2.1) and spine:6."
  author-agent-dialogue: "Raise it when a student wants to move from a pass towards a second-class result in reading and interpreting texts, or when a team calibrates marking for the middle of the range. Put it plainly and in the second person to a student, and to staff as the standard most graduates reach. Ask: How does the context in which a text was written change how you read it? Can you set out the argument of a passage step by step and say where it is weakest? Avoid presenting it as the minimum: the threshold cell (4.8.b2) is the floor."
- statement: qaa/philosophy-2025/4.8.b3
  forPractitioner: { text: "At threshold, graduates will use philosophical terms accurately.", rewrite: light, force: threshold, status: drafted }
  forBeneficiary: { text: "To reach the threshold standard, you will use philosophical terms correctly.", rewrite: full, force: threshold, status: drafted }
  author-agent-written: "Present this as the threshold cell of the 'Terminology' row in the subject-specific and intellectual skills table: the floor every single honours graduate in philosophy reaches, which the issuer matches to a third-class degree, at FHEQ level 6 (FQHEIS level 10). Cite it as QAA (2025), Philosophy Subject Benchmark Statement, para 4.8, Terminology row, threshold column. Do not call it a regulatory requirement, and do not apply it to a master's award or a joint honours course without noting that the issuer wrote the rungs for single honours (4.5). Set it beside the row's other cells (4.8.b3.typical and 4.8.b3.excellent), the descriptor qaa/fheq-2024/4.15.b8, Annex D's 3rd cell (qaa/fheq-2024/annex-d/transferable/r1/3rd) and spine:6."
  author-agent-dialogue: "Raise it when a student asks what they must show at the least in philosophical vocabulary to gain an honours degree, or when staff check that every student can reach it. Put it plainly and in the second person to a student, and to staff as the floor the course must make reachable. Ask: Which technical term in your current topic do you find hardest to use exactly? Could you define it in a sentence and give an example of its misuse? Avoid reading the table aloud; give this one cell and name the typical cell (4.8.b3.typical) only as the next step up."
- statement: qaa/philosophy-2025/4.8.b3.excellent
  forPractitioner: { text: "At the excellent level, graduates will handle both general and specialist terms precisely and introduce new terms where the argument needs them.", rewrite: light, force: will, status: drafted }
  forBeneficiary: { text: "To reach the excellent standard, you will use general and specialist terms precisely and, when it helps your argument, introduce new terms of your own.", rewrite: full, force: will, status: drafted }
  author-agent-written: "Present this as the excellent cell of the 'Terminology' row in the subject-specific and intellectual skills table: what the strongest single honours graduates in philosophy reach (will), which the issuer matches to a first-class degree, at FHEQ level 6 (FQHEIS level 10); it is an aspiration, not a requirement. Cite it as QAA (2025), Philosophy Subject Benchmark Statement, para 4.8, Terminology row, excellent column. Do not call it a regulatory requirement, and do not apply it to a master's award or a joint honours course without noting that the issuer wrote the rungs for single honours (4.5). Set it beside the row's other cells (4.8.b3 and 4.8.b3.typical), the descriptor qaa/fheq-2024/4.15.b8, Annex D's 1st cell (qaa/fheq-2024/annex-d/transferable/r1/1st) and spine:6."
  author-agent-dialogue: "Raise it with a student aiming for a first in philosophical vocabulary, or with markers deciding what earns one. Put it plainly and in the second person to a student, and to staff as what marks out the strongest work. Ask: Which technical term in your current topic do you find hardest to use exactly? Could you define it in a sentence and give an example of its misuse? Avoid treating it as what everyone must reach, and do not read the issuer's wording aloud at length."
- statement: qaa/philosophy-2025/4.8.b3.typical
  forPractitioner: { text: "At the typical level, graduates will use philosophical terms precisely, including some specialist ones.", rewrite: light, force: will, status: drafted }
  forBeneficiary: { text: "To reach the typical standard, you will use philosophical terms precisely, including some specialist ones.", rewrite: full, force: will, status: drafted }
  author-agent-written: "Present this as the typical cell of the 'Terminology' row in the subject-specific and intellectual skills table: what most single honours graduates in philosophy reach (will), which the issuer matches to a second-class degree, at FHEQ level 6 (FQHEIS level 10); it is an expectation above the pass line. Cite it as QAA (2025), Philosophy Subject Benchmark Statement, para 4.8, Terminology row, typical column. Do not call it a regulatory requirement, and do not apply it to a master's award or a joint honours course without noting that the issuer wrote the rungs for single honours (4.5). Set it beside the row's other cells (4.8.b3 and 4.8.b3.excellent), the descriptor qaa/fheq-2024/4.15.b8, Annex D's 2.2 and 2.1 cell (qaa/fheq-2024/annex-d/transferable/r1/2.2 and qaa/fheq-2024/annex-d/transferable/r1/2.1) and spine:6."
  author-agent-dialogue: "Raise it when a student wants to move from a pass towards a second-class result in philosophical vocabulary, or when a team calibrates marking for the middle of the range. Put it plainly and in the second person to a student, and to staff as the standard most graduates reach. Ask: Which technical term in your current topic do you find hardest to use exactly? Could you define it in a sentence and give an example of its misuse? Avoid presenting it as the minimum: the threshold cell (4.8.b3) is the floor."
- statement: qaa/philosophy-2025/4.8.b4
  forPractitioner: { text: "At threshold, graduates will present an argument and show awareness of what soundness requires.", rewrite: light, force: threshold, status: drafted }
  forBeneficiary: { text: "To reach the threshold standard, you will make an argument and show that you know what makes an argument sound.", rewrite: full, force: threshold, status: drafted }
  author-agent-written: "Present this as the threshold cell of the 'Formulating arguments' row in the subject-specific and intellectual skills table: the floor every single honours graduate in philosophy reaches, which the issuer matches to a third-class degree, at FHEQ level 6 (FQHEIS level 10). Cite it as QAA (2025), Philosophy Subject Benchmark Statement, para 4.8, Formulating arguments row, threshold column. Do not call it a regulatory requirement, and do not apply it to a master's award or a joint honours course without noting that the issuer wrote the rungs for single honours (4.5). Set it beside the row's other cells (4.8.b4.typical and 4.8.b4.excellent), the descriptor qaa/fheq-2024/4.15.b3.1, Annex D's 3rd cell (qaa/fheq-2024/annex-d/cognitive/r2/3rd) and spine:6."
  author-agent-dialogue: "Raise it when a student asks what they must show at the least in building and defending arguments to gain an honours degree, or when staff check that every student can reach it. Put it plainly and in the second person to a student, and to staff as the floor the course must make reachable. Ask: What is the strongest objection to your main argument, and how do you answer it? Does your conclusion claim more than your premises support? Avoid reading the table aloud; give this one cell and name the typical cell (4.8.b4.typical) only as the next step up."
- statement: qaa/philosophy-2025/4.8.b4.excellent
  forPractitioner: { text: "At the excellent level, graduates will produce precise, rigorous and nuanced arguments whose well-justified conclusions rest on sound reasoning and thorough command of the concepts and theories, aware of their complexities and implications.", rewrite: light, force: will, status: drafted }
  forBeneficiary: { text: "To reach the excellent standard, you will build subtle, precise and rigorous arguments, reach well-supported conclusions and show a deep, clear sense of the complications and consequences involved.", rewrite: full, force: will, status: drafted }
  author-agent-written: "Present this as the excellent cell of the 'Formulating arguments' row in the subject-specific and intellectual skills table: what the strongest single honours graduates in philosophy reach (will), which the issuer matches to a first-class degree, at FHEQ level 6 (FQHEIS level 10); it is an aspiration, not a requirement. Cite it as QAA (2025), Philosophy Subject Benchmark Statement, para 4.8, Formulating arguments row, excellent column. Do not call it a regulatory requirement, and do not apply it to a master's award or a joint honours course without noting that the issuer wrote the rungs for single honours (4.5). Set it beside the row's other cells (4.8.b4 and 4.8.b4.typical), the descriptor qaa/fheq-2024/4.15.b3.1, Annex D's 1st cell (qaa/fheq-2024/annex-d/cognitive/r2/1st) and spine:6."
  author-agent-dialogue: "Raise it with a student aiming for a first in building and defending arguments, or with markers deciding what earns one. Put it plainly and in the second person to a student, and to staff as what marks out the strongest work. Ask: What is the strongest objection to your main argument, and how do you answer it? Does your conclusion claim more than your premises support? Avoid treating it as what everyone must reach, and do not read the issuer's wording aloud at length."
- statement: qaa/philosophy-2025/4.8.b4.typical
  forPractitioner: { text: "At the typical level, graduates will formulate arguments scrupulously, draw only justified conclusions, foresee objections and answer them.", rewrite: light, force: will, status: drafted }
  forBeneficiary: { text: "To reach the typical standard, you will build arguments carefully, claim only what your reasons support, foresee objections and answer them.", rewrite: full, force: will, status: drafted }
  author-agent-written: "Present this as the typical cell of the 'Formulating arguments' row in the subject-specific and intellectual skills table: what most single honours graduates in philosophy reach (will), which the issuer matches to a second-class degree, at FHEQ level 6 (FQHEIS level 10); it is an expectation above the pass line. Cite it as QAA (2025), Philosophy Subject Benchmark Statement, para 4.8, Formulating arguments row, typical column. Do not call it a regulatory requirement, and do not apply it to a master's award or a joint honours course without noting that the issuer wrote the rungs for single honours (4.5). Set it beside the row's other cells (4.8.b4 and 4.8.b4.excellent), the descriptor qaa/fheq-2024/4.15.b3.1, Annex D's 2.2 and 2.1 cell (qaa/fheq-2024/annex-d/cognitive/r2/2.2 and qaa/fheq-2024/annex-d/cognitive/r2/2.1) and spine:6."
  author-agent-dialogue: "Raise it when a student wants to move from a pass towards a second-class result in building and defending arguments, or when a team calibrates marking for the middle of the range. Put it plainly and in the second person to a student, and to staff as the standard most graduates reach. Ask: What is the strongest objection to your main argument, and how do you answer it? Does your conclusion claim more than your premises support? Avoid presenting it as the minimum: the threshold cell (4.8.b4) is the floor."
- statement: qaa/philosophy-2025/4.8.b5
  forPractitioner: { text: "At threshold, graduates will explain complex issues and ideas.", rewrite: light, force: threshold, status: drafted }
  forBeneficiary: { text: "To reach the threshold standard, you will explain complicated ideas.", rewrite: full, force: threshold, status: drafted }
  author-agent-written: "Present this as the threshold cell of the 'Explaining' row in the subject-specific and intellectual skills table: the floor every single honours graduate in philosophy reaches, which the issuer matches to a third-class degree, at FHEQ level 6 (FQHEIS level 10). Cite it as QAA (2025), Philosophy Subject Benchmark Statement, para 4.8, Explaining row, threshold column. Do not call it a regulatory requirement, and do not apply it to a master's award or a joint honours course without noting that the issuer wrote the rungs for single honours (4.5). Set it beside the row's other cells (4.8.b5.typical and 4.8.b5.excellent), the descriptor qaa/fheq-2024/4.15.b8, Annex D's 3rd cell (qaa/fheq-2024/annex-d/transferable/r1/3rd) and spine:6."
  author-agent-dialogue: "Raise it when a student asks what they must show at the least in explaining ideas to gain an honours degree, or when staff check that every student can reach it. Put it plainly and in the second person to a student, and to staff as the floor the course must make reachable. Ask: Could you explain your essay's central idea to someone who has never studied philosophy? Which example best shows what you mean, and where does it mislead? Avoid reading the table aloud; give this one cell and name the typical cell (4.8.b5.typical) only as the next step up."
- statement: qaa/philosophy-2025/4.8.b5.excellent
  forPractitioner: { text: "At the excellent level, graduates will fit explanations to varied audiences while avoiding oversimplification.", rewrite: light, force: will, status: drafted }
  forBeneficiary: { text: "To reach the excellent standard, you will adjust your explanations to suit different audiences without making the ideas too simple.", rewrite: full, force: will, status: drafted }
  author-agent-written: "Present this as the excellent cell of the 'Explaining' row in the subject-specific and intellectual skills table: what the strongest single honours graduates in philosophy reach (will), which the issuer matches to a first-class degree, at FHEQ level 6 (FQHEIS level 10); it is an aspiration, not a requirement. Cite it as QAA (2025), Philosophy Subject Benchmark Statement, para 4.8, Explaining row, excellent column. Do not call it a regulatory requirement, and do not apply it to a master's award or a joint honours course without noting that the issuer wrote the rungs for single honours (4.5). Set it beside the row's other cells (4.8.b5 and 4.8.b5.typical), the descriptor qaa/fheq-2024/4.15.b8, Annex D's 1st cell (qaa/fheq-2024/annex-d/transferable/r1/1st) and spine:6."
  author-agent-dialogue: "Raise it with a student aiming for a first in explaining ideas, or with markers deciding what earns one. Put it plainly and in the second person to a student, and to staff as what marks out the strongest work. Ask: Could you explain your essay's central idea to someone who has never studied philosophy? Which example best shows what you mean, and where does it mislead? Avoid treating it as what everyone must reach, and do not read the issuer's wording aloud at length."
- statement: qaa/philosophy-2025/4.8.b5.typical
  forPractitioner: { text: "At the typical level, graduates will explain complex ideas clearly, simplify them appropriately and illustrate them with good examples.", rewrite: light, force: will, status: drafted }
  forBeneficiary: { text: "To reach the typical standard, you will explain complex ideas clearly, simplify them when that helps and use good examples.", rewrite: full, force: will, status: drafted }
  author-agent-written: "Present this as the typical cell of the 'Explaining' row in the subject-specific and intellectual skills table: what most single honours graduates in philosophy reach (will), which the issuer matches to a second-class degree, at FHEQ level 6 (FQHEIS level 10); it is an expectation above the pass line. Cite it as QAA (2025), Philosophy Subject Benchmark Statement, para 4.8, Explaining row, typical column. Do not call it a regulatory requirement, and do not apply it to a master's award or a joint honours course without noting that the issuer wrote the rungs for single honours (4.5). Set it beside the row's other cells (4.8.b5 and 4.8.b5.excellent), the descriptor qaa/fheq-2024/4.15.b8, Annex D's 2.2 and 2.1 cell (qaa/fheq-2024/annex-d/transferable/r1/2.2 and qaa/fheq-2024/annex-d/transferable/r1/2.1) and spine:6."
  author-agent-dialogue: "Raise it when a student wants to move from a pass towards a second-class result in explaining ideas, or when a team calibrates marking for the middle of the range. Put it plainly and in the second person to a student, and to staff as the standard most graduates reach. Ask: Could you explain your essay's central idea to someone who has never studied philosophy? Which example best shows what you mean, and where does it mislead? Avoid presenting it as the minimum: the threshold cell (4.8.b5) is the floor."
- statement: qaa/philosophy-2025/4.8.b6
  forPractitioner: { text: "At threshold, graduates will show some modest originality.", rewrite: light, force: threshold, status: drafted }
  forBeneficiary: { text: "To reach the threshold standard, you will show some ideas of your own.", rewrite: full, force: threshold, status: drafted }
  author-agent-written: "Present this as the threshold cell of the 'Originality' row in the subject-specific and intellectual skills table: the floor every single honours graduate in philosophy reaches, which the issuer matches to a third-class degree, at FHEQ level 6 (FQHEIS level 10). Cite it as QAA (2025), Philosophy Subject Benchmark Statement, para 4.8, Originality row, threshold column. Do not call it a regulatory requirement, and do not apply it to a master's award or a joint honours course without noting that the issuer wrote the rungs for single honours (4.5). Set it beside the row's other cells (4.8.b6.typical and 4.8.b6.excellent), the descriptor qaa/fqheis-2024/4.16.b6 (some originality at Scottish honours; the FHEQ asks for originality only from qaa/fheq-2024/4.17.b3), Annex D's 3rd cell (qaa/fheq-2024/annex-d/cognitive/r4/3rd) and spine:6."
  author-agent-dialogue: "Raise it when a student asks what they must show at the least in original thinking to gain an honours degree, or when staff check that every student can reach it. Put it plainly and in the second person to a student, and to staff as the floor the course must make reachable. Ask: What in your last piece of work was your own contribution rather than a report of others' views? How would you push that idea further? Avoid reading the table aloud; give this one cell and name the typical cell (4.8.b6.typical) only as the next step up."
- statement: qaa/philosophy-2025/4.8.b6.excellent
  forPractitioner: { text: "At the excellent level, graduates will develop original, plausible lines of argument in depth.", rewrite: light, force: will, status: drafted }
  forBeneficiary: { text: "To reach the excellent standard, you will develop original and convincing lines of argument in depth.", rewrite: full, force: will, status: drafted }
  author-agent-written: "Present this as the excellent cell of the 'Originality' row in the subject-specific and intellectual skills table: what the strongest single honours graduates in philosophy reach (will), which the issuer matches to a first-class degree, at FHEQ level 6 (FQHEIS level 10); it is an aspiration, not a requirement. Cite it as QAA (2025), Philosophy Subject Benchmark Statement, para 4.8, Originality row, excellent column. Do not call it a regulatory requirement, and do not apply it to a master's award or a joint honours course without noting that the issuer wrote the rungs for single honours (4.5). Set it beside the row's other cells (4.8.b6 and 4.8.b6.typical), the descriptor qaa/fqheis-2024/4.16.b6 (some originality at Scottish honours; the FHEQ asks for originality only from qaa/fheq-2024/4.17.b3), Annex D's 1st cell (qaa/fheq-2024/annex-d/cognitive/r4/1st) and spine:6."
  author-agent-dialogue: "Raise it with a student aiming for a first in original thinking, or with markers deciding what earns one. Put it plainly and in the second person to a student, and to staff as what marks out the strongest work. Ask: What in your last piece of work was your own contribution rather than a report of others' views? How would you push that idea further? Avoid treating it as what everyone must reach, and do not read the issuer's wording aloud at length."
- statement: qaa/philosophy-2025/4.8.b6.typical
  forPractitioner: { text: "At the typical level, graduates will develop some original ideas and arguments.", rewrite: light, force: will, status: drafted }
  forBeneficiary: { text: "To reach the typical standard, you will develop some ideas and arguments of your own.", rewrite: full, force: will, status: drafted }
  author-agent-written: "Present this as the typical cell of the 'Originality' row in the subject-specific and intellectual skills table: what most single honours graduates in philosophy reach (will), which the issuer matches to a second-class degree, at FHEQ level 6 (FQHEIS level 10); it is an expectation above the pass line. Cite it as QAA (2025), Philosophy Subject Benchmark Statement, para 4.8, Originality row, typical column. Do not call it a regulatory requirement, and do not apply it to a master's award or a joint honours course without noting that the issuer wrote the rungs for single honours (4.5). Set it beside the row's other cells (4.8.b6 and 4.8.b6.excellent), the descriptor qaa/fqheis-2024/4.16.b6 (some originality at Scottish honours; the FHEQ asks for originality only from qaa/fheq-2024/4.17.b3), Annex D's 2.2 and 2.1 cell (qaa/fheq-2024/annex-d/cognitive/r4/2.2 and qaa/fheq-2024/annex-d/cognitive/r4/2.1) and spine:6."
  author-agent-dialogue: "Raise it when a student wants to move from a pass towards a second-class result in original thinking, or when a team calibrates marking for the middle of the range. Put it plainly and in the second person to a student, and to staff as the standard most graduates reach. Ask: What in your last piece of work was your own contribution rather than a report of others' views? How would you push that idea further? Avoid presenting it as the minimum: the threshold cell (4.8.b6) is the floor."
- statement: qaa/philosophy-2025/4.8.b7
  forPractitioner: { text: "At threshold, graduates will identify strengths and weaknesses in arguments on both sides of a question.", rewrite: light, force: threshold, status: drafted }
  forBeneficiary: { text: "To reach the threshold standard, you will spot the strong and weak points in the arguments on each side of a philosophical question.", rewrite: full, force: threshold, status: drafted }
  author-agent-written: "Present this as the threshold cell of the 'Open-mindedness' row in the subject-specific and intellectual skills table: the floor every single honours graduate in philosophy reaches, which the issuer matches to a third-class degree, at FHEQ level 6 (FQHEIS level 10). Cite it as QAA (2025), Philosophy Subject Benchmark Statement, para 4.8, Open-mindedness row, threshold column. Do not call it a regulatory requirement, and do not apply it to a master's award or a joint honours course without noting that the issuer wrote the rungs for single honours (4.5). Set it beside the row's other cells (4.8.b7.typical and 4.8.b7.excellent), the descriptor qaa/fheq-2024/4.15.b4, Annex D's 3rd cell (qaa/fheq-2024/annex-d/cognitive/r2/3rd) and spine:6."
  author-agent-dialogue: "Raise it when a student asks what they must show at the least in weighing views you do not hold to gain an honours degree, or when staff check that every student can reach it. Put it plainly and in the second person to a student, and to staff as the floor the course must make reachable. Ask: What is the best argument against a view you hold? When did an argument last change your mind? Avoid reading the table aloud; give this one cell and name the typical cell (4.8.b7.typical) only as the next step up."
- statement: qaa/philosophy-2025/4.8.b7.excellent
  forPractitioner: { text: "At the excellent level, graduates will suspend judgement, approach new perspectives with curiosity and honestly revise strongly held views where warranted.", rewrite: light, force: will, status: drafted }
  forBeneficiary: { text: "To reach the excellent standard, you will hold off judging, explore new perspectives with curiosity and honestly change even firmly held beliefs when the arguments call for it.", rewrite: full, force: will, status: drafted }
  author-agent-written: "Present this as the excellent cell of the 'Open-mindedness' row in the subject-specific and intellectual skills table: what the strongest single honours graduates in philosophy reach (will), which the issuer matches to a first-class degree, at FHEQ level 6 (FQHEIS level 10); it is an aspiration, not a requirement. Cite it as QAA (2025), Philosophy Subject Benchmark Statement, para 4.8, Open-mindedness row, excellent column. Do not call it a regulatory requirement, and do not apply it to a master's award or a joint honours course without noting that the issuer wrote the rungs for single honours (4.5). Set it beside the row's other cells (4.8.b7 and 4.8.b7.typical), the descriptor qaa/fheq-2024/4.15.b4, Annex D's 1st cell (qaa/fheq-2024/annex-d/cognitive/r2/1st) and spine:6."
  author-agent-dialogue: "Raise it with a student aiming for a first in weighing views you do not hold, or with markers deciding what earns one. Put it plainly and in the second person to a student, and to staff as what marks out the strongest work. Ask: What is the best argument against a view you hold? When did an argument last change your mind? Avoid treating it as what everyone must reach, and do not read the issuer's wording aloud at length."
- statement: qaa/philosophy-2025/4.8.b7.typical
  forPractitioner: { text: "At the typical level, graduates will review unfamiliar ideas openly and change their minds where appropriate.", rewrite: light, force: will, status: drafted }
  forBeneficiary: { text: "To reach the typical standard, you will consider new ideas with an open mind and be willing to change your view when you should.", rewrite: full, force: will, status: drafted }
  author-agent-written: "Present this as the typical cell of the 'Open-mindedness' row in the subject-specific and intellectual skills table: what most single honours graduates in philosophy reach (will), which the issuer matches to a second-class degree, at FHEQ level 6 (FQHEIS level 10); it is an expectation above the pass line. Cite it as QAA (2025), Philosophy Subject Benchmark Statement, para 4.8, Open-mindedness row, typical column. Do not call it a regulatory requirement, and do not apply it to a master's award or a joint honours course without noting that the issuer wrote the rungs for single honours (4.5). Set it beside the row's other cells (4.8.b7 and 4.8.b7.excellent), the descriptor qaa/fheq-2024/4.15.b4, Annex D's 2.2 and 2.1 cell (qaa/fheq-2024/annex-d/cognitive/r2/2.2 and qaa/fheq-2024/annex-d/cognitive/r2/2.1) and spine:6."
  author-agent-dialogue: "Raise it when a student wants to move from a pass towards a second-class result in weighing views you do not hold, or when a team calibrates marking for the middle of the range. Put it plainly and in the second person to a student, and to staff as the standard most graduates reach. Ask: What is the best argument against a view you hold? When did an argument last change your mind? Avoid presenting it as the minimum: the threshold cell (4.8.b7) is the floor."
- statement: qaa/philosophy-2025/4.8.b8
  forPractitioner: { text: "At threshold, graduates will identify some ways in which philosophy feeds into, and draws on, other disciplines.", rewrite: light, force: threshold, status: drafted }
  forBeneficiary: { text: "To reach the threshold standard, you will point to some ways philosophy and other subjects learn from each other.", rewrite: full, force: threshold, status: drafted }
  author-agent-written: "Present this as the threshold cell of the 'Interdisciplinarity' row in the subject-specific and intellectual skills table: the floor every single honours graduate in philosophy reaches, which the issuer matches to a third-class degree, at FHEQ level 6 (FQHEIS level 10). Cite it as QAA (2025), Philosophy Subject Benchmark Statement, para 4.8, Interdisciplinarity row, threshold column. Do not call it a regulatory requirement, and do not apply it to a master's award or a joint honours course without noting that the issuer wrote the rungs for single honours (4.5). Set it beside the row's other cells (4.8.b8.typical and 4.8.b8.excellent), the descriptor qaa/fheq-2024/4.15.b6, Annex D's 3rd cell (qaa/fheq-2024/annex-d/knowledge/r1/3rd) and spine:6."
  author-agent-dialogue: "Raise it when a student asks what they must show at the least in links between philosophy and other subjects to gain an honours degree, or when staff check that every student can reach it. Put it plainly and in the second person to a student, and to staff as the floor the course must make reachable. Ask: Which other subject has your philosophical work drawn on, or could it help? What philosophical assumption have you noticed in work from another field? Avoid reading the table aloud; give this one cell and name the typical cell (4.8.b8.typical) only as the next step up."
- statement: qaa/philosophy-2025/4.8.b8.excellent
  forPractitioner: { text: "At the excellent level, graduates will analyse and critique philosophical doctrines embedded in work from other disciplines and recognise what outside ideas and research contribute to philosophical debate.", rewrite: light, force: will, status: drafted }
  forBeneficiary: { text: "To reach the excellent standard, you will find and critique the philosophical ideas inside work from other subjects, and see how research from those subjects matters to philosophical debates.", rewrite: full, force: will, status: drafted }
  author-agent-written: "Present this as the excellent cell of the 'Interdisciplinarity' row in the subject-specific and intellectual skills table: what the strongest single honours graduates in philosophy reach (will), which the issuer matches to a first-class degree, at FHEQ level 6 (FQHEIS level 10); it is an aspiration, not a requirement. Cite it as QAA (2025), Philosophy Subject Benchmark Statement, para 4.8, Interdisciplinarity row, excellent column. Do not call it a regulatory requirement, and do not apply it to a master's award or a joint honours course without noting that the issuer wrote the rungs for single honours (4.5). Set it beside the row's other cells (4.8.b8 and 4.8.b8.typical), the descriptor qaa/fheq-2024/4.15.b6, Annex D's 1st cell (qaa/fheq-2024/annex-d/knowledge/r1/1st) and spine:6."
  author-agent-dialogue: "Raise it with a student aiming for a first in links between philosophy and other subjects, or with markers deciding what earns one. Put it plainly and in the second person to a student, and to staff as what marks out the strongest work. Ask: Which other subject has your philosophical work drawn on, or could it help? What philosophical assumption have you noticed in work from another field? Avoid treating it as what everyone must reach, and do not read the issuer's wording aloud at length."
- statement: qaa/philosophy-2025/4.8.b8.typical
  forPractitioner: { text: "At the typical level, graduates will describe and explain some of the two-way links between philosophy and other disciplines.", rewrite: light, force: will, status: drafted }
  forBeneficiary: { text: "To reach the typical standard, you will describe and explain some ways philosophy and other subjects learn from each other.", rewrite: full, force: will, status: drafted }
  author-agent-written: "Present this as the typical cell of the 'Interdisciplinarity' row in the subject-specific and intellectual skills table: what most single honours graduates in philosophy reach (will), which the issuer matches to a second-class degree, at FHEQ level 6 (FQHEIS level 10); it is an expectation above the pass line. Cite it as QAA (2025), Philosophy Subject Benchmark Statement, para 4.8, Interdisciplinarity row, typical column. Do not call it a regulatory requirement, and do not apply it to a master's award or a joint honours course without noting that the issuer wrote the rungs for single honours (4.5). Set it beside the row's other cells (4.8.b8 and 4.8.b8.excellent), the descriptor qaa/fheq-2024/4.15.b6, Annex D's 2.2 and 2.1 cell (qaa/fheq-2024/annex-d/knowledge/r1/2.2 and qaa/fheq-2024/annex-d/knowledge/r1/2.1) and spine:6."
  author-agent-dialogue: "Raise it when a student wants to move from a pass towards a second-class result in links between philosophy and other subjects, or when a team calibrates marking for the middle of the range. Put it plainly and in the second person to a student, and to staff as the standard most graduates reach. Ask: Which other subject has your philosophical work drawn on, or could it help? What philosophical assumption have you noticed in work from another field? Avoid presenting it as the minimum: the threshold cell (4.8.b8) is the floor."
- statement: qaa/philosophy-2025/4.8.b9
  forPractitioner: { text: "At threshold, graduates will state some ways philosophy connects with ordinary life.", rewrite: light, force: threshold, status: drafted }
  forBeneficiary: { text: "To reach the threshold standard, you will say how philosophy can connect with some everyday concerns.", rewrite: full, force: threshold, status: drafted }
  author-agent-written: "Present this as the threshold cell of the 'Applications' row in the subject-specific and intellectual skills table: the floor every single honours graduate in philosophy reaches, which the issuer matches to a third-class degree, at FHEQ level 6 (FQHEIS level 10). Cite it as QAA (2025), Philosophy Subject Benchmark Statement, para 4.8, Applications row, threshold column. Do not call it a regulatory requirement, and do not apply it to a master's award or a joint honours course without noting that the issuer wrote the rungs for single honours (4.5). Set it beside the row's other cells (4.8.b9.typical and 4.8.b9.excellent), the descriptor qaa/fheq-2024/4.15.b6, Annex D's 3rd cell (qaa/fheq-2024/annex-d/practical/r1/3rd) and spine:6."
  author-agent-dialogue: "Raise it when a student asks what they must show at the least in using philosophy in everyday life to gain an honours degree, or when staff check that every student can reach it. Put it plainly and in the second person to a student, and to staff as the floor the course must make reachable. Ask: Where in everyday life, at work or in the news, could your philosophy make a difference? How would you use it on a real ethical dilemma? Avoid reading the table aloud; give this one cell and name the typical cell (4.8.b9.typical) only as the next step up."
- statement: qaa/philosophy-2025/4.8.b9.excellent
  forPractitioner: { text: "At the excellent level, graduates will apply philosophical insight with nuance to everyday experience, shedding light on real problems and ethical dilemmas and helping to address them.", rewrite: light, force: will, status: drafted }
  forBeneficiary: { text: "To reach the excellent standard, you will show a subtle grasp of how philosophy matters to daily life and use it to shed light on real problems and ethical dilemmas.", rewrite: full, force: will, status: drafted }
  author-agent-written: "Present this as the excellent cell of the 'Applications' row in the subject-specific and intellectual skills table: what the strongest single honours graduates in philosophy reach (will), which the issuer matches to a first-class degree, at FHEQ level 6 (FQHEIS level 10); it is an aspiration, not a requirement. Cite it as QAA (2025), Philosophy Subject Benchmark Statement, para 4.8, Applications row, excellent column. Do not call it a regulatory requirement, and do not apply it to a master's award or a joint honours course without noting that the issuer wrote the rungs for single honours (4.5). Set it beside the row's other cells (4.8.b9 and 4.8.b9.typical), the descriptor qaa/fheq-2024/4.15.b6, Annex D's 1st cell (qaa/fheq-2024/annex-d/practical/r1/1st) and spine:6."
  author-agent-dialogue: "Raise it with a student aiming for a first in using philosophy in everyday life, or with markers deciding what earns one. Put it plainly and in the second person to a student, and to staff as what marks out the strongest work. Ask: Where in everyday life, at work or in the news, could your philosophy make a difference? How would you use it on a real ethical dilemma? Avoid treating it as what everyone must reach, and do not read the issuer's wording aloud at length."
- statement: qaa/philosophy-2025/4.8.b9.typical
  forPractitioner: { text: "At the typical level, graduates will describe and explain some connections between philosophy and ordinary life.", rewrite: light, force: will, status: drafted }
  forBeneficiary: { text: "To reach the typical standard, you will describe and explain some ways philosophy connects with everyday concerns.", rewrite: full, force: will, status: drafted }
  author-agent-written: "Present this as the typical cell of the 'Applications' row in the subject-specific and intellectual skills table: what most single honours graduates in philosophy reach (will), which the issuer matches to a second-class degree, at FHEQ level 6 (FQHEIS level 10); it is an expectation above the pass line. Cite it as QAA (2025), Philosophy Subject Benchmark Statement, para 4.8, Applications row, typical column. Do not call it a regulatory requirement, and do not apply it to a master's award or a joint honours course without noting that the issuer wrote the rungs for single honours (4.5). Set it beside the row's other cells (4.8.b9 and 4.8.b9.excellent), the descriptor qaa/fheq-2024/4.15.b6, Annex D's 2.2 and 2.1 cell (qaa/fheq-2024/annex-d/practical/r1/2.2 and qaa/fheq-2024/annex-d/practical/r1/2.1) and spine:6."
  author-agent-dialogue: "Raise it when a student wants to move from a pass towards a second-class result in using philosophy in everyday life, or when a team calibrates marking for the middle of the range. Put it plainly and in the second person to a student, and to staff as the standard most graduates reach. Ask: Where in everyday life, at work or in the news, could your philosophy make a difference? How would you use it on a real ethical dilemma? Avoid presenting it as the minimum: the threshold cell (4.8.b9) is the floor."
- statement: qaa/philosophy-2025/4.10.b1
  forPractitioner: { text: "Graduates will identify the issues, questions and problems a topic raises.", rewrite: light, force: will, status: drafted }
  forBeneficiary: { text: "You will be able to spot the issues, questions and problems a topic raises.", rewrite: full, force: will, status: drafted }
  author-agent-written: "Present this as a generic skill that every philosophy graduate at undergraduate level will show, from a list with no rungs, at FHEQ level 6 (FQHEIS level 10). Cite it as QAA (2025), Philosophy Subject Benchmark Statement, para 4.10, item 1. Do not describe it as subject-specific, as regulatory or as graded into threshold, typical and excellent. Set it beside the descriptor qaa/fheq-2024/4.15.b7, Annex D's qaa/fheq-2024/annex-d/cognitive/r3/3rd and the reference framework's strand:thinking at spine:6."
  author-agent-dialogue: "Bring it up when a student or a team is discussing how to frame a question, for example in personal tutoring, before a placement or in a review of transferable skills. Put it plainly, in the second person to a student and as a programme outcome to staff. Ask: What is the real question behind the task you have been set? Which problems does it raise that are not yet answered? Avoid reading the whole list aloud; take one skill at a time."
- statement: qaa/philosophy-2025/4.10.b2
  forPractitioner: { text: "Graduates will identify gaps in what they know and acquire the knowledge to fill them.", rewrite: light, force: will, status: drafted }
  forBeneficiary: { text: "You will be able to see what you do not yet know and go and learn it.", rewrite: full, force: will, status: drafted }
  author-agent-written: "Present this as a generic skill that every philosophy graduate at undergraduate level will show, from a list with no rungs, at FHEQ level 6 (FQHEIS level 10). Cite it as QAA (2025), Philosophy Subject Benchmark Statement, para 4.10, item 2. Do not describe it as subject-specific, as regulatory or as graded into threshold, typical and excellent. Set it beside the descriptor qaa/fheq-2024/4.15.b4 and qaa/fheq-2024/4.15.b5, Annex D's qaa/fheq-2024/annex-d/transferable/r3/3rd and the reference framework's strand:autonomy at spine:6."
  author-agent-dialogue: "Bring it up when a student or a team is discussing gaps in what someone knows, for example in personal tutoring, before a placement or in a review of transferable skills. Put it plainly, in the second person to a student and as a programme outcome to staff. Ask: What do you still need to find out before you can answer this? Where will you go to learn it? Avoid reading the whole list aloud; take one skill at a time."
- statement: qaa/philosophy-2025/4.10.b3
  forPractitioner: { text: "Graduates will understand and analyse the knowledge and information they meet.", rewrite: light, force: will, status: drafted }
  forBeneficiary: { text: "You will be able to understand and analyse the knowledge and information you come across.", rewrite: full, force: will, status: drafted }
  author-agent-written: "Present this as a generic skill that every philosophy graduate at undergraduate level will show, from a list with no rungs, at FHEQ level 6 (FQHEIS level 10). Cite it as QAA (2025), Philosophy Subject Benchmark Statement, para 4.10, item 3. Do not describe it as subject-specific, as regulatory or as graded into threshold, typical and excellent. Set it beside the descriptor qaa/fheq-2024/4.15.b7, Annex D's qaa/fheq-2024/annex-d/cognitive/r2/3rd and the reference framework's strand:thinking at spine:6."
  author-agent-dialogue: "Bring it up when a student or a team is discussing making sense of sources and data, for example in personal tutoring, before a placement or in a review of transferable skills. Put it plainly, in the second person to a student and as a programme outcome to staff. Ask: What are the key claims in this source, and what supports them? Which piece of information here would you trust least, and why? Avoid reading the whole list aloud; take one skill at a time."
- statement: qaa/philosophy-2025/4.10.b4
  forPractitioner: { text: "Graduates will synthesise the current state of knowledge on a topic.", rewrite: light, force: will, status: drafted }
  forBeneficiary: { text: "You will be able to pull together what is currently known about a topic.", rewrite: full, force: will, status: drafted }
  author-agent-written: "Present this as a generic skill that every philosophy graduate at undergraduate level will show, from a list with no rungs, at FHEQ level 6 (FQHEIS level 10). Cite it as QAA (2025), Philosophy Subject Benchmark Statement, para 4.10, item 4. Do not describe it as subject-specific, as regulatory or as graded into threshold, typical and excellent. Set it beside the descriptor qaa/fheq-2024/4.15.b6, Annex D's qaa/fheq-2024/annex-d/knowledge/r3/3rd and the reference framework's strand:thinking at spine:6."
  author-agent-dialogue: "Bring it up when a student or a team is discussing summing up a field, for example in personal tutoring, before a placement or in a review of transferable skills. Put it plainly, in the second person to a student and as a programme outcome to staff. Ask: Could you sum up where the debate on your topic now stands in a paragraph? Which sources would you need to bring together to do that? Avoid reading the whole list aloud; take one skill at a time."
- statement: qaa/philosophy-2025/4.10.b5
  forPractitioner: { text: "Graduates will apply knowledge and understanding to reach conclusions supported by evidence.", rewrite: light, force: will, status: drafted }
  forBeneficiary: { text: "You will be able to use what you know to reach conclusions backed by evidence.", rewrite: full, force: will, status: drafted }
  author-agent-written: "Present this as a generic skill that every philosophy graduate at undergraduate level will show, from a list with no rungs, at FHEQ level 6 (FQHEIS level 10). Cite it as QAA (2025), Philosophy Subject Benchmark Statement, para 4.10, item 5. Do not describe it as subject-specific, as regulatory or as graded into threshold, typical and excellent. Set it beside the descriptor qaa/fheq-2024/4.15.b7, Annex D's qaa/fheq-2024/annex-d/cognitive/r3/3rd and the reference framework's strand:application at spine:6."
  author-agent-dialogue: "Bring it up when a student or a team is discussing drawing conclusions, for example in personal tutoring, before a placement or in a review of transferable skills. Put it plainly, in the second person to a student and as a programme outcome to staff. Ask: What evidence or reasons support your conclusion? What would make you change it? Avoid reading the whole list aloud; take one skill at a time."
- statement: qaa/philosophy-2025/4.10.b6
  forPractitioner: { text: "Graduates will communicate effectively and appropriately, verbally, non-verbally or both.", rewrite: light, force: will, status: drafted }
  forBeneficiary: { text: "You will be able to communicate well and appropriately, in speech or in other forms.", rewrite: full, force: will, status: drafted }
  author-agent-written: "Present this as a generic skill that every philosophy graduate at undergraduate level will show, from a list with no rungs, at FHEQ level 6 (FQHEIS level 10). Cite it as QAA (2025), Philosophy Subject Benchmark Statement, para 4.10, item 6. Do not describe it as subject-specific, as regulatory or as graded into threshold, typical and excellent. Set it beside the descriptor qaa/fheq-2024/4.15.b8, Annex D's qaa/fheq-2024/annex-d/transferable/r1/3rd and the reference framework's strand:communication at spine:6."
  author-agent-dialogue: "Bring it up when a student or a team is discussing communication, for example in personal tutoring, before a placement or in a review of transferable skills. Put it plainly, in the second person to a student and as a programme outcome to staff. Ask: Which form of communication, spoken, written or visual, do you find hardest? How could you practise it on your course? Avoid reading the whole list aloud; take one skill at a time."
- statement: qaa/philosophy-2025/4.10.b7
  forPractitioner: { text: "Graduates will present knowledge or an argument in a form others can understand.", rewrite: light, force: will, status: drafted }
  forBeneficiary: { text: "You will be able to set out what you know, or an argument, so other people can follow it.", rewrite: full, force: will, status: drafted }
  author-agent-written: "Present this as a generic skill that every philosophy graduate at undergraduate level will show, from a list with no rungs, at FHEQ level 6 (FQHEIS level 10). Cite it as QAA (2025), Philosophy Subject Benchmark Statement, para 4.10, item 7. Do not describe it as subject-specific, as regulatory or as graded into threshold, typical and excellent. Set it beside the descriptor qaa/fheq-2024/4.15.b8, Annex D's qaa/fheq-2024/annex-d/transferable/r1/3rd and the reference framework's strand:communication at spine:6."
  author-agent-dialogue: "Bring it up when a student or a team is discussing presenting work, for example in personal tutoring, before a placement or in a review of transferable skills. Put it plainly, in the second person to a student and as a programme outcome to staff. Ask: Could a classmate follow your argument without asking you questions? Where would they get lost? Avoid reading the whole list aloud; take one skill at a time."
- statement: qaa/philosophy-2025/4.10.b8
  forPractitioner: { text: "Graduates will engage critically with varied digital tools to collate, analyse, select and present information.", rewrite: light, force: will, status: drafted }
  forBeneficiary: { text: "You will be able to use different digital tools critically to gather, analyse, choose and present information.", rewrite: full, force: will, status: drafted }
  author-agent-written: "Present this as a generic skill that every philosophy graduate at undergraduate level will show, from a list with no rungs, at FHEQ level 6 (FQHEIS level 10). Cite it as QAA (2025), Philosophy Subject Benchmark Statement, para 4.10, item 8. Do not describe it as subject-specific, as regulatory or as graded into threshold, typical and excellent. Set it beside the descriptor qaa/fheq-2024/4.15.b8, Annex D's qaa/fheq-2024/annex-d/transferable/r1/3rd and the reference framework's strand:application at spine:6."
  author-agent-dialogue: "Bring it up when a student or a team is discussing digital tools, for example in personal tutoring, before a placement or in a review of transferable skills. Put it plainly, in the second person to a student and as a programme outcome to staff. Ask: Which digital tools do you use to find and organise sources, and how do you check what they give you? Where might a tool, generative AI included, be misleading you? Avoid reading the whole list aloud; take one skill at a time."
- statement: qaa/philosophy-2025/4.10.b9
  forPractitioner: { text: "Graduates will assert intellectual independence by working independently with fitting guidance, carrying out self-directed research and exercising critical judgement.", rewrite: light, force: will, status: drafted }
  forBeneficiary: { text: "You will be able to think for yourself: work on your own with the right support, carry out your own research and make critical judgements.", rewrite: full, force: will, status: drafted }
  author-agent-written: "Present this as a generic skill that every philosophy graduate at undergraduate level will show, from a list with no rungs, at FHEQ level 6 (FQHEIS level 10). Cite it as QAA (2025), Philosophy Subject Benchmark Statement, para 4.10, item 9. Do not describe it as subject-specific, as regulatory or as graded into threshold, typical and excellent. Set it beside the descriptor qaa/fheq-2024/4.15.b5 and qaa/fheq-2024/4.15.b9.1, Annex D's qaa/fheq-2024/annex-d/transferable/r3/3rd and the reference framework's strand:autonomy at spine:6."
  author-agent-dialogue: "Bring it up when a student or a team is discussing independent study, for example in personal tutoring, before a placement or in a review of transferable skills. Put it plainly, in the second person to a student and as a programme outcome to staff. Ask: Which part of your last project did you direct yourself? Where did you need guidance, and could you manage it alone next time? Avoid reading the whole list aloud; take one skill at a time."
- statement: qaa/philosophy-2025/4.10.b10
  forPractitioner: { text: "Graduates will work collaboratively, through group or team work, discussion or both.", rewrite: light, force: will, status: drafted }
  forBeneficiary: { text: "You will be able to work with others, in a group or team or by joining in discussions.", rewrite: full, force: will, status: drafted }
  author-agent-written: "Present this as a generic skill that every philosophy graduate at undergraduate level will show, from a list with no rungs, at FHEQ level 6 (FQHEIS level 10). Cite it as QAA (2025), Philosophy Subject Benchmark Statement, para 4.10, item 10. Do not describe it as subject-specific, as regulatory or as graded into threshold, typical and excellent. Set it beside the descriptor qaa/fheq-2024/4.15.b9.1, Annex D's qaa/fheq-2024/annex-d/transferable/r2/3rd and the reference framework's strand:communication at spine:6."
  author-agent-dialogue: "Bring it up when a student or a team is discussing group work and discussion, for example in personal tutoring, before a placement or in a review of transferable skills. Put it plainly, in the second person to a student and as a programme outcome to staff. Ask: What did you contribute to the last group task or seminar discussion? How did you respond when someone disagreed with you? Avoid reading the whole list aloud; take one skill at a time."
- statement: qaa/philosophy-2025/4.10.b11
  forPractitioner: { text: "Graduates will reflect on their own progress, including matters of academic integrity.", rewrite: light, force: will, status: drafted }
  forBeneficiary: { text: "You will be able to reflect on your own progress, including how you keep your work honest and properly referenced.", rewrite: full, force: will, status: drafted }
  author-agent-written: "Present this as a generic skill that every philosophy graduate at undergraduate level will show, from a list with no rungs, at FHEQ level 6 (FQHEIS level 10). Cite it as QAA (2025), Philosophy Subject Benchmark Statement, para 4.10, item 11. Do not describe it as subject-specific, as regulatory or as graded into threshold, typical and excellent. Set it beside the descriptor qaa/fheq-2024/4.15.b5, Annex D's qaa/fheq-2024/annex-d/transferable/r5/3rd and the reference framework's strand:autonomy at spine:6."
  author-agent-dialogue: "Bring it up when a student or a team is discussing progress and academic integrity, for example in personal tutoring, before a placement or in a review of transferable skills. Put it plainly, in the second person to a student and as a programme outcome to staff. Ask: What has improved most in your work this year, and what has not? How do you make sure your use of sources and tools keeps the work your own? Avoid reading the whole list aloud; take one skill at a time."
- statement: qaa/philosophy-2025/4.10.b12
  forPractitioner: { text: "Graduates will identify and examine the values and ethics underlying culture, society and personal life.", rewrite: light, force: will, status: drafted }
  forBeneficiary: { text: "You will be able to recognise and question the values and ethics behind culture, society and your own life.", rewrite: full, force: will, status: drafted }
  author-agent-written: "Present this as a generic skill that every philosophy graduate at undergraduate level will show, from a list with no rungs, at FHEQ level 6 (FQHEIS level 10). Cite it as QAA (2025), Philosophy Subject Benchmark Statement, para 4.10, item 12. Do not describe it as subject-specific, as regulatory or as graded into threshold, typical and excellent. Set it beside the descriptor qaa/fheq-2024/4.15.b7 and qaa/fheq-2024/4.15.b9.2, Annex D's qaa/fheq-2024/annex-d/summary/r1/3rd and the reference framework's strand:thinking at spine:6."
  author-agent-dialogue: "Bring it up when a student or a team is discussing values in culture, society and one's own life, for example in personal tutoring, before a placement or in a review of transferable skills. Put it plainly, in the second person to a student and as a programme outcome to staff. Ask: Which value is doing the work in this policy or practice? Do you hold it yourself, and why? Avoid reading the whole list aloud; take one skill at a time."
- statement: qaa/philosophy-2025/4.11.b1.masters
  forPractitioner: { text: "Master's graduates will understand the key concepts, theories, issues and debates of philosophy in a sophisticated and comprehensive way, shaped by current research.", rewrite: light, force: will, status: drafted }
  forBeneficiary: { text: "You will understand the main concepts, theories, issues and debates in philosophy in depth and breadth, shaped by current research.", rewrite: full, force: will, status: drafted }
  author-agent-written: "Present this as an outcome that holders of a master's degree in philosophy will show (will), at FHEQ level 7 (FQHEIS level 11); it comes from the one master's list, held here as that award's threshold. Cite it as QAA (2025), Philosophy Subject Benchmark Statement, para 4.11, item 1. Do not apply it to the honours degree, do not call it regulatory and do not grade it, since the issuer gives no typical or excellent master's rungs. Set it beside the descriptor qaa/fheq-2024/4.17.b1, spine:7 and, for the step up from honours, 4.6.b5.excellent."
  author-agent-dialogue: "Raise it with a master's student or a master's programme team when the depth of their grasp of the discipline comes up, for example in dissertation supervision or programme review. Use plain words: the second person for a student, a programme outcome for staff. Ask: Which current debate in your area could you map, with its main positions and recent contributions? How has recent research changed your view of it? Avoid holding an undergraduate to it, and do not read the list aloud."
- statement: qaa/philosophy-2025/4.11.b2.masters
  forPractitioner: { text: "Master's graduates will know which research methods suit their work and will apply the research skills it needs.", rewrite: light, force: will, status: drafted }
  forBeneficiary: { text: "You will know which research methods suit your work and use the research skills it calls for.", rewrite: full, force: will, status: drafted }
  author-agent-written: "Present this as an outcome that holders of a master's degree in philosophy will show (will), at FHEQ level 7 (FQHEIS level 11); it comes from the one master's list, held here as that award's threshold. Cite it as QAA (2025), Philosophy Subject Benchmark Statement, para 4.11, item 2. Do not apply it to the honours degree, do not call it regulatory and do not grade it, since the issuer gives no typical or excellent master's rungs. Set it beside the descriptor qaa/fheq-2024/4.17.b2, spine:7 and, for the step up from honours, 4.10.b9."
  author-agent-dialogue: "Raise it with a master's student or a master's programme team when research method comes up, for example in dissertation supervision or programme review. Use plain words: the second person for a student, a programme outcome for staff. Ask: What method does your dissertation use, and why that one? Which research skill do you most need to strengthen? Avoid holding an undergraduate to it, and do not read the list aloud."
- statement: qaa/philosophy-2025/4.11.b3.masters
  forPractitioner: { text: "Master's graduates will construct, evaluate and critically analyse demanding philosophical arguments, texts and problems at an advanced standard, with rigorous method.", rewrite: light, force: will, status: drafted }
  forBeneficiary: { text: "You will be able to build, assess and critically analyse difficult philosophical arguments, texts and problems at an advanced level, using rigorous methods.", rewrite: full, force: will, status: drafted }
  author-agent-written: "Present this as an outcome that holders of a master's degree in philosophy will show (will), at FHEQ level 7 (FQHEIS level 11); it comes from the one master's list, held here as that award's threshold. Cite it as QAA (2025), Philosophy Subject Benchmark Statement, para 4.11, item 3. Do not apply it to the honours degree, do not call it regulatory and do not grade it, since the issuer gives no typical or excellent master's rungs. Set it beside the descriptor qaa/fheq-2024/4.17.b4.1 and qaa/fheq-2024/4.17.b4.2, spine:7 and, for the step up from honours, 4.8.b4.excellent."
  author-agent-dialogue: "Raise it with a master's student or a master's programme team when the rigour of their analysis comes up, for example in dissertation supervision or programme review. Use plain words: the second person for a student, a programme outcome for staff. Ask: Which argument in your field have you analysed most rigorously, and what method did you use? Where does your analysis still rely on an assumption you have not defended? Avoid holding an undergraduate to it, and do not read the list aloud."
- statement: qaa/philosophy-2025/4.11.b4.masters
  forPractitioner: { text: "Master's graduates will have expert knowledge of one or more specialist areas or traditions from in-depth study and research.", rewrite: light, force: will, status: drafted }
  forBeneficiary: { text: "You will become expert in one or more specialist areas or traditions of philosophy through deep study and research.", rewrite: full, force: will, status: drafted }
  author-agent-written: "Present this as an outcome that holders of a master's degree in philosophy will show (will), at FHEQ level 7 (FQHEIS level 11); it comes from the one master's list, held here as that award's threshold. Cite it as QAA (2025), Philosophy Subject Benchmark Statement, para 4.11, item 4. Do not apply it to the honours degree, do not call it regulatory and do not grade it, since the issuer gives no typical or excellent master's rungs. Set it beside the descriptor qaa/fheq-2024/4.17.b1, spine:7 and, for the step up from honours, 4.6.b1.excellent."
  author-agent-dialogue: "Raise it with a master's student or a master's programme team when specialisation comes up, for example in dissertation supervision or programme review. Use plain words: the second person for a student, a programme outcome for staff. Ask: Which area or tradition would you call your specialism now? What have you read in it that a non-specialist would not know? Avoid holding an undergraduate to it, and do not read the list aloud."
- statement: qaa/philosophy-2025/4.11.b5.masters
  forPractitioner: { text: "Master's graduates will conceive, design and complete a substantial philosophical research project that makes a contribution to the field.", rewrite: light, force: will, status: drafted }
  forBeneficiary: { text: "You will be able to plan, design and complete a substantial philosophical research project that adds something to your field.", rewrite: full, force: will, status: drafted }
  author-agent-written: "Present this as an outcome that holders of a master's degree in philosophy will show (will), at FHEQ level 7 (FQHEIS level 11); it comes from the one master's list, held here as that award's threshold. Cite it as QAA (2025), Philosophy Subject Benchmark Statement, para 4.11, item 5. Do not apply it to the honours degree, do not call it regulatory and do not grade it, since the issuer gives no typical or excellent master's rungs. Set it beside the descriptor qaa/fheq-2024/4.17.b3 and qaa/fheq-2024/4.17.b6, spine:7 and, for the step up from honours, 4.10.b9 (and not spine:8: do not claim a doctoral contribution)."
  author-agent-dialogue: "Raise it with a master's student or a master's programme team when the dissertation or research project comes up, for example in dissertation supervision or programme review. Use plain words: the second person for a student, a programme outcome for staff. Ask: What will your research project add that is not already in the literature? Is its scope realistic for the time you have? Avoid holding an undergraduate to it, and do not read the list aloud."
- statement: qaa/philosophy-2025/4.11.b6.masters
  forPractitioner: { text: "Master's graduates will analyse rationally and logically, interpret complex ideas and construct sophisticated reasoning at a highly developed level.", rewrite: light, force: will, status: drafted }
  forBeneficiary: { text: "You will be highly skilled at logical analysis, at interpreting complex ideas and at building sophisticated arguments.", rewrite: full, force: will, status: drafted }
  author-agent-written: "Present this as an outcome that holders of a master's degree in philosophy will show (will), at FHEQ level 7 (FQHEIS level 11); it comes from the one master's list, held here as that award's threshold. Cite it as QAA (2025), Philosophy Subject Benchmark Statement, para 4.11, item 6. Do not apply it to the honours degree, do not call it regulatory and do not grade it, since the issuer gives no typical or excellent master's rungs. Set it beside the descriptor qaa/fheq-2024/4.17.b5, spine:7 and, for the step up from honours, 4.8.b4.excellent and 4.8.b2.excellent."
  author-agent-dialogue: "Raise it with a master's student or a master's programme team when the quality of their reasoning comes up, for example in dissertation supervision or programme review. Use plain words: the second person for a student, a programme outcome for staff. Ask: Which step in your argument would a logician press you on? How would you restate the hardest idea in your topic in your own terms? Avoid holding an undergraduate to it, and do not read the list aloud."
- statement: qaa/philosophy-2025/4.11.b7.masters
  forPractitioner: { text: "Master's graduates will appreciate the wider significance of philosophical ideas for other disciplines and for real-world settings.", rewrite: light, force: will, status: drafted }
  forBeneficiary: { text: "You will understand why philosophical ideas matter beyond philosophy, for other subjects and in real situations.", rewrite: full, force: will, status: drafted }
  author-agent-written: "Present this as an outcome that holders of a master's degree in philosophy will show (will), at FHEQ level 7 (FQHEIS level 11); it comes from the one master's list, held here as that award's threshold. Cite it as QAA (2025), Philosophy Subject Benchmark Statement, para 4.11, item 7. Do not apply it to the honours degree, do not call it regulatory and do not grade it, since the issuer gives no typical or excellent master's rungs. Set it beside the descriptor qaa/fheq-2024/4.17.b3, spine:7 and, for the step up from honours, 4.8.b8.excellent and 4.8.b9.excellent."
  author-agent-dialogue: "Raise it with a master's student or a master's programme team when why their work matters beyond philosophy comes up, for example in dissertation supervision or programme review. Use plain words: the second person for a student, a programme outcome for staff. Ask: Who outside philosophy should care about your research, and why? What would change in practice if your conclusion were accepted? Avoid holding an undergraduate to it, and do not read the list aloud."
- statement: qaa/philosophy-2025/4.11.b8.masters
  forPractitioner: { text: "Master's graduates will write and present at an advanced level, conveying complex ideas effectively to specialist and general audiences.", rewrite: light, force: will, status: drafted }
  forBeneficiary: { text: "You will write and present at an advanced level, getting complex ideas across to experts and non-experts.", rewrite: full, force: will, status: drafted }
  author-agent-written: "Present this as an outcome that holders of a master's degree in philosophy will show (will), at FHEQ level 7 (FQHEIS level 11); it comes from the one master's list, held here as that award's threshold. Cite it as QAA (2025), Philosophy Subject Benchmark Statement, para 4.11, item 8. Do not apply it to the honours degree, do not call it regulatory and do not grade it, since the issuer gives no typical or excellent master's rungs. Set it beside the descriptor qaa/fheq-2024/4.17.b5, spine:7 and, for the step up from honours, 4.8.b5.excellent."
  author-agent-dialogue: "Raise it with a master's student or a master's programme team when writing and presenting comes up, for example in dissertation supervision or programme review. Use plain words: the second person for a student, a programme outcome for staff. Ask: Could you present your research in five minutes to a non-specialist audience? What would you leave out, and what must stay? Avoid holding an undergraduate to it, and do not read the list aloud."
- statement: qaa/philosophy-2025/4.11.b9.masters
  forPractitioner: { text: "Master's graduates will sustain philosophical dialogue, debate and collaborative inquiry.", rewrite: light, force: will, status: drafted }
  forBeneficiary: { text: "You will be able to keep up philosophical discussion, debate and shared inquiry with others over time.", rewrite: full, force: will, status: drafted }
  author-agent-written: "Present this as an outcome that holders of a master's degree in philosophy will show (will), at FHEQ level 7 (FQHEIS level 11); it comes from the one master's list, held here as that award's threshold. Cite it as QAA (2025), Philosophy Subject Benchmark Statement, para 4.11, item 9. Do not apply it to the honours degree, do not call it regulatory and do not grade it, since the issuer gives no typical or excellent master's rungs. Set it beside the descriptor qaa/fheq-2024/4.17.b5, spine:7 and, for the step up from honours, 4.10.b10."
  author-agent-dialogue: "Raise it with a master's student or a master's programme team when seminars and debate comes up, for example in dissertation supervision or programme review. Use plain words: the second person for a student, a programme outcome for staff. Ask: How do you keep a disagreement in a seminar productive? What did you learn from the last debate in which you changed position? Avoid holding an undergraduate to it, and do not read the list aloud."
- statement: qaa/philosophy-2025/4.11.b10.masters
  forPractitioner: { text: "Master's graduates will reflect on the nature of philosophy, its methods and presuppositions and its relation to other inquiry.", rewrite: light, force: will, status: drafted }
  forBeneficiary: { text: "You will understand, reflectively, what philosophy is, how it works, what it assumes and how it relates to other kinds of inquiry.", rewrite: full, force: will, status: drafted }
  author-agent-written: "Present this as an outcome that holders of a master's degree in philosophy will show (will), at FHEQ level 7 (FQHEIS level 11); it comes from the one master's list, held here as that award's threshold. Cite it as QAA (2025), Philosophy Subject Benchmark Statement, para 4.11, item 10. Do not apply it to the honours degree, do not call it regulatory and do not grade it, since the issuer gives no typical or excellent master's rungs. Set it beside the descriptor qaa/fheq-2024/4.17.b4.2, spine:7 and, for the step up from honours, 4.6.b4.excellent."
  author-agent-dialogue: "Raise it with a master's student or a master's programme team when what philosophy is and how it works comes up, for example in dissertation supervision or programme review. Use plain words: the second person for a student, a programme outcome for staff. Ask: What does your own approach to philosophy assume? How is it different from the way another discipline would tackle your question? Avoid holding an undergraduate to it, and do not read the list aloud."
- statement: qaa/philosophy-2025/4.11.b11.masters
  forPractitioner: { text: "Master's graduates will reason ethically and appreciate both the moral dimensions of philosophical problems and philosophy's role in ethical, social and political questions.", rewrite: light, force: will, status: drafted }
  forBeneficiary: { text: "You will reason well about ethics and see the moral side of philosophical problems and how philosophy can help with ethical, social and political issues.", rewrite: full, force: will, status: drafted }
  author-agent-written: "Present this as an outcome that holders of a master's degree in philosophy will show (will), at FHEQ level 7 (FQHEIS level 11); it comes from the one master's list, held here as that award's threshold. Cite it as QAA (2025), Philosophy Subject Benchmark Statement, para 4.11, item 11. Do not apply it to the honours degree, do not call it regulatory and do not grade it, since the issuer gives no typical or excellent master's rungs. Set it beside the descriptor qaa/fheq-2024/4.17.b5, spine:7 and, for the step up from honours, 4.10.b12."
  author-agent-dialogue: "Raise it with a master's student or a master's programme team when ethics and public questions comes up, for example in dissertation supervision or programme review. Use plain words: the second person for a student, a programme outcome for staff. Ask: What moral question does your research raise, even if it is not about ethics? How could philosophy help with a social or political issue you care about? Avoid holding an undergraduate to it, and do not read the list aloud."
- statement: qaa/philosophy-2025/4.11.b12.masters
  forPractitioner: { text: "Master's graduates will learn and research independently, identifying, evaluating and synthesising sources and continuing their philosophical development.", rewrite: light, force: will, status: drafted }
  forBeneficiary: { text: "You will be able to learn and research on your own, finding, assessing and combining sources, and keep growing as a philosopher.", rewrite: full, force: will, status: drafted }
  author-agent-written: "Present this as an outcome that holders of a master's degree in philosophy will show (will), at FHEQ level 7 (FQHEIS level 11); it comes from the one master's list, held here as that award's threshold. Cite it as QAA (2025), Philosophy Subject Benchmark Statement, para 4.11, item 12. Do not apply it to the honours degree, do not call it regulatory and do not grade it, since the issuer gives no typical or excellent master's rungs. Set it beside the descriptor qaa/fheq-2024/4.17.b7 and qaa/fheq-2024/4.17.b8.3, spine:7 and, for the step up from honours, 4.10.b9."
  author-agent-dialogue: "Raise it with a master's student or a master's programme team when learning after the course comes up, for example in dissertation supervision or programme review. Use plain words: the second person for a student, a programme outcome for staff. Ask: How will you keep doing philosophy after the course ends? How do you now find and judge sources without a reading list? Avoid holding an undergraduate to it, and do not read the list aloud."
```

### S5 Levels and alignment
<!-- label: both; status: drafted; basis: primary -->
```yaml
levels:
  - { id: "fheq:4", role: "cites", locator: "D1, 2.2; 2.10" }
  - { id: "fheq:5", role: "cites", locator: "D1, 2.3; 2.10" }
  - { id: "fheq:6", role: "cites", locator: "D1, 2.4; 2.7" }
  - { id: "fheq:7", role: "cites", locator: "D1, 2.7; 2.11" }
  - { id: "fqheis:7", role: "cites", locator: "D1, 2.2" }
  - { id: "fqheis:8", role: "cites", locator: "D1, 2.3; 2.10" }
  - { id: "fqheis:9", role: "cites", locator: "D1, 2.4; 2.7; 2.10" }
  - { id: "fqheis:10", role: "cites", locator: "D1, 2.4; 2.7" }
  - { id: "fqheis:11", role: "cites", locator: "D1, 2.7; 2.11" }
  - { id: "spine:6", role: "inferred: the honours rungs and generic skills", locator: "std:ref:uk-framework R2, R8" }
  - { id: "spine:7", role: "inferred: the master's list", locator: "std:ref:uk-framework R2, R8" }
crosswalks:
  - { from: "fheq:4", to: "fqheis:7", relation: "equivalent", basis: "stated (D1, 2.2: first year); agrees with std:doc:qaa-fheq-2024-framework Table 1" }
  - { from: "fheq:5", to: "fqheis:8", relation: "equivalent", basis: "stated (D1, 2.3: second year); agrees with Table 1" }
  - { from: "fheq:6", to: "fqheis:10", relation: "equivalent", basis: "stated (D1, 2.4; 2.7: \"FQHEIS Levels 9/10\"); Table 1 puts honours at fqheis:10, other bachelor's at fqheis:9" }
  - { from: "fheq:7", to: "fqheis:11", relation: "equivalent", basis: "stated (D1, 2.7; 2.11); shared descriptor qaa/fheq-2024/4.17" }
  - { from: "fheq:4", to: "fqheis:8", relation: "as-stated, conflicting", basis: "stated (D1, 2.10: CertHE); Table 1 gives the CertHE fqheis:7: Part E" }
  - { from: "fheq:5", to: "fqheis:9", relation: "as-stated, conflicting", basis: "stated (D1, 2.10: DipHE); Table 1 gives the DipHE fqheis:8: Part E" }
```

### S6 Themes
<!-- label: both; status: drafted; basis: primary -->
```yaml
- { id: "theme:edi", role: "carries", carriedIn: ["front matter", "1.5", "1.6", "1.7", "1.8", "1.9", "1.10", "1.11", "1.12", "1.31", "3.13"] }
- { id: "theme:accessibility", role: "carries", carriedIn: ["front matter", "1.13", "1.14", "1.15", "1.16", "3.18"] }
- { id: "theme:esd", role: "carries", carriedIn: ["front matter", "1.17", "1.18", "1.19", "2.6"] }
- { id: "theme:enterprise", role: "carries", carriedIn: ["front matter", "1.20", "1.21", "1.22", "1.23", "1.24", "1.25", "1.26", "1.27"] }
- { id: "theme:generative-ai", role: "carries", carriedIn: ["front matter", "1.28", "1.29", "1.30", "1.31", "1.32", "1.33"] }
```

### S7 Relations
<!-- label: both; status: drafted; basis: primary -->
```yaml
- { rel: "partOf", target: "collection: QAA Subject Benchmark Statements", note: "one of 54 held by stan" }
- { rel: "supersedes", target: "std:doc:qaa-philosophy-2019-benchmarks (not held)", note: "the text names only \"the previous Subject Benchmark Statement\"; the 2019 minor update is read from the advisory group lists: Part E" }
- { rel: "refersTo", target: "std:doc:qaa-fheq-2024-framework, Annex D", note: "4.2: providers should refer to it; 4.4 matches the rungs to the 3rd, 2nd and 1st classes" }
- { rel: "refersTo", target: "std:doc:qaa-fheq-2024-framework", note: "levels 4 to 7 (2.2 to 2.4, 2.7, 2.10, 2.11)" }
- { rel: "refersTo", target: "std:doc:qaa-fqheis-2024-framework", note: "levels 7 to 11 as the statement gives them (2.2 to 2.4, 2.7, 2.10, 2.11); 2.10's pairings conflict with the FHEQ's Table 1: Part E" }
- { rel: "refersTo", target: "std:doc:qaa-advancehe-esd-2021-guidance", note: "1.18: to be consulted as a core resource" }
- { rel: "refersTo", target: "QAA Quality Code, 2024 update (not yet ingested)", note: "front matter" }
- { rel: "refersTo", target: "Equality Act 2010 and the Public Sector Equality Duty (law)", note: "1.10, 4.3" }
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
- Concerned with how we make sense of the world, of ourselves and of our relations; seen as underpinning the other disciplines and as sitting where the humanities and the social and natural sciences meet (D1, 1.1).
- Asks the large questions of knowledge, value, existence, morality and social life, with a clarifying role that supports constructive dialogue (D1, 1.2).
- Pluralistic: analytic, continental and comparative traditions, world philosophies among them, with methods from formal and logical analysis to hermeneutics, conceptual engineering and phenomenology; the traditions share precision, clarity and self-reflection (D1, 3.2, 3.4).
- Learned by doing: students practise philosophy rather than only study a body of knowledge, through reading, discussion and presentation, and formal methods through graded exercises (D1, 3.8, 3.10, 3.11).
- Seeks a safe space for controversial and uncomfortable views, voiced with care and met constructively, and a community of enquiry that values every member (D1, 1.7, 1.8, 1.10).
- Acknowledges a past canon dominated by privileged European men and treats diversifying the curriculum as imperative (D1, 1.9).
- Often studied jointly with other subjects, and taught by philosophers inside other disciplines' accredited degrees (D1, 1.22, 2.5, 2.6).

### SB2 Themes in this subject
<!-- label: both; status: drafted; basis: primary -->
```yaml
- theme: theme:edi
  inThisSubject: "named Equity, diversity and inclusion: limited access to the subject before university; varied materials, activities and assessment; a safe but challenging space for controversial views; diversifying a narrow Western canon; the Equality Act 2010 and the Public Sector Equality Duty; outward-looking comparison of traditions; reflective logs (D1, 1.5 to 1.12); assessment variety as an EDI gain from GenAI (D1, 1.31); bringing diverse students together (D1, 3.13)"
  statements: ["qaa/philosophy-2025/1.11"]
- theme: theme:accessibility
  inThisSubject: "named Accessibility and the needs of disabled students: an anticipatory approach after the Disabled Students Commission report (clear expectations, care that asynchronous materials and automated captions do not create new barriers, multiple means of engagement); reasonable adjustments; audio and audiovisual resources; the insight disabled students bring to debate (D1, 1.13 to 1.16); alternative assessments (D1, 3.18)"
  statements: []
- theme: theme:esd
  inThisSubject: "named Education for sustainable development: sustainability defined as a moral attribute of acts, processes and institutions; the UN SDGs and the 2021 Advance HE and QAA guidance; philosophy as critique of the concept and as a resource for exposing false sustainability claims (D1, 1.17 to 1.19); sustainability among the concepts other professions' degrees teach (D1, 2.6)"
  statements: ["qaa/philosophy-2025/1.18"]
- theme: theme:enterprise
  inThisSubject: "named Employability, enterprise and entrepreneurship education: clear thinking, logic and argument as employability skills; joint programmes, placements and years abroad; assessments such as policy briefs; support for social enterprise; leadership strengths; the sectors graduates enter (D1, 1.20 to 1.27)"
  statements: []
- theme: theme:generative-ai
  inThisSubject: "named Generative artificial intelligence: weighed against the degree's principal skills; formative benefits (critiquing outputs, an interlocutor, help for reticent students); risks to reading, analysis and originality; a challenge to essay-based assessment and integrity; GenAI as a philosophical topic in its own right (D1, 1.28 to 1.33)"
  statements: []
```

### SB3 Content and delivery
<!-- label: both; status: drafted; basis: primary -->
```yaml
areas:
  - { component: "3.2", gloss: "traditions (analytic, continental, comparative, world) and methods (formal, logical, textual, conceptual engineering, hermeneutic, phenomenological)" }
  - { component: "3.3", gloss: "general philosophy; philosophy of particular practices such as language, science, law and the arts; collaborative work on questions underlying other disciplines" }
  - { component: "3.6", gloss: "single honours: major philosophers in their own texts; theoretical philosophy; aesthetics, moral, political and social philosophy; contemporary challenges; current research issues" }
  - { component: "3.7", gloss: "joint honours and specialist courses; history, theoretical and practical philosophy; interdisciplinary modules" }
practices:
  - { component: "3.8", kind: "teaching", gloss: "model the practice of philosophy; balance knowledge with discussion and response" }
  - { component: "3.9", kind: "learning", gloss: "student-led research, peer exchange and self-chosen questions" }
  - { component: "3.10", kind: "learning", gloss: "own reading, discussion and presentation with feedback in every module" }
  - { component: "3.11", kind: "learning", gloss: "formal methods learned through graded exercises, with computer-assisted logic" }
  - { component: "3.12", kind: "learning", gloss: "incremental progression from supported to independent study" }
  - { component: "3.13", kind: "teaching", gloss: "two-year cycles; diverse students on shared problems; varied discussion modes" }
  - { component: "3.14", kind: "teaching", gloss: "lectures, tutorials, seminars, self-directed study, guided reading with essays, dissertation, online resources, student-led groups" }
  - { component: "3.15", kind: "assessment", gloss: "the suite tests knowledge and understanding, argument and analysis, presentation" }
  - { component: "3.16", kind: "assessment", gloss: "diverse ways of meeting outcomes" }
  - { component: "3.17", kind: "assessment", gloss: "co-created and reflective assessment; essays to curated events and logic exercises" }
  - { component: "3.18", kind: "assessment", gloss: "accessible alternatives; students propose formats and questions" }
  - { component: "3.19", kind: "assessment", gloss: "integrity through authenticity; transparency with technology; self and peer assessment" }
```

### SB4 Benchmark standards
<!-- label: both; status: drafted; basis: primary -->
```yaml
rungs:
  - { rung: "threshold", leadIn: "4.4", tables: ["4.6", "4.8"], award: "bachelor's with honours", items: 14 }
  - { rung: "typical", leadIn: "4.4", tables: ["4.6", "4.8"], award: "bachelor's with honours", items: 14 }
  - { rung: "excellent", leadIn: "4.4", tables: ["4.6", "4.8"], award: "bachelor's with honours", items: 14 }
  - { rung: "threshold", leadIn: "4.11", tables: [], award: "master's", items: 12, note: "the master's list, recorded as that award's threshold (batch 1 convention); no typical or excellent master's rungs" }
rungBases: "4.4 defines the rungs: threshold the minimum acceptable for an honours graduate, matched to a third; typical what most reach, a second; excellent the best, a first. 4.6 and 4.8 are tables listing each outcome once per row under the three rung columns, so each row's cells are paired by the issuer; 4.7 and 4.9 state that the higher rungs include the lower. 4.5: the rungs are written for single honours."
outcomeLists:
  - { leadIn: "4.10", gloss: "generic skills at undergraduate level, no rungs", items: 12, award: ["bachelor's with honours"] }
  - { leadIn: "4.11", gloss: "outcomes for the master's degree, recorded in rungs as the master's threshold", items: 12, award: ["master's"] }
outcomes:
  - { outcome: "major philosophers and their interpretation", threshold: "qaa/philosophy-2025/4.6.b1", typical: "qaa/philosophy-2025/4.6.b1.typical", excellent: "qaa/philosophy-2025/4.6.b1.excellent", basis: "stated", domain: "knowledge", award: "bachelor's with honours" }
  - { outcome: "theoretical philosophy", threshold: "qaa/philosophy-2025/4.6.b2", typical: "qaa/philosophy-2025/4.6.b2.typical", excellent: "qaa/philosophy-2025/4.6.b2.excellent", basis: "stated", domain: "knowledge", award: "bachelor's with honours" }
  - { outcome: "practical philosophy", threshold: "qaa/philosophy-2025/4.6.b3", typical: "qaa/philosophy-2025/4.6.b3.typical", excellent: "qaa/philosophy-2025/4.6.b3.excellent", basis: "stated", domain: "knowledge", award: "bachelor's with honours" }
  - { outcome: "techniques of reasoning and critiques of method", threshold: "qaa/philosophy-2025/4.6.b4", typical: "qaa/philosophy-2025/4.6.b4.typical", excellent: "qaa/philosophy-2025/4.6.b4.excellent", basis: "stated", domain: "understanding", award: "bachelor's with honours" }
  - { outcome: "current debates in philosophy", threshold: "qaa/philosophy-2025/4.6.b5", typical: "qaa/philosophy-2025/4.6.b5.typical", excellent: "qaa/philosophy-2025/4.6.b5.excellent", basis: "stated", domain: "knowledge", award: "bachelor's with honours" }
  - { outcome: "selecting readings", threshold: "qaa/philosophy-2025/4.8.b1", typical: "qaa/philosophy-2025/4.8.b1.typical", excellent: "qaa/philosophy-2025/4.8.b1.excellent", basis: "stated", domain: "subject-skill", award: "bachelor's with honours" }
  - { outcome: "interpreting texts", threshold: "qaa/philosophy-2025/4.8.b2", typical: "qaa/philosophy-2025/4.8.b2.typical", excellent: "qaa/philosophy-2025/4.8.b2.excellent", basis: "stated", domain: "subject-skill", award: "bachelor's with honours" }
  - { outcome: "terminology", threshold: "qaa/philosophy-2025/4.8.b3", typical: "qaa/philosophy-2025/4.8.b3.typical", excellent: "qaa/philosophy-2025/4.8.b3.excellent", basis: "stated", domain: "subject-skill", award: "bachelor's with honours" }
  - { outcome: "formulating arguments", threshold: "qaa/philosophy-2025/4.8.b4", typical: "qaa/philosophy-2025/4.8.b4.typical", excellent: "qaa/philosophy-2025/4.8.b4.excellent", basis: "stated", domain: "subject-skill", award: "bachelor's with honours" }
  - { outcome: "explaining", threshold: "qaa/philosophy-2025/4.8.b5", typical: "qaa/philosophy-2025/4.8.b5.typical", excellent: "qaa/philosophy-2025/4.8.b5.excellent", basis: "stated", domain: "subject-skill", award: "bachelor's with honours" }
  - { outcome: "originality", threshold: "qaa/philosophy-2025/4.8.b6", typical: "qaa/philosophy-2025/4.8.b6.typical", excellent: "qaa/philosophy-2025/4.8.b6.excellent", basis: "stated", domain: "subject-skill", award: "bachelor's with honours" }
  - { outcome: "open-mindedness", threshold: "qaa/philosophy-2025/4.8.b7", typical: "qaa/philosophy-2025/4.8.b7.typical", excellent: "qaa/philosophy-2025/4.8.b7.excellent", basis: "stated", domain: "subject-skill", award: "bachelor's with honours" }
  - { outcome: "interdisciplinarity", threshold: "qaa/philosophy-2025/4.8.b8", typical: "qaa/philosophy-2025/4.8.b8.typical", excellent: "qaa/philosophy-2025/4.8.b8.excellent", basis: "stated", domain: "subject-skill", award: "bachelor's with honours" }
  - { outcome: "applications", threshold: "qaa/philosophy-2025/4.8.b9", typical: "qaa/philosophy-2025/4.8.b9.typical", excellent: "qaa/philosophy-2025/4.8.b9.excellent", basis: "stated", domain: "subject-skill", award: "bachelor's with honours" }
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
- { body: "Professional, statutory and regulatory bodies (PSRBs), none named for the subject", says: "the statement can support PSRBs' definitions of academic standards (front matter); many accredited degrees in other disciplines require philosophical concepts such as ethics, risk and sustainability (D1, 2.6); courses with professional outcomes may need PSRB accreditation (D1, 2.19); competence standards may draw on PSRB requirements (D1, 4.3)", requirements: "not-applicable: no body is named for philosophy (Part E)" }
- { body: "Office for Students", says: "in England, benchmark statements are not sector-recognised standards under its regulatory framework (D1, front matter)", requirements: "not yet ingested (Part E)" }
- { body: "Equality and Human Rights Commission", says: "providers that write competence standards should follow its most recent guidance (D1, 4.3)", requirements: "not yet ingested (Part E; D3)" }
- { body: "Disabled Students Commission", says: "its Annual Report 2021-22 informs the anticipatory approach to accessibility (D1, 1.13)", requirements: "not-applicable: a report, not requirements (Part E)" }
```

### SB6 Cross-cutting references
<!-- label: both; status: drafted; basis: primary -->
```yaml
themes:
  - { id: "theme:edi", named: "Equity, diversity and inclusion (front matter: equity, diversity, and inclusion)", carriedIn: ["front matter", "1.5", "1.6", "1.7", "1.8", "1.9", "1.10", "1.11", "1.12", "1.31", "3.13"], statements: ["1.11"] }
  - { id: "theme:accessibility", named: "Accessibility and the needs of disabled students", carriedIn: ["front matter", "1.13", "1.14", "1.15", "1.16", "3.18"], statements: [] }
  - { id: "theme:esd", named: "Education for sustainable development", carriedIn: ["front matter", "1.17", "1.18", "1.19", "2.6"], statements: ["1.18"] }
  - { id: "theme:enterprise", named: "Employability, enterprise and entrepreneurship education (front matter: employability, entrepreneurship and enterprise education)", carriedIn: ["front matter", "1.20", "1.21", "1.22", "1.23", "1.24", "1.25", "1.26", "1.27"], statements: [] }
  - { id: "theme:generative-ai", named: "Generative artificial intelligence (GenAI)", carriedIn: ["front matter", "1.28", "1.29", "1.30", "1.31", "1.32", "1.33"], statements: [] }
frameworks:
  - { framework: "fheq", levels: ["fheq:4", "fheq:5", "fheq:6", "fheq:7"], citedIn: ["2.2", "2.3", "2.4", "2.7", "2.10", "2.11", "4.2"] }
  - { framework: "scqf", levels: ["fqheis:7", "fqheis:8", "fqheis:9", "fqheis:10", "fqheis:11"], citedIn: ["2.2", "2.3", "2.4", "2.7", "2.10", "2.11"] }
bodies:
  - { body: "PSRBs (unnamed)", citedIn: ["front matter", "2.6", "2.19", "4.3"] }
  - { body: "Office for Students", citedIn: ["front matter"] }
  - { body: "Equality and Human Rights Commission", citedIn: ["4.3"] }
  - { body: "Disabled Students Commission", citedIn: ["1.13"] }
  - { body: "Advance HE (co-author of the ESD guidance)", citedIn: ["1.18"] }
sharedDocuments:
  - { document: "std:doc:qaa-fheq-2024-framework, Annex D", named: "Annex D of the Frameworks for Higher Education Qualifications of UK Degree-Awarding Bodies", citedIn: ["4.2"], role: "descriptions of the four honours classes (1st, 2.1, 2.2, 3rd), for evidence of achievement above threshold; 4.4 matches the rungs to them" }
  - { document: "std:doc:qaa-advancehe-esd-2021-guidance", named: "Education for Sustainable Development Guidance produced by Advance HE and QAA (March 2021)", citedIn: ["1.18"], role: "a core resource for the sustainability theme" }
  - { document: "QAA Quality Code, 2024 update (not yet ingested: Part E)", named: "the Quality Code", citedIn: ["front matter"], role: "a further reference point" }
  - { document: "QAA Glossary (not ingested)", named: "QAA's Glossary", citedIn: ["front matter"], role: "explains unfamiliar terms" }
  - { document: "UN Sustainable Development Goals (external)", named: "UN Sustainable Development Goals (SDGs)", citedIn: ["1.18"], role: "the priorities the sustainability theme follows" }
  - { document: "Equality Act 2010 (law)", named: "Equality Act 2010", citedIn: ["1.10", "4.3"], role: "prohibitions guiding inclusive teaching; the definition of competence standards" }
  - { document: "Public Sector Equality Duty (law)", named: "Public Sector Equality Duty", citedIn: ["1.10"], role: "fostering good relations between students" }
  - { document: "Disabled Students Commission Annual Report 2021-22 (external)", named: "Disabled Students Commission Annual Report 2021-22", citedIn: ["1.13"], role: "grounds the anticipatory approach to accessibility" }
  - { document: "EHRC guidance on competence standards (not identified: D3)", named: "the most recent guidance from the Equality and Human Rights Commission", citedIn: ["4.3"], role: "what providers follow when writing competence standards" }
```

## Part B Terminology
<!-- The statement has no glossary of its own unless Part E says so; these are terms it defines in its text. -->

### B1 Concepts
<!-- label: both; status: drafted; basis: primary -->
```yaml
- { slug: "threshold-standard", definition: "the lowest standard acceptable for an honours graduate in the subject, matched to a third-class degree (D1, 4.4)", beneficiaryDefinition: "the least you need to show to gain an honours degree", scopeNote: "the first column of 4.6 and 4.8", category: "unknown", practices: ["education"] }
- { slug: "typical-standard", definition: "the standard most honours graduates reach, matched to a second-class degree (D1, 4.4)", beneficiaryDefinition: "what most students show by the end of the degree", scopeNote: "the second column of 4.6 and 4.8", category: "unknown", practices: ["education"] }
- { slug: "excellent-standard", definition: "the standard of the strongest honours graduates, matched to a first-class degree (D1, 4.4)", beneficiaryDefinition: "what the strongest students show", scopeNote: "the third column of 4.6 and 4.8", category: "unknown", practices: ["education"] }
- { slug: "sustainability", definition: "a quality, worthy of moral praise, of acts, processes or institutions that achieve their ends without harming the prospects of living things (D1, 1.17)", scopeNote: "the sense the statement uses for its ESD theme", category: "unknown", practices: ["education"] }
- { slug: "generative-artificial-intelligence", definition: "AI that generates text or images, abbreviated GenAI; more than a tool, since it changes its users and their relation to ideas (D1, 1.28, 1.31, 1.33)", category: "unknown", practices: ["education"] }
- { slug: "psrb", definition: "professional, statutory and regulatory bodies (D1, front matter)", category: "unknown", practices: ["education"] }
- { slug: "competence-standard", definition: "a standard in the sense of the Equality Act 2010; the rungs are not meant as universal ones (D1, 4.3)", category: "unknown", practices: ["education"] }
```

### B2a Terms as the issuer defines them
<!-- label: source; status: drafted; basis: primary -->
```yaml
- { concept: "threshold-standard", form: "Threshold", lang: "en", partOfSpeech: "noun", termStatus: "preferred", register: "formal" }
- { concept: "threshold-standard", form: "minimum threshold", lang: "en", partOfSpeech: "noun-phrase", termStatus: "admitted", register: "formal" }
- { concept: "typical-standard", form: "Typical", lang: "en", partOfSpeech: "noun", termStatus: "preferred", register: "formal" }
- { concept: "excellent-standard", form: "Excellent", lang: "en", partOfSpeech: "noun", termStatus: "preferred", register: "formal" }
- { concept: "sustainability", form: "sustainability", lang: "en", partOfSpeech: "noun", termStatus: "preferred", register: "formal" }
- { concept: "generative-artificial-intelligence", form: "generative artificial intelligence", lang: "en", partOfSpeech: "noun-phrase", termStatus: "preferred", register: "formal" }
- { concept: "generative-artificial-intelligence", form: "GenAI", lang: "en", partOfSpeech: "noun", termStatus: "admitted", register: "formal" }
- { concept: "psrb", form: "PSRBs", lang: "en", partOfSpeech: "noun", termStatus: "preferred", register: "formal" }
- { concept: "competence-standard", form: "competence standards", lang: "en", partOfSpeech: "noun-phrase", termStatus: "preferred", register: "formal" }
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
  title: "Subject Benchmark Statement Philosophy"
  edition: "April 2025"
  year: 2025
  url: unknown (the QAA page; the text came by stan's extraction)
  retrieved: "held from stan: wkspc2615-QAAVector mapped/philosophy-2025/philosophy-2025.raw.txt, commit 366bcb99a01118f2c4c3ebfa2a8337596bddc455; received 2026-10-03"
  licence: QAA copyright
  tier: primary
  readVia: direct
  held: 08aa2558e79693d680e19c26a51391ac58b6e1925c502159fe8265b42ad7ad86
  heldFiles: ["wkspc2601-library/txt/qaa-2025-philosophy-subject-benchmark-statement-standard.txt", "wkspc2601-library/txt/qaa-2025-philosophy-subject-benchmark-statement-standard.norm.txt", "wkspc2601-library/records/qaa-2025-philosophy-subject-benchmark-statement-standard.chunks.json", "wkspc2601-library/records/qaa-2025-philosophy-subject-benchmark-statement-standard.held.json"]
  citedIn: [S1, S2, S3, S4, S4a, S5, S6, S7, SB1, SB2, SB3, SB4, SB5, SB6]
```

### D2 Research log
```yaml
- { ref: D1, tier: primary, consulted: 2026-10-03, pass: P1, outcome: "read whole, direct, from the normalised text; skeleton by tools/std_prep.py, document by tools/bm_build.py" }
- { ref: "ADAPT subj HESA stores, cah.json and hecos.json (designs/ingest/standards/subj/vocab)", tier: primary, consulted: 2026-10-03, pass: P1, outcome: "codes for statedSubjects and subjects" }
```

### D3 Wanted sources
```yaml
- { w: "W-std-0083", citation: "Equality and Human Rights Commission, the most recent guidance on competence standards (named in 4.3, not identified)", settles: ["SB5", "SB6"], asked: "2026-10-03", state: "wanted" }
- { w: "W-std-0052", citation: "QAA (2024) the Quality Code, the update named in the front matter", settles: ["SB6", "S7"], asked: "2026-10-03", state: "wanted" }
```

## Part E Gaps and questions
- SB4, rung shape: two tables (4.6 knowledge and understanding, five rows; 4.8 subject-specific and intellectual skills, nine rows), each row given once under three column heads, Threshold (3rd), Typical (2nd), Excellent (1st); recorded one S4 record per rung on each cell's span (batch 1 convention). The rungs are defined once, in 4.4, not by lead-ins above lists: a new shape against Psychology.
- SB4, gradeOf: every typical and excellent cell links to the cell to its left in the same row, basis stated (the issuer pairs the cells by row; 4.7 and 4.9 add that the higher rungs include the lower). No inferred link.
- SB4, flattened tables: 4.6 and 4.8 are flattened in the held text, cells running row by row, threshold, typical, excellent. Placements read with some doubt, for P3: 4.6 row 1 (the threshold cell 'The writings of some major philosophers.' runs straight into the typical cell); 4.8 row 5, Explaining (the excellent cell 'Tailor explanations...' sits after a paragraph break); 4.8 rows 7 and 8 (cells broken across lines). 4.6 rows carry no labels: the row names in SB4 are ours.
- SB4, force: threshold cells take force `threshold` with forceFrom 4.4, where the issuer defines the threshold as the minimum for the award; typical and excellent cells take 'will' from the table lead-ins in 4.6 and 4.8 (forceFrom gives the lead-in text).
- SB4, the master's list (4.11) is an outcome list for another award, recorded as rung threshold, award master's, level fheq:7, id suffix .masters (batch 1 convention). The issuer gives no master's rungs, though 4.3 speaks of threshold, typical and excellent standards 'for undergraduate and master's level'.
- SB4, 4.10 generic skills: an outcome list at undergraduate level with no rung lead-in; recorded rung none, level fheq:6. 2.7 calls the generic skills 'threshold-level': for P3, whether they should carry rung threshold.
- S3, std-prep: the skeleton read 4.4's three definition bullets as threshold items because the bullets name the rungs; they define the rungs and are not statements. The skeleton found no typical or excellent items (the tables are flattened).
- S3, std-prep: the skeleton's component spans end with the next sub-heading (for example 1.1 ends 'Purposes and characteristics'; 1.4 ends 'Equity, diversity and inclusion Enabling potential'); the cut is the issuer's numbering and is kept; headings are in SUB.
- S4, not taken as statements (descriptive, for P3): 1.2 ('students will ask, and attempt to answer'); 1.3 (fourteen benefits of study, 'provides ... the ability to', plain present); 1.4 (ten social purposes); 1.26 (graduates 'are ready' for leadership, plain present); 2.11 (master's students 'will complete' modules: curricular); 2.16 ('will form part' of review); 4.1 (the standards 'a student will have demonstrated': framing for the tables); 4.7 and 4.9 (rung inclusion, recorded in rungBases).
- S4, plain-present provider norms (template open point 5), not statements: 1.6, 1.7, 1.10, 1.13 (three anticipatory practices), 1.14, 1.15, 3.3, 3.6, 3.10, 3.12, 3.14, 3.17, 3.18.
- S4, obliging words outside the five: 'it is expected that' (2.7, 2.8, 2.12) and 'expected to' (4.5); 'it is important that' (3.8, 3.13); 'is imperative' (1.9); 'is encouraged' (1.12). 4.5 is taken as a statement with force describes; the others are not statements, or their force sits beside a stated must, should or will. For Abbott: should 'expected to' read as should?
- S4, 3.19: 'transparency must be ensured' is passive and names no duty-holder; recorded as a provider duty (addressee provider). For P3: whether students share it.
- S4, 3.15: the stem's 'will test for' gives three provider records (3.15.b1 to b3); the stem's first sentence ('will balance the need to test...') is folded into 3.15.b1's paraphrase.
- S4, 1.11 and 1.18: one sentence in each paragraph obliges (should); the record's span is the whole numbered paragraph, as the issuer numbers it.
- S5, crosswalks: 2.10 pairs the CertHE with FQHEIS Level 8 and the DipHE with FQHEIS Level 9; the FHEQ's Table 1 (std:doc:qaa-fheq-2024-framework, S5) gives FQHEIS 7 and 8. Recorded as stated and conflicting; likely an issuer error. 2.4 and 2.7 give honours as 'FQHEIS Levels 9/10'; Table 1 puts honours at 10 and other bachelor's at 9.
- S5, levels: spine:6 and spine:7 are inferred from the reference framework (std:ref:uk-framework R2), not stated. CQFW is not cited by the statement.
- S2 and front matter, codes: HECoS 100791 'mental philosophy' entered for 'philosophy of mind' as inferred; no HECoS term for logic, aesthetics or political philosophy. Liberal arts (100065) is in statedSubjects only, as a programme the subject may be part of.
- S1, S8: 'Fifth edition Published - 10 April 2025' with copyright 2024; published recorded as 2025-04. The previous statement is named only as 'the previous Subject Benchmark Statement'; the advisory group lists name a 2019 minor update and 2015, 2007 and 2000 editions (recall-free: read from the back matter).
- S1, licence: the text gives a copyright notice and no re-use terms.
- SB5: no professional body accredits philosophy; PSRBs appear only in general. The Office for Students, the EHRC and the Disabled Students Commission are named; their requirements are not ingested. Advance HE is named only as co-author of the ESD guidance (SB6).
- SB6, themes: the statement names five cross-cutting themes, generative AI the fifth (theme:generative-ai, batch 1 convention). EDI is named 'Equity', not 'Equality'. 1.4 (diverse cultures) and 1.33.b3 (diversity in assessment) touch EDI without naming it and are not tagged.
- SB6, back matter: the references list (excluded matter) names the BPA and SWIP report on women in philosophy, the Diversity Reading List, QAA's advice on inclusive subject learning communities and the SOAS decolonising philosophy toolkit; not ingested.
- S9: not researched in P1.
- Patterns against Psychology: rung tables, not lists; rungs defined in 4.4 with class equivalents; a master's list as the last subsection; generic skills as a separate list at undergraduate level; a fifth theme (generative AI); no PSRB; rungs written for single honours only (4.5).
- ST-12: versions here run to the lengths the content needs; no length range is yet set.

---

## Change notes
- 0.1.2, 3 October 2026, 21:02: moved with its held text from UNI to the source library repo (`wkspc2601-library/ingested/standards/`, texts in `txt/`, records in `records/`); paths only (Abbott, 20:56; std N-0119).
- 0.1.1, 3 October 2026, 20:20: obliging words outside the five read as must, "ought to" as should, on statements outside the rungs, each marked on its force line (Abbott, 20:17; D-std-0016).
- 0.1.0, 2026-10-03 18:26: researched by run frame 0.1.1-draft and standards run layer 0.7.0-draft, std, run 0124 (P1); built by tools/bm_build.py.
