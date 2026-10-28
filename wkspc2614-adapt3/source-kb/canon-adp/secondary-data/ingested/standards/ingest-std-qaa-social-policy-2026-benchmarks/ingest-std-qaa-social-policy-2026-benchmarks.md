---
id: std:doc:qaa-social-policy-2026-benchmarks
title: "Subject Benchmark Statement: Social Policy"
profile: standards/subject-benchmark
profileVersion: 0.2.0-draft
issuer: QAA
kind: subject-benchmark
jurisdiction: [UK]
subjectScope: subjects
subjects:
  - { scheme: "hecos", code: "100502", label: "social policy", basis: "stated" }
  - { scheme: "cah", code: "CAH15-01-03", label: "social policy", basis: "stated" }
edition: "April 2026 (fifth edition)"
published: 2026-04
status: current
supersedes: "the fourth edition, 2019 (minor update), as the back matter records"
heldText: { method: sha256-bytes, raw: 94056f12b97c3fb116313a2f0780a4027e668e36a07d2847c6745e6ee453c8c3, normalised: 118c080e8d5dfd793d8bd3723c55c445b3a2f228b71f644b26b28518c7394e04 }
heldTextStan: { method: sha256-stan, raw: 94056f12b97c3fb116313a2f0780a4027e668e36a07d2847c6745e6ee453c8c3, normalised: fc0d1bef59b104769ab619adc0f93f9edcc62e568d275fb7af06301de9bff4a1 }
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
researchedBy: run frame 0.1.1-draft; standards run layer 0.7.0-draft; std, run 0129 (tools/bm_build.py)
passes:
  P1: "2026-10-03 18:29"
  P2: "skipped: read direct from the held text; inferred codes and rung links are for P3"
  P3: open
version: 0.1.2
---

<!-- from INGEST wpk-0016-ingest-pd-template-standards.md 0.8.0-draft and wpk-0016-ingest-pd-template-standards-benchmark.md 0.6.0-draft; built by tools/bm_build.py from run-src/ -->
# Subject Benchmark Statement: Social Policy (QAA, April 2026)

> Run 0129, P1 by std. The issuer's words are held in the source library, `wkspc2601-library/txt/qaa-2026-social-policy-subject-benchmark-statement-standard.norm.txt`; each S4 record carries its statement in full (`source`) for language analysis, with its span. Paraphrases and versions are ours. Private to the project, never published. In front matter `status` is the issuer's; ours is `lifecycle`. Doubts are in Part E.

## Part 0 Summary

### 0.1 Agent definition
<!-- label: editorial; status: drafted; basis: primary -->
QAA's UK reference point for what a Social Policy graduate can be expected to know, understand and do at the end of an honours degree, with lists for master's graduates. It holds three-rung tables (threshold, typical, excellent, tied to third, second and first-class honours) for knowledge and understanding, subject-specific skills, generic intellectual skills and generic transferable skills, a long list of knowledge areas and four master's lists. Reach for it when designing, reviewing or describing a Social Policy course, module or its outcomes. It is not a curriculum and not a regulatory requirement in England.

### 0.2 Summary
<!-- label: both; status: drafted; basis: primary -->
Published by QAA in April 2026 as the fifth edition, the statement sets out the context and purposes of the subject (human welfare, need, social justice and resource distribution, across state, market, voluntary and family sectors), its distinctive features (design, progression, flexibility, partnership, monitoring), content, teaching and assessment, and benchmark standards. For the bachelor's degree with honours it gives three rungs, threshold (third class), typical (second class) and excellent (first class), in four tables; for the master's degree it gives four lists with no rungs. It carries five cross-cutting themes: equity, diversity and inclusion (with a strong decolonising strand); accessibility and the needs of disabled students; education for sustainable development (the UN goals); employability, entrepreneurship and enterprise education; and generative AI. It points to Annex D of the Frameworks for the four honours classes, cites the FHEQ and the FQHEIS (SCQF) for levels, and names PSRBs as a class, the Equality and Human Rights Commission and the Disabled Students Commission.

## Part S Standard

### S1 Identity
<!-- label: source; status: drafted; basis: primary -->
```yaml
issuer: The Quality Assurance Agency for Higher Education
title: "Subject Benchmark Statement: Social Policy"
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
governs: "what a Social Policy graduate can be expected to know, do and understand at the end of an honours degree, with standards for the master's degree, and the nature of awards in the subject (D1, front matter: About this Statement; 1.1; 4.1)"
appliesTo:
  awards: ["bachelor's degree with honours", "integrated master's (described, 2.8, 2.12)", "taught master's degree (4.11 to 4.15)", "joint and combined honours (1.2, 2.10)", "CertHE and DipHE as exit awards (2.11)"]
  levels: ["fheq:6", "fheq:7", "fqheis:10", "fqheis:11"]
  providers: ["UK higher education providers"]
whoMustUse: "none-stated; it is a reference point, not a requirement (D1, front matter)"
howUsed: ["design", "approval", "review", "other: external examining; PSRBs; information for prospective students and employers"]
doesNot: "it does not prescribe approaches to teaching, learning or assessment; it does not interpret legislation or carry statutory or regulatory requirements; its threshold standards are not universal competence standards (D1, front matter; 4.4)"
beneficiary: the student
statedScope: "\"This QAA Subject Benchmark Statement for Social Policy defines what can be expected of a graduate in terms of what they might know, do, and understand at the end of their studies.\" (D1, front matter: About this Statement)"
statedSubjects:
  - { name: "Social Policy", locator: "(D1, title; 1.1; 1.3)", kind: "subject", codes: [{ scheme: "hecos", code: "100502", label: "social policy" }, { scheme: "cah", code: "CAH15-01-03", label: "social policy" }] }
  - { name: "Social Administration (the subject's historical root)", locator: "(D1, 1.9)", kind: "subject", codes: [{ scheme: "hecos", code: "100090", label: "public administration" }] }
  - { name: "wider social science programmes", locator: "(D1, 1.2; 3.1)", kind: "programme title", codes: [{ scheme: "hecos", code: "100471", label: "social sciences" }] }
  - { name: "Sociology, Politics, Criminology and Economics (degrees in which the subject is taught)", locator: "(D1, 1.59)", kind: "programme title", codes: [{ scheme: "hecos", code: "100505", label: "sociology" }, { scheme: "hecos", code: "100491", label: "politics" }, { scheme: "hecos", code: "100484", label: "criminology" }, { scheme: "hecos", code: "100450", label: "economics" }] }
  - { name: "Public Policy and Administration (overlapping field)", locator: "(D1, 2.6)", kind: "subject", codes: [{ scheme: "hecos", code: "100647", label: "public policy" }, { scheme: "hecos", code: "100090", label: "public administration" }] }
  - { name: "combined or joint degree (including major and minor options)", locator: "(D1, 1.2; 2.10)", kind: "programme title", codes: [{ scheme: "cah", code: "CAH15-01-03", label: "social policy" }] }
subjects: see front matter (subjectScope subjects)
```

### S3 Structure
<!-- label: both; status: drafted; basis: primary -->
```yaml
components:
  - { number: "1.1", order: 3, componentType: paragraph, parent: "section 1", heading: "Context and purposes of a Social Policy degree", gloss: "what the statement sets out, for undergraduate and taught postgraduate study" }
  - { number: "1.2", order: 4, componentType: paragraph, parent: "section 1", heading: "Context and purposes of a Social Policy degree", gloss: "joint honours and standalone modules" }
  - { number: "1.3", order: 5, componentType: paragraph, parent: "section 1", heading: "Context and purposes of a Social Policy degree", gloss: "the discipline against the practice of policy" }
  - { number: "1.4", order: 6, componentType: paragraph, parent: "section 1", heading: "Context and purposes of a Social Policy degree", gloss: "welfare, need and justice; academic and applied" }
  - { number: "1.5", order: 7, componentType: paragraph, parent: "section 1", heading: "Context and purposes of a Social Policy degree", gloss: "dividing and allocating welfare resources" }
  - { number: "1.6", order: 8, componentType: paragraph, parent: "section 1", heading: "Context and purposes of a Social Policy degree", gloss: "who gains and loses; social divisions" }
  - { number: "1.7", order: 9, componentType: paragraph, parent: "section 1", heading: "Context and purposes of a Social Policy degree", gloss: "devolution, local government and subsidiarity" }
  - { number: "1.8", order: 10, componentType: paragraph, parent: "section 1", heading: "Context and purposes of a Social Policy degree", gloss: "policy in lived experience over the life course" }
  - { number: "1.9", order: 11, componentType: paragraph, parent: "section 1", heading: "Context and purposes of a Social Policy degree", gloss: "roots in Social Administration" }
  - { number: "1.10", order: 12, componentType: paragraph, parent: "section 1", heading: "Context and purposes of a Social Policy degree", gloss: "polycrises and resilient welfare" }
  - { number: "1.11", order: 13, componentType: paragraph, parent: "section 1", heading: "Context and purposes of a Social Policy degree", gloss: "welfare beyond the state" }
  - { number: "1.12", order: 14, componentType: paragraph, parent: "section 1", heading: "Context and purposes of a Social Policy degree", gloss: "the four sectors of provision" }
  - { number: "1.13", order: 15, componentType: paragraph, parent: "section 1", heading: "Context and purposes of a Social Policy degree", gloss: "racism and other structural discrimination" }
  - { number: "1.14", order: 16, componentType: paragraph, parent: "section 1", heading: "Context and purposes of a Social Policy degree", gloss: "environmental sustainability central to welfare" }
  - { number: "1.15", order: 17, componentType: paragraph, parent: "section 1", heading: "Context and purposes of a Social Policy degree", gloss: "safety net or wide provision" }
  - { number: "1.16", order: 18, componentType: paragraph, parent: "section 1", heading: "Purposes and characteristics of a Social Policy degree", gloss: "entitlement, rights and citizenship" }
  - { number: "1.17", order: 19, componentType: paragraph, parent: "section 1", heading: "Purposes and characteristics of a Social Policy degree", gloss: "regimes, governance and policy design" }
  - { number: "1.18", order: 20, componentType: paragraph, parent: "section 1", heading: "Purposes and characteristics of a Social Policy degree", gloss: "cash, services and public finance" }
  - { number: "1.19", order: 21, componentType: paragraph, parent: "section 1", heading: "Purposes and characteristics of a Social Policy degree", gloss: "research evidence, power and ideology" }
  - { number: "1.20", order: 22, componentType: paragraph, parent: "section 1", heading: "Purposes and characteristics of a Social Policy degree", gloss: "a normative subject; values and research" }
  - { number: "1.21", order: 23, componentType: paragraph, parent: "section 1", heading: "Purposes and characteristics of a Social Policy degree", gloss: "decolonising curricula" }
  - { number: "1.22", order: 24, componentType: paragraph, parent: "section 1", heading: "Purposes and characteristics of a Social Policy degree", gloss: "UK history, empire and colonisation" }
  - { number: "1.23", order: 25, componentType: paragraph, parent: "section 1", heading: "Purposes and characteristics of a Social Policy degree", gloss: "empire, Commonwealth and post-war rebuilding" }
  - { number: "1.24", order: 26, componentType: paragraph, parent: "section 1", heading: "Purposes and characteristics of a Social Policy degree", gloss: "colonial legacies in analysis and funding" }
  - { number: "1.25", order: 27, componentType: paragraph, parent: "section 1", heading: "Purposes and characteristics of a Social Policy degree", gloss: "blind spots of the canon" }
  - { number: "1.26", order: 28, componentType: paragraph, parent: "section 1", heading: "Purposes and characteristics of a Social Policy degree", gloss: "global majority understandings" }
  - { number: "1.27", order: 29, componentType: paragraph, parent: "section 1", heading: "Purposes and characteristics of a Social Policy degree", gloss: "cannot be fully decolonised; diversify teaching" }
  - { number: "1.28", order: 30, componentType: paragraph, parent: "section 1", heading: "Purposes and characteristics of a Social Policy degree", gloss: "openness to diverse welfare systems" }
  - { number: "1.29", order: 31, componentType: paragraph, parent: "section 1", heading: "Equity, diversity and inclusion", gloss: "varied starting points on entry" }
  - { number: "1.30", order: 32, componentType: paragraph, parent: "section 1", heading: "Equity, diversity and inclusion", gloss: "diverse students; equity in teaching" }
  - { number: "1.31", order: 33, componentType: paragraph, parent: "section 1", heading: "Equity, diversity and inclusion", gloss: "diverse needs and awarding gaps" }
  - { number: "1.32", order: 34, componentType: paragraph, parent: "section 1", heading: "Equity, diversity and inclusion", gloss: "support and belonging for all" }
  - { number: "1.33", order: 35, componentType: paragraph, parent: "section 1", heading: "Equity, diversity and inclusion", gloss: "constructive dialogue across views" }
  - { number: "1.34", order: 36, componentType: paragraph, parent: "section 1", heading: "Equity, diversity and inclusion", gloss: "co-constructing curricula" }
  - { number: "1.35", order: 37, componentType: stem, parent: "section 1", heading: "Equity, diversity and inclusion", gloss: "equity, diversity and inclusion defined" }
  - { number: "1.36", order: 38, componentType: paragraph, parent: "section 1", heading: "Equity, diversity and inclusion", gloss: "good EDI practice in design" }
  - { number: "1.37", order: 39, componentType: paragraph, parent: "section 1", heading: "Equity, diversity and inclusion", gloss: "applying EDI critically to policy debate" }
  - { number: "1.38", order: 40, componentType: paragraph, parent: "section 1", heading: "Equity, diversity and inclusion", gloss: "self-reflection and others' views" }
  - { number: "1.39", order: 41, componentType: paragraph, parent: "section 1", heading: "Equity, diversity and inclusion", gloss: "graduates reflecting on inclusion and identity" }
  - { number: "1.40", order: 42, componentType: paragraph, parent: "section 1", heading: "Accessibility and the needs of disabled students", gloss: "anticipatory accessibility under equality law" }
  - { number: "1.41", order: 43, componentType: paragraph, parent: "section 1", heading: "Accessibility and the needs of disabled students", gloss: "diverse backgrounds as a learning resource" }
  - { number: "1.42", order: 44, componentType: stem, parent: "section 1", heading: "Accessibility and the needs of disabled students", gloss: "four areas for inclusive, accessible courses" }
  - { number: "1.43", order: 45, componentType: paragraph, parent: "section 1", heading: "Accessibility and the needs of disabled students", gloss: "placement support for disabled students" }
  - { number: "1.44", order: 46, componentType: paragraph, parent: "section 1", heading: "Education for sustainable development", gloss: "sustainable development in welfare debate" }
  - { number: "1.45", order: 47, componentType: paragraph, parent: "section 1", heading: "Education for sustainable development", gloss: "the UN goals described" }
  - { number: "1.46", order: 48, componentType: paragraph, parent: "section 1", heading: "Education for sustainable development", gloss: "the subject aligned with the UN goals" }
  - { number: "1.47", order: 49, componentType: paragraph, parent: "section 1", heading: "Education for sustainable development", gloss: "the UN goals as a way into eco-social policy" }
  - { number: "1.48", order: 50, componentType: paragraph, parent: "section 1", heading: "Education for sustainable development", gloss: "welfare, economy and the environment" }
  - { number: "1.49", order: 51, componentType: paragraph, parent: "section 1", heading: "Education for sustainable development", gloss: "goals in programme design; global problems" }
  - { number: "1.50", order: 52, componentType: paragraph, parent: "section 1", heading: "Education for sustainable development", gloss: "ESD resources; Inner Development Goals" }
  - { number: "1.51", order: 53, componentType: paragraph, parent: "section 1", heading: "Education for sustainable development", gloss: "sustainability across all teaching" }
  - { number: "1.52", order: 54, componentType: paragraph, parent: "section 1", heading: "Education for sustainable development", gloss: "critiquing sustainability; climate and privilege" }
  - { number: "1.53", order: 55, componentType: paragraph, parent: "section 1", heading: "Education for sustainable development", gloss: "sustainability and lifelong learning" }
  - { number: "1.54", order: 56, componentType: paragraph, parent: "section 1", heading: "Employability, entrepreneurship and enterprise education", gloss: "EEE for problem solving and careers" }
  - { number: "1.55", order: 57, componentType: paragraph, parent: "section 1", heading: "Employability, entrepreneurship and enterprise education", gloss: "EEE and careers services" }
  - { number: "1.56", order: 58, componentType: paragraph, parent: "section 1", heading: "Employability, entrepreneurship and enterprise education", gloss: "EEE through authentic assessment and placements" }
  - { number: "1.57", order: 59, componentType: paragraph, parent: "section 1", heading: "Employability, entrepreneurship and enterprise education", gloss: "accessible placements and volunteering" }
  - { number: "1.58", order: 60, componentType: paragraph, parent: "section 1", heading: "Employability, entrepreneurship and enterprise education", gloss: "EEE beyond placements" }
  - { number: "1.59", order: 61, componentType: paragraph, parent: "section 1", heading: "Employability, entrepreneurship and enterprise education", gloss: "graduate careers; teaching beside other subjects" }
  - { number: "1.60", order: 62, componentType: paragraph, parent: "section 1", heading: "Generative artificial intelligence", gloss: "critical engagement with GenAI" }
  - { number: "1.61", order: 63, componentType: stem, parent: "section 1", heading: "Generative artificial intelligence", gloss: "gains from GenAI in learning" }
  - { number: "1.62", order: 64, componentType: stem, parent: "section 1", heading: "Generative artificial intelligence", gloss: "risks of GenAI" }
  - { number: "1.63", order: 65, componentType: paragraph, parent: "section 1", heading: "Generative artificial intelligence", gloss: "integrating GenAI into teaching and assessment" }
  - { number: "1.64", order: 66, componentType: paragraph, parent: "section 1", heading: "Generative artificial intelligence", gloss: "employability and responsible GenAI use" }
  - { number: "1.65", order: 67, componentType: paragraph, parent: "section 1", heading: "Generative artificial intelligence", gloss: "institutional GenAI policy; teaching risks" }
  - { number: "1.66", order: 68, componentType: paragraph, parent: "section 1", heading: "Generative artificial intelligence", gloss: "pointer to QAA GenAI resources" }
  - { number: "2.1", order: 70, componentType: paragraph, parent: "section 2", heading: "Design", gloss: "core questions for any social problem" }
  - { number: "2.2", order: 71, componentType: stem, parent: "section 2", heading: "Design", gloss: "five elements of programme design" }
  - { number: "2.3", order: 72, componentType: stem, parent: "section 2", heading: "Design", gloss: "interdisciplinary knowledge; what students critique" }
  - { number: "2.4", order: 73, componentType: stem, parent: "section 2", heading: "Design", gloss: "skills for policy analysis and communication" }
  - { number: "2.5", order: 74, componentType: paragraph, parent: "section 2", heading: "Design", gloss: "debate, evidence and colonial influence" }
  - { number: "2.6", order: 75, componentType: paragraph, parent: "section 2", heading: "Design", gloss: "social administration; reflective practice" }
  - { number: "2.7", order: 76, componentType: paragraph, parent: "section 2", heading: "Design", gloss: "student contributions to review" }
  - { number: "2.8", order: 77, componentType: paragraph, parent: "section 2", heading: "Progression", gloss: "progression through the levels" }
  - { number: "2.9", order: 78, componentType: paragraph, parent: "section 2", heading: "Progression", gloss: "readiness for postgraduate study" }
  - { number: "2.10", order: 79, componentType: paragraph, parent: "section 2", heading: "Progression", gloss: "joint and combined degrees" }
  - { number: "2.11", order: 80, componentType: paragraph, parent: "section 2", heading: "Progression", gloss: "early exit awards" }
  - { number: "2.12", order: 81, componentType: paragraph, parent: "section 2", heading: "Flexibility", gloss: "course length and Scottish degrees" }
  - { number: "2.13", order: 82, componentType: paragraph, parent: "section 2", heading: "Flexibility", gloss: "modes of study and credit" }
  - { number: "2.14", order: 83, componentType: paragraph, parent: "section 2", heading: "Partnership", gloss: "partnership delivery" }
  - { number: "2.15", order: 84, componentType: paragraph, parent: "section 2", heading: "Monitoring and review", gloss: "monitoring, review and student voice" }
  - { number: "2.16", order: 85, componentType: paragraph, parent: "section 2", heading: "Monitoring and review", gloss: "external reviewers in periodic review" }
  - { number: "2.17", order: 86, componentType: paragraph, parent: "section 2", heading: "Monitoring and review", gloss: "the external examining system" }
  - { number: "2.18", order: 87, componentType: paragraph, parent: "section 2", heading: "Monitoring and review", gloss: "professional accreditation" }
  - { number: "3.1", order: 89, componentType: paragraph, parent: "section 3", heading: "Content", gloss: "a dynamic subject; core content without prescription" }
  - { number: "3.2", order: 90, componentType: area, parent: "section 3", heading: "Content", gloss: "insights at local to global scale; fields of policy" }
  - { number: "3.3", order: 91, componentType: area, parent: "section 3", heading: "Content", gloss: "knowledge areas of graduates, in five groups" }
  - { number: "3.4", order: 92, componentType: practice, parent: "section 3", heading: "Teaching and learning", gloss: "aims and methods of teaching" }
  - { number: "3.5", order: 93, componentType: practice, parent: "section 3", heading: "Teaching and learning", gloss: "virtual and distance learning" }
  - { number: "3.6", order: 94, componentType: practice, parent: "section 3", heading: "Teaching and learning", gloss: "experiences that prepare for work" }
  - { number: "3.7", order: 95, componentType: practice, parent: "section 3", heading: "Teaching and learning", gloss: "settings of learning" }
  - { number: "3.8", order: 96, componentType: practice, parent: "section 3", heading: "Teaching and learning", gloss: "learning methods students use" }
  - { number: "3.9", order: 97, componentType: paragraph, parent: "section 3", heading: "Teaching and learning", gloss: "mature learners and inclusive design" }
  - { number: "3.10", order: 98, componentType: practice, parent: "section 3", heading: "Assessment", gloss: "constructive alignment; varied assessment" }
  - { number: "3.11", order: 99, componentType: practice, parent: "section 3", heading: "Assessment", gloss: "authentic assessment recommended" }
  - { number: "3.12", order: 100, componentType: paragraph, parent: "section 3", heading: "Assessment", gloss: "independent competence, GenAI and misconduct" }
  - { number: "3.13", order: 101, componentType: practice, parent: "section 3", heading: "Assessment", gloss: "accessible, inclusive assessment principles" }
  - { number: "3.14", order: 102, componentType: practice, parent: "section 3", heading: "Assessment", gloss: "indicative assessment types" }
  - { number: "3.15", order: 103, componentType: practice, parent: "section 3", heading: "Assessment", gloss: "programme-level assessment diversity" }
  - { number: "3.16", order: 104, componentType: practice, parent: "section 3", heading: "Assessment", gloss: "feedback throughout studies" }
  - { number: "3.17", order: 105, componentType: paragraph, parent: "section 3", heading: "Assessment", gloss: "feedback on strengths for work" }
  - { number: "4.1", order: 107, componentType: paragraph, parent: "section 4", heading: "Introduction", gloss: "what the standards cover, by level" }
  - { number: "4.2", order: 108, componentType: paragraph, parent: "section 4", heading: "Introduction", gloss: "the three rungs defined by class" }
  - { number: "4.3", order: 109, componentType: paragraph, parent: "section 4", heading: "Introduction", gloss: "performance above typical; Annex D" }
  - { number: "4.4", order: 110, componentType: paragraph, parent: "section 4", heading: "Introduction", gloss: "not competence standards; EHRC guidance" }
  - { number: "4.5", order: 111, componentType: stem, parent: "section 4", heading: "Undergraduate programmes", gloss: "honours outcomes in line with the Frameworks" }
  - { number: "4.6", order: 112, componentType: paragraph, parent: "section 4", heading: "Undergraduate programmes", gloss: "not a checklist; rungs cumulative" }
  - { number: "4.7", order: 113, componentType: paragraph, parent: "section 4", heading: "Undergraduate programmes", gloss: "knowledge and understanding table" }
  - { number: "4.8", order: 114, componentType: paragraph, parent: "section 4", heading: "Undergraduate programmes", gloss: "subject-specific skills table" }
  - { number: "4.9", order: 115, componentType: paragraph, parent: "section 4", heading: "Undergraduate programmes", gloss: "generic intellectual skills table" }
  - { number: "4.10", order: 116, componentType: paragraph, parent: "section 4", heading: "Undergraduate programmes", gloss: "generic transferable skills table" }
  - { number: "4.11", order: 117, componentType: paragraph, parent: "section 4", heading: "Master's programmes", gloss: "master's standards; not a checklist" }
  - { number: "4.12", order: 118, componentType: stem, parent: "section 4", heading: "Master's programmes", gloss: "master's knowledge and understanding list" }
  - { number: "4.13", order: 119, componentType: stem, parent: "section 4", heading: "Master's programmes", gloss: "master's subject-specific skills list" }
  - { number: "4.14", order: 120, componentType: stem, parent: "section 4", heading: "Master's programmes", gloss: "master's generic intellectual skills list" }
  - { number: "4.15", order: 121, componentType: stem, parent: "section 4", heading: "Master's programmes", gloss: "master's generic transferable skills list" }
  - { number: "1", componentType: section, parent: none, heading: "Context and purposes of a Social Policy degree", gloss: "section 1" }
  - { number: "2", componentType: section, parent: none, heading: "Distinctive features of the Social Policy degree", gloss: "section 2" }
  - { number: "3", componentType: section, parent: none, heading: "Content, structure and delivery", gloss: "section 3" }
  - { number: "4", componentType: section, parent: none, heading: "Benchmark standards", gloss: "section 4" }
excluded:
  - { number: "none", heading: "Contents; About this Statement; How can I use this document?; Relationship to legislation; Additional sector reference points", kind: "other: front matter, read for S1, S2 and SB6" }
  - { number: "section headings 1 to 4", heading: "the four section heading lines and the lead paragraph of section 3", kind: "other: headings, recorded in SECTIONS" }
  - { number: "footnote 1", heading: "definition of polycrises (page 4)", kind: "other: footnote, read for Part B" }
  - { number: "5", heading: "List of references and further resources", kind: "other: back matter, read for SB6 and Part E" }
  - { number: "6", heading: "Membership of the Advisory Group (2026, 2019, 2016, 2007, 2000)", kind: "other: back matter, read for S7 and S8" }
  - { number: "none", heading: "Fifth Edition; Published 16 April 2026; copyright notice", kind: "other: colophon, read for S1 and S8" }
```

### S4 Statements
<!-- label: both; status: drafted; basis: primary. Only standards (D-std-0002 (a)): 167 records. `source` is the issuer's statement exactly as its span holds it (D-std-0014). -->
```yaml
- id: qaa/social-policy-2026/1.7
  locator: { number: "1.7", headingPath: ["Context and purposes of a Social Policy degree", "Context and purposes of a Social Policy degree"] }
  span: { start: 10781, end: 11027 }
  source: "Students should understand how social policy operates across local, national and international levels, including the principle of subsidiarity, emphasising the importance of addressing social needs at the most immediate level capable of doing so."
  stem: none
  statementType: expectation
  rung: none
  force: should
  level: fheq:6
  appliesTo: "Social Policy students"
  addressee: learner
  verbs: ["understand", "operates", "emphasising", "addressing"]
  about: "policy across levels; subsidiarity"
  themes: [none]
  domain: understanding
  award: ["bachelor's with honours"]
  gradeOf: none
  paraphrase: "Students should understand how social policy works at local, national and international levels, subsidiarity included: meeting needs at the closest level able to do so."
  quote: full   # the issuer's statement is in `source` (D-std-0014)
  audience: both
  subjects: inherited
- id: qaa/social-policy-2026/1.14
  locator: { number: "1.14", headingPath: ["Context and purposes of a Social Policy degree", "Context and purposes of a Social Policy degree"] }
  span: { start: 14537, end: 15146 }
  source: "1.14 Social policy must recognise the centrality of environmental sustainability in shaping welfare systems and future policy agendas. Traditional anthropocentric approaches, which prioritise human needs without considering ecological limits, risk exacerbating social and environmental inequalities. Embedding an understanding of the interdependence between human wellbeing and planetary health within the discipline ensures that graduates can critically engage with policies addressing climate change, energy transition and resource distribution, promoting sustainable and just outcomes for all communities.\n"
  stem: none
  statementType: requirement
  rung: none
  force: must
  level: none
  appliesTo: "the discipline and those who design its curricula"
  addressee: provider
  verbs: ["recognise", "shaping"]
  about: "environmental sustainability central to welfare"
  themes: [none]
  domain: none
  award: ["bachelor's with honours"]
  gradeOf: none
  paraphrase: "The subject must treat environmental sustainability as central to welfare systems and future policy; human-centred views that ignore ecological limits risk widening inequality, and teaching the tie between wellbeing and planetary health lets graduates engage critically with climate, energy and resource policy."
  quote: full   # the issuer's statement is in `source` (D-std-0014)
  audience: practitioner
  subjects: inherited
- id: qaa/social-policy-2026/1.17
  locator: { number: "1.17", headingPath: ["Context and purposes of a Social Policy degree", "Purposes and characteristics of a Social Policy degree"] }
  span: { start: 16239, end: 16407 }
  source: "Consequently, Social Policy students must develop an appreciation of the design, implementation and evaluation of social policies and broader theories of policy making."
  stem: none
  statementType: requirement
  rung: none
  force: must
  level: fheq:6
  appliesTo: "Social Policy students"
  addressee: learner
  verbs: ["develop"]
  about: "policy design, implementation, evaluation and theory"
  themes: [none]
  domain: understanding
  award: ["bachelor's with honours"]
  gradeOf: none
  paraphrase: "Students must come to appreciate how social policies are designed, put into practice and evaluated, and wider theories of how policy is made."
  quote: full   # the issuer's statement is in `source` (D-std-0014)
  audience: both
  subjects: inherited
- id: qaa/social-policy-2026/1.20
  locator: { number: "1.20", headingPath: ["Context and purposes of a Social Policy degree", "Purposes and characteristics of a Social Policy degree"] }
  span: { start: 17004, end: 17244 }
  source: "1.20 Social Policy is normatively focused; as such, its students should acknowledge their own individual values, the values of others and insights from research to inform their understanding of the subject and its practices and activities.\n"
  stem: none
  statementType: expectation
  rung: none
  force: should
  level: fheq:6
  appliesTo: "Social Policy students"
  addressee: learner
  verbs: ["acknowledge", "inform"]
  about: "own and others' values, with research"
  themes: [none]
  domain: generic-skill
  award: ["bachelor's with honours"]
  gradeOf: none
  paraphrase: "Because the subject is normative, students should recognise their own values, other people's values and research findings, and let these inform how they understand the subject."
  quote: full   # the issuer's statement is in `source` (D-std-0014)
  audience: both
  subjects: inherited
- id: qaa/social-policy-2026/1.24
  locator: { number: "1.24", headingPath: ["Context and purposes of a Social Policy degree", "Purposes and characteristics of a Social Policy degree"] }
  span: { start: 18475, end: 18831 }
  source: "1.24 Analysis is not purely historical but must also consider ongoing legacies and practices. Decolonial frameworks should also be applied in analysis of the internationalisation of social policy, and funding for social policy interventions by international organisations are often contingent on colonial ideas, values, interests, approaches and policies.\n"
  stem: none
  statementType: requirement
  rung: none
  force: must
  level: fheq:6
  appliesTo: "Social Policy students"
  addressee: both
  verbs: ["consider", "applied"]
  about: "colonial legacies in analysis"
  themes: [none]
  domain: understanding
  award: ["bachelor's with honours"]
  gradeOf: none
  paraphrase: "Analysis in the subject must look beyond history to the legacies and practices that continue; decolonial frameworks should also be used when analysing internationalised policy, since international funding often rests on colonial ideas and interests."
  quote: full   # the issuer's statement is in `source` (D-std-0014)
  audience: both
  subjects: inherited
- id: qaa/social-policy-2026/1.27
  locator: { number: "1.27", headingPath: ["Context and purposes of a Social Policy degree", "Purposes and characteristics of a Social Policy degree"] }
  span: { start: 19823, end: 20068 }
  source: "Teaching within the discipline should make efforts to diversify student learning through wider theories, knowledge and analyses which challenge the legacy of colonial and neocolonial assumptions and thinking often embedded within the discipline."
  stem: none
  statementType: expectation
  rung: none
  force: should
  level: none
  appliesTo: "those who teach the subject"
  addressee: provider
  verbs: ["diversify", "challenge"]
  about: "teaching that challenges colonial assumptions"
  themes: [none]
  domain: none
  award: ["bachelor's with honours"]
  gradeOf: none
  paraphrase: "Teaching should work to widen student learning with theories, knowledge and analyses that challenge the colonial and neocolonial assumptions long built into the discipline."
  quote: full   # the issuer's statement is in `source` (D-std-0014)
  audience: practitioner
  subjects: inherited
- id: qaa/social-policy-2026/1.29
  locator: { number: "1.29", headingPath: ["Context and purposes of a Social Policy degree", "Equity, diversity and inclusion"] }
  span: { start: 20540, end: 20794 }
  source: "Teaching of Social Policy should therefore be mindful of supporting students who may not have formally studied Social Policy but will have engaged with relevant key issues through lived experience and media coverage and public debates over social issues."
  stem: none
  statementType: expectation
  rung: none
  force: should
  level: none
  appliesTo: "teaching staff"
  addressee: provider
  verbs: ["supporting"]
  about: "support for students new to the subject"
  themes: [theme:edi]
  domain: none
  award: ["bachelor's with honours"]
  gradeOf: none
  paraphrase: "Since few students meet the subject before university, teaching should support those who have not studied it formally but know its issues from life, the media and public debate."
  quote: full   # the issuer's statement is in `source` (D-std-0014)
  audience: practitioner
  subjects: inherited
- id: qaa/social-policy-2026/1.31
  locator: { number: "1.31", headingPath: ["Context and purposes of a Social Policy degree", "Equity, diversity and inclusion"] }
  span: { start: 21324, end: 21875 }
  source: "1.31 Social Policy programme, teaching and learning design should reflect upon students' diverse needs. Provision should ensure that appropriate support is available, and efforts are made to address awarding gaps – starting with protected characteristics under the Equality Act 2010 and relevant equality legislation in Northern Ireland (including socio-economic status) and broadening to all relevant categories of student and recognising that students may embody multiple identities which might impact on their ability to engage with the programme.\n"
  stem: none
  statementType: expectation
  rung: none
  force: should
  level: none
  appliesTo: "those who design programmes and provision"
  addressee: provider
  verbs: ["reflect", "ensure"]
  about: "design for diverse needs; awarding gaps"
  themes: [theme:edi]
  domain: none
  award: ["bachelor's with honours"]
  gradeOf: none
  paraphrase: "Programme, teaching and learning design should take account of students' varied needs; provision should make sure support is in place and act on awarding gaps, starting from protected characteristics and widening to other groups, aware that students hold several identities at once."
  quote: full   # the issuer's statement is in `source` (D-std-0014)
  audience: practitioner
  subjects: inherited
- id: qaa/social-policy-2026/1.36
  locator: { number: "1.36", headingPath: ["Context and purposes of a Social Policy degree", "Equity, diversity and inclusion"] }
  span: { start: 23089, end: 23241 }
  source: "1.36 Programme, teaching and assessment design should adhere to good EDI practices, such as the QAA resource on Creating Inclusive Subject Communities.\n"
  stem: none
  statementType: expectation
  rung: none
  force: should
  level: none
  appliesTo: "those who design programmes, teaching and assessment"
  addressee: provider
  verbs: ["adhere"]
  about: "good EDI practice in design"
  themes: [theme:edi]
  domain: none
  award: ["bachelor's with honours"]
  gradeOf: none
  paraphrase: "Programme, teaching and assessment design should follow good practice on equity, diversity and inclusion, such as QAA's advice on inclusive subject communities."
  quote: full   # the issuer's statement is in `source` (D-std-0014)
  audience: practitioner
  subjects: inherited
- id: qaa/social-policy-2026/1.39
  locator: { number: "1.39", headingPath: ["Context and purposes of a Social Policy degree", "Equity, diversity and inclusion"] }
  span: { start: 23921, end: 24468 }
  source: "1.39 Social Policy graduates will be able to effectively reflect on how their work is inclusive of diversity, and how their own life experiences and identity may shape their viewpoints and approaches. In positions of leadership, Social Policy graduates understand the value of diversity in effective team-working and problem-solving, how their own background and experiences may influence their decision-making and demonstrate professional values of equity and inclusion in their work with others. Accessibility and the needs of disabled students\n"
  stem: none
  statementType: outcome
  rung: none
  force: will
  level: fheq:6
  appliesTo: "Social Policy students"
  addressee: learner
  verbs: ["reflect", "understand", "demonstrate"]
  about: "inclusive, reflexive practice"
  themes: [theme:edi]
  domain: generic-skill
  award: ["bachelor's with honours"]
  gradeOf: none
  paraphrase: "Graduates will be able to reflect on how inclusive their work is and how their own experience and identity shape their views; as leaders they understand the value of diversity in teams and how their background affects their decisions, and show equity and inclusion in working with others."
  quote: full   # the issuer's statement is in `source` (D-std-0014)
  audience: both
  subjects: inherited
- id: qaa/social-policy-2026/1.42.b1
  locator: { number: "1.42.b1", headingPath: ["Context and purposes of a Social Policy degree", "Accessibility and the needs of disabled students"] }
  span: { start: 25698, end: 25849 }
  source: "Programme design should integrate diverse modes of teaching and assessment types, to engage students in their learning through a variety of approaches."
  stem: "1.42"
  statementType: expectation
  rung: none
  force: should
  level: none
  appliesTo: "the provider"
  addressee: provider
  verbs: ["integrate", "engage"]
  about: "varied teaching and assessment modes"
  themes: [theme:accessibility]
  domain: none
  award: ["bachelor's with honours"]
  gradeOf: none
  paraphrase: "Programme design should combine varied teaching modes and assessment types so students engage through many approaches."
  quote: full   # the issuer's statement is in `source` (D-std-0014)
  audience: practitioner
  subjects: inherited
- id: qaa/social-policy-2026/1.42.b2
  locator: { number: "1.42.b2", headingPath: ["Context and purposes of a Social Policy degree", "Accessibility and the needs of disabled students"] }
  span: { start: 25852, end: 25957 }
  source: "Clear information is given to students from the start with regards to expectations and available support."
  stem: "1.42"
  statementType: expectation
  rung: none
  force: should
  level: none
  appliesTo: "the provider"
  addressee: provider
  verbs: ["given"]
  about: "clear early information on expectations and support"
  themes: [theme:accessibility]
  domain: none
  award: ["bachelor's with honours"]
  gradeOf: none
  paraphrase: "Students should get clear information from the outset about what is expected and what support exists."
  quote: full   # the issuer's statement is in `source` (D-std-0014)
  audience: practitioner
  subjects: inherited
- id: qaa/social-policy-2026/1.42.b3
  locator: { number: "1.42.b3", headingPath: ["Context and purposes of a Social Policy degree", "Accessibility and the needs of disabled students"] }
  span: { start: 25960, end: 26112 }
  source: "Full access to adequate learning resources, including assistive technology, is given to students with disabilities to support their individual learning."
  stem: "1.42"
  statementType: expectation
  rung: none
  force: should
  level: none
  appliesTo: "the provider"
  addressee: provider
  verbs: ["given", "support"]
  about: "resources and assistive technology for disabled students"
  themes: [theme:accessibility]
  domain: none
  award: ["bachelor's with honours"]
  gradeOf: none
  paraphrase: "Disabled students should have full access to adequate learning resources, assistive technology included, to support their learning."
  quote: full   # the issuer's statement is in `source` (D-std-0014)
  audience: practitioner
  subjects: inherited
- id: qaa/social-policy-2026/1.42.b4
  locator: { number: "1.42.b4", headingPath: ["Context and purposes of a Social Policy degree", "Accessibility and the needs of disabled students"] }
  span: { start: 26115, end: 26357 }
  source: "For assessments, reasonable adjustment is available to students through clearly communicated channels, enabling students to access alternative assessments and/or\n\n8\nobtain additional support to create equitable learning opportunities for all."
  stem: "1.42"
  statementType: expectation
  rung: none
  force: should
  level: none
  appliesTo: "the provider"
  addressee: provider
  verbs: ["enabling", "access", "obtain", "create"]
  about: "reasonable adjustment in assessment"
  themes: [theme:accessibility]
  domain: none
  award: ["bachelor's with honours"]
  gradeOf: none
  paraphrase: "Reasonable adjustment in assessment should be available through clearly communicated routes, so students can take alternative assessments or get extra support for fair opportunities."
  quote: full   # the issuer's statement is in `source` (D-std-0014)
  audience: practitioner
  subjects: inherited
- id: qaa/social-policy-2026/1.43
  locator: { number: "1.43", headingPath: ["Context and purposes of a Social Policy degree", "Accessibility and the needs of disabled students"] }
  span: { start: 26431, end: 26729 }
  source: "1.43 Where placements are a component of the curriculum, additional support should be provided to any students with disabilities who may face barriers in accessing such placements, and alternative forms of work-based learning ought to be offered if necessary. Education for sustainable development\n"
  stem: none
  statementType: expectation
  rung: none
  force: should
  level: none
  appliesTo: "the provider, where placements are in the curriculum"
  addressee: provider
  verbs: ["provided", "face", "offered"]
  about: "placement support for disabled students"
  themes: [theme:accessibility]
  domain: none
  award: ["bachelor's with honours"]
  gradeOf: none
  paraphrase: "Where placements are part of the curriculum, disabled students who face barriers to them should get extra support, with other work-based learning offered if needed."
  quote: full   # the issuer's statement is in `source` (D-std-0014)
  audience: practitioner
  subjects: inherited
- id: qaa/social-policy-2026/1.48
  locator: { number: "1.48", headingPath: ["Context and purposes of a Social Policy degree", "Education for sustainable development"] }
  span: { start: 27903, end: 28327 }
  source: "1.48 Students of Social Policy should have opportunity to explore the unique and essential role of welfare provision and its relationship to, for example, labour markets and the economy in shaping the consequences of human action on the natural environment. This can include awareness of how welfare policies will need to be reformed to address future challenges arising from climate, demographic and technological changes.\n"
  stem: none
  statementType: expectation
  rung: none
  force: should
  level: none
  appliesTo: "the course"
  addressee: provider
  verbs: ["explore", "shaping"]
  about: "welfare, economy and the environment"
  themes: [theme:esd]
  domain: none
  award: ["bachelor's with honours"]
  gradeOf: none
  paraphrase: "Students should have the chance to explore how welfare provision, with labour markets and the economy, shapes what human action does to the natural environment, including how welfare may need reform for climate, demographic and technological change."
  quote: full   # the issuer's statement is in `source` (D-std-0014)
  audience: practitioner
  subjects: inherited
- id: qaa/social-policy-2026/1.50
  locator: { number: "1.50", headingPath: ["Context and purposes of a Social Policy degree", "Education for sustainable development"] }
  span: { start: 28901, end: 29110 }
  source: "Additionally, attention should be given to the Inner Development Goals: to better identify, understand, develop, integrate and communicate the personal skills and attributes needed for sustainable development."
  stem: none
  statementType: expectation
  rung: none
  force: should
  level: none
  appliesTo: "those who design programmes"
  addressee: provider
  verbs: ["given"]
  about: "the Inner Development Goals"
  themes: [theme:esd]
  domain: none
  award: ["bachelor's with honours"]
  gradeOf: none
  paraphrase: "Attention should also go to the Inner Development Goals, to help identify, build and communicate the personal skills and qualities that sustainable development needs."
  quote: full   # the issuer's statement is in `source` (D-std-0014)
  audience: practitioner
  subjects: inherited
- id: qaa/social-policy-2026/1.52
  locator: { number: "1.52", headingPath: ["Context and purposes of a Social Policy degree", "Education for sustainable development"] }
  span: { start: 29459, end: 30201 }
  source: "1.52 Social Policy can offer opportunities to investigate, debate and critique the concept of sustainability, the diverse ideological and political influences on the term and how it is pursued (or not) through social and wider public and economic policies. Inclusive within such analysis, attention should be given to the role of climate change in deepening privilege (for\n\n9\nexample racial, gender, economic, ability) on local, national and global scales as well as the implications of climate change for the development and delivery of welfare services. This can empower students with competencies and intellectual capabilities to support sustainability and ethical ways of living within their own lives and those of their wider community.\n"
  stem: none
  statementType: expectation
  rung: none
  force: should
  level: none
  appliesTo: "those who teach sustainability"
  addressee: provider
  verbs: ["investigate", "debate", "critique", "given", "empower", "support"]
  about: "critique of sustainability; climate and privilege"
  themes: [theme:esd]
  domain: none
  award: ["bachelor's with honours"]
  gradeOf: none
  paraphrase: "The subject can let students investigate, debate and critique sustainability and its politics; within this, attention should be given to how climate change deepens privilege by race, gender, wealth and ability, locally to globally, and what it means for welfare services."
  quote: full   # the issuer's statement is in `source` (D-std-0014)
  audience: practitioner
  subjects: inherited
- id: qaa/social-policy-2026/1.53
  locator: { number: "1.53", headingPath: ["Context and purposes of a Social Policy degree", "Education for sustainable development"] }
  span: { start: 30201, end: 30720 }
  source: "1.53 Sustainability should also be considered in relation to ongoing lifelong learning beyond the degree. Social Policy by its nature is engaged with ever-changing economic, political and social contexts. Such changes may prompt revisions in policy or be caused by policy implementation. Students should graduate with a broader skills set to be able to engage in ever-evolving policy debates with the critical thinking and analytical skills their degrees offer. Employability, entrepreneurship and enterprise education\n"
  stem: none
  statementType: expectation
  rung: none
  force: should
  level: fheq:6
  appliesTo: "Social Policy students"
  addressee: learner
  verbs: ["considered", "graduate", "engage"]
  about: "skills for lifelong policy debate"
  themes: [theme:esd]
  domain: generic-skill
  award: ["bachelor's with honours"]
  gradeOf: none
  paraphrase: "Sustainability also bears on learning after the degree: since policy contexts keep changing, students should graduate with broad skills to join shifting policy debates with critical and analytical thinking."
  quote: full   # the issuer's statement is in `source` (D-std-0014)
  audience: both
  subjects: inherited
- id: qaa/social-policy-2026/1.56
  locator: { number: "1.56", headingPath: ["Context and purposes of a Social Policy degree", "Employability, entrepreneurship and enterprise education"] }
  span: { start: 32379, end: 32559 }
  source: "Opportunities should also encourage students to apply disciplinary knowledge to employment contexts (whether through placements, authentic assessments or other relevant practices)."
  stem: none
  statementType: expectation
  rung: none
  force: should
  level: none
  appliesTo: "those who design programmes"
  addressee: provider
  verbs: ["encourage", "apply"]
  about: "applying knowledge to work contexts"
  themes: [theme:enterprise]
  domain: none
  award: ["bachelor's with honours"]
  gradeOf: none
  paraphrase: "Opportunities should also encourage students to use what they know of the subject in work settings, through placements, authentic assessment or similar."
  quote: full   # the issuer's statement is in `source` (D-std-0014)
  audience: practitioner
  subjects: inherited
- id: qaa/social-policy-2026/1.60
  locator: { number: "1.60", headingPath: ["Context and purposes of a Social Policy degree", "Generative artificial intelligence"] }
  span: { start: 34179, end: 34545 }
  source: "1.60 Given the increasing relevance of generative artificial intelligence (GenAI) in professional and academic life, students of Social Policy should be provided with opportunities to critically engage with such tools, to develop skills for their ethical, effective and reflective use in future employment and (where permitted and appropriate) in academic contexts.\n"
  stem: none
  statementType: expectation
  rung: none
  force: should
  level: none
  appliesTo: "the course"
  addressee: provider
  verbs: ["provided", "engage", "develop"]
  about: "critical engagement with generative AI"
  themes: [theme:generative-ai]
  domain: none
  award: ["bachelor's with honours"]
  gradeOf: none
  paraphrase: "Given generative AI's growing place in work and study, students should be given chances to engage critically with it and learn to use it ethically, effectively and reflectively at work and, where allowed, in study."
  quote: full   # the issuer's statement is in `source` (D-std-0014)
  audience: practitioner
  subjects: inherited
- id: qaa/social-policy-2026/1.62.b5
  locator: { number: "1.62.b5", headingPath: ["Context and purposes of a Social Policy degree", "Generative artificial intelligence"] }
  span: { start: 35967, end: 36166 }
  source: "students should be informed about and encouraged to participate in debate around the ethical, legal, environmental and social consequences of GenAI, and social policy responses to these consequences."
  stem: "1.62"
  statementType: expectation
  rung: none
  force: should
  level: none
  appliesTo: "the course"
  addressee: provider
  verbs: ["informed", "encouraged", "participate"]
  about: "debate on the consequences of generative AI"
  themes: [theme:generative-ai]
  domain: none
  award: ["bachelor's with honours"]
  gradeOf: none
  paraphrase: "Students should be told about, and encouraged to join, debate on the ethical, legal, environmental and social effects of generative AI and on policy responses to them."
  quote: full   # the issuer's statement is in `source` (D-std-0014)
  audience: practitioner
  subjects: inherited
- id: qaa/social-policy-2026/1.65
  locator: { number: "1.65", headingPath: ["Context and purposes of a Social Policy degree", "Generative artificial intelligence"] }
  span: { start: 37247, end: 37501 }
  source: "1.65 Institutions will have their own policies on the use of GenAI to which Social Policy degrees programmes will have to adhere to. Within these usages, students should be taught about the risks, limitations and environmental consequences of GenAI use.\n"
  stem: none
  statementType: expectation
  rung: none
  force: should
  level: none
  appliesTo: "the course, within its institution's policy"
  addressee: provider
  verbs: ["adhere", "taught"]
  about: "institutional AI policy; teaching on risks"
  themes: [theme:generative-ai]
  domain: none
  award: ["bachelor's with honours"]
  gradeOf: none
  paraphrase: "Each institution will have its own generative AI policy that programmes have to follow; within it, students should be taught the risks, limits and environmental costs of using generative AI."
  quote: full   # the issuer's statement is in `source` (D-std-0014)
  audience: practitioner
  subjects: inherited
- id: qaa/social-policy-2026/2.1
  locator: { number: "2.1", headingPath: ["Distinctive features of the Social Policy degree", "Design"] }
  span: { start: 37945, end: 38232 }
  source: "Degrees in Social Policy should be designed so that students are able to address four fundamental questions in relation to any social problem: what is done by social policies, how is it done, why has this been done, and whether it should be done, who it is done to and who is it done by?"
  stem: none
  statementType: expectation
  rung: none
  force: should
  level: fheq:6
  appliesTo: "Social Policy students"
  addressee: both
  verbs: ["designed", "address"]
  about: "the core questions for any social problem"
  themes: [none]
  domain: subject-skill
  award: ["bachelor's with honours"]
  gradeOf: none
  paraphrase: "Degrees should be designed so students can put core questions to any social problem: what policy does, how, why, whether it should, to whom and by whom."
  quote: full   # the issuer's statement is in `source` (D-std-0014)
  audience: both
  subjects: inherited
- id: qaa/social-policy-2026/2.2.b1
  locator: { number: "2.2.b1", headingPath: ["Distinctive features of the Social Policy degree", "Design"] }
  span: { start: 38313, end: 38414 }
  source: "a distinct focus on the concept of welfare, welfare systems and entitlement to access welfare support"
  stem: "2.2"
  statementType: expectation
  rung: none
  force: should
  level: none
  appliesTo: "programme designers"
  addressee: provider
  verbs: []
  about: "welfare, welfare systems and entitlement"
  themes: [none]
  domain: none
  award: ["bachelor's with honours"]
  gradeOf: none
  paraphrase: "Programme design should focus clearly on the concept of welfare, welfare systems and who is entitled to support."
  quote: full   # the issuer's statement is in `source` (D-std-0014)
  audience: practitioner
  subjects: inherited
- id: qaa/social-policy-2026/2.2.b2
  locator: { number: "2.2.b2", headingPath: ["Distinctive features of the Social Policy degree", "Design"] }
  span: { start: 38417, end: 38567 }
  source: "a specific focus on policies directed to and impacting upon social welfare, for example, in relation to social security, health, education and housing"
  stem: "2.2"
  statementType: expectation
  rung: none
  force: should
  level: none
  appliesTo: "programme designers"
  addressee: provider
  verbs: ["directed", "impacting"]
  about: "policies that bear on welfare"
  themes: [none]
  domain: none
  award: ["bachelor's with honours"]
  gradeOf: none
  paraphrase: "Design should focus on policies aimed at or affecting social welfare, such as social security, health, education and housing."
  quote: full   # the issuer's statement is in `source` (D-std-0014)
  audience: practitioner
  subjects: inherited
- id: qaa/social-policy-2026/2.2.b3
  locator: { number: "2.2.b3", headingPath: ["Distinctive features of the Social Policy degree", "Design"] }
  span: { start: 38570, end: 38637 }
  source: "the rigorous linking of theoretical analysis with empirical enquiry"
  stem: "2.2"
  statementType: expectation
  rung: none
  force: should
  level: none
  appliesTo: "programme designers"
  addressee: provider
  verbs: ["linking"]
  about: "theory tied to empirical enquiry"
  themes: [none]
  domain: none
  award: ["bachelor's with honours"]
  gradeOf: none
  paraphrase: "Design should tie theoretical analysis rigorously to empirical enquiry."
  quote: full   # the issuer's statement is in `source` (D-std-0014)
  audience: practitioner
  subjects: inherited
- id: qaa/social-policy-2026/2.2.b4
  locator: { number: "2.2.b4", headingPath: ["Distinctive features of the Social Policy degree", "Design"] }
  span: { start: 38640, end: 38803 }
  source: "the identification and understanding of different value positions, ideologies and evidence bases which inform welfare debates, and policy design and implementation"
  stem: "2.2"
  statementType: expectation
  rung: none
  force: should
  level: none
  appliesTo: "programme designers"
  addressee: provider
  verbs: ["inform"]
  about: "values, ideologies and evidence in welfare debate"
  themes: [none]
  domain: none
  award: ["bachelor's with honours"]
  gradeOf: none
  paraphrase: "Design should help students identify and understand the values, ideologies and evidence that shape welfare debates and policy design and delivery."
  quote: full   # the issuer's statement is in `source` (D-std-0014)
  audience: practitioner
  subjects: inherited
- id: qaa/social-policy-2026/2.2.b5
  locator: { number: "2.2.b5", headingPath: ["Distinctive features of the Social Policy degree", "Design"] }
  span: { start: 38806, end: 38970 }
  source: "the development of academic and practical knowledge regarding the development, implementation and evaluation of policies designed to influence social circumstances."
  stem: "2.2"
  statementType: expectation
  rung: none
  force: should
  level: none
  appliesTo: "programme designers"
  addressee: provider
  verbs: ["designed", "influence"]
  about: "knowledge of policy making and evaluation"
  themes: [none]
  domain: none
  award: ["bachelor's with honours"]
  gradeOf: none
  paraphrase: "Design should build academic and practical knowledge of how policies meant to change social conditions are developed, carried out and evaluated."
  quote: full   # the issuer's statement is in `source` (D-std-0014)
  audience: practitioner
  subjects: inherited
- id: qaa/social-policy-2026/2.3.b1
  locator: { number: "2.3.b1", headingPath: ["Distinctive features of the Social Policy degree", "Design"] }
  span: { start: 39490, end: 39554 }
  source: "how social issues are conceived, and social problems constructed"
  stem: "2.3"
  statementType: expectation
  rung: none
  force: should
  level: fheq:6
  appliesTo: "Social Policy students"
  addressee: learner
  verbs: ["conceived", "constructed"]
  about: "how issues and problems are constructed"
  themes: [none]
  domain: subject-skill
  award: ["bachelor's with honours"]
  gradeOf: none
  paraphrase: "Students should be able to identify, apply and critique ideas of how social issues come to be understood and social problems built."
  quote: full   # the issuer's statement is in `source` (D-std-0014)
  audience: both
  subjects: inherited
- id: qaa/social-policy-2026/2.3.b2
  locator: { number: "2.3.b2", headingPath: ["Distinctive features of the Social Policy degree", "Design"] }
  span: { start: 39557, end: 39615 }
  source: "how interventions are justified, and provision established"
  stem: "2.3"
  statementType: expectation
  rung: none
  force: should
  level: fheq:6
  appliesTo: "Social Policy students"
  addressee: learner
  verbs: ["justified", "established"]
  about: "justifying interventions and provision"
  themes: [none]
  domain: subject-skill
  award: ["bachelor's with honours"]
  gradeOf: none
  paraphrase: "Students should be able to identify, apply and critique how interventions are justified and provision set up."
  quote: full   # the issuer's statement is in `source` (D-std-0014)
  audience: both
  subjects: inherited
- id: qaa/social-policy-2026/2.3.b3
  locator: { number: "2.3.b3", headingPath: ["Distinctive features of the Social Policy degree", "Design"] }
  span: { start: 39618, end: 39717 }
  source: "the resource distribution, design and administration of interventions and assess their consequences"
  stem: "2.3"
  statementType: expectation
  rung: none
  force: should
  level: fheq:6
  appliesTo: "Social Policy students"
  addressee: learner
  verbs: ["assess"]
  about: "resourcing, design and effects of interventions"
  themes: [none]
  domain: subject-skill
  award: ["bachelor's with honours"]
  gradeOf: none
  paraphrase: "Students should be able to identify, apply and critique how interventions are funded, designed and run, and assess their effects."
  quote: full   # the issuer's statement is in `source` (D-std-0014)
  audience: both
  subjects: inherited
- id: qaa/social-policy-2026/2.3.b4
  locator: { number: "2.3.b4", headingPath: ["Distinctive features of the Social Policy degree", "Design"] }
  span: { start: 39720, end: 39967 }
  source: "the historic, environmental, global/international factors and discriminatory attitudes and policies which influence welfare provision, adopting a multi-sectoral approach which gives attention beyond the state to other providers of welfare support."
  stem: "2.3"
  statementType: expectation
  rung: none
  force: should
  level: fheq:6
  appliesTo: "Social Policy students"
  addressee: learner
  verbs: ["influence", "adopting", "gives"]
  about: "historical, environmental, global and discriminatory forces; beyond the state"
  themes: [none]
  domain: subject-skill
  award: ["bachelor's with honours"]
  gradeOf: none
  paraphrase: "Students should be able to identify, apply and critique the historical, environmental, global and discriminatory forces behind welfare provision, looking beyond the state to other providers."
  quote: full   # the issuer's statement is in `source` (D-std-0014)
  audience: both
  subjects: inherited
- id: qaa/social-policy-2026/2.4.b1
  locator: { number: "2.4.b1", headingPath: ["Distinctive features of the Social Policy degree", "Design"] }
  span: { start: 40474, end: 40533 }
  source: "conduct policy analysis across varied professional settings"
  stem: "2.4"
  statementType: expectation
  rung: none
  force: should
  level: fheq:6
  appliesTo: "Social Policy students"
  addressee: learner
  verbs: ["conduct"]
  about: "policy analysis in varied settings"
  themes: [none]
  domain: subject-skill
  award: ["bachelor's with honours"]
  gradeOf: none
  paraphrase: "Students should have the skills and knowledge to analyse policy in a range of professional settings."
  quote: full   # the issuer's statement is in `source` (D-std-0014)
  audience: both
  subjects: inherited
- id: qaa/social-policy-2026/2.4.b2
  locator: { number: "2.4.b2", headingPath: ["Distinctive features of the Social Policy degree", "Design"] }
  span: { start: 40536, end: 40673 }
  source: "communicate research and recommendations in a variety of formats suitable to professional, policy-orientated professions and lay audience"
  stem: "2.4"
  statementType: expectation
  rung: none
  force: should
  level: fheq:6
  appliesTo: "Social Policy students"
  addressee: learner
  verbs: ["communicate"]
  about: "communicating research to varied audiences"
  themes: [none]
  domain: generic-skill
  award: ["bachelor's with honours"]
  gradeOf: none
  paraphrase: "Students should be able to communicate research and recommendations in formats fit for professional, policy and lay audiences."
  quote: full   # the issuer's statement is in `source` (D-std-0014)
  audience: both
  subjects: inherited
- id: qaa/social-policy-2026/2.4.b3
  locator: { number: "2.4.b3", headingPath: ["Distinctive features of the Social Policy degree", "Design"] }
  span: { start: 40676, end: 40753 }
  source: "develop innovative solutions to enhance individual and/or collective welfare."
  stem: "2.4"
  statementType: expectation
  rung: none
  force: should
  level: fheq:6
  appliesTo: "Social Policy students"
  addressee: learner
  verbs: ["develop", "enhance"]
  about: "innovative solutions for welfare"
  themes: [none]
  domain: subject-skill
  award: ["bachelor's with honours"]
  gradeOf: none
  paraphrase: "Students should be able to devise new solutions to improve individual or shared welfare."
  quote: full   # the issuer's statement is in `source` (D-std-0014)
  audience: both
  subjects: inherited
- id: qaa/social-policy-2026/2.5
  locator: { number: "2.5", headingPath: ["Distinctive features of the Social Policy degree", "Design"] }
  span: { start: 40965, end: 41128 }
  source: "Understanding should include awareness of multi-sectoral nature of providing welfare and how provision is developed in national, international and global contexts."
  stem: none
  statementType: expectation
  rung: none
  force: should
  level: fheq:6
  appliesTo: "Social Policy students"
  addressee: learner
  verbs: ["include", "developed"]
  about: "welfare from several sectors across contexts"
  themes: [none]
  domain: understanding
  award: ["bachelor's with honours"]
  gradeOf: none
  paraphrase: "Students' understanding should include awareness that welfare is provided by several sectors and how provision develops nationally, internationally and globally."
  quote: full   # the issuer's statement is in `source` (D-std-0014)
  audience: both
  subjects: inherited
- id: qaa/social-policy-2026/2.6
  locator: { number: "2.6", headingPath: ["Distinctive features of the Social Policy degree", "Design"] }
  span: { start: 41681, end: 41914 }
  source: "Programmes should aim to embed reflective practice alongside interpersonal skills such as communication and conflict resolution which will strengthen students' capacity to navigate the complexities of service delivery and governance."
  stem: none
  statementType: expectation
  rung: none
  force: should
  level: none
  appliesTo: "programme teams"
  addressee: provider
  verbs: ["embed", "strengthen", "navigate"]
  about: "reflective practice and interpersonal skills"
  themes: [none]
  domain: none
  award: ["bachelor's with honours"]
  gradeOf: none
  paraphrase: "Programmes should aim to build in reflective practice and interpersonal skills like communication and conflict resolution, to help students handle complex service delivery and governance."
  quote: full   # the issuer's statement is in `source` (D-std-0014)
  audience: practitioner
  subjects: inherited
- id: qaa/social-policy-2026/2.7
  locator: { number: "2.7", headingPath: ["Distinctive features of the Social Policy degree", "Design"] }
  span: { start: 41919, end: 41999 }
  source: "Review of programme design and provision should integrate student contributions."
  stem: none
  statementType: expectation
  rung: none
  force: should
  level: none
  appliesTo: "programme teams"
  addressee: provider
  verbs: ["integrate"]
  about: "student voice in programme review"
  themes: [none]
  domain: none
  award: ["bachelor's with honours"]
  gradeOf: none
  paraphrase: "Reviews of programme design and provision should take in students' contributions, through evaluations, staff-student meetings and co-production."
  quote: full   # the issuer's statement is in `source` (D-std-0014)
  audience: practitioner
  subjects: inherited
- id: qaa/social-policy-2026/2.8
  locator: { number: "2.8", headingPath: ["Distinctive features of the Social Policy degree", "Progression"] }
  span: { start: 42219, end: 42960 }
  source: "2.8 Over the course of a standard undergraduate degree with honours (FHEQ Level 6; FQHEIS Level 10) or, if available, an integrated master's degree (FHEQ Level 7; FQHEIS Level 11) a Social Policy student will progress from one level of study to the next, in line with the regulations and processes for each institution. However, it is expected that each level would see an attainment of knowledge, expertise and experience that builds towards the final achievement of meeting the threshold (and, if specified, higher-level) subject-specific and generic skills listed in this Statement. This will usually include successful completion and the award of credit for the full range of learning and assessment, including any practical components.\n"
  stem: none
  statementType: expectation
  rung: none
  force: will
  level: fheq:6
  appliesTo: "honours and integrated master's students"
  addressee: learner
  verbs: ["progress", "include"]
  about: "progression through the levels to the threshold"
  themes: [none]
  domain: none
  award: ["bachelor's with honours", "integrated master's"]
  gradeOf: none
  paraphrase: "A student will move from level to level under each institution's rules, each level building towards the threshold (and any higher) subject and generic skills; this will usually mean completing and gaining credit for all learning and assessment, practical parts included."
  quote: full   # the issuer's statement is in `source` (D-std-0014)
  audience: both
  subjects: inherited
- id: qaa/social-policy-2026/2.10
  locator: { number: "2.10", headingPath: ["Distinctive features of the Social Policy degree", "Progression"] }
  span: { start: 43334, end: 43816 }
  source: "2.10 Undergraduates studying Social Policy courses as part of a combined or joint degree with other subjects (including courses that specify major and minor options) will achieve core elements of the specific and generic skills outlined in this Statement and will add others according to the areas covered in the other subject(s) of their degree. Additionally, they may explore the overlaps between different disciplines, creating further opportunities for interdisciplinary study.\n"
  stem: none
  statementType: outcome
  rung: none
  force: will
  level: fheq:6
  appliesTo: "undergraduates taking the subject in joint or combined degrees"
  addressee: learner
  verbs: ["achieve", "add", "explore"]
  about: "joint and combined degrees"
  themes: [none]
  domain: none
  award: ["bachelor's with honours"]
  gradeOf: none
  paraphrase: "Undergraduates taking the subject in a joint or combined degree will achieve the core subject and generic skills set out here and add others from their other subject; they may also explore where the disciplines overlap."
  quote: full   # the issuer's statement is in `source` (D-std-0014)
  audience: both
  subjects: inherited
- id: qaa/social-policy-2026/2.15
  locator: { number: "2.15", headingPath: ["Distinctive features of the Social Policy degree", "Monitoring and review"] }
  span: { start: 46363, end: 46587 }
  source: "Degree-awarding bodies, and their collaborative partnerships, routinely collect and analyse information and undertake periodic course review according to their own needs. Considering the student voice will form part of this."
  stem: none
  statementType: expectation
  rung: none
  force: will
  level: none
  appliesTo: "degree-awarding bodies and their partners"
  addressee: provider
  verbs: ["collect", "analyse", "undertake", "form"]
  about: "periodic review with the student voice"
  themes: [none]
  domain: none
  award: ["bachelor's with honours"]
  gradeOf: none
  paraphrase: "Degree-awarding bodies and their partners gather and analyse information and review courses periodically; the student voice will be part of this."
  quote: full   # the issuer's statement is in `source` (D-std-0014)
  audience: practitioner
  subjects: inherited
- id: qaa/social-policy-2026/2.16
  locator: { number: "2.16", headingPath: ["Distinctive features of the Social Policy degree", "Monitoring and review"] }
  span: { start: 47004, end: 47303 }
  source: "2.16 Externality is an essential component of the quality assurance system in the UK. Providers will use external reviewers as part of periodic review to gain an independent perspective on any proposed changes and ensure threshold standards are achieved, and content is appropriate for the subject.\n"
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
- id: qaa/social-policy-2026/3.3.b1
  locator: { number: "3.3.b1", headingPath: ["Content, structure and delivery", "Content"] }
  span: { start: 50355, end: 50522 }
  source: "the origins and development of welfare institutions within as well as beyond the UK, and the economic, social, demographic and political contexts in which they operate"
  stem: "3.3"
  statementType: outcome
  rung: none
  force: describes
  level: fheq:6
  appliesTo: "graduates of Social Policy courses"
  addressee: learner
  verbs: ["operate"]
  about: "origins of welfare institutions and their settings"
  themes: [none]
  domain: knowledge
  award: ["bachelor's with honours"]
  gradeOf: none
  paraphrase: "Graduates show knowledge of how welfare institutions arose and grew in the UK and elsewhere, and their economic, social, demographic and political settings."
  quote: full   # the issuer's statement is in `source` (D-std-0014)
  audience: both
  subjects: inherited
- id: qaa/social-policy-2026/3.3.b2
  locator: { number: "3.3.b2", headingPath: ["Content, structure and delivery", "Content"] }
  span: { start: 50525, end: 50803 }
  source: "historical forces that have shaped entrenched patterns of discrimination – such as colonialism, capitalism and industrialisation, and the differential treatment of marginalised groups – and how these legacies continue to have profound influence on contemporary welfare provision"
  stem: "3.3"
  statementType: outcome
  rung: none
  force: describes
  level: fheq:6
  appliesTo: "graduates of Social Policy courses"
  addressee: learner
  verbs: ["shaped", "continue"]
  about: "historical roots of discrimination in welfare"
  themes: [none]
  domain: knowledge
  award: ["bachelor's with honours"]
  gradeOf: none
  paraphrase: "Graduates show knowledge of the historical forces, colonialism, capitalism and industrialisation among them, behind lasting discrimination, and how their legacy still shapes welfare."
  quote: full   # the issuer's statement is in `source` (D-std-0014)
  audience: both
  subjects: inherited
- id: qaa/social-policy-2026/3.3.b3
  locator: { number: "3.3.b3", headingPath: ["Content, structure and delivery", "Content"] }
  span: { start: 50806, end: 51012 }
  source: "the dynamics of social change, such as environmental sustainability and climate change, globalisation, internationalisation and trans-nationalisation; mass and social media, and the role of social movements"
  stem: "3.3"
  statementType: outcome
  rung: none
  force: describes
  level: fheq:6
  appliesTo: "graduates of Social Policy courses"
  addressee: learner
  verbs: []
  about: "drivers of social change"
  themes: [none]
  domain: knowledge
  award: ["bachelor's with honours"]
  gradeOf: none
  paraphrase: "Graduates show knowledge of drivers of social change such as climate change, sustainability, globalisation, the media and social movements."
  quote: full   # the issuer's statement is in `source` (D-std-0014)
  audience: both
  subjects: inherited
- id: qaa/social-policy-2026/3.3.b4
  locator: { number: "3.3.b4", headingPath: ["Content, structure and delivery", "Content"] }
  span: { start: 51015, end: 51279 }
  source: "the role, remit, organisation and contemporary activities of the main institutions of UK and global welfare systems, typically including the changing provision, financing and regulation of social security, education, employment, health and social care, and housing"
  stem: "3.3"
  statementType: outcome
  rung: none
  force: describes
  level: fheq:6
  appliesTo: "graduates of Social Policy courses"
  addressee: learner
  verbs: []
  about: "main welfare institutions and their work"
  themes: [none]
  domain: knowledge
  award: ["bachelor's with honours"]
  gradeOf: none
  paraphrase: "Graduates show knowledge of what the main UK and global welfare institutions do and how they are organised, funded and regulated across security, education, work, health, care and housing."
  quote: full   # the issuer's statement is in `source` (D-std-0014)
  audience: both
  subjects: inherited
- id: qaa/social-policy-2026/3.3.b5
  locator: { number: "3.3.b5", headingPath: ["Content, structure and delivery", "Content"] }
  span: { start: 51286, end: 51524 }
  source: "the universal features of welfare institutions and their common challenges in global contexts with regards to efficacy, equity, sustainability and political support/opposition, drawing on insights from comparative and global social policy"
  stem: "3.3"
  statementType: outcome
  rung: none
  force: describes
  level: fheq:6
  appliesTo: "graduates of Social Policy courses"
  addressee: learner
  verbs: ["drawing"]
  about: "shared features and challenges of welfare institutions"
  themes: [none]
  domain: knowledge
  award: ["bachelor's with honours"]
  gradeOf: none
  paraphrase: "Graduates show knowledge of common features and shared challenges of welfare institutions worldwide, in efficacy, equity, sustainability and political backing, from comparative study."
  quote: full   # the issuer's statement is in `source` (D-std-0014)
  audience: both
  subjects: inherited
- id: qaa/social-policy-2026/3.3.b6
  locator: { number: "3.3.b6", headingPath: ["Content, structure and delivery", "Content"] }
  span: { start: 51527, end: 51722 }
  source: "the ways in which countries organise their social policies and welfare institutions, the political modes through which they determine objectives and the effectiveness with which they realise them"
  stem: "3.3"
  statementType: outcome
  rung: none
  force: describes
  level: fheq:6
  appliesTo: "graduates of Social Policy courses"
  addressee: learner
  verbs: ["organise", "determine", "realise"]
  about: "how countries organise and pursue policy goals"
  themes: [none]
  domain: knowledge
  award: ["bachelor's with honours"]
  gradeOf: none
  paraphrase: "Graduates show knowledge of how countries organise their social policies and institutions, set goals politically and how well they meet them."
  quote: full   # the issuer's statement is in `source` (D-std-0014)
  audience: both
  subjects: inherited
- id: qaa/social-policy-2026/3.3.b7
  locator: { number: "3.3.b7", headingPath: ["Content, structure and delivery", "Content"] }
  span: { start: 51725, end: 52067 }
  source: "the role of global and national social policy in sustainability, environmental welfare, and the global climate crisis, including but not limited to sustainable growth (or degrowth) and development; energy and energy policy; and environmental injustices created by climate change across nations and communities (including climate displacement)"
  stem: "3.3"
  statementType: outcome
  rung: none
  force: describes
  level: fheq:6
  appliesTo: "graduates of Social Policy courses"
  addressee: learner
  verbs: []
  about: "policy in sustainability and the climate crisis"
  themes: [none]
  domain: knowledge
  award: ["bachelor's with honours"]
  gradeOf: none
  paraphrase: "Graduates show knowledge of the part policy plays, globally and nationally, in sustainability and the climate crisis, including growth or degrowth, energy and environmental injustice."
  quote: full   # the issuer's statement is in `source` (D-std-0014)
  audience: both
  subjects: inherited
- id: qaa/social-policy-2026/3.3.b8
  locator: { number: "3.3.b8", headingPath: ["Content, structure and delivery", "Content"] }
  span: { start: 52070, end: 52267 }
  source: "theoretical and conceptual ideas and principles driving the development of the subject, as well as key thinkers, with a critical awareness of the specific historical contexts in which they emerged."
  stem: "3.3"
  statementType: outcome
  rung: none
  force: describes
  level: fheq:6
  appliesTo: "graduates of Social Policy courses"
  addressee: learner
  verbs: ["driving", "emerged"]
  about: "ideas and thinkers of the subject in context"
  themes: [none]
  domain: knowledge
  award: ["bachelor's with honours"]
  gradeOf: none
  paraphrase: "Graduates show knowledge of the ideas, principles and key thinkers behind the subject, read in the historical settings that produced them."
  quote: full   # the issuer's statement is in `source` (D-std-0014)
  audience: both
  subjects: inherited
- id: qaa/social-policy-2026/3.3.b9
  locator: { number: "3.3.b9", headingPath: ["Content, structure and delivery", "Content"] }
  span: { start: 52349, end: 52537 }
  source: "the framework, operations and financing of the processes of policy making and implementation, with regards to the complex interplay of multiple stakeholders at diverse levels of governance"
  stem: "3.3"
  statementType: outcome
  rung: none
  force: describes
  level: fheq:6
  appliesTo: "graduates of Social Policy courses"
  addressee: learner
  verbs: []
  about: "framework and financing of policy processes"
  themes: [none]
  domain: knowledge
  award: ["bachelor's with honours"]
  gradeOf: none
  paraphrase: "Graduates show knowledge of how policy making and implementation are framed, run and funded, with many stakeholders at several levels of government."
  quote: full   # the issuer's statement is in `source` (D-std-0014)
  audience: both
  subjects: inherited
- id: qaa/social-policy-2026/3.3.b10
  locator: { number: "3.3.b10", headingPath: ["Content, structure and delivery", "Content"] }
  span: { start: 52540, end: 52732 }
  source: "subnational and supranational dimensions of social policy and the influence of international organisations on the conceptualisation of social policy problems and the design of policy solutions"
  stem: "3.3"
  statementType: outcome
  rung: none
  force: describes
  level: fheq:6
  appliesTo: "graduates of Social Policy courses"
  addressee: learner
  verbs: []
  about: "subnational and supranational policy; international organisations"
  themes: [none]
  domain: knowledge
  award: ["bachelor's with honours"]
  gradeOf: none
  paraphrase: "Graduates show knowledge of policy above and below the nation state and how international organisations frame problems and solutions."
  quote: full   # the issuer's statement is in `source` (D-std-0014)
  audience: both
  subjects: inherited
- id: qaa/social-policy-2026/3.3.b11
  locator: { number: "3.3.b11", headingPath: ["Content, structure and delivery", "Content"] }
  span: { start: 52735, end: 52914 }
  source: "the operation and impact of non-governmental sources of welfare, including the informal, voluntary and private sectors, and of how these interact within mixed economies of welfare"
  stem: "3.3"
  statementType: outcome
  rung: none
  force: describes
  level: fheq:6
  appliesTo: "graduates of Social Policy courses"
  addressee: learner
  verbs: ["interact"]
  about: "non-state welfare and mixed economies"
  themes: [none]
  domain: knowledge
  award: ["bachelor's with honours"]
  gradeOf: none
  paraphrase: "Graduates show knowledge of non-state welfare from informal, voluntary and private sources and how these mix with the state."
  quote: full   # the issuer's statement is in `source` (D-std-0014)
  audience: both
  subjects: inherited
- id: qaa/social-policy-2026/3.3.b12
  locator: { number: "3.3.b12", headingPath: ["Content, structure and delivery", "Content"] }
  span: { start: 52917, end: 53285 }
  source: "elements of social administration, recognising that understanding the leadership, management, and day-to-day operation of welfare institutions strengthen students' capacity to navigate the complexities of service delivery and governance; where suitable, this should embed reflective practice alongside interpersonal skills such as communication and conflict resolution"
  stem: "3.3"
  statementType: outcome
  rung: none
  force: describes
  level: fheq:6
  appliesTo: "graduates of Social Policy courses"
  addressee: learner
  verbs: ["recognising", "navigate", "embed"]
  about: "social administration and the running of institutions"
  themes: [none]
  domain: knowledge
  award: ["bachelor's with honours"]
  gradeOf: none
  paraphrase: "Graduates show knowledge of social administration: how welfare institutions are led, managed and run day to day, with reflective and interpersonal skills."
  quote: full   # the issuer's statement is in `source` (D-std-0014)
  audience: both
  subjects: inherited
- id: qaa/social-policy-2026/3.3.b13
  locator: { number: "3.3.b13", headingPath: ["Content, structure and delivery", "Content"] }
  span: { start: 53288, end: 53399 }
  source: "the use of digital technologies in the design, implementation and administration of social policy interventions"
  stem: "3.3"
  statementType: outcome
  rung: none
  force: describes
  level: fheq:6
  appliesTo: "graduates of Social Policy courses"
  addressee: learner
  verbs: []
  about: "digital technology in policy"
  themes: [none]
  domain: knowledge
  award: ["bachelor's with honours"]
  gradeOf: none
  paraphrase: "Graduates show knowledge of digital technology in designing, delivering and administering policy."
  quote: full   # the issuer's statement is in `source` (D-std-0014)
  audience: both
  subjects: inherited
- id: qaa/social-policy-2026/3.3.b14
  locator: { number: "3.3.b14", headingPath: ["Content, structure and delivery", "Content"] }
  span: { start: 53402, end: 53620 }
  source: "public perceptions and attitudes towards social policy and welfare, including the role of information, disinformation and misinformation and the roles of lobbying, campaigning and advocacy in influencing policy making."
  stem: "3.3"
  statementType: outcome
  rung: none
  force: describes
  level: fheq:6
  appliesTo: "graduates of Social Policy courses"
  addressee: learner
  verbs: ["influencing"]
  about: "public attitudes, misinformation and advocacy"
  themes: [none]
  domain: knowledge
  award: ["bachelor's with honours"]
  gradeOf: none
  paraphrase: "Graduates show knowledge of public attitudes to welfare, the effect of information and misinformation, and how lobbying, campaigns and advocacy shape policy."
  quote: full   # the issuer's statement is in `source` (D-std-0014)
  audience: both
  subjects: inherited
- id: qaa/social-policy-2026/3.3.b15
  locator: { number: "3.3.b15", headingPath: ["Content, structure and delivery", "Content"] }
  span: { start: 53678, end: 53957 }
  source: "the different ways in which social policy impacts on the welfare of individuals and social groups, with regards to the potential improvement of social conditions and collective risk management as well as failures in addressing or alleviating social inequalities and disadvantages"
  stem: "3.3"
  statementType: outcome
  rung: none
  force: describes
  level: fheq:6
  appliesTo: "graduates of Social Policy courses"
  addressee: learner
  verbs: ["impacts"]
  about: "how policy improves or fails welfare"
  themes: [none]
  domain: knowledge
  award: ["bachelor's with honours"]
  gradeOf: none
  paraphrase: "Graduates show knowledge of how policy affects the welfare of people and groups, both improving conditions and failing to reduce inequality."
  quote: full   # the issuer's statement is in `source` (D-std-0014)
  audience: both
  subjects: inherited
- id: qaa/social-policy-2026/3.3.b16
  locator: { number: "3.3.b16", headingPath: ["Content, structure and delivery", "Content"] }
  span: { start: 53960, end: 54196 }
  source: "the potentially ambivalent impacts of social policy interventions, with regards to their social control and disciplinary functions, for example in the context of welfare conditionality or the reproduction of existing social inequalities"
  stem: "3.3"
  statementType: outcome
  rung: none
  force: describes
  level: fheq:6
  appliesTo: "graduates of Social Policy courses"
  addressee: learner
  verbs: []
  about: "ambivalent effects: control and conditionality"
  themes: [none]
  domain: knowledge
  award: ["bachelor's with honours"]
  gradeOf: none
  paraphrase: "Graduates show knowledge of the mixed effects of policy, including control and discipline through conditionality or the reproduction of inequality."
  quote: full   # the issuer's statement is in `source` (D-std-0014)
  audience: both
  subjects: inherited
- id: qaa/social-policy-2026/3.3.b17
  locator: { number: "3.3.b17", headingPath: ["Content, structure and delivery", "Content"] }
  span: { start: 54199, end: 54467 }
  source: "methods of delivery of welfare and social services, including the differences between universal versus targeted welfare, conditional and unconditional welfare, means- testing, and broader concepts and debates around eligibility, 'deservingness', 'leakage' and coverage"
  stem: "3.3"
  statementType: outcome
  rung: none
  force: describes
  level: fheq:6
  appliesTo: "graduates of Social Policy courses"
  addressee: learner
  verbs: []
  about: "ways of delivering welfare; eligibility debates"
  themes: [none]
  domain: knowledge
  award: ["bachelor's with honours"]
  gradeOf: none
  paraphrase: "Graduates show knowledge of ways of delivering welfare: universal or targeted, conditional or not, means-tested, and debates on eligibility, deservingness, leakage and coverage."
  quote: full   # the issuer's statement is in `source` (D-std-0014)
  audience: both
  subjects: inherited
- id: qaa/social-policy-2026/3.3.b18
  locator: { number: "3.3.b18", headingPath: ["Content, structure and delivery", "Content"] }
  span: { start: 54474, end: 54781 }
  source: "the main features of the interrelationships between social policies and differently placed communities, families and individuals, notably those affected by intersectional disadvantages due to socio-economic background, class, ethnic minority, gender identity, sex, disability, religion or sexual orientation"
  stem: "3.3"
  statementType: outcome
  rung: none
  force: describes
  level: fheq:6
  appliesTo: "graduates of Social Policy courses"
  addressee: learner
  verbs: ["affected"]
  about: "policy and intersecting disadvantage"
  themes: [none]
  domain: knowledge
  award: ["bachelor's with honours"]
  gradeOf: none
  paraphrase: "Graduates show knowledge of how policy meets communities, families and people facing intersecting disadvantage of class, ethnicity, gender identity, sex, disability, religion or sexual orientation."
  quote: full   # the issuer's statement is in `source` (D-std-0014)
  audience: both
  subjects: inherited
- id: qaa/social-policy-2026/3.3.b19
  locator: { number: "3.3.b19", headingPath: ["Content, structure and delivery", "Content"] }
  span: { start: 54784, end: 55011 }
  source: "implications for social policy of the adoption of new technologies, such as GenAI and automation, across core dimensions such as work and employment, education, health and social care, and the administration of welfare services"
  stem: "3.3"
  statementType: outcome
  rung: none
  force: describes
  level: fheq:6
  appliesTo: "graduates of Social Policy courses"
  addressee: learner
  verbs: []
  about: "new technology, generative AI and automation"
  themes: [none]
  domain: knowledge
  award: ["bachelor's with honours"]
  gradeOf: none
  paraphrase: "Graduates show knowledge of what new technology, generative AI and automation among them, means for work, education, health, care and welfare administration."
  quote: full   # the issuer's statement is in `source` (D-std-0014)
  audience: both
  subjects: inherited
- id: qaa/social-policy-2026/3.3.b20
  locator: { number: "3.3.b20", headingPath: ["Content, structure and delivery", "Content"] }
  span: { start: 55014, end: 55263 }
  source: "the ways in which social policies shape – and are shaped by – environmental and sustainability debates, recognising the role in addressing climate-related inequalities, resource distribution, and the long-term wellbeing of communities and ecosystems"
  stem: "3.3"
  statementType: outcome
  rung: none
  force: describes
  level: fheq:6
  appliesTo: "graduates of Social Policy courses"
  addressee: learner
  verbs: ["shape", "recognising"]
  about: "policy and environmental debate"
  themes: [none]
  domain: knowledge
  award: ["bachelor's with honours"]
  gradeOf: none
  paraphrase: "Graduates show knowledge of how policy and environmental debate shape each other, including climate inequality, resource distribution and long-term wellbeing."
  quote: full   # the issuer's statement is in `source` (D-std-0014)
  audience: both
  subjects: inherited
- id: qaa/social-policy-2026/3.3.b21
  locator: { number: "3.3.b21", headingPath: ["Content, structure and delivery", "Content"] }
  span: { start: 55266, end: 55430 }
  source: "significant sources of data about social welfare, and the main quantitative and qualitative social research approaches and methods used to collect and analyse data."
  stem: "3.3"
  statementType: outcome
  rung: none
  force: describes
  level: fheq:6
  appliesTo: "graduates of Social Policy courses"
  addressee: learner
  verbs: ["collect", "analyse"]
  about: "welfare data sources and research methods"
  themes: [none]
  domain: knowledge
  award: ["bachelor's with honours"]
  gradeOf: none
  paraphrase: "Graduates show knowledge of major data sources on welfare and the main quantitative and qualitative research methods."
  quote: full   # the issuer's statement is in `source` (D-std-0014)
  audience: both
  subjects: inherited
- id: qaa/social-policy-2026/3.3.b22
  locator: { number: "3.3.b22", headingPath: ["Content, structure and delivery", "Content"] }
  span: { start: 55562, end: 55857 }
  source: "key concepts such as human needs, human wellbeing, and social welfare; poverty, inequality, and social exclusion; citizenship, human and social rights; equality, equity, and social justice; sustainability and environmental justice; social and cultural difference, diversity and intersectionality"
  stem: "3.3"
  statementType: outcome
  rung: none
  force: describes
  level: fheq:6
  appliesTo: "graduates of Social Policy courses"
  addressee: learner
  verbs: []
  about: "core concepts of welfare"
  themes: [none]
  domain: knowledge
  award: ["bachelor's with honours"]
  gradeOf: none
  paraphrase: "Graduates show knowledge of core concepts: need, wellbeing, welfare, poverty, inequality, exclusion, citizenship, rights, equity, justice, sustainability, difference and intersectionality."
  quote: full   # the issuer's statement is in `source` (D-std-0014)
  audience: both
  subjects: inherited
- id: qaa/social-policy-2026/3.3.b23
  locator: { number: "3.3.b23", headingPath: ["Content, structure and delivery", "Content"] }
  span: { start: 55860, end: 56046 }
  source: "different theories, philosophies and ideological debates related to human welfare and the role of state, market and other non-state actors in the collective provision of welfare services"
  stem: "3.3"
  statementType: outcome
  rung: none
  force: describes
  level: fheq:6
  appliesTo: "graduates of Social Policy courses"
  addressee: learner
  verbs: []
  about: "theories and ideologies of welfare"
  themes: [none]
  domain: knowledge
  award: ["bachelor's with honours"]
  gradeOf: none
  paraphrase: "Graduates show knowledge of theories, philosophies and ideological debates about welfare and the roles of state, market and other actors."
  quote: full   # the issuer's statement is in `source` (D-std-0014)
  audience: both
  subjects: inherited
- id: qaa/social-policy-2026/3.3.b24
  locator: { number: "3.3.b24", headingPath: ["Content, structure and delivery", "Content"] }
  span: { start: 56049, end: 56134 }
  source: "theories of the state and policy making; theories and methods of comparative analysis"
  stem: "3.3"
  statementType: outcome
  rung: none
  force: describes
  level: fheq:6
  appliesTo: "graduates of Social Policy courses"
  addressee: learner
  verbs: []
  about: "theories of the state and comparison"
  themes: [none]
  domain: knowledge
  award: ["bachelor's with honours"]
  gradeOf: none
  paraphrase: "Graduates show knowledge of theories of the state and policy making, and comparative theory and method."
  quote: full   # the issuer's statement is in `source` (D-std-0014)
  audience: both
  subjects: inherited
- id: qaa/social-policy-2026/3.3.b25
  locator: { number: "3.3.b25", headingPath: ["Content, structure and delivery", "Content"] }
  span: { start: 56137, end: 56313 }
  source: "interdisciplinary approaches to social policy topics and issues, with contributions of different social science disciplines coalescing around the applied focus of social policy"
  stem: "3.3"
  statementType: outcome
  rung: none
  force: describes
  level: fheq:6
  appliesTo: "graduates of Social Policy courses"
  addressee: learner
  verbs: ["coalescing"]
  about: "interdisciplinary approaches"
  themes: [none]
  domain: knowledge
  award: ["bachelor's with honours"]
  gradeOf: none
  paraphrase: "Graduates show knowledge of interdisciplinary approaches, with the social sciences meeting around policy's applied focus."
  quote: full   # the issuer's statement is in `source` (D-std-0014)
  audience: both
  subjects: inherited
- id: qaa/social-policy-2026/3.3.b26
  locator: { number: "3.3.b26", headingPath: ["Content, structure and delivery", "Content"] }
  span: { start: 56316, end: 56427 }
  source: "the political economy of welfare and how values and principles are related to political and economic interests."
  stem: "3.3"
  statementType: outcome
  rung: none
  force: describes
  level: fheq:6
  appliesTo: "graduates of Social Policy courses"
  addressee: learner
  verbs: ["related"]
  about: "political economy of welfare"
  themes: [none]
  domain: knowledge
  award: ["bachelor's with honours"]
  gradeOf: none
  paraphrase: "Graduates show knowledge of the political economy of welfare and how values link to political and economic interests."
  quote: full   # the issuer's statement is in `source` (D-std-0014)
  audience: both
  subjects: inherited
- id: qaa/social-policy-2026/3.3.b27
  locator: { number: "3.3.b27", headingPath: ["Content, structure and delivery", "Content"] }
  span: { start: 56521, end: 56593 }
  source: "ontological and epistemological underpinnings of varied research designs"
  stem: "3.3"
  statementType: outcome
  rung: none
  force: describes
  level: fheq:6
  appliesTo: "graduates of Social Policy courses"
  addressee: learner
  verbs: []
  about: "ontology and epistemology of research"
  themes: [none]
  domain: knowledge
  award: ["bachelor's with honours"]
  gradeOf: none
  paraphrase: "Graduates show knowledge of the ontology and epistemology beneath research designs."
  quote: full   # the issuer's statement is in `source` (D-std-0014)
  audience: both
  subjects: inherited
- id: qaa/social-policy-2026/3.3.b28
  locator: { number: "3.3.b28", headingPath: ["Content, structure and delivery", "Content"] }
  span: { start: 56596, end: 56653 }
  source: "identifying suitable research problems related to welfare"
  stem: "3.3"
  statementType: outcome
  rung: none
  force: describes
  level: fheq:6
  appliesTo: "graduates of Social Policy courses"
  addressee: learner
  verbs: ["identifying"]
  about: "framing research problems"
  themes: [none]
  domain: knowledge
  award: ["bachelor's with honours"]
  gradeOf: none
  paraphrase: "Graduates show knowledge of how to identify researchable problems about welfare."
  quote: full   # the issuer's statement is in `source` (D-std-0014)
  audience: both
  subjects: inherited
- id: qaa/social-policy-2026/3.3.b29
  locator: { number: "3.3.b29", headingPath: ["Content, structure and delivery", "Content"] }
  span: { start: 56656, end: 56740 }
  source: "research design principles for quantitative, qualitative and mixed method approaches"
  stem: "3.3"
  statementType: outcome
  rung: none
  force: describes
  level: fheq:6
  appliesTo: "graduates of Social Policy courses"
  addressee: learner
  verbs: []
  about: "research design principles"
  themes: [none]
  domain: knowledge
  award: ["bachelor's with honours"]
  gradeOf: none
  paraphrase: "Graduates show knowledge of the principles of quantitative, qualitative and mixed-method research design."
  quote: full   # the issuer's statement is in `source` (D-std-0014)
  audience: both
  subjects: inherited
- id: qaa/social-policy-2026/3.3.b30
  locator: { number: "3.3.b30", headingPath: ["Content, structure and delivery", "Content"] }
  span: { start: 56743, end: 56916 }
  source: "the selection of appropriate techniques and methods in the collection, management, interpretation and analysis of qualitative and quantitative data, including secondary data"
  stem: "3.3"
  statementType: outcome
  rung: none
  force: describes
  level: fheq:6
  appliesTo: "graduates of Social Policy courses"
  addressee: learner
  verbs: []
  about: "choosing techniques for data"
  themes: [none]
  domain: knowledge
  award: ["bachelor's with honours"]
  gradeOf: none
  paraphrase: "Graduates show knowledge of how to choose techniques for collecting, managing, interpreting and analysing data, secondary data included."
  quote: full   # the issuer's statement is in `source` (D-std-0014)
  audience: both
  subjects: inherited
- id: qaa/social-policy-2026/3.3.b31
  locator: { number: "3.3.b31", headingPath: ["Content, structure and delivery", "Content"] }
  span: { start: 56919, end: 56970 }
  source: "approaches to policy evaluation and policy analysis"
  stem: "3.3"
  statementType: outcome
  rung: none
  force: describes
  level: fheq:6
  appliesTo: "graduates of Social Policy courses"
  addressee: learner
  verbs: []
  about: "policy evaluation and analysis"
  themes: [none]
  domain: knowledge
  award: ["bachelor's with honours"]
  gradeOf: none
  paraphrase: "Graduates show knowledge of approaches to policy evaluation and analysis."
  quote: full   # the issuer's statement is in `source` (D-std-0014)
  audience: both
  subjects: inherited
- id: qaa/social-policy-2026/3.3.b32
  locator: { number: "3.3.b32", headingPath: ["Content, structure and delivery", "Content"] }
  span: { start: 56973, end: 57093 }
  source: "awareness of evidence-based policy debates and the role of social science research for informing policy-making processes"
  stem: "3.3"
  statementType: outcome
  rung: none
  force: describes
  level: fheq:6
  appliesTo: "graduates of Social Policy courses"
  addressee: learner
  verbs: ["informing"]
  about: "evidence-based policy and research"
  themes: [none]
  domain: knowledge
  award: ["bachelor's with honours"]
  gradeOf: none
  paraphrase: "Graduates show knowledge of debates on evidence-based policy and how social science research informs policy making."
  quote: full   # the issuer's statement is in `source` (D-std-0014)
  audience: both
  subjects: inherited
- id: qaa/social-policy-2026/3.3.b33
  locator: { number: "3.3.b33", headingPath: ["Content, structure and delivery", "Content"] }
  span: { start: 57096, end: 57130 }
  source: "ethics of social science research."
  stem: "3.3"
  statementType: outcome
  rung: none
  force: describes
  level: fheq:6
  appliesTo: "graduates of Social Policy courses"
  addressee: learner
  verbs: []
  about: "research ethics"
  themes: [none]
  domain: knowledge
  award: ["bachelor's with honours"]
  gradeOf: none
  paraphrase: "Graduates show knowledge of research ethics in the social sciences."
  quote: full   # the issuer's statement is in `source` (D-std-0014)
  audience: both
  subjects: inherited
- id: qaa/social-policy-2026/3.4
  locator: { number: "3.4", headingPath: ["Content, structure and delivery", "Teaching and learning"] }
  span: { start: 57437, end: 57558 }
  source: "Social Policy requires that students directly engage with current debates and arguments surrounding social policy issues."
  stem: none
  statementType: requirement
  rung: none
  force: must
  level: fheq:6
  appliesTo: "Social Policy students"
  addressee: learner
  verbs: ["requires", "engage"]
  about: "direct engagement with current debates"
  themes: [none]
  domain: subject-skill
  award: ["bachelor's with honours"]
  gradeOf: none
  paraphrase: "The subject requires students to take part directly in current debates and arguments on social policy issues."
  quote: full   # the issuer's statement is in `source` (D-std-0014)
  audience: both
  subjects: inherited
- id: qaa/social-policy-2026/3.9
  locator: { number: "3.9", headingPath: ["Content, structure and delivery", "Teaching and learning"] }
  span: { start: 60816, end: 60970 }
  source: "The needs of all students should be reflected in inclusive learning design and assessment methods, to ensure that all learners can fulfil their potential."
  stem: none
  statementType: expectation
  rung: none
  force: should
  level: none
  appliesTo: "those who design learning and assessment"
  addressee: provider
  verbs: ["reflected", "ensure", "fulfil"]
  about: "inclusive learning and assessment design"
  themes: [none]
  domain: none
  award: ["bachelor's with honours"]
  gradeOf: none
  paraphrase: "Inclusive learning design and assessment methods should reflect every student's needs so all can reach their potential, mature learners and those at higher risk of disadvantage among them."
  quote: full   # the issuer's statement is in `source` (D-std-0014)
  audience: practitioner
  subjects: inherited
- id: qaa/social-policy-2026/3.12
  locator: { number: "3.12", headingPath: ["Content, structure and delivery", "Assessment"] }
  span: { start: 61723, end: 62622 }
  source: "3.12 While Social Policy graduates should be equipped with competences to work within a wider team or effectively deploy GenAI tools for the purposes of analysis and presentation in an ethically responsible and appropriate manner, careful attention must be paid to ensure that, throughout the breadth of assessments on a course in Social Policy, there is sufficient validation of a graduate's independent competency across the range of subject-specific knowledge, skills and abilities. Expectations around independent working and collusion, including any prescriptions on the use of GenAI, should be clear in such cases where a student's independent competency is being assessed. There must be sufficient capacity and resourcing to investigate any suspected misconduct in such assessments to ensure they represent an authentic assessment of a graduate's core competencies. See paragraphs 1.60-1.66.\n"
  stem: none
  statementType: requirement
  rung: none
  force: must
  level: none
  appliesTo: "those who design assessment and the institution that resources it"
  addressee: provider
  verbs: ["equipped", "paid", "ensure", "investigate"]
  about: "validating independent competence; misconduct"
  themes: [none]
  domain: none
  award: ["bachelor's with honours"]
  gradeOf: none
  paraphrase: "Graduates should be able to work in teams and use generative AI responsibly, but across a course's assessments care must be taken that each graduate's own competence is validated; rules on collusion and AI use should be clear where independence is assessed, and there must be capacity to investigate suspected misconduct."
  quote: full   # the issuer's statement is in `source` (D-std-0014)
  audience: practitioner
  subjects: inherited
- id: qaa/social-policy-2026/3.13.b6
  locator: { number: "3.13.b6", headingPath: ["Content, structure and delivery", "Assessment"] }
  span: { start: 63096, end: 63173 }
  source: "students should be supported to complete assessments with competing deadlines"
  stem: "3.13"
  statementType: expectation
  rung: none
  force: should
  level: none
  appliesTo: "those who schedule and support assessment"
  addressee: provider
  verbs: ["supported", "complete"]
  about: "support with competing deadlines"
  themes: [none]
  domain: none
  award: ["bachelor's with honours"]
  gradeOf: none
  paraphrase: "Students should be helped to complete assessments when deadlines compete."
  quote: full   # the issuer's statement is in `source` (D-std-0014)
  audience: practitioner
  subjects: inherited
- id: qaa/social-policy-2026/3.17
  locator: { number: "3.17", headingPath: ["Content, structure and delivery", "Assessment"] }
  span: { start: 64717, end: 64954 }
  source: "3.17 Feedback should also be mindful to give learners a sense of their strengths and, in the case of academic tuition, development over time, to ensure they are able to identify and communicate these strengths in workplace settings.\n\n22\n"
  stem: none
  statementType: expectation
  rung: none
  force: should
  level: none
  appliesTo: "those who give feedback"
  addressee: provider
  verbs: ["give", "ensure", "identify", "communicate"]
  about: "feedback on strengths for work"
  themes: [none]
  domain: none
  award: ["bachelor's with honours"]
  gradeOf: none
  paraphrase: "Feedback should also show learners their strengths and, in academic tuition, their progress over time, so they can name and communicate those strengths at work."
  quote: full   # the issuer's statement is in `source` (D-std-0014)
  audience: practitioner
  subjects: inherited
- id: qaa/social-policy-2026/4.3
  locator: { number: "4.3", headingPath: ["Benchmark standards", "Introduction"] }
  span: { start: 65737, end: 66227 }
  source: "4.3 It is important to note that a significant proportion of graduates will perform above the 'typical' level. Each higher education provider has its own method of determining what appropriate evidence of this achievement will be and should refer to Annex D in The Frameworks for Higher Education Qualifications of UK Degree-Awarding Bodies. This Annex sets out common descriptions of the four main degree outcome classifications for bachelor's degrees with honours: 1st, 2.1, 2.2 and 3rd.\n"
  stem: none
  statementType: expectation
  rung: none
  force: should
  level: fheq:6
  appliesTo: "providers"
  addressee: provider
  verbs: ["perform", "refer"]
  about: "evidence above typical; Annex D"
  themes: [none]
  domain: none
  award: ["bachelor's with honours"]
  gradeOf: none
  paraphrase: "Many graduates will do better than the typical standard; each provider decides how to evidence that and should refer to Annex D of the Frameworks, which describes the four honours classes (1st, 2.1, 2.2, 3rd)."
  quote: full   # the issuer's statement is in `source` (D-std-0014)
  audience: practitioner
  subjects: inherited
- id: qaa/social-policy-2026/4.4
  locator: { number: "4.4", headingPath: ["Benchmark standards", "Introduction"] }
  span: { start: 66227, end: 66785 }
  source: "4.4 Please note that minimum 'threshold standards' are not intended to specify universal competence standards for a discipline. If a provider chooses to develop competence standards (as defined by the Equality Act 2010, and relevant equality legislation in Northern Ireland) as part of a programme specification, these can be informed by the relevant Subject Benchmark Statement along with any PSRB requirements. In these circumstances, providers should follow the most recent guidance from the Equality and Human Rights Commission. Undergraduate programmes\n"
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
- id: qaa/social-policy-2026/4.5.b1
  locator: { number: "4.5.b1", headingPath: ["Benchmark standards", "Undergraduate programmes"] }
  span: { start: 67222, end: 67284 }
  source: "have developed an understanding of a complex body of knowledge"
  stem: "4.5"
  statementType: outcome
  rung: none
  force: must   # D-std-0016: "are expected to" read as must
  level: fheq:6
  appliesTo: "honours graduates"
  addressee: learner
  verbs: ["developed"]
  about: "grasp of a complex body of knowledge"
  themes: [none]
  domain: understanding
  award: ["bachelor's with honours"]
  gradeOf: none
  paraphrase: "In line with the Frameworks, honours graduates are expected to grasp a complex and substantial body of knowledge."
  quote: full   # the issuer's statement is in `source` (D-std-0014)
  audience: both
  subjects: inherited
- id: qaa/social-policy-2026/4.5.b2
  locator: { number: "4.5.b2", headingPath: ["Benchmark standards", "Undergraduate programmes"] }
  span: { start: 67287, end: 67403 }
  source: "have developed analytical techniques and problem-solving skills that can be applied in different types of employment"
  stem: "4.5"
  statementType: outcome
  rung: none
  force: must   # D-std-0016: "are expected to" read as must
  level: fheq:6
  appliesTo: "honours graduates"
  addressee: learner
  verbs: ["developed", "applied"]
  about: "analytical and problem-solving skills for work"
  themes: [none]
  domain: generic-skill
  award: ["bachelor's with honours"]
  gradeOf: none
  paraphrase: "Honours graduates are expected to have gained analytical and problem-solving skills they can use in many kinds of work."
  quote: full   # the issuer's statement is in `source` (D-std-0014)
  audience: both
  subjects: inherited
- id: qaa/social-policy-2026/4.5.b3
  locator: { number: "4.5.b3", headingPath: ["Benchmark standards", "Undergraduate programmes"] }
  span: { start: 67406, end: 67512 }
  source: "have developed skills and experience of working in a co-creative, sustainable and socially responsible way"
  stem: "4.5"
  statementType: outcome
  rung: none
  force: must   # D-std-0016: "are expected to" read as must
  level: fheq:6
  appliesTo: "honours graduates"
  addressee: learner
  verbs: ["developed", "working"]
  about: "co-creative, sustainable and responsible working"
  themes: [none]
  domain: generic-skill
  award: ["bachelor's with honours"]
  gradeOf: none
  paraphrase: "Honours graduates are expected to have learned, through experience, to work with others in ways that are co-creative, sustainable and socially responsible."
  quote: full   # the issuer's statement is in `source` (D-std-0014)
  audience: both
  subjects: inherited
- id: qaa/social-policy-2026/4.5.b4
  locator: { number: "4.5.b4", headingPath: ["Benchmark standards", "Undergraduate programmes"] }
  span: { start: 67515, end: 67633 }
  source: "be able to analyse evidence, arguments and assumptions, to reach sound judgements and to communicate them effectively."
  stem: "4.5"
  statementType: outcome
  rung: none
  force: must   # D-std-0016: "are expected to" read as must
  level: fheq:6
  appliesTo: "honours graduates"
  addressee: learner
  verbs: ["analyse", "reach", "communicate"]
  about: "weighing evidence, judging soundly and communicating"
  themes: [none]
  domain: generic-skill
  award: ["bachelor's with honours"]
  gradeOf: none
  paraphrase: "Honours graduates are expected to be able to weigh evidence, arguments and assumptions, reach sound conclusions and communicate them well."
  quote: full   # the issuer's statement is in `source` (D-std-0014)
  audience: both
  subjects: inherited
- id: qaa/social-policy-2026/4.7.b1
  locator: { number: "4.7.b1", headingPath: ["Benchmark standards", "Undergraduate programmes"] }
  span: { start: 68333, end: 68446 }
  source: "Demonstrate factual knowledge of important historical and contemporary social policy events, issues and policies."
  stem: "4.7"
  statementType: threshold
  rung: threshold
  force: threshold
  level: fheq:6
  appliesTo: "honours graduates at the threshold standard (third-class)"
  addressee: learner
  verbs: ["demonstrate"]
  about: "factual knowledge of past and present policy events"
  themes: [none]
  domain: knowledge
  award: ["bachelor's with honours"]
  gradeOf: none
  paraphrase: "At the threshold for third-class honours, graduates show they know the facts of significant social policy events, issues and policies, past and present."
  quote: full   # the issuer's statement is in `source` (D-std-0014)
  audience: both
  subjects: inherited
- id: qaa/social-policy-2026/4.7.b1.excellent
  locator: { number: "4.7.b1.excellent", headingPath: ["Benchmark standards", "Undergraduate programmes"] }
  span: { start: 68764, end: 68920 }
  source: "Critique the role and evaluate the effects of policies in the main social policy areas across the UK and internationally, including new and emerging issues."
  stem: "4.7"
  statementType: excellent
  rung: excellent
  force: must
  level: fheq:6
  appliesTo: "honours graduates at the excellent standard (first-class)"
  addressee: learner
  verbs: ["critique", "evaluate"]
  about: "critique and evaluation of policy across the main fields"
  themes: [none]
  domain: knowledge
  award: ["bachelor's with honours"]
  gradeOf: { statement: qaa/social-policy-2026/4.7.b1.typical, basis: stated }
  paraphrase: "At the excellent standard, required for first-class honours, graduates critique what policies do and weigh their effects across the main policy fields, in the UK and abroad, emerging issues included."
  quote: full   # the issuer's statement is in `source` (D-std-0014)
  audience: both
  subjects: inherited
- id: qaa/social-policy-2026/4.7.b1.typical
  locator: { number: "4.7.b1.typical", headingPath: ["Benchmark standards", "Undergraduate programmes"] }
  span: { start: 68447, end: 68763 }
  source: "Demonstrate in-depth knowledge, understanding and critical awareness of key aspects of Social Policy analysis, including, for example, how social policies operate in local, national and international contexts in developing a sustainable future, with specific reference to the UN Sustainable Development Goals (SDGs)."
  stem: "4.7"
  statementType: typical
  rung: typical
  force: must
  level: fheq:6
  appliesTo: "honours graduates at the typical standard (second-class)"
  addressee: learner
  verbs: ["demonstrate", "operate"]
  about: "deep, critical knowledge of policy analysis, sustainability included"
  themes: [none]
  domain: knowledge
  award: ["bachelor's with honours"]
  gradeOf: { statement: qaa/social-policy-2026/4.7.b1, basis: stated }
  paraphrase: "At the typical standard, required for second-class honours, graduates show deep knowledge and critical awareness of central parts of policy analysis, such as how policies at local, national and international scale bear on a sustainable future and the UN goals."
  quote: full   # the issuer's statement is in `source` (D-std-0014)
  audience: both
  subjects: inherited
- id: qaa/social-policy-2026/4.7.b2
  locator: { number: "4.7.b2", headingPath: ["Benchmark standards", "Undergraduate programmes"] }
  span: { start: 68922, end: 69150 }
  source: "Understand and compare how social policies operate across the UK and internationally, with particular emphasis on, but not limited to, health, education, housing, employment, social protection/income maintenance and social care."
  stem: "4.7"
  statementType: threshold
  rung: threshold
  force: threshold
  level: fheq:6
  appliesTo: "honours graduates at the threshold standard (third-class)"
  addressee: learner
  verbs: ["understand", "compare", "operate"]
  about: "how policies work in the UK and elsewhere"
  themes: [none]
  domain: understanding
  award: ["bachelor's with honours"]
  gradeOf: none
  paraphrase: "At the threshold for third-class honours, graduates understand and compare the workings of social policies in the UK and in other countries, notably in health, education, housing, work, income support and care."
  quote: full   # the issuer's statement is in `source` (D-std-0014)
  audience: both
  subjects: inherited
- id: qaa/social-policy-2026/4.7.b2.excellent
  locator: { number: "4.7.b2.excellent", headingPath: ["Benchmark standards", "Undergraduate programmes"] }
  span: { start: 69239, end: 69433 }
  source: "Classify and critically evaluate the rationales for, coherence and effects of different types of welfare states and social policies, including their respective implications for different groups."
  stem: "4.7"
  statementType: excellent
  rung: excellent
  force: must
  level: fheq:6
  appliesTo: "honours graduates at the excellent standard (first-class)"
  addressee: learner
  verbs: ["classify", "evaluate"]
  about: "typing and judging welfare states and their effects on groups"
  themes: [none]
  domain: understanding
  award: ["bachelor's with honours"]
  gradeOf: { statement: qaa/social-policy-2026/4.7.b2.typical, basis: stated }
  paraphrase: "At the excellent standard, required for first-class honours, graduates sort types of welfare state and policy, and critically judge the reasoning, consistency and effects of each, including what each means for different groups."
  quote: full   # the issuer's statement is in `source` (D-std-0014)
  audience: both
  subjects: inherited
- id: qaa/social-policy-2026/4.7.b2.typical
  locator: { number: "4.7.b2.typical", headingPath: ["Benchmark standards", "Undergraduate programmes"] }
  span: { start: 69151, end: 69237 }
  source: "Distinguish, compare and critique welfare systems across different parts of the world."
  stem: "4.7"
  statementType: typical
  rung: typical
  force: must
  level: fheq:6
  appliesTo: "honours graduates at the typical standard (second-class)"
  addressee: learner
  verbs: ["distinguish", "compare", "critique"]
  about: "comparative critique of welfare systems"
  themes: [none]
  domain: understanding
  award: ["bachelor's with honours"]
  gradeOf: { statement: qaa/social-policy-2026/4.7.b2, basis: stated }
  paraphrase: "At the typical standard, required for second-class honours, graduates tell welfare systems in different regions of the world apart, compare them and critique them."
  quote: full   # the issuer's statement is in `source` (D-std-0014)
  audience: both
  subjects: inherited
- id: qaa/social-policy-2026/4.7.b3
  locator: { number: "4.7.b3", headingPath: ["Benchmark standards", "Undergraduate programmes"] }
  span: { start: 69435, end: 69539 }
  source: "Discuss, contrast and apply core theories, concepts, perspectives and methods relevant to Social Policy."
  stem: "4.7"
  statementType: threshold
  rung: threshold
  force: threshold
  level: fheq:6
  appliesTo: "honours graduates at the threshold standard (third-class)"
  addressee: learner
  verbs: ["discuss", "contrast", "apply"]
  about: "using the core theories and concepts"
  themes: [none]
  domain: understanding
  award: ["bachelor's with honours"]
  gradeOf: none
  paraphrase: "At the threshold for third-class honours, graduates discuss, set against each other and use the main theories, concepts, perspectives and methods of the subject."
  quote: full   # the issuer's statement is in `source` (D-std-0014)
  audience: both
  subjects: inherited
- id: qaa/social-policy-2026/4.7.b3.excellent
  locator: { number: "4.7.b3.excellent", headingPath: ["Benchmark standards", "Undergraduate programmes"] }
  span: { start: 69655, end: 69774 }
  source: "Analyse, classify, synthesise and critique core theories, concepts, perspectives and methods relevant to Social Policy."
  stem: "4.7"
  statementType: excellent
  rung: excellent
  force: must
  level: fheq:6
  appliesTo: "honours graduates at the excellent standard (first-class)"
  addressee: learner
  verbs: ["analyse", "classify", "synthesise", "critique"]
  about: "synthesis and critique of core theory"
  themes: [none]
  domain: understanding
  award: ["bachelor's with honours"]
  gradeOf: { statement: qaa/social-policy-2026/4.7.b3.typical, basis: stated }
  paraphrase: "At the excellent standard, required for first-class honours, graduates analyse, sort, bring together and critique the main theories, concepts, perspectives and methods of the subject."
  quote: full   # the issuer's statement is in `source` (D-std-0014)
  audience: both
  subjects: inherited
- id: qaa/social-policy-2026/4.7.b3.typical
  locator: { number: "4.7.b3.typical", headingPath: ["Benchmark standards", "Undergraduate programmes"] }
  span: { start: 69540, end: 69654 }
  source: "Categorise and engage critically with core theories, concepts, perspectives and methods relevant to Social Policy."
  stem: "4.7"
  statementType: typical
  rung: typical
  force: must
  level: fheq:6
  appliesTo: "honours graduates at the typical standard (second-class)"
  addressee: learner
  verbs: ["categorise", "engage"]
  about: "critical engagement with core theory"
  themes: [none]
  domain: understanding
  award: ["bachelor's with honours"]
  gradeOf: { statement: qaa/social-policy-2026/4.7.b3, basis: stated }
  paraphrase: "At the typical standard, required for second-class honours, graduates group the main theories, concepts, perspectives and methods of the subject and engage with them critically."
  quote: full   # the issuer's statement is in `source` (D-std-0014)
  audience: both
  subjects: inherited
- id: qaa/social-policy-2026/4.7.b4
  locator: { number: "4.7.b4", headingPath: ["Benchmark standards", "Undergraduate programmes"] }
  span: { start: 69775, end: 69812 }
  source: "Demonstrate awareness of the UN SDGs."
  stem: "4.7"
  statementType: threshold
  rung: threshold
  force: threshold
  level: fheq:6
  appliesTo: "honours graduates at the threshold standard (third-class)"
  addressee: learner
  verbs: ["demonstrate"]
  about: "awareness of the UN goals"
  themes: [none]
  domain: knowledge
  award: ["bachelor's with honours"]
  gradeOf: none
  paraphrase: "At the threshold for third-class honours, graduates show they are aware of the UN Sustainable Development Goals."
  quote: full   # the issuer's statement is in `source` (D-std-0014)
  audience: both
  subjects: inherited
- id: qaa/social-policy-2026/4.7.b4.excellent
  locator: { number: "4.7.b4.excellent", headingPath: ["Benchmark standards", "Undergraduate programmes"] }
  span: { start: 69909, end: 70050 }
  source: "Construct analysis of social problems and social policies which integrate the principles of sustainable development, which embed the UN SDGs."
  stem: "4.7"
  statementType: excellent
  rung: excellent
  force: must
  level: fheq:6
  appliesTo: "honours graduates at the excellent standard (first-class)"
  addressee: learner
  verbs: ["construct", "integrate", "embed"]
  about: "analysis built on sustainable development"
  themes: [none]
  domain: knowledge
  award: ["bachelor's with honours"]
  gradeOf: { statement: qaa/social-policy-2026/4.7.b4.typical, basis: stated }
  paraphrase: "At the excellent standard, required for first-class honours, graduates build analyses of social problems and policies with sustainable development principles and the UN goals at the core."
  quote: full   # the issuer's statement is in `source` (D-std-0014)
  audience: both
  subjects: inherited
- id: qaa/social-policy-2026/4.7.b4.typical
  locator: { number: "4.7.b4.typical", headingPath: ["Benchmark standards", "Undergraduate programmes"] }
  span: { start: 69813, end: 69908 }
  source: "Apply their knowledge and understanding of UN SDGs across a wide range of social policy issues."
  stem: "4.7"
  statementType: typical
  rung: typical
  force: must
  level: fheq:6
  appliesTo: "honours graduates at the typical standard (second-class)"
  addressee: learner
  verbs: ["apply"]
  about: "applying the UN goals to many issues"
  themes: [none]
  domain: knowledge
  award: ["bachelor's with honours"]
  gradeOf: { statement: qaa/social-policy-2026/4.7.b4, basis: stated }
  paraphrase: "At the typical standard, required for second-class honours, graduates use what they know of the UN goals on many different social policy issues."
  quote: full   # the issuer's statement is in `source` (D-std-0014)
  audience: both
  subjects: inherited
- id: qaa/social-policy-2026/4.8.b1
  locator: { number: "4.8.b1", headingPath: ["Benchmark standards", "Undergraduate programmes"] }
  span: { start: 70231, end: 70287 }
  source: "Recall key characteristics of different social problems."
  stem: "4.8"
  statementType: threshold
  rung: threshold
  force: threshold
  level: fheq:6
  appliesTo: "honours graduates at the threshold standard (third-class)"
  addressee: learner
  verbs: ["recall"]
  about: "features of social problems"
  themes: [none]
  domain: subject-skill
  award: ["bachelor's with honours"]
  gradeOf: none
  paraphrase: "At the threshold for third-class honours, graduates recall the main features of a range of social problems."
  quote: full   # the issuer's statement is in `source` (D-std-0014)
  audience: both
  subjects: inherited
- id: qaa/social-policy-2026/4.8.b1.excellent
  locator: { number: "4.8.b1.excellent", headingPath: ["Benchmark standards", "Undergraduate programmes"] }
  span: { start: 70380, end: 70541 }
  source: "Construct critical analysis of key social problems and policy responses, and evaluate alternative solutions using relevant analytical tools and research methods."
  stem: "4.8"
  statementType: excellent
  rung: excellent
  force: must
  level: fheq:6
  appliesTo: "honours graduates at the excellent standard (first-class)"
  addressee: learner
  verbs: ["construct", "evaluate", "using"]
  about: "critical analysis of problems and alternative solutions"
  themes: [none]
  domain: subject-skill
  award: ["bachelor's with honours"]
  gradeOf: { statement: qaa/social-policy-2026/4.8.b1.typical, basis: stated }
  paraphrase: "At the excellent standard, required for first-class honours, graduates build critical analyses of major social problems and the policies aimed at them, and weigh other solutions with suitable analytical tools and research methods."
  quote: full   # the issuer's statement is in `source` (D-std-0014)
  audience: both
  subjects: inherited
- id: qaa/social-policy-2026/4.8.b1.typical
  locator: { number: "4.8.b1.typical", headingPath: ["Benchmark standards", "Undergraduate programmes"] }
  span: { start: 70288, end: 70379 }
  source: "Utilise key conceptual frameworks to analyse complex social questions, issues and problems."
  stem: "4.8"
  statementType: typical
  rung: typical
  force: must
  level: fheq:6
  appliesTo: "honours graduates at the typical standard (second-class)"
  addressee: learner
  verbs: ["utilise", "analyse"]
  about: "frameworks used to analyse complex problems"
  themes: [none]
  domain: subject-skill
  award: ["bachelor's with honours"]
  gradeOf: { statement: qaa/social-policy-2026/4.8.b1, basis: stated }
  paraphrase: "At the typical standard, required for second-class honours, graduates use central conceptual frameworks to analyse complex social questions and problems."
  quote: full   # the issuer's statement is in `source` (D-std-0014)
  audience: both
  subjects: inherited
- id: qaa/social-policy-2026/4.8.b2
  locator: { number: "4.8.b2", headingPath: ["Benchmark standards", "Undergraduate programmes"] }
  span: { start: 70546, end: 70624 }
  source: "Summarise and contrast core Social Policy theories, concepts and perspectives."
  stem: "4.8"
  statementType: threshold
  rung: threshold
  force: threshold
  level: fheq:6
  appliesTo: "honours graduates at the threshold standard (third-class)"
  addressee: learner
  verbs: ["summarise", "contrast"]
  about: "summary and contrast of core theory"
  themes: [none]
  domain: subject-skill
  award: ["bachelor's with honours"]
  gradeOf: none
  paraphrase: "At the threshold for third-class honours, graduates sum up the subject's main theories, concepts and perspectives and show how they differ."
  quote: full   # the issuer's statement is in `source` (D-std-0014)
  audience: both
  subjects: inherited
- id: qaa/social-policy-2026/4.8.b2.excellent
  locator: { number: "4.8.b2.excellent", headingPath: ["Benchmark standards", "Undergraduate programmes"] }
  span: { start: 70773, end: 70882 }
  source: "Critically classify, compare, synthesise and evaluate core Social Policy theories, concepts and perspectives."
  stem: "4.8"
  statementType: excellent
  rung: excellent
  force: must
  level: fheq:6
  appliesTo: "honours graduates at the excellent standard (first-class)"
  addressee: learner
  verbs: ["classify", "compare", "synthesise", "evaluate"]
  about: "critical synthesis and evaluation of core theory"
  themes: [none]
  domain: subject-skill
  award: ["bachelor's with honours"]
  gradeOf: { statement: qaa/social-policy-2026/4.8.b2.typical, basis: stated }
  paraphrase: "At the excellent standard, required for first-class honours, graduates critically sort, compare, combine and judge the subject's main theories, concepts and perspectives."
  quote: full   # the issuer's statement is in `source` (D-std-0014)
  audience: both
  subjects: inherited
- id: qaa/social-policy-2026/4.8.b2.typical
  locator: { number: "4.8.b2.typical", headingPath: ["Benchmark standards", "Undergraduate programmes"] }
  span: { start: 70625, end: 70772 }
  source: "Understand and apply core theories, concepts and perspectives in Social Policy and appreciate their relevance for other subjects and practitioners."
  stem: "4.8"
  statementType: typical
  rung: typical
  force: must
  level: fheq:6
  appliesTo: "honours graduates at the typical standard (second-class)"
  addressee: learner
  verbs: ["understand", "apply", "appreciate"]
  about: "applying core theory, for other fields too"
  themes: [none]
  domain: subject-skill
  award: ["bachelor's with honours"]
  gradeOf: { statement: qaa/social-policy-2026/4.8.b2, basis: stated }
  paraphrase: "At the typical standard, required for second-class honours, graduates understand and use the subject's main theories, concepts and perspectives, and see why they matter to other disciplines and to practitioners."
  quote: full   # the issuer's statement is in `source` (D-std-0014)
  audience: both
  subjects: inherited
- id: qaa/social-policy-2026/4.8.b3
  locator: { number: "4.8.b3", headingPath: ["Benchmark standards", "Undergraduate programmes"] }
  span: { start: 70884, end: 70973 }
  source: "Recognise how ideology, values, interests and norms can affect and shape social policies."
  stem: "4.8"
  statementType: threshold
  rung: threshold
  force: threshold
  level: fheq:6
  appliesTo: "honours graduates at the threshold standard (third-class)"
  addressee: learner
  verbs: ["recognise", "affect", "shape"]
  about: "ideology and values in policy"
  themes: [none]
  domain: subject-skill
  award: ["bachelor's with honours"]
  gradeOf: none
  paraphrase: "At the threshold for third-class honours, graduates see how ideology, values, interests and norms can influence and form social policies."
  quote: full   # the issuer's statement is in `source` (D-std-0014)
  audience: both
  subjects: inherited
- id: qaa/social-policy-2026/4.8.b3.excellent
  locator: { number: "4.8.b3.excellent", headingPath: ["Benchmark standards", "Undergraduate programmes"] }
  span: { start: 71137, end: 71261 }
  source: "Understand the relevance of and apply different ideological positions, values, and norms to the analysis of social policies."
  stem: "4.8"
  statementType: excellent
  rung: excellent
  force: must
  level: fheq:6
  appliesTo: "honours graduates at the excellent standard (first-class)"
  addressee: learner
  verbs: ["understand", "apply"]
  about: "ideological positions applied in analysis"
  themes: [none]
  domain: subject-skill
  award: ["bachelor's with honours"]
  gradeOf: { statement: qaa/social-policy-2026/4.8.b3.typical, basis: stated }
  paraphrase: "At the excellent standard, required for first-class honours, graduates understand why different ideological positions, values and norms matter and use them in analysing social policies."
  quote: full   # the issuer's statement is in `source` (D-std-0014)
  audience: both
  subjects: inherited
- id: qaa/social-policy-2026/4.8.b3.typical
  locator: { number: "4.8.b3.typical", headingPath: ["Benchmark standards", "Undergraduate programmes"] }
  span: { start: 70974, end: 71136 }
  source: "Distinguish between normative values and empirical claims, and critically reflect on how values underpin and shape policy making and relate to empirical evidence."
  stem: "4.8"
  statementType: typical
  rung: typical
  force: must
  level: fheq:6
  appliesTo: "honours graduates at the typical standard (second-class)"
  addressee: learner
  verbs: ["distinguish", "reflect", "underpin", "shape", "relate"]
  about: "values against evidence in policy making"
  themes: [none]
  domain: subject-skill
  award: ["bachelor's with honours"]
  gradeOf: { statement: qaa/social-policy-2026/4.8.b3, basis: stated }
  paraphrase: "At the typical standard, required for second-class honours, graduates tell normative values from empirical claims and reflect critically on how values drive policy making and connect with evidence."
  quote: full   # the issuer's statement is in `source` (D-std-0014)
  audience: both
  subjects: inherited
- id: qaa/social-policy-2026/4.8.b4
  locator: { number: "4.8.b4", headingPath: ["Benchmark standards", "Undergraduate programmes"] }
  span: { start: 71262, end: 71354 }
  source: "Understand and explain the importance of human need and lived experience to social policies."
  stem: "4.8"
  statementType: threshold
  rung: threshold
  force: threshold
  level: fheq:6
  appliesTo: "honours graduates at the threshold standard (third-class)"
  addressee: learner
  verbs: ["understand", "explain"]
  about: "need and lived experience in policy"
  themes: [none]
  domain: subject-skill
  award: ["bachelor's with honours"]
  gradeOf: none
  paraphrase: "At the threshold for third-class honours, graduates understand and explain why human need and lived experience matter to social policies."
  quote: full   # the issuer's statement is in `source` (D-std-0014)
  audience: both
  subjects: inherited
- id: qaa/social-policy-2026/4.8.b4.excellent
  locator: { number: "4.8.b4.excellent", headingPath: ["Benchmark standards", "Undergraduate programmes"] }
  span: { start: 71580, end: 71720 }
  source: "Critically evaluate the significance of lived experience to social policy analysis and policies and apply insights from this where relevant."
  stem: "4.8"
  statementType: excellent
  rung: excellent
  force: must
  level: fheq:6
  appliesTo: "honours graduates at the excellent standard (first-class)"
  addressee: learner
  verbs: ["evaluate", "apply"]
  about: "lived experience weighed and applied"
  themes: [none]
  domain: subject-skill
  award: ["bachelor's with honours"]
  gradeOf: { statement: qaa/social-policy-2026/4.8.b4.typical, basis: stated }
  paraphrase: "At the excellent standard, required for first-class honours, graduates critically judge how much lived experience matters to policy analysis and to policies, and use what it shows where it fits."
  quote: full   # the issuer's statement is in `source` (D-std-0014)
  audience: both
  subjects: inherited
- id: qaa/social-policy-2026/4.8.b4.typical
  locator: { number: "4.8.b4.typical", headingPath: ["Benchmark standards", "Undergraduate programmes"] }
  span: { start: 71355, end: 71579 }
  source: "Demonstrate sensitivity to the values and interests of others to appreciate the diversity of human needs and understand how they can be addressed through social policy analysis and policy making and implementation processes."
  stem: "4.8"
  statementType: typical
  rung: typical
  force: must
  level: fheq:6
  appliesTo: "honours graduates at the typical standard (second-class)"
  addressee: learner
  verbs: ["demonstrate", "appreciate", "understand", "addressed"]
  about: "sensitivity to others and to diverse needs"
  themes: [none]
  domain: subject-skill
  award: ["bachelor's with honours"]
  gradeOf: { statement: qaa/social-policy-2026/4.8.b4, basis: stated }
  paraphrase: "At the typical standard, required for second-class honours, graduates show sensitivity to other people's values and interests, appreciate how varied human needs are and understand how analysis, policy making and implementation can meet them."
  quote: full   # the issuer's statement is in `source` (D-std-0014)
  audience: both
  subjects: inherited
- id: qaa/social-policy-2026/4.8.b5
  locator: { number: "4.8.b5", headingPath: ["Benchmark standards", "Undergraduate programmes"] }
  span: { start: 71722, end: 71789 }
  source: "Assess and undertake Social Policy research using relevant methods."
  stem: "4.8"
  statementType: threshold
  rung: threshold
  force: threshold
  level: fheq:6
  appliesTo: "honours graduates at the threshold standard (third-class)"
  addressee: learner
  verbs: ["assess", "undertake", "using"]
  about: "assessing and doing research"
  themes: [none]
  domain: subject-skill
  award: ["bachelor's with honours"]
  gradeOf: none
  paraphrase: "At the threshold for third-class honours, graduates assess research in the subject and carry out their own with suitable methods."
  quote: full   # the issuer's statement is in `source` (D-std-0014)
  audience: both
  subjects: inherited
- id: qaa/social-policy-2026/4.8.b5.excellent
  locator: { number: "4.8.b5.excellent", headingPath: ["Benchmark standards", "Undergraduate programmes"] }
  span: { start: 71928, end: 72062 }
  source: "Plan, develop and undertake valid and robust Social Policy research using relevant methods and applying appropriate ethical standards."
  stem: "4.8"
  statementType: excellent
  rung: excellent
  force: must
  level: fheq:6
  appliesTo: "honours graduates at the excellent standard (first-class)"
  addressee: learner
  verbs: ["plan", "develop", "undertake", "using", "applying"]
  about: "valid, robust and ethical research"
  themes: [none]
  domain: subject-skill
  award: ["bachelor's with honours"]
  gradeOf: { statement: qaa/social-policy-2026/4.8.b5.typical, basis: stated }
  paraphrase: "At the excellent standard, required for first-class honours, graduates plan, build and carry out valid, robust research in the subject with suitable methods and proper ethical standards."
  quote: full   # the issuer's statement is in `source` (D-std-0014)
  audience: both
  subjects: inherited
- id: qaa/social-policy-2026/4.8.b5.typical
  locator: { number: "4.8.b5.typical", headingPath: ["Benchmark standards", "Undergraduate programmes"] }
  span: { start: 71791, end: 71927 }
  source: "Apply knowledge and experience of research methods to provide informed and critical commentary on the quality of Social Policy research."
  stem: "4.8"
  statementType: typical
  rung: typical
  force: must
  level: fheq:6
  appliesTo: "honours graduates at the typical standard (second-class)"
  addressee: learner
  verbs: ["apply", "provide"]
  about: "critical comment on research quality"
  themes: [none]
  domain: subject-skill
  award: ["bachelor's with honours"]
  gradeOf: { statement: qaa/social-policy-2026/4.8.b5, basis: stated }
  paraphrase: "At the typical standard, required for second-class honours, graduates draw on what they know and have done with research methods to comment critically and knowledgeably on how good research in the subject is."
  quote: full   # the issuer's statement is in `source` (D-std-0014)
  audience: both
  subjects: inherited
- id: qaa/social-policy-2026/4.9.b1
  locator: { number: "4.9.b1", headingPath: ["Benchmark standards", "Undergraduate programmes"] }
  span: { start: 72251, end: 72377 }
  source: "Reasoned arguments: the ability to construct and develop coherent and logical arguments, discuss issues and propose responses."
  stem: "4.9"
  statementType: threshold
  rung: threshold
  force: threshold
  level: fheq:6
  appliesTo: "honours graduates at the threshold standard (third-class)"
  addressee: learner
  verbs: ["construct", "develop", "discuss", "propose"]
  about: "coherent, logical argument"
  themes: [none]
  domain: generic-skill
  award: ["bachelor's with honours"]
  gradeOf: none
  paraphrase: "At the threshold for third-class honours, graduates build and develop arguments that hang together logically, talk issues through and suggest responses."
  quote: full   # the issuer's statement is in `source` (D-std-0014)
  audience: both
  subjects: inherited
- id: qaa/social-policy-2026/4.9.b1.excellent
  locator: { number: "4.9.b1.excellent", headingPath: ["Benchmark standards", "Undergraduate programmes"] }
  span: { start: 72567, end: 72732 }
  source: "Creative and independent reasoning: the ability to construct and develop a coherent, logical, valid and evidence-based argument to discuss issues and solve problems."
  stem: "4.9"
  statementType: excellent
  rung: excellent
  force: must
  level: fheq:6
  appliesTo: "honours graduates at the excellent standard (first-class)"
  addressee: learner
  verbs: ["construct", "develop", "discuss", "solve"]
  about: "creative, independent and valid argument"
  themes: [none]
  domain: generic-skill
  award: ["bachelor's with honours"]
  gradeOf: { statement: qaa/social-policy-2026/4.9.b1.typical, basis: stated }
  paraphrase: "At the excellent standard, required for first-class honours, graduates reason creatively and for themselves, building a coherent, valid argument grounded in evidence to discuss issues and solve problems."
  quote: full   # the issuer's statement is in `source` (D-std-0014)
  audience: both
  subjects: inherited
- id: qaa/social-policy-2026/4.9.b1.typical
  locator: { number: "4.9.b1.typical", headingPath: ["Benchmark standards", "Undergraduate programmes"] }
  span: { start: 72378, end: 72566 }
  source: "Independent reasoning: the ability to construct and develop substantiated, evidence-based arguments, discuss issues and solve problems using appropriate information and critical judgement."
  stem: "4.9"
  statementType: typical
  rung: typical
  force: must
  level: fheq:6
  appliesTo: "honours graduates at the typical standard (second-class)"
  addressee: learner
  verbs: ["construct", "develop", "discuss", "solve", "using"]
  about: "independent, evidence-based argument"
  themes: [none]
  domain: generic-skill
  award: ["bachelor's with honours"]
  gradeOf: { statement: qaa/social-policy-2026/4.9.b1, basis: stated }
  paraphrase: "At the typical standard, required for second-class honours, graduates reason for themselves, building arguments backed by evidence and using fitting information and critical judgement to discuss issues and solve problems."
  quote: full   # the issuer's statement is in `source` (D-std-0014)
  audience: both
  subjects: inherited
- id: qaa/social-policy-2026/4.9.b2
  locator: { number: "4.9.b2", headingPath: ["Benchmark standards", "Undergraduate programmes"] }
  span: { start: 72734, end: 72840 }
  source: "Analytical skills: the ability to read, listen/watch and accurately summarise, restate and assess content."
  stem: "4.9"
  statementType: threshold
  rung: threshold
  force: threshold
  level: fheq:6
  appliesTo: "honours graduates at the threshold standard (third-class)"
  addressee: learner
  verbs: ["read", "listen", "watch", "summarise", "restate", "assess"]
  about: "accurate summary and assessment of content"
  themes: [none]
  domain: generic-skill
  award: ["bachelor's with honours"]
  gradeOf: none
  paraphrase: "At the threshold for third-class honours, graduates read, listen to or watch material and summarise, restate and assess it accurately."
  quote: full   # the issuer's statement is in `source` (D-std-0014)
  audience: both
  subjects: inherited
- id: qaa/social-policy-2026/4.9.b2.excellent
  locator: { number: "4.9.b2.excellent", headingPath: ["Benchmark standards", "Undergraduate programmes"] }
  span: { start: 73022, end: 73197 }
  source: "Critical analytical skills: the ability to read, listen/watch material and critically analyse its strength and weaknesses, offering evidence-based alternatives where relevant."
  stem: "4.9"
  statementType: excellent
  rung: excellent
  force: must
  level: fheq:6
  appliesTo: "honours graduates at the excellent standard (first-class)"
  addressee: learner
  verbs: ["read", "listen", "watch", "analyse", "offering"]
  about: "critical analysis with evidenced alternatives"
  themes: [none]
  domain: generic-skill
  award: ["bachelor's with honours"]
  gradeOf: { statement: qaa/social-policy-2026/4.9.b2.typical, basis: stated }
  paraphrase: "At the excellent standard, required for first-class honours, graduates read, listen to or watch material, analyse its strengths and weaknesses critically and, where it helps, offer alternatives backed by evidence."
  quote: full   # the issuer's statement is in `source` (D-std-0014)
  audience: both
  subjects: inherited
- id: qaa/social-policy-2026/4.9.b2.typical
  locator: { number: "4.9.b2.typical", headingPath: ["Benchmark standards", "Undergraduate programmes"] }
  span: { start: 72841, end: 73021 }
  source: "Evaluative and analytical skills: the ability to critically and thoroughly assess and summarise assumptions, arguments and evidence from reports, documents and audiovisual sources."
  stem: "4.9"
  statementType: typical
  rung: typical
  force: must
  level: fheq:6
  appliesTo: "honours graduates at the typical standard (second-class)"
  addressee: learner
  verbs: ["assess", "summarise"]
  about: "thorough evaluation of assumptions and evidence"
  themes: [none]
  domain: generic-skill
  award: ["bachelor's with honours"]
  gradeOf: { statement: qaa/social-policy-2026/4.9.b2, basis: stated }
  paraphrase: "At the typical standard, required for second-class honours, graduates assess and summarise, thoroughly and critically, the assumptions, arguments and evidence in reports, documents and audiovisual material."
  quote: full   # the issuer's statement is in `source` (D-std-0014)
  audience: both
  subjects: inherited
- id: qaa/social-policy-2026/4.9.b3
  locator: { number: "4.9.b3", headingPath: ["Benchmark standards", "Undergraduate programmes"] }
  span: { start: 73198, end: 73305 }
  source: "Problem-solving skills: the ability to identify challenging social issues and assess alternative responses."
  stem: "4.9"
  statementType: threshold
  rung: threshold
  force: threshold
  level: fheq:6
  appliesTo: "honours graduates at the threshold standard (third-class)"
  addressee: learner
  verbs: ["identify", "assess"]
  about: "spotting hard issues and weighing responses"
  themes: [none]
  domain: generic-skill
  award: ["bachelor's with honours"]
  gradeOf: none
  paraphrase: "At the threshold for third-class honours, graduates identify hard social issues and weigh the different responses to them."
  quote: full   # the issuer's statement is in `source` (D-std-0014)
  audience: both
  subjects: inherited
- id: qaa/social-policy-2026/4.9.b3.excellent
  locator: { number: "4.9.b3.excellent", headingPath: ["Benchmark standards", "Undergraduate programmes"] }
  span: { start: 73420, end: 73547 }
  source: "Problem-solving skills: the ability to critically evaluate issues and develop and assess alternative evidence- based responses."
  stem: "4.9"
  statementType: excellent
  rung: excellent
  force: must
  level: fheq:6
  appliesTo: "honours graduates at the excellent standard (first-class)"
  addressee: learner
  verbs: ["evaluate", "develop", "assess"]
  about: "devising and testing evidenced responses"
  themes: [none]
  domain: generic-skill
  award: ["bachelor's with honours"]
  gradeOf: { statement: qaa/social-policy-2026/4.9.b3.typical, basis: stated }
  paraphrase: "At the excellent standard, required for first-class honours, graduates evaluate issues critically and devise and test different responses grounded in evidence."
  quote: full   # the issuer's statement is in `source` (D-std-0014)
  audience: both
  subjects: inherited
- id: qaa/social-policy-2026/4.9.b3.typical
  locator: { number: "4.9.b3.typical", headingPath: ["Benchmark standards", "Undergraduate programmes"] }
  span: { start: 73306, end: 73419 }
  source: "Problem-solving skills: the ability to critically analyse issues and assess alternative evidence-based solutions."
  stem: "4.9"
  statementType: typical
  rung: typical
  force: must
  level: fheq:6
  appliesTo: "honours graduates at the typical standard (second-class)"
  addressee: learner
  verbs: ["analyse", "assess"]
  about: "critical analysis and evidenced solutions"
  themes: [none]
  domain: generic-skill
  award: ["bachelor's with honours"]
  gradeOf: { statement: qaa/social-policy-2026/4.9.b3, basis: stated }
  paraphrase: "At the typical standard, required for second-class honours, graduates analyse issues critically and weigh different solutions that rest on evidence."
  quote: full   # the issuer's statement is in `source` (D-std-0014)
  audience: both
  subjects: inherited
- id: qaa/social-policy-2026/4.9.b4
  locator: { number: "4.9.b4", headingPath: ["Benchmark standards", "Undergraduate programmes"] }
  span: { start: 73552, end: 73733 }
  source: "Data collection and research skills: the ability to devise and undertake a research project, including planning, collecting and analysing data and writing, with supervisory support."
  stem: "4.9"
  statementType: threshold
  rung: threshold
  force: threshold
  level: fheq:6
  appliesTo: "honours graduates at the threshold standard (third-class)"
  addressee: learner
  verbs: ["devise", "undertake", "planning", "collecting", "analysing"]
  about: "a supervised research project"
  themes: [none]
  domain: generic-skill
  award: ["bachelor's with honours"]
  gradeOf: none
  paraphrase: "At the threshold for third-class honours, graduates design and complete a research project, from planning through data collection and analysis to writing, with a supervisor's help."
  quote: full   # the issuer's statement is in `source` (D-std-0014)
  audience: both
  subjects: inherited
- id: qaa/social-policy-2026/4.9.b4.excellent
  locator: { number: "4.9.b4.excellent", headingPath: ["Benchmark standards", "Undergraduate programmes"] }
  span: { start: 73893, end: 74065 }
  source: "Independent research skills: the ability to independently devise and undertake a research project, including planning, collecting and analysing data and writing up results."
  stem: "4.9"
  statementType: excellent
  rung: excellent
  force: must
  level: fheq:6
  appliesTo: "honours graduates at the excellent standard (first-class)"
  addressee: learner
  verbs: ["devise", "undertake", "planning", "collecting", "analysing"]
  about: "an independent research project"
  themes: [none]
  domain: generic-skill
  award: ["bachelor's with honours"]
  gradeOf: { statement: qaa/social-policy-2026/4.9.b4.typical, basis: stated }
  paraphrase: "At the excellent standard, required for first-class honours, graduates design and complete a research project on their own, from planning and data work to writing up findings."
  quote: full   # the issuer's statement is in `source` (D-std-0014)
  audience: both
  subjects: inherited
- id: qaa/social-policy-2026/4.9.b4.typical
  locator: { number: "4.9.b4.typical", headingPath: ["Benchmark standards", "Undergraduate programmes"] }
  span: { start: 73734, end: 73891 }
  source: "Data collection and research skills: the ability to work independently to retrieve, record, synthesise and analyse information gathered from various sources."
  stem: "4.9"
  statementType: typical
  rung: typical
  force: must
  level: fheq:6
  appliesTo: "honours graduates at the typical standard (second-class)"
  addressee: learner
  verbs: ["work", "retrieve", "record", "synthesise", "analyse"]
  about: "independent gathering and analysis of information"
  themes: [none]
  domain: generic-skill
  award: ["bachelor's with honours"]
  gradeOf: { statement: qaa/social-policy-2026/4.9.b4, basis: stated }
  paraphrase: "At the typical standard, required for second-class honours, graduates work on their own to find, record, combine and analyse information from a range of sources."
  quote: full   # the issuer's statement is in `source` (D-std-0014)
  audience: both
  subjects: inherited
- id: qaa/social-policy-2026/4.9.b5.excellent
  locator: { number: "4.9.b5.excellent", headingPath: ["Benchmark standards", "Undergraduate programmes"] }
  span: { start: 74066, end: 74198 }
  source: "Synthesis skills: the ability to accurately combine and integrate diverse information sources to develop new knowledge or arguments."
  stem: "4.9"
  statementType: excellent
  rung: excellent
  force: must
  level: fheq:6
  appliesTo: "honours graduates at the excellent standard (first-class)"
  addressee: learner
  verbs: ["combine", "integrate", "develop"]
  about: "synthesis into new knowledge or argument"
  themes: [none]
  domain: generic-skill
  award: ["bachelor's with honours"]
  gradeOf: none
  paraphrase: "At the excellent standard, required for first-class honours, graduates bring varied sources together accurately to build new knowledge or arguments."
  quote: full   # the issuer's statement is in `source` (D-std-0014)
  audience: both
  subjects: inherited
- id: qaa/social-policy-2026/4.10.b1
  locator: { number: "4.10.b1", headingPath: ["Benchmark standards", "Undergraduate programmes"] }
  span: { start: 74388, end: 74582 }
  source: "Communication and presentation skills: the ability to communicate and present effectively in writing, verbally/non-verbally and visually, to different audiences using appropriate technical aids."
  stem: "4.10"
  statementType: threshold
  rung: threshold
  force: threshold
  level: fheq:6
  appliesTo: "honours graduates at the threshold standard (third-class)"
  addressee: learner
  verbs: ["communicate", "present", "using"]
  about: "effective communication to varied audiences"
  themes: [none]
  domain: generic-skill
  award: ["bachelor's with honours"]
  gradeOf: none
  paraphrase: "At the threshold for third-class honours, graduates communicate and present well in writing, in speech and other forms, and visually, to varied audiences with suitable technical aids."
  quote: full   # the issuer's statement is in `source` (D-std-0014)
  audience: both
  subjects: inherited
- id: qaa/social-policy-2026/4.10.b1.excellent
  locator: { number: "4.10.b1.excellent", headingPath: ["Benchmark standards", "Undergraduate programmes"] }
  span: { start: 74795, end: 75072 }
  source: "Communication and presentation skills: the ability to articulate a coherent and complex argument and communicate ideas effectively both verbally/non-verbally and in writing, and, where appropriate, use technical aids to develop and deliver complex presentations to an audience."
  stem: "4.10"
  statementType: excellent
  rung: excellent
  force: must
  level: fheq:6
  appliesTo: "honours graduates at the excellent standard (first-class)"
  addressee: learner
  verbs: ["articulate", "communicate", "use", "develop", "deliver"]
  about: "complex argument put across; complex presentations"
  themes: [none]
  domain: generic-skill
  award: ["bachelor's with honours"]
  gradeOf: { statement: qaa/social-policy-2026/4.10.b1.typical, basis: stated }
  paraphrase: "At the excellent standard, required for first-class honours, graduates put a complex, coherent argument into words, communicate ideas well in speech and writing and, where useful, use technical aids to build and give complex presentations."
  quote: full   # the issuer's statement is in `source` (D-std-0014)
  audience: both
  subjects: inherited
- id: qaa/social-policy-2026/4.10.b1.typical
  locator: { number: "4.10.b1.typical", headingPath: ["Benchmark standards", "Undergraduate programmes"] }
  span: { start: 74583, end: 74794 }
  source: "Communication and presentation skills: to communicate effectively with different audiences across a range of formats, including written, verbal/non-verbal and visual, and to use technical aids where appropriate."
  stem: "4.10"
  statementType: typical
  rung: typical
  force: must
  level: fheq:6
  appliesTo: "honours graduates at the typical standard (second-class)"
  addressee: learner
  verbs: ["communicate", "use"]
  about: "effective communication across formats"
  themes: [none]
  domain: generic-skill
  award: ["bachelor's with honours"]
  gradeOf: { statement: qaa/social-policy-2026/4.10.b1, basis: stated }
  paraphrase: "At the typical standard, required for second-class honours, graduates communicate well with varied audiences in many formats, written, spoken and visual, using technical aids where useful."
  quote: full   # the issuer's statement is in `source` (D-std-0014)
  audience: both
  subjects: inherited
- id: qaa/social-policy-2026/4.10.b2
  locator: { number: "4.10.b2", headingPath: ["Benchmark standards", "Undergraduate programmes"] }
  span: { start: 75073, end: 75165 }
  source: "Self-directed learning: the ability to plan, organise and prioritise work to meet deadlines."
  stem: "4.10"
  statementType: threshold
  rung: threshold
  force: threshold
  level: fheq:6
  appliesTo: "honours graduates at the threshold standard (third-class)"
  addressee: learner
  verbs: ["plan", "organise", "prioritise", "meet"]
  about: "planning work to deadlines"
  themes: [none]
  domain: generic-skill
  award: ["bachelor's with honours"]
  gradeOf: none
  paraphrase: "At the threshold for third-class honours, graduates plan, organise and order their work so they meet deadlines."
  quote: full   # the issuer's statement is in `source` (D-std-0014)
  audience: both
  subjects: inherited
- id: qaa/social-policy-2026/4.10.b2.excellent
  locator: { number: "4.10.b2.excellent", headingPath: ["Benchmark standards", "Undergraduate programmes"] }
  span: { start: 75260, end: 75386 }
  source: "Self-directed learning: the ability to design projects, organise resources, locate sources and exercise independent judgement."
  stem: "4.10"
  statementType: excellent
  rung: excellent
  force: must
  level: fheq:6
  appliesTo: "honours graduates at the excellent standard (first-class)"
  addressee: learner
  verbs: ["design", "organise", "locate", "exercise"]
  about: "designing projects; independent judgement"
  themes: [none]
  domain: generic-skill
  award: ["bachelor's with honours"]
  gradeOf: { statement: qaa/social-policy-2026/4.10.b2.typical, basis: stated }
  paraphrase: "At the excellent standard, required for first-class honours, graduates design projects, marshal resources, find sources and use their own judgement."
  quote: full   # the issuer's statement is in `source` (D-std-0014)
  audience: both
  subjects: inherited
- id: qaa/social-policy-2026/4.10.b2.typical
  locator: { number: "4.10.b2.typical", headingPath: ["Benchmark standards", "Undergraduate programmes"] }
  span: { start: 75166, end: 75258 }
  source: "Self-directed learning: the ability to plan, manage time effectively and work independently."
  stem: "4.10"
  statementType: typical
  rung: typical
  force: must
  level: fheq:6
  appliesTo: "honours graduates at the typical standard (second-class)"
  addressee: learner
  verbs: ["plan", "manage", "work"]
  about: "time management and independent work"
  themes: [none]
  domain: generic-skill
  award: ["bachelor's with honours"]
  gradeOf: { statement: qaa/social-policy-2026/4.10.b2, basis: stated }
  paraphrase: "At the typical standard, required for second-class honours, graduates plan, use their time well and work on their own."
  quote: full   # the issuer's statement is in `source` (D-std-0014)
  audience: both
  subjects: inherited
- id: qaa/social-policy-2026/4.10.b3
  locator: { number: "4.10.b3", headingPath: ["Benchmark standards", "Undergraduate programmes"] }
  span: { start: 75387, end: 75470 }
  source: "Team and group working: the ability to form, engage and work effectively in groups."
  stem: "4.10"
  statementType: threshold
  rung: threshold
  force: threshold
  level: fheq:6
  appliesTo: "honours graduates at the threshold standard (third-class)"
  addressee: learner
  verbs: ["form", "engage", "work"]
  about: "effective group work"
  themes: [none]
  domain: generic-skill
  award: ["bachelor's with honours"]
  gradeOf: none
  paraphrase: "At the threshold for third-class honours, graduates form groups, take part and work well within them."
  quote: full   # the issuer's statement is in `source` (D-std-0014)
  audience: both
  subjects: inherited
- id: qaa/social-policy-2026/4.10.b3.excellent
  locator: { number: "4.10.b3.excellent", headingPath: ["Benchmark standards", "Undergraduate programmes"] }
  span: { start: 75590, end: 75698 }
  source: "Team and group working: the ability to initiate, form, engage constructively and work effectively in groups."
  stem: "4.10"
  statementType: excellent
  rung: excellent
  force: must
  level: fheq:6
  appliesTo: "honours graduates at the excellent standard (first-class)"
  addressee: learner
  verbs: ["initiate", "form", "engage", "work"]
  about: "starting groups and engaging constructively"
  themes: [none]
  domain: generic-skill
  award: ["bachelor's with honours"]
  gradeOf: { statement: qaa/social-policy-2026/4.10.b3.typical, basis: stated }
  paraphrase: "At the excellent standard, required for first-class honours, graduates start and form groups, engage constructively and work well within them."
  quote: full   # the issuer's statement is in `source` (D-std-0014)
  audience: both
  subjects: inherited
- id: qaa/social-policy-2026/4.10.b3.typical
  locator: { number: "4.10.b3.typical", headingPath: ["Benchmark standards", "Undergraduate programmes"] }
  span: { start: 75471, end: 75589 }
  source: "Teamwork skills: the ability to initiate, coordinate and contribute effectively to group work and collective projects."
  stem: "4.10"
  statementType: typical
  rung: typical
  force: must
  level: fheq:6
  appliesTo: "honours graduates at the typical standard (second-class)"
  addressee: learner
  verbs: ["initiate", "coordinate", "contribute"]
  about: "starting and coordinating group work"
  themes: [none]
  domain: generic-skill
  award: ["bachelor's with honours"]
  gradeOf: { statement: qaa/social-policy-2026/4.10.b3, basis: stated }
  paraphrase: "At the typical standard, required for second-class honours, graduates start, coordinate and contribute well to group work and shared projects."
  quote: full   # the issuer's statement is in `source` (D-std-0014)
  audience: both
  subjects: inherited
- id: qaa/social-policy-2026/4.10.b4
  locator: { number: "4.10.b4", headingPath: ["Benchmark standards", "Undergraduate programmes"] }
  span: { start: 75700, end: 75893 }
  source: "Technology skills: the ability to use existing and new technologies and show awareness of evolving technologies, including appropriate, specific use of generative artificial intelligence tools."
  stem: "4.10"
  statementType: threshold
  rung: threshold
  force: threshold
  level: fheq:6
  appliesTo: "honours graduates at the threshold standard (third-class)"
  addressee: learner
  verbs: ["use", "show"]
  about: "using technologies, generative AI included"
  themes: [none]
  domain: generic-skill
  award: ["bachelor's with honours"]
  gradeOf: none
  paraphrase: "At the threshold for third-class honours, graduates use current and new technologies, know about emerging ones and use generative AI tools fittingly for specific tasks."
  quote: full   # the issuer's statement is in `source` (D-std-0014)
  audience: both
  subjects: inherited
- id: qaa/social-policy-2026/4.10.b4.excellent
  locator: { number: "4.10.b4.excellent", headingPath: ["Benchmark standards", "Undergraduate programmes"] }
  span: { start: 76117, end: 76283 }
  source: "Technology skills: proficient ability to use existing, new and evolving technologies, including appropriate, specific use of generative artificial intelligence tools."
  stem: "4.10"
  statementType: excellent
  rung: excellent
  force: must
  level: fheq:6
  appliesTo: "honours graduates at the excellent standard (first-class)"
  addressee: learner
  verbs: ["use"]
  about: "proficient use of evolving technology"
  themes: [none]
  domain: generic-skill
  award: ["bachelor's with honours"]
  gradeOf: { statement: qaa/social-policy-2026/4.10.b4.typical, basis: stated }
  paraphrase: "At the excellent standard, required for first-class honours, graduates use current, new and emerging technologies proficiently, generative AI tools included where fitting."
  quote: full   # the issuer's statement is in `source` (D-std-0014)
  audience: both
  subjects: inherited
- id: qaa/social-policy-2026/4.10.b4.typical
  locator: { number: "4.10.b4.typical", headingPath: ["Benchmark standards", "Undergraduate programmes"] }
  span: { start: 75894, end: 76116 }
  source: "Technology skills: competent and confident use of a wide range of existing and new technologies to retrieve, analyse and present information, including appropriate, specific use of generative artificial intelligence tools."
  stem: "4.10"
  statementType: typical
  rung: typical
  force: must
  level: fheq:6
  appliesTo: "honours graduates at the typical standard (second-class)"
  addressee: learner
  verbs: ["retrieve", "analyse", "present"]
  about: "confident use of technology to handle information"
  themes: [none]
  domain: generic-skill
  award: ["bachelor's with honours"]
  gradeOf: { statement: qaa/social-policy-2026/4.10.b4, basis: stated }
  paraphrase: "At the typical standard, required for second-class honours, graduates use a wide range of current and new technologies competently and confidently to find, analyse and present information, generative AI tools included where fitting."
  quote: full   # the issuer's statement is in `source` (D-std-0014)
  audience: both
  subjects: inherited
- id: qaa/social-policy-2026/4.10.b5
  locator: { number: "4.10.b5", headingPath: ["Benchmark standards", "Undergraduate programmes"] }
  span: { start: 76288, end: 76404 }
  source: "Evidence and referencing skills: the ability to accurately reference sources to provide evidence for submitted work."
  stem: "4.10"
  statementType: threshold
  rung: threshold
  force: threshold
  level: fheq:6
  appliesTo: "honours graduates at the threshold standard (third-class)"
  addressee: learner
  verbs: ["reference", "provide"]
  about: "accurate referencing"
  themes: [none]
  domain: generic-skill
  award: ["bachelor's with honours"]
  gradeOf: none
  paraphrase: "At the threshold for third-class honours, graduates reference their sources accurately as evidence for the work they hand in."
  quote: full   # the issuer's statement is in `source` (D-std-0014)
  audience: both
  subjects: inherited
- id: qaa/social-policy-2026/4.10.b5.excellent
  locator: { number: "4.10.b5.excellent", headingPath: ["Benchmark standards", "Undergraduate programmes"] }
  span: { start: 76541, end: 76669 }
  source: "Evidence and referencing skills: the ability to locate and accurately reference sources in accordance with academic conventions."
  stem: "4.10"
  statementType: excellent
  rung: excellent
  force: must
  level: fheq:6
  appliesTo: "honours graduates at the excellent standard (first-class)"
  addressee: learner
  verbs: ["locate", "reference"]
  about: "finding and referencing sources to convention"
  themes: [none]
  domain: generic-skill
  award: ["bachelor's with honours"]
  gradeOf: { statement: qaa/social-policy-2026/4.10.b5.typical, basis: stated }
  paraphrase: "At the excellent standard, required for first-class honours, graduates find sources and reference them accurately as academic convention requires."
  quote: full   # the issuer's statement is in `source` (D-std-0014)
  audience: both
  subjects: inherited
- id: qaa/social-policy-2026/4.10.b5.typical
  locator: { number: "4.10.b5.typical", headingPath: ["Benchmark standards", "Undergraduate programmes"] }
  span: { start: 76405, end: 76540 }
  source: "Evidence and referencing skills: understand and correctly apply standard systems for accurate referencing in texts and reference lists."
  stem: "4.10"
  statementType: typical
  rung: typical
  force: must
  level: fheq:6
  appliesTo: "honours graduates at the typical standard (second-class)"
  addressee: learner
  verbs: ["understand", "apply"]
  about: "standard referencing systems"
  themes: [none]
  domain: generic-skill
  award: ["bachelor's with honours"]
  gradeOf: { statement: qaa/social-policy-2026/4.10.b5, basis: stated }
  paraphrase: "At the typical standard, required for second-class honours, graduates understand standard referencing systems and apply them correctly in the text and the reference list."
  quote: full   # the issuer's statement is in `source` (D-std-0014)
  audience: both
  subjects: inherited
- id: qaa/social-policy-2026/4.12.b1.masters
  locator: { number: "4.12.b1.masters", headingPath: ["Benchmark standards", "Master's programmes"] }
  span: { start: 77188, end: 77530 }
  source: "a sound understanding of the broader social policy landscape, alongside in-depth knowledge of at least one major area of Social Policy, such as, but not limited to, employment, housing, eco-social policies, health, family, pensions, tax, social security, education, social care, gender and social policy, and international and global policies"
  stem: "4.12"
  statementType: threshold
  rung: threshold
  force: describes
  level: fheq:7
  appliesTo: "master's graduates"
  addressee: learner
  verbs: []
  about: "breadth across the field with depth in one area"
  themes: [none]
  domain: knowledge
  award: ["master's"]
  gradeOf: none
  paraphrase: "Master's graduates are expected to show a sound grasp of the wider policy field with deep knowledge of at least one major area, such as housing, health, pensions, social security or global policy."
  quote: full   # the issuer's statement is in `source` (D-std-0014)
  audience: both
  subjects: inherited
- id: qaa/social-policy-2026/4.12.b2.masters
  locator: { number: "4.12.b2.masters", headingPath: ["Benchmark standards", "Master's programmes"] }
  span: { start: 77533, end: 77722 }
  source: "a thorough and comprehensive understanding of human needs, social justice, and individual and collective wellbeing in contemporary societies and their relationship to Social Policy analysis"
  stem: "4.12"
  statementType: threshold
  rung: threshold
  force: describes
  level: fheq:7
  appliesTo: "master's graduates"
  addressee: learner
  verbs: []
  about: "need, justice and wellbeing in policy analysis"
  themes: [none]
  domain: understanding
  award: ["master's"]
  gradeOf: none
  paraphrase: "Master's graduates are expected to show a thorough, full understanding of human need, social justice and personal and shared wellbeing today, and how they relate to policy analysis."
  quote: full   # the issuer's statement is in `source` (D-std-0014)
  audience: both
  subjects: inherited
- id: qaa/social-policy-2026/4.12.b3.masters
  locator: { number: "4.12.b3.masters", headingPath: ["Benchmark standards", "Master's programmes"] }
  span: { start: 77725, end: 77866 }
  source: "the capacity to navigate and apply core concepts and theoretical frameworks in Social Policy to critically evaluate research and scholarships"
  stem: "4.12"
  statementType: threshold
  rung: threshold
  force: describes
  level: fheq:7
  appliesTo: "master's graduates"
  addressee: learner
  verbs: ["navigate", "apply", "evaluate"]
  about: "core theory used to judge research"
  themes: [none]
  domain: understanding
  award: ["master's"]
  gradeOf: none
  paraphrase: "Master's graduates are expected to show the capacity to work with and apply the subject's core concepts and theories to judge research and scholarship critically."
  quote: full   # the issuer's statement is in `source` (D-std-0014)
  audience: both
  subjects: inherited
- id: qaa/social-policy-2026/4.12.b4.masters
  locator: { number: "4.12.b4.masters", headingPath: ["Benchmark standards", "Master's programmes"] }
  span: { start: 77869, end: 78045 }
  source: "a sound understanding of a specific dimension or manifestation of social injustices, how they are reproduced, sustained and addressed, including their particular policy context"
  stem: "4.12"
  statementType: threshold
  rung: threshold
  force: describes
  level: fheq:7
  appliesTo: "master's graduates"
  addressee: learner
  verbs: ["reproduced", "sustained", "addressed"]
  about: "one form of social injustice in depth"
  themes: [none]
  domain: understanding
  award: ["master's"]
  gradeOf: none
  paraphrase: "Master's graduates are expected to show a sound understanding of one particular form of social injustice, how it is reproduced, kept in place and tackled, and its policy setting."
  quote: full   # the issuer's statement is in `source` (D-std-0014)
  audience: both
  subjects: inherited
- id: qaa/social-policy-2026/4.12.b5.masters
  locator: { number: "4.12.b5.masters", headingPath: ["Benchmark standards", "Master's programmes"] }
  span: { start: 78048, end: 78221 }
  source: "the ability to recognise and demonstrate the relevance of norms, values and worldviews in defining social injustices, shaping policy processes and informing policy solutions"
  stem: "4.12"
  statementType: threshold
  rung: threshold
  force: describes
  level: fheq:7
  appliesTo: "master's graduates"
  addressee: learner
  verbs: ["recognise", "demonstrate", "defining", "shaping", "informing"]
  about: "norms and worldviews in injustice and policy"
  themes: [none]
  domain: understanding
  award: ["master's"]
  gradeOf: none
  paraphrase: "Master's graduates are expected to show the ability to recognise and make plain how norms, values and worldviews define injustice, shape policy processes and inform solutions."
  quote: full   # the issuer's statement is in `source` (D-std-0014)
  audience: both
  subjects: inherited
- id: qaa/social-policy-2026/4.12.b6.masters
  locator: { number: "4.12.b6.masters", headingPath: ["Benchmark standards", "Master's programmes"] }
  span: { start: 78224, end: 78399 }
  source: "awareness and appreciation of alternative research methods and the ability to design and undertake an independent dissertation or research project with appropriate supervision"
  stem: "4.12"
  statementType: threshold
  rung: threshold
  force: describes
  level: fheq:7
  appliesTo: "master's graduates"
  addressee: learner
  verbs: ["design", "undertake"]
  about: "research methods and a supervised dissertation"
  themes: [none]
  domain: subject-skill
  award: ["master's"]
  gradeOf: none
  paraphrase: "Master's graduates are expected to show knowledge of a range of research methods and the ability to design and carry out an independent, supervised dissertation or project."
  quote: full   # the issuer's statement is in `source` (D-std-0014)
  audience: both
  subjects: inherited
- id: qaa/social-policy-2026/4.13.b1.masters
  locator: { number: "4.13.b1.masters", headingPath: ["Benchmark standards", "Master's programmes"] }
  span: { start: 78559, end: 78820 }
  source: "in-depth understanding of social policy making, practice and impact, including understanding policy in relevant local, national and international contexts, and significant social and economic differences among jurisdictions, and variations in welfare histories."
  stem: "4.13"
  statementType: threshold
  rung: threshold
  force: describes
  level: fheq:7
  appliesTo: "master's graduates"
  addressee: learner
  verbs: []
  about: "policy making and impact across jurisdictions"
  themes: [none]
  domain: subject-skill
  award: ["master's"]
  gradeOf: none
  paraphrase: "Master's graduates are expected to show deep understanding of how policy is made, practised and felt, at local, national and international scale, across differing jurisdictions and welfare histories."
  quote: full   # the issuer's statement is in `source` (D-std-0014)
  audience: both
  subjects: inherited
- id: qaa/social-policy-2026/4.13.b2.masters
  locator: { number: "4.13.b2.masters", headingPath: ["Benchmark standards", "Master's programmes"] }
  span: { start: 78823, end: 78969 }
  source: "awareness of and ability to undertake comparative analyses of differences in political regime types, policy-making styles and substantive policies"
  stem: "4.13"
  statementType: threshold
  rung: threshold
  force: describes
  level: fheq:7
  appliesTo: "master's graduates"
  addressee: learner
  verbs: ["undertake"]
  about: "comparative analysis of regimes and policies"
  themes: [none]
  domain: subject-skill
  award: ["master's"]
  gradeOf: none
  paraphrase: "Master's graduates are expected to show the ability to carry out comparative analysis of regime types, policy-making styles and actual policies."
  quote: full   # the issuer's statement is in `source` (D-std-0014)
  audience: both
  subjects: inherited
- id: qaa/social-policy-2026/4.13.b3.masters
  locator: { number: "4.13.b3.masters", headingPath: ["Benchmark standards", "Master's programmes"] }
  span: { start: 78972, end: 79272 }
  source: "identify and understand the roles, responsibilities and perspectives of key stakeholders in the social policy landscape – including service users, providers, practitioners,\n\n27\npolicymakers and professionals – and the openness of policy-making structures to democratic participation and co-production"
  stem: "4.13"
  statementType: threshold
  rung: threshold
  force: describes
  level: fheq:7
  appliesTo: "master's graduates"
  addressee: learner
  verbs: ["identify", "understand"]
  about: "stakeholders and democratic participation"
  themes: [none]
  domain: subject-skill
  award: ["master's"]
  gradeOf: none
  paraphrase: "Master's graduates are expected to show the ability to identify and understand what key stakeholders, from service users to policymakers, do and think, and how open policy making is to democratic participation and co-production."
  quote: full   # the issuer's statement is in `source` (D-std-0014)
  audience: both
  subjects: inherited
- id: qaa/social-policy-2026/4.13.b4.masters
  locator: { number: "4.13.b4.masters", headingPath: ["Benchmark standards", "Master's programmes"] }
  span: { start: 79275, end: 79450 }
  source: "a critical understanding of how social policy making, development and implementation impact upon and are experienced by service users, benefit claimants and the broader public"
  stem: "4.13"
  statementType: threshold
  rung: threshold
  force: describes
  level: fheq:7
  appliesTo: "master's graduates"
  addressee: learner
  verbs: ["impact", "experienced"]
  about: "how policy is felt by users and the public"
  themes: [none]
  domain: subject-skill
  award: ["master's"]
  gradeOf: none
  paraphrase: "Master's graduates are expected to show critical understanding of how making and delivering policy affects, and is lived by, service users, claimants and the public."
  quote: full   # the issuer's statement is in `source` (D-std-0014)
  audience: both
  subjects: inherited
- id: qaa/social-policy-2026/4.13.b5.masters
  locator: { number: "4.13.b5.masters", headingPath: ["Benchmark standards", "Master's programmes"] }
  span: { start: 79453, end: 79571 }
  source: "a critical understanding and application of equality issues and their intersections to the analysis of social policies"
  stem: "4.13"
  statementType: threshold
  rung: threshold
  force: describes
  level: fheq:7
  appliesTo: "master's graduates"
  addressee: learner
  verbs: []
  about: "intersecting equality issues in analysis"
  themes: [none]
  domain: subject-skill
  award: ["master's"]
  gradeOf: none
  paraphrase: "Master's graduates are expected to show critical understanding of equality issues and how they intersect, applied to policy analysis."
  quote: full   # the issuer's statement is in `source` (D-std-0014)
  audience: both
  subjects: inherited
- id: qaa/social-policy-2026/4.13.b6.masters
  locator: { number: "4.13.b6.masters", headingPath: ["Benchmark standards", "Master's programmes"] }
  span: { start: 79574, end: 79885 }
  source: "a critical and reflective understanding of the importance of diversity, equity, inclusion, decolonisation, equality issues and environmental sustainability across all stages of social policy research and practice, in local, national and global contexts, and how these operate in different cultures and countries"
  stem: "4.13"
  statementType: threshold
  rung: threshold
  force: describes
  level: fheq:7
  appliesTo: "master's graduates"
  addressee: learner
  verbs: ["operate"]
  about: "EDI, decolonisation and sustainability in research and practice"
  themes: [none]
  domain: subject-skill
  award: ["master's"]
  gradeOf: none
  paraphrase: "Master's graduates are expected to show critical, reflective understanding of why diversity, equity, inclusion, decolonisation, equality and environmental sustainability matter at every stage of research and practice, locally to globally and across cultures."
  quote: full   # the issuer's statement is in `source` (D-std-0014)
  audience: both
  subjects: inherited
- id: qaa/social-policy-2026/4.13.b7.masters
  locator: { number: "4.13.b7.masters", headingPath: ["Benchmark standards", "Master's programmes"] }
  span: { start: 79888, end: 80026 }
  source: "critical and constructive engagement with topical discussions on social injustices and social policy reform nationally and internationally"
  stem: "4.13"
  statementType: threshold
  rung: threshold
  force: describes
  level: fheq:7
  appliesTo: "master's graduates"
  addressee: learner
  verbs: []
  about: "engaging with current reform debates"
  themes: [none]
  domain: subject-skill
  award: ["master's"]
  gradeOf: none
  paraphrase: "Master's graduates are expected to show critical, constructive engagement with current debates on injustice and policy reform at home and abroad."
  quote: full   # the issuer's statement is in `source` (D-std-0014)
  audience: both
  subjects: inherited
- id: qaa/social-policy-2026/4.13.b8.masters
  locator: { number: "4.13.b8.masters", headingPath: ["Benchmark standards", "Master's programmes"] }
  span: { start: 80029, end: 80111 }
  source: "critical analysis of how related disciplines contribute to Social Policy analyses."
  stem: "4.13"
  statementType: threshold
  rung: threshold
  force: describes
  level: fheq:7
  appliesTo: "master's graduates"
  addressee: learner
  verbs: []
  about: "what neighbouring disciplines contribute"
  themes: [none]
  domain: subject-skill
  award: ["master's"]
  gradeOf: none
  paraphrase: "Master's graduates are expected to show critical analysis of what neighbouring disciplines bring to policy analysis."
  quote: full   # the issuer's statement is in `source` (D-std-0014)
  audience: both
  subjects: inherited
- id: qaa/social-policy-2026/4.14.b1.masters
  locator: { number: "4.14.b1.masters", headingPath: ["Benchmark standards", "Master's programmes"] }
  span: { start: 80278, end: 80358 }
  source: "capacity to assess and apply quantitative, qualitative or mixed methods research"
  stem: "4.14"
  statementType: threshold
  rung: threshold
  force: describes
  level: fheq:7
  appliesTo: "master's graduates"
  addressee: learner
  verbs: ["assess", "apply"]
  about: "judging and using research of every kind"
  themes: [none]
  domain: generic-skill
  award: ["master's"]
  gradeOf: none
  paraphrase: "Master's graduates are expected to show the capacity to judge and use quantitative, qualitative or mixed-methods research."
  quote: full   # the issuer's statement is in `source` (D-std-0014)
  audience: both
  subjects: inherited
- id: qaa/social-policy-2026/4.14.b2.masters
  locator: { number: "4.14.b2.masters", headingPath: ["Benchmark standards", "Master's programmes"] }
  span: { start: 80361, end: 80467 }
  source: "a developed ability to collect data using appropriate quantitative, qualitative or mixed method approaches"
  stem: "4.14"
  statementType: threshold
  rung: threshold
  force: describes
  level: fheq:7
  appliesTo: "master's graduates"
  addressee: learner
  verbs: ["collect", "using"]
  about: "collecting data by fitting methods"
  themes: [none]
  domain: generic-skill
  award: ["master's"]
  gradeOf: none
  paraphrase: "Master's graduates are expected to show a developed ability to gather data with fitting quantitative, qualitative or mixed approaches."
  quote: full   # the issuer's statement is in `source` (D-std-0014)
  audience: both
  subjects: inherited
- id: qaa/social-policy-2026/4.14.b3.masters
  locator: { number: "4.14.b3.masters", headingPath: ["Benchmark standards", "Master's programmes"] }
  span: { start: 80470, end: 80546 }
  source: "understanding and application of the principles of ethical research practice"
  stem: "4.14"
  statementType: threshold
  rung: threshold
  force: describes
  level: fheq:7
  appliesTo: "master's graduates"
  addressee: learner
  verbs: []
  about: "ethical research practice"
  themes: [none]
  domain: generic-skill
  award: ["master's"]
  gradeOf: none
  paraphrase: "Master's graduates are expected to show understanding and use of the principles of ethical research."
  quote: full   # the issuer's statement is in `source` (D-std-0014)
  audience: both
  subjects: inherited
- id: qaa/social-policy-2026/4.14.b4.masters
  locator: { number: "4.14.b4.masters", headingPath: ["Benchmark standards", "Master's programmes"] }
  span: { start: 80549, end: 80724 }
  source: "awareness and appreciation of alternative research methods and the ability to design and undertake an independent dissertation or research project with appropriate supervision"
  stem: "4.14"
  statementType: threshold
  rung: threshold
  force: describes
  level: fheq:7
  appliesTo: "master's graduates"
  addressee: learner
  verbs: ["design", "undertake"]
  about: "research methods and a supervised dissertation (repeated from 4.12)"
  themes: [none]
  domain: generic-skill
  award: ["master's"]
  gradeOf: none
  paraphrase: "Master's graduates are expected to show knowledge of different research methods and the ability to design and carry out an independent, supervised dissertation or project."
  quote: full   # the issuer's statement is in `source` (D-std-0014)
  audience: both
  subjects: inherited
- id: qaa/social-policy-2026/4.14.b5.masters
  locator: { number: "4.14.b5.masters", headingPath: ["Benchmark standards", "Master's programmes"] }
  span: { start: 80727, end: 80834 }
  source: "reflexive capacity to evaluate feedback to improve writing and enhance the quality of argument and analysis"
  stem: "4.14"
  statementType: threshold
  rung: threshold
  force: describes
  level: fheq:7
  appliesTo: "master's graduates"
  addressee: learner
  verbs: ["evaluate", "improve", "enhance"]
  about: "using feedback to improve"
  themes: [none]
  domain: generic-skill
  award: ["master's"]
  gradeOf: none
  paraphrase: "Master's graduates are expected to show the reflexive capacity to weigh feedback and use it to improve writing, argument and analysis."
  quote: full   # the issuer's statement is in `source` (D-std-0014)
  audience: both
  subjects: inherited
- id: qaa/social-policy-2026/4.14.b6.masters
  locator: { number: "4.14.b6.masters", headingPath: ["Benchmark standards", "Master's programmes"] }
  span: { start: 80837, end: 80943 }
  source: "expertise in scholarly practice, including locating relevant information sources and academic referencing."
  stem: "4.14"
  statementType: threshold
  rung: threshold
  force: describes
  level: fheq:7
  appliesTo: "master's graduates"
  addressee: learner
  verbs: ["locating"]
  about: "expert scholarly practice"
  themes: [none]
  domain: generic-skill
  award: ["master's"]
  gradeOf: none
  paraphrase: "Master's graduates are expected to show expert scholarly practice, from finding relevant sources to academic referencing."
  quote: full   # the issuer's statement is in `source` (D-std-0014)
  audience: both
  subjects: inherited
- id: qaa/social-policy-2026/4.15.b1.masters
  locator: { number: "4.15.b1.masters", headingPath: ["Benchmark standards", "Master's programmes"] }
  span: { start: 81110, end: 81168 }
  source: "critical, reflexive and independent approaches to learning"
  stem: "4.15"
  statementType: threshold
  rung: threshold
  force: describes
  level: fheq:7
  appliesTo: "master's graduates"
  addressee: learner
  verbs: []
  about: "critical, reflexive, independent learning"
  themes: [none]
  domain: generic-skill
  award: ["master's"]
  gradeOf: none
  paraphrase: "Master's graduates are expected to show critical, reflexive and independent ways of learning."
  quote: full   # the issuer's statement is in `source` (D-std-0014)
  audience: both
  subjects: inherited
- id: qaa/social-policy-2026/4.15.b2.masters
  locator: { number: "4.15.b2.masters", headingPath: ["Benchmark standards", "Master's programmes"] }
  span: { start: 81171, end: 81287 }
  source: "critical evaluation of, and commitment to, creating social value and public service contributing to social wellbeing"
  stem: "4.15"
  statementType: threshold
  rung: threshold
  force: describes
  level: fheq:7
  appliesTo: "master's graduates"
  addressee: learner
  verbs: ["creating", "contributing"]
  about: "commitment to social value and public service"
  themes: [none]
  domain: generic-skill
  award: ["master's"]
  gradeOf: none
  paraphrase: "Master's graduates are expected to show commitment to public service and to adding social value for wellbeing, with a critical eye on both."
  quote: full   # the issuer's statement is in `source` (D-std-0014)
  audience: both
  subjects: inherited
- id: qaa/social-policy-2026/4.15.b3.masters
  locator: { number: "4.15.b3.masters", headingPath: ["Benchmark standards", "Master's programmes"] }
  span: { start: 81290, end: 81403 }
  source: "critically reflective identification of learning needs, to enhance professional practice and personal development"
  stem: "4.15"
  statementType: threshold
  rung: threshold
  force: describes
  level: fheq:7
  appliesTo: "master's graduates"
  addressee: learner
  verbs: ["enhance"]
  about: "naming learning needs for growth"
  themes: [none]
  domain: generic-skill
  award: ["master's"]
  gradeOf: none
  paraphrase: "Master's graduates are expected to show critically reflective awareness of what they still need to learn, for professional and personal growth."
  quote: full   # the issuer's statement is in `source` (D-std-0014)
  audience: both
  subjects: inherited
- id: qaa/social-policy-2026/4.15.b4.masters
  locator: { number: "4.15.b4.masters", headingPath: ["Benchmark standards", "Master's programmes"] }
  span: { start: 81406, end: 81583 }
  source: "evaluation and application of practices of engaging productively and contributing effectively in collaborative, multicultural, and diverse environments domestically and globally"
  stem: "4.15"
  statementType: threshold
  rung: threshold
  force: describes
  level: fheq:7
  appliesTo: "master's graduates"
  addressee: learner
  verbs: ["engaging", "contributing"]
  about: "working well in diverse, multicultural settings"
  themes: [none]
  domain: generic-skill
  award: ["master's"]
  gradeOf: none
  paraphrase: "Master's graduates are expected to show the ability to evaluate and use ways of working productively in collaborative, multicultural and diverse settings at home and abroad."
  quote: full   # the issuer's statement is in `source` (D-std-0014)
  audience: both
  subjects: inherited
- id: qaa/social-policy-2026/4.15.b5.masters
  locator: { number: "4.15.b5.masters", headingPath: ["Benchmark standards", "Master's programmes"] }
  span: { start: 81586, end: 81794 }
  source: "awareness of and familiarity with evolving technologies, including generative artificial intelligence tools, their strengths and limitations, and the ethical implications of their use in research and writing."
  stem: "4.15"
  statementType: threshold
  rung: threshold
  force: describes
  level: fheq:7
  appliesTo: "master's graduates"
  addressee: learner
  verbs: []
  about: "emerging technology and generative AI, ethically"
  themes: [none]
  domain: generic-skill
  award: ["master's"]
  gradeOf: none
  paraphrase: "Master's graduates are expected to show familiarity with emerging technologies, generative AI among them, their strengths, limits and ethical questions in research and writing."
  quote: full   # the issuer's statement is in `source` (D-std-0014)
  audience: both
  subjects: inherited
```

### S4a Audience versions
<!-- label: both; status: drafted; basis: primary. forPractitioner: for the programme designer or teacher. forBeneficiary: for the student, second person, naming no issuer. author-agent-written: instructions to an AI agent writing about the statement (a course document, a handbook, an outcome, a report). author-agent-dialogue: instructions to an AI agent using the statement in conversation (with a student, a teacher or a programme team). Written fresh from the held text alone (benchmark rule 6; Abbott, 15:42). -->
```yaml
- statement: qaa/social-policy-2026/1.7
  forPractitioner: { text: "Teach how social policy works at local, national and international scale, with the principle of subsidiarity, so that students should understand it.", rewrite: light, force: should, status: drafted }
  forBeneficiary: { text: "You should understand how social policy works locally, nationally and internationally, including subsidiarity: dealing with needs at the nearest level that can handle them.", rewrite: full, force: should, status: drafted }
  author-agent-written: "Present this as an expectation of Social Policy students, in should, for the honours degree at FHEQ Level 6 (FQHEIS Level 10): policy across levels; subsidiarity. Cite it as (QAA, 2026, Social Policy Subject Benchmark Statement, para 1.7). Do not call it a regulatory requirement or a rung of the section 4 standards. Set it beside 1.12, 3.2, 4.7.b2 and qaa/fheq-2024/4.15.b1 and spine:6."
  author-agent-dialogue: "Raise this when devolution, local government or international policy come up. With a student, put it in plain second-person words; with staff, frame it as something the course should help students reach. Ask: \"Which level of government is best placed to meet the need you are studying, and why?\" Avoid reading the paragraph aloud or treating it as a graded standard."
- statement: qaa/social-policy-2026/1.14
  forPractitioner: { text: "Build the link between human wellbeing and planetary health into the curriculum: the subject must recognise sustainability as central to welfare, so that graduates can engage critically with climate, energy and resource policy.", rewrite: light, force: must, status: drafted }
  forBeneficiary: { text: "not-applicable: a requirement on the discipline and its curricula; the student meets it in what is taught", rewrite: full, force: must, status: drafted }
  author-agent-written: "Treat this as a duty, in must, on the discipline and those who design its curricula, not a learner outcome: environmental sustainability central to welfare. It holds for Social Policy courses at the levels the statement covers, not for one level. Cite it as (QAA, 2026, Social Policy Subject Benchmark Statement, para 1.14). Do not present it as a regulatory requirement or turn it into a task for the student; set it beside 1.44 to 1.53, 3.3.b7, 3.3.b20 and std:doc:qaa-advancehe-esd-2021-guidance."
  author-agent-dialogue: "Raise this when a team reviews how sustainability runs through the curriculum. With the programme team, frame it as practice they plan for and ask \"Where does the course connect welfare to ecological limits, beyond a single module?\" Do not put it to a student as their own duty; a student may only be told what the course should offer them."
- statement: qaa/social-policy-2026/1.17
  forPractitioner: { text: "Students must develop an appreciation of how policies are designed, delivered and evaluated, and of policy-making theory; give every route room for it.", rewrite: light, force: must, status: drafted }
  forBeneficiary: { text: "You must come to appreciate how social policies are designed, carried out and evaluated, and the wider theories of how policy gets made.", rewrite: full, force: must, status: drafted }
  author-agent-written: "Present this as an expectation of Social Policy students, in must, for the honours degree at FHEQ Level 6 (FQHEIS Level 10): policy design, implementation, evaluation and theory. Cite it as (QAA, 2026, Social Policy Subject Benchmark Statement, para 1.17). Do not call it a regulatory requirement or a rung of the section 4 standards. Set it beside 2.2.b5, 3.3.b9, 4.7.b3 and qaa/fheq-2024/4.15.b1 and spine:6."
  author-agent-dialogue: "Raise this when a student asks why policy-making theory matters. With a student, put it in plain second-person words; with staff, frame it as something the course should help students reach. Ask: \"Could you trace one policy from its design through to how it was evaluated?\" Avoid reading the paragraph aloud or treating it as a graded standard."
- statement: qaa/social-policy-2026/1.20
  forPractitioner: { text: "Give students room to name their own values, hear others' and set both against research, as they should in a normative subject.", rewrite: light, force: should, status: drafted }
  forBeneficiary: { text: "Because your subject is about values as well as facts, you should recognise your own values, respect other people's and use research to shape your understanding.", rewrite: full, force: should, status: drafted }
  author-agent-written: "Present this as an expectation of Social Policy students, in should, for the honours degree at FHEQ Level 6 (FQHEIS Level 10): own and others' values, with research. Cite it as (QAA, 2026, Social Policy Subject Benchmark Statement, para 1.20). Do not call it a regulatory requirement or a rung of the section 4 standards. Set it beside 1.38, 1.39, 4.8.b3 and qaa/fheq-2024/4.15.b4 and spine:6."
  author-agent-dialogue: "Raise this when values or politics come up in class or a student's position is challenged. With a student, put it in plain second-person words; with staff, frame it as something the course should help students reach. Ask: \"Which of your own values shapes how you see this issue, and what does the research say?\" Avoid reading the paragraph aloud or treating it as a graded standard."
- statement: qaa/social-policy-2026/1.24
  forPractitioner: { text: "Teach analysis that must take in continuing colonial legacies, and use decolonial frameworks when examining international policy and the conditions attached to its funding.", rewrite: light, force: must, status: drafted }
  forBeneficiary: { text: "Your analysis must look at colonial legacies that continue today, not only at history, and you should use decolonial frameworks when you examine international policy and who funds it.", rewrite: full, force: must, status: drafted }
  author-agent-written: "Present this as an expectation of Social Policy students, in must, for the honours degree at FHEQ Level 6 (FQHEIS Level 10): colonial legacies in analysis. Cite it as (QAA, 2026, Social Policy Subject Benchmark Statement, para 1.24). Do not call it a regulatory requirement or a rung of the section 4 standards. Set it beside 1.21 to 1.27, 2.5, 3.3.b2 and qaa/fheq-2024/4.15.b7 and spine:6."
  author-agent-dialogue: "Raise this when decolonisation, empire or international aid come up. With a student, put it in plain second-person words; with staff, frame it as something the course should help students reach. Ask: \"Whose ideas and interests shaped this international policy, and does their legacy still show?\" Avoid reading the paragraph aloud or treating it as a graded standard."
- statement: qaa/social-policy-2026/1.27
  forPractitioner: { text: "Widen reading lists and analyses so that teaching challenges the colonial and neocolonial assumptions in the subject, as it should.", rewrite: light, force: should, status: drafted }
  forBeneficiary: { text: "not-applicable: a duty on those who teach the subject", rewrite: full, force: should, status: drafted }
  author-agent-written: "Treat this as a duty, in should, on those who teach the subject, not a learner outcome: teaching that challenges colonial assumptions. It holds for Social Policy courses at the levels the statement covers, not for one level. Cite it as (QAA, 2026, Social Policy Subject Benchmark Statement, para 1.27). Do not present it as a regulatory requirement or turn it into a task for the student; set it beside 1.21 to 1.26, 4.13.b6.masters and theme:edi."
  author-agent-dialogue: "Raise this when a team reviews reading lists or decolonises the curriculum. With the programme team, frame it as practice they plan for and ask \"Which theories on this module come from outside the Global North, and which assumptions do they challenge?\" Do not put it to a student as their own duty; a student may only be told what the course should offer them."
- statement: qaa/social-policy-2026/1.29
  forPractitioner: { text: "Plan early teaching for students new to the subject, drawing on what they know from lived experience, the media and public debate.", rewrite: light, force: should, status: drafted }
  forBeneficiary: { text: "not-applicable: a duty on teaching staff", rewrite: full, force: should, status: drafted }
  author-agent-written: "Treat this as a duty, in should, on teaching staff, not a learner outcome: support for students new to the subject. It holds for Social Policy courses at the levels the statement covers, not for one level. Cite it as (QAA, 2026, Social Policy Subject Benchmark Statement, para 1.29). Do not present it as a regulatory requirement or turn it into a task for the student; set it beside 1.30, 1.31 and 3.9."
  author-agent-dialogue: "Raise this when a team plans first-year teaching or induction. With the programme team, frame it as practice they plan for and ask \"How does first-year teaching build on what students already know from life and the news?\" Do not put it to a student as their own duty; a student may only be told what the course should offer them."
- statement: qaa/social-policy-2026/1.31
  forPractitioner: { text: "Review awarding gaps by protected characteristic and beyond, socio-economic status included, and set support so every group can engage; this should shape programme and teaching design.", rewrite: light, force: should, status: drafted }
  forBeneficiary: { text: "not-applicable: a duty on those who design and run courses", rewrite: full, force: should, status: drafted }
  author-agent-written: "Treat this as a duty, in should, on those who design programmes and provision, not a learner outcome: design for diverse needs; awarding gaps. It holds for Social Policy courses at the levels the statement covers, not for one level. Cite it as (QAA, 2026, Social Policy Subject Benchmark Statement, para 1.31). Do not present it as a regulatory requirement or turn it into a task for the student; set it beside 1.30, 1.32, 3.13.b6 and the Equality Act 2010 the statement cites."
  author-agent-dialogue: "Raise this when a team examines awarding gaps or support. With the programme team, frame it as practice they plan for and ask \"Which groups of students are awarded fewer good degrees on this course, and what support is aimed at them?\" Do not put it to a student as their own duty; a student may only be told what the course should offer them."
- statement: qaa/social-policy-2026/1.36
  forPractitioner: { text: "Check programme, teaching and assessment design against recognised EDI guidance, such as QAA's inclusive subject communities advice.", rewrite: light, force: should, status: drafted }
  forBeneficiary: { text: "not-applicable: a duty on those who design programmes, teaching and assessment", rewrite: full, force: should, status: drafted }
  author-agent-written: "Treat this as a duty, in should, on those who design programmes, teaching and assessment, not a learner outcome: good EDI practice in design. It holds for Social Policy courses at the levels the statement covers, not for one level. Cite it as (QAA, 2026, Social Policy Subject Benchmark Statement, para 1.36). Do not present it as a regulatory requirement or turn it into a task for the student; set it beside 1.35 (the statement's definitions of equity, diversity and inclusion), 1.31 and 3.13."
  author-agent-dialogue: "Raise this when a team designs or revalidates a programme. With the programme team, frame it as practice they plan for and ask \"Which EDI guidance did you check this design against, and what changed?\" Do not put it to a student as their own duty; a student may only be told what the course should offer them."
- statement: qaa/social-policy-2026/1.39
  forPractitioner: { text: "Build reflection on inclusion and positionality into the course so that graduates will be able to examine how their identity shapes their work and lead diverse teams fairly.", rewrite: light, force: will, status: drafted }
  forBeneficiary: { text: "You will be able to reflect on how inclusive your work is and how your own background and identity shape your views, and to work and lead with others fairly and inclusively.", rewrite: full, force: will, status: drafted }
  author-agent-written: "Present this as an expectation of Social Policy students, in will, for the honours degree at FHEQ Level 6 (FQHEIS Level 10): inclusive, reflexive practice. Cite it as (QAA, 2026, Social Policy Subject Benchmark Statement, para 1.39). Do not call it a regulatory requirement or a rung of the section 4 standards. Set it beside 1.38, 1.20, 4.10.b3 and qaa/fheq-2024/4.15.b9.1 and spine:6."
  author-agent-dialogue: "Raise this when a student reflects on placement, group work or their own position. With a student, put it in plain second-person words; with staff, frame it as something the course should help students reach. Ask: \"How might your own background have shaped the way you approached this piece of work?\" Avoid reading the paragraph aloud or treating it as a graded standard."
- statement: qaa/social-policy-2026/1.42.b1
  forPractitioner: { text: "Mix teaching modes and assessment types across the programme so that every student finds ways in.", rewrite: light, force: should, status: drafted }
  forBeneficiary: { text: "not-applicable: a duty on the provider for accessible teaching", rewrite: full, force: should, status: drafted }
  author-agent-written: "Treat this as a duty, in should, on the provider, not a learner outcome: varied teaching and assessment modes. It holds for Social Policy courses at the levels the statement covers, not for one level. Cite it as (QAA, 2026, Social Policy Subject Benchmark Statement, para 1.42.b1). Do not present it as a regulatory requirement or turn it into a task for the student; set it beside 1.40, 1.43, 3.13 and the Equality Act 2010 duties named in 1.40."
  author-agent-dialogue: "Raise this when a team designs teaching and assessment or a disabled student asks about support. With the programme team, frame it as practice they plan for and ask \"How many different assessment types does a student meet across the programme?\" Do not put it to a student as their own duty; a student may only be told what the course should offer them."
- statement: qaa/social-policy-2026/1.42.b2
  forPractitioner: { text: "Tell students at the start, clearly, what is expected of them and what support they can use.", rewrite: light, force: should, status: drafted }
  forBeneficiary: { text: "not-applicable: a duty on the provider to inform students", rewrite: full, force: should, status: drafted }
  author-agent-written: "Treat this as a duty, in should, on the provider, not a learner outcome: clear early information on expectations and support. It holds for Social Policy courses at the levels the statement covers, not for one level. Cite it as (QAA, 2026, Social Policy Subject Benchmark Statement, para 1.42.b2). Do not present it as a regulatory requirement or turn it into a task for the student; set it beside 1.40, 1.43, 3.13 and the Equality Act 2010 duties named in 1.40."
  author-agent-dialogue: "Raise this when a team designs teaching and assessment or a disabled student asks about support. With the programme team, frame it as practice they plan for and ask \"What do students learn in week one about expectations and support?\" Do not put it to a student as their own duty; a student may only be told what the course should offer them."
- statement: qaa/social-policy-2026/1.42.b3
  forPractitioner: { text: "Make sure disabled students can fully use suitable learning resources and assistive technology for their own learning.", rewrite: light, force: should, status: drafted }
  forBeneficiary: { text: "not-applicable: a duty on the provider for accessible resources", rewrite: full, force: should, status: drafted }
  author-agent-written: "Treat this as a duty, in should, on the provider, not a learner outcome: resources and assistive technology for disabled students. It holds for Social Policy courses at the levels the statement covers, not for one level. Cite it as (QAA, 2026, Social Policy Subject Benchmark Statement, para 1.42.b3). Do not present it as a regulatory requirement or turn it into a task for the student; set it beside 1.40, 1.43, 3.13 and the Equality Act 2010 duties named in 1.40."
  author-agent-dialogue: "Raise this when a team designs teaching and assessment or a disabled student asks about support. With the programme team, frame it as practice they plan for and ask \"Which assistive technologies can disabled students use with your learning resources?\" Do not put it to a student as their own duty; a student may only be told what the course should offer them."
- statement: qaa/social-policy-2026/1.42.b4
  forPractitioner: { text: "Publish clear routes to reasonable adjustment, alternative assessment and extra support, in line with students' support plans.", rewrite: light, force: should, status: drafted }
  forBeneficiary: { text: "not-applicable: a duty on the provider in assessment", rewrite: full, force: should, status: drafted }
  author-agent-written: "Treat this as a duty, in should, on the provider, not a learner outcome: reasonable adjustment in assessment. It holds for Social Policy courses at the levels the statement covers, not for one level. Cite it as (QAA, 2026, Social Policy Subject Benchmark Statement, para 1.42.b4). Do not present it as a regulatory requirement or turn it into a task for the student; set it beside 1.40, 1.43, 3.13 and the Equality Act 2010 duties named in 1.40."
  author-agent-dialogue: "Raise this when a team designs teaching and assessment or a disabled student asks about support. With the programme team, frame it as practice they plan for and ask \"How does a student find out how to request an adjustment to an assessment?\" Do not put it to a student as their own duty; a student may only be told what the course should offer them."
- statement: qaa/social-policy-2026/1.43
  forPractitioner: { text: "Plan support for disabled students on placements and an alternative form of work-based learning for anyone the placement would exclude.", rewrite: light, force: should, status: drafted }
  forBeneficiary: { text: "not-applicable: a duty on the provider where placements are in the curriculum", rewrite: full, force: should, status: drafted }
  author-agent-written: "Treat this as a duty, in should, on the provider, where placements are in the curriculum, not a learner outcome: placement support for disabled students. It holds for Social Policy courses at the levels the statement covers, not for one level. Cite it as (QAA, 2026, Social Policy Subject Benchmark Statement, para 1.43). Do not present it as a regulatory requirement or turn it into a task for the student; set it beside 1.42, 1.57 and 3.4."
  author-agent-dialogue: "Raise this when a team plans placements. With the programme team, frame it as practice they plan for and ask \"What would a disabled student who cannot take this placement do instead?\" Do not put it to a student as their own duty; a student may only be told what the course should offer them."
- statement: qaa/social-policy-2026/1.48
  forPractitioner: { text: "Give students room to explore the link between welfare, work, the economy and the environment, and how welfare may need to change for future pressures.", rewrite: light, force: should, status: drafted }
  forBeneficiary: { text: "not-applicable: a duty on the course to offer the opportunity", rewrite: full, force: should, status: drafted }
  author-agent-written: "Treat this as a duty, in should, on the course, not a learner outcome: welfare, economy and the environment. It holds for Social Policy courses at the levels the statement covers, not for one level. Cite it as (QAA, 2026, Social Policy Subject Benchmark Statement, para 1.48). Do not present it as a regulatory requirement or turn it into a task for the student; set it beside 1.44 to 1.47, 3.3.b7, 4.7.b4 and std:doc:qaa-advancehe-esd-2021-guidance."
  author-agent-dialogue: "Raise this when a team plans sustainability content. With the programme team, frame it as practice they plan for and ask \"Where in the course do students examine how welfare policy affects the environment?\" Do not put it to a student as their own duty; a student may only be told what the course should offer them."
- statement: qaa/social-policy-2026/1.50
  forPractitioner: { text: "Draw on the Inner Development Goals in planning, so that personal skills for sustainable development are named and built.", rewrite: light, force: should, status: drafted }
  forBeneficiary: { text: "not-applicable: a duty on those who design programmes", rewrite: full, force: should, status: drafted }
  author-agent-written: "Treat this as a duty, in should, on those who design programmes, not a learner outcome: the Inner Development Goals. It holds for Social Policy courses at the levels the statement covers, not for one level. Cite it as (QAA, 2026, Social Policy Subject Benchmark Statement, para 1.50). Do not present it as a regulatory requirement or turn it into a task for the student; set it beside 1.49, 1.51 and std:doc:qaa-advancehe-esd-2021-guidance (the guidance 1.50 also names)."
  author-agent-dialogue: "Raise this when a team plans sustainability skills. With the programme team, frame it as practice they plan for and ask \"Which personal skills for sustainable development does the course name and develop?\" Do not put it to a student as their own duty; a student may only be told what the course should offer them."
- statement: qaa/social-policy-2026/1.52
  forPractitioner: { text: "In sustainability teaching, cover how climate change deepens privilege of several kinds and what it means for welfare services.", rewrite: light, force: should, status: drafted }
  forBeneficiary: { text: "not-applicable: a duty on those who teach sustainability", rewrite: full, force: should, status: drafted }
  author-agent-written: "Treat this as a duty, in should, on those who teach sustainability, not a learner outcome: critique of sustainability; climate and privilege. It holds for Social Policy courses at the levels the statement covers, not for one level. Cite it as (QAA, 2026, Social Policy Subject Benchmark Statement, para 1.52). Do not present it as a regulatory requirement or turn it into a task for the student; set it beside 1.14, 3.3.b20, 4.13.b6.masters and theme:edi."
  author-agent-dialogue: "Raise this when a team designs teaching on climate and inequality. With the programme team, frame it as practice they plan for and ask \"Where do students examine who gains and who loses from climate change?\" Do not put it to a student as their own duty; a student may only be told what the course should offer them."
- statement: qaa/social-policy-2026/1.53
  forPractitioner: { text: "Prepare students for learning after the degree: they should leave with broad critical and analytical skills to keep up with changing policy debates.", rewrite: light, force: should, status: drafted }
  forBeneficiary: { text: "You should leave your degree with a broad set of critical and analytical skills that let you keep joining policy debates as they change.", rewrite: full, force: should, status: drafted }
  author-agent-written: "Present this as an expectation of Social Policy students, in should, for the honours degree at FHEQ Level 6 (FQHEIS Level 10): skills for lifelong policy debate. Cite it as (QAA, 2026, Social Policy Subject Benchmark Statement, para 1.53). Do not call it a regulatory requirement or a rung of the section 4 standards. Set it beside 1.51, 4.10.b2 and qaa/fheq-2024/4.15.b9.3 and spine:6."
  author-agent-dialogue: "Raise this when a student asks how the degree prepares them for later learning or work. With a student, put it in plain second-person words; with staff, frame it as something the course should help students reach. Ask: \"How will you keep up with policy debates once you graduate?\" Avoid reading the paragraph aloud or treating it as a graded standard."
- statement: qaa/social-policy-2026/1.56
  forPractitioner: { text: "Design placements, authentic assessments or similar tasks where students apply the subject to real work settings.", rewrite: light, force: should, status: drafted }
  forBeneficiary: { text: "not-applicable: a duty on those who design programmes", rewrite: full, force: should, status: drafted }
  author-agent-written: "Treat this as a duty, in should, on those who design programmes, not a learner outcome: applying knowledge to work contexts. It holds for Social Policy courses at the levels the statement covers, not for one level. Cite it as (QAA, 2026, Social Policy Subject Benchmark Statement, para 1.56). Do not present it as a regulatory requirement or turn it into a task for the student; set it beside 1.54 to 1.58, 3.11 and std:doc:qaa-enterprise-2018-guidance."
  author-agent-dialogue: "Raise this when a team plans employability or authentic assessment. With the programme team, frame it as practice they plan for and ask \"Which tasks ask students to use the subject in a real or realistic work setting?\" Do not put it to a student as their own duty; a student may only be told what the course should offer them."
- statement: qaa/social-policy-2026/1.60
  forPractitioner: { text: "Build in chances for students to use and question generative AI tools, ethically and reflectively, within what your institution allows.", rewrite: light, force: should, status: drafted }
  forBeneficiary: { text: "not-applicable: a duty on the course to provide the opportunity", rewrite: full, force: should, status: drafted }
  author-agent-written: "Treat this as a duty, in should, on the course, not a learner outcome: critical engagement with generative AI. It holds for Social Policy courses at the levels the statement covers, not for one level. Cite it as (QAA, 2026, Social Policy Subject Benchmark Statement, para 1.60). Do not present it as a regulatory requirement or turn it into a task for the student; set it beside 1.61 to 1.66, 3.12, 4.10.b4 and 4.15.b5.masters."
  author-agent-dialogue: "Raise this when a team decides how generative AI enters teaching. With the programme team, frame it as practice they plan for and ask \"Where do students get to try generative AI critically, and under what rules?\" Do not put it to a student as their own duty; a student may only be told what the course should offer them."
- statement: qaa/social-policy-2026/1.62.b5
  forPractitioner: { text: "Bring the ethical, legal, environmental and social effects of generative AI, and policy responses, into class debate.", rewrite: light, force: should, status: drafted }
  forBeneficiary: { text: "not-applicable: a duty on the course to inform and involve students", rewrite: full, force: should, status: drafted }
  author-agent-written: "Treat this as a duty, in should, on the course, not a learner outcome: debate on the consequences of generative AI. It holds for Social Policy courses at the levels the statement covers, not for one level. Cite it as (QAA, 2026, Social Policy Subject Benchmark Statement, para 1.62.b5). Do not present it as a regulatory requirement or turn it into a task for the student; set it beside 1.60, 1.65 and 3.3.b19."
  author-agent-dialogue: "Raise this when a team plans teaching on AI and society. With the programme team, frame it as practice they plan for and ask \"Where do students debate the social and environmental costs of generative AI?\" Do not put it to a student as their own duty; a student may only be told what the course should offer them."
- statement: qaa/social-policy-2026/1.65
  forPractitioner: { text: "Within your institution's AI policy, teach students the risks, limits and environmental costs of generative AI use.", rewrite: light, force: should, status: drafted }
  forBeneficiary: { text: "not-applicable: a duty on the course to teach the risks", rewrite: full, force: should, status: drafted }
  author-agent-written: "Treat this as a duty, in should, on the course, within its institution's policy, not a learner outcome: institutional AI policy; teaching on risks. It holds for Social Policy courses at the levels the statement covers, not for one level. Cite it as (QAA, 2026, Social Policy Subject Benchmark Statement, para 1.65). Do not present it as a regulatory requirement or turn it into a task for the student; set it beside 1.60 to 1.64 and 3.12."
  author-agent-dialogue: "Raise this when a team aligns teaching with the institution's AI policy. With the programme team, frame it as practice they plan for and ask \"What do students learn here about the risks and environmental cost of generative AI?\" Do not put it to a student as their own duty; a student may only be told what the course should offer them."
- statement: qaa/social-policy-2026/2.1
  forPractitioner: { text: "Design the course so students can ask of any social problem what policy does, how and why, whether it should, and who acts and who is affected.", rewrite: light, force: should, status: drafted }
  forBeneficiary: { text: "Your course should equip you to ask of any social problem what policy does, how and why it does it, whether it should, who it affects and who carries it out.", rewrite: full, force: should, status: drafted }
  author-agent-written: "Present this as an expectation of Social Policy students, in should, for the honours degree at FHEQ Level 6 (FQHEIS Level 10): the core questions for any social problem. Cite it as (QAA, 2026, Social Policy Subject Benchmark Statement, para 2.1). Do not call it a regulatory requirement or a rung of the section 4 standards. Set it beside 2.2, 2.3, 4.8.b1 and qaa/fheq-2024/4.15.b7 and spine:6."
  author-agent-dialogue: "Raise this when a student asks how to approach a social problem, or a team frames course aims. With a student, put it in plain second-person words; with staff, frame it as something the course should help students reach. Ask: \"Take a social problem you care about: what is done, how, why, should it be, to whom and by whom?\" Avoid reading the paragraph aloud or treating it as a graded standard."
- statement: qaa/social-policy-2026/2.2.b1
  forPractitioner: { text: "Give the concept of welfare, welfare systems and entitlement a clear place in the programme.", rewrite: light, force: should, status: drafted }
  forBeneficiary: { text: "not-applicable: a design duty on the programme", rewrite: full, force: should, status: drafted }
  author-agent-written: "Treat this as a duty, in should, on programme designers, not a learner outcome: welfare, welfare systems and entitlement. It holds for Social Policy courses at the levels the statement covers, not for one level. Cite it as (QAA, 2026, Social Policy Subject Benchmark Statement, para 2.2.b1). Do not present it as a regulatory requirement or turn it into a task for the student; set it beside 2.1, 2.3, 3.3 and qaa/fheq-2024/4.15.b1."
  author-agent-dialogue: "Raise this when a team designs or reviews a Social Policy programme. With the programme team, frame it as practice they plan for and ask \"Where does the programme teach the concept of welfare and entitlement directly?\" Do not put it to a student as their own duty; a student may only be told what the course should offer them."
- statement: qaa/social-policy-2026/2.2.b2
  forPractitioner: { text: "Cover policies on social security, health, education, housing and similar fields that bear on welfare.", rewrite: light, force: should, status: drafted }
  forBeneficiary: { text: "not-applicable: a design duty on the programme", rewrite: full, force: should, status: drafted }
  author-agent-written: "Treat this as a duty, in should, on programme designers, not a learner outcome: policies that bear on welfare. It holds for Social Policy courses at the levels the statement covers, not for one level. Cite it as (QAA, 2026, Social Policy Subject Benchmark Statement, para 2.2.b2). Do not present it as a regulatory requirement or turn it into a task for the student; set it beside 2.1, 2.3, 3.3 and qaa/fheq-2024/4.15.b1."
  author-agent-dialogue: "Raise this when a team designs or reviews a Social Policy programme. With the programme team, frame it as practice they plan for and ask \"Which policy fields does the core curriculum cover?\" Do not put it to a student as their own duty; a student may only be told what the course should offer them."
- statement: qaa/social-policy-2026/2.2.b3
  forPractitioner: { text: "Pair theory with empirical work in modules and assessments.", rewrite: light, force: should, status: drafted }
  forBeneficiary: { text: "not-applicable: a design duty on the programme", rewrite: full, force: should, status: drafted }
  author-agent-written: "Treat this as a duty, in should, on programme designers, not a learner outcome: theory tied to empirical enquiry. It holds for Social Policy courses at the levels the statement covers, not for one level. Cite it as (QAA, 2026, Social Policy Subject Benchmark Statement, para 2.2.b3). Do not present it as a regulatory requirement or turn it into a task for the student; set it beside 2.1, 2.3, 3.3 and qaa/fheq-2024/4.15.b1."
  author-agent-dialogue: "Raise this when a team designs or reviews a Social Policy programme. With the programme team, frame it as practice they plan for and ask \"Where do students test a theory against data?\" Do not put it to a student as their own duty; a student may only be told what the course should offer them."
- statement: qaa/social-policy-2026/2.2.b4
  forPractitioner: { text: "Teach students to identify the values, ideologies and evidence behind welfare debates and policy.", rewrite: light, force: should, status: drafted }
  forBeneficiary: { text: "not-applicable: a design duty on the programme", rewrite: full, force: should, status: drafted }
  author-agent-written: "Treat this as a duty, in should, on programme designers, not a learner outcome: values, ideologies and evidence in welfare debate. It holds for Social Policy courses at the levels the statement covers, not for one level. Cite it as (QAA, 2026, Social Policy Subject Benchmark Statement, para 2.2.b4). Do not present it as a regulatory requirement or turn it into a task for the student; set it beside 2.1, 2.3, 3.3 and qaa/fheq-2024/4.15.b1."
  author-agent-dialogue: "Raise this when a team designs or reviews a Social Policy programme. With the programme team, frame it as practice they plan for and ask \"Where do students learn to separate values from evidence in a policy debate?\" Do not put it to a student as their own duty; a student may only be told what the course should offer them."
- statement: qaa/social-policy-2026/2.2.b5
  forPractitioner: { text: "Build both academic and practical knowledge of policy development, implementation and evaluation.", rewrite: light, force: should, status: drafted }
  forBeneficiary: { text: "not-applicable: a design duty on the programme", rewrite: full, force: should, status: drafted }
  author-agent-written: "Treat this as a duty, in should, on programme designers, not a learner outcome: knowledge of policy making and evaluation. It holds for Social Policy courses at the levels the statement covers, not for one level. Cite it as (QAA, 2026, Social Policy Subject Benchmark Statement, para 2.2.b5). Do not present it as a regulatory requirement or turn it into a task for the student; set it beside 2.1, 2.3, 3.3 and qaa/fheq-2024/4.15.b1."
  author-agent-dialogue: "Raise this when a team designs or reviews a Social Policy programme. With the programme team, frame it as practice they plan for and ask \"Where do students meet practitioners or practical tasks in policy evaluation?\" Do not put it to a student as their own duty; a student may only be told what the course should offer them."
- statement: qaa/social-policy-2026/2.3.b1
  forPractitioner: { text: "Teach students to identify and critique how social issues are framed and how problems come to be constructed.", rewrite: light, force: should, status: drafted }
  forBeneficiary: { text: "You should be able to identify, apply and critique ideas about how social issues come to be seen and problems defined.", rewrite: full, force: should, status: drafted }
  author-agent-written: "Present this as an expectation of Social Policy students, in should, for the honours degree at FHEQ Level 6 (FQHEIS Level 10): how issues and problems are constructed. Cite it as (QAA, 2026, Social Policy Subject Benchmark Statement, para 2.3.b1). Do not call it a regulatory requirement or a rung of the section 4 standards. Set it beside 2.1, 2.2, 3.3 and qaa/fheq-2024/4.15.b7 and spine:6."
  author-agent-dialogue: "Raise this when a student analyses a welfare issue or policy. With a student, put it in plain second-person words; with staff, frame it as something the course should help students reach. Ask: \"Who first called this a social problem, and how did that framing shape the response?\" Avoid reading the paragraph aloud or treating it as a graded standard."
- statement: qaa/social-policy-2026/2.3.b2
  forPractitioner: { text: "Teach students to examine and critique the reasons given for interventions and how provision is set up.", rewrite: light, force: should, status: drafted }
  forBeneficiary: { text: "You should be able to identify and critique how interventions are justified and services set up.", rewrite: full, force: should, status: drafted }
  author-agent-written: "Present this as an expectation of Social Policy students, in should, for the honours degree at FHEQ Level 6 (FQHEIS Level 10): justifying interventions and provision. Cite it as (QAA, 2026, Social Policy Subject Benchmark Statement, para 2.3.b2). Do not call it a regulatory requirement or a rung of the section 4 standards. Set it beside 2.1, 2.2, 3.3 and qaa/fheq-2024/4.15.b7 and spine:6."
  author-agent-dialogue: "Raise this when a student analyses a welfare issue or policy. With a student, put it in plain second-person words; with staff, frame it as something the course should help students reach. Ask: \"What reasons were given for this intervention, and do they hold?\" Avoid reading the paragraph aloud or treating it as a graded standard."
- statement: qaa/social-policy-2026/2.3.b3
  forPractitioner: { text: "Teach students to trace the funding, design and running of interventions and to assess their effects.", rewrite: light, force: should, status: drafted }
  forBeneficiary: { text: "You should be able to examine how interventions are funded, designed and run, and judge their effects.", rewrite: full, force: should, status: drafted }
  author-agent-written: "Present this as an expectation of Social Policy students, in should, for the honours degree at FHEQ Level 6 (FQHEIS Level 10): resourcing, design and effects of interventions. Cite it as (QAA, 2026, Social Policy Subject Benchmark Statement, para 2.3.b3). Do not call it a regulatory requirement or a rung of the section 4 standards. Set it beside 2.1, 2.2, 3.3 and qaa/fheq-2024/4.15.b7 and spine:6."
  author-agent-dialogue: "Raise this when a student analyses a welfare issue or policy. With a student, put it in plain second-person words; with staff, frame it as something the course should help students reach. Ask: \"Who pays for this intervention, how is it run, and what has it changed?\" Avoid reading the paragraph aloud or treating it as a graded standard."
- statement: qaa/social-policy-2026/2.3.b4
  forPractitioner: { text: "Teach students to examine the historical, environmental, global and discriminatory forces behind provision, across all sectors and not the state alone.", rewrite: light, force: should, status: drafted }
  forBeneficiary: { text: "You should be able to examine the historical, environmental, global and discriminatory forces behind welfare, looking beyond the state to other sources of support.", rewrite: full, force: should, status: drafted }
  author-agent-written: "Present this as an expectation of Social Policy students, in should, for the honours degree at FHEQ Level 6 (FQHEIS Level 10): historical, environmental, global and discriminatory forces; beyond the state. Cite it as (QAA, 2026, Social Policy Subject Benchmark Statement, para 2.3.b4). Do not call it a regulatory requirement or a rung of the section 4 standards. Set it beside 2.1, 2.2, 3.3 and qaa/fheq-2024/4.15.b7 and spine:6."
  author-agent-dialogue: "Raise this when a student analyses a welfare issue or policy. With a student, put it in plain second-person words; with staff, frame it as something the course should help students reach. Ask: \"Which actors besides the state provide welfare in your topic, and what history shaped that mix?\" Avoid reading the paragraph aloud or treating it as a graded standard."
- statement: qaa/social-policy-2026/2.4.b1
  forPractitioner: { text: "Give students practice in policy analysis for different kinds of professional setting.", rewrite: light, force: should, status: drafted }
  forBeneficiary: { text: "You should have the skills and knowledge to analyse policy in many kinds of workplace.", rewrite: full, force: should, status: drafted }
  author-agent-written: "Present this as an expectation of Social Policy students, in should, for the honours degree at FHEQ Level 6 (FQHEIS Level 10): policy analysis in varied settings. Cite it as (QAA, 2026, Social Policy Subject Benchmark Statement, para 2.4.b1). Do not call it a regulatory requirement or a rung of the section 4 standards. Set it beside 2.1, 4.8.b1, 4.10.b1 and qaa/fheq-2024/4.15.b8 and spine:6."
  author-agent-dialogue: "Raise this when a student prepares policy work, briefings or proposals. With a student, put it in plain second-person words; with staff, frame it as something the course should help students reach. Ask: \"Where have you analysed a policy for a real or realistic organisation?\" Avoid reading the paragraph aloud or treating it as a graded standard."
- statement: qaa/social-policy-2026/2.4.b2
  forPractitioner: { text: "Set tasks such as briefings, reports and public pieces so students learn to pitch research to different audiences.", rewrite: light, force: should, status: drafted }
  forBeneficiary: { text: "You should be able to share research and recommendations in formats that suit professionals, policy makers and the public.", rewrite: full, force: should, status: drafted }
  author-agent-written: "Present this as an expectation of Social Policy students, in should, for the honours degree at FHEQ Level 6 (FQHEIS Level 10): communicating research to varied audiences. Cite it as (QAA, 2026, Social Policy Subject Benchmark Statement, para 2.4.b2). Do not call it a regulatory requirement or a rung of the section 4 standards. Set it beside 2.1, 4.8.b1, 4.10.b1 and qaa/fheq-2024/4.15.b8 and spine:6."
  author-agent-dialogue: "Raise this when a student prepares policy work, briefings or proposals. With a student, put it in plain second-person words; with staff, frame it as something the course should help students reach. Ask: \"How would you turn your findings into a briefing for a policy maker?\" Avoid reading the paragraph aloud or treating it as a graded standard."
- statement: qaa/social-policy-2026/2.4.b3
  forPractitioner: { text: "Leave room in assessment for students to propose and defend new solutions to welfare problems.", rewrite: light, force: should, status: drafted }
  forBeneficiary: { text: "You should be able to come up with new solutions that improve welfare for individuals or groups.", rewrite: full, force: should, status: drafted }
  author-agent-written: "Present this as an expectation of Social Policy students, in should, for the honours degree at FHEQ Level 6 (FQHEIS Level 10): innovative solutions for welfare. Cite it as (QAA, 2026, Social Policy Subject Benchmark Statement, para 2.4.b3). Do not call it a regulatory requirement or a rung of the section 4 standards. Set it beside 2.1, 4.8.b1, 4.10.b1 and qaa/fheq-2024/4.15.b8 and spine:6."
  author-agent-dialogue: "Raise this when a student prepares policy work, briefings or proposals. With a student, put it in plain second-person words; with staff, frame it as something the course should help students reach. Ask: \"What new solution would you propose to the problem you studied?\" Avoid reading the paragraph aloud or treating it as a graded standard."
- statement: qaa/social-policy-2026/2.5
  forPractitioner: { text: "Teach welfare as provided by state, market, voluntary and family sectors, developing at national, international and global scale.", rewrite: light, force: should, status: drafted }
  forBeneficiary: { text: "Your understanding should include how welfare comes from several sectors and how it develops in national and global settings.", rewrite: full, force: should, status: drafted }
  author-agent-written: "Present this as an expectation of Social Policy students, in should, for the honours degree at FHEQ Level 6 (FQHEIS Level 10): welfare from several sectors across contexts. Cite it as (QAA, 2026, Social Policy Subject Benchmark Statement, para 2.5). Do not call it a regulatory requirement or a rung of the section 4 standards. Set it beside 1.12, 3.3.b11, 4.7.b2 and qaa/fheq-2024/4.15.b1 and spine:6."
  author-agent-dialogue: "Raise this when a student focuses only on the state. With a student, put it in plain second-person words; with staff, frame it as something the course should help students reach. Ask: \"Besides the state, who provides welfare in the area you are studying?\" Avoid reading the paragraph aloud or treating it as a graded standard."
- statement: qaa/social-policy-2026/2.6
  forPractitioner: { text: "Build reflective practice, communication and conflict resolution into modules to prepare students for the realities of delivering services.", rewrite: light, force: should, status: drafted }
  forBeneficiary: { text: "not-applicable: a design duty on the programme", rewrite: full, force: should, status: drafted }
  author-agent-written: "Treat this as a duty, in should, on programme teams, not a learner outcome: reflective practice and interpersonal skills. It holds for Social Policy courses at the levels the statement covers, not for one level. Cite it as (QAA, 2026, Social Policy Subject Benchmark Statement, para 2.6). Do not present it as a regulatory requirement or turn it into a task for the student; set it beside 1.10, 3.3.b12 and 4.10.b3."
  author-agent-dialogue: "Raise this when a team plans skills for practice or social administration. With the programme team, frame it as practice they plan for and ask \"Where do students practise conflict resolution or reflect on practice?\" Do not put it to a student as their own duty; a student may only be told what the course should offer them."
- statement: qaa/social-policy-2026/2.7
  forPractitioner: { text: "Use module evaluations, staff-student meetings and co-production so student views feed into programme review.", rewrite: light, force: should, status: drafted }
  forBeneficiary: { text: "not-applicable: a duty on programme teams in review", rewrite: full, force: should, status: drafted }
  author-agent-written: "Treat this as a duty, in should, on programme teams, not a learner outcome: student voice in programme review. It holds for Social Policy courses at the levels the statement covers, not for one level. Cite it as (QAA, 2026, Social Policy Subject Benchmark Statement, para 2.7). Do not present it as a regulatory requirement or turn it into a task for the student; set it beside 1.34, 2.15 and 2.16."
  author-agent-dialogue: "Raise this when a team prepares a programme review. With the programme team, frame it as practice they plan for and ask \"How did students' views reach the last review, and what changed?\" Do not put it to a student as their own duty; a student may only be told what the course should offer them."
- statement: qaa/social-policy-2026/2.8
  forPractitioner: { text: "Plan each level to build towards the threshold skills; students will usually need to pass and earn credit for every part, practical work included.", rewrite: light, force: will, status: drafted }
  forBeneficiary: { text: "You will move up a level at a time under your university's rules, building towards the skills your degree asks for; usually you will need to pass every part, practical work included.", rewrite: full, force: will, status: drafted }
  author-agent-written: "Describe this as the expected route, in will, by which an honours student (FHEQ Level 6; FQHEIS Level 10) or an integrated master's student (FHEQ Level 7; FQHEIS Level 11) progresses towards the threshold standards of 4.7 to 4.10. Cite it as (QAA, 2026, Social Policy Subject Benchmark Statement, para 2.8). Do not claim it sets progression rules, which stay with each institution. Set it beside the threshold cells, the descriptors qaa/fheq-2024/4.10, 4.12, 4.15 and 4.17, and spine:4 to spine:7."
  author-agent-dialogue: "Raise this when a student asks what moving from one year to the next involves, or a team maps credit to levels. Tell a student in plain words that each year builds towards the skills the degree asks for and that passing every part is usually needed; ask \"Which parts of this year are you less sure of passing?\" Avoid quoting the institution's regulations as if this statement set them."
- statement: qaa/social-policy-2026/2.10
  forPractitioner: { text: "In joint and combined routes, make sure students will reach the core skills of the subject while their other subject adds its own.", rewrite: light, force: will, status: drafted }
  forBeneficiary: { text: "If you study this subject in a joint or combined degree, you will gain its core subject and general skills and add others from your second subject.", rewrite: full, force: will, status: drafted }
  author-agent-written: "Present this as the expected outcome, in will, for students taking Social Policy in a joint, combined or major/minor honours degree at FHEQ Level 6 (FQHEIS Level 10): the core of the skills in 4.7 to 4.10, not every cell. Cite it as (QAA, 2026, Social Policy Subject Benchmark Statement, para 2.10). Do not claim that a joint-honours student must meet every cell, or that the statement says which elements are core. Set it beside 1.2, 4.6 and qaa/fheq-2024/4.15.b1."
  author-agent-dialogue: "Raise this when a joint-honours student or a team designing a combined route asks how much of the standard applies. Explain plainly that the core subject skills still apply and the other subject adds its own; ask \"Which Social Policy skills does your route give you the chance to show, and which come from your other subject?\" Avoid suggesting that joint honours is a lesser standard."
- statement: qaa/social-policy-2026/2.15
  forPractitioner: { text: "Your periodic course review will take account of what students say, alongside the data you routinely gather and analyse.", rewrite: light, force: will, status: drafted }
  forBeneficiary: { text: "not-applicable: a duty on the degree-awarding body in course review", rewrite: full, force: will, status: drafted }
  author-agent-written: "Treat this as an expectation, in will, on degree-awarding bodies and their partners: periodic course review takes account of the student voice. Cite it as (QAA, 2026, Social Policy Subject Benchmark Statement, para 2.15). Do not present it as a student outcome or as a regulatory requirement. Set it beside 2.7 (student contributions to review), 2.16 (external reviewers) and the external examining system described in 2.17."
  author-agent-dialogue: "Raise this with a programme team preparing a periodic review or answering student feedback. Frame it in practitioner terms and ask \"How did students' views reach this review, and what changed because of them?\" Do not hand it to a student as a task; it is the institution's duty, though students can be told their views count."
- statement: qaa/social-policy-2026/2.16
  forPractitioner: { text: "In periodic review you will bring in external reviewers, for an independent view on proposed changes and a check that threshold standards are met and content fits the subject.", rewrite: light, force: will, status: drafted }
  forBeneficiary: { text: "not-applicable: a duty on the provider in periodic review", rewrite: full, force: will, status: drafted }
  author-agent-written: "Present this as an expectation, in will, on providers: external reviewers take part in periodic review to check that the threshold standards (4.7 to 4.10) are achieved and content suits the subject. Cite it as (QAA, 2026, Social Policy Subject Benchmark Statement, para 2.16). Do not present it as a learner outcome. Set it beside 2.15, 2.17 and the threshold cells of 4.7 to 4.10."
  author-agent-dialogue: "Raise this when a programme team plans a periodic review or asks who checks its standards. Frame it as practice the team will follow and ask \"Who is your external reviewer, and which threshold standards will they look at?\" Avoid presenting it to students as something they must meet."
- statement: qaa/social-policy-2026/3.3.b1
  forPractitioner: { text: "Teach how welfare institutions arose and grew in the UK and elsewhere, and their economic, social, demographic and political settings, so that graduates can show knowledge of it.", rewrite: light, force: describes, status: drafted }
  forBeneficiary: { text: "By graduation you have knowledge of how welfare institutions arose and grew in the UK and elsewhere, and your economic, social, demographic and political settings.", rewrite: full, force: describes, status: drafted }
  author-agent-written: "Present this as one of the knowledge areas the statement describes Social Policy graduates as showing, in plain present with no obliging word, for the honours degree at FHEQ Level 6 (FQHEIS Level 10): origins of welfare institutions and their settings. Cite it as (QAA, 2026, Social Policy Subject Benchmark Statement, para 3.3), in the group on welfare systems. Do not turn it into a requirement or a rung, or treat the list as a fixed curriculum, since 3.1 declines to prescribe. Set it beside the 4.7 knowledge rows, qaa/fheq-2024/4.15.b1 and spine:6."
  author-agent-dialogue: "Raise this when a team plans core content on welfare history and systems, or a student asks what they should know of them. With a student, ask in plain second-person words what they already know of it; with staff, ask where in the course it is taught. Ask: \"How did the welfare institutions you study come about, and what pressures shaped them?\" Avoid presenting the list as a checklist every module must cover."
- statement: qaa/social-policy-2026/3.3.b2
  forPractitioner: { text: "Teach the historical forces, colonialism, capitalism and industrialisation among them, behind lasting discrimination, and how their legacy still shapes welfare, so that graduates can show knowledge of it.", rewrite: light, force: describes, status: drafted }
  forBeneficiary: { text: "By graduation you have knowledge of the historical forces, colonialism, capitalism and industrialisation among them, behind lasting discrimination, and how your legacy still shapes welfare.", rewrite: full, force: describes, status: drafted }
  author-agent-written: "Present this as one of the knowledge areas the statement describes Social Policy graduates as showing, in plain present with no obliging word, for the honours degree at FHEQ Level 6 (FQHEIS Level 10): historical roots of discrimination in welfare. Cite it as (QAA, 2026, Social Policy Subject Benchmark Statement, para 3.3), in the group on welfare systems. Do not turn it into a requirement or a rung, or treat the list as a fixed curriculum, since 3.1 declines to prescribe. Set it beside the 4.7 knowledge rows, qaa/fheq-2024/4.15.b1 and spine:6."
  author-agent-dialogue: "Raise this when a team plans core content on welfare history and systems, or a student asks what they should know of them. With a student, ask in plain second-person words what they already know of it; with staff, ask where in the course it is taught. Ask: \"Which historical force still shapes who is treated unequally by welfare today?\" Avoid presenting the list as a checklist every module must cover."
- statement: qaa/social-policy-2026/3.3.b3
  forPractitioner: { text: "Teach drivers of social change such as climate change, sustainability, globalisation, the media and social movements, so that graduates can show knowledge of it.", rewrite: light, force: describes, status: drafted }
  forBeneficiary: { text: "By graduation you have knowledge of drivers of social change such as climate change, sustainability, globalisation, the media and social movements.", rewrite: full, force: describes, status: drafted }
  author-agent-written: "Present this as one of the knowledge areas the statement describes Social Policy graduates as showing, in plain present with no obliging word, for the honours degree at FHEQ Level 6 (FQHEIS Level 10): drivers of social change. Cite it as (QAA, 2026, Social Policy Subject Benchmark Statement, para 3.3), in the group on welfare systems. Do not turn it into a requirement or a rung, or treat the list as a fixed curriculum, since 3.1 declines to prescribe. Set it beside the 4.7 knowledge rows, qaa/fheq-2024/4.15.b1 and spine:6."
  author-agent-dialogue: "Raise this when a team plans core content on welfare history and systems, or a student asks what they should know of them. With a student, ask in plain second-person words what they already know of it; with staff, ask where in the course it is taught. Ask: \"Which force for change, such as globalisation or a social movement, has most altered the policy area you study?\" Avoid presenting the list as a checklist every module must cover."
- statement: qaa/social-policy-2026/3.3.b4
  forPractitioner: { text: "Teach what the main UK and global welfare institutions do and how they are organised, funded and regulated across security, education, work, health, care and housing, so that graduates can show knowledge of it.", rewrite: light, force: describes, status: drafted }
  forBeneficiary: { text: "By graduation you have knowledge of what the main UK and global welfare institutions do and how you are organised, funded and regulated across security, education, work, health, care and housing.", rewrite: full, force: describes, status: drafted }
  author-agent-written: "Present this as one of the knowledge areas the statement describes Social Policy graduates as showing, in plain present with no obliging word, for the honours degree at FHEQ Level 6 (FQHEIS Level 10): main welfare institutions and their work. Cite it as (QAA, 2026, Social Policy Subject Benchmark Statement, para 3.3), in the group on welfare systems. Do not turn it into a requirement or a rung, or treat the list as a fixed curriculum, since 3.1 declines to prescribe. Set it beside the 4.7 knowledge rows, qaa/fheq-2024/4.15.b1 and spine:6."
  author-agent-dialogue: "Raise this when a team plans core content on welfare history and systems, or a student asks what they should know of them. With a student, ask in plain second-person words what they already know of it; with staff, ask where in the course it is taught. Ask: \"Who funds and regulates the main institution in your policy area, and what does it do day to day?\" Avoid presenting the list as a checklist every module must cover."
- statement: qaa/social-policy-2026/3.3.b5
  forPractitioner: { text: "Teach common features and shared challenges of welfare institutions worldwide, in efficacy, equity, sustainability and political backing, from comparative study, so that graduates can show knowledge of it.", rewrite: light, force: describes, status: drafted }
  forBeneficiary: { text: "By graduation you have knowledge of common features and shared challenges of welfare institutions worldwide, in efficacy, equity, sustainability and political backing, from comparative study.", rewrite: full, force: describes, status: drafted }
  author-agent-written: "Present this as one of the knowledge areas the statement describes Social Policy graduates as showing, in plain present with no obliging word, for the honours degree at FHEQ Level 6 (FQHEIS Level 10): shared features and challenges of welfare institutions. Cite it as (QAA, 2026, Social Policy Subject Benchmark Statement, para 3.3), in the group on welfare systems. Do not turn it into a requirement or a rung, or treat the list as a fixed curriculum, since 3.1 declines to prescribe. Set it beside the 4.7 knowledge rows, qaa/fheq-2024/4.15.b1 and spine:6."
  author-agent-dialogue: "Raise this when a team plans core content on welfare history and systems, or a student asks what they should know of them. With a student, ask in plain second-person words what they already know of it; with staff, ask where in the course it is taught. Ask: \"What challenge do welfare institutions in different countries share, and how do they meet it?\" Avoid presenting the list as a checklist every module must cover."
- statement: qaa/social-policy-2026/3.3.b6
  forPractitioner: { text: "Teach how countries organise their social policies and institutions, set goals politically and how well they meet them, so that graduates can show knowledge of it.", rewrite: light, force: describes, status: drafted }
  forBeneficiary: { text: "By graduation you have knowledge of how countries organise your social policies and institutions, set goals politically and how well you meet them.", rewrite: full, force: describes, status: drafted }
  author-agent-written: "Present this as one of the knowledge areas the statement describes Social Policy graduates as showing, in plain present with no obliging word, for the honours degree at FHEQ Level 6 (FQHEIS Level 10): how countries organise and pursue policy goals. Cite it as (QAA, 2026, Social Policy Subject Benchmark Statement, para 3.3), in the group on welfare systems. Do not turn it into a requirement or a rung, or treat the list as a fixed curriculum, since 3.1 declines to prescribe. Set it beside the 4.7 knowledge rows, qaa/fheq-2024/4.15.b1 and spine:6."
  author-agent-dialogue: "Raise this when a team plans core content on welfare history and systems, or a student asks what they should know of them. With a student, ask in plain second-person words what they already know of it; with staff, ask where in the course it is taught. Ask: \"How does one country set its welfare goals, and how well does it reach them?\" Avoid presenting the list as a checklist every module must cover."
- statement: qaa/social-policy-2026/3.3.b7
  forPractitioner: { text: "Teach the part policy plays, globally and nationally, in sustainability and the climate crisis, including growth or degrowth, energy and environmental injustice, so that graduates can show knowledge of it.", rewrite: light, force: describes, status: drafted }
  forBeneficiary: { text: "By graduation you have knowledge of the part policy plays, globally and nationally, in sustainability and the climate crisis, including growth or degrowth, energy and environmental injustice.", rewrite: full, force: describes, status: drafted }
  author-agent-written: "Present this as one of the knowledge areas the statement describes Social Policy graduates as showing, in plain present with no obliging word, for the honours degree at FHEQ Level 6 (FQHEIS Level 10): policy in sustainability and the climate crisis. Cite it as (QAA, 2026, Social Policy Subject Benchmark Statement, para 3.3), in the group on welfare systems. Do not turn it into a requirement or a rung, or treat the list as a fixed curriculum, since 3.1 declines to prescribe. Set it beside the 4.7 knowledge rows, qaa/fheq-2024/4.15.b1 and spine:6."
  author-agent-dialogue: "Raise this when a team plans core content on welfare history and systems, or a student asks what they should know of them. With a student, ask in plain second-person words what they already know of it; with staff, ask where in the course it is taught. Ask: \"Who bears the cost of climate change in the communities you study, and what can policy do about it?\" Avoid presenting the list as a checklist every module must cover."
- statement: qaa/social-policy-2026/3.3.b8
  forPractitioner: { text: "Teach the ideas, principles and key thinkers behind the subject, read in the historical settings that produced them, so that graduates can show knowledge of it.", rewrite: light, force: describes, status: drafted }
  forBeneficiary: { text: "By graduation you have knowledge of the ideas, principles and key thinkers behind the subject, read in the historical settings that produced them.", rewrite: full, force: describes, status: drafted }
  author-agent-written: "Present this as one of the knowledge areas the statement describes Social Policy graduates as showing, in plain present with no obliging word, for the honours degree at FHEQ Level 6 (FQHEIS Level 10): ideas and thinkers of the subject in context. Cite it as (QAA, 2026, Social Policy Subject Benchmark Statement, para 3.3), in the group on welfare systems. Do not turn it into a requirement or a rung, or treat the list as a fixed curriculum, since 3.1 declines to prescribe. Set it beside the 4.7 knowledge rows, qaa/fheq-2024/4.15.b1 and spine:6."
  author-agent-dialogue: "Raise this when a team plans core content on welfare history and systems, or a student asks what they should know of them. With a student, ask in plain second-person words what they already know of it; with staff, ask where in the course it is taught. Ask: \"Which thinker shaped the subject most for you, and what in their time shaped them?\" Avoid presenting the list as a checklist every module must cover."
- statement: qaa/social-policy-2026/3.3.b9
  forPractitioner: { text: "Teach how policy making and implementation are framed, run and funded, with many stakeholders at several levels of government, so that graduates can show knowledge of it.", rewrite: light, force: describes, status: drafted }
  forBeneficiary: { text: "By graduation you have knowledge of how policy making and implementation are framed, run and funded, with many stakeholders at several levels of government.", rewrite: full, force: describes, status: drafted }
  author-agent-written: "Present this as one of the knowledge areas the statement describes Social Policy graduates as showing, in plain present with no obliging word, for the honours degree at FHEQ Level 6 (FQHEIS Level 10): framework and financing of policy processes. Cite it as (QAA, 2026, Social Policy Subject Benchmark Statement, para 3.3), in the group on policy processes. Do not turn it into a requirement or a rung, or treat the list as a fixed curriculum, since 3.1 declines to prescribe. Set it beside the 4.7 knowledge rows, qaa/fheq-2024/4.15.b1 and qaa/fheq-2024/4.15.b3.2 and spine:6."
  author-agent-dialogue: "Raise this when policy making, governance or implementation is the topic. With a student, ask in plain second-person words what they already know of it; with staff, ask where in the course it is taught. Ask: \"Who was involved in making and funding this policy, and at which level of government?\" Avoid presenting the list as a checklist every module must cover."
- statement: qaa/social-policy-2026/3.3.b10
  forPractitioner: { text: "Teach policy above and below the nation state and how international organisations frame problems and solutions, so that graduates can show knowledge of it.", rewrite: light, force: describes, status: drafted }
  forBeneficiary: { text: "By graduation you have knowledge of policy above and below the nation state and how international organisations frame problems and solutions.", rewrite: full, force: describes, status: drafted }
  author-agent-written: "Present this as one of the knowledge areas the statement describes Social Policy graduates as showing, in plain present with no obliging word, for the honours degree at FHEQ Level 6 (FQHEIS Level 10): subnational and supranational policy; international organisations. Cite it as (QAA, 2026, Social Policy Subject Benchmark Statement, para 3.3), in the group on policy processes. Do not turn it into a requirement or a rung, or treat the list as a fixed curriculum, since 3.1 declines to prescribe. Set it beside the 4.7 knowledge rows, qaa/fheq-2024/4.15.b1 and qaa/fheq-2024/4.15.b3.2 and spine:6."
  author-agent-dialogue: "Raise this when policy making, governance or implementation is the topic. With a student, ask in plain second-person words what they already know of it; with staff, ask where in the course it is taught. Ask: \"How has an international organisation shaped how this problem is defined or solved?\" Avoid presenting the list as a checklist every module must cover."
- statement: qaa/social-policy-2026/3.3.b11
  forPractitioner: { text: "Teach non-state welfare from informal, voluntary and private sources and how these mix with the state, so that graduates can show knowledge of it.", rewrite: light, force: describes, status: drafted }
  forBeneficiary: { text: "By graduation you have knowledge of non-state welfare from informal, voluntary and private sources and how these mix with the state.", rewrite: full, force: describes, status: drafted }
  author-agent-written: "Present this as one of the knowledge areas the statement describes Social Policy graduates as showing, in plain present with no obliging word, for the honours degree at FHEQ Level 6 (FQHEIS Level 10): non-state welfare and mixed economies. Cite it as (QAA, 2026, Social Policy Subject Benchmark Statement, para 3.3), in the group on policy processes. Do not turn it into a requirement or a rung, or treat the list as a fixed curriculum, since 3.1 declines to prescribe. Set it beside the 4.7 knowledge rows, qaa/fheq-2024/4.15.b1 and qaa/fheq-2024/4.15.b3.2 and spine:6."
  author-agent-dialogue: "Raise this when policy making, governance or implementation is the topic. With a student, ask in plain second-person words what they already know of it; with staff, ask where in the course it is taught. Ask: \"What part do families, charities or firms play in welfare in your topic?\" Avoid presenting the list as a checklist every module must cover."
- statement: qaa/social-policy-2026/3.3.b12
  forPractitioner: { text: "Teach social administration: how welfare institutions are led, managed and run day to day, with reflective and interpersonal skills, so that graduates can show knowledge of it.", rewrite: light, force: describes, status: drafted }
  forBeneficiary: { text: "By graduation you have knowledge of social administration: how welfare institutions are led, managed and run day to day, with reflective and interpersonal skills.", rewrite: full, force: describes, status: drafted }
  author-agent-written: "Present this as one of the knowledge areas the statement describes Social Policy graduates as showing, in plain present with no obliging word, for the honours degree at FHEQ Level 6 (FQHEIS Level 10): social administration and the running of institutions. Cite it as (QAA, 2026, Social Policy Subject Benchmark Statement, para 3.3), in the group on policy processes. Do not turn it into a requirement or a rung, or treat the list as a fixed curriculum, since 3.1 declines to prescribe. Set it beside the 4.7 knowledge rows, qaa/fheq-2024/4.15.b1 and qaa/fheq-2024/4.15.b3.2 and spine:6."
  author-agent-dialogue: "Raise this when policy making, governance or implementation is the topic. With a student, ask in plain second-person words what they already know of it; with staff, ask where in the course it is taught. Ask: \"What would it take to manage a welfare service well, and what skills would you need?\" Avoid presenting the list as a checklist every module must cover."
- statement: qaa/social-policy-2026/3.3.b13
  forPractitioner: { text: "Teach digital technology in designing, delivering and administering policy, so that graduates can show knowledge of it.", rewrite: light, force: describes, status: drafted }
  forBeneficiary: { text: "By graduation you have knowledge of digital technology in designing, delivering and administering policy.", rewrite: full, force: describes, status: drafted }
  author-agent-written: "Present this as one of the knowledge areas the statement describes Social Policy graduates as showing, in plain present with no obliging word, for the honours degree at FHEQ Level 6 (FQHEIS Level 10): digital technology in policy. Cite it as (QAA, 2026, Social Policy Subject Benchmark Statement, para 3.3), in the group on policy processes. Do not turn it into a requirement or a rung, or treat the list as a fixed curriculum, since 3.1 declines to prescribe. Set it beside the 4.7 knowledge rows, qaa/fheq-2024/4.15.b1 and qaa/fheq-2024/4.15.b3.2 and spine:6."
  author-agent-dialogue: "Raise this when policy making, governance or implementation is the topic. With a student, ask in plain second-person words what they already know of it; with staff, ask where in the course it is taught. Ask: \"How has digital technology changed how a service in your area is delivered?\" Avoid presenting the list as a checklist every module must cover."
- statement: qaa/social-policy-2026/3.3.b14
  forPractitioner: { text: "Teach public attitudes to welfare, the effect of information and misinformation, and how lobbying, campaigns and advocacy shape policy, so that graduates can show knowledge of it.", rewrite: light, force: describes, status: drafted }
  forBeneficiary: { text: "By graduation you have knowledge of public attitudes to welfare, the effect of information and misinformation, and how lobbying, campaigns and advocacy shape policy.", rewrite: full, force: describes, status: drafted }
  author-agent-written: "Present this as one of the knowledge areas the statement describes Social Policy graduates as showing, in plain present with no obliging word, for the honours degree at FHEQ Level 6 (FQHEIS Level 10): public attitudes, misinformation and advocacy. Cite it as (QAA, 2026, Social Policy Subject Benchmark Statement, para 3.3), in the group on policy processes. Do not turn it into a requirement or a rung, or treat the list as a fixed curriculum, since 3.1 declines to prescribe. Set it beside the 4.7 knowledge rows, qaa/fheq-2024/4.15.b1 and qaa/fheq-2024/4.15.b3.2 and spine:6."
  author-agent-dialogue: "Raise this when policy making, governance or implementation is the topic. With a student, ask in plain second-person words what they already know of it; with staff, ask where in the course it is taught. Ask: \"How did public opinion or a campaign shape a policy you have studied?\" Avoid presenting the list as a checklist every module must cover."
- statement: qaa/social-policy-2026/3.3.b15
  forPractitioner: { text: "Teach how policy affects the welfare of people and groups, both improving conditions and failing to reduce inequality, so that graduates can show knowledge of it.", rewrite: light, force: describes, status: drafted }
  forBeneficiary: { text: "By graduation you have knowledge of how policy affects the welfare of people and groups, both improving conditions and failing to reduce inequality.", rewrite: full, force: describes, status: drafted }
  author-agent-written: "Present this as one of the knowledge areas the statement describes Social Policy graduates as showing, in plain present with no obliging word, for the honours degree at FHEQ Level 6 (FQHEIS Level 10): how policy improves or fails welfare. Cite it as (QAA, 2026, Social Policy Subject Benchmark Statement, para 3.3), in the group on impacts. Do not turn it into a requirement or a rung, or treat the list as a fixed curriculum, since 3.1 declines to prescribe. Set it beside the 4.7 knowledge rows, qaa/fheq-2024/4.15.b1 and qaa/fheq-2024/4.15.b7 and spine:6."
  author-agent-dialogue: "Raise this when the effects of policy on people and groups are being studied. With a student, ask in plain second-person words what they already know of it; with staff, ask where in the course it is taught. Ask: \"Where has a policy improved lives, and where has it left inequality untouched?\" Avoid presenting the list as a checklist every module must cover."
- statement: qaa/social-policy-2026/3.3.b16
  forPractitioner: { text: "Teach the mixed effects of policy, including control and discipline through conditionality or the reproduction of inequality, so that graduates can show knowledge of it.", rewrite: light, force: describes, status: drafted }
  forBeneficiary: { text: "By graduation you have knowledge of the mixed effects of policy, including control and discipline through conditionality or the reproduction of inequality.", rewrite: full, force: describes, status: drafted }
  author-agent-written: "Present this as one of the knowledge areas the statement describes Social Policy graduates as showing, in plain present with no obliging word, for the honours degree at FHEQ Level 6 (FQHEIS Level 10): ambivalent effects: control and conditionality. Cite it as (QAA, 2026, Social Policy Subject Benchmark Statement, para 3.3), in the group on impacts. Do not turn it into a requirement or a rung, or treat the list as a fixed curriculum, since 3.1 declines to prescribe. Set it beside the 4.7 knowledge rows, qaa/fheq-2024/4.15.b1 and qaa/fheq-2024/4.15.b7 and spine:6."
  author-agent-dialogue: "Raise this when the effects of policy on people and groups are being studied. With a student, ask in plain second-person words what they already know of it; with staff, ask where in the course it is taught. Ask: \"Does welfare conditionality in your area support people, discipline them, or both?\" Avoid presenting the list as a checklist every module must cover."
- statement: qaa/social-policy-2026/3.3.b17
  forPractitioner: { text: "Teach ways of delivering welfare: universal or targeted, conditional or not, means-tested, and debates on eligibility, deservingness, leakage and coverage, so that graduates can show knowledge of it.", rewrite: light, force: describes, status: drafted }
  forBeneficiary: { text: "By graduation you have knowledge of ways of delivering welfare: universal or targeted, conditional or not, means-tested, and debates on eligibility, deservingness, leakage and coverage.", rewrite: full, force: describes, status: drafted }
  author-agent-written: "Present this as one of the knowledge areas the statement describes Social Policy graduates as showing, in plain present with no obliging word, for the honours degree at FHEQ Level 6 (FQHEIS Level 10): ways of delivering welfare; eligibility debates. Cite it as (QAA, 2026, Social Policy Subject Benchmark Statement, para 3.3), in the group on impacts. Do not turn it into a requirement or a rung, or treat the list as a fixed curriculum, since 3.1 declines to prescribe. Set it beside the 4.7 knowledge rows, qaa/fheq-2024/4.15.b1 and qaa/fheq-2024/4.15.b7 and spine:6."
  author-agent-dialogue: "Raise this when the effects of policy on people and groups are being studied. With a student, ask in plain second-person words what they already know of it; with staff, ask where in the course it is taught. Ask: \"Should the benefit you are studying be universal or targeted, and why?\" Avoid presenting the list as a checklist every module must cover."
- statement: qaa/social-policy-2026/3.3.b18
  forPractitioner: { text: "Teach how policy meets communities, families and people facing intersecting disadvantage of class, ethnicity, gender identity, sex, disability, religion or sexual orientation, so that graduates can show knowledge of it.", rewrite: light, force: describes, status: drafted }
  forBeneficiary: { text: "By graduation you have knowledge of how policy meets communities, families and people facing intersecting disadvantage of class, ethnicity, gender identity, sex, disability, religion or sexual orientation.", rewrite: full, force: describes, status: drafted }
  author-agent-written: "Present this as one of the knowledge areas the statement describes Social Policy graduates as showing, in plain present with no obliging word, for the honours degree at FHEQ Level 6 (FQHEIS Level 10): policy and intersecting disadvantage. Cite it as (QAA, 2026, Social Policy Subject Benchmark Statement, para 3.3), in the group on impacts. Do not turn it into a requirement or a rung, or treat the list as a fixed curriculum, since 3.1 declines to prescribe. Set it beside the 4.7 knowledge rows, qaa/fheq-2024/4.15.b1 and qaa/fheq-2024/4.15.b7 and spine:6."
  author-agent-dialogue: "Raise this when the effects of policy on people and groups are being studied. With a student, ask in plain second-person words what they already know of it; with staff, ask where in the course it is taught. Ask: \"Who faces more than one disadvantage under this policy, and how does that change its effect?\" Avoid presenting the list as a checklist every module must cover."
- statement: qaa/social-policy-2026/3.3.b19
  forPractitioner: { text: "Teach what new technology, generative AI and automation among them, means for work, education, health, care and welfare administration, so that graduates can show knowledge of it.", rewrite: light, force: describes, status: drafted }
  forBeneficiary: { text: "By graduation you have knowledge of what new technology, generative AI and automation among them, means for work, education, health, care and welfare administration.", rewrite: full, force: describes, status: drafted }
  author-agent-written: "Present this as one of the knowledge areas the statement describes Social Policy graduates as showing, in plain present with no obliging word, for the honours degree at FHEQ Level 6 (FQHEIS Level 10): new technology, generative AI and automation. Cite it as (QAA, 2026, Social Policy Subject Benchmark Statement, para 3.3), in the group on impacts. Do not turn it into a requirement or a rung, or treat the list as a fixed curriculum, since 3.1 declines to prescribe. Set it beside the 4.7 knowledge rows, qaa/fheq-2024/4.15.b1 and qaa/fheq-2024/4.15.b7 and spine:6."
  author-agent-dialogue: "Raise this when the effects of policy on people and groups are being studied. With a student, ask in plain second-person words what they already know of it; with staff, ask where in the course it is taught. Ask: \"How might automation change the area of welfare you study?\" Avoid presenting the list as a checklist every module must cover."
- statement: qaa/social-policy-2026/3.3.b20
  forPractitioner: { text: "Teach how policy and environmental debate shape each other, including climate inequality, resource distribution and long-term wellbeing, so that graduates can show knowledge of it.", rewrite: light, force: describes, status: drafted }
  forBeneficiary: { text: "By graduation you have knowledge of how policy and environmental debate shape each other, including climate inequality, resource distribution and long-term wellbeing.", rewrite: full, force: describes, status: drafted }
  author-agent-written: "Present this as one of the knowledge areas the statement describes Social Policy graduates as showing, in plain present with no obliging word, for the honours degree at FHEQ Level 6 (FQHEIS Level 10): policy and environmental debate. Cite it as (QAA, 2026, Social Policy Subject Benchmark Statement, para 3.3), in the group on impacts. Do not turn it into a requirement or a rung, or treat the list as a fixed curriculum, since 3.1 declines to prescribe. Set it beside the 4.7 knowledge rows, qaa/fheq-2024/4.15.b1 and qaa/fheq-2024/4.15.b7 and spine:6."
  author-agent-dialogue: "Raise this when the effects of policy on people and groups are being studied. With a student, ask in plain second-person words what they already know of it; with staff, ask where in the course it is taught. Ask: \"How has environmental debate changed a policy you know, or been changed by it?\" Avoid presenting the list as a checklist every module must cover."
- statement: qaa/social-policy-2026/3.3.b21
  forPractitioner: { text: "Teach major data sources on welfare and the main quantitative and qualitative research methods, so that graduates can show knowledge of it.", rewrite: light, force: describes, status: drafted }
  forBeneficiary: { text: "By graduation you have knowledge of major data sources on welfare and the main quantitative and qualitative research methods.", rewrite: full, force: describes, status: drafted }
  author-agent-written: "Present this as one of the knowledge areas the statement describes Social Policy graduates as showing, in plain present with no obliging word, for the honours degree at FHEQ Level 6 (FQHEIS Level 10): welfare data sources and research methods. Cite it as (QAA, 2026, Social Policy Subject Benchmark Statement, para 3.3), in the group on impacts. Do not turn it into a requirement or a rung, or treat the list as a fixed curriculum, since 3.1 declines to prescribe. Set it beside the 4.7 knowledge rows, qaa/fheq-2024/4.15.b1 and qaa/fheq-2024/4.15.b7 and spine:6."
  author-agent-dialogue: "Raise this when the effects of policy on people and groups are being studied. With a student, ask in plain second-person words what they already know of it; with staff, ask where in the course it is taught. Ask: \"Which data source would you use to measure the problem you study, and what would it miss?\" Avoid presenting the list as a checklist every module must cover."
- statement: qaa/social-policy-2026/3.3.b22
  forPractitioner: { text: "Teach core concepts: need, wellbeing, welfare, poverty, inequality, exclusion, citizenship, rights, equity, justice, sustainability, difference and intersectionality, so that graduates can show knowledge of it.", rewrite: light, force: describes, status: drafted }
  forBeneficiary: { text: "By graduation you have knowledge of core concepts: need, wellbeing, welfare, poverty, inequality, exclusion, citizenship, rights, equity, justice, sustainability, difference and intersectionality.", rewrite: full, force: describes, status: drafted }
  author-agent-written: "Present this as one of the knowledge areas the statement describes Social Policy graduates as showing, in plain present with no obliging word, for the honours degree at FHEQ Level 6 (FQHEIS Level 10): core concepts of welfare. Cite it as (QAA, 2026, Social Policy Subject Benchmark Statement, para 3.3), in the group on concepts and theories. Do not turn it into a requirement or a rung, or treat the list as a fixed curriculum, since 3.1 declines to prescribe. Set it beside the 4.7 knowledge rows, qaa/fheq-2024/4.15.b1 and qaa/fheq-2024/4.15.b2 and spine:6."
  author-agent-dialogue: "Raise this when a student or team is working with the subject's core concepts and theories. With a student, ask in plain second-person words what they already know of it; with staff, ask where in the course it is taught. Ask: \"How would you define poverty, and how does your definition change the policy you would back?\" Avoid presenting the list as a checklist every module must cover."
- statement: qaa/social-policy-2026/3.3.b23
  forPractitioner: { text: "Teach theories, philosophies and ideological debates about welfare and the roles of state, market and other actors, so that graduates can show knowledge of it.", rewrite: light, force: describes, status: drafted }
  forBeneficiary: { text: "By graduation you have knowledge of theories, philosophies and ideological debates about welfare and the roles of state, market and other actors.", rewrite: full, force: describes, status: drafted }
  author-agent-written: "Present this as one of the knowledge areas the statement describes Social Policy graduates as showing, in plain present with no obliging word, for the honours degree at FHEQ Level 6 (FQHEIS Level 10): theories and ideologies of welfare. Cite it as (QAA, 2026, Social Policy Subject Benchmark Statement, para 3.3), in the group on concepts and theories. Do not turn it into a requirement or a rung, or treat the list as a fixed curriculum, since 3.1 declines to prescribe. Set it beside the 4.7 knowledge rows, qaa/fheq-2024/4.15.b1 and qaa/fheq-2024/4.15.b2 and spine:6."
  author-agent-dialogue: "Raise this when a student or team is working with the subject's core concepts and theories. With a student, ask in plain second-person words what they already know of it; with staff, ask where in the course it is taught. Ask: \"What should the state do for welfare, and what should be left to markets, families or charities?\" Avoid presenting the list as a checklist every module must cover."
- statement: qaa/social-policy-2026/3.3.b24
  forPractitioner: { text: "Teach theories of the state and policy making, and comparative theory and method, so that graduates can show knowledge of it.", rewrite: light, force: describes, status: drafted }
  forBeneficiary: { text: "By graduation you have knowledge of theories of the state and policy making, and comparative theory and method.", rewrite: full, force: describes, status: drafted }
  author-agent-written: "Present this as one of the knowledge areas the statement describes Social Policy graduates as showing, in plain present with no obliging word, for the honours degree at FHEQ Level 6 (FQHEIS Level 10): theories of the state and comparison. Cite it as (QAA, 2026, Social Policy Subject Benchmark Statement, para 3.3), in the group on concepts and theories. Do not turn it into a requirement or a rung, or treat the list as a fixed curriculum, since 3.1 declines to prescribe. Set it beside the 4.7 knowledge rows, qaa/fheq-2024/4.15.b1 and qaa/fheq-2024/4.15.b2 and spine:6."
  author-agent-dialogue: "Raise this when a student or team is working with the subject's core concepts and theories. With a student, ask in plain second-person words what they already know of it; with staff, ask where in the course it is taught. Ask: \"Which theory of the state best explains the policy you are studying?\" Avoid presenting the list as a checklist every module must cover."
- statement: qaa/social-policy-2026/3.3.b25
  forPractitioner: { text: "Teach interdisciplinary approaches, with the social sciences meeting around policy's applied focus, so that graduates can show knowledge of it.", rewrite: light, force: describes, status: drafted }
  forBeneficiary: { text: "By graduation you have knowledge of interdisciplinary approaches, with the social sciences meeting around policy's applied focus.", rewrite: full, force: describes, status: drafted }
  author-agent-written: "Present this as one of the knowledge areas the statement describes Social Policy graduates as showing, in plain present with no obliging word, for the honours degree at FHEQ Level 6 (FQHEIS Level 10): interdisciplinary approaches. Cite it as (QAA, 2026, Social Policy Subject Benchmark Statement, para 3.3), in the group on concepts and theories. Do not turn it into a requirement or a rung, or treat the list as a fixed curriculum, since 3.1 declines to prescribe. Set it beside the 4.7 knowledge rows, qaa/fheq-2024/4.15.b1 and qaa/fheq-2024/4.15.b2 and spine:6."
  author-agent-dialogue: "Raise this when a student or team is working with the subject's core concepts and theories. With a student, ask in plain second-person words what they already know of it; with staff, ask where in the course it is taught. Ask: \"What does another social science add to your view of this problem?\" Avoid presenting the list as a checklist every module must cover."
- statement: qaa/social-policy-2026/3.3.b26
  forPractitioner: { text: "Teach the political economy of welfare and how values link to political and economic interests, so that graduates can show knowledge of it.", rewrite: light, force: describes, status: drafted }
  forBeneficiary: { text: "By graduation you have knowledge of the political economy of welfare and how values link to political and economic interests.", rewrite: full, force: describes, status: drafted }
  author-agent-written: "Present this as one of the knowledge areas the statement describes Social Policy graduates as showing, in plain present with no obliging word, for the honours degree at FHEQ Level 6 (FQHEIS Level 10): political economy of welfare. Cite it as (QAA, 2026, Social Policy Subject Benchmark Statement, para 3.3), in the group on concepts and theories. Do not turn it into a requirement or a rung, or treat the list as a fixed curriculum, since 3.1 declines to prescribe. Set it beside the 4.7 knowledge rows, qaa/fheq-2024/4.15.b1 and qaa/fheq-2024/4.15.b2 and spine:6."
  author-agent-dialogue: "Raise this when a student or team is working with the subject's core concepts and theories. With a student, ask in plain second-person words what they already know of it; with staff, ask where in the course it is taught. Ask: \"Whose economic interests does this policy serve, and which values justify it?\" Avoid presenting the list as a checklist every module must cover."
- statement: qaa/social-policy-2026/3.3.b27
  forPractitioner: { text: "Teach the ontology and epistemology beneath research designs, so that graduates can show knowledge of it.", rewrite: light, force: describes, status: drafted }
  forBeneficiary: { text: "By graduation you have knowledge of the ontology and epistemology beneath research designs.", rewrite: full, force: describes, status: drafted }
  author-agent-written: "Present this as one of the knowledge areas the statement describes Social Policy graduates as showing, in plain present with no obliging word, for the honours degree at FHEQ Level 6 (FQHEIS Level 10): ontology and epistemology of research. Cite it as (QAA, 2026, Social Policy Subject Benchmark Statement, para 3.3), in the group on research and policy analysis. Do not turn it into a requirement or a rung, or treat the list as a fixed curriculum, since 3.1 declines to prescribe. Set it beside the 4.7 knowledge rows, qaa/fheq-2024/4.15.b2 and qaa/fheq-2024/4.15.b6 and spine:6."
  author-agent-dialogue: "Raise this when research methods, evaluation or a dissertation are being planned. With a student, ask in plain second-person words what they already know of it; with staff, ask where in the course it is taught. Ask: \"What do you assume about what can be known when you choose a research design?\" Avoid presenting the list as a checklist every module must cover."
- statement: qaa/social-policy-2026/3.3.b28
  forPractitioner: { text: "Teach how to identify researchable problems about welfare, so that graduates can show knowledge of it.", rewrite: light, force: describes, status: drafted }
  forBeneficiary: { text: "By graduation you have knowledge of how to identify researchable problems about welfare.", rewrite: full, force: describes, status: drafted }
  author-agent-written: "Present this as one of the knowledge areas the statement describes Social Policy graduates as showing, in plain present with no obliging word, for the honours degree at FHEQ Level 6 (FQHEIS Level 10): framing research problems. Cite it as (QAA, 2026, Social Policy Subject Benchmark Statement, para 3.3), in the group on research and policy analysis. Do not turn it into a requirement or a rung, or treat the list as a fixed curriculum, since 3.1 declines to prescribe. Set it beside the 4.7 knowledge rows, qaa/fheq-2024/4.15.b2 and qaa/fheq-2024/4.15.b6 and spine:6."
  author-agent-dialogue: "Raise this when research methods, evaluation or a dissertation are being planned. With a student, ask in plain second-person words what they already know of it; with staff, ask where in the course it is taught. Ask: \"What question about welfare could you actually research, and how would you narrow it?\" Avoid presenting the list as a checklist every module must cover."
- statement: qaa/social-policy-2026/3.3.b29
  forPractitioner: { text: "Teach the principles of quantitative, qualitative and mixed-method research design, so that graduates can show knowledge of it.", rewrite: light, force: describes, status: drafted }
  forBeneficiary: { text: "By graduation you have knowledge of the principles of quantitative, qualitative and mixed-method research design.", rewrite: full, force: describes, status: drafted }
  author-agent-written: "Present this as one of the knowledge areas the statement describes Social Policy graduates as showing, in plain present with no obliging word, for the honours degree at FHEQ Level 6 (FQHEIS Level 10): research design principles. Cite it as (QAA, 2026, Social Policy Subject Benchmark Statement, para 3.3), in the group on research and policy analysis. Do not turn it into a requirement or a rung, or treat the list as a fixed curriculum, since 3.1 declines to prescribe. Set it beside the 4.7 knowledge rows, qaa/fheq-2024/4.15.b2 and qaa/fheq-2024/4.15.b6 and spine:6."
  author-agent-dialogue: "Raise this when research methods, evaluation or a dissertation are being planned. With a student, ask in plain second-person words what they already know of it; with staff, ask where in the course it is taught. Ask: \"Why might your question need numbers, interviews or both?\" Avoid presenting the list as a checklist every module must cover."
- statement: qaa/social-policy-2026/3.3.b30
  forPractitioner: { text: "Teach how to choose techniques for collecting, managing, interpreting and analysing data, secondary data included, so that graduates can show knowledge of it.", rewrite: light, force: describes, status: drafted }
  forBeneficiary: { text: "By graduation you have knowledge of how to choose techniques for collecting, managing, interpreting and analysing data, secondary data included.", rewrite: full, force: describes, status: drafted }
  author-agent-written: "Present this as one of the knowledge areas the statement describes Social Policy graduates as showing, in plain present with no obliging word, for the honours degree at FHEQ Level 6 (FQHEIS Level 10): choosing techniques for data. Cite it as (QAA, 2026, Social Policy Subject Benchmark Statement, para 3.3), in the group on research and policy analysis. Do not turn it into a requirement or a rung, or treat the list as a fixed curriculum, since 3.1 declines to prescribe. Set it beside the 4.7 knowledge rows, qaa/fheq-2024/4.15.b2 and qaa/fheq-2024/4.15.b6 and spine:6."
  author-agent-dialogue: "Raise this when research methods, evaluation or a dissertation are being planned. With a student, ask in plain second-person words what they already know of it; with staff, ask where in the course it is taught. Ask: \"Which existing data set could answer part of your question?\" Avoid presenting the list as a checklist every module must cover."
- statement: qaa/social-policy-2026/3.3.b31
  forPractitioner: { text: "Teach approaches to policy evaluation and analysis, so that graduates can show knowledge of it.", rewrite: light, force: describes, status: drafted }
  forBeneficiary: { text: "By graduation you have knowledge of approaches to policy evaluation and analysis.", rewrite: full, force: describes, status: drafted }
  author-agent-written: "Present this as one of the knowledge areas the statement describes Social Policy graduates as showing, in plain present with no obliging word, for the honours degree at FHEQ Level 6 (FQHEIS Level 10): policy evaluation and analysis. Cite it as (QAA, 2026, Social Policy Subject Benchmark Statement, para 3.3), in the group on research and policy analysis. Do not turn it into a requirement or a rung, or treat the list as a fixed curriculum, since 3.1 declines to prescribe. Set it beside the 4.7 knowledge rows, qaa/fheq-2024/4.15.b2 and qaa/fheq-2024/4.15.b6 and spine:6."
  author-agent-dialogue: "Raise this when research methods, evaluation or a dissertation are being planned. With a student, ask in plain second-person words what they already know of it; with staff, ask where in the course it is taught. Ask: \"How would you tell whether this policy has worked?\" Avoid presenting the list as a checklist every module must cover."
- statement: qaa/social-policy-2026/3.3.b32
  forPractitioner: { text: "Teach debates on evidence-based policy and how social science research informs policy making, so that graduates can show knowledge of it.", rewrite: light, force: describes, status: drafted }
  forBeneficiary: { text: "By graduation you have knowledge of debates on evidence-based policy and how social science research informs policy making.", rewrite: full, force: describes, status: drafted }
  author-agent-written: "Present this as one of the knowledge areas the statement describes Social Policy graduates as showing, in plain present with no obliging word, for the honours degree at FHEQ Level 6 (FQHEIS Level 10): evidence-based policy and research. Cite it as (QAA, 2026, Social Policy Subject Benchmark Statement, para 3.3), in the group on research and policy analysis. Do not turn it into a requirement or a rung, or treat the list as a fixed curriculum, since 3.1 declines to prescribe. Set it beside the 4.7 knowledge rows, qaa/fheq-2024/4.15.b2 and qaa/fheq-2024/4.15.b6 and spine:6."
  author-agent-dialogue: "Raise this when research methods, evaluation or a dissertation are being planned. With a student, ask in plain second-person words what they already know of it; with staff, ask where in the course it is taught. Ask: \"When does research actually change policy, and when is it ignored?\" Avoid presenting the list as a checklist every module must cover."
- statement: qaa/social-policy-2026/3.3.b33
  forPractitioner: { text: "Teach research ethics in the social sciences, so that graduates can show knowledge of it.", rewrite: light, force: describes, status: drafted }
  forBeneficiary: { text: "By graduation you have knowledge of research ethics in the social sciences.", rewrite: full, force: describes, status: drafted }
  author-agent-written: "Present this as one of the knowledge areas the statement describes Social Policy graduates as showing, in plain present with no obliging word, for the honours degree at FHEQ Level 6 (FQHEIS Level 10): research ethics. Cite it as (QAA, 2026, Social Policy Subject Benchmark Statement, para 3.3), in the group on research and policy analysis. Do not turn it into a requirement or a rung, or treat the list as a fixed curriculum, since 3.1 declines to prescribe. Set it beside the 4.7 knowledge rows, qaa/fheq-2024/4.15.b2 and qaa/fheq-2024/4.15.b6 and spine:6."
  author-agent-dialogue: "Raise this when research methods, evaluation or a dissertation are being planned. With a student, ask in plain second-person words what they already know of it; with staff, ask where in the course it is taught. Ask: \"What ethical risks would your research raise, and how would you handle them?\" Avoid presenting the list as a checklist every module must cover."
- statement: qaa/social-policy-2026/3.4
  forPractitioner: { text: "Bring live policy debates into teaching so that students engage with them directly, as they must.", rewrite: light, force: must, status: drafted }
  forBeneficiary: { text: "You must engage directly with current debates and arguments on social policy issues.", rewrite: full, force: must, status: drafted }
  author-agent-written: "Present this as an expectation of Social Policy students, in must, for the honours degree at FHEQ Level 6 (FQHEIS Level 10): direct engagement with current debates. Cite it as (QAA, 2026, Social Policy Subject Benchmark Statement, para 3.4). Do not call it a regulatory requirement or a rung of the section 4 standards. Set it beside 3.8, 2.4 and qaa/fheq-2024/4.15.b3.2 and spine:6."
  author-agent-dialogue: "Raise this when a student relies only on textbooks. With a student, put it in plain second-person words; with staff, frame it as something the course should help students reach. Ask: \"Which current policy debate have you followed closely this term, and where do you stand?\" Avoid reading the paragraph aloud or treating it as a graded standard."
- statement: qaa/social-policy-2026/3.9
  forPractitioner: { text: "Design learning and assessment inclusively, with mature learners and students from disadvantaged backgrounds in mind.", rewrite: light, force: should, status: drafted }
  forBeneficiary: { text: "not-applicable: a duty on those who design learning and assessment", rewrite: full, force: should, status: drafted }
  author-agent-written: "Treat this as a duty, in should, on those who design learning and assessment, not a learner outcome: inclusive learning and assessment design. It holds for Social Policy courses at the levels the statement covers, not for one level. Cite it as (QAA, 2026, Social Policy Subject Benchmark Statement, para 3.9). Do not present it as a regulatory requirement or turn it into a task for the student; set it beside 1.29 to 1.32, 3.13 and theme:edi."
  author-agent-dialogue: "Raise this when a team designs learning or assessment. With the programme team, frame it as practice they plan for and ask \"How does this assessment work for a mature student with caring duties?\" Do not put it to a student as their own duty; a student may only be told what the course should offer them."
- statement: qaa/social-policy-2026/3.12
  forPractitioner: { text: "Across the assessment diet, keep enough tasks that validate each student's independent competence, state the rules on collusion and AI clearly, and resource misconduct investigation.", rewrite: light, force: must, status: drafted }
  forBeneficiary: { text: "not-applicable: a duty on those who design assessment and on the institution", rewrite: full, force: must, status: drafted }
  author-agent-written: "Treat this as a duty, in must, on those who design assessment and the institution that resources it, not a learner outcome: validating independent competence; misconduct. It holds for Social Policy courses at the levels the statement covers, not for one level. Cite it as (QAA, 2026, Social Policy Subject Benchmark Statement, para 3.12). Do not present it as a regulatory requirement or turn it into a task for the student; set it beside 1.60 to 1.66 (which 3.12 itself points to), 3.10, 3.13 and 4.10.b4."
  author-agent-dialogue: "Raise this when a team designs assessment in response to generative AI. With the programme team, frame it as practice they plan for and ask \"Which assessments show what a student can do without help, and are the AI rules for them clear?\" Do not put it to a student as their own duty; a student may only be told what the course should offer them."
- statement: qaa/social-policy-2026/3.13.b6
  forPractitioner: { text: "Plan deadlines across modules and support students when they cluster.", rewrite: light, force: should, status: drafted }
  forBeneficiary: { text: "not-applicable: a duty on those who schedule and support assessment", rewrite: full, force: should, status: drafted }
  author-agent-written: "Treat this as a duty, in should, on those who schedule and support assessment, not a learner outcome: support with competing deadlines. It holds for Social Policy courses at the levels the statement covers, not for one level. Cite it as (QAA, 2026, Social Policy Subject Benchmark Statement, para 3.13.b6). Do not present it as a regulatory requirement or turn it into a task for the student; set it beside 3.13 (its other principles, in 'ought to'), 1.42.b4 and 4.10.b2."
  author-agent-dialogue: "Raise this when deadlines bunch or a team plans the assessment calendar. With the programme team, frame it as practice they plan for and ask \"Where do assessment deadlines cluster, and what support is in place then?\" Do not put it to a student as their own duty; a student may only be told what the course should offer them."
- statement: qaa/social-policy-2026/3.17
  forPractitioner: { text: "Use feedback, and personal tutoring, to name students' strengths and growth so they can describe them to employers.", rewrite: light, force: should, status: drafted }
  forBeneficiary: { text: "not-applicable: a duty on those who give feedback; the student meets it in the feedback received", rewrite: full, force: should, status: drafted }
  author-agent-written: "Treat this as a duty, in should, on those who give feedback, not a learner outcome: feedback on strengths for work. It holds for Social Policy courses at the levels the statement covers, not for one level. Cite it as (QAA, 2026, Social Policy Subject Benchmark Statement, para 3.17). Do not present it as a regulatory requirement or turn it into a task for the student; set it beside 3.16, 4.10 and 4.14.b5.masters."
  author-agent-dialogue: "Raise this when a team reviews feedback practice. With the programme team, frame it as practice they plan for and ask \"Does your feedback tell students what they do well in terms they could use in an interview?\" Do not put it to a student as their own duty; a student may only be told what the course should offer them."
- statement: qaa/social-policy-2026/4.3
  forPractitioner: { text: "To evidence achievement above the typical standard, you should use Annex D of the Frameworks, its descriptions of first, upper second, lower second and third-class honours, alongside your own method.", rewrite: light, force: should, status: drafted }
  forBeneficiary: { text: "not-applicable: a duty on the provider in judging and classifying achievement; the student meets it through marks and class", rewrite: full, force: should, status: drafted }
  author-agent-written: "Treat this as a duty, in should, on each provider: to judge achievement above the typical rung it refers to Annex D of the Frameworks (std:doc:qaa-fheq-2024-framework, qaa/fheq-2024/annex-d/summary/r1/3rd to 1st). Cite it as (QAA, 2026, Social Policy Subject Benchmark Statement, para 4.3). Do not claim the statement itself sets class boundaries or mark bands. Set it beside 4.2 (the three rungs tied to third, second and first class), the Annex D bands (SL6 of the FHEQ document) and the band axis of std:ref:uk-assesscriteria."
  author-agent-dialogue: "Raise this when a team writes marking criteria or asks how the rungs relate to degree classes. Frame it for staff: threshold sits at the third-class line, typical at second class and excellent at first, while Annex D splits the second into 2.2 and 2.1; ask \"Do your criteria tell a 2.2 from a 2.1 where the typical column does not?\" Avoid telling students that most of them will exceed the typical standard as if it were a promise."
- statement: qaa/social-policy-2026/4.4
  forPractitioner: { text: "The threshold standards are not competence standards; if you set competence standards in a programme specification, inform them from this statement and any PSRB requirements, and you should follow the current Equality and Human Rights Commission guidance.", rewrite: light, force: should, status: drafted }
  forBeneficiary: { text: "not-applicable: a duty on the provider in writing competence standards", rewrite: full, force: should, status: drafted }
  author-agent-written: "Treat this as a duty, in should, on any provider that writes competence standards (in the Equality Act 2010 sense) for a Social Policy programme: follow current Equality and Human Rights Commission guidance. Cite it as (QAA, 2026, Social Policy Subject Benchmark Statement, para 4.4). Do not describe the threshold cells of 4.7 to 4.10 as competence standards or as universal requirements. Set it beside 4.2, 4.3 and the accessibility paragraphs 1.40 to 1.43."
  author-agent-dialogue: "Raise this when a programme team is drafting competence standards or a disabled student's adjustment turns on what is truly required. Frame it for staff and ask \"Is this a genuine competence standard, and have you checked it against the Commission's current guidance?\" Avoid presenting threshold standards to a student as fixed competences that rule out adjustments."
- statement: qaa/social-policy-2026/4.5.b1
  forPractitioner: { text: "Build the course so that by the end graduates have a grasp of a complex, substantial body of knowledge in the subject.", rewrite: light, force: must, status: drafted }
  forBeneficiary: { text: "By graduation you are expected to have a grasp of a complex and substantial body of knowledge.", rewrite: full, force: must, status: drafted }
  author-agent-written: "Present this as an outcome the statement expects of every Social Policy honours graduate at FHEQ Level 6 (FQHEIS Level 10), set out in line with the Frameworks: grasp of a complex body of knowledge. Cite it as (QAA, 2026, Social Policy Subject Benchmark Statement, para 4.5). It is not one of the rungs and the issuer's word is 'expected', so state it without must or will, and do not call it a regulatory requirement. Set it beside the matching honours descriptor qaa/fheq-2024/4.15.b1, the 4.7 to 4.10 tables and spine:6."
  author-agent-dialogue: "Raise this when a student asks what an honours degree adds up to. With a student, say in plain second-person words what you are expected to have built by graduation; with staff, frame it as the shape of the whole honours award. Ask: \"How would you sum up what you now know that you did not know in your first year?\" Avoid reading the list aloud or treating it as graded by class."
- statement: qaa/social-policy-2026/4.5.b2
  forPractitioner: { text: "Make sure analytical and problem-solving skills are taught and practised in ways students can carry into many kinds of job.", rewrite: light, force: must, status: drafted }
  forBeneficiary: { text: "By graduation you are expected to have analytical and problem-solving skills you can use in many kinds of work.", rewrite: full, force: must, status: drafted }
  author-agent-written: "Present this as an outcome the statement expects of every Social Policy honours graduate at FHEQ Level 6 (FQHEIS Level 10), set out in line with the Frameworks: analytical and problem-solving skills for work. Cite it as (QAA, 2026, Social Policy Subject Benchmark Statement, para 4.5). It is not one of the rungs and the issuer's word is 'expected', so state it without must or will, and do not call it a regulatory requirement. Set it beside the matching honours descriptor qaa/fheq-2024/4.15.b9.2, the 4.7 to 4.10 tables and spine:6."
  author-agent-dialogue: "Raise this when a student asks how the degree helps them get work. With a student, say in plain second-person words what you are expected to have built by graduation; with staff, frame it as the shape of the whole honours award. Ask: \"Which problem-solving skill from your degree would you describe to an employer, and with what example?\" Avoid reading the list aloud or treating it as graded by class."
- statement: qaa/social-policy-2026/4.5.b3
  forPractitioner: { text: "Give students experience of working with others co-creatively, sustainably and responsibly, and help them name what they learned.", rewrite: light, force: must, status: drafted }
  forBeneficiary: { text: "By graduation you are expected to have learned, through experience, to work with others in co-creative, sustainable and socially responsible ways.", rewrite: full, force: must, status: drafted }
  author-agent-written: "Present this as an outcome the statement expects of every Social Policy honours graduate at FHEQ Level 6 (FQHEIS Level 10), set out in line with the Frameworks: co-creative, sustainable and responsible working. Cite it as (QAA, 2026, Social Policy Subject Benchmark Statement, para 4.5). It is not one of the rungs and the issuer's word is 'expected', so state it without must or will, and do not call it a regulatory requirement. Set it beside the matching honours descriptor qaa/fheq-2024/4.15.b9.1, the 4.7 to 4.10 tables and spine:6."
  author-agent-dialogue: "Raise this when group projects, partnerships or volunteering come up. With a student, say in plain second-person words what you are expected to have built by graduation; with staff, frame it as the shape of the whole honours award. Ask: \"When have you worked with others to create something, and how did you keep it fair and sustainable?\" Avoid reading the list aloud or treating it as graded by class."
- statement: qaa/social-policy-2026/4.5.b4
  forPractitioner: { text: "Assess, across the course, how well students weigh evidence and assumptions, reach sound conclusions and communicate them.", rewrite: light, force: must, status: drafted }
  forBeneficiary: { text: "By graduation you are expected to be able to weigh evidence, arguments and assumptions, reach sound conclusions and explain them well.", rewrite: full, force: must, status: drafted }
  author-agent-written: "Present this as an outcome the statement expects of every Social Policy honours graduate at FHEQ Level 6 (FQHEIS Level 10), set out in line with the Frameworks: weighing evidence, judging soundly and communicating. Cite it as (QAA, 2026, Social Policy Subject Benchmark Statement, para 4.5). It is not one of the rungs and the issuer's word is 'expected', so state it without must or will, and do not call it a regulatory requirement. Set it beside the matching honours descriptor qaa/fheq-2024/4.15.b7 and qaa/fheq-2024/4.15.b8, the 4.7 to 4.10 tables and spine:6."
  author-agent-dialogue: "Raise this when a student is writing an argument or policy recommendation. With a student, say in plain second-person words what you are expected to have built by graduation; with staff, frame it as the shape of the whole honours award. Ask: \"What assumption in your argument would a sceptical reader challenge first?\" Avoid reading the list aloud or treating it as graded by class."
- statement: qaa/social-policy-2026/4.7.b1
  forPractitioner: { text: "Every honours route must give students the chance to show they know the facts of significant social policy events, issues and policies, past and present; this is the minimum for third-class honours.", rewrite: light, force: threshold, status: drafted }
  forBeneficiary: { text: "To gain honours at all, you need to be able to show you know the facts of significant social policy events, issues and policies, past and present.", rewrite: full, force: threshold, status: drafted }
  author-agent-written: "Present this as the threshold standard, the minimum for third-class honours in Social Policy at FHEQ Level 6 (FQHEIS Level 10): factual knowledge of past and present policy events. Cite it as (QAA, 2026, Social Policy Subject Benchmark Statement, para 4.7), threshold column. Do not call it a regulatory requirement or apply it to the master's award. Set it beside 4.7.b1.typical and 4.7.b1.excellent in the same row, qaa/fheq-2024/4.15.b1 and Annex D qaa/fheq-2024/annex-d/knowledge/r1/3rd and spine:6."
  author-agent-dialogue: "Raise this when a student asks how much policy knowledge they need, or a team plans core policy content. With a student, put it in plain second-person words as the least you need to show to gain honours at all; with staff, frame it as what teaching and assessment must give students room to show. Ask: \"Which major social policy events or reforms, past and recent, could you describe accurately?\" Avoid reading the table aloud or suggesting the threshold is what most students aim for."
- statement: qaa/social-policy-2026/4.7.b1.excellent
  forPractitioner: { text: "For first-class honours the statement requires that students critique what policies do and weigh their effects across the main policy fields, in the UK and abroad, emerging issues included; design tasks that let them show it.", rewrite: light, force: must, status: drafted }
  forBeneficiary: { text: "For a first-class degree, you need to be able to critique what policies do and weigh their effects across the main policy fields, in the UK and abroad, emerging issues included.", rewrite: full, force: must, status: drafted }
  author-agent-written: "Present this as the excellent standard, the attainment the statement requires for first-class honours in Social Policy at FHEQ Level 6 (FQHEIS Level 10): critique and evaluation of policy across the main fields. Cite it as (QAA, 2026, Social Policy Subject Benchmark Statement, para 4.7), excellent column. Do not call it a regulatory requirement or present it as the minimum to pass. Set it beside 4.7.b1 and 4.7.b1.typical in the same row, qaa/fheq-2024/4.15.b7 and Annex D qaa/fheq-2024/annex-d/knowledge/r1/1st and spine:6."
  author-agent-dialogue: "Raise this when a student asks how much policy knowledge they need, or a team plans core policy content. With a student, put it in plain second-person words as what a first-class result asks of you; with staff, frame it as what teaching and assessment must give students room to show. Ask: \"Pick a policy field: what has a recent policy achieved, what has it missed, and how do you know?\" Avoid reading the table aloud and never present this excellent standard as the minimum or as expected of everyone."
- statement: qaa/social-policy-2026/4.7.b1.typical
  forPractitioner: { text: "For second-class honours the statement requires that students show deep knowledge and critical awareness of central parts of policy analysis, such as how policies at local, national and international scale bear on a sustainable future and the UN goals; design tasks that let them show it.", rewrite: light, force: must, status: drafted }
  forBeneficiary: { text: "For a second-class degree, you need to be able to show deep knowledge and critical awareness of central parts of policy analysis, such as how policies at local, national and international scale bear on a sustainable future and the UN goals.", rewrite: full, force: must, status: drafted }
  author-agent-written: "Present this as the typical standard, the attainment the statement requires for second-class honours in Social Policy at FHEQ Level 6 (FQHEIS Level 10): deep, critical knowledge of policy analysis, sustainability included. Cite it as (QAA, 2026, Social Policy Subject Benchmark Statement, para 4.7), typical column. Do not call it a regulatory requirement or present it as the minimum to pass. Set it beside 4.7.b1 and 4.7.b1.excellent in the same row, qaa/fheq-2024/4.15.b1, qaa/fheq-2024/4.15.b3.2 and Annex D qaa/fheq-2024/annex-d/knowledge/r1/2.2 and 2.1 and spine:6."
  author-agent-dialogue: "Raise this when a student asks how much policy knowledge they need, or a team plans core policy content. With a student, put it in plain second-person words as what a second-class result asks of you; with staff, frame it as what teaching and assessment must give students room to show. Ask: \"How would you explain the way one policy, at local or national level, helps or hinders progress on a UN goal?\" Avoid reading the table aloud and never present this typical standard as the minimum for a pass."
- statement: qaa/social-policy-2026/4.7.b2
  forPractitioner: { text: "Every honours route must give students the chance to understand and compare the workings of social policies in the UK and in other countries, notably in health, education, housing, work, income support and care; this is the minimum for third-class honours.", rewrite: light, force: threshold, status: drafted }
  forBeneficiary: { text: "To gain honours at all, you need to be able to understand and compare the workings of social policies in the UK and in other countries, notably in health, education, housing, work, income support and care.", rewrite: full, force: threshold, status: drafted }
  author-agent-written: "Present this as the threshold standard, the minimum for third-class honours in Social Policy at FHEQ Level 6 (FQHEIS Level 10): how policies work in the UK and elsewhere. Cite it as (QAA, 2026, Social Policy Subject Benchmark Statement, para 4.7), threshold column. Do not call it a regulatory requirement or apply it to the master's award. Set it beside 4.7.b2.typical and 4.7.b2.excellent in the same row, qaa/fheq-2024/4.15.b1 and Annex D qaa/fheq-2024/annex-d/knowledge/r2/3rd and spine:6."
  author-agent-dialogue: "Raise this when a student is comparing countries or welfare regimes. With a student, put it in plain second-person words as the least you need to show to gain honours at all; with staff, frame it as what teaching and assessment must give students room to show. Ask: \"How does one service, say housing or social care, work differently in two countries or UK nations?\" Avoid reading the table aloud or suggesting the threshold is what most students aim for."
- statement: qaa/social-policy-2026/4.7.b2.excellent
  forPractitioner: { text: "For first-class honours the statement requires that students sort types of welfare state and policy, and critically judge the reasoning, consistency and effects of each, including what each means for different groups; design tasks that let them show it.", rewrite: light, force: must, status: drafted }
  forBeneficiary: { text: "For a first-class degree, you need to be able to sort types of welfare state and policy, and critically judge the reasoning, consistency and effects of each, including what each means for different groups.", rewrite: full, force: must, status: drafted }
  author-agent-written: "Present this as the excellent standard, the attainment the statement requires for first-class honours in Social Policy at FHEQ Level 6 (FQHEIS Level 10): typing and judging welfare states and their effects on groups. Cite it as (QAA, 2026, Social Policy Subject Benchmark Statement, para 4.7), excellent column. Do not call it a regulatory requirement or present it as the minimum to pass. Set it beside 4.7.b2 and 4.7.b2.typical in the same row, qaa/fheq-2024/4.15.b7 and Annex D qaa/fheq-2024/annex-d/knowledge/r2/1st and spine:6."
  author-agent-dialogue: "Raise this when a student is comparing countries or welfare regimes. With a student, put it in plain second-person words as what a first-class result asks of you; with staff, frame it as what teaching and assessment must give students room to show. Ask: \"Which welfare regime type fits a country you know, and who gains or loses most under it?\" Avoid reading the table aloud and never present this excellent standard as the minimum or as expected of everyone."
- statement: qaa/social-policy-2026/4.7.b2.typical
  forPractitioner: { text: "For second-class honours the statement requires that students tell welfare systems in different regions of the world apart, compare them and critique them; design tasks that let them show it.", rewrite: light, force: must, status: drafted }
  forBeneficiary: { text: "For a second-class degree, you need to be able to tell welfare systems in different regions of the world apart, compare them and critique them.", rewrite: full, force: must, status: drafted }
  author-agent-written: "Present this as the typical standard, the attainment the statement requires for second-class honours in Social Policy at FHEQ Level 6 (FQHEIS Level 10): comparative critique of welfare systems. Cite it as (QAA, 2026, Social Policy Subject Benchmark Statement, para 4.7), typical column. Do not call it a regulatory requirement or present it as the minimum to pass. Set it beside 4.7.b2 and 4.7.b2.excellent in the same row, qaa/fheq-2024/4.15.b7 and Annex D qaa/fheq-2024/annex-d/knowledge/r2/2.2 and 2.1 and spine:6."
  author-agent-dialogue: "Raise this when a student is comparing countries or welfare regimes. With a student, put it in plain second-person words as what a second-class result asks of you; with staff, frame it as what teaching and assessment must give students room to show. Ask: \"What sets two welfare systems you have studied apart, and which do you find weaker, and why?\" Avoid reading the table aloud and never present this typical standard as the minimum for a pass."
- statement: qaa/social-policy-2026/4.7.b3
  forPractitioner: { text: "Every honours route must give students the chance to discuss, set against each other and use the main theories, concepts, perspectives and methods of the subject; this is the minimum for third-class honours.", rewrite: light, force: threshold, status: drafted }
  forBeneficiary: { text: "To gain honours at all, you need to be able to discuss, set against each other and use the main theories, concepts, perspectives and methods of the subject.", rewrite: full, force: threshold, status: drafted }
  author-agent-written: "Present this as the threshold standard, the minimum for third-class honours in Social Policy at FHEQ Level 6 (FQHEIS Level 10): using the core theories and concepts. Cite it as (QAA, 2026, Social Policy Subject Benchmark Statement, para 4.7), threshold column. Do not call it a regulatory requirement or apply it to the master's award. Set it beside 4.7.b3.typical and 4.7.b3.excellent in the same row, qaa/fheq-2024/4.15.b2 and Annex D qaa/fheq-2024/annex-d/knowledge/r2/3rd and spine:6."
  author-agent-dialogue: "Raise this when a student is choosing or using theory in an essay. With a student, put it in plain second-person words as the least you need to show to gain honours at all; with staff, frame it as what teaching and assessment must give students room to show. Ask: \"Which two theories of welfare could you compare, and how have you used one in your work?\" Avoid reading the table aloud or suggesting the threshold is what most students aim for."
- statement: qaa/social-policy-2026/4.7.b3.excellent
  forPractitioner: { text: "For first-class honours the statement requires that students analyse, sort, bring together and critique the main theories, concepts, perspectives and methods of the subject; design tasks that let them show it.", rewrite: light, force: must, status: drafted }
  forBeneficiary: { text: "For a first-class degree, you need to be able to analyse, sort, bring together and critique the main theories, concepts, perspectives and methods of the subject.", rewrite: full, force: must, status: drafted }
  author-agent-written: "Present this as the excellent standard, the attainment the statement requires for first-class honours in Social Policy at FHEQ Level 6 (FQHEIS Level 10): synthesis and critique of core theory. Cite it as (QAA, 2026, Social Policy Subject Benchmark Statement, para 4.7), excellent column. Do not call it a regulatory requirement or present it as the minimum to pass. Set it beside 4.7.b3 and 4.7.b3.typical in the same row, qaa/fheq-2024/4.15.b7 and Annex D qaa/fheq-2024/annex-d/cognitive/r2/1st and spine:6."
  author-agent-dialogue: "Raise this when a student is choosing or using theory in an essay. With a student, put it in plain second-person words as what a first-class result asks of you; with staff, frame it as what teaching and assessment must give students room to show. Ask: \"Can you combine two perspectives into an argument of your own, and say where both fall short?\" Avoid reading the table aloud and never present this excellent standard as the minimum or as expected of everyone."
- statement: qaa/social-policy-2026/4.7.b3.typical
  forPractitioner: { text: "For second-class honours the statement requires that students group the main theories, concepts, perspectives and methods of the subject and engage with them critically; design tasks that let them show it.", rewrite: light, force: must, status: drafted }
  forBeneficiary: { text: "For a second-class degree, you need to be able to group the main theories, concepts, perspectives and methods of the subject and engage with them critically.", rewrite: full, force: must, status: drafted }
  author-agent-written: "Present this as the typical standard, the attainment the statement requires for second-class honours in Social Policy at FHEQ Level 6 (FQHEIS Level 10): critical engagement with core theory. Cite it as (QAA, 2026, Social Policy Subject Benchmark Statement, para 4.7), typical column. Do not call it a regulatory requirement or present it as the minimum to pass. Set it beside 4.7.b3 and 4.7.b3.excellent in the same row, qaa/fheq-2024/4.15.b3.1 and Annex D qaa/fheq-2024/annex-d/knowledge/r2/2.1 and spine:6."
  author-agent-dialogue: "Raise this when a student is choosing or using theory in an essay. With a student, put it in plain second-person words as what a second-class result asks of you; with staff, frame it as what teaching and assessment must give students room to show. Ask: \"Where does a theory you use fall short, and what would a critic say?\" Avoid reading the table aloud and never present this typical standard as the minimum for a pass."
- statement: qaa/social-policy-2026/4.7.b4
  forPractitioner: { text: "Every honours route must give students the chance to show they are aware of the UN Sustainable Development Goals; this is the minimum for third-class honours.", rewrite: light, force: threshold, status: drafted }
  forBeneficiary: { text: "To gain honours at all, you need to be able to show you are aware of the UN Sustainable Development Goals.", rewrite: full, force: threshold, status: drafted }
  author-agent-written: "Present this as the threshold standard, the minimum for third-class honours in Social Policy at FHEQ Level 6 (FQHEIS Level 10): awareness of the UN goals. Cite it as (QAA, 2026, Social Policy Subject Benchmark Statement, para 4.7), threshold column. Do not call it a regulatory requirement or apply it to the master's award. Set it beside 4.7.b4.typical and 4.7.b4.excellent in the same row, qaa/fheq-2024/4.15.b1 and spine:6."
  author-agent-dialogue: "Raise this when sustainability or the UN goals come up, or a team plans sustainability content. With a student, put it in plain second-person words as the least you need to show to gain honours at all; with staff, frame it as what teaching and assessment must give students room to show. Ask: \"Which of the UN goals touch the policy areas you study?\" Avoid reading the table aloud or suggesting the threshold is what most students aim for."
- statement: qaa/social-policy-2026/4.7.b4.excellent
  forPractitioner: { text: "For first-class honours the statement requires that students build analyses of social problems and policies with sustainable development principles and the UN goals at the core; design tasks that let them show it.", rewrite: light, force: must, status: drafted }
  forBeneficiary: { text: "For a first-class degree, you need to be able to build analyses of social problems and policies with sustainable development principles and the UN goals at the core.", rewrite: full, force: must, status: drafted }
  author-agent-written: "Present this as the excellent standard, the attainment the statement requires for first-class honours in Social Policy at FHEQ Level 6 (FQHEIS Level 10): analysis built on sustainable development. Cite it as (QAA, 2026, Social Policy Subject Benchmark Statement, para 4.7), excellent column. Do not call it a regulatory requirement or present it as the minimum to pass. Set it beside 4.7.b4 and 4.7.b4.typical in the same row, qaa/fheq-2024/4.15.b7 and Annex D qaa/fheq-2024/annex-d/cognitive/r4/1st and spine:6."
  author-agent-dialogue: "Raise this when sustainability or the UN goals come up, or a team plans sustainability content. With a student, put it in plain second-person words as what a first-class result asks of you; with staff, frame it as what teaching and assessment must give students room to show. Ask: \"How would your analysis of this problem change if sustainability were built in from the start?\" Avoid reading the table aloud and never present this excellent standard as the minimum or as expected of everyone."
- statement: qaa/social-policy-2026/4.7.b4.typical
  forPractitioner: { text: "For second-class honours the statement requires that students use what they know of the UN goals on many different social policy issues; design tasks that let them show it.", rewrite: light, force: must, status: drafted }
  forBeneficiary: { text: "For a second-class degree, you need to be able to use what you know of the UN goals on many different social policy issues.", rewrite: full, force: must, status: drafted }
  author-agent-written: "Present this as the typical standard, the attainment the statement requires for second-class honours in Social Policy at FHEQ Level 6 (FQHEIS Level 10): applying the UN goals to many issues. Cite it as (QAA, 2026, Social Policy Subject Benchmark Statement, para 4.7), typical column. Do not call it a regulatory requirement or present it as the minimum to pass. Set it beside 4.7.b4 and 4.7.b4.excellent in the same row, qaa/fheq-2024/4.15.b3.1 and spine:6."
  author-agent-dialogue: "Raise this when sustainability or the UN goals come up, or a team plans sustainability content. With a student, put it in plain second-person words as what a second-class result asks of you; with staff, frame it as what teaching and assessment must give students room to show. Ask: \"Take two different policy issues: how do the UN goals bear on each?\" Avoid reading the table aloud and never present this typical standard as the minimum for a pass."
- statement: qaa/social-policy-2026/4.8.b1
  forPractitioner: { text: "Every honours route must give students the chance to recall the main features of a range of social problems; this is the minimum for third-class honours.", rewrite: light, force: threshold, status: drafted }
  forBeneficiary: { text: "To gain honours at all, you need to be able to recall the main features of a range of social problems.", rewrite: full, force: threshold, status: drafted }
  author-agent-written: "Present this as the threshold standard, the minimum for third-class honours in Social Policy at FHEQ Level 6 (FQHEIS Level 10): features of social problems. Cite it as (QAA, 2026, Social Policy Subject Benchmark Statement, para 4.8), threshold column. Do not call it a regulatory requirement or apply it to the master's award. Set it beside 4.8.b1.typical and 4.8.b1.excellent in the same row, Annex D qaa/fheq-2024/annex-d/knowledge/r1/3rd and spine:6."
  author-agent-dialogue: "Raise this when a student is analysing a social problem. With a student, put it in plain second-person words as the least you need to show to gain honours at all; with staff, frame it as what teaching and assessment must give students room to show. Ask: \"What marks out two social problems you have studied, such as poverty and homelessness?\" Avoid reading the table aloud or suggesting the threshold is what most students aim for."
- statement: qaa/social-policy-2026/4.8.b1.excellent
  forPractitioner: { text: "For first-class honours the statement requires that students build critical analyses of major social problems and the policies aimed at them, and weigh other solutions with suitable analytical tools and research methods; design tasks that let them show it.", rewrite: light, force: must, status: drafted }
  forBeneficiary: { text: "For a first-class degree, you need to be able to build critical analyses of major social problems and the policies aimed at them, and weigh other solutions with suitable analytical tools and research methods.", rewrite: full, force: must, status: drafted }
  author-agent-written: "Present this as the excellent standard, the attainment the statement requires for first-class honours in Social Policy at FHEQ Level 6 (FQHEIS Level 10): critical analysis of problems and alternative solutions. Cite it as (QAA, 2026, Social Policy Subject Benchmark Statement, para 4.8), excellent column. Do not call it a regulatory requirement or present it as the minimum to pass. Set it beside 4.8.b1 and 4.8.b1.typical in the same row, qaa/fheq-2024/4.15.b7 and Annex D qaa/fheq-2024/annex-d/cognitive/r3/1st and spine:6."
  author-agent-dialogue: "Raise this when a student is analysing a social problem. With a student, put it in plain second-person words as what a first-class result asks of you; with staff, frame it as what teaching and assessment must give students room to show. Ask: \"What alternative to the current policy on this problem would you propose, and what evidence would test it?\" Avoid reading the table aloud and never present this excellent standard as the minimum or as expected of everyone."
- statement: qaa/social-policy-2026/4.8.b1.typical
  forPractitioner: { text: "For second-class honours the statement requires that students use central conceptual frameworks to analyse complex social questions and problems; design tasks that let them show it.", rewrite: light, force: must, status: drafted }
  forBeneficiary: { text: "For a second-class degree, you need to be able to use central conceptual frameworks to analyse complex social questions and problems.", rewrite: full, force: must, status: drafted }
  author-agent-written: "Present this as the typical standard, the attainment the statement requires for second-class honours in Social Policy at FHEQ Level 6 (FQHEIS Level 10): frameworks used to analyse complex problems. Cite it as (QAA, 2026, Social Policy Subject Benchmark Statement, para 4.8), typical column. Do not call it a regulatory requirement or present it as the minimum to pass. Set it beside 4.8.b1 and 4.8.b1.excellent in the same row, qaa/fheq-2024/4.15.b3.1 and Annex D qaa/fheq-2024/annex-d/practical/r1/2.2 and spine:6."
  author-agent-dialogue: "Raise this when a student is analysing a social problem. With a student, put it in plain second-person words as what a second-class result asks of you; with staff, frame it as what teaching and assessment must give students room to show. Ask: \"Which framework helped you make sense of a complex social problem, and how?\" Avoid reading the table aloud and never present this typical standard as the minimum for a pass."
- statement: qaa/social-policy-2026/4.8.b2
  forPractitioner: { text: "Every honours route must give students the chance to sum up the subject's main theories, concepts and perspectives and show how they differ; this is the minimum for third-class honours.", rewrite: light, force: threshold, status: drafted }
  forBeneficiary: { text: "To gain honours at all, you need to be able to sum up the subject's main theories, concepts and perspectives and show how they differ.", rewrite: full, force: threshold, status: drafted }
  author-agent-written: "Present this as the threshold standard, the minimum for third-class honours in Social Policy at FHEQ Level 6 (FQHEIS Level 10): summary and contrast of core theory. Cite it as (QAA, 2026, Social Policy Subject Benchmark Statement, para 4.8), threshold column. Do not call it a regulatory requirement or apply it to the master's award. Set it beside 4.8.b2.typical and 4.8.b2.excellent in the same row, qaa/fheq-2024/4.15.b2 and spine:6."
  author-agent-dialogue: "Raise this when a student is working with theory. With a student, put it in plain second-person words as the least you need to show to gain honours at all; with staff, frame it as what teaching and assessment must give students room to show. Ask: \"Can you sum up two perspectives on welfare and say how they differ?\" Avoid reading the table aloud or suggesting the threshold is what most students aim for."
- statement: qaa/social-policy-2026/4.8.b2.excellent
  forPractitioner: { text: "For first-class honours the statement requires that students critically sort, compare, combine and judge the subject's main theories, concepts and perspectives; design tasks that let them show it.", rewrite: light, force: must, status: drafted }
  forBeneficiary: { text: "For a first-class degree, you need to be able to critically sort, compare, combine and judge the subject's main theories, concepts and perspectives.", rewrite: full, force: must, status: drafted }
  author-agent-written: "Present this as the excellent standard, the attainment the statement requires for first-class honours in Social Policy at FHEQ Level 6 (FQHEIS Level 10): critical synthesis and evaluation of core theory. Cite it as (QAA, 2026, Social Policy Subject Benchmark Statement, para 4.8), excellent column. Do not call it a regulatory requirement or present it as the minimum to pass. Set it beside 4.8.b2 and 4.8.b2.typical in the same row, Annex D qaa/fheq-2024/annex-d/knowledge/r2/1st and spine:6."
  author-agent-dialogue: "Raise this when a student is working with theory. With a student, put it in plain second-person words as what a first-class result asks of you; with staff, frame it as what teaching and assessment must give students room to show. Ask: \"Which perspective holds up best against the evidence in your topic, and why?\" Avoid reading the table aloud and never present this excellent standard as the minimum or as expected of everyone."
- statement: qaa/social-policy-2026/4.8.b2.typical
  forPractitioner: { text: "For second-class honours the statement requires that students understand and use the subject's main theories, concepts and perspectives, and see why they matter to other disciplines and to practitioners; design tasks that let them show it.", rewrite: light, force: must, status: drafted }
  forBeneficiary: { text: "For a second-class degree, you need to be able to understand and use the subject's main theories, concepts and perspectives, and see why they matter to other disciplines and to practitioners.", rewrite: full, force: must, status: drafted }
  author-agent-written: "Present this as the typical standard, the attainment the statement requires for second-class honours in Social Policy at FHEQ Level 6 (FQHEIS Level 10): applying core theory, for other fields too. Cite it as (QAA, 2026, Social Policy Subject Benchmark Statement, para 4.8), typical column. Do not call it a regulatory requirement or present it as the minimum to pass. Set it beside 4.8.b2 and 4.8.b2.excellent in the same row, qaa/fheq-2024/4.15.b3.1 and Annex D qaa/fheq-2024/annex-d/knowledge/r2/2.2 and spine:6."
  author-agent-dialogue: "Raise this when a student is working with theory. With a student, put it in plain second-person words as what a second-class result asks of you; with staff, frame it as what teaching and assessment must give students room to show. Ask: \"Why might a practitioner, or a student of another subject, find this theory useful?\" Avoid reading the table aloud and never present this typical standard as the minimum for a pass."
- statement: qaa/social-policy-2026/4.8.b3
  forPractitioner: { text: "Every honours route must give students the chance to see how ideology, values, interests and norms can influence and form social policies; this is the minimum for third-class honours.", rewrite: light, force: threshold, status: drafted }
  forBeneficiary: { text: "To gain honours at all, you need to be able to see how ideology, values, interests and norms can influence and form social policies.", rewrite: full, force: threshold, status: drafted }
  author-agent-written: "Present this as the threshold standard, the minimum for third-class honours in Social Policy at FHEQ Level 6 (FQHEIS Level 10): ideology and values in policy. Cite it as (QAA, 2026, Social Policy Subject Benchmark Statement, para 4.8), threshold column. Do not call it a regulatory requirement or apply it to the master's award. Set it beside 4.8.b3.typical and 4.8.b3.excellent in the same row, qaa/fheq-2024/4.15.b1 and spine:6."
  author-agent-dialogue: "Raise this when values, ideology or politics in policy come up. With a student, put it in plain second-person words as the least you need to show to gain honours at all; with staff, frame it as what teaching and assessment must give students room to show. Ask: \"What values or interests lie behind a policy you have studied?\" Avoid reading the table aloud or suggesting the threshold is what most students aim for."
- statement: qaa/social-policy-2026/4.8.b3.excellent
  forPractitioner: { text: "For first-class honours the statement requires that students understand why different ideological positions, values and norms matter and use them in analysing social policies; design tasks that let them show it.", rewrite: light, force: must, status: drafted }
  forBeneficiary: { text: "For a first-class degree, you need to be able to understand why different ideological positions, values and norms matter and use them in analysing social policies.", rewrite: full, force: must, status: drafted }
  author-agent-written: "Present this as the excellent standard, the attainment the statement requires for first-class honours in Social Policy at FHEQ Level 6 (FQHEIS Level 10): ideological positions applied in analysis. Cite it as (QAA, 2026, Social Policy Subject Benchmark Statement, para 4.8), excellent column. Do not call it a regulatory requirement or present it as the minimum to pass. Set it beside 4.8.b3 and 4.8.b3.typical in the same row, qaa/fheq-2024/4.15.b3.1 and Annex D qaa/fheq-2024/annex-d/cognitive/r2/1st and spine:6."
  author-agent-dialogue: "Raise this when values, ideology or politics in policy come up. With a student, put it in plain second-person words as what a first-class result asks of you; with staff, frame it as what teaching and assessment must give students room to show. Ask: \"How would two ideological positions read the same policy differently?\" Avoid reading the table aloud and never present this excellent standard as the minimum or as expected of everyone."
- statement: qaa/social-policy-2026/4.8.b3.typical
  forPractitioner: { text: "For second-class honours the statement requires that students tell normative values from empirical claims and reflect critically on how values drive policy making and connect with evidence; design tasks that let them show it.", rewrite: light, force: must, status: drafted }
  forBeneficiary: { text: "For a second-class degree, you need to be able to tell normative values from empirical claims and reflect critically on how values drive policy making and connect with evidence.", rewrite: full, force: must, status: drafted }
  author-agent-written: "Present this as the typical standard, the attainment the statement requires for second-class honours in Social Policy at FHEQ Level 6 (FQHEIS Level 10): values against evidence in policy making. Cite it as (QAA, 2026, Social Policy Subject Benchmark Statement, para 4.8), typical column. Do not call it a regulatory requirement or present it as the minimum to pass. Set it beside 4.8.b3 and 4.8.b3.excellent in the same row, qaa/fheq-2024/4.15.b7 and spine:6."
  author-agent-dialogue: "Raise this when values, ideology or politics in policy come up. With a student, put it in plain second-person words as what a second-class result asks of you; with staff, frame it as what teaching and assessment must give students room to show. Ask: \"In this policy debate, which claims are about values and which can be tested with evidence?\" Avoid reading the table aloud and never present this typical standard as the minimum for a pass."
- statement: qaa/social-policy-2026/4.8.b4
  forPractitioner: { text: "Every honours route must give students the chance to understand and explain why human need and lived experience matter to social policies; this is the minimum for third-class honours.", rewrite: light, force: threshold, status: drafted }
  forBeneficiary: { text: "To gain honours at all, you need to be able to understand and explain why human need and lived experience matter to social policies.", rewrite: full, force: threshold, status: drafted }
  author-agent-written: "Present this as the threshold standard, the minimum for third-class honours in Social Policy at FHEQ Level 6 (FQHEIS Level 10): need and lived experience in policy. Cite it as (QAA, 2026, Social Policy Subject Benchmark Statement, para 4.8), threshold column. Do not call it a regulatory requirement or apply it to the master's award. Set it beside 4.8.b4.typical and 4.8.b4.excellent in the same row, qaa/fheq-2024/4.15.b1 and spine:6."
  author-agent-dialogue: "Raise this when a student is working with service users' views or lived experience. With a student, put it in plain second-person words as the least you need to show to gain honours at all; with staff, frame it as what teaching and assessment must give students room to show. Ask: \"How does lived experience change our understanding of what a policy does?\" Avoid reading the table aloud or suggesting the threshold is what most students aim for."
- statement: qaa/social-policy-2026/4.8.b4.excellent
  forPractitioner: { text: "For first-class honours the statement requires that students critically judge how much lived experience matters to policy analysis and to policies, and use what it shows where it fits; design tasks that let them show it.", rewrite: light, force: must, status: drafted }
  forBeneficiary: { text: "For a first-class degree, you need to be able to critically judge how much lived experience matters to policy analysis and to policies, and use what it shows where it fits.", rewrite: full, force: must, status: drafted }
  author-agent-written: "Present this as the excellent standard, the attainment the statement requires for first-class honours in Social Policy at FHEQ Level 6 (FQHEIS Level 10): lived experience weighed and applied. Cite it as (QAA, 2026, Social Policy Subject Benchmark Statement, para 4.8), excellent column. Do not call it a regulatory requirement or present it as the minimum to pass. Set it beside 4.8.b4 and 4.8.b4.typical in the same row, Annex D qaa/fheq-2024/annex-d/cognitive/r1/1st and spine:6."
  author-agent-dialogue: "Raise this when a student is working with service users' views or lived experience. With a student, put it in plain second-person words as what a first-class result asks of you; with staff, frame it as what teaching and assessment must give students room to show. Ask: \"Where have you used evidence from lived experience, and how did you weigh it against other evidence?\" Avoid reading the table aloud and never present this excellent standard as the minimum or as expected of everyone."
- statement: qaa/social-policy-2026/4.8.b4.typical
  forPractitioner: { text: "For second-class honours the statement requires that students show sensitivity to other people's values and interests, appreciate how varied human needs are and understand how analysis, policy making and implementation can meet them; design tasks that let them show it.", rewrite: light, force: must, status: drafted }
  forBeneficiary: { text: "For a second-class degree, you need to be able to show sensitivity to other people's values and interests, appreciate how varied human needs are and understand how analysis, policy making and implementation can meet them.", rewrite: full, force: must, status: drafted }
  author-agent-written: "Present this as the typical standard, the attainment the statement requires for second-class honours in Social Policy at FHEQ Level 6 (FQHEIS Level 10): sensitivity to others and to diverse needs. Cite it as (QAA, 2026, Social Policy Subject Benchmark Statement, para 4.8), typical column. Do not call it a regulatory requirement or present it as the minimum to pass. Set it beside 4.8.b4 and 4.8.b4.excellent in the same row, qaa/fheq-2024/4.15.b7 and spine:6."
  author-agent-dialogue: "Raise this when a student is working with service users' views or lived experience. With a student, put it in plain second-person words as what a second-class result asks of you; with staff, frame it as what teaching and assessment must give students room to show. Ask: \"Whose needs does this policy overlook, and how could the process have heard them?\" Avoid reading the table aloud and never present this typical standard as the minimum for a pass."
- statement: qaa/social-policy-2026/4.8.b5
  forPractitioner: { text: "Every honours route must give students the chance to assess research in the subject and carry out their own with suitable methods; this is the minimum for third-class honours.", rewrite: light, force: threshold, status: drafted }
  forBeneficiary: { text: "To gain honours at all, you need to be able to assess research in the subject and carry out your own with suitable methods.", rewrite: full, force: threshold, status: drafted }
  author-agent-written: "Present this as the threshold standard, the minimum for third-class honours in Social Policy at FHEQ Level 6 (FQHEIS Level 10): assessing and doing research. Cite it as (QAA, 2026, Social Policy Subject Benchmark Statement, para 4.8), threshold column. Do not call it a regulatory requirement or apply it to the master's award. Set it beside 4.8.b5.typical and 4.8.b5.excellent in the same row, qaa/fheq-2024/4.15.b6 and Annex D qaa/fheq-2024/annex-d/knowledge/r3/3rd and spine:6."
  author-agent-dialogue: "Raise this when a student is planning a dissertation or reading research critically. With a student, put it in plain second-person words as the least you need to show to gain honours at all; with staff, frame it as what teaching and assessment must give students room to show. Ask: \"What method did you choose for your research, and why did it fit the question?\" Avoid reading the table aloud or suggesting the threshold is what most students aim for."
- statement: qaa/social-policy-2026/4.8.b5.excellent
  forPractitioner: { text: "For first-class honours the statement requires that students plan, build and carry out valid, robust research in the subject with suitable methods and proper ethical standards; design tasks that let them show it.", rewrite: light, force: must, status: drafted }
  forBeneficiary: { text: "For a first-class degree, you need to be able to plan, build and carry out valid, robust research in the subject with suitable methods and proper ethical standards.", rewrite: full, force: must, status: drafted }
  author-agent-written: "Present this as the excellent standard, the attainment the statement requires for first-class honours in Social Policy at FHEQ Level 6 (FQHEIS Level 10): valid, robust and ethical research. Cite it as (QAA, 2026, Social Policy Subject Benchmark Statement, para 4.8), excellent column. Do not call it a regulatory requirement or present it as the minimum to pass. Set it beside 4.8.b5 and 4.8.b5.typical in the same row, qaa/fheq-2024/4.15.b6 and Annex D qaa/fheq-2024/annex-d/knowledge/r3/1st and spine:6."
  author-agent-dialogue: "Raise this when a student is planning a dissertation or reading research critically. With a student, put it in plain second-person words as what a first-class result asks of you; with staff, frame it as what teaching and assessment must give students room to show. Ask: \"How did you make your research valid and ethical, and what would an examiner question?\" Avoid reading the table aloud and never present this excellent standard as the minimum or as expected of everyone."
- statement: qaa/social-policy-2026/4.8.b5.typical
  forPractitioner: { text: "For second-class honours the statement requires that students draw on what they know and have done with research methods to comment critically and knowledgeably on how good research in the subject is; design tasks that let them show it.", rewrite: light, force: must, status: drafted }
  forBeneficiary: { text: "For a second-class degree, you need to be able to draw on what you know and have done with research methods to comment critically and knowledgeably on how good research in the subject is.", rewrite: full, force: must, status: drafted }
  author-agent-written: "Present this as the typical standard, the attainment the statement requires for second-class honours in Social Policy at FHEQ Level 6 (FQHEIS Level 10): critical comment on research quality. Cite it as (QAA, 2026, Social Policy Subject Benchmark Statement, para 4.8), typical column. Do not call it a regulatory requirement or present it as the minimum to pass. Set it beside 4.8.b5 and 4.8.b5.excellent in the same row, qaa/fheq-2024/4.15.b3.2 and Annex D qaa/fheq-2024/annex-d/knowledge/r3/2.1 and spine:6."
  author-agent-dialogue: "Raise this when a student is planning a dissertation or reading research critically. With a student, put it in plain second-person words as what a second-class result asks of you; with staff, frame it as what teaching and assessment must give students room to show. Ask: \"How strong was the method in a study you read recently, and what would you have done differently?\" Avoid reading the table aloud and never present this typical standard as the minimum for a pass."
- statement: qaa/social-policy-2026/4.9.b1
  forPractitioner: { text: "Every honours route must give students the chance to build and develop arguments that hang together logically, talk issues through and suggest responses; this is the minimum for third-class honours.", rewrite: light, force: threshold, status: drafted }
  forBeneficiary: { text: "To gain honours at all, you need to be able to build and develop arguments that hang together logically, talk issues through and suggest responses.", rewrite: full, force: threshold, status: drafted }
  author-agent-written: "Present this as the threshold standard, the minimum for third-class honours in Social Policy at FHEQ Level 6 (FQHEIS Level 10): coherent, logical argument. Cite it as (QAA, 2026, Social Policy Subject Benchmark Statement, para 4.9), threshold column. Do not call it a regulatory requirement or apply it to the master's award. Set it beside 4.9.b1.typical and 4.9.b1.excellent in the same row, qaa/fheq-2024/4.15.b3.1 and Annex D qaa/fheq-2024/annex-d/cognitive/r2/3rd and spine:6."
  author-agent-dialogue: "Raise this when a student asks what makes an argument stronger or why a mark was held back. With a student, put it in plain second-person words as the least you need to show to gain honours at all; with staff, frame it as what teaching and assessment must give students room to show. Ask: \"What is your argument in one sentence, and does each step follow?\" Avoid reading the table aloud or suggesting the threshold is what most students aim for."
- statement: qaa/social-policy-2026/4.9.b1.excellent
  forPractitioner: { text: "For first-class honours the statement requires that students reason creatively and for themselves, building a coherent, valid argument grounded in evidence to discuss issues and solve problems; design tasks that let them show it.", rewrite: light, force: must, status: drafted }
  forBeneficiary: { text: "For a first-class degree, you need to be able to reason creatively and for yourself, building a coherent, valid argument grounded in evidence to discuss issues and solve problems.", rewrite: full, force: must, status: drafted }
  author-agent-written: "Present this as the excellent standard, the attainment the statement requires for first-class honours in Social Policy at FHEQ Level 6 (FQHEIS Level 10): creative, independent and valid argument. Cite it as (QAA, 2026, Social Policy Subject Benchmark Statement, para 4.9), excellent column. Do not call it a regulatory requirement or present it as the minimum to pass. Set it beside 4.9.b1 and 4.9.b1.typical in the same row, Annex D qaa/fheq-2024/annex-d/cognitive/r4/1st and qaa/fheq-2024/annex-d/cognitive/r2/1st and spine:6."
  author-agent-dialogue: "Raise this when a student asks what makes an argument stronger or why a mark was held back. With a student, put it in plain second-person words as what a first-class result asks of you; with staff, frame it as what teaching and assessment must give students room to show. Ask: \"What in your argument is your own, beyond what the reading says?\" Avoid reading the table aloud and never present this excellent standard as the minimum or as expected of everyone."
- statement: qaa/social-policy-2026/4.9.b1.typical
  forPractitioner: { text: "For second-class honours the statement requires that students reason for themselves, building arguments backed by evidence and using fitting information and critical judgement to discuss issues and solve problems; design tasks that let them show it.", rewrite: light, force: must, status: drafted }
  forBeneficiary: { text: "For a second-class degree, you need to be able to reason for yourself, building arguments backed by evidence and using fitting information and critical judgement to discuss issues and solve problems.", rewrite: full, force: must, status: drafted }
  author-agent-written: "Present this as the typical standard, the attainment the statement requires for second-class honours in Social Policy at FHEQ Level 6 (FQHEIS Level 10): independent, evidence-based argument. Cite it as (QAA, 2026, Social Policy Subject Benchmark Statement, para 4.9), typical column. Do not call it a regulatory requirement or present it as the minimum to pass. Set it beside 4.9.b1 and 4.9.b1.excellent in the same row, qaa/fheq-2024/4.15.b7 and Annex D qaa/fheq-2024/annex-d/cognitive/r2/2.2 and 2.1 and spine:6."
  author-agent-dialogue: "Raise this when a student asks what makes an argument stronger or why a mark was held back. With a student, put it in plain second-person words as what a second-class result asks of you; with staff, frame it as what teaching and assessment must give students room to show. Ask: \"What evidence carries your argument, and where did you rely on your own judgement?\" Avoid reading the table aloud and never present this typical standard as the minimum for a pass."
- statement: qaa/social-policy-2026/4.9.b2
  forPractitioner: { text: "Every honours route must give students the chance to read, listen to or watch material and summarise, restate and assess it accurately; this is the minimum for third-class honours.", rewrite: light, force: threshold, status: drafted }
  forBeneficiary: { text: "To gain honours at all, you need to be able to read, listen to or watch material and summarise, restate and assess it accurately.", rewrite: full, force: threshold, status: drafted }
  author-agent-written: "Present this as the threshold standard, the minimum for third-class honours in Social Policy at FHEQ Level 6 (FQHEIS Level 10): accurate summary and assessment of content. Cite it as (QAA, 2026, Social Policy Subject Benchmark Statement, para 4.9), threshold column. Do not call it a regulatory requirement or apply it to the master's award. Set it beside 4.9.b2.typical and 4.9.b2.excellent in the same row, Annex D qaa/fheq-2024/annex-d/cognitive/r1/3rd and spine:6."
  author-agent-dialogue: "Raise this when a student is reading or reviewing sources. With a student, put it in plain second-person words as the least you need to show to gain honours at all; with staff, frame it as what teaching and assessment must give students room to show. Ask: \"Can you summarise this report accurately in a few lines and say how good it is?\" Avoid reading the table aloud or suggesting the threshold is what most students aim for."
- statement: qaa/social-policy-2026/4.9.b2.excellent
  forPractitioner: { text: "For first-class honours the statement requires that students read, listen to or watch material, analyse its strengths and weaknesses critically and, where it helps, offer alternatives backed by evidence; design tasks that let them show it.", rewrite: light, force: must, status: drafted }
  forBeneficiary: { text: "For a first-class degree, you need to be able to read, listen to or watch material, analyse its strengths and weaknesses critically and, where it helps, offer alternatives backed by evidence.", rewrite: full, force: must, status: drafted }
  author-agent-written: "Present this as the excellent standard, the attainment the statement requires for first-class honours in Social Policy at FHEQ Level 6 (FQHEIS Level 10): critical analysis with evidenced alternatives. Cite it as (QAA, 2026, Social Policy Subject Benchmark Statement, para 4.9), excellent column. Do not call it a regulatory requirement or present it as the minimum to pass. Set it beside 4.9.b2 and 4.9.b2.typical in the same row, Annex D qaa/fheq-2024/annex-d/cognitive/r1/1st and spine:6."
  author-agent-dialogue: "Raise this when a student is reading or reviewing sources. With a student, put it in plain second-person words as what a first-class result asks of you; with staff, frame it as what teaching and assessment must give students room to show. Ask: \"Where is this source weakest, and what better-evidenced view would you put in its place?\" Avoid reading the table aloud and never present this excellent standard as the minimum or as expected of everyone."
- statement: qaa/social-policy-2026/4.9.b2.typical
  forPractitioner: { text: "For second-class honours the statement requires that students assess and summarise, thoroughly and critically, the assumptions, arguments and evidence in reports, documents and audiovisual material; design tasks that let them show it.", rewrite: light, force: must, status: drafted }
  forBeneficiary: { text: "For a second-class degree, you need to be able to assess and summarise, thoroughly and critically, the assumptions, arguments and evidence in reports, documents and audiovisual material.", rewrite: full, force: must, status: drafted }
  author-agent-written: "Present this as the typical standard, the attainment the statement requires for second-class honours in Social Policy at FHEQ Level 6 (FQHEIS Level 10): thorough evaluation of assumptions and evidence. Cite it as (QAA, 2026, Social Policy Subject Benchmark Statement, para 4.9), typical column. Do not call it a regulatory requirement or present it as the minimum to pass. Set it beside 4.9.b2 and 4.9.b2.excellent in the same row, qaa/fheq-2024/4.15.b7 and Annex D qaa/fheq-2024/annex-d/cognitive/r1/2.1 and spine:6."
  author-agent-dialogue: "Raise this when a student is reading or reviewing sources. With a student, put it in plain second-person words as what a second-class result asks of you; with staff, frame it as what teaching and assessment must give students room to show. Ask: \"What does this report assume without saying so?\" Avoid reading the table aloud and never present this typical standard as the minimum for a pass."
- statement: qaa/social-policy-2026/4.9.b3
  forPractitioner: { text: "Every honours route must give students the chance to identify hard social issues and weigh the different responses to them; this is the minimum for third-class honours.", rewrite: light, force: threshold, status: drafted }
  forBeneficiary: { text: "To gain honours at all, you need to be able to identify hard social issues and weigh the different responses to them.", rewrite: full, force: threshold, status: drafted }
  author-agent-written: "Present this as the threshold standard, the minimum for third-class honours in Social Policy at FHEQ Level 6 (FQHEIS Level 10): spotting hard issues and weighing responses. Cite it as (QAA, 2026, Social Policy Subject Benchmark Statement, para 4.9), threshold column. Do not call it a regulatory requirement or apply it to the master's award. Set it beside 4.9.b3.typical and 4.9.b3.excellent in the same row, Annex D qaa/fheq-2024/annex-d/cognitive/r3/3rd and spine:6."
  author-agent-dialogue: "Raise this when a student is working on a policy problem or case study. With a student, put it in plain second-person words as the least you need to show to gain honours at all; with staff, frame it as what teaching and assessment must give students room to show. Ask: \"What is a hard social issue you have studied, and which responses to it did you compare?\" Avoid reading the table aloud or suggesting the threshold is what most students aim for."
- statement: qaa/social-policy-2026/4.9.b3.excellent
  forPractitioner: { text: "For first-class honours the statement requires that students evaluate issues critically and devise and test different responses grounded in evidence; design tasks that let them show it.", rewrite: light, force: must, status: drafted }
  forBeneficiary: { text: "For a first-class degree, you need to be able to evaluate issues critically and devise and test different responses grounded in evidence.", rewrite: full, force: must, status: drafted }
  author-agent-written: "Present this as the excellent standard, the attainment the statement requires for first-class honours in Social Policy at FHEQ Level 6 (FQHEIS Level 10): devising and testing evidenced responses. Cite it as (QAA, 2026, Social Policy Subject Benchmark Statement, para 4.9), excellent column. Do not call it a regulatory requirement or present it as the minimum to pass. Set it beside 4.9.b3 and 4.9.b3.typical in the same row, Annex D qaa/fheq-2024/annex-d/cognitive/r3/1st and spine:6."
  author-agent-dialogue: "Raise this when a student is working on a policy problem or case study. With a student, put it in plain second-person words as what a first-class result asks of you; with staff, frame it as what teaching and assessment must give students room to show. Ask: \"Which response would you design yourself, and how would you test it?\" Avoid reading the table aloud and never present this excellent standard as the minimum or as expected of everyone."
- statement: qaa/social-policy-2026/4.9.b3.typical
  forPractitioner: { text: "For second-class honours the statement requires that students analyse issues critically and weigh different solutions that rest on evidence; design tasks that let them show it.", rewrite: light, force: must, status: drafted }
  forBeneficiary: { text: "For a second-class degree, you need to be able to analyse issues critically and weigh different solutions that rest on evidence.", rewrite: full, force: must, status: drafted }
  author-agent-written: "Present this as the typical standard, the attainment the statement requires for second-class honours in Social Policy at FHEQ Level 6 (FQHEIS Level 10): critical analysis and evidenced solutions. Cite it as (QAA, 2026, Social Policy Subject Benchmark Statement, para 4.9), typical column. Do not call it a regulatory requirement or present it as the minimum to pass. Set it beside 4.9.b3 and 4.9.b3.excellent in the same row, Annex D qaa/fheq-2024/annex-d/cognitive/r3/2.2 and 2.1 and spine:6."
  author-agent-dialogue: "Raise this when a student is working on a policy problem or case study. With a student, put it in plain second-person words as what a second-class result asks of you; with staff, frame it as what teaching and assessment must give students room to show. Ask: \"Which solution has the strongest evidence behind it?\" Avoid reading the table aloud and never present this typical standard as the minimum for a pass."
- statement: qaa/social-policy-2026/4.9.b4
  forPractitioner: { text: "Every honours route must give students the chance to design and complete a research project, from planning through data collection and analysis to writing, with a supervisor's help; this is the minimum for third-class honours.", rewrite: light, force: threshold, status: drafted }
  forBeneficiary: { text: "To gain honours at all, you need to be able to design and complete a research project, from planning through data collection and analysis to writing, with a supervisor's help.", rewrite: full, force: threshold, status: drafted }
  author-agent-written: "Present this as the threshold standard, the minimum for third-class honours in Social Policy at FHEQ Level 6 (FQHEIS Level 10): a supervised research project. Cite it as (QAA, 2026, Social Policy Subject Benchmark Statement, para 4.9), threshold column. Do not call it a regulatory requirement or apply it to the master's award. Set it beside 4.9.b4.typical and 4.9.b4.excellent in the same row, qaa/fheq-2024/4.15.b6 and Annex D qaa/fheq-2024/annex-d/knowledge/r3/3rd and spine:6."
  author-agent-dialogue: "Raise this when a student is planning a dissertation or research project. With a student, put it in plain second-person words as the least you need to show to gain honours at all; with staff, frame it as what teaching and assessment must give students room to show. Ask: \"Which parts of your project did you plan yourself, and where did your supervisor step in?\" Avoid reading the table aloud or suggesting the threshold is what most students aim for."
- statement: qaa/social-policy-2026/4.9.b4.excellent
  forPractitioner: { text: "For first-class honours the statement requires that students design and complete a research project on their own, from planning and data work to writing up findings; design tasks that let them show it.", rewrite: light, force: must, status: drafted }
  forBeneficiary: { text: "For a first-class degree, you need to be able to design and complete a research project on your own, from planning and data work to writing up findings.", rewrite: full, force: must, status: drafted }
  author-agent-written: "Present this as the excellent standard, the attainment the statement requires for first-class honours in Social Policy at FHEQ Level 6 (FQHEIS Level 10): an independent research project. Cite it as (QAA, 2026, Social Policy Subject Benchmark Statement, para 4.9), excellent column. Do not call it a regulatory requirement or present it as the minimum to pass. Set it beside 4.9.b4 and 4.9.b4.typical in the same row, qaa/fheq-2024/4.15.b6 and Annex D qaa/fheq-2024/annex-d/knowledge/r3/1st and spine:6."
  author-agent-dialogue: "Raise this when a student is planning a dissertation or research project. With a student, put it in plain second-person words as what a first-class result asks of you; with staff, frame it as what teaching and assessment must give students room to show. Ask: \"Which decisions in your project were wholly yours?\" Avoid reading the table aloud and never present this excellent standard as the minimum or as expected of everyone."
- statement: qaa/social-policy-2026/4.9.b4.typical
  forPractitioner: { text: "For second-class honours the statement requires that students work on their own to find, record, combine and analyse information from a range of sources; design tasks that let them show it.", rewrite: light, force: must, status: drafted }
  forBeneficiary: { text: "For a second-class degree, you need to be able to work on your own to find, record, combine and analyse information from a range of sources.", rewrite: full, force: must, status: drafted }
  author-agent-written: "Present this as the typical standard, the attainment the statement requires for second-class honours in Social Policy at FHEQ Level 6 (FQHEIS Level 10): independent gathering and analysis of information. Cite it as (QAA, 2026, Social Policy Subject Benchmark Statement, para 4.9), typical column. Do not call it a regulatory requirement or present it as the minimum to pass. Set it beside 4.9.b4 and 4.9.b4.excellent in the same row, qaa/fheq-2024/4.15.b5 and Annex D qaa/fheq-2024/annex-d/knowledge/r3/2.2 and spine:6."
  author-agent-dialogue: "Raise this when a student is planning a dissertation or research project. With a student, put it in plain second-person words as what a second-class result asks of you; with staff, frame it as what teaching and assessment must give students room to show. Ask: \"How do you find and keep track of your sources without being told where to look?\" Avoid reading the table aloud and never present this typical standard as the minimum for a pass."
- statement: qaa/social-policy-2026/4.9.b5.excellent
  forPractitioner: { text: "For first-class honours the statement requires that students bring varied sources together accurately to build new knowledge or arguments; design tasks that let them show it.", rewrite: light, force: must, status: drafted }
  forBeneficiary: { text: "For a first-class degree, you need to be able to bring varied sources together accurately to build new knowledge or arguments.", rewrite: full, force: must, status: drafted }
  author-agent-written: "Present this as the excellent standard, the attainment the statement requires for first-class honours in Social Policy at FHEQ Level 6 (FQHEIS Level 10): synthesis into new knowledge or argument. Cite it as (QAA, 2026, Social Policy Subject Benchmark Statement, para 4.9), excellent column. Do not call it a regulatory requirement or present it as the minimum to pass. Set it beside 4.9.b4.excellent (the research row; this cell has no threshold or typical partner) in the same row, Annex D qaa/fheq-2024/annex-d/cognitive/r1/1st and spine:6."
  author-agent-dialogue: "Raise this when a student is drawing many sources together for a dissertation or long essay. With a student, put it in plain second-person words as what a first-class result asks of you; with staff, frame it as what teaching and assessment must give students room to show. Ask: \"What new argument came out of putting your sources together?\" Avoid reading the table aloud and never present this excellent standard as the minimum or as expected of everyone."
- statement: qaa/social-policy-2026/4.10.b1
  forPractitioner: { text: "Every honours route must give students the chance to communicate and present well in writing, in speech and other forms, and visually, to varied audiences with suitable technical aids; this is the minimum for third-class honours.", rewrite: light, force: threshold, status: drafted }
  forBeneficiary: { text: "To gain honours at all, you need to be able to communicate and present well in writing, in speech and other forms, and visually, to varied audiences with suitable technical aids.", rewrite: full, force: threshold, status: drafted }
  author-agent-written: "Present this as the threshold standard, the minimum for third-class honours in Social Policy at FHEQ Level 6 (FQHEIS Level 10): effective communication to varied audiences. Cite it as (QAA, 2026, Social Policy Subject Benchmark Statement, para 4.10), threshold column. Do not call it a regulatory requirement or apply it to the master's award. Set it beside 4.10.b1.typical and 4.10.b1.excellent in the same row, qaa/fheq-2024/4.15.b8 and Annex D qaa/fheq-2024/annex-d/transferable/r1/3rd and spine:6."
  author-agent-dialogue: "Raise this when a student prepares a presentation, briefing or written piece. With a student, put it in plain second-person words as the least you need to show to gain honours at all; with staff, frame it as what teaching and assessment must give students room to show. Ask: \"How did you adapt your last presentation for its audience?\" Avoid reading the table aloud or suggesting the threshold is what most students aim for."
- statement: qaa/social-policy-2026/4.10.b1.excellent
  forPractitioner: { text: "For first-class honours the statement requires that students put a complex, coherent argument into words, communicate ideas well in speech and writing and, where useful, use technical aids to build and give complex presentations; design tasks that let them show it.", rewrite: light, force: must, status: drafted }
  forBeneficiary: { text: "For a first-class degree, you need to be able to put a complex, coherent argument into words, communicate ideas well in speech and writing and, where useful, use technical aids to build and give complex presentations.", rewrite: full, force: must, status: drafted }
  author-agent-written: "Present this as the excellent standard, the attainment the statement requires for first-class honours in Social Policy at FHEQ Level 6 (FQHEIS Level 10): complex argument put across; complex presentations. Cite it as (QAA, 2026, Social Policy Subject Benchmark Statement, para 4.10), excellent column. Do not call it a regulatory requirement or present it as the minimum to pass. Set it beside 4.10.b1 and 4.10.b1.typical in the same row, Annex D qaa/fheq-2024/annex-d/transferable/r1/1st and spine:6."
  author-agent-dialogue: "Raise this when a student prepares a presentation, briefing or written piece. With a student, put it in plain second-person words as what a first-class result asks of you; with staff, frame it as what teaching and assessment must give students room to show. Ask: \"Could you present your most complex argument to a non-specialist audience in ten minutes?\" Avoid reading the table aloud and never present this excellent standard as the minimum or as expected of everyone."
- statement: qaa/social-policy-2026/4.10.b1.typical
  forPractitioner: { text: "For second-class honours the statement requires that students communicate well with varied audiences in many formats, written, spoken and visual, using technical aids where useful; design tasks that let them show it.", rewrite: light, force: must, status: drafted }
  forBeneficiary: { text: "For a second-class degree, you need to be able to communicate well with varied audiences in many formats, written, spoken and visual, using technical aids where useful.", rewrite: full, force: must, status: drafted }
  author-agent-written: "Present this as the typical standard, the attainment the statement requires for second-class honours in Social Policy at FHEQ Level 6 (FQHEIS Level 10): effective communication across formats. Cite it as (QAA, 2026, Social Policy Subject Benchmark Statement, para 4.10), typical column. Do not call it a regulatory requirement or present it as the minimum to pass. Set it beside 4.10.b1 and 4.10.b1.excellent in the same row, Annex D qaa/fheq-2024/annex-d/transferable/r1/2.2 and 2.1 and spine:6."
  author-agent-dialogue: "Raise this when a student prepares a presentation, briefing or written piece. With a student, put it in plain second-person words as what a second-class result asks of you; with staff, frame it as what teaching and assessment must give students room to show. Ask: \"Which formats have you used to share your work, and which suited which audience?\" Avoid reading the table aloud and never present this typical standard as the minimum for a pass."
- statement: qaa/social-policy-2026/4.10.b2
  forPractitioner: { text: "Every honours route must give students the chance to plan, organise and order their work so they meet deadlines; this is the minimum for third-class honours.", rewrite: light, force: threshold, status: drafted }
  forBeneficiary: { text: "To gain honours at all, you need to be able to plan, organise and order your work so you meet deadlines.", rewrite: full, force: threshold, status: drafted }
  author-agent-written: "Present this as the threshold standard, the minimum for third-class honours in Social Policy at FHEQ Level 6 (FQHEIS Level 10): planning work to deadlines. Cite it as (QAA, 2026, Social Policy Subject Benchmark Statement, para 4.10), threshold column. Do not call it a regulatory requirement or apply it to the master's award. Set it beside 4.10.b2.typical and 4.10.b2.excellent in the same row, Annex D qaa/fheq-2024/annex-d/transferable/r3/3rd and spine:6."
  author-agent-dialogue: "Raise this when a student is struggling with workload or moving to independent study. With a student, put it in plain second-person words as the least you need to show to gain honours at all; with staff, frame it as what teaching and assessment must give students room to show. Ask: \"How do you plan your week when two deadlines fall together?\" Avoid reading the table aloud or suggesting the threshold is what most students aim for."
- statement: qaa/social-policy-2026/4.10.b2.excellent
  forPractitioner: { text: "For first-class honours the statement requires that students design projects, marshal resources, find sources and use their own judgement; design tasks that let them show it.", rewrite: light, force: must, status: drafted }
  forBeneficiary: { text: "For a first-class degree, you need to be able to design projects, marshal resources, find sources and use your own judgement.", rewrite: full, force: must, status: drafted }
  author-agent-written: "Present this as the excellent standard, the attainment the statement requires for first-class honours in Social Policy at FHEQ Level 6 (FQHEIS Level 10): designing projects; independent judgement. Cite it as (QAA, 2026, Social Policy Subject Benchmark Statement, para 4.10), excellent column. Do not call it a regulatory requirement or present it as the minimum to pass. Set it beside 4.10.b2 and 4.10.b2.typical in the same row, qaa/fheq-2024/4.15.b9.1 and Annex D qaa/fheq-2024/annex-d/transferable/r3/1st and spine:6."
  author-agent-dialogue: "Raise this when a student is struggling with workload or moving to independent study. With a student, put it in plain second-person words as what a first-class result asks of you; with staff, frame it as what teaching and assessment must give students room to show. Ask: \"Which project have you shaped yourself from the start?\" Avoid reading the table aloud and never present this excellent standard as the minimum or as expected of everyone."
- statement: qaa/social-policy-2026/4.10.b2.typical
  forPractitioner: { text: "For second-class honours the statement requires that students plan, use their time well and work on their own; design tasks that let them show it.", rewrite: light, force: must, status: drafted }
  forBeneficiary: { text: "For a second-class degree, you need to be able to plan, use your time well and work on your own.", rewrite: full, force: must, status: drafted }
  author-agent-written: "Present this as the typical standard, the attainment the statement requires for second-class honours in Social Policy at FHEQ Level 6 (FQHEIS Level 10): time management and independent work. Cite it as (QAA, 2026, Social Policy Subject Benchmark Statement, para 4.10), typical column. Do not call it a regulatory requirement or present it as the minimum to pass. Set it beside 4.10.b2 and 4.10.b2.excellent in the same row, Annex D qaa/fheq-2024/annex-d/transferable/r3/2.2 and 2.1 and spine:6."
  author-agent-dialogue: "Raise this when a student is struggling with workload or moving to independent study. With a student, put it in plain second-person words as what a second-class result asks of you; with staff, frame it as what teaching and assessment must give students room to show. Ask: \"Where do you work best without guidance, and where do you still need it?\" Avoid reading the table aloud and never present this typical standard as the minimum for a pass."
- statement: qaa/social-policy-2026/4.10.b3
  forPractitioner: { text: "Every honours route must give students the chance to form groups, take part and work well within them; this is the minimum for third-class honours.", rewrite: light, force: threshold, status: drafted }
  forBeneficiary: { text: "To gain honours at all, you need to be able to form groups, take part and work well within them.", rewrite: full, force: threshold, status: drafted }
  author-agent-written: "Present this as the threshold standard, the minimum for third-class honours in Social Policy at FHEQ Level 6 (FQHEIS Level 10): effective group work. Cite it as (QAA, 2026, Social Policy Subject Benchmark Statement, para 4.10), threshold column. Do not call it a regulatory requirement or apply it to the master's award. Set it beside 4.10.b3.typical and 4.10.b3.excellent in the same row, Annex D qaa/fheq-2024/annex-d/transferable/r2/3rd and spine:6."
  author-agent-dialogue: "Raise this when group work is set or a group is not working well. With a student, put it in plain second-person words as the least you need to show to gain honours at all; with staff, frame it as what teaching and assessment must give students room to show. Ask: \"What did you contribute to your last group task?\" Avoid reading the table aloud or suggesting the threshold is what most students aim for."
- statement: qaa/social-policy-2026/4.10.b3.excellent
  forPractitioner: { text: "For first-class honours the statement requires that students start and form groups, engage constructively and work well within them; design tasks that let them show it.", rewrite: light, force: must, status: drafted }
  forBeneficiary: { text: "For a first-class degree, you need to be able to start and form groups, engage constructively and work well within them.", rewrite: full, force: must, status: drafted }
  author-agent-written: "Present this as the excellent standard, the attainment the statement requires for first-class honours in Social Policy at FHEQ Level 6 (FQHEIS Level 10): starting groups and engaging constructively. Cite it as (QAA, 2026, Social Policy Subject Benchmark Statement, para 4.10), excellent column. Do not call it a regulatory requirement or present it as the minimum to pass. Set it beside 4.10.b3 and 4.10.b3.typical in the same row, Annex D qaa/fheq-2024/annex-d/transferable/r2/1st and spine:6."
  author-agent-dialogue: "Raise this when group work is set or a group is not working well. With a student, put it in plain second-person words as what a first-class result asks of you; with staff, frame it as what teaching and assessment must give students room to show. Ask: \"How did you handle disagreement in a group you led?\" Avoid reading the table aloud and never present this excellent standard as the minimum or as expected of everyone."
- statement: qaa/social-policy-2026/4.10.b3.typical
  forPractitioner: { text: "For second-class honours the statement requires that students start, coordinate and contribute well to group work and shared projects; design tasks that let them show it.", rewrite: light, force: must, status: drafted }
  forBeneficiary: { text: "For a second-class degree, you need to be able to start, coordinate and contribute well to group work and shared projects.", rewrite: full, force: must, status: drafted }
  author-agent-written: "Present this as the typical standard, the attainment the statement requires for second-class honours in Social Policy at FHEQ Level 6 (FQHEIS Level 10): starting and coordinating group work. Cite it as (QAA, 2026, Social Policy Subject Benchmark Statement, para 4.10), typical column. Do not call it a regulatory requirement or present it as the minimum to pass. Set it beside 4.10.b3 and 4.10.b3.excellent in the same row, Annex D qaa/fheq-2024/annex-d/transferable/r2/2.2 and 2.1 and spine:6."
  author-agent-dialogue: "Raise this when group work is set or a group is not working well. With a student, put it in plain second-person words as what a second-class result asks of you; with staff, frame it as what teaching and assessment must give students room to show. Ask: \"Have you ever set a group task going or kept one on track, and how?\" Avoid reading the table aloud and never present this typical standard as the minimum for a pass."
- statement: qaa/social-policy-2026/4.10.b4
  forPractitioner: { text: "Every honours route must give students the chance to use current and new technologies, know about emerging ones and use generative AI tools fittingly for specific tasks; this is the minimum for third-class honours.", rewrite: light, force: threshold, status: drafted }
  forBeneficiary: { text: "To gain honours at all, you need to be able to use current and new technologies, know about emerging ones and use generative AI tools fittingly for specific tasks.", rewrite: full, force: threshold, status: drafted }
  author-agent-written: "Present this as the threshold standard, the minimum for third-class honours in Social Policy at FHEQ Level 6 (FQHEIS Level 10): using technologies, generative AI included. Cite it as (QAA, 2026, Social Policy Subject Benchmark Statement, para 4.10), threshold column. Do not call it a regulatory requirement or apply it to the master's award. Set it beside 4.10.b4.typical and 4.10.b4.excellent in the same row, Annex D qaa/fheq-2024/annex-d/transferable/r1/3rd and spine:6."
  author-agent-dialogue: "Raise this when a student asks about digital tools or generative AI. With a student, put it in plain second-person words as the least you need to show to gain honours at all; with staff, frame it as what teaching and assessment must give students room to show. Ask: \"Which digital tools, generative AI included, did you use on your last assignment, and for what?\" Avoid reading the table aloud or suggesting the threshold is what most students aim for."
- statement: qaa/social-policy-2026/4.10.b4.excellent
  forPractitioner: { text: "For first-class honours the statement requires that students use current, new and emerging technologies proficiently, generative AI tools included where fitting; design tasks that let them show it.", rewrite: light, force: must, status: drafted }
  forBeneficiary: { text: "For a first-class degree, you need to be able to use current, new and emerging technologies proficiently, generative AI tools included where fitting.", rewrite: full, force: must, status: drafted }
  author-agent-written: "Present this as the excellent standard, the attainment the statement requires for first-class honours in Social Policy at FHEQ Level 6 (FQHEIS Level 10): proficient use of evolving technology. Cite it as (QAA, 2026, Social Policy Subject Benchmark Statement, para 4.10), excellent column. Do not call it a regulatory requirement or present it as the minimum to pass. Set it beside 4.10.b4 and 4.10.b4.typical in the same row, Annex D qaa/fheq-2024/annex-d/transferable/r1/1st and spine:6."
  author-agent-dialogue: "Raise this when a student asks about digital tools or generative AI. With a student, put it in plain second-person words as what a first-class result asks of you; with staff, frame it as what teaching and assessment must give students room to show. Ask: \"Which new tool have you mastered recently, and where would you not use it?\" Avoid reading the table aloud and never present this excellent standard as the minimum or as expected of everyone."
- statement: qaa/social-policy-2026/4.10.b4.typical
  forPractitioner: { text: "For second-class honours the statement requires that students use a wide range of current and new technologies competently and confidently to find, analyse and present information, generative AI tools included where fitting; design tasks that let them show it.", rewrite: light, force: must, status: drafted }
  forBeneficiary: { text: "For a second-class degree, you need to be able to use a wide range of current and new technologies competently and confidently to find, analyse and present information, generative AI tools included where fitting.", rewrite: full, force: must, status: drafted }
  author-agent-written: "Present this as the typical standard, the attainment the statement requires for second-class honours in Social Policy at FHEQ Level 6 (FQHEIS Level 10): confident use of technology to handle information. Cite it as (QAA, 2026, Social Policy Subject Benchmark Statement, para 4.10), typical column. Do not call it a regulatory requirement or present it as the minimum to pass. Set it beside 4.10.b4 and 4.10.b4.excellent in the same row, Annex D qaa/fheq-2024/annex-d/transferable/r1/2.2 and 2.1 and spine:6."
  author-agent-dialogue: "Raise this when a student asks about digital tools or generative AI. With a student, put it in plain second-person words as what a second-class result asks of you; with staff, frame it as what teaching and assessment must give students room to show. Ask: \"How confident are you using software to analyse data, and how do you check what an AI tool gives you?\" Avoid reading the table aloud and never present this typical standard as the minimum for a pass."
- statement: qaa/social-policy-2026/4.10.b5
  forPractitioner: { text: "Every honours route must give students the chance to reference their sources accurately as evidence for the work they hand in; this is the minimum for third-class honours.", rewrite: light, force: threshold, status: drafted }
  forBeneficiary: { text: "To gain honours at all, you need to be able to reference your sources accurately as evidence for the work you hand in.", rewrite: full, force: threshold, status: drafted }
  author-agent-written: "Present this as the threshold standard, the minimum for third-class honours in Social Policy at FHEQ Level 6 (FQHEIS Level 10): accurate referencing. Cite it as (QAA, 2026, Social Policy Subject Benchmark Statement, para 4.10), threshold column. Do not call it a regulatory requirement or apply it to the master's award. Set it beside 4.10.b5.typical and 4.10.b5.excellent in the same row, Annex D qaa/fheq-2024/annex-d/professional/r2/3rd-1st and spine:6."
  author-agent-dialogue: "Raise this when referencing, plagiarism or academic integrity come up. With a student, put it in plain second-person words as the least you need to show to gain honours at all; with staff, frame it as what teaching and assessment must give students room to show. Ask: \"How do you make sure every source in your essay is credited accurately?\" Avoid reading the table aloud or suggesting the threshold is what most students aim for."
- statement: qaa/social-policy-2026/4.10.b5.excellent
  forPractitioner: { text: "For first-class honours the statement requires that students find sources and reference them accurately as academic convention requires; design tasks that let them show it.", rewrite: light, force: must, status: drafted }
  forBeneficiary: { text: "For a first-class degree, you need to be able to find sources and reference them accurately as academic convention requires.", rewrite: full, force: must, status: drafted }
  author-agent-written: "Present this as the excellent standard, the attainment the statement requires for first-class honours in Social Policy at FHEQ Level 6 (FQHEIS Level 10): finding and referencing sources to convention. Cite it as (QAA, 2026, Social Policy Subject Benchmark Statement, para 4.10), excellent column. Do not call it a regulatory requirement or present it as the minimum to pass. Set it beside 4.10.b5 and 4.10.b5.typical in the same row, Annex D qaa/fheq-2024/annex-d/knowledge/r3/1st and spine:6."
  author-agent-dialogue: "Raise this when referencing, plagiarism or academic integrity come up. With a student, put it in plain second-person words as what a first-class result asks of you; with staff, frame it as what teaching and assessment must give students room to show. Ask: \"How did you find the sources nobody pointed you to, and are they referenced correctly?\" Avoid reading the table aloud and never present this excellent standard as the minimum or as expected of everyone."
- statement: qaa/social-policy-2026/4.10.b5.typical
  forPractitioner: { text: "For second-class honours the statement requires that students understand standard referencing systems and apply them correctly in the text and the reference list; design tasks that let them show it.", rewrite: light, force: must, status: drafted }
  forBeneficiary: { text: "For a second-class degree, you need to be able to understand standard referencing systems and apply them correctly in the text and the reference list.", rewrite: full, force: must, status: drafted }
  author-agent-written: "Present this as the typical standard, the attainment the statement requires for second-class honours in Social Policy at FHEQ Level 6 (FQHEIS Level 10): standard referencing systems. Cite it as (QAA, 2026, Social Policy Subject Benchmark Statement, para 4.10), typical column. Do not call it a regulatory requirement or present it as the minimum to pass. Set it beside 4.10.b5 and 4.10.b5.excellent in the same row, Annex D qaa/fheq-2024/annex-d/professional/r2/3rd-1st and spine:6."
  author-agent-dialogue: "Raise this when referencing, plagiarism or academic integrity come up. With a student, put it in plain second-person words as what a second-class result asks of you; with staff, frame it as what teaching and assessment must give students room to show. Ask: \"Which referencing system do you use, and where does it trip you up?\" Avoid reading the table aloud and never present this typical standard as the minimum for a pass."
- statement: qaa/social-policy-2026/4.12.b1.masters
  forPractitioner: { text: "Design the master's course so that graduates can show a sound grasp of the wider policy field with deep knowledge of at least one major area, such as housing, health, pensions, social security or global policy.", rewrite: light, force: describes, status: drafted }
  forBeneficiary: { text: "By the end of your master's, you are expected to show a sound grasp of the wider policy field with deep knowledge of at least one major area, such as housing, health, pensions, social security or global policy.", rewrite: full, force: describes, status: drafted }
  author-agent-written: "Present this as an outcome expected of anyone completing a Social Policy master's degree, set at FHEQ Level 7 (FQHEIS Level 11): breadth across the field with depth in one area; the issuer's word is 'expected', so state it without must or will. Cite it as (QAA, 2026, Social Policy Subject Benchmark Statement, para 4.12). Do not apply it to the honours degree, call it a regulatory requirement or grade it into typical or excellent, since the master's lists name no rungs. Set it beside qaa/fheq-2024/4.17.b1 and spine:7."
  author-agent-dialogue: "Raise this when a master's student plans their specialism or a team designs the core of a master's course. With a master's student, ask in plain second-person words how far they can already show it; with staff, frame it as what the master's course is expected to develop. Ask: \"Which area of policy is your specialism, and how does it fit the wider field?\" Avoid treating the list as a checklist, which 4.11 says it is not, or reading it aloud."
- statement: qaa/social-policy-2026/4.12.b2.masters
  forPractitioner: { text: "Design the master's course so that graduates can show a thorough, full understanding of human need, social justice and personal and shared wellbeing today, and how they relate to policy analysis.", rewrite: light, force: describes, status: drafted }
  forBeneficiary: { text: "By the end of your master's, you are expected to show a thorough, full understanding of human need, social justice and personal and shared wellbeing today, and how you relate to policy analysis.", rewrite: full, force: describes, status: drafted }
  author-agent-written: "Present this as an outcome expected of anyone completing a Social Policy master's degree, set at FHEQ Level 7 (FQHEIS Level 11): need, justice and wellbeing in policy analysis; the issuer's word is 'expected', so state it without must or will. Cite it as (QAA, 2026, Social Policy Subject Benchmark Statement, para 4.12). Do not apply it to the honours degree, call it a regulatory requirement or grade it into typical or excellent, since the master's lists name no rungs. Set it beside qaa/fheq-2024/4.17.b1 and spine:7."
  author-agent-dialogue: "Raise this when a master's student plans their specialism or a team designs the core of a master's course. With a master's student, ask in plain second-person words how far they can already show it; with staff, frame it as what the master's course is expected to develop. Ask: \"How does your view of social justice shape the policy analysis you do?\" Avoid treating the list as a checklist, which 4.11 says it is not, or reading it aloud."
- statement: qaa/social-policy-2026/4.12.b3.masters
  forPractitioner: { text: "Design the master's course so that graduates can show the capacity to work with and apply the subject's core concepts and theories to judge research and scholarship critically.", rewrite: light, force: describes, status: drafted }
  forBeneficiary: { text: "By the end of your master's, you are expected to show the capacity to work with and apply the subject's core concepts and theories to judge research and scholarship critically.", rewrite: full, force: describes, status: drafted }
  author-agent-written: "Present this as an outcome expected of anyone completing a Social Policy master's degree, set at FHEQ Level 7 (FQHEIS Level 11): core theory used to judge research; the issuer's word is 'expected', so state it without must or will. Cite it as (QAA, 2026, Social Policy Subject Benchmark Statement, para 4.12). Do not apply it to the honours degree, call it a regulatory requirement or grade it into typical or excellent, since the master's lists name no rungs. Set it beside qaa/fheq-2024/4.17.b4.1 and spine:7."
  author-agent-dialogue: "Raise this when a master's student plans their specialism or a team designs the core of a master's course. With a master's student, ask in plain second-person words how far they can already show it; with staff, frame it as what the master's course is expected to develop. Ask: \"Which theory do you use to judge the studies you read, and why that one?\" Avoid treating the list as a checklist, which 4.11 says it is not, or reading it aloud."
- statement: qaa/social-policy-2026/4.12.b4.masters
  forPractitioner: { text: "Design the master's course so that graduates can show a sound understanding of one particular form of social injustice, how it is reproduced, kept in place and tackled, and its policy setting.", rewrite: light, force: describes, status: drafted }
  forBeneficiary: { text: "By the end of your master's, you are expected to show a sound understanding of one particular form of social injustice, how it is reproduced, kept in place and tackled, and its policy setting.", rewrite: full, force: describes, status: drafted }
  author-agent-written: "Present this as an outcome expected of anyone completing a Social Policy master's degree, set at FHEQ Level 7 (FQHEIS Level 11): one form of social injustice in depth; the issuer's word is 'expected', so state it without must or will. Cite it as (QAA, 2026, Social Policy Subject Benchmark Statement, para 4.12). Do not apply it to the honours degree, call it a regulatory requirement or grade it into typical or excellent, since the master's lists name no rungs. Set it beside qaa/fheq-2024/4.17.b1 and spine:7."
  author-agent-dialogue: "Raise this when a master's student plans their specialism or a team designs the core of a master's course. With a master's student, ask in plain second-person words how far they can already show it; with staff, frame it as what the master's course is expected to develop. Ask: \"Which injustice have you studied in depth, and what keeps it in place?\" Avoid treating the list as a checklist, which 4.11 says it is not, or reading it aloud."
- statement: qaa/social-policy-2026/4.12.b5.masters
  forPractitioner: { text: "Design the master's course so that graduates can show the ability to recognise and make plain how norms, values and worldviews define injustice, shape policy processes and inform solutions.", rewrite: light, force: describes, status: drafted }
  forBeneficiary: { text: "By the end of your master's, you are expected to show the ability to recognise and make plain how norms, values and worldviews define injustice, shape policy processes and inform solutions.", rewrite: full, force: describes, status: drafted }
  author-agent-written: "Present this as an outcome expected of anyone completing a Social Policy master's degree, set at FHEQ Level 7 (FQHEIS Level 11): norms and worldviews in injustice and policy; the issuer's word is 'expected', so state it without must or will. Cite it as (QAA, 2026, Social Policy Subject Benchmark Statement, para 4.12). Do not apply it to the honours degree, call it a regulatory requirement or grade it into typical or excellent, since the master's lists name no rungs. Set it beside qaa/fheq-2024/4.17.b4.2 and spine:7."
  author-agent-dialogue: "Raise this when a master's student plans their specialism or a team designs the core of a master's course. With a master's student, ask in plain second-person words how far they can already show it; with staff, frame it as what the master's course is expected to develop. Ask: \"Whose worldview defines the problem in the policy you are studying?\" Avoid treating the list as a checklist, which 4.11 says it is not, or reading it aloud."
- statement: qaa/social-policy-2026/4.12.b6.masters
  forPractitioner: { text: "Design the master's course so that graduates can show knowledge of a range of research methods and the ability to design and carry out an independent, supervised dissertation or project.", rewrite: light, force: describes, status: drafted }
  forBeneficiary: { text: "By the end of your master's, you are expected to show knowledge of a range of research methods and the ability to design and carry out an independent, supervised dissertation or project.", rewrite: full, force: describes, status: drafted }
  author-agent-written: "Present this as an outcome expected of anyone completing a Social Policy master's degree, set at FHEQ Level 7 (FQHEIS Level 11): research methods and a supervised dissertation; the issuer's word is 'expected', so state it without must or will. Cite it as (QAA, 2026, Social Policy Subject Benchmark Statement, para 4.12). Do not apply it to the honours degree, call it a regulatory requirement or grade it into typical or excellent, since the master's lists name no rungs. Set it beside qaa/fheq-2024/4.17.b2 and qaa/fheq-2024/4.17.b6 and spine:7."
  author-agent-dialogue: "Raise this when a master's student plans their specialism or a team designs the core of a master's course. With a master's student, ask in plain second-person words how far they can already show it; with staff, frame it as what the master's course is expected to develop. Ask: \"Which methods did you consider for your dissertation before choosing one?\" Avoid treating the list as a checklist, which 4.11 says it is not, or reading it aloud."
- statement: qaa/social-policy-2026/4.13.b1.masters
  forPractitioner: { text: "Design the master's course so that graduates can show deep understanding of how policy is made, practised and felt, at local, national and international scale, across differing jurisdictions and welfare histories.", rewrite: light, force: describes, status: drafted }
  forBeneficiary: { text: "By the end of your master's, you are expected to show deep understanding of how policy is made, practised and felt, at local, national and international scale, across differing jurisdictions and welfare histories.", rewrite: full, force: describes, status: drafted }
  author-agent-written: "Present this as an outcome expected of anyone completing a Social Policy master's degree, set at FHEQ Level 7 (FQHEIS Level 11): policy making and impact across jurisdictions; the issuer's word is 'expected', so state it without must or will. Cite it as (QAA, 2026, Social Policy Subject Benchmark Statement, para 4.13). Do not apply it to the honours degree, call it a regulatory requirement or grade it into typical or excellent, since the master's lists name no rungs. Set it beside qaa/fheq-2024/4.17.b1 and spine:7."
  author-agent-dialogue: "Raise this when a master's student is analysing policy or a team designs master's modules. With a master's student, ask in plain second-person words how far they can already show it; with staff, frame it as what the master's course is expected to develop. Ask: \"How would this policy play out differently in another jurisdiction with a different welfare history?\" Avoid treating the list as a checklist, which 4.11 says it is not, or reading it aloud."
- statement: qaa/social-policy-2026/4.13.b2.masters
  forPractitioner: { text: "Design the master's course so that graduates can show the ability to carry out comparative analysis of regime types, policy-making styles and actual policies.", rewrite: light, force: describes, status: drafted }
  forBeneficiary: { text: "By the end of your master's, you are expected to show the ability to carry out comparative analysis of regime types, policy-making styles and actual policies.", rewrite: full, force: describes, status: drafted }
  author-agent-written: "Present this as an outcome expected of anyone completing a Social Policy master's degree, set at FHEQ Level 7 (FQHEIS Level 11): comparative analysis of regimes and policies; the issuer's word is 'expected', so state it without must or will. Cite it as (QAA, 2026, Social Policy Subject Benchmark Statement, para 4.13). Do not apply it to the honours degree, call it a regulatory requirement or grade it into typical or excellent, since the master's lists name no rungs. Set it beside qaa/fheq-2024/4.17.b2 and spine:7."
  author-agent-dialogue: "Raise this when a master's student is analysing policy or a team designs master's modules. With a master's student, ask in plain second-person words how far they can already show it; with staff, frame it as what the master's course is expected to develop. Ask: \"Which two regimes would you compare for your topic, and on what basis?\" Avoid treating the list as a checklist, which 4.11 says it is not, or reading it aloud."
- statement: qaa/social-policy-2026/4.13.b3.masters
  forPractitioner: { text: "Design the master's course so that graduates can show the ability to identify and understand what key stakeholders, from service users to policymakers, do and think, and how open policy making is to democratic participation and co-production.", rewrite: light, force: describes, status: drafted }
  forBeneficiary: { text: "By the end of your master's, you are expected to show the ability to identify and understand what key stakeholders, from service users to policymakers, do and think, and how open policy making is to democratic participation and co-production.", rewrite: full, force: describes, status: drafted }
  author-agent-written: "Present this as an outcome expected of anyone completing a Social Policy master's degree, set at FHEQ Level 7 (FQHEIS Level 11): stakeholders and democratic participation; the issuer's word is 'expected', so state it without must or will. Cite it as (QAA, 2026, Social Policy Subject Benchmark Statement, para 4.13). Do not apply it to the honours degree, call it a regulatory requirement or grade it into typical or excellent, since the master's lists name no rungs. Set it beside qaa/fheq-2024/4.17.b5 and spine:7."
  author-agent-dialogue: "Raise this when a master's student is analysing policy or a team designs master's modules. With a master's student, ask in plain second-person words how far they can already show it; with staff, frame it as what the master's course is expected to develop. Ask: \"Who has a say in this policy, and who is left out?\" Avoid treating the list as a checklist, which 4.11 says it is not, or reading it aloud."
- statement: qaa/social-policy-2026/4.13.b4.masters
  forPractitioner: { text: "Design the master's course so that graduates can show critical understanding of how making and delivering policy affects, and is lived by, service users, claimants and the public.", rewrite: light, force: describes, status: drafted }
  forBeneficiary: { text: "By the end of your master's, you are expected to show critical understanding of how making and delivering policy affects, and is lived by, service users, claimants and the public.", rewrite: full, force: describes, status: drafted }
  author-agent-written: "Present this as an outcome expected of anyone completing a Social Policy master's degree, set at FHEQ Level 7 (FQHEIS Level 11): how policy is felt by users and the public; the issuer's word is 'expected', so state it without must or will. Cite it as (QAA, 2026, Social Policy Subject Benchmark Statement, para 4.13). Do not apply it to the honours degree, call it a regulatory requirement or grade it into typical or excellent, since the master's lists name no rungs. Set it beside qaa/fheq-2024/4.17.b1 and spine:7."
  author-agent-dialogue: "Raise this when a master's student is analysing policy or a team designs master's modules. With a master's student, ask in plain second-person words how far they can already show it; with staff, frame it as what the master's course is expected to develop. Ask: \"How do claimants experience the policy you are studying, and what evidence shows it?\" Avoid treating the list as a checklist, which 4.11 says it is not, or reading it aloud."
- statement: qaa/social-policy-2026/4.13.b5.masters
  forPractitioner: { text: "Design the master's course so that graduates can show critical understanding of equality issues and how they intersect, applied to policy analysis.", rewrite: light, force: describes, status: drafted }
  forBeneficiary: { text: "By the end of your master's, you are expected to show critical understanding of equality issues and how you intersect, applied to policy analysis.", rewrite: full, force: describes, status: drafted }
  author-agent-written: "Present this as an outcome expected of anyone completing a Social Policy master's degree, set at FHEQ Level 7 (FQHEIS Level 11): intersecting equality issues in analysis; the issuer's word is 'expected', so state it without must or will. Cite it as (QAA, 2026, Social Policy Subject Benchmark Statement, para 4.13). Do not apply it to the honours degree, call it a regulatory requirement or grade it into typical or excellent, since the master's lists name no rungs. Set it beside qaa/fheq-2024/4.17.b3 and spine:7."
  author-agent-dialogue: "Raise this when a master's student is analysing policy or a team designs master's modules. With a master's student, ask in plain second-person words how far they can already show it; with staff, frame it as what the master's course is expected to develop. Ask: \"Which intersecting inequalities matter most in your topic?\" Avoid treating the list as a checklist, which 4.11 says it is not, or reading it aloud."
- statement: qaa/social-policy-2026/4.13.b6.masters
  forPractitioner: { text: "Design the master's course so that graduates can show critical, reflective understanding of why diversity, equity, inclusion, decolonisation, equality and environmental sustainability matter at every stage of research and practice, locally to globally and across cultures.", rewrite: light, force: describes, status: drafted }
  forBeneficiary: { text: "By the end of your master's, you are expected to show critical, reflective understanding of why diversity, equity, inclusion, decolonisation, equality and environmental sustainability matter at every stage of research and practice, locally to globally and across cultures.", rewrite: full, force: describes, status: drafted }
  author-agent-written: "Present this as an outcome expected of anyone completing a Social Policy master's degree, set at FHEQ Level 7 (FQHEIS Level 11): EDI, decolonisation and sustainability in research and practice; the issuer's word is 'expected', so state it without must or will. Cite it as (QAA, 2026, Social Policy Subject Benchmark Statement, para 4.13). Do not apply it to the honours degree, call it a regulatory requirement or grade it into typical or excellent, since the master's lists name no rungs. Set it beside qaa/fheq-2024/4.17.b1 and qaa/fheq-2024/4.17.b8.2 and spine:7."
  author-agent-dialogue: "Raise this when a master's student is analysing policy or a team designs master's modules. With a master's student, ask in plain second-person words how far they can already show it; with staff, frame it as what the master's course is expected to develop. Ask: \"How have equity and sustainability shaped the design of your own research?\" Avoid treating the list as a checklist, which 4.11 says it is not, or reading it aloud."
- statement: qaa/social-policy-2026/4.13.b7.masters
  forPractitioner: { text: "Design the master's course so that graduates can show critical, constructive engagement with current debates on injustice and policy reform at home and abroad.", rewrite: light, force: describes, status: drafted }
  forBeneficiary: { text: "By the end of your master's, you are expected to show critical, constructive engagement with current debates on injustice and policy reform at home and abroad.", rewrite: full, force: describes, status: drafted }
  author-agent-written: "Present this as an outcome expected of anyone completing a Social Policy master's degree, set at FHEQ Level 7 (FQHEIS Level 11): engaging with current reform debates; the issuer's word is 'expected', so state it without must or will. Cite it as (QAA, 2026, Social Policy Subject Benchmark Statement, para 4.13). Do not apply it to the honours degree, call it a regulatory requirement or grade it into typical or excellent, since the master's lists name no rungs. Set it beside qaa/fheq-2024/4.17.b4.1 and spine:7."
  author-agent-dialogue: "Raise this when a master's student is analysing policy or a team designs master's modules. With a master's student, ask in plain second-person words how far they can already show it; with staff, frame it as what the master's course is expected to develop. Ask: \"Which current reform debate have you taken part in, and what did you add?\" Avoid treating the list as a checklist, which 4.11 says it is not, or reading it aloud."
- statement: qaa/social-policy-2026/4.13.b8.masters
  forPractitioner: { text: "Design the master's course so that graduates can show critical analysis of what neighbouring disciplines bring to policy analysis.", rewrite: light, force: describes, status: drafted }
  forBeneficiary: { text: "By the end of your master's, you are expected to show critical analysis of what neighbouring disciplines bring to policy analysis.", rewrite: full, force: describes, status: drafted }
  author-agent-written: "Present this as an outcome expected of anyone completing a Social Policy master's degree, set at FHEQ Level 7 (FQHEIS Level 11): what neighbouring disciplines contribute; the issuer's word is 'expected', so state it without must or will. Cite it as (QAA, 2026, Social Policy Subject Benchmark Statement, para 4.13). Do not apply it to the honours degree, call it a regulatory requirement or grade it into typical or excellent, since the master's lists name no rungs. Set it beside qaa/fheq-2024/4.17.b3 and spine:7."
  author-agent-dialogue: "Raise this when a master's student is analysing policy or a team designs master's modules. With a master's student, ask in plain second-person words how far they can already show it; with staff, frame it as what the master's course is expected to develop. Ask: \"What does economics or sociology add to your analysis that the subject alone would miss?\" Avoid treating the list as a checklist, which 4.11 says it is not, or reading it aloud."
- statement: qaa/social-policy-2026/4.14.b1.masters
  forPractitioner: { text: "Design the master's course so that graduates can show the capacity to judge and use quantitative, qualitative or mixed-methods research.", rewrite: light, force: describes, status: drafted }
  forBeneficiary: { text: "By the end of your master's, you are expected to show the capacity to judge and use quantitative, qualitative or mixed-methods research.", rewrite: full, force: describes, status: drafted }
  author-agent-written: "Present this as an outcome expected of anyone completing a Social Policy master's degree, set at FHEQ Level 7 (FQHEIS Level 11): judging and using research of every kind; the issuer's word is 'expected', so state it without must or will. Cite it as (QAA, 2026, Social Policy Subject Benchmark Statement, para 4.14). Do not apply it to the honours degree, call it a regulatory requirement or grade it into typical or excellent, since the master's lists name no rungs. Set it beside qaa/fheq-2024/4.17.b2 and spine:7."
  author-agent-dialogue: "Raise this when a master's student is planning research or a dissertation. With a master's student, ask in plain second-person words how far they can already show it; with staff, frame it as what the master's course is expected to develop. Ask: \"Which kind of evidence, numbers or interviews, do you find harder to judge?\" Avoid treating the list as a checklist, which 4.11 says it is not, or reading it aloud."
- statement: qaa/social-policy-2026/4.14.b2.masters
  forPractitioner: { text: "Design the master's course so that graduates can show a developed ability to gather data with fitting quantitative, qualitative or mixed approaches.", rewrite: light, force: describes, status: drafted }
  forBeneficiary: { text: "By the end of your master's, you are expected to show a developed ability to gather data with fitting quantitative, qualitative or mixed approaches.", rewrite: full, force: describes, status: drafted }
  author-agent-written: "Present this as an outcome expected of anyone completing a Social Policy master's degree, set at FHEQ Level 7 (FQHEIS Level 11): collecting data by fitting methods; the issuer's word is 'expected', so state it without must or will. Cite it as (QAA, 2026, Social Policy Subject Benchmark Statement, para 4.14). Do not apply it to the honours degree, call it a regulatory requirement or grade it into typical or excellent, since the master's lists name no rungs. Set it beside qaa/fheq-2024/4.17.b2 and spine:7."
  author-agent-dialogue: "Raise this when a master's student is planning research or a dissertation. With a master's student, ask in plain second-person words how far they can already show it; with staff, frame it as what the master's course is expected to develop. Ask: \"How did you decide how to collect your data?\" Avoid treating the list as a checklist, which 4.11 says it is not, or reading it aloud."
- statement: qaa/social-policy-2026/4.14.b3.masters
  forPractitioner: { text: "Design the master's course so that graduates can show understanding and use of the principles of ethical research.", rewrite: light, force: describes, status: drafted }
  forBeneficiary: { text: "By the end of your master's, you are expected to show understanding and use of the principles of ethical research.", rewrite: full, force: describes, status: drafted }
  author-agent-written: "Present this as an outcome expected of anyone completing a Social Policy master's degree, set at FHEQ Level 7 (FQHEIS Level 11): ethical research practice; the issuer's word is 'expected', so state it without must or will. Cite it as (QAA, 2026, Social Policy Subject Benchmark Statement, para 4.14). Do not apply it to the honours degree, call it a regulatory requirement or grade it into typical or excellent, since the master's lists name no rungs. Set it beside qaa/fheq-2024/4.17.b5 and spine:7."
  author-agent-dialogue: "Raise this when a master's student is planning research or a dissertation. With a master's student, ask in plain second-person words how far they can already show it; with staff, frame it as what the master's course is expected to develop. Ask: \"What ethical risks does your research carry, and how have you dealt with them?\" Avoid treating the list as a checklist, which 4.11 says it is not, or reading it aloud."
- statement: qaa/social-policy-2026/4.14.b4.masters
  forPractitioner: { text: "Design the master's course so that graduates can show knowledge of different research methods and the ability to design and carry out an independent, supervised dissertation or project.", rewrite: light, force: describes, status: drafted }
  forBeneficiary: { text: "By the end of your master's, you are expected to show knowledge of different research methods and the ability to design and carry out an independent, supervised dissertation or project.", rewrite: full, force: describes, status: drafted }
  author-agent-written: "Present this as an outcome expected of anyone completing a Social Policy master's degree, set at FHEQ Level 7 (FQHEIS Level 11): research methods and a supervised dissertation (repeated from 4.12); the issuer's word is 'expected', so state it without must or will. Cite it as (QAA, 2026, Social Policy Subject Benchmark Statement, para 4.14). Do not apply it to the honours degree, call it a regulatory requirement or grade it into typical or excellent, since the master's lists name no rungs. Set it beside qaa/fheq-2024/4.17.b6 and spine:7."
  author-agent-dialogue: "Raise this when a master's student is planning research or a dissertation. With a master's student, ask in plain second-person words how far they can already show it; with staff, frame it as what the master's course is expected to develop. Ask: \"Which research method would you defend as best for your question, and why?\" Avoid treating the list as a checklist, which 4.11 says it is not, or reading it aloud."
- statement: qaa/social-policy-2026/4.14.b5.masters
  forPractitioner: { text: "Design the master's course so that graduates can show the reflexive capacity to weigh feedback and use it to improve writing, argument and analysis.", rewrite: light, force: describes, status: drafted }
  forBeneficiary: { text: "By the end of your master's, you are expected to show the reflexive capacity to weigh feedback and use it to improve writing, argument and analysis.", rewrite: full, force: describes, status: drafted }
  author-agent-written: "Present this as an outcome expected of anyone completing a Social Policy master's degree, set at FHEQ Level 7 (FQHEIS Level 11): using feedback to improve; the issuer's word is 'expected', so state it without must or will. Cite it as (QAA, 2026, Social Policy Subject Benchmark Statement, para 4.14). Do not apply it to the honours degree, call it a regulatory requirement or grade it into typical or excellent, since the master's lists name no rungs. Set it beside qaa/fheq-2024/4.17.b8.3 and spine:7."
  author-agent-dialogue: "Raise this when a master's student is planning research or a dissertation. With a master's student, ask in plain second-person words how far they can already show it; with staff, frame it as what the master's course is expected to develop. Ask: \"What did your last feedback change in how you write?\" Avoid treating the list as a checklist, which 4.11 says it is not, or reading it aloud."
- statement: qaa/social-policy-2026/4.14.b6.masters
  forPractitioner: { text: "Design the master's course so that graduates can show expert scholarly practice, from finding relevant sources to academic referencing.", rewrite: light, force: describes, status: drafted }
  forBeneficiary: { text: "By the end of your master's, you are expected to show expert scholarly practice, from finding relevant sources to academic referencing.", rewrite: full, force: describes, status: drafted }
  author-agent-written: "Present this as an outcome expected of anyone completing a Social Policy master's degree, set at FHEQ Level 7 (FQHEIS Level 11): expert scholarly practice; the issuer's word is 'expected', so state it without must or will. Cite it as (QAA, 2026, Social Policy Subject Benchmark Statement, para 4.14). Do not apply it to the honours degree, call it a regulatory requirement or grade it into typical or excellent, since the master's lists name no rungs. Set it beside qaa/fheq-2024/4.17.b7 and spine:7."
  author-agent-dialogue: "Raise this when a master's student is planning research or a dissertation. With a master's student, ask in plain second-person words how far they can already show it; with staff, frame it as what the master's course is expected to develop. Ask: \"How do you find the most relevant sources for a new topic?\" Avoid treating the list as a checklist, which 4.11 says it is not, or reading it aloud."
- statement: qaa/social-policy-2026/4.15.b1.masters
  forPractitioner: { text: "Design the master's course so that graduates can show critical, reflexive and independent ways of learning.", rewrite: light, force: describes, status: drafted }
  forBeneficiary: { text: "By the end of your master's, you are expected to show critical, reflexive and independent ways of learning.", rewrite: full, force: describes, status: drafted }
  author-agent-written: "Present this as an outcome expected of anyone completing a Social Policy master's degree, set at FHEQ Level 7 (FQHEIS Level 11): critical, reflexive, independent learning; the issuer's word is 'expected', so state it without must or will. Cite it as (QAA, 2026, Social Policy Subject Benchmark Statement, para 4.15). Do not apply it to the honours degree, call it a regulatory requirement or grade it into typical or excellent, since the master's lists name no rungs. Set it beside qaa/fheq-2024/4.17.b8.3 and spine:7."
  author-agent-dialogue: "Raise this when a master's student reflects on skills for work and further learning. With a master's student, ask in plain second-person words how far they can already show it; with staff, frame it as what the master's course is expected to develop. Ask: \"How do you direct your own learning now?\" Avoid treating the list as a checklist, which 4.11 says it is not, or reading it aloud."
- statement: qaa/social-policy-2026/4.15.b2.masters
  forPractitioner: { text: "Design the master's course so that graduates can show commitment to public service and to adding social value for wellbeing, with a critical eye on both.", rewrite: light, force: describes, status: drafted }
  forBeneficiary: { text: "By the end of your master's, you are expected to show commitment to public service and to adding social value for wellbeing, with a critical eye on both.", rewrite: full, force: describes, status: drafted }
  author-agent-written: "Present this as an outcome expected of anyone completing a Social Policy master's degree, set at FHEQ Level 7 (FQHEIS Level 11): commitment to social value and public service; the issuer's word is 'expected', so state it without must or will. Cite it as (QAA, 2026, Social Policy Subject Benchmark Statement, para 4.15). Do not apply it to the honours degree, call it a regulatory requirement or grade it into typical or excellent, since the master's lists name no rungs. Set it beside qaa/fheq-2024/4.17.b8.1 and spine:7."
  author-agent-dialogue: "Raise this when a master's student reflects on skills for work and further learning. With a master's student, ask in plain second-person words how far they can already show it; with staff, frame it as what the master's course is expected to develop. Ask: \"What kind of public value do you want your work to create?\" Avoid treating the list as a checklist, which 4.11 says it is not, or reading it aloud."
- statement: qaa/social-policy-2026/4.15.b3.masters
  forPractitioner: { text: "Design the master's course so that graduates can show critically reflective awareness of what they still need to learn, for professional and personal growth.", rewrite: light, force: describes, status: drafted }
  forBeneficiary: { text: "By the end of your master's, you are expected to show critically reflective awareness of what you still need to learn, for professional and personal growth.", rewrite: full, force: describes, status: drafted }
  author-agent-written: "Present this as an outcome expected of anyone completing a Social Policy master's degree, set at FHEQ Level 7 (FQHEIS Level 11): naming learning needs for growth; the issuer's word is 'expected', so state it without must or will. Cite it as (QAA, 2026, Social Policy Subject Benchmark Statement, para 4.15). Do not apply it to the honours degree, call it a regulatory requirement or grade it into typical or excellent, since the master's lists name no rungs. Set it beside qaa/fheq-2024/4.17.b8.3 and spine:7."
  author-agent-dialogue: "Raise this when a master's student reflects on skills for work and further learning. With a master's student, ask in plain second-person words how far they can already show it; with staff, frame it as what the master's course is expected to develop. Ask: \"What do you still need to learn for the work you want to do?\" Avoid treating the list as a checklist, which 4.11 says it is not, or reading it aloud."
- statement: qaa/social-policy-2026/4.15.b4.masters
  forPractitioner: { text: "Design the master's course so that graduates can show the ability to evaluate and use ways of working productively in collaborative, multicultural and diverse settings at home and abroad.", rewrite: light, force: describes, status: drafted }
  forBeneficiary: { text: "By the end of your master's, you are expected to show the ability to evaluate and use ways of working productively in collaborative, multicultural and diverse settings at home and abroad.", rewrite: full, force: describes, status: drafted }
  author-agent-written: "Present this as an outcome expected of anyone completing a Social Policy master's degree, set at FHEQ Level 7 (FQHEIS Level 11): working well in diverse, multicultural settings; the issuer's word is 'expected', so state it without must or will. Cite it as (QAA, 2026, Social Policy Subject Benchmark Statement, para 4.15). Do not apply it to the honours degree, call it a regulatory requirement or grade it into typical or excellent, since the master's lists name no rungs. Set it beside qaa/fheq-2024/4.17.b8.2 and spine:7."
  author-agent-dialogue: "Raise this when a master's student reflects on skills for work and further learning. With a master's student, ask in plain second-person words how far they can already show it; with staff, frame it as what the master's course is expected to develop. Ask: \"How have you worked across cultures or in a diverse team?\" Avoid treating the list as a checklist, which 4.11 says it is not, or reading it aloud."
- statement: qaa/social-policy-2026/4.15.b5.masters
  forPractitioner: { text: "Design the master's course so that graduates can show familiarity with emerging technologies, generative AI among them, their strengths, limits and ethical questions in research and writing.", rewrite: light, force: describes, status: drafted }
  forBeneficiary: { text: "By the end of your master's, you are expected to show familiarity with emerging technologies, generative AI among them, your strengths, limits and ethical questions in research and writing.", rewrite: full, force: describes, status: drafted }
  author-agent-written: "Present this as an outcome expected of anyone completing a Social Policy master's degree, set at FHEQ Level 7 (FQHEIS Level 11): emerging technology and generative AI, ethically; the issuer's word is 'expected', so state it without must or will. Cite it as (QAA, 2026, Social Policy Subject Benchmark Statement, para 4.15). Do not apply it to the honours degree, call it a regulatory requirement or grade it into typical or excellent, since the master's lists name no rungs. Set it beside qaa/fheq-2024/4.17.b5 and spine:7."
  author-agent-dialogue: "Raise this when a master's student reflects on skills for work and further learning. With a master's student, ask in plain second-person words how far they can already show it; with staff, frame it as what the master's course is expected to develop. Ask: \"Where would you not use generative AI in your research, and why?\" Avoid treating the list as a checklist, which 4.11 says it is not, or reading it aloud."
```

### S5 Levels and alignment
<!-- label: both; status: drafted; basis: primary -->
```yaml
levels:
  - { id: "fheq:4", role: "cites", locator: "D1, 2.11 (Certificate of Higher Education)" }
  - { id: "fheq:5", role: "cites", locator: "D1, 2.11 (Diploma of Higher Education)" }
  - { id: "fheq:6", role: "cites", locator: "D1, 2.8; 4.1; 4.5; 4.6" }
  - { id: "fheq:7", role: "cites", locator: "D1, 2.8; 4.1" }
  - { id: "fqheis:8", role: "cites", locator: "D1, 2.11 (as the statement gives it for the CertHE: Part E)" }
  - { id: "fqheis:9", role: "cites", locator: "D1, 2.11 (DipHE, as stated: Part E); 2.12 (ordinary degree and MA)" }
  - { id: "fqheis:10", role: "cites", locator: "D1, 2.8; 2.12; 4.1" }
  - { id: "fqheis:11", role: "cites", locator: "D1, 2.8; 4.1" }
crosswalks:
  - { from: "fheq:6", to: "fqheis:10", relation: "equivalent", basis: "stated (D1, 2.8; 4.1: the honours degree at FHEQ Level 6 and FQHEIS Level 10); agrees with FHEQ Table 1" }
  - { from: "fheq:7", to: "fqheis:11", relation: "equivalent", basis: "stated (D1, 2.8; 4.1: integrated master's and master's at FHEQ Level 7 and FQHEIS Level 11); agrees with FHEQ 4.17" }
  - { from: "fheq:4", to: "fqheis:8", relation: "equivalent", basis: "stated (D1, 2.11: CertHE at FHEQ Level 4, FQHEIS Level 8); differs from FHEQ Table 1, which puts the CertHE at FQHEIS 7 (Part E)" }
  - { from: "fheq:5", to: "fqheis:9", relation: "equivalent", basis: "stated (D1, 2.11: DipHE at FHEQ Level 5, FQHEIS Level 9); differs from FHEQ Table 1, which puts the DipHE at FQHEIS 8 (Part E)" }
```

### S6 Themes
<!-- label: both; status: drafted; basis: primary -->
```yaml
- { id: "theme:edi", role: "carries", carriedIn: ["1.6", "1.13", "1.29", "1.30", "1.31", "1.32", "1.33", "1.34", "1.35", "1.36", "1.37", "1.38", "1.39", "1.41", "1.57", "3.9", "3.13", "4.13"] }
- { id: "theme:accessibility", role: "carries", carriedIn: ["1.40", "1.41", "1.42", "1.43", "1.57", "3.13"] }
- { id: "theme:esd", role: "carries", carriedIn: ["1.14", "1.44", "1.45", "1.46", "1.47", "1.48", "1.49", "1.50", "1.51", "1.52", "1.53", "2.3", "2.5", "3.3", "4.5", "4.7", "4.13"] }
- { id: "theme:enterprise", role: "carries", carriedIn: ["1.54", "1.55", "1.56", "1.57", "1.58", "1.59", "3.11"] }
- { id: "theme:generative-ai", role: "carries", carriedIn: ["1.60", "1.61", "1.62", "1.63", "1.64", "1.65", "1.66", "3.3", "3.12", "4.10", "4.15"] }
```

### S7 Relations
<!-- label: both; status: drafted; basis: primary -->
```yaml
- { rel: "partOf", target: "collection: QAA Subject Benchmark Statements", note: "one of 54 held by stan" }
- { rel: "supersedes", target: "std:doc:qaa-social-policy-2019-benchmarks (not ingested)", note: "the fourth edition, 2019 minor update; earlier editions 2016, 2007 (Social Policy and Administration) and 2000 (with Social Work), back matter" }
- { rel: "refersTo", target: "std:doc:qaa-fheq-2024-framework, Annex D", note: "the degree classification descriptions for bachelor's degrees with honours (4.3)" }
- { rel: "refersTo", target: "std:doc:qaa-fheq-2024-framework", note: "FHEQ Levels 4 to 7 (2.8, 2.11, 4.1, 4.5, 4.6)" }
- { rel: "refersTo", target: "std:doc:qaa-fqheis-2024-framework", note: "FQHEIS (SCQF) Levels 8 to 11 (2.8, 2.11, 2.12, 4.1)" }
- { rel: "refersTo", target: "std:doc:qaa-advancehe-esd-2021-guidance", note: "Education for Sustainable Development guidance (1.50)" }
- { rel: "refersTo", target: "std:doc:qaa-enterprise-2018-guidance", note: "Enterprise and Entrepreneurship Education guidance (1.54)" }
- { rel: "refersTo", target: "QAA Quality Code, 2024 update (not ingested)", note: "front matter" }
- { rel: "refersTo", target: "QAA Master's Degree Characteristics Statement (not ingested)", note: "4.11" }
- { rel: "refersTo", target: "Equality and Human Rights Commission guidance on competence standards (not ingested)", note: "4.4" }
- { rel: "overlaps", target: "std:doc:qaa-public-policy-and-public-administration-2025-benchmarks", note: "inferred: 2.6 names overlaps with Public Policy and Administration" }
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
- Examines policy and practice through the lens of human welfare: social need, social justice and how resources are divided and allocated (D1, 1.4 to 1.6).
- Both academic and applied: it explains social problems, analyses current interventions and argues for alternatives, bridging theory and practice (D1, 1.4).
- Separates the discipline (capitalised) from the practice of the state and other bodies in education, health, care, social security, pensions and housing (D1, 1.3).
- Studies welfare well beyond the state: commercial, voluntary and community sectors and families, in mixed economies of welfare (D1, 1.11, 1.12).
- Rooted in Social Administration and still attentive to how welfare institutions are governed and run (D1, 1.9; 2.6).
- Normative by nature: attends to values, ideology, social divisions and lived experience (D1, 1.6, 1.20, 1.38).
- Reckons with its colonial history and the global majority's understandings, while holding that it can never be fully decolonised (D1, 1.21 to 1.27).
- Works across local, devolved, national and international levels, including subsidiarity, and treats sustainability as central to welfare (D1, 1.7, 1.14).
- Taught in single and joint honours and as modules in wider social science degrees, beside Sociology, Politics, Criminology and Economics (D1, 1.2; 1.59).

### SB2 Themes in this subject
<!-- label: both; status: drafted; basis: primary -->
```yaml
- theme: theme:edi
  inThisSubject: "structural discrimination and intersecting disadvantage are subject matter; a strong decolonising strand runs through curriculum and analysis; diverse entrants, awarding gaps, co-construction and the statement's own definitions of equity, diversity and inclusion (D1, 1.13, 1.21 to 1.39); reflexive, inclusive practice is a graduate outcome (1.39) and EDI is a master's skill (4.13)"
  statements: ["qaa/social-policy-2026/1.27", "qaa/social-policy-2026/1.29", "qaa/social-policy-2026/1.31", "qaa/social-policy-2026/1.36", "qaa/social-policy-2026/1.39", "qaa/social-policy-2026/3.9", "qaa/social-policy-2026/3.3.b18", "qaa/social-policy-2026/4.13.b5.masters", "qaa/social-policy-2026/4.13.b6.masters"]
- theme: theme:accessibility
  inThisSubject: "anticipatory accessibility under equality law, four areas for inclusive courses, placement support for disabled students and accessible assessment principles (D1, 1.40 to 1.43, 3.13)"
  statements: ["qaa/social-policy-2026/1.42.b1", "qaa/social-policy-2026/1.42.b2", "qaa/social-policy-2026/1.42.b3", "qaa/social-policy-2026/1.42.b4", "qaa/social-policy-2026/1.43", "qaa/social-policy-2026/3.13.b6"]
- theme: theme:esd
  inThisSubject: "sustainability as central to welfare and as eco-social policy, the UN goals as a way in, the Inner Development Goals, and climate change deepening privilege (D1, 1.14, 1.44 to 1.53); the UN goals form a full row of the knowledge table (4.7) and a master's skill (4.13)"
  statements: ["qaa/social-policy-2026/1.14", "qaa/social-policy-2026/1.48", "qaa/social-policy-2026/1.50", "qaa/social-policy-2026/1.52", "qaa/social-policy-2026/1.53", "qaa/social-policy-2026/3.3.b7", "qaa/social-policy-2026/3.3.b20", "qaa/social-policy-2026/4.5.b3", "qaa/social-policy-2026/4.7.b1.typical", "qaa/social-policy-2026/4.7.b4", "qaa/social-policy-2026/4.7.b4.typical", "qaa/social-policy-2026/4.7.b4.excellent", "qaa/social-policy-2026/4.13.b6.masters"]
- theme: theme:enterprise
  inThisSubject: "problem solving, creative thinking and real-world experience through placements, volunteering and authentic assessment, with careers in the public, voluntary and private sectors (D1, 1.54 to 1.59, 3.11)"
  statements: ["qaa/social-policy-2026/1.56", "qaa/social-policy-2026/4.5.b2"]
- theme: theme:generative-ai
  inThisSubject: "critical, ethical and reflective use of generative AI, its gains and risks (including colonial bias and environmental cost), institutional policy and its place in assessment (D1, 1.60 to 1.66, 3.12); AI is a knowledge area (3.3) and part of the technology skill row (4.10) and a master's skill (4.15)"
  statements: ["qaa/social-policy-2026/1.60", "qaa/social-policy-2026/1.62.b5", "qaa/social-policy-2026/1.65", "qaa/social-policy-2026/3.12", "qaa/social-policy-2026/3.3.b19", "qaa/social-policy-2026/4.10.b4", "qaa/social-policy-2026/4.10.b4.typical", "qaa/social-policy-2026/4.10.b4.excellent", "qaa/social-policy-2026/4.15.b5.masters"]
```

### SB3 Content and delivery
<!-- label: both; status: drafted; basis: primary -->
```yaml
areas:
  - { component: "3.2", gloss: "policy at local, national, international and global scale; fields from criminal justice to work and labour markets" }
  - { component: "3.3", gloss: "five groups of knowledge: welfare systems, policy processes, impacts, concepts and theories, research and policy analysis" }
practices:
  - { component: "3.4", kind: "teaching", gloss: "lectures, seminars and workshops; placements, visits, volunteering, exchanges and life experience" }
  - { component: "3.5", kind: "teaching", gloss: "virtual learning, data software, distance and blended learning, MOOCs" }
  - { component: "3.6", kind: "learning", gloss: "a portfolio of experience that prepares for work" }
  - { component: "3.7", kind: "learning", gloss: "scheduled, peer, virtual, self-directed and experiential learning" }
  - { component: "3.8", kind: "learning", gloss: "critical reading, independent research, group work, contact with practitioners and users" }
  - { component: "3.10", kind: "assessment", gloss: "constructive alignment; assessment that reflects progression" }
  - { component: "3.11", kind: "assessment", gloss: "authentic assessment recommended" }
  - { component: "3.13", kind: "assessment", gloss: "accessible, inclusive principles, in ought to" }
  - { component: "3.14", kind: "assessment", gloss: "indicative types, from essays and exams to policy briefings and podcasts" }
  - { component: "3.15", kind: "assessment", gloss: "diversity monitored at programme level" }
  - { component: "3.16", kind: "assessment", gloss: "constructive feedback in many forms" }
```

### SB4 Benchmark standards
<!-- label: both; status: drafted; basis: primary -->
```yaml
rungs:
  - { rung: "threshold", leadIn: "4.7 to 4.10 (rungs defined in 4.2)", award: "bachelor's with honours", items: 18 }
  - { rung: "typical", leadIn: "4.7 to 4.10 (rungs defined in 4.2)", award: "bachelor's with honours", items: 18 }
  - { rung: "excellent", leadIn: "4.7 to 4.10 (rungs defined in 4.2)", award: "bachelor's with honours", items: 19 }
  - { rung: "threshold", leadIn: "4.12 to 4.15 (master's lists; no rung named)", award: "master's", items: 25 }
rungBases: "4.2: threshold is the minimally acceptable requirement for a third-class honours degree; typical the required attainment for a second-class degree; excellent the required attainment for a first. 4.6: the honours rungs are successive and cumulative. The four master's lists (4.12 to 4.15) name no rung and are recorded as threshold for the master's award by the batch 1 convention (Part E)"
outcomeLists:
  - { leadIn: "3.3", gloss: "knowledge areas graduates demonstrate, in five groups (plain present; force describes)", items: 33, award: ["honours"] }
  - { leadIn: "4.5", gloss: "honours outcomes in line with the Frameworks (expected to; force describes)", items: 4, award: ["honours"] }
outcomes:
  - { outcome: "knowledge of policies and their effects", threshold: "qaa/social-policy-2026/4.7.b1", typical: "qaa/social-policy-2026/4.7.b1.typical", excellent: "qaa/social-policy-2026/4.7.b1.excellent", basis: "stated", domain: "knowledge", award: "bachelor's with honours" }
  - { outcome: "comparing welfare systems", threshold: "qaa/social-policy-2026/4.7.b2", typical: "qaa/social-policy-2026/4.7.b2.typical", excellent: "qaa/social-policy-2026/4.7.b2.excellent", basis: "stated", domain: "understanding", award: "bachelor's with honours" }
  - { outcome: "core theories and concepts", threshold: "qaa/social-policy-2026/4.7.b3", typical: "qaa/social-policy-2026/4.7.b3.typical", excellent: "qaa/social-policy-2026/4.7.b3.excellent", basis: "stated", domain: "understanding", award: "bachelor's with honours" }
  - { outcome: "sustainable development and the UN goals", threshold: "qaa/social-policy-2026/4.7.b4", typical: "qaa/social-policy-2026/4.7.b4.typical", excellent: "qaa/social-policy-2026/4.7.b4.excellent", basis: "stated", domain: "knowledge", award: "bachelor's with honours" }
  - { outcome: "analysing social problems", threshold: "qaa/social-policy-2026/4.8.b1", typical: "qaa/social-policy-2026/4.8.b1.typical", excellent: "qaa/social-policy-2026/4.8.b1.excellent", basis: "stated", domain: "subject-skill", award: "bachelor's with honours" }
  - { outcome: "using theory", threshold: "qaa/social-policy-2026/4.8.b2", typical: "qaa/social-policy-2026/4.8.b2.typical", excellent: "qaa/social-policy-2026/4.8.b2.excellent", basis: "stated", domain: "subject-skill", award: "bachelor's with honours" }
  - { outcome: "values and ideology in policy", threshold: "qaa/social-policy-2026/4.8.b3", typical: "qaa/social-policy-2026/4.8.b3.typical", excellent: "qaa/social-policy-2026/4.8.b3.excellent", basis: "stated", domain: "subject-skill", award: "bachelor's with honours" }
  - { outcome: "human need and lived experience", threshold: "qaa/social-policy-2026/4.8.b4", typical: "qaa/social-policy-2026/4.8.b4.typical", excellent: "qaa/social-policy-2026/4.8.b4.excellent", basis: "stated", domain: "subject-skill", award: "bachelor's with honours" }
  - { outcome: "research", threshold: "qaa/social-policy-2026/4.8.b5", typical: "qaa/social-policy-2026/4.8.b5.typical", excellent: "qaa/social-policy-2026/4.8.b5.excellent", basis: "stated", domain: "subject-skill", award: "bachelor's with honours" }
  - { outcome: "reasoning and argument", threshold: "qaa/social-policy-2026/4.9.b1", typical: "qaa/social-policy-2026/4.9.b1.typical", excellent: "qaa/social-policy-2026/4.9.b1.excellent", basis: "stated", domain: "generic-skill", award: "bachelor's with honours" }
  - { outcome: "analysing material", threshold: "qaa/social-policy-2026/4.9.b2", typical: "qaa/social-policy-2026/4.9.b2.typical", excellent: "qaa/social-policy-2026/4.9.b2.excellent", basis: "stated", domain: "generic-skill", award: "bachelor's with honours" }
  - { outcome: "problem-solving", threshold: "qaa/social-policy-2026/4.9.b3", typical: "qaa/social-policy-2026/4.9.b3.typical", excellent: "qaa/social-policy-2026/4.9.b3.excellent", basis: "stated", domain: "generic-skill", award: "bachelor's with honours" }
  - { outcome: "research projects", threshold: "qaa/social-policy-2026/4.9.b4", typical: "qaa/social-policy-2026/4.9.b4.typical", excellent: "qaa/social-policy-2026/4.9.b4.excellent", basis: "stated", domain: "generic-skill", award: "bachelor's with honours" }
  - { outcome: "synthesis", threshold: "none", typical: "none", excellent: "qaa/social-policy-2026/4.9.b5.excellent", basis: "stated", domain: "generic-skill", award: "bachelor's with honours" }
  - { outcome: "communication", threshold: "qaa/social-policy-2026/4.10.b1", typical: "qaa/social-policy-2026/4.10.b1.typical", excellent: "qaa/social-policy-2026/4.10.b1.excellent", basis: "stated", domain: "generic-skill", award: "bachelor's with honours" }
  - { outcome: "self-directed learning", threshold: "qaa/social-policy-2026/4.10.b2", typical: "qaa/social-policy-2026/4.10.b2.typical", excellent: "qaa/social-policy-2026/4.10.b2.excellent", basis: "stated", domain: "generic-skill", award: "bachelor's with honours" }
  - { outcome: "teamwork", threshold: "qaa/social-policy-2026/4.10.b3", typical: "qaa/social-policy-2026/4.10.b3.typical", excellent: "qaa/social-policy-2026/4.10.b3.excellent", basis: "stated", domain: "generic-skill", award: "bachelor's with honours" }
  - { outcome: "technology", threshold: "qaa/social-policy-2026/4.10.b4", typical: "qaa/social-policy-2026/4.10.b4.typical", excellent: "qaa/social-policy-2026/4.10.b4.excellent", basis: "stated", domain: "generic-skill", award: "bachelor's with honours" }
  - { outcome: "evidence and referencing", threshold: "qaa/social-policy-2026/4.10.b5", typical: "qaa/social-policy-2026/4.10.b5.typical", excellent: "qaa/social-policy-2026/4.10.b5.excellent", basis: "stated", domain: "generic-skill", award: "bachelor's with honours" }
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
- { body: "Professional, statutory and regulatory bodies (PSRBs), none named", says: "statements can support PSRBs in defining academic standards; providers may weigh PSRB requirements; courses with professional outcomes may need accreditation; competence standards may draw on PSRB requirements (D1, front matter; 2.18; 4.4)", requirements: "not yet ingested (Part E)" }
- { body: "Equality and Human Rights Commission", says: "providers developing competence standards should follow its most recent guidance (D1, 4.4)", requirements: "not yet ingested (Part E)" }
- { body: "Office for Students", says: "in England benchmark statements are not sector-recognised standards under its regulatory framework (D1, front matter)", requirements: "not-applicable-by-design: named for status only (Part E)" }
- { body: "Disabled Students Commission", says: "its website is the pointer for more on accessibility (D1, 1.40)", requirements: "not-applicable-by-design: named as a resource (Part E)" }
- { body: "Advance HE", says: "co-author with QAA of the Education for Sustainable Development guidance programmes can draw on (D1, 1.50)", requirements: "std:doc:qaa-advancehe-esd-2021-guidance" }
```

### SB6 Cross-cutting references
<!-- label: both; status: drafted; basis: primary -->
```yaml
themes:
  - { id: "theme:edi", named: "Equity, diversity and inclusion", carriedIn: ["1.6", "1.13", "1.29", "1.30", "1.31", "1.32", "1.33", "1.34", "1.35", "1.36", "1.37", "1.38", "1.39", "1.41", "1.57", "3.9", "3.13", "4.13"], statements: ["1.27", "1.29", "1.31", "1.36", "1.39", "3.9", "3.3.b18", "4.13.b5.masters", "4.13.b6.masters"] }
  - { id: "theme:accessibility", named: "Accessibility and the needs of disabled students", carriedIn: ["1.40", "1.41", "1.42", "1.43", "1.57", "3.13"], statements: ["1.42.b1", "1.42.b2", "1.42.b3", "1.42.b4", "1.43", "3.13.b6"] }
  - { id: "theme:esd", named: "Education for sustainable development", carriedIn: ["1.14", "1.44", "1.45", "1.46", "1.47", "1.48", "1.49", "1.50", "1.51", "1.52", "1.53", "2.3", "2.5", "3.3", "4.5", "4.7", "4.13"], statements: ["1.14", "1.48", "1.50", "1.52", "1.53", "3.3.b7", "3.3.b20", "4.5.b3", "4.7.b1.typical", "4.7.b4", "4.7.b4.typical", "4.7.b4.excellent", "4.13.b6.masters"] }
  - { id: "theme:enterprise", named: "Employability, entrepreneurship and enterprise education", carriedIn: ["1.54", "1.55", "1.56", "1.57", "1.58", "1.59", "3.11"], statements: ["1.56", "4.5.b2"] }
  - { id: "theme:generative-ai", named: "Generative artificial intelligence", carriedIn: ["1.60", "1.61", "1.62", "1.63", "1.64", "1.65", "1.66", "3.3", "3.12", "4.10", "4.15"], statements: ["1.60", "1.62.b5", "1.65", "3.12", "3.3.b19", "4.10.b4", "4.10.b4.typical", "4.10.b4.excellent", "4.15.b5.masters"] }
frameworks:
  - { framework: "fheq", levels: ["fheq:4", "fheq:5", "fheq:6", "fheq:7"], citedIn: ["2.8", "2.11", "4.1", "4.3", "4.5", "4.6"] }
  - { framework: "scqf", levels: ["fqheis:8", "fqheis:9", "fqheis:10", "fqheis:11"], citedIn: ["2.8", "2.11", "2.12", "4.1"] }
bodies:
  - { body: "PSRBs (none named)", citedIn: ["front matter", "2.18", "4.4"] }
  - { body: "Equality and Human Rights Commission", citedIn: ["4.4"] }
  - { body: "Office for Students", citedIn: ["front matter"] }
  - { body: "Disabled Students Commission", citedIn: ["1.40"] }
  - { body: "Advance HE", citedIn: ["1.50"] }
sharedDocuments:
  - { document: "std:doc:qaa-fheq-2024-framework, Annex D", named: "Annex D in The Frameworks for Higher Education Qualifications of UK Degree-Awarding Bodies", citedIn: ["4.3"], role: "descriptions of the four honours classes (1st, 2.1, 2.2, 3rd) for evidence above typical" }
  - { document: "std:doc:qaa-fheq-2024-framework", named: "the Frameworks for Higher Education Qualifications of UK Degree Awarding Bodies", citedIn: ["4.5"], role: "the four honours outcomes of 4.5 are set in line with it" }
  - { document: "std:doc:qaa-advancehe-esd-2021-guidance", named: "the QAA and Advance HE Education for Sustainable Development", citedIn: ["1.50"], role: "a resource for curriculum design" }
  - { document: "std:doc:qaa-enterprise-2018-guidance", named: "Enterprise and Entrepreneurship Education: Guidance for UK Higher Education Providers", citedIn: ["1.54"], role: "further guidance on EEE" }
  - { document: "QAA Quality Code, 2024 update (not yet ingested)", named: "an update to the Quality Code", citedIn: ["front matter"], role: "a further reference point" }
  - { document: "QAA Glossary (not ingested)", named: "QAA's Glossary", citedIn: ["front matter"], role: "explains unfamiliar terms" }
  - { document: "QAA Creating Inclusive Subject Communities (not ingested)", named: "the QAA resource on Creating Inclusive Subject Communities", citedIn: ["1.36"], role: "an example of good EDI practice" }
  - { document: "QAA Generative artificial intelligence resources (not ingested)", named: "Generative artificial intelligence", citedIn: ["1.66"], role: "further guidance on GenAI" }
  - { document: "QAA Master's Degree Characteristics Statement (not ingested)", named: "The Master's Degree Characteristics Statement", citedIn: ["4.11"], role: "named in the lead-in to the master's standards" }
  - { document: "UN Sustainable Development Goals (external)", named: "The UN Sustainable Development Goals (UN SDGs)", citedIn: ["1.45", "1.46", "1.47", "4.7"], role: "the frame of the sustainability theme and a row of the knowledge table" }
  - { document: "Inner Development Goals (external)", named: "the Inner Development Goals", citedIn: ["1.50"], role: "personal skills for sustainable development" }
  - { document: "Equality Act 2010 (law)", named: "Equality Act 2010", citedIn: ["1.31", "1.40", "4.4"], role: "protected characteristics, accessibility duties, competence standards" }
  - { document: "Disability Discrimination Act 1995 and SEND (Northern Ireland) Order 2005 (law, Northern Ireland)", named: "Disability Discrimination Act 1995 and Special Educational Needs and Disability (Northern Ireland) Order 2005", citedIn: ["1.40"], role: "accessibility duties in Northern Ireland" }
```

## Part B Terminology
<!-- The statement has no glossary of its own unless Part E says so; these are terms it defines in its text. -->

### B1 Concepts
<!-- label: both; status: drafted; basis: primary -->
```yaml
- { slug: "social-policy-discipline", definition: "the capitalised name for the academic discipline, set against lower-case social policy, the practice of the state and other bodies in welfare fields (D1, 1.3)", beneficiaryDefinition: "the subject you study, as distinct from the policies it studies", scopeNote: "the statement's own convention", category: "unknown", practices: ["education"] }
- { slug: "equity", definition: "giving each person the particular resources and chances they need to reach an equal outcome (D1, 1.35)", beneficiaryDefinition: "getting what you in particular need to reach the same outcome as others", scopeNote: "one of the three EDI terms the statement defines", category: "unknown", practices: ["education"] }
- { slug: "diversity", definition: "recognising and valuing students' differing backgrounds and outlooks (D1, 1.35)", beneficiaryDefinition: "your background and outlook being recognised and valued", scopeNote: "one of the three EDI terms", category: "unknown", practices: ["education"] }
- { slug: "inclusion", definition: "an environment that respects the dignity and humanity of everyone (D1, 1.35)", beneficiaryDefinition: "a setting where your dignity is respected", scopeNote: "one of the three EDI terms", category: "unknown", practices: ["education"] }
- { slug: "polycrisis", definition: "several crises at once, each worsening the others (D1, 1.10, footnote 1)", beneficiaryDefinition: "several crises happening together and feeding each other", scopeNote: "used in the plural", category: "unknown", practices: ["education"] }
- { slug: "subsidiarity", definition: "meeting social needs at the closest level of government able to do so (D1, 1.7)", beneficiaryDefinition: "dealing with problems at the most local level that can handle them", scopeNote: "named as a principle students should understand", category: "unknown", practices: ["education"] }
- { slug: "authentic-assessment", definition: "assessment that mirrors real-world scenarios as closely as an academic setting allows (D1, 1.56; 3.11)", beneficiaryDefinition: "assessment that copies real work tasks", scopeNote: "recommended in 3.11", category: "unknown", practices: ["education"] }
- { slug: "threshold-standard", definition: "the least a student must reach to gain a third-class honours degree (D1, 4.2)", beneficiaryDefinition: "the least you need to show to gain honours", scopeNote: "first column of the 4.7 to 4.10 tables", category: "unknown", practices: ["education"] }
- { slug: "typical-standard", definition: "the attainment required for a second-class honours degree (D1, 4.2)", beneficiaryDefinition: "what a second-class degree asks of you", scopeNote: "second column", category: "unknown", practices: ["education"] }
- { slug: "excellent-standard", definition: "the attainment required for a first-class honours degree (D1, 4.2)", beneficiaryDefinition: "what a first-class degree asks of you", scopeNote: "third column; cumulative on the other two (4.6)", category: "unknown", practices: ["education"] }
```

### B2a Terms as the issuer defines them
<!-- label: source; status: drafted; basis: primary -->
```yaml
- { concept: "social-policy-discipline", form: "Social Policy", lang: "en", partOfSpeech: "noun-phrase", termStatus: "preferred", register: "discipline-specific" }
- { concept: "equity", form: "equity", lang: "en", partOfSpeech: "noun", termStatus: "preferred", register: "formal" }
- { concept: "diversity", form: "diversity", lang: "en", partOfSpeech: "noun", termStatus: "preferred", register: "formal" }
- { concept: "inclusion", form: "inclusion", lang: "en", partOfSpeech: "noun", termStatus: "preferred", register: "formal" }
- { concept: "polycrisis", form: "polycrises", lang: "en", partOfSpeech: "noun", termStatus: "preferred", register: "discipline-specific" }
- { concept: "subsidiarity", form: "subsidiarity", lang: "en", partOfSpeech: "noun", termStatus: "preferred", register: "discipline-specific" }
- { concept: "authentic-assessment", form: "authentic assessment", lang: "en", partOfSpeech: "noun-phrase", termStatus: "preferred", register: "formal" }
- { concept: "threshold-standard", form: "threshold standard", lang: "en", partOfSpeech: "noun-phrase", termStatus: "preferred", register: "formal" }
- { concept: "typical-standard", form: "typical standard", lang: "en", partOfSpeech: "noun-phrase", termStatus: "preferred", register: "formal" }
- { concept: "excellent-standard", form: "excellent standard", lang: "en", partOfSpeech: "noun-phrase", termStatus: "preferred", register: "formal" }
```

### B2b Associated vocabulary
`not-applicable-by-design`: the statement names no wider vocabulary.

### B3 Framework blocks
`not-applicable-by-design`: no term is defined its own way for one component.

### B4 Relations
<!-- label: both; status: drafted; basis: primary -->
```yaml
- { rel: "contrasts-with", from: "threshold-standard", to: "typical-standard", note: "4.2: the first two rungs" }
- { rel: "contrasts-with", from: "typical-standard", to: "excellent-standard", note: "4.2 and 4.6: the excellent rung incorporates and extends the others" }
```

## Part C Process
<!-- label: both; status: drafted; basis: primary -->

### C0 Formality
`not-applicable`: the statement sets out what graduates achieve and what courses provide, not a procedure.

## Part D Sources
```yaml
- key: D1
  issuer: The Quality Assurance Agency for Higher Education
  title: "Subject Benchmark Statement: Social Policy"
  edition: "April 2026 (fifth edition)"
  year: 2026
  url: unknown (the QAA page; the text came by stan's extraction)
  retrieved: "held from stan: wkspc2615-QAAVector mapped/social-policy-2026/social-policy-2026.raw.txt, commit 366bcb99a01118f2c4c3ebfa2a8337596bddc455; received 2026-10-03"
  licence: QAA copyright
  tier: primary
  readVia: direct
  held: 94056f12b97c3fb116313a2f0780a4027e668e36a07d2847c6745e6ee453c8c3
  heldFiles: ["wkspc2601-library/txt/qaa-2026-social-policy-subject-benchmark-statement-standard.txt", "wkspc2601-library/txt/qaa-2026-social-policy-subject-benchmark-statement-standard.norm.txt", "wkspc2601-library/records/qaa-2026-social-policy-subject-benchmark-statement-standard.chunks.json", "wkspc2601-library/records/qaa-2026-social-policy-subject-benchmark-statement-standard.held.json"]
  citedIn: [S1, S2, S3, S4, S4a, S5, S6, S7, SB1, SB2, SB3, SB4, SB5, SB6]
```

### D2 Research log
```yaml
- { ref: D1, tier: primary, consulted: 2026-10-03, pass: P1, outcome: "read whole, direct, from the normalised text; skeleton by tools/std_prep.py, document by tools/bm_build.py" }
- { ref: "ADAPT subj HESA stores, cah.json and hecos.json (designs/ingest/standards/subj/vocab)", tier: primary, consulted: 2026-10-03, pass: P1, outcome: "codes for statedSubjects and subjects" }
```

### D3 Wanted sources
```yaml
- { w: "W-std-0096", citation: "QAA (2019) Subject Benchmark Statement: Social Policy, fourth edition (minor update)", settles: ["S7"], asked: "2026-10-03", state: "wanted" }
- { w: "W-std-0026", citation: "QAA Master's Degree Characteristics Statement (current edition)", settles: ["SB6", "S7"], asked: "2026-10-03", state: "wanted" }
```

## Part E Gaps and questions
- SB4, pattern (differs from Psychology): one three-column table per block (knowledge and understanding 4.7, subject-specific skills 4.8, generic intellectual skills 4.9, generic transferable skills 4.10), each outcome a row with threshold (3rd class), typical (2nd class) and excellent (1st class) cells. Recorded one record per cell, ids `<n>.b<k>`, `.typical`, `.excellent`, `gradeOf` stated by row (batch 1 convention).
- SB4, flattened tables (P3): every table is flattened in the held text, cells running threshold, typical, excellent, row by row, with paragraph breaks falling at irregular points. Placement read from that order and the progression of verbs. Least sure: 4.7 row 1, where the typical cell (in-depth knowledge with sustainability and the UN goals) is not a plain step up from the threshold cell; 4.8 row 3, where the excellent cell ("understand the relevance of and apply") reads weaker than the typical cell ("distinguish ... and critically reflect"), so the two may be swapped; 4.8 row 5, where the threshold cell already asks students to undertake research.
- SB4, 4.9 orphan cell (P3): after the research row the held text has one more cell, "Synthesis skills", with no partners. Recorded as an excellent cell on its own row (4.9.b5.excellent, gradeOf none), as its wording reads as first-class work; it may instead belong to the typical column, or the research row may run threshold "data collection with supervisory support", typical "independent research", excellent "synthesis", with the second data collection cell misplaced. Rung counts: threshold 18, typical 18, excellent 19.
- S4, force of the table cells: the lead-ins (4.7 to 4.10) say "are expected to possess", outside the five. Threshold cells are `threshold` (4.2 defines the rung as the minimum for a third; forceFrom 4.2). Typical and excellent cells are `must`, from 4.2's "describes the required attainment" (the batch 1 convention reads "required" as must; forceFrom 4.2). For Abbott: is "required attainment" for a class must, or should these read as will?
- SB4, master's (P3): four lists (4.12 knowledge and understanding, 4.13 subject-specific skills, 4.14 generic intellectual skills, 4.15 generic transferable skills), 25 items, no rung named. Recorded as rung threshold, award master's, level fheq:7, ids `.masters`, by the batch 1 convention; force `describes`, since the lead-ins say "are expected to possess" or "are expected to demonstrate", outside the five, with no stated minimum.
- S4, master's lead-ins (issuer slips): 4.12 calls its list "generic transferable skills" though its heading (the 4.7-style block) and content are knowledge and understanding; 4.14 calls its list "generic transferable skills" under the heading "Generic intellectual skills". Domains set by heading and content: 4.12 knowledge or understanding (4.12.b6 subject-skill), 4.13 subject-skill, 4.14 and 4.15 generic-skill. 4.11 names a "Master's Degree Characteristics Statement" as setting out the characteristics; read as the 4.12 to 4.15 lists that follow (D3).
- S4, repeated item: 4.12.b6 and 4.14.b4 have identical text (research methods and a supervised dissertation). Both kept as records, each on its own span (4.14.b4 found after its lead-in); for P3 whether one is a duplication slip.
- S4, 3.3 (33 items): "Graduates of Social Policy courses in the UK demonstrate knowledge in the following areas", plain present with no modal, in five groups with run-in headings. Recorded as an outcome list, force `describes`, domain knowledge, honours (fheq:6), as earlier runs did for plain-present graduate lists (open point 5). 3.1 says it may be inappropriate to be prescriptive about knowledge. Items 3.3.b8, b14, b21, b26 and b33 cut by `find` to drop the run-in group headings the skeleton attached. 3.3.b12 holds its own "should" (embedding reflective practice); recorded with the list's describes. Verbs left empty where an item is a noun phrase with no verb of its own.
- S4, 4.5 (4 items): "In line with the Frameworks ..., Social Policy graduates are expected to:", honours outcomes outside the rungs. Recorded as an outcome list, force `describes` ("expected to"), rung none. Their content tracks the FHEQ honours descriptor (qaa/fheq-2024/4.15).
- S4, statements taken from prose (in should unless named): 1.7, 1.14 (must), 1.17 (must), 1.20, 1.24 (must, with a should), 1.27, 1.29, 1.31, 1.36, 1.39 (will), 1.42.b1 to b4 (lead-in should), 1.43, 1.48, 1.50, 1.52, 1.53, 1.56, 1.60, 1.62.b5, 1.65, 2.1, 2.2.b1 to b5, 2.3.b1 to b4, 2.4.b1 to b3, 2.5, 2.6, 2.7, 2.8 (will), 2.10 (will), 2.15 (will), 2.16 (will), 3.4 (requires, must), 3.9, 3.12 (must), 3.13.b6, 3.17, 4.3, 4.4. Provider duties carry no student version. Several are cut to their obliging sentence by `find`.
- S4, 1.14: "Social policy must recognise ..." is lower case, which by 1.3 means the practice, not the discipline; read as a requirement on the discipline and its curricula, since the paragraph is about what the discipline embeds and what graduates can do. For P3.
- S4, 1.65: "Social Policy degrees programmes will have to adhere to" institutional GenAI policy (must-like, outside the five) and "students should be taught" in one paragraph; one record at should.
- S4, 2.1: the issuer says "four fundamental questions" and lists six (what, how, why, whether, to whom, by whom). Kept as written.
- S4, obliging words outside the five, not taken as statements, for Abbott: 1.32 "This will require programme designs ..." (a consequence of a plain-present aim); 1.51 "it is important that programmes seek to integrate"; 1.57 "need to ensure they are accessible"; 1.62.b4 "students need to be able to critique" (inside a list of risks); 2.9 "It is expected that a student ... would be capable"; 3.1 "ought to remain responsive"; 3.11 "Authentic assessments are recommended"; 3.13 "ought to be accessible and inclusive" (six of its seven principles; the seventh, b6, has its own should and is taken); 3.15 "ought to be evaluated and monitored"; 3.16 "an appreciation ... is expected and discussed". For Abbott: should "ought to" read as should?
- S4, plain-present provider norms, not statements (template open point 5): 1.32, 1.33, 1.34, 1.37, 1.38, 1.40 (teaching teams take a proactive approach), 1.41, 1.63 (developers consider carefully), 1.64, 2.13, 2.14, 3.2 (students acquiring insights), 3.4 to 3.8 (methods), 3.10, 3.14, 3.16.
- S4, predictive or permissive words not taken: 1.29 "will likely mean"; 1.49 "will likely be working"; 1.57 "programmes will likely offer"; 2.6 "will have several overlaps"; 2.11 "may exit earlier and be eligible" (exit awards); 2.17 "external examiners will be asked"; 2.18 "may also require evaluation and accreditation".
- S4, 4.2 defines the rungs ("must attain" for the threshold) and is recorded in SB4 rungBases, not as a statement; 4.6 says the standards are "not a checklist" and the rungs cumulative.
- S4, section 1 to 3 learner statements are recorded at honours (fheq:6), the statement's main award; several (1.7, 1.17, 1.20, 2.1, 2.3, 2.4) are worded for the subject at any level and may also hold for the master's. For P3.
- S5, levels (doubt for P3): 2.11 places the CertHE at FQHEIS Level 8 and the DipHE at FQHEIS Level 9. The FHEQ document (Table 1) places them at SCQF 7 and 8. Recorded as stated with the difference noted in S5; the issuer's text may be in error (the same slip as the History of Art, Architecture and Design statement, run 0111).
- S5, generic skills: every generic-skill record carries fheq:6 (honours) or fheq:7 (master's), both in S5; the framework descriptors each instruction sets them beside are qaa/fheq-2024/4.15 and 4.17 and the Annex D cells (std:doc:qaa-fheq-2024-framework); these pairings are inferred, ours.
- SB6: five cross-cutting themes, named in the front matter and each with its own heading in section 1. GenAI uses theme:generative-ai. Decolonisation is a strong strand (1.21 to 1.27, 2.5, 4.13.b6) with no shared theme id; recorded under theme:edi here. For Abbott: a theme:decolonisation id?
- SB6: CQFW is not cited. The Social Policy Association appears only in the references and the advisory group history (excluded matter), and the Joint University Council only in the back matter; neither is in SB5.
- SB5: the PSRBs are named only as a class; no requirements document can be linked. The EHRC's guidance is not yet ingested. The Office for Students is named for status only; the Disabled Students Commission as a resource. Advance HE links to the ingested ESD guidance.
- S2, subjects: HECoS 100502 and CAH15-01-03 (social policy) taken as stated: the title names the subject and both codes carry that label. Other codes in statedSubjects are for degrees in which the subject is taught (1.2, 1.59) or neighbouring fields (1.9, 2.6), not the benchmark's own scope. International social policy (100645) and welfare policy (100649) sit in the same CAH group and are not named.
- S7: the previous edition (2019, fourth edition, minor update) is named in the back matter; earlier advisory groups 2016, 2007 (Social Policy and Administration) and 2000 (Social Policy and Administration and Social Work). Not ingested (D3). The overlap with Public Policy and Public Administration (2.6) is an inferred relation.
- S1, licence: the text gives a copyright notice and no re-use terms.
- S9: not researched in P1.
- Pattern (differs from Psychology): rungs in flattened three-column tables tied explicitly to degree classes (4.2), with an orphan cell; typical and excellent defined as 'required attainment' (must); a 33-item plain-present knowledge list; four master's lists with no rungs; five theme sections before the distinctive features, as in the 2026 revision; a strong decolonising strand; no subject body named outside the back matter.
- ST-12: versions here run to the lengths the content needs; no length range is yet set.

---

## Change notes
- 0.1.2, 3 October 2026, 21:02: moved with its held text from UNI to the source library repo (`wkspc2601-library/ingested/standards/`, texts in `txt/`, records in `records/`); paths only (Abbott, 20:56; std N-0119).
- 0.1.1, 3 October 2026, 20:20: obliging words outside the five read as must, "ought to" as should, on statements outside the rungs, each marked on its force line (Abbott, 20:17; D-std-0016).
- 0.1.0, 2026-10-03 18:29: researched by run frame 0.1.1-draft and standards run layer 0.7.0-draft, std, run 0129 (P1); built by tools/bm_build.py.
