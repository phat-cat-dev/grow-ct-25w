---
id: std:doc:qaa-mathematics-statistics-and-operational-research-2023-benchmarks
title: "Subject Benchmark Statement Mathematics, Statistics and Operational Research"
profile: standards/subject-benchmark
profileVersion: 0.2.0-draft
issuer: QAA
kind: subject-benchmark
jurisdiction: [UK]
subjectScope: subjects
subjects:
  - { scheme: "hecos", code: "100403", label: "mathematics", basis: "stated" }
  - { scheme: "hecos", code: "100406", label: "statistics", basis: "stated" }
  - { scheme: "hecos", code: "100404", label: "operational research", basis: "stated" }
  - { scheme: "cah", code: "CAH09-01-01", label: "mathematics", basis: "stated" }
  - { scheme: "cah", code: "CAH09-01-03", label: "statistics", basis: "stated" }
  - { scheme: "cah", code: "CAH09-01-02", label: "operational research", basis: "stated" }
  - { scheme: "cah", code: "CAH09-01", label: "mathematical sciences", basis: "stated" }
  - { scheme: "cah", code: "CAH09", label: "mathematical sciences", basis: "stated" }
  - { scheme: "hecos", code: "100405", label: "pure mathematics", basis: "stated" }
  - { scheme: "hecos", code: "101032", label: "probability", basis: "stated" }
  - { scheme: "hecos", code: "100402", label: "mathematical modelling", basis: "stated" }
  - { scheme: "hecos", code: "101034", label: "statistical modelling", basis: "stated" }
  - { scheme: "hecos", code: "101027", label: "numerical analysis", basis: "stated" }
  - { scheme: "hecos", code: "100784", label: "history of mathematics", basis: "stated" }
  - { scheme: "hecos", code: "101028", label: "engineering and industrial mathematics", basis: "inferred" }
  - { scheme: "hecos", code: "100400", label: "applied mathematics", basis: "inferred" }
edition: "March 2023 (fifth edition)"
published: 2023-03
status: current
supersedes: "the fourth edition (2019), named in the membership pages (D1, section 6); not ingested"
heldText: { method: sha256-bytes, raw: 7c8c162291f2a304a41442f89213ff5156deed1c942988d0a2b95d4e5787a0d6, normalised: 23ff4de485496bc7a3c380d5c29b258eb59ece974b0fed383c1fa6c690cef53c }
heldTextStan: { method: sha256-stan, raw: 7c8c162291f2a304a41442f89213ff5156deed1c942988d0a2b95d4e5787a0d6, normalised: a01674402681a07153207a5647bec7c8e5e4f0f65902af85527f50522418d119 }
licence: "QAA copyright; held for study, private to the project, never published"
series: "QAA Subject Benchmark Statements, fifth edition series with cross-cutting themes (2022 onward)"
awardsCovered: ["bachelor's with honours", "integrated master's", "master's"]
levelsCovered: ["fheq:6", "fheq:7", "fqheis:10", "fqheis:11"]
nations: ["England", "Wales", "Scotland", "Northern Ireland"]
parts:
  S: full
  B: "partial: no glossary in the document (it points readers to QAA's Glossary); terms it defines in its text"
  C: "not-applicable: the document sets expectations, not a procedure"
pins: { structure: 0.13.0-draft, template: 0.8.0-draft, benchmarkTemplate: 0.6.0-draft, runFrame: 0.1.1-draft, runLayer: 0.7.0-draft, standards: none yet, terminology: none yet }
lifecycle: drafted
researchedBy: run frame 0.1.1-draft; standards run layer 0.7.0-draft; std, run 0120 (tools/bm_build.py)
passes:
  P1: "2026-10-03 18:06"
  P2: "skipped: read direct from the held text; inferred codes and rung links are for P3"
  P3: open
version: 0.1.2
---

<!-- from INGEST wpk-0016-ingest-pd-template-standards.md 0.8.0-draft and wpk-0016-ingest-pd-template-standards-benchmark.md 0.6.0-draft; built by tools/bm_build.py from run-src/ -->
# Subject Benchmark Statement: Mathematics, Statistics and Operational Research (QAA, March 2023)

> Run 0120, P1 by std. The issuer's words are held in the source library, `wkspc2601-library/txt/qaa-2023-mathematics-statistics-operational-research-subject-benchmark-standard.norm.txt`; each S4 record carries its statement in full (`source`) for language analysis, with its span. Paraphrases and versions are ours. Private to the project, never published. In front matter `status` is the issuer's; ours is `lifecycle`. Doubts are in Part E.

## Part 0 Summary

### 0.1 Agent definition
<!-- label: editorial; status: drafted; basis: primary -->
QAA's UK reference point for what a graduate in mathematics, statistics or operational research (MSOR, treated as one field with many combinations) should know and be able to do. It sets threshold standards only, one list for the bachelor's degree with honours and one for the integrated master's, adds a list of professional standards and a list of general skills, and leaves performance above threshold to Annex D of the Frameworks. Reach for it when designing, reviewing or describing an MSOR course, a data science course with substantial MSOR content or service teaching that depends on the subject. It is not a curriculum, not an accrediting body's standard and not a regulatory requirement in England.

### 0.2 Summary
<!-- label: both; status: drafted; basis: primary -->
Published by QAA in March 2023 as the fifth edition, the statement covers bachelor's degrees with honours, integrated master's degrees and, more loosely, taught postgraduate master's degrees in MSOR. It describes the subject and its three fields, the spectrum from theory-based to practice-based courses, course design, progression, flexibility, partnership and review, the content, skills, teaching and assessment of a degree, and benchmark standards at threshold only (4.5 for honours, 4.6 for the integrated master's), with the bases for judging achievement above threshold (4.8) and a list of professional standards (4.9). It treats the four cross-cutting themes (equality, diversity and inclusion; accessibility; sustainability; enterprise and entrepreneurship education), refers to Annex D of the Frameworks for classification and names the IMA, RSS, ORS and IFoA as bodies offering accreditation or professional recognition.

## Part S Standard

### S1 Identity
<!-- label: source; status: drafted; basis: primary -->
```yaml
issuer: The Quality Assurance Agency for Higher Education
title: "Subject Benchmark Statement Mathematics, Statistics and Operational Research"
edition: "March 2023 (fifth edition)"
dates:
  published: 2023-03
  other: []
kind: subject-benchmark
jurisdiction: [UK]
authority: "reference: a sector reference point, not a regulatory requirement (D1, front matter); in England not a sector-recognised standard under the OfS framework; a key reference point in Wales and Scotland; part of current quality arrangements in Northern Ireland (D1, front matter: Relationship to legislation)"
licence: "QAA copyright; the document gives no re-use terms in its text (D1, front matter)"
copyrightNotice: { text: "© The Quality Assurance Agency for Higher Education 2023", locator: "D1, index" }
```

### S2 Purpose and scope
<!-- label: source; status: drafted; basis: primary -->
```yaml
governs: "what can be expected of a graduate in MSOR at the end of a bachelor's degree with honours or an integrated master's degree, with taught master's degrees developing some or all of those standards, and the nature and characteristics of awards in the subject (D1, front matter: About this Statement; 2.5; 4.2; 4.7)"
appliesTo:
  awards: ["bachelor's with honours", "integrated master's", "master's (taught postgraduate, 4.7)", "joint honours and interdisciplinary courses (described, 2.7, 2.13)", "integrated degree apprenticeships (academic component, 2.11)"]
  levels: ["fheq:6", "fheq:7", "fqheis:10", "fqheis:11"]
  providers: ["UK higher education providers"]
whoMustUse: "none-stated; it is a reference point, not a requirement (D1, front matter)"
howUsed: ["design", "approval", "review", "other: external examining; PSRBs; information for prospective students and employers"]
doesNot: "it is not a national curriculum and does not prescribe teaching, learning or assessment; it carries no statutory or regulatory requirement (D1, front matter)"
beneficiary: the student
statedScope: "\"For the purposes of this document, the term 'MSOR' (Mathematics, Statistics and Operational Research) should be understood to be more than the disjoint union of its three named elements and instead be understood to encompass a wide variety of combinations of the various fields.\" (D1, 1.1)"
statedSubjects:
  - { name: "Mathematics", locator: "(D1, title; 1.3; 1.4)", kind: "subject", codes: [{ scheme: "hecos", code: "100403", label: "mathematics" }, { scheme: "cah", code: "CAH09-01-01", label: "mathematics" }] }
  - { name: "Statistics", locator: "(D1, title; 1.5; 1.6)", kind: "subject", codes: [{ scheme: "hecos", code: "100406", label: "statistics" }, { scheme: "cah", code: "CAH09-01-03", label: "statistics" }] }
  - { name: "Operational research", locator: "(D1, title; 1.7; 1.8)", kind: "subject", codes: [{ scheme: "hecos", code: "100404", label: "operational research" }, { scheme: "cah", code: "CAH09-01-02", label: "operational research" }] }
  - { name: "probability theory", locator: "(D1, 1.5)", kind: "specialism", codes: [{ scheme: "hecos", code: "101032", label: "probability" }] }
  - { name: "data science", locator: "(D1, 1.1; 1.6; 2.7; 3.6; 4.3)", kind: "programme title", codes: [] }
  - { name: "analytics; 'management science'", locator: "(D1, 1.8)", kind: "programme title", codes: [] }
  - { name: "mathematics for engineering", locator: "(D1, 1.9)", kind: "specialism", codes: [{ scheme: "hecos", code: "101028", label: "engineering and industrial mathematics" }] }
  - { name: "pure mathematics", locator: "(D1, 2.4; 3.15)", kind: "specialism", codes: [{ scheme: "hecos", code: "100405", label: "pure mathematics" }] }
  - { name: "mathematical and statistical modelling", locator: "(D1, 3.18; 3.27)", kind: "specialism", codes: [{ scheme: "hecos", code: "100402", label: "mathematical modelling" }, { scheme: "hecos", code: "101034", label: "statistical modelling" }] }
  - { name: "numerical analysis", locator: "(D1, 3.39)", kind: "specialism", codes: [{ scheme: "hecos", code: "101027", label: "numerical analysis" }] }
  - { name: "history of mathematics; mathematics education", locator: "(D1, 3.20)", kind: "specialism", codes: [{ scheme: "hecos", code: "100784", label: "history of mathematics" }] }
  - { name: "integrated master's (such as MMath); standalone master's (MSc, MRes); conversion master's", locator: "(D1, 1.13; 2.4; 2.6)", kind: "programme title", codes: [{ scheme: "hecos", code: "100403", label: "mathematics" }] }
  - { name: "single honours; joint honours; interdisciplinary degrees", locator: "(D1, 1.13; 2.7; 2.13)", kind: "programme title", codes: [] }
subjects: see front matter (subjectScope subjects)
```

### S3 Structure
<!-- label: both; status: drafted; basis: primary -->
```yaml
components:
  - { number: "1.1", order: 3, componentType: paragraph, parent: "section 1", heading: "Context and purposes of a Mathematics, Statistics and Operational Research degree", gloss: "MSOR as more than its three parts; overlap and interdisciplinary provision such as data science" }
  - { number: "1.2", order: 4, componentType: paragraph, parent: "section 1", heading: "Context and purposes of a Mathematics, Statistics and Operational Research degree", gloss: "why each field is described in turn" }
  - { number: "1.3", order: 5, componentType: paragraph, parent: "section 1", heading: "Context and purposes of a Mathematics, Statistics and Operational Research degree", gloss: "mathematics: origins in practical problems, then generalisation and abstraction" }
  - { number: "1.4", order: 6, componentType: paragraph, parent: "section 1", heading: "Context and purposes of a Mathematics, Statistics and Operational Research degree", gloss: "mathematics today: deduction from assumptions about concepts or models" }
  - { number: "1.5", order: 7, componentType: paragraph, parent: "section 1", heading: "Context and purposes of a Mathematics, Statistics and Operational Research degree", gloss: "statistics and probability: data under random variation, and their history" }
  - { number: "1.6", order: 8, componentType: paragraph, parent: "section 1", heading: "Context and purposes of a Mathematics, Statistics and Operational Research degree", gloss: "statistics today: models, data science and explaining results to non-experts" }
  - { number: "1.7", order: 9, componentType: paragraph, parent: "section 1", heading: "Context and purposes of a Mathematics, Statistics and Operational Research degree", gloss: "operational research: wartime origins; optimisation to problem structuring" }
  - { number: "1.8", order: 10, componentType: paragraph, parent: "section 1", heading: "Context and purposes of a Mathematics, Statistics and Operational Research degree", gloss: "analytics and management science at the edge of the scope" }
  - { number: "1.9", order: 11, componentType: paragraph, parent: "section 1", heading: "Context and purposes of a Mathematics, Statistics and Operational Research degree", gloss: "the subject beyond STEM and as service teaching" }
  - { number: "1.10", order: 12, componentType: paragraph, parent: "section 1", heading: "Context and purposes of a Mathematics, Statistics and Operational Research degree", gloss: "theory-based and practice-based course styles; every graduate a practitioner (S4)" }
  - { number: "1.11", order: 13, componentType: paragraph, parent: "section 1", heading: "Purposes and characteristics of an MSOR degree", gloss: "abstract and applied purposes, blurred in practice" }
  - { number: "1.12", order: 14, componentType: paragraph, parent: "section 1", heading: "Purposes and characteristics of an MSOR degree", gloss: "each provider shapes its own courses" }
  - { number: "1.13", order: 15, componentType: stem, parent: "section 1", heading: "Purposes and characteristics of an MSOR degree", gloss: "course configurations: foundation years, honours, integrated and taught master's, placements" }
  - { number: "1.14", order: 16, componentType: paragraph, parent: "section 1", heading: "Purposes and characteristics of an MSOR degree", gloss: "academic and transferable skills, further study and careers" }
  - { number: "1.15", order: 17, componentType: paragraph, parent: "section 1", heading: "Purposes and characteristics of an MSOR degree", gloss: "abstract reasoning and accuracy throughout; time to consolidate" }
  - { number: "1.16", order: 18, componentType: paragraph, parent: "section 1", heading: "Purposes and characteristics of an MSOR degree", gloss: "uneven attainment across modules is normal" }
  - { number: "1.17", order: 19, componentType: paragraph, parent: "section 1", heading: "Purposes and characteristics of an MSOR degree", gloss: "cumulative subject with strict prerequisites" }
  - { number: "1.18", order: 20, componentType: paragraph, parent: "section 1", heading: "Purposes and characteristics of an MSOR degree", gloss: "further study, employability and careers information" }
  - { number: "1.19", order: 21, componentType: paragraph, parent: "section 1", heading: "Purposes and characteristics of an MSOR degree", gloss: "economic and social value of the mathematical sciences" }
  - { number: "1.20", order: 22, componentType: stem, parent: "section 1", heading: "Purposes and characteristics of an MSOR degree", gloss: "professional recognition by the IMA, RSS, ORS and IFoA" }
  - { number: "1.21", order: 23, componentType: paragraph, parent: "section 1", heading: "Equality, diversity and inclusion", gloss: "why EDI matters for the subject" }
  - { number: "1.22", order: 24, componentType: paragraph, parent: "section 1", heading: "Equality, diversity and inclusion", gloss: "diverse student backgrounds and inclusive support" }
  - { number: "1.23", order: 25, componentType: paragraph, parent: "section 1", heading: "Equality, diversity and inclusion", gloss: "EDI in curriculum, processes and monitoring (S4)" }
  - { number: "1.24", order: 26, componentType: paragraph, parent: "section 1", heading: "Equality, diversity and inclusion", gloss: "provider commitment to EDI; Athena SWAN; the LMS Good Practice Scheme" }
  - { number: "1.25", order: 27, componentType: paragraph, parent: "section 1", heading: "Equality, diversity and inclusion", gloss: "decolonising the curriculum; reviewing practice for equity (S4)" }
  - { number: "1.26", order: 28, componentType: paragraph, parent: "section 1", heading: "Equality, diversity and inclusion", gloss: "role models, gender imbalance and inclusive material" }
  - { number: "1.27", order: 29, componentType: stem, parent: "section 1", heading: "Equality, diversity and inclusion", gloss: "examples of EDI good practice in seven areas" }
  - { number: "1.28", order: 30, componentType: paragraph, parent: "section 1", heading: "Accessibility", gloss: "anticipating needs; institutional support for staff (S4)" }
  - { number: "1.29", order: 31, componentType: paragraph, parent: "section 1", heading: "Accessibility", gloss: "barriers to participation at course and module level (S4)" }
  - { number: "1.30", order: 32, componentType: paragraph, parent: "section 1", heading: "Accessibility", gloss: "embedding accessibility so adjustments are rarely needed (S4)" }
  - { number: "1.31", order: 33, componentType: paragraph, parent: "section 1", heading: "Accessibility", gloss: "reasonable adjustments and specialist disability services" }
  - { number: "1.32", order: 34, componentType: paragraph, parent: "section 1", heading: "Accessibility", gloss: "embedded accessibility helps many groups" }
  - { number: "1.33", order: 35, componentType: paragraph, parent: "section 1", heading: "Accessibility", gloss: "well-curated courses (S4)" }
  - { number: "1.34", order: 36, componentType: stem, parent: "section 1", heading: "Accessibility", gloss: "subject features needing attention: notation, board work, non-linear argument, diagrams" }
  - { number: "1.35", order: 37, componentType: paragraph, parent: "section 1", heading: "Accessibility", gloss: "specialist technology removing barriers" }
  - { number: "1.36", order: 38, componentType: stem, parent: "section 1", heading: "Accessibility", gloss: "mainstream assistive tools fail mathematical content; responses (S4: the provider item)" }
  - { number: "1.37", order: 39, componentType: paragraph, parent: "section 1", heading: "Accessibility", gloss: "online and captured content; capture, captions and visibility (S4)" }
  - { number: "1.38", order: 40, componentType: paragraph, parent: "section 1", heading: "Accessibility", gloss: "support workers need subject terminology (S4)" }
  - { number: "1.39", order: 41, componentType: paragraph, parent: "section 1", heading: "Accessibility", gloss: "rare activities such as fieldwork; advice from other subjects" }
  - { number: "1.40", order: 42, componentType: paragraph, parent: "section 1", heading: "Accessibility", gloss: "flexible pedagogy and accessible notes" }
  - { number: "1.41", order: 43, componentType: paragraph, parent: "section 1", heading: "Accessibility", gloss: "unwritten course norms made explicit" }
  - { number: "1.42", order: 44, componentType: paragraph, parent: "section 1", heading: "Accessibility", gloss: "removing irrelevant barriers in assessment (S4)" }
  - { number: "1.43", order: 45, componentType: paragraph, parent: "section 1", heading: "Accessibility", gloss: "community resources for accessible courses" }
  - { number: "1.44", order: 46, componentType: paragraph, parent: "section 1", heading: "Sustainability", gloss: "the subject and the UN goals; social mobility" }
  - { number: "1.45", order: 47, componentType: paragraph, parent: "section 1", heading: "Sustainability", gloss: "real-world examples link the subject to sustainability" }
  - { number: "1.46", order: 48, componentType: stem, parent: "section 1", heading: "Sustainability", gloss: "ways to teach sustainability in the degree" }
  - { number: "1.47", order: 49, componentType: stem, parent: "section 1", heading: "Sustainability", gloss: "examples of methods applied to sustainability" }
  - { number: "1.48", order: 50, componentType: paragraph, parent: "section 1", heading: "Sustainability", gloss: "revisiting sustainability; innovation encouraged" }
  - { number: "1.49", order: 51, componentType: paragraph, parent: "section 1", heading: "Enterprise and entrepreneurship education", gloss: "enterprise education and careers" }
  - { number: "1.50", order: 52, componentType: paragraph, parent: "section 1", heading: "Enterprise and entrepreneurship education", gloss: "employability embedded in courses (S4)" }
  - { number: "1.51", order: 53, componentType: paragraph, parent: "section 1", heading: "Enterprise and entrepreneurship education", gloss: "enterprise defined" }
  - { number: "1.52", order: 54, componentType: paragraph, parent: "section 1", heading: "Enterprise and entrepreneurship education", gloss: "entrepreneurship defined" }
  - { number: "1.53", order: 55, componentType: paragraph, parent: "section 1", heading: "Enterprise and entrepreneurship education", gloss: "enterprise and entrepreneurship education defined" }
  - { number: "1.54", order: 56, componentType: paragraph, parent: "section 1", heading: "Enterprise and entrepreneurship education", gloss: "problem-solving and related enterprise competencies" }
  - { number: "1.55", order: 57, componentType: paragraph, parent: "section 1", heading: "Enterprise and entrepreneurship education", gloss: "projects and group work; preparing students for group work (S4)" }
  - { number: "1.56", order: 58, componentType: paragraph, parent: "section 1", heading: "Enterprise and entrepreneurship education", gloss: "problem-based learning, resilience and adaptability" }
  - { number: "1.57", order: 59, componentType: paragraph, parent: "section 1", heading: "Enterprise and entrepreneurship education", gloss: "client projects and authentic assessment with employers" }
  - { number: "1.58", order: 60, componentType: paragraph, parent: "section 1", heading: "Enterprise and entrepreneurship education", gloss: "employer and alumni events" }
  - { number: "1.59", order: 61, componentType: paragraph, parent: "section 1", heading: "Enterprise and entrepreneurship education", gloss: "placements and entrepreneurial skills" }
  - { number: "1.60", order: 62, componentType: paragraph, parent: "section 1", heading: "Enterprise and entrepreneurship education", gloss: "graduates explain their enterprise and employability growth (S4)" }
  - { number: "2.1", order: 64, componentType: paragraph, parent: "section 2", heading: "Design", gloss: "theory-based and practice-based styles defined" }
  - { number: "2.2", order: 65, componentType: paragraph, parent: "section 2", heading: "Design", gloss: "a spectrum of emphases, read from the curriculum not the title" }
  - { number: "2.3", order: 66, componentType: paragraph, parent: "section 2", heading: "Design", gloss: "routes into undergraduate study and entry qualifications" }
  - { number: "2.4", order: 67, componentType: paragraph, parent: "section 2", heading: "Design", gloss: "routes into taught master's: conversion and specialist" }
  - { number: "2.5", order: 68, componentType: paragraph, parent: "section 2", heading: "Design", gloss: "bachelor's and integrated master's levels; what bachelor's degrees give (S4)" }
  - { number: "2.6", order: 69, componentType: paragraph, parent: "section 2", heading: "Design", gloss: "integrated master's and standalone master's courses" }
  - { number: "2.7", order: 70, componentType: paragraph, parent: "section 2", heading: "Design", gloss: "joint honours and interdisciplinary degrees" }
  - { number: "2.8", order: 71, componentType: paragraph, parent: "section 2", heading: "Design", gloss: "learning outside the institution: placements, schools, study abroad" }
  - { number: "2.9", order: 72, componentType: paragraph, parent: "section 2", heading: "Design", gloss: "placement periods and credit; integrating credit-bearing placements (S4)" }
  - { number: "2.10", order: 73, componentType: paragraph, parent: "section 2", heading: "Design", gloss: "shared core and later specialisation" }
  - { number: "2.11", order: 74, componentType: paragraph, parent: "section 2", heading: "Design", gloss: "integrated degree apprenticeships (S4)" }
  - { number: "2.12", order: 75, componentType: paragraph, parent: "section 2", heading: "Progression", gloss: "progression to threshold; second-class degrees and postgraduate study (S4)" }
  - { number: "2.13", order: 76, componentType: paragraph, parent: "section 2", heading: "Progression", gloss: "joint and interdisciplinary students gain each subject's core skills (S4)" }
  - { number: "2.14", order: 77, componentType: paragraph, parent: "section 2", heading: "Progression", gloss: "integrated master's adds a year" }
  - { number: "2.15", order: 78, componentType: paragraph, parent: "section 2", heading: "Progression", gloss: "exit awards; four-year Scottish honours; part-time study" }
  - { number: "2.16", order: 79, componentType: paragraph, parent: "section 2", heading: "Flexibility", gloss: "progressive learning supports flexibility" }
  - { number: "2.17", order: 80, componentType: paragraph, parent: "section 2", heading: "Flexibility", gloss: "a shared core eases transfer" }
  - { number: "2.18", order: 81, componentType: paragraph, parent: "section 2", heading: "Flexibility", gloss: "optional modules and guidance on choosing (S4)" }
  - { number: "2.19", order: 82, componentType: paragraph, parent: "section 2", heading: "Flexibility", gloss: "prerequisites limit flexibility and credit transfer" }
  - { number: "2.20", order: 83, componentType: paragraph, parent: "section 2", heading: "Flexibility", gloss: "routes to Qualified Teacher Status in England" }
  - { number: "2.21", order: 84, componentType: paragraph, parent: "section 2", heading: "Flexibility", gloss: "flexible education for access and social mobility" }
  - { number: "2.22", order: 85, componentType: stem, parent: "section 2", heading: "Flexibility", gloss: "flexible assessment, credit and recruitment" }
  - { number: "2.23", order: 86, componentType: stem, parent: "section 2", heading: "Flexibility", gloss: "flexible delivery modes and study patterns" }
  - { number: "2.24", order: 87, componentType: paragraph, parent: "section 2", heading: "Flexibility", gloss: "courses flexible to change and to learners' needs (S4)" }
  - { number: "2.25", order: 88, componentType: paragraph, parent: "section 2", heading: "Partnership", gloss: "academic and professional partnerships" }
  - { number: "2.26", order: 89, componentType: paragraph, parent: "section 2", heading: "Partnership", gloss: "academic partnerships and advanced standing" }
  - { number: "2.27", order: 90, componentType: paragraph, parent: "section 2", heading: "Partnership", gloss: "industry partnerships, placements and projects" }
  - { number: "2.28", order: 91, componentType: paragraph, parent: "section 2", heading: "Partnership", gloss: "what placements involve" }
  - { number: "2.29", order: 92, componentType: paragraph, parent: "section 2", heading: "Partnership", gloss: "employer demand for sandwich placements" }
  - { number: "2.30", order: 93, componentType: paragraph, parent: "section 2", heading: "Partnership", gloss: "benefits of work with employers; oversight of delivery partners (S4)" }
  - { number: "2.31", order: 94, componentType: paragraph, parent: "section 2", heading: "Monitoring and review", gloss: "monitoring and periodic review" }
  - { number: "2.32", order: 95, componentType: paragraph, parent: "section 2", heading: "Monitoring and review", gloss: "external reviewers in periodic review" }
  - { number: "2.33", order: 96, componentType: paragraph, parent: "section 2", heading: "Monitoring and review", gloss: "external examiners and threshold standards" }
  - { number: "2.34", order: 97, componentType: paragraph, parent: "section 2", heading: "Monitoring and review", gloss: "accreditation by professional bodies" }
  - { number: "3.1", order: 99, componentType: paragraph, parent: "section 3", heading: "Content: Introduction", gloss: "a broad area with wide-ranging expectations" }
  - { number: "3.2", order: 100, componentType: paragraph, parent: "section 3", heading: "Content: Introduction", gloss: "subject knowledge varies at higher levels; that variety not restricted (S4)" }
  - { number: "3.3", order: 101, componentType: paragraph, parent: "section 3", heading: "Content: Introduction", gloss: "foundations mostly early, not only early" }
  - { number: "3.4", order: 102, componentType: paragraph, parent: "section 3", heading: "Content: Introduction", gloss: "no comprehensive content list, by design" }
  - { number: "3.5", order: 103, componentType: paragraph, parent: "section 3", heading: "Content: Introduction", gloss: "general skills: numeracy, computing and modelling (S4)" }
  - { number: "3.6", order: 104, componentType: paragraph, parent: "section 3", heading: "Content: Introduction", gloss: "data science and data-related careers" }
  - { number: "3.7", order: 105, componentType: paragraph, parent: "section 3", heading: "Subject-specific knowledge and understanding: General principles", gloss: "methods and techniques; at least one application area" }
  - { number: "3.8", order: 106, componentType: area, parent: "section 3", heading: "Methods and techniques", gloss: "common ground: calculus, linear algebra, probability and statistics" }
  - { number: "3.9", order: 107, componentType: area, parent: "section 3", heading: "Areas of Mathematics, Statistics and Operational Research", gloss: "knowledge of a range of areas (S4)" }
  - { number: "3.10", order: 108, componentType: area, parent: "section 3", heading: "Areas of Mathematics, Statistics and Operational Research", gloss: "mathematics courses: example topics" }
  - { number: "3.11", order: 109, componentType: area, parent: "section 3", heading: "Areas of Mathematics, Statistics and Operational Research", gloss: "statistics courses: example topics; using a statistical package (S4)" }
  - { number: "3.12", order: 110, componentType: area, parent: "section 3", heading: "Areas of Mathematics, Statistics and Operational Research", gloss: "operational research courses: application fields" }
  - { number: "3.13", order: 111, componentType: area, parent: "section 3", heading: "Mathematical thinking and logical processes", gloss: "assumptions, their validity and their ethics" }
  - { number: "3.14", order: 112, componentType: area, parent: "section 3", heading: "Mathematical thinking and logical processes", gloss: "generalisation, abstraction, proof and problem-solving" }
  - { number: "3.15", order: 113, componentType: paragraph, parent: "section 3", heading: "Mathematical thinking and logical processes", gloss: "axiomatic approaches and modelling" }
  - { number: "3.16", order: 114, componentType: area, parent: "section 3", heading: "Numerical computation", gloss: "numerical approximation and its pitfalls" }
  - { number: "3.17", order: 115, componentType: area, parent: "section 3", heading: "Numerical computation", gloss: "programming and specialist software (S4)" }
  - { number: "3.18", order: 116, componentType: area, parent: "section 3", heading: "Modelling", gloss: "modelling expected of all graduates (S4)" }
  - { number: "3.19", order: 117, componentType: area, parent: "section 3", heading: "Modelling", gloss: "modelling techniques, validation and communication" }
  - { number: "3.20", order: 118, componentType: area, parent: "section 3", heading: "Related areas", gloss: "related content: history, education, careers" }
  - { number: "3.21", order: 119, componentType: area, parent: "section 3", heading: "Depth of study", gloss: "depth of study and course titles" }
  - { number: "3.22", order: 120, componentType: paragraph, parent: "section 3", heading: "Subject-specific skills", gloss: "subject-specific skills for later use" }
  - { number: "3.23", order: 121, componentType: paragraph, parent: "section 3", heading: "Subject-specific skills", gloss: "a problem-based subject" }
  - { number: "3.24", order: 122, componentType: stem, parent: "section 3", heading: "Subject-specific skills", gloss: "branch skills: mathematics, statistics, operational research" }
  - { number: "3.25", order: 123, componentType: paragraph, parent: "section 3", heading: "General skills", gloss: "general skills and transfer between contexts" }
  - { number: "3.26", order: 124, componentType: stem, parent: "section 3", heading: "General skills", gloss: "general skills expected of all graduates (S4)" }
  - { number: "3.27", order: 125, componentType: paragraph, parent: "section 3", heading: "General skills", gloss: "summary of graduate attributes" }
  - { number: "3.28", order: 126, componentType: practice, parent: "section 3", heading: "Teaching and learning", gloss: "choosing teaching approaches (S4)" }
  - { number: "3.29", order: 127, componentType: practice, parent: "section 3", heading: "Teaching and learning", gloss: "lectures, tutorials, laboratories and active learning" }
  - { number: "3.30", order: 128, componentType: practice, parent: "section 3", heading: "Teaching and learning", gloss: "advance materials, practice exercises and open problems" }
  - { number: "3.31", order: 129, componentType: practice, parent: "section 3", heading: "Teaching and learning", gloss: "revisiting topics in a cumulative subject" }
  - { number: "3.32", order: 130, componentType: practice, parent: "section 3", heading: "Teaching and learning", gloss: "peer learning and spaces for it (S4)" }
  - { number: "3.33", order: 131, componentType: practice, parent: "section 3", heading: "Teaching and learning", gloss: "extra support and mathematics support services" }
  - { number: "3.34", order: 132, componentType: paragraph, parent: "section 3", heading: "Teaching and learning", gloss: "shared responsibility for independent learners (S4)" }
  - { number: "3.35", order: 133, componentType: paragraph, parent: "section 3", heading: "Teaching and learning", gloss: "equipping students to learn on their own (S4)" }
  - { number: "3.36", order: 134, componentType: practice, parent: "section 3", heading: "Teaching and learning", gloss: "study skills, scholarly habits and time to consolidate (S4)" }
  - { number: "3.37", order: 135, componentType: practice, parent: "section 3", heading: "Teaching and learning", gloss: "teaching spaces and boards" }
  - { number: "3.38", order: 136, componentType: practice, parent: "section 3", heading: "Teaching and learning", gloss: "technology in teaching, including automated feedback" }
  - { number: "3.39", order: 137, componentType: stem, parent: "section 3", heading: "Teaching and learning", gloss: "computing across the course; programming and software (S4)" }
  - { number: "3.40", order: 138, componentType: stem, parent: "section 3", heading: "Teaching and learning", gloss: "learning materials" }
  - { number: "3.41", order: 139, componentType: paragraph, parent: "section 3", heading: "Teaching and learning", gloss: "bespoke resources kept up to date" }
  - { number: "3.42", order: 140, componentType: paragraph, parent: "section 3", heading: "Teaching and learning", gloss: "staff training and professional development (S4)" }
  - { number: "3.43", order: 141, componentType: paragraph, parent: "section 3", heading: "Teaching and learning", gloss: "engaging with quality assurance (S4)" }
  - { number: "3.44", order: 142, componentType: stem, parent: "section 3", heading: "Assessment", gloss: "what assessment sets out to establish" }
  - { number: "3.45", order: 143, componentType: stem, parent: "section 3", heading: "Assessment", gloss: "wider abilities summative assessment may test" }
  - { number: "3.46", order: 144, componentType: practice, parent: "section 3", heading: "Assessment", gloss: "formative feedback" }
  - { number: "3.47", order: 145, componentType: paragraph, parent: "section 3", heading: "Assessment", gloss: "general characteristics as outcomes; EDI in assessment design (S4)" }
  - { number: "3.48", order: 146, componentType: practice, parent: "section 3", heading: "Assessment", gloss: "varied methods; accessible and inclusive assessment (S4)" }
  - { number: "3.49", order: 147, componentType: paragraph, parent: "section 3", heading: "Assessment", gloss: "practice matched to assessment formats" }
  - { number: "3.50", order: 148, componentType: practice, parent: "section 3", heading: "Assessment", gloss: "professional judgement in marking" }
  - { number: "3.51", order: 149, componentType: practice, parent: "section 3", heading: "Assessment", gloss: "controlled conditions and academic integrity" }
  - { number: "3.52", order: 150, componentType: practice, parent: "section 3", heading: "Assessment", gloss: "full mark range; uneven module results; whole-course judgement" }
  - { number: "4.1", order: 152, componentType: paragraph, parent: "section 4", heading: "Introduction", gloss: "standards stated in general terms" }
  - { number: "4.2", order: 153, componentType: paragraph, parent: "section 4", heading: "Introduction", gloss: "threshold standards for honours, integrated and taught master's; met overall" }
  - { number: "4.3", order: 154, componentType: paragraph, parent: "section 4", heading: "Introduction", gloss: "a reference point for data science and joint courses" }
  - { number: "4.4", order: 155, componentType: paragraph, parent: "section 4", heading: "Introduction", gloss: "above-threshold performance, Annex D and master's outcomes (S4)" }
  - { number: "4.5", order: 156, componentType: stem, parent: "section 4", heading: "Academic standards", gloss: "threshold for the bachelor's degree with honours (S4)" }
  - { number: "4.6", order: 157, componentType: stem, parent: "section 4", heading: "Academic standards", gloss: "threshold for the integrated master's degree (S4)" }
  - { number: "4.7", order: 158, componentType: paragraph, parent: "section 4", heading: "Academic standards", gloss: "taught master's develop some or all standards (S4)" }
  - { number: "4.8", order: 159, componentType: stem, parent: "section 4", heading: "Academic standards", gloss: "bases on which achievement above threshold shows" }
  - { number: "4.9", order: 160, componentType: stem, parent: "section 4", heading: "Professional standards", gloss: "professional standards (S4)" }
  - { number: "4.10", order: 161, componentType: paragraph, parent: "section 4", heading: "Professional standards", gloss: "master's level: deeper experience and independence (S4)" }
  - { number: "1", componentType: section, parent: none, heading: "Context and purposes of a Mathematics, Statistics and Operational Research degree", gloss: "section 1" }
  - { number: "2", componentType: section, parent: none, heading: "Distinctive features of MSOR courses", gloss: "section 2" }
  - { number: "3", componentType: section, parent: none, heading: "Content, structure and delivery", gloss: "section 3" }
  - { number: "4", componentType: section, parent: none, heading: "Benchmark standards", gloss: "section 4" }
excluded:
  - { number: "none", heading: "Contents; About this Statement; How can I use this document?; Relationship to legislation; Additional sector reference points", kind: "other: front matter, read for S1, S2 and SB6" }
  - { number: "none", heading: "section heading lines (1 to 4)", kind: "other: headings, recorded in SECTIONS" }
  - { number: "5", heading: "List of references and further resources", kind: "other: references, read for SB6" }
  - { number: "6", heading: "Membership of the Advisory Groups for the Subject Benchmark Statement for Mathematics, Statistics and Operational Research", kind: "other: membership and edition history, read for S1 and S7 (fifth edition, published 8 March 2023)" }
```

