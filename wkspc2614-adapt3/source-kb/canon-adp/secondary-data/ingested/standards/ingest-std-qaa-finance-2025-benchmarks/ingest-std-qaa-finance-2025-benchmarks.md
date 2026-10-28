---
id: std:doc:qaa-finance-2025-benchmarks
title: "Subject Benchmark Statement Finance"
profile: standards/subject-benchmark
profileVersion: 0.2.0-draft
issuer: QAA
kind: subject-benchmark
jurisdiction: [UK]
subjectScope: subjects
subjects:
  - { scheme: "hecos", code: "100107", label: "finance", basis: "stated" }
  - { scheme: "cah", code: "CAH17-01-07", label: "finance", basis: "stated" }
  - { scheme: "cah", code: "CAH17-01", label: "business and management", basis: "inferred" }
  - { scheme: "cah", code: "CAH17", label: "business and management", basis: "inferred" }
  - { scheme: "hecos", code: "100832", label: "financial management", basis: "stated" }
  - { scheme: "hecos", code: "100827", label: "banking", basis: "stated" }
  - { scheme: "hecos", code: "100828", label: "investment", basis: "stated" }
edition: "April 2025 (Fourth Edition)"
published: 2025-04
status: current
supersedes: "the previous Finance statement, named only as \"the previous Subject Benchmark Statement\" (front matter); the back matter lists advisory groups for 2019 (minor update), 2014-2015 and 2007"
heldText: { method: sha256-bytes, raw: d25ca6ef8e4ef75bf4cdcac810e6e54f7165ca2896b48a68b9210c16fa7f396f, normalised: ca06534ba68bdeda6c0d925881b28986e4af986e41921ecbf97623822b3a38af }
heldTextStan: { method: sha256-stan, raw: d25ca6ef8e4ef75bf4cdcac810e6e54f7165ca2896b48a68b9210c16fa7f396f, normalised: 8e21105171c0d0c0042e8746e5d6f13ee17ef4c35151d6370757e245568e50c1 }
licence: "QAA copyright; held for study, private to the project, never published"
series: "QAA Subject Benchmark Statements, 2025 revision with cross-cutting themes (this statement: Fourth Edition, published 10 April 2025, D1 back matter)"
awardsCovered: ["bachelor's with honours", "master's", "integrated master's"]
levelsCovered: ["fheq:6", "fheq:7", "fqheis:10", "fqheis:11"]
nations: ["England", "Wales", "Scotland", "Northern Ireland"]
parts:
  S: full
  B: "partial: no glossary in the document (it points to QAA's Glossary); terms it defines in passing"
  C: "not-applicable: the document sets expectations, not a procedure"
pins: { structure: 0.13.0-draft, template: 0.8.0-draft, benchmarkTemplate: 0.6.0-draft, runFrame: 0.1.1-draft, runLayer: 0.7.0-draft, standards: none yet, terminology: none yet }
lifecycle: drafted
researchedBy: run frame 0.1.1-draft; standards run layer 0.7.0-draft; std, run 0106 (tools/bm_build.py)
passes:
  P1: "2026-10-03 17:30"
  P2: "skipped: read direct from the held text; inferred codes and rung links are for P3"
  P3: open
version: 0.1.2
---

<!-- from INGEST wpk-0016-ingest-pd-template-standards.md 0.8.0-draft and wpk-0016-ingest-pd-template-standards-benchmark.md 0.6.0-draft; built by tools/bm_build.py from run-src/ -->
# Subject Benchmark Statement: Finance (QAA, April 2025)

> Run 0106, P1 by std. The issuer's words are held in the source library, `wkspc2601-library/txt/qaa-2025-finance-subject-benchmark-statement-standard.norm.txt`; each S4 record carries its statement in full (`source`) for language analysis, with its span. Paraphrases and versions are ours. Private to the project, never published. In front matter `status` is the issuer's; ours is `lifecycle`. Doubts are in Part E.

## Part 0 Summary

### 0.1 Agent definition
<!-- label: editorial; status: drafted; basis: primary -->
This document is the structured ingestion of QAA's Subject Benchmark Statement for Finance (April 2025). Read it to learn what a Finance graduate is expected to know, understand and do: the threshold list for the bachelor's degree with honours (4.4), the typical and excellent levels written as prose (4.5, 4.6), the subject knowledge and generic skills lists (3.2, 3.3) and the duties it places on courses. Each statement carries the issuer's text in `source`, our paraphrase, a version for staff and one for students, and two instructions for AI agents. It is a sector reference point, not a regulation; levels are pointed to in the FHEQ and FQHEIS documents by id.

### 0.2 Summary
<!-- label: both; status: drafted; basis: primary -->
Finance, as a single, joint or combined bachelor's degree and as specialist, conversion or integrated master's study. Benchmark standards are given for the bachelor's degree only: a threshold list of 15 items (4.4) and typical and excellent levels as two prose paragraphs, cut here into 5 and 7 sentence records; master's courses are referred to the statement's highest levels (1.15). Two outcome lists, subject knowledge and skills (13) and cognitive and generic skills (9), sit in section 3. Cross-cutting themes: equality, diversity and inclusion; accessibility; education for sustainable development; employability, enterprise and entrepreneurship; generative AI. Frameworks: FHEQ and FQHEIS levels 4 to 7 and 8 to 11, with Annex D for evidence of achievement. Bodies: PSRBs in general and eighteen named professional and learned bodies (2.25, 2.26), the FRC, Advance HE and the EHRC.

## Part S Standard

### S1 Identity
<!-- label: source; status: drafted; basis: primary -->
```yaml
issuer: The Quality Assurance Agency for Higher Education
title: "Subject Benchmark Statement Finance"
edition: "April 2025 (Fourth Edition)"
dates:
  published: 2025-04
  other: []
kind: subject-benchmark
jurisdiction: [UK]
authority: "reference: \"not a regulatory requirement\"; sector-owned reference points; part of the quality arrangements in Scotland, Wales and Northern Ireland, not sector-recognised standards in England (D1, front matter)"
licence: "QAA copyright; the document gives no re-use terms in its text (D1, front matter)"
copyrightNotice: { text: "© The Quality Assurance Agency for Higher Education 2025", locator: "D1, index" }
```

### S2 Purpose and scope
<!-- label: source; status: drafted; basis: primary -->
```yaml
governs: "what can be expected of a Finance graduate, at bachelor's and master's level, in knowledge, skills and understanding, with the nature of awards in the subject (D1, front matter; 1.1; 4.1)"
appliesTo:
  awards: ["bachelor's degrees with honours, single, joint or combined", "specialist master's", "conversion master's", "integrated master's", "exit awards CertHE and DipHE (2.12)"]
  levels: ["fheq:4", "fheq:5", "fheq:6", "fheq:7", "fqheis:8", "fqheis:9", "fqheis:10", "fqheis:11"]
  providers: ["UK higher education providers"]
whoMustUse: "none-stated; it is a reference point, not a requirement (D1, front matter)"
howUsed: ["design", "approval", "review", "other: external examining; PSRBs; information for prospective students and employers"]
doesNot: "it does not prescribe teaching, learning or assessment, does not interpret legislation, carries no statutory or regulatory requirement and does not cover single honours accounting or economics (D1, front matter; 1.5)"
beneficiary: the student
statedScope: "\"This Subject Benchmark Statement sets out what is typically expected of successful graduates from bachelor's and master's level programmes in Finance, or Finance combined with another subject, offered by higher education providers in the UK.\" (D1, 1.1)"
statedSubjects:
  - { name: "Finance", locator: "(D1, title; 1.1)", kind: "subject", codes: [{ scheme: "hecos", code: "100107", label: "finance" }, { scheme: "cah", code: "CAH17-01-07", label: "finance" }] }
  - { name: "'finance' or 'financial management'", locator: "(D1, 1.3)", kind: "programme title", codes: [{ scheme: "hecos", code: "100107", label: "finance" }, { scheme: "hecos", code: "100832", label: "financial management" }] }
  - { name: "banking", locator: "(D1, 1.3)", kind: "programme title", codes: [{ scheme: "hecos", code: "100827", label: "banking" }] }
  - { name: "investment", locator: "(D1, 1.3)", kind: "programme title", codes: [{ scheme: "hecos", code: "100828", label: "investment" }] }
  - { name: "financial services, personal finance, sustainable finance, fintech, finance and data analytics, finance and AI", locator: "(D1, 1.3)", kind: "programme title", codes: [] }
  - { name: "Finance in a joint degree with accounting, management, economics, business, a modern language, law, engineering, computing, statistics or mathematics", locator: "(D1, 1.4; 2.5)", kind: "programme title", codes: [{ scheme: "hecos", code: "100107", label: "finance" }] }
  - { name: "specialist master's and conversion master's degrees in Finance", locator: "(D1, 1.15)", kind: "programme title", codes: [{ scheme: "hecos", code: "100107", label: "finance" }] }
  - { name: "integrated master's degrees in Finance", locator: "(D1, 1.17; 2.16)", kind: "programme title", codes: [{ scheme: "hecos", code: "100107", label: "finance" }] }
subjects: see front matter (subjectScope subjects)
```

### S3 Structure
<!-- label: both; status: drafted; basis: primary -->
```yaml
components:
  - { number: "1.1", order: 3, componentType: paragraph, parent: "section 1", heading: "Context and purposes of a Finance degree", gloss: "scope: bachelor's and master's Finance, conceptual and applied" }
  - { number: "1.2", order: 4, componentType: area, parent: "section 1", heading: "Context and purposes of a Finance degree", gloss: "what finance covers, traditional and emerging fields" }
  - { number: "1.3", order: 5, componentType: paragraph, parent: "section 1", heading: "Context and purposes of a Finance degree", gloss: "typical course titles and related titles" }
  - { number: "1.4", order: 6, componentType: paragraph, parent: "section 1", heading: "Context and purposes of a Finance degree", gloss: "Finance in joint degrees; balance of theory and practice" }
  - { number: "1.5", order: 7, componentType: paragraph, parent: "section 1", heading: "Context and purposes of a Finance degree", gloss: "accounting and economics: their own statements" }
  - { number: "1.6", order: 8, componentType: paragraph, parent: "section 1", heading: "Purposes and characteristics of a Finance degree", gloss: "purpose of the degree; two main domains" }
  - { number: "1.7", order: 9, componentType: area, parent: "section 1", heading: "Purposes and characteristics of a Finance degree", gloss: "markets and institutions; investment and corporate finance; newer areas" }
  - { number: "1.8", order: 10, componentType: paragraph, parent: "section 1", heading: "Purposes and characteristics of a Finance degree", gloss: "perspectives on finance; ethical and social awareness" }
  - { number: "1.9", order: 11, componentType: stem, parent: "section 1", heading: "Purposes and characteristics of a Finance degree", gloss: "careers the degree leads to" }
  - { number: "1.10", order: 12, componentType: stem, parent: "section 1", heading: "Purposes and characteristics of a Finance degree", gloss: "sectors graduates work in" }
  - { number: "1.11", order: 13, componentType: paragraph, parent: "section 1", heading: "Purposes and characteristics of a Finance degree", gloss: "work across national borders" }
  - { number: "1.12", order: 14, componentType: paragraph, parent: "section 1", heading: "Purposes and characteristics of a Finance degree", gloss: "why students choose Finance" }
  - { number: "1.13", order: 15, componentType: paragraph, parent: "section 1", heading: "Purposes and characteristics of a Finance degree", gloss: "wider aims, the SDGs, computational and higher skills" }
  - { number: "1.14", order: 16, componentType: paragraph, parent: "section 1", heading: "Purposes and characteristics of a Finance degree", gloss: "apprenticeships and placement-year courses" }
  - { number: "1.15", order: 17, componentType: stem, parent: "section 1", heading: "Purposes and characteristics of a Finance degree", gloss: "two kinds of master's: specialist and conversion" }
  - { number: "1.16", order: 18, componentType: paragraph, parent: "section 1", heading: "Purposes and characteristics of a Finance degree", gloss: "master's: taught study and self-directed research" }
  - { number: "1.17", order: 19, componentType: paragraph, parent: "section 1", heading: "Purposes and characteristics of a Finance degree", gloss: "integrated master's: typical honours then master's level" }
  - { number: "1.18", order: 20, componentType: paragraph, parent: "section 1", heading: "Equality, diversity and inclusion", gloss: "what EDI covers; embedding it in the discipline" }
  - { number: "1.19", order: 21, componentType: paragraph, parent: "section 1", heading: "Equality, diversity and inclusion", gloss: "principles for an inclusive learning community" }
  - { number: "1.20", order: 22, componentType: paragraph, parent: "section 1", heading: "Equality, diversity and inclusion", gloss: "inequality in finance and access to it" }
  - { number: "1.21", order: 23, componentType: paragraph, parent: "section 1", heading: "Equality, diversity and inclusion", gloss: "finance education and the SDGs on inequality" }
  - { number: "1.22", order: 24, componentType: paragraph, parent: "section 1", heading: "Equality, diversity and inclusion", gloss: "widening participation; an environment where all thrive" }
  - { number: "1.23", order: 25, componentType: paragraph, parent: "section 1", heading: "Equality, diversity and inclusion", gloss: "inclusive teaching modes and assessment" }
  - { number: "1.24", order: 26, componentType: stem, parent: "section 1", heading: "Equality, diversity and inclusion", gloss: "ways to embed EDI in learning and resources" }
  - { number: "1.25", order: 27, componentType: stem, parent: "section 1", heading: "Equality, diversity and inclusion", gloss: "EDI topics a Finance degree can explore" }
  - { number: "1.26", order: 28, componentType: paragraph, parent: "section 1", heading: "Equality, diversity and inclusion", gloss: "digital delivery, AI and their effect on EDI" }
  - { number: "1.27", order: 29, componentType: paragraph, parent: "section 1", heading: "Equality, diversity and inclusion", gloss: "monitoring and reviewing EDI in courses" }
  - { number: "1.28", order: 30, componentType: paragraph, parent: "section 1", heading: "Accessibility and the needs of disabled students", gloss: "accessibility: removing barriers, regulatory minimum" }
  - { number: "1.29", order: 31, componentType: stem, parent: "section 1", heading: "Accessibility and the needs of disabled students", gloss: "inclusive design: examples for accessible courses" }
  - { number: "1.30", order: 32, componentType: paragraph, parent: "section 1", heading: "Education for sustainable development", gloss: "sustainable finance and its guiding frameworks" }
  - { number: "1.31", order: 33, componentType: paragraph, parent: "section 1", heading: "Education for sustainable development", gloss: "environmental, social and governance factors and the SDGs" }
  - { number: "1.32", order: 34, componentType: paragraph, parent: "section 1", heading: "Education for sustainable development", gloss: "sustainability practice and its limits in finance" }
  - { number: "1.33", order: 35, componentType: paragraph, parent: "section 1", heading: "Education for sustainable development", gloss: "sustainable solutions across disciplines" }
  - { number: "1.34", order: 36, componentType: paragraph, parent: "section 1", heading: "Education for sustainable development", gloss: "ESD competencies and sustainable decision making" }
  - { number: "1.35", order: 37, componentType: paragraph, parent: "section 1", heading: "Education for sustainable development", gloss: "core competencies for sustainable futures" }
  - { number: "1.36", order: 38, componentType: paragraph, parent: "section 1", heading: "Education for sustainable development", gloss: "ESG disclosure, environmental assets, tools" }
  - { number: "1.37", order: 39, componentType: paragraph, parent: "section 1", heading: "Employability, enterprise and entrepreneurship education", gloss: "what enterprise and entrepreneurship education does" }
  - { number: "1.38", order: 40, componentType: paragraph, parent: "section 1", heading: "Employability, enterprise and entrepreneurship education", gloss: "EED and employability; transferable skills" }
  - { number: "1.39", order: 41, componentType: paragraph, parent: "section 1", heading: "Employability, enterprise and entrepreneurship education", gloss: "software and data skills" }
  - { number: "1.40", order: 42, componentType: paragraph, parent: "section 1", heading: "Employability, enterprise and entrepreneurship education", gloss: "placements, simulations and industry engagement" }
  - { number: "1.41", order: 43, componentType: paragraph, parent: "section 1", heading: "Employability, enterprise and entrepreneurship education", gloss: "entrepreneurship beyond employment; wider context" }
  - { number: "1.42", order: 44, componentType: paragraph, parent: "section 1", heading: "Employability, enterprise and entrepreneurship education", gloss: "experiential learning and awareness of industry change" }
  - { number: "1.43", order: 45, componentType: paragraph, parent: "section 1", heading: "Generative artificial intelligence (GenAI) and AI applications in finance", gloss: "what GenAI is and its uses in finance" }
  - { number: "1.44", order: 46, componentType: paragraph, parent: "section 1", heading: "Generative artificial intelligence (GenAI) and AI applications in finance", gloss: "AI change and its effect on the profession" }
  - { number: "1.45", order: 47, componentType: paragraph, parent: "section 1", heading: "Generative artificial intelligence (GenAI) and AI applications in finance", gloss: "learning to use AI and judge its limits" }
  - { number: "1.46", order: 48, componentType: paragraph, parent: "section 1", heading: "Generative artificial intelligence (GenAI) and AI applications in finance", gloss: "teaching and assessment adapt to AI" }
  - { number: "1.47", order: 49, componentType: paragraph, parent: "section 1", heading: "Generative artificial intelligence (GenAI) and AI applications in finance", gloss: "integrity with AI; following current guidance" }
  - { number: "2.1", order: 51, componentType: area, parent: "section 2", heading: "Introduction", gloss: "markets, instruments and institutions studied" }
  - { number: "2.2", order: 52, componentType: paragraph, parent: "section 2", heading: "Introduction", gloss: "learning objectives, perspectives, design flexibility" }
  - { number: "2.3", order: 53, componentType: area, parent: "section 2", heading: "Introduction", gloss: "accounting knowledge needed; joint degrees" }
  - { number: "2.4", order: 54, componentType: paragraph, parent: "section 2", heading: "Introduction", gloss: "lifelong learning and range of careers" }
  - { number: "2.5", order: 55, componentType: paragraph, parent: "section 2", heading: "Design", gloss: "undergraduate and master's course designs" }
  - { number: "2.6", order: 56, componentType: paragraph, parent: "section 2", heading: "Design", gloss: "bachelor's designed to section 4's outcomes" }
  - { number: "2.7", order: 57, componentType: paragraph, parent: "section 2", heading: "Design", gloss: "variation among master's courses" }
  - { number: "2.8", order: 58, componentType: paragraph, parent: "section 2", heading: "Design", gloss: "integrating knowledge for work and society" }
  - { number: "2.9", order: 59, componentType: paragraph, parent: "section 2", heading: "Progression", gloss: "progression through levels to the rungs" }
  - { number: "2.10", order: 60, componentType: paragraph, parent: "section 2", heading: "Progression", gloss: "readiness for master's study" }
  - { number: "2.11", order: 61, componentType: paragraph, parent: "section 2", heading: "Progression", gloss: "joint degree students and the core skills" }
  - { number: "2.12", order: 62, componentType: paragraph, parent: "section 2", heading: "Progression", gloss: "exit awards: CertHE and DipHE" }
  - { number: "2.13", order: 63, componentType: paragraph, parent: "section 2", heading: "Progression", gloss: "placement or study abroad" }
  - { number: "2.14", order: 64, componentType: paragraph, parent: "section 2", heading: "Progression", gloss: "full master's: credit, dissertation, empirical work" }
  - { number: "2.15", order: 65, componentType: paragraph, parent: "section 2", heading: "Progression", gloss: "postgraduate certificates and diplomas" }
  - { number: "2.16", order: 66, componentType: paragraph, parent: "section 2", heading: "Progression", gloss: "integrated master's: duration and level 7 study" }
  - { number: "2.17", order: 67, componentType: paragraph, parent: "section 2", heading: "Progression", gloss: "research in master's education" }
  - { number: "2.18", order: 68, componentType: paragraph, parent: "section 2", heading: "Flexibility", gloss: "course length across the UK nations" }
  - { number: "2.19", order: 69, componentType: paragraph, parent: "section 2", heading: "Flexibility", gloss: "length of master's courses" }
  - { number: "2.20", order: 70, componentType: paragraph, parent: "section 2", heading: "Flexibility", gloss: "modes of learning and credit routes" }
  - { number: "2.21", order: 71, componentType: paragraph, parent: "section 2", heading: "Flexibility", gloss: "flexibility kept coherent; EDI duties" }
  - { number: "2.22", order: 72, componentType: paragraph, parent: "section 2", heading: "Partnership", gloss: "validation, franchising and apprenticeships" }
  - { number: "2.23", order: 73, componentType: stem, parent: "section 2", heading: "Partnership", gloss: "kinds of partnership" }
  - { number: "2.24", order: 74, componentType: paragraph, parent: "section 2", heading: "Partnership", gloss: "PSRB recognition and professional frameworks" }
  - { number: "2.25", order: 75, componentType: paragraph, parent: "section 2", heading: "Partnership", gloss: "networks and learned societies" }
  - { number: "2.26", order: 76, componentType: paragraph, parent: "section 2", heading: "Partnership", gloss: "advanced standing with professional bodies" }
  - { number: "2.27", order: 77, componentType: paragraph, parent: "section 2", heading: "Monitoring and review", gloss: "monitoring and periodic review" }
  - { number: "2.28", order: 78, componentType: paragraph, parent: "section 2", heading: "Monitoring and review", gloss: "external review, employers and professional bodies" }
  - { number: "2.29", order: 79, componentType: paragraph, parent: "section 2", heading: "Monitoring and review", gloss: "external examiners" }
  - { number: "2.30", order: 80, componentType: paragraph, parent: "section 2", heading: "Monitoring and review", gloss: "advisory boards" }
  - { number: "3.1", order: 82, componentType: paragraph, parent: "section 3", heading: "Content, structure and delivery", gloss: "how to read the outcome lists and examples" }
  - { number: "3.2", order: 83, componentType: stem, parent: "section 3", heading: "Subject-specific knowledge and skills", gloss: "subject knowledge and skills at bachelor's completion" }
  - { number: "3.3", order: 84, componentType: stem, parent: "section 3", heading: "Cognitive abilities and generic skills", gloss: "cognitive and generic skills at bachelor's completion" }
  - { number: "3.4", order: 85, componentType: paragraph, parent: "section 3", heading: "Teaching and learning", gloss: "each course's choice of activities" }
  - { number: "3.5", order: 86, componentType: practice, parent: "section 3", heading: "Teaching and learning", gloss: "what shapes teaching and learning design" }
  - { number: "3.6", order: 87, componentType: practice, parent: "section 3", heading: "Teaching and learning", gloss: "active learning and the methods used" }
  - { number: "3.7", order: 88, componentType: practice, parent: "section 3", heading: "Teaching and learning", gloss: "blended delivery and academic integrity" }
  - { number: "3.8", order: 89, componentType: practice, parent: "section 3", heading: "Teaching and learning", gloss: "support for students from diverse backgrounds" }
  - { number: "3.9", order: 90, componentType: practice, parent: "section 3", heading: "Assessment", gloss: "a balanced mix of assessment" }
  - { number: "3.10", order: 91, componentType: practice, parent: "section 3", heading: "Assessment", gloss: "formative and summative balance" }
  - { number: "3.11", order: 92, componentType: paragraph, parent: "section 3", heading: "Assessment", gloss: "reliability of assessment; programme-level review" }
  - { number: "3.12", order: 93, componentType: practice, parent: "section 3", heading: "Assessment", gloss: "problem-solving and authentic assessment" }
  - { number: "3.13", order: 94, componentType: practice, parent: "section 3", heading: "Assessment", gloss: "range of assessment formats, data-oriented tasks" }
  - { number: "3.14", order: 95, componentType: paragraph, parent: "section 3", heading: "Assessment", gloss: "informed design and regular review" }
  - { number: "4.1", order: 97, componentType: paragraph, parent: "section 4", heading: "Introduction", gloss: "the three levels set for the bachelor's award" }
  - { number: "4.2", order: 98, componentType: paragraph, parent: "section 4", heading: "Introduction", gloss: "most exceed the minimum; Annex D for evidence" }
  - { number: "4.3", order: 99, componentType: paragraph, parent: "section 4", heading: "Introduction", gloss: "not competence standards; Equality Act guidance" }
  - { number: "4.4", order: 100, componentType: stem, parent: "section 4", heading: "Threshold level", gloss: "threshold list for the bachelor's graduate" }
  - { number: "4.5", order: 101, componentType: paragraph, parent: "section 4", heading: "Typical level", gloss: "the typical level, in prose" }
  - { number: "4.6", order: 102, componentType: paragraph, parent: "section 4", heading: "Excellent level", gloss: "the excellent level, in prose" }
  - { number: "1", componentType: section, parent: none, heading: "Context and purposes of a Finance degree", gloss: "section 1" }
  - { number: "2", componentType: section, parent: none, heading: "Distinctive features of the Finance degree", gloss: "section 2" }
  - { number: "3", componentType: section, parent: none, heading: "Content, structure and delivery", gloss: "section 3" }
  - { number: "4", componentType: section, parent: none, heading: "Benchmark standards", gloss: "section 4" }
excluded:
  - { number: "none", heading: "About this Statement; How can I use this document?; Relationship to legislation; Additional sector reference points", kind: "other: front matter, read for S1, S2 and S7" }
  - { number: "none", heading: "Contents", kind: "other: table of contents" }
  - { number: "1, 2, 3, 4", heading: "section headings", kind: "other: headings, recorded as section components" }
  - { number: "5", heading: "List of references and further resources", kind: "other: references, read for SB6 and D3" }
  - { number: "6", heading: "Membership of the Advisory Group", kind: "other: membership lists (2025, 2019, 2014-2015, 2007) and the copyright notice" }
```

