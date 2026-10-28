---
id: std:doc:qaa-creative-writing-2024-benchmarks
title: "Subject Benchmark Statement Creative Writing"
profile: standards/subject-benchmark
profileVersion: 0.2.0-draft
issuer: QAA
kind: subject-benchmark
jurisdiction: [UK]
subjectScope: subjects
subjects:
  - { scheme: "hecos", code: "100046", label: "creative writing", basis: "stated" }
  - { scheme: "cah", code: "CAH19-01-05", label: "creative writing", basis: "stated" }
  - { scheme: "cah", code: "CAH19-01", label: "English studies", basis: "inferred" }
edition: "April 2024 (third edition)"
published: 2024-04
status: current
supersedes: "Subject Benchmark Statement for Creative Writing, second edition (2019), as section 6 names it"
heldText: { method: sha256-bytes, raw: 78b6f29fa59e46757a2316de6e1561bf33038430fa3952d40e498deb76d3cc89, normalised: c646b21ab7789d549f9bded88e0ba0583a045341248998c83cb18d75f0e8bfd5 }
heldTextStan: { method: sha256-stan, raw: 78b6f29fa59e46757a2316de6e1561bf33038430fa3952d40e498deb76d3cc89, normalised: 33de05d8b56e150629fead1fed5775cdda5751a01bf0f4bbec3d257e014f12f7 }
licence: "QAA copyright; held for study, private to the project, never published"
series: "QAA Subject Benchmark Statements, 2024 revision with the cross-cutting themes (third edition of this statement)"
awardsCovered: ["bachelor's with honours", "master's"]
levelsCovered: ["fheq:6", "fqheis:10", "fheq:7", "fqheis:11"]
nations: ["England", "Wales", "Scotland", "Northern Ireland"]
parts:
  S: full
  B: "partial: no glossary in the document (it points to QAA's Glossary); terms it defines in passing"
  C: "not-applicable: the document sets expectations, not a procedure"
pins: { structure: 0.13.0-draft, template: 0.8.0-draft, benchmarkTemplate: 0.6.0-draft, runFrame: 0.1.1-draft, runLayer: 0.7.0-draft, standards: none yet, terminology: none yet }
lifecycle: drafted
researchedBy: run frame 0.1.1-draft; standards run layer 0.7.0-draft; std, run 0097 (tools/bm_build.py)
passes:
  P1: "2026-10-03 16:53"
  P2: "skipped: read direct from the held text; inferred codes and rung links are for P3"
  P3: open
version: 0.1.2
---

<!-- from INGEST wpk-0016-ingest-pd-template-standards.md 0.8.0-draft and wpk-0016-ingest-pd-template-standards-benchmark.md 0.6.0-draft; built by tools/bm_build.py from run-src/ -->
# Subject Benchmark Statement: Creative Writing (QAA, April 2024)

> Run 0097, P1 by std. The issuer's words are held in the source library, `wkspc2601-library/txt/qaa-2024-creative-writing-subject-benchmark-statement-standard.norm.txt`; each S4 record carries its statement in full (`source`) for language analysis, with its span. Paraphrases and versions are ours. Private to the project, never published. In front matter `status` is the issuer's; ours is `lifecycle`. Doubts are in Part E.

## Part 0 Summary

### 0.1 Agent definition
<!-- label: editorial; status: drafted; basis: primary -->
QAA's UK reference point for what an honours graduate in Creative Writing knows, understands and can do, with a further list for master's study. Its standards are three rung lists (threshold, typical, excellent), a list of generic skills and a master's list, beside an outcome list in section 2. Reach for it when designing, reviewing or describing a Creative Writing course, its modules or its outcomes. It is not a curriculum and not a regulatory requirement in England.

### 0.2 Summary
<!-- label: both; status: drafted; basis: primary -->
Published by QAA in April 2024 as the third edition, the statement sets out the purposes and characteristics of a Creative Writing degree, its distinctive features (design, progression, flexibility, partnerships, review) and its content, teaching and assessment. Its benchmark standards for the bachelor's degree with honours are 13 threshold items, 19 typical items and an excellent rung of a lead paragraph and 9 items, of which graduates show some. Beside them stand 18 generic skills that graduates should have and 16 outcomes for master's level. It carries the four cross-cutting themes (equality, diversity and inclusion; accessibility; sustainability; enterprise and entrepreneurship education) and treats artificial intelligence in content and assessment. It cites FHEQ Levels 6 and 7 with FQHEIS Levels 10 and 11, and Annex D for the honours classifications; it names UNESCO's ESD competencies and the Equality Act 2010, but no professional body for the subject.

## Part S Standard

### S1 Identity
<!-- label: source; status: drafted; basis: primary -->
```yaml
issuer: The Quality Assurance Agency for Higher Education
title: "Subject Benchmark Statement Creative Writing"
edition: "April 2024 (third edition)"
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
governs: "what can be expected of a Creative Writing graduate at the end of an honours degree, what master's study adds and what courses in the subject provide"
appliesTo:
  awards: ["bachelor's with honours", "master's"]
  levels: ["fheq:6", "fqheis:10", "fheq:7", "fqheis:11"]
  providers: ["UK higher education providers"]
whoMustUse: "none-stated; it is a reference point, not a requirement (D1, front matter)"
howUsed: ["design", "approval", "review", "other: external examining; PSRBs; information for prospective students and employers"]
doesNot: "it is not a national curriculum and does not prescribe teaching, learning or assessment; it carries no statutory or regulatory requirement (D1, front matter)"
beneficiary: the student
statedScope: "\"This document is a QAA Subject Benchmark Statement for Creative Writing that defines what can be expected of a graduate in the subject, in terms of what they might know, do and understand at the end of their studies.\" (D1, front matter)"
statedSubjects:
  - { name: "Creative Writing", locator: "(D1, front matter; 1.1)", kind: "subject", codes: [{ scheme: "hecos", code: "100046", label: "creative writing" }, { scheme: "cah", code: "CAH19-01-05", label: "creative writing" }] }
  - { name: "combined, joint and major-minor degrees with Creative Writing", locator: "(D1, 2.7; 3.2; 3.3)", kind: "programme title", codes: [] }
  - { name: "integrated master's and master's level Creative Writing degrees", locator: "(D1, 2.10; 3.33; 4.7)", kind: "programme title", codes: [{ scheme: "hecos", code: "100046", label: "creative writing" }] }
subjects: see front matter (subjectScope subjects)
```

### S3 Structure
<!-- label: both; status: drafted; basis: primary -->
```yaml
components:
  - { number: "1.1", order: 3, componentType: paragraph, parent: "section 1", heading: "Context and purposes of a Creative Writing degree", gloss: "imagination and language; the creative industries and careers" }
  - { number: "1.2", order: 4, componentType: paragraph, parent: "section 1", heading: "Context and purposes of a Creative Writing degree", gloss: "interdisciplinary; own practice; workshops; independence" }
  - { number: "1.3", order: 5, componentType: paragraph, parent: "section 1", heading: "Context and purposes of a Creative Writing degree", gloss: "subject skills and transferable skills; traditions drawn on" }
  - { number: "1.4", order: 6, componentType: paragraph, parent: "section 1", heading: "Context and purposes of a Creative Writing degree", gloss: "communication, literacy and oracy; peer feedback" }
  - { number: "1.5", order: 7, componentType: paragraph, parent: "section 1", heading: "Context and purposes of a Creative Writing degree", gloss: "research culture; creative writing as research" }
  - { number: "1.6", order: 8, componentType: paragraph, parent: "section 1", heading: "Context and purposes of a Creative Writing degree", gloss: "research-informed teaching; who teaches the subject" }
  - { number: "1.7", order: 9, componentType: stem, parent: "section 1", heading: "Context and purposes of a Creative Writing degree", gloss: "skills students gain; then the subject's purposes in higher education (a list of aims)" }
  - { number: "1.8", order: 10, componentType: paragraph, parent: "section 1", heading: "Purposes and characteristics of a Creative Writing degree: Characteristics of Creative Writing in higher education", gloss: "an artistic and critical discipline across media" }
  - { number: "1.9", order: 11, componentType: paragraph, parent: "section 1", heading: "Purposes and characteristics of a Creative Writing degree: Characteristics of Creative Writing in higher education", gloss: "ideas and originality as the focus" }
  - { number: "1.10", order: 12, componentType: stem, parent: "section 1", heading: "Purposes and characteristics of a Creative Writing degree: Characteristics of Creative Writing in higher education", gloss: "what originality means in the subject (with a list)" }
  - { number: "1.11", order: 13, componentType: paragraph, parent: "section 1", heading: "Purposes and characteristics of a Creative Writing degree: Characteristics of Creative Writing in higher education", gloss: "research skills and reading" }
  - { number: "1.12", order: 14, componentType: area, parent: "section 1", heading: "Purposes and characteristics of a Creative Writing degree: Characteristics of Creative Writing in higher education", gloss: "what reading covers, from games to criticism" }
  - { number: "1.13", order: 15, componentType: paragraph, parent: "section 1", heading: "Purposes and characteristics of a Creative Writing degree: Characteristics of Creative Writing in higher education", gloss: "creative-critical projects; diverse texts; theory" }
  - { number: "1.14", order: 16, componentType: paragraph, parent: "section 1", heading: "Purposes and characteristics of a Creative Writing degree: Characteristics of Creative Writing in higher education", gloss: "literary and media analysis; editing skills" }
  - { number: "1.15", order: 17, componentType: paragraph, parent: "section 1", heading: "Purposes and characteristics of a Creative Writing degree: Characteristics of Creative Writing in higher education", gloss: "professional, entrepreneurial and social skills" }
  - { number: "1.16", order: 18, componentType: paragraph, parent: "section 1", heading: "Purposes and characteristics of a Creative Writing degree: Characteristics of Creative Writing in higher education", gloss: "graduate destinations; creative entrepreneurs" }
  - { number: "1.17", order: 19, componentType: paragraph, parent: "section 1", heading: "Purposes and characteristics of a Creative Writing degree: Characteristics of Creative Writing in higher education", gloss: "kinds of degree" }
  - { number: "1.18", order: 20, componentType: paragraph, parent: "section 1", heading: "Purposes and characteristics of a Creative Writing degree: Characteristics of Creative Writing in higher education", gloss: "partnered with other disciplines" }
  - { number: "1.19", order: 21, componentType: paragraph, parent: "section 1", heading: "Purposes and characteristics of a Creative Writing degree: Characteristics of Creative Writing in higher education", gloss: "individual or collaborative assessment" }
  - { number: "1.20", order: 22, componentType: paragraph, parent: "section 1", heading: "Purposes and characteristics of a Creative Writing degree: Characteristics of Creative Writing in higher education", gloss: "peer feedback and encouraging students to use it" }
  - { number: "1.21", order: 23, componentType: paragraph, parent: "section 1", heading: "Equality, diversity and inclusion", gloss: "inclusive learning communities; the Equality Act 2010" }
  - { number: "1.22", order: 24, componentType: paragraph, parent: "section 1", heading: "Equality, diversity and inclusion", gloss: "inclusive curricula and reading lists" }
  - { number: "1.23", order: 25, componentType: paragraph, parent: "section 1", heading: "Equality, diversity and inclusion", gloss: "belonging and critical dialogue" }
  - { number: "1.24", order: 26, componentType: paragraph, parent: "section 1", heading: "Equality, diversity and inclusion", gloss: "participation plans in the four nations; student support" }
  - { number: "1.25", order: 27, componentType: paragraph, parent: "section 1", heading: "Equality, diversity and inclusion", gloss: "external agencies for equality and diversity" }
  - { number: "1.26", order: 28, componentType: paragraph, parent: "section 1", heading: "Equality, diversity and inclusion", gloss: "inclusive responses through content and pedagogy" }
  - { number: "1.27", order: 29, componentType: paragraph, parent: "section 1", heading: "Accessibility", gloss: "routes of entry; adult returners" }
  - { number: "1.28", order: 30, componentType: paragraph, parent: "section 1", heading: "Accessibility", gloss: "open to all; disclosure and adjustments" }
  - { number: "1.29", order: 31, componentType: paragraph, parent: "section 1", heading: "Accessibility", gloss: "entry by portfolio or presentation" }
  - { number: "1.30", order: 32, componentType: stem, parent: "section 1", heading: "Accessibility", gloss: "accessible materials, spaces and placements (a list of aims)" }
  - { number: "1.31", order: 33, componentType: paragraph, parent: "section 1", heading: "Accessibility", gloss: "workshops and accessibility; preparation required" }
  - { number: "1.32", order: 34, componentType: paragraph, parent: "section 1", heading: "Accessibility", gloss: "learning support plans; adaptable approach" }
  - { number: "1.33", order: 35, componentType: paragraph, parent: "section 1", heading: "Sustainability", gloss: "education for sustainable development; UNESCO" }
  - { number: "1.34", order: 36, componentType: paragraph, parent: "section 1", heading: "Sustainability", gloss: "human and non-human; UNESCO key competencies" }
  - { number: "1.35", order: 37, componentType: paragraph, parent: "section 1", heading: "Sustainability", gloss: "nature and environmental writing" }
  - { number: "1.36", order: 38, componentType: paragraph, parent: "section 1", heading: "Sustainability", gloss: "research and ecological responsibility" }
  - { number: "1.37", order: 39, componentType: paragraph, parent: "section 1", heading: "Sustainability", gloss: "environmental publishing and the more than human" }
  - { number: "1.38", order: 40, componentType: paragraph, parent: "section 1", heading: "Sustainability", gloss: "global interdependence; imagining sustainable futures" }
  - { number: "1.39", order: 41, componentType: paragraph, parent: "section 1", heading: "Enterprise and entrepreneurship education", gloss: "enterprise education and careers" }
  - { number: "1.40", order: 42, componentType: paragraph, parent: "section 1", heading: "Enterprise and entrepreneurship education", gloss: "a self-determined professional life" }
  - { number: "1.41", order: 43, componentType: stem, parent: "section 1", heading: "Enterprise and entrepreneurship education", gloss: "skills the subject builds for enterprise (a list)" }
  - { number: "2.1", order: 45, componentType: stem, parent: "section 2", heading: "Design", gloss: "what characterises course design (a list)" }
  - { number: "2.2", order: 46, componentType: stem, parent: "section 2", heading: "Design", gloss: "what students will do through study (an outcome list)" }
  - { number: "2.3", order: 47, componentType: paragraph, parent: "section 2", heading: "Progression", gloss: "progression across levels towards the threshold" }
  - { number: "2.4", order: 48, componentType: paragraph, parent: "section 2", heading: "Progression", gloss: "year one: workshop practice and reflection" }
  - { number: "2.5", order: 49, componentType: paragraph, parent: "section 2", heading: "Progression", gloss: "year two: wider research and practice" }
  - { number: "2.6", order: 50, componentType: paragraph, parent: "section 2", heading: "Progression", gloss: "final year: major project and employability" }
  - { number: "2.7", order: 51, componentType: paragraph, parent: "section 2", heading: "Progression", gloss: "joint and combined degrees" }
  - { number: "2.8", order: 52, componentType: paragraph, parent: "section 2", heading: "Progression", gloss: "exit awards; course length in the four nations" }
  - { number: "2.9", order: 53, componentType: paragraph, parent: "section 2", heading: "Progression", gloss: "postgraduate study after a second-class degree" }
  - { number: "2.10", order: 54, componentType: paragraph, parent: "section 2", heading: "Progression", gloss: "integrated master's degrees" }
  - { number: "2.11", order: 55, componentType: paragraph, parent: "section 2", heading: "Flexibility", gloss: "modes of study and micro-credentials" }
  - { number: "2.12", order: 56, componentType: paragraph, parent: "section 2", heading: "Partnerships", gloss: "students, industries and presses as partners" }
  - { number: "2.13", order: 57, componentType: stem, parent: "section 2", heading: "Partnerships", gloss: "work placements (a list of opportunities)" }
  - { number: "2.14", order: 58, componentType: paragraph, parent: "section 2", heading: "Monitoring and review", gloss: "monitoring and periodic review" }
  - { number: "2.15", order: 59, componentType: paragraph, parent: "section 2", heading: "Monitoring and review", gloss: "externality in quality assurance" }
  - { number: "2.16", order: 60, componentType: paragraph, parent: "section 2", heading: "Monitoring and review", gloss: "external examiners and threshold standards" }
  - { number: "3.1", order: 62, componentType: area, parent: "section 3", heading: "Content", gloss: "making texts at the centre; varied design" }
  - { number: "3.2", order: 63, componentType: paragraph, parent: "section 3", heading: "Content", gloss: "single honours and combinations" }
  - { number: "3.3", order: 64, componentType: paragraph, parent: "section 3", heading: "Content", gloss: "a minor beside subjects outside the arts" }
  - { number: "3.4", order: 65, componentType: paragraph, parent: "section 3", heading: "Content", gloss: "an outline of typical structure" }
  - { number: "3.5", order: 66, componentType: area, parent: "section 3", heading: "Content", gloss: "Level 4 content (a list)" }
  - { number: "3.6", order: 67, componentType: area, parent: "section 3", heading: "Content", gloss: "Level 5 content (a list)" }
  - { number: "3.7", order: 68, componentType: area, parent: "section 3", heading: "Content", gloss: "Level 6 content (a list)" }
  - { number: "3.8", order: 69, componentType: area, parent: "section 3", heading: "Content", gloss: "community of practice and belonging" }
  - { number: "3.9", order: 70, componentType: area, parent: "section 3", heading: "Content", gloss: "changing content: digital forms and AI" }
  - { number: "3.10", order: 71, componentType: practice, parent: "section 3", heading: "Teaching and learning", gloss: "teaching strategies; risk and failure" }
  - { number: "3.11", order: 72, componentType: paragraph, parent: "section 3", heading: "Teaching and learning", gloss: "staff research and visiting practitioners" }
  - { number: "3.12", order: 73, componentType: practice, parent: "section 3", heading: "Teaching and learning", gloss: "preparing for class" }
  - { number: "3.13", order: 74, componentType: practice, parent: "section 3", heading: "Teaching and learning", gloss: "learning environments, on and off campus" }
  - { number: "3.14", order: 75, componentType: practice, parent: "section 3", heading: "Teaching and learning", gloss: "scheduled activities; online learning" }
  - { number: "3.15", order: 76, componentType: paragraph, parent: "section 3", heading: "Teaching and learning", gloss: "skills in action; small-group teaching" }
  - { number: "3.16", order: 77, componentType: practice, parent: "section 3", heading: "Teaching and learning", gloss: "collaborative and independent study" }
  - { number: "3.17", order: 78, componentType: practice, parent: "section 3", heading: "Teaching and learning", gloss: "presenting work; steps for accessible workshops (a list)" }
  - { number: "3.18", order: 79, componentType: practice, parent: "section 3", heading: "Teaching and learning", gloss: "writing about personal and difficult themes (a list of supports)" }
  - { number: "3.19", order: 80, componentType: paragraph, parent: "section 3", heading: "Teaching and learning", gloss: "tailored support for chosen specialisms" }
  - { number: "3.20", order: 81, componentType: paragraph, parent: "section 3", heading: "Teaching and learning", gloss: "generative AI in practice and analysis" }
  - { number: "3.21", order: 82, componentType: practice, parent: "section 3", heading: "Teaching and learning", gloss: "portfolio, dissertation or capstone project" }
  - { number: "3.22", order: 83, componentType: paragraph, parent: "section 3", heading: "Assessment", gloss: "formative and summative assessment; accessible assessment" }
  - { number: "3.23", order: 84, componentType: practice, parent: "section 3", heading: "Formative assessment", gloss: "formative assessment in workshops" }
  - { number: "3.24", order: 85, componentType: practice, parent: "section 3", heading: "Formative assessment", gloss: "written feedback; self-critique" }
  - { number: "3.25", order: 86, componentType: paragraph, parent: "section 3", heading: "Summative assessment", gloss: "summative assessment and stated outcomes" }
  - { number: "3.26", order: 87, componentType: practice, parent: "section 3", heading: "Summative assessment", gloss: "forms of submission (a list)" }
  - { number: "3.27", order: 88, componentType: practice, parent: "section 3", heading: "Summative assessment", gloss: "student-devised assignments" }
  - { number: "3.28", order: 89, componentType: practice, parent: "section 3", heading: "Assessment criteria", gloss: "clear, visible assessment criteria" }
  - { number: "3.29", order: 90, componentType: practice, parent: "section 3", heading: "Assessment criteria", gloss: "what criteria may evaluate (a list)" }
  - { number: "3.30", order: 91, componentType: paragraph, parent: "section 3", heading: "Assessment criteria", gloss: "specific criteria" }
  - { number: "3.31", order: 92, componentType: practice, parent: "section 3", heading: "Assessment criteria", gloss: "assessing workshop contribution" }
  - { number: "3.32", order: 93, componentType: paragraph, parent: "section 3", heading: "Assessment criteria", gloss: "AI and the assessment of originality" }
  - { number: "3.33", order: 94, componentType: paragraph, parent: "section 3", heading: "Postgraduate programmes", gloss: "master's degrees: aims and professional readiness" }
  - { number: "4.1", order: 96, componentType: paragraph, parent: "section 4", heading: "Introduction", gloss: "minimum, typical and excellent standards for honours" }
  - { number: "4.2", order: 97, componentType: paragraph, parent: "section 4", heading: "Introduction", gloss: "most exceed the threshold; Annex D" }
  - { number: "4.3", order: 98, componentType: stem, parent: "section 4", heading: "Threshold level: Subject knowledge, understanding and skills", gloss: "threshold rung (a list)" }
  - { number: "4.4", order: 99, componentType: stem, parent: "section 4", heading: "Typical level: Subject knowledge, understanding and skills", gloss: "typical rung (a list)" }
  - { number: "4.5", order: 100, componentType: stem, parent: "section 4", heading: "Excellent level: Subject knowledge, understanding and skills", gloss: "excellent rung: a lead paragraph and a list" }
  - { number: "4.6", order: 101, componentType: stem, parent: "section 4", heading: "Generic skills", gloss: "generic skills (a list)" }
  - { number: "4.7", order: 102, componentType: stem, parent: "section 4", heading: "Master's level", gloss: "master's level outcomes (a list)" }
  - { number: "1", componentType: section, parent: none, heading: "Context and purposes of a Creative Writing degree", gloss: "section 1" }
  - { number: "2", componentType: section, parent: none, heading: "Distinctive features of the Creative Writing degree", gloss: "section 2" }
  - { number: "3", componentType: section, parent: none, heading: "Content, structure and delivery", gloss: "section 3" }
  - { number: "4", componentType: section, parent: none, heading: "Benchmark standards", gloss: "section 4" }
excluded:
  - { number: "none", heading: "Contents; About this Statement; How can I use this document?; Relationship to legislation; Additional sector reference points", kind: "other: front matter, read for S1, S2, S7 and SB6" }
  - { number: "1, 2, 3, 4", heading: "section heading lines", kind: "other: headings, recorded in SECTIONS" }
  - { number: "5", heading: "List of references and further resources", kind: "other: ten references, read for SB6" }
  - { number: "6", heading: "Membership of the Advisory Group (2023, 2019, 2016)", kind: "other: authorship history, read for S7 supersedes" }
```