### S4 Statements
<!-- label: both; status: drafted; basis: primary. Only standards (D-std-0002 (a)): 76 records. `source` is the issuer's statement exactly as its span holds it (D-std-0014). -->
```yaml
- id: qaa/mathematics-statistics-and-operational-research-2023/1.10
  locator: { number: "1.10", headingPath: ["Context and purposes of a Mathematics, Statistics and Operational Research degree", "Context and purposes of a Mathematics, Statistics and Operational Research degree"] }
  span: { start: 14371, end: 15257 }
  source: "1.10 MSOR course curricula form a broad spectrum of styles. To meet students’ needs, courses may combine or focus more on one of these styles. At one end of the spectrum are 'theory-based courses' that are concerned with the way in which theory establishes general propositions leading to methods and techniques which can then be applied to a range of problems. At the other end are 'practice-based courses' that cover the understanding and application of results, methods and techniques to a variety of situations in different contexts. The subject’s interdisciplinary nature means courses may apply theory and practice to areas both within and outside MSOR. Providers should take steps to ensure that all MSOR graduates, whatever the nature of the course they have studied, are able to fully identify as professional MSOR practitioners. Purposes and characteristics of an MSOR degree\n"
  stem: none
  statementType: expectation
  rung: none
  force: should
  level: none
  appliesTo: "courses of every style, theory-based to practice-based"
  addressee: provider
  verbs: ["take", "ensure", "identify"]
  about: "every graduate able to identify as a practitioner"
  themes: [none]
  domain: none
  award: ["bachelor's with honours", "integrated master's", "master's"]
  gradeOf: none
  paraphrase: "Whatever the style of course, from theory-based to practice-based, providers should act so that every graduate can see themselves fully as a professional practitioner of the subject."
  quote: full   # the issuer's statement is in `source` (D-std-0014)
  audience: practitioner
  subjects: inherited
- id: qaa/mathematics-statistics-and-operational-research-2023/1.23
  locator: { number: "1.23", headingPath: ["Context and purposes of a Mathematics, Statistics and Operational Research degree", "Equality, diversity and inclusion"] }
  span: { start: 21902, end: 22459 }
  source: "1.23 Values of EDI should permeate the curriculum and every aspect of the learning experience to ensure the diverse nature of society in all its forms is evident. MSOR providers should reflect on their curricula and processes to ensure that no group is disadvantaged or othered; for example, by reflecting on how policies and practices around delivery, admission and assessment might adversely impact on certain subgroups within the student cohort. EDI aspects of student engagement and achievement should be monitored, and actions formed to ensure equity.\n"
  stem: none
  statementType: expectation
  rung: none
  force: should
  level: none
  appliesTo: "curricula, processes and monitoring"
  addressee: provider
  verbs: ["permeate", "reflect", "ensure", "monitored"]
  about: "EDI through curriculum, processes and monitoring"
  themes: [theme:edi]
  domain: none
  award: ["bachelor's with honours", "integrated master's", "master's"]
  gradeOf: none
  paraphrase: "Equality, diversity and inclusion should run through the curriculum and the whole learning experience; providers should examine curricula and processes, delivery, admissions and assessment among them, so no group is disadvantaged, and should monitor engagement and achievement by group and act on the results."
  quote: full   # the issuer's statement is in `source` (D-std-0014)
  audience: practitioner
  subjects: inherited
- id: qaa/mathematics-statistics-and-operational-research-2023/1.25
  locator: { number: "1.25", headingPath: ["Context and purposes of a Mathematics, Statistics and Operational Research degree", "Equality, diversity and inclusion"] }
  span: { start: 22854, end: 24065 }
  source: "1.25 There is active discussion in higher education on the topic of decolonising the curriculum, and this topic is relevant to MSOR. Though there is no suggestion of omitting or censoring core discipline content, MSOR subjects are not neutral nor detached from society, and explicit reflection on the history and practice of MSOR knowledge generation can be useful in attempting to avoid unconscious biases in course design and delivery. While presenting the positive contributions that MSOR disciplines have made, provision might also reflect the fact that such contributions sometimes arose from cultural contexts with issues that would now be considered problematic. For example, some early ideas in statistics were motivated by their proposers’ support for eugenics, some astronomical data were collected\n\n7\non plantations by enslaved people, and, historically, some mathematicians have recorded racist or fascist views or connections to groups such as the Nazis. Further, there are historical and ongoing issues around power dynamics and gatekeeping in both access to and generation of MSOR knowledge. Providers should review their practices, in line with paragraph 1.23, with an explicit focus on equity.\n"
  stem: none
  statementType: expectation
  rung: none
  force: should
  level: none
  appliesTo: "curricula and practice"
  addressee: provider
  verbs: ["review"]
  about: "decolonising the curriculum; equity review"
  themes: [theme:edi]
  domain: none
  award: ["bachelor's with honours", "integrated master's", "master's"]
  gradeOf: none
  paraphrase: "Decolonising the curriculum is a live question for the subject; without dropping core content, provision might reflect the troubled settings some contributions came from and the gatekeeping around knowledge, and providers should review their practices with equity as the explicit focus, as 1.23 sets out."
  quote: full   # the issuer's statement is in `source` (D-std-0014)
  audience: practitioner
  subjects: inherited
- id: qaa/mathematics-statistics-and-operational-research-2023/1.28
  locator: { number: "1.28", headingPath: ["Context and purposes of a Mathematics, Statistics and Operational Research degree", "Accessibility"] }
  span: { start: 28986, end: 29622 }
  source: "1.28 In order to ensure an accessible course experience, providers should anticipate their learners’ needs and proactively ensure that these are met. Providing institutions should support MSOR staff to overcome discipline-specific barriers to accessibility (see paragraphs\n1.34 to 1.36) that can significantly increase staff time creating accessible resources and content. Provider good practice in this area may include support staff with disciplinary and technology knowledge, MSOR-accessibility-specific training, consideration of MSOR needs in policymaking, or ensuring learning tools adequately meet the needs of MSOR disciplines.\n"
  stem: none
  statementType: expectation
  rung: none
  force: should
  level: none
  appliesTo: "providers and their institutions"
  addressee: provider
  verbs: ["anticipate", "ensure", "support", "overcome"]
  about: "anticipatory accessibility and support for subject staff"
  themes: [theme:accessibility]
  domain: none
  award: ["bachelor's with honours", "integrated master's", "master's"]
  gradeOf: none
  paraphrase: "For an accessible course, providers should foresee what learners will need and meet it in advance, and institutions should help subject staff past the barriers peculiar to the subject, which can add much to the time spent making materials accessible."
  quote: full   # the issuer's statement is in `source` (D-std-0014)
  audience: practitioner
  subjects: inherited
- id: qaa/mathematics-statistics-and-operational-research-2023/1.29
  locator: { number: "1.29", headingPath: ["Context and purposes of a Mathematics, Statistics and Operational Research degree", "Accessibility"] }
  span: { start: 29622, end: 30054 }
  source: "1.29 Providers should consider the challenges and barriers that need to be overcome to successfully empower their students to be full participants in their own education and academic communities. The diverse nature of MSOR courses and individual modules within courses means these challenges and barriers should be considered both at course level and within modules to create a coherent and consistent approach to accessibility.\n\n9\n"
  stem: none
  statementType: expectation
  rung: none
  force: should
  level: none
  appliesTo: "course and module design"
  addressee: provider
  verbs: ["consider", "empower"]
  about: "barriers to participation at course and module level"
  themes: [theme:accessibility]
  domain: none
  award: ["bachelor's with honours", "integrated master's", "master's"]
  gradeOf: none
  paraphrase: "Providers should think through the barriers that stop students taking a full part in their education and academic communities, at course level and inside modules, so accessibility is handled coherently and consistently."
  quote: full   # the issuer's statement is in `source` (D-std-0014)
  audience: practitioner
  subjects: inherited
- id: qaa/mathematics-statistics-and-operational-research-2023/1.30
  locator: { number: "1.30", headingPath: ["Context and purposes of a Mathematics, Statistics and Operational Research degree", "Accessibility"] }
  span: { start: 30054, end: 30317 }
  source: "1.30 In addition, it is imperative that providers anticipate the discipline-specific digital, physical and pedagogical accessibility needs of disabled students, embedding accessibility in a manner that minimises or eliminates the need for reasonable adjustments.\n"
  stem: none
  statementType: expectation
  rung: none
  force: must   # D-std-0016: "imperative" read as must
  level: none
  appliesTo: "providers"
  addressee: provider
  verbs: ["anticipate", "embedding", "minimises", "eliminates"]
  about: "embedding accessibility so adjustments are rarely needed"
  themes: [theme:accessibility]
  domain: none
  award: ["bachelor's with honours", "integrated master's", "master's"]
  gradeOf: none
  paraphrase: "It is essential that providers foresee disabled students' subject-specific digital, physical and teaching needs and build accessibility in, so that reasonable adjustments are needed as little as possible or not at all."
  quote: full   # the issuer's statement is in `source` (D-std-0014)
  audience: practitioner
  subjects: inherited
- id: qaa/mathematics-statistics-and-operational-research-2023/1.33
  locator: { number: "1.33", headingPath: ["Context and purposes of a Mathematics, Statistics and Operational Research degree", "Accessibility"] }
  span: { start: 30955, end: 31386 }
  source: "1.33 Providers should seek to ensure that their courses are well curated. Well-curated courses benefit all students by promoting good mental health and well-being and reduce the administrative burden and cognitive load on disabled students. Well-curated courses include clearly communicated learning opportunities, assessments that are appropriately spaced and particular support when concepts and skills are initially introduced.\n"
  stem: none
  statementType: expectation
  rung: none
  force: should
  level: none
  appliesTo: "course curation"
  addressee: provider
  verbs: ["seek", "ensure"]
  about: "well-curated courses"
  themes: [theme:accessibility]
  domain: none
  award: ["bachelor's with honours", "integrated master's", "master's"]
  gradeOf: none
  paraphrase: "Providers should aim for well-curated courses, which help every student's mental health and lighten the administrative and cognitive load on disabled students, through clear communication of learning opportunities, well-spaced assessment and extra support when new ideas first appear."
  quote: full   # the issuer's statement is in `source` (D-std-0014)
  audience: practitioner
  subjects: inherited
- id: qaa/mathematics-statistics-and-operational-research-2023/1.36.b1
  locator: { number: "1.36.b1", headingPath: ["Context and purposes of a Mathematics, Statistics and Operational Research degree", "Accessibility"] }
  span: { start: 32934, end: 33171 }
  source: "providers should acknowledge the special needs of MSOR and the deficiencies in many adaptive features of mainstream technology by providing additional resources which may not be needed by subjects where the medium is primarily text based"
  stem: "1.36"
  statementType: expectation
  rung: none
  force: should
  level: none
  appliesTo: "providers"
  addressee: provider
  verbs: ["acknowledge", "providing"]
  about: "extra resources where assistive technology fails"
  themes: [theme:accessibility]
  domain: none
  award: ["bachelor's with honours", "integrated master's", "master's"]
  gradeOf: none
  paraphrase: "Because mainstream assistive technology handles mathematical content poorly, providers should recognise the subject's particular needs and supply extra resources that mostly text-based subjects may not need."
  quote: full   # the issuer's statement is in `source` (D-std-0014)
  audience: practitioner
  subjects: inherited
- id: qaa/mathematics-statistics-and-operational-research-2023/1.37
  locator: { number: "1.37", headingPath: ["Context and purposes of a Mathematics, Statistics and Operational Research degree", "Accessibility"] }
  span: { start: 33492, end: 33943 }
  source: "1.37 Including elements of online, hybrid or blended learning across courses can significantly increase access for students, as can, where appropriate, the provision of captured content fro m in-person sessions. Associated enabling technology is required to capture the live display of extended written material and ensure accurate captions. Within a physical venue, consideration of the visibility of boards and other display equipment is essential.\n"
  stem: none
  statementType: requirement
  rung: none
  force: must
  level: none
  appliesTo: "captured, online and in-person delivery"
  addressee: provider
  verbs: ["increase", "capture", "ensure"]
  about: "capture, captions and visibility"
  themes: [theme:accessibility]
  domain: none
  award: ["bachelor's with honours", "integrated master's", "master's"]
  gradeOf: none
  paraphrase: "Online, hybrid or blended elements and captured sessions can widen access; suitable technology must be in place to capture live written work and caption it accurately, and in the room boards and displays must be visible."
  quote: full   # the issuer's statement is in `source` (D-std-0014)
  audience: practitioner
  subjects: inherited
- id: qaa/mathematics-statistics-and-operational-research-2023/1.38
  locator: { number: "1.38", headingPath: ["Context and purposes of a Mathematics, Statistics and Operational Research degree", "Accessibility"] }
  span: { start: 33943, end: 34191 }
  source: "1.38 Those in support roles, including scribes, notetakers, readers and communication support workers, need to have an understanding of MSOR terminology and symbolism since even minor symbolic differences can radically change the intended meaning.\n"
  stem: none
  statementType: requirement
  rung: none
  force: must   # D-std-0016: "need to" read as must
  level: none
  appliesTo: "those in support roles"
  addressee: provider
  verbs: ["need"]
  about: "support workers knowing subject terminology"
  themes: [theme:accessibility]
  domain: none
  award: ["bachelor's with honours", "integrated master's", "master's"]
  gradeOf: none
  paraphrase: "Scribes, notetakers, readers, communication support workers and others in support roles need to know the subject's terms and symbols, because a small change in a symbol can alter the meaning entirely."
  quote: full   # the issuer's statement is in `source` (D-std-0014)
  audience: practitioner
  subjects: inherited
- id: qaa/mathematics-statistics-and-operational-research-2023/1.42
  locator: { number: "1.42", headingPath: ["Context and purposes of a Mathematics, Statistics and Operational Research degree", "Accessibility"] }
  span: { start: 35379, end: 35822 }
  source: "1.42 Assessment design should anticipate and remove potentially irrelevant or context- dependent barriers that are irrelevant to knowledge, skills or abilities measured by the assessment. For example, consideration should be given to whether a student will spend disproportionate time and effort interpreting material; be exposed to distracting and needless imagery; be unfamiliar with the assumed context, customs or colloquialism of a task.\n"
  stem: none
  statementType: expectation
  rung: none
  force: should
  level: none
  appliesTo: "assessment design"
  addressee: provider
  verbs: ["anticipate", "remove"]
  about: "removing irrelevant barriers in assessment"
  themes: [theme:accessibility]
  domain: none
  award: ["bachelor's with honours", "integrated master's", "master's"]
  gradeOf: none
  paraphrase: "Assessment design should foresee and remove barriers unrelated to what is being measured, such as heavy interpretation of material, distracting images or unfamiliar context, customs or colloquial language."
  quote: full   # the issuer's statement is in `source` (D-std-0014)
  audience: practitioner
  subjects: inherited
- id: qaa/mathematics-statistics-and-operational-research-2023/1.50
  locator: { number: "1.50", headingPath: ["Context and purposes of a Mathematics, Statistics and Operational Research degree", "Enterprise and entrepreneurship education"] }
  span: { start: 40827, end: 41252 }
  source: "1.50 Preparing students of MSOR to move successfully from education into employment is an essential part of a degree course. While there is a personal responsibility for students to take ownership of their career development, and other departments within institutions will provide support, development of employability skills should be embedded into MSOR courses, including through enterprise and entrepreneurship education.\n"
  stem: none
  statementType: expectation
  rung: none
  force: should
  level: none
  appliesTo: "courses"
  addressee: provider
  verbs: ["embedded"]
  about: "employability embedded in the course"
  themes: [theme:enterprise]
  domain: none
  award: ["bachelor's with honours", "integrated master's", "master's"]
  gradeOf: none
  paraphrase: "Helping students into work is an essential part of the degree; students own their career development and other services help, but employability skills should be built into the course, enterprise and entrepreneurship education included."
  quote: full   # the issuer's statement is in `source` (D-std-0014)
  audience: practitioner
  subjects: inherited
- id: qaa/mathematics-statistics-and-operational-research-2023/1.55
  locator: { number: "1.55", headingPath: ["Context and purposes of a Mathematics, Statistics and Operational Research degree", "Enterprise and entrepreneurship education"] }
  span: { start: 42595, end: 43369 }
  source: "1.55 Modules such as a final dissertation or project can foster a student’s ability to reflect, take responsibility and take risks in a supervised environment. Modules enabling students to work in groups can provide opportunities for developing and improving skills in influencing, leadership, negotiation and communication. In advance of any group work, students should be supported in developing an appreciation of the differences between working individually and working with others, group management and general good group working behaviours. An ability to work with and interrogate large data sets is key to successful entrepreneurship and enterprise and a module that provides this opportunity will enable students to develop many of the competencies mentioned above.\n"
  stem: none
  statementType: expectation
  rung: none
  force: should
  level: none
  appliesTo: "group work and projects"
  addressee: provider
  verbs: ["supported", "foster"]
  about: "preparing students for group work"
  themes: [theme:enterprise]
  domain: none
  award: ["bachelor's with honours", "integrated master's", "master's"]
  gradeOf: none
  paraphrase: "Projects and dissertations build reflection, responsibility and supervised risk-taking, and group modules build influencing, leadership, negotiation and communication; before group work, students should be supported to understand how working with others differs from working alone and how good groups behave."
  quote: full   # the issuer's statement is in `source` (D-std-0014)
  audience: practitioner
  subjects: inherited
- id: qaa/mathematics-statistics-and-operational-research-2023/1.60
  locator: { number: "1.60", headingPath: ["Context and purposes of a Mathematics, Statistics and Operational Research degree", "Enterprise and entrepreneurship education"] }
  span: { start: 45174, end: 45480 }
  source: "1.60 In order for graduates to build on these skills in their future career or further studies they need to be able to reflect, understand and articulate how their degree has given them the opportunities to develop many areas of entrepreneurship and enterprise as well as general employability skills.\n\n14\n"
  stem: none
  statementType: outcome
  rung: none
  force: must   # D-std-0016: "need to" read as must
  level: fheq:6
  appliesTo: "graduates of the subject"
  addressee: learner
  verbs: ["reflect", "understand", "articulate", "build"]
  about: "explaining enterprise and employability development"
  themes: [theme:enterprise]
  domain: generic-skill
  award: ["bachelor's with honours", "integrated master's"]
  gradeOf: none
  paraphrase: "To build on these skills later in work or study, graduates need to be able to reflect on, understand and explain how their degree let them develop enterprise, entrepreneurship and wider employability skills."
  quote: full   # the issuer's statement is in `source` (D-std-0014)
  audience: both
  subjects: inherited
- id: qaa/mathematics-statistics-and-operational-research-2023/2.5
  locator: { number: "2.5", headingPath: ["Distinctive features of MSOR courses", "Design"] }
  span: { start: 47912, end: 48420 }
  source: "2.5 Undergraduates in MSOR may choose to study a standard bachelor’s degree with honours (FHEQ Level 6; FQHEIS Level 10) or an integrated master’s degree with honours (FHEQ Level 7; FQHEIS Level 11). These each have distinct learning outcomes to reflect the level of the award. Bachelor’s degrees should provide students with the subject-specific knowledge, understanding and skills, as well as the wider transferable skills and attributes that prepare graduates for a wide range of careers in many sectors.\n"
  stem: none
  statementType: expectation
  rung: none
  force: should
  level: fheq:6
  appliesTo: "bachelor's degrees with honours"
  addressee: provider
  verbs: ["provide", "prepare"]
  about: "what a bachelor's degree should give students"
  themes: [none]
  domain: none
  award: ["bachelor's with honours"]
  gradeOf: none
  paraphrase: "Undergraduates may take a bachelor's degree with honours (FHEQ 6, FQHEIS 10) or an integrated master's with honours (FHEQ 7, FQHEIS 11), each with its own outcomes; bachelor's degrees should give students subject knowledge, understanding and skills and wider transferable skills that equip them for many careers."
  quote: full   # the issuer's statement is in `source` (D-std-0014)
  audience: practitioner
  subjects: inherited
- id: qaa/mathematics-statistics-and-operational-research-2023/2.9
  locator: { number: "2.9", headingPath: ["Distinctive features of MSOR courses", "Design"] }
  span: { start: 50528, end: 51280 }
  source: "2.9 Both bachelor's and integrated master’s degrees may include such periods of study, and this may or may not extend the period of the degree, depending on the expected learning undertaken during that period. Credit awarded during such study also varies according to the learning and assessment workload during the experience. Credit-bearing placements (see paragraph 2.27 in the Partnership section) should, however, be integrated within the programme of study, so that students can relate their experience to, and use the skills that they have developed in, their academic study. Many providers also offer or facilitate non-credit-bearing industrial and research placement experiences during vacations to enhance student experience and development.\n"
  stem: none
  statementType: expectation
  rung: none
  force: should
  level: none
  appliesTo: "credit-bearing placements"
  addressee: provider
  verbs: ["integrated", "relate", "use"]
  about: "integrating credit-bearing placements"
  themes: [none]
  domain: none
  award: ["bachelor's with honours", "integrated master's"]
  gradeOf: none
  paraphrase: "Bachelor's and integrated master's degrees may include study away from the institution, with credit set by the workload; where a placement carries credit it should be built into the programme so students can link the experience to their academic study."
  quote: full   # the issuer's statement is in `source` (D-std-0014)
  audience: practitioner
  subjects: inherited
- id: qaa/mathematics-statistics-and-operational-research-2023/2.11
  locator: { number: "2.11", headingPath: ["Distinctive features of MSOR courses", "Design"] }
  span: { start: 51743, end: 52150 }
  source: "2.11 The academic component of integrated degree apprenticeships in MSOR should follow the guidelines in this Subject Benchmark Statement. Degree apprenticeships in higher education are covered explicitly in the Characteristics Statement for Higher Education in Apprenticeships which describes the general characteristics and distinctive features of higher and degree apprenticeships in the UK. Progression\n"
  stem: none
  statementType: expectation
  rung: none
  force: should
  level: none
  appliesTo: "integrated degree apprenticeships"
  addressee: provider
  verbs: ["follow"]
  about: "apprenticeships follow this statement"
  themes: [none]
  domain: none
  award: ["bachelor's with honours", "integrated master's"]
  gradeOf: none
  paraphrase: "The academic part of an integrated degree apprenticeship in the subject should follow this statement's guidance; degree apprenticeships are described more fully in QAA's Characteristics Statement on apprenticeships."
  quote: full   # the issuer's statement is in `source` (D-std-0014)
  audience: practitioner
  subjects: inherited
- id: qaa/mathematics-statistics-and-operational-research-2023/2.12
  locator: { number: "2.12", headingPath: ["Distinctive features of MSOR courses", "Progression"] }
  span: { start: 52150, end: 53202 }
  source: "2.12 Over the course of a bachelor’s degree with honours (FHEQ Level 6; FQHEIS Level 10) or an integrated master’s degree (FHEQ Level 7; FQHEIS Level 11), an MSOR student will progress from one level of study to the next, in line with the regulations and processes for each institution. However, it is expected that each level would see the attainment of knowledge, expertise and experience that build towards the final achievement of meeting at least the threshold-level subject-specific and generic skills listed in this Statement. This would include successful completion and the award of credit for the full range of learning and assessment. Upon graduation from an undergraduate degree, it would be expected that a student who has achieved a second-class degree or higher would be capable of, and equipped for, undertaking postgraduate study in MSOR or an associated discipline. Entry requirements to postgraduate courses are, however, determined by individual providers and may require specified levels of achievement at undergraduate level.\n\n16\n"
  stem: none
  statementType: expectation
  rung: none
  force: must   # D-std-0016: "requirements" read as must
  level: fheq:6
  appliesTo: "undergraduates progressing through their course"
  addressee: learner
  verbs: ["progress", "meeting"]
  about: "progression towards threshold; readiness for postgraduate study"
  themes: [none]
  domain: none
  award: ["bachelor's with honours", "integrated master's"]
  gradeOf: none
  paraphrase: "Students move up the levels of a bachelor's or integrated master's under their institution's rules; each level is expected to build towards reaching at least the threshold subject-specific and generic skills by the end, and a student with a second-class degree or better is expected to be ready for postgraduate study."
  quote: full   # the issuer's statement is in `source` (D-std-0014)
  audience: both
  subjects: inherited
- id: qaa/mathematics-statistics-and-operational-research-2023/2.13
  locator: { number: "2.13", headingPath: ["Distinctive features of MSOR courses", "Progression"] }
  span: { start: 53202, end: 53374 }
  source: "2.13 Undergraduates studying joint honours or interdisciplinary courses will achieve core elements of the specific and generic skills for each subject (see paragraph 2.7).\n"
  stem: none
  statementType: outcome
  rung: none
  force: will
  level: fheq:6
  appliesTo: "joint honours and interdisciplinary undergraduates"
  addressee: learner
  verbs: ["achieve"]
  about: "core skills of each subject in a combination"
  themes: [none]
  domain: subject-skill
  award: ["bachelor's with honours", "integrated master's"]
  gradeOf: none
  paraphrase: "Students on joint honours or interdisciplinary courses will reach the core of the specific and general skills of each subject they combine."
  quote: full   # the issuer's statement is in `source` (D-std-0014)
  audience: both
  subjects: inherited
- id: qaa/mathematics-statistics-and-operational-research-2023/2.18
  locator: { number: "2.18", headingPath: ["Distinctive features of MSOR courses", "Flexibility"] }
  span: { start: 54704, end: 54914 }
  source: "2.18 MSOR students should also have flexibility to select some optional modules in alignment with their interests, and therefore appropriate guidance on option choices should be made available to the students.\n"
  stem: none
  statementType: expectation
  rung: none
  force: should
  level: none
  appliesTo: "option choices"
  addressee: provider
  verbs: ["have", "select", "made"]
  about: "optional modules and guidance"
  themes: [none]
  domain: none
  award: ["bachelor's with honours", "integrated master's"]
  gradeOf: none
  paraphrase: "Students should have some freedom to choose optional modules that suit their interests, and suitable advice on those choices should be available."
  quote: full   # the issuer's statement is in `source` (D-std-0014)
  audience: practitioner
  subjects: inherited
- id: qaa/mathematics-statistics-and-operational-research-2023/2.24
  locator: { number: "2.24", headingPath: ["Distinctive features of MSOR courses", "Flexibility"] }
  span: { start: 56887, end: 57242 }
  source: "2.24 MSOR courses should be sufficiently flexible to be able to respond to and anticipate change, in the advancement of the subject and its interface with other disciplines, as well as in the needs of its graduates and their employers. They should also take account of learners’ needs and make appropriate reasonable adjustments, as required. Partnership\n"
  stem: none
  statementType: expectation
  rung: none
  force: should
  level: none
  appliesTo: "courses"
  addressee: provider
  verbs: ["respond", "anticipate", "take", "make"]
  about: "courses flexible to change and to learners"
  themes: [none]
  domain: none
  award: ["bachelor's with honours", "integrated master's", "master's"]
  gradeOf: none
  paraphrase: "Courses should be flexible enough to respond to, and anticipate, change in the subject, its links with other disciplines and the needs of graduates and employers, and should take account of learners' needs, making reasonable adjustments where required."
  quote: full   # the issuer's statement is in `source` (D-std-0014)
  audience: practitioner
  subjects: inherited
- id: qaa/mathematics-statistics-and-operational-research-2023/2.30
  locator: { number: "2.30", headingPath: ["Distinctive features of MSOR courses", "Partnership"] }
  span: { start: 58975, end: 59797 }
  source: "2.30 Students gain numerous benefits from working with employers on placements or projects (see paragraph 1.59). Work-related projects may involve employers posing problems for students to work on which have arisen or are inspired by the business of the employer. Some of these are detailed in paragraph 1.57. Any partnership with a potential employer or professional organisation can lead to input into curriculum design or other activities that enhance the curriculum as well as students’ employability and graduate outcomes. Some providers offer degree apprenticeships, for example in data science, in conjunction with employers. Providers should develop processes for oversight to ensure that partners involved in degree delivery meet all relevant safeguards, quality standards and expectations. Monitoring and review\n"
  stem: none
  statementType: expectation
  rung: none
  force: should
  level: none
  appliesTo: "delivery partners"
  addressee: provider
  verbs: ["develop", "ensure", "meet"]
  about: "oversight of partners in delivery"
  themes: [none]
  domain: none
  award: ["bachelor's with honours", "integrated master's", "master's"]
  gradeOf: none
  paraphrase: "Work with employers brings students many benefits and can shape the curriculum; where partners take part in delivering a degree, providers should set up oversight so the partners meet each relevant safeguard, quality standard and expectation."
  quote: full   # the issuer's statement is in `source` (D-std-0014)
  audience: practitioner
  subjects: inherited
- id: qaa/mathematics-statistics-and-operational-research-2023/3.2
  locator: { number: "3.2", headingPath: ["Content, structure and delivery", "Content: Introduction"] }
  span: { start: 61999, end: 62715 }
  source: "3.2 Courses develop graduates who have knowledge and skills that are specific to areas within MSOR. In this Subject Benchmark Statement, such knowledge and skills are referred to as subject-specific. At the higher levels of study, this knowledge and these skills naturally vary between graduates because of the different areas of the subject(s) that different students pursue. This diversity, which is a natural feature of the MSOR subject area, is to be welcomed, and must not be restricted in any way. Furthermore, it is dynamic and evolving, as courses develop to encompass new areas of study. It is, however, possible to discern subject-specific knowledge and skills that are demonstrated by all MSOR graduates.\n"
  stem: none
  statementType: requirement
  rung: none
  force: must
  level: none
  appliesTo: "subject-specific knowledge at higher levels"
  addressee: provider
  verbs: ["restricted", "welcomed"]
  about: "variety of advanced subject knowledge"
  themes: [none]
  domain: none
  award: ["bachelor's with honours", "integrated master's", "master's"]
  gradeOf: none
  paraphrase: "Courses build subject-specific knowledge and skills; at higher levels these differ between graduates by what each pursued, and this variety, natural to the subject, is welcome and must not be limited at all, though a core shared by all graduates can be seen."
  quote: full   # the issuer's statement is in `source` (D-std-0014)
  audience: practitioner
  subjects: inherited
- id: qaa/mathematics-statistics-and-operational-research-2023/3.5
  locator: { number: "3.5", headingPath: ["Content, structure and delivery", "Content: Introduction"] }
  span: { start: 63464, end: 63719 }
  source: "3.5 Courses in the MSOR area will also produce graduates who have highly developed skills of a more general kind. Obvious examples are that they should be highly numerate and that most graduates are competent with applications in computing and modelling.\n"
  stem: none
  statementType: outcome
  rung: none
  force: will
  level: fheq:6
  appliesTo: "graduates of the subject"
  addressee: learner
  verbs: ["produce"]
  about: "numeracy, computing and modelling as general skills"
  themes: [none]
  domain: generic-skill
  award: ["bachelor's with honours", "integrated master's"]
  gradeOf: none
  paraphrase: "Courses will also produce graduates with well-developed general skills; plainly they should be highly numerate, and most will be competent with computing and modelling applications."
  quote: full   # the issuer's statement is in `source` (D-std-0014)
  audience: both
  subjects: inherited
- id: qaa/mathematics-statistics-and-operational-research-2023/3.9
  locator: { number: "3.9", headingPath: ["Content, structure and delivery", "Areas of Mathematics, Statistics and Operational Research"] }
  span: { start: 65453, end: 65712 }
  source: "3.9 Courses develop graduates who will have knowledge of a range of areas of MSOR with the level of understanding of derivation of results and their application commensurate with the course’s placement on the spectrum between practice-based and theory-based.\n"
  stem: none
  statementType: outcome
  rung: none
  force: will
  level: fheq:6
  appliesTo: "graduates of the subject"
  addressee: learner
  verbs: ["develop", "have"]
  about: "knowledge of a range of areas"
  themes: [none]
  domain: knowledge
  award: ["bachelor's with honours", "integrated master's"]
  gradeOf: none
  paraphrase: "Courses will give graduates knowledge of a range of areas of the subject, with understanding of how results are derived and applied that matches where the course sits between practice-based and theory-based."
  quote: full   # the issuer's statement is in `source` (D-std-0014)
  audience: both
  subjects: inherited
- id: qaa/mathematics-statistics-and-operational-research-2023/3.11
  locator: { number: "3.11", headingPath: ["Content, structure and delivery", "Areas of Mathematics, Statistics and Operational Research"] }
  span: { start: 66115, end: 66454 }
  source: "3.11 Statistics courses develop graduates who have knowledge of core areas of mathematics and a range of major areas in statistics. Examples may include exploratory data analysis, inference, likelihood, linear models, stochastic processes, time series and data analytics. Graduates are able to use a statistical package for data analysis.\n"
  stem: none
  statementType: outcome
  rung: none
  force: will
  level: fheq:6
  appliesTo: "graduates of statistics courses"
  addressee: learner
  verbs: ["use"]
  about: "using a statistical package"
  themes: [none]
  domain: subject-skill
  award: ["bachelor's with honours", "integrated master's"]
  gradeOf: none
  paraphrase: "Statistics courses give graduates core mathematics and several major statistical areas, such as inference, likelihood, linear modelling, time series, stochastic processes, exploratory work and analytics; graduates are able to analyse data with a statistical package."
  quote: full   # the issuer's statement is in `source` (D-std-0014)
  audience: both
  subjects: inherited
- id: qaa/mathematics-statistics-and-operational-research-2023/3.17
  locator: { number: "3.17", headingPath: ["Content, structure and delivery", "Numerical computation"] }
  span: { start: 68561, end: 69043 }
  source: "3.17 Courses develop graduates who have some knowledge and understanding of programming in service of computation. With computation regularly used in the workplace and familiarity with software packages an essential part of data analysis, graduates will have familiarity with at least one programming language and direct experience of specialist software for the problems being addressed and, when feasible, knowledge of the nature of the algorithms on which it is based. Modelling\n"
  stem: none
  statementType: outcome
  rung: none
  force: will
  level: fheq:6
  appliesTo: "graduates of the subject"
  addressee: learner
  verbs: ["have"]
  about: "programming and specialist software"
  themes: [none]
  domain: subject-skill
  award: ["bachelor's with honours", "integrated master's"]
  gradeOf: none
  paraphrase: "Courses give graduates some knowledge of programming for computation; since computation and software are central to data analysis at work, graduates will be familiar with at least one programming language, will have used specialist software on the problems in hand and, where feasible, will know how its algorithms work."
  quote: full   # the issuer's statement is in `source` (D-std-0014)
  audience: both
  subjects: inherited
- id: qaa/mathematics-statistics-and-operational-research-2023/3.18
  locator: { number: "3.18", headingPath: ["Content, structure and delivery", "Modelling"] }
  span: { start: 69043, end: 69338 }
  source: "3.18 Mathematical and statistical modelling involve abstract representations of processes. All graduates are expected to have some knowledge and understanding of this activity. Generally, the problems come from at least one application area, but they may also come from other areas within MSOR.\n"
  stem: none
  statementType: outcome
  rung: none
  force: must   # D-std-0016: "are expected to" read as must
  level: fheq:6
  appliesTo: "all graduates of the subject"
  addressee: learner
  verbs: ["have"]
  about: "knowledge of modelling"
  themes: [none]
  domain: understanding
  award: ["bachelor's with honours", "integrated master's"]
  gradeOf: none
  paraphrase: "Mathematical and statistical modelling represents processes abstractly; every graduate is expected to know and understand something of modelling, usually through problems from at least one application area."
  quote: full   # the issuer's statement is in `source` (D-std-0014)
  audience: both
  subjects: inherited
- id: qaa/mathematics-statistics-and-operational-research-2023/3.26.b1
  locator: { number: "3.26.b1", headingPath: ["Content, structure and delivery", "General skills"] }
  span: { start: 73505, end: 73576 }
  source: "study skills, particularly including the ability to learn independently"
  stem: "3.26"
  statementType: outcome
  rung: none
  force: describes
  level: fheq:6
  appliesTo: "all graduates of the subject"
  addressee: learner
  verbs: ["learn"]
  about: "study skills and independent learning"
  themes: [none]
  domain: generic-skill
  award: ["bachelor's with honours", "integrated master's"]
  gradeOf: none
  paraphrase: "Expected of all graduates: study skills, above all learning on one's own."
  quote: full   # the issuer's statement is in `source` (D-std-0014)
  audience: both
  subjects: inherited
- id: qaa/mathematics-statistics-and-operational-research-2023/3.26.b2
  locator: { number: "3.26.b2", headingPath: ["Content, structure and delivery", "General skills"] }
  span: { start: 73579, end: 73696 }
  source: "the ability to work independently with patience and persistence, pursuing the solution of a problem to its conclusion"
  stem: "3.26"
  statementType: outcome
  rung: none
  force: describes
  level: fheq:6
  appliesTo: "all graduates of the subject"
  addressee: learner
  verbs: ["work", "pursuing"]
  about: "persistent independent problem-solving"
  themes: [none]
  domain: generic-skill
  award: ["bachelor's with honours", "integrated master's"]
  gradeOf: none
  paraphrase: "Expected of all graduates: working alone with patience and persistence until a problem is solved."
  quote: full   # the issuer's statement is in `source` (D-std-0014)
  audience: both
  subjects: inherited
- id: qaa/mathematics-statistics-and-operational-research-2023/3.26.b3
  locator: { number: "3.26.b3", headingPath: ["Content, structure and delivery", "General skills"] }
  span: { start: 73699, end: 73746 }
  source: "efficient management of processes and deadlines"
  stem: "3.26"
  statementType: outcome
  rung: none
  force: describes
  level: fheq:6
  appliesTo: "all graduates of the subject"
  addressee: learner
  verbs: []
  about: "managing processes and deadlines"
  themes: [none]
  domain: generic-skill
  award: ["bachelor's with honours", "integrated master's"]
  gradeOf: none
  paraphrase: "Expected of all graduates: managing processes and deadlines efficiently."
  quote: full   # the issuer's statement is in `source` (D-std-0014)
  audience: both
  subjects: inherited
- id: qaa/mathematics-statistics-and-operational-research-2023/3.26.b4
  locator: { number: "3.26.b4", headingPath: ["Content, structure and delivery", "General skills"] }
  span: { start: 73749, end: 73836 }
  source: "adaptability, in particular displaying readiness to address new problems from new areas"
  stem: "3.26"
  statementType: outcome
  rung: none
  force: describes
  level: fheq:6
  appliesTo: "all graduates of the subject"
  addressee: learner
  verbs: ["displaying", "address"]
  about: "adaptability to new problems"
  themes: [none]
  domain: generic-skill
  award: ["bachelor's with honours", "integrated master's"]
  gradeOf: none
  paraphrase: "Expected of all graduates: adaptability, especially readiness to take on new problems from unfamiliar areas."
  quote: full   # the issuer's statement is in `source` (D-std-0014)
  audience: both
  subjects: inherited
- id: qaa/mathematics-statistics-and-operational-research-2023/3.26.b5
  locator: { number: "3.26.b5", headingPath: ["Content, structure and delivery", "General skills"] }
  span: { start: 73839, end: 73964 }
  source: "the ability to transfer knowledge from one context to another, to assess problems logically and to approach them analytically"
  stem: "3.26"
  statementType: outcome
  rung: none
  force: describes
  level: fheq:6
  appliesTo: "all graduates of the subject"
  addressee: learner
  verbs: ["transfer", "assess", "approach"]
  about: "transferring knowledge and analytical approach"
  themes: [none]
  domain: generic-skill
  award: ["bachelor's with honours", "integrated master's"]
  gradeOf: none
  paraphrase: "Expected of all graduates: carrying knowledge from one setting to another, judging problems logically and tackling them analytically."
  quote: full   # the issuer's statement is in `source` (D-std-0014)
  audience: both
  subjects: inherited
- id: qaa/mathematics-statistics-and-operational-research-2023/3.26.b6
  locator: { number: "3.26.b6", headingPath: ["Content, structure and delivery", "General skills"] }
  span: { start: 73967, end: 74101 }
  source: "highly developed skills of numeracy, including being thoroughly comfortable with numerate concepts and arguments in all stages of work"
  stem: "3.26"
  statementType: outcome
  rung: none
  force: describes
  level: fheq:6
  appliesTo: "all graduates of the subject"
  addressee: learner
  verbs: []
  about: "numeracy"
  themes: [none]
  domain: generic-skill
  award: ["bachelor's with honours", "integrated master's"]
  gradeOf: none
  paraphrase: "Expected of all graduates: highly developed numeracy, at ease with numerical ideas and arguments at every stage of work."
  quote: full   # the issuer's statement is in `source` (D-std-0014)
  audience: both
  subjects: inherited
- id: qaa/mathematics-statistics-and-operational-research-2023/3.26.b7
  locator: { number: "3.26.b7", headingPath: ["Content, structure and delivery", "General skills"] }
  span: { start: 74104, end: 74158 }
  source: "the ability to apply specialist software appropriately"
  stem: "3.26"
  statementType: outcome
  rung: none
  force: describes
  level: fheq:6
  appliesTo: "all graduates of the subject"
  addressee: learner
  verbs: ["apply"]
  about: "using specialist software"
  themes: [none]
  domain: generic-skill
  award: ["bachelor's with honours", "integrated master's"]
  gradeOf: none
  paraphrase: "Expected of all graduates: using specialist software appropriately."
  quote: full   # the issuer's statement is in `source` (D-std-0014)
  audience: both
  subjects: inherited
- id: qaa/mathematics-statistics-and-operational-research-2023/3.26.b8
  locator: { number: "3.26.b8", headingPath: ["Content, structure and delivery", "General skills"] }
  span: { start: 74161, end: 74328 }
  source: "information technology (IT) skills and the ability to obtain information from a variety of sources, always taking care that these sources are referred to appropriately"
  stem: "3.26"
  statementType: outcome
  rung: none
  force: describes
  level: fheq:6
  appliesTo: "all graduates of the subject"
  addressee: learner
  verbs: ["obtain", "referred"]
  about: "IT skills and sourcing information"
  themes: [none]
  domain: generic-skill
  award: ["bachelor's with honours", "integrated master's"]
  gradeOf: none
  paraphrase: "Expected of all graduates: IT skills and finding information from varied sources, always citing them properly."
  quote: full   # the issuer's statement is in `source` (D-std-0014)
  audience: both
  subjects: inherited
- id: qaa/mathematics-statistics-and-operational-research-2023/3.26.b9
  locator: { number: "3.26.b9", headingPath: ["Content, structure and delivery", "General skills"] }
  span: { start: 74331, end: 74390 }
  source: "working in collaboration and building on the work of others"
  stem: "3.26"
  statementType: outcome
  rung: none
  force: describes
  level: fheq:6
  appliesTo: "all graduates of the subject"
  addressee: learner
  verbs: ["working", "building"]
  about: "collaboration"
  themes: [none]
  domain: generic-skill
  award: ["bachelor's with honours", "integrated master's"]
  gradeOf: none
  paraphrase: "Expected of all graduates: working with others and building on their work."
  quote: full   # the issuer's statement is in `source` (D-std-0014)
  audience: both
  subjects: inherited
- id: qaa/mathematics-statistics-and-operational-research-2023/3.26.b10
  locator: { number: "3.26.b10", headingPath: ["Content, structure and delivery", "General skills"] }
  span: { start: 74393, end: 74555 }
  source: "communication skills, generally including verbal and non-verbal, and to communicate results clearly in various ways (for example, reports, presentations, posters)"
  stem: "3.26"
  statementType: outcome
  rung: none
  force: describes
  level: fheq:6
  appliesTo: "all graduates of the subject"
  addressee: learner
  verbs: ["communicate"]
  about: "communicating results"
  themes: [none]
  domain: generic-skill
  award: ["bachelor's with honours", "integrated master's"]
  gradeOf: none
  paraphrase: "Expected of all graduates: communication, verbal and non-verbal, and presenting results clearly in several forms such as reports, talks and posters."
  quote: full   # the issuer's statement is in `source` (D-std-0014)
  audience: both
  subjects: inherited
- id: qaa/mathematics-statistics-and-operational-research-2023/3.26.b11
  locator: { number: "3.26.b11", headingPath: ["Content, structure and delivery", "General skills"] }
  span: { start: 74558, end: 74702 }
  source: "knowledge of ethical issues, including the need for sensitivity in handling data of a personal nature and the impact of MSOR in its application."
  stem: "3.26"
  statementType: outcome
  rung: none
  force: describes
  level: fheq:6
  appliesTo: "all graduates of the subject"
  addressee: learner
  verbs: ["handling"]
  about: "ethical issues, personal data and impact"
  themes: [none]
  domain: generic-skill
  award: ["bachelor's with honours", "integrated master's"]
  gradeOf: none
  paraphrase: "Expected of all graduates: knowledge of ethical issues, including care with personal data and the effects of the subject when applied."
  quote: full   # the issuer's statement is in `source` (D-std-0014)
  audience: both
  subjects: inherited
- id: qaa/mathematics-statistics-and-operational-research-2023/3.28
  locator: { number: "3.28", headingPath: ["Content, structure and delivery", "Teaching and learning"] }
  span: { start: 75119, end: 75693 }
  source: "3.28 A variety of teaching and learning methods are in use in MSOR. These may differ markedly depending on, for example, the style of the course, the subject matter, the level and progression route of the learners and the resources which are available. Providers should carefully choose their approach, having evaluated a wide range of available pedagogies. It is anticipated that multiple approaches will be necessary, even within a single module, but consideration should also be given to maintaining a coherent experience for the student over the duration of the course.\n"
  stem: none
  statementType: expectation
  rung: none
  force: should
  level: none
  appliesTo: "choice of teaching approach"
  addressee: provider
  verbs: ["choose", "evaluated", "given"]
  about: "choosing teaching approaches"
  themes: [none]
  domain: none
  award: ["bachelor's with honours", "integrated master's", "master's"]
  gradeOf: none
  paraphrase: "Teaching and learning methods vary with course style, content, the learners' level and route and the resources at hand; providers should choose carefully after weighing many pedagogies, expecting to mix approaches even within one module while keeping the student's experience coherent across the course."
  quote: full   # the issuer's statement is in `source` (D-std-0014)
  audience: practitioner
  subjects: inherited
- id: qaa/mathematics-statistics-and-operational-research-2023/3.32
  locator: { number: "3.32", headingPath: ["Content, structure and delivery", "Teaching and learning"] }
  span: { start: 77688, end: 78688 }
  source: "3.32 The practice and repetition required for MSOR lends itself to collaborative learning. It is common across a cohort to find a range of strengths and weaknesses, and students vary in the speed in which they gain proficiency in different concepts. Therefore, peer-based learning enriches an individual’s learning experience, providing an important and valuable resource. Peer-based learning is facilitated through certain teaching formats, such as workshops, tutorials and seminars. Peer-based learning also exists outside of scheduled teaching activities and can be student-led, including, for example, group study sessions and student society events. Providers should ensure access to appropriate formal and informal learning spaces for students to facilitate group activities. Providers should promote and encourage peer-based learning in a way that follows good academic practice. As such, students develop understanding of how to learn from others without compromising academic integrity.\n\n24\n"
  stem: none
  statementType: expectation
  rung: none
  force: should
  level: none
  appliesTo: "peer learning"
  addressee: provider
  verbs: ["ensure", "promote", "encourage"]
  about: "peer learning and spaces for it"
  themes: [none]
  domain: none
  award: ["bachelor's with honours", "integrated master's", "master's"]
  gradeOf: none
  paraphrase: "Practice and repetition suit collaborative learning, and peer learning, in class or student-led, enriches each learner; providers should make formal and informal spaces available for group work and should promote peer learning in ways consistent with good academic practice, so students learn from others without compromising integrity."
  quote: full   # the issuer's statement is in `source` (D-std-0014)
  audience: practitioner
  subjects: inherited
- id: qaa/mathematics-statistics-and-operational-research-2023/3.34
  locator: { number: "3.34", headingPath: ["Content, structure and delivery", "Teaching and learning"] }
  span: { start: 79720, end: 80106 }
  source: "3.34 Providers should acknowledge their responsibility, shared with their students, for developing their students into independent scholars and practitioners of their disciplines; this includes, but is not limited to, recognising the need to provide appropriate scaffolding, confidence building and development opportunities to enable students to become effective independent learners.\n"
  stem: none
  statementType: expectation
  rung: none
  force: should
  level: none
  appliesTo: "developing independent learners"
  addressee: provider
  verbs: ["acknowledge", "developing", "recognising"]
  about: "shared responsibility for independent learners"
  themes: [none]
  domain: none
  award: ["bachelor's with honours", "integrated master's", "master's"]
  gradeOf: none
  paraphrase: "Providers should accept that they share with students the responsibility for turning them into independent scholars and practitioners, which includes the scaffolding, confidence-building and opportunities students need to become effective independent learners."
  quote: full   # the issuer's statement is in `source` (D-std-0014)
  audience: practitioner
  subjects: inherited
- id: qaa/mathematics-statistics-and-operational-research-2023/3.35
  locator: { number: "3.35", headingPath: ["Content, structure and delivery", "Teaching and learning"] }
  span: { start: 80106, end: 80607 }
  source: "3.35 A characteristic of MSOR is that significant quantities of domain knowledge and practice of associated skills are required before a student is able to independently and meaningfully engage with solving more advanced problems, especially in more abstract areas. Providers should prioritise equipping students with the discipline-based skills to enable them to independently learn MSOR content and recognise that in doing so their provision is enriched by the nurtured potential of their students.\n"
  stem: none
  statementType: expectation
  rung: none
  force: should
  level: none
  appliesTo: "discipline skills for independent learning"
  addressee: provider
  verbs: ["prioritise", "equipping", "recognise"]
  about: "equipping students to learn on their own"
  themes: [none]
  domain: none
  award: ["bachelor's with honours", "integrated master's", "master's"]
  gradeOf: none
  paraphrase: "Students need a large base of knowledge and practised skill before they can tackle harder problems alone, especially in abstract areas; providers should put first the discipline skills that let students learn the subject independently, recognising that this enriches the provision."
  quote: full   # the issuer's statement is in `source` (D-std-0014)
  audience: practitioner
  subjects: inherited
- id: qaa/mathematics-statistics-and-operational-research-2023/3.36
  locator: { number: "3.36", headingPath: ["Content, structure and delivery", "Teaching and learning"] }
  span: { start: 80607, end: 81523 }
  source: "3.36 Providers should assist students in developing effective study skills so that they can actively engage with teaching and resources. Tutors should model and explain the value of spending time on tasks which do not easily fit within formal timetabled hours. These tasks may include reading ahead or around the topic, diligently checking mathematical arguments, or independent practice of skills, including problem-solving and programming. Scholarly behaviours, such as playing and experimenting with ideas, challenging the necessity of particular assumptions, or attempting to solve a question, even if the solution is incomplete or later found to contain errors, should be encouraged. Students will need time to consolidate their understanding and develop MSOR discipline skills, perhaps through spaced repetition, and providers should timetable teaching hours and schedule assessments to accommodate this need.\n"
  stem: none
  statementType: expectation
  rung: none
  force: should
  level: none
  appliesTo: "study skills and scheduling"
  addressee: provider
  verbs: ["assist", "model", "explain", "encouraged", "timetable", "schedule"]
  about: "study skills, scholarly habits and consolidation time"
  themes: [none]
  domain: none
  award: ["bachelor's with honours", "integrated master's", "master's"]
  gradeOf: none
  paraphrase: "Providers should help students build study skills; tutors should model and explain the worth of work outside timetabled hours, such as reading ahead, checking arguments and independent practice; scholarly habits like experimenting with ideas and attempting incomplete solutions should be encouraged; and teaching and assessment should be timed to leave room to consolidate."
  quote: full   # the issuer's statement is in `source` (D-std-0014)
  audience: practitioner
  subjects: inherited
- id: qaa/mathematics-statistics-and-operational-research-2023/3.39
  locator: { number: "3.39", headingPath: ["Content, structure and delivery", "Teaching and learning"] }
  span: { start: 82660, end: 83443 }
  source: "3.39 Computational work is found across MSOR. In teaching and learning, computing for MSOR may be concentrated within modules or embedded across a course, depending on the emphasis of the course. Students develop skills in computational thinking, should encounter at least one programming language, and may use specialist software to carry out technical MSOR work. Examples include:\n• computer algebra systems\n• specialised software for particular areas of algebra\n• programs for numerical analysis\n• statistical packages for data analysis and model building\n• mathematical programming software for formulating and solving operational research problems.\n\nThis is in addition to the use of standard spreadsheets, graphics systems and specialised systems for mathematical typesetting.\n"
  stem: none
  statementType: expectation
  rung: none
  force: should
  level: fheq:6
  appliesTo: "students of the subject"
  addressee: both
  verbs: ["develop", "encounter", "use"]
  about: "computational thinking and programming"
  themes: [none]
  domain: subject-skill
  award: ["bachelor's with honours", "integrated master's"]
  gradeOf: none
  paraphrase: "Computing runs through the subject, concentrated in modules or spread across a course; students develop computational thinking, should meet one programming language or more and may draw on specialist software such as computer algebra, numerical and statistical packages and optimisation software, beside spreadsheets, graphics and typesetting tools."
  quote: full   # the issuer's statement is in `source` (D-std-0014)
  audience: both
  subjects: inherited
- id: qaa/mathematics-statistics-and-operational-research-2023/3.42
  locator: { number: "3.42", headingPath: ["Content, structure and delivery", "Teaching and learning"] }
  span: { start: 84317, end: 85216 }
  source: "3.42 As in all subjects, MSOR teaching is continually evolving, with providers and individual members of staff responding to changing circumstances and changes to wider educational practice. Innovation in learning, aimed at improvement, is to be welcomed, with the outcomes critically evaluated and disseminated. Providers should support new MSOR staf f to take part in relevant training appropriate to their discipline. Where postgraduate tutors assist staf f in the delivery of the programmes, the provider should ensure that postgraduate tutors receive sufficient discipline-relevant training to best support them in this role. All MSOR staf f have a responsibility to engage in continuing professional development throughout their career. To support the ongoing enhancement of MSOR education there are many continuing professional development opportunities for staf f run by the MSOR community.\n"
  stem: none
  statementType: expectation
  rung: none
  force: should
  level: none
  appliesTo: "staff development"
  addressee: provider
  verbs: ["support", "ensure", "engage"]
  about: "staff training and professional development"
  themes: [none]
  domain: none
  award: ["bachelor's with honours", "integrated master's", "master's"]
  gradeOf: none
  paraphrase: "Teaching keeps changing and innovation should be evaluated and shared; providers should support new staff to train in ways suited to the discipline and should ensure postgraduate tutors receive enough discipline-relevant training, and every member of staff carries a responsibility to keep developing professionally."
  quote: full   # the issuer's statement is in `source` (D-std-0014)
  audience: practitioner
  subjects: inherited
- id: qaa/mathematics-statistics-and-operational-research-2023/3.43
  locator: { number: "3.43", headingPath: ["Content, structure and delivery", "Teaching and learning"] }
  span: { start: 85216, end: 85532 }
  source: "3.43 Providers should engage with quality assurance processes to maintain and enhance the quality of their provision; some of these are locally determined, others are statutory in nature and linked to the retention of degree awarding powers, and others are linked to accreditation by external bodies.\n\n26\nAssessment\n"
  stem: none
  statementType: expectation
  rung: none
  force: should
  level: none
  appliesTo: "quality assurance"
  addressee: provider
  verbs: ["engage", "maintain", "enhance"]
  about: "engaging with quality assurance"
  themes: [none]
  domain: none
  award: ["bachelor's with honours", "integrated master's", "master's"]
  gradeOf: none
  paraphrase: "Providers should take part in quality assurance processes, local, statutory or tied to accreditation, to keep up and improve the quality of their provision."
  quote: full   # the issuer's statement is in `source` (D-std-0014)
  audience: practitioner
  subjects: inherited
- id: qaa/mathematics-statistics-and-operational-research-2023/3.47
  locator: { number: "3.47", headingPath: ["Content, structure and delivery", "Assessment"] }
  span: { start: 87040, end: 87774 }
  source: "3.47 MSOR has important general characteristics which pervade the culture of the discipline and can be taken to apply to all specific courses as intended learning outcomes. For example, minor symbolic differences can radically change the intended meaning, and in applications inaccuracy can have very serious consequences. Similarly, spatial awareness; appreciation of patterns; agility in complex logical reasoning; writing proof; and clarity of expression are all important. Some assessments, or some components of assessments, will seek to establish whether students can demonstrate these intended general learning outcomes. Assessment design should consider equality, diversity and inclusion issues as outlined in paragraph 1.27.\n"
  stem: none
  statementType: expectation
  rung: none
  force: should
  level: none
  appliesTo: "assessment design"
  addressee: provider
  verbs: ["consider", "demonstrate"]
  about: "general characteristics as outcomes; EDI in assessment design"
  themes: [theme:edi]
  domain: none
  award: ["bachelor's with honours", "integrated master's", "master's"]
  gradeOf: none
  paraphrase: "The subject's general characteristics, such as precision with symbols, spatial awareness, pattern recognition, complex logical reasoning, proof and clear expression, can serve as intended outcomes of every course, and some assessments will test them; assessment design should take account of the equality, diversity and inclusion issues set out in 1.27."
  quote: full   # the issuer's statement is in `source` (D-std-0014)
  audience: practitioner
  subjects: inherited
- id: qaa/mathematics-statistics-and-operational-research-2023/3.48
  locator: { number: "3.48", headingPath: ["Content, structure and delivery", "Assessment"] }
  span: { start: 87774, end: 88252 }
  source: "3.48 A wide variety of methods may be used for assessment according to context and purpose, recognising that learners may exhibit different aptitudes in different forms of assessment. Automatically marked online assessment has widespread application, particularly for formative work. All assessments, including traditional invigilated examinations, should be designed taking into consideration both matters of accessibility and factors around equality, diversity and inclusion.\n"
  stem: none
  statementType: expectation
  rung: none
  force: should
  level: none
  appliesTo: "assessment design"
  addressee: provider
  verbs: ["designed", "taking"]
  about: "accessible and inclusive assessment"
  themes: [theme:accessibility, theme:edi]
  domain: none
  award: ["bachelor's with honours", "integrated master's", "master's"]
  gradeOf: none
  paraphrase: "Assessment may use many methods suited to context and purpose, since learners show different aptitudes in different formats, with automatic online marking common for formative work; every assessment, invigilated examinations included, should be designed with accessibility and equality, diversity and inclusion in mind."
  quote: full   # the issuer's statement is in `source` (D-std-0014)
  audience: practitioner
  subjects: inherited
- id: qaa/mathematics-statistics-and-operational-research-2023/4.4
  locator: { number: "4.4", headingPath: ["Benchmark standards", "Introduction"] }
  span: { start: 91713, end: 92464 }
  source: "4.4 The vast majority of students will perform significantly better than the minimum threshold standards. Each higher education provider has its own method of determining what appropriate evidence of this achievement will be and should refer to Annex D: Outcome classification descriptions for FHEQ Level 6 and FQHEIS Level 10 degrees. This Annex sets out common descriptions of the four main degree outcome classifications for bachelor's degrees with honours: 1st, 2.1, 2.2 and 3rd. Students graduating at master’s level will build on the outcomes expected at Levels 6/10 but focus in greater depth on a specific subject area and achieving outcomes as described at this level in the Frameworks for Higher Education Qualifications. Academic standards\n"
  stem: none
  statementType: expectation
  rung: none
  force: should
  level: fheq:6
  appliesTo: "judging achievement above threshold"
  addressee: provider
  verbs: ["perform", "refer", "build"]
  about: "Annex D for performance above threshold; master's outcomes"
  themes: [none]
  domain: none
  award: ["bachelor's with honours", "integrated master's", "master's"]
  gradeOf: none
  paraphrase: "Most students will do much better than the minimum threshold; each provider decides how to evidence this and should refer to Annex D's descriptions of the four honours classifications; master's graduates build on the level 6 and 10 outcomes, in more depth in a specialist area, to the outcomes the Frameworks set for their level."
  quote: full   # the issuer's statement is in `source` (D-std-0014)
  audience: practitioner
  subjects: inherited
- id: qaa/mathematics-statistics-and-operational-research-2023/4.5.b1
  locator: { number: "4.5.b1", headingPath: ["Benchmark standards", "Academic standards"] }
  span: { start: 92579, end: 92799 }
  source: "a reasonable understanding of the basic body of knowledge for the course of study, normally including calculus, linear algebra and probability/statistics, and an ability to comprehend the basic language of the discipline"
  stem: "4.5"
  statementType: threshold
  rung: threshold
  force: should
  level: fheq:6
  appliesTo: "graduates at the honours threshold"
  addressee: learner
  verbs: ["comprehend"]
  about: "core body of knowledge and basic language"
  themes: [none]
  domain: knowledge
  award: ["bachelor's with honours"]
  gradeOf: none
  paraphrase: "Should be able to show a reasonable grasp of the basic knowledge of the course, normally calculus, linear algebra and probability and statistics, and to follow the discipline's basic language."
  quote: full   # the issuer's statement is in `source` (D-std-0014)
  audience: both
  subjects: inherited
- id: qaa/mathematics-statistics-and-operational-research-2023/4.5.b2
  locator: { number: "4.5.b2", headingPath: ["Benchmark standards", "Academic standards"] }
  span: { start: 92802, end: 92956 }
  source: "a reasonable level of skill in calculation and manipulation within this basic body of knowledge and some capability to solve problems formulated within it"
  stem: "4.5"
  statementType: threshold
  rung: threshold
  force: should
  level: fheq:6
  appliesTo: "graduates at the honours threshold"
  addressee: learner
  verbs: ["solve"]
  about: "calculation, manipulation and solving set problems"
  themes: [none]
  domain: subject-skill
  award: ["bachelor's with honours"]
  gradeOf: none
  paraphrase: "Should be able to show reasonable skill at calculating and manipulating within that core, and some ability to solve problems set inside it."
  quote: full   # the issuer's statement is in `source` (D-std-0014)
  audience: both
  subjects: inherited
- id: qaa/mathematics-statistics-and-operational-research-2023/4.5.b3
  locator: { number: "4.5.b3", headingPath: ["Benchmark standards", "Academic standards"] }
  span: { start: 92959, end: 93150 }
  source: "application of concepts and principles in well-defined contexts, showing judgement in the selection and application of tools and techniques and demonstrating justification of the methods used"
  stem: "4.5"
  statementType: threshold
  rung: threshold
  force: should
  level: fheq:6
  appliesTo: "graduates at the honours threshold"
  addressee: learner
  verbs: ["showing", "demonstrating"]
  about: "applying concepts with justified choice of method"
  themes: [none]
  domain: subject-skill
  award: ["bachelor's with honours"]
  gradeOf: none
  paraphrase: "Should be able to show concepts and principles applied in well-defined settings, with judgement in choosing and using tools and techniques and a justification of the methods used."
  quote: full   # the issuer's statement is in `source` (D-std-0014)
  audience: both
  subjects: inherited
- id: qaa/mathematics-statistics-and-operational-research-2023/4.5.b4
  locator: { number: "4.5.b4", headingPath: ["Benchmark standards", "Academic standards"] }
  span: { start: 93153, end: 93256 }
  source: "reasoning using logical arguments, including identifying the assumptions made and the conclusions drawn"
  stem: "4.5"
  statementType: threshold
  rung: threshold
  force: should
  level: fheq:6
  appliesTo: "graduates at the honours threshold"
  addressee: learner
  verbs: ["reasoning", "identifying"]
  about: "logical reasoning, assumptions and conclusions"
  themes: [none]
  domain: subject-skill
  award: ["bachelor's with honours"]
  gradeOf: none
  paraphrase: "Should be able to show reasoning by logical argument, naming the assumptions made and the conclusions reached."
  quote: full   # the issuer's statement is in `source` (D-std-0014)
  audience: both
  subjects: inherited
- id: qaa/mathematics-statistics-and-operational-research-2023/4.5.b5
  locator: { number: "4.5.b5", headingPath: ["Benchmark standards", "Academic standards"] }
  span: { start: 93259, end: 93430 }
  source: "a reasonable level of skill in comprehending problems, formulating them mathematically, obtaining solutions by appropriate methods, and drawing valid inferences from these"
  stem: "4.5"
  statementType: threshold
  rung: threshold
  force: should
  level: fheq:6
  appliesTo: "graduates at the honours threshold"
  addressee: learner
  verbs: ["comprehending", "formulating", "obtaining", "drawing"]
  about: "formulating and solving problems; valid inferences"
  themes: [none]
  domain: subject-skill
  award: ["bachelor's with honours"]
  gradeOf: none
  paraphrase: "Should be able to show reasonable skill at understanding problems, putting them in mathematical form, solving them by suitable methods and drawing valid inferences."
  quote: full   # the issuer's statement is in `source` (D-std-0014)
  audience: both
  subjects: inherited
- id: qaa/mathematics-statistics-and-operational-research-2023/4.5.b6
  locator: { number: "4.5.b6", headingPath: ["Benchmark standards", "Academic standards"] }
  span: { start: 93433, end: 93632 }
  source: "an ability to communicate logical arguments, evidence and conclusions reasonably accurately and clearly, including, if appropriate, acknowledging the degree of uncertainty associated with conclusions"
  stem: "4.5"
  statementType: threshold
  rung: threshold
  force: should
  level: fheq:6
  appliesTo: "graduates at the honours threshold"
  addressee: learner
  verbs: ["communicate", "acknowledging"]
  about: "communicating arguments and uncertainty"
  themes: [none]
  domain: generic-skill
  award: ["bachelor's with honours"]
  gradeOf: none
  paraphrase: "Should be able to show logical arguments, evidence and conclusions communicated with reasonable accuracy and clarity, admitting the uncertainty of conclusions where fitting."
  quote: full   # the issuer's statement is in `source` (D-std-0014)
  audience: both
  subjects: inherited
- id: qaa/mathematics-statistics-and-operational-research-2023/4.5.b7
  locator: { number: "4.5.b7", headingPath: ["Benchmark standards", "Academic standards"] }
  span: { start: 93635, end: 93741 }
  source: "familiarity with at least one programming language and competent use of other appropriate MSOR technology."
  stem: "4.5"
  statementType: threshold
  rung: threshold
  force: should
  level: fheq:6
  appliesTo: "graduates at the honours threshold"
  addressee: learner
  verbs: []
  about: "a programming language and MSOR technology"
  themes: [none]
  domain: subject-skill
  award: ["bachelor's with honours"]
  gradeOf: none
  paraphrase: "Should be able to show they know one programming language or more and can use other suitable technology for the subject competently."
  quote: full   # the issuer's statement is in `source` (D-std-0014)
  audience: both
  subjects: inherited
- id: qaa/mathematics-statistics-and-operational-research-2023/4.6.b1
  locator: { number: "4.6.b1", headingPath: ["Benchmark standards", "Academic standards"] }
  span: { start: 93857, end: 93963 }
  source: "a good understanding of the main body of knowledge for the course of study, including some advanced topics"
  stem: "4.6"
  statementType: threshold
  rung: threshold
  force: should
  level: fheq:7
  appliesTo: "graduates at the integrated master's threshold"
  addressee: learner
  verbs: []
  about: "main body of knowledge with advanced topics"
  themes: [none]
  domain: knowledge
  award: ["integrated master's"]
  gradeOf: none
  paraphrase: "Should be able to show a good grasp of the main knowledge of the course, some advanced topics included."
  quote: full   # the issuer's statement is in `source` (D-std-0014)
  audience: both
  subjects: inherited
- id: qaa/mathematics-statistics-and-operational-research-2023/4.6.b2
  locator: { number: "4.6.b2", headingPath: ["Benchmark standards", "Academic standards"] }
  span: { start: 93966, end: 94131 }
  source: "a good level of skill in calculation and manipulation of the material within this body of knowledge, and be capable of solving advanced problems formulated within it"
  stem: "4.6"
  statementType: threshold
  rung: threshold
  force: should
  level: fheq:7
  appliesTo: "graduates at the integrated master's threshold"
  addressee: learner
  verbs: ["solving"]
  about: "calculation and advanced problems"
  themes: [none]
  domain: subject-skill
  award: ["integrated master's"]
  gradeOf: none
  paraphrase: "Should be able to show good skill at calculating and manipulating the material and the capacity to solve advanced problems framed within it."
  quote: full   # the issuer's statement is in `source` (D-std-0014)
  audience: both
  subjects: inherited
- id: qaa/mathematics-statistics-and-operational-research-2023/4.6.b3
  locator: { number: "4.6.b3", headingPath: ["Benchmark standards", "Academic standards"] }
  span: { start: 94134, end: 94344 }
  source: "application of a range of concepts and principles in loosely defined contexts, showing good judgement in the selection and application of tools and techniques and demonstrating justification of the methods used"
  stem: "4.6"
  statementType: threshold
  rung: threshold
  force: should
  level: fheq:7
  appliesTo: "graduates at the integrated master's threshold"
  addressee: learner
  verbs: ["showing", "demonstrating"]
  about: "applying a range of concepts in loosely defined settings"
  themes: [none]
  domain: subject-skill
  award: ["integrated master's"]
  gradeOf: none
  paraphrase: "Should be able to show a range of concepts and principles applied in loosely defined settings, with good judgement in choosing and using tools and techniques and a justification of the methods used."
  quote: full   # the issuer's statement is in `source` (D-std-0014)
  audience: both
  subjects: inherited
- id: qaa/mathematics-statistics-and-operational-research-2023/4.6.b4
  locator: { number: "4.6.b4", headingPath: ["Benchmark standards", "Academic standards"] }
  span: { start: 94347, end: 94420 }
  source: "a good level of capability in developing and evaluating logical arguments"
  stem: "4.6"
  statementType: threshold
  rung: threshold
  force: should
  level: fheq:7
  appliesTo: "graduates at the integrated master's threshold"
  addressee: learner
  verbs: ["developing", "evaluating"]
  about: "building and evaluating logical arguments"
  themes: [none]
  domain: subject-skill
  award: ["integrated master's"]
  gradeOf: none
  paraphrase: "Should be able to show good capability in building and judging logical arguments."
  quote: full   # the issuer's statement is in `source` (D-std-0014)
  audience: both
  subjects: inherited
- id: qaa/mathematics-statistics-and-operational-research-2023/4.6.b5
  locator: { number: "4.6.b5", headingPath: ["Benchmark standards", "Academic standards"] }
  span: { start: 94423, end: 94588 }
  source: "a good level of skill in comprehending problems, formulating them mathematically, obtaining solutions by appropriate methods, and drawing valid inferences from these"
  stem: "4.6"
  statementType: threshold
  rung: threshold
  force: should
  level: fheq:7
  appliesTo: "graduates at the integrated master's threshold"
  addressee: learner
  verbs: ["comprehending", "formulating", "obtaining", "drawing"]
  about: "formulating and solving problems; valid inferences"
  themes: [none]
  domain: subject-skill
  award: ["integrated master's"]
  gradeOf: none
  paraphrase: "Should be able to show good skill at understanding problems, putting them in mathematical form, solving them by suitable methods and drawing valid inferences."
  quote: full   # the issuer's statement is in `source` (D-std-0014)
  audience: both
  subjects: inherited
- id: qaa/mathematics-statistics-and-operational-research-2023/4.6.b6
  locator: { number: "4.6.b6", headingPath: ["Benchmark standards", "Academic standards"] }
  span: { start: 94591, end: 94788 }
  source: "confident and effective communication of logical arguments, evidence and conclusions accurately and clearly, and, if appropriate, acknowledging the degree of uncertainty associated with conclusions"
  stem: "4.6"
  statementType: threshold
  rung: threshold
  force: should
  level: fheq:7
  appliesTo: "graduates at the integrated master's threshold"
  addressee: learner
  verbs: ["acknowledging"]
  about: "confident communication and uncertainty"
  themes: [none]
  domain: generic-skill
  award: ["integrated master's"]
  gradeOf: none
  paraphrase: "Should be able to show confident, effective communication of logical arguments, evidence and conclusions, accurate and clear, admitting uncertainty where fitting."
  quote: full   # the issuer's statement is in `source` (D-std-0014)
  audience: both
  subjects: inherited
- id: qaa/mathematics-statistics-and-operational-research-2023/4.6.b7
  locator: { number: "4.6.b7", headingPath: ["Benchmark standards", "Academic standards"] }
  span: { start: 94791, end: 94896 }
  source: "familiarity with at least one programming language and competent use of other appropriate MSOR technology"
  stem: "4.6"
  statementType: threshold
  rung: threshold
  force: should
  level: fheq:7
  appliesTo: "graduates at the integrated master's threshold"
  addressee: learner
  verbs: []
  about: "a programming language and MSOR technology"
  themes: [none]
  domain: subject-skill
  award: ["integrated master's"]
  gradeOf: none
  paraphrase: "Should be able to show they know one programming language or more and can use other suitable technology for the subject competently."
  quote: full   # the issuer's statement is in `source` (D-std-0014)
  audience: both
  subjects: inherited
- id: qaa/mathematics-statistics-and-operational-research-2023/4.6.b8
  locator: { number: "4.6.b8", headingPath: ["Benchmark standards", "Academic standards"] }
  span: { start: 94899, end: 95016 }
  source: "the ability to work competently and independently, to be aware of own strengths and to understand when help is needed"
  stem: "4.6"
  statementType: threshold
  rung: threshold
  force: should
  level: fheq:7
  appliesTo: "graduates at the integrated master's threshold"
  addressee: learner
  verbs: ["work", "understand"]
  about: "independent work and knowing when to seek help"
  themes: [none]
  domain: generic-skill
  award: ["integrated master's"]
  gradeOf: none
  paraphrase: "Should be able to show competent, independent working, awareness of one's own strengths and an understanding of when help is needed."
  quote: full   # the issuer's statement is in `source` (D-std-0014)
  audience: both
  subjects: inherited
- id: qaa/mathematics-statistics-and-operational-research-2023/4.6.b9
  locator: { number: "4.6.b9", headingPath: ["Benchmark standards", "Academic standards"] }
  span: { start: 95019, end: 95152 }
  source: "competence in planning and conducting an advanced project in mathematics, statistics or operational research or a related topic area."
  stem: "4.6"
  statementType: threshold
  rung: threshold
  force: should
  level: fheq:7
  appliesTo: "graduates at the integrated master's threshold"
  addressee: learner
  verbs: ["planning", "conducting"]
  about: "an advanced project"
  themes: [none]
  domain: subject-skill
  award: ["integrated master's"]
  gradeOf: none
  paraphrase: "Should be able to show competence in planning and carrying out an advanced project in mathematics, statistics, operational research or a related area."
  quote: full   # the issuer's statement is in `source` (D-std-0014)
  audience: both
  subjects: inherited
- id: qaa/mathematics-statistics-and-operational-research-2023/4.7
  locator: { number: "4.7", headingPath: ["Benchmark standards", "Academic standards"] }
  span: { start: 95154, end: 95406 }
  source: "4.7 Taught postgraduate master’s degrees will develop some or all of the standards listed above, depending on the precise nature of the course of study, which may be specialised within a subdiscipline or interdisciplinary with another discipline area.\n"
  stem: none
  statementType: expectation
  rung: none
  force: will
  level: fheq:7
  appliesTo: "taught postgraduate master's courses"
  addressee: both
  verbs: ["develop"]
  about: "taught master's and the listed standards"
  themes: [none]
  domain: none
  award: ["master's"]
  gradeOf: none
  paraphrase: "Taught postgraduate master's courses will build some or all of the standards above, depending on the course, which may specialise within one part of the subject or combine it with another discipline."
  quote: full   # the issuer's statement is in `source` (D-std-0014)
  audience: both
  subjects: inherited
- id: qaa/mathematics-statistics-and-operational-research-2023/4.9.b1
  locator: { number: "4.9.b1", headingPath: ["Benchmark standards", "Professional standards"] }
  span: { start: 96452, end: 96513 }
  source: "synthesize information from different branches of the subject"
  stem: "4.9"
  statementType: outcome
  rung: none
  force: should
  level: fheq:6
  appliesTo: "graduates of the subject"
  addressee: learner
  verbs: ["synthesize"]
  about: "synthesising across branches"
  themes: [none]
  domain: subject-skill
  award: ["bachelor's with honours", "integrated master's"]
  gradeOf: none
  paraphrase: "Graduates should be expected to bring together information from different branches of the subject."
  quote: full   # the issuer's statement is in `source` (D-std-0014)
  audience: both
  subjects: inherited
- id: qaa/mathematics-statistics-and-operational-research-2023/4.9.b2
  locator: { number: "4.9.b2", headingPath: ["Benchmark standards", "Professional standards"] }
  span: { start: 96516, end: 96650 }
  source: "apply critical thinking and problem-solving skills to problems arising in MSOR and in the context of other disciplines or applications"
  stem: "4.9"
  statementType: outcome
  rung: none
  force: should
  level: fheq:6
  appliesTo: "graduates of the subject"
  addressee: learner
  verbs: ["apply"]
  about: "critical thinking and problem-solving"
  themes: [none]
  domain: generic-skill
  award: ["bachelor's with honours", "integrated master's"]
  gradeOf: none
  paraphrase: "Graduates should be expected to use critical thinking and problem-solving on problems from within the subject and from other disciplines or applications."
  quote: full   # the issuer's statement is in `source` (D-std-0014)
  audience: both
  subjects: inherited
- id: qaa/mathematics-statistics-and-operational-research-2023/4.9.b3
  locator: { number: "4.9.b3", headingPath: ["Benchmark standards", "Professional standards"] }
  span: { start: 96653, end: 96730 }
  source: "work effectively individually or as part of a group to achieve a specific aim"
  stem: "4.9"
  statementType: outcome
  rung: none
  force: should
  level: fheq:6
  appliesTo: "graduates of the subject"
  addressee: learner
  verbs: ["work", "achieve"]
  about: "working alone or in a group to an aim"
  themes: [none]
  domain: generic-skill
  award: ["bachelor's with honours", "integrated master's"]
  gradeOf: none
  paraphrase: "Graduates should be expected to work effectively alone or in a group towards a set aim."
  quote: full   # the issuer's statement is in `source` (D-std-0014)
  audience: both
  subjects: inherited
- id: qaa/mathematics-statistics-and-operational-research-2023/4.9.b4
  locator: { number: "4.9.b4", headingPath: ["Benchmark standards", "Professional standards"] }
  span: { start: 96733, end: 96898 }
  source: "communicate accurately and clearly verbally and/or non-verbally using a variety of formats; this may include communication to specialist and non-specialist audiences"
  stem: "4.9"
  statementType: outcome
  rung: none
  force: should
  level: fheq:6
  appliesTo: "graduates of the subject"
  addressee: learner
  verbs: ["communicate"]
  about: "communicating to specialist and non-specialist audiences"
  themes: [none]
  domain: generic-skill
  award: ["bachelor's with honours", "integrated master's"]
  gradeOf: none
  paraphrase: "Graduates should be expected to communicate accurately and clearly, verbally or non-verbally, in varied formats, possibly to specialist and non-specialist audiences."
  quote: full   # the issuer's statement is in `source` (D-std-0014)
  audience: both
  subjects: inherited
- id: qaa/mathematics-statistics-and-operational-research-2023/4.9.b5
  locator: { number: "4.9.b5", headingPath: ["Benchmark standards", "Professional standards"] }
  span: { start: 96905, end: 97153 }
  source: "possess digital capabilities, including retrieval of information and the assessment of its veracity, the use of generic IT, and the ability to select and employ appropriate digital tools to support mathematical thinking, reasoning and communication"
  stem: "4.9"
  statementType: outcome
  rung: none
  force: should
  level: fheq:6
  appliesTo: "graduates of the subject"
  addressee: learner
  verbs: ["possess", "select", "employ", "support"]
  about: "digital capability"
  themes: [none]
  domain: generic-skill
  award: ["bachelor's with honours", "integrated master's"]
  gradeOf: none
  paraphrase: "Graduates should be expected to have digital capabilities: finding information and judging its reliability, using general IT and choosing and using digital tools that support mathematical thinking, reasoning and communication."
  quote: full   # the issuer's statement is in `source` (D-std-0014)
  audience: both
  subjects: inherited
- id: qaa/mathematics-statistics-and-operational-research-2023/4.9.b6
  locator: { number: "4.9.b6", headingPath: ["Benchmark standards", "Professional standards"] }
  span: { start: 97156, end: 97312 }
  source: "be aware of the need to work within existing professional and legal frameworks, including data security, EDI and sustainability, each within an MSOR context"
  stem: "4.9"
  statementType: outcome
  rung: none
  force: should
  level: fheq:6
  appliesTo: "graduates of the subject"
  addressee: learner
  verbs: ["work"]
  about: "professional and legal frameworks, EDI and sustainability"
  themes: [theme:edi, theme:esd]
  domain: generic-skill
  award: ["bachelor's with honours", "integrated master's"]
  gradeOf: none
  paraphrase: "Graduates should be expected to be aware that work must sit within professional and legal frameworks, data security, EDI and sustainability among them, each in the subject's setting."
  quote: full   # the issuer's statement is in `source` (D-std-0014)
  audience: both
  subjects: inherited
- id: qaa/mathematics-statistics-and-operational-research-2023/4.9.b7
  locator: { number: "4.9.b7", headingPath: ["Benchmark standards", "Professional standards"] }
  span: { start: 97315, end: 97408 }
  source: "maintain appropriate ethical standards and be aware of the broader implications of their work"
  stem: "4.9"
  statementType: outcome
  rung: none
  force: should
  level: fheq:6
  appliesTo: "graduates of the subject"
  addressee: learner
  verbs: ["maintain"]
  about: "ethical standards and wider implications"
  themes: [none]
  domain: generic-skill
  award: ["bachelor's with honours", "integrated master's"]
  gradeOf: none
  paraphrase: "Graduates should be expected to keep to suitable ethical standards and be aware of the wider consequences of their work."
  quote: full   # the issuer's statement is in `source` (D-std-0014)
  audience: both
  subjects: inherited
- id: qaa/mathematics-statistics-and-operational-research-2023/4.9.b8
  locator: { number: "4.9.b8", headingPath: ["Benchmark standards", "Professional standards"] }
  span: { start: 97411, end: 97537 }
  source: "be able to initiate self-learning and monitor/adjust personal programmes of work in light of reflection and feedback received."
  stem: "4.9"
  statementType: outcome
  rung: none
  force: should
  level: fheq:6
  appliesTo: "graduates of the subject"
  addressee: learner
  verbs: ["initiate", "monitor"]
  about: "self-directed learning and reflection"
  themes: [none]
  domain: generic-skill
  award: ["bachelor's with honours", "integrated master's"]
  gradeOf: none
  paraphrase: "Graduates should be expected to start their own learning and to check and adjust their plans of work in the light of reflection and feedback."
  quote: full   # the issuer's statement is in `source` (D-std-0014)
  audience: both
  subjects: inherited
- id: qaa/mathematics-statistics-and-operational-research-2023/4.10
  locator: { number: "4.10", headingPath: ["Benchmark standards", "Professional standards"] }
  span: { start: 97539, end: 97806 }
  source: "4.10 Students at master’s level will have had a deeper or broader experience of a subset of the skills listed and greater experience of working independently, with additional opportunities to form novel and creative approaches for tackling non-standard problems.\n\n31\n"
  stem: none
  statementType: expectation
  rung: none
  force: will
  level: fheq:7
  appliesTo: "students at master's level"
  addressee: learner
  verbs: ["had"]
  about: "deeper professional skills and independence at master's level"
  themes: [none]
  domain: generic-skill
  award: ["integrated master's", "master's"]
  gradeOf: none
  paraphrase: "Master's-level students will have had deeper or broader experience of part of the professional skills listed, more experience of working independently and extra chances to devise new and creative approaches to non-standard problems."
  quote: full   # the issuer's statement is in `source` (D-std-0014)
  audience: both
  subjects: inherited
```