### S4 Statements
<!-- label: both; status: drafted; basis: primary. Only standards (D-std-0002 (a)): 86 records. `source` is the issuer's statement exactly as its span holds it (D-std-0014). -->
```yaml
- id: qaa/finance-2025/1.4
  locator: { number: "1.4", headingPath: ["Context and purposes of a Finance degree", "Context and purposes of a Finance degree"] }
  span: { start: 10474, end: 11036 }
  source: "1.4 Finance can be studied as part of a joint degree with related or unrelated disciplines, such as accounting, management, economics, business, a modern language, law, engineering, computing, statistics or mathematics. In these instances, this Subject Benchmark Statement should be used alongside other Statements relevant to the joint disciplines. For combined programmes, it is important to ensure that the scope, depth and balance between theoretical concepts and practical applications are maintained, so that neither aspect is neglected in the curriculum.\n"
  stem: none
  statementType: expectation
  rung: none
  force: should
  level: none
  appliesTo: "joint and combined Finance degrees"
  addressee: provider
  verbs: ["used", "maintained"]
  about: "joint degrees read with the partner subject's statement"
  themes: [none]
  domain: none
  award: ["bachelor's with honours"]
  gradeOf: none
  paraphrase: "Where Finance is one half of a joint degree, the statement should be read together with the statements for the other discipline, keeping the balance of theory and application intact."
  quote: full   # the issuer's statement is in `source` (D-std-0014)
  audience: practitioner
  subjects: inherited
- id: qaa/finance-2025/1.6
  locator: { number: "1.6", headingPath: ["Context and purposes of a Finance degree", "Purposes and characteristics of a Finance degree"] }
  span: { start: 11592, end: 12045 }
  source: "1.6 The purpose of a Finance degree is to educate students to enable them to understand the role of finance in business and organisations, thereby providing a sound foundation for a range of careers. Finance as a degree requires students to study both the fundamentals and cutting-edge developments in finance theory and practice. While encompassing numerous significant areas as described in section 3, it typically focuses on two main subject domains."
  stem: none
  statementType: requirement
  rung: none
  force: must
  level: none
  appliesTo: "students of Finance"
  addressee: learner
  verbs: ["educate", "study", "focuses"]
  about: "fundamentals and new developments in theory and practice"
  themes: [none]
  domain: knowledge
  award: ["bachelor's with honours", "master's"]
  gradeOf: none
  paraphrase: "A Finance degree aims to help students understand what finance does in business and organisations, as a base for many careers; it requires study of both the foundations and the newest work in finance theory and practice."
  quote: full   # the issuer's statement is in `source` (D-std-0014)
  audience: both
  subjects: inherited
- id: qaa/finance-2025/1.7
  locator: { number: "1.7", headingPath: ["Context and purposes of a Finance degree", "Purposes and characteristics of a Finance degree"] }
  span: { start: 12049, end: 13472 }
  source: "1.7 Firstly, Finance as a degree requires students to understand the design and functioning of financial markets, banking markets, stock exchanges, and financial institutions (traditional and newer alternative institutions), along with the roles governments and individuals play within these systems. Secondly, Finance as a degree also requires students to understand the principles of investment and value, corporate finance dynamics, decision- making processes, securities analysis (such as equity, currency, fixed income and derivative instruments), risk management, and international financial management. Moreover, students are also expected to understand contemporary financial areas beyond these traditional domains. These may include, but are not limited to:\n• climate, sustainable and biodiversity finance, environmental, social, and governance (ESG) investing, digital transformation and fintech (for example, cryptocurrency, crowdfunding, peer-to-peer lending)\n• the application of AI and data analytics in finance, exploration of alternative investments (that is, those exploring market inefficiencies through unconventional assets and investment strategies such as hedge funds, private equity, private credit, alternative investments and real assets)\n• global economic uncertainty and the impact on financial and banking markets and central bank policies, and new evolving strategies used in asset management.\n"
  stem: none
  statementType: requirement
  rung: none
  force: must
  level: none
  appliesTo: "students of Finance"
  addressee: learner
  verbs: ["requires", "understand", "expected"]
  about: "the two core domains and contemporary areas"
  themes: [none]
  domain: understanding
  award: ["bachelor's with honours", "master's"]
  gradeOf: none
  paraphrase: "Students must understand two domains: how markets, banks, exchanges and institutions are designed and work, with the roles of governments and individuals; and investment, value, corporate finance, securities analysis, risk and international financial management. They are also expected to understand newer areas such as climate and sustainable finance, fintech, AI and data analytics, alternative investments and global uncertainty."
  quote: full   # the issuer's statement is in `source` (D-std-0014)
  audience: both
  subjects: inherited
- id: qaa/finance-2025/1.8
  locator: { number: "1.8", headingPath: ["Context and purposes of a Finance degree", "Purposes and characteristics of a Finance degree"] }
  span: { start: 13472, end: 14064 }
  source: "1.8 The curriculum of a Finance degree is founded on the typical finance areas mentioned in paragraph 1.7. Notably, Finance studies can be approached from multiple perspectives - behavioural, ethical, economic, sustainable and statistical/mathematical. At a minimum, students will become aware of the ethical and social dimensions of financial activities and systems, in addition to their economic aspects. This holistic approach cultivates a well- rounded mindset, and decision-making skills using both qualitative and quantitative data to solve problems and make sound financial decisions.\n"
  stem: none
  statementType: expectation
  rung: none
  force: will
  level: none
  appliesTo: "students of Finance"
  addressee: learner
  verbs: ["become"]
  about: "awareness of the ethical and social side of finance"
  themes: [none]
  domain: understanding
  award: ["bachelor's with honours", "master's"]
  gradeOf: none
  paraphrase: "Finance can be studied from behavioural, ethical, economic, sustainable and statistical angles; students will at least become conscious of the ethical and social sides of financial activity and systems, as well as the economic ones."
  quote: full   # the issuer's statement is in `source` (D-std-0014)
  audience: both
  subjects: inherited
- id: qaa/finance-2025/1.15.b1
  locator: { number: "1.15.b1", headingPath: ["Context and purposes of a Finance degree", "Purposes and characteristics of a Finance degree"] }
  span: { start: 16935, end: 17727 }
  source: "Specialist master's degrees in Finance involve the in-depth and advanced theoretical and conceptual exploration of one or more core components typically covered in a bachelor's Finance degrees. These programmes may also incorporate supplementary specialised subjects within or related to the discipline, such as banking, fintech, data analytics, or specific research specialisms in the field. This type of master's degree in\n\n6\nFinance would be expected to be evaluated against the highest levels of achievement outlined in the Subject Benchmark Statement, alongside additional content criteria pertinent to the degree's specialised focus. Typically, applicants for these programmes are required to hold at least a second-class single or joint honours bachelor's degree in Finance, or higher."
  stem: "1.15"
  statementType: expectation
  rung: none
  force: must   # D-std-0016: "be expected to" read as must
  level: fheq:7
  appliesTo: "specialist master's degrees in Finance"
  addressee: provider
  verbs: ["involve", "expected", "evaluated", "required"]
  about: "specialist master's judged against the highest levels"
  themes: [none]
  domain: none
  award: ["master's"]
  gradeOf: none
  paraphrase: "Specialist master's courses go deeper into one or more core bachelor's components and may add related specialisms; they would be expected to be judged against the statement's highest levels of achievement plus content criteria for their focus, and usually admit holders of at least a second-class Finance degree."
  quote: full   # the issuer's statement is in `source` (D-std-0014)
  audience: practitioner
  subjects: inherited
- id: qaa/finance-2025/1.18
  locator: { number: "1.18", headingPath: ["Context and purposes of a Finance degree", "Equality, diversity and inclusion"] }
  span: { start: 19143, end: 19916 }
  source: "1.18 Equality, diversity and inclusion (EDI) encompass a wide range of identity characteristics, including, but not limited to, race/ethnicity, gender, sexual orientation, religion and belief, disability, age, and socioeconomic background. It is recognised that there are many forms of difference and that these are, in part, reflected in legal equality duties, but go beyond that to recognise intersectionalities across the student and staff population. EDI should be meaningfully embedded within the culture and practice of the Finance discipline and in all Finance degree programmes. Finance degree programmes reflect the growing importance and emphasis on EDI in the finance industry itself and make reference to relevant industry-adopted EDI codes, where appropriate.\n"
  stem: none
  statementType: expectation
  rung: none
  force: should
  level: none
  appliesTo: "Finance courses and the discipline"
  addressee: provider
  verbs: ["embedded", "reflect"]
  about: "EDI embedded in the culture and practice of Finance"
  themes: [theme:edi]
  domain: none
  award: ["none"]
  gradeOf: none
  paraphrase: "Equality, diversity and inclusion take in many identity characteristics and their intersections; EDI should be built meaningfully into the culture and practice of the discipline and every Finance course, which also reflect industry EDI codes where suitable."
  quote: full   # the issuer's statement is in `source` (D-std-0014)
  audience: practitioner
  subjects: inherited
- id: qaa/finance-2025/1.22
  locator: { number: "1.22", headingPath: ["Context and purposes of a Finance degree", "Equality, diversity and inclusion"] }
  span: { start: 21840, end: 22458 }
  source: "1.22 Students from diverse socioeconomic, cultural, and ethnic backgrounds may aspire to study Finance to support their progression to careers in the financial sector and in other related areas. Whether Finance is taught as a stand-alone subject, or in combination with other disciplines such as accounting, business, mathematics and technology, Finance educators must create an environment where all students can thrive, and feel represented and fully included. This starts with widening participation initiatives that reduce the limiting effect of economic disadvantage on a student's access, experience or outcome.\n"
  stem: none
  statementType: requirement
  rung: none
  force: must
  level: none
  appliesTo: "Finance educators"
  addressee: provider
  verbs: ["create", "thrive"]
  about: "an environment where every student can thrive"
  themes: [theme:edi]
  domain: none
  award: ["none"]
  gradeOf: none
  paraphrase: "Students from varied backgrounds come to Finance; whatever the combination taught, those who teach it must create an environment in which all students can thrive and feel represented and included, starting with widening participation."
  quote: full   # the issuer's statement is in `source` (D-std-0014)
  audience: practitioner
  subjects: inherited
- id: qaa/finance-2025/1.23
  locator: { number: "1.23", headingPath: ["Context and purposes of a Finance degree", "Equality, diversity and inclusion"] }
  span: { start: 22458, end: 23182 }
  source: "1.23 It is important that Finance degrees are taught and the assessment methods deployed in a manner that reflects EDI principles. A range of learning and teaching modes (in-person, digital, blended, hybrid, hyflex, synchronous or asynchronous, block release, full or part- time) can be considered. Assessment should be designed to be as inclusive as possible, reflecting an awareness of EDI and the opportunity for all students to succeed, including, for example, setting alternative assessments in terms of type, duration and mode, where appropriate. For example, this could include a written assessment instead of a presentation, typed answers instead of handwritten, and allowing students additional time for the exams.\n"
  stem: none
  statementType: expectation
  rung: none
  force: should
  level: none
  appliesTo: "Finance assessment design"
  addressee: provider
  verbs: ["designed"]
  about: "inclusive assessment and alternatives"
  themes: [theme:edi]
  domain: none
  award: ["none"]
  gradeOf: none
  paraphrase: "Teaching and assessment in Finance should reflect EDI principles; varied teaching modes can be used, and assessment should be as inclusive as possible, for instance by offering alternative types, timings or modes where suitable."
  quote: full   # the issuer's statement is in `source` (D-std-0014)
  audience: practitioner
  subjects: inherited
- id: qaa/finance-2025/1.24.b1
  locator: { number: "1.24.b1", headingPath: ["Context and purposes of a Finance degree", "Equality, diversity and inclusion"] }
  span: { start: 23381, end: 23470 }
  source: "physical and virtual learning environments must be flexible and reflect student diversity"
  stem: "1.24"
  statementType: requirement
  rung: none
  force: must
  level: none
  appliesTo: "learning environments"
  addressee: provider
  verbs: ["flexible", "reflect"]
  about: "flexible environments that reflect diversity"
  themes: [theme:edi]
  domain: none
  award: ["none"]
  gradeOf: none
  paraphrase: "Physical and online learning environments must be adaptable and mirror the diversity of the students."
  quote: full   # the issuer's statement is in `source` (D-std-0014)
  audience: practitioner
  subjects: inherited
- id: qaa/finance-2025/1.24.b2
  locator: { number: "1.24.b2", headingPath: ["Context and purposes of a Finance degree", "Equality, diversity and inclusion"] }
  span: { start: 23473, end: 23720 }
  source: "different perspectives and inclusivity should be reflected in teaching and assessment materials, including reading materials and case studies, to ensure that a student's background does not become a source of disadvantage in their study of Finance"
  stem: "1.24"
  statementType: expectation
  rung: none
  force: should
  level: none
  appliesTo: "teaching and assessment materials"
  addressee: provider
  verbs: ["reflected", "ensure"]
  about: "diverse perspectives in materials"
  themes: [theme:edi]
  domain: none
  award: ["none"]
  gradeOf: none
  paraphrase: "Teaching and assessment materials, readings and case studies included, should carry varied perspectives so that no student's background puts them at a disadvantage."
  quote: full   # the issuer's statement is in `source` (D-std-0014)
  audience: practitioner
  subjects: inherited
- id: qaa/finance-2025/1.24.b3
  locator: { number: "1.24.b3", headingPath: ["Context and purposes of a Finance degree", "Equality, diversity and inclusion"] }
  span: { start: 23723, end: 23958 }
  source: "consideration of the hidden curriculum is necessary, particularly concerning the language of finance so that this does not act as a barrier to learning, for example see Unpacking your Hidden Curriculum: Guide for educators (qaa.ac.uk)."
  stem: "1.24"
  statementType: requirement
  rung: none
  force: must
  level: none
  appliesTo: "Finance teaching"
  addressee: provider
  verbs: ["necessary"]
  about: "the hidden curriculum and the language of finance"
  themes: [theme:edi]
  domain: none
  award: ["none"]
  gradeOf: none
  paraphrase: "The hidden curriculum needs attention, above all the specialist language of finance, so that it does not get in the way of learning."
  quote: full   # the issuer's statement is in `source` (D-std-0014)
  audience: practitioner
  subjects: inherited
- id: qaa/finance-2025/1.24.b7
  locator: { number: "1.24.b7", headingPath: ["Context and purposes of a Finance degree", "Equality, diversity and inclusion"] }
  span: { start: 24334, end: 24486 }
  source: "where a placement, work experience or industry visit in a Finance degree is offered, there must be consideration to equality of access for all students."
  stem: "1.24"
  statementType: requirement
  rung: none
  force: must
  level: none
  appliesTo: "placements, work experience and visits"
  addressee: provider
  verbs: ["offered"]
  about: "equal access to placements and visits"
  themes: [theme:edi]
  domain: none
  award: ["none"]
  gradeOf: none
  paraphrase: "Where a Finance course offers a placement, work experience or industry visit, equality of access for all students must be considered."
  quote: full   # the issuer's statement is in `source` (D-std-0014)
  audience: practitioner
  subjects: inherited
- id: qaa/finance-2025/1.27
  locator: { number: "1.27", headingPath: ["Context and purposes of a Finance degree", "Equality, diversity and inclusion"] }
  span: { start: 26432, end: 26624 }
  source: "1.27 There should be monitoring and review of EDI within Finance degree programmes to examine how effective the current EDI policies have been implemented and how they can be further enhanced."
  stem: none
  statementType: expectation
  rung: none
  force: should
  level: none
  appliesTo: "Finance courses"
  addressee: provider
  verbs: ["examine", "enhanced"]
  about: "monitoring and review of EDI"
  themes: [theme:edi]
  domain: none
  award: ["none"]
  gradeOf: none
  paraphrase: "Finance courses should monitor and review EDI to see how well current policies work and how to improve them."
  quote: full   # the issuer's statement is in `source` (D-std-0014)
  audience: practitioner
  subjects: inherited
- id: qaa/finance-2025/1.28
  locator: { number: "1.28", headingPath: ["Context and purposes of a Finance degree", "Accessibility and the needs of disabled students"] }
  span: { start: 26674, end: 27720 }
  source: "1.28 Accessibility is concerned with removing barriers so that learners can achieve learning outcomes equitably. Teaching methods in Finance degree programmes reflect the needs of the student body to ensure that each student can succeed and reach their full potential, regardless of their background, disability, health, or other protected characteristics. Accessibility should, as a minimum, meet regulatory requirements and will apply to all stages of the programme, from providing pre-application information through to graduation and beyond. Many providers have their own general accessibility guidance that provides advice and tools to enhance accessibility at the point of design. Some providers also publish accessibility policies which serve as a useful reference point. People with impairments may face barriers to education and employment in higher education institutions. Providing support and adjustments can remove these barriers and therefore support the development of an inclusive environment; please see examples from Advance HE."
  stem: none
  statementType: expectation
  rung: none
  force: should
  level: none
  appliesTo: "Finance courses"
  addressee: provider
  verbs: ["meet", "apply"]
  about: "accessibility at every stage, regulatory minimum"
  themes: [theme:accessibility]
  domain: none
  award: ["none"]
  gradeOf: none
  paraphrase: "Accessibility means removing barriers so that learners can reach outcomes fairly; it should at least meet regulatory requirements and will apply at every stage, from pre-application information to graduation and after."
  quote: full   # the issuer's statement is in `source` (D-std-0014)
  audience: practitioner
  subjects: inherited
- id: qaa/finance-2025/1.29.b4
  locator: { number: "1.29.b4", headingPath: ["Context and purposes of a Finance degree", "Accessibility and the needs of disabled students"] }
  span: { start: 28486, end: 28874 }
  source: "Databases, simulation tools, programming and other software should be accessible to all students, for example, remote access to fixed data terminals, and low stimulation areas. Accessibility is considered in the selection of such products for incorporation into the curriculum. Materials in class consider the hidden curriculum (that is, the implicit expectations for student behaviours)."
  stem: "1.29"
  statementType: expectation
  rung: none
  force: should
  level: none
  appliesTo: "software and data resources"
  addressee: provider
  verbs: ["accessible", "considered"]
  about: "accessible databases, simulations and software"
  themes: [theme:accessibility]
  domain: none
  award: ["none"]
  gradeOf: none
  paraphrase: "Databases, simulation tools and software should be usable by every student, for example through remote access or quiet spaces; accessibility counts when choosing them, and class materials take account of the hidden curriculum."
  quote: full   # the issuer's statement is in `source` (D-std-0014)
  audience: practitioner
  subjects: inherited
- id: qaa/finance-2025/1.29.b5
  locator: { number: "1.29.b5", headingPath: ["Context and purposes of a Finance degree", "Accessibility and the needs of disabled students"] }
  span: { start: 28877, end: 29144 }
  source: "The same opportunities for work placement and experiences, internship opportunities, international learning, and extracurricular and co-curricular activities should be available for all students regardless of background, disability or other protected characteristics."
  stem: "1.29"
  statementType: expectation
  rung: none
  force: should
  level: none
  appliesTo: "placements and wider opportunities"
  addressee: provider
  verbs: ["available"]
  about: "the same opportunities for every student"
  themes: [theme:accessibility]
  domain: none
  award: ["none"]
  gradeOf: none
  paraphrase: "Placements, internships, international learning and extracurricular activities should be open to every student whatever their background, disability or other protected characteristic."
  quote: full   # the issuer's statement is in `source` (D-std-0014)
  audience: practitioner
  subjects: inherited
- id: qaa/finance-2025/1.29.b7
  locator: { number: "1.29.b7", headingPath: ["Context and purposes of a Finance degree", "Accessibility and the needs of disabled students"] }
  span: { start: 29372, end: 29591 }
  source: "Consideration should be taken of barriers to student attendance and achievement, such as caring responsibilities and digital poverty, and steps taken where possible to lessen the impact of these impediments to learning."
  stem: "1.29"
  statementType: expectation
  rung: none
  force: should
  level: none
  appliesTo: "Finance courses"
  addressee: provider
  verbs: ["taken", "lessen"]
  about: "barriers to attendance and achievement"
  themes: [theme:accessibility]
  domain: none
  award: ["none"]
  gradeOf: none
  paraphrase: "Courses should take account of what keeps students from attending or achieving, such as caring duties and digital poverty, and act where they can to reduce it."
  quote: full   # the issuer's statement is in `source` (D-std-0014)
  audience: practitioner
  subjects: inherited
- id: qaa/finance-2025/1.29.b8
  locator: { number: "1.29.b8", headingPath: ["Context and purposes of a Finance degree", "Accessibility and the needs of disabled students"] }
  span: { start: 29594, end: 29799 }
  source: "Assessment methods in Finance should consider accessibility issues in achieving the learning outcomes for the module. Often, learning outcomes can be demonstrated by other means in alternative assessments."
  stem: "1.29"
  statementType: expectation
  rung: none
  force: should
  level: none
  appliesTo: "assessment methods"
  addressee: provider
  verbs: ["consider", "demonstrated"]
  about: "accessible assessment of outcomes"
  themes: [theme:accessibility]
  domain: none
  award: ["none"]
  gradeOf: none
  paraphrase: "Assessment in Finance should take accessibility into account; outcomes can often be shown another way through alternative assessment."
  quote: full   # the issuer's statement is in `source` (D-std-0014)
  audience: practitioner
  subjects: inherited
- id: qaa/finance-2025/1.29.b9
  locator: { number: "1.29.b9", headingPath: ["Context and purposes of a Finance degree", "Accessibility and the needs of disabled students"] }
  span: { start: 29802, end: 29930 }
  source: "Consideration should be made of a universal design for learning principles and embedded assessment choice in Finance programmes."
  stem: "1.29"
  statementType: expectation
  rung: none
  force: should
  level: none
  appliesTo: "Finance programmes"
  addressee: provider
  verbs: ["made"]
  about: "universal design and assessment choice"
  themes: [theme:accessibility]
  domain: none
  award: ["none"]
  gradeOf: none
  paraphrase: "Courses should consider universal design for learning and build choice of assessment into Finance programmes."
  quote: full   # the issuer's statement is in `source` (D-std-0014)
  audience: practitioner
  subjects: inherited
- id: qaa/finance-2025/1.29.b10
  locator: { number: "1.29.b10", headingPath: ["Context and purposes of a Finance degree", "Accessibility and the needs of disabled students"] }
  span: { start: 29933, end: 30162 }
  source: "Proactive approaches should be taken in the design of learning and teaching, and assessment, in order to build in inclusivity and avoid creating barriers for students with specific learning difficulties or who are neurodivergent."
  stem: "1.29"
  statementType: expectation
  rung: none
  force: should
  level: none
  appliesTo: "learning, teaching and assessment design"
  addressee: provider
  verbs: ["taken", "build", "avoid"]
  about: "proactive inclusive design for neurodivergent students"
  themes: [theme:accessibility]
  domain: none
  award: ["none"]
  gradeOf: none
  paraphrase: "Learning, teaching and assessment should be designed ahead of time to include everyone and to avoid barriers for neurodivergent students and those with specific learning difficulties."
  quote: full   # the issuer's statement is in `source` (D-std-0014)
  audience: practitioner
  subjects: inherited
- id: qaa/finance-2025/1.33
  locator: { number: "1.33", headingPath: ["Context and purposes of a Finance degree", "Education for sustainable development"] }
  span: { start: 32332, end: 33370 }
  source: "1.33 Finance degrees aim to enhance the understanding, knowledge, and abilities of bachelor's and master's students, equipping them to critically address and devise effective, sustainable solutions that promote the stability and sustainability of the financial system. These solutions should be viewed as part of wider attempts across disciplines to address risks and challenges posed by climate change, nature and biodiversity loss, environmental pollution, social inequalities, and economic/political uncertainties. These problems are characterised by pervasive uncertainties which require students to foster critical and creative skills that work across discipline boundaries. For example, innovative financing and policy changes are required to provide the significant amount of funding required to conserve nature and to reform policies that will result from biodiversity loss. Finance graduates understand how financial decisions may intentionally or unintentionally influence real-world behaviour in the finance sector and beyond.\n"
  stem: none
  statementType: expectation
  rung: none
  force: should
  level: none
  appliesTo: "students of Finance"
  addressee: learner
  verbs: ["viewed", "foster", "understand"]
  about: "sustainable solutions as part of wider efforts"
  themes: [theme:esd]
  domain: understanding
  award: ["bachelor's with honours", "master's"]
  gradeOf: none
  paraphrase: "Finance degrees aim to equip students to devise sustainable solutions for a stable financial system; these should be seen as one part of efforts across disciplines on climate, nature, pollution, inequality and uncertainty, which call for critical and creative skills that cross subject boundaries."
  quote: full   # the issuer's statement is in `source` (D-std-0014)
  audience: both
  subjects: inherited
- id: qaa/finance-2025/1.34
  locator: { number: "1.34", headingPath: ["Context and purposes of a Finance degree", "Education for sustainable development"] }
  span: { start: 33370, end: 34376 }
  source: "1.34 The core skills developed by all Finance degrees align with the learning outcomes identified by the Education for Sustainable Development Guidance developed by Advance HE and QAA. These learning outcomes go beyond environmental issues alone, focusing instead on interconnections and interdependencies between economic, social and environmental factors, supporting the knowledge, skills and competencies that students and staff develop to contribute to a more sustainable future. These core skills include self- awareness, systems, anticipatory and strategic thinking, critical thinking and integrated problem-solving competency. Finance has a direct impact on the design, implementation and evaluation of policies that aim to create sustainable growth and development. Bachelor's and master's degrees in Finance should develop capacities and competencies that prioritise sustainable decision making and disclosure, which can help drive the sustainability agenda for business, the economy and society.\n"
  stem: none
  statementType: expectation
  rung: none
  force: should
  level: none
  appliesTo: "bachelor's and master's Finance degrees"
  addressee: provider
  verbs: ["align", "develop", "prioritise"]
  about: "competencies for sustainable decisions and disclosure"
  themes: [theme:esd]
  domain: none
  award: ["bachelor's with honours", "master's"]
  gradeOf: none
  paraphrase: "The core skills of Finance degrees match the ESD guidance's outcomes, among them systems, anticipatory, strategic and critical thinking and integrated problem-solving; Finance degrees should develop capacities that put sustainable decisions and disclosure first."
  quote: full   # the issuer's statement is in `source` (D-std-0014)
  audience: practitioner
  subjects: inherited
- id: qaa/finance-2025/1.41
  locator: { number: "1.41", headingPath: ["Context and purposes of a Finance degree", "Employability, enterprise and entrepreneurship education"] }
  span: { start: 38312, end: 38871 }
  source: "1.41 Beyond employment, entrepreneurship education provides competencies to help students lead a rewarding, self-determined professional life, well placed to add social, cultural and economic value at individual, organisational and societal levels through their careers by engaging and leading debates and offering ideas towards creative solutions. Finance graduates should have an appreciation of the wider context of the application of their skills and knowledge, including areas such as sustainability, climate finance and nature and biodiversity finance.\n"
  stem: none
  statementType: expectation
  rung: none
  force: should
  level: none
  appliesTo: "graduates of the subject"
  addressee: learner
  verbs: ["provides", "appreciation"]
  about: "the wider context of finance skills"
  themes: [theme:enterprise]
  domain: understanding
  award: ["bachelor's with honours", "master's"]
  gradeOf: none
  paraphrase: "Entrepreneurship education helps students build a rewarding, self-directed working life that adds social, cultural and economic value; Finance graduates should appreciate the wider setting in which they apply their skills, including sustainability, climate finance and nature and biodiversity finance."
  quote: full   # the issuer's statement is in `source` (D-std-0014)
  audience: both
  subjects: inherited
- id: qaa/finance-2025/2.2
  locator: { number: "2.2", headingPath: ["Distinctive features of the Finance degree", "Introduction"] }
  span: { start: 43930, end: 45132 }
  source: "2.2 Finance degree programmes are designed to include learning objectives that are aligned with the knowledge, understanding and skills detailed in section 4 and to reflect appropriate principles of learning, teaching and assessment. They should be designed to provide students with the opportunity to develop critical thinking and apply skills, knowledge and judgement in dealing with finance questions and problems. Finance degree programmes can be pursued from a variety of perspectives, including, but not restricted to, the behavioural, economic, sustainable or quantitative perspectives. The learning objectives are structured to ensure that they integrate the conceptual and applied aspects of the curriculum and the relationship between them and between different areas of knowledge and understanding. Design flexibility is required to facilitate recent developments such as AI and fintech, blockchains and digital assets. Students should be able to evaluate the potential ethical, sustainability and regulatory dimensions of financial activities and systems, and not merely the different functions of financial institutions and firms, or the pricing and risk management of financial products.\n"
  stem: none
  statementType: expectation
  rung: none
  force: should
  level: none
  appliesTo: "Finance courses and their students"
  addressee: both
  verbs: ["designed", "develop", "evaluate"]
  about: "critical thinking and the ethical and regulatory side of finance"
  themes: [none]
  domain: subject-skill
  award: ["bachelor's with honours", "master's"]
  gradeOf: none
  paraphrase: "Finance courses align learning objectives with section 4 and should be designed so that students can build critical thinking and apply judgement to finance problems; design flexibility is needed for AI, fintech and digital assets, and students should be able to judge the ethical, sustainability and regulatory sides of financial activity, not only how institutions work or how products are priced."
  quote: full   # the issuer's statement is in `source` (D-std-0014)
  audience: both
  subjects: inherited
- id: qaa/finance-2025/2.3
  locator: { number: "2.3", headingPath: ["Distinctive features of the Finance degree", "Introduction"] }
  span: { start: 45132, end: 45931 }
  source: "2.3 Although Finance is often studied in conjunction with accounting, an in-depth knowledge of accounting is not required. The extent to which accounting is covered will be highly dependent on the structure of the degree programme. However, a reasonable knowledge of the principles of accounting, regulatory environment for financial reporting, contents of financial statements and the use of accounting information for decision-making is required. Other topics in accounting may include, but are not limited to, accountability, responsibility and trust, audit and assurance, and accounting systems. Joint discipline degree programmes that include Finance are designed to ensure that they include the majority of the knowledge, understanding and skills detailed in this Subject Benchmark Statement.\n"
  stem: none
  statementType: requirement
  rung: none
  force: must
  level: none
  appliesTo: "students of Finance"
  addressee: learner
  verbs: ["required"]
  about: "a reasonable knowledge of accounting"
  themes: [none]
  domain: knowledge
  award: ["bachelor's with honours", "master's"]
  gradeOf: none
  paraphrase: "Deep accounting knowledge is not required, but a reasonable knowledge of accounting principles, the regulation of financial reporting, what financial statements contain and how accounting information informs decisions is required; joint degrees with Finance include most of the statement's knowledge and skills."
  quote: full   # the issuer's statement is in `source` (D-std-0014)
  audience: both
  subjects: inherited
- id: qaa/finance-2025/2.4
  locator: { number: "2.4", headingPath: ["Distinctive features of the Finance degree", "Introduction"] }
  span: { start: 45931, end: 46233 }
  source: "2.4 Finance degree programmes should prepare students for lifelong and self-directed learning. They should be designed to enable students to thrive in a range of careers in finance, including public, private and the third sector, entrepreneurial and enterprise activities, or further academic pursuits."
  stem: none
  statementType: expectation
  rung: none
  force: should
  level: none
  appliesTo: "Finance courses"
  addressee: provider
  verbs: ["prepare", "designed", "thrive"]
  about: "lifelong learning and a range of careers"
  themes: [none]
  domain: none
  award: ["bachelor's with honours", "master's"]
  gradeOf: none
  paraphrase: "Finance courses should ready students for self-directed learning throughout life and be designed so that they can flourish in many finance careers across sectors, in enterprise or in further study."
  quote: full   # the issuer's statement is in `source` (D-std-0014)
  audience: practitioner
  subjects: inherited
- id: qaa/finance-2025/2.11
  locator: { number: "2.11", headingPath: ["Distinctive features of the Finance degree", "Progression"] }
  span: { start: 48484, end: 48916 }
  source: "2.11 Undergraduates studying Finance programmes as part of a combined or joint bachelor's degree with other subjects will achieve core elements of the specific and generic skills outlined in this Statement and will add others according to the areas covered in the other subject(s) of their degree. Additionally, they may explore the overlap between different disciplines, creating further opportunities for interdisciplinary study.\n"
  stem: none
  statementType: expectation
  rung: none
  force: will
  level: fheq:6
  appliesTo: "joint and combined degree undergraduates"
  addressee: learner
  verbs: ["achieve", "add", "explore"]
  about: "core skills in a joint degree"
  themes: [none]
  domain: subject-skill
  award: ["bachelor's with honours"]
  gradeOf: none
  paraphrase: "Undergraduates taking Finance within a joint or combined degree will achieve the core of the specific and generic skills in the statement, add others from their other subject and may explore where the disciplines overlap."
  quote: full   # the issuer's statement is in `source` (D-std-0014)
  audience: both
  subjects: inherited
- id: qaa/finance-2025/2.14
  locator: { number: "2.14", headingPath: ["Distinctive features of the Finance degree", "Progression"] }
  span: { start: 49501, end: 50236 }
  source: "2.14 Full master's degree programmes (FHEQ Level 7; FQHEIS Level 11) typically comprise a workload equivalent to one year of full-time study, usually of 180 credits (see the Frameworks for Higher Education Qualifications of UK Degree-Awarding Bodies , and the Characteristics Statement: Master's Degree). Following the taught programmes, students normally work on a self-directed project or dissertation which ideally should include empirical work. There is an increasing trend to provide applied projects where students work on a live brief or combine their dissertations with an internship. Some institutions hold three semesters, and instead of a master's dissertation they offer additional taught course units/modules or projects.\n"
  stem: none
  statementType: expectation
  rung: none
  force: should
  level: fheq:7
  appliesTo: "full master's degrees"
  addressee: both
  verbs: ["comprise", "work", "include"]
  about: "the master's project or dissertation and empirical work"
  themes: [none]
  domain: subject-skill
  award: ["master's"]
  gradeOf: none
  paraphrase: "A full master's usually carries 180 credits over one full-time year; after the taught part, students normally complete a self-directed project or dissertation that ideally should include empirical work, though applied projects or extra taught units may take its place."
  quote: full   # the issuer's statement is in `source` (D-std-0014)
  audience: both
  subjects: inherited
- id: qaa/finance-2025/2.17
  locator: { number: "2.17", headingPath: ["Distinctive features of the Finance degree", "Progression"] }
  span: { start: 50869, end: 51049 }
  source: "2.17 Students at master's level should be educated having in mind that the opportunity to conduct research is an important aspect, as some will explore further study opportunities."
  stem: none
  statementType: expectation
  rung: none
  force: should
  level: fheq:7
  appliesTo: "master's teaching"
  addressee: provider
  verbs: ["educated"]
  about: "research as part of master's education"
  themes: [none]
  domain: none
  award: ["master's"]
  gradeOf: none
  paraphrase: "Master's students should be taught with research in mind as an important part of their study, since some will go on to further study."
  quote: full   # the issuer's statement is in `source` (D-std-0014)
  audience: practitioner
  subjects: inherited
- id: qaa/finance-2025/2.20
  locator: { number: "2.20", headingPath: ["Distinctive features of the Finance degree", "Flexibility"] }
  span: { start: 51906, end: 52808 }
  source: "2.20 Higher education providers structure the programmes they offer to support students' learning and attainment and be inclusive to all students. Finance degrees should be offered in a variety of learning modes and with assessment to suit students' learning and other needs. Depending on the educational mission of the provider, this may include opportunities to engage in learning on campus in person, online, and/or through hybrid learning, arranged in terms, by semester, year-long, block, or other formats. These may be offered in full and/or part-time modes of study, in person, digital, blended, hybrid, hyflex, block release, and synchronous/asynchronous, and credit may be accumulated through the completion of micro-credentials, short-accredited learning, recognition of prior learning or accreditation of prior experiential learning with the possibility of switching between modes of study.\n"
  stem: none
  statementType: expectation
  rung: none
  force: should
  level: none
  appliesTo: "Finance degrees"
  addressee: provider
  verbs: ["offered", "suit"]
  about: "a variety of learning modes"
  themes: [none]
  domain: none
  award: ["none"]
  gradeOf: none
  paraphrase: "Courses support learning and are inclusive; Finance degrees should be offered in several modes with assessment that suits students' needs, which may include on-campus, online, hybrid, block or part-time study and credit from micro-credentials or prior learning."
  quote: full   # the issuer's statement is in `source` (D-std-0014)
  audience: practitioner
  subjects: inherited
- id: qaa/finance-2025/2.21
  locator: { number: "2.21", headingPath: ["Distinctive features of the Finance degree", "Flexibility"] }
  span: { start: 52808, end: 53100 }
  source: "2.21 When structuring flexibility into Finance degrees it is essential to ensure that programmes are coherent and meet the benchmarks in this Statement. Flexibility in Finance degrees may be required to meet EDI obligations and partnership relationships may also offer additional flexibility."
  stem: none
  statementType: requirement
  rung: none
  force: must
  level: none
  appliesTo: "flexible Finance degrees"
  addressee: provider
  verbs: ["ensure", "meet", "required"]
  about: "flexibility kept coherent and on standard"
  themes: [none]
  domain: none
  award: ["none"]
  gradeOf: none
  paraphrase: "When flexibility is built into Finance degrees, it is essential that programmes stay coherent and meet the statement's standards; flexibility may be needed to meet EDI obligations, and partnerships can add more."
  quote: full   # the issuer's statement is in `source` (D-std-0014)
  audience: practitioner
  subjects: inherited
- id: qaa/finance-2025/3.2.b1
  locator: { number: "3.2.b1", headingPath: ["Content, structure and delivery", "Subject-specific knowledge and skills"] }
  span: { start: 61378, end: 61769 }
  source: "An appreciation of the contexts in which finance operates, including knowledge of the institutional framework necessary for understanding the role, operation and function of markets and financial institutions (for example, the economic, ethical, legal, political, regulatory, social and tax environment, both national and international; the firm; the capital markets; and the public sector)."
  stem: "3.2"
  statementType: outcome
  rung: none
  force: must   # D-std-0016: "necessary" read as must
  level: fheq:6
  appliesTo: "bachelor's graduates of the subject"
  addressee: learner
  verbs: ["appreciation", "knowledge"]
  about: "the contexts finance operates in"
  themes: [none]
  domain: knowledge
  award: ["bachelor's with honours"]
  gradeOf: none
  paraphrase: "A grasp of the settings finance works in, with knowledge of the institutional framework needed to understand how markets and institutions function, such as economic, ethical, legal, political, regulatory, social and tax settings."
  quote: full   # the issuer's statement is in `source` (D-std-0014)
  audience: both
  subjects: inherited
- id: qaa/finance-2025/3.2.b2
  locator: { number: "3.2.b2", headingPath: ["Content, structure and delivery", "Subject-specific knowledge and skills"] }
  span: { start: 61772, end: 62629 }
  source: "Knowledge of the major theoretical tools and theories of finance, and their relevance and application to theoretical and practical problems (for example, the concept of arbitrage and examples of its use; financial mathematics; informational efficiency; optimal risk sharing; portfolio theory; asset pricing models and the valuation of securities; cost of capital; derivatives and derivative pricing; risk management; information asymmetry; principal-agent relationships; signalling; trading mechanisms, the risks presented by climate change, green finance, climate finance, finance for nature and biodiversity; corporate finance, capital budgeting; behavioural finance; personal finance and literacy, scope and impact of financial regulation, term structure and the movement of interest rates; determination of exchange rates; and financial intermediation)."
  stem: "3.2"
  statementType: outcome
  rung: none
  force: must   # D-std-0016: "expected to" read as must
  level: fheq:6
  appliesTo: "bachelor's graduates of the subject"
  addressee: learner
  verbs: ["knowledge", "relevance", "application"]
  about: "major theories and tools of finance"
  themes: [none]
  domain: knowledge
  award: ["bachelor's with honours"]
  gradeOf: none
  paraphrase: "Knowledge of finance's main theoretical tools and theories and how they bear on theoretical and practical problems, for example arbitrage, portfolio theory, asset pricing, cost of capital, derivatives, behavioural finance and climate finance."
  quote: full   # the issuer's statement is in `source` (D-std-0014)
  audience: both
  subjects: inherited
- id: qaa/finance-2025/3.2.b3
  locator: { number: "3.2.b3", headingPath: ["Content, structure and delivery", "Subject-specific knowledge and skills"] }
  span: { start: 62632, end: 63206 }
  source: "An understanding of the relationship between financial theory and empirical testing, and application of this knowledge to the appraisal of the empirical evidence in one or more major theoretical areas. The appraisal should involve some recognition of the limitations and evolution of empirical tests and theory (for example, the efficient markets hypothesis; asset pricing anomalies; risk management; pricing of derivatives and other securities; portfolio management; interest rates; exchange rates; raising capital and capital structure; agency theory; and sustainability)."
  stem: "3.2"
  statementType: outcome
  rung: none
  force: must   # D-std-0016: "expected to" read as must
  level: fheq:6
  appliesTo: "bachelor's graduates of the subject"
  addressee: learner
  verbs: ["understanding", "appraisal", "recognition"]
  about: "theory and empirical testing"
  themes: [none]
  domain: understanding
  award: ["bachelor's with honours"]
  gradeOf: none
  paraphrase: "An understanding of how finance theory relates to empirical testing, used to appraise the evidence in at least one major area, recognising how tests and theory are limited and change over time."
  quote: full   # the issuer's statement is in `source` (D-std-0014)
  audience: both
  subjects: inherited
- id: qaa/finance-2025/3.2.b4
  locator: { number: "3.2.b4", headingPath: ["Content, structure and delivery", "Subject-specific knowledge and skills"] }
  span: { start: 63209, end: 64172 }
  source: "An ability to interpret financial data, including those arising in the context of the firm or household or national levels from accounting statements and data generated in financial markets. The interpretation should involve analysis using statistical and financial decisions and procedures routinely available in spreadsheets and other statistical/econometric software packages. It may involve the skills necessary to manipulate financial data and conduct statistical and econometric tests (for example, estimation and interpretation of asset pricing models; financial modelling and projections; event studies; elements of panel data analysis, including endogeneity and causality effects as well as time series analysis, such as serial correlation, mean reversion, and time-varying volatility). Interpretation of financial data can also involve critique of the results and understanding the judgements involved, and assumptions and limitations of financial data."
  stem: "3.2"
  statementType: outcome
  rung: none
  force: must   # D-std-0016: "necessary" read as must
  level: fheq:6
  appliesTo: "bachelor's graduates of the subject"
  addressee: learner
  verbs: ["interpret", "manipulate", "conduct"]
  about: "interpreting financial data"
  themes: [none]
  domain: subject-skill
  award: ["bachelor's with honours"]
  gradeOf: none
  paraphrase: "An ability to interpret financial data from firms, households, national sources and markets, analysing it with statistical tools in spreadsheets or econometric software, possibly running statistical and econometric tests, and critiquing results and their assumptions."
  quote: full   # the issuer's statement is in `source` (D-std-0014)
  audience: both
  subjects: inherited
- id: qaa/finance-2025/3.2.b5
  locator: { number: "3.2.b5", headingPath: ["Content, structure and delivery", "Subject-specific knowledge and skills"] }
  span: { start: 64179, end: 64771 }
  source: "An understanding of the financing arrangements and governance mechanisms and structures of business entities and other organisations, and an appreciation of how theory and evidence can be combined to assess the effectiveness and efficiency of such arrangements (for example, decisions related to sources of finance and financial structure; the pricing of corporate securities; the market for corporate control; corporate governance, including aspects related to diversity and equality; environmental, social and governance issues; financial planning; and international dimensions of finance)."
  stem: "3.2"
  statementType: outcome
  rung: none
  force: must   # D-std-0016: "expected to" read as must
  level: fheq:6
  appliesTo: "bachelor's graduates of the subject"
  addressee: learner
  verbs: ["understanding", "appreciation", "assess"]
  about: "financing arrangements and governance"
  themes: [none]
  domain: understanding
  award: ["bachelor's with honours"]
  gradeOf: none
  paraphrase: "An understanding of how firms and other organisations are financed and governed, and how theory and evidence together can judge whether those arrangements are effective and efficient."
  quote: full   # the issuer's statement is in `source` (D-std-0014)
  audience: both
  subjects: inherited
- id: qaa/finance-2025/3.2.b6
  locator: { number: "3.2.b6", headingPath: ["Content, structure and delivery", "Subject-specific knowledge and skills"] }
  span: { start: 64774, end: 65277 }
  source: "An understanding of the factors influencing the financial management and investment behaviour and opportunities of private individuals (for example, bonds, equities, and derivatives; money market instruments; risk aversion; risk/return trade-offs; portfolio management and performance measurement; pensions and long-term savings; the tax treatment of savings and investments; international diversification; foreign exchange risk; objectives of, and constraints on, institutional investors and advisers)."
  stem: "3.2"
  statementType: outcome
  rung: none
  force: must   # D-std-0016: "expected to" read as must
  level: fheq:6
  appliesTo: "bachelor's graduates of the subject"
  addressee: learner
  verbs: ["understanding"]
  about: "personal financial management and investment"
  themes: [none]
  domain: understanding
  award: ["bachelor's with honours"]
  gradeOf: none
  paraphrase: "An understanding of what shapes how individuals manage money and invest, and the opportunities open to them, such as risk attitudes, portfolio choice, pensions, tax on savings and currency risk."
  quote: full   # the issuer's statement is in `source` (D-std-0014)
  audience: both
  subjects: inherited
- id: qaa/finance-2025/3.2.b7
  locator: { number: "3.2.b7", headingPath: ["Content, structure and delivery", "Subject-specific knowledge and skills"] }
  span: { start: 65280, end: 65898 }
  source: "An understanding of financial service activities in the economy, the factors that are changing these activities over time, and an appreciation of how finance theory and evidence can be employed to aid such understanding (for example, ideas of information asymmetry, moral hazard and risk sharing could be employed to analyse the fundamental nature of services, such as insurance, pensions, bank lending and consumer credit, and also explore fundamental problems arising in such financial service provision; the efficient market hypothesis could be used to explore the value added by investment and financial services)."
  stem: "3.2"
  statementType: outcome
  rung: none
  force: must   # D-std-0016: "expected to" read as must
  level: fheq:6
  appliesTo: "bachelor's graduates of the subject"
  addressee: learner
  verbs: ["understanding", "appreciation", "employed"]
  about: "financial services in the economy"
  themes: [none]
  domain: understanding
  award: ["bachelor's with honours"]
  gradeOf: none
  paraphrase: "An understanding of financial service activity in the economy and what changes it, and of how theory and evidence, such as information asymmetry or market efficiency, help explain it."
  quote: full   # the issuer's statement is in `source` (D-std-0014)
  audience: both
  subjects: inherited
- id: qaa/finance-2025/3.2.b8
  locator: { number: "3.2.b8", headingPath: ["Content, structure and delivery", "Subject-specific knowledge and skills"] }
  span: { start: 65901, end: 66289 }
  source: "An ability to understand financial statements, and a reasonable appreciation of the limitations of financial reporting and disclosure practices and procedures (for example, financial statement analysis; the relation between cash flow accounting and accrual accounting; discretionary accounting practices; and financial statement derived measures of financial performance, including risk)."
  stem: "3.2"
  statementType: outcome
  rung: none
  force: must   # D-std-0016: "expected to" read as must
  level: fheq:6
  appliesTo: "bachelor's graduates of the subject"
  addressee: learner
  verbs: ["understand", "appreciation"]
  about: "financial statements and reporting limits"
  themes: [none]
  domain: subject-skill
  award: ["bachelor's with honours"]
  gradeOf: none
  paraphrase: "Able to read financial statements, with a fair awareness of where financial reporting and disclosure fall short, for example accrual versus cash accounting and discretionary practices."
  quote: full   # the issuer's statement is in `source` (D-std-0014)
  audience: both
  subjects: inherited
- id: qaa/finance-2025/3.2.b9
  locator: { number: "3.2.b9", headingPath: ["Content, structure and delivery", "Subject-specific knowledge and skills"] }
  span: { start: 66292, end: 66623 }
  source: "An understanding of the organisation, scope and wider impact of regulatory activity in the finance sector; the rationale for regulation; the requirements and obligations on financial firms and markets, the differentiated nature across finance industries and economies; the implications for professionalism of finance practitioners."
  stem: "3.2"
  statementType: outcome
  rung: none
  force: must   # D-std-0016: "requirements" read as must
  level: fheq:6
  appliesTo: "bachelor's graduates of the subject"
  addressee: learner
  verbs: ["understanding"]
  about: "regulation in the finance sector"
  themes: [none]
  domain: understanding
  award: ["bachelor's with honours"]
  gradeOf: none
  paraphrase: "An understanding of how regulation in finance is organised, why it exists, what it asks of firms and markets, how it differs across industries and economies, and what it means for practitioners' professionalism."
  quote: full   # the issuer's statement is in `source` (D-std-0014)
  audience: both
  subjects: inherited
- id: qaa/finance-2025/3.2.b10
  locator: { number: "3.2.b10", headingPath: ["Content, structure and delivery", "Subject-specific knowledge and skills"] }
  span: { start: 66626, end: 67066 }
  source: "An ability to assess the role of different technologies, including digital, AI, including GenAI, and the latest technology developments, in enabling innovative means of delivering financial services and in the functioning of financial markets and investment (for example, in the domains of payments, credit and lending, fraud detection, crowdfunding, compliance, investment management, insurance, regulation and digital/virtual currencies)."
  stem: "3.2"
  statementType: outcome
  rung: none
  force: must   # D-std-0016: "expected to" read as must
  level: fheq:6
  appliesTo: "bachelor's graduates of the subject"
  addressee: learner
  verbs: ["assess"]
  about: "technology, AI and GenAI in finance"
  themes: [none]
  domain: subject-skill
  award: ["bachelor's with honours"]
  gradeOf: none
  paraphrase: "An ability to judge how technologies, including digital tools, AI and GenAI, make new ways of delivering financial services possible and affect markets and investment, in areas such as payments, lending, fraud detection and compliance."
  quote: full   # the issuer's statement is in `source` (D-std-0014)
  audience: both
  subjects: inherited
- id: qaa/finance-2025/3.2.b11
  locator: { number: "3.2.b11", headingPath: ["Content, structure and delivery", "Subject-specific knowledge and skills"] }
  span: { start: 67069, end: 67375 }
  source: "An ability to understand personal finance concepts, identify how to develop competencies in the domains of financial literacy and capability. Appreciate the social and economic value of widening access to finance using a variety of channels, including those that have emerged outside of mainstream avenues."
  stem: "3.2"
  statementType: outcome
  rung: none
  force: must   # D-std-0016: "expected to" read as must
  level: fheq:6
  appliesTo: "bachelor's graduates of the subject"
  addressee: learner
  verbs: ["understand", "identify", "appreciate"]
  about: "personal finance and financial literacy"
  themes: [none]
  domain: understanding
  award: ["bachelor's with honours"]
  gradeOf: none
  paraphrase: "An ability to understand personal finance and see how financial literacy and capability are built, and to value widening access to finance through mainstream and alternative channels."
  quote: full   # the issuer's statement is in `source` (D-std-0014)
  audience: both
  subjects: inherited
- id: qaa/finance-2025/3.2.b12
  locator: { number: "3.2.b12", headingPath: ["Content, structure and delivery", "Subject-specific knowledge and skills"] }
  span: { start: 67378, end: 67683 }
  source: "An ability to understand the role of the finance sector in addressing the challenges and impact of the risks presented by climate change and other environmental risks; the growth and functions of green/climate finance, finance for nature and biodiversity, and sustainable finance products and initiatives."
  stem: "3.2"
  statementType: outcome
  rung: none
  force: must   # D-std-0016: "expected to" read as must
  level: fheq:6
  appliesTo: "bachelor's graduates of the subject"
  addressee: learner
  verbs: ["understand"]
  about: "finance and climate and environmental risk"
  themes: [none]
  domain: understanding
  award: ["bachelor's with honours"]
  gradeOf: none
  paraphrase: "An ability to understand what the finance sector does about climate change and other environmental risks, and how green and climate finance, nature and biodiversity finance and sustainable products have grown."
  quote: full   # the issuer's statement is in `source` (D-std-0014)
  audience: both
  subjects: inherited
- id: qaa/finance-2025/3.2.b13
  locator: { number: "3.2.b13", headingPath: ["Content, structure and delivery", "Subject-specific knowledge and skills"] }
  span: { start: 67686, end: 68118 }
  source: "Knowledge of appropriate programming, data visualisation, AI, and other computing skills required in the modern finance profession will be part of a degree programme. An ability to use such techniques on actual economic, financial or social data using suitable statistical or econometric software. An appreciation of both quantitative\n\n20\nand qualitative data and ability to select appropriate research methods to analyse such data."
  stem: "3.2"
  statementType: outcome
  rung: none
  force: must   # D-std-0016: "required" read as must
  level: fheq:6
  appliesTo: "bachelor's graduates of the subject"
  addressee: learner
  verbs: ["use", "select", "analyse"]
  about: "programming, data and research methods"
  themes: [none]
  domain: subject-skill
  award: ["bachelor's with honours"]
  gradeOf: none
  paraphrase: "Knowledge of the programming, data visualisation, AI and computing skills the profession needs, the ability to apply them to real data in statistical or econometric software, and a grasp of quantitative and qualitative data with the choice of fitting research methods."
  quote: full   # the issuer's statement is in `source` (D-std-0014)
  audience: both
  subjects: inherited
- id: qaa/finance-2025/3.3.b1
  locator: { number: "3.3.b1", headingPath: ["Content, structure and delivery", "Cognitive abilities and generic skills"] }
  span: { start: 68340, end: 68385 }
  source: "critical evaluation of arguments and evidence"
  stem: "3.3"
  statementType: outcome
  rung: none
  force: must   # D-std-0016: "expected to" read as must
  level: fheq:6
  appliesTo: "bachelor's graduates of the subject"
  addressee: learner
  verbs: ["evaluation"]
  about: "critical evaluation"
  themes: [none]
  domain: generic-skill
  award: ["bachelor's with honours"]
  gradeOf: none
  paraphrase: "Weighing arguments and evidence critically."
  quote: full   # the issuer's statement is in `source` (D-std-0014)
  audience: both
  subjects: inherited
- id: qaa/finance-2025/3.3.b2
  locator: { number: "3.3.b2", headingPath: ["Content, structure and delivery", "Cognitive abilities and generic skills"] }
  span: { start: 68388, end: 68425 }
  source: "independent and self-managed learning"
  stem: "3.3"
  statementType: outcome
  rung: none
  force: must   # D-std-0016: "expected to" read as must
  level: fheq:6
  appliesTo: "bachelor's graduates of the subject"
  addressee: learner
  verbs: ["learning"]
  about: "independent learning"
  themes: [none]
  domain: generic-skill
  award: ["bachelor's with honours"]
  gradeOf: none
  paraphrase: "Learning on one's own initiative and managing one's own study."
  quote: full   # the issuer's statement is in `source` (D-std-0014)
  audience: both
  subjects: inherited
- id: qaa/finance-2025/3.3.b3
  locator: { number: "3.3.b3", headingPath: ["Content, structure and delivery", "Cognitive abilities and generic skills"] }
  span: { start: 68428, end: 68642 }
  source: "analysis, filtering and evaluation of data, and drawing reasoned conclusions concerning structured and, to a more limited extent, unstructured problems from a given set of data and from data acquired by the student"
  stem: "3.3"
  statementType: outcome
  rung: none
  force: must   # D-std-0016: "expected to" read as must
  level: fheq:6
  appliesTo: "bachelor's graduates of the subject"
  addressee: learner
  verbs: ["analysis", "drawing"]
  about: "analysing data and drawing conclusions"
  themes: [none]
  domain: generic-skill
  award: ["bachelor's with honours"]
  gradeOf: none
  paraphrase: "Analysing, filtering and judging data, and drawing reasoned conclusions about structured and, to a lesser degree, unstructured problems from given data or data the student gathers."
  quote: full   # the issuer's statement is in `source` (D-std-0014)
  audience: both
  subjects: inherited
- id: qaa/finance-2025/3.3.b4
  locator: { number: "3.3.b4", headingPath: ["Content, structure and delivery", "Cognitive abilities and generic skills"] }
  span: { start: 68645, end: 68772 }
  source: "location, extraction, management and analysis of data from multiple sources, including acknowledging and referencing of sources"
  stem: "3.3"
  statementType: outcome
  rung: none
  force: must   # D-std-0016: "expected to" read as must
  level: fheq:6
  appliesTo: "bachelor's graduates of the subject"
  addressee: learner
  verbs: ["location", "extraction", "management"]
  about: "finding and managing data from many sources"
  themes: [none]
  domain: generic-skill
  award: ["bachelor's with honours"]
  gradeOf: none
  paraphrase: "Locating, extracting, managing and analysing data from several sources, acknowledging and referencing them."
  quote: full   # the issuer's statement is in `source` (D-std-0014)
  audience: both
  subjects: inherited
- id: qaa/finance-2025/3.3.b5
  locator: { number: "3.3.b5", headingPath: ["Content, structure and delivery", "Cognitive abilities and generic skills"] }
  span: { start: 68775, end: 68945 }
  source: "numeracy, including the processing and analysis of financial and other numerical data and the appreciation of statistical and econometric concepts at an appropriate level"
  stem: "3.3"
  statementType: outcome
  rung: none
  force: must   # D-std-0016: "expected to" read as must
  level: fheq:6
  appliesTo: "bachelor's graduates of the subject"
  addressee: learner
  verbs: ["processing", "analysis", "appreciation"]
  about: "numeracy"
  themes: [none]
  domain: generic-skill
  award: ["bachelor's with honours"]
  gradeOf: none
  paraphrase: "Numeracy, including handling and analysing financial and other numbers and grasping statistical and econometric ideas at a suitable level."
  quote: full   # the issuer's statement is in `source` (D-std-0014)
  audience: both
  subjects: inherited
- id: qaa/finance-2025/3.3.b6
  locator: { number: "3.3.b6", headingPath: ["Content, structure and delivery", "Cognitive abilities and generic skills"] }
  span: { start: 68948, end: 69076 }
  source: "selection and application of relevant research tools to design, guide and interpret financial, social and environmental policies"
  stem: "3.3"
  statementType: outcome
  rung: none
  force: must   # D-std-0016: "expected to" read as must
  level: fheq:6
  appliesTo: "bachelor's graduates of the subject"
  addressee: learner
  verbs: ["selection", "application", "design"]
  about: "research tools for policy"
  themes: [none]
  domain: generic-skill
  award: ["bachelor's with honours"]
  gradeOf: none
  paraphrase: "Choosing and using research tools to design, steer and interpret financial, social and environmental policy."
  quote: full   # the issuer's statement is in `source` (D-std-0014)
  audience: both
  subjects: inherited
- id: qaa/finance-2025/3.3.b7
  locator: { number: "3.3.b7", headingPath: ["Content, structure and delivery", "Cognitive abilities and generic skills"] }
  span: { start: 69079, end: 69168 }
  source: "using technology for the acquisition, analysis and communication of financial information"
  stem: "3.3"
  statementType: outcome
  rung: none
  force: must   # D-std-0016: "expected to" read as must
  level: fheq:6
  appliesTo: "bachelor's graduates of the subject"
  addressee: learner
  verbs: ["using"]
  about: "technology for financial information"
  themes: [none]
  domain: generic-skill
  award: ["bachelor's with honours"]
  gradeOf: none
  paraphrase: "Using technology to gather, analyse and communicate financial information."
  quote: full   # the issuer's statement is in `source` (D-std-0014)
  audience: both
  subjects: inherited
- id: qaa/finance-2025/3.3.b8
  locator: { number: "3.3.b8", headingPath: ["Content, structure and delivery", "Cognitive abilities and generic skills"] }
  span: { start: 69171, end: 69406 }
  source: "communication, including presenting quantitative and qualitative information, together with analysis, argument and commentary, in a form appropriate to the intended audience, and verbal and/or non-verbal as well as written presentation"
  stem: "3.3"
  statementType: outcome
  rung: none
  force: must   # D-std-0016: "expected to" read as must
  level: fheq:6
  appliesTo: "bachelor's graduates of the subject"
  addressee: learner
  verbs: ["communication", "presenting"]
  about: "communication to an audience"
  themes: [none]
  domain: generic-skill
  award: ["bachelor's with honours"]
  gradeOf: none
  paraphrase: "Communicating quantitative and qualitative information with analysis and argument in a form suited to the audience, spoken, non-verbal and written."
  quote: full   # the issuer's statement is in `source` (D-std-0014)
  audience: both
  subjects: inherited
- id: qaa/finance-2025/3.3.b9
  locator: { number: "3.3.b9", headingPath: ["Content, structure and delivery", "Cognitive abilities and generic skills"] }
  span: { start: 69409, end: 69462 }
  source: "working with others (such as through group projects)."
  stem: "3.3"
  statementType: outcome
  rung: none
  force: must   # D-std-0016: "expected to" read as must
  level: fheq:6
  appliesTo: "bachelor's graduates of the subject"
  addressee: learner
  verbs: ["working"]
  about: "working with others"
  themes: [none]
  domain: generic-skill
  award: ["bachelor's with honours"]
  gradeOf: none
  paraphrase: "Working with others, for instance in group projects."
  quote: full   # the issuer's statement is in `source` (D-std-0014)
  audience: both
  subjects: inherited
- id: qaa/finance-2025/3.4
  locator: { number: "3.4", headingPath: ["Content, structure and delivery", "Teaching and learning"] }
  span: { start: 69485, end: 69957 }
  source: "3.4 It is the responsibility of each higher education provider offering a degree programme in Finance to select a set of teaching, learning and assessment activities that is appropriate for meeting the aims and desired outcomes of the degree. Whatever set of activities is determined, providers will be able to demonstrate how these activities enable students to achieve the subject-specific knowledge and skills, the cognitive abilities and generic skills set out above.\n"
  stem: none
  statementType: requirement
  rung: none
  force: will
  level: none
  appliesTo: "higher education providers offering Finance"
  addressee: provider
  verbs: ["select", "demonstrate", "achieve"]
  about: "the provider's choice of activities and showing they work"
  themes: [none]
  domain: none
  award: ["none"]
  gradeOf: none
  paraphrase: "Each provider is responsible for choosing teaching, learning and assessment suited to its degree's aims, and will be able to show how those activities let students reach the subject knowledge and skills and the generic skills in section 3."
  quote: full   # the issuer's statement is in `source` (D-std-0014)
  audience: practitioner
  subjects: inherited
- id: qaa/finance-2025/3.7
  locator: { number: "3.7", headingPath: ["Content, structure and delivery", "Teaching and learning"] }
  span: { start: 71237, end: 71931 }
  source: "3.7 In terms of delivery methods, blended learning, incorporating a mixture of online and in-person elements and appropriate combinations of synchronous and asynchronous materials and activities can be considered. This approach offers greater flexibility to students and educators, but it could create challenges related to engagement and motivation of students to fully benefit from these approaches. Technology-supported learning and assessment needs to be innovative, working with both students and the technology, to keep students motivated and proactively address potential issues with academic integrity. The application of the blended learning approach must maintain academic integrity.\n"
  stem: none
  statementType: requirement
  rung: none
  force: must
  level: none
  appliesTo: "blended learning"
  addressee: provider
  verbs: ["maintain", "needs"]
  about: "blended learning and academic integrity"
  themes: [none]
  domain: none
  award: ["none"]
  gradeOf: none
  paraphrase: "Blended delivery mixing online and in-person work can be used and adds flexibility but can weaken engagement; learning and assessment supported by technology needs fresh approaches that also address integrity, and blended learning must maintain academic integrity."
  quote: full   # the issuer's statement is in `source` (D-std-0014)
  audience: practitioner
  subjects: inherited
- id: qaa/finance-2025/3.8
  locator: { number: "3.8", headingPath: ["Content, structure and delivery", "Teaching and learning"] }
  span: { start: 71931, end: 72245 }
  source: "3.8 Students on both bachelor's and master's taught programmes in Finance often have diverse backgrounds. Programme directors and course leaders should consider specific help for subject-specific language, mathematical (where appropriate) support, academic writing, as well as study and examination skills support."
  stem: none
  statementType: expectation
  rung: none
  force: should
  level: none
  appliesTo: "programme directors and course leaders"
  addressee: provider
  verbs: ["consider"]
  about: "support for language, mathematics, writing and study skills"
  themes: [none]
  domain: none
  award: ["bachelor's with honours", "master's"]
  gradeOf: none
  paraphrase: "Finance students at both levels often come from varied backgrounds; programme directors and course leaders should consider targeted help with subject language, mathematics where needed, academic writing and study and exam skills."
  quote: full   # the issuer's statement is in `source` (D-std-0014)
  audience: practitioner
  subjects: inherited
- id: qaa/finance-2025/3.14
  locator: { number: "3.14", headingPath: ["Content, structure and delivery", "Assessment"] }
  span: { start: 74371, end: 74831 }
  source: "3.14 Where appropriate, the design of teaching and learning activities, together with associated assessment activities, can usefully be informed by current pedagogical developments and research in these areas (including developments in technology). Also, regular reviews must be undertaken to ensure that such activities remain 'fit for purpose' and\n\n22\nup to date in achieving the programme's desired outcomes with respect to this Subject Benchmark Statement."
  stem: none
  statementType: requirement
  rung: none
  force: must
  level: none
  appliesTo: "teaching, learning and assessment activities"
  addressee: provider
  verbs: ["informed", "undertaken", "ensure"]
  about: "regular review of activities"
  themes: [none]
  domain: none
  award: ["none"]
  gradeOf: none
  paraphrase: "Teaching and assessment design can draw on current pedagogical research and technology; regular reviews must be carried out so that the activities stay fit for purpose and current for the programme's outcomes."
  quote: full   # the issuer's statement is in `source` (D-std-0014)
  audience: practitioner
  subjects: inherited
- id: qaa/finance-2025/4.2
  locator: { number: "4.2", headingPath: ["Benchmark standards", "Introduction"] }
  span: { start: 75243, end: 75609 }
  source: "4.2 Most students are likely to perform significantly better than the minimum threshold standards outlined below. Each higher education provider has its own method of determining what appropriate evidence of this achievement will be and should refer to Annex D of the Frameworks for Higher Education Qualifications of UK Degree-Awarding Bodies for further guidance.\n"
  stem: none
  statementType: expectation
  rung: none
  force: should
  level: fheq:6
  appliesTo: "higher education providers"
  addressee: provider
  verbs: ["refer", "determining"]
  about: "Annex D for evidence of achievement"
  themes: [none]
  domain: none
  award: ["bachelor's with honours"]
  gradeOf: none
  paraphrase: "Most students are likely to go well beyond the threshold; each provider sets how to evidence achievement and should consult Annex D of the Frameworks for more guidance."
  quote: full   # the issuer's statement is in `source` (D-std-0014)
  audience: practitioner
  subjects: inherited
- id: qaa/finance-2025/4.3
  locator: { number: "4.3", headingPath: ["Benchmark standards", "Introduction"] }
  span: { start: 75609, end: 76111 }
  source: "4.3 Please note that the minimum threshold, typical and excellent standards are not intended to specify universal competence standards for a discipline. If a provider chooses to develop competence standards (as defined by the Equality Act 2010) as part of a programme specification these can be informed by the relevant Subject Benchmark Statement along with any PSRB requirements. In these circumstances, providers should follow the most recent guidance from the Equality and Human Rights Commission ."
  stem: none
  statementType: expectation
  rung: none
  force: should
  level: none
  appliesTo: "providers developing competence standards"
  addressee: provider
  verbs: ["follow", "informed"]
  about: "competence standards and Equality Act guidance"
  themes: [none]
  domain: none
  award: ["none"]
  gradeOf: none
  paraphrase: "The three levels are not universal competence standards; a provider that sets competence standards under the Equality Act 2010 may draw on the statement and PSRB requirements, and should follow the latest guidance from the Equality and Human Rights Commission."
  quote: full   # the issuer's statement is in `source` (D-std-0014)
  audience: practitioner
  subjects: inherited
- id: qaa/finance-2025/4.4.b1
  locator: { number: "4.4.b1", headingPath: ["Benchmark standards", "Threshold level"] }
  span: { start: 76249, end: 76338 }
  source: "demonstrate a depth of knowledge of the main concepts, theories and tools used in finance"
  stem: "4.4"
  statementType: threshold
  rung: threshold
  force: threshold
  level: fheq:6
  appliesTo: "graduates at the threshold level"
  addressee: learner
  verbs: ["demonstrate"]
  about: "depth of knowledge of core concepts"
  themes: [none]
  domain: knowledge
  award: ["bachelor's with honours"]
  gradeOf: none
  paraphrase: "Will show a depth of knowledge of finance's main concepts, theories and tools."
  quote: full   # the issuer's statement is in `source` (D-std-0014)
  audience: both
  subjects: inherited
- id: qaa/finance-2025/4.4.b2
  locator: { number: "4.4.b2", headingPath: ["Benchmark standards", "Threshold level"] }
  span: { start: 76341, end: 76446 }
  source: "apply acquired knowledge to finance problems relevant to individuals, companies, institutions and society"
  stem: "4.4"
  statementType: threshold
  rung: threshold
  force: threshold
  level: fheq:6
  appliesTo: "graduates at the threshold level"
  addressee: learner
  verbs: ["apply"]
  about: "applying knowledge to finance problems"
  themes: [none]
  domain: subject-skill
  award: ["bachelor's with honours"]
  gradeOf: none
  paraphrase: "Will apply what they know to finance problems that matter to people, firms, institutions and society."
  quote: full   # the issuer's statement is in `source` (D-std-0014)
  audience: both
  subjects: inherited
- id: qaa/finance-2025/4.4.b3
  locator: { number: "4.4.b3", headingPath: ["Benchmark standards", "Threshold level"] }
  span: { start: 76449, end: 76582 }
  source: "demonstrate understanding of the institutional, economic, political, regulatory and social environments within which finance operates"
  stem: "4.4"
  statementType: threshold
  rung: threshold
  force: threshold
  level: fheq:6
  appliesTo: "graduates at the threshold level"
  addressee: learner
  verbs: ["demonstrate"]
  about: "the environments finance operates in"
  themes: [none]
  domain: understanding
  award: ["bachelor's with honours"]
  gradeOf: none
  paraphrase: "Will show they understand the settings of finance: institutional, economic, political, regulatory and social."
  quote: full   # the issuer's statement is in `source` (D-std-0014)
  audience: both
  subjects: inherited
- id: qaa/finance-2025/4.4.b4
  locator: { number: "4.4.b4", headingPath: ["Benchmark standards", "Threshold level"] }
  span: { start: 76585, end: 76714 }
  source: "recognise the fundamental importance of reliable governance structures and of ethical considerations in financial decision making"
  stem: "4.4"
  statementType: threshold
  rung: threshold
  force: threshold
  level: fheq:6
  appliesTo: "graduates at the threshold level"
  addressee: learner
  verbs: ["recognise"]
  about: "governance and ethics in decisions"
  themes: [none]
  domain: understanding
  award: ["bachelor's with honours"]
  gradeOf: none
  paraphrase: "Will recognise how much sound governance and ethics matter in financial decisions."
  quote: full   # the issuer's statement is in `source` (D-std-0014)
  audience: both
  subjects: inherited
- id: qaa/finance-2025/4.4.b5
  locator: { number: "4.4.b5", headingPath: ["Benchmark standards", "Threshold level"] }
  span: { start: 76717, end: 76852 }
  source: "understand the operation, regulation and supervision of financial markets and some of the services and products traded in these markets"
  stem: "4.4"
  statementType: threshold
  rung: threshold
  force: threshold
  level: fheq:6
  appliesTo: "graduates at the threshold level"
  addressee: learner
  verbs: ["understand"]
  about: "markets, their regulation and products"
  themes: [none]
  domain: understanding
  award: ["bachelor's with honours"]
  gradeOf: none
  paraphrase: "Will understand how financial markets work and are regulated and supervised, with some of what they trade."
  quote: full   # the issuer's statement is in `source` (D-std-0014)
  audience: both
  subjects: inherited
- id: qaa/finance-2025/4.4.b6
  locator: { number: "4.4.b6", headingPath: ["Benchmark standards", "Threshold level"] }
  span: { start: 76855, end: 76939 }
  source: "understand the fundamentals of valuation, security analysis and portfolio management"
  stem: "4.4"
  statementType: threshold
  rung: threshold
  force: threshold
  level: fheq:6
  appliesTo: "graduates at the threshold level"
  addressee: learner
  verbs: ["understand"]
  about: "valuation, securities and portfolios"
  themes: [none]
  domain: understanding
  award: ["bachelor's with honours"]
  gradeOf: none
  paraphrase: "Will understand the basics of valuing assets, analysing securities and managing portfolios."
  quote: full   # the issuer's statement is in `source` (D-std-0014)
  audience: both
  subjects: inherited
- id: qaa/finance-2025/4.4.b7
  locator: { number: "4.4.b7", headingPath: ["Benchmark standards", "Threshold level"] }
  span: { start: 76942, end: 77023 }
  source: "collect, manage, synthesise and interpret financial, accounting and economic data"
  stem: "4.4"
  statementType: threshold
  rung: threshold
  force: threshold
  level: fheq:6
  appliesTo: "graduates at the threshold level"
  addressee: learner
  verbs: ["collect", "manage", "synthesise", "interpret"]
  about: "handling financial and economic data"
  themes: [none]
  domain: subject-skill
  award: ["bachelor's with honours"]
  gradeOf: none
  paraphrase: "Will gather, organise, combine and make sense of financial, accounting and economic data."
  quote: full   # the issuer's statement is in `source` (D-std-0014)
  audience: both
  subjects: inherited
- id: qaa/finance-2025/4.4.b8
  locator: { number: "4.4.b8", headingPath: ["Benchmark standards", "Threshold level"] }
  span: { start: 77026, end: 77112 }
  source: "execute straightforward statistical analyses of financial data using software packages"
  stem: "4.4"
  statementType: threshold
  rung: threshold
  force: threshold
  level: fheq:6
  appliesTo: "graduates at the threshold level"
  addressee: learner
  verbs: ["execute"]
  about: "straightforward statistical analysis with software"
  themes: [none]
  domain: subject-skill
  award: ["bachelor's with honours"]
  gradeOf: none
  paraphrase: "Will carry out simple statistical analyses of financial data in software."
  quote: full   # the issuer's statement is in `source` (D-std-0014)
  audience: both
  subjects: inherited
- id: qaa/finance-2025/4.4.b9
  locator: { number: "4.4.b9", headingPath: ["Benchmark standards", "Threshold level"] }
  span: { start: 77115, end: 77218 }
  source: "assess the significance, problems and limitations of finance theories and associated empirical evidence"
  stem: "4.4"
  statementType: threshold
  rung: threshold
  force: threshold
  level: fheq:6
  appliesTo: "graduates at the threshold level"
  addressee: learner
  verbs: ["assess"]
  about: "limits of theory and evidence"
  themes: [none]
  domain: subject-skill
  award: ["bachelor's with honours"]
  gradeOf: none
  paraphrase: "Will judge the importance, problems and limits of finance theories and the evidence behind them."
  quote: full   # the issuer's statement is in `source` (D-std-0014)
  audience: both
  subjects: inherited
- id: qaa/finance-2025/4.4.b10
  locator: { number: "4.4.b10", headingPath: ["Benchmark standards", "Threshold level"] }
  span: { start: 77221, end: 77360 }
  source: "demonstrate a critical appreciation and understanding of how finance theory and empirical evidence can be used to guide policy and practice"
  stem: "4.4"
  statementType: threshold
  rung: threshold
  force: threshold
  level: fheq:6
  appliesTo: "graduates at the threshold level"
  addressee: learner
  verbs: ["demonstrate", "guide"]
  about: "theory and evidence guiding policy and practice"
  themes: [none]
  domain: understanding
  award: ["bachelor's with honours"]
  gradeOf: none
  paraphrase: "Will show a critical understanding of how theory and evidence in finance can inform policy and practice."
  quote: full   # the issuer's statement is in `source` (D-std-0014)
  audience: both
  subjects: inherited
- id: qaa/finance-2025/4.4.b11
  locator: { number: "4.4.b11", headingPath: ["Benchmark standards", "Threshold level"] }
  span: { start: 77363, end: 77473 }
  source: "understand the importance of finance as a key lever to achieve sustainable outcomes for society and the planet"
  stem: "4.4"
  statementType: threshold
  rung: threshold
  force: threshold
  level: fheq:6
  appliesTo: "graduates at the threshold level"
  addressee: learner
  verbs: ["understand", "achieve"]
  about: "finance as a lever for sustainable outcomes"
  themes: [none]
  domain: understanding
  award: ["bachelor's with honours"]
  gradeOf: none
  paraphrase: "Will understand why finance is a key means of reaching sustainable outcomes for society and the planet."
  quote: full   # the issuer's statement is in `source` (D-std-0014)
  audience: both
  subjects: inherited
- id: qaa/finance-2025/4.4.b12
  locator: { number: "4.4.b12", headingPath: ["Benchmark standards", "Threshold level"] }
  span: { start: 77480, end: 77602 }
  source: "understand the impact fintech exerts on financial services through innovations such as AI, blockchain and digital payments"
  stem: "4.4"
  statementType: threshold
  rung: threshold
  force: threshold
  level: fheq:6
  appliesTo: "graduates at the threshold level"
  addressee: learner
  verbs: ["understand", "exerts"]
  about: "the effect of fintech on financial services"
  themes: [none]
  domain: understanding
  award: ["bachelor's with honours"]
  gradeOf: none
  paraphrase: "Will understand how fintech changes financial services through AI, blockchain and digital payments."
  quote: full   # the issuer's statement is in `source` (D-std-0014)
  audience: both
  subjects: inherited
- id: qaa/finance-2025/4.4.b13
  locator: { number: "4.4.b13", headingPath: ["Benchmark standards", "Threshold level"] }
  span: { start: 77605, end: 77769 }
  source: "distil and summarise financial knowledge and information, communicating (both verbally and in writing) knowledge and/or information effectively to diverse audiences"
  stem: "4.4"
  statementType: threshold
  rung: threshold
  force: threshold
  level: fheq:6
  appliesTo: "graduates at the threshold level"
  addressee: learner
  verbs: ["distil", "summarise", "communicating"]
  about: "summarising and communicating to varied audiences"
  themes: [none]
  domain: generic-skill
  award: ["bachelor's with honours"]
  gradeOf: none
  paraphrase: "Will condense financial knowledge and information and convey it well, orally and in writing, to varied audiences."
  quote: full   # the issuer's statement is in `source` (D-std-0014)
  audience: both
  subjects: inherited
- id: qaa/finance-2025/4.4.b14
  locator: { number: "4.4.b14", headingPath: ["Benchmark standards", "Threshold level"] }
  span: { start: 77772, end: 77887 }
  source: "demonstrate collaborative and leadership skills by working productively in both finance and interdisciplinary teams"
  stem: "4.4"
  statementType: threshold
  rung: threshold
  force: threshold
  level: fheq:6
  appliesTo: "graduates at the threshold level"
  addressee: learner
  verbs: ["demonstrate", "working"]
  about: "collaboration and leadership in teams"
  themes: [none]
  domain: generic-skill
  award: ["bachelor's with honours"]
  gradeOf: none
  paraphrase: "Will show they can collaborate and lead by working well in finance and cross-disciplinary teams."
  quote: full   # the issuer's statement is in `source` (D-std-0014)
  audience: both
  subjects: inherited
- id: qaa/finance-2025/4.4.b15
  locator: { number: "4.4.b15", headingPath: ["Benchmark standards", "Threshold level"] }
  span: { start: 77890, end: 77946 }
  source: "assert intellectual independence and critical judgement."
  stem: "4.4"
  statementType: threshold
  rung: threshold
  force: threshold
  level: fheq:6
  appliesTo: "graduates at the threshold level"
  addressee: learner
  verbs: ["assert"]
  about: "intellectual independence and critical judgement"
  themes: [none]
  domain: generic-skill
  award: ["bachelor's with honours"]
  gradeOf: none
  paraphrase: "Will show independent thought and critical judgement."
  quote: full   # the issuer's statement is in `source` (D-std-0014)
  audience: both
  subjects: inherited
- id: qaa/finance-2025/4.5.s1
  locator: { number: "4.5.s1", headingPath: ["Benchmark standards", "Typical level"] }
  span: { start: 77965, end: 78170 }
  source: "Typical graduates can distinguish themselves from threshold graduates by demonstrating a breadth and depth of knowledge and understanding and showing a clear and critical insight of the Finance discipline."
  stem: none
  statementType: typical
  rung: typical
  force: will
  level: fheq:6
  appliesTo: "graduates at the typical level"
  addressee: learner
  verbs: ["distinguish", "demonstrating", "showing"]
  about: "breadth, depth and critical insight"
  themes: [none]
  domain: knowledge
  award: ["bachelor's with honours"]
  gradeOf: none
  paraphrase: "Graduates at the typical level stand out from those at threshold by the breadth and depth of what they know and understand and by clear, critical insight into finance."
  quote: full   # the issuer's statement is in `source` (D-std-0014)
  audience: both
  subjects: inherited
- id: qaa/finance-2025/4.5.s2
  locator: { number: "4.5.s2", headingPath: ["Benchmark standards", "Typical level"] }
  span: { start: 78171, end: 78369 }
  source: "They will demonstrate a rigorous understanding of Finance theories, paradigms, methods, concepts and principles along with a strong understanding of some specialised topics within the Finance field."
  stem: none
  statementType: typical
  rung: typical
  force: will
  level: fheq:6
  appliesTo: "graduates at the typical level"
  addressee: learner
  verbs: ["demonstrate"]
  about: "rigorous theory and some specialised topics"
  themes: [none]
  domain: knowledge
  award: ["bachelor's with honours"]
  gradeOf: { statement: qaa/finance-2025/4.4.b1, basis: inferred }
  paraphrase: "Will show a rigorous grasp of the theories, paradigms, methods, concepts and principles of finance, and a strong grasp of some specialised topics."
  quote: full   # the issuer's statement is in `source` (D-std-0014)
  audience: both
  subjects: inherited
- id: qaa/finance-2025/4.5.s3
  locator: { number: "4.5.s3", headingPath: ["Benchmark standards", "Typical level"] }
  span: { start: 78370, end: 78672 }
  source: "They will possess a sophisticated ability to select and critically appraise a wide range of information, sources, views and knowledge which may be specialised within a sub-discipline of Finance or interdisciplinary in nature and recognise the uncertainty, ambiguity and limits of sources and knowledge."
  stem: none
  statementType: typical
  rung: typical
  force: will
  level: fheq:6
  appliesTo: "graduates at the typical level"
  addressee: learner
  verbs: ["possess", "select", "appraise", "recognise"]
  about: "critical appraisal of sources and their limits"
  themes: [none]
  domain: subject-skill
  award: ["bachelor's with honours"]
  gradeOf: { statement: qaa/finance-2025/4.4.b9, basis: inferred }
  paraphrase: "Will have a sophisticated ability to choose many kinds of information, sources, views and knowledge and appraise them critically, specialised or interdisciplinary, recognising their uncertainty, ambiguity and limits."
  quote: full   # the issuer's statement is in `source` (D-std-0014)
  audience: both
  subjects: inherited
- id: qaa/finance-2025/4.5.s4
  locator: { number: "4.5.s4", headingPath: ["Benchmark standards", "Typical level"] }
  span: { start: 78673, end: 78893 }
  source: "With a degree of autonomy, they will conduct thorough background investigation, reading, analysis, research, and/or study and solve complex finance problems, applying a wide range of established methodologies accurately."
  stem: none
  statementType: typical
  rung: typical
  force: will
  level: fheq:6
  appliesTo: "graduates at the typical level"
  addressee: learner
  verbs: ["conduct", "solve", "applying"]
  about: "investigation and solving complex problems"
  themes: [none]
  domain: subject-skill
  award: ["bachelor's with honours"]
  gradeOf: { statement: qaa/finance-2025/4.4.b2, basis: inferred }
  paraphrase: "With some autonomy, will carry out thorough investigation, reading, analysis and research and solve complex finance problems, using a wide range of established methods accurately."
  quote: full   # the issuer's statement is in `source` (D-std-0014)
  audience: both
  subjects: inherited
- id: qaa/finance-2025/4.5.s5
  locator: { number: "4.5.s5", headingPath: ["Benchmark standards", "Typical level"] }
  span: { start: 78894, end: 79184 }
  source: "They will meaningfully select, evaluate, synthesize, discuss, communicate and present different information and results with substantiated arguments and demonstrate thorough and thoughtful interpretation of complex ideas and a high level of creativity and originality throughout their work."
  stem: none
  statementType: typical
  rung: typical
  force: will
  level: fheq:6
  appliesTo: "graduates at the typical level"
  addressee: learner
  verbs: ["select", "evaluate", "synthesize", "communicate", "present", "demonstrate"]
  about: "synthesis, argument and originality in communication"
  themes: [none]
  domain: generic-skill
  award: ["bachelor's with honours"]
  gradeOf: { statement: qaa/finance-2025/4.4.b13, basis: inferred }
  paraphrase: "Will select, evaluate, synthesise, discuss and present information and results with well-supported arguments, interpreting complex ideas thoroughly and showing a high degree of creativity and originality."
  quote: full   # the issuer's statement is in `source` (D-std-0014)
  audience: both
  subjects: inherited
- id: qaa/finance-2025/4.6.s1
  locator: { number: "4.6.s1", headingPath: ["Benchmark standards", "Excellent level"] }
  span: { start: 79205, end: 79444 }
  source: "Excellent level graduates can distinguish themselves from threshold and typical graduates by showing exceptional knowledge and understanding of the Finance discipline, significantly beyond the typical level and beyond what has been taught."
  stem: none
  statementType: excellent
  rung: excellent
  force: will
  level: fheq:6
  appliesTo: "graduates at the excellent level"
  addressee: learner
  verbs: ["distinguish", "showing"]
  about: "exceptional knowledge beyond the taught"
  themes: [none]
  domain: knowledge
  award: ["bachelor's with honours"]
  gradeOf: { statement: qaa/finance-2025/4.5.s1, basis: inferred }
  paraphrase: "Graduates at the excellent level stand out from those at threshold and typical levels by exceptional knowledge and understanding of finance, well past the typical and past what was taught."
  quote: full   # the issuer's statement is in `source` (D-std-0014)
  audience: both
  subjects: inherited
- id: qaa/finance-2025/4.6.s2
  locator: { number: "4.6.s2", headingPath: ["Benchmark standards", "Excellent level"] }
  span: { start: 79445, end: 79647 }
  source: "They will demonstrate an exceptional knowledge of Finance theories, paradigms, methods, concepts and principles and will have in-depth knowledge of a range of specialised areas within the Finance field."
  stem: none
  statementType: excellent
  rung: excellent
  force: will
  level: fheq:6
  appliesTo: "graduates at the excellent level"
  addressee: learner
  verbs: ["demonstrate", "have"]
  about: "exceptional theory and in-depth specialist knowledge"
  themes: [none]
  domain: knowledge
  award: ["bachelor's with honours"]
  gradeOf: { statement: qaa/finance-2025/4.5.s2, basis: inferred }
  paraphrase: "Will show exceptional command of the theories, paradigms, methods, concepts and principles of finance and deep knowledge of several specialised areas."
  quote: full   # the issuer's statement is in `source` (D-std-0014)
  audience: both
  subjects: inherited
- id: qaa/finance-2025/4.6.s3
  locator: { number: "4.6.s3", headingPath: ["Benchmark standards", "Excellent level"] }
  span: { start: 79648, end: 79824 }
  source: "They will assert intellectual independence and conduct thorough and extensive background investigation, reading, analysis, research, and/or study well beyond the typical range."
  stem: none
  statementType: excellent
  rung: excellent
  force: will
  level: fheq:6
  appliesTo: "graduates at the excellent level"
  addressee: learner
  verbs: ["assert", "conduct"]
  about: "independent, extensive investigation"
  themes: [none]
  domain: subject-skill
  award: ["bachelor's with honours"]
  gradeOf: { statement: qaa/finance-2025/4.5.s4, basis: inferred }
  paraphrase: "Will think independently and carry out thorough, extensive investigation, reading, analysis and research well past the typical range."
  quote: full   # the issuer's statement is in `source` (D-std-0014)
  audience: both
  subjects: inherited
- id: qaa/finance-2025/4.6.s4
  locator: { number: "4.6.s4", headingPath: ["Benchmark standards", "Excellent level"] }
  span: { start: 79825, end: 80034 }
  source: "They will possess an exceptional ability to critically appraise a wide range of sources, views and knowledge and masterly appreciate the uncertainty, ambiguity and limits of those views, sources and knowledge."
  stem: none
  statementType: excellent
  rung: excellent
  force: will
  level: fheq:6
  appliesTo: "graduates at the excellent level"
  addressee: learner
  verbs: ["possess", "appraise", "appreciate"]
  about: "exceptional critical appraisal"
  themes: [none]
  domain: subject-skill
  award: ["bachelor's with honours"]
  gradeOf: { statement: qaa/finance-2025/4.5.s3, basis: inferred }
  paraphrase: "Will have an exceptional ability to appraise many sources, views and knowledge critically and a masterly sense of their uncertainty, ambiguity and limits."
  quote: full   # the issuer's statement is in `source` (D-std-0014)
  audience: both
  subjects: inherited
- id: qaa/finance-2025/4.6.s5
  locator: { number: "4.6.s5", headingPath: ["Benchmark standards", "Excellent level"] }
  span: { start: 80035, end: 80321 }
  source: "They will show exceptional problem-solving skills and a strong ability for decision-making and for solving complex finance problems, with a high degree of autonomy, justifying and evidencing the use and application of a wide range of established methodologies critically and accurately."
  stem: none
  statementType: excellent
  rung: excellent
  force: will
  level: fheq:6
  appliesTo: "graduates at the excellent level"
  addressee: learner
  verbs: ["show", "solving", "justifying", "evidencing"]
  about: "exceptional problem-solving and decisions"
  themes: [none]
  domain: subject-skill
  award: ["bachelor's with honours"]
  gradeOf: { statement: qaa/finance-2025/4.5.s4, basis: inferred }
  paraphrase: "Will show exceptional problem-solving and strong decision-making on complex finance problems, working largely autonomously, justifying and evidencing the critical and accurate use of a wide range of established methods."
  quote: full   # the issuer's statement is in `source` (D-std-0014)
  audience: both
  subjects: inherited
- id: qaa/finance-2025/4.6.s6
  locator: { number: "4.6.s6", headingPath: ["Benchmark standards", "Excellent level"] }
  span: { start: 80322, end: 80449 }
  source: "They will proficiently select, evaluate, synthesize, discuss, communicate and present different views, information and results."
  stem: none
  statementType: excellent
  rung: excellent
  force: will
  level: fheq:6
  appliesTo: "graduates at the excellent level"
  addressee: learner
  verbs: ["select", "evaluate", "synthesize", "communicate", "present"]
  about: "proficient synthesis and presentation"
  themes: [none]
  domain: generic-skill
  award: ["bachelor's with honours"]
  gradeOf: { statement: qaa/finance-2025/4.5.s5, basis: inferred }
  paraphrase: "Will proficiently select, evaluate, synthesise, discuss and present views, information and results."
  quote: full   # the issuer's statement is in `source` (D-std-0014)
  audience: both
  subjects: inherited
- id: qaa/finance-2025/4.6.s7
  locator: { number: "4.6.s7", headingPath: ["Benchmark standards", "Excellent level"] }
  span: { start: 80450, end: 80683 }
  source: "They will construct and present substantiated arguments and demonstrate a sophisticated perception and critical insight of complex matters and ideas and an exceptional level of creativity, flair and originality throughout their work."
  stem: none
  statementType: excellent
  rung: excellent
  force: will
  level: fheq:6
  appliesTo: "graduates at the excellent level"
  addressee: learner
  verbs: ["construct", "present", "demonstrate"]
  about: "substantiated argument, insight and originality"
  themes: [none]
  domain: generic-skill
  award: ["bachelor's with honours"]
  gradeOf: { statement: qaa/finance-2025/4.5.s5, basis: inferred }
  paraphrase: "Will build and present well-supported arguments and show sophisticated perception, critical insight into complex matters and exceptional creativity, flair and originality."
  quote: full   # the issuer's statement is in `source` (D-std-0014)
  audience: both
  subjects: inherited
```