### S4 Statements
<!-- label: both; status: drafted; basis: primary. Only standards (D-std-0002 (a)): 90 records. `source` is the issuer's statement exactly as its span holds it (D-std-0014). -->
```yaml
- id: qaa/creative-writing-2024/1.20
  locator: { number: "1.20", headingPath: ["Context and purposes of a Creative Writing degree", "Purposes and characteristics of a Creative Writing degree: Characteristics of Creative Writing in higher education"] }
  span: { start: 22285, end: 22799 }
  source: "Teaching and learning activities employed by Creative Writing courses will often involve significant opportunities for peer-to-peer feedback. Creative Writing students may be exposed to a range of perspectives when presenting their work. Such collaborative activities can be considered as a key stage in the development of student work. Students should be encouraged to take advantage of these experiences to refine their skills in giving and receiving feedback, in a manner that is both productive and empathetic."
  stem: none
  statementType: expectation
  rung: none
  force: should
  level: none
  appliesTo: "Creative Writing courses"
  addressee: provider
  verbs: ["encouraged", "refine"]
  about: "encouraging students to use peer feedback"
  themes: [none]
  domain: none
  award: ["bachelor's with honours"]
  gradeOf: none
  paraphrase: "Peer feedback is a frequent and formative part of teaching in the subject; courses should encourage students to use these occasions to sharpen how they give and take feedback, usefully and with empathy."
  quote: full   # the issuer's statement is in `source` (D-std-0014)
  audience: practitioner
  subjects: inherited
- id: qaa/creative-writing-2024/1.31
  locator: { number: "1.31", headingPath: ["Context and purposes of a Creative Writing degree", "Accessibility"] }
  span: { start: 29605, end: 30314 }
  source: "Collaborative and/or peer-led workshops are a common feature of many Creative Writing courses. During these workshops students read a section of their writing in progress to the group. The tutor then invites other workshop participants to provide feedback on the work in progress. There are some important critiques of pedagogical approaches to workshops which are worth considering when designing inclusive learning experiences. While workshops can provide a valuable learning experience, additional preparation is required to ensure that the experience is accessible to all students, including those with physical disabilities, learning disabilities, and neurodivergent and chronic mental health conditions."
  stem: none
  statementType: requirement
  rung: none
  force: must
  level: none
  appliesTo: "Creative Writing courses that use workshops"
  addressee: provider
  verbs: ["required", "ensure"]
  about: "extra preparation to make workshops accessible"
  themes: [theme:accessibility]
  domain: none
  award: ["bachelor's with honours"]
  gradeOf: none
  paraphrase: "Workshops, where students read work in progress and peers respond, are common and open to critique; to make them accessible to every student, including disabled and neurodivergent students and those with chronic mental health conditions, further preparation is required."
  quote: full   # the issuer's statement is in `source` (D-std-0014)
  audience: practitioner
  subjects: inherited
- id: qaa/creative-writing-2024/2.2.b1
  locator: { number: "2.2.b1", headingPath: ["Distinctive features of the Creative Writing degree", "Design"] }
  span: { start: 38231, end: 38350 }
  source: "be practised in the expressive, imaginative and affective resources of language and story, including structure and form"
  stem: "2.2"
  statementType: outcome
  rung: none
  force: will
  level: fheq:6
  appliesTo: "students of the subject"
  addressee: learner
  verbs: ["practised"]
  about: "the resources of language and story"
  themes: [none]
  domain: subject-skill
  award: ["bachelor's with honours"]
  gradeOf: none
  paraphrase: "Through study of the subject, students will reach experienced use of the expressive, imaginative and emotional resources of language and story, structure and form included."
  quote: full   # the issuer's statement is in `source` (D-std-0014)
  audience: both
  subjects: inherited
- id: qaa/creative-writing-2024/2.2.b2
  locator: { number: "2.2.b2", headingPath: ["Distinctive features of the Creative Writing degree", "Design"] }
  span: { start: 38353, end: 38475 }
  source: "understand text, narrative and language as artistic materials, including historical traditions and possibilities for usage"
  stem: "2.2"
  statementType: outcome
  rung: none
  force: will
  level: fheq:6
  appliesTo: "students of the subject"
  addressee: learner
  verbs: ["understand"]
  about: "text, narrative and language as artistic materials"
  themes: [none]
  domain: understanding
  award: ["bachelor's with honours"]
  gradeOf: none
  paraphrase: "Through study of the subject, students will reach an understanding of text, narrative and language as materials for art, with their past traditions and possible uses."
  quote: full   # the issuer's statement is in `source` (D-std-0014)
  audience: both
  subjects: inherited
- id: qaa/creative-writing-2024/2.2.b3
  locator: { number: "2.2.b3", headingPath: ["Distinctive features of the Creative Writing degree", "Design"] }
  span: { start: 38478, end: 38554 }
  source: "recognise a range of audience responses to and interpretations of their work"
  stem: "2.2"
  statementType: outcome
  rung: none
  force: will
  level: fheq:6
  appliesTo: "students of the subject"
  addressee: learner
  verbs: ["recognise"]
  about: "audience responses to own work"
  themes: [none]
  domain: understanding
  award: ["bachelor's with honours"]
  gradeOf: none
  paraphrase: "Through study of the subject, students will reach recognition of the many ways audiences respond to and read their work."
  quote: full   # the issuer's statement is in `source` (D-std-0014)
  audience: both
  subjects: inherited
- id: qaa/creative-writing-2024/2.2.b4
  locator: { number: "2.2.b4", headingPath: ["Distinctive features of the Creative Writing degree", "Design"] }
  span: { start: 38557, end: 38611 }
  source: "develop critical insights, capabilities and capacities"
  stem: "2.2"
  statementType: outcome
  rung: none
  force: will
  level: fheq:6
  appliesTo: "students of the subject"
  addressee: learner
  verbs: ["develop"]
  about: "critical insight and capability"
  themes: [none]
  domain: understanding
  award: ["bachelor's with honours"]
  gradeOf: none
  paraphrase: "Through study of the subject, students will reach growth in critical insight and in the capacity to use it."
  quote: full   # the issuer's statement is in `source` (D-std-0014)
  audience: both
  subjects: inherited
- id: qaa/creative-writing-2024/2.2.b5
  locator: { number: "2.2.b5", headingPath: ["Distinctive features of the Creative Writing degree", "Design"] }
  span: { start: 38614, end: 38722 }
  source: "have responsibility for their own work, from conception through to development, editing and final redrafting"
  stem: "2.2"
  statementType: outcome
  rung: none
  force: will
  level: fheq:6
  appliesTo: "students of the subject"
  addressee: learner
  verbs: ["have"]
  about: "responsibility for own work from idea to final draft"
  themes: [none]
  domain: generic-skill
  award: ["bachelor's with honours"]
  gradeOf: none
  paraphrase: "Through study of the subject, students will reach ownership of their own work from first idea through development and editing to the last redraft."
  quote: full   # the issuer's statement is in `source` (D-std-0014)
  audience: both
  subjects: inherited
- id: qaa/creative-writing-2024/2.2.b6
  locator: { number: "2.2.b6", headingPath: ["Distinctive features of the Creative Writing degree", "Design"] }
  span: { start: 38725, end: 38903 }
  source: "be practised in, and appreciate the significance of, editing work over successive drafts, both independently and in discussion with tutors and fellow students through peer review"
  stem: "2.2"
  statementType: outcome
  rung: none
  force: will
  level: fheq:6
  appliesTo: "students of the subject"
  addressee: learner
  verbs: ["practised", "appreciate"]
  about: "editing over successive drafts, alone and with peers"
  themes: [none]
  domain: subject-skill
  award: ["bachelor's with honours"]
  gradeOf: none
  paraphrase: "Through study of the subject, students will reach practice in editing work through repeated drafts, on their own and with tutors and other students through peer review, and a grasp of why it matters."
  quote: full   # the issuer's statement is in `source` (D-std-0014)
  audience: both
  subjects: inherited
- id: qaa/creative-writing-2024/2.2.b7
  locator: { number: "2.2.b7", headingPath: ["Distinctive features of the Creative Writing degree", "Design"] }
  span: { start: 38906, end: 39010 }
  source: "appreciate a wide range of creative and cultural contexts for the production and consumption of writing."
  stem: "2.2"
  statementType: outcome
  rung: none
  force: will
  level: fheq:6
  appliesTo: "students of the subject"
  addressee: learner
  verbs: ["appreciate"]
  about: "creative and cultural contexts of writing"
  themes: [none]
  domain: understanding
  award: ["bachelor's with honours"]
  gradeOf: none
  paraphrase: "Through study of the subject, students will reach an appreciation of the many creative and cultural settings in which writing is made and read."
  quote: full   # the issuer's statement is in `source` (D-std-0014)
  audience: both
  subjects: inherited
- id: qaa/creative-writing-2024/2.3
  locator: { number: "2.3", headingPath: ["Distinctive features of the Creative Writing degree", "Progression"] }
  span: { start: 39027, end: 39636 }
  source: "Over the course of a degree with honours (FHEQ Level 6; FQHEIS Level 10) a Creative Writing student will progress from one level of study to the next, in line with the regulations and processes for each institution. However, it is expected that each level would see the attainment of knowledge, expertise and experience that builds towards the final achievement of meeting the threshold-level subject-specific and generic skills listed in this Statement. This will usually include successful completion and the award of credit for the full range of learning and assessment, including any practical components."
  stem: none
  statementType: expectation
  rung: none
  force: will
  level: fheq:6
  appliesTo: "students on the honours degree"
  addressee: learner
  verbs: ["progress", "builds"]
  about: "progression across levels towards the threshold"
  themes: [none]
  domain: none
  award: ["bachelor's with honours"]
  gradeOf: none
  paraphrase: "Across the honours degree (FHEQ level 6, FQHEIS level 10) a student will move up through the levels under each institution's rules, each level adding knowledge, expertise and experience towards meeting the threshold subject and generic skills, usually by completing and gaining credit for all learning and assessment."
  quote: full   # the issuer's statement is in `source` (D-std-0014)
  audience: both
  subjects: inherited
- id: qaa/creative-writing-2024/2.7
  locator: { number: "2.7", headingPath: ["Distinctive features of the Creative Writing degree", "Progression"] }
  span: { start: 40982, end: 41404 }
  source: "Undergraduates studying Creative Writing courses as part of a combined or joint degree with other subjects will achieve core elements of the specific and generic skills outlined in this Statement and will add others according to the topics covered in the other subject(s) of their degree. Additionally, they may explore the overlap between different disciplines, creating further opportunities for interdisciplinary study."
  stem: none
  statementType: outcome
  rung: none
  force: will
  level: fheq:6
  appliesTo: "joint and combined honours students"
  addressee: learner
  verbs: ["achieve", "add", "explore"]
  about: "core skills in joint and combined degrees"
  themes: [none]
  domain: none
  award: ["bachelor's with honours"]
  gradeOf: none
  paraphrase: "Students taking the subject within a joint or combined degree will reach the core of its specific and generic skills, add others from their other subject and may work across the boundary between disciplines."
  quote: full   # the issuer's statement is in `source` (D-std-0014)
  audience: both
  subjects: inherited
- id: qaa/creative-writing-2024/3.22
  locator: { number: "3.22", headingPath: ["Content, structure and delivery", "Assessment"] }
  span: { start: 64589, end: 64937 }
  source: "Learning in Creative Writing is supported by both formative and summative forms of assessment. Assessments should be made accessible for all students. Alternative assessments should be offered to meet all students' accessibility needs. Policies around extensions, late submissions and extenuating circumstances should be made clear to all students."
  stem: none
  statementType: requirement
  rung: none
  force: should
  level: none
  appliesTo: "Creative Writing courses"
  addressee: provider
  verbs: ["made", "offered"]
  about: "accessible assessment and clear policies"
  themes: [none]
  domain: none
  award: ["bachelor's with honours"]
  gradeOf: none
  paraphrase: "Learning is supported by formative and summative assessment; assessment should be accessible to every student, alternatives should be offered to meet accessibility needs and the rules on extensions, late work and extenuating circumstances should be clear to all."
  quote: full   # the issuer's statement is in `source` (D-std-0014)
  audience: practitioner
  subjects: inherited
- id: qaa/creative-writing-2024/4.2
  locator: { number: "4.2", headingPath: ["Benchmark standards", "Introduction"] }
  span: { start: 70540, end: 71020 }
  source: "The vast majority of students will perform significantly better than the minimum threshold standards. Each higher education provider has its own method of determining what appropriate evidence of this achievement will be and should refer to Annex D in The Frameworks for Higher Education Qualifications of UK Degree-Awarding Bodies. This Annex sets out common descriptions of the four main degree outcome classifications for bachelor's degrees with honours: 1st, 2.1, 2.2 and 3rd."
  stem: none
  statementType: expectation
  rung: none
  force: should
  level: fheq:6
  appliesTo: "higher education providers"
  addressee: provider
  verbs: ["perform", "refer"]
  about: "performance above threshold; Annex D"
  themes: [none]
  domain: none
  award: ["bachelor's with honours"]
  gradeOf: none
  paraphrase: "Most students will do clearly better than the threshold; each provider decides how such achievement is evidenced and should consult Annex D of the qualifications frameworks, which describes the four honours classifications."
  quote: full   # the issuer's statement is in `source` (D-std-0014)
  audience: practitioner
  subjects: inherited
- id: qaa/creative-writing-2024/4.3.b1
  locator: { number: "4.3.b1", headingPath: ["Benchmark standards", "Threshold level: Subject knowledge, understanding and skills"] }
  span: { start: 71163, end: 71244 }
  source: "the ability to generate creative work and develop it through editing and revision"
  stem: "4.3"
  statementType: threshold
  rung: threshold
  force: threshold
  level: fheq:6
  appliesTo: "graduates at the threshold level"
  addressee: learner
  verbs: ["generate", "develop"]
  about: "generating work and developing it by revision"
  themes: [none]
  domain: subject-skill
  award: ["bachelor's with honours"]
  gradeOf: none
  paraphrase: "Will have shown, as the minimum for the honours degree, the capacity to produce creative writing and improve it through editing and redrafting."
  quote: full   # the issuer's statement is in `source` (D-std-0014)
  audience: both
  subjects: inherited
- id: qaa/creative-writing-2024/4.3.b2
  locator: { number: "4.3.b2", headingPath: ["Benchmark standards", "Threshold level: Subject knowledge, understanding and skills"] }
  span: { start: 71247, end: 71315 }
  source: "the ability to reflect upon their own creative processes and outputs"
  stem: "4.3"
  statementType: threshold
  rung: threshold
  force: threshold
  level: fheq:6
  appliesTo: "graduates at the threshold level"
  addressee: learner
  verbs: ["reflect"]
  about: "reflection on own creative process and outputs"
  themes: [none]
  domain: subject-skill
  award: ["bachelor's with honours"]
  gradeOf: none
  paraphrase: "Will have shown, as the minimum for the honours degree, the capacity to think back over how they write and what they produce."
  quote: full   # the issuer's statement is in `source` (D-std-0014)
  audience: both
  subjects: inherited
- id: qaa/creative-writing-2024/4.3.b3
  locator: { number: "4.3.b3", headingPath: ["Benchmark standards", "Threshold level: Subject knowledge, understanding and skills"] }
  span: { start: 71318, end: 71373 }
  source: "engagement with their creative interests and influences"
  stem: "4.3"
  statementType: threshold
  rung: threshold
  force: threshold
  level: fheq:6
  appliesTo: "graduates at the threshold level"
  addressee: learner
  verbs: []
  about: "engagement with own creative interests and influences"
  themes: [none]
  domain: subject-skill
  award: ["bachelor's with honours"]
  gradeOf: none
  paraphrase: "Will have shown, as the minimum for the honours degree, active engagement with the interests that drive their writing and with the writers and works that shape it."
  quote: full   # the issuer's statement is in `source` (D-std-0014)
  audience: both
  subjects: inherited
- id: qaa/creative-writing-2024/4.3.b4
  locator: { number: "4.3.b4", headingPath: ["Benchmark standards", "Threshold level: Subject knowledge, understanding and skills"] }
  span: { start: 71376, end: 71444 }
  source: "an emerging awareness of a variety of craft and narrative techniques"
  stem: "4.3"
  statementType: threshold
  rung: threshold
  force: threshold
  level: fheq:6
  appliesTo: "graduates at the threshold level"
  addressee: learner
  verbs: []
  about: "early awareness of craft and narrative techniques"
  themes: [none]
  domain: knowledge
  award: ["bachelor's with honours"]
  gradeOf: none
  paraphrase: "Will have shown, as the minimum for the honours degree, a beginning awareness of a range of craft and storytelling techniques."
  quote: full   # the issuer's statement is in `source` (D-std-0014)
  audience: both
  subjects: inherited
- id: qaa/creative-writing-2024/4.3.b5
  locator: { number: "4.3.b5", headingPath: ["Benchmark standards", "Threshold level: Subject knowledge, understanding and skills"] }
  span: { start: 71447, end: 71572 }
  source: "an awareness of the rules, conventions and possibilities of written and spoken language in a range of forms, genres and media"
  stem: "4.3"
  statementType: threshold
  rung: threshold
  force: threshold
  level: fheq:6
  appliesTo: "graduates at the threshold level"
  addressee: learner
  verbs: []
  about: "awareness of the rules and possibilities of written and spoken language"
  themes: [none]
  domain: knowledge
  award: ["bachelor's with honours"]
  gradeOf: none
  paraphrase: "Will have shown, as the minimum for the honours degree, awareness of how written and spoken language works across forms, genres and media, with its rules, its conventions and what it makes possible."
  quote: full   # the issuer's statement is in `source` (D-std-0014)
  audience: both
  subjects: inherited
- id: qaa/creative-writing-2024/4.3.b6
  locator: { number: "4.3.b6", headingPath: ["Benchmark standards", "Threshold level: Subject knowledge, understanding and skills"] }
  span: { start: 71575, end: 71645 }
  source: "the ability to read and respond to published work and work in progress"
  stem: "4.3"
  statementType: threshold
  rung: threshold
  force: threshold
  level: fheq:6
  appliesTo: "graduates at the threshold level"
  addressee: learner
  verbs: ["read", "respond"]
  about: "reading and responding to published and draft work"
  themes: [none]
  domain: subject-skill
  award: ["bachelor's with honours"]
  gradeOf: none
  paraphrase: "Will have shown, as the minimum for the honours degree, the capacity to read published writing and drafts in progress and to respond to them."
  quote: full   # the issuer's statement is in `source` (D-std-0014)
  audience: both
  subjects: inherited
- id: qaa/creative-writing-2024/4.3.b7
  locator: { number: "4.3.b7", headingPath: ["Benchmark standards", "Threshold level: Subject knowledge, understanding and skills"] }
  span: { start: 71648, end: 71783 }
  source: "an awareness of the historical and cultural dimensions of language use and literature, including story skills and evolving technologies"
  stem: "4.3"
  statementType: threshold
  rung: threshold
  force: threshold
  level: fheq:6
  appliesTo: "graduates at the threshold level"
  addressee: learner
  verbs: []
  about: "historical and cultural dimensions of language and literature"
  themes: [none]
  domain: understanding
  award: ["bachelor's with honours"]
  gradeOf: none
  paraphrase: "Will have shown, as the minimum for the honours degree, awareness of the history and culture behind how language is used and literature made, storytelling and changing technologies included."
  quote: full   # the issuer's statement is in `source` (D-std-0014)
  audience: both
  subjects: inherited
- id: qaa/creative-writing-2024/4.3.b8
  locator: { number: "4.3.b8", headingPath: ["Benchmark standards", "Threshold level: Subject knowledge, understanding and skills"] }
  span: { start: 71786, end: 71899 }
  source: "the ability to communicate to diverse audiences, using a range of narrative forms, digital technologies and media"
  stem: "4.3"
  statementType: threshold
  rung: threshold
  force: threshold
  level: fheq:6
  appliesTo: "graduates at the threshold level"
  addressee: learner
  verbs: ["communicate", "using"]
  about: "communicating to diverse audiences across forms and media"
  themes: [none]
  domain: subject-skill
  award: ["bachelor's with honours"]
  gradeOf: none
  paraphrase: "Will have shown, as the minimum for the honours degree, the capacity to reach varied audiences through a range of narrative forms, digital tools and media."
  quote: full   # the issuer's statement is in `source` (D-std-0014)
  audience: both
  subjects: inherited
- id: qaa/creative-writing-2024/4.3.b9
  locator: { number: "4.3.b9", headingPath: ["Benchmark standards", "Threshold level: Subject knowledge, understanding and skills"] }
  span: { start: 71902, end: 72019 }
  source: "an awareness of the skills required for effective work in groups, including an openness and commitment to inclusivity"
  stem: "4.3"
  statementType: threshold
  rung: threshold
  force: threshold
  level: fheq:6
  appliesTo: "graduates at the threshold level"
  addressee: learner
  verbs: []
  about: "awareness of group work skills and inclusivity"
  themes: [none]
  domain: generic-skill
  award: ["bachelor's with honours"]
  gradeOf: none
  paraphrase: "Will have shown, as the minimum for the honours degree, awareness of what effective group work needs, with openness and a commitment to inclusion."
  quote: full   # the issuer's statement is in `source` (D-std-0014)
  audience: both
  subjects: inherited
- id: qaa/creative-writing-2024/4.3.b10
  locator: { number: "4.3.b10", headingPath: ["Benchmark standards", "Threshold level: Subject knowledge, understanding and skills"] }
  span: { start: 72022, end: 72144 }
  source: "an awareness of the applications of Creative Writing skills to a variety of contexts, careers and entrepreneurial settings"
  stem: "4.3"
  statementType: threshold
  rung: threshold
  force: threshold
  level: fheq:6
  appliesTo: "graduates at the threshold level"
  addressee: learner
  verbs: []
  about: "applications of writing skills to careers and enterprise"
  themes: [none]
  domain: understanding
  award: ["bachelor's with honours"]
  gradeOf: none
  paraphrase: "Will have shown, as the minimum for the honours degree, awareness of how the subject's skills apply in varied settings, careers and enterprises."
  quote: full   # the issuer's statement is in `source` (D-std-0014)
  audience: both
  subjects: inherited
- id: qaa/creative-writing-2024/4.3.b11
  locator: { number: "4.3.b11", headingPath: ["Benchmark standards", "Threshold level: Subject knowledge, understanding and skills"] }
  span: { start: 72147, end: 72253 }
  source: "an awareness of the contribution that Creative Writing can make to sustainability and environmental issues"
  stem: "4.3"
  statementType: threshold
  rung: threshold
  force: threshold
  level: fheq:6
  appliesTo: "graduates at the threshold level"
  addressee: learner
  verbs: []
  about: "the subject's contribution to sustainability"
  themes: [none]
  domain: understanding
  award: ["bachelor's with honours"]
  gradeOf: none
  paraphrase: "Will have shown, as the minimum for the honours degree, awareness of what creative writing can contribute to sustainability and environmental questions."
  quote: full   # the issuer's statement is in `source` (D-std-0014)
  audience: both
  subjects: inherited
- id: qaa/creative-writing-2024/4.3.b12
  locator: { number: "4.3.b12", headingPath: ["Benchmark standards", "Threshold level: Subject knowledge, understanding and skills"] }
  span: { start: 72256, end: 72315 }
  source: "an understanding of forms of prose, poetry, story and drama"
  stem: "4.3"
  statementType: threshold
  rung: threshold
  force: threshold
  level: fheq:6
  appliesTo: "graduates at the threshold level"
  addressee: learner
  verbs: []
  about: "forms of prose, poetry, story and drama"
  themes: [none]
  domain: knowledge
  award: ["bachelor's with honours"]
  gradeOf: none
  paraphrase: "Will have shown, as the minimum for the honours degree, an understanding of the forms that prose, poetry, story and drama take."
  quote: full   # the issuer's statement is in `source` (D-std-0014)
  audience: both
  subjects: inherited
- id: qaa/creative-writing-2024/4.3.b13
  locator: { number: "4.3.b13", headingPath: ["Benchmark standards", "Threshold level: Subject knowledge, understanding and skills"] }
  span: { start: 72318, end: 72498 }
  source: "the ability to explore and engage with a range of genres, which may include memoir, life writing, short fiction, crime, fantasy, literary, children and young adults, and many more."
  stem: "4.3"
  statementType: threshold
  rung: threshold
  force: threshold
  level: fheq:6
  appliesTo: "graduates at the threshold level"
  addressee: learner
  verbs: ["explore", "engage"]
  about: "exploring a range of genres"
  themes: [none]
  domain: subject-skill
  award: ["bachelor's with honours"]
  gradeOf: none
  paraphrase: "Will have shown, as the minimum for the honours degree, the capacity to try out and work within a range of genres, such as memoir, short fiction, crime or fantasy."
  quote: full   # the issuer's statement is in `source` (D-std-0014)
  audience: both
  subjects: inherited
- id: qaa/creative-writing-2024/4.4.b1
  locator: { number: "4.4.b1", headingPath: ["Benchmark standards", "Typical level: Subject knowledge, understanding and skills"] }
  span: { start: 72640, end: 72803 }
  source: "the ability to conceptualise, generate and develop original Creative Writing skills using a wide range of editorial, presentational, narrative and craft techniques"
  stem: "4.4"
  statementType: typical
  rung: typical
  force: will
  level: fheq:6
  appliesTo: "graduates at the typical level"
  addressee: learner
  verbs: ["conceptualise", "generate", "develop"]
  about: "conceiving and developing original work with many techniques"
  themes: [none]
  domain: subject-skill
  award: ["bachelor's with honours"]
  gradeOf: { statement: qaa/creative-writing-2024/4.3.b1, basis: inferred }
  paraphrase: "Will have shown, at the typical level for the honours degree, the capacity to conceive, produce and develop original creative writing, drawing on many editing, presentation, narrative and craft techniques."
  quote: full   # the issuer's statement is in `source` (D-std-0014)
  audience: both
  subjects: inherited
- id: qaa/creative-writing-2024/4.4.b2
  locator: { number: "4.4.b2", headingPath: ["Benchmark standards", "Typical level: Subject knowledge, understanding and skills"] }
  span: { start: 72806, end: 72923 }
  source: "a reflective approach to the process of composition that encompasses critical evaluation of Creative Writing practice"
  stem: "4.4"
  statementType: typical
  rung: typical
  force: will
  level: fheq:6
  appliesTo: "graduates at the typical level"
  addressee: learner
  verbs: []
  about: "reflective, critically evaluative approach to composition"
  themes: [none]
  domain: subject-skill
  award: ["bachelor's with honours"]
  gradeOf: { statement: qaa/creative-writing-2024/4.3.b2, basis: inferred }
  paraphrase: "Will have shown, at the typical level for the honours degree, a reflective approach to writing that includes critical evaluation of their own practice."
  quote: full   # the issuer's statement is in `source` (D-std-0014)
  audience: both
  subjects: inherited
- id: qaa/creative-writing-2024/4.4.b3
  locator: { number: "4.4.b3", headingPath: ["Benchmark standards", "Typical level: Subject knowledge, understanding and skills"] }
  span: { start: 72926, end: 73010 }
  source: "the ability to actively explore relationships between reading and their own practice"
  stem: "4.4"
  statementType: typical
  rung: typical
  force: will
  level: fheq:6
  appliesTo: "graduates at the typical level"
  addressee: learner
  verbs: ["explore"]
  about: "relationships between reading and own practice"
  themes: [none]
  domain: subject-skill
  award: ["bachelor's with honours"]
  gradeOf: none
  paraphrase: "Will have shown, at the typical level for the honours degree, active exploration of how their reading relates to their own writing."
  quote: full   # the issuer's statement is in `source` (D-std-0014)
  audience: both
  subjects: inherited
- id: qaa/creative-writing-2024/4.4.b4
  locator: { number: "4.4.b4", headingPath: ["Benchmark standards", "Typical level: Subject knowledge, understanding and skills"] }
  span: { start: 73013, end: 73079 }
  source: "the ability to effectively compose a story, poem or piece of prose"
  stem: "4.4"
  statementType: typical
  rung: typical
  force: will
  level: fheq:6
  appliesTo: "graduates at the typical level"
  addressee: learner
  verbs: ["compose"]
  about: "composing a story, poem or prose piece"
  themes: [none]
  domain: subject-skill
  award: ["bachelor's with honours"]
  gradeOf: none
  paraphrase: "Will have shown, at the typical level for the honours degree, the capacity to write a story, poem or prose piece that works."
  quote: full   # the issuer's statement is in `source` (D-std-0014)
  audience: both
  subjects: inherited
- id: qaa/creative-writing-2024/4.4.b5
  locator: { number: "4.4.b5", headingPath: ["Benchmark standards", "Typical level: Subject knowledge, understanding and skills"] }
  span: { start: 73082, end: 73216 }
  source: "the ability to utilise the conventions and possibilities of written and spoken language in a range of forms, genres and emerging media"
  stem: "4.4"
  statementType: typical
  rung: typical
  force: will
  level: fheq:6
  appliesTo: "graduates at the typical level"
  addressee: learner
  verbs: ["utilise"]
  about: "using the conventions and possibilities of language in emerging media"
  themes: [none]
  domain: subject-skill
  award: ["bachelor's with honours"]
  gradeOf: none
  paraphrase: "Will have shown, at the typical level for the honours degree, the capacity to use the conventions of written and spoken language, and what it makes possible, across forms, genres and new media."
  quote: full   # the issuer's statement is in `source` (D-std-0014)
  audience: both
  subjects: inherited
- id: qaa/creative-writing-2024/4.4.b6
  locator: { number: "4.4.b6", headingPath: ["Benchmark standards", "Typical level: Subject knowledge, understanding and skills"] }
  span: { start: 73219, end: 73366 }
  source: "a creative and discriminating engagement with the expressive, poetic, narratological and/or imaginative capabilities of written and spoken language"
  stem: "4.4"
  statementType: typical
  rung: typical
  force: will
  level: fheq:6
  appliesTo: "graduates at the typical level"
  addressee: learner
  verbs: []
  about: "creative, discerning engagement with what language can do"
  themes: [none]
  domain: subject-skill
  award: ["bachelor's with honours"]
  gradeOf: none
  paraphrase: "Will have shown, at the typical level for the honours degree, a creative and discerning engagement with what written and spoken language can do expressively, poetically and in narrative."
  quote: full   # the issuer's statement is in `source` (D-std-0014)
  audience: both
  subjects: inherited
- id: qaa/creative-writing-2024/4.4.b7
  locator: { number: "4.4.b7", headingPath: ["Benchmark standards", "Typical level: Subject knowledge, understanding and skills"] }
  span: { start: 73369, end: 73431 }
  source: "an independent and disciplined commitment to their own writing"
  stem: "4.4"
  statementType: typical
  rung: typical
  force: will
  level: fheq:6
  appliesTo: "graduates at the typical level"
  addressee: learner
  verbs: []
  about: "independent, disciplined commitment to writing"
  themes: [none]
  domain: generic-skill
  award: ["bachelor's with honours"]
  gradeOf: none
  paraphrase: "Will have shown, at the typical level for the honours degree, independent, disciplined commitment to their own writing."
  quote: full   # the issuer's statement is in `source` (D-std-0014)
  audience: both
  subjects: inherited
- id: qaa/creative-writing-2024/4.4.b8
  locator: { number: "4.4.b8", headingPath: ["Benchmark standards", "Typical level: Subject knowledge, understanding and skills"] }
  span: { start: 73434, end: 73501 }
  source: "an understanding of the connection of reading to their own practice"
  stem: "4.4"
  statementType: typical
  rung: typical
  force: will
  level: fheq:6
  appliesTo: "graduates at the typical level"
  addressee: learner
  verbs: []
  about: "understanding the link between reading and own practice"
  themes: [none]
  domain: understanding
  award: ["bachelor's with honours"]
  gradeOf: none
  paraphrase: "Will have shown, at the typical level for the honours degree, an understanding of how reading connects to their own writing practice."
  quote: full   # the issuer's statement is in `source` (D-std-0014)
  audience: both
  subjects: inherited
- id: qaa/creative-writing-2024/4.4.b9
  locator: { number: "4.4.b9", headingPath: ["Benchmark standards", "Typical level: Subject knowledge, understanding and skills"] }
  span: { start: 73504, end: 73616 }
  source: "the ability to read and respond critically, creatively and practically to published work and to work in progress"
  stem: "4.4"
  statementType: typical
  rung: typical
  force: will
  level: fheq:6
  appliesTo: "graduates at the typical level"
  addressee: learner
  verbs: ["read", "respond"]
  about: "critical, creative and practical response to published and draft work"
  themes: [none]
  domain: subject-skill
  award: ["bachelor's with honours"]
  gradeOf: { statement: qaa/creative-writing-2024/4.3.b6, basis: inferred }
  paraphrase: "Will have shown, at the typical level for the honours degree, the capacity to read published writing and drafts in progress and to answer them critically, creatively and practically."
  quote: full   # the issuer's statement is in `source` (D-std-0014)
  audience: both
  subjects: inherited
- id: qaa/creative-writing-2024/4.4.b10
  locator: { number: "4.4.b10", headingPath: ["Benchmark standards", "Typical level: Subject knowledge, understanding and skills"] }
  span: { start: 73619, end: 73820 }
  source: "an understanding of the historical and socio-cultural dimensions of language use, including traditional modes of textual production, divergent forms of story and emerging digital and media technologies"
  stem: "4.4"
  statementType: typical
  rung: typical
  force: will
  level: fheq:6
  appliesTo: "graduates at the typical level"
  addressee: learner
  verbs: []
  about: "historical and socio-cultural dimensions of language and story"
  themes: [none]
  domain: understanding
  award: ["bachelor's with honours"]
  gradeOf: { statement: qaa/creative-writing-2024/4.3.b7, basis: inferred }
  paraphrase: "Will have shown, at the typical level for the honours degree, an understanding of the history and the social and cultural setting of language use, from older ways of making texts to divergent kinds of story and new digital and media technologies."
  quote: full   # the issuer's statement is in `source` (D-std-0014)
  audience: both
  subjects: inherited
- id: qaa/creative-writing-2024/4.4.b11
  locator: { number: "4.4.b11", headingPath: ["Benchmark standards", "Typical level: Subject knowledge, understanding and skills"] }
  span: { start: 73823, end: 73925 }
  source: "the ability to contextualise their own writing within given historical, cultural or generic frameworks"
  stem: "4.4"
  statementType: typical
  rung: typical
  force: will
  level: fheq:6
  appliesTo: "graduates at the typical level"
  addressee: learner
  verbs: ["contextualise"]
  about: "placing own writing in historical, cultural or generic frameworks"
  themes: [none]
  domain: subject-skill
  award: ["bachelor's with honours"]
  gradeOf: none
  paraphrase: "Will have shown, at the typical level for the honours degree, the capacity to place their own writing within a given historical, cultural or genre framework."
  quote: full   # the issuer's statement is in `source` (D-std-0014)
  audience: both
  subjects: inherited
- id: qaa/creative-writing-2024/4.4.b12
  locator: { number: "4.4.b12", headingPath: ["Benchmark standards", "Typical level: Subject knowledge, understanding and skills"] }
  span: { start: 73928, end: 74048 }
  source: "an understanding of writing as a narrative form of expression and communication, engaging diverse audiences and purposes"
  stem: "4.4"
  statementType: typical
  rung: typical
  force: will
  level: fheq:6
  appliesTo: "graduates at the typical level"
  addressee: learner
  verbs: []
  about: "writing as narrative expression for diverse audiences and purposes"
  themes: [none]
  domain: understanding
  award: ["bachelor's with honours"]
  gradeOf: none
  paraphrase: "Will have shown, at the typical level for the honours degree, an understanding of writing as a narrative means of expression and communication that serves varied audiences and purposes."
  quote: full   # the issuer's statement is in `source` (D-std-0014)
  audience: both
  subjects: inherited
- id: qaa/creative-writing-2024/4.4.b13
  locator: { number: "4.4.b13", headingPath: ["Benchmark standards", "Typical level: Subject knowledge, understanding and skills"] }
  span: { start: 74051, end: 74163 }
  source: "the ability to communicate with diverse audiences, using a wide range of narrative forms, story skills and media"
  stem: "4.4"
  statementType: typical
  rung: typical
  force: will
  level: fheq:6
  appliesTo: "graduates at the typical level"
  addressee: learner
  verbs: ["communicate", "using"]
  about: "communicating with diverse audiences across many forms and media"
  themes: [none]
  domain: subject-skill
  award: ["bachelor's with honours"]
  gradeOf: { statement: qaa/creative-writing-2024/4.3.b8, basis: inferred }
  paraphrase: "Will have shown, at the typical level for the honours degree, the capacity to communicate with varied audiences through many narrative forms, story skills and media."
  quote: full   # the issuer's statement is in `source` (D-std-0014)
  audience: both
  subjects: inherited
- id: qaa/creative-writing-2024/4.4.b14
  locator: { number: "4.4.b14", headingPath: ["Benchmark standards", "Typical level: Subject knowledge, understanding and skills"] }
  span: { start: 74166, end: 74283 }
  source: "the ability to imaginatively explore place, planet, climate, habitat, sustainability and/or the life of other species"
  stem: "4.4"
  statementType: typical
  rung: typical
  force: will
  level: fheq:6
  appliesTo: "graduates at the typical level"
  addressee: learner
  verbs: ["explore"]
  about: "imaginative exploration of place, planet and other species"
  themes: [none]
  domain: subject-skill
  award: ["bachelor's with honours"]
  gradeOf: none
  paraphrase: "Will have shown, at the typical level for the honours degree, the capacity to explore imaginatively place, planet, climate, habitat, sustainability or the lives of other species."
  quote: full   # the issuer's statement is in `source` (D-std-0014)
  audience: both
  subjects: inherited
- id: qaa/creative-writing-2024/4.4.b15
  locator: { number: "4.4.b15", headingPath: ["Benchmark standards", "Typical level: Subject knowledge, understanding and skills"] }
  span: { start: 74286, end: 74409 }
  source: "the ability to engage effectively with different voices and diverse groups of writers to improve their own and others' work"
  stem: "4.4"
  statementType: typical
  rung: typical
  force: will
  level: fheq:6
  appliesTo: "graduates at the typical level"
  addressee: learner
  verbs: ["engage", "improve"]
  about: "engaging with diverse writers to improve own and others' work"
  themes: [none]
  domain: generic-skill
  award: ["bachelor's with honours"]
  gradeOf: { statement: qaa/creative-writing-2024/4.3.b9, basis: inferred }
  paraphrase: "Will have shown, at the typical level for the honours degree, the capacity to work well with different voices and varied groups of writers to strengthen their own and others' writing."
  quote: full   # the issuer's statement is in `source` (D-std-0014)
  audience: both
  subjects: inherited
- id: qaa/creative-writing-2024/4.4.b16
  locator: { number: "4.4.b16", headingPath: ["Benchmark standards", "Typical level: Subject knowledge, understanding and skills"] }
  span: { start: 74412, end: 74508 }
  source: "skills in the constructive reception and delivery of feedback on their own and their peers' work"
  stem: "4.4"
  statementType: typical
  rung: typical
  force: will
  level: fheq:6
  appliesTo: "graduates at the typical level"
  addressee: learner
  verbs: []
  about: "giving and receiving feedback constructively"
  themes: [none]
  domain: generic-skill
  award: ["bachelor's with honours"]
  gradeOf: none
  paraphrase: "Will have shown, at the typical level for the honours degree, skill in taking and giving constructive feedback on their own work and their peers'."
  quote: full   # the issuer's statement is in `source` (D-std-0014)
  audience: both
  subjects: inherited
- id: qaa/creative-writing-2024/4.4.b17
  locator: { number: "4.4.b17", headingPath: ["Benchmark standards", "Typical level: Subject knowledge, understanding and skills"] }
  span: { start: 74511, end: 74579 }
  source: "co-authoring skills and techniques to realise a collaborative vision"
  stem: "4.4"
  statementType: typical
  rung: typical
  force: will
  level: fheq:6
  appliesTo: "graduates at the typical level"
  addressee: learner
  verbs: []
  about: "co-authoring for a shared vision"
  themes: [none]
  domain: subject-skill
  award: ["bachelor's with honours"]
  gradeOf: none
  paraphrase: "Will have shown, at the typical level for the honours degree, co-writing skills and techniques that bring a shared creative vision to life."
  quote: full   # the issuer's statement is in `source` (D-std-0014)
  audience: both
  subjects: inherited
- id: qaa/creative-writing-2024/4.4.b18
  locator: { number: "4.4.b18", headingPath: ["Benchmark standards", "Typical level: Subject knowledge, understanding and skills"] }
  span: { start: 74582, end: 74723 }
  source: "an awareness of research skills and methodologies appropriate to Creative Writing, and the ability to plan and carry out independent research"
  stem: "4.4"
  statementType: typical
  rung: typical
  force: will
  level: fheq:6
  appliesTo: "graduates at the typical level"
  addressee: learner
  verbs: ["plan", "carry"]
  about: "research skills and independent research"
  themes: [none]
  domain: subject-skill
  award: ["bachelor's with honours"]
  gradeOf: none
  paraphrase: "Will have shown, at the typical level for the honours degree, awareness of research skills and methods suited to creative writing, and the capacity to plan and conduct their own research."
  quote: full   # the issuer's statement is in `source` (D-std-0014)
  audience: both
  subjects: inherited
- id: qaa/creative-writing-2024/4.4.b19
  locator: { number: "4.4.b19", headingPath: ["Benchmark standards", "Typical level: Subject knowledge, understanding and skills"] }
  span: { start: 74726, end: 74876 }
  source: "an understanding of the strategic transferability of Creative Writing and story skills to a variety of contexts, careers and entrepreneurial settings."
  stem: "4.4"
  statementType: typical
  rung: typical
  force: will
  level: fheq:6
  appliesTo: "graduates at the typical level"
  addressee: learner
  verbs: []
  about: "strategic transferability of writing and story skills"
  themes: [none]
  domain: understanding
  award: ["bachelor's with honours"]
  gradeOf: { statement: qaa/creative-writing-2024/4.3.b10, basis: inferred }
  paraphrase: "Will have shown, at the typical level for the honours degree, an understanding of how, with strategy, the subject's writing and story skills transfer to varied settings, careers and enterprises."
  quote: full   # the issuer's statement is in `source` (D-std-0014)
  audience: both
  subjects: inherited
- id: qaa/creative-writing-2024/4.5
  locator: { number: "4.5", headingPath: ["Benchmark standards", "Excellent level: Subject knowledge, understanding and skills"] }
  span: { start: 74945, end: 75247 }
  source: "Creative Writing graduates who attain the excellent standard demonstrate the qualities listed above, creatively integrated and combined with independent enterprise and flair to produce work that is ambitious, markedly original in its relation to existing work in its field and searching in its enquiry."
  stem: none
  statementType: excellent
  rung: excellent
  force: will
  level: fheq:6
  appliesTo: "graduates at the excellent level"
  addressee: learner
  verbs: ["demonstrate", "produce"]
  about: "integrating the lower rungs with enterprise and flair"
  themes: [none]
  domain: subject-skill
  award: ["bachelor's with honours"]
  gradeOf: none
  paraphrase: "Will have shown, at the excellent level, the qualities of the lower rungs brought together creatively with independent enterprise and flair, in work that is ambitious, clearly original against what already exists and probing in its enquiry."
  quote: full   # the issuer's statement is in `source` (D-std-0014)
  audience: both
  subjects: inherited
- id: qaa/creative-writing-2024/4.5.b1
  locator: { number: "4.5.b1", headingPath: ["Benchmark standards", "Excellent level: Subject knowledge, understanding and skills"] }
  span: { start: 75431, end: 75517 }
  source: "the ability to produce original writing that offers transformative approaches to genre"
  stem: "4.5"
  statementType: excellent
  rung: excellent
  force: will
  level: fheq:6
  appliesTo: "graduates at the excellent level"
  addressee: learner
  verbs: ["produce", "offers"]
  about: "original writing transforming genre"
  themes: [none]
  domain: subject-skill
  award: ["bachelor's with honours"]
  gradeOf: none
  paraphrase: "May be among the qualities, of which graduates at the excellent level will show some: original writing that changes how a genre can be approached."
  quote: full   # the issuer's statement is in `source` (D-std-0014)
  audience: both
  subjects: inherited
- id: qaa/creative-writing-2024/4.5.b2
  locator: { number: "4.5.b2", headingPath: ["Benchmark standards", "Excellent level: Subject knowledge, understanding and skills"] }
  span: { start: 75520, end: 75586 }
  source: "fluency in a wide range of narrative forms, story skills and media"
  stem: "4.5"
  statementType: excellent
  rung: excellent
  force: will
  level: fheq:6
  appliesTo: "graduates at the excellent level"
  addressee: learner
  verbs: []
  about: "fluency across narrative forms, story skills and media"
  themes: [none]
  domain: subject-skill
  award: ["bachelor's with honours"]
  gradeOf: { statement: qaa/creative-writing-2024/4.4.b13, basis: inferred }
  paraphrase: "May be among the qualities, of which graduates at the excellent level will show some: fluent command of many narrative forms, story skills and media."
  quote: full   # the issuer's statement is in `source` (D-std-0014)
  audience: both
  subjects: inherited
- id: qaa/creative-writing-2024/4.5.s2
  locator: { number: "4.5.s2", headingPath: ["Benchmark standards", "Excellent level: Subject knowledge, understanding and skills"] }
  span: { start: 75248, end: 75335 }
  source: "Where an industry presentation standard exists, the writing should meet or exceed this."
  stem: none
  statementType: excellent
  rung: excellent
  force: should
  level: fheq:6
  appliesTo: "graduates at the excellent level"
  addressee: learner
  verbs: ["meet", "exceed"]
  about: "meeting industry presentation standards"
  themes: [none]
  domain: subject-skill
  award: ["bachelor's with honours"]
  gradeOf: none
  paraphrase: "Where the industry has a presentation standard, writing at the excellent level should match or surpass it."
  quote: full   # the issuer's statement is in `source` (D-std-0014)
  audience: both
  subjects: inherited
- id: qaa/creative-writing-2024/4.5.b3
  locator: { number: "4.5.b3", headingPath: ["Benchmark standards", "Excellent level: Subject knowledge, understanding and skills"] }
  span: { start: 75589, end: 75655 }
  source: "innovation in the use of language, regardless of the topic or form"
  stem: "4.5"
  statementType: excellent
  rung: excellent
  force: will
  level: fheq:6
  appliesTo: "graduates at the excellent level"
  addressee: learner
  verbs: []
  about: "innovative use of language"
  themes: [none]
  domain: subject-skill
  award: ["bachelor's with honours"]
  gradeOf: { statement: qaa/creative-writing-2024/4.4.b6, basis: inferred }
  paraphrase: "May be among the qualities, of which graduates at the excellent level will show some: inventive use of language whatever the subject or form."
  quote: full   # the issuer's statement is in `source` (D-std-0014)
  audience: both
  subjects: inherited
- id: qaa/creative-writing-2024/4.5.b4
  locator: { number: "4.5.b4", headingPath: ["Benchmark standards", "Excellent level: Subject knowledge, understanding and skills"] }
  span: { start: 75658, end: 75820 }
  source: "writing which presents original approaches and responses in meaningful and potentially impactful ways to societal inclusion, diversity, accessibility and equality"
  stem: "4.5"
  statementType: excellent
  rung: excellent
  force: will
  level: fheq:6
  appliesTo: "graduates at the excellent level"
  addressee: learner
  verbs: ["presents"]
  about: "original responses to inclusion, diversity, accessibility and equality"
  themes: [none]
  domain: subject-skill
  award: ["bachelor's with honours"]
  gradeOf: none
  paraphrase: "May be among the qualities, of which graduates at the excellent level will show some: writing that brings original, meaningful and potentially influential responses to inclusion, diversity, accessibility and equality in society."
  quote: full   # the issuer's statement is in `source` (D-std-0014)
  audience: both
  subjects: inherited
- id: qaa/creative-writing-2024/4.5.b5
  locator: { number: "4.5.b5", headingPath: ["Benchmark standards", "Excellent level: Subject knowledge, understanding and skills"] }
  span: { start: 75823, end: 76037 }
  source: "writing which presents a transformative awareness of how changes can be made to support sustainability and/or explores new possibilities for the relationship between humans, non-humans and their ecological habitats"
  stem: "4.5"
  statementType: excellent
  rung: excellent
  force: will
  level: fheq:6
  appliesTo: "graduates at the excellent level"
  addressee: learner
  verbs: ["presents", "explores"]
  about: "transformative writing on sustainability and ecology"
  themes: [none]
  domain: subject-skill
  award: ["bachelor's with honours"]
  gradeOf: { statement: qaa/creative-writing-2024/4.4.b14, basis: inferred }
  paraphrase: "May be among the qualities, of which graduates at the excellent level will show some: writing that shows a transforming awareness of how change can support sustainability, or that opens new ways of seeing how humans, other beings and their habitats relate."
  quote: full   # the issuer's statement is in `source` (D-std-0014)
  audience: both
  subjects: inherited
- id: qaa/creative-writing-2024/4.5.b6
  locator: { number: "4.5.b6", headingPath: ["Benchmark standards", "Excellent level: Subject knowledge, understanding and skills"] }
  span: { start: 76040, end: 76120 }
  source: "writing which articulates new spaces for creative and entrepreneurial expression"
  stem: "4.5"
  statementType: excellent
  rung: excellent
  force: will
  level: fheq:6
  appliesTo: "graduates at the excellent level"
  addressee: learner
  verbs: ["articulates"]
  about: "new spaces for creative and entrepreneurial expression"
  themes: [none]
  domain: subject-skill
  award: ["bachelor's with honours"]
  gradeOf: none
  paraphrase: "May be among the qualities, of which graduates at the excellent level will show some: writing that opens new room for creative and entrepreneurial expression."
  quote: full   # the issuer's statement is in `source` (D-std-0014)
  audience: both
  subjects: inherited
- id: qaa/creative-writing-2024/4.5.b7
  locator: { number: "4.5.b7", headingPath: ["Benchmark standards", "Excellent level: Subject knowledge, understanding and skills"] }
  span: { start: 76123, end: 76340 }
  source: "writing which has critical impact and self-awareness and is highly self-reflective, in ways which sustain and develop critical connections between Creative Writing and interdisciplinary approaches to creative practice"
  stem: "4.5"
  statementType: excellent
  rung: excellent
  force: will
  level: fheq:6
  appliesTo: "graduates at the excellent level"
  addressee: learner
  verbs: ["sustain", "develop"]
  about: "critically impactful, self-reflective, interdisciplinary writing"
  themes: [none]
  domain: subject-skill
  award: ["bachelor's with honours"]
  gradeOf: { statement: qaa/creative-writing-2024/4.4.b2, basis: inferred }
  paraphrase: "May be among the qualities, of which graduates at the excellent level will show some: writing with critical force and self-awareness, deeply reflective, that builds and keeps up critical links between the subject and creative practice in other disciplines."
  quote: full   # the issuer's statement is in `source` (D-std-0014)
  audience: both
  subjects: inherited
- id: qaa/creative-writing-2024/4.5.b8
  locator: { number: "4.5.b8", headingPath: ["Benchmark standards", "Excellent level: Subject knowledge, understanding and skills"] }
  span: { start: 76343, end: 76489 }
  source: "writing that explores and uses the rich diversity of languages and dialects, representing regional, global and media-specific varieties and voices"
  stem: "4.5"
  statementType: excellent
  rung: excellent
  force: will
  level: fheq:6
  appliesTo: "graduates at the excellent level"
  addressee: learner
  verbs: ["explores", "uses"]
  about: "diversity of languages and dialects"
  themes: [none]
  domain: subject-skill
  award: ["bachelor's with honours"]
  gradeOf: none
  paraphrase: "May be among the qualities, of which graduates at the excellent level will show some: writing that draws on and explores the wide variety of languages and dialects, giving voice to regional, global and media-specific varieties."
  quote: full   # the issuer's statement is in `source` (D-std-0014)
  audience: both
  subjects: inherited
- id: qaa/creative-writing-2024/4.5.b9
  locator: { number: "4.5.b9", headingPath: ["Benchmark standards", "Excellent level: Subject knowledge, understanding and skills"] }
  span: { start: 76492, end: 76667 }
  source: "writing that demonstrates advanced co-production skills via editing, workshopping, collaborative, creative and/or engagement with communities of practice beyond the classroom."
  stem: "4.5"
  statementType: excellent
  rung: excellent
  force: will
  level: fheq:6
  appliesTo: "graduates at the excellent level"
  addressee: learner
  verbs: ["demonstrates"]
  about: "advanced co-production with communities of practice"
  themes: [none]
  domain: subject-skill
  award: ["bachelor's with honours"]
  gradeOf: { statement: qaa/creative-writing-2024/4.4.b17, basis: inferred }
  paraphrase: "May be among the qualities, of which graduates at the excellent level will show some: writing that shows advanced co-production through editing, workshops and collaboration, and work with communities of practice outside the classroom."
  quote: full   # the issuer's statement is in `source` (D-std-0014)
  audience: both
  subjects: inherited
- id: qaa/creative-writing-2024/4.6.b1
  locator: { number: "4.6.b1", headingPath: ["Benchmark standards", "Generic skills"] }
  span: { start: 76776, end: 76827 }
  source: "initiate and take responsibility for their own work"
  stem: "4.6"
  statementType: outcome
  rung: none
  force: should
  level: fheq:6
  appliesTo: "honours graduates of the subject"
  addressee: learner
  verbs: ["initiate", "take"]
  about: "initiative and responsibility for own work"
  themes: [none]
  domain: generic-skill
  award: ["bachelor's with honours"]
  gradeOf: none
  paraphrase: "On graduating with honours, students should be able to start their own work and answer for it."
  quote: full   # the issuer's statement is in `source` (D-std-0014)
  audience: both
  subjects: inherited
- id: qaa/creative-writing-2024/4.6.b2
  locator: { number: "4.6.b2", headingPath: ["Benchmark standards", "Generic skills"] }
  span: { start: 76830, end: 76900 }
  source: "present information to a professional standard, appropriate to context"
  stem: "4.6"
  statementType: outcome
  rung: none
  force: should
  level: fheq:6
  appliesTo: "honours graduates of the subject"
  addressee: learner
  verbs: ["present"]
  about: "professional presentation of information"
  themes: [none]
  domain: generic-skill
  award: ["bachelor's with honours"]
  gradeOf: none
  paraphrase: "On graduating with honours, students should be able to present information to a professional standard that suits the setting."
  quote: full   # the issuer's statement is in `source` (D-std-0014)
  audience: both
  subjects: inherited
- id: qaa/creative-writing-2024/4.6.b3
  locator: { number: "4.6.b3", headingPath: ["Benchmark standards", "Generic skills"] }
  span: { start: 76903, end: 77012 }
  source: "self-manage and show a distinct ability to work independently, set goals, manage workloads and meet deadlines"
  stem: "4.6"
  statementType: outcome
  rung: none
  force: should
  level: fheq:6
  appliesTo: "honours graduates of the subject"
  addressee: learner
  verbs: ["work", "set", "manage", "meet"]
  about: "self-management and independent work"
  themes: [none]
  domain: generic-skill
  award: ["bachelor's with honours"]
  gradeOf: none
  paraphrase: "On graduating with honours, students should be able to manage themselves, work independently, set goals, handle their workload and keep to deadlines."
  quote: full   # the issuer's statement is in `source` (D-std-0014)
  audience: both
  subjects: inherited
- id: qaa/creative-writing-2024/4.6.b4
  locator: { number: "4.6.b4", headingPath: ["Benchmark standards", "Generic skills"] }
  span: { start: 77015, end: 77116 }
  source: "anticipate and accommodate change, and negotiate contexts of ambiguity, uncertainty and unfamiliarity"
  stem: "4.6"
  statementType: outcome
  rung: none
  force: should
  level: fheq:6
  appliesTo: "honours graduates of the subject"
  addressee: learner
  verbs: ["anticipate", "accommodate", "negotiate"]
  about: "handling change and ambiguity"
  themes: [none]
  domain: generic-skill
  award: ["bachelor's with honours"]
  gradeOf: none
  paraphrase: "On graduating with honours, students should be able to foresee and adjust to change, and work through situations that are ambiguous, uncertain or unfamiliar."
  quote: full   # the issuer's statement is in `source` (D-std-0014)
  audience: both
  subjects: inherited
- id: qaa/creative-writing-2024/4.6.b5
  locator: { number: "4.6.b5", headingPath: ["Benchmark standards", "Generic skills"] }
  span: { start: 77119, end: 77185 }
  source: "identify strengths and needs in reflecting on personal development"
  stem: "4.6"
  statementType: outcome
  rung: none
  force: should
  level: fheq:6
  appliesTo: "honours graduates of the subject"
  addressee: learner
  verbs: ["identify", "reflecting"]
  about: "identifying strengths and needs through reflection"
  themes: [none]
  domain: generic-skill
  award: ["bachelor's with honours"]
  gradeOf: none
  paraphrase: "On graduating with honours, students should be able to identify strengths and development needs by reflecting on their personal growth."
  quote: full   # the issuer's statement is in `source` (D-std-0014)
  audience: both
  subjects: inherited
- id: qaa/creative-writing-2024/4.6.b6
  locator: { number: "4.6.b6", headingPath: ["Benchmark standards", "Generic skills"] }
  span: { start: 77188, end: 77355 }
  source: "select and employ communication and information technologies; source, navigate, select, retrieve, evaluate, manipulate and manage information from a variety of sources"
  stem: "4.6"
  statementType: outcome
  rung: none
  force: should
  level: fheq:6
  appliesTo: "honours graduates of the subject"
  addressee: learner
  verbs: ["select", "employ", "source", "navigate", "retrieve", "evaluate", "manipulate", "manage"]
  about: "information and communication technologies; managing information"
  themes: [none]
  domain: generic-skill
  award: ["bachelor's with honours"]
  gradeOf: none
  paraphrase: "On graduating with honours, students should be able to choose and use communication and information technologies, and find, sift, judge and manage information from many sources."
  quote: full   # the issuer's statement is in `source` (D-std-0014)
  audience: both
  subjects: inherited
- id: qaa/creative-writing-2024/4.6.b7
  locator: { number: "4.6.b7", headingPath: ["Benchmark standards", "Generic skills"] }
  span: { start: 77358, end: 77512 }
  source: "produce or narrate a factual story using transparent and/or persuasive language, drawing from their own experience and/or from accounts provided by others"
  stem: "4.6"
  statementType: outcome
  rung: none
  force: should
  level: fheq:6
  appliesTo: "honours graduates of the subject"
  addressee: learner
  verbs: ["produce", "narrate", "drawing"]
  about: "factual storytelling from own or others' accounts"
  themes: [none]
  domain: generic-skill
  award: ["bachelor's with honours"]
  gradeOf: none
  paraphrase: "On graduating with honours, students should be able to produce or tell a true story in clear or persuasive language, from their own experience or from other people's accounts."
  quote: full   # the issuer's statement is in `source` (D-std-0014)
  audience: both
  subjects: inherited
- id: qaa/creative-writing-2024/4.6.b8
  locator: { number: "4.6.b8", headingPath: ["Benchmark standards", "Generic skills"] }
  span: { start: 77515, end: 77568 }
  source: "work flexibly, both independently and collaboratively"
  stem: "4.6"
  statementType: outcome
  rung: none
  force: should
  level: fheq:6
  appliesTo: "honours graduates of the subject"
  addressee: learner
  verbs: ["work"]
  about: "flexible independent and collaborative work"
  themes: [none]
  domain: generic-skill
  award: ["bachelor's with honours"]
  gradeOf: none
  paraphrase: "On graduating with honours, students should be able to work adaptably, alone and with others."
  quote: full   # the issuer's statement is in `source` (D-std-0014)
  audience: both
  subjects: inherited
- id: qaa/creative-writing-2024/4.6.b9
  locator: { number: "4.6.b9", headingPath: ["Benchmark standards", "Generic skills"] }
  span: { start: 77575, end: 77670 }
  source: "demonstrate and actively use a wide range of transferable communication skills and story skills"
  stem: "4.6"
  statementType: outcome
  rung: none
  force: should
  level: fheq:6
  appliesTo: "honours graduates of the subject"
  addressee: learner
  verbs: ["demonstrate", "use"]
  about: "transferable communication and story skills"
  themes: [none]
  domain: generic-skill
  award: ["bachelor's with honours"]
  gradeOf: none
  paraphrase: "On graduating with honours, students should be able to show and put to active use many transferable communication and storytelling skills."
  quote: full   # the issuer's statement is in `source` (D-std-0014)
  audience: both
  subjects: inherited
- id: qaa/creative-writing-2024/4.6.b10
  locator: { number: "4.6.b10", headingPath: ["Benchmark standards", "Generic skills"] }
  span: { start: 77673, end: 77855 }
  source: "communicate their own ideas and the ideas of others concisely, accurately and persuasively to influence opinion, developing, constructing and presenting arguments in appropriate ways"
  stem: "4.6"
  statementType: outcome
  rung: none
  force: should
  level: fheq:6
  appliesTo: "honours graduates of the subject"
  addressee: learner
  verbs: ["communicate", "influence", "developing", "constructing", "presenting"]
  about: "concise, accurate, persuasive communication and argument"
  themes: [none]
  domain: generic-skill
  award: ["bachelor's with honours"]
  gradeOf: none
  paraphrase: "On graduating with honours, students should be able to put across their own and others' ideas briefly, accurately and persuasively so as to sway opinion, building and presenting arguments suitably."
  quote: full   # the issuer's statement is in `source` (D-std-0014)
  audience: both
  subjects: inherited
- id: qaa/creative-writing-2024/4.6.b11
  locator: { number: "4.6.b11", headingPath: ["Benchmark standards", "Generic skills"] }
  span: { start: 77858, end: 77927 }
  source: "develop skills in and understand the importance of listening actively"
  stem: "4.6"
  statementType: outcome
  rung: none
  force: should
  level: fheq:6
  appliesTo: "honours graduates of the subject"
  addressee: learner
  verbs: ["develop", "understand", "listening"]
  about: "active listening"
  themes: [none]
  domain: generic-skill
  award: ["bachelor's with honours"]
  gradeOf: none
  paraphrase: "On graduating with honours, students should be able to build the skill of listening actively and see why it matters."
  quote: full   # the issuer's statement is in `source` (D-std-0014)
  audience: both
  subjects: inherited
- id: qaa/creative-writing-2024/4.6.b12
  locator: { number: "4.6.b12", headingPath: ["Benchmark standards", "Generic skills"] }
  span: { start: 77930, end: 78044 }
  source: "communicate in a variety of media, with a strong awareness of the values and uses of story, narrative and language"
  stem: "4.6"
  statementType: outcome
  rung: none
  force: should
  level: fheq:6
  appliesTo: "honours graduates of the subject"
  addressee: learner
  verbs: ["communicate"]
  about: "communicating across media with awareness of story and language"
  themes: [none]
  domain: generic-skill
  award: ["bachelor's with honours"]
  gradeOf: none
  paraphrase: "On graduating with honours, students should be able to communicate in varied media with a strong sense of what story, narrative and language are for and how they work."
  quote: full   # the issuer's statement is in `source` (D-std-0014)
  audience: both
  subjects: inherited
- id: qaa/creative-writing-2024/4.6.b13
  locator: { number: "4.6.b13", headingPath: ["Benchmark standards", "Generic skills"] }
  span: { start: 78047, end: 78163 }
  source: "interact effectively with others, in team or group work, for example through collaboration or in workshop situations"
  stem: "4.6"
  statementType: outcome
  rung: none
  force: should
  level: fheq:6
  appliesTo: "honours graduates of the subject"
  addressee: learner
  verbs: ["interact"]
  about: "effective interaction in teams and workshops"
  themes: [none]
  domain: generic-skill
  award: ["bachelor's with honours"]
  gradeOf: none
  paraphrase: "On graduating with honours, students should be able to work well with others in teams or groups, for instance in collaboration or workshops."
  quote: full   # the issuer's statement is in `source` (D-std-0014)
  audience: both
  subjects: inherited
- id: qaa/creative-writing-2024/4.6.b14
  locator: { number: "4.6.b14", headingPath: ["Benchmark standards", "Generic skills"] }
  span: { start: 78166, end: 78260 }
  source: "demonstrate an understanding of equality, diversity and inclusivity (see paragraphs 1.21-1.24)"
  stem: "4.6"
  statementType: outcome
  rung: none
  force: should
  level: fheq:6
  appliesTo: "honours graduates of the subject"
  addressee: learner
  verbs: ["demonstrate"]
  about: "understanding equality, diversity and inclusivity"
  themes: [none]
  domain: generic-skill
  award: ["bachelor's with honours"]
  gradeOf: none
  paraphrase: "On graduating with honours, students should be able to show that they understand equality, diversity and inclusion."
  quote: full   # the issuer's statement is in `source` (D-std-0014)
  audience: both
  subjects: inherited
- id: qaa/creative-writing-2024/4.6.b15
  locator: { number: "4.6.b15", headingPath: ["Benchmark standards", "Generic skills"] }
  span: { start: 78263, end: 78425 }
  source: "adapt to different demands and tasks and be able to look beyond the immediate task to the wider context, including the social and commercial effects of their work"
  stem: "4.6"
  statementType: outcome
  rung: none
  force: should
  level: fheq:6
  appliesTo: "honours graduates of the subject"
  addressee: learner
  verbs: ["adapt", "look"]
  about: "adapting to demands; wider social and commercial effects"
  themes: [none]
  domain: generic-skill
  award: ["bachelor's with honours"]
  gradeOf: none
  paraphrase: "On graduating with honours, students should be able to adjust to varied demands and tasks and see past the task in hand to its wider setting, including what their work does socially and commercially."
  quote: full   # the issuer's statement is in `source` (D-std-0014)
  audience: both
  subjects: inherited
- id: qaa/creative-writing-2024/4.6.b16
  locator: { number: "4.6.b16", headingPath: ["Benchmark standards", "Generic skills"] }
  span: { start: 78428, end: 78483 }
  source: "appreciate the benefit of giving and receiving feedback"
  stem: "4.6"
  statementType: outcome
  rung: none
  force: should
  level: fheq:6
  appliesTo: "honours graduates of the subject"
  addressee: learner
  verbs: ["appreciate"]
  about: "value of giving and receiving feedback"
  themes: [none]
  domain: generic-skill
  award: ["bachelor's with honours"]
  gradeOf: none
  paraphrase: "On graduating with honours, students should be able to value giving feedback and receiving it."
  quote: full   # the issuer's statement is in `source` (D-std-0014)
  audience: both
  subjects: inherited
- id: qaa/creative-writing-2024/4.6.b17
  locator: { number: "4.6.b17", headingPath: ["Benchmark standards", "Generic skills"] }
  span: { start: 78486, end: 78584 }
  source: "evaluate and be self-reflective, able to critically reflect on their own practices and assumptions"
  stem: "4.6"
  statementType: outcome
  rung: none
  force: should
  level: fheq:6
  appliesTo: "honours graduates of the subject"
  addressee: learner
  verbs: ["evaluate", "reflect"]
  about: "critical self-reflection on practice and assumptions"
  themes: [none]
  domain: generic-skill
  award: ["bachelor's with honours"]
  gradeOf: none
  paraphrase: "On graduating with honours, students should be able to evaluate and reflect on themselves, critically examining their own practices and assumptions."
  quote: full   # the issuer's statement is in `source` (D-std-0014)
  audience: both
  subjects: inherited
- id: qaa/creative-writing-2024/4.6.b18
  locator: { number: "4.6.b18", headingPath: ["Benchmark standards", "Generic skills"] }
  span: { start: 78587, end: 78731 }
  source: "exhibit increased confidence in a wide range of life-enhancing skills related to the subject, such as confidence, expression and self-awareness."
  stem: "4.6"
  statementType: outcome
  rung: none
  force: should
  level: fheq:6
  appliesTo: "honours graduates of the subject"
  addressee: learner
  verbs: ["exhibit"]
  about: "confidence in life-enhancing skills"
  themes: [none]
  domain: generic-skill
  award: ["bachelor's with honours"]
  gradeOf: none
  paraphrase: "On graduating with honours, students should be able to show growing confidence in the wider personal skills the subject builds, for example self-expression and self-awareness."
  quote: full   # the issuer's statement is in `source` (D-std-0014)
  audience: both
  subjects: inherited
- id: qaa/creative-writing-2024/4.7.b1
  locator: { number: "4.7.b1", headingPath: ["Benchmark standards", "Master's level"] }
  span: { start: 78818, end: 78960 }
  source: "advanced creative and imaginative skills to support the effective conception, design, and production of a substantial Creative Writing project"
  stem: "4.7"
  statementType: outcome
  rung: none
  force: must   # D-std-0016: "required" read as must
  level: fheq:7
  appliesTo: "students achieving master's level"
  addressee: learner
  verbs: ["support"]
  about: "advanced creative skills for a substantial project"
  themes: [none]
  domain: subject-skill
  award: ["master's"]
  gradeOf: none
  paraphrase: "Students achieving master's level show advanced creative and imaginative skills that carry the conception, design and making of a substantial creative writing project."
  quote: full   # the issuer's statement is in `source` (D-std-0014)
  audience: both
  subjects: inherited
- id: qaa/creative-writing-2024/4.7.b2
  locator: { number: "4.7.b2", headingPath: ["Benchmark standards", "Master's level"] }
  span: { start: 78963, end: 79211 }
  source: "composite professional skills (managing self, time, writing independently and learning autonomously) required to deliver a substantial writing project in a way that demonstrates initiative and decision-making in complex and unpredictable situations"
  stem: "4.7"
  statementType: outcome
  rung: none
  force: must   # D-std-0016: "required" read as must
  level: fheq:7
  appliesTo: "students achieving master's level"
  addressee: learner
  verbs: ["managing", "writing", "learning", "required", "deliver", "demonstrates"]
  about: "composite professional skills for a substantial project"
  themes: [none]
  domain: generic-skill
  award: ["master's"]
  gradeOf: none
  paraphrase: "Students achieving master's level show combined professional skills, managing themselves and their time, writing independently and learning on their own, needed to complete a substantial project with initiative and sound decisions when things are complex and unpredictable."
  quote: full   # the issuer's statement is in `source` (D-std-0014)
  audience: both
  subjects: inherited
- id: qaa/creative-writing-2024/4.7.b3
  locator: { number: "4.7.b3", headingPath: ["Benchmark standards", "Master's level"] }
  span: { start: 79214, end: 79369 }
  source: "the ability to complete a substantial piece of Creative Writing of an appropriate length and/or form that constitutes an original contribution to its field"
  stem: "4.7"
  statementType: outcome
  rung: none
  force: must   # D-std-0016: "required" read as must
  level: fheq:7
  appliesTo: "students achieving master's level"
  addressee: learner
  verbs: ["complete", "constitutes"]
  about: "a substantial original piece of writing"
  themes: [none]
  domain: subject-skill
  award: ["master's"]
  gradeOf: none
  paraphrase: "Students achieving master's level show the completion of a large creative writing piece, of suitable length or form, that adds something original to its field."
  quote: full   # the issuer's statement is in `source` (D-std-0014)
  audience: both
  subjects: inherited
- id: qaa/creative-writing-2024/4.7.b4
  locator: { number: "4.7.b4", headingPath: ["Benchmark standards", "Master's level"] }
  span: { start: 79372, end: 79620 }
  source: "the ability to produce a critical piece of writing relating to the genesis and execution of their project, contextualising their work within an appropriate scholarly or creative tradition, and illuminating the original aspects of their contribution"
  stem: "4.7"
  statementType: outcome
  rung: none
  force: must   # D-std-0016: "required" read as must
  level: fheq:7
  appliesTo: "students achieving master's level"
  addressee: learner
  verbs: ["produce", "relating", "contextualising", "illuminating"]
  about: "critical writing on the project and its tradition"
  themes: [none]
  domain: subject-skill
  award: ["master's"]
  gradeOf: none
  paraphrase: "Students achieving master's level show a critical piece on how their project arose and was carried out, setting it within a fitting scholarly or creative tradition and making clear what is original in it."
  quote: full   # the issuer's statement is in `source` (D-std-0014)
  audience: both
  subjects: inherited
- id: qaa/creative-writing-2024/4.7.b5
  locator: { number: "4.7.b5", headingPath: ["Benchmark standards", "Master's level"] }
  span: { start: 79623, end: 79768 }
  source: "advanced analytical and imaginative skills as required to identify, define and resolve challenges arising from their professional writing project"
  stem: "4.7"
  statementType: outcome
  rung: none
  force: must   # D-std-0016: "required" read as must
  level: fheq:7
  appliesTo: "students achieving master's level"
  addressee: learner
  verbs: ["identify", "define", "resolve"]
  about: "analytical and imaginative problem-solving in a professional project"
  themes: [none]
  domain: subject-skill
  award: ["master's"]
  gradeOf: none
  paraphrase: "Students achieving master's level show advanced analytical and imaginative skills for spotting, defining and solving the problems a professional writing project throws up."
  quote: full   # the issuer's statement is in `source` (D-std-0014)
  audience: both
  subjects: inherited
- id: qaa/creative-writing-2024/4.7.b6
  locator: { number: "4.7.b6", headingPath: ["Benchmark standards", "Master's level"] }
  span: { start: 79771, end: 79924 }
  source: "an applied awareness of their own processes, influences and approaches to writing, enabling skilful adaptation to any creative challenge that might arise"
  stem: "4.7"
  statementType: outcome
  rung: none
  force: must   # D-std-0016: "required" read as must
  level: fheq:7
  appliesTo: "students achieving master's level"
  addressee: learner
  verbs: ["enabling"]
  about: "applied awareness of own process for adaptability"
  themes: [none]
  domain: understanding
  award: ["master's"]
  gradeOf: none
  paraphrase: "Students achieving master's level show a practical grasp of how they work as writers, what influences them and how they approach writing, so that they adapt skilfully to any creative challenge."
  quote: full   # the issuer's statement is in `source` (D-std-0014)
  audience: both
  subjects: inherited
- id: qaa/creative-writing-2024/4.7.b7
  locator: { number: "4.7.b7", headingPath: ["Benchmark standards", "Master's level"] }
  span: { start: 79927, end: 80000 }
  source: "the ability to carry out independent research in support of their project"
  stem: "4.7"
  statementType: outcome
  rung: none
  force: must   # D-std-0016: "required" read as must
  level: fheq:7
  appliesTo: "students achieving master's level"
  addressee: learner
  verbs: ["carry"]
  about: "independent research for the project"
  themes: [none]
  domain: subject-skill
  award: ["master's"]
  gradeOf: none
  paraphrase: "Students achieving master's level show the capacity to conduct their own research to support the project."
  quote: full   # the issuer's statement is in `source` (D-std-0014)
  audience: both
  subjects: inherited
- id: qaa/creative-writing-2024/4.7.b8
  locator: { number: "4.7.b8", headingPath: ["Benchmark standards", "Master's level"] }
  span: { start: 80003, end: 80244 }
  source: "advanced craft, editing and story skills to support the progressive development of their work, including the ability to respond to feedback from peers/tutors; and the confidence to form their own judgements about how to improve their project"
  stem: "4.7"
  statementType: outcome
  rung: none
  force: must   # D-std-0016: "required" read as must
  level: fheq:7
  appliesTo: "students achieving master's level"
  addressee: learner
  verbs: ["support", "respond", "form", "improve"]
  about: "advanced craft, editing and story skills; using feedback"
  themes: [none]
  domain: subject-skill
  award: ["master's"]
  gradeOf: none
  paraphrase: "Students achieving master's level show advanced craft, editing and storytelling skills that move the work forward, including acting on feedback from peers and tutors and the confidence to judge for themselves how to make the project better."
  quote: full   # the issuer's statement is in `source` (D-std-0014)
  audience: both
  subjects: inherited
- id: qaa/creative-writing-2024/4.7.b9
  locator: { number: "4.7.b9", headingPath: ["Benchmark standards", "Master's level"] }
  span: { start: 80247, end: 80379 }
  source: "the ability to engage in analytical and critical group discussion, applying problem- solving skills to the assessment of peer's work"
  stem: "4.7"
  statementType: outcome
  rung: none
  force: must   # D-std-0016: "required" read as must
  level: fheq:7
  appliesTo: "students achieving master's level"
  addressee: learner
  verbs: ["engage", "applying"]
  about: "analytical group discussion and problem-solving on peers' work"
  themes: [none]
  domain: generic-skill
  award: ["master's"]
  gradeOf: none
  paraphrase: "Students achieving master's level show the capacity to take part in analytical, critical group discussion, bringing problem-solving to bear on other writers' work."
  quote: full   # the issuer's statement is in `source` (D-std-0014)
  audience: both
  subjects: inherited
- id: qaa/creative-writing-2024/4.7.b10
  locator: { number: "4.7.b10", headingPath: ["Benchmark standards", "Master's level"] }
  span: { start: 80386, end: 80645 }
  source: "the ability to give feedback in a way that demonstrates sensitivity - exhibiting, for example, a strong awareness of what a writer is trying to achieve and considering the diversity of contexts and experiences that may influence perceptions of skilful writing"
  stem: "4.7"
  statementType: outcome
  rung: none
  force: must   # D-std-0016: "required" read as must
  level: fheq:7
  appliesTo: "students achieving master's level"
  addressee: learner
  verbs: ["give", "demonstrates", "exhibiting", "considering", "influence"]
  about: "sensitive feedback"
  themes: [none]
  domain: generic-skill
  award: ["master's"]
  gradeOf: none
  paraphrase: "Students achieving master's level show the capacity to give feedback with sensitivity, for instance by showing a keen sense of what the writer is aiming for and weighing how varied backgrounds and experiences shape judgements of good writing."
  quote: full   # the issuer's statement is in `source` (D-std-0014)
  audience: both
  subjects: inherited
- id: qaa/creative-writing-2024/4.7.b11
  locator: { number: "4.7.b11", headingPath: ["Benchmark standards", "Master's level"] }
  span: { start: 80648, end: 80820 }
  source: "skills in adapting writing styles to a range of media and narrative forms, considering the creative risks and benefits of technology as a creative and representational tool"
  stem: "4.7"
  statementType: outcome
  rung: none
  force: must   # D-std-0016: "required" read as must
  level: fheq:7
  appliesTo: "students achieving master's level"
  addressee: learner
  verbs: ["adapting", "considering"]
  about: "adapting style across media; technology as a creative tool"
  themes: [none]
  domain: subject-skill
  award: ["master's"]
  gradeOf: none
  paraphrase: "Students achieving master's level show skill in adjusting writing style to varied media and narrative forms, weighing the creative risks and gains of technology as a tool for making and representing."
  quote: full   # the issuer's statement is in `source` (D-std-0014)
  audience: both
  subjects: inherited
- id: qaa/creative-writing-2024/4.7.b12
  locator: { number: "4.7.b12", headingPath: ["Benchmark standards", "Master's level"] }
  span: { start: 80823, end: 81061 }
  source: "the ability to evaluate, discuss, adapt and position their work within the context of broader social challenges and contexts such as sustainable development, diversity and/or the ethics of using new technologies such as AI to develop work"
  stem: "4.7"
  statementType: outcome
  rung: none
  force: must   # D-std-0016: "required" read as must
  level: fheq:7
  appliesTo: "students achieving master's level"
  addressee: learner
  verbs: ["evaluate", "discuss", "adapt", "position", "using", "develop"]
  about: "positioning work within social challenges, including AI ethics"
  themes: [none]
  domain: subject-skill
  award: ["master's"]
  gradeOf: none
  paraphrase: "Students achieving master's level show the capacity to evaluate, discuss, adapt and place their work in relation to wider social challenges such as sustainable development, diversity or the ethics of making work with AI and other new technologies."
  quote: full   # the issuer's statement is in `source` (D-std-0014)
  audience: both
  subjects: inherited
- id: qaa/creative-writing-2024/4.7.b13
  locator: { number: "4.7.b13", headingPath: ["Benchmark standards", "Master's level"] }
  span: { start: 81064, end: 81514 }
  source: "the ability to transform complex cultural and sometimes emotionally challenging materials, observations and experiences into effective Creative Writing, applying relevant narrative and literary forms and techniques. This may include, for example, an exploration of the relationship between people and place through writing, in a way that transforms the audience's perception of how they see and experience other beings and the environment around them"
  stem: "4.7"
  statementType: outcome
  rung: none
  force: must   # D-std-0016: "required" read as must
  level: fheq:7
  appliesTo: "students achieving master's level"
  addressee: learner
  verbs: ["transform", "applying", "transforms"]
  about: "transforming complex and difficult material into effective writing"
  themes: [none]
  domain: subject-skill
  award: ["master's"]
  gradeOf: none
  paraphrase: "Students achieving master's level show the capacity to turn complex cultural material, and sometimes emotionally hard material, observation and experience, into effective creative writing with fitting narrative and literary forms and techniques, for example writing about people and place that changes how readers perceive other beings and their surroundings."
  quote: full   # the issuer's statement is in `source` (D-std-0014)
  audience: both
  subjects: inherited
- id: qaa/creative-writing-2024/4.7.b14
  locator: { number: "4.7.b14", headingPath: ["Benchmark standards", "Master's level"] }
  span: { start: 81517, end: 81667 }
  source: "advanced teamworking skills, demonstrating the ability to respond to rapidly changing cultural industries, professional challenges and global contexts"
  stem: "4.7"
  statementType: outcome
  rung: none
  force: must   # D-std-0016: "required" read as must
  level: fheq:7
  appliesTo: "students achieving master's level"
  addressee: learner
  verbs: ["demonstrating", "respond"]
  about: "advanced teamwork in changing cultural industries"
  themes: [none]
  domain: generic-skill
  award: ["master's"]
  gradeOf: none
  paraphrase: "Students achieving master's level show advanced teamwork, showing they can respond to fast-moving cultural industries, to professional challenges and to global contexts."
  quote: full   # the issuer's statement is in `source` (D-std-0014)
  audience: both
  subjects: inherited
- id: qaa/creative-writing-2024/4.7.b15
  locator: { number: "4.7.b15", headingPath: ["Benchmark standards", "Master's level"] }
  span: { start: 81670, end: 81821 }
  source: "the ability to communicate effectively to specialist and non-specialist audiences, demonstrated through advanced writing, speaking and narrative skills"
  stem: "4.7"
  statementType: outcome
  rung: none
  force: must   # D-std-0016: "required" read as must
  level: fheq:7
  appliesTo: "students achieving master's level"
  addressee: learner
  verbs: ["communicate", "demonstrated"]
  about: "communicating to specialist and non-specialist audiences"
  themes: [none]
  domain: generic-skill
  award: ["master's"]
  gradeOf: none
  paraphrase: "Students achieving master's level show the capacity to communicate well with specialists and non-specialists, shown through advanced writing, speaking and storytelling."
  quote: full   # the issuer's statement is in `source` (D-std-0014)
  audience: both
  subjects: inherited
- id: qaa/creative-writing-2024/4.7.b16
  locator: { number: "4.7.b16", headingPath: ["Benchmark standards", "Master's level"] }
  span: { start: 81824, end: 82023 }
  source: "the ability to apply an understanding of the values and uses of Creative Writing as a life-enhancing skill to improve both their own and others’ well-being, confidence, expression and self-awareness."
  stem: "4.7"
  statementType: outcome
  rung: none
  force: must   # D-std-0016: "required" read as must
  level: fheq:7
  appliesTo: "students achieving master's level"
  addressee: learner
  verbs: ["apply", "improve"]
  about: "writing as a life-enhancing skill for well-being"
  themes: [none]
  domain: generic-skill
  award: ["master's"]
  gradeOf: none
  paraphrase: "Students achieving master's level show the capacity to draw on their grasp of how creative writing can enrich lives to help themselves and others gain well-being, confidence, self-expression and self-awareness."
  quote: full   # the issuer's statement is in `source` (D-std-0014)
  audience: both
  subjects: inherited
```