### S4a Audience versions
<!-- label: both; status: drafted; basis: primary. forPractitioner: for the programme designer or teacher. forBeneficiary: for the student, second person, naming no issuer. author-agent-written: instructions to an AI agent writing about the statement (a course document, a handbook, an outcome, a report). author-agent-dialogue: instructions to an AI agent using the statement in conversation (with a student, a teacher or a programme team). Written fresh from the held text alone (benchmark rule 6; Abbott, 15:42). -->
```yaml
- statement: qaa/mathematics-statistics-and-operational-research-2023/1.10
  forPractitioner: { text: "Whether your course leans to theory or to practice, you should plan it so every graduate leaves able to identify fully as a professional practitioner in mathematics, statistics or operational research.", rewrite: light, force: should, status: drafted }
  forBeneficiary: { text: "not-applicable: a duty on the provider; the student meets its effect, not a standard to reach", rewrite: full, force: should, status: drafted }
  author-agent-written: "Describe this as a provider expectation about professional identity across the spectrum of course styles; its force is should, a duty on the provider rather than an outcome a student shows. State that it holds for bachelor's, integrated master's and taught master's courses alike, at no single level. Cite it as (QAA, 2023, Mathematics, Statistics and Operational Research Subject Benchmark Statement, para 1.10) and do not claim that it sets a graded outcome or that it is a regulatory requirement. Set it beside 2.1 and 2.2 on course styles and the professional standards in 4.9.b1 to 4.9.b8."
  author-agent-dialogue: "Raise it when a programme team asks whether a practice-based or interdisciplinary course prepares graduates to call themselves practitioners. Frame it for staff as a design aim, in plain words. Ask how would a graduate of this course describe their professional identity, and where is that built? Avoid presenting it to a student as a test to pass or fail."
- statement: qaa/mathematics-statistics-and-operational-research-2023/1.23
  forPractitioner: { text: "You should build EDI into the curriculum and every part of the student experience, review delivery, admissions and assessment for their effects on particular groups, and monitor engagement and attainment by group so you can act for equity.", rewrite: light, force: should, status: drafted }
  forBeneficiary: { text: "not-applicable: a duty on the provider; the student meets its effect, not a standard to reach", rewrite: full, force: should, status: drafted }
  author-agent-written: "Describe this as a provider expectation on equality, diversity and inclusion in curriculum, processes and monitoring; its force is should, a duty on the provider. State that it holds for all MSOR courses, at no single level. Cite it as (QAA, 2023, Mathematics, Statistics and Operational Research Subject Benchmark Statement, para 1.23) and do not claim that it states a legal duty or describes a student outcome. Set it beside 1.25 (review of practice for equity), the examples in 1.27 and the assessment statements 3.47 and 3.48."
  author-agent-dialogue: "Raise it when staff review a curriculum, an admissions policy or attainment data broken down by group. Put it to the team as a question of who the present design may leave out. Ask which groups' attainment do you monitor, and what changed the last time a gap appeared? Avoid giving it to a student as something they must do, or reading the issuer's wording aloud."
- statement: qaa/mathematics-statistics-and-operational-research-2023/1.25
  forPractitioner: { text: "Keep core content, but reflect openly on the discipline's history, including contributions from contexts now seen as problematic and long-standing gatekeeping; you should review your practices with equity as the explicit focus.", rewrite: light, force: should, status: drafted }
  forBeneficiary: { text: "not-applicable: a duty on the provider; the student meets its effect, not a standard to reach", rewrite: full, force: should, status: drafted }
  author-agent-written: "Describe this as a provider expectation to review practice for equity, set in the debate on decolonising the curriculum; its force is should for the review; the reflection on history around it is advisory (might). State that it holds for all MSOR courses. Cite it as (QAA, 2023, Mathematics, Statistics and Operational Research Subject Benchmark Statement, para 1.25) and do not claim that it asks for core content to be cut or censored. Set it beside 1.23, which it points back to, and the curriculum examples in 1.27."
  author-agent-dialogue: "Raise it when a teacher asks how to handle the history of figures linked to eugenics or other harms, or how to widen the examples used. Use the practitioner framing: keep the mathematics, widen the story told about it. Ask where do your modules tell the history of their methods, and whose work appears in them? Avoid treating it as a demand to remove content, or putting the duty to a student."
- statement: qaa/mathematics-statistics-and-operational-research-2023/1.28
  forPractitioner: { text: "You should anticipate learners' needs and meet them before they are raised; your institution should give MSOR staff support (specialist staff, training, policy that allows for mathematical content, suitable tools) to overcome barriers the subject brings.", rewrite: light, force: should, status: drafted }
  forBeneficiary: { text: "not-applicable: a duty on the provider; the student meets its effect, not a standard to reach", rewrite: full, force: should, status: drafted }
  author-agent-written: "Describe this as a provider expectation on anticipatory accessibility and on support for subject staff; its force is should, a duty on the provider and its institution. State that it holds for all MSOR courses. Cite it as (QAA, 2023, Mathematics, Statistics and Operational Research Subject Benchmark Statement, para 1.28) and do not claim that it is a student outcome or that it restates the law. Set it beside 1.30 (embedding accessibility) and 1.34 to 1.36 (the subject's own barriers)."
  author-agent-dialogue: "Raise it when staff say that accessible notes with dense notation take too long, or an institution writes accessibility policy. Frame it for staff as support the institution owes them, not only work they owe students. Ask what help do staff get to make mathematical content accessible, and where does it fall short? Avoid putting the duty to a student or reading the text aloud at length."
- statement: qaa/mathematics-statistics-and-operational-research-2023/1.29
  forPractitioner: { text: "You should consider the barriers to full participation both across the course and within each module, so the approach to accessibility is one coherent, consistent whole.", rewrite: light, force: should, status: drafted }
  forBeneficiary: { text: "not-applicable: a duty on the provider; the student meets its effect, not a standard to reach", rewrite: full, force: should, status: drafted }
  author-agent-written: "Describe this as a provider expectation to plan accessibility at both course and module level; its force is should, a duty on the provider. State that it holds for all MSOR courses. Cite it as (QAA, 2023, Mathematics, Statistics and Operational Research Subject Benchmark Statement, para 1.29) and do not claim that module-level fixes alone meet it. Set it beside 1.28 and 1.33 (well-curated courses)."
  author-agent-dialogue: "Raise it when a module leader plans accessibility alone, or a review finds modules handling it in different ways. Frame it for staff as joining up module practice into one course approach. Ask do students meet the same accessibility arrangements in every module, and who checks? Avoid treating it as something a student must arrange."
- statement: qaa/mathematics-statistics-and-operational-research-2023/1.30
  forPractitioner: { text: "It is essential that you anticipate the digital, physical and pedagogical accessibility needs disabled students have in this subject, and embed accessibility so individual adjustments are rarely or never needed.", rewrite: light, force: must, status: drafted }
  forBeneficiary: { text: "not-applicable: a duty on the provider; the student meets its effect, not a standard to reach", rewrite: full, force: must, status: drafted }
  author-agent-written: "Describe this as a provider duty worded as imperative, recorded as describes and read as close to must (Part E); its force is the strongest the statement uses outside its modal verbs. State that it holds for all MSOR courses. Cite it as (QAA, 2023, Mathematics, Statistics and Operational Research Subject Benchmark Statement, para 1.30) and do not claim that it replaces the legal duty to make reasonable adjustments. Set it beside 1.31 (reasonable adjustments) and 1.32 (who embedded accessibility helps)."
  author-agent-dialogue: "Raise it when a team relies on individual adjustments rather than accessible design. Frame it for staff as moving work from reaction to design. Ask how many adjustments did you make last year that accessible design would have removed? Avoid putting the duty to a student or softening its strength."
- statement: qaa/mathematics-statistics-and-operational-research-2023/1.33
  forPractitioner: { text: "You should curate the course well: communicate learning opportunities clearly, space assessments sensibly and give particular support when a concept or skill first appears.", rewrite: light, force: should, status: drafted }
  forBeneficiary: { text: "not-applicable: a duty on the provider; the student meets its effect, not a standard to reach", rewrite: full, force: should, status: drafted }
  author-agent-written: "Describe this as a provider expectation that courses be well curated; its force is should, a duty on the provider. State that it holds for all MSOR courses. Cite it as (QAA, 2023, Mathematics, Statistics and Operational Research Subject Benchmark Statement, para 1.33) and do not claim that it sets a standard for students. Set it beside 1.32 (embedded accessibility) and 3.36 (time to consolidate)."
  author-agent-dialogue: "Raise it when students report bunched deadlines or confusing course information. Frame it for staff as course housekeeping that helps everyone. Ask where do assessment deadlines cluster, and how do students first hear about each learning opportunity? Avoid giving it to a student as their task."
- statement: qaa/mathematics-statistics-and-operational-research-2023/1.36.b1
  forPractitioner: { text: "You should recognise that common assistive tools (screen readers, captioning, learning platforms) often fail on mathematical content, and fund the extra resources needed to close that gap.", rewrite: light, force: should, status: drafted }
  forBeneficiary: { text: "not-applicable: a duty on the provider; the student meets its effect, not a standard to reach", rewrite: full, force: should, status: drafted }
  author-agent-written: "Describe this as a provider expectation to resource the gap left by mainstream assistive technology; its force is should, a duty on the provider. State that it holds for all MSOR courses. Cite it as (QAA, 2023, Mathematics, Statistics and Operational Research Subject Benchmark Statement, para 1.36, first item) and do not claim that the other two items of 1.36 carry the same force. Set it beside 1.35 (specialist technology) and 1.28 (support for staff)."
  author-agent-dialogue: "Raise it when a team assumes the institution's standard captioning or screen reader is enough for mathematical material. Frame it for staff as a budget and planning question. Ask which tools fail on your notation today, and what would replace them? Avoid putting the duty to a student."
- statement: qaa/mathematics-statistics-and-operational-research-2023/1.37
  forPractitioner: { text: "Where you capture or caption sessions, the technology must record extended written working and caption it accurately; in physical rooms, boards and displays must be visible to everyone.", rewrite: light, force: must, status: drafted }
  forBeneficiary: { text: "not-applicable: a duty on the provider; the student meets its effect, not a standard to reach", rewrite: full, force: must, status: drafted }
  author-agent-written: "Describe this as a provider requirement, worded 'is required' and 'is essential', on capture technology, captions and visibility; its force is must, a duty on the provider. State that it holds for all MSOR courses. Cite it as (QAA, 2023, Mathematics, Statistics and Operational Research Subject Benchmark Statement, para 1.37) and do not claim that it requires any one delivery mode. Set it beside 1.40 (flexible pedagogy) and 3.37 (teaching spaces)."
  author-agent-dialogue: "Raise it when a team plans recorded lectures with board work, or chooses rooms. Frame it for staff as a minimum for any captured or in-person session. Ask can a student watching the recording read every line of working, and are the captions accurate for symbols? Avoid putting the requirement to a student."
- statement: qaa/mathematics-statistics-and-operational-research-2023/1.38
  forPractitioner: { text: "Those who support disabled students (scribes, notetakers, readers, communication support workers) need training in MSOR terminology and notation, since one wrong symbol can change what is meant.", rewrite: light, force: must, status: drafted }
  forBeneficiary: { text: "not-applicable: a duty on the provider; the student meets its effect, not a standard to reach", rewrite: full, force: must, status: drafted }
  author-agent-written: "Describe this as a requirement on support arrangements, worded 'need to' and recorded as describes (Part E); its force is an obligation outside the modal verbs, read as close to should. State that it holds for all MSOR courses. Cite it as (QAA, 2023, Mathematics, Statistics and Operational Research Subject Benchmark Statement, para 1.38) and do not claim that it sets a standard for students. Set it beside 1.34 (special notation) and 1.31 (reasonable adjustments)."
  author-agent-dialogue: "Raise it when a disability service assigns support workers to MSOR students. Frame it for staff as a training and matching question. Ask do the support workers your students rely on read mathematical notation confidently? Avoid putting it to a student as their responsibility."
- statement: qaa/mathematics-statistics-and-operational-research-2023/1.42
  forPractitioner: { text: "When designing assessments you should anticipate and strip out barriers that have nothing to do with the knowledge or skill measured: needless reading load, distracting imagery, unfamiliar cultural context or idiom.", rewrite: light, force: should, status: drafted }
  forBeneficiary: { text: "not-applicable: a duty on the provider; the student meets its effect, not a standard to reach", rewrite: full, force: should, status: drafted }
  author-agent-written: "Describe this as a provider expectation on accessible assessment design; its force is should, a duty on whoever designs assessment. State that it holds for all MSOR assessment. Cite it as (QAA, 2023, Mathematics, Statistics and Operational Research Subject Benchmark Statement, para 1.42) and do not claim that it lowers the standard assessed. Set it beside 3.47 and 3.48 (assessment design and EDI) and the threshold lists 4.5 and 4.6."
  author-agent-dialogue: "Raise it when a teacher drafts or reviews an exam paper or coursework brief. Frame it for staff as a check that each question tests only what it means to. Ask what in this question would slow a student who knows the mathematics perfectly well? Avoid suggesting the standard itself should fall."
- statement: qaa/mathematics-statistics-and-operational-research-2023/1.50
  forPractitioner: { text: "Students carry personal responsibility for their careers and central services help, but you should embed employability skills in the course itself, through enterprise and entrepreneurship education among other means.", rewrite: light, force: should, status: drafted }
  forBeneficiary: { text: "not-applicable: a duty on the provider; the student meets its effect, not a standard to reach", rewrite: full, force: should, status: drafted }
  author-agent-written: "Describe this as a provider expectation to embed employability in the course; its force is should, a duty on the provider; the student's own responsibility is noted beside it. State that it holds for all MSOR courses. Cite it as (QAA, 2023, Mathematics, Statistics and Operational Research Subject Benchmark Statement, para 1.50) and do not claim that careers services alone meet it. Set it beside 1.53 (enterprise education defined), 1.60 and the professional standards 4.9.b1 to 4.9.b8."
  author-agent-dialogue: "Raise it when a team treats careers work as something outside the curriculum. Frame it for staff as course design, not an add-on. Ask where in the modules do students build and recognise employability skills? Avoid putting the provider's duty to a student."
- statement: qaa/mathematics-statistics-and-operational-research-2023/1.55
  forPractitioner: { text: "Before any group task you should help students understand how collaborative work differs from individual work, how groups are managed and what good group behaviour looks like; projects, group modules and work with large data sets then build enterprise skills.", rewrite: light, force: should, status: drafted }
  forBeneficiary: { text: "not-applicable: a duty on the provider; the student meets its effect, not a standard to reach", rewrite: full, force: should, status: drafted }
  author-agent-written: "Describe this as a provider expectation to prepare students for group work, set among enterprise competencies; its force is should, a duty on the provider. State that it holds for all MSOR courses. Cite it as (QAA, 2023, Mathematics, Statistics and Operational Research Subject Benchmark Statement, para 1.55) and do not claim that every module must include group work. Set it beside 4.9.b3 (working in groups) and 3.26.b9 (collaboration)."
  author-agent-dialogue: "Raise it when a team plans assessed group work or students complain about group dynamics. Frame it for staff as preparation students need before the task begins. Ask what do students learn about working in a group before the group task starts? Avoid giving the duty to a student."
- statement: qaa/mathematics-statistics-and-operational-research-2023/1.60
  forPractitioner: { text: "Graduates need to be able to reflect on and explain how the course developed their enterprise and employability skills; give them chances to practise saying so.", rewrite: light, force: must, status: drafted }
  forBeneficiary: { text: "To make the most of your skills in a job or further study, you need to be able to reflect on, understand and explain how your degree helped you develop enterprising and employability skills.", rewrite: full, force: must, status: drafted }
  author-agent-written: "Describe this as a learner expectation worded 'need to', recorded as describes (Part E); its force is an expectation, not a threshold requirement. State that it holds for graduates of honours and integrated master's courses, read at fheq:6 beside qaa/fheq-2024/4.15.b9.3. Cite it as (QAA, 2023, Mathematics, Statistics and Operational Research Subject Benchmark Statement, para 1.60) and do not claim that it is a condition of the award. Set it beside 4.9.b8 (self-learning and reflection) and qaa/fheq-2024/annex-d/transferable/r5/3rd."
  author-agent-dialogue: "Raise it when a student prepares for applications or interviews, or a tutor plans reflective work. Put it to a student in the second person: you will need to say what your degree taught you beyond the mathematics. Ask what have you done on your course that shows enterprise, and how would you describe it to an employer? Avoid presenting it as something examined for the degree."
- statement: qaa/mathematics-statistics-and-operational-research-2023/2.5
  forPractitioner: { text: "Your bachelor's course should equip students with the knowledge, understanding and skills of the subject and with transferable skills that open a wide range of careers; integrated master's courses carry their own higher outcomes.", rewrite: light, force: should, status: drafted }
  forBeneficiary: { text: "not-applicable: a duty on the provider; the student meets its effect, not a standard to reach", rewrite: full, force: should, status: drafted }
  author-agent-written: "Describe this as a provider expectation on what a bachelor's degree should give students, with the stated level crosswalk; its force is should, a duty on the provider. State that it holds for the bachelor's degree with honours at fheq:6 and fqheis:10. Cite it as (QAA, 2023, Mathematics, Statistics and Operational Research Subject Benchmark Statement, para 2.5) and do not claim that it sets the integrated master's outcomes. Set it beside 4.5 (the honours threshold) and qaa/fheq-2024/4.15.b1 to 4.15.b9.3."
  author-agent-dialogue: "Raise it when a team writes the aims of a bachelor's programme. Frame it for staff as the two halves every bachelor's aim needs: subject and transferable. Ask which aims cover the subject itself and which cover the skills that carry into any career? Avoid putting the provider's duty to a student."
- statement: qaa/mathematics-statistics-and-operational-research-2023/2.9
  forPractitioner: { text: "If a placement earns credit, you should integrate it into the programme so students connect what they did and learned there with their academic work.", rewrite: light, force: should, status: drafted }
  forBeneficiary: { text: "not-applicable: a duty on the provider; the student meets its effect, not a standard to reach", rewrite: full, force: should, status: drafted }
  author-agent-written: "Describe this as a provider expectation on credit-bearing placements; its force is should, a duty on the provider. State that it holds for bachelor's and integrated master's courses that carry placement credit. Cite it as (QAA, 2023, Mathematics, Statistics and Operational Research Subject Benchmark Statement, para 2.9) and do not claim that placements are required. Set it beside 2.8 (learning outside the institution) and 2.27 (industry partnerships)."
  author-agent-dialogue: "Raise it when a team designs a placement year or decides whether it carries credit. Frame it for staff as joining the placement to the taught programme. Ask how will students bring what they learn on placement back into their modules? Avoid giving the duty to a student."
- statement: qaa/mathematics-statistics-and-operational-research-2023/2.11
  forPractitioner: { text: "If you run an integrated degree apprenticeship in MSOR, its academic component should follow the guidance of this statement, read with the Characteristics Statement for apprenticeships.", rewrite: light, force: should, status: drafted }
  forBeneficiary: { text: "not-applicable: a duty on the provider; the student meets its effect, not a standard to reach", rewrite: full, force: should, status: drafted }
  author-agent-written: "Describe this as a provider expectation that apprenticeships meet the statement's guidance; its force is should, a duty on the provider. State that it holds for the academic component of integrated degree apprenticeships. Cite it as (QAA, 2023, Mathematics, Statistics and Operational Research Subject Benchmark Statement, para 2.11) and do not claim that it covers the work-based component. Set it beside the Characteristics Statement for Higher Education in Apprenticeships (not yet ingested) and 4.5."
  author-agent-dialogue: "Raise it when a team designs or reviews a degree apprenticeship in data science or mathematics. Frame it for staff as the academic floor the apprenticeship shares with other degrees. Ask does the academic component reach the same threshold as your bachelor's degree? Avoid giving the duty to an apprentice."
- statement: qaa/mathematics-statistics-and-operational-research-2023/2.12
  forPractitioner: { text: "Plan each level so it builds towards at least the threshold standards by the end; a graduate with a second-class degree or better is expected to be ready for postgraduate study, though each course sets its own entry rules.", rewrite: light, force: must, status: drafted }
  forBeneficiary: { text: "As you move from one year to the next, each stage builds you towards at least the threshold level of subject and general skills by the end; with a second-class degree or better you can expect to be ready for postgraduate study, though each course sets its own entry rules.", rewrite: full, force: must, status: drafted }
  author-agent-written: "Describe this as a progression expectation worded 'it is expected that', recorded as describes (Part E); its force is an expectation, not a rule for progression decisions. State that it holds for bachelor's degrees with honours (fheq:6, fqheis:10) and integrated master's (fheq:7, fqheis:11). Cite it as (QAA, 2023, Mathematics, Statistics and Operational Research Subject Benchmark Statement, para 2.12) and do not claim that a second-class degree guarantees postgraduate entry. Set it beside 4.5 and 4.6 (the thresholds) and the progression thread in the FHEQ's SL4."
  author-agent-dialogue: "Raise it when a student asks whether they are on track, or whether a 2.2 opens postgraduate study. Put it to a student in plain words: each year should move you towards the threshold. Ask which threshold skills do you feel secure in now, and which still need work? Avoid promising postgraduate entry or treating the threshold as the whole aim."
- statement: qaa/mathematics-statistics-and-operational-research-2023/2.13
  forPractitioner: { text: "Joint honours and interdisciplinary students will reach the core subject-specific and generic skills of each subject; make sure the MSOR half delivers its core.", rewrite: light, force: will, status: drafted }
  forBeneficiary: { text: "If you study MSOR jointly with another subject, or on an interdisciplinary course, you will gain the core subject and general skills of each subject you combine.", rewrite: full, force: will, status: drafted }
  author-agent-written: "Describe this as an expected outcome for joint and interdisciplinary students; its force is will, an expected outcome. State that it holds for joint honours and interdisciplinary undergraduates, at fheq:6. Cite it as (QAA, 2023, Mathematics, Statistics and Operational Research Subject Benchmark Statement, para 2.13) and do not claim that joint students meet the whole single honours list. Set it beside 2.7 (joint honours described), 4.3 (data science and joint courses) and 4.5."
  author-agent-dialogue: "Raise it when a joint honours student asks what they are expected to master in MSOR. Put it to a student in the second person: you will cover the core, not everything a single honours student covers. Ask which parts of the MSOR core does your course include, and where do they sit? Avoid presenting the full single honours list as their minimum."
- statement: qaa/mathematics-statistics-and-operational-research-2023/2.18
  forPractitioner: { text: "You should offer students some optional modules matched to their interests and give them proper guidance on choosing among them.", rewrite: light, force: should, status: drafted }
  forBeneficiary: { text: "not-applicable: a duty on the provider; the student meets its effect, not a standard to reach", rewrite: full, force: should, status: drafted }
  author-agent-written: "Describe this as a provider expectation on optional modules and guidance; its force is should, a duty on the provider. State that it holds for undergraduate MSOR courses. Cite it as (QAA, 2023, Mathematics, Statistics and Operational Research Subject Benchmark Statement, para 2.18) and do not claim that it overrides prerequisite structures. Set it beside 2.19 (prerequisites limit flexibility)."
  author-agent-dialogue: "Raise it when a team reviews its option structure or advising. Frame it for staff as choice with guidance. Ask how do students find out what each option leads to before they choose? Avoid telling a student they are entitled to any option."
- statement: qaa/mathematics-statistics-and-operational-research-2023/2.24
  forPractitioner: { text: "You should keep the course flexible enough to anticipate and respond to change in the discipline, in neighbouring fields and in what graduates and employers need, and make reasonable adjustments for learners as required.", rewrite: light, force: should, status: drafted }
  forBeneficiary: { text: "not-applicable: a duty on the provider; the student meets its effect, not a standard to reach", rewrite: full, force: should, status: drafted }
  author-agent-written: "Describe this as a provider expectation on course flexibility and reasonable adjustments; its force is should, a duty on the provider. State that it holds for all MSOR courses. Cite it as (QAA, 2023, Mathematics, Statistics and Operational Research Subject Benchmark Statement, para 2.24) and do not claim that it is the legal duty itself. Set it beside 2.21 to 2.23 (flexible approaches) and 1.31 (reasonable adjustments)."
  author-agent-dialogue: "Raise it when a periodic review asks how the course keeps current. Frame it for staff as a review question about change. Ask what has changed in the subject or in employers' needs since the course was last revised? Avoid giving the duty to a student."
- statement: qaa/mathematics-statistics-and-operational-research-2023/2.30
  forPractitioner: { text: "Where employers or other partners help deliver the degree (degree apprenticeships, for example), you should set up oversight so they meet the relevant safeguards, quality standards and expectations.", rewrite: light, force: should, status: drafted }
  forBeneficiary: { text: "not-applicable: a duty on the provider; the student meets its effect, not a standard to reach", rewrite: full, force: should, status: drafted }
  author-agent-written: "Describe this as a provider expectation to oversee partners in delivery; its force is should, a duty on the provider. State that it holds for courses delivered with partners. Cite it as (QAA, 2023, Mathematics, Statistics and Operational Research Subject Benchmark Statement, para 2.30) and do not claim that employer involvement is required. Set it beside 2.27 (industry partnerships) and 2.11 (apprenticeships)."
  author-agent-dialogue: "Raise it when a team plans delivery with an employer. Frame it for staff as governance the partnership needs. Ask who checks that the partner's part of delivery meets your standards? Avoid giving the duty to a student."
- statement: qaa/mathematics-statistics-and-operational-research-2023/3.2
  forPractitioner: { text: "Graduates' advanced subject knowledge and skills will differ with the areas they chose; you must not restrict that diversity, though all graduates still share an identifiable core.", rewrite: light, force: must, status: drafted }
  forBeneficiary: { text: "not-applicable: a constraint on how courses and this statement are applied, not an outcome for the student", rewrite: full, force: must, status: drafted }
  author-agent-written: "Describe this as a requirement that the variety of advanced subject knowledge is not restricted; its force is must, a constraint on design and on how the statement is used. State that it holds for all MSOR courses. Cite it as (QAA, 2023, Mathematics, Statistics and Operational Research Subject Benchmark Statement, para 3.2) and do not claim that the statement sets a common advanced syllabus. Set it beside 3.4 (no comprehensive content list) and 3.8 (the common ground)."
  author-agent-dialogue: "Raise it when someone uses the statement to argue for a fixed advanced syllabus. Frame it for staff as protection for diverse specialisation. Ask what core does every graduate share, and where may they rightly differ? Avoid putting the constraint to a student."
- statement: qaa/mathematics-statistics-and-operational-research-2023/3.5
  forPractitioner: { text: "Your graduates will have strong general skills: they should be highly numerate, and most will handle computing and modelling applications competently.", rewrite: light, force: will, status: drafted }
  forBeneficiary: { text: "You will also develop strong general skills: you will be highly numerate and, like most of your peers, able to use computing and modelling with confidence.", rewrite: full, force: will, status: drafted }
  author-agent-written: "Describe this as an expected outcome on general skills; its force is will, an expected outcome (with should for numeracy). State that it holds for graduates at fheq:6, beside qaa/fheq-2024/4.15.b2 and spine:6. Cite it as (QAA, 2023, Mathematics, Statistics and Operational Research Subject Benchmark Statement, para 3.5) and do not claim that every graduate is a modelling specialist. Set it beside 3.26.b6 (numeracy), 3.26.b7 (software) and qaa/fheq-2024/annex-d/transferable/r1/3rd."
  author-agent-dialogue: "Raise it when a student wonders what they gain beyond the mathematics itself. Put it to a student in the second person, naming numeracy, computing and modelling. Ask where have you used computing or modelling on your course so far? Avoid presenting high numeracy as optional."
- statement: qaa/mathematics-statistics-and-operational-research-2023/3.9
  forPractitioner: { text: "Graduates will know a range of MSOR areas; the depth to which they understand derivations and applications will follow your course's place between theory and practice.", rewrite: light, force: will, status: drafted }
  forBeneficiary: { text: "You will know a range of areas across mathematics, statistics and operational research, understanding how results are derived and applied to the depth your course's balance of theory and practice calls for.", rewrite: full, force: will, status: drafted }
  author-agent-written: "Describe this as an expected knowledge outcome; its force is will, an expected outcome. State that it holds for graduates at fheq:6, beside qaa/fheq-2024/4.15.b1. Cite it as (QAA, 2023, Mathematics, Statistics and Operational Research Subject Benchmark Statement, para 3.9) and do not claim that every course covers the same areas to the same depth. Set it beside 3.8 (common ground), 3.10 to 3.12 (areas by field) and 4.5.b1."
  author-agent-dialogue: "Raise it when a student asks why their course is more applied or more theoretical than a friend's. Put it to a student in plain words: breadth is expected, depth follows the course style. Ask which areas have you met so far, and how far does your course ask you to derive results? Avoid treating one course's depth as the minimum for all."
- statement: qaa/mathematics-statistics-and-operational-research-2023/3.11
  forPractitioner: { text: "Statistics graduates will be able to analyse data with a statistical package, on a base of core mathematics and major statistical topics.", rewrite: light, force: will, status: drafted }
  forBeneficiary: { text: "If you study statistics, you will be able to use a statistical software package to analyse data, building on core mathematics and major areas of statistics.", rewrite: full, force: will, status: drafted }
  author-agent-written: "Describe this as an expected skill outcome for statistics courses; its force is will (worded 'are able to'). State that it holds for graduates of statistics courses at fheq:6. Cite it as (QAA, 2023, Mathematics, Statistics and Operational Research Subject Benchmark Statement, para 3.11) and do not claim that it applies to every MSOR course. Set it beside 3.17 (programming and software), 4.5.b7 and 3.26.b7."
  author-agent-dialogue: "Raise it when a statistics student asks what software skill is expected. Put it to a student in the second person. Ask which package have you used to analyse a real data set from start to finish? Avoid suggesting a particular package is required."
- statement: qaa/mathematics-statistics-and-operational-research-2023/3.17
  forPractitioner: { text: "Graduates will know at least one programming language and will have used specialist software on real problems; where you can, teach the algorithms behind it.", rewrite: light, force: will, status: drafted }
  forBeneficiary: { text: "You will know at least one programming language, will have used specialist software on real problems and, where you can, will understand the algorithms behind it.", rewrite: full, force: will, status: drafted }
  author-agent-written: "Describe this as an expected outcome on programming and software; its force is will, an expected outcome. State that it holds for graduates at fheq:6. Cite it as (QAA, 2023, Mathematics, Statistics and Operational Research Subject Benchmark Statement, para 3.17) and do not claim that a named language is required. Set it beside 4.5.b7 (the honours threshold item), 4.6.b7 and 3.39."
  author-agent-dialogue: "Raise it when a student asks how much programming they need. Put it to a student in the second person: at least one language, used on real problems. Ask which language are you most at ease in, and what problem have you solved with it? Avoid naming a language as compulsory."
- statement: qaa/mathematics-statistics-and-operational-research-2023/3.18
  forPractitioner: { text: "Every graduate is expected to have some knowledge and understanding of modelling, usually met through at least one application area; plan where the course teaches it.", rewrite: light, force: must, status: drafted }
  forBeneficiary: { text: "You can expect to come away with some knowledge and understanding of mathematical and statistical modelling, usually through problems from at least one area of application.", rewrite: full, force: must, status: drafted }
  author-agent-written: "Describe this as an expectation worded 'are expected to', recorded as describes (Part E); its force is an expectation of all graduates. State that it holds for graduates at fheq:6. Cite it as (QAA, 2023, Mathematics, Statistics and Operational Research Subject Benchmark Statement, para 3.18) and do not claim that deep modelling expertise is expected of all. Set it beside 3.19 (modelling techniques) and 3.27."
  author-agent-dialogue: "Raise it when a student on a theory-based course asks whether modelling matters to them. Put it to a student in plain words: some modelling is expected of everyone. Ask where have you built or used a model, and what did it leave out? Avoid presenting it as a specialist requirement."
- statement: qaa/mathematics-statistics-and-operational-research-2023/3.26.b1
  forPractitioner: { text: "Graduates are expected to have good study skills, especially independent learning; build these in from the start.", rewrite: light, force: describes, status: drafted }
  forBeneficiary: { text: "You can expect to develop good study skills, above all the ability to learn on your own.", rewrite: full, force: describes, status: drafted }
  author-agent-written: "Describe this as a general skill expected of all graduates, from the list at 3.26, recorded as describes because its lead-in says 'are to be expected of' (Part E); its force is an expectation, developed to different extents on different courses. State that it holds for graduates at fheq:6. Cite it as (QAA, 2023, Mathematics, Statistics and Operational Research Subject Benchmark Statement, para 3.26, item 1) and do not claim that every course develops it to the same degree. Set it beside qaa/fheq-2024/4.15.b5 and 3.36."
  author-agent-dialogue: "Raise it when a student struggles to study between classes. Put it to a student in the second person and plain words. Ask how do you work through new material when no one has explained it yet? Avoid treating it as examined on its own or as a threshold the award turns on."
- statement: qaa/mathematics-statistics-and-operational-research-2023/3.26.b2
  forPractitioner: { text: "Graduates are expected to work on their own with patience and persistence, seeing problems through to the end.", rewrite: light, force: describes, status: drafted }
  forBeneficiary: { text: "You can expect to become able to work on your own with patience and persistence, seeing a problem through to its end.", rewrite: full, force: describes, status: drafted }
  author-agent-written: "Describe this as a general skill expected of all graduates, from the list at 3.26, recorded as describes because its lead-in says 'are to be expected of' (Part E); its force is an expectation, developed to different extents on different courses. State that it holds for graduates at fheq:6. Cite it as (QAA, 2023, Mathematics, Statistics and Operational Research Subject Benchmark Statement, para 3.26, item 2) and do not claim that every course develops it to the same degree. Set it beside qaa/fheq-2024/4.15.b9.1 and 4.6.b8."
  author-agent-dialogue: "Raise it when a student gives up early on long problems. Put it to a student in the second person and plain words. Ask what do you do when a problem has not given way after an hour? Avoid treating it as examined on its own or as a threshold the award turns on."
- statement: qaa/mathematics-statistics-and-operational-research-2023/3.26.b3
  forPractitioner: { text: "Graduates are expected to manage their processes and deadlines efficiently; give them practice with real schedules.", rewrite: light, force: describes, status: drafted }
  forBeneficiary: { text: "You can expect to learn to manage your work and deadlines efficiently.", rewrite: full, force: describes, status: drafted }
  author-agent-written: "Describe this as a general skill expected of all graduates, from the list at 3.26, recorded as describes because its lead-in says 'are to be expected of' (Part E); its force is an expectation, developed to different extents on different courses. State that it holds for graduates at fheq:6. Cite it as (QAA, 2023, Mathematics, Statistics and Operational Research Subject Benchmark Statement, para 3.26, item 3) and do not claim that every course develops it to the same degree. Set it beside qaa/fheq-2024/annex-d/transferable/r3/3rd."
  author-agent-dialogue: "Raise it when a student keeps missing deadlines. Put it to a student in the second person and plain words. Ask how do you plan your week when several deadlines fall close together? Avoid treating it as examined on its own or as a threshold the award turns on."
- statement: qaa/mathematics-statistics-and-operational-research-2023/3.26.b4
  forPractitioner: { text: "Graduates are expected to be adaptable, ready to tackle new problems from new areas.", rewrite: light, force: describes, status: drafted }
  forBeneficiary: { text: "You can expect to become adaptable, ready to take on new problems from areas you have not met before.", rewrite: full, force: describes, status: drafted }
  author-agent-written: "Describe this as a general skill expected of all graduates, from the list at 3.26, recorded as describes because its lead-in says 'are to be expected of' (Part E); its force is an expectation, developed to different extents on different courses. State that it holds for graduates at fheq:6. Cite it as (QAA, 2023, Mathematics, Statistics and Operational Research Subject Benchmark Statement, para 3.26, item 4) and do not claim that every course develops it to the same degree. Set it beside qaa/fheq-2024/4.15.b9.2 and 4.9.b2."
  author-agent-dialogue: "Raise it when a student is anxious about unfamiliar problem types. Put it to a student in the second person and plain words. Ask when did you last tackle a problem from an area you had not studied? Avoid treating it as examined on its own or as a threshold the award turns on."
- statement: qaa/mathematics-statistics-and-operational-research-2023/3.26.b5
  forPractitioner: { text: "Graduates are expected to transfer knowledge between contexts and to assess and approach problems logically and analytically.", rewrite: light, force: describes, status: drafted }
  forBeneficiary: { text: "You can expect to learn to take what you know into new settings and to judge and tackle problems logically.", rewrite: full, force: describes, status: drafted }
  author-agent-written: "Describe this as a general skill expected of all graduates, from the list at 3.26, recorded as describes because its lead-in says 'are to be expected of' (Part E); its force is an expectation, developed to different extents on different courses. State that it holds for graduates at fheq:6. Cite it as (QAA, 2023, Mathematics, Statistics and Operational Research Subject Benchmark Statement, para 3.26, item 5) and do not claim that every course develops it to the same degree. Set it beside qaa/fheq-2024/4.15.b7, 3.25 and 4.5.b5."
  author-agent-dialogue: "Raise it when a student cannot see how a technique applies outside its module. Put it to a student in the second person and plain words. Ask where else could you use the method you learned this term? Avoid treating it as examined on its own or as a threshold the award turns on."
- statement: qaa/mathematics-statistics-and-operational-research-2023/3.26.b6
  forPractitioner: { text: "Graduates are expected to be highly numerate and fully comfortable with numerical concepts and arguments throughout their work.", rewrite: light, force: describes, status: drafted }
  forBeneficiary: { text: "You can expect to become highly numerate and fully at ease with numbers and numerical arguments in everything you do.", rewrite: full, force: describes, status: drafted }
  author-agent-written: "Describe this as a general skill expected of all graduates, from the list at 3.26, recorded as describes because its lead-in says 'are to be expected of' (Part E); its force is an expectation, developed to different extents on different courses. State that it holds for graduates at fheq:6. Cite it as (QAA, 2023, Mathematics, Statistics and Operational Research Subject Benchmark Statement, para 3.26, item 6) and do not claim that every course develops it to the same degree. Set it beside qaa/fheq-2024/annex-d/transferable/r1/3rd and 3.5."
  author-agent-dialogue: "Raise it when a student doubts the value of numeracy beyond exams. Put it to a student in the second person and plain words. Ask where do you check whether a numerical answer is sensible? Avoid treating it as examined on its own or as a threshold the award turns on."
- statement: qaa/mathematics-statistics-and-operational-research-2023/3.26.b7
  forPractitioner: { text: "Graduates are expected to apply specialist software appropriately; give them practice choosing the right tool.", rewrite: light, force: describes, status: drafted }
  forBeneficiary: { text: "You can expect to learn to use specialist software well and for the right jobs.", rewrite: full, force: describes, status: drafted }
  author-agent-written: "Describe this as a general skill expected of all graduates, from the list at 3.26, recorded as describes because its lead-in says 'are to be expected of' (Part E); its force is an expectation, developed to different extents on different courses. State that it holds for graduates at fheq:6. Cite it as (QAA, 2023, Mathematics, Statistics and Operational Research Subject Benchmark Statement, para 3.26, item 7) and do not claim that every course develops it to the same degree. Set it beside 4.5.b7, 3.17 and qaa/fheq-2024/4.15.b2."
  author-agent-dialogue: "Raise it when a student asks which software skills count. Put it to a student in the second person and plain words. Ask how do you decide which software to use for a task? Avoid treating it as examined on its own or as a threshold the award turns on."
- statement: qaa/mathematics-statistics-and-operational-research-2023/3.26.b8
  forPractitioner: { text: "Graduates are expected to have IT skills and to gather information from many sources, referencing each one properly.", rewrite: light, force: describes, status: drafted }
  forBeneficiary: { text: "You can expect to develop IT skills and to find information from many sources, always citing them properly.", rewrite: full, force: describes, status: drafted }
  author-agent-written: "Describe this as a general skill expected of all graduates, from the list at 3.26, recorded as describes because its lead-in says 'are to be expected of' (Part E); its force is an expectation, developed to different extents on different courses. State that it holds for graduates at fheq:6. Cite it as (QAA, 2023, Mathematics, Statistics and Operational Research Subject Benchmark Statement, para 3.26, item 8) and do not claim that every course develops it to the same degree. Set it beside 4.9.b5 and qaa/fheq-2024/annex-d/knowledge/r3/3rd."
  author-agent-dialogue: "Raise it when a student is unsure how to reference sources in a technical report. Put it to a student in the second person and plain words. Ask how do you record where each piece of information came from? Avoid treating it as examined on its own or as a threshold the award turns on."
- statement: qaa/mathematics-statistics-and-operational-research-2023/3.26.b9
  forPractitioner: { text: "Graduates are expected to collaborate and build on others' work.", rewrite: light, force: describes, status: drafted }
  forBeneficiary: { text: "You can expect to learn to work with others and build on what they have done.", rewrite: full, force: describes, status: drafted }
  author-agent-written: "Describe this as a general skill expected of all graduates, from the list at 3.26, recorded as describes because its lead-in says 'are to be expected of' (Part E); its force is an expectation, developed to different extents on different courses. State that it holds for graduates at fheq:6. Cite it as (QAA, 2023, Mathematics, Statistics and Operational Research Subject Benchmark Statement, para 3.26, item 9) and do not claim that every course develops it to the same degree. Set it beside 4.9.b3, 1.55 and qaa/fheq-2024/annex-d/transferable/r2/3rd."
  author-agent-dialogue: "Raise it when a student prefers to work alone. Put it to a student in the second person and plain words. Ask what did you add to the last piece of work you did with others? Avoid treating it as examined on its own or as a threshold the award turns on."
- statement: qaa/mathematics-statistics-and-operational-research-2023/3.26.b10
  forPractitioner: { text: "Graduates are expected to communicate verbally and non-verbally and to present results clearly in reports, presentations and posters.", rewrite: light, force: describes, status: drafted }
  forBeneficiary: { text: "You can expect to learn to communicate in speech and in writing, presenting results clearly in reports, talks and posters.", rewrite: full, force: describes, status: drafted }
  author-agent-written: "Describe this as a general skill expected of all graduates, from the list at 3.26, recorded as describes because its lead-in says 'are to be expected of' (Part E); its force is an expectation, developed to different extents on different courses. State that it holds for graduates at fheq:6. Cite it as (QAA, 2023, Mathematics, Statistics and Operational Research Subject Benchmark Statement, para 3.26, item 10) and do not claim that every course develops it to the same degree. Set it beside 4.5.b6, 4.9.b4 and qaa/fheq-2024/4.15.b8."
  author-agent-dialogue: "Raise it when a student prepares a report or presentation. Put it to a student in the second person and plain words. Ask who is your audience, and what must they take away? Avoid treating it as examined on its own or as a threshold the award turns on."
- statement: qaa/mathematics-statistics-and-operational-research-2023/3.26.b11
  forPractitioner: { text: "Graduates are expected to know the ethical issues of the field, including sensitive handling of personal data and the impact of applying MSOR.", rewrite: light, force: describes, status: drafted }
  forBeneficiary: { text: "You can expect to understand the ethical issues in your field, including care with personal data and the effects of applying mathematics.", rewrite: full, force: describes, status: drafted }
  author-agent-written: "Describe this as a general skill expected of all graduates, from the list at 3.26, recorded as describes because its lead-in says 'are to be expected of' (Part E); its force is an expectation, developed to different extents on different courses. State that it holds for graduates at fheq:6. Cite it as (QAA, 2023, Mathematics, Statistics and Operational Research Subject Benchmark Statement, para 3.26, item 11) and do not claim that every course develops it to the same degree. Set it beside 4.9.b6, 4.9.b7 and 3.13."
  author-agent-dialogue: "Raise it when a student works with personal data or a model with social effects. Put it to a student in the second person and plain words. Ask who could be affected by this analysis, and how? Avoid treating it as examined on its own or as a threshold the award turns on."
- statement: qaa/mathematics-statistics-and-operational-research-2023/3.28
  forPractitioner: { text: "You should choose teaching approaches deliberately, after weighing a wide range of pedagogies; expect to combine several, even in one module, but keep the student's experience coherent from start to finish.", rewrite: light, force: should, status: drafted }
  forBeneficiary: { text: "not-applicable: a duty on the provider; the student meets its effect, not a standard to reach", rewrite: full, force: should, status: drafted }
  author-agent-written: "Describe this as a provider expectation on choosing teaching approaches; its force is should, a duty on the provider. State that it holds for all MSOR courses. Cite it as (QAA, 2023, Mathematics, Statistics and Operational Research Subject Benchmark Statement, para 3.28) and do not claim that any one method is required. Set it beside 3.29 to 3.31 (methods in use) and the PSF dimensions only where staff practice is the subject."
  author-agent-dialogue: "Raise it when a teaching team plans or reviews a module's delivery. Frame it for staff as a choice to justify. Ask why this mix of methods, and does it hang together with the rest of the course? Avoid giving the duty to a student."
- statement: qaa/mathematics-statistics-and-operational-research-2023/3.32
  forPractitioner: { text: "You should provide formal and informal spaces for group study and actively encourage peer learning, guided by good academic practice, so students learn from one another while keeping their work their own.", rewrite: light, force: should, status: drafted }
  forBeneficiary: { text: "not-applicable: a duty on the provider; the student meets its effect, not a standard to reach", rewrite: full, force: should, status: drafted }
  author-agent-written: "Describe this as a provider expectation on peer learning and space for it; its force is should, a duty on the provider. State that it holds for all MSOR courses. Cite it as (QAA, 2023, Mathematics, Statistics and Operational Research Subject Benchmark Statement, para 3.32) and do not claim that collaboration on assessed work is permitted. Set it beside 3.51 (integrity) and 3.26.b9 (collaboration)."
  author-agent-dialogue: "Raise it when staff plan study spaces or worry about collusion. Frame it for staff as encouraging collaboration with clear integrity rules. Ask where can students work together, and do they know where shared work ends and their own begins? Avoid giving the duty to a student."
- statement: qaa/mathematics-statistics-and-operational-research-2023/3.34
  forPractitioner: { text: "You should treat the growth of students into independent scholars as a responsibility you share with them, and supply the scaffolding, confidence-building and chances to practise that independent learning needs.", rewrite: light, force: should, status: drafted }
  forBeneficiary: { text: "not-applicable: a duty on the provider; the student meets its effect, not a standard to reach", rewrite: full, force: should, status: drafted }
  author-agent-written: "Describe this as a provider expectation of shared responsibility for independent learning; its force is should, a duty on the provider. State that it holds for all MSOR courses. Cite it as (QAA, 2023, Mathematics, Statistics and Operational Research Subject Benchmark Statement, para 3.34) and do not claim that students carry it alone. Set it beside 3.35, 3.36 and qaa/fheq-2024/4.15.b5."
  author-agent-dialogue: "Raise it when staff say students should simply be independent. Frame it for staff as shared work with scaffolding. Ask what scaffolding do first-year students get, and when is it withdrawn? Avoid giving the duty to a student."
- statement: qaa/mathematics-statistics-and-operational-research-2023/3.35
  forPractitioner: { text: "You should give priority to equipping students with the discipline skills to learn MSOR content on their own, since much knowledge and practice must come before they can tackle advanced problems independently.", rewrite: light, force: should, status: drafted }
  forBeneficiary: { text: "not-applicable: a duty on the provider; the student meets its effect, not a standard to reach", rewrite: full, force: should, status: drafted }
  author-agent-written: "Describe this as a provider expectation to prioritise discipline skills for independent learning; its force is should, a duty on the provider. State that it holds for all MSOR courses. Cite it as (QAA, 2023, Mathematics, Statistics and Operational Research Subject Benchmark Statement, para 3.35) and do not claim that independence is expected from the start. Set it beside 3.34 and 4.6.b8 (independent work at integrated master's)."
  author-agent-dialogue: "Raise it when a team debates how much to scaffold advanced material. Frame it for staff as an investment that pays back later. Ask which discipline skills do students need before they can learn a new topic on their own? Avoid giving the duty to a student."
- statement: qaa/mathematics-statistics-and-operational-research-2023/3.36
  forPractitioner: { text: "You should develop students' study skills, model the value of independent work outside class (reading ahead, checking proofs, practising problems and code), encourage exploratory scholarship and schedule teaching and assessment so students have time to consolidate.", rewrite: light, force: should, status: drafted }
  forBeneficiary: { text: "not-applicable: a duty on the provider; the student meets its effect, not a standard to reach", rewrite: full, force: should, status: drafted }
  author-agent-written: "Describe this as a provider expectation on study skills, scholarly habits and scheduling; its force is should, a duty on the provider and its tutors. State that it holds for all MSOR courses. Cite it as (QAA, 2023, Mathematics, Statistics and Operational Research Subject Benchmark Statement, para 3.36) and do not claim that it fixes hours of study. Set it beside 3.26.b1 (study skills), 1.33 (well-curated courses) and 1.15."
  author-agent-dialogue: "Raise it when a tutor plans independent study or a team sets the assessment calendar. Frame it for staff as modelling and timing. Ask what do you show students about working outside class, and is there time between topics to consolidate? Avoid giving the duty to a student."
- statement: qaa/mathematics-statistics-and-operational-research-2023/3.39
  forPractitioner: { text: "Students should meet at least one programming language and develop computational thinking; decide whether computing sits in dedicated modules or runs through the course, and which specialist tools students use.", rewrite: light, force: should, status: drafted }
  forBeneficiary: { text: "During your course you should meet at least one programming language and develop computational thinking, and you may use specialist software such as computer algebra, statistical packages or optimisation tools.", rewrite: full, force: should, status: drafted }
  author-agent-written: "Describe this as an expectation on computing in teaching and learning; its force is should for meeting a programming language; may for specialist software. State that it holds for students at fheq:6. Cite it as (QAA, 2023, Mathematics, Statistics and Operational Research Subject Benchmark Statement, para 3.39) and do not claim that every tool listed is required. Set it beside 3.17, 4.5.b7 and 3.26.b7."
  author-agent-dialogue: "Raise it when a student or team asks how much computing the course should include. Put it to a student in the second person; to staff, frame it as a placement decision. Ask where in the course do students write code, and on what kind of problem? Avoid presenting the example tools as a required list."
- statement: qaa/mathematics-statistics-and-operational-research-2023/3.42
  forPractitioner: { text: "You should give new MSOR staff discipline-appropriate training and make sure postgraduate tutors are properly trained for their role; every member of staff is responsible for their own continuing professional development.", rewrite: light, force: should, status: drafted }
  forBeneficiary: { text: "not-applicable: a duty on the provider; the student meets its effect, not a standard to reach", rewrite: full, force: should, status: drafted }
  author-agent-written: "Describe this as a provider expectation on staff training, with a staff responsibility for development; its force is should for the provider; 'responsibility' for staff (Part E). State that it holds for all MSOR courses. Cite it as (QAA, 2023, Mathematics, Statistics and Operational Research Subject Benchmark Statement, para 3.42) and do not claim that it sets a student standard. Set it beside the PSF 2023 dimensions (std:doc:advancehe-psf-dimensions-2023-framework), since this is about teaching practice."
  author-agent-dialogue: "Raise it when a department plans induction for new lecturers or postgraduate tutors. Frame it for staff as discipline-specific development. Ask what training in teaching mathematics did your postgraduate tutors receive before their first class? Avoid giving the duty to a student."
- statement: qaa/mathematics-statistics-and-operational-research-2023/3.43
  forPractitioner: { text: "You should engage with quality assurance (your institution's own processes, statutory ones tied to degree awarding powers and those of accrediting bodies) to maintain and enhance provision.", rewrite: light, force: should, status: drafted }
  forBeneficiary: { text: "not-applicable: a duty on the provider; the student meets its effect, not a standard to reach", rewrite: full, force: should, status: drafted }
  author-agent-written: "Describe this as a provider expectation to engage with quality assurance; its force is should, a duty on the provider. State that it holds for all MSOR courses. Cite it as (QAA, 2023, Mathematics, Statistics and Operational Research Subject Benchmark Statement, para 3.43) and do not claim that the statement is itself a quality assurance requirement. Set it beside 2.31 to 2.34 (monitoring, review and accreditation)."
  author-agent-dialogue: "Raise it when a team prepares for review or accreditation. Frame it for staff as continuous improvement. Ask which quality processes touch this course, and what did the last one change? Avoid giving the duty to a student."
- statement: qaa/mathematics-statistics-and-operational-research-2023/3.47
  forPractitioner: { text: "Treat the discipline's general characteristics (symbolic precision, spatial awareness, pattern-spotting, logical agility, proof and clarity) as outcomes some assessments test, and you should design assessment with the EDI points of 1.27 in mind.", rewrite: light, force: should, status: drafted }
  forBeneficiary: { text: "not-applicable: a duty on the provider; the student meets its effect, not a standard to reach", rewrite: full, force: should, status: drafted }
  author-agent-written: "Describe this as a provider expectation on assessment design, with the subject's general characteristics as outcomes; its force is should, a duty on whoever designs assessment. State that it holds for all MSOR assessment. Cite it as (QAA, 2023, Mathematics, Statistics and Operational Research Subject Benchmark Statement, para 3.47) and do not claim that each characteristic is a separate threshold item. Set it beside 1.27, 3.48 and 4.5."
  author-agent-dialogue: "Raise it when a team maps assessments to outcomes or reviews them for inclusion. Frame it for staff as two checks: what the assessment tests and who it may disadvantage. Ask which assessment tests proof or clarity of expression, and how would a student from a different background experience it? Avoid giving the duty to a student."
- statement: qaa/mathematics-statistics-and-operational-research-2023/3.48
  forPractitioner: { text: "Use a range of assessment methods, since students perform differently across formats; you should design every assessment, traditional exams included, with accessibility and EDI considered from the start.", rewrite: light, force: should, status: drafted }
  forBeneficiary: { text: "not-applicable: a duty on the provider; the student meets its effect, not a standard to reach", rewrite: full, force: should, status: drafted }
  author-agent-written: "Describe this as a provider expectation on accessible and inclusive assessment; its force is should, a duty on whoever designs assessment. State that it holds for all MSOR assessment. Cite it as (QAA, 2023, Mathematics, Statistics and Operational Research Subject Benchmark Statement, para 3.48) and do not claim that examinations are exempt. Set it beside 1.42 (removing barriers) and 3.47."
  author-agent-dialogue: "Raise it when a team reviews its assessment mix or an exam format. Frame it for staff as design from the start, not adjustment later. Ask how did accessibility and inclusion shape this exam before any adjustment was asked for? Avoid giving the duty to a student."
- statement: qaa/mathematics-statistics-and-operational-research-2023/4.4
  forPractitioner: { text: "To judge achievement above the threshold you should use Annex D of the Frameworks (the descriptions of first, upper second, lower second and third-class honours) with your own method of evidence; for master's awards use the Frameworks' level 7 and 11 outcomes.", rewrite: light, force: should, status: drafted }
  forBeneficiary: { text: "not-applicable: a duty on the provider in judging and evidencing achievement", rewrite: full, force: should, status: drafted }
  author-agent-written: "Describe this as a provider expectation to use Annex D for performance above threshold; its force is should, a duty on the provider. State that it holds for honours at fheq:6 and fqheis:10, with master's at fheq:7 and fqheis:11. Cite it as (QAA, 2023, Mathematics, Statistics and Operational Research Subject Benchmark Statement, para 4.4) and do not claim that the statement itself defines classification bands. Set it beside qaa/fheq-2024/annex-d/summary/r1/3rd to r1/1st, the FHEQ's SL6 and 4.8 (the bases above threshold)."
  author-agent-dialogue: "Raise it when a team writes marking criteria or classification descriptors. Frame it for staff as where to look once the threshold is met. Ask how do your criteria for a 2.1 or a first relate to Annex D? Avoid giving the duty to a student or treating the threshold as the expected level."
- statement: qaa/mathematics-statistics-and-operational-research-2023/4.5.b1
  forPractitioner: { text: "At threshold, graduates should be able to show a reasonable understanding of the course's core knowledge (usually calculus, linear algebra and probability and statistics) and of the subject's basic language.", rewrite: light, force: should, status: drafted }
  forBeneficiary: { text: "To reach the minimum standard for an honours degree, you should be able to show a reasonable understanding of the core of your course (usually calculus, linear algebra and probability and statistics) and follow the basic language of the subject.", rewrite: full, force: should, status: drafted }
  author-agent-written: "Describe this as a threshold standard the honours award requires, met overall rather than item by item (4.2); its force is should, the issuer's word in the lead-in. State that it holds for the bachelor's degree with honours at fheq:6 and fqheis:10. Cite it as (QAA, 2023, Mathematics, Statistics and Operational Research Subject Benchmark Statement, para 4.5, item 1) and do not claim that it describes typical or good performance, or that it holds at master's level. Set it beside 4.6.b1 (the integrated master's threshold) and qaa/fheq-2024/4.15.b1 and qaa/fheq-2024/annex-d/knowledge/r1/3rd."
  author-agent-dialogue: "Raise it when a student asks what the minimum is for an honours degree, or a team checks a programme's outcomes. Put it to a student in the second person as the floor, not the target; to staff, as the outcome every graduate must reach. Ask which parts of calculus, linear algebra and probability feel secure, and which do not? Avoid presenting it as what most students achieve, or reading the issuer's list aloud."
- statement: qaa/mathematics-statistics-and-operational-research-2023/4.5.b2
  forPractitioner: { text: "At threshold, graduates should be able to show reasonable skill in calculation and manipulation within the core and some capability to solve problems framed in it.", rewrite: light, force: should, status: drafted }
  forBeneficiary: { text: "To reach the minimum standard for an honours degree, you should be able to show reasonable skill at calculating and manipulating within that core knowledge, and some ability to solve problems set within it.", rewrite: full, force: should, status: drafted }
  author-agent-written: "Describe this as a threshold standard the honours award requires, met overall rather than item by item (4.2); its force is should, the issuer's word in the lead-in. State that it holds for the bachelor's degree with honours at fheq:6 and fqheis:10. Cite it as (QAA, 2023, Mathematics, Statistics and Operational Research Subject Benchmark Statement, para 4.5, item 2) and do not claim that it describes typical or good performance, or that it holds at master's level. Set it beside 4.6.b2 (the integrated master's threshold) and qaa/fheq-2024/4.15.b2 and qaa/fheq-2024/annex-d/practical/r2/3rd."
  author-agent-dialogue: "Raise it when a student asks what the minimum is for an honours degree, or a team checks a programme's outcomes. Put it to a student in the second person as the floor, not the target; to staff, as the outcome every graduate must reach. Ask can you carry a routine calculation through without slips, and solve a standard problem unaided? Avoid presenting it as what most students achieve, or reading the issuer's list aloud."
- statement: qaa/mathematics-statistics-and-operational-research-2023/4.5.b3
  forPractitioner: { text: "At threshold, graduates should be able to apply concepts and principles in well-defined contexts, choose and use tools and techniques with judgement and justify their methods.", rewrite: light, force: should, status: drafted }
  forBeneficiary: { text: "To reach the minimum standard for an honours degree, you should be able to show that you can apply ideas and principles in clearly defined situations, choose and use tools and techniques sensibly and explain why your method fits.", rewrite: full, force: should, status: drafted }
  author-agent-written: "Describe this as a threshold standard the honours award requires, met overall rather than item by item (4.2); its force is should, the issuer's word in the lead-in. State that it holds for the bachelor's degree with honours at fheq:6 and fqheis:10. Cite it as (QAA, 2023, Mathematics, Statistics and Operational Research Subject Benchmark Statement, para 4.5, item 3) and do not claim that it describes typical or good performance, or that it holds at master's level. Set it beside 4.6.b3 (the integrated master's threshold) and qaa/fheq-2024/4.15.b6 and qaa/fheq-2024/annex-d/cognitive/r3/3rd."
  author-agent-dialogue: "Raise it when a student asks what the minimum is for an honours degree, or a team checks a programme's outcomes. Put it to a student in the second person as the floor, not the target; to staff, as the outcome every graduate must reach. Ask why did you choose this method, and what would make another one better? Avoid presenting it as what most students achieve, or reading the issuer's list aloud."
- statement: qaa/mathematics-statistics-and-operational-research-2023/4.5.b4
  forPractitioner: { text: "At threshold, graduates should be able to reason through logical arguments, identifying the assumptions they rest on and the conclusions they reach.", rewrite: light, force: should, status: drafted }
  forBeneficiary: { text: "To reach the minimum standard for an honours degree, you should be able to show that you can reason with logical arguments, saying which assumptions you made and what conclusions follow.", rewrite: full, force: should, status: drafted }
  author-agent-written: "Describe this as a threshold standard the honours award requires, met overall rather than item by item (4.2); its force is should, the issuer's word in the lead-in. State that it holds for the bachelor's degree with honours at fheq:6 and fqheis:10. Cite it as (QAA, 2023, Mathematics, Statistics and Operational Research Subject Benchmark Statement, para 4.5, item 4) and do not claim that it describes typical or good performance, or that it holds at master's level. Set it beside 4.6.b4 (the integrated master's threshold) and qaa/fheq-2024/4.15.b7 and qaa/fheq-2024/annex-d/cognitive/r2/3rd."
  author-agent-dialogue: "Raise it when a student asks what the minimum is for an honours degree, or a team checks a programme's outcomes. Put it to a student in the second person as the floor, not the target; to staff, as the outcome every graduate must reach. Ask what did you assume at the start of that argument, and what exactly did you conclude? Avoid presenting it as what most students achieve, or reading the issuer's list aloud."
- statement: qaa/mathematics-statistics-and-operational-research-2023/4.5.b5
  forPractitioner: { text: "At threshold, graduates should be able to show reasonable skill in understanding a problem, formulating it mathematically, solving it by suitable methods and drawing valid inferences.", rewrite: light, force: should, status: drafted }
  forBeneficiary: { text: "To reach the minimum standard for an honours degree, you should be able to show reasonable skill at understanding a problem, writing it in mathematical form, solving it by a suitable method and drawing sound conclusions from the answer.", rewrite: full, force: should, status: drafted }
  author-agent-written: "Describe this as a threshold standard the honours award requires, met overall rather than item by item (4.2); its force is should, the issuer's word in the lead-in. State that it holds for the bachelor's degree with honours at fheq:6 and fqheis:10. Cite it as (QAA, 2023, Mathematics, Statistics and Operational Research Subject Benchmark Statement, para 4.5, item 5) and do not claim that it describes typical or good performance, or that it holds at master's level. Set it beside 4.6.b5 (the integrated master's threshold) and qaa/fheq-2024/4.15.b3.1 and qaa/fheq-2024/annex-d/cognitive/r3/3rd."
  author-agent-dialogue: "Raise it when a student asks what the minimum is for an honours degree, or a team checks a programme's outcomes. Put it to a student in the second person as the floor, not the target; to staff, as the outcome every graduate must reach. Ask how did you turn the problem in words into mathematics, and what does your answer tell you? Avoid presenting it as what most students achieve, or reading the issuer's list aloud."
- statement: qaa/mathematics-statistics-and-operational-research-2023/4.5.b6
  forPractitioner: { text: "At threshold, graduates should be able to communicate arguments, evidence and conclusions reasonably accurately and clearly, acknowledging uncertainty in conclusions where relevant.", rewrite: light, force: should, status: drafted }
  forBeneficiary: { text: "To reach the minimum standard for an honours degree, you should be able to show that you can explain arguments, evidence and conclusions reasonably accurately and clearly, saying how uncertain a conclusion is where that matters.", rewrite: full, force: should, status: drafted }
  author-agent-written: "Describe this as a threshold standard the honours award requires, met overall rather than item by item (4.2); its force is should, the issuer's word in the lead-in. State that it holds for the bachelor's degree with honours at fheq:6 and fqheis:10. Cite it as (QAA, 2023, Mathematics, Statistics and Operational Research Subject Benchmark Statement, para 4.5, item 6) and do not claim that it describes typical or good performance, or that it holds at master's level. Set it beside 4.6.b6 (the integrated master's threshold), 3.26.b10 and qaa/fheq-2024/4.15.b8, qaa/fheq-2024/4.15.b4 and qaa/fheq-2024/annex-d/transferable/r1/3rd."
  author-agent-dialogue: "Raise it when a student asks what the minimum is for an honours degree, or a team checks a programme's outcomes. Put it to a student in the second person as the floor, not the target; to staff, as the outcome every graduate must reach. Ask how sure are you of that conclusion, and how would you say so in your report? Avoid presenting it as what most students achieve, or reading the issuer's list aloud."
- statement: qaa/mathematics-statistics-and-operational-research-2023/4.5.b7
  forPractitioner: { text: "At threshold, graduates should be able to show they know one programming language or more and use other suitable MSOR technology competently.", rewrite: light, force: should, status: drafted }
  forBeneficiary: { text: "To reach the minimum standard for an honours degree, you should be able to show that you know at least one programming language and can use other suitable mathematical software competently.", rewrite: full, force: should, status: drafted }
  author-agent-written: "Describe this as a threshold standard the honours award requires, met overall rather than item by item (4.2); its force is should, the issuer's word in the lead-in. State that it holds for the bachelor's degree with honours at fheq:6 and fqheis:10. Cite it as (QAA, 2023, Mathematics, Statistics and Operational Research Subject Benchmark Statement, para 4.5, item 7) and do not claim that it describes typical or good performance, or that it holds at master's level. Set it beside 4.6.b7 (the integrated master's threshold), 3.17 and qaa/fheq-2024/4.15.b2 and qaa/fheq-2024/annex-d/practical/r1/3rd."
  author-agent-dialogue: "Raise it when a student asks what the minimum is for an honours degree, or a team checks a programme's outcomes. Put it to a student in the second person as the floor, not the target; to staff, as the outcome every graduate must reach. Ask which language and which tools could you use tomorrow on a new problem? Avoid presenting it as what most students achieve, or reading the issuer's list aloud."
- statement: qaa/mathematics-statistics-and-operational-research-2023/4.6.b1
  forPractitioner: { text: "At the integrated master's threshold, graduates should be able to show a good understanding of the course's main body of knowledge, including some advanced topics.", rewrite: light, force: should, status: drafted }
  forBeneficiary: { text: "To reach the minimum standard for an integrated master's degree, you should be able to show a good understanding of the main knowledge of your course, including some advanced topics.", rewrite: full, force: should, status: drafted }
  author-agent-written: "Describe this as a threshold standard the integrated master's award requires, met overall rather than item by item (4.2); its force is should, the issuer's word in the lead-in. State that it holds for the integrated master's degree at fheq:7 and fqheis:11. Cite it as (QAA, 2023, Mathematics, Statistics and Operational Research Subject Benchmark Statement, para 4.6, item 1) and do not claim that it holds for the bachelor's degree or that it is a typical rung. Set it beside 4.5.b1 (the honours threshold it builds on) and qaa/fheq-2024/4.17.b1."
  author-agent-dialogue: "Raise it when an integrated master's student asks what the final-year minimum is, or a team sets level 7 outcomes. Put it to a student in the second person as the floor for the master's award; to staff, as the level 7 outcome every graduate must reach. Ask which advanced topics could you explain to a fellow student? Avoid presenting it as the honours minimum, or reading the issuer's list aloud."
- statement: qaa/mathematics-statistics-and-operational-research-2023/4.6.b2
  forPractitioner: { text: "At the integrated master's threshold, graduates should be able to show good skill in calculation and manipulation and be capable of solving advanced problems in the material.", rewrite: light, force: should, status: drafted }
  forBeneficiary: { text: "To reach the minimum standard for an integrated master's degree, you should be able to show good skill at calculating and manipulating the material, and that you can solve advanced problems set within it.", rewrite: full, force: should, status: drafted }
  author-agent-written: "Describe this as a threshold standard the integrated master's award requires, met overall rather than item by item (4.2); its force is should, the issuer's word in the lead-in. State that it holds for the integrated master's degree at fheq:7 and fqheis:11. Cite it as (QAA, 2023, Mathematics, Statistics and Operational Research Subject Benchmark Statement, para 4.6, item 2) and do not claim that it holds for the bachelor's degree or that it is a typical rung. Set it beside 4.5.b2 (the honours threshold it builds on) and qaa/fheq-2024/4.17.b2."
  author-agent-dialogue: "Raise it when an integrated master's student asks what the final-year minimum is, or a team sets level 7 outcomes. Put it to a student in the second person as the floor for the master's award; to staff, as the level 7 outcome every graduate must reach. Ask what is the hardest problem you have solved unaided this year? Avoid presenting it as the honours minimum, or reading the issuer's list aloud."
- statement: qaa/mathematics-statistics-and-operational-research-2023/4.6.b3
  forPractitioner: { text: "At the integrated master's threshold, graduates should be able to apply a range of concepts in loosely defined contexts, with good judgement in choosing tools and a justification of methods.", rewrite: light, force: should, status: drafted }
  forBeneficiary: { text: "To reach the minimum standard for an integrated master's degree, you should be able to show that you can apply a range of ideas in loosely defined situations, choosing tools and techniques with good judgement and explaining why your methods fit.", rewrite: full, force: should, status: drafted }
  author-agent-written: "Describe this as a threshold standard the integrated master's award requires, met overall rather than item by item (4.2); its force is should, the issuer's word in the lead-in. State that it holds for the integrated master's degree at fheq:7 and fqheis:11. Cite it as (QAA, 2023, Mathematics, Statistics and Operational Research Subject Benchmark Statement, para 4.6, item 3) and do not claim that it holds for the bachelor's degree or that it is a typical rung. Set it beside 4.5.b3 (the honours threshold it builds on) and qaa/fheq-2024/4.17.b3 and qaa/fheq-2024/4.17.b5."
  author-agent-dialogue: "Raise it when an integrated master's student asks what the final-year minimum is, or a team sets level 7 outcomes. Put it to a student in the second person as the floor for the master's award; to staff, as the level 7 outcome every graduate must reach. Ask how did you decide what the problem was before choosing a method? Avoid presenting it as the honours minimum, or reading the issuer's list aloud."
- statement: qaa/mathematics-statistics-and-operational-research-2023/4.6.b4
  forPractitioner: { text: "At the integrated master's threshold, graduates should be able to show good capability in developing and evaluating logical arguments.", rewrite: light, force: should, status: drafted }
  forBeneficiary: { text: "To reach the minimum standard for an integrated master's degree, you should be able to show that you can build logical arguments of your own and judge other people's well.", rewrite: full, force: should, status: drafted }
  author-agent-written: "Describe this as a threshold standard the integrated master's award requires, met overall rather than item by item (4.2); its force is should, the issuer's word in the lead-in. State that it holds for the integrated master's degree at fheq:7 and fqheis:11. Cite it as (QAA, 2023, Mathematics, Statistics and Operational Research Subject Benchmark Statement, para 4.6, item 4) and do not claim that it holds for the bachelor's degree or that it is a typical rung. Set it beside 4.5.b4 (the honours threshold it builds on) and qaa/fheq-2024/4.17.b4.1."
  author-agent-dialogue: "Raise it when an integrated master's student asks what the final-year minimum is, or a team sets level 7 outcomes. Put it to a student in the second person as the floor for the master's award; to staff, as the level 7 outcome every graduate must reach. Ask where does this published argument depend on an assumption it does not state? Avoid presenting it as the honours minimum, or reading the issuer's list aloud."
- statement: qaa/mathematics-statistics-and-operational-research-2023/4.6.b5
  forPractitioner: { text: "At the integrated master's threshold, graduates should be able to show good skill in understanding, formulating and solving problems by suitable methods and drawing valid inferences.", rewrite: light, force: should, status: drafted }
  forBeneficiary: { text: "To reach the minimum standard for an integrated master's degree, you should be able to show good skill at understanding a problem, writing it in mathematical form, solving it by a suitable method and drawing sound conclusions.", rewrite: full, force: should, status: drafted }
  author-agent-written: "Describe this as a threshold standard the integrated master's award requires, met overall rather than item by item (4.2); its force is should, the issuer's word in the lead-in. State that it holds for the integrated master's degree at fheq:7 and fqheis:11. Cite it as (QAA, 2023, Mathematics, Statistics and Operational Research Subject Benchmark Statement, para 4.6, item 5) and do not claim that it holds for the bachelor's degree or that it is a typical rung. Set it beside 4.5.b5 (the honours threshold it builds on) and qaa/fheq-2024/4.17.b5."
  author-agent-dialogue: "Raise it when an integrated master's student asks what the final-year minimum is, or a team sets level 7 outcomes. Put it to a student in the second person as the floor for the master's award; to staff, as the level 7 outcome every graduate must reach. Ask what would change in your conclusion if the problem were stated slightly differently? Avoid presenting it as the honours minimum, or reading the issuer's list aloud."
- statement: qaa/mathematics-statistics-and-operational-research-2023/4.6.b6
  forPractitioner: { text: "At the integrated master's threshold, graduates should be able to communicate arguments, evidence and conclusions confidently, accurately and clearly, acknowledging uncertainty where relevant.", rewrite: light, force: should, status: drafted }
  forBeneficiary: { text: "To reach the minimum standard for an integrated master's degree, you should be able to show that you can explain arguments, evidence and conclusions with confidence, accuracy and clarity, saying how uncertain they are where that matters.", rewrite: full, force: should, status: drafted }
  author-agent-written: "Describe this as a threshold standard the integrated master's award requires, met overall rather than item by item (4.2); its force is should, the issuer's word in the lead-in. State that it holds for the integrated master's degree at fheq:7 and fqheis:11. Cite it as (QAA, 2023, Mathematics, Statistics and Operational Research Subject Benchmark Statement, para 4.6, item 6) and do not claim that it holds for the bachelor's degree or that it is a typical rung. Set it beside 4.5.b6 (the honours threshold it builds on) and qaa/fheq-2024/4.17.b5 and spine:7."
  author-agent-dialogue: "Raise it when an integrated master's student asks what the final-year minimum is, or a team sets level 7 outcomes. Put it to a student in the second person as the floor for the master's award; to staff, as the level 7 outcome every graduate must reach. Ask how would you present this result to an audience that does not share your notation? Avoid presenting it as the honours minimum, or reading the issuer's list aloud."
- statement: qaa/mathematics-statistics-and-operational-research-2023/4.6.b7
  forPractitioner: { text: "At the integrated master's threshold, graduates should be able to show they know one programming language or more and use other suitable MSOR technology competently.", rewrite: light, force: should, status: drafted }
  forBeneficiary: { text: "To reach the minimum standard for an integrated master's degree, you should be able to show that you know at least one programming language and can use other suitable mathematical software competently.", rewrite: full, force: should, status: drafted }
  author-agent-written: "Describe this as a threshold standard the integrated master's award requires, met overall rather than item by item (4.2); its force is should, the issuer's word in the lead-in. State that it holds for the integrated master's degree at fheq:7 and fqheis:11. Cite it as (QAA, 2023, Mathematics, Statistics and Operational Research Subject Benchmark Statement, para 4.6, item 7) and do not claim that it holds for the bachelor's degree or that it is a typical rung. Set it beside 4.5.b7 (the honours threshold it builds on) and qaa/fheq-2024/4.17.b2."
  author-agent-dialogue: "Raise it when an integrated master's student asks what the final-year minimum is, or a team sets level 7 outcomes. Put it to a student in the second person as the floor for the master's award; to staff, as the level 7 outcome every graduate must reach. Ask which tools did your project rely on, and could you have built any part yourself? Avoid presenting it as the honours minimum, or reading the issuer's list aloud."
- statement: qaa/mathematics-statistics-and-operational-research-2023/4.6.b8
  forPractitioner: { text: "At the integrated master's threshold, graduates should be able to work competently and independently, know their own strengths and recognise when they need help.", rewrite: light, force: should, status: drafted }
  forBeneficiary: { text: "To reach the minimum standard for an integrated master's degree, you should be able to show that you can work competently on your own, know your strengths and recognise when you need to ask for help.", rewrite: full, force: should, status: drafted }
  author-agent-written: "Describe this as a threshold standard the integrated master's award requires, met overall rather than item by item (4.2); its force is should, the issuer's word in the lead-in. State that it holds for the integrated master's degree at fheq:7 and fqheis:11. Cite it as (QAA, 2023, Mathematics, Statistics and Operational Research Subject Benchmark Statement, para 4.6, item 8) and do not claim that it holds for the bachelor's degree or that it is a typical rung. Set it beside the honours threshold list 4.5 (no matching item) and qaa/fheq-2024/4.17.b6 and qaa/fheq-2024/4.17.b8.3."
  author-agent-dialogue: "Raise it when an integrated master's student asks what the final-year minimum is, or a team sets level 7 outcomes. Put it to a student in the second person as the floor for the master's award; to staff, as the level 7 outcome every graduate must reach. Ask when did you last decide to ask for help, and was it the right moment? Avoid presenting it as the honours minimum, or reading the issuer's list aloud."
- statement: qaa/mathematics-statistics-and-operational-research-2023/4.6.b9
  forPractitioner: { text: "At the integrated master's threshold, graduates should be able to plan and carry out an advanced project competently, in one of the three fields or a neighbouring area.", rewrite: light, force: should, status: drafted }
  forBeneficiary: { text: "To reach the minimum standard for an integrated master's degree, you should be able to show that you can plan and carry out an advanced project in mathematics, statistics, operational research or a related area.", rewrite: full, force: should, status: drafted }
  author-agent-written: "Describe this as a threshold standard the integrated master's award requires, met overall rather than item by item (4.2); its force is should, the issuer's word in the lead-in. State that it holds for the integrated master's degree at fheq:7 and fqheis:11. Cite it as (QAA, 2023, Mathematics, Statistics and Operational Research Subject Benchmark Statement, para 4.6, item 9) and do not claim that it holds for the bachelor's degree or that it is a typical rung. Set it beside the honours threshold list 4.5 (no matching item) and qaa/fheq-2024/4.17.b3 and qaa/fheq-2024/4.17.b6."
  author-agent-dialogue: "Raise it when an integrated master's student asks what the final-year minimum is, or a team sets level 7 outcomes. Put it to a student in the second person as the floor for the master's award; to staff, as the level 7 outcome every graduate must reach. Ask how did you plan your project, and what did you change when the plan met the problem? Avoid presenting it as the honours minimum, or reading the issuer's list aloud."
- statement: qaa/mathematics-statistics-and-operational-research-2023/4.7
  forPractitioner: { text: "A taught master's will develop some or all of the threshold standards in 4.5 and 4.6, depending on whether it specialises within MSOR or combines it with another discipline; state which apply.", rewrite: light, force: will, status: drafted }
  forBeneficiary: { text: "On a taught master's course you will develop some or all of these standards, depending on whether your course specialises within the subject or combines it with another field.", rewrite: full, force: will, status: drafted }
  author-agent-written: "Describe this as an expectation that taught master's courses develop some or all of the listed standards; its force is will, an expectation varying by course. State that it holds for taught postgraduate master's degrees at fheq:7 and fqheis:11. Cite it as (QAA, 2023, Mathematics, Statistics and Operational Research Subject Benchmark Statement, para 4.7) and do not claim that every taught master's must meet the whole integrated master's list. Set it beside 4.6.b1 to 4.6.b9, 4.10 and qaa/fheq-2024/4.17.b1 to 4.17.b8.3."
  author-agent-dialogue: "Raise it when a conversion or specialist master's team writes its outcomes, or a student asks what the statement expects of them. Frame it for staff as a selection to justify; for a student, plainly and in the second person. Ask which of the threshold standards does your course develop, and which does it leave aside? Avoid presenting the full integrated master's list as every taught master's minimum."
- statement: qaa/mathematics-statistics-and-operational-research-2023/4.9.b1
  forPractitioner: { text: "Graduates should be able to synthesise information drawn from different branches of MSOR; design tasks that cross module boundaries.", rewrite: light, force: should, status: drafted }
  forBeneficiary: { text: "You should be able to bring together ideas and results from different branches of the subject.", rewrite: full, force: should, status: drafted }
  author-agent-written: "Describe this as a professional standard expected of graduates, listed beside the academic thresholds; its force is should, the lead-in's word; not stated as a threshold. State that it holds for graduates of honours and integrated master's courses, read at fheq:6 (4.10 deepens it at master's level). Cite it as (QAA, 2023, Mathematics, Statistics and Operational Research Subject Benchmark Statement, para 4.9, item 1) and do not claim that it is a professional body's accreditation requirement. Set it beside 3.25 (transfer between contexts) and qaa/fheq-2024/4.15.b7."
  author-agent-dialogue: "Raise it when a student asks what employers or professional settings will expect, or a team maps transferable skills. Put it to a student in the second person and plain words; to staff, as an outcome to build into modules. Ask when did you last use a result from one module to crack a problem in another? Avoid presenting it as a pass or fail threshold, or reading the issuer's list aloud."
- statement: qaa/mathematics-statistics-and-operational-research-2023/4.9.b2
  forPractitioner: { text: "Graduates should apply critical thinking and problem-solving to problems from MSOR and from other disciplines and applications.", rewrite: light, force: should, status: drafted }
  forBeneficiary: { text: "You should be able to think critically and solve problems, both within the subject and in other fields where it is applied.", rewrite: full, force: should, status: drafted }
  author-agent-written: "Describe this as a professional standard expected of graduates, listed beside the academic thresholds; its force is should, the lead-in's word; not stated as a threshold. State that it holds for graduates of honours and integrated master's courses, read at fheq:6 (4.10 deepens it at master's level). Cite it as (QAA, 2023, Mathematics, Statistics and Operational Research Subject Benchmark Statement, para 4.9, item 2) and do not claim that it is a professional body's accreditation requirement. Set it beside 3.26.b5 and qaa/fheq-2024/annex-d/summary/r4/3rd."
  author-agent-dialogue: "Raise it when a student asks what employers or professional settings will expect, or a team maps transferable skills. Put it to a student in the second person and plain words; to staff, as an outcome to build into modules. Ask what problem from outside mathematics have you tackled with mathematical tools? Avoid presenting it as a pass or fail threshold, or reading the issuer's list aloud."
- statement: qaa/mathematics-statistics-and-operational-research-2023/4.9.b3
  forPractitioner: { text: "Graduates should work effectively on their own or in a group to achieve a specific aim.", rewrite: light, force: should, status: drafted }
  forBeneficiary: { text: "You should be able to work well on your own or as part of a group to reach a shared goal.", rewrite: full, force: should, status: drafted }
  author-agent-written: "Describe this as a professional standard expected of graduates, listed beside the academic thresholds; its force is should, the lead-in's word; not stated as a threshold. State that it holds for graduates of honours and integrated master's courses, read at fheq:6 (4.10 deepens it at master's level). Cite it as (QAA, 2023, Mathematics, Statistics and Operational Research Subject Benchmark Statement, para 4.9, item 3) and do not claim that it is a professional body's accreditation requirement. Set it beside 3.26.b9, 1.55 and qaa/fheq-2024/annex-d/transferable/r2/3rd."
  author-agent-dialogue: "Raise it when a student asks what employers or professional settings will expect, or a team maps transferable skills. Put it to a student in the second person and plain words; to staff, as an outcome to build into modules. Ask what did you contribute to your last group task, and what would you do differently? Avoid presenting it as a pass or fail threshold, or reading the issuer's list aloud."
- statement: qaa/mathematics-statistics-and-operational-research-2023/4.9.b4
  forPractitioner: { text: "Graduates should communicate accurately and clearly, spoken and written, in a variety of formats, which may include specialist and non-specialist audiences.", rewrite: light, force: should, status: drafted }
  forBeneficiary: { text: "You should be able to communicate accurately and clearly, in speech and writing and in different formats, to specialists and non-specialists alike.", rewrite: full, force: should, status: drafted }
  author-agent-written: "Describe this as a professional standard expected of graduates, listed beside the academic thresholds; its force is should, the lead-in's word; not stated as a threshold. State that it holds for graduates of honours and integrated master's courses, read at fheq:6 (4.10 deepens it at master's level). Cite it as (QAA, 2023, Mathematics, Statistics and Operational Research Subject Benchmark Statement, para 4.9, item 4) and do not claim that it is a professional body's accreditation requirement. Set it beside 4.5.b6, 3.26.b10 and qaa/fheq-2024/4.15.b8."
  author-agent-dialogue: "Raise it when a student asks what employers or professional settings will expect, or a team maps transferable skills. Put it to a student in the second person and plain words; to staff, as an outcome to build into modules. Ask how would you explain your last result to someone with no mathematics beyond school? Avoid presenting it as a pass or fail threshold, or reading the issuer's list aloud."
- statement: qaa/mathematics-statistics-and-operational-research-2023/4.9.b5
  forPractitioner: { text: "Graduates should have digital capabilities: retrieving information and checking its reliability, general IT, and selecting digital tools to support mathematical reasoning and communication.", rewrite: light, force: should, status: drafted }
  forBeneficiary: { text: "You should be confident with digital tools: finding information and checking whether it can be trusted, everyday IT, and choosing software that helps you think, reason and communicate mathematically.", rewrite: full, force: should, status: drafted }
  author-agent-written: "Describe this as a professional standard expected of graduates, listed beside the academic thresholds; its force is should, the lead-in's word; not stated as a threshold. State that it holds for graduates of honours and integrated master's courses, read at fheq:6 (4.10 deepens it at master's level). Cite it as (QAA, 2023, Mathematics, Statistics and Operational Research Subject Benchmark Statement, para 4.9, item 5) and do not claim that it is a professional body's accreditation requirement. Set it beside 3.26.b8 and qaa/fheq-2024/annex-d/transferable/r1/3rd."
  author-agent-dialogue: "Raise it when a student asks what employers or professional settings will expect, or a team maps transferable skills. Put it to a student in the second person and plain words; to staff, as an outcome to build into modules. Ask how do you check whether a source or a piece of software output can be trusted? Avoid presenting it as a pass or fail threshold, or reading the issuer's list aloud."
- statement: qaa/mathematics-statistics-and-operational-research-2023/4.9.b6
  forPractitioner: { text: "Graduates should be aware of the need to keep their work inside professional and legal frameworks, such as those on data security, EDI and sustainability, as they bear on MSOR.", rewrite: light, force: should, status: drafted }
  forBeneficiary: { text: "You should be aware that your work has to fit professional and legal rules, including data security, equality, diversity and inclusion and sustainability, as they apply to mathematics.", rewrite: full, force: should, status: drafted }
  author-agent-written: "Describe this as a professional standard expected of graduates, listed beside the academic thresholds; its force is should, the lead-in's word; not stated as a threshold. State that it holds for graduates of honours and integrated master's courses, read at fheq:6 (4.10 deepens it at master's level). Cite it as (QAA, 2023, Mathematics, Statistics and Operational Research Subject Benchmark Statement, para 4.9, item 6) and do not claim that it is a professional body's accreditation requirement. Set it beside 3.26.b11, qaa/fheq-2024/annex-d/professional/r2/3rd-1st and the theme statements 1.23 and 1.44 to 1.48."
  author-agent-dialogue: "Raise it when a student asks what employers or professional settings will expect, or a team maps transferable skills. Put it to a student in the second person and plain words; to staff, as an outcome to build into modules. Ask which legal or professional rules applied to the data in your last project? Avoid presenting it as a pass or fail threshold, or reading the issuer's list aloud."
- statement: qaa/mathematics-statistics-and-operational-research-2023/4.9.b7
  forPractitioner: { text: "Graduates should keep to suitable ethical standards and stay alert to the wider consequences of what they do.", rewrite: light, force: should, status: drafted }
  forBeneficiary: { text: "You should keep to sound ethical standards and think about the wider effects of your work.", rewrite: full, force: should, status: drafted }
  author-agent-written: "Describe this as a professional standard expected of graduates, listed beside the academic thresholds; its force is should, the lead-in's word; not stated as a threshold. State that it holds for graduates of honours and integrated master's courses, read at fheq:6 (4.10 deepens it at master's level). Cite it as (QAA, 2023, Mathematics, Statistics and Operational Research Subject Benchmark Statement, para 4.9, item 7) and do not claim that it is a professional body's accreditation requirement. Set it beside 3.26.b11, 3.13 and qaa/fheq-2024/annex-d/professional/r2/3rd-1st."
  author-agent-dialogue: "Raise it when a student asks what employers or professional settings will expect, or a team maps transferable skills. Put it to a student in the second person and plain words; to staff, as an outcome to build into modules. Ask who might be affected by how your model is used, and how? Avoid presenting it as a pass or fail threshold, or reading the issuer's list aloud."
- statement: qaa/mathematics-statistics-and-operational-research-2023/4.9.b8
  forPractitioner: { text: "Graduates should be able to initiate self-learning and monitor and adjust their own work plans in response to reflection and feedback.", rewrite: light, force: should, status: drafted }
  forBeneficiary: { text: "You should be able to start learning on your own and to check and adjust your plans as you reflect and receive feedback.", rewrite: full, force: should, status: drafted }
  author-agent-written: "Describe this as a professional standard expected of graduates, listed beside the academic thresholds; its force is should, the lead-in's word; not stated as a threshold. State that it holds for graduates of honours and integrated master's courses, read at fheq:6 (4.10 deepens it at master's level). Cite it as (QAA, 2023, Mathematics, Statistics and Operational Research Subject Benchmark Statement, para 4.9, item 8) and do not claim that it is a professional body's accreditation requirement. Set it beside 3.26.b1, qaa/fheq-2024/4.15.b5 and qaa/fheq-2024/annex-d/transferable/r5/3rd."
  author-agent-dialogue: "Raise it when a student asks what employers or professional settings will expect, or a team maps transferable skills. Put it to a student in the second person and plain words; to staff, as an outcome to build into modules. Ask what did you change in how you work after your last piece of feedback? Avoid presenting it as a pass or fail threshold, or reading the issuer's list aloud."
- statement: qaa/mathematics-statistics-and-operational-research-2023/4.10
  forPractitioner: { text: "At master's level, graduates will have had deeper or broader experience of some of the 4.9 skills, more independent work and more chances to find creative approaches to non-standard problems; plan where these come.", rewrite: light, force: will, status: drafted }
  forBeneficiary: { text: "At master's level you will have gone deeper or wider in some of these professional skills, worked more independently and had more chances to find new, creative ways into unusual problems.", rewrite: full, force: will, status: drafted }
  author-agent-written: "Describe this as an expectation of deeper professional skill and independence at master's level; its force is will, an expected outcome. State that it holds for integrated and taught master's degrees at fheq:7 and fqheis:11. Cite it as (QAA, 2023, Mathematics, Statistics and Operational Research Subject Benchmark Statement, para 4.10) and do not claim that every 4.9 skill is deepened. Set it beside 4.9.b1 to 4.9.b8, 4.6.b8 and qaa/fheq-2024/4.17.b6."
  author-agent-dialogue: "Raise it when a master's student asks how their skills should differ from a bachelor's graduate's. Put it to a student in the second person: depth in some skills, more independence, more creativity. Ask which professional skills have you taken further this year, and on what non-standard problem? Avoid presenting it as deepening every skill."
```

