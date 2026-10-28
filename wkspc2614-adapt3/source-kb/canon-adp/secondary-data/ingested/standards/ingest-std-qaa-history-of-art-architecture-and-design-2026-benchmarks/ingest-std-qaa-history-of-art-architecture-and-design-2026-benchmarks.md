---
id: std:doc:qaa-history-of-art-architecture-and-design-2026-benchmarks
title: "Subject Benchmark Statement: History of Art, Architecture and Design"
profile: standards/subject-benchmark
profileVersion: 0.2.0-draft
issuer: QAA
kind: subject-benchmark
jurisdiction: [UK]
subjectScope: subjects
subjects:
  - { scheme: "hecos", code: "100306", label: "history of art", basis: "stated" }
  - { scheme: "hecos", code: "100782", label: "history of architecture", basis: "stated" }
  - { scheme: "hecos", code: "100783", label: "history of design", basis: "stated" }
  - { scheme: "cah", code: "CAH20-01-02", label: "history of art, architecture and design", basis: "stated" }
edition: "April 2026 (fifth edition)"
published: 2026-04
status: current
supersedes: "the fourth edition, 2019 (minor update), as the back matter records"
heldText: { method: sha256-bytes, raw: 0cfad140e51634d734d72d1afd40a3f9cea7eaeae7317abfc50fea6b9924f4aa, normalised: 2c061d312657522130ab80641f0e2e7a724f9a62c93616b9270784a9e43f2275 }
heldTextStan: { method: sha256-stan, raw: 0cfad140e51634d734d72d1afd40a3f9cea7eaeae7317abfc50fea6b9924f4aa, normalised: 2ce43414b34363600fd3a3f1268709529a69d14a0a96b4876f3dc563d910395b }
licence: "QAA copyright; held for study, private to the project, never published"
series: "QAA Subject Benchmark Statements, 2026 revision (fifth edition for this subject)"
awardsCovered: ["bachelor's with honours", "master's"]
levelsCovered: ["fheq:6", "fheq:7", "fqheis:10", "fqheis:11"]
nations: ["England", "Wales", "Scotland", "Northern Ireland"]
parts:
  S: full
  B: "partial: no glossary in the document (it points to QAA's Glossary); terms it defines in passing"
  C: "not-applicable: the document sets expectations, not a procedure"
pins: { structure: 0.13.0-draft, template: 0.8.0-draft, benchmarkTemplate: 0.6.0-draft, runFrame: 0.1.1-draft, runLayer: 0.7.0-draft, standards: none yet, terminology: none yet }
lifecycle: drafted
researchedBy: run frame 0.1.1-draft; standards run layer 0.7.0-draft; std, run 0111 (tools/bm_build.py)
passes:
  P1: "2026-10-03 17:29"
  P2: "skipped: read direct from the held text; inferred codes and rung links are for P3"
  P3: open
version: 0.1.2
---

<!-- from INGEST wpk-0016-ingest-pd-template-standards.md 0.8.0-draft and wpk-0016-ingest-pd-template-standards-benchmark.md 0.6.0-draft; built by tools/bm_build.py from run-src/ -->
# Subject Benchmark Statement: History of Art, Architecture and Design (QAA, April 2026)

> Run 0111, P1 by std. The issuer's words are held in the source library, `wkspc2601-library/txt/qaa-2026-history-art-architecture-design-subject-benchmark-standard.norm.txt`; each S4 record carries its statement in full (`source`) for language analysis, with its span. Paraphrases and versions are ours. Private to the project, never published. In front matter `status` is the issuer's; ours is `lifecycle`. Doubts are in Part E.

## Part 0 Summary

### 0.1 Agent definition
<!-- label: editorial; status: drafted; basis: primary -->
QAA's UK reference point for what a graduate in the history of art, architecture and design (HAAD) can be expected to know and do at the end of an honours degree, with a short list for master's graduates. It holds a two-rung table (threshold and typical) across subject knowledge, subject-specific skills and generic intellectual skills, a list of transferable skills and a master's list. Reach for it when designing, reviewing or describing a HAAD course or its outcomes. It is not a curriculum and not a regulatory requirement in England.

### 0.2 Summary
<!-- label: both; status: drafted; basis: primary -->
Published by QAA in April 2026 as the fifth edition, the statement describes the subject's purposes and characteristics (the study of artefacts as visual and material culture, in every medium and period), the distinctive features of courses (design, progression, flexibility, partnerships, monitoring), content, teaching and assessment, and benchmark standards for the bachelor's degree with honours at two rungs, threshold (equivalent to a third) and typical (equivalent to a second), plus transferable skills and a master's list. It carries five cross-cutting themes: equity, diversity and inclusion; accessibility and the needs of disabled students; education for sustainable development; employability, entrepreneurship and enterprise education; and generative AI. It points to Annex D of the Frameworks for the four honours classes, cites the FHEQ and the FQHEIS (SCQF) for levels, and names PSRBs and the Equality and Human Rights Commission without naming a subject body.

## Part S Standard

### S1 Identity
<!-- label: source; status: drafted; basis: primary -->
```yaml
issuer: The Quality Assurance Agency for Higher Education
title: "Subject Benchmark Statement: History of Art, Architecture and Design"
edition: "April 2026 (fifth edition)"
dates:
  published: 2026-04
  other: []
kind: subject-benchmark
jurisdiction: [UK]
authority: "reference: a sector-owned reference point; in England not a sector-recognised standard under the OfS regulatory framework; part of the current quality arrangements in Scotland, Wales and Northern Ireland (D1, front matter: Relationship to legislation)"
licence: "QAA copyright; the document gives no re-use terms in its text (D1, front matter)"
copyrightNotice: { text: "© The Quality Assurance Agency for Higher Education 2026", locator: "D1, index" }
```

### S2 Purpose and scope
<!-- label: source; status: drafted; basis: primary -->
```yaml
governs: "what a HAAD graduate can be expected to know, do and understand at the end of an honours degree, with postgraduate standards for the master's degree, and the nature of awards in the subject (D1, front matter: About this Statement; 4.1; 4.4; 4.6)"
appliesTo:
  awards: ["bachelor's degree with honours", "integrated master's (described, 2.6, 2.12)", "master's degree (4.4, 4.6)", "joint and combined honours (2.8)"]
  levels: ["fheq:6", "fheq:7", "fqheis:10", "fqheis:11"]
  providers: ["UK higher education providers"]
whoMustUse: "none-stated; it is a reference point, not a requirement (D1, front matter)"
howUsed: ["design", "approval", "review", "other: external examining; PSRBs; information for prospective students and employers"]
doesNot: "it does not prescribe approaches to teaching, learning or assessment; it does not interpret legislation or carry statutory or regulatory requirements; its threshold standards are not universal competence standards (D1, front matter; 4.3)"
beneficiary: the student
statedScope: "\"This QAA Subject Benchmark Statement for History of Art, Architecture and Design defines what can be expected of a graduate in terms of what they might know, do and understand at the end of their studies.\" (D1, front matter: About this Statement)"
statedSubjects:
  - { name: "History of Art, Architecture and Design (HAAD)", locator: "(D1, title; 1.1)", kind: "subject", codes: [{ scheme: "hecos", code: "100306", label: "history of art" }, { scheme: "hecos", code: "100782", label: "history of architecture" }, { scheme: "hecos", code: "100783", label: "history of design" }, { scheme: "cah", code: "CAH20-01-02", label: "history of art, architecture and design" }] }
  - { name: "Fine Art", locator: "(D1, 1.2)", kind: "programme title", codes: [{ scheme: "hecos", code: "100059", label: "fine art" }] }
  - { name: "Design", locator: "(D1, 1.2)", kind: "programme title", codes: [{ scheme: "hecos", code: "100048", label: "design" }] }
  - { name: "Architecture", locator: "(D1, 1.2; 1.15)", kind: "programme title", codes: [{ scheme: "hecos", code: "100122", label: "architecture" }] }
  - { name: "History, Museum and Heritage Studies", locator: "(D1, 1.2)", kind: "programme title", codes: [{ scheme: "hecos", code: "100302", label: "history" }, { scheme: "hecos", code: "100918", label: "museum studies" }, { scheme: "hecos", code: "100805", label: "heritage studies" }] }
  - { name: "Curatorial Practice", locator: "(D1, 1.2)", kind: "programme title", codes: [{ scheme: "hecos", code: "100914", label: "curatorial studies" }] }
  - { name: "Photography, Film and Media Studies", locator: "(D1, 1.2)", kind: "programme title", codes: [{ scheme: "hecos", code: "100063", label: "photography" }, { scheme: "hecos", code: "100058", label: "film studies" }, { scheme: "hecos", code: "100444", label: "media and communication studies" }] }
  - { name: "Area Studies, Social Sciences and Humanities", locator: "(D1, 1.2)", kind: "programme title", codes: [] }
  - { name: "combined or joint degree (including major and minor options)", locator: "(D1, 2.8)", kind: "programme title", codes: [{ scheme: "cah", code: "CAH20-01-02", label: "history of art, architecture and design" }] }
subjects: see front matter (subjectScope subjects)
```

### S3 Structure
<!-- label: both; status: drafted; basis: primary -->
```yaml
components:
  - { number: "1.1", order: 3, componentType: paragraph, parent: "section 1", heading: "Context and purposes of a History of Art, Architecture", gloss: "the subject studies how images, objects and buildings shape societies" }
  - { number: "1.2", order: 4, componentType: paragraph, parent: "section 1", heading: "Context and purposes of a History of Art, Architecture", gloss: "an established field taught alone and inside many other degrees" }
  - { number: "1.3", order: 5, componentType: area, parent: "section 1", heading: "Purposes and characteristics of a History of Art, Architecture and Design degree", gloss: "artefacts named by medium, from painting to games" }
  - { number: "1.4", order: 6, componentType: paragraph, parent: "section 1", heading: "Purposes and characteristics of a History of Art, Architecture and Design degree", gloss: "art and design read as historical constructs; global scope" }
  - { number: "1.5", order: 7, componentType: area, parent: "section 1", heading: "Purposes and characteristics of a History of Art, Architecture and Design degree", gloss: "descriptive methods for the visual and material" }
  - { number: "1.6", order: 8, componentType: paragraph, parent: "section 1", heading: "Purposes and characteristics of a History of Art, Architecture and Design degree", gloss: "context, sources and the making and use of artefacts" }
  - { number: "1.7", order: 9, componentType: paragraph, parent: "section 1", heading: "Purposes and characteristics of a History of Art, Architecture and Design degree", gloss: "power, inequality and marginalised histories; sustainability" }
  - { number: "1.8", order: 10, componentType: paragraph, parent: "section 1", heading: "Purposes and characteristics of a History of Art, Architecture and Design degree", gloss: "display, institutions and digital access" }
  - { number: "1.9", order: 11, componentType: paragraph, parent: "section 1", heading: "Purposes and characteristics of a History of Art, Architecture and Design degree", gloss: "varied entrants; skills and careers of graduates" }
  - { number: "1.10", order: 12, componentType: paragraph, parent: "section 1", heading: "Equity, diversity and inclusion", gloss: "a safe environment beyond equality law" }
  - { number: "1.11", order: 13, componentType: paragraph, parent: "section 1", heading: "Equity, diversity and inclusion", gloss: "inclusive, object-centred learning and provenance" }
  - { number: "1.12", order: 14, componentType: paragraph, parent: "section 1", heading: "Equity, diversity and inclusion", gloss: "communities shaping the subject; wellbeing benefits" }
  - { number: "1.13", order: 15, componentType: paragraph, parent: "section 1", heading: "Accessibility and the needs of disabled students", gloss: "accessible methods and reasonable adjustment" }
  - { number: "1.14", order: 16, componentType: practice, parent: "section 1", heading: "Accessibility and the needs of disabled students", gloss: "varied delivery, off-campus study and digital tools" }
  - { number: "1.15", order: 17, componentType: paragraph, parent: "section 1", heading: "Accessibility and the needs of disabled students", gloss: "no prerequisites; portfolios; widening participation" }
  - { number: "1.16", order: 18, componentType: paragraph, parent: "section 1", heading: "Education for sustainable development", gloss: "artefacts and the UN goals" }
  - { number: "1.17", order: 19, componentType: paragraph, parent: "section 1", heading: "Education for sustainable development", gloss: "global links, resource use and sensitive artefacts" }
  - { number: "1.18", order: 20, componentType: paragraph, parent: "section 1", heading: "Education for sustainable development", gloss: "environmental cost of travel and digital technology" }
  - { number: "1.19", order: 21, componentType: paragraph, parent: "section 1", heading: "Employability, entrepreneurship and enterprise education", gloss: "what enterprise education does for students" }
  - { number: "1.20", order: 22, componentType: paragraph, parent: "section 1", heading: "Employability, entrepreneurship and enterprise education", gloss: "cultural economy and the museum and heritage sectors" }
  - { number: "1.21", order: 23, componentType: paragraph, parent: "section 1", heading: "Employability, entrepreneurship and enterprise education", gloss: "experiential tasks, placements and graduate destinations" }
  - { number: "1.22", order: 24, componentType: paragraph, parent: "section 1", heading: "Generative artificial intelligence", gloss: "guidance to students on generative AI" }
  - { number: "1.23", order: 25, componentType: paragraph, parent: "section 1", heading: "Generative artificial intelligence", gloss: "generative AI and questions of authorship and creativity" }
  - { number: "1.24", order: 26, componentType: paragraph, parent: "section 1", heading: "Generative artificial intelligence", gloss: "critical engagement with and disclosure of AI use" }
  - { number: "1.25", order: 27, componentType: paragraph, parent: "section 1", heading: "Generative artificial intelligence", gloss: "AI fluency and informed choices about use" }
  - { number: "1.26", order: 28, componentType: paragraph, parent: "section 1", heading: "Generative artificial intelligence", gloss: "AI in assessment: openings and concerns" }
  - { number: "2.1", order: 30, componentType: paragraph, parent: "section 2", heading: "Design", gloss: "range of periods, places, media and issues in design" }
  - { number: "2.2", order: 31, componentType: paragraph, parent: "section 2", heading: "Design", gloss: "visual literacy, interdisciplinarity and transferable skills" }
  - { number: "2.3", order: 32, componentType: paragraph, parent: "section 2", heading: "Design", gloss: "course design for year-on-year progression" }
  - { number: "2.4", order: 33, componentType: practice, parent: "section 2", heading: "Design", gloss: "digital resources and site-based learning" }
  - { number: "2.5", order: 34, componentType: practice, parent: "section 2", heading: "Design", gloss: "balanced, aligned assessment portfolio" }
  - { number: "2.6", order: 35, componentType: paragraph, parent: "section 2", heading: "Progression", gloss: "progression through levels to the threshold" }
  - { number: "2.7", order: 36, componentType: paragraph, parent: "section 2", heading: "Progression", gloss: "readiness for postgraduate study" }
  - { number: "2.8", order: 37, componentType: paragraph, parent: "section 2", heading: "Progression", gloss: "joint and combined degrees" }
  - { number: "2.9", order: 38, componentType: paragraph, parent: "section 2", heading: "Progression", gloss: "early exit awards" }
  - { number: "2.10", order: 39, componentType: paragraph, parent: "section 2", heading: "Flexibility", gloss: "bachelor's length outside Scotland" }
  - { number: "2.11", order: 40, componentType: paragraph, parent: "section 2", heading: "Flexibility", gloss: "Scottish degree structure and the MA title" }
  - { number: "2.12", order: 41, componentType: paragraph, parent: "section 2", heading: "Flexibility", gloss: "integrated master's length and level" }
  - { number: "2.13", order: 42, componentType: paragraph, parent: "section 2", heading: "Flexibility", gloss: "part-time credit" }
  - { number: "2.14", order: 43, componentType: paragraph, parent: "section 2", heading: "Flexibility", gloss: "modes of study and credit accumulation" }
  - { number: "2.15", order: 44, componentType: paragraph, parent: "section 2", heading: "Partnerships", gloss: "formal and informal partnerships" }
  - { number: "2.16", order: 45, componentType: paragraph, parent: "section 2", heading: "Partnerships", gloss: "inclusive, safe, contracted partnership learning" }
  - { number: "2.17", order: 46, componentType: paragraph, parent: "section 2", heading: "Partnerships", gloss: "partnerships for employability and hosts" }
  - { number: "2.18", order: 47, componentType: paragraph, parent: "section 2", heading: "Monitoring and review", gloss: "monitoring, evaluation and the student voice" }
  - { number: "2.19", order: 48, componentType: paragraph, parent: "section 2", heading: "Monitoring and review", gloss: "external reviewers in periodic review" }
  - { number: "2.20", order: 49, componentType: paragraph, parent: "section 2", heading: "Monitoring and review", gloss: "the external examining system" }
  - { number: "2.21", order: 50, componentType: paragraph, parent: "section 2", heading: "Monitoring and review", gloss: "professional accreditation of vocational courses" }
  - { number: "3.1", order: 52, componentType: paragraph, parent: "section 3", heading: "Content, structure and delivery", gloss: "what the section covers" }
  - { number: "3.2", order: 53, componentType: area, parent: "section 3", heading: "Content", gloss: "diverse content set by local circumstance" }
  - { number: "3.3", order: 54, componentType: paragraph, parent: "section 3", heading: "Content", gloss: "from core skills to a final-year project" }
  - { number: "3.4", order: 55, componentType: practice, parent: "section 3", heading: "Content", gloss: "research-informed teaching and collections partnerships" }
  - { number: "3.5", order: 56, componentType: area, parent: "section 3", heading: "Content", gloss: "historiography, physical properties and current contexts" }
  - { number: "3.6", order: 57, componentType: practice, parent: "section 3", heading: "Teaching and learning", gloss: "competences built through varied formats" }
  - { number: "3.7", order: 58, componentType: practice, parent: "section 3", heading: "Teaching and learning", gloss: "inclusive design and study visits" }
  - { number: "3.8", order: 59, componentType: practice, parent: "section 3", heading: "Teaching and learning", gloss: "indicative teaching methods and approaches" }
  - { number: "3.9", order: 60, componentType: practice, parent: "section 3", heading: "Assessment", gloss: "assessment within learning; handbooks" }
  - { number: "3.10", order: 61, componentType: practice, parent: "section 3", heading: "Assessment", gloss: "effective, flexible, aligned assessment" }
  - { number: "3.11", order: 62, componentType: practice, parent: "section 3", heading: "Assessment", gloss: "self- and peer assessment" }
  - { number: "3.12", order: 63, componentType: practice, parent: "section 3", heading: "Assessment", gloss: "generative AI and the assessment portfolio" }
  - { number: "3.13", order: 64, componentType: practice, parent: "section 3", heading: "Assessment", gloss: "indicative assessment methods; inclusive by design" }
  - { number: "4.1", order: 66, componentType: paragraph, parent: "section 4", heading: "Introduction", gloss: "what the standards set out" }
  - { number: "4.2", order: 67, componentType: paragraph, parent: "section 4", heading: "Introduction", gloss: "performance above threshold; Annex D" }
  - { number: "4.3", order: 68, componentType: paragraph, parent: "section 4", heading: "Introduction", gloss: "not competence standards; EHRC guidance" }
  - { number: "4.4", order: 69, componentType: paragraph, parent: "section 4", heading: "Introduction", gloss: "two rungs defined; the threshold and typical table" }
  - { number: "4.5", order: 70, componentType: stem, parent: "section 4", heading: "Transferable skills", gloss: "transferable skills on graduating with honours" }
  - { number: "4.6", order: 71, componentType: stem, parent: "section 4", heading: "Master's level", gloss: "outcomes on graduating with a master's" }
  - { number: "1", componentType: section, parent: none, heading: "Context and purposes of a History of Art, Architecture and Design degree", gloss: "section 1" }
  - { number: "2", componentType: section, parent: none, heading: "Distinctive features of HAAD courses", gloss: "section 2" }
  - { number: "3", componentType: section, parent: none, heading: "Content, structure and delivery", gloss: "section 3" }
  - { number: "4", componentType: section, parent: none, heading: "Benchmark standards", gloss: "section 4" }
excluded:
  - { number: "none", heading: "Contents; About this Statement; How can I use this document?; Relationship to legislation; Additional sector reference points", kind: "other: front matter, read for S1, S2 and SB6" }
  - { number: "section headings 1 to 4", heading: "the four section heading lines", kind: "other: headings, recorded in SECTIONS" }
  - { number: "5", heading: "Membership of the Advisory Group (2026, 2019, 2016, 2007, 2002)", kind: "other: back matter, read for S7 and S8" }
  - { number: "none", heading: "Fifth Edition; Published 16 April 2026; copyright notice", kind: "other: colophon, read for S1 and S8" }
```