### S4a Audience versions
<!-- label: both; status: drafted; basis: primary. forPractitioner: for the programme designer or teacher. forBeneficiary: for the student, second person, naming no issuer. author-agent-written: instructions to an AI agent writing about the statement (a course document, a handbook, an outcome, a report). author-agent-dialogue: instructions to an AI agent using the statement in conversation (with a student, a teacher or a programme team). Written fresh from the held text alone (benchmark rule 6; Abbott, 15:42). -->
```yaml
- statement: qaa/creative-writing-2024/1.20
  forPractitioner: { text: "Build regular peer feedback into teaching and actively encourage students to use it to get better at offering and receiving critique that is both useful and kind.", rewrite: light, force: should, status: drafted }
  forBeneficiary: { text: "not-applicable: a duty on the course to encourage; the student-facing skill is in 4.4.b16 and 4.6.b16", rewrite: full, force: should, status: drafted }
  author-agent-written: "Treat this as a should-level expectation on the course, not a student outcome: courses should encourage students to use peer feedback to improve how they give and take it. It holds for the honours degree at every stage. Cite it as QAA (2024), Creative Writing Subject Benchmark Statement, para 1.20. Do not claim it is a requirement or a graduate standard; set it beside 4.4.b16 and 4.6.b16, which state the feedback skills graduates show, and beside the level 6 descriptor qaa/fheq-2024/4.15.b8."
  author-agent-dialogue: "Raise it with a programme team planning workshops or reviewing how feedback is taught. For staff, put it as a design expectation and ask: 'Where in each year do students practise giving feedback, and how do you know they are improving at it?' With a student, do not present it as a rule they must meet; talk instead about the feedback skills in 4.4.b16."
- statement: qaa/creative-writing-2024/1.31
  forPractitioner: { text: "Workshops are valuable but not accessible by default: prepare them in advance so that disabled students, neurodivergent students and those with long-term mental health conditions can take full part, and weigh the critiques of the workshop model when designing them.", rewrite: light, force: must, status: drafted }
  forBeneficiary: { text: "not-applicable: a duty on the course and its tutors; the student meets its effect, not a standard to reach", rewrite: full, force: must, status: drafted }
  author-agent-written: "Treat this as a requirement on the course under the accessibility theme (the issuer's word is 'required', recorded as must): workshops need further preparation so that every student can take part. It applies to provision for the honours degree, not to a level of attainment. Cite it as QAA (2024), Creative Writing Subject Benchmark Statement, para 1.31. Do not present it as a legal duty in its own right or as a student outcome; set it beside 1.30, 3.17 and 3.22 on accessible materials, workshops and assessment."
  author-agent-dialogue: "Raise it with tutors or a programme team who run workshops, especially when planning a new module or responding to a student's support plan. Frame it for staff and ask: 'What does a student who cannot read aloud, or who finds the room overwhelming, do in your workshop?' Do not give it to a student as something they must achieve; if a student raises access to workshops, point to the adjustments it implies."
- statement: qaa/creative-writing-2024/2.2.b1
  forPractitioner: { text: "Students will, through the course, develop experienced use of the expressive, imaginative and emotional resources of language and story, structure and form included; make it visible in modules and assessment.", rewrite: light, force: will, status: drafted }
  forBeneficiary: { text: "Through your studies you will become practised in what language and story can do expressively, imaginatively and emotionally, including structure and form.", rewrite: full, force: will, status: drafted }
  author-agent-written: "Describe this as an outcome the statement says students will reach through study of the subject (force will), for the honours degree at FHEQ level 6 and FQHEIS level 10 (level inferred: the list sits under Design, before the levels are named in 2.3): the resources of language and story. Cite it as QAA (2024), Creative Writing Subject Benchmark Statement, para 2.2, bullet 1. Do not treat it as a rung of section 4 or as a regulatory requirement; set it beside 4.4.b6 and 4.3.b5 and the FHEQ level 6 descriptor qaa/fheq-2024/4.15.b2 (FQHEIS level 10, std:doc:qaa-fqheis-2024-framework 4.16; spine:6)."
  author-agent-dialogue: "Raise this when a student asks what the course will make them good at. To a student, put it plainly in the second person as something the course will build; to staff, frame it as an outcome to make visible across modules. Ask: 'Which resource of language do you rely on most, and which least?' Avoid reading the list aloud or presenting the item as a pass hurdle."
- statement: qaa/creative-writing-2024/2.2.b2
  forPractitioner: { text: "Students will, through the course, develop an understanding of text, narrative and language as materials for art, with their past traditions and possible uses; make it visible in modules and assessment.", rewrite: light, force: will, status: drafted }
  forBeneficiary: { text: "Through your studies you will understand text, narrative and language as materials for art, each with its own history and possible uses.", rewrite: full, force: will, status: drafted }
  author-agent-written: "Describe this as an outcome the statement says students will reach through study of the subject (force will), for the honours degree at FHEQ level 6 and FQHEIS level 10 (level inferred: the list sits under Design, before the levels are named in 2.3): text, narrative and language as artistic materials. Cite it as QAA (2024), Creative Writing Subject Benchmark Statement, para 2.2, bullet 2. Do not treat it as a rung of section 4 or as a regulatory requirement; set it beside 4.3.b7 and 4.4.b10 and the FHEQ level 6 descriptor qaa/fheq-2024/4.15.b1 (FQHEIS level 10, std:doc:qaa-fqheis-2024-framework 4.16; spine:6)."
  author-agent-dialogue: "Raise this when a student treats language only as a vehicle for content. To a student, put it plainly in the second person as something the course will build; to staff, frame it as an outcome to make visible across modules. Ask: 'If language is your material, what are you shaping in this piece?' Avoid reading the list aloud or presenting the item as a pass hurdle."
- statement: qaa/creative-writing-2024/2.2.b3
  forPractitioner: { text: "Students will, through the course, develop recognition of the many ways audiences respond to and read their work; make it visible in modules and assessment.", rewrite: light, force: will, status: drafted }
  forBeneficiary: { text: "Through your studies you will recognise the many ways readers and audiences may respond to and interpret your work.", rewrite: full, force: will, status: drafted }
  author-agent-written: "Describe this as an outcome the statement says students will reach through study of the subject (force will), for the honours degree at FHEQ level 6 and FQHEIS level 10 (level inferred: the list sits under Design, before the levels are named in 2.3): audience responses to own work. Cite it as QAA (2024), Creative Writing Subject Benchmark Statement, para 2.2, bullet 3. Do not treat it as a rung of section 4 or as a regulatory requirement; set it beside 4.3.b8 and 4.4.b12 and the FHEQ level 6 descriptor qaa/fheq-2024/4.15.b4 (FQHEIS level 10, std:doc:qaa-fqheis-2024-framework 4.16; spine:6)."
  author-agent-dialogue: "Raise this when a student is surprised by how readers took a piece. To a student, put it plainly in the second person as something the course will build; to staff, frame it as an outcome to make visible across modules. Ask: 'How did your readers' responses differ from what you intended?' Avoid reading the list aloud or presenting the item as a pass hurdle."
- statement: qaa/creative-writing-2024/2.2.b4
  forPractitioner: { text: "Students will, through the course, develop growth in critical insight and in the capacity to use it; make it visible in modules and assessment.", rewrite: light, force: will, status: drafted }
  forBeneficiary: { text: "Through your studies you will develop critical insight and the capacity to use it.", rewrite: full, force: will, status: drafted }
  author-agent-written: "Describe this as an outcome the statement says students will reach through study of the subject (force will), for the honours degree at FHEQ level 6 and FQHEIS level 10 (level inferred: the list sits under Design, before the levels are named in 2.3): critical insight and capability. Cite it as QAA (2024), Creative Writing Subject Benchmark Statement, para 2.2, bullet 4. Do not treat it as a rung of section 4 or as a regulatory requirement; set it beside 4.4.b2 and 4.6.b17 and the FHEQ level 6 descriptor qaa/fheq-2024/4.15.b7 (FQHEIS level 10, std:doc:qaa-fqheis-2024-framework 4.16; spine:6)."
  author-agent-dialogue: "Raise this when a student asks how critical work fits a creative degree. To a student, put it plainly in the second person as something the course will build; to staff, frame it as an outcome to make visible across modules. Ask: 'What has critical reading shown you about your own writing?' Avoid reading the list aloud or presenting the item as a pass hurdle."
- statement: qaa/creative-writing-2024/2.2.b5
  forPractitioner: { text: "Students will, through the course, develop ownership of their own work from first idea through development and editing to the last redraft; make it visible in modules and assessment.", rewrite: light, force: will, status: drafted }
  forBeneficiary: { text: "Through your studies you will take responsibility for your own work, from the first idea through development and editing to the last draft.", rewrite: full, force: will, status: drafted }
  author-agent-written: "Describe this as an outcome the statement says students will reach through study of the subject (force will), for the honours degree at FHEQ level 6 and FQHEIS level 10 (level inferred: the list sits under Design, before the levels are named in 2.3): responsibility for own work from idea to final draft. Cite it as QAA (2024), Creative Writing Subject Benchmark Statement, para 2.2, bullet 5. Do not treat it as a rung of section 4 or as a regulatory requirement; set it beside 4.6.b1 and 4.7.b2 and the FHEQ level 6 descriptor qaa/fheq-2024/4.15.b9.1 (FQHEIS level 10, std:doc:qaa-fqheis-2024-framework 4.16; spine:6)."
  author-agent-dialogue: "Raise this when a student relies on tutors to decide when a piece is finished. To a student, put it plainly in the second person as something the course will build; to staff, frame it as an outcome to make visible across modules. Ask: 'How do you decide a piece is ready?' Avoid reading the list aloud or presenting the item as a pass hurdle."
- statement: qaa/creative-writing-2024/2.2.b6
  forPractitioner: { text: "Students will, through the course, develop practice in editing work through repeated drafts, on their own and with tutors and other students through peer review, and a grasp of why it matters; make it visible in modules and assessment.", rewrite: light, force: will, status: drafted }
  forBeneficiary: { text: "Through your studies you will practise editing your work over many drafts, on your own and with tutors and classmates, and see why it matters.", rewrite: full, force: will, status: drafted }
  author-agent-written: "Describe this as an outcome the statement says students will reach through study of the subject (force will), for the honours degree at FHEQ level 6 and FQHEIS level 10 (level inferred: the list sits under Design, before the levels are named in 2.3): editing over successive drafts, alone and with peers. Cite it as QAA (2024), Creative Writing Subject Benchmark Statement, para 2.2, bullet 6. Do not treat it as a rung of section 4 or as a regulatory requirement; set it beside 4.3.b1 and 4.4.b16 and the FHEQ level 6 descriptor qaa/fheq-2024/4.15.b2 (FQHEIS level 10, std:doc:qaa-fqheis-2024-framework 4.16; spine:6)."
  author-agent-dialogue: "Raise this when a student wants to submit a first draft. To a student, put it plainly in the second person as something the course will build; to staff, frame it as an outcome to make visible across modules. Ask: 'What changed between your second and third drafts, and who helped?' Avoid reading the list aloud or presenting the item as a pass hurdle."
- statement: qaa/creative-writing-2024/2.2.b7
  forPractitioner: { text: "Students will, through the course, develop an appreciation of the many creative and cultural settings in which writing is made and read; make it visible in modules and assessment.", rewrite: light, force: will, status: drafted }
  forBeneficiary: { text: "Through your studies you will appreciate the many creative and cultural settings in which writing is made and read.", rewrite: full, force: will, status: drafted }
  author-agent-written: "Describe this as an outcome the statement says students will reach through study of the subject (force will), for the honours degree at FHEQ level 6 and FQHEIS level 10 (level inferred: the list sits under Design, before the levels are named in 2.3): creative and cultural contexts of writing. Cite it as QAA (2024), Creative Writing Subject Benchmark Statement, para 2.2, bullet 7. Do not treat it as a rung of section 4 or as a regulatory requirement; set it beside 4.3.b7 and 4.4.b10 and the FHEQ level 6 descriptor qaa/fheq-2024/4.15.b1 (FQHEIS level 10, std:doc:qaa-fqheis-2024-framework 4.16; spine:6)."
  author-agent-dialogue: "Raise this when a student considers where their work might be published or performed. To a student, put it plainly in the second person as something the course will build; to staff, frame it as an outcome to make visible across modules. Ask: 'Where does writing like yours get made and read, and who decides?' Avoid reading the list aloud or presenting the item as a pass hurdle."
- statement: qaa/creative-writing-2024/2.3
  forPractitioner: { text: "Plan each level so that it builds knowledge, expertise and experience towards the threshold subject-specific and generic skills in 4.3 and 4.6; students will normally progress by completing, and earning credit for, all learning and assessment, practical work included.", rewrite: light, force: will, status: drafted }
  forBeneficiary: { text: "As you move up through the levels of your degree, you will build knowledge, skill and experience towards the minimum subject and general skills for honours, usually by passing and gaining credit for all your learning and assessment, practical work included.", rewrite: full, force: will, status: drafted }
  author-agent-written: "Describe this as the statement's account of progression (force will) through the honours degree, which it places at FHEQ level 6 and FQHEIS level 10. Cite it as QAA (2024), Creative Writing Subject Benchmark Statement, para 2.3. Do not claim it sets progression rules, which stay with each institution, or that it fixes what each lower level contains; set it beside 4.3 and 4.6 (the threshold it builds towards), 3.5 to 3.7 (content by level) and spine:4 to spine:6 in std:ref:uk-framework."
  author-agent-dialogue: "Raise it when a student or programme team asks how the years of the degree fit together or what each level is for. To a student, say plainly that each year builds towards the minimum skills for the degree; to staff, frame it as a design check on the curriculum map. Ask: 'Which of the threshold skills does each year of your course start, and which does it finish?' Avoid presenting the statement as the source of progression rules."
- statement: qaa/creative-writing-2024/2.7
  forPractitioner: { text: "In joint and combined degrees, make sure students will reach the core of the subject-specific and generic skills, let the partner subject add its own and use the overlap for interdisciplinary work.", rewrite: light, force: will, status: drafted }
  forBeneficiary: { text: "If you study creative writing as part of a joint or combined degree, you will gain the core subject and general skills, add others from your other subject and may explore where the two meet.", rewrite: full, force: will, status: drafted }
  author-agent-written: "Describe this as an outcome (force will) for joint and combined honours students: the core of the subject's specific and generic skills, at FHEQ level 6. Cite it as QAA (2024), Creative Writing Subject Benchmark Statement, para 2.7. Do not claim that a joint honours student must meet every item in 4.3 to 4.6, since the issuer says core elements only and does not name them; set it beside 4.3, 4.6 and the FHEQ level 6 descriptor qaa/fheq-2024/4.15.b1 (FQHEIS level 10, std:doc:qaa-fqheis-2024-framework 4.16; spine:6)."
  author-agent-dialogue: "Raise it when a joint or combined honours student, or a team designing such a course, asks what the writing half must cover. To a student, say that you will gain the core of the subject's skills and add others from your other subject; to staff, ask: 'Which of the threshold items does the writing half carry, and which does the other subject?' Avoid implying that the student must match a single honours student item for item."
- statement: qaa/creative-writing-2024/3.22
  forPractitioner: { text: "Make every assessment accessible, offer alternative assessments where a student's access needs call for them and publish the extension, late submission and extenuating circumstances policies in terms every student can find and follow.", rewrite: light, force: should, status: drafted }
  forBeneficiary: { text: "not-applicable: a duty on the course; the student meets its effect, not a standard to reach", rewrite: full, force: should, status: drafted }
  author-agent-written: "Treat this as a set of should-level expectations on the course: accessible assessment, alternative assessments for access needs and clear policies on extensions and late work. It applies to provision for the honours degree, not to a level of attainment. Cite it as QAA (2024), Creative Writing Subject Benchmark Statement, para 3.22. Do not present it as a student outcome or as a legal duty in itself; set it beside 1.31 and 3.17 on accessible workshops and 3.28 on clear criteria."
  author-agent-dialogue: "Raise it with a programme team reviewing assessment or responding to a student's access needs. For staff, frame it as a design and policy check and ask: 'If a student cannot do this assessment as set, what is the alternative and who decides?' With a student who raises an access need or a late submission, point to the course policies it expects; do not give it to them as a standard to meet."
- statement: qaa/creative-writing-2024/4.2
  forPractitioner: { text: "Expect most students to go well past the threshold; when setting how achievement above it is evidenced and classified, refer to Annex D's descriptions of first, upper second, lower second and third-class honours.", rewrite: light, force: should, status: drafted }
  forBeneficiary: { text: "not-applicable: a duty on the provider in judging classification; the student-facing rungs are 4.3 to 4.5", rewrite: full, force: should, status: drafted }
  author-agent-written: "Treat this as a should-level expectation on the provider: in judging achievement above threshold, refer to Annex D of the FHEQ (std:doc:qaa-fheq-2024-framework, Annex D, qaa/fheq-2024/annex-d/summary/r1/1st to 3rd). It holds for the honours degree at FHEQ level 6 and FQHEIS level 10. Cite it as QAA (2024), Creative Writing Subject Benchmark Statement, para 4.2. Do not claim that the typical or excellent rungs map one to one onto classes; set it beside 4.3, 4.4 and 4.5."
  author-agent-dialogue: "Raise it with a programme team or examiners setting marking criteria or classification rules. Frame it for staff and ask: 'How do your criteria for a first or a 2.1 draw on Annex D and on the typical and excellent rungs?' Avoid telling a student that a rung equals a class; with a student, talk about the rungs themselves."
- statement: qaa/creative-writing-2024/4.3.b1
  forPractitioner: { text: "At threshold, every honours graduate will have shown the capacity to produce creative writing and improve it through editing and redrafting; make sure every passing student can evidence it.", rewrite: light, force: threshold, status: drafted }
  forBeneficiary: { text: "As a minimum for your honours degree, you will produce your own creative writing and improve it by editing and redrafting.", rewrite: full, force: threshold, status: drafted }
  author-agent-written: "Describe this as a threshold outcome: the least an honours graduate in the subject will have shown (FHEQ level 6, FQHEIS level 10), here generating work and developing it by revision. Cite it as QAA (2024), Creative Writing Subject Benchmark Statement, para 4.3, bullet 1. Do not present it as a regulatory requirement or as where most students end, since 4.2 expects most to do clearly better. Set it beside 4.4.b1 and 4.6.b1 and the FHEQ level 6 descriptor qaa/fheq-2024/4.15.b2 (FQHEIS level 10, std:doc:qaa-fqheis-2024-framework 4.16; spine:6)."
  author-agent-dialogue: "Raise this when a student asks what the minimum is for a portfolio or how much redrafting counts. To a student, say in plain second-person words that this is the floor for the honours degree, not the target; to staff, frame it as the minimum a module's assessment must let every passing student show. Ask: 'Which piece have you taken through more than one draft, and what changed between versions?' Avoid reading the issuer's list aloud or treating this minimum as all a student should aim for."
- statement: qaa/creative-writing-2024/4.3.b2
  forPractitioner: { text: "At threshold, every honours graduate will have shown the capacity to think back over how they write and what they produce; make sure every passing student can evidence it.", rewrite: light, force: threshold, status: drafted }
  forBeneficiary: { text: "As a minimum for your honours degree, you will think back over how you write and what you produce.", rewrite: full, force: threshold, status: drafted }
  author-agent-written: "Describe this as a threshold outcome: the least an honours graduate in the subject will have shown (FHEQ level 6, FQHEIS level 10), here reflection on own creative process and outputs. Cite it as QAA (2024), Creative Writing Subject Benchmark Statement, para 4.3, bullet 2. Do not present it as a regulatory requirement or as where most students end, since 4.2 expects most to do clearly better. Set it beside 4.4.b2, 4.5.b7 and 4.6.b17 and the FHEQ level 6 descriptor qaa/fheq-2024/4.15.b7 (FQHEIS level 10, std:doc:qaa-fqheis-2024-framework 4.16; spine:6)."
  author-agent-dialogue: "Raise this when a student is preparing a reflective commentary or learning journal. To a student, say in plain second-person words that this is the floor for the honours degree, not the target; to staff, frame it as the minimum a module's assessment must let every passing student show. Ask: 'What did you learn about your own way of working from your last piece?' Avoid reading the issuer's list aloud or treating this minimum as all a student should aim for."
- statement: qaa/creative-writing-2024/4.3.b3
  forPractitioner: { text: "At threshold, every honours graduate will have shown active engagement with the interests that drive their writing and with the writers and works that shape it; make sure every passing student can evidence it.", rewrite: light, force: threshold, status: drafted }
  forBeneficiary: { text: "As a minimum for your honours degree, you will engage actively with what interests you as a writer and with the writers and works that influence you.", rewrite: full, force: threshold, status: drafted }
  author-agent-written: "Describe this as a threshold outcome: the least an honours graduate in the subject will have shown (FHEQ level 6, FQHEIS level 10), here engagement with own creative interests and influences. Cite it as QAA (2024), Creative Writing Subject Benchmark Statement, para 4.3, bullet 3. Do not present it as a regulatory requirement or as where most students end, since 4.2 expects most to do clearly better. Set it beside 4.4.b3 and 4.4.b8 and the FHEQ level 6 descriptor qaa/fheq-2024/4.15.b5 (FQHEIS level 10, std:doc:qaa-fqheis-2024-framework 4.16; spine:6)."
  author-agent-dialogue: "Raise this when a student is unsure what to write about or whose work to read. To a student, say in plain second-person words that this is the floor for the honours degree, not the target; to staff, frame it as the minimum a module's assessment must let every passing student show. Ask: 'Which writers or works have shaped your recent writing, and how can you tell?' Avoid reading the issuer's list aloud or treating this minimum as all a student should aim for."
- statement: qaa/creative-writing-2024/4.3.b4
  forPractitioner: { text: "At threshold, every honours graduate will have shown a beginning awareness of a range of craft and storytelling techniques; make sure every passing student can evidence it.", rewrite: light, force: threshold, status: drafted }
  forBeneficiary: { text: "As a minimum for your honours degree, you will be starting to recognise a range of craft and storytelling techniques.", rewrite: full, force: threshold, status: drafted }
  author-agent-written: "Describe this as a threshold outcome: the least an honours graduate in the subject will have shown (FHEQ level 6, FQHEIS level 10), here early awareness of craft and narrative techniques. Cite it as QAA (2024), Creative Writing Subject Benchmark Statement, para 4.3, bullet 4. Do not present it as a regulatory requirement or as where most students end, since 4.2 expects most to do clearly better. Set it beside 4.4.b1 and 4.4.b4 and the FHEQ level 6 descriptor qaa/fheq-2024/4.15.b1 (FQHEIS level 10, std:doc:qaa-fqheis-2024-framework 4.16; spine:6)."
  author-agent-dialogue: "Raise this when a student asks what technical knowledge the course expects. To a student, say in plain second-person words that this is the floor for the honours degree, not the target; to staff, frame it as the minimum a module's assessment must let every passing student show. Ask: 'Name two techniques you used on purpose in your last piece: what did each do?' Avoid reading the issuer's list aloud or treating this minimum as all a student should aim for."
- statement: qaa/creative-writing-2024/4.3.b5
  forPractitioner: { text: "At threshold, every honours graduate will have shown awareness of how written and spoken language works across forms, genres and media, with its rules, its conventions and what it makes possible; make sure every passing student can evidence it.", rewrite: light, force: threshold, status: drafted }
  forBeneficiary: { text: "As a minimum for your honours degree, you will know how written and spoken language works across different forms, genres and media, including its rules, its conventions and what it lets you do.", rewrite: full, force: threshold, status: drafted }
  author-agent-written: "Describe this as a threshold outcome: the least an honours graduate in the subject will have shown (FHEQ level 6, FQHEIS level 10), here awareness of the rules and possibilities of written and spoken language. Cite it as QAA (2024), Creative Writing Subject Benchmark Statement, para 4.3, bullet 5. Do not present it as a regulatory requirement or as where most students end, since 4.2 expects most to do clearly better. Set it beside 4.4.b5 and 2.2.b1 and the FHEQ level 6 descriptor qaa/fheq-2024/4.15.b1 (FQHEIS level 10, std:doc:qaa-fqheis-2024-framework 4.16; spine:6)."
  author-agent-dialogue: "Raise this when a student is moving between page, performance and screen forms. To a student, say in plain second-person words that this is the floor for the honours degree, not the target; to staff, frame it as the minimum a module's assessment must let every passing student show. Ask: 'What changes when a piece written for the page is read aloud or adapted for screen?' Avoid reading the issuer's list aloud or treating this minimum as all a student should aim for."
- statement: qaa/creative-writing-2024/4.3.b6
  forPractitioner: { text: "At threshold, every honours graduate will have shown the capacity to read published writing and drafts in progress and to respond to them; make sure every passing student can evidence it.", rewrite: light, force: threshold, status: drafted }
  forBeneficiary: { text: "As a minimum for your honours degree, you will read both published writing and drafts in progress, and respond to them.", rewrite: full, force: threshold, status: drafted }
  author-agent-written: "Describe this as a threshold outcome: the least an honours graduate in the subject will have shown (FHEQ level 6, FQHEIS level 10), here reading and responding to published and draft work. Cite it as QAA (2024), Creative Writing Subject Benchmark Statement, para 4.3, bullet 6. Do not present it as a regulatory requirement or as where most students end, since 4.2 expects most to do clearly better. Set it beside 4.4.b9 and the FHEQ level 6 descriptor qaa/fheq-2024/4.15.b7 (FQHEIS level 10, std:doc:qaa-fqheis-2024-framework 4.16; spine:6)."
  author-agent-dialogue: "Raise this when a student prepares for a workshop or a critical response. To a student, say in plain second-person words that this is the floor for the honours degree, not the target; to staff, frame it as the minimum a module's assessment must let every passing student show. Ask: 'When you read a classmate's draft, what do you look for first?' Avoid reading the issuer's list aloud or treating this minimum as all a student should aim for."
- statement: qaa/creative-writing-2024/4.3.b7
  forPractitioner: { text: "At threshold, every honours graduate will have shown awareness of the history and culture behind how language is used and literature made, storytelling and changing technologies included; make sure every passing student can evidence it.", rewrite: light, force: threshold, status: drafted }
  forBeneficiary: { text: "As a minimum for your honours degree, you will understand the history and culture behind how language is used and literature is made, including storytelling and changing technologies.", rewrite: full, force: threshold, status: drafted }
  author-agent-written: "Describe this as a threshold outcome: the least an honours graduate in the subject will have shown (FHEQ level 6, FQHEIS level 10), here historical and cultural dimensions of language and literature. Cite it as QAA (2024), Creative Writing Subject Benchmark Statement, para 4.3, bullet 7. Do not present it as a regulatory requirement or as where most students end, since 4.2 expects most to do clearly better. Set it beside 4.4.b10 and 2.2.b7 and the FHEQ level 6 descriptor qaa/fheq-2024/4.15.b1 (FQHEIS level 10, std:doc:qaa-fqheis-2024-framework 4.16; spine:6)."
  author-agent-dialogue: "Raise this when a student asks why historical or contextual reading matters to a writer. To a student, say in plain second-person words that this is the floor for the honours degree, not the target; to staff, frame it as the minimum a module's assessment must let every passing student show. Ask: 'How has a change in technology altered the way stories are told in a form you write in?' Avoid reading the issuer's list aloud or treating this minimum as all a student should aim for."
- statement: qaa/creative-writing-2024/4.3.b8
  forPractitioner: { text: "At threshold, every honours graduate will have shown the capacity to reach varied audiences through a range of narrative forms, digital tools and media; make sure every passing student can evidence it.", rewrite: light, force: threshold, status: drafted }
  forBeneficiary: { text: "As a minimum for your honours degree, you will communicate with different audiences, using a range of narrative forms, digital tools and media.", rewrite: full, force: threshold, status: drafted }
  author-agent-written: "Describe this as a threshold outcome: the least an honours graduate in the subject will have shown (FHEQ level 6, FQHEIS level 10), here communicating to diverse audiences across forms and media. Cite it as QAA (2024), Creative Writing Subject Benchmark Statement, para 4.3, bullet 8. Do not present it as a regulatory requirement or as where most students end, since 4.2 expects most to do clearly better. Set it beside 4.4.b13 and 4.5.b2 and the FHEQ level 6 descriptor qaa/fheq-2024/4.15.b8 (FQHEIS level 10, std:doc:qaa-fqheis-2024-framework 4.16; spine:6)."
  author-agent-dialogue: "Raise this when a student plans a piece for a particular readership or platform. To a student, say in plain second-person words that this is the floor for the honours degree, not the target; to staff, frame it as the minimum a module's assessment must let every passing student show. Ask: 'Who is this piece for, and what would you change to reach a different audience?' Avoid reading the issuer's list aloud or treating this minimum as all a student should aim for."
- statement: qaa/creative-writing-2024/4.3.b9
  forPractitioner: { text: "At threshold, every honours graduate will have shown awareness of what effective group work needs, with openness and a commitment to inclusion; make sure every passing student can evidence it.", rewrite: light, force: threshold, status: drafted }
  forBeneficiary: { text: "As a minimum for your honours degree, you will know what it takes to work well in a group, and be open and committed to including everyone.", rewrite: full, force: threshold, status: drafted }
  author-agent-written: "Describe this as a threshold outcome: the least an honours graduate in the subject will have shown (FHEQ level 6, FQHEIS level 10), here awareness of group work skills and inclusivity. Cite it as QAA (2024), Creative Writing Subject Benchmark Statement, para 4.3, bullet 9. Do not present it as a regulatory requirement or as where most students end, since 4.2 expects most to do clearly better. Set it beside 4.4.b15, 4.6.b13 and 4.6.b14 and the FHEQ level 6 descriptor qaa/fheq-2024/4.15.b9.1 (FQHEIS level 10, std:doc:qaa-fqheis-2024-framework 4.16; spine:6)."
  author-agent-dialogue: "Raise this when a student prepares for a workshop or a group project. To a student, say in plain second-person words that this is the floor for the honours degree, not the target; to staff, frame it as the minimum a module's assessment must let every passing student show. Ask: 'What helps a writing group work well for everyone in it?' Avoid reading the issuer's list aloud or treating this minimum as all a student should aim for."
- statement: qaa/creative-writing-2024/4.3.b10
  forPractitioner: { text: "At threshold, every honours graduate will have shown awareness of how the subject's skills apply in varied settings, careers and enterprises; make sure every passing student can evidence it.", rewrite: light, force: threshold, status: drafted }
  forBeneficiary: { text: "As a minimum for your honours degree, you will know how your writing skills can be used in different settings, careers and ventures of your own.", rewrite: full, force: threshold, status: drafted }
  author-agent-written: "Describe this as a threshold outcome: the least an honours graduate in the subject will have shown (FHEQ level 6, FQHEIS level 10), here applications of writing skills to careers and enterprise. Cite it as QAA (2024), Creative Writing Subject Benchmark Statement, para 4.3, bullet 10. Do not present it as a regulatory requirement or as where most students end, since 4.2 expects most to do clearly better. Set it beside 4.4.b19 and 4.5.b6 and the FHEQ level 6 descriptor qaa/fheq-2024/4.15.b9.3 (FQHEIS level 10, std:doc:qaa-fqheis-2024-framework 4.16; spine:6)."
  author-agent-dialogue: "Raise this when a student asks what the degree leads to. To a student, say in plain second-person words that this is the floor for the honours degree, not the target; to staff, frame it as the minimum a module's assessment must let every passing student show. Ask: 'Which two kinds of work could use the skills you are building, and how?' Avoid reading the issuer's list aloud or treating this minimum as all a student should aim for."
- statement: qaa/creative-writing-2024/4.3.b11
  forPractitioner: { text: "At threshold, every honours graduate will have shown awareness of what creative writing can contribute to sustainability and environmental questions; make sure every passing student can evidence it.", rewrite: light, force: threshold, status: drafted }
  forBeneficiary: { text: "As a minimum for your honours degree, you will understand what creative writing can contribute to sustainability and to environmental questions.", rewrite: full, force: threshold, status: drafted }
  author-agent-written: "Describe this as a threshold outcome: the least an honours graduate in the subject will have shown (FHEQ level 6, FQHEIS level 10), here the subject's contribution to sustainability. Cite it as QAA (2024), Creative Writing Subject Benchmark Statement, para 4.3, bullet 11. Do not present it as a regulatory requirement or as where most students end, since 4.2 expects most to do clearly better. Set it beside 4.4.b14 and 4.5.b5 and the FHEQ level 6 descriptor qaa/fheq-2024/4.15.b1 (FQHEIS level 10, std:doc:qaa-fqheis-2024-framework 4.16; spine:6)."
  author-agent-dialogue: "Raise this when a student is drawn to nature or climate writing, or asks how writing bears on sustainability. To a student, say in plain second-person words that this is the floor for the honours degree, not the target; to staff, frame it as the minimum a module's assessment must let every passing student show. Ask: 'How could a story or poem change how a reader thinks about the environment?' Avoid reading the issuer's list aloud or treating this minimum as all a student should aim for."
- statement: qaa/creative-writing-2024/4.3.b12
  forPractitioner: { text: "At threshold, every honours graduate will have shown an understanding of the forms that prose, poetry, story and drama take; make sure every passing student can evidence it.", rewrite: light, force: threshold, status: drafted }
  forBeneficiary: { text: "As a minimum for your honours degree, you will understand the forms of prose, poetry, story and drama.", rewrite: full, force: threshold, status: drafted }
  author-agent-written: "Describe this as a threshold outcome: the least an honours graduate in the subject will have shown (FHEQ level 6, FQHEIS level 10), here forms of prose, poetry, story and drama. Cite it as QAA (2024), Creative Writing Subject Benchmark Statement, para 4.3, bullet 12. Do not present it as a regulatory requirement or as where most students end, since 4.2 expects most to do clearly better. Set it beside 4.4.b4 and 4.3.b4 and the FHEQ level 6 descriptor qaa/fheq-2024/4.15.b1 (FQHEIS level 10, std:doc:qaa-fqheis-2024-framework 4.16; spine:6)."
  author-agent-dialogue: "Raise this when a student chooses forms to work in or asks what forms they need to know. To a student, say in plain second-person words that this is the floor for the honours degree, not the target; to staff, frame it as the minimum a module's assessment must let every passing student show. Ask: 'Which form are you least familiar with, and what defines it?' Avoid reading the issuer's list aloud or treating this minimum as all a student should aim for."
- statement: qaa/creative-writing-2024/4.3.b13
  forPractitioner: { text: "At threshold, every honours graduate will have shown the capacity to try out and work within a range of genres, such as memoir, short fiction, crime or fantasy; make sure every passing student can evidence it.", rewrite: light, force: threshold, status: drafted }
  forBeneficiary: { text: "As a minimum for your honours degree, you will try out and work in a range of genres, from memoir and short fiction to crime, fantasy or writing for young readers.", rewrite: full, force: threshold, status: drafted }
  author-agent-written: "Describe this as a threshold outcome: the least an honours graduate in the subject will have shown (FHEQ level 6, FQHEIS level 10), here exploring a range of genres. Cite it as QAA (2024), Creative Writing Subject Benchmark Statement, para 4.3, bullet 13. Do not present it as a regulatory requirement or as where most students end, since 4.2 expects most to do clearly better. Set it beside 4.5.b1 and the FHEQ level 6 descriptor qaa/fheq-2024/4.15.b2 (FQHEIS level 10, std:doc:qaa-fqheis-2024-framework 4.16; spine:6)."
  author-agent-dialogue: "Raise this when a student has written in one genre only. To a student, say in plain second-person words that this is the floor for the honours degree, not the target; to staff, frame it as the minimum a module's assessment must let every passing student show. Ask: 'Which genre have you not yet tried, and what might it teach you?' Avoid reading the issuer's list aloud or treating this minimum as all a student should aim for."
- statement: qaa/creative-writing-2024/4.4.b1
  forPractitioner: { text: "At the typical level, most honours graduates will have shown the capacity to conceive, produce and develop original creative writing, drawing on many editing, presentation, narrative and craft techniques; design teaching so that most students reach it.", rewrite: light, force: will, status: drafted }
  forBeneficiary: { text: "At the typical level for your honours degree, you will conceive, produce and develop original writing, drawing on many editing, presentation, storytelling and craft techniques.", rewrite: full, force: will, status: drafted }
  author-agent-written: "Describe this as a typical outcome: what most honours graduates in the subject will have shown, above the threshold, at FHEQ level 6 (FQHEIS level 10): conceiving and developing original work with many techniques. Cite it as QAA (2024), Creative Writing Subject Benchmark Statement, para 4.4, bullet 1. Do not claim it is the pass requirement or a regulatory standard; the threshold list in 4.3 is the minimum. Set it beside 4.3.b1, the FHEQ level 6 descriptor qaa/fheq-2024/4.15.b2 (FQHEIS level 10, std:doc:qaa-fqheis-2024-framework 4.16; spine:6) and Annex D's upper second band (qaa/fheq-2024/annex-d/summary/r1/2.1)."
  author-agent-dialogue: "Raise this when a student wants to know what good, not just passing, work looks like. To a student, put it plainly in the second person as what most people show by the end of the honours degree, not the minimum; to staff, frame it as the profile a module should help most students reach. Ask: 'Which techniques did you choose for this piece, and why those?' Avoid presenting it as the pass mark or reading the list aloud."
- statement: qaa/creative-writing-2024/4.4.b2
  forPractitioner: { text: "At the typical level, most honours graduates will have shown a reflective approach to writing that includes critical evaluation of their own practice; design teaching so that most students reach it.", rewrite: light, force: will, status: drafted }
  forBeneficiary: { text: "At the typical level for your honours degree, you will reflect on how you compose and evaluate your writing practice critically.", rewrite: full, force: will, status: drafted }
  author-agent-written: "Describe this as a typical outcome: what most honours graduates in the subject will have shown, above the threshold, at FHEQ level 6 (FQHEIS level 10): reflective, critically evaluative approach to composition. Cite it as QAA (2024), Creative Writing Subject Benchmark Statement, para 4.4, bullet 2. Do not claim it is the pass requirement or a regulatory standard; the threshold list in 4.3 is the minimum. Set it beside 4.3.b2 and 4.5.b7, the FHEQ level 6 descriptor qaa/fheq-2024/4.15.b7 (FQHEIS level 10, std:doc:qaa-fqheis-2024-framework 4.16; spine:6) and Annex D's upper second band (qaa/fheq-2024/annex-d/summary/r1/2.1)."
  author-agent-dialogue: "Raise this when a student writes a critical commentary. To a student, put it plainly in the second person as what most people show by the end of the honours degree, not the minimum; to staff, frame it as the profile a module should help most students reach. Ask: 'Where does your commentary judge your choices, rather than only describe them?' Avoid presenting it as the pass mark or reading the list aloud."
- statement: qaa/creative-writing-2024/4.4.b3
  forPractitioner: { text: "At the typical level, most honours graduates will have shown active exploration of how their reading relates to their own writing; design teaching so that most students reach it.", rewrite: light, force: will, status: drafted }
  forBeneficiary: { text: "At the typical level for your honours degree, you will explore actively how what you read relates to what you write.", rewrite: full, force: will, status: drafted }
  author-agent-written: "Describe this as a typical outcome: what most honours graduates in the subject will have shown, above the threshold, at FHEQ level 6 (FQHEIS level 10): relationships between reading and own practice. Cite it as QAA (2024), Creative Writing Subject Benchmark Statement, para 4.4, bullet 3. Do not claim it is the pass requirement or a regulatory standard; the threshold list in 4.3 is the minimum. Set it beside 4.3.b3 and 4.4.b8, the FHEQ level 6 descriptor qaa/fheq-2024/4.15.b5 (FQHEIS level 10, std:doc:qaa-fqheis-2024-framework 4.16; spine:6) and Annex D's upper second band (qaa/fheq-2024/annex-d/summary/r1/2.1)."
  author-agent-dialogue: "Raise this when a student builds a reading list or writes about influences. To a student, put it plainly in the second person as what most people show by the end of the honours degree, not the minimum; to staff, frame it as the profile a module should help most students reach. Ask: 'What have you read this term that changed something in your own writing?' Avoid presenting it as the pass mark or reading the list aloud."
- statement: qaa/creative-writing-2024/4.4.b4
  forPractitioner: { text: "At the typical level, most honours graduates will have shown the capacity to write a story, poem or prose piece that works; design teaching so that most students reach it.", rewrite: light, force: will, status: drafted }
  forBeneficiary: { text: "At the typical level for your honours degree, you will write a story, poem or prose piece that works well.", rewrite: full, force: will, status: drafted }
  author-agent-written: "Describe this as a typical outcome: what most honours graduates in the subject will have shown, above the threshold, at FHEQ level 6 (FQHEIS level 10): composing a story, poem or prose piece. Cite it as QAA (2024), Creative Writing Subject Benchmark Statement, para 4.4, bullet 4. Do not claim it is the pass requirement or a regulatory standard; the threshold list in 4.3 is the minimum. Set it beside 4.3.b12, the FHEQ level 6 descriptor qaa/fheq-2024/4.15.b2 (FQHEIS level 10, std:doc:qaa-fqheis-2024-framework 4.16; spine:6) and Annex D's upper second band (qaa/fheq-2024/annex-d/summary/r1/2.1)."
  author-agent-dialogue: "Raise this when a student submits a finished piece. To a student, put it plainly in the second person as what most people show by the end of the honours degree, not the minimum; to staff, frame it as the profile a module should help most students reach. Ask: 'What makes this piece complete, and what would you still change?' Avoid presenting it as the pass mark or reading the list aloud."
- statement: qaa/creative-writing-2024/4.4.b5
  forPractitioner: { text: "At the typical level, most honours graduates will have shown the capacity to use the conventions of written and spoken language, and what it makes possible, across forms, genres and new media; design teaching so that most students reach it.", rewrite: light, force: will, status: drafted }
  forBeneficiary: { text: "At the typical level for your honours degree, you will use the conventions of written and spoken language, and what it makes possible, across forms, genres and new media.", rewrite: full, force: will, status: drafted }
  author-agent-written: "Describe this as a typical outcome: what most honours graduates in the subject will have shown, above the threshold, at FHEQ level 6 (FQHEIS level 10): using the conventions and possibilities of language in emerging media. Cite it as QAA (2024), Creative Writing Subject Benchmark Statement, para 4.4, bullet 5. Do not claim it is the pass requirement or a regulatory standard; the threshold list in 4.3 is the minimum. Set it beside 4.3.b5, the FHEQ level 6 descriptor qaa/fheq-2024/4.15.b2 (FQHEIS level 10, std:doc:qaa-fqheis-2024-framework 4.16; spine:6) and Annex D's upper second band (qaa/fheq-2024/annex-d/summary/r1/2.1)."
  author-agent-dialogue: "Raise this when a student adapts work between page, stage, audio or digital media. To a student, put it plainly in the second person as what most people show by the end of the honours degree, not the minimum; to staff, frame it as the profile a module should help most students reach. Ask: 'Which convention did you bend on purpose, and what did it gain you?' Avoid presenting it as the pass mark or reading the list aloud."
- statement: qaa/creative-writing-2024/4.4.b6
  forPractitioner: { text: "At the typical level, most honours graduates will have shown a creative and discerning engagement with what written and spoken language can do expressively, poetically and in narrative; design teaching so that most students reach it.", rewrite: light, force: will, status: drafted }
  forBeneficiary: { text: "At the typical level for your honours degree, you will engage creatively and with discernment with what written and spoken language can do: its expressive, poetic and storytelling power.", rewrite: full, force: will, status: drafted }
  author-agent-written: "Describe this as a typical outcome: what most honours graduates in the subject will have shown, above the threshold, at FHEQ level 6 (FQHEIS level 10): creative, discerning engagement with what language can do. Cite it as QAA (2024), Creative Writing Subject Benchmark Statement, para 4.4, bullet 6. Do not claim it is the pass requirement or a regulatory standard; the threshold list in 4.3 is the minimum. Set it beside 4.5.b3 and 2.2.b1, the FHEQ level 6 descriptor qaa/fheq-2024/4.15.b7 (FQHEIS level 10, std:doc:qaa-fqheis-2024-framework 4.16; spine:6) and Annex D's upper second band (qaa/fheq-2024/annex-d/summary/r1/2.1)."
  author-agent-dialogue: "Raise this when a student works on voice, imagery or sound in their writing. To a student, put it plainly in the second person as what most people show by the end of the honours degree, not the minimum; to staff, frame it as the profile a module should help most students reach. Ask: 'Which line in your draft does the most work, and how?' Avoid presenting it as the pass mark or reading the list aloud."
- statement: qaa/creative-writing-2024/4.4.b7
  forPractitioner: { text: "At the typical level, most honours graduates will have shown independent, disciplined commitment to their own writing; design teaching so that most students reach it.", rewrite: light, force: will, status: drafted }
  forBeneficiary: { text: "At the typical level for your honours degree, you will commit to your own writing independently and with discipline.", rewrite: full, force: will, status: drafted }
  author-agent-written: "Describe this as a typical outcome: what most honours graduates in the subject will have shown, above the threshold, at FHEQ level 6 (FQHEIS level 10): independent, disciplined commitment to writing. Cite it as QAA (2024), Creative Writing Subject Benchmark Statement, para 4.4, bullet 7. Do not claim it is the pass requirement or a regulatory standard; the threshold list in 4.3 is the minimum. Set it beside 4.6.b1 and 4.6.b3, the FHEQ level 6 descriptor qaa/fheq-2024/4.15.b9.1 (FQHEIS level 10, std:doc:qaa-fqheis-2024-framework 4.16; spine:6) and Annex D's upper second band (qaa/fheq-2024/annex-d/summary/r1/2.1)."
  author-agent-dialogue: "Raise this when a student struggles with routine or deadlines. To a student, put it plainly in the second person as what most people show by the end of the honours degree, not the minimum; to staff, frame it as the profile a module should help most students reach. Ask: 'What writing routine do you keep when no deadline is close?' Avoid presenting it as the pass mark or reading the list aloud."
- statement: qaa/creative-writing-2024/4.4.b8
  forPractitioner: { text: "At the typical level, most honours graduates will have shown an understanding of how reading connects to their own writing practice; design teaching so that most students reach it.", rewrite: light, force: will, status: drafted }
  forBeneficiary: { text: "At the typical level for your honours degree, you will understand how your reading connects to your own writing.", rewrite: full, force: will, status: drafted }
  author-agent-written: "Describe this as a typical outcome: what most honours graduates in the subject will have shown, above the threshold, at FHEQ level 6 (FQHEIS level 10): understanding the link between reading and own practice. Cite it as QAA (2024), Creative Writing Subject Benchmark Statement, para 4.4, bullet 8. Do not claim it is the pass requirement or a regulatory standard; the threshold list in 4.3 is the minimum. Set it beside 4.4.b3 and 4.3.b3, the FHEQ level 6 descriptor qaa/fheq-2024/4.15.b5 (FQHEIS level 10, std:doc:qaa-fqheis-2024-framework 4.16; spine:6) and Annex D's upper second band (qaa/fheq-2024/annex-d/summary/r1/2.1)."
  author-agent-dialogue: "Raise this when a student asks why a writing course asks them to read so much. To a student, put it plainly in the second person as what most people show by the end of the honours degree, not the minimum; to staff, frame it as the profile a module should help most students reach. Ask: 'How does what you read show up in what you write?' Avoid presenting it as the pass mark or reading the list aloud."
- statement: qaa/creative-writing-2024/4.4.b9
  forPractitioner: { text: "At the typical level, most honours graduates will have shown the capacity to read published writing and drafts in progress and to answer them critically, creatively and practically; design teaching so that most students reach it.", rewrite: light, force: will, status: drafted }
  forBeneficiary: { text: "At the typical level for your honours degree, you will read published writing and drafts in progress and answer them critically, creatively and practically.", rewrite: full, force: will, status: drafted }
  author-agent-written: "Describe this as a typical outcome: what most honours graduates in the subject will have shown, above the threshold, at FHEQ level 6 (FQHEIS level 10): critical, creative and practical response to published and draft work. Cite it as QAA (2024), Creative Writing Subject Benchmark Statement, para 4.4, bullet 9. Do not claim it is the pass requirement or a regulatory standard; the threshold list in 4.3 is the minimum. Set it beside 4.3.b6 and 4.4.b16, the FHEQ level 6 descriptor qaa/fheq-2024/4.15.b7 (FQHEIS level 10, std:doc:qaa-fqheis-2024-framework 4.16; spine:6) and Annex D's upper second band (qaa/fheq-2024/annex-d/summary/r1/2.1)."
  author-agent-dialogue: "Raise this when a student gives workshop feedback or writes a critical response. To a student, put it plainly in the second person as what most people show by the end of the honours degree, not the minimum; to staff, frame it as the profile a module should help most students reach. Ask: 'What practical change would you suggest to this draft, and why?' Avoid presenting it as the pass mark or reading the list aloud."
- statement: qaa/creative-writing-2024/4.4.b10
  forPractitioner: { text: "At the typical level, most honours graduates will have shown an understanding of the history and the social and cultural setting of language use, from older ways of making texts to divergent kinds of story and new digital and media technologies; design teaching so that most students reach it.", rewrite: light, force: will, status: drafted }
  forBeneficiary: { text: "At the typical level for your honours degree, you will understand the history and the social and cultural setting of language, from older ways of making texts to different kinds of story and new digital media.", rewrite: full, force: will, status: drafted }
  author-agent-written: "Describe this as a typical outcome: what most honours graduates in the subject will have shown, above the threshold, at FHEQ level 6 (FQHEIS level 10): historical and socio-cultural dimensions of language and story. Cite it as QAA (2024), Creative Writing Subject Benchmark Statement, para 4.4, bullet 10. Do not claim it is the pass requirement or a regulatory standard; the threshold list in 4.3 is the minimum. Set it beside 4.3.b7 and 2.2.b7, the FHEQ level 6 descriptor qaa/fheq-2024/4.15.b1 (FQHEIS level 10, std:doc:qaa-fqheis-2024-framework 4.16; spine:6) and Annex D's upper second band (qaa/fheq-2024/annex-d/summary/r1/2.1)."
  author-agent-dialogue: "Raise this when a student studies the contexts of a form or writes for new media. To a student, put it plainly in the second person as what most people show by the end of the honours degree, not the minimum; to staff, frame it as the profile a module should help most students reach. Ask: 'How did the way this form was produced in the past shape what it became?' Avoid presenting it as the pass mark or reading the list aloud."
- statement: qaa/creative-writing-2024/4.4.b11
  forPractitioner: { text: "At the typical level, most honours graduates will have shown the capacity to place their own writing within a given historical, cultural or genre framework; design teaching so that most students reach it.", rewrite: light, force: will, status: drafted }
  forBeneficiary: { text: "At the typical level for your honours degree, you will place your own writing within a historical, cultural or genre setting.", rewrite: full, force: will, status: drafted }
  author-agent-written: "Describe this as a typical outcome: what most honours graduates in the subject will have shown, above the threshold, at FHEQ level 6 (FQHEIS level 10): placing own writing in historical, cultural or generic frameworks. Cite it as QAA (2024), Creative Writing Subject Benchmark Statement, para 4.4, bullet 11. Do not claim it is the pass requirement or a regulatory standard; the threshold list in 4.3 is the minimum. Set it beside 4.7.b4, the FHEQ level 6 descriptor qaa/fheq-2024/4.15.b3.1 (FQHEIS level 10, std:doc:qaa-fqheis-2024-framework 4.16; spine:6) and Annex D's upper second band (qaa/fheq-2024/annex-d/summary/r1/2.1)."
  author-agent-dialogue: "Raise this when a student writes a critical commentary or preface. To a student, put it plainly in the second person as what most people show by the end of the honours degree, not the minimum; to staff, frame it as the profile a module should help most students reach. Ask: 'Which tradition does your piece belong to, and where does it depart from it?' Avoid presenting it as the pass mark or reading the list aloud."
- statement: qaa/creative-writing-2024/4.4.b12
  forPractitioner: { text: "At the typical level, most honours graduates will have shown an understanding of writing as a narrative means of expression and communication that serves varied audiences and purposes; design teaching so that most students reach it.", rewrite: light, force: will, status: drafted }
  forBeneficiary: { text: "At the typical level for your honours degree, you will understand writing as a way of telling and communicating that serves different audiences and purposes.", rewrite: full, force: will, status: drafted }
  author-agent-written: "Describe this as a typical outcome: what most honours graduates in the subject will have shown, above the threshold, at FHEQ level 6 (FQHEIS level 10): writing as narrative expression for diverse audiences and purposes. Cite it as QAA (2024), Creative Writing Subject Benchmark Statement, para 4.4, bullet 12. Do not claim it is the pass requirement or a regulatory standard; the threshold list in 4.3 is the minimum. Set it beside 4.4.b13 and 2.2.b3, the FHEQ level 6 descriptor qaa/fheq-2024/4.15.b8 (FQHEIS level 10, std:doc:qaa-fqheis-2024-framework 4.16; spine:6) and Annex D's upper second band (qaa/fheq-2024/annex-d/summary/r1/2.1)."
  author-agent-dialogue: "Raise this when a student asks why audience and purpose matter in creative work. To a student, put it plainly in the second person as what most people show by the end of the honours degree, not the minimum; to staff, frame it as the profile a module should help most students reach. Ask: 'What is this piece trying to do for its reader?' Avoid presenting it as the pass mark or reading the list aloud."
- statement: qaa/creative-writing-2024/4.4.b13
  forPractitioner: { text: "At the typical level, most honours graduates will have shown the capacity to communicate with varied audiences through many narrative forms, story skills and media; design teaching so that most students reach it.", rewrite: light, force: will, status: drafted }
  forBeneficiary: { text: "At the typical level for your honours degree, you will communicate with different audiences through many narrative forms, storytelling skills and media.", rewrite: full, force: will, status: drafted }
  author-agent-written: "Describe this as a typical outcome: what most honours graduates in the subject will have shown, above the threshold, at FHEQ level 6 (FQHEIS level 10): communicating with diverse audiences across many forms and media. Cite it as QAA (2024), Creative Writing Subject Benchmark Statement, para 4.4, bullet 13. Do not claim it is the pass requirement or a regulatory standard; the threshold list in 4.3 is the minimum. Set it beside 4.3.b8 and 4.5.b2, the FHEQ level 6 descriptor qaa/fheq-2024/4.15.b8 (FQHEIS level 10, std:doc:qaa-fqheis-2024-framework 4.16; spine:6) and Annex D's upper second band (qaa/fheq-2024/annex-d/summary/r1/2.1)."
  author-agent-dialogue: "Raise this when a student adapts a piece for a new platform or readership. To a student, put it plainly in the second person as what most people show by the end of the honours degree, not the minimum; to staff, frame it as the profile a module should help most students reach. Ask: 'How would you retell this piece for an audience unlike you?' Avoid presenting it as the pass mark or reading the list aloud."
- statement: qaa/creative-writing-2024/4.4.b14
  forPractitioner: { text: "At the typical level, most honours graduates will have shown the capacity to explore imaginatively place, planet, climate, habitat, sustainability or the lives of other species; design teaching so that most students reach it.", rewrite: light, force: will, status: drafted }
  forBeneficiary: { text: "At the typical level for your honours degree, you will explore in your writing places, the planet, climate, habitats, sustainability or the lives of other species.", rewrite: full, force: will, status: drafted }
  author-agent-written: "Describe this as a typical outcome: what most honours graduates in the subject will have shown, above the threshold, at FHEQ level 6 (FQHEIS level 10): imaginative exploration of place, planet and other species. Cite it as QAA (2024), Creative Writing Subject Benchmark Statement, para 4.4, bullet 14. Do not claim it is the pass requirement or a regulatory standard; the threshold list in 4.3 is the minimum. Set it beside 4.3.b11 and 4.5.b5, the FHEQ level 6 descriptor qaa/fheq-2024/4.15.b6 (FQHEIS level 10, std:doc:qaa-fqheis-2024-framework 4.16; spine:6) and Annex D's upper second band (qaa/fheq-2024/annex-d/summary/r1/2.1)."
  author-agent-dialogue: "Raise this when a student takes up nature, place or climate writing. To a student, put it plainly in the second person as what most people show by the end of the honours degree, not the minimum; to staff, frame it as the profile a module should help most students reach. Ask: 'What does your setting do in the story beyond being a backdrop?' Avoid presenting it as the pass mark or reading the list aloud."
- statement: qaa/creative-writing-2024/4.4.b15
  forPractitioner: { text: "At the typical level, most honours graduates will have shown the capacity to work well with different voices and varied groups of writers to strengthen their own and others' writing; design teaching so that most students reach it.", rewrite: light, force: will, status: drafted }
  forBeneficiary: { text: "At the typical level for your honours degree, you will work well with writers whose voices and backgrounds differ from yours, so that your writing and theirs gets better.", rewrite: full, force: will, status: drafted }
  author-agent-written: "Describe this as a typical outcome: what most honours graduates in the subject will have shown, above the threshold, at FHEQ level 6 (FQHEIS level 10): engaging with diverse writers to improve own and others' work. Cite it as QAA (2024), Creative Writing Subject Benchmark Statement, para 4.4, bullet 15. Do not claim it is the pass requirement or a regulatory standard; the threshold list in 4.3 is the minimum. Set it beside 4.3.b9 and 4.6.b14, the FHEQ level 6 descriptor qaa/fheq-2024/4.15.b9.1 (FQHEIS level 10, std:doc:qaa-fqheis-2024-framework 4.16; spine:6) and Annex D's upper second band (qaa/fheq-2024/annex-d/summary/r1/2.1)."
  author-agent-dialogue: "Raise this when a student works in a mixed workshop group. To a student, put it plainly in the second person as what most people show by the end of the honours degree, not the minimum; to staff, frame it as the profile a module should help most students reach. Ask: 'Whose perspective in your workshop has most changed your writing?' Avoid presenting it as the pass mark or reading the list aloud."
- statement: qaa/creative-writing-2024/4.4.b16
  forPractitioner: { text: "At the typical level, most honours graduates will have shown skill in taking and giving constructive feedback on their own work and their peers'; design teaching so that most students reach it.", rewrite: light, force: will, status: drafted }
  forBeneficiary: { text: "At the typical level for your honours degree, you will give useful feedback to others and take feedback on your own work constructively.", rewrite: full, force: will, status: drafted }
  author-agent-written: "Describe this as a typical outcome: what most honours graduates in the subject will have shown, above the threshold, at FHEQ level 6 (FQHEIS level 10): giving and receiving feedback constructively. Cite it as QAA (2024), Creative Writing Subject Benchmark Statement, para 4.4, bullet 16. Do not claim it is the pass requirement or a regulatory standard; the threshold list in 4.3 is the minimum. Set it beside 4.6.b16, 4.7.b10 and 4.4.b9, the FHEQ level 6 descriptor qaa/fheq-2024/4.15.b8 (FQHEIS level 10, std:doc:qaa-fqheis-2024-framework 4.16; spine:6) and Annex D's upper second band (qaa/fheq-2024/annex-d/summary/r1/2.1)."
  author-agent-dialogue: "Raise this when a student is nervous about workshops. To a student, put it plainly in the second person as what most people show by the end of the honours degree, not the minimum; to staff, frame it as the profile a module should help most students reach. Ask: 'What feedback have you acted on recently, what did you set aside, and why?' Avoid presenting it as the pass mark or reading the list aloud."
- statement: qaa/creative-writing-2024/4.4.b17
  forPractitioner: { text: "At the typical level, most honours graduates will have shown co-writing skills and techniques that bring a shared creative vision to life; design teaching so that most students reach it.", rewrite: light, force: will, status: drafted }
  forBeneficiary: { text: "At the typical level for your honours degree, you will write with others, using skills and techniques that bring a shared vision to life.", rewrite: full, force: will, status: drafted }
  author-agent-written: "Describe this as a typical outcome: what most honours graduates in the subject will have shown, above the threshold, at FHEQ level 6 (FQHEIS level 10): co-authoring for a shared vision. Cite it as QAA (2024), Creative Writing Subject Benchmark Statement, para 4.4, bullet 17. Do not claim it is the pass requirement or a regulatory standard; the threshold list in 4.3 is the minimum. Set it beside 4.5.b9 and 4.6.b13, the FHEQ level 6 descriptor qaa/fheq-2024/4.15.b9.1 (FQHEIS level 10, std:doc:qaa-fqheis-2024-framework 4.16; spine:6) and Annex D's upper second band (qaa/fheq-2024/annex-d/summary/r1/2.1)."
  author-agent-dialogue: "Raise this when a student joins a collaborative project such as a script or anthology. To a student, put it plainly in the second person as what most people show by the end of the honours degree, not the minimum; to staff, frame it as the profile a module should help most students reach. Ask: 'How did you and your co-writers settle a disagreement about the piece?' Avoid presenting it as the pass mark or reading the list aloud."
- statement: qaa/creative-writing-2024/4.4.b18
  forPractitioner: { text: "At the typical level, most honours graduates will have shown awareness of research skills and methods suited to creative writing, and the capacity to plan and conduct their own research; design teaching so that most students reach it.", rewrite: light, force: will, status: drafted }
  forBeneficiary: { text: "At the typical level for your honours degree, you will know the research skills and methods that suit creative writing, and plan and carry out research of your own.", rewrite: full, force: will, status: drafted }
  author-agent-written: "Describe this as a typical outcome: what most honours graduates in the subject will have shown, above the threshold, at FHEQ level 6 (FQHEIS level 10): research skills and independent research. Cite it as QAA (2024), Creative Writing Subject Benchmark Statement, para 4.4, bullet 18. Do not claim it is the pass requirement or a regulatory standard; the threshold list in 4.3 is the minimum. Set it beside 4.7.b7, the FHEQ level 6 descriptor qaa/fheq-2024/4.15.b6 (FQHEIS level 10, std:doc:qaa-fqheis-2024-framework 4.16; spine:6) and Annex D's upper second band (qaa/fheq-2024/annex-d/summary/r1/2.1)."
  author-agent-dialogue: "Raise this when a student plans research for a novel, script or project. To a student, put it plainly in the second person as what most people show by the end of the honours degree, not the minimum; to staff, frame it as the profile a module should help most students reach. Ask: 'What research does your project need, and how will you gather it?' Avoid presenting it as the pass mark or reading the list aloud."
- statement: qaa/creative-writing-2024/4.4.b19
  forPractitioner: { text: "At the typical level, most honours graduates will have shown an understanding of how, with strategy, the subject's writing and story skills transfer to varied settings, careers and enterprises; design teaching so that most students reach it.", rewrite: light, force: will, status: drafted }
  forBeneficiary: { text: "At the typical level for your honours degree, you will understand how to transfer your writing and storytelling skills, with purpose, to different settings, careers and ventures of your own.", rewrite: full, force: will, status: drafted }
  author-agent-written: "Describe this as a typical outcome: what most honours graduates in the subject will have shown, above the threshold, at FHEQ level 6 (FQHEIS level 10): strategic transferability of writing and story skills. Cite it as QAA (2024), Creative Writing Subject Benchmark Statement, para 4.4, bullet 19. Do not claim it is the pass requirement or a regulatory standard; the threshold list in 4.3 is the minimum. Set it beside 4.3.b10 and 4.5.b6, the FHEQ level 6 descriptor qaa/fheq-2024/4.15.b9.3 (FQHEIS level 10, std:doc:qaa-fqheis-2024-framework 4.16; spine:6) and Annex D's upper second band (qaa/fheq-2024/annex-d/summary/r1/2.1)."
  author-agent-dialogue: "Raise this when a student plans a career or placement. To a student, put it plainly in the second person as what most people show by the end of the honours degree, not the minimum; to staff, frame it as the profile a module should help most students reach. Ask: 'How would you describe your story skills to an employer outside publishing?' Avoid presenting it as the pass mark or reading the list aloud."
- statement: qaa/creative-writing-2024/4.5
  forPractitioner: { text: "At the excellent level, graduates will have joined up the threshold and typical qualities creatively, with independent enterprise and flair, producing ambitious work that stands out as original in its field and asks searching questions.", rewrite: light, force: will, status: drafted }
  forBeneficiary: { text: "At the excellent level, you will bring together everything above with flair and independent enterprise, producing ambitious work that is clearly original next to what already exists and that asks probing questions.", rewrite: full, force: will, status: drafted }
  author-agent-written: "Describe this as the excellent rung's defining standard: the threshold and typical qualities, integrated with enterprise and flair, at FHEQ level 6 (FQHEIS level 10) for the honours degree. Cite it as QAA (2024), Creative Writing Subject Benchmark Statement, para 4.5. Do not present it as the minimum or as a regulatory requirement; set it beside 4.5.b1 to 4.5.b9, the typical list in 4.4 and Annex D's first-class descriptions (qaa/fheq-2024/annex-d/cognitive/r4/1st, qaa/fheq-2024/annex-d/summary/r1/1st)."
  author-agent-dialogue: "Raise it when a student or a marking team asks what lifts work above the typical level. To a student, say plainly that excellent work combines everything else with ambition, originality and flair; to staff, frame it as the profile of the top band. Ask: 'Where in this portfolio is the work most ambitious, and what makes it original against its field?' Avoid presenting it as what every student must reach."
- statement: qaa/creative-writing-2024/4.5.b1
  forPractitioner: { text: "At the excellent level, graduates will show some of these qualities; this one is original writing that changes how a genre can be approached; treat it as evidence for the top band, not a requirement.", rewrite: light, force: will, status: drafted }
  forBeneficiary: { text: "If you reach the excellent level, this may be one of the qualities you show: you write original work that changes how a genre can be approached.", rewrite: full, force: will, status: drafted }
  author-agent-written: "Describe this as one of the excellent-level qualities, of which the strongest honours graduates will show some, at FHEQ level 6 (FQHEIS level 10): original writing transforming genre. Cite it as QAA (2024), Creative Writing Subject Benchmark Statement, para 4.5, bullet 1. Do not claim every graduate, or every excellent graduate, shows it, or that it sets a pass requirement. Set it beside 4.3.b13 and 4.5 and Annex D's first-class description qaa/fheq-2024/annex-d/cognitive/r4/1st."
  author-agent-dialogue: "Raise this when a student works within or against genre conventions. To a student, put it plainly as a mark of the best work, something to stretch towards rather than a requirement; to staff, frame it as evidence for the top band. Ask: 'What does your piece do that the genre usually does not?' Avoid presenting it as the minimum or as a list to tick off in full."
- statement: qaa/creative-writing-2024/4.5.b2
  forPractitioner: { text: "At the excellent level, graduates will show some of these qualities; this one is fluent command of many narrative forms, story skills and media; treat it as evidence for the top band, not a requirement.", rewrite: light, force: will, status: drafted }
  forBeneficiary: { text: "If you reach the excellent level, this may be one of the qualities you show: you move fluently between many narrative forms, storytelling skills and media.", rewrite: full, force: will, status: drafted }
  author-agent-written: "Describe this as one of the excellent-level qualities, of which the strongest honours graduates will show some, at FHEQ level 6 (FQHEIS level 10): fluency across narrative forms, story skills and media. Cite it as QAA (2024), Creative Writing Subject Benchmark Statement, para 4.5, bullet 2. Do not claim every graduate, or every excellent graduate, shows it, or that it sets a pass requirement. Set it beside 4.4.b13 and 4.3.b8 and Annex D's first-class description qaa/fheq-2024/annex-d/practical/r1/1st."
  author-agent-dialogue: "Raise this when a student works confidently across forms. To a student, put it plainly as a mark of the best work, something to stretch towards rather than a requirement; to staff, frame it as evidence for the top band. Ask: 'Which form or medium feels as natural to you as your main one?' Avoid presenting it as the minimum or as a list to tick off in full."
- statement: qaa/creative-writing-2024/4.5.s2
  forPractitioner: { text: "At the excellent level, where an industry sets a presentation standard (a script format or a manuscript layout, for instance), the writing should reach or go beyond it.", rewrite: light, force: should, status: drafted }
  forBeneficiary: { text: "If you aim for the excellent level, and an industry has its own presentation standard, such as a script or manuscript format, your writing should reach or go beyond it.", rewrite: full, force: should, status: drafted }
  author-agent-written: "Describe this as a should-level condition on excellent work at FHEQ level 6 (FQHEIS level 10): where an industry presentation standard exists, the writing meets or exceeds it. Cite it as QAA (2024), Creative Writing Subject Benchmark Statement, para 4.5 (second sentence). Do not extend it to the threshold or typical rungs, or name a particular industry standard the issuer does not; set it beside 4.6.b2 and Annex D's first-class presentation description (qaa/fheq-2024/annex-d/practical/r4/1st)."
  author-agent-dialogue: "Raise it when a student prepares a submission package, script or manuscript, or when a team sets criteria for the top band. To a student, say plainly that the best work looks professional by the standards of its industry; to staff, frame it as a check at the excellent level only. Ask: 'Which industry format applies to this piece, and does it meet it?' Avoid treating presentation as a pass requirement."
- statement: qaa/creative-writing-2024/4.5.b3
  forPractitioner: { text: "At the excellent level, graduates will show some of these qualities; this one is inventive use of language whatever the subject or form; treat it as evidence for the top band, not a requirement.", rewrite: light, force: will, status: drafted }
  forBeneficiary: { text: "If you reach the excellent level, this may be one of the qualities you show: you use language inventively, whatever your subject or form.", rewrite: full, force: will, status: drafted }
  author-agent-written: "Describe this as one of the excellent-level qualities, of which the strongest honours graduates will show some, at FHEQ level 6 (FQHEIS level 10): innovative use of language. Cite it as QAA (2024), Creative Writing Subject Benchmark Statement, para 4.5, bullet 3. Do not claim every graduate, or every excellent graduate, shows it, or that it sets a pass requirement. Set it beside 4.4.b6 and Annex D's first-class description qaa/fheq-2024/annex-d/cognitive/r4/1st."
  author-agent-dialogue: "Raise this when a student experiments with style or voice. To a student, put it plainly as a mark of the best work, something to stretch towards rather than a requirement; to staff, frame it as evidence for the top band. Ask: 'Where in this piece does your use of language surprise the reader?' Avoid presenting it as the minimum or as a list to tick off in full."
- statement: qaa/creative-writing-2024/4.5.b4
  forPractitioner: { text: "At the excellent level, graduates will show some of these qualities; this one is writing that brings original, meaningful and potentially influential responses to inclusion, diversity, accessibility and equality in society; treat it as evidence for the top band, not a requirement.", rewrite: light, force: will, status: drafted }
  forBeneficiary: { text: "If you reach the excellent level, this may be one of the qualities you show: you write in original, meaningful ways that could make a difference to inclusion, diversity, accessibility and equality.", rewrite: full, force: will, status: drafted }
  author-agent-written: "Describe this as one of the excellent-level qualities, of which the strongest honours graduates will show some, at FHEQ level 6 (FQHEIS level 10): original responses to inclusion, diversity, accessibility and equality. Cite it as QAA (2024), Creative Writing Subject Benchmark Statement, para 4.5, bullet 4. Do not claim every graduate, or every excellent graduate, shows it, or that it sets a pass requirement. Set it beside 4.4.b15 and 4.6.b14 and Annex D's first-class description qaa/fheq-2024/annex-d/cognitive/r4/1st."
  author-agent-dialogue: "Raise this when a student writes about identity, difference or access. To a student, put it plainly as a mark of the best work, something to stretch towards rather than a requirement; to staff, frame it as evidence for the top band. Ask: 'What does your piece let a reader see about inclusion that they might have missed?' Avoid presenting it as the minimum or as a list to tick off in full."
- statement: qaa/creative-writing-2024/4.5.b5
  forPractitioner: { text: "At the excellent level, graduates will show some of these qualities; this one is writing that shows a transforming awareness of how change can support sustainability, or that opens new ways of seeing how humans, other beings and their habitats relate; treat it as evidence for the top band, not a requirement.", rewrite: light, force: will, status: drafted }
  forBeneficiary: { text: "If you reach the excellent level, this may be one of the qualities you show: you write in ways that show how change could support sustainability, or open new ways of seeing how people, other creatures and their habitats relate.", rewrite: full, force: will, status: drafted }
  author-agent-written: "Describe this as one of the excellent-level qualities, of which the strongest honours graduates will show some, at FHEQ level 6 (FQHEIS level 10): transformative writing on sustainability and ecology. Cite it as QAA (2024), Creative Writing Subject Benchmark Statement, para 4.5, bullet 5. Do not claim every graduate, or every excellent graduate, shows it, or that it sets a pass requirement. Set it beside 4.4.b14 and 4.3.b11 and Annex D's first-class description qaa/fheq-2024/annex-d/cognitive/r4/1st."
  author-agent-dialogue: "Raise this when a student's work engages with climate, nature or ecology. To a student, put it plainly as a mark of the best work, something to stretch towards rather than a requirement; to staff, frame it as evidence for the top band. Ask: 'What might a reader see or do differently about the living world after reading this?' Avoid presenting it as the minimum or as a list to tick off in full."
- statement: qaa/creative-writing-2024/4.5.b6
  forPractitioner: { text: "At the excellent level, graduates will show some of these qualities; this one is writing that opens new room for creative and entrepreneurial expression; treat it as evidence for the top band, not a requirement.", rewrite: light, force: will, status: drafted }
  forBeneficiary: { text: "If you reach the excellent level, this may be one of the qualities you show: you write in ways that open new room for creative and enterprising expression.", rewrite: full, force: will, status: drafted }
  author-agent-written: "Describe this as one of the excellent-level qualities, of which the strongest honours graduates will show some, at FHEQ level 6 (FQHEIS level 10): new spaces for creative and entrepreneurial expression. Cite it as QAA (2024), Creative Writing Subject Benchmark Statement, para 4.5, bullet 6. Do not claim every graduate, or every excellent graduate, shows it, or that it sets a pass requirement. Set it beside 4.4.b19 and 4.3.b10 and Annex D's first-class description qaa/fheq-2024/annex-d/transferable/r4/1st."
  author-agent-dialogue: "Raise this when a student develops a new format, venture or publishing idea. To a student, put it plainly as a mark of the best work, something to stretch towards rather than a requirement; to staff, frame it as evidence for the top band. Ask: 'What space for writing does your project create that did not exist before?' Avoid presenting it as the minimum or as a list to tick off in full."
- statement: qaa/creative-writing-2024/4.5.b7
  forPractitioner: { text: "At the excellent level, graduates will show some of these qualities; this one is writing with critical force and self-awareness, deeply reflective, that builds and keeps up critical links between the subject and creative practice in other disciplines; treat it as evidence for the top band, not a requirement.", rewrite: light, force: will, status: drafted }
  forBeneficiary: { text: "If you reach the excellent level, this may be one of the qualities you show: you write with critical force and self-awareness, reflecting deeply and linking your writing to creative practice in other disciplines.", rewrite: full, force: will, status: drafted }
  author-agent-written: "Describe this as one of the excellent-level qualities, of which the strongest honours graduates will show some, at FHEQ level 6 (FQHEIS level 10): critically impactful, self-reflective, interdisciplinary writing. Cite it as QAA (2024), Creative Writing Subject Benchmark Statement, para 4.5, bullet 7. Do not claim every graduate, or every excellent graduate, shows it, or that it sets a pass requirement. Set it beside 4.4.b2 and 4.3.b2 and Annex D's first-class description qaa/fheq-2024/annex-d/transferable/r5/1st."
  author-agent-dialogue: "Raise this when a student writes a creative-critical or interdisciplinary piece. To a student, put it plainly as a mark of the best work, something to stretch towards rather than a requirement; to staff, frame it as evidence for the top band. Ask: 'What does your reflection reveal about the piece that the piece alone does not?' Avoid presenting it as the minimum or as a list to tick off in full."
- statement: qaa/creative-writing-2024/4.5.b8
  forPractitioner: { text: "At the excellent level, graduates will show some of these qualities; this one is writing that draws on and explores the wide variety of languages and dialects, giving voice to regional, global and media-specific varieties; treat it as evidence for the top band, not a requirement.", rewrite: light, force: will, status: drafted }
  forBeneficiary: { text: "If you reach the excellent level, this may be one of the qualities you show: you draw on and explore many languages and dialects, giving voice to regional, global and media-specific ways of speaking.", rewrite: full, force: will, status: drafted }
  author-agent-written: "Describe this as one of the excellent-level qualities, of which the strongest honours graduates will show some, at FHEQ level 6 (FQHEIS level 10): diversity of languages and dialects. Cite it as QAA (2024), Creative Writing Subject Benchmark Statement, para 4.5, bullet 8. Do not claim every graduate, or every excellent graduate, shows it, or that it sets a pass requirement. Set it beside 4.4.b6 and 4.4.b15 and Annex D's first-class description qaa/fheq-2024/annex-d/practical/r1/1st."
  author-agent-dialogue: "Raise this when a student writes in dialect, another language or a mixed idiom. To a student, put it plainly as a mark of the best work, something to stretch towards rather than a requirement; to staff, frame it as evidence for the top band. Ask: 'Why does this voice need its own dialect or language, and how will readers meet it?' Avoid presenting it as the minimum or as a list to tick off in full."
- statement: qaa/creative-writing-2024/4.5.b9
  forPractitioner: { text: "At the excellent level, graduates will show some of these qualities; this one is writing that shows advanced co-production through editing, workshops and collaboration, and work with communities of practice outside the classroom; treat it as evidence for the top band, not a requirement.", rewrite: light, force: will, status: drafted }
  forBeneficiary: { text: "If you reach the excellent level, this may be one of the qualities you show: you co-create at an advanced level through editing, workshops and collaboration, working with writing communities outside your classes.", rewrite: full, force: will, status: drafted }
  author-agent-written: "Describe this as one of the excellent-level qualities, of which the strongest honours graduates will show some, at FHEQ level 6 (FQHEIS level 10): advanced co-production with communities of practice. Cite it as QAA (2024), Creative Writing Subject Benchmark Statement, para 4.5, bullet 9. Do not claim every graduate, or every excellent graduate, shows it, or that it sets a pass requirement. Set it beside 4.4.b17 and 4.6.b13 and Annex D's first-class description qaa/fheq-2024/annex-d/transferable/r2/1st."
  author-agent-dialogue: "Raise this when a student leads a group project, anthology or community writing work. To a student, put it plainly as a mark of the best work, something to stretch towards rather than a requirement; to staff, frame it as evidence for the top band. Ask: 'What did the group make that none of you could have made alone?' Avoid presenting it as the minimum or as a list to tick off in full."
- statement: qaa/creative-writing-2024/4.6.b1
  forPractitioner: { text: "By graduation, honours students should be able to start their own work and answer for it; give them chances to practise and evidence it.", rewrite: light, force: should, status: drafted }
  forBeneficiary: { text: "By the time you graduate, you should be able to start your own work and take responsibility for it.", rewrite: full, force: should, status: drafted }
  author-agent-written: "Describe this as a generic skill that honours graduates in the subject should be able to show (force should) at FHEQ level 6 (FQHEIS level 10): initiative and responsibility for own work. Cite it as QAA (2024), Creative Writing Subject Benchmark Statement, para 4.6, bullet 1. Do not claim it is a subject-specific or regulatory requirement, or that it holds unchanged at master's level. Set it beside 2.2.b5 and 4.7.b2 and the FHEQ level 6 descriptor qaa/fheq-2024/4.15.b9.1 (FQHEIS level 10, std:doc:qaa-fqheis-2024-framework 4.16; spine:6), which it refines."
  author-agent-dialogue: "Raise this when a student waits to be told what to write. To a student, say plainly that you should be able to do this by graduation; to staff, frame it as a transferable skill to build and evidence across modules. Ask: 'What project have you started without being asked?' Avoid reading the list aloud or treating it as separate from the writing itself."
- statement: qaa/creative-writing-2024/4.6.b2
  forPractitioner: { text: "By graduation, honours students should be able to present information to a professional standard that suits the setting; give them chances to practise and evidence it.", rewrite: light, force: should, status: drafted }
  forBeneficiary: { text: "By the time you graduate, you should be able to present information professionally, in a way that suits the setting.", rewrite: full, force: should, status: drafted }
  author-agent-written: "Describe this as a generic skill that honours graduates in the subject should be able to show (force should) at FHEQ level 6 (FQHEIS level 10): professional presentation of information. Cite it as QAA (2024), Creative Writing Subject Benchmark Statement, para 4.6, bullet 2. Do not claim it is a subject-specific or regulatory requirement, or that it holds unchanged at master's level. Set it beside 4.5.s2 and the FHEQ level 6 descriptor qaa/fheq-2024/4.15.b8 (FQHEIS level 10, std:doc:qaa-fqheis-2024-framework 4.16; spine:6), which it refines."
  author-agent-dialogue: "Raise this when a student prepares a submission, pitch or portfolio. To a student, say plainly that you should be able to do this by graduation; to staff, frame it as a transferable skill to build and evidence across modules. Ask: 'Would an editor or agent take this submission seriously as it stands?' Avoid reading the list aloud or treating it as separate from the writing itself."
- statement: qaa/creative-writing-2024/4.6.b3
  forPractitioner: { text: "By graduation, honours students should be able to manage themselves, work independently, set goals, handle their workload and keep to deadlines; give them chances to practise and evidence it.", rewrite: light, force: should, status: drafted }
  forBeneficiary: { text: "By the time you graduate, you should be able to manage yourself, work on your own, set goals, handle your workload and hit deadlines.", rewrite: full, force: should, status: drafted }
  author-agent-written: "Describe this as a generic skill that honours graduates in the subject should be able to show (force should) at FHEQ level 6 (FQHEIS level 10): self-management and independent work. Cite it as QAA (2024), Creative Writing Subject Benchmark Statement, para 4.6, bullet 3. Do not claim it is a subject-specific or regulatory requirement, or that it holds unchanged at master's level. Set it beside 4.4.b7 and 4.7.b2 and the FHEQ level 6 descriptor qaa/fheq-2024/4.15.b9.1 (FQHEIS level 10, std:doc:qaa-fqheis-2024-framework 4.16; spine:6), which it refines."
  author-agent-dialogue: "Raise this when a student is behind or overloaded. To a student, say plainly that you should be able to do this by graduation; to staff, frame it as a transferable skill to build and evidence across modules. Ask: 'How do you plan your writing time across competing deadlines?' Avoid reading the list aloud or treating it as separate from the writing itself."
- statement: qaa/creative-writing-2024/4.6.b4
  forPractitioner: { text: "By graduation, honours students should be able to foresee and adjust to change, and work through situations that are ambiguous, uncertain or unfamiliar; give them chances to practise and evidence it.", rewrite: light, force: should, status: drafted }
  forBeneficiary: { text: "By the time you graduate, you should be able to see change coming, adjust to it and find your way through situations that are unclear, uncertain or new to you.", rewrite: full, force: should, status: drafted }
  author-agent-written: "Describe this as a generic skill that honours graduates in the subject should be able to show (force should) at FHEQ level 6 (FQHEIS level 10): handling change and ambiguity. Cite it as QAA (2024), Creative Writing Subject Benchmark Statement, para 4.6, bullet 4. Do not claim it is a subject-specific or regulatory requirement, or that it holds unchanged at master's level. Set it beside 4.6.b15 and 4.7.b2 and the FHEQ level 6 descriptor qaa/fheq-2024/4.15.b4 (FQHEIS level 10, std:doc:qaa-fqheis-2024-framework 4.16; spine:6), which it refines."
  author-agent-dialogue: "Raise this when a student faces an open or unclear brief. To a student, say plainly that you should be able to do this by graduation; to staff, frame it as a transferable skill to build and evidence across modules. Ask: 'What did you do the last time a brief was unclear?' Avoid reading the list aloud or treating it as separate from the writing itself."
- statement: qaa/creative-writing-2024/4.6.b5
  forPractitioner: { text: "By graduation, honours students should be able to identify strengths and development needs by reflecting on their personal growth; give them chances to practise and evidence it.", rewrite: light, force: should, status: drafted }
  forBeneficiary: { text: "By the time you graduate, you should be able to reflect on your own development and identify your strengths and what you need to work on.", rewrite: full, force: should, status: drafted }
  author-agent-written: "Describe this as a generic skill that honours graduates in the subject should be able to show (force should) at FHEQ level 6 (FQHEIS level 10): identifying strengths and needs through reflection. Cite it as QAA (2024), Creative Writing Subject Benchmark Statement, para 4.6, bullet 5. Do not claim it is a subject-specific or regulatory requirement, or that it holds unchanged at master's level. Set it beside 4.3.b2 and 4.6.b17 and the FHEQ level 6 descriptor qaa/fheq-2024/4.15.b9.3 (FQHEIS level 10, std:doc:qaa-fqheis-2024-framework 4.16; spine:6), which it refines."
  author-agent-dialogue: "Raise this when a student plans personal development or writes a reflective account. To a student, say plainly that you should be able to do this by graduation; to staff, frame it as a transferable skill to build and evidence across modules. Ask: 'What is one strength you can show evidence for, and one need you are working on?' Avoid reading the list aloud or treating it as separate from the writing itself."
- statement: qaa/creative-writing-2024/4.6.b6
  forPractitioner: { text: "By graduation, honours students should be able to choose and use communication and information technologies, and find, sift, judge and manage information from many sources; give them chances to practise and evidence it.", rewrite: light, force: should, status: drafted }
  forBeneficiary: { text: "By the time you graduate, you should be able to choose and use digital and communication tools, and find, judge and manage information from many sources.", rewrite: full, force: should, status: drafted }
  author-agent-written: "Describe this as a generic skill that honours graduates in the subject should be able to show (force should) at FHEQ level 6 (FQHEIS level 10): information and communication technologies; managing information. Cite it as QAA (2024), Creative Writing Subject Benchmark Statement, para 4.6, bullet 6. Do not claim it is a subject-specific or regulatory requirement, or that it holds unchanged at master's level. Set it beside 4.4.b18 and the FHEQ level 6 descriptor qaa/fheq-2024/4.15.b5 (FQHEIS level 10, std:doc:qaa-fqheis-2024-framework 4.16; spine:6), which it refines."
  author-agent-dialogue: "Raise this when a student researches for a project or works with digital platforms. To a student, say plainly that you should be able to do this by graduation; to staff, frame it as a transferable skill to build and evidence across modules. Ask: 'How do you judge whether a source is reliable enough to use?' Avoid reading the list aloud or treating it as separate from the writing itself."
- statement: qaa/creative-writing-2024/4.6.b7
  forPractitioner: { text: "By graduation, honours students should be able to produce or tell a true story in clear or persuasive language, from their own experience or from other people's accounts; give them chances to practise and evidence it.", rewrite: light, force: should, status: drafted }
  forBeneficiary: { text: "By the time you graduate, you should be able to write or tell a true story in clear or persuasive language, using your own experience or what others have told you.", rewrite: full, force: should, status: drafted }
  author-agent-written: "Describe this as a generic skill that honours graduates in the subject should be able to show (force should) at FHEQ level 6 (FQHEIS level 10): factual storytelling from own or others' accounts. Cite it as QAA (2024), Creative Writing Subject Benchmark Statement, para 4.6, bullet 7. Do not claim it is a subject-specific or regulatory requirement, or that it holds unchanged at master's level. Set it beside 4.7.b13 and the FHEQ level 6 descriptor qaa/fheq-2024/4.15.b8 (FQHEIS level 10, std:doc:qaa-fqheis-2024-framework 4.16; spine:6), which it refines."
  author-agent-dialogue: "Raise this when a student writes memoir, life writing, journalism or creative non-fiction. To a student, say plainly that you should be able to do this by graduation; to staff, frame it as a transferable skill to build and evidence across modules. Ask: 'Whose account are you telling, and what do you owe them?' Avoid reading the list aloud or treating it as separate from the writing itself."
- statement: qaa/creative-writing-2024/4.6.b8
  forPractitioner: { text: "By graduation, honours students should be able to work adaptably, alone and with others; give them chances to practise and evidence it.", rewrite: light, force: should, status: drafted }
  forBeneficiary: { text: "By the time you graduate, you should be able to work flexibly, on your own and with other people.", rewrite: full, force: should, status: drafted }
  author-agent-written: "Describe this as a generic skill that honours graduates in the subject should be able to show (force should) at FHEQ level 6 (FQHEIS level 10): flexible independent and collaborative work. Cite it as QAA (2024), Creative Writing Subject Benchmark Statement, para 4.6, bullet 8. Do not claim it is a subject-specific or regulatory requirement, or that it holds unchanged at master's level. Set it beside 4.6.b13 and the FHEQ level 6 descriptor qaa/fheq-2024/4.15.b9.1 (FQHEIS level 10, std:doc:qaa-fqheis-2024-framework 4.16; spine:6), which it refines."
  author-agent-dialogue: "Raise this when a student moves between solo and group tasks. To a student, say plainly that you should be able to do this by graduation; to staff, frame it as a transferable skill to build and evidence across modules. Ask: 'When do you work best alone, and when with others?' Avoid reading the list aloud or treating it as separate from the writing itself."
- statement: qaa/creative-writing-2024/4.6.b9
  forPractitioner: { text: "By graduation, honours students should be able to show and put to active use many transferable communication and storytelling skills; give them chances to practise and evidence it.", rewrite: light, force: should, status: drafted }
  forBeneficiary: { text: "By the time you graduate, you should be able to show and put to active use many transferable communication and storytelling skills.", rewrite: full, force: should, status: drafted }
  author-agent-written: "Describe this as a generic skill that honours graduates in the subject should be able to show (force should) at FHEQ level 6 (FQHEIS level 10): transferable communication and story skills. Cite it as QAA (2024), Creative Writing Subject Benchmark Statement, para 4.6, bullet 9. Do not claim it is a subject-specific or regulatory requirement, or that it holds unchanged at master's level. Set it beside 4.6.b10 and 4.6.b12 and the FHEQ level 6 descriptor qaa/fheq-2024/4.15.b8 (FQHEIS level 10, std:doc:qaa-fqheis-2024-framework 4.16; spine:6), which it refines."
  author-agent-dialogue: "Raise this when a student asks what the degree gives them beyond writing. To a student, say plainly that you should be able to do this by graduation; to staff, frame it as a transferable skill to build and evidence across modules. Ask: 'Which of your story skills would help in a job that is not about writing?' Avoid reading the list aloud or treating it as separate from the writing itself."
- statement: qaa/creative-writing-2024/4.6.b10
  forPractitioner: { text: "By graduation, honours students should be able to put across their own and others' ideas briefly, accurately and persuasively so as to sway opinion, building and presenting arguments suitably; give them chances to practise and evidence it.", rewrite: light, force: should, status: drafted }
  forBeneficiary: { text: "By the time you graduate, you should be able to put your own and others' ideas across briefly, accurately and persuasively to change minds, building and presenting arguments in the right way.", rewrite: full, force: should, status: drafted }
  author-agent-written: "Describe this as a generic skill that honours graduates in the subject should be able to show (force should) at FHEQ level 6 (FQHEIS level 10): concise, accurate, persuasive communication and argument. Cite it as QAA (2024), Creative Writing Subject Benchmark Statement, para 4.6, bullet 10. Do not claim it is a subject-specific or regulatory requirement, or that it holds unchanged at master's level. Set it beside 4.6.b9 and 4.7.b15 and the FHEQ level 6 descriptor qaa/fheq-2024/4.15.b3.1 (FQHEIS level 10, std:doc:qaa-fqheis-2024-framework 4.16; spine:6), which it refines."
  author-agent-dialogue: "Raise this when a student writes an essay, pitch or argument. To a student, say plainly that you should be able to do this by graduation; to staff, frame it as a transferable skill to build and evidence across modules. Ask: 'What is your central claim, and what would persuade a sceptical reader?' Avoid reading the list aloud or treating it as separate from the writing itself."
- statement: qaa/creative-writing-2024/4.6.b11
  forPractitioner: { text: "By graduation, honours students should be able to build the skill of listening actively and see why it matters; give them chances to practise and evidence it.", rewrite: light, force: should, status: drafted }
  forBeneficiary: { text: "By the time you graduate, you should be able to build your skill in listening actively and understand why it matters.", rewrite: full, force: should, status: drafted }
  author-agent-written: "Describe this as a generic skill that honours graduates in the subject should be able to show (force should) at FHEQ level 6 (FQHEIS level 10): active listening. Cite it as QAA (2024), Creative Writing Subject Benchmark Statement, para 4.6, bullet 11. Do not claim it is a subject-specific or regulatory requirement, or that it holds unchanged at master's level. Set it beside 4.4.b16 and the FHEQ level 6 descriptor qaa/fheq-2024/4.15.b8 (FQHEIS level 10, std:doc:qaa-fqheis-2024-framework 4.16; spine:6), which it refines."
  author-agent-dialogue: "Raise this when a student takes part in workshops. To a student, say plainly that you should be able to do this by graduation; to staff, frame it as a transferable skill to build and evidence across modules. Ask: 'What did you hear in the last workshop that you nearly missed?' Avoid reading the list aloud or treating it as separate from the writing itself."
- statement: qaa/creative-writing-2024/4.6.b12
  forPractitioner: { text: "By graduation, honours students should be able to communicate in varied media with a strong sense of what story, narrative and language are for and how they work; give them chances to practise and evidence it.", rewrite: light, force: should, status: drafted }
  forBeneficiary: { text: "By the time you graduate, you should be able to communicate in different media, with a strong sense of how story, narrative and language work and what they are for.", rewrite: full, force: should, status: drafted }
  author-agent-written: "Describe this as a generic skill that honours graduates in the subject should be able to show (force should) at FHEQ level 6 (FQHEIS level 10): communicating across media with awareness of story and language. Cite it as QAA (2024), Creative Writing Subject Benchmark Statement, para 4.6, bullet 12. Do not claim it is a subject-specific or regulatory requirement, or that it holds unchanged at master's level. Set it beside 4.4.b13 and 4.6.b9 and the FHEQ level 6 descriptor qaa/fheq-2024/4.15.b8 (FQHEIS level 10, std:doc:qaa-fqheis-2024-framework 4.16; spine:6), which it refines."
  author-agent-dialogue: "Raise this when a student moves a piece into a new medium. To a student, say plainly that you should be able to do this by graduation; to staff, frame it as a transferable skill to build and evidence across modules. Ask: 'What does story do in this medium that it cannot do on the page?' Avoid reading the list aloud or treating it as separate from the writing itself."
- statement: qaa/creative-writing-2024/4.6.b13
  forPractitioner: { text: "By graduation, honours students should be able to work well with others in teams or groups, for instance in collaboration or workshops; give them chances to practise and evidence it.", rewrite: light, force: should, status: drafted }
  forBeneficiary: { text: "By the time you graduate, you should be able to work well with others in teams and groups, for example in workshops or joint projects.", rewrite: full, force: should, status: drafted }
  author-agent-written: "Describe this as a generic skill that honours graduates in the subject should be able to show (force should) at FHEQ level 6 (FQHEIS level 10): effective interaction in teams and workshops. Cite it as QAA (2024), Creative Writing Subject Benchmark Statement, para 4.6, bullet 13. Do not claim it is a subject-specific or regulatory requirement, or that it holds unchanged at master's level. Set it beside 4.3.b9, 4.4.b17 and 4.7.b14 and the FHEQ level 6 descriptor qaa/fheq-2024/4.15.b9.1 (FQHEIS level 10, std:doc:qaa-fqheis-2024-framework 4.16; spine:6), which it refines."
  author-agent-dialogue: "Raise this when a student has trouble in a group. To a student, say plainly that you should be able to do this by graduation; to staff, frame it as a transferable skill to build and evidence across modules. Ask: 'What do you do when a group stalls or disagrees?' Avoid reading the list aloud or treating it as separate from the writing itself."
- statement: qaa/creative-writing-2024/4.6.b14
  forPractitioner: { text: "By graduation, honours students should be able to show that they understand equality, diversity and inclusion; give them chances to practise and evidence it.", rewrite: light, force: should, status: drafted }
  forBeneficiary: { text: "By the time you graduate, you should be able to show that you understand equality, diversity and inclusion.", rewrite: full, force: should, status: drafted }
  author-agent-written: "Describe this as a generic skill that honours graduates in the subject should be able to show (force should) at FHEQ level 6 (FQHEIS level 10): understanding equality, diversity and inclusivity. Cite it as QAA (2024), Creative Writing Subject Benchmark Statement, para 4.6, bullet 14. Do not claim it is a subject-specific or regulatory requirement, or that it holds unchanged at master's level. Set it beside 4.3.b9, 4.4.b15 and 4.5.b4, and paragraphs 1.21 to 1.24 to which the issuer points and the FHEQ level 6 descriptor qaa/fheq-2024/4.15.b9.1 (no level 6 descriptor names equality; personal responsibility is the nearest) (FQHEIS level 10, std:doc:qaa-fqheis-2024-framework 4.16; spine:6), which it refines."
  author-agent-dialogue: "Raise this when a student asks how inclusion bears on their writing or workshop conduct. To a student, say plainly that you should be able to do this by graduation; to staff, frame it as a transferable skill to build and evidence across modules. Ask: 'How does your writing or workshop practice make room for people unlike you?' Avoid reading the list aloud or treating it as separate from the writing itself."
- statement: qaa/creative-writing-2024/4.6.b15
  forPractitioner: { text: "By graduation, honours students should be able to adjust to varied demands and tasks and see past the task in hand to its wider setting, including what their work does socially and commercially; give them chances to practise and evidence it.", rewrite: light, force: should, status: drafted }
  forBeneficiary: { text: "By the time you graduate, you should be able to adapt to different demands and tasks and look past the immediate job to its wider setting, including the social and commercial impact of what you make.", rewrite: full, force: should, status: drafted }
  author-agent-written: "Describe this as a generic skill that honours graduates in the subject should be able to show (force should) at FHEQ level 6 (FQHEIS level 10): adapting to demands; wider social and commercial effects. Cite it as QAA (2024), Creative Writing Subject Benchmark Statement, para 4.6, bullet 15. Do not claim it is a subject-specific or regulatory requirement, or that it holds unchanged at master's level. Set it beside 4.6.b4 and the FHEQ level 6 descriptor qaa/fheq-2024/4.15.b9.2 (FQHEIS level 10, std:doc:qaa-fqheis-2024-framework 4.16; spine:6), which it refines."
  author-agent-dialogue: "Raise this when a student works to a brief or commission. To a student, say plainly that you should be able to do this by graduation; to staff, frame it as a transferable skill to build and evidence across modules. Ask: 'Who else is affected by this piece once it is published?' Avoid reading the list aloud or treating it as separate from the writing itself."
- statement: qaa/creative-writing-2024/4.6.b16
  forPractitioner: { text: "By graduation, honours students should be able to value giving feedback and receiving it; give them chances to practise and evidence it.", rewrite: light, force: should, status: drafted }
  forBeneficiary: { text: "By the time you graduate, you should be able to value both giving and receiving feedback.", rewrite: full, force: should, status: drafted }
  author-agent-written: "Describe this as a generic skill that honours graduates in the subject should be able to show (force should) at FHEQ level 6 (FQHEIS level 10): value of giving and receiving feedback. Cite it as QAA (2024), Creative Writing Subject Benchmark Statement, para 4.6, bullet 16. Do not claim it is a subject-specific or regulatory requirement, or that it holds unchanged at master's level. Set it beside 4.4.b16 and 4.7.b10 and the FHEQ level 6 descriptor qaa/fheq-2024/4.15.b9.3 (FQHEIS level 10, std:doc:qaa-fqheis-2024-framework 4.16; spine:6), which it refines."
  author-agent-dialogue: "Raise this when a student resists critique. To a student, say plainly that you should be able to do this by graduation; to staff, frame it as a transferable skill to build and evidence across modules. Ask: 'What is the most useful feedback you have had, and why did it help?' Avoid reading the list aloud or treating it as separate from the writing itself."
- statement: qaa/creative-writing-2024/4.6.b17
  forPractitioner: { text: "By graduation, honours students should be able to evaluate and reflect on themselves, critically examining their own practices and assumptions; give them chances to practise and evidence it.", rewrite: light, force: should, status: drafted }
  forBeneficiary: { text: "By the time you graduate, you should be able to evaluate your work and reflect critically on your own practices and assumptions.", rewrite: full, force: should, status: drafted }
  author-agent-written: "Describe this as a generic skill that honours graduates in the subject should be able to show (force should) at FHEQ level 6 (FQHEIS level 10): critical self-reflection on practice and assumptions. Cite it as QAA (2024), Creative Writing Subject Benchmark Statement, para 4.6, bullet 17. Do not claim it is a subject-specific or regulatory requirement, or that it holds unchanged at master's level. Set it beside 4.3.b2, 4.4.b2 and 4.5.b7 and the FHEQ level 6 descriptor qaa/fheq-2024/4.15.b7 (FQHEIS level 10, std:doc:qaa-fqheis-2024-framework 4.16; spine:6), which it refines."
  author-agent-dialogue: "Raise this when a student writes a reflective commentary. To a student, say plainly that you should be able to do this by graduation; to staff, frame it as a transferable skill to build and evidence across modules. Ask: 'Which assumption about your writing has your reflection challenged?' Avoid reading the list aloud or treating it as separate from the writing itself."
- statement: qaa/creative-writing-2024/4.6.b18
  forPractitioner: { text: "By graduation, honours students should be able to show growing confidence in the wider personal skills the subject builds, for example self-expression and self-awareness; give them chances to practise and evidence it.", rewrite: light, force: should, status: drafted }
  forBeneficiary: { text: "By the time you graduate, you should be able to grow more confident in the wider personal skills writing builds, such as self-expression and self-awareness.", rewrite: full, force: should, status: drafted }
  author-agent-written: "Describe this as a generic skill that honours graduates in the subject should be able to show (force should) at FHEQ level 6 (FQHEIS level 10): confidence in life-enhancing skills. Cite it as QAA (2024), Creative Writing Subject Benchmark Statement, para 4.6, bullet 18. Do not claim it is a subject-specific or regulatory requirement, or that it holds unchanged at master's level. Set it beside 4.7.b16 and the FHEQ level 6 descriptor qaa/fheq-2024/4.15.b9.3 (FQHEIS level 10, std:doc:qaa-fqheis-2024-framework 4.16; spine:6), which it refines."
  author-agent-dialogue: "Raise this when a student talks about why they write or how the course has changed them. To a student, say plainly that you should be able to do this by graduation; to staff, frame it as a transferable skill to build and evidence across modules. Ask: 'How has writing changed the way you express yourself outside class?' Avoid reading the list aloud or treating it as separate from the writing itself."
- statement: qaa/creative-writing-2024/4.7.b1
  forPractitioner: { text: "At master's level, students show advanced creative and imaginative skills that carry the conception, design and making of a substantial creative writing project; design the course and its final project so that they can.", rewrite: light, force: must, status: drafted }
  forBeneficiary: { text: "At master's level, you use advanced creative and imaginative skill to conceive, design and produce a substantial writing project.", rewrite: full, force: must, status: drafted }
  author-agent-written: "Describe this as a master's-level outcome that the statement describes for students achieving that level (plain present, force describes), at FHEQ level 7 (FQHEIS level 11): advanced creative skills for a substantial project. Cite it as QAA (2024), Creative Writing Subject Benchmark Statement, para 4.7, bullet 1. Do not claim it applies to the honours degree or that the issuer makes it a requirement. Set it beside 4.7.b3 and 4.5 and the FHEQ level 7 descriptor qaa/fheq-2024/4.17.b3 (shared with FQHEIS level 11; spine:7)."
  author-agent-dialogue: "Raise this when a master's student plans their major project. To a master's student, put it plainly in the second person as what work at this level shows; to staff, frame it as a design aim for the master's course and its final project. Ask: 'What is the core idea of your project, and how will its design serve it?' Avoid applying it to undergraduates or reading the list aloud."
- statement: qaa/creative-writing-2024/4.7.b2
  forPractitioner: { text: "At master's level, students show combined professional skills, managing themselves and their time, writing independently and learning on their own, needed to complete a substantial project with initiative and sound decisions when things are complex and unpredictable; design the course and its final project so that they can.", rewrite: light, force: must, status: drafted }
  forBeneficiary: { text: "At master's level, you manage yourself and your time, write independently and learn on your own, so that you can complete a major project, taking the initiative and deciding well when things are complex and unpredictable.", rewrite: full, force: must, status: drafted }
  author-agent-written: "Describe this as a master's-level outcome that the statement describes for students achieving that level (plain present, force describes), at FHEQ level 7 (FQHEIS level 11): composite professional skills for a substantial project. Cite it as QAA (2024), Creative Writing Subject Benchmark Statement, para 4.7, bullet 2. Do not claim it applies to the honours degree or that the issuer makes it a requirement. Set it beside 4.6.b3 and 4.6.b1 and the FHEQ level 7 descriptor qaa/fheq-2024/4.17.b8.2 (shared with FQHEIS level 11; spine:7)."
  author-agent-dialogue: "Raise this when a master's student is managing a long project alone. To a master's student, put it plainly in the second person as what work at this level shows; to staff, frame it as a design aim for the master's course and its final project. Ask: 'What decisions have you made on your project without guidance, and how did you make them?' Avoid applying it to undergraduates or reading the list aloud."
- statement: qaa/creative-writing-2024/4.7.b3
  forPractitioner: { text: "At master's level, students show the completion of a large creative writing piece, of suitable length or form, that adds something original to its field; design the course and its final project so that they can.", rewrite: light, force: must, status: drafted }
  forBeneficiary: { text: "At master's level, you finish a large creative writing piece, of fitting length or form, that adds something original to its field.", rewrite: full, force: must, status: drafted }
  author-agent-written: "Describe this as a master's-level outcome that the statement describes for students achieving that level (plain present, force describes), at FHEQ level 7 (FQHEIS level 11): a substantial original piece of writing. Cite it as QAA (2024), Creative Writing Subject Benchmark Statement, para 4.7, bullet 3. Do not claim it applies to the honours degree or that the issuer makes it a requirement. Set it beside 4.7.b1 and 4.7.b4 and the FHEQ level 7 descriptor qaa/fheq-2024/4.17.b3 (shared with FQHEIS level 11; spine:7)."
  author-agent-dialogue: "Raise this when a master's student asks what the final project must achieve. To a master's student, put it plainly in the second person as what work at this level shows; to staff, frame it as a design aim for the master's course and its final project. Ask: 'What does your project add that is not already in its field?' Avoid applying it to undergraduates or reading the list aloud."
- statement: qaa/creative-writing-2024/4.7.b4
  forPractitioner: { text: "At master's level, students show a critical piece on how their project arose and was carried out, setting it within a fitting scholarly or creative tradition and making clear what is original in it; design the course and its final project so that they can.", rewrite: light, force: must, status: drafted }
  forBeneficiary: { text: "At master's level, you write a critical piece on how your project began and developed, place it in a scholarly or creative tradition and show what is original about it.", rewrite: full, force: must, status: drafted }
  author-agent-written: "Describe this as a master's-level outcome that the statement describes for students achieving that level (plain present, force describes), at FHEQ level 7 (FQHEIS level 11): critical writing on the project and its tradition. Cite it as QAA (2024), Creative Writing Subject Benchmark Statement, para 4.7, bullet 4. Do not claim it applies to the honours degree or that the issuer makes it a requirement. Set it beside 4.4.b11 and 4.7.b3 and the FHEQ level 7 descriptor qaa/fheq-2024/4.17.b4.1 (shared with FQHEIS level 11; spine:7)."
  author-agent-dialogue: "Raise this when a master's student drafts the critical or reflective part of the project. To a master's student, put it plainly in the second person as what work at this level shows; to staff, frame it as a design aim for the master's course and its final project. Ask: 'Which tradition does your project answer to, and where does it break new ground?' Avoid applying it to undergraduates or reading the list aloud."
- statement: qaa/creative-writing-2024/4.7.b5
  forPractitioner: { text: "At master's level, students show advanced analytical and imaginative skills for spotting, defining and solving the problems a professional writing project throws up; design the course and its final project so that they can.", rewrite: light, force: must, status: drafted }
  forBeneficiary: { text: "At master's level, you use advanced analytical and imaginative skills to spot, define and solve the problems your writing project raises.", rewrite: full, force: must, status: drafted }
  author-agent-written: "Describe this as a master's-level outcome that the statement describes for students achieving that level (plain present, force describes), at FHEQ level 7 (FQHEIS level 11): analytical and imaginative problem-solving in a professional project. Cite it as QAA (2024), Creative Writing Subject Benchmark Statement, para 4.7, bullet 5. Do not claim it applies to the honours degree or that the issuer makes it a requirement. Set it beside 4.7.b2 and 4.7.b9 and the FHEQ level 7 descriptor qaa/fheq-2024/4.17.b5 (shared with FQHEIS level 11; spine:7)."
  author-agent-dialogue: "Raise this when a master's student is stuck on a structural or practical problem. To a master's student, put it plainly in the second person as what work at this level shows; to staff, frame it as a design aim for the master's course and its final project. Ask: 'How did you define the problem before you tried to solve it?' Avoid applying it to undergraduates or reading the list aloud."
- statement: qaa/creative-writing-2024/4.7.b6
  forPractitioner: { text: "At master's level, students show a practical grasp of how they work as writers, what influences them and how they approach writing, so that they adapt skilfully to any creative challenge; design the course and its final project so that they can.", rewrite: light, force: must, status: drafted }
  forBeneficiary: { text: "At master's level, you know in practice how you work, what influences you and how you approach writing, so you can adapt well to any creative challenge.", rewrite: full, force: must, status: drafted }
  author-agent-written: "Describe this as a master's-level outcome that the statement describes for students achieving that level (plain present, force describes), at FHEQ level 7 (FQHEIS level 11): applied awareness of own process for adaptability. Cite it as QAA (2024), Creative Writing Subject Benchmark Statement, para 4.7, bullet 6. Do not claim it applies to the honours degree or that the issuer makes it a requirement. Set it beside 4.3.b2 and 4.6.b17 and the FHEQ level 7 descriptor qaa/fheq-2024/4.17.b6 (shared with FQHEIS level 11; spine:7)."
  author-agent-dialogue: "Raise this when a master's student meets an unfamiliar brief or form. To a master's student, put it plainly in the second person as what work at this level shows; to staff, frame it as a design aim for the master's course and its final project. Ask: 'How would you change your usual process for a form you have never tried?' Avoid applying it to undergraduates or reading the list aloud."
- statement: qaa/creative-writing-2024/4.7.b7
  forPractitioner: { text: "At master's level, students show the capacity to conduct their own research to support the project; design the course and its final project so that they can.", rewrite: light, force: must, status: drafted }
  forBeneficiary: { text: "At master's level, you carry out your own research to support your project.", rewrite: full, force: must, status: drafted }
  author-agent-written: "Describe this as a master's-level outcome that the statement describes for students achieving that level (plain present, force describes), at FHEQ level 7 (FQHEIS level 11): independent research for the project. Cite it as QAA (2024), Creative Writing Subject Benchmark Statement, para 4.7, bullet 7. Do not claim it applies to the honours degree or that the issuer makes it a requirement. Set it beside 4.4.b18 and the FHEQ level 7 descriptor qaa/fheq-2024/4.17.b2 (shared with FQHEIS level 11; spine:7)."
  author-agent-dialogue: "Raise this when a master's student plans project research. To a master's student, put it plainly in the second person as what work at this level shows; to staff, frame it as a design aim for the master's course and its final project. Ask: 'What research has changed the direction of your project?' Avoid applying it to undergraduates or reading the list aloud."
- statement: qaa/creative-writing-2024/4.7.b8
  forPractitioner: { text: "At master's level, students show advanced craft, editing and storytelling skills that move the work forward, including acting on feedback from peers and tutors and the confidence to judge for themselves how to make the project better; design the course and its final project so that they can.", rewrite: light, force: must, status: drafted }
  forBeneficiary: { text: "At master's level, you use advanced craft, editing and storytelling skills to move your work forward, respond to feedback from peers and tutors and trust your own judgement on how to make it better.", rewrite: full, force: must, status: drafted }
  author-agent-written: "Describe this as a master's-level outcome that the statement describes for students achieving that level (plain present, force describes), at FHEQ level 7 (FQHEIS level 11): advanced craft, editing and story skills; using feedback. Cite it as QAA (2024), Creative Writing Subject Benchmark Statement, para 4.7, bullet 8. Do not claim it applies to the honours degree or that the issuer makes it a requirement. Set it beside 4.4.b16 and 4.7.b10 and the FHEQ level 7 descriptor qaa/fheq-2024/4.17.b6 (shared with FQHEIS level 11; spine:7)."
  author-agent-dialogue: "Raise this when a master's student weighs conflicting feedback. To a master's student, put it plainly in the second person as what work at this level shows; to staff, frame it as a design aim for the master's course and its final project. Ask: 'Which feedback did you decide not to follow, and why?' Avoid applying it to undergraduates or reading the list aloud."
- statement: qaa/creative-writing-2024/4.7.b9
  forPractitioner: { text: "At master's level, students show the capacity to take part in analytical, critical group discussion, bringing problem-solving to bear on other writers' work; design the course and its final project so that they can.", rewrite: light, force: must, status: drafted }
  forBeneficiary: { text: "At master's level, you take part in analytical, critical group discussion and help solve problems in other writers' work.", rewrite: full, force: must, status: drafted }
  author-agent-written: "Describe this as a master's-level outcome that the statement describes for students achieving that level (plain present, force describes), at FHEQ level 7 (FQHEIS level 11): analytical group discussion and problem-solving on peers' work. Cite it as QAA (2024), Creative Writing Subject Benchmark Statement, para 4.7, bullet 9. Do not claim it applies to the honours degree or that the issuer makes it a requirement. Set it beside 4.7.b10 and 4.6.b13 and the FHEQ level 7 descriptor qaa/fheq-2024/4.17.b5 (shared with FQHEIS level 11; spine:7)."
  author-agent-dialogue: "Raise this when a master's student takes part in workshops. To a master's student, put it plainly in the second person as what work at this level shows; to staff, frame it as a design aim for the master's course and its final project. Ask: 'What problem in a peer's draft did you help them solve, and how?' Avoid applying it to undergraduates or reading the list aloud."
- statement: qaa/creative-writing-2024/4.7.b10
  forPractitioner: { text: "At master's level, students show the capacity to give feedback with sensitivity, for instance by showing a keen sense of what the writer is aiming for and weighing how varied backgrounds and experiences shape judgements of good writing; design the course and its final project so that they can.", rewrite: light, force: must, status: drafted }
  forBeneficiary: { text: "At master's level, you give feedback sensitively, showing you grasp what the writer is trying to do and that different backgrounds and experiences shape how people judge good writing.", rewrite: full, force: must, status: drafted }
  author-agent-written: "Describe this as a master's-level outcome that the statement describes for students achieving that level (plain present, force describes), at FHEQ level 7 (FQHEIS level 11): sensitive feedback. Cite it as QAA (2024), Creative Writing Subject Benchmark Statement, para 4.7, bullet 10. Do not claim it applies to the honours degree or that the issuer makes it a requirement. Set it beside 4.4.b16 and 4.6.b16 and the FHEQ level 7 descriptor qaa/fheq-2024/4.17.b8.1 (shared with FQHEIS level 11; spine:7)."
  author-agent-dialogue: "Raise this when a master's student gives workshop feedback. To a master's student, put it plainly in the second person as what work at this level shows; to staff, frame it as a design aim for the master's course and its final project. Ask: 'What was the writer trying to achieve, and did your feedback start there?' Avoid applying it to undergraduates or reading the list aloud."
- statement: qaa/creative-writing-2024/4.7.b11
  forPractitioner: { text: "At master's level, students show skill in adjusting writing style to varied media and narrative forms, weighing the creative risks and gains of technology as a tool for making and representing; design the course and its final project so that they can.", rewrite: light, force: must, status: drafted }
  forBeneficiary: { text: "At master's level, you adjust your writing style to different media and narrative forms, and weigh the creative risks and gains of using technology.", rewrite: full, force: must, status: drafted }
  author-agent-written: "Describe this as a master's-level outcome that the statement describes for students achieving that level (plain present, force describes), at FHEQ level 7 (FQHEIS level 11): adapting style across media; technology as a creative tool. Cite it as QAA (2024), Creative Writing Subject Benchmark Statement, para 4.7, bullet 11. Do not claim it applies to the honours degree or that the issuer makes it a requirement. Set it beside 4.5.b2 and 4.7.b12 and the FHEQ level 7 descriptor qaa/fheq-2024/4.17.b3 (shared with FQHEIS level 11; spine:7)."
  author-agent-dialogue: "Raise this when a master's student writes for digital or multimedia platforms. To a master's student, put it plainly in the second person as what work at this level shows; to staff, frame it as a design aim for the master's course and its final project. Ask: 'What does this technology add to the work, and what does it risk?' Avoid applying it to undergraduates or reading the list aloud."
- statement: qaa/creative-writing-2024/4.7.b12
  forPractitioner: { text: "At master's level, students show the capacity to evaluate, discuss, adapt and place their work in relation to wider social challenges such as sustainable development, diversity or the ethics of making work with AI and other new technologies; design the course and its final project so that they can.", rewrite: light, force: must, status: drafted }
  forBeneficiary: { text: "At master's level, you evaluate, discuss, adapt and place your work in relation to wider social questions such as sustainability, diversity or the ethics of using AI to create.", rewrite: full, force: must, status: drafted }
  author-agent-written: "Describe this as a master's-level outcome that the statement describes for students achieving that level (plain present, force describes), at FHEQ level 7 (FQHEIS level 11): positioning work within social challenges, including AI ethics. Cite it as QAA (2024), Creative Writing Subject Benchmark Statement, para 4.7, bullet 12. Do not claim it applies to the honours degree or that the issuer makes it a requirement. Set it beside 4.4.b14, 4.5.b4 and 4.5.b5 and the FHEQ level 7 descriptor qaa/fheq-2024/4.17.b5 (shared with FQHEIS level 11; spine:7)."
  author-agent-dialogue: "Raise this when a master's student uses AI tools or writes on social themes. To a master's student, put it plainly in the second person as what work at this level shows; to staff, frame it as a design aim for the master's course and its final project. Ask: 'How would you justify, to a reader, the way you used or avoided AI in this work?' Avoid applying it to undergraduates or reading the list aloud."
- statement: qaa/creative-writing-2024/4.7.b13
  forPractitioner: { text: "At master's level, students show the capacity to turn complex cultural material, and sometimes emotionally hard material, observation and experience, into effective creative writing with fitting narrative and literary forms and techniques, for example writing about people and place that changes how readers perceive other beings and their surroundings; design the course and its final project so that they can.", rewrite: light, force: must, status: drafted }
  forBeneficiary: { text: "At master's level, you turn complex and sometimes emotionally difficult material, observations and experiences into effective writing, using the right narrative and literary forms, for instance writing about people and place that changes how readers see other beings and the world around them.", rewrite: full, force: must, status: drafted }
  author-agent-written: "Describe this as a master's-level outcome that the statement describes for students achieving that level (plain present, force describes), at FHEQ level 7 (FQHEIS level 11): transforming complex and difficult material into effective writing. Cite it as QAA (2024), Creative Writing Subject Benchmark Statement, para 4.7, bullet 13. Do not claim it applies to the honours degree or that the issuer makes it a requirement. Set it beside 4.4.b14 and 4.5.b5 and the FHEQ level 7 descriptor qaa/fheq-2024/4.17.b5 (shared with FQHEIS level 11; spine:7)."
  author-agent-dialogue: "Raise this when a master's student writes from difficult personal or cultural material, with the support 3.18 describes in mind. To a master's student, put it plainly in the second person as what work at this level shows; to staff, frame it as a design aim for the master's course and its final project. Ask: 'What craft choices let you handle this material without being overwhelmed by it?' Avoid applying it to undergraduates or reading the list aloud."
- statement: qaa/creative-writing-2024/4.7.b14
  forPractitioner: { text: "At master's level, students show advanced teamwork, showing they can respond to fast-moving cultural industries, to professional challenges and to global contexts; design the course and its final project so that they can.", rewrite: light, force: must, status: drafted }
  forBeneficiary: { text: "At master's level, you work in teams at an advanced level and respond to fast-moving cultural industries, to professional challenges and to global settings.", rewrite: full, force: must, status: drafted }
  author-agent-written: "Describe this as a master's-level outcome that the statement describes for students achieving that level (plain present, force describes), at FHEQ level 7 (FQHEIS level 11): advanced teamwork in changing cultural industries. Cite it as QAA (2024), Creative Writing Subject Benchmark Statement, para 4.7, bullet 14. Do not claim it applies to the honours degree or that the issuer makes it a requirement. Set it beside 4.6.b13 and 4.4.b17 and the FHEQ level 7 descriptor qaa/fheq-2024/4.17.b8.2 (shared with FQHEIS level 11; spine:7)."
  author-agent-dialogue: "Raise this when a master's student works on a collaborative or industry project. To a master's student, put it plainly in the second person as what work at this level shows; to staff, frame it as a design aim for the master's course and its final project. Ask: 'How did your team adjust when the brief or the market changed?' Avoid applying it to undergraduates or reading the list aloud."
- statement: qaa/creative-writing-2024/4.7.b15
  forPractitioner: { text: "At master's level, students show the capacity to communicate well with specialists and non-specialists, shown through advanced writing, speaking and storytelling; design the course and its final project so that they can.", rewrite: light, force: must, status: drafted }
  forBeneficiary: { text: "At master's level, you communicate well with experts and non-experts through advanced writing, speaking and storytelling.", rewrite: full, force: must, status: drafted }
  author-agent-written: "Describe this as a master's-level outcome that the statement describes for students achieving that level (plain present, force describes), at FHEQ level 7 (FQHEIS level 11): communicating to specialist and non-specialist audiences. Cite it as QAA (2024), Creative Writing Subject Benchmark Statement, para 4.7, bullet 15. Do not claim it applies to the honours degree or that the issuer makes it a requirement. Set it beside 4.6.b10 and 4.6.b12 and the FHEQ level 7 descriptor qaa/fheq-2024/4.17.b5 (shared with FQHEIS level 11; spine:7)."
  author-agent-dialogue: "Raise this when a master's student presents work publicly or pitches to industry. To a master's student, put it plainly in the second person as what work at this level shows; to staff, frame it as a design aim for the master's course and its final project. Ask: 'How would you explain your project to a funder who has never read poetry?' Avoid applying it to undergraduates or reading the list aloud."
- statement: qaa/creative-writing-2024/4.7.b16
  forPractitioner: { text: "At master's level, students show the capacity to draw on their grasp of how creative writing can enrich lives to help themselves and others gain well-being, confidence, self-expression and self-awareness; design the course and its final project so that they can.", rewrite: light, force: must, status: drafted }
  forBeneficiary: { text: "At master's level, you use what you understand about writing as a life-enhancing skill to support your own and other people's well-being, confidence and self-expression.", rewrite: full, force: must, status: drafted }
  author-agent-written: "Describe this as a master's-level outcome that the statement describes for students achieving that level (plain present, force describes), at FHEQ level 7 (FQHEIS level 11): writing as a life-enhancing skill for well-being. Cite it as QAA (2024), Creative Writing Subject Benchmark Statement, para 4.7, bullet 16. Do not claim it applies to the honours degree or that the issuer makes it a requirement. Set it beside 4.6.b18 and the FHEQ level 7 descriptor qaa/fheq-2024/4.17.b8.1 (shared with FQHEIS level 11; spine:7)."
  author-agent-dialogue: "Raise this when a master's student plans community, teaching or well-being work. To a master's student, put it plainly in the second person as what work at this level shows; to staff, frame it as a design aim for the master's course and its final project. Ask: 'Where could your writing skills help other people, and how would you know it helped?' Avoid applying it to undergraduates or reading the list aloud."
```