### S5 Levels and alignment
<!-- label: both; status: drafted; basis: primary -->
```yaml
levels:
  - { id: "fheq:6", role: "cites", locator: "D1, 2.5; 2.12; 4.4", descriptor: "std:doc:qaa-fheq-2024-framework: qaa/fheq-2024/4.15.*", spine: "spine:6" }
  - { id: "fheq:7", role: "cites", locator: "D1, 2.5; 2.12; 2.14", descriptor: "std:doc:qaa-fheq-2024-framework: qaa/fheq-2024/4.17.*", spine: "spine:7" }
  - { id: "fqheis:10", role: "cites", locator: "D1, 2.5; 2.12; 4.4", descriptor: "std:doc:qaa-fqheis-2024-framework: 4.16", spine: "spine:6" }
  - { id: "fqheis:11", role: "cites", locator: "D1, 2.5; 2.12; 2.14", descriptor: "std:doc:qaa-fheq-2024-framework: qaa/fheq-2024/4.17.* (shared)", spine: "spine:7" }
crosswalks:
  - { from: "fheq:6", to: "fqheis:10", relation: "equivalent", basis: "stated (D1, 2.5; 2.12: \"FHEQ Level 6; FQHEIS Level 10\" for the bachelor's degree with honours; 4.4 \"Levels 6/10\")" }
  - { from: "fheq:7", to: "fqheis:11", relation: "equivalent", basis: "stated (D1, 2.5; 2.12; 2.14: \"FHEQ Level 7; FQHEIS Level 11\" for the integrated master's)" }
```