### S4 Statements
<!-- label: both; status: drafted; basis: primary. Only standards (D-std-0002 (a)): 60 records. `source` is the issuer's statement exactly as its span holds it (D-std-0014). -->
```yaml
- id: qaa/history-of-art-architecture-and-design-2026/2.3
  locator: { number: "2.3", headingPath: ["Distinctive features of HAAD courses", "Design"] }
  span: { start: 32934, end: 33435 }
  source: "2.3 Course design teams make use of institutional guidance and external reference points to assist them in determining programme specifications and learning outcomes, setting appropriate levels of challenge and framing curriculum content. The design of courses will consider how content, learning and teaching in each year will provide the necessary knowledge, skills and ways of thinking to allow all students to subsequently progress to more complex problems and phenomena (see also paragraph 3.3).\n"
  stem: none
  statementType: expectation
  rung: none
  force: will
  level: none
  appliesTo: "course design teams"
  addressee: provider
  verbs: ["consider", "provide", "progress"]
  about: "course design for progression across years"
  themes: [none]
  domain: none
  award: ["bachelor's with honours"]
  gradeOf: none
  paraphrase: "Course design teams use institutional guidance and external reference points for specifications, outcomes, challenge and content; the design will consider how each year's content and teaching prepares every student to move on to harder problems."
  quote: full   # the issuer's statement is in `source` (D-std-0014)
  audience: practitioner
  subjects: inherited
- id: qaa/history-of-art-architecture-and-design-2026/2.6
  locator: { number: "2.6", headingPath: ["Distinctive features of HAAD courses", "Progression"] }
  span: { start: 34491, end: 35229 }
  source: "2.6 Over the course of a standard undergraduate degree with honours (FHEQ Level 6; FQHEIS Level 10) or, if available, an integrated master's degree (FHEQ Level 7; FQHEIS Level 11), a HAAD student will progress from one level of study to the next, in line with the regulations and processes for each institution. However, it is expected that each level would see the attainment of knowledge, expertise and experience that builds towards the final achievement of meeting the threshold (and, if specified, higher-level) subject-specific and generic skills listed in this Statement. This will usually include successful completion and the award of credit for the full range of learning and assessment, including any practical components.\n\n10\n"
  stem: none
  statementType: expectation
  rung: none
  force: will
  level: none
  appliesTo: "honours and integrated master's students"
  addressee: learner
  verbs: ["progress", "include"]
  about: "progression through the levels to the threshold"
  themes: [none]
  domain: none
  award: ["bachelor's with honours", "integrated master's"]
  gradeOf: none
  paraphrase: "A student will move up through the levels as each institution's rules set out, each level expected to build knowledge, expertise and experience towards the threshold (and any higher) subject and generic skills; this will usually mean passing and gaining credit for all learning and assessment, practical work included."
  quote: full   # the issuer's statement is in `source` (D-std-0014)
  audience: both
  subjects: inherited
- id: qaa/history-of-art-architecture-and-design-2026/2.8
  locator: { number: "2.8", headingPath: ["Distinctive features of HAAD courses", "Progression"] }
  span: { start: 35631, end: 36102 }
  source: "2.8 Undergraduates studying HAAD courses as part of a combined or joint degree with other subjects (including courses that specify major and minor options) will achieve core elements of the specific and generic skills outlined in this Statement and will add others according to the areas covered in the other subject(s) of their degree. Additionally, they may explore the overlap between different disciplines, creating further opportunities for interdisciplinary study.\n"
  stem: none
  statementType: outcome
  rung: none
  force: will
  level: fheq:6
  appliesTo: "students taking HAAD in joint or combined degrees"
  addressee: learner
  verbs: ["achieve", "add", "explore"]
  about: "joint and combined degrees"
  themes: [none]
  domain: none
  award: ["bachelor's with honours"]
  gradeOf: none
  paraphrase: "Students taking HAAD within a joint or combined degree, major and minor routes included, will reach the core of the subject and generic skills set out here and will add further skills from their other subject or subjects."
  quote: full   # the issuer's statement is in `source` (D-std-0014)
  audience: both
  subjects: inherited
- id: qaa/history-of-art-architecture-and-design-2026/2.18
  locator: { number: "2.18", headingPath: ["Distinctive features of HAAD courses", "Monitoring and review"] }
  span: { start: 41112, end: 41336 }
  source: "Degree-awarding bodies, and their collaborative partnerships, routinely collect and analyse information and undertake periodic course review according to their own needs. Considering the student voice will form part of this."
  stem: none
  statementType: expectation
  rung: none
  force: will
  level: none
  appliesTo: "degree-awarding bodies and their partners"
  addressee: provider
  verbs: ["collect", "analyse", "undertake", "form"]
  about: "periodic review and the student voice"
  themes: [none]
  domain: none
  award: ["bachelor's with honours"]
  gradeOf: none
  paraphrase: "Degree-awarding bodies and their partners routinely gather and analyse information and review courses periodically to suit their needs; the student voice will be considered as part of this."
  quote: full   # the issuer's statement is in `source` (D-std-0014)
  audience: practitioner
  subjects: inherited
- id: qaa/history-of-art-architecture-and-design-2026/2.19
  locator: { number: "2.19", headingPath: ["Distinctive features of HAAD courses", "Monitoring and review"] }
  span: { start: 41751, end: 42049 }
  source: "2.19 Externality is an essential component of the quality assurance system in the UK. Providers will use external reviewers as part of periodic review to gain an independent perspective on any proposed changes and ensure threshold standards are achieved and content is appropriate for the subject.\n"
  stem: none
  statementType: expectation
  rung: none
  force: will
  level: none
  appliesTo: "providers"
  addressee: provider
  verbs: ["use", "gain", "ensure"]
  about: "external reviewers in periodic review"
  themes: [none]
  domain: none
  award: ["bachelor's with honours"]
  gradeOf: none
  paraphrase: "Externality is essential to UK quality assurance; providers will use external reviewers in periodic review for an independent view of proposed changes and to make sure threshold standards are met and content suits the subject."
  quote: full   # the issuer's statement is in `source` (D-std-0014)
  audience: practitioner
  subjects: inherited
- id: qaa/history-of-art-architecture-and-design-2026/3.13
  locator: { number: "3.13", headingPath: ["Content, structure and delivery", "Assessment"] }
  span: { start: 51854, end: 51986 }
  source: "Assessment methods will be inclusive by design. Considerations for accessibility and inclusivity will determine forms of assessment."
  stem: none
  statementType: expectation
  rung: none
  force: will
  level: none
  appliesTo: "those who design assessment"
  addressee: provider
  verbs: ["determine"]
  about: "inclusive, accessible assessment design"
  themes: [none]
  domain: none
  award: ["bachelor's with honours"]
  gradeOf: none
  paraphrase: "Assessment methods will be inclusive from the outset, and accessibility and inclusion will shape which forms of assessment are used."
  quote: full   # the issuer's statement is in `source` (D-std-0014)
  audience: practitioner
  subjects: inherited
- id: qaa/history-of-art-architecture-and-design-2026/4.2
  locator: { number: "4.2", headingPath: ["Benchmark standards", "Introduction"] }
  span: { start: 53446, end: 53931 }
  source: "4.2 The vast majority of students will perform significantly better than the minimum threshold standards. Each higher education provider has its own method of determining what appropriate evidence of this achievement will be and should refer to Annex D in The Frameworks for Higher Education Qualifications of UK Degree-Awarding Bodies. This Annex sets out common descriptions of the four main degree outcome classifications for bachelor's degrees with honours: 1st, 2.1, 2.2 and 3rd.\n"
  stem: none
  statementType: expectation
  rung: none
  force: should
  level: fheq:6
  appliesTo: "providers"
  addressee: provider
  verbs: ["perform", "refer"]
  about: "evidence above threshold; Annex D"
  themes: [none]
  domain: none
  award: ["bachelor's with honours"]
  gradeOf: none
  paraphrase: "Most students will do far better than the minimum threshold; each provider decides how to evidence that achievement and should refer to Annex D of the Frameworks, which describes the four honours classes (1st, 2.1, 2.2, 3rd)."
  quote: full   # the issuer's statement is in `source` (D-std-0014)
  audience: practitioner
  subjects: inherited
- id: qaa/history-of-art-architecture-and-design-2026/4.3
  locator: { number: "4.3", headingPath: ["Benchmark standards", "Introduction"] }
  span: { start: 53931, end: 54411 }
  source: "4.3 Please note that the minimum threshold standards are not intended to specify universal competence standards for a discipline. If a provider chooses to develop competence standards (as defined by the Equality Act 2010) as part of a programme specification, these can be informed by the relevant Subject Benchmark Statement along with any PSRB requirements. In these circumstances, providers should follow the most recent guidance from the Equality and Human Rights Commission.\n"
  stem: none
  statementType: requirement
  rung: none
  force: should
  level: none
  appliesTo: "providers that develop competence standards"
  addressee: provider
  verbs: ["follow"]
  about: "competence standards and EHRC guidance"
  themes: [none]
  domain: none
  award: ["bachelor's with honours"]
  gradeOf: none
  paraphrase: "The minimum threshold standards do not set universal competence standards; a provider that develops competence standards under the Equality Act 2010 may draw on the statement and PSRB requirements, and should follow the latest Equality and Human Rights Commission guidance."
  quote: full   # the issuer's statement is in `source` (D-std-0014)
  audience: practitioner
  subjects: inherited
- id: qaa/history-of-art-architecture-and-design-2026/4.4.b1
  locator: { number: "4.4.b1", headingPath: ["Benchmark standards", "Introduction"] }
  span: { start: 55057, end: 55176 }
  source: "Analyse and interpret the visual and material culture of more than one geographical region and/or chronological period."
  stem: "4.4"
  statementType: threshold
  rung: threshold
  force: threshold
  level: fheq:6
  appliesTo: "honours graduates at the threshold"
  addressee: learner
  verbs: ["analyse", "interpret"]
  about: "visual and material culture of more than one region or period"
  themes: [none]
  domain: knowledge
  award: ["bachelor's with honours"]
  gradeOf: none
  paraphrase: "At threshold, can analyse and interpret the art and objects of at least two regions or periods."
  quote: full   # the issuer's statement is in `source` (D-std-0014)
  audience: both
  subjects: inherited
- id: qaa/history-of-art-architecture-and-design-2026/4.4.b1.typical
  locator: { number: "4.4.b1.typical", headingPath: ["Benchmark standards", "Introduction"] }
  span: { start: 55177, end: 55350 }
  source: "Devise and sustain arguments relating to the knowledge and understanding of the visual and material culture of more than one geographical region and/or chronological period."
  stem: "4.4"
  statementType: typical
  rung: typical
  force: will
  level: fheq:6
  appliesTo: "honours graduates at the typical level"
  addressee: learner
  verbs: ["devise", "sustain"]
  about: "arguments about the culture of more than one region or period"
  themes: [none]
  domain: knowledge
  award: ["bachelor's with honours"]
  gradeOf: { statement: qaa/history-of-art-architecture-and-design-2026/4.4.b1, basis: stated }
  paraphrase: "At the typical level, will build and hold arguments about the visual and material culture of at least two regions or periods."
  quote: full   # the issuer's statement is in `source` (D-std-0014)
  audience: both
  subjects: inherited
- id: qaa/history-of-art-architecture-and-design-2026/4.4.b2
  locator: { number: "4.4.b2", headingPath: ["Benchmark standards", "Introduction"] }
  span: { start: 55351, end: 55470 }
  source: "Describe and comment upon the materials and techniques through which artefacts are constructed in the cultures studied."
  stem: "4.4"
  statementType: threshold
  rung: threshold
  force: threshold
  level: fheq:6
  appliesTo: "honours graduates at the threshold"
  addressee: learner
  verbs: ["describe", "comment"]
  about: "materials and making techniques of artefacts"
  themes: [none]
  domain: knowledge
  award: ["bachelor's with honours"]
  gradeOf: none
  paraphrase: "At threshold, can describe and remark on the materials and making techniques of artefacts in the cultures studied."
  quote: full   # the issuer's statement is in `source` (D-std-0014)
  audience: both
  subjects: inherited
- id: qaa/history-of-art-architecture-and-design-2026/4.4.b2.typical
  locator: { number: "4.4.b2.typical", headingPath: ["Benchmark standards", "Introduction"] }
  span: { start: 55471, end: 55640 }
  source: "Devise and sustain arguments relating to the knowledge and understanding of the materials and techniques through which artefacts are constructed in the cultures studied."
  stem: "4.4"
  statementType: typical
  rung: typical
  force: will
  level: fheq:6
  appliesTo: "honours graduates at the typical level"
  addressee: learner
  verbs: ["devise", "sustain"]
  about: "arguments from knowledge of materials and techniques"
  themes: [none]
  domain: knowledge
  award: ["bachelor's with honours"]
  gradeOf: { statement: qaa/history-of-art-architecture-and-design-2026/4.4.b2, basis: stated }
  paraphrase: "At the typical level, will build and hold arguments from knowledge of how and from what the artefacts of the cultures studied were made."
  quote: full   # the issuer's statement is in `source` (D-std-0014)
  audience: both
  subjects: inherited
- id: qaa/history-of-art-architecture-and-design-2026/4.4.b3
  locator: { number: "4.4.b3", headingPath: ["Benchmark standards", "Introduction"] }
  span: { start: 55641, end: 55697 }
  source: "Follow current debates and approaches to the discipline."
  stem: "4.4"
  statementType: threshold
  rung: threshold
  force: threshold
  level: fheq:6
  appliesTo: "honours graduates at the threshold"
  addressee: learner
  verbs: ["follow"]
  about: "current debates and approaches in the discipline"
  themes: [none]
  domain: understanding
  award: ["bachelor's with honours"]
  gradeOf: none
  paraphrase: "At threshold, can keep up with the discipline's present debates and approaches."
  quote: full   # the issuer's statement is in `source` (D-std-0014)
  audience: both
  subjects: inherited
- id: qaa/history-of-art-architecture-and-design-2026/4.4.b3.typical
  locator: { number: "4.4.b3.typical", headingPath: ["Benchmark standards", "Introduction"] }
  span: { start: 55698, end: 55841 }
  source: "Demonstrate sound knowledge of current debates and approaches to the discipline and accurately deploy established techniques of interpretation."
  stem: "4.4"
  statementType: typical
  rung: typical
  force: will
  level: fheq:6
  appliesTo: "honours graduates at the typical level"
  addressee: learner
  verbs: ["demonstrate", "deploy"]
  about: "sound knowledge of debates; accurate interpretive technique"
  themes: [none]
  domain: understanding
  award: ["bachelor's with honours"]
  gradeOf: { statement: qaa/history-of-art-architecture-and-design-2026/4.4.b3, basis: stated }
  paraphrase: "At the typical level, will show secure knowledge of the discipline's present debates and approaches and use its recognised methods of interpretation accurately."
  quote: full   # the issuer's statement is in `source` (D-std-0014)
  audience: both
  subjects: inherited
- id: qaa/history-of-art-architecture-and-design-2026/4.4.b4
  locator: { number: "4.4.b4", headingPath: ["Benchmark standards", "Introduction"] }
  span: { start: 55842, end: 55997 }
  source: "Demonstrate some familiarity with professional practice in the arts and creative cultural industries, including museums, galleries and the heritage sector."
  stem: "4.4"
  statementType: threshold
  rung: threshold
  force: threshold
  level: fheq:6
  appliesTo: "honours graduates at the threshold"
  addressee: learner
  verbs: ["demonstrate"]
  about: "some acquaintance with how the arts and heritage sectors work"
  themes: [none]
  domain: knowledge
  award: ["bachelor's with honours"]
  gradeOf: none
  paraphrase: "At threshold, will show some acquaintance with professional practice in the arts and cultural industries, such as museums, galleries and heritage."
  quote: full   # the issuer's statement is in `source` (D-std-0014)
  audience: both
  subjects: inherited
- id: qaa/history-of-art-architecture-and-design-2026/4.4.b4.typical
  locator: { number: "4.4.b4.typical", headingPath: ["Benchmark standards", "Introduction"] }
  span: { start: 55998, end: 56187 }
  source: "Engage with professional practice in the arts and creative cultural industries, including museums, galleries and the heritage sector that can be used to devise arguments and solve problems."
  stem: "4.4"
  statementType: typical
  rung: typical
  force: will
  level: fheq:6
  appliesTo: "honours graduates at the typical level"
  addressee: learner
  verbs: ["engage", "devise", "solve"]
  about: "using professional practice to argue and solve problems"
  themes: [none]
  domain: knowledge
  award: ["bachelor's with honours"]
  gradeOf: { statement: qaa/history-of-art-architecture-and-design-2026/4.4.b4, basis: stated }
  paraphrase: "At the typical level, will engage with professional practice in museums, galleries, heritage and the creative industries and draw on it to argue and solve problems."
  quote: full   # the issuer's statement is in `source` (D-std-0014)
  audience: both
  subjects: inherited
- id: qaa/history-of-art-architecture-and-design-2026/4.4.b5
  locator: { number: "4.4.b5", headingPath: ["Benchmark standards", "Introduction"] }
  span: { start: 56192, end: 56310 }
  source: "Analyse the ways art, design and architecture contribute to and reflect upon the formation of cultures and identities."
  stem: "4.4"
  statementType: threshold
  rung: threshold
  force: threshold
  level: fheq:6
  appliesTo: "honours graduates at the threshold"
  addressee: learner
  verbs: ["analyse", "contribute", "reflect"]
  about: "how art, design and architecture shape cultures and identities"
  themes: [none]
  domain: understanding
  award: ["bachelor's with honours"]
  gradeOf: none
  paraphrase: "At threshold, can analyse how art, design and architecture help shape, and comment on, cultures and identities."
  quote: full   # the issuer's statement is in `source` (D-std-0014)
  audience: both
  subjects: inherited
- id: qaa/history-of-art-architecture-and-design-2026/4.4.b5.typical
  locator: { number: "4.4.b5.typical", headingPath: ["Benchmark standards", "Introduction"] }
  span: { start: 56311, end: 56439 }
  source: "Apply theories to the ways art, design and architecture contribute to and reflect upon the formation of cultures and identities."
  stem: "4.4"
  statementType: typical
  rung: typical
  force: will
  level: fheq:6
  appliesTo: "honours graduates at the typical level"
  addressee: learner
  verbs: ["apply", "contribute", "reflect"]
  about: "theory applied to art, culture and identity"
  themes: [none]
  domain: understanding
  award: ["bachelor's with honours"]
  gradeOf: { statement: qaa/history-of-art-architecture-and-design-2026/4.4.b5, basis: stated }
  paraphrase: "At the typical level, will apply theory to how art, design and architecture shape and reflect cultures and identities."
  quote: full   # the issuer's statement is in `source` (D-std-0014)
  audience: both
  subjects: inherited
- id: qaa/history-of-art-architecture-and-design-2026/4.4.b6
  locator: { number: "4.4.b6", headingPath: ["Benchmark standards", "Introduction"] }
  span: { start: 56543, end: 56625 }
  source: "Apply basic skills of observation and visual and material description in analysis."
  stem: "4.4"
  statementType: threshold
  rung: threshold
  force: threshold
  level: fheq:6
  appliesTo: "honours graduates at the threshold"
  addressee: learner
  verbs: ["apply"]
  about: "basic observation and description in analysis"
  themes: [none]
  domain: subject-skill
  award: ["bachelor's with honours"]
  gradeOf: none
  paraphrase: "At threshold, can use basic observation and visual and material description when analysing."
  quote: full   # the issuer's statement is in `source` (D-std-0014)
  audience: both
  subjects: inherited
- id: qaa/history-of-art-architecture-and-design-2026/4.4.b6.typical
  locator: { number: "4.4.b6.typical", headingPath: ["Benchmark standards", "Introduction"] }
  span: { start: 56626, end: 56759 }
  source: "Deploy skills of observation and visual and material description to the interpretation of artefacts and the elaboration of arguments."
  stem: "4.4"
  statementType: typical
  rung: typical
  force: will
  level: fheq:6
  appliesTo: "honours graduates at the typical level"
  addressee: learner
  verbs: ["deploy"]
  about: "observation and description put to interpretation and argument"
  themes: [none]
  domain: subject-skill
  award: ["bachelor's with honours"]
  gradeOf: { statement: qaa/history-of-art-architecture-and-design-2026/4.4.b6, basis: stated }
  paraphrase: "At the typical level, will use observation and description of visual and material qualities to interpret artefacts and develop arguments."
  quote: full   # the issuer's statement is in `source` (D-std-0014)
  audience: both
  subjects: inherited
- id: qaa/history-of-art-architecture-and-design-2026/4.4.b7
  locator: { number: "4.4.b7", headingPath: ["Benchmark standards", "Introduction"] }
  span: { start: 56760, end: 56845 }
  source: "Situate artefacts within appropriate environmental, historical and cultural contexts."
  stem: "4.4"
  statementType: threshold
  rung: threshold
  force: threshold
  level: fheq:6
  appliesTo: "honours graduates at the threshold"
  addressee: learner
  verbs: ["situate"]
  about: "placing artefacts in context, environmental included"
  themes: [none]
  domain: subject-skill
  award: ["bachelor's with honours"]
  gradeOf: none
  paraphrase: "At threshold, can place artefacts in fitting environmental, historical and cultural contexts."
  quote: full   # the issuer's statement is in `source` (D-std-0014)
  audience: both
  subjects: inherited
- id: qaa/history-of-art-architecture-and-design-2026/4.4.b7.typical
  locator: { number: "4.4.b7.typical", headingPath: ["Benchmark standards", "Introduction"] }
  span: { start: 56846, end: 56963 }
  source: "Situate artefacts within appropriate historical and cultural contexts to advance enquiry within the HAAD disciplines."
  stem: "4.4"
  statementType: typical
  rung: typical
  force: will
  level: fheq:6
  appliesTo: "honours graduates at the typical level"
  addressee: learner
  verbs: ["situate", "advance"]
  about: "context used to advance enquiry"
  themes: [none]
  domain: subject-skill
  award: ["bachelor's with honours"]
  gradeOf: { statement: qaa/history-of-art-architecture-and-design-2026/4.4.b7, basis: stated }
  paraphrase: "At the typical level, will place artefacts in fitting historical and cultural contexts so as to move enquiry in the discipline forward."
  quote: full   # the issuer's statement is in `source` (D-std-0014)
  audience: both
  subjects: inherited
- id: qaa/history-of-art-architecture-and-design-2026/4.4.b8
  locator: { number: "4.4.b8", headingPath: ["Benchmark standards", "Introduction"] }
  span: { start: 56964, end: 57145 }
  source: "Use evidence from relevant interdisciplinary sources (visual, verbal, textual, technical, primary and secondary) in relation to current issues and enquiries in the HAAD disciplines."
  stem: "4.4"
  statementType: threshold
  rung: threshold
  force: threshold
  level: fheq:6
  appliesTo: "honours graduates at the threshold"
  addressee: learner
  verbs: ["use"]
  about: "interdisciplinary evidence on current issues"
  themes: [none]
  domain: subject-skill
  award: ["bachelor's with honours"]
  gradeOf: none
  paraphrase: "At threshold, can use evidence of many kinds from across disciplines, such as images, texts, technical data and primary and secondary material, on current questions in the discipline."
  quote: full   # the issuer's statement is in `source` (D-std-0014)
  audience: both
  subjects: inherited
- id: qaa/history-of-art-architecture-and-design-2026/4.4.b8.typical
  locator: { number: "4.4.b8.typical", headingPath: ["Benchmark standards", "Introduction"] }
  span: { start: 57146, end: 57327 }
  source: "Locate, use and evaluate evidence from relevant interdisciplinary sources (visual, verbal, textual, technical, primary and secondary) to advance inquiry within the HAAD disciplines."
  stem: "4.4"
  statementType: typical
  rung: typical
  force: will
  level: fheq:6
  appliesTo: "honours graduates at the typical level"
  addressee: learner
  verbs: ["locate", "use", "evaluate", "advance"]
  about: "finding and weighing interdisciplinary evidence"
  themes: [none]
  domain: subject-skill
  award: ["bachelor's with honours"]
  gradeOf: { statement: qaa/history-of-art-architecture-and-design-2026/4.4.b8, basis: stated }
  paraphrase: "At the typical level, will find, use and weigh evidence from many kinds of source across disciplines to advance enquiry in the discipline."
  quote: full   # the issuer's statement is in `source` (D-std-0014)
  audience: both
  subjects: inherited
- id: qaa/history-of-art-architecture-and-design-2026/4.4.b9
  locator: { number: "4.4.b9", headingPath: ["Benchmark standards", "Introduction"] }
  span: { start: 57328, end: 57433 }
  source: "Demonstrate awareness of methodologies, theories and approaches established in the HAAD discipline areas."
  stem: "4.4"
  statementType: threshold
  rung: threshold
  force: threshold
  level: fheq:6
  appliesTo: "honours graduates at the threshold"
  addressee: learner
  verbs: ["demonstrate"]
  about: "awareness of the discipline's methods and theories"
  themes: [none]
  domain: subject-skill
  award: ["bachelor's with honours"]
  gradeOf: none
  paraphrase: "At threshold, will show awareness of the discipline's established methods, theories and approaches."
  quote: full   # the issuer's statement is in `source` (D-std-0014)
  audience: both
  subjects: inherited
- id: qaa/history-of-art-architecture-and-design-2026/4.4.b9.typical
  locator: { number: "4.4.b9.typical", headingPath: ["Benchmark standards", "Introduction"] }
  span: { start: 57434, end: 57533 }
  source: "Deploy appropriate methodologies, theories and approaches established in the HAAD discipline areas."
  stem: "4.4"
  statementType: typical
  rung: typical
  force: will
  level: fheq:6
  appliesTo: "honours graduates at the typical level"
  addressee: learner
  verbs: ["deploy"]
  about: "choosing and using fitting methods and theories"
  themes: [none]
  domain: subject-skill
  award: ["bachelor's with honours"]
  gradeOf: { statement: qaa/history-of-art-architecture-and-design-2026/4.4.b9, basis: stated }
  paraphrase: "At the typical level, will use suitable established methods, theories and approaches of the discipline."
  quote: full   # the issuer's statement is in `source` (D-std-0014)
  audience: both
  subjects: inherited
- id: qaa/history-of-art-architecture-and-design-2026/4.4.b10
  locator: { number: "4.4.b10", headingPath: ["Benchmark standards", "Introduction"] }
  span: { start: 57534, end: 57654 }
  source: "Show some ability to produce relevant arguments and concepts supported by visual, textual or other appropriate evidence."
  stem: "4.4"
  statementType: threshold
  rung: threshold
  force: threshold
  level: fheq:6
  appliesTo: "honours graduates at the threshold"
  addressee: learner
  verbs: ["show", "produce"]
  about: "relevant arguments backed by evidence"
  themes: [none]
  domain: subject-skill
  award: ["bachelor's with honours"]
  gradeOf: none
  paraphrase: "At threshold, will show some ability to make relevant arguments and concepts backed by visual, written or other fitting evidence."
  quote: full   # the issuer's statement is in `source` (D-std-0014)
  audience: both
  subjects: inherited
- id: qaa/history-of-art-architecture-and-design-2026/4.4.b10.typical
  locator: { number: "4.4.b10.typical", headingPath: ["Benchmark standards", "Introduction"] }
  span: { start: 57655, end: 57810 }
  source: "Consistently demonstrate an ability to produce cohesive, well-structured and relevant arguments supported by visual, textual or other appropriate evidence."
  stem: "4.4"
  statementType: typical
  rung: typical
  force: will
  level: fheq:6
  appliesTo: "honours graduates at the typical level"
  addressee: learner
  verbs: ["demonstrate", "produce"]
  about: "consistent, well-built, evidenced argument"
  themes: [none]
  domain: subject-skill
  award: ["bachelor's with honours"]
  gradeOf: { statement: qaa/history-of-art-architecture-and-design-2026/4.4.b10, basis: stated }
  paraphrase: "At the typical level, will consistently make coherent, well-organised, relevant arguments backed by fitting visual, written or other evidence."
  quote: full   # the issuer's statement is in `source` (D-std-0014)
  audience: both
  subjects: inherited
- id: qaa/history-of-art-architecture-and-design-2026/4.4.b11
  locator: { number: "4.4.b11", headingPath: ["Benchmark standards", "Introduction"] }
  span: { start: 57811, end: 57879 }
  source: "Discern the difference between alternative arguments and approaches."
  stem: "4.4"
  statementType: threshold
  rung: threshold
  force: threshold
  level: fheq:6
  appliesTo: "honours graduates at the threshold"
  addressee: learner
  verbs: ["discern"]
  about: "telling alternative arguments apart"
  themes: [none]
  domain: subject-skill
  award: ["bachelor's with honours"]
  gradeOf: none
  paraphrase: "At threshold, can tell alternative arguments and approaches apart."
  quote: full   # the issuer's statement is in `source` (D-std-0014)
  audience: both
  subjects: inherited
- id: qaa/history-of-art-architecture-and-design-2026/4.4.b11.typical
  locator: { number: "4.4.b11.typical", headingPath: ["Benchmark standards", "Introduction"] }
  span: { start: 57881, end: 58002 }
  source: "Demonstrate critical judgement and the ability to evaluate alternative arguments and to engage with competing approaches."
  stem: "4.4"
  statementType: typical
  rung: typical
  force: will
  level: fheq:6
  appliesTo: "honours graduates at the typical level"
  addressee: learner
  verbs: ["demonstrate", "evaluate", "engage"]
  about: "critical judgement between competing approaches"
  themes: [none]
  domain: subject-skill
  award: ["bachelor's with honours"]
  gradeOf: { statement: qaa/history-of-art-architecture-and-design-2026/4.4.b11, basis: stated }
  paraphrase: "At the typical level, will show critical judgement, weighing alternative arguments and engaging with rival approaches."
  quote: full   # the issuer's statement is in `source` (D-std-0014)
  audience: both
  subjects: inherited
- id: qaa/history-of-art-architecture-and-design-2026/4.4.b12
  locator: { number: "4.4.b12", headingPath: ["Benchmark standards", "Introduction"] }
  span: { start: 58032, end: 58116 }
  source: "Communicate comprehensibly in a variety of media, using visual aids where necessary."
  stem: "4.4"
  statementType: threshold
  rung: threshold
  force: threshold
  level: fheq:6
  appliesTo: "honours graduates at the threshold"
  addressee: learner
  verbs: ["communicate", "using"]
  about: "understandable communication in varied media"
  themes: [none]
  domain: generic-skill
  award: ["bachelor's with honours"]
  gradeOf: none
  paraphrase: "At threshold, can communicate understandably in various media, with visual aids where needed."
  quote: full   # the issuer's statement is in `source` (D-std-0014)
  audience: both
  subjects: inherited
- id: qaa/history-of-art-architecture-and-design-2026/4.4.b12.typical
  locator: { number: "4.4.b12.typical", headingPath: ["Benchmark standards", "Introduction"] }
  span: { start: 58118, end: 58244 }
  source: "Communicate effectively in a variety of media with specialist and non-specialist audiences, using visual aids where necessary."
  stem: "4.4"
  statementType: typical
  rung: typical
  force: will
  level: fheq:6
  appliesTo: "honours graduates at the typical level"
  addressee: learner
  verbs: ["communicate", "using"]
  about: "effective communication to expert and lay audiences"
  themes: [none]
  domain: generic-skill
  award: ["bachelor's with honours"]
  gradeOf: { statement: qaa/history-of-art-architecture-and-design-2026/4.4.b12, basis: stated }
  paraphrase: "At the typical level, will communicate effectively in various media to specialist and general audiences, with visual aids where needed."
  quote: full   # the issuer's statement is in `source` (D-std-0014)
  audience: both
  subjects: inherited
- id: qaa/history-of-art-architecture-and-design-2026/4.4.b13
  locator: { number: "4.4.b13", headingPath: ["Benchmark standards", "Introduction"] }
  span: { start: 58245, end: 58322 }
  source: "Undertake information gathering and basic research with guidance and support."
  stem: "4.4"
  statementType: threshold
  rung: threshold
  force: threshold
  level: fheq:6
  appliesTo: "honours graduates at the threshold"
  addressee: learner
  verbs: ["undertake"]
  about: "guided information gathering and basic research"
  themes: [none]
  domain: generic-skill
  award: ["bachelor's with honours"]
  gradeOf: none
  paraphrase: "At threshold, can gather information and carry out basic research with guidance and help."
  quote: full   # the issuer's statement is in `source` (D-std-0014)
  audience: both
  subjects: inherited
- id: qaa/history-of-art-architecture-and-design-2026/4.4.b13.typical
  locator: { number: "4.4.b13.typical", headingPath: ["Benchmark standards", "Introduction"] }
  span: { start: 58323, end: 58489 }
  source: "Conduct self-directed research demonstrating a capacity for effective and verifiable information retrieval, critical review and organisation relevant to a given task."
  stem: "4.4"
  statementType: typical
  rung: typical
  force: will
  level: fheq:6
  appliesTo: "honours graduates at the typical level"
  addressee: learner
  verbs: ["conduct", "demonstrating"]
  about: "self-directed, verifiable research"
  themes: [none]
  domain: generic-skill
  award: ["bachelor's with honours"]
  gradeOf: { statement: qaa/history-of-art-architecture-and-design-2026/4.4.b13, basis: stated }
  paraphrase: "At the typical level, will carry out self-directed research, retrieving information effectively and verifiably, reviewing it critically and organising it for the task."
  quote: full   # the issuer's statement is in `source` (D-std-0014)
  audience: both
  subjects: inherited
- id: qaa/history-of-art-architecture-and-design-2026/4.4.b14
  locator: { number: "4.4.b14", headingPath: ["Benchmark standards", "Introduction"] }
  span: { start: 58490, end: 58578 }
  source: "Display open-mindedness: be receptive to unfamiliar artefacts, issues, values and ideas."
  stem: "4.4"
  statementType: threshold
  rung: threshold
  force: threshold
  level: fheq:6
  appliesTo: "honours graduates at the threshold"
  addressee: learner
  verbs: ["display"]
  about: "open-mindedness to the unfamiliar"
  themes: [none]
  domain: generic-skill
  award: ["bachelor's with honours"]
  gradeOf: none
  paraphrase: "At threshold, will show open-mindedness, being open to artefacts, issues, values and ideas they have not met before."
  quote: full   # the issuer's statement is in `source` (D-std-0014)
  audience: both
  subjects: inherited
- id: qaa/history-of-art-architecture-and-design-2026/4.4.b14.typical
  locator: { number: "4.4.b14.typical", headingPath: ["Benchmark standards", "Introduction"] }
  span: { start: 58579, end: 58771 }
  source: "Demonstrate the ability to take an inclusive approach to interpretation by taking into account the ideas, contexts and structures out of which various visual and material cultures have arisen."
  stem: "4.4"
  statementType: typical
  rung: typical
  force: will
  level: fheq:6
  appliesTo: "honours graduates at the typical level"
  addressee: learner
  verbs: ["demonstrate", "take", "taking"]
  about: "inclusive interpretation"
  themes: [none]
  domain: generic-skill
  award: ["bachelor's with honours"]
  gradeOf: { statement: qaa/history-of-art-architecture-and-design-2026/4.4.b14, basis: stated }
  paraphrase: "At the typical level, will show they can interpret inclusively, allowing for the ideas, contexts and structures from which different visual and material cultures emerged."
  quote: full   # the issuer's statement is in `source` (D-std-0014)
  audience: both
  subjects: inherited
- id: qaa/history-of-art-architecture-and-design-2026/4.4.b15
  locator: { number: "4.4.b15", headingPath: ["Benchmark standards", "Introduction"] }
  span: { start: 58772, end: 58837 }
  source: "Identify underlying values and ethics within culture and society."
  stem: "4.4"
  statementType: threshold
  rung: threshold
  force: threshold
  level: fheq:6
  appliesTo: "honours graduates at the threshold"
  addressee: learner
  verbs: ["identify"]
  about: "values and ethics in culture and society"
  themes: [none]
  domain: generic-skill
  award: ["bachelor's with honours"]
  gradeOf: none
  paraphrase: "At threshold, can identify the values and ethics that underlie culture and society."
  quote: full   # the issuer's statement is in `source` (D-std-0014)
  audience: both
  subjects: inherited
- id: qaa/history-of-art-architecture-and-design-2026/4.4.b15.typical
  locator: { number: "4.4.b15.typical", headingPath: ["Benchmark standards", "Introduction"] }
  span: { start: 58838, end: 58915 }
  source: "Identify and examine underlying values and ethics within culture and society."
  stem: "4.4"
  statementType: typical
  rung: typical
  force: will
  level: fheq:6
  appliesTo: "honours graduates at the typical level"
  addressee: learner
  verbs: ["identify", "examine"]
  about: "examining values and ethics in culture and society"
  themes: [none]
  domain: generic-skill
  award: ["bachelor's with honours"]
  gradeOf: { statement: qaa/history-of-art-architecture-and-design-2026/4.4.b15, basis: stated }
  paraphrase: "At the typical level, will identify and also examine the values and ethics that underlie culture and society."
  quote: full   # the issuer's statement is in `source` (D-std-0014)
  audience: both
  subjects: inherited
- id: qaa/history-of-art-architecture-and-design-2026/4.5.b1
  locator: { number: "4.5.b1", headingPath: ["Benchmark standards", "Transferable skills"] }
  span: { start: 59017, end: 59155 }
  source: "present knowledge or an argument that is comprehensible to others while\n\n19\ndemonstrating a sound technical proficiency of written English"
  stem: "4.5"
  statementType: outcome
  rung: none
  force: should
  level: fheq:6
  appliesTo: "honours graduates"
  addressee: learner
  verbs: ["present", "demonstrating"]
  about: "clear presentation in sound written English"
  themes: [none]
  domain: generic-skill
  award: ["bachelor's with honours"]
  gradeOf: none
  paraphrase: "Should be able to put knowledge or a case so others can follow it, with technically sound written English."
  quote: full   # the issuer's statement is in `source` (D-std-0014)
  audience: both
  subjects: inherited
- id: qaa/history-of-art-architecture-and-design-2026/4.5.b2
  locator: { number: "4.5.b2", headingPath: ["Benchmark standards", "Transferable skills"] }
  span: { start: 59156, end: 59207 }
  source: "work as part of a team as an effective collaborator"
  stem: "4.5"
  statementType: outcome
  rung: none
  force: should
  level: fheq:6
  appliesTo: "honours graduates"
  addressee: learner
  verbs: ["work"]
  about: "effective teamwork"
  themes: [none]
  domain: generic-skill
  award: ["bachelor's with honours"]
  gradeOf: none
  paraphrase: "Should be able to collaborate well as a member of a team."
  quote: full   # the issuer's statement is in `source` (D-std-0014)
  audience: both
  subjects: inherited
- id: qaa/history-of-art-architecture-and-design-2026/4.5.b3
  locator: { number: "4.5.b3", headingPath: ["Benchmark standards", "Transferable skills"] }
  span: { start: 59210, end: 59279 }
  source: "research and study effectively in a guided and structured environment"
  stem: "4.5"
  statementType: outcome
  rung: none
  force: should
  level: fheq:6
  appliesTo: "honours graduates"
  addressee: learner
  verbs: ["research", "study"]
  about: "effective study where learning is guided"
  themes: [none]
  domain: generic-skill
  award: ["bachelor's with honours"]
  gradeOf: none
  paraphrase: "Should be able to research and study well in a guided, structured setting."
  quote: full   # the issuer's statement is in `source` (D-std-0014)
  audience: both
  subjects: inherited
- id: qaa/history-of-art-architecture-and-design-2026/4.5.b4
  locator: { number: "4.5.b4", headingPath: ["Benchmark standards", "Transferable skills"] }
  span: { start: 59282, end: 59409 }
  source: "appreciate and engage in contemporary debates relating to culture and society, for example around inequality and sustainability"
  stem: "4.5"
  statementType: outcome
  rung: none
  force: should
  level: fheq:6
  appliesTo: "honours graduates"
  addressee: learner
  verbs: ["appreciate", "engage"]
  about: "current debates on culture and society"
  themes: [none]
  domain: generic-skill
  award: ["bachelor's with honours"]
  gradeOf: none
  paraphrase: "Should be able to value and take part in current debates on culture and society, such as those on inequality and sustainability."
  quote: full   # the issuer's statement is in `source` (D-std-0014)
  audience: both
  subjects: inherited
- id: qaa/history-of-art-architecture-and-design-2026/4.5.b5
  locator: { number: "4.5.b5", headingPath: ["Benchmark standards", "Transferable skills"] }
  span: { start: 59412, end: 59530 }
  source: "use digital technologies (including GenAI, used and applied ethically) to research, select and communicate information"
  stem: "4.5"
  statementType: outcome
  rung: none
  force: should
  level: fheq:6
  appliesTo: "honours graduates"
  addressee: learner
  verbs: ["use", "research", "select", "communicate"]
  about: "ethical use of digital tools and GenAI"
  themes: [none]
  domain: generic-skill
  award: ["bachelor's with honours"]
  gradeOf: none
  paraphrase: "Should be able to use digital technologies, generative AI included and used ethically, to research, choose and convey information."
  quote: full   # the issuer's statement is in `source` (D-std-0014)
  audience: both
  subjects: inherited
- id: qaa/history-of-art-architecture-and-design-2026/4.5.b6
  locator: { number: "4.5.b6", headingPath: ["Benchmark standards", "Transferable skills"] }
  span: { start: 59533, end: 59609 }
  source: "work diligently, to take appropriate decisions and meet assessment deadlines"
  stem: "4.5"
  statementType: outcome
  rung: none
  force: should
  level: fheq:6
  appliesTo: "honours graduates"
  addressee: learner
  verbs: ["work", "take", "meet"]
  about: "diligence, decisions and deadlines"
  themes: [none]
  domain: generic-skill
  award: ["bachelor's with honours"]
  gradeOf: none
  paraphrase: "Should be able to work conscientiously, make sound decisions and keep to assessment deadlines."
  quote: full   # the issuer's statement is in `source` (D-std-0014)
  audience: both
  subjects: inherited
- id: qaa/history-of-art-architecture-and-design-2026/4.5.b7
  locator: { number: "4.5.b7", headingPath: ["Benchmark standards", "Transferable skills"] }
  span: { start: 59612, end: 59697 }
  source: "take responsibility for their own work, understanding questions of academic integrity"
  stem: "4.5"
  statementType: outcome
  rung: none
  force: should
  level: fheq:6
  appliesTo: "honours graduates"
  addressee: learner
  verbs: ["take", "understanding"]
  about: "responsibility for own work; academic integrity"
  themes: [none]
  domain: generic-skill
  award: ["bachelor's with honours"]
  gradeOf: none
  paraphrase: "Should be able to take responsibility for their work and understand what academic integrity asks of it."
  quote: full   # the issuer's statement is in `source` (D-std-0014)
  audience: both
  subjects: inherited
- id: qaa/history-of-art-architecture-and-design-2026/4.5.b8
  locator: { number: "4.5.b8", headingPath: ["Benchmark standards", "Transferable skills"] }
  span: { start: 59700, end: 59825 }
  source: "reflect on their own progress, making appropriate use of feedback to further intellectual development and improve performance"
  stem: "4.5"
  statementType: outcome
  rung: none
  force: should
  level: fheq:6
  appliesTo: "honours graduates"
  addressee: learner
  verbs: ["reflect", "making"]
  about: "reflection and use of feedback"
  themes: [none]
  domain: generic-skill
  award: ["bachelor's with honours"]
  gradeOf: none
  paraphrase: "Should be able to reflect on their progress and use feedback well to develop intellectually and do better."
  quote: full   # the issuer's statement is in `source` (D-std-0014)
  audience: both
  subjects: inherited
- id: qaa/history-of-art-architecture-and-design-2026/4.5.b9
  locator: { number: "4.5.b9", headingPath: ["Benchmark standards", "Transferable skills"] }
  span: { start: 59828, end: 59933 }
  source: "identify and examine underlying values and ethics both within culture and society and on a personal level"
  stem: "4.5"
  statementType: outcome
  rung: none
  force: should
  level: fheq:6
  appliesTo: "honours graduates"
  addressee: learner
  verbs: ["identify", "examine"]
  about: "values and ethics, personal as well as social"
  themes: [none]
  domain: generic-skill
  award: ["bachelor's with honours"]
  gradeOf: none
  paraphrase: "Should be able to identify and examine the values and ethics beneath culture and society and in their own lives."
  quote: full   # the issuer's statement is in `source` (D-std-0014)
  audience: both
  subjects: inherited
- id: qaa/history-of-art-architecture-and-design-2026/4.5.b10
  locator: { number: "4.5.b10", headingPath: ["Benchmark standards", "Transferable skills"] }
  span: { start: 59936, end: 60027 }
  source: "exhibit some awareness of the inherent uncertainty, ambiguities and the limits of knowledge"
  stem: "4.5"
  statementType: outcome
  rung: none
  force: should
  level: fheq:6
  appliesTo: "honours graduates"
  addressee: learner
  verbs: ["exhibit"]
  about: "awareness of uncertainty and the limits of knowledge"
  themes: [none]
  domain: generic-skill
  award: ["bachelor's with honours"]
  gradeOf: none
  paraphrase: "Should be able to show some awareness that knowledge is uncertain, ambiguous and limited."
  quote: full   # the issuer's statement is in `source` (D-std-0014)
  audience: both
  subjects: inherited
- id: qaa/history-of-art-architecture-and-design-2026/4.6.b1.masters
  locator: { number: "4.6.b1.masters", headingPath: ["Benchmark standards", "Master's level"] }
  span: { start: 60134, end: 60187 }
  source: "demonstrate sophisticated and nuanced visual literacy"
  stem: "4.6"
  statementType: typical
  rung: typical
  force: should
  level: fheq:7
  appliesTo: "master's graduates"
  addressee: learner
  verbs: ["demonstrate"]
  about: "refined visual literacy"
  themes: [none]
  domain: subject-skill
  award: ["master's"]
  gradeOf: none
  paraphrase: "Should typically be able to show refined, subtle visual literacy."
  quote: full   # the issuer's statement is in `source` (D-std-0014)
  audience: both
  subjects: inherited
- id: qaa/history-of-art-architecture-and-design-2026/4.6.b2.masters
  locator: { number: "4.6.b2.masters", headingPath: ["Benchmark standards", "Master's level"] }
  span: { start: 60190, end: 60326 }
  source: "systematically and critically engage with texts and artefacts, as well as theories and methods for examining visual and material culture"
  stem: "4.6"
  statementType: typical
  rung: typical
  force: should
  level: fheq:7
  appliesTo: "master's graduates"
  addressee: learner
  verbs: ["engage"]
  about: "systematic, critical work with texts, artefacts and theory"
  themes: [none]
  domain: subject-skill
  award: ["master's"]
  gradeOf: none
  paraphrase: "Should typically be able to engage systematically and critically with texts, artefacts and the theories and methods for studying visual and material culture."
  quote: full   # the issuer's statement is in `source` (D-std-0014)
  audience: both
  subjects: inherited
- id: qaa/history-of-art-architecture-and-design-2026/4.6.b3.masters
  locator: { number: "4.6.b3.masters", headingPath: ["Benchmark standards", "Master's level"] }
  span: { start: 60329, end: 60488 }
  source: "demonstrate awareness of how methodologies and research trends in the discipline have challenged assumptions and interpretations of art, architecture or design"
  stem: "4.6"
  statementType: typical
  rung: typical
  force: should
  level: fheq:7
  appliesTo: "master's graduates"
  addressee: learner
  verbs: ["demonstrate", "challenged"]
  about: "how methods and research have unsettled received readings"
  themes: [none]
  domain: understanding
  award: ["master's"]
  gradeOf: none
  paraphrase: "Should typically be able to show how the discipline's methods and research trends have unsettled earlier assumptions and readings of art, architecture or design."
  quote: full   # the issuer's statement is in `source` (D-std-0014)
  audience: both
  subjects: inherited
- id: qaa/history-of-art-architecture-and-design-2026/4.6.b4.masters
  locator: { number: "4.6.b4.masters", headingPath: ["Benchmark standards", "Master's level"] }
  span: { start: 60491, end: 60639 }
  source: "use unfamiliar arguments and artefacts constructively, while engaging critically with prominent, familiar or established ideas within the discipline"
  stem: "4.6"
  statementType: typical
  rung: typical
  force: should
  level: fheq:7
  appliesTo: "master's graduates"
  addressee: learner
  verbs: ["use", "engaging"]
  about: "unfamiliar material set against established ideas"
  themes: [none]
  domain: subject-skill
  award: ["master's"]
  gradeOf: none
  paraphrase: "Should typically be able to use unfamiliar arguments and artefacts productively while engaging critically with well-known or established ideas."
  quote: full   # the issuer's statement is in `source` (D-std-0014)
  audience: both
  subjects: inherited
- id: qaa/history-of-art-architecture-and-design-2026/4.6.b5.masters
  locator: { number: "4.6.b5.masters", headingPath: ["Benchmark standards", "Master's level"] }
  span: { start: 60642, end: 60745 }
  source: "demonstrate advanced knowledge of the place of HAAD in relation to larger social and political contexts"
  stem: "4.6"
  statementType: typical
  rung: typical
  force: should
  level: fheq:7
  appliesTo: "master's graduates"
  addressee: learner
  verbs: ["demonstrate"]
  about: "the subject in its social and political setting"
  themes: [none]
  domain: knowledge
  award: ["master's"]
  gradeOf: none
  paraphrase: "Should typically be able to show advanced knowledge of how the discipline sits within wider social and political contexts."
  quote: full   # the issuer's statement is in `source` (D-std-0014)
  audience: both
  subjects: inherited
- id: qaa/history-of-art-architecture-and-design-2026/4.6.b6.masters
  locator: { number: "4.6.b6.masters", headingPath: ["Benchmark standards", "Master's level"] }
  span: { start: 60748, end: 60872 }
  source: "form a systematic and critically engaged approach to the representation of art in museums, galleries and the heritage sector"
  stem: "4.6"
  statementType: typical
  rung: typical
  force: should
  level: fheq:7
  appliesTo: "master's graduates"
  addressee: learner
  verbs: ["form"]
  about: "a critical approach to display and representation"
  themes: [none]
  domain: subject-skill
  award: ["master's"]
  gradeOf: none
  paraphrase: "Should typically be able to develop a systematic, critical approach to how art is represented in museums, galleries and heritage."
  quote: full   # the issuer's statement is in `source` (D-std-0014)
  audience: both
  subjects: inherited
- id: qaa/history-of-art-architecture-and-design-2026/4.6.b7.masters
  locator: { number: "4.6.b7.masters", headingPath: ["Benchmark standards", "Master's level"] }
  span: { start: 60875, end: 60957 }
  source: "demonstrate comprehensive grounding in skills of analysis, argument and expression"
  stem: "4.6"
  statementType: typical
  rung: typical
  force: should
  level: fheq:7
  appliesTo: "master's graduates"
  addressee: learner
  verbs: ["demonstrate"]
  about: "grounding in analysis, argument and expression"
  themes: [none]
  domain: generic-skill
  award: ["master's"]
  gradeOf: none
  paraphrase: "Should typically be able to show thorough grounding in analysis, argument and expression."
  quote: full   # the issuer's statement is in `source` (D-std-0014)
  audience: both
  subjects: inherited
- id: qaa/history-of-art-architecture-and-design-2026/4.6.b8.masters
  locator: { number: "4.6.b8.masters", headingPath: ["Benchmark standards", "Master's level"] }
  span: { start: 60960, end: 61068 }
  source: "assemble data from a variety of relevant primary and secondary sources, and discern connections between them"
  stem: "4.6"
  statementType: typical
  rung: typical
  force: should
  level: fheq:7
  appliesTo: "master's graduates"
  addressee: learner
  verbs: ["assemble", "discern"]
  about: "assembling and connecting sources"
  themes: [none]
  domain: generic-skill
  award: ["master's"]
  gradeOf: none
  paraphrase: "Should typically be able to gather data from varied relevant primary and secondary sources and see the links between them."
  quote: full   # the issuer's statement is in `source` (D-std-0014)
  audience: both
  subjects: inherited
- id: qaa/history-of-art-architecture-and-design-2026/4.6.b9.masters
  locator: { number: "4.6.b9.masters", headingPath: ["Benchmark standards", "Master's level"] }
  span: { start: 61071, end: 61171 }
  source: "recognise their own academic strengths and weaknesses, and reflect on their performance and progress"
  stem: "4.6"
  statementType: typical
  rung: typical
  force: should
  level: fheq:7
  appliesTo: "master's graduates"
  addressee: learner
  verbs: ["recognise", "reflect"]
  about: "self-knowledge and reflection"
  themes: [none]
  domain: generic-skill
  award: ["master's"]
  gradeOf: none
  paraphrase: "Should typically be able to see where they are strong and weak academically and think about how they are performing and progressing."
  quote: full   # the issuer's statement is in `source` (D-std-0014)
  audience: both
  subjects: inherited
- id: qaa/history-of-art-architecture-and-design-2026/4.6.b10.masters
  locator: { number: "4.6.b10.masters", headingPath: ["Benchmark standards", "Master's level"] }
  span: { start: 61174, end: 61295 }
  source: "identify the relationship between different intellectual approaches and choose those appropriate to a particular instance"
  stem: "4.6"
  statementType: typical
  rung: typical
  force: should
  level: fheq:7
  appliesTo: "master's graduates"
  addressee: learner
  verbs: ["identify", "choose"]
  about: "relating approaches and choosing one"
  themes: [none]
  domain: generic-skill
  award: ["master's"]
  gradeOf: none
  paraphrase: "Should typically be able to see how different intellectual approaches relate and pick the right one for a given case."
  quote: full   # the issuer's statement is in `source` (D-std-0014)
  audience: both
  subjects: inherited
- id: qaa/history-of-art-architecture-and-design-2026/4.6.b11.masters
  locator: { number: "4.6.b11.masters", headingPath: ["Benchmark standards", "Master's level"] }
  span: { start: 61298, end: 61350 }
  source: "carry out a self-directed, original research project"
  stem: "4.6"
  statementType: typical
  rung: typical
  force: should
  level: fheq:7
  appliesTo: "master's graduates"
  addressee: learner
  verbs: ["carry"]
  about: "an original, self-directed research project"
  themes: [none]
  domain: subject-skill
  award: ["master's"]
  gradeOf: none
  paraphrase: "Should typically be able to complete an original research project that they direct themselves."
  quote: full   # the issuer's statement is in `source` (D-std-0014)
  audience: both
  subjects: inherited
- id: qaa/history-of-art-architecture-and-design-2026/4.6.b12.masters
  locator: { number: "4.6.b12.masters", headingPath: ["Benchmark standards", "Master's level"] }
  span: { start: 61353, end: 61451 }
  source: "communicate ideas and structured arguments effectively to specialist and non- specialist audiences"
  stem: "4.6"
  statementType: typical
  rung: typical
  force: should
  level: fheq:7
  appliesTo: "master's graduates"
  addressee: learner
  verbs: ["communicate"]
  about: "communication to expert and lay audiences"
  themes: [none]
  domain: generic-skill
  award: ["master's"]
  gradeOf: none
  paraphrase: "Should typically be able to convey ideas and structured arguments effectively to expert and general audiences."
  quote: full   # the issuer's statement is in `source` (D-std-0014)
  audience: both
  subjects: inherited
```