### S5 Levels and alignment
<!-- label: both; status: drafted; basis: primary -->
```yaml
levels:
  - { id: "fheq:6", role: "cites", locator: "D1, 2.3" }
  - { id: "fqheis:10", role: "cites", locator: "D1, 2.3" }
  - { id: "fheq:7", role: "cites", locator: "D1, 2.10 (integrated master's); 4.7 (master's level, framework not named there)" }
  - { id: "fqheis:11", role: "cites", locator: "D1, 2.10" }
  - { id: "fheq:4", role: "mentions", locator: "D1, 3.5 (\"At Level 4\": framework not named; inferred FHEQ, Part E)" }
  - { id: "fheq:5", role: "mentions", locator: "D1, 3.6 (\"At Level 5\": framework not named; inferred FHEQ, Part E)" }
crosswalks:
  - { from: "fheq:6", to: "fqheis:10", relation: "equivalent", basis: "stated (D1, 2.3: \"FHEQ Level 6; FQHEIS Level 10\" for the degree with honours); matches std:doc:qaa-fheq-2024-framework Table 1" }
  - { from: "fheq:7", to: "fqheis:11", relation: "equivalent", basis: "stated (D1, 2.10: \"FHEQ Level 7; FQHEIS Level 11\" for the integrated master's); matches std:doc:qaa-fheq-2024-framework S5 (shared descriptor 4.17)" }
```