### S6 Themes
<!-- label: both; status: drafted; basis: primary -->
```yaml
- { id: "theme:edi", role: "carries", carriedIn: ["1.21", "1.22", "1.23", "1.24", "1.25", "1.26", "1.27", "1.46", "3.47", "3.48", "4.9"] }
- { id: "theme:accessibility", role: "carries", carriedIn: ["1.27", "1.28", "1.29", "1.30", "1.31", "1.32", "1.33", "1.34", "1.35", "1.36", "1.37", "1.38", "1.39", "1.40", "1.41", "1.42", "1.43", "2.24", "3.30", "3.48"] }
- { id: "theme:esd", role: "carries", carriedIn: ["1.44", "1.45", "1.46", "1.47", "1.48", "4.9"] }
- { id: "theme:enterprise", role: "carries", carriedIn: ["1.49", "1.50", "1.51", "1.52", "1.53", "1.54", "1.55", "1.56", "1.57", "1.58", "1.59", "1.60", "2.30", "3.26"] }
```

### S7 Relations
<!-- label: both; status: drafted; basis: primary -->
```yaml
- { rel: "partOf", target: "collection: QAA Subject Benchmark Statements", note: "one of 54 held by stan" }
- { rel: "supersedes", target: "std:doc:qaa-mathematics-statistics-and-operational-research-2019-benchmarks (not yet ingested)", note: "the fifth edition (2023); the fourth was published in 2019 (D1, section 6)" }
- { rel: "refersTo", target: "std:doc:qaa-fheq-2024-framework, Annex D", note: "the degree classification descriptions for FHEQ level 6 and FQHEIS level 10, cited as QAA 2019 (4.4; section 5)" }
- { rel: "refersTo", target: "std:doc:qaa-fheq-2024-framework", note: "levels 6 and 7 (2.5, 2.12, 2.14, 4.4); the Frameworks for master's outcomes (4.4)" }
- { rel: "refersTo", target: "std:doc:qaa-fqheis-2024-framework", note: "levels 10 and 11 (2.5, 2.12, 2.14, 4.4)" }
- { rel: "themeReference", target: "std:doc:qaa-advancehe-esd-2021-guidance", note: "Education for Sustainable Development Guidance (1.46)" }
- { rel: "themeReference", target: "std:doc:qaa-enterprise-2018-guidance", note: "QAA's enterprise and entrepreneurship guidance (1.49; section 5)" }
- { rel: "refersTo", target: "QAA Characteristics Statement: Higher Education in Apprenticeships (not yet ingested)", note: "2.11" }
- { rel: "refersTo", target: "QAA Contracting to Cheat in Higher Education, third edition (not yet ingested)", note: "3.51" }
- { rel: "refersTo", target: "IMA, RSS and IFoA accreditation requirements (not yet ingested)", note: "1.20, 2.34" }
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
- MSOR is treated as one body of knowledge and skill, wider than its three fields and often combined with others, as in data science (D1, 1.1, 1.2)
- Mathematics draws conclusions by strict deduction from assumptions, and owes its reach to generalisation and abstraction (D1, 1.3, 1.4)
- Statistics handles data under random variation on a base of probability, and explaining results to non-experts is central to it (D1, 1.5, 1.6)
- Operational research spans heavily mathematical optimisation and rigorous non-mathematical problem structuring, in support of decisions (D1, 1.7, 1.8)
- Courses run along a spectrum from theory-based to practice-based, each emphasis equally valued and read from the curriculum, not the title (D1, 1.10, 2.1, 2.2)
- The subject is cumulative, with strict prerequisites; accuracy with symbols and numbers matters; uneven attainment across modules is normal (D1, 1.15 to 1.17, 3.52)
- It is widely taught to non-specialists as service teaching (D1, 1.9)
- Dense notation, board-based argument and diagrams shape both teaching and accessibility (D1, 1.34, 3.29, 3.37)

### SB2 Themes in this subject
<!-- label: both; status: drafted; basis: primary -->
```yaml
- theme: theme:edi
  inThisSubject: "the subject names its gender imbalance, awarding gaps and a curriculum centred on white Western men, and debates decolonising its history (eugenics, enslaved labour, fascist links) without cutting core content; inclusion also reaches data collection and analysis (D1, 1.21 to 1.27)"
  statements: ["qaa/mathematics-statistics-and-operational-research-2023/1.23", "qaa/mathematics-statistics-and-operational-research-2023/1.25", "qaa/mathematics-statistics-and-operational-research-2023/3.47", "qaa/mathematics-statistics-and-operational-research-2023/3.48", "qaa/mathematics-statistics-and-operational-research-2023/4.9.b6"]