### S4a Audience versions
<!-- label: both; status: drafted; basis: primary. forPractitioner: for the programme designer or teacher. forBeneficiary: for the student, second person, naming no issuer. author-agent-written: instructions to an AI agent writing about the statement (a course document, a handbook, an outcome, a report). author-agent-dialogue: instructions to an AI agent using the statement in conversation (with a student, a teacher or a programme team). Written fresh from the held text alone (benchmark rule 6; Abbott, 15:42). -->
```yaml
- statement: qaa/finance-2025/1.4
  forPractitioner: { text: "For a joint or combined award, read this statement alongside the partner subject's statement, and check that the Finance part keeps its scope, depth and balance of theory and practice.", rewrite: light, force: should, status: drafted }
  forBeneficiary: { text: "not-applicable: a duty on those who design joint courses", rewrite: full, force: should, status: drafted }
  author-agent-written: "Describe this as guidance that should shape joint and combined Finance courses, addressed to course designers. Apply it to joint honours at bachelor's level. Cite it as (QAA, 2025, Finance Subject Benchmark Statement, para 1.4). Do not claim that it sets learning outcomes for students or that it overrides the partner subject's statement; set it beside the other subject's statement and paragraph 2.11 on what joint degree students achieve."
  author-agent-dialogue: "Raise it when a team is designing or reviewing a joint or combined award with Finance. Put it to the programme team as a design or review duty in their own terms. Ask: \"Which statement did you use for the other half, and where would theory or application be thin?\" Avoid reading the paragraph aloud and handing this duty to a student as if it were theirs."
- statement: qaa/finance-2025/1.6
  forPractitioner: { text: "Build the curriculum so that students study both the established foundations and current advances in finance theory and practice, organised around two main subject domains.", rewrite: light, force: must, status: drafted }
  forBeneficiary: { text: "Studying finance means learning both its established foundations and its newest ideas, in theory and in practice, so that you understand what finance does in organisations.", rewrite: full, force: must, status: drafted }
  author-agent-written: "Describe this as a requirement the subject places on every Finance student: to study both foundations and new developments. Treat it as holding for bachelor's and master's study alike, without a level of its own. Cite it as (QAA, 2025, Finance Subject Benchmark Statement, para 1.6). Do not claim that it is an assessed outcome or a regulatory rule; set it beside paragraph 1.7 (the two domains) and the threshold item 4.4.b1."
  author-agent-dialogue: "Raise it when a student asks what a Finance degree is for or why new topics keep entering the course. Put it to a student in plain words and the second person; to staff, frame it as what the course lets every graduate show. Ask: \"Which parts of your course feel like foundations and which feel like current developments?\" Avoid reading the text aloud at length and treating it as a graded standard."
- statement: qaa/finance-2025/1.7
  forPractitioner: { text: "Cover both core domains, financial markets and institutions, and investment and corporate finance, and add contemporary areas such as sustainable finance, fintech, AI and alternative investments; the newer areas are expected, the core domains required.", rewrite: light, force: must, status: drafted }
  forBeneficiary: { text: "You will need to understand how financial markets and institutions work and the principles of investment, value, corporate finance and risk; you are also expected to understand newer areas such as sustainable finance, fintech and AI.", rewrite: full, force: must, status: drafted }
  author-agent-written: "Describe this as what the subject requires students to understand (the two core domains) and what it also expects (contemporary areas, given as examples). Treat it as holding for bachelor's and master's study, without a level of its own. Cite it as (QAA, 2025, Finance Subject Benchmark Statement, para 1.7). Do not claim that the listed contemporary areas are compulsory topics, since the text says they may include others; set it beside the subject knowledge list 3.2.b1 to 3.2.b12 and threshold items 4.4.b5 and 4.4.b6."
  author-agent-dialogue: "Raise it when a student or a module team asks what core content a Finance course must cover. With a student use plain words and the second person; with staff separate the required domains from the expected newer areas. Ask: \"Which of the two core domains do you feel more secure in, and which newer area have you met so far?\" Avoid reciting the lists and presenting the example areas as a fixed syllabus."
- statement: qaa/finance-2025/1.8
  forPractitioner: { text: "Whatever the angle a course takes, make sure every student will come away conscious of the ethical and social sides of financial activity, not only the economic one.", rewrite: light, force: will, status: drafted }
  forBeneficiary: { text: "Whatever your route through the subject, you will become aware of the ethical and social side of financial activity and systems, not only the economics.", rewrite: full, force: will, status: drafted }
  author-agent-written: "Describe this as a minimum expected outcome, in \"will\", for every Finance student. Read it at the level of the award the student is taking; it names no level. Cite it as (QAA, 2025, Finance Subject Benchmark Statement, para 1.8). Do not claim that it requires a separate ethics module; set it beside threshold item 4.4.b4 (governance and ethics) and the level 6 descriptor qaa/fheq-2024/4.15.b7."
  author-agent-dialogue: "Raise it when a student treats finance as purely technical or asks why ethics appears in the course. Put it to a student in plain words and the second person; to staff, frame it as what the course lets every graduate show. Ask: \"Can you name one financial decision you studied where the ethical or social effect mattered as much as the return?\" Avoid lecturing and treating awareness as if it were a graded rung."
- statement: qaa/finance-2025/1.15.b1
  forPractitioner: { text: "Judge a specialist master's in Finance against the excellent level (4.6) and against extra content criteria for its specialism; entry is usually a second-class Finance honours degree or above.", rewrite: light, force: must, status: drafted }
  forBeneficiary: { text: "not-applicable: a statement about how a course is evaluated and who it admits", rewrite: full, force: must, status: drafted }
  author-agent-written: "Describe this as how the statement would expect a specialist master's to be evaluated: against its highest levels, the excellent rung. Place the award at FHEQ level 7 (FQHEIS level 11 in Scotland). Cite it as (QAA, 2025, Finance Subject Benchmark Statement, para 1.15.b1). Do not claim that the statement sets master's rungs of its own or that this wording (\"would be expected\") is a requirement; set it beside the excellent level 4.6.s1 to 4.6.s7 and the master's descriptor qaa/fheq-2024/4.17.b1."
  author-agent-dialogue: "Raise it when a team designs or reviews a specialist master's in Finance. Put it to the programme team as a design or review duty in their own terms. Ask: \"Which excellent-level sentences does your programme specification reach, and what content criteria does your specialism add?\" Avoid telling a student that the excellent rung is the pass mark for a master's."
- statement: qaa/finance-2025/1.18
  forPractitioner: { text: "Embed EDI meaningfully in the culture, practice and curriculum of every Finance course, and refer to industry EDI codes where they apply.", rewrite: light, force: should, status: drafted }
  forBeneficiary: { text: "not-applicable: a duty on the course and the discipline", rewrite: full, force: should, status: drafted }
  author-agent-written: "Describe this as an expectation, in \"should\", on Finance courses to embed EDI. It holds for every award and has no level. Cite it as (QAA, 2025, Finance Subject Benchmark Statement, para 1.18). Do not claim that it sets a student outcome or a legal duty beyond the equality duties it mentions; set it beside paragraphs 1.22 to 1.27 and the theme record theme:edi."
  author-agent-dialogue: "Raise it when a team reviews a programme for inclusion or an EDI audit is due. Put it to the programme team as a design or review duty in their own terms. Ask: \"Where in the curriculum and its culture is EDI visible to students, and where is it only a policy?\" Avoid reading the paragraph aloud and handing this duty to a student as if it were theirs."
- statement: qaa/finance-2025/1.22
  forPractitioner: { text: "Create a learning environment where every student can thrive and feels represented and included, and support widening participation to limit the effect of economic disadvantage.", rewrite: light, force: must, status: drafted }
  forBeneficiary: { text: "not-applicable: a duty on those who teach", rewrite: full, force: must, status: drafted }
  author-agent-written: "Describe this as a requirement, in \"must\", on those who teach Finance. It holds at every level. Cite it as (QAA, 2025, Finance Subject Benchmark Statement, para 1.22). Do not claim that it sets a student outcome; set it beside paragraph 1.18 and the theme record theme:edi."
  author-agent-dialogue: "Raise it when teaching staff discuss belonging, attainment gaps or widening participation. Put it to the programme team as a design or review duty in their own terms. Ask: \"Which groups of students feel least represented in your examples and case studies?\" Avoid reading the paragraph aloud and handing this duty to a student as if it were theirs."
- statement: qaa/finance-2025/1.23
  forPractitioner: { text: "Design assessment to be as inclusive as possible: offer alternatives in type, duration and mode where suitable, such as a written task for a presentation or extra exam time.", rewrite: light, force: should, status: drafted }
  forBeneficiary: { text: "not-applicable: a duty on the course; a student meets its effect as alternative assessment", rewrite: full, force: should, status: drafted }
  author-agent-written: "Describe this as an expectation, in \"should\", on assessment design. It holds at every level. Cite it as (QAA, 2025, Finance Subject Benchmark Statement, para 1.23). Do not claim that students have a right to any one listed alternative; set it beside paragraph 1.29.b8 on accessible assessment and Annex D, std:doc:qaa-fheq-2024-framework."
  author-agent-dialogue: "Raise it when an assessment strategy is being written or reviewed. Put it to the programme team as a design or review duty in their own terms. Ask: \"Which assessments could take a different form without changing what they test?\" Avoid reading the paragraph aloud and handing this duty to a student as if it were theirs."
- statement: qaa/finance-2025/1.24.b1
  forPractitioner: { text: "Make physical and virtual learning spaces flexible and reflective of the students who use them.", rewrite: light, force: must, status: drafted }
  forBeneficiary: { text: "not-applicable: a duty on the course and its spaces", rewrite: full, force: must, status: drafted }
  author-agent-written: "Describe this as a requirement, in \"must\", on learning environments, given as one example of embedding EDI. It holds at every level. Cite it as (QAA, 2025, Finance Subject Benchmark Statement, para 1.24). Do not claim that it is a student outcome; set it beside the other items of 1.24 and paragraph 1.29.b3 on safe learning spaces."
  author-agent-dialogue: "Raise it when a team reviews its rooms, virtual learning environment or timetable. Put it to the programme team as a design or review duty in their own terms. Ask: \"Who finds your learning spaces hardest to use, and why?\" Avoid reading the paragraph aloud and handing this duty to a student as if it were theirs."
- statement: qaa/finance-2025/1.24.b2
  forPractitioner: { text: "Choose readings, cases and assessment materials that carry varied perspectives, so that no student is disadvantaged by background.", rewrite: light, force: should, status: drafted }
  forBeneficiary: { text: "not-applicable: a duty on those who choose materials", rewrite: full, force: should, status: drafted }
  author-agent-written: "Describe this as an expectation, in \"should\", on teaching and assessment materials. It holds at every level. Cite it as (QAA, 2025, Finance Subject Benchmark Statement, para 1.24). Do not claim that every reading list must meet a quota; set it beside paragraph 1.29.b2 on materials reflecting the cohort."
  author-agent-dialogue: "Raise it when a module team refreshes its reading list or case studies. Put it to the programme team as a design or review duty in their own terms. Ask: \"Whose markets, firms and households appear in your cases, and whose are missing?\" Avoid reading the paragraph aloud and handing this duty to a student as if it were theirs."
- statement: qaa/finance-2025/1.24.b3
  forPractitioner: { text: "Attend to the hidden curriculum, especially the jargon of finance, so that unspoken expectations and terms do not block learning.", rewrite: light, force: must, status: drafted }
  forBeneficiary: { text: "not-applicable: a duty on those who teach", rewrite: full, force: must, status: drafted }
  author-agent-written: "Describe this as a requirement read from \"is necessary\", on attention to the hidden curriculum. It holds at every level. Cite it as (QAA, 2025, Finance Subject Benchmark Statement, para 1.24). Do not claim that the issuer used \"must\" here: the force is our reading (Part E); set it beside paragraph 1.29.b4 and QAA's guide on the hidden curriculum (not yet ingested)."
  author-agent-dialogue: "Raise it when students struggle with finance terms or unstated expectations. Put it to the programme team as a design or review duty in their own terms. Ask: \"Which terms do you use in week one that students have never been taught?\" Avoid reading the paragraph aloud and handing this duty to a student as if it were theirs."
- statement: qaa/finance-2025/1.24.b7
  forPractitioner: { text: "When you offer placements, work experience or industry visits, consider whether every student can take them up on equal terms.", rewrite: light, force: must, status: drafted }
  forBeneficiary: { text: "not-applicable: a duty on the course", rewrite: full, force: must, status: drafted }
  author-agent-written: "Describe this as a requirement, in \"must\", on access to placements and visits. It holds at every level. Cite it as (QAA, 2025, Finance Subject Benchmark Statement, para 1.24). Do not claim that the statement requires every course to offer a placement; set it beside paragraph 1.29.b5 on equal opportunities for placements."
  author-agent-dialogue: "Raise it when a team plans placements or industry visits. Put it to the programme team as a design or review duty in their own terms. Ask: \"Which students could not take up this placement, and what would let them?\" Avoid reading the paragraph aloud and handing this duty to a student as if it were theirs."
- statement: qaa/finance-2025/1.27
  forPractitioner: { text: "Monitor and review how well your EDI policies are working in the programme, and plan improvements.", rewrite: light, force: should, status: drafted }
  forBeneficiary: { text: "not-applicable: a duty on the course", rewrite: full, force: should, status: drafted }
  author-agent-written: "Describe this as an expectation, in \"should\", on course monitoring. It holds at every level. Cite it as (QAA, 2025, Finance Subject Benchmark Statement, para 1.27). Do not claim that it sets a reporting format; set it beside paragraphs 2.27 to 2.30 on monitoring and review."
  author-agent-dialogue: "Raise it when an annual or periodic review is being prepared. Put it to the programme team as a design or review duty in their own terms. Ask: \"What evidence shows your EDI measures are working, and what would you change?\" Avoid reading the paragraph aloud and handing this duty to a student as if it were theirs."
- statement: qaa/finance-2025/1.28
  forPractitioner: { text: "Meet the regulatory requirements for accessibility as a minimum and apply them at every stage, from pre-application information to after graduation; draw on institutional guidance and support.", rewrite: light, force: should, status: drafted }
  forBeneficiary: { text: "not-applicable: a duty on the course; a student meets its effect", rewrite: full, force: should, status: drafted }
  author-agent-written: "Describe this as an expectation, in \"should\", that accessibility meets regulation as a minimum, applying at every stage. It holds at every level. Cite it as (QAA, 2025, Finance Subject Benchmark Statement, para 1.28). Do not claim that it restates the law in detail; set it beside paragraph 1.29's examples and the theme record theme:accessibility."
  author-agent-dialogue: "Raise it when a team designs or reviews a course for accessibility. Put it to the programme team as a design or review duty in their own terms. Ask: \"Where in the student journey, from applying to graduating, is access weakest?\" Avoid reading the paragraph aloud and handing this duty to a student as if it were theirs."
- statement: qaa/finance-2025/1.29.b4
  forPractitioner: { text: "Make databases, trading simulations and software accessible to all, for example by remote access or low-stimulation spaces, and weigh accessibility when you choose them.", rewrite: light, force: should, status: drafted }
  forBeneficiary: { text: "not-applicable: a duty on the course and its resources", rewrite: full, force: should, status: drafted }
  author-agent-written: "Describe this as an expectation, in \"should\", on accessible data and software resources. It holds at every level. Cite it as (QAA, 2025, Finance Subject Benchmark Statement, para 1.29). Do not claim that it names products or standards; set it beside threshold item 4.4.b8 (statistical analysis with software) and 1.24.b3."
  author-agent-dialogue: "Raise it when a team buys or renews data terminals, simulations or software. Put it to the programme team as a design or review duty in their own terms. Ask: \"Can a student who cannot reach the trading room use these tools?\" Avoid reading the paragraph aloud and handing this duty to a student as if it were theirs."
- statement: qaa/finance-2025/1.29.b5
  forPractitioner: { text: "Open placements, internships, international and extracurricular opportunities to every student on equal terms.", rewrite: light, force: should, status: drafted }
  forBeneficiary: { text: "not-applicable: a duty on the course", rewrite: full, force: should, status: drafted }
  author-agent-written: "Describe this as an expectation, in \"should\", that wider opportunities are open to all. It holds at every level. Cite it as (QAA, 2025, Finance Subject Benchmark Statement, para 1.29). Do not claim that every course must offer each opportunity named; set it beside item 1.24.b7."
  author-agent-dialogue: "Raise it when a team reviews who takes up placements or study abroad. Put it to the programme team as a design or review duty in their own terms. Ask: \"Which groups take up these opportunities least, and why?\" Avoid reading the paragraph aloud and handing this duty to a student as if it were theirs."
- statement: qaa/finance-2025/1.29.b7
  forPractitioner: { text: "Identify barriers such as caring responsibilities and digital poverty and take what steps you can to reduce their effect on learning.", rewrite: light, force: should, status: drafted }
  forBeneficiary: { text: "not-applicable: a duty on the course", rewrite: full, force: should, status: drafted }
  author-agent-written: "Describe this as an expectation, in \"should\", on reducing barriers to attendance and achievement. It holds at every level. Cite it as (QAA, 2025, Finance Subject Benchmark Statement, para 1.29). Do not claim that it obliges any single remedy; set it beside items 1.29.b4 and 1.29.b5."
  author-agent-dialogue: "Raise it when a team looks at attendance or attainment data. Put it to the programme team as a design or review duty in their own terms. Ask: \"What stops some students from attending, and what could the course change?\" Avoid reading the paragraph aloud and handing this duty to a student as if it were theirs."
- statement: qaa/finance-2025/1.29.b8
  forPractitioner: { text: "Check each assessment for accessibility and, where needed, let students show the same outcome another way.", rewrite: light, force: should, status: drafted }
  forBeneficiary: { text: "not-applicable: a duty on assessment design", rewrite: full, force: should, status: drafted }
  author-agent-written: "Describe this as an expectation, in \"should\", on accessible assessment. It holds at every level. Cite it as (QAA, 2025, Finance Subject Benchmark Statement, para 1.29). Do not claim that alternatives change the outcome being tested; set it beside paragraph 1.23."
  author-agent-dialogue: "Raise it when an assessment is being redesigned. Put it to the programme team as a design or review duty in their own terms. Ask: \"Could this outcome be shown in another way without lowering the standard?\" Avoid reading the paragraph aloud and handing this duty to a student as if it were theirs."
- statement: qaa/finance-2025/1.29.b9
  forPractitioner: { text: "Consider universal design for learning and build assessment choice into the programme.", rewrite: light, force: should, status: drafted }
  forBeneficiary: { text: "not-applicable: a duty on course design", rewrite: full, force: should, status: drafted }
  author-agent-written: "Describe this as an expectation, in \"should\", to consider universal design and assessment choice. It holds at every level. Cite it as (QAA, 2025, Finance Subject Benchmark Statement, para 1.29). Do not claim that it requires choice in every assessment; set it beside item 1.29.b8 and item 1.29.b10."
  author-agent-dialogue: "Raise it when a programme is being designed or revalidated. Put it to the programme team as a design or review duty in their own terms. Ask: \"Where could students choose how they show an outcome?\" Avoid reading the paragraph aloud and handing this duty to a student as if it were theirs."
- statement: qaa/finance-2025/1.29.b10
  forPractitioner: { text: "Design learning, teaching and assessment in advance to include neurodivergent students and those with specific learning difficulties, rather than adjusting later.", rewrite: light, force: should, status: drafted }
  forBeneficiary: { text: "not-applicable: a duty on course design", rewrite: full, force: should, status: drafted }
  author-agent-written: "Describe this as an expectation, in \"should\", for proactive inclusive design. It holds at every level. Cite it as (QAA, 2025, Finance Subject Benchmark Statement, para 1.29). Do not claim that individual adjustments are no longer needed; set it beside item 1.24 (access for neurodivergent community members) and item 1.29.b9."
  author-agent-dialogue: "Raise it when a team designs a new module or assessment. Put it to the programme team as a design or review duty in their own terms. Ask: \"What would a neurodivergent student find hardest here, and can you remove it now?\" Avoid reading the paragraph aloud and handing this duty to a student as if it were theirs."
- statement: qaa/finance-2025/1.33
  forPractitioner: { text: "Teach sustainable financial solutions as one part of work across disciplines on climate, nature loss and inequality, and build the critical and creative skills that cross subject lines.", rewrite: light, force: should, status: drafted }
  forBeneficiary: { text: "You should see the sustainable solutions you work on in finance as one part of a wider effort across many disciplines, and build critical and creative skills that cross subject lines.", rewrite: full, force: should, status: drafted }
  author-agent-written: "Describe this as an expectation, in \"should\", about how students frame sustainable financial solutions. Read it at the award the student is taking; it names no level. Cite it as (QAA, 2025, Finance Subject Benchmark Statement, para 1.33). Do not claim that it requires an interdisciplinary module; set it beside threshold item 4.4.b11, item 3.2.b12 and the theme record theme:esd."
  author-agent-dialogue: "Raise it when a student works on a sustainability problem in finance. Put it to a student in plain words and the second person; to staff, frame it as what the course lets every graduate show. Ask: \"Which other discipline would you need to talk to for this problem to be solved well?\" Avoid reading the text aloud and presenting it as an assessed rung."
- statement: qaa/finance-2025/1.34
  forPractitioner: { text: "Develop capacities and competencies that put sustainable decision making and disclosure first, using the ESD guidance's competencies as a reference.", rewrite: light, force: should, status: drafted }
  forBeneficiary: { text: "not-applicable: a duty on course design; the student-facing outcome is 4.4.b11", rewrite: full, force: should, status: drafted }
  author-agent-written: "Describe this as an expectation, in \"should\", on course design for sustainability. It holds for bachelor's and master's degrees. Cite it as (QAA, 2025, Finance Subject Benchmark Statement, para 1.34). Do not claim that the ESD guidance is mandatory; set it beside the ESD guidance std:doc:qaa-advancehe-esd-2021-guidance and threshold item 4.4.b11."
  author-agent-dialogue: "Raise it when a team maps its programme to sustainability or the ESD guidance. Put it to the programme team as a design or review duty in their own terms. Ask: \"Where does a student make a sustainable decision or disclosure judgement in your programme?\" Avoid reading the paragraph aloud and handing this duty to a student as if it were theirs."
- statement: qaa/finance-2025/1.41
  forPractitioner: { text: "Graduates should appreciate where their skills are used, including sustainability, climate finance and biodiversity finance; build this into enterprise education.", rewrite: light, force: should, status: drafted }
  forBeneficiary: { text: "You should come to appreciate the wider setting for your finance skills, including sustainability, climate finance and finance for nature and biodiversity.", rewrite: full, force: should, status: drafted }
  author-agent-written: "Describe this as an expectation, in \"should\", that graduates appreciate the wider context of their skills. Read it at the award the student is taking. Cite it as (QAA, 2025, Finance Subject Benchmark Statement, para 1.41). Do not claim that it makes entrepreneurship compulsory; set it beside threshold item 4.4.b11 and the theme records theme:enterprise and theme:esd."
  author-agent-dialogue: "Raise it when a student talks about careers or the purpose of their finance skills. Put it to a student in plain words and the second person; to staff, frame it as what the course lets every graduate show. Ask: \"Where might your finance skills add value beyond profit in a job you would like?\" Avoid presenting it as a graded outcome and lecturing on values."
- statement: qaa/finance-2025/2.2
  forPractitioner: { text: "Design objectives that integrate concept and application and let students develop critical thinking and judgement; students should be able to evaluate the ethical, sustainability and regulatory dimensions of finance, beyond pricing and functions.", rewrite: light, force: should, status: drafted }
  forBeneficiary: { text: "You should be able to judge the ethical, sustainability and regulatory side of financial activity, not only how institutions work or how products are priced, and use critical thinking on finance problems.", rewrite: full, force: should, status: drafted }
  author-agent-written: "Describe this as an expectation, in \"should\", with two parts: course design for critical thinking, and a student ability to evaluate ethical, sustainability and regulatory dimensions. Read it with the bachelor's threshold at FHEQ level 6 (FQHEIS level 10 in Scotland). Cite it as (QAA, 2025, Finance Subject Benchmark Statement, para 2.2). Do not claim that design flexibility for AI is a requirement on students; set it beside threshold items 4.4.b4 and 4.4.b10 and the level 6 descriptor qaa/fheq-2024/4.15.b7."
  author-agent-dialogue: "Raise it when a student only describes how a product works, or a team reviews learning objectives. With a student use the second person and plain words; with staff, separate the design duty from the student ability. Ask: \"Beyond how it is priced, what are the ethical and regulatory questions about this product?\" Avoid reading the paragraph aloud and turning the design duty into a student task."
- statement: qaa/finance-2025/2.3
  forPractitioner: { text: "Teach enough accounting for a reasonable command of its principles, financial reporting regulation, the content of financial statements and using accounting information for decisions; depth beyond that depends on the programme.", rewrite: light, force: must, status: drafted }
  forBeneficiary: { text: "You do not need deep accounting, but you are required to know the principles of accounting, how financial reporting is regulated, what financial statements contain and how accounting information supports decisions.", rewrite: full, force: must, status: drafted }
  author-agent-written: "Describe this as a requirement, read from \"is required\", for reasonable accounting knowledge. Read it with the bachelor's award at FHEQ level 6 (FQHEIS level 10 in Scotland). Cite it as (QAA, 2025, Finance Subject Benchmark Statement, para 2.3). Do not claim that the degree must teach accounting in depth; set it beside item 3.2.b8 on financial statements and the Accounting statement std:doc:qaa-accounting-2025-benchmarks."
  author-agent-dialogue: "Raise it when a student without an accounting background worries about the accounting content. Put it to a student in plain words and the second person; to staff, frame it as what the course lets every graduate show. Ask: \"Could you read a set of financial statements and say what they tell a decision maker?\" Avoid implying that deep accounting is required."
- statement: qaa/finance-2025/2.4
  forPractitioner: { text: "Design the programme to prepare students for self-directed, lifelong learning and for careers across public, private and third sectors, enterprise or further study.", rewrite: light, force: should, status: drafted }
  forBeneficiary: { text: "not-applicable: a duty on course design", rewrite: full, force: should, status: drafted }
  author-agent-written: "Describe this as an expectation, in \"should\", on course design for lifelong learning and careers. Read it for bachelor's and master's courses. Cite it as (QAA, 2025, Finance Subject Benchmark Statement, para 2.4). Do not claim that it guarantees employment; set it beside the level 6 descriptor qaa/fheq-2024/4.15.b9.3 and the theme record theme:enterprise."
  author-agent-dialogue: "Raise it when a team reviews employability or independent learning in its programme. Put it to the programme team as a design or review duty in their own terms. Ask: \"Where does the programme hand responsibility for learning to the student?\" Avoid reading the paragraph aloud and handing this duty to a student as if it were theirs."
- statement: qaa/finance-2025/2.11
  forPractitioner: { text: "Make sure joint and combined students will achieve the core specific and generic skills, then add the other subject's skills and room for interdisciplinary work.", rewrite: light, force: will, status: drafted }
  forBeneficiary: { text: "If you study finance as part of a joint degree, you will gain its core subject and general skills, add skills from your other subject and can explore where the two meet.", rewrite: full, force: will, status: drafted }
  author-agent-written: "Describe this as an expected outcome, in \"will\", for joint and combined degree students. Place it at FHEQ level 6 (FQHEIS level 10 in Scotland), for the bachelor's degree with honours. Cite it as (QAA, 2025, Finance Subject Benchmark Statement, para 2.11). Do not claim that joint students must meet every item a single honours student does; set it beside paragraph 1.4, item 2.3 and the threshold list 4.4.b1 to 4.4.b15."
  author-agent-dialogue: "Raise it when a joint honours student asks how much finance they must master. Put it to a student in plain words and the second person; to staff, frame it as what the course lets every graduate show. Ask: \"Which core finance skills do you already use in your other subject?\" Avoid presenting the full single honours list as their minimum."
- statement: qaa/finance-2025/2.14
  forPractitioner: { text: "Plan the master's around about 180 credits with a self-directed project or dissertation that ideally should include empirical work; live briefs, internships or extra taught units are accepted variants.", rewrite: light, force: should, status: drafted }
  forBeneficiary: { text: "On a full master's you will usually finish with your own project or dissertation, ideally one that should include empirical work you carry out yourself.", rewrite: full, force: should, status: drafted }
  author-agent-written: "Describe this as an expectation, softened by \"ideally should\", that the master's dissertation includes empirical work. Place it at FHEQ level 7 (FQHEIS level 11 in Scotland). Cite it as (QAA, 2025, Finance Subject Benchmark Statement, para 2.14). Do not claim that a dissertation is compulsory, since the text accepts taught alternatives; set it beside the master's descriptor qaa/fheq-2024/4.17.b2 and the FHEQ credit table in std:doc:qaa-fheq-2024-framework, S5."
  author-agent-dialogue: "Raise it when a master's student plans a dissertation or a team designs the project stage. With a student use the second person and plain words; with staff, name the accepted alternatives. Ask: \"What data will your project use, and how will you collect or obtain it?\" Avoid presenting empirical work as an absolute rule."
- statement: qaa/finance-2025/2.17
  forPractitioner: { text: "Treat research as a central part of master's teaching, since some students will continue to doctoral study.", rewrite: light, force: should, status: drafted }
  forBeneficiary: { text: "not-applicable: a duty on how the course is taught", rewrite: full, force: should, status: drafted }
  author-agent-written: "Describe this as an expectation, in \"should\", that master's teaching keeps research in view. Place it at FHEQ level 7 (FQHEIS level 11 in Scotland). Cite it as (QAA, 2025, Finance Subject Benchmark Statement, para 2.17). Do not claim that every master's student must do original research; set it beside item 2.14 and the master's descriptor qaa/fheq-2024/4.17.b3."
  author-agent-dialogue: "Raise it when a team designs a master's curriculum. Put it to the programme team as a design or review duty in their own terms. Ask: \"Where do your master's students meet research methods before the dissertation?\" Avoid reading the paragraph aloud and handing this duty to a student as if it were theirs."
- statement: qaa/finance-2025/2.20
  forPractitioner: { text: "Offer the degree in a variety of learning modes, with assessment suited to students' needs, and consider credit routes such as micro-credentials and recognition of prior learning.", rewrite: light, force: should, status: drafted }
  forBeneficiary: { text: "not-applicable: a duty on how the course is offered", rewrite: full, force: should, status: drafted }
  author-agent-written: "Describe this as an expectation, in \"should\", on modes of study and assessment. It holds at every level. Cite it as (QAA, 2025, Finance Subject Benchmark Statement, para 2.20). Do not claim that every mode listed must be offered; set it beside item 2.21 and paragraph 1.23."
  author-agent-dialogue: "Raise it when a team considers part-time, online or block delivery. Put it to the programme team as a design or review duty in their own terms. Ask: \"Which students can your current mode of delivery not reach?\" Avoid reading the paragraph aloud and handing this duty to a student as if it were theirs."
- statement: qaa/finance-2025/2.21
  forPractitioner: { text: "However flexible the structure, keep the programme coherent and meeting this statement's standards; flexibility may also be how you meet EDI obligations.", rewrite: light, force: must, status: drafted }
  forBeneficiary: { text: "not-applicable: a duty on course design", rewrite: full, force: must, status: drafted }
  author-agent-written: "Describe this as a requirement read from \"it is essential\", that flexible programmes stay coherent and meet the statement. It holds at every level. Cite it as (QAA, 2025, Finance Subject Benchmark Statement, para 2.21). Do not claim that the issuer used \"must\": the force is our reading (Part E); set it beside item 2.20 and the threshold list 4.4.b1 to 4.4.b15."
  author-agent-dialogue: "Raise it when a team adds flexible routes, credit transfer or micro-credentials. Put it to the programme team as a design or review duty in their own terms. Ask: \"Does a student on the most flexible route still meet every threshold item?\" Avoid reading the paragraph aloud and handing this duty to a student as if it were theirs."
- statement: qaa/finance-2025/3.2.b1
  forPractitioner: { text: "Graduates are generally expected to know the economic, legal, regulatory, social and tax settings of finance and the institutional framework of markets and firms.", rewrite: light, force: must, status: drafted }
  forBeneficiary: { text: "You are expected to understand the settings finance works in, from law and regulation to tax, and how they shape markets and institutions.", rewrite: full, force: must, status: drafted }
  author-agent-written: "Describe this as an outcome the statement generally expects of a bachelor's Finance graduate (the contexts finance operates in), listed outside the rungs. Place it at FHEQ level 6 (FQHEIS level 10 in Scotland), for the bachelor's degree with honours. Cite it as (QAA, 2025, Finance Subject Benchmark Statement, para 3.2). Do not claim that it is a threshold the award requires, or that its examples in brackets are a set syllabus; set it beside threshold item 4.4.b3 and the level 6 descriptor qaa/fheq-2024/4.15.b1."
  author-agent-dialogue: "Raise it when a student or team asks what a Finance graduate should know about the contexts finance operates in. Put it to a student in plain words and the second person; to staff, frame it as what the course lets every graduate show. Ask: \"Which rule or institution most shapes the market you know best?\" Avoid reciting the examples and treating the item as a rung."
- statement: qaa/finance-2025/3.2.b2
  forPractitioner: { text: "Graduates are generally expected to know the main theories and tools of finance and how to apply them to theoretical and practical problems.", rewrite: light, force: must, status: drafted }
  forBeneficiary: { text: "You are expected to know the main theories and tools of finance, such as portfolio theory and asset pricing, and how to use them on real problems.", rewrite: full, force: must, status: drafted }
  author-agent-written: "Describe this as an outcome the statement generally expects of a bachelor's Finance graduate (major theories and tools of finance), listed outside the rungs. Place it at FHEQ level 6 (FQHEIS level 10 in Scotland), for the bachelor's degree with honours. Cite it as (QAA, 2025, Finance Subject Benchmark Statement, para 3.2). Do not claim that it is a threshold the award requires, or that its examples in brackets are a set syllabus; set it beside threshold item 4.4.b1 and the level 6 descriptor qaa/fheq-2024/4.15.b1."
  author-agent-dialogue: "Raise it when a student or team asks what a Finance graduate should know about major theories and tools of finance. Put it to a student in plain words and the second person; to staff, frame it as what the course lets every graduate show. Ask: \"Pick one theory you have studied: what real problem does it help you solve?\" Avoid reciting the examples and treating the item as a rung."
- statement: qaa/finance-2025/3.2.b3
  forPractitioner: { text: "Graduates are generally expected to relate finance theory to empirical tests and to appraise the evidence in at least one major area, aware of its limits.", rewrite: light, force: must, status: drafted }
  forBeneficiary: { text: "You are expected to understand how finance theories are tested against data, and to weigh up the evidence in at least one area while seeing its limits.", rewrite: full, force: must, status: drafted }
  author-agent-written: "Describe this as an outcome the statement generally expects of a bachelor's Finance graduate (theory and empirical testing), listed outside the rungs. Place it at FHEQ level 6 (FQHEIS level 10 in Scotland), for the bachelor's degree with honours. Cite it as (QAA, 2025, Finance Subject Benchmark Statement, para 3.2). Do not claim that it is a threshold the award requires, or that its examples in brackets are a set syllabus; set it beside threshold item 4.4.b9 and the level 6 descriptor qaa/fheq-2024/4.15.b4."
  author-agent-dialogue: "Raise it when a student or team asks what a Finance graduate should know about theory and empirical testing. Put it to a student in plain words and the second person; to staff, frame it as what the course lets every graduate show. Ask: \"In one area, what does the evidence support, and where does it fall short?\" Avoid reciting the examples and treating the item as a rung."
- statement: qaa/finance-2025/3.2.b4
  forPractitioner: { text: "Graduates are generally expected to interpret and analyse financial data with spreadsheets and statistical software, and to critique the results and their assumptions.", rewrite: light, force: must, status: drafted }
  forBeneficiary: { text: "You are expected to read and analyse financial data with spreadsheets or statistical software, and to question your results and the assumptions behind them.", rewrite: full, force: must, status: drafted }
  author-agent-written: "Describe this as an outcome the statement generally expects of a bachelor's Finance graduate (interpreting financial data), listed outside the rungs. Place it at FHEQ level 6 (FQHEIS level 10 in Scotland), for the bachelor's degree with honours. Cite it as (QAA, 2025, Finance Subject Benchmark Statement, para 3.2). Do not claim that it is a threshold the award requires, or that its examples in brackets are a set syllabus; set it beside threshold item 4.4.b8 and the level 6 descriptor qaa/fheq-2024/4.15.b2."
  author-agent-dialogue: "Raise it when a student or team asks what a Finance graduate should know about interpreting financial data. Put it to a student in plain words and the second person; to staff, frame it as what the course lets every graduate show. Ask: \"What assumption behind your last analysis would most change the result if it were wrong?\" Avoid reciting the examples and treating the item as a rung."
- statement: qaa/finance-2025/3.2.b5
  forPractitioner: { text: "Graduates are generally expected to understand financing and governance structures and to judge their effectiveness using theory and evidence.", rewrite: light, force: must, status: drafted }
  forBeneficiary: { text: "You are expected to understand how organisations raise money and are governed, and to judge how well those arrangements work.", rewrite: full, force: must, status: drafted }
  author-agent-written: "Describe this as an outcome the statement generally expects of a bachelor's Finance graduate (financing arrangements and governance), listed outside the rungs. Place it at FHEQ level 6 (FQHEIS level 10 in Scotland), for the bachelor's degree with honours. Cite it as (QAA, 2025, Finance Subject Benchmark Statement, para 3.2). Do not claim that it is a threshold the award requires, or that its examples in brackets are a set syllabus; set it beside threshold item 4.4.b4 and the level 6 descriptor qaa/fheq-2024/4.15.b1."
  author-agent-dialogue: "Raise it when a student or team asks what a Finance graduate should know about financing arrangements and governance. Put it to a student in plain words and the second person; to staff, frame it as what the course lets every graduate show. Ask: \"How would you judge whether a firm's capital structure serves it well?\" Avoid reciting the examples and treating the item as a rung."
- statement: qaa/finance-2025/3.2.b6
  forPractitioner: { text: "Graduates are generally expected to understand what drives the financial and investment behaviour of individuals and their options.", rewrite: light, force: must, status: drafted }
  forBeneficiary: { text: "You are expected to understand what shapes how people save, invest and manage money, from risk attitudes to pensions and tax.", rewrite: full, force: must, status: drafted }
  author-agent-written: "Describe this as an outcome the statement generally expects of a bachelor's Finance graduate (personal financial management and investment), listed outside the rungs. Place it at FHEQ level 6 (FQHEIS level 10 in Scotland), for the bachelor's degree with honours. Cite it as (QAA, 2025, Finance Subject Benchmark Statement, para 3.2). Do not claim that it is a threshold the award requires, or that its examples in brackets are a set syllabus; set it beside threshold item 4.4.b6 and the level 6 descriptor qaa/fheq-2024/4.15.b1."
  author-agent-dialogue: "Raise it when a student or team asks what a Finance graduate should know about personal financial management and investment. Put it to a student in plain words and the second person; to staff, frame it as what the course lets every graduate show. Ask: \"What would you tell a friend about the trade-off between risk and return in their savings?\" Avoid reciting the examples and treating the item as a rung."
- statement: qaa/finance-2025/3.2.b7
  forPractitioner: { text: "Graduates are generally expected to understand financial services and their change over time, using theory and evidence to explain them.", rewrite: light, force: must, status: drafted }
  forBeneficiary: { text: "You are expected to understand how financial services such as banking, insurance and pensions work and change, and how theory helps explain them.", rewrite: full, force: must, status: drafted }
  author-agent-written: "Describe this as an outcome the statement generally expects of a bachelor's Finance graduate (financial services in the economy), listed outside the rungs. Place it at FHEQ level 6 (FQHEIS level 10 in Scotland), for the bachelor's degree with honours. Cite it as (QAA, 2025, Finance Subject Benchmark Statement, para 3.2). Do not claim that it is a threshold the award requires, or that its examples in brackets are a set syllabus; set it beside threshold item 4.4.b5 and the level 6 descriptor qaa/fheq-2024/4.15.b1."
  author-agent-dialogue: "Raise it when a student or team asks what a Finance graduate should know about financial services in the economy. Put it to a student in plain words and the second person; to staff, frame it as what the course lets every graduate show. Ask: \"Which idea, such as moral hazard, best explains a problem in a financial service you use?\" Avoid reciting the examples and treating the item as a rung."
- statement: qaa/finance-2025/3.2.b8
  forPractitioner: { text: "Graduates are generally expected to read financial statements and to recognise the limits of reporting and disclosure.", rewrite: light, force: must, status: drafted }
  forBeneficiary: { text: "You are expected to read financial statements and see where reporting and disclosure can mislead or leave gaps.", rewrite: full, force: must, status: drafted }
  author-agent-written: "Describe this as an outcome the statement generally expects of a bachelor's Finance graduate (financial statements and reporting limits), listed outside the rungs. Place it at FHEQ level 6 (FQHEIS level 10 in Scotland), for the bachelor's degree with honours. Cite it as (QAA, 2025, Finance Subject Benchmark Statement, para 3.2). Do not claim that it is a threshold the award requires, or that its examples in brackets are a set syllabus; set it beside threshold item 4.4.b7 and the level 6 descriptor qaa/fheq-2024/4.15.b2."
  author-agent-dialogue: "Raise it when a student or team asks what a Finance graduate should know about financial statements and reporting limits. Put it to a student in plain words and the second person; to staff, frame it as what the course lets every graduate show. Ask: \"What can a set of accounts not tell you about a company?\" Avoid reciting the examples and treating the item as a rung."
- statement: qaa/finance-2025/3.2.b9
  forPractitioner: { text: "Graduates are generally expected to understand the reasons for, reach and effect of financial regulation and its implications for professional practice.", rewrite: light, force: must, status: drafted }
  forBeneficiary: { text: "You are expected to understand why finance is regulated, what rules firms and markets face and what that means for how you work as a professional.", rewrite: full, force: must, status: drafted }
  author-agent-written: "Describe this as an outcome the statement generally expects of a bachelor's Finance graduate (regulation in the finance sector), listed outside the rungs. Place it at FHEQ level 6 (FQHEIS level 10 in Scotland), for the bachelor's degree with honours. Cite it as (QAA, 2025, Finance Subject Benchmark Statement, para 3.2). Do not claim that it is a threshold the award requires, or that its examples in brackets are a set syllabus; set it beside threshold item 4.4.b5 and the level 6 descriptor qaa/fheq-2024/4.15.b1."
  author-agent-dialogue: "Raise it when a student or team asks what a Finance graduate should know about regulation in the finance sector. Put it to a student in plain words and the second person; to staff, frame it as what the course lets every graduate show. Ask: \"Why does this part of finance need regulating, and what would happen without it?\" Avoid reciting the examples and treating the item as a rung."
- statement: qaa/finance-2025/3.2.b10
  forPractitioner: { text: "Graduates are generally expected to assess the role of digital technology, AI and GenAI in financial services, markets and investment.", rewrite: light, force: must, status: drafted }
  forBeneficiary: { text: "You are expected to judge how digital technology, AI and generative AI are changing financial services, markets and investment.", rewrite: full, force: must, status: drafted }
  author-agent-written: "Describe this as an outcome the statement generally expects of a bachelor's Finance graduate (technology, AI and GenAI in finance), listed outside the rungs. Place it at FHEQ level 6 (FQHEIS level 10 in Scotland), for the bachelor's degree with honours. Cite it as (QAA, 2025, Finance Subject Benchmark Statement, para 3.2). Do not claim that it is a threshold the award requires, or that its examples in brackets are a set syllabus; set it beside threshold item 4.4.b12 and the level 6 descriptor qaa/fheq-2024/4.15.b7."
  author-agent-dialogue: "Raise it when a student or team asks what a Finance graduate should know about technology, AI and GenAI in finance. Put it to a student in plain words and the second person; to staff, frame it as what the course lets every graduate show. Ask: \"Where has AI improved a financial service, and where has it added a new risk?\" Avoid reciting the examples and treating the item as a rung."
- statement: qaa/finance-2025/3.2.b11
  forPractitioner: { text: "Graduates are generally expected to understand personal finance and financial capability and to value wider access to finance.", rewrite: light, force: must, status: drafted }
  forBeneficiary: { text: "You are expected to understand personal finance, how people become financially capable, and why wider access to finance matters.", rewrite: full, force: must, status: drafted }
  author-agent-written: "Describe this as an outcome the statement generally expects of a bachelor's Finance graduate (personal finance and financial literacy), listed outside the rungs. Place it at FHEQ level 6 (FQHEIS level 10 in Scotland), for the bachelor's degree with honours. Cite it as (QAA, 2025, Finance Subject Benchmark Statement, para 3.2). Do not claim that it is a threshold the award requires, or that its examples in brackets are a set syllabus; set it beside threshold item 4.4.b2 and the level 6 descriptor qaa/fheq-2024/4.15.b1."
  author-agent-dialogue: "Raise it when a student or team asks what a Finance graduate should know about personal finance and financial literacy. Put it to a student in plain words and the second person; to staff, frame it as what the course lets every graduate show. Ask: \"Who lacks access to mainstream finance in your area, and what fills the gap?\" Avoid reciting the examples and treating the item as a rung."
- statement: qaa/finance-2025/3.2.b12
  forPractitioner: { text: "Graduates are generally expected to understand finance's role in climate and environmental risk and the growth of green and sustainable finance.", rewrite: light, force: must, status: drafted }
  forBeneficiary: { text: "You are expected to understand how finance responds to climate change and environmental risk, and how green and sustainable finance products work.", rewrite: full, force: must, status: drafted }
  author-agent-written: "Describe this as an outcome the statement generally expects of a bachelor's Finance graduate (finance and climate and environmental risk), listed outside the rungs. Place it at FHEQ level 6 (FQHEIS level 10 in Scotland), for the bachelor's degree with honours. Cite it as (QAA, 2025, Finance Subject Benchmark Statement, para 3.2). Do not claim that it is a threshold the award requires, or that its examples in brackets are a set syllabus; set it beside threshold item 4.4.b11 and the level 6 descriptor qaa/fheq-2024/4.15.b1."
  author-agent-dialogue: "Raise it when a student or team asks what a Finance graduate should know about finance and climate and environmental risk. Put it to a student in plain words and the second person; to staff, frame it as what the course lets every graduate show. Ask: \"How would climate risk change the value of an asset you have studied?\" Avoid reciting the examples and treating the item as a rung."
- statement: qaa/finance-2025/3.2.b13
  forPractitioner: { text: "Graduates are generally expected to use programming, visualisation and AI tools on real data and to choose suitable quantitative or qualitative methods.", rewrite: light, force: must, status: drafted }
  forBeneficiary: { text: "You are expected to use programming, data visualisation and AI tools on real data, and to choose the right research methods for the data you have.", rewrite: full, force: must, status: drafted }
  author-agent-written: "Describe this as an outcome the statement generally expects of a bachelor's Finance graduate (programming, data and research methods), listed outside the rungs. Place it at FHEQ level 6 (FQHEIS level 10 in Scotland), for the bachelor's degree with honours. Cite it as (QAA, 2025, Finance Subject Benchmark Statement, para 3.2). Do not claim that it is a threshold the award requires, or that its examples in brackets are a set syllabus; set it beside threshold item 4.4.b8 and the level 6 descriptor qaa/fheq-2024/4.15.b2."
  author-agent-dialogue: "Raise it when a student or team asks what a Finance graduate should know about programming, data and research methods. Put it to a student in plain words and the second person; to staff, frame it as what the course lets every graduate show. Ask: \"Which tool or language would you choose for this data, and why?\" Avoid reciting the examples and treating the item as a rung."
- statement: qaa/finance-2025/3.3.b1
  forPractitioner: { text: "Graduates are generally expected to evaluate arguments and evidence critically.", rewrite: light, force: must, status: drafted }
  forBeneficiary: { text: "You are expected to weigh up arguments and evidence critically.", rewrite: full, force: must, status: drafted }
  author-agent-written: "Describe this as a generic skill the statement generally expects of a bachelor's Finance graduate (critical evaluation), listed outside the rungs. Place it at FHEQ level 6 (FQHEIS level 10 in Scotland), for the bachelor's degree with honours. As a generic skill, it refines that level. Cite it as (QAA, 2025, Finance Subject Benchmark Statement, para 3.3). Do not claim that it is a threshold the award requires or that it is particular to finance; set it beside threshold item 4.4.b15 and the level 6 descriptor qaa/fheq-2024/4.15.b7."
  author-agent-dialogue: "Raise it when a student reflects on transferable skills or prepares for a job application. Put it to a student in plain words and the second person; to staff, frame it as what the course lets every graduate show. Ask: \"What is the weakest point in the argument you found most convincing?\" Avoid treating the skill as a rung and reading the list aloud."
- statement: qaa/finance-2025/3.3.b2
  forPractitioner: { text: "Graduates are generally expected to learn independently and manage their own learning.", rewrite: light, force: must, status: drafted }
  forBeneficiary: { text: "You are expected to learn on your own initiative and manage your own study.", rewrite: full, force: must, status: drafted }
  author-agent-written: "Describe this as a generic skill the statement generally expects of a bachelor's Finance graduate (independent learning), listed outside the rungs. Place it at FHEQ level 6 (FQHEIS level 10 in Scotland), for the bachelor's degree with honours. As a generic skill, it refines that level. Cite it as (QAA, 2025, Finance Subject Benchmark Statement, para 3.3). Do not claim that it is a threshold the award requires or that it is particular to finance; set it beside threshold item 4.4.b15 and the level 6 descriptor qaa/fheq-2024/4.15.b5."
  author-agent-dialogue: "Raise it when a student reflects on transferable skills or prepares for a job application. Put it to a student in plain words and the second person; to staff, frame it as what the course lets every graduate show. Ask: \"What have you learned recently that no one set for you?\" Avoid treating the skill as a rung and reading the list aloud."
- statement: qaa/finance-2025/3.3.b3
  forPractitioner: { text: "Graduates are generally expected to analyse and filter data and reach reasoned conclusions on structured and some unstructured problems.", rewrite: light, force: must, status: drafted }
  forBeneficiary: { text: "You are expected to analyse and sift data, whether given or gathered yourself, and reach reasoned conclusions, mostly on well-defined problems.", rewrite: full, force: must, status: drafted }
  author-agent-written: "Describe this as a generic skill the statement generally expects of a bachelor's Finance graduate (analysing data and drawing conclusions), listed outside the rungs. Place it at FHEQ level 6 (FQHEIS level 10 in Scotland), for the bachelor's degree with honours. As a generic skill, it refines that level. Cite it as (QAA, 2025, Finance Subject Benchmark Statement, para 3.3). Do not claim that it is a threshold the award requires or that it is particular to finance; set it beside threshold item 4.4.b7 and the level 6 descriptor qaa/fheq-2024/4.15.b7."
  author-agent-dialogue: "Raise it when a student reflects on transferable skills or prepares for a job application. Put it to a student in plain words and the second person; to staff, frame it as what the course lets every graduate show. Ask: \"How did you decide which data to leave out of your analysis?\" Avoid treating the skill as a rung and reading the list aloud."
- statement: qaa/finance-2025/3.3.b4
  forPractitioner: { text: "Graduates are generally expected to locate, extract, manage and analyse data from several sources, with proper referencing.", rewrite: light, force: must, status: drafted }
  forBeneficiary: { text: "You are expected to find, extract and manage data from different sources and reference them properly.", rewrite: full, force: must, status: drafted }
  author-agent-written: "Describe this as a generic skill the statement generally expects of a bachelor's Finance graduate (finding and managing data from many sources), listed outside the rungs. Place it at FHEQ level 6 (FQHEIS level 10 in Scotland), for the bachelor's degree with honours. As a generic skill, it refines that level. Cite it as (QAA, 2025, Finance Subject Benchmark Statement, para 3.3). Do not claim that it is a threshold the award requires or that it is particular to finance; set it beside threshold item 4.4.b7 and the level 6 descriptor qaa/fheq-2024/4.15.b5."
  author-agent-dialogue: "Raise it when a student reflects on transferable skills or prepares for a job application. Put it to a student in plain words and the second person; to staff, frame it as what the course lets every graduate show. Ask: \"Where did your data come from, and how would someone else find it?\" Avoid treating the skill as a rung and reading the list aloud."
- statement: qaa/finance-2025/3.3.b5
  forPractitioner: { text: "Graduates are generally expected to be numerate, processing financial data and grasping statistical and econometric concepts.", rewrite: light, force: must, status: drafted }
  forBeneficiary: { text: "You are expected to be confident with numbers, analysing financial data and understanding the statistics behind it.", rewrite: full, force: must, status: drafted }
  author-agent-written: "Describe this as a generic skill the statement generally expects of a bachelor's Finance graduate (numeracy), listed outside the rungs. Place it at FHEQ level 6 (FQHEIS level 10 in Scotland), for the bachelor's degree with honours. As a generic skill, it refines that level. Cite it as (QAA, 2025, Finance Subject Benchmark Statement, para 3.3). Do not claim that it is a threshold the award requires or that it is particular to finance; set it beside threshold item 4.4.b8 and the level 6 descriptor qaa/fheq-2024/4.15.b2."
  author-agent-dialogue: "Raise it when a student reflects on transferable skills or prepares for a job application. Put it to a student in plain words and the second person; to staff, frame it as what the course lets every graduate show. Ask: \"Which statistical idea do you use most, and could you explain it to a non-specialist?\" Avoid treating the skill as a rung and reading the list aloud."
- statement: qaa/finance-2025/3.3.b6
  forPractitioner: { text: "Graduates are generally expected to select and apply research tools to design and interpret financial, social and environmental policies.", rewrite: light, force: must, status: drafted }
  forBeneficiary: { text: "You are expected to choose and use research tools to shape and interpret policies in finance, society and the environment.", rewrite: full, force: must, status: drafted }
  author-agent-written: "Describe this as a generic skill the statement generally expects of a bachelor's Finance graduate (research tools for policy), listed outside the rungs. Place it at FHEQ level 6 (FQHEIS level 10 in Scotland), for the bachelor's degree with honours. As a generic skill, it refines that level. Cite it as (QAA, 2025, Finance Subject Benchmark Statement, para 3.3). Do not claim that it is a threshold the award requires or that it is particular to finance; set it beside threshold item 4.4.b10 and the level 6 descriptor qaa/fheq-2024/4.15.b6."
  author-agent-dialogue: "Raise it when a student reflects on transferable skills or prepares for a job application. Put it to a student in plain words and the second person; to staff, frame it as what the course lets every graduate show. Ask: \"Which research tool would show whether a policy is working?\" Avoid treating the skill as a rung and reading the list aloud."
- statement: qaa/finance-2025/3.3.b7
  forPractitioner: { text: "Graduates are generally expected to use technology to acquire, analyse and communicate financial information.", rewrite: light, force: must, status: drafted }
  forBeneficiary: { text: "You are expected to use technology to gather, analyse and share financial information.", rewrite: full, force: must, status: drafted }
  author-agent-written: "Describe this as a generic skill the statement generally expects of a bachelor's Finance graduate (technology for financial information), listed outside the rungs. Place it at FHEQ level 6 (FQHEIS level 10 in Scotland), for the bachelor's degree with honours. As a generic skill, it refines that level. Cite it as (QAA, 2025, Finance Subject Benchmark Statement, para 3.3). Do not claim that it is a threshold the award requires or that it is particular to finance; set it beside threshold item 4.4.b8 and the level 6 descriptor qaa/fheq-2024/4.15.b2."
  author-agent-dialogue: "Raise it when a student reflects on transferable skills or prepares for a job application. Put it to a student in plain words and the second person; to staff, frame it as what the course lets every graduate show. Ask: \"Which software do you rely on most, and what does it not do well?\" Avoid treating the skill as a rung and reading the list aloud."
- statement: qaa/finance-2025/3.3.b8
  forPractitioner: { text: "Graduates are generally expected to communicate numerical and qualitative analysis and argument in forms that suit the audience.", rewrite: light, force: must, status: drafted }
  forBeneficiary: { text: "You are expected to present numbers and ideas, with your analysis and argument, in a way that suits your audience, in speech and in writing.", rewrite: full, force: must, status: drafted }
  author-agent-written: "Describe this as a generic skill the statement generally expects of a bachelor's Finance graduate (communication to an audience), listed outside the rungs. Place it at FHEQ level 6 (FQHEIS level 10 in Scotland), for the bachelor's degree with honours. As a generic skill, it refines that level. Cite it as (QAA, 2025, Finance Subject Benchmark Statement, para 3.3). Do not claim that it is a threshold the award requires or that it is particular to finance; set it beside threshold item 4.4.b13 and the level 6 descriptor qaa/fheq-2024/4.15.b8."
  author-agent-dialogue: "Raise it when a student reflects on transferable skills or prepares for a job application. Put it to a student in plain words and the second person; to staff, frame it as what the course lets every graduate show. Ask: \"Who was the audience for your last presentation, and what did you change for them?\" Avoid treating the skill as a rung and reading the list aloud."
- statement: qaa/finance-2025/3.3.b9
  forPractitioner: { text: "Graduates are generally expected to work well with others, for example in group projects.", rewrite: light, force: must, status: drafted }
  forBeneficiary: { text: "You are expected to work well with others, for example on group projects.", rewrite: full, force: must, status: drafted }
  author-agent-written: "Describe this as a generic skill the statement generally expects of a bachelor's Finance graduate (working with others), listed outside the rungs. Place it at FHEQ level 6 (FQHEIS level 10 in Scotland), for the bachelor's degree with honours. As a generic skill, it refines that level. Cite it as (QAA, 2025, Finance Subject Benchmark Statement, para 3.3). Do not claim that it is a threshold the award requires or that it is particular to finance; set it beside threshold item 4.4.b14 and the level 6 descriptor qaa/fheq-2024/4.15.b9.1."
  author-agent-dialogue: "Raise it when a student reflects on transferable skills or prepares for a job application. Put it to a student in plain words and the second person; to staff, frame it as what the course lets every graduate show. Ask: \"What did you contribute to your last group project, and what would you do differently?\" Avoid treating the skill as a rung and reading the list aloud."
- statement: qaa/finance-2025/3.4
  forPractitioner: { text: "Choose your own mix of teaching, learning and assessment, and be ready to show how it enables students to reach the outcomes in 3.2 and 3.3.", rewrite: light, force: will, status: drafted }
  forBeneficiary: { text: "not-applicable: a duty on the provider", rewrite: full, force: will, status: drafted }
  author-agent-written: "Describe this as a provider responsibility, with the expectation in \"will\" that it can show its activities work. It holds at every level. Cite it as (QAA, 2025, Finance Subject Benchmark Statement, para 3.4). Do not claim that the statement prescribes methods; set it beside the outcome lists 3.2.b1 to 3.2.b13 and 3.3.b1 to 3.3.b9."
  author-agent-dialogue: "Raise it when a team prepares a programme specification or review. Put it to the programme team as a design or review duty in their own terms. Ask: \"For each outcome in 3.2 and 3.3, which activity lets students reach it?\" Avoid reading the paragraph aloud and handing this duty to a student as if it were theirs."
- statement: qaa/finance-2025/3.7
  forPractitioner: { text: "If you use blended learning, keep students engaged and make sure the approach maintains academic integrity, designing technology-supported assessment with integrity in mind.", rewrite: light, force: must, status: drafted }
  forBeneficiary: { text: "not-applicable: a duty on course delivery", rewrite: full, force: must, status: drafted }
  author-agent-written: "Describe this as a requirement, in \"must\", that blended learning maintains academic integrity. It holds at every level. Cite it as (QAA, 2025, Finance Subject Benchmark Statement, para 3.7). Do not claim that blended learning is required; set it beside paragraphs 1.46 and 1.47 on AI and integrity."
  author-agent-dialogue: "Raise it when a team moves teaching or assessment online. Put it to the programme team as a design or review duty in their own terms. Ask: \"How will you know the work submitted online is the student's own?\" Avoid reading the paragraph aloud and handing this duty to a student as if it were theirs."
- statement: qaa/finance-2025/3.8
  forPractitioner: { text: "Consider targeted support in subject-specific language, mathematics where relevant, academic writing and study and examination skills for a diverse cohort.", rewrite: light, force: should, status: drafted }
  forBeneficiary: { text: "not-applicable: a duty on programme leaders; a student meets its effect as support", rewrite: full, force: should, status: drafted }
  author-agent-written: "Describe this as an expectation, in \"should\", on programme leaders to consider academic support. It holds for bachelor's and master's taught programmes. Cite it as (QAA, 2025, Finance Subject Benchmark Statement, para 3.8). Do not claim that a particular support service is required; set it beside item 1.24.b3 on the language of finance."
  author-agent-dialogue: "Raise it when a team sees students struggling with maths, writing or finance terms. Put it to the programme team as a design or review duty in their own terms. Ask: \"Which support could you build into the modules rather than leave to a central service?\" Avoid reading the paragraph aloud and handing this duty to a student as if it were theirs."
- statement: qaa/finance-2025/3.14
  forPractitioner: { text: "Review teaching, learning and assessment regularly so that it stays fit for purpose and current, drawing on pedagogical research and new technology.", rewrite: light, force: must, status: drafted }
  forBeneficiary: { text: "not-applicable: a duty on the course", rewrite: full, force: must, status: drafted }
  author-agent-written: "Describe this as a requirement, in \"must\", for regular review of activities. It holds at every level. Cite it as (QAA, 2025, Finance Subject Benchmark Statement, para 3.14). Do not claim that it sets a review cycle; set it beside paragraphs 2.27 to 2.29 on monitoring, review and external examining."
  author-agent-dialogue: "Raise it when a periodic review or module evaluation is due. Put it to the programme team as a design or review duty in their own terms. Ask: \"When did you last change an activity because evidence showed it was not working?\" Avoid reading the paragraph aloud and handing this duty to a student as if it were theirs."
- statement: qaa/finance-2025/4.2
  forPractitioner: { text: "Decide what evidence shows achievement at each level and use Annex D, the degree classification descriptions, as your guide.", rewrite: light, force: should, status: drafted }
  forBeneficiary: { text: "not-applicable: a duty on the provider in judging achievement", rewrite: full, force: should, status: drafted }
  author-agent-written: "Describe this as an expectation, in \"should\", that providers refer to Annex D when judging evidence of achievement. Place it at FHEQ level 6 (FQHEIS level 10 in Scotland), for the bachelor's degree with honours. Cite it as (QAA, 2025, Finance Subject Benchmark Statement, para 4.2). Do not claim that Annex D bands map one to one onto threshold, typical and excellent; set it beside the Annex D records qaa/fheq-2024/annex-d/summary/r1/3rd to qaa/fheq-2024/annex-d/summary/r1/1st and the rungs 4.4, 4.5 and 4.6."
  author-agent-dialogue: "Raise it when a team writes marking criteria or classifies degrees. Put it to the programme team as a design or review duty in their own terms. Ask: \"How do your marking criteria use Annex D, and where do they part from it?\" Avoid reading the paragraph aloud and handing this duty to a student as if it were theirs."
- statement: qaa/finance-2025/4.3
  forPractitioner: { text: "Do not treat the threshold, typical and excellent levels as competence standards; if you write competence standards under the Equality Act 2010, follow the EHRC's latest guidance.", rewrite: light, force: should, status: drafted }
  forBeneficiary: { text: "not-applicable: a duty on the provider", rewrite: full, force: should, status: drafted }
  author-agent-written: "Describe this as an expectation, in \"should\", on providers that set competence standards. It holds at every level. Cite it as (QAA, 2025, Finance Subject Benchmark Statement, para 4.3). Do not claim that the rungs are competence standards in the Equality Act's sense; set it beside the rungs 4.4 to 4.6 and SB5's record of the EHRC."
  author-agent-dialogue: "Raise it when a team writes competence standards or handles a reasonable adjustment request. Put it to the programme team as a design or review duty in their own terms. Ask: \"Which of your requirements is a true competence standard, and which is only the usual way of assessing it?\" Avoid reading the paragraph aloud and handing this duty to a student as if it were theirs."
- statement: qaa/finance-2025/4.4.b1
  forPractitioner: { text: "At threshold, graduates will show deep knowledge of finance's main concepts, theories and tools.", rewrite: light, force: threshold, status: drafted }
  forBeneficiary: { text: "To pass, you will show solid knowledge of the main ideas, theories and tools of finance.", rewrite: full, force: threshold, status: drafted }
  author-agent-written: "Describe this as a threshold outcome, the minimum the bachelor's degree with honours in Finance requires (depth of knowledge of core concepts). Place it at FHEQ level 6 (FQHEIS level 10 in Scotland), for the bachelor's degree with honours. Cite it as (QAA, 2025, Finance Subject Benchmark Statement, para 4.4). Do not claim that it is a regulatory requirement, that it describes the typical graduate, or that it holds for a master's; set it beside the typical and excellent levels 4.5 and 4.6, the level 6 descriptor qaa/fheq-2024/4.15.b1 and Annex D's third-class cell qaa/fheq-2024/annex-d/knowledge/r1/3rd."
  author-agent-dialogue: "Raise it when a student asks what they must be able to do to pass the degree, or a team checks its programme outcomes. Put it to a student in plain words and the second person; to staff, frame it as what the course lets every graduate show. Make clear this is the minimum. Ask: \"Which core idea in finance could you explain without notes?\" Avoid reading the list aloud and implying that the threshold is what most students reach."
- statement: qaa/finance-2025/4.4.b2
  forPractitioner: { text: "At threshold, graduates will apply their knowledge to finance problems facing individuals, companies, institutions and society.", rewrite: light, force: threshold, status: drafted }
  forBeneficiary: { text: "To pass, you will use what you know to tackle finance problems for people, firms, institutions and society.", rewrite: full, force: threshold, status: drafted }
  author-agent-written: "Describe this as a threshold outcome, the minimum the bachelor's degree with honours in Finance requires (applying knowledge to finance problems). Place it at FHEQ level 6 (FQHEIS level 10 in Scotland), for the bachelor's degree with honours. Cite it as (QAA, 2025, Finance Subject Benchmark Statement, para 4.4). Do not claim that it is a regulatory requirement, that it describes the typical graduate, or that it holds for a master's; set it beside the typical and excellent levels 4.5 and 4.6, the level 6 descriptor qaa/fheq-2024/4.15.b3.1 and Annex D's third-class cell qaa/fheq-2024/annex-d/cognitive/r3/3rd."
  author-agent-dialogue: "Raise it when a student asks what they must be able to do to pass the degree, or a team checks its programme outcomes. Put it to a student in plain words and the second person; to staff, frame it as what the course lets every graduate show. Make clear this is the minimum. Ask: \"What finance problem have you solved where the answer mattered to someone?\" Avoid reading the list aloud and implying that the threshold is what most students reach."
- statement: qaa/finance-2025/4.4.b3
  forPractitioner: { text: "At threshold, graduates will understand the institutional, economic, political, regulatory and social environments of finance.", rewrite: light, force: threshold, status: drafted }
  forBeneficiary: { text: "To pass, you will understand the institutions, economics, politics, regulation and society that finance works within.", rewrite: full, force: threshold, status: drafted }
  author-agent-written: "Describe this as a threshold outcome, the minimum the bachelor's degree with honours in Finance requires (the environments finance operates in). Place it at FHEQ level 6 (FQHEIS level 10 in Scotland), for the bachelor's degree with honours. Cite it as (QAA, 2025, Finance Subject Benchmark Statement, para 4.4). Do not claim that it is a regulatory requirement, that it describes the typical graduate, or that it holds for a master's; set it beside the typical and excellent levels 4.5 and 4.6, the level 6 descriptor qaa/fheq-2024/4.15.b1 and Annex D's third-class cell qaa/fheq-2024/annex-d/knowledge/r2/3rd."
  author-agent-dialogue: "Raise it when a student asks what they must be able to do to pass the degree, or a team checks its programme outcomes. Put it to a student in plain words and the second person; to staff, frame it as what the course lets every graduate show. Make clear this is the minimum. Ask: \"How does regulation change what a bank can do?\" Avoid reading the list aloud and implying that the threshold is what most students reach."
- statement: qaa/finance-2025/4.4.b4
  forPractitioner: { text: "At threshold, graduates will recognise that reliable governance and ethical considerations are fundamental to financial decisions.", rewrite: light, force: threshold, status: drafted }
  forBeneficiary: { text: "To pass, you will recognise why good governance and ethics matter in financial decisions.", rewrite: full, force: threshold, status: drafted }
  author-agent-written: "Describe this as a threshold outcome, the minimum the bachelor's degree with honours in Finance requires (governance and ethics in decisions). Place it at FHEQ level 6 (FQHEIS level 10 in Scotland), for the bachelor's degree with honours. Cite it as (QAA, 2025, Finance Subject Benchmark Statement, para 4.4). Do not claim that it is a regulatory requirement, that it describes the typical graduate, or that it holds for a master's; set it beside the typical and excellent levels 4.5 and 4.6, the level 6 descriptor qaa/fheq-2024/4.15.b7 and Annex D's third-class cell qaa/fheq-2024/annex-d/knowledge/r2/3rd."
  author-agent-dialogue: "Raise it when a student asks what they must be able to do to pass the degree, or a team checks its programme outcomes. Put it to a student in plain words and the second person; to staff, frame it as what the course lets every graduate show. Make clear this is the minimum. Ask: \"When would you refuse a profitable decision on ethical grounds?\" Avoid reading the list aloud and implying that the threshold is what most students reach."
- statement: qaa/finance-2025/4.4.b5
  forPractitioner: { text: "At threshold, graduates will understand how financial markets operate and are regulated and supervised, with some of their products.", rewrite: light, force: threshold, status: drafted }
  forBeneficiary: { text: "To pass, you will understand how financial markets work and are regulated, and some of the products traded in them.", rewrite: full, force: threshold, status: drafted }
  author-agent-written: "Describe this as a threshold outcome, the minimum the bachelor's degree with honours in Finance requires (markets, their regulation and products). Place it at FHEQ level 6 (FQHEIS level 10 in Scotland), for the bachelor's degree with honours. Cite it as (QAA, 2025, Finance Subject Benchmark Statement, para 4.4). Do not claim that it is a regulatory requirement, that it describes the typical graduate, or that it holds for a master's; set it beside the typical and excellent levels 4.5 and 4.6, the level 6 descriptor qaa/fheq-2024/4.15.b1 and Annex D's third-class cell qaa/fheq-2024/annex-d/knowledge/r1/3rd."
  author-agent-dialogue: "Raise it when a student asks what they must be able to do to pass the degree, or a team checks its programme outcomes. Put it to a student in plain words and the second person; to staff, frame it as what the course lets every graduate show. Make clear this is the minimum. Ask: \"Who supervises the market you know best, and what do they watch for?\" Avoid reading the list aloud and implying that the threshold is what most students reach."
- statement: qaa/finance-2025/4.4.b6
  forPractitioner: { text: "At threshold, graduates will understand the basics of valuation, security analysis and portfolio management.", rewrite: light, force: threshold, status: drafted }
  forBeneficiary: { text: "To pass, you will understand the basics of valuing assets, analysing securities and managing a portfolio.", rewrite: full, force: threshold, status: drafted }
  author-agent-written: "Describe this as a threshold outcome, the minimum the bachelor's degree with honours in Finance requires (valuation, securities and portfolios). Place it at FHEQ level 6 (FQHEIS level 10 in Scotland), for the bachelor's degree with honours. Cite it as (QAA, 2025, Finance Subject Benchmark Statement, para 4.4). Do not claim that it is a regulatory requirement, that it describes the typical graduate, or that it holds for a master's; set it beside the typical and excellent levels 4.5 and 4.6, the level 6 descriptor qaa/fheq-2024/4.15.b2 and Annex D's third-class cell qaa/fheq-2024/annex-d/knowledge/r2/3rd."
  author-agent-dialogue: "Raise it when a student asks what they must be able to do to pass the degree, or a team checks its programme outcomes. Put it to a student in plain words and the second person; to staff, frame it as what the course lets every graduate show. Make clear this is the minimum. Ask: \"How would you put a value on a share you have never seen before?\" Avoid reading the list aloud and implying that the threshold is what most students reach."
- statement: qaa/finance-2025/4.4.b7
  forPractitioner: { text: "At threshold, graduates will collect, manage, combine and interpret financial, accounting and economic data.", rewrite: light, force: threshold, status: drafted }
  forBeneficiary: { text: "To pass, you will gather, organise, combine and make sense of financial, accounting and economic data.", rewrite: full, force: threshold, status: drafted }
  author-agent-written: "Describe this as a threshold outcome, the minimum the bachelor's degree with honours in Finance requires (handling financial and economic data). Place it at FHEQ level 6 (FQHEIS level 10 in Scotland), for the bachelor's degree with honours. Cite it as (QAA, 2025, Finance Subject Benchmark Statement, para 4.4). Do not claim that it is a regulatory requirement, that it describes the typical graduate, or that it holds for a master's; set it beside the typical and excellent levels 4.5 and 4.6, the level 6 descriptor qaa/fheq-2024/4.15.b2 and Annex D's third-class cell qaa/fheq-2024/annex-d/practical/r4/3rd."
  author-agent-dialogue: "Raise it when a student asks what they must be able to do to pass the degree, or a team checks its programme outcomes. Put it to a student in plain words and the second person; to staff, frame it as what the course lets every graduate show. Make clear this is the minimum. Ask: \"Where would you find the data for this question, and how would you check it?\" Avoid reading the list aloud and implying that the threshold is what most students reach."
- statement: qaa/finance-2025/4.4.b8
  forPractitioner: { text: "At threshold, graduates will execute straightforward statistical analyses of financial data with software packages.", rewrite: light, force: threshold, status: drafted }
  forBeneficiary: { text: "To pass, you will run simple statistical analyses of financial data using software.", rewrite: full, force: threshold, status: drafted }
  author-agent-written: "Describe this as a threshold outcome, the minimum the bachelor's degree with honours in Finance requires (straightforward statistical analysis with software). Place it at FHEQ level 6 (FQHEIS level 10 in Scotland), for the bachelor's degree with honours. Cite it as (QAA, 2025, Finance Subject Benchmark Statement, para 4.4). Do not claim that it is a regulatory requirement, that it describes the typical graduate, or that it holds for a master's; set it beside the typical and excellent levels 4.5 and 4.6, the level 6 descriptor qaa/fheq-2024/4.15.b2 and Annex D's third-class cell qaa/fheq-2024/annex-d/practical/r2/3rd."
  author-agent-dialogue: "Raise it when a student asks what they must be able to do to pass the degree, or a team checks its programme outcomes. Put it to a student in plain words and the second person; to staff, frame it as what the course lets every graduate show. Make clear this is the minimum. Ask: \"Which analysis would you run first on this data set, and in which package?\" Avoid reading the list aloud and implying that the threshold is what most students reach."
- statement: qaa/finance-2025/4.4.b9
  forPractitioner: { text: "At threshold, graduates will assess how far finance theories and their evidence matter, and their problems and limits.", rewrite: light, force: threshold, status: drafted }
  forBeneficiary: { text: "To pass, you will judge how far finance theories and their evidence hold up, and where they fall short.", rewrite: full, force: threshold, status: drafted }
  author-agent-written: "Describe this as a threshold outcome, the minimum the bachelor's degree with honours in Finance requires (limits of theory and evidence). Place it at FHEQ level 6 (FQHEIS level 10 in Scotland), for the bachelor's degree with honours. Cite it as (QAA, 2025, Finance Subject Benchmark Statement, para 4.4). Do not claim that it is a regulatory requirement, that it describes the typical graduate, or that it holds for a master's; set it beside the typical and excellent levels 4.5 and 4.6, the level 6 descriptor qaa/fheq-2024/4.15.b4 and Annex D's third-class cell qaa/fheq-2024/annex-d/cognitive/r1/3rd."
  author-agent-dialogue: "Raise it when a student asks what they must be able to do to pass the degree, or a team checks its programme outcomes. Put it to a student in plain words and the second person; to staff, frame it as what the course lets every graduate show. Make clear this is the minimum. Ask: \"Which theory you studied does the evidence support least well?\" Avoid reading the list aloud and implying that the threshold is what most students reach."
- statement: qaa/finance-2025/4.4.b10
  forPractitioner: { text: "At threshold, graduates will critically appreciate how finance theory and empirical evidence can guide policy and practice.", rewrite: light, force: threshold, status: drafted }
  forBeneficiary: { text: "To pass, you will show you understand, critically, how finance theory and evidence can shape policy and practice.", rewrite: full, force: threshold, status: drafted }
  author-agent-written: "Describe this as a threshold outcome, the minimum the bachelor's degree with honours in Finance requires (theory and evidence guiding policy and practice). Place it at FHEQ level 6 (FQHEIS level 10 in Scotland), for the bachelor's degree with honours. Cite it as (QAA, 2025, Finance Subject Benchmark Statement, para 4.4). Do not claim that it is a regulatory requirement, that it describes the typical graduate, or that it holds for a master's; set it beside the typical and excellent levels 4.5 and 4.6, the level 6 descriptor qaa/fheq-2024/4.15.b3.2 and Annex D's third-class cell qaa/fheq-2024/annex-d/cognitive/r2/3rd."
  author-agent-dialogue: "Raise it when a student asks what they must be able to do to pass the degree, or a team checks its programme outcomes. Put it to a student in plain words and the second person; to staff, frame it as what the course lets every graduate show. Make clear this is the minimum. Ask: \"Name a policy that finance research changed, and say whether it should have.\" Avoid reading the list aloud and implying that the threshold is what most students reach."
- statement: qaa/finance-2025/4.4.b11
  forPractitioner: { text: "At threshold, graduates will understand finance as a key lever for sustainable outcomes for society and the planet.", rewrite: light, force: threshold, status: drafted }
  forBeneficiary: { text: "To pass, you will understand how finance can drive sustainable outcomes for people and the planet.", rewrite: full, force: threshold, status: drafted }
  author-agent-written: "Describe this as a threshold outcome, the minimum the bachelor's degree with honours in Finance requires (finance as a lever for sustainable outcomes). Place it at FHEQ level 6 (FQHEIS level 10 in Scotland), for the bachelor's degree with honours. Cite it as (QAA, 2025, Finance Subject Benchmark Statement, para 4.4). Do not claim that it is a regulatory requirement, that it describes the typical graduate, or that it holds for a master's; set it beside the typical and excellent levels 4.5 and 4.6, the level 6 descriptor qaa/fheq-2024/4.15.b1 and Annex D's third-class cell qaa/fheq-2024/annex-d/knowledge/r2/3rd."
  author-agent-dialogue: "Raise it when a student asks what they must be able to do to pass the degree, or a team checks its programme outcomes. Put it to a student in plain words and the second person; to staff, frame it as what the course lets every graduate show. Make clear this is the minimum. Ask: \"Where could finance do most to cut emissions or protect nature?\" Avoid reading the list aloud and implying that the threshold is what most students reach."
- statement: qaa/finance-2025/4.4.b12
  forPractitioner: { text: "At threshold, graduates will understand the impact of fintech innovations such as AI, blockchain and digital payments on financial services.", rewrite: light, force: threshold, status: drafted }
  forBeneficiary: { text: "To pass, you will understand how fintech, such as AI, blockchain and digital payments, is changing financial services.", rewrite: full, force: threshold, status: drafted }
  author-agent-written: "Describe this as a threshold outcome, the minimum the bachelor's degree with honours in Finance requires (the effect of fintech on financial services). Place it at FHEQ level 6 (FQHEIS level 10 in Scotland), for the bachelor's degree with honours. Cite it as (QAA, 2025, Finance Subject Benchmark Statement, para 4.4). Do not claim that it is a regulatory requirement, that it describes the typical graduate, or that it holds for a master's; set it beside the typical and excellent levels 4.5 and 4.6, the level 6 descriptor qaa/fheq-2024/4.15.b1 and Annex D's third-class cell qaa/fheq-2024/annex-d/knowledge/r1/3rd."
  author-agent-dialogue: "Raise it when a student asks what they must be able to do to pass the degree, or a team checks its programme outcomes. Put it to a student in plain words and the second person; to staff, frame it as what the course lets every graduate show. Make clear this is the minimum. Ask: \"Which fintech innovation has most changed how you use money?\" Avoid reading the list aloud and implying that the threshold is what most students reach."
- statement: qaa/finance-2025/4.4.b13
  forPractitioner: { text: "At threshold, graduates will distil financial information and communicate it effectively, spoken and written, to diverse audiences.", rewrite: light, force: threshold, status: drafted }
  forBeneficiary: { text: "To pass, you will boil down financial information and explain it well, in speech and writing, to different audiences.", rewrite: full, force: threshold, status: drafted }
  author-agent-written: "Describe this as a threshold outcome, the minimum the bachelor's degree with honours in Finance requires (summarising and communicating to varied audiences). Place it at FHEQ level 6 (FQHEIS level 10 in Scotland), for the bachelor's degree with honours. Cite it as (QAA, 2025, Finance Subject Benchmark Statement, para 4.4). Do not claim that it is a regulatory requirement, that it describes the typical graduate, or that it holds for a master's; set it beside the typical and excellent levels 4.5 and 4.6, the level 6 descriptor qaa/fheq-2024/4.15.b8 and Annex D's third-class cell qaa/fheq-2024/annex-d/transferable/r1/3rd."
  author-agent-dialogue: "Raise it when a student asks what they must be able to do to pass the degree, or a team checks its programme outcomes. Put it to a student in plain words and the second person; to staff, frame it as what the course lets every graduate show. Make clear this is the minimum. Ask: \"How would you explain this result to a client with no finance background?\" Avoid reading the list aloud and implying that the threshold is what most students reach."
- statement: qaa/finance-2025/4.4.b14
  forPractitioner: { text: "At threshold, graduates will show collaborative and leadership skills in finance and interdisciplinary teams.", rewrite: light, force: threshold, status: drafted }
  forBeneficiary: { text: "To pass, you will show you can work with others and lead, in finance teams and mixed-discipline teams.", rewrite: full, force: threshold, status: drafted }
  author-agent-written: "Describe this as a threshold outcome, the minimum the bachelor's degree with honours in Finance requires (collaboration and leadership in teams). Place it at FHEQ level 6 (FQHEIS level 10 in Scotland), for the bachelor's degree with honours. Cite it as (QAA, 2025, Finance Subject Benchmark Statement, para 4.4). Do not claim that it is a regulatory requirement, that it describes the typical graduate, or that it holds for a master's; set it beside the typical and excellent levels 4.5 and 4.6, the level 6 descriptor qaa/fheq-2024/4.15.b9.1 and Annex D's third-class cell qaa/fheq-2024/annex-d/transferable/r2/3rd."
  author-agent-dialogue: "Raise it when a student asks what they must be able to do to pass the degree, or a team checks its programme outcomes. Put it to a student in plain words and the second person; to staff, frame it as what the course lets every graduate show. Make clear this is the minimum. Ask: \"When did you last take the lead in a team, and what happened?\" Avoid reading the list aloud and implying that the threshold is what most students reach."
- statement: qaa/finance-2025/4.4.b15
  forPractitioner: { text: "At threshold, graduates will assert intellectual independence and critical judgement.", rewrite: light, force: threshold, status: drafted }
  forBeneficiary: { text: "To pass, you will think for yourself and judge critically.", rewrite: full, force: threshold, status: drafted }
  author-agent-written: "Describe this as a threshold outcome, the minimum the bachelor's degree with honours in Finance requires (intellectual independence and critical judgement). Place it at FHEQ level 6 (FQHEIS level 10 in Scotland), for the bachelor's degree with honours. Cite it as (QAA, 2025, Finance Subject Benchmark Statement, para 4.4). Do not claim that it is a regulatory requirement, that it describes the typical graduate, or that it holds for a master's; set it beside the typical and excellent levels 4.5 and 4.6, the level 6 descriptor qaa/fheq-2024/4.15.b7 and Annex D's third-class cell qaa/fheq-2024/annex-d/transferable/r3/3rd."
  author-agent-dialogue: "Raise it when a student asks what they must be able to do to pass the degree, or a team checks its programme outcomes. Put it to a student in plain words and the second person; to staff, frame it as what the course lets every graduate show. Make clear this is the minimum. Ask: \"Where in your work did you reach a view that differed from your sources?\" Avoid reading the list aloud and implying that the threshold is what most students reach."
- statement: qaa/finance-2025/4.5.s1
  forPractitioner: { text: "At the typical level, graduates show breadth and depth of knowledge and a clear, critical insight into the discipline, beyond the threshold.", rewrite: light, force: will, status: drafted }
  forBeneficiary: { text: "To go beyond a pass, you will show broad and deep knowledge and a clear, critical view of finance as a discipline.", rewrite: full, force: will, status: drafted }
  author-agent-written: "Describe this as a typical-level expectation, in \"will\", above the threshold (breadth, depth and critical insight). Place it at FHEQ level 6 (FQHEIS level 10 in Scotland), for the bachelor's degree with honours. Cite it as (QAA, 2025, Finance Subject Benchmark Statement, para 4.5). Do not claim that it is the minimum for the award, or that it equals an upper second; set it beside the threshold list 4.4, Annex D's upper-second cell qaa/fheq-2024/annex-d/knowledge/r1/2.1 for reading only, and qaa/fheq-2024/4.15.b1."
  author-agent-dialogue: "Raise it when a student asks how to move beyond a pass, or a team sets criteria above the threshold. Put it to a student in plain words and the second person; to staff, frame it as what the course lets every graduate show. Say it describes a higher level, not what is needed to pass. Ask: \"What do you understand about finance now that you could not have argued in your first year?\" Avoid presenting this as the minimum and reading the paragraph aloud."
- statement: qaa/finance-2025/4.5.s2
  forPractitioner: { text: "At the typical level, graduates will show rigorous understanding of finance theory and method and strong understanding of some specialist topics.", rewrite: light, force: will, status: drafted }
  forBeneficiary: { text: "To go beyond a pass, you will show a rigorous grasp of finance theory and method and know some specialist topics well.", rewrite: full, force: will, status: drafted }
  author-agent-written: "Describe this as a typical-level expectation, in \"will\", above the threshold (rigorous theory and some specialised topics). Place it at FHEQ level 6 (FQHEIS level 10 in Scotland), for the bachelor's degree with honours. Cite it as (QAA, 2025, Finance Subject Benchmark Statement, para 4.5). Do not claim that it is the minimum for the award, or that it equals an upper second; set it beside threshold item 4.4.b1, excellent 4.6.s2 and qaa/fheq-2024/annex-d/knowledge/r2/2.1."
  author-agent-dialogue: "Raise it when a student asks how to move beyond a pass, or a team sets criteria above the threshold. Put it to a student in plain words and the second person; to staff, frame it as what the course lets every graduate show. Say it describes a higher level, not what is needed to pass. Ask: \"Which specialist topic do you know well enough to teach a classmate?\" Avoid presenting this as the minimum and reading the paragraph aloud."
- statement: qaa/finance-2025/4.5.s3
  forPractitioner: { text: "At the typical level, graduates will select and critically appraise a wide range of sources, specialist or interdisciplinary, and recognise their uncertainty and limits.", rewrite: light, force: will, status: drafted }
  forBeneficiary: { text: "To go beyond a pass, you will choose and critically weigh many kinds of sources and views, and see where they are uncertain or limited.", rewrite: full, force: will, status: drafted }
  author-agent-written: "Describe this as a typical-level expectation, in \"will\", above the threshold (critical appraisal of sources and their limits). Place it at FHEQ level 6 (FQHEIS level 10 in Scotland), for the bachelor's degree with honours. Cite it as (QAA, 2025, Finance Subject Benchmark Statement, para 4.5). Do not claim that it is the minimum for the award, or that it equals an upper second; set it beside threshold item 4.4.b9, excellent 4.6.s4, qaa/fheq-2024/4.15.b4 and qaa/fheq-2024/annex-d/cognitive/r1/2.1."
  author-agent-dialogue: "Raise it when a student asks how to move beyond a pass, or a team sets criteria above the threshold. Put it to a student in plain words and the second person; to staff, frame it as what the course lets every graduate show. Say it describes a higher level, not what is needed to pass. Ask: \"Which of your sources disagree, and how did you decide between them?\" Avoid presenting this as the minimum and reading the paragraph aloud."
- statement: qaa/finance-2025/4.5.s4
  forPractitioner: { text: "At the typical level, graduates will investigate thoroughly with some autonomy and solve complex finance problems with established methods, accurately.", rewrite: light, force: will, status: drafted }
  forBeneficiary: { text: "To go beyond a pass, you will research thoroughly with some independence and solve complex finance problems using a wide range of methods accurately.", rewrite: full, force: will, status: drafted }
  author-agent-written: "Describe this as a typical-level expectation, in \"will\", above the threshold (investigation and solving complex problems). Place it at FHEQ level 6 (FQHEIS level 10 in Scotland), for the bachelor's degree with honours. Cite it as (QAA, 2025, Finance Subject Benchmark Statement, para 4.5). Do not claim that it is the minimum for the award, or that it equals an upper second; set it beside threshold item 4.4.b2, excellent 4.6.s3 and 4.6.s5, qaa/fheq-2024/4.15.b6 and qaa/fheq-2024/annex-d/cognitive/r3/2.1."
  author-agent-dialogue: "Raise it when a student asks how to move beyond a pass, or a team sets criteria above the threshold. Put it to a student in plain words and the second person; to staff, frame it as what the course lets every graduate show. Say it describes a higher level, not what is needed to pass. Ask: \"Which complex problem did you solve mostly on your own, and which method did you choose?\" Avoid presenting this as the minimum and reading the paragraph aloud."
- statement: qaa/finance-2025/4.5.s5
  forPractitioner: { text: "At the typical level, graduates will synthesise and present information and results with supported arguments, interpret complex ideas thoroughly and show creativity and originality.", rewrite: light, force: will, status: drafted }
  forBeneficiary: { text: "To go beyond a pass, you will pull information together, argue from evidence, explain complex ideas carefully and show creativity and original thought in your work.", rewrite: full, force: will, status: drafted }
  author-agent-written: "Describe this as a typical-level expectation, in \"will\", above the threshold (synthesis, argument and originality in communication). Place it at FHEQ level 6 (FQHEIS level 10 in Scotland), for the bachelor's degree with honours. Cite it as (QAA, 2025, Finance Subject Benchmark Statement, para 4.5). Do not claim that it is the minimum for the award, or that it equals an upper second; set it beside threshold item 4.4.b13, excellent 4.6.s6 and 4.6.s7, qaa/fheq-2024/4.15.b8 and qaa/fheq-2024/annex-d/cognitive/r4/2.1."
  author-agent-dialogue: "Raise it when a student asks how to move beyond a pass, or a team sets criteria above the threshold. Put it to a student in plain words and the second person; to staff, frame it as what the course lets every graduate show. Say it describes a higher level, not what is needed to pass. Ask: \"Where in your recent work did you make an argument nobody gave you?\" Avoid presenting this as the minimum and reading the paragraph aloud."
- statement: qaa/finance-2025/4.6.s1
  forPractitioner: { text: "At the excellent level, graduates show exceptional knowledge and understanding of finance, well beyond the typical level and beyond what was taught.", rewrite: light, force: will, status: drafted }
  forBeneficiary: { text: "At the highest level, you will show exceptional knowledge and understanding of finance, going well past what you were taught.", rewrite: full, force: will, status: drafted }
  author-agent-written: "Describe this as an excellent-level expectation, in \"will\", the highest level the statement describes (exceptional knowledge beyond the taught). Place it at FHEQ level 6 (FQHEIS level 10 in Scotland), for the bachelor's degree with honours. Cite it as (QAA, 2025, Finance Subject Benchmark Statement, para 4.6). Do not claim that it is the minimum for the award, or that it equals a first or a master's standard; set it beside typical 4.5.s1, qaa/fheq-2024/annex-d/knowledge/r1/1st for reading only, and the master's descriptor qaa/fheq-2024/4.17.b1."
  author-agent-dialogue: "Raise it when a student asks how to move beyond a pass, or a team sets criteria above the threshold. Put it to a student in plain words and the second person; to staff, frame it as what the course lets every graduate show. Say it describes a higher level, not what is needed to pass. Ask: \"What have you read or worked out that goes beyond your course?\" Avoid presenting this as the minimum and reading the paragraph aloud."
- statement: qaa/finance-2025/4.6.s2
  forPractitioner: { text: "At the excellent level, graduates will show exceptional command of finance theory and method and in-depth knowledge of several specialist areas.", rewrite: light, force: will, status: drafted }
  forBeneficiary: { text: "At the highest level, you will show exceptional command of finance theory and method and know several specialist areas in depth.", rewrite: full, force: will, status: drafted }
  author-agent-written: "Describe this as an excellent-level expectation, in \"will\", the highest level the statement describes (exceptional theory and in-depth specialist knowledge). Place it at FHEQ level 6 (FQHEIS level 10 in Scotland), for the bachelor's degree with honours. Cite it as (QAA, 2025, Finance Subject Benchmark Statement, para 4.6). Do not claim that it is the minimum for the award, or that it equals a first or a master's standard; set it beside typical 4.5.s2, qaa/fheq-2024/annex-d/knowledge/r2/1st and qaa/fheq-2024/4.15.b1."
  author-agent-dialogue: "Raise it when a student asks how to move beyond a pass, or a team sets criteria above the threshold. Put it to a student in plain words and the second person; to staff, frame it as what the course lets every graduate show. Say it describes a higher level, not what is needed to pass. Ask: \"In which specialist areas could you hold your own with a practitioner?\" Avoid presenting this as the minimum and reading the paragraph aloud."
- statement: qaa/finance-2025/4.6.s3
  forPractitioner: { text: "At the excellent level, graduates will work with intellectual independence and investigate thoroughly and extensively, well beyond the typical range.", rewrite: light, force: will, status: drafted }
  forBeneficiary: { text: "At the highest level, you will think independently and research thoroughly and widely, well beyond what most students do.", rewrite: full, force: will, status: drafted }
  author-agent-written: "Describe this as an excellent-level expectation, in \"will\", the highest level the statement describes (independent, extensive investigation). Place it at FHEQ level 6 (FQHEIS level 10 in Scotland), for the bachelor's degree with honours. Cite it as (QAA, 2025, Finance Subject Benchmark Statement, para 4.6). Do not claim that it is the minimum for the award, or that it equals a first or a master's standard; set it beside typical 4.5.s4, threshold item 4.4.b15 and qaa/fheq-2024/annex-d/knowledge/r3/1st."
  author-agent-dialogue: "Raise it when a student asks how to move beyond a pass, or a team sets criteria above the threshold. Put it to a student in plain words and the second person; to staff, frame it as what the course lets every graduate show. Say it describes a higher level, not what is needed to pass. Ask: \"What question did you pursue further than the assignment asked?\" Avoid presenting this as the minimum and reading the paragraph aloud."
- statement: qaa/finance-2025/4.6.s4
  forPractitioner: { text: "At the excellent level, graduates will critically appraise a wide range of sources with exceptional skill and show a masterly grasp of their uncertainty and limits.", rewrite: light, force: will, status: drafted }
  forBeneficiary: { text: "At the highest level, you will weigh up a wide range of sources with exceptional skill and show a masterly sense of what they cannot tell you.", rewrite: full, force: will, status: drafted }
  author-agent-written: "Describe this as an excellent-level expectation, in \"will\", the highest level the statement describes (exceptional critical appraisal). Place it at FHEQ level 6 (FQHEIS level 10 in Scotland), for the bachelor's degree with honours. Cite it as (QAA, 2025, Finance Subject Benchmark Statement, para 4.6). Do not claim that it is the minimum for the award, or that it equals a first or a master's standard; set it beside typical 4.5.s3, qaa/fheq-2024/annex-d/cognitive/r1/1st and qaa/fheq-2024/4.15.b4."
  author-agent-dialogue: "Raise it when a student asks how to move beyond a pass, or a team sets criteria above the threshold. Put it to a student in plain words and the second person; to staff, frame it as what the course lets every graduate show. Say it describes a higher level, not what is needed to pass. Ask: \"Where does the evidence you rely on most stop being trustworthy?\" Avoid presenting this as the minimum and reading the paragraph aloud."
- statement: qaa/finance-2025/4.6.s5
  forPractitioner: { text: "At the excellent level, graduates will solve complex finance problems exceptionally well and largely autonomously, justifying their choice and use of methods critically and accurately.", rewrite: light, force: will, status: drafted }
  forBeneficiary: { text: "At the highest level, you will solve complex finance problems exceptionally well and largely on your own, and justify the methods you chose.", rewrite: full, force: will, status: drafted }
  author-agent-written: "Describe this as an excellent-level expectation, in \"will\", the highest level the statement describes (exceptional problem-solving and decisions). Place it at FHEQ level 6 (FQHEIS level 10 in Scotland), for the bachelor's degree with honours. Cite it as (QAA, 2025, Finance Subject Benchmark Statement, para 4.6). Do not claim that it is the minimum for the award, or that it equals a first or a master's standard; set it beside typical 4.5.s4, threshold item 4.4.b2, qaa/fheq-2024/annex-d/cognitive/r3/1st and the master's descriptor qaa/fheq-2024/4.17.b5."
  author-agent-dialogue: "Raise it when a student asks how to move beyond a pass, or a team sets criteria above the threshold. Put it to a student in plain words and the second person; to staff, frame it as what the course lets every graduate show. Say it describes a higher level, not what is needed to pass. Ask: \"Why did you choose that method over the alternatives, and what would change your mind?\" Avoid presenting this as the minimum and reading the paragraph aloud."
- statement: qaa/finance-2025/4.6.s6
  forPractitioner: { text: "At the excellent level, graduates will proficiently select, evaluate, synthesise and present views, information and results.", rewrite: light, force: will, status: drafted }
  forBeneficiary: { text: "At the highest level, you will select, weigh, combine and present views, information and results with real skill.", rewrite: full, force: will, status: drafted }
  author-agent-written: "Describe this as an excellent-level expectation, in \"will\", the highest level the statement describes (proficient synthesis and presentation). Place it at FHEQ level 6 (FQHEIS level 10 in Scotland), for the bachelor's degree with honours. Cite it as (QAA, 2025, Finance Subject Benchmark Statement, para 4.6). Do not claim that it is the minimum for the award, or that it equals a first or a master's standard; set it beside typical 4.5.s5, threshold item 4.4.b13 and qaa/fheq-2024/annex-d/transferable/r1/1st."
  author-agent-dialogue: "Raise it when a student asks how to move beyond a pass, or a team sets criteria above the threshold. Put it to a student in plain words and the second person; to staff, frame it as what the course lets every graduate show. Say it describes a higher level, not what is needed to pass. Ask: \"How did you decide what to leave out of your presentation?\" Avoid presenting this as the minimum and reading the paragraph aloud."
- statement: qaa/finance-2025/4.6.s7
  forPractitioner: { text: "At the excellent level, graduates will build supported arguments with sophisticated insight into complex matters and show exceptional creativity and originality.", rewrite: light, force: will, status: drafted }
  forBeneficiary: { text: "At the highest level, you will build strong, evidenced arguments, see deeply into complex matters and show exceptional creativity and originality.", rewrite: full, force: will, status: drafted }
  author-agent-written: "Describe this as an excellent-level expectation, in \"will\", the highest level the statement describes (substantiated argument, insight and originality). Place it at FHEQ level 6 (FQHEIS level 10 in Scotland), for the bachelor's degree with honours. Cite it as (QAA, 2025, Finance Subject Benchmark Statement, para 4.6). Do not claim that it is the minimum for the award, or that it equals a first or a master's standard; set it beside typical 4.5.s5, qaa/fheq-2024/annex-d/cognitive/r4/1st and qaa/fheq-2024/annex-d/cognitive/r2/1st."
  author-agent-dialogue: "Raise it when a student asks how to move beyond a pass, or a team sets criteria above the threshold. Put it to a student in plain words and the second person; to staff, frame it as what the course lets every graduate show. Say it describes a higher level, not what is needed to pass. Ask: \"What is the most original point in your recent work, and how did you support it?\" Avoid presenting this as the minimum and reading the paragraph aloud."
```

