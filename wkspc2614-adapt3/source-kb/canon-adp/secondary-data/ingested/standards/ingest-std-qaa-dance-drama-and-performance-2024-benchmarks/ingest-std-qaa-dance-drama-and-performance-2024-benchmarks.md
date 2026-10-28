---
id: std:doc:qaa-dance-drama-and-performance-2024-benchmarks
title: "Subject Benchmark Statement Dance, Drama and Performance"
profile: standards/subject-benchmark
profileVersion: 0.2.0-draft
issuer: QAA
kind: subject-benchmark
jurisdiction: [UK]
subjectScope: subjects
subjects:
  - { scheme: "hecos", code: "100068", label: "dance", basis: "stated" }
  - { scheme: "hecos", code: "100069", label: "drama", basis: "stated" }
  - { scheme: "hecos", code: "100071", label: "performing arts", basis: "stated" }
  - { scheme: "cah", code: "CAH25-02-04", label: "dance", basis: "stated" }
  - { scheme: "cah", code: "CAH25-02-03", label: "drama", basis: "stated" }
  - { scheme: "cah", code: "CAH25-02-01", label: "performing arts (non-specific)", basis: "stated" }
  - { scheme: "cah", code: "CAH25-02", label: "performing arts", basis: "stated" }
  - { scheme: "hecos", code: "100067", label: "acting", basis: "stated" }
  - { scheme: "hecos", code: "100035", label: "musical theatre", basis: "stated" }
  - { scheme: "hecos", code: "100698", label: "theatre studies", basis: "stated" }
  - { scheme: "hecos", code: "100708", label: "stage design", basis: "inferred" }
  - { scheme: "hecos", code: "100710", label: "community theatre", basis: "inferred" }
  - { scheme: "hecos", code: "100700", label: "theatre production", basis: "inferred" }
edition: "April 2024 (fifth edition)"
published: 2024-04
status: current
supersedes: "the fourth edition (2019), named in the membership section (section 6)"
heldText: { method: sha256-bytes, raw: 33cac4483fa4445fc15ce646384e70a94c23d0201949ce0847bcafe96baad525, normalised: e36610ace7ca981186c5a8f064d7811ce9867edc053c7bd97867735b988bb4e5 }
heldTextStan: { method: sha256-stan, raw: 33cac4483fa4445fc15ce646384e70a94c23d0201949ce0847bcafe96baad525, normalised: 1d7e6a7c828a85a00124fcaee1a56a69fd540b0d5500c7a8319e706c2b1ce840 }
licence: "QAA copyright; held for study, private to the project, never published"
series: "QAA Subject Benchmark Statements, the 2022 onward revision with cross-cutting themes (fifth edition of this statement)"
awardsCovered: ["bachelor's with honours", "master's"]
levelsCovered: ["fheq:6", "fqheis:10", "fheq:7", "fqheis:11"]
nations: ["England", "Wales", "Scotland", "Northern Ireland"]
parts:
  S: full
  B: "partial: no glossary in the document (it points to QAA's Glossary); terms it defines in passing"
  C: "not-applicable: the document sets expectations, not a procedure"
pins: { structure: 0.13.0-draft, template: 0.8.0-draft, benchmarkTemplate: 0.6.0-draft, runFrame: 0.1.1-draft, runLayer: 0.7.0-draft, standards: none yet, terminology: none yet }
lifecycle: drafted
researchedBy: run frame 0.1.1-draft; standards run layer 0.7.0-draft; std, run 0099 (tools/bm_build.py)
passes:
  P1: "2026-10-03 16:54"
  P2: "skipped: read direct from the held text; inferred codes and rung links are for P3"
  P3: open
version: 0.1.2
---

<!-- from INGEST wpk-0016-ingest-pd-template-standards.md 0.8.0-draft and wpk-0016-ingest-pd-template-standards-benchmark.md 0.6.0-draft; built by tools/bm_build.py from run-src/ -->
# Subject Benchmark Statement: Dance, Drama and Performance (QAA, April 2024)

> Run 0099, P1 by std. The issuer's words are held in the source library, `wkspc2601-library/txt/qaa-2024-dance-drama-performance-subject-benchmark-statement-standard.norm.txt`; each S4 record carries its statement in full (`source`) for language analysis, with its span. Paraphrases and versions are ours. Private to the project, never published. In front matter `status` is the issuer's; ours is `lifecycle`. Doubts are in Part E.

## Part 0 Summary

### 0.1 Agent definition
<!-- label: editorial; status: drafted; basis: primary -->
QAA's UK reference point for what a graduate in dance, drama, theatre and performance should know and be able to do, with honours standards at three rungs (threshold, typical, excellent), each split into subject knowledge and understanding, subject-specific skills and generic skills, and a short list for master's study. Reach for it when designing, approving, reviewing or describing a performance course, its outcomes or its marking. It is not a curriculum and not a regulatory requirement in England; its outcomes are indicative, written for single honours.

### 0.2 Summary
<!-- label: both; status: drafted; basis: primary -->
Published by QAA in April 2024 as the fifth edition, the statement covers undergraduate and taught postgraduate courses in dance, drama and performance and associated areas such as acting, musical theatre and scenography. It sets out the field's context and purposes, its distinctive features (design, progression, flexibility, partnerships, monitoring and review), its content, teaching, learning and assessment, and benchmark standards for the honours degree at threshold (30 items), typical (24) and excellent (24) rungs, each in three lists, plus five master's outcomes at FHEQ level 7. It carries four cross-cutting themes (equality, diversity and inclusion; accessibility; sustainability; enterprise and entrepreneurship education), a paragraph on generative AI, points to Annex D for the degree classes and names professional, statutory and regulatory bodies only in general.

## Part S Standard

### S1 Identity
<!-- label: source; status: drafted; basis: primary -->
```yaml
issuer: The Quality Assurance Agency for Higher Education
title: "Subject Benchmark Statement Dance, Drama and Performance"
edition: "April 2024 (fifth edition)"
dates:
  published: 2024-04
  other: []
kind: subject-benchmark
jurisdiction: [UK]
authority: "reference: a sector reference point, not a regulatory requirement (D1, front matter); in England not a sector-recognised standard under the OfS framework; a key reference point in Wales and Scotland; part of the quality arrangements in Northern Ireland (D1, front matter: Relationship to legislation)"
licence: "QAA copyright; the document gives no re-use terms in its text (D1, front matter)"
copyrightNotice: { text: "© The Quality Assurance Agency for Higher Education 2024", locator: "D1, index" }
```

### S2 Purpose and scope
<!-- label: source; status: drafted; basis: primary -->
```yaml
governs: "what a graduate in dance, drama and performance is expected to know, do and understand at honours, at threshold, typical and excellent, and the added outcomes for master's study"
appliesTo:
  awards: ["bachelor's with honours", "master's (taught postgraduate and integrated master's)"]
  levels: ["fheq:6", "fqheis:10", "fheq:7", "fqheis:11"]
  providers: ["UK higher education providers"]
whoMustUse: "none-stated; it is a reference point, not a requirement (D1, front matter)"
howUsed: ["design", "approval", "review", "other: external examining; PSRBs; information for prospective students and employers"]
doesNot: "it is not a national curriculum and does not prescribe teaching, learning or assessment; it carries no statutory or regulatory requirement (D1, front matter)"
beneficiary: the student
statedScope: "\"Within the scope of this Subject Benchmark Statement are undergraduate and taught postgraduate degree programmes delivered by a broad range of providers, each with their own ethos and pedagogic emphases, as well as varying approaches to student journeys.\" (D1, 1.2)"
statedSubjects:
  - { name: "Dance, Drama and Performance", locator: "(D1, title; 1.1; 1.5)", kind: "subject", codes: [{ scheme: "hecos", code: "100068", label: "dance" }, { scheme: "hecos", code: "100069", label: "drama" }, { scheme: "hecos", code: "100071", label: "performing arts" }, { scheme: "cah", code: "CAH25-02", label: "performing arts" }] }
  - { name: "acting", locator: "(D1, 2.2; 2.3.b1)", kind: "specialism", codes: [{ scheme: "hecos", code: "100067", label: "acting" }] }
  - { name: "musical theatre", locator: "(D1, 2.2; 2.3.b1)", kind: "specialism", codes: [{ scheme: "hecos", code: "100035", label: "musical theatre" }] }
  - { name: "theatre", locator: "(D1, 2.2.b2; 2.3.b1)", kind: "specialism", codes: [{ scheme: "hecos", code: "100698", label: "theatre studies" }] }
  - { name: "scenography and theatre design", locator: "(D1, 2.2; 2.3.b1)", kind: "specialism", codes: [{ scheme: "hecos", code: "100708", label: "stage design" }] }
  - { name: "applied and social theatre", locator: "(D1, 2.2)", kind: "specialism", codes: [{ scheme: "hecos", code: "100710", label: "community theatre" }] }
  - { name: "dance theatre; writing for performance", locator: "(D1, 2.2)", kind: "specialism", codes: [] }
  - { name: "contemporary arts (interdisciplinary courses with no subject named in the award)", locator: "(D1, 2.2.b5)", kind: "programme title", codes: [] }
subjects: see front matter (subjectScope subjects)
```

### S3 Structure
<!-- label: both; status: drafted; basis: primary -->
```yaml
components:
  - { number: "1.1", order: 3, componentType: paragraph, parent: "section 1", heading: "Context", gloss: "a broad field joining practice and theory, old and new methods" }
  - { number: "1.2", order: 4, componentType: paragraph, parent: "section 1", heading: "Context", gloss: "scope: undergraduate and taught postgraduate courses" }
  - { number: "1.3", order: 5, componentType: paragraph, parent: "section 1", heading: "Context", gloss: "diverse provision; the four cross-cutting themes named" }
  - { number: "1.4", order: 6, componentType: paragraph, parent: "section 1", heading: "Context", gloss: "practice and concept in performance, contested and alive" }
  - { number: "1.5", order: 7, componentType: paragraph, parent: "section 1", heading: "Context", gloss: "single, combined and interdisciplinary courses; vocational and hybrid growth" }
  - { number: "1.6", order: 8, componentType: paragraph, parent: "section 1", heading: "Context", gloss: "industry-facing, critical, research-led and socially engaged courses" }
  - { number: "1.7", order: 9, componentType: paragraph, parent: "section 1", heading: "Purposes", gloss: "creativity and its communication at the centre" }
  - { number: "1.8", order: 10, componentType: paragraph, parent: "section 1", heading: "Purposes", gloss: "theory and practice across creative, vocational and professional dimensions" }
  - { number: "1.9", order: 11, componentType: paragraph, parent: "section 1", heading: "Purposes", gloss: "embodied learning and knowing" }
  - { number: "1.10", order: 12, componentType: paragraph, parent: "section 1", heading: "Purposes", gloss: "creative industries, cultural change and alternative worlds" }
  - { number: "1.11", order: 13, componentType: area, parent: "section 1", heading: "Characteristics", gloss: "six broad strands of study, from practice to employment" }
  - { number: "1.12", order: 14, componentType: paragraph, parent: "section 1", heading: "Characteristics", gloss: "learning through collaboration and ensemble" }
  - { number: "1.13", order: 15, componentType: paragraph, parent: "section 1", heading: "Characteristics", gloss: "inclusive learning communities; safety balanced with creative risk" }
  - { number: "1.14", order: 16, componentType: paragraph, parent: "section 1", heading: "Characteristics", gloss: "many perspectives, cultures and histories; authorship questions" }
  - { number: "1.15", order: 17, componentType: paragraph, parent: "section 1", heading: "Characteristics", gloss: "generative AI analysed and used openly as a creative tool" }
  - { number: "1.16", order: 18, componentType: paragraph, parent: "section 1", heading: "Characteristics", gloss: "the four themes run through the whole statement" }
  - { number: "1.17", order: 19, componentType: paragraph, parent: "section 1", heading: "Equality, diversity and inclusion", gloss: "EDI commitment; no structural disadvantage; Equality Act 2010" }
  - { number: "1.18", order: 20, componentType: stem, parent: "section 1", heading: "Equality, diversity and inclusion", gloss: "guiding principles for studios and classrooms" }
  - { number: "1.19", order: 21, componentType: paragraph, parent: "section 1", heading: "Equality, diversity and inclusion", gloss: "performance as diverse; centring marginalised voices" }
  - { number: "1.20", order: 22, componentType: stem, parent: "section 1", heading: "Equality, diversity and inclusion", gloss: "what inclusive learning opportunities do" }
  - { number: "1.21", order: 23, componentType: paragraph, parent: "section 1", heading: "Accessibility", gloss: "inclusive design across every learning setting" }
  - { number: "1.22", order: 24, componentType: paragraph, parent: "section 1", heading: "Accessibility", gloss: "questioning ableist knowledge; anticipating access needs" }
  - { number: "1.23", order: 25, componentType: paragraph, parent: "section 1", heading: "Accessibility", gloss: "live learning first, blended learning valued" }
  - { number: "1.24", order: 26, componentType: paragraph, parent: "section 1", heading: "Accessibility", gloss: "teaching methods that answer to student needs and access" }
  - { number: "1.25", order: 27, componentType: paragraph, parent: "section 1", heading: "Accessibility", gloss: "programmes that remove barriers to learning" }
  - { number: "1.26", order: 28, componentType: paragraph, parent: "section 1", heading: "Accessibility", gloss: "flexible outcomes and scaffolded curricula" }
  - { number: "1.27", order: 29, componentType: paragraph, parent: "section 1", heading: "Accessibility", gloss: "dignity, respect and seeing oneself in the curriculum" }
  - { number: "1.28", order: 30, componentType: paragraph, parent: "section 1", heading: "Accessibility", gloss: "fieldwork with attention to individual needs" }
  - { number: "1.29", order: 31, componentType: paragraph, parent: "section 1", heading: "Accessibility", gloss: "barriers in group and practical work planned for" }
  - { number: "1.30", order: 32, componentType: paragraph, parent: "section 1", heading: "Accessibility", gloss: "belonging, support and students as partners" }
  - { number: "1.31", order: 33, componentType: paragraph, parent: "section 1", heading: "Sustainability", gloss: "ESD defined; SDGs, the 2021 guidance and the Theatre Green Book" }
  - { number: "1.32", order: 34, componentType: paragraph, parent: "section 1", heading: "Sustainability", gloss: "the art forms well placed for a sustainable future" }
  - { number: "1.33", order: 35, componentType: stem, parent: "section 1", heading: "Sustainability", gloss: "economic, social and environmental themes for curricula" }
  - { number: "1.34", order: 36, componentType: paragraph, parent: "section 1", heading: "Sustainability", gloss: "technology and fair digital access" }
  - { number: "1.35", order: 37, componentType: paragraph, parent: "section 1", heading: "Enterprise and entrepreneurship education", gloss: "enterprise education for employability and value to society" }
  - { number: "1.36", order: 38, componentType: paragraph, parent: "section 1", heading: "Enterprise and entrepreneurship education", gloss: "social, political and cultural value of the field" }
  - { number: "1.37", order: 39, componentType: paragraph, parent: "section 1", heading: "Enterprise and entrepreneurship education", gloss: "critical thinking communicated in many forms" }
  - { number: "1.38", order: 40, componentType: paragraph, parent: "section 1", heading: "Enterprise and entrepreneurship education", gloss: "training for roles and portfolio careers" }
  - { number: "2.1", order: 42, componentType: paragraph, parent: "section 2", heading: "Design", gloss: "integrative, progressive, co-created course design" }
  - { number: "2.2", order: 43, componentType: stem, parent: "section 2", heading: "Design", gloss: "associated areas and kinds of course at FHEQ 6 and 7" }
  - { number: "2.3", order: 44, componentType: area, parent: "section 2", heading: "Design", gloss: "what degrees in the field study" }
  - { number: "2.4", order: 45, componentType: paragraph, parent: "section 2", heading: "Design", gloss: "knowledge made through performance-making" }
  - { number: "2.5", order: 46, componentType: paragraph, parent: "section 2", heading: "Design", gloss: "definition must not block innovation or tradition" }
  - { number: "2.6", order: 47, componentType: paragraph, parent: "section 2", heading: "Design", gloss: "courses engage with national and international performing arts" }
  - { number: "2.7", order: 48, componentType: paragraph, parent: "section 2", heading: "Design", gloss: "critical discourse, synthesis and practical skill" }
  - { number: "2.8", order: 49, componentType: paragraph, parent: "section 2", heading: "Progression", gloss: "progression by level towards the threshold" }
  - { number: "2.9", order: 50, componentType: paragraph, parent: "section 2", heading: "Progression", gloss: "readiness for postgraduate study" }
  - { number: "2.10", order: 51, componentType: paragraph, parent: "section 2", heading: "Progression", gloss: "joint and combined students reach the core skills" }
  - { number: "2.11", order: 52, componentType: paragraph, parent: "section 2", heading: "Progression", gloss: "integrated master's at FHEQ 7 and FQHEIS 11" }
  - { number: "2.12", order: 53, componentType: paragraph, parent: "section 2", heading: "Progression", gloss: "exit awards and course lengths across the nations" }
  - { number: "2.13", order: 54, componentType: paragraph, parent: "section 2", heading: "Flexibility", gloss: "flexible modes, credit and micro-credentials" }
  - { number: "2.14", order: 55, componentType: paragraph, parent: "section 2", heading: "Partnerships", gloss: "partnerships for progression and employability" }
  - { number: "2.15", order: 56, componentType: paragraph, parent: "section 2", heading: "Partnerships", gloss: "kinds of partnership activity" }
  - { number: "2.16", order: 57, componentType: paragraph, parent: "section 2", heading: "Partnerships", gloss: "formal and informal partnerships" }
  - { number: "2.17", order: 58, componentType: paragraph, parent: "section 2", heading: "Partnerships", gloss: "equal access to partnership activity; work-based learning guidance" }
  - { number: "2.18", order: 59, componentType: paragraph, parent: "section 2", heading: "Partnerships", gloss: "partners support professional development" }
  - { number: "2.19", order: 60, componentType: paragraph, parent: "section 2", heading: "Partnerships", gloss: "partners share the community's equity principles" }
  - { number: "2.20", order: 61, componentType: paragraph, parent: "section 2", heading: "Partnerships", gloss: "transferable skills developed with partners" }
  - { number: "2.21", order: 62, componentType: paragraph, parent: "section 2", heading: "Partnerships", gloss: "partners comment on curriculum and skills" }
  - { number: "2.22", order: 63, componentType: paragraph, parent: "section 2", heading: "Monitoring and review", gloss: "routine monitoring and periodic review with the student voice" }
  - { number: "2.23", order: 64, componentType: paragraph, parent: "section 2", heading: "Monitoring and review", gloss: "external reviewers in periodic review" }
  - { number: "2.24", order: 65, componentType: paragraph, parent: "section 2", heading: "Monitoring and review", gloss: "external examiners and their yearly reports" }
  - { number: "2.25", order: 66, componentType: paragraph, parent: "section 2", heading: "Monitoring and review", gloss: "professional accreditation for vocational courses" }
  - { number: "2.26", order: 67, componentType: paragraph, parent: "section 2", heading: "Monitoring and review", gloss: "regular curriculum review" }
  - { number: "3.1", order: 69, componentType: paragraph, parent: "section 3", heading: "Content", gloss: "no prescriptive model; courses pick and emphasise areas" }
  - { number: "3.2", order: 70, componentType: area, parent: "section 3", heading: "Content", gloss: "areas of knowledge and understanding" }
  - { number: "3.3", order: 71, componentType: stem, parent: "section 3", heading: "Content", gloss: "thirteen skills students develop" }
  - { number: "3.4", order: 72, componentType: paragraph, parent: "section 3", heading: "Content", gloss: "same outcomes for all Performance module students" }
  - { number: "3.5", order: 73, componentType: paragraph, parent: "section 3", heading: "Content", gloss: "progression and depth for specialists and others; capstone" }
  - { number: "3.6", order: 74, componentType: paragraph, parent: "section 3", heading: "Content", gloss: "diversity, inclusion, access and reasonable adjustments" }
  - { number: "3.7", order: 75, componentType: practice, parent: "section 3", heading: "Teaching and learning", gloss: "varied approaches joining practice and theory" }
  - { number: "3.8", order: 76, componentType: practice, parent: "section 3", heading: "Teaching and learning", gloss: "experiential and embodied learning as the basis" }
  - { number: "3.9", order: 77, componentType: paragraph, parent: "section 3", heading: "Teaching and learning", gloss: "teaching drawn from the disciplines' own practice" }
  - { number: "3.10", order: 78, componentType: practice, parent: "section 3", heading: "Teaching and learning", gloss: "learning in practical and professional contexts, many roles" }
  - { number: "3.11", order: 79, componentType: practice, parent: "section 3", heading: "Teaching and learning", gloss: "tutor-led to independent learning; group work" }
  - { number: "3.12", order: 80, componentType: practice, parent: "section 3", heading: "Teaching and learning", gloss: "settings and modes of learning" }
  - { number: "3.13", order: 81, componentType: practice, parent: "section 3", heading: "Assessment", gloss: "inclusive, negotiated assessment as part of learning" }
  - { number: "3.14", order: 82, componentType: practice, parent: "section 3", heading: "Assessment", gloss: "formats of formative and summative assessment" }
  - { number: "3.15", order: 83, componentType: practice, parent: "section 3", heading: "Assessment", gloss: "self and peer assessment; course information" }
  - { number: "3.16", order: 84, componentType: paragraph, parent: "section 3", heading: "Assessment", gloss: "more course information to include" }
  - { number: "3.17", order: 85, componentType: practice, parent: "section 3", heading: "Assessment", gloss: "handbooks on academic issues and support" }
  - { number: "4.1", order: 87, componentType: paragraph, parent: "section 4", heading: "Introduction", gloss: "'Performance' used for the whole field" }
  - { number: "4.2", order: 88, componentType: paragraph, parent: "section 4", heading: "Introduction", gloss: "three rungs shown at the award of honours" }
  - { number: "4.3", order: 89, componentType: paragraph, parent: "section 4", heading: "Introduction", gloss: "most exceed the threshold; Annex D for classes" }
  - { number: "4.4", order: 90, componentType: paragraph, parent: "section 4", heading: "Introduction", gloss: "standards as learning outcomes" }
  - { number: "4.5", order: 91, componentType: paragraph, parent: "section 4", heading: "Introduction", gloss: "the typical goal: creative and critical artists and thinkers" }
  - { number: "4.6", order: 92, componentType: paragraph, parent: "section 4", heading: "Introduction", gloss: "what the threshold and excellent rungs mean" }
  - { number: "4.7", order: 93, componentType: paragraph, parent: "section 4", heading: "Introduction", gloss: "indicative outcomes for single honours; themes in all courses" }
  - { number: "4.8", order: 94, componentType: stem, parent: "section 4", heading: "Threshold level", gloss: "threshold: subject knowledge and understanding" }
  - { number: "4.9", order: 95, componentType: stem, parent: "section 4", heading: "Threshold level", gloss: "threshold: subject-specific skills" }
  - { number: "4.10", order: 96, componentType: stem, parent: "section 4", heading: "Threshold level", gloss: "threshold: generic and graduate skills" }
  - { number: "4.11", order: 97, componentType: stem, parent: "section 4", heading: "Typical level", gloss: "typical: subject knowledge, understanding and skills" }
  - { number: "4.12", order: 98, componentType: stem, parent: "section 4", heading: "Typical level", gloss: "typical: subject-specific skills" }
  - { number: "4.13", order: 99, componentType: stem, parent: "section 4", heading: "Typical level", gloss: "typical: generic and graduate skills" }
  - { number: "4.14", order: 100, componentType: stem, parent: "section 4", heading: "Excellent level", gloss: "excellent: subject knowledge, understanding and skills" }
  - { number: "4.15", order: 101, componentType: stem, parent: "section 4", heading: "Excellent level", gloss: "excellent: subject-specific skills" }
  - { number: "4.16", order: 102, componentType: stem, parent: "section 4", heading: "Excellent level", gloss: "excellent: generic and graduate skills" }
  - { number: "4.17", order: 103, componentType: stem, parent: "section 4", heading: "Master's level degrees in Dance, Drama and Performance", gloss: "master's: five added outcomes" }
  - { number: "1", componentType: section, parent: none, heading: "Context and purposes of a Dance, Drama and Performance degree", gloss: "section 1" }
  - { number: "2", componentType: section, parent: none, heading: "Distinctive features of the Dance, Drama and Performance degree", gloss: "section 2" }
  - { number: "3", componentType: section, parent: none, heading: "Content, structure and delivery", gloss: "section 3" }
  - { number: "4", componentType: section, parent: none, heading: "Benchmark standards", gloss: "section 4" }
excluded:
  - { number: "none", heading: "About this Statement; How can I use this document?; Relationship to legislation; Additional sector reference points", kind: "other: front matter, read for S1, S2 and SB6" }
  - { number: "none", heading: "section headings (1 to 4)", kind: "other: heading lines" }
  - { number: "5", heading: "List of references and further resources", kind: "other: references, read for S7 and SB6" }
  - { number: "6", heading: "Membership of the Advisory Group", kind: "other: membership, read for S7 (earlier editions 2019, 2015, 2007, 2002)" }
```

### S4 Statements
<!-- label: both; status: drafted; basis: primary. Only standards (D-std-0002 (a)): 118 records. `source` is the issuer's statement exactly as its span holds it (D-std-0014). -->
```yaml
- id: qaa/dance-drama-and-performance-2024/1.17
  locator: { number: "1.17", headingPath: ["Context and purposes of a Dance, Drama and Performance degree", "Equality, diversity and inclusion"] }
  span: { start: 17935, end: 18023 }
  source: "No student should be structurally disadvantaged due to their individual characteristics."
  stem: none
  statementType: expectation
  rung: none
  force: should
  level: none
  appliesTo: "students of the subject"
  addressee: both
  verbs: ["disadvantaged"]
  about: "no structural disadvantage from personal characteristics"
  themes: [theme:edi]
  domain: none
  award: ["bachelor's with honours", "master's"]
  gradeOf: none
  paraphrase: "No student in the subject should be put at a built-in disadvantage because of their personal characteristics."
  quote: full   # the issuer's statement is in `source` (D-std-0014)
  audience: both
  subjects: inherited
- id: qaa/dance-drama-and-performance-2024/1.24
  locator: { number: "1.24", headingPath: ["Context and purposes of a Dance, Drama and Performance degree", "Accessibility"] }
  span: { start: 21366, end: 21701 }
  source: "1.24 Pedagogic methods for teaching Dance, Drama and Performance will generally reflect the needs of the student body and professional practices relevant to the disciplines, through an inclusive curriculum that prioritises accessibility and equity. The availability of appropriate learning and teaching resources and materials is key.\n"
  stem: none
  statementType: expectation
  rung: none
  force: will
  level: none
  appliesTo: "teaching in the subject"
  addressee: provider
  verbs: ["reflect"]
  about: "teaching methods that answer to student needs, access and equity"
  themes: [theme:accessibility]
  domain: none
  award: ["bachelor's with honours", "master's"]
  gradeOf: none
  paraphrase: "Teaching methods in the subject will generally answer to the needs of the student body and the professional practices of the disciplines, through an inclusive curriculum that puts access and equity first; suitable resources are key."
  quote: full   # the issuer's statement is in `source` (D-std-0014)
  audience: practitioner
  subjects: inherited
- id: qaa/dance-drama-and-performance-2024/2.6
  locator: { number: "2.6", headingPath: ["Distinctive features of the Dance, Drama and Performance degree", "Design"] }
  span: { start: 34209, end: 34367 }
  source: "2.6 Courses will engage with, reflect and be informed by national and international performing arts contexts, developments, industries, people and practices.\n"
  stem: none
  statementType: expectation
  rung: none
  force: will
  level: none
  appliesTo: "courses in the subject"
  addressee: provider
  verbs: ["engage", "reflect", "informed"]
  about: "engaging with national and international performing arts"
  themes: [none]
  domain: none
  award: ["bachelor's with honours", "master's"]
  gradeOf: none
  paraphrase: "Courses will draw on, mirror and learn from performing arts contexts, industries, people and practices at home and abroad."
  quote: full   # the issuer's statement is in `source` (D-std-0014)
  audience: both
  subjects: inherited
- id: qaa/dance-drama-and-performance-2024/2.8
  locator: { number: "2.8", headingPath: ["Distinctive features of the Dance, Drama and Performance degree", "Progression"] }
  span: { start: 34791, end: 35343 }
  source: "2.8 A Dance, Drama and Performance student will progress from one level of study to the next, in line with the regulations, processes and exit qualifications for each institution. However, it is expected that each level will be accompanied by the attainment of knowledge, expertise and experience that builds towards the final achievement of meeting the threshold- level subject-specific and generic skills listed in this Statement. This will usually include successful completion and the award of credit for the full range of learning and assessment.\n"
  stem: none
  statementType: expectation
  rung: none
  force: will
  level: fheq:6
  appliesTo: "students progressing through the degree"
  addressee: both
  verbs: ["progress", "accompanied", "include"]
  about: "each level builds towards the threshold"
  themes: [none]
  domain: none
  award: ["bachelor's with honours"]
  gradeOf: none
  paraphrase: "Students will move up through the levels under each institution's regulations; each level is expected to bring knowledge, expertise and experience that build towards the threshold subject and generic skills, usually with credit for all learning and assessment."
  quote: full   # the issuer's statement is in `source` (D-std-0014)
  audience: both
  subjects: inherited
- id: qaa/dance-drama-and-performance-2024/2.9
  locator: { number: "2.9", headingPath: ["Distinctive features of the Dance, Drama and Performance degree", "Progression"] }
  span: { start: 35343, end: 35764 }
  source: "2.9 Upon graduation from an undergraduate degree, it is expected that a student who had achieved a second-class degree or higher will be capable of, and equipped for, undertaking postgraduate study in Dance, Drama and Performance or a related discipline. Entry requirements to postgraduate courses are, however, determined by individual providers which may require specified levels of achievement at undergraduate level.\n"
  stem: none
  statementType: expectation
  rung: none
  force: will
  level: fheq:6
  appliesTo: "graduates with a second-class degree or higher"
  addressee: learner
  verbs: ["undertaking"]
  about: "readiness for postgraduate study"
  themes: [none]
  domain: none
  award: ["bachelor's with honours"]
  gradeOf: none
  paraphrase: "On completing an undergraduate degree with at least a second-class result, a student is expected to be able and ready to take on postgraduate study in the subject or a related one; entry rules stay with each institution."
  quote: full   # the issuer's statement is in `source` (D-std-0014)
  audience: both
  subjects: inherited
- id: qaa/dance-drama-and-performance-2024/2.10
  locator: { number: "2.10", headingPath: ["Distinctive features of the Dance, Drama and Performance degree", "Progression"] }
  span: { start: 35764, end: 36196 }
  source: "2.10 Undergraduates studying Dance, Drama and Performance as part of a combined or joint degree with other subjects will achieve core elements of the specific and generic skills outlined in this Statement and will add others according to the topics covered in the other subject(s) of their degree. Additionally, they may explore the overlap between different disciplines, creating further opportunities for interdisciplinary study.\n"
  stem: none
  statementType: expectation
  rung: none
  force: will
  level: fheq:6
  appliesTo: "joint and combined honours students"
  addressee: learner
  verbs: ["achieve", "add", "explore"]
  about: "core skills for joint and combined students"
  themes: [none]
  domain: none
  award: ["bachelor's with honours"]
  gradeOf: none
  paraphrase: "Undergraduates taking the subject within a joint or combined degree will gain the core of its subject and generic skills and add further skills from their other subject, with scope to work across the disciplines."
  quote: full   # the issuer's statement is in `source` (D-std-0014)
  audience: both
  subjects: inherited
- id: qaa/dance-drama-and-performance-2024/2.23
  locator: { number: "2.23", headingPath: ["Distinctive features of the Dance, Drama and Performance degree", "Monitoring and review"] }
  span: { start: 41100, end: 41395 }
  source: "2.23 Externality is an essential component of the quality assurance system in the UK. Providers will use external reviewers as part of periodic review to gain an external perspective on any proposed changes and ensure threshold standards are achieved and content is appropriate for the subject.\n"
  stem: none
  statementType: expectation
  rung: none
  force: will
  level: none
  appliesTo: "institutions in periodic review"
  addressee: provider
  verbs: ["use", "gain", "ensure", "achieved"]
  about: "external reviewers in periodic review"
  themes: [none]
  domain: none
  award: ["bachelor's with honours", "master's"]
  gradeOf: none
  paraphrase: "Externality is essential to UK quality assurance: institutions will bring in external reviewers in periodic review for an outside view of proposed changes and to make sure threshold standards are met and content suits the subject."
  quote: full   # the issuer's statement is in `source` (D-std-0014)
  audience: practitioner
  subjects: inherited
- id: qaa/dance-drama-and-performance-2024/2.24
  locator: { number: "2.24", headingPath: ["Distinctive features of the Dance, Drama and Performance degree", "Monitoring and review"] }
  span: { start: 41884, end: 42030 }
  source: "External examiners are required to produce a report each year and make recommendations for changes to modules and assessments (where appropriate)."
  stem: none
  statementType: requirement
  rung: none
  force: must
  level: none
  appliesTo: "external examiners"
  addressee: provider
  verbs: ["produce", "make"]
  about: "the external examiner's yearly report"
  themes: [none]
  domain: none
  award: ["bachelor's with honours", "master's"]
  gradeOf: none
  paraphrase: "Each year, external examiners must write a report and, where fitting, recommend changes to modules and assessment."
  quote: full   # the issuer's statement is in `source` (D-std-0014)
  audience: practitioner
  subjects: inherited
- id: qaa/dance-drama-and-performance-2024/3.1
  locator: { number: "3.1", headingPath: ["Content, structure and delivery", "Content"] }
  span: { start: 43344, end: 43472 }
  source: "Typically, courses will incorporate several areas listed in paragraphs 3.2 and 3.3, focusing on some as distinguishing features."
  stem: none
  statementType: expectation
  rung: none
  force: will
  level: none
  appliesTo: "courses in the subject"
  addressee: provider
  verbs: ["incorporate", "focusing"]
  about: "courses select and emphasise areas"
  themes: [none]
  domain: none
  award: ["bachelor's with honours"]
  gradeOf: none
  paraphrase: "Courses usually take up several of the areas and skills set out in 3.2 and 3.3, making some of them the course's distinctive emphasis."
  quote: full   # the issuer's statement is in `source` (D-std-0014)
  audience: practitioner
  subjects: inherited
- id: qaa/dance-drama-and-performance-2024/3.3.b1
  locator: { number: "3.3.b1", headingPath: ["Content, structure and delivery", "Content"] }
  span: { start: 44658, end: 44853 }
  source: "engage in performance and production, based on the acquisition and understanding of appropriate performance and production vocabularies, skills, structures, working methods and research paradigms"
  stem: "3.3"
  statementType: outcome
  rung: none
  force: will
  level: fheq:6
  appliesTo: "students of Performance"
  addressee: learner
  verbs: ["engage"]
  about: "performing and producing with the field's vocabularies and methods"
  themes: [none]
  domain: subject-skill
  award: ["bachelor's with honours"]
  gradeOf: none
  paraphrase: "Will take part in performance and production, grounded in learning and understanding suitable vocabularies, skills, structures, working methods and research approaches."
  quote: full   # the issuer's statement is in `source` (D-std-0014)
  audience: both
  subjects: inherited
- id: qaa/dance-drama-and-performance-2024/3.3.b2
  locator: { number: "3.3.b2", headingPath: ["Content, structure and delivery", "Content"] }
  span: { start: 44856, end: 44969 }
  source: "develop techniques informed by or derived from particular cultural forms/histories/ contexts and/or practitioners"
  stem: "3.3"
  statementType: outcome
  rung: none
  force: will
  level: fheq:6
  appliesTo: "students of Performance"
  addressee: learner
  verbs: ["develop"]
  about: "techniques from cultural forms or practitioners"
  themes: [none]
  domain: subject-skill
  award: ["bachelor's with honours"]
  gradeOf: none
  paraphrase: "Will develop techniques drawn from or shaped by particular cultural forms, histories, contexts or practitioners."
  quote: full   # the issuer's statement is in `source` (D-std-0014)
  audience: both
  subjects: inherited
- id: qaa/dance-drama-and-performance-2024/3.3.b3
  locator: { number: "3.3.b3", headingPath: ["Content, structure and delivery", "Content"] }
  span: { start: 44972, end: 45091 }
  source: "take responsibility for project management and creative decision-making, whether working independently or within groups"
  stem: "3.3"
  statementType: outcome
  rung: none
  force: will
  level: fheq:6
  appliesTo: "students of Performance"
  addressee: learner
  verbs: ["take"]
  about: "project management and creative decision-making"
  themes: [none]
  domain: generic-skill
  award: ["bachelor's with honours"]
  gradeOf: none
  paraphrase: "Will take responsibility for managing projects and making creative decisions, alone or in groups."
  quote: full   # the issuer's statement is in `source` (D-std-0014)
  audience: both
  subjects: inherited
- id: qaa/dance-drama-and-performance-2024/3.3.b4
  locator: { number: "3.3.b4", headingPath: ["Content, structure and delivery", "Content"] }
  span: { start: 45094, end: 45243 }
  source: "describe, theorise, interpret and evaluate Performance texts and events from a range of perspectives, using appropriate subject-specific vocabularies"
  stem: "3.3"
  statementType: outcome
  rung: none
  force: will
  level: fheq:6
  appliesTo: "students of Performance"
  addressee: learner
  verbs: ["describe", "theorise", "interpret", "evaluate"]
  about: "analysing performance texts and events"
  themes: [none]
  domain: subject-skill
  award: ["bachelor's with honours"]
  gradeOf: none
  paraphrase: "Will describe, theorise, interpret and evaluate texts and events in performance from several perspectives, using the subject's vocabularies."
  quote: full   # the issuer's statement is in `source` (D-std-0014)
  audience: both
  subjects: inherited
- id: qaa/dance-drama-and-performance-2024/3.3.b5
  locator: { number: "3.3.b5", headingPath: ["Content, structure and delivery", "Content"] }
  span: { start: 45246, end: 45285 }
  source: "access and analyse historical materials"
  stem: "3.3"
  statementType: outcome
  rung: none
  force: will
  level: fheq:6
  appliesTo: "students of Performance"
  addressee: learner
  verbs: ["access", "analyse"]
  about: "historical materials"
  themes: [none]
  domain: subject-skill
  award: ["bachelor's with honours"]
  gradeOf: none
  paraphrase: "Will find and analyse historical materials."
  quote: full   # the issuer's statement is in `source` (D-std-0014)
  audience: both
  subjects: inherited
- id: qaa/dance-drama-and-performance-2024/3.3.b6
  locator: { number: "3.3.b6", headingPath: ["Content, structure and delivery", "Content"] }
  span: { start: 45288, end: 45388 }
  source: "analyse the role of Performance in social, cultural and political discourse, in the past and present"
  stem: "3.3"
  statementType: outcome
  rung: none
  force: will
  level: fheq:6
  appliesTo: "students of Performance"
  addressee: learner
  verbs: ["analyse"]
  about: "performance's role in social, cultural and political discourse"
  themes: [none]
  domain: understanding
  award: ["bachelor's with honours"]
  gradeOf: none
  paraphrase: "Will analyse what performance does in social, cultural and political debate, past and present."
  quote: full   # the issuer's statement is in `source` (D-std-0014)
  audience: both
  subjects: inherited
- id: qaa/dance-drama-and-performance-2024/3.3.b7
  locator: { number: "3.3.b7", headingPath: ["Content, structure and delivery", "Content"] }
  span: { start: 45395, end: 45535 }
  source: "plan, facilitate, deliver and evaluate projects that apply participatory Performance expertise in social, educational and community settings"
  stem: "3.3"
  statementType: outcome
  rung: none
  force: will
  level: fheq:6
  appliesTo: "students of Performance"
  addressee: learner
  verbs: ["plan", "facilitate", "deliver", "evaluate"]
  about: "participatory projects in social, educational and community settings"
  themes: [none]
  domain: subject-skill
  award: ["bachelor's with honours"]
  gradeOf: none
  paraphrase: "Will plan, lead, deliver and evaluate projects that use participatory performance skill in social, educational and community settings."
  quote: full   # the issuer's statement is in `source` (D-std-0014)
  audience: both
  subjects: inherited
- id: qaa/dance-drama-and-performance-2024/3.3.b8
  locator: { number: "3.3.b8", headingPath: ["Content, structure and delivery", "Content"] }
  span: { start: 45538, end: 45585 }
  source: "address the ethical implications of Performance"
  stem: "3.3"
  statementType: outcome
  rung: none
  force: will
  level: fheq:6
  appliesTo: "students of Performance"
  addressee: learner
  verbs: ["address"]
  about: "ethical implications of performance"
  themes: [none]
  domain: understanding
  award: ["bachelor's with honours"]
  gradeOf: none
  paraphrase: "Will deal with the ethical questions performance raises."
  quote: full   # the issuer's statement is in `source` (D-std-0014)
  audience: both
  subjects: inherited
- id: qaa/dance-drama-and-performance-2024/3.3.b9
  locator: { number: "3.3.b9", headingPath: ["Content, structure and delivery", "Content"] }
  span: { start: 45588, end: 45690 }
  source: "research and evaluate information, arrive at independent judgements, and articulate reasoned arguments"
  stem: "3.3"
  statementType: outcome
  rung: none
  force: will
  level: fheq:6
  appliesTo: "students of Performance"
  addressee: learner
  verbs: ["research", "evaluate", "arrive", "articulate"]
  about: "research, independent judgement and reasoned argument"
  themes: [none]
  domain: generic-skill
  award: ["bachelor's with honours"]
  gradeOf: none
  paraphrase: "Will research and evaluate information, reach their own judgements and make reasoned arguments."
  quote: full   # the issuer's statement is in `source` (D-std-0014)
  audience: both
  subjects: inherited
- id: qaa/dance-drama-and-performance-2024/3.3.b10
  locator: { number: "3.3.b10", headingPath: ["Content, structure and delivery", "Content"] }
  span: { start: 45693, end: 45804 }
  source: "operate collaboratively in intellectual, creative and professional contexts to generate and pursue shared goals"
  stem: "3.3"
  statementType: outcome
  rung: none
  force: will
  level: fheq:6
  appliesTo: "students of Performance"
  addressee: learner
  verbs: ["operate", "generate", "pursue"]
  about: "collaboration towards shared goals"
  themes: [none]
  domain: generic-skill
  award: ["bachelor's with honours"]
  gradeOf: none
  paraphrase: "Will work with others in intellectual, creative and professional settings to set and pursue shared goals."
  quote: full   # the issuer's statement is in `source` (D-std-0014)
  audience: both
  subjects: inherited
- id: qaa/dance-drama-and-performance-2024/3.3.b11
  locator: { number: "3.3.b11", headingPath: ["Content, structure and delivery", "Content"] }
  span: { start: 45807, end: 45897 }
  source: "consider, acknowledge and respect diverse opinions, experiences and performance traditions"
  stem: "3.3"
  statementType: outcome
  rung: none
  force: will
  level: fheq:6
  appliesTo: "students of Performance"
  addressee: learner
  verbs: ["consider", "acknowledge", "respect"]
  about: "respect for diverse views and traditions"
  themes: [none]
  domain: generic-skill
  award: ["bachelor's with honours"]
  gradeOf: none
  paraphrase: "Will consider, recognise and respect different opinions, experiences and performance traditions."
  quote: full   # the issuer's statement is in `source` (D-std-0014)
  audience: both
  subjects: inherited
- id: qaa/dance-drama-and-performance-2024/3.3.b12
  locator: { number: "3.3.b12", headingPath: ["Content, structure and delivery", "Content"] }
  span: { start: 45900, end: 45992 }
  source: "produce written work within appropriate scholarly and professional registers and conventions"
  stem: "3.3"
  statementType: outcome
  rung: none
  force: will
  level: fheq:6
  appliesTo: "students of Performance"
  addressee: learner
  verbs: ["produce"]
  about: "scholarly and professional writing"
  themes: [none]
  domain: generic-skill
  award: ["bachelor's with honours"]
  gradeOf: none
  paraphrase: "Will write in fitting scholarly and professional registers and conventions."
  quote: full   # the issuer's statement is in `source` (D-std-0014)
  audience: both
  subjects: inherited
- id: qaa/dance-drama-and-performance-2024/3.3.b13
  locator: { number: "3.3.b13", headingPath: ["Content, structure and delivery", "Content"] }
  span: { start: 45995, end: 46080 }
  source: "present information in a range of forms appropriate to content, audience and context."
  stem: "3.3"
  statementType: outcome
  rung: none
  force: will
  level: fheq:6
  appliesTo: "students of Performance"
  addressee: learner
  verbs: ["present"]
  about: "presenting information in suitable forms"
  themes: [none]
  domain: generic-skill
  award: ["bachelor's with honours"]
  gradeOf: none
  paraphrase: "Will present information in a range of forms suited to content, audience and context."
  quote: full   # the issuer's statement is in `source` (D-std-0014)
  audience: both
  subjects: inherited
- id: qaa/dance-drama-and-performance-2024/3.4
  locator: { number: "3.4", headingPath: ["Content, structure and delivery", "Content"] }
  span: { start: 46333, end: 46469 }
  source: "Whatever the focus of the course, the same learning outcomes are expected of those students undertaking Performance modules or pathways."
  stem: none
  statementType: expectation
  rung: none
  force: describes
  level: fheq:6
  appliesTo: "students taking Performance modules in any course"
  addressee: both
  verbs: ["expected", "undertaking"]
  about: "the same outcomes for all students on Performance modules"
  themes: [none]
  domain: none
  award: ["bachelor's with honours"]
  gradeOf: none
  paraphrase: "Whatever course they belong to, students on Performance modules or pathways are held to the same learning outcomes."
  quote: full   # the issuer's statement is in `source` (D-std-0014)
  audience: both
  subjects: inherited
- id: qaa/dance-drama-and-performance-2024/3.5
  locator: { number: "3.5", headingPath: ["Content, structure and delivery", "Content"] }
  span: { start: 46470, end: 47186 }
  source: "3.5 All students engaging in the study of Performance will develop subject-specific knowledge and/or skills and a commensurate degree of experience. The study of Performance within any programme of study will facilitate progression in terms of subject- specific expertise, personal and social development and intellectual maturity through engagement with appropriate ways of thinking and doing. Courses will often culminate in a final year capstone project. Some highly specialised modules may not be available to students for whom Performance is not their principal area of study; therefore, for such students the same level of progression in terms of in-depth knowledge and/or technical skill may not be expected.\n"
  stem: none
  statementType: expectation
  rung: none
  force: will
  level: fheq:6
  appliesTo: "all students of Performance"
  addressee: learner
  verbs: ["develop", "facilitate", "culminate"]
  about: "subject growth and progression for all Performance students; capstone"
  themes: [none]
  domain: none
  award: ["bachelor's with honours"]
  gradeOf: none
  paraphrase: "Everyone studying Performance will build subject knowledge or skills with matching experience, and that study will support progress in expertise, personal and social growth and intellectual maturity; courses often end in a capstone project, and non-specialists may not reach the same depth."
  quote: full   # the issuer's statement is in `source` (D-std-0014)
  audience: both
  subjects: inherited
- id: qaa/dance-drama-and-performance-2024/3.6
  locator: { number: "3.6", headingPath: ["Content, structure and delivery", "Content"] }
  span: { start: 47186, end: 47506 }
  source: "3.6 Teaching, learning and assessment will be underpinned by a commitment to diversity, inclusion and accessibility. Curriculum design, delivery and assessment activities will have the built-in flexibility to allow for reasonable adjustments to be made in recognition of individual learning needs. Teaching and learning\n"
  stem: none
  statementType: expectation
  rung: none
  force: will
  level: none
  appliesTo: "teaching, learning and assessment in the subject"
  addressee: both
  verbs: ["underpinned", "allow", "made"]
  about: "inclusion, access and reasonable adjustments built in"
  themes: [none]
  domain: none
  award: ["bachelor's with honours", "master's"]
  gradeOf: none
  paraphrase: "A commitment to diversity, inclusion and accessibility will underpin teaching, learning and assessment, and design, delivery and assessment will have flexibility built in so that reasonable adjustments can be made for individual needs."
  quote: full   # the issuer's statement is in `source` (D-std-0014)
  audience: both
  subjects: inherited
- id: qaa/dance-drama-and-performance-2024/3.9
  locator: { number: "3.9", headingPath: ["Content, structure and delivery", "Teaching and learning"] }
  span: { start: 47930, end: 48088 }
  source: "3.9 Learning and teaching activities will be informed by practices that are typical of, and relevant to, the diverse disciplines that constitute Performance.\n"
  stem: none
  statementType: expectation
  rung: none
  force: will
  level: none
  appliesTo: "teaching and learning in the subject"
  addressee: provider
  verbs: ["informed"]
  about: "teaching drawn from the disciplines' practice"
  themes: [none]
  domain: none
  award: ["bachelor's with honours", "master's"]
  gradeOf: none
  paraphrase: "Teaching and learning will rest on methods that suit and belong to the different disciplines within Performance."
  quote: full   # the issuer's statement is in `source` (D-std-0014)
  audience: practitioner
  subjects: inherited
- id: qaa/dance-drama-and-performance-2024/3.10
  locator: { number: "3.10", headingPath: ["Content, structure and delivery", "Teaching and learning"] }
  span: { start: 48088, end: 48447 }
  source: "3.10 Students will usually experience learning in, or related to, practical and professional Performance contexts. Students will undertake a variety of roles appropriate to their subject area and participate in a range of processes, including initial research, interpretative and creative practice, experimentation, rehearsal, production and performance.\n\n16\n"
  stem: none
  statementType: expectation
  rung: none
  force: will
  level: fheq:6
  appliesTo: "students of the subject"
  addressee: learner
  verbs: ["experience", "undertake", "participate"]
  about: "learning in practical and professional contexts, in varied roles"
  themes: [none]
  domain: none
  award: ["bachelor's with honours"]
  gradeOf: none
  paraphrase: "Students will usually learn in or alongside practical and professional Performance settings, taking on roles suited to their subject and joining processes from first research through creative work, rehearsal and production to performance."
  quote: full   # the issuer's statement is in `source` (D-std-0014)
  audience: both
  subjects: inherited
- id: qaa/dance-drama-and-performance-2024/3.11
  locator: { number: "3.11", headingPath: ["Content, structure and delivery", "Teaching and learning"] }
  span: { start: 48447, end: 48788 }
  source: "3.11 Students will typically experience both tutor-led and self-directed methods of learning. As they progress through different levels, their learning trajectory moves towards increased levels of independence and autonomy, encouraging positive attitudes towards lifelong learning. Group work is a typical feature of courses in Performance.\n"
  stem: none
  statementType: expectation
  rung: none
  force: will
  level: fheq:6
  appliesTo: "students of the subject"
  addressee: learner
  verbs: ["experience", "progress"]
  about: "tutor-led to independent learning; group work"
  themes: [none]
  domain: none
  award: ["bachelor's with honours"]
  gradeOf: none
  paraphrase: "Students will typically meet both tutor-led and self-directed learning, becoming more independent and autonomous as they move through the levels, which builds a positive attitude to lifelong learning; group work is a common feature."
  quote: full   # the issuer's statement is in `source` (D-std-0014)
  audience: both
  subjects: inherited
- id: qaa/dance-drama-and-performance-2024/3.12
  locator: { number: "3.12", headingPath: ["Content, structure and delivery", "Teaching and learning"] }
  span: { start: 48793, end: 49084 }
  source: "Learning and teaching will normally take place in a variety of continually evolving contexts, both in person and online, including an appropriate balance of workshops, rehearsals, productions, practical classes, laboratory/studio-based practice, screenings, lectures, seminars and tutorials."
  stem: none
  statementType: expectation
  rung: none
  force: will
  level: none
  appliesTo: "teaching and learning in the subject"
  addressee: provider
  verbs: ["take"]
  about: "a balance of settings, in person and online"
  themes: [none]
  domain: none
  award: ["bachelor's with honours", "master's"]
  gradeOf: none
  paraphrase: "Learning and teaching will normally happen in varied and changing settings, face to face and online, balancing workshops, rehearsals, productions, practical and studio classes, screenings, lectures, seminars and tutorials."
  quote: full   # the issuer's statement is in `source` (D-std-0014)
  audience: practitioner
  subjects: inherited
- id: qaa/dance-drama-and-performance-2024/3.15
  locator: { number: "3.15", headingPath: ["Content, structure and delivery", "Assessment"] }
  span: { start: 51632, end: 51714 }
  source: "Opportunities should be provided for self and peer assessment to support learning."
  stem: none
  statementType: expectation
  rung: none
  force: should
  level: none
  appliesTo: "assessment in the subject"
  addressee: both
  verbs: ["provided", "support"]
  about: "self and peer assessment for learning"
  themes: [none]
  domain: none
  award: ["bachelor's with honours", "master's"]
  gradeOf: none
  paraphrase: "Courses should give students chances to assess their own and each other's work, as support for learning."
  quote: full   # the issuer's statement is in `source` (D-std-0014)
  audience: both
  subjects: inherited
- id: qaa/dance-drama-and-performance-2024/3.16
  locator: { number: "3.16", headingPath: ["Content, structure and delivery", "Assessment"] }
  span: { start: 52148, end: 52322 }
  source: "Details regarding the provision of feedback, tutorial support (academic and pastoral), online resources and access, and bibliographies and screenings should also be included."
  stem: none
  statementType: expectation
  rung: none
  force: should
  level: none
  appliesTo: "course information"
  addressee: provider
  verbs: ["included"]
  about: "feedback, support and resources in course information"
  themes: [none]
  domain: none
  award: ["bachelor's with honours", "master's"]
  gradeOf: none
  paraphrase: "Course information should also set out feedback arrangements, academic and pastoral tutorial support, online resources and access, and reading and viewing lists."
  quote: full   # the issuer's statement is in `source` (D-std-0014)
  audience: practitioner
  subjects: inherited
- id: qaa/dance-drama-and-performance-2024/4.2
  locator: { number: "4.2", headingPath: ["Benchmark standards", "Introduction"] }
  span: { start: 53096, end: 53456 }
  source: "4.2 This Subject Benchmark Statement sets out the minimum threshold, typical and excellent standards that a student will have demonstrated when they are awarded an honours degree in Performance. Demonstrating these standards over time will show that a student has achieved the range of knowledge, understanding and skills expected of graduates in Performance.\n"
  stem: none
  statementType: expectation
  rung: none
  force: will
  level: fheq:6
  appliesTo: "honours graduates in Performance"
  addressee: learner
  verbs: ["sets", "demonstrated", "show"]
  about: "three rungs shown at the award of honours"
  themes: [none]
  domain: none
  award: ["bachelor's with honours"]
  gradeOf: none
  paraphrase: "The standards set out the minimum, typical and excellent achievement a student will have shown on being awarded an honours degree in Performance; showing them over time indicates the expected range of knowledge, understanding and skills."
  quote: full   # the issuer's statement is in `source` (D-std-0014)
  audience: both
  subjects: inherited
- id: qaa/dance-drama-and-performance-2024/4.3
  locator: { number: "4.3", headingPath: ["Benchmark standards", "Introduction"] }
  span: { start: 53456, end: 53941 }
  source: "4.3 The vast majority of students will perform significantly better than the minimum threshold standards. Each higher education provider has its own method of determining what appropriate evidence of this achievement will be and should refer to Annex D in The Frameworks for Higher Education Qualifications of UK Degree-Awarding Bodies. This Annex sets out common descriptions of the four main degree outcome classifications for bachelor's degrees with honours: 1st, 2.1, 2.2 and 3rd.\n"
  stem: none
  statementType: expectation
  rung: none
  force: should
  level: fheq:6
  appliesTo: "institutions and honours students in Performance"
  addressee: both
  verbs: ["perform", "refer"]
  about: "most exceed the threshold; Annex D for classification evidence"
  themes: [none]
  domain: none
  award: ["bachelor's with honours"]
  gradeOf: none
  paraphrase: "Most students will do well above the threshold; each institution decides what counts as evidence of that and should refer to Annex D of the qualification frameworks, which describes the four honours classes."
  quote: full   # the issuer's statement is in `source` (D-std-0014)
  audience: both
  subjects: inherited
- id: qaa/dance-drama-and-performance-2024/4.6
  locator: { number: "4.6", headingPath: ["Benchmark standards", "Introduction"] }
  span: { start: 54521, end: 55287 }
  source: "4.6 It is important that students are made aware of expected standards and inspired and supported to achieve beyond the threshold. Students will meet the threshold level if they have demonstrated, as appropriate to their course of study, knowledge, understanding, creativity and skill sufficient to provide a presentation of performance and/or information or arguments with respect to discipline-specific skills or materials. Students demonstrating excellent standards of work will tend to transcend the learning outcomes and display originality, insight and a selection or combination of qualities associated with artistic insight and/or technical excellence. They are also likely to demonstrate the highest standards of research appropriate to the field of study.\n"
  stem: none
  statementType: expectation
  rung: none
  force: will
  level: fheq:6
  appliesTo: "honours students in Performance"
  addressee: both
  verbs: ["made", "meet", "demonstrated", "transcend", "display", "demonstrate"]
  about: "what meeting the threshold and excellent work mean"
  themes: [none]
  domain: none
  award: ["bachelor's with honours"]
  gradeOf: none
  paraphrase: "It matters that students know the standards and are pushed and helped past the minimum. They will meet the threshold when, as fits their course, their knowledge, understanding, creativity and skill are enough to present performance or argument on the discipline's skills or materials; excellent work tends to go past the outcomes, with originality, insight, artistic or technical excellence and research of the highest standard."
  quote: full   # the issuer's statement is in `source` (D-std-0014)
  audience: both
  subjects: inherited
- id: qaa/dance-drama-and-performance-2024/4.7
  locator: { number: "4.7", headingPath: ["Benchmark standards", "Introduction"] }
  span: { start: 55772, end: 55933 }
  source: "However, all courses should embed and promote concepts and practices of accessibility, equality, diversity and inclusion, enterprise and sustainable development."
  stem: none
  statementType: expectation
  rung: none
  force: should
  level: none
  appliesTo: "all courses in the subject"
  addressee: provider
  verbs: ["embed", "promote"]
  about: "the cross-cutting themes in every course"
  themes: [none]
  domain: none
  award: ["bachelor's with honours", "master's"]
  gradeOf: none
  paraphrase: "Every course should build in and advance, as concepts and as practice, access, equality, diversity and inclusion, enterprise and sustainability."
  quote: full   # the issuer's statement is in `source` (D-std-0014)
  audience: practitioner
  subjects: inherited
- id: qaa/dance-drama-and-performance-2024/4.8.b1
  locator: { number: "4.8.b1", headingPath: ["Benchmark standards", "Threshold level"] }
  span: { start: 56049, end: 56162 }
  source: "knowledge of forms, practices, techniques, traditions, local and global histories and applications of Performance"
  stem: "4.8"
  statementType: threshold
  rung: threshold
  force: should
  level: fheq:6
  appliesTo: "honours graduates in Performance at the threshold rung"
  addressee: learner
  verbs: []
  about: "forms, traditions and histories of performance"
  themes: [none]
  domain: knowledge
  award: ["bachelor's with honours"]
  gradeOf: none
  paraphrase: "Should be able to show knowledge of performance's forms, practices, techniques and traditions, its local and global histories and its applications."
  quote: full   # the issuer's statement is in `source` (D-std-0014)
  audience: both
  subjects: inherited
- id: qaa/dance-drama-and-performance-2024/4.8.b2
  locator: { number: "4.8.b2", headingPath: ["Benchmark standards", "Threshold level"] }
  span: { start: 56169, end: 56313 }
  source: "knowledge of the key components of Performance and the processes by which it is created, realised, managed, distributed, consumed and documented"
  stem: "4.8"
  statementType: threshold
  rung: threshold
  force: should
  level: fheq:6
  appliesTo: "honours graduates in Performance at the threshold rung"
  addressee: learner
  verbs: []
  about: "components of performance and how it is made"
  themes: [none]
  domain: knowledge
  award: ["bachelor's with honours"]
  gradeOf: none
  paraphrase: "Should show knowledge of the main components of performance and of how work is made, realised, managed, distributed, received and recorded."
  quote: full   # the issuer's statement is in `source` (D-std-0014)
  audience: both
  subjects: inherited
- id: qaa/dance-drama-and-performance-2024/4.8.b3
  locator: { number: "4.8.b3", headingPath: ["Benchmark standards", "Threshold level"] }
  span: { start: 56316, end: 56409 }
  source: "knowledge of critical and theoretical perspectives appropriate to the study of the discipline"
  stem: "4.8"
  statementType: threshold
  rung: threshold
  force: should
  level: fheq:6
  appliesTo: "honours graduates in Performance at the threshold rung"
  addressee: learner
  verbs: []
  about: "critical and theoretical perspectives"
  themes: [none]
  domain: knowledge
  award: ["bachelor's with honours"]
  gradeOf: none
  paraphrase: "Should show knowledge of the critical and theoretical approaches suited to studying the discipline."
  quote: full   # the issuer's statement is in `source` (D-std-0014)
  audience: both
  subjects: inherited
- id: qaa/dance-drama-and-performance-2024/4.8.b4
  locator: { number: "4.8.b4", headingPath: ["Benchmark standards", "Threshold level"] }
  span: { start: 56412, end: 56517 }
  source: "knowledge of practitioners and practices, and/or theorists, and their cultural and/or historical contexts"
  stem: "4.8"
  statementType: threshold
  rung: threshold
  force: should
  level: fheq:6
  appliesTo: "honours graduates in Performance at the threshold rung"
  addressee: learner
  verbs: []
  about: "practitioners, theorists and their contexts"
  themes: [none]
  domain: knowledge
  award: ["bachelor's with honours"]
  gradeOf: none
  paraphrase: "Should show knowledge of practitioners and practices, or theorists, set in their cultural or historical contexts."
  quote: full   # the issuer's statement is in `source` (D-std-0014)
  audience: both
  subjects: inherited
- id: qaa/dance-drama-and-performance-2024/4.8.b5
  locator: { number: "4.8.b5", headingPath: ["Benchmark standards", "Threshold level"] }
  span: { start: 56520, end: 56642 }
  source: "knowledge of the role and function of Performance in social, educational, participatory and industry contexts and settings"
  stem: "4.8"
  statementType: threshold
  rung: threshold
  force: should
  level: fheq:6
  appliesTo: "honours graduates in Performance at the threshold rung"
  addressee: learner
  verbs: []
  about: "role of performance in society, education and industry"
  themes: [none]
  domain: knowledge
  award: ["bachelor's with honours"]
  gradeOf: none
  paraphrase: "Should show knowledge of what performance does and how it works in social, educational, participatory and industry settings."
  quote: full   # the issuer's statement is in `source` (D-std-0014)
  audience: both
  subjects: inherited
- id: qaa/dance-drama-and-performance-2024/4.8.b6
  locator: { number: "4.8.b6", headingPath: ["Benchmark standards", "Threshold level"] }
  span: { start: 56645, end: 56748 }
  source: "understanding of the interplay between critical and creative modes of enquiry within the field of study"
  stem: "4.8"
  statementType: threshold
  rung: threshold
  force: should
  level: fheq:6
  appliesTo: "honours graduates in Performance at the threshold rung"
  addressee: learner
  verbs: []
  about: "interplay of critical and creative enquiry"
  themes: [none]
  domain: understanding
  award: ["bachelor's with honours"]
  gradeOf: none
  paraphrase: "Should show understanding of how critical and creative ways of enquiring interact in the field."
  quote: full   # the issuer's statement is in `source` (D-std-0014)
  audience: both
  subjects: inherited
- id: qaa/dance-drama-and-performance-2024/4.8.b7
  locator: { number: "4.8.b7", headingPath: ["Benchmark standards", "Threshold level"] }
  span: { start: 56751, end: 56860 }
  source: "understanding of how to engage with and interpret texts, media, notations and/or scores to create Performance"
  stem: "4.8"
  statementType: threshold
  rung: threshold
  force: should
  level: fheq:6
  appliesTo: "honours graduates in Performance at the threshold rung"
  addressee: learner
  verbs: []
  about: "interpreting texts and scores to make performance"
  themes: [none]
  domain: understanding
  award: ["bachelor's with honours"]
  gradeOf: none
  paraphrase: "Should show understanding of how to work with and interpret texts, media, notations or scores in order to make performance."
  quote: full   # the issuer's statement is in `source` (D-std-0014)
  audience: both
  subjects: inherited
- id: qaa/dance-drama-and-performance-2024/4.8.b8
  locator: { number: "4.8.b8", headingPath: ["Benchmark standards", "Threshold level"] }
  span: { start: 56863, end: 56947 }
  source: "understanding of group and collective processes, and associated impacts and dynamics"
  stem: "4.8"
  statementType: threshold
  rung: threshold
  force: should
  level: fheq:6
  appliesTo: "honours graduates in Performance at the threshold rung"
  addressee: learner
  verbs: []
  about: "group and collective processes"
  themes: [none]
  domain: understanding
  award: ["bachelor's with honours"]
  gradeOf: none
  paraphrase: "Should show understanding of group and collective ways of working, with their effects and dynamics."
  quote: full   # the issuer's statement is in `source` (D-std-0014)
  audience: both
  subjects: inherited
- id: qaa/dance-drama-and-performance-2024/4.8.b9
  locator: { number: "4.8.b9", headingPath: ["Benchmark standards", "Threshold level"] }
  span: { start: 56950, end: 57141 }
  source: "understanding of key components of Performance within the disciplines, such as the role and function of source materials, performers, space, music, soundscapes, text, movement and environment"
  stem: "4.8"
  statementType: threshold
  rung: threshold
  force: should
  level: fheq:6
  appliesTo: "honours graduates in Performance at the threshold rung"
  addressee: learner
  verbs: []
  about: "elements of performance"
  themes: [none]
  domain: understanding
  award: ["bachelor's with honours"]
  gradeOf: none
  paraphrase: "Should show understanding of the key elements of performance in the disciplines, such as source material, performers, space, music, soundscape, text, movement and setting."
  quote: full   # the issuer's statement is in `source` (D-std-0014)
  audience: both
  subjects: inherited
- id: qaa/dance-drama-and-performance-2024/4.8.b10
  locator: { number: "4.8.b10", headingPath: ["Benchmark standards", "Threshold level"] }
  span: { start: 57144, end: 57238 }
  source: "understanding of appropriate interdisciplinary elements of Performance, and how to apply these"
  stem: "4.8"
  statementType: threshold
  rung: threshold
  force: should
  level: fheq:6
  appliesTo: "honours graduates in Performance at the threshold rung"
  addressee: learner
  verbs: []
  about: "interdisciplinary elements and their use"
  themes: [none]
  domain: understanding
  award: ["bachelor's with honours"]
  gradeOf: none
  paraphrase: "Should show understanding of the interdisciplinary elements relevant to performance and how to put them to use."
  quote: full   # the issuer's statement is in `source` (D-std-0014)
  audience: both
  subjects: inherited
- id: qaa/dance-drama-and-performance-2024/4.8.b11
  locator: { number: "4.8.b11", headingPath: ["Benchmark standards", "Threshold level"] }
  span: { start: 57241, end: 57323 }
  source: "understanding of knowledges, practices, concepts and skills from other disciplines"
  stem: "4.8"
  statementType: threshold
  rung: threshold
  force: should
  level: fheq:6
  appliesTo: "honours graduates in Performance at the threshold rung"
  addressee: learner
  verbs: []
  about: "knowledge and skills from other disciplines"
  themes: [none]
  domain: understanding
  award: ["bachelor's with honours"]
  gradeOf: none
  paraphrase: "Should show understanding of knowledge, practices, concepts and skills drawn from other disciplines."
  quote: full   # the issuer's statement is in `source` (D-std-0014)
  audience: both
  subjects: inherited
- id: qaa/dance-drama-and-performance-2024/4.8.b12
  locator: { number: "4.8.b12", headingPath: ["Benchmark standards", "Threshold level"] }
  span: { start: 57326, end: 57471 }
  source: "understanding of the responsibilities of performance practitioners to facilitate safe, ethical and environmentally sustainable working practices."
  stem: "4.8"
  statementType: threshold
  rung: threshold
  force: should
  level: fheq:6
  appliesTo: "honours graduates in Performance at the threshold rung"
  addressee: learner
  verbs: []
  about: "safe, ethical and sustainable working practice"
  themes: [none]
  domain: understanding
  award: ["bachelor's with honours"]
  gradeOf: none
  paraphrase: "Should show understanding of performance practitioners' duty to make working practice safe, ethical and environmentally sustainable."
  quote: full   # the issuer's statement is in `source` (D-std-0014)
  audience: both
  subjects: inherited
- id: qaa/dance-drama-and-performance-2024/4.9.b1
  locator: { number: "4.9.b1", headingPath: ["Benchmark standards", "Threshold level"] }
  span: { start: 57583, end: 57794 }
  source: "engage in the creation and/or production of Performance through utilisation of appropriate performance vocabularies, techniques, crafts, technologies, structures, contexts, working methods and research paradigms"
  stem: "4.9"
  statementType: threshold
  rung: threshold
  force: should
  level: fheq:6
  appliesTo: "honours graduates in Performance at the threshold rung"
  addressee: learner
  verbs: ["engage"]
  about: "creating or producing performance with the field's vocabularies and methods"
  themes: [none]
  domain: subject-skill
  award: ["bachelor's with honours"]
  gradeOf: none
  paraphrase: "Should be able to take part in making or producing performance, drawing on the field's vocabularies, techniques, crafts and technologies, its structures and contexts, and its working and research methods."
  quote: full   # the issuer's statement is in `source` (D-std-0014)
  audience: both
  subjects: inherited
- id: qaa/dance-drama-and-performance-2024/4.9.b2
  locator: { number: "4.9.b2", headingPath: ["Benchmark standards", "Threshold level"] }
  span: { start: 57797, end: 57987 }
  source: "understand the possibilities for Performance implied by a text, stimulus, media, dance notation or score and, as appropriate, realise these sources through design, technology and performance"
  stem: "4.9"
  statementType: threshold
  rung: threshold
  force: should
  level: fheq:6
  appliesTo: "honours graduates in Performance at the threshold rung"
  addressee: learner
  verbs: ["understand", "realise"]
  about: "realising the possibilities of a text, stimulus or score"
  themes: [none]
  domain: subject-skill
  award: ["bachelor's with honours"]
  gradeOf: none
  paraphrase: "Should be able to see what a text, stimulus, media, dance notation or score makes possible for performance and, where suitable, realise it through design, technology and performance."
  quote: full   # the issuer's statement is in `source` (D-std-0014)
  audience: both
  subjects: inherited
- id: qaa/dance-drama-and-performance-2024/4.9.b3
  locator: { number: "4.9.b3", headingPath: ["Benchmark standards", "Threshold level"] }
  span: { start: 57990, end: 58080 }
  source: "make records of Performance using skills and technologies in notation and/or documentation"
  stem: "4.9"
  statementType: threshold
  rung: threshold
  force: should
  level: fheq:6
  appliesTo: "honours graduates in Performance at the threshold rung"
  addressee: learner
  verbs: ["make"]
  about: "recording performance through notation or documentation"
  themes: [none]
  domain: subject-skill
  award: ["bachelor's with honours"]
  gradeOf: none
  paraphrase: "Should be able to record performance, using notation or documentation skills and technologies."
  quote: full   # the issuer's statement is in `source` (D-std-0014)
  audience: both
  subjects: inherited
- id: qaa/dance-drama-and-performance-2024/4.9.b4
  locator: { number: "4.9.b4", headingPath: ["Benchmark standards", "Threshold level"] }
  span: { start: 58083, end: 58135 }
  source: "describe, interpret, and evaluate Performance events"
  stem: "4.9"
  statementType: threshold
  rung: threshold
  force: should
  level: fheq:6
  appliesTo: "honours graduates in Performance at the threshold rung"
  addressee: learner
  verbs: ["describe", "interpret", "evaluate"]
  about: "describing, interpreting and evaluating performance events"
  themes: [none]
  domain: subject-skill
  award: ["bachelor's with honours"]
  gradeOf: none
  paraphrase: "Should be able to describe, interpret and evaluate performance events."
  quote: full   # the issuer's statement is in `source` (D-std-0014)
  audience: both
  subjects: inherited
- id: qaa/dance-drama-and-performance-2024/4.9.b5
  locator: { number: "4.9.b5", headingPath: ["Benchmark standards", "Threshold level"] }
  span: { start: 58138, end: 58291 }
  source: "engage in independent research, whether investigating past or present Performances or as part of the process of creating and/or responding to Performance"
  stem: "4.9"
  statementType: threshold
  rung: threshold
  force: should
  level: fheq:6
  appliesTo: "honours graduates in Performance at the threshold rung"
  addressee: learner
  verbs: ["engage"]
  about: "independent research into performance"
  themes: [none]
  domain: subject-skill
  award: ["bachelor's with honours"]
  gradeOf: none
  paraphrase: "Should be able to carry out independent research, whether into past or present performance or as part of making or responding to it."
  quote: full   # the issuer's statement is in `source` (D-std-0014)
  audience: both
  subjects: inherited
- id: qaa/dance-drama-and-performance-2024/4.9.b6
  locator: { number: "4.9.b6", headingPath: ["Benchmark standards", "Threshold level"] }
  span: { start: 58294, end: 58356 }
  source: "identify the cultural and contextual frameworks of Performance"
  stem: "4.9"
  statementType: threshold
  rung: threshold
  force: should
  level: fheq:6
  appliesTo: "honours graduates in Performance at the threshold rung"
  addressee: learner
  verbs: ["identify"]
  about: "identifying cultural and contextual frameworks"
  themes: [none]
  domain: subject-skill
  award: ["bachelor's with honours"]
  gradeOf: none
  paraphrase: "Should be able to identify the cultural and contextual frameworks within which performance sits."
  quote: full   # the issuer's statement is in `source` (D-std-0014)
  audience: both
  subjects: inherited
- id: qaa/dance-drama-and-performance-2024/4.9.b7
  locator: { number: "4.9.b7", headingPath: ["Benchmark standards", "Threshold level"] }
  span: { start: 58359, end: 58451 }
  source: "investigate performance environments to determine the significance of spatial relationships."
  stem: "4.9"
  statementType: threshold
  rung: threshold
  force: should
  level: fheq:6
  appliesTo: "honours graduates in Performance at the threshold rung"
  addressee: learner
  verbs: ["investigate", "determine"]
  about: "spatial relationships in performance environments"
  themes: [none]
  domain: subject-skill
  award: ["bachelor's with honours"]
  gradeOf: none
  paraphrase: "Should be able to investigate performance environments and work out what their spatial relationships mean."
  quote: full   # the issuer's statement is in `source` (D-std-0014)
  audience: both
  subjects: inherited
- id: qaa/dance-drama-and-performance-2024/4.10.b1
  locator: { number: "4.10.b1", headingPath: ["Benchmark standards", "Threshold level"] }
  span: { start: 58572, end: 58682 }
  source: "demonstrate skills in self-management, including the ability to set goals, manage workloads and meet deadlines"
  stem: "4.10"
  statementType: threshold
  rung: threshold
  force: should
  level: fheq:6
  appliesTo: "honours graduates in Performance at the threshold rung"
  addressee: learner
  verbs: ["demonstrate", "set", "manage", "meet"]
  about: "self-management: goals, workload and deadlines"
  themes: [none]
  domain: generic-skill
  award: ["bachelor's with honours"]
  gradeOf: none
  paraphrase: "Should be able to manage themselves: setting goals, handling workloads and meeting deadlines."
  quote: full   # the issuer's statement is in `source` (D-std-0014)
  audience: both
  subjects: inherited
- id: qaa/dance-drama-and-performance-2024/4.10.b2
  locator: { number: "4.10.b2", headingPath: ["Benchmark standards", "Threshold level"] }
  span: { start: 58685, end: 58760 }
  source: "display adaptability, flexibility and critical awareness of self and others"
  stem: "4.10"
  statementType: threshold
  rung: threshold
  force: should
  level: fheq:6
  appliesTo: "honours graduates in Performance at the threshold rung"
  addressee: learner
  verbs: ["display"]
  about: "adaptability and critical awareness of self and others"
  themes: [none]
  domain: generic-skill
  award: ["bachelor's with honours"]
  gradeOf: none
  paraphrase: "Should be able to show adaptability, flexibility and a critical awareness of themselves and others."
  quote: full   # the issuer's statement is in `source` (D-std-0014)
  audience: both
  subjects: inherited
- id: qaa/dance-drama-and-performance-2024/4.10.b3
  locator: { number: "4.10.b3", headingPath: ["Benchmark standards", "Threshold level"] }
  span: { start: 58763, end: 58822 }
  source: "assess and manage risk and employ ethical working practices"
  stem: "4.10"
  statementType: threshold
  rung: threshold
  force: should
  level: fheq:6
  appliesTo: "honours graduates in Performance at the threshold rung"
  addressee: learner
  verbs: ["assess", "manage", "employ"]
  about: "risk management and ethical practice"
  themes: [none]
  domain: generic-skill
  award: ["bachelor's with honours"]
  gradeOf: none
  paraphrase: "Should be able to assess and manage risk and work ethically."
  quote: full   # the issuer's statement is in `source` (D-std-0014)
  audience: both
  subjects: inherited
- id: qaa/dance-drama-and-performance-2024/4.10.b4
  locator: { number: "4.10.b4", headingPath: ["Benchmark standards", "Threshold level"] }
  span: { start: 58825, end: 59027 }
  source: "deploy skills in critical engagement, demonstrating the ability to operate and respond reflexively, creatively and critically, to develop ideas and to construct and present arguments in appropriate ways"
  stem: "4.10"
  statementType: threshold
  rung: threshold
  force: should
  level: fheq:6
  appliesTo: "honours graduates in Performance at the threshold rung"
  addressee: learner
  verbs: ["deploy", "operate", "respond", "develop", "construct", "present"]
  about: "critical engagement and argument"
  themes: [none]
  domain: generic-skill
  award: ["bachelor's with honours"]
  gradeOf: none
  paraphrase: "Should be able to engage critically, responding with reflexive, creative and critical thought, to develop ideas and build and present arguments suitably."
  quote: full   # the issuer's statement is in `source` (D-std-0014)
  audience: both
  subjects: inherited
- id: qaa/dance-drama-and-performance-2024/4.10.b5
  locator: { number: "4.10.b5", headingPath: ["Benchmark standards", "Threshold level"] }
  span: { start: 59030, end: 59139 }
  source: "work in a group or team and to have the skills needed for the realisation of collaborative project-based work"
  stem: "4.10"
  statementType: threshold
  rung: threshold
  force: should
  level: fheq:6
  appliesTo: "honours graduates in Performance at the threshold rung"
  addressee: learner
  verbs: ["work", "have"]
  about: "group and team work on collaborative projects"
  themes: [none]
  domain: generic-skill
  award: ["bachelor's with honours"]
  gradeOf: none
  paraphrase: "Should be able to work in a group or team, with the skills to carry out collaborative project work."
  quote: full   # the issuer's statement is in `source` (D-std-0014)
  audience: both
  subjects: inherited
- id: qaa/dance-drama-and-performance-2024/4.10.b6
  locator: { number: "4.10.b6", headingPath: ["Benchmark standards", "Threshold level"] }
  span: { start: 59142, end: 59264 }
  source: "demonstrate the ability to manage creative, personal and interpersonal relationship issues in the context of creative work"
  stem: "4.10"
  statementType: threshold
  rung: threshold
  force: should
  level: fheq:6
  appliesTo: "honours graduates in Performance at the threshold rung"
  addressee: learner
  verbs: ["demonstrate", "manage"]
  about: "managing creative, personal and interpersonal issues"
  themes: [none]
  domain: generic-skill
  award: ["bachelor's with honours"]
  gradeOf: none
  paraphrase: "Should be able to handle creative, personal and interpersonal relationship issues in creative work."
  quote: full   # the issuer's statement is in `source` (D-std-0014)
  audience: both
  subjects: inherited
- id: qaa/dance-drama-and-performance-2024/4.10.b7
  locator: { number: "4.10.b7", headingPath: ["Benchmark standards", "Threshold level"] }
  span: { start: 59267, end: 59444 }
  source: "demonstrate skills in communication and presentation and be able to articulate and communicate ideas and information in a variety of forms, as appropriate to content and context"
  stem: "4.10"
  statementType: threshold
  rung: threshold
  force: should
  level: fheq:6
  appliesTo: "honours graduates in Performance at the threshold rung"
  addressee: learner
  verbs: ["demonstrate", "articulate", "communicate"]
  about: "communication and presentation"
  themes: [none]
  domain: generic-skill
  award: ["bachelor's with honours"]
  gradeOf: none
  paraphrase: "Should be able to communicate and present, expressing ideas and information in different forms suited to content and context."
  quote: full   # the issuer's statement is in `source` (D-std-0014)
  audience: both
  subjects: inherited
- id: qaa/dance-drama-and-performance-2024/4.10.b8
  locator: { number: "4.10.b8", headingPath: ["Benchmark standards", "Threshold level"] }
  span: { start: 59447, end: 59563 }
  source: "deploy information management skills, be able to retrieve information, and to gather, sift, evaluate and organise it"
  stem: "4.10"
  statementType: threshold
  rung: threshold
  force: should
  level: fheq:6
  appliesTo: "honours graduates in Performance at the threshold rung"
  addressee: learner
  verbs: ["deploy", "retrieve", "gather", "sift", "evaluate", "organise"]
  about: "information management"
  themes: [none]
  domain: generic-skill
  award: ["bachelor's with honours"]
  gradeOf: none
  paraphrase: "Should be able to manage information: finding it, gathering, sifting, judging and organising it."
  quote: full   # the issuer's statement is in `source` (D-std-0014)
  audience: both
  subjects: inherited
- id: qaa/dance-drama-and-performance-2024/4.10.b9
  locator: { number: "4.10.b9", headingPath: ["Benchmark standards", "Threshold level"] }
  span: { start: 59566, end: 59660 }
  source: "demonstrate the ability to select, employ and adapt digital media and information technologies"
  stem: "4.10"
  statementType: threshold
  rung: threshold
  force: should
  level: fheq:6
  appliesTo: "honours graduates in Performance at the threshold rung"
  addressee: learner
  verbs: ["demonstrate", "select", "employ", "adapt"]
  about: "using digital media and information technology"
  themes: [none]
  domain: generic-skill
  award: ["bachelor's with honours"]
  gradeOf: none
  paraphrase: "Should be able to choose, use and adapt digital media and information technologies."
  quote: full   # the issuer's statement is in `source` (D-std-0014)
  audience: both
  subjects: inherited
- id: qaa/dance-drama-and-performance-2024/4.10.b10
  locator: { number: "4.10.b10", headingPath: ["Benchmark standards", "Threshold level"] }
  span: { start: 59663, end: 59740 }
  source: "use project management skills to investigate, organise and realise activities"
  stem: "4.10"
  statementType: threshold
  rung: threshold
  force: should
  level: fheq:6
  appliesTo: "honours graduates in Performance at the threshold rung"
  addressee: learner
  verbs: ["use", "investigate", "organise", "realise"]
  about: "project management"
  themes: [none]
  domain: generic-skill
  award: ["bachelor's with honours"]
  gradeOf: none
  paraphrase: "Should be able to use project management skills to investigate, organise and carry out activities."
  quote: full   # the issuer's statement is in `source` (D-std-0014)
  audience: both
  subjects: inherited
- id: qaa/dance-drama-and-performance-2024/4.10.b11
  locator: { number: "4.10.b11", headingPath: ["Benchmark standards", "Threshold level"] }
  span: { start: 59743, end: 59825 }
  source: "apply appropriate numeracy skills to solve problems and realise creative outcomes."
  stem: "4.10"
  statementType: threshold
  rung: threshold
  force: should
  level: fheq:6
  appliesTo: "honours graduates in Performance at the threshold rung"
  addressee: learner
  verbs: ["apply", "solve", "realise"]
  about: "numeracy for problem-solving and creative outcomes"
  themes: [none]
  domain: generic-skill
  award: ["bachelor's with honours"]
  gradeOf: none
  paraphrase: "Should be able to apply suitable numeracy skills to solve problems and achieve creative outcomes."
  quote: full   # the issuer's statement is in `source` (D-std-0014)
  audience: both
  subjects: inherited
- id: qaa/dance-drama-and-performance-2024/4.11.b1
  locator: { number: "4.11.b1", headingPath: ["Benchmark standards", "Typical level"] }
  span: { start: 59984, end: 60144 }
  source: "creative and critical engagement with forms, practices, techniques, traditions, histories and applications of Performance, and the capacity to problematise them"
  stem: "4.11"
  statementType: typical
  rung: typical
  force: should
  level: fheq:6
  appliesTo: "honours graduates in Performance at the typical rung"
  addressee: learner
  verbs: []
  about: "creative and critical engagement with forms and traditions, problematising them"
  themes: [none]
  domain: knowledge
  award: ["bachelor's with honours"]
  gradeOf: { statement: qaa/dance-drama-and-performance-2024/4.8.b1, basis: inferred }
  paraphrase: "Should show creative and critical engagement with performance's forms, practices, techniques, traditions, histories and applications, and be able to question them."
  quote: full   # the issuer's statement is in `source` (D-std-0014)
  audience: both
  subjects: inherited
- id: qaa/dance-drama-and-performance-2024/4.11.b2
  locator: { number: "4.11.b2", headingPath: ["Benchmark standards", "Typical level"] }
  span: { start: 60147, end: 60306 }
  source: "creative and critical engagement with the key components of Performance and the processes by which it is created, realised, managed, distributed and documented"
  stem: "4.11"
  statementType: typical
  rung: typical
  force: should
  level: fheq:6
  appliesTo: "honours graduates in Performance at the typical rung"
  addressee: learner
  verbs: []
  about: "creative and critical engagement with components and making"
  themes: [none]
  domain: knowledge
  award: ["bachelor's with honours"]
  gradeOf: { statement: qaa/dance-drama-and-performance-2024/4.8.b2, basis: inferred }
  paraphrase: "Should show creative and critical engagement with the main components of performance and with how work is made, realised, managed, distributed and recorded."
  quote: full   # the issuer's statement is in `source` (D-std-0014)
  audience: both
  subjects: inherited
- id: qaa/dance-drama-and-performance-2024/4.11.b3
  locator: { number: "4.11.b3", headingPath: ["Benchmark standards", "Typical level"] }
  span: { start: 60309, end: 60402 }
  source: "engagement with critical and theoretical perspectives appropriate to the study of Performance"
  stem: "4.11"
  statementType: typical
  rung: typical
  force: should
  level: fheq:6
  appliesTo: "honours graduates in Performance at the typical rung"
  addressee: learner
  verbs: []
  about: "engaging with critical and theoretical perspectives"
  themes: [none]
  domain: knowledge
  award: ["bachelor's with honours"]
  gradeOf: { statement: qaa/dance-drama-and-performance-2024/4.8.b3, basis: inferred }
  paraphrase: "Should show engagement with the critical and theoretical approaches suited to studying performance."
  quote: full   # the issuer's statement is in `source` (D-std-0014)
  audience: both
  subjects: inherited
- id: qaa/dance-drama-and-performance-2024/4.11.b4
  locator: { number: "4.11.b4", headingPath: ["Benchmark standards", "Typical level"] }
  span: { start: 60405, end: 60525 }
  source: "critical understanding of key practitioners and practices and/or theorists and their cultural and/or historical contexts"
  stem: "4.11"
  statementType: typical
  rung: typical
  force: should
  level: fheq:6
  appliesTo: "honours graduates in Performance at the typical rung"
  addressee: learner
  verbs: []
  about: "critical understanding of practitioners and contexts"
  themes: [none]
  domain: knowledge
  award: ["bachelor's with honours"]
  gradeOf: { statement: qaa/dance-drama-and-performance-2024/4.8.b4, basis: inferred }
  paraphrase: "Should show critical understanding of key practitioners, practices or theorists and their cultural or historical settings."
  quote: full   # the issuer's statement is in `source` (D-std-0014)
  audience: both
  subjects: inherited
- id: qaa/dance-drama-and-performance-2024/4.11.b5
  locator: { number: "4.11.b5", headingPath: ["Benchmark standards", "Typical level"] }
  span: { start: 60528, end: 60662 }
  source: "creative and critical engagement with the role and function of Performance in social, educational, participatory and industry contexts"
  stem: "4.11"
  statementType: typical
  rung: typical
  force: should
  level: fheq:6
  appliesTo: "honours graduates in Performance at the typical rung"
  addressee: learner
  verbs: []
  about: "engaging with the role of performance in society and industry"
  themes: [none]
  domain: knowledge
  award: ["bachelor's with honours"]
  gradeOf: { statement: qaa/dance-drama-and-performance-2024/4.8.b5, basis: inferred }
  paraphrase: "Should show creative and critical engagement with how performance functions in social, educational, participatory and industry settings."
  quote: full   # the issuer's statement is in `source` (D-std-0014)
  audience: both
  subjects: inherited
- id: qaa/dance-drama-and-performance-2024/4.11.b6
  locator: { number: "4.11.b6", headingPath: ["Benchmark standards", "Typical level"] }
  span: { start: 60665, end: 60775 }
  source: "strong understanding of the interplay between critical and creative modes of enquiry within the field of study"
  stem: "4.11"
  statementType: typical
  rung: typical
  force: should
  level: fheq:6
  appliesTo: "honours graduates in Performance at the typical rung"
  addressee: learner
  verbs: []
  about: "strong understanding of critical and creative enquiry"
  themes: [none]
  domain: understanding
  award: ["bachelor's with honours"]
  gradeOf: { statement: qaa/dance-drama-and-performance-2024/4.8.b6, basis: inferred }
  paraphrase: "Should show a strong understanding of how critical and creative enquiry interact in the field."
  quote: full   # the issuer's statement is in `source` (D-std-0014)
  audience: both
  subjects: inherited
- id: qaa/dance-drama-and-performance-2024/4.11.b7
  locator: { number: "4.11.b7", headingPath: ["Benchmark standards", "Typical level"] }
  span: { start: 60778, end: 60896 }
  source: "critical understanding of how to engage with and interpret texts, media, notations and/or scores to create Performance"
  stem: "4.11"
  statementType: typical
  rung: typical
  force: should
  level: fheq:6
  appliesTo: "honours graduates in Performance at the typical rung"
  addressee: learner
  verbs: []
  about: "critical interpretation of texts and scores"
  themes: [none]
  domain: understanding
  award: ["bachelor's with honours"]
  gradeOf: { statement: qaa/dance-drama-and-performance-2024/4.8.b7, basis: inferred }
  paraphrase: "Should show critical understanding of how to work with and interpret texts, media, notations or scores to make performance."
  quote: full   # the issuer's statement is in `source` (D-std-0014)
  audience: both
  subjects: inherited
- id: qaa/dance-drama-and-performance-2024/4.11.b8
  locator: { number: "4.11.b8", headingPath: ["Benchmark standards", "Typical level"] }
  span: { start: 60903, end: 60972 }
  source: "creative and critical understanding of group and collective processes"
  stem: "4.11"
  statementType: typical
  rung: typical
  force: should
  level: fheq:6
  appliesTo: "honours graduates in Performance at the typical rung"
  addressee: learner
  verbs: []
  about: "creative and critical understanding of group processes"
  themes: [none]
  domain: understanding
  award: ["bachelor's with honours"]
  gradeOf: { statement: qaa/dance-drama-and-performance-2024/4.8.b8, basis: inferred }
  paraphrase: "Should show creative and critical understanding of group and collective ways of working."
  quote: full   # the issuer's statement is in `source` (D-std-0014)
  audience: both
  subjects: inherited
- id: qaa/dance-drama-and-performance-2024/4.11.b9
  locator: { number: "4.11.b9", headingPath: ["Benchmark standards", "Typical level"] }
  span: { start: 60975, end: 61182 }
  source: "creative and critical understanding of key components of Performance within the disciplines such as the role and function of source materials, performers, bodies, space, sound, text, movement and environment"
  stem: "4.11"
  statementType: typical
  rung: typical
  force: should
  level: fheq:6
  appliesTo: "honours graduates in Performance at the typical rung"
  addressee: learner
  verbs: []
  about: "creative and critical understanding of the elements of performance"
  themes: [none]
  domain: understanding
  award: ["bachelor's with honours"]
  gradeOf: { statement: qaa/dance-drama-and-performance-2024/4.8.b9, basis: inferred }
  paraphrase: "Should show creative and critical understanding of the key elements of performance, such as sources, performers, bodies, space, sound, text, movement and setting."
  quote: full   # the issuer's statement is in `source` (D-std-0014)
  audience: both
  subjects: inherited
- id: qaa/dance-drama-and-performance-2024/4.11.b10
  locator: { number: "4.11.b10", headingPath: ["Benchmark standards", "Typical level"] }
  span: { start: 61185, end: 61359 }
  source: "creative and critical understanding of appropriate interdisciplinary elements of Performance and how to apply knowledge, practices, concepts and skills from other disciplines"
  stem: "4.11"
  statementType: typical
  rung: typical
  force: should
  level: fheq:6
  appliesTo: "honours graduates in Performance at the typical rung"
  addressee: learner
  verbs: []
  about: "interdisciplinary elements and drawing on other fields"
  themes: [none]
  domain: understanding
  award: ["bachelor's with honours"]
  gradeOf: { statement: qaa/dance-drama-and-performance-2024/4.8.b10, basis: inferred }
  paraphrase: "Should show creative and critical understanding of suitable interdisciplinary elements of performance and how to use ideas, methods and skills taken from other fields."
  quote: full   # the issuer's statement is in `source` (D-std-0014)
  audience: both
  subjects: inherited
- id: qaa/dance-drama-and-performance-2024/4.11.b11
  locator: { number: "4.11.b11", headingPath: ["Benchmark standards", "Typical level"] }
  span: { start: 61362, end: 61516 }
  source: "critical understanding of the responsibilities of performance practitioners to facilitate safe, environmentally sustainable and ethical working practices."
  stem: "4.11"
  statementType: typical
  rung: typical
  force: should
  level: fheq:6
  appliesTo: "honours graduates in Performance at the typical rung"
  addressee: learner
  verbs: []
  about: "critical understanding of safe, sustainable and ethical practice"
  themes: [none]
  domain: understanding
  award: ["bachelor's with honours"]
  gradeOf: { statement: qaa/dance-drama-and-performance-2024/4.8.b12, basis: inferred }
  paraphrase: "Should show critical understanding of performance practitioners' duty to make working practice safe, environmentally sustainable and ethical."
  quote: full   # the issuer's statement is in `source` (D-std-0014)
  audience: both
  subjects: inherited
- id: qaa/dance-drama-and-performance-2024/4.12.b1
  locator: { number: "4.12.b1", headingPath: ["Benchmark standards", "Typical level"] }
  span: { start: 61629, end: 61801 }
  source: "engage creatively and critically with the skills and processes of performance and production, and demonstrate the ability to select, refine and present these in Performance"
  stem: "4.12"
  statementType: typical
  rung: typical
  force: should
  level: fheq:6
  appliesTo: "honours graduates in Performance at the typical rung"
  addressee: learner
  verbs: ["engage", "demonstrate", "select", "refine", "present"]
  about: "selecting, refining and presenting performance and production skills"
  themes: [none]
  domain: subject-skill
  award: ["bachelor's with honours"]
  gradeOf: none
  paraphrase: "Should be able to work creatively and critically with performance and production skills and processes, choosing, refining and presenting them in performance."
  quote: full   # the issuer's statement is in `source` (D-std-0014)
  audience: both
  subjects: inherited
- id: qaa/dance-drama-and-performance-2024/4.12.b2
  locator: { number: "4.12.b2", headingPath: ["Benchmark standards", "Typical level"] }
  span: { start: 61804, end: 62009 }
  source: "engage creatively and critically with the possibilities for Performance implied by a text, stimulus, notation or score, and, as appropriate, realise these sources sensitively through design and performance"
  stem: "4.12"
  statementType: typical
  rung: typical
  force: should
  level: fheq:6
  appliesTo: "honours graduates in Performance at the typical rung"
  addressee: learner
  verbs: ["engage", "realise"]
  about: "realising a text or score sensitively"
  themes: [none]
  domain: subject-skill
  award: ["bachelor's with honours"]
  gradeOf: { statement: qaa/dance-drama-and-performance-2024/4.9.b2, basis: inferred }
  paraphrase: "Should be able to work creatively and critically with what a text, stimulus, notation or score offers performance, and where suitable realise it with sensitivity through design and performance."
  quote: full   # the issuer's statement is in `source` (D-std-0014)
  audience: both
  subjects: inherited
- id: qaa/dance-drama-and-performance-2024/4.12.b3
  locator: { number: "4.12.b3", headingPath: ["Benchmark standards", "Typical level"] }
  span: { start: 62012, end: 62221 }
  source: "engage creatively and critically with the creation and/or production of Performance through a developed understanding of appropriate performance vocabularies, techniques, crafts, structures and working methods"
  stem: "4.12"
  statementType: typical
  rung: typical
  force: should
  level: fheq:6
  appliesTo: "honours graduates in Performance at the typical rung"
  addressee: learner
  verbs: ["engage"]
  about: "making performance with a developed grasp of its vocabularies"
  themes: [none]
  domain: subject-skill
  award: ["bachelor's with honours"]
  gradeOf: { statement: qaa/dance-drama-and-performance-2024/4.9.b1, basis: inferred }
  paraphrase: "Should be able to work creatively and critically on making or producing performance, with a developed grasp of suitable vocabularies, techniques, crafts, structures and working methods."
  quote: full   # the issuer's statement is in `source` (D-std-0014)
  audience: both
  subjects: inherited
- id: qaa/dance-drama-and-performance-2024/4.12.b4
  locator: { number: "4.12.b4", headingPath: ["Benchmark standards", "Typical level"] }
  span: { start: 62224, end: 62398 }
  source: "engage creatively and critically in appropriate independent research, whether investigating past or present performances or as part of the process of creating new performance"
  stem: "4.12"
  statementType: typical
  rung: typical
  force: should
  level: fheq:6
  appliesTo: "honours graduates in Performance at the typical rung"
  addressee: learner
  verbs: ["engage"]
  about: "creative and critical independent research"
  themes: [none]
  domain: subject-skill
  award: ["bachelor's with honours"]
  gradeOf: { statement: qaa/dance-drama-and-performance-2024/4.9.b5, basis: inferred }
  paraphrase: "Should be able to carry out suitable independent research creatively and critically, whether into past or present performance or within the making of new work."
  quote: full   # the issuer's statement is in `source` (D-std-0014)
  audience: both
  subjects: inherited
- id: qaa/dance-drama-and-performance-2024/4.12.b5
  locator: { number: "4.12.b5", headingPath: ["Benchmark standards", "Typical level"] }
  span: { start: 62401, end: 62543 }
  source: "identify and interpret the cultural frameworks that surround performance events and their specific relation to social and historical contexts."
  stem: "4.12"
  statementType: typical
  rung: typical
  force: should
  level: fheq:6
  appliesTo: "honours graduates in Performance at the typical rung"
  addressee: learner
  verbs: ["identify", "interpret"]
  about: "interpreting cultural frameworks in social and historical context"
  themes: [none]
  domain: subject-skill
  award: ["bachelor's with honours"]
  gradeOf: { statement: qaa/dance-drama-and-performance-2024/4.9.b6, basis: inferred }
  paraphrase: "Should be able to identify and interpret the cultural frameworks around performance events and how they relate to social and historical contexts."
  quote: full   # the issuer's statement is in `source` (D-std-0014)
  audience: both
  subjects: inherited
- id: qaa/dance-drama-and-performance-2024/4.13.b1
  locator: { number: "4.13.b1", headingPath: ["Benchmark standards", "Typical level"] }
  span: { start: 62660, end: 62807 }
  source: "have critical and analytical skills in developing ideas and constructing arguments and the capacity to evaluate and present them in a range of ways"
  stem: "4.13"
  statementType: typical
  rung: typical
  force: should
  level: fheq:6
  appliesTo: "honours graduates in Performance at the typical rung"
  addressee: learner
  verbs: ["have", "developing", "constructing", "evaluate", "present"]
  about: "critical and analytical argument"
  themes: [none]
  domain: generic-skill
  award: ["bachelor's with honours"]
  gradeOf: { statement: qaa/dance-drama-and-performance-2024/4.10.b4, basis: inferred }
  paraphrase: "Should be able to analyse critically when developing ideas and building arguments, and judge and present them in different ways."
  quote: full   # the issuer's statement is in `source` (D-std-0014)
  audience: both
  subjects: inherited
- id: qaa/dance-drama-and-performance-2024/4.13.b2
  locator: { number: "4.13.b2", headingPath: ["Benchmark standards", "Typical level"] }
  span: { start: 62810, end: 62972 }
  source: "demonstrate a developed capacity to examine and evaluate forms of discourse and their effects on representation and reception in the arts and culture more broadly"
  stem: "4.13"
  statementType: typical
  rung: typical
  force: should
  level: fheq:6
  appliesTo: "honours graduates in Performance at the typical rung"
  addressee: learner
  verbs: ["demonstrate", "examine", "evaluate"]
  about: "discourse and its effects on representation and reception"
  themes: [none]
  domain: generic-skill
  award: ["bachelor's with honours"]
  gradeOf: none
  paraphrase: "Should show a developed ability to examine and evaluate kinds of discourse and their effects on how the arts and wider culture represent and are received."
  quote: full   # the issuer's statement is in `source` (D-std-0014)
  audience: both
  subjects: inherited
- id: qaa/dance-drama-and-performance-2024/4.13.b3
  locator: { number: "4.13.b3", headingPath: ["Benchmark standards", "Typical level"] }
  span: { start: 62975, end: 63120 }
  source: "work productively, creatively and imaginatively as part of a group and have the creative skills needed for the realisation of practice-based work"
  stem: "4.13"
  statementType: typical
  rung: typical
  force: should
  level: fheq:6
  appliesTo: "honours graduates in Performance at the typical rung"
  addressee: learner
  verbs: ["work", "have"]
  about: "productive, creative group work on practice-based projects"
  themes: [none]
  domain: generic-skill
  award: ["bachelor's with honours"]
  gradeOf: { statement: qaa/dance-drama-and-performance-2024/4.10.b5, basis: inferred }
  paraphrase: "Should be able to work productively, creatively and imaginatively in a group, with the creative skills to carry out practice-based work."
  quote: full   # the issuer's statement is in `source` (D-std-0014)
  audience: both
  subjects: inherited
- id: qaa/dance-drama-and-performance-2024/4.13.b4
  locator: { number: "4.13.b4", headingPath: ["Benchmark standards", "Typical level"] }
  span: { start: 63123, end: 63249 }
  source: "manage personal workloads efficiently and effectively, meet deadlines, and negotiate and successfully pursue goals with others"
  stem: "4.13"
  statementType: typical
  rung: typical
  force: should
  level: fheq:6
  appliesTo: "honours graduates in Performance at the typical rung"
  addressee: learner
  verbs: ["manage", "meet", "negotiate", "pursue"]
  about: "workload, deadlines and goals with others"
  themes: [none]
  domain: generic-skill
  award: ["bachelor's with honours"]
  gradeOf: { statement: qaa/dance-drama-and-performance-2024/4.10.b1, basis: inferred }
  paraphrase: "Should be able to manage their own workload efficiently and effectively, meet deadlines, and agree and pursue goals with others successfully."
  quote: full   # the issuer's statement is in `source` (D-std-0014)
  audience: both
  subjects: inherited
- id: qaa/dance-drama-and-performance-2024/4.13.b5
  locator: { number: "4.13.b5", headingPath: ["Benchmark standards", "Typical level"] }
  span: { start: 63252, end: 63365 }
  source: "constructively and effectively manage creative, personal and interpersonal issues in the context of creative work"
  stem: "4.13"
  statementType: typical
  rung: typical
  force: should
  level: fheq:6
  appliesTo: "honours graduates in Performance at the typical rung"
  addressee: learner
  verbs: ["manage"]
  about: "managing creative and interpersonal issues constructively"
  themes: [none]
  domain: generic-skill
  award: ["bachelor's with honours"]
  gradeOf: { statement: qaa/dance-drama-and-performance-2024/4.10.b6, basis: inferred }
  paraphrase: "Should be able to manage creative, personal and interpersonal issues in creative work constructively and effectively."
  quote: full   # the issuer's statement is in `source` (D-std-0014)
  audience: both
  subjects: inherited
- id: qaa/dance-drama-and-performance-2024/4.13.b6
  locator: { number: "4.13.b6", headingPath: ["Benchmark standards", "Typical level"] }
  span: { start: 63368, end: 63507 }
  source: "use the information retrieval skills needed to gather, sift and organise material independently and to critically evaluate its significance"
  stem: "4.13"
  statementType: typical
  rung: typical
  force: should
  level: fheq:6
  appliesTo: "honours graduates in Performance at the typical rung"
  addressee: learner
  verbs: ["use", "gather", "sift", "organise", "evaluate"]
  about: "independent information retrieval and critical evaluation"
  themes: [none]
  domain: generic-skill
  award: ["bachelor's with honours"]
  gradeOf: { statement: qaa/dance-drama-and-performance-2024/4.10.b8, basis: inferred }
  paraphrase: "Should be able to use information retrieval skills to gather, sift and organise material on their own and to judge its significance critically."
  quote: full   # the issuer's statement is in `source` (D-std-0014)
  audience: both
  subjects: inherited
- id: qaa/dance-drama-and-performance-2024/4.13.b7
  locator: { number: "4.13.b7", headingPath: ["Benchmark standards", "Typical level"] }
  span: { start: 63510, end: 63670 }
  source: "demonstrate appropriate technological and digital skills, and have developed considerable awareness of their application and potential within the field of study"
  stem: "4.13"
  statementType: typical
  rung: typical
  force: should
  level: fheq:6
  appliesTo: "honours graduates in Performance at the typical rung"
  addressee: learner
  verbs: ["demonstrate", "have"]
  about: "technological and digital skills and awareness"
  themes: [none]
  domain: generic-skill
  award: ["bachelor's with honours"]
  gradeOf: { statement: qaa/dance-drama-and-performance-2024/4.10.b9, basis: inferred }
  paraphrase: "Should show suitable technological and digital skills and a considerable awareness of how they apply and what they could do in the field."
  quote: full   # the issuer's statement is in `source` (D-std-0014)
  audience: both
  subjects: inherited
- id: qaa/dance-drama-and-performance-2024/4.13.b8
  locator: { number: "4.13.b8", headingPath: ["Benchmark standards", "Typical level"] }
  span: { start: 63677, end: 63783 }
  source: "identify and apply a range of appropriate numeracy skills to solve problems and realise creative outcomes."
  stem: "4.13"
  statementType: typical
  rung: typical
  force: should
  level: fheq:6
  appliesTo: "honours graduates in Performance at the typical rung"
  addressee: learner
  verbs: ["identify", "apply", "solve", "realise"]
  about: "choosing and applying numeracy skills"
  themes: [none]
  domain: generic-skill
  award: ["bachelor's with honours"]
  gradeOf: { statement: qaa/dance-drama-and-performance-2024/4.10.b11, basis: inferred }
  paraphrase: "Should be able to identify and apply a range of suitable numeracy skills to solve problems and achieve creative outcomes."
  quote: full   # the issuer's statement is in `source` (D-std-0014)
  audience: both
  subjects: inherited
- id: qaa/dance-drama-and-performance-2024/4.14.b1
  locator: { number: "4.14.b1", headingPath: ["Benchmark standards", "Excellent level"] }
  span: { start: 63978, end: 64124 }
  source: "sophisticated engagement with, and ability to interrogate, the forms, practices, techniques, traditions, histories and applications of Performance"
  stem: "4.14"
  statementType: excellent
  rung: excellent
  force: should
  level: fheq:6
  appliesTo: "honours graduates in Performance at the excellent rung"
  addressee: learner
  verbs: []
  about: "sophisticated engagement with forms and traditions, interrogating them"
  themes: [none]
  domain: knowledge
  award: ["bachelor's with honours"]
  gradeOf: { statement: qaa/dance-drama-and-performance-2024/4.11.b1, basis: inferred }
  paraphrase: "Should show sophisticated engagement with performance's forms, practices, techniques, traditions, histories and applications, and the ability to interrogate them."
  quote: full   # the issuer's statement is in `source` (D-std-0014)
  audience: both
  subjects: inherited
- id: qaa/dance-drama-and-performance-2024/4.14.b2
  locator: { number: "4.14.b2", headingPath: ["Benchmark standards", "Excellent level"] }
  span: { start: 64127, end: 64343 }
  source: "sophisticated creative and theoretical engagement with the key components of Performance and the processes by which it is created, realised, managed, distributed, interpreted and documented, leading to novel insights"
  stem: "4.14"
  statementType: excellent
  rung: excellent
  force: should
  level: fheq:6
  appliesTo: "honours graduates in Performance at the excellent rung"
  addressee: learner
  verbs: []
  about: "sophisticated engagement with components and making, leading to new insight"
  themes: [none]
  domain: knowledge
  award: ["bachelor's with honours"]
  gradeOf: { statement: qaa/dance-drama-and-performance-2024/4.11.b2, basis: inferred }
  paraphrase: "Should show sophisticated creative and theoretical engagement with performance's components and with how work is made, realised, managed, distributed, interpreted and recorded, producing new insight."
  quote: full   # the issuer's statement is in `source` (D-std-0014)
  audience: both
  subjects: inherited
- id: qaa/dance-drama-and-performance-2024/4.14.b3
  locator: { number: "4.14.b3", headingPath: ["Benchmark standards", "Excellent level"] }
  span: { start: 64346, end: 64453 }
  source: "sophisticated engagement with critical and theoretical perspectives appropriate to the study of Performance"
  stem: "4.14"
  statementType: excellent
  rung: excellent
  force: should
  level: fheq:6
  appliesTo: "honours graduates in Performance at the excellent rung"
  addressee: learner
  verbs: []
  about: "sophisticated engagement with critical and theoretical perspectives"
  themes: [none]
  domain: knowledge
  award: ["bachelor's with honours"]
  gradeOf: { statement: qaa/dance-drama-and-performance-2024/4.11.b3, basis: inferred }
  paraphrase: "Should show sophisticated engagement with the critical and theoretical approaches suited to studying performance."
  quote: full   # the issuer's statement is in `source` (D-std-0014)
  audience: both
  subjects: inherited
- id: qaa/dance-drama-and-performance-2024/4.14.b4
  locator: { number: "4.14.b4", headingPath: ["Benchmark standards", "Excellent level"] }
  span: { start: 64456, end: 64595 }
  source: "comprehensive and critical understanding of key practitioners and practices and/or theorists, and their cultural and/or historical contexts"
  stem: "4.14"
  statementType: excellent
  rung: excellent
  force: should
  level: fheq:6
  appliesTo: "honours graduates in Performance at the excellent rung"
  addressee: learner
  verbs: []
  about: "comprehensive, critical understanding of practitioners and contexts"
  themes: [none]
  domain: knowledge
  award: ["bachelor's with honours"]
  gradeOf: { statement: qaa/dance-drama-and-performance-2024/4.11.b4, basis: inferred }
  paraphrase: "Should show a comprehensive and critical understanding of key practitioners, practices or theorists and their cultural or historical settings."
  quote: full   # the issuer's statement is in `source` (D-std-0014)
  audience: both
  subjects: inherited
- id: qaa/dance-drama-and-performance-2024/4.14.b5
  locator: { number: "4.14.b5", headingPath: ["Benchmark standards", "Excellent level"] }
  span: { start: 64598, end: 64724 }
  source: "sophisticated engagement with the role and function of Performance in social, educational, participatory and industry contexts"
  stem: "4.14"
  statementType: excellent
  rung: excellent
  force: should
  level: fheq:6
  appliesTo: "honours graduates in Performance at the excellent rung"
  addressee: learner
  verbs: []
  about: "sophisticated engagement with the role of performance in society and industry"
  themes: [none]
  domain: knowledge
  award: ["bachelor's with honours"]
  gradeOf: { statement: qaa/dance-drama-and-performance-2024/4.11.b5, basis: inferred }
  paraphrase: "Should show sophisticated engagement with how performance functions in social, educational, participatory and industry settings."
  quote: full   # the issuer's statement is in `source` (D-std-0014)
  audience: both
  subjects: inherited
- id: qaa/dance-drama-and-performance-2024/4.14.b6
  locator: { number: "4.14.b6", headingPath: ["Benchmark standards", "Excellent level"] }
  span: { start: 64727, end: 64844 }
  source: "sophisticated understanding of the interplay between critical and creative modes of enquiry within the field of study"
  stem: "4.14"
  statementType: excellent
  rung: excellent
  force: should
  level: fheq:6
  appliesTo: "honours graduates in Performance at the excellent rung"
  addressee: learner
  verbs: []
  about: "sophisticated understanding of critical and creative enquiry"
  themes: [none]
  domain: understanding
  award: ["bachelor's with honours"]
  gradeOf: { statement: qaa/dance-drama-and-performance-2024/4.11.b6, basis: inferred }
  paraphrase: "Should show sophisticated understanding of how critical and creative enquiry interact in the field."
  quote: full   # the issuer's statement is in `source` (D-std-0014)
  audience: both
  subjects: inherited
- id: qaa/dance-drama-and-performance-2024/4.14.b7
  locator: { number: "4.14.b7", headingPath: ["Benchmark standards", "Excellent level"] }
  span: { start: 64847, end: 64976 }
  source: "sophisticated understanding of how to engage with and interpret texts, media, dance notations and/or scores to create performance"
  stem: "4.14"
  statementType: excellent
  rung: excellent
  force: should
  level: fheq:6
  appliesTo: "honours graduates in Performance at the excellent rung"
  addressee: learner
  verbs: []
  about: "sophisticated interpretation of texts, notations and scores"
  themes: [none]
  domain: understanding
  award: ["bachelor's with honours"]
  gradeOf: { statement: qaa/dance-drama-and-performance-2024/4.11.b7, basis: inferred }
  paraphrase: "Should show sophisticated understanding of how to work with and interpret texts, media, dance notations or scores to make performance."
  quote: full   # the issuer's statement is in `source` (D-std-0014)
  audience: both
  subjects: inherited
- id: qaa/dance-drama-and-performance-2024/4.14.b8
  locator: { number: "4.14.b8", headingPath: ["Benchmark standards", "Excellent level"] }
  span: { start: 64979, end: 65050 }
  source: "sophisticated critical understanding and application of group processes"
  stem: "4.14"
  statementType: excellent
  rung: excellent
  force: should
  level: fheq:6
  appliesTo: "honours graduates in Performance at the excellent rung"
  addressee: learner
  verbs: []
  about: "sophisticated understanding and use of group processes"
  themes: [none]
  domain: understanding
  award: ["bachelor's with honours"]
  gradeOf: { statement: qaa/dance-drama-and-performance-2024/4.11.b8, basis: inferred }
  paraphrase: "Should show sophisticated critical understanding of group processes and the ability to apply it."
  quote: full   # the issuer's statement is in `source` (D-std-0014)
  audience: both
  subjects: inherited
- id: qaa/dance-drama-and-performance-2024/4.14.b9
  locator: { number: "4.14.b9", headingPath: ["Benchmark standards", "Excellent level"] }
  span: { start: 65053, end: 65259 }
  source: "sophisticated critical understanding of key components of Performance within the disciplines such as the role and function of source materials, performers, body, space, sound, text, movement and environment"
  stem: "4.14"
  statementType: excellent
  rung: excellent
  force: should
  level: fheq:6
  appliesTo: "honours graduates in Performance at the excellent rung"
  addressee: learner
  verbs: []
  about: "sophisticated understanding of the elements of performance"
  themes: [none]
  domain: understanding
  award: ["bachelor's with honours"]
  gradeOf: { statement: qaa/dance-drama-and-performance-2024/4.11.b9, basis: inferred }
  paraphrase: "Should show sophisticated critical understanding of the key elements of performance, such as sources, performers, the body, space, sound, text, movement and setting."
  quote: full   # the issuer's statement is in `source` (D-std-0014)
  audience: both
  subjects: inherited
- id: qaa/dance-drama-and-performance-2024/4.14.b10
  locator: { number: "4.14.b10", headingPath: ["Benchmark standards", "Excellent level"] }
  span: { start: 65262, end: 65437 }
  source: "sophisticated critical understanding of appropriate interdisciplinary elements of Performance and how to apply knowledge, practices, concepts and skills from other disciplines"
  stem: "4.14"
  statementType: excellent
  rung: excellent
  force: should
  level: fheq:6
  appliesTo: "honours graduates in Performance at the excellent rung"
  addressee: learner
  verbs: []
  about: "sophisticated understanding of interdisciplinary elements and other fields"
  themes: [none]
  domain: understanding
  award: ["bachelor's with honours"]
  gradeOf: { statement: qaa/dance-drama-and-performance-2024/4.11.b10, basis: inferred }
  paraphrase: "Should show sophisticated critical understanding of suitable interdisciplinary elements of performance and of how to use ideas, methods and skills from other fields."
  quote: full   # the issuer's statement is in `source` (D-std-0014)
  audience: both
  subjects: inherited
- id: qaa/dance-drama-and-performance-2024/4.14.b11
  locator: { number: "4.14.b11", headingPath: ["Benchmark standards", "Excellent level"] }
  span: { start: 65440, end: 65599 }
  source: "comprehensive understanding of the responsibilities of performance practitioners to facilitate safe, environmentally sustainable and ethical working practices."
  stem: "4.14"
  statementType: excellent
  rung: excellent
  force: should
  level: fheq:6
  appliesTo: "honours graduates in Performance at the excellent rung"
  addressee: learner
  verbs: []
  about: "comprehensive understanding of safe, sustainable and ethical practice"
  themes: [none]
  domain: understanding
  award: ["bachelor's with honours"]
  gradeOf: { statement: qaa/dance-drama-and-performance-2024/4.11.b11, basis: inferred }
  paraphrase: "Should show comprehensive understanding of performance practitioners' duty to make working practice safe, environmentally sustainable and ethical."
  quote: full   # the issuer's statement is in `source` (D-std-0014)
  audience: both
  subjects: inherited
- id: qaa/dance-drama-and-performance-2024/4.15.b1
  locator: { number: "4.15.b1", headingPath: ["Benchmark standards", "Excellent level"] }
  span: { start: 65712, end: 65878 }
  source: "engage critically and comprehensively with the processes of Performance and production, and demonstrate the ability to select, refine and present these in Performance"
  stem: "4.15"
  statementType: excellent
  rung: excellent
  force: should
  level: fheq:6
  appliesTo: "honours graduates in Performance at the excellent rung"
  addressee: learner
  verbs: ["engage", "demonstrate", "select", "refine", "present"]
  about: "thorough critical command of performance and production processes"
  themes: [none]
  domain: subject-skill
  award: ["bachelor's with honours"]
  gradeOf: { statement: qaa/dance-drama-and-performance-2024/4.12.b1, basis: inferred }
  paraphrase: "Should be able to handle performance and production processes with critical depth and thoroughness, choosing, refining and presenting them in performance."
  quote: full   # the issuer's statement is in `source` (D-std-0014)
  audience: both
  subjects: inherited
- id: qaa/dance-drama-and-performance-2024/4.15.b2
  locator: { number: "4.15.b2", headingPath: ["Benchmark standards", "Excellent level"] }
  span: { start: 65881, end: 66116 }
  source: "engage creatively and thoroughly with the possibilities for Performance implied by a text, dance notation or score and, as appropriate, realise these sources sensitively through design and performance, leading to novel or original work"
  stem: "4.15"
  statementType: excellent
  rung: excellent
  force: should
  level: fheq:6
  appliesTo: "honours graduates in Performance at the excellent rung"
  addressee: learner
  verbs: ["engage", "realise"]
  about: "realising a text or score to make new or original work"
  themes: [none]
  domain: subject-skill
  award: ["bachelor's with honours"]
  gradeOf: { statement: qaa/dance-drama-and-performance-2024/4.12.b2, basis: inferred }
  paraphrase: "Should be able to work creatively and thoroughly with what a text, dance notation or score offers performance and, where suitable, realise it with sensitivity through design and performance, producing new or original work."
  quote: full   # the issuer's statement is in `source` (D-std-0014)
  audience: both
  subjects: inherited
- id: qaa/dance-drama-and-performance-2024/4.15.b3
  locator: { number: "4.15.b3", headingPath: ["Benchmark standards", "Excellent level"] }
  span: { start: 66119, end: 66347 }
  source: "engage creatively and comprehensively with the creation and/or production of Performance, through a developed and thorough understanding of appropriate performance vocabularies, techniques, crafts, structures and working methods"
  stem: "4.15"
  statementType: excellent
  rung: excellent
  force: should
  level: fheq:6
  appliesTo: "honours graduates in Performance at the excellent rung"
  addressee: learner
  verbs: ["engage"]
  about: "making performance with a thorough grasp of its vocabularies"
  themes: [none]
  domain: subject-skill
  award: ["bachelor's with honours"]
  gradeOf: { statement: qaa/dance-drama-and-performance-2024/4.12.b3, basis: inferred }
  paraphrase: "Should be able to work creatively and comprehensively on making or producing performance, with a developed and thorough grasp of suitable vocabularies, techniques, crafts, structures and working methods."
  quote: full   # the issuer's statement is in `source` (D-std-0014)
  audience: both
  subjects: inherited
- id: qaa/dance-drama-and-performance-2024/4.15.b4
  locator: { number: "4.15.b4", headingPath: ["Benchmark standards", "Excellent level"] }
  span: { start: 66354, end: 66558 }
  source: "engage critically and comprehensively in appropriate independent research, whether investigating past or present performances or as part of the process of creating new or novel performance and/or insights"
  stem: "4.15"
  statementType: excellent
  rung: excellent
  force: should
  level: fheq:6
  appliesTo: "honours graduates in Performance at the excellent rung"
  addressee: learner
  verbs: ["engage"]
  about: "critical, comprehensive independent research towards new insight"
  themes: [none]
  domain: subject-skill
  award: ["bachelor's with honours"]
  gradeOf: { statement: qaa/dance-drama-and-performance-2024/4.12.b4, basis: inferred }
  paraphrase: "Should be able to carry out suitable independent research critically and comprehensively, into past or present performance or within the making of new or novel work or insight."
  quote: full   # the issuer's statement is in `source` (D-std-0014)
  audience: both
  subjects: inherited
- id: qaa/dance-drama-and-performance-2024/4.15.b5
  locator: { number: "4.15.b5", headingPath: ["Benchmark standards", "Excellent level"] }
  span: { start: 66561, end: 66731 }
  source: "identify and interpret through critical modes of investigation the cultural frameworks that surround performance events and their specific social and historical contexts."
  stem: "4.15"
  statementType: excellent
  rung: excellent
  force: should
  level: fheq:6
  appliesTo: "honours graduates in Performance at the excellent rung"
  addressee: learner
  verbs: ["identify", "interpret"]
  about: "critical investigation of cultural frameworks in context"
  themes: [none]
  domain: subject-skill
  award: ["bachelor's with honours"]
  gradeOf: { statement: qaa/dance-drama-and-performance-2024/4.12.b5, basis: inferred }
  paraphrase: "Should be able to identify and interpret, through critical investigation, the cultural frameworks around performance events and their particular social and historical settings."
  quote: full   # the issuer's statement is in `source` (D-std-0014)
  audience: both
  subjects: inherited
- id: qaa/dance-drama-and-performance-2024/4.16.b1
  locator: { number: "4.16.b1", headingPath: ["Benchmark standards", "Excellent level"] }
  span: { start: 66848, end: 67020 }
  source: "demonstrate sophisticated levels of creative and analytical skill in developing and constructing arguments, and the capacity to evaluate and present them in a range of ways"
  stem: "4.16"
  statementType: excellent
  rung: excellent
  force: should
  level: fheq:6
  appliesTo: "honours graduates in Performance at the excellent rung"
  addressee: learner
  verbs: ["demonstrate", "developing", "constructing", "evaluate", "present"]
  about: "sophisticated creative and analytical argument"
  themes: [none]
  domain: generic-skill
  award: ["bachelor's with honours"]
  gradeOf: { statement: qaa/dance-drama-and-performance-2024/4.13.b1, basis: inferred }
  paraphrase: "Should show sophisticated creative and analytical skill in developing and building arguments, and be able to judge and present them in different ways."
  quote: full   # the issuer's statement is in `source` (D-std-0014)
  audience: both
  subjects: inherited
- id: qaa/dance-drama-and-performance-2024/4.16.b2
  locator: { number: "4.16.b2", headingPath: ["Benchmark standards", "Excellent level"] }
  span: { start: 67023, end: 67181 }
  source: "demonstrate a developed critical capacity to examine and evaluate forms of discourse and their effects on representation in the arts, and culture more broadly"
  stem: "4.16"
  statementType: excellent
  rung: excellent
  force: should
  level: fheq:6
  appliesTo: "honours graduates in Performance at the excellent rung"
  addressee: learner
  verbs: ["demonstrate", "examine", "evaluate"]
  about: "critical analysis of discourse and representation"
  themes: [none]
  domain: generic-skill
  award: ["bachelor's with honours"]
  gradeOf: { statement: qaa/dance-drama-and-performance-2024/4.13.b2, basis: inferred }
  paraphrase: "Should show a developed critical ability to examine and evaluate kinds of discourse and how they shape representation in the arts and wider culture."
  quote: full   # the issuer's statement is in `source` (D-std-0014)
  audience: both
  subjects: inherited
- id: qaa/dance-drama-and-performance-2024/4.16.b3
  locator: { number: "4.16.b3", headingPath: ["Benchmark standards", "Excellent level"] }
  span: { start: 67184, end: 67242 }
  source: "work productively, creatively and imaginatively in a group"
  stem: "4.16"
  statementType: excellent
  rung: excellent
  force: should
  level: fheq:6
  appliesTo: "honours graduates in Performance at the excellent rung"
  addressee: learner
  verbs: ["work"]
  about: "productive, creative group work"
  themes: [none]
  domain: generic-skill
  award: ["bachelor's with honours"]
  gradeOf: { statement: qaa/dance-drama-and-performance-2024/4.13.b3, basis: inferred }
  paraphrase: "Should be able to work in a group productively, creatively and imaginatively."
  quote: full   # the issuer's statement is in `source` (D-std-0014)
  audience: both
  subjects: inherited
- id: qaa/dance-drama-and-performance-2024/4.16.b4
  locator: { number: "4.16.b4", headingPath: ["Benchmark standards", "Excellent level"] }
  span: { start: 67245, end: 67365 }
  source: "manage personal workloads efficiently and effectively, meet deadlines, and negotiate and pursue shared goals with others"
  stem: "4.16"
  statementType: excellent
  rung: excellent
  force: should
  level: fheq:6
  appliesTo: "honours graduates in Performance at the excellent rung"
  addressee: learner
  verbs: ["manage", "meet", "negotiate", "pursue"]
  about: "workload, deadlines and shared goals"
  themes: [none]
  domain: generic-skill
  award: ["bachelor's with honours"]
  gradeOf: { statement: qaa/dance-drama-and-performance-2024/4.13.b4, basis: inferred }
  paraphrase: "Should be able to manage their own workload efficiently and effectively, meet deadlines, and agree and pursue shared goals with others."
  quote: full   # the issuer's statement is in `source` (D-std-0014)
  audience: both
  subjects: inherited
- id: qaa/dance-drama-and-performance-2024/4.16.b5
  locator: { number: "4.16.b5", headingPath: ["Benchmark standards", "Excellent level"] }
  span: { start: 67368, end: 67459 }
  source: "constructively and effectively manage creative, artistic, personal and interpersonal issues"
  stem: "4.16"
  statementType: excellent
  rung: excellent
  force: should
  level: fheq:6
  appliesTo: "honours graduates in Performance at the excellent rung"
  addressee: learner
  verbs: ["manage"]
  about: "managing creative, artistic and interpersonal issues"
  themes: [none]
  domain: generic-skill
  award: ["bachelor's with honours"]
  gradeOf: { statement: qaa/dance-drama-and-performance-2024/4.13.b5, basis: inferred }
  paraphrase: "Should be able to manage creative, artistic, personal and interpersonal issues constructively and effectively."
  quote: full   # the issuer's statement is in `source` (D-std-0014)
  audience: both
  subjects: inherited
- id: qaa/dance-drama-and-performance-2024/4.16.b6
  locator: { number: "4.16.b6", headingPath: ["Benchmark standards", "Excellent level"] }
  span: { start: 67462, end: 67621 }
  source: "use discerning information retrieval skills needed to gather, sift, synthesise and organise material independently, and to critically evaluate its significance"
  stem: "4.16"
  statementType: excellent
  rung: excellent
  force: should
  level: fheq:6
  appliesTo: "honours graduates in Performance at the excellent rung"
  addressee: learner
  verbs: ["use", "gather", "sift", "synthesise", "organise", "evaluate"]
  about: "discerning information retrieval and synthesis"
  themes: [none]
  domain: generic-skill
  award: ["bachelor's with honours"]
  gradeOf: { statement: qaa/dance-drama-and-performance-2024/4.13.b6, basis: inferred }
  paraphrase: "Should be able to use discerning information retrieval skills to gather, sift, synthesise and organise material on their own and to judge its significance critically."
  quote: full   # the issuer's statement is in `source` (D-std-0014)
  audience: both
  subjects: inherited
- id: qaa/dance-drama-and-performance-2024/4.16.b7
  locator: { number: "4.16.b7", headingPath: ["Benchmark standards", "Excellent level"] }
  span: { start: 67624, end: 67732 }
  source: "demonstrate appropriate technological and digital skills, and be fully aware of their potential applications"
  stem: "4.16"
  statementType: excellent
  rung: excellent
  force: should
  level: fheq:6
  appliesTo: "honours graduates in Performance at the excellent rung"
  addressee: learner
  verbs: ["demonstrate", "be"]
  about: "digital skills and full awareness of their potential"
  themes: [none]
  domain: generic-skill
  award: ["bachelor's with honours"]
  gradeOf: { statement: qaa/dance-drama-and-performance-2024/4.13.b7, basis: inferred }
  paraphrase: "Should show suitable technical and digital skills and full awareness of what they could be used for."
  quote: full   # the issuer's statement is in `source` (D-std-0014)
  audience: both
  subjects: inherited
- id: qaa/dance-drama-and-performance-2024/4.16.b8
  locator: { number: "4.16.b8", headingPath: ["Benchmark standards", "Excellent level"] }
  span: { start: 67735, end: 67829 }
  source: "identify and deploy a range of numeracy skills to solve problems and realise creative outputs."
  stem: "4.16"
  statementType: excellent
  rung: excellent
  force: should
  level: fheq:6
  appliesTo: "honours graduates in Performance at the excellent rung"
  addressee: learner
  verbs: ["identify", "deploy", "solve", "realise"]
  about: "deploying numeracy for creative outputs"
  themes: [none]
  domain: generic-skill
  award: ["bachelor's with honours"]
  gradeOf: { statement: qaa/dance-drama-and-performance-2024/4.13.b8, basis: inferred }
  paraphrase: "Should be able to identify and use several numeracy skills to solve problems and achieve creative outputs."
  quote: full   # the issuer's statement is in `source` (D-std-0014)
  audience: both
  subjects: inherited
- id: qaa/dance-drama-and-performance-2024/4.17.b1
  locator: { number: "4.17.b1", headingPath: ["Benchmark standards", "Master's level degrees in Dance, Drama and Performance"] }
  span: { start: 68072, end: 68236 }
  source: "demonstrate a systematic and comprehensive understanding and critical awareness of current and emerging trends in Dance, Drama and Performance practice and research"
  stem: "4.17"
  statementType: outcome
  rung: none
  force: should
  level: fheq:7
  appliesTo: "master's students in Performance"
  addressee: learner
  verbs: ["demonstrate"]
  about: "systematic, critical grasp of current and emerging directions"
  themes: [none]
  domain: knowledge
  award: ["master's"]
  gradeOf: none
  paraphrase: "Should be able to show a systematic, thorough and critically aware grasp of where practice and research in the field now stand and where they are heading."
  quote: full   # the issuer's statement is in `source` (D-std-0014)
  audience: both
  subjects: inherited
- id: qaa/dance-drama-and-performance-2024/4.17.b2
  locator: { number: "4.17.b2", headingPath: ["Benchmark standards", "Master's level degrees in Dance, Drama and Performance"] }
  span: { start: 68239, end: 68353 }
  source: "evaluate current research and advanced scholarship to apply knowledge in original ways in the field of Performance"
  stem: "4.17"
  statementType: outcome
  rung: none
  force: should
  level: fheq:7
  appliesTo: "master's students in Performance"
  addressee: learner
  verbs: ["evaluate", "apply"]
  about: "evaluating research to apply knowledge originally"
  themes: [none]
  domain: understanding
  award: ["master's"]
  gradeOf: none
  paraphrase: "Should be able to evaluate current research and advanced scholarship and use what they know in original ways in the field."
  quote: full   # the issuer's statement is in `source` (D-std-0014)
  audience: both
  subjects: inherited
- id: qaa/dance-drama-and-performance-2024/4.17.b3
  locator: { number: "4.17.b3", headingPath: ["Benchmark standards", "Master's level degrees in Dance, Drama and Performance"] }
  span: { start: 68356, end: 68510 }
  source: "evaluate appropriate methodologies and demonstrate self-direction and originality in dealing with complex problems in Performance practice and/or research"
  stem: "4.17"
  statementType: outcome
  rung: none
  force: should
  level: fheq:7
  appliesTo: "master's students in Performance"
  addressee: learner
  verbs: ["evaluate", "demonstrate", "dealing"]
  about: "method, self-direction and originality with complex problems"
  themes: [none]
  domain: generic-skill
  award: ["master's"]
  gradeOf: none
  paraphrase: "Should be able to evaluate suitable methods and show self-direction and originality in tackling complex problems in practice or research."
  quote: full   # the issuer's statement is in `source` (D-std-0014)
  audience: both
  subjects: inherited
- id: qaa/dance-drama-and-performance-2024/4.17.b4
  locator: { number: "4.17.b4", headingPath: ["Benchmark standards", "Master's level degrees in Dance, Drama and Performance"] }
  span: { start: 68513, end: 68635 }
  source: "create new insight in their field of study, and communicate conclusions clearly to specialist and non-specialist audiences"
  stem: "4.17"
  statementType: outcome
  rung: none
  force: should
  level: fheq:7
  appliesTo: "master's students in Performance"
  addressee: learner
  verbs: ["create", "communicate"]
  about: "new insight communicated to all audiences"
  themes: [none]
  domain: generic-skill
  award: ["master's"]
  gradeOf: none
  paraphrase: "Should be able to create new insight in their field and communicate conclusions clearly to specialists and non-specialists."
  quote: full   # the issuer's statement is in `source` (D-std-0014)
  audience: both
  subjects: inherited
- id: qaa/dance-drama-and-performance-2024/4.17.b5
  locator: { number: "4.17.b5", headingPath: ["Benchmark standards", "Master's level degrees in Dance, Drama and Performance"] }
  span: { start: 68638, end: 68764 }
  source: "complete of a major piece of practice, or substantial research project, informed by thorough understandings of the discipline."
  stem: "4.17"
  statementType: outcome
  rung: none
  force: should
  level: fheq:7
  appliesTo: "master's students in Performance"
  addressee: learner
  verbs: ["complete"]
  about: "a major practice or research project"
  themes: [none]
  domain: subject-skill
  award: ["master's"]
  gradeOf: none
  paraphrase: "Should be able to complete a major piece of practice or a substantial research project, grounded in a thorough understanding of the discipline."
  quote: full   # the issuer's statement is in `source` (D-std-0014)
  audience: both
  subjects: inherited
```

### S4a Audience versions
<!-- label: both; status: drafted; basis: primary. forPractitioner: for the programme designer or teacher. forBeneficiary: for the student, second person, naming no issuer. author-agent-written: instructions to an AI agent writing about the statement (a course document, a handbook, an outcome, a report). author-agent-dialogue: instructions to an AI agent using the statement in conversation (with a student, a teacher or a programme team). Written fresh from the held text alone (benchmark rule 6; Abbott, 15:42). -->
```yaml
- statement: qaa/dance-drama-and-performance-2024/1.17
  forPractitioner: { text: "Check course structures, assessment and timetabling so that no student is disadvantaged by design because of who they are; the statement says this should not happen.", rewrite: light, force: should, status: drafted }
  forBeneficiary: { text: "Your course should not be set up in a way that puts you at a disadvantage because of who you are.", rewrite: full, force: should, status: drafted }
  author-agent-written: "Describe this as an expectation (should) on courses in the subject at every level of study, set within its equality, diversity and inclusion section. Cite it as (QAA, 2024, Dance, Drama and Performance Subject Benchmark Statement, para 1.17) and read it with paras 1.18 to 1.20 and the Equality Act 2010 the paragraph names. Do not claim it creates a legal duty of its own; the legal duties come from the Act."
  author-agent-dialogue: "Raise it when a student reports a barrier built into how the course runs, or when a team reviews a module for inclusion. With a student, ask where the course's set-up has made things harder for them than for others; with staff, ask which structures could disadvantage a group by design. Avoid promising a fix the course team has not agreed."
- statement: qaa/dance-drama-and-performance-2024/1.24
  forPractitioner: { text: "Shape teaching methods around your student body and the professional practice of the discipline: the curriculum will put access and equity first, backed by suitable learning resources.", rewrite: light, force: will, status: drafted }
  forBeneficiary: { text: "not-applicable: a duty on those who design and teach courses; it sets no outcome for the student", rewrite: full, force: will, status: drafted }
  author-agent-written: "Present this as a stated expectation (will, generally) on teaching in the subject, in its accessibility section, not as an outcome for students. Cite it as (QAA, 2024, Dance, Drama and Performance Subject Benchmark Statement, para 1.24) and set it beside paras 1.21 to 1.30 and the inclusion commitment in para 3.6. Do not claim it fixes a teaching method; it asks that methods answer to students' needs and to professional practice."
  author-agent-dialogue: "Raise it with a programme team planning teaching methods or resources. Ask which students' access needs the current methods serve poorly, and what resources are missing. Keep the duty with staff; do not hand it to a student as something to meet."
- statement: qaa/dance-drama-and-performance-2024/2.6
  forPractitioner: { text: "Build national and international performing arts work into the course: its contexts, industries, practitioners and developments will shape what is taught.", rewrite: light, force: will, status: drafted }
  forBeneficiary: { text: "Your course will connect you with how the performing arts work in the UK and around the world: their industries, people and practices.", rewrite: full, force: will, status: drafted }
  author-agent-written: "Describe this as a stated expectation (will) on courses in the subject: that they engage with national and international performing arts. Cite it as (QAA, 2024, Dance, Drama and Performance Subject Benchmark Statement, para 2.6) and set it beside the partnership paragraphs 2.14 to 2.20 and para 1.10. Do not claim it requires international travel or placements; it names contexts to engage with, not activities."
  author-agent-dialogue: "Raise it when a team reviews whether the curriculum looks beyond one national tradition, or a student asks how the course links to the profession. Ask staff which international practices or industries the course draws on now; ask a student which work from outside the UK has shaped their own. Avoid treating it as a student requirement."
- statement: qaa/dance-drama-and-performance-2024/2.8
  forPractitioner: { text: "Plan each level so that it adds knowledge, expertise and experience leading towards the threshold skills in paras 4.8 to 4.10; progression will follow your institution's regulations and usually means credit for the full range of study.", rewrite: light, force: will, status: drafted }
  forBeneficiary: { text: "You will move from one year of study to the next under your university's rules, and each year is expected to build what you know and can do towards the minimum standard for your degree.", rewrite: full, force: will, status: drafted }
  author-agent-written: "State it as an expectation (will; it is expected) on progression towards the honours award at FHEQ level 6: each level builds towards the threshold. Cite it as (QAA, 2024, Dance, Drama and Performance Subject Benchmark Statement, para 2.8) and set it beside the threshold rung in paras 4.8 to 4.10 and the lower-level descriptors from qaa/fheq-2024/4.10.b1 and qaa/fheq-2024/4.12.b1 (FHEQ 4 and 5). Do not claim the statement sets progression rules; each institution's regulations do."
  author-agent-dialogue: "Raise it when a student asks how a first or second year relates to the final standard, or when staff map outcomes across levels. Ask a student what this year has added towards the final-year standard; ask staff where each level's outcomes point to the threshold items. Avoid suggesting the statement decides who progresses."
- statement: qaa/dance-drama-and-performance-2024/2.9
  forPractitioner: { text: "Prepare students so that those graduating with a second-class degree or better will be ready for postgraduate study in the field or a related one, while noting that entry criteria belong to each institution.", rewrite: light, force: will, status: drafted }
  forBeneficiary: { text: "If you graduate with a second-class degree or above, you will be ready to take on postgraduate study in this or a related field, though each institution sets its own entry rules.", rewrite: full, force: will, status: drafted }
  author-agent-written: "Present this as a stated expectation (will; it is expected) about honours graduates with a second-class degree or higher at FHEQ level 6: readiness for postgraduate study. Cite it as (QAA, 2024, Dance, Drama and Performance Subject Benchmark Statement, para 2.9) and set it beside the master's outcomes in para 4.17 and qaa/fheq-2024/4.15.b9.3. Do not claim it guarantees entry to a master's course; the paragraph leaves entry to each institution."
  author-agent-dialogue: "Bring it up when a student asks whether they could go on to a master's. Ask what result they are on course for and which postgraduate area interests them. Avoid promising admission; point them to each institution's entry requirements."
- statement: qaa/dance-drama-and-performance-2024/2.10
  forPractitioner: { text: "For joint or combined students, make sure the core subject-specific and generic skills are covered; they will add others from their second subject and may work across both.", rewrite: light, force: will, status: drafted }
  forBeneficiary: { text: "If you take this subject as part of a joint or combined degree, you will gain its core skills and add others from your other subject, with room to explore where the two meet.", rewrite: full, force: will, status: drafted }
  author-agent-written: "Describe this as a stated expectation (will) for joint and combined honours students at FHEQ level 6: the core of the subject's skills, not all of them. Cite it as (QAA, 2024, Dance, Drama and Performance Subject Benchmark Statement, para 2.10) and set it beside the skills rungs in paras 4.9 and 4.10 and para 3.5 on students for whom Performance is not the main subject. Do not claim joint students meet every single-honours outcome; para 4.7 says the standards are written for single honours."
  author-agent-dialogue: "Raise it when a joint honours student worries they cannot cover everything a single honours student does, or when a team plans a combined route. Ask which core skills the route secures and what the other subject adds. Avoid presenting the single honours list as a checklist for joint students."
- statement: qaa/dance-drama-and-performance-2024/2.23
  forPractitioner: { text: "In periodic review, use external reviewers: they will give an outside view of planned changes and confirm that threshold standards are met and content fits the subject.", rewrite: light, force: will, status: drafted }
  forBeneficiary: { text: "not-applicable: a duty on the institution in periodic review; it sets no outcome for the student", rewrite: full, force: will, status: drafted }
  author-agent-written: "Describe this as a stated expectation (will) on institutions in periodic review, not an outcome for students. Cite it as (QAA, 2024, Dance, Drama and Performance Subject Benchmark Statement, para 2.23) and set it beside paras 2.22 and 2.24 on monitoring and external examining. Do not claim the statement prescribes how review is run; it asks only that external reviewers take part."
  author-agent-dialogue: "Raise it with a programme team preparing for periodic review. Ask who will act as external reviewer and what they will be asked to judge against the threshold standards. Keep it for staff."
- statement: qaa/dance-drama-and-performance-2024/2.24
  forPractitioner: { text: "Expect a yearly report from each external examiner, with recommendations on modules and assessment where they see the need, and plan how the course will respond.", rewrite: light, force: must, status: drafted }
  forBeneficiary: { text: "not-applicable: a requirement on external examiners and the institution; it sets no outcome for the student", rewrite: full, force: must, status: drafted }
  author-agent-written: "Present this as a requirement (required; recorded as must) on external examiners within UK external examining, not a standard students meet. Cite it as (QAA, 2024, Dance, Drama and Performance Subject Benchmark Statement, para 2.24) and set it beside para 2.23 on external review and para 4.3 on threshold standards. Do not claim the statement itself creates the requirement; it describes the sector's external examiner system."
  author-agent-dialogue: "Raise it with a programme team reading or answering an external examiner's report. Ask which recommendations from the last report have been acted on and which were set aside, and why. Do not raise it with students as something they must do."
- statement: qaa/dance-drama-and-performance-2024/3.1
  forPractitioner: { text: "Choose several of the content areas and skills from 3.2 and 3.3 and make some of them the course's defining features; courses will typically differ in balance.", rewrite: light, force: will, status: drafted }
  forBeneficiary: { text: "not-applicable: about how course teams select content; it sets no outcome for the student", rewrite: full, force: will, status: drafted }
  author-agent-written: "Describe this as a typical expectation (will, typically) on honours course content, not a required list. Cite it as (QAA, 2024, Dance, Drama and Performance Subject Benchmark Statement, para 3.1) and set it beside the areas in para 3.2 and the skills in paras 3.3.b1 to 3.3.b13. Do not claim a course must cover every area; the same paragraph rules out a prescriptive model."
  author-agent-dialogue: "Raise it when a team asks how much of the subject's range a course must cover. Ask which areas the course makes its distinguishing features and why. Keep it with staff."
- statement: qaa/dance-drama-and-performance-2024/3.3.b1
  forPractitioner: { text: "Give students performance and production work built on the field's vocabularies, skills, structures and research approaches.", rewrite: light, force: will, status: drafted }
  forBeneficiary: { text: "You will take part in performing and producing work, built on learning the vocabularies, skills and methods of your field.", rewrite: full, force: will, status: drafted }
  author-agent-written: "Describe this as an outcome students will reach (will) on honours courses in the subject at FHEQ level 6 (FQHEIS level 10), from the skills list in para 3.3, whose stem asks courses to enable these skills and to go deep in some. Cite it as (QAA, 2024, Dance, Drama and Performance Subject Benchmark Statement, para 3.3.b1). Set it beside the rung item 4.9.b1, the honours descriptor qaa/fheq-2024/4.15.b2 and spine:6. Do not claim every course develops every item to the same depth."
  author-agent-dialogue: "Raise it when a student asks what skills the course builds, or staff map modules to the subject's skills. Put it in plain words; for staff, ask which module develops it in depth. Ask a student: Which performance or production methods can you now use without being shown? Avoid reading the whole list aloud."
- statement: qaa/dance-drama-and-performance-2024/3.3.b2
  forPractitioner: { text: "Teach techniques in relation to the cultural forms, histories and practitioners they come from.", rewrite: light, force: will, status: drafted }
  forBeneficiary: { text: "You will develop techniques that come from, or are shaped by, particular cultures, histories or practitioners.", rewrite: full, force: will, status: drafted }
  author-agent-written: "Describe this as an outcome students will reach (will) on honours courses in the subject at FHEQ level 6 (FQHEIS level 10), from the skills list in para 3.3, whose stem asks courses to enable these skills and to go deep in some. Cite it as (QAA, 2024, Dance, Drama and Performance Subject Benchmark Statement, para 3.3.b2). Set it beside the rung item 4.9.b1, the honours descriptor qaa/fheq-2024/4.15.b2 and spine:6. Do not claim every course develops every item to the same depth."
  author-agent-dialogue: "Raise it when a student asks what skills the course builds, or staff map modules to the subject's skills. Put it in plain words; for staff, ask which module develops it in depth. Ask a student: Which tradition or practitioner has shaped your technique most, and how? Avoid reading the whole list aloud."
- statement: qaa/dance-drama-and-performance-2024/3.3.b3
  forPractitioner: { text: "Give students ownership of project management and creative decisions, individually and in groups.", rewrite: light, force: will, status: drafted }
  forBeneficiary: { text: "You will take charge of managing projects and making creative decisions, on your own or in a group.", rewrite: full, force: will, status: drafted }
  author-agent-written: "Describe this as an outcome students will reach (will) on honours courses in the subject at FHEQ level 6 (FQHEIS level 10), from the skills list in para 3.3, whose stem asks courses to enable these skills and to go deep in some. Cite it as (QAA, 2024, Dance, Drama and Performance Subject Benchmark Statement, para 3.3.b3). Set it beside the rung item 4.10.b10, the honours descriptor qaa/fheq-2024/4.15.b9.1 and spine:6. Do not claim every course develops every item to the same depth."
  author-agent-dialogue: "Raise it when a student asks what skills the course builds, or staff map modules to the subject's skills. Put it in plain words; for staff, ask which module develops it in depth. Ask a student: When did you last make a creative decision that the group then followed? Avoid reading the whole list aloud."
- statement: qaa/dance-drama-and-performance-2024/3.3.b4
  forPractitioner: { text: "Ask students to analyse performance texts and events from more than one perspective in the subject's terms.", rewrite: light, force: will, status: drafted }
  forBeneficiary: { text: "You will describe, theorise, interpret and judge performance texts and events from different points of view, using the subject's language.", rewrite: full, force: will, status: drafted }
  author-agent-written: "Describe this as an outcome students will reach (will) on honours courses in the subject at FHEQ level 6 (FQHEIS level 10), from the skills list in para 3.3, whose stem asks courses to enable these skills and to go deep in some. Cite it as (QAA, 2024, Dance, Drama and Performance Subject Benchmark Statement, para 3.3.b4). Set it beside the rung item 4.9.b4, the honours descriptor qaa/fheq-2024/4.15.b7 and spine:6. Do not claim every course develops every item to the same depth."
  author-agent-dialogue: "Raise it when a student asks what skills the course builds, or staff map modules to the subject's skills. Put it in plain words; for staff, ask which module develops it in depth. Ask a student: Which perspective do you reach for first when you analyse a performance, and which do you neglect? Avoid reading the whole list aloud."
- statement: qaa/dance-drama-and-performance-2024/3.3.b5
  forPractitioner: { text: "Include work with archives and historical sources.", rewrite: light, force: will, status: drafted }
  forBeneficiary: { text: "You will find and analyse historical sources.", rewrite: full, force: will, status: drafted }
  author-agent-written: "Describe this as an outcome students will reach (will) on honours courses in the subject at FHEQ level 6 (FQHEIS level 10), from the skills list in para 3.3, whose stem asks courses to enable these skills and to go deep in some. Cite it as (QAA, 2024, Dance, Drama and Performance Subject Benchmark Statement, para 3.3.b5). Set it beside the rung item 4.9.b5, the honours descriptor qaa/fheq-2024/4.15.b5 and spine:6. Do not claim every course develops every item to the same depth."
  author-agent-dialogue: "Raise it when a student asks what skills the course builds, or staff map modules to the subject's skills. Put it in plain words; for staff, ask which module develops it in depth. Ask a student: Which historical source have you worked with directly, not through someone else's account? Avoid reading the whole list aloud."
- statement: qaa/dance-drama-and-performance-2024/3.3.b6
  forPractitioner: { text: "Set analysis of performance's part in social, cultural and political debate, then and now.", rewrite: light, force: will, status: drafted }
  forBeneficiary: { text: "You will analyse what performance does in social, cultural and political debate, past and present.", rewrite: full, force: will, status: drafted }
  author-agent-written: "Describe this as an outcome students will reach (will) on honours courses in the subject at FHEQ level 6 (FQHEIS level 10), from the skills list in para 3.3, whose stem asks courses to enable these skills and to go deep in some. Cite it as (QAA, 2024, Dance, Drama and Performance Subject Benchmark Statement, para 3.3.b6). Set it beside the rung item 4.8.b5, the honours descriptor qaa/fheq-2024/4.15.b1 and spine:6. Do not claim every course develops every item to the same depth."
  author-agent-dialogue: "Raise it when a student asks what skills the course builds, or staff map modules to the subject's skills. Put it in plain words; for staff, ask which module develops it in depth. Ask a student: Can you name a performance that changed a public conversation, and explain how? Avoid reading the whole list aloud."
- statement: qaa/dance-drama-and-performance-2024/3.3.b7
  forPractitioner: { text: "Offer participatory projects that students plan, facilitate, deliver and evaluate in community, educational or social settings.", rewrite: light, force: will, status: drafted }
  forBeneficiary: { text: "You will plan, lead, run and evaluate projects that use participatory performance in community, educational and social settings.", rewrite: full, force: will, status: drafted }
  author-agent-written: "Describe this as an outcome students will reach (will) on honours courses in the subject at FHEQ level 6 (FQHEIS level 10), from the skills list in para 3.3, whose stem asks courses to enable these skills and to go deep in some. Cite it as (QAA, 2024, Dance, Drama and Performance Subject Benchmark Statement, para 3.3.b7). Set it beside the rung item 4.8.b5, the honours descriptor qaa/fheq-2024/4.15.b6 and spine:6. Do not claim every course develops every item to the same depth."
  author-agent-dialogue: "Raise it when a student asks what skills the course builds, or staff map modules to the subject's skills. Put it in plain words; for staff, ask which module develops it in depth. Ask a student: What would you change after evaluating the last participatory session you led? Avoid reading the whole list aloud."
- statement: qaa/dance-drama-and-performance-2024/3.3.b8
  forPractitioner: { text: "Make the ethics of performance an explicit topic and a part of practical work.", rewrite: light, force: will, status: drafted }
  forBeneficiary: { text: "You will deal with the ethical questions that performance raises.", rewrite: full, force: will, status: drafted }
  author-agent-written: "Describe this as an outcome students will reach (will) on honours courses in the subject at FHEQ level 6 (FQHEIS level 10), from the skills list in para 3.3, whose stem asks courses to enable these skills and to go deep in some. Cite it as (QAA, 2024, Dance, Drama and Performance Subject Benchmark Statement, para 3.3.b8). Set it beside the rung item 4.10.b3, the honours descriptor qaa/fheq-2024/4.15.b4 and spine:6. Do not claim every course develops every item to the same depth."
  author-agent-dialogue: "Raise it when a student asks what skills the course builds, or staff map modules to the subject's skills. Put it in plain words; for staff, ask which module develops it in depth. Ask a student: What ethical question did your last project raise, and how did you handle it? Avoid reading the whole list aloud."
- statement: qaa/dance-drama-and-performance-2024/3.3.b9
  forPractitioner: { text: "Set tasks that call for research, independent judgement and reasoned argument.", rewrite: light, force: will, status: drafted }
  forBeneficiary: { text: "You will research and evaluate information, reach your own judgements and make reasoned arguments.", rewrite: full, force: will, status: drafted }
  author-agent-written: "Describe this as an outcome students will reach (will) on honours courses in the subject at FHEQ level 6 (FQHEIS level 10), from the skills list in para 3.3, whose stem asks courses to enable these skills and to go deep in some. Cite it as (QAA, 2024, Dance, Drama and Performance Subject Benchmark Statement, para 3.3.b9). Set it beside the rung item 4.10.b4, the honours descriptor qaa/fheq-2024/4.15.b3.1 and spine:6. Do not claim every course develops every item to the same depth."
  author-agent-dialogue: "Raise it when a student asks what skills the course builds, or staff map modules to the subject's skills. Put it in plain words; for staff, ask which module develops it in depth. Ask a student: Where in your last essay or project did you reach a judgement of your own? Avoid reading the whole list aloud."
- statement: qaa/dance-drama-and-performance-2024/3.3.b10
  forPractitioner: { text: "Build collaboration into intellectual, creative and professional tasks, with shared goals.", rewrite: light, force: will, status: drafted }
  forBeneficiary: { text: "You will work with others in academic, creative and professional settings to set and reach shared goals.", rewrite: full, force: will, status: drafted }
  author-agent-written: "Describe this as an outcome students will reach (will) on honours courses in the subject at FHEQ level 6 (FQHEIS level 10), from the skills list in para 3.3, whose stem asks courses to enable these skills and to go deep in some. Cite it as (QAA, 2024, Dance, Drama and Performance Subject Benchmark Statement, para 3.3.b10). Set it beside the rung item 4.10.b5, the honours descriptor qaa/fheq-2024/4.15.b9.1 and spine:6. Do not claim every course develops every item to the same depth."
  author-agent-dialogue: "Raise it when a student asks what skills the course builds, or staff map modules to the subject's skills. Put it in plain words; for staff, ask which module develops it in depth. Ask a student: How did your group agree its goals on the last shared project? Avoid reading the whole list aloud."
- statement: qaa/dance-drama-and-performance-2024/3.3.b11
  forPractitioner: { text: "Create space where students engage respectfully with different views, experiences and traditions.", rewrite: light, force: will, status: drafted }
  forBeneficiary: { text: "You will consider, recognise and respect different opinions, experiences and performance traditions.", rewrite: full, force: will, status: drafted }
  author-agent-written: "Describe this as an outcome students will reach (will) on honours courses in the subject at FHEQ level 6 (FQHEIS level 10), from the skills list in para 3.3, whose stem asks courses to enable these skills and to go deep in some. Cite it as (QAA, 2024, Dance, Drama and Performance Subject Benchmark Statement, para 3.3.b11). Set it beside the rung item 4.10.b2, the honours descriptor qaa/fheq-2024/4.15.b9.1 and spine:6. Do not claim every course develops every item to the same depth."
  author-agent-dialogue: "Raise it when a student asks what skills the course builds, or staff map modules to the subject's skills. Put it in plain words; for staff, ask which module develops it in depth. Ask a student: Which tradition unlike your own have you learned most from? Avoid reading the whole list aloud."
- statement: qaa/dance-drama-and-performance-2024/3.3.b12
  forPractitioner: { text: "Teach and assess writing in both scholarly and professional registers.", rewrite: light, force: will, status: drafted }
  forBeneficiary: { text: "You will write in the right academic and professional styles for the task.", rewrite: full, force: will, status: drafted }
  author-agent-written: "Describe this as an outcome students will reach (will) on honours courses in the subject at FHEQ level 6 (FQHEIS level 10), from the skills list in para 3.3, whose stem asks courses to enable these skills and to go deep in some. Cite it as (QAA, 2024, Dance, Drama and Performance Subject Benchmark Statement, para 3.3.b12). Set it beside the rung item 4.10.b7, the honours descriptor qaa/fheq-2024/4.15.b8 and spine:6. Do not claim every course develops every item to the same depth."
  author-agent-dialogue: "Raise it when a student asks what skills the course builds, or staff map modules to the subject's skills. Put it in plain words; for staff, ask which module develops it in depth. Ask a student: Which kind of writing for the profession have you practised, beyond essays? Avoid reading the whole list aloud."
- statement: qaa/dance-drama-and-performance-2024/3.3.b13
  forPractitioner: { text: "Assess presentation in several forms, fitted to content, audience and setting.", rewrite: light, force: will, status: drafted }
  forBeneficiary: { text: "You will present information in different forms to suit the content, the audience and the setting.", rewrite: full, force: will, status: drafted }
  author-agent-written: "Describe this as an outcome students will reach (will) on honours courses in the subject at FHEQ level 6 (FQHEIS level 10), from the skills list in para 3.3, whose stem asks courses to enable these skills and to go deep in some. Cite it as (QAA, 2024, Dance, Drama and Performance Subject Benchmark Statement, para 3.3.b13). Set it beside the rung item 4.10.b7, the honours descriptor qaa/fheq-2024/4.15.b8 and spine:6. Do not claim every course develops every item to the same depth."
  author-agent-dialogue: "Raise it when a student asks what skills the course builds, or staff map modules to the subject's skills. Put it in plain words; for staff, ask which module develops it in depth. Ask a student: How did you change a presentation for a different audience? Avoid reading the whole list aloud."
- statement: qaa/dance-drama-and-performance-2024/3.4
  forPractitioner: { text: "Hold students on Performance modules to the same outcomes whatever their course: single, joint, combined, major-minor or general.", rewrite: light, force: describes, status: drafted }
  forBeneficiary: { text: "Whatever course you are on, if you take Performance modules you are held to the same learning outcomes as everyone else on them.", rewrite: full, force: describes, status: drafted }
  author-agent-written: "Describe this as a stated expectation (are expected; recorded as describes, an obliging word outside the five) that students on Performance modules meet the same outcomes whatever their course, at honours level. Cite it as (QAA, 2024, Dance, Drama and Performance Subject Benchmark Statement, para 3.4) and read it with para 3.5, which allows less depth where specialist modules are closed to non-specialists. Do not claim non-specialist students must reach single honours depth across the whole subject."
  author-agent-dialogue: "Raise it when a student from another subject asks whether a Performance module will be marked differently for them, or when staff set outcomes for an elective. Ask the student which module outcomes they find hardest coming from their own subject. Avoid suggesting easier outcomes for visiting students; the outcomes are the same."
- statement: qaa/dance-drama-and-performance-2024/3.5
  forPractitioner: { text: "Plan for every Performance student, specialist or not, to build subject knowledge or skill and grow personally and intellectually; a final-year capstone is common, and depth may differ for students whose main subject lies elsewhere.", rewrite: light, force: will, status: drafted }
  forBeneficiary: { text: "However you study Performance, you will build knowledge or skills in it and grow personally, socially and intellectually, often finishing with a major final-year project.", rewrite: full, force: will, status: drafted }
  author-agent-written: "Present this as a stated expectation (will) for all students studying Performance at honours level, with the depth expected of non-specialists left lower. Cite it as (QAA, 2024, Dance, Drama and Performance Subject Benchmark Statement, para 3.5) and set it beside paras 3.4 and 2.10 and the honours descriptor qaa/fheq-2024/4.15.b6 on projects. Do not claim a capstone project is required; the paragraph says courses often have one."
  author-agent-dialogue: "Raise it when a student asks how their learning should grow over the course, or whether a final project is expected. Ask what has changed in how they think and work since their first year. Avoid presenting the capstone as compulsory."
- statement: qaa/dance-drama-and-performance-2024/3.6
  forPractitioner: { text: "Build diversity, inclusion and access into teaching, learning and assessment, and design in the flexibility needed to make reasonable adjustments for individual learning needs.", rewrite: light, force: will, status: drafted }
  forBeneficiary: { text: "Your teaching and assessment will be built on a commitment to diversity, inclusion and access, with room to make reasonable adjustments for your learning needs.", rewrite: full, force: will, status: drafted }
  author-agent-written: "Describe this as a stated expectation (will) on teaching, learning and assessment in courses in the subject. Cite it as (QAA, 2024, Dance, Drama and Performance Subject Benchmark Statement, para 3.6) and set it beside the equality and accessibility sections in paras 1.17 to 1.30 and the inclusive assessment in para 3.13. Do not claim the statement sets out the legal duty to make reasonable adjustments; it asks for flexibility to make them."
  author-agent-dialogue: "Raise it when a student asks whether an assessment can be adjusted for them, or when a team designs a new module. Ask a student what adjustment would let them show what they can do; ask staff where the module's design already allows adjustment. Avoid promising a particular adjustment, which the institution decides."
- statement: qaa/dance-drama-and-performance-2024/3.9
  forPractitioner: { text: "Choose teaching and learning activities from the working methods of the disciplines you teach: dance, drama, theatre and related practice.", rewrite: light, force: will, status: drafted }
  forBeneficiary: { text: "not-applicable: a duty on those who design teaching; it sets no outcome for the student", rewrite: full, force: will, status: drafted }
  author-agent-written: "Describe this as a stated expectation (will) on how teaching and learning are designed in courses in the subject. Cite it as (QAA, 2024, Dance, Drama and Performance Subject Benchmark Statement, para 3.9) and set it beside paras 3.7, 3.8 and 3.12. Do not claim it names required methods; it ties methods to the disciplines' own practice."
  author-agent-dialogue: "Raise it when a team plans teaching for a new module. Ask staff which disciplinary practices their sessions borrow from and which they leave out. Keep the duty with staff."
- statement: qaa/dance-drama-and-performance-2024/3.10
  forPractitioner: { text: "Give students learning in or near practical and professional settings, where they will take varied roles across the whole process from research to performance.", rewrite: light, force: will, status: drafted }
  forBeneficiary: { text: "You will usually learn in practical and professional settings, take on different roles and work through the whole process from early research to rehearsal, production and performance.", rewrite: full, force: will, status: drafted }
  author-agent-written: "Present this as a stated expectation (will, usually) about students' learning on honours courses in the subject. Cite it as (QAA, 2024, Dance, Drama and Performance Subject Benchmark Statement, para 3.10) and set it beside the subject skill rung items 4.9.b1 and 4.9.b2 and the honours descriptor qaa/fheq-2024/4.15.b6. Do not claim every student takes every role; the roles fit the student's subject area."
  author-agent-dialogue: "Raise it when a student asks what kinds of role they will take on, or staff plan production work. Ask a student which roles they have tried and which they want next. Avoid implying all roles are required of everyone."
- statement: qaa/dance-drama-and-performance-2024/3.11
  forPractitioner: { text: "Mix tutor-led and self-directed learning and shift the balance towards independence as students move up the levels; group work is a typical part of the course.", rewrite: light, force: will, status: drafted }
  forBeneficiary: { text: "You will usually learn both with tutors and on your own, becoming more independent as you go, and you will often work in groups.", rewrite: full, force: will, status: drafted }
  author-agent-written: "Describe this as a typical expectation (will, typically) on learning methods across the levels of an honours course in the subject. Cite it as (QAA, 2024, Dance, Drama and Performance Subject Benchmark Statement, para 3.11) and set it beside qaa/fheq-2024/4.15.b5 on managing one's own learning and spine:6 (strand:autonomy). Do not claim a fixed balance of tutor-led and independent study."
  author-agent-dialogue: "Raise it when a student finds the move to independent work hard, or staff plan how support tapers off. Ask a student which parts of their work they now lead themselves. Avoid treating less contact time as less support."
- statement: qaa/dance-drama-and-performance-2024/3.12
  forPractitioner: { text: "Offer a suitable mix of settings, in person and online: workshops, rehearsals, productions, studio and practical classes, screenings, lectures, seminars and tutorials.", rewrite: light, force: will, status: drafted }
  forBeneficiary: { text: "not-applicable: a duty on those who plan teaching; it sets no outcome for the student", rewrite: full, force: will, status: drafted }
  author-agent-written: "Present this as a normal expectation (will, normally) on the settings of teaching on courses in the subject. Cite it as (QAA, 2024, Dance, Drama and Performance Subject Benchmark Statement, para 3.12) and read it with the modes of learning listed after it in the same paragraph, which are typical rather than required. Do not claim every listed setting must appear in every course."
  author-agent-dialogue: "Raise it when staff balance in-person and online sessions or plan a timetable. Ask whether the current mix suits the practical work the module asks for. Keep it with staff."
- statement: qaa/dance-drama-and-performance-2024/3.15
  forPractitioner: { text: "Build in self- and peer-assessment tasks that support learning, with clear guidance on how they work.", rewrite: light, force: should, status: drafted }
  forBeneficiary: { text: "You should get chances to assess your own work and your classmates' work, to help you learn.", rewrite: full, force: should, status: drafted }
  author-agent-written: "Describe this as an expectation (should) on assessment design in courses in the subject. Cite it as (QAA, 2024, Dance, Drama and Performance Subject Benchmark Statement, para 3.15) and set it beside paras 3.13 and 3.14 on inclusive and varied assessment and Annex D's reflection row qaa/fheq-2024/annex-d/transferable/r5/3rd. Do not claim self or peer assessment must count towards marks; the paragraph ties it to learning."
  author-agent-dialogue: "Raise it when a student asks why they are asked to judge a peer's work, or a team designs formative tasks. Ask a student what they learned about their own work from judging someone else's. Avoid presenting peer marks as final grades."
- statement: qaa/dance-drama-and-performance-2024/3.16
  forPractitioner: { text: "Add to the course information how feedback works, what academic and pastoral tutoring is offered, what online resources exist and how to reach them, and reading and screening lists.", rewrite: light, force: should, status: drafted }
  forBeneficiary: { text: "not-applicable: a duty on the course team in writing course information", rewrite: full, force: should, status: drafted }
  author-agent-written: "Present this as an expectation (should) on the course information given to students in the subject. Cite it as (QAA, 2024, Dance, Drama and Performance Subject Benchmark Statement, para 3.16) and read it with the list of course information in para 3.15. Do not claim it fixes a format or a document; the information may be online or in print."
  author-agent-dialogue: "Raise it with a team writing or revising a handbook. Ask where a student would find feedback timings, tutorial support and reading lists today. Keep it with staff."
- statement: qaa/dance-drama-and-performance-2024/4.2
  forPractitioner: { text: "Read the three rungs as what students will have shown at award: minimum, typical and excellent; design assessment so that students show them over time, not in a single task.", rewrite: light, force: will, status: drafted }
  forBeneficiary: { text: "When you are awarded your honours degree, you will have shown at least the minimum standard, and showing these standards over time shows the range of what you know and can do.", rewrite: full, force: will, status: drafted }
  author-agent-written: "Describe this as the statement's own frame for its rungs: threshold, typical and excellent standards that students will have shown at the award of an honours degree, FHEQ level 6 (FQHEIS level 10). Cite it as (QAA, 2024, Dance, Drama and Performance Subject Benchmark Statement, para 4.2) and set it beside the rung lead-ins 4.8, 4.11 and 4.14 and qaa/fheq-2024/4.15.b1. Do not claim that every student reaches the excellent standard."
  author-agent-dialogue: "Raise it when a student asks what the degree expects of them overall. Ask which of the three standards they are aiming for in their strongest area. Never present the typical or excellent standard as the minimum."
- statement: qaa/dance-drama-and-performance-2024/4.3
  forPractitioner: { text: "When setting what counts as evidence of achievement, refer to Annex D's descriptions of the four honours classes, expecting most students to perform well above the threshold.", rewrite: light, force: should, status: drafted }
  forBeneficiary: { text: "Most students will do much better than the minimum standard, and your university should judge your work against shared national descriptions of the honours classes.", rewrite: full, force: should, status: drafted }
  author-agent-written: "Describe this as an expectation (should) on institutions to refer to Annex D when deciding evidence of achievement, with a stated expectation (will) that most students exceed the threshold, at FHEQ level 6 and FQHEIS level 10. Cite it as (QAA, 2024, Dance, Drama and Performance Subject Benchmark Statement, para 4.3) and set it beside qaa/fheq-2024/annex-d/summary/r1/3rd to r1/1st and the FHEQ document's SL6 bands. Do not claim the statement sets the class boundaries itself."
  author-agent-dialogue: "Raise it when a team aligns its marking criteria to degree classes, or a student asks what a 2.1 means. Ask staff how their 2.1 criteria compare with Annex D's description; ask a student which class description fits their recent work. Avoid suggesting the threshold is where most students finish."
- statement: qaa/dance-drama-and-performance-2024/4.6
  forPractitioner: { text: "Make the standards known to students and support them past the minimum. Treat the threshold as met when knowledge, understanding, creativity and skill are enough to present performance, information or argument in the discipline; expect excellent work to exceed the outcomes with originality, insight and artistic or technical excellence.", rewrite: light, force: will, status: drafted }
  forBeneficiary: { text: "You will meet the minimum standard when what you know and can do is enough to present a performance or an argument on your discipline's skills or materials; excellent work goes beyond the set outcomes, with originality, insight and high artistic or technical quality.", rewrite: full, force: will, status: drafted }
  author-agent-written: "Present this as the statement's own definition of its threshold and excellent rungs (will) for honours graduates at FHEQ level 6, with an expectation that students are supported beyond the minimum. Cite it as (QAA, 2024, Dance, Drama and Performance Subject Benchmark Statement, para 4.6) and set it beside the rung lists 4.8 to 4.16 and Annex D qaa/fheq-2024/annex-d/summary/r1/3rd and qaa/fheq-2024/annex-d/summary/r1/1st. Do not claim the excellent description is a requirement; it says what excellent work tends to show."
  author-agent-dialogue: "Raise it when a student asks what separates passing from excellent work. Ask them where in their recent work they went beyond what the brief asked. Never present originality as a condition of passing."
- statement: qaa/dance-drama-and-performance-2024/4.7
  forPractitioner: { text: "Whatever outcomes your course selects from the indicative list, build access, equality, diversity and inclusion, enterprise and sustainability into both content and practice.", rewrite: light, force: should, status: drafted }
  forBeneficiary: { text: "not-applicable: a duty on those who design courses; it sets no outcome for the student", rewrite: full, force: should, status: drafted }
  author-agent-written: "Describe this as an expectation (should) on every course in the subject: that the cross-cutting themes are embedded. Cite it as (QAA, 2024, Dance, Drama and Performance Subject Benchmark Statement, para 4.7) and set it beside the theme sections in paras 1.17 to 1.38 and the note in the same paragraph that the outcomes are indicative, not a checklist. Do not claim each listed outcome is required; only the themes carry this should."
  author-agent-dialogue: "Raise it when a team reviews a module for the four themes. Ask staff where in the module each theme shows in practice, not only in reading. Keep it with staff."
- statement: qaa/dance-drama-and-performance-2024/4.8.b1
  forPractitioner: { text: "Ensure students can show what they know of the art form's forms, practices, techniques and traditions, its histories locally and globally, and its uses.", rewrite: light, force: should, status: drafted }
  forBeneficiary: { text: "At the minimum standard for your honours degree, you should be able to show what you know about the forms, practices, techniques and traditions of performance, its histories around the world and how it is used.", rewrite: full, force: should, status: drafted }
  author-agent-written: "Treat this as the threshold standard: what every honours graduate should be able to show, the minimum for the award (should), in subject knowledge and understanding, for a bachelor's degree with honours in the subject at FHEQ level 6 (FQHEIS level 10). Cite it as (QAA, 2024, Dance, Drama and Performance Subject Benchmark Statement, para 4.8.b1). Do not present it as the level most students reach, since the statement expects most to go well beyond it (para 4.3), and do not call it a regulatory requirement. Set it beside the same outcome at the other rungs (4.11.b1, 4.14.b1), the honours descriptor qaa/fheq-2024/4.15.b1 with spine:6, and Annex D qaa/fheq-2024/annex-d/knowledge/r1/3rd."
  author-agent-dialogue: "Raise it when a student asks what they need to show to pass in this area, or staff check that a module secures the minimum. Put it in plain words: second person for a student, and for staff as what a module lets students show. Ask: Which tradition or history of performance could you explain to a newcomer, and which do you know only by name? Avoid reading the list aloud; draw out one example from their own work."
- statement: qaa/dance-drama-and-performance-2024/4.8.b2
  forPractitioner: { text: "Cover the building blocks of performance and the full life of a work, from creation and management to distribution, audience and documentation.", rewrite: light, force: should, status: drafted }
  forBeneficiary: { text: "At the minimum standard for your honours degree, you should know the main parts that make up a performance and how a work is made, managed, shared, watched and recorded.", rewrite: full, force: should, status: drafted }
  author-agent-written: "Treat this as the threshold standard: what every honours graduate should be able to show, the minimum for the award (should), in subject knowledge and understanding, for a bachelor's degree with honours in the subject at FHEQ level 6 (FQHEIS level 10). Cite it as (QAA, 2024, Dance, Drama and Performance Subject Benchmark Statement, para 4.8.b2). Do not present it as the level most students reach, since the statement expects most to go well beyond it (para 4.3), and do not call it a regulatory requirement. Set it beside the same outcome at the other rungs (4.11.b2, 4.14.b2), the honours descriptor qaa/fheq-2024/4.15.b1 with spine:6, and Annex D qaa/fheq-2024/annex-d/knowledge/r1/3rd."
  author-agent-dialogue: "Raise it when a student asks what they need to show to pass in this area, or staff check that a module secures the minimum. Put it in plain words: second person for a student, and for staff as what a module lets students show. Ask: Can you trace one of your own pieces from first idea to its record afterwards? Avoid reading the list aloud; draw out one example from their own work."
- statement: qaa/dance-drama-and-performance-2024/4.8.b3
  forPractitioner: { text: "Teach the critical and theoretical approaches the discipline uses and check students can show they know them.", rewrite: light, force: should, status: drafted }
  forBeneficiary: { text: "At the minimum standard for your honours degree, you should know the main critical and theoretical ways of studying your discipline.", rewrite: full, force: should, status: drafted }
  author-agent-written: "Treat this as the threshold standard: what every honours graduate should be able to show, the minimum for the award (should), in subject knowledge and understanding, for a bachelor's degree with honours in the subject at FHEQ level 6 (FQHEIS level 10). Cite it as (QAA, 2024, Dance, Drama and Performance Subject Benchmark Statement, para 4.8.b3). Do not present it as the level most students reach, since the statement expects most to go well beyond it (para 4.3), and do not call it a regulatory requirement. Set it beside the same outcome at the other rungs (4.11.b3, 4.14.b3), the honours descriptor qaa/fheq-2024/4.15.b7 with spine:6, and Annex D qaa/fheq-2024/annex-d/knowledge/r2/3rd."
  author-agent-dialogue: "Raise it when a student asks what they need to show to pass in this area, or staff check that a module secures the minimum. Put it in plain words: second person for a student, and for staff as what a module lets students show. Ask: Which critical or theoretical approach do you use most, and when did you last test it against another? Avoid reading the list aloud; draw out one example from their own work."
- statement: qaa/dance-drama-and-performance-2024/4.8.b4
  forPractitioner: { text: "Introduce key practitioners, practices or theorists and the cultural and historical settings that shaped them.", rewrite: light, force: should, status: drafted }
  forBeneficiary: { text: "At the minimum standard for your honours degree, you should know about practitioners, practices or theorists and the cultural or historical settings they come from.", rewrite: full, force: should, status: drafted }
  author-agent-written: "Treat this as the threshold standard: what every honours graduate should be able to show, the minimum for the award (should), in subject knowledge and understanding, for a bachelor's degree with honours in the subject at FHEQ level 6 (FQHEIS level 10). Cite it as (QAA, 2024, Dance, Drama and Performance Subject Benchmark Statement, para 4.8.b4). Do not present it as the level most students reach, since the statement expects most to go well beyond it (para 4.3), and do not call it a regulatory requirement. Set it beside the same outcome at the other rungs (4.11.b4, 4.14.b4), the honours descriptor qaa/fheq-2024/4.15.b1 with spine:6, and Annex D qaa/fheq-2024/annex-d/knowledge/r1/3rd."
  author-agent-dialogue: "Raise it when a student asks what they need to show to pass in this area, or staff check that a module secures the minimum. Put it in plain words: second person for a student, and for staff as what a module lets students show. Ask: Which practitioner shaped your work most, and what in their context explains their approach? Avoid reading the list aloud; draw out one example from their own work."
- statement: qaa/dance-drama-and-performance-2024/4.8.b5
  forPractitioner: { text: "Show students how performance functions in communities, education, participatory work and the industry.", rewrite: light, force: should, status: drafted }
  forBeneficiary: { text: "At the minimum standard for your honours degree, you should know what performance does in society, in education, in participatory work and in the industry.", rewrite: full, force: should, status: drafted }
  author-agent-written: "Treat this as the threshold standard: what every honours graduate should be able to show, the minimum for the award (should), in subject knowledge and understanding, for a bachelor's degree with honours in the subject at FHEQ level 6 (FQHEIS level 10). Cite it as (QAA, 2024, Dance, Drama and Performance Subject Benchmark Statement, para 4.8.b5). Do not present it as the level most students reach, since the statement expects most to go well beyond it (para 4.3), and do not call it a regulatory requirement. Set it beside the same outcome at the other rungs (4.11.b5, 4.14.b5), the honours descriptor qaa/fheq-2024/4.15.b1 with spine:6, and Annex D qaa/fheq-2024/annex-d/knowledge/r1/3rd."
  author-agent-dialogue: "Raise it when a student asks what they need to show to pass in this area, or staff check that a module secures the minimum. Put it in plain words: second person for a student, and for staff as what a module lets students show. Ask: Where have you seen performance do work outside the theatre, in a school, a community or an industry? Avoid reading the list aloud; draw out one example from their own work."
- statement: qaa/dance-drama-and-performance-2024/4.8.b6
  forPractitioner: { text: "Help students see how critical study and creative practice feed each other as ways of enquiring.", rewrite: light, force: should, status: drafted }
  forBeneficiary: { text: "At the minimum standard for your honours degree, you should understand how thinking critically and making creative work feed into each other.", rewrite: full, force: should, status: drafted }
  author-agent-written: "Treat this as the threshold standard: what every honours graduate should be able to show, the minimum for the award (should), in subject knowledge and understanding, for a bachelor's degree with honours in the subject at FHEQ level 6 (FQHEIS level 10). Cite it as (QAA, 2024, Dance, Drama and Performance Subject Benchmark Statement, para 4.8.b6). Do not present it as the level most students reach, since the statement expects most to go well beyond it (para 4.3), and do not call it a regulatory requirement. Set it beside the same outcome at the other rungs (4.11.b6, 4.14.b6), the honours descriptor qaa/fheq-2024/4.15.b7 with spine:6, and Annex D qaa/fheq-2024/annex-d/cognitive/r2/3rd."
  author-agent-dialogue: "Raise it when a student asks what they need to show to pass in this area, or staff check that a module secures the minimum. Put it in plain words: second person for a student, and for staff as what a module lets students show. Ask: When did critical reading last change something you made, or making change how you read? Avoid reading the list aloud; draw out one example from their own work."
- statement: qaa/dance-drama-and-performance-2024/4.8.b7
  forPractitioner: { text: "Teach students to read and interpret scripts, media, notation and scores as material for making performance.", rewrite: light, force: should, status: drafted }
  forBeneficiary: { text: "At the minimum standard for your honours degree, you should understand how to read and interpret scripts, media, notation or scores to make performance.", rewrite: full, force: should, status: drafted }
  author-agent-written: "Treat this as the threshold standard: what every honours graduate should be able to show, the minimum for the award (should), in subject knowledge and understanding, for a bachelor's degree with honours in the subject at FHEQ level 6 (FQHEIS level 10). Cite it as (QAA, 2024, Dance, Drama and Performance Subject Benchmark Statement, para 4.8.b7). Do not present it as the level most students reach, since the statement expects most to go well beyond it (para 4.3), and do not call it a regulatory requirement. Set it beside the same outcome at the other rungs (4.11.b7, 4.14.b7), the honours descriptor qaa/fheq-2024/4.15.b2 with spine:6, and Annex D qaa/fheq-2024/annex-d/knowledge/r2/3rd."
  author-agent-dialogue: "Raise it when a student asks what they need to show to pass in this area, or staff check that a module secures the minimum. Put it in plain words: second person for a student, and for staff as what a module lets students show. Ask: How do you move from a script or score to choices in the room? Avoid reading the list aloud; draw out one example from their own work."
- statement: qaa/dance-drama-and-performance-2024/4.8.b8
  forPractitioner: { text: "Help students understand how groups and ensembles work, including their dynamics and effects.", rewrite: light, force: should, status: drafted }
  forBeneficiary: { text: "At the minimum standard for your honours degree, you should understand how groups and ensembles work, and the effects and dynamics they bring.", rewrite: full, force: should, status: drafted }
  author-agent-written: "Treat this as the threshold standard: what every honours graduate should be able to show, the minimum for the award (should), in subject knowledge and understanding, for a bachelor's degree with honours in the subject at FHEQ level 6 (FQHEIS level 10). Cite it as (QAA, 2024, Dance, Drama and Performance Subject Benchmark Statement, para 4.8.b8). Do not present it as the level most students reach, since the statement expects most to go well beyond it (para 4.3), and do not call it a regulatory requirement. Set it beside the same outcome at the other rungs (4.11.b8, 4.14.b8), the honours descriptor qaa/fheq-2024/4.15.b9.1 with spine:6, and Annex D qaa/fheq-2024/annex-d/transferable/r2/3rd."
  author-agent-dialogue: "Raise it when a student asks what they need to show to pass in this area, or staff check that a module secures the minimum. Put it in plain words: second person for a student, and for staff as what a module lets students show. Ask: What did your last group process teach you about how ensembles work? Avoid reading the list aloud; draw out one example from their own work."
- statement: qaa/dance-drama-and-performance-2024/4.8.b9
  forPractitioner: { text: "Cover the elements performance works with, for example sources, performers, space, sound, text, movement and setting.", rewrite: light, force: should, status: drafted }
  forBeneficiary: { text: "At the minimum standard for your honours degree, you should understand the building blocks of performance, such as source material, performers, space, sound, text, movement and setting.", rewrite: full, force: should, status: drafted }
  author-agent-written: "Treat this as the threshold standard: what every honours graduate should be able to show, the minimum for the award (should), in subject knowledge and understanding, for a bachelor's degree with honours in the subject at FHEQ level 6 (FQHEIS level 10). Cite it as (QAA, 2024, Dance, Drama and Performance Subject Benchmark Statement, para 4.8.b9). Do not present it as the level most students reach, since the statement expects most to go well beyond it (para 4.3), and do not call it a regulatory requirement. Set it beside the same outcome at the other rungs (4.11.b9, 4.14.b9), the honours descriptor qaa/fheq-2024/4.15.b1 with spine:6, and Annex D qaa/fheq-2024/annex-d/knowledge/r2/3rd."
  author-agent-dialogue: "Raise it when a student asks what they need to show to pass in this area, or staff check that a module secures the minimum. Put it in plain words: second person for a student, and for staff as what a module lets students show. Ask: Which element of performance do you tend to overlook, and what happens when you put it first? Avoid reading the list aloud; draw out one example from their own work."
- statement: qaa/dance-drama-and-performance-2024/4.8.b10
  forPractitioner: { text: "Introduce the interdisciplinary elements that suit the course and show students how to apply them.", rewrite: light, force: should, status: drafted }
  forBeneficiary: { text: "At the minimum standard for your honours degree, you should understand which ideas and methods from across disciplines suit performance, and how to use them.", rewrite: full, force: should, status: drafted }
  author-agent-written: "Treat this as the threshold standard: what every honours graduate should be able to show, the minimum for the award (should), in subject knowledge and understanding, for a bachelor's degree with honours in the subject at FHEQ level 6 (FQHEIS level 10). Cite it as (QAA, 2024, Dance, Drama and Performance Subject Benchmark Statement, para 4.8.b10). Do not present it as the level most students reach, since the statement expects most to go well beyond it (para 4.3), and do not call it a regulatory requirement. Set it beside the same outcome at the other rungs (4.11.b10, 4.14.b10), the honours descriptor qaa/fheq-2024/4.15.b3.1 with spine:6, and Annex D qaa/fheq-2024/annex-d/knowledge/r2/3rd."
  author-agent-dialogue: "Raise it when a student asks what they need to show to pass in this area, or staff check that a module secures the minimum. Put it in plain words: second person for a student, and for staff as what a module lets students show. Ask: Which idea from another discipline has changed your practice, and how did you apply it? Avoid reading the list aloud; draw out one example from their own work."
- statement: qaa/dance-drama-and-performance-2024/4.8.b11
  forPractitioner: { text: "Bring in knowledge, practices, concepts and skills from neighbouring disciplines and check students understand them.", rewrite: light, force: should, status: drafted }
  forBeneficiary: { text: "At the minimum standard for your honours degree, you should understand ideas, practices and skills that come from other subjects.", rewrite: full, force: should, status: drafted }
  author-agent-written: "Treat this as the threshold standard: what every honours graduate should be able to show, the minimum for the award (should), in subject knowledge and understanding, for a bachelor's degree with honours in the subject at FHEQ level 6 (FQHEIS level 10). Cite it as (QAA, 2024, Dance, Drama and Performance Subject Benchmark Statement, para 4.8.b11). Do not present it as the level most students reach, since the statement expects most to go well beyond it (para 4.3), and do not call it a regulatory requirement. Set it beside the other items in para 4.8, since this outcome has no counterpart at the other rungs, the honours descriptor qaa/fheq-2024/4.15.b1 with spine:6, and Annex D qaa/fheq-2024/annex-d/knowledge/r2/3rd."
  author-agent-dialogue: "Raise it when a student asks what they need to show to pass in this area, or staff check that a module secures the minimum. Put it in plain words: second person for a student, and for staff as what a module lets students show. Ask: Which subject outside performance do you draw on, and for what? Avoid reading the list aloud; draw out one example from their own work."
- statement: qaa/dance-drama-and-performance-2024/4.8.b12
  forPractitioner: { text: "Teach students the duty performance practitioners carry for safe, ethical and environmentally sustainable ways of working.", rewrite: light, force: should, status: drafted }
  forBeneficiary: { text: "At the minimum standard for your honours degree, you should understand your duty, as someone who makes performance, to work safely, ethically and sustainably.", rewrite: full, force: should, status: drafted }
  author-agent-written: "Treat this as the threshold standard: what every honours graduate should be able to show, the minimum for the award (should), in subject knowledge and understanding, for a bachelor's degree with honours in the subject at FHEQ level 6 (FQHEIS level 10). Cite it as (QAA, 2024, Dance, Drama and Performance Subject Benchmark Statement, para 4.8.b12). Do not present it as the level most students reach, since the statement expects most to go well beyond it (para 4.3), and do not call it a regulatory requirement. Set it beside the same outcome at the other rungs (4.11.b11, 4.14.b11), the honours descriptor qaa/fheq-2024/4.15.b9.2 with spine:6, and Annex D qaa/fheq-2024/annex-d/transferable/r4/3rd."
  author-agent-dialogue: "Raise it when a student asks what they need to show to pass in this area, or staff check that a module secures the minimum. Put it in plain words: second person for a student, and for staff as what a module lets students show. Ask: How did you make your last project safe, ethical and environmentally sound? Avoid reading the list aloud; draw out one example from their own work."
- statement: qaa/dance-drama-and-performance-2024/4.9.b1
  forPractitioner: { text: "Give students repeated practice in making or producing performance with the field's vocabularies, techniques, crafts, technologies and methods.", rewrite: light, force: should, status: drafted }
  forBeneficiary: { text: "At the minimum standard for your honours degree, you should be able to make or produce performance using the techniques, crafts, technologies and working methods of your field.", rewrite: full, force: should, status: drafted }
  author-agent-written: "Treat this as the threshold standard: what every honours graduate should be able to show, the minimum for the award (should), in subject-specific skills, for a bachelor's degree with honours in the subject at FHEQ level 6 (FQHEIS level 10). Cite it as (QAA, 2024, Dance, Drama and Performance Subject Benchmark Statement, para 4.9.b1). Do not present it as the level most students reach, since the statement expects most to go well beyond it (para 4.3), and do not call it a regulatory requirement. Set it beside the same outcome at the other rungs (4.12.b3, 4.15.b3), the honours descriptor qaa/fheq-2024/4.15.b2 with spine:6, and Annex D qaa/fheq-2024/annex-d/practical/r3/3rd."
  author-agent-dialogue: "Raise it when a student asks what they need to show to pass in this area, or staff check that a module secures the minimum. Put it in plain words: second person for a student, and for staff as what a module lets students show. Ask: Which working methods could you use to make a piece from scratch without being shown? Avoid reading the list aloud; draw out one example from their own work."
- statement: qaa/dance-drama-and-performance-2024/4.9.b2
  forPractitioner: { text: "Train students to read a text, stimulus, media, notation or score for its performance possibilities and to realise them in design, technology and performance.", rewrite: light, force: should, status: drafted }
  forBeneficiary: { text: "At the minimum standard for your honours degree, you should be able to see what a script, prompt, notation or score could become in performance and bring it to life through design, technology and performance.", rewrite: full, force: should, status: drafted }
  author-agent-written: "Treat this as the threshold standard: what every honours graduate should be able to show, the minimum for the award (should), in subject-specific skills, for a bachelor's degree with honours in the subject at FHEQ level 6 (FQHEIS level 10). Cite it as (QAA, 2024, Dance, Drama and Performance Subject Benchmark Statement, para 4.9.b2). Do not present it as the level most students reach, since the statement expects most to go well beyond it (para 4.3), and do not call it a regulatory requirement. Set it beside the same outcome at the other rungs (4.12.b2, 4.15.b2), the honours descriptor qaa/fheq-2024/4.15.b2 with spine:6, and Annex D qaa/fheq-2024/annex-d/practical/r3/3rd."
  author-agent-dialogue: "Raise it when a student asks what they need to show to pass in this area, or staff check that a module secures the minimum. Put it in plain words: second person for a student, and for staff as what a module lets students show. Ask: What did the last text or score you worked on make possible, and what did you do with it? Avoid reading the list aloud; draw out one example from their own work."
- statement: qaa/dance-drama-and-performance-2024/4.9.b3
  forPractitioner: { text: "Teach notation and documentation so students can make records of performance.", rewrite: light, force: should, status: drafted }
  forBeneficiary: { text: "At the minimum standard for your honours degree, you should be able to record performance using notation, documentation and the technology for it.", rewrite: full, force: should, status: drafted }
  author-agent-written: "Treat this as the threshold standard: what every honours graduate should be able to show, the minimum for the award (should), in subject-specific skills, for a bachelor's degree with honours in the subject at FHEQ level 6 (FQHEIS level 10). Cite it as (QAA, 2024, Dance, Drama and Performance Subject Benchmark Statement, para 4.9.b3). Do not present it as the level most students reach, since the statement expects most to go well beyond it (para 4.3), and do not call it a regulatory requirement. Set it beside the other items in para 4.9, since this outcome has no counterpart at the other rungs, the honours descriptor qaa/fheq-2024/4.15.b2 with spine:6, and Annex D qaa/fheq-2024/annex-d/practical/r4/3rd."
  author-agent-dialogue: "Raise it when a student asks what they need to show to pass in this area, or staff check that a module secures the minimum. Put it in plain words: second person for a student, and for staff as what a module lets students show. Ask: How did you record your last piece, and could someone restage it from that record? Avoid reading the list aloud; draw out one example from their own work."
- statement: qaa/dance-drama-and-performance-2024/4.9.b4
  forPractitioner: { text: "Give students practice in describing, interpreting and judging performances they make or see.", rewrite: light, force: should, status: drafted }
  forBeneficiary: { text: "At the minimum standard for your honours degree, you should be able to describe, interpret and judge performances.", rewrite: full, force: should, status: drafted }
  author-agent-written: "Treat this as the threshold standard: what every honours graduate should be able to show, the minimum for the award (should), in subject-specific skills, for a bachelor's degree with honours in the subject at FHEQ level 6 (FQHEIS level 10). Cite it as (QAA, 2024, Dance, Drama and Performance Subject Benchmark Statement, para 4.9.b4). Do not present it as the level most students reach, since the statement expects most to go well beyond it (para 4.3), and do not call it a regulatory requirement. Set it beside the other items in para 4.9, since this outcome has no counterpart at the other rungs, the honours descriptor qaa/fheq-2024/4.15.b7 with spine:6, and Annex D qaa/fheq-2024/annex-d/cognitive/r1/3rd."
  author-agent-dialogue: "Raise it when a student asks what they need to show to pass in this area, or staff check that a module secures the minimum. Put it in plain words: second person for a student, and for staff as what a module lets students show. Ask: Can you describe, interpret and judge a performance you saw recently in a few sentences? Avoid reading the list aloud; draw out one example from their own work."
- statement: qaa/dance-drama-and-performance-2024/4.9.b5
  forPractitioner: { text: "Build independent research into the course, both historical study and research within the making of work.", rewrite: light, force: should, status: drafted }
  forBeneficiary: { text: "At the minimum standard for your honours degree, you should be able to research on your own, whether looking at past or present performance or as part of making or responding to work.", rewrite: full, force: should, status: drafted }
  author-agent-written: "Treat this as the threshold standard: what every honours graduate should be able to show, the minimum for the award (should), in subject-specific skills, for a bachelor's degree with honours in the subject at FHEQ level 6 (FQHEIS level 10). Cite it as (QAA, 2024, Dance, Drama and Performance Subject Benchmark Statement, para 4.9.b5). Do not present it as the level most students reach, since the statement expects most to go well beyond it (para 4.3), and do not call it a regulatory requirement. Set it beside the same outcome at the other rungs (4.12.b4, 4.15.b4), the honours descriptor qaa/fheq-2024/4.15.b6 with spine:6, and Annex D qaa/fheq-2024/annex-d/knowledge/r3/3rd."
  author-agent-dialogue: "Raise it when a student asks what they need to show to pass in this area, or staff check that a module secures the minimum. Put it in plain words: second person for a student, and for staff as what a module lets students show. Ask: What question did your last independent research answer, and where did you find the evidence? Avoid reading the list aloud; draw out one example from their own work."
- statement: qaa/dance-drama-and-performance-2024/4.9.b6
  forPractitioner: { text: "Help students name the cultural and contextual frameworks around the performance they study and make.", rewrite: light, force: should, status: drafted }
  forBeneficiary: { text: "At the minimum standard for your honours degree, you should be able to identify the cultural settings and contexts that frame a performance.", rewrite: full, force: should, status: drafted }
  author-agent-written: "Treat this as the threshold standard: what every honours graduate should be able to show, the minimum for the award (should), in subject-specific skills, for a bachelor's degree with honours in the subject at FHEQ level 6 (FQHEIS level 10). Cite it as (QAA, 2024, Dance, Drama and Performance Subject Benchmark Statement, para 4.9.b6). Do not present it as the level most students reach, since the statement expects most to go well beyond it (para 4.3), and do not call it a regulatory requirement. Set it beside the same outcome at the other rungs (4.12.b5, 4.15.b5), the honours descriptor qaa/fheq-2024/4.15.b7 with spine:6, and Annex D qaa/fheq-2024/annex-d/cognitive/r1/3rd."
  author-agent-dialogue: "Raise it when a student asks what they need to show to pass in this area, or staff check that a module secures the minimum. Put it in plain words: second person for a student, and for staff as what a module lets students show. Ask: What cultural frame shapes the piece you are working on now? Avoid reading the list aloud; draw out one example from their own work."
- statement: qaa/dance-drama-and-performance-2024/4.9.b7
  forPractitioner: { text: "Give students tasks that explore performance spaces and what their spatial relationships mean for the work.", rewrite: light, force: should, status: drafted }
  forBeneficiary: { text: "At the minimum standard for your honours degree, you should be able to explore a performance space and work out what its spatial relationships mean.", rewrite: full, force: should, status: drafted }
  author-agent-written: "Treat this as the threshold standard: what every honours graduate should be able to show, the minimum for the award (should), in subject-specific skills, for a bachelor's degree with honours in the subject at FHEQ level 6 (FQHEIS level 10). Cite it as (QAA, 2024, Dance, Drama and Performance Subject Benchmark Statement, para 4.9.b7). Do not present it as the level most students reach, since the statement expects most to go well beyond it (para 4.3), and do not call it a regulatory requirement. Set it beside the other items in para 4.9, since this outcome has no counterpart at the other rungs, the honours descriptor qaa/fheq-2024/4.15.b6 with spine:6, and Annex D qaa/fheq-2024/annex-d/practical/r1/3rd."
  author-agent-dialogue: "Raise it when a student asks what they need to show to pass in this area, or staff check that a module secures the minimum. Put it in plain words: second person for a student, and for staff as what a module lets students show. Ask: How did the space change your last piece? Avoid reading the list aloud; draw out one example from their own work."
- statement: qaa/dance-drama-and-performance-2024/4.10.b1
  forPractitioner: { text: "Give students tasks where they set their own goals, manage workloads and meet deadlines.", rewrite: light, force: should, status: drafted }
  forBeneficiary: { text: "At the minimum standard for your honours degree, you should be able to manage yourself: set goals, handle your workload and meet deadlines.", rewrite: full, force: should, status: drafted }
  author-agent-written: "Treat this as the threshold standard: what every honours graduate should be able to show, the minimum for the award (should), in generic and graduate skills, for a bachelor's degree with honours in the subject at FHEQ level 6 (FQHEIS level 10). Cite it as (QAA, 2024, Dance, Drama and Performance Subject Benchmark Statement, para 4.10.b1). Do not present it as the level most students reach, since the statement expects most to go well beyond it (para 4.3), and do not call it a regulatory requirement. Set it beside the same outcome at the other rungs (4.13.b4, 4.16.b4), the honours descriptor qaa/fheq-2024/4.15.b5 with spine:6, and Annex D qaa/fheq-2024/annex-d/transferable/r3/3rd."
  author-agent-dialogue: "Raise it when a student asks what they need to show to pass in this area, or staff check that a module secures the minimum. Put it in plain words: second person for a student, and for staff as what a module lets students show. Ask: How do you plan your time when rehearsals and deadlines collide? Avoid reading the list aloud; draw out one example from their own work."
- statement: qaa/dance-drama-and-performance-2024/4.10.b2
  forPractitioner: { text: "Create situations that ask students to adapt and to reflect critically on themselves and others.", rewrite: light, force: should, status: drafted }
  forBeneficiary: { text: "At the minimum standard for your honours degree, you should be able to adapt, stay flexible and think critically about yourself and others.", rewrite: full, force: should, status: drafted }
  author-agent-written: "Treat this as the threshold standard: what every honours graduate should be able to show, the minimum for the award (should), in generic and graduate skills, for a bachelor's degree with honours in the subject at FHEQ level 6 (FQHEIS level 10). Cite it as (QAA, 2024, Dance, Drama and Performance Subject Benchmark Statement, para 4.10.b2). Do not present it as the level most students reach, since the statement expects most to go well beyond it (para 4.3), and do not call it a regulatory requirement. Set it beside the other items in para 4.10, since this outcome has no counterpart at the other rungs, the honours descriptor qaa/fheq-2024/4.15.b4 with spine:6, and Annex D qaa/fheq-2024/annex-d/transferable/r5/3rd."
  author-agent-dialogue: "Raise it when a student asks what they need to show to pass in this area, or staff check that a module secures the minimum. Put it in plain words: second person for a student, and for staff as what a module lets students show. Ask: When did you last change your approach because of feedback, and what did you notice about yourself? Avoid reading the list aloud; draw out one example from their own work."
- statement: qaa/dance-drama-and-performance-2024/4.10.b3
  forPractitioner: { text: "Teach risk assessment and ethical working, and expect both in practical work.", rewrite: light, force: should, status: drafted }
  forBeneficiary: { text: "At the minimum standard for your honours degree, you should be able to assess and manage risk and work ethically.", rewrite: full, force: should, status: drafted }
  author-agent-written: "Treat this as the threshold standard: what every honours graduate should be able to show, the minimum for the award (should), in generic and graduate skills, for a bachelor's degree with honours in the subject at FHEQ level 6 (FQHEIS level 10). Cite it as (QAA, 2024, Dance, Drama and Performance Subject Benchmark Statement, para 4.10.b3). Do not present it as the level most students reach, since the statement expects most to go well beyond it (para 4.3), and do not call it a regulatory requirement. Set it beside the other items in para 4.10, since this outcome has no counterpart at the other rungs, the honours descriptor qaa/fheq-2024/4.15.b9.2 with spine:6, and Annex D qaa/fheq-2024/annex-d/transferable/r4/3rd."
  author-agent-dialogue: "Raise it when a student asks what they need to show to pass in this area, or staff check that a module secures the minimum. Put it in plain words: second person for a student, and for staff as what a module lets students show. Ask: What risks did you assess on your last practical project, and how did you manage them? Avoid reading the list aloud; draw out one example from their own work."
- statement: qaa/dance-drama-and-performance-2024/4.10.b4
  forPractitioner: { text: "Ask students to respond reflexively and critically, develop ideas and make and present arguments in fitting forms.", rewrite: light, force: should, status: drafted }
  forBeneficiary: { text: "At the minimum standard for your honours degree, you should be able to think critically and reflexively, develop ideas and build and present an argument in a suitable form.", rewrite: full, force: should, status: drafted }
  author-agent-written: "Treat this as the threshold standard: what every honours graduate should be able to show, the minimum for the award (should), in generic and graduate skills, for a bachelor's degree with honours in the subject at FHEQ level 6 (FQHEIS level 10). Cite it as (QAA, 2024, Dance, Drama and Performance Subject Benchmark Statement, para 4.10.b4). Do not present it as the level most students reach, since the statement expects most to go well beyond it (para 4.3), and do not call it a regulatory requirement. Set it beside the same outcome at the other rungs (4.13.b1, 4.16.b1), the honours descriptor qaa/fheq-2024/4.15.b3.1 with spine:6, and Annex D qaa/fheq-2024/annex-d/cognitive/r2/3rd."
  author-agent-dialogue: "Raise it when a student asks what they need to show to pass in this area, or staff check that a module secures the minimum. Put it in plain words: second person for a student, and for staff as what a module lets students show. Ask: What is the strongest argument you have built this year, and how did you present it? Avoid reading the list aloud; draw out one example from their own work."
- statement: qaa/dance-drama-and-performance-2024/4.10.b5
  forPractitioner: { text: "Build collaborative projects that call for and assess team skills.", rewrite: light, force: should, status: drafted }
  forBeneficiary: { text: "At the minimum standard for your honours degree, you should be able to work in a group or team and have the skills to complete a shared project.", rewrite: full, force: should, status: drafted }
  author-agent-written: "Treat this as the threshold standard: what every honours graduate should be able to show, the minimum for the award (should), in generic and graduate skills, for a bachelor's degree with honours in the subject at FHEQ level 6 (FQHEIS level 10). Cite it as (QAA, 2024, Dance, Drama and Performance Subject Benchmark Statement, para 4.10.b5). Do not present it as the level most students reach, since the statement expects most to go well beyond it (para 4.3), and do not call it a regulatory requirement. Set it beside the same outcome at the other rungs (4.13.b3, 4.16.b3), the honours descriptor qaa/fheq-2024/4.15.b9.1 with spine:6, and Annex D qaa/fheq-2024/annex-d/transferable/r2/3rd."
  author-agent-dialogue: "Raise it when a student asks what they need to show to pass in this area, or staff check that a module secures the minimum. Put it in plain words: second person for a student, and for staff as what a module lets students show. Ask: What did you contribute to your last group project that no one else did? Avoid reading the list aloud; draw out one example from their own work."
- statement: qaa/dance-drama-and-performance-2024/4.10.b6
  forPractitioner: { text: "Support students to manage creative and interpersonal tensions within creative work.", rewrite: light, force: should, status: drafted }
  forBeneficiary: { text: "At the minimum standard for your honours degree, you should be able to handle creative, personal and interpersonal issues that come up in creative work.", rewrite: full, force: should, status: drafted }
  author-agent-written: "Treat this as the threshold standard: what every honours graduate should be able to show, the minimum for the award (should), in generic and graduate skills, for a bachelor's degree with honours in the subject at FHEQ level 6 (FQHEIS level 10). Cite it as (QAA, 2024, Dance, Drama and Performance Subject Benchmark Statement, para 4.10.b6). Do not present it as the level most students reach, since the statement expects most to go well beyond it (para 4.3), and do not call it a regulatory requirement. Set it beside the same outcome at the other rungs (4.13.b5, 4.16.b5), the honours descriptor qaa/fheq-2024/4.15.b9.1 with spine:6, and Annex D qaa/fheq-2024/annex-d/transferable/r2/3rd."
  author-agent-dialogue: "Raise it when a student asks what they need to show to pass in this area, or staff check that a module secures the minimum. Put it in plain words: second person for a student, and for staff as what a module lets students show. Ask: How did you handle a disagreement in a creative team? Avoid reading the list aloud; draw out one example from their own work."
- statement: qaa/dance-drama-and-performance-2024/4.10.b7
  forPractitioner: { text: "Assess communication in varied forms, matched to content and context.", rewrite: light, force: should, status: drafted }
  forBeneficiary: { text: "At the minimum standard for your honours degree, you should be able to communicate and present ideas and information in different forms, suited to what you are saying and to whom.", rewrite: full, force: should, status: drafted }
  author-agent-written: "Treat this as the threshold standard: what every honours graduate should be able to show, the minimum for the award (should), in generic and graduate skills, for a bachelor's degree with honours in the subject at FHEQ level 6 (FQHEIS level 10). Cite it as (QAA, 2024, Dance, Drama and Performance Subject Benchmark Statement, para 4.10.b7). Do not present it as the level most students reach, since the statement expects most to go well beyond it (para 4.3), and do not call it a regulatory requirement. Set it beside the other items in para 4.10, since this outcome has no counterpart at the other rungs, the honours descriptor qaa/fheq-2024/4.15.b8 with spine:6, and Annex D qaa/fheq-2024/annex-d/transferable/r1/3rd."
  author-agent-dialogue: "Raise it when a student asks what they need to show to pass in this area, or staff check that a module secures the minimum. Put it in plain words: second person for a student, and for staff as what a module lets students show. Ask: In which forms have you presented your ideas this year, and which worked best for which audience? Avoid reading the list aloud; draw out one example from their own work."
- statement: qaa/dance-drama-and-performance-2024/4.10.b8
  forPractitioner: { text: "Teach information skills: finding, gathering, sifting, judging and organising sources.", rewrite: light, force: should, status: drafted }
  forBeneficiary: { text: "At the minimum standard for your honours degree, you should be able to find, gather, sift, judge and organise information.", rewrite: full, force: should, status: drafted }
  author-agent-written: "Treat this as the threshold standard: what every honours graduate should be able to show, the minimum for the award (should), in generic and graduate skills, for a bachelor's degree with honours in the subject at FHEQ level 6 (FQHEIS level 10). Cite it as (QAA, 2024, Dance, Drama and Performance Subject Benchmark Statement, para 4.10.b8). Do not present it as the level most students reach, since the statement expects most to go well beyond it (para 4.3), and do not call it a regulatory requirement. Set it beside the same outcome at the other rungs (4.13.b6, 4.16.b6), the honours descriptor qaa/fheq-2024/4.15.b5 with spine:6, and Annex D qaa/fheq-2024/annex-d/cognitive/r1/3rd."
  author-agent-dialogue: "Raise it when a student asks what they need to show to pass in this area, or staff check that a module secures the minimum. Put it in plain words: second person for a student, and for staff as what a module lets students show. Ask: How do you decide which sources to keep and which to drop? Avoid reading the list aloud; draw out one example from their own work."
- statement: qaa/dance-drama-and-performance-2024/4.10.b9
  forPractitioner: { text: "Give students practice in choosing, using and adapting digital tools for their work.", rewrite: light, force: should, status: drafted }
  forBeneficiary: { text: "At the minimum standard for your honours degree, you should be able to choose, use and adapt digital media and technology.", rewrite: full, force: should, status: drafted }
  author-agent-written: "Treat this as the threshold standard: what every honours graduate should be able to show, the minimum for the award (should), in generic and graduate skills, for a bachelor's degree with honours in the subject at FHEQ level 6 (FQHEIS level 10). Cite it as (QAA, 2024, Dance, Drama and Performance Subject Benchmark Statement, para 4.10.b9). Do not present it as the level most students reach, since the statement expects most to go well beyond it (para 4.3), and do not call it a regulatory requirement. Set it beside the same outcome at the other rungs (4.13.b7, 4.16.b7), the honours descriptor qaa/fheq-2024/4.15.b6 with spine:6, and Annex D qaa/fheq-2024/annex-d/transferable/r1/3rd."
  author-agent-dialogue: "Raise it when a student asks what they need to show to pass in this area, or staff check that a module secures the minimum. Put it in plain words: second person for a student, and for staff as what a module lets students show. Ask: Which digital tool have you adapted for your own creative purpose? Avoid reading the list aloud; draw out one example from their own work."
- statement: qaa/dance-drama-and-performance-2024/4.10.b10
  forPractitioner: { text: "Give students projects they plan, organise and deliver themselves.", rewrite: light, force: should, status: drafted }
  forBeneficiary: { text: "At the minimum standard for your honours degree, you should be able to plan, organise and carry out a project.", rewrite: full, force: should, status: drafted }
  author-agent-written: "Treat this as the threshold standard: what every honours graduate should be able to show, the minimum for the award (should), in generic and graduate skills, for a bachelor's degree with honours in the subject at FHEQ level 6 (FQHEIS level 10). Cite it as (QAA, 2024, Dance, Drama and Performance Subject Benchmark Statement, para 4.10.b10). Do not present it as the level most students reach, since the statement expects most to go well beyond it (para 4.3), and do not call it a regulatory requirement. Set it beside the other items in para 4.10, since this outcome has no counterpart at the other rungs, the honours descriptor qaa/fheq-2024/4.15.b9.1 with spine:6, and Annex D qaa/fheq-2024/annex-d/transferable/r3/3rd."
  author-agent-dialogue: "Raise it when a student asks what they need to show to pass in this area, or staff check that a module secures the minimum. Put it in plain words: second person for a student, and for staff as what a module lets students show. Ask: How did you plan and organise the last activity you led? Avoid reading the list aloud; draw out one example from their own work."
- statement: qaa/dance-drama-and-performance-2024/4.10.b11
  forPractitioner: { text: "Build numeracy into practical work, such as budgets, timings and technical calculations.", rewrite: light, force: should, status: drafted }
  forBeneficiary: { text: "At the minimum standard for your honours degree, you should be able to use numbers to solve problems and make creative work happen.", rewrite: full, force: should, status: drafted }
  author-agent-written: "Treat this as the threshold standard: what every honours graduate should be able to show, the minimum for the award (should), in generic and graduate skills, for a bachelor's degree with honours in the subject at FHEQ level 6 (FQHEIS level 10). Cite it as (QAA, 2024, Dance, Drama and Performance Subject Benchmark Statement, para 4.10.b11). Do not present it as the level most students reach, since the statement expects most to go well beyond it (para 4.3), and do not call it a regulatory requirement. Set it beside the same outcome at the other rungs (4.13.b8, 4.16.b8), the honours descriptor qaa/fheq-2024/4.15.b3.1 with spine:6, and Annex D qaa/fheq-2024/annex-d/transferable/r1/3rd."
  author-agent-dialogue: "Raise it when a student asks what they need to show to pass in this area, or staff check that a module secures the minimum. Put it in plain words: second person for a student, and for staff as what a module lets students show. Ask: Where did numbers matter in your last production, for example a budget, a schedule or a lighting plot? Avoid reading the list aloud; draw out one example from their own work."
- statement: qaa/dance-drama-and-performance-2024/4.11.b1
  forPractitioner: { text: "Expect students to engage creatively and critically with the art form's forms, techniques, traditions and histories, and to problematise them rather than accept them.", rewrite: light, force: should, status: drafted }
  forBeneficiary: { text: "At the typical standard, you should engage creatively and critically with the forms, techniques, traditions and histories of performance, and be able to question them.", rewrite: full, force: should, status: drafted }
  author-agent-written: "Treat this as the typical standard: what most honours graduates should show, above the minimum (should), in subject knowledge, understanding and skills, for a bachelor's degree with honours in the subject at FHEQ level 6 (FQHEIS level 10). Cite it as (QAA, 2024, Dance, Drama and Performance Subject Benchmark Statement, para 4.11.b1). Do not present it as the pass standard; the minimum is the threshold item. Set it beside the same outcome at the other rungs (4.8.b1, 4.14.b1), the honours descriptor qaa/fheq-2024/4.15.b1 with spine:6, and Annex D qaa/fheq-2024/annex-d/knowledge/r1/2.2 and qaa/fheq-2024/annex-d/knowledge/r1/2.1."
  author-agent-dialogue: "Raise it when a student who has the basics asks what solid work looks like here, or staff write criteria for the middle classes. Put it in plain words: second person for a student, and for staff as what a module lets students show. Ask: Which tradition or history of performance could you explain to a newcomer, and which do you know only by name? Never treat this as the pass mark."
- statement: qaa/dance-drama-and-performance-2024/4.11.b2
  forPractitioner: { text: "Ask students to work creatively and critically with performance's components and with every stage of a work's life.", rewrite: light, force: should, status: drafted }
  forBeneficiary: { text: "At the typical standard, you should work creatively and critically with the parts of a performance and with how a work is made, managed, shared and recorded.", rewrite: full, force: should, status: drafted }
  author-agent-written: "Treat this as the typical standard: what most honours graduates should show, above the minimum (should), in subject knowledge, understanding and skills, for a bachelor's degree with honours in the subject at FHEQ level 6 (FQHEIS level 10). Cite it as (QAA, 2024, Dance, Drama and Performance Subject Benchmark Statement, para 4.11.b2). Do not present it as the pass standard; the minimum is the threshold item. Set it beside the same outcome at the other rungs (4.8.b2, 4.14.b2), the honours descriptor qaa/fheq-2024/4.15.b1 with spine:6, and Annex D qaa/fheq-2024/annex-d/knowledge/r1/2.2 and qaa/fheq-2024/annex-d/knowledge/r1/2.1."
  author-agent-dialogue: "Raise it when a student who has the basics asks what solid work looks like here, or staff write criteria for the middle classes. Put it in plain words: second person for a student, and for staff as what a module lets students show. Ask: Can you trace one of your own pieces from first idea to its record afterwards? Never treat this as the pass mark."
- statement: qaa/dance-drama-and-performance-2024/4.11.b3
  forPractitioner: { text: "Expect students to engage with, not only know, the critical and theoretical approaches of the field.", rewrite: light, force: should, status: drafted }
  forBeneficiary: { text: "At the typical standard, you should engage actively with critical and theoretical ways of studying performance.", rewrite: full, force: should, status: drafted }
  author-agent-written: "Treat this as the typical standard: what most honours graduates should show, above the minimum (should), in subject knowledge, understanding and skills, for a bachelor's degree with honours in the subject at FHEQ level 6 (FQHEIS level 10). Cite it as (QAA, 2024, Dance, Drama and Performance Subject Benchmark Statement, para 4.11.b3). Do not present it as the pass standard; the minimum is the threshold item. Set it beside the same outcome at the other rungs (4.8.b3, 4.14.b3), the honours descriptor qaa/fheq-2024/4.15.b7 with spine:6, and Annex D qaa/fheq-2024/annex-d/knowledge/r2/2.2 and qaa/fheq-2024/annex-d/knowledge/r2/2.1."
  author-agent-dialogue: "Raise it when a student who has the basics asks what solid work looks like here, or staff write criteria for the middle classes. Put it in plain words: second person for a student, and for staff as what a module lets students show. Ask: Which critical or theoretical approach do you use most, and when did you last test it against another? Never treat this as the pass mark."
- statement: qaa/dance-drama-and-performance-2024/4.11.b4
  forPractitioner: { text: "Expect a critical grasp of key practitioners, practices or theorists in their cultural and historical settings.", rewrite: light, force: should, status: drafted }
  forBeneficiary: { text: "At the typical standard, you should understand key practitioners, practices or theorists critically, in their cultural or historical settings.", rewrite: full, force: should, status: drafted }
  author-agent-written: "Treat this as the typical standard: what most honours graduates should show, above the minimum (should), in subject knowledge, understanding and skills, for a bachelor's degree with honours in the subject at FHEQ level 6 (FQHEIS level 10). Cite it as (QAA, 2024, Dance, Drama and Performance Subject Benchmark Statement, para 4.11.b4). Do not present it as the pass standard; the minimum is the threshold item. Set it beside the same outcome at the other rungs (4.8.b4, 4.14.b4), the honours descriptor qaa/fheq-2024/4.15.b1 with spine:6, and Annex D qaa/fheq-2024/annex-d/knowledge/r1/2.2 and qaa/fheq-2024/annex-d/knowledge/r1/2.1."
  author-agent-dialogue: "Raise it when a student who has the basics asks what solid work looks like here, or staff write criteria for the middle classes. Put it in plain words: second person for a student, and for staff as what a module lets students show. Ask: Which practitioner shaped your work most, and what in their context explains their approach? Never treat this as the pass mark."
- statement: qaa/dance-drama-and-performance-2024/4.11.b5
  forPractitioner: { text: "Expect students to engage creatively and critically with performance's place in communities, education, participation and industry.", rewrite: light, force: should, status: drafted }
  forBeneficiary: { text: "At the typical standard, you should engage creatively and critically with what performance does in society, education, participatory work and the industry.", rewrite: full, force: should, status: drafted }
  author-agent-written: "Treat this as the typical standard: what most honours graduates should show, above the minimum (should), in subject knowledge, understanding and skills, for a bachelor's degree with honours in the subject at FHEQ level 6 (FQHEIS level 10). Cite it as (QAA, 2024, Dance, Drama and Performance Subject Benchmark Statement, para 4.11.b5). Do not present it as the pass standard; the minimum is the threshold item. Set it beside the same outcome at the other rungs (4.8.b5, 4.14.b5), the honours descriptor qaa/fheq-2024/4.15.b1 with spine:6, and Annex D qaa/fheq-2024/annex-d/knowledge/r1/2.2 and qaa/fheq-2024/annex-d/knowledge/r1/2.1."
  author-agent-dialogue: "Raise it when a student who has the basics asks what solid work looks like here, or staff write criteria for the middle classes. Put it in plain words: second person for a student, and for staff as what a module lets students show. Ask: Where have you seen performance do work outside the theatre, in a school, a community or an industry? Never treat this as the pass mark."
- statement: qaa/dance-drama-and-performance-2024/4.11.b6
  forPractitioner: { text: "Expect a strong grasp of how critical and creative enquiry work together.", rewrite: light, force: should, status: drafted }
  forBeneficiary: { text: "At the typical standard, you should have a strong understanding of how critical thinking and creative making feed into each other.", rewrite: full, force: should, status: drafted }
  author-agent-written: "Treat this as the typical standard: what most honours graduates should show, above the minimum (should), in subject knowledge, understanding and skills, for a bachelor's degree with honours in the subject at FHEQ level 6 (FQHEIS level 10). Cite it as (QAA, 2024, Dance, Drama and Performance Subject Benchmark Statement, para 4.11.b6). Do not present it as the pass standard; the minimum is the threshold item. Set it beside the same outcome at the other rungs (4.8.b6, 4.14.b6), the honours descriptor qaa/fheq-2024/4.15.b7 with spine:6, and Annex D qaa/fheq-2024/annex-d/cognitive/r2/2.2 and qaa/fheq-2024/annex-d/cognitive/r2/2.1."
  author-agent-dialogue: "Raise it when a student who has the basics asks what solid work looks like here, or staff write criteria for the middle classes. Put it in plain words: second person for a student, and for staff as what a module lets students show. Ask: When did critical reading last change something you made, or making change how you read? Never treat this as the pass mark."
- statement: qaa/dance-drama-and-performance-2024/4.11.b7
  forPractitioner: { text: "Expect students to interpret scripts, media, notation and scores critically as material for performance.", rewrite: light, force: should, status: drafted }
  forBeneficiary: { text: "At the typical standard, you should understand critically how to read and interpret scripts, media, notation or scores to make performance.", rewrite: full, force: should, status: drafted }
  author-agent-written: "Treat this as the typical standard: what most honours graduates should show, above the minimum (should), in subject knowledge, understanding and skills, for a bachelor's degree with honours in the subject at FHEQ level 6 (FQHEIS level 10). Cite it as (QAA, 2024, Dance, Drama and Performance Subject Benchmark Statement, para 4.11.b7). Do not present it as the pass standard; the minimum is the threshold item. Set it beside the same outcome at the other rungs (4.8.b7, 4.14.b7), the honours descriptor qaa/fheq-2024/4.15.b2 with spine:6, and Annex D qaa/fheq-2024/annex-d/knowledge/r2/2.2 and qaa/fheq-2024/annex-d/knowledge/r2/2.1."
  author-agent-dialogue: "Raise it when a student who has the basics asks what solid work looks like here, or staff write criteria for the middle classes. Put it in plain words: second person for a student, and for staff as what a module lets students show. Ask: How do you move from a script or score to choices in the room? Never treat this as the pass mark."
- statement: qaa/dance-drama-and-performance-2024/4.11.b8
  forPractitioner: { text: "Expect a creative and critical grasp of how groups and ensembles work.", rewrite: light, force: should, status: drafted }
  forBeneficiary: { text: "At the typical standard, you should understand group and ensemble work creatively and critically.", rewrite: full, force: should, status: drafted }
  author-agent-written: "Treat this as the typical standard: what most honours graduates should show, above the minimum (should), in subject knowledge, understanding and skills, for a bachelor's degree with honours in the subject at FHEQ level 6 (FQHEIS level 10). Cite it as (QAA, 2024, Dance, Drama and Performance Subject Benchmark Statement, para 4.11.b8). Do not present it as the pass standard; the minimum is the threshold item. Set it beside the same outcome at the other rungs (4.8.b8, 4.14.b8), the honours descriptor qaa/fheq-2024/4.15.b9.1 with spine:6, and Annex D qaa/fheq-2024/annex-d/transferable/r2/2.2 and qaa/fheq-2024/annex-d/transferable/r2/2.1."
  author-agent-dialogue: "Raise it when a student who has the basics asks what solid work looks like here, or staff write criteria for the middle classes. Put it in plain words: second person for a student, and for staff as what a module lets students show. Ask: What did your last group process teach you about how ensembles work? Never treat this as the pass mark."
- statement: qaa/dance-drama-and-performance-2024/4.11.b9
  forPractitioner: { text: "Expect students to understand performance's elements creatively and critically, the body included.", rewrite: light, force: should, status: drafted }
  forBeneficiary: { text: "At the typical standard, you should understand the building blocks of performance creatively and critically, including bodies, space, sound, text, movement and setting.", rewrite: full, force: should, status: drafted }
  author-agent-written: "Treat this as the typical standard: what most honours graduates should show, above the minimum (should), in subject knowledge, understanding and skills, for a bachelor's degree with honours in the subject at FHEQ level 6 (FQHEIS level 10). Cite it as (QAA, 2024, Dance, Drama and Performance Subject Benchmark Statement, para 4.11.b9). Do not present it as the pass standard; the minimum is the threshold item. Set it beside the same outcome at the other rungs (4.8.b9, 4.14.b9), the honours descriptor qaa/fheq-2024/4.15.b1 with spine:6, and Annex D qaa/fheq-2024/annex-d/knowledge/r2/2.2 and qaa/fheq-2024/annex-d/knowledge/r2/2.1."
  author-agent-dialogue: "Raise it when a student who has the basics asks what solid work looks like here, or staff write criteria for the middle classes. Put it in plain words: second person for a student, and for staff as what a module lets students show. Ask: Which element of performance do you tend to overlook, and what happens when you put it first? Never treat this as the pass mark."
- statement: qaa/dance-drama-and-performance-2024/4.11.b10
  forPractitioner: { text: "Expect students to understand, creatively and critically, which interdisciplinary elements suit their work and how to draw on other fields.", rewrite: light, force: should, status: drafted }
  forBeneficiary: { text: "At the typical standard, you should understand creatively and critically how ideas, methods and skills from other subjects can be used in performance.", rewrite: full, force: should, status: drafted }
  author-agent-written: "Treat this as the typical standard: what most honours graduates should show, above the minimum (should), in subject knowledge, understanding and skills, for a bachelor's degree with honours in the subject at FHEQ level 6 (FQHEIS level 10). Cite it as (QAA, 2024, Dance, Drama and Performance Subject Benchmark Statement, para 4.11.b10). Do not present it as the pass standard; the minimum is the threshold item. Set it beside the same outcome at the other rungs (4.8.b10, 4.14.b10), the honours descriptor qaa/fheq-2024/4.15.b3.1 with spine:6, and Annex D qaa/fheq-2024/annex-d/knowledge/r2/2.2 and qaa/fheq-2024/annex-d/knowledge/r2/2.1."
  author-agent-dialogue: "Raise it when a student who has the basics asks what solid work looks like here, or staff write criteria for the middle classes. Put it in plain words: second person for a student, and for staff as what a module lets students show. Ask: Which idea from another discipline has changed your practice, and how did you apply it? Never treat this as the pass mark."
- statement: qaa/dance-drama-and-performance-2024/4.11.b11
  forPractitioner: { text: "Expect a critical grasp of the practitioner's duty to work safely, sustainably and ethically.", rewrite: light, force: should, status: drafted }
  forBeneficiary: { text: "At the typical standard, you should understand critically your duty to work safely, sustainably and ethically when making performance.", rewrite: full, force: should, status: drafted }
  author-agent-written: "Treat this as the typical standard: what most honours graduates should show, above the minimum (should), in subject knowledge, understanding and skills, for a bachelor's degree with honours in the subject at FHEQ level 6 (FQHEIS level 10). Cite it as (QAA, 2024, Dance, Drama and Performance Subject Benchmark Statement, para 4.11.b11). Do not present it as the pass standard; the minimum is the threshold item. Set it beside the same outcome at the other rungs (4.8.b12, 4.14.b11), the honours descriptor qaa/fheq-2024/4.15.b9.2 with spine:6, and Annex D qaa/fheq-2024/annex-d/transferable/r4/2.2 and qaa/fheq-2024/annex-d/transferable/r4/2.1."
  author-agent-dialogue: "Raise it when a student who has the basics asks what solid work looks like here, or staff write criteria for the middle classes. Put it in plain words: second person for a student, and for staff as what a module lets students show. Ask: How did you make your last project safe, ethical and environmentally sound? Never treat this as the pass mark."
- statement: qaa/dance-drama-and-performance-2024/4.12.b1
  forPractitioner: { text: "Expect students to choose, refine and present performance and production skills with creative and critical judgement.", rewrite: light, force: should, status: drafted }
  forBeneficiary: { text: "At the typical standard, you should be able to work creatively and critically with performance and production skills, choosing, refining and presenting them in your work.", rewrite: full, force: should, status: drafted }
  author-agent-written: "Treat this as the typical standard: what most honours graduates should show, above the minimum (should), in subject-specific skills, for a bachelor's degree with honours in the subject at FHEQ level 6 (FQHEIS level 10). Cite it as (QAA, 2024, Dance, Drama and Performance Subject Benchmark Statement, para 4.12.b1). Do not present it as the pass standard; the minimum is the threshold item. Set it beside the same outcome at the other rungs (4.15.b1), the honours descriptor qaa/fheq-2024/4.15.b2 with spine:6, and Annex D qaa/fheq-2024/annex-d/practical/r3/2.2 and qaa/fheq-2024/annex-d/practical/r3/2.1."
  author-agent-dialogue: "Raise it when a student who has the basics asks what solid work looks like here, or staff write criteria for the middle classes. Put it in plain words: second person for a student, and for staff as what a module lets students show. Ask: Which of your skills do you choose to show first, and how have you refined it? Never treat this as the pass mark."
- statement: qaa/dance-drama-and-performance-2024/4.12.b2
  forPractitioner: { text: "Expect sensitive, creative and critical realisation of texts, stimuli, notation or scores in design and performance.", rewrite: light, force: should, status: drafted }
  forBeneficiary: { text: "At the typical standard, you should be able to work creatively and critically with what a script, prompt, notation or score offers and bring it to life with sensitivity through design and performance.", rewrite: full, force: should, status: drafted }
  author-agent-written: "Treat this as the typical standard: what most honours graduates should show, above the minimum (should), in subject-specific skills, for a bachelor's degree with honours in the subject at FHEQ level 6 (FQHEIS level 10). Cite it as (QAA, 2024, Dance, Drama and Performance Subject Benchmark Statement, para 4.12.b2). Do not present it as the pass standard; the minimum is the threshold item. Set it beside the same outcome at the other rungs (4.9.b2, 4.15.b2), the honours descriptor qaa/fheq-2024/4.15.b2 with spine:6, and Annex D qaa/fheq-2024/annex-d/practical/r3/2.2 and qaa/fheq-2024/annex-d/practical/r3/2.1."
  author-agent-dialogue: "Raise it when a student who has the basics asks what solid work looks like here, or staff write criteria for the middle classes. Put it in plain words: second person for a student, and for staff as what a module lets students show. Ask: What did the last text or score you worked on make possible, and what did you do with it? Never treat this as the pass mark."
- statement: qaa/dance-drama-and-performance-2024/4.12.b3
  forPractitioner: { text: "Expect students to make or produce work creatively and critically, drawing on a developed command of the field's vocabularies and methods.", rewrite: light, force: should, status: drafted }
  forBeneficiary: { text: "At the typical standard, you should be able to make or produce performance creatively and critically, with a developed grasp of the techniques, crafts and working methods involved.", rewrite: full, force: should, status: drafted }
  author-agent-written: "Treat this as the typical standard: what most honours graduates should show, above the minimum (should), in subject-specific skills, for a bachelor's degree with honours in the subject at FHEQ level 6 (FQHEIS level 10). Cite it as (QAA, 2024, Dance, Drama and Performance Subject Benchmark Statement, para 4.12.b3). Do not present it as the pass standard; the minimum is the threshold item. Set it beside the same outcome at the other rungs (4.9.b1, 4.15.b3), the honours descriptor qaa/fheq-2024/4.15.b2 with spine:6, and Annex D qaa/fheq-2024/annex-d/practical/r3/2.2 and qaa/fheq-2024/annex-d/practical/r3/2.1."
  author-agent-dialogue: "Raise it when a student who has the basics asks what solid work looks like here, or staff write criteria for the middle classes. Put it in plain words: second person for a student, and for staff as what a module lets students show. Ask: Which working methods could you use to make a piece from scratch without being shown? Never treat this as the pass mark."
- statement: qaa/dance-drama-and-performance-2024/4.12.b4
  forPractitioner: { text: "Expect independent research that is creative and critical, historical or practice-based.", rewrite: light, force: should, status: drafted }
  forBeneficiary: { text: "At the typical standard, you should be able to research on your own creatively and critically, whether into past or present performance or as part of making new work.", rewrite: full, force: should, status: drafted }
  author-agent-written: "Treat this as the typical standard: what most honours graduates should show, above the minimum (should), in subject-specific skills, for a bachelor's degree with honours in the subject at FHEQ level 6 (FQHEIS level 10). Cite it as (QAA, 2024, Dance, Drama and Performance Subject Benchmark Statement, para 4.12.b4). Do not present it as the pass standard; the minimum is the threshold item. Set it beside the same outcome at the other rungs (4.9.b5, 4.15.b4), the honours descriptor qaa/fheq-2024/4.15.b6 with spine:6, and Annex D qaa/fheq-2024/annex-d/knowledge/r3/2.2 and qaa/fheq-2024/annex-d/knowledge/r3/2.1."
  author-agent-dialogue: "Raise it when a student who has the basics asks what solid work looks like here, or staff write criteria for the middle classes. Put it in plain words: second person for a student, and for staff as what a module lets students show. Ask: What question did your last independent research answer, and where did you find the evidence? Never treat this as the pass mark."
- statement: qaa/dance-drama-and-performance-2024/4.12.b5
  forPractitioner: { text: "Expect students to interpret, not only name, the cultural frameworks of performance events and link them to social and historical context.", rewrite: light, force: should, status: drafted }
  forBeneficiary: { text: "At the typical standard, you should be able to identify and interpret the cultural frameworks around a performance and how they link to its social and historical setting.", rewrite: full, force: should, status: drafted }
  author-agent-written: "Treat this as the typical standard: what most honours graduates should show, above the minimum (should), in subject-specific skills, for a bachelor's degree with honours in the subject at FHEQ level 6 (FQHEIS level 10). Cite it as (QAA, 2024, Dance, Drama and Performance Subject Benchmark Statement, para 4.12.b5). Do not present it as the pass standard; the minimum is the threshold item. Set it beside the same outcome at the other rungs (4.9.b6, 4.15.b5), the honours descriptor qaa/fheq-2024/4.15.b7 with spine:6, and Annex D qaa/fheq-2024/annex-d/cognitive/r1/2.2 and qaa/fheq-2024/annex-d/cognitive/r1/2.1."
  author-agent-dialogue: "Raise it when a student who has the basics asks what solid work looks like here, or staff write criteria for the middle classes. Put it in plain words: second person for a student, and for staff as what a module lets students show. Ask: What cultural frame shapes the piece you are working on now? Never treat this as the pass mark."
- statement: qaa/dance-drama-and-performance-2024/4.13.b1
  forPractitioner: { text: "Expect critical, analytical development of ideas and arguments, judged and presented in several forms.", rewrite: light, force: should, status: drafted }
  forBeneficiary: { text: "At the typical standard, you should be able to develop ideas and arguments critically and analytically, and judge and present them in different ways.", rewrite: full, force: should, status: drafted }
  author-agent-written: "Treat this as the typical standard: what most honours graduates should show, above the minimum (should), in generic and graduate skills, for a bachelor's degree with honours in the subject at FHEQ level 6 (FQHEIS level 10). Cite it as (QAA, 2024, Dance, Drama and Performance Subject Benchmark Statement, para 4.13.b1). Do not present it as the pass standard; the minimum is the threshold item. Set it beside the same outcome at the other rungs (4.10.b4, 4.16.b1), the honours descriptor qaa/fheq-2024/4.15.b3.1 with spine:6, and Annex D qaa/fheq-2024/annex-d/cognitive/r2/2.2 and qaa/fheq-2024/annex-d/cognitive/r2/2.1."
  author-agent-dialogue: "Raise it when a student who has the basics asks what solid work looks like here, or staff write criteria for the middle classes. Put it in plain words: second person for a student, and for staff as what a module lets students show. Ask: What is the strongest argument you have built this year, and how did you present it? Never treat this as the pass mark."
- statement: qaa/dance-drama-and-performance-2024/4.13.b2
  forPractitioner: { text: "Expect students to analyse how forms of discourse shape representation and reception in the arts and culture.", rewrite: light, force: should, status: drafted }
  forBeneficiary: { text: "At the typical standard, you should be able to examine and judge different kinds of discourse and how they shape representation and reception in the arts and culture.", rewrite: full, force: should, status: drafted }
  author-agent-written: "Treat this as the typical standard: what most honours graduates should show, above the minimum (should), in generic and graduate skills, for a bachelor's degree with honours in the subject at FHEQ level 6 (FQHEIS level 10). Cite it as (QAA, 2024, Dance, Drama and Performance Subject Benchmark Statement, para 4.13.b2). Do not present it as the pass standard; the minimum is the threshold item. Set it beside the same outcome at the other rungs (4.16.b2), the honours descriptor qaa/fheq-2024/4.15.b7 with spine:6, and Annex D qaa/fheq-2024/annex-d/cognitive/r2/2.2 and qaa/fheq-2024/annex-d/cognitive/r2/2.1."
  author-agent-dialogue: "Raise it when a student who has the basics asks what solid work looks like here, or staff write criteria for the middle classes. Put it in plain words: second person for a student, and for staff as what a module lets students show. Ask: How does the way something is talked about shape how audiences receive it? Never treat this as the pass mark."
- statement: qaa/dance-drama-and-performance-2024/4.13.b3
  forPractitioner: { text: "Expect productive, imaginative group work and the creative skills to complete practice-based projects.", rewrite: light, force: should, status: drafted }
  forBeneficiary: { text: "At the typical standard, you should be able to work productively and imaginatively in a group and have the creative skills to complete practical projects.", rewrite: full, force: should, status: drafted }
  author-agent-written: "Treat this as the typical standard: what most honours graduates should show, above the minimum (should), in generic and graduate skills, for a bachelor's degree with honours in the subject at FHEQ level 6 (FQHEIS level 10). Cite it as (QAA, 2024, Dance, Drama and Performance Subject Benchmark Statement, para 4.13.b3). Do not present it as the pass standard; the minimum is the threshold item. Set it beside the same outcome at the other rungs (4.10.b5, 4.16.b3), the honours descriptor qaa/fheq-2024/4.15.b9.1 with spine:6, and Annex D qaa/fheq-2024/annex-d/transferable/r2/2.2 and qaa/fheq-2024/annex-d/transferable/r2/2.1."
  author-agent-dialogue: "Raise it when a student who has the basics asks what solid work looks like here, or staff write criteria for the middle classes. Put it in plain words: second person for a student, and for staff as what a module lets students show. Ask: What did you contribute to your last group project that no one else did? Never treat this as the pass mark."
- statement: qaa/dance-drama-and-performance-2024/4.13.b4
  forPractitioner: { text: "Expect students to manage their own workload, meet deadlines and negotiate and achieve goals with others.", rewrite: light, force: should, status: drafted }
  forBeneficiary: { text: "At the typical standard, you should be able to manage your own workload well, meet deadlines and agree and reach goals with others.", rewrite: full, force: should, status: drafted }
  author-agent-written: "Treat this as the typical standard: what most honours graduates should show, above the minimum (should), in generic and graduate skills, for a bachelor's degree with honours in the subject at FHEQ level 6 (FQHEIS level 10). Cite it as (QAA, 2024, Dance, Drama and Performance Subject Benchmark Statement, para 4.13.b4). Do not present it as the pass standard; the minimum is the threshold item. Set it beside the same outcome at the other rungs (4.10.b1, 4.16.b4), the honours descriptor qaa/fheq-2024/4.15.b5 with spine:6, and Annex D qaa/fheq-2024/annex-d/transferable/r3/2.2 and qaa/fheq-2024/annex-d/transferable/r3/2.1."
  author-agent-dialogue: "Raise it when a student who has the basics asks what solid work looks like here, or staff write criteria for the middle classes. Put it in plain words: second person for a student, and for staff as what a module lets students show. Ask: How do you plan your time when rehearsals and deadlines collide? Never treat this as the pass mark."
- statement: qaa/dance-drama-and-performance-2024/4.13.b5
  forPractitioner: { text: "Expect constructive, effective handling of creative and interpersonal issues in group work.", rewrite: light, force: should, status: drafted }
  forBeneficiary: { text: "At the typical standard, you should be able to deal constructively and effectively with creative, personal and interpersonal issues in creative work.", rewrite: full, force: should, status: drafted }
  author-agent-written: "Treat this as the typical standard: what most honours graduates should show, above the minimum (should), in generic and graduate skills, for a bachelor's degree with honours in the subject at FHEQ level 6 (FQHEIS level 10). Cite it as (QAA, 2024, Dance, Drama and Performance Subject Benchmark Statement, para 4.13.b5). Do not present it as the pass standard; the minimum is the threshold item. Set it beside the same outcome at the other rungs (4.10.b6, 4.16.b5), the honours descriptor qaa/fheq-2024/4.15.b9.1 with spine:6, and Annex D qaa/fheq-2024/annex-d/transferable/r2/2.2 and qaa/fheq-2024/annex-d/transferable/r2/2.1."
  author-agent-dialogue: "Raise it when a student who has the basics asks what solid work looks like here, or staff write criteria for the middle classes. Put it in plain words: second person for a student, and for staff as what a module lets students show. Ask: How did you handle a disagreement in a creative team? Never treat this as the pass mark."
- statement: qaa/dance-drama-and-performance-2024/4.13.b6
  forPractitioner: { text: "Expect independent searching and organising of material, with critical judgement of its value.", rewrite: light, force: should, status: drafted }
  forBeneficiary: { text: "At the typical standard, you should be able to find, sift and organise material on your own and judge critically how much it matters.", rewrite: full, force: should, status: drafted }
  author-agent-written: "Treat this as the typical standard: what most honours graduates should show, above the minimum (should), in generic and graduate skills, for a bachelor's degree with honours in the subject at FHEQ level 6 (FQHEIS level 10). Cite it as (QAA, 2024, Dance, Drama and Performance Subject Benchmark Statement, para 4.13.b6). Do not present it as the pass standard; the minimum is the threshold item. Set it beside the same outcome at the other rungs (4.10.b8, 4.16.b6), the honours descriptor qaa/fheq-2024/4.15.b5 with spine:6, and Annex D qaa/fheq-2024/annex-d/cognitive/r1/2.2 and qaa/fheq-2024/annex-d/cognitive/r1/2.1."
  author-agent-dialogue: "Raise it when a student who has the basics asks what solid work looks like here, or staff write criteria for the middle classes. Put it in plain words: second person for a student, and for staff as what a module lets students show. Ask: How do you decide which sources to keep and which to drop? Never treat this as the pass mark."
- statement: qaa/dance-drama-and-performance-2024/4.13.b7
  forPractitioner: { text: "Expect sound digital skills and an informed view of how technology serves the field.", rewrite: light, force: should, status: drafted }
  forBeneficiary: { text: "At the typical standard, you should have suitable technical and digital skills and a good sense of how they can be used in your field.", rewrite: full, force: should, status: drafted }
  author-agent-written: "Treat this as the typical standard: what most honours graduates should show, above the minimum (should), in generic and graduate skills, for a bachelor's degree with honours in the subject at FHEQ level 6 (FQHEIS level 10). Cite it as (QAA, 2024, Dance, Drama and Performance Subject Benchmark Statement, para 4.13.b7). Do not present it as the pass standard; the minimum is the threshold item. Set it beside the same outcome at the other rungs (4.10.b9, 4.16.b7), the honours descriptor qaa/fheq-2024/4.15.b6 with spine:6, and Annex D qaa/fheq-2024/annex-d/transferable/r1/2.2 and qaa/fheq-2024/annex-d/transferable/r1/2.1."
  author-agent-dialogue: "Raise it when a student who has the basics asks what solid work looks like here, or staff write criteria for the middle classes. Put it in plain words: second person for a student, and for staff as what a module lets students show. Ask: Which digital tool have you adapted for your own creative purpose? Never treat this as the pass mark."
- statement: qaa/dance-drama-and-performance-2024/4.13.b8
  forPractitioner: { text: "Expect students to choose the right numeracy skills for practical and creative problems.", rewrite: light, force: should, status: drafted }
  forBeneficiary: { text: "At the typical standard, you should be able to pick and use the right number skills to solve problems and make creative work happen.", rewrite: full, force: should, status: drafted }
  author-agent-written: "Treat this as the typical standard: what most honours graduates should show, above the minimum (should), in generic and graduate skills, for a bachelor's degree with honours in the subject at FHEQ level 6 (FQHEIS level 10). Cite it as (QAA, 2024, Dance, Drama and Performance Subject Benchmark Statement, para 4.13.b8). Do not present it as the pass standard; the minimum is the threshold item. Set it beside the same outcome at the other rungs (4.10.b11, 4.16.b8), the honours descriptor qaa/fheq-2024/4.15.b3.1 with spine:6, and Annex D qaa/fheq-2024/annex-d/transferable/r1/2.2 and qaa/fheq-2024/annex-d/transferable/r1/2.1."
  author-agent-dialogue: "Raise it when a student who has the basics asks what solid work looks like here, or staff write criteria for the middle classes. Put it in plain words: second person for a student, and for staff as what a module lets students show. Ask: Where did numbers matter in your last production, for example a budget, a schedule or a lighting plot? Never treat this as the pass mark."
- statement: qaa/dance-drama-and-performance-2024/4.14.b1
  forPractitioner: { text: "Look for sophisticated engagement with the art form's forms, techniques, traditions and histories, interrogating them.", rewrite: light, force: should, status: drafted }
  forBeneficiary: { text: "At the excellent standard, you should engage with the forms, techniques, traditions and histories of performance in a sophisticated way and question them closely.", rewrite: full, force: should, status: drafted }
  author-agent-written: "Treat this as the excellent standard: what the strongest honours graduates should show, an aspiration rather than a requirement (should), in subject knowledge, understanding and skills, for a bachelor's degree with honours in the subject at FHEQ level 6 (FQHEIS level 10). Cite it as (QAA, 2024, Dance, Drama and Performance Subject Benchmark Statement, para 4.14.b1). Do not present it as the minimum or as expected of every student. Set it beside the same outcome at the other rungs (4.8.b1, 4.11.b1), the honours descriptor qaa/fheq-2024/4.15.b1 with spine:6, and Annex D qaa/fheq-2024/annex-d/knowledge/r1/1st."
  author-agent-dialogue: "Raise it when a student aims for a first, or staff describe what first-class work looks like in this area. Put it in plain words: second person for a student, and for staff as what a module lets students show. Ask: Which tradition or history of performance could you explain to a newcomer, and which do you know only by name? Never present this as what everyone must reach."
- statement: qaa/dance-drama-and-performance-2024/4.14.b2
  forPractitioner: { text: "Look for sophisticated creative and theoretical work across performance's components and a work's whole life, leading to fresh insight.", rewrite: light, force: should, status: drafted }
  forBeneficiary: { text: "At the excellent standard, you should work with the parts of a performance and the whole life of a work in a sophisticated creative and theoretical way that produces new insight.", rewrite: full, force: should, status: drafted }
  author-agent-written: "Treat this as the excellent standard: what the strongest honours graduates should show, an aspiration rather than a requirement (should), in subject knowledge, understanding and skills, for a bachelor's degree with honours in the subject at FHEQ level 6 (FQHEIS level 10). Cite it as (QAA, 2024, Dance, Drama and Performance Subject Benchmark Statement, para 4.14.b2). Do not present it as the minimum or as expected of every student. Set it beside the same outcome at the other rungs (4.8.b2, 4.11.b2), the honours descriptor qaa/fheq-2024/4.15.b1 with spine:6, and Annex D qaa/fheq-2024/annex-d/knowledge/r1/1st."
  author-agent-dialogue: "Raise it when a student aims for a first, or staff describe what first-class work looks like in this area. Put it in plain words: second person for a student, and for staff as what a module lets students show. Ask: Can you trace one of your own pieces from first idea to its record afterwards? Never present this as what everyone must reach."
- statement: qaa/dance-drama-and-performance-2024/4.14.b3
  forPractitioner: { text: "Look for a sophisticated handling of the field's critical and theoretical approaches.", rewrite: light, force: should, status: drafted }
  forBeneficiary: { text: "At the excellent standard, you should handle critical and theoretical ways of studying performance in a sophisticated way.", rewrite: full, force: should, status: drafted }
  author-agent-written: "Treat this as the excellent standard: what the strongest honours graduates should show, an aspiration rather than a requirement (should), in subject knowledge, understanding and skills, for a bachelor's degree with honours in the subject at FHEQ level 6 (FQHEIS level 10). Cite it as (QAA, 2024, Dance, Drama and Performance Subject Benchmark Statement, para 4.14.b3). Do not present it as the minimum or as expected of every student. Set it beside the same outcome at the other rungs (4.8.b3, 4.11.b3), the honours descriptor qaa/fheq-2024/4.15.b7 with spine:6, and Annex D qaa/fheq-2024/annex-d/knowledge/r2/1st."
  author-agent-dialogue: "Raise it when a student aims for a first, or staff describe what first-class work looks like in this area. Put it in plain words: second person for a student, and for staff as what a module lets students show. Ask: Which critical or theoretical approach do you use most, and when did you last test it against another? Never present this as what everyone must reach."
- statement: qaa/dance-drama-and-performance-2024/4.14.b4
  forPractitioner: { text: "Look for a comprehensive, critical grasp of key practitioners, practices or theorists in context.", rewrite: light, force: should, status: drafted }
  forBeneficiary: { text: "At the excellent standard, you should have a full and critical understanding of key practitioners, practices or theorists in their cultural or historical settings.", rewrite: full, force: should, status: drafted }
  author-agent-written: "Treat this as the excellent standard: what the strongest honours graduates should show, an aspiration rather than a requirement (should), in subject knowledge, understanding and skills, for a bachelor's degree with honours in the subject at FHEQ level 6 (FQHEIS level 10). Cite it as (QAA, 2024, Dance, Drama and Performance Subject Benchmark Statement, para 4.14.b4). Do not present it as the minimum or as expected of every student. Set it beside the same outcome at the other rungs (4.8.b4, 4.11.b4), the honours descriptor qaa/fheq-2024/4.15.b1 with spine:6, and Annex D qaa/fheq-2024/annex-d/knowledge/r1/1st."
  author-agent-dialogue: "Raise it when a student aims for a first, or staff describe what first-class work looks like in this area. Put it in plain words: second person for a student, and for staff as what a module lets students show. Ask: Which practitioner shaped your work most, and what in their context explains their approach? Never present this as what everyone must reach."
- statement: qaa/dance-drama-and-performance-2024/4.14.b5
  forPractitioner: { text: "Look for sophisticated engagement with performance's place in communities, education, participation and industry.", rewrite: light, force: should, status: drafted }
  forBeneficiary: { text: "At the excellent standard, you should engage in a sophisticated way with what performance does in society, education, participatory work and the industry.", rewrite: full, force: should, status: drafted }
  author-agent-written: "Treat this as the excellent standard: what the strongest honours graduates should show, an aspiration rather than a requirement (should), in subject knowledge, understanding and skills, for a bachelor's degree with honours in the subject at FHEQ level 6 (FQHEIS level 10). Cite it as (QAA, 2024, Dance, Drama and Performance Subject Benchmark Statement, para 4.14.b5). Do not present it as the minimum or as expected of every student. Set it beside the same outcome at the other rungs (4.8.b5, 4.11.b5), the honours descriptor qaa/fheq-2024/4.15.b1 with spine:6, and Annex D qaa/fheq-2024/annex-d/knowledge/r1/1st."
  author-agent-dialogue: "Raise it when a student aims for a first, or staff describe what first-class work looks like in this area. Put it in plain words: second person for a student, and for staff as what a module lets students show. Ask: Where have you seen performance do work outside the theatre, in a school, a community or an industry? Never present this as what everyone must reach."
- statement: qaa/dance-drama-and-performance-2024/4.14.b6
  forPractitioner: { text: "Look for a sophisticated grasp of how critical and creative enquiry work together.", rewrite: light, force: should, status: drafted }
  forBeneficiary: { text: "At the excellent standard, you should have a sophisticated understanding of how critical thinking and creative making feed into each other.", rewrite: full, force: should, status: drafted }
  author-agent-written: "Treat this as the excellent standard: what the strongest honours graduates should show, an aspiration rather than a requirement (should), in subject knowledge, understanding and skills, for a bachelor's degree with honours in the subject at FHEQ level 6 (FQHEIS level 10). Cite it as (QAA, 2024, Dance, Drama and Performance Subject Benchmark Statement, para 4.14.b6). Do not present it as the minimum or as expected of every student. Set it beside the same outcome at the other rungs (4.8.b6, 4.11.b6), the honours descriptor qaa/fheq-2024/4.15.b7 with spine:6, and Annex D qaa/fheq-2024/annex-d/cognitive/r2/1st."
  author-agent-dialogue: "Raise it when a student aims for a first, or staff describe what first-class work looks like in this area. Put it in plain words: second person for a student, and for staff as what a module lets students show. Ask: When did critical reading last change something you made, or making change how you read? Never present this as what everyone must reach."
- statement: qaa/dance-drama-and-performance-2024/4.14.b7
  forPractitioner: { text: "Look for sophisticated interpretation of scripts, media, dance notation and scores as material for performance.", rewrite: light, force: should, status: drafted }
  forBeneficiary: { text: "At the excellent standard, you should understand in a sophisticated way how to read and interpret scripts, media, dance notation or scores to make performance.", rewrite: full, force: should, status: drafted }
  author-agent-written: "Treat this as the excellent standard: what the strongest honours graduates should show, an aspiration rather than a requirement (should), in subject knowledge, understanding and skills, for a bachelor's degree with honours in the subject at FHEQ level 6 (FQHEIS level 10). Cite it as (QAA, 2024, Dance, Drama and Performance Subject Benchmark Statement, para 4.14.b7). Do not present it as the minimum or as expected of every student. Set it beside the same outcome at the other rungs (4.8.b7, 4.11.b7), the honours descriptor qaa/fheq-2024/4.15.b2 with spine:6, and Annex D qaa/fheq-2024/annex-d/knowledge/r2/1st."
  author-agent-dialogue: "Raise it when a student aims for a first, or staff describe what first-class work looks like in this area. Put it in plain words: second person for a student, and for staff as what a module lets students show. Ask: How do you move from a script or score to choices in the room? Never present this as what everyone must reach."
- statement: qaa/dance-drama-and-performance-2024/4.14.b8
  forPractitioner: { text: "Look for a sophisticated critical grasp of group processes, shown in how students use them.", rewrite: light, force: should, status: drafted }
  forBeneficiary: { text: "At the excellent standard, you should understand group processes in a sophisticated, critical way and put that understanding to use.", rewrite: full, force: should, status: drafted }
  author-agent-written: "Treat this as the excellent standard: what the strongest honours graduates should show, an aspiration rather than a requirement (should), in subject knowledge, understanding and skills, for a bachelor's degree with honours in the subject at FHEQ level 6 (FQHEIS level 10). Cite it as (QAA, 2024, Dance, Drama and Performance Subject Benchmark Statement, para 4.14.b8). Do not present it as the minimum or as expected of every student. Set it beside the same outcome at the other rungs (4.8.b8, 4.11.b8), the honours descriptor qaa/fheq-2024/4.15.b9.1 with spine:6, and Annex D qaa/fheq-2024/annex-d/transferable/r2/1st."
  author-agent-dialogue: "Raise it when a student aims for a first, or staff describe what first-class work looks like in this area. Put it in plain words: second person for a student, and for staff as what a module lets students show. Ask: What did your last group process teach you about how ensembles work? Never present this as what everyone must reach."
- statement: qaa/dance-drama-and-performance-2024/4.14.b9
  forPractitioner: { text: "Look for a sophisticated critical grasp of performance's elements, the body included.", rewrite: light, force: should, status: drafted }
  forBeneficiary: { text: "At the excellent standard, you should understand the building blocks of performance in a sophisticated, critical way, including the body, space, sound, text, movement and setting.", rewrite: full, force: should, status: drafted }
  author-agent-written: "Treat this as the excellent standard: what the strongest honours graduates should show, an aspiration rather than a requirement (should), in subject knowledge, understanding and skills, for a bachelor's degree with honours in the subject at FHEQ level 6 (FQHEIS level 10). Cite it as (QAA, 2024, Dance, Drama and Performance Subject Benchmark Statement, para 4.14.b9). Do not present it as the minimum or as expected of every student. Set it beside the same outcome at the other rungs (4.8.b9, 4.11.b9), the honours descriptor qaa/fheq-2024/4.15.b1 with spine:6, and Annex D qaa/fheq-2024/annex-d/knowledge/r2/1st."
  author-agent-dialogue: "Raise it when a student aims for a first, or staff describe what first-class work looks like in this area. Put it in plain words: second person for a student, and for staff as what a module lets students show. Ask: Which element of performance do you tend to overlook, and what happens when you put it first? Never present this as what everyone must reach."
- statement: qaa/dance-drama-and-performance-2024/4.14.b10
  forPractitioner: { text: "Look for a sophisticated critical grasp of interdisciplinary elements and of drawing on other fields.", rewrite: light, force: should, status: drafted }
  forBeneficiary: { text: "At the excellent standard, you should understand in a sophisticated, critical way how ideas, methods and skills from other subjects can be used in performance.", rewrite: full, force: should, status: drafted }
  author-agent-written: "Treat this as the excellent standard: what the strongest honours graduates should show, an aspiration rather than a requirement (should), in subject knowledge, understanding and skills, for a bachelor's degree with honours in the subject at FHEQ level 6 (FQHEIS level 10). Cite it as (QAA, 2024, Dance, Drama and Performance Subject Benchmark Statement, para 4.14.b10). Do not present it as the minimum or as expected of every student. Set it beside the same outcome at the other rungs (4.8.b10, 4.11.b10), the honours descriptor qaa/fheq-2024/4.15.b3.1 with spine:6, and Annex D qaa/fheq-2024/annex-d/knowledge/r2/1st."
  author-agent-dialogue: "Raise it when a student aims for a first, or staff describe what first-class work looks like in this area. Put it in plain words: second person for a student, and for staff as what a module lets students show. Ask: Which idea from another discipline has changed your practice, and how did you apply it? Never present this as what everyone must reach."
- statement: qaa/dance-drama-and-performance-2024/4.14.b11
  forPractitioner: { text: "Look for a comprehensive grasp of the practitioner's duty to work safely, sustainably and ethically.", rewrite: light, force: should, status: drafted }
  forBeneficiary: { text: "At the excellent standard, you should have a full understanding of your duty to work safely, sustainably and ethically when making performance.", rewrite: full, force: should, status: drafted }
  author-agent-written: "Treat this as the excellent standard: what the strongest honours graduates should show, an aspiration rather than a requirement (should), in subject knowledge, understanding and skills, for a bachelor's degree with honours in the subject at FHEQ level 6 (FQHEIS level 10). Cite it as (QAA, 2024, Dance, Drama and Performance Subject Benchmark Statement, para 4.14.b11). Do not present it as the minimum or as expected of every student. Set it beside the same outcome at the other rungs (4.8.b12, 4.11.b11), the honours descriptor qaa/fheq-2024/4.15.b9.2 with spine:6, and Annex D qaa/fheq-2024/annex-d/transferable/r4/1st."
  author-agent-dialogue: "Raise it when a student aims for a first, or staff describe what first-class work looks like in this area. Put it in plain words: second person for a student, and for staff as what a module lets students show. Ask: How did you make your last project safe, ethical and environmentally sound? Never present this as what everyone must reach."
- statement: qaa/dance-drama-and-performance-2024/4.15.b1
  forPractitioner: { text: "Look for critical, thorough command of performance and production processes in what students select, refine and present.", rewrite: light, force: should, status: drafted }
  forBeneficiary: { text: "At the excellent standard, you should be able to handle performance and production processes with critical depth and thoroughness, choosing, refining and presenting them in your work.", rewrite: full, force: should, status: drafted }
  author-agent-written: "Treat this as the excellent standard: what the strongest honours graduates should show, an aspiration rather than a requirement (should), in subject-specific skills, for a bachelor's degree with honours in the subject at FHEQ level 6 (FQHEIS level 10). Cite it as (QAA, 2024, Dance, Drama and Performance Subject Benchmark Statement, para 4.15.b1). Do not present it as the minimum or as expected of every student. Set it beside the same outcome at the other rungs (4.12.b1), the honours descriptor qaa/fheq-2024/4.15.b2 with spine:6, and Annex D qaa/fheq-2024/annex-d/practical/r3/1st."
  author-agent-dialogue: "Raise it when a student aims for a first, or staff describe what first-class work looks like in this area. Put it in plain words: second person for a student, and for staff as what a module lets students show. Ask: Which of your skills do you choose to show first, and how have you refined it? Never present this as what everyone must reach."
- statement: qaa/dance-drama-and-performance-2024/4.15.b2
  forPractitioner: { text: "Look for thorough, sensitive realisation of texts, notation or scores that leads to new or original work.", rewrite: light, force: should, status: drafted }
  forBeneficiary: { text: "At the excellent standard, you should be able to explore thoroughly and creatively what a script, notation or score offers and bring it to life with sensitivity, creating new or original work.", rewrite: full, force: should, status: drafted }
  author-agent-written: "Treat this as the excellent standard: what the strongest honours graduates should show, an aspiration rather than a requirement (should), in subject-specific skills, for a bachelor's degree with honours in the subject at FHEQ level 6 (FQHEIS level 10). Cite it as (QAA, 2024, Dance, Drama and Performance Subject Benchmark Statement, para 4.15.b2). Do not present it as the minimum or as expected of every student. Set it beside the same outcome at the other rungs (4.9.b2, 4.12.b2), the honours descriptor qaa/fheq-2024/4.15.b2 with spine:6, and Annex D qaa/fheq-2024/annex-d/practical/r3/1st."
  author-agent-dialogue: "Raise it when a student aims for a first, or staff describe what first-class work looks like in this area. Put it in plain words: second person for a student, and for staff as what a module lets students show. Ask: What did the last text or score you worked on make possible, and what did you do with it? Never present this as what everyone must reach."
- statement: qaa/dance-drama-and-performance-2024/4.15.b3
  forPractitioner: { text: "Look for creative, comprehensive making or production backed by a thorough command of the field's vocabularies and methods.", rewrite: light, force: should, status: drafted }
  forBeneficiary: { text: "At the excellent standard, you should be able to make or produce performance creatively and comprehensively, with a thorough grasp of the techniques, crafts and working methods involved.", rewrite: full, force: should, status: drafted }
  author-agent-written: "Treat this as the excellent standard: what the strongest honours graduates should show, an aspiration rather than a requirement (should), in subject-specific skills, for a bachelor's degree with honours in the subject at FHEQ level 6 (FQHEIS level 10). Cite it as (QAA, 2024, Dance, Drama and Performance Subject Benchmark Statement, para 4.15.b3). Do not present it as the minimum or as expected of every student. Set it beside the same outcome at the other rungs (4.9.b1, 4.12.b3), the honours descriptor qaa/fheq-2024/4.15.b2 with spine:6, and Annex D qaa/fheq-2024/annex-d/practical/r3/1st."
  author-agent-dialogue: "Raise it when a student aims for a first, or staff describe what first-class work looks like in this area. Put it in plain words: second person for a student, and for staff as what a module lets students show. Ask: Which working methods could you use to make a piece from scratch without being shown? Never present this as what everyone must reach."
- statement: qaa/dance-drama-and-performance-2024/4.15.b4
  forPractitioner: { text: "Look for thorough, critical independent research that yields new performance or new insight.", rewrite: light, force: should, status: drafted }
  forBeneficiary: { text: "At the excellent standard, you should be able to research on your own critically and thoroughly, whether into past or present performance or as part of creating new work or ideas.", rewrite: full, force: should, status: drafted }
  author-agent-written: "Treat this as the excellent standard: what the strongest honours graduates should show, an aspiration rather than a requirement (should), in subject-specific skills, for a bachelor's degree with honours in the subject at FHEQ level 6 (FQHEIS level 10). Cite it as (QAA, 2024, Dance, Drama and Performance Subject Benchmark Statement, para 4.15.b4). Do not present it as the minimum or as expected of every student. Set it beside the same outcome at the other rungs (4.9.b5, 4.12.b4), the honours descriptor qaa/fheq-2024/4.15.b6 with spine:6, and Annex D qaa/fheq-2024/annex-d/knowledge/r3/1st."
  author-agent-dialogue: "Raise it when a student aims for a first, or staff describe what first-class work looks like in this area. Put it in plain words: second person for a student, and for staff as what a module lets students show. Ask: What question did your last independent research answer, and where did you find the evidence? Never present this as what everyone must reach."
- statement: qaa/dance-drama-and-performance-2024/4.15.b5
  forPractitioner: { text: "Look for critical investigation that identifies and interprets the cultural frameworks of performance events in their social and historical settings.", rewrite: light, force: should, status: drafted }
  forBeneficiary: { text: "At the excellent standard, you should be able to investigate critically the cultural frameworks around a performance and interpret them in their social and historical setting.", rewrite: full, force: should, status: drafted }
  author-agent-written: "Treat this as the excellent standard: what the strongest honours graduates should show, an aspiration rather than a requirement (should), in subject-specific skills, for a bachelor's degree with honours in the subject at FHEQ level 6 (FQHEIS level 10). Cite it as (QAA, 2024, Dance, Drama and Performance Subject Benchmark Statement, para 4.15.b5). Do not present it as the minimum or as expected of every student. Set it beside the same outcome at the other rungs (4.9.b6, 4.12.b5), the honours descriptor qaa/fheq-2024/4.15.b7 with spine:6, and Annex D qaa/fheq-2024/annex-d/cognitive/r1/1st."
  author-agent-dialogue: "Raise it when a student aims for a first, or staff describe what first-class work looks like in this area. Put it in plain words: second person for a student, and for staff as what a module lets students show. Ask: What cultural frame shapes the piece you are working on now? Never present this as what everyone must reach."
- statement: qaa/dance-drama-and-performance-2024/4.16.b1
  forPractitioner: { text: "Look for sophisticated creative and analytical argument, judged and presented in several forms.", rewrite: light, force: should, status: drafted }
  forBeneficiary: { text: "At the excellent standard, you should be able to develop arguments with sophisticated creative and analytical skill, and judge and present them in different ways.", rewrite: full, force: should, status: drafted }
  author-agent-written: "Treat this as the excellent standard: what the strongest honours graduates should show, an aspiration rather than a requirement (should), in generic and graduate skills, for a bachelor's degree with honours in the subject at FHEQ level 6 (FQHEIS level 10). Cite it as (QAA, 2024, Dance, Drama and Performance Subject Benchmark Statement, para 4.16.b1). Do not present it as the minimum or as expected of every student. Set it beside the same outcome at the other rungs (4.10.b4, 4.13.b1), the honours descriptor qaa/fheq-2024/4.15.b3.1 with spine:6, and Annex D qaa/fheq-2024/annex-d/cognitive/r2/1st."
  author-agent-dialogue: "Raise it when a student aims for a first, or staff describe what first-class work looks like in this area. Put it in plain words: second person for a student, and for staff as what a module lets students show. Ask: What is the strongest argument you have built this year, and how did you present it? Never present this as what everyone must reach."
- statement: qaa/dance-drama-and-performance-2024/4.16.b2
  forPractitioner: { text: "Look for developed critical analysis of how discourse shapes representation in the arts and culture.", rewrite: light, force: should, status: drafted }
  forBeneficiary: { text: "At the excellent standard, you should be able to examine and judge, critically and in depth, how kinds of discourse shape representation in the arts and culture.", rewrite: full, force: should, status: drafted }
  author-agent-written: "Treat this as the excellent standard: what the strongest honours graduates should show, an aspiration rather than a requirement (should), in generic and graduate skills, for a bachelor's degree with honours in the subject at FHEQ level 6 (FQHEIS level 10). Cite it as (QAA, 2024, Dance, Drama and Performance Subject Benchmark Statement, para 4.16.b2). Do not present it as the minimum or as expected of every student. Set it beside the same outcome at the other rungs (4.13.b2), the honours descriptor qaa/fheq-2024/4.15.b7 with spine:6, and Annex D qaa/fheq-2024/annex-d/cognitive/r2/1st."
  author-agent-dialogue: "Raise it when a student aims for a first, or staff describe what first-class work looks like in this area. Put it in plain words: second person for a student, and for staff as what a module lets students show. Ask: How does the way something is talked about shape how audiences receive it? Never present this as what everyone must reach."
- statement: qaa/dance-drama-and-performance-2024/4.16.b3
  forPractitioner: { text: "Look for productive, imaginative contributions to group work.", rewrite: light, force: should, status: drafted }
  forBeneficiary: { text: "At the excellent standard, you should be able to work in a group productively, creatively and imaginatively.", rewrite: full, force: should, status: drafted }
  author-agent-written: "Treat this as the excellent standard: what the strongest honours graduates should show, an aspiration rather than a requirement (should), in generic and graduate skills, for a bachelor's degree with honours in the subject at FHEQ level 6 (FQHEIS level 10). Cite it as (QAA, 2024, Dance, Drama and Performance Subject Benchmark Statement, para 4.16.b3). Do not present it as the minimum or as expected of every student. Set it beside the same outcome at the other rungs (4.10.b5, 4.13.b3), the honours descriptor qaa/fheq-2024/4.15.b9.1 with spine:6, and Annex D qaa/fheq-2024/annex-d/transferable/r2/1st."
  author-agent-dialogue: "Raise it when a student aims for a first, or staff describe what first-class work looks like in this area. Put it in plain words: second person for a student, and for staff as what a module lets students show. Ask: What did you contribute to your last group project that no one else did? Never present this as what everyone must reach."
- statement: qaa/dance-drama-and-performance-2024/4.16.b4
  forPractitioner: { text: "Look for efficient self-management and skilled negotiation of shared goals.", rewrite: light, force: should, status: drafted }
  forBeneficiary: { text: "At the excellent standard, you should be able to manage your own workload very well, meet deadlines and agree and work towards shared goals with others.", rewrite: full, force: should, status: drafted }
  author-agent-written: "Treat this as the excellent standard: what the strongest honours graduates should show, an aspiration rather than a requirement (should), in generic and graduate skills, for a bachelor's degree with honours in the subject at FHEQ level 6 (FQHEIS level 10). Cite it as (QAA, 2024, Dance, Drama and Performance Subject Benchmark Statement, para 4.16.b4). Do not present it as the minimum or as expected of every student. Set it beside the same outcome at the other rungs (4.10.b1, 4.13.b4), the honours descriptor qaa/fheq-2024/4.15.b5 with spine:6, and Annex D qaa/fheq-2024/annex-d/transferable/r3/1st."
  author-agent-dialogue: "Raise it when a student aims for a first, or staff describe what first-class work looks like in this area. Put it in plain words: second person for a student, and for staff as what a module lets students show. Ask: How do you plan your time when rehearsals and deadlines collide? Never present this as what everyone must reach."
- statement: qaa/dance-drama-and-performance-2024/4.16.b5
  forPractitioner: { text: "Look for constructive, effective handling of creative, artistic and interpersonal issues.", rewrite: light, force: should, status: drafted }
  forBeneficiary: { text: "At the excellent standard, you should be able to deal constructively and effectively with creative, artistic, personal and interpersonal issues.", rewrite: full, force: should, status: drafted }
  author-agent-written: "Treat this as the excellent standard: what the strongest honours graduates should show, an aspiration rather than a requirement (should), in generic and graduate skills, for a bachelor's degree with honours in the subject at FHEQ level 6 (FQHEIS level 10). Cite it as (QAA, 2024, Dance, Drama and Performance Subject Benchmark Statement, para 4.16.b5). Do not present it as the minimum or as expected of every student. Set it beside the same outcome at the other rungs (4.10.b6, 4.13.b5), the honours descriptor qaa/fheq-2024/4.15.b9.1 with spine:6, and Annex D qaa/fheq-2024/annex-d/transferable/r2/1st."
  author-agent-dialogue: "Raise it when a student aims for a first, or staff describe what first-class work looks like in this area. Put it in plain words: second person for a student, and for staff as what a module lets students show. Ask: How did you handle a disagreement in a creative team? Never present this as what everyone must reach."
- statement: qaa/dance-drama-and-performance-2024/4.16.b6
  forPractitioner: { text: "Look for discerning searching, synthesis and critical judgement of material.", rewrite: light, force: should, status: drafted }
  forBeneficiary: { text: "At the excellent standard, you should be able to find, sift, combine and organise material with discernment on your own and judge critically how much it matters.", rewrite: full, force: should, status: drafted }
  author-agent-written: "Treat this as the excellent standard: what the strongest honours graduates should show, an aspiration rather than a requirement (should), in generic and graduate skills, for a bachelor's degree with honours in the subject at FHEQ level 6 (FQHEIS level 10). Cite it as (QAA, 2024, Dance, Drama and Performance Subject Benchmark Statement, para 4.16.b6). Do not present it as the minimum or as expected of every student. Set it beside the same outcome at the other rungs (4.10.b8, 4.13.b6), the honours descriptor qaa/fheq-2024/4.15.b5 with spine:6, and Annex D qaa/fheq-2024/annex-d/cognitive/r1/1st."
  author-agent-dialogue: "Raise it when a student aims for a first, or staff describe what first-class work looks like in this area. Put it in plain words: second person for a student, and for staff as what a module lets students show. Ask: How do you decide which sources to keep and which to drop? Never present this as what everyone must reach."
- statement: qaa/dance-drama-and-performance-2024/4.16.b7
  forPractitioner: { text: "Look for strong digital skills and a full grasp of their possible uses.", rewrite: light, force: should, status: drafted }
  forBeneficiary: { text: "At the excellent standard, you should have suitable technical and digital skills and be fully aware of how they could be used.", rewrite: full, force: should, status: drafted }
  author-agent-written: "Treat this as the excellent standard: what the strongest honours graduates should show, an aspiration rather than a requirement (should), in generic and graduate skills, for a bachelor's degree with honours in the subject at FHEQ level 6 (FQHEIS level 10). Cite it as (QAA, 2024, Dance, Drama and Performance Subject Benchmark Statement, para 4.16.b7). Do not present it as the minimum or as expected of every student. Set it beside the same outcome at the other rungs (4.10.b9, 4.13.b7), the honours descriptor qaa/fheq-2024/4.15.b6 with spine:6, and Annex D qaa/fheq-2024/annex-d/transferable/r1/1st."
  author-agent-dialogue: "Raise it when a student aims for a first, or staff describe what first-class work looks like in this area. Put it in plain words: second person for a student, and for staff as what a module lets students show. Ask: Which digital tool have you adapted for your own creative purpose? Never present this as what everyone must reach."
- statement: qaa/dance-drama-and-performance-2024/4.16.b8
  forPractitioner: { text: "Look for confident choice and use of numeracy in practical and creative problems.", rewrite: light, force: should, status: drafted }
  forBeneficiary: { text: "At the excellent standard, you should be able to choose and use a range of number skills to solve problems and produce creative work.", rewrite: full, force: should, status: drafted }
  author-agent-written: "Treat this as the excellent standard: what the strongest honours graduates should show, an aspiration rather than a requirement (should), in generic and graduate skills, for a bachelor's degree with honours in the subject at FHEQ level 6 (FQHEIS level 10). Cite it as (QAA, 2024, Dance, Drama and Performance Subject Benchmark Statement, para 4.16.b8). Do not present it as the minimum or as expected of every student. Set it beside the same outcome at the other rungs (4.10.b11, 4.13.b8), the honours descriptor qaa/fheq-2024/4.15.b3.1 with spine:6, and Annex D qaa/fheq-2024/annex-d/transferable/r1/1st."
  author-agent-dialogue: "Raise it when a student aims for a first, or staff describe what first-class work looks like in this area. Put it in plain words: second person for a student, and for staff as what a module lets students show. Ask: Where did numbers matter in your last production, for example a budget, a schedule or a lighting plot? Never present this as what everyone must reach."
- statement: qaa/dance-drama-and-performance-2024/4.17.b1
  forPractitioner: { text: "Expect master's students to show a systematic, critical grasp of current and emerging directions in the field's practice and research.", rewrite: light, force: should, status: drafted }
  forBeneficiary: { text: "By the end of your master's degree, you should be able to show a systematic, thorough and critical grasp of where practice and research in your field are now and where they are going.", rewrite: full, force: should, status: drafted }
  author-agent-written: "Treat this as a master's outcome (should) at FHEQ level 7 (FQHEIS level 11), added to the honours standards for master's study in the subject. Cite it as (QAA, 2024, Dance, Drama and Performance Subject Benchmark Statement, para 4.17.b1). Set it beside the honours excellent rung item 4.14.b1 and the master's descriptor qaa/fheq-2024/4.17.b1 with spine:7. Do not claim it applies to honours graduates or that it sets rungs; the master's list has no threshold, typical or excellent split."
  author-agent-dialogue: "Raise it when a master's student or a postgraduate team asks how master's work differs from honours. Put it in plain words, second person for a student. Ask: Which current development in the field could you explain and critique to a specialist? Avoid presenting it as an honours expectation."
- statement: qaa/dance-drama-and-performance-2024/4.17.b2
  forPractitioner: { text: "Expect critical evaluation of current research and scholarship, applied with originality.", rewrite: light, force: should, status: drafted }
  forBeneficiary: { text: "By the end of your master's degree, you should be able to evaluate current research and advanced scholarship and use what you know in original ways.", rewrite: full, force: should, status: drafted }
  author-agent-written: "Treat this as a master's outcome (should) at FHEQ level 7 (FQHEIS level 11), added to the honours standards for master's study in the subject. Cite it as (QAA, 2024, Dance, Drama and Performance Subject Benchmark Statement, para 4.17.b2). Set it beside the honours excellent rung item 4.15.b4 and the master's descriptor qaa/fheq-2024/4.17.b4.1 with spine:7. Do not claim it applies to honours graduates or that it sets rungs; the master's list has no threshold, typical or excellent split."
  author-agent-dialogue: "Raise it when a master's student or a postgraduate team asks how master's work differs from honours. Put it in plain words, second person for a student. Ask: Where has your reading of recent research changed what you made or argued? Avoid presenting it as an honours expectation."
- statement: qaa/dance-drama-and-performance-2024/4.17.b3
  forPractitioner: { text: "Expect students to choose and justify methods and to tackle complex problems with self-direction and originality.", rewrite: light, force: should, status: drafted }
  forBeneficiary: { text: "By the end of your master's degree, you should be able to weigh up methods and tackle complex problems in practice or research on your own initiative and in original ways.", rewrite: full, force: should, status: drafted }
  author-agent-written: "Treat this as a master's outcome (should) at FHEQ level 7 (FQHEIS level 11), added to the honours standards for master's study in the subject. Cite it as (QAA, 2024, Dance, Drama and Performance Subject Benchmark Statement, para 4.17.b3). Set it beside the honours excellent rung item 4.16.b1 and the master's descriptor qaa/fheq-2024/4.17.b6 with spine:7. Do not claim it applies to honours graduates or that it sets rungs; the master's list has no threshold, typical or excellent split."
  author-agent-dialogue: "Raise it when a master's student or a postgraduate team asks how master's work differs from honours. Put it in plain words, second person for a student. Ask: Why did you choose the method you used, and what else did you rule out? Avoid presenting it as an honours expectation."
- statement: qaa/dance-drama-and-performance-2024/4.17.b4
  forPractitioner: { text: "Expect new insight and clear communication of conclusions to specialist and general audiences.", rewrite: light, force: should, status: drafted }
  forBeneficiary: { text: "By the end of your master's degree, you should be able to create new insight in your field and explain your conclusions clearly to experts and non-experts.", rewrite: full, force: should, status: drafted }
  author-agent-written: "Treat this as a master's outcome (should) at FHEQ level 7 (FQHEIS level 11), added to the honours standards for master's study in the subject. Cite it as (QAA, 2024, Dance, Drama and Performance Subject Benchmark Statement, para 4.17.b4). Set it beside the honours excellent rung item 4.16.b1 and the master's descriptor qaa/fheq-2024/4.17.b5 with spine:7. Do not claim it applies to honours graduates or that it sets rungs; the master's list has no threshold, typical or excellent split."
  author-agent-dialogue: "Raise it when a master's student or a postgraduate team asks how master's work differs from honours. Put it in plain words, second person for a student. Ask: How would you explain your main finding to someone outside the field? Avoid presenting it as an honours expectation."
- statement: qaa/dance-drama-and-performance-2024/4.17.b5
  forPractitioner: { text: "Build in a major practice piece or substantial research project grounded in deep knowledge of the discipline.", rewrite: light, force: should, status: drafted }
  forBeneficiary: { text: "By the end of your master's degree, you should be able to complete a major piece of practice or a substantial research project, built on a thorough understanding of your discipline.", rewrite: full, force: should, status: drafted }
  author-agent-written: "Treat this as a master's outcome (should) at FHEQ level 7 (FQHEIS level 11), added to the honours standards for master's study in the subject. Cite it as (QAA, 2024, Dance, Drama and Performance Subject Benchmark Statement, para 4.17.b5). Set it beside the honours excellent rung item 4.15.b4 and the master's descriptor qaa/fheq-2024/4.17.b2 with spine:7. Do not claim it applies to honours graduates or that it sets rungs; the master's list has no threshold, typical or excellent split."
  author-agent-dialogue: "Raise it when a master's student or a postgraduate team asks how master's work differs from honours. Put it in plain words, second person for a student. Ask: What will your major project add that a shorter piece could not? Avoid presenting it as an honours expectation."
```

### S5 Levels and alignment
<!-- label: both; status: drafted; basis: primary -->
```yaml
levels:
  - { id: "fheq:6", role: "cites", locator: "D1, 2.2 (\"FHEQ Levels 6 and 7\"); 4.2 to 4.16 (honours)" }
  - { id: "fqheis:10", role: "cites", locator: "D1, 2.2 (\"FQHEIS 10 and 11\")" }
  - { id: "fheq:7", role: "cites", locator: "D1, 2.2; 2.11 (integrated master's); 4.17" }
  - { id: "fqheis:11", role: "cites", locator: "D1, 2.2; 2.11" }
  - { id: "fheq:4", role: "inferred: CertHE named as an exit award (D1, 2.12); level from std:doc:qaa-fheq-2024-framework S5 (Table 1)", locator: "D1, 2.12" }
  - { id: "fheq:5", role: "inferred: DipHE named as an exit award (D1, 2.12); level from std:doc:qaa-fheq-2024-framework S5 (Table 1)", locator: "D1, 2.12" }
  - { id: "spine:6", role: "inferred: the reference framework step for the honours standards (std:ref:uk-framework R2, R8)", locator: "D1, 4.8 to 4.16" }
  - { id: "spine:7", role: "inferred: the reference framework step for the master's outcomes (std:ref:uk-framework R2, R8)", locator: "D1, 4.17" }
crosswalks:
  - { from: "fheq:6", to: "fqheis:10", relation: "equivalent", basis: "stated (D1, 2.2: \"FHEQ Levels 6 and 7/FQHEIS 10 and 11\")" }
  - { from: "fheq:7", to: "fqheis:11", relation: "equivalent", basis: "stated (D1, 2.11: \"(FHEQ Level 7; FQHEIS Level 11)\")" }
  - { from: "fheq:6", to: "cqfw:6", relation: "compares-with", basis: "inferred from std:doc:qaa-fheq-2024-framework S5 (its 2.24); the statement does not name the CQFW (Part E)" }
```

### S6 Themes
<!-- label: both; status: drafted; basis: primary -->
```yaml
- { id: "theme:edi", role: "carries", carriedIn: ["front matter", "1.3", "1.13", "1.14", "1.16", "1.17", "1.18", "1.19", "1.20", "1.27", "1.28", "1.33", "2.1", "2.7", "2.17", "2.19", "3.6", "3.13", "4.7"] }
- { id: "theme:accessibility", role: "carries", carriedIn: ["front matter", "1.3", "1.13", "1.16", "1.21", "1.22", "1.23", "1.24", "1.25", "1.26", "1.28", "1.29", "1.30", "1.34", "3.6", "4.7"] }
- { id: "theme:esd", role: "carries", carriedIn: ["front matter", "1.3", "1.10", "1.16", "1.31", "1.32", "1.33", "1.34", "4.7", "4.8", "4.11", "4.14"] }
- { id: "theme:enterprise", role: "carries", carriedIn: ["front matter", "1.3", "1.16", "1.33", "1.35", "1.36", "1.37", "1.38", "2.14", "2.18", "2.20", "4.7"] }
- { id: "theme:generative-ai", role: "carries", carriedIn: ["1.15"] }
```

### S7 Relations
<!-- label: both; status: drafted; basis: primary -->
```yaml
- { rel: "partOf", target: "collection: QAA Subject Benchmark Statements", note: "one of 54 held by stan" }
- { rel: "supersedes", target: "std:doc:qaa-dance-drama-and-performance-2019-benchmarks (not held)", note: "the fourth edition, 2019, named in section 6; earlier editions 2015, 2007 and 2002 are named there too" }
- { rel: "refersTo", target: "std:doc:qaa-fheq-2024-framework, Annex D", note: "the degree outcome classification descriptions, cited in 4.3 as Annex D in The Frameworks for Higher Education Qualifications of UK Degree-Awarding Bodies" }
- { rel: "refersTo", target: "std:doc:qaa-fheq-2024-framework", note: "FHEQ levels 6 and 7 (2.2, 2.11)" }
- { rel: "refersTo", target: "std:doc:qaa-fqheis-2024-framework", note: "FQHEIS levels 10 and 11 (2.2, 2.11)" }
- { rel: "themeReference", target: "std:doc:qaa-advancehe-esd-2021-guidance", note: "QAA and Advance HE Education for Sustainable Development Guidance (2021), cited in 1.31 and section 5" }
- { rel: "themeReference", target: "std:doc:qaa-enterprise-2018-guidance", note: "Enterprise and Entrepreneurship Education guidance, QAA 2018, listed in section 5 only" }
- { rel: "refersTo", target: "QAA Quality Code, Advice and Guidance, including work-based learning (not yet ingested)", note: "front matter; 2.17 (\"QAA guidance on work-based learning\")" }
- { rel: "refersTo", target: "QAA Glossary (not ingested)", note: "front matter" }
- { rel: "refersTo", target: "Equality Act 2010 (legislation, not a standards document)", note: "1.17" }
- { rel: "refersTo", target: "UN Sustainable Development Goals and the 2030 Agenda; the Theatre Green Book (not standards documents)", note: "1.31" }
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
- A broad field of established and emerging forms joining practice and theory in studying performance and how it is produced (D1, 1.1, 2.3).
- Diversity of provision is a strength: specialist training, single, combined and interdisciplinary courses, from industry-ready to research-led and socially engaged (D1, 1.3, 1.5, 1.6, 2.2).
- Embodied and experiential learning is its distinctive way of knowing (D1, 1.9, 3.8).
- Creativity and its communication sit at the centre, with critical and creative work feeding each other (D1, 1.7, 1.8, 3.7).
- Learning is collaborative: ensembles, companies and group work are typical, balanced with safety and creative risk (D1, 1.12, 1.13, 3.11).
- The field's practices are dynamic and contested, open to change and respectful of tradition (D1, 1.4, 2.4, 2.5).
- Strongly tied to the creative industries and wider employment through partnerships, placements and portfolio careers (D1, 1.35, 1.38, 2.14 to 2.20).
- 'Performance' is used inclusively for all of dance, drama and performance in sections 3 and 4 (D1, 3.2, 4.1).

### SB2 Themes in this subject
<!-- label: both; status: drafted; basis: primary -->
```yaml
- theme: theme:edi
  inThisSubject: "framed through inclusive learning communities and the studio: ethical, non-judgemental conversation about lived realities, centring marginalised voices and histories, no structural disadvantage, the Equality Act 2010, and partners who share the same principles (D1, 1.17 to 1.20, 2.19)"
  statements: ["qaa/dance-drama-and-performance-2024/1.17", "qaa/dance-drama-and-performance-2024/3.6", "qaa/dance-drama-and-performance-2024/4.7", "qaa/dance-drama-and-performance-2024/3.3.b11"]
- theme: theme:accessibility
  inThisSubject: "anticipatory design across studio, classroom, fieldwork and digital work, questioning ableist knowledge, planning for barriers in group and practical work, blended options and fair digital access (D1, 1.21 to 1.30, 1.34)"
  statements: ["qaa/dance-drama-and-performance-2024/1.24", "qaa/dance-drama-and-performance-2024/3.6", "qaa/dance-drama-and-performance-2024/4.7"]
- theme: theme:esd
  inThisSubject: "named sustainability in 1.3 and 1.16; ESD defined with the SDGs, the 2021 guidance and the Theatre Green Book, with economic, social and environmental themes for curricula, and safe, environmentally sustainable practice in each rung (D1, 1.31 to 1.34, 4.8, 4.11, 4.14)"
  statements: ["qaa/dance-drama-and-performance-2024/4.7", "qaa/dance-drama-and-performance-2024/4.8.b12", "qaa/dance-drama-and-performance-2024/4.11.b11", "qaa/dance-drama-and-performance-2024/4.14.b11"]
- theme: theme:enterprise
  inThisSubject: "enterprise and entrepreneurship education for future-ready employability and portfolio careers, authentic assessment, partnerships and operating entrepreneurially; the front matter joins it with employability (D1, 1.35 to 1.38, 2.14, 2.20)"
  statements: ["qaa/dance-drama-and-performance-2024/4.7"]
- theme: theme:generative-ai
  inThisSubject: "generative AI and other new technologies are analysed for their effect on the creative industries and used, with critical reflection and openness, to develop creative material (D1, 1.15)"
  statements: []
```

### SB3 Content and delivery
<!-- label: both; status: drafted; basis: primary -->
```yaml
areas:
  - { component: "1.11", gloss: "six broad strands: practical work, technique, critical studies, technology, communication and collaboration, preparation for employment" }
  - { component: "2.3", gloss: "the fields degrees cover: the disciplines and their production, cognate media, practical skill with critical analysis, histories, social contexts and audiences" }
  - { component: "3.2", gloss: "eight areas of knowledge and understanding, from practitioners and histories to research methods and interdisciplinarity" }
practices:
  - { component: "3.7", kind: "teaching", gloss: "varied approaches built round practice and theory together" }
  - { component: "3.8", kind: "learning", gloss: "experiential and embodied learning as the basis of study" }
  - { component: "3.10", kind: "learning", gloss: "practical and professional contexts and varied roles" }
  - { component: "3.11", kind: "learning", gloss: "tutor-led to self-directed learning; group work" }
  - { component: "3.12", kind: "teaching", gloss: "workshops, rehearsals, productions, studio, lectures, seminars, tutorials, in person and online" }
  - { component: "3.13", kind: "assessment", gloss: "inclusive, diverse and negotiated assessment as part of learning" }
  - { component: "3.14", kind: "assessment", gloss: "formats from performance and design outputs to essays, portfolios and dissertations" }
  - { component: "3.15", kind: "assessment", gloss: "self and peer assessment; course information on assessment" }
  - { component: "3.17", kind: "learning", gloss: "handbooks on academic practice, support and well-being" }
```

### SB4 Benchmark standards
<!-- label: both; status: drafted; basis: primary -->
```yaml
rungs:
  - { rung: "threshold", leadIn: "4.8", award: "bachelor's with honours", items: 30 }
  - { rung: "typical", leadIn: "4.11", award: "bachelor's with honours", items: 24 }
  - { rung: "excellent", leadIn: "4.14", award: "bachelor's with honours", items: 24 }
rungBases: "Each rung is named by a sub-heading (Threshold level, Typical level, Excellent level) and holds three lists, each with its own lead-in in 'should be able to': subject knowledge and understanding (4.8, 4.11, 4.14), subject-specific skills (4.9, 4.12, 4.15) and generic and graduate skills (4.10, 4.13, 4.16). Counts: threshold 12, 7 and 11; typical 11, 5 and 8; excellent 11, 5 and 8. 4.2: the minimum threshold, typical and excellent standards shown at the award of honours. 4.3: most students exceed the threshold; Annex D for the classes. 4.6: the threshold is met when knowledge, understanding, creativity and skill suffice to present performance or argument; excellent work tends to go past the outcomes. 4.7: outcomes indicative, for single honours, not a checklist."
outcomeLists:
  - { leadIn: "3.3", gloss: "thirteen skills students will develop (will; the stem asks courses to enable them, should)", items: 13, award: ["honours"] }
  - { leadIn: "4.17", gloss: "five added outcomes for master's study (should), with no rungs", items: 5, award: ["master's"] }
outcomes:
  - { outcome: "forms, traditions and histories", threshold: "qaa/dance-drama-and-performance-2024/4.8.b1", typical: "qaa/dance-drama-and-performance-2024/4.11.b1", excellent: "qaa/dance-drama-and-performance-2024/4.14.b1", basis: "inferred", domain: "knowledge", award: "bachelor's with honours" }
  - { outcome: "components of performance and how work is made", threshold: "qaa/dance-drama-and-performance-2024/4.8.b2", typical: "qaa/dance-drama-and-performance-2024/4.11.b2", excellent: "qaa/dance-drama-and-performance-2024/4.14.b2", basis: "inferred", domain: "knowledge", award: "bachelor's with honours" }
  - { outcome: "critical and theoretical perspectives", threshold: "qaa/dance-drama-and-performance-2024/4.8.b3", typical: "qaa/dance-drama-and-performance-2024/4.11.b3", excellent: "qaa/dance-drama-and-performance-2024/4.14.b3", basis: "inferred", domain: "knowledge", award: "bachelor's with honours" }
  - { outcome: "practitioners, theorists and their contexts", threshold: "qaa/dance-drama-and-performance-2024/4.8.b4", typical: "qaa/dance-drama-and-performance-2024/4.11.b4", excellent: "qaa/dance-drama-and-performance-2024/4.14.b4", basis: "inferred", domain: "knowledge", award: "bachelor's with honours" }
  - { outcome: "role of performance in society, education and industry", threshold: "qaa/dance-drama-and-performance-2024/4.8.b5", typical: "qaa/dance-drama-and-performance-2024/4.11.b5", excellent: "qaa/dance-drama-and-performance-2024/4.14.b5", basis: "inferred", domain: "knowledge", award: "bachelor's with honours" }
  - { outcome: "critical and creative enquiry together", threshold: "qaa/dance-drama-and-performance-2024/4.8.b6", typical: "qaa/dance-drama-and-performance-2024/4.11.b6", excellent: "qaa/dance-drama-and-performance-2024/4.14.b6", basis: "inferred", domain: "understanding", award: "bachelor's with honours" }
  - { outcome: "interpreting texts and scores to make performance", threshold: "qaa/dance-drama-and-performance-2024/4.8.b7", typical: "qaa/dance-drama-and-performance-2024/4.11.b7", excellent: "qaa/dance-drama-and-performance-2024/4.14.b7", basis: "inferred", domain: "understanding", award: "bachelor's with honours" }
  - { outcome: "group and collective processes", threshold: "qaa/dance-drama-and-performance-2024/4.8.b8", typical: "qaa/dance-drama-and-performance-2024/4.11.b8", excellent: "qaa/dance-drama-and-performance-2024/4.14.b8", basis: "inferred", domain: "understanding", award: "bachelor's with honours" }
  - { outcome: "elements of performance", threshold: "qaa/dance-drama-and-performance-2024/4.8.b9", typical: "qaa/dance-drama-and-performance-2024/4.11.b9", excellent: "qaa/dance-drama-and-performance-2024/4.14.b9", basis: "inferred", domain: "understanding", award: "bachelor's with honours" }
  - { outcome: "interdisciplinary elements and their use", threshold: "qaa/dance-drama-and-performance-2024/4.8.b10", typical: "qaa/dance-drama-and-performance-2024/4.11.b10", excellent: "qaa/dance-drama-and-performance-2024/4.14.b10", basis: "inferred", domain: "understanding", award: "bachelor's with honours" }
  - { outcome: "knowledge and skills from other disciplines", threshold: "qaa/dance-drama-and-performance-2024/4.8.b11", typical: "none", excellent: "none", basis: "inferred", domain: "understanding", award: "bachelor's with honours" }
  - { outcome: "safe, ethical and sustainable practice", threshold: "qaa/dance-drama-and-performance-2024/4.8.b12", typical: "qaa/dance-drama-and-performance-2024/4.11.b11", excellent: "qaa/dance-drama-and-performance-2024/4.14.b11", basis: "inferred", domain: "understanding", award: "bachelor's with honours" }
  - { outcome: "making and producing performance", threshold: "qaa/dance-drama-and-performance-2024/4.9.b1", typical: "qaa/dance-drama-and-performance-2024/4.12.b3", excellent: "qaa/dance-drama-and-performance-2024/4.15.b3", basis: "inferred", domain: "subject-skill", award: "bachelor's with honours" }
  - { outcome: "realising a text, stimulus or score", threshold: "qaa/dance-drama-and-performance-2024/4.9.b2", typical: "qaa/dance-drama-and-performance-2024/4.12.b2", excellent: "qaa/dance-drama-and-performance-2024/4.15.b2", basis: "inferred", domain: "subject-skill", award: "bachelor's with honours" }
  - { outcome: "records and documentation", threshold: "qaa/dance-drama-and-performance-2024/4.9.b3", typical: "none", excellent: "none", basis: "inferred", domain: "subject-skill", award: "bachelor's with honours" }
  - { outcome: "describing and evaluating performance events", threshold: "qaa/dance-drama-and-performance-2024/4.9.b4", typical: "none", excellent: "none", basis: "inferred", domain: "subject-skill", award: "bachelor's with honours" }
  - { outcome: "independent research", threshold: "qaa/dance-drama-and-performance-2024/4.9.b5", typical: "qaa/dance-drama-and-performance-2024/4.12.b4", excellent: "qaa/dance-drama-and-performance-2024/4.15.b4", basis: "inferred", domain: "subject-skill", award: "bachelor's with honours" }
  - { outcome: "cultural frameworks of performance", threshold: "qaa/dance-drama-and-performance-2024/4.9.b6", typical: "qaa/dance-drama-and-performance-2024/4.12.b5", excellent: "qaa/dance-drama-and-performance-2024/4.15.b5", basis: "inferred", domain: "subject-skill", award: "bachelor's with honours" }
  - { outcome: "performance space", threshold: "qaa/dance-drama-and-performance-2024/4.9.b7", typical: "none", excellent: "none", basis: "inferred", domain: "subject-skill", award: "bachelor's with honours" }
  - { outcome: "selecting, refining and presenting skills", threshold: "none", typical: "qaa/dance-drama-and-performance-2024/4.12.b1", excellent: "qaa/dance-drama-and-performance-2024/4.15.b1", basis: "inferred", domain: "subject-skill", award: "bachelor's with honours" }
  - { outcome: "self-management and shared goals", threshold: "qaa/dance-drama-and-performance-2024/4.10.b1", typical: "qaa/dance-drama-and-performance-2024/4.13.b4", excellent: "qaa/dance-drama-and-performance-2024/4.16.b4", basis: "inferred", domain: "generic-skill", award: "bachelor's with honours" }
  - { outcome: "adaptability and awareness of self and others", threshold: "qaa/dance-drama-and-performance-2024/4.10.b2", typical: "none", excellent: "none", basis: "inferred", domain: "generic-skill", award: "bachelor's with honours" }
  - { outcome: "risk and ethical practice", threshold: "qaa/dance-drama-and-performance-2024/4.10.b3", typical: "none", excellent: "none", basis: "inferred", domain: "generic-skill", award: "bachelor's with honours" }
  - { outcome: "critical argument", threshold: "qaa/dance-drama-and-performance-2024/4.10.b4", typical: "qaa/dance-drama-and-performance-2024/4.13.b1", excellent: "qaa/dance-drama-and-performance-2024/4.16.b1", basis: "inferred", domain: "generic-skill", award: "bachelor's with honours" }
  - { outcome: "group work", threshold: "qaa/dance-drama-and-performance-2024/4.10.b5", typical: "qaa/dance-drama-and-performance-2024/4.13.b3", excellent: "qaa/dance-drama-and-performance-2024/4.16.b3", basis: "inferred", domain: "generic-skill", award: "bachelor's with honours" }
  - { outcome: "creative and interpersonal issues", threshold: "qaa/dance-drama-and-performance-2024/4.10.b6", typical: "qaa/dance-drama-and-performance-2024/4.13.b5", excellent: "qaa/dance-drama-and-performance-2024/4.16.b5", basis: "inferred", domain: "generic-skill", award: "bachelor's with honours" }
  - { outcome: "communication and presentation", threshold: "qaa/dance-drama-and-performance-2024/4.10.b7", typical: "none", excellent: "none", basis: "inferred", domain: "generic-skill", award: "bachelor's with honours" }
  - { outcome: "information retrieval and management", threshold: "qaa/dance-drama-and-performance-2024/4.10.b8", typical: "qaa/dance-drama-and-performance-2024/4.13.b6", excellent: "qaa/dance-drama-and-performance-2024/4.16.b6", basis: "inferred", domain: "generic-skill", award: "bachelor's with honours" }
  - { outcome: "digital media and technology", threshold: "qaa/dance-drama-and-performance-2024/4.10.b9", typical: "qaa/dance-drama-and-performance-2024/4.13.b7", excellent: "qaa/dance-drama-and-performance-2024/4.16.b7", basis: "inferred", domain: "generic-skill", award: "bachelor's with honours" }
  - { outcome: "project management", threshold: "qaa/dance-drama-and-performance-2024/4.10.b10", typical: "none", excellent: "none", basis: "inferred", domain: "generic-skill", award: "bachelor's with honours" }
  - { outcome: "numeracy for creative outcomes", threshold: "qaa/dance-drama-and-performance-2024/4.10.b11", typical: "qaa/dance-drama-and-performance-2024/4.13.b8", excellent: "qaa/dance-drama-and-performance-2024/4.16.b8", basis: "inferred", domain: "generic-skill", award: "bachelor's with honours" }
  - { outcome: "discourse and representation", threshold: "none", typical: "qaa/dance-drama-and-performance-2024/4.13.b2", excellent: "qaa/dance-drama-and-performance-2024/4.16.b2", basis: "inferred", domain: "generic-skill", award: "bachelor's with honours" }
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
- { body: "professional, statutory and regulatory bodies (PSRBs), in general", says: "the statement supports PSRBs on academic standards; courses may consider their requirements; courses with professional and vocational outcomes may need evaluation and accreditation by professional and regulatory bodies (D1, front matter, 2.25)", requirements: "not-applicable-by-design: no body named" }
- { body: "funding and regulatory bodies (unnamed)", says: "providers meet the legislative and regulatory requirements these bodies place on them; the statement does not interpret them (D1, front matter)", requirements: "not-applicable-by-design: no body named" }
- { body: "Office for Students", says: "in England the statement is not a sector-recognised standard under its regulatory framework (D1, front matter)", requirements: "not yet ingested (Part E)" }
- { body: "Disabled Students Commission", says: "listed in section 5 only, with no text in the numbered paragraphs (D1, section 5)", requirements: "not yet ingested (Part E)" }
```

### SB6 Cross-cutting references
<!-- label: both; status: drafted; basis: primary -->
```yaml
themes:
  - { id: "theme:edi", named: "Equality, diversity and inclusion", carriedIn: ["front matter", "1.3", "1.13", "1.14", "1.16", "1.17", "1.18", "1.19", "1.20", "1.27", "1.28", "1.33", "2.1", "2.7", "2.17", "2.19", "3.6", "3.13", "4.7"], statements: ["1.17", "3.6", "4.7", "3.3.b11"] }
  - { id: "theme:accessibility", named: "Accessibility (front matter: accessibility and the needs of disabled students)", carriedIn: ["front matter", "1.3", "1.13", "1.16", "1.21", "1.22", "1.23", "1.24", "1.25", "1.26", "1.28", "1.29", "1.30", "1.34", "3.6", "4.7"], statements: ["1.24", "3.6", "4.7"] }
  - { id: "theme:esd", named: "Sustainability (front matter: education for sustainable development; 1.31: Education for Sustainable Development (ESD))", carriedIn: ["front matter", "1.3", "1.10", "1.16", "1.31", "1.32", "1.33", "1.34", "4.7", "4.8", "4.11", "4.14"], statements: ["4.7", "4.8.b12", "4.11.b11", "4.14.b11"] }
  - { id: "theme:enterprise", named: "Enterprise and entrepreneurship education (front matter: employability, entrepreneurship and enterprise education)", carriedIn: ["front matter", "1.3", "1.16", "1.33", "1.35", "1.36", "1.37", "1.38", "2.14", "2.18", "2.20", "4.7"], statements: ["4.7"] }
  - { id: "theme:generative-ai", named: "Generative artificial intelligence (AI) and other new technologies", carriedIn: ["1.15"], statements: [] }
frameworks:
  - { framework: "fheq", levels: ["fheq:6", "fheq:7"], citedIn: ["2.2", "2.11"] }
  - { framework: "scqf", levels: ["fqheis:10", "fqheis:11"], citedIn: ["2.2", "2.11"] }
bodies:
  - { body: "professional, statutory and regulatory bodies (PSRBs)", citedIn: ["front matter", "2.25"] }
  - { body: "funding and regulatory bodies (unnamed)", citedIn: ["front matter"] }
  - { body: "Office for Students (regulatory framework, England)", citedIn: ["front matter"] }
  - { body: "Disabled Students Commission", citedIn: ["section 5"] }
sharedDocuments:
  - { document: "std:doc:qaa-fheq-2024-framework, Annex D", named: "Annex D in The Frameworks for Higher Education Qualifications of UK Degree-Awarding Bodies", citedIn: ["4.3"], role: "descriptions of the four honours classes (1st, 2.1, 2.2, 3rd) that providers should refer to when setting evidence of achievement" }
  - { document: "std:doc:qaa-advancehe-esd-2021-guidance", named: "the QAA and Advance HE Education for Sustainable Development Guidance (2021)", citedIn: ["1.31", "section 5"], role: "a reference for creating ESD curricula" }
  - { document: "std:doc:qaa-enterprise-2018-guidance", named: "QAA (2018) Enterprise and Entrepreneurship Education: Guidance for UK Higher Education Providers", citedIn: ["section 5"], role: "listed as a further resource for the enterprise theme" }
  - { document: "QAA Quality Code, Advice and Guidance (not yet ingested: Part E)", named: "Advice and Guidance to support the Quality Code; QAA guidance on work-based learning", citedIn: ["front matter", "2.17"], role: "course design, teaching, external expertise, monitoring; placement learning" }
  - { document: "QAA Glossary (not ingested)", named: "QAA's Glossary", citedIn: ["front matter"], role: "explains unfamiliar terms" }
```

## Part B Terminology
<!-- The statement has no glossary of its own unless Part E says so; these are terms it defines in its text. -->

### B1 Concepts
<!-- label: both; status: drafted; basis: primary -->
```yaml
- { slug: "performance-inclusive", definition: "used inclusively in sections 3 and 4 for activity, practical or theoretical, across all of dance, drama and performance and associated courses (D1, 3.2, 4.1)", beneficiaryDefinition: "any dance, drama, theatre or performance work, practical or written", scopeNote: "capitalised as Performance in the text", category: "unknown", practices: ["performing arts"] }
- { slug: "education-for-sustainable-development", definition: "the process of creating curricula, with subject content and pedagogy, that support sustainable development (D1, 1.31)", beneficiaryDefinition: "learning that helps you act for a sustainable future", scopeNote: "the section is headed Sustainability", category: "unknown", practices: ["education"] }
- { slug: "threshold-typical-excellent", definition: "the three rungs of standards: the minimum shown at award, the typical and the excellent (D1, 4.2, 4.6)", beneficiaryDefinition: "the minimum, the usual and the highest standard for your honours degree", scopeNote: "each rung has three lists in 4.8 to 4.16", category: "unknown", practices: ["education"] }
```

### B2a Terms as the issuer defines them
<!-- label: source; status: drafted; basis: primary -->
```yaml
- { concept: "performance-inclusive", form: "'Performance'", lang: "en", partOfSpeech: "noun", termStatus: "preferred", register: "formal" }
- { concept: "education-for-sustainable-development", form: "Education for Sustainable Development (ESD)", lang: "en", partOfSpeech: "noun-phrase", termStatus: "preferred", register: "formal" }
- { concept: "threshold-typical-excellent", form: "Threshold level; Typical level; Excellent level", lang: "en", partOfSpeech: "noun-phrase", termStatus: "preferred", register: "formal" }
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
  title: "Subject Benchmark Statement Dance, Drama and Performance"
  edition: "April 2024 (fifth edition)"
  year: 2024
  url: unknown (the QAA page; the text came by stan's extraction)
  retrieved: "held from stan: wkspc2615-QAAVector mapped/dance-drama-and-performance-2024/dance-drama-and-performance-2024.raw.txt, commit 366bcb99a01118f2c4c3ebfa2a8337596bddc455; received 2026-10-03"
  licence: QAA copyright
  tier: primary
  readVia: direct
  held: 33cac4483fa4445fc15ce646384e70a94c23d0201949ce0847bcafe96baad525
  heldFiles: ["wkspc2601-library/txt/qaa-2024-dance-drama-performance-subject-benchmark-statement-standard.txt", "wkspc2601-library/txt/qaa-2024-dance-drama-performance-subject-benchmark-statement-standard.norm.txt", "wkspc2601-library/records/qaa-2024-dance-drama-performance-subject-benchmark-statement-standard.chunks.json", "wkspc2601-library/records/qaa-2024-dance-drama-performance-subject-benchmark-statement-standard.held.json"]
  citedIn: [S1, S2, S3, S4, S4a, S5, S6, S7, SB1, SB2, SB3, SB4, SB5, SB6]
```

### D2 Research log
```yaml
- { ref: D1, tier: primary, consulted: 2026-10-03, pass: P1, outcome: "read whole, direct, from the normalised text; skeleton by tools/std_prep.py, document by tools/bm_build.py" }
- { ref: "ADAPT subj HESA stores, cah.json and hecos.json (designs/ingest/standards/subj/vocab)", tier: primary, consulted: 2026-10-03, pass: P1, outcome: "codes for statedSubjects and subjects" }
```

### D3 Wanted sources
```yaml
- { w: "W-std-0051", source: "QAA Subject Benchmark Statement: Dance, Drama and Performance (2019, fourth edition)", why: "the edition this one supersedes, for the change comparison" }
- { w: "W-std-0052", source: "QAA Quality Code Advice and Guidance: Work-based Learning", why: "cited in 2.17 for placement learning; not ingested" }
```

## Part E Gaps and questions
- Rungs: three, each named by a sub-heading and split into three lists with their own lead-ins (subject knowledge and understanding; subject-specific skills; generic and graduate skills), 30, 24 and 24 items. Psychology has one list per rung. SB4 leadIn names the first list of each rung (4.8, 4.11, 4.14); the other lead-ins are in rungBases.
- Rung force: every rung lead-in reads "should be able to" (4.14: "It is expected that ... graduates should be able to demonstrate"), so all 78 rung items carry should, the issuer's own word, not threshold. 4.2 calls the threshold the minimum.
- The rung lists are not parallel (threshold 12, 7, 11; typical 11, 5, 8; excellent 11, 5, 8). gradeOf links are all inferred from plain content matches: 22 typical-to-threshold and 24 excellent-to-typical links (the ROWS table in run-src). For P3.
- 4.11.b10 and 4.14.b10 join the two threshold items 4.8.b10 (interdisciplinary elements) and 4.8.b11 (other disciplines); gradeOf points to 4.8.b10 only, and 4.8.b11 has no counterpart above.
- Unmatched items: threshold 4.9.b3 (records), 4.9.b4 (describe and evaluate events), 4.9.b7 (space), 4.10.b2 (adaptability), 4.10.b3 (risk), 4.10.b7 (communication), 4.10.b10 (project management) have no typical or excellent counterpart; typical 4.12.b1 and 4.13.b2 first appear above the threshold.
- Domains on the rungs are by outcome row: rows 1 to 5 of each knowledge list as knowledge, rows 6 to 12 as understanding, though the typical and excellent items read as "engagement"; 4.9.b2 opens with "understand" but is a skill list item (subject-skill). Generic skills at fheq:6; master's generic items at fheq:7.
- Master's: 4.17 lists five added outcomes for master's study (should), with no rungs; recorded as outcome items at fheq:7, award master's. A new pattern against Psychology. 4.17.b5 reads "complete of a major piece" (issuer's typo, kept in source).
- Outcome list 3.3: thirteen items under "Students will:" after a stem that says courses "should typically be designed to enable" the skills; items recorded with will. The stem's should sentence is not cut as its own record: 3.3 is also a reference in 3.1 ("paragraphs 3.2 and 3.3").
- Obliging words outside the five: 3.4 "are expected" recorded as describes; 2.24 "are required" recorded as must; 2.8, 2.9 and 4.14 "it is expected that" recorded with will or should as the sentence gives. Not cut: 1.17 "collective responsibility to embed", 1.28 "requires access" and "is crucial", 2.5 "It is vital that", 4.6 "It is important that" (inside a cut record), 1.27 "will see themselves reflected" (inside a noun clause).
- Plain-present provider norms, not statements (template open point 5): 1.13, 1.16, 1.20 (committed to), 1.21, 1.22, 1.25, 1.26, 1.29, 1.30, 1.34, 1.35, 1.37, 1.38, 2.1, 2.13, 2.15, 2.17, 2.22, 2.26, 3.2, 3.13, 3.14, 3.15 (course information list), 3.17.
- Not statements, judged: 1.11, 1.18 and 2.2 to 2.3 lists (descriptive), 1.33 (suggestions), 3.12 and 3.14 list items (typical modes and formats), 2.11, 2.12, 2.21 and 2.25 (may), 4.1, 4.4 and 4.5 (framing; 4.5 the typical goal).
- Recut by find (skeleton spans ran on into the next heading): 4.8.b12, 4.10.b11, 4.11.b11, 4.12.b5, 4.13.b8, 4.14.b11, 4.15.b5, 4.16.b8; and cut to their obliging sentence: 1.17, 2.24, 3.1, 3.4, 3.12, 3.15, 3.16, 4.7.
- Themes: the four named in 1.3 and 1.16 (sustainability, not ESD, in the body; ESD in the front matter and 1.31). Generative AI is a paragraph (1.15) inside Characteristics, not a section; recorded as theme:generative-ai. Employability is joined with enterprise in the front matter, under theme:enterprise.
- Frameworks: FHEQ and FQHEIS levels 6 and 7 / 10 and 11 are named in 2.2 and 2.11; 4.3 names The Frameworks for Higher Education Qualifications only for Annex D. The front matter names the Quality Assessment Framework for Wales and Scotland's Quality Enhancement Framework, which are quality frameworks, not qualification frameworks. CQFW not named; fheq:6 to cqfw:6 recorded as inferred.
- Bodies: PSRBs and funding and regulatory bodies are named only in general; the Office for Students in the front matter; the Disabled Students Commission only in section 5. None of their requirements is ingested.
- Inferred subject codes (P3 to confirm; held back from lookup): hecos 100708 stage design (for "scenography and theatre design"), hecos 100710 community theatre (for "applied and social theatre"), hecos 100700 theatre production (for production in 2.3). Dance theatre and writing for performance have no matching HECoS term.
- Awards: honours is the award of the rungs; the scope (1.2) covers taught postgraduate degrees, and 2.11 integrated master's at FHEQ 7 and FQHEIS 11; awardsCovered records both. CertHE and DipHE (2.12) are exit awards; fheq:4 and fheq:5 inferred.
- Annex D is cited in 4.3 without a date; linked to its current home in std:doc:qaa-fheq-2024-framework (SL6).
- Other references: Equality Act 2010 (1.17), UN SDGs and the 2030 Agenda and the Theatre Green Book (1.31) are not standards documents; recorded in S7 only.
- S9 commentary not researched in P1.
- Licence: QAA copyright; the document gives no re-use terms in its text.
- ST-12: versions here run to the lengths the content needs; no length range is yet set.

---

## Change notes
- 0.1.2, 3 October 2026, 21:02: moved with its held text from UNI to the source library repo (`wkspc2601-library/ingested/standards/`, texts in `txt/`, records in `records/`); paths only (Abbott, 20:56; std N-0119).
- 0.1.1, 3 October 2026, 20:20: obliging words outside the five read as must, "ought to" as should, on statements outside the rungs, each marked on its force line (Abbott, 20:17; D-std-0016).
- 0.1.0, 2026-10-03 16:54: researched by run frame 0.1.1-draft and standards run layer 0.7.0-draft, std, run 0099 (P1); built by tools/bm_build.py.
