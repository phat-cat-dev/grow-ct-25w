---
id: std:doc:qaa-sociology-2026-benchmarks
title: "Subject Benchmark Statement: Sociology"
profile: standards/subject-benchmark
profileVersion: 0.2.0-draft
issuer: QAA
kind: subject-benchmark
jurisdiction: [UK]
subjectScope: subjects
subjects:
  - { scheme: "hecos", code: "100505", label: "sociology", basis: "stated" }
  - { scheme: "cah", code: "CAH15-01-02", label: "sociology", basis: "stated" }
  - { scheme: "cah", code: "CAH15-01", label: "sociology, social policy and anthropology", basis: "inferred" }
  - { scheme: "cah", code: "CAH15", label: "social sciences", basis: "stated" }
edition: "April 2026 (fifth edition)"
published: 2026-04
status: current
supersedes: "Subject Benchmark Statement: Sociology, fourth edition (2019, minor update), as the back matter names it"
heldText: { method: sha256-bytes, raw: 77725c932f691e154481d14f48fd597208986236aec92bd6dfd1314bd9ef1147, normalised: 27c8e20501cfc6545001286dc515afb39705e87e765561fc316d0cc32d602557 }
heldTextStan: { method: sha256-stan, raw: 77725c932f691e154481d14f48fd597208986236aec92bd6dfd1314bd9ef1147, normalised: fff06368b42ea19f91ee1d71c30c4bd48f7b40e11225ca5bba550605e8f4083b }
licence: "QAA copyright; held for study, private to the project, never published"
series: "QAA Subject Benchmark Statements, 2026 revision with six cross-cutting themes (this statement's fifth edition)"
awardsCovered: ["bachelor's with honours", "master's"]
levelsCovered: ["fheq:6", "fheq:7", "fqheis:10", "fqheis:11"]
nations: ["England", "Wales", "Scotland", "Northern Ireland"]
parts:
  S: full
  B: "partial: no glossary of its own (the front matter points to QAA's Glossary); terms it defines in passing"
  C: "not-applicable: the document sets expectations, not a procedure"
pins: { structure: 0.13.0-draft, template: 0.8.0-draft, benchmarkTemplate: 0.6.0-draft, runFrame: 0.1.1-draft, runLayer: 0.7.0-draft, standards: none yet, terminology: none yet }
lifecycle: drafted
researchedBy: run frame 0.1.1-draft; standards run layer 0.7.0-draft; std, run 0131 (tools/bm_build.py)
passes:
  P1: "2026-10-03 18:40"
  P2: "skipped: read direct from the held text; inferred codes and rung links are for P3"
  P3: open
version: 0.1.2
---

<!-- from INGEST wpk-0016-ingest-pd-template-standards.md 0.8.0-draft and wpk-0016-ingest-pd-template-standards-benchmark.md 0.6.0-draft; built by tools/bm_build.py from run-src/ -->
# Subject Benchmark Statement: Sociology (QAA, April 2026)

> Run 0131, P1 by std. The issuer's words are held in the source library, `wkspc2601-library/txt/qaa-2026-sociology-subject-benchmark-statement-standard.norm.txt`; each S4 record carries its statement in full (`source`) for language analysis, with its span. Paraphrases and versions are ours. Private to the project, never published. In front matter `status` is the issuer's; ours is `lifecycle`. Doubts are in Part E.

## Part 0 Summary

### 0.1 Agent definition
<!-- label: editorial; status: drafted; basis: primary -->
QAA's UK reference point for what a Sociology graduate should know, understand and be able to do: one threshold list of subject knowledge, understanding and skills and one of transferable skills for the honours degree, and a further list for master's study. Reach for it when designing, approving, reviewing or describing a Sociology course, its modules or its outcomes. It sets minimums only: it names no typical or excellent rung, sends classification to Annex D of the qualification frameworks, and is neither a curriculum nor a regulatory requirement in England.

### 0.2 Summary
<!-- label: both; status: drafted; basis: primary -->
Published by QAA in April 2026 as the fifth edition, the statement describes Sociology as the study of how people shape and are shaped by their social world, with its purposes (academic, vocational, professional) and its distinctive features in design, progression, flexibility, partnership and review; it then sets out content, teaching, learning and assessment. Its benchmark standards are threshold only: 18 subject items and 16 transferable skills for bachelor's degrees with honours (FHEQ 6, FQHEIS 10), and 10 items for a master's degree (FHEQ 7), added on top of the honours threshold. It carries six cross-cutting themes: equity, diversity and inclusion; accessibility and the needs of disabled students; education for sustainable development; internationalisation; employability, entrepreneurship and enterprise education; and generative AI. No body accredits Sociology degrees; it names the British, European and International Sociological Associations as partners and the Equality and Human Rights Commission for competence standards.

## Part S Standard

### S1 Identity
<!-- label: source; status: drafted; basis: primary -->
```yaml
issuer: The Quality Assurance Agency for Higher Education
title: "Subject Benchmark Statement: Sociology"
edition: "April 2026 (fifth edition)"
dates:
  published: 2026-04
  other: []
kind: subject-benchmark
jurisdiction: [UK]
authority: "reference: a sector-owned reference point; in England not one of the OfS sector-recognised standards; part of the current quality arrangements in Scotland, Wales and Northern Ireland (D1, front matter: Relationship to legislation)"
licence: "QAA copyright; the document gives no re-use terms in its text (D1, front matter)"
copyrightNotice: { text: "© The Quality Assurance Agency for Higher Education 2026", locator: "D1, index" }
```

### S2 Purpose and scope
<!-- label: source; status: drafted; basis: primary -->
```yaml
governs: "what a Sociology graduate should know, understand and be able to do at the end of a bachelor's degree with honours, with a further list for a master's degree"
appliesTo:
  awards: ["bachelor's with honours", "master's"]
  levels: ["fheq:6", "fqheis:10", "fheq:7", "fqheis:11"]
  providers: ["UK higher education providers"]
whoMustUse: "none-stated; it is a reference point, not a requirement (D1, front matter)"
howUsed: ["design", "approval", "review", "other: external examining; PSRBs; information for prospective students and employers"]
doesNot: "it is not a national curriculum and does not prescribe teaching, learning or assessment; it carries no statutory or regulatory requirement (D1, front matter)"
beneficiary: the student
statedScope: "\"This QAA Subject Benchmark Statement for Sociology defines what can be expected of a graduate in terms of what they might know, do and understand at the end of their studies.\" (D1, front matter: About this Statement)"
statedSubjects:
  - { name: "Sociology", locator: "(D1, front matter; 1.1; 2.3)", kind: "subject", codes: [{ scheme: "hecos", code: "100505", label: "sociology" }, { scheme: "cah", code: "CAH15-01-02", label: "sociology" }] }
subjects: see front matter (subjectScope subjects)
```

### S3 Structure
<!-- label: both; status: drafted; basis: primary -->
```yaml
components:
  - { number: "1.1", order: 3, componentType: paragraph, parent: "section 1", heading: "Context and purposes of a Sociology degree", gloss: "what the subject studies and where its graduates work" }
  - { number: "1.2", order: 4, componentType: paragraph, parent: "section 1", heading: "Context and purposes of a Sociology degree", gloss: "a core social science joining theory and evidence" }
  - { number: "1.3", order: 5, componentType: paragraph, parent: "section 1", heading: "Context and purposes of a Sociology degree", gloss: "its research informs public debate and other disciplines" }
  - { number: "1.4", order: 6, componentType: paragraph, parent: "section 1", heading: "Purposes and characteristics of a Sociology degree", gloss: "three linked purposes: academic, vocational, professional" }
  - { number: "1.5", order: 7, componentType: stem, parent: "section 1", heading: "Purposes and characteristics of a Sociology degree", gloss: "how the three purposes feed one another" }
  - { number: "1.6", order: 8, componentType: paragraph, parent: "section 1", heading: "Equity, diversity and inclusion", gloss: "EDI central; inequality explained by structures; curriculum expectation" }
  - { number: "1.7", order: 9, componentType: paragraph, parent: "section 1", heading: "Equity, diversity and inclusion", gloss: "equality law and inclusion across the student journey" }
  - { number: "1.8", order: 10, componentType: paragraph, parent: "section 1", heading: "Equity, diversity and inclusion", gloss: "difficult topics, inclusive curricula and respect in every setting" }
  - { number: "1.9", order: 11, componentType: paragraph, parent: "section 1", heading: "Accessibility and the needs of disabled students", gloss: "accessibility designed in, not left to individual requests" }
  - { number: "1.10", order: 12, componentType: paragraph, parent: "section 1", heading: "Accessibility and the needs of disabled students", gloss: "flexible, accessible courses with adjustments built in" }
  - { number: "1.11", order: 13, componentType: paragraph, parent: "section 1", heading: "Accessibility and the needs of disabled students", gloss: "access for students from non-standard backgrounds; foundation years" }
  - { number: "1.12", order: 14, componentType: paragraph, parent: "section 1", heading: "Accessibility and the needs of disabled students", gloss: "digital and physical access; disabled people not made the object of study" }
  - { number: "1.13", order: 15, componentType: stem, parent: "section 1", heading: "Education for sustainable development", gloss: "what sustainable development and ESD mean; three things ESD promotes" }
  - { number: "1.14", order: 16, componentType: paragraph, parent: "section 1", heading: "Education for sustainable development", gloss: "ESD as more than environment: a critical, transformative agenda" }
  - { number: "1.15", order: 17, componentType: paragraph, parent: "section 1", heading: "Education for sustainable development", gloss: "competencies ESD builds; communication as its companion" }
  - { number: "1.16", order: 18, componentType: paragraph, parent: "section 1", heading: "Education for sustainable development", gloss: "the subject as a lens on environment, justice and prosperity" }
  - { number: "1.17", order: 19, componentType: paragraph, parent: "section 1", heading: "Education for sustainable development", gloss: "engaging with and critiquing the UN SDGs" }
  - { number: "1.18", order: 20, componentType: paragraph, parent: "section 1", heading: "Education for sustainable development", gloss: "ESD through the whole curriculum, teaching and assessment" }
  - { number: "1.19", order: 21, componentType: paragraph, parent: "section 1", heading: "Internationalisation", gloss: "internationalisation defined; beyond European founders; ESA and ISA resources" }
  - { number: "1.20", order: 22, componentType: paragraph, parent: "section 1", heading: "Internationalisation", gloss: "cross-cultural learning and critique of Western knowledge" }
  - { number: "1.21", order: 23, componentType: stem, parent: "section 1", heading: "Internationalisation", gloss: "five pedagogical routes to internationalisation" }
  - { number: "1.22", order: 24, componentType: paragraph, parent: "section 1", heading: "Internationalisation", gloss: "how context shapes research; international data sources" }
  - { number: "1.23", order: 25, componentType: paragraph, parent: "section 1", heading: "Internationalisation", gloss: "interdisciplinary collaboration for internationalisation" }
  - { number: "1.24", order: 26, componentType: paragraph, parent: "section 1", heading: "Internationalisation", gloss: "responding to a diverse student body; feedback across cultures" }
  - { number: "1.25", order: 27, componentType: paragraph, parent: "section 1", heading: "Internationalisation", gloss: "valuing the knowledge students bring" }
  - { number: "1.26", order: 28, componentType: paragraph, parent: "section 1", heading: "Internationalisation", gloss: "cross-cultural competence for global work and citizenship" }
  - { number: "1.27", order: 29, componentType: paragraph, parent: "section 1", heading: "Employability, entrepreneurship and enterprise education", gloss: "what EEE education is and does for careers" }
  - { number: "1.28", order: 30, componentType: paragraph, parent: "section 1", heading: "Employability, entrepreneurship and enterprise education", gloss: "why the subject and EEE fit together" }
  - { number: "1.29", order: 31, componentType: paragraph, parent: "section 1", heading: "Employability, entrepreneurship and enterprise education", gloss: "research training and ethics as employability strengths" }
  - { number: "1.30", order: 32, componentType: paragraph, parent: "section 1", heading: "Employability, entrepreneurship and enterprise education", gloss: "EEE for change-makers and a self-directed working life" }
  - { number: "1.31", order: 33, componentType: paragraph, parent: "section 1", heading: "Employability, entrepreneurship and enterprise education", gloss: "placements, partnerships and cross-disciplinary work" }
  - { number: "1.32", order: 34, componentType: paragraph, parent: "section 1", heading: "Employability, entrepreneurship and enterprise education", gloss: "applied projects with outside partners" }
  - { number: "1.33", order: 35, componentType: paragraph, parent: "section 1", heading: "Employability, entrepreneurship and enterprise education", gloss: "course teams working with careers and employers" }
  - { number: "1.34", order: 36, componentType: stem, parent: "section 1", heading: "Employability, entrepreneurship and enterprise education", gloss: "eight broader capabilities courses give chances to learn" }
  - { number: "1.35", order: 37, componentType: paragraph, parent: "section 1", heading: "Generative artificial intelligence", gloss: "generative AI defined; the subject placed to study it" }
  - { number: "1.36", order: 38, componentType: paragraph, parent: "section 1", heading: "Generative artificial intelligence", gloss: "critical engagement with power, wealth and environmental cost" }
  - { number: "1.37", order: 39, componentType: paragraph, parent: "section 1", heading: "Generative artificial intelligence", gloss: "AI as tool and social reality; responsible use" }
  - { number: "1.38", order: 40, componentType: paragraph, parent: "section 1", heading: "Generative artificial intelligence", gloss: "the subject's critical angle on technology" }
  - { number: "1.39", order: 41, componentType: paragraph, parent: "section 1", heading: "Generative artificial intelligence", gloss: "staff keeping current; ethics and judgement for graduates" }
  - { number: "1.40", order: 42, componentType: paragraph, parent: "section 1", heading: "Generative artificial intelligence", gloss: "teaching with AI while keeping disciplinary questions" }
  - { number: "1.41", order: 43, componentType: paragraph, parent: "section 1", heading: "Generative artificial intelligence", gloss: "assessment guidance on AI use; criteria for ethical use" }
  - { number: "2.1", order: 45, componentType: paragraph, parent: "section 2", heading: "Design", gloss: "what courses provide and what students develop" }
  - { number: "2.2", order: 46, componentType: paragraph, parent: "section 2", heading: "Design", gloss: "joining empirical method and theory" }
  - { number: "2.3", order: 47, componentType: paragraph, parent: "section 2", heading: "Design", gloss: "connections to other subjects; distinctiveness to grasp" }
  - { number: "2.4", order: 48, componentType: paragraph, parent: "section 2", heading: "Progression", gloss: "varied entry routes and lived experience" }
  - { number: "2.5", order: 49, componentType: paragraph, parent: "section 2", heading: "Progression", gloss: "progression to the threshold through honours or integrated master's" }
  - { number: "2.6", order: 50, componentType: paragraph, parent: "section 2", heading: "Progression", gloss: "readiness for postgraduate study" }
  - { number: "2.7", order: 51, componentType: paragraph, parent: "section 2", heading: "Progression", gloss: "joint and combined honours" }
  - { number: "2.8", order: 52, componentType: paragraph, parent: "section 2", heading: "Progression", gloss: "early exit awards" }
  - { number: "2.9", order: 53, componentType: paragraph, parent: "section 2", heading: "Flexibility", gloss: "varied teaching and assessment across courses" }
  - { number: "2.10", order: 54, componentType: paragraph, parent: "section 2", heading: "Flexibility", gloss: "course length across the UK nations; Scottish degrees" }
  - { number: "2.11", order: 55, componentType: paragraph, parent: "section 2", heading: "Flexibility", gloss: "modes, terms and credit routes" }
  - { number: "2.12", order: 56, componentType: paragraph, parent: "section 2", heading: "Partnership", gloss: "delivery with partners" }
  - { number: "2.13", order: 57, componentType: paragraph, parent: "section 2", heading: "Partnership", gloss: "no accrediting body; professional associations" }
  - { number: "2.14", order: 58, componentType: paragraph, parent: "section 2", heading: "Monitoring and review", gloss: "routine monitoring and periodic review" }
  - { number: "2.15", order: 59, componentType: paragraph, parent: "section 2", heading: "Monitoring and review", gloss: "external reviewers in periodic review" }
  - { number: "2.16", order: 60, componentType: paragraph, parent: "section 2", heading: "Monitoring and review", gloss: "the external examining system" }
  - { number: "3.1", order: 62, componentType: area, parent: "section 3", heading: "Content", gloss: "a theoretical and empirical discipline, local to global" }
  - { number: "3.2", order: 63, componentType: area, parent: "section 3", heading: "Content", gloss: "its range across time, place and setting" }
  - { number: "3.3", order: 64, componentType: area, parent: "section 3", heading: "Content", gloss: "seven ways the subject studies social life" }
  - { number: "3.4", order: 65, componentType: area, parent: "section 3", heading: "Content", gloss: "six typical areas of a course" }
  - { number: "3.5", order: 66, componentType: paragraph, parent: "section 3", heading: "Teaching, learning and assessment", gloss: "accessible curricula and assessment; this section as guidance" }
  - { number: "3.6", order: 67, componentType: stem, parent: "section 3", heading: "Teaching and learning", gloss: "learning resources open to students" }
  - { number: "3.7", order: 68, componentType: paragraph, parent: "section 3", heading: "Teaching and learning", gloss: "extracurricular and international resources" }
  - { number: "3.8", order: 69, componentType: practice, parent: "section 3", heading: "Teaching and learning", gloss: "interaction, independent study and formative assessment" }
  - { number: "3.9", order: 70, componentType: practice, parent: "section 3", heading: "Teaching and learning", gloss: "forms of teaching; flipped classrooms" }
  - { number: "3.10", order: 71, componentType: practice, parent: "section 3", heading: "Teaching and learning", gloss: "digital tools and generative AI in teaching" }
  - { number: "3.11", order: 72, componentType: practice, parent: "section 3", heading: "Teaching and learning", gloss: "ten features of teaching and learning in the subject" }
  - { number: "3.12", order: 73, componentType: paragraph, parent: "section 3", heading: "Assessment", gloss: "assessment of and for learning, explained to students" }
  - { number: "3.13", order: 74, componentType: practice, parent: "section 3", heading: "Assessment", gloss: "decolonising assessment" }
  - { number: "3.14", order: 75, componentType: paragraph, parent: "section 3", heading: "Assessment", gloss: "equality, accessibility and review in assessment design" }
  - { number: "3.15", order: 76, componentType: practice, parent: "section 3", heading: "Assessment", gloss: "varied assessment forms; digital and AI-enabled tasks" }
  - { number: "3.16", order: 77, componentType: practice, parent: "section 3", heading: "Assessment", gloss: "assessment that mirrors real outputs" }
  - { number: "3.17", order: 78, componentType: practice, parent: "section 3", heading: "Assessment", gloss: "practical research exercises and their four aspects" }
  - { number: "3.18", order: 79, componentType: paragraph, parent: "section 3", heading: "Assessment", gloss: "transferable skills from practical exercises" }
  - { number: "3.19", order: 80, componentType: paragraph, parent: "section 3", heading: "Assessment", gloss: "assessment for employability" }
  - { number: "3.20", order: 81, componentType: paragraph, parent: "section 3", heading: "Assessment", gloss: "transparent assessment and clear rubrics" }
  - { number: "3.21", order: 82, componentType: practice, parent: "section 3", heading: "Assessment", gloss: "five accessible assessment features" }
  - { number: "3.22", order: 83, componentType: practice, parent: "section 3", heading: "Assessment", gloss: "feedback that improves later work" }
  - { number: "4.1", order: 85, componentType: paragraph, parent: "section 4", heading: "Introduction", gloss: "the standards are minimums for the honours award" }
  - { number: "4.2", order: 86, componentType: paragraph, parent: "section 4", heading: "Introduction", gloss: "most exceed the threshold; Annex D for classes" }
  - { number: "4.3", order: 87, componentType: paragraph, parent: "section 4", heading: "Introduction", gloss: "not competence standards; EHRC guidance" }
  - { number: "4.4", order: 88, componentType: stem, parent: "section 4", heading: "Threshold level: Subject knowledge, understanding and skills", gloss: "threshold subject knowledge, understanding and skills (18 items)" }
  - { number: "4.5", order: 89, componentType: stem, parent: "section 4", heading: "Threshold level: Transferable skills", gloss: "threshold transferable skills (16 items)" }
  - { number: "4.6", order: 90, componentType: stem, parent: "section 4", heading: "Master's level study", gloss: "master's outcomes added to the honours threshold (10 items)" }
  - { number: "1", componentType: section, parent: none, heading: "Context and purposes of a Sociology degree", gloss: "section 1" }
  - { number: "2", componentType: section, parent: none, heading: "Distinctive features of a Sociology degree", gloss: "section 2" }
  - { number: "3", componentType: section, parent: none, heading: "Content, structure and delivery", gloss: "section 3" }
  - { number: "4", componentType: section, parent: none, heading: "Benchmark standards", gloss: "section 4" }
excluded:
  - { number: "none", heading: "About this Statement; How can I use this document?; Relationship to legislation; Additional sector reference points", kind: "other: front matter, read for S1, S2, S7 and SB6" }
  - { number: "1, 2, 3, 4", heading: "section heading lines", kind: "other: headings, recorded in S3 as sections" }
  - { number: "5", heading: "List of references and further resources", kind: "other: back matter, read for S7 and SB6" }
  - { number: "6", heading: "Membership of the Advisory Group", kind: "other: names, out of scope; read for the edition history (S7 supersedes)" }
```