### S5 Levels and alignment
<!-- label: both; status: drafted; basis: primary -->
```yaml
levels:
  - { id: "fheq:4", role: "cites", locator: "D1, 2.12" }
  - { id: "fheq:5", role: "cites", locator: "D1, 2.12" }
  - { id: "fheq:6", role: "cites", locator: "D1, 2.9" }
  - { id: "fheq:7", role: "cites", locator: "D1, 2.9; 2.14; 2.15; 2.16" }
  - { id: "fqheis:8", role: "cites", locator: "D1, 2.12" }
  - { id: "fqheis:9", role: "cites", locator: "D1, 2.12" }
  - { id: "fqheis:10", role: "cites", locator: "D1, 2.9" }
  - { id: "fqheis:11", role: "cites", locator: "D1, 2.9; 2.14; 2.16" }
  - { id: "spine:6", role: "inferred", locator: "the bachelor's rungs, by std:ref:uk-framework R2" }
  - { id: "spine:7", role: "inferred", locator: "master's awards, by std:ref:uk-framework R2" }
crosswalks:
  - { from: "fheq:6", to: "fqheis:10", relation: "equivalent", basis: "stated (D1, 2.9: bachelor's degree with honours); agrees with std:doc:qaa-fheq-2024-framework Table 1" }
  - { from: "fheq:7", to: "fqheis:11", relation: "equivalent", basis: "stated (D1, 2.9; 2.14; 2.16: integrated and full master's); agrees with Table 1" }
  - { from: "fheq:4", to: "fqheis:8", relation: "equivalent", basis: "stated (D1, 2.12: CertHE); conflicts with Table 1, which places CertHE at FQHEIS 7 (Part E)" }
  - { from: "fheq:5", to: "fqheis:9", relation: "equivalent", basis: "stated (D1, 2.12: DipHE); conflicts with Table 1, which places DipHE at FQHEIS 8 (Part E)" }
```