### S6 Themes
<!-- label: both; status: drafted; basis: primary -->
```yaml
- { id: "theme:edi", role: "carries", carriedIn: ["1.21", "1.22", "1.23", "1.24", "1.25", "1.26", "3.5", "3.6", "3.18", "3.19", "4.3", "4.4", "4.5", "4.6", "4.7"] }
- { id: "theme:accessibility", role: "carries", carriedIn: ["1.27", "1.28", "1.29", "1.30", "1.31", "1.32", "3.17", "3.18", "3.19", "3.22", "4.5"] }
- { id: "theme:esd", role: "carries", carriedIn: ["1.33", "1.34", "1.35", "1.36", "1.37", "1.38", "3.19", "4.3", "4.4", "4.5", "4.7"] }
- { id: "theme:enterprise", role: "carries", carriedIn: ["1.15", "1.16", "1.39", "1.40", "1.41", "2.6", "3.19", "4.3", "4.4", "4.5"] }
- { id: "theme:generative-ai", role: "carries", carriedIn: ["3.9", "3.20", "3.26", "3.32", "4.7"] }
```

### S7 Relations
<!-- label: both; status: drafted; basis: primary -->
```yaml
- { rel: "partOf", target: "collection: QAA Subject Benchmark Statements", note: "one of 54 held by stan" }
- { rel: "supersedes", target: "std:doc:qaa-creative-writing-2019-benchmarks (not ingested)", note: "section 6 names the second edition (2019) and the original (2016); the closing line names this the third edition (D1, section 6)" }
- { rel: "refersTo", target: "std:doc:qaa-fheq-2024-framework, Annex D", note: "the four honours classifications, for achievement above threshold (D1, 4.2)" }
- { rel: "refersTo", target: "std:doc:qaa-fheq-2024-framework", note: "FHEQ Levels 6 and 7 (D1, 2.3, 2.10)" }
- { rel: "refersTo", target: "std:doc:qaa-fqheis-2024-framework", note: "FQHEIS Levels 10 and 11 (D1, 2.3, 2.10)" }
- { rel: "refersTo", target: "std:doc:qaa-advancehe-esd-2021-guidance", note: "listed in section 5; the sustainability paragraphs cite UNESCO (2017) directly (1.33, 1.34)" }
- { rel: "refersTo", target: "std:doc:qaa-enterprise-2018-guidance", note: "listed in section 5, behind the enterprise paragraphs (1.39 to 1.41)" }
- { rel: "refersTo", target: "QAA Quality Code for Higher Education and its Advice and Guidance (not ingested)", note: "front matter; section 5" }
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
- An artistic and critical discipline centred on imagination, curiosity and the power of language, whose focus is generating ideas and expressing originality through literary, poetic or narrative forms (D1, 1.1, 1.8, 1.9).
- Making texts sits at the centre: students develop their own creative practice and methods, drafting and redrafting, across many genres, forms and media, from print to performance, screen, audio, games and new forms (D1, 1.2, 1.8, 3.1).
- Originality is understood as emerging from the writer's own cultural, literary and personal contexts in dialogue with existing forms, influences and techniques (D1, 1.10).
- Learning is collaborative and workshop-based, with peer and tutor feedback at its heart, alongside independent study (D1, 1.2, 1.4, 1.20, 3.17, 3.23).
- Reading is broad and includes craft, criticism, theory and other media; projects may be creative-critical, and creative writing is itself a form of research (D1, 1.5, 1.11 to 1.13).
- Highly interdisciplinary: studied alone or in many combinations, drawing on literature, drama, poetics, mythology, folklore, rhetoric and more (D1, 1.2, 1.3, 1.18, 3.2, 3.3).
- Strongly tied to the creative industries and wider careers, and to well-being and personal confidence in self-expression (D1, 1.1, 1.7, 1.16).

### SB2 Themes in this subject
<!-- label: both; status: drafted; basis: primary -->
```yaml
- theme: theme:edi
  inThisSubject: "inclusive learning communities and reading lists in line with the Equality Act 2010, belonging, participation plans in the four nations, external agencies tackling inequality in publishing and students defining their own canon of forms and voices; graduates show understanding of equality and engage with diverse writers and voices (D1, 1.21 to 1.26, 3.18, 3.19, 4.6)"
  statements: ["qaa/creative-writing-2024/4.3.b9", "qaa/creative-writing-2024/4.4.b15", "qaa/creative-writing-2024/4.5.b4", "qaa/creative-writing-2024/4.5.b8", "qaa/creative-writing-2024/4.6.b14", "qaa/creative-writing-2024/4.7.b10", "qaa/creative-writing-2024/4.7.b12"]