### S4a Audience versions
<!-- label: both; status: drafted; basis: primary. forPractitioner: for the programme designer or teacher. forBeneficiary: for the student, second person, naming no issuer. author-agent-written: instructions to an AI agent writing about the statement (a course document, a handbook, an outcome, a report). author-agent-dialogue: instructions to an AI agent using the statement in conversation (with a student, a teacher or a programme team). Written fresh from the held text alone (benchmark rule 6; Abbott, 15:42). -->
```yaml
- statement: qaa/history-of-art-architecture-and-design-2026/2.3
  forPractitioner: { text: "Use institutional guidance and external reference points to set outcomes and challenge; the design will need to show how each year's content, learning and teaching equips all students for more complex work the next year.", rewrite: light, force: will, status: drafted }
  forBeneficiary: { text: "not-applicable: a duty on course design teams; the student meets its effect in how the years build", rewrite: full, force: will, status: drafted }
  author-agent-written: "Treat this as an expectation, in will, on course design teams rather than students: a HAAD honours course is designed so each year readies all students for harder problems. Cite it as (QAA, 2026, History of Art, Architecture and Design Subject Benchmark Statement, para 2.3) and read it with 3.3, which describes the move from core skills to a final-year project. Do not present it as a regulatory requirement. Set it beside the level descriptors qaa/fheq-2024/4.10, 4.12 and 4.15 and spine:4 to spine:6."
  author-agent-dialogue: "Raise this with a programme team planning or reviewing year-by-year structure. Frame it as a design check and ask \"Which skills does each year introduce, and where does the next year depend on them?\" and \"Could every student, whatever their route in, make the step up?\" Do not put it to a student as their own task; it describes the course's duty."
- statement: qaa/history-of-art-architecture-and-design-2026/2.6
  forPractitioner: { text: "Plan each level so that students will build towards the threshold skills listed for the award; progression usually depends on passing and earning credit for every part of the course, practical components included.", rewrite: light, force: will, status: drafted }
  forBeneficiary: { text: "You will move up one level each year as your university's rules allow, building towards the skills your degree asks for; usually that means passing every part of the course, including practical work, and earning its credit.", rewrite: full, force: will, status: drafted }
  author-agent-written: "Describe this as the expected route, in will, by which an honours student (FHEQ Level 6; FQHEIS Level 10) or an integrated master's student (FHEQ Level 7; FQHEIS Level 11) progresses towards the threshold standards in 4.4 and 4.5. Cite it as (QAA, 2026, History of Art, Architecture and Design Subject Benchmark Statement, para 2.6). Do not claim it sets progression rules, which stay with each institution. Set it beside the threshold cells 4.4.b1 to 4.4.b15, the descriptors qaa/fheq-2024/4.10, 4.12, 4.15 and 4.17, and spine:4 to spine:7."
  author-agent-dialogue: "Raise this when a student asks what moving from one year to the next involves, or a team maps credit to levels. Tell a student in plain words that each year builds towards the skills the degree asks for and that passing every part, practical work included, is usually needed; ask \"Which parts of this year are you less sure of passing?\" Avoid quoting the institution's regulations as if this statement set them."
- statement: qaa/history-of-art-architecture-and-design-2026/2.8
  forPractitioner: { text: "In joint, combined and major/minor routes, design the HAAD share so that students will achieve the core subject-specific and generic skills of this statement, while their other subject adds its own.", rewrite: light, force: will, status: drafted }
  forBeneficiary: { text: "If you study HAAD as part of a joint or combined degree, you will gain the core subject and general skills of the field and add others from your second subject.", rewrite: full, force: will, status: drafted }
  author-agent-written: "Present this as the expected outcome, in will, for students taking HAAD in a joint, combined or major/minor honours degree at FHEQ Level 6 (FQHEIS Level 10): the core of the skills in 4.4 and 4.5, not every one of them. Cite it as (QAA, 2026, History of Art, Architecture and Design Subject Benchmark Statement, para 2.8). Do not claim that a joint-honours student must meet every cell of 4.4, or that the statement says which elements are core. Set it beside 4.4, 4.5 and qaa/fheq-2024/4.15.b1."
  author-agent-dialogue: "Raise this when a joint-honours student or a team designing a combined route asks how much of the HAAD standard applies. Explain plainly that the core subject skills still apply and the other subject adds its own; ask \"Which HAAD skills does your route give you the chance to show, and which come from your other subject?\" Avoid suggesting that joint honours is a lesser standard."
- statement: qaa/history-of-art-architecture-and-design-2026/2.18
  forPractitioner: { text: "Your periodic course review, alone or with partners, will take account of what students say, alongside the data you routinely gather and analyse.", rewrite: light, force: will, status: drafted }
  forBeneficiary: { text: "not-applicable: a duty on the degree-awarding body in course review", rewrite: full, force: will, status: drafted }
  author-agent-written: "Treat this as an expectation, in will, on degree-awarding bodies and their partners: periodic course review takes account of the student voice. Cite it as (QAA, 2026, History of Art, Architecture and Design Subject Benchmark Statement, para 2.18). Do not present it as a student outcome or as a regulatory requirement. Set it beside 2.19 (external reviewers) and the external examining system the statement describes in 2.20."
  author-agent-dialogue: "Raise this with a programme team preparing a periodic review or answering student feedback. Frame it in practitioner terms and ask \"How did students' views reach this review, and what changed because of them?\" Do not hand it to a student as a task; it is the institution's duty, though students can be told their views count."
- statement: qaa/history-of-art-architecture-and-design-2026/2.19
  forPractitioner: { text: "In periodic review you will bring in external reviewers, for an independent view on proposed changes and a check that threshold standards are met and content fits the subject.", rewrite: light, force: will, status: drafted }
  forBeneficiary: { text: "not-applicable: a duty on the provider in periodic review", rewrite: full, force: will, status: drafted }
  author-agent-written: "Present this as an expectation, in will, on providers: external reviewers take part in periodic review to check that the threshold standards (4.4, 4.5) are achieved and content suits the subject. Cite it as (QAA, 2026, History of Art, Architecture and Design Subject Benchmark Statement, para 2.19). Do not present it as a learner outcome. Set it beside 2.18, 2.20 and the threshold cells 4.4.b1 to 4.4.b15."
  author-agent-dialogue: "Raise this when a programme team plans a periodic review or asks who checks its standards. Frame it as practice the team will follow and ask \"Who is your external reviewer, and which threshold standards will they look at?\" Avoid presenting it to students as something they must meet."
- statement: qaa/history-of-art-architecture-and-design-2026/3.13
  forPractitioner: { text: "Design assessment to be inclusive from the start: accessibility and inclusion will decide which forms of assessment you use, rather than being added afterwards.", rewrite: light, force: will, status: drafted }
  forBeneficiary: { text: "not-applicable: a duty on those who design assessment; the student meets its effect", rewrite: full, force: will, status: drafted }
  author-agent-written: "Treat this as an expectation, in will, on those who design assessment on a HAAD course: methods are inclusive by design and accessibility shapes their form. Cite it as (QAA, 2026, History of Art, Architecture and Design Subject Benchmark Statement, para 3.13) and read it with the accessibility paragraphs 1.13 to 1.15. Do not present the indicative list of methods in 3.13 as required. Set it beside 3.10, 3.11 and the Equality Act 2010 duties the statement cites in 1.13."
  author-agent-dialogue: "Raise this when a team is choosing or revising assessment, or a disabled student asks about adjustments. With staff, ask \"Was accessibility decided before this assessment was set, or added afterwards?\"; with a student, explain in plain words that assessment should be designed with their needs in mind and point them to the course's support. Avoid giving the student this as a duty of their own."
- statement: qaa/history-of-art-architecture-and-design-2026/4.2
  forPractitioner: { text: "To evidence achievement above threshold, you should use Annex D of the Frameworks, its descriptions of first, upper second, lower second and third-class honours, alongside your own method.", rewrite: light, force: should, status: drafted }
  forBeneficiary: { text: "not-applicable: a duty on the provider in judging and classifying achievement; the student meets it through marks and class", rewrite: full, force: should, status: drafted }
  author-agent-written: "Treat this as a duty, in should, on each provider: to judge achievement above threshold it refers to Annex D of the Frameworks (std:doc:qaa-fheq-2024-framework, qaa/fheq-2024/annex-d/summary/r1/3rd to 1st). Cite it as (QAA, 2026, History of Art, Architecture and Design Subject Benchmark Statement, para 4.2). Do not claim the statement itself sets class boundaries or mark bands. Set it beside the threshold and typical cells of 4.4, the Annex D bands (SL6 of the FHEQ document) and the band axis of std:ref:uk-assesscriteria."
  author-agent-dialogue: "Raise this when a team writes marking criteria or asks how the threshold and typical rungs relate to degree classes. Frame it for staff: threshold sits at the third-class line and typical at second class, while Annex D describes all four classes; ask \"Do your criteria for a 2.1 and a first say more than the typical cells do?\" Avoid telling students that most of them will exceed the threshold as if it were a promise."
- statement: qaa/history-of-art-architecture-and-design-2026/4.3
  forPractitioner: { text: "The threshold standards are not competence standards; if you set competence standards in a programme specification, inform them from this statement and any PSRB requirements, and you should follow the current Equality and Human Rights Commission guidance.", rewrite: light, force: should, status: drafted }
  forBeneficiary: { text: "not-applicable: a duty on the provider in writing competence standards", rewrite: full, force: should, status: drafted }
  author-agent-written: "Treat this as a duty, in should, on any provider that writes competence standards (in the Equality Act 2010 sense) for a HAAD programme: follow current Equality and Human Rights Commission guidance. Cite it as (QAA, 2026, History of Art, Architecture and Design Subject Benchmark Statement, para 4.3). Do not describe the threshold cells of 4.4 as competence standards or as universal requirements. Set it beside 4.4, 4.2 and the accessibility paragraphs 1.13 to 1.15."
  author-agent-dialogue: "Raise this when a programme team is drafting competence standards or a disabled student's adjustment turns on what is truly required. Frame it for staff and ask \"Is this a genuine competence standard, and have you checked it against the Commission's current guidance?\" Avoid presenting threshold standards to a student as fixed competences that rule out adjustments."
- statement: qaa/history-of-art-architecture-and-design-2026/4.4.b1
  forPractitioner: { text: "At threshold, graduates analyse and interpret artefacts from more than one region or period, so the curriculum spans at least two.", rewrite: light, force: threshold, status: drafted }
  forBeneficiary: { text: "To reach the minimum standard, you will analyse and interpret art, buildings and objects from at least two parts of the world or periods of history.", rewrite: full, force: threshold, status: drafted }
  author-agent-written: "Present this as the threshold standard, the minimum an honours graduate must show (equivalent to a third) for the bachelor's degree with honours at FHEQ Level 6 (FQHEIS Level 10): visual and material culture of more than one region or period. Cite it as (QAA, 2026, History of Art, Architecture and Design Subject Benchmark Statement, para 4.4), naming the threshold column. Do not call it a regulatory requirement or apply it to another award or level. Set it beside its typical cell (4.4.b1.typical), qaa/fheq-2024/4.15.b1 and Annex D qaa/fheq-2024/annex-d/knowledge/r1/3rd and the reference framework's spine:6."
  author-agent-dialogue: "Raise this when a student or team asks how wide the geographical or historical range of study needs to be. With a student, put it in plain second-person words as the least you need to show to pass the honours degree; with staff, frame it as what modules must give students the chance to show. Ask: \"Which regions or periods have you analysed so far, and could you interpret an artefact from each?\" Avoid reading the issuer's wording aloud and do not suggest the threshold is what most students aim for."
- statement: qaa/history-of-art-architecture-and-design-2026/4.4.b1.typical
  forPractitioner: { text: "At the typical level, graduates will construct and sustain arguments grounded in knowledge of artefacts from more than one region or period.", rewrite: light, force: will, status: drafted }
  forBeneficiary: { text: "At the typical standard, you will build and keep up your own arguments about art and objects from at least two places or periods.", rewrite: full, force: will, status: drafted }
  author-agent-written: "Present this as the typical standard, which most honours graduates will reach (equivalent to a second) for the bachelor's degree with honours at FHEQ Level 6 (FQHEIS Level 10): arguments about the culture of more than one region or period. Cite it as (QAA, 2026, History of Art, Architecture and Design Subject Benchmark Statement, para 4.4), naming the typical column. Do not call it a regulatory requirement or apply it to another award or level, and do not present it as the pass standard. Set it beside its threshold cell (4.4.b1), qaa/fheq-2024/4.15.b3.1 and Annex D qaa/fheq-2024/annex-d/knowledge/r1/2.2 and 2.1 and the reference framework's spine:6."
  author-agent-dialogue: "Raise this when a student or team asks how wide the geographical or historical range of study needs to be. With a student, put it in plain second-person words as what most students reach, above the pass line; with staff, frame it as what modules must give students the chance to show. Ask: \"Can you build an argument of your own about artefacts from two different regions or periods, not only describe them?\" Avoid reading the issuer's wording aloud and never present this typical standard as the minimum for a pass."
- statement: qaa/history-of-art-architecture-and-design-2026/4.4.b2
  forPractitioner: { text: "At threshold, graduates describe how artefacts in the cultures they study were made and from what, and comment on those materials and techniques.", rewrite: light, force: threshold, status: drafted }
  forBeneficiary: { text: "To reach the minimum standard, you will describe what artefacts were made from and how, and comment on those materials and methods.", rewrite: full, force: threshold, status: drafted }
  author-agent-written: "Present this as the threshold standard, the minimum an honours graduate must show (equivalent to a third) for the bachelor's degree with honours at FHEQ Level 6 (FQHEIS Level 10): materials and making techniques of artefacts. Cite it as (QAA, 2026, History of Art, Architecture and Design Subject Benchmark Statement, para 4.4), naming the threshold column. Do not call it a regulatory requirement or apply it to another award or level. Set it beside its typical cell (4.4.b2.typical), qaa/fheq-2024/4.15.b1 and Annex D qaa/fheq-2024/annex-d/practical/r1/3rd and the reference framework's spine:6."
  author-agent-dialogue: "Raise this when a student is writing about how an object was made or a team plans material or technical study. With a student, put it in plain second-person words as the least you need to show to pass the honours degree; with staff, frame it as what modules must give students the chance to show. Ask: \"Pick an artefact you have studied: what is it made of, and how was it made?\" Avoid reading the issuer's wording aloud and do not suggest the threshold is what most students aim for."
- statement: qaa/history-of-art-architecture-and-design-2026/4.4.b2.typical
  forPractitioner: { text: "At the typical level, graduates will argue from a grasp of materials and making processes, not only describe them.", rewrite: light, force: will, status: drafted }
  forBeneficiary: { text: "At the typical standard, you will use what you know about materials and making methods to build and sustain your own arguments.", rewrite: full, force: will, status: drafted }
  author-agent-written: "Present this as the typical standard, which most honours graduates will reach (equivalent to a second) for the bachelor's degree with honours at FHEQ Level 6 (FQHEIS Level 10): arguments from knowledge of materials and techniques. Cite it as (QAA, 2026, History of Art, Architecture and Design Subject Benchmark Statement, para 4.4), naming the typical column. Do not call it a regulatory requirement or apply it to another award or level, and do not present it as the pass standard. Set it beside its threshold cell (4.4.b2), qaa/fheq-2024/4.15.b3.1 and the reference framework's spine:6."
  author-agent-dialogue: "Raise this when a student is writing about how an object was made or a team plans material or technical study. With a student, put it in plain second-person words as what most students reach, above the pass line; with staff, frame it as what modules must give students the chance to show. Ask: \"How does what an object is made of change the argument you make about it?\" Avoid reading the issuer's wording aloud and never present this typical standard as the minimum for a pass."
- statement: qaa/history-of-art-architecture-and-design-2026/4.4.b3
  forPractitioner: { text: "At threshold, graduates keep track of current debates and approaches in the discipline.", rewrite: light, force: threshold, status: drafted }
  forBeneficiary: { text: "To reach the minimum standard, you will keep up with the current debates and ways of working in your subject.", rewrite: full, force: threshold, status: drafted }
  author-agent-written: "Present this as the threshold standard, the minimum an honours graduate must show (equivalent to a third) for the bachelor's degree with honours at FHEQ Level 6 (FQHEIS Level 10): current debates and approaches in the discipline. Cite it as (QAA, 2026, History of Art, Architecture and Design Subject Benchmark Statement, para 4.4), naming the threshold column. Do not call it a regulatory requirement or apply it to another award or level. Set it beside its typical cell (4.4.b3.typical), qaa/fheq-2024/4.15.b3.2 and the reference framework's spine:6."
  author-agent-dialogue: "Raise this when a student asks how far they need to follow scholarship beyond the reading list. With a student, put it in plain second-person words as the least you need to show to pass the honours degree; with staff, frame it as what modules must give students the chance to show. Ask: \"Which current debate in the discipline could you summarise for someone new to it?\" Avoid reading the issuer's wording aloud and do not suggest the threshold is what most students aim for."
- statement: qaa/history-of-art-architecture-and-design-2026/4.4.b3.typical
  forPractitioner: { text: "At the typical level, graduates will know current debates and approaches soundly and apply the discipline's established interpretive techniques with accuracy.", rewrite: light, force: will, status: drafted }
  forBeneficiary: { text: "At the typical standard, you will know the current debates well and use the subject's recognised ways of interpreting artefacts accurately.", rewrite: full, force: will, status: drafted }
  author-agent-written: "Present this as the typical standard, which most honours graduates will reach (equivalent to a second) for the bachelor's degree with honours at FHEQ Level 6 (FQHEIS Level 10): sound knowledge of debates; accurate interpretive technique. Cite it as (QAA, 2026, History of Art, Architecture and Design Subject Benchmark Statement, para 4.4), naming the typical column. Do not call it a regulatory requirement or apply it to another award or level, and do not present it as the pass standard. Set it beside its threshold cell (4.4.b3), qaa/fheq-2024/4.15.b2 and qaa/fheq-2024/4.15.b3.2 and the reference framework's spine:6."
  author-agent-dialogue: "Raise this when a student asks how far they need to follow scholarship beyond the reading list. With a student, put it in plain second-person words as what most students reach, above the pass line; with staff, frame it as what modules must give students the chance to show. Ask: \"Which interpretive technique do you use most, and how do you check you are using it accurately?\" Avoid reading the issuer's wording aloud and never present this typical standard as the minimum for a pass."
- statement: qaa/history-of-art-architecture-and-design-2026/4.4.b4
  forPractitioner: { text: "At threshold, graduates have some familiarity with how museums, galleries, heritage bodies and the creative industries work.", rewrite: light, force: threshold, status: drafted }
  forBeneficiary: { text: "To reach the minimum standard, you will know something of how museums, galleries, heritage sites and the creative industries work.", rewrite: full, force: threshold, status: drafted }
  author-agent-written: "Present this as the threshold standard, the minimum an honours graduate must show (equivalent to a third) for the bachelor's degree with honours at FHEQ Level 6 (FQHEIS Level 10): some acquaintance with how the arts and heritage sectors work. Cite it as (QAA, 2026, History of Art, Architecture and Design Subject Benchmark Statement, para 4.4), naming the threshold column. Do not call it a regulatory requirement or apply it to another award or level. Set it beside its typical cell (4.4.b4.typical), qaa/fheq-2024/4.15.b9.1 and the reference framework's spine:6."
  author-agent-dialogue: "Raise this when a student asks about placements, curatorial work or careers in the sector, or a team plans partnership learning. With a student, put it in plain second-person words as the least you need to show to pass the honours degree; with staff, frame it as what modules must give students the chance to show. Ask: \"What have you seen of how a museum, gallery or heritage site actually works?\" Avoid reading the issuer's wording aloud and do not suggest the threshold is what most students aim for."
- statement: qaa/history-of-art-architecture-and-design-2026/4.4.b4.typical
  forPractitioner: { text: "At the typical level, graduates will engage with professional practice across the arts, heritage and creative sectors and use it to build arguments and tackle problems.", rewrite: light, force: will, status: drafted }
  forBeneficiary: { text: "At the typical standard, you will engage with how museums, galleries, heritage and creative organisations work and use that to make arguments and solve problems.", rewrite: full, force: will, status: drafted }
  author-agent-written: "Present this as the typical standard, which most honours graduates will reach (equivalent to a second) for the bachelor's degree with honours at FHEQ Level 6 (FQHEIS Level 10): using professional practice to argue and solve problems. Cite it as (QAA, 2026, History of Art, Architecture and Design Subject Benchmark Statement, para 4.4), naming the typical column. Do not call it a regulatory requirement or apply it to another award or level, and do not present it as the pass standard. Set it beside its threshold cell (4.4.b4), qaa/fheq-2024/4.15.b6 and Annex D qaa/fheq-2024/annex-d/cognitive/r3/2.2 and the reference framework's spine:6."
  author-agent-dialogue: "Raise this when a student asks about placements, curatorial work or careers in the sector, or a team plans partnership learning. With a student, put it in plain second-person words as what most students reach, above the pass line; with staff, frame it as what modules must give students the chance to show. Ask: \"Where have you used something from professional practice to answer a question or solve a problem in your work?\" Avoid reading the issuer's wording aloud and never present this typical standard as the minimum for a pass."
- statement: qaa/history-of-art-architecture-and-design-2026/4.4.b5
  forPractitioner: { text: "At threshold, graduates analyse the part art, design and architecture play in forming cultures and identities, and how they mirror that formation.", rewrite: light, force: threshold, status: drafted }
  forBeneficiary: { text: "To reach the minimum standard, you will analyse how art, design and buildings help to shape cultures and identities and respond to them.", rewrite: full, force: threshold, status: drafted }
  author-agent-written: "Present this as the threshold standard, the minimum an honours graduate must show (equivalent to a third) for the bachelor's degree with honours at FHEQ Level 6 (FQHEIS Level 10): how art, design and architecture shape cultures and identities. Cite it as (QAA, 2026, History of Art, Architecture and Design Subject Benchmark Statement, para 4.4), naming the threshold column. Do not call it a regulatory requirement or apply it to another award or level. Set it beside its typical cell (4.4.b5.typical), qaa/fheq-2024/4.15.b7 and the reference framework's spine:6."
  author-agent-dialogue: "Raise this when a student is working on identity, representation or the social role of art. With a student, put it in plain second-person words as the least you need to show to pass the honours degree; with staff, frame it as what modules must give students the chance to show. Ask: \"Choose a building, design or artwork: how did it help shape who a community thought it was?\" Avoid reading the issuer's wording aloud and do not suggest the threshold is what most students aim for."
- statement: qaa/history-of-art-architecture-and-design-2026/4.4.b5.typical
  forPractitioner: { text: "At the typical level, graduates will bring theory to bear on the role of art, design and architecture in forming and reflecting cultures and identities.", rewrite: light, force: will, status: drafted }
  forBeneficiary: { text: "At the typical standard, you will use theory to explain how art, design and buildings shape and mirror cultures and identities.", rewrite: full, force: will, status: drafted }
  author-agent-written: "Present this as the typical standard, which most honours graduates will reach (equivalent to a second) for the bachelor's degree with honours at FHEQ Level 6 (FQHEIS Level 10): theory applied to art, culture and identity. Cite it as (QAA, 2026, History of Art, Architecture and Design Subject Benchmark Statement, para 4.4), naming the typical column. Do not call it a regulatory requirement or apply it to another award or level, and do not present it as the pass standard. Set it beside its threshold cell (4.4.b5), qaa/fheq-2024/4.15.b3.1 and the reference framework's spine:6."
  author-agent-dialogue: "Raise this when a student is working on identity, representation or the social role of art. With a student, put it in plain second-person words as what most students reach, above the pass line; with staff, frame it as what modules must give students the chance to show. Ask: \"Which theory would you use to explain that, and why that one?\" Avoid reading the issuer's wording aloud and never present this typical standard as the minimum for a pass."
- statement: qaa/history-of-art-architecture-and-design-2026/4.4.b6
  forPractitioner: { text: "At threshold, graduates bring basic skills of close looking and of describing artefacts' visual and material qualities into their analysis.", rewrite: light, force: threshold, status: drafted }
  forBeneficiary: { text: "To reach the minimum standard, you will look closely at artefacts and describe what you see and what they are made of as part of your analysis.", rewrite: full, force: threshold, status: drafted }
  author-agent-written: "Present this as the threshold standard, the minimum an honours graduate must show (equivalent to a third) for the bachelor's degree with honours at FHEQ Level 6 (FQHEIS Level 10): basic observation and description in analysis. Cite it as (QAA, 2026, History of Art, Architecture and Design Subject Benchmark Statement, para 4.4), naming the threshold column. Do not call it a regulatory requirement or apply it to another award or level. Set it beside its typical cell (4.4.b6.typical), qaa/fheq-2024/4.15.b2 and Annex D qaa/fheq-2024/annex-d/practical/r1/3rd and the reference framework's spine:6."
  author-agent-dialogue: "Raise this when a student is learning visual analysis or struggling to move from description to argument. With a student, put it in plain second-person words as the least you need to show to pass the honours degree; with staff, frame it as what modules must give students the chance to show. Ask: \"Describe this object to me as if I could not see it: what do you notice first?\" Avoid reading the issuer's wording aloud and do not suggest the threshold is what most students aim for."
- statement: qaa/history-of-art-architecture-and-design-2026/4.4.b6.typical
  forPractitioner: { text: "At the typical level, graduates will deploy close observation and description to interpret artefacts and to elaborate arguments.", rewrite: light, force: will, status: drafted }
  forBeneficiary: { text: "At the typical standard, you will use close looking and careful description to interpret artefacts and develop your arguments.", rewrite: full, force: will, status: drafted }
  author-agent-written: "Present this as the typical standard, which most honours graduates will reach (equivalent to a second) for the bachelor's degree with honours at FHEQ Level 6 (FQHEIS Level 10): observation and description put to interpretation and argument. Cite it as (QAA, 2026, History of Art, Architecture and Design Subject Benchmark Statement, para 4.4), naming the typical column. Do not call it a regulatory requirement or apply it to another award or level, and do not present it as the pass standard. Set it beside its threshold cell (4.4.b6), qaa/fheq-2024/4.15.b2 and qaa/fheq-2024/4.15.b7 and the reference framework's spine:6."
  author-agent-dialogue: "Raise this when a student is learning visual analysis or struggling to move from description to argument. With a student, put it in plain second-person words as what most students reach, above the pass line; with staff, frame it as what modules must give students the chance to show. Ask: \"How does what you noticed in that description support the argument you are making?\" Avoid reading the issuer's wording aloud and never present this typical standard as the minimum for a pass."
- statement: qaa/history-of-art-architecture-and-design-2026/4.4.b7
  forPractitioner: { text: "At threshold, graduates place artefacts in suitable environmental, historical and cultural contexts.", rewrite: light, force: threshold, status: drafted }
  forBeneficiary: { text: "To reach the minimum standard, you will place artefacts in the right environmental, historical and cultural settings.", rewrite: full, force: threshold, status: drafted }
  author-agent-written: "Present this as the threshold standard, the minimum an honours graduate must show (equivalent to a third) for the bachelor's degree with honours at FHEQ Level 6 (FQHEIS Level 10): placing artefacts in context, environmental included. Cite it as (QAA, 2026, History of Art, Architecture and Design Subject Benchmark Statement, para 4.4), naming the threshold column. Do not call it a regulatory requirement or apply it to another award or level. Set it beside its typical cell (4.4.b7.typical), qaa/fheq-2024/4.15.b1 and the reference framework's spine:6."
  author-agent-dialogue: "Raise this when a student is contextualising an artefact in an essay or project. With a student, put it in plain second-person words as the least you need to show to pass the honours degree; with staff, frame it as what modules must give students the chance to show. Ask: \"When and where was this artefact made, and what environment and culture shaped it?\" Avoid reading the issuer's wording aloud and do not suggest the threshold is what most students aim for."
- statement: qaa/history-of-art-architecture-and-design-2026/4.4.b7.typical
  forPractitioner: { text: "At the typical level, graduates will use historical and cultural context to push enquiry in the discipline forward, not only to label artefacts.", rewrite: light, force: will, status: drafted }
  forBeneficiary: { text: "At the typical standard, you will use the historical and cultural setting of artefacts to open up new questions in your subject.", rewrite: full, force: will, status: drafted }
  author-agent-written: "Present this as the typical standard, which most honours graduates will reach (equivalent to a second) for the bachelor's degree with honours at FHEQ Level 6 (FQHEIS Level 10): context used to advance enquiry. Cite it as (QAA, 2026, History of Art, Architecture and Design Subject Benchmark Statement, para 4.4), naming the typical column. Do not call it a regulatory requirement or apply it to another award or level, and do not present it as the pass standard. Set it beside its threshold cell (4.4.b7), qaa/fheq-2024/4.15.b6 and the reference framework's spine:6."
  author-agent-dialogue: "Raise this when a student is contextualising an artefact in an essay or project. With a student, put it in plain second-person words as what most students reach, above the pass line; with staff, frame it as what modules must give students the chance to show. Ask: \"What new question does that context open up for you?\" Avoid reading the issuer's wording aloud and never present this typical standard as the minimum for a pass."
- statement: qaa/history-of-art-architecture-and-design-2026/4.4.b8
  forPractitioner: { text: "At threshold, graduates draw on evidence from several disciplines, visual, spoken, written and technical, original and secondary, in addressing current issues in the field.", rewrite: light, force: threshold, status: drafted }
  forBeneficiary: { text: "To reach the minimum standard, you will use evidence from different subjects and kinds of source, such as images, texts, technical data, original and secondary material, on current questions.", rewrite: full, force: threshold, status: drafted }
  author-agent-written: "Present this as the threshold standard, the minimum an honours graduate must show (equivalent to a third) for the bachelor's degree with honours at FHEQ Level 6 (FQHEIS Level 10): interdisciplinary evidence on current issues. Cite it as (QAA, 2026, History of Art, Architecture and Design Subject Benchmark Statement, para 4.4), naming the threshold column. Do not call it a regulatory requirement or apply it to another award or level. Set it beside its typical cell (4.4.b8.typical), qaa/fheq-2024/4.15.b5 and the reference framework's spine:6."
  author-agent-dialogue: "Raise this when a student is gathering sources or a team is designing a research-skills module. With a student, put it in plain second-person words as the least you need to show to pass the honours degree; with staff, frame it as what modules must give students the chance to show. Ask: \"What kinds of evidence did you use in your last piece of work, and from which subjects?\" Avoid reading the issuer's wording aloud and do not suggest the threshold is what most students aim for."
- statement: qaa/history-of-art-architecture-and-design-2026/4.4.b8.typical
  forPractitioner: { text: "At the typical level, graduates will locate and critically evaluate evidence from several disciplines themselves and use it to move enquiry forward.", rewrite: light, force: will, status: drafted }
  forBeneficiary: { text: "At the typical standard, you will find evidence for yourself across many kinds of source, judge how good it is and use it to move your enquiry on.", rewrite: full, force: will, status: drafted }
  author-agent-written: "Present this as the typical standard, which most honours graduates will reach (equivalent to a second) for the bachelor's degree with honours at FHEQ Level 6 (FQHEIS Level 10): finding and weighing interdisciplinary evidence. Cite it as (QAA, 2026, History of Art, Architecture and Design Subject Benchmark Statement, para 4.4), naming the typical column. Do not call it a regulatory requirement or apply it to another award or level, and do not present it as the pass standard. Set it beside its threshold cell (4.4.b8), qaa/fheq-2024/4.15.b5 and Annex D qaa/fheq-2024/annex-d/knowledge/r3/2.2 and the reference framework's spine:6."
  author-agent-dialogue: "Raise this when a student is gathering sources or a team is designing a research-skills module. With a student, put it in plain second-person words as what most students reach, above the pass line; with staff, frame it as what modules must give students the chance to show. Ask: \"How did you find that source, and how did you decide it was reliable?\" Avoid reading the issuer's wording aloud and never present this typical standard as the minimum for a pass."
- statement: qaa/history-of-art-architecture-and-design-2026/4.4.b9
  forPractitioner: { text: "At threshold, graduates are aware of the established methodologies, theories and approaches of the field.", rewrite: light, force: threshold, status: drafted }
  forBeneficiary: { text: "To reach the minimum standard, you will know the main methods, theories and approaches used in your subject.", rewrite: full, force: threshold, status: drafted }
  author-agent-written: "Present this as the threshold standard, the minimum an honours graduate must show (equivalent to a third) for the bachelor's degree with honours at FHEQ Level 6 (FQHEIS Level 10): awareness of the discipline's methods and theories. Cite it as (QAA, 2026, History of Art, Architecture and Design Subject Benchmark Statement, para 4.4), naming the threshold column. Do not call it a regulatory requirement or apply it to another award or level. Set it beside its typical cell (4.4.b9.typical), qaa/fheq-2024/4.15.b2 and the reference framework's spine:6."
  author-agent-dialogue: "Raise this when a student is choosing a method for an essay or dissertation. With a student, put it in plain second-person words as the least you need to show to pass the honours degree; with staff, frame it as what modules must give students the chance to show. Ask: \"Which methods, such as iconography or formal analysis, could you name and explain?\" Avoid reading the issuer's wording aloud and do not suggest the threshold is what most students aim for."
- statement: qaa/history-of-art-architecture-and-design-2026/4.4.b9.typical
  forPractitioner: { text: "At the typical level, graduates will choose and deploy fitting methodologies, theories and approaches from the field.", rewrite: light, force: will, status: drafted }
  forBeneficiary: { text: "At the typical standard, you will choose and use the right methods, theories and approaches for the task.", rewrite: full, force: will, status: drafted }
  author-agent-written: "Present this as the typical standard, which most honours graduates will reach (equivalent to a second) for the bachelor's degree with honours at FHEQ Level 6 (FQHEIS Level 10): choosing and using fitting methods and theories. Cite it as (QAA, 2026, History of Art, Architecture and Design Subject Benchmark Statement, para 4.4), naming the typical column. Do not call it a regulatory requirement or apply it to another award or level, and do not present it as the pass standard. Set it beside its threshold cell (4.4.b9), qaa/fheq-2024/4.15.b2 and qaa/fheq-2024/4.15.b6 and the reference framework's spine:6."
  author-agent-dialogue: "Raise this when a student is choosing a method for an essay or dissertation. With a student, put it in plain second-person words as what most students reach, above the pass line; with staff, frame it as what modules must give students the chance to show. Ask: \"Which method did you choose for this project, and why does it suit the question?\" Avoid reading the issuer's wording aloud and never present this typical standard as the minimum for a pass."
- statement: qaa/history-of-art-architecture-and-design-2026/4.4.b10
  forPractitioner: { text: "At threshold, graduates show some capacity to build relevant arguments and ideas supported by suitable evidence, visual, textual or other.", rewrite: light, force: threshold, status: drafted }
  forBeneficiary: { text: "To reach the minimum standard, you will show some ability to make relevant arguments backed by images, texts or other suitable evidence.", rewrite: full, force: threshold, status: drafted }
  author-agent-written: "Present this as the threshold standard, the minimum an honours graduate must show (equivalent to a third) for the bachelor's degree with honours at FHEQ Level 6 (FQHEIS Level 10): relevant arguments backed by evidence. Cite it as (QAA, 2026, History of Art, Architecture and Design Subject Benchmark Statement, para 4.4), naming the threshold column. Do not call it a regulatory requirement or apply it to another award or level. Set it beside its typical cell (4.4.b10.typical), qaa/fheq-2024/4.15.b3.1 and Annex D qaa/fheq-2024/annex-d/cognitive/r2/3rd and the reference framework's spine:6."
  author-agent-dialogue: "Raise this when a student asks what makes an argument stronger or why a mark was held back. With a student, put it in plain second-person words as the least you need to show to pass the honours degree; with staff, frame it as what modules must give students the chance to show. Ask: \"What is the main claim in your essay, and what evidence supports it?\" Avoid reading the issuer's wording aloud and do not suggest the threshold is what most students aim for."
- statement: qaa/history-of-art-architecture-and-design-2026/4.4.b10.typical
  forPractitioner: { text: "At the typical level, graduates will consistently write arguments that hang together, are well organised and relevant, with suitable supporting evidence.", rewrite: light, force: will, status: drafted }
  forBeneficiary: { text: "At the typical standard, you will consistently make clear, well-organised and relevant arguments backed by good evidence.", rewrite: full, force: will, status: drafted }
  author-agent-written: "Present this as the typical standard, which most honours graduates will reach (equivalent to a second) for the bachelor's degree with honours at FHEQ Level 6 (FQHEIS Level 10): consistent, well-built, evidenced argument. Cite it as (QAA, 2026, History of Art, Architecture and Design Subject Benchmark Statement, para 4.4), naming the typical column. Do not call it a regulatory requirement or apply it to another award or level, and do not present it as the pass standard. Set it beside its threshold cell (4.4.b10), Annex D qaa/fheq-2024/annex-d/cognitive/r2/2.2 and 2.1 and the reference framework's spine:6."
  author-agent-dialogue: "Raise this when a student asks what makes an argument stronger or why a mark was held back. With a student, put it in plain second-person words as what most students reach, above the pass line; with staff, frame it as what modules must give students the chance to show. Ask: \"Is every paragraph doing work for that claim, and is that so in all your recent pieces?\" Avoid reading the issuer's wording aloud and never present this typical standard as the minimum for a pass."
- statement: qaa/history-of-art-architecture-and-design-2026/4.4.b11
  forPractitioner: { text: "At threshold, graduates distinguish between alternative arguments and approaches.", rewrite: light, force: threshold, status: drafted }
  forBeneficiary: { text: "To reach the minimum standard, you will be able to tell different arguments and approaches apart.", rewrite: full, force: threshold, status: drafted }
  author-agent-written: "Present this as the threshold standard, the minimum an honours graduate must show (equivalent to a third) for the bachelor's degree with honours at FHEQ Level 6 (FQHEIS Level 10): telling alternative arguments apart. Cite it as (QAA, 2026, History of Art, Architecture and Design Subject Benchmark Statement, para 4.4), naming the threshold column. Do not call it a regulatory requirement or apply it to another award or level. Set it beside its typical cell (4.4.b11.typical), qaa/fheq-2024/4.15.b7 and the reference framework's spine:6."
  author-agent-dialogue: "Raise this when a student is reviewing scholarship or weighing interpretations. With a student, put it in plain second-person words as the least you need to show to pass the honours degree; with staff, frame it as what modules must give students the chance to show. Ask: \"What are two different ways scholars have read this artwork, and how do they differ?\" Avoid reading the issuer's wording aloud and do not suggest the threshold is what most students aim for."
- statement: qaa/history-of-art-architecture-and-design-2026/4.4.b11.typical
  forPractitioner: { text: "At the typical level, graduates will exercise critical judgement, evaluating alternative arguments and engaging with competing approaches.", rewrite: light, force: will, status: drafted }
  forBeneficiary: { text: "At the typical standard, you will judge competing arguments critically and engage with approaches that differ from your own.", rewrite: full, force: will, status: drafted }
  author-agent-written: "Present this as the typical standard, which most honours graduates will reach (equivalent to a second) for the bachelor's degree with honours at FHEQ Level 6 (FQHEIS Level 10): critical judgement between competing approaches. Cite it as (QAA, 2026, History of Art, Architecture and Design Subject Benchmark Statement, para 4.4), naming the typical column. Do not call it a regulatory requirement or apply it to another award or level, and do not present it as the pass standard. Set it beside its threshold cell (4.4.b11), qaa/fheq-2024/4.15.b7 and Annex D qaa/fheq-2024/annex-d/cognitive/r2/2.1 and the reference framework's spine:6."
  author-agent-dialogue: "Raise this when a student is reviewing scholarship or weighing interpretations. With a student, put it in plain second-person words as what most students reach, above the pass line; with staff, frame it as what modules must give students the chance to show. Ask: \"Which of those readings do you find stronger, and why?\" Avoid reading the issuer's wording aloud and never present this typical standard as the minimum for a pass."
- statement: qaa/history-of-art-architecture-and-design-2026/4.4.b12
  forPractitioner: { text: "At threshold, graduates communicate comprehensibly across different media, using visual aids when the task calls for them.", rewrite: light, force: threshold, status: drafted }
  forBeneficiary: { text: "To reach the minimum standard, you will communicate clearly enough to be understood in different media, using images or other visual aids where they help.", rewrite: full, force: threshold, status: drafted }
  author-agent-written: "Present this as the threshold standard, the minimum an honours graduate must show (equivalent to a third) for the bachelor's degree with honours at FHEQ Level 6 (FQHEIS Level 10): understandable communication in varied media. Cite it as (QAA, 2026, History of Art, Architecture and Design Subject Benchmark Statement, para 4.4), naming the threshold column. Do not call it a regulatory requirement or apply it to another award or level. Set it beside its typical cell (4.4.b12.typical), qaa/fheq-2024/4.15.b8 and Annex D qaa/fheq-2024/annex-d/transferable/r1/3rd and the reference framework's spine:6."
  author-agent-dialogue: "Raise this when a student is preparing a presentation, video essay or exhibition text. With a student, put it in plain second-person words as the least you need to show to pass the honours degree; with staff, frame it as what modules must give students the chance to show. Ask: \"In which formats have you presented your work, and did your audience follow it?\" Avoid reading the issuer's wording aloud and do not suggest the threshold is what most students aim for."
- statement: qaa/history-of-art-architecture-and-design-2026/4.4.b12.typical
  forPractitioner: { text: "At the typical level, graduates will communicate effectively in a range of media for both expert and lay audiences, using visual aids as needed.", rewrite: light, force: will, status: drafted }
  forBeneficiary: { text: "At the typical standard, you will communicate well in different media to experts and non-experts alike, using visual aids where they help.", rewrite: full, force: will, status: drafted }
  author-agent-written: "Present this as the typical standard, which most honours graduates will reach (equivalent to a second) for the bachelor's degree with honours at FHEQ Level 6 (FQHEIS Level 10): effective communication to expert and lay audiences. Cite it as (QAA, 2026, History of Art, Architecture and Design Subject Benchmark Statement, para 4.4), naming the typical column. Do not call it a regulatory requirement or apply it to another award or level, and do not present it as the pass standard. Set it beside its threshold cell (4.4.b12), qaa/fheq-2024/4.15.b8 and Annex D qaa/fheq-2024/annex-d/transferable/r1/2.2 and the reference framework's spine:6."
  author-agent-dialogue: "Raise this when a student is preparing a presentation, video essay or exhibition text. With a student, put it in plain second-person words as what most students reach, above the pass line; with staff, frame it as what modules must give students the chance to show. Ask: \"How would you change this talk for a general audience rather than your tutors?\" Avoid reading the issuer's wording aloud and never present this typical standard as the minimum for a pass."
- statement: qaa/history-of-art-architecture-and-design-2026/4.4.b13
  forPractitioner: { text: "At threshold, graduates gather information and do basic research when guided and supported.", rewrite: light, force: threshold, status: drafted }
  forBeneficiary: { text: "To reach the minimum standard, you will gather information and do basic research with guidance and help.", rewrite: full, force: threshold, status: drafted }
  author-agent-written: "Present this as the threshold standard, the minimum an honours graduate must show (equivalent to a third) for the bachelor's degree with honours at FHEQ Level 6 (FQHEIS Level 10): guided information gathering and basic research. Cite it as (QAA, 2026, History of Art, Architecture and Design Subject Benchmark Statement, para 4.4), naming the threshold column. Do not call it a regulatory requirement or apply it to another award or level. Set it beside its typical cell (4.4.b13.typical), qaa/fheq-2024/4.15.b5 and Annex D qaa/fheq-2024/annex-d/transferable/r3/3rd and the reference framework's spine:6."
  author-agent-dialogue: "Raise this when a student is starting independent research or a dissertation. With a student, put it in plain second-person words as the least you need to show to pass the honours degree; with staff, frame it as what modules must give students the chance to show. Ask: \"How did you find your sources for this piece, and who helped?\" Avoid reading the issuer's wording aloud and do not suggest the threshold is what most students aim for."
- statement: qaa/history-of-art-architecture-and-design-2026/4.4.b13.typical
  forPractitioner: { text: "At the typical level, graduates will direct their own research, finding information reliably and traceably, reviewing it critically and organising it to suit the task.", rewrite: light, force: will, status: drafted }
  forBeneficiary: { text: "At the typical standard, you will lead your own research, finding information in ways others can check, reviewing it critically and organising it for the task.", rewrite: full, force: will, status: drafted }
  author-agent-written: "Present this as the typical standard, which most honours graduates will reach (equivalent to a second) for the bachelor's degree with honours at FHEQ Level 6 (FQHEIS Level 10): self-directed, verifiable research. Cite it as (QAA, 2026, History of Art, Architecture and Design Subject Benchmark Statement, para 4.4), naming the typical column. Do not call it a regulatory requirement or apply it to another award or level, and do not present it as the pass standard. Set it beside its threshold cell (4.4.b13), qaa/fheq-2024/4.15.b5 and Annex D qaa/fheq-2024/annex-d/knowledge/r3/2.1 and the reference framework's spine:6."
  author-agent-dialogue: "Raise this when a student is starting independent research or a dissertation. With a student, put it in plain second-person words as what most students reach, above the pass line; with staff, frame it as what modules must give students the chance to show. Ask: \"Could someone else retrace how you found your sources?\" Avoid reading the issuer's wording aloud and never present this typical standard as the minimum for a pass."
- statement: qaa/history-of-art-architecture-and-design-2026/4.4.b14
  forPractitioner: { text: "At threshold, graduates are open-minded: willing to take seriously artefacts, issues, values and ideas new to them.", rewrite: light, force: threshold, status: drafted }
  forBeneficiary: { text: "To reach the minimum standard, you will be open-minded about artefacts, issues, values and ideas you have not met before.", rewrite: full, force: threshold, status: drafted }
  author-agent-written: "Present this as the threshold standard, the minimum an honours graduate must show (equivalent to a third) for the bachelor's degree with honours at FHEQ Level 6 (FQHEIS Level 10): open-mindedness to the unfamiliar. Cite it as (QAA, 2026, History of Art, Architecture and Design Subject Benchmark Statement, para 4.4), naming the threshold column. Do not call it a regulatory requirement or apply it to another award or level. Set it beside its typical cell (4.4.b14.typical), qaa/fheq-2024/4.15.b4 and the reference framework's spine:6."
  author-agent-dialogue: "Raise this when a student meets unfamiliar cultures or contested artefacts. With a student, put it in plain second-person words as the least you need to show to pass the honours degree; with staff, frame it as what modules must give students the chance to show. Ask: \"What is an artefact or idea you met on the course that was new to you, and how did you approach it?\" Avoid reading the issuer's wording aloud and do not suggest the threshold is what most students aim for."
- statement: qaa/history-of-art-architecture-and-design-2026/4.4.b14.typical
  forPractitioner: { text: "At the typical level, graduates will interpret inclusively, taking account of the ideas, settings and structures behind diverse visual and material cultures.", rewrite: light, force: will, status: drafted }
  forBeneficiary: { text: "At the typical standard, you will interpret artefacts inclusively, taking account of the ideas, settings and structures behind different cultures.", rewrite: full, force: will, status: drafted }
  author-agent-written: "Present this as the typical standard, which most honours graduates will reach (equivalent to a second) for the bachelor's degree with honours at FHEQ Level 6 (FQHEIS Level 10): inclusive interpretation. Cite it as (QAA, 2026, History of Art, Architecture and Design Subject Benchmark Statement, para 4.4), naming the typical column. Do not call it a regulatory requirement or apply it to another award or level, and do not present it as the pass standard. Set it beside its threshold cell (4.4.b14), qaa/fheq-2024/4.15.b7 and the reference framework's spine:6."
  author-agent-dialogue: "Raise this when a student meets unfamiliar cultures or contested artefacts. With a student, put it in plain second-person words as what most students reach, above the pass line; with staff, frame it as what modules must give students the chance to show. Ask: \"Whose ideas and circumstances shaped this artefact, and have you allowed for them in your reading?\" Avoid reading the issuer's wording aloud and never present this typical standard as the minimum for a pass."
- statement: qaa/history-of-art-architecture-and-design-2026/4.4.b15
  forPractitioner: { text: "At threshold, graduates identify the values and ethics underlying culture and society.", rewrite: light, force: threshold, status: drafted }
  forBeneficiary: { text: "To reach the minimum standard, you will spot the values and ethics that lie beneath culture and society.", rewrite: full, force: threshold, status: drafted }
  author-agent-written: "Present this as the threshold standard, the minimum an honours graduate must show (equivalent to a third) for the bachelor's degree with honours at FHEQ Level 6 (FQHEIS Level 10): values and ethics in culture and society. Cite it as (QAA, 2026, History of Art, Architecture and Design Subject Benchmark Statement, para 4.4), naming the threshold column. Do not call it a regulatory requirement or apply it to another award or level. Set it beside its typical cell (4.4.b15.typical), qaa/fheq-2024/4.15.b9.1 and the reference framework's spine:6."
  author-agent-dialogue: "Raise this when a student is discussing ethics, provenance or values in art. With a student, put it in plain second-person words as the least you need to show to pass the honours degree; with staff, frame it as what modules must give students the chance to show. Ask: \"What values does this artefact take for granted?\" Avoid reading the issuer's wording aloud and do not suggest the threshold is what most students aim for."
- statement: qaa/history-of-art-architecture-and-design-2026/4.4.b15.typical
  forPractitioner: { text: "At the typical level, graduates will go beyond naming the values and ethics beneath culture and society to examine them.", rewrite: light, force: will, status: drafted }
  forBeneficiary: { text: "At the typical standard, you will not only spot the values and ethics beneath culture and society but examine them.", rewrite: full, force: will, status: drafted }
  author-agent-written: "Present this as the typical standard, which most honours graduates will reach (equivalent to a second) for the bachelor's degree with honours at FHEQ Level 6 (FQHEIS Level 10): examining values and ethics in culture and society. Cite it as (QAA, 2026, History of Art, Architecture and Design Subject Benchmark Statement, para 4.4), naming the typical column. Do not call it a regulatory requirement or apply it to another award or level, and do not present it as the pass standard. Set it beside its threshold cell (4.4.b15), qaa/fheq-2024/4.15.b7 and the reference framework's spine:6."
  author-agent-dialogue: "Raise this when a student is discussing ethics, provenance or values in art. With a student, put it in plain second-person words as what most students reach, above the pass line; with staff, frame it as what modules must give students the chance to show. Ask: \"How would you test or question those values?\" Avoid reading the issuer's wording aloud and never present this typical standard as the minimum for a pass."
- statement: qaa/history-of-art-architecture-and-design-2026/4.5.b1
  forPractitioner: { text: "Graduates should be able to put knowledge or a case across understandably, writing English with sound technical accuracy.", rewrite: light, force: should, status: drafted }
  forBeneficiary: { text: "You should be able to explain what you know or argue a case so others can follow it, writing English accurately.", rewrite: full, force: should, status: drafted }
  author-agent-written: "Present this as an expected transferable skill, in should, for every graduate with a bachelor's degree with honours at FHEQ Level 6 (FQHEIS Level 10): clear presentation in sound written English; it is not one of the two rungs. Cite it as (QAA, 2026, History of Art, Architecture and Design Subject Benchmark Statement, para 4.5). Do not call it a regulatory requirement or a measure of degree class. Set it beside the generic cells 4.4.b12 to 4.4.b15, qaa/fheq-2024/4.15.b8 and Annex D qaa/fheq-2024/annex-d/transferable/r1/3rd and spine:6."
  author-agent-dialogue: "Raise this when a student asks about writing standards or feedback on expression. With a student, say plainly what you should be able to do by graduation; with staff, frame it as a skill modules should build and assess. Ask: \"Could someone outside your subject follow your last essay, and where did the writing slip?\" Avoid reading the list aloud or treating it as graded."
- statement: qaa/history-of-art-architecture-and-design-2026/4.5.b2
  forPractitioner: { text: "Graduates should be able to collaborate effectively as members of a team.", rewrite: light, force: should, status: drafted }
  forBeneficiary: { text: "You should be able to work well with others as part of a team.", rewrite: full, force: should, status: drafted }
  author-agent-written: "Present this as an expected transferable skill, in should, for every graduate with a bachelor's degree with honours at FHEQ Level 6 (FQHEIS Level 10): effective teamwork; it is not one of the two rungs. Cite it as (QAA, 2026, History of Art, Architecture and Design Subject Benchmark Statement, para 4.5). Do not call it a regulatory requirement or a measure of degree class. Set it beside the generic cells 4.4.b12 to 4.4.b15, Annex D qaa/fheq-2024/annex-d/transferable/r2/3rd and spine:6."
  author-agent-dialogue: "Raise this when group work is set or a group is not working well. With a student, say plainly what you should be able to do by graduation; with staff, frame it as a skill modules should build and assess. Ask: \"What did you contribute to your last group task, and how did the group use it?\" Avoid reading the list aloud or treating it as graded."
- statement: qaa/history-of-art-architecture-and-design-2026/4.5.b3
  forPractitioner: { text: "Graduates should be able to research and study well where the learning is guided and structured.", rewrite: light, force: should, status: drafted }
  forBeneficiary: { text: "You should be able to research and study well when your learning is guided and structured.", rewrite: full, force: should, status: drafted }
  author-agent-written: "Present this as an expected transferable skill, in should, for every graduate with a bachelor's degree with honours at FHEQ Level 6 (FQHEIS Level 10): effective study where learning is guided; it is not one of the two rungs. Cite it as (QAA, 2026, History of Art, Architecture and Design Subject Benchmark Statement, para 4.5). Do not call it a regulatory requirement or a measure of degree class. Set it beside the generic cells 4.4.b12 to 4.4.b15, qaa/fheq-2024/4.15.b5 and spine:6."
  author-agent-dialogue: "Raise this when a student is adjusting to university study or planning independent work. With a student, say plainly what you should be able to do by graduation; with staff, frame it as a skill modules should build and assess. Ask: \"Where do you need more structure to study well, and where less?\" Avoid reading the list aloud or treating it as graded."
- statement: qaa/history-of-art-architecture-and-design-2026/4.5.b4
  forPractitioner: { text: "Graduates should be able to appreciate and join contemporary debates about culture and society, for instance on inequality and sustainability.", rewrite: light, force: should, status: drafted }
  forBeneficiary: { text: "You should be able to understand and join today's debates about culture and society, such as those on inequality and sustainability.", rewrite: full, force: should, status: drafted }
  author-agent-written: "Present this as an expected transferable skill, in should, for every graduate with a bachelor's degree with honours at FHEQ Level 6 (FQHEIS Level 10): current debates on culture and society; it is not one of the two rungs. Cite it as (QAA, 2026, History of Art, Architecture and Design Subject Benchmark Statement, para 4.5). Do not call it a regulatory requirement or a measure of degree class. Set it beside the generic cells 4.4.b12 to 4.4.b15, qaa/fheq-2024/4.15.b3.2 and spine:6."
  author-agent-dialogue: "Raise this when inequality, sustainability or current cultural controversies come up. With a student, say plainly what you should be able to do by graduation; with staff, frame it as a skill modules should build and assess. Ask: \"Which current debate about inequality or sustainability in the arts have you followed, and where do you stand?\" Avoid reading the list aloud or treating it as graded."
- statement: qaa/history-of-art-architecture-and-design-2026/4.5.b5
  forPractitioner: { text: "Graduates should be able to use digital tools, including generative AI applied ethically, to research, select and share information.", rewrite: light, force: should, status: drafted }
  forBeneficiary: { text: "You should be able to use digital tools, including generative AI used ethically, to research, choose and share information.", rewrite: full, force: should, status: drafted }
  author-agent-written: "Present this as an expected transferable skill, in should, for every graduate with a bachelor's degree with honours at FHEQ Level 6 (FQHEIS Level 10): ethical use of digital tools and GenAI; it is not one of the two rungs. Cite it as (QAA, 2026, History of Art, Architecture and Design Subject Benchmark Statement, para 4.5). Do not call it a regulatory requirement or a measure of degree class. Set it beside the generic cells 4.4.b12 to 4.4.b15, Annex D qaa/fheq-2024/annex-d/transferable/r1/3rd and spine:6."
  author-agent-dialogue: "Raise this when a student asks whether or how to use generative AI or other digital tools. With a student, say plainly what you should be able to do by graduation; with staff, frame it as a skill modules should build and assess. Ask: \"Which digital tools, generative AI included, did you use on your last assignment, and how did you declare that use?\" Avoid reading the list aloud or treating it as graded."
- statement: qaa/history-of-art-architecture-and-design-2026/4.5.b6
  forPractitioner: { text: "Graduates should be able to work diligently, decide appropriately and keep to assessment deadlines.", rewrite: light, force: should, status: drafted }
  forBeneficiary: { text: "You should be able to work steadily, make sensible decisions and hand in assessments on time.", rewrite: full, force: should, status: drafted }
  author-agent-written: "Present this as an expected transferable skill, in should, for every graduate with a bachelor's degree with honours at FHEQ Level 6 (FQHEIS Level 10): diligence, decisions and deadlines; it is not one of the two rungs. Cite it as (QAA, 2026, History of Art, Architecture and Design Subject Benchmark Statement, para 4.5). Do not call it a regulatory requirement or a measure of degree class. Set it beside the generic cells 4.4.b12 to 4.4.b15, Annex D qaa/fheq-2024/annex-d/transferable/r3/3rd and qaa/fheq-2024/4.15.b9.2 and spine:6."
  author-agent-dialogue: "Raise this when a student is struggling with workload or deadlines. With a student, say plainly what you should be able to do by graduation; with staff, frame it as a skill modules should build and assess. Ask: \"How do you plan your work so that you meet deadlines, and what happens when the plan slips?\" Avoid reading the list aloud or treating it as graded."
- statement: qaa/history-of-art-architecture-and-design-2026/4.5.b7
  forPractitioner: { text: "Graduates should be able to own their work and understand the questions of academic integrity it raises.", rewrite: light, force: should, status: drafted }
  forBeneficiary: { text: "You should be able to take responsibility for your own work and understand what academic integrity means for it.", rewrite: full, force: should, status: drafted }
  author-agent-written: "Present this as an expected transferable skill, in should, for every graduate with a bachelor's degree with honours at FHEQ Level 6 (FQHEIS Level 10): responsibility for own work; academic integrity; it is not one of the two rungs. Cite it as (QAA, 2026, History of Art, Architecture and Design Subject Benchmark Statement, para 4.5). Do not call it a regulatory requirement or a measure of degree class. Set it beside the generic cells 4.4.b12 to 4.4.b15, Annex D qaa/fheq-2024/annex-d/transferable/r4/3rd and spine:6."
  author-agent-dialogue: "Raise this when referencing, collusion or AI use come up. With a student, say plainly what you should be able to do by graduation; with staff, frame it as a skill modules should build and assess. Ask: \"How do you make sure the work you hand in is your own, and how do you credit what is not?\" Avoid reading the list aloud or treating it as graded."
- statement: qaa/history-of-art-architecture-and-design-2026/4.5.b8
  forPractitioner: { text: "Graduates should be able to reflect on their progress and use feedback to deepen their thinking and raise their performance.", rewrite: light, force: should, status: drafted }
  forBeneficiary: { text: "You should be able to reflect on how you are doing and use feedback to develop your thinking and improve your work.", rewrite: full, force: should, status: drafted }
  author-agent-written: "Present this as an expected transferable skill, in should, for every graduate with a bachelor's degree with honours at FHEQ Level 6 (FQHEIS Level 10): reflection and use of feedback; it is not one of the two rungs. Cite it as (QAA, 2026, History of Art, Architecture and Design Subject Benchmark Statement, para 4.5). Do not call it a regulatory requirement or a measure of degree class. Set it beside the generic cells 4.4.b12 to 4.4.b15, Annex D qaa/fheq-2024/annex-d/transferable/r5/3rd and spine:6."
  author-agent-dialogue: "Raise this when feedback has just been returned or a student is planning how to improve. With a student, say plainly what you should be able to do by graduation; with staff, frame it as a skill modules should build and assess. Ask: \"What did your last piece of feedback say, and what did you change because of it?\" Avoid reading the list aloud or treating it as graded."
- statement: qaa/history-of-art-architecture-and-design-2026/4.5.b9
  forPractitioner: { text: "Graduates should be able to identify and examine the values and ethics in culture, in society and in themselves.", rewrite: light, force: should, status: drafted }
  forBeneficiary: { text: "You should be able to spot and question the values and ethics beneath culture, society and your own choices.", rewrite: full, force: should, status: drafted }
  author-agent-written: "Present this as an expected transferable skill, in should, for every graduate with a bachelor's degree with honours at FHEQ Level 6 (FQHEIS Level 10): values and ethics, personal as well as social; it is not one of the two rungs. Cite it as (QAA, 2026, History of Art, Architecture and Design Subject Benchmark Statement, para 4.5). Do not call it a regulatory requirement or a measure of degree class. Set it beside the generic cells 4.4.b12 to 4.4.b15, qaa/fheq-2024/4.15.b7 and spine:6."
  author-agent-dialogue: "Raise this when a student is reflecting on their own position or on an ethical question in the subject. With a student, say plainly what you should be able to do by graduation; with staff, frame it as a skill modules should build and assess. Ask: \"Which of your own values shapes how you read artefacts?\" Avoid reading the list aloud or treating it as graded."
- statement: qaa/history-of-art-architecture-and-design-2026/4.5.b10
  forPractitioner: { text: "Graduates should be able to show some awareness of the uncertainty, ambiguity and limits that come with any knowledge.", rewrite: light, force: should, status: drafted }
  forBeneficiary: { text: "You should be able to show some awareness that what we know is uncertain, open to more than one reading and limited.", rewrite: full, force: should, status: drafted }
  author-agent-written: "Present this as an expected transferable skill, in should, for every graduate with a bachelor's degree with honours at FHEQ Level 6 (FQHEIS Level 10): awareness of uncertainty and the limits of knowledge; it is not one of the two rungs. Cite it as (QAA, 2026, History of Art, Architecture and Design Subject Benchmark Statement, para 4.5). Do not call it a regulatory requirement or a measure of degree class. Set it beside the generic cells 4.4.b12 to 4.4.b15, qaa/fheq-2024/4.15.b4 and spine:6."
  author-agent-dialogue: "Raise this when a student wants a single right answer or evidence runs out. With a student, say plainly what you should be able to do by graduation; with staff, frame it as a skill modules should build and assess. Ask: \"Where in your topic does the evidence run out, and how did you handle that?\" Avoid reading the list aloud or treating it as graded."
- statement: qaa/history-of-art-architecture-and-design-2026/4.6.b1.masters
  forPractitioner: { text: "Master's graduates should typically show sophisticated, nuanced visual literacy.", rewrite: light, force: should, status: drafted }
  forBeneficiary: { text: "At master's level, you should usually be able to read images and objects with real subtlety and sophistication.", rewrite: full, force: should, status: drafted }
  author-agent-written: "Present this as a typical outcome, in should, for a master's graduate at FHEQ Level 7 (FQHEIS Level 11): refined visual literacy. Cite it as (QAA, 2026, History of Art, Architecture and Design Subject Benchmark Statement, para 4.6). Do not apply it to the honours degree, call it a regulatory requirement or treat it as a master's pass threshold. Set it beside qaa/fheq-2024/4.17.b1 and spine:7."
  author-agent-dialogue: "Raise this when a master's student is analysing images or objects in depth. With a master's student, say plainly what you should usually be able to do by the end; with staff, frame it as what the course typically develops at Level 7. Ask: \"Take an image you know well: what can you now see in it that you missed as an undergraduate?\" Avoid presenting this typical list as the minimum for the award."
- statement: qaa/history-of-art-architecture-and-design-2026/4.6.b2.masters
  forPractitioner: { text: "Master's graduates should typically work systematically and critically with texts and artefacts and with the theories and methods of the field.", rewrite: light, force: should, status: drafted }
  forBeneficiary: { text: "At master's level, you should usually work systematically and critically with texts, objects and the theories and methods used to study them.", rewrite: full, force: should, status: drafted }
  author-agent-written: "Present this as a typical outcome, in should, for a master's graduate at FHEQ Level 7 (FQHEIS Level 11): systematic, critical work with texts, artefacts and theory. Cite it as (QAA, 2026, History of Art, Architecture and Design Subject Benchmark Statement, para 4.6). Do not apply it to the honours degree, call it a regulatory requirement or treat it as a master's pass threshold. Set it beside qaa/fheq-2024/4.17.b1 and qaa/fheq-2024/4.17.b4.2 and spine:7."
  author-agent-dialogue: "Raise this when a master's student is planning a literature or object review. With a master's student, say plainly what you should usually be able to do by the end; with staff, frame it as what the course typically develops at Level 7. Ask: \"How systematic was your approach to the sources in your last project?\" Avoid presenting this typical list as the minimum for the award."
- statement: qaa/history-of-art-architecture-and-design-2026/4.6.b3.masters
  forPractitioner: { text: "Master's graduates should typically understand how methodological change and research trends have overturned received views and readings in the field.", rewrite: light, force: should, status: drafted }
  forBeneficiary: { text: "At master's level, you should usually be able to explain how new methods and research have overturned older assumptions about art, architecture or design.", rewrite: full, force: should, status: drafted }
  author-agent-written: "Present this as a typical outcome, in should, for a master's graduate at FHEQ Level 7 (FQHEIS Level 11): how methods and research have unsettled received readings. Cite it as (QAA, 2026, History of Art, Architecture and Design Subject Benchmark Statement, para 4.6). Do not apply it to the honours degree, call it a regulatory requirement or treat it as a master's pass threshold. Set it beside qaa/fheq-2024/4.17.b1 and qaa/fheq-2024/4.17.b4.2 and spine:7."
  author-agent-dialogue: "Raise this when a master's student is writing on historiography or the state of the field. With a master's student, say plainly what you should usually be able to do by the end; with staff, frame it as what the course typically develops at Level 7. Ask: \"Which older reading in your field has been overturned, and by what kind of research?\" Avoid presenting this typical list as the minimum for the award."
- statement: qaa/history-of-art-architecture-and-design-2026/4.6.b4.masters
  forPractitioner: { text: "Master's graduates should typically put unfamiliar arguments and artefacts to good use and question the field's established ideas.", rewrite: light, force: should, status: drafted }
  forBeneficiary: { text: "At master's level, you should usually be able to make good use of unfamiliar arguments and objects while questioning the field's established ideas.", rewrite: full, force: should, status: drafted }
  author-agent-written: "Present this as a typical outcome, in should, for a master's graduate at FHEQ Level 7 (FQHEIS Level 11): unfamiliar material set against established ideas. Cite it as (QAA, 2026, History of Art, Architecture and Design Subject Benchmark Statement, para 4.6). Do not apply it to the honours degree, call it a regulatory requirement or treat it as a master's pass threshold. Set it beside qaa/fheq-2024/4.17.b3 and spine:7."
  author-agent-dialogue: "Raise this when a master's student is testing a received view. With a master's student, say plainly what you should usually be able to do by the end; with staff, frame it as what the course typically develops at Level 7. Ask: \"Which established idea in your field have you questioned, and what unfamiliar evidence did you bring?\" Avoid presenting this typical list as the minimum for the award."
- statement: qaa/history-of-art-architecture-and-design-2026/4.6.b5.masters
  forPractitioner: { text: "Master's graduates should typically show advanced knowledge of the subject's place in wider social and political contexts.", rewrite: light, force: should, status: drafted }
  forBeneficiary: { text: "At master's level, you should usually know in depth how your subject connects with wider social and political questions.", rewrite: full, force: should, status: drafted }
  author-agent-written: "Present this as a typical outcome, in should, for a master's graduate at FHEQ Level 7 (FQHEIS Level 11): the subject in its social and political setting. Cite it as (QAA, 2026, History of Art, Architecture and Design Subject Benchmark Statement, para 4.6). Do not apply it to the honours degree, call it a regulatory requirement or treat it as a master's pass threshold. Set it beside qaa/fheq-2024/4.17.b1 and spine:7."
  author-agent-dialogue: "Raise this when a master's student asks why the subject matters beyond the academy. With a master's student, say plainly what you should usually be able to do by the end; with staff, frame it as what the course typically develops at Level 7. Ask: \"How does your research topic connect with a current social or political question?\" Avoid presenting this typical list as the minimum for the award."
- statement: qaa/history-of-art-architecture-and-design-2026/4.6.b6.masters
  forPractitioner: { text: "Master's graduates should typically form a systematic, critically engaged view of how museums, galleries and heritage bodies represent art.", rewrite: light, force: should, status: drafted }
  forBeneficiary: { text: "At master's level, you should usually have a systematic and critical way of looking at how museums, galleries and heritage sites present art.", rewrite: full, force: should, status: drafted }
  author-agent-written: "Present this as a typical outcome, in should, for a master's graduate at FHEQ Level 7 (FQHEIS Level 11): a critical approach to display and representation. Cite it as (QAA, 2026, History of Art, Architecture and Design Subject Benchmark Statement, para 4.6). Do not apply it to the honours degree, call it a regulatory requirement or treat it as a master's pass threshold. Set it beside qaa/fheq-2024/4.17.b4.1 and spine:7."
  author-agent-dialogue: "Raise this when a master's student is studying exhibitions, curating or heritage interpretation. With a master's student, say plainly what you should usually be able to do by the end; with staff, frame it as what the course typically develops at Level 7. Ask: \"What choices did the last exhibition you saw make about how to present its art, and what did they leave out?\" Avoid presenting this typical list as the minimum for the award."
- statement: qaa/history-of-art-architecture-and-design-2026/4.6.b7.masters
  forPractitioner: { text: "Master's graduates should typically be comprehensively grounded in analysis, argument and expression.", rewrite: light, force: should, status: drafted }
  forBeneficiary: { text: "At master's level, you should usually be thoroughly skilled in analysing, arguing and expressing your ideas.", rewrite: full, force: should, status: drafted }
  author-agent-written: "Present this as a typical outcome, in should, for a master's graduate at FHEQ Level 7 (FQHEIS Level 11): grounding in analysis, argument and expression. Cite it as (QAA, 2026, History of Art, Architecture and Design Subject Benchmark Statement, para 4.6). Do not apply it to the honours degree, call it a regulatory requirement or treat it as a master's pass threshold. Set it beside qaa/fheq-2024/4.17.b5 and spine:7."
  author-agent-dialogue: "Raise this when a master's student asks how their writing should change from undergraduate work. With a master's student, say plainly what you should usually be able to do by the end; with staff, frame it as what the course typically develops at Level 7. Ask: \"Which of analysis, argument or expression is your strongest, and which needs work?\" Avoid presenting this typical list as the minimum for the award."
- statement: qaa/history-of-art-architecture-and-design-2026/4.6.b8.masters
  forPractitioner: { text: "Master's graduates should typically bring together data from a range of pertinent original and secondary sources and see how they connect.", rewrite: light, force: should, status: drafted }
  forBeneficiary: { text: "At master's level, you should usually gather information from many original and secondary sources and see how they connect.", rewrite: full, force: should, status: drafted }
  author-agent-written: "Present this as a typical outcome, in should, for a master's graduate at FHEQ Level 7 (FQHEIS Level 11): assembling and connecting sources. Cite it as (QAA, 2026, History of Art, Architecture and Design Subject Benchmark Statement, para 4.6). Do not apply it to the honours degree, call it a regulatory requirement or treat it as a master's pass threshold. Set it beside qaa/fheq-2024/4.17.b2 and spine:7."
  author-agent-dialogue: "Raise this when a master's student is building an evidence base for a dissertation. With a master's student, say plainly what you should usually be able to do by the end; with staff, frame it as what the course typically develops at Level 7. Ask: \"How do your primary and secondary sources speak to each other in your project?\" Avoid presenting this typical list as the minimum for the award."
- statement: qaa/history-of-art-architecture-and-design-2026/4.6.b9.masters
  forPractitioner: { text: "Master's graduates should typically know their academic strengths and weak points and review how well they are performing and progressing.", rewrite: light, force: should, status: drafted }
  forBeneficiary: { text: "At master's level, you should usually know where you are strong and weak academically and reflect on how you are getting on.", rewrite: full, force: should, status: drafted }
  author-agent-written: "Present this as a typical outcome, in should, for a master's graduate at FHEQ Level 7 (FQHEIS Level 11): self-knowledge and reflection. Cite it as (QAA, 2026, History of Art, Architecture and Design Subject Benchmark Statement, para 4.6). Do not apply it to the honours degree, call it a regulatory requirement or treat it as a master's pass threshold. Set it beside qaa/fheq-2024/4.17.b8.3 and spine:7."
  author-agent-dialogue: "Raise this when a master's student is planning development or responding to feedback. With a master's student, say plainly what you should usually be able to do by the end; with staff, frame it as what the course typically develops at Level 7. Ask: \"What is one academic weakness you are working on, and how will you know it has improved?\" Avoid presenting this typical list as the minimum for the award."
- statement: qaa/history-of-art-architecture-and-design-2026/4.6.b10.masters
  forPractitioner: { text: "Master's graduates should typically identify how intellectual approaches relate and choose those suited to a particular case.", rewrite: light, force: should, status: drafted }
  forBeneficiary: { text: "At master's level, you should usually see how different ways of thinking relate and choose the right one for each case.", rewrite: full, force: should, status: drafted }
  author-agent-written: "Present this as a typical outcome, in should, for a master's graduate at FHEQ Level 7 (FQHEIS Level 11): relating approaches and choosing one. Cite it as (QAA, 2026, History of Art, Architecture and Design Subject Benchmark Statement, para 4.6). Do not apply it to the honours degree, call it a regulatory requirement or treat it as a master's pass threshold. Set it beside qaa/fheq-2024/4.17.b4.2 and spine:7."
  author-agent-dialogue: "Raise this when a master's student is choosing a framework for a project. With a master's student, say plainly what you should usually be able to do by the end; with staff, frame it as what the course typically develops at Level 7. Ask: \"Why did you choose this approach for your case rather than another?\" Avoid presenting this typical list as the minimum for the award."
- statement: qaa/history-of-art-architecture-and-design-2026/4.6.b11.masters
  forPractitioner: { text: "Master's graduates should typically carry out an original, self-directed research project.", rewrite: light, force: should, status: drafted }
  forBeneficiary: { text: "At master's level, you should usually carry out an original research project that you lead yourself.", rewrite: full, force: should, status: drafted }
  author-agent-written: "Present this as a typical outcome, in should, for a master's graduate at FHEQ Level 7 (FQHEIS Level 11): an original, self-directed research project. Cite it as (QAA, 2026, History of Art, Architecture and Design Subject Benchmark Statement, para 4.6). Do not apply it to the honours degree, call it a regulatory requirement or treat it as a master's pass threshold. Set it beside qaa/fheq-2024/4.17.b3 and qaa/fheq-2024/4.17.b6 and spine:7."
  author-agent-dialogue: "Raise this when a master's student is scoping a dissertation. With a master's student, say plainly what you should usually be able to do by the end; with staff, frame it as what the course typically develops at Level 7. Ask: \"What is original about your research project, and which decisions in it were yours?\" Avoid presenting this typical list as the minimum for the award."
- statement: qaa/history-of-art-architecture-and-design-2026/4.6.b12.masters
  forPractitioner: { text: "Master's graduates should typically put across ideas and well-built arguments effectively to both expert and lay audiences.", rewrite: light, force: should, status: drafted }
  forBeneficiary: { text: "At master's level, you should usually explain ideas and well-built arguments clearly to experts and non-experts.", rewrite: full, force: should, status: drafted }
  author-agent-written: "Present this as a typical outcome, in should, for a master's graduate at FHEQ Level 7 (FQHEIS Level 11): communication to expert and lay audiences. Cite it as (QAA, 2026, History of Art, Architecture and Design Subject Benchmark Statement, para 4.6). Do not apply it to the honours degree, call it a regulatory requirement or treat it as a master's pass threshold. Set it beside qaa/fheq-2024/4.17.b5 and spine:7."
  author-agent-dialogue: "Raise this when a master's student is presenting research or writing for the public. With a master's student, say plainly what you should usually be able to do by the end; with staff, frame it as what the course typically develops at Level 7. Ask: \"How would you present your research to a museum visitor rather than an examiner?\" Avoid presenting this typical list as the minimum for the award."
```