### S6 Themes
<!-- label: both; status: drafted; basis: primary -->
```yaml
- { id: "theme:edi", role: "carries", carriedIn: ["1.13", "1.18", "1.19", "1.20", "1.21", "1.22", "1.23", "1.24", "1.25", "1.26", "1.27", "2.21", "2.30", "3.2"] }
- { id: "theme:accessibility", role: "carries", carriedIn: ["1.28", "1.29"] }
- { id: "theme:esd", role: "carries", carriedIn: ["1.13", "1.21", "1.30", "1.31", "1.32", "1.33", "1.34", "1.35", "1.36", "1.41", "2.2", "3.2", "4.4"] }
- { id: "theme:enterprise", role: "carries", carriedIn: ["1.37", "1.38", "1.40", "1.41", "1.42", "2.4"] }
- { id: "theme:generative-ai", role: "carries", carriedIn: ["1.43", "1.44", "1.45", "1.46", "1.47", "3.2"] }
```

### S7 Relations
<!-- label: both; status: drafted; basis: primary -->
```yaml
- { rel: "partOf", target: "collection: QAA Subject Benchmark Statements", note: "one of 54 held by stan" }
- { rel: "supersedes", target: "std:doc:qaa-finance-2019-benchmarks (not yet ingested)", note: "the text names \"the previous Subject Benchmark Statement\" without a date; 2019 (minor update) is the latest earlier advisory group in the back matter (Part E)" }
- { rel: "refersTo", target: "std:doc:qaa-fheq-2024-framework, Annex D", note: "evidence of achievement against the rungs (4.2)" }
- { rel: "refersTo", target: "std:doc:qaa-fheq-2024-framework", note: "levels 4 to 7 and master's credit (2.9, 2.12, 2.14 to 2.16)" }
- { rel: "refersTo", target: "std:doc:qaa-fqheis-2024-framework", note: "levels 8 to 11 (2.9, 2.12, 2.14, 2.16)" }
- { rel: "readWith", target: "std:doc:qaa-accounting-2025-benchmarks", note: "joint degrees and single honours accounting (1.4, 1.5)" }
- { rel: "readWith", target: "std:doc:qaa-economics-2023-benchmarks", note: "joint degrees and single honours economics (1.4, 1.5)" }
- { rel: "themeReference", target: "std:doc:qaa-advancehe-esd-2021-guidance", note: "the ESD guidance's learning outcomes (1.34)" }
- { rel: "themeReference", target: "std:doc:qaa-enterprise-2018-guidance", note: "QAA's enterprise and entrepreneurship guidance (1.37; edition inferred, Part E)" }
- { rel: "refersTo", target: "QAA Characteristics Statements: Master's Degree; Micro-credentials (not yet ingested)", note: "2.14; 2.26" }
- { rel: "refersTo", target: "QAA, Unpacking your Hidden Curriculum: Guide for Educators (2022; not yet ingested)", note: "1.24" }
- { rel: "refersTo", target: "PSRB requirements (not yet ingested)", note: "2.24, 2.26, 2.28, 4.3; bodies in SB5" }
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
- Finance studies national and international financial markets and how they interact with households, firms, the third sector, institutions and governments; it is global, central to decisions and always changing (D1, 1.2).
- It joins conceptual study, the theory, with applied study, empirical methods and theory in practice, and keeps both in balance, also in joint degrees (D1, 1.1, 1.4, 2.2).
- Two core domains: markets, banks and institutions; and investment, value, corporate finance, securities, risk and international financial management, with newer areas such as sustainable finance, fintech and AI (D1, 1.6, 1.7).
- It is approached from behavioural, ethical, economic, sustainable and statistical or mathematical angles, with the ethical and social side always present (D1, 1.8, 2.2).
- It draws on accounting and economics but needs only a reasonable knowledge of accounting (D1, 1.5, 2.3).
- It is data driven: statistical and econometric work, programming and AI tools are part of the degree (D1, 1.39, 3.2, 3.13).
- Professional bodies give advanced standing and accreditation, especially for specialist master's courses (D1, 2.24 to 2.26).

### SB2 Themes in this subject
<!-- label: both; status: drafted; basis: primary -->
```yaml
- theme: theme:edi
  inThisSubject: "finance itself carries inequality: access to finance, discrimination in credit, pay gaps and a sector short of diversity are topics to study, alongside an inclusive learning environment, inclusive assessment and attention to the language of finance (D1, 1.18 to 1.27)"
  statements: ["qaa/finance-2025/1.18", "qaa/finance-2025/1.22", "qaa/finance-2025/1.23", "qaa/finance-2025/1.24.b1", "qaa/finance-2025/1.24.b2", "qaa/finance-2025/1.24.b3", "qaa/finance-2025/1.24.b7", "qaa/finance-2025/1.27"]