### S4 Statements
<!-- label: both; status: drafted; basis: primary. Only standards (D-std-0002 (a)): 72 records. `source` is the issuer's statement exactly as its span holds it (D-std-0014). -->
```yaml
- id: qaa/sociology-2026/1.6
  locator: { number: "1.6", headingPath: ["Context and purposes of a Sociology degree", "Equity, diversity and inclusion"] }
  span: { start: 10499, end: 11302 }
  source: "1.6 Developing knowledge and understanding of equity, diversity and inclusion (EDI) is central to the discipline of Sociology. Given its historical and contemporary focus on stratification and differential access to wealth and power, Sociology is uniquely equipped to offer explanations of inequalities such as those related to race/ethnicity, social class, gender, sexuality, disability, religion and age (and the ways in which these intersect). As a discipline,\n\n4\nSociology prioritises an understanding of the social drivers and structures that (re)produce inequality, rather than focusing predominantly on individual actions and responsibility. Therefore, there is an expectation that all Sociology courses have matters relating to (in)equality, diversity and inclusion embedded into the curriculum."
  stem: none
  statementType: expectation
  rung: none
  force: describes
  level: none
  appliesTo: "all Sociology courses"
  addressee: provider
  verbs: ["embedded"]
  about: "equality, diversity and inclusion built into every curriculum"
  themes: [theme:edi]
  domain: none
  award: ["none"]
  gradeOf: none
  paraphrase: "Equity, diversity and inclusion are central to the subject, which explains inequality through social drivers and structures rather than individual choices; every Sociology course is expected to build questions of equality, diversity and inclusion into its curriculum."
  quote: full   # the issuer's statement is in `source` (D-std-0014)
  audience: practitioner
  subjects: inherited
- id: qaa/sociology-2026/1.7
  locator: { number: "1.7", headingPath: ["Context and purposes of a Sociology degree", "Equity, diversity and inclusion"] }
  span: { start: 11303, end: 12066 }
  source: "1.7 EDI is central to the design and implementation of contemporary Sociology curricula. Legislation requires institutions to ensure that both staff and students are treated fairly under the law and are not discriminated against. However, inclusion and engagement needs can go beyond the confines of equalities legislation and be considered during all aspects of the student journey. This includes giving thought to the ways in which students are part of, and accounted for, in the curriculum design, the content of the course, the delivery of learning and teaching, and assessment and feedback practices. It is important for all those involved to consider the diversity of the student population and ensure that all students are given the opportunity to succeed."
  stem: none
  statementType: requirement
  rung: none
  force: must
  level: none
  appliesTo: "institutions and everyone involved in a course"
  addressee: provider
  verbs: ["requires", "ensure", "treated"]
  about: "fair treatment under equality law; inclusion through the student journey"
  themes: [theme:edi]
  domain: none
  award: ["none"]
  gradeOf: none
  paraphrase: "Equality, diversity and inclusion shape how Sociology curricula are designed and run; the law requires institutions to make sure staff and students are treated fairly and not discriminated against, and inclusion should reach past the law into curriculum design, content, teaching, assessment and feedback."
  quote: full   # the issuer's statement is in `source` (D-std-0014)
  audience: practitioner
  subjects: inherited
- id: qaa/sociology-2026/1.8
  locator: { number: "1.8", headingPath: ["Context and purposes of a Sociology degree", "Equity, diversity and inclusion"] }
  span: { start: 12067, end: 13626 }
  source: "1.8 Difficult and sometimes controversial topics will likely be studied during a Sociology programme. Students should be supported to make use of evidence to help express their arguments and engage with diverse perspectives in a safe and inclusive learning environment, while critically reflecting on their views. Sociologists ensure that curriculum content and learning resources are accessible and responsive to a diverse student population, and staff supported to do this in ways that are appropriate for their programme. This includes the development of more inclusive Sociology curricula to ensure that students critically examine and challenge the theories and research that have historically been dominant within the discipline. Inclusivity (and creating inclusive curricula) is an ongoing process. Local quality assurance and enhancement processes within institutions can consider and promote equality of opportunity for students, while removing barriers to learning and participation wherever possible. Students have diverse needs depending on their circumstances, and Sociology courses should be inclusive for all students, recognising the different types of exclusion students face as well as multiple forms of exclusion which might impact accessibility. Course teams should, wherever possible, ensure that all students are equally respected in settings they attend as part of their course, for example on campus, course trips or placements, regardless of their race/ethnicity, gender, disability, age, sexuality or other aspects of their identity."
  stem: none
  statementType: expectation
  rung: none
  force: should
  level: none
  appliesTo: "Sociology course teams and institutions"
  addressee: provider
  verbs: ["supported", "ensure", "examine", "challenge", "respected"]
  about: "safe study of contested topics; inclusive curricula; respect in every setting"
  themes: [theme:edi]
  domain: none
  award: ["none"]
  gradeOf: none
  paraphrase: "Students meet difficult and contested topics, and should be supported to argue from evidence and engage with differing views in a safe, inclusive setting while reflecting on their own; curricula should be made more inclusive so students question historically dominant theories, courses should be inclusive for all, and course teams should, where they can, see that every student is equally respected on campus, on trips and on placement."
  quote: full   # the issuer's statement is in `source` (D-std-0014)
  audience: practitioner
  subjects: inherited
- id: qaa/sociology-2026/1.9
  locator: { number: "1.9", headingPath: ["Context and purposes of a Sociology degree", "Accessibility and the needs of disabled students"] }
  span: { start: 13676, end: 14139 }
  source: "1.9 Sociology courses are committed to accessibility in its broadest form, embedding a commitment to inclusivity from the design of the course through to delivery and practice. Accessibility is about making the course accessible to all. Accessibility should be part of course design, and delivery should make all aspects of the course, including teaching, assessment, activities and fieldtrips, accessible without the need for individual requests for adjustments."
  stem: none
  statementType: expectation
  rung: none
  force: should
  level: none
  appliesTo: "Sociology course design and delivery"
  addressee: provider
  verbs: ["embedding", "make"]
  about: "accessibility designed in from the start"
  themes: [theme:accessibility]
  domain: none
  award: ["none"]
  gradeOf: none
  paraphrase: "Courses commit to accessibility in the widest sense; course design should include accessibility from the start, and delivery should make teaching, assessment, activities and fieldtrips accessible without students having to ask for individual adjustments."
  quote: full   # the issuer's statement is in `source` (D-std-0014)
  audience: practitioner
  subjects: inherited
- id: qaa/sociology-2026/1.10
  locator: { number: "1.10", headingPath: ["Context and purposes of a Sociology degree", "Accessibility and the needs of disabled students"] }
  span: { start: 14140, end: 14481 }
  source: "1.10 Sociology courses should be flexible and accessible. This can apply to admissions, learning resources, fieldwork and fieldtrips, and teamwork activities. Sociology courses should build in accessibility and embed inclusive practice to ensure disabled students are not singled out so that adjustments are part of the design of the course."
  stem: none
  statementType: expectation
  rung: none
  force: should
  level: none
  appliesTo: "Sociology courses"
  addressee: provider
  verbs: ["build", "embed"]
  about: "flexible, accessible courses with adjustments in the design"
  themes: [theme:accessibility]
  domain: none
  award: ["none"]
  gradeOf: none
  paraphrase: "Courses should be flexible and accessible, in admissions, resources, fieldwork, fieldtrips and teamwork, and should build accessibility and inclusive practice in so that disabled students are not singled out and adjustments are part of the course design."
  quote: full   # the issuer's statement is in `source` (D-std-0014)
  audience: practitioner
  subjects: inherited
- id: qaa/sociology-2026/1.12
  locator: { number: "1.12", headingPath: ["Context and purposes of a Sociology degree", "Accessibility and the needs of disabled students"] }
  span: { start: 14735, end: 15536 }
  source: "1.12 Accessibility while studying: Following entry and enrolment, ongoing teaching and learning considerations include the importance of digital accessibility, especially in blended learning environments where materials can be accessed by all students. Classrooms and\n\n5\nstudy spaces should be accessible for all students, recognising the specific accessibility needs of disabled people. Inclusive language and approaches that avoid positioning disabled people as 'other' or 'the object of study' are a priority. Similarly, research and pedagogic approaches that explore the lived experiences of disabled people are valued. This includes creating communities of care within the curriculum, recognising that many students who cannot attend extracurricular activities can still be welcomed and involved."
  stem: none
  statementType: expectation
  rung: none
  force: should
  level: none
  appliesTo: "Sociology teaching spaces and approaches"
  addressee: provider
  verbs: ["recognising"]
  about: "digital and physical access; inclusive language about disability"
  themes: [theme:accessibility]
  domain: none
  award: ["none"]
  gradeOf: none
  paraphrase: "Once students are enrolled, digital accessibility matters, above all in blended learning; classrooms and study spaces should be accessible to all, language and approaches should not cast disabled people as other or as objects of study, and research and teaching that explore disabled people's lived experience are valued."
  quote: full   # the issuer's statement is in `source` (D-std-0014)
  audience: practitioner
  subjects: inherited
- id: qaa/sociology-2026/1.18
  locator: { number: "1.18", headingPath: ["Context and purposes of a Sociology degree", "Education for sustainable development"] }
  span: { start: 18159, end: 18867 }
  source: "1.18 A focus on ESD should underpin not just the curriculum but also teaching and learning practices and assessment. Indeed, it may be useful to consider the three-fold focus outlined in the QAA/Advance HE guidance on ESD, which emphasises the importance of exploring (i) ways of thinking, (ii) ways of practising, and (iii) ways of being in relation to ESD. ESD can benefit from innovative learning and teaching practices. The interdisciplinary nature of ESD\n\n6\nencourages collaborative, co-created problem-based learning, bringing together students, tutors and possibly external partners to test ideas, share knowledge and develop solutions to address real-life challenges and advance sustainability goals."
  stem: none
  statementType: expectation
  rung: none
  force: should
  level: none
  appliesTo: "Sociology curricula, teaching and assessment"
  addressee: provider
  verbs: ["underpin"]
  about: "education for sustainable development across curriculum, teaching and assessment"
  themes: [theme:esd]
  domain: none
  award: ["none"]
  gradeOf: none
  paraphrase: "Education for sustainable development should underpin teaching, learning and assessment as well as the curriculum; the QAA and Advance HE guidance's three ways (thinking, practising, being) may help, and its interdisciplinary nature suits co-created, problem-based work with students, tutors and partners on real challenges."
  quote: full   # the issuer's statement is in `source` (D-std-0014)
  audience: practitioner
  subjects: inherited
- id: qaa/sociology-2026/1.21.b1
  locator: { number: "1.21.b1", headingPath: ["Context and purposes of a Sociology degree", "Internationalisation"] }
  span: { start: 20188, end: 20237 }
  source: "the contribution of international guest lecturers"
  stem: "1.21"
  statementType: expectation
  rung: none
  force: should
  level: none
  appliesTo: "Sociology courses pursuing internationalisation"
  addressee: provider
  verbs: []
  about: "international guest lecturers"
  themes: [theme:internationalisation]
  domain: none
  award: ["none"]
  gradeOf: none
  paraphrase: "Internationalisation should be pursued through teaching as well as the curriculum, one route being lectures from international guests."
  quote: full   # the issuer's statement is in `source` (D-std-0014)
  audience: practitioner
  subjects: inherited
- id: qaa/sociology-2026/1.21.b2
  locator: { number: "1.21.b2", headingPath: ["Context and purposes of a Sociology degree", "Internationalisation"] }
  span: { start: 20240, end: 20343 }
  source: "the promotion of students' mobility, such as field trips, studying abroad, and international placements"
  stem: "1.21"
  statementType: expectation
  rung: none
  force: should
  level: none
  appliesTo: "Sociology courses pursuing internationalisation"
  addressee: provider
  verbs: []
  about: "student mobility: trips, study abroad, placements"
  themes: [theme:internationalisation]
  domain: none
  award: ["none"]
  gradeOf: none
  paraphrase: "One route is promoting student mobility, through field trips, study abroad and placements overseas."
  quote: full   # the issuer's statement is in `source` (D-std-0014)
  audience: practitioner
  subjects: inherited
- id: qaa/sociology-2026/1.21.b3
  locator: { number: "1.21.b3", headingPath: ["Context and purposes of a Sociology degree", "Internationalisation"] }
  span: { start: 20346, end: 20483 }
  source: "the exploration of collaborations with institutions in the Global South for meaningful engagement in alternative sociological standpoints"
  stem: "1.21"
  statementType: expectation
  rung: none
  force: should
  level: none
  appliesTo: "Sociology courses pursuing internationalisation"
  addressee: provider
  verbs: []
  about: "collaboration with Global South institutions"
  themes: [theme:internationalisation]
  domain: none
  award: ["none"]
  gradeOf: none
  paraphrase: "One route is exploring partnerships with institutions in the Global South so students meet other sociological standpoints in a meaningful way."
  quote: full   # the issuer's statement is in `source` (D-std-0014)
  audience: practitioner
  subjects: inherited
- id: qaa/sociology-2026/1.21.b4
  locator: { number: "1.21.b4", headingPath: ["Context and purposes of a Sociology degree", "Internationalisation"] }
  span: { start: 20486, end: 20594 }
  source: "the celebration of students' diverse cultural backgrounds as sources of alternative sociological standpoints"
  stem: "1.21"
  statementType: expectation
  rung: none
  force: should
  level: none
  appliesTo: "Sociology courses pursuing internationalisation"
  addressee: provider
  verbs: []
  about: "students' cultural backgrounds as standpoints"
  themes: [theme:internationalisation]
  domain: none
  award: ["none"]
  gradeOf: none
  paraphrase: "One route is celebrating the cultural backgrounds students bring as sources of other sociological standpoints."
  quote: full   # the issuer's statement is in `source` (D-std-0014)
  audience: practitioner
  subjects: inherited
- id: qaa/sociology-2026/1.21.b5
  locator: { number: "1.21.b5", headingPath: ["Context and purposes of a Sociology degree", "Internationalisation"] }
  span: { start: 20597, end: 20658 }
  source: "the promotion of Collaborative Online International Learning."
  stem: "1.21"
  statementType: expectation
  rung: none
  force: should
  level: none
  appliesTo: "Sociology courses pursuing internationalisation"
  addressee: provider
  verbs: []
  about: "Collaborative Online International Learning"
  themes: [theme:internationalisation]
  domain: none
  award: ["none"]
  gradeOf: none
  paraphrase: "One route is promoting Collaborative Online International Learning."
  quote: full   # the issuer's statement is in `source` (D-std-0014)
  audience: practitioner
  subjects: inherited
- id: qaa/sociology-2026/1.25
  locator: { number: "1.25", headingPath: ["Context and purposes of a Sociology degree", "Internationalisation"] }
  span: { start: 22423, end: 22759 }
  source: "1.25 Internationalisation requires teaching practices that value the unique knowledge that students bring with them into the teaching situation. For example, encouraging dialogue between students and their teachers that helps students to see themselves as legitimate and valued contributors to knowledge within the learning environment."
  stem: none
  statementType: requirement
  rung: none
  force: must
  level: none
  appliesTo: "teaching that aims to internationalise"
  addressee: provider
  verbs: ["requires", "value", "encouraging"]
  about: "teaching that values what students bring"
  themes: [theme:internationalisation]
  domain: none
  award: ["none"]
  gradeOf: none
  paraphrase: "Internationalisation needs teaching that values the distinct knowledge students bring with them, for example through dialogue that helps students see themselves as legitimate contributors to knowledge."
  quote: full   # the issuer's statement is in `source` (D-std-0014)
  audience: practitioner
  subjects: inherited
- id: qaa/sociology-2026/1.33
  locator: { number: "1.33", headingPath: ["Context and purposes of a Sociology degree", "Employability, entrepreneurship and enterprise education"] }
  span: { start: 25846, end: 26389 }
  source: "1.33 Course teams should collaborate with colleagues in careers services, partnership delivery, alumni, social enterprises and sector employers to design and deliver EEE education and to create pathways for students. This may take the form of, for example, visiting lectures, master classes and client briefs – with appropriate career learning tasks scaffolded around such opportunities to maximise their benefit for students. Reflective and reflexive practice can also consolidate learning, supporting emotional awareness and action planning."
  stem: none
  statementType: expectation
  rung: none
  force: should
  level: none
  appliesTo: "Sociology course teams"
  addressee: provider
  verbs: ["collaborate", "design", "deliver", "create"]
  about: "working with careers services and employers on EEE education"
  themes: [theme:enterprise]
  domain: none
  award: ["none"]
  gradeOf: none
  paraphrase: "Course teams should work with careers services, partnership staff, alumni, social enterprises and employers to design and deliver employability, enterprise and entrepreneurship education and to open pathways for students, for example through visiting lectures, master classes and client briefs with scaffolded career tasks."
  quote: full   # the issuer's statement is in `source` (D-std-0014)
  audience: practitioner
  subjects: inherited
- id: qaa/sociology-2026/1.40
  locator: { number: "1.40", headingPath: ["Context and purposes of a Sociology degree", "Generative artificial intelligence"] }
  span: { start: 29082, end: 29437 }
  source: "1.40 Creative teaching integrates GenAI to enhance digital literacy while remaining rooted in core disciplinary questions. Students should be encouraged to engage critically with new tools – understanding not only what GenAI can facilitate, but also what is lost when dialogue and human creativity are replaced, so that marginalised voices are not erased."
  stem: none
  statementType: expectation
  rung: none
  force: should
  level: none
  appliesTo: "students and those who teach them"
  addressee: both
  verbs: ["encouraged", "engage"]
  about: "critical engagement with generative AI"
  themes: [theme:generative-ai]
  domain: none
  award: ["none"]
  gradeOf: none
  paraphrase: "Teaching can use generative AI to build digital literacy while keeping to the subject's core questions, and students should be encouraged to approach new tools critically, weighing what they make possible against what is lost when they stand in for human dialogue and creativity, so that the voices of marginalised people are kept."
  quote: full   # the issuer's statement is in `source` (D-std-0014)
  audience: both
  subjects: inherited
- id: qaa/sociology-2026/2.1
  locator: { number: "2.1", headingPath: ["Distinctive features of a Sociology degree", "Design"] }
  span: { start: 29859, end: 30380 }
  source: "2.1 Sociology courses are designed to provide students with an education in the theoretical, methodological, analytical and practical aspects of the discipline, as well as the relationships between its concepts and principles. Students are expected to develop a range of skills that will enable them to examine how social structures and institutions shape, and are shaped by, human agency. They are also expected to understand social phenomena at global, community and personal levels, and how these levels are connected."
  stem: none
  statementType: outcome
  rung: none
  force: must   # D-std-0016: "are expected to" read as must
  level: fheq:6
  appliesTo: "students on Sociology courses"
  addressee: learner
  verbs: ["develop", "examine", "understand"]
  about: "skills to examine structure and agency; social phenomena across levels"
  themes: [none]
  domain: understanding
  award: ["bachelor's with honours"]
  gradeOf: none
  paraphrase: "Courses give an education in the theory, methods, analysis and practice of the subject; students are expected to build skills to examine how institutions and structures mould human agency and are moulded by it, and to understand social life at the global, community and personal scales and the links between them."
  quote: full   # the issuer's statement is in `source` (D-std-0014)
  audience: both
  subjects: inherited
- id: qaa/sociology-2026/2.3
  locator: { number: "2.3", headingPath: ["Distinctive features of a Sociology degree", "Design"] }
  span: { start: 30883, end: 31732 }
  source: "2.3 Sociology, as a core social science discipline, provides intellectual, methodological and analytical tools relevant to other subjects associated with the analysis of social life and society. Sociology may be studied as a single honours degree but also has connections to (and is often studied alongside) a range of subjects, including health and life sciences, Psychology, Philosophy, Education Studies, legal studies, Politics and International Relations, Geography, Economics, Social Policy, History, and other humanities disciplines. Following a programme of study, graduates and students should be able to understand and appreciate the distinctiveness of Sociology – for example, regarding social standpoints, social explanations, levels of analysis, the value of theory, and evidence – as well as its shared concerns with other disciplines."
  stem: none
  statementType: outcome
  rung: none
  force: should
  level: fheq:6
  appliesTo: "graduates and students after a programme of study"
  addressee: learner
  verbs: ["understand", "appreciate"]
  about: "the distinctiveness of the subject and its shared concerns"
  themes: [none]
  domain: understanding
  award: ["bachelor's with honours"]
  gradeOf: none
  paraphrase: "The subject gives tools used across the social sciences and is often studied with other subjects; once their studies end, students and graduates should be able to understand and value what makes Sociology distinct (its standpoints, explanations, levels of analysis, use of theory and evidence) and what it shares with other disciplines."
  quote: full   # the issuer's statement is in `source` (D-std-0014)
  audience: both
  subjects: inherited
- id: qaa/sociology-2026/2.7
  locator: { number: "2.7", headingPath: ["Distinctive features of a Sociology degree", "Progression"] }
  span: { start: 33151, end: 33630 }
  source: "2.7 Undergraduates studying Sociology courses as part of a combined or joint degree with other subjects (including courses that specify major and minor options) will achieve core elements of the specific and generic skills outlined in this Statement and will add others according to the areas covered in the other subject(s) of their degree. Additionally, they may\n\n11\nexplore the overlap between different disciplines, creating further opportunities for interdisciplinary study."
  stem: none
  statementType: outcome
  rung: none
  force: will
  level: fheq:6
  appliesTo: "undergraduates on joint or combined Sociology courses"
  addressee: learner
  verbs: ["achieve", "add"]
  about: "core skills in joint and combined honours"
  themes: [none]
  domain: none
  award: ["bachelor's with honours"]
  gradeOf: none
  paraphrase: "Undergraduates taking Sociology in a joint or combined degree, including major and minor routes, will reach core parts of the subject-specific and generic skills set out here and will add others from their other subject, and may explore the overlaps."
  quote: full   # the issuer's statement is in `source` (D-std-0014)
  audience: both
  subjects: inherited
- id: qaa/sociology-2026/2.9
  locator: { number: "2.9", headingPath: ["Distinctive features of a Sociology degree", "Flexibility"] }
  span: { start: 33986, end: 34461 }
  source: "2.9 Teaching, learning and approaches to assessment will vary across Sociology programmes of study, reflecting differences in departmental/school orientations, aims, specialisms and interests. However, it is expected that all Sociology courses will value approaches that incorporate varied and flexible learning and teaching styles, to reflect the diverse learning needs of Sociology students. As such, students can expect to be taught and assessed in a wide variety of ways."
  stem: none
  statementType: expectation
  rung: none
  force: will
  level: none
  appliesTo: "all Sociology courses"
  addressee: provider
  verbs: ["value", "incorporate", "reflect"]
  about: "varied, flexible teaching for diverse learning needs"
  themes: [none]
  domain: none
  award: ["none"]
  gradeOf: none
  paraphrase: "Teaching and assessment vary between departments, but every Sociology course is expected to value varied, flexible teaching and learning styles that reflect students' diverse needs, so students meet many kinds of teaching and assessment."
  quote: full   # the issuer's statement is in `source` (D-std-0014)
  audience: practitioner
  subjects: inherited
- id: qaa/sociology-2026/2.15
  locator: { number: "2.15", headingPath: ["Distinctive features of a Sociology degree", "Monitoring and review"] }
  span: { start: 37370, end: 37667 }
  source: "2.15 Externality is an essential component of the quality assurance system in the UK. Providers will use external reviewers as part of periodic review to gain an independent perspective on any proposed changes and ensure threshold standards are achieved and content is appropriate for the subject."
  stem: none
  statementType: expectation
  rung: none
  force: will
  level: none
  appliesTo: "providers conducting periodic review"
  addressee: provider
  verbs: ["use", "gain", "ensure"]
  about: "external reviewers in periodic review"
  themes: [none]
  domain: none
  award: ["none"]
  gradeOf: none
  paraphrase: "Externality is essential to UK quality assurance; providers will use external reviewers in periodic review for an independent view on changes and to make sure threshold standards are met and content suits the subject."
  quote: full   # the issuer's statement is in `source` (D-std-0014)
  audience: practitioner
  subjects: inherited
- id: qaa/sociology-2026/3.11.b1
  locator: { number: "3.11.b1", headingPath: ["Content, structure and delivery", "Teaching and learning"] }
  span: { start: 44160, end: 44312 }
  source: "Teaching and learning approaches support students' experimentation with theory, which should be scaffolded and revisited throughout the levels of study."
  stem: "3.11"
  statementType: expectation
  rung: none
  force: should
  level: none
  appliesTo: "teaching and learning in Sociology"
  addressee: provider
  verbs: ["support", "scaffolded", "revisited"]
  about: "scaffolded experimentation with theory across the levels"
  themes: [none]
  domain: none
  award: ["none"]
  gradeOf: none
  paraphrase: "Teaching supports students in experimenting with theory, and this should be scaffolded and returned to at each level of study."
  quote: full   # the issuer's statement is in `source` (D-std-0014)
  audience: practitioner
  subjects: inherited
- id: qaa/sociology-2026/3.11.b4
  locator: { number: "3.11.b4", headingPath: ["Content, structure and delivery", "Teaching and learning"] }
  span: { start: 45000, end: 45272 }
  source: "Decolonisation as a subject includes knowledge, research and theories from across the world, supporting students to understand how some knowledge and perspectives are valued more than others, and students should be able to articulate the impact of colonial legacies today."
  stem: "3.11"
  statementType: outcome
  rung: none
  force: should
  level: none
  appliesTo: "students of Sociology"
  addressee: learner
  verbs: ["articulate"]
  about: "colonial legacies and whose knowledge is valued"
  themes: [none]
  domain: understanding
  award: ["bachelor's with honours"]
  gradeOf: none
  paraphrase: "Decolonisation draws on knowledge, research and theory from across the world and helps students see that some knowledge and perspectives are valued above others; students should be able to explain how colonial legacies matter today."
  quote: full   # the issuer's statement is in `source` (D-std-0014)
  audience: both
  subjects: inherited
- id: qaa/sociology-2026/3.12
  locator: { number: "3.12", headingPath: ["Content, structure and delivery", "Assessment"] }
  span: { start: 46531, end: 46833 }
  source: "3.12 Assessment occupies an important role in Sociology courses, as students' progress through the programme and engage more widely with the discipline. The distinction between assessment of learning and assessment for learning – and the importance of both – should be communicated clearly to students."
  stem: none
  statementType: expectation
  rung: none
  force: should
  level: none
  appliesTo: "Sociology course teams"
  addressee: provider
  verbs: ["communicated"]
  about: "explaining assessment of and for learning"
  themes: [none]
  domain: none
  award: ["none"]
  gradeOf: none
  paraphrase: "Assessment matters as students progress; the difference between assessing what has been learned and assessing to support learning, and the value of each, should be explained clearly to students."
  quote: full   # the issuer's statement is in `source` (D-std-0014)
  audience: practitioner
  subjects: inherited
- id: qaa/sociology-2026/3.14
  locator: { number: "3.14", headingPath: ["Content, structure and delivery", "Assessment"] }
  span: { start: 47034, end: 47486 }
  source: "3.14 As assessment practices may reproduce inequalities, it is important that assessments are designed to take account of equality and diversity, ensuring accessibility and inclusivity for all students to minimise the need for subsequent adjustments. Providing a choice of assessment approaches for students can be an effective means of increasing accessibility. Assessments should also be regularly reviewed to ensure that they remain fit for purpose."
  stem: none
  statementType: expectation
  rung: none
  force: should
  level: none
  appliesTo: "assessment design in Sociology"
  addressee: provider
  verbs: ["designed", "reviewed"]
  about: "equitable, accessible assessment, reviewed regularly"
  themes: [none]
  domain: none
  award: ["none"]
  gradeOf: none
  paraphrase: "Since assessment can reproduce inequality, it matters that assessments take account of equality and diversity and are accessible and inclusive, reducing later adjustments; offering choice can widen access, and assessments should be reviewed regularly to stay fit for purpose."
  quote: full   # the issuer's statement is in `source` (D-std-0014)
  audience: practitioner
  subjects: inherited
- id: qaa/sociology-2026/3.15
  locator: { number: "3.15", headingPath: ["Content, structure and delivery", "Assessment"] }
  span: { start: 47487, end: 48161 }
  source: "3.15 There are many diverse and inclusive forms of formative and summative assessment that can be used in Sociology, including posters, idea pitches, autoethnography, reflective assessments and group projects, as well as more conventional essays and exams. Approaches to assessment are increasingly facilitated by digital technologies – for example,\n\n16\npodcasts, videocasts and recorded presentations – and staff and students should be familiar with local institutional policies and developments regarding the integration of technology into teaching and assessment. GenAI represents an opportunity for developing imaginative assessments, making use of its analytical power."
  stem: none
  statementType: expectation
  rung: none
  force: should
  level: none
  appliesTo: "staff and students"
  addressee: both
  verbs: ["be familiar", "used"]
  about: "varied assessment; knowing local policy on technology"
  themes: [none]
  domain: none
  award: ["none"]
  gradeOf: none
  paraphrase: "Many inclusive forms of assessment suit the subject, from posters and autoethnography to essays and exams, and digital forms are growing; staff and students should know their institution's policies on technology in teaching and assessment, and generative AI offers scope for imaginative tasks."
  quote: full   # the issuer's statement is in `source` (D-std-0014)
  audience: both
  subjects: inherited
- id: qaa/sociology-2026/3.20
  locator: { number: "3.20", headingPath: ["Content, structure and delivery", "Assessment"] }
  span: { start: 49896, end: 50095 }
  source: "3.20 Transparency and clear communication are important in assessment, ensuring students are aware of how they will be assessed and for what purpose. The use of clear assessment rubrics is essential."
  stem: none
  statementType: expectation
  rung: none
  force: must   # D-std-0016: "is essential" read as must
  level: none
  appliesTo: "assessment in Sociology"
  addressee: provider
  verbs: ["ensuring", "assessed"]
  about: "transparent assessment and clear rubrics"
  themes: [none]
  domain: none
  award: ["none"]
  gradeOf: none
  paraphrase: "Assessment should be transparent and clearly communicated so students know how and why they are assessed; clear rubrics are called essential."
  quote: full   # the issuer's statement is in `source` (D-std-0014)
  audience: practitioner
  subjects: inherited
- id: qaa/sociology-2026/4.2
  locator: { number: "4.2", headingPath: ["Benchmark standards", "Introduction"] }
  span: { start: 51670, end: 52154 }
  source: "4.2 The vast majority of students will perform significantly better than the minimum threshold standards. Each higher education provider has its own method of determining what appropriate evidence of this achievement will be and should refer to Annex D in The Frameworks for Higher Education Qualifications of UK Degree-Awarding Bodies. This Annex sets out common descriptions of the four main degree outcome classifications for bachelor's degrees with honours: 1st, 2.1, 2.2 and 3rd."
  stem: none
  statementType: expectation
  rung: none
  force: should
  level: fheq:6
  appliesTo: "each higher education provider"
  addressee: provider
  verbs: ["refer", "determining"]
  about: "evidence above threshold; Annex D for classifications"
  themes: [none]
  domain: none
  award: ["bachelor's with honours"]
  gradeOf: none
  paraphrase: "Most students will do much better than the threshold; each provider decides what evidence shows this and should refer to Annex D of the qualification frameworks, which describes the four honours classifications."
  quote: full   # the issuer's statement is in `source` (D-std-0014)
  audience: practitioner
  subjects: inherited
- id: qaa/sociology-2026/4.3
  locator: { number: "4.3", headingPath: ["Benchmark standards", "Introduction"] }
  span: { start: 52155, end: 52648 }
  source: "4.3 Please note that the minimum threshold standards outlined below are not intended to specify universal competence standards for a discipline. If a provider chooses to develop competence standards (as defined by the Equality Act 2010) as part of a programme specification, these can be informed by the relevant Subject Benchmark Statement along with any PSRB requirements. In these circumstances, providers should follow the most recent guidance from the Equality and Human Right Commission."
  stem: none
  statementType: expectation
  rung: none
  force: should
  level: none
  appliesTo: "providers developing competence standards"
  addressee: provider
  verbs: ["follow", "develop"]
  about: "threshold standards are not competence standards; EHRC guidance"
  themes: [none]
  domain: none
  award: ["none"]
  gradeOf: none
  paraphrase: "The threshold standards are not meant as universal competence standards; a provider that sets competence standards under the Equality Act 2010 in a programme specification may draw on this statement and any professional body requirements, and should then follow the latest Equality and Human Rights Commission guidance."
  quote: full   # the issuer's statement is in `source` (D-std-0014)
  audience: practitioner
  subjects: inherited
- id: qaa/sociology-2026/4.4.b1
  locator: { number: "4.4.b1", headingPath: ["Benchmark standards", "Threshold level: Subject knowledge, understanding and skills"] }
  span: { start: 52767, end: 52838 }
  source: "describe and examine a range of key concepts and theoretical approaches"
  stem: "4.4"
  statementType: threshold
  rung: threshold
  force: threshold
  level: fheq:6
  appliesTo: "honours graduates in Sociology"
  addressee: learner
  verbs: ["describe", "examine"]
  about: "key concepts and theoretical approaches"
  themes: [none]
  domain: knowledge
  award: ["bachelor's with honours"]
  gradeOf: none
  paraphrase: "Can set out and look closely at a range of the subject's central concepts and theoretical approaches."
  quote: full   # the issuer's statement is in `source` (D-std-0014)
  audience: both
  subjects: inherited
- id: qaa/sociology-2026/4.4.b2
  locator: { number: "4.4.b2", headingPath: ["Benchmark standards", "Threshold level: Subject knowledge, understanding and skills"] }
  span: { start: 52841, end: 52933 }
  source: "explain how Sociology can be distinguished from other forms of understanding and explanation"
  stem: "4.4"
  statementType: threshold
  rung: threshold
  force: threshold
  level: fheq:6
  appliesTo: "honours graduates in Sociology"
  addressee: learner
  verbs: ["explain", "distinguished"]
  about: "how Sociology differs from other ways of explaining"
  themes: [none]
  domain: understanding
  award: ["bachelor's with honours"]
  gradeOf: none
  paraphrase: "Can say what sets sociological understanding and explanation apart from other kinds."
  quote: full   # the issuer's statement is in `source` (D-std-0014)
  audience: both
  subjects: inherited
- id: qaa/sociology-2026/4.4.b3
  locator: { number: "4.4.b3", headingPath: ["Benchmark standards", "Threshold level: Subject knowledge, understanding and skills"] }
  span: { start: 52936, end: 53089 }
  source: "discuss sociological topics with an appreciation of theory and evidence, responding to current debates and presenting conclusions in a variety of formats"
  stem: "4.4"
  statementType: threshold
  rung: threshold
  force: threshold
  level: fheq:6
  appliesTo: "honours graduates in Sociology"
  addressee: learner
  verbs: ["discuss", "responding", "presenting"]
  about: "discussing topics with theory and evidence, in varied formats"
  themes: [none]
  domain: subject-skill
  award: ["bachelor's with honours"]
  gradeOf: none
  paraphrase: "Can discuss sociological topics drawing on theory and evidence, take part in current debates and present conclusions in different formats."
  quote: full   # the issuer's statement is in `source` (D-std-0014)
  audience: both
  subjects: inherited
- id: qaa/sociology-2026/4.4.b4
  locator: { number: "4.4.b4", headingPath: ["Benchmark standards", "Threshold level: Subject knowledge, understanding and skills"] }
  span: { start: 53092, end: 53172 }
  source: "explain the processes that underpin social change, conflict and social stability"
  stem: "4.4"
  statementType: threshold
  rung: threshold
  force: threshold
  level: fheq:6
  appliesTo: "honours graduates in Sociology"
  addressee: learner
  verbs: ["explain"]
  about: "processes of social change, conflict and stability"
  themes: [none]
  domain: understanding
  award: ["bachelor's with honours"]
  gradeOf: none
  paraphrase: "Can explain the processes behind social change, conflict and stability."
  quote: full   # the issuer's statement is in `source` (D-std-0014)
  audience: both
  subjects: inherited
- id: qaa/sociology-2026/4.4.b5
  locator: { number: "4.4.b5", headingPath: ["Benchmark standards", "Threshold level: Subject knowledge, understanding and skills"] }
  span: { start: 53175, end: 53289 }
  source: "describe the relationship between individuals, groups, social structures, and the natural and physical environment"
  stem: "4.4"
  statementType: threshold
  rung: threshold
  force: threshold
  level: fheq:6
  appliesTo: "honours graduates in Sociology"
  addressee: learner
  verbs: ["describe"]
  about: "individuals, groups, structures and the environment"
  themes: [none]
  domain: knowledge
  award: ["bachelor's with honours"]
  gradeOf: none
  paraphrase: "Can describe how individuals, groups and social structures relate to one another and to the natural and physical environment."
  quote: full   # the issuer's statement is in `source` (D-std-0014)
  audience: both
  subjects: inherited
- id: qaa/sociology-2026/4.4.b6
  locator: { number: "4.4.b6", headingPath: ["Benchmark standards", "Threshold level: Subject knowledge, understanding and skills"] }
  span: { start: 53292, end: 53403 }
  source: "demonstrate awareness of the interconnections of power imbalances, colonial legacies, inequities and injustices"
  stem: "4.4"
  statementType: threshold
  rung: threshold
  force: threshold
  level: fheq:6
  appliesTo: "honours graduates in Sociology"
  addressee: learner
  verbs: ["demonstrate"]
  about: "power, colonial legacies, inequity and injustice"
  themes: [none]
  domain: understanding
  award: ["bachelor's with honours"]
  gradeOf: none
  paraphrase: "Can show awareness of how power imbalances, colonial legacies, inequity and injustice are bound up with one another."
  quote: full   # the issuer's statement is in `source` (D-std-0014)
  audience: both
  subjects: inherited
- id: qaa/sociology-2026/4.4.b7
  locator: { number: "4.4.b7", headingPath: ["Benchmark standards", "Threshold level: Subject knowledge, understanding and skills"] }
  span: { start: 53406, end: 53509 }
  source: "use specialist knowledge of one or more subtopics within Sociology to construct a sociological argument"
  stem: "4.4"
  statementType: threshold
  rung: threshold
  force: threshold
  level: fheq:6
  appliesTo: "honours graduates in Sociology"
  addressee: learner
  verbs: ["use", "construct"]
  about: "specialist knowledge used to build an argument"
  themes: [none]
  domain: subject-skill
  award: ["bachelor's with honours"]
  gradeOf: none
  paraphrase: "Can draw on specialist knowledge of at least one area within the subject to build a sociological argument."
  quote: full   # the issuer's statement is in `source` (D-std-0014)
  audience: both
  subjects: inherited
- id: qaa/sociology-2026/4.4.b8
  locator: { number: "4.4.b8", headingPath: ["Benchmark standards", "Threshold level: Subject knowledge, understanding and skills"] }
  span: { start: 53512, end: 53631 }
  source: "evaluate the use of comparison in Sociology, either looking diachronically across time or synchronically across context"
  stem: "4.4"
  statementType: threshold
  rung: threshold
  force: threshold
  level: fheq:6
  appliesTo: "honours graduates in Sociology"
  addressee: learner
  verbs: ["evaluate", "looking"]
  about: "comparison across time or context"
  themes: [none]
  domain: subject-skill
  award: ["bachelor's with honours"]
  gradeOf: none
  paraphrase: "Can judge how comparison is used in the subject, whether across time or across settings."
  quote: full   # the issuer's statement is in `source` (D-std-0014)
  audience: both
  subjects: inherited
- id: qaa/sociology-2026/4.4.b9
  locator: { number: "4.4.b9", headingPath: ["Benchmark standards", "Threshold level: Subject knowledge, understanding and skills"] }
  span: { start: 53634, end: 53766 }
  source: "understand different sociological perspectives on social diversity and inequality while addressing key dimensions and sites of power"
  stem: "4.4"
  statementType: threshold
  rung: threshold
  force: threshold
  level: fheq:6
  appliesTo: "honours graduates in Sociology"
  addressee: learner
  verbs: ["understand", "addressing"]
  about: "perspectives on diversity, inequality and power"
  themes: [none]
  domain: understanding
  award: ["bachelor's with honours"]
  gradeOf: none
  paraphrase: "Can understand the different sociological perspectives on social diversity and inequality, taking in the main dimensions and sites of power."
  quote: full   # the issuer's statement is in `source` (D-std-0014)
  audience: both
  subjects: inherited
- id: qaa/sociology-2026/4.4.b10
  locator: { number: "4.4.b10", headingPath: ["Benchmark standards", "Threshold level: Subject knowledge, understanding and skills"] }
  span: { start: 53769, end: 53893 }
  source: "analyse quantitative and qualitative data to understand patterns around social inequalities, their concerns and consequences"
  stem: "4.4"
  statementType: threshold
  rung: threshold
  force: threshold
  level: fheq:6
  appliesTo: "honours graduates in Sociology"
  addressee: learner
  verbs: ["analyse", "understand"]
  about: "analysing data on social inequality"
  themes: [none]
  domain: subject-skill
  award: ["bachelor's with honours"]
  gradeOf: none
  paraphrase: "Can analyse quantitative and qualitative data to grasp patterns of social inequality, what drives concern about them and what follows from them."
  quote: full   # the issuer's statement is in `source` (D-std-0014)
  audience: both
  subjects: inherited
- id: qaa/sociology-2026/4.4.b11
  locator: { number: "4.4.b11", headingPath: ["Benchmark standards", "Threshold level: Subject knowledge, understanding and skills"] }
  span: { start: 53896, end: 54087 }
  source: "evaluate complex global and local social problems and the influence of global and local forces promote opportunities to contribute to multi and interdisciplinary approaches to social problems"
  stem: "4.4"
  statementType: threshold
  rung: threshold
  force: threshold
  level: fheq:6
  appliesTo: "honours graduates in Sociology"
  addressee: learner
  verbs: ["evaluate", "promote", "contribute"]
  about: "global and local social problems; interdisciplinary approaches"
  themes: [none]
  domain: subject-skill
  award: ["bachelor's with honours"]
  gradeOf: none
  paraphrase: "Can assess complex social problems at global and local scale and the forces shaping them, and help bring several disciplines to bear on them. The item's wording runs two clauses together (Part E)."
  quote: full   # the issuer's statement is in `source` (D-std-0014)
  audience: both
  subjects: inherited
- id: qaa/sociology-2026/4.4.b12
  locator: { number: "4.4.b12", headingPath: ["Benchmark standards", "Threshold level: Subject knowledge, understanding and skills"] }
  span: { start: 54090, end: 54236 }
  source: "summarise and explain the findings of empirical sociological research, and offer a critical assessment of frameworks, theories and methods adopted"
  stem: "4.4"
  statementType: threshold
  rung: threshold
  force: threshold
  level: fheq:6
  appliesTo: "honours graduates in Sociology"
  addressee: learner
  verbs: ["summarise", "explain", "offer"]
  about: "summarising research and critiquing its frameworks and methods"
  themes: [none]
  domain: subject-skill
  award: ["bachelor's with honours"]
  gradeOf: none
  paraphrase: "Can summarise and explain what empirical sociological research has found, and critically assess the frameworks, theories and methods it used."
  quote: full   # the issuer's statement is in `source` (D-std-0014)
  audience: both
  subjects: inherited
- id: qaa/sociology-2026/4.4.b13
  locator: { number: "4.4.b13", headingPath: ["Benchmark standards", "Threshold level: Subject knowledge, understanding and skills"] }
  span: { start: 54239, end: 54337 }
  source: "evaluate the suitability of a range of research strategies and methods to identify social problems"
  stem: "4.4"
  statementType: threshold
  rung: threshold
  force: threshold
  level: fheq:6
  appliesTo: "honours graduates in Sociology"
  addressee: learner
  verbs: ["evaluate", "identify"]
  about: "choosing research strategies and methods"
  themes: [none]
  domain: subject-skill
  award: ["bachelor's with honours"]
  gradeOf: none
  paraphrase: "Can judge how suitable a range of research strategies and methods are for identifying social problems."
  quote: full   # the issuer's statement is in `source` (D-std-0014)
  audience: both
  subjects: inherited
- id: qaa/sociology-2026/4.4.b14
  locator: { number: "4.4.b14", headingPath: ["Benchmark standards", "Threshold level: Subject knowledge, understanding and skills"] }
  span: { start: 54344, end: 54433 }
  source: "be able to use qualitative and quantitative methodologies in research problems and design"
  stem: "4.4"
  statementType: threshold
  rung: threshold
  force: threshold
  level: fheq:6
  appliesTo: "honours graduates in Sociology"
  addressee: learner
  verbs: ["use"]
  about: "using qualitative and quantitative methodologies in design"
  themes: [none]
  domain: subject-skill
  award: ["bachelor's with honours"]
  gradeOf: none
  paraphrase: "Can use both qualitative and quantitative methodologies in framing and designing research."
  quote: full   # the issuer's statement is in `source` (D-std-0014)
  audience: both
  subjects: inherited
- id: qaa/sociology-2026/4.4.b15
  locator: { number: "4.4.b15", headingPath: ["Benchmark standards", "Threshold level: Subject knowledge, understanding and skills"] }
  span: { start: 54436, end: 54630 }
  source: "use appropriate research tools for the collection and analysis of quantitative and qualitative data, including the use of appropriate software and basic statistical and interpretative procedures"
  stem: "4.4"
  statementType: threshold
  rung: threshold
  force: threshold
  level: fheq:6
  appliesTo: "honours graduates in Sociology"
  addressee: learner
  verbs: ["use"]
  about: "research tools, software and basic statistics"
  themes: [none]
  domain: subject-skill
  award: ["bachelor's with honours"]
  gradeOf: none
  paraphrase: "Can use suitable tools to collect and analyse both numerical and qualitative data, with software and with basic statistical and interpretive procedures."
  quote: full   # the issuer's statement is in `source` (D-std-0014)
  audience: both
  subjects: inherited
- id: qaa/sociology-2026/4.4.b16
  locator: { number: "4.4.b16", headingPath: ["Benchmark standards", "Threshold level: Subject knowledge, understanding and skills"] }
  span: { start: 54633, end: 54718 }
  source: "analyse the ethical implications of social research in a variety of research settings"
  stem: "4.4"
  statementType: threshold
  rung: threshold
  force: threshold
  level: fheq:6
  appliesTo: "honours graduates in Sociology"
  addressee: learner
  verbs: ["analyse"]
  about: "ethics of social research in different settings"
  themes: [none]
  domain: subject-skill
  award: ["bachelor's with honours"]
  gradeOf: none
  paraphrase: "Can analyse the ethical implications of social research across different research settings."
  quote: full   # the issuer's statement is in `source` (D-std-0014)
  audience: both
  subjects: inherited
- id: qaa/sociology-2026/4.4.b17
  locator: { number: "4.4.b17", headingPath: ["Benchmark standards", "Threshold level: Subject knowledge, understanding and skills"] }
  span: { start: 54721, end: 54772 }
  source: "independently plan and complete a Sociology project"
  stem: "4.4"
  statementType: threshold
  rung: threshold
  force: threshold
  level: fheq:6
  appliesTo: "honours graduates in Sociology"
  addressee: learner
  verbs: ["plan", "complete"]
  about: "planning and completing an independent project"
  themes: [none]
  domain: subject-skill
  award: ["bachelor's with honours"]
  gradeOf: none
  paraphrase: "Can plan and finish a Sociology project working independently."
  quote: full   # the issuer's statement is in `source` (D-std-0014)
  audience: both
  subjects: inherited
- id: qaa/sociology-2026/4.4.b18
  locator: { number: "4.4.b18", headingPath: ["Benchmark standards", "Threshold level: Subject knowledge, understanding and skills"] }
  span: { start: 54775, end: 54923 }
  source: "recognise the application of sociological knowledge to social, public, civic and environmental policy and the place and value of sociology in policy"
  stem: "4.4"
  statementType: threshold
  rung: threshold
  force: threshold
  level: fheq:6
  appliesTo: "honours graduates in Sociology"
  addressee: learner
  verbs: ["recognise"]
  about: "sociology applied to policy"
  themes: [none]
  domain: understanding
  award: ["bachelor's with honours"]
  gradeOf: none
  paraphrase: "Can recognise how sociological knowledge bears on policy (social, public, civic and environmental), and the place and worth of the subject in policy."
  quote: full   # the issuer's statement is in `source` (D-std-0014)
  audience: both
  subjects: inherited
- id: qaa/sociology-2026/4.5.b1
  locator: { number: "4.5.b1", headingPath: ["Benchmark standards", "Threshold level: Transferable skills"] }
  span: { start: 55225, end: 55288 }
  source: "undertake and present scholarly work using a variety of formats"
  stem: "4.5"
  statementType: threshold
  rung: threshold
  force: threshold
  level: fheq:6
  appliesTo: "honours graduates in Sociology"
  addressee: learner
  verbs: ["undertake", "present"]
  about: "scholarly work in a range of formats"
  themes: [none]
  domain: generic-skill
  award: ["bachelor's with honours"]
  gradeOf: none
  paraphrase: "Can carry out and present scholarly work in different formats."
  quote: full   # the issuer's statement is in `source` (D-std-0014)
  audience: both
  subjects: inherited
- id: qaa/sociology-2026/4.5.b2
  locator: { number: "4.5.b2", headingPath: ["Benchmark standards", "Threshold level: Transferable skills"] }
  span: { start: 55291, end: 55371 }
  source: "assess the merits of competing explanations and provide evidence-based responses"
  stem: "4.5"
  statementType: threshold
  rung: threshold
  force: threshold
  level: fheq:6
  appliesTo: "honours graduates in Sociology"
  addressee: learner
  verbs: ["assess", "provide"]
  about: "weighing rival explanations; evidence-based responses"
  themes: [none]
  domain: generic-skill
  award: ["bachelor's with honours"]
  gradeOf: none
  paraphrase: "Can weigh competing explanations and respond on the basis of evidence."
  quote: full   # the issuer's statement is in `source` (D-std-0014)
  audience: both
  subjects: inherited
- id: qaa/sociology-2026/4.5.b3
  locator: { number: "4.5.b3", headingPath: ["Benchmark standards", "Threshold level: Transferable skills"] }
  span: { start: 55374, end: 55420 }
  source: "communicate to others in a variety of contexts"
  stem: "4.5"
  statementType: threshold
  rung: threshold
  force: threshold
  level: fheq:6
  appliesTo: "honours graduates in Sociology"
  addressee: learner
  verbs: ["communicate"]
  about: "communicating in different contexts"
  themes: [none]
  domain: generic-skill
  award: ["bachelor's with honours"]
  gradeOf: none
  paraphrase: "Can communicate with other people in a range of settings."
  quote: full   # the issuer's statement is in `source` (D-std-0014)
  audience: both
  subjects: inherited
- id: qaa/sociology-2026/4.5.b4
  locator: { number: "4.5.b4", headingPath: ["Benchmark standards", "Threshold level: Transferable skills"] }
  span: { start: 55423, end: 55501 }
  source: "use digital technology and digital skills when organising and presenting ideas"
  stem: "4.5"
  statementType: threshold
  rung: threshold
  force: threshold
  level: fheq:6
  appliesTo: "honours graduates in Sociology"
  addressee: learner
  verbs: ["use"]
  about: "digital skills for organising and presenting ideas"
  themes: [none]
  domain: generic-skill
  award: ["bachelor's with honours"]
  gradeOf: none
  paraphrase: "Can use digital technology and skills to organise and present ideas."
  quote: full   # the issuer's statement is in `source` (D-std-0014)
  audience: both
  subjects: inherited
- id: qaa/sociology-2026/4.5.b5
  locator: { number: "4.5.b5", headingPath: ["Benchmark standards", "Threshold level: Transferable skills"] }
  span: { start: 55504, end: 55566 }
  source: "demonstrate information retrieval and synthesis of information"
  stem: "4.5"
  statementType: threshold
  rung: threshold
  force: threshold
  level: fheq:6
  appliesTo: "honours graduates in Sociology"
  addressee: learner
  verbs: ["demonstrate"]
  about: "retrieving and synthesising information"
  themes: [none]
  domain: generic-skill
  award: ["bachelor's with honours"]
  gradeOf: none
  paraphrase: "Can show skill in finding information and drawing it together."
  quote: full   # the issuer's statement is in `source` (D-std-0014)
  audience: both
  subjects: inherited
- id: qaa/sociology-2026/4.5.b6
  locator: { number: "4.5.b6", headingPath: ["Benchmark standards", "Threshold level: Transferable skills"] }
  span: { start: 55569, end: 55634 }
  source: "discuss and present ideas with others in a clear and reasoned way"
  stem: "4.5"
  statementType: threshold
  rung: threshold
  force: threshold
  level: fheq:6
  appliesTo: "honours graduates in Sociology"
  addressee: learner
  verbs: ["discuss", "present"]
  about: "clear, reasoned discussion with others"
  themes: [none]
  domain: generic-skill
  award: ["bachelor's with honours"]
  gradeOf: none
  paraphrase: "Can discuss and present ideas with other people clearly and with reasons."
  quote: full   # the issuer's statement is in `source` (D-std-0014)
  audience: both
  subjects: inherited
- id: qaa/sociology-2026/4.5.b7
  locator: { number: "4.5.b7", headingPath: ["Benchmark standards", "Threshold level: Transferable skills"] }
  span: { start: 55637, end: 55701 }
  source: "demonstrate the ability to work independently and work in groups"
  stem: "4.5"
  statementType: threshold
  rung: threshold
  force: threshold
  level: fheq:6
  appliesTo: "honours graduates in Sociology"
  addressee: learner
  verbs: ["demonstrate", "work"]
  about: "working alone and in groups"
  themes: [none]
  domain: generic-skill
  award: ["bachelor's with honours"]
  gradeOf: none
  paraphrase: "Can show the ability to work both independently and in groups."
  quote: full   # the issuer's statement is in `source` (D-std-0014)
  audience: both
  subjects: inherited
- id: qaa/sociology-2026/4.5.b8
  locator: { number: "4.5.b8", headingPath: ["Benchmark standards", "Threshold level: Transferable skills"] }
  span: { start: 55704, end: 55782 }
  source: "understand how to apply research principles and practices in an ethical manner"
  stem: "4.5"
  statementType: threshold
  rung: threshold
  force: threshold
  level: fheq:6
  appliesTo: "honours graduates in Sociology"
  addressee: learner
  verbs: ["understand", "apply"]
  about: "applying research principles ethically"
  themes: [none]
  domain: generic-skill
  award: ["bachelor's with honours"]
  gradeOf: none
  paraphrase: "Can understand how to put research principles and practices into effect ethically."
  quote: full   # the issuer's statement is in `source` (D-std-0014)
  audience: both
  subjects: inherited
- id: qaa/sociology-2026/4.5.b9
  locator: { number: "4.5.b9", headingPath: ["Benchmark standards", "Threshold level: Transferable skills"] }
  span: { start: 55785, end: 55926 }
  source: "appropriately use artificial intelligence and other digital technologies, including Generative AI, and critically evaluate their implications"
  stem: "4.5"
  statementType: threshold
  rung: threshold
  force: threshold
  level: fheq:6
  appliesTo: "honours graduates in Sociology"
  addressee: learner
  verbs: ["use", "evaluate"]
  about: "using and evaluating AI and digital technology, including generative AI"
  themes: [none]
  domain: generic-skill
  award: ["bachelor's with honours"]
  gradeOf: none
  paraphrase: "Can use artificial intelligence and other digital technologies, generative AI among them, appropriately, and evaluate their implications critically."
  quote: full   # the issuer's statement is in `source` (D-std-0014)
  audience: both
  subjects: inherited
- id: qaa/sociology-2026/4.5.b10
  locator: { number: "4.5.b10", headingPath: ["Benchmark standards", "Threshold level: Transferable skills"] }
  span: { start: 55929, end: 56003 }
  source: "present knowledge or an argument in a way that is comprehensible to others"
  stem: "4.5"
  statementType: threshold
  rung: threshold
  force: threshold
  level: fheq:6
  appliesTo: "honours graduates in Sociology"
  addressee: learner
  verbs: ["present"]
  about: "making knowledge and argument understandable"
  themes: [none]
  domain: generic-skill
  award: ["bachelor's with honours"]
  gradeOf: none
  paraphrase: "Can present knowledge or an argument so that others can follow it."
  quote: full   # the issuer's statement is in `source` (D-std-0014)
  audience: both
  subjects: inherited
- id: qaa/sociology-2026/4.5.b11
  locator: { number: "4.5.b11", headingPath: ["Benchmark standards", "Threshold level: Transferable skills"] }
  span: { start: 56006, end: 56193 }
  source: "assert intellectual independence, including undertaking tasks independently (with appropriate guidance and support), conducting self-directed research and demonstrating critical judgement"
  stem: "4.5"
  statementType: threshold
  rung: threshold
  force: threshold
  level: fheq:6
  appliesTo: "honours graduates in Sociology"
  addressee: learner
  verbs: ["assert", "undertaking", "conducting", "demonstrating"]
  about: "intellectual independence and critical judgement"
  themes: [none]
  domain: generic-skill
  award: ["bachelor's with honours"]
  gradeOf: none
  paraphrase: "Can show intellectual independence: working on tasks alone with suitable support, carrying out self-directed research and exercising critical judgement."
  quote: full   # the issuer's statement is in `source` (D-std-0014)
  audience: both
  subjects: inherited
- id: qaa/sociology-2026/4.5.b12
  locator: { number: "4.5.b12", headingPath: ["Benchmark standards", "Threshold level: Transferable skills"] }
  span: { start: 56196, end: 56296 }
  source: "use computer-aided techniques for storing, collating and analysing quantitative and qualitative data"
  stem: "4.5"
  statementType: threshold
  rung: threshold
  force: threshold
  level: fheq:6
  appliesTo: "honours graduates in Sociology"
  addressee: learner
  verbs: ["use"]
  about: "computer-aided data storage and analysis"
  themes: [none]
  domain: generic-skill
  award: ["bachelor's with honours"]
  gradeOf: none
  paraphrase: "Can use computer-based techniques to store, collate and analyse quantitative and qualitative data."
  quote: full   # the issuer's statement is in `source` (D-std-0014)
  audience: both
  subjects: inherited
- id: qaa/sociology-2026/4.5.b13
  locator: { number: "4.5.b13", headingPath: ["Benchmark standards", "Threshold level: Transferable skills"] }
  span: { start: 56299, end: 56402 }
  source: "work collaboratively, including undertaking work in a group or team and/or participating in discussions"
  stem: "4.5"
  statementType: threshold
  rung: threshold
  force: threshold
  level: fheq:6
  appliesTo: "honours graduates in Sociology"
  addressee: learner
  verbs: ["work"]
  about: "collaborative work in teams and discussion"
  themes: [none]
  domain: generic-skill
  award: ["bachelor's with honours"]
  gradeOf: none
  paraphrase: "Can work collaboratively, in a group or team or by taking part in discussion."
  quote: full   # the issuer's statement is in `source` (D-std-0014)
  audience: both
  subjects: inherited
- id: qaa/sociology-2026/4.5.b14
  locator: { number: "4.5.b14", headingPath: ["Benchmark standards", "Threshold level: Transferable skills"] }
  span: { start: 56405, end: 56512 }
  source: "identify and examine underlying values and ethics within culture and society as well as on a personal level"
  stem: "4.5"
  statementType: threshold
  rung: threshold
  force: threshold
  level: fheq:6
  appliesTo: "honours graduates in Sociology"
  addressee: learner
  verbs: ["identify", "examine"]
  about: "values and ethics in culture, society and self"
  themes: [none]
  domain: generic-skill
  award: ["bachelor's with honours"]
  gradeOf: none
  paraphrase: "Can identify and examine the values and ethics beneath culture and society and in one's own life."
  quote: full   # the issuer's statement is in `source` (D-std-0014)
  audience: both
  subjects: inherited
- id: qaa/sociology-2026/4.5.b15
  locator: { number: "4.5.b15", headingPath: ["Benchmark standards", "Threshold level: Transferable skills"] }
  span: { start: 56515, end: 56620 }
  source: "understand the importance of wellbeing, mental health and emotions – and their relationship with learning"
  stem: "4.5"
  statementType: threshold
  rung: threshold
  force: threshold
  level: fheq:6
  appliesTo: "honours graduates in Sociology"
  addressee: learner
  verbs: ["understand"]
  about: "wellbeing, emotions and learning"
  themes: [none]
  domain: generic-skill
  award: ["bachelor's with honours"]
  gradeOf: none
  paraphrase: "Can understand why wellbeing, mental health and emotions matter and how they bear on learning."
  quote: full   # the issuer's statement is in `source` (D-std-0014)
  audience: both
  subjects: inherited
- id: qaa/sociology-2026/4.5.b16
  locator: { number: "4.5.b16", headingPath: ["Benchmark standards", "Threshold level: Transferable skills"] }
  span: { start: 56623, end: 56706 }
  source: "make appropriate use of feedback provided to further their intellectual development"
  stem: "4.5"
  statementType: threshold
  rung: threshold
  force: threshold
  level: fheq:6
  appliesTo: "honours graduates in Sociology"
  addressee: learner
  verbs: ["make"]
  about: "using feedback for development"
  themes: [none]
  domain: generic-skill
  award: ["bachelor's with honours"]
  gradeOf: none
  paraphrase: "Can make good use of feedback to further intellectual development."
  quote: full   # the issuer's statement is in `source` (D-std-0014)
  audience: both
  subjects: inherited
- id: qaa/sociology-2026/4.6.b1.masters
  locator: { number: "4.6.b1.masters", headingPath: ["Benchmark standards", "Master's level study"] }
  span: { start: 56880, end: 56982 }
  source: "synthesise theoretical, conceptual and empirical research when discussing contemporary social problems"
  stem: "4.6"
  statementType: threshold
  rung: threshold
  force: should
  level: fheq:7
  appliesTo: "master's graduates in Sociology"
  addressee: learner
  verbs: ["synthesise"]
  about: "synthesising theory, concepts and empirical research on current problems"
  themes: [none]
  domain: subject-skill
  award: ["master's"]
  gradeOf: none
  paraphrase: "Should bring theoretical, conceptual and empirical research together when discussing present-day social problems."
  quote: full   # the issuer's statement is in `source` (D-std-0014)
  audience: both
  subjects: inherited
- id: qaa/sociology-2026/4.6.b2.masters
  locator: { number: "4.6.b2.masters", headingPath: ["Benchmark standards", "Master's level study"] }
  span: { start: 56985, end: 57134 }
  source: "demonstrate critical awareness of historical, cultural, social, political and environmental contexts and theories that inform and influence Sociology"
  stem: "4.6"
  statementType: threshold
  rung: threshold
  force: should
  level: fheq:7
  appliesTo: "master's graduates in Sociology"
  addressee: learner
  verbs: ["demonstrate", "inform", "influence"]
  about: "critical awareness of the contexts and theories behind the subject"
  themes: [none]
  domain: knowledge
  award: ["master's"]
  gradeOf: none
  paraphrase: "Should show critical awareness of the theories, and the historical, cultural, social, political and environmental settings, that shape the subject."
  quote: full   # the issuer's statement is in `source` (D-std-0014)
  audience: both
  subjects: inherited
- id: qaa/sociology-2026/4.6.b3.masters
  locator: { number: "4.6.b3.masters", headingPath: ["Benchmark standards", "Master's level study"] }
  span: { start: 57137, end: 57254 }
  source: "critically discuss the interconnections and overlaps of power imbalance, colonial legacies, inequities and injustices"
  stem: "4.6"
  statementType: threshold
  rung: threshold
  force: should
  level: fheq:7
  appliesTo: "master's graduates in Sociology"
  addressee: learner
  verbs: ["discuss"]
  about: "critical discussion of power, colonial legacies and injustice"
  themes: [none]
  domain: understanding
  award: ["master's"]
  gradeOf: none
  paraphrase: "Should discuss critically how power imbalance, colonial legacies, inequity and injustice connect and overlap."
  quote: full   # the issuer's statement is in `source` (D-std-0014)
  audience: both
  subjects: inherited
- id: qaa/sociology-2026/4.6.b4.masters
  locator: { number: "4.6.b4.masters", headingPath: ["Benchmark standards", "Master's level study"] }
  span: { start: 57261, end: 57351 }
  source: "design and carry out sociological research using both quantitative and qualitative sources"
  stem: "4.6"
  statementType: threshold
  rung: threshold
  force: should
  level: fheq:7
  appliesTo: "master's graduates in Sociology"
  addressee: learner
  verbs: ["design", "carry"]
  about: "designing and carrying out research with both kinds of source"
  themes: [none]
  domain: subject-skill
  award: ["master's"]
  gradeOf: none
  paraphrase: "Should design and conduct sociological research drawing on quantitative and qualitative sources."
  quote: full   # the issuer's statement is in `source` (D-std-0014)
  audience: both
  subjects: inherited
- id: qaa/sociology-2026/4.6.b5.masters
  locator: { number: "4.6.b5.masters", headingPath: ["Benchmark standards", "Master's level study"] }
  span: { start: 57354, end: 57431 }
  source: "critically assess appropriate methodologies for dealing with complex problems"
  stem: "4.6"
  statementType: threshold
  rung: threshold
  force: should
  level: fheq:7
  appliesTo: "master's graduates in Sociology"
  addressee: learner
  verbs: ["assess"]
  about: "assessing methodologies for complex problems"
  themes: [none]
  domain: subject-skill
  award: ["master's"]
  gradeOf: none
  paraphrase: "Should critically judge which methodologies suit complex problems."
  quote: full   # the issuer's statement is in `source` (D-std-0014)
  audience: both
  subjects: inherited
- id: qaa/sociology-2026/4.6.b6.masters
  locator: { number: "4.6.b6.masters", headingPath: ["Benchmark standards", "Master's level study"] }
  span: { start: 57434, end: 57492 }
  source: "discuss sensitive and ethical issues in Sociology research"
  stem: "4.6"
  statementType: threshold
  rung: threshold
  force: should
  level: fheq:7
  appliesTo: "master's graduates in Sociology"
  addressee: learner
  verbs: ["discuss"]
  about: "sensitive and ethical issues in research"
  themes: [none]
  domain: subject-skill
  award: ["master's"]
  gradeOf: none
  paraphrase: "Should discuss the sensitive and ethical questions that sociological research raises."
  quote: full   # the issuer's statement is in `source` (D-std-0014)
  audience: both
  subjects: inherited
- id: qaa/sociology-2026/4.6.b7.masters
  locator: { number: "4.6.b7.masters", headingPath: ["Benchmark standards", "Master's level study"] }
  span: { start: 57495, end: 57676 }
  source: "select and use appropriate research tools for collection and/or analysis of quantitative and qualitative data, including software and basic statistical and interpretative procedures"
  stem: "4.6"
  statementType: threshold
  rung: threshold
  force: should
  level: fheq:7
  appliesTo: "master's graduates in Sociology"
  addressee: learner
  verbs: ["select", "use"]
  about: "selecting and using research tools, software and statistics"
  themes: [none]
  domain: subject-skill
  award: ["master's"]
  gradeOf: none
  paraphrase: "Should choose and use suitable tools to gather or analyse quantitative and qualitative data, with software and basic statistical and interpretive procedures."
  quote: full   # the issuer's statement is in `source` (D-std-0014)
  audience: both
  subjects: inherited
- id: qaa/sociology-2026/4.6.b8.masters
  locator: { number: "4.6.b8.masters", headingPath: ["Benchmark standards", "Master's level study"] }
  span: { start: 57679, end: 57776 }
  source: "critically discuss and analyse complex concepts, and work independently and with some originality"
  stem: "4.6"
  statementType: threshold
  rung: threshold
  force: should
  level: fheq:7
  appliesTo: "master's graduates in Sociology"
  addressee: learner
  verbs: ["discuss", "analyse", "work"]
  about: "complex concepts; independent work with some originality"
  themes: [none]
  domain: subject-skill
  award: ["master's"]
  gradeOf: none
  paraphrase: "Should discuss and analyse complex concepts critically and work independently with a degree of originality. The item joins a subject skill and a generic one (Part E)."
  quote: full   # the issuer's statement is in `source` (D-std-0014)
  audience: both
  subjects: inherited
- id: qaa/sociology-2026/4.6.b9.masters
  locator: { number: "4.6.b9.masters", headingPath: ["Benchmark standards", "Master's level study"] }
  span: { start: 57779, end: 57914 }
  source: "complete a research project, involving the generation of reformulation of data, and informed by a critical understanding of the subject"
  stem: "4.6"
  statementType: threshold
  rung: threshold
  force: should
  level: fheq:7
  appliesTo: "master's graduates in Sociology"
  addressee: learner
  verbs: ["complete", "informed"]
  about: "completing a research project with original or reworked data"
  themes: [none]
  domain: subject-skill
  award: ["master's"]
  gradeOf: none
  paraphrase: "Should complete a research project that generates or reformulates data and rests on a critical understanding of the subject. The item reads 'generation of reformulation', most likely a slip for 'or' (Part E)."
  quote: full   # the issuer's statement is in `source` (D-std-0014)
  audience: both
  subjects: inherited
- id: qaa/sociology-2026/4.6.b10.masters
  locator: { number: "4.6.b10.masters", headingPath: ["Benchmark standards", "Master's level study"] }
  span: { start: 57917, end: 58023 }
  source: "critically evaluate social policies and interventions by applying social theories, frameworks and evidence"
  stem: "4.6"
  statementType: threshold
  rung: threshold
  force: should
  level: fheq:7
  appliesTo: "master's graduates in Sociology"
  addressee: learner
  verbs: ["evaluate", "applying"]
  about: "evaluating policies and interventions with theory and evidence"
  themes: [none]
  domain: subject-skill
  award: ["master's"]
  gradeOf: none
  paraphrase: "Should evaluate social policies and interventions critically, using social theory, frameworks and evidence."
  quote: full   # the issuer's statement is in `source` (D-std-0014)
  audience: both
  subjects: inherited
```