### S5 Levels and alignment
<!-- label: both; status: drafted; basis: primary -->
```yaml
levels:
  - { id: "fheq:4", role: "cites", locator: "D1, 2.9 (Certificate of Higher Education)" }
  - { id: "fheq:5", role: "cites", locator: "D1, 2.9 (Diploma of Higher Education)" }
  - { id: "fheq:6", role: "cites", locator: "D1, 2.6; 2.10; 2.12; 2.15" }
  - { id: "fheq:7", role: "cites", locator: "D1, 2.6; 2.12; 2.15; 4.4" }
  - { id: "fqheis:8", role: "cites", locator: "D1, 2.9 (as the statement gives it for the CertHE: Part E)" }
  - { id: "fqheis:9", role: "cites", locator: "D1, 2.9 (DipHE, as stated: Part E); 2.11 (ordinary degree and MA)" }
  - { id: "fqheis:10", role: "cites", locator: "D1, 2.6; 2.11; 2.12" }
  - { id: "fqheis:11", role: "cites", locator: "D1, 2.6; 2.12; 4.4" }
crosswalks:
  - { from: "fheq:6", to: "fqheis:10", relation: "equivalent", basis: "stated (D1, 2.6; 2.12: the honours degree at FHEQ Level 6 and FQHEIS Level 10); agrees with FHEQ Table 1" }
  - { from: "fheq:7", to: "fqheis:11", relation: "equivalent", basis: "stated (D1, 2.6; 2.12; 4.4: master's at Level 7 in England, Wales and Northern Ireland and Level 11 in Scotland); agrees with FHEQ 4.17" }
  - { from: "fheq:4", to: "fqheis:8", relation: "equivalent", basis: "stated (D1, 2.9: CertHE at FHEQ Level 4, FQHEIS Level 8); differs from FHEQ Table 1, which puts the CertHE at FQHEIS 7 (Part E)" }
  - { from: "fheq:5", to: "fqheis:9", relation: "equivalent", basis: "stated (D1, 2.9: DipHE at FHEQ Level 5, FQHEIS Level 9); differs from FHEQ Table 1, which puts the DipHE at FQHEIS 8 (Part E)" }
```