- theme: theme:accessibility
  inThisSubject: "accessible data terminals, trading simulations and software, equal access to placements and proactive design for neurodivergent students (D1, 1.28, 1.29)"
  statements: ["qaa/finance-2025/1.28", "qaa/finance-2025/1.29.b4", "qaa/finance-2025/1.29.b5", "qaa/finance-2025/1.29.b7", "qaa/finance-2025/1.29.b8", "qaa/finance-2025/1.29.b9", "qaa/finance-2025/1.29.b10"]
- theme: theme:esd
  inThisSubject: "sustainable finance defined through ESG factors; climate, nature and biodiversity finance, ESG disclosure and the SDGs; finance as a lever for sustainable outcomes, also at threshold (D1, 1.30 to 1.36; 4.4)"
  statements: ["qaa/finance-2025/1.33", "qaa/finance-2025/1.34", "qaa/finance-2025/1.41", "qaa/finance-2025/2.2", "qaa/finance-2025/3.2.b12", "qaa/finance-2025/4.4.b11"]
- theme: theme:enterprise
  inThisSubject: "employability through trading simulations, investment competitions, placements, guest practitioners and incubators; transferable skills sought by the finance sector (D1, 1.37 to 1.42)"
  statements: ["qaa/finance-2025/1.41", "qaa/finance-2025/2.4"]