### S4a Audience versions
<!-- label: both; status: drafted; basis: primary. forPractitioner: for the programme designer or teacher. forBeneficiary: for the student, second person, naming no issuer. author-agent-written: instructions to an AI agent writing about the statement (a course document, a handbook, an outcome, a report). author-agent-dialogue: instructions to an AI agent using the statement in conversation (with a student, a teacher or a programme team). Written fresh from the held text alone (benchmark rule 6; Abbott, 15:42). -->
```yaml
- statement: qaa/sociology-2026/1.6
  forPractitioner: { text: "Make equality, diversity and inclusion part of the curriculum itself, not an add-on: the subject reads inequality as structural, and the statement expects this of every course.", rewrite: light, force: describes, status: drafted }
  forBeneficiary: { text: "not-applicable: an expectation of the course; the student meets its effect in what is taught", rewrite: full, force: describes, status: drafted }
  author-agent-written: "Describe this as an expectation the statement places on every Sociology course, not a duty in law and not an outcome a student is graded on; its obliging word is 'expectation', recorded here as describes. Cite it as (QAA, 2026, Sociology Subject Benchmark Statement, para 1.6). Set it beside 1.7, 1.8 and the honours items that carry the theme, 4.4.b6 and 4.4.b9, and do not claim it names particular content."
  author-agent-dialogue: "Raise it with a programme team that is reviewing where equality, diversity and inclusion sit in the curriculum. Frame it for staff as a course-level expectation and ask: in which modules do students meet structural accounts of inequality, and is that by design or by chance? Do not put it to a student as something they must do."
- statement: qaa/sociology-2026/1.7
  forPractitioner: { text: "Treat the legal duty of fair, non-discriminatory treatment as the floor and go past it: consider the diversity of your students in curriculum design, content, teaching, assessment and feedback so that every student can succeed.", rewrite: light, force: must, status: drafted }
  forBeneficiary: { text: "not-applicable: a legal duty on the institution, reported by the statement", rewrite: full, force: must, status: drafted }
  author-agent-written: "Present this as the statement's report of a legal duty on institutions (fair treatment and no discrimination), with a wider expectation of inclusion across the student journey. Cite it as (QAA, 2026, Sociology Subject Benchmark Statement, para 1.7) and name the legislation only as the statement does, without adding sections or cases. Do not turn it into a duty on students. Set it beside 1.6, 1.8 and the competence-standards note in 4.3."
  author-agent-dialogue: "Use it when staff ask whether inclusion is a legal matter or good practice: it is both, and the law is the minimum. Ask the team where in the student journey (design, delivery, assessment, feedback) inclusion is weakest now. Avoid giving legal advice; point to the institution's own equality office for that."
- statement: qaa/sociology-2026/1.8
  forPractitioner: { text: "Support students to handle contested topics with evidence in a safe, inclusive space; keep resources accessible and responsive; widen the curriculum so students question theories that have dominated; and, wherever possible, make sure every student is treated with equal respect in every setting the course uses.", rewrite: light, force: should, status: drafted }
  forBeneficiary: { text: "not-applicable: a set of duties on the course team and institution", rewrite: full, force: should, status: drafted }
  author-agent-written: "Write of this as a should-level expectation on course teams and institutions about how contested topics are taught and how inclusion is kept up, with 'wherever possible' qualifying the duty on settings. Cite it as (QAA, 2026, Sociology Subject Benchmark Statement, para 1.8). Do not state it as a student outcome or as a legal requirement. Set it beside 1.6, 1.7 and the honours item on power and colonial legacies, 4.4.b6."
  author-agent-dialogue: "Raise it when a team plans modules on sensitive topics or prepares placements and trips. Ask staff how students are helped to disagree with evidence and respect, and how the team would know if a student felt unsafe or unequally treated in an off-campus setting. Do not frame it to students as a rule they must keep."
- statement: qaa/sociology-2026/1.9
  forPractitioner: { text: "Design accessibility in from the outset so that teaching, assessment, activities and fieldtrips work for disabled students without each having to request an adjustment.", rewrite: light, force: should, status: drafted }
  forBeneficiary: { text: "not-applicable: a duty on course design and delivery", rewrite: full, force: should, status: drafted }
  author-agent-written: "Describe this as a should-level expectation that accessibility is designed into a course rather than added through individual requests. Cite it as (QAA, 2026, Sociology Subject Benchmark Statement, para 1.9) and do not present it as the full legal duty, which the statement leaves to legislation (front matter). Set it beside 1.10, 1.12, 3.14 and 3.21."
  author-agent-dialogue: "Bring it up when a team reviews a module or assessment that relies on individual adjustments. Ask: which parts of this module would a disabled student still have to ask to have changed, and could the design remove that need? Keep it with staff; it is not a student's task."
- statement: qaa/sociology-2026/1.10
  forPractitioner: { text: "Make the course flexible and accessible across admissions, resources, fieldwork and group work, with adjustments built into the design so no disabled student is singled out.", rewrite: light, force: should, status: drafted }
  forBeneficiary: { text: "not-applicable: a duty on the course", rewrite: full, force: should, status: drafted }
  author-agent-written: "Present this as a should-level expectation on Sociology courses about flexibility and built-in adjustments. Cite it as (QAA, 2026, Sociology Subject Benchmark Statement, para 1.10). Do not claim it sets admissions criteria. Set it beside 1.9 and 1.12."
  author-agent-dialogue: "Use it with a team planning fieldwork, fieldtrips or group tasks. Ask how a disabled student would take part in each without being singled out, and what would have to change in the design. Do not give it to a student as a requirement on them."
- statement: qaa/sociology-2026/1.12
  forPractitioner: { text: "Keep materials digitally accessible, make rooms and study spaces accessible, use language that does not treat disabled people as the object of study, and value approaches that draw on their lived experience.", rewrite: light, force: should, status: drafted }
  forBeneficiary: { text: "not-applicable: a duty on the course and its spaces", rewrite: full, force: should, status: drafted }
  author-agent-written: "Write of this as a should-level expectation on access while studying: digital materials, physical spaces and the language used about disability. Cite it as (QAA, 2026, Sociology Subject Benchmark Statement, para 1.12). Do not widen it into a statement about admissions, which is 1.11. Set it beside 1.9, 1.10 and the EDI paragraph 1.8."
  author-agent-dialogue: "Raise it when staff review learning materials, rooms or reading lists that discuss disability. Ask whether any material positions disabled people as a topic rather than as participants, and whether blended materials work with assistive tools. Avoid putting this duty to students."
- statement: qaa/sociology-2026/1.18
  forPractitioner: { text: "Let education for sustainable development shape how you teach and assess, not only what you teach; the three-fold frame of the national ESD guidance can help, as can co-created, problem-based projects with outside partners.", rewrite: light, force: should, status: drafted }
  forBeneficiary: { text: "not-applicable: a duty on curriculum, teaching and assessment design", rewrite: full, force: should, status: drafted }
  author-agent-written: "Present this as a should-level expectation that ESD runs through curriculum, teaching and assessment, with the three-fold frame offered as a may, not a must. Cite it as (QAA, 2026, Sociology Subject Benchmark Statement, para 1.18) and point to std:doc:qaa-advancehe-esd-2021-guidance for the frame, without copying it. Set it beside 1.13 to 1.17 and the honours item on society and environment, 4.4.b5."
  author-agent-dialogue: "Raise it when a team maps sustainability only to content. Ask: where do students practise acting on sustainability, not only reading about it, and does any assessment ask them to? Do not present the guidance's frame as compulsory."
- statement: qaa/sociology-2026/1.21.b1
  forPractitioner: { text: "Bring in guest lecturers from other countries as one way of internationalising teaching.", rewrite: light, force: should, status: drafted }
  forBeneficiary: { text: "not-applicable: a route the course should take; not a student standard", rewrite: full, force: should, status: drafted }
  author-agent-written: "Record this as one of five routes through which the statement says internationalisation should be pursued; the should sits in the stem of 1.21, not in this item. Cite it as (QAA, 2026, Sociology Subject Benchmark Statement, para 1.21). Set it beside the other four routes (1.21.b2 to 1.21.b5) and 1.19."
  author-agent-dialogue: "Raise it when a team asks how to internationalise beyond the reading list. Ask the team which of the five routes the course uses now and which it could add. Do not treat any single route as required on its own; the duty is the stem's."
- statement: qaa/sociology-2026/1.21.b2
  forPractitioner: { text: "Promote student mobility, such as field trips, a period of study abroad or an international placement.", rewrite: light, force: should, status: drafted }
  forBeneficiary: { text: "not-applicable: a route the course should take; not a student standard", rewrite: full, force: should, status: drafted }
  author-agent-written: "Record this as the mobility route among the five in 1.21, under the stem's should. Cite it as (QAA, 2026, Sociology Subject Benchmark Statement, para 1.21). Do not claim that the statement requires a year abroad. Set it beside 1.21.b1 to 1.21.b5 and the accessibility expectations 1.9 and 1.10, since mobility must stay open to all."
  author-agent-dialogue: "Raise it when a team plans trips, exchanges or placements abroad. Ask the team which of the five routes the course uses now and which it could add. Do not treat any single route as required on its own; the duty is the stem's."
- statement: qaa/sociology-2026/1.21.b3
  forPractitioner: { text: "Explore partnerships with institutions in the Global South to give students real engagement with other sociological standpoints.", rewrite: light, force: should, status: drafted }
  forBeneficiary: { text: "not-applicable: a route the course should take; not a student standard", rewrite: full, force: should, status: drafted }
  author-agent-written: "Record this as the partnership route among the five in 1.21, under the stem's should, and keep its verb, explore: it asks for exploration, not a set partnership. Cite it as (QAA, 2026, Sociology Subject Benchmark Statement, para 1.21). Set it beside 1.20 and the honours item on colonial legacies, 4.4.b6."
  author-agent-dialogue: "Raise it when a team discusses decolonising or widening the curriculum. Ask the team which of the five routes the course uses now and which it could add. Do not treat any single route as required on its own; the duty is the stem's."
- statement: qaa/sociology-2026/1.21.b4
  forPractitioner: { text: "Treat the varied cultural backgrounds of your students as a resource for alternative sociological standpoints.", rewrite: light, force: should, status: drafted }
  forBeneficiary: { text: "not-applicable: a route the course should take; not a student standard", rewrite: full, force: should, status: drafted }
  author-agent-written: "Record this as the route through students' own backgrounds among the five in 1.21, under the stem's should. Cite it as (QAA, 2026, Sociology Subject Benchmark Statement, para 1.21). Set it beside 1.24 and 1.25, which develop the same idea."
  author-agent-dialogue: "Raise it when a team asks how to draw on a diverse cohort. Ask the team which of the five routes the course uses now and which it could add. Do not treat any single route as required on its own; the duty is the stem's."
- statement: qaa/sociology-2026/1.21.b5
  forPractitioner: { text: "Promote Collaborative Online International Learning (shared online work with students in other countries).", rewrite: light, force: should, status: drafted }
  forBeneficiary: { text: "not-applicable: a route the course should take; not a student standard", rewrite: full, force: should, status: drafted }
  author-agent-written: "Record this as the online collaboration route among the five in 1.21, under the stem's should. Cite it as (QAA, 2026, Sociology Subject Benchmark Statement, para 1.21) and give the approach its own name as the statement does. Set it beside 1.21.b2, the physical mobility route."
  author-agent-dialogue: "Raise it when mobility abroad is out of reach for many students. Ask the team which of the five routes the course uses now and which it could add. Do not treat any single route as required on its own; the duty is the stem's."
- statement: qaa/sociology-2026/1.25
  forPractitioner: { text: "If you aim to internationalise, teach in a way that values what students already know, for instance through dialogue that lets them see themselves as rightful contributors to knowledge.", rewrite: light, force: must, status: drafted }
  forBeneficiary: { text: "not-applicable: a condition on teaching practice", rewrite: full, force: must, status: drafted }
  author-agent-written: "Present this as a condition the statement attaches to internationalisation: it 'requires' teaching that values students' knowledge, recorded here as must, though it is a condition of the aim rather than a rule in law (Part E). Cite it as (QAA, 2026, Sociology Subject Benchmark Statement, para 1.25). Set it beside 1.21.b4 and 1.24."
  author-agent-dialogue: "Raise it when a team reflects on who speaks in seminars and whose knowledge counts. Ask: how does your teaching invite students to bring their own knowledge in, and how would they know it is valued? Do not put it to students as their duty."
- statement: qaa/sociology-2026/1.33
  forPractitioner: { text: "Work with careers staff, alumni, social enterprises and employers to plan and deliver EEE education, using visiting speakers, master classes or client briefs with career tasks built around them.", rewrite: light, force: should, status: drafted }
  forBeneficiary: { text: "not-applicable: a duty on course teams", rewrite: full, force: should, status: drafted }
  author-agent-written: "Describe this as a should-level expectation on course teams to collaborate on employability, enterprise and entrepreneurship education; the forms named after it are examples (may). Cite it as (QAA, 2026, Sociology Subject Benchmark Statement, para 1.33) and point to std:doc:qaa-enterprise-2018-guidance for the wider guidance. Set it beside 1.31, 1.32 and the capabilities in 1.34."
  author-agent-dialogue: "Raise it when a team plans careers content or employer links. Ask who outside the department helps design the course's employability work now, and which of the named forms could fit. Do not present the examples as required."
- statement: qaa/sociology-2026/1.40
  forPractitioner: { text: "Encourage students to use AI tools critically: what they make easier, and what goes missing when human talk and creativity are handed over, including the risk of erasing marginalised voices.", rewrite: light, force: should, status: drafted }
  forBeneficiary: { text: "You should be encouraged to use new AI tools critically, asking both what they help you do and what is lost when they replace human dialogue and creativity, including whose voices go missing.", rewrite: full, force: should, status: drafted }
  author-agent-written: "Present this as a should-level expectation that students are encouraged to engage critically with generative AI, within teaching that stays rooted in the discipline's questions. Cite it as (QAA, 2026, Sociology Subject Benchmark Statement, para 1.40). Do not claim it permits or bans any tool; 1.41 leaves that to institutional policy. Set it beside 1.35 to 1.41 and the transferable skill 4.5.b9."
  author-agent-dialogue: "Raise it when a student or teacher asks how to use AI in their work. With a student, use plain second-person words and ask: what did the tool do for you here, and what might it have left out or flattened? With staff, ask where the course invites that reflection. Avoid treating this as a rule about permitted use."
- statement: qaa/sociology-2026/2.1
  forPractitioner: { text: "Design the course so students build the skills to analyse how institutions and structures mould human agency and are moulded by it, and to connect global, community and personal levels of social life; the statement expects this of students.", rewrite: light, force: must, status: drafted }
  forBeneficiary: { text: "You are expected to build the skills to examine how social structures and institutions shape people's actions and are shaped by them, and to understand social life from the global to the personal and how these levels link.", rewrite: full, force: must, status: drafted }
  author-agent-written: "Present this as an expectation of what students develop on a Sociology honours course; its obliging words are 'expected to', recorded here as describes, so do not raise it to a threshold. Cite it as (QAA, 2026, Sociology Subject Benchmark Statement, para 2.1). Set it beside the threshold items 4.4.b5 and 4.4.b4 and the FHEQ level 6 descriptor qaa/fheq-2024/4.15.b1."
  author-agent-dialogue: "Raise it when a student asks what the degree is really about or a team states the course's aims. With a student, ask: can you give an example where a structure shaped what people did, and where people changed a structure? With staff, ask which modules link the global and the personal. Do not present it as a pass requirement."
- statement: qaa/sociology-2026/2.3
  forPractitioner: { text: "By the end of the programme, students should be able to say what makes Sociology distinct, in standpoint, explanation, levels of analysis, theory and evidence, and where it overlaps with neighbouring subjects.", rewrite: light, force: should, status: drafted }
  forBeneficiary: { text: "By the end of your studies you should be able to explain what makes Sociology different from neighbouring subjects, in how it explains, the levels it works at and how it uses theory and evidence, and what it has in common with them.", rewrite: full, force: should, status: drafted }
  author-agent-written: "Present this as a should-level outcome for students at the end of a programme, stated outside the threshold lists but close to threshold item 4.4.b2. Cite it as (QAA, 2026, Sociology Subject Benchmark Statement, para 2.3). Do not list the neighbouring subjects as required combinations. Set it beside 4.4.b2 and the FHEQ level 6 descriptor qaa/fheq-2024/4.15.b1."
  author-agent-dialogue: "Raise it with a joint honours student or anyone unsure how Sociology differs from Psychology, Social Policy or Politics. Ask: if a psychologist and a sociologist studied the same problem, how would their questions differ? Avoid reading the list of subjects aloud."
- statement: qaa/sociology-2026/2.7
  forPractitioner: { text: "Joint and combined honours students will achieve the core of the statement's subject and generic skills, not necessarily all of them, and will add skills from their other subject.", rewrite: light, force: will, status: drafted }
  forBeneficiary: { text: "If you study Sociology alongside another subject, you will gain the core of its subject and general skills and add skills from your other subject, with room to explore where the two overlap.", rewrite: full, force: will, status: drafted }
  author-agent-written: "Present this as a will-level statement that joint and combined honours students achieve core elements, not the whole, of the skills in 4.4 and 4.5. Cite it as (QAA, 2026, Sociology Subject Benchmark Statement, para 2.7). Do not claim the statement says which elements are core; it does not. Set it beside 4.4 and 4.5 and the FHEQ level 6 descriptor qaa/fheq-2024/4.15.b1."
  author-agent-dialogue: "Raise it when a joint honours student or a joint programme team asks which standards apply. With a student, ask: which of your skills come from Sociology and which from your other subject? With staff, ask how the course decides what is core. Avoid implying that joint students meet every item."
- statement: qaa/sociology-2026/2.9
  forPractitioner: { text: "Use a range of flexible teaching, learning and assessment styles that reflect the varied needs of your students; the statement expects this of every course whatever its orientation.", rewrite: light, force: will, status: drafted }
  forBeneficiary: { text: "not-applicable: an expectation of courses", rewrite: full, force: will, status: drafted }
  author-agent-written: "Describe this as a will-level expectation on all courses to value varied and flexible teaching, while leaving each department its own approach. Cite it as (QAA, 2026, Sociology Subject Benchmark Statement, para 2.9). Do not claim it prescribes methods; the front matter says the statement does not. Set it beside 3.8, 3.9 and 3.11."
  author-agent-dialogue: "Raise it when a team relies on one teaching or assessment form. Ask how the course's mix serves students with different learning needs. Do not give it to students as their duty."
- statement: qaa/sociology-2026/2.15
  forPractitioner: { text: "Include external reviewers in periodic review to get an independent view of proposed changes and to confirm that threshold standards are met and content fits the subject.", rewrite: light, force: will, status: drafted }
  forBeneficiary: { text: "not-applicable: a provider duty in quality assurance", rewrite: full, force: will, status: drafted }
  author-agent-written: "Describe this as a will-level statement of provider practice in periodic review, part of the statement's account of externality. Cite it as (QAA, 2026, Sociology Subject Benchmark Statement, para 2.15). Do not present it as a new rule from this statement; it describes sector arrangements. Set it beside 2.14, 2.16 and the threshold lists 4.4 and 4.5."
  author-agent-dialogue: "Raise it with a programme team preparing for periodic review. Ask which threshold items the external reviewer will be asked to confirm and what evidence the team holds for each. Keep it away from students."
- statement: qaa/sociology-2026/3.11.b1
  forPractitioner: { text: "Give students room to try out theory, and scaffold and revisit that work at every level of the course.", rewrite: light, force: should, status: drafted }
  forBeneficiary: { text: "not-applicable: a duty on the design of teaching", rewrite: full, force: should, status: drafted }
  author-agent-written: "Present this as a should-level expectation on how teaching handles theory across the levels of a course. Cite it as (QAA, 2026, Sociology Subject Benchmark Statement, para 3.11). Set it beside the threshold item on concepts and theory, 4.4.b1, and the FHEQ level 6 descriptor qaa/fheq-2024/4.15.b3.1."
  author-agent-dialogue: "Raise it when a team maps theory teaching across years. Ask where students first try out a theory themselves and where they come back to it with more depth. Do not put it to a student as a duty."
- statement: qaa/sociology-2026/3.11.b4
  forPractitioner: { text: "Draw on knowledge and theory from across the world so students see how some perspectives are valued above others; students should be able to explain the effects of colonial legacies now.", rewrite: light, force: should, status: drafted }
  forBeneficiary: { text: "You should be able to explain how colonial histories still shape the world today, and why some knowledge and viewpoints are valued more than others.", rewrite: full, force: should, status: drafted }
  author-agent-written: "Present this as a should-level student outcome stated within the teaching section, outside the threshold lists, which carry a related item (4.4.b6). Cite it as (QAA, 2026, Sociology Subject Benchmark Statement, para 3.11). Do not claim it as a separate threshold standard. Set it beside 4.4.b6 and, for master's, 4.6.b3.masters."
  author-agent-dialogue: "Raise it when a student meets decolonial readings or asks why the reading list has changed. Ask: can you name one way a colonial history shapes something you studied this year? With staff, ask where students practise this. Avoid lecturing; let the student give the example."
- statement: qaa/sociology-2026/3.12
  forPractitioner: { text: "Explain clearly to students how assessment of learning differs from assessment for learning and why both matter.", rewrite: light, force: should, status: drafted }
  forBeneficiary: { text: "not-applicable: a duty on staff to explain; the student receives it", rewrite: full, force: should, status: drafted }
  author-agent-written: "Present this as a should-level expectation on staff to explain the two purposes of assessment to students. Cite it as (QAA, 2026, Sociology Subject Benchmark Statement, para 3.12). Set it beside 3.8 (formative opportunities) and 3.20 (transparency)."
  author-agent-dialogue: "Raise it when students seem to ignore formative tasks. Ask the team how and when students are told what each task is for. Do not present it to students as their responsibility."
- statement: qaa/sociology-2026/3.14
  forPractitioner: { text: "Design assessment with equality and diversity in mind so it is accessible from the start, consider giving students a choice of approach, and review assessments regularly.", rewrite: light, force: should, status: drafted }
  forBeneficiary: { text: "not-applicable: a duty on assessment design", rewrite: full, force: should, status: drafted }
  author-agent-written: "Present this as a should-level expectation on assessment design and review, joining the EDI and accessibility themes. Cite it as (QAA, 2026, Sociology Subject Benchmark Statement, para 3.14). Do not claim it requires assessment choice; choice is offered as one effective means. Set it beside 1.9, 1.10 and 3.21."
  author-agent-dialogue: "Raise it when a team reviews an assessment strategy or sees attainment gaps. Ask: which students does this task disadvantage, and when was it last reviewed? Do not give it to students as their duty."
- statement: qaa/sociology-2026/3.15
  forPractitioner: { text: "Use a wide range of inclusive assessment forms, including digital ones, and make sure staff and students know the institution's policies on technology in teaching and assessment.", rewrite: light, force: should, status: drafted }
  forBeneficiary: { text: "You should know your institution's rules on using technology, including AI tools, in your learning and assessment, and expect to be assessed in many forms, from posters and podcasts to essays and exams.", rewrite: full, force: should, status: drafted }
  author-agent-written: "Present this as a should-level expectation that both staff and students know local policy on technology in assessment, set within a description of varied assessment forms. Cite it as (QAA, 2026, Sociology Subject Benchmark Statement, para 3.15). Do not state what any policy allows; the statement leaves that to the institution (1.41). Set it beside 1.41 and 3.21."
  author-agent-dialogue: "Raise it when a student is unsure whether a tool is allowed in an assignment. With a student, ask: have you read your institution's guidance on this, and does the brief say anything? With staff, ask where the policy is shown to students. Avoid giving your own ruling on what is permitted."
- statement: qaa/sociology-2026/3.20
  forPractitioner: { text: "Tell students how and why they will be assessed and give them clear rubrics; the statement calls these essential.", rewrite: light, force: must, status: drafted }
  forBeneficiary: { text: "not-applicable: a duty on assessment practice", rewrite: full, force: must, status: drafted }
  author-agent-written: "Describe this as an expectation of transparent assessment with clear rubrics; its obliging words are 'important' and 'essential', recorded here as describes (Part E). Cite it as (QAA, 2026, Sociology Subject Benchmark Statement, para 3.20). Set it beside 3.12 and 3.21.b2."
  author-agent-dialogue: "Raise it when students say they do not know what a task wants. Ask the team whether each brief carries a rubric students can read before they start. Keep the duty with staff."
- statement: qaa/sociology-2026/4.2
  forPractitioner: { text: "Use your own method for judging achievement above the threshold, and refer to Annex D of the UK qualification frameworks, which describes first, upper second, lower second and third class honours.", rewrite: light, force: should, status: drafted }
  forBeneficiary: { text: "not-applicable: a duty on the provider in classifying degrees", rewrite: full, force: should, status: drafted }
  author-agent-written: "Present this as a should-level duty on providers to refer to Annex D when judging achievement above the threshold; this statement itself sets no rung above threshold. Cite it as (QAA, 2026, Sociology Subject Benchmark Statement, para 4.2) and point to Annex D as std:doc:qaa-fheq-2024-framework, qaa/fheq-2024/annex-d/summary, without copying it. Do not claim the statement defines the classes."
  author-agent-dialogue: "Raise it when a team writes classification criteria or a student asks what a first needs. With staff, ask how the course's marking criteria line up with Annex D. With a student, say plainly that the subject's lists set a minimum and that the institution's criteria describe the classes. Avoid presenting the threshold lists as a description of a good degree."
- statement: qaa/sociology-2026/4.3
  forPractitioner: { text: "Do not treat the threshold lists as competence standards; if you set competence standards in a programme specification, draw on the statement if useful and follow the Equality and Human Rights Commission's current guidance.", rewrite: light, force: should, status: drafted }
  forBeneficiary: { text: "not-applicable: a duty on the provider", rewrite: full, force: should, status: drafted }
  author-agent-written: "Present this as a should-level duty on providers that choose to set competence standards, and as the statement's own warning that its threshold items are not competence standards. Cite it as (QAA, 2026, Sociology Subject Benchmark Statement, para 4.3). Never describe items 4.4 to 4.6 as competence standards. Set it beside 1.7 and the threshold lists 4.4 and 4.5."
  author-agent-dialogue: "Raise it when a team writes competence standards or a student asks about reasonable adjustments to outcomes. With staff, ask whether any outcome is being used as a competence standard and whether the current EHRC guidance was followed. Avoid giving legal advice."
- statement: qaa/sociology-2026/4.4.b1
  forPractitioner: { text: "At threshold, honours graduates should be able to set out and examine a range of central concepts and theoretical approaches.", rewrite: light, force: threshold, status: drafted }
  forBeneficiary: { text: "By the end of your degree you should be able to explain and look critically at a range of the main ideas and theories in Sociology.", rewrite: full, force: threshold, status: drafted }
  author-agent-written: "State this as a threshold standard: the least an honours graduate in Sociology should have shown, at FHEQ level 6 (FQHEIS level 10), here key concepts and theoretical approaches. Cite it as (QAA, 2026, Sociology Subject Benchmark Statement, para 4.4) and do not call it a regulatory rule, a competence standard (4.3) or a master's expectation. Set it beside qaa/fheq-2024/4.15.b1, spine:6 and the master's item 4.6.b2.masters; the statement gives no typical or excellent rung, so take classification language from Annex D, not from this item."
  author-agent-dialogue: "Raise it when a student is preparing for a theory exam or a team checks first-year coverage. Put it to a student in plain words as something they should be able to do by the end of the degree, and to staff as a floor every route through the course should let students reach. Ask: which two or three theoretical approaches could you describe and compare without notes? Do not read the list aloud or treat it as the mark of a good degree; it is the minimum."
- statement: qaa/sociology-2026/4.4.b2
  forPractitioner: { text: "At threshold, honours graduates should be able to explain what distinguishes sociological explanation from other ways of understanding the social world.", rewrite: light, force: threshold, status: drafted }
  forBeneficiary: { text: "By the end of your degree you should be able to explain what makes a sociological explanation different from other ways of making sense of the world.", rewrite: full, force: threshold, status: drafted }
  author-agent-written: "State this as a threshold standard: the least an honours graduate in Sociology should have shown, at FHEQ level 6 (FQHEIS level 10), here how Sociology differs from other ways of explaining. Cite it as (QAA, 2026, Sociology Subject Benchmark Statement, para 4.4) and do not call it a regulatory rule, a competence standard (4.3) or a master's expectation. Set it beside qaa/fheq-2024/4.15.b1, spine:6 and 2.3; the statement gives no typical or excellent rung, so take classification language from Annex D, not from this item."
  author-agent-dialogue: "Raise it when a student asks how Sociology differs from common sense or from another subject. Put it to a student in plain words as something they should be able to do by the end of the degree, and to staff as a floor every route through the course should let students reach. Ask: how would a sociological explanation of this event differ from an everyday one? Do not read the list aloud or treat it as the mark of a good degree; it is the minimum."
- statement: qaa/sociology-2026/4.4.b3
  forPractitioner: { text: "At threshold, honours graduates should be able to discuss sociological topics with theory and evidence, engage with current debates and present conclusions in several formats.", rewrite: light, force: threshold, status: drafted }
  forBeneficiary: { text: "By the end of your degree you should be able to discuss sociological topics using theory and evidence, join current debates and present your conclusions in different formats.", rewrite: full, force: threshold, status: drafted }
  author-agent-written: "State this as a threshold standard: the least an honours graduate in Sociology should have shown, at FHEQ level 6 (FQHEIS level 10), here discussing topics with theory and evidence, in varied formats. Cite it as (QAA, 2026, Sociology Subject Benchmark Statement, para 4.4) and do not call it a regulatory rule, a competence standard (4.3) or a master's expectation. Set it beside qaa/fheq-2024/4.15.b3.1 and qaa/fheq-2024/4.15.b8, spine:6 and the transferable skill 4.5.b1; the statement gives no typical or excellent rung, so take classification language from Annex D, not from this item."
  author-agent-dialogue: "Raise it when a student plans a presentation or essay on a live debate. Put it to a student in plain words as something they should be able to do by the end of the degree, and to staff as a floor every route through the course should let students reach. Ask: where in your argument do theory and evidence each do work, and how would the format change for a different audience? Do not read the list aloud or treat it as the mark of a good degree; it is the minimum."
- statement: qaa/sociology-2026/4.4.b4
  forPractitioner: { text: "At threshold, honours graduates should be able to explain the processes beneath social change, conflict and stability.", rewrite: light, force: threshold, status: drafted }
  forBeneficiary: { text: "By the end of your degree you should be able to explain what drives social change and conflict, and what keeps societies stable.", rewrite: full, force: threshold, status: drafted }
  author-agent-written: "State this as a threshold standard: the least an honours graduate in Sociology should have shown, at FHEQ level 6 (FQHEIS level 10), here processes of social change, conflict and stability. Cite it as (QAA, 2026, Sociology Subject Benchmark Statement, para 4.4) and do not call it a regulatory rule, a competence standard (4.3) or a master's expectation. Set it beside qaa/fheq-2024/4.15.b1, spine:6 and the content area 3.3 and 2.1; the statement gives no typical or excellent rung, so take classification language from Annex D, not from this item."
  author-agent-dialogue: "Raise it when a student studies social change or a team maps content on conflict and order. Put it to a student in plain words as something they should be able to do by the end of the degree, and to staff as a floor every route through the course should let students reach. Ask: can you explain one process that drives change and one that holds a society stable? Do not read the list aloud or treat it as the mark of a good degree; it is the minimum."
- statement: qaa/sociology-2026/4.4.b5
  forPractitioner: { text: "At threshold, honours graduates should be able to describe how individuals, groups and social structures relate to each other and to the natural and physical environment.", rewrite: light, force: threshold, status: drafted }
  forBeneficiary: { text: "By the end of your degree you should be able to describe how people, groups and social structures relate to one another and to the natural and built world.", rewrite: full, force: threshold, status: drafted }
  author-agent-written: "State this as a threshold standard: the least an honours graduate in Sociology should have shown, at FHEQ level 6 (FQHEIS level 10), here individuals, groups, structures and the environment. Cite it as (QAA, 2026, Sociology Subject Benchmark Statement, para 4.4) and do not call it a regulatory rule, a competence standard (4.3) or a master's expectation. Set it beside qaa/fheq-2024/4.15.b1, spine:6 and 2.1 and the ESD paragraph 1.18; the statement gives no typical or excellent rung, so take classification language from Annex D, not from this item."
  author-agent-dialogue: "Raise it when a student links personal life to wider structures or to environmental questions. Put it to a student in plain words as something they should be able to do by the end of the degree, and to staff as a floor every route through the course should let students reach. Ask: how does one structure you have studied shape both people and their relation to the natural world? Do not read the list aloud or treat it as the mark of a good degree; it is the minimum."
- statement: qaa/sociology-2026/4.4.b6
  forPractitioner: { text: "At threshold, honours graduates should be able to show awareness of how power imbalances, colonial legacies, inequities and injustices connect.", rewrite: light, force: threshold, status: drafted }
  forBeneficiary: { text: "By the end of your degree you should be able to show you are aware of how unequal power, colonial histories and injustice are linked.", rewrite: full, force: threshold, status: drafted }
  author-agent-written: "State this as a threshold standard: the least an honours graduate in Sociology should have shown, at FHEQ level 6 (FQHEIS level 10), here power, colonial legacies, inequity and injustice. Cite it as (QAA, 2026, Sociology Subject Benchmark Statement, para 4.4) and do not call it a regulatory rule, a competence standard (4.3) or a master's expectation. Set it beside qaa/fheq-2024/4.15.b4, spine:6 and the master's item 4.6.b3.masters and 3.11.b4; the statement gives no typical or excellent rung, so take classification language from Annex D, not from this item."
  author-agent-dialogue: "Raise it when a student meets work on race, empire or global inequality. Put it to a student in plain words as something they should be able to do by the end of the degree, and to staff as a floor every route through the course should let students reach. Ask: can you trace one link between a colonial history and an inequality you see now? Do not read the list aloud or treat it as the mark of a good degree; it is the minimum."
- statement: qaa/sociology-2026/4.4.b7
  forPractitioner: { text: "At threshold, honours graduates should be able to use specialist knowledge of one or more sub-areas to construct a sociological argument.", rewrite: light, force: threshold, status: drafted }
  forBeneficiary: { text: "By the end of your degree you should be able to use your specialist knowledge of at least one area of Sociology to build an argument.", rewrite: full, force: threshold, status: drafted }
  author-agent-written: "State this as a threshold standard: the least an honours graduate in Sociology should have shown, at FHEQ level 6 (FQHEIS level 10), here specialist knowledge used to build an argument. Cite it as (QAA, 2026, Sociology Subject Benchmark Statement, para 4.4) and do not call it a regulatory rule, a competence standard (4.3) or a master's expectation. Set it beside qaa/fheq-2024/4.15.b3.1, spine:6 and 4.4.b3; the statement gives no typical or excellent rung, so take classification language from Annex D, not from this item."
  author-agent-dialogue: "Raise it when a student chooses a dissertation topic or option modules. Put it to a student in plain words as something they should be able to do by the end of the degree, and to staff as a floor every route through the course should let students reach. Ask: which part of the subject do you know best, and what argument could you build from it? Do not read the list aloud or treat it as the mark of a good degree; it is the minimum."
- statement: qaa/sociology-2026/4.4.b8
  forPractitioner: { text: "At threshold, honours graduates should be able to evaluate the use of comparison, over time (diachronic) or across contexts (synchronic).", rewrite: light, force: threshold, status: drafted }
  forBeneficiary: { text: "By the end of your degree you should be able to judge how well comparison works in Sociology, whether you compare across time or across places.", rewrite: full, force: threshold, status: drafted }
  author-agent-written: "State this as a threshold standard: the least an honours graduate in Sociology should have shown, at FHEQ level 6 (FQHEIS level 10), here comparison across time or context. Cite it as (QAA, 2026, Sociology Subject Benchmark Statement, para 4.4) and do not call it a regulatory rule, a competence standard (4.3) or a master's expectation. Set it beside qaa/fheq-2024/4.15.b7, spine:6 and 4.4.b11; the statement gives no typical or excellent rung, so take classification language from Annex D, not from this item."
  author-agent-dialogue: "Raise it when a student designs a comparative or historical study. Put it to a student in plain words as something they should be able to do by the end of the degree, and to staff as a floor every route through the course should let students reach. Ask: what does your comparison let you see that a single case would hide, and what does it miss? Do not read the list aloud or treat it as the mark of a good degree; it is the minimum."
- statement: qaa/sociology-2026/4.4.b9
  forPractitioner: { text: "At threshold, honours graduates should be able to understand the range of sociological perspectives on diversity and inequality and address the main dimensions and sites of power.", rewrite: light, force: threshold, status: drafted }
  forBeneficiary: { text: "By the end of your degree you should understand the different sociological views of diversity and inequality and the main places where power operates.", rewrite: full, force: threshold, status: drafted }
  author-agent-written: "State this as a threshold standard: the least an honours graduate in Sociology should have shown, at FHEQ level 6 (FQHEIS level 10), here perspectives on diversity, inequality and power. Cite it as (QAA, 2026, Sociology Subject Benchmark Statement, para 4.4) and do not call it a regulatory rule, a competence standard (4.3) or a master's expectation. Set it beside qaa/fheq-2024/4.15.b1, spine:6 and the EDI paragraphs 1.6 to 1.8 and 4.4.b6; the statement gives no typical or excellent rung, so take classification language from Annex D, not from this item."
  author-agent-dialogue: "Raise it when a student studies class, gender, ethnicity or other divisions. Put it to a student in plain words as something they should be able to do by the end of the degree, and to staff as a floor every route through the course should let students reach. Ask: which perspectives on inequality have you compared, and where do they disagree about power? Do not read the list aloud or treat it as the mark of a good degree; it is the minimum."
- statement: qaa/sociology-2026/4.4.b10
  forPractitioner: { text: "At threshold, honours graduates should be able to analyse quantitative and qualitative data to understand patterns in social inequalities and their consequences.", rewrite: light, force: threshold, status: drafted }
  forBeneficiary: { text: "By the end of your degree you should be able to analyse numbers and qualitative material to find patterns of inequality and what they lead to.", rewrite: full, force: threshold, status: drafted }
  author-agent-written: "State this as a threshold standard: the least an honours graduate in Sociology should have shown, at FHEQ level 6 (FQHEIS level 10), here analysing data on social inequality. Cite it as (QAA, 2026, Sociology Subject Benchmark Statement, para 4.4) and do not call it a regulatory rule, a competence standard (4.3) or a master's expectation. Set it beside qaa/fheq-2024/4.15.b2, spine:6 and the master's item 4.6.b7.masters and 4.4.b15; the statement gives no typical or excellent rung, so take classification language from Annex D, not from this item."
  author-agent-dialogue: "Raise it when a student meets a dataset or interview material about inequality. Put it to a student in plain words as something they should be able to do by the end of the degree, and to staff as a floor every route through the course should let students reach. Ask: what pattern of inequality does your data show, and what would you need to know to explain it? Do not read the list aloud or treat it as the mark of a good degree; it is the minimum."
- statement: qaa/sociology-2026/4.4.b11
  forPractitioner: { text: "At threshold, honours graduates should be able to judge complex social problems, global and local, and the forces at work, and contribute to multi- and interdisciplinary approaches.", rewrite: light, force: threshold, status: drafted }
  forBeneficiary: { text: "By the end of your degree you should be able to assess complex social problems, local and global, and the forces behind them, and help other subjects work on them with you.", rewrite: full, force: threshold, status: drafted }
  author-agent-written: "State this as a threshold standard: the least an honours graduate in Sociology should have shown, at FHEQ level 6 (FQHEIS level 10), here global and local social problems; interdisciplinary approaches. Cite it as (QAA, 2026, Sociology Subject Benchmark Statement, para 4.4) and do not call it a regulatory rule, a competence standard (4.3) or a master's expectation. Set it beside qaa/fheq-2024/4.15.b7, spine:6 and 4.4.b8 and the internationalisation paragraphs 1.19 to 1.26; the statement gives no typical or excellent rung, so take classification language from Annex D, not from this item."
  author-agent-dialogue: "Raise it when a student works on a global issue or with students from other disciplines. Put it to a student in plain words as something they should be able to do by the end of the degree, and to staff as a floor every route through the course should let students reach. Ask: how do global and local forces each shape the problem you are studying, and what could another discipline add? Do not read the list aloud or treat it as the mark of a good degree; it is the minimum."
- statement: qaa/sociology-2026/4.4.b12
  forPractitioner: { text: "At threshold, honours graduates should be able to summarise and explain empirical findings and give a critical assessment of the frameworks, theories and methods behind them.", rewrite: light, force: threshold, status: drafted }
  forBeneficiary: { text: "By the end of your degree you should be able to sum up and explain what sociological research has found, and judge critically the theories and methods it used.", rewrite: full, force: threshold, status: drafted }
  author-agent-written: "State this as a threshold standard: the least an honours graduate in Sociology should have shown, at FHEQ level 6 (FQHEIS level 10), here summarising research and critiquing its frameworks and methods. Cite it as (QAA, 2026, Sociology Subject Benchmark Statement, para 4.4) and do not call it a regulatory rule, a competence standard (4.3) or a master's expectation. Set it beside qaa/fheq-2024/4.15.b3.2, spine:6 and the master's item 4.6.b1.masters; the statement gives no typical or excellent rung, so take classification language from Annex D, not from this item."
  author-agent-dialogue: "Raise it when a student writes a literature review. Put it to a student in plain words as something they should be able to do by the end of the degree, and to staff as a floor every route through the course should let students reach. Ask: can you sum up this study in three sentences, and say what its method could not show? Do not read the list aloud or treat it as the mark of a good degree; it is the minimum."
- statement: qaa/sociology-2026/4.4.b13
  forPractitioner: { text: "At threshold, honours graduates should be able to evaluate how well a range of research strategies and methods suit the identification of social problems.", rewrite: light, force: threshold, status: drafted }
  forBeneficiary: { text: "By the end of your degree you should be able to judge which research approaches and methods suit the social problem you want to study.", rewrite: full, force: threshold, status: drafted }
  author-agent-written: "State this as a threshold standard: the least an honours graduate in Sociology should have shown, at FHEQ level 6 (FQHEIS level 10), here choosing research strategies and methods. Cite it as (QAA, 2026, Sociology Subject Benchmark Statement, para 4.4) and do not call it a regulatory rule, a competence standard (4.3) or a master's expectation. Set it beside qaa/fheq-2024/4.15.b2, spine:6 and the master's item 4.6.b5.masters and 4.4.b14; the statement gives no typical or excellent rung, so take classification language from Annex D, not from this item."
  author-agent-dialogue: "Raise it when a student chooses a method for a project. Put it to a student in plain words as something they should be able to do by the end of the degree, and to staff as a floor every route through the course should let students reach. Ask: why is this method better suited to your question than the obvious alternative? Do not read the list aloud or treat it as the mark of a good degree; it is the minimum."
- statement: qaa/sociology-2026/4.4.b14
  forPractitioner: { text: "At threshold, honours graduates should be able to draw on qualitative and quantitative methodologies when framing problems and designing research.", rewrite: light, force: threshold, status: drafted }
  forBeneficiary: { text: "By the end of your degree you should be able to use both qualitative and quantitative approaches when you frame and design research.", rewrite: full, force: threshold, status: drafted }
  author-agent-written: "State this as a threshold standard: the least an honours graduate in Sociology should have shown, at FHEQ level 6 (FQHEIS level 10), here using qualitative and quantitative methodologies in design. Cite it as (QAA, 2026, Sociology Subject Benchmark Statement, para 4.4) and do not call it a regulatory rule, a competence standard (4.3) or a master's expectation. Set it beside qaa/fheq-2024/4.15.b2 and qaa/fheq-2024/4.15.b6, spine:6 and the master's item 4.6.b4.masters; the statement gives no typical or excellent rung, so take classification language from Annex D, not from this item."
  author-agent-dialogue: "Raise it when a student drafts a research design. Put it to a student in plain words as something they should be able to do by the end of the degree, and to staff as a floor every route through the course should let students reach. Ask: where does your design use numbers, where words or images, and why? Do not read the list aloud or treat it as the mark of a good degree; it is the minimum."
- statement: qaa/sociology-2026/4.4.b15
  forPractitioner: { text: "At threshold, honours graduates should be able to use suitable tools for gathering and analysing both kinds of data, including software and basic statistical and interpretive techniques.", rewrite: light, force: threshold, status: drafted }
  forBeneficiary: { text: "By the end of your degree you should be able to use the right tools to gather and analyse numerical and qualitative data, including software and basic statistics.", rewrite: full, force: threshold, status: drafted }
  author-agent-written: "State this as a threshold standard: the least an honours graduate in Sociology should have shown, at FHEQ level 6 (FQHEIS level 10), here research tools, software and basic statistics. Cite it as (QAA, 2026, Sociology Subject Benchmark Statement, para 4.4) and do not call it a regulatory rule, a competence standard (4.3) or a master's expectation. Set it beside qaa/fheq-2024/4.15.b2, spine:6 and the master's item 4.6.b7.masters and the transferable skill 4.5.b12; the statement gives no typical or excellent rung, so take classification language from Annex D, not from this item."
  author-agent-dialogue: "Raise it when a student prepares to collect or analyse data. Put it to a student in plain words as something they should be able to do by the end of the degree, and to staff as a floor every route through the course should let students reach. Ask: which software and which basic statistical or interpretive procedures could you use on your own data now? Do not read the list aloud or treat it as the mark of a good degree; it is the minimum."
- statement: qaa/sociology-2026/4.4.b16
  forPractitioner: { text: "At threshold, honours graduates should be able to analyse the ethical implications of social research in varied settings.", rewrite: light, force: threshold, status: drafted }
  forBeneficiary: { text: "By the end of your degree you should be able to work through the ethical questions social research raises in different settings.", rewrite: full, force: threshold, status: drafted }
  author-agent-written: "State this as a threshold standard: the least an honours graduate in Sociology should have shown, at FHEQ level 6 (FQHEIS level 10), here ethics of social research in different settings. Cite it as (QAA, 2026, Sociology Subject Benchmark Statement, para 4.4) and do not call it a regulatory rule, a competence standard (4.3) or a master's expectation. Set it beside qaa/fheq-2024/4.15.b7, spine:6 and the master's item 4.6.b6.masters and the transferable skill 4.5.b8; the statement gives no typical or excellent rung, so take classification language from Annex D, not from this item."
  author-agent-dialogue: "Raise it when a student seeks ethical approval or meets a sensitive setting. Put it to a student in plain words as something they should be able to do by the end of the degree, and to staff as a floor every route through the course should let students reach. Ask: what ethical risks does your setting raise that a different setting would not? Do not read the list aloud or treat it as the mark of a good degree; it is the minimum."
- statement: qaa/sociology-2026/4.4.b17
  forPractitioner: { text: "At threshold, honours graduates should be able to plan and complete a Sociology project on their own.", rewrite: light, force: threshold, status: drafted }
  forBeneficiary: { text: "By the end of your degree you should be able to plan and complete a Sociology project of your own.", rewrite: full, force: threshold, status: drafted }
  author-agent-written: "State this as a threshold standard: the least an honours graduate in Sociology should have shown, at FHEQ level 6 (FQHEIS level 10), here planning and completing an independent project. Cite it as (QAA, 2026, Sociology Subject Benchmark Statement, para 4.4) and do not call it a regulatory rule, a competence standard (4.3) or a master's expectation. Set it beside qaa/fheq-2024/4.15.b6 and qaa/fheq-2024/4.15.b5, spine:6 and the master's item 4.6.b9.masters and the transferable skill 4.5.b11; the statement gives no typical or excellent rung, so take classification language from Annex D, not from this item."
  author-agent-dialogue: "Raise it when a student begins a dissertation or independent project. Put it to a student in plain words as something they should be able to do by the end of the degree, and to staff as a floor every route through the course should let students reach. Ask: what is your plan from question to write-up, and which parts will you manage on your own? Do not read the list aloud or treat it as the mark of a good degree; it is the minimum."
- statement: qaa/sociology-2026/4.4.b18
  forPractitioner: { text: "At threshold, honours graduates should be able to recognise how sociological knowledge is applied to social, public, civic and environmental policy and what the subject contributes there.", rewrite: light, force: threshold, status: drafted }
  forBeneficiary: { text: "By the end of your degree you should be able to see how sociological knowledge is used in social, public and environmental policy and why it matters there.", rewrite: full, force: threshold, status: drafted }
  author-agent-written: "State this as a threshold standard: the least an honours graduate in Sociology should have shown, at FHEQ level 6 (FQHEIS level 10), here sociology applied to policy. Cite it as (QAA, 2026, Sociology Subject Benchmark Statement, para 4.4) and do not call it a regulatory rule, a competence standard (4.3) or a master's expectation. Set it beside qaa/fheq-2024/4.15.b9.2, spine:6 and the master's item 4.6.b10.masters; the statement gives no typical or excellent rung, so take classification language from Annex D, not from this item."
  author-agent-dialogue: "Raise it when a student asks how the subject is used outside academia. Put it to a student in plain words as something they should be able to do by the end of the degree, and to staff as a floor every route through the course should let students reach. Ask: which policy area could your work inform, and how? Do not read the list aloud or treat it as the mark of a good degree; it is the minimum."
- statement: qaa/sociology-2026/4.5.b1
  forPractitioner: { text: "At threshold, honours graduates should be able to undertake scholarly work and present it in several formats.", rewrite: light, force: threshold, status: drafted }
  forBeneficiary: { text: "By the end of your degree you should be able to carry out academic work and present it in different formats.", rewrite: full, force: threshold, status: drafted }
  author-agent-written: "State this as a transferable skill the statement places among the honours threshold standards, at FHEQ level 6 (FQHEIS level 10): scholarly work in a range of formats. Cite it as (QAA, 2026, Sociology Subject Benchmark Statement, para 4.5) and do not present it as subject-specific, as a regulatory requirement or as a master's outcome. Set it beside the generic level descriptor qaa/fheq-2024/4.15.b8, the Annex D transferable strand qaa/fheq-2024/annex-d/transferable, spine:6 and 4.4.b3."
  author-agent-dialogue: "Raise it when a student meets a new assessment format. With a student, use plain second-person words and frame it as a skill employers and further study value; with staff, ask where the course teaches and assesses it. Ask: which formats have you produced scholarly work in, and which is weakest? Avoid reading the list aloud or treating it as a higher rung; it is part of the minimum."
- statement: qaa/sociology-2026/4.5.b2
  forPractitioner: { text: "At threshold, honours graduates should be able to assess rival explanations and give responses grounded in evidence.", rewrite: light, force: threshold, status: drafted }
  forBeneficiary: { text: "By the end of your degree you should be able to weigh up competing explanations and respond using evidence.", rewrite: full, force: threshold, status: drafted }
  author-agent-written: "State this as a transferable skill the statement places among the honours threshold standards, at FHEQ level 6 (FQHEIS level 10): weighing rival explanations; evidence-based responses. Cite it as (QAA, 2026, Sociology Subject Benchmark Statement, para 4.5) and do not present it as subject-specific, as a regulatory requirement or as a master's outcome. Set it beside the generic level descriptor qaa/fheq-2024/4.15.b7, the Annex D transferable strand qaa/fheq-2024/annex-d/transferable, spine:6 and 4.4.b12."
  author-agent-dialogue: "Raise it when a student faces competing accounts of the same issue. With a student, use plain second-person words and frame it as a skill employers and further study value; with staff, ask where the course teaches and assesses it. Ask: which explanation does the evidence favour here, and what would change your mind? Avoid reading the list aloud or treating it as a higher rung; it is part of the minimum."
- statement: qaa/sociology-2026/4.5.b3
  forPractitioner: { text: "At threshold, honours graduates should be able to communicate with others across varied contexts.", rewrite: light, force: threshold, status: drafted }
  forBeneficiary: { text: "By the end of your degree you should be able to communicate well with different people in different settings.", rewrite: full, force: threshold, status: drafted }
  author-agent-written: "State this as a transferable skill the statement places among the honours threshold standards, at FHEQ level 6 (FQHEIS level 10): communicating in different contexts. Cite it as (QAA, 2026, Sociology Subject Benchmark Statement, para 4.5) and do not present it as subject-specific, as a regulatory requirement or as a master's outcome. Set it beside the generic level descriptor qaa/fheq-2024/4.15.b8, the Annex D transferable strand qaa/fheq-2024/annex-d/transferable, spine:6 and 4.5.b10."
  author-agent-dialogue: "Raise it when a student prepares to speak to a non-academic audience. With a student, use plain second-person words and frame it as a skill employers and further study value; with staff, ask where the course teaches and assesses it. Ask: how would you explain your project to a classmate, an employer and a community group? Avoid reading the list aloud or treating it as a higher rung; it is part of the minimum."
- statement: qaa/sociology-2026/4.5.b4
  forPractitioner: { text: "At threshold, honours graduates should be able to use digital technology and skills in organising and presenting ideas.", rewrite: light, force: threshold, status: drafted }
  forBeneficiary: { text: "By the end of your degree you should be able to use digital tools to organise your ideas and present them.", rewrite: full, force: threshold, status: drafted }
  author-agent-written: "State this as a transferable skill the statement places among the honours threshold standards, at FHEQ level 6 (FQHEIS level 10): digital skills for organising and presenting ideas. Cite it as (QAA, 2026, Sociology Subject Benchmark Statement, para 4.5) and do not present it as subject-specific, as a regulatory requirement or as a master's outcome. Set it beside the generic level descriptor qaa/fheq-2024/annex-d/transferable/r1/3rd, the Annex D transferable strand qaa/fheq-2024/annex-d/transferable, spine:6 and 4.5.b9 and 4.5.b12."
  author-agent-dialogue: "Raise it when a student plans a digital output or organises research material. With a student, use plain second-person words and frame it as a skill employers and further study value; with staff, ask where the course teaches and assesses it. Ask: which digital tools do you use to organise and present your ideas, and could you teach one to a peer? Avoid reading the list aloud or treating it as a higher rung; it is part of the minimum."
- statement: qaa/sociology-2026/4.5.b5
  forPractitioner: { text: "At threshold, honours graduates should be able to demonstrate information retrieval and synthesis.", rewrite: light, force: threshold, status: drafted }
  forBeneficiary: { text: "By the end of your degree you should be able to find information and bring it together into a coherent whole.", rewrite: full, force: threshold, status: drafted }
  author-agent-written: "State this as a transferable skill the statement places among the honours threshold standards, at FHEQ level 6 (FQHEIS level 10): retrieving and synthesising information. Cite it as (QAA, 2026, Sociology Subject Benchmark Statement, para 4.5) and do not present it as subject-specific, as a regulatory requirement or as a master's outcome. Set it beside the generic level descriptor qaa/fheq-2024/4.15.b5, the Annex D transferable strand qaa/fheq-2024/annex-d/transferable, spine:6 and 4.4.b12."
  author-agent-dialogue: "Raise it when a student starts a literature search. With a student, use plain second-person words and frame it as a skill employers and further study value; with staff, ask where the course teaches and assesses it. Ask: how did you find your sources, and how have you combined them rather than listed them? Avoid reading the list aloud or treating it as a higher rung; it is part of the minimum."
- statement: qaa/sociology-2026/4.5.b6
  forPractitioner: { text: "At threshold, honours graduates should be able to discuss and present ideas with others clearly and with reasoning.", rewrite: light, force: threshold, status: drafted }
  forBeneficiary: { text: "By the end of your degree you should be able to discuss and present ideas with others clearly and with good reasons.", rewrite: full, force: threshold, status: drafted }
  author-agent-written: "State this as a transferable skill the statement places among the honours threshold standards, at FHEQ level 6 (FQHEIS level 10): clear, reasoned discussion with others. Cite it as (QAA, 2026, Sociology Subject Benchmark Statement, para 4.5) and do not present it as subject-specific, as a regulatory requirement or as a master's outcome. Set it beside the generic level descriptor qaa/fheq-2024/4.15.b8, the Annex D transferable strand qaa/fheq-2024/annex-d/transferable, spine:6 and 4.4.b3 and 4.5.b10."
  author-agent-dialogue: "Raise it when a student prepares for a seminar or group presentation. With a student, use plain second-person words and frame it as a skill employers and further study value; with staff, ask where the course teaches and assesses it. Ask: when you disagree in a seminar, how do you set out your reasons? Avoid reading the list aloud or treating it as a higher rung; it is part of the minimum."
- statement: qaa/sociology-2026/4.5.b7
  forPractitioner: { text: "At threshold, honours graduates should be able to demonstrate independent and group working.", rewrite: light, force: threshold, status: drafted }
  forBeneficiary: { text: "By the end of your degree you should be able to show you can work on your own and in a group.", rewrite: full, force: threshold, status: drafted }
  author-agent-written: "State this as a transferable skill the statement places among the honours threshold standards, at FHEQ level 6 (FQHEIS level 10): working alone and in groups. Cite it as (QAA, 2026, Sociology Subject Benchmark Statement, para 4.5) and do not present it as subject-specific, as a regulatory requirement or as a master's outcome. Set it beside the generic level descriptor qaa/fheq-2024/4.15.b9.1, the Annex D transferable strand qaa/fheq-2024/annex-d/transferable, spine:6 and 4.5.b11 and 4.5.b13."
  author-agent-dialogue: "Raise it when a student starts group work or an independent task. With a student, use plain second-person words and frame it as a skill employers and further study value; with staff, ask where the course teaches and assesses it. Ask: what do you do well on your own, and what do you add to a group? Avoid reading the list aloud or treating it as a higher rung; it is part of the minimum."
- statement: qaa/sociology-2026/4.5.b8
  forPractitioner: { text: "At threshold, honours graduates should understand how to apply research principles and practices ethically.", rewrite: light, force: threshold, status: drafted }
  forBeneficiary: { text: "By the end of your degree you should understand how to carry out research in an ethical way.", rewrite: full, force: threshold, status: drafted }
  author-agent-written: "State this as a transferable skill the statement places among the honours threshold standards, at FHEQ level 6 (FQHEIS level 10): applying research principles ethically. Cite it as (QAA, 2026, Sociology Subject Benchmark Statement, para 4.5) and do not present it as subject-specific, as a regulatory requirement or as a master's outcome. Set it beside the generic level descriptor qaa/fheq-2024/4.15.b9.2, the Annex D transferable strand qaa/fheq-2024/annex-d/transferable, spine:6 and the subject item 4.4.b16."
  author-agent-dialogue: "Raise it when a student designs a study or handles personal data. With a student, use plain second-person words and frame it as a skill employers and further study value; with staff, ask where the course teaches and assesses it. Ask: which ethical principle shaped a decision in your last piece of research? Avoid reading the list aloud or treating it as a higher rung; it is part of the minimum."
- statement: qaa/sociology-2026/4.5.b9
  forPractitioner: { text: "At threshold, honours graduates should be able to use AI and other digital technologies appropriately, including generative AI, and critically evaluate what they imply.", rewrite: light, force: threshold, status: drafted }
  forBeneficiary: { text: "By the end of your degree you should be able to use AI and other digital tools, including generative AI, in suitable ways and judge critically what they mean for your work and for society.", rewrite: full, force: threshold, status: drafted }
  author-agent-written: "State this as a transferable skill the statement places among the honours threshold standards, at FHEQ level 6 (FQHEIS level 10): using and evaluating AI and digital technology, including generative AI. Cite it as (QAA, 2026, Sociology Subject Benchmark Statement, para 4.5) and do not present it as subject-specific, as a regulatory requirement or as a master's outcome. Set it beside the generic level descriptor qaa/fheq-2024/annex-d/transferable/r1/3rd, the Annex D transferable strand qaa/fheq-2024/annex-d/transferable, spine:6 and 1.40, 1.41 and 4.5.b4."
  author-agent-dialogue: "Raise it when a student asks whether and how to use AI tools in their work. With a student, use plain second-person words and frame it as a skill employers and further study value; with staff, ask where the course teaches and assesses it. Ask: how did you use an AI tool in your last task, and what did you check or decide yourself? Avoid reading the list aloud or treating it as a higher rung; it is part of the minimum."
- statement: qaa/sociology-2026/4.5.b10
  forPractitioner: { text: "At threshold, honours graduates should be able to present knowledge or argument in a way others can understand.", rewrite: light, force: threshold, status: drafted }
  forBeneficiary: { text: "By the end of your degree you should be able to present what you know, or an argument, so that others can follow it.", rewrite: full, force: threshold, status: drafted }
  author-agent-written: "State this as a transferable skill the statement places among the honours threshold standards, at FHEQ level 6 (FQHEIS level 10): making knowledge and argument understandable. Cite it as (QAA, 2026, Sociology Subject Benchmark Statement, para 4.5) and do not present it as subject-specific, as a regulatory requirement or as a master's outcome. Set it beside the generic level descriptor qaa/fheq-2024/4.15.b8, the Annex D transferable strand qaa/fheq-2024/annex-d/transferable, spine:6 and 4.5.b3 and 4.5.b6."
  author-agent-dialogue: "Raise it when a student writes for a general audience. With a student, use plain second-person words and frame it as a skill employers and further study value; with staff, ask where the course teaches and assesses it. Ask: could someone outside the subject follow your main argument from your first page? Avoid reading the list aloud or treating it as a higher rung; it is part of the minimum."
- statement: qaa/sociology-2026/4.5.b11
  forPractitioner: { text: "At threshold, honours graduates should be able to show intellectual independence, taking on tasks with suitable guidance, doing self-directed research and showing critical judgement.", rewrite: light, force: threshold, status: drafted }
  forBeneficiary: { text: "By the end of your degree you should be able to think and work independently, with the right support, carry out your own research and use critical judgement.", rewrite: full, force: threshold, status: drafted }
  author-agent-written: "State this as a transferable skill the statement places among the honours threshold standards, at FHEQ level 6 (FQHEIS level 10): intellectual independence and critical judgement. Cite it as (QAA, 2026, Sociology Subject Benchmark Statement, para 4.5) and do not present it as subject-specific, as a regulatory requirement or as a master's outcome. Set it beside the generic level descriptor qaa/fheq-2024/4.15.b5 and qaa/fheq-2024/4.15.b9.1, the Annex D transferable strand qaa/fheq-2024/annex-d/transferable, spine:6 and the subject item 4.4.b17 and the master's item 4.6.b8.masters."
  author-agent-dialogue: "Raise it when a student moves to self-directed study. With a student, use plain second-person words and frame it as a skill employers and further study value; with staff, ask where the course teaches and assesses it. Ask: what did you decide for yourself in your last project, and where did you need guidance? Avoid reading the list aloud or treating it as a higher rung; it is part of the minimum."
- statement: qaa/sociology-2026/4.5.b12
  forPractitioner: { text: "At threshold, honours graduates should be able to use computer-based techniques for storing, collating and analysing both kinds of data.", rewrite: light, force: threshold, status: drafted }
  forBeneficiary: { text: "By the end of your degree you should be able to use computer tools to store, organise and analyse numerical and qualitative data.", rewrite: full, force: threshold, status: drafted }
  author-agent-written: "State this as a transferable skill the statement places among the honours threshold standards, at FHEQ level 6 (FQHEIS level 10): computer-aided data storage and analysis. Cite it as (QAA, 2026, Sociology Subject Benchmark Statement, para 4.5) and do not present it as subject-specific, as a regulatory requirement or as a master's outcome. Set it beside the generic level descriptor qaa/fheq-2024/annex-d/practical/r4/3rd, the Annex D transferable strand qaa/fheq-2024/annex-d/transferable, spine:6 and the subject item 4.4.b15."
  author-agent-dialogue: "Raise it when a student sets up data management for a project. With a student, use plain second-person words and frame it as a skill employers and further study value; with staff, ask where the course teaches and assesses it. Ask: where is your data stored, and which software will you analyse it with? Avoid reading the list aloud or treating it as a higher rung; it is part of the minimum."
- statement: qaa/sociology-2026/4.5.b13
  forPractitioner: { text: "At threshold, honours graduates should be able to collaborate, working in a group or team or taking part in discussion.", rewrite: light, force: threshold, status: drafted }
  forBeneficiary: { text: "By the end of your degree you should be able to work with others, in a team or in discussion.", rewrite: full, force: threshold, status: drafted }
  author-agent-written: "State this as a transferable skill the statement places among the honours threshold standards, at FHEQ level 6 (FQHEIS level 10): collaborative work in teams and discussion. Cite it as (QAA, 2026, Sociology Subject Benchmark Statement, para 4.5) and do not present it as subject-specific, as a regulatory requirement or as a master's outcome. Set it beside the generic level descriptor qaa/fheq-2024/annex-d/transferable/r2/3rd, the Annex D transferable strand qaa/fheq-2024/annex-d/transferable, spine:6 and 4.5.b7."
  author-agent-dialogue: "Raise it when a team task starts or stalls. With a student, use plain second-person words and frame it as a skill employers and further study value; with staff, ask where the course teaches and assesses it. Ask: what role did you take in your last group task, and what would you change? Avoid reading the list aloud or treating it as a higher rung; it is part of the minimum."
- statement: qaa/sociology-2026/4.5.b14
  forPractitioner: { text: "At threshold, honours graduates should be able to identify and examine underlying values and ethics, social and cultural as well as personal.", rewrite: light, force: threshold, status: drafted }
  forBeneficiary: { text: "By the end of your degree you should be able to identify and question the values and ethics behind culture, society and your own views.", rewrite: full, force: threshold, status: drafted }
  author-agent-written: "State this as a transferable skill the statement places among the honours threshold standards, at FHEQ level 6 (FQHEIS level 10): values and ethics in culture, society and self. Cite it as (QAA, 2026, Sociology Subject Benchmark Statement, para 4.5) and do not present it as subject-specific, as a regulatory requirement or as a master's outcome. Set it beside the generic level descriptor qaa/fheq-2024/4.15.b9.2, the Annex D transferable strand qaa/fheq-2024/annex-d/transferable, spine:6 and the subject item 4.4.b16 and 1.33 on reflective practice."
  author-agent-dialogue: "Raise it when a student reflects on their own position in a debate. With a student, use plain second-person words and frame it as a skill employers and further study value; with staff, ask where the course teaches and assesses it. Ask: which of your own values shaped how you read this evidence? Avoid reading the list aloud or treating it as a higher rung; it is part of the minimum."
- statement: qaa/sociology-2026/4.5.b15
  forPractitioner: { text: "At threshold, honours graduates should understand why wellbeing, mental health and emotions matter and how they bear on learning.", rewrite: light, force: threshold, status: drafted }
  forBeneficiary: { text: "By the end of your degree you should understand why your wellbeing, mental health and emotions matter and how they affect your learning.", rewrite: full, force: threshold, status: drafted }
  author-agent-written: "State this as a transferable skill the statement places among the honours threshold standards, at FHEQ level 6 (FQHEIS level 10): wellbeing, emotions and learning. Cite it as (QAA, 2026, Sociology Subject Benchmark Statement, para 4.5) and do not present it as subject-specific, as a regulatory requirement or as a master's outcome. Set it beside the generic level descriptor qaa/fheq-2024/annex-d/transferable/r5/3rd, the Annex D transferable strand qaa/fheq-2024/annex-d/transferable, spine:6 and 1.33 on reflective practice and emotional awareness."
  author-agent-dialogue: "Raise it when a student is struggling or talks about stress and study. With a student, use plain second-person words and frame it as a skill employers and further study value; with staff, ask where the course teaches and assesses it. Ask: what helps you learn well, and what gets in the way? Avoid reading the list aloud or treating it as a higher rung; it is part of the minimum."
- statement: qaa/sociology-2026/4.5.b16
  forPractitioner: { text: "At threshold, honours graduates should be able to use feedback appropriately to develop intellectually.", rewrite: light, force: threshold, status: drafted }
  forBeneficiary: { text: "By the end of your degree you should be able to use the feedback you receive to keep developing your thinking.", rewrite: full, force: threshold, status: drafted }
  author-agent-written: "State this as a transferable skill the statement places among the honours threshold standards, at FHEQ level 6 (FQHEIS level 10): using feedback for development. Cite it as (QAA, 2026, Sociology Subject Benchmark Statement, para 4.5) and do not present it as subject-specific, as a regulatory requirement or as a master's outcome. Set it beside the generic level descriptor qaa/fheq-2024/annex-d/transferable/r5/3rd, the Annex D transferable strand qaa/fheq-2024/annex-d/transferable, spine:6 and 3.22 on feedback."
  author-agent-dialogue: "Raise it when a student receives marked work. With a student, use plain second-person words and frame it as a skill employers and further study value; with staff, ask where the course teaches and assesses it. Ask: what one change will you make in your next piece of work because of this feedback? Avoid reading the list aloud or treating it as a higher rung; it is part of the minimum."
- statement: qaa/sociology-2026/4.6.b1.masters
  forPractitioner: { text: "Master's graduates should be able to synthesise theory, concepts and empirical research when they discuss contemporary social problems.", rewrite: light, force: should, status: drafted }
  forBeneficiary: { text: "By the end of your master's you should be able to bring theory, concepts and research findings together when you discuss current social problems.", rewrite: full, force: should, status: drafted }
  author-agent-written: "State this as an outcome a master's graduate in Sociology should be able to show at FHEQ level 7 (FQHEIS level 11), on top of the honours threshold: synthesising theory, concepts and empirical research on current problems. Cite it as (QAA, 2026, Sociology Subject Benchmark Statement, para 4.6) and do not apply it to the honours degree or call it a regulatory requirement; the statement sets it as an addition to the undergraduate threshold, not as a typical or excellent rung. Set it beside qaa/fheq-2024/4.17.b1, spine:7 and its nearest honours item 4.4.b12."
  author-agent-dialogue: "Raise it when a master's student frames a dissertation literature review. Put it to a master's student in plain second-person words, and to a master's team as what the award adds to honours. Ask: how do the theories and the empirical studies you cite fit together into one account of the problem? Avoid presenting it to an undergraduate as their minimum."
- statement: qaa/sociology-2026/4.6.b2.masters
  forPractitioner: { text: "Master's graduates should be able to show critical awareness of the historical, cultural, social, political and environmental settings and theories that shape the discipline.", rewrite: light, force: should, status: drafted }
  forBeneficiary: { text: "By the end of your master's you should be critically aware of the historical, cultural, political and environmental settings and theories that shape Sociology.", rewrite: full, force: should, status: drafted }
  author-agent-written: "State this as an outcome a master's graduate in Sociology should be able to show at FHEQ level 7 (FQHEIS level 11), on top of the honours threshold: critical awareness of the contexts and theories behind the subject. Cite it as (QAA, 2026, Sociology Subject Benchmark Statement, para 4.6) and do not apply it to the honours degree or call it a regulatory requirement; the statement sets it as an addition to the undergraduate threshold, not as a typical or excellent rung. Set it beside qaa/fheq-2024/4.17.b1, spine:7 and its nearest honours item 4.4.b1."
  author-agent-dialogue: "Raise it when a master's student situates their field historically or politically. Put it to a master's student in plain second-person words, and to a master's team as what the award adds to honours. Ask: which historical or political context most shaped the theory you rely on? Avoid presenting it to an undergraduate as their minimum."
- statement: qaa/sociology-2026/4.6.b3.masters
  forPractitioner: { text: "Master's graduates should be able to discuss critically the connections and overlaps between power imbalance, colonial legacies, inequity and injustice.", rewrite: light, force: should, status: drafted }
  forBeneficiary: { text: "By the end of your master's you should be able to discuss critically how unequal power, colonial histories and injustice connect and overlap.", rewrite: full, force: should, status: drafted }
  author-agent-written: "State this as an outcome a master's graduate in Sociology should be able to show at FHEQ level 7 (FQHEIS level 11), on top of the honours threshold: critical discussion of power, colonial legacies and injustice. Cite it as (QAA, 2026, Sociology Subject Benchmark Statement, para 4.6) and do not apply it to the honours degree or call it a regulatory requirement; the statement sets it as an addition to the undergraduate threshold, not as a typical or excellent rung. Set it beside qaa/fheq-2024/4.17.b4.1, spine:7 and its nearest honours item 4.4.b6."
  author-agent-dialogue: "Raise it when a master's student works on global inequality or decolonial theory. Put it to a master's student in plain second-person words, and to a master's team as what the award adds to honours. Ask: where do these forms of injustice overlap in your case, and which accounts handle the overlap best? Avoid presenting it to an undergraduate as their minimum."
- statement: qaa/sociology-2026/4.6.b4.masters
  forPractitioner: { text: "Master's graduates should be able to design and conduct sociological research using quantitative and qualitative sources.", rewrite: light, force: should, status: drafted }
  forBeneficiary: { text: "By the end of your master's you should be able to design and carry out sociological research using both numerical and qualitative sources.", rewrite: full, force: should, status: drafted }
  author-agent-written: "State this as an outcome a master's graduate in Sociology should be able to show at FHEQ level 7 (FQHEIS level 11), on top of the honours threshold: designing and carrying out research with both kinds of source. Cite it as (QAA, 2026, Sociology Subject Benchmark Statement, para 4.6) and do not apply it to the honours degree or call it a regulatory requirement; the statement sets it as an addition to the undergraduate threshold, not as a typical or excellent rung. Set it beside qaa/fheq-2024/4.17.b2, spine:7 and its nearest honours item 4.4.b14."
  author-agent-dialogue: "Raise it when a master's student plans fieldwork or analysis. Put it to a master's student in plain second-person words, and to a master's team as what the award adds to honours. Ask: what does each kind of source add to your design? Avoid presenting it to an undergraduate as their minimum."
- statement: qaa/sociology-2026/4.6.b5.masters
  forPractitioner: { text: "Master's graduates should be able to critically assess suitable methodologies for complex problems.", rewrite: light, force: should, status: drafted }
  forBeneficiary: { text: "By the end of your master's you should be able to judge critically which research methodologies suit complex problems.", rewrite: full, force: should, status: drafted }
  author-agent-written: "State this as an outcome a master's graduate in Sociology should be able to show at FHEQ level 7 (FQHEIS level 11), on top of the honours threshold: assessing methodologies for complex problems. Cite it as (QAA, 2026, Sociology Subject Benchmark Statement, para 4.6) and do not apply it to the honours degree or call it a regulatory requirement; the statement sets it as an addition to the undergraduate threshold, not as a typical or excellent rung. Set it beside qaa/fheq-2024/4.17.b4.2, spine:7 and its nearest honours item 4.4.b13."
  author-agent-dialogue: "Raise it when a master's student justifies a methodology. Put it to a master's student in plain second-person words, and to a master's team as what the award adds to honours. Ask: why does your methodology fit a problem this complex better than the alternatives? Avoid presenting it to an undergraduate as their minimum."
- statement: qaa/sociology-2026/4.6.b6.masters
  forPractitioner: { text: "Master's graduates should be able to discuss sensitive and ethical issues in sociological research.", rewrite: light, force: should, status: drafted }
  forBeneficiary: { text: "By the end of your master's you should be able to discuss the sensitive and ethical questions that come up in sociological research.", rewrite: full, force: should, status: drafted }
  author-agent-written: "State this as an outcome a master's graduate in Sociology should be able to show at FHEQ level 7 (FQHEIS level 11), on top of the honours threshold: sensitive and ethical issues in research. Cite it as (QAA, 2026, Sociology Subject Benchmark Statement, para 4.6) and do not apply it to the honours degree or call it a regulatory requirement; the statement sets it as an addition to the undergraduate threshold, not as a typical or excellent rung. Set it beside qaa/fheq-2024/4.17.b5, spine:7 and its nearest honours item 4.4.b16."
  author-agent-dialogue: "Raise it when a master's student plans research with vulnerable groups or on a sensitive topic. Put it to a master's student in plain second-person words, and to a master's team as what the award adds to honours. Ask: which sensitive issue in your study is hardest to resolve, and how will you handle it? Avoid presenting it to an undergraduate as their minimum."
- statement: qaa/sociology-2026/4.6.b7.masters
  forPractitioner: { text: "Master's graduates should be able to select and use suitable tools to collect and/or analyse both kinds of data, including software and basic statistical and interpretive procedures.", rewrite: light, force: should, status: drafted }
  forBeneficiary: { text: "By the end of your master's you should be able to choose and use the right tools, software and basic statistics to gather or analyse numerical and qualitative data.", rewrite: full, force: should, status: drafted }
  author-agent-written: "State this as an outcome a master's graduate in Sociology should be able to show at FHEQ level 7 (FQHEIS level 11), on top of the honours threshold: selecting and using research tools, software and statistics. Cite it as (QAA, 2026, Sociology Subject Benchmark Statement, para 4.6) and do not apply it to the honours degree or call it a regulatory requirement; the statement sets it as an addition to the undergraduate threshold, not as a typical or excellent rung. Set it beside qaa/fheq-2024/4.17.b2, spine:7 and its nearest honours item 4.4.b15."
  author-agent-dialogue: "Raise it when a master's student chooses analysis software or procedures. Put it to a master's student in plain second-person words, and to a master's team as what the award adds to honours. Ask: why did you choose this tool and procedure over others? Avoid presenting it to an undergraduate as their minimum."
- statement: qaa/sociology-2026/4.6.b8.masters
  forPractitioner: { text: "Master's graduates should be able to discuss and analyse complex concepts critically and work on their own with some originality.", rewrite: light, force: should, status: drafted }
  forBeneficiary: { text: "By the end of your master's you should be able to discuss and analyse complex ideas critically and work on your own with some originality.", rewrite: full, force: should, status: drafted }
  author-agent-written: "State this as an outcome a master's graduate in Sociology should be able to show at FHEQ level 7 (FQHEIS level 11), on top of the honours threshold: complex concepts; independent work with some originality. Cite it as (QAA, 2026, Sociology Subject Benchmark Statement, para 4.6) and do not apply it to the honours degree or call it a regulatory requirement; the statement sets it as an addition to the undergraduate threshold, not as a typical or excellent rung. Set it beside qaa/fheq-2024/4.17.b6, spine:7 and its nearest honours item 4.5.b11."
  author-agent-dialogue: "Raise it when a master's student moves from coursework to independent study. Put it to a master's student in plain second-person words, and to a master's team as what the award adds to honours. Ask: which idea in your work is your own contribution, and how did you reach it? Avoid presenting it to an undergraduate as their minimum."
- statement: qaa/sociology-2026/4.6.b9.masters
  forPractitioner: { text: "Master's graduates should be able to complete a research project that generates or reformulates data, informed by a critical understanding of the subject.", rewrite: light, force: should, status: drafted }
  forBeneficiary: { text: "By the end of your master's you should be able to complete a research project in which you produce or rework data, guided by a critical understanding of Sociology.", rewrite: full, force: should, status: drafted }
  author-agent-written: "State this as an outcome a master's graduate in Sociology should be able to show at FHEQ level 7 (FQHEIS level 11), on top of the honours threshold: completing a research project with original or reworked data. Cite it as (QAA, 2026, Sociology Subject Benchmark Statement, para 4.6) and do not apply it to the honours degree or call it a regulatory requirement; the statement sets it as an addition to the undergraduate threshold, not as a typical or excellent rung. Set it beside qaa/fheq-2024/4.17.b3, spine:7 and its nearest honours item 4.4.b17."
  author-agent-dialogue: "Raise it when a master's student begins the dissertation. Put it to a master's student in plain second-person words, and to a master's team as what the award adds to honours. Ask: what data will you generate or reshape, and what understanding of the field guides that? Avoid presenting it to an undergraduate as their minimum."
- statement: qaa/sociology-2026/4.6.b10.masters
  forPractitioner: { text: "Master's graduates should be able to critically evaluate social policies and interventions using social theories, frameworks and evidence.", rewrite: light, force: should, status: drafted }
  forBeneficiary: { text: "By the end of your master's you should be able to judge social policies and interventions critically using social theory, frameworks and evidence.", rewrite: full, force: should, status: drafted }
  author-agent-written: "State this as an outcome a master's graduate in Sociology should be able to show at FHEQ level 7 (FQHEIS level 11), on top of the honours threshold: evaluating policies and interventions with theory and evidence. Cite it as (QAA, 2026, Sociology Subject Benchmark Statement, para 4.6) and do not apply it to the honours degree or call it a regulatory requirement; the statement sets it as an addition to the undergraduate threshold, not as a typical or excellent rung. Set it beside qaa/fheq-2024/4.17.b5, spine:7 and its nearest honours item 4.4.b18."
  author-agent-dialogue: "Raise it when a master's student studies a policy or intervention. Put it to a master's student in plain second-person words, and to a master's team as what the award adds to honours. Ask: which theory and which evidence would you use to judge whether this policy works, and for whom? Avoid presenting it to an undergraduate as their minimum."
```