- theme: theme:accessibility
  inThisSubject: "many routes of entry, portfolio or presentation in place of written entry tests, accessible materials and spaces, prepared and adapted workshops, support for writing about personal themes and accessible assessment with alternatives (D1, 1.27 to 1.32, 3.17, 3.18, 3.22)"
  statements: ["qaa/creative-writing-2024/1.31", "qaa/creative-writing-2024/3.22", "qaa/creative-writing-2024/4.5.b4"]
- theme: theme:esd
  inThisSubject: "nature and environmental writing, the human and the more than human, ecological thinking through story and UNESCO's key competencies (critical, self-aware and anticipatory thinking); the rungs move from awareness to imaginative exploration to transformative writing on sustainability (D1, 1.33 to 1.38, 4.3, 4.4, 4.5, 4.7)"
  statements: ["qaa/creative-writing-2024/4.3.b11", "qaa/creative-writing-2024/4.4.b14", "qaa/creative-writing-2024/4.5.b5", "qaa/creative-writing-2024/4.7.b12", "qaa/creative-writing-2024/4.7.b13"]
- theme: theme:enterprise
  inThisSubject: "careers in the creative industries and beyond, creative entrepreneurship, writing to commission and to briefs, with a list of enterprise skills the subject builds; the rungs move from awareness of applications to strategic transfer to new spaces for entrepreneurial expression (D1, 1.15, 1.16, 1.39 to 1.41, 4.3, 4.4, 4.5)"
  statements: ["qaa/creative-writing-2024/4.3.b10", "qaa/creative-writing-2024/4.4.b19", "qaa/creative-writing-2024/4.5.b6", "qaa/creative-writing-2024/4.6.b15"]