### S6 Themes
<!-- label: both; status: drafted; basis: primary -->
```yaml
- { id: "theme:edi", role: "carries", carriedIn: ["1.7", "1.10", "1.11", "1.12", "1.13", "2.16", "3.7", "3.13", "4.3", "4.4", "4.5"] }
- { id: "theme:accessibility", role: "carries", carriedIn: ["1.13", "1.14", "1.15", "2.16", "3.8", "3.13"] }
- { id: "theme:esd", role: "carries", carriedIn: ["1.7", "1.8", "1.16", "1.17", "1.18", "1.23", "1.26", "4.4", "4.5"] }
- { id: "theme:enterprise", role: "carries", carriedIn: ["1.19", "1.20", "1.21", "1.25", "2.2", "2.17"] }
- { id: "theme:generative-ai", role: "carries", carriedIn: ["1.14", "1.18", "1.22", "1.23", "1.24", "1.25", "1.26", "3.6", "3.8", "3.12", "4.5"] }
```

### S7 Relations
<!-- label: both; status: drafted; basis: primary -->
```yaml
- { rel: "partOf", target: "collection: QAA Subject Benchmark Statements", note: "one of 54 held by stan" }
- { rel: "supersedes", target: "std:doc:qaa-history-of-art-architecture-and-design-2019-benchmarks (not ingested)", note: "the fourth edition, 2019 minor update; earlier editions 2016, 2007 and 2002 (back matter)" }
- { rel: "refersTo", target: "std:doc:qaa-fheq-2024-framework, Annex D", note: "the degree classification descriptions for bachelor's degrees with honours (4.2)" }
- { rel: "refersTo", target: "std:doc:qaa-fheq-2024-framework", note: "FHEQ Levels 4 to 7 (2.6, 2.9, 2.10, 2.12, 2.15)" }
- { rel: "refersTo", target: "std:doc:qaa-fqheis-2024-framework", note: "FQHEIS (SCQF) Levels 8 to 11 (2.6, 2.9, 2.11, 2.12; 4.4 by level number)" }
- { rel: "refersTo", target: "QAA Quality Code, 2024 update (not ingested)", note: "front matter" }
- { rel: "refersTo", target: "Equality and Human Rights Commission guidance on competence standards (not ingested)", note: "4.3" }
```