### S5 Levels and alignment
<!-- label: both; status: drafted; basis: primary -->
```yaml
levels:
  - { id: "fheq:4", role: "cites", locator: "D1, 2.8" }
  - { id: "fheq:5", role: "cites", locator: "D1, 2.8" }
  - { id: "fheq:6", role: "cites", locator: "D1, 2.5; the honours threshold 4.1, 4.4, 4.5" }
  - { id: "fheq:7", role: "cites", locator: "D1, 2.5 (integrated master's); 4.6 by award (inferred: the paragraph names no level)" }
  - { id: "fqheis:8", role: "cites", locator: "D1, 2.8 (as stated for the CertHE: Part E)" }
  - { id: "fqheis:9", role: "cites", locator: "D1, 2.8 (as stated for the DipHE: Part E); 2.10 (ordinary degree)" }
  - { id: "fqheis:10", role: "cites", locator: "D1, 2.5; 2.10" }
  - { id: "fqheis:11", role: "cites", locator: "D1, 2.5" }
  - { id: "spine:6", role: "refers", locator: "std:ref:uk-framework R2, R8 (inferred: the honours items set beside it)" }
  - { id: "spine:7", role: "refers", locator: "std:ref:uk-framework R2, R8 (inferred: the master's items set beside it)" }
crosswalks:
  - { from: "fheq:6", to: "fqheis:10", relation: "equivalent", basis: "stated (D1, 2.5: undergraduate degree with honours); agrees with FHEQ Table 1" }
  - { from: "fheq:7", to: "fqheis:11", relation: "equivalent", basis: "stated (D1, 2.5: integrated master's); agrees with FHEQ Table 1" }
  - { from: "fheq:4", to: "fqheis:8", relation: "equivalent", basis: "stated (D1, 2.8: CertHE); conflicts with FHEQ Table 1, which places the CertHE at SCQF 7 (Part E)" }
  - { from: "fheq:5", to: "fqheis:9", relation: "equivalent", basis: "stated (D1, 2.8: DipHE); conflicts with FHEQ Table 1, which places the DipHE at SCQF 8 (Part E)" }
```