- theme: theme:accessibility
  inThisSubject: "mathematical notation, board work, non-linear argument and diagrams defeat mainstream assistive technology, so the subject asks for specialist tools, trained support workers and staff support to embed accessibility (D1, 1.28 to 1.43)"
  statements: ["qaa/mathematics-statistics-and-operational-research-2023/1.28", "qaa/mathematics-statistics-and-operational-research-2023/1.29", "qaa/mathematics-statistics-and-operational-research-2023/1.30", "qaa/mathematics-statistics-and-operational-research-2023/1.33", "qaa/mathematics-statistics-and-operational-research-2023/1.36.b1", "qaa/mathematics-statistics-and-operational-research-2023/1.37", "qaa/mathematics-statistics-and-operational-research-2023/1.38", "qaa/mathematics-statistics-and-operational-research-2023/1.42", "qaa/mathematics-statistics-and-operational-research-2023/3.48"]
- theme: theme:esd
  inThisSubject: "headed Sustainability in the text: models for climate, epidemics, transport and health serve the UN goals; projects, modules and case studies carry it, along with the ethics of computing's footprint (D1, 1.44 to 1.48)"
  statements: ["qaa/mathematics-statistics-and-operational-research-2023/4.9.b6"]
- theme: theme:enterprise
  inThisSubject: "problem-solving is the core enterprise competency; projects, group work, data-heavy modules, client projects and placements build it, and graduates must be able to say how (D1, 1.49 to 1.60)"
  statements: ["qaa/mathematics-statistics-and-operational-research-2023/1.50", "qaa/mathematics-statistics-and-operational-research-2023/1.55", "qaa/mathematics-statistics-and-operational-research-2023/1.60"]