### S8 Currency and review
<!-- label: source; status: drafted; basis: primary -->
```yaml
published: "2026-04"
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
- Studies artefacts as visual and material culture in every medium, from painting, sculpture and buildings to applied arts, performance, photography, film, social media and games, past and present (D1, 1.3, 1.5).
- Joins close description (formal, iconographic, semiotic, material, spatial or functional analysis) with critical study of context, making, patronage and use (D1, 1.5, 1.6).
- Reads "art" and "design" as historical categories shaped by colonialism, the Enlightenment and modern institutions, and examines inequalities of power and histories pushed to the margins (D1, 1.4, 1.7, 1.11).
- Interdisciplinary by nature, drawing on archives, literary texts and scientific analysis across the arts, humanities and sciences (D1, 1.6, 2.2).
- Display is part of the subject: museums, galleries, heritage sites and digital display shape how artefacts are received, and many partner with courses (D1, 1.8, 3.4).
- Object-based learning and visual and material literacy are its signature skills, built through study visits, collections and handling (D1, 2.2, 3.5, 3.8).
- Taught as single honours and as a component of many other degrees, among them fine art, design, architecture, heritage, curating and media (D1, 1.2).

### SB2 Themes in this subject
<!-- label: both; status: drafted; basis: primary -->
```yaml
- theme: theme:edi
  inThisSubject: "the subject examines power, class, race, gender, sexuality and health in artefacts, recentres marginalised voices, questions Eurocentric narratives and object provenance, and ties inclusive environments to the Equality Act and partnership practice (D1, 1.7, 1.10 to 1.12, 2.16); inclusive interpretation is a typical generic skill (4.4)"
  statements: ["qaa/history-of-art-architecture-and-design-2026/3.13", "qaa/history-of-art-architecture-and-design-2026/4.3", "qaa/history-of-art-architecture-and-design-2026/4.4.b14.typical", "qaa/history-of-art-architecture-and-design-2026/4.5.b4"]