- theme: theme:generative-ai
  inThisSubject: "AI and GenAI as subject matter (payments, lending, fraud detection, algorithmic trading), as tools students learn to use and critique, and as a matter for assessment design and integrity (D1, 1.43 to 1.47; 3.2)"
  statements: ["qaa/finance-2025/3.2.b10", "qaa/finance-2025/4.4.b12"]
```

### SB3 Content and delivery
<!-- label: both; status: drafted; basis: primary -->
```yaml
areas:
  - { component: "1.2", gloss: "traditional areas (banking, corporate, personal, public finance, investment, risk) and emerging ones (climate, green, biodiversity finance, fintech, AI)" }
  - { component: "1.7", gloss: "the two core domains and contemporary areas; the knowledge outcomes are in 3.2" }
  - { component: "2.1", gloss: "global capital, commodity, currency, fixed income and derivatives markets and the institutions in them" }
  - { component: "2.3", gloss: "a reasonable knowledge of accounting" }
practices:
  - { component: "3.5", kind: "teaching", gloss: "what shapes the design of activities: balance of theory and application, research, the student body, mode" }
  - { component: "3.6", kind: "learning", gloss: "active learning: lectures, seminars, workshops, peer and project-based learning, trading simulations, placements" }
  - { component: "3.7", kind: "teaching", gloss: "blended delivery with academic integrity" }
  - { component: "3.8", kind: "learning", gloss: "support in subject language, maths, writing and study skills" }
  - { component: "3.9", kind: "assessment", gloss: "a balanced mix testing concept, application and generic skills" }
  - { component: "3.10", kind: "assessment", gloss: "formative and summative balance; feedback and feed forward" }
  - { component: "3.12", kind: "assessment", gloss: "authentic assessment for problem-solving and reasoning" }
  - { component: "3.13", kind: "assessment", gloss: "closed and open book exams, projects, essays, group and data-oriented tasks" }