```

### SB3 Content and delivery
<!-- label: both; status: drafted; basis: primary -->
```yaml
areas:
  - { component: "3.8", gloss: "common ground for all courses: calculus, linear algebra, probability and statistics" }
  - { component: "3.9", gloss: "a range of areas, depth set by the course's place on the theory to practice spectrum" }
  - { component: "3.10", gloss: "mathematics: algebra, analysis, geometry, number theory, differential equations, mechanics, mathematical physics" }
  - { component: "3.11", gloss: "statistics: exploratory analysis, inference, likelihood, linear models, stochastic processes, time series, analytics" }
  - { component: "3.12", gloss: "operational research: healthcare, transport, logistics, planning, manufacturing, retail" }
  - { component: "3.13", gloss: "assumptions and their validity" }
  - { component: "3.14", gloss: "generalisation, abstraction and proof" }
  - { component: "3.16", gloss: "numerical approximation" }
  - { component: "3.17", gloss: "programming and specialist software" }
  - { component: "3.18", gloss: "mathematical and statistical modelling" }
  - { component: "3.19", gloss: "modelling techniques, validation and interpretation" }
  - { component: "3.20", gloss: "related content: history of mathematics, mathematics education, careers" }
  - { component: "3.21", gloss: "depth in particular areas" }