- theme: theme:generative-ai
  inThisSubject: "AI as content and tool: courses explore its limits and possibilities, analyse its effect on creative industries and use it to develop material with transparency; submissions may engage with AI; assessment of originality and methods may need to change; master's students weigh the ethics of using AI (D1, 3.9, 3.20, 3.26, 3.32, 4.7)"
  statements: ["qaa/creative-writing-2024/4.7.b12"]
```

### SB3 Content and delivery
<!-- label: both; status: drafted; basis: primary -->
```yaml
areas:
  - { component: "1.12", gloss: "reading: traditional and contemporary models, games, audio, podcasts, criticism and theory" }
  - { component: "3.1", gloss: "making texts in literary, poetic, narrative and multimodal forms" }
  - { component: "3.5", gloss: "Level 4: habits of writing, principal forms, reader and audience, language and contexts" }
  - { component: "3.6", gloss: "Level 5: craft techniques, reflective practice, reading and practice, context and diversity" }
  - { component: "3.7", gloss: "Level 6: advanced modules, extended project, languages and dialects, research practices, live briefs" }
  - { component: "3.8", gloss: "a community of practice and individual and collective voices" }
  - { component: "3.9", gloss: "digital, multi-platform and multimodal forms, games, graphic novels and AI" }
practices:
  - { component: "3.10", kind: "teaching", gloss: "direct instruction, discussion of student work, experiment, risk-taking and failure" }
  - { component: "3.12", kind: "learning", gloss: "preparatory exercises, prompts and pieces for feedback" }
  - { component: "3.13", kind: "teaching", gloss: "lectures, seminars and workshops; in person, online, hybrid, on site" }
  - { component: "3.14", kind: "teaching", gloss: "seminars, small workshops, tutorials, supervision, online activity" }
  - { component: "3.16", kind: "learning", gloss: "collaborative and independent study with reflection" }
  - { component: "3.17", kind: "teaching", gloss: "presenting work in writing rooms and workshops, with accessible practice" }
  - { component: "3.18", kind: "teaching", gloss: "support for writing on personal and difficult themes" }
  - { component: "3.21", kind: "assessment", gloss: "portfolio, dissertation or capstone research project" }
  - { component: "3.23", kind: "assessment", gloss: "formative assessment through workshops and self-critique" }
  - { component: "3.24", kind: "assessment", gloss: "written feedback on work in progress" }
  - { component: "3.26", kind: "assessment", gloss: "forms of submission, from novel extracts and scripts to pitches and collaborative projects" }
  - { component: "3.27", kind: "assessment", gloss: "students devising assignments and criteria with tutors" }
  - { component: "3.28", kind: "assessment", gloss: "clear, shared criteria used in peer and self-evaluation" }
  - { component: "3.29", kind: "assessment", gloss: "what criteria may evaluate, from originality to engagement with feedback" }
  - { component: "3.31", kind: "assessment", gloss: "assessing workshop facilitation and contribution" }