- theme: theme:accessibility
  inThisSubject: "accessible teaching and assessment, hybrid delivery and reasonable adjustment under equality law; no prerequisites and portfolio entry; assessment inclusive by design (D1, 1.13 to 1.15, 3.13)"
  statements: ["qaa/history-of-art-architecture-and-design-2026/3.13"]
- theme: theme:esd
  inThisSubject: "artefacts as vehicles for the UN goals; the environmental cost of making, conserving, travelling to and digitising artefacts; environmental context is part of the threshold skill of situating artefacts (D1, 1.16 to 1.18; 4.4)"
  statements: ["qaa/history-of-art-architecture-and-design-2026/4.4.b7", "qaa/history-of-art-architecture-and-design-2026/4.5.b4"]
- theme: theme:enterprise
  inThisSubject: "the cultural economy and art markets, experiential and partnership learning, curatorial and public programming tasks, and graduate routes into museums, heritage and creative industries (D1, 1.19 to 1.21, 2.17)"
  statements: []
- theme: theme:generative-ai
  inThisSubject: "guidance and disclosure of use, questions of authorship and creativity, critical AI fluency, new assessment forms and concerns over bias and energy use (D1, 1.22 to 1.26, 3.12); ethical use is a transferable skill (4.5)"
  statements: ["qaa/history-of-art-architecture-and-design-2026/4.5.b5"]