### S6 Themes
<!-- label: both; status: drafted; basis: primary -->
```yaml
- { id: "theme:edi", role: "carries", carriedIn: ["1.6", "1.7", "1.8", "1.24", "1.29", "3.14", "3.15"] }
- { id: "theme:accessibility", role: "carries", carriedIn: ["1.8", "1.9", "1.10", "1.11", "1.12", "3.5", "3.14", "3.21"] }
- { id: "theme:esd", role: "carries", carriedIn: ["1.13", "1.14", "1.15", "1.16", "1.17", "1.18"] }
- { id: "theme:internationalisation", role: "carries", carriedIn: ["1.19", "1.20", "1.21", "1.22", "1.23", "1.24", "1.25", "1.26"] }
- { id: "theme:enterprise", role: "carries", carriedIn: ["1.27", "1.28", "1.29", "1.30", "1.31", "1.32", "1.33", "1.34", "3.19"] }
- { id: "theme:generative-ai", role: "carries", carriedIn: ["1.34", "1.35", "1.36", "1.37", "1.38", "1.39", "1.40", "1.41", "3.6", "3.10", "3.15", "4.5"] }
```

### S7 Relations
<!-- label: both; status: drafted; basis: primary -->
```yaml
- { rel: "partOf", target: "collection: QAA Subject Benchmark Statements", note: "one of 54 held by stan" }
- { rel: "supersedes", target: "std:doc:qaa-sociology-2019-benchmarks (not yet ingested)", note: "back matter: the fourth edition, 2019, a minor update of 2016; this is the fifth edition" }
- { rel: "refersTo", target: "std:doc:qaa-fheq-2024-framework, Annex D", note: "4.2: the four honours classifications; the statement sets no rung above threshold" }
- { rel: "refersTo", target: "std:doc:qaa-fheq-2024-framework", note: "levels 4 to 7 (2.5, 2.8)" }
- { rel: "refersTo", target: "std:doc:qaa-fqheis-2024-framework", note: "levels 8 to 11, named SCQF/FQHEIS (2.5, 2.8, 2.10)" }
- { rel: "refersTo", target: "std:doc:qaa-advancehe-esd-2021-guidance", note: "1.18 (the three-fold focus); section 5" }
- { rel: "refersTo", target: "std:doc:qaa-enterprise-2018-guidance", note: "section 5 only" }
- { rel: "refersTo", target: "QAA Quality Code (2024 update) (not yet ingested)", note: "front matter" }
- { rel: "refersTo", target: "Equality Act 2010 (law)", note: "4.3: competence standards" }
- { rel: "refersTo", target: "Equality and Human Rights Commission guidance on competence standards (not yet ingested)", note: "4.3" }
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
- The study of how people shape and are shaped by their social world and their relations with others, drawing on evidence to inform action on social issues from local to global (D1, 1.1).
- A core social science that joins theory and evidence, so that students learn to apply and test both theories and methods (D1, 1.2, 2.2, 3.1).
- Explains inequality through social structures and drivers rather than individual choice; questions of equity, diversity and inclusion are central to it (D1, 1.6, 3.3).
- Ranges across time, place and scale, from macro structures to face-to-face interaction, and uses quantitative, qualitative, mixed and creative methods (D1, 3.2, 3.3).
- Three interlinked purposes, academic, vocational and professional, which feed one another (D1, 1.4, 1.5).
- Reflexive about its own canon: it asks students to question historically dominant theories, to look beyond European founding figures and to consider colonial legacies (D1, 1.8, 1.19, 3.11).
- Has no accrediting body; works with professional associations (D1, 2.13).

### SB2 Themes in this subject
<!-- label: both; status: drafted; basis: primary -->
```yaml
- theme: theme:edi
  inThisSubject: "central to the discipline, which studies stratification and unequal access to wealth and power and their intersections; expected in every curriculum, with safe handling of contested topics and equal respect in all settings (D1, 1.6 to 1.8)"
  statements: ["qaa/sociology-2026/1.6", "qaa/sociology-2026/1.7", "qaa/sociology-2026/1.8"]