practices:
  - { component: "3.28", kind: "teaching", gloss: "a deliberate mix of pedagogies, coherent across the course" }
  - { component: "3.29", kind: "teaching", gloss: "lectures, tutorials, computer laboratories, active and flipped learning" }
  - { component: "3.30", kind: "learning", gloss: "advance materials, practice exercises and open problems" }
  - { component: "3.31", kind: "teaching", gloss: "revisiting topics in a cumulative subject" }
  - { component: "3.32", kind: "learning", gloss: "peer learning, formal and informal" }
  - { component: "3.33", kind: "learning", gloss: "additional support and mathematics support services" }
  - { component: "3.36", kind: "learning", gloss: "study skills and independent practice" }
  - { component: "3.37", kind: "teaching", gloss: "teaching spaces and board space" }
  - { component: "3.38", kind: "teaching", gloss: "technology, including automated feedback" }
  - { component: "3.39", kind: "learning", gloss: "computing, programming and specialist software" }
  - { component: "1.46", kind: "teaching", gloss: "sustainability through projects, modules, case studies and problems" }
  - { component: "1.56", kind: "learning", gloss: "problem-based learning" }
  - { component: "1.57", kind: "assessment", gloss: "client projects and authentic outputs such as posters and client reports" }
  - { component: "3.44", kind: "assessment", gloss: "what assessment establishes against section 4" }
  - { component: "3.46", kind: "assessment", gloss: "formative feedback" }
  - { component: "3.48", kind: "assessment", gloss: "varied methods; automated online marking; accessible and inclusive design" }
  - { component: "3.50", kind: "assessment", gloss: "professional judgement in marking" }
  - { component: "3.51", kind: "assessment", gloss: "controlled conditions and integrity" }
  - { component: "3.52", kind: "assessment", gloss: "the full mark range and whole-course judgement" }
```

### SB4 Benchmark standards
<!-- label: both; status: drafted; basis: primary -->
```yaml
rungs:
  - { rung: "threshold", leadIn: "4.5", award: "bachelor's with honours", items: 7 }
  - { rung: "threshold", leadIn: "4.6", award: "integrated master's", items: 9 }
rungBases: "4.8: performance above threshold may show in depth of understanding, breadth of knowledge, the support needed for an extended task, the complexity of problems solved or modelled, creative solutions to unfamiliar problems, constructing and presenting argument or proof, and facility with calculation; 4.4 points to Annex D for the classification bands. No typical or excellent rung is stated."
outcomeLists:
  - { leadIn: "3.26", gloss: "general skills expected of all graduates", items: 11, award: ["honours", "integrated master's"] }
  - { leadIn: "4.9", gloss: "professional standards", items: 8, award: ["honours", "integrated master's"] }
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
- { body: "Institute of Mathematics and its Applications (IMA)", says: "accredits courses meeting its requirements for graduates to reach Chartered Mathematician status; runs individual professional recognition (D1, 1.20)", requirements: "not yet ingested (Part E)" }
- { body: "Royal Statistical Society (RSS)", says: "accredits courses meeting its requirements for Graduate Statistician status and individual modules in statistical literacy (the RSS Quality Mark); runs individual recognition (D1, 1.20)", requirements: "not yet ingested (Part E)" }
- { body: "Operational Research Society (ORS)", says: "runs individual professional recognition schemes (D1, 1.20)", requirements: "not yet ingested (Part E)" }
- { body: "Institute and Faculty of Actuaries (IFoA)", says: "accredits courses and modules, giving students exemption from some of its examinations (D1, 1.20)", requirements: "not yet ingested (Part E)" }
- { body: "London Mathematical Society (LMS)", says: "runs a Good Practice Scheme for women's careers in the subject, to which many providers work, and publishes Mathematics and Accessibility resources (D1, 1.24, 1.43)", requirements: "not-applicable-by-design: a learned society, not an accrediting body here (Part E)" }
- { body: "professional bodies that accredit MSOR courses (unnamed)", says: "accreditation carries each body's own requirements; quality processes include those tied to accreditation (D1, 2.34, 3.43)", requirements: "not yet ingested (Part E)" }
```

### SB6 Cross-cutting references
<!-- label: both; status: drafted; basis: primary -->
```yaml
themes:
  - { id: "theme:edi", named: "Equality, diversity and inclusion", carriedIn: ["1.21", "1.22", "1.23", "1.24", "1.25", "1.26", "1.27", "1.46", "3.47", "3.48", "4.9"], statements: ["1.23", "1.25", "3.47", "3.48", "4.9.b6"] }
  - { id: "theme:accessibility", named: "Accessibility (front matter: accessibility and the needs of disabled students)", carriedIn: ["1.27", "1.28", "1.29", "1.30", "1.31", "1.32", "1.33", "1.34", "1.35", "1.36", "1.37", "1.38", "1.39", "1.40", "1.41", "1.42", "1.43", "2.24", "3.30", "3.48"], statements: ["1.28", "1.29", "1.30", "1.33", "1.36.b1", "1.37", "1.38", "1.42", "3.48"] }
  - { id: "theme:esd", named: "Sustainability (front matter: education for sustainable development)", carriedIn: ["1.44", "1.45", "1.46", "1.47", "1.48", "4.9"], statements: ["4.9.b6"] }
  - { id: "theme:enterprise", named: "Enterprise and entrepreneurship education (front matter: employability, entrepreneurship and enterprise education)", carriedIn: ["1.49", "1.50", "1.51", "1.52", "1.53", "1.54", "1.55", "1.56", "1.57", "1.58", "1.59", "1.60", "2.30", "3.26"], statements: ["1.50", "1.55", "1.60"] }
frameworks:
  - { framework: "fheq", levels: ["fheq:6", "fheq:7"], citedIn: ["2.5", "2.12", "2.14", "4.4"] }
  - { framework: "scqf", levels: ["fqheis:10", "fqheis:11"], citedIn: ["2.5", "2.12", "2.14", "4.4"] }
bodies:
  - { body: "Institute of Mathematics and its Applications", citedIn: ["1.20"] }
  - { body: "Royal Statistical Society", citedIn: ["1.20"] }
  - { body: "Operational Research Society", citedIn: ["1.20"] }
  - { body: "Institute and Faculty of Actuaries", citedIn: ["1.20"] }
  - { body: "London Mathematical Society", citedIn: ["1.24", "1.43"] }
  - { body: "professional bodies (accrediting, unnamed)", citedIn: ["2.34", "3.43"] }
sharedDocuments:
  - { document: "std:doc:qaa-fheq-2024-framework, Annex D", named: "Annex D: Outcome classification descriptions for FHEQ Level 6 and FQHEIS Level 10 degrees", citedIn: ["4.4"], role: "descriptions of the four honours classifications (1st, 2.1, 2.2, 3rd), used for performance above threshold" }
  - { document: "std:doc:qaa-fheq-2024-framework; std:doc:qaa-fqheis-2024-framework", named: "Frameworks for Higher Education Qualifications", citedIn: ["4.4"], role: "the outcomes for master's level" }
  - { document: "std:doc:qaa-advancehe-esd-2021-guidance", named: "Education for Sustainable Development Guidance produced by QAA and Advance HE", citedIn: ["1.46"], role: "pedagogic approaches for sustainability" }
  - { document: "std:doc:qaa-enterprise-2018-guidance", named: "QAA's guidance (enterprise and entrepreneurship education)", citedIn: ["1.49"], role: "the frame for enterprise education" }
  - { document: "QAA Characteristics Statement: Higher Education in Apprenticeships (not yet ingested: Part E)", named: "Characteristics Statement for Higher Education in Apprenticeships", citedIn: ["2.11"], role: "the characteristics of degree apprenticeships" }
  - { document: "QAA Contracting to Cheat in Higher Education (not yet ingested: Part E)", named: "QAA's guidance Contracting to Cheat in Higher Education", citedIn: ["3.51"], role: "academic integrity under controlled conditions" }
  - { document: "QAA Quality Code, Advice and Guidance (not yet ingested)", named: "Advice and Guidance to support the Quality Code", citedIn: ["front matter"], role: "course design, teaching, external expertise, monitoring" }
  - { document: "QAA Glossary (not ingested)", named: "QAA's Glossary", citedIn: ["front matter"], role: "explains unfamiliar terms" }
  - { document: "UN Sustainable Development Goals (external)", named: "the UN's Sustainable Development Goals", citedIn: ["1.44", "1.45"], role: "the frame of the sustainability theme" }
  - { document: "reports on the value of the mathematical sciences (external)", named: "Measuring the Economic Benefits of Mathematical Science Research in the UK (2012); The Era of Mathematics (2018)", citedIn: ["1.19"], role: "evidence of the subject's economic contribution" }
  - { document: "Council for the Mathematical Sciences report (external)", named: "The Mathematical Sciences People Pipeline (2015)", citedIn: ["1.26"], role: "demographic imbalance data" }
  - { document: "LMS resources (external)", named: "Good Practice Scheme; Mathematics and Accessibility", citedIn: ["1.24", "1.43"], role: "EDI and accessibility practice" }
  - { document: "Athena SWAN (external award scheme)", named: "Athena SWAN awards", citedIn: ["1.24"], role: "evidence of commitment to EDI" }
  - { document: "Maths Careers website (external)", named: "Maths Careers website", citedIn: ["1.18"], role: "careers information" }
```

## Part B Terminology
<!-- The statement has no glossary of its own unless Part E says so; these are terms it defines in its text. -->

### B1 Concepts
<!-- label: both; status: drafted; basis: primary -->
```yaml
- { slug: "msor", definition: "mathematics, statistics and operational research taken together as one field, with the many combinations of its parts (D1, 1.1, 1.2)", beneficiaryDefinition: "the three subjects, and their mixtures, treated as one subject area", scopeNote: "used throughout; wider than the three fields side by side", category: "unknown", practices: ["education"] }
- { slug: "theory-based-course", definition: "a course concerned chiefly with how theory yields general propositions and then methods to apply (D1, 1.10, 2.1)", scopeNote: "one end of a spectrum; most courses mix both styles (2.2)", category: "unknown", practices: ["education"] }
- { slug: "practice-based-course", definition: "a course concerned chiefly with understanding and applying results, methods and techniques in varied settings (D1, 1.10, 2.1)", scopeNote: "the other end of the spectrum", category: "unknown", practices: ["education"] }
- { slug: "enterprise", definition: "generating ideas and putting them to work in practical situations during a project or undertaking (D1, 1.51)", scopeNote: "generic, involving creativity and problem-solving", category: "unknown", practices: ["education"] }
- { slug: "entrepreneurship", definition: "using enterprise behaviours, attributes and competencies to create cultural, social or economic value (D1, 1.52)", scopeNote: "may, but need not, lead to a new venture", category: "unknown", practices: ["education"] }
- { slug: "enterprise-and-entrepreneurship-education", definition: "developing students so they can better generate and evaluate ideas and widen the behaviours needed to carry them out (D1, 1.53)", scopeNote: "one of the cross-cutting themes", category: "unknown", practices: ["education"] }
- { slug: "threshold-level", definition: "the minimum standard of competence the statement sets for an award, met overall rather than item by item (D1, 4.2, 4.4, 4.5, 4.6)", beneficiaryDefinition: "the minimum you need to show to gain the award", scopeNote: "set for honours and for the integrated master's", category: "unknown", practices: ["education"] }
- { slug: "conversion-masters", definition: "a taught master's course letting graduates of other subjects retrain in the field (D1, 1.13, 2.4)", scopeNote: "often in data science and statistics", category: "unknown", practices: ["education"] }
- { slug: "well-curated-course", definition: "a course with clearly communicated learning opportunities, well-spaced assessment and extra support when concepts first appear (D1, 1.33)", scopeNote: "part of the accessibility theme", category: "unknown", practices: ["education"] }
```

### B2a Terms as the issuer defines them
<!-- label: source; status: drafted; basis: primary -->
```yaml
- { concept: "msor", form: "MSOR", lang: "en", partOfSpeech: "noun", termStatus: "preferred", register: "discipline-specific" }
- { concept: "msor", form: "Mathematics, Statistics and Operational Research", lang: "en", partOfSpeech: "noun-phrase", termStatus: "admitted", register: "formal" }
- { concept: "theory-based-course", form: "theory-based courses", lang: "en", partOfSpeech: "noun-phrase", termStatus: "preferred", register: "formal" }
- { concept: "practice-based-course", form: "practice-based courses", lang: "en", partOfSpeech: "noun-phrase", termStatus: "preferred", register: "formal" }
- { concept: "enterprise", form: "Enterprise", lang: "en", partOfSpeech: "noun", termStatus: "preferred", register: "formal" }
- { concept: "entrepreneurship", form: "Entrepreneurship", lang: "en", partOfSpeech: "noun", termStatus: "preferred", register: "formal" }
- { concept: "enterprise-and-entrepreneurship-education", form: "Enterprise and entrepreneurship education", lang: "en", partOfSpeech: "noun-phrase", termStatus: "preferred", register: "formal" }
- { concept: "threshold-level", form: "threshold level", lang: "en", partOfSpeech: "noun-phrase", termStatus: "preferred", register: "formal" }
- { concept: "conversion-masters", form: "conversion master's", lang: "en", partOfSpeech: "noun-phrase", termStatus: "preferred", register: "formal" }
- { concept: "well-curated-course", form: "well curated", lang: "en", partOfSpeech: "adjective-phrase", termStatus: "preferred", register: "formal" }
```

### B2b Associated vocabulary
`not-applicable-by-design`: the statement names no wider vocabulary.

### B3 Framework blocks
`not-applicable-by-design`: no term is defined its own way for one component.

### B4 Relations
<!-- label: both; status: drafted; basis: primary -->
```yaml
- { rel: "contrasts-with", from: "theory-based-course", to: "practice-based-course", note: "ends of one spectrum; most courses mix both (2.2)" }
- { rel: "related", from: "enterprise", to: "entrepreneurship", note: "entrepreneurship applies enterprise to value creation (1.52)" }
- { rel: "broader", from: "enterprise-and-entrepreneurship-education", to: "enterprise", note: "1.53" }
```

## Part C Process
<!-- label: both; status: drafted; basis: primary -->

### C0 Formality
`not-applicable`: the statement sets out what graduates achieve and what courses provide, not a procedure.

## Part D Sources
```yaml
- key: D1
  issuer: The Quality Assurance Agency for Higher Education
  title: "Subject Benchmark Statement Mathematics, Statistics and Operational Research"
  edition: "March 2023 (fifth edition)"
  year: 2023
  url: unknown (the QAA page; the text came by stan's extraction)
  retrieved: "held from stan: wkspc2615-QAAVector mapped/mathematics-statistics-and-operational-research-2023/mathematics-statistics-and-operational-research-2023.raw.txt, commit 366bcb99a01118f2c4c3ebfa2a8337596bddc455; received 2026-10-03"
  licence: QAA copyright
  tier: primary
  readVia: direct
  held: 7c8c162291f2a304a41442f89213ff5156deed1c942988d0a2b95d4e5787a0d6
  heldFiles: ["wkspc2601-library/txt/qaa-2023-mathematics-statistics-operational-research-subject-benchmark-standard.txt", "wkspc2601-library/txt/qaa-2023-mathematics-statistics-operational-research-subject-benchmark-standard.norm.txt", "wkspc2601-library/records/qaa-2023-mathematics-statistics-operational-research-subject-benchmark-standard.chunks.json", "wkspc2601-library/records/qaa-2023-mathematics-statistics-operational-research-subject-benchmark-standard.held.json"]
  citedIn: [S1, S2, S3, S4, S4a, S5, S6, S7, SB1, SB2, SB3, SB4, SB5, SB6]
```

### D2 Research log
```yaml
- { ref: D1, tier: primary, consulted: 2026-10-03, pass: P1, outcome: "read whole, direct, from the normalised text; skeleton by tools/std_prep.py, document by tools/bm_build.py" }
- { ref: "ADAPT subj HESA stores, cah.json and hecos.json (designs/ingest/standards/subj/vocab)", tier: primary, consulted: 2026-10-03, pass: P1, outcome: "codes for statedSubjects and subjects" }
```

### D3 Wanted sources
```yaml
- { w: "W-std-0036", citation: "QAA (2019) Characteristics Statement: Higher Education in Apprenticeships", settles: ["SB6", "S7"], asked: "2026-10-03", state: "wanted" }
- { w: "W-std-0080", citation: "QAA (2022) Contracting to Cheat in Higher Education: How to address Essay Mills and Contract Cheating, third edition", settles: ["SB6", "S7"], asked: "2026-10-03", state: "wanted" }
- { w: "W-std-0081", citation: "QAA (2019) Subject Benchmark Statement: Mathematics, Statistics and Operational Research, fourth edition", settles: ["S7"], asked: "2026-10-03", state: "wanted" }
```

## Part E Gaps and questions
- SB4, rungs: the statement sets threshold standards only, two lists for two awards: 4.5 for the bachelor's degree with honours (7 items) and 4.6 for the integrated master's (9 items). No typical or excellent rung is stated; 4.8 lists the bases on which performance above threshold shows (SB4 `rungBases`), and 4.4 hands classification to Annex D. Differs from Psychology, which states three rungs.
- S4, skeleton correction: std_prep read 4.8's seven bullets as threshold items because the lead-in names 'threshold'; they are the bases for judging performance above threshold ('may be demonstrated through'), not statements. Recorded in `rungBases` and as an S3 component.
- S4, skeleton correction: std_prep gave 4.6's items rung threshold with no award; they are the integrated master's threshold, recorded with award integrated master's and level fheq:7 under their own skeleton ids (4.6.b1 to 4.6.b9), not with the `.masters` suffix, since 4.6 is a separate list with its own spans.
- S4, 4.5 and 4.6 force: the lead-ins read 'should be able to demonstrate'; force is recorded as should, the issuer's word, not threshold, though 4.2 and 4.4 define these lists as the minimum for the award. For Abbott: should a threshold lead-in in 'should' take force threshold?
- S4, 4.2: the standards are to be met 'in an overall sense, not necessarily in respect of each and every criterion listed'; every 4.5 and 4.6 author-agent-written field says so. A new pattern against Psychology.
- SB4, cross-award parallels (inferred, not `gradeOf`, since both lists are threshold): 4.6.b1 to 4.6.b7 follow 4.5.b1 to 4.5.b7 in order, raising 'reasonable' to 'good' and 'well-defined' to 'loosely defined'; 4.5.b4 (reasoning) and 4.6.b4 (developing and evaluating arguments) are the loosest match; 4.6.b8 (independent work) and 4.6.b9 (advanced project) have no honours counterpart.
- S4, 4.9 professional standards: a list headed 'Professional standards' beside the academic standards, with lead-in 'graduates should be expected to'; recorded as an outcome list (rung none, force should), not a rung, and read at fheq:6 for both undergraduate awards, with 4.10 adding the master's deepening. Whether it is a threshold is not stated.
- S4, 3.26 general skills: the lead-in 'are to be expected of all MSOR graduates' is outside the five obliging words; its eleven items are recorded with force describes (forceFrom 3.26). For Abbott: read as should?
- S4, obliging words outside the five, each recorded with force describes: 1.30 'it is imperative that' (read as close to must); 1.38 'need to'; 1.60 'need to be able to'; 2.12 'it is expected that'; 3.18 'are expected to'; 3.26 'are to be expected of'. 1.37 'is required' is recorded as must, by the convention. 1.50 'personal responsibility' (students) and 3.42 'responsibility' (staff) sit in paragraphs already taken as should statements.
- S4, not taken as statements (impersonal obligation or a consequence of practice; for Abbott): 1.21 'it is important that'; 1.26 'There is a need for'; 1.41 'All students will benefit from' explicit instruction; 2.32 'Providers will use external reviewers'; 3.38 technology 'is widespread and expected'; 3.41 staff 'need to routinely update materials'; 1.36.b2 staff 'will require' specialist support and 1.36.b3 'are likely to need'.
- S4, plain-present provider norms and outcomes (template open point 5; not statements): section 3's 'Courses develop graduates who have ...' paragraphs (3.2 first sentences, 3.7, 3.10, 3.12 to 3.14, 3.16, 3.19, 3.21), 3.22 and 3.24's branch skills ('have skills', 'may have skills'), 3.25 and 3.27. They carry much of the subject's knowledge content; only the paragraphs with 'will', 'are able to' or 'expected' (3.5, 3.9, 3.11, 3.17, 3.18) are statements. For Abbott at P3: this subject leans on plain present more than Psychology does.
- S4, list items not taken: 1.13 and 1.20 (descriptive), 1.27 ('good practice here could include', 23 items), 1.34, 1.46 ('might include'), 1.47 (examples), 2.22 and 2.23 ('it is beneficial'), 3.39.b1 to b5 and 3.40 (examples of software and materials), 3.44 and 3.45 (what assessment establishes or could establish).
- S4, 1.1 'should be understood' defines the scope term MSOR; not an obligation on anyone, so not a statement.
- S4, 4.4 mixes a provider 'should' (refer to Annex D) with a student 'will' (master's graduates build on levels 6 and 10); recorded as one provider statement, the master's sentence carried in its paraphrase.
- S4, 4.7: taught master's 'will develop some or all of the standards listed above'; recorded as an expectation for both learner and course, award master's, with no list of its own.
- S4, verbs: 3.26.b3, 3.26.b6, 4.5.b7, 4.6.b1 and 4.6.b7 are noun phrases with no verb of their own; their verbs fields are empty.
- S4, domain: provider duties and 2.12, 4.4 and 4.7 take domain none, as Psychology's requirements do; SB-4 asks for one of the four values on every benchmark standard. For P3.
- S4, themes: 2.24 (reasonable adjustments), 2.30 and 3.26 (employability) carry a theme in SB6 without naming its heading; their S4 records are not theme-tagged, since tags are what the paragraph names.
- S6 and SB6, std_prep correction: the skeleton's theme hits on 1.20 (EDI), 1.43 (sustainability) and 1.48 (enterprise) come from the next heading caught at the end of each span; 1.43 carries accessibility only.
- S5 and SB6: 2.3 names 'Level 4' (foundation years preparing for 'Level 4 study') with no framework named; not recorded as a level (inferred fheq:4).
- S5: integrated master's crosswalk fheq:7 to fqheis:11 stated in 2.5, 2.12 and 2.14; the FHEQ's Table 1 agrees (std:doc:qaa-fheq-2024-framework, S5).
- SB6, sharedDocuments: the statement cites Annex D as QAA 2019; it is now held in the Frameworks 2024 (std:doc:qaa-fheq-2024-framework, Annex D).
- SB5: the IMA, RSS, ORS and IFoA requirements are not yet ingested; the LMS is a learned society, recorded with requirements not-applicable-by-design. The OfS appears only in the front matter (England's regulatory framework) and is not listed as a body.
- S2 and front matter, codes: no HECoS term for data science, analytics or management science; mathematics for engineering mapped to 101028 engineering and industrial mathematics (inferred); applied mathematics 100400 inferred from 'applications of mathematics' (3.8, 3.24). Both inferred codes held back from lookups until P3.
- S2: 1.8 says courses titled 'management science', often with little mathematics, might not fall wholly within the statement; 1.9 says the statement is directly relevant to service courses such as mathematics for engineering; 4.3 makes it a reference point for data science and joint courses.
- Pattern: the master's level appears as its own award list (4.6) and a separate taught master's paragraph (4.7, 4.10), not as a column. Section 4 splits into Academic standards (4.5 to 4.8) and Professional standards (4.9, 4.10), a heading not met in Psychology.
- Pattern: S4 records for 4.9 carry `award` honours and integrated master's but a single `level` fheq:6; 4.10 is recorded at fheq:7.
- S1, licence: copyright notice only; QAA's terms for holding and chunking are to check (template open point 3).
- S9: not researched in P1.
- ST-12: versions here run to the lengths the content needs; no length range is yet set.

---

## Change notes
- 0.1.2, 3 October 2026, 21:02: moved with its held text from UNI to the source library repo (`wkspc2601-library/ingested/standards/`, texts in `txt/`, records in `records/`); paths only (Abbott, 20:56; std N-0119).
- 0.1.1, 3 October 2026, 20:20: obliging words outside the five read as must, "ought to" as should, on statements outside the rungs, each marked on its force line (Abbott, 20:17; D-std-0016).
- 0.1.0, 2026-10-03 18:06: researched by run frame 0.1.1-draft and standards run layer 0.7.0-draft, std, run 0120 (P1); built by tools/bm_build.py.