```

### SB4 Benchmark standards
<!-- label: both; status: drafted; basis: primary -->
```yaml
rungs:
  - { rung: "threshold", leadIn: "4.3", award: "bachelor's with honours", items: 13 }
  - { rung: "typical", leadIn: "4.4", award: "bachelor's with honours", items: 19 }
  - { rung: "excellent", leadIn: "4.5", award: "bachelor's with honours", items: 11 }
rungBases: "4.1: the statement sets minimum, typical and excellent standards that students will have demonstrated at the award of honours; 4.2: most students do significantly better than the threshold, judged by each provider with Annex D; 4.5: the excellent rung is a lead paragraph (two records: the integrating standard, and a should on industry presentation standards) and a list of which excellent graduates show some; 4.6: generic skills, outside the rungs; 4.7: master's level, outside the rungs"
outcomeLists:
  - { leadIn: "2.2", gloss: "what students will do through study of the subject", items: 7, award: ["bachelor's with honours"] }
  - { leadIn: "4.6", gloss: "generic skills honours graduates should be able to show", items: 18, award: ["bachelor's with honours"] }
  - { leadIn: "4.7", gloss: "what students achieving master's level show (plain present; force describes)", items: 16, award: ["master's"] }
outcomes:
  - { outcome: "generating and developing work", threshold: "qaa/creative-writing-2024/4.3.b1", typical: "qaa/creative-writing-2024/4.4.b1", excellent: "none", basis: "inferred", domain: "subject-skill", award: "bachelor's with honours" }
  - { outcome: "reflection on own practice", threshold: "qaa/creative-writing-2024/4.3.b2", typical: "qaa/creative-writing-2024/4.4.b2", excellent: "qaa/creative-writing-2024/4.5.b7", basis: "inferred", domain: "subject-skill", award: "bachelor's with honours" }
  - { outcome: "reading and responding to work", threshold: "qaa/creative-writing-2024/4.3.b6", typical: "qaa/creative-writing-2024/4.4.b9", excellent: "none", basis: "inferred", domain: "subject-skill", award: "bachelor's with honours" }
  - { outcome: "historical and cultural dimensions of language", threshold: "qaa/creative-writing-2024/4.3.b7", typical: "qaa/creative-writing-2024/4.4.b10", excellent: "none", basis: "inferred", domain: "understanding", award: "bachelor's with honours" }
  - { outcome: "communicating with diverse audiences across forms and media", threshold: "qaa/creative-writing-2024/4.3.b8", typical: "qaa/creative-writing-2024/4.4.b13", excellent: "qaa/creative-writing-2024/4.5.b2", basis: "inferred", domain: "subject-skill", award: "bachelor's with honours" }
  - { outcome: "inclusive work with others", threshold: "qaa/creative-writing-2024/4.3.b9", typical: "qaa/creative-writing-2024/4.4.b15", excellent: "none", basis: "inferred", domain: "generic-skill", award: "bachelor's with honours" }
  - { outcome: "transferring skills to careers and enterprise", threshold: "qaa/creative-writing-2024/4.3.b10", typical: "qaa/creative-writing-2024/4.4.b19", excellent: "none", basis: "inferred", domain: "understanding", award: "bachelor's with honours" }
  - { outcome: "what language can do", threshold: "none", typical: "qaa/creative-writing-2024/4.4.b6", excellent: "qaa/creative-writing-2024/4.5.b3", basis: "inferred", domain: "subject-skill", award: "bachelor's with honours" }
  - { outcome: "place, planet and other species", threshold: "none", typical: "qaa/creative-writing-2024/4.4.b14", excellent: "qaa/creative-writing-2024/4.5.b5", basis: "inferred", domain: "subject-skill", award: "bachelor's with honours" }
  - { outcome: "co-writing and co-production", threshold: "none", typical: "qaa/creative-writing-2024/4.4.b17", excellent: "qaa/creative-writing-2024/4.5.b9", basis: "inferred", domain: "subject-skill", award: "bachelor's with honours" }
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
- { body: "professional, statutory and regulatory bodies (PSRBs), unnamed", says: "the statement supports them on academic standards, and their requirements are a further reference point in course design (D1, front matter)", requirements: "not-applicable-by-design: no body named (Part E)" }
- { body: "Office for Students (regulator, England)", says: "under its regulatory framework the statements are not sector-recognised standards in England (D1, front matter)", requirements: "not yet ingested (Part E)" }
```

### SB6 Cross-cutting references
<!-- label: both; status: drafted; basis: primary -->
```yaml
themes:
  - { id: "theme:edi", named: "Equality, diversity and inclusion", carriedIn: ["1.21", "1.22", "1.23", "1.24", "1.25", "1.26", "3.5", "3.6", "3.18", "3.19", "4.3", "4.4", "4.5", "4.6", "4.7"], statements: ["4.3.b9", "4.4.b15", "4.5.b4", "4.5.b8", "4.6.b14", "4.7.b10", "4.7.b12"] }
  - { id: "theme:accessibility", named: "Accessibility (front matter: accessibility and the needs of disabled students)", carriedIn: ["1.27", "1.28", "1.29", "1.30", "1.31", "1.32", "3.17", "3.18", "3.19", "3.22", "4.5"], statements: ["1.31", "3.22", "4.5.b4"] }
  - { id: "theme:esd", named: "Sustainability (front matter: education for sustainable development)", carriedIn: ["1.33", "1.34", "1.35", "1.36", "1.37", "1.38", "3.19", "4.3", "4.4", "4.5", "4.7"], statements: ["4.3.b11", "4.4.b14", "4.5.b5", "4.7.b12", "4.7.b13"] }
  - { id: "theme:enterprise", named: "Enterprise and entrepreneurship education (front matter: employability, entrepreneurship and enterprise education)", carriedIn: ["1.15", "1.16", "1.39", "1.40", "1.41", "2.6", "3.19", "4.3", "4.4", "4.5"], statements: ["4.3.b10", "4.4.b19", "4.5.b6", "4.6.b15"] }
  - { id: "theme:generative-ai", named: "artificial intelligence (AI); generative AI", carriedIn: ["3.9", "3.20", "3.26", "3.32", "4.7"], statements: ["4.7.b12"] }
frameworks:
  - { framework: "fheq", levels: ["fheq:6", "fheq:7"], citedIn: ["2.3", "2.10", "4.2"] }
  - { framework: "scqf", levels: ["fqheis:10", "fqheis:11"], citedIn: ["2.3", "2.10"] }
bodies:
  - { body: "PSRBs (unnamed)", citedIn: ["front matter"] }
  - { body: "Office for Students (regulator, England)", citedIn: ["front matter"] }
  - { body: "UCAS (admissions; disclosure of disability)", citedIn: ["1.28"] }
  - { body: "UNESCO (source of the ESD definition and key competencies)", citedIn: ["1.33", "1.34"] }
sharedDocuments:
  - { document: "std:doc:qaa-fheq-2024-framework, Annex D", named: "Annex D in The Frameworks for Higher Education Qualifications of UK Degree-Awarding Bodies", citedIn: ["4.2", "5"], role: "descriptions of the four honours classifications (1st, 2.1, 2.2, 3rd), for achievement above threshold" }
  - { document: "std:doc:qaa-advancehe-esd-2021-guidance", named: "QAA and Advance HE (2021) Education for Sustainable Development Guidance", citedIn: ["5"], role: "listed reference behind the sustainability paragraphs" }
  - { document: "std:doc:qaa-enterprise-2018-guidance", named: "QAA (2018) Enterprise and Entrepreneurship Education: Guidance for UK Higher Education Providers", citedIn: ["5"], role: "listed reference behind the enterprise paragraphs" }
  - { document: "UNESCO (2017) Education for Sustainable Development Goals: Learning Objectives (external, not ingested)", named: "UNESCO, 2017; UNESCO's Key Competencies for Sustainable Development", citedIn: ["1.33", "1.34", "5"], role: "definition of ESD and the key competencies the subject develops" }
  - { document: "Equality Act 2010 (legislation, not ingested)", named: "the Equality Act 2010", citedIn: ["1.21", "5"], role: "the principles that texts and community-building align with" }
  - { document: "Research Excellence Framework (external, not ingested)", named: "the Research Excellence Framework", citedIn: ["1.5"], role: "acknowledges creative writing as research" }
  - { document: "QAA Quality Code, Advice and Guidance (not yet ingested)", named: "Advice and Guidance to support the Quality Code for Higher Education; The UK Quality Code for Higher Education", citedIn: ["front matter", "5"], role: "course design, teaching, external expertise, monitoring" }
  - { document: "QAA Glossary (not ingested)", named: "QAA's Glossary", citedIn: ["front matter", "5"], role: "explains unfamiliar terms" }
  - { document: "Quality Assessment Framework for Wales; Quality Enhancement Framework (Scotland); Quality Enhancement Review (Wales) (not ingested)", named: "the same", citedIn: ["front matter", "5"], role: "where the statement is a key reference point" }
  - { document: "Access and Participation Plans (England); Enhancement-led Institutional Review (Scotland); Access to Success Strategy (Northern Ireland); Strategic Equality Plan (Wales) (not ingested)", named: "the same", citedIn: ["1.24"], role: "institution-level routes to wider participation" }
```

## Part B Terminology
<!-- The statement has no glossary of its own unless Part E says so; these are terms it defines in its text. -->

### B1 Concepts
<!-- label: both; status: drafted; basis: primary -->
```yaml
- { slug: "threshold-standard", definition: "the minimum a student will have demonstrated to be awarded the honours degree (D1, 4.1, 4.3)", beneficiaryDefinition: "the least you must have shown by the end of your honours degree", scopeNote: "the list in 4.3", category: "unknown", practices: ["education"] }
- { slug: "typical-standard", definition: "what most honours graduates will have demonstrated, above the threshold (D1, 4.1, 4.4)", beneficiaryDefinition: "what most people show by the end of the degree", scopeNote: "the list in 4.4", category: "unknown", practices: ["education"] }
- { slug: "excellent-standard", definition: "the lower rungs integrated with enterprise and flair, with some of a further list of qualities (D1, 4.1, 4.5)", beneficiaryDefinition: "what the strongest work shows, beyond the typical", scopeNote: "graduates show some, not all, of the list", category: "unknown", practices: ["education"] }
- { slug: "originality", definition: "writing that reflects the writer's own cultural, literary and personal contexts, reached gradually by joining individual expression with existing forms and techniques (D1, 1.10)", beneficiaryDefinition: "work only you could have written, made from your own contexts in dialogue with what exists", category: "unknown", practices: ["education"] }
- { slug: "workshop", definition: "a collaborative or peer-led session where students read work in progress and peers, invited by the tutor, respond (D1, 1.31, 3.17)", beneficiaryDefinition: "a class where you share a draft and others give feedback", scopeNote: "also writing rooms", category: "unknown", practices: ["education"] }
- { slug: "creative-critical", definition: "a project whose creative text also makes a critical or theoretical argument or explores process, method and technique (D1, 1.13)", category: "unknown", practices: ["education"] }
```

### B2a Terms as the issuer defines them
<!-- label: source; status: drafted; basis: primary -->
```yaml
- { concept: "threshold-standard", form: "threshold standard", lang: "en", partOfSpeech: "noun-phrase", termStatus: "preferred", register: "formal" }
- { concept: "typical-standard", form: "typical standard", lang: "en", partOfSpeech: "noun-phrase", termStatus: "preferred", register: "formal" }
- { concept: "excellent-standard", form: "excellent standard", lang: "en", partOfSpeech: "noun-phrase", termStatus: "preferred", register: "formal" }
- { concept: "originality", form: "Originality", lang: "en", partOfSpeech: "noun", termStatus: "preferred", register: "discipline-specific" }
- { concept: "workshop", form: "workshops", lang: "en", partOfSpeech: "noun", termStatus: "preferred", register: "discipline-specific" }
- { concept: "creative-critical", form: "creative-critical", lang: "en", partOfSpeech: "adjective", termStatus: "preferred", register: "discipline-specific" }
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
  title: "Subject Benchmark Statement Creative Writing"
  edition: "April 2024 (third edition)"
  year: 2024
  url: unknown (the QAA page; the text came by stan's extraction)
  retrieved: "held from stan: wkspc2615-QAAVector mapped/creative-writing-2024/creative-writing-2024.raw.txt, commit 366bcb99a01118f2c4c3ebfa2a8337596bddc455; received 2026-10-03"
  licence: QAA copyright
  tier: primary
  readVia: direct
  held: 78b6f29fa59e46757a2316de6e1561bf33038430fa3952d40e498deb76d3cc89
  heldFiles: ["wkspc2601-library/txt/qaa-2024-creative-writing-subject-benchmark-statement-standard.txt", "wkspc2601-library/txt/qaa-2024-creative-writing-subject-benchmark-statement-standard.norm.txt", "wkspc2601-library/records/qaa-2024-creative-writing-subject-benchmark-statement-standard.chunks.json", "wkspc2601-library/records/qaa-2024-creative-writing-subject-benchmark-statement-standard.held.json"]
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
- SB4, rung shape: three lists with lead-ins naming the rung, as in Psychology (4.3 threshold 13, 4.4 typical 19, 4.5 excellent 9), but the excellent lead-in 4.5 says graduates show 'some of the following', so no excellent item is expected of every excellent graduate. The lead paragraph of 4.5 is itself recorded as two excellent statements (4.5: the integrating standard; 4.5.s2: the industry presentation standard, 'should'), so the excellent rung counts 11 records.
- S4, id 4.5.s2: our id for 4.5's second sentence, which carries its own 'should'; it is not the issuer's numbering and the builder sorts it after the numbered records.
- S4, force: threshold items take `threshold` from 4.1 ('minimum ... standards that students will have demonstrated'); typical and excellent items, whose lead-ins have no modal ('demonstrate'), take `will` from 4.1 by `forceFrom`. Generic skills (4.6) take `should` from their lead-in. For Abbott at P3.
- S4, 4.7 master's level: the lead-in is plain present ('students achieving master's level demonstrate'), and 4.1's 'will' covers the honours degree only, so the 16 items are recorded with force `describes`. For Abbott: read as will? Their level is recorded as fheq:7 from 2.10 (integrated master's, 'FHEQ Level 7; FQHEIS Level 11'); 4.7 names no framework and 3.33 speaks of master's degrees generally.
- S4, 2.2: an outcome list in 'will' under Design ('Through study of the subject, Creative Writing students will'); recorded as 7 outcome items at fheq:6, the level inferred from 2.3.
- S4, paragraphs taken as statements: 1.20 (should, a provider expectation in the last sentence; the paragraph is the record), 1.31 ('required', recorded as must), 2.3 (will, with 'it is expected that'), 2.7 (will), 3.22 (should), 4.2 (should).
- S4, not taken as statements (D-std-0002 (a)): the purposes list after 1.7 and the list in 1.10 (aims and descriptions, no modal; 1.10's 'will always exhibit innovation' describes originality); 1.11 ('will involve', descriptive); 1.41 (skills the subject 'enables', no outcome lead-in); 2.1 (design characteristics); 2.4 and 2.5 ('will seek', 'will introduce', 'may be expected': predictive or hedged); 2.9 ('it would be expected', 'would be capable': outside the five words); 3.14 ('will usually'); 3.32 ('will need to consider', a forecast for the discipline); 3.33 ('the added expectation that graduates are prepared': plain present, outside the five words).
- S4, plain-present provider norms not recorded as statements (template open point 5): 1.21 (texts 'are selected to act in alignment' with the Equality Act 2010), 1.30 (course designers and tutors 'consider accessibility'; 'they aim to ensure' a list of five), 2.14 to 2.16 (review, externality, examiners), 3.25 (outcomes and criteria 'are clearly articulated'), 3.28 (criteria 'are as clear, itemised and transparent as possible'), 3.30 ('care is taken'). 1.32's 'an adaptable approach may be required' is hedged by may and not taken.
- S4, skeleton corrections by `find`: 1.20, 2.2.b7, 2.3, 3.22, 4.2, 4.5.b9 and 4.6.b18, whose skeleton spans ran on into the next heading or a page number; 1.31 and 2.7 cut without their paragraph numbers. 4.5 is cut as its first sentence and 4.5.s2 as its second; the lead-in's last sentence stays with the stem.
- S4, gradeOf: 12 links, all inferred (the issuer lists each rung separately and pairs nothing): 4.4.b1, b2, b9, b10, b13, b15, b19 to the threshold list; 4.5.b2, b3, b5, b7, b9 to the typical list. Less plain matches, for P3: 4.4.b15 to 4.3.b9 (inclusive group work against engaging diverse writers), 4.5.b3 to 4.4.b6 (inventive language against creative engagement with language), 4.5.b7 to 4.4.b2 (reflection; the excellent item adds interdisciplinary connection).
- S4, gradeOf not drawn where the content matches but the domain shifts from awareness to use, since a link must keep its domain: 4.4.b5 (using language conventions) against 4.3.b5 (awareness of them, knowledge); 4.4.b14 (exploring place and planet) against 4.3.b11 (awareness of the subject's contribution to sustainability, understanding). The outcomes 'what language can do', 'place, planet and other species' and 'co-writing' start at the typical rung.
- S4, domain: our reading, not stated. Awareness items are knowledge where they concern techniques or language rules (4.3.b4, b5, b12) and understanding where they concern contexts and applications (4.3.b7, b10, b11). 4.3.b9 (awareness of group-work skills) is generic-skill. 4.4.b1 says 'original Creative Writing skills', read as original writing.
- S4, 4.6.b14 points to 'paragraphs 1.21-1.24' (the EDI paragraphs); a reference, not cut (DPN-1). 4.6.b14 has no matching FHEQ level 6 descriptor; its aaw points to personal responsibility (4.15.b9.1) as the nearest.
- S4, verbs: noun-phrase items (4.3.b3 to b5, b7, b9 to b12; 4.4.b2, b6 to b8, b10, b12, b16, b17, b19; 4.5.b2, b3) give no action verb, so `verbs` is empty; 4.6.b3's 'self-manage' and 4.6.b9 to 4.7 items' auxiliaries are left out.
- S3: the purposes list (16 bullets) belongs to the heading 'Purposes of Creative Writing in higher education' after 1.7 and is held in the skeleton's component 1.7; the heading 'Characteristics of Creative Writing in higher education' follows it, before 1.8. Sub-heading ranges in SUB are ours, from the heading lines.
- S5 and SB6, frameworks: FHEQ by name in 2.3, 2.10 and 4.2 (Frameworks, Annex D); FQHEIS in 2.3 and 2.10. 3.5 to 3.7 say 'Level 4', 'Level 5' and 'Level 6' without naming a framework: read as FHEQ levels (inferred) and recorded in S5 as mentions only. CQFW is not cited. 'Scottish Highers' (1.27) and the four-year Scottish honours degree (2.8) name no framework.
- SB5 and SB6, bodies: no professional body for the subject is named; PSRBs appear only generically (front matter). The Office for Students is named as England's regulator. UCAS (1.28) and UNESCO (1.33, 1.34) are named organisations, not PSRBs; listed in SB6 only.
- SB6, themes: the generative AI material (3.9, 3.20, 3.26 bullet 12, 3.32, 4.7.b12) is recorded as theme:generative-ai by the batch 1 convention; the issuer has no AI section of its own. TH tags in S4 only 1.31, the one statement inside a theme's own paragraphs; SB2 and SB6 list the statements elsewhere that carry a theme.
- SB6, shared documents: the ESD guidance (2021) and the enterprise guidance (2018) are cited only in section 5 (excluded matter); the body text cites UNESCO (2017) directly. citedIn '5' marks the reference list.
- S2, subjects: HECoS 100046 and CAH19-01-05 are the subject's own name ('creative writing'), entered as stated; CAH19-01 (English studies), the CAH2 group above it, is inferred. Scriptwriting (100729) and poetry writing (100730), in the same CAH3 group, are not named as subjects and are not entered.
- S7, supersedes: section 6 names the 2019 second edition and the 2016 original; this is the third edition (April 2024). The 2023 advisory group is the one that wrote this edition.
- Patterns differing from Psychology: an excellent lead-in that asks for 'some of' its list and carries a 'should' of its own (industry presentation standard); generic skills as a separate should-list (4.6); a master's list in plain present (4.7); an outcome list in section 2 (2.2) rather than section 3; lead-ins with no modal ('demonstrate'); a generative AI strand across content and assessment; no professional body.
- S9: not researched in P1.
- S1, licence: the text gives a copyright notice and no re-use terms; QAA's terms for holding and chunking are still to check.
- ST-12: versions here run to the lengths the content needs; no length range is yet set.

---

## Change notes
- 0.1.2, 3 October 2026, 21:02: moved with its held text from UNI to the source library repo (`wkspc2601-library/ingested/standards/`, texts in `txt/`, records in `records/`); paths only (Abbott, 20:56; std N-0119).
- 0.1.1, 3 October 2026, 20:20: obliging words outside the five read as must, "ought to" as should, on statements outside the rungs, each marked on its force line (Abbott, 20:17; D-std-0016).
- 0.1.0, 2026-10-03 16:53: researched by run frame 0.1.1-draft and standards run layer 0.7.0-draft, std, run 0097 (P1); built by tools/bm_build.py.