- theme: theme:accessibility
  inThisSubject: "designed in from admission to assessment so that adjustments are rarely needed; digital access, accessible rooms and language that does not make disabled people the object of study (D1, 1.9 to 1.12, 3.14, 3.21)"
  statements: ["qaa/sociology-2026/1.9", "qaa/sociology-2026/1.10", "qaa/sociology-2026/1.12", "qaa/sociology-2026/3.14"]
- theme: theme:esd
  inThisSubject: "a critical lens on environmental integrity, social justice and prosperity, with a critique of the SDGs as well as engagement with them; ESD through teaching and assessment, not content alone (D1, 1.13 to 1.18)"
  statements: ["qaa/sociology-2026/1.18"]
- theme: theme:internationalisation
  inThisSubject: "widening theory beyond European founders, critiquing Western knowledge, routes through guests, mobility, Global South partners, students' own backgrounds and online collaboration (D1, 1.19 to 1.26)"
  statements: ["qaa/sociology-2026/1.21.b1", "qaa/sociology-2026/1.21.b2", "qaa/sociology-2026/1.21.b3", "qaa/sociology-2026/1.21.b4", "qaa/sociology-2026/1.21.b5", "qaa/sociology-2026/1.25"]
- theme: theme:enterprise
  inThisSubject: "named employability, entrepreneurship and enterprise education; the subject's research and critical skills as employability, delivered with careers services and outside partners (D1, 1.27 to 1.34, 3.19)"
  statements: ["qaa/sociology-2026/1.33"]