```

### SB4 Benchmark standards
<!-- label: both; status: drafted; basis: primary -->
```yaml
rungs:
  - { rung: "threshold", leadIn: "4.4", award: "bachelor's with honours", items: 15 }
  - { rung: "typical", leadIn: "4.5", award: "bachelor's with honours", items: 5 }
  - { rung: "excellent", leadIn: "4.6", award: "bachelor's with honours", items: 7 }
rungBases: "4.1: the three levels are the standards a student will have shown at the award of a bachelor's degree; 4.4 is a list after a \"will be able to\" lead-in under \"Threshold level\"; 4.5 and 4.6 are prose paragraphs under \"Typical level\" and \"Excellent level\", cut here by sentence; 1.15 points specialist master's to the highest levels"
outcomeLists:
  - { leadIn: "3.2", gloss: "subject-specific knowledge and skills on completing a bachelor's", items: 13, award: ["honours"] }
  - { leadIn: "3.3", gloss: "cognitive abilities and generic skills on completing a bachelor's", items: 9, award: ["honours"] }
outcomes:
  - { outcome: "breadth, depth and insight", threshold: "none", typical: "qaa/finance-2025/4.5.s1", excellent: "qaa/finance-2025/4.6.s1", basis: "inferred", domain: "knowledge", award: "bachelor's with honours" }
  - { outcome: "knowledge of theory and specialist topics", threshold: "qaa/finance-2025/4.4.b1", typical: "qaa/finance-2025/4.5.s2", excellent: "qaa/finance-2025/4.6.s2", basis: "inferred", domain: "knowledge", award: "bachelor's with honours" }
  - { outcome: "appraising sources and their limits", threshold: "qaa/finance-2025/4.4.b9", typical: "qaa/finance-2025/4.5.s3", excellent: "qaa/finance-2025/4.6.s4", basis: "inferred", domain: "subject-skill", award: "bachelor's with honours" }
  - { outcome: "investigation and research", threshold: "none", typical: "qaa/finance-2025/4.5.s4", excellent: "qaa/finance-2025/4.6.s3", basis: "inferred", domain: "subject-skill", award: "bachelor's with honours" }
  - { outcome: "solving finance problems", threshold: "qaa/finance-2025/4.4.b2", typical: "qaa/finance-2025/4.5.s4", excellent: "qaa/finance-2025/4.6.s5", basis: "inferred", domain: "subject-skill", award: "bachelor's with honours" }
  - { outcome: "synthesising and communicating", threshold: "qaa/finance-2025/4.4.b13", typical: "qaa/finance-2025/4.5.s5", excellent: "qaa/finance-2025/4.6.s6", basis: "inferred", domain: "generic-skill", award: "bachelor's with honours" }
  - { outcome: "argument, insight and originality", threshold: "none", typical: "qaa/finance-2025/4.5.s5", excellent: "qaa/finance-2025/4.6.s7", basis: "inferred", domain: "generic-skill", award: "bachelor's with honours" }
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
- { body: "professional, statutory and regulatory bodies (PSRBs), in general", says: "courses may meet PSRB requirements for recognition, which can embed a professional standards framework; PSRBs take part in review and may accredit; their requirements may inform competence standards (D1, 2.24, 2.28, 4.3)", requirements: "not yet ingested (Part E)" }
- { body: "AACSB; Association of Corporate Treasurers (ACT); British Accounting and Finance Association (BAFA); Chartered Banker Institute (CBI); CFA Institute; Chartered Institute for Securities and Investment (CISI); EFMD; Financial Management Association (FMA); GARP; PRMIA", says: "networks, professional and learned bodies that course teams may engage with for good practice and development (D1, 2.25)", requirements: "not yet ingested (Part E)" }
- { body: "CFA; CISI; Chartered Banker Institute; ICAEW; ICAS; ACT; GARP; AICPA-CIMA", says: "bodies whose exams or qualifications some courses give advanced standing or accelerated progression towards, mainly specialist master's (D1, 2.26)", requirements: "not yet ingested (Part E)" }
- { body: "Financial Reporting Council (FRC)", says: "its UK Corporate Governance Code (2024) on board diversity, inclusion and equal opportunity is an EDI topic for study (D1, 1.25)", requirements: "not yet ingested (Part E)" }
- { body: "Equality and Human Rights Commission", says: "providers setting competence standards should follow its latest guidance (D1, 4.3)", requirements: "not yet ingested (Part E)" }
- { body: "Advance HE", says: "source of examples of support and adjustments for disabled students, and co-author of the ESD guidance (D1, 1.28, 1.34)", requirements: "std:doc:qaa-advancehe-esd-2021-guidance (for the ESD guidance)" }
```

### SB6 Cross-cutting references
<!-- label: both; status: drafted; basis: primary -->
```yaml
themes:
  - { id: "theme:edi", named: "Equality, diversity and inclusion (front matter: equity, diversity and inclusion)", carriedIn: ["1.13", "1.18", "1.19", "1.20", "1.21", "1.22", "1.23", "1.24", "1.25", "1.26", "1.27", "2.21", "2.30", "3.2"], statements: ["1.18", "1.22", "1.23", "1.24.b1", "1.24.b2", "1.24.b3", "1.24.b7", "1.27"] }
  - { id: "theme:accessibility", named: "Accessibility and the needs of disabled students", carriedIn: ["1.28", "1.29"], statements: ["1.28", "1.29.b4", "1.29.b5", "1.29.b7", "1.29.b8", "1.29.b9", "1.29.b10"] }
  - { id: "theme:esd", named: "Education for sustainable development", carriedIn: ["1.13", "1.21", "1.30", "1.31", "1.32", "1.33", "1.34", "1.35", "1.36", "1.41", "2.2", "3.2", "4.4"], statements: ["1.33", "1.34", "1.41", "2.2", "3.2.b12", "4.4.b11"] }
  - { id: "theme:enterprise", named: "Employability, enterprise and entrepreneurship education", carriedIn: ["1.37", "1.38", "1.40", "1.41", "1.42", "2.4"], statements: ["1.41", "2.4"] }
  - { id: "theme:generative-ai", named: "Generative artificial intelligence (GenAI) and AI applications in finance", carriedIn: ["1.43", "1.44", "1.45", "1.46", "1.47", "3.2"], statements: ["3.2.b10", "4.4.b12"] }
frameworks:
  - { framework: "fheq", levels: ["fheq:4", "fheq:5", "fheq:6", "fheq:7"], citedIn: ["2.9", "2.12", "2.14", "2.15", "2.16"] }
  - { framework: "scqf", named: "FQHEIS", levels: ["fqheis:8", "fqheis:9", "fqheis:10", "fqheis:11"], citedIn: ["2.9", "2.12", "2.14", "2.16"] }
bodies:
  - { body: "PSRBs", citedIn: ["2.24", "2.28", "4.3"] }
  - { body: "AACSB, BAFA, EFMD, FMA, PRMIA", citedIn: ["2.25"] }
  - { body: "ACT, Chartered Banker Institute, CFA Institute, CISI, GARP", citedIn: ["2.25", "2.26"] }
  - { body: "ICAEW, ICAS, AICPA-CIMA", citedIn: ["2.26"] }
  - { body: "Financial Reporting Council", citedIn: ["1.25"] }
  - { body: "Equality and Human Rights Commission", citedIn: ["4.3"] }
  - { body: "Advance HE", citedIn: ["1.28", "1.34"] }
sharedDocuments:
  - { document: "std:doc:qaa-fheq-2024-framework, Annex D", named: "Annex D of the Frameworks for Higher Education Qualifications of UK Degree-Awarding Bodies", citedIn: ["4.2"], role: "guidance on evidence of achievement against the rungs" }
  - { document: "std:doc:qaa-fheq-2024-framework", named: "the Frameworks for Higher Education Qualifications of UK Degree-Awarding Bodies", citedIn: ["2.14"], role: "master's credit and level" }
  - { document: "std:doc:qaa-advancehe-esd-2021-guidance", named: "Education for Sustainable Development Guidance developed by Advance HE and QAA", citedIn: ["1.34"], role: "learning outcomes the core skills align with" }
  - { document: "std:doc:qaa-enterprise-2018-guidance", named: "guidance on Enterprise and Entrepreneurship Education", citedIn: ["1.37"], role: "guidance providers may find helpful (edition inferred, Part E)" }
  - { document: "not yet ingested: listed in Part E", named: "the Characteristics Statement: Master's Degree", citedIn: ["2.14"], role: "master's structure" }
  - { document: "not yet ingested: listed in Part E", named: "the Characteristics Statement on Micro-Credentials", citedIn: ["2.26"], role: "level 7 micro-credits" }
  - { document: "not yet ingested: listed in Part E", named: "Unpacking your Hidden Curriculum: Guide for educators", citedIn: ["1.24"], role: "an example for attending to the hidden curriculum" }
  - { document: "not yet ingested: listed in Part E", named: "the latest guidance from QAA (on generative AI)", citedIn: ["1.47"], role: "due diligence on AI and integrity" }
  - { document: "std:doc:qaa-accounting-2025-benchmarks; std:doc:qaa-economics-2023-benchmarks", named: "the Subject Benchmark Statements for Accounting and Economics", citedIn: ["1.5"], role: "cover single honours accounting and economics; joint degrees align with both" }
```

## Part B Terminology
<!-- The statement has no glossary of its own unless Part E says so; these are terms it defines in its text. -->

### B1 Concepts
<!-- label: both; status: drafted; basis: primary -->
```yaml
- { slug: "sustainable-finance", definition: "finance decisions (investing, lending, risk, insurance, disclosure) that weigh environmental, social and governance factors for long-term sustainable activity (D1, 1.30)", beneficiaryDefinition: "finance that takes account of environmental, social and governance effects, not only returns", scopeNote: "the definition the statement gives for its ESD section", category: "unknown", practices: ["education"] }
- { slug: "generative-ai", definition: "large language model systems that use deep learning to imitate creativity and produce new content from prompts (D1, 1.43)", beneficiaryDefinition: "AI tools that write or create new content when you give them a prompt", scopeNote: "the statement treats AI more broadly beside it", category: "unknown", practices: ["education"] }
- { slug: "enterprise-and-entrepreneurship-education", definition: "education that builds behaviours, attributes and competencies for successful careers and changing settings (D1, 1.37)", beneficiaryDefinition: "learning that builds the enterprising skills and mindset that help in any career", scopeNote: "abbreviated EED", category: "unknown", practices: ["education"] }
- { slug: "accessibility", definition: "removing barriers so that learners can reach outcomes fairly (D1, 1.28)", beneficiaryDefinition: "making sure nothing in the course stops you from reaching its outcomes", scopeNote: "with a regulatory minimum", category: "unknown", practices: ["education"] }
- { slug: "hidden-curriculum", definition: "the unstated expectations of how students behave (D1, 1.29)", beneficiaryDefinition: "the unwritten rules of studying that nobody spells out", scopeNote: "also the language of finance (1.24)", category: "unknown", practices: ["education"] }
- { slug: "alternative-investments", definition: "investments that seek market inefficiencies through unusual assets and strategies, such as hedge funds, private equity, private credit and real assets (D1, 1.7)", scopeNote: "given as a contemporary area", category: "unknown", practices: ["finance"] }
- { slug: "conversion-masters", definition: "a master's for students whose first degree is not in Finance or who studied it in another jurisdiction (D1, 1.15)", scopeNote: "beside the specialist master's", category: "unknown", practices: ["education"] }
- { slug: "threshold-standard", definition: "the minimum a student will have shown on being awarded a bachelor's degree in Finance (D1, 4.1, 4.4)", scopeNote: "with typical and excellent above it (4.5, 4.6)", category: "unknown", practices: ["education"] }
```

### B2a Terms as the issuer defines them
<!-- label: source; status: drafted; basis: primary -->
```yaml
- { concept: "sustainable-finance", form: "sustainable finance", lang: "en", partOfSpeech: "noun-phrase", termStatus: "preferred", register: "discipline-specific" }
- { concept: "generative-ai", form: "Generative artificial intelligence", lang: "en", partOfSpeech: "noun-phrase", termStatus: "preferred", register: "formal" }
- { concept: "generative-ai", form: "GenAI", lang: "en", partOfSpeech: "noun", termStatus: "admitted", register: "formal" }
- { concept: "enterprise-and-entrepreneurship-education", form: "Enterprise and entrepreneurship education", lang: "en", partOfSpeech: "noun-phrase", termStatus: "preferred", register: "formal" }
- { concept: "enterprise-and-entrepreneurship-education", form: "EED", lang: "en", partOfSpeech: "noun", termStatus: "admitted", register: "formal" }
- { concept: "accessibility", form: "Accessibility", lang: "en", partOfSpeech: "noun", termStatus: "preferred", register: "formal" }
- { concept: "hidden-curriculum", form: "hidden curriculum", lang: "en", partOfSpeech: "noun-phrase", termStatus: "preferred", register: "formal" }
- { concept: "alternative-investments", form: "alternative investments", lang: "en", partOfSpeech: "noun-phrase", termStatus: "preferred", register: "discipline-specific" }
- { concept: "conversion-masters", form: "Finance conversion master's degrees", lang: "en", partOfSpeech: "noun-phrase", termStatus: "preferred", register: "formal" }
- { concept: "threshold-standard", form: "minimum threshold", lang: "en", partOfSpeech: "noun-phrase", termStatus: "preferred", register: "formal" }
```

### B2b Associated vocabulary
`not-applicable-by-design`: the statement names no wider vocabulary.

### B3 Framework blocks
`not-applicable-by-design`: no term is defined its own way for one component.

### B4 Relations
<!-- label: both; status: drafted; basis: primary -->
```yaml
- { rel: "contrasts-with", from: "conversion-masters", to: "specialist master's (1.15)", note: "the two kinds of master's the statement names" }
```

## Part C Process
<!-- label: both; status: drafted; basis: primary -->

### C0 Formality
`not-applicable`: the statement sets out what graduates achieve and what courses provide, not a procedure.

## Part D Sources
```yaml
- key: D1
  issuer: The Quality Assurance Agency for Higher Education
  title: "Subject Benchmark Statement Finance"
  edition: "April 2025 (Fourth Edition)"
  year: 2025
  url: unknown (the QAA page; the text came by stan's extraction)
  retrieved: "held from stan: wkspc2615-QAAVector mapped/finance-2025/finance-2025.raw.txt, commit 366bcb99a01118f2c4c3ebfa2a8337596bddc455; received 2026-10-03"
  licence: QAA copyright
  tier: primary
  readVia: direct
  held: d25ca6ef8e4ef75bf4cdcac810e6e54f7165ca2896b48a68b9210c16fa7f396f
  heldFiles: ["wkspc2601-library/txt/qaa-2025-finance-subject-benchmark-statement-standard.txt", "wkspc2601-library/txt/qaa-2025-finance-subject-benchmark-statement-standard.norm.txt", "wkspc2601-library/records/qaa-2025-finance-subject-benchmark-statement-standard.chunks.json", "wkspc2601-library/records/qaa-2025-finance-subject-benchmark-statement-standard.held.json"]
  citedIn: [S1, S2, S3, S4, S4a, S5, S6, S7, SB1, SB2, SB3, SB4, SB5, SB6]
```

### D2 Research log
```yaml
- { ref: D1, tier: primary, consulted: 2026-10-03, pass: P1, outcome: "read whole, direct, from the normalised text; skeleton by tools/std_prep.py, document by tools/bm_build.py" }
- { ref: "ADAPT subj HESA stores, cah.json and hecos.json (designs/ingest/standards/subj/vocab)", tier: primary, consulted: 2026-10-03, pass: P1, outcome: "codes for statedSubjects and subjects" }
```

### D3 Wanted sources
```yaml
- { w: "W-std-0026", title: "QAA Characteristics Statement: Master's Degree", why: "cited in 2.14" }
- { w: "W-std-0038", title: "QAA Characteristics Statement: Micro-credentials", why: "cited in 2.26" }
- { w: "W-std-0059", title: "QAA (2022) Unpacking your Hidden Curriculum: Guide for Educators", why: "cited in 1.24" }
- { w: "W-std-0044", title: "QAA guidance on generative AI (the latest, as 1.47 asks)", why: "cited in 1.47" }
- { w: "W-std-0060", title: "Finance Subject Benchmark Statement, previous edition (2019)", why: "S7 supersedes and the key changes the front matter names" }
```

## Part E Gaps and questions
- Pattern (new rung shape): threshold is a list (4.4, 15 items, lead-in "will be able to"); typical (4.5) and excellent (4.6) are prose paragraphs of "will" sentences. Cut here one record per sentence, with our ids 4.5.s1 to 4.5.s5 and 4.6.s1 to 4.6.s7 (the issuer's paragraph number plus sentence). The alternative, one record per paragraph, is for Abbott at P3. The builder leaves the sub-heading out of `headingPath` for these ids, since it reads only numeric ids (a tool point for std).
- Pattern: the threshold lead-in names no rung; the sub-heading "Threshold level" and 4.1's "minimum threshold" make it the rung. Threshold items take force `threshold` (4.1 defines it as the minimum for the award), with forceFrom 4.1; typical and excellent sentences keep "will" (their first sentences use "can distinguish themselves").
- Pattern: benchmark standards are for the bachelor's degree only; master's awards have no rungs of their own, and 1.15 says a specialist master's would be expected to be judged against the highest levels (recorded as 1.15.b1, force `describes`).
- Pattern: integrated master's (1.17) take the typical honours standard then master's level in their specialism: a plain-present norm, not taken as a statement.
- Force, words outside the five: 3.2 and 3.3 lead in "is generally expected to have" (all 22 items recorded as `describes`; for Abbott: should "generally expected" read as `will` or `should`?); 1.15.b1 "would be expected to be evaluated" (`describes`); 1.24.b3 "is necessary" read as `must`; 2.21 "it is essential to ensure" read as `must`; 1.6 and 1.7 "requires students to" and 2.3 "is required" read as `must`; 3.4 "It is the responsibility of each higher education provider" with "will be able to demonstrate" (taken as `will`).
- Not taken as statements, for P3: plain-present provider norms 1.13, 1.17, 1.29.b1, b2, b3 and b6 (under the lead-in "This will go beyond compliance ... to include, for example"), 1.30, 1.36, 1.45, 1.46, 1.47, 2.6, 2.8, 2.27; plain-present graduate descriptions 1.33 (last sentence), 1.39, 1.42 ("Finance graduates have an awareness"); predictive or descriptive "will" 1.14, 1.26 ("An EDI approach ... will take cognisance"), 1.29 lead-in, 2.10, 2.18, 4.1; predictive "should help" 1.35; "will need to adapt" 1.44; "it is expected that each level would see" 2.9; "It is not intended that degree programmes should include all the examples" 3.1 (negated); "is an essential component" 2.28; "it is important that" 1.19, 1.23 (first sentence), 1.36.
- S4: 1.24.b4 to b6 and 1.25.b1 to b8 follow "could include" or "including, but not limited to" lead-ins: examples, not statements. 1.7.b1 to b3 are kept inside the 1.7 record (examples of contemporary areas). 1.9 and 1.10 list careers and sectors: not statements.
- Skeleton corrections (`find` used): 4.4.b15, 3.3.b9, 1.29.b10, 2.4, 2.17, 2.21, 3.8 and 4.3 carried the next run-in heading; 1.15.b1 and 3.2.b13 were cut at a page break; 1.6, 1.28 and 3.14 trimmed of a trailing page number. The skeleton's rung counts (0, 0, 0) were wrong: the rungs are 15, 5 and 7.
- Skeleton theme hits corrected: 1.17 (EDI), 1.27 (accessibility), 1.29 (ESD) and 1.36 (enterprise) were heading run-ins of the next section, not content; 1.35 ("financial accessibility and inclusion") and 1.44 ("more accessible") use the words in another sense; 1.38 and 2.20 carry no EDI content. 2.20 and 1.2 dropped for the same reason. Added: generative AI (1.43 to 1.47, 3.2.b10), not in the skeleton.
- SB4 gradeOf, all inferred (the issuer pairs nothing): 4.5.s2 to 4.4.b1, 4.5.s3 to 4.4.b9, 4.5.s4 to 4.4.b2, 4.5.s5 to 4.4.b13; 4.6.s1 to 4.5.s1, 4.6.s2 to 4.5.s2, 4.6.s3 to 4.5.s4, 4.6.s4 to 4.5.s3, 4.6.s5 to 4.5.s4, 4.6.s6 to 4.5.s5, 4.6.s7 to 4.5.s5. Two excellent sentences share one typical sentence twice (4.5.s4 and 4.5.s5); weaker matches: 4.5.s4 to 4.4.b2 (investigation is not in the threshold item) and 4.6.s7 to 4.5.s5. 4.5.s1 has no threshold match; 4.4.b3 to b8, b10 to b12, b14 and b15 have no typical match.
- S5, crosswalk conflict: 2.12 places the CertHE at FHEQ 4 and FQHEIS 8 and the DipHE at FHEQ 5 and FQHEIS 9; the FHEQ document's Table 1 (std:doc:qaa-fheq-2024-framework, S5) places them at SCQF 7 and SCQF 8. Recorded as stated; for Abbott at P3 (an issuer error, recall: likely).
- S5: spine:6 and spine:7 are inferred from the reference framework R2, not stated.
- Subjects: hecos 100107 and cah CAH17-01-07 (finance) and the titles in 1.3 (financial management 100832, banking 100827, investment 100828) are stated by name; CAH17-01 and CAH17 (business and management) are inferred from the CAH hierarchy, held back until P3. No HECoS term found for fintech, personal finance, financial services or sustainable finance.
- S7: the previous statement is named only as "the previous Subject Benchmark Statement"; 2019 is read from the back matter's advisory group list (minor update) and is inferred.
- S7, SB6: the enterprise guidance is cited without a date (1.37); std:doc:qaa-enterprise-2018-guidance is our inference (recall).
- SB6, front matter: names the EDI theme "equity, diversity and inclusion" and the enterprise theme "employability, entrepreneurship and enterprise education"; the section headings use "Equality" and "Employability, enterprise and entrepreneurship education". Front matter is excluded matter, so cited by section only.
- SB6, not tagged as bodies or shared QAA documents (outside QAA, named once): the UN SDGs (1.13, 1.21, 1.30, 1.31, 1.32), OECD Principles of Corporate Governance, Principles of Responsible Investment, Principles for Responsible Banking, Principles for Sustainable Insurance and the UK net zero legislation (1.30), the Financial Stability Task Force (1.36), the Russell Group Principles on generative AI (1.47), the Equality Act 2010 (4.3), the Office for Students (front matter), the Quality Code and QAA Glossary (front matter).
- SB5: the issuer writes "Chartered Institute of Management Accountants (AICPA-CIMA)" and "CFA Institute (Chartered Financial Analyst)"; kept as given. None of the bodies' requirements is ingested.
- S1, licence: the text gives a copyright notice and no re-use terms; QAA's terms for holding and chunking are to check.
- S9: not researched in P1.
- Levels: generic-skill records (3.3, 4.4.b13 to b15, 4.5.s5, 4.6.s6, 4.6.s7) refine fheq:6, which is in S5.
- Provider duties (28 records) have no student version; their `aad` addresses the programme team only.
- ST-12: versions here run to the lengths the content needs; no length range is yet set.

---

## Change notes
- 0.1.2, 3 October 2026, 21:02: moved with its held text from UNI to the source library repo (`wkspc2601-library/ingested/standards/`, texts in `txt/`, records in `records/`); paths only (Abbott, 20:56; std N-0119).
- 0.1.1, 3 October 2026, 20:20: obliging words outside the five read as must, "ought to" as should, on statements outside the rungs, each marked on its force line (Abbott, 20:17; D-std-0016).
- 0.1.0, 2026-10-03 17:30: researched by run frame 0.1.1-draft and standards run layer 0.7.0-draft, std, run 0106 (P1); built by tools/bm_build.py.