```

### SB3 Content and delivery
<!-- label: both; status: drafted; basis: primary -->
```yaml
areas:
  - { component: "1.3", gloss: "artefacts by medium: painting, sculpture, architecture, applied arts, lens and screen media, performance" }
  - { component: "1.5", gloss: "descriptive methods: formalism, iconography, semiotics, materiality, spatial and functional analysis" }
  - { component: "3.2", gloss: "many periods, places and cultures, studied in depth and comparatively; content varies by provider" }
  - { component: "3.5", gloss: "historiography of the discipline, physical properties of artefacts, contemporary professional contexts" }
practices:
  - { component: "1.14", kind: "teaching", gloss: "lectures, seminars, tutorials, peer learning and off-campus visits" }
  - { component: "2.4", kind: "learning", gloss: "digital reproductions, databases and archives; fieldwork and site-based learning" }
  - { component: "2.5", kind: "assessment", gloss: "independent and group tasks; formative and summative balance" }
  - { component: "3.4", kind: "teaching", gloss: "research-informed teaching; collections partnerships" }
  - { component: "3.6", kind: "teaching", gloss: "varied output formats; visual literacy and communication" }
  - { component: "3.7", kind: "learning", gloss: "inclusive design; study visits; placements on some courses" }
  - { component: "3.8", kind: "teaching", gloss: "indicative methods and approaches: object-based, experiential, collaborative, problem-based, authentic, creative, digital" }
  - { component: "3.9", kind: "assessment", gloss: "feedback points; criteria in handbooks" }
  - { component: "3.10", kind: "assessment", gloss: "flexible, aligned, formative and summative" }
  - { component: "3.11", kind: "assessment", gloss: "self- and peer assessment for independence" }
  - { component: "3.12", kind: "assessment", gloss: "a broader portfolio in response to generative AI" }
  - { component: "3.13", kind: "assessment", gloss: "indicative methods: tests, written and spoken, creative and digital, industry-based" }
```

### SB4 Benchmark standards
<!-- label: both; status: drafted; basis: primary -->
```yaml
rungs:
  - { rung: "threshold", leadIn: "4.4", award: "bachelor's with honours", items: 15 }
  - { rung: "typical", leadIn: "4.4", award: "bachelor's with honours", items: 15 }
  - { rung: "typical", leadIn: "4.6", award: "master's", items: 12 }
rungBases: "4.4: threshold is the minimum acceptable standard of an honours graduate, equivalent to a third; typical is the standard most honours graduates attain, equivalent to a second; no excellent rung (4.2 leaves performance above threshold to Annex D). 4.6's master's list says 'should typically', recorded as a typical rung for the master's award"
outcomeLists:
  - { leadIn: "4.5", gloss: "transferable skills on graduating with honours", items: 10, award: ["honours"] }
outcomes:
  - { outcome: "range of cultures studied", threshold: "qaa/history-of-art-architecture-and-design-2026/4.4.b1", typical: "qaa/history-of-art-architecture-and-design-2026/4.4.b1.typical", excellent: "none", basis: "stated", domain: "knowledge", award: "bachelor's with honours" }
  - { outcome: "materials and techniques", threshold: "qaa/history-of-art-architecture-and-design-2026/4.4.b2", typical: "qaa/history-of-art-architecture-and-design-2026/4.4.b2.typical", excellent: "none", basis: "stated", domain: "knowledge", award: "bachelor's with honours" }
  - { outcome: "current debates", threshold: "qaa/history-of-art-architecture-and-design-2026/4.4.b3", typical: "qaa/history-of-art-architecture-and-design-2026/4.4.b3.typical", excellent: "none", basis: "stated", domain: "understanding", award: "bachelor's with honours" }
  - { outcome: "professional practice", threshold: "qaa/history-of-art-architecture-and-design-2026/4.4.b4", typical: "qaa/history-of-art-architecture-and-design-2026/4.4.b4.typical", excellent: "none", basis: "stated", domain: "knowledge", award: "bachelor's with honours" }
  - { outcome: "cultures and identities", threshold: "qaa/history-of-art-architecture-and-design-2026/4.4.b5", typical: "qaa/history-of-art-architecture-and-design-2026/4.4.b5.typical", excellent: "none", basis: "stated", domain: "understanding", award: "bachelor's with honours" }
  - { outcome: "observation and description", threshold: "qaa/history-of-art-architecture-and-design-2026/4.4.b6", typical: "qaa/history-of-art-architecture-and-design-2026/4.4.b6.typical", excellent: "none", basis: "stated", domain: "subject-skill", award: "bachelor's with honours" }
  - { outcome: "context", threshold: "qaa/history-of-art-architecture-and-design-2026/4.4.b7", typical: "qaa/history-of-art-architecture-and-design-2026/4.4.b7.typical", excellent: "none", basis: "stated", domain: "subject-skill", award: "bachelor's with honours" }
  - { outcome: "evidence from sources", threshold: "qaa/history-of-art-architecture-and-design-2026/4.4.b8", typical: "qaa/history-of-art-architecture-and-design-2026/4.4.b8.typical", excellent: "none", basis: "stated", domain: "subject-skill", award: "bachelor's with honours" }
  - { outcome: "methods and theories", threshold: "qaa/history-of-art-architecture-and-design-2026/4.4.b9", typical: "qaa/history-of-art-architecture-and-design-2026/4.4.b9.typical", excellent: "none", basis: "stated", domain: "subject-skill", award: "bachelor's with honours" }
  - { outcome: "evidenced argument", threshold: "qaa/history-of-art-architecture-and-design-2026/4.4.b10", typical: "qaa/history-of-art-architecture-and-design-2026/4.4.b10.typical", excellent: "none", basis: "stated", domain: "subject-skill", award: "bachelor's with honours" }
  - { outcome: "alternative arguments", threshold: "qaa/history-of-art-architecture-and-design-2026/4.4.b11", typical: "qaa/history-of-art-architecture-and-design-2026/4.4.b11.typical", excellent: "none", basis: "stated", domain: "subject-skill", award: "bachelor's with honours" }
  - { outcome: "communication", threshold: "qaa/history-of-art-architecture-and-design-2026/4.4.b12", typical: "qaa/history-of-art-architecture-and-design-2026/4.4.b12.typical", excellent: "none", basis: "stated", domain: "generic-skill", award: "bachelor's with honours" }
  - { outcome: "research", threshold: "qaa/history-of-art-architecture-and-design-2026/4.4.b13", typical: "qaa/history-of-art-architecture-and-design-2026/4.4.b13.typical", excellent: "none", basis: "stated", domain: "generic-skill", award: "bachelor's with honours" }
  - { outcome: "open-minded and inclusive interpretation", threshold: "qaa/history-of-art-architecture-and-design-2026/4.4.b14", typical: "qaa/history-of-art-architecture-and-design-2026/4.4.b14.typical", excellent: "none", basis: "stated", domain: "generic-skill", award: "bachelor's with honours" }
  - { outcome: "values and ethics", threshold: "qaa/history-of-art-architecture-and-design-2026/4.4.b15", typical: "qaa/history-of-art-architecture-and-design-2026/4.4.b15.typical", excellent: "none", basis: "stated", domain: "generic-skill", award: "bachelor's with honours" }
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
- { body: "Professional, statutory and regulatory bodies (PSRBs), none named", says: "architecture courses with HAAD modules may be subject to PSRB requirements; courses with professional outcomes may need their accreditation; competence standards may draw on PSRB requirements (D1, 1.15, 2.21, 4.3; front matter)", requirements: "not yet ingested (Part E)" }
- { body: "Equality and Human Rights Commission", says: "providers developing competence standards should follow its most recent guidance (D1, 4.3)", requirements: "not yet ingested (Part E)" }
- { body: "Office for Students", says: "in England benchmark statements are not sector-recognised standards under its regulatory framework (D1, front matter)", requirements: "not-applicable-by-design: named for status only (Part E)" }
```

### SB6 Cross-cutting references
<!-- label: both; status: drafted; basis: primary -->
```yaml
themes:
  - { id: "theme:edi", named: "Equity, diversity and inclusion", carriedIn: ["1.7", "1.10", "1.11", "1.12", "1.13", "2.16", "3.7", "3.13", "4.3", "4.4", "4.5"], statements: ["3.13", "4.3", "4.4.b14.typical", "4.5.b4"] }
  - { id: "theme:accessibility", named: "Accessibility and the needs of disabled students", carriedIn: ["1.13", "1.14", "1.15", "2.16", "3.8", "3.13"], statements: ["3.13"] }
  - { id: "theme:esd", named: "Education for sustainable development", carriedIn: ["1.7", "1.8", "1.16", "1.17", "1.18", "1.23", "1.26", "4.4", "4.5"], statements: ["4.4.b7", "4.5.b4"] }
  - { id: "theme:enterprise", named: "Employability, entrepreneurship and enterprise education", carriedIn: ["1.19", "1.20", "1.21", "1.25", "2.2", "2.17"], statements: [] }
  - { id: "theme:generative-ai", named: "Generative artificial intelligence", carriedIn: ["1.14", "1.18", "1.22", "1.23", "1.24", "1.25", "1.26", "3.6", "3.8", "3.12", "4.5"], statements: ["4.5.b5"] }
frameworks:
  - { framework: "fheq", levels: ["fheq:4", "fheq:5", "fheq:6", "fheq:7"], citedIn: ["2.6", "2.9", "2.10", "2.12", "2.15", "4.4"] }
  - { framework: "scqf", levels: ["fqheis:8", "fqheis:9", "fqheis:10", "fqheis:11"], citedIn: ["2.6", "2.9", "2.11", "2.12", "4.4"] }
bodies:
  - { body: "PSRBs (none named)", citedIn: ["front matter", "1.15", "2.21", "4.3"] }
  - { body: "Equality and Human Rights Commission", citedIn: ["4.3"] }
  - { body: "Office for Students", citedIn: ["front matter"] }
sharedDocuments:
  - { document: "std:doc:qaa-fheq-2024-framework, Annex D", named: "Annex D in The Frameworks for Higher Education Qualifications of UK Degree-Awarding Bodies", citedIn: ["4.2"], role: "descriptions of the four honours classes (1st, 2.1, 2.2, 3rd) for evidence above threshold" }
  - { document: "QAA Quality Code, 2024 update (not yet ingested)", named: "an update to the Quality Code", citedIn: ["front matter"], role: "a further reference point" }
  - { document: "QAA Glossary (not ingested)", named: "QAA's Glossary", citedIn: ["front matter"], role: "explains unfamiliar terms" }
  - { document: "UN Sustainable Development Goals (external)", named: "UN Sustainable Development goals (2015)", citedIn: ["1.16"], role: "the frame of the sustainability theme, goals 3, 5, 9 to 16 named" }
  - { document: "Equality Act 2010 (law)", named: "Equality Act 2010", citedIn: ["1.10", "1.13", "4.3"], role: "EDI duties, reasonable adjustment, competence standards" }
  - { document: "Disability Discrimination Act 1995 (law, Northern Ireland)", named: "Disability Discrimination Act 1995", citedIn: ["1.13"], role: "reasonable adjustment in Northern Ireland" }
  - { document: "SEND legislation and guidance (law)", named: "Special Educational Needs and Disability (SEND) legislation and guidance", citedIn: ["1.13"], role: "inclusion of disabled learners" }
```

## Part B Terminology
<!-- The statement has no glossary of its own unless Part E says so; these are terms it defines in its text. -->

### B1 Concepts
<!-- label: both; status: drafted; basis: primary -->
```yaml
- { slug: "artefact", definition: "any entity the subject studies, in any medium, from painting and buildings to screen media and performance (D1, 1.3)", beneficiaryDefinition: "any object, image, building, design or performance you study", scopeNote: "the statement's own umbrella term", category: "unknown", practices: ["education"] }
- { slug: "visual-and-material-culture", definition: "the subject's object of study across all regions and periods, wider than \"art\" and \"design\" (D1, 1.4)", beneficiaryDefinition: "everything people have made to be seen or used", scopeNote: "replaces a focus on intrinsic artistic quality", category: "unknown", practices: ["education"] }
- { slug: "threshold-standard", definition: "the minimum acceptable standard of an honours graduate, equivalent to a third-class degree (D1, 4.4)", beneficiaryDefinition: "the least you need to show to gain the honours degree", scopeNote: "paired with typical in the 4.4 table", category: "unknown", practices: ["education"] }
- { slug: "typical-standard", definition: "the standard most honours graduates reach, equivalent to a second-class degree (D1, 4.4)", beneficiaryDefinition: "the level most students reach", scopeNote: "used for the master's list too (\"should typically\", 4.6)", category: "unknown", practices: ["education"] }
- { slug: "haad", definition: "the abbreviation the statement uses for the subject (D1, 1.1)", scopeNote: "used throughout", category: "unknown", practices: ["education"] }
```

### B2a Terms as the issuer defines them
<!-- label: source; status: drafted; basis: primary -->
```yaml
- { concept: "artefact", form: "artefacts", lang: "en", partOfSpeech: "noun", termStatus: "preferred", register: "discipline-specific" }
- { concept: "visual-and-material-culture", form: "visual and material culture", lang: "en", partOfSpeech: "noun-phrase", termStatus: "preferred", register: "discipline-specific" }
- { concept: "threshold-standard", form: "threshold", lang: "en", partOfSpeech: "noun", termStatus: "preferred", register: "formal" }
- { concept: "typical-standard", form: "typical", lang: "en", partOfSpeech: "adjective", termStatus: "preferred", register: "formal" }
- { concept: "haad", form: "HAAD", lang: "en", partOfSpeech: "noun", termStatus: "preferred", register: "formal" }
```

### B2b Associated vocabulary
`not-applicable-by-design`: the statement names no wider vocabulary.

### B3 Framework blocks
`not-applicable-by-design`: no term is defined its own way for one component.

### B4 Relations
<!-- label: both; status: drafted; basis: primary -->
```yaml
- { rel: "contrasts-with", from: "threshold-standard", to: "typical-standard", note: "4.4: the two rungs of the table" }
```

## Part C Process
<!-- label: both; status: drafted; basis: primary -->

### C0 Formality
`not-applicable`: the statement sets out what graduates achieve and what courses provide, not a procedure.

## Part D Sources
```yaml
- key: D1
  issuer: The Quality Assurance Agency for Higher Education
  title: "Subject Benchmark Statement: History of Art, Architecture and Design"
  edition: "April 2026 (fifth edition)"
  year: 2026
  url: unknown (the QAA page; the text came by stan's extraction)
  retrieved: "held from stan: wkspc2615-QAAVector mapped/history-of-art-architecture-and-design-2026/history-of-art-architecture-and-design-2026.raw.txt, commit 366bcb99a01118f2c4c3ebfa2a8337596bddc455; received 2026-10-03"
  licence: QAA copyright
  tier: primary
  readVia: direct
  held: 0cfad140e51634d734d72d1afd40a3f9cea7eaeae7317abfc50fea6b9924f4aa
  heldFiles: ["wkspc2601-library/txt/qaa-2026-history-art-architecture-design-subject-benchmark-standard.txt", "wkspc2601-library/txt/qaa-2026-history-art-architecture-design-subject-benchmark-standard.norm.txt", "wkspc2601-library/records/qaa-2026-history-art-architecture-design-subject-benchmark-standard.chunks.json", "wkspc2601-library/records/qaa-2026-history-art-architecture-design-subject-benchmark-standard.held.json"]
  citedIn: [S1, S2, S3, S4, S4a, S5, S6, S7, SB1, SB2, SB3, SB4, SB5, SB6]
```

### D2 Research log
```yaml
- { ref: D1, tier: primary, consulted: 2026-10-03, pass: P1, outcome: "read whole, direct, from the normalised text; skeleton by tools/std_prep.py, document by tools/bm_build.py" }
- { ref: "ADAPT subj HESA stores, cah.json and hecos.json (designs/ingest/standards/subj/vocab)", tier: primary, consulted: 2026-10-03, pass: P1, outcome: "codes for statedSubjects and subjects" }
```

### D3 Wanted sources
```yaml
- { w: "W-std-0068", citation: "QAA (2019) Subject Benchmark Statement: History of Art, Architecture and Design, fourth edition (minor update)", settles: ["S7"], asked: "2026-10-03", state: "wanted" }
```

## Part E Gaps and questions
- SB4, pattern (differs from Psychology): two rungs only, threshold and typical, in one table of 15 rows across three blocks (subject knowledge, subject-specific skills, generic intellectual skills); no excellent rung. Each cell has its own text, so each is its own record with its own span; the typical cell is `<id>.typical`, and `gradeOf` is stated, the issuer pairing the cells in one row.
- SB4, flattened table (P3): the table is flattened in the held text, cells running threshold then typical, row by row. Placement read from the order and the plain pairing of content. The generic intellectual skills block has no column headings in the held text; its four rows were placed by the same alternation (threshold first). Least sure: row 14 (open-mindedness to inclusive interpretation), where the pairing is by theme, not by shared wording.
- SB4, row 7: the threshold cell names environmental context; the typical cell drops "environmental". Kept as the issuer has it; ESD tagged on the threshold cell only.
- SB4, master's: 4.6's lead-in reads 'should typically be able to'. Recorded as rung typical, award master's, level fheq:7, ids `.masters`, per the batch 1 convention ('the rung its heading names'; here the lead-in's word). For P3: threshold may be the intended reading.
- S4, force: the table cells take force from distant lead-ins: threshold cells `threshold` (4.4 defines it as the minimum for the award; forceFrom 4.4); typical cells `will` from 4.1 ("a student will have demonstrated"; forceFrom 4.1). 4.5 and 4.6 take `should` from their lead-ins.
- S4, 4.5 list: transferable skills on graduating with honours in "should be able to", not tied to a rung; recorded as an outcome list (rung none). The lead-in sits under the 4.4 heading run and 4.5 has no rung of its own: for P3.
- S4, 4.5.b1 and 4.5.b2: the held text runs two bullets together across a page break ("... written English work as part of a team ..."). Split into two records; 4.5.b1's span crosses the page number 19, so its `source` carries that page number. Skeleton ids 4.5.b2 to 4.5.b9 renumbered 4.5.b3 to 4.5.b10 by `find`.
- S4, skeleton correction: candidates 3.8.b1 to b42 and 3.13.b1 to b18 are indicative lists of teaching and assessment methods ("not exhaustive", "indicative rather than prescriptive"), not standards; recorded as practice components (SB3). The skeleton found no rungs: the rungs were judged by hand.
- S4, statements taken from prose: 2.3, 2.6, 2.8, 2.18 (sentence), 2.19 and 3.13 (sentence) in will; 4.2 and 4.3 in should. 2.6 and 2.8 are learner outcomes; the rest provider duties with no student version. Domain `none` for these paragraph statements, as in Psychology.
- S4, obliging words outside the five, not taken as statements, for Abbott: 2.7 "it would be expected that" (readiness for postgraduate study); 2.17 "are also expected to be beneficial" (partnerships for hosts); 2.6 "it is expected that" sits inside a statement taken on its "will".
- S4, plain-present provider norms, not statements (template open point 5): 1.13 (access proactively considered), 1.22 and 1.24 (students given guidance on GenAI), 2.12 (integrated master's designed to meet descriptors), 2.15 (formal partnerships aligned and reviewed), 2.16 (providers ensure equal opportunity; formal contracts), 3.9 (criteria communicated via handbooks), 3.11 and 3.12 (designers consider methods).
- S4, predictive "will" not taken: 1.25 ("Critical GenAI fluency will also enhance graduates' employability skills"), 2.20 (external examiners will be asked and will consider), 3.2 (content will vary).
- S5, levels (doubt for P3): 2.9 places the CertHE at FQHEIS Level 8 and the DipHE at FQHEIS Level 9. The FHEQ document (Table 1) places them at SCQF 7 and 8. Recorded as stated with the difference noted in S5; the issuer's text may be in error.
- S5, levels: 4.4 cites "Level 7 (in England, Northern Ireland and Wales) and Level 11 (in Scotland)" without naming a framework; read as fheq:7 and fqheis:11 and listed in SB6 under both frameworks.
- S5, generic skills: every generic-skill record carries fheq:6 (honours) or fheq:7 (master's), both in S5; the framework descriptors each instruction sets them beside are 4.15 and 4.17 of std:doc:qaa-fheq-2024-framework (inferred pairings, ours).
- SB6: the cross-cutting themes are named as five in the front matter (EDI; accessibility; ESD; EEE; GenAI) and each has its own heading in section 1. GenAI uses theme:generative-ai. 2.15's "sustainability and resilience of delivery" means continuity, not ESD, and is not tagged.
- SB6: CQFW is not cited. No subject association is named outside the back matter (the Association for Art History appears only in the advisory group list, excluded matter).
- SB5: the PSRBs are named only as a class; none is identified, so no requirements document can be linked. The EHRC's guidance is not yet ingested. The Office for Students is named for status only.
- S2, subjects: HECoS 100306, 100782 and 100783 and CAH20-01-02 are taken as stated: the title names history of art, architecture and design, and CAH20-01-02 carries the same label. The 1.2 programme codes are for degrees that include HAAD components, not the benchmark's own scope.
- S7: the previous edition (2019, fourth edition, minor update) is named in the back matter; earlier advisory groups 2016, 2007 and 2002 also listed. Not ingested (D3).
- S1, licence: the text gives a copyright notice and no re-use terms.
- S9: not researched in P1.
- Pattern (differs from Psychology): no professional body; a two-rung table rather than three separate lists; a master's list beside the honours standards; a generative AI theme section; the theme sections come before the distinctive features, as in the 2026 revision.
- ST-12: versions here run to the lengths the content needs; no length range is yet set.

---

## Change notes
- 0.1.2, 3 October 2026, 21:02: moved with its held text from UNI to the source library repo (`wkspc2601-library/ingested/standards/`, texts in `txt/`, records in `records/`); paths only (Abbott, 20:56; std N-0119).
- 0.1.1, 3 October 2026, 20:20: obliging words outside the five read as must, "ought to" as should, on statements outside the rungs, each marked on its force line (Abbott, 20:17; D-std-0016).
- 0.1.0, 2026-10-03 17:29: researched by run frame 0.1.1-draft and standards run layer 0.7.0-draft, std, run 0111 (P1); built by tools/bm_build.py.