- theme: theme:generative-ai
  inThisSubject: "AI treated as both a tool and a social reality to study critically (power, bias, environmental cost, authorship); critical use in teaching and assessment within institutional policy; one transferable skill (D1, 1.35 to 1.41, 3.10, 3.15, 4.5)"
  statements: ["qaa/sociology-2026/1.40", "qaa/sociology-2026/4.5.b9"]
```

### SB3 Content and delivery
<!-- label: both; status: drafted; basis: primary -->
```yaml
areas:
  - { component: "3.1", gloss: "a theoretical and empirical discipline, from the local to the global" }
  - { component: "3.2", gloss: "historical, cross-cultural and transnational range, or one present-day setting" }
  - { component: "3.3", gloss: "seven approaches: agency in context, macro and micro, data across methods, unequal distribution, norms and roles, change, global challenges" }
  - { component: "3.4", gloss: "six typical areas: structure and agency, social constructions, group relations, communication and technology, evidence-based research, research ethics" }
practices:
  - { component: "3.8", kind: "learning", gloss: "interaction with staff and peers, independent study, formative assessment" }
  - { component: "3.9", kind: "teaching", gloss: "lectures, seminars, workshops, lab classes, tutorials, visits, projects; flipped classrooms" }
  - { component: "3.10", kind: "teaching", gloss: "digital tools and AI in teaching, with critical attention to their effects" }
  - { component: "3.11", kind: "teaching", gloss: "ten features: scaffolded theory, guided study, enquiry-led groups, decolonisation, group work, debate, positionality, research projects, experiential learning, applied practice" }
  - { component: "3.13", kind: "assessment", gloss: "decolonising assessment; different ways of knowing" }
  - { component: "3.15", kind: "assessment", gloss: "posters, pitches, autoethnography, reflective and group work, essays, exams; digital forms" }
  - { component: "3.16", kind: "assessment", gloss: "authentic outputs such as stakeholder reports and consultation responses" }
  - { component: "3.17", kind: "assessment", gloss: "practical research exercises from framing questions to communicating findings" }
  - { component: "3.21", kind: "assessment", gloss: "five accessible design features: choice, clear guidance, continuous assessment, flexibility, digital platforms" }
  - { component: "3.22", kind: "assessment", gloss: "feedback that feeds forward; audio, video and peer feedback" }
