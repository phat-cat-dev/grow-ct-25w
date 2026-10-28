---
id: std:doc:qaa-accounting-2025-benchmarks
title: "Subject Benchmark Statement Accounting"
profile: standards/subject-benchmark
profileVersion: 0.2.0-draft
issuer: QAA
kind: subject-benchmark
jurisdiction: [UK]
subjectScope: subjects
subjects:
  - { scheme: "hecos", code: "100105", label: "accounting", basis: "stated" }
  - { scheme: "hecos", code: "100104", label: "accountancy", basis: "stated" }
  - { scheme: "cah", code: "CAH17-01-08", label: "accounting", basis: "stated" }
  - { scheme: "hecos", code: "100831", label: "taxation", basis: "stated" }
  - { scheme: "hecos", code: "100840", label: "audit management", basis: "inferred" }
  - { scheme: "hecos", code: "100836", label: "management accountancy", basis: "inferred" }
  - { scheme: "hecos", code: "100107", label: "finance", basis: "inferred" }
edition: "April 2025 (fifth edition)"
published: 2025-04
status: current
supersedes: "the Accounting statement of 2019 (a minor update of 2016 and earlier editions; dates from the advisory group lists, back matter)"
heldText: { method: sha256-bytes, raw: aa0d574de5b392592fe4023fcfaf70a8591a6cd7e483d981c497f40049b2e541, normalised: c0698d13bfee1e0a4172195c03a3af2587c9cf2b8a6160343d778c5d729b2545 }
heldTextStan: { method: sha256-stan, raw: aa0d574de5b392592fe4023fcfaf70a8591a6cd7e483d981c497f40049b2e541, normalised: 24faf90a513e17ba8eef0d1ddfd790d2c2ae850af7ac0f5e689b44ddb6c8711b }
licence: "QAA copyright; held for study, private to the project, never published"
series: "QAA Subject Benchmark Statements, fifth edition series with cross-cutting themes (published 10 April 2025)"
awardsCovered: ["bachelor's with honours", "master's (advanced or specialist)", "master's (conversion)", "master's (professional)", "integrated master's"]
levelsCovered: ["fheq:6", "fheq:7", "fqheis:10", "fqheis:11"]
nations: ["England", "Wales", "Scotland", "Northern Ireland"]
parts:
  S: full
  B: "partial: no glossary in the document (it points to QAA's Glossary); terms it defines in passing"
  C: "not-applicable: the document sets expectations, not a procedure"
pins: { structure: 0.13.0-draft, template: 0.8.0-draft, benchmarkTemplate: 0.6.0-draft, runFrame: 0.1.1-draft, runLayer: 0.7.0-draft, standards: none yet, terminology: none yet }
lifecycle: drafted
researchedBy: run frame 0.1.1-draft; standards run layer 0.7.0-draft; std, run 0082 (tools/bm_build.py)
passes:
  P1: "2026-10-03 16:21"
  P2: "skipped: read direct from the held text; inferred codes and rung links are for P3"
  P3: open
version: 0.1.2
---

<!-- from INGEST wpk-0016-ingest-pd-template-standards.md 0.8.0-draft and wpk-0016-ingest-pd-template-standards-benchmark.md 0.6.0-draft; built by tools/bm_build.py from run-src/ -->
# Subject Benchmark Statement: Accounting (QAA, April 2025)

> Run 0082, P1 by std. The issuer's words are held in the source library, `wkspc2601-library/txt/qaa-2025-accounting-subject-benchmark-statement-standard.norm.txt`; each S4 record carries its statement in full (`source`) for language analysis, with its span. Paraphrases and versions are ours. Private to the project, never published. In front matter `status` is the issuer's; ours is `lifecycle`. Doubts are in Part E.

## Part 0 Summary

### 0.1 Agent definition
<!-- label: editorial; status: drafted; basis: primary -->
QAA's UK reference point for what an Accounting graduate should know, understand and be able to do, for the honours degree and for four kinds of taught master's (advanced or specialist, conversion, professional, integrated). Reach for it when designing, approving, reviewing or describing an Accounting course, its outcomes or its classification boundaries. Its honours standards run on four levels (threshold, typical, very good, excellent), one per degree class; its master's standards are threshold only. It is not a regulatory requirement, not an accrediting body's syllabus and not a mark scheme.

### 0.2 Summary
<!-- label: both; status: drafted; basis: primary -->
Published by QAA on 10 April 2025, the statement covers Accounting and Accounting with another subject at undergraduate and master's levels, including Accounting with a significant finance element but not single honours finance. It sets the subject's purposes (accounting as social, economic and governance practice, beyond profit), five cross-cutting themes (EDI, accessibility, education for sustainable development, employability with enterprise and entrepreneurship, and generative AI), the distinctive features of design, progression, flexibility, partnership and review, twelve broad areas of knowledge and twelve graduate skills, and standards in two tables: Table 1 for honours at four levels tied to degree classes and to Annex D, and Table 2 for the threshold of four master's types. It names the PSRBs (the accountancy institutes in Appendix 1) as partners whose accreditation must not narrow the degree.

## Part S Standard

### S1 Identity
<!-- label: source; status: drafted; basis: primary -->
```yaml
issuer: The Quality Assurance Agency for Higher Education
title: "Subject Benchmark Statement Accounting"
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
governs: "what can be expected of a graduate in Accounting, or Accounting with another subject, at honours and taught master's level, and the nature of awards in the subject (D1, front matter; 1.1; 4.1)"
appliesTo:
  awards: ["bachelor's degrees with honours, including joint honours and degree apprenticeships (1.3, 1.15, 2.14)", "master's (advanced or specialist)", "master's (conversion)", "master's (professional)", "integrated master's"]
  levels: ["fheq:6", "fheq:7", "fqheis:10", "fqheis:11"]
  providers: ["UK higher education providers"]
whoMustUse: "none-stated; it is a reference point, not a requirement (D1, front matter)"
howUsed: ["design", "approval", "review", "other: external examining (2.32); PSRBs (front matter); prospective students and employers (front matter)"]
doesNot: "it does not prescribe teaching, learning or assessment, interpret legislation or carry statutory or regulatory requirements; it does not cover single honours finance (1.2) or research master's programmes (1.16 d) (D1, front matter)"
beneficiary: the student
statedScope: "\"The purpose of this Statement is to articulate what is to be expected of successful graduates in Accounting, or Accounting with another subject, at undergraduate and master's levels.\" (D1, 1.1)"
statedSubjects:
  - { name: "Accounting", locator: "(D1, title; 1.1)", kind: "subject", codes: [{ scheme: "hecos", code: "100105", label: "accounting" }, { scheme: "cah", code: "CAH17-01-08", label: "accounting" }] }
  - { name: "Accountancy", locator: "(D1, 1.1)", kind: "programme title", codes: [{ scheme: "hecos", code: "100104", label: "accountancy" }] }
  - { name: "Accounting and Finance", locator: "(D1, 1.1; 1.2)", kind: "programme title", codes: [{ scheme: "hecos", code: "100105", label: "accounting" }, { scheme: "hecos", code: "100107", label: "finance" }] }
  - { name: "Accounting and Financial Management", locator: "(D1, 1.1)", kind: "programme title", codes: [{ scheme: "hecos", code: "100105", label: "accounting" }, { scheme: "hecos", code: "100832", label: "financial management" }] }
  - { name: "Accounting and Data Analytics", locator: "(D1, 1.1)", kind: "programme title", codes: [{ scheme: "hecos", code: "100105", label: "accounting" }] }
  - { name: "Accounting and Business Analysis", locator: "(D1, 1.1)", kind: "programme title", codes: [{ scheme: "hecos", code: "100105", label: "accounting" }] }
  - { name: "Accounting and Sustainability", locator: "(D1, 1.1)", kind: "programme title", codes: [{ scheme: "hecos", code: "100105", label: "accounting" }] }
  - { name: "Audit and assurance", locator: "(D1, 3.10 h)", kind: "specialism", codes: [{ scheme: "hecos", code: "100840", label: "audit management" }] }
  - { name: "Taxation", locator: "(D1, 3.10 i)", kind: "specialism", codes: [{ scheme: "hecos", code: "100831", label: "taxation" }] }
  - { name: "strategic management accounting", locator: "(D1, 3.10 e)", kind: "specialism", codes: [{ scheme: "hecos", code: "100836", label: "management accountancy" }] }
  - { name: "sustainability accounting, carbon accounting, forensic accounting, data analytics", locator: "(D1, 1.16 a)", kind: "specialism", codes: [] }
subjects: see front matter (subjectScope subjects)
```

### S3 Structure
<!-- label: both; status: drafted; basis: primary -->
```yaml
components:
  - { number: "1.1", order: 3, componentType: paragraph, parent: "section 1", heading: "Context and purposes of an Accounting degree", gloss: "purpose of the statement; typical course titles" }
  - { number: "1.2", order: 4, componentType: paragraph, parent: "section 1", heading: "Context and purposes of an Accounting degree", gloss: "finance content; joint Accounting and finance" }
  - { number: "1.3", order: 5, componentType: paragraph, parent: "section 1", heading: "Context and purposes of an Accounting degree", gloss: "Accounting in joint honours" }
  - { number: "1.4", order: 6, componentType: paragraph, parent: "section 1", heading: "Purposes and characteristics of an Accounting degree", gloss: "purpose: accounting in society and governance" }
  - { number: "1.5", order: 7, componentType: paragraph, parent: "section 1", heading: "Purposes and characteristics of an Accounting degree", gloss: "students study for different reasons" }
  - { number: "1.6", order: 8, componentType: paragraph, parent: "section 1", heading: "Purposes and characteristics of an Accounting degree", gloss: "accounting systems and the social sciences" }
  - { number: "1.7", order: 9, componentType: paragraph, parent: "section 1", heading: "Purposes and characteristics of an Accounting degree", gloss: "the contested space between academy and PSRBs" }
  - { number: "1.8", order: 10, componentType: paragraph, parent: "section 1", heading: "Purposes and characteristics of an Accounting degree", gloss: "technical focus at the cost of breadth falls short" }
  - { number: "1.9", order: 11, componentType: paragraph, parent: "section 1", heading: "Purposes and characteristics of an Accounting degree", gloss: "preparing for a changing future" }
  - { number: "1.10", order: 12, componentType: paragraph, parent: "section 1", heading: "Purposes and characteristics of an Accounting degree", gloss: "judgement under uncertainty at the core" }
  - { number: "1.11", order: 13, componentType: paragraph, parent: "section 1", heading: "Purposes and characteristics of an Accounting degree", gloss: "systems that provide data and information" }
  - { number: "1.12", order: 14, componentType: paragraph, parent: "section 1", heading: "Purposes and characteristics of an Accounting degree", gloss: "automation and AI raise the bar for thinking" }
  - { number: "1.13", order: 15, componentType: paragraph, parent: "section 1", heading: "Purposes and characteristics of an Accounting degree", gloss: "critique of the status quo; other futures" }
  - { number: "1.14", order: 16, componentType: paragraph, parent: "section 1", heading: "Purposes and characteristics of an Accounting degree", gloss: "conceptual and applied study as a minimum" }
  - { number: "1.15", order: 17, componentType: paragraph, parent: "section 1", heading: "Purposes and characteristics of an Accounting degree", gloss: "apprenticeship degrees judged alike" }
  - { number: "1.16", order: 18, componentType: stem, parent: "section 1", heading: "Purposes and characteristics of an Accounting degree", gloss: "four master's types (a to d)" }
  - { number: "1.17", order: 19, componentType: paragraph, parent: "section 1", heading: "Purposes and characteristics of an Accounting degree", gloss: "self-directed research in every master's" }
  - { number: "1.18", order: 20, componentType: paragraph, parent: "section 1", heading: "Purposes and characteristics of an Accounting degree", gloss: "the integrated master's" }
  - { number: "1.19", order: 21, componentType: paragraph, parent: "section 1", heading: "Equality, diversity and inclusion", gloss: "EDI defined; embedded everywhere" }
  - { number: "1.20", order: 22, componentType: paragraph, parent: "section 1", heading: "Equality, diversity and inclusion", gloss: "principles for an inclusive community" }
  - { number: "1.21", order: 23, componentType: paragraph, parent: "section 1", heading: "Equality, diversity and inclusion", gloss: "EDI, the SDGs and reporting" }
  - { number: "1.22", order: 24, componentType: paragraph, parent: "section 1", heading: "Equality, diversity and inclusion", gloss: "diverse content and critique" }
  - { number: "1.23", order: 25, componentType: stem, parent: "section 1", heading: "Equality, diversity and inclusion", gloss: "examples of diversifying content" }
  - { number: "1.24", order: 26, componentType: stem, parent: "section 1", heading: "Equality, diversity and inclusion", gloss: "EDI by area of content" }
  - { number: "1.25", order: 27, componentType: paragraph, parent: "section 1", heading: "Equality, diversity and inclusion", gloss: "inclusive design and assessment" }
  - { number: "1.26", order: 28, componentType: paragraph, parent: "section 1", heading: "Equality, diversity and inclusion", gloss: "inclusive pedagogies" }
  - { number: "1.27", order: 29, componentType: paragraph, parent: "section 1", heading: "Equality, diversity and inclusion", gloss: "institutional EDI support" }
  - { number: "1.28", order: 30, componentType: paragraph, parent: "section 1", heading: "Equality, diversity and inclusion", gloss: "monitoring EDI" }
  - { number: "1.29", order: 31, componentType: paragraph, parent: "section 1", heading: "Accessibility and the needs of disabled students", gloss: "widening access; anticipating needs" }
  - { number: "1.30", order: 32, componentType: stem, parent: "section 1", heading: "Accessibility and the needs of disabled students", gloss: "accessibility requirements and practices" }
  - { number: "1.31", order: 33, componentType: paragraph, parent: "section 1", heading: "Accessibility and the needs of disabled students", gloss: "proactive design; attainment gaps" }
  - { number: "1.32", order: 34, componentType: paragraph, parent: "section 1", heading: "Accessibility and the needs of disabled students", gloss: "equal access to placements and activities" }
  - { number: "1.33", order: 35, componentType: paragraph, parent: "section 1", heading: "Education for sustainable development", gloss: "sustainability in its broad sense" }
  - { number: "1.34", order: 36, componentType: paragraph, parent: "section 1", heading: "Education for sustainable development", gloss: "accounting for a sustainable transition" }
  - { number: "1.35", order: 37, componentType: paragraph, parent: "section 1", heading: "Education for sustainable development", gloss: "accounting as catalyst for change" }
  - { number: "1.36", order: 38, componentType: paragraph, parent: "section 1", heading: "Education for sustainable development", gloss: "graduate knowledge for sustainable development" }
  - { number: "1.37", order: 39, componentType: paragraph, parent: "section 1", heading: "Education for sustainable development", gloss: "ethical responsibility in how one accounts" }
  - { number: "1.38", order: 40, componentType: paragraph, parent: "section 1", heading: "Education for sustainable development", gloss: "leading the sustainability agenda" }
  - { number: "1.39", order: 41, componentType: paragraph, parent: "section 1", heading: "Education for sustainable development", gloss: "accounting as performative practice" }
  - { number: "1.40", order: 42, componentType: paragraph, parent: "section 1", heading: "Education for sustainable development", gloss: "current sustainability priorities" }
  - { number: "1.41", order: 43, componentType: paragraph, parent: "section 1", heading: "Education for sustainable development", gloss: "sustainability data in systems" }
  - { number: "1.42", order: 44, componentType: paragraph, parent: "section 1", heading: "Education for sustainable development", gloss: "critical enquiry on planetary limits" }
  - { number: "1.43", order: 45, componentType: paragraph, parent: "section 1", heading: "Education for sustainable development", gloss: "sustainability throughout the curriculum" }
  - { number: "1.44", order: 46, componentType: paragraph, parent: "section 1", heading: "Employability, enterprise and entrepreneurship education", gloss: "enterprise and entrepreneurship defined" }
  - { number: "1.45", order: 47, componentType: paragraph, parent: "section 1", heading: "Employability, enterprise and entrepreneurship education", gloss: "critical thinkers who act on ideas" }
  - { number: "1.46", order: 48, componentType: paragraph, parent: "section 1", heading: "Employability, enterprise and entrepreneurship education", gloss: "enterprise skills through core content" }
  - { number: "1.47", order: 49, componentType: paragraph, parent: "section 1", heading: "Employability, enterprise and entrepreneurship education", gloss: "experiential approaches to enterprise" }
  - { number: "1.48", order: 50, componentType: paragraph, parent: "section 1", heading: "Employability, enterprise and entrepreneurship education", gloss: "co-creating enterprise curricula" }
  - { number: "1.49", order: 51, componentType: paragraph, parent: "section 1", heading: "Generative artificial intelligence", gloss: "GenAI defined; five areas of impact" }
  - { number: "1.50", order: 52, componentType: paragraph, parent: "section 1", heading: "Generative artificial intelligence", gloss: "automation raises the value of judgement" }
  - { number: "1.51", order: 53, componentType: paragraph, parent: "section 1", heading: "Generative artificial intelligence", gloss: "GenAI in practice and skills" }
  - { number: "1.52", order: 54, componentType: paragraph, parent: "section 1", heading: "Generative artificial intelligence", gloss: "bias in AI" }
  - { number: "1.53", order: 55, componentType: paragraph, parent: "section 1", heading: "Generative artificial intelligence", gloss: "GenAI for learning" }
  - { number: "1.54", order: 56, componentType: paragraph, parent: "section 1", heading: "Generative artificial intelligence", gloss: "GenAI and assessment design" }
  - { number: "1.55", order: 57, componentType: paragraph, parent: "section 1", heading: "Generative artificial intelligence", gloss: "integrity policies for GenAI" }
  - { number: "2.1", order: 59, componentType: paragraph, parent: "section 2", heading: "Design", gloss: "design aims" }
  - { number: "2.2", order: 60, componentType: paragraph, parent: "section 2", heading: "Design", gloss: "objectives aligned to section 3" }
  - { number: "2.3", order: 61, componentType: paragraph, parent: "section 2", heading: "Design", gloss: "higher-order skills and lifelong learning" }
  - { number: "2.4", order: 62, componentType: paragraph, parent: "section 2", heading: "Design", gloss: "many career routes" }
  - { number: "2.5", order: 63, componentType: paragraph, parent: "section 2", heading: "Design", gloss: "accreditation not at the cost of breadth" }
  - { number: "2.6", order: 64, componentType: paragraph, parent: "section 2", heading: "Design", gloss: "coverage in joint degrees" }
  - { number: "2.7", order: 65, componentType: paragraph, parent: "section 2", heading: "Progression", gloss: "progressive attainment through levels" }
  - { number: "2.8", order: 66, componentType: paragraph, parent: "section 2", heading: "Progression", gloss: "prerequisites and credit" }
  - { number: "2.9", order: 67, componentType: paragraph, parent: "section 2", heading: "Progression", gloss: "typical length by nation" }
  - { number: "2.10", order: 68, componentType: paragraph, parent: "section 2", heading: "Progression", gloss: "joint honours progression" }
  - { number: "2.11", order: 69, componentType: paragraph, parent: "section 2", heading: "Progression", gloss: "progression and individual needs" }
  - { number: "2.12", order: 70, componentType: paragraph, parent: "section 2", heading: "Progression", gloss: "honours as a basis for careers" }
  - { number: "2.13", order: 71, componentType: paragraph, parent: "section 2", heading: "Progression", gloss: "readiness for postgraduate study" }
  - { number: "2.14", order: 72, componentType: paragraph, parent: "section 2", heading: "Progression", gloss: "degree apprenticeship progression" }
  - { number: "2.15", order: 73, componentType: paragraph, parent: "section 2", heading: "Progression", gloss: "exit awards" }
  - { number: "2.16", order: 74, componentType: paragraph, parent: "section 2", heading: "Flexibility", gloss: "adaptable courses" }
  - { number: "2.17", order: 75, componentType: paragraph, parent: "section 2", heading: "Flexibility", gloss: "inclusive flexibility of mode" }
  - { number: "2.18", order: 76, componentType: paragraph, parent: "section 2", heading: "Flexibility", gloss: "options and micro-credentials" }
  - { number: "2.19", order: 77, componentType: paragraph, parent: "section 2", heading: "Flexibility", gloss: "multiple learning modes" }
  - { number: "2.20", order: 78, componentType: paragraph, parent: "section 2", heading: "Flexibility", gloss: "flexible assessment for EDI" }
  - { number: "2.21", order: 79, componentType: paragraph, parent: "section 2", heading: "Flexibility", gloss: "coherence within flexibility" }
  - { number: "2.22", order: 80, componentType: paragraph, parent: "section 2", heading: "Flexibility", gloss: "partnership as flexibility" }
  - { number: "2.23", order: 81, componentType: paragraph, parent: "section 2", heading: "Partnership", gloss: "standards across partnerships" }
  - { number: "2.24", order: 82, componentType: stem, parent: "section 2", heading: "Partnership", gloss: "examples of partnership" }
  - { number: "2.25", order: 83, componentType: paragraph, parent: "section 2", heading: "Partnership", gloss: "strategic and structural partnerships" }
  - { number: "2.26", order: 84, componentType: paragraph, parent: "section 2", heading: "Partnership", gloss: "PSRBs as partners" }
  - { number: "2.27", order: 85, componentType: paragraph, parent: "section 2", heading: "Partnership", gloss: "networks and learned societies" }
  - { number: "2.28", order: 86, componentType: paragraph, parent: "section 2", heading: "Monitoring and review", gloss: "external reference points in review" }
  - { number: "2.29", order: 87, componentType: paragraph, parent: "section 2", heading: "Monitoring and review", gloss: "externality" }
  - { number: "2.30", order: 88, componentType: paragraph, parent: "section 2", heading: "Monitoring and review", gloss: "advisory boards" }
  - { number: "2.31", order: 89, componentType: paragraph, parent: "section 2", heading: "Monitoring and review", gloss: "monitoring the themes" }
  - { number: "2.32", order: 90, componentType: paragraph, parent: "section 2", heading: "Monitoring and review", gloss: "external examining" }
  - { number: "2.33", order: 91, componentType: paragraph, parent: "section 2", heading: "Monitoring and review", gloss: "PSRB monitoring; informing students" }
  - { number: "3.1", order: 93, componentType: paragraph, parent: "section 3", heading: "Content, structure and delivery", gloss: "courses map the areas to modules" }
  - { number: "3.2", order: 94, componentType: paragraph, parent: "section 3", heading: "Knowledge, understanding and subject-specific skills", gloss: "content follows section 1" }
  - { number: "3.3", order: 95, componentType: paragraph, parent: "section 3", heading: "Knowledge, understanding and subject-specific skills", gloss: "public interest role" }
  - { number: "3.4", order: 96, componentType: paragraph, parent: "section 3", heading: "Knowledge, understanding and subject-specific skills", gloss: "critical, social science grounding" }
  - { number: "3.5", order: 97, componentType: paragraph, parent: "section 3", heading: "Knowledge, understanding and subject-specific skills", gloss: "many kinds of organisation" }
  - { number: "3.6", order: 98, componentType: paragraph, parent: "section 3", heading: "Knowledge, understanding and subject-specific skills", gloss: "conceptual and applied" }
  - { number: "3.7", order: 99, componentType: paragraph, parent: "section 3", heading: "Knowledge, understanding and subject-specific skills", gloss: "why rules exist and their critique" }
  - { number: "3.8", order: 100, componentType: paragraph, parent: "section 3", heading: "Knowledge, understanding and subject-specific skills", gloss: "beyond numbers" }
  - { number: "3.9", order: 101, componentType: area, parent: "section 3", heading: "Knowledge, understanding and subject-specific skills", gloss: "core accounting-specific skills" }
  - { number: "3.10", order: 102, componentType: area, parent: "section 3", heading: "Knowledge, understanding and subject-specific skills", gloss: "twelve broad areas of knowledge (a to l)" }
  - { number: "3.11", order: 103, componentType: paragraph, parent: "section 3", heading: "Knowledge, understanding and subject-specific skills", gloss: "optional modules" }
  - { number: "3.12", order: 104, componentType: paragraph, parent: "section 3", heading: "Transferable, professional and practice skills", gloss: "skills follow section 1" }
  - { number: "3.13", order: 105, componentType: paragraph, parent: "section 3", heading: "Transferable, professional and practice skills", gloss: "skills that put knowledge to work" }
  - { number: "3.14", order: 106, componentType: paragraph, parent: "section 3", heading: "Transferable, professional and practice skills", gloss: "skills used together; where subject skills sit" }
  - { number: "3.15", order: 107, componentType: area, parent: "section 3", heading: "Transferable, professional and practice skills", gloss: "twelve graduate skills (m to x)" }
  - { number: "3.16", order: 108, componentType: paragraph, parent: "section 3", heading: "Learning and teaching", gloss: "learning and teaching strategy" }
  - { number: "3.17", order: 109, componentType: paragraph, parent: "section 3", heading: "Learning and teaching", gloss: "alignment and balance" }
  - { number: "3.18", order: 110, componentType: paragraph, parent: "section 3", heading: "Learning and teaching", gloss: "employability and citizenship" }
  - { number: "3.19", order: 111, componentType: practice, parent: "section 3", heading: "Learning and teaching", gloss: "pedagogies for deep learning" }
  - { number: "3.20", order: 112, componentType: practice, parent: "section 3", heading: "Learning and teaching", gloss: "varied, active approaches" }
  - { number: "3.21", order: 113, componentType: practice, parent: "section 3", heading: "Learning and teaching", gloss: "innovative methods" }
  - { number: "3.22", order: 114, componentType: practice, parent: "section 3", heading: "Learning and teaching", gloss: "digital technologies in teaching" }
  - { number: "3.23", order: 115, componentType: paragraph, parent: "section 3", heading: "Learning and teaching", gloss: "inclusive, accessible teaching" }
  - { number: "3.24", order: 116, componentType: paragraph, parent: "section 3", heading: "Learning and teaching", gloss: "research and practice in teaching" }
  - { number: "3.25", order: 117, componentType: paragraph, parent: "section 3", heading: "Learning and teaching", gloss: "responsive strategy; staff development" }
  - { number: "3.26", order: 118, componentType: paragraph, parent: "section 3", heading: "Learning and teaching", gloss: "reviewing teaching" }
  - { number: "3.27", order: 119, componentType: paragraph, parent: "section 3", heading: "Assessment", gloss: "robust summative assessment" }
  - { number: "3.28", order: 120, componentType: practice, parent: "section 3", heading: "Assessment", gloss: "formative assessment" }
  - { number: "3.29", order: 121, componentType: paragraph, parent: "section 3", heading: "Assessment", gloss: "balanced portfolio" }
  - { number: "3.30", order: 122, componentType: paragraph, parent: "section 3", heading: "Assessment", gloss: "no avoiding critical elements" }
  - { number: "3.31", order: 123, componentType: practice, parent: "section 3", heading: "Assessment", gloss: "depth, not rote" }
  - { number: "3.32", order: 124, componentType: paragraph, parent: "section 3", heading: "Assessment", gloss: "assessment for independent learners" }
  - { number: "3.33", order: 125, componentType: paragraph, parent: "section 3", heading: "Assessment", gloss: "inclusive assessment" }
  - { number: "3.34", order: 126, componentType: practice, parent: "section 3", heading: "Assessment", gloss: "assessment as dialogue" }
  - { number: "3.35", order: 127, componentType: paragraph, parent: "section 3", heading: "Assessment", gloss: "clear schemes and workload" }
  - { number: "3.36", order: 128, componentType: paragraph, parent: "section 3", heading: "Assessment", gloss: "timely criteria and rubrics" }
  - { number: "3.37", order: 129, componentType: practice, parent: "section 3", heading: "Assessment", gloss: "typical assessment methods" }
  - { number: "3.38", order: 130, componentType: paragraph, parent: "section 3", heading: "Assessment", gloss: "individual or group modes" }
  - { number: "3.39", order: 131, componentType: practice, parent: "section 3", heading: "Assessment", gloss: "fair group assessment" }
  - { number: "3.40", order: 132, componentType: paragraph, parent: "section 3", heading: "Assessment", gloss: "synchronous and asynchronous assessment" }
  - { number: "3.41", order: 133, componentType: practice, parent: "section 3", heading: "Assessment", gloss: "peer assessment safeguards" }
  - { number: "3.42", order: 134, componentType: paragraph, parent: "section 3", heading: "Assessment", gloss: "GenAI and assessment" }
  - { number: "3.43", order: 135, componentType: paragraph, parent: "section 3", heading: "Assessment", gloss: "GenAI policies communicated" }
  - { number: "4.1", order: 137, componentType: paragraph, parent: "section 4", heading: "Introduction", gloss: "what the standards set out" }
  - { number: "4.2", order: 138, componentType: paragraph, parent: "section 4", heading: "Introduction", gloss: "not competence standards" }
  - { number: "4.3", order: 139, componentType: stem, parent: "section 4", heading: "Undergraduate awards", gloss: "four levels and their classes" }
  - { number: "4.4", order: 140, componentType: paragraph, parent: "section 4", heading: "Undergraduate awards", gloss: "most exceed the threshold" }
  - { number: "4.5", order: 141, componentType: paragraph, parent: "section 4", heading: "Undergraduate awards", gloss: "Table 1: honours standards by level" }
  - { number: "4.6", order: 142, componentType: paragraph, parent: "section 4", heading: "Master's awards", gloss: "basis of the master's standards" }
  - { number: "4.7", order: 143, componentType: paragraph, parent: "section 4", heading: "Master's awards", gloss: "Table 2: master's types and standards" }
  - { number: "4.8", order: 144, componentType: paragraph, parent: "section 4", heading: "Master's awards", gloss: "master's classifications left to institutions; Table 2 follows" }
  - { number: "1", componentType: section, parent: none, heading: "Context and purposes of an Accounting degree", gloss: "section 1" }
  - { number: "2", componentType: section, parent: none, heading: "Distinctive features of the Accounting degree", gloss: "section 2" }
  - { number: "3", componentType: section, parent: none, heading: "Content, structure and delivery", gloss: "section 3" }
  - { number: "4", componentType: section, parent: none, heading: "Benchmark Standards", gloss: "section 4" }
excluded:
  - { number: "none", heading: "About this Statement; How can I use this document?; Relationship to legislation; Additional sector reference points", kind: "other: front matter, read for S1, S2 and SB6" }
  - { number: "none", heading: "section heading lines 1 to 4", kind: "other: headings, recorded in SECTIONS" }
  - { number: "5", heading: "List of references and further resources", kind: "other: back matter, read for SB6 shared documents" }
  - { number: "6", heading: "Membership of the Advisory Group", kind: "other: back matter, read for S8 (earlier editions 2019, 2014, 2007, 2000)" }
  - { number: "7", heading: "Appendices", kind: "other: back matter, read for SB5 (Appendix 1 PSRBs) and SB6 (Appendix 2 learned societies)" }
```

### S4 Statements
<!-- label: both; status: drafted; basis: primary. Only standards (D-std-0002 (a)): 178 records. `source` is the issuer's statement exactly as its span holds it (D-std-0014). -->
```yaml
- id: qaa/accounting-2025/1.2
  locator: { number: "1.2", headingPath: ["Context and purposes of an Accounting degree", "Context and purposes of an Accounting degree"] }
  span: { start: 8640, end: 9411 }
  source: "1.2 Most undergraduate degree programmes with substantial Accounting content also include some finance. This Subject Benchmark Statement also covers Accounting programmes that include a significant proportion of finance. It does not, however, cover single honours degrees in finance or the finance content of such degrees: these are covered by the Subject Benchmark Statement for Finance . Joint degree programmes in Accounting and finance should be aligned with significant content from both the Accounting and Finance Subject Benchmark Statements, and must include conceptual accounting issues, accounting theory, accountability, sustainability, non-business uses of accounting, the applied aspects of accounting and the development of higher-level intellectual skills."
  stem: none
  statementType: requirement
  rung: none
  force: must
  level: fheq:6
  appliesTo: "joint Accounting and finance courses"
  addressee: provider
  verbs: ["aligned", "include"]
  about: "joint Accounting and finance courses"
  themes: [none]
  domain: none
  award: ["bachelor's with honours"]
  gradeOf: none
  paraphrase: "Courses with a large finance element fall within this statement, single honours finance does not (the Finance statement covers it); a joint Accounting and finance course should draw substantially on both statements and must cover conceptual issues and theory in accounting, accountability, sustainability, uses of accounting outside business, its applied side and higher-order thinking."
  quote: full   # the issuer's statement is in `source` (D-std-0014)
  audience: practitioner
  subjects: inherited
- id: qaa/accounting-2025/1.3
  locator: { number: "1.3", headingPath: ["Context and purposes of an Accounting degree", "Context and purposes of an Accounting degree"] }
  span: { start: 9412, end: 10148 }
  source: "1.3 Accounting can be studied as part of a joint undergraduate deg ree programme in combination with related (for example, management, economics, business, computer science, mathematics, statistics or law) or unrelated disciplines (for example, modern language, drama, or hospitality). In such cases, this Subject Benchmark Statement should be applied in conjunction with others relating to the joint course. In the case of joint degree programmes, the scope, depth and balance of concepts and application should not result in a neglect of the conceptual accounting issues, accounting theory, accountability, sustainability, non-business uses, or the applied aspects of accounting or the development of higher-level intellectual skills."
  stem: none
  statementType: requirement
  rung: none
  force: should
  level: fheq:6
  appliesTo: "joint honours courses that include Accounting"
  addressee: provider
  verbs: ["applied"]
  about: "Accounting within joint honours with other subjects"
  themes: [none]
  domain: none
  award: ["bachelor's with honours"]
  gradeOf: none
  paraphrase: "Where Accounting is joined with a related or an unrelated subject, this statement should be used together with the other subject's statement, and the mix should not squeeze out accounting concepts, theory, accountability, sustainability, non-business uses, application or higher-order thinking."
  quote: full   # the issuer's statement is in `source` (D-std-0014)
  audience: practitioner
  subjects: inherited
- id: qaa/accounting-2025/1.4
  locator: { number: "1.4", headingPath: ["Context and purposes of an Accounting degree", "Purposes and characteristics of an Accounting degree"] }
  span: { start: 10202, end: 11724 }
  source: "1.4 The purpose of an Accounting degree is to educate students to enable them to understand the role of accounting in its socioeconomic context and to understand the role of accounting and accountants in responsible governance (including assurance and audit), thereby providing a sound foundation for a range of careers. This involves an education that aims to develop responsible citizens and ethical professionals. In this context, all Accounting degrees should go beyond considering a focus on profit and the measurement and accumulation of capital. Accounting degrees need to reflect the broad role of accountability for sustainability, welfare and a range of social, environmental, political and other perspectives, recognising that accounting is a key form of information provision and control within and of many types of organisations, including governmental organisations (at many levels), charities, not-for-profits, co-operatives, social enterprises, political, social pressure movements, as well as for-profit businesses and professional organisations. Accounting degrees need to consider the uses and potential uses of a broad range of stakeholders, both within and external to organisations, including the use of accounting-based data, information and concepts for the purposes of economic, social and political argument, and in making business, social and legal cases for change. An Accounting degree should reflect foundational and contemporary research and debate relevant to accounting and accountability."
  stem: none
  statementType: expectation
  rung: none
  force: should
  level: none
  appliesTo: "Accounting courses and their students"
  addressee: both
  verbs: ["educate", "understand", "reflect", "consider"]
  about: "the purpose of an Accounting degree"
  themes: [none]
  domain: understanding
  award: ["none"]
  gradeOf: none
  paraphrase: "An Accounting degree should prepare students to understand accounting in its social and economic setting and its part in responsible governance, audit and assurance, as a base for many careers and for ethical citizenship; it should look past profit and capital to accountability for sustainability and welfare, to the many kinds of organisation and stakeholder that use accounting, and to past and current research."
  quote: full   # the issuer's statement is in `source` (D-std-0014)
  audience: both
  subjects: inherited
- id: qaa/accounting-2025/1.5
  locator: { number: "1.5", headingPath: ["Context and purposes of an Accounting degree", "Purposes and characteristics of an Accounting degree"] }
  span: { start: 11725, end: 12387 }
  source: "1.5 The need for Accounting degrees to cover such a broad range of perspectives is because Accounting degrees should be designed to meet the intellectual and knowledge needs of students studying Accounting for a variety of reasons. For example, some students\n\n4\nmay intend to pursue a professional accountancy qualification while others see accounting as a useful introduction to business enterprise (for example, finance, commerce, services, manufacturing), government, public and not-for profit sectors or education. Students may also study Accounting as a way of understanding accounting for broader social purposes or as a predominantly intellectual pursuit."
  stem: none
  statementType: requirement
  rung: none
  force: should
  level: none
  appliesTo: "Accounting courses"
  addressee: provider
  verbs: ["designed", "meet"]
  about: "designing for students with different aims"
  themes: [none]
  domain: none
  award: ["none"]
  gradeOf: none
  paraphrase: "Accounting degrees should be built to serve students who come to them for different reasons: a professional qualification, a route into business, government or other sectors, a wider social interest or the intellectual pursuit itself."
  quote: full   # the issuer's statement is in `source` (D-std-0014)
  audience: practitioner
  subjects: inherited
- id: qaa/accounting-2025/1.6
  locator: { number: "1.6", headingPath: ["Context and purposes of an Accounting degree", "Purposes and characteristics of an Accounting degree"] }
  span: { start: 12388, end: 13187 }
  source: "1.6 Accounting as a degree subject requires students to study how the design, operation and validation of accounting systems affect, and are affected by, the development of accounting theory, individuals, organisations, information technologies, markets, society and the environment. This study should be informed by perspectives from the social sciences. Such perspectives may be derived from, but are not restricted to, disciplines such as economics, information systems, politics, psychology and sociology. Accounting degree programmes normally include elements of finance; this requires the study of the operation and design of financial systems, risk, financial structures, and financial instruments. The extent of coverage of finance depends on the nature of the programme (see paragraph 1.2)."
  stem: none
  statementType: expectation
  rung: none
  force: should
  level: none
  appliesTo: "Accounting courses and their students"
  addressee: both
  verbs: ["study", "informed"]
  about: "accounting systems and the social sciences"
  themes: [none]
  domain: understanding
  award: ["none"]
  gradeOf: none
  paraphrase: "Students study how accounting systems shape and are shaped by theory, people, organisations, technology, markets, society and the environment; that study should draw on social science perspectives, for example politics, sociology, psychology, economics and information systems, with finance covered as the course's nature requires."
  quote: full   # the issuer's statement is in `source` (D-std-0014)
  audience: both
  subjects: inherited
- id: qaa/accounting-2025/1.8
  locator: { number: "1.8", headingPath: ["Context and purposes of an Accounting degree", "Purposes and characteristics of an Accounting degree"] }
  span: { start: 14118, end: 14758 }
  source: "1.8 The contested space in which Accounting degrees sit includes a number of interest groups, including higher education, potential employers, the professional accounting bodies and the overall financial regulatory bodies, as well as students and parents. The nature of the tensions in this space could lead to a focus on technical and non-critical accounting content (Ellington and Williams, 2017; Ballantine, Boyce and Stoner, 2024). Degrees that do this at the expense of the broader intellectual, social and environmental needs of Accounting outlined in this Statement do not meet the specifications in this Subject Benchmark Statement."
  stem: none
  statementType: requirement
  rung: none
  force: threshold
  level: none
  appliesTo: "Accounting courses"
  addressee: provider
  verbs: ["meet"]
  about: "technical, non-critical content at the expense of breadth"
  themes: [none]
  domain: none
  award: ["none"]
  gradeOf: none
  paraphrase: "Pressures from employers, professional bodies, regulators and others can push courses towards technical, uncritical accounting; a degree that does so at the cost of the broader intellectual, social and environmental needs the statement sets out falls short of it."
  quote: full   # the issuer's statement is in `source` (D-std-0014)
  audience: practitioner
  subjects: inherited
- id: qaa/accounting-2025/1.9
  locator: { number: "1.9", headingPath: ["Context and purposes of an Accounting degree", "Purposes and characteristics of an Accounting degree"] }
  span: { start: 14759, end: 15509 }
  source: "1.9 An Accounting degree should prepare students to deal with a dynamic future, in which technical standards and practices are likely to change radically or evolve within a lifetime career. Consequently, an Accounting degree that focuses primarily on technical content will not be sufficient to meet this Subject Benchmark Statement. Additionally, while covering the skills, knowledge and ability to apply current regulatory frameworks and standards is an important element of any Accounting degree, the development of graduates with lifelong and self-directed learning, professional, transferable (soft) and critical skills is therefore important (Gebreiter, 2022), both as an element of any degree and to make graduates employable in the long term."
  stem: none
  statementType: expectation
  rung: none
  force: should
  level: none
  appliesTo: "Accounting courses and their students"
  addressee: both
  verbs: ["prepare", "deal"]
  about: "preparing for a changing profession"
  themes: [none]
  domain: none
  award: ["none"]
  gradeOf: none
  paraphrase: "An Accounting degree should ready students for a future in which standards and practice may change radically within a career, so a mainly technical degree is not enough; alongside current regulation and standards it should build lifelong, self-directed learning and professional, transferable and critical skills."
  quote: full   # the issuer's statement is in `source` (D-std-0014)
  audience: both
  subjects: inherited
- id: qaa/accounting-2025/1.11
  locator: { number: "1.11", headingPath: ["Context and purposes of an Accounting degree", "Purposes and characteristics of an Accounting degree"] }
  span: { start: 16044, end: 16900 }
  source: "1.11 An Accounting degree programme should prepare students to understand the design and operation of systems to provide data and information. This requires both an understanding of the process of traditional accounting (including double entry bookkeeping and the preparation of accounting statements) and of broader business systems that can deal with non-financial and additional financial data, including that required or helpful in fulfilling the broader accountability for sustainability, social reporting and regulatory compliance. This also requires students to understand, interrogate, analyse and evaluate both structured and unstructured data, including an understanding of data structures (including those in relational databases, enterprise resource planning (ERP) and other organisational systems) containing complex organisational attributes."
  stem: none
  statementType: expectation
  rung: none
  force: should
  level: none
  appliesTo: "Accounting courses and their students"
  addressee: both
  verbs: ["prepare", "understand", "interrogate", "analyse", "evaluate"]
  about: "systems that provide data and information"
  themes: [none]
  domain: subject-skill
  award: ["none"]
  gradeOf: none
  paraphrase: "An Accounting degree should prepare students to understand how systems that provide data and information are designed and run: traditional double-entry bookkeeping and the preparation of statements, wider business systems for non-financial and further financial data (for sustainability, social reporting and compliance), and the analysis and evaluation of structured and unstructured data and the structures that hold it."
  quote: full   # the issuer's statement is in `source` (D-std-0014)
  audience: both
  subjects: inherited
- id: qaa/accounting-2025/1.13
  locator: { number: "1.13", headingPath: ["Context and purposes of an Accounting degree", "Purposes and characteristics of an Accounting degree"] }
  span: { start: 17376, end: 18114 }
  source: "1.13 Accounting degree programmes need to enable students to develop the knowledge, skills and confidence to be critical of the status quo in accounting, and to think about and advise on alternative modes of accounting and business organisation, considering the public interest and the common good. This needs to include engendering students to imagine futures for accounting that are different to those that are currently considered mainstream, of which accounting for sustainability is an important element. Accounting degree programmes should not be just about what accounting is today: they need to prepare students for an uncertain future, including the ability to conceive solutions to problems that society may not have recognised."
  stem: none
  statementType: expectation
  rung: none
  force: should
  level: none
  appliesTo: "Accounting courses and their students"
  addressee: both
  verbs: ["enable", "develop", "imagine", "prepare"]
  about: "critique of the status quo and other futures for accounting"
  themes: [none]
  domain: understanding
  award: ["none"]
  gradeOf: none
  paraphrase: "Courses need to give students the knowledge, skills and confidence to criticise current accounting, to propose other ways of accounting and organising business in the public interest, and to imagine futures for accounting, sustainability accounting among them; they should not be confined to accounting as it now stands."
  quote: full   # the issuer's statement is in `source` (D-std-0014)
  audience: both
  subjects: inherited
- id: qaa/accounting-2025/1.14
  locator: { number: "1.14", headingPath: ["Context and purposes of an Accounting degree", "Purposes and characteristics of an Accounting degree"] }
  span: { start: 18115, end: 18682 }
  source: "1.14 As noted in the preceding paragraphs, the study of Accounting involves the consideration of both conceptual and applied aspects of the subject. The term 'conceptual' here is intended to include theoretical accounting as well as broad social, sustainability, political, economic and other considerations. A degree without a substantive study of these conceptual considerations underlying accounting cannot be considered to meet the minimum requirements of an Accounting degree. Neither can one that completely neglects applied and technical aspects of accounting."
  stem: none
  statementType: requirement
  rung: none
  force: threshold
  level: none
  appliesTo: "Accounting courses"
  addressee: provider
  verbs: ["meet", "neglects"]
  about: "conceptual and applied study as a minimum"
  themes: [none]
  domain: none
  award: ["none"]
  gradeOf: none
  paraphrase: "Accounting is studied in both its conceptual and its applied aspects, conceptual covering accounting theory and broad social, sustainability, political and economic questions; a degree lacking substantial conceptual study does not reach the minimum, and nor does one that wholly leaves out the applied and technical side."
  quote: full   # the issuer's statement is in `source` (D-std-0014)
  audience: practitioner
  subjects: inherited
- id: qaa/accounting-2025/1.15
  locator: { number: "1.15", headingPath: ["Context and purposes of an Accounting degree", "Purposes and characteristics of an Accounting degree"] }
  span: { start: 18683, end: 18767 }
  source: "1.15 Apprenticeship degrees should be judged by the same criteria as outlined above."
  stem: none
  statementType: requirement
  rung: none
  force: should
  level: fheq:6
  appliesTo: "Accounting degree apprenticeships"
  addressee: provider
  verbs: ["judged"]
  about: "degree apprenticeships judged the same way"
  themes: [none]
  domain: none
  award: ["degree apprenticeship"]
  gradeOf: none
  paraphrase: "Apprenticeship degrees should be measured against the same criteria as other Accounting degrees."
  quote: full   # the issuer's statement is in `source` (D-std-0014)
  audience: practitioner
  subjects: inherited
- id: qaa/accounting-2025/1.16.b1
  locator: { number: "1.16.b1", headingPath: ["Context and purposes of an Accounting degree", "Purposes and characteristics of an Accounting degree"] }
  span: { start: 18844, end: 19799 }
  source: "a Advanced or specialist academic Accounting master's degrees involve the advanced theoretical and conceptual study of one or more of the main elements of an honours Accounting degree, sometimes alongside additional specialist subjects in or adjacent to the discipline, such as sustainability accounting, carbon accounting, forensic accounting, data analytics, or specific research specialisms in the field. Students graduating from this type of master's degree in Accounting are expected, in relevant areas, to demonstrate the same high levels of attainment as an undergraduate honours graduate (Table 1 on page 31) along with a range of additional content requirements relevant to the specialist area of the master's degree and the requirement to demonstrate independent self-directed study involving personal inquiry. This type of master's degree would normally require a good honours degree with a major or joint major in Accounting as a prerequisite."
  stem: "1.16"
  statementType: expectation
  rung: none
  force: must   # D-std-0016: "requirements" read as must
  level: fheq:7
  appliesTo: "graduates of an advanced or specialist academic master's"
  addressee: learner
  verbs: ["demonstrate"]
  about: "the advanced or specialist academic master's"
  themes: [none]
  domain: knowledge
  award: ["master's (advanced or specialist)"]
  gradeOf: none
  paraphrase: "Advanced or specialist master's degrees study one or more main parts of an honours Accounting degree at an advanced theoretical level, sometimes with specialist subjects; their graduates are expected to reach honours-level attainment in those areas, meet extra content needs of the specialism and show independent, self-directed inquiry; entry normally needs a good honours degree mainly or jointly in Accounting."
  quote: full   # the issuer's statement is in `source` (D-std-0014)
  audience: both
  subjects: inherited
- id: qaa/accounting-2025/1.16.b2
  locator: { number: "1.16.b2", headingPath: ["Context and purposes of an Accounting degree", "Purposes and characteristics of an Accounting degree"] }
  span: { start: 19800, end: 20832 }
  source: "b Accounting conversion master's degrees are designed to provide the opportunity for students whose first discipline is in an area that does not specialise in accounting, or who have studied elements of accounting in a different jurisdiction, to secure the\n\n6\nessential elements of knowledge, understanding and skills of an honours degree in Accounting and to develop these further, with additional independent synoptic or research achievements at master's level. This type of master's degree should therefore normally be informed by the benchmarks for a good honours degree in Accounting with additional expectations at master's level in relation to further development of at least some topics and the requirement to demonstrate independent self-directed study involving personal inquiry. A good honours degree in a subject other than accounting or equivalent practical experience, would normally be a prerequisite for this type of degree, although some prior achievements in accounting or related studies may also be advantageous."
  stem: "1.16"
  statementType: expectation
  rung: none
  force: should
  level: fheq:7
  appliesTo: "Accounting conversion master's courses"
  addressee: both
  verbs: ["secure", "develop", "informed", "demonstrate"]
  about: "the Accounting conversion master's"
  themes: [none]
  domain: knowledge
  award: ["master's (conversion)"]
  gradeOf: none
  paraphrase: "Conversion master's degrees let students from other disciplines, or who met accounting in another jurisdiction, gain the essentials of an Accounting honours degree and go further at master's level; they should normally be guided by the standards for a good honours degree, with added master's expectations and independent inquiry; entry normally needs a good honours degree in another subject or equivalent experience."
  quote: full   # the issuer's statement is in `source` (D-std-0014)
  audience: both
  subjects: inherited
- id: qaa/accounting-2025/1.16.b3
  locator: { number: "1.16.b3", headingPath: ["Context and purposes of an Accounting degree", "Purposes and characteristics of an Accounting degree"] }
  span: { start: 20833, end: 21898 }
  source: "c Professional master's degrees in Accounting are those degrees designed to provide professional-level knowledge, skills and critical thinking, including ethical and moral judgement and professional scepticism in an applied context, and are relevant for students seeking high levels of professional accreditation and exemptions from PSRBs. This type of master's degree will involve the advanced theoretical and conceptual study of one or more of the main elements of an honours Accounting degree, with a particular focus on high level application. Graduates from this type of master's degree in Accounting would not only be expected to reach the same high levels of attainment as an honours graduate in those areas, but extend them to master's level content requirements relevant to the professional focus of the degree and demonstrate independent self-directed study involving personal inquiry. This type of master's degree would normally require a good honours degree with a major or joint major in Accounting or equivalent practical experience as a prerequisite."
  stem: "1.16"
  statementType: expectation
  rung: none
  force: will
  level: fheq:7
  appliesTo: "professional master's courses in Accounting"
  addressee: both
  verbs: ["involve", "reach", "extend", "demonstrate"]
  about: "the professional master's in Accounting"
  themes: [none]
  domain: subject-skill
  award: ["master's (professional)"]
  gradeOf: none
  paraphrase: "Professional master's degrees give professional-level knowledge, skills and critical thinking, with ethical judgement and scepticism in applied settings, for students seeking accreditation and exemptions; they will involve advanced study of main parts of an honours degree focused on high-level application, and their graduates are expected to reach and then extend honours-level attainment and show independent inquiry."
  quote: full   # the issuer's statement is in `source` (D-std-0014)
  audience: both
  subjects: inherited
- id: qaa/accounting-2025/1.17
  locator: { number: "1.17", headingPath: ["Context and purposes of an Accounting degree", "Purposes and characteristics of an Accounting degree"] }
  span: { start: 22169, end: 22704 }
  source: "1.17 In all cases, master's degree programmes in Accounting should be expected to include a substantial element of self-directed research-based study, involving personal inquiry demonstrating intellectual curiosity into a theoretical area of the discipline or the application of theoretical and conceptual learning to a 'real-world' project or issue of importance. Such projects or issues might be in business or other organisational settings, or based on the environmental, work or social aspects outside of organisational boundaries."
  stem: none
  statementType: expectation
  rung: none
  force: should
  level: fheq:7
  appliesTo: "taught master's courses in Accounting"
  addressee: both
  verbs: ["include"]
  about: "self-directed research-based study at master's level"
  themes: [none]
  domain: subject-skill
  award: ["master's (advanced or specialist)", "master's (conversion)", "master's (professional)", "integrated master's"]
  gradeOf: none
  paraphrase: "Every master's in Accounting should include a substantial piece of self-directed, research-based study, a personal inquiry into theory or into applying theory to a real project or issue, inside organisations or beyond them."
  quote: full   # the issuer's statement is in `source` (D-std-0014)
  audience: both
  subjects: inherited
- id: qaa/accounting-2025/1.18
  locator: { number: "1.18", headingPath: ["Context and purposes of an Accounting degree", "Purposes and characteristics of an Accounting degree"] }
  span: { start: 22705, end: 23337 }
  source: "1.18 Integrated master's degrees in Accounting typically add an extra year of full-time equivalent study to an honours degree in the subject and are expected to include attainment of the benchmark requirements for a good honours degree and to take student achievement beyond those levels to the benchmark requirements for either an advanced or specialist academic master's degree (paragraph 1.16 a), or in some jurisdictions to the more advanced levels of a professional master's degree (paragraph 1.16 c), including the expectation to include a substantial element of self-directed research-based study, involving personal inquiry."
  stem: none
  statementType: expectation
  rung: none
  force: must   # D-std-0016: "are expected to" read as must
  level: fheq:7
  appliesTo: "integrated master's degrees in Accounting"
  addressee: both
  verbs: ["include", "take"]
  about: "the integrated master's in Accounting"
  themes: [none]
  domain: knowledge
  award: ["integrated master's"]
  gradeOf: none
  paraphrase: "Integrated master's degrees usually add a year to the honours degree and are expected to reach the standards for a good honours degree and then those of an advanced or specialist master's, or in some jurisdictions a professional master's, including substantial self-directed research-based inquiry."
  quote: full   # the issuer's statement is in `source` (D-std-0014)
  audience: both
  subjects: inherited
- id: qaa/accounting-2025/1.19
  locator: { number: "1.19", headingPath: ["Context and purposes of an Accounting degree", "Equality, diversity and inclusion"] }
  span: { start: 23372, end: 23963 }
  source: "1.19 Equality, diversity and inclusion (EDI) encompass a wide range of identity characteristics, including, but not limited to, race/ethnicity, gender, sexual orientation, religion and belief, disability, age, and socioeconomic background. It is recognised that there are many forms of difference and that these are, in part, reflected in legal equality duties but go beyond that to recognise intersectionalities across the student and staff population. EDI should be meaningfully embedded within the culture and practice of the accounting discipline and in all Accounting degree programmes."
  stem: none
  statementType: requirement
  rung: none
  force: should
  level: none
  appliesTo: "Accounting courses"
  addressee: provider
  verbs: ["embedded"]
  about: "EDI built into the discipline and every course"
  themes: [theme:edi]
  domain: none
  award: ["none"]
  gradeOf: none
  paraphrase: "EDI spans many identity characteristics and forms of difference, beyond legal equality duties and including intersections across students and staff; it should be built meaningfully into the culture and practice of accounting and into every Accounting degree."
  quote: full   # the issuer's statement is in `source` (D-std-0014)
  audience: practitioner
  subjects: inherited
- id: qaa/accounting-2025/1.20
  locator: { number: "1.20", headingPath: ["Context and purposes of an Accounting degree", "Equality, diversity and inclusion"] }
  span: { start: 23967, end: 24625 }
  source: "1.20 In creating an inclusive learning community, providers should draw on appropriate principles and engagement and guidance of embedding EDI in the curriculum (for example, Hanesworth, 2015; Mercer-Mapstone and Bovill, 2020; Stentiford and Koutsouris, 2021). These principles might include enabling potential, nurturing belonging and engagement, increasing awareness and understanding, encouraging an appreciation of others' perspectives, and developing self-reflection. It is important that a conscious and proactive approach to EDI is adopted within the learning environment, the design of Accounting degree content, and learning and teaching strategies."
  stem: none
  statementType: requirement
  rung: none
  force: should
  level: none
  appliesTo: "Accounting courses"
  addressee: provider
  verbs: ["draw", "adopted"]
  about: "principles for an inclusive learning community"
  themes: [theme:edi]
  domain: none
  award: ["none"]
  gradeOf: none
  paraphrase: "To create an inclusive learning community, providers should draw on established principles and guidance for embedding EDI in the curriculum (enabling potential, belonging, awareness, appreciation of other views, self-reflection), with a conscious, proactive approach in environment, content and teaching."
  quote: full   # the issuer's statement is in `source` (D-std-0014)
  audience: practitioner
  subjects: inherited
- id: qaa/accounting-2025/1.21
  locator: { number: "1.21", headingPath: ["Context and purposes of an Accounting degree", "Equality, diversity and inclusion"] }
  span: { start: 24626, end: 25577 }
  source: "1.21 Through a focus on EDI, Accounting education can support the progress of organisations of all types in addressing inequality and disadvantage as captured by, for example, the UN Sustainable Development Goals gender equality (Goal 5), decent work and economic growth (Goal 8), reduced inequalities (Goal 10), and peace, justice and strong institutions (Goal 16). The principles of EDI should be designed into the Accounting curriculum, along with an appreciation of the importance of continued reflective practice, to allow students to flourish in an increasingly diverse and global world, and to foster an inclusive approach in their future careers within a range of organisations and society more broadly. The study of Accounting should be designed to provide students with an understanding of the role which reporting and record keeping should play in addressing these issues, along with the tools and motivation to embed EDI in their practice."
  stem: none
  statementType: expectation
  rung: none
  force: should
  level: none
  appliesTo: "Accounting courses and their students"
  addressee: both
  verbs: ["designed", "provide", "embed"]
  about: "EDI in the curriculum and in reporting"
  themes: [theme:edi]
  domain: understanding
  award: ["none"]
  gradeOf: none
  paraphrase: "Through EDI, accounting education can help organisations tackle inequality (the SDGs on gender equality, decent work, reduced inequalities and strong institutions); the curriculum should build in EDI and continued reflection so students can thrive in a diverse world and act inclusively at work, and should give them an understanding of how reporting and record keeping can address these issues and the means and will to apply EDI in practice."
  quote: full   # the issuer's statement is in `source` (D-std-0014)
  audience: both
  subjects: inherited
- id: qaa/accounting-2025/1.22
  locator: { number: "1.22", headingPath: ["Context and purposes of an Accounting degree", "Equality, diversity and inclusion"] }
  span: { start: 25578, end: 26746 }
  source: "1.22 Accounting degree programmes should equip students with appropriate knowledge and skills needed to foster diverse and inclusive workplaces to meet the economic, social and environmental objectives of organisations and wider stakeholders. Degree programmes should ensure that students have an appreciation of the role of accounting in addressing global challenges, including poverty, justice, inequality and unethical behaviour. Accounting degree programmes should ensure that the content covered is diverse and offers a critical examination of dominant approaches to the discipline, thereby raising awareness of the ways in which they can perpetuate exclusion, and explore alternative approaches. In doing so, it is important that a wide and diverse range of perspectives is recognised and drawn upon, such as from the Global South, marginalised communities and local/regional/national communities. Using examples and cases that are representative of both the diversity of the student cohort and society more widely not only enriches the educational provision for all students, but also helps foster greater engagement and a sense of belonging among all students."
  stem: none
  statementType: expectation
  rung: none
  force: should
  level: none
  appliesTo: "Accounting courses and their students"
  addressee: both
  verbs: ["equip", "ensure", "explore"]
  about: "diverse content and critique of dominant approaches"
  themes: [theme:edi]
  domain: understanding
  award: ["none"]
  gradeOf: none
  paraphrase: "Courses should equip students to build diverse, inclusive workplaces and to see accounting's role in global challenges such as poverty, injustice and inequality; content should be diverse and should examine dominant approaches critically, drawing on perspectives from the Global South, marginalised and local communities, with examples that reflect the cohort and society."
  quote: full   # the issuer's statement is in `source` (D-std-0014)
  audience: both
  subjects: inherited
- id: qaa/accounting-2025/1.25
  locator: { number: "1.25", headingPath: ["Context and purposes of an Accounting degree", "Equality, diversity and inclusion"] }
  span: { start: 30604, end: 31530 }
  source: "1.25 Accounting degree programmes should be designed to enable students from all backgrounds to realise their potential and for all students, regardless of their protected or other characteristics (for example, race/ethnicity, religion, sex, gender, sexual orientation, disability or social background), and to feel represented and included. It is important that the learning, teaching and assessment environment is designed to be inclusive. A range of learning and teaching modes might be considered, including in-person, digital, blended, hybrid, hyflex, synchronous or asynchronous, block release, full or part-time. Assessment should be designed to be as inclusive as possible, reflecting an awareness of EDI. This involves considering a broad range of assessment types, including alternatives as required to address EDI issues and mitigating potential disadvantage (see also the assessment section, paragraphs 3.27-3.43)."
  stem: none
  statementType: requirement
  rung: none
  force: should
  level: none
  appliesTo: "Accounting courses"
  addressee: provider
  verbs: ["designed", "realise"]
  about: "inclusive design for all backgrounds"
  themes: [theme:edi]
  domain: none
  award: ["none"]
  gradeOf: none
  paraphrase: "Courses should be designed so that students of every background can reach their potential and feel represented and included whatever their characteristics; learning, teaching and assessment should be inclusive, using varied modes and a broad range of assessment types, with alternatives where needed."
  quote: full   # the issuer's statement is in `source` (D-std-0014)
  audience: practitioner
  subjects: inherited
- id: qaa/accounting-2025/1.28
  locator: { number: "1.28", headingPath: ["Context and purposes of an Accounting degree", "Equality, diversity and inclusion"] }
  span: { start: 32775, end: 33039 }
  source: "1.28 Continuous monitoring and review of EDI within degree programmes is essential. Programme teams should regularly reflect upon how well EDI policies have been implemented and how they can be further enhanced, where possible working in partnership with students."
  stem: none
  statementType: requirement
  rung: none
  force: should
  level: none
  appliesTo: "Accounting courses"
  addressee: provider
  verbs: ["reflect"]
  about: "monitoring and reviewing EDI"
  themes: [theme:edi]
  domain: none
  award: ["none"]
  gradeOf: none
  paraphrase: "EDI in a course needs continuous monitoring and review, and programme teams should regularly consider how well EDI policies are working and how to improve them, with students as partners where they can."
  quote: full   # the issuer's statement is in `source` (D-std-0014)
  audience: practitioner
  subjects: inherited
- id: qaa/accounting-2025/1.29
  locator: { number: "1.29", headingPath: ["Context and purposes of an Accounting degree", "Accessibility and the needs of disabled students"] }
  span: { start: 33089, end: 33694 }
  source: "1.29 Accounting degree programmes should include a commitment to widening access and inclusive participation to ensure that each Accounting student can thrive and reach their full potential, regardless of their background, disability, health or other protected characteristics. Providers of Accounting degree programmes should anticipate and take responsibility for the provision of inclusive learning, teaching and assessment. In conjunction with student support services, providers of Accounting degree programmes will also have responsibilities for making reasonable adjustments in a proactive fashion."
  stem: none
  statementType: requirement
  rung: none
  force: should
  level: none
  appliesTo: "Accounting courses"
  addressee: provider
  verbs: ["anticipate", "thrive"]
  about: "widening access and anticipating needs"
  themes: [theme:accessibility]
  domain: none
  award: ["none"]
  gradeOf: none
  paraphrase: "Courses should commit to widening access and inclusive participation so every student can thrive whatever their background, disability or health; providers should anticipate needs and take responsibility for inclusive learning, teaching and assessment, and with support services will make reasonable adjustments proactively."
  quote: full   # the issuer's statement is in `source` (D-std-0014)
  audience: practitioner
  subjects: inherited
- id: qaa/accounting-2025/1.30
  locator: { number: "1.30", headingPath: ["Context and purposes of an Accounting degree", "Accessibility and the needs of disabled students"] }
  span: { start: 33695, end: 34011 }
  source: "1.30 In addressing accessibility needs, providers of Accounting degree programmes should, as a minimum, meet regulatory requirements which will apply to all stages of the degree, from providing pre-application information through to graduation and beyond. Accessibility practices may include, but are not limited to:"
  stem: none
  statementType: requirement
  rung: none
  force: should
  level: none
  appliesTo: "Accounting courses"
  addressee: provider
  verbs: ["meet", "apply"]
  about: "meeting accessibility requirements at every stage"
  themes: [theme:accessibility]
  domain: none
  award: ["none"]
  gradeOf: none
  paraphrase: "On accessibility, providers should at the least meet the regulatory requirements, which run from pre-application information to graduation and after; the paragraph then lists practices that may help."
  quote: full   # the issuer's statement is in `source` (D-std-0014)
  audience: practitioner
  subjects: inherited
- id: qaa/accounting-2025/1.31
  locator: { number: "1.31", headingPath: ["Context and purposes of an Accounting degree", "Accessibility and the needs of disabled students"] }
  span: { start: 35081, end: 35337 }
  source: "1.31 Proactive approaches (including relevant investigation of potential attainment gaps) should be taken in the design of learning and teaching, and assessment, in order to build in inclusivity and flexibility to respond to the diversity of student needs."
  stem: none
  statementType: requirement
  rung: none
  force: should
  level: none
  appliesTo: "Accounting courses"
  addressee: provider
  verbs: ["taken", "respond"]
  about: "proactive inclusive design and attainment gaps"
  themes: [theme:accessibility]
  domain: none
  award: ["none"]
  gradeOf: none
  paraphrase: "Learning, teaching and assessment should be designed proactively, including looking into possible attainment gaps, so that inclusivity and flexibility are built in for diverse needs."
  quote: full   # the issuer's statement is in `source` (D-std-0014)
  audience: practitioner
  subjects: inherited
- id: qaa/accounting-2025/1.32
  locator: { number: "1.32", headingPath: ["Context and purposes of an Accounting degree", "Accessibility and the needs of disabled students"] }
  span: { start: 35338, end: 35614 }
  source: "1.32 Where applicable, accessibility should aim to provide all students, regardless of background, disability or other protected characteristics, with the same or similar opportunities for workplace and international learning, and extracurricular and co-curricular activities."
  stem: none
  statementType: requirement
  rung: none
  force: should
  level: none
  appliesTo: "Accounting courses"
  addressee: provider
  verbs: ["aim", "provide"]
  about: "equal access to placements, study abroad and activities"
  themes: [theme:accessibility]
  domain: none
  award: ["none"]
  gradeOf: none
  paraphrase: "Where relevant, accessibility should aim to give all students the same or similar chances of workplace and international learning and of extra-curricular and co-curricular activity."
  quote: full   # the issuer's statement is in `source` (D-std-0014)
  audience: practitioner
  subjects: inherited
- id: qaa/accounting-2025/1.33
  locator: { number: "1.33", headingPath: ["Context and purposes of an Accounting degree", "Education for sustainable development"] }
  span: { start: 35653, end: 36147 }
  source: "1.33 Accounting degree programmes should address sustainability in relation to current thinking, such as that articulated by the United Nations . In the context of this Accounting Subject Benchmark Statement, sustainable development is taken to encompass sustainability in its broadest sense, including welfare and a range of social, environmental, political and other perspectives (paragraph 1.4). Sustainable development is broader than environmental, social and governance (ESG) disclosures."
  stem: none
  statementType: requirement
  rung: none
  force: should
  level: none
  appliesTo: "Accounting courses"
  addressee: provider
  verbs: ["address"]
  about: "sustainability in its broadest sense"
  themes: [theme:esd]
  domain: none
  award: ["none"]
  gradeOf: none
  paraphrase: "Courses should address sustainability in line with current thinking such as the United Nations', taking sustainable development in its widest sense of welfare and social, environmental and political perspectives, which is wider than ESG disclosure."
  quote: full   # the issuer's statement is in `source` (D-std-0014)
  audience: practitioner
  subjects: inherited
- id: qaa/accounting-2025/1.34
  locator: { number: "1.34", headingPath: ["Context and purposes of an Accounting degree", "Education for sustainable development"] }
  span: { start: 36148, end: 37081 }
  source: "1.34 An Accounting degree programme should provide students with the capacity to apply traditional and emerging accounting practices in a way that supports the transition towards a more sustainable and fairer world as envisaged by extant national and global standards on sustainability and sustainable development, such as the United Nations Sustainable Development Goals (SDGs) and UN Principles of Responsible Management Education (PRME). To achieve this capacity, accounting degree programmes should develop students' traditional and emerging technical, critical and transferable skills, higher-level intellectual skills, ethical orientation, and anticipatory mindsets that Accounting graduates need to steer organisations and communities toward sustainable outcomes, recognising the urgency and extent of sustainability challenges to society and the planet and reflecting potential impact on, and risks for, diverse stakeholders."
  stem: none
  statementType: expectation
  rung: none
  force: should
  level: none
  appliesTo: "Accounting courses and their students"
  addressee: both
  verbs: ["provide", "apply", "develop"]
  about: "accounting for a sustainable transition"
  themes: [theme:esd]
  domain: subject-skill
  award: ["none"]
  gradeOf: none
  paraphrase: "A degree should give students the capacity to use traditional and emerging accounting practices to support the move to a more sustainable and fairer world, as framed by the SDGs and PRME; to that end it should develop their technical, critical and transferable skills, higher-order thinking, ethics and forward-looking mindsets for steering organisations towards sustainable outcomes."
  quote: full   # the issuer's statement is in `source` (D-std-0014)
  audience: both
  subjects: inherited
- id: qaa/accounting-2025/1.35
  locator: { number: "1.35", headingPath: ["Context and purposes of an Accounting degree", "Education for sustainable development"] }
  span: { start: 37082, end: 37587 }
  source: "1.35 Accounting degree programmes should exemplify the role of accounting, accountants and the accounting profession as leaders and catalysts for change, including making sustainability issues visible; determining how the impact of the actions of business and other organisations are accounted for and communicated; integrating concepts such as double materiality into reporting; valuing assets and investments; enhancing transparency and accountability; and enabling engagement with diverse stakeholders."
  stem: none
  statementType: expectation
  rung: none
  force: should
  level: none
  appliesTo: "Accounting courses and their students"
  addressee: both
  verbs: ["exemplify"]
  about: "accounting as a catalyst for sustainable change"
  themes: [theme:esd]
  domain: understanding
  award: ["none"]
  gradeOf: none
  paraphrase: "Courses should show accounting and accountants as leaders of change: making sustainability visible, deciding how organisations' impacts are counted and reported, building in double materiality, valuing assets, increasing transparency and engaging diverse stakeholders."
  quote: full   # the issuer's statement is in `source` (D-std-0014)
  audience: both
  subjects: inherited
- id: qaa/accounting-2025/1.36
  locator: { number: "1.36", headingPath: ["Context and purposes of an Accounting degree", "Education for sustainable development"] }
  span: { start: 37588, end: 37943 }
  source: "1.36 Accounting graduates should have knowledge and understanding of accounting, assurance and accountability theories and practices that can contribute towards achieving sustainable development. Graduates should also be able to critically evaluate how the application of these or alternative practices and theories can engender more sustainable outcomes."
  stem: none
  statementType: expectation
  rung: none
  force: should
  level: none
  appliesTo: "graduates of the subject"
  addressee: learner
  verbs: ["evaluate"]
  about: "accounting theories and practices for sustainable development"
  themes: [theme:esd]
  domain: knowledge
  award: ["none"]
  gradeOf: none
  paraphrase: "Graduates should know and understand theories and practices of accounting, assurance and accountability that can help achieve sustainable development, and be able to evaluate critically how these or other approaches can lead to more sustainable results."
  quote: full   # the issuer's statement is in `source` (D-std-0014)
  audience: both
  subjects: inherited
- id: qaa/accounting-2025/1.38
  locator: { number: "1.38", headingPath: ["Context and purposes of an Accounting degree", "Education for sustainable development"] }
  span: { start: 38283, end: 38649 }
  source: "1.38 Accounting graduates should have the capabilities to drive and lead the sustainability agenda for business and society, particularly in relation to the ethics, responsibility and sustainability requirements of relevant accounting accrediting bodies and EDI responsibilities (paragraphs 1.19- 1.28) and in the development of sustainable entrepreneurial mindsets."
  stem: none
  statementType: expectation
  rung: none
  force: should
  level: fheq:6
  appliesTo: "graduates of the subject"
  addressee: learner
  verbs: ["drive", "lead"]
  about: "leading the sustainability agenda"
  themes: [theme:esd]
  domain: generic-skill
  award: ["bachelor's with honours"]
  gradeOf: none
  paraphrase: "Graduates should be capable of driving and leading the sustainability agenda for business and society, above all on the ethics, responsibility and sustainability expectations of accounting accrediting bodies and on EDI, and in growing sustainable entrepreneurial mindsets."
  quote: full   # the issuer's statement is in `source` (D-std-0014)
  audience: both
  subjects: inherited
- id: qaa/accounting-2025/1.39
  locator: { number: "1.39", headingPath: ["Context and purposes of an Accounting degree", "Education for sustainable development"] }
  span: { start: 38654, end: 39133 }
  source: "1.39 Accounting degree programmes should be designed and configured to equip students to support organisations and society in their transition to a more sustainable future. The study of Accounting should consider accounting and accountants as embedded in a dynamic set of social, economic, organisational and political practices that are performative in bringing about material changes through articulating and making transparent evidence of decision consequences (Walker, 2016)."
  stem: none
  statementType: expectation
  rung: none
  force: should
  level: none
  appliesTo: "Accounting courses and their students"
  addressee: both
  verbs: ["designed", "equip", "support", "consider"]
  about: "accounting as a performative social practice"
  themes: [theme:esd]
  domain: understanding
  award: ["none"]
  gradeOf: none
  paraphrase: "Courses should be designed to prepare students to help organisations and society move to a more sustainable future, and should treat accounting and accountants as part of changing social, economic, organisational and political practices that bring about real change by making the consequences of decisions transparent."
  quote: full   # the issuer's statement is in `source` (D-std-0014)
  audience: both
  subjects: inherited
- id: qaa/accounting-2025/1.40
  locator: { number: "1.40", headingPath: ["Context and purposes of an Accounting degree", "Education for sustainable development"] }
  span: { start: 39134, end: 39641 }
  source: "1.40 Accounting degree programmes should reflect extant and emerging sustainable development priorities that are drivers in shaping and reshaping accounting and assurance practices, such as transitioning to net zero, regenerative business models, eliminating modern slavery, managing carbon emissions, greenhouse gas management, management of plastic usage and waste, water conservation, sustainable supply chain management, and contemporary developments in sustainability reporting and assurance standards."
  stem: none
  statementType: requirement
  rung: none
  force: should
  level: none
  appliesTo: "Accounting courses"
  addressee: provider
  verbs: ["reflect"]
  about: "current sustainability priorities in content"
  themes: [theme:esd]
  domain: none
  award: ["none"]
  gradeOf: none
  paraphrase: "Courses should reflect current and emerging sustainability priorities that are reshaping accounting and assurance, such as net zero, regenerative business models, modern slavery, carbon and greenhouse gas management, plastics and waste, water, sustainable supply chains and new reporting and assurance standards."
  quote: full   # the issuer's statement is in `source` (D-std-0014)
  audience: practitioner
  subjects: inherited
- id: qaa/accounting-2025/1.41
  locator: { number: "1.41", headingPath: ["Context and purposes of an Accounting degree", "Education for sustainable development"] }
  span: { start: 39642, end: 40237 }
  source: "1.41 An Accounting degree programme should prepare students to understand how the design and operation of systems to provide data and information facilitates the embedding of sustainability in all accounting and organisational information systems, and for students to develop skills to facilitate them to design, analyse, transform and manage sustainability data and information (paragraph 1.11). This requires an understanding of how sustainability data can be embedded in data structures within systems (including ERP systems) and how unstructured data can be used for sustainability purposes."
  stem: none
  statementType: expectation
  rung: none
  force: should
  level: none
  appliesTo: "Accounting courses and their students"
  addressee: both
  verbs: ["prepare", "understand", "develop", "design", "analyse", "transform", "manage"]
  about: "sustainability data in information systems"
  themes: [theme:esd]
  domain: subject-skill
  award: ["none"]
  gradeOf: none
  paraphrase: "A degree should prepare students to understand how information systems can embed sustainability throughout accounting and organisational systems and develop their skill in designing, analysing, transforming and managing sustainability data, including how it sits in data structures and ERP systems and how unstructured data can serve sustainability ends."
  quote: full   # the issuer's statement is in `source` (D-std-0014)
  audience: both
  subjects: inherited
- id: qaa/accounting-2025/1.42
  locator: { number: "1.42", headingPath: ["Context and purposes of an Accounting degree", "Education for sustainable development"] }
  span: { start: 40238, end: 40789 }
  source: "1.42 Accounting degree programmes should highlight the importance of critical enquiry on issues affecting planetary boundaries and the implications of sustainability for economic growth, social well-being and political stability. This entails students building skills in critical thinking; self-awareness; self-efficacy in raising issues; collaborative competencies; anticipatory, systemic and strategic thinking; and effective measurement, valuation and communication. These skills form a foundation for further study, research and lifelong learning."
  stem: none
  statementType: expectation
  rung: none
  force: should
  level: fheq:6
  appliesTo: "Accounting courses and their students"
  addressee: both
  verbs: ["highlight"]
  about: "critical enquiry on planetary limits"
  themes: [theme:esd]
  domain: generic-skill
  award: ["bachelor's with honours"]
  gradeOf: none
  paraphrase: "Courses should stress critical enquiry into planetary boundaries and what sustainability means for growth, well-being and political stability, with students building critical thinking, self-awareness, confidence to raise issues, collaboration, anticipatory and systemic thinking and sound measurement, valuation and communication as a base for further study and lifelong learning."
  quote: full   # the issuer's statement is in `source` (D-std-0014)
  audience: both
  subjects: inherited
- id: qaa/accounting-2025/1.43
  locator: { number: "1.43", headingPath: ["Context and purposes of an Accounting degree", "Education for sustainable development"] }
  span: { start: 40790, end: 41059 }
  source: "1.43 Accounting degree programmes should integrate and mainstream economic, social and environmental sustainability throughout the Accounting curriculum, complemented where appropriate with specialist modules for specific topics, such as climate change or biodiversity."
  stem: none
  statementType: requirement
  rung: none
  force: should
  level: none
  appliesTo: "Accounting courses"
  addressee: provider
  verbs: ["integrate", "mainstream"]
  about: "sustainability throughout the curriculum"
  themes: [theme:esd]
  domain: none
  award: ["none"]
  gradeOf: none
  paraphrase: "Courses should weave economic, social and environmental sustainability through the whole curriculum, adding specialist modules on topics such as climate change or biodiversity where suitable."
  quote: full   # the issuer's statement is in `source` (D-std-0014)
  audience: practitioner
  subjects: inherited
- id: qaa/accounting-2025/1.44
  locator: { number: "1.44", headingPath: ["Context and purposes of an Accounting degree", "Employability, enterprise and entrepreneurship education"] }
  span: { start: 41117, end: 41980 }
  source: "1.44 In the context of Accounting degree programmes, enterprise and entrepreneurship education is the process of developing students in a manner that provides them with an enhanced capacity to generate ideas, and the behaviours, attributes and competencies to make them happen. Allied to this, entrepreneurship is the application of enterprise behaviours, attributes and competencies to create cultural, social or economic value, at individual, organisational and societal levels. The inclusion of enterprise and entrepreneurship in Accounting degree programmes enhances employability by promoting personal development. Accounting degree programmes should include enterprise and entrepreneurship to develop graduates who are enterprising, flexible and innovative to navigate through the complexities of the dynamic work environment with confidence and creativity."
  stem: none
  statementType: expectation
  rung: none
  force: should
  level: fheq:6
  appliesTo: "Accounting courses and their students"
  addressee: both
  verbs: ["include", "develop", "navigate"]
  about: "enterprise and entrepreneurship education"
  themes: [theme:enterprise]
  domain: generic-skill
  award: ["bachelor's with honours"]
  gradeOf: none
  paraphrase: "Enterprise education develops the capacity to generate ideas and the behaviours to realise them, and entrepreneurship applies them to create cultural, social or economic value; including both improves employability, and courses should include them to produce enterprising, flexible and innovative graduates who can handle a changing workplace with confidence and creativity."
  quote: full   # the issuer's statement is in `source` (D-std-0014)
  audience: both
  subjects: inherited
- id: qaa/accounting-2025/1.45
  locator: { number: "1.45", headingPath: ["Context and purposes of an Accounting degree", "Employability, enterprise and entrepreneurship education"] }
  span: { start: 41981, end: 42556 }
  source: "1.45 Accounting degree programmes should develop students' capacity to be critical thinkers to enable them to generate and implement innovative ideas that support them in being entrepreneurial (including self-employment) and to be more likely to be employable in any sector. In addition, enterprise and entrepreneurial education within Accounting degree programmes should contribute to students' cultural, social and economic values, equipping\n\n12\nthem for lifelong learning, a self-determined professional life and an ability to succeed in a wide variety of career pathways."
  stem: none
  statementType: expectation
  rung: none
  force: should
  level: fheq:6
  appliesTo: "Accounting courses and their students"
  addressee: both
  verbs: ["develop", "generate", "implement", "contribute"]
  about: "critical thinkers who can act on ideas"
  themes: [theme:enterprise]
  domain: generic-skill
  award: ["bachelor's with honours"]
  gradeOf: none
  paraphrase: "Courses should make students critical thinkers who can generate and carry out new ideas, to be entrepreneurial (self-employment included) and employable in any sector; enterprise education should add to their cultural, social and economic values and fit them for lifelong learning, a self-directed career and many career paths."
  quote: full   # the issuer's statement is in `source` (D-std-0014)
  audience: both
  subjects: inherited
- id: qaa/accounting-2025/1.46
  locator: { number: "1.46", headingPath: ["Context and purposes of an Accounting degree", "Employability, enterprise and entrepreneurship education"] }
  span: { start: 42557, end: 43434 }
  source: "1.46 By covering the principles set out in paragraphs 1.4 to 1.14, Accounting degrees should develop skills and attributes that are consistent with the enterprise and entrepreneurship agenda to cultivate their critical thinking and higher-level intellectual skills. In addition, research-led and research-informed educational approaches (paragraphs 1.4,\n1.46 and 3.16-3.26) should be used to further develop enterprise and entrepreneurship skills such as open-mindedness, proactivity, determination, resilience, and self-efficacy. Within an Accounting degree programme, enterprise and entrepreneurial skills should also be developed via recognition of the importance of knowledge and understanding of alternative accounting options being integral to effective negotiation; creative problem-solving; professional judgement; leadership; commercial awareness; and business acumen."
  stem: none
  statementType: expectation
  rung: none
  force: should
  level: fheq:6
  appliesTo: "Accounting courses and their students"
  addressee: both
  verbs: ["develop", "used"]
  about: "enterprise skills through the core content"
  themes: [theme:enterprise]
  domain: generic-skill
  award: ["bachelor's with honours"]
  gradeOf: none
  paraphrase: "Covering the core principles of the subject should develop enterprise-related skills and attributes, and research-led and research-informed teaching should be used to grow open-mindedness, proactivity, determination, resilience and self-efficacy; enterprise skills should also come through seeing that knowing alternative accounting options supports negotiation, creative problem-solving, judgement, leadership, commercial awareness and business acumen."
  quote: full   # the issuer's statement is in `source` (D-std-0014)
  audience: both
  subjects: inherited
- id: qaa/accounting-2025/1.51
  locator: { number: "1.51", headingPath: ["Context and purposes of an Accounting degree", "Generative artificial intelligence"] }
  span: { start: 45568, end: 46285 }
  source: "1.51 Accounting degree programmes should include knowledge and understanding of the ways in which GenAI is used in accounting practice, build students' skills in the use of appropriate accounting and professional GenAI tools, and develop students' critical thinking concerning the implications and limitations of the use of GenAI tools. AI and GenAI are already widely used in the accounting profession (for example, in document repositories, practice management software, audit and tax analytics, and audit planning support software) and the use of GenAI is making its way into a wider range of professional support systems. This means that Accounting degrees need to adapt dynamically to future development changes."
  stem: none
  statementType: expectation
  rung: none
  force: should
  level: none
  appliesTo: "Accounting courses and their students"
  addressee: both
  verbs: ["include", "build", "develop", "adapt"]
  about: "GenAI in accounting practice"
  themes: [theme:genai]
  domain: subject-skill
  award: ["none"]
  gradeOf: none
  paraphrase: "Courses should cover how GenAI is used in accounting practice, build students' skill with suitable professional GenAI tools and develop critical thinking about the limits and implications of those tools; since AI is already common in practice software, analytics and audit planning, degrees need to keep adapting."
  quote: full   # the issuer's statement is in `source` (D-std-0014)
  audience: both
  subjects: inherited
- id: qaa/accounting-2025/1.52
  locator: { number: "1.52", headingPath: ["Context and purposes of an Accounting degree", "Generative artificial intelligence"] }
  span: { start: 46290, end: 46869 }
  source: "1.52 Accounting degree programme providers need to be aware of the potential dangers of AI in that it learns from existing text, decisions and actions. It therefore has the potential to propagate existing biases (for example, gender, race, social class and capitalist-rationale- based discrimination) unless it is controlled or mitigated, which is itself likely to be biased. Accounting degree programmes should develop students' knowledge and understanding of the potential for bias and discrimination within AI systems and how these might be mitigated (Ballantine et al, 2024)."
  stem: none
  statementType: expectation
  rung: none
  force: should
  level: none
  appliesTo: "Accounting courses and their students"
  addressee: both
  verbs: ["develop", "mitigated"]
  about: "bias in AI systems"
  themes: [theme:genai]
  domain: understanding
  award: ["none"]
  gradeOf: none
  paraphrase: "Because AI learns from existing text and decisions it can spread bias (by gender, race, class or capitalist logic) unless controlled, and the control can itself be biased; providers need to know this, and courses should develop students' understanding of bias and discrimination in AI and how to reduce them."
  quote: full   # the issuer's statement is in `source` (D-std-0014)
  audience: both
  subjects: inherited
- id: qaa/accounting-2025/1.53
  locator: { number: "1.53", headingPath: ["Context and purposes of an Accounting degree", "Generative artificial intelligence"] }
  span: { start: 46870, end: 47700 }
  source: "1.53 Accounting degree programmes should be designed to include GenAI that promotes positive learning and teaching, for example by: making learning and teaching more interactive; providing AI-generated essay-type answers for students to discuss and critique, and as comparators for their own writing; using these comparators to help students develop dialogues of learning via inner feedback (Nicol, 2021; Nicol and McCallum, 2022); and using alternative pedagogies that are particularly useful for engendering understanding (for example, dialogic and experiential learning) (Ballantine et al., 2024; Thomson and Bebbington, 2004). In this context it is important that students learn to use technology, including GenAI , with integrity, and that Accounting degree programmes link this to the broader ethics landscape of accounting."
  stem: none
  statementType: expectation
  rung: none
  force: should
  level: none
  appliesTo: "Accounting courses and their students"
  addressee: both
  verbs: ["designed", "include", "learn", "link"]
  about: "GenAI in learning and teaching"
  themes: [theme:genai]
  domain: none
  award: ["none"]
  gradeOf: none
  paraphrase: "Courses should use GenAI to support learning, for example to make teaching more interactive, to provide AI-written answers for students to critique and compare with their own writing, and to support dialogic and experiential learning; students should learn to use technology with integrity, linked to the profession's ethics."
  quote: full   # the issuer's statement is in `source` (D-std-0014)
  audience: both
  subjects: inherited
- id: qaa/accounting-2025/1.54
  locator: { number: "1.54", headingPath: ["Context and purposes of an Accounting degree", "Generative artificial intelligence"] }
  span: { start: 47701, end: 48668 }
  source: "1.54 The widespread availability of GenAI makes it essential that Accounting degree programmes take account of the implications of AI in assessment design. However, GenAI also provides opportunities to design assessment that is more in line with the requirements of this Subject Benchmark Statement. This might include moving away from assessment that relies on rote learning, regurgitation, and surface learning (for example, objective or multiple- choice assessment); the use of critical assessment, including authentic scenario and case- based work; embedding technical problem questions into dynamic cases or scenarios; evaluating experiential learning tasks; and assessing students' critical understanding of the implications of AI within accounting as a discipline and accounting practice. Such changes are also important in developing the range of skills outlined in this Statement. These issues should be considered in both formative and summative assessment."
  stem: none
  statementType: requirement
  rung: none
  force: should
  level: none
  appliesTo: "Accounting courses"
  addressee: provider
  verbs: ["take", "design", "considered"]
  about: "assessment design in the age of GenAI"
  themes: [theme:genai]
  domain: none
  award: ["none"]
  gradeOf: none
  paraphrase: "GenAI makes it essential to rethink assessment: it can move assessment away from rote and multiple-choice formats towards critical, authentic, case-based and experiential tasks, including assessment of students' grasp of AI in accounting; these points should be weighed in formative and summative assessment alike."
  quote: full   # the issuer's statement is in `source` (D-std-0014)
  audience: practitioner
  subjects: inherited
- id: qaa/accounting-2025/1.55
  locator: { number: "1.55", headingPath: ["Context and purposes of an Accounting degree", "Generative artificial intelligence"] }
  span: { start: 48669, end: 49405 }
  source: "1.55 It is the responsibility of Accounting degree programme providers to employ appropriate due diligence procedures to ensure that assessment is rigorous and has academic integrity in the face of the challenges of GenAI. This involves the existence and consistent application of appropriate and comprehensive authorial integrity and GenAI aware quality control policies and practices, and an awareness of the potential unethical use of GenAI by both students and staff. Continuous monitoring and review of authorial integrity and GenAI aware control policies and practices is essential, especially as GenAI content is very difficult to reliably detect. The policies and practices should be adequately communicated to all stakeholders."
  stem: none
  statementType: requirement
  rung: none
  force: should
  level: none
  appliesTo: "Accounting courses"
  addressee: provider
  verbs: ["employ", "ensure", "communicated"]
  about: "academic integrity and GenAI policies"
  themes: [theme:genai]
  domain: none
  award: ["none"]
  gradeOf: none
  paraphrase: "Providers are responsible for due diligence to keep assessment rigorous and honest despite GenAI: clear, consistently applied integrity and GenAI-aware quality policies, awareness of misuse by students and staff, continuous review, since detection is unreliable, and policies communicated to everyone involved."
  quote: full   # the issuer's statement is in `source` (D-std-0014)
  audience: practitioner
  subjects: inherited
- id: qaa/accounting-2025/2.1
  locator: { number: "2.1", headingPath: ["Distinctive features of the Accounting degree", "Design"] }
  span: { start: 49465, end: 50183 }
  source: "2.1 Accounting degree programmes should be designed to provide students with the opportunity to develop a broad-based and intellectually rigorous understanding of accounting in its socioeconomic context (paragraph 1.4); to equip students to make sound and creative judgements on complex problems (paragraph 1.10); to understand the role of accounting in a range of different types of organisations (including not-for-profit) and from the perspectives of various stakeholders (paragraph 1.5); to understand the role of accounting in major issues such as sustainability (paragraphs 1.33-1.43), and EDI and accessibility (paragraphs 1.19- 1.32); and enable them to become responsible and ethical citizens (paragraph 1.4)."
  stem: none
  statementType: expectation
  rung: none
  force: should
  level: none
  appliesTo: "Accounting courses and their students"
  addressee: both
  verbs: ["designed", "develop", "equip", "understand", "enable"]
  about: "design aims of an Accounting degree"
  themes: [none]
  domain: understanding
  award: ["none"]
  gradeOf: none
  paraphrase: "Courses should be designed so students can build a broad, rigorous understanding of accounting in its social and economic setting, make sound and creative judgements on complex problems, understand accounting across kinds of organisation and stakeholder and in issues such as sustainability, EDI and accessibility, and become responsible, ethical citizens."
  quote: full   # the issuer's statement is in `source` (D-std-0014)
  audience: both
  subjects: inherited
- id: qaa/accounting-2025/2.2
  locator: { number: "2.2", headingPath: ["Distinctive features of the Accounting degree", "Design"] }
  span: { start: 50184, end: 51080 }
  source: "2.2 Accounting degree programmes should be designed to include learning objectives that are aligned with the knowledge, understanding and skills detailed in section 3 (paragraphs 3.12-3.15) and to reflect appropriate principles of learning, teaching (paragraphs 3.16-3.26) and assessment (paragraphs 3.27-3.43). The design of an Accounting degree programme should be shaped, but not be overly constrained, by institutional structures and practices. The learning objectives should be structured to ensure that they integrate the conceptual and applied aspects of the curriculum and the relationship between them and between different areas of knowledge and understanding. Design flexibility is required to facilitate the dynamic nature of accounting (paragraph 1.9) as a subject and as a profession, particularly in relation to increasing use of technology, including GenAI (paragraphs 1.49-1.55)."
  stem: none
  statementType: requirement
  rung: none
  force: should
  level: none
  appliesTo: "Accounting courses"
  addressee: provider
  verbs: ["designed", "include", "structured", "integrate"]
  about: "learning objectives aligned to the statement"
  themes: [none]
  domain: none
  award: ["none"]
  gradeOf: none
  paraphrase: "Courses should set learning objectives in line with section 3's knowledge, understanding and skills and with sound learning, teaching and assessment principles; institutional structures should shape but not overly limit the design; objectives should join the conceptual and applied and link areas of knowledge, with room to adapt to change in the subject and to technology such as GenAI."
  quote: full   # the issuer's statement is in `source` (D-std-0014)
  audience: practitioner
  subjects: inherited
- id: qaa/accounting-2025/2.3
  locator: { number: "2.3", headingPath: ["Distinctive features of the Accounting degree", "Design"] }
  span: { start: 51081, end: 51465 }
  source: "2.3 Accounting degree programmes should be designed to provide students with the opportunity to develop the higher-level intellectual skills (paragraph 1.12) that are necessary to deal with the changing nature of society and the workplace, including increasing levels of automation. An Accounting degree should prepare students for lifelong and self-directed learning (paragraph 1.9)."
  stem: none
  statementType: expectation
  rung: none
  force: should
  level: fheq:6
  appliesTo: "Accounting courses and their students"
  addressee: both
  verbs: ["designed", "develop", "prepare"]
  about: "higher-order thinking and lifelong learning"
  themes: [none]
  domain: generic-skill
  award: ["bachelor's with honours"]
  gradeOf: none
  paraphrase: "Courses should be designed so students develop the higher-order intellectual skills needed in a changing, increasingly automated society and workplace, and a degree should prepare them for lifelong, self-directed learning."
  quote: full   # the issuer's statement is in `source` (D-std-0014)
  audience: both
  subjects: inherited
- id: qaa/accounting-2025/2.4
  locator: { number: "2.4", headingPath: ["Distinctive features of the Accounting degree", "Design"] }
  span: { start: 51466, end: 51634 }
  source: "2.4 Accounting degree programmes should be designed to enable students to thrive in a range of careers, entrepreneurial activities or academic pursuits (paragraph 1.4)."
  stem: none
  statementType: expectation
  rung: none
  force: should
  level: none
  appliesTo: "Accounting courses and their students"
  addressee: both
  verbs: ["designed", "enable", "thrive"]
  about: "preparing for many careers"
  themes: [none]
  domain: none
  award: ["none"]
  gradeOf: none
  paraphrase: "Courses should be designed so students can succeed in a range of careers, entrepreneurial ventures or academic paths."
  quote: full   # the issuer's statement is in `source` (D-std-0014)
  audience: both
  subjects: inherited
- id: qaa/accounting-2025/2.5
  locator: { number: "2.5", headingPath: ["Distinctive features of the Accounting degree", "Design"] }
  span: { start: 51635, end: 52073 }
  source: "2.5 While many students aspire to pursue a professional accounting qualification on graduation, Accounting degree programmes should be designed taking into account the broader and changing objectives and career aspirations of students. Therefore, Accounting degree programmes should not be designed to meet the exemption and accreditation of professional accounting and other PSRBs at the expense of broader design objectives (section 3)."
  stem: none
  statementType: requirement
  rung: none
  force: should
  level: none
  appliesTo: "Accounting courses"
  addressee: provider
  verbs: ["designed", "meet"]
  about: "accreditation not at the expense of breadth"
  themes: [none]
  domain: none
  award: ["none"]
  gradeOf: none
  paraphrase: "Many students hope to qualify professionally, but courses should take account of students' wider and changing aims and should not be designed to win PSRB exemptions and accreditation at the cost of the broader aims of section 3."
  quote: full   # the issuer's statement is in `source` (D-std-0014)
  audience: practitioner
  subjects: inherited
- id: qaa/accounting-2025/2.6
  locator: { number: "2.6", headingPath: ["Distinctive features of the Accounting degree", "Design"] }
  span: { start: 52074, end: 52611 }
  source: "2.6 Joint degree programmes that include Accounting should be designed to ensure that they include the majority of the knowledge, understanding and skills detailed in this Subject Benchmark Statement (paragraph 1.3). The design should also ensure that the scope, depth and balance of concepts and application does not result in a neglect of the conceptual accounting issues, accounting theory, accountability, sustainability, non-business uses, or the applied aspects of accounting or the development of higher-level intellectual skills."
  stem: none
  statementType: requirement
  rung: none
  force: should
  level: fheq:6
  appliesTo: "joint degrees that include Accounting"
  addressee: provider
  verbs: ["designed", "ensure", "include"]
  about: "coverage in joint degrees"
  themes: [none]
  domain: none
  award: ["bachelor's with honours"]
  gradeOf: none
  paraphrase: "Joint degrees with Accounting should be designed to include most of the statement's knowledge, understanding and skills, with a balance that still keeps conceptual issues, theory, accountability, sustainability, non-business uses, application and higher-order thinking."
  quote: full   # the issuer's statement is in `source` (D-std-0014)
  audience: practitioner
  subjects: inherited
- id: qaa/accounting-2025/2.10
  locator: { number: "2.10", headingPath: ["Distinctive features of the Accounting degree", "Progression"] }
  span: { start: 54137, end: 54338 }
  source: "2.10 Progression requirements for students studying Accounting as part of a combined or joint honours degree with other subjects will be designed to satisfy the progression needs of both subject areas."
  stem: none
  statementType: requirement
  rung: none
  force: will
  level: fheq:6
  appliesTo: "combined or joint honours with Accounting"
  addressee: provider
  verbs: ["designed", "satisfy"]
  about: "progression rules in joint honours"
  themes: [none]
  domain: none
  award: ["bachelor's with honours"]
  gradeOf: none
  paraphrase: "In combined or joint honours, progression requirements will be designed to meet the progression needs of both subjects."
  quote: full   # the issuer's statement is in `source` (D-std-0014)
  audience: practitioner
  subjects: inherited
- id: qaa/accounting-2025/2.11
  locator: { number: "2.11", headingPath: ["Distinctive features of the Accounting degree", "Progression"] }
  span: { start: 54339, end: 54580 }
  source: "2.11 Progression should be designed to take account of individual needs and, where relevant and possible, allow reasonable adjustments to be put in place (paragraph 1.27), to help all students to reach their potential (paragraphs 1.25-1.27)."
  stem: none
  statementType: requirement
  rung: none
  force: should
  level: none
  appliesTo: "Accounting courses"
  addressee: provider
  verbs: ["designed", "allow", "reach"]
  about: "progression that allows for individual needs"
  themes: [none]
  domain: none
  award: ["none"]
  gradeOf: none
  paraphrase: "Progression should allow for each student's needs and, where it is relevant and feasible, permit reasonable adjustments, so that every student can reach their potential."
  quote: full   # the issuer's statement is in `source` (D-std-0014)
  audience: practitioner
  subjects: inherited
- id: qaa/accounting-2025/2.12
  locator: { number: "2.12", headingPath: ["Distinctive features of the Accounting degree", "Progression"] }
  span: { start: 54581, end: 54743 }
  source: "2.12 An honours degree in Accounting should provide a sound basis for pursuing a professional qualification or other careers, particularly in business or finance."
  stem: none
  statementType: expectation
  rung: none
  force: should
  level: fheq:6
  appliesTo: "Accounting courses and their students"
  addressee: both
  verbs: ["provide", "pursuing"]
  about: "honours as a basis for qualification and careers"
  themes: [none]
  domain: none
  award: ["bachelor's with honours"]
  gradeOf: none
  paraphrase: "An honours degree in Accounting should give a sound base for a professional qualification or other careers, especially in business or finance."
  quote: full   # the issuer's statement is in `source` (D-std-0014)
  audience: both
  subjects: inherited
- id: qaa/accounting-2025/2.13
  locator: { number: "2.13", headingPath: ["Distinctive features of the Accounting degree", "Progression"] }
  span: { start: 54744, end: 55417 }
  source: "2.13 It would be expected that a student who had achieved a second-class degree or higher should be equipped to undertake postgraduate study in Accounting or a related discipline. However, entry requirements to postgraduate degrees are determined by individual providers and may require specified levels of achievement at undergraduate level and consider other types of achievement and experiences. The same principles of progression will normally apply to progression to the master's element of an integrated master's degree (FHEQ Level 7; FQHEIS Level 11), which typically require the equivalent of an additional full-time year of study following an undergraduate degree."
  stem: none
  statementType: expectation
  rung: none
  force: should
  level: fheq:6
  appliesTo: "honours graduates with a second-class degree or higher"
  addressee: learner
  verbs: ["equipped", "undertake"]
  about: "readiness for postgraduate study"
  themes: [none]
  domain: none
  award: ["bachelor's with honours"]
  gradeOf: none
  paraphrase: "A student with at least a second-class degree should be ready for postgraduate study in Accounting or a related subject, though entry is for each provider to set; the same principles normally govern progression to the master's year of an integrated master's."
  quote: full   # the issuer's statement is in `source` (D-std-0014)
  audience: both
  subjects: inherited
- id: qaa/accounting-2025/2.14
  locator: { number: "2.14", headingPath: ["Distinctive features of the Accounting degree", "Progression"] }
  span: { start: 55418, end: 55653 }
  source: "2.14 Similar progression standards will apply to students undertaking Degree Apprenticeships at FHEQ Level 6 or FQHEIS Level 10. Students may be required to pass additional end-point assessment in order to be awarded an apprenticeship."
  stem: none
  statementType: expectation
  rung: none
  force: will
  level: fheq:6
  appliesTo: "degree apprentices in Accounting"
  addressee: both
  verbs: ["apply", "pass"]
  about: "progression on degree apprenticeships"
  themes: [none]
  domain: none
  award: ["degree apprenticeship"]
  gradeOf: none
  paraphrase: "Similar progression standards will apply to degree apprentices at honours level (FHEQ 6, FQHEIS 10), and apprentices may also need to pass an end-point assessment."
  quote: full   # the issuer's statement is in `source` (D-std-0014)
  audience: both
  subjects: inherited
- id: qaa/accounting-2025/2.16
  locator: { number: "2.16", headingPath: ["Distinctive features of the Accounting degree", "Flexibility"] }
  span: { start: 55987, end: 56371 }
  source: "2.16 Accounting degree programmes need to be adaptable to respond to, and anticipate, advances in the subject, related disciplines and the needs of its graduates and employers. They should be sufficiently flexible to address the needs of learners, the profession, wider community stakeholders, and factors related to the requirements of external governing, regulating bodies or PSRBs."
  stem: none
  statementType: requirement
  rung: none
  force: should
  level: none
  appliesTo: "Accounting courses"
  addressee: provider
  verbs: ["respond", "anticipate", "address"]
  about: "adaptable and flexible courses"
  themes: [none]
  domain: none
  award: ["none"]
  gradeOf: none
  paraphrase: "Courses need to adapt to, and anticipate, advances in the subject and related fields and the needs of graduates and employers, and should be flexible enough to serve learners, the profession, wider stakeholders and external bodies' requirements."
  quote: full   # the issuer's statement is in `source` (D-std-0014)
  audience: practitioner
  subjects: inherited
- id: qaa/accounting-2025/2.17
  locator: { number: "2.17", headingPath: ["Distinctive features of the Accounting degree", "Flexibility"] }
  span: { start: 56372, end: 56918 }
  source: "2.17 Accounting degrees should be designed with inclusivity in mind and may be offered in a variety of learning modes and with assessment to suit students' learning and other needs. (see paragraphs 1.19-1.32). Accounting degree programmes may achieve flexibility in a\n\n16\nvariety of ways, including the length of the degree programme (for example, whether to include a placement or study-abroad year), mode of study (full or part-time, in person or distance, or other modes or combinations of modes, their entry criteria, and modes of assessment."
  stem: none
  statementType: requirement
  rung: none
  force: should
  level: none
  appliesTo: "Accounting courses"
  addressee: provider
  verbs: ["designed", "offered", "achieve"]
  about: "inclusive flexibility of mode and length"
  themes: [none]
  domain: none
  award: ["none"]
  gradeOf: none
  paraphrase: "Courses should be planned with inclusion in mind and may vary learning mode and assessment to suit students; flexibility can come from length (a placement or study abroad year), mode (full or part-time, in person or distance), entry criteria and assessment."
  quote: full   # the issuer's statement is in `source` (D-std-0014)
  audience: practitioner
  subjects: inherited
- id: qaa/accounting-2025/2.23
  locator: { number: "2.23", headingPath: ["Distinctive features of the Accounting degree", "Partnership"] }
  span: { start: 58285, end: 58952 }
  source: "2.23 Degree-awarding bodies may deliver degree programmes in partnership with other providers or organisations. This Subject Benchmark Statement should be applied to ensure that Accounting degree programmes that include such partnerships are designed to ensure that the benchmark standards are met across the entire programme. Accounting degree programmes designed in partnership with providers or organisations should not be designed to meet the exemption and accreditation of PRSBs at the expense of broader design objectives (section 3). Further advice and guidance on working in partnership can be found in the UK Quality Code, Advice and Guidance: Partnerships ."
  stem: none
  statementType: requirement
  rung: none
  force: should
  level: none
  appliesTo: "Accounting courses"
  addressee: provider
  verbs: ["applied", "ensure", "met", "designed"]
  about: "standards across partnership delivery"
  themes: [none]
  domain: none
  award: ["none"]
  gradeOf: none
  paraphrase: "Degree-awarding bodies may deliver with partners; the statement should be applied so the standards are met across the whole partnership course, and courses designed with partners should not be built for PSRB exemption and accreditation at the cost of the broader aims."
  quote: full   # the issuer's statement is in `source` (D-std-0014)
  audience: practitioner
  subjects: inherited
- id: qaa/accounting-2025/2.26
  locator: { number: "2.26", headingPath: ["Distinctive features of the Accounting degree", "Partnership"] }
  span: { start: 60728, end: 61612 }
  source: "2.26 Professional statutory and regulatory bodies (PSRBs), particularly the professional accountancy bodies, are potentially important partners in the design of Accounting degree programmes. While Accounting degree programmes may be designed to reflect the requirements for recognition (accreditation or exemptions) by PSRBs, Accounting degrees sit in a contested space between being an academic degree (providing broad intellectual and conceptual development and future-looking knowledge of a broad range of aspects of accounting, reporting, assurance and accountability), and the professional requirements of various professional accountancy (and other) PSRBs (paragraph 1.7). All Accounting degree programmes should meet the benchmark standards outlined in this Subject Benchmark Statement rather than having content prescribed by PSRBs' accreditation requirements (paragraph 1.8)."
  stem: none
  statementType: requirement
  rung: none
  force: should
  level: none
  appliesTo: "Accounting courses"
  addressee: provider
  verbs: ["meet", "designed", "reflect"]
  about: "PSRBs as partners, not prescribers"
  themes: [none]
  domain: none
  award: ["none"]
  gradeOf: none
  paraphrase: "PSRBs, above all the professional accountancy bodies, can be important partners in design and courses may reflect their recognition requirements, but every Accounting degree should meet this statement's standards rather than have its content set by PSRB accreditation."
  quote: full   # the issuer's statement is in `source` (D-std-0014)
  audience: practitioner
  subjects: inherited
- id: qaa/accounting-2025/2.28
  locator: { number: "2.28", headingPath: ["Distinctive features of the Accounting degree", "Monitoring and review"] }
  span: { start: 61937, end: 63016 }
  source: "2.28 A major feature of academic quality assurance and enhancement in higher education institutions is having in place monitoring and regular review processes for the degree programmes it delivers. Monitoring and evaluation include both annual or continuous and periodic processes. Degree-awarding bodies, and their collaborative partnerships, routinely collect and analyse information, including information representing the student voice, and undertake reviews appropriate to their own needs and institutional norms. Degree-awarding bodies should draw on a range of external reference points, including relevant QAA Subject Benchmark Statements, to ensure that their provision aligns with sector norms. Suitable monitoring and evaluation processes normally include periodic assessment or (re)validation of degree programmes that are conducted internally with external experts or by external independent advisers. These evaluations typically use information from both current and historic monitoring to develop an understanding of student achievement and inform future planning."
  stem: none
  statementType: requirement
  rung: none
  force: should
  level: none
  appliesTo: "Accounting courses"
  addressee: provider
  verbs: ["draw", "ensure", "aligns"]
  about: "external reference points in review"
  themes: [none]
  domain: none
  award: ["none"]
  gradeOf: none
  paraphrase: "Monitoring and regular review are central to quality; degree-awarding bodies should use a range of external reference points, relevant subject statements among them, to keep provision in line with sector norms, through annual and periodic review with external input."
  quote: full   # the issuer's statement is in `source` (D-std-0014)
  audience: practitioner
  subjects: inherited
- id: qaa/accounting-2025/2.31
  locator: { number: "2.31", headingPath: ["Distinctive features of the Accounting degree", "Monitoring and review"] }
  span: { start: 63812, end: 64205 }
  source: "2.31 Monitoring and evaluation processes should ensure that important themes, including sustainable development (paragraphs 1.33-1.43), EDI (paragraphs 1.19-1.28), accessibility (paragraphs 1.29-1.32), enterprise and entrepreneurship (paragraphs 1.44-1.48), and GenAI (paragraphs 1.49-1.55), are embedded throughout the curriculum and are reflected in learning, teaching and assessment design."
  stem: none
  statementType: requirement
  rung: none
  force: should
  level: none
  appliesTo: "Accounting courses"
  addressee: provider
  verbs: ["ensure", "embedded", "reflected"]
  about: "monitoring the cross-cutting themes"
  themes: [none]
  domain: none
  award: ["none"]
  gradeOf: none
  paraphrase: "Monitoring and evaluation should check that sustainable development, EDI, accessibility, enterprise and entrepreneurship and GenAI run through the curriculum and show in learning, teaching and assessment design."
  quote: full   # the issuer's statement is in `source` (D-std-0014)
  audience: practitioner
  subjects: inherited
- id: qaa/accounting-2025/2.32
  locator: { number: "2.32", headingPath: ["Distinctive features of the Accounting degree", "Monitoring and review"] }
  span: { start: 64206, end: 65102 }
  source: "2.32 The external examining system currently in use across the UK higher education sector helps to ensure consistency in the way academic standards are secured by degree-awarding bodies. Typically, external examiners will be asked to comment on the types, principles and purposes of assessments being offered to students and to assess the adequacy of marking or grading. They will also typically consider the types of modules on offer to students, the outcomes of a cohort and how these compare to similar provisions offered and outcomes within other UK higher education providers. External examiners are asked to produce a report each year and make recommendations, for example concerning changes to modules and assessments. This Subject Benchmark Statement and other relevant Statements, particularly the benchmark standards, should play a key role in external examiners' evaluation and advice."
  stem: none
  statementType: requirement
  rung: none
  force: should
  level: none
  appliesTo: "Accounting courses"
  addressee: provider
  verbs: ["play"]
  about: "the statement in external examining"
  themes: [none]
  domain: none
  award: ["none"]
  gradeOf: none
  paraphrase: "External examiners help keep standards consistent across the sector by commenting on assessment, marking, modules and outcomes, and reporting yearly; this statement and others, especially their standards, should have a central place in their evaluation and advice."
  quote: full   # the issuer's statement is in `source` (D-std-0014)
  audience: practitioner
  subjects: inherited
- id: qaa/accounting-2025/2.33
  locator: { number: "2.33", headingPath: ["Distinctive features of the Accounting degree", "Monitoring and review"] }
  span: { start: 65103, end: 65576 }
  source: "2.33 Accounting degree programmes which are aligned with accounting or other PSRBs are typically subject to additional monitoring and evaluation from those PSRBs for exemption and accreditation (paragraphs 1.7-1.8). In these cases, monitoring and review typically involve a combination of site visits and desk-based reviews: Accounting degree programme providers should provide information to potential and current students about their routes to professional qualification."
  stem: none
  statementType: requirement
  rung: none
  force: should
  level: none
  appliesTo: "Accounting courses"
  addressee: provider
  verbs: ["provide"]
  about: "informing students about professional routes"
  themes: [none]
  domain: none
  award: ["none"]
  gradeOf: none
  paraphrase: "Courses aligned with PSRBs face extra monitoring by those bodies for exemption and accreditation, through visits and desk reviews; providers should tell prospective and current students about their routes to a professional qualification."
  quote: full   # the issuer's statement is in `source` (D-std-0014)
  audience: practitioner
  subjects: inherited
- id: qaa/accounting-2025/3.2
  locator: { number: "3.2", headingPath: ["Content, structure and delivery", "Knowledge, understanding and subject-specific skills"] }
  span: { start: 65996, end: 66363 }
  source: "3.2 The content of an Accounting degree programme should reflect the broad principles set out in section 1, Context and purposes of an Accounting degree. The main subject content should be shaped by the subsection Purposes and characteristics of an Accounting degree, and reflect the issues discussed in the cross-cutting themes subsections (paragraphs 1.19 to 1.55)."
  stem: none
  statementType: requirement
  rung: none
  force: should
  level: none
  appliesTo: "Accounting courses"
  addressee: provider
  verbs: ["reflect", "shaped"]
  about: "content shaped by section 1 and the themes"
  themes: [none]
  domain: none
  award: ["none"]
  gradeOf: none
  paraphrase: "Course content should follow section 1's principles, be shaped mainly by the purposes and characteristics subsection and reflect the cross-cutting themes."
  quote: full   # the issuer's statement is in `source` (D-std-0014)
  audience: practitioner
  subjects: inherited
- id: qaa/accounting-2025/3.3
  locator: { number: "3.3", headingPath: ["Content, structure and delivery", "Knowledge, understanding and subject-specific skills"] }
  span: { start: 66364, end: 66879 }
  source: "3.3 Accounting degree programmes should include significant coverage of the public interest role of accounting and accountability, the current and future needs of society, and the need to be critical of the status quo of accounting and encourage students to build capability to imagine futures for accounting that are different to those that are currently considered mainstream (paragraph 1.13). This requires Accounting degrees to instil a sense of responsibility and anticipation of change, underpinned by ethics."
  stem: none
  statementType: expectation
  rung: none
  force: should
  level: none
  appliesTo: "Accounting courses and their students"
  addressee: both
  verbs: ["include", "encourage", "build", "imagine", "instil"]
  about: "the public interest role of accounting"
  themes: [none]
  domain: understanding
  award: ["none"]
  gradeOf: none
  paraphrase: "Courses should give real weight to accounting's public interest role and accountability, society's present and future needs and critique of current accounting, encouraging students to imagine other futures; degrees need to instil responsibility and readiness for change, grounded in ethics."
  quote: full   # the issuer's statement is in `source` (D-std-0014)
  audience: both
  subjects: inherited
- id: qaa/accounting-2025/3.4
  locator: { number: "3.4", headingPath: ["Content, structure and delivery", "Knowledge, understanding and subject-specific skills"] }
  span: { start: 66880, end: 67443 }
  source: "3.4 Accounting degree programmes should foster critical discussion of accounting and accountability knowledge and understanding in a socioeconomic context and should be firmly based in the understanding that accounting is informed by perspectives from the social sciences (paragraph 1.4). Accounting degree programmes should go beyond a focus on profit and the measurement and accumulation of capital and reflect the broader role of accountability for sustainability, welfare and a range of social, environmental, political and other perspectives (paragraph 1.4)."
  stem: none
  statementType: expectation
  rung: none
  force: should
  level: none
  appliesTo: "Accounting courses and their students"
  addressee: both
  verbs: ["foster", "based", "reflect"]
  about: "critical, socially grounded study"
  themes: [none]
  domain: understanding
  award: ["none"]
  gradeOf: none
  paraphrase: "Courses should encourage critical discussion of accounting and accountability in their social and economic setting, rest on social science perspectives, and look past profit and capital to accountability for sustainability, welfare and social, environmental and political concerns."
  quote: full   # the issuer's statement is in `source` (D-std-0014)
  audience: both
  subjects: inherited
- id: qaa/accounting-2025/3.5
  locator: { number: "3.5", headingPath: ["Content, structure and delivery", "Knowledge, understanding and subject-specific skills"] }
  span: { start: 67444, end: 68021 }
  source: "3.5 Accounting degree programmes will be based on the understanding that accounting is a key form of information provision and control within and of many types of organisations, including governmental organisations (at many levels), charities, not-for-profits, co-operative, social enterprises, political, social pressure movements, as well as for-profit businesses and professional organisations (paragraph 1.4). Accounting degree programmes should include the application of accounting knowledge, understanding, skills and critique to a range of these types of organisations."
  stem: none
  statementType: expectation
  rung: none
  force: should
  level: none
  appliesTo: "Accounting courses and their students"
  addressee: both
  verbs: ["based", "include"]
  about: "accounting across many kinds of organisation"
  themes: [none]
  domain: subject-skill
  award: ["none"]
  gradeOf: none
  paraphrase: "Courses rest on accounting as a main form of information and control in many organisations (public, charitable, co-operative, social enterprise, campaigning and for-profit) and should include applying accounting knowledge, skills and critique to a range of them."
  quote: full   # the issuer's statement is in `source` (D-std-0014)
  audience: both
  subjects: inherited
- id: qaa/accounting-2025/3.6
  locator: { number: "3.6", headingPath: ["Content, structure and delivery", "Knowledge, understanding and subject-specific skills"] }
  span: { start: 68022, end: 68150 }
  source: "3.6 Accounting degree programmes should include both conceptual/theoretical and applied aspects of the subject (paragraph 1.14)."
  stem: none
  statementType: requirement
  rung: none
  force: should
  level: none
  appliesTo: "Accounting courses"
  addressee: provider
  verbs: ["include"]
  about: "conceptual and applied aspects"
  themes: [none]
  domain: none
  award: ["none"]
  gradeOf: none
  paraphrase: "Courses should cover both the conceptual and theoretical and the applied sides of accounting."
  quote: full   # the issuer's statement is in `source` (D-std-0014)
  audience: practitioner
  subjects: inherited
- id: qaa/accounting-2025/3.8
  locator: { number: "3.8", headingPath: ["Content, structure and delivery", "Knowledge, understanding and subject-specific skills"] }
  span: { start: 69014, end: 70010 }
  source: "3.8 Accounting degree programmes should not be just about numbers, and certainly not just about financial amounts; accounting is a discipline concerned with broad levels of accountability involving dealing with and reporting on substantial elements of non-financial\n\n20\ndata or information. Accounting degree programmes should prepare students to learn from the involvement of accounting in historical developments and to be able to take the opportunity, and the responsibility, to apply accounting knowledge and understanding and accounting-specific and transferable skills to guide organisations in navigating the complexities of the modern world. These complexities should include the role of accounting in sustainability challenges, evolving stakeholder expectations, engendering social and welfare issues (for example, modern slavery, war, injustices, human rights and decolonisation), and dealing with questions without answers and the ambiguity inherent in the real world (paragraph 1.10)."
  stem: none
  statementType: expectation
  rung: none
  force: should
  level: none
  appliesTo: "Accounting courses and their students"
  addressee: both
  verbs: ["prepare", "learn", "apply", "guide", "include"]
  about: "accounting beyond numbers in a complex world"
  themes: [none]
  domain: subject-skill
  award: ["none"]
  gradeOf: none
  paraphrase: "Courses should not be only about numbers or money, since accounting deals with accountability and much non-financial information; they should prepare students to learn from accounting's history and to apply their knowledge and skills to guide organisations through modern complexity, including sustainability, stakeholder expectations, social and welfare issues and questions with no settled answer."
  quote: full   # the issuer's statement is in `source` (D-std-0014)
  audience: both
  subjects: inherited
- id: qaa/accounting-2025/3.9
  locator: { number: "3.9", headingPath: ["Content, structure and delivery", "Knowledge, understanding and subject-specific skills"] }
  span: { start: 70011, end: 70688 }
  source: "3.9 Accounting degree programmes should incorporate appropriate subject-specific skills in order to ensure that graduates are able to understand accounting knowledge and are able to apply this in practical situations. These accounting-specific skills include, but are not restricted to, skills in recording and summarising transactions and other economic events; preparation of financial statements; analysis of the operations of business activities (for example, decision analysis, performance measurement, management control, budgeting and discounted cash flow analysis); and financial analysis and projections (for example, analysis of financial ratios and financial risks)."
  stem: none
  statementType: expectation
  rung: none
  force: should
  level: none
  appliesTo: "Accounting courses and their students"
  addressee: both
  verbs: ["incorporate", "understand", "apply"]
  about: "core accounting-specific skills"
  themes: [none]
  domain: subject-skill
  award: ["none"]
  gradeOf: none
  paraphrase: "Courses should build in subject-specific skills so students understand accounting knowledge and can apply it in practice, including recording and summarising transactions, preparing financial statements, analysing operations (decisions, performance, control, budgets, discounted cash flow) and financial analysis and projection."
  quote: full   # the issuer's statement is in `source` (D-std-0014)
  audience: both
  subjects: inherited
- id: qaa/accounting-2025/3.10
  locator: { number: "3.10", headingPath: ["Content, structure and delivery", "Knowledge, understanding and subject-specific skills"] }
  span: { start: 70689, end: 71859 }
  source: "3.10 Accounting degree programmes should include all of the following broad areas of knowledge, understanding and in situ skills, recognising that there is a high degree of overlap between these areas and accepting that different Accounting degree programmes will include them in different combinations. The content of all of these areas of knowledge and understanding should include, in local, national and global contexts: theoretical underpinnings; current practices; regulatory environments (jurisdictions); contemporary debates and controversies; and application in diverse and complex contexts, including the application of evidence-informed judgements in ambiguous situations. Many of these areas will be developed to different levels throughout the degree programme. However, it is important that these areas of knowledge and understanding are seen as integrated parts of accounting and accountability, and not as separate silos of knowledge and understanding. Each of these areas of knowledge and understanding potentially interact with a number of cross-cutting themes (paragraphs 1.19 to 1.55), and the implications of these interactions should be recognised."
  stem: none
  statementType: requirement
  rung: none
  force: should
  level: none
  appliesTo: "Accounting courses"
  addressee: provider
  verbs: ["include", "developed", "recognised"]
  about: "the broad areas of knowledge, integrated"
  themes: [none]
  domain: none
  award: ["none"]
  gradeOf: none
  paraphrase: "Courses should cover all of the broad areas listed, in varying combinations and with overlap; each area should include theory, current practice, regulation, current debate and application in complex settings with evidence-based judgement, in local, national and global contexts, developed to rising levels and taught as connected parts of accounting rather than separate silos, with their links to the themes recognised."
  quote: full   # the issuer's statement is in `source` (D-std-0014)
  audience: practitioner
  subjects: inherited
- id: qaa/accounting-2025/3.10.b1
  locator: { number: "3.10.b1", headingPath: ["Content, structure and delivery", "Knowledge, understanding and subject-specific skills"] }
  span: { start: 71860, end: 72392 }
  source: "a Accountability, responsibility and trust: Accounting helps organisations navigate challenging and competitive operating environments to ethically create sustainable value streams. Graduates (as accountants or in other professional capacities) have a responsibility to communicate in a transparent, reliable and responsible way to a broad range of stakeholders. An Accounting degree programme should equip students to recognise this position of trust, make better judgements, and provide assurance, guidance, advice and leadership."
  stem: "3.10"
  statementType: expectation
  rung: none
  force: should
  level: none
  appliesTo: "Accounting courses and their students"
  addressee: both
  verbs: ["equip", "recognise", "make", "provide"]
  about: "area a: accountability, responsibility and trust"
  themes: [none]
  domain: understanding
  award: ["none"]
  gradeOf: none
  paraphrase: "Area a: accounting helps organisations create sustainable value ethically, and accountants carry a duty to communicate openly and reliably to many stakeholders; a course should equip students to see this position of trust, judge well and give assurance, advice and leadership."
  quote: full   # the issuer's statement is in `source` (D-std-0014)
  audience: both
  subjects: inherited
- id: qaa/accounting-2025/3.10.b2
  locator: { number: "3.10.b2", headingPath: ["Content, structure and delivery", "Knowledge, understanding and subject-specific skills"] }
  span: { start: 72393, end: 72961 }
  source: "b Business, social and economic environment: An Accounting degree programme should consider the business, economic and social environment and graduates should demonstrate knowledge and understanding of the impact the environment has on a range of organisations and the impact of organisations on the environment. This encompasses organisations at a local, national and international level and includes, for example, a wide range of factors, including environmental, cultural, ethical, legal and regulatory, taxation, political, sociological, digital and technological."
  stem: "3.10"
  statementType: expectation
  rung: none
  force: should
  level: none
  appliesTo: "Accounting courses and their students"
  addressee: both
  verbs: ["consider", "demonstrate"]
  about: "area b: the business, social and economic environment"
  themes: [none]
  domain: knowledge
  award: ["none"]
  gradeOf: none
  paraphrase: "Area b: a course should look at the business, social and economic setting, and graduates should show they know how that environment affects organisations, and organisations it, locally to internationally, across environmental, cultural, ethical, legal, tax, political, social and technological factors."
  quote: full   # the issuer's statement is in `source` (D-std-0014)
  audience: both
  subjects: inherited
- id: qaa/accounting-2025/3.10.b3
  locator: { number: "3.10.b3", headingPath: ["Content, structure and delivery", "Knowledge, understanding and subject-specific skills"] }
  span: { start: 72962, end: 73999 }
  source: "c Ethics: Ethics is more than just knowing rules, it is about identifying ethical dilemmas,\n\n21\nunderstanding implications, making ethical and moral judgements and behaving appropriately. Ethics has implications broadly for organisations and society, but also has specific importance to accounting and accountability. Both of these aspects should be included in Accounting degree programmes. How, and to what extent, an organisation (business or otherwise) adopts an ethical approach has a significant impact on the way it operates and is perceived in the environment and on how performance measures or operational improvement can be interpreted. To develop responsible citizens and ethical professionals, ethics needs to be integrated throughout an Accounting degree programme to develop students' capacity to apply professional scepticism, to navigate complex ethical and moral situations, and to make ethical decisions that are in the public interest and that resonate with the common good, thereby contributing positively to society."
  stem: "3.10"
  statementType: expectation
  rung: none
  force: should
  level: none
  appliesTo: "Accounting courses and their students"
  addressee: both
  verbs: ["included", "integrated", "apply", "navigate", "make"]
  about: "area c: ethics"
  themes: [none]
  domain: subject-skill
  award: ["none"]
  gradeOf: none
  paraphrase: "Area c: ethics means spotting dilemmas, understanding their effects, judging and acting well, for organisations and society and for accounting in particular; both should be taught, woven through the degree so students can apply professional scepticism, handle complex moral situations and decide in the public interest."
  quote: full   # the issuer's statement is in `source` (D-std-0014)
  audience: both
  subjects: inherited
- id: qaa/accounting-2025/3.10.b4
  locator: { number: "3.10.b4", headingPath: ["Content, structure and delivery", "Knowledge, understanding and subject-specific skills"] }
  span: { start: 74000, end: 75169 }
  source: "d Organisational governance and corporate reporting: Reporting encompasses the preparation, analysis and interpretation (including financial statement analysis) of all aspects of reporting to a wide range of stakeholders, including financial statements, annual reports, chairman's statements, sustainability reports, employee reports, EDI reports, and other financial and non- financial reports (for example, biodiversity, climate change, modern day slavery statements). An Accounting degree programme should ensure that graduates have an understanding of how to apply relevant laws, regulations and professional standards (both regulatory and voluntary), including appropriate recording and accounting skills. Graduates should be aware of the important role of accounting in the context of corporate and organisational governance (including groups of companies or other organisations). Graduates should also have knowledge and understanding of contemporary theoretical developments and research in the field, as part of their ability to apply critical thinking and the use of evidence in the evaluation of practice from disciplinary and multidisciplinary perspectives."
  stem: "3.10"
  statementType: expectation
  rung: none
  force: should
  level: none
  appliesTo: "Accounting courses and their students"
  addressee: both
  verbs: ["ensure", "apply"]
  about: "area d: organisational governance and corporate reporting"
  themes: [none]
  domain: knowledge
  award: ["none"]
  gradeOf: none
  paraphrase: "Area d: reporting covers preparing, analysing and interpreting all reports to stakeholders, financial and non-financial; a course should make sure graduates can apply the laws, regulations and standards with sound recording skills, know accounting's role in governance (groups included) and know current theory and research so they can judge practice critically."
  quote: full   # the issuer's statement is in `source` (D-std-0014)
  audience: both
  subjects: inherited
- id: qaa/accounting-2025/3.10.b5
  locator: { number: "3.10.b5", headingPath: ["Content, structure and delivery", "Knowledge, understanding and subject-specific skills"] }
  span: { start: 75170, end: 76786 }
  source: "e Information for effective and impactful decision-making: Focuses on providing timely, relevant and insightful financial and non-financial information for planning, performance management, organisational control, project management, operational, strategic and broader decision-making. This includes methodologies for various type of decision-making (for example, treasury and working capital management, investment, competitive games, multi-criteria evaluation). It also includes analysing, interpreting and effectively communicating financial and non- financial information to decision-makers, and supporting strategic objectives, while recognising broader social and ecological impacts. It encompasses strategic management accounting, aligning accounting data with organisational and sustainability objectives. An Accounting degree programme should equip students to develop, implement and operate performance measurement systems, including key performance indicators; monitor and formulate budgets; and implement costing and valuation strategies. It will emphasise the importance of critical thinking; problem- solving (including in complex and novel situations, including cases with incomplete data, cases bound with ambiguity and problems without definitive answers); analytical skills; challenging students to anticipate potential risks and opportunities; and develop innovative solutions to address organisational challenges. It will also include leveraging technology and data analytics to enhance information accuracy, efficiency and effectiveness, and keep abreast of the latest developments in the field."
  stem: "3.10"
  statementType: expectation
  rung: none
  force: should
  level: none
  appliesTo: "Accounting courses and their students"
  addressee: both
  verbs: ["equip", "develop", "implement", "operate", "monitor", "formulate"]
  about: "area e: information for decision-making"
  themes: [none]
  domain: subject-skill
  award: ["none"]
  gradeOf: none
  paraphrase: "Area e: providing timely, relevant financial and non-financial information for planning, performance, control and strategy, including decision methods, communication to decision-makers and strategic management accounting; a course should equip students to build and run performance measurement systems and KPIs, set and track budgets, apply costing and valuation, solve problems with incomplete or ambiguous data, anticipate risks and use technology and analytics."
  quote: full   # the issuer's statement is in `source` (D-std-0014)
  audience: both
  subjects: inherited
- id: qaa/accounting-2025/3.10.b6
  locator: { number: "3.10.b6", headingPath: ["Content, structure and delivery", "Knowledge, understanding and subject-specific skills"] }
  span: { start: 76787, end: 77707 }
  source: "f Systems, processes and data structures: Data and the processing of that data is the core of accounting, therefore Accounting degree programmes need to include knowledge and understanding of the design, operation and control of systems to provide data and information (paragraph 1.11).\n\n22\nThis should include both traditional and technical accounting (for example, double entry bookkeeping, ledger accounting and the production of financial statements) and systems useful for broader non-financial and financial data to deal with the broader accountability for sustainability, social reporting and regulatory compliance. This requires that graduates understand, interrogate, analyse and be able to work with both structured and unstructured data, including an understanding of data structures (including those in relational databases, ERP and other organisational systems) containing complex organisational attributes."
  stem: "3.10"
  statementType: expectation
  rung: none
  force: should
  level: none
  appliesTo: "Accounting courses and their students"
  addressee: both
  verbs: ["include", "understand", "interrogate", "analyse"]
  about: "area f: systems, processes and data structures"
  themes: [none]
  domain: subject-skill
  award: ["none"]
  gradeOf: none
  paraphrase: "Area f: data and its processing are central, so courses need to cover how systems that supply data are designed, run and controlled, both traditional bookkeeping, ledgers and statements and wider systems for non-financial data, with graduates able to question, analyse and work with structured and unstructured data and the structures that hold it."
  quote: full   # the issuer's statement is in `source` (D-std-0014)
  audience: both
  subjects: inherited
- id: qaa/accounting-2025/3.10.b7
  locator: { number: "3.10.b7", headingPath: ["Content, structure and delivery", "Knowledge, understanding and subject-specific skills"] }
  span: { start: 77708, end: 78602 }
  source: "g The regulatory environment: Focuses on the regulations and norms governing accounting, the accounting profession, business and other accountable organisations in all sectors. A knowledge and understanding of the regulatory environment enables graduates to understand the importance of financial system integrity and organisational governance. It includes interpreting and applying corporate governance codes, sustainability reporting requirements, tax laws and ethical considerations. It also explores the importance of sustainability (including environmental, social and governance) reporting and the integration of sustainability considerations into accounting practices (paragraphs 1.33- 1.43), as well as fostering an understanding of how ethical considerations are incorporated into the regulatory environment and the importance of equity, diversity and inclusion (paragraphs 1.19-1.28)."
  stem: "3.10"
  statementType: expectation
  rung: none
  force: must   # D-std-0016: "requirements" read as must
  level: none
  appliesTo: "Accounting courses and their students"
  addressee: both
  verbs: ["understand", "interpreting", "applying"]
  about: "area g: the regulatory environment"
  themes: [none]
  domain: knowledge
  award: ["none"]
  gradeOf: none
  paraphrase: "Area g: the rules and norms governing accounting, the profession and accountable organisations in every sector, which let graduates see why financial system integrity and governance matter, covering governance codes, sustainability reporting rules, tax law and ethics, sustainability reporting and EDI."
  quote: full   # the issuer's statement is in `source` (D-std-0014)
  audience: both
  subjects: inherited
- id: qaa/accounting-2025/3.10.b8
  locator: { number: "3.10.b8", headingPath: ["Content, structure and delivery", "Knowledge, understanding and subject-specific skills"] }
  span: { start: 78603, end: 79500 }
  source: "h Audit and assurance: Accounting degree programmes should be designed to instil students with the requisite knowledge and understanding to prepare, as well as empower them to deliver, quality audit and assurance services that boost trust, integrity and transparency in financial and non-financial reporting, data transfers and other communications to various stakeholders. Central to this is the cultivation of professional scepticism and critical thinking, understanding the public interest responsibility of the accounting profession, empowering students to discern risks and make informed professional judgements. Accounting degree programmes should, unequivocally, foster the essential importance of professional ethics, accountability and responsibility for graduates to navigate audit practice, standards and processes with confidence and proficiency in local, national and global contexts."
  stem: "3.10"
  statementType: expectation
  rung: none
  force: should
  level: none
  appliesTo: "Accounting courses and their students"
  addressee: both
  verbs: ["designed", "instil", "prepare", "deliver", "foster", "navigate"]
  about: "area h: audit and assurance"
  themes: [none]
  domain: subject-skill
  award: ["none"]
  gradeOf: none
  paraphrase: "Area h: courses should give students the knowledge to prepare for, and deliver, good audit and assurance that strengthens trust and transparency in financial and non-financial reporting, centred on scepticism, critical thinking, the public interest and professional judgement, and should firmly promote professional ethics so graduates can handle audit practice and standards confidently."
  quote: full   # the issuer's statement is in `source` (D-std-0014)
  audience: both
  subjects: inherited
- id: qaa/accounting-2025/3.10.b9
  locator: { number: "3.10.b9", headingPath: ["Content, structure and delivery", "Knowledge, understanding and subject-specific skills"] }
  span: { start: 79501, end: 80724 }
  source: "i Taxation: It is essential that Accounting degree programmes equip students with knowledge and understanding to navigate the principles, practices and complexities of taxation systems in a tax-conscious society. This enables graduates to play a meaningful role in societal well-being, fostering an appreciation of the implications on economic and social welfare and the purposes of taxation. Taxation content also serves as a crucial tool in cultivating awareness of the ethical and legal repercussions associated with policies/regulations, non-compliance and illicit tax practices. Accounting degree programmes should champion a culture of transparency, responsibility and accountability, and support the integrity of tax systems, and foster an environment conducive to ethically informed financial planning and decision-making. Accounting degree programmes should encompass a diverse array of taxation topics, ensuring that students are adept at facing local, national and global challenges. This should include, at a minimum, a knowledge and understanding of the nuances of pervasive UK taxes such as income tax, National Insurance contributions, capital gains tax, inheritance tax, corporation tax and value-added tax."
  stem: "3.10"
  statementType: expectation
  rung: none
  force: should
  level: none
  appliesTo: "Accounting courses and their students"
  addressee: both
  verbs: ["equip", "navigate", "champion", "support", "foster", "encompass", "include"]
  about: "area i: taxation"
  themes: [none]
  domain: knowledge
  award: ["none"]
  gradeOf: none
  paraphrase: "Area i: it is essential that courses equip students to handle the principles and complexity of tax and its social and economic purposes, the ethics and law of compliance and avoidance, and should promote transparency and the integrity of tax systems; at the least they should cover the main UK taxes, including income tax, National Insurance, capital gains, inheritance, corporation tax and VAT."
  quote: full   # the issuer's statement is in `source` (D-std-0014)
  audience: both
  subjects: inherited
- id: qaa/accounting-2025/3.10.b10
  locator: { number: "3.10.b10", headingPath: ["Content, structure and delivery", "Knowledge, understanding and subject-specific skills"] }
  span: { start: 80729, end: 81977 }
  source: "j Uncertainty and risk management: An Accounting degree programme should prepare graduates to navigate the complexities of a range of organisational environments, including an appreciation of the importance of risk and uncertainty. Uncertainty and risk management are intrinsic to all decision-making and accounting and reporting practices. An Accounting degree programme should ensure that graduates have a knowledge and understanding of risk and uncertainty, and how to differentiate between these, including dealing with financial unpredictability, ambiguity, safeguarding of assets, and ensuring compliance. A critical understanding of these aspects is necessary for strategic decision-making and enhancing an organisation's resilience and adaptability in a dynamic business, economic and social environment. Graduates should have an understanding of appropriate risk and uncertainty management and mitigation practices, and be able to apply appropriate techniques to a range of accounting and decision-making situations, including, for example, risk appetite/culture, scenario planning, game theory, decision trees and forecasting. Accounting graduates should also be able to advise on appropriate data to use within such risk analysis models."
  stem: "3.10"
  statementType: expectation
  rung: none
  force: should
  level: none
  appliesTo: "Accounting courses and their students"
  addressee: both
  verbs: ["prepare", "navigate", "ensure", "differentiate", "apply", "advise"]
  about: "area j: uncertainty and risk management"
  themes: [none]
  domain: subject-skill
  award: ["none"]
  gradeOf: none
  paraphrase: "Area j: courses should prepare graduates for the complexity of organisational settings, with knowledge of risk and uncertainty and how they differ, of protecting assets and compliance, and of management and mitigation, so they can apply techniques such as risk appetite, scenario planning, game theory, decision trees and forecasting and advise on the data to use."
  quote: full   # the issuer's statement is in `source` (D-std-0014)
  audience: both
  subjects: inherited
- id: qaa/accounting-2025/3.10.b11
  locator: { number: "3.10.b11", headingPath: ["Content, structure and delivery", "Knowledge, understanding and subject-specific skills"] }
  span: { start: 81978, end: 82765 }
  source: "k Data analytics and statistics: These are important within Accounting degree programmes from the perspective of both informing decision-making and in understanding research, including academic research papers, in the field. Data analytics and statistics enable the interpretation of large datasets, the testing of hypotheses, the detection of anomalies, and identification of trends in data which can be important in corporate reporting and audit and assurance. The incorporation of coding, search techniques and strategies, AI and machine learning techniques can also be important in contemporary data analytics. Accounting degree programmes should include knowledge, understanding and application skills for a variety of these techniques, including critical interpretation of results."
  stem: "3.10"
  statementType: expectation
  rung: none
  force: should
  level: none
  appliesTo: "Accounting courses and their students"
  addressee: both
  verbs: ["include"]
  about: "area k: data analytics and statistics"
  themes: [none]
  domain: subject-skill
  award: ["none"]
  gradeOf: none
  paraphrase: "Area k: analytics and statistics inform decisions and help in reading research; they allow large datasets to be interpreted, hypotheses tested and anomalies and trends found, with coding, search, AI and machine learning increasingly relevant; courses should include knowledge and applied skill in a range of these, with critical interpretation of results."
  quote: full   # the issuer's statement is in `source` (D-std-0014)
  audience: both
  subjects: inherited
- id: qaa/accounting-2025/3.10.b12
  locator: { number: "3.10.b12", headingPath: ["Content, structure and delivery", "Knowledge, understanding and subject-specific skills"] }
  span: { start: 82766, end: 84227 }
  source: "l Financial markets and institutions: Knowledge and understanding of financial markets and institutions are an essential element of an Accounting degree programme, as accounting (particularly traditional corporate reporting) is a major element of the operation of financial markets and organisational interactions with financial institutions. The extent to which this area is covered will be highly dependent on the structure of the degree programme. However, at a minimum, it is expected that an Accounting degree programme will include knowledge, understanding and subject-specific skills in the following areas: time value of money, the nature and sources of corporate and organisational finance, capital markets and instruments, project finance, the role of the stock exchange and other financial markets, asset pricing, corporate finance, alternative sources of finance, behavioural finance, personal finance and ethics in finance. Other topics in finance may be included, for example: other financial instruments and markets; global financial markets; fintech and financial innovation; mergers and acquisitions; liquidity management valuation techniques; credit analysis and management; insurance and risk financing; pension and retirement planning; public finance; financial crisis and economic downturns; futures and options; international banking. The content and nature of these topic areas are detailed in the Subject Benchmark Statement for Finance."
  stem: "3.10"
  statementType: expectation
  rung: none
  force: will
  level: none
  appliesTo: "Accounting courses and their students"
  addressee: both
  verbs: ["include"]
  about: "area l: financial markets and institutions"
  themes: [none]
  domain: knowledge
  award: ["none"]
  gradeOf: none
  paraphrase: "Area l: knowledge of financial markets and institutions is essential because accounting is central to how markets work; coverage depends on the degree, but at minimum a course is expected to include the time value of money, sources of finance, capital markets and instruments, project and corporate finance, stock exchanges, asset pricing, alternative, behavioural and personal finance and ethics in finance, with further topics optional."
  quote: full   # the issuer's statement is in `source` (D-std-0014)
  audience: both
  subjects: inherited
- id: qaa/accounting-2025/3.12
  locator: { number: "3.12", headingPath: ["Content, structure and delivery", "Transferable, professional and practice skills"] }
  span: { start: 84555, end: 84738 }
  source: "3.12 The skills required of a student completing an Accounting degree programme should reflect the broad principles set out in section 1, Context and purposes of an Accounting degree."
  stem: none
  statementType: requirement
  rung: none
  force: should
  level: none
  appliesTo: "Accounting courses"
  addressee: provider
  verbs: ["reflect"]
  about: "skills shaped by section 1"
  themes: [none]
  domain: none
  award: ["none"]
  gradeOf: none
  paraphrase: "The skills asked of a student completing the degree should follow the broad principles of section 1."
  quote: full   # the issuer's statement is in `source` (D-std-0014)
  audience: practitioner
  subjects: inherited
- id: qaa/accounting-2025/3.13
  locator: { number: "3.13", headingPath: ["Content, structure and delivery", "Transferable, professional and practice skills"] }
  span: { start: 84739, end: 85139 }
  source: "3.13 In an Accounting degree programme, students should develop skills that equip them to demonstrate, apply and operationalise their knowledge and understanding (paragraphs 3.2- 3.11), including appropriate technical accounting skills, remain mindful of their context, including the cross-cutting themes (paragraphs 1.19-1.55), and enable them to act in an ethical way (for example, paragraph 1.37)."
  stem: none
  statementType: outcome
  rung: none
  force: should
  level: fheq:6
  appliesTo: "students of the subject"
  addressee: learner
  verbs: ["develop", "demonstrate", "apply", "operationalise", "act"]
  about: "skills that put knowledge into action"
  themes: [none]
  domain: generic-skill
  award: ["bachelor's with honours"]
  gradeOf: none
  paraphrase: "Students should develop skills to show, apply and put into practice their knowledge and understanding, technical accounting skills included, to stay alert to context and the themes, and to act ethically."
  quote: full   # the issuer's statement is in `source` (D-std-0014)
  audience: both
  subjects: inherited
- id: qaa/accounting-2025/3.15.b1
  locator: { number: "3.15.b1", headingPath: ["Content, structure and delivery", "Transferable, professional and practice skills"] }
  span: { start: 85898, end: 86228 }
  source: "m Communication: including effective presentation of quantitative and qualitative data and information, together with analysis, argument and commentary, in a form appropriate to intended audiences and a range of stakeholders, and in a range of forms, including verbal and/or non-verbal, written and visual, using a range of media."
  stem: "3.15"
  statementType: outcome
  rung: none
  force: must   # D-std-0016: "is expected to" read as must
  level: fheq:6
  appliesTo: "graduates of the subject"
  addressee: learner
  verbs: ["including"]
  about: "skill m: communication"
  themes: [none]
  domain: generic-skill
  award: ["bachelor's with honours"]
  gradeOf: none
  paraphrase: "Skill m: presenting quantitative and qualitative data, analysis and argument to suit different audiences and stakeholders, in spoken, written, visual and other forms and media."
  quote: full   # the issuer's statement is in `source` (D-std-0014)
  audience: both
  subjects: inherited
- id: qaa/accounting-2025/3.15.b2
  locator: { number: "3.15.b2", headingPath: ["Content, structure and delivery", "Transferable, professional and practice skills"] }
  span: { start: 86229, end: 86677 }
  source: "n Collaboration: including interpersonal skills of effective listening, negotiating, persuasion and communication to enable boundary-spanning, influencing, relational and inclusive collaborative working with others and leadership. This should include ability to work in an inclusive and emotionally intelligent manner in a range of group and teamwork settings and may include collaboration with people in other organisations and other stakeholders."
  stem: "3.15"
  statementType: outcome
  rung: none
  force: must   # D-std-0016: "is expected to" read as must
  level: fheq:6
  appliesTo: "graduates of the subject"
  addressee: learner
  verbs: ["enable"]
  about: "skill n: collaboration"
  themes: [none]
  domain: generic-skill
  award: ["bachelor's with honours"]
  gradeOf: none
  paraphrase: "Skill n: listening, negotiating, persuading and communicating so as to work across boundaries, influence and collaborate inclusively and lead, including emotionally intelligent teamwork and work with other organisations and stakeholders."
  quote: full   # the issuer's statement is in `source` (D-std-0014)
  audience: both
  subjects: inherited
- id: qaa/accounting-2025/3.15.b3
  locator: { number: "3.15.b3", headingPath: ["Content, structure and delivery", "Transferable, professional and practice skills"] }
  span: { start: 86678, end: 87113 }
  source: "o Self-efficacy and lifelong learning: self-efficacy refers to an ability and belief in one's own ability (Bandura, 1997), including reflection and proactive commitment to independent action. Self-efficacy is closely associated with the skill of self-managed lifelong learning, including taking responsibility for one's own development and the consequences of actions, ethical decision-making, resilience and the ability to prioritise."
  stem: "3.15"
  statementType: outcome
  rung: none
  force: must   # D-std-0016: "is expected to" read as must
  level: fheq:6
  appliesTo: "graduates of the subject"
  addressee: learner
  verbs: ["including"]
  about: "skill o: self-efficacy and lifelong learning"
  themes: [none]
  domain: generic-skill
  award: ["bachelor's with honours"]
  gradeOf: none
  paraphrase: "Skill o: belief in and ability to act on one's own capacity, with reflection and commitment to independent action, tied to self-managed lifelong learning: owning one's development and the results of one's actions, ethical decisions, resilience and prioritising."
  quote: full   # the issuer's statement is in `source` (D-std-0014)
  audience: both
  subjects: inherited
- id: qaa/accounting-2025/3.15.b4
  locator: { number: "3.15.b4", headingPath: ["Content, structure and delivery", "Transferable, professional and practice skills"] }
  span: { start: 87114, end: 87554 }
  source: "p Critical thinking and scepticism: including critical and reflective evaluation of evidence, arguments, accounting theory and research. Critical thinking skills include judgement (including in situations of uncertainty where there is ambiguity and there are not necessarily clear solutions), scepticism (as an application of critical thinking), considering the nature of rationality, reflection and adopting an ethical and activist stance."
  stem: "3.15"
  statementType: outcome
  rung: none
  force: must   # D-std-0016: "is expected to" read as must
  level: fheq:6
  appliesTo: "graduates of the subject"
  addressee: learner
  verbs: ["including"]
  about: "skill p: critical thinking and scepticism"
  themes: [none]
  domain: generic-skill
  award: ["bachelor's with honours"]
  gradeOf: none
  paraphrase: "Skill p: critical and reflective evaluation of evidence, argument, theory and research, including judgement under uncertainty and ambiguity, scepticism as applied critical thinking, the nature of rationality, reflection and an ethical, activist stance."
  quote: full   # the issuer's statement is in `source` (D-std-0014)
  audience: both
  subjects: inherited
- id: qaa/accounting-2025/3.15.b5
  locator: { number: "3.15.b5", headingPath: ["Content, structure and delivery", "Transferable, professional and practice skills"] }
  span: { start: 87555, end: 87847 }
  source: "q Problem solving/reasoning: analysing data and information in structured and unstructured situations to determine potential causes of a problem, analysing alternative courses of action (including ethical reasoning), interpretation and selecting appropriate ethical and sustainable solutions."
  stem: "3.15"
  statementType: outcome
  rung: none
  force: must   # D-std-0016: "is expected to" read as must
  level: fheq:6
  appliesTo: "graduates of the subject"
  addressee: learner
  verbs: ["analysing", "selecting"]
  about: "skill q: problem solving and reasoning"
  themes: [none]
  domain: generic-skill
  award: ["bachelor's with honours"]
  gradeOf: none
  paraphrase: "Skill q: analysing data and information in structured and messy situations to find a problem's likely causes, weighing alternative actions with ethical reasoning, and choosing ethical and sustainable solutions."
  quote: full   # the issuer's statement is in `source` (D-std-0014)
  audience: both
  subjects: inherited
- id: qaa/accounting-2025/3.15.b6
  locator: { number: "3.15.b6", headingPath: ["Content, structure and delivery", "Transferable, professional and practice skills"] }
  span: { start: 87848, end: 88364 }
  source: "r Data analysis: including identification, collection and verification of data from a range of (referenced) sources in structured and unstructured forms, filtering, evaluation and\n\n25\ninterpretation of data and drawing reasoned conclusions. This would include analysis for complex or real-world problems, with incomplete data and ambiguous objectives. Data analysis should consider communication to ensure findings are presented in an appropriate form for the intended audience, potentially including visualisations."
  stem: "3.15"
  statementType: outcome
  rung: none
  force: must   # D-std-0016: "is expected to" read as must
  level: fheq:6
  appliesTo: "graduates of the subject"
  addressee: learner
  verbs: ["including", "consider"]
  about: "skill r: data analysis"
  themes: [none]
  domain: generic-skill
  award: ["bachelor's with honours"]
  gradeOf: none
  paraphrase: "Skill r: identifying, collecting and checking data from referenced sources in varied forms, then filtering, evaluating and interpreting it to reach reasoned conclusions, including for complex real problems with incomplete data and unclear aims, and presenting findings suitably, visualisations included."
  quote: full   # the issuer's statement is in `source` (D-std-0014)
  audience: both
  subjects: inherited
- id: qaa/accounting-2025/3.15.b7
  locator: { number: "3.15.b7", headingPath: ["Content, structure and delivery", "Transferable, professional and practice skills"] }
  span: { start: 88365, end: 89011 }
  source: "s Systems thinking: which provides ways of looking at the operation of processes that acknowledges the interconnectedness between different systems (processes and activities) and represents a holistic way of understanding the processes and structures that underlie complex situations, including, for example, accounting and management control systems. It therefore includes analysis, design, implementation, communication, evaluation, improvement and innovation of systems that provide data for reporting and decision-making, including the mitigation of risk, error, fraud and cyber risks, and aspects of resilience, sustainability and assurance."
  stem: "3.15"
  statementType: outcome
  rung: none
  force: must   # D-std-0016: "is expected to" read as must
  level: fheq:6
  appliesTo: "graduates of the subject"
  addressee: learner
  verbs: ["provides", "includes"]
  about: "skill s: systems thinking"
  themes: [none]
  domain: generic-skill
  award: ["bachelor's with honours"]
  gradeOf: none
  paraphrase: "Skill s: seeing processes as interconnected systems and understanding the structures beneath complex situations, such as accounting and control systems, including analysing, designing, running, communicating, evaluating and improving systems that supply data, and managing risk, error, fraud and cyber threats, resilience, sustainability and assurance."
  quote: full   # the issuer's statement is in `source` (D-std-0014)
  audience: both
  subjects: inherited
- id: qaa/accounting-2025/3.15.b8
  locator: { number: "3.15.b8", headingPath: ["Content, structure and delivery", "Transferable, professional and practice skills"] }
  span: { start: 89012, end: 89382 }
  source: "t Digital literacy: including skills to utilise and evaluate the sources, context, ability to manipulate and communicate data in all its forms, including questions of storage, control and cybersecurity. Ability to use and evaluate a range of contemporary technologies, including spreadsheets, databases and AI, as they emerge, in relation to their effective use of data."
  stem: "3.15"
  statementType: outcome
  rung: none
  force: must   # D-std-0016: "is expected to" read as must
  level: fheq:6
  appliesTo: "graduates of the subject"
  addressee: learner
  verbs: ["including", "use", "evaluate"]
  about: "skill t: digital literacy"
  themes: [none]
  domain: generic-skill
  award: ["bachelor's with honours"]
  gradeOf: none
  paraphrase: "Skill t: using and evaluating sources and contexts of data, handling and communicating it in all forms, with attention to storage, control and cyber security, and using and assessing current technologies such as spreadsheets, databases and AI as they emerge."
  quote: full   # the issuer's statement is in `source` (D-std-0014)
  audience: both
  subjects: inherited
- id: qaa/accounting-2025/3.15.b9
  locator: { number: "3.15.b9", headingPath: ["Content, structure and delivery", "Transferable, professional and practice skills"] }
  span: { start: 89383, end: 89518 }
  source: "u Numeracy: the use of quantitative skills to manipulate data, evaluate, estimate and model business problems, functions and phenomena."
  stem: "3.15"
  statementType: outcome
  rung: none
  force: must   # D-std-0016: "is expected to" read as must
  level: fheq:6
  appliesTo: "graduates of the subject"
  addressee: learner
  verbs: ["use", "manipulate", "evaluate", "estimate", "model"]
  about: "skill u: numeracy"
  themes: [none]
  domain: generic-skill
  award: ["bachelor's with honours"]
  gradeOf: none
  paraphrase: "Skill u: applying quantitative skills to work with data and to estimate, evaluate and model business problems, functions and phenomena."
  quote: full   # the issuer's statement is in `source` (D-std-0014)
  audience: both
  subjects: inherited
- id: qaa/accounting-2025/3.15.b10
  locator: { number: "3.15.b10", headingPath: ["Content, structure and delivery", "Transferable, professional and practice skills"] }
  span: { start: 89519, end: 89751 }
  source: "v Entrepreneurialism: including commercial awareness and business acumen, demonstrating innovation, creativity, flexibility, awareness of public interest (paragraph 1.13) and enterprise/entrepreneurial skills (paragraphs 1.44-1.48)."
  stem: "3.15"
  statementType: outcome
  rung: none
  force: must   # D-std-0016: "is expected to" read as must
  level: fheq:6
  appliesTo: "graduates of the subject"
  addressee: learner
  verbs: ["including", "demonstrating"]
  about: "skill v: entrepreneurialism"
  themes: [none]
  domain: generic-skill
  award: ["bachelor's with honours"]
  gradeOf: none
  paraphrase: "Skill v: commercial awareness and business acumen, shown through innovation, creativity, flexibility, regard for the public interest and enterprise skills."
  quote: full   # the issuer's statement is in `source` (D-std-0014)
  audience: both
  subjects: inherited
- id: qaa/accounting-2025/3.15.b11
  locator: { number: "3.15.b11", headingPath: ["Content, structure and delivery", "Transferable, professional and practice skills"] }
  span: { start: 89752, end: 90073 }
  source: "w Cultural awareness: an ability to appreciate cultural differences and the potential impact of these, for example on the discipline, on study, and on business and organisations. For programmes with a work or study abroad component (for example, Accounting with a language), foreign language capability is also important."
  stem: "3.15"
  statementType: outcome
  rung: none
  force: must   # D-std-0016: "is expected to" read as must
  level: fheq:6
  appliesTo: "graduates of the subject"
  addressee: learner
  verbs: ["appreciate"]
  about: "skill w: cultural awareness"
  themes: [none]
  domain: generic-skill
  award: ["bachelor's with honours"]
  gradeOf: none
  paraphrase: "Skill w: appreciating cultural differences and their possible effects on the discipline, on study and on organisations; where a course includes work or study abroad, ability in another language matters too."
  quote: full   # the issuer's statement is in `source` (D-std-0014)
  audience: both
  subjects: inherited
- id: qaa/accounting-2025/3.15.b12
  locator: { number: "3.15.b12", headingPath: ["Content, structure and delivery", "Transferable, professional and practice skills"] }
  span: { start: 90074, end: 90574 }
  source: "x Research: the ability to bring together a number of the skills previously discussed to undertake a systematic and robust investigation to reach an informed conclusion about a particular situation or issue of importance. It involves engaging critically with academic and other literature, identifying credible sources, formulating relevant questions, undertaking analysis, project management, presenting findings and clear communication, in order to enhance knowledge and drive innovation or change."
  stem: "3.15"
  statementType: outcome
  rung: none
  force: must   # D-std-0016: "is expected to" read as must
  level: fheq:6
  appliesTo: "graduates of the subject"
  addressee: learner
  verbs: ["undertake", "reach"]
  about: "skill x: research"
  themes: [none]
  domain: generic-skill
  award: ["bachelor's with honours"]
  gradeOf: none
  paraphrase: "Skill x: combining earlier skills to carry out a systematic, robust investigation that reaches an informed conclusion on an issue: engaging critically with literature, finding credible sources, framing questions, analysing, managing the project and presenting findings clearly, to add knowledge or drive change."
  quote: full   # the issuer's statement is in `source` (D-std-0014)
  audience: both
  subjects: inherited
- id: qaa/accounting-2025/3.16
  locator: { number: "3.16", headingPath: ["Content, structure and delivery", "Learning and teaching"] }
  span: { start: 90597, end: 90988 }
  source: "3.16 The learning and teaching strategies employed in Accounting degree programmes will be designed to allow students to develop conceptual and applied knowledge and understanding of the discipline, to develop higher level intellectual (cognitive) skills, technical accounting skills and professional and transferable (soft) skills that are relevant to the discipline (paragraphs 3.12-3.15)."
  stem: none
  statementType: requirement
  rung: none
  force: will
  level: none
  appliesTo: "Accounting courses"
  addressee: provider
  verbs: ["designed", "allow", "develop"]
  about: "learning and teaching strategy"
  themes: [none]
  domain: none
  award: ["none"]
  gradeOf: none
  paraphrase: "Learning and teaching strategies will be designed so students build conceptual and applied knowledge, higher-order thinking, technical accounting skills and relevant professional and transferable skills."
  quote: full   # the issuer's statement is in `source` (D-std-0014)
  audience: practitioner
  subjects: inherited
- id: qaa/accounting-2025/3.17
  locator: { number: "3.17", headingPath: ["Content, structure and delivery", "Learning and teaching"] }
  span: { start: 90989, end: 91546 }
  source: "3.17 The methods of learning and teaching will be designed so that the learning activities are aligned with intended learning outcomes or learning objectives of the programme, and there should be coherence between learning and teaching and assessment. Learning and teaching activities should consider the need to achieve an appropriate balance between the conceptual (including theoretical) and applied aspects of the subject and should promote continuous learning and enquiry, instilling in students an appetite to become lifelong learners (paragraph 1.9)."
  stem: none
  statementType: requirement
  rung: none
  force: will
  level: none
  appliesTo: "Accounting courses"
  addressee: provider
  verbs: ["designed", "consider", "promote"]
  about: "constructive alignment and balance"
  themes: [none]
  domain: none
  award: ["none"]
  gradeOf: none
  paraphrase: "Methods will be designed so activities align with intended outcomes, and teaching should be coherent with assessment, balance conceptual and applied study and encourage continuous learning and enquiry, giving students an appetite for lifelong learning."
  quote: full   # the issuer's statement is in `source` (D-std-0014)
  audience: practitioner
  subjects: inherited
- id: qaa/accounting-2025/3.18
  locator: { number: "3.18", headingPath: ["Content, structure and delivery", "Learning and teaching"] }
  span: { start: 91551, end: 91988 }
  source: "3.18 Learning and teaching should be designed to support the development of skills, competencies, attitudes and experiences which support students in becoming employable professionals and responsible citizens. Some Accounting degree programmes allow or require students to undertake a work-based internship or placement, which provides students with opportunities to apply their learning in the outside world and to enhance their skills."
  stem: none
  statementType: expectation
  rung: none
  force: should
  level: none
  appliesTo: "Accounting courses and their students"
  addressee: both
  verbs: ["designed", "support"]
  about: "employability and responsible citizenship"
  themes: [none]
  domain: none
  award: ["none"]
  gradeOf: none
  paraphrase: "Learning and teaching should be designed to build skills, competencies, attitudes and experiences that help students become employable professionals and responsible citizens; some courses allow or require a placement for applying learning outside."
  quote: full   # the issuer's statement is in `source` (D-std-0014)
  audience: both
  subjects: inherited
- id: qaa/accounting-2025/3.19
  locator: { number: "3.19", headingPath: ["Content, structure and delivery", "Learning and teaching"] }
  span: { start: 91989, end: 92505 }
  source: "3.19 Different pedagogic approaches can be adopted in teaching Accounting, including the use of dialogic, critical, reflexive, constructivist and collaborative pedagogies, or a blend of these. The pedagogies adopted should result in 'deep learning', whereby students are required to think critically about newly learned concepts, as opposed to 'shallow' or rote learning. The pedagogical approach should inform the choice of assessment methods and encourage student's intellectual development (paragraphs 3.27-3.43)."
  stem: none
  statementType: requirement
  rung: none
  force: should
  level: none
  appliesTo: "Accounting courses"
  addressee: provider
  verbs: ["adopted", "result", "inform", "encourage"]
  about: "pedagogy for deep learning"
  themes: [none]
  domain: none
  award: ["none"]
  gradeOf: none
  paraphrase: "Teaching may draw on critical, dialogic, reflexive, collaborative and constructivist approaches, alone or mixed; whatever is chosen should lead to deep learning, in which students think critically about new concepts, rather than rote learning, and should guide assessment choices and intellectual growth."
  quote: full   # the issuer's statement is in `source` (D-std-0014)
  audience: practitioner
  subjects: inherited
- id: qaa/accounting-2025/3.20
  locator: { number: "3.20", headingPath: ["Content, structure and delivery", "Learning and teaching"] }
  span: { start: 92506, end: 93279 }
  source: "3.20 A diversity of learning and teaching approaches should be encouraged within modules (units) and across degree programmes. These include face-to-face lectures, seminars, workshops and tutorials; blended learning involving a mix of online and face-to-face elements, and appropriate use of synchronous and asynchronous materials; active learning; and other innovative ways of designing learning. Some of the design elements may offer greater flexibility for students and educators. Digital technologies can be important in the delivery of learning and teaching in Accounting degree programmes, particularly as they are widely used in practice. The teaching and approaches and pedagogies adopted should be designed to encourage student engagement and active participation."
  stem: none
  statementType: requirement
  rung: none
  force: should
  level: none
  appliesTo: "Accounting courses"
  addressee: provider
  verbs: ["encouraged", "designed"]
  about: "diverse and active teaching approaches"
  themes: [none]
  domain: none
  award: ["none"]
  gradeOf: none
  paraphrase: "A range of approaches should be encouraged within and across modules, from lectures, seminars, workshops and tutorials to blended, active and innovative learning; digital technologies matter because practice uses them, and approaches should be designed for engagement and active participation."
  quote: full   # the issuer's statement is in `source` (D-std-0014)
  audience: practitioner
  subjects: inherited
- id: qaa/accounting-2025/3.22
  locator: { number: "3.22", headingPath: ["Content, structure and delivery", "Learning and teaching"] }
  span: { start: 93682, end: 94294 }
  source: "3.22 As an Accounting degree programme should prepare students to understand the design and operation of systems to provide data and information (paragraph 1.11), it is highly likely that it will be necessary to design into the learning and teaching approaches the use of appropriate digital technologies; for example cloud-based accounting packages, data acquisition and cleaning tools, data analytics packages, appropriate generic software (such as spreadsheets), AI (including GenAI, paragraphs 1.49-1.55) and other innovative and emerging technologies relevant to accounting theory or practice as they arise."
  stem: none
  statementType: requirement
  rung: none
  force: will
  level: none
  appliesTo: "Accounting courses"
  addressee: provider
  verbs: ["prepare", "understand", "design"]
  about: "digital technologies in teaching"
  themes: [none]
  domain: none
  award: ["none"]
  gradeOf: none
  paraphrase: "Because a degree should prepare students to understand data systems, it will very probably be necessary to build suitable digital technology into teaching: cloud accounting packages, data cleaning and analytics tools, spreadsheets, AI including GenAI and emerging technology."
  quote: full   # the issuer's statement is in `source` (D-std-0014)
  audience: practitioner
  subjects: inherited
- id: qaa/accounting-2025/3.23
  locator: { number: "3.23", headingPath: ["Content, structure and delivery", "Learning and teaching"] }
  span: { start: 94295, end: 94838 }
  source: "3.23 Learning and teaching should be inclusive (paragraphs 1.19-1.28) and accessible (paragraphs 1.29-1.32) in design , recognising the diverse needs of learners. In addition, ideally, learning and teaching design should address the diversity of cultures and learning environments that students may have previously experienced, and provide opportunities for students to transition towards a critical learning environment and learn from others to better understand the global context of their learning and of future employment or further study."
  stem: none
  statementType: expectation
  rung: none
  force: should
  level: none
  appliesTo: "Accounting courses and their students"
  addressee: both
  verbs: ["recognising", "address", "provide"]
  about: "inclusive, accessible and culturally aware teaching"
  themes: [none]
  domain: none
  award: ["none"]
  gradeOf: none
  paraphrase: "Learning and teaching should be inclusive and accessible by design and, ideally, should address the varied cultures and learning settings students come from, helping them move into a critical learning environment and learn from others about the global context."
  quote: full   # the issuer's statement is in `source` (D-std-0014)
  audience: both
  subjects: inherited
- id: qaa/accounting-2025/3.24
  locator: { number: "3.24", headingPath: ["Content, structure and delivery", "Learning and teaching"] }
  span: { start: 94839, end: 95327 }
  source: "3.24 The interactions between teaching, research and professional practice are key elements of the environment in which Accounting is learnt, recognising that teaching should be research informed or research led. As appropriate, Accounting educators should be encouraged to reflect on their professional and academic experience and practice to enhance and enrich the learning environment, ensuring that teaching reflects current developments in the professional and research environments."
  stem: none
  statementType: requirement
  rung: none
  force: should
  level: none
  appliesTo: "Accounting courses"
  addressee: provider
  verbs: ["encouraged", "reflect", "enhance"]
  about: "research-informed and practice-informed teaching"
  themes: [none]
  domain: none
  award: ["none"]
  gradeOf: none
  paraphrase: "Teaching, research and professional practice interact in the learning setting, and teaching should be research-informed or research-led; staff should be encouraged to draw on their professional and academic experience so teaching reflects current developments."
  quote: full   # the issuer's statement is in `source` (D-std-0014)
  audience: practitioner
  subjects: inherited
- id: qaa/accounting-2025/3.25
  locator: { number: "3.25", headingPath: ["Content, structure and delivery", "Learning and teaching"] }
  span: { start: 95328, end: 95910 }
  source: "3.25 Where appropriate, the design of learning and teaching activities, together with associated assessment activities, can usefully be informed by current pedagogical developments and research in these areas. Learning and teaching strategies should adapt\n\n27\nto changes in the business world and regulatory developments. Technological advances also need to be considered as they relate to teaching practice. In this context, there is an expectation that educators should have access to a range of educational professional development opportunities and receive appropriate training."
  stem: none
  statementType: requirement
  rung: none
  force: should
  level: none
  appliesTo: "Accounting courses"
  addressee: provider
  verbs: ["adapt", "considered", "receive"]
  about: "responsive strategy and staff development"
  themes: [none]
  domain: none
  award: ["none"]
  gradeOf: none
  paraphrase: "Teaching design can usefully draw on pedagogic research; strategies should adapt to business and regulatory change and technology, and teaching staff are expected to have access to professional development and suitable training."
  quote: full   # the issuer's statement is in `source` (D-std-0014)
  audience: practitioner
  subjects: inherited
- id: qaa/accounting-2025/3.26
  locator: { number: "3.26", headingPath: ["Content, structure and delivery", "Learning and teaching"] }
  span: { start: 95911, end: 96083 }
  source: "3.26 Learning and teaching strategies, structures and approaches should be monitored and reviewed on an ongoing basis to ensure quality and currency (paragraphs 2.28-2.33)."
  stem: none
  statementType: requirement
  rung: none
  force: should
  level: none
  appliesTo: "Accounting courses"
  addressee: provider
  verbs: ["monitored", "reviewed", "ensure"]
  about: "reviewing learning and teaching"
  themes: [none]
  domain: none
  award: ["none"]
  gradeOf: none
  paraphrase: "The strategy, structures and approaches for teaching should be kept under continual review for quality and currency."
  quote: full   # the issuer's statement is in `source` (D-std-0014)
  audience: practitioner
  subjects: inherited
- id: qaa/accounting-2025/3.27
  locator: { number: "3.27", headingPath: ["Content, structure and delivery", "Assessment"] }
  span: { start: 96095, end: 96436 }
  source: "3.27 Summative assessment within an Accounting degree programme should be robust and rigorous in assessing student's attainment of the knowledge, understanding and skills (subject-specific, transferable, professional and practice) set out in this Subject Benchmark Statement, as incorporated in the learning outcomes of the degree programme."
  stem: none
  statementType: requirement
  rung: none
  force: should
  level: none
  appliesTo: "Accounting courses"
  addressee: provider
  verbs: ["assessing"]
  about: "robust summative assessment"
  themes: [none]
  domain: none
  award: ["none"]
  gradeOf: none
  paraphrase: "Summative assessment should be robust and rigorous in measuring students' attainment of the statement's knowledge, understanding and skills as built into the course's learning outcomes."
  quote: full   # the issuer's statement is in `source` (D-std-0014)
  audience: practitioner
  subjects: inherited
- id: qaa/accounting-2025/3.28
  locator: { number: "3.28", headingPath: ["Content, structure and delivery", "Assessment"] }
  span: { start: 96437, end: 96848 }
  source: "3.28 In addition to summative assessment, Accounting degree programmes should include a range of formative assessments and feedback processes. The formative assessments should be designed in a way to enhance the learning environment and encourage active and independent learning. Formative assessment may include a broad range of methods, including, but not limited to, the methods used in summative assessment."
  stem: none
  statementType: requirement
  rung: none
  force: should
  level: none
  appliesTo: "Accounting courses"
  addressee: provider
  verbs: ["include", "designed", "enhance", "encourage"]
  about: "formative assessment and feedback"
  themes: [none]
  domain: none
  award: ["none"]
  gradeOf: none
  paraphrase: "Alongside summative assessment, courses should include varied formative assessment and feedback, designed to enrich the learning setting and promote active, independent learning."
  quote: full   # the issuer's statement is in `source` (D-std-0014)
  audience: practitioner
  subjects: inherited
- id: qaa/accounting-2025/3.29
  locator: { number: "3.29", headingPath: ["Content, structure and delivery", "Assessment"] }
  span: { start: 96849, end: 97180 }
  source: "3.29 The portfolio of assessment should be balanced, including an appropriate range of methods of assessment, across the degree programme to ensure that the scheme of assessment is inclusive (paragraphs 1.19-1.28), flexible and innovative to support student learning and enable them to demonstrate progressive levels of attainment."
  stem: none
  statementType: requirement
  rung: none
  force: should
  level: none
  appliesTo: "Accounting courses"
  addressee: provider
  verbs: ["balanced", "support", "enable", "demonstrate"]
  about: "a balanced and inclusive portfolio"
  themes: [none]
  domain: none
  award: ["none"]
  gradeOf: none
  paraphrase: "The assessment portfolio across the degree should be balanced, with a fitting range of methods, so that it is inclusive, flexible and innovative, supports learning and lets students show rising attainment."
  quote: full   # the issuer's statement is in `source` (D-std-0014)
  audience: practitioner
  subjects: inherited
- id: qaa/accounting-2025/3.30
  locator: { number: "3.30", headingPath: ["Content, structure and delivery", "Assessment"] }
  span: { start: 97181, end: 97616 }
  source: "3.30 Taken across the entire Accounting degree programme, the balance of assessment should ensure that all of the required knowledge, understanding and skills are achieved, including the discursive, conceptual/theoretical and critical elements, and that the weighting and structure of assessment does not allow students to avoid these elements by concentrating on the routine, calculative, applied and technical elements of accounting."
  stem: none
  statementType: requirement
  rung: none
  force: should
  level: none
  appliesTo: "Accounting courses"
  addressee: provider
  verbs: ["ensure", "achieved", "avoid"]
  about: "no route around critical elements"
  themes: [none]
  domain: none
  award: ["none"]
  gradeOf: none
  paraphrase: "Across the degree, assessment should make sure all required knowledge and skills are achieved, including the discursive, conceptual and critical, and should not let students avoid them by concentrating on routine, calculative and technical work."
  quote: full   # the issuer's statement is in `source` (D-std-0014)
  audience: practitioner
  subjects: inherited
- id: qaa/accounting-2025/3.31
  locator: { number: "3.31", headingPath: ["Content, structure and delivery", "Assessment"] }
  span: { start: 97617, end: 98514 }
  source: "3.31 It is important that assessment within an Accounting degree programmes concentrates on assessing the depth of student's learning of knowledge and understanding and the acquisition of subject-specific, transferable, professional and practice skills. Therefore, assessment should be designed to avoid the potential for students to pass modules using only rote learning, regurgitation, and surface learning (for example, objective or multiple- choice assessment). Modules should include substantial elements of critical assessment, including, for example: authentic scenario and case-based work; embedding technical problem questions into dynamic cases or scenarios. Where multiple choice assessment (or other forms of objective assessment) are used (in either summative of formative assessment), it should be carefully designed to avoid encouraging or rewarding surface and uncritical learning."
  stem: none
  statementType: requirement
  rung: none
  force: should
  level: none
  appliesTo: "Accounting courses"
  addressee: provider
  verbs: ["designed", "avoid", "include"]
  about: "assessing depth, not rote learning"
  themes: [none]
  domain: none
  award: ["none"]
  gradeOf: none
  paraphrase: "Assessment should test depth of learning and skill, avoiding designs that let students pass through rote or surface learning such as objective tests; modules should include substantial critical assessment, authentic cases and technical questions set in dynamic scenarios, and any multiple choice should be designed not to reward uncritical learning."
  quote: full   # the issuer's statement is in `source` (D-std-0014)
  audience: practitioner
  subjects: inherited
- id: qaa/accounting-2025/3.32
  locator: { number: "3.32", headingPath: ["Content, structure and delivery", "Assessment"] }
  span: { start: 98515, end: 98789 }
  source: "3.32 The assessment strategy within an Accounting degree programme should be designed and operated in order to equip students to become independent, self-directed, lifelong learners, critical thinkers and should include appropriate feedback to aid students' future learning."
  stem: none
  statementType: expectation
  rung: none
  force: should
  level: fheq:6
  appliesTo: "Accounting courses and their students"
  addressee: both
  verbs: ["designed", "operated", "equip", "include"]
  about: "assessment for independent, lifelong learners"
  themes: [none]
  domain: generic-skill
  award: ["bachelor's with honours"]
  gradeOf: none
  paraphrase: "The assessment strategy should be designed and run to make students independent, self-directed lifelong learners and critical thinkers, with feedback that helps their future learning."
  quote: full   # the issuer's statement is in `source` (D-std-0014)
  audience: both
  subjects: inherited
- id: qaa/accounting-2025/3.33
  locator: { number: "3.33", headingPath: ["Content, structure and delivery", "Assessment"] }
  span: { start: 98790, end: 99263 }
  source: "3.33 Assessment should be designed to be inclusive (in relation to EDI, paragraphs 1.19- 1.28, and accessibility, paragraphs 1.29-1.32), including reasonable adjustments as appropriate, acknowledging that reasonable adjustments to assessment should not undermine the nature and scope of the assessment or undermine the assessment of attainment of programme learning outcomes. Overall assessment is best designed to allow students to demonstrate their learning achievements."
  stem: none
  statementType: requirement
  rung: none
  force: should
  level: none
  appliesTo: "Accounting courses"
  addressee: provider
  verbs: ["designed", "undermine", "demonstrate"]
  about: "inclusive assessment and reasonable adjustments"
  themes: [none]
  domain: none
  award: ["none"]
  gradeOf: none
  paraphrase: "Assessment should be inclusive for EDI and accessibility, with reasonable adjustments where suitable that leave the assessment's nature, scope and outcomes intact; overall it should let students show what they have achieved."
  quote: full   # the issuer's statement is in `source` (D-std-0014)
  audience: practitioner
  subjects: inherited
- id: qaa/accounting-2025/3.34
  locator: { number: "3.34", headingPath: ["Content, structure and delivery", "Assessment"] }
  span: { start: 99268, end: 100240 }
  source: "3.34 Assessment (both summative and formative) should be designed to facilitate dialogues of learning (Laurillard 1993; Friere 1970, 1974), and therefore to contribute to students' specific learning and their capacity to become lifelong learners. Feedback helps to engender this dialogue, but this can take many forms and need not involve direct comments from or discussions with staff. Feedback can be engendered by encouraging students to provide their own feedback via the design of learning experiences involving comparison of their work with information in resources (such as exemplars, videos, peers' work, GenAI outputs, underlying theory) (Nicol, 2021; Nicol and McCallum, 2022). Educator feedback, where provided, may include comments in a classroom or seminar discussions or written, verbal, audio or video feedback on completed assessments. Feedback schemes should be designed to be timely and able to be actioned by students so that they can use it to develop."
  stem: none
  statementType: expectation
  rung: none
  force: should
  level: none
  appliesTo: "Accounting courses and their students"
  addressee: both
  verbs: ["designed", "facilitate", "contribute"]
  about: "assessment as dialogue and feedback"
  themes: [none]
  domain: none
  award: ["none"]
  gradeOf: none
  paraphrase: "Summative and formative assessment should support dialogues of learning that help students learn and become lifelong learners; feedback can take many forms, including students comparing their work with exemplars, peers' work, GenAI outputs or theory, and feedback schemes should be timely and usable."
  quote: full   # the issuer's statement is in `source` (D-std-0014)
  audience: both
  subjects: inherited
- id: qaa/accounting-2025/3.35
  locator: { number: "3.35", headingPath: ["Content, structure and delivery", "Assessment"] }
  span: { start: 100241, end: 100625 }
  source: "3.35 The scheme of assessment (the nature of individual assessment elements and their contribution to the summative assessment) for individual modules within an Accounting degree programme should be clear to students at the outset of each module. When designing programme assessment schemes, consideration should be given to the timing of and overall assessment workload for students."
  stem: none
  statementType: requirement
  rung: none
  force: should
  level: none
  appliesTo: "Accounting courses"
  addressee: provider
  verbs: ["clear", "given"]
  about: "clear assessment schemes and workload"
  themes: [none]
  domain: none
  award: ["none"]
  gradeOf: none
  paraphrase: "Each module's assessment scheme should be clear to students at its start, and programme schemes should take account of timing and total workload."
  quote: full   # the issuer's statement is in `source` (D-std-0014)
  audience: practitioner
  subjects: inherited
- id: qaa/accounting-2025/3.36
  locator: { number: "3.36", headingPath: ["Content, structure and delivery", "Assessment"] }
  span: { start: 100626, end: 101074 }
  source: "3.36 The assessment criteria for each element of assessment should be clearly communicated to students in a timely manner, normally at least by the time students are expected to work on the assessment element. The marking criteria may be communicated by way of assessment rubrics: rubrics should normally be indicative and related to module and programme learning outcomes rather than prescriptive (for example, detailed marking/grading schedules)."
  stem: none
  statementType: requirement
  rung: none
  force: should
  level: none
  appliesTo: "Accounting courses"
  addressee: provider
  verbs: ["communicated", "related"]
  about: "timely, indicative assessment criteria"
  themes: [none]
  domain: none
  award: ["none"]
  gradeOf: none
  paraphrase: "Assessment criteria should be communicated to students in good time, normally before they start work on the task; rubrics should normally be indicative and linked to learning outcomes rather than prescriptive."
  quote: full   # the issuer's statement is in `source` (D-std-0014)
  audience: practitioner
  subjects: inherited
- id: qaa/accounting-2025/3.39
  locator: { number: "3.39", headingPath: ["Content, structure and delivery", "Assessment"] }
  span: { start: 102160, end: 102803 }
  source: "3.39 Team or group-based assessment can be appropriate within an Accounting degree programme, particularly in relation to the assessment of collaborative and related skills. Where team or group-based assessment is used, care should be taken to ensure that the grading of team or group assessments fairly reflects the attainment of individuals. Careful consideration should be given to the balance between team or group-based and individual work in an Accounting degree programme. Where team or group-based assessment is used, students should be provided with appropriate guidance and support on the management and operation of teams or groups."
  stem: none
  statementType: expectation
  rung: none
  force: should
  level: none
  appliesTo: "Accounting courses and their students"
  addressee: both
  verbs: ["taken", "given", "provided"]
  about: "fair team and group assessment"
  themes: [none]
  domain: none
  award: ["none"]
  gradeOf: none
  paraphrase: "Group assessment can suit collaborative skills; where it is used, grades should fairly reflect individuals' attainment, the balance with individual work should be weighed, and students should get guidance on running teams."
  quote: full   # the issuer's statement is in `source` (D-std-0014)
  audience: both
  subjects: inherited
- id: qaa/accounting-2025/3.41
  locator: { number: "3.41", headingPath: ["Content, structure and delivery", "Assessment"] }
  span: { start: 103058, end: 103827 }
  source: "3.41 Peer discussion and review can play an important role in learning by promoting student engagement, and assessment might be designed to facilitate peer dialogue. Peer discussion and review processes should be well managed with appropriate safeguards in place to ensure students are not disadvantaged, especially in relation to EDI issues. Students should normally be provided with appropriate guidelines or training. Given the real and serious potential for students to be disadvantaged from an EDI perspective, peer ratings or assessments should not normally contribute to summative assessment unless there are strong processes in place to protect potentially disadvantaged students and there is robust and appropriate academic input into the summative assessment."
  stem: none
  statementType: requirement
  rung: none
  force: should
  level: none
  appliesTo: "Accounting courses"
  addressee: provider
  verbs: ["managed", "provided", "contribute"]
  about: "safeguards for peer assessment"
  themes: [none]
  domain: none
  award: ["none"]
  gradeOf: none
  paraphrase: "Peer discussion and review can aid learning, but it should be well managed with safeguards so no one is disadvantaged, especially for EDI reasons; students should normally have guidance or training, and peer ratings should not normally count towards summative marks without strong protection and academic input."
  quote: full   # the issuer's statement is in `source` (D-std-0014)
  audience: practitioner
  subjects: inherited
- id: qaa/accounting-2025/3.42
  locator: { number: "3.42", headingPath: ["Content, structure and delivery", "Assessment"] }
  span: { start: 103828, end: 104755 }
  source: "3.42 The widespread availability of GenAI makes it essential that Accounting degree programmes take account of the implications of AI in assessment design. However, GenAI also provides opportunities to design assessment that is more in line with the requirements of this Subject Benchmark Statement, in relation to both knowledge and understanding, and skills development. This might include, for example, moving away from assessment that relies on rote learning, regurgitation and surface learning (paragraph 3.31); the use of critical assessment, including authentic scenario and case-based work; embedding technical problem questions into dynamic cases or scenarios; evaluating experiential learning tasks; and assessing students' critical understanding of the implications of AI within accounting as a discipline and accounting practice. These issues should be taken into account in both formative and summative assessment."
  stem: none
  statementType: requirement
  rung: none
  force: should
  level: none
  appliesTo: "Accounting courses"
  addressee: provider
  verbs: ["take", "design", "taken"]
  about: "GenAI and assessment design"
  themes: [none]
  domain: none
  award: ["none"]
  gradeOf: none
  paraphrase: "Widespread GenAI means assessment design must account for AI, but it also allows designs closer to the statement's aims, such as critical, authentic, case-based and experiential tasks and assessment of students' grasp of AI in accounting; these points should apply to formative and summative work."
  quote: full   # the issuer's statement is in `source` (D-std-0014)
  audience: practitioner
  subjects: inherited
- id: qaa/accounting-2025/3.43
  locator: { number: "3.43", headingPath: ["Content, structure and delivery", "Assessment"] }
  span: { start: 104756, end: 105399 }
  source: "3.43 When designing assessment to address the widespread availability of GenAI, modules should ensure there is continuous monitoring and review of authorial integrity and GenAI- aware control policies and practices. This is essential as GenAI content is very difficult to reliably detect. GenAI policies and practices should be clearly communicated to all staff and students (including scope of acceptable usage) and students should be reminded about the importance of upholding the highest ethical and professional standards in assessment in line with professional bodies expectations (paragraphs 1.7-1.8) and extant institutional guidelines."
  stem: none
  statementType: requirement
  rung: none
  force: should
  level: none
  appliesTo: "Accounting courses"
  addressee: provider
  verbs: ["ensure", "communicated", "reminded"]
  about: "GenAI policies communicated to all"
  themes: [none]
  domain: none
  award: ["none"]
  gradeOf: none
  paraphrase: "When designing assessment for GenAI, modules should keep integrity and GenAI control policies under continuous review, since AI content is hard to detect; policies, including acceptable use, should be clear to all staff and students, and students should be reminded of the highest ethical and professional standards."
  quote: full   # the issuer's statement is in `source` (D-std-0014)
  audience: practitioner
  subjects: inherited
- id: qaa/accounting-2025/4.2
  locator: { number: "4.2", headingPath: ["Benchmark Standards", "Introduction"] }
  span: { start: 105691, end: 106220 }
  source: "4.2 Please note that minimum threshold standards as well as typical, very good and excellent standards are not intended to specify universal competence standards for a discipline. If a provider chooses to develop competence standards (as defined by the Equality Act 2010) as part of a programme specification, these can be informed by the relevant Subject Benchmark Statement along with any PSRB requirements. In these circumstances, providers should follow the most recent guidance from the Equality and Human Rights Commission."
  stem: none
  statementType: requirement
  rung: none
  force: should
  level: none
  appliesTo: "Accounting courses"
  addressee: provider
  verbs: ["follow"]
  about: "competence standards and EHRC guidance"
  themes: [none]
  domain: none
  award: ["none"]
  gradeOf: none
  paraphrase: "The standards at each level are not universal competence standards; a provider developing competence standards under the Equality Act 2010 may draw on the statement and PSRB requirements and should then follow the Equality and Human Rights Commission's latest guidance."
  quote: full   # the issuer's statement is in `source` (D-std-0014)
  audience: practitioner
  subjects: inherited
- id: qaa/accounting-2025/4.4
  locator: { number: "4.4", headingPath: ["Benchmark Standards", "Undergraduate awards"] }
  span: { start: 107282, end: 107616 }
  source: "4.4 It is expected that most students will perform significantly better than the minimum threshold standards. The benchmark standards below should be interpreted and applied recognising that each higher education provider has its own method of determining what appropriate evidence of achievement is required for each class of degree."
  stem: none
  statementType: requirement
  rung: none
  force: should
  level: none
  appliesTo: "Accounting courses"
  addressee: provider
  verbs: ["interpreted", "applied", "recognising"]
  about: "interpreting the standards"
  themes: [none]
  domain: none
  award: ["none"]
  gradeOf: none
  paraphrase: "Most students are expected to do much better than the threshold; the standards should be read and applied with the understanding that each provider decides what evidence each class of degree needs."
  quote: full   # the issuer's statement is in `source` (D-std-0014)
  audience: practitioner
  subjects: inherited
- id: qaa/accounting-2025/4.5.b1
  locator: { number: "4.5.b1", headingPath: ["Benchmark Standards", "Undergraduate awards"] }
  span: { start: 108417, end: 108516 }
  source: "Basic knowledge and understanding of the critical, ethical and contextual importance of accounting."
  stem: "4.5"
  statementType: threshold
  rung: threshold
  force: threshold
  level: fheq:6
  appliesTo: "honours graduates at the threshold level"
  addressee: learner
  verbs: []
  about: "critical, ethical and contextual knowledge"
  themes: [none]
  domain: knowledge
  award: ["bachelor's with honours"]
  gradeOf: none
  paraphrase: "A basic grasp of why accounting matters critically, ethically and in context."
  quote: full   # the issuer's statement is in `source` (D-std-0014)
  audience: both
  subjects: inherited
- id: qaa/accounting-2025/4.5.b2
  locator: { number: "4.5.b2", headingPath: ["Benchmark Standards", "Undergraduate awards"] }
  span: { start: 108518, end: 108752 }
  source: "Some ability to integrate theoretical and conceptual issues and debates within discussion of key areas of public and organisational interests, reflecting a range of socioeconomic, accountability, sustainability and other perspectives."
  stem: "4.5"
  statementType: threshold
  rung: threshold
  force: threshold
  level: fheq:6
  appliesTo: "honours graduates at the threshold level"
  addressee: learner
  verbs: ["integrate"]
  about: "bringing theory into discussion of public and organisational issues"
  themes: [none]
  domain: understanding
  award: ["bachelor's with honours"]
  gradeOf: none
  paraphrase: "Some capacity to bring theory, concepts and debate into discussion of public and organisational questions from several social, economic, accountability and sustainability angles."
  quote: full   # the issuer's statement is in `source` (D-std-0014)
  audience: both
  subjects: inherited
- id: qaa/accounting-2025/4.5.b3
  locator: { number: "4.5.b3", headingPath: ["Benchmark Standards", "Undergraduate awards"] }
  span: { start: 108753, end: 108852 }
  source: "Solid knowledge and understanding of the critical, ethical and contextual importance of accounting."
  stem: "4.5"
  statementType: typical
  rung: typical
  force: threshold
  level: fheq:6
  appliesTo: "honours graduates at the typical level"
  addressee: learner
  verbs: []
  about: "critical, ethical and contextual knowledge"
  themes: [none]
  domain: knowledge
  award: ["bachelor's with honours"]
  gradeOf: { statement: qaa/accounting-2025/4.5.b1, basis: inferred }
  paraphrase: "A solid grasp of accounting's critical, ethical and contextual significance."
  quote: full   # the issuer's statement is in `source` (D-std-0014)
  audience: both
  subjects: inherited
- id: qaa/accounting-2025/4.5.b4
  locator: { number: "4.5.b4", headingPath: ["Benchmark Standards", "Undergraduate awards"] }
  span: { start: 108854, end: 109099 }
  source: "Good ability to integrate theoretical and conceptual issues and debates within critical discussion of key areas of public and organisational interests, reflecting a range of socio- economic, accountability, sustainability and other perspectives."
  stem: "4.5"
  statementType: typical
  rung: typical
  force: threshold
  level: fheq:6
  appliesTo: "honours graduates at the typical level"
  addressee: learner
  verbs: ["integrate"]
  about: "bringing theory into critical discussion of public and organisational issues"
  themes: [none]
  domain: understanding
  award: ["bachelor's with honours"]
  gradeOf: { statement: qaa/accounting-2025/4.5.b2, basis: inferred }
  paraphrase: "A good capacity to bring theory, concepts and debate into critical discussion of public and organisational questions from several perspectives."
  quote: full   # the issuer's statement is in `source` (D-std-0014)
  audience: both
  subjects: inherited
- id: qaa/accounting-2025/4.5.b5
  locator: { number: "4.5.b5", headingPath: ["Benchmark Standards", "Undergraduate awards"] }
  span: { start: 109100, end: 109203 }
  source: "Very good knowledge and understanding of the critical, ethical and contextual importance of accounting."
  stem: "4.5"
  statementType: very-good
  rung: very-good
  force: threshold
  level: fheq:6
  appliesTo: "honours graduates at the very-good level"
  addressee: learner
  verbs: []
  about: "critical, ethical and contextual knowledge"
  themes: [none]
  domain: knowledge
  award: ["bachelor's with honours"]
  gradeOf: { statement: qaa/accounting-2025/4.5.b3, basis: inferred }
  paraphrase: "A very good grasp of accounting's critical, ethical and contextual significance."
  quote: full   # the issuer's statement is in `source` (D-std-0014)
  audience: both
  subjects: inherited
- id: qaa/accounting-2025/4.5.b6
  locator: { number: "4.5.b6", headingPath: ["Benchmark Standards", "Undergraduate awards"] }
  span: { start: 109205, end: 109498 }
  source: "Very good ability to integrate theoretical and conceptual issues and debates within critical discussion of key areas of public and organisational interests, reflecting a wide range of socioeconomic, accountability, sustainability and other perspectives in an integrated and synthesised manner."
  stem: "4.5"
  statementType: very-good
  rung: very-good
  force: threshold
  level: fheq:6
  appliesTo: "honours graduates at the very-good level"
  addressee: learner
  verbs: ["integrate"]
  about: "bringing theory into critical discussion of public and organisational issues"
  themes: [none]
  domain: understanding
  award: ["bachelor's with honours"]
  gradeOf: { statement: qaa/accounting-2025/4.5.b4, basis: inferred }
  paraphrase: "A very good capacity to bring theory and debate into critical discussion of public and organisational questions across a wide range of perspectives, joined up and synthesised."
  quote: full   # the issuer's statement is in `source` (D-std-0014)
  audience: both
  subjects: inherited
- id: qaa/accounting-2025/4.5.b7
  locator: { number: "4.5.b7", headingPath: ["Benchmark Standards", "Undergraduate awards"] }
  span: { start: 109499, end: 109602 }
  source: "Excellent knowledge and understanding of the critical, ethical and contextual importance of accounting."
  stem: "4.5"
  statementType: excellent
  rung: excellent
  force: threshold
  level: fheq:6
  appliesTo: "honours graduates at the excellent level"
  addressee: learner
  verbs: []
  about: "critical, ethical and contextual knowledge"
  themes: [none]
  domain: knowledge
  award: ["bachelor's with honours"]
  gradeOf: { statement: qaa/accounting-2025/4.5.b5, basis: inferred }
  paraphrase: "An excellent grasp of accounting's critical, ethical and contextual significance."
  quote: full   # the issuer's statement is in `source` (D-std-0014)
  audience: both
  subjects: inherited
- id: qaa/accounting-2025/4.5.b8
  locator: { number: "4.5.b8", headingPath: ["Benchmark Standards", "Undergraduate awards"] }
  span: { start: 109604, end: 109905 }
  source: "Excellent ability to integrate theoretical and conceptual issues and debates into critical discussion of key areas of public and organisational interests, reflecting a wide range of socioeconomic, accountability, sustainability and other perspectives in a very well- integrated and synthesised manner."
  stem: "4.5"
  statementType: excellent
  rung: excellent
  force: threshold
  level: fheq:6
  appliesTo: "honours graduates at the excellent level"
  addressee: learner
  verbs: ["integrate"]
  about: "bringing theory into critical discussion of public and organisational issues"
  themes: [none]
  domain: understanding
  award: ["bachelor's with honours"]
  gradeOf: { statement: qaa/accounting-2025/4.5.b6, basis: inferred }
  paraphrase: "An excellent capacity to weave theory and debate into critical discussion of public and organisational questions across a wide range of perspectives, fully synthesised."
  quote: full   # the issuer's statement is in `source` (D-std-0014)
  audience: both
  subjects: inherited
- id: qaa/accounting-2025/4.5.b9
  locator: { number: "4.5.b9", headingPath: ["Benchmark Standards", "Undergraduate awards"] }
  span: { start: 109998, end: 110086 }
  source: "Basic knowledge and understanding of substantially all of the broad areas of accounting."
  stem: "4.5"
  statementType: threshold
  rung: threshold
  force: threshold
  level: fheq:6
  appliesTo: "honours graduates at the threshold level"
  addressee: learner
  verbs: []
  about: "knowledge across the broad areas"
  themes: [none]
  domain: knowledge
  award: ["bachelor's with honours"]
  gradeOf: none
  paraphrase: "Basic knowledge of nearly all the broad areas of accounting."
  quote: full   # the issuer's statement is in `source` (D-std-0014)
  audience: both
  subjects: inherited
- id: qaa/accounting-2025/4.5.b10
  locator: { number: "4.5.b10", headingPath: ["Benchmark Standards", "Undergraduate awards"] }
  span: { start: 110088, end: 110205 }
  source: "Able to demonstrate some ability to integrate their knowledge and understanding across the broad areas of accounting."
  stem: "4.5"
  statementType: threshold
  rung: threshold
  force: threshold
  level: fheq:6
  appliesTo: "honours graduates at the threshold level"
  addressee: learner
  verbs: ["demonstrate", "integrate"]
  about: "integrating knowledge across the areas"
  themes: [none]
  domain: understanding
  award: ["bachelor's with honours"]
  gradeOf: none
  paraphrase: "Shows some capacity to connect knowledge across the broad areas."
  quote: full   # the issuer's statement is in `source` (D-std-0014)
  audience: both
  subjects: inherited
- id: qaa/accounting-2025/4.5.b11
  locator: { number: "4.5.b11", headingPath: ["Benchmark Standards", "Undergraduate awards"] }
  span: { start: 110206, end: 110344 }
  source: "Solid knowledge and understanding of substantially all of the broad areas of accounting, and a basic understanding of the remaining areas."
  stem: "4.5"
  statementType: typical
  rung: typical
  force: threshold
  level: fheq:6
  appliesTo: "honours graduates at the typical level"
  addressee: learner
  verbs: []
  about: "knowledge across the broad areas"
  themes: [none]
  domain: knowledge
  award: ["bachelor's with honours"]
  gradeOf: { statement: qaa/accounting-2025/4.5.b9, basis: inferred }
  paraphrase: "Solid knowledge of nearly all the broad areas and a basic grasp of the rest."
  quote: full   # the issuer's statement is in `source` (D-std-0014)
  audience: both
  subjects: inherited
- id: qaa/accounting-2025/4.5.b12
  locator: { number: "4.5.b12", headingPath: ["Benchmark Standards", "Undergraduate awards"] }
  span: { start: 110346, end: 110462 }
  source: "Able to demonstrate a good level of integration of knowledge and understanding across the broad areas of accounting."
  stem: "4.5"
  statementType: typical
  rung: typical
  force: threshold
  level: fheq:6
  appliesTo: "honours graduates at the typical level"
  addressee: learner
  verbs: ["demonstrate"]
  about: "integrating knowledge across the areas"
  themes: [none]
  domain: understanding
  award: ["bachelor's with honours"]
  gradeOf: { statement: qaa/accounting-2025/4.5.b10, basis: inferred }
  paraphrase: "Shows good integration of knowledge across the broad areas."
  quote: full   # the issuer's statement is in `source` (D-std-0014)
  audience: both
  subjects: inherited
- id: qaa/accounting-2025/4.5.b13
  locator: { number: "4.5.b13", headingPath: ["Benchmark Standards", "Undergraduate awards"] }
  span: { start: 110463, end: 110614 }
  source: "Very good knowledge and critical understanding of substantially all of the broad areas of accounting, and a solid understanding of the remaining areas."
  stem: "4.5"
  statementType: very-good
  rung: very-good
  force: threshold
  level: fheq:6
  appliesTo: "honours graduates at the very-good level"
  addressee: learner
  verbs: []
  about: "knowledge across the broad areas"
  themes: [none]
  domain: knowledge
  award: ["bachelor's with honours"]
  gradeOf: { statement: qaa/accounting-2025/4.5.b11, basis: inferred }
  paraphrase: "Very good, critical knowledge of nearly all the broad areas and a solid grasp of the rest."
  quote: full   # the issuer's statement is in `source` (D-std-0014)
  audience: both
  subjects: inherited
- id: qaa/accounting-2025/4.5.b14
  locator: { number: "4.5.b14", headingPath: ["Benchmark Standards", "Undergraduate awards"] }
  span: { start: 110616, end: 110737 }
  source: "Able to demonstrate a very good level of integration of knowledge and understanding across the broad areas of accounting."
  stem: "4.5"
  statementType: very-good
  rung: very-good
  force: threshold
  level: fheq:6
  appliesTo: "honours graduates at the very-good level"
  addressee: learner
  verbs: ["demonstrate"]
  about: "integrating knowledge across the areas"
  themes: [none]
  domain: understanding
  award: ["bachelor's with honours"]
  gradeOf: { statement: qaa/accounting-2025/4.5.b12, basis: inferred }
  paraphrase: "Shows very good integration of knowledge across the broad areas."
  quote: full   # the issuer's statement is in `source` (D-std-0014)
  audience: both
  subjects: inherited
- id: qaa/accounting-2025/4.5.b15
  locator: { number: "4.5.b15", headingPath: ["Benchmark Standards", "Undergraduate awards"] }
  span: { start: 110738, end: 110913 }
  source: "Excellent knowledge and critical understanding at an advanced level of substantially all of the broad areas of accounting and a very good understanding of the remaining areas."
  stem: "4.5"
  statementType: excellent
  rung: excellent
  force: threshold
  level: fheq:6
  appliesTo: "honours graduates at the excellent level"
  addressee: learner
  verbs: []
  about: "knowledge across the broad areas"
  themes: [none]
  domain: knowledge
  award: ["bachelor's with honours"]
  gradeOf: { statement: qaa/accounting-2025/4.5.b13, basis: inferred }
  paraphrase: "Excellent, critical and advanced knowledge of nearly all the broad areas and a very good grasp of the rest."
  quote: full   # the issuer's statement is in `source` (D-std-0014)
  audience: both
  subjects: inherited
- id: qaa/accounting-2025/4.5.b16
  locator: { number: "4.5.b16", headingPath: ["Benchmark Standards", "Undergraduate awards"] }
  span: { start: 110915, end: 111034 }
  source: "Able to demonstrate an excellent ability to integrate knowledge and understanding across all broad areas of accounting."
  stem: "4.5"
  statementType: excellent
  rung: excellent
  force: threshold
  level: fheq:6
  appliesTo: "honours graduates at the excellent level"
  addressee: learner
  verbs: ["demonstrate", "integrate"]
  about: "integrating knowledge across the areas"
  themes: [none]
  domain: understanding
  award: ["bachelor's with honours"]
  gradeOf: { statement: qaa/accounting-2025/4.5.b14, basis: inferred }
  paraphrase: "Shows excellent integration of knowledge across every broad area."
  quote: full   # the issuer's statement is in `source` (D-std-0014)
  audience: both
  subjects: inherited
- id: qaa/accounting-2025/4.5.b17
  locator: { number: "4.5.b17", headingPath: ["Benchmark Standards", "Undergraduate awards"] }
  span: { start: 111159, end: 111346 }
  source: "Sufficient levels of proficiency in the majority of these skills, with an ability to perform adequately in applying these skills to straightforward and structured problems and situations."
  stem: "4.5"
  statementType: threshold
  rung: threshold
  force: threshold
  level: fheq:6
  appliesTo: "honours graduates at the threshold level"
  addressee: learner
  verbs: ["perform", "applying"]
  about: "proficiency in transferable and professional skills"
  themes: [none]
  domain: generic-skill
  award: ["bachelor's with honours"]
  gradeOf: none
  paraphrase: "Adequate proficiency in most of the skills in 3.14 and 3.15, used adequately on simple, well-defined problems."
  quote: full   # the issuer's statement is in `source` (D-std-0014)
  audience: both
  subjects: inherited
- id: qaa/accounting-2025/4.5.b18
  locator: { number: "4.5.b18", headingPath: ["Benchmark Standards", "Undergraduate awards"] }
  span: { start: 111348, end: 111512 }
  source: "Able to demonstrate some ability to select, consider, evaluate, comment on and synthesise a broad range of knowledge and understanding to construct valid arguments."
  stem: "4.5"
  statementType: threshold
  rung: threshold
  force: threshold
  level: fheq:6
  appliesTo: "honours graduates at the threshold level"
  addressee: learner
  verbs: ["demonstrate", "select", "consider", "evaluate", "synthesise", "construct"]
  about: "building arguments from knowledge"
  themes: [none]
  domain: generic-skill
  award: ["bachelor's with honours"]
  gradeOf: none
  paraphrase: "Shows some capacity to choose, weigh, comment on and combine knowledge into sound arguments."
  quote: full   # the issuer's statement is in `source` (D-std-0014)
  audience: both
  subjects: inherited
- id: qaa/accounting-2025/4.5.b19
  locator: { number: "4.5.b19", headingPath: ["Benchmark Standards", "Undergraduate awards"] }
  span: { start: 111513, end: 111717 }
  source: "Good levels of proficiency in substantially all of these skills, with an ability to perform well in applying these skills critically to moderately complex and not fully structured problems and situations."
  stem: "4.5"
  statementType: typical
  rung: typical
  force: threshold
  level: fheq:6
  appliesTo: "honours graduates at the typical level"
  addressee: learner
  verbs: ["perform", "applying"]
  about: "proficiency in transferable and professional skills"
  themes: [none]
  domain: generic-skill
  award: ["bachelor's with honours"]
  gradeOf: { statement: qaa/accounting-2025/4.5.b17, basis: inferred }
  paraphrase: "Good proficiency in nearly all the skills, used critically and well on moderately complex, partly structured problems."
  quote: full   # the issuer's statement is in `source` (D-std-0014)
  audience: both
  subjects: inherited
- id: qaa/accounting-2025/4.5.b20
  locator: { number: "4.5.b20", headingPath: ["Benchmark Standards", "Undergraduate awards"] }
  span: { start: 111719, end: 111884 }
  source: "Able to demonstrate good ability to select, consider, evaluate, comment on and synthesise a broad range of knowledge and understanding to construct strong arguments."
  stem: "4.5"
  statementType: typical
  rung: typical
  force: threshold
  level: fheq:6
  appliesTo: "honours graduates at the typical level"
  addressee: learner
  verbs: ["demonstrate", "select", "consider", "evaluate", "synthesise", "construct"]
  about: "building arguments from knowledge"
  themes: [none]
  domain: generic-skill
  award: ["bachelor's with honours"]
  gradeOf: { statement: qaa/accounting-2025/4.5.b18, basis: inferred }
  paraphrase: "Shows good capacity to choose, weigh, comment on and combine knowledge into strong arguments."
  quote: full   # the issuer's statement is in `source` (D-std-0014)
  audience: both
  subjects: inherited
- id: qaa/accounting-2025/4.5.b21
  locator: { number: "4.5.b21", headingPath: ["Benchmark Standards", "Undergraduate awards"] }
  span: { start: 111885, end: 112108 }
  source: "Very good levels of proficiency in substantially all of these skills, with an ability to perform very well in applying these skills critically and in an integrated manner to complex and unstructured problems and situations."
  stem: "4.5"
  statementType: very-good
  rung: very-good
  force: threshold
  level: fheq:6
  appliesTo: "honours graduates at the very-good level"
  addressee: learner
  verbs: ["perform", "applying"]
  about: "proficiency in transferable and professional skills"
  themes: [none]
  domain: generic-skill
  award: ["bachelor's with honours"]
  gradeOf: { statement: qaa/accounting-2025/4.5.b19, basis: inferred }
  paraphrase: "Very good proficiency in nearly all the skills, applied critically and in combination to complex, unstructured problems."
  quote: full   # the issuer's statement is in `source` (D-std-0014)
  audience: both
  subjects: inherited
- id: qaa/accounting-2025/4.5.b22
  locator: { number: "4.5.b22", headingPath: ["Benchmark Standards", "Undergraduate awards"] }
  span: { start: 112110, end: 112293 }
  source: "Able to demonstrate very good ability to select, consider, evaluate, comment on and synthesise a broad range of knowledge and understanding to construct strong and creative arguments."
  stem: "4.5"
  statementType: very-good
  rung: very-good
  force: threshold
  level: fheq:6
  appliesTo: "honours graduates at the very-good level"
  addressee: learner
  verbs: ["demonstrate", "select", "consider", "evaluate", "synthesise", "construct"]
  about: "building arguments from knowledge"
  themes: [none]
  domain: generic-skill
  award: ["bachelor's with honours"]
  gradeOf: { statement: qaa/accounting-2025/4.5.b20, basis: inferred }
  paraphrase: "Shows very good capacity to choose, weigh, comment on and combine knowledge into strong and creative arguments."
  quote: full   # the issuer's statement is in `source` (D-std-0014)
  audience: both
  subjects: inherited
- id: qaa/accounting-2025/4.5.b23
  locator: { number: "4.5.b23", headingPath: ["Benchmark Standards", "Undergraduate awards"] }
  span: { start: 112294, end: 112538 }
  source: "Excellent levels of proficiency in substantially all of these skills, with an ability to perform at excellent levels in applying these skills critically and in an integrated manner to complex, unstructured and unbounded problems and situations."
  stem: "4.5"
  statementType: excellent
  rung: excellent
  force: threshold
  level: fheq:6
  appliesTo: "honours graduates at the excellent level"
  addressee: learner
  verbs: ["perform", "applying"]
  about: "proficiency in transferable and professional skills"
  themes: [none]
  domain: generic-skill
  award: ["bachelor's with honours"]
  gradeOf: { statement: qaa/accounting-2025/4.5.b21, basis: inferred }
  paraphrase: "Excellent proficiency in nearly all the skills, applied critically and in combination to complex, unstructured and open-ended problems."
  quote: full   # the issuer's statement is in `source` (D-std-0014)
  audience: both
  subjects: inherited
- id: qaa/accounting-2025/4.5.b24
  locator: { number: "4.5.b24", headingPath: ["Benchmark Standards", "Undergraduate awards"] }
  span: { start: 112540, end: 112723 }
  source: "Able to demonstrate excellent ability to select, consider, evaluate, comment on and synthesise a broad range of knowledge and understanding to construct strong and creative arguments."
  stem: "4.5"
  statementType: excellent
  rung: excellent
  force: threshold
  level: fheq:6
  appliesTo: "honours graduates at the excellent level"
  addressee: learner
  verbs: ["demonstrate", "select", "consider", "evaluate", "synthesise", "construct"]
  about: "building arguments from knowledge"
  themes: [none]
  domain: generic-skill
  award: ["bachelor's with honours"]
  gradeOf: { statement: qaa/accounting-2025/4.5.b22, basis: inferred }
  paraphrase: "Shows excellent capacity to choose, weigh, comment on and combine knowledge into strong and creative arguments."
  quote: full   # the issuer's statement is in `source` (D-std-0014)
  audience: both
  subjects: inherited
- id: qaa/accounting-2025/4.5.b25
  locator: { number: "4.5.b25", headingPath: ["Benchmark Standards", "Undergraduate awards"] }
  span: { start: 112800, end: 113021 }
  source: "Basic ability to apply knowledge and understanding of accounting, utilising a range of skills and critique to straightforward and structured problems and situations within the context of a range of types of organisations."
  stem: "4.5"
  statementType: threshold
  rung: threshold
  force: threshold
  level: fheq:6
  appliesTo: "honours graduates at the threshold level"
  addressee: learner
  verbs: ["apply"]
  about: "applying accounting to problems in many organisations"
  themes: [none]
  domain: subject-skill
  award: ["bachelor's with honours"]
  gradeOf: none
  paraphrase: "A basic capacity to apply accounting knowledge, with a range of skills and critique, to simple, well-defined problems in various kinds of organisation."
  quote: full   # the issuer's statement is in `source` (D-std-0014)
  audience: both
  subjects: inherited
- id: qaa/accounting-2025/4.5.b26
  locator: { number: "4.5.b26", headingPath: ["Benchmark Standards", "Undergraduate awards"] }
  span: { start: 113022, end: 113261 }
  source: "Good ability to apply knowledge and understanding of accounting, utilising a broad range of skills and critique to moderately complex and not fully structured problems and situations within the context of a range of types of organisations."
  stem: "4.5"
  statementType: typical
  rung: typical
  force: threshold
  level: fheq:6
  appliesTo: "honours graduates at the typical level"
  addressee: learner
  verbs: ["apply"]
  about: "applying accounting to problems in many organisations"
  themes: [none]
  domain: subject-skill
  award: ["bachelor's with honours"]
  gradeOf: { statement: qaa/accounting-2025/4.5.b25, basis: inferred }
  paraphrase: "A good capacity to apply accounting knowledge, drawing on a broad set of skills and critical thought, on moderately complex, partly structured problems in various organisations."
  quote: full   # the issuer's statement is in `source` (D-std-0014)
  audience: both
  subjects: inherited
- id: qaa/accounting-2025/4.5.b27
  locator: { number: "4.5.b27", headingPath: ["Benchmark Standards", "Undergraduate awards"] }
  span: { start: 113262, end: 113486 }
  source: "Very good ability to apply knowledge and understanding of accounting, utilising a wide range of skills and critique to complex and unstructured problems and situations within the context of a range of types of organisations."
  stem: "4.5"
  statementType: very-good
  rung: very-good
  force: threshold
  level: fheq:6
  appliesTo: "honours graduates at the very-good level"
  addressee: learner
  verbs: ["apply"]
  about: "applying accounting to problems in many organisations"
  themes: [none]
  domain: subject-skill
  award: ["bachelor's with honours"]
  gradeOf: { statement: qaa/accounting-2025/4.5.b26, basis: inferred }
  paraphrase: "A very good capacity to apply accounting knowledge, drawing on a wide set of skills and critical thought, on complex, unstructured problems in various organisations."
  quote: full   # the issuer's statement is in `source` (D-std-0014)
  audience: both
  subjects: inherited
- id: qaa/accounting-2025/4.5.b28
  locator: { number: "4.5.b28", headingPath: ["Benchmark Standards", "Undergraduate awards"] }
  span: { start: 113487, end: 113722 }
  source: "Excellent ability to apply knowledge and understanding of accounting, utilising a wide range of skills and critique to complex, unstructured and unbounded problems and situations within the context of a range of types of organisations."
  stem: "4.5"
  statementType: excellent
  rung: excellent
  force: threshold
  level: fheq:6
  appliesTo: "honours graduates at the excellent level"
  addressee: learner
  verbs: ["apply"]
  about: "applying accounting to problems in many organisations"
  themes: [none]
  domain: subject-skill
  award: ["bachelor's with honours"]
  gradeOf: { statement: qaa/accounting-2025/4.5.b27, basis: inferred }
  paraphrase: "An excellent capacity to apply accounting knowledge, drawing on a wide set of skills and critical thought, on complex, unstructured and open-ended problems in various organisations."
  quote: full   # the issuer's statement is in `source` (D-std-0014)
  audience: both
  subjects: inherited
- id: qaa/accounting-2025/4.7.b1
  locator: { number: "4.7.b1", headingPath: ["Benchmark Standards", "Master's awards"] }
  span: { start: 117602, end: 117724 }
  source: "Specialist and sophisticated knowledge and understanding of the critical, ethical and contextual importance of accounting."
  stem: "4.7"
  statementType: threshold
  rung: threshold
  force: threshold
  level: fheq:7
  appliesTo: "graduates of the master's (advanced or specialist)"
  addressee: learner
  verbs: []
  about: "specialist critical, ethical and contextual knowledge"
  themes: [none]
  domain: knowledge
  award: ["master's (advanced or specialist)"]
  gradeOf: none
  paraphrase: "Specialist, sophisticated knowledge of accounting's critical, ethical and contextual significance."
  quote: full   # the issuer's statement is in `source` (D-std-0014)
  audience: both
  subjects: inherited
- id: qaa/accounting-2025/4.7.b2
  locator: { number: "4.7.b2", headingPath: ["Benchmark Standards", "Master's awards"] }
  span: { start: 117726, end: 118075 }
  source: "Ability to integrate theoretical and conceptual issues and debates into critical discussion of key areas of public or organisational interests, reflecting an appropriate range of socioeconomic, accountability, sustainability and other perspectives in a very well- integrated and synthesised manner as appropriate to the specialisation of the degree."
  stem: "4.7"
  statementType: threshold
  rung: threshold
  force: threshold
  level: fheq:7
  appliesTo: "graduates of the master's (advanced or specialist)"
  addressee: learner
  verbs: ["integrate"]
  about: "integrating theory into critical discussion, by specialism"
  themes: [none]
  domain: understanding
  award: ["master's (advanced or specialist)"]
  gradeOf: none
  paraphrase: "The capacity to integrate theory and debate into critical discussion of public or organisational questions, drawing on suitable perspectives, very well synthesised and fitted to the specialism."
  quote: full   # the issuer's statement is in `source` (D-std-0014)
  audience: both
  subjects: inherited
- id: qaa/accounting-2025/4.7.b3
  locator: { number: "4.7.b3", headingPath: ["Benchmark Standards", "Master's awards"] }
  span: { start: 118076, end: 118183 }
  source: "Comprehensive knowledge and understanding of the critical, ethical and contextual importance of accounting."
  stem: "4.7"
  statementType: threshold
  rung: threshold
  force: threshold
  level: fheq:7
  appliesTo: "graduates of the master's (conversion)"
  addressee: learner
  verbs: []
  about: "comprehensive critical, ethical and contextual knowledge"
  themes: [none]
  domain: knowledge
  award: ["master's (conversion)"]
  gradeOf: none
  paraphrase: "Comprehensive knowledge of accounting's critical, ethical and contextual significance."
  quote: full   # the issuer's statement is in `source` (D-std-0014)
  audience: both
  subjects: inherited
- id: qaa/accounting-2025/4.7.b4
  locator: { number: "4.7.b4", headingPath: ["Benchmark Standards", "Master's awards"] }
  span: { start: 118185, end: 118429 }
  source: "Ability to integrate theoretical and conceptual issues and debates within sound critical discussion of key areas of public and organisational interests, reflecting a range of socioeconomic, accountability, sustainability and other perspectives."
  stem: "4.7"
  statementType: threshold
  rung: threshold
  force: threshold
  level: fheq:7
  appliesTo: "graduates of the master's (conversion)"
  addressee: learner
  verbs: ["integrate"]
  about: "integrating theory into sound critical discussion"
  themes: [none]
  domain: understanding
  award: ["master's (conversion)"]
  gradeOf: none
  paraphrase: "The capacity to integrate theory and debate into sound critical discussion of public and organisational questions from a range of perspectives."
  quote: full   # the issuer's statement is in `source` (D-std-0014)
  audience: both
  subjects: inherited
- id: qaa/accounting-2025/4.7.b5
  locator: { number: "4.7.b5", headingPath: ["Benchmark Standards", "Master's awards"] }
  span: { start: 118431, end: 118575 }
  source: "Comprehensive knowledge and understanding of the critical, ethical and contextual importance of accounting, particularly as applied in practice."
  stem: "4.7"
  statementType: threshold
  rung: threshold
  force: threshold
  level: fheq:7
  appliesTo: "graduates of the master's (professional)"
  addressee: learner
  verbs: ["applied"]
  about: "comprehensive knowledge, as applied in practice"
  themes: [none]
  domain: knowledge
  award: ["master's (professional)"]
  gradeOf: none
  paraphrase: "Comprehensive knowledge of accounting's critical, ethical and contextual significance, above all in practice."
  quote: full   # the issuer's statement is in `source` (D-std-0014)
  audience: both
  subjects: inherited
- id: qaa/accounting-2025/4.7.b6
  locator: { number: "4.7.b6", headingPath: ["Benchmark Standards", "Master's awards"] }
  span: { start: 118577, end: 118955 }
  source: "Ability to integrate theoretical and conceptual issues and debates within critical discussion of key areas of professional, public and organisational interests, particularly as this relates to professional or organisational practice, reflecting an appropriate range of socioeconomic, accountability, sustainability and other perspectives in an integrated and synthesised manner."
  stem: "4.7"
  statementType: threshold
  rung: threshold
  force: threshold
  level: fheq:7
  appliesTo: "graduates of the master's (professional)"
  addressee: learner
  verbs: ["integrate"]
  about: "integrating theory into discussion of professional practice"
  themes: [none]
  domain: understanding
  award: ["master's (professional)"]
  gradeOf: none
  paraphrase: "The capacity to integrate theory and debate into critical discussion of professional, public and organisational questions, especially practice, from suitable perspectives, joined up and synthesised."
  quote: full   # the issuer's statement is in `source` (D-std-0014)
  audience: both
  subjects: inherited
- id: qaa/accounting-2025/4.7.b7
  locator: { number: "4.7.b7", headingPath: ["Benchmark Standards", "Master's awards"] }
  span: { start: 118957, end: 119291 }
  source: "In addition to reaching the benchmark standards for a typical or very good honours degree (Table 1); achievement of the benchmark standards for either an advanced or specialist academic master's degree (paragraph 1.16 a), or to the more advanced levels of a professional master's degree (paragraph 1.16 c) (as detailed in this table)."
  stem: "4.7"
  statementType: threshold
  rung: threshold
  force: threshold
  level: fheq:7
  appliesTo: "graduates of the integrated master's"
  addressee: learner
  verbs: []
  about: "honours standards plus master's standards, combined"
  themes: [none]
  domain: knowledge
  award: ["integrated master's"]
  gradeOf: none
  paraphrase: "Reaching the typical or very good honours level of Table 1 and then the advanced or specialist master's level, or the higher levels of the professional master's, as the table sets out."
  quote: full   # the issuer's statement is in `source` (D-std-0014)
  audience: both
  subjects: inherited
- id: qaa/accounting-2025/4.7.b8
  locator: { number: "4.7.b8", headingPath: ["Benchmark Standards", "Master's awards"] }
  span: { start: 119387, end: 119671 }
  source: "Specialist and sophisticated knowledge and critical understanding at an advanced level either across a wide range of the broad subject areas of accounting or more deeply in a subset of these areas, possibly combined with additional subject area within accounting or other disciplines."
  stem: "4.7"
  statementType: threshold
  rung: threshold
  force: threshold
  level: fheq:7
  appliesTo: "graduates of the master's (advanced or specialist)"
  addressee: learner
  verbs: []
  about: "specialist knowledge across or within the broad areas"
  themes: [none]
  domain: knowledge
  award: ["master's (advanced or specialist)"]
  gradeOf: none
  paraphrase: "Specialist, sophisticated and critical knowledge at an advanced level, either broadly across the areas of accounting or deeply in some, possibly with a further area inside or outside accounting."
  quote: full   # the issuer's statement is in `source` (D-std-0014)
  audience: both
  subjects: inherited
- id: qaa/accounting-2025/4.7.b9
  locator: { number: "4.7.b9", headingPath: ["Benchmark Standards", "Master's awards"] }
  span: { start: 119673, end: 119830 }
  source: "Ability to demonstrate informed and insightful integration of their knowledge and understanding across the appropriate areas of study in a sophisticated way."
  stem: "4.7"
  statementType: threshold
  rung: threshold
  force: threshold
  level: fheq:7
  appliesTo: "graduates of the master's (advanced or specialist)"
  addressee: learner
  verbs: ["demonstrate"]
  about: "sophisticated integration across the areas studied"
  themes: [none]
  domain: understanding
  award: ["master's (advanced or specialist)"]
  gradeOf: none
  paraphrase: "Shows informed, insightful and sophisticated integration of knowledge across the areas studied."
  quote: full   # the issuer's statement is in `source` (D-std-0014)
  audience: both
  subjects: inherited
- id: qaa/accounting-2025/4.7.b10
  locator: { number: "4.7.b10", headingPath: ["Benchmark Standards", "Master's awards"] }
  span: { start: 119831, end: 119977 }
  source: "Comprehensive knowledge and understanding of substantially all of the broad areas of accounting, and a basic understanding of the remaining areas."
  stem: "4.7"
  statementType: threshold
  rung: threshold
  force: threshold
  level: fheq:7
  appliesTo: "graduates of the master's (conversion)"
  addressee: learner
  verbs: []
  about: "comprehensive knowledge of the broad areas"
  themes: [none]
  domain: knowledge
  award: ["master's (conversion)"]
  gradeOf: none
  paraphrase: "Comprehensive knowledge of nearly all the broad areas and a basic grasp of the rest."
  quote: full   # the issuer's statement is in `source` (D-std-0014)
  audience: both
  subjects: inherited
- id: qaa/accounting-2025/4.7.b11
  locator: { number: "4.7.b11", headingPath: ["Benchmark Standards", "Master's awards"] }
  span: { start: 119979, end: 120112 }
  source: "Ability to demonstrate informed and insightful integration of their knowledge and understanding across the broad areas of accounting."
  stem: "4.7"
  statementType: threshold
  rung: threshold
  force: threshold
  level: fheq:7
  appliesTo: "graduates of the master's (conversion)"
  addressee: learner
  verbs: ["demonstrate"]
  about: "insightful integration across the broad areas"
  themes: [none]
  domain: understanding
  award: ["master's (conversion)"]
  gradeOf: none
  paraphrase: "Shows informed and insightful integration of knowledge across the broad areas."
  quote: full   # the issuer's statement is in `source` (D-std-0014)
  audience: both
  subjects: inherited
- id: qaa/accounting-2025/4.7.b12
  locator: { number: "4.7.b12", headingPath: ["Benchmark Standards", "Master's awards"] }
  span: { start: 120113, end: 120281 }
  source: "Comprehensive and advanced knowledge and critical understanding of substantially all of the broad areas of accounting, and a solid understanding of the remaining areas."
  stem: "4.7"
  statementType: threshold
  rung: threshold
  force: threshold
  level: fheq:7
  appliesTo: "graduates of the master's (professional)"
  addressee: learner
  verbs: []
  about: "comprehensive, advanced knowledge of the broad areas"
  themes: [none]
  domain: knowledge
  award: ["master's (professional)"]
  gradeOf: none
  paraphrase: "Comprehensive, advanced and critical knowledge of nearly all the broad areas and a solid grasp of the rest."
  quote: full   # the issuer's statement is in `source` (D-std-0014)
  audience: both
  subjects: inherited
- id: qaa/accounting-2025/4.7.b13
  locator: { number: "4.7.b13", headingPath: ["Benchmark Standards", "Master's awards"] }
  span: { start: 120283, end: 120495 }
  source: "Ability to demonstrate informed and insightful integration of their knowledge and understanding across the broad areas of accounting, particularly in relation to issues of professional or organisational practice."
  stem: "4.7"
  statementType: threshold
  rung: threshold
  force: threshold
  level: fheq:7
  appliesTo: "graduates of the master's (professional)"
  addressee: learner
  verbs: ["demonstrate"]
  about: "integration across the areas for professional practice"
  themes: [none]
  domain: understanding
  award: ["master's (professional)"]
  gradeOf: none
  paraphrase: "Shows informed, insightful integration of knowledge across the broad areas, especially for professional and organisational practice."
  quote: full   # the issuer's statement is in `source` (D-std-0014)
  audience: both
  subjects: inherited
- id: qaa/accounting-2025/4.7.b14
  locator: { number: "4.7.b14", headingPath: ["Benchmark Standards", "Master's awards"] }
  span: { start: 120620, end: 120854 }
  source: "Very good levels of proficiency in substantially all of these skills, with an ability to perform very well in applying these skills critically and in an integrated manner to complex, unstructured and unbounded problems and situations."
  stem: "4.7"
  statementType: threshold
  rung: threshold
  force: threshold
  level: fheq:7
  appliesTo: "graduates of the master's (advanced or specialist)"
  addressee: learner
  verbs: ["perform", "applying"]
  about: "proficiency in transferable and professional skills"
  themes: [none]
  domain: generic-skill
  award: ["master's (advanced or specialist)"]
  gradeOf: none
  paraphrase: "Very good proficiency in nearly all the skills, applied critically and in combination to complex, unstructured and open-ended problems."
  quote: full   # the issuer's statement is in `source` (D-std-0014)
  audience: both
  subjects: inherited
- id: qaa/accounting-2025/4.7.b15
  locator: { number: "4.7.b15", headingPath: ["Benchmark Standards", "Master's awards"] }
  span: { start: 120856, end: 121058 }
  source: "Ability to demonstrate capacity to select, consider, evaluate, comment on and synthesise a broad range of specialised and advanced knowledge and understanding to construct strong and creative arguments."
  stem: "4.7"
  statementType: threshold
  rung: threshold
  force: threshold
  level: fheq:7
  appliesTo: "graduates of the master's (advanced or specialist)"
  addressee: learner
  verbs: ["demonstrate", "select", "consider", "evaluate", "synthesise", "construct"]
  about: "arguments from specialised, advanced knowledge"
  themes: [none]
  domain: generic-skill
  award: ["master's (advanced or specialist)"]
  gradeOf: none
  paraphrase: "Shows the capacity to choose, weigh, comment on and combine specialised, advanced knowledge into strong and creative arguments."
  quote: full   # the issuer's statement is in `source` (D-std-0014)
  audience: both
  subjects: inherited
- id: qaa/accounting-2025/4.7.b16
  locator: { number: "4.7.b16", headingPath: ["Benchmark Standards", "Master's awards"] }
  span: { start: 121059, end: 121265 }
  source: "Very good levels of proficiency in substantially all of these skills, with an ability to perform very well in applying these skills critically to moderately complex and unstructured problems and situations."
  stem: "4.7"
  statementType: threshold
  rung: threshold
  force: threshold
  level: fheq:7
  appliesTo: "graduates of the master's (conversion)"
  addressee: learner
  verbs: ["perform", "applying"]
  about: "proficiency in transferable and professional skills"
  themes: [none]
  domain: generic-skill
  award: ["master's (conversion)"]
  gradeOf: none
  paraphrase: "Very good proficiency in nearly all the skills, applied critically and well to moderately complex, unstructured problems."
  quote: full   # the issuer's statement is in `source` (D-std-0014)
  audience: both
  subjects: inherited
- id: qaa/accounting-2025/4.7.b17
  locator: { number: "4.7.b17", headingPath: ["Benchmark Standards", "Master's awards"] }
  span: { start: 121267, end: 121431 }
  source: "Ability to demonstrate capacity to select, consider, evaluate, comment on and synthesise a broad range of knowledge and understanding to construct strong arguments."
  stem: "4.7"
  statementType: threshold
  rung: threshold
  force: threshold
  level: fheq:7
  appliesTo: "graduates of the master's (conversion)"
  addressee: learner
  verbs: ["demonstrate", "select", "consider", "evaluate", "synthesise", "construct"]
  about: "building strong arguments"
  themes: [none]
  domain: generic-skill
  award: ["master's (conversion)"]
  gradeOf: none
  paraphrase: "Shows the capacity to choose, weigh, comment on and combine knowledge into strong arguments."
  quote: full   # the issuer's statement is in `source` (D-std-0014)
  audience: both
  subjects: inherited
- id: qaa/accounting-2025/4.7.b18
  locator: { number: "4.7.b18", headingPath: ["Benchmark Standards", "Master's awards"] }
  span: { start: 121432, end: 121695 }
  source: "Very good levels of proficiency in substantially all of these skills, with an ability to perform very well in applying these skills critically and in an integrated manner to complex and unstructured problems and situations, typically with an emphasis on practice."
  stem: "4.7"
  statementType: threshold
  rung: threshold
  force: threshold
  level: fheq:7
  appliesTo: "graduates of the master's (professional)"
  addressee: learner
  verbs: ["perform", "applying"]
  about: "proficiency in skills, with a practice emphasis"
  themes: [none]
  domain: generic-skill
  award: ["master's (professional)"]
  gradeOf: none
  paraphrase: "Very good proficiency in nearly all the skills, applied critically and in combination to complex, unstructured problems, usually with a practice focus."
  quote: full   # the issuer's statement is in `source` (D-std-0014)
  audience: both
  subjects: inherited
- id: qaa/accounting-2025/4.7.b19
  locator: { number: "4.7.b19", headingPath: ["Benchmark Standards", "Master's awards"] }
  span: { start: 121697, end: 121946 }
  source: "Ability to demonstrate capacity to select, consider, evaluate, comment on and synthesise a broad range of knowledge and understanding to construct strong and creative arguments, particularly in the context of professional or organisational practice."
  stem: "4.7"
  statementType: threshold
  rung: threshold
  force: threshold
  level: fheq:7
  appliesTo: "graduates of the master's (professional)"
  addressee: learner
  verbs: ["demonstrate", "select", "consider", "evaluate", "synthesise", "construct"]
  about: "arguments for professional practice"
  themes: [none]
  domain: generic-skill
  award: ["master's (professional)"]
  gradeOf: none
  paraphrase: "Shows the capacity to choose, weigh, comment on and combine knowledge into strong and creative arguments, especially for professional or organisational practice."
  quote: full   # the issuer's statement is in `source` (D-std-0014)
  audience: both
  subjects: inherited
- id: qaa/accounting-2025/4.7.b20
  locator: { number: "4.7.b20", headingPath: ["Benchmark Standards", "Master's awards"] }
  span: { start: 121948, end: 122282 }
  source: "In addition to reaching the benchmark standards for a typical or very good honours degree (Table 1); achievement of the benchmark standards for either an advanced or specialist academic master's degree (paragraph 1.16 a), or to the more advanced levels of a professional master's degree (paragraph 1.16 c) (as detailed in this table)."
  stem: "4.7"
  statementType: threshold
  rung: threshold
  force: threshold
  level: fheq:7
  appliesTo: "graduates of the integrated master's"
  addressee: learner
  verbs: []
  about: "honours skills plus master's skills, combined"
  themes: [none]
  domain: generic-skill
  award: ["integrated master's"]
  gradeOf: none
  paraphrase: "For skills, reaching the typical or very good honours level of Table 1 and then the advanced or specialist master's level, or the higher professional master's level, as the table sets out."
  quote: full   # the issuer's statement is in `source` (D-std-0014)
  audience: both
  subjects: inherited
- id: qaa/accounting-2025/4.7.b21
  locator: { number: "4.7.b21", headingPath: ["Benchmark Standards", "Master's awards"] }
  span: { start: 122361, end: 122710 }
  source: "Ability to apply specialised and advance knowledge and understanding of accounting in a sophisticated, informed and insightful way, utilising a wide range of skills and critique to complex, unstructured and unbounded problems and situations within the context of a range of types of organisations as appropriate to the focus of the degree programme."
  stem: "4.7"
  statementType: threshold
  rung: threshold
  force: threshold
  level: fheq:7
  appliesTo: "graduates of the master's (advanced or specialist)"
  addressee: learner
  verbs: ["apply"]
  about: "sophisticated application to open-ended problems"
  themes: [none]
  domain: subject-skill
  award: ["master's (advanced or specialist)"]
  gradeOf: none
  paraphrase: "The capacity to apply specialised, advanced knowledge with sophistication and insight, drawing on a wide set of skills and critical thought, on complex, unstructured and open-ended problems in various organisations, fitted to the degree's focus."
  quote: full   # the issuer's statement is in `source` (D-std-0014)
  audience: both
  subjects: inherited
- id: qaa/accounting-2025/4.7.b22
  locator: { number: "4.7.b22", headingPath: ["Benchmark Standards", "Master's awards"] }
  span: { start: 122711, end: 122971 }
  source: "Ability to apply knowledge and understanding of accounting in an informed and insightful way, utilising a broad range of skills and critique to moderately complex and unstructured problems and situations within the context of a range of types of organisations."
  stem: "4.7"
  statementType: threshold
  rung: threshold
  force: threshold
  level: fheq:7
  appliesTo: "graduates of the master's (conversion)"
  addressee: learner
  verbs: ["apply"]
  about: "informed application to moderately complex problems"
  themes: [none]
  domain: subject-skill
  award: ["master's (conversion)"]
  gradeOf: none
  paraphrase: "The capacity to apply accounting knowledge with insight, drawing on a broad set of skills and critical thought, on moderately complex, unstructured problems in various organisations."
  quote: full   # the issuer's statement is in `source` (D-std-0014)
  audience: both
  subjects: inherited
- id: qaa/accounting-2025/4.7.b23
  locator: { number: "4.7.b23", headingPath: ["Benchmark Standards", "Master's awards"] }
  span: { start: 122972, end: 123279 }
  source: "Ability to apply knowledge and understanding of accounting in an informed and insightful way, utilising a wide range of skills and critique to complex and unstructured problems, particularly those of a practical and professional focus, and situations within the context of a range of types of organisations."
  stem: "4.7"
  statementType: threshold
  rung: threshold
  force: threshold
  level: fheq:7
  appliesTo: "graduates of the master's (professional)"
  addressee: learner
  verbs: ["apply"]
  about: "informed application to practical, professional problems"
  themes: [none]
  domain: subject-skill
  award: ["master's (professional)"]
  gradeOf: none
  paraphrase: "The capacity to apply accounting knowledge with insight, drawing on a wide set of skills and critical thought, on complex, unstructured problems, especially practical and professional ones, in various organisations."
  quote: full   # the issuer's statement is in `source` (D-std-0014)
  audience: both
  subjects: inherited
- id: qaa/accounting-2025/4.7.b24
  locator: { number: "4.7.b24", headingPath: ["Benchmark Standards", "Master's awards"] }
  span: { start: 123368, end: 123753 }
  source: "Convincing evidence of achievement in completion of a substantial element of self-directed research-based study in the specialist area of the programme at an advanced level, involving personal inquiry demonstrating intellectual curiosity into a theoretical area of the discipline or the application of theoretical and conceptual learning to a real-world project or issue of importance."
  stem: "4.7"
  statementType: threshold
  rung: threshold
  force: threshold
  level: fheq:7
  appliesTo: "graduates of the master's (advanced or specialist)"
  addressee: learner
  verbs: []
  about: "the self-directed research project, specialist"
  themes: [none]
  domain: subject-skill
  award: ["master's (advanced or specialist)"]
  gradeOf: none
  paraphrase: "Persuasive evidence of completing a substantial, self-directed research study at an advanced level in the specialism: a personal inquiry, driven by curiosity, into theory or into applying theory to a real issue."
  quote: full   # the issuer's statement is in `source` (D-std-0014)
  audience: both
  subjects: inherited
- id: qaa/accounting-2025/4.7.b25
  locator: { number: "4.7.b25", headingPath: ["Benchmark Standards", "Master's awards"] }
  span: { start: 123754, end: 124079 }
  source: "Convincing evidence of achievement in completion of a substantial element of self-directed research- based study, involving personal inquiry demonstrating intellectual curiosity into a theoretical area of the discipline or the application of theoretical and conceptual learning to a real-world project or issue of importance."
  stem: "4.7"
  statementType: threshold
  rung: threshold
  force: threshold
  level: fheq:7
  appliesTo: "graduates of the master's (conversion)"
  addressee: learner
  verbs: []
  about: "the self-directed research project"
  themes: [none]
  domain: subject-skill
  award: ["master's (conversion)"]
  gradeOf: none
  paraphrase: "Persuasive evidence of completing a substantial, self-directed research study: a personal inquiry, driven by curiosity, into theory or into applying theory to a real issue."
  quote: full   # the issuer's statement is in `source` (D-std-0014)
  audience: both
  subjects: inherited
- id: qaa/accounting-2025/4.7.b26
  locator: { number: "4.7.b26", headingPath: ["Benchmark Standards", "Master's awards"] }
  span: { start: 124080, end: 124407 }
  source: "Convincing evidence of achievement in completion of a substantial element of self-directed study, involving personal inquiry typically demonstrating high levels of achievement in applying knowledge and understanding to a practical or real- world project or issue of importance, possibly related to field or work-based learning."
  stem: "4.7"
  statementType: threshold
  rung: threshold
  force: threshold
  level: fheq:7
  appliesTo: "graduates of the master's (professional)"
  addressee: learner
  verbs: ["applying"]
  about: "the self-directed project, applied to practice"
  themes: [none]
  domain: subject-skill
  award: ["master's (professional)"]
  gradeOf: none
  paraphrase: "Persuasive evidence of completing a substantial, self-directed study, usually showing high achievement in applying knowledge to a practical or real project, perhaps linked to field or work-based learning."
  quote: full   # the issuer's statement is in `source` (D-std-0014)
  audience: both
  subjects: inherited
- id: qaa/accounting-2025/4.7.b27
  locator: { number: "4.7.b27", headingPath: ["Benchmark Standards", "Master's awards"] }
  span: { start: 124408, end: 124568 }
  source: "Convincing evidence of achievement in completion of a substantial element of self-directed study as appropriate to the nature of the integrated master's degree."
  stem: "4.7"
  statementType: threshold
  rung: threshold
  force: threshold
  level: fheq:7
  appliesTo: "graduates of the integrated master's"
  addressee: learner
  verbs: []
  about: "the self-directed study in an integrated master's"
  themes: [none]
  domain: subject-skill
  award: ["integrated master's"]
  gradeOf: none
  paraphrase: "Persuasive evidence of completing a substantial, self-directed study suited to the nature of the integrated master's."
  quote: full   # the issuer's statement is in `source` (D-std-0014)
  audience: both
  subjects: inherited
```

### S4a Audience versions
<!-- label: both; status: drafted; basis: primary. forPractitioner: for the programme designer or teacher. forBeneficiary: for the student, second person, naming no issuer. author-agent-written: instructions to an AI agent writing about the statement (a course document, a handbook, an outcome, a report). author-agent-dialogue: instructions to an AI agent using the statement in conversation (with a student, a teacher or a programme team). Written fresh from the held text alone (benchmark rule 6; Abbott, 15:42). -->
```yaml
- statement: qaa/accounting-2025/1.2
  forPractitioner: { text: "If you lead a joint Accounting and finance course, align it with both subject statements; it must still give real weight to accounting concepts and theory, accountability, sustainability, non-business uses, practical application and higher-order intellectual skills.", rewrite: light, force: must, status: drafted }
  forBeneficiary: { text: "not-applicable: a duty on the course and the people who design and run it, not a standard the student reaches", rewrite: full, force: must, status: drafted }
  author-agent-written: "Write about this as a requirement worded with \"must\" on the course and its team, on joint Accounting and finance courses, holding for the bachelor's degree with honours. Cite it as (QAA, 2025, Accounting Subject Benchmark Statement, para 1.2). Do not present it as a regulatory requirement, and do not turn it into an outcome a student must show. Set it beside qaa/accounting-2025/1.3, and where it shapes outcomes beside qaa/fheq-2024/4.15.b1 at spine:6."
  author-agent-dialogue: "Raise it with a programme team or teacher who is designing, reviewing or defending the course's approach to joint Accounting and finance courses. Frame it for staff as a requirement worded with \"must\", and ask: Which modules carry the conceptual and non-business side of accounting, so that finance content does not crowd it out? Do not quote the issuer at length, and do not put this duty to a student as something they have to achieve."
- statement: qaa/accounting-2025/1.3
  forPractitioner: { text: "In a joint honours design, read this statement beside the partner subject's and check that the balance still leaves room for accounting concepts and theory, accountability, sustainability, non-business uses, application and higher-order thinking.", rewrite: light, force: should, status: drafted }
  forBeneficiary: { text: "not-applicable: a duty on the course and the people who design and run it, not a standard the student reaches", rewrite: full, force: should, status: drafted }
  author-agent-written: "Write about this as an expectation worded with \"should\" on the course and its team, on Accounting within joint honours with other subjects, holding for the bachelor's degree with honours. Cite it as (QAA, 2025, Accounting Subject Benchmark Statement, para 1.3). Do not present it as a regulatory requirement, and do not turn it into an outcome a student must show. Set it beside qaa/accounting-2025/1.2 and qaa/accounting-2025/1.4, and where it shapes outcomes beside qaa/fheq-2024/4.15.b1 at spine:6."
  author-agent-dialogue: "Raise it with a programme team or teacher who is designing, reviewing or defending the course's approach to Accounting within joint honours with other subjects. Frame it for staff as an expectation worded with \"should\", and ask: When the partner subject takes half the credit, what is left of accounting theory and accountability? Do not quote the issuer at length, and do not put this duty to a student as something they have to achieve."
- statement: qaa/accounting-2025/1.4
  forPractitioner: { text: "Shape the course so that students see accounting as a social and economic practice tied to governance and accountability, across public, charitable, co-operative and private bodies and their stakeholders, not only as the measurement of profit and capital; ground it in foundational and current research.", rewrite: light, force: should, status: drafted }
  forBeneficiary: { text: "Your course should help you see what accounting does in society and in how organisations are governed, well beyond profit, including its part in sustainability and welfare and in the work of charities, public bodies and campaigns.", rewrite: full, force: should, status: drafted }
  author-agent-written: "Write about this as an expectation worded with \"should\" for any Accounting degree the statement covers, at the level of the award it is applied to, on the purpose of an Accounting degree. Cite it as (QAA, 2025, Accounting Subject Benchmark Statement, para 1.4). Do not claim it is a regulatory requirement or that it sets the standard at another level. Set it beside qaa/accounting-2025/1.3 and qaa/accounting-2025/1.5 and the framework descriptor the honours and master's descriptors (qaa/fheq-2024/4.15.b1, qaa/fheq-2024/4.17.b1) at spine:6 and spine:7."
  author-agent-dialogue: "Bring it up when a student asks about the purpose of an Accounting degree, or when staff check a module or outcome against it. Tell a student in plain words, as 'you', what it means for their course; for staff, frame it as an expectation worded with \"should\". Ask: Where in your course do you meet accounting outside the for-profit company, and what did it show you? Avoid long quotation of the issuer's text."
- statement: qaa/accounting-2025/1.5
  forPractitioner: { text: "Design for a mixed cohort: some students want a professional accountancy route, others business, public-sector or third-sector careers, social understanding or the subject for its own sake; the breadth of perspectives serves them all.", rewrite: light, force: should, status: drafted }
  forBeneficiary: { text: "not-applicable: a duty on the course and the people who design and run it, not a standard the student reaches", rewrite: full, force: should, status: drafted }
  author-agent-written: "Write about this as an expectation worded with \"should\" on the course and its team, on designing for students with different aims, holding for any Accounting degree the statement covers. Cite it as (QAA, 2025, Accounting Subject Benchmark Statement, para 1.5). Do not present it as a regulatory requirement, and do not turn it into an outcome a student must show. Set it beside qaa/accounting-2025/1.4 and qaa/accounting-2025/1.6, and where it shapes outcomes beside the honours and master's descriptors (qaa/fheq-2024/4.15.b1, qaa/fheq-2024/4.17.b1) at spine:6 and spine:7."
  author-agent-dialogue: "Raise it with a programme team or teacher who is designing, reviewing or defending the course's approach to designing for students with different aims. Frame it for staff as an expectation worded with \"should\", and ask: Which of these student aims does the current design serve least well? Do not quote the issuer at length, and do not put this duty to a student as something they have to achieve."
- statement: qaa/accounting-2025/1.6
  forPractitioner: { text: "Bring social science perspectives (economics, information systems, politics, psychology, sociology and others) into the study of how accounting systems are designed, run and validated, and size the finance content to the course type.", rewrite: light, force: should, status: drafted }
  forBeneficiary: { text: "You will study how accounting systems affect, and are affected by, people, organisations, technology, markets, society and the environment, and your course should draw on ideas from economics, politics, sociology and other social sciences to help you.", rewrite: full, force: should, status: drafted }
  author-agent-written: "Write about this as an expectation worded with \"should\" for any Accounting degree the statement covers, at the level of the award it is applied to, on accounting systems and the social sciences. Cite it as (QAA, 2025, Accounting Subject Benchmark Statement, para 1.6). Do not claim it is a regulatory requirement or that it sets the standard at another level. Set it beside qaa/accounting-2025/1.5 and qaa/accounting-2025/1.8 and the framework descriptor the honours and master's descriptors (qaa/fheq-2024/4.15.b1, qaa/fheq-2024/4.17.b1) at spine:6 and spine:7."
  author-agent-dialogue: "Bring it up when a student asks about accounting systems and the social sciences, or when staff check a module or outcome against it. Tell a student in plain words, as 'you', what it means for their course; for staff, frame it as an expectation worded with \"should\". Ask: Which social science lens has most changed how you think about an accounting system? Avoid long quotation of the issuer's text."
- statement: qaa/accounting-2025/1.8
  forPractitioner: { text: "Check the design against accreditation pull: a course that trades the broader intellectual, social and environmental content for narrow technical material does not satisfy this statement, whatever exemptions it earns.", rewrite: light, force: threshold, status: drafted }
  forBeneficiary: { text: "not-applicable: a duty on the course and the people who design and run it, not a standard the student reaches", rewrite: full, force: threshold, status: drafted }
  author-agent-written: "Write about this as a minimum condition on the course and its team, on technical, non-critical content at the expense of breadth, holding for any Accounting degree the statement covers. Cite it as (QAA, 2025, Accounting Subject Benchmark Statement, para 1.8). Do not present it as a regulatory requirement, and do not turn it into an outcome a student must show. Set it beside qaa/accounting-2025/1.6 and qaa/accounting-2025/1.9, and where it shapes outcomes beside the honours and master's descriptors (qaa/fheq-2024/4.15.b1, qaa/fheq-2024/4.17.b1) at spine:6 and spine:7."
  author-agent-dialogue: "Raise it with a programme team or teacher who is designing, reviewing or defending the course's approach to technical, non-critical content at the expense of breadth. Frame it for staff as a minimum condition, and ask: If an accrediting body's syllabus were removed, what broader content would remain in the course? Do not quote the issuer at length, and do not put this duty to a student as something they have to achieve."
- statement: qaa/accounting-2025/1.9
  forPractitioner: { text: "Do not build the course around today's technical rules alone: they will change within your graduates' careers. Teach current frameworks, and build self-directed learning and professional, transferable and critical skills that keep graduates employable long term.", rewrite: light, force: should, status: drafted }
  forBeneficiary: { text: "Your course should prepare you for a profession whose rules and practices may change a great deal during your career, so it should help you keep learning on your own and build professional, transferable and critical skills, not only today's techniques.", rewrite: full, force: should, status: drafted }
  author-agent-written: "Write about this as an expectation worded with \"should\" for any Accounting degree the statement covers, at the level of the award it is applied to, on preparing for a changing profession. Cite it as (QAA, 2025, Accounting Subject Benchmark Statement, para 1.9). Do not claim it is a regulatory requirement or that it sets the standard at another level. Set it beside qaa/accounting-2025/1.8 and qaa/accounting-2025/1.11 and the framework descriptor the honours and master's descriptors (qaa/fheq-2024/4.15.b1, qaa/fheq-2024/4.17.b1) at spine:6 and spine:7."
  author-agent-dialogue: "Bring it up when a student asks about preparing for a changing profession, or when staff check a module or outcome against it. Tell a student in plain words, as 'you', what it means for their course; for staff, frame it as an expectation worded with \"should\". Ask: What will you do when a standard you learned is replaced five years after you graduate? Avoid long quotation of the issuer's text."
- statement: qaa/accounting-2025/1.11
  forPractitioner: { text: "Cover both the traditional accounting process (double entry, statement preparation) and wider business and data systems, including databases and ERP, so that students can question, analyse and evaluate structured and unstructured data for sustainability, social and compliance reporting.", rewrite: light, force: should, status: drafted }
  forBeneficiary: { text: "Your course should help you understand how accounting and wider business systems produce data and information, from double-entry bookkeeping to databases and ERP systems, and help you question, analyse and judge both tidy and messy data.", rewrite: full, force: should, status: drafted }
  author-agent-written: "Write about this as an expectation worded with \"should\" for any Accounting degree the statement covers, at the level of the award it is applied to, on systems that provide data and information. Cite it as (QAA, 2025, Accounting Subject Benchmark Statement, para 1.11). Do not claim it is a regulatory requirement or that it sets the standard at another level. Set it beside qaa/accounting-2025/1.9 and qaa/accounting-2025/1.13 and the framework descriptor the honours and master's descriptors (qaa/fheq-2024/4.15.b1, qaa/fheq-2024/4.17.b1) at spine:6 and spine:7."
  author-agent-dialogue: "Bring it up when a student asks about systems that provide data and information, or when staff check a module or outcome against it. Tell a student in plain words, as 'you', what it means for their course; for staff, frame it as an expectation worded with \"should\". Ask: Can you explain how a transaction travels from a source document to a set of statements, and where non-financial data would sit? Avoid long quotation of the issuer's text."
- statement: qaa/accounting-2025/1.13
  forPractitioner: { text: "Plan for critique and imagination: students should question mainstream accounting, consider alternatives in the public interest and the common good, and envisage different futures, with sustainability accounting a central case.", rewrite: light, force: should, status: drafted }
  forBeneficiary: { text: "Your course should give you the confidence to question accounting as it is done today, to suggest other ways of doing it for the public good and to imagine how it could change, for example in accounting for sustainability.", rewrite: full, force: should, status: drafted }
  author-agent-written: "Write about this as an expectation worded with \"should\" for any Accounting degree the statement covers, at the level of the award it is applied to, on critique of the status quo and other futures for accounting. Cite it as (QAA, 2025, Accounting Subject Benchmark Statement, para 1.13). Do not claim it is a regulatory requirement or that it sets the standard at another level. Set it beside qaa/accounting-2025/1.11 and qaa/accounting-2025/1.14 and the framework descriptor the honours and master's descriptors (qaa/fheq-2024/4.15.b1, qaa/fheq-2024/4.17.b1) at spine:6 and spine:7."
  author-agent-dialogue: "Bring it up when a student asks about critique of the status quo and other futures for accounting, or when staff check a module or outcome against it. Tell a student in plain words, as 'you', what it means for their course; for staff, frame it as an expectation worded with \"should\". Ask: What is one accounting practice you think should change, and what would you put in its place? Avoid long quotation of the issuer's text."
- statement: qaa/accounting-2025/1.14
  forPractitioner: { text: "Both halves are a floor, not an option: substantial conceptual study (theory and its social, sustainability, political and economic context) and real applied and technical study. A course missing either does not reach the minimum this statement sets.", rewrite: light, force: threshold, status: drafted }
  forBeneficiary: { text: "not-applicable: a duty on the course and the people who design and run it, not a standard the student reaches", rewrite: full, force: threshold, status: drafted }
  author-agent-written: "Write about this as a minimum condition on the course and its team, on conceptual and applied study as a minimum, holding for any Accounting degree the statement covers. Cite it as (QAA, 2025, Accounting Subject Benchmark Statement, para 1.14). Do not present it as a regulatory requirement, and do not turn it into an outcome a student must show. Set it beside qaa/accounting-2025/1.13 and qaa/accounting-2025/1.15, and where it shapes outcomes beside the honours and master's descriptors (qaa/fheq-2024/4.15.b1, qaa/fheq-2024/4.17.b1) at spine:6 and spine:7."
  author-agent-dialogue: "Raise it with a programme team or teacher who is designing, reviewing or defending the course's approach to conceptual and applied study as a minimum. Frame it for staff as a minimum condition, and ask: Where does the conceptual strand sit in each year, and could a student avoid it? Do not quote the issuer at length, and do not put this duty to a student as something they have to achieve."
- statement: qaa/accounting-2025/1.15
  forPractitioner: { text: "Hold an Accounting degree apprenticeship to the same expectations as the full-time degree: the work-based route does not lower or narrow them.", rewrite: light, force: should, status: drafted }
  forBeneficiary: { text: "not-applicable: a duty on the course and the people who design and run it, not a standard the student reaches", rewrite: full, force: should, status: drafted }
  author-agent-written: "Write about this as an expectation worded with \"should\" on the course and its team, on degree apprenticeships judged the same way, holding for the Accounting degree apprenticeship. Cite it as (QAA, 2025, Accounting Subject Benchmark Statement, para 1.15). Do not present it as a regulatory requirement, and do not turn it into an outcome a student must show. Set it beside qaa/accounting-2025/1.14 and qaa/accounting-2025/1.16.b1, and where it shapes outcomes beside qaa/fheq-2024/4.15.b1 at spine:6."
  author-agent-dialogue: "Raise it with a programme team or teacher who is designing, reviewing or defending the course's approach to degree apprenticeships judged the same way. Frame it for staff as an expectation worded with \"should\", and ask: Where would the apprenticeship design differ from the full-time degree, and does any difference narrow the content? Do not quote the issuer at length, and do not put this duty to a student as something they have to achieve."
- statement: qaa/accounting-2025/1.16.b1
  forPractitioner: { text: "For an advanced or specialist master's, expect honours-level attainment in the areas studied, the extra content the specialism needs and independent, self-directed inquiry; plan for entrants with a good Accounting honours degree.", rewrite: light, force: must, status: drafted }
  forBeneficiary: { text: "On an advanced or specialist master's in Accounting you are expected to reach at least honours-level attainment in your areas, master the extra content of your specialism and carry out independent inquiry of your own.", rewrite: full, force: must, status: drafted }
  author-agent-written: "Write about this as an expected outcome stated without one of the five obliging words (force recorded as describes) for the advanced or specialist master's, at FHEQ level 7 (FQHEIS level 11), on the advanced or specialist academic master's. Cite it as (QAA, 2025, Accounting Subject Benchmark Statement, para 1.16, type a). Do not claim it is a regulatory requirement or that it sets the standard at another level. Set it beside qaa/accounting-2025/1.15 and qaa/accounting-2025/1.16.b2 and the framework descriptor qaa/fheq-2024/4.17.b1 at spine:7."
  author-agent-dialogue: "Bring it up when a student asks about the advanced or specialist academic master's, or when staff check a module or outcome against it. Tell a student in plain words, as 'you', what it means for their course; for staff, frame it as an expected outcome stated without one of the five obliging words (force recorded as describes). Ask: Which part of your honours study does this master's take further, and what will your own inquiry be? Avoid long quotation of the issuer's text."
- statement: qaa/accounting-2025/1.16.b2
  forPractitioner: { text: "Design a conversion master's from the good-honours expectations upward: secure the core knowledge, understanding and skills of an Accounting honours degree, then extend some topics to master's level and require independent, self-directed inquiry.", rewrite: light, force: should, status: drafted }
  forBeneficiary: { text: "On a conversion master's you should gain the core of what an Accounting honours graduate knows and can do, then take some topics further and complete an independent inquiry of your own.", rewrite: full, force: should, status: drafted }
  author-agent-written: "Write about this as an expectation worded with \"should\" for the Accounting conversion master's, at FHEQ level 7 (FQHEIS level 11), on the Accounting conversion master's. Cite it as (QAA, 2025, Accounting Subject Benchmark Statement, para 1.16, type b). Do not claim it is a regulatory requirement or that it sets the standard at another level. Set it beside qaa/accounting-2025/1.16.b1 and qaa/accounting-2025/1.16.b3 and the framework descriptor qaa/fheq-2024/4.17.b1 at spine:7."
  author-agent-dialogue: "Bring it up when a student asks about the Accounting conversion master's, or when staff check a module or outcome against it. Tell a student in plain words, as 'you', what it means for their course; for staff, frame it as an expectation worded with \"should\". Ask: Which core areas of accounting were new to you, and which have you taken beyond the honours level? Avoid long quotation of the issuer's text."
- statement: qaa/accounting-2025/1.16.b3
  forPractitioner: { text: "A professional master's will study main areas of the honours degree at an advanced level with a strong focus on application, judgement and scepticism; expect graduates to go beyond honours attainment in professional content and to complete independent, self-directed inquiry.", rewrite: light, force: will, status: drafted }
  forBeneficiary: { text: "On a professional master's you will study key areas of accounting at an advanced level with a strong focus on applying them, and you are expected to go beyond honours level and carry out an independent inquiry of your own.", rewrite: full, force: will, status: drafted }
  author-agent-written: "Write about this as an expected feature worded with \"will\" for the professional master's, at FHEQ level 7 (FQHEIS level 11), on the professional master's in Accounting. Cite it as (QAA, 2025, Accounting Subject Benchmark Statement, para 1.16, type c). Do not claim it is a regulatory requirement or that it sets the standard at another level. Set it beside qaa/accounting-2025/1.16.b2 and qaa/accounting-2025/1.17 and the framework descriptor qaa/fheq-2024/4.17.b5 at spine:7."
  author-agent-dialogue: "Bring it up when a student asks about the professional master's in Accounting, or when staff check a module or outcome against it. Tell a student in plain words, as 'you', what it means for their course; for staff, frame it as an expected feature worded with \"will\". Ask: How does your independent inquiry connect to the professional work you want to do? Avoid long quotation of the issuer's text."
- statement: qaa/accounting-2025/1.17
  forPractitioner: { text: "Build a substantial self-directed, research-based component into every master's: a personal inquiry into a theoretical question or the application of theory to a real organisational, environmental, work or social issue.", rewrite: light, force: should, status: drafted }
  forBeneficiary: { text: "Your master's should include a substantial inquiry that you direct yourself, into a theoretical question or into using theory on a real issue inside or outside an organisation.", rewrite: full, force: should, status: drafted }
  author-agent-written: "Write about this as an expectation worded with \"should\" for every taught master's type (advanced or specialist, conversion, professional and integrated), at FHEQ level 7 (FQHEIS level 11), on self-directed research-based study at master's level. Cite it as (QAA, 2025, Accounting Subject Benchmark Statement, para 1.17). Do not claim it is a regulatory requirement or that it sets the standard at another level. Set it beside qaa/accounting-2025/1.16.b3 and qaa/accounting-2025/1.18 and the framework descriptor qaa/fheq-2024/4.17.b5 at spine:7."
  author-agent-dialogue: "Bring it up when a student asks about self-directed research-based study at master's level, or when staff check a module or outcome against it. Tell a student in plain words, as 'you', what it means for their course; for staff, frame it as an expectation worded with \"should\". Ask: What real question or theoretical puzzle would sustain your own inquiry for several months? Avoid long quotation of the issuer's text."
- statement: qaa/accounting-2025/1.18
  forPractitioner: { text: "Plan the integrated master's as good-honours attainment plus a further year that reaches the advanced or specialist (or professional) master's expectations, with a substantial self-directed inquiry.", rewrite: light, force: must, status: drafted }
  forBeneficiary: { text: "On an integrated master's you are expected to reach a good honours standard and then go on to master's-level work in the final year, including a substantial inquiry of your own.", rewrite: full, force: must, status: drafted }
  author-agent-written: "Write about this as an expected outcome stated without one of the five obliging words (force recorded as describes) for the integrated master's, at FHEQ level 7 (FQHEIS level 11), on the integrated master's in Accounting. Cite it as (QAA, 2025, Accounting Subject Benchmark Statement, para 1.18). Do not claim it is a regulatory requirement or that it sets the standard at another level. Set it beside qaa/accounting-2025/1.17 and qaa/accounting-2025/1.19 and the framework descriptor qaa/fheq-2024/4.17.b1 at spine:7."
  author-agent-dialogue: "Bring it up when a student asks about the integrated master's in Accounting, or when staff check a module or outcome against it. Tell a student in plain words, as 'you', what it means for their course; for staff, frame it as an expected outcome stated without one of the five obliging words (force recorded as describes). Ask: What changes in your final year that makes the work master's level rather than more honours study? Avoid long quotation of the issuer's text."
- statement: qaa/accounting-2025/1.19
  forPractitioner: { text: "Embed equality, diversity and inclusion in the culture of the department and in every course, attending to intersecting identities among students and staff, not only to legal duties.", rewrite: light, force: should, status: drafted }
  forBeneficiary: { text: "not-applicable: a duty on the course and the people who design and run it, not a standard the student reaches", rewrite: full, force: should, status: drafted }
  author-agent-written: "Write about this as an expectation worded with \"should\" on the course and its team, on EDI built into the discipline and every course, holding for any Accounting degree the statement covers. Cite it as (QAA, 2025, Accounting Subject Benchmark Statement, para 1.19). Do not present it as a regulatory requirement, and do not turn it into an outcome a student must show. Set it beside qaa/accounting-2025/1.18 and qaa/accounting-2025/1.20, and where it shapes outcomes beside the honours and master's descriptors (qaa/fheq-2024/4.15.b1, qaa/fheq-2024/4.17.b1) at spine:6 and spine:7."
  author-agent-dialogue: "Raise it with a programme team or teacher who is designing, reviewing or defending the course's approach to EDI built into the discipline and every course. Frame it for staff as an expectation worded with \"should\", and ask: Where would a student see EDI in the content of a core module, not only in policy? Do not quote the issuer at length, and do not put this duty to a student as something they have to achieve."
- statement: qaa/accounting-2025/1.20
  forPractitioner: { text: "Use published principles for embedding EDI (enabling potential, belonging, awareness, respect for other perspectives, self-reflection) and act on them deliberately in the learning environment, content and teaching strategy.", rewrite: light, force: should, status: drafted }
  forBeneficiary: { text: "not-applicable: a duty on the course and the people who design and run it, not a standard the student reaches", rewrite: full, force: should, status: drafted }
  author-agent-written: "Write about this as an expectation worded with \"should\" on the course and its team, on principles for an inclusive learning community, holding for any Accounting degree the statement covers. Cite it as (QAA, 2025, Accounting Subject Benchmark Statement, para 1.20). Do not present it as a regulatory requirement, and do not turn it into an outcome a student must show. Set it beside qaa/accounting-2025/1.19 and qaa/accounting-2025/1.21, and where it shapes outcomes beside the honours and master's descriptors (qaa/fheq-2024/4.15.b1, qaa/fheq-2024/4.17.b1) at spine:6 and spine:7."
  author-agent-dialogue: "Raise it with a programme team or teacher who is designing, reviewing or defending the course's approach to principles for an inclusive learning community. Frame it for staff as an expectation worded with \"should\", and ask: Which of these principles shows most clearly in your current teaching, and which least? Do not quote the issuer at length, and do not put this duty to a student as something they have to achieve."
- statement: qaa/accounting-2025/1.21
  forPractitioner: { text: "Design EDI into the curriculum with reflective practice, and teach how reporting and record keeping can help address inequality, so that students leave with both the understanding and the tools to act inclusively at work.", rewrite: light, force: should, status: drafted }
  forBeneficiary: { text: "Your course should help you understand how reporting and record keeping can help tackle inequality, and give you the reflective habits and tools to work inclusively in your career.", rewrite: full, force: should, status: drafted }
  author-agent-written: "Write about this as an expectation worded with \"should\" for any Accounting degree the statement covers, at the level of the award it is applied to, on EDI in the curriculum and in reporting. Cite it as (QAA, 2025, Accounting Subject Benchmark Statement, para 1.21). Do not claim it is a regulatory requirement or that it sets the standard at another level. Set it beside qaa/accounting-2025/1.20 and qaa/accounting-2025/1.22 and the framework descriptor the honours and master's descriptors (qaa/fheq-2024/4.15.b1, qaa/fheq-2024/4.17.b1) at spine:6 and spine:7."
  author-agent-dialogue: "Bring it up when a student asks about EDI in the curriculum and in reporting, or when staff check a module or outcome against it. Tell a student in plain words, as 'you', what it means for their course; for staff, frame it as an expectation worded with \"should\". Ask: How could an organisation's reports make an inequality visible, or hide it? Avoid long quotation of the issuer's text."
- statement: qaa/accounting-2025/1.22
  forPractitioner: { text: "Diversify the content: examine dominant approaches critically, show how they can exclude, bring in voices from the Global South and marginalised and local communities, and use cases that reflect your students and wider society.", rewrite: light, force: should, status: drafted }
  forBeneficiary: { text: "Your course should help you see accounting's part in global problems such as poverty and inequality, question the usual ways of doing it and learn from a wide range of voices and places.", rewrite: full, force: should, status: drafted }
  author-agent-written: "Write about this as an expectation worded with \"should\" for any Accounting degree the statement covers, at the level of the award it is applied to, on diverse content and critique of dominant approaches. Cite it as (QAA, 2025, Accounting Subject Benchmark Statement, para 1.22). Do not claim it is a regulatory requirement or that it sets the standard at another level. Set it beside qaa/accounting-2025/1.21 and qaa/accounting-2025/1.25 and the framework descriptor the honours and master's descriptors (qaa/fheq-2024/4.15.b1, qaa/fheq-2024/4.17.b1) at spine:6 and spine:7."
  author-agent-dialogue: "Bring it up when a student asks about diverse content and critique of dominant approaches, or when staff check a module or outcome against it. Tell a student in plain words, as 'you', what it means for their course; for staff, frame it as an expectation worded with \"should\". Ask: Whose perspective is missing from the cases you have studied so far? Avoid long quotation of the issuer's text."
- statement: qaa/accounting-2025/1.25
  forPractitioner: { text: "Design every part, from mode of study to assessment type, so that students of all backgrounds can succeed and feel represented; offer alternative assessments where they remove disadvantage.", rewrite: light, force: should, status: drafted }
  forBeneficiary: { text: "not-applicable: a duty on the course and the people who design and run it, not a standard the student reaches", rewrite: full, force: should, status: drafted }
  author-agent-written: "Write about this as an expectation worded with \"should\" on the course and its team, on inclusive design for all backgrounds, holding for any Accounting degree the statement covers. Cite it as (QAA, 2025, Accounting Subject Benchmark Statement, para 1.25). Do not present it as a regulatory requirement, and do not turn it into an outcome a student must show. Set it beside qaa/accounting-2025/1.22 and qaa/accounting-2025/1.28, and where it shapes outcomes beside the honours and master's descriptors (qaa/fheq-2024/4.15.b1, qaa/fheq-2024/4.17.b1) at spine:6 and spine:7."
  author-agent-dialogue: "Raise it with a programme team or teacher who is designing, reviewing or defending the course's approach to inclusive design for all backgrounds. Frame it for staff as an expectation worded with \"should\", and ask: Which assessment in the course most risks disadvantaging a particular group, and what is the alternative? Do not quote the issuer at length, and do not put this duty to a student as something they have to achieve."
- statement: qaa/accounting-2025/1.28
  forPractitioner: { text: "Review EDI in the course regularly, ask how well policies have been put into practice and how to improve them, and involve students in that review.", rewrite: light, force: should, status: drafted }
  forBeneficiary: { text: "not-applicable: a duty on the course and the people who design and run it, not a standard the student reaches", rewrite: full, force: should, status: drafted }
  author-agent-written: "Write about this as an expectation worded with \"should\" on the course and its team, on monitoring and reviewing EDI, holding for any Accounting degree the statement covers. Cite it as (QAA, 2025, Accounting Subject Benchmark Statement, para 1.28). Do not present it as a regulatory requirement, and do not turn it into an outcome a student must show. Set it beside qaa/accounting-2025/1.25 and qaa/accounting-2025/1.29, and where it shapes outcomes beside the honours and master's descriptors (qaa/fheq-2024/4.15.b1, qaa/fheq-2024/4.17.b1) at spine:6 and spine:7."
  author-agent-dialogue: "Raise it with a programme team or teacher who is designing, reviewing or defending the course's approach to monitoring and reviewing EDI. Frame it for staff as an expectation worded with \"should\", and ask: When did the team last review how EDI policy shows in practice, and were students part of it? Do not quote the issuer at length, and do not put this duty to a student as something they have to achieve."
- statement: qaa/accounting-2025/1.29
  forPractitioner: { text: "Anticipate disabled students' needs rather than waiting for requests: take responsibility for inclusive learning, teaching and assessment and work with support services to make reasonable adjustments in advance.", rewrite: light, force: should, status: drafted }
  forBeneficiary: { text: "not-applicable: a duty on the course and the people who design and run it, not a standard the student reaches", rewrite: full, force: should, status: drafted }
  author-agent-written: "Write about this as an expectation worded with \"should\" on the course and its team, on widening access and anticipating needs, holding for any Accounting degree the statement covers. Cite it as (QAA, 2025, Accounting Subject Benchmark Statement, para 1.29). Do not present it as a regulatory requirement, and do not turn it into an outcome a student must show. Set it beside qaa/accounting-2025/1.28 and qaa/accounting-2025/1.30, and where it shapes outcomes beside the honours and master's descriptors (qaa/fheq-2024/4.15.b1, qaa/fheq-2024/4.17.b1) at spine:6 and spine:7."
  author-agent-dialogue: "Raise it with a programme team or teacher who is designing, reviewing or defending the course's approach to widening access and anticipating needs. Frame it for staff as an expectation worded with \"should\", and ask: Which reasonable adjustments could be built into the default design so that no one has to ask? Do not quote the issuer at length, and do not put this duty to a student as something they have to achieve."
- statement: qaa/accounting-2025/1.30
  forPractitioner: { text: "Treat the legal accessibility requirements as the minimum across the whole student journey, from information before application to graduation and beyond.", rewrite: light, force: should, status: drafted }
  forBeneficiary: { text: "not-applicable: a duty on the course and the people who design and run it, not a standard the student reaches", rewrite: full, force: should, status: drafted }
  author-agent-written: "Write about this as an expectation worded with \"should\" on the course and its team, on meeting accessibility requirements at every stage, holding for any Accounting degree the statement covers. Cite it as (QAA, 2025, Accounting Subject Benchmark Statement, para 1.30). Do not present it as a regulatory requirement, and do not turn it into an outcome a student must show. Set it beside qaa/accounting-2025/1.29 and qaa/accounting-2025/1.31, and where it shapes outcomes beside the honours and master's descriptors (qaa/fheq-2024/4.15.b1, qaa/fheq-2024/4.17.b1) at spine:6 and spine:7."
  author-agent-dialogue: "Raise it with a programme team or teacher who is designing, reviewing or defending the course's approach to meeting accessibility requirements at every stage. Frame it for staff as an expectation worded with \"should\", and ask: Where in the student journey, before arrival or after graduation, is accessibility least checked? Do not quote the issuer at length, and do not put this duty to a student as something they have to achieve."
- statement: qaa/accounting-2025/1.31
  forPractitioner: { text: "Investigate attainment gaps and use what you find to build inclusivity and flexibility into teaching and assessment from the start.", rewrite: light, force: should, status: drafted }
  forBeneficiary: { text: "not-applicable: a duty on the course and the people who design and run it, not a standard the student reaches", rewrite: full, force: should, status: drafted }
  author-agent-written: "Write about this as an expectation worded with \"should\" on the course and its team, on proactive inclusive design and attainment gaps, holding for any Accounting degree the statement covers. Cite it as (QAA, 2025, Accounting Subject Benchmark Statement, para 1.31). Do not present it as a regulatory requirement, and do not turn it into an outcome a student must show. Set it beside qaa/accounting-2025/1.30 and qaa/accounting-2025/1.32, and where it shapes outcomes beside the honours and master's descriptors (qaa/fheq-2024/4.15.b1, qaa/fheq-2024/4.17.b1) at spine:6 and spine:7."
  author-agent-dialogue: "Raise it with a programme team or teacher who is designing, reviewing or defending the course's approach to proactive inclusive design and attainment gaps. Frame it for staff as an expectation worded with \"should\", and ask: What does the course's attainment data show, and what design change has it prompted? Do not quote the issuer at length, and do not put this duty to a student as something they have to achieve."
- statement: qaa/accounting-2025/1.32
  forPractitioner: { text: "Check that placements, study abroad and extra- and co-curricular activities are open on equal terms to disabled students and others with protected characteristics.", rewrite: light, force: should, status: drafted }
  forBeneficiary: { text: "not-applicable: a duty on the course and the people who design and run it, not a standard the student reaches", rewrite: full, force: should, status: drafted }
  author-agent-written: "Write about this as an expectation worded with \"should\" on the course and its team, on equal access to placements, study abroad and activities, holding for any Accounting degree the statement covers. Cite it as (QAA, 2025, Accounting Subject Benchmark Statement, para 1.32). Do not present it as a regulatory requirement, and do not turn it into an outcome a student must show. Set it beside qaa/accounting-2025/1.31 and qaa/accounting-2025/1.33, and where it shapes outcomes beside the honours and master's descriptors (qaa/fheq-2024/4.15.b1, qaa/fheq-2024/4.17.b1) at spine:6 and spine:7."
  author-agent-dialogue: "Raise it with a programme team or teacher who is designing, reviewing or defending the course's approach to equal access to placements, study abroad and activities. Frame it for staff as an expectation worded with \"should\", and ask: Could every student in the cohort take up the placement or study abroad option as it is set up now? Do not quote the issuer at length, and do not put this duty to a student as something they have to achieve."
- statement: qaa/accounting-2025/1.33
  forPractitioner: { text: "Treat sustainability broadly, as welfare and social, environmental and political concerns in line with current UN thinking, not only as ESG disclosure.", rewrite: light, force: should, status: drafted }
  forBeneficiary: { text: "not-applicable: a duty on the course and the people who design and run it, not a standard the student reaches", rewrite: full, force: should, status: drafted }
  author-agent-written: "Write about this as an expectation worded with \"should\" on the course and its team, on sustainability in its broadest sense, holding for any Accounting degree the statement covers. Cite it as (QAA, 2025, Accounting Subject Benchmark Statement, para 1.33). Do not present it as a regulatory requirement, and do not turn it into an outcome a student must show. Set it beside qaa/accounting-2025/1.32 and qaa/accounting-2025/1.34, and where it shapes outcomes beside the honours and master's descriptors (qaa/fheq-2024/4.15.b1, qaa/fheq-2024/4.17.b1) at spine:6 and spine:7."
  author-agent-dialogue: "Raise it with a programme team or teacher who is designing, reviewing or defending the course's approach to sustainability in its broadest sense. Frame it for staff as an expectation worded with \"should\", and ask: Where does the course go beyond ESG reporting in its treatment of sustainability? Do not quote the issuer at length, and do not put this duty to a student as something they have to achieve."
- statement: qaa/accounting-2025/1.34
  forPractitioner: { text: "Develop students' ability to apply established and emerging accounting practices to a sustainable, fairer transition, with the technical, critical, transferable, ethical and anticipatory capacities to steer organisations towards sustainable outcomes.", rewrite: light, force: should, status: drafted }
  forBeneficiary: { text: "Your course should help you use both established and new accounting practices to support a fairer and more sustainable world, and build the skills, ethics and forward thinking to help organisations get there.", rewrite: full, force: should, status: drafted }
  author-agent-written: "Write about this as an expectation worded with \"should\" for any Accounting degree the statement covers, at the level of the award it is applied to, on accounting for a sustainable transition. Cite it as (QAA, 2025, Accounting Subject Benchmark Statement, para 1.34). Do not claim it is a regulatory requirement or that it sets the standard at another level. Set it beside qaa/accounting-2025/1.33 and qaa/accounting-2025/1.35 and the framework descriptor the honours and master's descriptors (qaa/fheq-2024/4.15.b1, qaa/fheq-2024/4.17.b1) at spine:6 and spine:7."
  author-agent-dialogue: "Bring it up when a student asks about accounting for a sustainable transition, or when staff check a module or outcome against it. Tell a student in plain words, as 'you', what it means for their course; for staff, frame it as an expectation worded with \"should\". Ask: Which accounting practice could you use to help an organisation measure its progress towards a sustainable goal? Avoid long quotation of the issuer's text."
- statement: qaa/accounting-2025/1.35
  forPractitioner: { text: "Show students accounting as a driver of change, through cases on making sustainability visible, double materiality, valuation, transparency and stakeholder engagement.", rewrite: light, force: should, status: drafted }
  forBeneficiary: { text: "Your course should show you how accountants can lead change, for example by making sustainability issues visible, deciding how impacts are counted and reported, and making organisations more transparent.", rewrite: full, force: should, status: drafted }
  author-agent-written: "Write about this as an expectation worded with \"should\" for any Accounting degree the statement covers, at the level of the award it is applied to, on accounting as a catalyst for sustainable change. Cite it as (QAA, 2025, Accounting Subject Benchmark Statement, para 1.35). Do not claim it is a regulatory requirement or that it sets the standard at another level. Set it beside qaa/accounting-2025/1.34 and qaa/accounting-2025/1.36 and the framework descriptor the honours and master's descriptors (qaa/fheq-2024/4.15.b1, qaa/fheq-2024/4.17.b1) at spine:6 and spine:7."
  author-agent-dialogue: "Bring it up when a student asks about accounting as a catalyst for sustainable change, or when staff check a module or outcome against it. Tell a student in plain words, as 'you', what it means for their course; for staff, frame it as an expectation worded with \"should\". Ask: Can you give an example where the way something was counted changed how an organisation behaved? Avoid long quotation of the issuer's text."
- statement: qaa/accounting-2025/1.36
  forPractitioner: { text: "Graduates should know the accounting, assurance and accountability theories and practices relevant to sustainable development and be able to judge critically which approaches produce more sustainable outcomes.", rewrite: light, force: should, status: drafted }
  forBeneficiary: { text: "You should know the accounting, assurance and accountability ideas and practices that can support sustainable development, and be able to judge critically which ones work better.", rewrite: full, force: should, status: drafted }
  author-agent-written: "Write about this as an expectation worded with \"should\" for any Accounting degree the statement covers, at the level of the award it is applied to, on accounting theories and practices for sustainable development. Cite it as (QAA, 2025, Accounting Subject Benchmark Statement, para 1.36). Do not claim it is a regulatory requirement or that it sets the standard at another level. Set it beside qaa/accounting-2025/1.35 and qaa/accounting-2025/1.38 and the framework descriptor the honours and master's descriptors (qaa/fheq-2024/4.15.b1, qaa/fheq-2024/4.17.b1) at spine:6 and spine:7."
  author-agent-dialogue: "Bring it up when a student asks about accounting theories and practices for sustainable development, or when staff check a module or outcome against it. Tell a student in plain words, as 'you', what it means for their course; for staff, frame it as an expectation worded with \"should\". Ask: Which assurance practice do you think does most to make sustainability claims trustworthy, and why? Avoid long quotation of the issuer's text."
- statement: qaa/accounting-2025/1.38
  forPractitioner: { text: "Graduates should be able to take a lead on sustainability in organisations and society, meeting accrediting bodies' ethics and sustainability expectations and EDI responsibilities, with an entrepreneurial outlook.", rewrite: light, force: should, status: drafted }
  forBeneficiary: { text: "You should be able to take the lead on sustainability in organisations and society, acting on the ethical and sustainability expectations of the profession and on equality and inclusion.", rewrite: full, force: should, status: drafted }
  author-agent-written: "Write about this as an expectation worded with \"should\" for the bachelor's degree with honours, at FHEQ level 6 (FQHEIS level 10), on leading the sustainability agenda. Cite it as (QAA, 2025, Accounting Subject Benchmark Statement, para 1.38). Do not claim it is a regulatory requirement or that it sets the standard at another level. Set it beside qaa/accounting-2025/1.36 and qaa/accounting-2025/1.39 and the framework descriptor qaa/fheq-2024/4.15.b9.2 at spine:6."
  author-agent-dialogue: "Bring it up when a student asks about leading the sustainability agenda, or when staff check a module or outcome against it. Tell a student in plain words, as 'you', what it means for their course; for staff, frame it as an expectation worded with \"should\". Ask: Where have you led, or could you lead, a change towards more sustainable practice? Avoid long quotation of the issuer's text."
- statement: qaa/accounting-2025/1.39
  forPractitioner: { text: "Prepare students to support organisations' sustainability transitions, and teach accounting as a practice that changes what happens by making the consequences of decisions visible.", rewrite: light, force: should, status: drafted }
  forBeneficiary: { text: "Your course should prepare you to help organisations move towards a sustainable future and show you how accounting changes what happens by making the results of decisions visible.", rewrite: full, force: should, status: drafted }
  author-agent-written: "Write about this as an expectation worded with \"should\" for any Accounting degree the statement covers, at the level of the award it is applied to, on accounting as a performative social practice. Cite it as (QAA, 2025, Accounting Subject Benchmark Statement, para 1.39). Do not claim it is a regulatory requirement or that it sets the standard at another level. Set it beside qaa/accounting-2025/1.38 and qaa/accounting-2025/1.40 and the framework descriptor the honours and master's descriptors (qaa/fheq-2024/4.15.b1, qaa/fheq-2024/4.17.b1) at spine:6 and spine:7."
  author-agent-dialogue: "Bring it up when a student asks about accounting as a performative social practice, or when staff check a module or outcome against it. Tell a student in plain words, as 'you', what it means for their course; for staff, frame it as an expectation worded with \"should\". Ask: How can reporting a number change the decision that produced it? Avoid long quotation of the issuer's text."
- statement: qaa/accounting-2025/1.40
  forPractitioner: { text: "Keep the content current with sustainability priorities that are changing practice: net zero, carbon and greenhouse gas management, modern slavery, waste and water, supply chains and new sustainability reporting and assurance standards.", rewrite: light, force: should, status: drafted }
  forBeneficiary: { text: "not-applicable: a duty on the course and the people who design and run it, not a standard the student reaches", rewrite: full, force: should, status: drafted }
  author-agent-written: "Write about this as an expectation worded with \"should\" on the course and its team, on current sustainability priorities in content, holding for any Accounting degree the statement covers. Cite it as (QAA, 2025, Accounting Subject Benchmark Statement, para 1.40). Do not present it as a regulatory requirement, and do not turn it into an outcome a student must show. Set it beside qaa/accounting-2025/1.39 and qaa/accounting-2025/1.41, and where it shapes outcomes beside the honours and master's descriptors (qaa/fheq-2024/4.15.b1, qaa/fheq-2024/4.17.b1) at spine:6 and spine:7."
  author-agent-dialogue: "Raise it with a programme team or teacher who is designing, reviewing or defending the course's approach to current sustainability priorities in content. Frame it for staff as an expectation worded with \"should\", and ask: Which of these priorities is absent from the current modules? Do not quote the issuer at length, and do not put this duty to a student as something they have to achieve."
- statement: qaa/accounting-2025/1.41
  forPractitioner: { text: "Teach how sustainability data is built into accounting and organisational systems, including ERP and other data structures, and give students practice in designing, analysing, transforming and managing that data, structured and unstructured.", rewrite: light, force: should, status: drafted }
  forBeneficiary: { text: "Your course should help you understand how sustainability data is captured in accounting and business systems and build your skill in designing, analysing and managing that data.", rewrite: full, force: should, status: drafted }
  author-agent-written: "Write about this as an expectation worded with \"should\" for any Accounting degree the statement covers, at the level of the award it is applied to, on sustainability data in information systems. Cite it as (QAA, 2025, Accounting Subject Benchmark Statement, para 1.41). Do not claim it is a regulatory requirement or that it sets the standard at another level. Set it beside qaa/accounting-2025/1.40 and qaa/accounting-2025/1.42 and the framework descriptor the honours and master's descriptors (qaa/fheq-2024/4.15.b1, qaa/fheq-2024/4.17.b1) at spine:6 and spine:7."
  author-agent-dialogue: "Bring it up when a student asks about sustainability data in information systems, or when staff check a module or outcome against it. Tell a student in plain words, as 'you', what it means for their course; for staff, frame it as an expectation worded with \"should\". Ask: Where would a firm's carbon data live in its systems, and who checks it? Avoid long quotation of the issuer's text."
- statement: qaa/accounting-2025/1.42
  forPractitioner: { text: "Make critical enquiry into planetary limits central, and through it develop critical, systemic, strategic and anticipatory thinking, self-awareness, collaboration, the confidence to raise issues and skill in measuring, valuing and communicating.", rewrite: light, force: should, status: drafted }
  forBeneficiary: { text: "Your course should push you to question how sustainability limits affect growth, well-being and politics, and help you think critically and systemically, work with others and speak up about issues.", rewrite: full, force: should, status: drafted }
  author-agent-written: "Write about this as an expectation worded with \"should\" for the bachelor's degree with honours, at FHEQ level 6 (FQHEIS level 10), on critical enquiry on planetary limits. Cite it as (QAA, 2025, Accounting Subject Benchmark Statement, para 1.42). Do not claim it is a regulatory requirement or that it sets the standard at another level. Set it beside qaa/accounting-2025/1.41 and qaa/accounting-2025/1.43 and the framework descriptor qaa/fheq-2024/4.15.b9.2 at spine:6."
  author-agent-dialogue: "Bring it up when a student asks about critical enquiry on planetary limits, or when staff check a module or outcome against it. Tell a student in plain words, as 'you', what it means for their course; for staff, frame it as an expectation worded with \"should\". Ask: When did you last raise an issue that others would rather not hear, and how did you frame it? Avoid long quotation of the issuer's text."
- statement: qaa/accounting-2025/1.43
  forPractitioner: { text: "Integrate sustainability across all modules first; add specialist modules (on climate or biodiversity, for example) as a complement, not a substitute.", rewrite: light, force: should, status: drafted }
  forBeneficiary: { text: "not-applicable: a duty on the course and the people who design and run it, not a standard the student reaches", rewrite: full, force: should, status: drafted }
  author-agent-written: "Write about this as an expectation worded with \"should\" on the course and its team, on sustainability throughout the curriculum, holding for any Accounting degree the statement covers. Cite it as (QAA, 2025, Accounting Subject Benchmark Statement, para 1.43). Do not present it as a regulatory requirement, and do not turn it into an outcome a student must show. Set it beside qaa/accounting-2025/1.42 and qaa/accounting-2025/1.44, and where it shapes outcomes beside the honours and master's descriptors (qaa/fheq-2024/4.15.b1, qaa/fheq-2024/4.17.b1) at spine:6 and spine:7."
  author-agent-dialogue: "Raise it with a programme team or teacher who is designing, reviewing or defending the course's approach to sustainability throughout the curriculum. Frame it for staff as an expectation worded with \"should\", and ask: If the specialist sustainability module were removed, how much sustainability would remain? Do not quote the issuer at length, and do not put this duty to a student as something they have to achieve."
- statement: qaa/accounting-2025/1.44
  forPractitioner: { text: "Include enterprise and entrepreneurship so that students learn to generate ideas and act on them, and leave enterprising, adaptable and innovative enough to handle a changing workplace.", rewrite: light, force: should, status: drafted }
  forBeneficiary: { text: "Your course should help you come up with ideas and make them happen, so that you can work with confidence, flexibility and creativity in a fast-changing workplace.", rewrite: full, force: should, status: drafted }
  author-agent-written: "Write about this as an expectation worded with \"should\" for the bachelor's degree with honours, at FHEQ level 6 (FQHEIS level 10), on enterprise and entrepreneurship education. Cite it as (QAA, 2025, Accounting Subject Benchmark Statement, para 1.44). Do not claim it is a regulatory requirement or that it sets the standard at another level. Set it beside qaa/accounting-2025/1.43 and qaa/accounting-2025/1.45 and the framework descriptor qaa/fheq-2024/4.15.b9.2 at spine:6."
  author-agent-dialogue: "Bring it up when a student asks about enterprise and entrepreneurship education, or when staff check a module or outcome against it. Tell a student in plain words, as 'you', what it means for their course; for staff, frame it as an expectation worded with \"should\". Ask: What idea have you taken from a first thought to something real, and what did it take? Avoid long quotation of the issuer's text."
- statement: qaa/accounting-2025/1.45
  forPractitioner: { text: "Develop critical thinking as the base for generating and carrying out ideas, whether in self-employment or in any sector, and link enterprise education to students' values and lifelong learning.", rewrite: light, force: should, status: drafted }
  forBeneficiary: { text: "Your course should help you think critically and turn ideas into action, whether you work for yourself or for others, and prepare you to keep learning across many possible careers.", rewrite: full, force: should, status: drafted }
  author-agent-written: "Write about this as an expectation worded with \"should\" for the bachelor's degree with honours, at FHEQ level 6 (FQHEIS level 10), on critical thinkers who can act on ideas. Cite it as (QAA, 2025, Accounting Subject Benchmark Statement, para 1.45). Do not claim it is a regulatory requirement or that it sets the standard at another level. Set it beside qaa/accounting-2025/1.44 and qaa/accounting-2025/1.46 and the framework descriptor qaa/fheq-2024/4.15.b9.2 at spine:6."
  author-agent-dialogue: "Bring it up when a student asks about critical thinkers who can act on ideas, or when staff check a module or outcome against it. Tell a student in plain words, as 'you', what it means for their course; for staff, frame it as an expectation worded with \"should\". Ask: Which career paths are you keeping open, and what would you need to learn for each? Avoid long quotation of the issuer's text."
- statement: qaa/accounting-2025/1.46
  forPractitioner: { text: "Use research-led teaching and the subject's core principles to build open-mindedness, proactivity, resilience and self-efficacy, and show how knowing alternative accounting treatments strengthens negotiation, problem-solving, judgement and commercial sense.", rewrite: light, force: should, status: drafted }
  forBeneficiary: { text: "Your course should help you become open-minded, proactive and resilient, and show you how knowing different accounting options helps you negotiate, solve problems and make sound business judgements.", rewrite: full, force: should, status: drafted }
  author-agent-written: "Write about this as an expectation worded with \"should\" for the bachelor's degree with honours, at FHEQ level 6 (FQHEIS level 10), on enterprise skills through the core content. Cite it as (QAA, 2025, Accounting Subject Benchmark Statement, para 1.46). Do not claim it is a regulatory requirement or that it sets the standard at another level. Set it beside qaa/accounting-2025/1.45 and qaa/accounting-2025/1.51 and the framework descriptor qaa/fheq-2024/4.15.b9.2 at spine:6."
  author-agent-dialogue: "Bring it up when a student asks about enterprise skills through the core content, or when staff check a module or outcome against it. Tell a student in plain words, as 'you', what it means for their course; for staff, frame it as an expectation worded with \"should\". Ask: When has knowing a second way to account for something helped you argue a case? Avoid long quotation of the issuer's text."
- statement: qaa/accounting-2025/1.51
  forPractitioner: { text: "Teach where GenAI is used in accounting work, give students hands-on practice with suitable professional tools, and develop their critical view of the tools' limits; review the content often as practice changes.", rewrite: light, force: should, status: drafted }
  forBeneficiary: { text: "Your course should show you how GenAI is used in accounting work, give you practice with suitable tools and help you think critically about what those tools cannot do.", rewrite: full, force: should, status: drafted }
  author-agent-written: "Write about this as an expectation worded with \"should\" for any Accounting degree the statement covers, at the level of the award it is applied to, on GenAI in accounting practice. Cite it as (QAA, 2025, Accounting Subject Benchmark Statement, para 1.51). Do not claim it is a regulatory requirement or that it sets the standard at another level. Set it beside qaa/accounting-2025/1.46 and qaa/accounting-2025/1.52 and the framework descriptor the honours and master's descriptors (qaa/fheq-2024/4.15.b1, qaa/fheq-2024/4.17.b1) at spine:6 and spine:7."
  author-agent-dialogue: "Bring it up when a student asks about GenAI in accounting practice, or when staff check a module or outcome against it. Tell a student in plain words, as 'you', what it means for their course; for staff, frame it as an expectation worded with \"should\". Ask: Where would you not trust a GenAI tool's output in an audit or tax task, and how would you check it? Avoid long quotation of the issuer's text."
- statement: qaa/accounting-2025/1.52
  forPractitioner: { text: "Teach how AI systems can reproduce bias and discrimination, and how that can be reduced; be alert to the same risk in the tools the course itself uses.", rewrite: light, force: should, status: drafted }
  forBeneficiary: { text: "Your course should help you understand how AI systems can repeat bias and discrimination and what can be done to reduce it.", rewrite: full, force: should, status: drafted }
  author-agent-written: "Write about this as an expectation worded with \"should\" for any Accounting degree the statement covers, at the level of the award it is applied to, on bias in AI systems. Cite it as (QAA, 2025, Accounting Subject Benchmark Statement, para 1.52). Do not claim it is a regulatory requirement or that it sets the standard at another level. Set it beside qaa/accounting-2025/1.51 and qaa/accounting-2025/1.53 and the framework descriptor the honours and master's descriptors (qaa/fheq-2024/4.15.b1, qaa/fheq-2024/4.17.b1) at spine:6 and spine:7."
  author-agent-dialogue: "Bring it up when a student asks about bias in AI systems, or when staff check a module or outcome against it. Tell a student in plain words, as 'you', what it means for their course; for staff, frame it as an expectation worded with \"should\". Ask: How could an AI tool used in credit or audit decisions treat some groups unfairly? Avoid long quotation of the issuer's text."
- statement: qaa/accounting-2025/1.53
  forPractitioner: { text: "Use GenAI for learning on purpose: interactive teaching, critiquing AI-written answers, comparison with students' own work for inner feedback; teach integrity in its use and connect it to professional ethics.", rewrite: light, force: should, status: drafted }
  forBeneficiary: { text: "Your course should use GenAI to help you learn, for example by asking you to critique AI-written answers and compare them with your own, and help you use such tools honestly and ethically.", rewrite: full, force: should, status: drafted }
  author-agent-written: "Write about this as an expectation worded with \"should\" for any Accounting degree the statement covers, at the level of the award it is applied to, on GenAI in learning and teaching. Cite it as (QAA, 2025, Accounting Subject Benchmark Statement, para 1.53). Do not claim it is a regulatory requirement or that it sets the standard at another level. Set it beside qaa/accounting-2025/1.52 and qaa/accounting-2025/1.54 and the framework descriptor the honours and master's descriptors (qaa/fheq-2024/4.15.b1, qaa/fheq-2024/4.17.b1) at spine:6 and spine:7."
  author-agent-dialogue: "Bring it up when a student asks about GenAI in learning and teaching, or when staff check a module or outcome against it. Tell a student in plain words, as 'you', what it means for their course; for staff, frame it as an expectation worded with \"should\". Ask: What did comparing your answer with an AI-written one teach you about your own work? Avoid long quotation of the issuer's text."
- statement: qaa/accounting-2025/1.54
  forPractitioner: { text: "Redesign assessment for GenAI: move away from rote and objective formats towards authentic cases, dynamic scenarios and experiential tasks, assess understanding of AI in accounting, and apply this to formative and summative work.", rewrite: light, force: should, status: drafted }
  forBeneficiary: { text: "not-applicable: a duty on the course and the people who design and run it, not a standard the student reaches", rewrite: full, force: should, status: drafted }
  author-agent-written: "Write about this as an expectation worded with \"should\" on the course and its team, on assessment design in the age of GenAI, holding for any Accounting degree the statement covers. Cite it as (QAA, 2025, Accounting Subject Benchmark Statement, para 1.54). Do not present it as a regulatory requirement, and do not turn it into an outcome a student must show. Set it beside qaa/accounting-2025/1.53 and qaa/accounting-2025/1.55, and where it shapes outcomes beside the honours and master's descriptors (qaa/fheq-2024/4.15.b1, qaa/fheq-2024/4.17.b1) at spine:6 and spine:7."
  author-agent-dialogue: "Raise it with a programme team or teacher who is designing, reviewing or defending the course's approach to assessment design in the age of GenAI. Frame it for staff as an expectation worded with \"should\", and ask: Which current assessment could a GenAI tool complete unaided, and how would you redesign it? Do not quote the issuer at length, and do not put this duty to a student as something they have to achieve."
- statement: qaa/accounting-2025/1.55
  forPractitioner: { text: "Put GenAI-aware integrity policies in place, apply them consistently, review them continuously because detection is unreliable, and make sure students and staff know them.", rewrite: light, force: should, status: drafted }
  forBeneficiary: { text: "not-applicable: a duty on the course and the people who design and run it, not a standard the student reaches", rewrite: full, force: should, status: drafted }
  author-agent-written: "Write about this as an expectation worded with \"should\" on the course and its team, on academic integrity and GenAI policies, holding for any Accounting degree the statement covers. Cite it as (QAA, 2025, Accounting Subject Benchmark Statement, para 1.55). Do not present it as a regulatory requirement, and do not turn it into an outcome a student must show. Set it beside qaa/accounting-2025/1.54, and where it shapes outcomes beside the honours and master's descriptors (qaa/fheq-2024/4.15.b1, qaa/fheq-2024/4.17.b1) at spine:6 and spine:7."
  author-agent-dialogue: "Raise it with a programme team or teacher who is designing, reviewing or defending the course's approach to academic integrity and GenAI policies. Frame it for staff as an expectation worded with \"should\", and ask: How are students told what use of GenAI is acceptable in each assessment? Do not quote the issuer at length, and do not put this duty to a student as something they have to achieve."
- statement: qaa/accounting-2025/2.1
  forPractitioner: { text: "Design for breadth and rigour: accounting in context, sound and creative judgement on complex problems, many kinds of organisation and stakeholder, sustainability, EDI and accessibility, and ethical citizenship.", rewrite: light, force: should, status: drafted }
  forBeneficiary: { text: "Your course should be designed to give you a broad, rigorous understanding of accounting in society, the ability to make sound judgements on complex problems and the grounding to act as a responsible, ethical citizen.", rewrite: full, force: should, status: drafted }
  author-agent-written: "Write about this as an expectation worded with \"should\" for any Accounting degree the statement covers, at the level of the award it is applied to, on design aims of an Accounting degree. Cite it as (QAA, 2025, Accounting Subject Benchmark Statement, para 2.1). Do not claim it is a regulatory requirement or that it sets the standard at another level. Set it beside qaa/accounting-2025/2.2 and the framework descriptor the honours and master's descriptors (qaa/fheq-2024/4.15.b1, qaa/fheq-2024/4.17.b1) at spine:6 and spine:7."
  author-agent-dialogue: "Bring it up when a student asks about design aims of an Accounting degree, or when staff check a module or outcome against it. Tell a student in plain words, as 'you', what it means for their course; for staff, frame it as an expectation worded with \"should\". Ask: Which complex problem have you had to judge without a clear right answer? Avoid long quotation of the issuer's text."
- statement: qaa/accounting-2025/2.2
  forPractitioner: { text: "Write programme objectives that map to the knowledge, understanding and skills in section 3, join conceptual and applied study and connect areas, and keep the design flexible enough to adapt to new technology.", rewrite: light, force: should, status: drafted }
  forBeneficiary: { text: "not-applicable: a duty on the course and the people who design and run it, not a standard the student reaches", rewrite: full, force: should, status: drafted }
  author-agent-written: "Write about this as an expectation worded with \"should\" on the course and its team, on learning objectives aligned to the statement, holding for any Accounting degree the statement covers. Cite it as (QAA, 2025, Accounting Subject Benchmark Statement, para 2.2). Do not present it as a regulatory requirement, and do not turn it into an outcome a student must show. Set it beside qaa/accounting-2025/2.1 and qaa/accounting-2025/2.3, and where it shapes outcomes beside the honours and master's descriptors (qaa/fheq-2024/4.15.b1, qaa/fheq-2024/4.17.b1) at spine:6 and spine:7."
  author-agent-dialogue: "Raise it with a programme team or teacher who is designing, reviewing or defending the course's approach to learning objectives aligned to the statement. Frame it for staff as an expectation worded with \"should\", and ask: Can you show each section 3 area against a programme objective and a module where it is assessed? Do not quote the issuer at length, and do not put this duty to a student as something they have to achieve."
- statement: qaa/accounting-2025/2.3
  forPractitioner: { text: "Give priority to higher-order thinking (analysis, evaluation, creativity) over routine tasks that automation will absorb, and build habits of self-directed, lifelong learning.", rewrite: light, force: should, status: drafted }
  forBeneficiary: { text: "Your course should develop your higher-level thinking, such as analysis, evaluation and creativity, for a workplace where routine tasks are increasingly automated, and prepare you to keep learning on your own.", rewrite: full, force: should, status: drafted }
  author-agent-written: "Write about this as an expectation worded with \"should\" for the bachelor's degree with honours, at FHEQ level 6 (FQHEIS level 10), on higher-order thinking and lifelong learning. Cite it as (QAA, 2025, Accounting Subject Benchmark Statement, para 2.3). Do not claim it is a regulatory requirement or that it sets the standard at another level. Set it beside qaa/accounting-2025/2.2 and qaa/accounting-2025/2.4 and the framework descriptor qaa/fheq-2024/4.15.b9.2 at spine:6."
  author-agent-dialogue: "Bring it up when a student asks about higher-order thinking and lifelong learning, or when staff check a module or outcome against it. Tell a student in plain words, as 'you', what it means for their course; for staff, frame it as an expectation worded with \"should\". Ask: Which part of your current work could be automated, and what thinking would still be yours? Avoid long quotation of the issuer's text."
- statement: qaa/accounting-2025/2.4
  forPractitioner: { text: "Keep career routes open: design for employment in many sectors, for entrepreneurship and for academic study, not only for professional accountancy.", rewrite: light, force: should, status: drafted }
  forBeneficiary: { text: "Your course should prepare you to do well in many kinds of career, in starting something of your own or in further academic study.", rewrite: full, force: should, status: drafted }
  author-agent-written: "Write about this as an expectation worded with \"should\" for any Accounting degree the statement covers, at the level of the award it is applied to, on preparing for many careers. Cite it as (QAA, 2025, Accounting Subject Benchmark Statement, para 2.4). Do not claim it is a regulatory requirement or that it sets the standard at another level. Set it beside qaa/accounting-2025/2.3 and qaa/accounting-2025/2.5 and the framework descriptor the honours and master's descriptors (qaa/fheq-2024/4.15.b1, qaa/fheq-2024/4.17.b1) at spine:6 and spine:7."
  author-agent-dialogue: "Bring it up when a student asks about preparing for many careers, or when staff check a module or outcome against it. Tell a student in plain words, as 'you', what it means for their course; for staff, frame it as an expectation worded with \"should\". Ask: Which route are you leaning towards, and what in the course is preparing you for it? Avoid long quotation of the issuer's text."
- statement: qaa/accounting-2025/2.5
  forPractitioner: { text: "Seek accreditation where it helps students, but do not let exemption requirements drive out the broader design aims; plan for students whose career aims change.", rewrite: light, force: should, status: drafted }
  forBeneficiary: { text: "not-applicable: a duty on the course and the people who design and run it, not a standard the student reaches", rewrite: full, force: should, status: drafted }
  author-agent-written: "Write about this as an expectation worded with \"should\" on the course and its team, on accreditation not at the expense of breadth, holding for any Accounting degree the statement covers. Cite it as (QAA, 2025, Accounting Subject Benchmark Statement, para 2.5). Do not present it as a regulatory requirement, and do not turn it into an outcome a student must show. Set it beside qaa/accounting-2025/2.4 and qaa/accounting-2025/2.6, and where it shapes outcomes beside the honours and master's descriptors (qaa/fheq-2024/4.15.b1, qaa/fheq-2024/4.17.b1) at spine:6 and spine:7."
  author-agent-dialogue: "Raise it with a programme team or teacher who is designing, reviewing or defending the course's approach to accreditation not at the expense of breadth. Frame it for staff as an expectation worded with \"should\", and ask: What would change in the design if accreditation were not a consideration? Do not quote the issuer at length, and do not put this duty to a student as something they have to achieve."
- statement: qaa/accounting-2025/2.6
  forPractitioner: { text: "In a joint degree, cover most of the statement's knowledge and skills and keep the balance from squeezing out conceptual, accountability, sustainability and higher-order content.", rewrite: light, force: should, status: drafted }
  forBeneficiary: { text: "not-applicable: a duty on the course and the people who design and run it, not a standard the student reaches", rewrite: full, force: should, status: drafted }
  author-agent-written: "Write about this as an expectation worded with \"should\" on the course and its team, on coverage in joint degrees, holding for the bachelor's degree with honours. Cite it as (QAA, 2025, Accounting Subject Benchmark Statement, para 2.6). Do not present it as a regulatory requirement, and do not turn it into an outcome a student must show. Set it beside qaa/accounting-2025/2.5 and qaa/accounting-2025/2.10, and where it shapes outcomes beside qaa/fheq-2024/4.15.b1 at spine:6."
  author-agent-dialogue: "Raise it with a programme team or teacher who is designing, reviewing or defending the course's approach to coverage in joint degrees. Frame it for staff as an expectation worded with \"should\", and ask: Which areas of section 3 does the joint design leave out, and is that a majority or a minority? Do not quote the issuer at length, and do not put this duty to a student as something they have to achieve."
- statement: qaa/accounting-2025/2.10
  forPractitioner: { text: "Set progression rules for a joint or combined honours route that satisfy both subjects' needs, not only the larger one.", rewrite: light, force: will, status: drafted }
  forBeneficiary: { text: "not-applicable: a duty on the course and the people who design and run it, not a standard the student reaches", rewrite: full, force: will, status: drafted }
  author-agent-written: "Write about this as an expected feature worded with \"will\" on the course and its team, on progression rules in joint honours, holding for the bachelor's degree with honours. Cite it as (QAA, 2025, Accounting Subject Benchmark Statement, para 2.10). Do not present it as a regulatory requirement, and do not turn it into an outcome a student must show. Set it beside qaa/accounting-2025/2.6 and qaa/accounting-2025/2.11, and where it shapes outcomes beside qaa/fheq-2024/4.15.b1 at spine:6."
  author-agent-dialogue: "Raise it with a programme team or teacher who is designing, reviewing or defending the course's approach to progression rules in joint honours. Frame it for staff as an expected feature worded with \"will\", and ask: Can a joint honours student progress without the Accounting prerequisites the next level depends on? Do not quote the issuer at length, and do not put this duty to a student as something they have to achieve."
- statement: qaa/accounting-2025/2.11
  forPractitioner: { text: "Build flexibility for individual needs into progression rules, including reasonable adjustments where possible.", rewrite: light, force: should, status: drafted }
  forBeneficiary: { text: "not-applicable: a duty on the course and the people who design and run it, not a standard the student reaches", rewrite: full, force: should, status: drafted }
  author-agent-written: "Write about this as an expectation worded with \"should\" on the course and its team, on progression that allows for individual needs, holding for any Accounting degree the statement covers. Cite it as (QAA, 2025, Accounting Subject Benchmark Statement, para 2.11). Do not present it as a regulatory requirement, and do not turn it into an outcome a student must show. Set it beside qaa/accounting-2025/2.10 and qaa/accounting-2025/2.12, and where it shapes outcomes beside the honours and master's descriptors (qaa/fheq-2024/4.15.b1, qaa/fheq-2024/4.17.b1) at spine:6 and spine:7."
  author-agent-dialogue: "Raise it with a programme team or teacher who is designing, reviewing or defending the course's approach to progression that allows for individual needs. Frame it for staff as an expectation worded with \"should\", and ask: Where do the progression regulations leave no room for an adjustment? Do not quote the issuer at length, and do not put this duty to a student as something they have to achieve."
- statement: qaa/accounting-2025/2.12
  forPractitioner: { text: "Make sure the honours degree gives a sound foundation for professional qualification and for other careers, notably in business and finance.", rewrite: light, force: should, status: drafted }
  forBeneficiary: { text: "Your honours degree should give you a sound start towards a professional qualification or another career, especially in business or finance.", rewrite: full, force: should, status: drafted }
  author-agent-written: "Write about this as an expectation worded with \"should\" for the bachelor's degree with honours, at FHEQ level 6 (FQHEIS level 10), on honours as a basis for qualification and careers. Cite it as (QAA, 2025, Accounting Subject Benchmark Statement, para 2.12). Do not claim it is a regulatory requirement or that it sets the standard at another level. Set it beside qaa/accounting-2025/2.11 and qaa/accounting-2025/2.13 and the framework descriptor qaa/fheq-2024/4.15.b1 at spine:6."
  author-agent-dialogue: "Bring it up when a student asks about honours as a basis for qualification and careers, or when staff check a module or outcome against it. Tell a student in plain words, as 'you', what it means for their course; for staff, frame it as an expectation worded with \"should\". Ask: Which professional qualification or career are you aiming at, and which parts of the degree count towards it? Avoid long quotation of the issuer's text."
- statement: qaa/accounting-2025/2.13
  forPractitioner: { text: "Graduates with a second-class degree or better should be ready for postgraduate study in the subject; admissions decisions remain each institution's, and the same principles apply to entering an integrated master's final year.", rewrite: light, force: should, status: drafted }
  forBeneficiary: { text: "If you gain a second-class degree or higher, you should be ready for postgraduate study in Accounting or a related subject, though each institution sets its own entry rules.", rewrite: full, force: should, status: drafted }
  author-agent-written: "Write about this as an expectation worded with \"should\" for the bachelor's degree with honours, at FHEQ level 6 (FQHEIS level 10), on readiness for postgraduate study. Cite it as (QAA, 2025, Accounting Subject Benchmark Statement, para 2.13). Do not claim it is a regulatory requirement or that it sets the standard at another level. Set it beside qaa/accounting-2025/2.12 and qaa/accounting-2025/2.14 and the framework descriptor qaa/fheq-2024/4.15.b1 at spine:6."
  author-agent-dialogue: "Bring it up when a student asks about readiness for postgraduate study, or when staff check a module or outcome against it. Tell a student in plain words, as 'you', what it means for their course; for staff, frame it as an expectation worded with \"should\". Ask: Is postgraduate study part of your plan, and what class of degree does your target course ask for? Avoid long quotation of the issuer's text."
- statement: qaa/accounting-2025/2.14
  forPractitioner: { text: "Apply the same progression standards to degree apprentices as to other students, and plan for the end-point assessment the apprenticeship may require.", rewrite: light, force: will, status: drafted }
  forBeneficiary: { text: "As a degree apprentice, the same progression standards will apply to you, and you may also need to pass an end-point assessment to complete the apprenticeship.", rewrite: full, force: will, status: drafted }
  author-agent-written: "Write about this as an expected feature worded with \"will\" for the Accounting degree apprenticeship, at FHEQ level 6 (FQHEIS level 10), on progression on degree apprenticeships. Cite it as (QAA, 2025, Accounting Subject Benchmark Statement, para 2.14). Do not claim it is a regulatory requirement or that it sets the standard at another level. Set it beside qaa/accounting-2025/2.13 and qaa/accounting-2025/2.16 and the framework descriptor qaa/fheq-2024/4.15.b1 at spine:6."
  author-agent-dialogue: "Bring it up when a student asks about progression on degree apprenticeships, or when staff check a module or outcome against it. Tell a student in plain words, as 'you', what it means for their course; for staff, frame it as an expected feature worded with \"will\". Ask: Do you know what your end-point assessment involves and when it falls? Avoid long quotation of the issuer's text."
- statement: qaa/accounting-2025/2.16
  forPractitioner: { text: "Review and adapt the course as the subject and employers' needs change, and keep it flexible enough to meet learners', the profession's and external bodies' needs.", rewrite: light, force: should, status: drafted }
  forBeneficiary: { text: "not-applicable: a duty on the course and the people who design and run it, not a standard the student reaches", rewrite: full, force: should, status: drafted }
  author-agent-written: "Write about this as an expectation worded with \"should\" on the course and its team, on adaptable and flexible courses, holding for any Accounting degree the statement covers. Cite it as (QAA, 2025, Accounting Subject Benchmark Statement, para 2.16). Do not present it as a regulatory requirement, and do not turn it into an outcome a student must show. Set it beside qaa/accounting-2025/2.14 and qaa/accounting-2025/2.17, and where it shapes outcomes beside the honours and master's descriptors (qaa/fheq-2024/4.15.b1, qaa/fheq-2024/4.17.b1) at spine:6 and spine:7."
  author-agent-dialogue: "Raise it with a programme team or teacher who is designing, reviewing or defending the course's approach to adaptable and flexible courses. Frame it for staff as an expectation worded with \"should\", and ask: What changed in the course after the last major development in the profession? Do not quote the issuer at length, and do not put this duty to a student as something they have to achieve."
- statement: qaa/accounting-2025/2.17
  forPractitioner: { text: "Design for inclusivity through options in length, mode, entry criteria and assessment, such as placement years, part-time and distance study.", rewrite: light, force: should, status: drafted }
  forBeneficiary: { text: "not-applicable: a duty on the course and the people who design and run it, not a standard the student reaches", rewrite: full, force: should, status: drafted }
  author-agent-written: "Write about this as an expectation worded with \"should\" on the course and its team, on inclusive flexibility of mode and length, holding for any Accounting degree the statement covers. Cite it as (QAA, 2025, Accounting Subject Benchmark Statement, para 2.17). Do not present it as a regulatory requirement, and do not turn it into an outcome a student must show. Set it beside qaa/accounting-2025/2.16 and qaa/accounting-2025/2.23, and where it shapes outcomes beside the honours and master's descriptors (qaa/fheq-2024/4.15.b1, qaa/fheq-2024/4.17.b1) at spine:6 and spine:7."
  author-agent-dialogue: "Raise it with a programme team or teacher who is designing, reviewing or defending the course's approach to inclusive flexibility of mode and length. Frame it for staff as an expectation worded with \"should\", and ask: Which mode or length option would most widen who can study the course? Do not quote the issuer at length, and do not put this duty to a student as something they have to achieve."
- statement: qaa/accounting-2025/2.23
  forPractitioner: { text: "Apply the statement across the whole of a partnership course so that the standards hold everywhere, and do not let a partner's accreditation aims narrow the design.", rewrite: light, force: should, status: drafted }
  forBeneficiary: { text: "not-applicable: a duty on the course and the people who design and run it, not a standard the student reaches", rewrite: full, force: should, status: drafted }
  author-agent-written: "Write about this as an expectation worded with \"should\" on the course and its team, on standards across partnership delivery, holding for any Accounting degree the statement covers. Cite it as (QAA, 2025, Accounting Subject Benchmark Statement, para 2.23). Do not present it as a regulatory requirement, and do not turn it into an outcome a student must show. Set it beside qaa/accounting-2025/2.17 and qaa/accounting-2025/2.26, and where it shapes outcomes beside the honours and master's descriptors (qaa/fheq-2024/4.15.b1, qaa/fheq-2024/4.17.b1) at spine:6 and spine:7."
  author-agent-dialogue: "Raise it with a programme team or teacher who is designing, reviewing or defending the course's approach to standards across partnership delivery. Frame it for staff as an expectation worded with \"should\", and ask: How do you check that the standards are met in the partner's delivery, not only in your own? Do not quote the issuer at length, and do not put this duty to a student as something they have to achieve."
- statement: qaa/accounting-2025/2.26
  forPractitioner: { text: "Work with professional bodies, but measure the course against this statement's standards first; accreditation requirements do not replace them.", rewrite: light, force: should, status: drafted }
  forBeneficiary: { text: "not-applicable: a duty on the course and the people who design and run it, not a standard the student reaches", rewrite: full, force: should, status: drafted }
  author-agent-written: "Write about this as an expectation worded with \"should\" on the course and its team, on PSRBs as partners, not prescribers, holding for any Accounting degree the statement covers. Cite it as (QAA, 2025, Accounting Subject Benchmark Statement, para 2.26). Do not present it as a regulatory requirement, and do not turn it into an outcome a student must show. Set it beside qaa/accounting-2025/2.23 and qaa/accounting-2025/2.28, and where it shapes outcomes beside the honours and master's descriptors (qaa/fheq-2024/4.15.b1, qaa/fheq-2024/4.17.b1) at spine:6 and spine:7."
  author-agent-dialogue: "Raise it with a programme team or teacher who is designing, reviewing or defending the course's approach to PSRBs as partners, not prescribers. Frame it for staff as an expectation worded with \"should\", and ask: Where does an accreditation requirement now set content that the statement would weigh differently? Do not quote the issuer at length, and do not put this duty to a student as something they have to achieve."
- statement: qaa/accounting-2025/2.28
  forPractitioner: { text: "Use external reference points, this statement included, in annual monitoring and periodic review, with external experts or advisers, to keep the course in line with the sector.", rewrite: light, force: should, status: drafted }
  forBeneficiary: { text: "not-applicable: a duty on the course and the people who design and run it, not a standard the student reaches", rewrite: full, force: should, status: drafted }
  author-agent-written: "Write about this as an expectation worded with \"should\" on the course and its team, on external reference points in review, holding for any Accounting degree the statement covers. Cite it as (QAA, 2025, Accounting Subject Benchmark Statement, para 2.28). Do not present it as a regulatory requirement, and do not turn it into an outcome a student must show. Set it beside qaa/accounting-2025/2.26 and qaa/accounting-2025/2.31, and where it shapes outcomes beside the honours and master's descriptors (qaa/fheq-2024/4.15.b1, qaa/fheq-2024/4.17.b1) at spine:6 and spine:7."
  author-agent-dialogue: "Raise it with a programme team or teacher who is designing, reviewing or defending the course's approach to external reference points in review. Frame it for staff as an expectation worded with \"should\", and ask: Which external reference points did the last periodic review use? Do not quote the issuer at length, and do not put this duty to a student as something they have to achieve."
- statement: qaa/accounting-2025/2.31
  forPractitioner: { text: "Use monitoring and review to check that the five themes are present across the curriculum and in teaching and assessment, not in one module only.", rewrite: light, force: should, status: drafted }
  forBeneficiary: { text: "not-applicable: a duty on the course and the people who design and run it, not a standard the student reaches", rewrite: full, force: should, status: drafted }
  author-agent-written: "Write about this as an expectation worded with \"should\" on the course and its team, on monitoring the cross-cutting themes, holding for any Accounting degree the statement covers. Cite it as (QAA, 2025, Accounting Subject Benchmark Statement, para 2.31). Do not present it as a regulatory requirement, and do not turn it into an outcome a student must show. Set it beside qaa/accounting-2025/2.28 and qaa/accounting-2025/2.32, and where it shapes outcomes beside the honours and master's descriptors (qaa/fheq-2024/4.15.b1, qaa/fheq-2024/4.17.b1) at spine:6 and spine:7."
  author-agent-dialogue: "Raise it with a programme team or teacher who is designing, reviewing or defending the course's approach to monitoring the cross-cutting themes. Frame it for staff as an expectation worded with \"should\", and ask: Where does each of the five themes appear in assessment, not only in content? Do not quote the issuer at length, and do not put this duty to a student as something they have to achieve."
- statement: qaa/accounting-2025/2.32
  forPractitioner: { text: "Ask external examiners to judge the course and its outcomes against this statement's standards, and use their reports in review.", rewrite: light, force: should, status: drafted }
  forBeneficiary: { text: "not-applicable: a duty on the course and the people who design and run it, not a standard the student reaches", rewrite: full, force: should, status: drafted }
  author-agent-written: "Write about this as an expectation worded with \"should\" on the course and its team, on the statement in external examining, holding for any Accounting degree the statement covers. Cite it as (QAA, 2025, Accounting Subject Benchmark Statement, para 2.32). Do not present it as a regulatory requirement, and do not turn it into an outcome a student must show. Set it beside qaa/accounting-2025/2.31 and qaa/accounting-2025/2.33, and where it shapes outcomes beside the honours and master's descriptors (qaa/fheq-2024/4.15.b1, qaa/fheq-2024/4.17.b1) at spine:6 and spine:7."
  author-agent-dialogue: "Raise it with a programme team or teacher who is designing, reviewing or defending the course's approach to the statement in external examining. Frame it for staff as an expectation worded with \"should\", and ask: Did the last examiner's report refer to the subject standards, and what changed as a result? Do not quote the issuer at length, and do not put this duty to a student as something they have to achieve."
- statement: qaa/accounting-2025/2.33
  forPractitioner: { text: "Give prospective and current students clear information about how the course leads to professional qualification and which exemptions it carries.", rewrite: light, force: should, status: drafted }
  forBeneficiary: { text: "not-applicable: a duty on the course and the people who design and run it, not a standard the student reaches", rewrite: full, force: should, status: drafted }
  author-agent-written: "Write about this as an expectation worded with \"should\" on the course and its team, on informing students about professional routes, holding for any Accounting degree the statement covers. Cite it as (QAA, 2025, Accounting Subject Benchmark Statement, para 2.33). Do not present it as a regulatory requirement, and do not turn it into an outcome a student must show. Set it beside qaa/accounting-2025/2.32, and where it shapes outcomes beside the honours and master's descriptors (qaa/fheq-2024/4.15.b1, qaa/fheq-2024/4.17.b1) at spine:6 and spine:7."
  author-agent-dialogue: "Raise it with a programme team or teacher who is designing, reviewing or defending the course's approach to informing students about professional routes. Frame it for staff as an expectation worded with \"should\", and ask: Where can a prospective student find the exemptions the course gives? Do not quote the issuer at length, and do not put this duty to a student as something they have to achieve."
- statement: qaa/accounting-2025/3.2
  forPractitioner: { text: "Derive the content from section 1's purposes and characteristics and carry the cross-cutting themes into it.", rewrite: light, force: should, status: drafted }
  forBeneficiary: { text: "not-applicable: a duty on the course and the people who design and run it, not a standard the student reaches", rewrite: full, force: should, status: drafted }
  author-agent-written: "Write about this as an expectation worded with \"should\" on the course and its team, on content shaped by section 1 and the themes, holding for any Accounting degree the statement covers. Cite it as (QAA, 2025, Accounting Subject Benchmark Statement, para 3.2). Do not present it as a regulatory requirement, and do not turn it into an outcome a student must show. Set it beside qaa/accounting-2025/3.3, and where it shapes outcomes beside the honours and master's descriptors (qaa/fheq-2024/4.15.b1, qaa/fheq-2024/4.17.b1) at spine:6 and spine:7."
  author-agent-dialogue: "Raise it with a programme team or teacher who is designing, reviewing or defending the course's approach to content shaped by section 1 and the themes. Frame it for staff as an expectation worded with \"should\", and ask: Which purposes in section 1 have no clear home in the current content? Do not quote the issuer at length, and do not put this duty to a student as something they have to achieve."
- statement: qaa/accounting-2025/3.3
  forPractitioner: { text: "Give substantial time to the public interest and accountability, to critique of current accounting and to imagining alternatives, and build an ethical sense of responsibility and anticipation of change.", rewrite: light, force: should, status: drafted }
  forBeneficiary: { text: "Your course should give real weight to accounting's role in the public interest, encourage you to question how it is done now and help you imagine other ways, with a sense of ethical responsibility.", rewrite: full, force: should, status: drafted }
  author-agent-written: "Write about this as an expectation worded with \"should\" for any Accounting degree the statement covers, at the level of the award it is applied to, on the public interest role of accounting. Cite it as (QAA, 2025, Accounting Subject Benchmark Statement, para 3.3). Do not claim it is a regulatory requirement or that it sets the standard at another level. Set it beside qaa/accounting-2025/3.2 and qaa/accounting-2025/3.4 and the framework descriptor the honours and master's descriptors (qaa/fheq-2024/4.15.b1, qaa/fheq-2024/4.17.b1) at spine:6 and spine:7."
  author-agent-dialogue: "Bring it up when a student asks about the public interest role of accounting, or when staff check a module or outcome against it. Tell a student in plain words, as 'you', what it means for their course; for staff, frame it as an expectation worded with \"should\". Ask: Whose interest does a particular accounting rule serve, and whose does it overlook? Avoid long quotation of the issuer's text."
- statement: qaa/accounting-2025/3.4
  forPractitioner: { text: "Teach accounting critically and in context, drawing on the social sciences and treating accountability for sustainability, welfare and social concerns as core.", rewrite: light, force: should, status: drafted }
  forBeneficiary: { text: "Your course should get you discussing accounting critically in its social and economic setting and looking beyond profit to sustainability, welfare and social concerns.", rewrite: full, force: should, status: drafted }
  author-agent-written: "Write about this as an expectation worded with \"should\" for any Accounting degree the statement covers, at the level of the award it is applied to, on critical, socially grounded study. Cite it as (QAA, 2025, Accounting Subject Benchmark Statement, para 3.4). Do not claim it is a regulatory requirement or that it sets the standard at another level. Set it beside qaa/accounting-2025/3.3 and qaa/accounting-2025/3.5 and the framework descriptor the honours and master's descriptors (qaa/fheq-2024/4.15.b1, qaa/fheq-2024/4.17.b1) at spine:6 and spine:7."
  author-agent-dialogue: "Bring it up when a student asks about critical, socially grounded study, or when staff check a module or outcome against it. Tell a student in plain words, as 'you', what it means for their course; for staff, frame it as an expectation worded with \"should\". Ask: What would an account of the same organisation look like from a community's point of view rather than an investor's? Avoid long quotation of the issuer's text."
- statement: qaa/accounting-2025/3.5
  forPractitioner: { text: "Give students practice in applying accounting knowledge, skills and critique to public, charitable, co-operative, social enterprise and campaigning bodies as well as companies.", rewrite: light, force: should, status: drafted }
  forBeneficiary: { text: "Your course should give you practice in using and questioning accounting in many kinds of organisation, from charities and public bodies to co-operatives and companies.", rewrite: full, force: should, status: drafted }
  author-agent-written: "Write about this as an expectation worded with \"should\" for any Accounting degree the statement covers, at the level of the award it is applied to, on accounting across many kinds of organisation. Cite it as (QAA, 2025, Accounting Subject Benchmark Statement, para 3.5). Do not claim it is a regulatory requirement or that it sets the standard at another level. Set it beside qaa/accounting-2025/3.4 and qaa/accounting-2025/3.6 and the framework descriptor the honours and master's descriptors (qaa/fheq-2024/4.15.b1, qaa/fheq-2024/4.17.b1) at spine:6 and spine:7."
  author-agent-dialogue: "Bring it up when a student asks about accounting across many kinds of organisation, or when staff check a module or outcome against it. Tell a student in plain words, as 'you', what it means for their course; for staff, frame it as an expectation worded with \"should\". Ask: How would the accounts of a charity tell a different story from those of a company of the same size? Avoid long quotation of the issuer's text."
- statement: qaa/accounting-2025/3.6
  forPractitioner: { text: "Include both conceptual and theoretical study and applied study in every course.", rewrite: light, force: should, status: drafted }
  forBeneficiary: { text: "not-applicable: a duty on the course and the people who design and run it, not a standard the student reaches", rewrite: full, force: should, status: drafted }
  author-agent-written: "Write about this as an expectation worded with \"should\" on the course and its team, on conceptual and applied aspects, holding for any Accounting degree the statement covers. Cite it as (QAA, 2025, Accounting Subject Benchmark Statement, para 3.6). Do not present it as a regulatory requirement, and do not turn it into an outcome a student must show. Set it beside qaa/accounting-2025/3.5 and qaa/accounting-2025/3.8, and where it shapes outcomes beside the honours and master's descriptors (qaa/fheq-2024/4.15.b1, qaa/fheq-2024/4.17.b1) at spine:6 and spine:7."
  author-agent-dialogue: "Raise it with a programme team or teacher who is designing, reviewing or defending the course's approach to conceptual and applied aspects. Frame it for staff as an expectation worded with \"should\", and ask: What share of assessment credit goes to conceptual and theoretical work? Do not quote the issuer at length, and do not put this duty to a student as something they have to achieve."
- statement: qaa/accounting-2025/3.8
  forPractitioner: { text: "Go beyond financial numbers: teach accounting's history, its non-financial reporting and its role in sustainability, stakeholder expectations and social issues, and give students practice in guiding organisations through ambiguous problems.", rewrite: light, force: should, status: drafted }
  forBeneficiary: { text: "Your course should show you that accounting is about more than numbers and money, and prepare you to use what you learn to guide organisations through complex social, sustainability and ethical questions.", rewrite: full, force: should, status: drafted }
  author-agent-written: "Write about this as an expectation worded with \"should\" for any Accounting degree the statement covers, at the level of the award it is applied to, on accounting beyond numbers in a complex world. Cite it as (QAA, 2025, Accounting Subject Benchmark Statement, para 3.8). Do not claim it is a regulatory requirement or that it sets the standard at another level. Set it beside qaa/accounting-2025/3.6 and qaa/accounting-2025/3.9 and the framework descriptor the honours and master's descriptors (qaa/fheq-2024/4.15.b1, qaa/fheq-2024/4.17.b1) at spine:6 and spine:7."
  author-agent-dialogue: "Bring it up when a student asks about accounting beyond numbers in a complex world, or when staff check a module or outcome against it. Tell a student in plain words, as 'you', what it means for their course; for staff, frame it as an expectation worded with \"should\". Ask: What non-financial information would you need to judge how well an organisation is doing? Avoid long quotation of the issuer's text."
- statement: qaa/accounting-2025/3.9
  forPractitioner: { text: "Make sure students practise recording and summarising transactions, preparing financial statements, analysing operations (decision analysis, performance measurement, budgeting, discounted cash flow) and analysing ratios, risks and projections.", rewrite: light, force: should, status: drafted }
  forBeneficiary: { text: "Your course should build your practical accounting skills: recording transactions, preparing financial statements, analysing how a business performs and projecting its finances.", rewrite: full, force: should, status: drafted }
  author-agent-written: "Write about this as an expectation worded with \"should\" for any Accounting degree the statement covers, at the level of the award it is applied to, on core accounting-specific skills. Cite it as (QAA, 2025, Accounting Subject Benchmark Statement, para 3.9). Do not claim it is a regulatory requirement or that it sets the standard at another level. Set it beside qaa/accounting-2025/3.8 and qaa/accounting-2025/3.10 and the framework descriptor the honours and master's descriptors (qaa/fheq-2024/4.15.b1, qaa/fheq-2024/4.17.b1) at spine:6 and spine:7."
  author-agent-dialogue: "Bring it up when a student asks about core accounting-specific skills, or when staff check a module or outcome against it. Tell a student in plain words, as 'you', what it means for their course; for staff, frame it as an expectation worded with \"should\". Ask: Could you prepare a set of statements from a trial balance and explain what the ratios show? Avoid long quotation of the issuer's text."
- statement: qaa/accounting-2025/3.10
  forPractitioner: { text: "Cover every listed area, each with theory, practice, regulation, debate and application in local, national and global contexts; teach them as linked parts of accounting, build them up across the years, and show how the themes cut across them.", rewrite: light, force: should, status: drafted }
  forBeneficiary: { text: "not-applicable: a duty on the course and the people who design and run it, not a standard the student reaches", rewrite: full, force: should, status: drafted }
  author-agent-written: "Write about this as an expectation worded with \"should\" on the course and its team, on the broad areas of knowledge, integrated, holding for any Accounting degree the statement covers. Cite it as (QAA, 2025, Accounting Subject Benchmark Statement, para 3.10). Do not present it as a regulatory requirement, and do not turn it into an outcome a student must show. Set it beside qaa/accounting-2025/3.9 and qaa/accounting-2025/3.10.b1, and where it shapes outcomes beside the honours and master's descriptors (qaa/fheq-2024/4.15.b1, qaa/fheq-2024/4.17.b1) at spine:6 and spine:7."
  author-agent-dialogue: "Raise it with a programme team or teacher who is designing, reviewing or defending the course's approach to the broad areas of knowledge, integrated. Frame it for staff as an expectation worded with \"should\", and ask: Which two areas are most often taught in isolation from each other, and how could they be linked? Do not quote the issuer at length, and do not put this duty to a student as something they have to achieve."
- statement: qaa/accounting-2025/3.10.b1
  forPractitioner: { text: "Teach the position of trust accountants hold and give students practice in judgement, assurance, advice and leadership that honours it.", rewrite: light, force: should, status: drafted }
  forBeneficiary: { text: "Your course should help you see the trust placed in accountants and build your ability to judge well and to give assurance, advice and leadership.", rewrite: full, force: should, status: drafted }
  author-agent-written: "Write about this as an expectation worded with \"should\" for any Accounting degree the statement covers, at the level of the award it is applied to, on area a: accountability, responsibility and trust. Cite it as (QAA, 2025, Accounting Subject Benchmark Statement, para 3.10, area a). Do not claim it is a regulatory requirement or that it sets the standard at another level. Set it beside qaa/accounting-2025/3.10 and qaa/accounting-2025/3.10.b2 and the framework descriptor the honours and master's descriptors (qaa/fheq-2024/4.15.b1, qaa/fheq-2024/4.17.b1) at spine:6 and spine:7."
  author-agent-dialogue: "Bring it up when a student asks about area a: accountability, responsibility and trust, or when staff check a module or outcome against it. Tell a student in plain words, as 'you', what it means for their course; for staff, frame it as an expectation worded with \"should\". Ask: What would losing that trust cost a client, and what would it cost the profession? Avoid long quotation of the issuer's text."
- statement: qaa/accounting-2025/3.10.b2
  forPractitioner: { text: "Cover the environment organisations work in and their effect on it, at local, national and international scale, across environmental, cultural, ethical, legal, tax, political, social and digital factors.", rewrite: light, force: should, status: drafted }
  forBeneficiary: { text: "You should be able to show that you understand how the business, economic and social environment shapes organisations, and how organisations shape it in turn.", rewrite: full, force: should, status: drafted }
  author-agent-written: "Write about this as an expectation worded with \"should\" for any Accounting degree the statement covers, at the level of the award it is applied to, on area b: the business, social and economic environment. Cite it as (QAA, 2025, Accounting Subject Benchmark Statement, para 3.10, area b). Do not claim it is a regulatory requirement or that it sets the standard at another level. Set it beside qaa/accounting-2025/3.10.b1 and qaa/accounting-2025/3.10.b3 and the framework descriptor the honours and master's descriptors (qaa/fheq-2024/4.15.b1, qaa/fheq-2024/4.17.b1) at spine:6 and spine:7."
  author-agent-dialogue: "Bring it up when a student asks about area b: the business, social and economic environment, or when staff check a module or outcome against it. Tell a student in plain words, as 'you', what it means for their course; for staff, frame it as an expectation worded with \"should\". Ask: How has a recent legal, technological or environmental change altered the way a firm you know operates? Avoid long quotation of the issuer's text."
- statement: qaa/accounting-2025/3.10.b3
  forPractitioner: { text: "Weave ethics through the whole degree, general and accounting-specific, so students practise scepticism, work through hard moral cases and decide in the public interest.", rewrite: light, force: should, status: drafted }
  forBeneficiary: { text: "Ethics should run through your whole course, helping you spot dilemmas, apply professional scepticism and make decisions that serve the public interest.", rewrite: full, force: should, status: drafted }
  author-agent-written: "Write about this as an expectation worded with \"should\" for any Accounting degree the statement covers, at the level of the award it is applied to, on area c: ethics. Cite it as (QAA, 2025, Accounting Subject Benchmark Statement, para 3.10, area c). Do not claim it is a regulatory requirement or that it sets the standard at another level. Set it beside qaa/accounting-2025/3.10.b2 and qaa/accounting-2025/3.10.b4 and the framework descriptor the honours and master's descriptors (qaa/fheq-2024/4.15.b1, qaa/fheq-2024/4.17.b1) at spine:6 and spine:7."
  author-agent-dialogue: "Bring it up when a student asks about area c: ethics, or when staff check a module or outcome against it. Tell a student in plain words, as 'you', what it means for their course; for staff, frame it as an expectation worded with \"should\". Ask: Describe a case where the rules allowed something you still judged to be wrong. Avoid long quotation of the issuer's text."
- statement: qaa/accounting-2025/3.10.b4
  forPractitioner: { text: "Teach the full range of reports, financial and non-financial, the laws and standards that govern them, recording skills, accounting's governance role and current research, so that graduates can evaluate practice critically.", rewrite: light, force: should, status: drafted }
  forBeneficiary: { text: "You should be able to apply the laws, regulations and standards for reporting, understand accounting's part in how organisations are governed and use current research to judge reporting practice.", rewrite: full, force: should, status: drafted }
  author-agent-written: "Write about this as an expectation worded with \"should\" for any Accounting degree the statement covers, at the level of the award it is applied to, on area d: organisational governance and corporate reporting. Cite it as (QAA, 2025, Accounting Subject Benchmark Statement, para 3.10, area d). Do not claim it is a regulatory requirement or that it sets the standard at another level. Set it beside qaa/accounting-2025/3.10.b3 and qaa/accounting-2025/3.10.b5 and the framework descriptor the honours and master's descriptors (qaa/fheq-2024/4.15.b1, qaa/fheq-2024/4.17.b1) at spine:6 and spine:7."
  author-agent-dialogue: "Bring it up when a student asks about area d: organisational governance and corporate reporting, or when staff check a module or outcome against it. Tell a student in plain words, as 'you', what it means for their course; for staff, frame it as an expectation worded with \"should\". Ask: Which report beyond the financial statements would you read first to judge a company's governance, and why? Avoid long quotation of the issuer's text."
- statement: qaa/accounting-2025/3.10.b5
  forPractitioner: { text: "Give students practice in performance measurement systems and KPIs, budgeting, costing and valuation, communicating to decision-makers and solving problems with incomplete data, using analytics and current technology.", rewrite: light, force: should, status: drafted }
  forBeneficiary: { text: "Your course should prepare you to design and run performance measures, build and monitor budgets, apply costing and valuation, and make sound recommendations even when the data is incomplete.", rewrite: full, force: should, status: drafted }
  author-agent-written: "Write about this as an expectation worded with \"should\" for any Accounting degree the statement covers, at the level of the award it is applied to, on area e: information for decision-making. Cite it as (QAA, 2025, Accounting Subject Benchmark Statement, para 3.10, area e). Do not claim it is a regulatory requirement or that it sets the standard at another level. Set it beside qaa/accounting-2025/3.10.b4 and qaa/accounting-2025/3.10.b6 and the framework descriptor the honours and master's descriptors (qaa/fheq-2024/4.15.b1, qaa/fheq-2024/4.17.b1) at spine:6 and spine:7."
  author-agent-dialogue: "Bring it up when a student asks about area e: information for decision-making, or when staff check a module or outcome against it. Tell a student in plain words, as 'you', what it means for their course; for staff, frame it as an expectation worded with \"should\". Ask: If a key figure in your budget were missing, how would you still reach a recommendation? Avoid long quotation of the issuer's text."
- statement: qaa/accounting-2025/3.10.b6
  forPractitioner: { text: "Cover double entry, ledgers and statement production alongside wider data systems, databases and ERP, and give students practice with structured and unstructured data.", rewrite: light, force: should, status: drafted }
  forBeneficiary: { text: "Your course should help you understand how accounting and wider data systems work, from ledgers to databases, and build your skill in working with both tidy and messy data.", rewrite: full, force: should, status: drafted }
  author-agent-written: "Write about this as an expectation worded with \"should\" for any Accounting degree the statement covers, at the level of the award it is applied to, on area f: systems, processes and data structures. Cite it as (QAA, 2025, Accounting Subject Benchmark Statement, para 3.10, area f). Do not claim it is a regulatory requirement or that it sets the standard at another level. Set it beside qaa/accounting-2025/3.10.b5 and qaa/accounting-2025/3.10.b7 and the framework descriptor the honours and master's descriptors (qaa/fheq-2024/4.15.b1, qaa/fheq-2024/4.17.b1) at spine:6 and spine:7."
  author-agent-dialogue: "Bring it up when a student asks about area f: systems, processes and data structures, or when staff check a module or outcome against it. Tell a student in plain words, as 'you', what it means for their course; for staff, frame it as an expectation worded with \"should\". Ask: What controls would you look for in a system before relying on its data? Avoid long quotation of the issuer's text."
- statement: qaa/accounting-2025/3.10.b7
  forPractitioner: { text: "Teach the regulation of accounting, the profession and organisations in all sectors, including governance codes, sustainability reporting rules and tax law, and how ethics and equality enter regulation.", rewrite: light, force: must, status: drafted }
  forBeneficiary: { text: "Your course should help you understand the rules that govern accounting and organisations, from governance codes to sustainability reporting and tax law, and why they matter.", rewrite: full, force: must, status: drafted }
  author-agent-written: "Write about this as an expected outcome stated without one of the five obliging words (force recorded as describes) for any Accounting degree the statement covers, at the level of the award it is applied to, on area g: the regulatory environment. Cite it as (QAA, 2025, Accounting Subject Benchmark Statement, para 3.10, area g). Do not claim it is a regulatory requirement or that it sets the standard at another level. Set it beside qaa/accounting-2025/3.10.b6 and qaa/accounting-2025/3.10.b8 and the framework descriptor the honours and master's descriptors (qaa/fheq-2024/4.15.b1, qaa/fheq-2024/4.17.b1) at spine:6 and spine:7."
  author-agent-dialogue: "Bring it up when a student asks about area g: the regulatory environment, or when staff check a module or outcome against it. Tell a student in plain words, as 'you', what it means for their course; for staff, frame it as an expected outcome stated without one of the five obliging words (force recorded as describes). Ask: Which regulation affecting accounting has changed most recently, and why was it changed? Avoid long quotation of the issuer's text."
- statement: qaa/accounting-2025/3.10.b8
  forPractitioner: { text: "Teach audit and assurance with professional scepticism, critical thinking and public interest responsibility at the centre, for financial and non-financial reporting, and stress professional ethics throughout.", rewrite: light, force: should, status: drafted }
  forBeneficiary: { text: "Your course should prepare you to carry out good audit and assurance work, with professional scepticism, sound judgement and a clear sense of the public interest.", rewrite: full, force: should, status: drafted }
  author-agent-written: "Write about this as an expectation worded with \"should\" for any Accounting degree the statement covers, at the level of the award it is applied to, on area h: audit and assurance. Cite it as (QAA, 2025, Accounting Subject Benchmark Statement, para 3.10, area h). Do not claim it is a regulatory requirement or that it sets the standard at another level. Set it beside qaa/accounting-2025/3.10.b7 and qaa/accounting-2025/3.10.b9 and the framework descriptor the honours and master's descriptors (qaa/fheq-2024/4.15.b1, qaa/fheq-2024/4.17.b1) at spine:6 and spine:7."
  author-agent-dialogue: "Bring it up when a student asks about area h: audit and assurance, or when staff check a module or outcome against it. Tell a student in plain words, as 'you', what it means for their course; for staff, frame it as an expectation worded with \"should\". Ask: What would make you sceptical of a figure a client's finance director assures you is correct? Avoid long quotation of the issuer's text."
- statement: qaa/accounting-2025/3.10.b9
  forPractitioner: { text: "Cover tax principles, purposes and ethics, the consequences of non-compliance and illicit practice, and at minimum the main UK taxes (income tax, National Insurance, capital gains, inheritance, corporation tax and VAT).", rewrite: light, force: should, status: drafted }
  forBeneficiary: { text: "Your course should help you understand how tax works and why, the ethics and law around it and, at the least, the main UK taxes such as income tax, National Insurance, corporation tax and VAT.", rewrite: full, force: should, status: drafted }
  author-agent-written: "Write about this as an expectation worded with \"should\" for any Accounting degree the statement covers, at the level of the award it is applied to, on area i: taxation. Cite it as (QAA, 2025, Accounting Subject Benchmark Statement, para 3.10, area i). Do not claim it is a regulatory requirement or that it sets the standard at another level. Set it beside qaa/accounting-2025/3.10.b8 and qaa/accounting-2025/3.10.b10 and the framework descriptor the honours and master's descriptors (qaa/fheq-2024/4.15.b1, qaa/fheq-2024/4.17.b1) at spine:6 and spine:7."
  author-agent-dialogue: "Bring it up when a student asks about area i: taxation, or when staff check a module or outcome against it. Tell a student in plain words, as 'you', what it means for their course; for staff, frame it as an expectation worded with \"should\". Ask: Where would you draw the line between legitimate tax planning and aggressive avoidance? Avoid long quotation of the issuer's text."
- statement: qaa/accounting-2025/3.10.b10
  forPractitioner: { text: "Teach the difference between risk and uncertainty and give students practice with risk appetite, scenario planning, decision trees, forecasting and the data those models need.", rewrite: light, force: should, status: drafted }
  forBeneficiary: { text: "Your course should help you tell risk from uncertainty, use tools such as scenario planning, decision trees and forecasting, and advise on the right data for them.", rewrite: full, force: should, status: drafted }
  author-agent-written: "Write about this as an expectation worded with \"should\" for any Accounting degree the statement covers, at the level of the award it is applied to, on area j: uncertainty and risk management. Cite it as (QAA, 2025, Accounting Subject Benchmark Statement, para 3.10, area j). Do not claim it is a regulatory requirement or that it sets the standard at another level. Set it beside qaa/accounting-2025/3.10.b9 and qaa/accounting-2025/3.10.b11 and the framework descriptor the honours and master's descriptors (qaa/fheq-2024/4.15.b1, qaa/fheq-2024/4.17.b1) at spine:6 and spine:7."
  author-agent-dialogue: "Bring it up when a student asks about area j: uncertainty and risk management, or when staff check a module or outcome against it. Tell a student in plain words, as 'you', what it means for their course; for staff, frame it as an expectation worded with \"should\". Ask: Give an example of uncertainty that no probability could capture, and how you would plan for it. Avoid long quotation of the issuer's text."
- statement: qaa/accounting-2025/3.10.b11
  forPractitioner: { text: "Give students applied practice in analytics and statistics (hypothesis testing, anomaly detection and trend analysis, with some coding and machine learning), with critical reading of results and of research papers.", rewrite: light, force: should, status: drafted }
  forBeneficiary: { text: "Your course should give you practical skills in data analytics and statistics, and help you read the results, and the research that uses them, critically.", rewrite: full, force: should, status: drafted }
  author-agent-written: "Write about this as an expectation worded with \"should\" for any Accounting degree the statement covers, at the level of the award it is applied to, on area k: data analytics and statistics. Cite it as (QAA, 2025, Accounting Subject Benchmark Statement, para 3.10, area k). Do not claim it is a regulatory requirement or that it sets the standard at another level. Set it beside qaa/accounting-2025/3.10.b10 and qaa/accounting-2025/3.10.b12 and the framework descriptor the honours and master's descriptors (qaa/fheq-2024/4.15.b1, qaa/fheq-2024/4.17.b1) at spine:6 and spine:7."
  author-agent-dialogue: "Bring it up when a student asks about area k: data analytics and statistics, or when staff check a module or outcome against it. Tell a student in plain words, as 'you', what it means for their course; for staff, frame it as an expectation worded with \"should\". Ask: What would make you doubt an anomaly that an analytics tool has flagged? Avoid long quotation of the issuer's text."
- statement: qaa/accounting-2025/3.10.b12
  forPractitioner: { text: "At minimum cover time value of money, sources of corporate finance, capital markets, project and corporate finance, asset pricing, behavioural and personal finance and ethics in finance; add further finance topics to suit the course.", rewrite: light, force: will, status: drafted }
  forBeneficiary: { text: "Your course will cover the essentials of financial markets and institutions, such as the time value of money, sources of finance, capital markets, asset pricing and ethics in finance.", rewrite: full, force: will, status: drafted }
  author-agent-written: "Write about this as an expected feature worded with \"will\" for any Accounting degree the statement covers, at the level of the award it is applied to, on area l: financial markets and institutions. Cite it as (QAA, 2025, Accounting Subject Benchmark Statement, para 3.10, area l). Do not claim it is a regulatory requirement or that it sets the standard at another level. Set it beside qaa/accounting-2025/3.10.b11 and qaa/accounting-2025/3.12 and the framework descriptor the honours and master's descriptors (qaa/fheq-2024/4.15.b1, qaa/fheq-2024/4.17.b1) at spine:6 and spine:7."
  author-agent-dialogue: "Bring it up when a student asks about area l: financial markets and institutions, or when staff check a module or outcome against it. Tell a student in plain words, as 'you', what it means for their course; for staff, frame it as an expected feature worded with \"will\". Ask: How would a change in interest rates move the value of a project you have appraised? Avoid long quotation of the issuer's text."
- statement: qaa/accounting-2025/3.12
  forPractitioner: { text: "Derive the skills the course develops from section 1's principles.", rewrite: light, force: should, status: drafted }
  forBeneficiary: { text: "not-applicable: a duty on the course and the people who design and run it, not a standard the student reaches", rewrite: full, force: should, status: drafted }
  author-agent-written: "Write about this as an expectation worded with \"should\" on the course and its team, on skills shaped by section 1, holding for any Accounting degree the statement covers. Cite it as (QAA, 2025, Accounting Subject Benchmark Statement, para 3.12). Do not present it as a regulatory requirement, and do not turn it into an outcome a student must show. Set it beside qaa/accounting-2025/3.10.b12 and qaa/accounting-2025/3.13, and where it shapes outcomes beside the honours and master's descriptors (qaa/fheq-2024/4.15.b1, qaa/fheq-2024/4.17.b1) at spine:6 and spine:7."
  author-agent-dialogue: "Raise it with a programme team or teacher who is designing, reviewing or defending the course's approach to skills shaped by section 1. Frame it for staff as an expectation worded with \"should\", and ask: Which section 1 principle is least visible in the skills the course assesses? Do not quote the issuer at length, and do not put this duty to a student as something they have to achieve."
- statement: qaa/accounting-2025/3.13
  forPractitioner: { text: "Students should build skills that turn their knowledge into practice, technical skills included, while staying aware of context and the themes and acting ethically.", rewrite: light, force: should, status: drafted }
  forBeneficiary: { text: "You should develop the skills to show and use what you know in practice, including technical accounting skills, while keeping the wider context in view and acting ethically.", rewrite: full, force: should, status: drafted }
  author-agent-written: "Write about this as an expectation worded with \"should\" for the bachelor's degree with honours, at FHEQ level 6 (FQHEIS level 10), on skills that put knowledge into action. Cite it as (QAA, 2025, Accounting Subject Benchmark Statement, para 3.13). Do not claim it is a regulatory requirement or that it sets the standard at another level. Set it beside qaa/accounting-2025/3.12 and qaa/accounting-2025/3.15.b1 and the framework descriptor qaa/fheq-2024/4.15.b9.2 at spine:6."
  author-agent-dialogue: "Bring it up when a student asks about skills that put knowledge into action, or when staff check a module or outcome against it. Tell a student in plain words, as 'you', what it means for their course; for staff, frame it as an expectation worded with \"should\". Ask: Where have you had to use what you know in a real or realistic setting, and what did that demand? Avoid long quotation of the issuer's text."
- statement: qaa/accounting-2025/3.15.b1
  forPractitioner: { text: "Graduates are expected to communicate data, analysis and argument effectively to different audiences, in speech, writing, visuals and varied media.", rewrite: light, force: must, status: drafted }
  forBeneficiary: { text: "You are expected to present numbers, analysis and arguments clearly to different audiences, in speech, writing, visuals and other media.", rewrite: full, force: must, status: drafted }
  author-agent-written: "Write about this as an expected outcome stated without one of the five obliging words (force recorded as describes) for the bachelor's degree with honours, at FHEQ level 6 (FQHEIS level 10), on skill m: communication. Cite it as (QAA, 2025, Accounting Subject Benchmark Statement, para 3.15, skill m). Do not claim it is a regulatory requirement or that it sets the standard at another level. Set it beside qaa/accounting-2025/3.13 and qaa/accounting-2025/3.15.b2 and the framework descriptor qaa/fheq-2024/4.15.b9.2 at spine:6."
  author-agent-dialogue: "Bring it up when a student asks about skill m: communication, or when staff check a module or outcome against it. Tell a student in plain words, as 'you', what it means for their course; for staff, frame it as an expected outcome stated without one of the five obliging words (force recorded as describes). Ask: How would you explain the same result to a board, a regulator and a community group? Avoid long quotation of the issuer's text."
- statement: qaa/accounting-2025/3.15.b2
  forPractitioner: { text: "Graduates are expected to collaborate inclusively and with emotional intelligence in teams and across organisations, using listening, negotiation and persuasion, and to show leadership.", rewrite: light, force: must, status: drafted }
  forBeneficiary: { text: "You are expected to work well with others: listening, negotiating, persuading and leading, inclusively and with emotional intelligence, in teams and with other organisations.", rewrite: full, force: must, status: drafted }
  author-agent-written: "Write about this as an expected outcome stated without one of the five obliging words (force recorded as describes) for the bachelor's degree with honours, at FHEQ level 6 (FQHEIS level 10), on skill n: collaboration. Cite it as (QAA, 2025, Accounting Subject Benchmark Statement, para 3.15, skill n). Do not claim it is a regulatory requirement or that it sets the standard at another level. Set it beside qaa/accounting-2025/3.15.b1 and qaa/accounting-2025/3.15.b3 and the framework descriptor qaa/fheq-2024/4.15.b9.2 at spine:6."
  author-agent-dialogue: "Bring it up when a student asks about skill n: collaboration, or when staff check a module or outcome against it. Tell a student in plain words, as 'you', what it means for their course; for staff, frame it as an expected outcome stated without one of the five obliging words (force recorded as describes). Ask: What did you change in how you worked after a team project went badly? Avoid long quotation of the issuer's text."
- statement: qaa/accounting-2025/3.15.b3
  forPractitioner: { text: "Graduates are expected to show self-efficacy: confidence in their own ability, reflection, independent action, ownership of their development, resilience and the ability to prioritise.", rewrite: light, force: must, status: drafted }
  forBeneficiary: { text: "You are expected to believe in and act on your own ability, reflect on your progress, take charge of your own learning and of the results of your actions, and bounce back from setbacks.", rewrite: full, force: must, status: drafted }
  author-agent-written: "Write about this as an expected outcome stated without one of the five obliging words (force recorded as describes) for the bachelor's degree with honours, at FHEQ level 6 (FQHEIS level 10), on skill o: self-efficacy and lifelong learning. Cite it as (QAA, 2025, Accounting Subject Benchmark Statement, para 3.15, skill o). Do not claim it is a regulatory requirement or that it sets the standard at another level. Set it beside qaa/accounting-2025/3.15.b2 and qaa/accounting-2025/3.15.b4 and the framework descriptor qaa/fheq-2024/4.15.b9.2 at spine:6."
  author-agent-dialogue: "Bring it up when a student asks about skill o: self-efficacy and lifelong learning, or when staff check a module or outcome against it. Tell a student in plain words, as 'you', what it means for their course; for staff, frame it as an expected outcome stated without one of the five obliging words (force recorded as describes). Ask: What is the next thing you need to learn, and how will you go about it without being told to? Avoid long quotation of the issuer's text."
- statement: qaa/accounting-2025/3.15.b4
  forPractitioner: { text: "Graduates are expected to evaluate evidence, arguments, theory and research critically, judge under uncertainty, apply scepticism and take an ethical stance.", rewrite: light, force: must, status: drafted }
  forBeneficiary: { text: "You are expected to weigh evidence, arguments and research critically, make judgements when things are uncertain, apply professional scepticism and take an ethical stand.", rewrite: full, force: must, status: drafted }
  author-agent-written: "Write about this as an expected outcome stated without one of the five obliging words (force recorded as describes) for the bachelor's degree with honours, at FHEQ level 6 (FQHEIS level 10), on skill p: critical thinking and scepticism. Cite it as (QAA, 2025, Accounting Subject Benchmark Statement, para 3.15, skill p). Do not claim it is a regulatory requirement or that it sets the standard at another level. Set it beside qaa/accounting-2025/3.15.b3 and qaa/accounting-2025/3.15.b5 and the framework descriptor qaa/fheq-2024/4.15.b9.2 at spine:6."
  author-agent-dialogue: "Bring it up when a student asks about skill p: critical thinking and scepticism, or when staff check a module or outcome against it. Tell a student in plain words, as 'you', what it means for their course; for staff, frame it as an expected outcome stated without one of the five obliging words (force recorded as describes). Ask: What evidence would change your mind about a conclusion you hold firmly? Avoid long quotation of the issuer's text."
- statement: qaa/accounting-2025/3.15.b5
  forPractitioner: { text: "Graduates are expected to diagnose problems from data in structured and unstructured situations, compare options with ethical reasoning and choose ethical, sustainable solutions.", rewrite: light, force: must, status: drafted }
  forBeneficiary: { text: "You are expected to work out the likely causes of a problem from the data, compare possible actions, including their ethics, and choose solutions that are ethical and sustainable.", rewrite: full, force: must, status: drafted }
  author-agent-written: "Write about this as an expected outcome stated without one of the five obliging words (force recorded as describes) for the bachelor's degree with honours, at FHEQ level 6 (FQHEIS level 10), on skill q: problem solving and reasoning. Cite it as (QAA, 2025, Accounting Subject Benchmark Statement, para 3.15, skill q). Do not claim it is a regulatory requirement or that it sets the standard at another level. Set it beside qaa/accounting-2025/3.15.b4 and qaa/accounting-2025/3.15.b6 and the framework descriptor qaa/fheq-2024/4.15.b9.2 at spine:6."
  author-agent-dialogue: "Bring it up when a student asks about skill q: problem solving and reasoning, or when staff check a module or outcome against it. Tell a student in plain words, as 'you', what it means for their course; for staff, frame it as an expected outcome stated without one of the five obliging words (force recorded as describes). Ask: What were the other options you rejected for your last recommendation, and why? Avoid long quotation of the issuer's text."
- statement: qaa/accounting-2025/3.15.b6
  forPractitioner: { text: "Graduates are expected to source, verify, filter, evaluate and interpret data, reach reasoned conclusions on messy real problems and present findings to suit the audience, using visualisation where it helps.", rewrite: light, force: must, status: drafted }
  forBeneficiary: { text: "You are expected to find, check and interpret data from different sources, draw reasoned conclusions even when the data is incomplete, and present what you find in a form your audience can use.", rewrite: full, force: must, status: drafted }
  author-agent-written: "Write about this as an expected outcome stated without one of the five obliging words (force recorded as describes) for the bachelor's degree with honours, at FHEQ level 6 (FQHEIS level 10), on skill r: data analysis. Cite it as (QAA, 2025, Accounting Subject Benchmark Statement, para 3.15, skill r). Do not claim it is a regulatory requirement or that it sets the standard at another level. Set it beside qaa/accounting-2025/3.15.b5 and qaa/accounting-2025/3.15.b7 and the framework descriptor qaa/fheq-2024/4.15.b9.2 at spine:6."
  author-agent-dialogue: "Bring it up when a student asks about skill r: data analysis, or when staff check a module or outcome against it. Tell a student in plain words, as 'you', what it means for their course; for staff, frame it as an expected outcome stated without one of the five obliging words (force recorded as describes). Ask: How did you check the reliability of the data behind your last conclusion? Avoid long quotation of the issuer's text."
- statement: qaa/accounting-2025/3.15.b7
  forPractitioner: { text: "Graduates are expected to think in systems: analyse, design, evaluate and improve the systems that supply data for reporting and decisions, including their controls against error, fraud and cyber risk.", rewrite: light, force: must, status: drafted }
  forBeneficiary: { text: "You are expected to see how processes connect as systems and to help analyse, design and improve the systems that produce data, including controls against error, fraud and cyber attack.", rewrite: full, force: must, status: drafted }
  author-agent-written: "Write about this as an expected outcome stated without one of the five obliging words (force recorded as describes) for the bachelor's degree with honours, at FHEQ level 6 (FQHEIS level 10), on skill s: systems thinking. Cite it as (QAA, 2025, Accounting Subject Benchmark Statement, para 3.15, skill s). Do not claim it is a regulatory requirement or that it sets the standard at another level. Set it beside qaa/accounting-2025/3.15.b6 and qaa/accounting-2025/3.15.b8 and the framework descriptor qaa/fheq-2024/4.15.b9.2 at spine:6."
  author-agent-dialogue: "Bring it up when a student asks about skill s: systems thinking, or when staff check a module or outcome against it. Tell a student in plain words, as 'you', what it means for their course; for staff, frame it as an expected outcome stated without one of the five obliging words (force recorded as describes). Ask: If one control in a purchasing system failed, what else in the system would be affected? Avoid long quotation of the issuer's text."
- statement: qaa/accounting-2025/3.15.b8
  forPractitioner: { text: "Graduates are expected to handle, communicate and secure data in all forms and to use and evaluate spreadsheets, databases, AI and new technologies as they arrive.", rewrite: light, force: must, status: drafted }
  forBeneficiary: { text: "You are expected to handle and share data in all its forms, keep it secure and use and judge tools such as spreadsheets, databases and AI as new ones appear.", rewrite: full, force: must, status: drafted }
  author-agent-written: "Write about this as an expected outcome stated without one of the five obliging words (force recorded as describes) for the bachelor's degree with honours, at FHEQ level 6 (FQHEIS level 10), on skill t: digital literacy. Cite it as (QAA, 2025, Accounting Subject Benchmark Statement, para 3.15, skill t). Do not claim it is a regulatory requirement or that it sets the standard at another level. Set it beside qaa/accounting-2025/3.15.b7 and qaa/accounting-2025/3.15.b9 and the framework descriptor qaa/fheq-2024/4.15.b9.2 at spine:6."
  author-agent-dialogue: "Bring it up when a student asks about skill t: digital literacy, or when staff check a module or outcome against it. Tell a student in plain words, as 'you', what it means for their course; for staff, frame it as an expected outcome stated without one of the five obliging words (force recorded as describes). Ask: Which new tool have you learned recently, and how did you judge whether it was reliable? Avoid long quotation of the issuer's text."
- statement: qaa/accounting-2025/3.15.b9
  forPractitioner: { text: "Graduates are expected to use quantitative skills to manipulate data and to evaluate, estimate and model business problems.", rewrite: light, force: must, status: drafted }
  forBeneficiary: { text: "You are expected to use number skills to work with data and to evaluate, estimate and model business problems.", rewrite: full, force: must, status: drafted }
  author-agent-written: "Write about this as an expected outcome stated without one of the five obliging words (force recorded as describes) for the bachelor's degree with honours, at FHEQ level 6 (FQHEIS level 10), on skill u: numeracy. Cite it as (QAA, 2025, Accounting Subject Benchmark Statement, para 3.15, skill u). Do not claim it is a regulatory requirement or that it sets the standard at another level. Set it beside qaa/accounting-2025/3.15.b8 and qaa/accounting-2025/3.15.b10 and the framework descriptor qaa/fheq-2024/4.15.b9.2 at spine:6."
  author-agent-dialogue: "Bring it up when a student asks about skill u: numeracy, or when staff check a module or outcome against it. Tell a student in plain words, as 'you', what it means for their course; for staff, frame it as an expected outcome stated without one of the five obliging words (force recorded as describes). Ask: How would you estimate a figure quickly to check whether a model's output is plausible? Avoid long quotation of the issuer's text."
- statement: qaa/accounting-2025/3.15.b10
  forPractitioner: { text: "Graduates are expected to show commercial awareness, business acumen, innovation, creativity and flexibility, with regard to the public interest and enterprise skills.", rewrite: light, force: must, status: drafted }
  forBeneficiary: { text: "You are expected to show commercial awareness and business sense, with creativity, flexibility and new ideas, while keeping the public interest in mind.", rewrite: full, force: must, status: drafted }
  author-agent-written: "Write about this as an expected outcome stated without one of the five obliging words (force recorded as describes) for the bachelor's degree with honours, at FHEQ level 6 (FQHEIS level 10), on skill v: entrepreneurialism. Cite it as (QAA, 2025, Accounting Subject Benchmark Statement, para 3.15, skill v). Do not claim it is a regulatory requirement or that it sets the standard at another level. Set it beside qaa/accounting-2025/3.15.b9 and qaa/accounting-2025/3.15.b11 and the framework descriptor qaa/fheq-2024/4.15.b9.2 at spine:6."
  author-agent-dialogue: "Bring it up when a student asks about skill v: entrepreneurialism, or when staff check a module or outcome against it. Tell a student in plain words, as 'you', what it means for their course; for staff, frame it as an expected outcome stated without one of the five obliging words (force recorded as describes). Ask: What opportunity have you spotted that others missed, and what would it take to act on it? Avoid long quotation of the issuer's text."
- statement: qaa/accounting-2025/3.15.b11
  forPractitioner: { text: "Graduates are expected to appreciate cultural differences and how they affect the discipline, study and organisations; on courses with time abroad, foreign language ability also matters.", rewrite: light, force: must, status: drafted }
  forBeneficiary: { text: "You are expected to appreciate cultural differences and how they can shape accounting, study and organisations; if your course includes time abroad, another language helps too.", rewrite: full, force: must, status: drafted }
  author-agent-written: "Write about this as an expected outcome stated without one of the five obliging words (force recorded as describes) for the bachelor's degree with honours, at FHEQ level 6 (FQHEIS level 10), on skill w: cultural awareness. Cite it as (QAA, 2025, Accounting Subject Benchmark Statement, para 3.15, skill w). Do not claim it is a regulatory requirement or that it sets the standard at another level. Set it beside qaa/accounting-2025/3.15.b10 and qaa/accounting-2025/3.15.b12 and the framework descriptor qaa/fheq-2024/4.15.b9.2 at spine:6."
  author-agent-dialogue: "Bring it up when a student asks about skill w: cultural awareness, or when staff check a module or outcome against it. Tell a student in plain words, as 'you', what it means for their course; for staff, frame it as an expected outcome stated without one of the five obliging words (force recorded as describes). Ask: How might a cultural difference change how a set of accounts is read? Avoid long quotation of the issuer's text."
- statement: qaa/accounting-2025/3.15.b12
  forPractitioner: { text: "Graduates are expected to plan and complete a systematic investigation: critical use of literature, credible sources, focused questions, analysis, project management and clear reporting of findings.", rewrite: light, force: must, status: drafted }
  forBeneficiary: { text: "You are expected to carry out a careful, systematic investigation of your own: read critically, find credible sources, ask good questions, analyse, manage the project and present clear findings.", rewrite: full, force: must, status: drafted }
  author-agent-written: "Write about this as an expected outcome stated without one of the five obliging words (force recorded as describes) for the bachelor's degree with honours, at FHEQ level 6 (FQHEIS level 10), on skill x: research. Cite it as (QAA, 2025, Accounting Subject Benchmark Statement, para 3.15, skill x). Do not claim it is a regulatory requirement or that it sets the standard at another level. Set it beside qaa/accounting-2025/3.15.b11 and qaa/accounting-2025/3.16 and the framework descriptor qaa/fheq-2024/4.15.b9.2 at spine:6."
  author-agent-dialogue: "Bring it up when a student asks about skill x: research, or when staff check a module or outcome against it. Tell a student in plain words, as 'you', what it means for their course; for staff, frame it as an expected outcome stated without one of the five obliging words (force recorded as describes). Ask: What question would you most like to investigate, and how would you know your sources were credible? Avoid long quotation of the issuer's text."
- statement: qaa/accounting-2025/3.16
  forPractitioner: { text: "Design the learning and teaching strategy to develop conceptual and applied knowledge, higher-order thinking, technical skills and professional and transferable skills together.", rewrite: light, force: will, status: drafted }
  forBeneficiary: { text: "not-applicable: a duty on the course and the people who design and run it, not a standard the student reaches", rewrite: full, force: will, status: drafted }
  author-agent-written: "Write about this as an expected feature worded with \"will\" on the course and its team, on learning and teaching strategy, holding for any Accounting degree the statement covers. Cite it as (QAA, 2025, Accounting Subject Benchmark Statement, para 3.16). Do not present it as a regulatory requirement, and do not turn it into an outcome a student must show. Set it beside qaa/accounting-2025/3.15.b12 and qaa/accounting-2025/3.17, and where it shapes outcomes beside the honours and master's descriptors (qaa/fheq-2024/4.15.b1, qaa/fheq-2024/4.17.b1) at spine:6 and spine:7."
  author-agent-dialogue: "Raise it with a programme team or teacher who is designing, reviewing or defending the course's approach to learning and teaching strategy. Frame it for staff as an expected feature worded with \"will\", and ask: Which of these four strands gets the least teaching time? Do not quote the issuer at length, and do not put this duty to a student as something they have to achieve."
- statement: qaa/accounting-2025/3.17
  forPractitioner: { text: "Align activities with intended outcomes and with assessment, balance conceptual and applied work and encourage continuing enquiry and lifelong learning.", rewrite: light, force: will, status: drafted }
  forBeneficiary: { text: "not-applicable: a duty on the course and the people who design and run it, not a standard the student reaches", rewrite: full, force: will, status: drafted }
  author-agent-written: "Write about this as an expected feature worded with \"will\" on the course and its team, on constructive alignment and balance, holding for any Accounting degree the statement covers. Cite it as (QAA, 2025, Accounting Subject Benchmark Statement, para 3.17). Do not present it as a regulatory requirement, and do not turn it into an outcome a student must show. Set it beside qaa/accounting-2025/3.16 and qaa/accounting-2025/3.18, and where it shapes outcomes beside the honours and master's descriptors (qaa/fheq-2024/4.15.b1, qaa/fheq-2024/4.17.b1) at spine:6 and spine:7."
  author-agent-dialogue: "Raise it with a programme team or teacher who is designing, reviewing or defending the course's approach to constructive alignment and balance. Frame it for staff as an expected feature worded with \"will\", and ask: For one module, can you trace each outcome to an activity and an assessment? Do not quote the issuer at length, and do not put this duty to a student as something they have to achieve."
- statement: qaa/accounting-2025/3.18
  forPractitioner: { text: "Design teaching to build employability and civic responsibility together; where possible offer placements where students apply their learning.", rewrite: light, force: should, status: drafted }
  forBeneficiary: { text: "Your course should help you build the skills, attitudes and experience to become an employable professional and a responsible citizen, sometimes through a placement.", rewrite: full, force: should, status: drafted }
  author-agent-written: "Write about this as an expectation worded with \"should\" for any Accounting degree the statement covers, at the level of the award it is applied to, on employability and responsible citizenship. Cite it as (QAA, 2025, Accounting Subject Benchmark Statement, para 3.18). Do not claim it is a regulatory requirement or that it sets the standard at another level. Set it beside qaa/accounting-2025/3.17 and qaa/accounting-2025/3.19 and the framework descriptor the honours and master's descriptors (qaa/fheq-2024/4.15.b1, qaa/fheq-2024/4.17.b1) at spine:6 and spine:7."
  author-agent-dialogue: "Bring it up when a student asks about employability and responsible citizenship, or when staff check a module or outcome against it. Tell a student in plain words, as 'you', what it means for their course; for staff, frame it as an expectation worded with \"should\". Ask: What experience outside the classroom would most help your career plans? Avoid long quotation of the issuer's text."
- statement: qaa/accounting-2025/3.19
  forPractitioner: { text: "Choose pedagogies (dialogic, critical, reflexive, constructivist, collaborative) that produce deep rather than rote learning, and let them shape assessment.", rewrite: light, force: should, status: drafted }
  forBeneficiary: { text: "not-applicable: a duty on the course and the people who design and run it, not a standard the student reaches", rewrite: full, force: should, status: drafted }
  author-agent-written: "Write about this as an expectation worded with \"should\" on the course and its team, on pedagogy for deep learning, holding for any Accounting degree the statement covers. Cite it as (QAA, 2025, Accounting Subject Benchmark Statement, para 3.19). Do not present it as a regulatory requirement, and do not turn it into an outcome a student must show. Set it beside qaa/accounting-2025/3.18 and qaa/accounting-2025/3.20, and where it shapes outcomes beside the honours and master's descriptors (qaa/fheq-2024/4.15.b1, qaa/fheq-2024/4.17.b1) at spine:6 and spine:7."
  author-agent-dialogue: "Raise it with a programme team or teacher who is designing, reviewing or defending the course's approach to pedagogy for deep learning. Frame it for staff as an expectation worded with \"should\", and ask: Which teaching session most reliably produces deep rather than surface learning, and why? Do not quote the issuer at length, and do not put this duty to a student as something they have to achieve."
- statement: qaa/accounting-2025/3.20
  forPractitioner: { text: "Mix lectures, seminars, workshops, tutorials, blended and active learning, use the digital tools practice uses, and design for student engagement.", rewrite: light, force: should, status: drafted }
  forBeneficiary: { text: "not-applicable: a duty on the course and the people who design and run it, not a standard the student reaches", rewrite: full, force: should, status: drafted }
  author-agent-written: "Write about this as an expectation worded with \"should\" on the course and its team, on diverse and active teaching approaches, holding for any Accounting degree the statement covers. Cite it as (QAA, 2025, Accounting Subject Benchmark Statement, para 3.20). Do not present it as a regulatory requirement, and do not turn it into an outcome a student must show. Set it beside qaa/accounting-2025/3.19 and qaa/accounting-2025/3.22, and where it shapes outcomes beside the honours and master's descriptors (qaa/fheq-2024/4.15.b1, qaa/fheq-2024/4.17.b1) at spine:6 and spine:7."
  author-agent-dialogue: "Raise it with a programme team or teacher who is designing, reviewing or defending the course's approach to diverse and active teaching approaches. Frame it for staff as an expectation worded with \"should\", and ask: What share of contact time asks students to do something rather than listen? Do not quote the issuer at length, and do not put this duty to a student as something they have to achieve."
- statement: qaa/accounting-2025/3.22
  forPractitioner: { text: "Build current digital tools into teaching: cloud accounting packages, data preparation and analytics tools, spreadsheets and AI, refreshed as practice changes.", rewrite: light, force: will, status: drafted }
  forBeneficiary: { text: "not-applicable: a duty on the course and the people who design and run it, not a standard the student reaches", rewrite: full, force: will, status: drafted }
  author-agent-written: "Write about this as an expected feature worded with \"will\" on the course and its team, on digital technologies in teaching, holding for any Accounting degree the statement covers. Cite it as (QAA, 2025, Accounting Subject Benchmark Statement, para 3.22). Do not present it as a regulatory requirement, and do not turn it into an outcome a student must show. Set it beside qaa/accounting-2025/3.20 and qaa/accounting-2025/3.23, and where it shapes outcomes beside the honours and master's descriptors (qaa/fheq-2024/4.15.b1, qaa/fheq-2024/4.17.b1) at spine:6 and spine:7."
  author-agent-dialogue: "Raise it with a programme team or teacher who is designing, reviewing or defending the course's approach to digital technologies in teaching. Frame it for staff as an expected feature worded with \"will\", and ask: Which software that graduates will meet at work do they never use on the course? Do not quote the issuer at length, and do not put this duty to a student as something they have to achieve."
- statement: qaa/accounting-2025/3.23
  forPractitioner: { text: "Design teaching to be inclusive and accessible, and help students from varied educational cultures adjust to critical learning and learn from one another.", rewrite: light, force: should, status: drafted }
  forBeneficiary: { text: "Your course should be inclusive and accessible, and help you adjust if you are used to a different way of learning, and learn from classmates with other backgrounds.", rewrite: full, force: should, status: drafted }
  author-agent-written: "Write about this as an expectation worded with \"should\" for any Accounting degree the statement covers, at the level of the award it is applied to, on inclusive, accessible and culturally aware teaching. Cite it as (QAA, 2025, Accounting Subject Benchmark Statement, para 3.23). Do not claim it is a regulatory requirement or that it sets the standard at another level. Set it beside qaa/accounting-2025/3.22 and qaa/accounting-2025/3.24 and the framework descriptor the honours and master's descriptors (qaa/fheq-2024/4.15.b1, qaa/fheq-2024/4.17.b1) at spine:6 and spine:7."
  author-agent-dialogue: "Bring it up when a student asks about inclusive, accessible and culturally aware teaching, or when staff check a module or outcome against it. Tell a student in plain words, as 'you', what it means for their course; for staff, frame it as an expectation worded with \"should\". Ask: What was hardest to adjust to in how you are taught here, compared with before? Avoid long quotation of the issuer's text."
- statement: qaa/accounting-2025/3.24
  forPractitioner: { text: "Keep teaching research-informed or research-led, and draw on staff's professional and academic experience to reflect current developments.", rewrite: light, force: should, status: drafted }
  forBeneficiary: { text: "not-applicable: a duty on the course and the people who design and run it, not a standard the student reaches", rewrite: full, force: should, status: drafted }
  author-agent-written: "Write about this as an expectation worded with \"should\" on the course and its team, on research-informed and practice-informed teaching, holding for any Accounting degree the statement covers. Cite it as (QAA, 2025, Accounting Subject Benchmark Statement, para 3.24). Do not present it as a regulatory requirement, and do not turn it into an outcome a student must show. Set it beside qaa/accounting-2025/3.23 and qaa/accounting-2025/3.25, and where it shapes outcomes beside the honours and master's descriptors (qaa/fheq-2024/4.15.b1, qaa/fheq-2024/4.17.b1) at spine:6 and spine:7."
  author-agent-dialogue: "Raise it with a programme team or teacher who is designing, reviewing or defending the course's approach to research-informed and practice-informed teaching. Frame it for staff as an expectation worded with \"should\", and ask: Where does current research or practice experience show up in a core module? Do not quote the issuer at length, and do not put this duty to a student as something they have to achieve."
- statement: qaa/accounting-2025/3.25
  forPractitioner: { text: "Update strategies for business, regulatory and technological change, use pedagogic research and give teaching staff professional development and training.", rewrite: light, force: should, status: drafted }
  forBeneficiary: { text: "not-applicable: a duty on the course and the people who design and run it, not a standard the student reaches", rewrite: full, force: should, status: drafted }
  author-agent-written: "Write about this as an expectation worded with \"should\" on the course and its team, on responsive strategy and staff development, holding for any Accounting degree the statement covers. Cite it as (QAA, 2025, Accounting Subject Benchmark Statement, para 3.25). Do not present it as a regulatory requirement, and do not turn it into an outcome a student must show. Set it beside qaa/accounting-2025/3.24 and qaa/accounting-2025/3.26, and where it shapes outcomes beside the honours and master's descriptors (qaa/fheq-2024/4.15.b1, qaa/fheq-2024/4.17.b1) at spine:6 and spine:7."
  author-agent-dialogue: "Raise it with a programme team or teacher who is designing, reviewing or defending the course's approach to responsive strategy and staff development. Frame it for staff as an expectation worded with \"should\", and ask: What training have staff had in the last year on new technology for teaching? Do not quote the issuer at length, and do not put this duty to a student as something they have to achieve."
- statement: qaa/accounting-2025/3.26
  forPractitioner: { text: "Review the learning and teaching strategy continually, through the monitoring and review cycle, for quality and currency.", rewrite: light, force: should, status: drafted }
  forBeneficiary: { text: "not-applicable: a duty on the course and the people who design and run it, not a standard the student reaches", rewrite: full, force: should, status: drafted }
  author-agent-written: "Write about this as an expectation worded with \"should\" on the course and its team, on reviewing learning and teaching, holding for any Accounting degree the statement covers. Cite it as (QAA, 2025, Accounting Subject Benchmark Statement, para 3.26). Do not present it as a regulatory requirement, and do not turn it into an outcome a student must show. Set it beside qaa/accounting-2025/3.25 and qaa/accounting-2025/3.27, and where it shapes outcomes beside the honours and master's descriptors (qaa/fheq-2024/4.15.b1, qaa/fheq-2024/4.17.b1) at spine:6 and spine:7."
  author-agent-dialogue: "Raise it with a programme team or teacher who is designing, reviewing or defending the course's approach to reviewing learning and teaching. Frame it for staff as an expectation worded with \"should\", and ask: What did the last review of teaching approaches change? Do not quote the issuer at length, and do not put this duty to a student as something they have to achieve."
- statement: qaa/accounting-2025/3.27
  forPractitioner: { text: "Make summative assessment robust and rigorous against the knowledge, understanding and skills in the statement as written into the outcomes.", rewrite: light, force: should, status: drafted }
  forBeneficiary: { text: "not-applicable: a duty on the course and the people who design and run it, not a standard the student reaches", rewrite: full, force: should, status: drafted }
  author-agent-written: "Write about this as an expectation worded with \"should\" on the course and its team, on robust summative assessment, holding for any Accounting degree the statement covers. Cite it as (QAA, 2025, Accounting Subject Benchmark Statement, para 3.27). Do not present it as a regulatory requirement, and do not turn it into an outcome a student must show. Set it beside qaa/accounting-2025/3.26 and qaa/accounting-2025/3.28, and where it shapes outcomes beside the honours and master's descriptors (qaa/fheq-2024/4.15.b1, qaa/fheq-2024/4.17.b1) at spine:6 and spine:7."
  author-agent-dialogue: "Raise it with a programme team or teacher who is designing, reviewing or defending the course's approach to robust summative assessment. Frame it for staff as an expectation worded with \"should\", and ask: Which programme outcome is assessed least rigorously? Do not quote the issuer at length, and do not put this duty to a student as something they have to achieve."
- statement: qaa/accounting-2025/3.28
  forPractitioner: { text: "Provide a range of formative assessments and feedback that encourage active, independent learning.", rewrite: light, force: should, status: drafted }
  forBeneficiary: { text: "not-applicable: a duty on the course and the people who design and run it, not a standard the student reaches", rewrite: full, force: should, status: drafted }
  author-agent-written: "Write about this as an expectation worded with \"should\" on the course and its team, on formative assessment and feedback, holding for any Accounting degree the statement covers. Cite it as (QAA, 2025, Accounting Subject Benchmark Statement, para 3.28). Do not present it as a regulatory requirement, and do not turn it into an outcome a student must show. Set it beside qaa/accounting-2025/3.27 and qaa/accounting-2025/3.29, and where it shapes outcomes beside the honours and master's descriptors (qaa/fheq-2024/4.15.b1, qaa/fheq-2024/4.17.b1) at spine:6 and spine:7."
  author-agent-dialogue: "Raise it with a programme team or teacher who is designing, reviewing or defending the course's approach to formative assessment and feedback. Frame it for staff as an expectation worded with \"should\", and ask: How many formative opportunities does a student get before the first summative task? Do not quote the issuer at length, and do not put this duty to a student as something they have to achieve."
- statement: qaa/accounting-2025/3.29
  forPractitioner: { text: "Balance assessment methods across the degree so the scheme is inclusive, flexible and innovative and shows progression.", rewrite: light, force: should, status: drafted }
  forBeneficiary: { text: "not-applicable: a duty on the course and the people who design and run it, not a standard the student reaches", rewrite: full, force: should, status: drafted }
  author-agent-written: "Write about this as an expectation worded with \"should\" on the course and its team, on a balanced and inclusive portfolio, holding for any Accounting degree the statement covers. Cite it as (QAA, 2025, Accounting Subject Benchmark Statement, para 3.29). Do not present it as a regulatory requirement, and do not turn it into an outcome a student must show. Set it beside qaa/accounting-2025/3.28 and qaa/accounting-2025/3.30, and where it shapes outcomes beside the honours and master's descriptors (qaa/fheq-2024/4.15.b1, qaa/fheq-2024/4.17.b1) at spine:6 and spine:7."
  author-agent-dialogue: "Raise it with a programme team or teacher who is designing, reviewing or defending the course's approach to a balanced and inclusive portfolio. Frame it for staff as an expectation worded with \"should\", and ask: Is any single method used so often that it advantages one group of students? Do not quote the issuer at length, and do not put this duty to a student as something they have to achieve."
- statement: qaa/accounting-2025/3.30
  forPractitioner: { text: "Weight and structure assessment so students cannot pass by focusing on calculation and technique alone; the discursive and critical elements must be unavoidable.", rewrite: light, force: should, status: drafted }
  forBeneficiary: { text: "not-applicable: a duty on the course and the people who design and run it, not a standard the student reaches", rewrite: full, force: should, status: drafted }
  author-agent-written: "Write about this as an expectation worded with \"should\" on the course and its team, on no route around critical elements, holding for any Accounting degree the statement covers. Cite it as (QAA, 2025, Accounting Subject Benchmark Statement, para 3.30). Do not present it as a regulatory requirement, and do not turn it into an outcome a student must show. Set it beside qaa/accounting-2025/3.29 and qaa/accounting-2025/3.31, and where it shapes outcomes beside the honours and master's descriptors (qaa/fheq-2024/4.15.b1, qaa/fheq-2024/4.17.b1) at spine:6 and spine:7."
  author-agent-dialogue: "Raise it with a programme team or teacher who is designing, reviewing or defending the course's approach to no route around critical elements. Frame it for staff as an expectation worded with \"should\", and ask: Could a student pass the degree with almost no essay or critical writing? Do not quote the issuer at length, and do not put this duty to a student as something they have to achieve."
- statement: qaa/accounting-2025/3.31
  forPractitioner: { text: "Design out rote learning: include substantial critical, authentic and case-based assessment, embed technical questions in dynamic scenarios and use multiple choice only where it is designed not to reward surface learning.", rewrite: light, force: should, status: drafted }
  forBeneficiary: { text: "not-applicable: a duty on the course and the people who design and run it, not a standard the student reaches", rewrite: full, force: should, status: drafted }
  author-agent-written: "Write about this as an expectation worded with \"should\" on the course and its team, on assessing depth, not rote learning, holding for any Accounting degree the statement covers. Cite it as (QAA, 2025, Accounting Subject Benchmark Statement, para 3.31). Do not present it as a regulatory requirement, and do not turn it into an outcome a student must show. Set it beside qaa/accounting-2025/3.30 and qaa/accounting-2025/3.32, and where it shapes outcomes beside the honours and master's descriptors (qaa/fheq-2024/4.15.b1, qaa/fheq-2024/4.17.b1) at spine:6 and spine:7."
  author-agent-dialogue: "Raise it with a programme team or teacher who is designing, reviewing or defending the course's approach to assessing depth, not rote learning. Frame it for staff as an expectation worded with \"should\", and ask: What proportion of marks in core modules comes from objective tests? Do not quote the issuer at length, and do not put this duty to a student as something they have to achieve."
- statement: qaa/accounting-2025/3.32
  forPractitioner: { text: "Design assessment and feedback to develop independent, self-directed and critical learners, with feedback aimed at the next task.", rewrite: light, force: should, status: drafted }
  forBeneficiary: { text: "Your assessments and feedback should help you become an independent, critical learner who keeps learning after graduation.", rewrite: full, force: should, status: drafted }
  author-agent-written: "Write about this as an expectation worded with \"should\" for the bachelor's degree with honours, at FHEQ level 6 (FQHEIS level 10), on assessment for independent, lifelong learners. Cite it as (QAA, 2025, Accounting Subject Benchmark Statement, para 3.32). Do not claim it is a regulatory requirement or that it sets the standard at another level. Set it beside qaa/accounting-2025/3.31 and qaa/accounting-2025/3.33 and the framework descriptor qaa/fheq-2024/4.15.b9.2 at spine:6."
  author-agent-dialogue: "Bring it up when a student asks about assessment for independent, lifelong learners, or when staff check a module or outcome against it. Tell a student in plain words, as 'you', what it means for their course; for staff, frame it as an expectation worded with \"should\". Ask: How have you used feedback from one assessment in the next? Avoid long quotation of the issuer's text."
- statement: qaa/accounting-2025/3.33
  forPractitioner: { text: "Make assessment inclusive and accessible, with reasonable adjustments that keep the assessment's purpose and the outcomes intact.", rewrite: light, force: should, status: drafted }
  forBeneficiary: { text: "not-applicable: a duty on the course and the people who design and run it, not a standard the student reaches", rewrite: full, force: should, status: drafted }
  author-agent-written: "Write about this as an expectation worded with \"should\" on the course and its team, on inclusive assessment and reasonable adjustments, holding for any Accounting degree the statement covers. Cite it as (QAA, 2025, Accounting Subject Benchmark Statement, para 3.33). Do not present it as a regulatory requirement, and do not turn it into an outcome a student must show. Set it beside qaa/accounting-2025/3.32 and qaa/accounting-2025/3.34, and where it shapes outcomes beside the honours and master's descriptors (qaa/fheq-2024/4.15.b1, qaa/fheq-2024/4.17.b1) at spine:6 and spine:7."
  author-agent-dialogue: "Raise it with a programme team or teacher who is designing, reviewing or defending the course's approach to inclusive assessment and reasonable adjustments. Frame it for staff as an expectation worded with \"should\", and ask: Which adjustment request last tested whether an assessment's purpose could be kept? Do not quote the issuer at length, and do not put this duty to a student as something they have to achieve."
- statement: qaa/accounting-2025/3.34
  forPractitioner: { text: "Design assessment as dialogue: use exemplars, peer work and GenAI outputs for students to compare against their own, and give timely feedback they can act on.", rewrite: light, force: should, status: drafted }
  forBeneficiary: { text: "Your assessments should help you learn through dialogue, for example by comparing your work with examples, classmates' work or AI outputs, and you should get feedback in time to use it.", rewrite: full, force: should, status: drafted }
  author-agent-written: "Write about this as an expectation worded with \"should\" for any Accounting degree the statement covers, at the level of the award it is applied to, on assessment as dialogue and feedback. Cite it as (QAA, 2025, Accounting Subject Benchmark Statement, para 3.34). Do not claim it is a regulatory requirement or that it sets the standard at another level. Set it beside qaa/accounting-2025/3.33 and qaa/accounting-2025/3.35 and the framework descriptor the honours and master's descriptors (qaa/fheq-2024/4.15.b1, qaa/fheq-2024/4.17.b1) at spine:6 and spine:7."
  author-agent-dialogue: "Bring it up when a student asks about assessment as dialogue and feedback, or when staff check a module or outcome against it. Tell a student in plain words, as 'you', what it means for their course; for staff, frame it as an expectation worded with \"should\". Ask: Which comparison has taught you most about the quality of your own work? Avoid long quotation of the issuer's text."
- statement: qaa/accounting-2025/3.35
  forPractitioner: { text: "Publish each module's assessment scheme at the start and plan the timing and total assessment load across the programme.", rewrite: light, force: should, status: drafted }
  forBeneficiary: { text: "not-applicable: a duty on the course and the people who design and run it, not a standard the student reaches", rewrite: full, force: should, status: drafted }
  author-agent-written: "Write about this as an expectation worded with \"should\" on the course and its team, on clear assessment schemes and workload, holding for any Accounting degree the statement covers. Cite it as (QAA, 2025, Accounting Subject Benchmark Statement, para 3.35). Do not present it as a regulatory requirement, and do not turn it into an outcome a student must show. Set it beside qaa/accounting-2025/3.34 and qaa/accounting-2025/3.36, and where it shapes outcomes beside the honours and master's descriptors (qaa/fheq-2024/4.15.b1, qaa/fheq-2024/4.17.b1) at spine:6 and spine:7."
  author-agent-dialogue: "Raise it with a programme team or teacher who is designing, reviewing or defending the course's approach to clear assessment schemes and workload. Frame it for staff as an expectation worded with \"should\", and ask: Where do deadlines across modules cluster in the same week? Do not quote the issuer at length, and do not put this duty to a student as something they have to achieve."
- statement: qaa/accounting-2025/3.36
  forPractitioner: { text: "Give students the criteria before they begin each task, using indicative rubrics linked to module and programme outcomes rather than detailed marking schedules.", rewrite: light, force: should, status: drafted }
  forBeneficiary: { text: "not-applicable: a duty on the course and the people who design and run it, not a standard the student reaches", rewrite: full, force: should, status: drafted }
  author-agent-written: "Write about this as an expectation worded with \"should\" on the course and its team, on timely, indicative assessment criteria, holding for any Accounting degree the statement covers. Cite it as (QAA, 2025, Accounting Subject Benchmark Statement, para 3.36). Do not present it as a regulatory requirement, and do not turn it into an outcome a student must show. Set it beside qaa/accounting-2025/3.35 and qaa/accounting-2025/3.39, and where it shapes outcomes beside the honours and master's descriptors (qaa/fheq-2024/4.15.b1, qaa/fheq-2024/4.17.b1) at spine:6 and spine:7."
  author-agent-dialogue: "Raise it with a programme team or teacher who is designing, reviewing or defending the course's approach to timely, indicative assessment criteria. Frame it for staff as an expectation worded with \"should\", and ask: When do students first see the criteria for the main assessment in each module? Do not quote the issuer at length, and do not put this duty to a student as something they have to achieve."
- statement: qaa/accounting-2025/3.39
  forPractitioner: { text: "Where you assess group work, make grades reflect individual contributions, balance it with individual work and teach students how to manage teams.", rewrite: light, force: should, status: drafted }
  forBeneficiary: { text: "Where you are assessed as a group, your grade should fairly reflect your own contribution, and you should get guidance on how to run a team.", rewrite: full, force: should, status: drafted }
  author-agent-written: "Write about this as an expectation worded with \"should\" for any Accounting degree the statement covers, at the level of the award it is applied to, on fair team and group assessment. Cite it as (QAA, 2025, Accounting Subject Benchmark Statement, para 3.39). Do not claim it is a regulatory requirement or that it sets the standard at another level. Set it beside qaa/accounting-2025/3.36 and qaa/accounting-2025/3.41 and the framework descriptor the honours and master's descriptors (qaa/fheq-2024/4.15.b1, qaa/fheq-2024/4.17.b1) at spine:6 and spine:7."
  author-agent-dialogue: "Bring it up when a student asks about fair team and group assessment, or when staff check a module or outcome against it. Tell a student in plain words, as 'you', what it means for their course; for staff, frame it as an expectation worded with \"should\". Ask: How was your individual contribution recognised in your last group assessment? Avoid long quotation of the issuer's text."
- statement: qaa/accounting-2025/3.41
  forPractitioner: { text: "Manage peer review with safeguards and training; keep peer ratings out of summative marks unless strong protections and academic oversight are in place.", rewrite: light, force: should, status: drafted }
  forBeneficiary: { text: "not-applicable: a duty on the course and the people who design and run it, not a standard the student reaches", rewrite: full, force: should, status: drafted }
  author-agent-written: "Write about this as an expectation worded with \"should\" on the course and its team, on safeguards for peer assessment, holding for any Accounting degree the statement covers. Cite it as (QAA, 2025, Accounting Subject Benchmark Statement, para 3.41). Do not present it as a regulatory requirement, and do not turn it into an outcome a student must show. Set it beside qaa/accounting-2025/3.39 and qaa/accounting-2025/3.42, and where it shapes outcomes beside the honours and master's descriptors (qaa/fheq-2024/4.15.b1, qaa/fheq-2024/4.17.b1) at spine:6 and spine:7."
  author-agent-dialogue: "Raise it with a programme team or teacher who is designing, reviewing or defending the course's approach to safeguards for peer assessment. Frame it for staff as an expectation worded with \"should\", and ask: Do peer ratings count anywhere in summative marks, and what protects students who might be marked down unfairly? Do not quote the issuer at length, and do not put this duty to a student as something they have to achieve."
- statement: qaa/accounting-2025/3.42
  forPractitioner: { text: "Rework assessment for GenAI: authentic cases, dynamic scenarios, experiential tasks and assessment of students' understanding of AI in accounting, in formative and summative work.", rewrite: light, force: should, status: drafted }
  forBeneficiary: { text: "not-applicable: a duty on the course and the people who design and run it, not a standard the student reaches", rewrite: full, force: should, status: drafted }
  author-agent-written: "Write about this as an expectation worded with \"should\" on the course and its team, on GenAI and assessment design, holding for any Accounting degree the statement covers. Cite it as (QAA, 2025, Accounting Subject Benchmark Statement, para 3.42). Do not present it as a regulatory requirement, and do not turn it into an outcome a student must show. Set it beside qaa/accounting-2025/3.41 and qaa/accounting-2025/3.43, and where it shapes outcomes beside the honours and master's descriptors (qaa/fheq-2024/4.15.b1, qaa/fheq-2024/4.17.b1) at spine:6 and spine:7."
  author-agent-dialogue: "Raise it with a programme team or teacher who is designing, reviewing or defending the course's approach to GenAI and assessment design. Frame it for staff as an expectation worded with \"should\", and ask: Which assessments has the team redesigned since GenAI tools became common? Do not quote the issuer at length, and do not put this duty to a student as something they have to achieve."
- statement: qaa/accounting-2025/3.43
  forPractitioner: { text: "Review GenAI and integrity policies continuously, state acceptable use clearly to staff and students, and remind students of the profession's ethical standards.", rewrite: light, force: should, status: drafted }
  forBeneficiary: { text: "not-applicable: a duty on the course and the people who design and run it, not a standard the student reaches", rewrite: full, force: should, status: drafted }
  author-agent-written: "Write about this as an expectation worded with \"should\" on the course and its team, on GenAI policies communicated to all, holding for any Accounting degree the statement covers. Cite it as (QAA, 2025, Accounting Subject Benchmark Statement, para 3.43). Do not present it as a regulatory requirement, and do not turn it into an outcome a student must show. Set it beside qaa/accounting-2025/3.42, and where it shapes outcomes beside the honours and master's descriptors (qaa/fheq-2024/4.15.b1, qaa/fheq-2024/4.17.b1) at spine:6 and spine:7."
  author-agent-dialogue: "Raise it with a programme team or teacher who is designing, reviewing or defending the course's approach to GenAI policies communicated to all. Frame it for staff as an expectation worded with \"should\", and ask: Is acceptable GenAI use stated for each assessment, and do staff apply it the same way? Do not quote the issuer at length, and do not put this duty to a student as something they have to achieve."
- statement: qaa/accounting-2025/4.2
  forPractitioner: { text: "Do not read the standards as competence standards; if you write competence standards, use the statement and PSRB requirements and follow current EHRC guidance.", rewrite: light, force: should, status: drafted }
  forBeneficiary: { text: "not-applicable: a duty on the course and the people who design and run it, not a standard the student reaches", rewrite: full, force: should, status: drafted }
  author-agent-written: "Write about this as an expectation worded with \"should\" on the course and its team, on competence standards and EHRC guidance, holding for any Accounting degree the statement covers. Cite it as (QAA, 2025, Accounting Subject Benchmark Statement, para 4.2). Do not present it as a regulatory requirement, and do not turn it into an outcome a student must show. Set it beside qaa/accounting-2025/4.4, and where it shapes outcomes beside the honours and master's descriptors (qaa/fheq-2024/4.15.b1, qaa/fheq-2024/4.17.b1) at spine:6 and spine:7."
  author-agent-dialogue: "Raise it with a programme team or teacher who is designing, reviewing or defending the course's approach to competence standards and EHRC guidance. Frame it for staff as an expectation worded with \"should\", and ask: Has the course defined competence standards, and were they checked against current EHRC guidance? Do not quote the issuer at length, and do not put this duty to a student as something they have to achieve."
- statement: qaa/accounting-2025/4.4
  forPractitioner: { text: "Apply the standards as a guide, not a mark scheme: your institution sets the evidence each class needs, and most students should exceed the threshold.", rewrite: light, force: should, status: drafted }
  forBeneficiary: { text: "not-applicable: a duty on the course and the people who design and run it, not a standard the student reaches", rewrite: full, force: should, status: drafted }
  author-agent-written: "Write about this as an expectation worded with \"should\" on the course and its team, on interpreting the standards, holding for any Accounting degree the statement covers. Cite it as (QAA, 2025, Accounting Subject Benchmark Statement, para 4.4). Do not present it as a regulatory requirement, and do not turn it into an outcome a student must show. Set it beside qaa/accounting-2025/4.2, and where it shapes outcomes beside the honours and master's descriptors (qaa/fheq-2024/4.15.b1, qaa/fheq-2024/4.17.b1) at spine:6 and spine:7."
  author-agent-dialogue: "Raise it with a programme team or teacher who is designing, reviewing or defending the course's approach to interpreting the standards. Frame it for staff as an expectation worded with \"should\", and ask: How do the institution's class descriptors line up with the four levels in Table 1? Do not quote the issuer at length, and do not put this duty to a student as something they have to achieve."
- statement: qaa/accounting-2025/4.5.b1
  forPractitioner: { text: "At threshold, graduates have a basic grasp of accounting's critical, ethical and contextual significance.", rewrite: light, force: threshold, status: drafted }
  forBeneficiary: { text: "For a third or a pass, at the least, you need a basic grasp of why accounting matters ethically, critically and in its wider setting.", rewrite: full, force: threshold, status: drafted }
  author-agent-written: "Write about this as the threshold level of Table 1, the least a graduate shows for a third-class or pass honours degree in Accounting at FHEQ level 6 (FQHEIS level 10): critical, ethical and contextual knowledge. Cite it as (QAA, 2025, Accounting Subject Benchmark Statement, para 4.5, Table 1). Do not present it as a regulatory requirement, as a mark scheme or as a level for master's awards. Set it beside qaa/accounting-2025/4.5.b3, the Annex D band qaa/fheq-2024/annex-d/knowledge/r2/3rd and the descriptor qaa/fheq-2024/4.15.b1 at spine:6."
  author-agent-dialogue: "Raise it when a student asks what third-class or pass work looks like in critical, ethical and contextual knowledge, or when markers calibrate between classes. Tell a student plainly what the level asks of them; with staff, treat it as a guide to a class boundary, not a mark scheme. Ask: Can you say in a few sentences why accounting is more than a technical exercise? Make clear that this is the floor for any honours award, not the target."
- statement: qaa/accounting-2025/4.5.b2
  forPractitioner: { text: "At threshold, graduates show some capacity to draw theory and debate into discussion of public and organisational questions from several perspectives.", rewrite: light, force: threshold, status: drafted }
  forBeneficiary: { text: "For a third or a pass, at the least, you need some ability to bring theories and debates into a discussion of public or organisational questions, looking at them from more than one angle.", rewrite: full, force: threshold, status: drafted }
  author-agent-written: "Write about this as the threshold level of Table 1, the least a graduate shows for a third-class or pass honours degree in Accounting at FHEQ level 6 (FQHEIS level 10): bringing theory into discussion of public and organisational issues. Cite it as (QAA, 2025, Accounting Subject Benchmark Statement, para 4.5, Table 1). Do not present it as a regulatory requirement, as a mark scheme or as a level for master's awards. Set it beside qaa/accounting-2025/4.5.b4, the Annex D band qaa/fheq-2024/annex-d/cognitive/r2/3rd and the descriptor qaa/fheq-2024/4.15.b7 at spine:6."
  author-agent-dialogue: "Raise it when a student asks what third-class or pass work looks like in bringing theory into discussion of public and organisational issues, or when markers calibrate between classes. Tell a student plainly what the level asks of them; with staff, treat it as a guide to a class boundary, not a mark scheme. Ask: Which theory have you used to make sense of a real organisational issue? Make clear that this is the floor for any honours award, not the target."
- statement: qaa/accounting-2025/4.5.b3
  forPractitioner: { text: "At the typical level, graduates have a solid grasp of accounting's critical, ethical and contextual significance.", rewrite: light, force: threshold, status: drafted }
  forBeneficiary: { text: "For a lower second (2:2), at the least, you need a solid grasp of why accounting matters ethically, critically and in its wider setting.", rewrite: full, force: threshold, status: drafted }
  author-agent-written: "Write about this as the typical level of Table 1, the least a graduate shows for a lower second (2:2) honours degree in Accounting at FHEQ level 6 (FQHEIS level 10): critical, ethical and contextual knowledge. Cite it as (QAA, 2025, Accounting Subject Benchmark Statement, para 4.5, Table 1). Do not present it as a regulatory requirement, as a mark scheme or as a level for master's awards. Set it beside qaa/accounting-2025/4.5.b1 and qaa/accounting-2025/4.5.b5, the Annex D band qaa/fheq-2024/annex-d/knowledge/r2/2.2 and the descriptor qaa/fheq-2024/4.15.b1 at spine:6."
  author-agent-dialogue: "Raise it when a student asks what lower second (2:2) work looks like in critical, ethical and contextual knowledge, or when markers calibrate between classes. Tell a student plainly what the level asks of them; with staff, treat it as a guide to a class boundary, not a mark scheme. Ask: Where does your understanding of accounting's wider importance feel secure, and where thin? Never present this level as what is needed simply to pass."
- statement: qaa/accounting-2025/4.5.b4
  forPractitioner: { text: "At the typical level, graduates bring theory and debate well into critical discussion of public and organisational questions from several perspectives.", rewrite: light, force: threshold, status: drafted }
  forBeneficiary: { text: "For a lower second (2:2), at the least, you need to bring theories and debates well into a critical discussion of public or organisational questions from several angles.", rewrite: full, force: threshold, status: drafted }
  author-agent-written: "Write about this as the typical level of Table 1, the least a graduate shows for a lower second (2:2) honours degree in Accounting at FHEQ level 6 (FQHEIS level 10): bringing theory into critical discussion of public and organisational issues. Cite it as (QAA, 2025, Accounting Subject Benchmark Statement, para 4.5, Table 1). Do not present it as a regulatory requirement, as a mark scheme or as a level for master's awards. Set it beside qaa/accounting-2025/4.5.b2 and qaa/accounting-2025/4.5.b6, the Annex D band qaa/fheq-2024/annex-d/cognitive/r2/2.2 and the descriptor qaa/fheq-2024/4.15.b7 at spine:6."
  author-agent-dialogue: "Raise it when a student asks what lower second (2:2) work looks like in bringing theory into critical discussion of public and organisational issues, or when markers calibrate between classes. Tell a student plainly what the level asks of them; with staff, treat it as a guide to a class boundary, not a mark scheme. Ask: In your last essay, did the theory drive the argument or decorate it? Never present this level as what is needed simply to pass."
- statement: qaa/accounting-2025/4.5.b5
  forPractitioner: { text: "At the very good level, graduates have a very good grasp of accounting's critical, ethical and contextual significance.", rewrite: light, force: threshold, status: drafted }
  forBeneficiary: { text: "For an upper second (2:1), at the least, you need a very good grasp of why accounting matters ethically, critically and in its wider setting.", rewrite: full, force: threshold, status: drafted }
  author-agent-written: "Write about this as the very good level of Table 1, the least a graduate shows for an upper second (2:1) honours degree in Accounting at FHEQ level 6 (FQHEIS level 10): critical, ethical and contextual knowledge. Cite it as (QAA, 2025, Accounting Subject Benchmark Statement, para 4.5, Table 1). Do not present it as a regulatory requirement, as a mark scheme or as a level for master's awards. Set it beside qaa/accounting-2025/4.5.b3 and qaa/accounting-2025/4.5.b7, the Annex D band qaa/fheq-2024/annex-d/knowledge/r2/2.1 and the descriptor qaa/fheq-2024/4.15.b1 at spine:6."
  author-agent-dialogue: "Raise it when a student asks what upper second (2:1) work looks like in critical, ethical and contextual knowledge, or when markers calibrate between classes. Tell a student plainly what the level asks of them; with staff, treat it as a guide to a class boundary, not a mark scheme. Ask: Can you explain an ethical tension in accounting and the context that creates it? Never present this level as what is needed simply to pass."
- statement: qaa/accounting-2025/4.5.b6
  forPractitioner: { text: "At the very good level, graduates integrate theory and debate into critical discussion across a wide range of perspectives, in a joined-up, synthesised way.", rewrite: light, force: threshold, status: drafted }
  forBeneficiary: { text: "For an upper second (2:1), at the least, you need to bring theories and debates into critical discussion from a wide range of angles and pull them together into one coherent view.", rewrite: full, force: threshold, status: drafted }
  author-agent-written: "Write about this as the very good level of Table 1, the least a graduate shows for an upper second (2:1) honours degree in Accounting at FHEQ level 6 (FQHEIS level 10): bringing theory into critical discussion of public and organisational issues. Cite it as (QAA, 2025, Accounting Subject Benchmark Statement, para 4.5, Table 1). Do not present it as a regulatory requirement, as a mark scheme or as a level for master's awards. Set it beside qaa/accounting-2025/4.5.b4 and qaa/accounting-2025/4.5.b8, the Annex D band qaa/fheq-2024/annex-d/cognitive/r2/2.1 and the descriptor qaa/fheq-2024/4.15.b7 at spine:6."
  author-agent-dialogue: "Raise it when a student asks what upper second (2:1) work looks like in bringing theory into critical discussion of public and organisational issues, or when markers calibrate between classes. Tell a student plainly what the level asks of them; with staff, treat it as a guide to a class boundary, not a mark scheme. Ask: How did you reconcile two perspectives that pulled in different directions? Never present this level as what is needed simply to pass."
- statement: qaa/accounting-2025/4.5.b7
  forPractitioner: { text: "At the excellent level, graduates have an excellent grasp of accounting's critical, ethical and contextual significance.", rewrite: light, force: threshold, status: drafted }
  forBeneficiary: { text: "For a first, at the least, you need an excellent grasp of why accounting matters ethically, critically and in its wider setting.", rewrite: full, force: threshold, status: drafted }
  author-agent-written: "Write about this as the excellent level of Table 1, the least a graduate shows for a first-class honours degree in Accounting at FHEQ level 6 (FQHEIS level 10): critical, ethical and contextual knowledge. Cite it as (QAA, 2025, Accounting Subject Benchmark Statement, para 4.5, Table 1). Do not present it as a regulatory requirement, as a mark scheme or as a level for master's awards. Set it beside qaa/accounting-2025/4.5.b5, the Annex D band qaa/fheq-2024/annex-d/knowledge/r2/1st and the descriptor qaa/fheq-2024/4.15.b1 at spine:6."
  author-agent-dialogue: "Raise it when a student asks what first-class work looks like in critical, ethical and contextual knowledge, or when markers calibrate between classes. Tell a student plainly what the level asks of them; with staff, treat it as a guide to a class boundary, not a mark scheme. Ask: What would you teach a first-year student about why accounting matters beyond the numbers? Never present this level as what is needed simply to pass."
- statement: qaa/accounting-2025/4.5.b8
  forPractitioner: { text: "At the excellent level, graduates weave theory and debate into critical discussion across a wide range of perspectives with full synthesis.", rewrite: light, force: threshold, status: drafted }
  forBeneficiary: { text: "For a first, at the least, you need to weave theories and debates into critical discussion from a wide range of angles, synthesising them into a well-integrated argument.", rewrite: full, force: threshold, status: drafted }
  author-agent-written: "Write about this as the excellent level of Table 1, the least a graduate shows for a first-class honours degree in Accounting at FHEQ level 6 (FQHEIS level 10): bringing theory into critical discussion of public and organisational issues. Cite it as (QAA, 2025, Accounting Subject Benchmark Statement, para 4.5, Table 1). Do not present it as a regulatory requirement, as a mark scheme or as a level for master's awards. Set it beside qaa/accounting-2025/4.5.b6, the Annex D band qaa/fheq-2024/annex-d/cognitive/r2/1st and the descriptor qaa/fheq-2024/4.15.b7 at spine:6."
  author-agent-dialogue: "Raise it when a student asks what first-class work looks like in bringing theory into critical discussion of public and organisational issues, or when markers calibrate between classes. Tell a student plainly what the level asks of them; with staff, treat it as a guide to a class boundary, not a mark scheme. Ask: Where did your synthesis produce a view that none of your sources held on its own? Never present this level as what is needed simply to pass."
- statement: qaa/accounting-2025/4.5.b9
  forPractitioner: { text: "At threshold, graduates have basic knowledge and understanding of almost all the broad areas in 3.10.", rewrite: light, force: threshold, status: drafted }
  forBeneficiary: { text: "For a third or a pass, at the least, you need a basic knowledge of nearly all the main areas of accounting.", rewrite: full, force: threshold, status: drafted }
  author-agent-written: "Write about this as the threshold level of Table 1, the least a graduate shows for a third-class or pass honours degree in Accounting at FHEQ level 6 (FQHEIS level 10): knowledge across the broad areas. Cite it as (QAA, 2025, Accounting Subject Benchmark Statement, para 4.5, Table 1). Do not present it as a regulatory requirement, as a mark scheme or as a level for master's awards. Set it beside qaa/accounting-2025/4.5.b11, the Annex D band qaa/fheq-2024/annex-d/knowledge/r1/3rd and the descriptor qaa/fheq-2024/4.15.b1 at spine:6."
  author-agent-dialogue: "Raise it when a student asks what third-class or pass work looks like in knowledge across the broad areas, or when markers calibrate between classes. Tell a student plainly what the level asks of them; with staff, treat it as a guide to a class boundary, not a mark scheme. Ask: Which of the broad areas of accounting would you be least confident to explain? Make clear that this is the floor for any honours award, not the target."
- statement: qaa/accounting-2025/4.5.b10
  forPractitioner: { text: "At threshold, graduates show some ability to connect knowledge across the broad areas.", rewrite: light, force: threshold, status: drafted }
  forBeneficiary: { text: "For a third or a pass, at the least, you need to show some ability to connect what you know across the main areas of accounting.", rewrite: full, force: threshold, status: drafted }
  author-agent-written: "Write about this as the threshold level of Table 1, the least a graduate shows for a third-class or pass honours degree in Accounting at FHEQ level 6 (FQHEIS level 10): integrating knowledge across the areas. Cite it as (QAA, 2025, Accounting Subject Benchmark Statement, para 4.5, Table 1). Do not present it as a regulatory requirement, as a mark scheme or as a level for master's awards. Set it beside qaa/accounting-2025/4.5.b12, the Annex D band qaa/fheq-2024/annex-d/knowledge/r2/3rd and the descriptor qaa/fheq-2024/4.15.b3.1 at spine:6."
  author-agent-dialogue: "Raise it when a student asks what third-class or pass work looks like in integrating knowledge across the areas, or when markers calibrate between classes. Tell a student plainly what the level asks of them; with staff, treat it as a guide to a class boundary, not a mark scheme. Ask: Can you link something from audit to something from management accounting? Make clear that this is the floor for any honours award, not the target."
- statement: qaa/accounting-2025/4.5.b11
  forPractitioner: { text: "At the typical level, graduates have solid knowledge of almost all the broad areas and basic understanding of the remainder.", rewrite: light, force: threshold, status: drafted }
  forBeneficiary: { text: "For a lower second (2:2), at the least, you need a solid knowledge of nearly all the main areas of accounting and a basic grasp of the rest.", rewrite: full, force: threshold, status: drafted }
  author-agent-written: "Write about this as the typical level of Table 1, the least a graduate shows for a lower second (2:2) honours degree in Accounting at FHEQ level 6 (FQHEIS level 10): knowledge across the broad areas. Cite it as (QAA, 2025, Accounting Subject Benchmark Statement, para 4.5, Table 1). Do not present it as a regulatory requirement, as a mark scheme or as a level for master's awards. Set it beside qaa/accounting-2025/4.5.b9 and qaa/accounting-2025/4.5.b13, the Annex D band qaa/fheq-2024/annex-d/knowledge/r1/2.2 and the descriptor qaa/fheq-2024/4.15.b1 at spine:6."
  author-agent-dialogue: "Raise it when a student asks what lower second (2:2) work looks like in knowledge across the broad areas, or when markers calibrate between classes. Tell a student plainly what the level asks of them; with staff, treat it as a guide to a class boundary, not a mark scheme. Ask: Which areas feel solid for you, and which only basic? Never present this level as what is needed simply to pass."
- statement: qaa/accounting-2025/4.5.b12
  forPractitioner: { text: "At the typical level, graduates show good integration of knowledge across the broad areas.", rewrite: light, force: threshold, status: drafted }
  forBeneficiary: { text: "For a lower second (2:2), at the least, you need to show that you connect what you know across the main areas of accounting well.", rewrite: full, force: threshold, status: drafted }
  author-agent-written: "Write about this as the typical level of Table 1, the least a graduate shows for a lower second (2:2) honours degree in Accounting at FHEQ level 6 (FQHEIS level 10): integrating knowledge across the areas. Cite it as (QAA, 2025, Accounting Subject Benchmark Statement, para 4.5, Table 1). Do not present it as a regulatory requirement, as a mark scheme or as a level for master's awards. Set it beside qaa/accounting-2025/4.5.b10 and qaa/accounting-2025/4.5.b14, the Annex D band qaa/fheq-2024/annex-d/knowledge/r2/2.2 and the descriptor qaa/fheq-2024/4.15.b3.1 at spine:6."
  author-agent-dialogue: "Raise it when a student asks what lower second (2:2) work looks like in integrating knowledge across the areas, or when markers calibrate between classes. Tell a student plainly what the level asks of them; with staff, treat it as a guide to a class boundary, not a mark scheme. Ask: Where did knowledge from one area change your answer in another? Never present this level as what is needed simply to pass."
- statement: qaa/accounting-2025/4.5.b13
  forPractitioner: { text: "At the very good level, graduates have very good knowledge and critical understanding of almost all broad areas and solid understanding of the rest.", rewrite: light, force: threshold, status: drafted }
  forBeneficiary: { text: "For an upper second (2:1), at the least, you need very good, critical knowledge of nearly all the main areas of accounting and a solid grasp of the rest.", rewrite: full, force: threshold, status: drafted }
  author-agent-written: "Write about this as the very good level of Table 1, the least a graduate shows for an upper second (2:1) honours degree in Accounting at FHEQ level 6 (FQHEIS level 10): knowledge across the broad areas. Cite it as (QAA, 2025, Accounting Subject Benchmark Statement, para 4.5, Table 1). Do not present it as a regulatory requirement, as a mark scheme or as a level for master's awards. Set it beside qaa/accounting-2025/4.5.b11 and qaa/accounting-2025/4.5.b15, the Annex D band qaa/fheq-2024/annex-d/knowledge/r1/2.1 and the descriptor qaa/fheq-2024/4.15.b1 at spine:6."
  author-agent-dialogue: "Raise it when a student asks what upper second (2:1) work looks like in knowledge across the broad areas, or when markers calibrate between classes. Tell a student plainly what the level asks of them; with staff, treat it as a guide to a class boundary, not a mark scheme. Ask: In which area could you criticise the standard approach, not only describe it? Never present this level as what is needed simply to pass."
- statement: qaa/accounting-2025/4.5.b14
  forPractitioner: { text: "At the very good level, graduates show very good integration of knowledge across the broad areas.", rewrite: light, force: threshold, status: drafted }
  forBeneficiary: { text: "For an upper second (2:1), at the least, you need to show that you connect what you know across the main areas of accounting very well.", rewrite: full, force: threshold, status: drafted }
  author-agent-written: "Write about this as the very good level of Table 1, the least a graduate shows for an upper second (2:1) honours degree in Accounting at FHEQ level 6 (FQHEIS level 10): integrating knowledge across the areas. Cite it as (QAA, 2025, Accounting Subject Benchmark Statement, para 4.5, Table 1). Do not present it as a regulatory requirement, as a mark scheme or as a level for master's awards. Set it beside qaa/accounting-2025/4.5.b12 and qaa/accounting-2025/4.5.b16, the Annex D band qaa/fheq-2024/annex-d/knowledge/r2/2.1 and the descriptor qaa/fheq-2024/4.15.b3.1 at spine:6."
  author-agent-dialogue: "Raise it when a student asks what upper second (2:1) work looks like in integrating knowledge across the areas, or when markers calibrate between classes. Tell a student plainly what the level asks of them; with staff, treat it as a guide to a class boundary, not a mark scheme. Ask: How would a tax decision ripple through reporting, audit and risk? Never present this level as what is needed simply to pass."
- statement: qaa/accounting-2025/4.5.b15
  forPractitioner: { text: "At the excellent level, graduates have excellent, advanced critical knowledge of almost all broad areas and very good understanding of the remainder.", rewrite: light, force: threshold, status: drafted }
  forBeneficiary: { text: "For a first, at the least, you need excellent, advanced and critical knowledge of nearly all the main areas of accounting and a very good grasp of the rest.", rewrite: full, force: threshold, status: drafted }
  author-agent-written: "Write about this as the excellent level of Table 1, the least a graduate shows for a first-class honours degree in Accounting at FHEQ level 6 (FQHEIS level 10): knowledge across the broad areas. Cite it as (QAA, 2025, Accounting Subject Benchmark Statement, para 4.5, Table 1). Do not present it as a regulatory requirement, as a mark scheme or as a level for master's awards. Set it beside qaa/accounting-2025/4.5.b13, the Annex D band qaa/fheq-2024/annex-d/knowledge/r1/1st and the descriptor qaa/fheq-2024/4.15.b1 at spine:6."
  author-agent-dialogue: "Raise it when a student asks what first-class work looks like in knowledge across the broad areas, or when markers calibrate between classes. Tell a student plainly what the level asks of them; with staff, treat it as a guide to a class boundary, not a mark scheme. Ask: Which area could you discuss at the level of current research? Never present this level as what is needed simply to pass."
- statement: qaa/accounting-2025/4.5.b16
  forPractitioner: { text: "At the excellent level, graduates integrate knowledge excellently across all the broad areas.", rewrite: light, force: threshold, status: drafted }
  forBeneficiary: { text: "For a first, at the least, you need to show that you connect what you know across all the main areas of accounting excellently.", rewrite: full, force: threshold, status: drafted }
  author-agent-written: "Write about this as the excellent level of Table 1, the least a graduate shows for a first-class honours degree in Accounting at FHEQ level 6 (FQHEIS level 10): integrating knowledge across the areas. Cite it as (QAA, 2025, Accounting Subject Benchmark Statement, para 4.5, Table 1). Do not present it as a regulatory requirement, as a mark scheme or as a level for master's awards. Set it beside qaa/accounting-2025/4.5.b14, the Annex D band qaa/fheq-2024/annex-d/knowledge/r2/1st and the descriptor qaa/fheq-2024/4.15.b3.1 at spine:6."
  author-agent-dialogue: "Raise it when a student asks what first-class work looks like in integrating knowledge across the areas, or when markers calibrate between classes. Tell a student plainly what the level asks of them; with staff, treat it as a guide to a class boundary, not a mark scheme. Ask: Can you build one case that draws on five or more areas at once? Never present this level as what is needed simply to pass."
- statement: qaa/accounting-2025/4.5.b17
  forPractitioner: { text: "At threshold, graduates are adequately proficient in most of the listed skills and use them adequately on straightforward, structured problems.", rewrite: light, force: threshold, status: drafted }
  forBeneficiary: { text: "For a third or a pass, at the least, you need to be reasonably skilled in most of the transferable and professional skills and use them adequately on simple, well-defined problems.", rewrite: full, force: threshold, status: drafted }
  author-agent-written: "Write about this as the threshold level of Table 1, the least a graduate shows for a third-class or pass honours degree in Accounting at FHEQ level 6 (FQHEIS level 10): proficiency in transferable and professional skills. Cite it as (QAA, 2025, Accounting Subject Benchmark Statement, para 4.5, Table 1). Do not present it as a regulatory requirement, as a mark scheme or as a level for master's awards. Set it beside qaa/accounting-2025/4.5.b19, the Annex D band qaa/fheq-2024/annex-d/transferable/r1/3rd and the descriptor qaa/fheq-2024/4.15.b8 and 4.15.b9.2 at spine:6."
  author-agent-dialogue: "Raise it when a student asks what third-class or pass work looks like in proficiency in transferable and professional skills, or when markers calibrate between classes. Tell a student plainly what the level asks of them; with staff, treat it as a guide to a class boundary, not a mark scheme. Ask: Which of the listed skills could you not yet use on your own? Make clear that this is the floor for any honours award, not the target."
- statement: qaa/accounting-2025/4.5.b18
  forPractitioner: { text: "At threshold, graduates show some ability to select, evaluate and synthesise knowledge into valid arguments.", rewrite: light, force: threshold, status: drafted }
  forBeneficiary: { text: "For a third or a pass, at the least, you need to show some ability to choose, weigh up and combine what you know into a sound argument.", rewrite: full, force: threshold, status: drafted }
  author-agent-written: "Write about this as the threshold level of Table 1, the least a graduate shows for a third-class or pass honours degree in Accounting at FHEQ level 6 (FQHEIS level 10): building arguments from knowledge. Cite it as (QAA, 2025, Accounting Subject Benchmark Statement, para 4.5, Table 1). Do not present it as a regulatory requirement, as a mark scheme or as a level for master's awards. Set it beside qaa/accounting-2025/4.5.b20, the Annex D band qaa/fheq-2024/annex-d/cognitive/r2/3rd and the descriptor qaa/fheq-2024/4.15.b7 at spine:6."
  author-agent-dialogue: "Raise it when a student asks what third-class or pass work looks like in building arguments from knowledge, or when markers calibrate between classes. Tell a student plainly what the level asks of them; with staff, treat it as a guide to a class boundary, not a mark scheme. Ask: What makes an argument valid rather than just plausible? Make clear that this is the floor for any honours award, not the target."
- statement: qaa/accounting-2025/4.5.b19
  forPractitioner: { text: "At the typical level, graduates are proficient in almost all the skills and apply them critically and well to moderately complex, partly structured problems.", rewrite: light, force: threshold, status: drafted }
  forBeneficiary: { text: "For a lower second (2:2), at the least, you need good skill in nearly all the transferable and professional skills and use them critically on moderately complex problems that are not fully defined.", rewrite: full, force: threshold, status: drafted }
  author-agent-written: "Write about this as the typical level of Table 1, the least a graduate shows for a lower second (2:2) honours degree in Accounting at FHEQ level 6 (FQHEIS level 10): proficiency in transferable and professional skills. Cite it as (QAA, 2025, Accounting Subject Benchmark Statement, para 4.5, Table 1). Do not present it as a regulatory requirement, as a mark scheme or as a level for master's awards. Set it beside qaa/accounting-2025/4.5.b17 and qaa/accounting-2025/4.5.b21, the Annex D band qaa/fheq-2024/annex-d/transferable/r1/2.2 and the descriptor qaa/fheq-2024/4.15.b8 and 4.15.b9.2 at spine:6."
  author-agent-dialogue: "Raise it when a student asks what lower second (2:2) work looks like in proficiency in transferable and professional skills, or when markers calibrate between classes. Tell a student plainly what the level asks of them; with staff, treat it as a guide to a class boundary, not a mark scheme. Ask: How did you handle a problem whose brief left key details open? Never present this level as what is needed simply to pass."
- statement: qaa/accounting-2025/4.5.b20
  forPractitioner: { text: "At the typical level, graduates show good ability to select, evaluate and synthesise knowledge into strong arguments.", rewrite: light, force: threshold, status: drafted }
  forBeneficiary: { text: "For a lower second (2:2), at the least, you need to show that you can choose, weigh up and combine what you know into strong arguments.", rewrite: full, force: threshold, status: drafted }
  author-agent-written: "Write about this as the typical level of Table 1, the least a graduate shows for a lower second (2:2) honours degree in Accounting at FHEQ level 6 (FQHEIS level 10): building arguments from knowledge. Cite it as (QAA, 2025, Accounting Subject Benchmark Statement, para 4.5, Table 1). Do not present it as a regulatory requirement, as a mark scheme or as a level for master's awards. Set it beside qaa/accounting-2025/4.5.b18 and qaa/accounting-2025/4.5.b22, the Annex D band qaa/fheq-2024/annex-d/cognitive/r2/2.2 and the descriptor qaa/fheq-2024/4.15.b7 at spine:6."
  author-agent-dialogue: "Raise it when a student asks what lower second (2:2) work looks like in building arguments from knowledge, or when markers calibrate between classes. Tell a student plainly what the level asks of them; with staff, treat it as a guide to a class boundary, not a mark scheme. Ask: What would make your last argument stronger? Never present this level as what is needed simply to pass."
- statement: qaa/accounting-2025/4.5.b21
  forPractitioner: { text: "At the very good level, graduates are very proficient in almost all the skills and apply them critically and together to complex, unstructured problems.", rewrite: light, force: threshold, status: drafted }
  forBeneficiary: { text: "For an upper second (2:1), at the least, you need very good skill in nearly all the transferable and professional skills and use them together, critically, on complex problems without a set structure.", rewrite: full, force: threshold, status: drafted }
  author-agent-written: "Write about this as the very good level of Table 1, the least a graduate shows for an upper second (2:1) honours degree in Accounting at FHEQ level 6 (FQHEIS level 10): proficiency in transferable and professional skills. Cite it as (QAA, 2025, Accounting Subject Benchmark Statement, para 4.5, Table 1). Do not present it as a regulatory requirement, as a mark scheme or as a level for master's awards. Set it beside qaa/accounting-2025/4.5.b19 and qaa/accounting-2025/4.5.b23, the Annex D band qaa/fheq-2024/annex-d/transferable/r1/2.1 and the descriptor qaa/fheq-2024/4.15.b8 and 4.15.b9.2 at spine:6."
  author-agent-dialogue: "Raise it when a student asks what upper second (2:1) work looks like in proficiency in transferable and professional skills, or when markers calibrate between classes. Tell a student plainly what the level asks of them; with staff, treat it as a guide to a class boundary, not a mark scheme. Ask: When did you use several skills together to crack a messy problem? Never present this level as what is needed simply to pass."
- statement: qaa/accounting-2025/4.5.b22
  forPractitioner: { text: "At the very good level, graduates select, evaluate and synthesise knowledge very well into strong, creative arguments.", rewrite: light, force: threshold, status: drafted }
  forBeneficiary: { text: "For an upper second (2:1), at the least, you need to show that you can choose, weigh up and combine what you know into strong and original arguments.", rewrite: full, force: threshold, status: drafted }
  author-agent-written: "Write about this as the very good level of Table 1, the least a graduate shows for an upper second (2:1) honours degree in Accounting at FHEQ level 6 (FQHEIS level 10): building arguments from knowledge. Cite it as (QAA, 2025, Accounting Subject Benchmark Statement, para 4.5, Table 1). Do not present it as a regulatory requirement, as a mark scheme or as a level for master's awards. Set it beside qaa/accounting-2025/4.5.b20 and qaa/accounting-2025/4.5.b24, the Annex D band qaa/fheq-2024/annex-d/cognitive/r2/2.1 and the descriptor qaa/fheq-2024/4.15.b7 at spine:6."
  author-agent-dialogue: "Raise it when a student asks what upper second (2:1) work looks like in building arguments from knowledge, or when markers calibrate between classes. Tell a student plainly what the level asks of them; with staff, treat it as a guide to a class boundary, not a mark scheme. Ask: Where did you make an argument that surprised your reader? Never present this level as what is needed simply to pass."
- statement: qaa/accounting-2025/4.5.b23
  forPractitioner: { text: "At the excellent level, graduates are excellently proficient in almost all the skills and apply them critically and together to complex, unstructured and unbounded problems.", rewrite: light, force: threshold, status: drafted }
  forBeneficiary: { text: "For a first, at the least, you need excellent skill in nearly all the transferable and professional skills and use them together, critically, on complex, open-ended problems with no clear edges.", rewrite: full, force: threshold, status: drafted }
  author-agent-written: "Write about this as the excellent level of Table 1, the least a graduate shows for a first-class honours degree in Accounting at FHEQ level 6 (FQHEIS level 10): proficiency in transferable and professional skills. Cite it as (QAA, 2025, Accounting Subject Benchmark Statement, para 4.5, Table 1). Do not present it as a regulatory requirement, as a mark scheme or as a level for master's awards. Set it beside qaa/accounting-2025/4.5.b21, the Annex D band qaa/fheq-2024/annex-d/transferable/r1/1st and the descriptor qaa/fheq-2024/4.15.b8 and 4.15.b9.2 at spine:6."
  author-agent-dialogue: "Raise it when a student asks what first-class work looks like in proficiency in transferable and professional skills, or when markers calibrate between classes. Tell a student plainly what the level asks of them; with staff, treat it as a guide to a class boundary, not a mark scheme. Ask: How did you decide where to draw the boundary of a problem that had none? Never present this level as what is needed simply to pass."
- statement: qaa/accounting-2025/4.5.b24
  forPractitioner: { text: "At the excellent level, graduates select, evaluate and synthesise knowledge excellently into strong, creative arguments.", rewrite: light, force: threshold, status: drafted }
  forBeneficiary: { text: "For a first, at the least, you need to show excellent skill in choosing, weighing up and combining what you know into strong and original arguments.", rewrite: full, force: threshold, status: drafted }
  author-agent-written: "Write about this as the excellent level of Table 1, the least a graduate shows for a first-class honours degree in Accounting at FHEQ level 6 (FQHEIS level 10): building arguments from knowledge. Cite it as (QAA, 2025, Accounting Subject Benchmark Statement, para 4.5, Table 1). Do not present it as a regulatory requirement, as a mark scheme or as a level for master's awards. Set it beside qaa/accounting-2025/4.5.b22, the Annex D band qaa/fheq-2024/annex-d/cognitive/r2/1st and the descriptor qaa/fheq-2024/4.15.b7 at spine:6."
  author-agent-dialogue: "Raise it when a student asks what first-class work looks like in building arguments from knowledge, or when markers calibrate between classes. Tell a student plainly what the level asks of them; with staff, treat it as a guide to a class boundary, not a mark scheme. Ask: What is the most original argument you have made, and how did you test it? Never present this level as what is needed simply to pass."
- statement: qaa/accounting-2025/4.5.b25
  forPractitioner: { text: "At threshold, graduates apply accounting knowledge with a range of skills and critique to straightforward, structured problems across organisation types.", rewrite: light, force: threshold, status: drafted }
  forBeneficiary: { text: "For a third or a pass, at the least, you need to be able to apply what you know about accounting, with some critical thought, to simple, well-defined problems in different kinds of organisation.", rewrite: full, force: threshold, status: drafted }
  author-agent-written: "Write about this as the threshold level of Table 1, the least a graduate shows for a third-class or pass honours degree in Accounting at FHEQ level 6 (FQHEIS level 10): applying accounting to problems in many organisations. Cite it as (QAA, 2025, Accounting Subject Benchmark Statement, para 4.5, Table 1). Do not present it as a regulatory requirement, as a mark scheme or as a level for master's awards. Set it beside qaa/accounting-2025/4.5.b26, the Annex D band qaa/fheq-2024/annex-d/cognitive/r3/3rd and the descriptor qaa/fheq-2024/4.15.b3.1 at spine:6."
  author-agent-dialogue: "Raise it when a student asks what third-class or pass work looks like in applying accounting to problems in many organisations, or when markers calibrate between classes. Tell a student plainly what the level asks of them; with staff, treat it as a guide to a class boundary, not a mark scheme. Ask: Can you solve a standard problem and say what its answer leaves out? Make clear that this is the floor for any honours award, not the target."
- statement: qaa/accounting-2025/4.5.b26
  forPractitioner: { text: "At the typical level, graduates apply accounting knowledge well, drawing on a broad set of skills and critical thought, on moderately complex, partly structured problems.", rewrite: light, force: threshold, status: drafted }
  forBeneficiary: { text: "For a lower second (2:2), at the least, you need to apply what you know about accounting well, with a broad range of skills and critical thought, to moderately complex problems that are not fully defined.", rewrite: full, force: threshold, status: drafted }
  author-agent-written: "Write about this as the typical level of Table 1, the least a graduate shows for a lower second (2:2) honours degree in Accounting at FHEQ level 6 (FQHEIS level 10): applying accounting to problems in many organisations. Cite it as (QAA, 2025, Accounting Subject Benchmark Statement, para 4.5, Table 1). Do not present it as a regulatory requirement, as a mark scheme or as a level for master's awards. Set it beside qaa/accounting-2025/4.5.b25 and qaa/accounting-2025/4.5.b27, the Annex D band qaa/fheq-2024/annex-d/cognitive/r3/2.2 and the descriptor qaa/fheq-2024/4.15.b3.1 at spine:6."
  author-agent-dialogue: "Raise it when a student asks what lower second (2:2) work looks like in applying accounting to problems in many organisations, or when markers calibrate between classes. Tell a student plainly what the level asks of them; with staff, treat it as a guide to a class boundary, not a mark scheme. Ask: What judgement did you have to make where the problem did not tell you what to do? Never present this level as what is needed simply to pass."
- statement: qaa/accounting-2025/4.5.b27
  forPractitioner: { text: "At the very good level, graduates apply accounting knowledge very well, drawing on a wide set of skills and critical thought, on complex, unstructured problems.", rewrite: light, force: threshold, status: drafted }
  forBeneficiary: { text: "For an upper second (2:1), at the least, you need to apply what you know about accounting very well, with a wide range of skills and critical thought, to complex problems without a set structure.", rewrite: full, force: threshold, status: drafted }
  author-agent-written: "Write about this as the very good level of Table 1, the least a graduate shows for an upper second (2:1) honours degree in Accounting at FHEQ level 6 (FQHEIS level 10): applying accounting to problems in many organisations. Cite it as (QAA, 2025, Accounting Subject Benchmark Statement, para 4.5, Table 1). Do not present it as a regulatory requirement, as a mark scheme or as a level for master's awards. Set it beside qaa/accounting-2025/4.5.b26 and qaa/accounting-2025/4.5.b28, the Annex D band qaa/fheq-2024/annex-d/cognitive/r3/2.1 and the descriptor qaa/fheq-2024/4.15.b3.1 at spine:6."
  author-agent-dialogue: "Raise it when a student asks what upper second (2:1) work looks like in applying accounting to problems in many organisations, or when markers calibrate between classes. Tell a student plainly what the level asks of them; with staff, treat it as a guide to a class boundary, not a mark scheme. Ask: How did you structure a complex case before analysing it? Never present this level as what is needed simply to pass."
- statement: qaa/accounting-2025/4.5.b28
  forPractitioner: { text: "At the excellent level, graduates apply accounting knowledge excellently, drawing on a wide set of skills and critical thought, on complex, unstructured and unbounded problems.", rewrite: light, force: threshold, status: drafted }
  forBeneficiary: { text: "For a first, at the least, you need to apply what you know about accounting excellently, with a wide range of skills and critical thought, to complex, open-ended problems.", rewrite: full, force: threshold, status: drafted }
  author-agent-written: "Write about this as the excellent level of Table 1, the least a graduate shows for a first-class honours degree in Accounting at FHEQ level 6 (FQHEIS level 10): applying accounting to problems in many organisations. Cite it as (QAA, 2025, Accounting Subject Benchmark Statement, para 4.5, Table 1). Do not present it as a regulatory requirement, as a mark scheme or as a level for master's awards. Set it beside qaa/accounting-2025/4.5.b27, the Annex D band qaa/fheq-2024/annex-d/cognitive/r3/1st and the descriptor qaa/fheq-2024/4.15.b3.1 at spine:6."
  author-agent-dialogue: "Raise it when a student asks what first-class work looks like in applying accounting to problems in many organisations, or when markers calibrate between classes. Tell a student plainly what the level asks of them; with staff, treat it as a guide to a class boundary, not a mark scheme. Ask: Where did you show judgement on a problem with several defensible answers? Never present this level as what is needed simply to pass."
- statement: qaa/accounting-2025/4.7.b1
  forPractitioner: { text: "Advanced or specialist master's graduates hold specialist and sophisticated knowledge of accounting's critical, ethical and contextual significance.", rewrite: light, force: threshold, status: drafted }
  forBeneficiary: { text: "On an advanced or specialist master's, as a minimum, you need specialist, sophisticated knowledge of why accounting matters ethically, critically and in context.", rewrite: full, force: threshold, status: drafted }
  author-agent-written: "Write about this as the threshold standard for the advanced or specialist master's at FHEQ level 7 (FQHEIS level 11): specialist critical, ethical and contextual knowledge. Cite it as (QAA, 2025, Accounting Subject Benchmark Statement, para 4.7, Table 2). Do not claim it grades merit or distinction, which the statement leaves to institutions, or that it holds for honours or research master's awards. Set it beside qaa/accounting-2025/4.5.b3 and qaa/accounting-2025/4.5.b5, which it builds on, and the master's descriptor qaa/fheq-2024/4.17.b1 at spine:7."
  author-agent-dialogue: "Raise it when a master's student or course team asks what the minimum looks like for specialist critical, ethical and contextual knowledge. Put it in plain words to a student, and to staff as the floor the award type sets. Ask: How does your specialism change the ethical questions accounting raises? Do not read the table cell aloud at length or apply another master's type's column."
- statement: qaa/accounting-2025/4.7.b2
  forPractitioner: { text: "Advanced or specialist master's graduates integrate theory and debate into critical discussion with a high degree of synthesis suited to their specialism.", rewrite: light, force: threshold, status: drafted }
  forBeneficiary: { text: "On an advanced or specialist master's, as a minimum, you need to bring theory and debate into critical discussion of public or organisational issues, pulling perspectives together in a way that suits your specialism.", rewrite: full, force: threshold, status: drafted }
  author-agent-written: "Write about this as the threshold standard for the advanced or specialist master's at FHEQ level 7 (FQHEIS level 11): integrating theory into critical discussion, by specialism. Cite it as (QAA, 2025, Accounting Subject Benchmark Statement, para 4.7, Table 2). Do not claim it grades merit or distinction, which the statement leaves to institutions, or that it holds for honours or research master's awards. Set it beside qaa/accounting-2025/4.5.b4 and qaa/accounting-2025/4.5.b6, which it builds on, and the master's descriptor qaa/fheq-2024/4.17.b5 at spine:7."
  author-agent-dialogue: "Raise it when a master's student or course team asks what the minimum looks like for integrating theory into critical discussion, by specialism. Put it in plain words to a student, and to staff as the floor the award type sets. Ask: Which debate in your specialism is still unresolved, and where do you stand? Do not read the table cell aloud at length or apply another master's type's column."
- statement: qaa/accounting-2025/4.7.b3
  forPractitioner: { text: "Conversion master's graduates hold comprehensive knowledge of accounting's critical, ethical and contextual significance.", rewrite: light, force: threshold, status: drafted }
  forBeneficiary: { text: "On a conversion master's, as a minimum, you need comprehensive knowledge of why accounting matters ethically, critically and in context.", rewrite: full, force: threshold, status: drafted }
  author-agent-written: "Write about this as the threshold standard for the Accounting conversion master's at FHEQ level 7 (FQHEIS level 11): comprehensive critical, ethical and contextual knowledge. Cite it as (QAA, 2025, Accounting Subject Benchmark Statement, para 4.7, Table 2). Do not claim it grades merit or distinction, which the statement leaves to institutions, or that it holds for honours or research master's awards. Set it beside qaa/accounting-2025/4.5.b3 and qaa/accounting-2025/4.5.b5, which it builds on, and the master's descriptor qaa/fheq-2024/4.17.b1 at spine:7."
  author-agent-dialogue: "Raise it when a master's student or course team asks what the minimum looks like for comprehensive critical, ethical and contextual knowledge. Put it in plain words to a student, and to staff as the floor the award type sets. Ask: What did you assume about accounting before the course that you now see differently? Do not read the table cell aloud at length or apply another master's type's column."
- statement: qaa/accounting-2025/4.7.b4
  forPractitioner: { text: "Conversion master's graduates integrate theory and debate into sound critical discussion of public and organisational questions from several perspectives.", rewrite: light, force: threshold, status: drafted }
  forBeneficiary: { text: "On a conversion master's, as a minimum, you need to bring theory and debate into a sound critical discussion of public and organisational questions from several angles.", rewrite: full, force: threshold, status: drafted }
  author-agent-written: "Write about this as the threshold standard for the Accounting conversion master's at FHEQ level 7 (FQHEIS level 11): integrating theory into sound critical discussion. Cite it as (QAA, 2025, Accounting Subject Benchmark Statement, para 4.7, Table 2). Do not claim it grades merit or distinction, which the statement leaves to institutions, or that it holds for honours or research master's awards. Set it beside qaa/accounting-2025/4.5.b4 and qaa/accounting-2025/4.5.b6, which it builds on, and the master's descriptor qaa/fheq-2024/4.17.b5 at spine:7."
  author-agent-dialogue: "Raise it when a master's student or course team asks what the minimum looks like for integrating theory into sound critical discussion. Put it in plain words to a student, and to staff as the floor the award type sets. Ask: Which perspective from your first discipline helps you criticise accounting? Do not read the table cell aloud at length or apply another master's type's column."
- statement: qaa/accounting-2025/4.7.b5
  forPractitioner: { text: "Professional master's graduates hold comprehensive knowledge of accounting's critical, ethical and contextual significance, especially as practised.", rewrite: light, force: threshold, status: drafted }
  forBeneficiary: { text: "On a professional master's, as a minimum, you need comprehensive knowledge of why accounting matters ethically, critically and in context, especially in professional practice.", rewrite: full, force: threshold, status: drafted }
  author-agent-written: "Write about this as the threshold standard for the professional master's at FHEQ level 7 (FQHEIS level 11): comprehensive knowledge, as applied in practice. Cite it as (QAA, 2025, Accounting Subject Benchmark Statement, para 4.7, Table 2). Do not claim it grades merit or distinction, which the statement leaves to institutions, or that it holds for honours or research master's awards. Set it beside qaa/accounting-2025/4.5.b3 and qaa/accounting-2025/4.5.b5, which it builds on, and the master's descriptor qaa/fheq-2024/4.17.b1 at spine:7."
  author-agent-dialogue: "Raise it when a master's student or course team asks what the minimum looks like for comprehensive knowledge, as applied in practice. Put it in plain words to a student, and to staff as the floor the award type sets. Ask: Where in practice have you seen an ethical judgement that the rules did not settle? Do not read the table cell aloud at length or apply another master's type's column."
- statement: qaa/accounting-2025/4.7.b6
  forPractitioner: { text: "Professional master's graduates integrate theory and debate into critical, synthesised discussion of professional and organisational practice.", rewrite: light, force: threshold, status: drafted }
  forBeneficiary: { text: "On a professional master's, as a minimum, you need to bring theory and debate into a critical, joined-up discussion of professional and organisational practice.", rewrite: full, force: threshold, status: drafted }
  author-agent-written: "Write about this as the threshold standard for the professional master's at FHEQ level 7 (FQHEIS level 11): integrating theory into discussion of professional practice. Cite it as (QAA, 2025, Accounting Subject Benchmark Statement, para 4.7, Table 2). Do not claim it grades merit or distinction, which the statement leaves to institutions, or that it holds for honours or research master's awards. Set it beside qaa/accounting-2025/4.5.b4 and qaa/accounting-2025/4.5.b6, which it builds on, and the master's descriptor qaa/fheq-2024/4.17.b5 at spine:7."
  author-agent-dialogue: "Raise it when a master's student or course team asks what the minimum looks like for integrating theory into discussion of professional practice. Put it in plain words to a student, and to staff as the floor the award type sets. Ask: Which theory best explains a practice you have seen at work? Do not read the table cell aloud at length or apply another master's type's column."
- statement: qaa/accounting-2025/4.7.b7
  forPractitioner: { text: "Integrated master's graduates reach the typical or very good honours standard and then the advanced or specialist (or professional) master's standard set out in Table 2.", rewrite: light, force: threshold, status: drafted }
  forBeneficiary: { text: "On an integrated master's, as a minimum, you need to reach at least a lower or upper second honours level and then the level of an advanced, specialist or professional master's.", rewrite: full, force: threshold, status: drafted }
  author-agent-written: "Write about this as the threshold standard for the integrated master's at FHEQ level 7 (FQHEIS level 11): honours standards plus master's standards, combined. Cite it as (QAA, 2025, Accounting Subject Benchmark Statement, para 4.7, Table 2). Do not claim it grades merit or distinction, which the statement leaves to institutions, or that it holds for honours or research master's awards. Set it beside qaa/accounting-2025/4.5.b3 and qaa/accounting-2025/4.5.b5, which it builds on, and the master's descriptor qaa/fheq-2024/4.15.b1 and 4.17.b1 at spine:7."
  author-agent-dialogue: "Raise it when a master's student or course team asks what the minimum looks like for honours standards plus master's standards, combined. Put it in plain words to a student, and to staff as the floor the award type sets. Ask: Which master's type does your final year most resemble, and does your work reach its level? Do not read the table cell aloud at length or apply another master's type's column."
- statement: qaa/accounting-2025/4.7.b8
  forPractitioner: { text: "Advanced or specialist master's graduates hold advanced, critical knowledge across many broad areas or in depth in a subset, perhaps with another subject.", rewrite: light, force: threshold, status: drafted }
  forBeneficiary: { text: "On an advanced or specialist master's, as a minimum, you need specialist, advanced and critical knowledge, either across many areas of accounting or in real depth in a few.", rewrite: full, force: threshold, status: drafted }
  author-agent-written: "Write about this as the threshold standard for the advanced or specialist master's at FHEQ level 7 (FQHEIS level 11): specialist knowledge across or within the broad areas. Cite it as (QAA, 2025, Accounting Subject Benchmark Statement, para 4.7, Table 2). Do not claim it grades merit or distinction, which the statement leaves to institutions, or that it holds for honours or research master's awards. Set it beside qaa/accounting-2025/4.5.b11 and qaa/accounting-2025/4.5.b13, which it builds on, and the master's descriptor qaa/fheq-2024/4.17.b1 at spine:7."
  author-agent-dialogue: "Raise it when a master's student or course team asks what the minimum looks like for specialist knowledge across or within the broad areas. Put it in plain words to a student, and to staff as the floor the award type sets. Ask: Is your master's broad or deep, and how would an employer see that? Do not read the table cell aloud at length or apply another master's type's column."
- statement: qaa/accounting-2025/4.7.b9
  forPractitioner: { text: "Advanced or specialist master's graduates integrate knowledge across their areas of study with insight and sophistication.", rewrite: light, force: threshold, status: drafted }
  forBeneficiary: { text: "On an advanced or specialist master's, as a minimum, you need to connect what you know across your areas of study in an informed, insightful and sophisticated way.", rewrite: full, force: threshold, status: drafted }
  author-agent-written: "Write about this as the threshold standard for the advanced or specialist master's at FHEQ level 7 (FQHEIS level 11): sophisticated integration across the areas studied. Cite it as (QAA, 2025, Accounting Subject Benchmark Statement, para 4.7, Table 2). Do not claim it grades merit or distinction, which the statement leaves to institutions, or that it holds for honours or research master's awards. Set it beside qaa/accounting-2025/4.5.b12 and qaa/accounting-2025/4.5.b14, which it builds on, and the master's descriptor qaa/fheq-2024/4.17.b3 at spine:7."
  author-agent-dialogue: "Raise it when a master's student or course team asks what the minimum looks like for sophisticated integration across the areas studied. Put it in plain words to a student, and to staff as the floor the award type sets. Ask: Where did connecting two of your areas give you an insight neither gave alone? Do not read the table cell aloud at length or apply another master's type's column."
- statement: qaa/accounting-2025/4.7.b10
  forPractitioner: { text: "Conversion master's graduates hold comprehensive knowledge of almost all broad areas and basic understanding of the remainder.", rewrite: light, force: threshold, status: drafted }
  forBeneficiary: { text: "On a conversion master's, as a minimum, you need comprehensive knowledge of nearly all the main areas of accounting and a basic grasp of the rest.", rewrite: full, force: threshold, status: drafted }
  author-agent-written: "Write about this as the threshold standard for the Accounting conversion master's at FHEQ level 7 (FQHEIS level 11): comprehensive knowledge of the broad areas. Cite it as (QAA, 2025, Accounting Subject Benchmark Statement, para 4.7, Table 2). Do not claim it grades merit or distinction, which the statement leaves to institutions, or that it holds for honours or research master's awards. Set it beside qaa/accounting-2025/4.5.b11 and qaa/accounting-2025/4.5.b13, which it builds on, and the master's descriptor qaa/fheq-2024/4.17.b1 at spine:7."
  author-agent-dialogue: "Raise it when a master's student or course team asks what the minimum looks like for comprehensive knowledge of the broad areas. Put it in plain words to a student, and to staff as the floor the award type sets. Ask: Which of the broad areas would you most want more time on? Do not read the table cell aloud at length or apply another master's type's column."
- statement: qaa/accounting-2025/4.7.b11
  forPractitioner: { text: "Conversion master's graduates integrate knowledge across the broad areas with insight.", rewrite: light, force: threshold, status: drafted }
  forBeneficiary: { text: "On a conversion master's, as a minimum, you need to connect what you know across the main areas of accounting in an informed, insightful way.", rewrite: full, force: threshold, status: drafted }
  author-agent-written: "Write about this as the threshold standard for the Accounting conversion master's at FHEQ level 7 (FQHEIS level 11): insightful integration across the broad areas. Cite it as (QAA, 2025, Accounting Subject Benchmark Statement, para 4.7, Table 2). Do not claim it grades merit or distinction, which the statement leaves to institutions, or that it holds for honours or research master's awards. Set it beside qaa/accounting-2025/4.5.b12 and qaa/accounting-2025/4.5.b14, which it builds on, and the master's descriptor qaa/fheq-2024/4.17.b3 at spine:7."
  author-agent-dialogue: "Raise it when a master's student or course team asks what the minimum looks like for insightful integration across the broad areas. Put it in plain words to a student, and to staff as the floor the award type sets. Ask: How does a decision in one area of accounting show up in another? Do not read the table cell aloud at length or apply another master's type's column."
- statement: qaa/accounting-2025/4.7.b12
  forPractitioner: { text: "Professional master's graduates hold comprehensive, advanced critical knowledge of almost all broad areas and solid understanding of the rest.", rewrite: light, force: threshold, status: drafted }
  forBeneficiary: { text: "On a professional master's, as a minimum, you need comprehensive, advanced and critical knowledge of nearly all the main areas of accounting and a solid grasp of the rest.", rewrite: full, force: threshold, status: drafted }
  author-agent-written: "Write about this as the threshold standard for the professional master's at FHEQ level 7 (FQHEIS level 11): comprehensive, advanced knowledge of the broad areas. Cite it as (QAA, 2025, Accounting Subject Benchmark Statement, para 4.7, Table 2). Do not claim it grades merit or distinction, which the statement leaves to institutions, or that it holds for honours or research master's awards. Set it beside qaa/accounting-2025/4.5.b11 and qaa/accounting-2025/4.5.b13, which it builds on, and the master's descriptor qaa/fheq-2024/4.17.b1 at spine:7."
  author-agent-dialogue: "Raise it when a master's student or course team asks what the minimum looks like for comprehensive, advanced knowledge of the broad areas. Put it in plain words to a student, and to staff as the floor the award type sets. Ask: Where would your knowledge be tested hardest in a professional examination? Do not read the table cell aloud at length or apply another master's type's column."
- statement: qaa/accounting-2025/4.7.b13
  forPractitioner: { text: "Professional master's graduates integrate knowledge across the broad areas with insight, particularly for professional and organisational practice.", rewrite: light, force: threshold, status: drafted }
  forBeneficiary: { text: "On a professional master's, as a minimum, you need to connect what you know across the main areas of accounting with insight, especially in professional practice.", rewrite: full, force: threshold, status: drafted }
  author-agent-written: "Write about this as the threshold standard for the professional master's at FHEQ level 7 (FQHEIS level 11): integration across the areas for professional practice. Cite it as (QAA, 2025, Accounting Subject Benchmark Statement, para 4.7, Table 2). Do not claim it grades merit or distinction, which the statement leaves to institutions, or that it holds for honours or research master's awards. Set it beside qaa/accounting-2025/4.5.b12 and qaa/accounting-2025/4.5.b14, which it builds on, and the master's descriptor qaa/fheq-2024/4.17.b3 at spine:7."
  author-agent-dialogue: "Raise it when a master's student or course team asks what the minimum looks like for integration across the areas for professional practice. Put it in plain words to a student, and to staff as the floor the award type sets. Ask: Which client problem would draw on several areas of accounting at once? Do not read the table cell aloud at length or apply another master's type's column."
- statement: qaa/accounting-2025/4.7.b14
  forPractitioner: { text: "Advanced or specialist master's graduates apply nearly all the skills very well, critically and together, to complex, unstructured and unbounded problems.", rewrite: light, force: threshold, status: drafted }
  forBeneficiary: { text: "On an advanced or specialist master's, as a minimum, you need very good skill in nearly all the transferable and professional skills, used together and critically on complex, open-ended problems.", rewrite: full, force: threshold, status: drafted }
  author-agent-written: "Write about this as the threshold standard for the advanced or specialist master's at FHEQ level 7 (FQHEIS level 11): proficiency in transferable and professional skills. Cite it as (QAA, 2025, Accounting Subject Benchmark Statement, para 4.7, Table 2). Do not claim it grades merit or distinction, which the statement leaves to institutions, or that it holds for honours or research master's awards. Set it beside qaa/accounting-2025/4.5.b19 and qaa/accounting-2025/4.5.b21, which it builds on, and the master's descriptor qaa/fheq-2024/4.17.b5 and 4.17.b8.2 at spine:7."
  author-agent-dialogue: "Raise it when a master's student or course team asks what the minimum looks like for proficiency in transferable and professional skills. Put it in plain words to a student, and to staff as the floor the award type sets. Ask: Which open-ended problem in your specialism have you tackled from scratch? Do not read the table cell aloud at length or apply another master's type's column."
- statement: qaa/accounting-2025/4.7.b15
  forPractitioner: { text: "Advanced or specialist master's graduates select, evaluate and synthesise specialised, advanced knowledge into strong, creative arguments.", rewrite: light, force: threshold, status: drafted }
  forBeneficiary: { text: "On an advanced or specialist master's, as a minimum, you need to choose, weigh up and combine specialised, advanced knowledge into strong and original arguments.", rewrite: full, force: threshold, status: drafted }
  author-agent-written: "Write about this as the threshold standard for the advanced or specialist master's at FHEQ level 7 (FQHEIS level 11): arguments from specialised, advanced knowledge. Cite it as (QAA, 2025, Accounting Subject Benchmark Statement, para 4.7, Table 2). Do not claim it grades merit or distinction, which the statement leaves to institutions, or that it holds for honours or research master's awards. Set it beside qaa/accounting-2025/4.5.b20 and qaa/accounting-2025/4.5.b22, which it builds on, and the master's descriptor qaa/fheq-2024/4.17.b4.1 at spine:7."
  author-agent-dialogue: "Raise it when a master's student or course team asks what the minimum looks like for arguments from specialised, advanced knowledge. Put it in plain words to a student, and to staff as the floor the award type sets. Ask: What is the strongest original argument in your dissertation plan? Do not read the table cell aloud at length or apply another master's type's column."
- statement: qaa/accounting-2025/4.7.b16
  forPractitioner: { text: "Conversion master's graduates apply nearly all the skills very well and critically to moderately complex, unstructured problems.", rewrite: light, force: threshold, status: drafted }
  forBeneficiary: { text: "On a conversion master's, as a minimum, you need very good skill in nearly all the transferable and professional skills, used critically on moderately complex problems without a set structure.", rewrite: full, force: threshold, status: drafted }
  author-agent-written: "Write about this as the threshold standard for the Accounting conversion master's at FHEQ level 7 (FQHEIS level 11): proficiency in transferable and professional skills. Cite it as (QAA, 2025, Accounting Subject Benchmark Statement, para 4.7, Table 2). Do not claim it grades merit or distinction, which the statement leaves to institutions, or that it holds for honours or research master's awards. Set it beside qaa/accounting-2025/4.5.b19 and qaa/accounting-2025/4.5.b21, which it builds on, and the master's descriptor qaa/fheq-2024/4.17.b5 and 4.17.b8.2 at spine:7."
  author-agent-dialogue: "Raise it when a master's student or course team asks what the minimum looks like for proficiency in transferable and professional skills. Put it in plain words to a student, and to staff as the floor the award type sets. Ask: Which skill from your earlier degree has carried over best into accounting? Do not read the table cell aloud at length or apply another master's type's column."
- statement: qaa/accounting-2025/4.7.b17
  forPractitioner: { text: "Conversion master's graduates select, evaluate and synthesise knowledge into strong arguments.", rewrite: light, force: threshold, status: drafted }
  forBeneficiary: { text: "On a conversion master's, as a minimum, you need to choose, weigh up and combine what you know into strong arguments.", rewrite: full, force: threshold, status: drafted }
  author-agent-written: "Write about this as the threshold standard for the Accounting conversion master's at FHEQ level 7 (FQHEIS level 11): building strong arguments. Cite it as (QAA, 2025, Accounting Subject Benchmark Statement, para 4.7, Table 2). Do not claim it grades merit or distinction, which the statement leaves to institutions, or that it holds for honours or research master's awards. Set it beside qaa/accounting-2025/4.5.b20 and qaa/accounting-2025/4.5.b22, which it builds on, and the master's descriptor qaa/fheq-2024/4.17.b4.1 at spine:7."
  author-agent-dialogue: "Raise it when a master's student or course team asks what the minimum looks like for building strong arguments. Put it in plain words to a student, and to staff as the floor the award type sets. Ask: How do you decide which evidence to leave out of an argument? Do not read the table cell aloud at length or apply another master's type's column."
- statement: qaa/accounting-2025/4.7.b18
  forPractitioner: { text: "Professional master's graduates apply nearly all the skills very well, critically and together, to complex, unstructured problems, typically practice-based.", rewrite: light, force: threshold, status: drafted }
  forBeneficiary: { text: "On a professional master's, as a minimum, you need very good skill in nearly all the transferable and professional skills, used together and critically on complex practical problems.", rewrite: full, force: threshold, status: drafted }
  author-agent-written: "Write about this as the threshold standard for the professional master's at FHEQ level 7 (FQHEIS level 11): proficiency in skills, with a practice emphasis. Cite it as (QAA, 2025, Accounting Subject Benchmark Statement, para 4.7, Table 2). Do not claim it grades merit or distinction, which the statement leaves to institutions, or that it holds for honours or research master's awards. Set it beside qaa/accounting-2025/4.5.b19 and qaa/accounting-2025/4.5.b21, which it builds on, and the master's descriptor qaa/fheq-2024/4.17.b5 and 4.17.b8.2 at spine:7."
  author-agent-dialogue: "Raise it when a master's student or course team asks what the minimum looks like for proficiency in skills, with a practice emphasis. Put it in plain words to a student, and to staff as the floor the award type sets. Ask: Which practical problem from work tested your skills most? Do not read the table cell aloud at length or apply another master's type's column."
- statement: qaa/accounting-2025/4.7.b19
  forPractitioner: { text: "Professional master's graduates select, evaluate and synthesise knowledge into strong, creative arguments about professional and organisational practice.", rewrite: light, force: threshold, status: drafted }
  forBeneficiary: { text: "On a professional master's, as a minimum, you need to choose, weigh up and combine what you know into strong and original arguments about professional practice.", rewrite: full, force: threshold, status: drafted }
  author-agent-written: "Write about this as the threshold standard for the professional master's at FHEQ level 7 (FQHEIS level 11): arguments for professional practice. Cite it as (QAA, 2025, Accounting Subject Benchmark Statement, para 4.7, Table 2). Do not claim it grades merit or distinction, which the statement leaves to institutions, or that it holds for honours or research master's awards. Set it beside qaa/accounting-2025/4.5.b20 and qaa/accounting-2025/4.5.b22, which it builds on, and the master's descriptor qaa/fheq-2024/4.17.b4.1 at spine:7."
  author-agent-dialogue: "Raise it when a master's student or course team asks what the minimum looks like for arguments for professional practice. Put it in plain words to a student, and to staff as the floor the award type sets. Ask: How would you persuade a sceptical partner to change a firm's practice? Do not read the table cell aloud at length or apply another master's type's column."
- statement: qaa/accounting-2025/4.7.b20
  forPractitioner: { text: "Integrated master's graduates reach the typical or very good honours skills standard and then the advanced or specialist (or professional) master's standard.", rewrite: light, force: threshold, status: drafted }
  forBeneficiary: { text: "On an integrated master's, as a minimum, your skills need to reach at least a lower or upper second honours level and then the level of an advanced, specialist or professional master's.", rewrite: full, force: threshold, status: drafted }
  author-agent-written: "Write about this as the threshold standard for the integrated master's at FHEQ level 7 (FQHEIS level 11): honours skills plus master's skills, combined. Cite it as (QAA, 2025, Accounting Subject Benchmark Statement, para 4.7, Table 2). Do not claim it grades merit or distinction, which the statement leaves to institutions, or that it holds for honours or research master's awards. Set it beside qaa/accounting-2025/4.5.b19 and qaa/accounting-2025/4.5.b21, which it builds on, and the master's descriptor qaa/fheq-2024/4.15.b9.2 and 4.17.b6 at spine:7."
  author-agent-dialogue: "Raise it when a master's student or course team asks what the minimum looks like for honours skills plus master's skills, combined. Put it in plain words to a student, and to staff as the floor the award type sets. Ask: Which skill has grown most between your honours years and your master's year? Do not read the table cell aloud at length or apply another master's type's column."
- statement: qaa/accounting-2025/4.7.b21
  forPractitioner: { text: "Advanced or specialist master's graduates apply specialised, advanced knowledge with sophistication to complex, unstructured and unbounded problems, as the degree's focus requires.", rewrite: light, force: threshold, status: drafted }
  forBeneficiary: { text: "On an advanced or specialist master's, as a minimum, you need to apply specialised, advanced knowledge with insight and a wide range of skills to complex, open-ended problems in different organisations.", rewrite: full, force: threshold, status: drafted }
  author-agent-written: "Write about this as the threshold standard for the advanced or specialist master's at FHEQ level 7 (FQHEIS level 11): sophisticated application to open-ended problems. Cite it as (QAA, 2025, Accounting Subject Benchmark Statement, para 4.7, Table 2). Do not claim it grades merit or distinction, which the statement leaves to institutions, or that it holds for honours or research master's awards. Set it beside qaa/accounting-2025/4.5.b26 and qaa/accounting-2025/4.5.b27, which it builds on, and the master's descriptor qaa/fheq-2024/4.17.b3 at spine:7."
  author-agent-dialogue: "Raise it when a master's student or course team asks what the minimum looks like for sophisticated application to open-ended problems. Put it in plain words to a student, and to staff as the floor the award type sets. Ask: Where has your specialist knowledge solved a problem that general knowledge could not? Do not read the table cell aloud at length or apply another master's type's column."
- statement: qaa/accounting-2025/4.7.b22
  forPractitioner: { text: "Conversion master's graduates apply accounting knowledge with insight and a broad range of skills to moderately complex, unstructured problems.", rewrite: light, force: threshold, status: drafted }
  forBeneficiary: { text: "On a conversion master's, as a minimum, you need to apply what you know about accounting with insight and a broad range of skills to moderately complex problems without a set structure.", rewrite: full, force: threshold, status: drafted }
  author-agent-written: "Write about this as the threshold standard for the Accounting conversion master's at FHEQ level 7 (FQHEIS level 11): informed application to moderately complex problems. Cite it as (QAA, 2025, Accounting Subject Benchmark Statement, para 4.7, Table 2). Do not claim it grades merit or distinction, which the statement leaves to institutions, or that it holds for honours or research master's awards. Set it beside qaa/accounting-2025/4.5.b26 and qaa/accounting-2025/4.5.b27, which it builds on, and the master's descriptor qaa/fheq-2024/4.17.b3 at spine:7."
  author-agent-dialogue: "Raise it when a master's student or course team asks what the minimum looks like for informed application to moderately complex problems. Put it in plain words to a student, and to staff as the floor the award type sets. Ask: Which kind of organisation's accounting problem do you now feel able to tackle? Do not read the table cell aloud at length or apply another master's type's column."
- statement: qaa/accounting-2025/4.7.b23
  forPractitioner: { text: "Professional master's graduates apply accounting knowledge with insight and a wide range of skills to complex, unstructured problems, particularly practical and professional ones.", rewrite: light, force: threshold, status: drafted }
  forBeneficiary: { text: "On a professional master's, as a minimum, you need to apply what you know about accounting with insight and a wide range of skills to complex practical and professional problems.", rewrite: full, force: threshold, status: drafted }
  author-agent-written: "Write about this as the threshold standard for the professional master's at FHEQ level 7 (FQHEIS level 11): informed application to practical, professional problems. Cite it as (QAA, 2025, Accounting Subject Benchmark Statement, para 4.7, Table 2). Do not claim it grades merit or distinction, which the statement leaves to institutions, or that it holds for honours or research master's awards. Set it beside qaa/accounting-2025/4.5.b26 and qaa/accounting-2025/4.5.b27, which it builds on, and the master's descriptor qaa/fheq-2024/4.17.b3 at spine:7."
  author-agent-dialogue: "Raise it when a master's student or course team asks what the minimum looks like for informed application to practical, professional problems. Put it in plain words to a student, and to staff as the floor the award type sets. Ask: Which professional problem would you choose to show this to an employer? Do not read the table cell aloud at length or apply another master's type's column."
- statement: qaa/accounting-2025/4.7.b24
  forPractitioner: { text: "Advanced or specialist master's graduates give convincing evidence of a substantial, self-directed, advanced research study in their specialism, theoretical or applied.", rewrite: light, force: threshold, status: drafted }
  forBeneficiary: { text: "On an advanced or specialist master's, as a minimum, you need to show convincingly that you have completed a substantial research inquiry of your own, at an advanced level in your specialism.", rewrite: full, force: threshold, status: drafted }
  author-agent-written: "Write about this as the threshold standard for the advanced or specialist master's at FHEQ level 7 (FQHEIS level 11): the self-directed research project, specialist. Cite it as (QAA, 2025, Accounting Subject Benchmark Statement, para 4.7, Table 2). Do not claim it grades merit or distinction, which the statement leaves to institutions, or that it holds for honours or research master's awards. Set it beside qaa/accounting-2025/1.17 and qaa/accounting-2025/3.15.b12, which it builds on, and the master's descriptor qaa/fheq-2024/4.17.b2 and 4.17.b6 at spine:7."
  author-agent-dialogue: "Raise it when a master's student or course team asks what the minimum looks like for the self-directed research project, specialist. Put it in plain words to a student, and to staff as the floor the award type sets. Ask: What makes your research question worth a substantial study? Do not read the table cell aloud at length or apply another master's type's column."
- statement: qaa/accounting-2025/4.7.b25
  forPractitioner: { text: "Conversion master's graduates give convincing evidence of a substantial, self-directed research study, theoretical or applied.", rewrite: light, force: threshold, status: drafted }
  forBeneficiary: { text: "On a conversion master's, as a minimum, you need to show convincingly that you have completed a substantial research inquiry of your own, into theory or a real issue.", rewrite: full, force: threshold, status: drafted }
  author-agent-written: "Write about this as the threshold standard for the Accounting conversion master's at FHEQ level 7 (FQHEIS level 11): the self-directed research project. Cite it as (QAA, 2025, Accounting Subject Benchmark Statement, para 4.7, Table 2). Do not claim it grades merit or distinction, which the statement leaves to institutions, or that it holds for honours or research master's awards. Set it beside qaa/accounting-2025/1.17 and qaa/accounting-2025/3.15.b12, which it builds on, and the master's descriptor qaa/fheq-2024/4.17.b2 and 4.17.b6 at spine:7."
  author-agent-dialogue: "Raise it when a master's student or course team asks what the minimum looks like for the self-directed research project. Put it in plain words to a student, and to staff as the floor the award type sets. Ask: How will your inquiry bring together your earlier discipline and accounting? Do not read the table cell aloud at length or apply another master's type's column."
- statement: qaa/accounting-2025/4.7.b26
  forPractitioner: { text: "Professional master's graduates give convincing evidence of a substantial, self-directed study that applies knowledge to a practical project, often work-based.", rewrite: light, force: threshold, status: drafted }
  forBeneficiary: { text: "On a professional master's, as a minimum, you need to show convincingly that you have completed a substantial study of your own that applies what you know to a real, practical project.", rewrite: full, force: threshold, status: drafted }
  author-agent-written: "Write about this as the threshold standard for the professional master's at FHEQ level 7 (FQHEIS level 11): the self-directed project, applied to practice. Cite it as (QAA, 2025, Accounting Subject Benchmark Statement, para 4.7, Table 2). Do not claim it grades merit or distinction, which the statement leaves to institutions, or that it holds for honours or research master's awards. Set it beside qaa/accounting-2025/1.17 and qaa/accounting-2025/3.15.b12, which it builds on, and the master's descriptor qaa/fheq-2024/4.17.b2 and 4.17.b6 at spine:7."
  author-agent-dialogue: "Raise it when a master's student or course team asks what the minimum looks like for the self-directed project, applied to practice. Put it in plain words to a student, and to staff as the floor the award type sets. Ask: Which workplace issue would make the best practical project? Do not read the table cell aloud at length or apply another master's type's column."
- statement: qaa/accounting-2025/4.7.b27
  forPractitioner: { text: "Integrated master's graduates give convincing evidence of a substantial, self-directed study suited to the degree.", rewrite: light, force: threshold, status: drafted }
  forBeneficiary: { text: "On an integrated master's, as a minimum, you need to show convincingly that you have completed a substantial study of your own, suited to your integrated master's.", rewrite: full, force: threshold, status: drafted }
  author-agent-written: "Write about this as the threshold standard for the integrated master's at FHEQ level 7 (FQHEIS level 11): the self-directed study in an integrated master's. Cite it as (QAA, 2025, Accounting Subject Benchmark Statement, para 4.7, Table 2). Do not claim it grades merit or distinction, which the statement leaves to institutions, or that it holds for honours or research master's awards. Set it beside qaa/accounting-2025/1.17 and qaa/accounting-2025/3.15.b12, which it builds on, and the master's descriptor qaa/fheq-2024/4.17.b2 and 4.17.b6 at spine:7."
  author-agent-dialogue: "Raise it when a master's student or course team asks what the minimum looks like for the self-directed study in an integrated master's. Put it in plain words to a student, and to staff as the floor the award type sets. Ask: How does your final-year study go beyond your honours dissertation or project? Do not read the table cell aloud at length or apply another master's type's column."
```

### S5 Levels and alignment
<!-- label: both; status: drafted; basis: primary -->
```yaml
levels:
  - { id: "fheq:6", role: "cites", locator: "D1, 2.7; 2.14; Table 1 (honours)" }
  - { id: "fqheis:10", role: "cites", locator: "D1, 2.7; 2.14" }
  - { id: "fheq:7", role: "cites", locator: "D1, 2.7; 2.13 (integrated master's); Table 2 read as master's (inferred for the taught master's types)" }
  - { id: "fqheis:11", role: "cites", locator: "D1, 2.7; 2.13" }
crosswalks:
  - { from: "fheq:6", to: "fqheis:10", relation: "equivalent", basis: "stated (D1, 2.7; 2.14: honours at FHEQ Level 6, FQHEIS Level 10)" }
  - { from: "fheq:7", to: "fqheis:11", relation: "equivalent", basis: "stated (D1, 2.7; 2.13: integrated master's at FHEQ Level 7, FQHEIS Level 11)" }
  - { from: "Table 1 levels", to: "Annex D classes", relation: "thresholdAt", basis: "stated (D1, 4.3: threshold = 3rd or pass, typical = 2:2, very good = 2:1, excellent = 1st)" }
```

### S6 Themes
<!-- label: both; status: drafted; basis: primary -->
```yaml
- { id: "theme:edi", role: "carries", carriedIn: ["front matter", "1.19", "1.20", "1.21", "1.22", "1.23", "1.24", "1.25", "1.26", "1.27", "1.28", "1.38", "2.1", "2.20", "2.24", "2.30", "2.31", "3.10", "3.15", "3.23", "3.29", "3.33", "3.41"] }
- { id: "theme:accessibility", role: "carries", carriedIn: ["front matter", "1.29", "1.30", "1.31", "1.32", "2.1", "2.19", "2.31", "3.23", "3.33"] }
- { id: "theme:esd", role: "carries", carriedIn: ["front matter", "1.1", "1.2", "1.3", "1.4", "1.11", "1.13", "1.14", "1.16", "1.21", "1.33", "1.34", "1.35", "1.36", "1.38", "1.39", "1.40", "1.41", "1.42", "1.43", "2.1", "2.6", "2.24", "2.31", "3.4", "3.8", "3.10", "3.15", "4.5", "4.8"] }
- { id: "theme:enterprise", role: "carries", carriedIn: ["front matter", "1.38", "1.44", "1.45", "1.46", "1.47", "1.48", "2.4", "2.31", "3.15"] }
- { id: "theme:genai", role: "carries", carriedIn: ["front matter", "1.12", "1.23", "1.49", "1.50", "1.51", "1.52", "1.53", "1.54", "1.55", "2.2", "2.31", "3.10", "3.15", "3.22", "3.34", "3.42", "3.43"] }
```

### S7 Relations
<!-- label: both; status: drafted; basis: primary -->
```yaml
- { rel: "partOf", target: "collection: QAA Subject Benchmark Statements", note: "one of 54 held by stan" }
- { rel: "supersedes", target: "std:doc:qaa-accounting-2019-benchmarks (not held)", note: "the 2025 statement lists key changes from the previous one; advisory groups are named for 2019 (minor update), 2014, 2007 and 2000 (back matter)" }
- { rel: "refersTo", target: "std:doc:qaa-fheq-2024-framework, Annex D", note: "4.3: the honours levels are informed by Annex D's four classification descriptions; cited as QAA (2024a) in the references" }
- { rel: "refersTo", target: "std:doc:qaa-fheq-2024-framework", note: "levels 6 and 7 (2.7, 2.13, 2.14)" }
- { rel: "refersTo", target: "std:doc:qaa-fqheis-2024-framework", note: "levels 10 and 11 (2.7, 2.13, 2.14)" }
- { rel: "readWith", target: "std:doc:qaa-finance-2025-benchmarks (not yet ingested)", note: "1.2 and 3.10 l: single honours finance and the content of finance topics are in the Finance statement; joint courses draw on both" }
- { rel: "refersTo", target: "QAA Master's Degree Characteristics Statement (not ingested)", note: "4.6: the master's standards are informed by it" }
- { rel: "refersTo", target: "QAA Quality Code (2024), Advice and Guidance: Partnerships (not ingested)", note: "front matter; 2.23" }
- { rel: "refersTo", target: "QAA Characteristics Statement: Micro-credentials (2022) (not ingested)", note: "2.18" }
- { rel: "themeReference", target: "std:doc:qaa-enterprise-2018-guidance", note: "listed in the references (back matter); the enterprise theme, 1.44 to 1.48" }
- { rel: "themeReference", target: "std:doc:qaa-advancehe-esd-2021-guidance", note: "listed in the references (back matter); the sustainability theme, 1.33 to 1.43" }
- { rel: "refersTo", target: "PSRB accreditation requirements (Appendix 1 bodies; not yet ingested)", note: "1.7, 2.5, 2.26, 2.33" }
```

### S8 Currency and review
<!-- label: source; status: drafted; basis: primary -->
```yaml
published: "2025-04"
lastReviewed: "none-stated"
reviewCycle: "none-stated"
consultation: "none-stated; the advisory group includes PSRB and employer representatives (back matter)"
replacedBy: "none"
```

### S9 Commentary (optional)
<!-- label: editorial; status: drafted; basis: secondary -->
`unknown`: not researched in P1 (Part E).

### SB1 The subject
<!-- label: both; status: drafted; basis: primary -->
- Accounting is studied as a social, economic and governance practice, a main form of information and control in every kind of organisation, not only as the measurement of profit and capital (D1, 1.4, 3.4, 3.5).
- It joins the conceptual (theory and its social, sustainability, political and economic context) and the applied and technical; both are a floor (D1, 1.14, 3.6).
- Judgement under uncertainty, ethics, professional scepticism and integrity in weighing evidence are at its core (D1, 1.10, 3.10 c, 3.10 h).
- It sits in a contested space between academic study and the accountancy bodies' professional requirements; the statement, not accreditation, sets the degree (D1, 1.7, 1.8, 2.5, 2.26).
- Data and the systems that produce it are central, from double entry to ERP, analytics and AI (D1, 1.11, 3.10 f, 3.10 k).
- It looks forward: critical of current accounting, imagining other futures, sustainability accounting foremost, and preparing for rules that change within a career (D1, 1.9, 1.13, 3.3, 3.7).
- Master's study comes in four taught types (advanced or specialist, conversion, professional, integrated), each with self-directed research-based inquiry; research master's are outside the statement (D1, 1.16, 1.17, 1.18).

### SB2 Themes in this subject
<!-- label: both; status: drafted; basis: primary -->
```yaml
- theme: theme:edi
  inThisSubject: "diverse and decolonised content, critique of dominant approaches, EDI applied area by area (governance, reporting, decisions, tax, audit, finance, economics), inclusive assessment and safeguards in peer marking (D1, 1.19 to 1.28, 3.41)"
  statements: ["qaa/accounting-2025/1.19", "qaa/accounting-2025/1.20", "qaa/accounting-2025/1.21", "qaa/accounting-2025/1.22", "qaa/accounting-2025/1.25", "qaa/accounting-2025/1.28", "qaa/accounting-2025/3.41"]
- theme: theme:accessibility
  inThisSubject: "legal requirements as the minimum across the student journey, anticipatory adjustments, attainment gap investigation, equal access to placements and abroad study (D1, 1.29 to 1.32, 3.33)"
  statements: ["qaa/accounting-2025/1.29", "qaa/accounting-2025/1.30", "qaa/accounting-2025/1.31", "qaa/accounting-2025/1.32", "qaa/accounting-2025/3.33"]
- theme: theme:esd
  inThisSubject: "sustainability in its broadest sense, wider than ESG disclosure; accounting as catalyst for change (double materiality, net zero, modern slavery, carbon), sustainability data in systems, and graduates able to lead the agenda (D1, 1.33 to 1.43, 3.10 g)"
  statements: ["qaa/accounting-2025/1.33", "qaa/accounting-2025/1.34", "qaa/accounting-2025/1.35", "qaa/accounting-2025/1.36", "qaa/accounting-2025/1.38", "qaa/accounting-2025/1.39", "qaa/accounting-2025/1.40", "qaa/accounting-2025/1.41", "qaa/accounting-2025/1.42", "qaa/accounting-2025/1.43"]
- theme: theme:enterprise
  inThisSubject: "enterprise and entrepreneurship as employability and personal development, built through the core content and research-led teaching, and graduate entrepreneurialism with regard to the public interest (D1, 1.44 to 1.48, 3.15 v)"
  statements: ["qaa/accounting-2025/1.44", "qaa/accounting-2025/1.45", "qaa/accounting-2025/1.46", "qaa/accounting-2025/3.15.b10"]
- theme: theme:genai
  inThisSubject: "a fifth theme of its own: GenAI in accounting practice, bias in AI, GenAI for learning and the redesign of assessment and integrity policy (D1, 1.49 to 1.55, 3.42, 3.43)"
  statements: ["qaa/accounting-2025/1.51", "qaa/accounting-2025/1.52", "qaa/accounting-2025/1.53", "qaa/accounting-2025/1.54", "qaa/accounting-2025/1.55", "qaa/accounting-2025/3.42", "qaa/accounting-2025/3.43"]
```

### SB3 Content and delivery
<!-- label: both; status: drafted; basis: primary -->
```yaml
areas:
  - { component: "3.9", gloss: "core accounting-specific skills: recording, statements, operational and financial analysis" }
  - { component: "3.10", gloss: "twelve broad areas a to l: accountability and trust; environment; ethics; governance and reporting; decision information; systems and data; regulation; audit and assurance; taxation; uncertainty and risk; analytics and statistics; financial markets" }
  - { component: "3.15", gloss: "twelve graduate skills m to x: communication; collaboration; self-efficacy; critical thinking; problem solving; data analysis; systems thinking; digital literacy; numeracy; entrepreneurialism; cultural awareness; research" }
practices:
  - { component: "3.19", kind: "teaching", gloss: "dialogic, critical, reflexive, constructivist and collaborative pedagogies for deep learning" }
  - { component: "3.20", kind: "teaching", gloss: "lectures, seminars, workshops, tutorials, blended and active learning" }
  - { component: "3.21", kind: "learning", gloss: "games, simulations, authentic and experiential learning, cases, role play, practitioners" }
  - { component: "3.22", kind: "learning", gloss: "cloud accounting, analytics tools, spreadsheets, AI" }
  - { component: "3.28", kind: "assessment", gloss: "formative assessment and feedback" }
  - { component: "3.31", kind: "assessment", gloss: "critical, authentic, case-based assessment; limits on multiple choice" }
  - { component: "3.34", kind: "assessment", gloss: "dialogues of learning; inner feedback by comparison" }
  - { component: "3.37", kind: "assessment", gloss: "fifteen typical methods, from examinations to capstone projects" }
  - { component: "3.39", kind: "assessment", gloss: "team and group assessment" }
  - { component: "3.41", kind: "assessment", gloss: "peer discussion and review with safeguards" }
```

### SB4 Benchmark standards
<!-- label: both; status: drafted; basis: primary -->
```yaml
rungs:
  - { rung: "threshold", leadIn: "4.5", award: "bachelor's with honours", items: 7, label: "Threshold (3rd or pass)" }
  - { rung: "typical", leadIn: "4.5", award: "bachelor's with honours", items: 7, label: "Typical (2:2)" }
  - { rung: "very-good", leadIn: "4.5", award: "bachelor's with honours", items: 7, label: "Very good (2:1)" }
  - { rung: "excellent", leadIn: "4.5", award: "bachelor's with honours", items: 7, label: "Excellent (1st)" }
  - { rung: "threshold", leadIn: "4.7", award: ["master's (advanced or specialist)", "master's (conversion)", "master's (professional)", "integrated master's"], items: 27, label: "Table 2: Master's degree benchmark standards (threshold level)" }
rungBases: "4.3 defines each honours level as the least shown by every graduate in its class (threshold 3rd or pass, typical 2:2, very good 2:1, excellent 1st), informed by Annex D; 4.5 names four bases of difference: depth of mastery, breadth of mastery, integration of mastery and mastery of application; higher levels include all lower ones. Table 2 sets threshold only for four master's types; merit and distinction are left to institutions (4.8)."
outcomeLists:
  - { leadIn: "3.15", gloss: "twelve graduate skills on completing the degree (m to x)", items: 12, award: ["bachelor's with honours"] }
  - { leadIn: "3.10", gloss: "twelve broad areas of knowledge, understanding and in situ skills courses include (a to l)", items: 12, award: ["all Accounting degrees"] }
outcomes:
  - { outcome: "critical, ethical and contextual knowledge", threshold: "qaa/accounting-2025/4.5.b1", typical: "qaa/accounting-2025/4.5.b3", veryGood: "qaa/accounting-2025/4.5.b5", excellent: "qaa/accounting-2025/4.5.b7", basis: "inferred", domain: "knowledge", award: "bachelor's with honours" }
  - { outcome: "theory in critical discussion", threshold: "qaa/accounting-2025/4.5.b2", typical: "qaa/accounting-2025/4.5.b4", veryGood: "qaa/accounting-2025/4.5.b6", excellent: "qaa/accounting-2025/4.5.b8", basis: "inferred", domain: "understanding", award: "bachelor's with honours" }
  - { outcome: "knowledge across the broad areas", threshold: "qaa/accounting-2025/4.5.b9", typical: "qaa/accounting-2025/4.5.b11", veryGood: "qaa/accounting-2025/4.5.b13", excellent: "qaa/accounting-2025/4.5.b15", basis: "inferred", domain: "knowledge", award: "bachelor's with honours" }
  - { outcome: "integration across the areas", threshold: "qaa/accounting-2025/4.5.b10", typical: "qaa/accounting-2025/4.5.b12", veryGood: "qaa/accounting-2025/4.5.b14", excellent: "qaa/accounting-2025/4.5.b16", basis: "inferred", domain: "understanding", award: "bachelor's with honours" }
  - { outcome: "transferable and professional skills", threshold: "qaa/accounting-2025/4.5.b17", typical: "qaa/accounting-2025/4.5.b19", veryGood: "qaa/accounting-2025/4.5.b21", excellent: "qaa/accounting-2025/4.5.b23", basis: "inferred", domain: "generic-skill", award: "bachelor's with honours" }
  - { outcome: "building arguments", threshold: "qaa/accounting-2025/4.5.b18", typical: "qaa/accounting-2025/4.5.b20", veryGood: "qaa/accounting-2025/4.5.b22", excellent: "qaa/accounting-2025/4.5.b24", basis: "inferred", domain: "generic-skill", award: "bachelor's with honours" }
  - { outcome: "application to problems", threshold: "qaa/accounting-2025/4.5.b25", typical: "qaa/accounting-2025/4.5.b26", veryGood: "qaa/accounting-2025/4.5.b27", excellent: "qaa/accounting-2025/4.5.b28", basis: "inferred", domain: "subject-skill", award: "bachelor's with honours" }
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
- { body: "professional, statutory and regulatory bodies (PSRBs), chiefly the accountancy bodies", says: "potential partners in design whose accreditation and exemptions many students seek; degrees sit in a contested space with them; courses must not be built for exemptions at the cost of broader aims and should meet the statement rather than PSRB-prescribed content; they monitor accredited courses; their requirements may inform competence standards (D1, front matter, 1.7, 1.8, 1.16 c, 1.38, 1.48, 2.5, 2.16, 2.23, 2.26, 2.33, 3.43, 4.2)", requirements: "not yet ingested (Part E)" }
- { body: "Association of Chartered Certified Accountants (ACCA)", says: "listed among the main PSRBs, accounting institutes and regulators relevant to UK accounting courses (D1, Appendix 1)", requirements: "not yet ingested (Part E)" }
- { body: "Association of International Accountants (AIA)", says: "listed among the main PSRBs, accounting institutes and regulators relevant to UK accounting courses (D1, Appendix 1)", requirements: "not yet ingested (Part E)" }
- { body: "Chartered Accountants Ireland (CAI)", says: "listed among the main PSRBs, accounting institutes and regulators relevant to UK accounting courses (D1, Appendix 1)", requirements: "not yet ingested (Part E)" }
- { body: "Chartered Institute of Public Finance and Accountancy (CIPFA)", says: "listed among the main PSRBs, accounting institutes and regulators relevant to UK accounting courses (D1, Appendix 1)", requirements: "not yet ingested (Part E)" }
- { body: "AICPA & CIMA", says: "listed among the main PSRBs, accounting institutes and regulators relevant to UK accounting courses (D1, Appendix 1)", requirements: "not yet ingested (Part E)" }
- { body: "Financial Reporting Council (FRC)", says: "listed among the main PSRBs, accounting institutes and regulators relevant to UK accounting courses (D1, Appendix 1)", requirements: "not yet ingested (Part E)" }
- { body: "IFRS Foundation", says: "listed among the main PSRBs, accounting institutes and regulators relevant to UK accounting courses (D1, Appendix 1)", requirements: "not yet ingested (Part E)" }
- { body: "Institute of Chartered Accountants in England and Wales (ICAEW)", says: "listed among the main PSRBs, accounting institutes and regulators relevant to UK accounting courses (D1, Appendix 1)", requirements: "not yet ingested (Part E)" }
- { body: "Institute of Chartered Accountants of Scotland (ICAS)", says: "listed among the main PSRBs, accounting institutes and regulators relevant to UK accounting courses (D1, Appendix 1)", requirements: "not yet ingested (Part E)" }
- { body: "Institute of Financial Accountants (IFA)", says: "listed among the main PSRBs, accounting institutes and regulators relevant to UK accounting courses (D1, Appendix 1)", requirements: "not yet ingested (Part E)" }
- { body: "International Federation of Accountants (IFAC)", says: "listed among the main PSRBs, accounting institutes and regulators relevant to UK accounting courses (D1, Appendix 1)", requirements: "not yet ingested (Part E)" }
- { body: "Association of Accounting Technicians (AAT)", says: "listed among the main PSRBs, accounting institutes and regulators relevant to UK accounting courses (D1, Appendix 1)", requirements: "not yet ingested (Part E)" }
- { body: "Accounting Technicians Ireland (ATI)", says: "listed among the main PSRBs, accounting institutes and regulators relevant to UK accounting courses (D1, Appendix 1)", requirements: "not yet ingested (Part E)" }
- { body: "Equality and Human Rights Commission", says: "providers writing competence standards should follow its latest guidance (D1, 4.2)", requirements: "not-applicable-by-design: guidance, not course requirements" }
- { body: "Office for Students", says: "in England the statement is not a sector-recognised standard under its regulatory framework (D1, front matter)", requirements: "not-applicable-by-design" }
```

### SB6 Cross-cutting references
<!-- label: both; status: drafted; basis: primary -->
```yaml
themes:
  - { id: "theme:edi", named: "Equality, diversity and inclusion (front matter: equity, diversity, and inclusion)", carriedIn: ["front matter", "1.19", "1.20", "1.21", "1.22", "1.23", "1.24", "1.25", "1.26", "1.27", "1.28", "1.38", "2.1", "2.20", "2.24", "2.30", "2.31", "3.10", "3.15", "3.23", "3.29", "3.33", "3.41"], statements: ["qaa/accounting-2025/1.19", "qaa/accounting-2025/1.20", "qaa/accounting-2025/1.21", "qaa/accounting-2025/1.22", "qaa/accounting-2025/1.25", "qaa/accounting-2025/1.28", "qaa/accounting-2025/3.41"] }
  - { id: "theme:accessibility", named: "Accessibility and the needs of disabled students", carriedIn: ["front matter", "1.29", "1.30", "1.31", "1.32", "2.1", "2.19", "2.31", "3.23", "3.33"], statements: ["qaa/accounting-2025/1.29", "qaa/accounting-2025/1.30", "qaa/accounting-2025/1.31", "qaa/accounting-2025/1.32", "qaa/accounting-2025/3.33"] }
  - { id: "theme:esd", named: "Education for sustainable development", carriedIn: ["front matter", "1.1", "1.2", "1.3", "1.4", "1.11", "1.13", "1.14", "1.16", "1.21", "1.33", "1.34", "1.35", "1.36", "1.38", "1.39", "1.40", "1.41", "1.42", "1.43", "2.1", "2.6", "2.24", "2.31", "3.4", "3.8", "3.10", "3.15", "4.5", "4.8"], statements: ["qaa/accounting-2025/1.33", "qaa/accounting-2025/1.34", "qaa/accounting-2025/1.35", "qaa/accounting-2025/1.36", "qaa/accounting-2025/1.38", "qaa/accounting-2025/1.39", "qaa/accounting-2025/1.40", "qaa/accounting-2025/1.41", "qaa/accounting-2025/1.42", "qaa/accounting-2025/1.43"] }
  - { id: "theme:enterprise", named: "Employability, enterprise and entrepreneurship education", carriedIn: ["front matter", "1.38", "1.44", "1.45", "1.46", "1.47", "1.48", "2.4", "2.31", "3.15"], statements: ["qaa/accounting-2025/1.44", "qaa/accounting-2025/1.45", "qaa/accounting-2025/1.46", "qaa/accounting-2025/3.15.b10"] }
  - { id: "theme:genai", named: "Generative artificial intelligence (new theme id: Part E)", carriedIn: ["front matter", "1.12", "1.23", "1.49", "1.50", "1.51", "1.52", "1.53", "1.54", "1.55", "2.2", "2.31", "3.10", "3.15", "3.22", "3.34", "3.42", "3.43"], statements: ["qaa/accounting-2025/1.51", "qaa/accounting-2025/1.52", "qaa/accounting-2025/1.53", "qaa/accounting-2025/1.54", "qaa/accounting-2025/1.55", "qaa/accounting-2025/3.42", "qaa/accounting-2025/3.43"] }
frameworks:
  - { framework: "fheq", levels: ["fheq:6", "fheq:7"], citedIn: ["2.7", "2.13", "2.14", "4.3"] }
  - { framework: "scqf", levels: ["fqheis:10", "fqheis:11"], citedIn: ["2.7", "2.13", "2.14"] }
bodies:
  - { body: "PSRBs (generic)", citedIn: ["front matter", "1.7", "1.8", "1.16", "1.38", "1.48", "2.5", "2.16", "2.23", "2.26", "2.33", "3.43", "4.2", "4.8"] }
  - { body: "Association of Chartered Certified Accountants (ACCA)", citedIn: ["appendix 1", "back matter: advisory group"] }
  - { body: "Association of International Accountants (AIA)", citedIn: ["appendix 1"] }
  - { body: "Chartered Accountants Ireland (CAI)", citedIn: ["appendix 1", "back matter: advisory group"] }
  - { body: "Chartered Institute of Public Finance and Accountancy (CIPFA)", citedIn: ["appendix 1"] }
  - { body: "AICPA & CIMA", citedIn: ["appendix 1"] }
  - { body: "Financial Reporting Council (FRC)", citedIn: ["appendix 1"] }
  - { body: "IFRS Foundation", citedIn: ["appendix 1"] }
  - { body: "Institute of Chartered Accountants in England and Wales (ICAEW)", citedIn: ["appendix 1", "back matter: advisory group"] }
  - { body: "Institute of Chartered Accountants of Scotland (ICAS)", citedIn: ["appendix 1", "back matter: advisory group"] }
  - { body: "Institute of Financial Accountants (IFA)", citedIn: ["appendix 1"] }
  - { body: "International Federation of Accountants (IFAC)", citedIn: ["appendix 1"] }
  - { body: "Association of Accounting Technicians (AAT)", citedIn: ["appendix 1"] }
  - { body: "Accounting Technicians Ireland (ATI)", citedIn: ["appendix 1"] }
  - { body: "Equality and Human Rights Commission", citedIn: ["4.2"] }
  - { body: "Office for Students", citedIn: ["front matter"] }
sharedDocuments:
  - { document: "std:doc:qaa-fheq-2024-framework, Annex D", named: "Annex D of the Frameworks for Higher Education Qualifications of UK Degree-Awarding Bodies", citedIn: ["4.3", "back matter: references"], role: "the four classification descriptions the honours levels are informed by" }
  - { document: "std:doc:qaa-finance-2025-benchmarks (not yet ingested: Part E)", named: "Subject Benchmark Statement for Finance", citedIn: ["1.2", "3.10"], role: "covers single honours finance and details finance topics" }
  - { document: "QAA Master's Degree Characteristics Statement (not ingested: Part E)", named: "QAA Master's Degree Characteristics Statement", citedIn: ["4.6"], role: "informs the master's standards" }
  - { document: "QAA Quality Code 2024 (not ingested)", named: "Quality Code; UK Quality Code, Advice and Guidance: Partnerships", citedIn: ["front matter", "2.23"], role: "sector reference point; partnership guidance" }
  - { document: "QAA Glossary (not ingested)", named: "QAA's Glossary", citedIn: ["front matter"], role: "explains unfamiliar terms" }
  - { document: "QAA Characteristics Statement: Micro-credentials (2022) (not ingested)", named: "micro-credentials (QAA, 2022)", citedIn: ["2.18"], role: "flexible credit options" }
  - { document: "std:doc:qaa-enterprise-2018-guidance", named: "Enterprise and Entrepreneurship Education: Guidance for UK Higher Education Providers (2018)", citedIn: ["back matter: references"], role: "the enterprise theme" }
  - { document: "std:doc:qaa-advancehe-esd-2021-guidance", named: "Education for Sustainable Development Guidance (QAA and Advance HE, 2021)", citedIn: ["back matter: references"], role: "the sustainability theme" }
  - { document: "QAA advice on Generative AI (2023) (not ingested)", named: "Maintaining quality and standards in the ChatGPT era", citedIn: ["back matter: references"], role: "the GenAI theme" }
  - { document: "UN Sustainable Development Goals (external)", named: "UN Sustainable Development Goals", citedIn: ["1.21", "1.24", "1.33", "1.34"], role: "frame for EDI and sustainability" }
  - { document: "UN Principles of Responsible Management Education (external)", named: "UN Principles of Responsible Management Education (PRME)", citedIn: ["1.34", "appendix 2"], role: "frame for sustainability" }
  - { document: "Equality Act 2010 (law)", named: "Equality Act 2010", citedIn: ["4.2"], role: "defines competence standards" }
```

## Part B Terminology
<!-- The statement has no glossary of its own unless Part E says so; these are terms it defines in its text. -->

### B1 Concepts
<!-- label: both; status: drafted; basis: primary -->
```yaml
- { slug: "enterprise-and-entrepreneurship-education", definition: "developing students' capacity to generate ideas and the behaviours, attributes and competencies to realise them (D1, 1.44)", beneficiaryDefinition: "learning to come up with ideas and make them happen", scopeNote: "entrepreneurship is the applying of these to create cultural, social or economic value (1.44)", category: "unknown", practices: ["education"] }
- { slug: "generative-ai", definition: "AI algorithms that produce content from prompts, built on a probability model of their training data (D1, 1.49)", beneficiaryDefinition: "AI tools that write or make content when you ask them", scopeNote: "the fifth cross-cutting theme", category: "unknown", practices: ["education", "accounting"] }
- { slug: "self-efficacy", definition: "the ability to act and belief in one's own ability, with reflection and commitment to independent action (D1, 3.15 o)", beneficiaryDefinition: "believing you can do something and acting on it", scopeNote: "tied to self-managed lifelong learning", category: "unknown", practices: ["education"] }
- { slug: "systems-thinking", definition: "a way of seeing processes as interconnected systems and understanding the structures beneath complex situations (D1, 3.15 s)", beneficiaryDefinition: "seeing how the parts of a process connect", scopeNote: "applied to accounting and control systems", category: "unknown", practices: ["accounting"] }
- { slug: "conceptual-study", definition: "theoretical accounting with its social, sustainability, political and economic considerations (D1, 1.14)", beneficiaryDefinition: "the theory and wider context of accounting, as against its techniques", scopeNote: "with applied study, a minimum for the degree", category: "unknown", practices: ["accounting"] }
- { slug: "straightforward-and-structured-problem", definition: "a bounded problem whose key data and methods are well known, mainly quantitative and fairly certain (D1, Table 1 note)", beneficiaryDefinition: "a problem with clear edges, known methods and mostly numerical data", scopeNote: "higher levels deal with less bounded, more ambiguous, judgement-based problems", category: "unknown", practices: ["education"] }
- { slug: "honours-achievement-levels", definition: "four levels, each the least shown by every graduate in a degree class: threshold (3rd or pass), typical (2:2), very good (2:1), excellent (1st) (D1, 4.3)", beneficiaryDefinition: "what you need at the least for each class of honours degree", scopeNote: "very good is a fourth level beyond the three most statements use", category: "unknown", practices: ["education"] }
```

### B2a Terms as the issuer defines them
<!-- label: source; status: drafted; basis: primary -->
```yaml
- { concept: "enterprise-and-entrepreneurship-education", form: "enterprise and entrepreneurship education", lang: "en", partOfSpeech: "noun-phrase", termStatus: "preferred", register: "formal" }
- { concept: "generative-ai", form: "Generative AI", lang: "en", partOfSpeech: "noun-phrase", termStatus: "preferred", register: "formal" }
- { concept: "generative-ai", form: "GenAI", lang: "en", partOfSpeech: "noun", termStatus: "admitted", register: "formal" }
- { concept: "self-efficacy", form: "self-efficacy", lang: "en", partOfSpeech: "noun", termStatus: "preferred", register: "formal" }
- { concept: "systems-thinking", form: "systems thinking", lang: "en", partOfSpeech: "noun-phrase", termStatus: "preferred", register: "formal" }
- { concept: "conceptual-study", form: "conceptual", lang: "en", partOfSpeech: "adjective", termStatus: "preferred", register: "discipline-specific" }
- { concept: "straightforward-and-structured-problem", form: "straightforward and structured", lang: "en", partOfSpeech: "adjective", termStatus: "preferred", register: "formal" }
- { concept: "honours-achievement-levels", form: "Very good", lang: "en", partOfSpeech: "adjective", termStatus: "preferred", register: "formal" }
```

### B2b Associated vocabulary
`not-applicable-by-design`: the statement names no wider vocabulary.

### B3 Framework blocks
`not-applicable-by-design`: no term is defined its own way for one component.

### B4 Relations
<!-- label: both; status: drafted; basis: primary -->
```yaml
- { rel: "contrasts-with", from: "straightforward-and-structured-problem", to: "honours-achievement-levels", note: "Table 1 note: the higher levels deal with less bounded, more uncertain problems" }
```

## Part C Process
<!-- label: both; status: drafted; basis: primary -->

### C0 Formality
`not-applicable`: the statement sets out what graduates achieve and what courses provide, not a procedure.

## Part D Sources
```yaml
- key: D1
  issuer: The Quality Assurance Agency for Higher Education
  title: "Subject Benchmark Statement Accounting"
  edition: "April 2025 (fifth edition)"
  year: 2025
  url: unknown (the QAA page; the text came by stan's extraction)
  retrieved: "held from stan: wkspc2615-QAAVector mapped/accounting-2025/accounting-2025.raw.txt, commit 366bcb99a01118f2c4c3ebfa2a8337596bddc455; received 2026-10-03"
  licence: QAA copyright
  tier: primary
  readVia: direct
  held: aa0d574de5b392592fe4023fcfaf70a8591a6cd7e483d981c497f40049b2e541
  heldFiles: ["wkspc2601-library/txt/qaa-2025-accounting-subject-benchmark-statement-standard.txt", "wkspc2601-library/txt/qaa-2025-accounting-subject-benchmark-statement-standard.norm.txt", "wkspc2601-library/records/qaa-2025-accounting-subject-benchmark-statement-standard.chunks.json", "wkspc2601-library/records/qaa-2025-accounting-subject-benchmark-statement-standard.held.json"]
  citedIn: [S1, S2, S3, S4, S4a, S5, S6, S7, SB1, SB2, SB3, SB4, SB5, SB6]
```

### D2 Research log
```yaml
- { ref: D1, tier: primary, consulted: 2026-10-03, pass: P1, outcome: "read whole, direct, from the normalised text; skeleton by tools/std_prep.py, document by tools/bm_build.py" }
- { ref: "ADAPT subj HESA stores, cah.json and hecos.json (designs/ingest/standards/subj/vocab)", tier: primary, consulted: 2026-10-03, pass: P1, outcome: "codes for statedSubjects and subjects" }
```

### D3 Wanted sources
```yaml
- { w: "W-std-0025", citation: "QAA (2025) Subject Benchmark Statement: Finance", settles: ["SB6", "S7"], asked: "2026-10-03", state: "held by stan, not yet ingested (S-02)" }
- { w: "W-std-0026", citation: "QAA Master's Degree Characteristics Statement", settles: ["SB6", "S7", "S5"], asked: "2026-10-03", state: "wanted" }
```

## Part E Gaps and questions
- SB4, rungs: four honours levels, not three: threshold (3rd or pass), typical (2:2), very good (2:1), excellent (1st) (4.3). `very-good` is recorded as a rung value the template does not yet list (threshold, typical, excellent, none): for a template ruling. SB4 `outcomes` carries it as `veryGood`.
- SB4, shape: the honours standards are one table (Table 1, 4.5) of four categories by four levels; three categories hold two sentences per cell, recorded as two S4 records each (a knowledge sentence and an ability sentence), so seven outcomes at four levels (28 records, 4.5.b1 to b28 in reading order). Table 2 (4.7; it follows 4.8 in the text) gives master's standards at threshold only for four master's types (27 records, 4.7.b1 to b27).
- SB4, gradeOf: Table 1 pairs each cell with the next level in the same row, so each link (21) is plain; the builder writes `basis: inferred` throughout. Candidate for `stated` at P3. Master's cells take no gradeOf: Table 2 has threshold only.
- S4, force: every table cell takes force `threshold`, since 4.3 defines each level as "the minimum to be achieved by all graduates" in its class and Table 2 is headed "(threshold level)"; the Table 1 caption also says graduates "will have achieved" these.
- S4, force: "is/are expected to" is not one of the five obliging words. 3.15 m to x ("a graduate is expected to have acquired skills"), 1.16 a and 1.18 are recorded as `describes` and treated as statements, as is 3.10 g, which has no modal of its own and whose lead-in "should" is too far away for the script check to see. For Abbott: should "expected to" read as `should` or `will`?
- S4, force: paragraphs obliging only in words outside the five were not taken as statements: 1.37 ("need to appreciate"), 2.21 and 2.29 ("essential"), 3.7 ("need to include", "is necessary"); 1.10, 1.12, 1.47, 1.48 ("might consider"), 2.7, 2.8, 2.9, 2.15, 2.18 to 2.20, 2.22, 2.24, 2.25, 2.27, 2.30, 3.1, 3.11, 3.14, 3.21, 3.38, 3.40, 4.1, 4.3, 4.6 and 4.8 are descriptive, permissive or introductory and are S3 components only.
- S4, list items not taken: the bullets of 1.23 ("could"), 1.24 ("might"), 1.30 ("may include"), 2.24 ("examples include") and 3.37 ("typically include") are examples under non-obliging lead-ins; the skeleton offered them as candidates. 1.30's own lead-in obliges and is one record (its stem). 4.3's four bullets are the definitions of the levels (SB4 `rungBases`), not rung items, though the skeleton marked them threshold.
- S4, ids: list items use the builder's `.b<n>` form for the issuer's letters: 1.16.b1 to b3 = types a to c (d, research master's, is out of scope and not a statement); 3.10.b1 to b12 = areas a to l; 3.15.b1 to b12 = skills m to x. The 3.10 stem is its own record.
- S4, 1.2: "should be aligned ... and must include": force recorded as `must`, which governs the content clause.
- S4, 3.10 i: "It is essential that ... equip" and "should": force `should`; "at a minimum" names the UK taxes.
- S4, 3.22: "it is highly likely that it will be necessary": force `will`, hedged in the issuer's own words.
- S4, levels: statements addressed to "graduates" in sections 1 to 3 with a generic-skill domain (1.38, 1.42, 1.44 to 1.46, 2.3, 3.13, 3.32, 3.15 m to x) are recorded at fheq:6 for the honours degree; they also bear on master's graduates. Course-wide provider duties carry level none.
- S4, spans: the skeleton's paragraph spans run on into the next sub-heading (for example 1.18 ends with "Equality, diversity and inclusion"); records here use `find` with the paragraph text alone. Page numbers inside a span (3.10 c, i, j; 3.15 r) are part of the held text and stay in `source`.
- S4, 1.46: the held text breaks a reference across lines ("paragraphs 1.4,\n1.46 and 3.16-3.26"); the second "1.46" is a reference (DPN-1), not a new paragraph; the skeleton kept 1.46 whole.
- S6, SB6: a fifth cross-cutting theme, generative artificial intelligence, has no shared theme id; `theme:genai` is proposed here and needs adding to the shared list.
- S6: the front matter names the EDI theme "equity, diversity, and inclusion" and section 1 "Equality, diversity and inclusion"; the same theme.
- S2, subjects: HECoS 100105 accounting, 100104 accountancy, CAH17-01-08 and 100831 taxation are named by the text; 100840 audit management, 100836 management accountancy and 100107 finance are inferred (finance only for joint courses; single honours finance is out of scope, 1.2) and wait for P3.
- S5: the statement cites FHEQ Level 7 and FQHEIS Level 11 only for the integrated master's (2.7, 2.13); fheq:7 for the other master's types is inferred from the frameworks (std:doc:qaa-fheq-2024-framework S5, Table 1).
- S5, CQFW: not named; Wales appears only for course length (2.9).
- SB5: Appendix 1 lists 13 bodies; the AICPA & CIMA entry spells out its parent bodies. 2.23 writes "PRSBs", the issuer's typo for PSRBs. Appendix 2's learned associations (BAFA, IAFA, EAA, AAA and others; CABS listed twice) are not PSRBs and are not recorded in SB5.
- SB5: none of the PSRBs' own requirements is ingested.
- S7, S8: the previous statement's date is not given in the body; the back matter names advisory groups for 2019 (minor update), 2014, 2007 and 2000, and the cover note says "Fifth Edition Published - 10 April 2025". supersedes points to a 2019 statement not held.
- Patterns against Psychology: four honours levels with a very good (2:1) level; standards given as tables, not lists; master's standards for four types at threshold only; a fifth theme (GenAI); course-design duties in "should" dominate sections 1 to 3, so most statements are provider duties (student version not applicable); outcome lists use "is expected to have acquired" rather than "are able to".
- S1, licence: the text gives a copyright notice and no re-use terms; QAA's terms for holding are to check.
- S9: not researched in P1.
- ST-12: versions here run to the lengths the content needs; no length range is yet set.

---

## Change notes
- 0.1.2, 3 October 2026, 21:02: moved with its held text from UNI to the source library repo (`wkspc2601-library/ingested/standards/`, texts in `txt/`, records in `records/`); paths only (Abbott, 20:56; std N-0119).
- 0.1.1, 3 October 2026, 20:20: obliging words outside the five read as must, "ought to" as should, on statements outside the rungs, each marked on its force line (Abbott, 20:17; D-std-0016).
- 0.1.0, 2026-10-03 16:21: researched by run frame 0.1.1-draft and standards run layer 0.7.0-draft, std, run 0082 (P1); built by tools/bm_build.py.