```

### SB4 Benchmark standards
<!-- label: both; status: drafted; basis: primary -->
```yaml
rungs:
  - { rung: "threshold", leadIn: "4.4", award: "bachelor's with honours", items: 18 }
  - { rung: "threshold", leadIn: "4.5", award: "bachelor's with honours", items: 16 }
  - { rung: "threshold", leadIn: "4.6", award: "master's", items: 10 }
rungBases: "4.1: the threshold is the minimum for the honours award; 4.2: most students will do significantly better, with classification left to Annex D. No typical or excellent rung is stated. 4.6 adds a master's list to the undergraduate threshold: another award, recorded as rung threshold (BM-BRIEF convention)."
outcomeLists: []
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
- { body: "British Sociological Association", says: "a professional association providers work with to meet social and educational needs; not an accrediting body (D1, 2.13)", requirements: "none: the statement says no body accredits Sociology degrees (Part E)" }
- { body: "European Sociological Association", says: "a professional association providers work with, and a source of resources for an international curriculum (D1, 1.19, 2.13)", requirements: "none: no degree requirements (Part E)" }
- { body: "International Sociological Association", says: "as the European association: partner and source of international curriculum resources (D1, 1.19, 2.13)", requirements: "none: no degree requirements (Part E)" }
- { body: "Equality and Human Rights Commission", says: "its latest guidance is to be followed by a provider that sets competence standards (D1, 4.3; named there as the Equality and Human Right Commission)", requirements: "not yet ingested: listed in Part E" }
- { body: "professional, statutory and regulatory bodies (generic)", says: "may use the statement for their own definitions of standards; their requirements may inform competence standards (D1, front matter, 4.3)", requirements: "not-applicable: none is named for the subject (Part E)" }
- { body: "Office for Students", says: "in England the statement is not one of the sector-recognised standards under its regulatory framework (D1, front matter)", requirements: "not yet ingested: listed in Part E" }
- { body: "Advance HE", says: "co-author of the ESD guidance and source of material on flipped classrooms (D1, 1.18, 3.9)", requirements: "not-applicable: guidance, not requirements (Part E)" }
```

### SB6 Cross-cutting references
<!-- label: both; status: drafted; basis: primary -->
```yaml
themes:
  - { id: "theme:edi", named: "Equity, diversity and inclusion (EDI)", carriedIn: ["1.6", "1.7", "1.8", "1.24", "1.29", "3.14", "3.15"], statements: ["1.6", "1.7", "1.8", "3.14"] }
  - { id: "theme:accessibility", named: "Accessibility and the needs of disabled students", carriedIn: ["1.8", "1.9", "1.10", "1.11", "1.12", "3.5", "3.14", "3.21"], statements: ["1.9", "1.10", "1.12", "3.14"] }
  - { id: "theme:esd", named: "Education for sustainable development (ESD)", carriedIn: ["1.13", "1.14", "1.15", "1.16", "1.17", "1.18"], statements: ["1.18"] }
  - { id: "theme:internationalisation", named: "Internationalisation", carriedIn: ["1.19", "1.20", "1.21", "1.22", "1.23", "1.24", "1.25", "1.26"], statements: ["1.21.b1", "1.21.b2", "1.21.b3", "1.21.b4", "1.21.b5", "1.25"] }
  - { id: "theme:enterprise", named: "Employability, entrepreneurship and enterprise education (EEE)", carriedIn: ["1.27", "1.28", "1.29", "1.30", "1.31", "1.32", "1.33", "1.34", "3.19"], statements: ["1.33"] }
  - { id: "theme:generative-ai", named: "Generative artificial intelligence (GenAI)", carriedIn: ["1.34", "1.35", "1.36", "1.37", "1.38", "1.39", "1.40", "1.41", "3.6", "3.10", "3.15", "4.5"], statements: ["1.40", "4.5.b9"] }
frameworks:
  - { framework: "fheq", levels: ["fheq:4", "fheq:5", "fheq:6", "fheq:7"], citedIn: ["2.5", "2.8"] }
  - { framework: "scqf", levels: ["fqheis:8", "fqheis:9", "fqheis:10", "fqheis:11"], citedIn: ["2.5", "2.8", "2.10"] }
bodies:
  - { body: "British Sociological Association", citedIn: ["2.13"] }
  - { body: "European Sociological Association", citedIn: ["1.19", "2.13"] }
  - { body: "International Sociological Association", citedIn: ["1.19", "2.13"] }
  - { body: "Equality and Human Rights Commission", citedIn: ["4.3"] }
  - { body: "professional, statutory and regulatory bodies (PSRBs)", citedIn: ["front matter", "4.3"] }
  - { body: "Office for Students", citedIn: ["front matter"] }
  - { body: "Advance HE", citedIn: ["1.18", "3.9"] }
sharedDocuments:
  - { document: "std:doc:qaa-fheq-2024-framework, Annex D", named: "Annex D in The Frameworks for Higher Education Qualifications of UK Degree-Awarding Bodies", citedIn: ["4.2"], role: "descriptions of the four honours classifications, for achievement above the threshold" }
  - { document: "std:doc:qaa-advancehe-esd-2021-guidance", named: "the QAA/Advance HE guidance on ESD", citedIn: ["1.18"], role: "the three-fold focus: ways of thinking, practising and being" }
  - { document: "std:doc:qaa-enterprise-2018-guidance", named: "QAA (2018) Enterprise and Entrepreneurship Education", citedIn: ["section 5 (references)"], role: "further reading for the EEE theme; not cited in the body" }
  - { document: "QAA Quality Code, 2024 update (not yet ingested: Part E)", named: "an update to the Quality Code", citedIn: ["front matter"], role: "helpful alongside the statement" }
  - { document: "QAA Glossary (not ingested: Part E)", named: "QAA's Glossary", citedIn: ["front matter"], role: "explains unfamiliar terms" }
  - { document: "UN Sustainable Development Goals (external)", named: "the 2015 United Nations Sustainable Development Goals (SDGs)", citedIn: ["1.17"], role: "a frame for ESD that the subject also critiques" }
  - { document: "Equality Act 2010 (law)", named: "the Equality Act 2010", citedIn: ["4.3"], role: "defines competence standards" }
```

## Part B Terminology
<!-- The statement has no glossary of its own unless Part E says so; these are terms it defines in its text. -->

### B1 Concepts
<!-- label: both; status: drafted; basis: primary -->
```yaml
- { slug: "threshold-standard", definition: "the minimum a student should have shown to be awarded the honours degree (D1, 4.1)", beneficiaryDefinition: "the least you need to have shown to gain your degree", scopeNote: "most students exceed it (4.2); not a competence standard (4.3)", category: "unknown", practices: ["education"] }
- { slug: "transferable-skills", definition: "in this statement, skills not tied to technical or subject knowledge that let graduates adapt, create and contribute beyond the discipline (D1, 4.5)", beneficiaryDefinition: "skills you can carry from your subject into other work and study", scopeNote: "the issuer's wording ('non-technical or subject knowledge related') is ambiguous: Part E", category: "unknown", practices: ["education"] }
- { slug: "education-for-sustainable-development", definition: "building curriculum structures and subject content that support and enact sustainable development (D1, 1.13)", scopeNote: "sustainable development itself defined there as an aspirational, ongoing process", category: "unknown", practices: ["education"] }
- { slug: "internationalisation", definition: "a strategic commitment to help students understand the varied ways the subject engages with social issues, locally and globally (D1, 1.19)", category: "unknown", practices: ["education"] }
- { slug: "eee-education", definition: "education that builds the behaviours, attributes and competencies affecting a student's choice of employment and later career success (D1, 1.27)", scopeNote: "employability, enterprise and entrepreneurship education", category: "unknown", practices: ["education"] }
- { slug: "generative-ai", definition: "text- and image-based probability models that produce content in answer to prompts (D1, 1.35)", category: "unknown", practices: ["education"] }
- { slug: "competence-standard", definition: "a standard as the Equality Act 2010 defines it, which a provider may choose to set in a programme specification (D1, 4.3)", scopeNote: "the threshold standards are not competence standards", category: "unknown", practices: ["education"] }
```

### B2a Terms as the issuer defines them
<!-- label: source; status: drafted; basis: primary -->
```yaml
- { concept: "threshold-standard", form: "minimum threshold standards", lang: "en", partOfSpeech: "noun-phrase", termStatus: "preferred", register: "formal" }
- { concept: "transferable-skills", form: "transferable skills", lang: "en", partOfSpeech: "noun-phrase", termStatus: "preferred", register: "formal" }
- { concept: "education-for-sustainable-development", form: "Education for Sustainable Development", lang: "en", partOfSpeech: "noun-phrase", termStatus: "preferred", register: "formal" }
- { concept: "education-for-sustainable-development", form: "ESD", lang: "en", partOfSpeech: "noun", termStatus: "admitted", register: "formal" }
- { concept: "internationalisation", form: "internationalisation", lang: "en", partOfSpeech: "noun", termStatus: "preferred", register: "formal" }
- { concept: "eee-education", form: "EEE education", lang: "en", partOfSpeech: "noun-phrase", termStatus: "preferred", register: "formal" }
- { concept: "generative-ai", form: "Generative AI", lang: "en", partOfSpeech: "noun-phrase", termStatus: "preferred", register: "formal" }
- { concept: "generative-ai", form: "GenAI", lang: "en", partOfSpeech: "noun", termStatus: "admitted", register: "formal" }
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
  title: "Subject Benchmark Statement: Sociology"
  edition: "April 2026 (fifth edition)"
  year: 2026
  url: unknown (the QAA page; the text came by stan's extraction)
  retrieved: "held from stan: wkspc2615-QAAVector mapped/sociology-2026/sociology-2026.raw.txt, commit 366bcb99a01118f2c4c3ebfa2a8337596bddc455; received 2026-10-03"
  licence: QAA copyright
  tier: primary
  readVia: direct
  held: 77725c932f691e154481d14f48fd597208986236aec92bd6dfd1314bd9ef1147
  heldFiles: ["wkspc2601-library/txt/qaa-2026-sociology-subject-benchmark-statement-standard.txt", "wkspc2601-library/txt/qaa-2026-sociology-subject-benchmark-statement-standard.norm.txt", "wkspc2601-library/records/qaa-2026-sociology-subject-benchmark-statement-standard.chunks.json", "wkspc2601-library/records/qaa-2026-sociology-subject-benchmark-statement-standard.held.json"]
  citedIn: [S1, S2, S3, S4, S4a, S5, S6, S7, SB1, SB2, SB3, SB4, SB5, SB6]
```

### D2 Research log
```yaml
- { ref: D1, tier: primary, consulted: 2026-10-03, pass: P1, outcome: "read whole, direct, from the normalised text; skeleton by tools/std_prep.py, document by tools/bm_build.py" }
- { ref: "ADAPT subj HESA stores, cah.json and hecos.json (designs/ingest/standards/subj/vocab)", tier: primary, consulted: 2026-10-03, pass: P1, outcome: "codes for statedSubjects and subjects" }
```

### D3 Wanted sources
```yaml
- { w: "W-std-0083", source: "Equality and Human Rights Commission, the most recent guidance on competence standards", why: "4.3 sends providers that set competence standards to it", citedIn: ["4.3"] }
- { w: "W-std-0099", source: "QAA Subject Benchmark Statement: Sociology, fourth edition (2019)", why: "the edition this one supersedes, for a comparison of the standards", citedIn: ["S7"] }
```

## Part E Gaps and questions
- Rungs: threshold only. 4.4 (18 subject items) and 4.5 (16 transferable skills) sit under the heading "Threshold level"; no typical or excellent rung is stated, and 4.2 leaves achievement above the threshold to Annex D. Differs from Psychology, which has three rungs.
- Force of the honours lists: recorded as threshold because 4.1 defines them as the minimum a student should have shown for the honours award (forceFrom 4.1). The lead-in 4.4 says 'should be able to'; 4.5 has no modal ('These skills include an ability to'). For P3.
- Master's list 4.6: a separate list for a master's degree 'in addition to the undergraduate threshold benchmark statements', recorded as rung threshold, award master's, level fheq:7 and ids with the .masters suffix (BM-BRIEF convention). The paragraph names no level: fheq:7 is inferred from the award (FHEQ Table 1). Force should, the lead-in's word: the statement does not call this list a minimum.
- No gradeOf links: one rung per award. Honours-to-master's pairs that plainly match are named in the agent instructions only (for example 4.4.b6 and 4.6.b3.masters; 4.4.b17 and 4.6.b9.masters); they are not gradeOf links because the award differs.
- Crosswalk conflict (2.8): the statement places the CertHE at 'FHEQ Level 4; FQHEIS Level 8' and the DipHE at 'FHEQ Level 5; FQHEIS Level 9'. FHEQ Table 1 (std:doc:qaa-fheq-2024-framework, S5) puts the CertHE at SCQF 7 and the DipHE at SCQF 8. Recorded as stated in S5 and SB6; flagged for P3 and for the issuer.
- Cross-reference fault (1.34.b6): 'see paragraphs 1.36- 1.42'; the GenAI section runs 1.35 to 1.41 and there is no 1.42. Not cut as a statement (DPN-1).
- Obliging words outside the five: 1.6 'there is an expectation that' (describes); 2.1 'are expected to' (describes); 3.20 'important' and 'essential' (describes); 1.7 'Legislation requires' (must, plain); 1.25 'Internationalisation requires' (must; a condition of the aim rather than a rule, for P3).
- Not cut as statements (will or would used for prediction or description, not an expected outcome): 1.31, 1.37, 1.39, 2.5, 2.6, 2.14, 2.16; 4.1 is the rung definition, read for force. For P3.
- Plain-present provider norms not cut (template open point 5): 1.9's first sentence, 1.34 (eight capabilities courses 'facilitate opportunities' to learn), 2.12, 2.13, 3.5, 3.6, 3.11 items b2, b3, b5 to b10, 3.17, 3.21. Listed for Abbott.
- 1.21: the should sits in the stem; each of the five items is recorded under it as one route (forceFrom 1.21), following the one-record-per-item rule. The items are examples ("including"), so the duty is to the set, not to each one: for P3.
- 4.4.b11 runs two clauses together without a joining word ('...global and local forces promote opportunities to contribute...'); recorded whole, paraphrase reads both parts.
- 4.6.b9 reads 'the generation of reformulation of data', most likely a slip for 'or'; recorded as the text has it.
- 4.6.b8 joins a subject skill (complex concepts) and a generic one (independent, original work); domain subject-skill chosen; generic part noted.
- 4.5's definition of transferable skills ('non-technical or subject knowledge related') reads as the opposite of its likely meaning; B1 glosses the likely sense, for P3.
- 4.3 names the 'Equality and Human Right Commission' (sic).
- Skeleton corrections: spans of 4.4.b18 and 4.5.b16 carried the next heading ("Transferable skills"; "Master's level study"); spans of paragraph statements carried trailing sub-headings and were cut at the last full stop (find). 4.6 items re-keyed .masters. The skeleton's 10 threshold rung hits (4.6) are the master's list; its theme hits on 1.5, 1.12 and 1.26 are sub-heading text bleeding into the paragraph and were dropped.
- New theme ids: theme:internationalisation (a sixth cross-cutting theme, new to the shared list) and theme:generative-ai (the batch-1 id). The statement names six themes in its front matter; Psychology had four.
- Subject codes: CAH15-01 (sociology, social policy and anthropology) is inferred from the HESA parent of CAH15-01-02; held back from lookups until P3. CAH15 (social sciences) is stated: the text calls Sociology a core social science (1.2, 2.3).
- SB5: no body requirements are ingested. The BSA, ESA and ISA set no degree requirements (2.13 says no body accredits Sociology degrees); the EHRC guidance (4.3) and the OfS framework (front matter) are not yet ingested (D3). UNHCR and WHO (1.22) are named as data sources for teaching, not as bodies, and are not recorded in SB5.
- Excluded matter: the references list (section 5) is read for S7 and SB6 only; std:doc:qaa-enterprise-2018-guidance is cited there and nowhere in the body.
- Edition: the back matter calls this the fifth edition, published 16 April 2026, and names the 2019 fourth edition (minor update of 2016) and the 2007 and 2002 groups; supersedes is recorded from the back matter.
- Patterns that differ from Psychology: threshold only, split into subject and transferable lists under one rung heading; a master's list added on top of honours; six cross-cutting themes, including internationalisation; no PSRB; a stated crosswalk at levels 4 and 5 that conflicts with the FHEQ.
- ST-12: versions here run to the lengths the content needs; no length range is yet set.

---

## Change notes
- 0.1.2, 3 October 2026, 21:02: moved with its held text from UNI to the source library repo (`wkspc2601-library/ingested/standards/`, texts in `txt/`, records in `records/`); paths only (Abbott, 20:56; std N-0119).
- 0.1.1, 3 October 2026, 20:20: obliging words outside the five read as must, "ought to" as should, on statements outside the rungs, each marked on its force line (Abbott, 20:17; D-std-0016).
- 0.1.0, 2026-10-03 18:40: researched by run frame 0.1.1-draft and standards run layer 0.7.0-draft, std, run 0131 (P1); built by tools/bm_build.py.
